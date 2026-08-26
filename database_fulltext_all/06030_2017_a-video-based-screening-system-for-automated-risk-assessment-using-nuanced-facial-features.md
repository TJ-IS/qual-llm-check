---
otero_id: 6030
otero_key: "GF59YPKG"
title: "A Video-Based Screening System for Automated Risk Assessment Using Nuanced Facial Features"
authors: "Steven J. Pentland; Nathan W. Twyman; Judee K. Burgoon; Jay F. Nunamaker; Christopher B.R. Diller"
year: "2017"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2017.1393304"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Video-Based Screening System for Automated Risk Assessment Using Nuanced Facial Features

Steven J. Pentland, Nathan W. Twyman, Judee K. Burgoon, Jay F. Nunamaker Jr. & Christopher B.R. Diller

To cite this article: Steven J. Pentland, Nathan W. Twyman, Judee K. Burgoon, Jay F. Nunamaker Jr. & Christopher B.R. Diller (2017) A Video-Based Screening System for Automated Risk Assessment Using Nuanced Facial Features, Journal of Management Information Systems, 34:4, 970-993, DOI: 10.1080/07421222.2017.1393304

To link to this article: https://doi.org/10.1080/07421222.2017.1393304

![](/api/attachments/GF59YPKG/fulltext/images/f14040abeed649ad4309700e324362930f81854e08ffec3f79e8805d9c47d421.jpg)

Published online: 02 Jan 2018.

![](/api/attachments/GF59YPKG/fulltext/images/c789ba955776f13f3f84230036581c9e1e700984a40d1f26fe999b7ce0801fcf.jpg)

Submit your article to this journal

![](/api/attachments/GF59YPKG/fulltext/images/d72e1e7e68368b1470cfb3dfac710f62720a885baba88cb62bd69f3ddf1b3c3d.jpg)

View related articles

![](/api/attachments/GF59YPKG/fulltext/images/1957662801574b46cfad247661a9dd9d65ec6ead2fa1bd4787f2d61fcdd1f97a.jpg)

View Crossmark data

# A Video-Based Screening System for Automated Risk Assessment Using Nuanced Facial Features

STEVEN J. PENTLAND, NATHAN W. TWYMAN, JUDEE K. BURGOON, JAY F. NUNAMAKER JR., AND CHRISTOPHER B.R. DILLER

STEVEN J. PENTLAND (spentland@cmi.arizona.edu; corresponding author) is a Ph.D. student at the University of Arizona. His research interests include interpersonal deception, affective computing, and automated interviewing. His work focuses on the extraction and analysis of nonverbal behaviors using remote sensing technology. He has contributed to a variety of projects supported by the National Science Foundation, Department of Homeland Security, and the Department of Defense.

NATHAN W. TWYMAN (twymann@mst.edu) is an assistant professor of business and information technology at the Missouri University of Science and Technology. He received his Ph.D. in management information systems (IS) from the University of Arizona. His interests span the research on human–computer interaction, decision support systems and group support systems, virtual communities, credibility assessment systems, and health IS. He has been a principal investigator of and key contributor to research grants from the National Science Foundation, the Department of Homeland Security, and the Department of Defense. His industry experience is in data management, business intelligence, strategic planning, training, and electronics. His research is published in Journal of Management Information Systems, Journal of the AIS, and Information and Management.

JUDEE K. BURGOON (jburgoon@cmi.arizona.edu) is professor of communication, family studies and human development. She is the director of research for the Center for the Management of Information and site director for the National Science Foundation– sponsored Center for Identification Technology Research at the University of Arizona. She holds a doctorate in communication and educational psychology from West Virginia University. She has authored or edited 14 books and monographs and over 300 articles, chapters, and reviews related to nonverbal and relational communication, deception, the impact of new communication technologies on human–human and human–computer interaction, research methods, and public opinion toward the media. Her research has been supported by the National Science Foundation, the Department of Defense, the Department of Homeland Security, the National Center for Credibility Assessment, the National Institutes of Mental Health, and others.

JAY F. NUNAMAKER JR. (jnunamaker@cmi.arizona.edu) is Regents and Soldwedel Professor of MIS, Computer Science and Communication and director of the Center for the Management of Information and the National Center for Border Security and Immigration at the University of Arizona. He received his Ph.D. in operations research and systems engineering from Case Institute of Technology. He has held a professional engineer’s license since 1965. He was inducted into the Design Science Hall of Fame and received the LEO Award for Lifetime Achievement from the Association for Information Systems. He was featured in the July 1997 issue of Forbes Magazine on technology as one of eight key innovators in information technology. His specialization is in the fields of system analysis and design, collaboration technology, and deception detection. The commercial product GroupSystems ThinkTank, based on his research, is often referred to as the gold standard for structured collaboration systems. He founded the MIS Department at the University of Arizona in 1974 and served as department head for 18 years.

CHRISTOPHER B.R. DILLER (cdiller@unomaha.edu) is an instructor at the College of Business Administration, University of Nebraska at Omaha (UNO). He earned a Ph.D. in management information systems from the Eller College of Management at the University of Arizona. His research interests include dynamic collaboration, collaboration in large groups, group support systems, rapid screening technology, change management, economics of informatics, data fusion, decision support systems, and strategic system development methodologies. He serves as the director of Facilitation and Systems Development for the Center for Collaboration Science at UNO. He is recognized as a world-class facilitator, with over 25 years of experience, helping groups develop effective solutions to a broad array of highly complex, time-sensitive challenges.

ABSTRACT: This study investigates the development of an automated interviewing system that uses facial behavior as an indicator of the risk of given illicit behavior. Traditional facial emotion indicators of risk in semistructured dialogue may have limitations in an automated approach. However, an initial analysis of mock crime interviews suggests that the face may exhibit some form of rigidity during highly structured interviews. An interviewing system design using facial rigidity analysis was implemented and experimentally evaluated, the results of which further reveal that the rigidity is fairly generalized across the face. Whereas existing theory traditionally focuses on leakage of facial expressions, this study provides evidence that neutralization of facial expression may be a valuable alternative for automated interviewing systems. The proof-of-concept system in this study may help human risk assessment move beyond traditional boundaries, into fields such as auditing, emergency room management, and security screening.

KEY WORDS AND PHRASES: automated interviewing, credibility assessment, deception detection, facial expression recognition, facial rigidity analysis, risk assessment.

Automated interviewing systems are increasingly called upon to accurately and efficiently collect and process data for decision support. An example is seen in the growing use of asynchronous video interview systems by industry as a method of screening job applicants early in the hiring process. In situations where companies are inundated with applications for a single position, the use of a system that centralizes prescreening interviews through an automated online platform reduces the time and cost associated with screening job candidates. Similar systems designed to process documents, collect information, answer questions, and sell goods are becoming common in environments associated with high volumes of human traffic. Systems such as self-checkouts, customer service kiosks, and security screening terminals demonstrate the business value of scalable systems for human-flow processing.

Most of these systems rely on information that is directly submitted by the human user, but fail to account for emotions, intent, demeanor, and other nuanced cues important to context during human interactions. Nuanced behavioral analytics may further increase the value of automated interviewing systems. An example context where added value is clear is the identification of mal-intent in areas such as immigration, corporate espionage, and fraud investigations. To this end, this study investigates the potential for a human interviewing system that examines video footage for facial behaviors that indicate a person’s likelihood of involvement in a specified illicit behavior.

