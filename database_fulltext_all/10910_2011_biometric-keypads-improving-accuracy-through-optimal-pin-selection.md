---
otero_id: 10910
otero_key: "GZD9F3E4"
title: "Biometric keypads: Improving accuracy through optimal PIN selection"
authors: "Benjamin Ngugi; Marilyn Tremaine; Peter Tarasewich"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.016"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Biometric keypads: Improving accuracy through optimal PIN selection

Benjamin Ngugi <sup>a,</sup>⁎, Marilyn Tremaine <sup>b,1</sup>, Peter Tarasewich <sup>a,2</sup>

<sup>a</sup> Information Systems and Operations Management, Suffolk University, 8 Ashburton place, Boston, MA 02108, USA

<sup>b</sup> Center for Advanced Information Processing, Rutgers University, 96 Freylinghuysen Road, Piscataway, NJ 08554, USA

## a r t i c l e i n f o

## Available online 19 Augsut 2010

Keywords: Authentication Security Biometrics Keypads Keystroke dynamics Typing patterns

## a b s t r a c t

While online applications can provide convenience to individuals and organizations, they can pose signi<sup>fi</sup>cant remote user authentication challenges. One possible solution to these challenges is to utilize behavioral typing patterns to provide an additional layer of authentication. Such behavioral biometrics have the advantage of being revocable if compromised, unlike physical biometrics such as <sup>fi</sup>ngerprints. This study investigates the viability of biometric keypads. Results indicate that biometric keypads can differentiate authentic users from impostors even when a secure PIN has been compromised. Furthermore, it is shown that authentication accuracy can be improved through optimal PIN selection by avoiding correlated key combinations.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Web 2.0 is revolutionizing the way people interact and conduct transactions through continued migration of information activities to the online environment. These changes present numerous business opportunities. The average person can now use the Web to conduct many basic life management activities like paying bills, purchasing products, and making travel plans. Most enterprises use the Web and its technologies for collecting and distributing information, conducting transactions, and managing their operations with individual consumers, business partners, other organizations, and employees.

The <sup>fl</sup>ip side of all this progress is a proliferation of personally identifying information such as user names, passwords, social security numbers, dates of birth, and mothers' maiden names being stored on disparate databases and information systems. If an intruder gains access to enough of this information, they can masquerade as an authentic user and gain access to secured resources. Given the continued increase in Web activity, it is not surprising that cases of computer intrusions and fraud continue to rise each year [10].

The mining and pro<sup>fi</sup>ling of behavioral patterns can assist in countering fraud, organized crime, and system intrusions (as well as many other criminal activities). Examples are cited here to illustrate each of these three applications, respectively. In a study by [6], a rulebased fraud detection system was designed to uncover indicators of fraudulent behavior from a large database of customer call transactions. In a second example [28], behavioral patterns were used to identify the strongest association paths between entities in criminal networks. Such information can be used by law enforcement agencies in <sup>fi</sup>ghting organized crime. Lastly, [4] proposed a real-time intrusion detection system capable of detecting break-ins, penetrations, and other types of computer abuse based on anomalous behavioral patterns. Such a system can be implemented as a core part of overall organizational security controls.

The use of such behavioral patterns should be done both at access control points (to prevent intruders from getting into systems) and within the network (to detect those who may have bypassed access control systems or trusted insiders who have access due to their organizational positions). This can be done through a defense-in-depth strategy in which several layers of controls are put around the protected resource such that an intruder would have to overcome one layer after another in order to succeed [26]. This gives the organization time to react, and possibly defend or recover from the attack.

Typing patterns can be used to increase organization security by adding a second layer to current authentication systems. Two commonly used authentication systems are knowledge-based (for example, using passwords) and token-based (using a smart card, for example) or a combination of the two. These systems can become compromised if an intruder acquires the password and/or the token. Adding a layer of behavioral biometrics (biometrics which depend on human behavioral characteristics) makes such systems more robust since it is harder to separate biometric patterns from their owners. Thus it becomes harder for a hacker to masquerade as another user.

The current tendency is to use physical biometrics (biometrics which depend on human physical characteristics) for a second control layer. For example, <sup>fi</sup>ngerprints have been used to strengthen authentication systems due to their high recognition accuracy [21]. Physical biometrics, however, have large drawbacks in that they are expensive, non-standardized, and not easily revoked if compromised (for example, the <sup>fi</sup>ngerprints captured from a user cannot be changed as the user has only one set). Furthermore, most physical biometric systems require proprietary hardware and software [20].

In contrast, behavioral biometrics can provide an alternative solution to physical biometrics at a cheaper cost and address several of the previously mentioned drawbacks. However, most behavioral biometric techniques and applications are relatively unexplored and untested, which calls for more research to create usable systems for commercial purposes [29]. Thus, there is a need for further improvements in behavioral pattern solutions if they are to achieve their potential in detecting and preventing intrusions. One challenge to be addressed is the fact that a person's behavior may change over time as he or she learns to perform a task faster. This may impact the performance of behavioral biometric techniques; especially if such change occurs the same way (co-varies) in several portions of the same task. This study shows that such a challenge exists when using typing biometric keypads for authentication. Such keypads capture key-press typing patterns to build unique pro<sup>fi</sup>les for differentiating individuals.

This study contributes to the understanding and use of behavioral biometrics in several ways. First it demonstrates that the typing patterns made when entering a PIN can be used to differentiate an authentic user from an impostor even when the impostor knows the authentic user's PIN. Secondly, the study investigates whether the choice of PINs can be used to improve resulting authentication accuracy. Thirdly the study explains the implications of these <sup>fi</sup>ndings to the <sup>fi</sup>elds of behavioral biometrics and usability design. PINs are common passwords used on numeric keypads with applications such as automated teller machines (ATMs) and information systems which are accessed through telephones. The biometric data collected from users of these applications is mined to discover patterns used to verify whether the PIN is actually being typed by its owner or not. This method is software-based, so it is relatively inexpensive to implement, easy to use, transportable, and can be used on any network including the Internet. Study results show that the method holds promise as being a reliable authentication method that can be used in conjunction with password-based systems.

