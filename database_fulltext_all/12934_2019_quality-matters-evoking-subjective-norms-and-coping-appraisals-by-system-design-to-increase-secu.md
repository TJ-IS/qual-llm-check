---
otero_id: 12934
otero_key: "KWRQB5RS"
title: "Quality matters: Evoking subjective norms and coping appraisals by system design to increase security intentions"
authors: "Mark Grimes; Jim Marquardson"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.02.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Quality matters: Evoking subjective norms and coping appraisals by system design to increase security intentions

![](/api/attachments/KWRQB5RS/fulltext/images/daa34c409533f3b598b6b851d4370a51d70f2cb0739b6c12d19d4a83afbabd71.jpg)

Mark Grimes<sup>a,⁎</sup>, Jim Marquardson<sup>b</sup>

<sup>a</sup> University of Houston, United States of America

<sup>b</sup> Northern Michigan University, United States of America

## A R T I C L E I N F O

Keywords: Information systems security Intentions Quality Trust Visual appeal

## A B S T R A C T

The eficacy of direct messages such as threats, warnings, reminders, and training for influencing information security intentions is well established. Despite the pervasiveness of these approaches, users' poor adherence to security best practices remains a significant problem. Thus, it is critical that new approaches for improving security intentions are explored. System quality is known to play an important role in many aspects of information systems interactions, however, its efect on security intentions has not been established. In this paper, we develop and test a theoretical model that extends protection motivation theory and the theory of planned behavior to describe how system quality evokes positive social norms, lowers threat appraisal, and increases coping appraisal to influence intentions of secure behavior. The hypotheses were tested using a laboratory experiment. The results suggest that system quality positively influences social norms and coping appraisals to enhance security intentions. Threat appraisals, however, were unafected. These findings illustrate how system quality can influence users' security intentions and perceptions of the eficacy of their actions without using direct messaging to warn, train, or reassure them. This technique gives researchers and developers new tools that can influence users to engage in desired behaviors.

## 1. Introduction

Influencing users to engage in secure information systems behaviors is a challenge that has significant personal and business ramifications [1]. Users of information systems are frequently required to perform information security tasks for which they have insuficient ability, motivation, or resources to comply [2–4]. Further, since the act of en gaging in secure behavior itself is seldom, if ever, the primary purpose for interacting with an information system, security is typically not users' primary intention for interacting with a system [5]. This lack of motivation and intentionality toward secure behavior results in carelessness, neglect, or rejection of security best practices [6]. When users fail to engage in secure information systems behaviors, consequences such as identity theft, malware infection, and data loss may be realized for both the user and the system owner.

In order to protect both users and their infrastructure, organizations go to great lengths to create secure environments through technical (e.g., security hardware and software), operational (e.g., training and reminders), and managerial (e.g., policy and risk assessments) controls [6–9]. Despite these eforts, the failure of users to adhere to security best practices can thwart otherwise secure systems thereby negatively impacting their security [2,10–13]. Improving users' security intentions is one method in which this failure might be addressed, as intentions frequently lead to behaviors [14,15] and can be considered a decision to engage in secure behavior [10]. Thus eforts to shape users' security intentions are valuable for shaping users' behaviors.

The failure of users to behave in a secure manner has driven a great deal of research investigating how to influence users' security intentions and behaviors [16]. The majority of research to date has investigated direct methods of influence, such as fear appeals [3,17], warnings [18,19], reminders [20,21], and training [4,22,23]. Despite the efectiveness of these approaches, users still frequently fail in both their behaviors and intentions to adhere to security policies and best practices. Additionally, these methods require users to consciously process and take some action based on the message. To this end, there has been a call for research to investigate new theoretical foundations and methodological approaches for improving security behaviors [16,24].

We posit that one such alternative method for influencing secure computing behaviors is the use of peripheral cues of system quality. As opposed to direct messages, peripheral cues influence people not through deliberate, conscious processing but through a broad assessment of relevant cues [25]. Peripheral cues are known to invoke guiding rules [26] and to shape attitudes and behaviors [27–29]. In the physical world, peripheral cues of social disorder such as broken windows, litter, and grafiti have been found to decrease perceptions of neighborhood quality and safety, thus inducing fear and leading individuals to engage in more protective behaviors [30]. As described by Wilson and Kelling, “…one unrepaired broken window is a signal that no one cares…the sense of mutual regard and the obligations of civility are lowered by actions that seem to signal that no one cares” (1982, pp. 2–3).

Users of information systems are known to similarly evaluate periph eral cues in their computing environments, which in turn afect their be liefs, attitudes, and behaviors [31–34]. Thus, it is reasonable to expect that the same judgment processes people use to make decisions about their behaviors in physical environments will persist in digital environments. However, it is currently an open question as to if and how these system design cues influence users' security intentions—that is, their decision to engage in behaviors that align with security policies or best practices.

In order to make good design choices, system designers must understand how the investment in system quality influences users' security intentions. One plausible viewpoint is that there is a negative relationship between perceived system quality and security intentions. If this perspective is correct, systems that exhibit cues of low quality will cause users to perceive higher threat due to the poor quality of the system, and users will compensate for the heightened threat by engaging in more secure behavior, and vice versa, thus suggesting that investment in highquality design is counterproductive, as users will have heightened intentions to protect themselves when systems are perceived as being of low quality. A second plausible view is that there is a positive relationship between perceived system quality and security intentions. From this perspective, cues of low system quality will lead users to believe the designer of the system does not regard the system highly enough to put forth efort into a high-quality interaction with the user, thus evoking a subjective norm of indiferent or haphazard behavior, while cues of high quality will evoke a subjective norm of thoughtful, deliberate, and ultimately more secure behavior. Models that include subjective norms predict that users will reciprocate the presumed indiference from the system designer that results in low quality systems with indiferent behavior of their own, including failure to adhere to security best practices, and vice versa. That is, there will be a positive relationship between quality and security intentions, and investment in making systems appear to be of high quality are valuable for improving security intentions.

Building on prior research on influencing intentions and behaviors. we believe that peripheral cues of system quality influence behaviors through a combination of signaling, the halo efect, threat appraisals, coping appraisals, and subjective norms. In this manuscript, we present a research model that combines and extends components of protection motivation theory (PMT; [35]) and the theory of planned behavior (TBP; [36]) to describe the influence of peripheral cues of system quality in an information security context. Our model was tested using an experiment in which 169 participants created user accounts on a website containing cues that signal either high or low system quality. This work makes theoretical contributions to the existing literature by providing a novel exploration of the combined efects of PMT and TPB on information security intentions and extends these oft-studied con structs by describing the influence of perceived system quality as an antecedent to threat appraisals, coping appraisals, and subjective norms. In this, we show that visual elements of web site design are not only aesthetically beneficial, but also influence users to interact with the system in a more security conscious way. We close with a discussion of the theoretical and practical implications of these findings and di rections for future research.

## 2. Theory development and hypotheses

## 2.1. Signals and perceptions of quality

Quality can generally be defined as the degree of excellence of an object or process of interest. Quality may be quantified in many ways including measures such as mean time between failure, failure rate per unit time, purity of constituent materials, conformance to standards, and frequency of returns or repairs [37]. While there are many objective ways to measure quality, there is often an information asymmetry between producers and consumers such that these quantifiable measures are not readily available to consumers. This is particularly true for information systems, such as websites, where there are many levels of technical architecture that make it impossible for even the most sophisticated users to make a complete objective assessment of a system's quality [38]. Thus, quality is often described in terms of users' perceptions of quality, which may be defined as a “consumer's judgment about a product's overall excellence or superiority” ([39], p. 3). Perceptions of quality difer from objective measures of quality in that objective quality describes “actual technical superiority” ([39,40], p. 4) while perceptions of quality reflect only a surface understanding of the product or service.

This information asymmetry forces consumers to make assessments of quality based on the cues that are available to them. Consumers commonly interpret cues (i.e., signals) to make assessments of quality when information is scarce [41]. In physical environments such as stores, ofices, and restaurants, signals of quality may be provided via means such as fine furnishings and décor [42,43], neatness [44], cleanliness [45], aesthetically pleasing arrangements [46], or display of awards, certificates, and diplomas [47,48]. While these elements are not directly related to the actual quality of the product of interest, they do influence perceptions of quality through a heuristic known as the halo efect—a cognitive bias in which the appraisal of one attribute is carried over to a diferent attribute [49,50]. While such assessments lack rigor, they are critical to enable users to make rapid assessments, many of which are made in well under one second [51].

Just as visual cues influence perceptions of quality in physical environments, information systems exhibit visual cues, such as appealing colors and graphics or meaningful symbols of trust, which influence users' beliefs about the underlying quality of the system [52–54]. Visual appeal refers to a user's general perception of a system's aesthetic and is facilitated by using “…colors, graphics, and text that are pleasing to the consumer's eye…” ([55], p. 36). Visual appeal may “…be managed to evoke desired quality perceptions” ([39], p. 18) and has been identified as one of the most important components of perceived quality [43]. Visual appeal is accomplished by paying attention to design elements such as color [56,57], layout [58–60], legibility of text [61–63], and image quality [64]. Failure to adhere to design guidelines that create visual appeal signals that the website has not been thoughtfully constructed and maintained, thus creating an overall perception of low quality [65].

