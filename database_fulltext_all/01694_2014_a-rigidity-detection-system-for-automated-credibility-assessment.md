---
otero_id: 1694
otero_key: "5HVKFQ4K"
title: "A Rigidity Detection System for Automated Credibility Assessment"
authors: "Nathan W. Twyman; Aaron C. Elkins; Judee K. Burgoon; Jay F. Nunamaker"
year: "2014"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222310108"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Rigidity Detection System for Automated Credibility Assessment

Nathan W. Twyman , Aaron C. Elkins , Judee K. Burgoon & Jay F. Nunamaker

To cite this article: Nathan W. Twyman , Aaron C. Elkins , Judee K. Burgoon & Jay F. Nunamaker (2014) A Rigidity Detection System for Automated Credibility Assessment, Journal of Management Information Systems, 31:1, 173-202

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222310108

![](/api/attachments/5HVKFQ4K/fulltext/images/57da47b79e509e3d74c3143ab31474044d887171b5175a8e7323b86806022192.jpg)

Published online: 05 Dec 2014.

![](/api/attachments/5HVKFQ4K/fulltext/images/9d530ee2a16cdadbf0b967991a0945ab4454a12b0e2a4fbd17327601b947f134.jpg)

Submit your article to this journal

![](/api/attachments/5HVKFQ4K/fulltext/images/b9667e5bd65f68e247e89a81d3f1829c94f8de00c5b5e74a795d02a7ddab8a93.jpg)

Article views: 33

![](/api/attachments/5HVKFQ4K/fulltext/images/7ccba3d381095d84fb1a281ee3d43561902cd3e1001e3bfdb5706b5455389c47.jpg)

View related articles

![](/api/attachments/5HVKFQ4K/fulltext/images/16be293691ce2930ed4d2779f1b1d8a1e95ef45a794036ed4c644ca2a7730fac.jpg)

View Crossmark data

![](/api/attachments/5HVKFQ4K/fulltext/images/9f30b9d914546a5ef00f23a2fe293f86945a9a3ace81b4e8ee3742f6120895b5.jpg)

Citing articles: 1 View citing articles

# A Rigidity Detection System for Automated Credibility Assessment

Na than W. Tw yman , Aa ron C. Elkins , Jude K. Burgon , and Ja y F. Nunam ke r Jr.

Nathan W. Tw yman is a postdoctoral research scientist in the MIS Department at the University of Arizona, where he received his Ph.D. in MIS. His research interests span human–computer interaction, group support systems, virtual communities, health IS, and leveraging human and organizational factors in auditing, security, and forensic investigation systems. He has published articles in the Journal of Management Information Systems, Journal of the Association for Information Systems, and Information & Management.

Aaron C. Elkin s is a postdoctoral researcher in both the MIS Department at the University of Arizona and the Department of Computing at Imperial College London. He holds a Ph.D. in MIS from the University of Arizona. He investigates how the voice, face, body, and language reveal emotion, deception, and cognition for advanced human–computer interaction and artificial intelligence applications. Complementary to the development of advanced artificial intelligence systems is their impact on the people using them to make decisions. Dr. Elkins also investigates how human decision makers are psychologically affected by, use, perceive, and incorporate the next generation of screening technologies into their lives.

Jude K. Burgoon is a professor of communications, a professor of family studies and human development, the director of human communication research for the Center for the Management of Information, and the site director of the Center for Identification Technology Research at the University of Arizona. She holds a Ph.D. in communication and educational psychology from West Virginia University. Her research interests are in deception, trust, interpersonal interaction, and new technologies.

Jay F. Nun amake r Jr. is Regents and Soldwedel Professor of MIS, Computer Science and Communication and Director of the Center for the Management of Information and the National Center for Border Security and Immigration at the University of Arizona. He received his Ph.D. in operations research and systems engineering from Case Institute of Technology, an M.S. and B.S. in engineering from the University of Pittsburgh, and a B.S. from Carnegie Mellon University. He received his professional engineer’s license in 1965. Dr. Nunamaker was inducted into the Design Science Hall of Fame in May 2008 and received the LEO Award for Lifetime Achievement from the Association for Information Systems (AIS) in December 2002 and was elected a fellow of the AIS in 2000. He was featured in the July 1997 issue of Forbes Magazine on technology as one of eight key innovators in information technology. He is widely published, with an H  index of 60. His specialization is in the fields of system analysis and design, collaboration technology, and deception detection. The commercial product GroupSystems’ ThinkTank, based on Dr. Nunamaker’s research, is often referred to as the gold standard for structured collaboration systems. He was a research assistant funded by the ISDOS project at the University of Michigan and an associate professor of computer science at Purdue University. He founded the MIS Department at the University of Arizona in 1974 and served as department head for 18 years.

Ab strac t: Credibility assessment is an area in which information systems research can make a major impact. This paper reports on two studies investigating a system solution for automatic, noninvasive detection of rigidity for automated interviewing. Kinesic rigidity has long been a phenomenon of interest in the credibility assessment literature, but until now was infeasible as a veracity indicator in practical use cases. An initial study unexpectedly revealed the occurrence of rigidity in a highly controlled concealed information test setting, prompting the design and implementation of an automated rigidity detection system for interviewing. A unique experimental evaluation supported the system concept. The results of the second study confirmed the kinesic rigidity found in the first, and provided further theoretical insights explaining the rigidity phenomenon. Although additional research is needed, the evidence from this investigation suggests that credibility assessment can benefit from a rigidity detection system.

Ke y w ords an d phrase s: automated interviewing systems, computer vision, concealed information test, credibility assessment, deception detection, freeze response, kinesic rigidity.

Cre dib ility asse ssmen t is a maj or c once rn in man y organ ization s and is an area in which information systems (IS) research can have a major impact. KPMG Integrity Surveys report that nearly three-quarters of employees have firsthand knowledge of wrongdoing in their organization and half state that if such wrongdoing were made public, a significant loss of trust would result [42, 43]. The U.S. government estimates that less than 1 percent of drug trafficking proceeds were detected in a two-year span [74]. In these and many other examples that could be cited, noncredible information has proven difficult to detect, spurring interest among researchers in criminal justice, cognitive psychology, and more recently, IS. Unaided human judgment consistently performs near chance levels [9] in spite of chronic overconfidence by decision makers [22, 31], while current veracity system aids are cumbersome, criticized for validity problems, and labor intensive, thus limiting ubiquity.

The most well-known and widely used methods of veracity assessment rely on skilled professionals using interviewing techniques that require time and specialized equipment. Extensive training, invasive sensors, and time limitations are among the factors that have limited the application of these traditional methods mostly to criminal investigations. From an academic standpoint, the validity of current techniques and the reliability of results have been questioned [51, 58]. In particular, lack of procedural control and potential for human error have been cited as potential concerns [58].

IS research can have a major impact in this area by integrating theory, methods, and technology to generate useful and creative solutions [59, 61]. Many efforts have already begun. Proposed alternative approaches range from monitoring text-based communication in search of linguistic indicators [46, 90] to identifying telling vocalic or eye movement patterns in human screening [63, 79]. These methods differ from traditional approaches employed to assess veracity in the sensors used, questioning protocols administered and cues identified. The present paper builds on this work by investigating the veracity assessment potential of a body movement cue termed rigidity via the Nunamaker approach [59, 60, 61].

This paper has four objectives. First, it reports on the unique discovery of a rigidity effect in a concealed information test (CIT) protocol via a realistic exploratory mock crime experiment. Second, it proposes a system design for automatic recognition of rigidity in credibility assessment interviews. Third, it reports on an implementation of the proposed system design, and evaluation of the instance via a mock screening experiment. Fourth, it summarizes theoretical insights gained throughout this investigation.

Reported here are proof-of-concept iterations, beginning by examining (1) results of an experiment that informed (2) a conceptual system design for rigidity detection, of which an instance was (3) built and evaluated to (4) generate valuable knowledge for advancing credibility assessment. The results of this work help establish the proof of concept for a system for automated rigidity detection and also feed back into a larger program of research investigating solutions for enhancing the accuracy, validity, ubiq uity, and management of automated credibility assessment [23, 63, 64, 78].

## Background

Cre dib ility asse ssmen t an d dec ption de tec tion are gaining increasing interest in IS. Some IS research has focused on how decision makers interact with credibility assessment decision aids [6, 37, 38]. From an e-commerce perspective, IS research has begun to develop a deeper understanding of the key factors involved in e-commerce deception [8]. Automated extraction of linguistic cues to deception has been explored in computer-mediated communication [46, 90, 91], written criminal statements [28], and financial reports [32, 35]. Systems for exploring oculometric indicators of hidden knowledge have also been an emerging interest [63, 78, 79]. Particularly relevant to the current study, there exists a stream of research investigating the use of certain computer vision techniques to identify movement variables that may have relevance to deception detection [14, 39, 56]. Outside of IS circles, recent research has examined systems for credibility assessment using blinking patterns [27] as well as more invasive systems such as functional magnetic resonance imaging (fMRI) [29, 30, 45] and electroencephalography (EEG) [1].

Some IS credibility assessment research has emphasized the need for noninvasive, autonomic system solutions to increase the ubiquity and reliability of credibility assessment, allowing it to create value in nontraditional contexts such as employment screening, auditing, and physical security screening [23, 64, 78]. This forward-looking approach to credibility assessment inspired the concept of an automated conversational agent that monitors psychophysiological and behavioral indicators relevant to credibility assessment [63, 66]. For such an approach to work, many research questions need to be addressed. Among these include the need for identification of valid, reliable cues to deception that can be automatically generated in real or near-real time in a noninvasive manner. Kinesic rigidity is one cue that has the potential to meet these criteria.

## Kinesic Rigidity in Credibility Assessment