The remainder of the paper is organized is follows. Section 2 reviews previous work on biometric keypad performance and the acquisition of human motor skills. Section 3 develops hypotheses which are tested in a study of the effects of PIN design on authentication accuracy. The design and methodology of the study are detailed in Section 4, and Section 5 presents the results of the study. Section 6 discusses the study's <sup>fi</sup>ndings and its implications for behavioral biometrics, system usability, and security design. This is followed by limitations of the study and avenues for future work in Section 7.

## 2. Related work

This section starts by reviewing how biometric keypads work and how their performance can be improved. This is followed by a review of what is known on human typing patterns on different PIN combinations.

## 2.1. Improving the performance of typing biometric keypads

Biometric keypads work either in enrollment mode or in authentication mode [11]. During enrollment, the user provides his or her biometric patterns to the system. The desired features are then extracted, labeled, and stored in a biometric template database. In authentication mode, a pattern template collected during a current log-in attempt by a user is compared with a stored pattern template captured from the user during enrollment. The user is granted access only if the patterns match or are otherwise determined to have come from the same person.

The performance of a biometric authentication system can primarily be hindered by two types of errors, a false rejection rate (FRR) and a false acceptance rate (FAR). FAR (also called a type II error) is the probability that an impostor will be falsely accepted as a legally registered user. FRR (also called a type I error) is the probability that a legally registered user will be falsely rejected by a system when presenting his or her biometric feature(s) [9].

Earlier work in the area of keystroke dynamics demonstrated that key-press time (time that a key is held down), inter-key time (time between releasing one key and pressing the next), <sup>fi</sup>nger placement, and applied pressure are unique for different individuals and can hence be used to construct a unique user signature which can be used for veri<sup>fi</sup>cation [12,15]. There are several extensions of this work that will not be covered here in detail, but the interested reader is referred to a summary of twenty-three different studies that have been done in the area of biometric keypads [19]. Most of the reported studies have error rates (both FAR and FRR) ranging from about 1% to 10% with the median around 3%. These are commendable rates for behavioral biometrics. However, most of these studies reported that an average of about 10 key-presses were required for authentication, and <sup>fi</sup>ve of the studies reported using over 100 key-presses per authentication. Common consumer access control devices such as ATM keypads, however, only allow an average of four digits (key-presses) per PIN. This means that authentication performance from such devices would most likely be less since the number of distinguishing features used for authentication is reduced. This calls for concerted efforts in improving the performance of biometric keypads if they are to be commercially viable and widely accepted.

There are various ways that can be used to improve the performance of the biometric keypads. One approach has been the design of better classi<sup>fi</sup>ers through the use of new technologies like neural networks and support vector machines [18,30]. Classi<sup>fi</sup>ers are programs that separate a group of patterns into their separate categories or classes [5]. Another approach is the enrichment of the classi<sup>fi</sup>er by increasing the number of features that can be used for classi<sup>fi</sup>cation. For example, the addition of pressure has been shown to improve classi<sup>fi</sup>cation [13,17]. Likewise, the inclusion of the acoustics produced when pressing the keys has been shown to lead to better classi<sup>fi</sup>cation [1,7].

The study reported in this paper focuses on improving biometric keypads by better understanding the variation and correlations of key-press and inter-key times of different PIN combinations. This knowledge can then be leveraged to select key combinations that result in optimal performance. The next section reviews previous work in psychology on the acquisition of human motor skills such as typing to provide a theoretical foundation for this study.

## 2.2. Acquisition of skills and habits

Research discussed in Section 2.1 shows that key-press times, inter-key times, and the pressure applied to keys are unique among individuals, and can therefore be used to authenticate a given user. Key-press and inter-key times can be easily and reliably captured on existing systems. Obtaining pressure patterns, however, requires proprietary hardware which can be expensive and may not viable for use across different organizations and applications over the Internet. Thus the study in this paper focuses only on better understanding the variations and correlations patterns made from timing durations (both key-press and inter-key) when entering PINs.

Fitts' law, as extended to two-dimensional tasks [14], can be used to predict the time it takes to move from one key to another within a particular biometric keypad layout. The law states that the time required to move to and to select a target of width W which lies at a distance (or amplitude) A from a starting location is:

$$
\mathrm{MT} = \mathrm{a} + \mathrm{b} \log_ {2} (2 \mathrm{A} / \mathrm{W})\tag{1}
$$

where a and b are constants determined through linear regression. The log term is the index of dif<sup>fi</sup>culty. This means that for a standard computer keypad with <sup>fi</sup>xed key widths, key-press times will be determined by the distance from a starting key to a target key and the index of dif<sup>fi</sup>culty.

Learning to type a PIN on a biometric keypad is a motor learning skill, hence we can use <sup>fi</sup>ndings from previous studies in psychology. Early work in psychology looked at the patterns that occurred in learning to transmit Morse code [2]. The researchers demonstrated that learning to send or receive Morse code consisted of the acquisition of psycho-physical habits. Some of these habits were low-level while others were high-level. An example of a low-level task is learning to type a single letter (or dot) on a keyboard; typing a whole word or sentence from memory would be a high-level task.

The time to perform the perceptual skill of identifying patterns of dots and dashes was measured over time along with the total time to type in a sequence of code. The time to perform these skilled tasks was found to decrease steadily until it plateaued. After remaining at this constant level for a while, subject performance time would again start decreasing steadily until a second plateau was reached, and so on. A plateau in the curve meant that the improvement in a given lower order habit was approaching its development maximum but was not yet automatic enough to allow attention to move to the next order level habit. Furthermore, it was shown that connected words (for example, words that form a logical sentence) could be read faster than disconnected words. Likewise, letters connected in words could be processed faster than disconnected letters.

A key question is whether such results can be extended to the typing of different PIN combinations and subsequently to other behavioral biometrics. For example, would a connected PIN (one which has a common sequence, like 1234) be typed faster than a disconnected PIN (one which has an unfamiliar sequence, like 1324)? Even more important, would the choice of a connected or disconnected PIN determine the stability of timing patterns, and would such a choice affect the overall accuracy of the authentication system?

