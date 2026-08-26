---
otero_id: 13408
otero_key: "FEFP87WT"
title: "Computer-Mediated Deception: Strategies Revealed by Language-Action Cues in Spontaneous Communication"
authors: "Shuyuan Mary Ho; Jeffrey T. Hancock; Cheryl Booth; Xiuwen Liu"
year: "2016"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2016.1205924"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computer-Mediated Deception: Strategies Revealed by Language-Action Cues in Spontaneous Communication

Shuyuan Mary Ho, Jeffrey T. Hancock, Cheryl Booth & Xiuwen Liu

To cite this article: Shuyuan Mary Ho, Jeffrey T. Hancock, Cheryl Booth & Xiuwen Liu (2016) Computer-Mediated Deception: Strategies Revealed by Language-Action Cues in Spontaneous Communication, Journal of Management Information Systems, 33:2, 393-420, DOI: 10.1080/07421222.2016.1205924

To link to this article: http://dx.doi.org/10.1080/07421222.2016.1205924

![](/api/attachments/FEFP87WT/fulltext/images/40f3169e6632184ea3c35439f6c34fe1ebf8322680d2155d585d7c65a019c4dc.jpg)

Published online: 05 Oct 2016.

![](/api/attachments/FEFP87WT/fulltext/images/d50009c3a66d27e8a77c4546f66f0bea44b913ab125eeb5b44ba97af57ef729f.jpg)

Submit your article to this journal

![](/api/attachments/FEFP87WT/fulltext/images/6ad31ece083235075466e671df975e45bb1144ad66216629af46169ab976f859.jpg)

Article views: 54

![](/api/attachments/FEFP87WT/fulltext/images/146aceff19b5addb16db9f62d22225f32a0a5dec488e530a6d2cfc25dc3b2f5e.jpg)

View related articles

![](/api/attachments/FEFP87WT/fulltext/images/4dae30107e20bd3f22fa80a1e8b18378bbd7f6a122d4a06e8b506c4bc257643e.jpg)

View Crossmark data

# Computer-Mediated Deception: Strategies Revealed by Language-Action Cues in Spontaneous Communication

SHUYUAN MARY HO, JEFFREY T. HANCOCK, CHERYL BOOTH, AND XIUWEN LIU

SHUYUAN MARY HO (smho@fsu.edu; corresponding author) is an assistant professor at the College of Communication and Information, Florida State University. Her research focuses on trusted human–computer interactions, specifically addressing issues of cyber insider threats and online deception. Her research has been funded by the U.S. National Science Foundation, Florida Center for Cybersecurity, and the Florida State University Council of Research and Creativity Her work appears in Journal of Management Information Systems, Journal of the American Society for Information Science and Technology, Information Systems Frontiers, Information Processing & Management, as well as IEEE and ACM Conference Proceedings.

JEFFREY T. HANCOCK (hancockj@stanford.edu) is a professor of in the Department of Communication at Stanford University. He works on understanding psychological and interpersonal processes in social media by using computational linguistics and behavioral experiments to examine deception and trust, emotional dynamics, intimacy and relationships, and social support. His research has been published in over eighty journal articles and conference proceedings, and has been supported by funding from the U.S. National Science Foundation and U.S. Department of Defense. His work has also been featured in the popular press, including the New York Times, CNN, NPR, CBS, and the BBC.

CHERYL BOOTH (clb14h@my.fsu.edu) is a doctoral candidate in the School of Information, Florida State University. She earned a JD from the Valparaiso (Indiana) University School of Law. She is a licensed attorney in the state of Massachusetts. Her primary research interest is in the national and international information policies vis-à-vis information privacy and data security, with an emphasis on the potential impact of different policies on information behaviors.

XIUWEN LIU (liux@cs.fsu.edu) is a professor of computer science at Florida State University. His research interests include modeling high dimensional spatial-temporal data in different domains and identifying intrinsic patterns with applications in cyber security, remote sensing, image and video analysis, computational biology, and machine learning. His research has been published in IEEE Transactions on Pattern Recognition and Machine Intelligence, IEEE Transactions on Neural Networks, and IEEE Transactions on Image Processing.

ABSTRACT: Computer-mediated deception threatens the security of online users’ private and personal information. Previous research confirms that humans are bad lie detectors, while demonstrating that certain observable linguistic features can provide crucial cues to detect deception. We designed and conducted an experiment that creates spontaneous deception scenarios in an interactive online game environment. Logistic regression, and certain classification methodologies were applied to analyzing data collected during fall 2014 through spring 2015. Our findings suggest that certain language-action cues (e.g., cognitive load, affective process, latency, and wordiness) reveal patterns of information behavior manifested by deceivers in spontaneous online communication. Moreover, computational approaches to analyzing these language-action cues can provide significant accuracy in detecting computer-mediated deception.

KEY WORDS AND PHRASES: computer-mediated communication, computer-mediated deception, deception detection, deceptive communications, human–computer interaction, interpersonal deception theory, language-action cues.

Computer-mediated communication (CMC) technologies include e-mail, instant-messaging/chat, social media, and blogs, which have become an increasingly prevalent means of communication today. However, while the adoption of these communication technologies continues to enhance the geographical scope, speed, and convenience of interpersonal communication, its quasi-anonymous nature allows online actors to exploit human vulnerability and susceptibility to deception [48]. Moreover, as the de facto facilitator of a variety of computer-mediated deception, these communication technologies present new threats, including social engineering attempts, such as phishing, spear phishing, identity theft, and fraud.

To understand the unique problems of computer-mediated deception, it is first necessary to understand the nature of deceptive communication. This has been broadly defined as “a message knowingly transmitted by a sender to foster a false belief or conclusion by the receiver” [2, p. 205]. Deceptive communication involves or implements persuasive strategies employed by that sender, and the activities in which he/she engages [41], to deliberately distort the message conveyed and thereby influence “the beliefs, attitudes and behaviors” of the receiver [33, p. 99]. This task is made easier by our inherent propensity to expect that the parties with whom we communicate are being truthful, which effectively works “to reduce a person’s search for the [cues] that might reveal [a] lie” [31, p. 380] and makes a receiver less inclined to look for, and thus less apt to pick up on, cues that might reveal deception [31]. The function of this “truth bias” [2, 21] is thus an important factor in the success of a message sender in deceiving a message receiver. To be precise, the sender’s success largely depends on how the receiver evaluates the sender’s truthfulness, and particularly how the receiver assesses identity in his/her decision about whether or not to trust the information exchange. In the physical world, this assessment and evaluation is often informed by a variety of physical, nonverbal cues (body language, gestures, eye contact, facial expression, tone and pitch of voice, pace of speech, etc.), as well as verbal cues (words written or spoken). The crux of the problem with computermediated deception is that the availability and influence of physical cues is reduced when compared with face-to-face (F2F) communication. Indeed, in text-based CMC, no physical cues are present; the only cues available to the receiver are the sender’s written words. It is therefore particularly difficult to detect deceptive intent in CMC, and hence even more difficult to protect against computer-mediated deception.

Ongoing research into deceptive communication has shown that deceptive intent can be revealed through subtle language-action cues—that is, linguistic styles, phrases, patterns, or actions in a sender’s written expression and manifested as an indirect or subtle signal to others [26–29]. Although people in general are bad lie detectors [15], it may be possible to learn from these cues for the development of an automated process that identifies the underlying intent of a potential deceptive act. A first step in developing such a process is to identify indicative language-action cues that reveal deceptive intent. As will be discussed, these language-action cues can vary depending on media type and mode of communication. While there has been research into specific cues that are significant in the context of e-mail, blogs, and social media (such as online dating profiles [23, 42, 43] and hotel reviews [37–39]), research into deception in spontaneous, synchronous CMC is sparse. This study contributes to the body of literature by focusing on identifying cues that are most predictive of deceptive intent in synchronous, spontaneous CMC. Specifically, this research attempts to answer the research question: Which language-action cues are most predictive of deception in synchronous, spontaneous computer-mediated communication?

## Theoretical Foundations

Research from a variety of fields—including psychology, sociology, communication, and linguistics—informs our understanding of deceptive communication and deception detection. This section explores some predominant theoretical frameworks, particularly social distance theory and interpersonal deception theory in the F2F context, and media richness theory and feature-based modeling in the context of CMC.

## Deception in Face-to-Face Communication

Ekman and Friesen [16] studied nonverbal communication behavior (i.e., body language) as an indicator of deception, and particularly focused on the phenomenon of nonverbal leakage, which occurs when nonverbal cues (unconsciously or subconsciously manifested by a communication sender) operate to provide clues to a communication receiver. Ekman and Friesen [16] also suggested that the interactive process through which deception is maintained or discovered is a key consideration in deception detection, as is the importance or saliency of the deception to the respective parties. However, despite identifying these potential ways in which deception may be detected, humans continue to perform poorly in detecting lies [15, 17].