Rigidity is one of se ve ral kine sic (i.e., body movement) cues that have been identified in communication and psychology research as potential indicators of veracity. Kinesic rigidity is a temporal period of constricted body movement. During high-stakes deception, a liar tends to exhibit fewer noncommunicative movements, such as fewer instances of rubbing hands together or bouncing a leg. Expressive or illustrative gestures that do occur tend to be more confined and appear forced, as if they are being resisted [12, 85, 88]. Rigidity has been discovered in several studies featuring openended questioning protocols [17, 86, 87].

Despite decades of research into bodily rigidity and related kinesic cues to deception, the contextual boundaries of these phenomena are still not well understood, and defining the nuanced interrelationships among nonverbal behaviors and veracity is an active area of investigation in psychology, communication, criminology, and IS research. Several theories have been proposed as explanations for rigidity during periods of low veracity.

Common theoretical explanations include cognitive load [24, 89] and behavioral control [20]; the results of the current study help make a case that hypervigilance may also be a plausible explanation. Proponents of a cognitive load explanation propose that lying takes more cognitive effort than telling the truth, and assumes that fabricating events requires more cognitive resources than simply recalling events. Because more cognitive resources are allocated to creating a plausible deception, it is thought that other activities, including movement, are given less attention, leading to fewer illustrative or communicative gestures [21].

The second common explanation is overt behavioral control. Proponents of this theory emphasize that the general population holds to a false belief that liars show increased nervousness in their body movements. However, while the average person believes a person shows increased body movement when lying, the opposite tends to be the case [75, 76]. According to behavioral control proponents, a deceiver therefore either reflexively or perhaps purposely becomes more rigid in an attempt to mimic his or her own false perception of what a truthful communication should look like [13, 92].

A third possible explanation of rigidity may be more basic, and a precursor to cognitive excitation or overt behavior. Rigidity may result from the body entering a state of hypervigilance during the biologically driven “stop, look, and listen” response to a perceived threat [10, 33]. When examinees perceive that a line of inquiry has the potential to expose their deception, their body may naturally gravitate toward this hypervigilant state, which is characterized partially by bodily rigidity. Rigidity in hypervigilance is explained in more depth in the Study 1 Discussion section.

Traditionally, rigidity has been measured using human coders, who review video recordings and subjectively rate interview segments according to the appearance of forced versus natural gesturing given the type of gesture and the context in which it was made. Human coding is limited to the major movement that can be perceived by a given coder, and it remains subject to intercoder error. Minute changes in movement can be imperceptible to human coders.

Beyond natural human bias and limitation, the biggest restriction to wider adoption of subjective rigidity coding for deception detection is that of the large amount of time and labor costs involved. Every hour of a recorded interview can take two to six hours of expert post-process coding. An automated solution will have the potential to greatly decrease the time and labor cost. Operator training costs can be eliminated altogether if sensors do not require attachment to or manual calibration with each examinee. A noninvasive, automated measurement method is thus a key contribution of this study and an integral component of the proposed rigidity detection system design.

A second important contribution is the exploration of rigidity in CIT interviews, which previously has not been investigated. In addition to automated and noninvasive measurement, an effective system design requires a reliable questioning protocol. Several potential protocols were investigated in the experimental phase of Study 1, and a CIT structure was ultimately selected as the foundational questioning protocol in the system design. The CIT is detailed further in the Study 1 Discussion section.

## Study 1: Initial Investigation into Automated Rigidity Detection

Base d on the ob se rvation s n ote d in the Bac kgroun d sec tion , general requirements for an automated rigidity detection system were clear from the beginning of the investigation (Table 1). The design requirements were necessarily at a high-level stage, given the novelty of the knowledge space. Additional requirements were added as the investigation progressed, and key considerations were revealed through prototyping and experimentation.

Our initial efforts to track and measure movement in credibility assessment interviews involved using automated techniques for detecting the location of the face and hands in video and tracking two-dimensional changes in location over time. An initial experiment using a mock crime paradigm led to the discovery of rigidity in a CIT paradigm, driving further understanding and development of an automated screening and rigidity detection system design.

## Tracking Movement in Credibility Assessment Interviews

The context first selected for investigating movement was a standard interview setting with the examiner and examinee sitting across from one another, with cameras recording the examinee throughout the interaction. To measure movement, we adapted existing computer vision algorithms for recognizing the hands and face in images [14, 56].

Table 1. Initial Design Requirements for Automated Rigidity Detection

<table><tr><td>Requirement number</td><td>Description</td></tr><tr><td>1</td><td>Automatic tracking of overall movement</td></tr><tr><td>2</td><td>Noninvasive measurement apparatus</td></tr><tr><td>3</td><td>Automatic identification of rigidity during deception</td></tr></table>

For the detection of face and hand/arm locations in video, we applied a skin blob tracking (SBT) technique recently introduced to deception detection research [14, 55, 56, 70]. The SBT technique involves analyzing video frame by frame. For each frame, the face is detected using the Viola–Jones algorithm [84]. Once the face is detected, hand/arm “blobs” are identified by searching for areas of similar (skin) color. The centroid of the face and each hand/arm blob is identified for each frame.

Compared to hand/arm movement, minor changes in head movement ultimately proved more difficult to detect using a full-body frame, standard-definition video. As an alternative method of collecting data for head movement, a close-up video recording of the face was processed using the software suite ASM Face Tracker [41]. This software tracks the two-dimensional Cartesian coordinates of many points on a face. The computer vision technique is built on active shape modeling (ASM), which uses spatial-statistical models of shapes to match identified points on an object in one image to points on an object in a new image. The ASM algorithm tries to match the statistical model parameters to the image. Thus, the model can deform (e.g., stretch), but not beyond what would be naturally seen in a real-world object of similar features, given properly defined model parameters [19]. For faces, this means that identified facial points must represent the image of a face as a whole. For instance, a point on the chin cannot be accidentally identified as immediately adjacent to a point on the eye as this would be outside the bounds of statistically normal model parameters.

## Experiment 1

The SBT and ASM body point location tracking algorithms were used to generate movement data through postprocessing of video recordings of interviews that were part of a realistic mock crime experiment. Mock crime experiments are appropriate for veracity assessment research because the realism involved can elicit reactions that closely mirror real-world scenarios [16]. This mock crime experiment was designed to explore many sensor and questioning technique combinations. The current paper emphasizes that portion of the experiment relevant to automated rigidity detection for credibility assessment.

## Participants

Participants (n = 164) were recruited from the local community of a large university in the southwestern United States via newspaper and Craigslist (www.craigslist.org) listings and paper flyers placed in community centers. We recruited from the local community in order to obtain a sample of participants more representative than students alone, which we felt was important for this more exploratory phase. The participants received \$15 per hour for participation, plus a \$50 bonus if they successfully convinced the examiner that they were innocent of the mock crime. Qualitative observations of the participants noted a broad diversity in economic and social status. Of the 164 enrolled participants, 134 (82 percent) followed instructions and completed the experiment. The remaining 18 percent were disqualified because they did not follow instructions, failed to consent to participate, or confessed during the interview. Because of technical problems with the video recording and analysis system, only 107 of the initial 134 cases produced usable data for analysis. Of these 107 participants, 40 participants “committed” the crime, leaving 67 who did not. In this subset, 63 percent were female, and the average age was 39.5 (standard deviation = 14.0).

## Experimental Procedures

Participants in a simple two-treatment mock crime experiment were instructed to arrive at a room in an upper floor of an old apartment complex. A prerecorded set of instructions was waiting for them. After listening to the instructions and signing a consent form, the participants left the apartment complex and walked to a nearby building.

Per the instructions, the participants reported to a room on the top floor and asked for a Mr. Carlson. A confederate acting as a new receptionist who did not know Mr. Carlson asked the participant to wait while he went to locate Mr. Carlson. A camera in the room verified the participants’ activities while they were waiting for the receptionist’s return. Participants in the Innocent condition simply waited, while those in the Guilty condition stole a diamond ring from the desk. Guilty participants took a key from a mug on the top of a desk and used it to open a blue cash box in the desk drawer that was hidden underneath a tissue box. They removed the ring from the cash box and hid it somewhere on their person.

Upon returning, the receptionist directed the participants to another room on the bottom floor of the building, the layout of which is depicted in Figure 1. There, the participants were told that a crime had occurred in the building that day and that they would be interviewed to assess their possible involvement in the crime. All the participants were interviewed by one of four professional polygraph examiners provided by the National Center for Credibility Assessment (NCCA). The interviewers were trained and experienced, and were familiar with the purpose and procedure involved in administering various interviewing techniques, including CIT, a veracity assessment technique highly regarded in academic circles [5, 58, 80] but rarely used in practice, Japanese criminal investigations being the notable exception [57, 65]. The participants were offered a \$50 bonus if they successfully convinced the interviewer that they were innocent. This large monetary reward together with the realism of the experiment was important to induce behavioral effects and motivate participants to appear innocent in ways that would closely mirror real-world scenarios.

![](/api/attachments/5HVKFQ4K/fulltext/images/a60b49bc3b6888aadacf553e74c3d5fc90b7add991672a43d9bb412dae2956fd.jpg)  
Figure 1. Layout of Interviewing Room for Experiment 1

Two studio-quality video cameras were placed directly in front of the chair in which each participant sat during the interview. The chair had a low back and did not have armrests. No other furniture or objects were within reach. This setup ensured that inactive arms and hands would rest on legs during the CIT portion of the interview. Other cameras and sensors were also present in the room, to examine their potential for credibility assessment (to be reported elsewhere). The location of each hand/arm and the head were identified frame by frame using the SBT and ASM computer vision techniques.