Studies conducted with typists suggest that this might be so. One study [8] found that inter-key time for one digraph (a pair of characters) was found to have more variability than another. For example, the distribution of inter-key times for the digraph “ce” had a median of 204 milliseconds (ms) and a half-width (the point at which a signal's amplitude is half of what it was at its peak) of 20 ms, but the distribution for “ne” had a median of 120 ms and a half-width of 41 ms. Thus, some key combinations, because of their higher variance, may be harder to classify than others.

Further research showed that in a number of cases, the inter-key interval for a given digraph differed signi<sup>fi</sup>cantly depending on the word in which the digraph was embedded [24]. For example, they found that the inter-key interval for the digraph “an” was 147 ms in the word “thank” and 94 ms in the word “ran.” A simulation model for typing was created in which keystroke timing was based on keyboard layout and the physical constraints to the hands. Test results showed context effects similar to those found in [22] which were explained by key distances and hand interchanges in the keying pattern. It is likely that the learning and context effect may exhibit differences among users and impact authentication accuracy. However, no studies have looked at the individual differences found between these digraphs or the relationship between PIN patterns and authentication accuracy.

## 3. Study of the use of two different PINs

Five hypotheses were developed to study authentication accuracy behavior with two different PIN combinations. The <sup>fi</sup>rst two hypotheses compare typing pattern differences between individual subjects, while the last three hypotheses compare the variations and correlations between the two PINs. Results of typing studies discussed in Section 2.2 suggest that typing patterns are unique for every individual and can be used to authenticate or differentiate a given individual from impostors [15]. However, these observations are based on testing large amounts of text, and it is not known whether the same would hold true for a four-digit PIN, even when an impostor knows an authentic user's PIN. This leads to our <sup>fi</sup>rst hypothesis:

H1. Typing patterns differ across subjects.

This will be tested for the two different key duration metrics:

H1a. Key-press times differ across subjects.

H1b. Inter-key times differ across subjects.

Second, if individuals have unique typing patterns, as suggested by the <sup>fi</sup>rst hypothesis, then it should be possible to develop a typing biometric keypad that can accurately differentiate a given individual from any impostors, even if they are all using the same PIN. The typing biometric system should allow an authentic user to have access to protected resources while rejecting an impostor, which leads to the second hypothesis:

H2. Typing biometrics differentiate authentic users from impostors.

This will be tested by measuring how well the typing biometric accepts authorized users (with minimal false rejection rates) and rejects impostors (with minimal false acceptance rates):

H2a. The typing biometric keypad will accept authorized users.

H2b. The typing biometric keypad will reject impostors.

Third, previous work suggested that it may be easier to type some keys and words than others. An experiment was performed to test this hypothesis. Two PINs, “1234” and “1324”, were selected for comparison purposes. These are referred to as PIN 1 and PIN 2, respectively. PIN 1 was selected for several reasons: First, the keys are linearly and sequentially placed on the keypad. Second, it consists of the counting sequence of numbers one through four, taught from an early age and hence easy to remember. PIN 2 reverses the middle two digits in the <sup>fi</sup>rst PIN to make it more dif<sup>fi</sup>cult both to type and recall. The sequence of key-presses necessary to enter each PIN is shown in Fig. 1. Based on previous work [2], it seems likely that the time necessary to enter PIN 1 will be less than that for PIN 2 since the former is faster to recall and type. This leads to a third hypothesis:

H3. PIN 2 will take longer to enter than PIN 1.

This will be tested for the two key duration metrics:

H3a. Total key-press time will be greater for PIN 2 than for PIN 1.

H3b. Total inter-key time will be greater for PIN 2 than for PIN 1.

Fourth, since PIN 1 is easier to recall and type than PIN 2 as suggested by the third hypothesis, the learning curve for PIN 1 will be steeper due to a more rapid improvement in typing speed when compared to PIN 2. This more rapid improvement means that there should be greater variance in the typing patterns of PIN 1 over time. Further, the improvement in the typing pattern durations will correlate more for PIN 1 than for PIN 2 since the <sup>fi</sup>rst three digits of PIN 1 are sequential, leading to easier typing biomechanics (physical <sup>fi</sup>nger movement). This leads to the next hypotheses to be tested in the experiment:

H4. PIN 2 typing patterns will have fewer correlations than those of PIN 1.

This will be tested for all possible correlations between the seven (four key-press and three inter-key) key durations. The degree of correlation is usually measured by a correlation coef<sup>fi</sup>cient. The correlation coef<sup>fi</sup>cient between two random variables is their covariance (how much two variables change together, or co-vary) divided by the product of their standard deviation [3]. The coef<sup>fi</sup>cient ranges between +1 and −1 (denoting positive and negative correlations) and is equal to 0 when the two variables are independent.

![](/api/attachments/GZD9F3E4/fulltext/images/f17433051f13280c9478382df05d25df8eb1e5c42acbc3a65bf085616590c375.jpg)  
Fig. 1. Illustration of the keypad <sup>fi</sup>nger movements.

Fifth, for an authentication classi<sup>fi</sup>er system, a lower correlation in PIN 2 would mean that the different typing pattern features are more independent of each other and hence have higher differentiating power compared to PIN 1. For example, a classi<sup>fi</sup>er using three typing variables (Key1, Key2, and Key3), two of which were fully dependent (say Key1 and Key2) would be equivalent to same classi<sup>fi</sup>er only using Key1 and Key3, since Key2 cannot offer anything that Key1 is not already providing. This should lead to lower authentication accuracy for PIN 1. This leads to a <sup>fi</sup>fth hypothesis:

H5. Typing patterns for PIN 1 will be less accurate than those of PIN 2.

Speci<sup>fi</sup>cally, this hypothesis will be tested for each of the two biometric performance measures (FAR and FRR), creating the subhypotheses:

H5a. Keying patterns for PIN 1 will have higher false acceptance rates (FAR) than those for PIN 2.

H5b. Keying patterns for PIN 1 will have higher false rejections rates (FRR) than those for PIN 2.

These <sup>fi</sup>ve hypotheses are directly related to an experimental design, described in the following section, which selects two PIN numbers to test.

## 4. Design of experiment

A two by one factorial design was used to build the experiment using the two PINs as the independent variables. The dependent variables were key-press and inter-key time durations, as well as authentication accuracy (false acceptance and false rejection rates).

## 4.1. Description of subjects

The subjects who participated in the biometric keypad experiment were undergraduate students enrolled in a software engineering class at a large university in the eastern United States. For extra credit, students could either volunteer to participate in the experiment or do an alternative assignment. Twenty-four subjects participated in the study. All were enrolled in a college of computing at the university and were in their 2nd or 3rd year of study. Subjects ranged in age from 18 to 33 years old with a median age of 22 years. Twenty-<sup>fi</sup>ve percent (six) of the subjects were female and 75% (eighteen) were male. All subjects had considerable prior experience using an ATM machine (i.e., greater than 12 months of regular use). All subjects were right handed.

## 4.2. Methodology

Relevant demographic data was collected <sup>fi</sup>rst using a short questionnaire after signing an informed consent form. The twentyfour subjects were randomly divided into two groups of twelve subjects each. The <sup>fi</sup>rst group was assigned PIN 1 (1234) while the second group was assigned PIN 2 (1324). The experiment took approximately 20 min to complete, and subjects were scheduled at thirty-minute intervals in a testing laboratory over the course of several days. The subjects were then trained on the experimental task. During the training, subjects were asked to type “T” (for true) or “F” (for false) to a set of world trivia questions [23]. After each answer, they entered their assigned 4 digit PIN number as a way of con<sup>fi</sup>rming their answer. The next question was then displayed. Subjects were not told whether their question responses were correct or not to avoid confounding effects. Subjects were given time to practice answering the questions until they indicated that they felt pro<sup>fi</sup>cient with the typing program which typically took about <sup>fi</sup>ve to ten questions. They then moved on to the main test which consisted of twenty-<sup>fi</sup>ve questions. Fig. 2 shows an example trial in the experiment. The <sup>fi</sup>rst <sup>fi</sup>ve questions in the set were considered warm-up questions, so each session of twenty-<sup>fi</sup>ve trials resulted in a set of twenty PIN typing patterns for each subject that were used for data analysis.

A computer program called Lab-View [16] was used to sample data from this keyboard. The timing features were extracted from each subject's data [17]. The experiment was designed to avoid measurement errors and the possible confounding of variables. This was accomplished by implementing the following steps and actions into the procedure:

1) All subjects were trained until they indicated that they felt pro<sup>fi</sup>cient with the program. Most subjects felt ready after between <sup>fi</sup>ve and seven questions.