Granhag and Strömwall [20] categorized nonverbal deceptive behaviors into three types of internal processes: (1) emotional processes, which describe the emotional state of the deceiver (e.g., displaying a sense of guilt); (2) cognitive processes, which emphasize the complexity of deception (e.g., reflected in slowed reactions on the part of the deceiver); and (3) attempted control processes, which reflect the struggles of a deceiver who is trying to appear exceedingly honest and genuine. Granhag and Strömwall [20], moreover, examined verbal cues using the statement validity analysis (SVA) credibility assessment technique to identify and examine verbal features that correlate with deception, and suggested that truthful statements are more detailed than false statements, and that the quantity and consistency of detail may be the most determinative factor in detecting deception. Since then, several credibility assessment systems/techniques [14, 18, 20, 45, 46] have been adopted to examine both verbal and nonverbal behaviors and cues to deception. Nunamaker et al. [36], for instance, developed an automated credibility assessment machine, an intelligent agent, to detect nonverbal cues and behavioral changes when a person is being interviewed.

These psychological aspects (e.g., emotional, cognitive, and attempted control processes) of a deceptive act [20] are central to one of the primary theoretical frameworks in deception research: social distance theory. Social distance theory [19] posits that to avoid the social discomfort related to deception (i.e., guilt, etc.), deceivers will tend to separate or distance themselves from the person they are attempting to deceive [12]. This separation or distance can be literal, figurative, or both. One way in which distance can be created literally is in the deceiver’s choice of communication channel or media type. Social distance theory [19] suggests that deceivers are more likely to select a communication channel or media type that allows for less direct interaction and thus offers the communicating partner less insight (i.e., cues) into the deceiver’s intentions. For example, a deceiver might feel more comfortable communicating in a public place where the surroundings could serve to distract the person they are attempting to deceive, rather than in a private confined space involving one-on-one conversation. Perhaps a deceiver would choose to make a telephone call rather than meeting in person. The wide range of media choices for online communication could be a particularly important decision to the deceiver when carrying out a planned deception. From a figurative standpoint, separation or distance can also be achieved through both verbal and nonverbal immediacy strategies.

DePaulo et al. [12] focused on the psychological ramifications of deception as reflected in verbal cues, and strategies deceivers use to falsify, conceal, or minimize these cues. DePaulo et al. [10] further posited that, in accordance with social distance theory, the deceiver will feel relatively safer when deceiving strangers remotely (particularly in terms of the risk and consequences of detection). This, in turn, suggests that casual “everyday lies” occur more frequently in remote relationships [11, 12] while serious lies are mostly told in close relationships [10]. DePaulo et al. [10, 11, 13] suggested that social distance theory accounts for a phenomenon similar to attribution error as described by Ekman and O’Sullivan [17]. That is, a truthful speaker may also have “self-regulatory demands” to avoid being perceived as a deceiver. When a truth-teller is concerned about being taken for a liar, he/she may employ types of distancing behaviors similar to those of a deceiver. However, as DePaulo et al. [10] pointed out, a caveat exists with respect to individuals who simply do not experience the psychological ramifications of lying. In the case of such individuals, the predictive indicators of deception would simply not apply.

Buller and Burgoon [2] proposed a set of principles in interpersonal deception theory (IDT) for identifying verbal and nonverbal cues to deception. These principles initially focus on F2F interpersonal communication, but many of these cues are also applicable to asynchronous online communication (such as e-mail). The theory examines the interpersonal, interactive, and iterative nature of deceptive (and truthful) communications and behaviors, instead of the message or communication itself. Burgoon et al. [4, 5] suggested that an act of deception may be best characterized as an ongoing strategic process, like a chess match. Although both strategic and nonstrategic behaviors may be manifested during deception, IDT views deception as fundamentally a strategic practice through which the deceiver seeks to satisfy multiple (and/or competing) objectives, including impression management, relational communication, emotion management, and conversation management [3].

In developing IDT, Burgoon et al. [5] focused on the evaluation of a receiver’s suspicions and perceptions, as communicated through verbal and nonverbal cues to the deceiver, to better understand the strategies that shape a deceiver’s behavior during a deceptive act. The results of this research indicate that to avoid detection, a deceiver will adjust his/her deceptive strategy—perhaps more than a few times, and often “on the fly”—during the course of a deceptive communication, and this strategy itself tends to be fluid and variable. IDT therefore posits that the deceiver’s behavior tends to affect the receiver’s behavior, which in turn tends to affect the deceiver’s strategy. It further predicts that the deceiver’s message reflects language/ word choices consistent with strategic attempts to manipulate information through nonimmediate language. Burgoon et al. [6] additionally examined the influence of suspicion on the dynamics of communication, and found that suspicion can have an influence similar to that of deception. This concept is also similar to the attribution error phenomenon discussed above; even if a speaker is not being deceptive, suspicion on the part of the receiver may cause the speaker (in an attempt to avoid suspicion) to interact in a way that may perpetuate suspicion.

To recap, IDT considers deceptive communication cues not only from the standpoint of the receiver but also from the standpoint of the deceiver. Although IDT differs and distinguishes itself from social distance theory, IDT is still intrinsically informed by social distance theory and the concept of “leakage.” Subsequent studies applying IDT have generally relied on either nonstrategic leakage cues (e.g., visual and tactile cues such as expressiveness), or uncovering nonimmediacy cues (e.g., response latency) that may also be useful in detecting deception [3–5]. Thus, while unique, IDT also includes the underpinnings of social distance theory.

## Deception in Computer-Mediated Communication

As problematic as it can be to detect deception in F2F communication, these difficulties are compounded by the additional and unique challenges presented in

CMC. In particular, the type, kind, quantity, quality, and modality [54] of the cues and clues available in CMC differ considerably from F2F communication. The cuelean nature of CMC presents specific challenges, and advantages, for online deceivers. This, in turn, has given rise to the development of theoretical frameworks that have been designed to explore computer-mediated deception.

One such framework is media richness theory. While not exclusively belonging to CMC, this theory has become particularly important in CMC. Media richness theorists [9, 30, 44] suggest that the nature of a message (equivocal or unequivocal) drives the choice of medium for transmission of that message. Accordingly, media richness theory posits that cues to deceptive intent can be found in the selection of communication method (CMC vs. F2F), and the richness of the medium (i.e., e-mail vs. instant message vs. telephone call vs. social media post). The richness of the medium can be defined by four factors: feedback (e.g., immediate or delayed); number of available cues (e.g., social cues); language variety (i.e., the type and variety of symbols used to convey a message); and personal focus (i.e., infusing the message with personal feeling/emotions) [9]. The richer the medium type, the better it is for ambiguous communication, which might help to conceal deception. Media richness theory further suggests that, in the context of deceptive online communication, deceivers will tend to use quick feedback and personal focus to emotionally connect with the communicating recipient (i.e., to create immediacy), and obfuscate their deception by sending conflicting cues that the receiver may or may not be able to unscramble. However, even if a medium has some characteristics of richness, it may still be unsuitable as a media choice. For example, although online text/chat provides immediate feedback, it still lacks the amount of cues available.

Different types of media adopted will result in different strategies and cues being employed by the deceivers. This is the core of the feature-based model [25], which views deception detection through the lens of the specific features used. Deceivers may consider various aspects of media for use in deception—for example, does the media afford real-time communication? Is the message exchange recorded/recordable? Is the communication able to be distributed? Are the communicating parties in the same location (e.g., copresent), or are they in different locales? A key element of this model is its fundamental assumption that deception is spontaneous, suggesting that deception is more likely to occur when media is “synchronous and distributed, but non-recordable” [47, p. 209]. In addition to examining what the choice of medium can reveal concerning the potentially deceptive intent, Hancock et al. [22, 24] further examined various linguistic features (e.g., first-person singular, emotionally toned words, use of inhibition, prepositions, and conjunctions), specifically in the context of online dating profiles, to demonstrate that these can be important indicators for distinguishing truth-tellers from deceivers.

Finally, not all types of modern communications are purely asynchronous or synchronous. Often, we use a communication medium that is a combination of these [25, 47, 51, 53]. Instant messaging (IM), for example, is a “hybrid” communication mode: the immediacy features of F2F communication are shared, but nonetheless may be asynchronous (and a bit more like e-mail), depending upon the situation and the users [34]. Such hybrid communication presents challenges in detecting computermediated deception. Based on these foregoing theoretical discussions, we provide our theoretical framework for analyzing computer-mediated deception.

## Hypotheses Development

The ability to detect deception, in any environment, depends on numerous factors such as a communicator’s cognitive and affective processes. Perhaps the most important of these is availability of certain verbal and nonverbal cues that may indicate potentially deceptive intent, which may serve to alert a message recipient to be more critical of the information being communicated. Certain language-action cues, such as latency in response time, wordiness, and expression within a CMC environment [22, 23, 53] can be useful indicators. This section will first discuss some of the more indicative language-action cues, specifically noting the different contexts in which these have been studied. Then, we will raise four specific hypotheses to frame computer-mediated deception in the context of synchronous, spontaneous communication.