The interview consisted of several questioning techniques, including a CIT. The CIT was a major portion of the interview and became the focal procedural component of the rigidity detection system, as explained in later sections. To our knowledge, rigidity has never been investigated in a CIT format prior to this study, and exploring rigidity in the CIT was not initially a primary consideration. Rather, we sought to detect rigidity in alternative questioning techniques similar to previous work. However, the control and simplicity of the CIT, together with its potential for an automated system prompted an exploratory rigidity analysis. The three CIT questions together with their associated target and nontarget items are included in Table 2.

Table 2. Questions Used in the Study 1 Concealed Information Test

<table><tr><td>Question</td><td>Words repeated by suspect</td></tr><tr><td rowspan="6">If you are the person who stole the ring, you are familiar with details of the cash box it was stored in. Repeat after me these cash box colors:</td><td>Green</td></tr><tr><td>Beige</td></tr><tr><td>White</td></tr><tr><td>Blue*</td></tr><tr><td>Black</td></tr><tr><td>Red</td></tr><tr><td rowspan="6">If you are the person who stole the ring, you moved an object in the desk drawer to locate the cash box containing the ring. Repeat after me these objects:</td><td>Notepad</td></tr><tr><td>Telephone book</td></tr><tr><td>Woman&#x27;s sweater</td></tr><tr><td>Laptop bag</td></tr><tr><td>Tissue box*</td></tr><tr><td>Brown purse</td></tr><tr><td rowspan="6">If you are the person who stole the ring, you know what type of ring it was. Repeat after me these types of rings:</td><td>Emerald ring</td></tr><tr><td>Turquoise ring</td></tr><tr><td>Amethyst ring</td></tr><tr><td>Diamond ring*</td></tr><tr><td>Ruby ring</td></tr><tr><td>Gold ring</td></tr></table>

\* Target items (i.e., correct answers).

Video from the two cameras recorded during the interview were processed to generate overall movement data, as explained in the next section. A final questionnaire followed the interview portion of the experiment, and contained simple manipulation check questions, together with a question about perceived behavioral control and measures of arousal and motivation levels.

## Measuring Rigidity

This study took a novel approach to measuring movement, designed to circumvent the need for post hoc, manual subjective judgments. For the mock crime experiment, the centroid coordinates of each SBT-generated blob and the center coordinates of the ASM face model were generated for each frame between the end of an interviewer question and the beginning of the next question. Once data for each frame were generated, overall movement for the left and right hands/arms for each video segment was calculated by determining the average Euclidean distance between centroid position changes frame by frame during a given response in the following manner:

$$
M _ {s} = \left(\sum_ {j} ^ {i} \sqrt {\left(y _ {2} - y _ {1}\right) ^ {2} + \left(x _ {2} - x _ {1}\right) ^ {2}}\right) / j.
$$

This produced an average overall movement score for each response for each individual. However, average overall movement during a response is certain to be affected by more than just veracity level. Culture, personality, mood, gender, and question type are example factors that may also affect overall movement or lack thereof. For instance, qualitative observations of the participants revealed that, on average, those from Western cultures tended to exhibit more movement overall when “sitting still” than those from Eastern cultures. Identifying, automatically measuring, and integrating all such potential global moderating factors that influence movement is a difficult and complex task, and well beyond the scope of this study.

However, a repeated-measures interviewing protocol provides the possibility of an alternative approach. Individuals can be compared to an individual baseline rather than an overall population average [2, 82], sidestepping the need to account for factors such as gender, culture, or mood. The movement averages for each segment were thus standardized as within-subject z-scores. The z-scores were also body point specific, because natural variance is expected in the amount of movement that each point on the body will exhibit (e.g., a little movement of the head can be just as meaningful as a relatively large movement of a hand). In the case of the CIT questions, z-scores were also question specific to control for the possibility of question effects.

## Results

As part of the postinterview questionnaire, the respondents self-reported their levels of motivation, effort, and tension, each on a seven-point scale (see the Appendix). Participants reported high levels of motivation and effort, and moderate levels of tension. Summary statistics are in Table 3.

Within-subject comparisons of interquestion overall movement did not produce significant results for any tested interviewing protocols except the CIT. The rigidity results of tests other than the CIT are omitted for succinctness.

For the CIT questions, a multilevel regression model was specified for overall movement during the response time for each foil item. Multilevel regression models use adjusted standard errors to reflect the uncertainty that arises from variation within a subject. The summation of standardized movement scores for right hand, left hand, and head was used as the dependent variable. The independent variables included Condition (dummy coded: 1 = G uilty, 0 = Innocent), Participant, and Target Item (dummy coded: 1 = Correct Answer, 0 = Incorrect Answer). Question and interviewer were initially included as covariates but were found to not be significant predictors and were subsequently dropped from the model. The effect of greatest interest was the Condition and Target Item interaction, which reflected overall movement when Guilty participants responded to the correct answer. The results of the multilevel regression model are shown in Table 4, with Condition labeled “Guilty” to help facilitate interpretation.

The significant estimate of –0.624 in the Guilty × T arget Item interaction can be interpreted to mean that when Guilty participants were asked to repeat the correct answer to a CIT question, they tended to be approximately 0.624 standard deviations below their own personal average. To test if the Guilty and Target Item interaction provided a significant improvement to the fit of the data, the model was compared to an unconditional model, omitting any fixed effects and using deviance-based hypothesis tests. The fit of the current model was significantly better than the unconditional model, $\chi ^ { 2 } ( 1 , N = 1 , 8 8 7 ) = 1 7 . 1 5 , p < 0 . 0 0 1$

Table 3. Self-Reported Motivation, Effort, and Tension

<table><tr><td>Self-report(seven-point scale)</td><td>Condition</td><td>Mean</td><td>Standard deviation</td></tr><tr><td rowspan="2">Motivation to succeed</td><td>Innocent</td><td>6.12</td><td>1.31</td></tr><tr><td>Guilty</td><td>6.15</td><td>1.29</td></tr><tr><td rowspan="2">Effort</td><td>Innocent</td><td>5.75</td><td>1.54</td></tr><tr><td>Guilty</td><td>6.13</td><td>1.24</td></tr><tr><td rowspan="2">Tension</td><td>Innocent</td><td>3.00</td><td>1.56</td></tr><tr><td>Guilty</td><td>3.21</td><td>1.75</td></tr><tr><td colspan="4">Note: No comparisons were significantly different between groups.</td></tr></table>

Table 4. Overall Movement: Multilevel Regression Model Results

<table><tr><td>Fixed effects</td><td> $\beta$ </td><td> $\beta$  standard error</td></tr><tr><td>Intercept</td><td> $0.044^{n.s.}$ </td><td>0.069</td></tr><tr><td>Guilty</td><td> $0.102^{n.s.}$ </td><td>0.109</td></tr><tr><td>Target Item</td><td> $-0.197^{n.s.}$ </td><td>0.171</td></tr><tr><td>Guilty  $\times$  Target Item</td><td> $-0.624^{*}$ </td><td>0.267</td></tr><tr><td colspan="3">Notes: N = 1,887. Model fit using maximum likelihood. * p &lt; 0.05; n.s. = not significant.</td></tr></table>

## Study 1 Discussion

Using the SBT and ASM tracking techniques and the automated movement measurement method, rigidity was successfully detected automatically in only one interviewing protocol—the CIT. There were several important lessons learned from this initial investigation, including the discovery of rigidity in the CIT and important observations and refinements necessary to advance the initial concept of a rigidity detection design closer toward a successful proof of concept.

The rigidity effect was consistently significant for three successive CIT questions. Rigidity has previously been identified in open-ended interviewing where various types of movement are common, each measured in frequency or duration [73, 85, 88], but the CIT offers little opportunity for communicative movement during short answers. No story fabrication occurs in a CIT; any movement that does occur in a CIT is either natural movement that occurs even during a state of stillness, or self-adaptors or similar movements that are non-communicative in nature. Thus, in a CIT context, the previously referenced cognitive load theory is not plausible. Behavioral control remains a possibility, and participants did self-report high motivation and effort. However, the rigidity in head movement even though no nodding occurred suggests that the rigidity detected in the CIT might have been at a more granular level than what has been traditionally attributed to behavioral control. These unanticipated findings prompted a more in-depth investigation into the driving factors behind rigidity and the CIT, in order to better understand how a rigidity detection system could best be designed to take advantage of this unique discovery.

## Rigidity in the Concealed Information Test

The CIT is a questioning method that seeks to minimize potential interviewer effects while generating a strong individual baseline for analysis. The CIT is similar to a multiple choice exam: An interviewer asks multiple-choice questions specific to an illicit act, with each question followed by a series of possible answers, each stated verbally by the interviewer [50]. When each possible answer is stated, the examinee is required to either repeat each possible answer or respond with “yes” or “no” [52, 83]. Physiological measurements such as skin electrical conductivity are traditionally measured throughout this exercise, and analyzed for abnormalities during target items (correct answers) as compared to nontarget items (incorrect answers) [48]. The CIT has been praised as the most valid of current credibility assessment interviewing techniques, and calls have been made for its more widespread use [4, 36], perhaps even to applications other than criminal interviewing. Some evidence even suggests that the CIT format can be used to measure and predict behavioral intent [54].

Traditional measures in the CIT gauge levels of the psychophysiological orienting response, the sympathetic nervous system activation triggered by novel or personally significant stimuli [48, 51, 72]. A commonly cited example of the orienting response depicts a loud cocktail party where an individual is oblivious to peripheral conversations [18]. Yet the same individual will naturally orient attention toward a peripheral conversation when his or her name is spoken, because of its personal significance. The physiological effects of this natural, autonomic orienting range from variations in pupil dilation and respiration to skin conductivity and heart rate, with skin conductivity being the most commonly measured effect in the CIT  [1, 4, 25].