2) Subjects answered a world trivia question and then entered a PIN instead of being asked to simply type in a PIN multiple times. The question was used to <sup>fi</sup>rst divert the subjects’ attention from the mechanics of keying the PIN for each trial through the cognitive task of answering the questions correctly. This resulted in an experimental task that closely parallels the use of PINs in the real world (such as when using an ATM machine) with users responding automatically with their learned typing patterns at the point in time when a PIN becomes necessary.

3) Subjects were instructed to only use the numeric keypad and not the row of numbers across the top of the keyboard. The numeric keypad is a close approximation of a typical ATM keypad.

![](/api/attachments/GZD9F3E4/fulltext/images/0df700376a49dfeaee62c705ecba0711fb4c82794ac52a54a1d64227e824ea20.jpg)  
Fig. 2. World trivia welcome and question screens.

4) Subjects received the error message “Wrong PIN” on the screen if the PIN was incorrectly entered and were asked to enter the PIN again. This also simulates typical ATM interactions. Erroneous data was not used in the <sup>fi</sup>nal analysis of results.

5) Experiments were performed in a controlled laboratory environment to minimize any outside disturbances and to ensure that the setting remained consistent across all participants. Chairs were adjusted so that a subject's elbows were level with the biometric keyboard.

A Microsoft extended keyboard (model E06401PS2) with a keypad number arrangement similar to the one shown in Fig. 1 was used for the experiment. It was kept at the same angle for each subject.

## 5. Results

This section presents 1) the results in the PIN key-press and interkey time durations and 2) the effect of each PIN combination on the classi<sup>fi</sup>ers' performance.

## 5.1. Comparison of typing pattern durations across subjects

PIN 1 (1234) produced four key-press times (the time from when a key is <sup>fi</sup>rst pressed until it released) labeled Key1, Key2, Key3 and Key4, and three inter-key times (the time between the release of one key and the pressing of another) labeled Key12, Key23 and Key34.

“Key12” designates the time between releasing Key 1 and pressing Key 2; other labels follow this same notation. Likewise, PIN 2 (1324) produced four key-press times Key1, Key3, Key2, and Key4, and three inter-key times Key13, Key32, and Key24.

H1 suggested that the typing patterns would be a different across subjects. To test the validity of this hypothesis, the average key-press and inter-key times were compared across the twelve subjects for each of the two PINs. For PIN 1, both the key-press times (F=162.3, pb0.0001) and inter-key times (F=89.9, pb0.0001) are signi<sup>fi</sup>cantly different. Similarly for PIN 2, both the key-press times (F=196.7, pb0.0001) and inter-key times (F=83.7, pb0.0001) are signi<sup>fi</sup>cantly different. This supports H1.

## 5.2. Comparison of typing pattern durations across the two PINs

The means for each key-press and inter-key time are shown in Table 1. The grand mean for key-press times of PIN 1 was computed by taking the average of the four key-press times. The remaining three grand means were computed in a similar manner.

The key-press time grand mean for PIN 2 is signi<sup>fi</sup>cantly greater than that of PIN 1 (t=13.65, p=.0001), but there is no signi<sup>fi</sup>cant difference in the inter-key time grand means. Therefore, H3a is supported but H3b is not. This can be explained by the fact that PIN 2 is more complex (that is, more dif<sup>fi</sup>cult to recall) than PIN 1, making the time it takes to determine movement from one key to the next greater for PIN 2.

Table 1  
Comparison of typing pattern durations across the two PINs