A second way in which system owners can signal the quality of a system is by displaying symbols of trust. Symbols of trust are emblems, logos, and other tokens that users can rapidly assess through visual inspection of a system [66]. While these symbols may have some aesthetic appeal in their own right, their primary function is to provide additional details about the system. These symbols may serve as indicators of referent authority by leveraging the reputation of a trusted entity such as a university or respected company, or they may have specific meaning, such as indicating that the website is using highly secure software, has been vetted by a security audit firm, or that communications with the website are encrypted by a trusted third party certificate signing authority (e.g., Verisign or Thawte). When a website is perceived as secure, users believe that the website will facilitate secure communication and protect the privacy of their information—that is, that they can trust the website [55]. This trust implicitly means users believe the website operator will ensure the technical reliability of the website, thus leading to higher perceptions of overall quality [38]. Like visual appeal, trust has been identified as one of the most important components of quality in online systems [38,67].

## 2.2. Threat appraisals

One outcome of people's observation of visual cues is that these cues provide information about the relative safety or danger of the environment. The process of interpreting these cues is known as threat appraisal. The threat appraisal consists of two dimensions: perceived vulnerability to the threat and the perceived severity of the threat [17]. While a heightened threat appraisal is often equated with the presence of fear, it should be noted that fear is not required for individuals to engage in protective behaviors. As described by Rogers [35], Protection Motivation Theory “…makes it clear that one is coping with and avoiding a noxious event, rather than escaping from an unpleasant emotional state of fear. One advantage of this distinction is that it di rects our attention back to environmental stimulation...For example, when crossing a street, there is no emotional state of fear aroused, yet one engages in protective activity” (p. 101). Similarly, we suggest that while it is unlikely that individuals experience the emotional state of fear when interacting with an information system in typical use cases, they do perceive threats—for example, the threat that unauthorized individuals might access their data—and respond accordingly through means such as creating secure passwords or choosing not to use the system at all. Consistent with Rogers, we suggest that even in the absence of fear, people enlist the aid of peripheral cues—such as the visual appeal of the system, the presence of symbols of security, and the overall perception of quality—to make a cognitive appraisal of the level of threat that is present and decide what protective behaviors to employ. The intentional exclusion of fear in our model is intended to “emphasize the importance of cognitive processes to the relative exclusion of visceral ones” ([35], p. 100).

The protection motivation process is a common occurrence in the “ofline” world where visual cues of the presence of potential threats send signals that suggest one's vulnerability to and the severity of a threat [68,69]. For example, if one were to walk into a convenience store in an unfamiliar part of town late at night, peripheral cues such as broken glass or bars on the windows signal that the store has likely been the victim of criminal activity in the past. Thus, a customer observing these cues would likely have a heightened feeling of threat vulnerability. Similarly peripheral cues such as grafiti might signal the severity of the threat—if the grafiti is relatively benign in nature (e.g. the text “Joe was here”) the perceived severity of the threat associated with that cue might be considered lower than if the grafiti were related to violence or gang activity (e.g. images of weapons or gang symbols). Such cues prompt individuals to engage in protective behaviors such as more carefully guarding one's wallet or purse, or perhaps choosing to leave the location altogether.

Peripheral cues of quality similarly influence threat appraisals in the online world. Since users typically have little insight into the objective quality of the system, the halo efect plays an important role in making this assessment. Users assume that a system's quality is consistent across its constituent parts—that is, a system that has a high-quality appearance will also be of high quality in the non-customer facing components such as security features [43]. This heuristic is commonly used by patrons of restaurants where they “…do not see the inner operations of a service establishment…[but]…The overall cleanliness of the dining room, the appearance of the employees, and the condition of the servers' station can suggest similar conditions in the kitchen.” ([45], p. 72). Similarly, if the outward appearance of a web site is of low quality, users will assume the back-end functionality of the site, including security features, is similarly of low quality, and that their account is more vulnerable [55,60,65,70].

As online threats such as viruses, malware, phishing, and data breaches become more prevalent, users are increasingly faced with evaluating the risks associated with providing sensitive data such as email addresses, passwords, and personal information to a web site [71,72]. As previously described, cues of quality help users estimate these risks. Low quality sites send the message that the web site operators care little about the site and have likely done little to reduce how vulnerable users' data is to compromise, and how severe the consequences of a compromise would be, as a website operator who neglects interface design best practices is also likely to neglect security features. Rational website users who doubt the security of a web site are more likely believe that the web site—and therefore their personal data—is vulnerable to attack [73]. Likewise, users are more likely be lieve that a successful attack on a low-quality site will lead to consequences that are of higher severity because just as the operators did not invest the time and efort into creating a high-quality site, they would not have put the time and efort into implementing controls to limit the severity of a successful attack. In contrast, high quality sites send the message that the operators care about the system and would be proactive both in preventing attacks and taking actions to limit the severity of attacks—e.g., applying principles of least privilege, network segmentation, encryption, log monitoring, and informing users and the proper authorities in the case of a breech. In summary, we expect that high-quality systems will reduce perceptions of both the vulnerability to and severity of threats, and vice versa. Thus we propose the fol lowing hypothesis:

H1. System quality will negatively influence a) perceived severity of a threat and b) perceived vulnerability to a threat.

## 2.3. Coping appraisals

Coping appraisals are comprised of an individual's perceived ability to execute a proposed threat mitigation (self-eficacy) and their belief in the efectiveness of the mitigation (response eficacy) [35,74]. Self-efficacy beliefs are informed by “…factors that increase or reduce the perceived dificulty of performing the behavior in question” ([36], p. 196), while response eficacy beliefs are based on perceptions that the proposed mitigation strategy is efective and useful [75]. When interacting with information systems, the levels of abstraction introduced by the computer complicate coping appraisals. Since users are not privy to the inner workings of the system, it can be dificult to determine whether the system is configured in such a way that the mitigation is efective (response eficacy), or if they even have the ability to execute the proposed mitigation (self-eficacy). This results in the coping appraisal being a multifaceted assessment in which perceptions of the quality of the system drive the user's self-eficacy and response eficacy.

Self-eficacy is influenced by system quality in two complimentary ways. First, well-designed (i.e., high-quality) user interfaces decrease the dificulty of performing actions in a system and vice versa [76], thus increasing or decreasing the user's feeling of eficacy. Even for users with a high level of computer skill, a low-quality interface can reduce their perceived ability to use a system, thereby reducing their self-ef ficacy. Second, poor website design has been shown to evoke negative emotional arousal [77]—a state that is known to reduce feelings of self eficacy [78,79]. Thus, poorly designed websites which elicit negative emotional arousal, such as disgust or frustration, during the initial use of the system will decrease self-eficacy for users interacting with the system. Even if the actions that are made more or less dificult are not directly related to security functions, the halo efect of the system being dificult to use may make users perceive these tasks as being more dificult, thereby reducing their self-eficacy for executing the secure behavior.

The coping appraisal also includes perceptions of the security response eficacy. When a system's security is robust, protective actions taken by a user will efectively give protection. Since users have little insight into the actual security configuration of the system, however, users are forced to estimate the robustness of the system's security from what is observable [80]. Research has shown that improving system quality through observable elements such as visual appeal increases perceptions of the quality of other unrelated features such as speed, content, and security, even when there has been no change in these elements [43]. Users of high quality sites will perceive the security to be better, consequently they will feel that their secure actions will be effective. Thus we propose the following relationships between system quality and the constituent components of coping appraisals:

H2. System quality will positively influence a) security response eficacy and b) security self-eficacy.

## 2.4. Subjective norms

In addition to serving as an antecedent to threat and coping appraisals, we suggest system quality also influences subjective norms—“the perceived social pressure to perform or not perform…[a]… behavior” ([36], p. 188). Subjective norms are formed by aggregating the beliefs of groups or individuals that matter to an individual. For example, members of a work team often share norms of work behaviors and adopt norms from those in their circle of influence [81, 82], training exercises, discussions with friends, and media. In an information security context these norms may come from managers, IT personnel, or peers [6]. Importantly, subjective norms are influenced by the context in which they are invoked [36]. This explains why the same conduct is acceptable in one context but not in another [83]. For example, while one may have a desire to celebrate when their favorite sports team scores a point, the environment the person is in influences norms that determine how this celebratory behavior is carried out. While it may be perfectly acceptable to cheer out loud at an arena or sports bar, in other environments such as a library or quiet restaurant, norms limit the celebratory behavior to more restrained displays such as a silent smile or fist pump. Cues in the environment indicate norms and what behaviors are appropriate.