## Immediacy

One particularly indicative language-action cue is the concept of immediacy in communication.<sup>1</sup> Mehrabian defined immediacy as “the extent to which communication behaviors enhance closeness and nonverbal interaction” [32, p. 203]. In the context of detecting deception, however, closeness to a communicating partner(s) may increase (either in fact or merely in perception) a deceiver’s chance of being exposed—for example, by inconsistency in details between statements. Moreover, a deceiver may not want to be held responsible, and thus will distance him/herself from a deceptive statement. Thus, not only may a deceiver not want to increase (“enhance”) his/her closeness by fostering immediacy, but he/she may indeed actively seek to distance him- or herself by employing a strategy of nonimmediacy, which Buller and Burgoon defined as the “verbal and nonverbal means used to distance oneself from others, to disaffiliate, and to close off scrutiny or probing communication” [1, p. 204]. Indeed, Buller and Burgoon [1] specifically identified nonimmediacy as one of four strategic or intentional communications that deceivers may employ [1, p. 204],<sup>2</sup> and the communication style of deceivers tends to be more nonimmediate than that of truth-tellers.

Immediacy is an important consideration in both social distance theory and media richness theory [8, 53]. Research on verbal and nonverbal immediacy in communication provides insight into the dynamics of psychological distance between communicating actors. This section will first discuss verbal cues to immediacy, and then nonverbal immediacy cues.

## Verbal Immediacy Cues

Psychological distance can be created, in either a F2F or a CMC environment, through word choice and phraseology—that is, verbal immediacy. Word choice and overall tone suggesting negative feelings (such as disappointment, frustration, or even anger), may be a sign of potential negative intent, while word choice and tone suggesting a positive relationship—perhaps conveying humor or praise—can foster a positive, trusting relationship between communicating actors. Some important verbal immediacy cues include use of words associated with affective processes, self- and otherreferences, as well as the use of peripheral expressions and overall wordiness.

1. Affective Process: The awareness that deception is contrary to approved/ accepted societal behavioral norms may make deceivers feel guilty and discomfort [35]. Such awareness may be reflected in the use of more words conveying negative emotion. Research examining words conveying emotion in deception suggests a consistent pattern of more negative emotion words being used by deceivers when compared with truth-tellers [13], for example, 911-call transcript analysis [7]. In the context of e-mail correspondence, Zhou et al. [49] reported similar results and suggested that deceivers prefer to use more emotional expressions (both negative and positive) as compared to truth-tellers. However, in the context of online dating profiles, Toma and Hancock [42] found that truth-tellers were more likely than deceivers to reflect negative emotions. The difference between these findings lies in the nature and objectives of the communication—that is, to attract a potential mate through asynchronous communication versus summoning assistance in an emergency. We further suggest that the particular propensity of a deceiver to use emotionally (i.e., affect) related words could be influenced by the specific context of the communication. However, deception in synchronous and spontaneous online communication has not been thoroughly investigated, and thus we hypothesize that the use of words associated with affective processes can be a significant predictor of deception, and more specifically:

## Hypothesis 1: Deceivers tend to use more words associated with affective processes than truth-tellers.

2. Self- and Other-References: Self-reference is a proclamation of one’s ownership of a statement [1]. Buller and Burgoon [1] suggested that deceivers tend to avoid self-reference in order to disassociate themselves from their words. This result is in accord with social distance theory [12, 19], which suggests that deceivers tend to distance themselves from their fictional stories in order to avoid taking responsibility for deception. While Zhou et al. [50] confirmed that truth-tellers refer to themselves more in their communications, Hancock et al. [22] and Zhou et al. [51] suggested that deceivers tended to use fewer self-references, and more other-references. Zhou and Zenebe [52] further suggested that, in general (irrespective of context), deceivers not only employ fewer self-references but also have shorter pauses during conversational discourse. Similarly, Toma and Hancock [42, 43] found that in the context of online dating profiles, users who were highly deceptive in online dating profiles included fewer self-references and fewer words overall when compared to less deceptive profiles. Overall, deceptive communication can be characterized by infrequent use of self-reference (e.g., “I,” or “we”).

While self-reference can be understood as a means of taking ownership and responsibility for a statement or actions, this is equally the case regarding reference to “other” (e.g., “you,” “they,” “them”). Other-references are often used for the opposite purpose—to shift ownership and responsibility away from a deceiver (i.e., “I”) and toward the other party (i.e., “you”) and/or parties involved in the subject of the conversation (i.e., “they,” “them”). Zhou et al. [51, p. 7] stated that the second-person pronoun “depict(s) the speakers attitudes and involvement” in the interaction. One would expect that deceptive actors would use more other-references than truth-tellers. Zhou et al. [49] supported this assumption, and further found that in e-mail correspondence, deceivers used “you” more than truth-tellers. However, one can easily imagine scenarios in which the context and/or subject of a communication may be such that a deceiver may not want to use evasive other-references, because a third party might be likely to refute the deceiver’s statement. Hence, the frequency and use of other-references—as well as self-references—can fluctuate depending upon the context. These references may be somewhat indicative, but would not be strong indicators.

## Nonverbal Immediacy and Latency

Unlike verbal immediacy cues, which are present in both CMC and F2F communication, the physical nonverbal immediacy cues, such as eye contact, body language, and facial expressions, are not present in text-based communication. Nonetheless, there are certain nonverbal immediacy cues that can serve similar functions. For example, emoticons that indicate mood (e.g., a “smiley face”) are used to invoke similar responses to their physical equivalent. Certain common textmessage abbreviations (e.g., “LOL” for laughing out loud) can be interpreted as if the sender were in front of them and smiling.

One particularly important nonverbal immediacy cue is latency (i.e., response delay, or time lag), which refers to the length of time between when one party asks a question and when the other party responds [52]. A delay in response in F2F communication can create a sense of psychological distance between the parties. In this sense, it can be seen as a type of strategy for nonimmediacy (nonverbal immediacy). Although text-based latency is not indicative of deception (e.g., an individual may be multitasking, or just slow in responding), it could be interpreted as an inability (or unwillingness) to respond promptly so as to fabricate a response.

Although minimal, research can be found to support the proposition that latency can create a psychological distance in CMC, just as it does in F2F communication [15–17]. Zhou and Zhang suggested that when chatting, the average length of time lag for a deceiver is shorter than that for a truth-teller [53, p. 6]. This finding not only contradicts our understanding of deception in a F2F context, where a party with deceptive intent may take slightly longer to consider and respond, but also was statistically insignificant [53, p. 6]. With few studies benchmarking latency and time-to-response, we consider time lag to be a significant predictor of deception in synchronous, spontaneous online communication. Specifically, because of the inherent spontaneity of this particular type of synchronous online communication, we hypothesize that:

Hypothesis 2: Deceivers tend to have longer response time lags than truthtellers.

## Cognitive Processes

Research has shown that the complex process of fabricating lies and maintaining deception usually involves an increased cognitive load. The quantity, level, and consistency of details may be strongly indicative of deceptive intent. Buller and Burgoon [2] suggested that the increase in cognitive load could impact performance, and therefore increase the chance of detection. By extension, deceivers would tend to be less likely to provide specific detail when fabricating a story. Deceivers tend to be more reluctant to use distinction markers, such as exclusive words and negation terms that delimit the content of their story [35]. Deceivers may also use fewer words of exclusivity or negation because they do not want specifics to increase the likelihood of being caught [40]. Truth-tellers, by contrast, tend to use more complex words to provide specific, factual details, since they have firsthand knowledge of the event. This same burden on cognitive load can be seen as an explanation of a related “indicator;” consistency of detail. The more fabricated details a deceiver offers up, the greater the chances he/she may forget the details of their deception and thus to self-contradict. These cues are measureable via salient language-action cues in a dynamic exchange of text messages, by focusing on words such as adverbs, adjectives, inclusive words, and so on [26–29]. Thus, we hypothesize that use of words associated with cognitive processes is a significant predictor of deception in synchronous, spontaneous online communication, and specifically:

Hypothesis 3: Deceivers tend to use more words associated with cognitive processes than truth-tellers.

## Peripheral Expressions and Wordiness

There are many potential indicators of deceptive intent. These include the use of more or fewer sensory or spatiotemporal words and changes in the diversity and complexity of language [35]. These also include specific language cues, such as emotion words, inhibition words, prepositions, and conjunctions, which have also been shown to be indicators that can differentiate deceivers from truth-tellers [22]. In addition, another salient language-action cue in CMC is conciseness. Zhou and Zhang [53] found that deceivers tend to be more wordy (i.e., use more words) in language usage, and take shorter pauses between messages. Zhou and Zhang [55] also found that deceivers tend to be more wordy, use more peripheral expressions in their messages, use more restricted vocabulary and syntax, use fewer self-references, and are more casual in their linguistic style. Although wordiness could be a significant predictor of deception in the context of spontaneous, synchronous online communication, the inherent spontaneity will have an impact on the number of words a deceiver uses. Thus, we hypothesize that:

## Hypothesis 4: Deceivers tend to use fewer words than truth-tellers.

In sum, it is possible to benchmark verbal indicators (such as word count, overall vocabulary and syntax used, details of information disclosed, descriptiveness, conciseness, self- versus other-references, and use of words associated with cognitive and affective processes) and capture certain nonverbal behaviors (such as latency/ response time lag, and similar textual representations of present emotional state) which can then be statistically computed [51].

## Socio-technical Research Design

To test the foregoing hypotheses, and answer our overarching research question, this research approach focuses on two elements: (1) development of specific metrics for language-action cues as information behavior; and (2) analysis of communication patterns in order to distinguish between communication typologies.

## Study Framework

The study framework (Figure 1) illustrates our conceptual approach to understanding, analyzing, and designing ways to explore the dynamics of computer-mediated deception and detection. This framework depicts a sociotechnical research system that provides a directed, analytical approach, and breaks down the process into different phases. Further, it creates a platform to capture players’ spontaneous online communication, interaction, and perceptions (i.e., truth-telling or deception), allowing interpersonal deception scenarios to be simulated.

The first layer depicts the user space that holds and manages registration of new users, and user profiles (Figure 1). It maintains a list of active users available for game sessions, and uses a profile-based selection for each game. Players are randomly matched based on their availability when a game is launched. Random assignments allow players from diverse demographic backgrounds an equal chance of being selected, which supports the overall generalizability of the data collected. The second layer, the game space, has two main components: the database and the chat application. It is responsible for scenario selection, session management, and collection of survey data. It also logs the players’ chats, and then passes the logged chat data to the text analyzer for further processing. The third layer, the text analysis layer, is responsible for data processing. Its function is to evaluate the consistency of conversation, and the use frequency of specific words, terms, or phrases. This layer processes the raw conversational data, extracts language-action cues, and sends the processed cues to the learning layer. The fourth layer, the learning space, is to support future development of a “live” machine learning system. Relationships among cues and data are statistically established, represented, and visualized. Language patterns that represent the psychological constructs are recognized and normalized using regression analysis and machine classification respectively.

![](/api/attachments/FEFP87WT/fulltext/images/3b7942b36916f2c89a851fb5b61abf1f0e50eb296a3275f124fc53d128392bc6.jpg)  
Figure 1. The Research Design

## Game Design and Development

The framework described above was used in developing an interactive online game, called Real or Spiel, with Google+ Hangout as the platform (Figure 2). Real or Spiel simulates real-time, interactive deception scenarios, wherein players attempt to deceive and to detect deception. Two participants (i.e., players) are randomly paired up, with each pair playing four game sessions. Each player in the pair is randomly assigned an outer role—either a “speaker” or a “detector”—to begin the first session. Each outer role as speaker is also assigned an inner role—either “saint” (truth-teller) or “sinner” (deceiver). Thereafter, the players’ outer roles are automatically switched to ensure that all players have an equal chance to initiate conversation. In addition, the game is designed to ensure that each player has an equal chance to be a “speaker-saint” and “speaker-sinner.”

![](/api/attachments/FEFP87WT/fulltext/images/c04deb94e5724c7ffe522a6c1864cd6c42cd0efe16a930805f8b704735ef13bd.jpg)  
Figure 2. An Illustration of the Real or Spiel Online Game Platform

In order to compare deceptive messages with nondeceptive, our design establishes two mutually exclusive sets of messages, and the ground truth. That is, each game session consists of a number of scenarios, and each scenario consists of chat exchanges concerning a specific question (e.g., “Have you ever gotten a parking ticket?”). At the outset, the player assigned the outer role as “speaker” submits a truthful answer to establish the ground truth. This is prior to being assigned the inner role, before the start of the game session. The player assigned to the outer role of “detector” then asks probing questions in an effort to determine the ground truth for that scenario (i.e., has the speaker ever been given a parking ticket?), and thereby assesses whether the speaker is attempting to deceive or being truthful vis-à-vis the ground truth. The player assigned to the outer role of “speaker” responds to the detector’s questions in accordance with the inner role assigned. At the end of each game session, the detector makes a determination as to the speaker’s inner role based on these question-and-answer exchanges.

## Data Collection

Data were collected during fall 2014 through spring 2015. Data on participants ground truth assertion as well as both truthful and deceptive statements for the corresponding scenario were collected and stored in the MySQL database. A total of 40 players (22 men and 18 women) were recruited, and randomly paired. Each of the 20 pairs played 4 game sessions, so the final data set consists of data from a total of 80 game sessions. As noted previously, players were paired up to discuss questions randomly drawn from a corpus of 92 total questions in the database. Although players were predominantly (though not exclusively) drawn from the student population of Florida State University, participants also included nonstudents with ages ranging from eighteen to sixty-eight. Thus, the results may be generalizable to include a broader population group.

Across 80 game sessions, 40 participants, in their outer role as detectors, made 1,210 deception guesses on whether the inner role of their conversational partner was a “saint” or a “sinner.” Out of a total of 1,210 guesses collected, 634 correctly guessed that their partner was a deceiver (i.e., a sinner), yielding a success rate of 52.4 percent. This result is consistent with Ekman and O’Sullivan’s [17] proposition that humans are poor lie detectors, and generally have an accuracy rate of spotting deception at around 50 percent (nearly random) chances.

## Data Analysis

The data set extracted from the MySQL database were cleaned and validated. A Python utility program (i.e., a spell-checker) was developed to revise various common abbreviations, acronyms, and chat terms (such as “U” for “you,” “2” for “to,” etc.) to ensure correct psychological categorization and language feature extraction. We further validated the quality of the data set to ensure that all chats were matched with the corresponding speakers’ inner role (saint vs. sinner) assignment.

Our final data set consists of 2,196 lines of chat with a total of 7,271 words processed by the Linguistic Inquiry and Word Count (LIWC) tool. The specific LIWC categories are set forth below in Table 1.

After data were cleaned and categorized, we then analyzed our data set using logistic regression analysis, decision tree, and support vector machine (SVM) analysis to further assess the predictive value of certain significant cues.

## Logistic Regression Analysis

From a top-down perspective, we approached our research question and hypotheses by examining which language-action cues were more predictive of a deceiver. This established a natural deceiver/truth-teller dichotomy, and suggested that logistic regression would be the appropriate statistical technique to apply. Accordingly, we coded our outcome variable with 0 representing truth-tellers, and 1 representing deceivers. Our independent/predictor variables are the LIWC categories listed in Table 1, and the data were parsed out from these categories plus time lag. We eliminated the overarching categories of affect and cogmech to avoid the potential problem of multicollinearity.

Table 1. Language-Action Cues Categories Extracted by the LIWC Tool

<table><tr><td>LIWC categories</td><td>Coding schema</td><td>Examples</td></tr><tr><td>Affective process</td><td>affect</td><td>happy, cried, abandon</td></tr><tr><td>Positive emotion</td><td>posemo</td><td>love, nice, sweet</td></tr><tr><td>Negative emotion</td><td>negemo</td><td>hurt, ugly, nasty</td></tr><tr><td>Cognitive process</td><td>cogmech</td><td>cause, know, ought</td></tr><tr><td>Certainty</td><td>certain</td><td>always, never</td></tr><tr><td>Inclusive</td><td>incl</td><td>and, with, include</td></tr><tr><td>Exclusive</td><td>excl</td><td>but, without, exclude</td></tr><tr><td>Discrepancy</td><td>discrep</td><td>should, would, could</td></tr><tr><td>Insight</td><td>insight</td><td>think, know, consider</td></tr><tr><td>Causation</td><td>cause</td><td>because, effect, since</td></tr><tr><td>Tentative</td><td>tentat</td><td>maybe, perhaps, guess</td></tr><tr><td>Inhibition</td><td>inhib</td><td>block, constrain, stop</td></tr><tr><td>Negations</td><td>negate</td><td>no, not, never</td></tr><tr><td>Pronouns</td><td>pronoun</td><td></td></tr><tr><td>1st person singular</td><td>self-reference</td><td>I, me, myself, mine</td></tr><tr><td>1st person plural</td><td>self-reference</td><td>we, us, our, ours</td></tr><tr><td>2nd person</td><td>other reference</td><td>you, your, yours, they, them</td></tr><tr><td>Word count</td><td>WC</td><td>n/a</td></tr></table>

Logistic regression analysis indicated the model itself (depicted in Table 2) is significant with $\chi ^ { 2 } = 3 9 . 6 , p \leq 0 . 0 0 1$ . However, only three individual languageaction cues, word count (WC), insight, and “we,” were statistically significant (Table 3). We attribute this phenomenon to the nature of communication: the context itself. It is the context—the combination of words—that is most indicative of deception, rather than the words alone. Thus, even if individual language-action cues themselves are not significant, a particular combination of language-action cues may well be significant in its ability to predict deception.