<table><tr><td colspan="2">PIN</td><td colspan="5">Key-press times (milliseconds)</td><td colspan="4">Inter-key times (milliseconds)</td></tr><tr><td rowspan="2">One</td><td></td><td>Key1</td><td>Key2</td><td>Key3</td><td>Key4</td><td>Grand Mean</td><td>Key12</td><td>Key23</td><td>Key34</td><td>Grand Mean</td></tr><tr><td>Mean</td><td>110.7</td><td>113.4</td><td>95.5</td><td>123.0</td><td>110.7</td><td>193.3</td><td>184.7</td><td>236.4</td><td>204.8</td></tr><tr><td rowspan="2">Two</td><td></td><td>Key1</td><td>Key2</td><td>Key3</td><td>Key4</td><td>Grand Mean</td><td>Key13</td><td>Key32</td><td>Key24</td><td>Grand Mean</td></tr><tr><td>Mean</td><td>130.7</td><td>122.6</td><td>122.7</td><td>137.7</td><td>128.4</td><td>201.0</td><td>191.3</td><td>214.9</td><td>202.4</td></tr><tr><td>Significant</td><td></td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td rowspan="2">difference in the PIN means?</td><td></td><td>t = -4.41</td><td>t = -2.50</td><td>t = -7.40</td><td>t = -3.95,</td><td>t = -13.65,</td><td>t = -2.09</td><td>t = -1.81</td><td>t = 5.80</td><td>t = 0.85</td></tr><tr><td></td><td>p &lt; .0001</td><td>p = .1023</td><td>p &lt; .0001</td><td>p &lt; .0001</td><td>p &lt; 0.0001</td><td>p = .0364</td><td>p = .0708</td><td>p &lt; .0001</td><td>p = 0.397</td></tr></table>

Table 3  
Table 2  
Correlations between the different key durations for PIN 1.

<table><tr><td rowspan="2"></td><td colspan="4">Key-press</td><td colspan="3">Inter-key</td></tr><tr><td>Key 1</td><td>Key 2</td><td>Key 3</td><td>Key 4</td><td>Key 12</td><td>Key 23</td><td>Key 34</td></tr><tr><td>Key 1</td><td>1.000</td><td>0.536</td><td>0.503</td><td>0.427</td><td>0.157</td><td>0.168</td><td>0.115</td></tr><tr><td>Key 2</td><td></td><td>1.000</td><td>0.857</td><td>0.430</td><td>-0.345</td><td>-0.237</td><td>-0.068</td></tr><tr><td>Key 3</td><td></td><td></td><td>1.000</td><td>0.376</td><td>-0.253</td><td>-0.196</td><td>-0.079</td></tr><tr><td>Key 4</td><td></td><td></td><td></td><td>1.000</td><td>-0.260</td><td>-0.265</td><td>-0.126</td></tr><tr><td>Key 12</td><td></td><td></td><td></td><td></td><td>1.000</td><td>0.850</td><td>0.644</td></tr><tr><td>Key 23</td><td></td><td></td><td></td><td></td><td></td><td>1.000</td><td>0.597</td></tr><tr><td>Key 34</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.000</td></tr></table>

Correlations between the different key durations for PIN 2.

<table><tr><td rowspan="2"></td><td colspan="4">Key-press</td><td colspan="3">Inter-key</td></tr><tr><td>Key 1</td><td>Key 3</td><td>Key 2</td><td>Key 4</td><td>Key 13</td><td>Key 32</td><td>Key 24</td></tr><tr><td>Key 1</td><td>1.000</td><td>0.719</td><td>0.733</td><td>0.333</td><td>0.012</td><td>-0.075</td><td>0.403</td></tr><tr><td>Key 3</td><td></td><td>1.000</td><td>0.617</td><td>0.269</td><td>-0.247</td><td>-0.287</td><td>0.398</td></tr><tr><td>Key 2</td><td></td><td></td><td>1.000</td><td>0.338</td><td>-0.202</td><td>-0.147</td><td>0.337</td></tr><tr><td>Key 4</td><td></td><td></td><td></td><td>1.000</td><td>0.121</td><td>0.225</td><td>0.279</td></tr><tr><td>Key 13</td><td></td><td></td><td></td><td></td><td>1.000</td><td>0.552</td><td>0.274</td></tr><tr><td>Key 32</td><td></td><td></td><td></td><td></td><td></td><td>1.000</td><td>0.304</td></tr><tr><td>Key 24</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.000</td></tr></table>

A paired key-by-key comparison con<sup>fi</sup>rms this. Each of the four average key-press times (Key1, Key2, Key3, and Key4) is higher for PIN 2 than for PIN 1. Thus, there is a difference in times for the same keys when used in different PIN sequences. These key-press time differences are signi<sup>fi</sup>cant as shown by the t-values in Table 1. This supports H3a. The lack of support for H3b probably results from the fact that the inter-key times from PIN 1 (Key12, Key23 and Key34) do not directly correspond to those of PIN 2 (Key13, Key32, and Key24); hence they are dif<sup>fi</sup>cult to compare as they involve different typing dynamics.

## 5.3. Comparison of typing pattern correlations within the two PINs

The next step was to compare the correlations within the two PINs for all seven (four key-press and three inter-key) durations. Tables 2 and 3 show the Pearson correlation coef<sup>fi</sup>cients for PIN 1 and PIN 2, respectively. The gray cells indicate those correlation coef<sup>fi</sup>cients which are greater than 0.5 and are statistically signi<sup>fi</sup>cant (p≤.05).

It is observed that PIN 1 has six correlations meeting these criteria, while PIN 2 has four. Thus PIN 2 has fewer correlations compared with PIN 1, which supports H4.

## 5.4. Algorithm used to develop and compute accuracy rates

This section explains how two performance measures (FAR and FRR) of the typing biometric keypad were computed. Two sets of typing patterns in total were captured for the two PINs. The following algorithm was used to develop the classi<sup>fi</sup>er for PIN 1 and then repeated for PIN 2. The seven typing times (key-press and inter-key)

for each subject were <sup>fi</sup>rst extracted from recorded experimental data. A test for outliers was performed using a Matlab toolbox [25]. This toolbox uses a method <sup>fi</sup>rst developed by [27] to detect a single outlier from a multivariate sample of data points and later extended by to detect multiple outliers. The method uses an F-distribution to test whether or not a signi<sup>fi</sup>cant difference exists between a given set of typing times (Key1…Key34) from the rest of the typing patterns made by the same subject in a given time period. Finding signi<sup>fi</sup>cance means that the set in question is an outlier. This exercise was repeated on the data collected from each subject. The maximum number of outliers found in the experiment for a given subject was two.