Similarly, in an information systems context, users have an overarching desire to “protect themselves and their assets” ([84], p. 13), however, the environment in which they find themselves influences how they operationalize this behavior. The previously described cues of system quality provide a context for the interaction. If the cues suggest that the system is of high quality—and thus has high quality security, as the halo efect would lead them to believe—users will intend to engage in secure behavior in order to meet the implicitly agreed upon shared expectations (i.e., norms for the interaction). Likewise, if the system is perceived to be of low quality—and thus is perceived to have lowquality security—users will exhibit low-quality security of their own. In line with this proposition, prior work has shown that normative beliefs influence intentions to comply with security policies [6].

Ultimately, the same cognitive processes that evoke positive social norms in the physical environment should hold true in digital en vironments. High-quality systems will evoke norms corresponding to behavior that is aligned with good outcomes. Conversely, low-quality systems will suggest norms that result in diminished quality of out comes. While system quality will not serve to form beliefs about acceptable behavior, system quality will evoke sets of norms associated with desirable behavior and influence how beliefs are acted upon. Thus, we propose that system quality will evoke subjective norms of how one is expected to interact with a system and therefore:

H3. System quality will have a positive relationship with subjective norms of security.

## 2.5. Attitudes, intentions, and behaviors

TPB explains an individual's intention to perform a given behavior by evaluating attitudes toward the behavior, subjective norms, and self eficacy (i.e., perceived behavioral control). These constructs are in fluenced respectively by behavioral, normative, and control beliefs, each of which are dependent on the particular context (i.e., environment) in which the individual finds themselves [36]. Just as one's physical environment serves to define this context, we propose that the quality of the system the user is interacting with—i.e., their digital environment—will similarly shape these beliefs. While prior work has used TPB to explain security intentions [10,85,86], to our knowledge the role of quality in the formation of these beliefs has not previously been studied.

As described by TPB, attitudes are a summation of relevant evalua tions of behavioral beliefs and the strengths of those beliefs, and are formed independently for specific behaviors. A person's “attitude toward…a specific act is proposed to be a function of the act's perceived consequences and of their values to the person.” ([87], p. 42) In the context of information security, the relevant behavioral beliefs are those related to the threat and coping appraisals [55]. The attitude construct in TPB is conceptually similar to the protection motivation construct in PMT in that both constructs are formed by evaluation of relevant threat appraisals [3]. A high threat appraisal will improve attitudes toward security behaviors that help to avoid negative consequences. In contrast, a person who perceives no threat is unlikely to have a particularly strong attitude toward secure behavior because in the absence of a threat, there is likely to be no diference in the outcome regardless of their security behavior. Thus, each dimension of threat appraisal—perceived severity and perceived vulnerability—will have a direct impact on attitudes. Therefore:

H4. Attitude toward security behaviors will be positively influenced by a) perceived severity and b) perceived vulnerability.

Attitude toward security behavior is also influenced by the user's coping appraisal—that is, their self-eficacy and the system's response eficacy. High security self-eficacy will cause people to perceive that threat mitigation is within their power to execute, thus improving their attitude toward acting upon it. If one has low security self-eficacy, however, they will be less likely to have a positive attitude toward engaging in the secure behavior, as they will find it dificult [88]. Security response eficacy—which must be estimated by users, since they have no insight into the actual security of the system—is the level of protection they feel the system can aford them. If users feel that the system has not been properly secured, their attitude toward security behaviors will be low, as their eforts will be for naught. Only when users feel that the system is configured securely so that their protective actions will meaningfully protect them from harm will attitudes toward security behaviors be high. Thus, we propose:

H5. Attitude toward security behaviors will be positively influenced by a) security response eficacy and b) security self-eficacy.

Finally, as proposed by TPB, attitudes, self-eficacy, and subjective norms will directly influence intentions. Thus, we propose the following hypotheses:

H6. Attitude toward security behaviors will positively influence security intentions.

H7. Security self-eficacy will positively influence behavioral security intentions.

H8. Subjective norms of security will positively influence behavioral security intentions.

## 3. Methodology

A laboratory experiment was conducted at a large public university in the Southwestern United States. The experiment was reviewed and approved by the university's human subjects protection program. One hundred and eighty-nine students from a junior level management information systems class participated in exchange for a modest amount of class credit. Participation was voluntary, and other opportunities to receive credit were given to the class. Twenty participants were removed from the sample for providing invalid survey responses such as failing to mark “strongly disagree” when prompted in attention check questions or for providing invariant responses to reverse coded items (i.e., marking the same answer for every question), leaving 169 parti cipants (90 male) for the analysis.

Table 1  
Manipulations of site quality.

<table><tr><td>Feature</td><td>Prior findings</td><td>High quality manipulation</td><td>Low quality manipulation</td></tr><tr><td>Symbols of trust</td><td>Security symbols increase trustworthiness [66]</td><td>RSA and Verisign logos present, the word “secure” in the name of the system</td><td>No symbols of security</td></tr><tr><td>Logos</td><td>Globe logo associated with protection, stability and reliability [93]</td><td>Globe shaped logo with collage of pleasant images, university logo provides referent authority</td><td>Under construction logo suggests an incomplete website</td></tr><tr><td>Quality of images</td><td>Contrast and image dominance lead to higher ratings of credibility [89].</td><td>Visually appealing, dominant, high quality images</td><td>Antiquated, low-quality images with improper aspect ratios</td></tr><tr><td>Symmetry of page</td><td>High complexity and low symmetry of elements leads to lower aesthetic appeal [58]</td><td>Simple, symmetrical layout</td><td>Busy, asymmetrical layout</td></tr><tr><td>Links</td><td>Fraudulent sites tend to have fewer working links [94, 95]</td><td>Working links for help, contact and about us</td><td>Broken links for help, contact and about us, broken image link</td></tr><tr><td>Grammar and spelling</td><td>Fraudulent sites contain incorrect spelling/grammar [94]</td><td>Proper use of grammar and no spelling mistakes</td><td>Incorrect grammar and misspelled words</td></tr><tr><td>Color</td><td>Color appeal results in greater trust and satisfaction [96]. Blue/brown associated with protection, stability and reliability [93]. Reassuring colors increase trustworthiness [97]. Blue and Orange considered more “usual” and received higher appreciation than grey sites [98].</td><td>Use of bold, contrasting colors including red to match university branding and invoke referent authority and blue to suggest protection, stability, and reliability</td><td>Use of unappealing, low contrast colors such as yellow, grey and white</td></tr></table>

Upon arriving at the lab, participants were informed they would need to create a user account for the study so they could log in again in 5–7 days to complete a second part of the experiment. Participants were encouraged to create a unique password for this account and were reminded they would need to use the password again, so they should use a password they would remember. This reminder was intended to encourage participants to use a password that was in line with their usual password creation parameters. Participants were randomly assigned to use either a high-quality site or a low-quality site (Appendix C) when creating their accounts. Quality was manipulated as described in Table 1. The elements that were manipulated are not intended to be an exhaustive list of components of website quality, but rather to provide a wide range of manipulations that were conspicuous, easily interpretable, and in line with manipulations used by prior research [43,89,90].

Immediately following the account creation, participants completed a survey about their perception of the website and their security attitudes and intentions. The survey consisted of previously validated items for constructs of PMT, TPB, visual appeal, and trust. Multi-item scales were used to improve reliability and validity (Appendix A). With the exception of perceived severity, all constructs were measured using 7- point Likert scales anchored at “strongly disagree” and “strongly agree.” Perceived severity was measured using a 7-point Likert-like scale with options ranging from “not severe at all” to “very severe.” Perceived vulnerability, perceived severity, response eficacy, and response cost—were taken from Zhang and McDowell [91]. Attitude, subjective norms, perceived self-eficacy, and intentions—were adapted from Anderson and Agarwal [92]. Quality was operationalized as a superordinate construct consisting of two reflective constructs, visual appeal and trust, which were measured using items adapted from the WebQual instrument [55].

Quality is a multidimensional construct composed of several latent constructs. Due to the wide range of elements of quality [37], and the subjective nature of what elements particular users might employ to assess quality [39], we chose to specifically measure components of quality that can be rapidly assessed by users, as would be the case in a typical account creation scenario—the quality of the visual appeal of the system, and the symbols of trust presented by the system. We treat quality as a superordinate construct in which the latent reflective constructs of visual appeal and trust make up the higher order con struct. These constructs are important elements in the perceived quality of a web site [55]. Measuring these specific dimensions of quality allowed us to isolate the efect of the manipulation, rather than defining quality in a more comprehensive way—which would include elements that were either not manipulated (e.g., response time) or would not be evident to the participants during their brief interaction with the system (e.g., relative advantage). Because of the timing of the manipulation in the experiment flow, asking participants to rate quality broadly would have required participants to determine their own definition of quality, or make judgments with insuficient data. The procedures following the survey (the two part experiment they were required to create an account to complete) are unrelated to the current study and are thus discussed in no further detail here.

## 4. Analysis and results