The initial model (depicted in Table 4), with a cutoff value of 0.5, has an overall accuracy of 79 percent in correctly separating “0’s” (truth-tellers’ statements) and “1’s” (deceivers’ statements), and the accuracy of classifying “1’s” as deceptive statements is 80 percent.

Table 2. Model Coefficients

<table><tr><td colspan="5">Omnibus tests of model coefficients</td></tr><tr><td></td><td></td><td> $\chi^2$ </td><td>df</td><td>Sig.</td></tr><tr><td rowspan="3">Step 1</td><td>Step</td><td>.001</td><td>1</td><td>.971</td></tr><tr><td>Block</td><td>.001</td><td>1</td><td>.971</td></tr><tr><td>Model</td><td>39.573</td><td>17</td><td>.001</td></tr></table>

Table 3. Variable Coefficients and Significance

<table><tr><td colspan="8">Variables in the equation</td></tr><tr><td></td><td></td><td>B</td><td>S.E.</td><td>Wald</td><td>df</td><td>Sig.</td><td>Exp(B)</td></tr><tr><td rowspan="18"> $Step 1^a$ </td><td>WC</td><td>-.024</td><td>.008</td><td>8.187</td><td>1</td><td>.004</td><td>.976</td></tr><tr><td>TimeLag</td><td>.006</td><td>.022</td><td>.088</td><td>1</td><td>.767</td><td>1.006</td></tr><tr><td>I</td><td>-.113</td><td>.108</td><td>1.086</td><td>1</td><td>.297</td><td>.894</td></tr><tr><td>we</td><td>1.258</td><td>.609</td><td>4.270</td><td>1</td><td>.039</td><td>3.519</td></tr><tr><td>you</td><td>.071</td><td>.171</td><td>.175</td><td>1</td><td>.676</td><td>1.074</td></tr><tr><td>posemo</td><td>.107</td><td>.114</td><td>.883</td><td>1</td><td>.347</td><td>1.113</td></tr><tr><td>negemo</td><td>.456</td><td>.258</td><td>3.141</td><td>1</td><td>.076</td><td>1.578</td></tr><tr><td>insight</td><td>.438</td><td>.214</td><td>4.193</td><td>1</td><td>.041</td><td>1.549</td></tr><tr><td>cause</td><td>.086</td><td>.221</td><td>.151</td><td>1</td><td>.698</td><td>1.090</td></tr><tr><td>discrep</td><td>.059</td><td>.245</td><td>.058</td><td>1</td><td>.810</td><td>1.061</td></tr><tr><td>tentat</td><td>-.114</td><td>.119</td><td>.926</td><td>1</td><td>.336</td><td>.892</td></tr><tr><td>certain</td><td>.225</td><td>.190</td><td>1.399</td><td>1</td><td>.237</td><td>1.253</td></tr><tr><td>inhib</td><td>.548</td><td>.367</td><td>2.222</td><td>1</td><td>.136</td><td>1.729</td></tr><tr><td>incl</td><td>-.266</td><td>.166</td><td>2.569</td><td>1</td><td>.109</td><td>.767</td></tr><tr><td>excl</td><td>-.198</td><td>.121</td><td>2.684</td><td>1</td><td>.101</td><td>.820</td></tr><tr><td>social</td><td>-.215</td><td>.147</td><td>2.133</td><td>1</td><td>.144</td><td>.807</td></tr><tr><td>negate</td><td>-.003</td><td>.072</td><td>.001</td><td>1</td><td>.971</td><td>.997</td></tr><tr><td>Constant</td><td>2.728</td><td>2.012</td><td>1.838</td><td>1</td><td>.175</td><td>15.296</td></tr></table>

<sup>a</sup>Variable(s) entered on step 1: negate.

Table 4. Classification Table (0.5 Cutoff)

<table><tr><td rowspan="3"></td><td rowspan="3">Observed</td><td></td><td></td><td colspan="2">Predicted</td></tr><tr><td></td><td colspan="2">Deceiver</td><td>Percentage correct</td></tr><tr><td></td><td>0</td><td>1</td><td></td></tr><tr><td rowspan="3">Step 1</td><td rowspan="2">Deceiver</td><td>0</td><td>31</td><td>9</td><td>77.5</td></tr><tr><td>1</td><td>8</td><td>32</td><td>80.0</td></tr><tr><td>Overall percentage</td><td></td><td></td><td></td><td>78.8</td></tr></table>

However, in order to increase the accuracy of predicting deception (i.e., classifying 1’s) without negatively impacting the overall strength of the model, we changed the cutoff value to 0.4. This yielded an accuracy rate for classification of “1’s” of 90 percent, and had a higher overall model accuracy of 80 percent (Table 5). Although the accuracy of classifying “saints” (i.e., truth-tellers) was reduced (70 percent), the overall model classifies better for purposes of our specific interest (i.e., classifying deceivers). Thus, we submit that the model using a cut-off at 0.4 is optimal.

Table 5. Classification Table (0.4 Cutoff)

<table><tr><td rowspan="3"></td><td rowspan="3">Observed</td><td></td><td colspan="3">Predicted</td></tr><tr><td></td><td colspan="2">Deceiver</td><td>Percentage correct</td></tr><tr><td></td><td>Saint</td><td>Sinner</td><td></td></tr><tr><td rowspan="3">Step 1</td><td rowspan="2">Deceiver</td><td>0</td><td>28</td><td>12</td><td>70.0</td></tr><tr><td>1</td><td>4</td><td>36</td><td>90.0</td></tr><tr><td>Overall percentage</td><td></td><td></td><td></td><td>80.0</td></tr></table>

## Decision Tree Learning

From a bottom-up analytical perspective, we studied the potential utility or predictive value of the other LIWC categories by applying decision tree analysis (using Matlab R2015a)—a machine learning approach—to derive decision points from the data set itself to computationally learn how these predictors contribute to detecting deception, and how deception is reflected in linguistic choices or decisions. Our decision tree (Figure 3) was developed based on certain learned classifiers that were automatically derived from within our data set. These classifiers explain and provide insight into the structure and surface of latent relationships across language-action cues as variables, identifying strong predictor variables as decision points.

From this, we developed a set of rules around the particular properties of each classifier (i.e., input variable), which were then applied to the data set. The three major decision points (i.e., strong predictor-variables) surfaced from the data were cogmech, timelag, and posemo as depicted in Figure 3. Interestingly, the social language-action cue also surfaced as being a strong predictor/decision-point.<sup>3</sup> This particular cue has not been widely discussed in the literature, but this result suggests that more study of this particular cue is warranted.

Although Zhou et al. [50] suggested that decision tree analysis was perhaps not as accurate in classification as other machine learning techniques (such as neural net processing), we submit that it is perhaps the most intuitive and understandable approach for translating language-action cues into an automated deception-detection system. To illustrate, the variables cogmech, timelag, posemo represent good decision points (strong predictors), and the decisions are made in sequence on whether to classify the corresponding speaker as a deceiver or a truth-teller can be easily determined from the normalized word count corresponding to that classifier (in this case, $\ge ~ \mathrm { o r } ~ \le ~ 1 6 . 5 )$ . These decision points can be translated into pseudo code for the design and development of an automated classification system [28]. We submit that the decision points surfacing from the decision tree analysis are strongly aligned with the language-action cues derived from the logistic regression model. The decision tree is an effective approach to automatically classify deceivers from truth-tellers. Figure 3 illustrates an approach that can be effectively used to automatically classify deceivers from truth-tellers.

![](/api/attachments/FEFP87WT/fulltext/images/fa9ad43af070af76b7e3bcb9021ceab1ac9e5edb762d451d811f82f13ebfed0c.jpg)  
Figure 3. Decision Tree Learning

## Support Vector Machines

To further validate the proposed language-action cues and test their effectiveness in detecting deception, we applied the support vector machine approach to construct classifiers and illustrate the resulting decision boundaries. Our data set was used as training data. The resulting classifiers were defined uniquely as those with the largest margin where the minimum distance from training samples to the decision boundaries is maximized.

With the resulting language-action cues, there are different combinations of features that can be used as input for SVM analysis. We first experimented with pairs of features. For each pair of features, we used both a linear kernel and a radial basis function (RBF) kernel. The results of SVM analysis using a linear decision boundary across different language-action cues are illustrated in Figure 4.

The data points displayed below the decision boundaries represent saints (i.e., circles) correctly separated, while those above decision boundaries represent sinners (i.e., dots) correctly separated. Outliers represent saints (i.e., circles) that fall outside or above the decision boundary and vice versa. Outliers also include sinners (i.e., circles dots) that fall within or below the decision boundary and vice versa. The liner kernel model separates “sinners” and “saints” with an accuracy of 70.00 percent (pairing cogmech and timelag language-action cues) and 68.33 percent (pairing affect and timelag language-action cues), respectively (Figure 4).

The results of a RBF kernel with a nonlinear decision boundary across the same pairs of language-action cues are illustrated in Figure 5. The data points displayed within the decision boundaries represent saints (i.e., circles) correctly separated, while those outside of decision boundaries represent sinners (i.e., dots) correctly separated.