A four-fold cross-validation algorithm (K=4 folds was experimentally determined to be optimum) was then used to train a Support Vector Machine (SVM) classi<sup>fi</sup>er which could then determine whether a pattern belonged to the authentic user or an impostor. For a given iteration, three quarters of the keying pattern data are randomly selected and used to train the SVM classi<sup>fi</sup>er while the remaining quarter is used to test it. This process is shifted forward three more times for the remaining folds so that a different quarter of patterns is selected each time for testing while the remainder are used for training. A detailed explanation of this process can be found in [17]. Training and testing were repeated using a bootstrap algorithm for 20 iterations. After each iteration of the bootstrap algorithm, the classi<sup>fi</sup>cation for each subject was examined and given a score of 1 (authentic user) or 0 (impostor). FAR for each cycle was computed as the number of impostor patterns wrongly classi<sup>fi</sup>ed as belonging to the authentic user divided by the total number of impostor patterns. FRR was computed as the number of authentic user patterns wrongly classi<sup>fi</sup>ed as impostor divided by the total number of authentic patterns for each cycle. The same process was used to develop a classi<sup>fi</sup>er for PIN 2.

## 5.5. Comparison of authentication accuracy across subjects

Table 4 shows the accuracy rates results of FAR and FRR for each subject that used PIN 1 while Table 5 shows the corresponding results for subjects that used PIN 2. The goal of this part of the analysis was to determine whether the typing biometric keypad classi<sup>fi</sup>ers could accurately differentiate the authentic users from the rest of the group members acting as impostors for each PIN. It is seen that the classi<sup>fi</sup>ers performed very well, with the worst FAR and FRR rates all being below 1.6% and 15.7% respectively. This supports H2a and H2b, and con<sup>fi</sup>rms that the typing biometric keypads can be used as a second layer for security. It is also observed that the FAR rate is much lower than the FRR rate. FAR is normally the more critical measure since it indicates the percentage of impostors allowed access to the protected resource. FRR indicates the percentage of authentic users denied access and usually requested to re-authenticate. It is thus an annoyance factor, but users are usually willing to submit their biometrics a second time if this is the tradeoff for better security [17].

## 5.6. Comparison of authentication accuracy across the two PINs

Table 6 shows the grand mean accuracy results of FAR and FRR for subjects using PIN 1 and PIN 2. This was computed by averaging the individual accuracy rates for authenticating each of the twelve individuals in each PIN group. Comparing the two grand means, it can be seen that PIN 1 has higher false acceptance and rejection rates than PIN 2. The differences are statistically signi<sup>fi</sup>cant as shown by the test results in the last column of Table 6.

Table 4  
Performance measure accuracy rates for subjects when using PIN 1.

<table><tr><td>Subject</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>Overall average</td></tr><tr><td>FAR</td><td>1.60</td><td>0.80</td><td>0.50</td><td>0.80</td><td>1.20</td><td>0.90</td><td>0.50</td><td>0.30</td><td>0.70</td><td>0.60</td><td>0.30</td><td>0.002</td><td>0.70</td></tr><tr><td>FRR</td><td>3.70</td><td>6.60</td><td>2.00</td><td>13.65</td><td>8.60</td><td>15.7</td><td>7.60</td><td>3.20</td><td>5.80</td><td>6.70</td><td>0.80</td><td>0.006</td><td>6.22</td></tr></table>

Table 5  
Performance measure accuracy rates for subjects when using PIN 2.

<table><tr><td>Subject</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>Overall average</td></tr><tr><td>FAR</td><td>0.00</td><td>0.30</td><td>0.80</td><td>0.18</td><td>1.10</td><td>0.30</td><td>0.70</td><td>0.40</td><td>0.60</td><td>0.50</td><td>0.80</td><td>0.40</td><td>0.59</td></tr><tr><td>FRR</td><td>2.00</td><td>6.00</td><td>2.00</td><td>1.00</td><td>6.30</td><td>2.90</td><td>1.70</td><td>2.60</td><td>1.80</td><td>3.80</td><td>2.30</td><td>1.70</td><td>4.50</td></tr></table>

Thus, the two performance measures (FAR and FRR) are worse for PIN 1 than for PIN 2 as suggested by H5. This can be attributed to the lower correlations in PIN 2, which results in more accurate authentication.

## 6. Discussion

The results of the study show support for each of the <sup>fi</sup>ve hypotheses proposed in Section 3. Overall, the results have several implications for applications in behavioral biometrics, usability, and security design.

The <sup>fi</sup>rst and second hypotheses are closely related and were aimed at testing individual user differences. Testing of the <sup>fi</sup>rst hypothesis showed that typing patterns durations differ across different subjects. This suggests that such patterns can be used to differentiate individuals. This is con<sup>fi</sup>rmed by the results of the second hypothesis, which indicated that such patterns can be used to accurately differentiate authentic users from impostors with very reasonable FAR and FRR rates. This is in line with earlier work [15], but makes two new contributions. First, it overcomes the earlier shortcoming of requiring large amounts of text for validation, which does not match current ATM practices which usually allow the use of only four to six digits. Secondly, it extends previous work to situations where a PIN sequence has been compromised and is known by an impostor. In this case, results indicate that the typing biometric keypad can still differentiate the authentic user from the impostor.