Recent information systems (IS) research has introduced the idea of structured interviewing systems that assess an individual’s risk of such involvement. And yet, to find application in common organizational processes, these systems will need to favor noninvasive sensors rather than contact sensors such as those typically used in a polygraph-based screening. A typical web cam can capture video of the face, and is commonly available in business, government, and home environments. Given its commonality and ease of deployment, a video camera may be the most practical mechanism for collecting behavioral data. This simple device combined with computer vision algorithms has the potential to track the heart rate of a patient during a telehealth consultation, estimate the demeanor of a customer, or identify uncertainty during job candidate screenings. To the extent this data could be diagnostic and a system could effectively harness it in an interviewing paradigm, the potential for impact could be widespread. This was the inspiration for this study.

The human face communicates much more than words. Facial expressions can communicate ideas, give context, convey emotion, and reveal strength of conviction. People rely on facial cues to glean both intentional and unintentional meaning. With so much communicated by the face, it is natural that facial expressions have been investigated for possible cues to deception for decades. Microexpressions, macroexpressions, and facial pleasantness are example behaviors examined for their potential to indicate the possibility of illicit behavior [7].

Only recently has the possibility of automated interviewing for human risk assessment been possible. Most research to date has used trained human coders to identify facial behaviors helpful for this context. Advances in computer vision now provide for the possibility of detecting facial movement variations on a more granular scale than the human eye can perceive. This provides additional opportunities for discovering indicators of dishonest communication not normally detectable by human perception [36].

Further, when analyzing the human face, related credibility and deception research has generally focused on affective facial expressions. “Leaked” affective expressions have been proposed as a means of determining concealed true emotional states [12]. However, while people may sometimes struggle forcing certain facial expressions, they do seem to have some skill at neutralizing all emotion on their face [30]. Thus, while certain facial emotion may have merit as cues to deception, this study ultimately considers using a different kind of facial behavior to gauge risk—facial rigidity, or lack of facial movement.

Remaining still can be easier than generating an animated expression. In many situations, a deceiver more aptly shows no expression rather than trying to display fake expressions. Human interviewing system processes may be designed to encourage such behavior. In such cases, facial rigidity may be a common and useful indicator of low-credibility answers or outright deception. This study investigates the possibility of facial rigidity and how it might best be harnessed in an automated interviewing system as outlined in Figure 1.

## Research Approach

This study takes a design science approach to generating knowledge. It implements Nunamaker et al.’s [27, 28] design science framework, following its prescription for producing proof-of-concept: a novel type of information system is progressively developed using iterative development and evaluation, with each step providing insight into definition, necessary affordances, possible explanations, and theoretical boundaries for the phenomena involved.

This study implements that approach by first conducting a post hoc exploration of facial movement data obtained from an initial broad-ranging experiment. Results of this exploratory analysis are followed by a second experimental evaluation in an automated screening context. Knowledge gained from the process reveals the potential drivers of facial rigidity. Evaluation outcomes provide researchers and practitioners with evidence and insight toward the potential of systematic facial rigidity analysis for risk assessment.

## Literature Review

Identifying the source of illicit behaviors such as theft of intellectual property or trafficking can be very difficult. Perpetrators hide their actions through careful deceit or misdirection. Yet, when this concealment behavior arouses suspicion, investigatory resources can be appropriately employed. However, in human-to-human dialogue, no single behavioral or physiological variation correlates perfectly with deception [7]. Given the differentiated nature of human behavior, the perfect predictor—a “Pinocchio’s nose”—will not likely be discovered. Addressing this likelihood, recent information systems research has demonstrated that simultaneous evaluation of multiple behavioral and psychophysiological signals may increase the probability of identifying deception [9, 43].

![](/api/attachments/GF59YPKG/fulltext/images/e531aa5fb6e79f13f525fee54c05542d5abc02f220f105f432e0619578a89d42.jpg)  
Figure 1. Controlled Interview System for Facial Rigidity Analysis

However, the mechanics underlying those behaviors must be understood well enough to assess their reliability as risk assessment indicators, and to most effectively harness their potential in an interviewing system design. To create a reliable automated human screening system, researchers first must undertake a careful feature selection process to understand the idiosyncrasies of each human signal. Otherwise, the reliability and scientific value of prediction algorithms that use the cues as inputs remains unknown. Thus, it is important not only to identify a potential indicator of deception but also to explore its boundaries, requirements, and affordances.

## Automated Human Screening Systems

For gauging risk of illicit behavior, the most common tool used in practice is a polygraph [19, 20, 45]. But polygraph-based screening is unwieldy, expensive, timeconsuming, and invasive [37]. The most popular polygraph-based screening methods are criticized for lacking reliability and validity [1, 21, 22]. Information systems research has responded by proposing systems that use noncontact sensors (e.g., video cameras) together with automated interviewing [24] to screen individuals in a given scenario and provide an assessment of threat or deception. These proposed systems have taken the form of a stand-alone kiosk [25, 43], a typical desktop workstation [41], or an installed application [10]. Interviews are conducted by a virtual agent that communicates via text [44], a disembodied voice [40], or an embodied conversational agent [8]. Such systems have potential application in areas as diverse as trusted traveler programs [26], fraud auditing and policy compliance assessment [42], and criminal investigations [32].

At least two general design frameworks have been proposed for this new class of information systems. One design [8, 25] uses a kiosk-based interview with openended questions that mimic a human-to-human interaction, providing for the incorporation of interpersonal deception theories into the design. Only noninvasive, automatically calibrated sensors are used to capture behavioral and psychophysiological responses in addition to verbal responses. Raw data are captured and translated into useful behavioral indicators, which are then used as inputs for a classification algorithm that generates a risk assessment.

A second design also uses noninvasive sensors, new deception indicators, and a decision engine, but emphasizes heavy scientific control [40] in the computer-driven interview. This design calls for a block of only binary response (yes-or-no) questions for each topic of interest. The block contains baseline questions for which all responses are certain to be truthful, as well as Target questions that ask about the behavior of interest for which risk is being assessed. The questions are designed such that interviewees always respond with the same “no” response, whether truthful or not. This general design controls for much of the variance attributed to interviewer skill and demeanor, examinee mood and general nervousness, and question type and delivery.

Both designs acknowledge the need to discover both psychophysiological variations and behavioral modifications that are useful and usable in an automated, standardized interview. Though several such behavioral indicators have been identified in a variety of other contexts [38], it is clear that no single indicator is perfectly reliable [7], and contextual and individual factors can influence the type or strength of deception indicators [3]. Thus, it is important to (1) discover risk indicators that can be captured by these new systems, and (2) learn how to design systems in a manner that most effectively elicits these indicators.

## Background on the Face in Deception Detection

One of the more obvious human features for seeking truth is the face. The face is the focal point of the body during communication not only due to the vocal functions of the mouth but also because of the expressive power of facial muscles. Most of the relevant research on facial behaviors during interviews comes from deception detection research. The bulk of deception detection research dealing with the face has primarily relied on the presence or absence of facial emotions, and the initial motivation of this study was to examine facial emotions within the new context of automated screening systems.