With the RBF kernel (Figure 5) the decision boundary separates all the samples correctly, showing the discriminative, predictive power of the proposed features. As a result, the same pairs of cues yielded 100 percent accuracy. That is, there are no anomalies classified by the RBF kernel, and all data are separated correctly in their own categories. RBF kernel decision boundaries are more complex than linear kernel decision boundaries, so this approach requires further validation using independent test samples.

![](/api/attachments/FEFP87WT/fulltext/images/4e423f5fc5620657db4b80d919c44ce67b50c57a9b10319879cd1c6ea2468fbe.jpg)  
Figure 4. SVM 2D Decision Boundary with Linear Kernel Model

In addition, we experimented with combinations of three cues, and the model achieved similar levels of accuracy. Figure 6 shows the visualizations generated using affective process (as $a f f e c t )$ , cognitive mechanism (as cogmech), and latency (as timelag) as the language-action cues of interest. The results show that the parameters of the classifier for the three-cue model(s) can be fine-tuned to reach an accuracy level as high as that obtained from the corresponding two-cue models. As in the models with two cues, the decision boundary in models using three cues also separates the samples in the corresponding three classes with fairly high accuracy. Using the linear kernel, the accuracy is improved to 75 percent, suggesting that the addition of more variables (i.e., language-action cues) increases the overall accuracy of the model (or, at a minimum, did not negatively impact it). After finetuning the parameters of the classifiers, the three-cue RBF kernel model yielded an accuracy of 100 percent. We submit that this result indicates the predictor variables are strong predictors for modeling deception.

![](/api/attachments/FEFP87WT/fulltext/images/27e2899872b199b9ff4d40dc7bff114d6ddf7ea3819f8ad79f3b06134d2e47a5.jpg)  
Figure 5. SVM 2D Decision Boundary with RBF Kernel Model

![](/api/attachments/FEFP87WT/fulltext/images/af446dc195f9876c2cdd34834aa7b35d3f76a458c6dc266ccd57329537846e02.jpg)

![](/api/attachments/FEFP87WT/fulltext/images/1651b54460efbb4e5f0f21a0414c84cd05df1844b734914e3e03913c6147ce74.jpg)  
(a) SVM linear kernel model

![](/api/attachments/FEFP87WT/fulltext/images/72dd3973b36ff18d297f227ae24a6653077fb2d8959803fa70cf8360666801ad.jpg)  
(b) SVM RBF kernel model  
Figure 6. SVM 3D Decision Boundary

## Hypotheses Testing

Below we discuss our hypotheses in view of our findings from the analyses described in the previous section.

## Affective Process (H1: Supported)

H1 posited that, in the context of synchronous, spontaneous online communication, use of words associated with affective process can be a strong predictor of computermediated deception. Specifically, deceivers will tend to use more words associated with affective processes than truth-tellers. As depicted in Table 1, affect is an overarching category that includes related cues such as words denoting positive or negative emotions. In our study, words expressing positive emotion (posemo, $\beta \ : = \ : 0 . 1 0 7 )$ and words expressing negative emotion (negemo, $\beta = 0 . 4 5 6 )$ were measured separately. The underlying hypothesis is supported, as the beta/slope is a positive value—indicating increased use of posemo and negemo by deceivers (Table 3) when compared to truth-tellers.

In terms of predictive strength, the decision tree analysis (Figure 3) shows that use of words conveying or associated with positive emotion has a strong predictive value for determining deceptive intent. SVM analysis, likewise, illustrates that, with reasonable accuracy, a clear separation between deceiver and truth-teller can be made based on use of words associated with affect (including both positive and negative emotion) (Figures 4, 5, and 6). Accordingly, we submit that our results support H1.

## Nonverbal Immediacy and Latency (H2: Supported)

H2 posited that, in the context of synchronous, spontaneous online communication, latency (response timelag) can be a significant predictor of computer-mediated deception. Specifically, deceivers will tend to have longer response timelags $( \beta = 0 . 0 0 6 )$ than truth-tellers (Table 3). Unlike the other indicators and language-action cues we investigated, latency is not itself an LIWC categorical feature. However, the literature indicates that deceivers employ nonimmediacy (specifically, latency) as a communication strategy [1, p. 204]. Thus, this indicator potentially has some predictive value. The slope/beta value generated for this variable—timelag—is slightly positive, indicating that the longer the timelag, the more likely the speaker is to be a deceiver. Furthermore, the results of the decision tree model demonstrate that timelag is predictive, and an important decision point for predicting deception (Figure 3). The SVM analysis also clearly suggests that timelag is predictive. Accordingly, we submit that our results support H2.

## Cognitive Process (H3: Supported)

H3 posited that, in the context of synchronous, spontaneous online communication, use of words associated with cognitive processes can be an important predictor of computer-mediated deception. Specifically, we hypothesized that deceivers will tend to use more words associated with cognitive processes than truth-tellers. Our results suggest that use of words reflecting cognitive processes (i.e., active thinking) such as words conveying certainty (β = 0.225), discrepancy $( \beta = 0 . 0 5 9 )$ , insight $( \beta = 0 . 4 3 8 ,$ $p = 0 . 0 4 1 )$ , inhibition (β = 0.548), and causation $( \beta = 0 . 0 8 6 )$ , differs noticeably between deceivers and truth-tellers (Table 3). Among the cues in our logistic regression model, use of words associated with insight—that is, words of knowledge and thought—while not widely researched or discussed in the literature, were found to be statistically significant (Table 3) in predicting deception in the context of synchronous, spontaneous online communication. The positive slope for insight (β = 0.438, p = 0.041) shows that deceivers use words associated with insight more often than truth-tellers.

In addition, the predictive value of this category of language-action cue is further illustrated by the results of the decision tree analysis—which surfaced cogmech as the primary decision point (Figure 3). SVM analysis likewise illustrates that, with reasonable accuracy, a clear separation can be made between deceiver and truthteller based on the use of words associated with cognitive processes. We accordingly submit that H3 is also supported.

## Wordiness and Expressiveness (H4: Supported)

H4 posited that deceivers tend to use fewer words than truth-tellers. Word count— wordiness and expressiveness—has been widely studied as a strongly predictive cue to computer-mediated deception, so it was somewhat unsurprising that this was found to be statistically significant (using logistic regression) in our overall model. We also identified a negative slope with word count (β = −0.024, p = 0.004) indicating that deceivers use fewer words than truth-tellers (Table 3). We thus submit that H4 is supported. It is important to note, however, that although word count was identified as a significant predictor variable, it was not derived as a decision point in decision tree analysis (Figure 3).

## Other Significant Language-action Cues in Context

In addition to the above cues, our study identified several more language-action cues that appear to be good predictors of deceptive behavior. Among these are selfversus other-references; use of words of inclusivity versus exclusivity, and use of words of negation. Each of these is discussed briefly below.

## Self- versus Other-References

Overall, the use of both self-reference and other-reference appears to be a good predictor of deceptive intent in the logistic regression models (Tables 2 and 3). Specifically, firstperson singular (“I”) self-references had a modest negative slope coefficient (β = −0.113), suggesting that deceivers will use fewer “I” self-references than truth-tellers. However, an examination of the use of first-person plural (“we”) self-references (β = 1.258, p = 0.039) shows that deceivers will indeed use more inclusive term of selfreference than truth-tellers (Table 3). Moreover, “we” was found to be statistically significant in our model. Both of these findings make sense from a theoretical standpoint. In accordance with social distance theory, and the general concept of immediacy, deceivers will attempt to avoid personal responsibility and thus can be expected to use fewer “I” references. In addition, to deflect personal/individual responsibility onto a wider group, deceivers may reasonably be expected to refer to the collective, inclusive “we” rather than “I.” Based on this, it is evident that these self-reference variables do exert some influence within the model, and thus hold some predictive value.

Other-reference cues (i.e., you) were not shown to have statistical significance (Table 3). With a slight positive slope (β = 0.071), deceivers tend to use references to “you” more often than truth-tellers in the logistic regression model. However, in the decision tree analysis, truth-tellers tend to reference “you” more often than deceivers do, and the word “you” surfaced as a moderately important decision point (Figure 3). We submit that other-reference is not a good predictor of deception.

## Inclusivity versus Exclusivity

We also found that use of words associated with inclusivity and exclusivity contributed as predictor variables in logistic regression models (Tables 2 and 3). Specifically, in the logistic regression models, deceivers appeared to use fewer words associated with inclusivity (β = −0.266) and exclusivity $( \beta = - 0 . 1 9 8 )$ than truth-tellers (Table 3). These findings support the results in Newman et al. [35], and we conclude that inclusivity and exclusivity are relevant, but not statitically significant, predictors.

## Negation

Likewise, we found that words associated with negation contribute, albeit minimally, to deception detection as a predictor variable. The negative β-value derived for this cue, negation $( \beta = - 0 . 0 0 3 )$ , indicates that truth-tellers appear to use more words associated with negation than deceivers (Table 3). This result confirms the findings from Hancock et al. [23] that truth-tellers used words associated with negation more frequently than deceivers. However, this cue was not statistically significant and did not surface in decision tree analysis as a decision point. Thus, we submit negate is not a strong predictor.