Testing of the third hypothesis indicated that the average time to type PIN 1 was shorter than that of PIN 2. This can be important for usability design as it offers a metric for choosing a PIN if the goal is to minimize the time spent by the user on the keypad. Furthermore, results showed that there is a difference in key-press times for the same keys (Keys 1, 2, 3, and 4) when used in another PIN sequence. This has implications for behavioral biometrics and security design. As discussed in Section 1, one of the disadvantages of physical biometrics such as retinal scan is that it cannot be revoked (changed) if compromised. On the other hand, behavioral biometrics like the typing patterns can be revoked by choosing another combination. Now that results have shown that patterns are different for the same keys when used in different PIN sequence, it can become more dif<sup>fi</sup>cult to compromise a given pattern since it is now like chasing a moving target. If patterns did not change with different PIN sequence, then it would be theoretically possible for an impostor to store individual key-press times that make up a pattern, eventually storing the times for all ten digits (zero through nine). It would then be trivial for the impostor to defeat a typing biometric keypad by executing a “replay attack” in which the digit patterns stored earlier would be reused or replayed [21] as if they were being typed by an authentic user — even for a new PIN combination. Fortunately, evidence that patterns change with sequence means that more choices are available.

Table 6  
Comparison of subject performance across the two PINs.

<table><tr><td>Accuracy</td><td>PIN 1234</td><td>PIN 1324</td><td>Significant difference?</td></tr><tr><td>FAR</td><td>0.70</td><td>0.59</td><td>Yes, t = 3.13 p = 0.0018 n = 1198</td></tr><tr><td>FRR</td><td>6.22</td><td>4.50</td><td>Yes t = 4.82 p &lt; 0.001 n = 1198</td></tr></table>

The fourth and <sup>fi</sup>fth hypotheses are related. The testing of H4 showed fewer correlations between the typing patterns of PIN 2 compared to those of PIN 1. The testing of H5 showed that PIN 2 has higher authentication accuracy than PIN 1. The higher accuracy of PIN 2 can be attributed to having fewer correlations, as predicted by H4. Testing of H5 also demonstrated that such correlations can impact overall systems behavior, which in this case was a desirable increase in authentication accuracy. The <sup>fi</sup>rst three digits of PIN 1 are in sequential order, and movement from one key to the next is in a straight line. Therefore, it is expected that these keys will be learnt together faster and have a steeper learning curve, which will lead to higher covariance and hence poorer accuracy.

Overall, this research study has several major implications for designers of behavioral biometrics such as typing patterns. This study has shown that typing biometric keypads can be used for differentiating authentic users from impostors. Use of typing biometric keypads can also be extended to other applications. Section 1 provided examples which show the value of mining behavioral patterns in the detection and prevention of fraud, organized crime, and system intrusions. However, many other behavioral patterns can be mined to solve problems in areas such as security, identi<sup>fi</sup>cation, and target marketing. The reader is referred to a survey and classi<sup>fi</sup>cation of different behavioral biometric solutions [29]. Thus, the mining of behavioral patterns is a large <sup>fi</sup>eld with numerous possible applications that can be based on user skills, interaction styles, and preferences.

The results also suggest that some PINs are more accurate than others. Users should be encouraged to choose such PINs. For example, a user may be asked to suggest three possible PIN combinations and then tested on each of them. The one with fewer correlations is then suggested as the better PIN. The user may also be encouraged to select PINs with keys which are far apart from each other, and require diagonal movements across the keypad. This should result in a PIN with fewer key correlations, and hence more accuracy.

Furthermore, the results of the study provide a way of hardening PINs without increasing their length. This <sup>fi</sup>nding provides a potential way of breaking (or at least reducing) the password dilemma in which memorable passwords are the most easy to guess or crack using brute force methods. In addition, the fact that different PINs may be memorable to one individual and not to others may greatly help in separating his or her patterns from those of the general population. For example, an individual may easily remember a PIN because it is a family member's birth date, which is not so obvious to the general population. This will improve the authentication accuracy as the typing patterns between the given individual and the general population will be far apart, reducing the chance for errors (that is, FAR and FRR).

## 7. limitations and future research

By nature, empirical studies focus on speci<sup>fi</sup>c problems. They test a few variables while keeping all other parameters constant. This study used twenty-four subjects, which limited the number of PIN combinations that could be realistically compared while obtaining results that could be statistically tested for signi<sup>fi</sup>cance. Future experiments should look at comparing more pins of different sizes, different PIN digit layouts and combinations, and perhaps testing alphanumeric passwords as well. Furthermore, there may be more variation in results if different subject populations are used, especially those more general than the undergraduate students used in this study.

There are other aspects of typing behavior that are not addressed by this study. For example; user typing speed, typing pressure, stress, illness, the height and size of keys, and the external environment (e.g., temperature) or context can all potentially affect the ability to effectively classify patterns. There is also need to extend the research into other behavioral patterns to investigate the effect of learning. These <sup>fi</sup>nal thoughts and observations provide many avenues for future work based on the <sup>fi</sup>ndings of this study.

## References

[1] D. Asonov, R. Agrawal, Keyboard acoustic emanations, 2004 IEEE Symposium on Security and Privacy, IEEE Computer Society, Berkeley, CA, USA, 2004.

[2] W.L. Bryan, N. Harter, Studies in telegraphic language: the acquisition of a hierarchy of habits, Psychological Review 6 (1899).

[3] W. Conover, Practical Nonparametric Statistics, 3rd ed. John Wiley, New York, 1999.

[4] D. Denning, An intrusion-detection model, IEEE Software Engineering 13 (2) (1987).

[5] R. Duda, P. Hart, D. Stork, Pattern Classi<sup>fi</sup>cation, John Wiley & Sons, Inc., New York, 2000.

[6] T. Fawcett, F. Provost, Adaptive fraud detection, Data Mining and Knowledge Discovery 1 (3) (1997).

[7] U. Galassi, A. Giordana, M. Mendola, Learning user pro<sup>fi</sup>le from traces, 2005 IEEE/ IPSJ International Symposium on Applications and the Internet Workshops, IEEE Computer Society, Trento, Italy, 2005.

[8] D. Gentner, Why nouns are learned before verbs: linguistic relativity versus natural partitioning, in: Kuczaj (Ed.), Language Development, Earlbaum, Hillsdale, NJ, 1982.

[9] G.V. Graeventiz, Biometrics in access control, A&S International Automation & Security 50 (2003).

[10] Identity Theft Resource Center, ITRC Breach Report2008 [cited Access (2008) August, 26th]; Available from: http://idtheftmostwanted.org/ITRC%20Breach% 20Report%202007.pdf 2007.