This area of research has commonly cited leakage as the underlying mechanism causing variations in facial behavior. The leakage hypothesis posits that a person’s true feelings will be detectable during deception despite the person’s best efforts to tell a credible lie [12]. Proponents of the leakage hypothesis claim that the face will show signs of fear, anger, or contempt during deception even though an individual may be doing his or her best to conceal these feelings. Related research has also indicated that people often show more negative valence during dishonest communication [7].

However, a major drawback when relying on facial emotions as inputs for risk assessment systems is how well people can control their emotional displays. Compared to other communication channels, the face is much more controllable [5, 12, 48, 49]. From an early age, humans learn display rules that dictate the emotions that should be displayed in varying contexts [11]. By learning and practicing these display rules from a young age, humans become experts at controlling their facial emotions.

Simulating, masking, and neutralizing are tactics humans employ when trying to conceal felt emotions [14]. Simulating an expression refers to presenting a facial emotion that is not connected to a felt emotion; masking involves disguising felt emotions; and neutralizing is an attempt to conceal any type of emotional valence. Some of these tactics are relatively easier for humans to convincingly employ. For example, Porter and ten Brinke [30] found no discernible difference between genuine and falsified neutral expressions. In other words, people are very good at neutralizing—making their faces appear unemotional. The same research also indicated that people are better at fabricating positive emotions compared to negative emotions. This likely stems from social pressures to appear positive.

## Theoretical Case for Facial Rigidity

The controllability of the face was initially thought to be a drawback to the idea of using facial behavioral cues in an automated screening system design, because it might bring reliability into question: a successful system would need to rely on indicators that both appear consistently and are hard for people to control.

However, instead of emotional valence, more appropriate features for an interviewing system may stem from neutralization patterns in the face. This study proposes that the lack of facial movement, or increase in facial rigidity, has the potential to be both a reliable and a prevalent feature. Deception research has indicated that deceivers tend to reduce kinesic (i.e., body movement) behavior [7, 13, 38, 44, 46]. This rigidity has been found to occur in the trunk, limbs, and head. Further, in two studies where participants were told about the discriminating corollaries of rigidity, results indicated they were still unable to conceal rigidity [43, 47].

At least two relevant explanations have been proposed for the source of kinesic rigidity: (1) an autonomic freeze response to perceived threat, and (2) an overt behavioral attempt to appear truthful. The autonomic freeze response occurs when an individual perceives a stimulus as threatening: the body enters what has been colloquially referred to as a “fight-or-flight” response, which involves body movement freezing or diminishing [17]. The perceived threat can be either physical or social in nature [33]. This freezing effect may explain some observed body and head rigidity, and it may also affect the face.

The second possible explanation stems from the generally held belief that people who are deceptive show increased movement. Though this belief is widespread, normally deceivers do not display increased movement. Some research has postulated that deceivers purposefully inhibit their own movement in an attempt to appear truthful, thereby creating the bodily rigidity seen in prior research [6]. Since facial emotional control is a well-practiced behavior, it seems likely that deceivers could extend such overt behavioral control to the face.

Nevertheless, it is also possible that such behavioral control could more commonly result in a masking rather than a neutralizing behavior, in which case no facial rigidity would occur. Results from an initial investigation unveiled unexpected facial behavior that led to these rigidity considerations and subsequently to a full investigation into the possibility of a facial rigidity-based risk interviewing system.

## Initial Investigation

A mock theft experiment was conducted with the original intent to evaluate the potential of various noncontact technologies for technology-based human risk assessment. Participants (N = 164) were recruited from the local community, and underwent an elaborate process of receiving clandestine instructions, stealing an item, and finally being interviewed by a professional polygraph examiner while various sensors collected data. Standard-definition video was among the data obtained, and an initial analysis resulted in the discovery of rigidity in body movement. This earlier discovery of bodily rigidity, together with the previously described theoretical foundation, inspired the idea of looking for facial rigidity in a follow-up analysis. Full details of the experiment have been published elsewhere; reported here are only those aspects relevant to the current topic.

## Experimental Task

Tasks for both experiments reported in this article were elaborately planned with the goal of increasing realism and perceived stakes, which is important for eliciting psychological and behavioral indicators of deception that are reflective of real-world highstake situations [31]. In this study, participants arrived at a prescheduled location where they received instructions only from an ominous audio recording. The use of the recording was designed to remove research personnel from the instruction process and reduce the effects of sanctioning. The recording instructed participants to proceed to an office building on an upper floor and ask for a Mr. Carlson. When the secretary left to find Mr. Carlson, they were to find a key left on the desk, open a cash box, steal a diamond ring, and hide it somewhere on their person. Participants then waited for the secretary to return. Participants in a control group were given no such instructions to steal a ring and instead simply waited. Upon returning and finding the participant waiting, the (confederate) secretary told them to go to a different location in the building. Upon arriving at the new location, participants were told they would be interviewed regarding a crime that had occurred in the building. A professional polygraph examiner conducted a multipart interview, while various sensors collected data, including video footage of the face (see Figure 2). Although participants were not explicitly told to lie, they were incentivized by a cash reward to appear innocent during the interview.

![](/api/attachments/GF59YPKG/fulltext/images/399b1b743f93bb0b896fae313355df147bee05c49e7eefab4406bd182f4a91e2.jpg)  
Figure 2. Participant Being Interviewed About Theft

Each interview consisted of sequential but distinct interviewing procedures. The procedure most relevant to the current investigation was a concealed information test (CIT), a highly controlled, multiple-choice question interviewing method that compares responses during incorrect (baseline) answers to responses during correct (Target) answers [2]. The CIT’s scripted questions require very short, uniform responses, minimizing effects of interviewer style, demeanor, and skill. After repeating a word as requested by the interviewer, the interviewer and examinee sit in silence for about 5 to 15 seconds before moving on to the next repetition. Table 1 shows the CIT questions used by the polygraph examiners in this study. The CIT questions were designed to target only those things that were certain to have required conscious attention from the perpetrator.

Because of the simplicity of the communication requirements, there was no need for examinees to vary facial expressions to help convey a concept or to vary facial animation to assist in describing an idea. Unlike related studies that have examined kinesic behaviors while examinees used gestures, facial expressions, and other verbal and nonverbal behaviors while responding to questions, very little movement of any kind occurred throughout this portion of the interview. After the interview, each participant was debriefed and received monetary compensation for their participation. Video data from the CIT portion of the interview was used for this followup analysis.

Table 1. Questions Used in Study 1 Experiment Interview

<table><tr><td>Question</td><td>Words repeated by suspect</td></tr><tr><td>1. “If you are the person who stole the ring, you are familiar with details of the cash box it was stored in. Repeat after me these cash box colors:”</td><td>GreenBeigeWhiteBlueBlackRed</td></tr><tr><td>2. “If you are the person who stole the ring, you moved an object in the desk drawer to locate the cash box containing the ring. Repeat after me these objects:”</td><td>NotepadTelephone bookWoman’s sweaterLaptop bagTissue boxBrown purse</td></tr><tr><td>3. “If you are the person who stole the ring, you know what type of ring it was. Repeat after me these types of rings:”</td><td>Emerald ringTurquoise ringAmethyst ringDiamond ringRuby ringGold ring</td></tr></table>