There is evidence to suggest that CIT rigidity may also stem from the orienting reflex, if the stimulus is associated with a potential threat. Perceived threats cause an individual to enter a “stop, look, and listen” hypervigilant state characterized by physiological and behavioral modifications designed to better recognize and respond to perceived threats. Although the term hypervigilance may seem to imply increased movement, when a non-immediate threat is involved the opposite tends to be the case. In such cases an individual exhibits less overall movement, at the same time experiencing heightened sensitivity to cues that may require a defensive reaction, such as fight or flight [15, 40]. This “freeze response” has often been grouped with what is termed a defensive response rather than with the orienting reflex. However, the freeze response is associated with bradycardia (i.e., decreased heart rate) [7, 69], a distinguishing characteristic of the orienting reflex [81, 83]. This apparent contradiction may be resolved by the defense cascade model, which describes the defensive response as a temporal sequence of events, of which one event is an orienting response. The defense cascade model conceptualizes the freeze response as part of an orienting reflex [11, 44], “possibly serving to facilitate detection of information relevant for a subsequent fight-or-flight response involving whole-body movements” [68, p. 1580]. The freeze response occurs as part of the orienting reflex when a perceived threat is not immediate, such as when an animal senses a predator from afar [26, 68].

Recent evidence indicates that the freeze reflex is also evident when the nature of the perceived threat is social, rather than physical [68]. To the extent, then, that a CIT stimulus is perceived as having potential to expose a deception and subject an individual to consequences, the natural reaction should include a freeze response, or whole-body rigidity. In such a case, the threat is not imminent, but can have serious social repercussions, and we would therefore expect the orienting reflex to include a freeze response.

## Design Performance and Revised Requirements

Several key observations and results from Study 1 generated the insight necessary for a revised and more specific design for a rigidity detection system for credibility assessment. These insights affected the questioning protocol as well as the interaction design and measurement technology.

Effective credibility assessment systems will necessarily synthesize questioning protocol with technology and interaction design requirements, because the manner in which questions are asked can be just as important a factor as the deception cues measured [34, 47]. That rigidity was discovered only in the CIT indicated that a reliable system questioning protocol and interview design will need to minimize or control for many potentially confounding factors. In a credibility assessment interview, the amount of movement appeared to be strongly affected by many factors beyond veracity level, including culture, interview style, and context. This likely caused difficulty automatically detecting rigidity in open-ended interviewing protocols, counter to prior research. For instance, one individual response to a question may involve minor communicative gestures depicting “small,” while a similar gesture later in the discussion may be more expansive when depicting the concept “large.” Also, individuals from certain cultural backgrounds were less inclined to gesture compared to others. The interviewer’s style and demeanor influenced the response style and demeanor of the examinee.

The effects of these cultural and contextual factors were likely large enough to significantly impact overall movement in non-CIT question responses. Traditional manual coding can subjectively account for context and movement type, whereas the proposed automated method treated all movement equally. The analysis revealed that traditional human coding may be more useful for detecting rigidity in certain types of movement, such as a behavioral control–induced decrease in hand and finger movements, while the automated approach used in this study may work best for detecting rigidity resulting from the freeze response, which affects the whole body (Table 5).

In addition to discovering the advantage of a CIT-like questioning protocol, the results of Study 1 have interaction design and measurement technology implications. If the rigidity effect in a CIT stems more from an overall, whole-body freeze response, a better system design may be one that captures movement from more body points, rather than focusing mostly on hand and head movement as in Study 1. Also, a standing interview may be more effective for capturing body movement, as opposed to a sitting interview where movement at a resting state is inhibited by a chair. SBT and ASM tracking provided usable data for every participant for whom video was properly recorded, but movement in the third dimension (i.e., depth) was not possible to capture using standard two-dimensional video. The SBT and ASM techniques required timeconsuming post-processing to complete, which in practice would limit usefulness to contexts that require less rapid decision making, such as criminal investigations, or, in order to be useful in rapid contexts, would require improvement in hardware or software to generate near real-time data for analysis. Also, the beginning and end points for each response had to be manually marked, as the SBT and ASM procedures by themselves provide no video segmentation or tagging capability.

Table 5. Comparison of Rigidity Measurement Methods

<table><tr><td></td><td>Traditional manual movement coding</td><td>Proposed automated method</td></tr><tr><td>Rigidity measurement method</td><td>Human judgments of frequencies and durations of predefined movements</td><td>Automatically captured movement measured by detecting body point position changes</td></tr><tr><td>Granularity of measurement</td><td>Major gestures to minor finger movements</td><td>Pixel-level changes (assuming computer vision approach)</td></tr><tr><td>Time requirement</td><td>2 to 3 man-hours per hour of recorded interview (estimated)</td><td>Near real-time</td></tr><tr><td>Categorization of movement</td><td>Can reliably classify movement (e.g., self-adaptor, illustrator gesture)</td><td>All movement for a given body point treated equally; no differentiation of movement types</td></tr><tr><td>What can be detected in the CIT</td><td>Frequencies and durations of non-functional movements (e.g., fidgeting)</td><td>Overall body movement rates</td></tr></table>

In sum, the observations and findings from Study 1 helped to better specify requirements for a system for automated rigidity detection for credibility assessment (Table 6).

## Study 2: Development of a Rigidity Detection System for Credibility Assessment

Buildin g on the re sults of Study 1, we developed an autonomous screening system for automated rigidity detection that would operationalize the design requirements. The underlying software for automated interviewing was adapted from earlier efforts at automated interviewing systems designed for a kiosk-like interaction [63, 77]. These automated screening technologies use an automated agent to ask questions and record responses. The same virtual interview can be used for every examinee, controlling for interviewer effects. The screening systems also enable automatic segmentation of interviews into relevant portions. The current project built on and extended these system designs by implementing the CIT-based questioning protocol and adding a method for movement detection.

Table 6. Design Requirements for an Automated Rigidity Detection System

<table><tr><td>Requirement number</td><td>Description</td></tr><tr><td>1</td><td>Conduct an interview which includes potentially threatening stimuli (for guilty individuals) mixed with non-threatening stimuli in a multiple choice-like format</td></tr><tr><td>2</td><td>Ensure the interviewing protocol that minimizes potentially confounding communicative movement</td></tr><tr><td>3</td><td>Conduct the interview automatically to control for or minimize the effects of a human interviewer</td></tr><tr><td>4</td><td>Preferably use a standing interview</td></tr><tr><td>5</td><td>Employ non-invasive, near-real time or better raw movement data capture, such as computer vision algorithms</td></tr><tr><td>6</td><td>Preferably track movement in three dimensions</td></tr><tr><td>7</td><td>Automatically segment interviews into relevant time periods (e.g., tag start and end points for responses)</td></tr><tr><td>8</td><td>Leverage the questioning protocol to generate a strong individual baseline for comparison</td></tr><tr><td>9</td><td>Compare overall movement during key questions to that during irrelevant questions</td></tr></table>

## Interviewing Protocol

Because rigidity in a CIT was a new discovery, it was important to determine whether rigidity is a robust effect and whether it translates to alternative contexts. From a practical standpoint, it was important to design and evaluate a system capable of delivering an automated CIT and detecting rigidity with minimal user input. Instantiating the findings of Study 1, the CIT served as the foundational questioning protocol for the rigidity system design. The multiple-choice question format provided a means for generating a strong individual- and question-specific baseline, by comparing behavior displayed during the response to the correct answers to behavior during incorrect answers. This questioning format makes it possible to control for individual and question effects.

## Rigidity Detection and Measurement

We adapted a process for detecting rigidity using an automated screening approach. To capture data for movement analysis, we used a Microsoft<sup>®</sup> Kinect<sup>®</sup> sensor rather than standard cameras. The Kinect uses stereoscopic imaging to identify the three-dimensional (3D) location of 20 major body points in real time at roughly 30 samples per second in real time. The Kinect was chosen over SBT and ASM because of its ability to capture the position of more body points (potentially important for a standing interview), track in three dimensions, and minimize the delay in data generation.

![](/api/attachments/5HVKFQ4K/fulltext/images/c232f2ddda9915ed74d72468b86645fe1c51653d14397ec6ec35ff18f074bef3.jpg)  
Figure 2. Physical System Configuration Used in Experimental Evaluation  
Note: The Kinect sensor (circled) was place approximately 6 feet from the platform where interviewees stood.

The Kinect sensor was placed approximately 6 feet away from a platform where an interviewee was told to stand during the interview. This distance was just enough to allow the sensor to capture a full body view. A computer screen serving as the interface for the automated interview was mounted on a reticulating arm rather than a desk or table so that the sensor’s line of sight would be unobstructed. Custom lighting was kept constant and designed to eliminate shadows similar to the first iteration. Figure 2 depicts this configuration.

Custom algorithms were scripted to capture the 3D Cartesian coordinates (in meters) of each of the 20 points in real time and segment and analyze the data. Data from an entire interview were segmented into relevant portions, then summarized and standardized in the same manner as were the SBT and ASM data in Study 1, the only difference being that there were 20 body points to standardize rather than 3.

## Experiment 2

A laboratory experiment was designed to evaluate the system. Rather than a mock crime scenario, a building security screening context was chosen. This choice stemmed from a desire to identify potential contextual nuances for the rigidity effect for credibility assessment. Important to this evaluation from a design science perspective was identification of the extent to which the system fulfilled design requirements as well as the most promising areas for improvement. From a theoretical perspective, it was important to confirm the rigidity effect discovered in the first experiment, and perhaps gain further insight into its origins.

## Participants