[11] A. Jain, S. Prabhakar, L. Hong, A. Ross, et al., Biometrics: a grand challenge, International Conference on Pattern Recognition. Cambridge, UK, 2004.

[12] R. Joyce, G. Gupta, Identity authentication based on keystroke latencies, Communications of the ACM 33 (2) (1990).

[13] K. Kotani, K. Horii, Evaluation on a keystroke authentication system by keying force incorporated with temporal characteristics of keystroke dynamics, Behaviour & Information Technology 24 (4) (2005).

[14] I.S. MacKenzie, W.A.S. Buxton, Extending Fitts' law to two-dimensional tasks, ACM CHI 1992 Conference on Human Factors in Computing Systems. Monterey, California, 1992.

[15] F. Monrose, A. Rubin, Keystroke dynamics as a biometric for authentication Future Generation Computer Systems 16 (4) (2000)

[16] National Instruments Corporation, LabVIEW, 2005 Austin, Texas.

[17] B. Ngugi, Electronic capture and analysis of fraudulent behavioral patterns: an application to identity fraud, Information Systems Department, New Jersey Institute of Technology, Newark, NJ, 2005.

[18] M. Obaidat, B. Sadoun, Veri<sup>fi</sup>cation of computer users, using keystrokes dynamic, IEEE Transaction on Systems, Man and Cybernetics Part B 27 (1997).

[19] A. Peacock, X. Ke, M. Wilkerson, Identifying users from their typing patterns, in: L.F. Cranor, S. Gar<sup>fi</sup>nkel (Eds.), Security and Usability: Designing Secure Systems that People can use O'Reilly Media Inc. Sebastopol CA USA 2005

[20] D. Polemi, Biometric techniques: review and evaluation of biometric techniques for identification and authentication — final report, and editors, Institute of Communication and Computer Systems, National Technical University of Athens, 1995.

[21] P. Reid, Biometrics for Network Security, Prentice Hall, Upper Saddle River, NJ, 2004.

[22] L.H. Shaffer, Timing in the Motor Programming of Typing, Quarterly Journal of Experimental Psychology 30 (1978)

[23] Sheppard Software, World trivia games2009 [cited Access (2009) June 26th]; Available from:, http://www.sheppardsoftware.com/Geography.htm.

[24] C. Terzuolo, P. Viviani, Determinants and characteristics of motor patterns used for typing, Neuroscience 5 (1980).

[25] A. Trujillo-Ortiz, R. Hernandez-Walls, A. Castro-Perez, K. Barba-Rojo, MOUTLIER1: Detection of Outlier in Multivariate Samples Test. A MATLAB <sup>fi</sup>le, 2006.

[26] M. Whitman, H. Mattord, Principles of Information Security, 2nd ed. Course Technology, Boston, Massachusetts, USA, 2005.

[27] S.S. Wilks, Multivariate Statistical Outliers, Sankhya, Series A 25 (1963).

[28] J. Xu, H. Chen, Fighting organized crimes: using shortest-path algorithms to identify associations in criminal networks, Decision Support Systems 38 (3) (2003).

[29] R. Yampolskiy, V. Govindaraju, Behavioral biometrics: a survey and classi<sup>fi</sup>cation, International Journal of Biometrics 1 (1) (2008).

[30] E. Yu, S. Cho, Keystroke dynamics identity veri<sup>fi</sup>cation — its problems and practica solutions, Computers & Security 23 (5) (2004).

![](/api/attachments/GZD9F3E4/fulltext/images/a72a60d3376852d6c940ab517f3fac2a3401a6b298ec229d5be04886f4feabdf.jpg)

Dr. Benjamin Ngugi, is an Assistant Professor in the Information Systems and Operations Management at the Sawyer Business School, Suffolk University in Boston. He received his Ph.D. in Information Systems from New Jersey Institute of Technology and his degree in Electrical and Electronics Engineering from University of Nairobi, Kenya. He conducts his research in the areas of identity fraud biometrics, security compliance, e-Health security and technology adoption. He has published his research in journals including International Journal of Information Security and Privacy, and The CASE Journal.

![](/api/attachments/GZD9F3E4/fulltext/images/d5d7029d450b959603a802f713c4c9bf95032c4e230017ec4147946e89ef2b8e.jpg)

Dr. Marilyn Tremaine, is a Research Professor at the Center for Advanced Information Processing Research Institute at Rutgers University where she engages in research on multimodal interfaces, assistive and rehabilitative technology and scienti<sup>fi</sup>c visualization. She has been active in the ACM SIGCHI community, chairing 2 of its major conferences and 2 smaller ones plus serving as technical program chair to 2 other conferences. She has been vice president of communications and conference planning and president of SIGCHI. Dr. Tremaine has received a lifetime service award from ACM and two lifetime career awards from her <sup>fi</sup>eld.

![](/api/attachments/GZD9F3E4/fulltext/images/7dd47cfaea3c7d8895518176b908385a92a2b7400d2444cefd3ebc71645e2610.jpg)

Dr Peter Tarasewich is an Associate Professor of Information Systems and Operations Management at the Sawver Business School Suffolk University. He received his Ph.D. in Operations and Information Management from the University of Connecticut, his MBA (focusing on Management Information Systems) from the University of Pittsburgh, and dual degrees in Electrical Engineering and Computer Science from Duke University. Dr. Tarasewich's research interests include human computer interaction with mobile devices, text entry, information display, privacy/security of information, mobile commerce, ubiquitous computing, product design, aesthetics of information systems, and Web engineering, He has published his

research in journals including Communications of the ACM, International Journal of Human Computer Interaction, IEEE Transactions on Engineering Management, Communications of the AIS, Internet Research, Quarterly Journal of Electronic Commerce, Journal of Computer Information Systems, IIE Transactions, European Journal of Operations Research, International Journal of Production Management, International Journal of Production Economics, and Journal of Case Research, as well as in the proceedings of conferences such as CHI, AMCIS, and UbiComp. Dr. Tarasewich has served as a track chair for the annual Association of Information Systems' (AIS) Americas Conference on Information Systems (AMCIS) conference, and on the Program Committee for the annual AIS pre-ICIS (International Conference on Information Systems) HCI/MIS Workshop.