Note: Target Items (i.e., correct answers) are in bold.

## Analysis and Results

Standard definition video was recorded using studio-quality video cameras. Videos from the interviews were post-processed using the computer expression recognition toolbox (CERT) [18], which estimates the intensity of six basic emotions (anger, disgust, fear, joy, sadness, surprise) for each frame of video.

Due to 24 audio-video recording failures, 2 nonconsents, 4 confessions, and 19 failures to follow instructions, 49 participants were removed from the study. Video from another 20 participants could not be processed with CERT due to corrupted video files. The data analysis included 95 total participants (Guilty = 37; Innocent = 58). The imbalance between the number of Guilty and Innocent participants is the result of higher disqualification rates for Guilty subjects. For instance, participants in the Guilty condition were less likely to follow illicit instructions, thus disqualifying them from the experiment.

Dependent variables in a multivariate analysis included standardized average emotion intensity across the duration of a subject’s response. Six emotions were measured. Independent variables included experimental condition (a binary variable coded as 1 for Guilty and 0 for Innocent participants), and Target Stimulus (coded as 1 when responding to target stimulus and 0 otherwise). Interaction effects of Guilt and Target were the key independent variables of interest. The overall model showed significance in Target Stimulus, $F ( 1 , \ 6 ) = 4 . 3 8 , \ p { < } . 0 0 1$ , but not the Guilt and

Table 2. Multivariate Regression Results for Average Facial Emotion Intensity

<table><tr><td>Emotion</td><td>Guilt $\beta$  (S.E.)</td><td>Target Stimulus $\beta$  (S.E.)</td><td>Guilt  $\times$  Target Stimulus $\beta$  (S.E.)</td></tr><tr><td>Anger</td><td>0.02(0.05)</td><td>0.01(0.08)</td><td>-0.11(0.12)</td></tr><tr><td>Disgust</td><td>0.02(0.05)</td><td>-0.15(0.08)*</td><td>-0.12(0.12)</td></tr><tr><td>Fear</td><td>0.02(0.05)</td><td>0.02(0.08)</td><td>-0.12(0.12)</td></tr><tr><td>Joy</td><td>-0.02(0.05)</td><td>-0.26(0.08)*</td><td>0.10(0.12)</td></tr><tr><td>Sadness</td><td>0.01(0.05)</td><td>-0.06(0.08)</td><td>-0.06(0.12)</td></tr><tr><td>Surprise</td><td>0.03(0.05)</td><td>-0.04(0.08)</td><td>-0.15(0.12)</td></tr></table>

Note: \*p<:05; statistically significant results are in bold.

Table 3. Multivariate Regression Results for Variance in Facial Emotion Intensity

<table><tr><td>Emotion</td><td>Guilt $\beta$  (S.E.)</td><td>Target Stimulus $\beta$  (S.E.)</td><td>Guilt  $\times$  Target Stimulus $\beta$  (S.E.)</td></tr><tr><td>Anger</td><td>0.03(0.05)</td><td>-0.03(0.08)</td><td>-0.16(0.12)</td></tr><tr><td>Disgust</td><td>0.04(0.05)</td><td>-0.15(0.08)*</td><td>-0.24(0.12)*</td></tr><tr><td>Fear</td><td>0.04(0.05)</td><td>-0.04(0.08)</td><td>-0.26(0.12)*</td></tr><tr><td>Joy</td><td>0.00(0.05)</td><td>-0.22(0.08)*</td><td>-0.01(0.12)</td></tr><tr><td>Sadness</td><td>0.05(0.05)</td><td>-0.06(0.08)</td><td>-0.29(0.12)*</td></tr><tr><td>Surprise</td><td>0.06(0.05)</td><td>-0.06(0.08)</td><td>-0.36(0.12)*</td></tr><tr><td colspan="4">Note: *p&lt;.05; statistically significant results are in bold.</td></tr></table>

Target interaction, $F ( 1 , \ 6 ) = 0 . 8 5 , \ p = 0 . 5 3$ . Model results for each emotion are summarized in Table 2.

Next, the variance in emotional intensity across the duration of a subject’s response was calculated. These values were also standardized and included as dependent variables in a multivariate model. In this case, both Target, $F ( 1 , 6 ) = 4 . 8 9 , \ p { < } . 0 0 1$ , and Guilt and Target interaction, $F ( 1 , 6 ) = 2 . 5 3 , p { < } . 0 5 ,$ had significant effects. Model results for variance in each emotion are summarized in Table 3. Four of the six emotions analyzed had significantly reduced variance for Guilty subjects during deception.

There was a main effect of Target for two of the emotions, meaning when both Guilty and Innocent examinees were repeating the correct answer, the variance of joy and disgust on their faces decreased. The cause of these main effects is unclear, but it could stem from the fact that different words were spoken for the correct answer as compared to baseline responses. The differences in mouth movement between words may affect variance in certain portions of the face in a manner that happens to correlate with facial emotion. A second possibility is that human interviewers sometimes unknowingly signaled higher significance of correct answers. Study 2 was designed to control for these factors.

## Study 1 Discussion

The results of the initial analysis revealed no significant difference in intensity of facial emotion among Guilty participants when repeating Target answers, as compared to repeating nonTarget answers. This does not show any evidence of masking, meaning those trying to hide their nefarious behavior from the polygraph examiner did not appear to suddenly mask their fear or nervousness with an alternative expression, or at least not with any expression listed in Table 2.

Previous research (e.g., [7, 12, 15, 35]) citing emotional correlates of deception suggests that facial emotions of Guilty subjects should distinguish them from Innocent subjects during Target items. However, in this case no significant interaction effects were found.

There was, however, a significant decrease in the variance in facial emotion intensity for each Guilty participant, when compared to the participant’s own movement during baseline responses. Put simply, facial emotion did not change much when Guilty interviewees were actively repeating the Target words that represented their illicit behavior. Whatever emotions were expressed on their face during this phase remained relatively static. Natural minor fluctuations seen in their facial emotion during baseline responses were muted during Target responses. This trend was seen for all emotional displays except joy and anger, with statistically significant decreases seen in four out of six measured emotions.

This suggested the possibility that a common underlying feature was affecting the emotional displays while lying, and helped inspire the idea that facial rigidity may be a phenomenon that reliably occurs when hiding nefarious behavior in a structured interview, and one that is detectable using only a video camera. To the extent this was so, the requirements for our proposed system might be realized. These considerations prompted follow-up research to (1) begin to understand the underlying cause of facial rigidity when hiding illicit behavior, (2) ensure facial rigidity was a consistent behavior in this context, and (3) begin to understand how an automated human screening system design can best elicit and measure this risk indicator.

## An Automated Screening Design for Facial Rigidity Detection

Consistency is an important factor anytime a behavior is used to infer some underlying cognition. This is especially true for facial cues, some of which have been criticized for being unreliable indicators when used to predict deception. Unlike some related work on the face, the current study focuses on the context of a highly controlled risk screening interview.