Students from a large southwestern university participated in the experiment as part of a course requirement. While the ideal population to test would be individuals who intend to commit an actual crime, such a population would be prohibitively difficult to find. Students are an appropriate alternative because the main drivers behind the standard CIT have been found to be equally valid among adult populations and antisocial or hyporesponsive criminals [82], and kinesic rigidity itself has been observed in criminal behavior during conditions of low veracity [86] as well as students [88]. Thus, while students are not the optimal test population, the observations seen in this population likely have a useful level of external validity.

The participants were offered \$20 if the system judged them as truthful. This was a mild deception designed to promote engagement and jeopardy; in reality, all the participants received \$20. In both experiments, human subjects protocols were followed, and approval was obtained from the university’s human subject institutional review board. Of the initial 175 participants, 18 were disqualified because they either did not follow instructions (e.g., failed to construct/pack the device) or failed both manipulation check questions.<sup>1</sup> Of the remaining 157 participants, 43 percent were female.

## Experimental Procedures

As in experiment 1, there were two conditions in this study: Guilty and Innocent. The protocol mirrored the experiment detailed in Twyman et al. [77], except in this case, the Guilty condition was broken into four groups, with three of the groups trying different countermeasures (i.e., methods for defeating a system). The effectiveness of the countermeasures was an important consideration, but is beyond the scope of this paper and will be reported elsewhere.

Participants packed a bag with standard travel items (e.g., clothes, books) with the intention to deliver the bag to a contact ostensibly in a secure portion of the building. The Guilty participants in this experiment also constructed a mock improvised explosive device (IED) and packed it with the innocuous items. The participants were told that to get to the secure portion of the building, they would have to pass through a security screening checkpoint. A separate room was set aside for the screening (Figure 3) to ensure no distractions would be present. Participants interacted with the second-generation ASK system as a prerequisite for entering the secure portion of the building where they were to deliver the bag. All of the participants had been introduced to the ASK system during the experiment sign-up, and on arrival, they were offered \$20 if they were able to successfully pass through the screening without being flagged by the system. The task to deliver the bag was a mild deception to encourage realism; in reality, no deliveries took place. After the automated screening, the participants filled out a questionnaire and were debriefed to ensure they understood that their task was complete in spite of not having delivered the bag, and that the experiment was only a simulation and they had not done anything illegal.

![](/api/attachments/5HVKFQ4K/fulltext/images/90db9498feaefe3510806bad40b1f0b1f3e9de49b6f3807972b1bbb4fb61c81b.jpg)  
Figure 3. Screening Room Layout for Experiment 2  
Note: Participants brought their packed bag into the room and stood on the platform for the brief screening interview.

The interview phase proceeded in the following manner: A participant stepped up to the ASK system, and the automated system provided audible initial instructions and guided the individual through a 15-second calibration process. After this, a realistic, on-screen animated avatar face asked the question, “Are you carrying any of these items?” A screen appeared immediately after each question was asked, displaying four images representing banned items for five seconds. Figure 4 shows an example of a screen displaying the images. This question was asked five times. An image representing an IED appeared only once during this period. The sequence of five questions was asked three more times, rotating the location of the images and changing the temporal point at which the image representing an IED was displayed. The entire 20-question process took about four minutes, after which the participants proceeded through the exit, filled out a questionnaire, and were debriefed.

![](/api/attachments/5HVKFQ4K/fulltext/images/06d5e07f617c13138c9bc8c1d78b69df9b9d4c658c40f8433dbbb77deedbf30a.jpg)  
Figure 4. Sample Stimuli Screen  
Note: Twenty of these stimuli were displayed during each interview.

## Results

Two manipulation check questions ensured the participants had understood and followed the instructions. Additional manipulation check questions in the postexperiment questionnaire captured self-reported motivation, effort, and tension (see the Appendix). As in Study 1, the participants reported high levels of motivation and effort as well as moderate levels of tension (Table 7).

As in Study 1, summations of the major body points’ standardized movement scores served as a measure of overall movement in a target segment (when an IED appeared on the screen) relative to control segments (where no IED was present). A multilevel regression model using these standardized movement scores as the dependent variable was specified in a manner similar to that reported in the first experiment. Age, gender, education level, and English fluency were initially included but, as expected, because of the standardization procedure, produced no significant results and did not add to the fit of the model. Although the Guilty condition contained four distinct groups, the overall trend of rigidity was similar for all groups. Because the nuances between the Guilty groups will be investigated in detail in a future study, and for the sake of simplicity, we collapsed all Guilty conditions into a single group for this analysis. Table 8 summarizes the overall movement results.

The significant estimate of –0.109 in the Guilty × T arget Item interaction can be interpreted to mean that when Guilty participants viewed the image of an explosive on the screen, they tended to be approximately 0.109 standard deviations below their own personal average. To test if the effects seen provide a significant improvement to the fit of the data, the model was compared to an unconditional model, which omits any fixed effects, using deviance-based hypothesis tests. The fit of the current model was significantly better than the unconditional model, $\chi ^ { 2 } ( 1 , N = 6 2 , 7 8 0 ) = 1 8 1 . 2 6$ 4 $p < 0 . 0 0 1$

Table 7. Self-Reported Motivation, Effort, and Tension

<table><tr><td>Self-report(five-point scale)</td><td>Condition</td><td>Mean</td><td>Standard deviation</td></tr><tr><td rowspan="2">Motivation to succeed</td><td>Innocent</td><td>4.29</td><td>0.76</td></tr><tr><td>Guilty</td><td>4.33</td><td>0.74</td></tr><tr><td rowspan="2">Effort</td><td>Innocent</td><td>3.17</td><td>1.14</td></tr><tr><td>Guilty</td><td>3.52</td><td>1.15</td></tr><tr><td rowspan="2">Tension</td><td>Innocent</td><td>2.71</td><td>1.14</td></tr><tr><td>Guilty</td><td>3.15</td><td>1.14</td></tr></table>

Note: No comparisons were significantly different between groups.

Table 8. Overall Movement: Multilevel Regression Model Results

<table><tr><td>Fixed effects</td><td> $\beta$ </td><td> $\beta$  standard error</td></tr><tr><td>Intercept</td><td> $0.013^{n.s.}$ </td><td>0.014</td></tr><tr><td>Target item</td><td> $-0.024^{n.s.}$ </td><td>0.019</td></tr><tr><td>Guilty</td><td> $0.022^{*}$ </td><td>0.010</td></tr><tr><td>Guilty  $\times$  Target item</td><td> $-0.109^{*}$ </td><td>0.028</td></tr></table>

Notes: $N = 6 2 , 7 8 0 .$ . Model fit using maximum likelihood. \* $p < 0 . 0 5 ;$ n.s. = not significant.

A follow-up analysis was undertaken to examine stillness on a more granular level. Overall movement was broken down by major body points and similar variables were identified using principal components analysis (PCA). Using the traditional cutoff point of eigenvalues > 1, five factors were generated. Table 9 shows the PCA factor loadings; Table 10 shows the variance explained by each factor.

The first factor and most of the explained movement came from the core part of the body, with the remaining four components each centered on a hand or foot. The results of separate multilevel regression models for each component were generated to help locate the area(s) of greatest rigidity during CIT target items (Table 11).

The significant estimate of –0.250 in the Guilty × T arget Item interaction can be interpreted to mean that when Guilty participants viewed the image of an explosive on the screen, their movement tended to be approximately 0.250 standard deviations below their own personal average. This represents a significant drop in overall movement for the core body, which is ostensibly at a state of rest throughout the entire interview.

## Discussion

In prac tice , rigidity is n ot a c ommon ly c on side re d variab le for credibility assessment. To the extent rigidity is considered, it is only in an ad hoc, subjective matter. Such usage is unreliable and prone to error. Person-to-person credibility assessment in interviews, negotiations, and other meetings could benefit from a credibility assessment IS that includes a rigidity detection system.

Table 9. PCA Factor Loadings for Overall Movement

<table><tr><td>Body point</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td></tr><tr><td>Head</td><td>0.56</td><td></td><td></td><td></td><td></td></tr><tr><td>Hip center</td><td>0.93</td><td></td><td></td><td></td><td></td></tr><tr><td>Left hip</td><td>0.88</td><td></td><td></td><td></td><td></td></tr><tr><td>Right hip</td><td>0.88</td><td></td><td></td><td></td><td></td></tr><tr><td>Shoulder center</td><td>0.71</td><td></td><td></td><td></td><td></td></tr><tr><td>Left shoulder</td><td>0.71</td><td></td><td></td><td></td><td></td></tr><tr><td>Right shoulder</td><td>0.65</td><td></td><td></td><td></td><td></td></tr><tr><td>Spine</td><td>0.94</td><td></td><td></td><td></td><td></td></tr><tr><td>Right hand</td><td></td><td>0.88</td><td></td><td></td><td></td></tr><tr><td>Right wrist</td><td></td><td>0.91</td><td></td><td></td><td></td></tr><tr><td>Left hand</td><td></td><td></td><td>0.87</td><td></td><td></td></tr><tr><td>Left wrist</td><td></td><td></td><td>0.89</td><td></td><td></td></tr><tr><td>Left ankle</td><td></td><td></td><td></td><td>0.87</td><td></td></tr><tr><td>Left foot</td><td></td><td></td><td></td><td>0.86</td><td></td></tr><tr><td>Right ankle</td><td></td><td></td><td></td><td></td><td>0.85</td></tr><tr><td>Right foot</td><td></td><td></td><td></td><td></td><td>0.84</td></tr><tr><td>Left elbow</td><td>0.42</td><td></td><td>0.49</td><td></td><td></td></tr><tr><td>Right elbow</td><td>0.35</td><td>0.49</td><td></td><td></td><td></td></tr><tr><td>Left knee</td><td>0.42</td><td></td><td></td><td></td><td></td></tr><tr><td>Right knee</td><td>0.34</td><td></td><td></td><td></td><td></td></tr></table>