## Social

Finally, words associated with social surfaced as a moderately important decision point $( \mathrm { i . e . , ~ \geq ~ o r ~ \leq ~ 1 6 . 5 } )$ in our decision tree analysis. A speaker using fewer than 16.5 words (Figure 3) from this category would be classified as deceiver (i.e., sinner). In our logistic regression model, this cue has a negative slope (β = −0.215), indicating that deceivers tend to reference words associated with social, family, and friends less than truth-tellers do. Although the social cue has not been discussed as a significant indicator to deception by earlier literature, it is nonetheless found in this study to be a fairly good predictor of deceptive intent.

## Conclusions

The results of our study have important implications for computer-mediated deception research, theory, and detection practice.

## Theoretical and Practical Implications

Our study demonstrates that context will influence specific language-action cues used by a deceiver in computer-mediated deception. Our study further identifies words relating to cognitive load and affective process as well as word count and latency as being strategic language-action cues, which are specifically indicative of deception in synchronous, spontaneous computer-mediated communication. Our research supports social distance theory [12] in that deceivers tend to distance themselves by taking longer response time (H2) in spontaneous communication. Our findings also support interpersonal deception theory [2] in that deceivers tend to strategize and construct their lies by using more words associated with cognitive process than truth-tellers (H3), especially in interactive, dynamic, and spontaneous online communication. Deceivers also tend to display their affective processes by expressing emotions and closeness in their spontaneous communication. That is, deceivers tend to use more words associated with affective processes than truthtellers (H1). Overall, our study confirms that deceivers tend to use fewer words than truth-tellers (H4) in a spontaneous, synchronous communication environment. This result is particularly interesting in that it is contrary to findings in other communication environments.

The results of our research also have practical implications for future research. Our data (i.e., 52.4 percent accuracy) confirm that humans are, indeed, poor lie detectors. The chances for humans to spot lies are equivalent to random. However our study identifies key language-action cues that can reveal deceptive intent and strategies used within synchronous, spontaneous computer-mediated communications. These findings imply that a machine learning/computational approach can perform better than humans with as much as 100 percent accuracy in classifying deceivers (Figure 5 and Figure 6b). We may ultimately be able to model and “train” a deception-learning system to learn online actors’ information behavior. Wider application may include developing an “online polygraph” mechanism to protect proprietary business communications, detect deception in online dating and other social media interactions, and validate the source and provenance of tactical military communications.

## Limitations

There are however several limitations to our study that should be noted. These primarily involve the design and implementation of the game itself. In particular, scenarios (and roles) could change without the message receiver-player having to formally guess the message sender’s role in the current scenario (i.e., saint or sinner) before the players move on to the next scenario. This limitation can be easily addressed in future iterations by slightly redesigning the game so that the next scenario does not start until the message receiver has actually responded to the pop-up asking him/her to guess the message sender’s role.

In addition, our research participants experienced technical difficulties in signing into the Google+ Hangout platform using their pseudo credentials. This limitation shortened the time that players actually spent in the game, which reduced our ability to collect data. In future iterations, we plan to rebuild the game on a standalone game platform. We also intend to automate the pairing of players by the system, rather than doing this manually.

## Contributions and Future Research

Our research contributes a framework that can be used to automate the detection process by constructing deception-learning classifiers based on online actors’ interactive information behavior as manifested in language-action cues. Our sociotechnical research design, developed based on the IDT framework, contributes to deception research in that it mimics and explores the dynamic, interactive, and iterative nature of interpersonal deceptive (or truthful) communication and information behavior. Our research design allows us to observe how a deceiver shapes his/ her deceptive communication strategy. This approach provides a platform to collect an unbiased and generalizable data set, and further enables the objective detection of deception strategies that is computable based on language-action cues.

Subsequent studies might employ different variations of interactive social media game environments to collect additional data from new, less general deception scenarios for mapping out both known and unknown deceptive language-action cues. This may also involve evaluation of detectors’ suspicion and perception as a means to understand how a deceiver shapes and strategizes on deception. In addition to text-based language-action cues, future research may further include voice (pitch, pace and tone) and image data in studying deception. Deep learning architecture models and similar learning algorithms, have demonstrated substantial improvements in classification and recognition tasks regarding object identification and natural language processing, and these techniques could also be effectively used in future studies.

Acknowledgments: The authors appreciate advice from Mike Burmester, and acknowledge the game development, data collection, and analysis efforts of Muye Liu, Shashanka S. Timmarajus, Kashyap Vemuri, Hengyi Fu, Laura Clark, Aravind Hariharan, and many research participants from Florida State University.

## Funding

The authors wish to thank the National Science Foundation EAGER grants #1347113 and #1347120, 09/01/13–08/31/15, the Florida Center for Cybersecurity Collaborative Seed Grant 03/01/15–02/28/16, and the Florida State University Council for Research and Creativity Planning Grant #034138, 12/01/13–12/12/14.

## NOTES

1. With the exception of this paragraph, which specifically discusses “immediacy” and its converse, “nonimmediacy,” the balance of the discussion will simply refer to the general/broad concept of immediacy, as encompassing behaviors that create either psychological closeness (i.e., immediacy behaviors) or psychological distance (nonimmediacy behaviors).

2. These strategies include (1) uncertainty and vagueness, (2) nonimmediacy, reticence, and withdrawal, (3) disassociation, and (4) image- and relationship-protecting behavior.

3. Words categorized or classified as relating to the “social” category in LIWC include words such as “family,” “friends,” and “humans.”

## ORCID

## REFERENCES

1. Buller, D.B., and Burgoon, J.K. Deception: Strategic and nonstrategic communication. In Daly, J.A., and Wiemann, J.M. (Eds.), Strategic interpersonal communication. New York, NY: Psychology Press, 1994, 191–223.

2. Buller, D.B., and Burgoon, J. K. Interpersonal deception theory. Communication Theory, 6, 3 (1996), 203–242.

3. Burgoon, J.K., and Buller, D. B. Interpersonal deception: III. Effects of deceit on perceived communication and nonverbal behavior dynamics. Journal of Nonverbal Behavior, 18, 2 (1994), 155–184.

4. Burgoon, J.K.; Buller, D.B.; Dillman, L.; and Walther, J.B. Interpersonal deception: IV. Effects of suspicion on perceived communication and nonverbal behavior dynamics. Human Communication Research, 22, 2 (1995), 163–196.

5. Burgoon, J.K.; Buller, D.B.; Ebesu, A.S.; White, C.H.; and Rockwell, P.A. Testing interpersonal deception theory: Effects of suspicion on communication behaviors and perceptions. Communication Theory, 6, 3 (1996), 243–267.

6. Burgoon, J.K.; Stern, L.A.; and Dillman, L. Interpersonal Adaptation: Dyadic Interaction Patterns. New York: Cambridge University Press, 1995.

7. Burns, M.B., and Moffitt, K.C. Automated deception detection of 911 call transcripts. Security Informatics, 3, 8 (2014), 1–9.

8. Daft, R.L., and Lengel, R.H. Organizational information requirements, media richness and structural design. Journal of Management Science, 32, 5 (1986), 554–571.

9. Daft, R.L.; Lengel, R.H.; and Trevino, L.K. Message equivocality, media selection, and manager performance: Implications for information systems. MIS Quarterly, 11, 3 (1987), 355–366.

10. DePaulo, B.M.; Ansfield, M.E.; Kirkendol, S.E.; and Boden, J.M. Serious lies. Basic and Applied Social Psychology, 26, 2 and 3 (2004), 147–167.

11. DePaulo, B.M., and Kashy, D.A. Everyday lies in close and causal relationships. Journal of Personality and Social Psychology, 74, 1 (1998), 63–79.

12. DePaulo, B.M.; Kashy, D.A.; Kirkendol, S.E.; Wyer, M.M.; and Epstein, J.A. Lying in everyday life. Journal of Personality and Social Psychology, 70, 5 (1996), 979–995.

13. DePaulo, B.M.; Lindsay, J.J.; Malone, B.E.; Muhlenbruck, L.; Charlton, K.; and Cooper, H. Cues to deception. Psychological Bulletin, 129 (2003), 74–112.

14. Derrick, D.C.; Elkins, A.C.; Burgoon, J.K.; and Nunamaker, J.F., Jr. Border security credibility assessments via heterogeneous sensor fusion. IEEE Intelligent Systems, 25, 3 (2010), 41–49.

15. Ekman, P. Telling Lies: Clues to Deceit in the Marketplace, Politics, and Marriage. 4th ed. New York: Norton, 2009.

16. Ekman, P., and Friesen, W B. Nonverbal leakage and clues to deception. Psychiatry, 32 (1969), 88–106.

17. Ekman, P., and O’Sullivan, M. Who can catch a liar? American Psychologist, 46, 9 (1991), 913–920.