Results from the initial exploration did not reveal which portion(s) of the face were rigid during deception. It was unclear whether a particular part of the face (e.g., the mouth) was being held more still, or the rigidity was more generalized. If the observed decrease in variation is specific to particular areas on the face, it could reflect greater consistency in an underlying affective state. For instance, less variation in the brow region alone could indicate concerted concentration, or less variation in the mouth corners could reflect more consistent affect. If the entire face is rigid, a more general neutralization or tension would be the underlying cause. To explore these possibilities, we chose to use measures that more directly reflect movement in Study 2.

Whether facial rigidity stems from intensive concentration, neutralizing one or more emotional displays, or a generalized increase in tension, a system design should be able to elicit this effect using a controlled interviewing technique similar to the CIT. Changes in concentration and neutralization cannot be expected unless the examinee perceives a potential threat of exposure, or at least perceives a Target Stimulus as personally significant [14, 31]. Therefore, a feasible design could involve a system presenting a battery of stimuli of which most are known a priori to be benign, comparing behavioral responses to benign stimuli to responses to Target Stimuli [40].

Since comparisons among responses to stimuli are at the core of the design, presentation of the stimuli must be delivered in a highly controlled manner to eliminate possible artifacts corrupting the behavioral responses. In this regard, Study 1 offered less control than is ideal. Reflecting real-world investigative procedures, the human interviewer was aware of the correct answers to questions. Separation of this knowledge from the interviewer would prevent the possibility of inadvertently communicating it to an interviewee. Also, even though a human interviewer simply repeats multiple choice questions with no variation in script, he or she introduces variation in speech, mannerisms, timing, emotion, volume, and other nonverbal behaviors that should be eliminated. Further, the repeat-after-me style of questioning introduced additional variation in facial movement in that different words are used for each answer: different mouth movements are required to form different words. To effectively compare facial movement between responses, the required verbal responses to all stimuli must be uniform.

These standardized delivery requirements fall within the framework of automated, scientifically controlled screening systems (ASCSS) [40]. This class of systems emphasizes scientific control, including automated timing, and highly controlled stimuli presentation. The prototype system evaluated in Study 2 implements the ASCSS specifications, using a desktop computer with an embodied conversational agent to conduct human screenings while simultaneously collecting raw video for post hoc facial expression analysis. Beyond these foundational requirements, all questions were required to elicit a “no” response only, to control for facial movement specific to word formation. Lighting was carefully placed to ensure high-quality face images with no shadow. High definition video was captured to ensure that minor variations in movement could be effectively captured. Rather than generating facial emotion data and inferring lack of movement, facial movement was to be measured directly, with movement during baseline question responses compared to movement during Target question responses.

## Study 2

A second realistic mock theft experiment was conducted to test a prototype screening system that implemented these requirements. Participants (N = 107) were recruited from undergraduate business courses at a large university in the southwest United States. Similar to Study 1, participants were randomly assigned to a theft (Guilty) or no-theft (Innocent) condition and undertook a series of tasks before being interviewed about their knowledge of a theft. A high-definition camera was used to record participants as they responded to interview questions.

## Experimental Task

Participants recruited from undergraduate business classes were instructed to arrive at an office on the ground floor of a building. After arriving, they were randomly assigned to Innocent (truthful) or Guilty (deceptive) conditions. Once participants consented to participate, they received instructions from a research assistant. Participants in the Guilty condition were asked to select one of several possible false identifications (IDs) and an envelope. The assistant told the participant to select an ID that was the closest match to their appearance. An envelope containing further instructions was then given to the participant, who was told to read the instructions in the envelope when riding a nearby elevator up to the fourth floor. Participants in the Innocent condition followed steps similar to those of the Guilty participants, except no false identification was presented or selected.

Enveloped instructions given to Guilty participants outlined details on how they should steal an exam key from a secured computer located in the building. They were given a username and password for an ostensibly secure computer, and instructed to copy the exam key onto a thumb drive contained in the envelope. The instructions also noted that if they confessed to any crime during the experiment, they would forfeit their cash incentive.

Enveloped instructions for Innocent participants told them to retrieve information about an upcoming speaker series from an open, public computer located in the building. The computer was not password protected. Rather than copying information onto a thumb drive, Innocent participants were asked to write down basic information about the speaker series.

After completing their assigned task, all participants reported to an office near where they first entered the experiment. Upon arriving at the office, they were greeted by a confederate acting as a security officer, told that a crime had been committed and that they would be interviewed about their involvement. Up until this point, participants were unaware that they would be interviewed. The interview was conducted by the prototype screening system, while a camera captured the participant’s face and shoulders at 30 Hz. Table 4 displays the questions used in the interview, all of which required the same “No” response. A question was asked five times in a row by an on-screen avatar, and each time, a stimulus screen immediately followed the question and remained on screen for five seconds. Four of the five stimulus screens contained baseline items, but one of the screens contained an item that was the Target (i.e., “correct”) answer. All items, baseline and Target, were displayed only once. The presentation order of items was fixed rather than randomized or counterbalanced, because analysis of prior research data that used the same paradigm revealed no ordering effect. The location of the Target item varied between questions. Questions were designed to target only those things that were certain to have required conscious attention from the perpetrator (e.g., the perpetrators were certain to know they used fake identification). The interview took less than five minutes, after which participants were debriefed and took a post-task survey. Open-

Table 4. Questions Used in Study 2 Experiment Interview  
![](/api/attachments/GF59YPKG/fulltext/images/15bd1fff9ca32d9524372feaeac1932b31587a919b1bb8622881d21434d52f08.jpg)  
ended feedback from participants during debrief revealed evidence of a strong perception of realism.

## Facial Movement Measures and Initial Analyses

For each frame of video, Cartesian coordinates for 49 distinct points on the face was generated using IntraFace, a facial feature tracking algorithm [48]. These points were adjusted to remove variation due to head pose and scale. Movement was first calculated in a manner similar to previous rigidity research [39], in that Euclidean distance was calculated, frame to frame, for each of the 49 points. Variances in Euclidean distances were then calculated for each 5-second response period, for each participant. Variances from all 49 points were summed to produce an overall facial movement estimate.

Of the 107 participants who were recruited for the experiment, 3 withdrew because they did not feel comfortable performing the task. Of the 104 who participated, 13 were removed due to confessing to the theft, 7 were removed for not following directions, 5 were removed due to system crashes during the interview, and 11 were removed due to corrupted video files, which would not process through the feature extraction software. The data analysis included 68 participants (Guilty = 32; Innocent = 36).

A multilevel regression model was specified with movement as the dependent variable, and Guilt and Target Stimulus as independent variables. Guilt was dummycoded with 1 for the Guilty condition and 0 for the Innocent condition, and Target Stimulus was dummy coded with 1 for when a Target Stimulus was present on screen, and zero when no Target Stimulus was on screen. Time was included as a covariate. Participant and question set were included as random effects. Results of the multilevel regression model are displayed in Table 5.

While this first set of measures and analysis is useful for testing facial rigidity generally, more specific measures are needed to identify movement in particular areas of the face. For this, we opted to adapt measures from the facial expression measurement system (FACEM). FACEM was developed for the rapid quantification of facial expressions in clinical settings [29]. The system is based on a mathematical model using Euclidean distances between key facial landmarks, which describe upper and lower facial actions. The developers of FACEM found that distance measures could be used to distinguish between facial expressions. Distance measures