To ensure the manipulation of quality had the intended efect, re sponses to the visual appeal and trust items were compared across the two conditions. Participants in the low-quality group reported lower levels of perceived quality of the visual appeal of the system $( \mathrm { M } _ { \nu i s u a l } = 3 . 2 6 , ~ \mathrm { S D } = 1 . 3 4 )$ and lower levels of trust $( \mathbf { M } _ { t r u s t } = 4 . 6 0 ,$ $\mathrm { { S D } } = 1 . 2 7 )$ in the system than those in the high-quality group $( \mathrm { M } _ { \small { \nu i s u a l } } = 4 . 9 2 , ~ \mathrm { S D } = 1 . 0 3 ; ~ \mathrm { M } _ { \small { t r u s t } } = 5 . 3 4 , ~ \mathrm { S D } = 0 . 9 6 )$ . The diference was statistically significant at the 0.001 level for each test. Thus, the manipulation was successful. Based on these outcomes of the reflective constructs of quality, we move forward with a binary manipulation of quality (high or low) as the independent variable in the subsequent analysis. With this in mind, we proceeded to assess the measurement and structural models using SmartPLS 3.2.6, a software package for partial least squares structural equation modeling [99].

## 4.1. Measurement model

One self-eficacy and one perceived vulnerability item were removed due to poor loadings. After removing the items, the analysis showed that all constructs had large and standardized loadings $( p \ < \ . 0 0 1 )$ . The composite reliabilities range from 0.81 to 0.93, which are above the recommended threshold of 0.70, suggesting suficient reliability. Convergent validity is supported as the AVEs for all con structs are above the 0.50 level [100]. Convergent validity was assessed by analyzing the factor loadings which range from 0.72 to 0.93. For all constructs the factors load more highly on their intended construct than the other constructs (see Appendix B). The t-statistics of the outer model loadings range from a low of 3.66 to a high of 68.40. Each item's factor loading was significant $( p \ < \ . 0 0 1 )$ . The data support the conclusion that the latent constructs are distinct. Table 2 reports the composite reliabilities, average variance extracted, and correlations between the latent constructs. The square roots of the AVEs are reported on the diagonal. Discriminant validity of the latent constructs is demonstrated as the square root of the AVEs are greater than the constructs' correlations [100]. We used the full collinearity assessment approach to test for common method bias [101]. None of the variance inflation factors exceeded the threshold of 3.3, indicating the model can be considered free of common method bias.

Table 2  
Composite reliabilities, AVE, and correlations. Square root of the AVE is on the diagonal.

<table><tr><td></td><td>CR</td><td>AVE</td><td>Att</td><td>Int</td><td>Norm</td><td>RespEff</td><td>SelfEff</td><td>Sev</td><td>Vuln</td><td>Quality</td></tr><tr><td>Att</td><td>0.88</td><td>0.70</td><td>0.84</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Int</td><td>0.89</td><td>0.73</td><td>0.52</td><td>0.85</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Norm</td><td>0.89</td><td>0.73</td><td>0.40</td><td>0.36</td><td>0.86</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RespEff</td><td>0.87</td><td>0.70</td><td>0.62</td><td>0.29</td><td>0.24</td><td>0.83</td><td></td><td></td><td></td><td></td></tr><tr><td>SelfEff</td><td>0.88</td><td>0.64</td><td>0.42</td><td>0.42</td><td>0.21</td><td>0.37</td><td>0.80</td><td></td><td></td><td></td></tr><tr><td>Sev</td><td>0.93</td><td>0.82</td><td>0.32</td><td>0.25</td><td>0.11</td><td>0.37</td><td>0.20</td><td>0.91</td><td></td><td></td></tr><tr><td>Vuln</td><td>0.81</td><td>0.72</td><td>0.06</td><td>-0.13</td><td>-0.01</td><td>0.12</td><td>0.11</td><td>-0.22</td><td>0.88</td><td></td></tr><tr><td>Quality</td><td>NA</td><td>NA</td><td>0.21</td><td>0.32</td><td>0.30</td><td>0.13</td><td>0.11</td><td>-0.04</td><td>0.21</td><td>NA</td></tr></table>

Note: CR and AVE are not applicable for quality as it is a binary manipulation.

## 4.2. Structural model

Testing of the research model found the relationships between quality and perceived severity and perceived vulnerability to not be significant, thus giving no support to H1. Quality was, however, found to positively influence security response eficacy $( b = 0 . 1 3 , p = . 0 2 9 )$ and security self-eficacy $( b = 0 . 2 1 , p < 0 . 0 0 1 )$ , thus giving support to H2a and H2b. Similarly, we find a significant positive relationship between quality and subjective norms of security $( b = 0 . 3 0 , p < 0 . 0 0 1 )$ , thus giving support to H3. In testing H4 and H5—that threat appraisal and coping appraisal serve as behavioral beliefs that influence attitudes toward security behaviors—we find no significant relationship between perceived severity and attitude nor between perceived vulnerability and attitude. Thus H4 was not supported. We do, however, find a significant relationship between security response eficacy and attitude $( b = 0 . 4 9 6 , p < 0 . 0 0 1 )$ and security self-eficacy and attitude $( b = 0 . 2 3 , \ p = . 0 0 3 )$ , thereby giving support to H5. Altogether, the behavioral beliefs related to coping appraisals were found to explain a large amount of the variance in atti tude toward security behaviors $( \mathrm { R } ^ { 2 } = 0 . 4 3 ) .$

The testing also found that all three TPB constructs were significant predictors of security intentions. Attitude $( b = 0 . 3 6 , p < 0 . 0 0 1 )$ , security self-eficacy $( b = 0 . 2 3 , p = 0 . 0 0 1 )$ and subjective norms $( b = 0 . 1 6 , \ p = 0 . 0 0 7 )$ were each positively correlated with security intentions, thus providing support for H6–H8. In all, the model explained a large proportion of the variance in behavioral intentions $( \mathrm { R } ^ { 2 } = 0 . 3 4 )$ . For completeness, a model was tested in which the constructs of perceived severity, perceived vulnerability and response efficacy predicted security intentions directly, as would be hypothesized by PMT. These paths were found to be non-significant and are thus not included in the final model. Results of the structural model testing are shown in Fig. 1 with the path coeficients and the p-values.

## 5. Discussion

Influencing users' intentions of secure behavior is important because it is widely accepted that security is often seen by users as an impediment to the intended use of a system [4]. Thus, techniques that improve the decisions users make with regard to their intentions of behaving securely can provide great value to information security. To this end, the driving force behind this research was to better understand how the quality of a system influences security intentions. To our knowledge, this is the first investigation of this relationship. The data support the overarching proposition that system quality positively influences security intentions. The data also support many of our hypotheses regarding the causal mechanisms underlying the complex relationship between system quality and security intentions. Here we discuss some of the theoretical and practical implications of these findings.

Evaluation of the path coeficients shows that website quality positively influences both self-eficacy and response eficacy. This suggests that when people interact with high quality systems their perceptions of their ability to cope with threats is improved. It should be emphasized that people in the high-quality condition did not receive any direct messaging that would influence perceptions of their own abilities or the eficacy of their actions. Rather, cues of system quality evoked these changes without needing to warn, train, or reassure system users. System quality also had a positive efect on subjective norms. The data support the notion that system quality influences security intentions through users' perceptions of their environment and the expectations of what behavior is acceptable within that environment. Again, no direct messaging or training was necessary—merely increasing the quality of the system was enough to evoke a set of norms that encouraged secure computing practices. This finding supports the idea that people take behavioral cues from their digital environments in much the same way as they take cues from the physical world. The data did not, however, support the relationship between system quality and threat appraisals. This suggests that low quality systems do not influence perceived vulnerability or severity. As would be expected based on the extant research, attitudes, self-eficacy, and subjective norms all had a positive influence on intentions. For a concise summary of the results, refer to Table 3.

## 5.1. Theoretical contributions

This work makes three important contributions to theory. First, while PMT and TPB both individually provide a great deal of value in understanding security intentions and behaviors, as illustrated in this study, by observing their components together it is possible to more fully understand users' intentions. By combining PMT and TPB, we are able to gather a more complete picture of the mediating efect of attitudes, the influence of subjective norms, and the view of threat and coping appraisals as a system of behavioral beliefs.

Second, it has been suggested that of the three TPB constructs, subjective norms are the weakest [36,102]. However, it has also been proposed that this weakness may stem from failure to properly invoke normative influence [103,104]. Our work examines one antecedent to subjective norms—system quality—and finds that system quality positively influences subjective norms. In turn, subjective norms significantly influence behavioral intentions. These results suggest that subjective norms are indeed an important construct in the TPB framework and that manipulation of norms can result in significant changes to behavioral intentions and can shape decisions users make about how they interact with their environment. This understanding can help researchers use manipulations of subjective norms more efectively in the future.