Notes: Movement values are standardized as noted in the Measuring Rigidity section. Varimax rotation factor loadings less than 0.3 are omitted.

Table 10. PCA Factors Variance Explained

<table><tr><td></td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td></tr><tr><td>Proportion of variance explained</td><td>0.28</td><td>0.10</td><td>0.09</td><td>0.08</td><td>0.07</td></tr><tr><td>Cumulative variance explained</td><td>0.28</td><td>0.38</td><td>0.48</td><td>0.56</td><td>0.63</td></tr></table>

Given the potential impact, the purpose of this project was to use prototyping and experimentation to investigate the potential of automated rigidity detection for credibility assessment and advance a system design toward a proof of concept. These goals were realized in Studies 1 and 2, as new understanding emerged with regard to rigidity itself in a credibility assessment context as well as to a requirement set that could be feasibly instantiated in a system solution.

The results of Study 1 unexpectedly revealed that rigidity was present in the highly controlled CIT, which suggested the possibility of exploiting this finding in an automated interviewing solution. The results from Study 2 verified the initial discovery of CIT rigidity, and provided evidence that the automated screening system design can work. The investigation also provides theoretical insight with regard to the rigidity phenomenon. Previous work investigating rigidity has focused on conversational interactions where movement is a natural, integral part of the interaction. Rigidity has been thought to stem from an increase in cognitive load or misapplied behavioral control. In the CIT, there is no message production or similar demand for increased cognitive activity when lying. It is difficult to argue, then, that the nervous system lacks sufficient resources to attend to natural movement. Behavioral control remains a plausible explanation for rigidity in a CIT context; however, if most rigidity is centered in the core body, as was seen in Study 2, the psychophysiological freeze response may be a more likely explanation. It is important to note that these insights are limited to a highly controlled format such as the CIT, and thus do not necessarily contradict prior rigidity research. Rigidity in alternative, more communicative, and open-ended interviewing techniques may have different underlying drivers.

Table 11. Results by Principal Component

<table><tr><td>Fixed effects</td><td>Core body (C1) β</td><td>Right hand/arm (C2) β</td><td>Left hand/arm (C3) β</td><td>Left foot (C4) β</td><td>Right foot (C5) β</td></tr><tr><td>Intercept</td><td>0.013</td><td>0.009</td><td>-0.005</td><td>-0.002</td><td>-0.004</td></tr><tr><td>Target Item</td><td>-0.063</td><td>-0.046</td><td>0.026</td><td>-0.008</td><td>0.018</td></tr><tr><td>Guilty</td><td>0.050</td><td>-0.002</td><td>0.010</td><td>0.001</td><td>0.014</td></tr><tr><td>Guilty × Target Item</td><td>-0.250*</td><td>0.012</td><td>-0.048</td><td>-0.003</td><td>-0.070</td></tr></table>

Notes: N = 3,139. Model fit using maximum likelihood. $^ { * } p < 0 . 0 5 .$

It is also important to note also the differences in measurement. Prior research has focused on manually measuring frequencies of distinct, visible movements, whereas this study collapsed all movement within a given segment. Manual coding differentiates between movement types and can consider semantic meaning of movement types. This may be one reason why rigidity was not found in alternative questioning protocols in Study 1, where open-ended questions encourage semantically driven movements. While it lacks the ability to recognize intended semantic meaning, the movement-tracking design in this study has advantages of automation and ability to capture fine-grained movement, even at a natural resting state.

The second study replicated the first, but with several variations, including a systemdriven rather than a human-driven interview, movement detection using an alternative approach, and a screening paradigm rather than a post-crime investigative interview. The rigidity effect appeared to be robust to these differences.

## Contributions

Nunamaker and Briggs [59] have called for an expanded vision of IS research that includes inventing new systems that address information needs. The overall contribution of this investigation is a design for a proof-of-concept prototype for automated rigidity detection for credibility assessment—a novel and previously unexplored concept. Although the domain and design are somewhat novel to IS research, the contribution lies at the heart of IS: The greatest value of this prototype design is not the process or the technology chosen, but in the synthesis of technology and process [71].

This investigation generated knowledge through exploration, prototyping, theory development, and experimentation. Whereas initially the requirements for a feasible system for rigidity detection for credibility assessment were an unknown or lacked evidence, this investigation specified a process and technology combination that can achieve this goal. In so doing, new insights into rigidity were revealed. Prior to this investigation, rigidity had been observed in open-ended responses. Rigidity was discovered in a CIT setting, a scenario not previously investigated, likely because of the expectation of little movement in a CIT. However, it was this very controlled and simple technique that suggested not all rigidity is due to cognitive overload, and may derive from the natural hypervigilance state—more directly hardwired into human genetic makeup than was previously thought.

This new discovery for credibility assessment systems and CIT research has potential for high impact not only to IS researchers developing credibility assessment systems but also to criminal justice, communication, and psychology research on CIT and kinesic rigidity. Research in reference disciplines bemoans the fact that unaided human credibility assessment is consistently poor [9], uncorrelated with decision makers confidence [22], and the most common methods employed to help are scientifically unsound [3, 58]. The CIT was initially proposed in part to add validity to credibility assessment interviewing. This systems approach to conducting a CIT furthers that ideal via greater control of interviewer effects and noninvasive sensors, while at the same time increasing the potential for ubiquitous application. Minimizing the human skill and specialized technology requirements by developing noninvasive, automated system solutions such as these may facilitate the adoption of CIT examinations on a much broader scale, whereas current usage is limited to a very small percentage of criminal investigations, and very few other applications. As this line of research advances, rigidity detection may also be useful as an additional indicator for existing and alternative use cases, such as security screening, employment interviews, pre-auditscreening interviews, insider threat detection, or group collaboration sessions.

## Limitations and Future Directions

The instantiation of the design requirements performed as anticipated for all of the interviews. Thus, the results of Study 2 provide support for a proof of concept. Nevertheless, several observations revealed areas for improvement on the conceptual design. A potential drawback of the Kinect sensor was its low resolution, which increases the probability that minor differences in movement patterns will go undetected, and may therefore have affected the movement detection ability of the overall system. An evaluation of the SBT and ASM techniques in Study 1 revealed that rigidity in head movement was indiscernible in a full-body standard-definition video frame, but easily detected in a facial close-up frame. This indicates that points on the body that naturally have little movement may need higher resolution to discover rigidity effects stemming from a freeze response.

The findings in this investigation serve as an important piece of a large research program focused on systems solutions for modern credibility assessment needs. The research program mirrors the University of Arizona group support systems research program in that high-impact knowledge is discovered and integrated over an extended period of time using many system iterations and explorations [62]. Many additional important research topics and critical research questions will be investigated through the exploration, design, and evaluation of automated credibility assessment systems. Some immediate examples include prediction, sensor and indicator fusion, and countermeasures.

While this study focused on feasibility and proof of concept, future research will need to investigate the predictive capability of the rigidity phenomenon alone and in combination with other CIT deception cues usable in automated credibility assessment. There are many prediction algorithms and scoring methods investigated in the extant CIT research [49, 53], and an investigation into the usefulness of each of these and novel approaches will be important for establishing proof of value. Investigating the most appropriate prediction techniques and identifying key system design changes they will warrant will be an important topic for follow-up work.

In many contexts it is unlikely that a single indicator or sensor will be adequately predictive of veracity or credibility risk [63, 67]. Future systems for border checkpoints, airport security terminals, employment screenings, internal investigations, or financial audits will likely require many predictive indicators to better triangulate and make countermeasures more difficult. Thus, future work will seek to integrate the contributions of this paper into systems that will impact both practical outcomes and understanding of the interrelationships of cognitive and behavioral correlates of veracity.

## Conclusion

This projec t has taken importan t ste ps tow ard def in in g a feasible system design for automated rigidity detection for credibility assessment. The initial study helped identify important technological and process constraints for the system, at the same time generating insight into the rigidity phenomenon. Future work will emphasize prediction and integration of additional noninvasive sensors and automated solutions in an effort to improve on the conceptual design and move it closer to proof of value. As noninvasive, automated credibility assessment systems such as these advance and integrate, the resulting increased understanding and solutions will have potential to revolutionize approaches to managing security and integrity.

ing for this research. Statements provided herein do not necessarily represent the opinions of the funding organizations.

## Note

1. Manipulation check questions involved asking the participants to state whether they had carried anything illicit in their bag and to identify the person to whom they were supposed to deliver the bag.

## Ref renc s

1. Ambach, W.; Bursch, S.; Stark, R.; and Vaitl, D. A concealed information test with multimodal measurement. International Journal of Psychophysiology, 75, 3 (2010), 258–267.

2. Ben-Shakhar, G. Standardization within individuals: A simple method to neutralize individual differences in skin conductance. Psychophysiology, 22, 3 (1985), 292–299.

3. Ben-Shakhar, G. A critical review of the control question test (CQT). In M. K leiner (ed.), Handbook of Polygraph Testing. San Diego: Academic Press, 2002, pp. 103–126.

4. Ben-Shakhar, G., and Elaad, E. The validity of psychophysiological detection of information with the guilty knowledge test: A meta-analytic review. Journal of Applied Psychology, 88, 1 (2003), 131–151.

5. Ben-Shakhar, G.; Bar-Hillel, M.; and Kremnitzer, M. Trial by polygraph: Reconsidering the use of the guilty knowledge technique in court. Law and Human Behavior, 26, 5 (2002), 527–541.

6. Biros, D.P.; George, J.F.; and Zmud, R.W. Inducing sensitivity to deception in order to improve decision making performance: A field study. MIS Quarterly, 26, 2 (2002), 119–144.

7. Blanchard, R.J.; Flannelly, K.J.; and Blanchard, D.C. Defensive behaviors of laboratory and wild Rattus norvegicus. Journal of Comparative Psychology, 100, 2 (1986), 101–107.