Table 5. Multilevel Regression Results for Overall Facial Movement Variance During Question Responses

<table><tr><td>Fixed effects</td><td>Estimate</td><td>(S.E.)</td></tr><tr><td>Time</td><td>0.10</td><td>(0.12)</td></tr><tr><td>Guilt</td><td>-3.43</td><td>(3.51)</td></tr><tr><td>Target Stimulus</td><td>6.64</td><td>(3.48)</td></tr><tr><td>Guilt × Target Stimulus</td><td>-10.27*</td><td>(5.02)</td></tr><tr><td colspan="3">Note: *p&lt;.05; statistically significant results are in bold.</td></tr></table>

Bott  toent

Mouhh uppen

Moihh dth

![](/api/attachments/GF59YPKG/fulltext/images/95b1ff6c46b3cf4df4644c43a80c1ade6ed268c377b9deb967b79a763d7ecefc.jpg)  
Top  o  dth

![](/api/attachments/GF59YPKG/fulltext/images/fe20cf2e974b387cc378a018ff23ab0b77c25503d87fa24c2321ac236544b081.jpg)

![](/api/attachments/GF59YPKG/fulltext/images/352add0fa433804521b67c22cfd9e6c89b9308d831cfb5129c2c0a11bcd30692.jpg)

Ri    nd  
![](/api/attachments/GF59YPKG/fulltext/images/3c57032a2c421a6d037d329798cf1757b07cc51b547c09d4dc156b1a50b6ef13.jpg)

![](/api/attachments/GF59YPKG/fulltext/images/f398e44e27816e724e9f9dd422992aa0b6989abc27af9713f0e6e06d4974ae78.jpg)  
Rie   ow  
Figure 3. Face Measures Using Fiducial Points  
Tovp  ent

![](/api/attachments/GF59YPKG/fulltext/images/5c76883dbf0dc60ff1204d88a94cb8aa637a051a4cd8d972d8486ce692222e5e.jpg)

![](/api/attachments/GF59YPKG/fulltext/images/30246fa6cae3e6180cfca3db1e4748dea2049c11a566c657e404fa820753cb97.jpg)

Notes: $* * * p ^ { < } . 0 0 1 ; * * p ^ { < } . 0 1 ; * p ^ { < } . 0 5 ;$ statistically significant results are in bold.

more clearly define movement behaviors of the face, as opposed to intensity levels of specific emotions or action units.

Figure 3 displays seven FACEM-based measures used in this analysis. Our measures differ slightly from the traditional measures. We found that blinking caused IntraFace to change the location of fiducial points at the corner of the eyes. To avoid confounding facial actions with blink behavior, we used the tip of the nose as a reference point in place of the corner of the eyes. We also averaged the distance of five brow measures for each eye brow as opposed to using just a single distance measure. This produced a more granular measure of brow behavior.

The general definition of these measures is shown in Equation (1). In the cases of multiple points comprising measurements, the average Euclidean distance was calculated. For measures without definitive start and end points, such as brow measures, the tip of the nose was used as a reference point. In total, 10 measures were calculated to monitor rigidity in different areas of the face.

$$
M e a s u r e = \sqrt {\frac {\sum \left(p _ {f n} - q _ {f m}\right) ^ {2}}{N}},\tag{1}
$$

where $p _ { f n } = \mathrm { s t a r t i n g }$ point n at frame f , $q _ { f m } = \mathrm { e n d i n g }$ point m at frame $f ,$ and $N =$ number of distance measures.

## Study 2 Analysis and Results

Variance of each face measure was calculated for each five-second response. Each variance value was then standardized by subject and CIT question. Given that the face measures describe distances within video frames as opposed to between video frames, we opted for variance as the aggregating function to describe movement as opposed to the mean of between-frame distances. Between-frame mean distance values would resemble average facial point positions during a response rather than capturing the movement of those facial points.

Table 6. Multivariate Regression Model Results for Upper and Lower Face Measures

<table><tr><td>Face measure</td><td>Guilt $\beta$  (S.E.)</td><td>Target Stimulus $\beta$  (S.E.)</td><td>Guilt X Target Stimulus $\beta$  (S.E.)</td></tr><tr><td>Right Brow</td><td>0.12(0.06)</td><td>0.15(0.1)</td><td>-0.58(0.14)***</td></tr><tr><td>Left Brow</td><td>0.13(0.06)*</td><td>0.16(0.1)</td><td>-0.64(0.14)***</td></tr><tr><td>Right Lip End</td><td>0.08(0.06)</td><td>0.03(0.1)</td><td>-0.42(0.14)**</td></tr><tr><td>Left Lip End</td><td>0.06(0.06)</td><td>-0.09(0.1)</td><td>-0.30(0.14)*</td></tr><tr><td>Top Lip Width</td><td>0.05(0.06)</td><td>0.04(0.1)</td><td>-0.23(0.14)</td></tr><tr><td>Bottom Lip Width</td><td>0.12(0.06)</td><td>0.23(0.1)*</td><td>-0.60(0.14)***</td></tr><tr><td>Mouth Width</td><td>0.11(0.06)</td><td>0.15(0.1)</td><td>-0.53(0.14)***</td></tr><tr><td>Mouth Open</td><td>0.05(0.06)</td><td>0.01(0.1)</td><td>-0.24(0.14)</td></tr><tr><td>Top Lip Movement</td><td>0.08(0.06)</td><td>0.02(0.1)</td><td>-0.38(0.14)**</td></tr><tr><td>Bottom Lip Movement</td><td>0.11(0.06)</td><td>0.15(0.1)</td><td>-0.57(0.14)***</td></tr></table>

A multivariate regression model was specified with face measure variance as the independent variable and Guilt and Target Stimulus as dependent variables. Guilt was dummy-coded with 1 for Guilty condition and 0 for Innocent condition and Target Stimulus was dummy-coded with 1 for when a Target Stimulus was present on screen, and zero when no Target Stimuli were on screen. The overall model produced a significant Guilt and Target interaction, $F ( 1 , \ 1 0 ) = 3 . 5 3 , \ p { < } . 0 0 1$ . Standardized estimates for specific measures are included in Table 6, with standard deviations in parentheses.

## Discussion

The theoretical contributions of this study include identifying a new phenomenon in the context of behavioral analysis for decision support and providing initial insight into the mechanisms that drive it. The post hoc analysis of Study 1 provided initial evidence of facial rigidity during risk assessment in scientifically controlled interviewing. Results of Study 2 confirmed the existence of this phenomenon, and provided evidence that facial rigidity is a consistent indicator of risk, at least in a controlled deception interview setting. All ten measures of facial movement showed a negative correlation with stimuli representing a committed illicit behavior. Eight of these significantly differentiated Guilty from Innocent interviewees when a Target Stimulus was present. Based on the results, it appears that the observed rigidity is not specific to a particular region or regions of the face.

This provides further evidence that rigidity is not likely a function of masking, because rigidity is not concentrated around specific areas of the face associated with the masked expression or fake expression. For instance, a fake smile would affect movement in the mouth but not necessarily movement in the brows. Instead, facial rigidity appears to result from neutralizing; a task at which people perform relatively better. It is possible that neutralizing in this context is an extension of the freeze response, but further research is needed to discover more about the nature of neutralizing in automated screening. To the extent that the underlying mechanisms are based on perception more than emotion, facial rigidity could be a robust indicator even for desensitized or routine deception.