Third, this is the first research to our knowledge that has proposed and tested a causal pathway from system quality to security intentions. This is important as exhibiting security intentions demonstrates that a choice regarding security behaviors has been made [10]. Thus this finding shows that system quality can play a role in security-behavior decision making. Additionally, while it is commonly accepted that design components can influence a number of perceptions, our study shows that these design choices can also influence intentions, thus making good system design an even more important consideration. Finally, our model helps to illustrate a number of relationships that may be useful for research not only in security, but in a wide range of areas in which influencing user behavior would be useful. For example, our findings demonstrate that self-eficacy, which has been studied extensively and is commonly used in predictive models, can be manipulated by the visual appearance of a system. We also find that system quality is an antecedent for influencing behavioral beliefs and subjective norms.

![](/api/attachments/KWRQB5RS/fulltext/images/132bb7b048304d93f3f52b4f2482c8bd988bff96fa954af516614390eeb3de13.jpg)  
Fig. 1. Model testing results, $^ { \ast } p < . 0 5 , ^ { \ast \ast } p < . 0 1 , ^ { \ast \ast \ast } p < . 0 0 1 .$

Table 3  
Overview of results, $^ { * } p < . 0 5 , ^ { * * } p < . 0 1 , ^ { * * * } p < . 0 0 1 .$

<table><tr><td>Hypothesis</td><td>Supported?</td></tr><tr><td>H1a. Quality → Perceived Severity</td><td>No</td></tr><tr><td>H1b. Quality → Perceived Vulnerability</td><td>No</td></tr><tr><td>H2a. Quality → Response Efficacy</td><td>Yes*</td></tr><tr><td>H2b. Quality → Self-Efficacy</td><td>Yes***</td></tr><tr><td>H3. Quality → Subjective Norms</td><td>Yes***</td></tr><tr><td>H4a. Perceived Severity → Attitude</td><td>No</td></tr><tr><td>H4b. Perceived Vulnerability → Attitude</td><td>No</td></tr><tr><td>H5a. Response Efficacy → Attitude</td><td>Yes***</td></tr><tr><td>H5b. Self-Efficacy → Attitude</td><td>Yes**</td></tr><tr><td>H6. Attitude → Security Intentions</td><td>Yes***</td></tr><tr><td>H7. Self-Efficacy → Security Intentions</td><td>Yes**</td></tr><tr><td>H8. Subjective Norms → Security Intentions</td><td>Yes**</td></tr></table>

## 5.2. Practical and managerial implications

This work has implications for practitioners aiming to influence security behaviors. While traditional methods of explicitly shaping users' intentions, such as training, warnings, and reminders, are known to be efective, the current work demonstrates that quality—an environmental cue that can be manipulated without actively involving the user—can also enhance (or diminish) security intentions. We do not suggest that system quality could replace these incumbent methods of improving security intentions, but rather that it might supplement them. To this end, managers should provide developers the resources they need to create visually appealing systems that exude a sense of high quality. For example, if a programmer does not have the design skills to create aesthetically appealing systems, managers should consider involving graphic designers to enhance the visual appeal of the system. Quality assurance testing should be performed to find functionality defects such as broken links, and other errors such as spelling and grammatical mistakes. Eforts should be made to make symbols of security that establish the trustworthiness of the system apparent. Building a high quality, visually appealing system will result not only in a more aesthetically pleasing product, but also in improved security intentions.

While the current study investigates the relationship between system quality and subjective norms, there are many other ways in which norms can be communicated to employees, including by making minor changes to processes that are already in place. For example, fear appeals are commonly used in warning and informational messages. Building on the current research, these messages should not only communicate the dangers or consequences of the actions, but also emphasize that secure behavior is the expected norm and give users information to improve their coping ability. Similarly, those conducting training and composing reminders about security would be well served to emphasize that behaving securely is the norm for the organization.

Finally, while this research involves using subjective norms to influence security behaviors, similar techniques might be used to influence a wide range of behaviors and decision-making activities. For example, e-commerce sites might attempt to influence subjective norms to manipulate purchasing behavior, political candidates might do so to inspire supporters to take a more active role in their campaign, or systems that rely on user generated content might use norms to influence users to more actively participate in their community. The prospect that visual components of a website not only serve an aesthetic function, but may also serve to change the way users interact with the system has significant potential impact.

## 5.3. Limitations and future research

Some limitations in the current study warrant consideration and provide opportunities for future research. First, fear and the use of fear appeals that are directly relevant to the intention of interest are key components often used in information security research [17]. While fear is not strictly required to elicit protective behaviors [35], the eli citation of fear may change the influence of norms and coping apprai sals. Future research should work to more closely integrate quality with specific fear appeals to determine if the efects of fear appeals are magnified or nullified with quality manipulations. Second, despite efforts to make the elicitation of security intentions as natural as possible—i.e., by having it as a necessary component of a larger study, rather than the focus of the main study itself, thus obscuring the phenomena of interest and endeavoring to elicit typical security behaviors—the fact remains that participants were aware they were taking part in a laboratory experiment. Future research should seek to extend our find ings into a more natural environment.

Another limitation of the current work is that in order to isolate specific aspects of quality that we believed would impact security de cisions, we operationalized participants' perception of quality specifi cally as the quality of the visual appeal and the presence of symbols of trust. This simplifies the assessment of quality substantially beyond the full gamut of items that might influence perceptions of quality. While this operationalization was appropriate given the specific focus of the study, which examined the brief window of time during which users are making security assessments related to creating a user account on a website, a more comprehensive measurement of quality could perhaps unveil additional insights about more extensive system interactions. Future work should extend this work beyond visual appeal and symbols of trust and observe longer system interactions in order to more fully capture the construct of quality.

Finally, while the current work focuses on security intentions—which frequently lead to behaviors—future work should consider taking this a step further and investigating the influence of perceived system quality on actual security-related behaviors. This could take the form of long itudinal field studies which use A/B testing on real systems and observe outcome variables such as password strength, use of encryption, computer backups, or other protective behaviors. Future studies might also consider extending the study of system quality outside the realm of security by investigating topics such as how perceived system quality influences other desirable interactions such as quality of user generated content, focus, willingness to collaborate, information retention, and decision-making tasks. Not only would this help to extend these findings to actual behaviors, but would also make it possible to explore other components of quality that require more extensive interactions with the system (i.e., information quality, intuitive operation, informational fit-totask, etc.). Finally, manipulating elements of quality is just one method for changing the environment. Other environmental factors such as background noise, number of applications demanding attention, and physical workspace arrangement also contribute to the overall com puting environment and may influence behavioral intentions.

## 6. Conclusion

Information systems security researchers have extensively explored the eficacy of explicit messages to influence information security in tentions. In this study we have described a novel method for influencing security intentions via peripheral cues rather than explicit messages by manipulating system quality. We have explored the causal pathway by which this influence takes place and demonstrated that signals of system quality influence security intentions primarily through subjective norms and coping appraisals rather than threat appraisals. The current data suggest that system quality causes users to consider more heavily their capabilities and environmentally evoked norms rather than threats. Improving system quality should be seen as a way to augment, not replace, existing training and direct messaging that focuses on information security in order to achieve better security outcomes. Succinctly stated: in addition to existing security training and messaging, systems that promote a sense of eficacy and a culture that secure behavior is the norm are valuable for improving security intentions.

## Acknowledgements

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## Appendix A. Survey items

<table><tr><td></td><td>Item</td><td>Text</td></tr><tr><td rowspan="3">Attitude</td><td>Attitude-1</td><td>Password security measures such as creating long passwords, changing passwords frequently, or not sharing passwords are a good idea</td></tr><tr><td>Attitude-2</td><td>Creating secure passwords to protect your online accounts is important</td></tr><tr><td>Attitude-3</td><td>I like the idea of taking password security measures to secure my online accounts</td></tr><tr><td rowspan="5">Self-Efficacy</td><td>Self_Eff-1</td><td>I feel comfortable taking measures to use passwords securely</td></tr><tr><td>Self_Eff-2</td><td>I feel comfortable securing my passwords to limit the threat to other people and the Internet in general.</td></tr><tr><td>Self_Eff-3</td><td>Taking the necessary password security measures is entirely under my control</td></tr><tr><td>Self_Eff-4</td><td>I have the resources and the knowledge to take the necessary password security measures</td></tr><tr><td>Self_Eff-5**</td><td>Taking the necessary password security measures is easy</td></tr><tr><td rowspan="3">Intention</td><td>Intent-1</td><td>I am likely to take password security measures on my online accounts to protect myself</td></tr><tr><td>Intent-2</td><td>It is possible that I will take password security measures on my online accounts to protect myself</td></tr><tr><td>Intent-3</td><td>I am certain that I will take password security measures on my online accounts to protect myself</td></tr><tr><td rowspan="3">Vulnerability</td><td>Vuln-1</td><td>What are your chances of someone guessing your passwords?</td></tr><tr><td>Vuln-2</td><td>What are your chances of someone cracking your passwords?</td></tr><tr><td>Vuln-3**</td><td>What are your chances of someone obtaining your passwords?</td></tr><tr><td rowspan="3">Severity</td><td>Severity-1</td><td>How severe do you think the consequence will be if someone guessed your passwords?</td></tr><tr><td>Severity-2</td><td>How severe do you think the consequence will be if someone cracked your passwords?</td></tr><tr><td>Severity-3</td><td>How severe do you think the consequence will be if someone obtained your passwords?</td></tr><tr><td rowspan="3">Response Efficacy</td><td>Resp_Eff-1</td><td>I can protect my online accounts better if I use strong passwords</td></tr><tr><td>Resp_Eff-2</td><td>I can protect my online accounts better if I update my passwords often</td></tr><tr><td>Resp_Eff-3</td><td>I can protect my online accounts better if I use unique passwords for each online account</td></tr><tr><td rowspan="3">Subjective Norms</td><td>Subj_Norm-1</td><td>Friends who influence my behavior would think that I should take measures to choose a secure password on this website</td></tr><tr><td>Subj_Norm-2</td><td>Significant others who are important to me would think that I should take measures to use a strong password on this website</td></tr><tr><td>Subj_Norm-3</td><td>My peers would think that I should choose a strong password to secure my account on this website</td></tr><tr><td rowspan="3">Visual Appeal</td><td>Visual-1</td><td>The website is visually pleasing.</td></tr><tr><td>Visual-2</td><td>The website displays visually pleasing design.</td></tr><tr><td>Visual-3</td><td>The website is visually appealing.</td></tr><tr><td rowspan="3">Trust</td><td>Trust-1</td><td>I feel safe in my transactions with the website.</td></tr><tr><td>Trust-2</td><td>I trust the website to keep my personal information safe.</td></tr><tr><td>Trust-3</td><td>I trust the website administrators will not misuse my personal information.</td></tr></table>