8. Bo, X., and Benbasat, I. Product-related deception in e-commerce: A theoretical perspective. MIS Quarterly, 35, 1 (2011), 169–95.

9. Bond, C.F., and DePaulo, B.M. Accuracy of deception judgments. Personality and Social Psychology Review, 10, 3 (2006), 214–234.

10. Bracha, H.S.; Ralston, T.C.; Matsukawa, J.M.; Williams, A.E.; and Bracha, A.S. Does “fight or flight” need updating? Psychosomatics, 45, 5 (2004), 448–449.

11. Bradley, M.M.; Codispoti, M.; Cuthbert, B.N.; and Lang, P.J. Emotion and motivation I: Defensive and appetitive reactions in picture processing. Emotion, 1, 3 (2001), 276–298.

12. Buller, D.B., and Aune, R.K. Nonverbal cues to deception among intimates, friends, and strangers. Journal of Nonverbal Behavior, 11, 4 (1987), 269–290.

13. Buller, D.B., and Burgoon, J.K. Interpersonal deception theory. Communication Theory, 6, 3 (1996), 203–242.

14. Burgoon, J.K.; Jensen, M.; Twyman, N.W.; Meservy, T.O.; Metaxas, D.N.; Michael, N.; Elder, K.; and Nunamaker, J.F., Jr. Automated kinesic analysis for deception detection. In Proceedings of the HICSS-43 Credibility Assessment and Information Quality in Government and Business Symposium. Koloa, HI: IEEE Computer Society, 2010, pp. 31–40.

15. Campbell, B.A.; Wood, G.; and McBride, T. Origins of orienting and defensive responses: An evolutionary perspective. In P.J. Lang, R.F. Simons, and M. Balaban (eds.), Attention and Orienting: Sensory and Motivational Processes. Mahwah, NJ: Lawrence Erlbaum, 1997, pp. 137–164.

16. Carmel, D.; Dayan, E.; Naveh, A.; Raveh, O.; and Ben-Shakhar, G. Estimating the validity of the guilty knowledge test from simulated experiments: The external validity of mock crime studies. Journal of Experimental Psychology: Applied, 9, 4 (2003), 261–269.

17. Caso, L.; Maricchiolo, F.; Bonaiuto, M.; Vrij, A.; and Mann, S. The impact of deception and suspicion on different hand movements. Journal of Nonverbal Behavior, 30, 1 (2006), 1–19.

18. Cherry, E.C. Some experiments on the recognition of speech, with one and with two ears. Journal of the Acoustic Society of America, 25, 5 (1953), 975–979.

19. Cootes, T.F.; Taylor, C.J.; Cooper, D.H.; and Graham, J. Active shape models—Their training and application. Computer Vision and Image Understanding, 61, 1 (1995), 38–59.

20. DePaulo, B.M., and Kirkendol, S.E. The motivational impairment effect in the communication of deception. In J.C. Yuille (ed.), Credibility Assessment. Dordrecht: Kluwer, 1989, pp. 51–70.

21. DePaulo, B.M.; Kirkendol, S.E.; Tang, J.; and O’Brien, T.P. The motivational impairment effect in the communication of deception: Replications and extensions. Journal of Nonverbal Behavior, 12, 3 (1988), 177–201.

22. DePaulo, B.M.; Charlton, K.; Cooper, H.; Lindsay, J.J.; and Muhlenbruch, L. The accuracyconfidence correlation in the detection of deception. Personality and Social Psychology Review, 1, 4 (1997), 346–357.

23. Derrick, D.C.; Elkins, A.C.; Burgoon, J.K.; Nunamaker, J.F., Jr.; and Zeng, D.D. Border security credibility assessments via heterogeneous sensor fusion. IEEE Intelligent Systems, 25, 3 (2010), 41–49.

24. Ekman, P., and Friesen, W.V. Hand movements. Journal of Communication, 22, 4 (1972), 353–374.

25. Elaad, E., and Ben-Shakhar, G. Countering countermeasures in the concealed information test using covert respiration measures. Applied Psychophysiology and Biofeedback, 34, 3 (2009), 197–208.

26. Fanselow, M.S. Neural organization of the defensive behavior system responsible for fear. Psychonomic Bulletin & Review, 1, 4 (1994), 429–438.

27. Fukuda, K. Eye blinks: New indices for the detection of deception. International Journal of Psychophysiology, 40, 3 (2001), 239–245.

28. Fuller, C.M.; Biros, D.P.; Burgoon, J.K.; and Nunamaker, J.F., Jr. An examination and validation of linguistic constructs for studying high-stakes deception. Group Decision and Negotiation, 22, 1 (2013), 117–134.

29. Gamer, M.; Bauermann, T.; Stoeter, P.; and Vossel, G. Covariations among fMRI, skin conductance, and behavioral data during processing of concealed information. Human Brain Mapping, 28, 12 (2007), 1287–1301.

30. Ganis, G.; Kosslyn, S.M.; Stose, S.; Thompson, W.L.; and Yurgelun-Todd, D.A. Neural correlates of different types of deception: An fMRI investigation. Cerebral Cortex, 13, 8 (2003), 830–836.

31. Garrido, E.; Masip, J.; and Herrero, C. Police officers’ credibility judgments: Accuracy and estimated ability. International Journal of Psychology, 39, 4 (2004), 254–275.

32. Glancy, F.H. and Yadav, S.B. A computational model for financial reporting fraud detection. Decision Support Systems, 50, 3 (2011), 595–601.

33. Gray, J.A. The Psychology of Fear and Stress, 2d ed. Cambridge: Cambridge University Press, 1988.

34. Hartwig, M.; Granhag, P.A.; Stromwall, L.A.; and Kronkvist, O. Strategic use of evidence during police interviews: When training to detect deception works. Law and Human Behavior, 30, 5 (2006), 603–619.

35. Humpherys, S.L.; Moffitt, K.C.; Burns, M.B.; Burgoon, J.K.; and Felix, W.F. Identification of fraudulent financial statements using linguistic credibility analysis. Decision Support Systems, 50, 3 (2011), 585–594.

36. Iacono, W.G. Encouraging the use of the guilty knowledge test (GKT ): What the GKT has to offer law enforcement. In B. Verschuere, G. Ben-Shakhar, and E. Meijer (eds.), Memory Detection: Theory and Application of the Concealed Information Test. New York: Cambridge University Press, 2011, pp. 12–24.

37. Jensen, M.L.; Lowry, P.B.; and Jenkins, J.L. Effects of automated and participative decision support in computer-aided credibility assessment. Journal of Management Information Systems, 28, 1 (Summer 2011), 201–233.

38. Jensen, M.L.; Lowry, P.B.; Burgoon, J.K.; and Nunamaker, J.F., Jr. Technology dominance in complex decision making: The case of aided credibility assessment. Journal of Management Information Systems, 27, 1 (2010), 175–201.

39. Jensen, M.L.; Meservy, T.O.; Burgoon, J.K.; and Nunamaker, J.F., Jr. Automatic, multimodal evaluation of human interaction. Group Decision and Negotiation, 19, 4 (2010), 367–389.

40. Kalin, N.H. The neurobiology of fear. Scientific American, 268, 5 (1993), 94–101.

41. Kanaujia, A.; Huang, Y.; and Metaxas, D. Tracking facial features using mixture of point distribution models. Computer Vision, Graphics and Image Processing, 4338 (2006), 492–503.

42. KPMG. Integrity Survey 2005–2006. Amsterdam, 2006.

43. KPMG. Integrity Survey 2008–2009. Amsterdam, 2009.

44. Lang, P.J. The emotion probe: Studies of motivation and attention. American Psychologist, 50, 5 (1995), 371–385.

45. Langleben, D.D. Detection of deception with fMRI: Are we there yet? Legal and Criminological Psychology, 13, 1 (2008), 1–9.

46. Lee, C.C.; Welker, R.B.; and Odom, M.D. Features of computer-mediated, text-based messages that support automatable, linguistics-based indicators for deception detection. Journal of Information Systems, 23, 1 (2009), 5–24.

47. Levine, T.R.; Shaw, A.; and Shulman, H.C. Increasing deception detection accuracy with strategic questioning. Human Communication Research, 36, 2 (2010), 216–231.

48. Lykken, D.T. The GSR in the detection of guilt. Journal of Applied Psychology, 43, 6 (1959), 385–388.

49. Lykken, D.T. The validity of the guilty knowledge technique: The effects of faking. Journal of Applied Psychology, 44, 4 (1960), 258–262.

50. Lykken, D.T. Psychology and the lie detector industry. American Psychologist, 29, 10 (1974), 725–739.

51. Lykken, D.T. A Tremor in the Blood: Uses and Abuses of the Lie Detector. New York: Plenum Trade, 1998.

52. MacLaren, V.V. A quantitative review of the guilty knowledge test. Journal of Applied Psychology, 86, 4 (2001), 674–683.

53. Matsuda, I.; Hirota, A.; Ogawa, T.; Takasawa, N.; and Shigemasu, K. Within-individual discrimination on the concealed information test using dynamic mixture modeling. Psychophysiology, 46, 2 (2009), 439–449.

54. Meijer, E.; Verschuere, B.; and Merckelbach, H. Detecting criminal intent with the concealed information test. Open Criminology Journal, 3 (2010), 44–47.

55. Meservy, T.O.; Jensen, M.L.; Kruse, J.; Burgoon, J.K.; and Nunamaker, J.F., Jr. Automatic extraction of deceptive behavioral cues from video. In P. Kantor, G. Muresan, F. Roberts, D. Zeng, F.-Y. Wang, H. Chen, and R. Merkle (eds.), Proceedings of the IEEE International Conference on Intelligence and Security Informatics (ISI 2005). Berlin: Springer, pp. 198–208.