Identifying facial neutralization as a behavioral mechanism is an important contribution for automated screening systems research. If these system designs are to effectively act as risk segmentation tools, we must understand the drivers of the behavioral indicators used so as to effectively elicit them in an interview and control or account for their inherent limitations. Additional contributions of this study include evidence that elicitation and capture of facial neutralization can be effectively incorporated into an automatic screening design, together with a description of how that can be accomplished. Nearly all similar prior studies in this area have used human coding to manually identify facial behaviors. Identifying facial rigidity on the granular level achieved in this study would not be possible using a manual approach, and a manual solution is not feasible for most potential applications, such as visa application screening or financial audit interviews. In contrast, the proposed design can be deployed in any environment that allows for the use of a video camera, and is even suitable for web-based interview settings.

Prior work has demonstrated that facial cues to deception exist, but the boundaries that affect their consistency are not well understood, making replicability uncertain. The proposed design demonstrates facial rigidity within an established design framework that provides for consistency and replicability. In both studies, using repeated measures to compare differences on an individual and question level controls for potential effects of general nervousness, interpersonal, and question differences. Study 2 controlled for the variability that a human interviewer injects into the process, as well as that of using different words for Target vs. baseline responses. The nature of the questions asked in Study 2 elicited a consistent, single-word response from each interviewee, further controlling variability between responses.

Prior studies that have successfully used computer vision to detect deceptive facial expressions have focused on situations where the deceiver simulated a high-intensity emotion they were not actually experiencing [4, 17, 33]. A strategy of simulating emotional expressions may be appropriate in some contexts, but more often than not, a deceiver’s best strategy is to control their emotional valence so as to appear unemotional, for example, while crossing through a border checkpoint. In this scenario, micro and macro expressions are less likely to be usable traits for deception detection. The approach used in this current study should not be impeded by low emotional valence, making facial rigidity analysis applicable for a wider variety of interview settings.

These studies have important implications for practice. Vast resources have been allocated to law enforcement training programs to assess risk using facial expressions, but have not found widespread success. Human ability to neutralize or disguise emotions may be too great to allow for consistent deception detection. There is clear value in new information systems specially designed to elicit and capture indicators of veracity quickly and noninvasively. The evidence suggests that facial rigidity can be a useful focus for these decision support systems.

## Conclusion

As the need for efficient human screening continues to grow, government and industry will increasing rely on automated systems to assist with decision support. With this reliance comes the need to capture and process data that are most diagnostic of the phenomenon of interest. Facial behaviors that indicate a likelihood of having engaged in illicit activity have been a topic of study for decades, but demonstrable widespread efficacy and usefulness of these cues has not yet been achieved. Whereas existing theory traditionally focuses on leakage of facial expressions in unstructured or semistructured dialogues, this study identified facial rigidity in a scientifically controlled automated interview as a possible alternative. Rigid facial movement in controlled interactions may be key to more ubiquitous use of facial data in veracity assessment in auditing, emergency room management, rapid security screening, and employment interviews.

Acknowledgments: The Department of Homeland Security’s (DHS) National Center for Border Security and Immigration (BORDERS), the National Center for Credibility Assessment (NCCA), and the Center for Identification Technology Research (CITeR), a National Science Foundation (NSF) Industry/University Cooperative Research Center (I/ UCRC), provided funding for this research. Statements provided herein do not necessarily represent the opinions of the funding organizations.

## REFERENCES

1. Ben-Shakhar, G.; Bar-Hillel, M.; and Lieblich, I. Trial by polygraph: Scientific and juridical issues in lie detection. Behavioral Sciences and the Law, 4, 4 (1986), 459–479.

2. Ben-Shakhar, G., and Elaad, E. The validity of psychophysiological detection of information with the Guilty Knowledge Test: A meta-analytic review. Journal of Applied Psychology, 88, 1 (2003), 131–151.

3. Buller, D.B., and Aune, R.K. Nonverbal cues to deception among intimates, friends, and strangers. Journal of Nonverbal Behavior, 11, 4 (1987), 269–290.

4. Cohn, J.F., and Schmidt, K.L. The timing of facial motion in posed and spontaneous smiles. International Journal of Wavelets, Multiresolution and Information Processing, 2, 2 (2004), 121–132.

5. DePaulo, B.M., and Fisher, J.D. Too tuned-out to take: The role of nonverbal sensitivity in help-seeking. Personality and Social Psychology Bulletin, 7, 2 (1981), 201–205.

6. DePaulo, B.M., and Kirkendol, S.E. The Motivational Impairment Effect in the Communication of Deception. Dordrecht, The Netherlands: Kluwer, 1989.

7. DePaulo, B.M.; Lindsay, J.J.; Malone, B.E.; Muhlenbruck, L.; Charlton, K.; and Cooper, H. Cues to deception. Psychological Bulletin, 129, 1 (2003), 74–118.

8. Derrick, D.; Jenkins, J.L.; and Nunamaker Jr., J.F. Design principles for special purpose, embodied, conversational intelligence with environmental sensors (SPECIES). ACM Transactions on Human–Computer Interaction, 3, 2 (2011), 62–81.

9. Derrick, D.C.; Elkins, A.C.; Burgoon, J.K.; Nunamaker, J.F.; and Zeng, D.D. Border security credibility assessments via heterogeneous sensor fusion. IEEE Intelligent Systems, 25, 3 (2010), 41–49.

10. Derrick, D.C.; Meservy, T.O.; Jenkins, J.L.; Burgoon, J.K.; and Nunamaker Jr., J.F. Detecting deceptive chat-based communication using typing behavior and message cues. ACM Transactions on Management Information Systems, 4, 2 (2013), 1–21.

11. Ekman, P. Telling Lies: Clues to Deceit in the Marketplace, Marriage, and Politics. New York, NY: Norton, 1985.

12. Ekman, P., and Friesen, W.V. Nonverbal Leakage and Clues to Deception. Psychiatry, 32, 1 (1969), 88–106.

13. Ekman, P., and Friesen, W.V. Detecting deception from the body or face. Journal of Personality and Social Psychology, 29, 3 (1974), 288–298.

14. Ekman, P., and Friesen, W.V. Unmasking the Face: A Guide to Recognizing Emotions from Facial Cues. Englewood Cliffs, NJ: Prentice Hall, 1975.

15. Ekman, P.; Friesen, W.V.; and Sullivan, M.O. Smiles when lying. Interpersonal Relations and Group, 54 (1988), 414–420.

16. Gray, J.A. The Psychology of Fear and Stress. Cambridge, UK: Cambridge University Press, 1988.

17. Littlewort, G.; Whitehill, J.; Wu, T.; Fasel, I.; Frank, M.; Movellan, J.; and Bartlett, M. The computer expression recognition toolbox (CERT). In Proceedings of the IEEE

International Conference on Automatic Face and Gesture Recognition and Workshops (FG 2011). Santa Barbara, CA: IEEE, 2011, pp. 298–305.

18. Littlewort, G.C.; Bartlett, M.S.; and Lee, K. Automatic coding of facial expressions displayed during posed and genuine pain. Vision Computing, 27, 12 (2009), 1797–1803.