Appendix B. Factor loading

<table><tr><td></td><td>Attitude</td><td>Self-Efficacy</td><td>Intent</td><td>Vulner-ability</td><td>Severity</td><td>Resp. Efficacy</td><td>Sub. Norms</td></tr><tr><td>Attitude-1</td><td>0.88</td><td>0.38</td><td>0.45</td><td>0.01</td><td>0.29</td><td>0.57</td><td>0.30</td></tr><tr><td>Attitude-2</td><td>0.85</td><td>0.40</td><td>0.45</td><td>0.05</td><td>0.32</td><td>0.50</td><td>0.36</td></tr><tr><td>Attitude-3</td><td>0.79</td><td>0.26</td><td>0.42</td><td>0.11</td><td>0.18</td><td>0.47</td><td>0.37</td></tr><tr><td>Self_Eff-1</td><td>0.39</td><td>0.87</td><td>0.40</td><td>-0.17</td><td>0.21</td><td>0.30</td><td>0.20</td></tr><tr><td>Self_Eff-2</td><td>0.43</td><td>0.87</td><td>0.39</td><td>-0.18</td><td>0.16</td><td>0.35</td><td>0.21</td></tr><tr><td>Self_Eff-3</td><td>0.23</td><td>0.72</td><td>0.23</td><td>-0.16</td><td>0.14</td><td>0.25</td><td>0.13</td></tr><tr><td>Self_Eff-4</td><td>0.19</td><td>0.73</td><td>0.25</td><td>-0.23</td><td>0.12</td><td>0.27</td><td>0.07</td></tr><tr><td>Intent-1</td><td>0.52</td><td>0.42</td><td>0.93</td><td>-0.11</td><td>0.31</td><td>0.33</td><td>0.33</td></tr><tr><td>Intent-2</td><td>0.29</td><td>0.30</td><td>0.74</td><td>-0.08</td><td>0.15</td><td>0.16</td><td>0.14</td></tr><tr><td>Intent-3</td><td>0.48</td><td>0.34</td><td>0.89</td><td>-0.15</td><td>0.16</td><td>0.23</td><td>0.39</td></tr><tr><td>Vuln-1</td><td>0.07</td><td>-0.15</td><td>-0.10</td><td>0.93</td><td>0.14</td><td>0.10</td><td>-0.04</td></tr><tr><td>Vuln-2</td><td>0.04</td><td>-0.26</td><td>-0.15</td><td>0.83</td><td>0.04</td><td>0.11</td><td>0.03</td></tr><tr><td>Severity-1</td><td>0.32</td><td>0.21</td><td>0.19</td><td>0.14</td><td>0.90</td><td>0.39</td><td>0.11</td></tr><tr><td>Severity-2</td><td>0.27</td><td>0.15</td><td>0.26</td><td>0.03</td><td>0.90</td><td>0.29</td><td>0.10</td></tr><tr><td>Severity-3</td><td>0.27</td><td>0.18</td><td>0.23</td><td>0.13</td><td>0.92</td><td>0.32</td><td>0.10</td></tr><tr><td>Resp_Eff-1</td><td>0.49</td><td>0.29</td><td>0.18</td><td>0.05</td><td>0.33</td><td>0.81</td><td>0.21</td></tr><tr><td>Resp_Eff-2</td><td>0.53</td><td>0.31</td><td>0.30</td><td>0.20</td><td>0.29</td><td>0.87</td><td>0.24</td></tr><tr><td>Resp_Eff-3</td><td>0.51</td><td>0.32</td><td>0.25</td><td>0.04</td><td>0.32</td><td>0.81</td><td>0.15</td></tr><tr><td>Sub_Norm1</td><td>0.31</td><td>0.17</td><td>0.28</td><td>0.01</td><td>0.08</td><td>0.19</td><td>0.84</td></tr><tr><td>Sub_Norm2</td><td>0.38</td><td>0.23</td><td>0.33</td><td>0.04</td><td>0.14</td><td>0.28</td><td>0.85</td></tr><tr><td>Sub_Norm3</td><td>0.35</td><td>0.14</td><td>0.30</td><td>-0.08</td><td>0.07</td><td>0.15</td><td>0.87</td></tr></table>

Appendix C. Web site manipulation  
Secure Experiment Management System

![](/api/attachments/KWRQB5RS/fulltext/images/84fecfd7dd5ddb2666a9aaca1a5c24f46af1e65d7ed18d0d66e6236835c1a3be.jpg)  
Advancing Management Science through Information Sustems research

![](/api/attachments/KWRQB5RS/fulltext/images/e54437c8d21b2e24d2b85b140b053bb7670e5beeb61f00d0e740eda844e97e42.jpg)  
Low quality site

## References

[1] K.H. Guo, Y. Yuan, N.P. Archer, C.E. Connelly, Understanding nonmalicious se curity violations in the workplace: a composite behavior model. Journal of Management Information Systems 28 (2) (2011) 203–236.

[2] S.R. Boss, L.J. Kirsch, I. Angermeier, R.A. Shingler, R.W. Boss, If someone is watching, I'll do what I'm asked: mandatoriness, control, and information security, European Journal of Information Systems 18 (2) (2009) 151–164.

[3] T. Herath, H.R. Rao, Protection motivation and deterrence: a framework for security policy compliance in organisations, European Journal of Information Systems 18 (2) (2009) 106–125.

[4] C. Woo, G.L. Sanders, R.P. Cerveny, Exploring the influence of flow and psycho logical ownership on security education, training and awareness efectiveness and security compliance, Decision Support Systems 108 (March) (2018) 107–118.

[5] A. Adams, M. Sasse, Users are not the enemy, Communications of the ACM 42 (12) (1999).

[6] T. Herath, H.R. Rao, Encouraging information security behaviors in organizations: role of penalties, pressures and perceived efectiveness, Decision Support Systems 47 (2) (2009) 154–165.

[7] M. Chan, I. Woon, A. Kankanhalli, Perceptions of information security in the workplace: linking information security climate to compliant behavior, Journal of Information Privacy and Security 1 (3) (2005) 18–41.

[8] M. Warkentin, A.C. Johnston, IT governance and organizational design for security management, in: D. Straub, S. Goodman, R. Baskerville (Eds.), Information Security Policies and Practices, M.E. Sharpe, Armonk, NY, 2008, pp. 46–68.

[9] H. Zhang, K. Chari, M. Agrawal, Decision support for the optimal allocation of security controls, Decision Support Systems 115 (May) (2018) 92–104

[10] B. Bulgurcu, H. Cavusoglu, I. Benbasat, Information security policy compliance: an empirical study of rationality-based beliefs and information security awareness, MIS Quarterly 34 (3) (2010) 523–548.

[11] D. Straub, R.J. Welke, Coping with systems risk: security planning models for management decision making, MIS Quaterly December (4) (1998) 441–469.

[12] M. Warkentin, K. Davis, E. Bekkering, Introducing the check-of password system (COpS): an advancement in user authentication methods and information security Journal of Organizational and End User Computing (JOEUC) 16 (3) (2004) 41–58

[13] R. Willison, M. Warkentin, Beyond deterrence: an expanded view of employee computer abuse, MIS Ouarterly 37 (1) (2013) 1–20.

[14] I. Aizen, M. Fishbein, Understanding Attitudes and Predicting Social Behavior, NY Prentice Hall, Englewood Cliffs, 1980.