56. Meservy, T.O.; Jensen, M.L.; Kruse, J.; Burgoon, J.K.; Nunamaker, J.F., Jr.; Twitchell, D.P.; Tsechpenakis, G .; and Metaxas, D.N. Deception detection through automatic, unobtrusive analysis of nonverbal behavior. IEEE Intelligent Systems, 20, 5 (2005), 36–43.

57. Nakayama, M. Practical use of the concealed information test for criminal investigation in Japan. In M. K leiner (ed.), Handbook of Polygraph Testing. San Diego: Academic Press, 2002, pp. 49–86.

58. National Research Council. The Polygraph and Lie Detection. Committee to Review the Scientific Evidence on the Polygraph (ed.). Washington, DC: National Academies Press, 2003.

59. Nunamaker, J.F., Jr., and Briggs, R.O. Toward a broader vision for information systems. ACM Transactions on Management Information Systems, 2, 4 (2011), article 20.

60. Nunamaker, J.F., Jr.; Chen, M.; and Purdin, T.D.M. Systems development in information systems research. Journal of Management Information Systems, 7, 3 (Winter 1990–91), 89–106.

61. Nunamaker, J.F., Jr.; Twyman, N.W.; and Giboney, J.S. Breaking out of the design science box: High-value impact through multidisciplinary design science programs of research. In Proceedings of the Nineteenth Americas Conference on Information Systems. Chicago: Association for Information Systems, 2013.

62. Nunamaker, J.R., Jr.; Briggs, R.O.; Mittleman, D.D.; Vogel, D.R.; and Balthazard, P.A. Lessons from a dozen years of group support systems research: A discussion of lab and field findings. Journal of Management Information Systems, 13, 3 (Winter 1996–97), 163–207.

63. Nunamaker, J.F., Jr.; Derrick, D.C.; Elkins, A.C.; Burgoon, J.K.; and Patton, M.W. Embodied conversational agent–based kiosk for automated interviewing. Journal of Management Information Systems, 28, 1 (Summer 2011), 17–48.

64. Nunamaker, J.F., Jr.; Burgoon, J.K.; Twyman, N.W.; Proudfoot, J.G.; Schuetzler, R.; and Giboney, J.S. Establishing a foundation for automated human credibility screening. In Proceedings of the 2012 IEEE International Conference on Intelligence and Security Informatics. Los Alamitos, CA: IEEE Computer Society, 2012, pp. 202–211.

65. Osugi, A. Daily application of the concealed information test: Japan. In B. Verschuere, G. Ben-Shakhar, and E. Meijer (eds.), Memory Detection: Theory and Application of the Concealed Information Test. Cambridge: Cambridge University Press, 2011, pp. 253–275.

66. Patton, M.W. Decision support for rapid assessment of truth and deception using automated assessment technologies and kiosk-based embodied conversational agents. Ph.D. dissertation, University of Arizona, Tucson, 2009.

67. Porter, S., and ten Brinke, L. The truth about lies: What works in detecting high-stakes deception? Legal and Criminological Psychology, 15, 1 (2010), 57–75.

68. Roelofs, K.; Hagenaars, M.A.; and Stins, J. Facing freeze: Social threat induces bodily freeze in humans. Psychological Science, 21, 11 (2010), 1575–1581.

69. Schenberg, L.C.; Vasquez, E.C.; and Dacosta, M.B. Cardiac baroreflex dynamics during the defense reaction in freely moving rats. Brain Research, 621, 1 (1993), 50–58.

70. Shan, L.; Tsechpenakis, G.; Metaxas, D.N.; Jensen, M.L.; and Kruse, J. Blob analysis of the head and hands: A method for deception detection. In R.H. Sprague (ed.), Proceedings of the 38th Annual Hawaii International Conference on System Sciences. Washington, DC: IEEE Computer Society, 2005.

71. Silver, M.S.; Markus, M.L.; and Beath, C.M. The information technology interaction model: A foundation for the MBA core course. MIS Quarterly, 19, 3 (1995), 361–390.

72. Sokolov, E.N. Higher nervous functions—Orienting reflex. Annual Review of Physiology, 25, 1 (1963), 545–580.

73. Sporer, S.L., and Schwandt, B. Moderators of nonverbal indicators of deception—A meta-analytic synthesis. Psychology, Public Policy, and Law, 13, 1 (2007), 1–34.

74. Stana, R.M. Moving illegal proceeds: Opportunities exist for strengthening the federal government’s efforts to stem cross-border currency smuggling. Testimony before the Senate Caucus on International Narcotics Control, Washington, DC, 2011.

75. Strömwall, L.A., and Granhag, P.A. How to detect deception? Arresting the beliefs of police officers, prosecutors and judges. Psychology, Crime & Law, 9, 1 (2003), 19–36.

76. Strömwall, L.A.; Granhag, P.A.; and Hartwig, M. Practitioners’ beliefs about deception. In P.A. Granhag and L.A. Strömwall (eds.), The Detection of Deception in Forensic Contexts. New York: Cambridge University Press, 2004, pp. 229–250.

77. Twyman, N.W.; Burgoon, J.K.; and Nunamaker, J.F., Jr. Non-invasive screening for concealed information. In R.H. Sprague (ed.), Proceedings of the 44th Annual Hawaii International Conference on System Sciences. Koloa, HI: IEEE Computer Society, 2011.

78. Twyman, N.W.; Burgoon, J.K.; Elkins, A.C.; and Proudfoot, J.G. Alternative cues in concealed information testing. In R.H. Sprague (ed.), Proceedings of the 46th Annual Hawaii International Conference on System Sciences. Maui, HI: IEEE Computer Society, 2013.

79. Twyman, N.W.; Moffitt, K.; Burgoon, J.K.; and Marchak, F. Using eye tracking technology as a concealed information test. In R.H. Sprague (ed.), Proceedings of the 43rd Annual Hawaii International Conference on System Sciences. Koloa, HI: IEEE Computer Society, 2010.

80. Verschuere, B.; Ben-Shakhar, G.; and Meijer, E. Memory Detection: Theory and Application of the Concealed Information Test. Cambridge: Cambridge University Press, 2012.

81. Verschuere, B.; Crombez, G.; de Clercq, A.; and Koster, E.H.W. Autonomic and behavioral responding to concealed information: Differentiating orienting and defensive responses. Psychophysiology, 41, 3 (2004), 461–466.

82. Verschuere, B.; Crombez, G.; de Clercq, A.; and Koster, E.H.W. Psychopathic traits and autonomic responding to concealed information in a prison sample. Psychophysiology, 42, 2 (2005), 239–245.

83. Verschuere, B.; Crombez, G.; Smolders, L.; and de Clercq, A. Differentiating orienting and defensive responses to concealed information: The role of verbalization. Applied Psychophysiology and Biofeedback, 34, 4 (2009), 237–244.

84. Viola, P., and Jones, M.J. Robust real-time face detection. International Journal of Computer Vision, 57, 2 (2004), 137–154.

85. Vrij, A. Behavioral correlates of deception in a simulated police interview. Journal of Psychology, 129, 1 (1995), 15–28.

86. Vrij, A., and Mann, S. Telling and detecting lies in a high-stake situation: The case of a convicted murderer. Applied Cognitive Psychology, 15, 2 (2001), 187–203.

87. Vrij, A.; Mann, S.; and Fisher, R.P. An empirical test of the behaviour analysis interview. Law and Human Behavior, 30, 3 (2006), 329–345.

88. Vrij, A.; Semin, G.R.; and Bull, R. Insight into behavior displayed during deception. Human Communication Research, 22, 4 (1996), 544–562.

89. Vrij, A.; Granhag, P.A.; Mann, S.; and Leal, S. Outsmarting the liars: Toward a cognitive lie detection approach. Current Directions in Psychological Science, 20, 1 (2011), 28–32.

90. Zhou, L., and Zhang, D. Following linguistic footprints: Automatic deception detection in online communication. Communications of the ACM, 51, 9 (2008), 119–122.

91. Zhou, L.; Burgoon, J.K.; Nunamaker, J.F., Jr.; and Twitchell, D.P. Automating linguisticsbased cues for detecting deception in text-based asynchronous computer-mediated communication. Group Decision and Negotiation, 13, 1 (2004), 81–106.

92. Zuckerman, M.; DePaulo, B.M.; and Rosenthal, R. Verbal and nonverbal communication of deception. Advances in Experimental Social Psychology, 14, 1 (1981), 1–59.

## Appendix

The e xpe rimen ts in this in ve stigation we re de signe d w ith a le ve l of re alism. As such, it was important to gauge whether participants approached the interviews with a reasonable level of motivation, effort, and tension. The manipulation check questions used are included in Tables A1 and A2.

Table A1. Self-Report Questions for Experiment 1 (Seven-Point Scale)

<table><tr><td>Measure</td><td>Question</td></tr><tr><td>Motivation to succeed</td><td>During the interview, how important was it to you to succeed in making the interviewer believe you?</td></tr><tr><td>Effort</td><td>How hard did you try to convince the interviewer that you were telling the truth?</td></tr><tr><td>Tension</td><td>How tense did you feel during the interview?</td></tr></table>

Table A2. Self-Report Questions for Experiment 2 (Five-Point Scale)

<table><tr><td>Measure</td><td>Question</td></tr><tr><td>Motivation to succeed</td><td>During the interview, how important was it to you to succeed in making the interviewer believe you?</td></tr><tr><td>Effort</td><td>How hard did you try to convince the interviewer that you were telling the truth?</td></tr><tr><td>Tension</td><td>How much do you agree (or disagree) with the following statement? I was tense during the screening process.</td></tr></table>