19. Lykken, D.T. Psychology and lie detector industry. American Psychologist, 29, 10 (1974), 725–739.

20. Lykken, D.T. A Tremor in the Blood: Uses and Abuses of the Lie Detector. New York, NY: Plenum Trade, 1998.

21. Meijer, E.H., and Verschuere, B. The polygraph and the detection of deception. Journal of Forensic Psychology Practice, 10, 4 (2010), 325–338.

22. National Research Council. Committee to Review the Scientific Evidence on the Polygraph (ed.) The Polygraph and Lie Detection. Washington, DC: National Academies Press, 2003.

23. Nunamaker Jr., J.F.; Burgoon, J.K.; Twyman, N.W.; Proudfoot, J.G.; Schuetzler, R.; and Giboney, J.S. Establishing a foundation for automated human credibility screening. In Proceedings of the 2012 IEEE International Conference on Intelligence and Security Informatics (ISI). Washington, D.C.: IEEE, 2012, pp. 202–211.

24. Nunamaker Jr., J.F.; Derrick, D.C.; Elkins, A.C.; Burgoon, J.K.; and Patton, M.W. Embodied conversational agent-based kiosk for automated interviewing. Journal of Management Information Systems, 28, 1 (2011), 17–48.

25. Nunamaker Jr., J.F.; Golob, E.; Derrick, D.C.; Elkins, A.C.; and Twyman, N.W. Field Tests of an AVATAR Interviewing System for Trusted Traveler Applicants. Technical report published by the Center for Border Security and Immigration, 2013. www.borders.arizona.edu/cms/sites/ default/files/FieldTestsofanAVATARInterviewingSystemforTrustedTravelerApplicants.pdf.

26. Nunamaker Jr., J.F.; Twyman, N.W.; and Giboney, J.S. Breaking out of the design science box: High-value impact through multidisciplinary design science programs of research. In Proceedings of the Americas Conference on Information Systems (AMCIS 2013). Chicago, IL: AIS, 2013, pp. 575–585.

27. Nunamaker Jr., J.F.; Twyman, N.W.; Giboney, J.S.; and Briggs, R.O. Creating highvalue real-world impact through systematic programs of research. Management Information Systems Quarterly, 41, 2 (2017), 335–351.

28. Pilowsky, I., and Katsikitis, M. Classification of facial emotions: A computer based taxonomic approach. Journal of Affective Disorders, 30 (1994), 61–71.

29. Porter, S., and ten Brinke, L. Reading between the lies: Identifying concealed and falsified emotions in universal facial expressions. Psychological Science, 19, 5 (2008), 508–514.

30. Porter, S., and ten Brinke, L. The truth about lies: What works in detecting high-stakes deception? Legal and Criminological Psychology, 15, 1 (2010), 57–75.

31. Proudfoot, J.G.; Twyman, N.W.; and Burgoon, J.K. Eye tracking and the CIT: Utilizing oculometric cues to identify familiarity with wanted persons. In HICSS-46 Proceedings of the Rapid Screening Technologies, Deception Detection, and Credibility Assessment Symposium. Maui, HI, 2013.

32. Roelofs, K.; Hagenaars, M.A.; and Stins, J. Facing freeze: Social threat induces bodily freeze in humans. Psychological Science, 21, 11 (2010), 1575–1581.

33. Su, L., and Levine, M. Does “lie to me” lie to you? An evaluation of facial clues to high-stakes deception. Computer Vision and Image Understanding, 147 (2016), 52–68.

34. ten Brinke, L., and Porter, S. Cry me a river: Identifying the behavioral consequences of extremely high-stakes interpersonal deception. Law and Human Behavior, 36, 6 (2012), 469–477.

35. Tsiamyrtzis, P.; Dowdall, J.; Shastri, D.; Pavlidis, I.T.; Frank, M.G.; and Ekman, P. Imaging facial physiology for the detection of deceit. International Journal of Computer Vision, 71, 2 (2007), 197–214.

36. Twyman, N.W. Automated human screening for detecting concealed information. Department of Management Information Systems. Tucson, AZ: University of Arizona, 2012.

37. Twyman, N.W.; Burgoon, J.K.; Elkins, A.C.; and Proudfoot, J.G. Alternative cues in concealed information testing. In The Rapid Screening Technologies, Deception Detection and Credibility Assessment Symposium at the Hawaii International Conference on System Sciences (HICSS 2013). Maui, HI: IEEE, 2013.

38. Twyman, N.W.; Elkins, A.C.; Burgoon, J.K.; and Nunamaker Jr., J.F. A Rigidity detection system for automated credibility assessment. Journal of Management Information Systems, 31, 1 (2014), 173–202.

39. Twyman, N.W.; Lowry, P.B.; Burgoon, J.K.; and Nunamaker Jr., J.F. Automated screening for detecting purposely concealed knowledge in individuals. Journal of Management Information Systems, 31, 3 (2014), 106–137.

40. Twyman, N.W.; Moffitt, K.; Burgoon, J.K.; and Marchak, F. Using eye tracking technology as a concealed information test. In HICSS-43 Symposium on Credibility Assessment and Information Quality in Government and Business, 43rd Annual Hawaii International Conference on System Sciences, Koloa, HI, 2010.

41. Twyman, N.W.; Pickard, M.D.; and Burns, M.B. Proposing automated human credibility screening systems to augment forensic interviews and fraud auditing. In Proceedings of the Strategic and Emerging Technologies Workshop at the American Accounting Association Annual Meeting. Washington, D.C., 2012.

42. Twyman, N.W.; Proudfoot, J.G.; Schuetzler, R.M.; Elkins, A.C.; and Derrick, D.C. Robustness of multiple indicators in automated screening systems for deception detection. Journal of Management Information Systems, 32, 4 (2015), 215–245.

43. Valacich, J.; Jenkins, J.L.; and Byrd, M. Suspicion detection in the wild: Lessons learned from an early stage company. In Proceedings of the Hawaii International Conference on Computer and Systems Sciences, Symposium on Rapid Screening Technologies, Deception Detection, and Credibility Assessment. Kauai, HI, 2016.

44. Vrij, A. Behavioral correlates of deception in a simulated police interview. Journal of Psychology, 129, 1 (1995), 15–28.

45. Vrij, A. Detecting Lies and Deceit: Pitfalls and Opportunities. West Sussex, UK: Wiley, 2008.

46. Vrij, A.; Mann, S.; and Fisher, R.P. An empirical evaluation of the behaviour analysis interview. Law and Human Behavior, 30, 3 (2006), 329–345.

47. Xiong, X., and De la Torre, F. Supervised descent method and its application to face alignment. Paper presented at the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Portland, OR, June 23–28, 2013, pp. 532–539.

48. Zuckerman, M.; DePaulo, B.M.; and Rosenthal, R. Verbal and nonverbal communication of deception. Advances in Experimental Social Psychology, 14, 1 (1981), 1–59.

49. Zuckerman, M.; Larrance, D.T.; Spiegel, N.H.; and Klorman, R. Controlling nonverbal displays: Facial expressions and tone of voice. Journal of Experimental Social Psychology, 17, 5 (1981), 506–524.