18. Elkins, A.C.; Dunbar, N.E.; Adame, B.; and Nunamaker, J.F., Jr. Are users threatened by credibility assessment systems? Journal of Management Information Systems, 29, 4 (2013), 249–262.

19. Goffman, E. The Presentation of Self in Everyday Life. New York: Anchor Books, 1959. 20. Granhag, P.A., and Strömwall, L.A. Repeated interrogations: Verbal and non-verbal cues to deception. Applied Cognitive Psychology, 16 (2002), 243–257.

21. Grice, P. Further notes on logic and conversation. Studies in the Way of Words. Cambridge, MA: Harvard University Press, 1989, pp. 41–57.

22. Hancock, J.; Birnholtz, J.; Bazarova, N.; Guillory, J.; Perlin, J.; and Amos, B. Butler lies: Awareness, deception and design. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI’09), Boston, MA, April 7, 2009, pp. 517–526.

23. Hancock, J.; Toma, C.; and Ellison, N. The truth about lying in online dating profile. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI’07), San Jose, CA, April 28–May 3, 2007, pp. 449–452.

24. Hancock, J.T.; Curry, L E.; Goorha, S.; and Woodworth, M. On lying and being lied to: A linguistic analysis of deception in computer-mediated communication. Discourse Processes, 45, 1 (2008), 1–23.

25. Hancock, J.T.; Thom-Santelli, J.; and Ritchie, T. Deception and design: The impact of communication technologies on lying behavior. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI’04), Vienna, Austria, April 24–29, 2004, pp. 129–134.

26. Ho, S.M.; Fu, H.; Timmarajus, S.S.; Booth, C.; Baeg, J.H.; and Liu, M. Insider threat: Language-action cues in group dynamics. In Proceedings of the 2015 ACM SIGMIS Conference on Computers and People Research (SIGMIS-CPR’15), Newport Beach, CA, June 4–6, 2015, pp. 101–104.

27. Ho, S.M.; Hancock, J.T.; Booth, C.; Burmester, M.; Liu, X.; and Timmarajus, S.S. Demystifying insider threat: Language-action cues in group dynamics. In Proceedings of the Hawaii International Conference on System Sciences (HICSS-49), Kauai, Hawaii, January 5–6, 2016, pp. 2729–2738.

28. Ho, S.M.; Hancock, J.T.; Booth, C.; Liu, X.; Liu, M.; Timmarajus, S. S.; and Burmester, M. Real or Spiel? A decision tree approach for automated detection of deceptive languageaction cues. In Proceedings of the Hawaii International Conference on System Sciences (HICSS-49), Kauai, Hawaii, January 5–8, 2016, pp. 3706–3715.

29. Ho, S. M., Hancock, J. T., Booth, C., Liu, X., Timmarajus, S. S., and Burmester, M. Liar, Liar, IM on Fire: Deceptive language-action cues in spontaneous online communication. In IEEE International Conference on Intelligence and Security Informatics, Baltimore, MD, May 27–29, 2015, pp. 157–159.

30. Kahai, S.S., and Cooper, R.B. Exploring the core concepts of media richness theory: The impact of cue multiplicity and feedback immediacy on decision quality. Journal of Management Information Systems, 20, 1 (2003), 263–299.

31. McCornack, S.A., and Park, H.S. Deception detection accuracy in dating relationships: The other side of trust. In M.L. McLaughlin (ed.), Communication Yearbook. Beverly Hills, CA: Sage Publication, 1986, pp. 377–389.

32. Mehrabian, A. Methods and designs: Some referents and measures of nonverbal behavior. Behavior Research Methods and Instrumentation, 1, 6 (1968), 203–207.

33. Miller, G.R.; Deturck, M.A.; and Kalbfleisch, P.J. Self-monitoring, rehearsal, and deceptive communication. Human Communication Research, 10, 1 (1983), 97–117.

34. Nardi, B.A. Beyond bandwidth: Dimensions of connection in interpersonal communication. Computer Supported Cooperative Work, 14, 2 (2005), 91–130.

35. Newman, M.L.; Pennebaker, J.W.; Berry, D.S.; and Richard, J.M. Lying words: Predicting deception from linguistic styles. Personal Social Psychology Bulletin, 29, 5 (2003), 665–675.

36. Nunamaker, J.F., Jr.; Derrick, D.C.; Elkins, A.C.; Burgoon, J.K.; and Patton, M.W. Embodied conversational agent-based kiosk for automated interviewing. Journal of Management Information Systems, 28, 1 (2011), 17–48.

37. Ott, M.; Cardie, C.; and Hancock, J. Estimating the prevalence of deception in online review communities. In Proceedings of the Twenty-First International Conference on World Wide Web (WWW’12), Lyon, France, April 16–20, 2012, pp. 201–210.

38. Ott, M.; Cardie, C.; and Hancock, J.T. Negative deceptive opinion spam. In Proceedings of the Fifty-First Annual Meeting of the Association for Computational Linguistics: Human Language Technologies (HLT’13), Atlanta, GA, June 9–14, 2013, pp. 497–501.

39. Ott, M.; Choi, Y.; Cardie, C.; and Hancock, J.T. Finding deceptive online spam by any stretch of the imagination. In Proceedings of the Forty-Ninth Annual Meeting of the Association for Computational Linguistics: Human Language Technologies (HLT’11). Portland, OR, June 19–24, 2011, pp. 309–319.

40. Pennebaker, J.W., and King, L.A. Linguistic styles: Language use as an individual difference. Journal of Personality and Social Psychology, 77, 6 (1999), 1296–1312.

41. Stiff, J.B. Theoretical approaches to the study of deceptive communication: Comments on interpersonal deception theory. Communication Theory, 6, 3 (1996), 289–296.

42. Toma, C., and Hancock, J. Reading between the lines: Linguistic cues to deception in online dating profiles. In Proceedings of the ACM Conference on Computer-Supported Cooperative Work (CSCW 2010), Savannah, GA, February 6–10, 2010, pp. 5–8.

43. Toma, C.L., and Hancock, J.T. What lies beneath: The linguistic traces of deception in online dating profiles. Journal of Communication, 62, 1 (2012), 78–97.

44. Trevino, L.K.; Lengel, R.H.; and Daft, R.L. Media symbolism, media richness and media choice in organizations. Communication Research, 14, 5 (1987), 553–574.

45. Twyman, N.W.; Elkins, A.C.; Burgoon, J.K.; and Nunamaker, J.F., Jr. A rigidity detection system for automated credibility assessment. Journal of Management Information Systems, 31, 1 (2014), 173–201.

46. Twyman, N.W.; Lowry, P.B.; Burgoon, J.K.; and Nunamaker, J.F., Jr. Autonomous scientifically controlled screening systems for detecting information purposely concealed by individuals. Journal of Management Information Systems, 31, 3 (2014), 106–137.

47. Whitty, M.T.; Buchanan, T.; Joinson, A.N. and Meredith, A. Not all lies are spontaneous: An examination of deception across different modes of communication. Journal of the American Society for Information Science and Technology, 63, 1 (2012), 208–216.

48. Wright, R.T., and Marett, K. The influence of experiential and dispositional factors in phishing: An empirical investigation of the deceived. Journal of Management Information Systems, 27, 1 (2010), 273–303.

49. Zhou, L.; Burgoon, J.K.; Nunamaker, J.F., Jr.; and Twitchell, D.P. Automating linguistics-based cues for detecting deception in text-based asynchronous computer-mediated communications. Group Decision and Negotiation, 13, 1 (2004), 81–106.

50. Zhou, L.; Burgoon, J.K.; Twitchell, D.P.; Qin, T.; and Nunamaker, J.F., Jr. A comparison of classification methods for predicting deception in computer-mediated communication. Journal of Management Information Systems, 20, 4 (2004), 139–166.

51. Zhou, L.; Twitchell, D.P.; Qin, T.; Burgoon, J.K.; and Nunamaker, J.F., Jr. An exploratory study into deception detection in text-based computer-mediated communication. In Proceedings of the Hawaii International Conference on System Sciences (HICSS–36), Hawaii, January 6–9, 2003, pp. 1–10.

52. Zhou, L., and Zenebe, A. Representation and reasoning under uncertainty in deception detection: A neuro-fuzzy approach. IEEE Transactions on Fuzzy Systems, 16, 2 (2008), 442–454.

53. Zhou, L., and Zhang, D. Can online behavior unveil a deceiver? In Proceedings of the Hawaii International Conference on System Sciences (HICSS-37), Hilton Waikoloa Village Big Island, Hawaii, January 5–8, 2004, pp. 1–9.

54. Zhou, L., and Zhang, D. Typing or messaging? Modality effect on deception detection in computer-mediated communication. Decision Support Systems, 44, 1 (2007), 188–201.

55. Zhou, L., and Zhang, D. Following linguistic footprints: Automatic deception detection in online communication. Communications of the ACM, 51, 9 (2008), 119–122.