[15] V. Venkatesh, M. Morris, G. Davis, F. Davis, User acceptance of information

[16] M. Warkentin, R. Willison, Behavioral and policy issues in information systems security: the insider threat, European Journal of Information Systems 18 (2) (2009) 101–105.

[17] S.R. Boss, D.F. Galletta, P.B. Lowry, G.D. Moody, P. Polak, What do Systems users have to fear? Using fear appeals to engender threats and fear that motivate protective security behaviors, MIS Ouarterly 39 (4) (2015) 837–864

[18] B. Anderson, A. Vance, C.B. Kirwan, D. Eargle, J.L. Jenkins, How users perceive and respond to security messages: a NeuroIS research agenda and empirical study, European Journal of Information Systems 2016 (2015) (2016) 1–27

[19] M. Wu, R. Miller, S. Garfinkel, Do security toolbars actually prevent phishing attacks? Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, 2006, pp. 601–610.

[20] J.L. Jenkins, A. Durcikova, What, I Shouldn't have done that?: the influence of training and just-in-time reminders on secure behavior, International Conference on Information Systems. 2013. pp. 1–18.

[21] K. Rudolph, Implementing a security-awareness program, Computer Security

Handbook, Sixth edition, 2006.

[22] S. Furnell, M. Gennatou, P. Dowland, A prototype tool for information security awareness and training, International Journal of Logisitics Information Management 15 (5) (2002) 352–357

[23] P.P. Puhakainen, M. Siponen, Improving employee’ compliance through information systems security training: an action research study, MIS Quarterly 34 (4) (2010) 757–778.

[24] G. Dhillon, J. Backhouse, Current directions in IS security research: towards socioorganizational perspectives, Information Systems Journal 11 (2) (2001) 127–153.

[25] R.E. Petty, J.T. Cacioppo, The elaboration likelihood model of persuasion, Advances in Experimental Social Psychology 19 (1986) 123–205.

[26] F. Heider, Attitudes and cognitive organization, The Journal of Psychology 21 (1) (1946) 107–112.

[27] X. Luo, R. Brody, A. Seazzu, S. Burd, Social engineering: the neglected human factor for information security management, Information Resources Management Journal 24 (3) (2011) 1–8.

[28] C. Schooler, M.D. Basil, D.G. Altman, Alcohol and cigarette advertising on bill. boards: targeting with social cues. Health Communication 8 (2) (1996) 109–129

[29] R.J. Welch Cline, H.N. Young, Marketing drugs, marketing health care relation ships: a content analysis of visual cues in direct-to-consumer prescription drug advertising, Health Communication 16 (2) (2004) 131–157.

[30] D.M. Austin, L.A. Furr, M. Spine, The efects of neighborhood conditions on perceptions of safety, Journal of Criminal Justice 30 (5) (2002) 417–427.

[31] A. Benlian, Web personalization cues and their diferential efects on user as sessments of website value, Journal of Management Information Systems 32 (1) (2015) 225–260.

[32] H.H. Chang, S.W. Chen, The impact of online store environment cues on purchase intention: trust and perceived risk as a mediator, Online Information Review 32 (6) (2008) 818–841.

[33] H. Li, X. Luo, J. Zhang, H. Xu, Resolving the privacy paradox: toward a cognitive appraisal and emotion approach to online privacy behaviors, Information and Management 2016 (2016)

[34] R.T. Watson, G.M. Zinkhan, L.F. Pitt, Integrated Internet marketing. Communications of the ACM 43 (March 2017) (2000) 97–102.

[35] R.W. Rogers, A protection motivation theory of fear appeals and attitude change, The Journal of Psychology 91 (1) (1975) 93–114.

[36] I. Ajzen, The theory of planned behavior, Organizational Behavior and Human

[37] D.A. Garvin, What does “product quality” really mean? Sloan Management Review

[38] T.S.H. Teo, S.C. Srivastava, L. Jiang, Trust and electronic government success: an empirical study. Journal of Management Information Systems 25 (3) (2009) 99-132

[39] V.A. Zeithaml, Consumer perceptions of price, quality, and value: a means-end model and synthesis of evidence, Source Journal of Marketing 52 (3) (1988) 2–22

[40] C. Hjorth-Andersen, The concept of quality and the eficiency of markets for consumer products, Journal of Consumer Research 11 (2) (1984) 708.

[41] A. Kirmani, A.R. Rao, No pain, no gain: a critical review of the literature on signaling unobservable product quality, Journal of Marketing 64 (2) (2000) 66–79.

[42] S.C. King, A.J. Weber, H.L. Meiselman, N. Lv, The efect of meal situation, social interaction, physical environment and choice on food acceptability, Food Quality and Preference 15 (7–8 SPEC,JSS) (2004) 645–653

[43] J. Wells, J. Valacich, T. Hess, What signals are you sending? How website quality influences perceptions of product quality and purchase intentions, MIS Quarterly 35 (2) (2011) 373–396.

[44] D.A. Zellner, E. Siemers, V. Teran, R. Conroy, M. Lankford, A. Agrafiotis, ... P. Locher. Neatness counts. How plating affects liking for the taste of food. Appetite 57 (3) (2011) 642–648.

[45] N. Barber, J.M. Scarcelli, Enhancing the assessment of tangible service quality through the creation of a cleanliness measurement scale, Managing Service Quality 20 (1) (2010) 70–88.

[46] C. Michel, C. Velasco, E. Gatti, C. Spence, A taste of Kandinsky: assessing the influence of the artistic visual presentation of food on the dining experience, Flavou 3 (1) (2014).

[47] A.S. Devlin, S. Donovan, A. Nicolov, O. Nold, A. Packard, G. Zandan, “Impressive?” Credentials, family photographs, and the perception of therapist qualities, Journal of Environmental Psychology 29 (4) (2009) 503–512.

[48] P.P. Heppner, S. Pew, Efects of diplomas, awards, and counselor sex on perceived expertness, Journal of Counseling Psychology 24 (2) (1977) 147–149.

[49] R.A. Baron, Environmentally induced positive afect: its impact on self-eficacy, task performance, negotiation, and conflict, Journal of Applied Social Psychology 20 (5) (1990) 268–384

[50] S. Plous, The Psychology of Judgment and Decision Making, Mcgraw-Hill Book Company, 1993.

[51] G. Lindgaard, G. Fernandes, C. Dudek, J. Brown, Attention web designers: you have 50 milliseconds to make a good first impression!. Behaviour & Information Technology 25 (2) (2006) 115–126.

[52] S. Cebi, Determining importance degrees of website design parameters based on interactions and types of websites, Decision Support Systems 54 (2) (2013) 1030–1043.

[53] Y. Hwang, D.J. Kim, Customer self-service systems: the efects of perceived web quality with service contents on enjoyment, anxiety, and e-trust, Decision Support Systems 43 (3) (2007) 746–760.

[54] Y. Lee, K.A. Kozar, Understanding of website usability: specifying and measuring constructs and their relationships, Decision Support Systems 52 (2) (2012) 450–463.

[55] E.T. Loiocono, R.T. Watson, D.L. Goodhue, WebQUAL: a measure of website quality, Marketing Theory and Application 13 (3) (2002) 432–437.

[56] A.J. Elliot, M.A. Maier, A.C. Moller, R. Friedman, J. Meinhardt, Color and psychological functioning: the effect of red on performance attainment, Journal of Experimental Psychology: General 136 (1) (2007) 154–168.

[57] A.S. Soldat, R.C. Sinclair, Colors, smiles, and frowns: external afective cues can directly afect responses to persuasive communications in a mood-like manne without afecting mood, Social Cognition 19 (4) (2001) 469–490.

[58] M. Bauerly, Y. Liu, Efects of symmetry and number of compositional elements on interface and design aesthetics, International Journal of Human Computer Interaction 24 (3) (2008) 275–287

[59] B.J. Fogg, C. Soohoo, D. Danielson, L. Marable, J. Stanford, E.R. Tauber, How do users evaluate the credibility of web sites? A study with over 2,500 participants, Proceedings of the 2003 Conference on Designing for User Experiences, vol. 15, ACM, 2003, pp. 1–105.

[60] J. Kim, J.Y. Moon, Designing towards emotional usability in customer interfaces—trustworthiness of cyber-banking system interfaces, Interacting with Computers 10 (97) (1998) 1–29.

[61] J.H. Nielsen, J.E. Escalas, Easier is not always better: the moderating role of processing type on preference fluency, Journal of Consumer Psychology 20 (3) (2010) 295–305.

[62] N. Novemsky, R. Dhar, N. Schwarz, T. Simonson, Preference fluency in choice,

[63] D.M. Oppenheimer, Consequences of erudite vernacular utilized irrespective of necessity: problems with using long words needlessly. Applied Cognitive Psychology 20 (2) (2006) 139–156.

[64] R. Reber, P. Winkielman, N. Schwarz, Efects of perceptual fluency on afective judgments. Psychological Science 9 (1) (1998) 45–48.

[65] A. Everard, D.F. Galletta, How presentation flaws afect perceived site quality, trust. and intention to purchase from an online store. Journal of Management Information Systems 22 (3) (2005) 56–95

[66] F. Bélanger, J.S. Hiller, W.J. Smith, Trustworthiness in electronic commerce: the role of privacy, security, and site attributes, Journal of Strategic Information Systems 11 (3–4) (2002) 245–270.

[67] S. Gounaris, S. Dimitriadis, V. Stathakopoulos, Antecedents of perceived quality ir the context of internet retail stores, Journal of Marketing Management 21 (7–8) (2005) 669–700

[68] B. Harcourt, Reflecting on the subject: a critique of the social influence conception of deterrence, the broken windows theory, and order-maintenance policing New York, Michigan Law Review 97 (2) (1998) 291–389.

[69] J. Wilson, G. Kelling, Broken windows, Atlantic Monthly, 1982, pp. 1–9 (March)

[70] S. Tseng, B.J. Fogg, Credibility and computing technology, Communications of the ACM 42 (5) (1999) 39–44

[71] G. Ögütçü, Ö.M. Testik, O. Chouseinoglou, Analysis of personal information se curity behavior and awareness, Computers & Security 56 (2016) 83–93.

[72] H.Y.S. Tsai, M. Jiang, S. Alhabash, R. Larose, N.J. Rifon, S.R. Cotten, tive, Computers and Security 59 (1318885) (2016) 138–150

[73] J. Lee, M. Warkentin, A.C. Johnston, A broader view of perceived risk during internet transactions, Communications of the Association for Information Systems 38 (1) (2016) 171–189.

[74] R.W. Rogers, Cognitive and physiological processes in attitude change: a revised theory of protection motivation, Social Psychophysiology (1983) 153–176 (July).

[75] I.M. Lewis, B. Watson, K.M. White, Response eficacy: the key to minimizing rejection and maximizing acceptance of emotion-based anti-speeding messages, Accident Analysis and Prevention 42 (2) (2010) 459–467

[76] S. Krug, Don't Make me Think!: A Common Sense Approach to Web Usability, Pearson Education India, 2000

[77] V. Mummalaneni, An empirical investigation of web site characteristics, consumer emotional states and on-line shopping behaviors, Journal of Business Research 58 (4) (2005) 526–532.

[78] S. Folkman, R.S. Lazarus, C. Dunkel-Schetter, A. DeLongis, R.J. Gruen, Dynamic of a stressful encounter: cognitive appraisal, coping, and encounter outcomes, Journal of Personality and Social Psychology 50 (5) (1986) 992–1003.

[79] D.J. Kavanagh, G.H. Bower, Mood and self-eficacy: impact of joy and sadness on perceived capabilities, Cognitive Therapy and Research 9 (5) (1985) 507–525.

[80] H.H. Chang, S.W. Chen, Consumer perception of interface quality, security, and loyalty in electronic commerce, Information and Management 46 (7) (2009) 411–417.

[81] G.L. Stewart, S.H. Courtright, M.R. Barrick, Peer-based control in self-managing teams: linking rational and normative influence with individual and group performance, Journal of Applied Psychology 97 (2) (2012) 435–447.

[82] H. Zhang, X. Luo, Q. Liao, L. Peng, Does IT team climate matter? An empirical study of the impact of co-workers and the Confucian work ethic on deviance behavior. Information and Management 52 (6) (2015) 658–667.

[83] R. Cialdini, R. Raymond, K. Carl, A focus theory of normative conduct: recycling the concept of norms to reduce littering in public places, Journal of Personality and Social Psychology 58 (6) (1990) 1015

[84] M.A. Sasse, I. Flechais, Usable security: why do we need it? How do we get it? in: L.F. Cranor, S. Garfinkel (Eds.), Security and Usability: Designing Secure Systems That People Can Use, O'Reilly, 2005.

[85] T. Dinev, Q. Hu, The centrality of awareness in the formation of user behavioral intention toward protective information technologies, Journal of the Association for Information Systems 8 (7) (2007) 386–408

[86] S. Pahnila, M. Siponen, A. Mahmood, Employees' behavior towards IS security policy compliance, Proceedings of the Annual Hawaii International Conference on System Sciences, 2007 (April).

[87] I. Ajzen, M. Fishbein, Attitudinal and normative variables as predictors of specific behavior, Journal of Personality and Social Psychology 27 (1) (1973) 41–57.

[88] A. Bandura, Social cognitive theory: an agentic perspective, Annual Review of Psychology 52 (1) (2001) 1–26.

[89] F. Alsudani, M. Casey, The efect of aesthetics on web credibility, 23rd British HCI Group Annual Conference on People and Computers, 2009, pp. 512–519

[90] B.J. Fogg, Prominence-interpretation theory: explaining how people assess credibility online, Conference on Human Factors in Computing Systems, 2003, pp. 722–723.

[91] L. Zhang, W.C. McDowell, Am I really at risk? Determinants of online Users' in tentions to use strong passwords, Journal of Internet Commerce 8 (3/4) (2009) 180–197.

[92] C.L. Anderson, R. Agarwal, Practicing safe computing: a multimedia empirica examination of home computer user security behavioral intentions, MIS Quarterly 34 (3) (2010) 613–643.

[93] N. Hynes, Colour and meaning in corporate logos: an empirical study, Journal of Brand Management 16 (8) (2009) 545–555.

[94] A. Abbasi, Z. Zhang, D. Zimbra, H. Chen, J.F. Nunamaker Jr., Detecting fake websites: the contribution of statistical learning theory. MIS Ouarterly 34 (3) (2010) 435–461.

[95] Y. Lee, K.A. Kozar, Investigating the efect of website quality on e-business success: an analytic hierarchy process (AHP) approach, Decision Support Systems 42 (3) (2006)1383–1401.

[96] D. Cyr, M. Head, H. Larios, Colour appeal in website design within and across cultures: a multi-method evaluation. International Journal of Human-Computer Studies 68 (2010) 1–2), 1–21.

[97] P.B. Lowry, D.W. Wilson, W.L. Haig, A picture is worth a thousand words: source credibility theory applied to logo and website design for heightened credibility and consumer trust. International Journal of Human-Computer Interaction 30 (1 (2014) 63–93.

[98] N. Bonnardel, A. Piolat, L. Le Bigot, The impact of colour on website appeal and users' cognitive processes, Displays 32 (2) (2011) 69–80

[99] C.M. Ringle, S. Wende, J.-M. Becker, SmartPLS 3. Bönningstedt: SmartPLS, Retrieved from, 2015. http://www.smartpls.com.

[100] D. Straub, M.-C. Boudreau, D. Gefen, Validation guidelines for IS positivist research, Communications of the Association for Information Systems 13 (24) (2004).380–427

[101] N. Kock, Common method bias in PLS-SEM: a full collinearity assessment ap proach, International Journal of E-Collaboration 11 (4) (2015) 1–10.

[102] C.J. Armitage, M. Conner, Eficacy of the theory of planned behaviour: a meta analytic review, British Journal of Social Psychology 40 (Pt 4) (2001) 471–499.

[103] M. Conner, C.J. Armitage, Extending the theory of planned behavior: a review and avenues for further research, Journal of Applied Social Psychology 28 (15) (1998) 1429-1464

[104] D.J. Terry, M. a Hogg, K.M. White, The theory of planned behaviour: self-identity, social identity and group norms, The British Journal of Social Psychology 38 (Pt 3) (1999) 225–244.

![](/api/attachments/KWRQB5RS/fulltext/images/24caf6b14a8fdedc3b866dd47e587ded0b64b5662b9c0cbc67595bdbff779dbd.jpg)

received his Ph.D. in Management Information Systems from the University of Arizona.

Mark Grimes is Assistant Professor of Decision and Information Sciences in the Bauer College of Business at the University of Houston. His research focuses on information systems security and analysis of HCI behaviors to detect changes in emotional and cognitive states. Mark's research has been published in the Journal of the Association for Information Systems, Decision Support Systems, Information Technology for Development, Interacting with Computers, numerous conference proceedings, and has been presented to various industry and government stakeholders. Prior to entering academia, Mark worked as an IT infrastructure architect, specializing in large scale datacenter migrations, business continuity planning, and disaster recovery. Mark

![](/api/attachments/KWRQB5RS/fulltext/images/847701c6ce610d3961b8d30dade5a7f6d47556aa54ec8ea35d18d4eb0ca10f2e.jpg)  
Systems from the University of Arizona.

Jim Marquardson is Assistant Professor of Information Assurance and Cyber Defense in the College of Business at Northern Michigan University. His research interests include human computer interaction, persuasive technology, and the human factors of information security. Jim's research has been published in Interacting with Computers and presented at the Americas Conference on Information systems and to various government stakeholders. Jim worked for ExxonMobil's IT department as a senior information systems analyst. He developed software, engineered large software deployments, perform risk assessments, and optimized change management processes. After leaving industry, Jim received his Ph.D. in Management Information
