---
otero_id: 8042
otero_key: "UWZHQUXC"
title: "Decision support for determining veracity via linguistic-based cues"
authors: "Christie M. Fuller; David P. Biros; Rick L. Wilson"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.11.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for determining veracity via linguistic-based cues

Christie M. Fuller <sup>a,</sup>⁎, David P. Biros <sup>b</sup>, Rick L. Wilson

<sup>a</sup> Management and Information Systems Department, Louisiana Tech University, P.O. Box 10318, Ruston, Louisiana 71270, United States

<sup>b</sup> Management Science and Information Systems Department, Oklahoma State University, Stillwater, Oklahoma, United States

## a r t i c l e i n f o

Article history: Received 26 September 2007 Received in revised form 28 October 2008 Accepted 5 November 2008 Available online 11 November 2008

Keywords: Deception Deception detection Credibility assessment Classi<sup>fi</sup>cation Linguistic-based cues Decision support systems Neural networks Decision trees Logistic regression

## a b s t r a c t

Deception detection is an essential skill in careers such as law enforcement and must be accomplished accurately. However, humans are not very competent at determining veracity without aid. This study examined automated text-based deception detection which attempts to overcome the shortcomings of previous credibility assessment methods. A real-world, high-stakes sample of statements was collected and analyzed. Several different sets of linguistic-based cues were used as inputs for classi<sup>fi</sup>cation models. Overall accuracy rates of up to 74% were achieved, suggesting that automated deception detection systems can be an invaluable tool for those who must assess the credibility of text.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Deception detection is a critical decision making activity, crucial in professions such as law enforcement, psychology, and human resources. Unfortunately, as Bond and DePaulo note, humans have not shown the ability to perform the task at a level much better than pure chance [3]. This has been con<sup>fi</sup>rmed for both untrained civilian workers as well as experienced government professionals.

A variety of methods are available to assist professionals with the task of deception detection, but few are relevant to text-based communications so prevalent today. Additionally, these approaches such as Computerized Voice Stress Analysis, Scienti<sup>fi</sup>c Content Analysis (SCAN), Content-Based Criteria Analysis (CBCA), Behavioral Analysis Interview and the polygraph test require extensive examiner training, may be invasive techniques, may work only with carefully structured interviews, have subjective results, rely heavily on the examiner's interpretation, or may not work in all situations [13,20,28,34,40,44,46].

Automated text-based deception detection has been suggested as an alternative that may overcome such shortcomings [44,51] and is especially timely and important given the dramatic increase in textbased communications (such as e-mail) and the fact that humans typically <sup>fi</sup>nd only one-third of text-based deceptions[21,25]. Further, automated text-based deception detection requires little user training, and the results are independent of the operator. Previous work using this approach has shown promise. However, this automated analysis has only been tested in contrived laboratory situations and/or very small real-world samples [44,51,52].

This study extends previous work in automated text-based deception detection in a number of important ways. First, a relatively large sample of real-world data from the military law enforcement domain is used as the data set, thus representing a rare opportunity to apply these deception detection techniques to “high-stakes, realworld” situations with a meaningful number of cases. Individuals involved in the cases face severe consequences such as incarceration, loss of career, and demotion in rank. Therefore, detection accuracy becomes crucial as false positives can be detrimental to those truly innocent. Second, by systematically developing potential decision support models to detect text-based deception, the study clari<sup>fi</sup>es and provides evidence for relative importance of the myriad of linguistic cues previously proposed in the literature in an attempt to build a more parsimonious framework for text-based deception detection. Third, by systematically evaluating multiple tools for classi<sup>fi</sup>cation, the study also provides insight into possible best practices in building DSS to aid those who must identify deceptive communications. Ultimately, this study provides important ground work for providing proof of concept in the ability to build decision support technologies that help determine statement veracity in minimal time and with minimal operator expertise and resources for the important problem of textbased deception detection.

## 2. Background

## 2.1. Deception detection

Methods of deception detection have existed for thousands of years. Interestingly, humans have not proven to be very capable at this task. A synthesis of over 23,000 subjects showed that human performance at lie detection is approximately 54% [3]. In their work, Ekman and O'sullivan [14] found just 15 out of 13,000 people, or about 0.12%, capable of detecting deception with 80% accuracy.

Previous studies have shown that professional lie catchers such as police of<sup>fi</sup>cers or customs of<sup>fi</sup>cers (excluding secret service agents and psychiatrists with an interest in deception) are generally not better than college students or the general public at detecting deception. A summary of eight such studies showed overall accuracy levels of these professionals (total correct in detecting truthful and deceptive messages) ranging from 49 to 64% [46]. However, these results showed that the accuracy rates were in<sup>fl</sup>ated by the 70–80% correct rate of detecting truthful statements (versus a 35–40% rate of detecting lies) [16]. A recent study also showed a signi<sup>fi</sup>cantly higher ability of participants to accurately identify truthful than deceptive behavior [54], though neither type of communication was identi<sup>fi</sup>ed with more than 60% accuracy. This re<sup>fl</sup>ects the so-called ‘truth bias’ or the notion that people are more apt to judge communications as truthful (and, relatedly, that they are not good at deception detection) [46].

Given this inability of humans to successfully detect deception, a clear need exists for improved tools to assist in these credibility determinations. Improved methods of deception detection are particularly important to those who must detect lies in the usual course of their work, such as security personnel, human resource managers, among others. Numerous methods have been developed to assist with this task. This includes methods for detecting deception in nonverbal, paraverbal, and verbal environments. These methods, and the shortcomings associated with each, are listed in Table 1.

The focus of this study is on detecting deception in verbal communication, speci<sup>fi</sup>cally text-based communication. Analyzing linguistic cues shows promise because 1) a very large amount of communication is already in text format (i.e. email, text chat, letters, reports, etc.), 2) it is unobtrusive and the communicator may not even be aware that a veracity analysis is taking place, and 3) it is very cost effective and does not require expensive equipment or specially trained operators. While the sample used in this paper is written text produced as part of the investigation of crimes, the technique is potentially applicable to other forms of text, such as email, web pages, or blogs. It could also be used with transcribed text of oral communications. While the technique presented here is not the only technique for analyzing the veracity of text, the fact that it is an automated process may lend itself to more readily analyze large data sets.

## 2.2. Deception detection in verbal communication

There are methods that have been implemented to study deception in verbal communications, of which text-based communication is one type. These methods include Automated Text-Based Deception Detection, Scienti<sup>fi</sup>c Content Analysis, Statement Validity Analysis, and the Behavioral Analysis Interview.

## 2.2.1. Automated-text based deception detection

Linguistic analysis tools have been introduced as a possible aid in deception detection [51]. To date, about 30 text-based cues to deception have been implemented in automated analysis tools. Good candidates for automated analysis are objectively measured cues and those that can be de<sup>fi</sup>ned independent of text content [51]. There are two primary research streams studying deception using such linguistic cues.

One such research stream uses a tool called Agent 99 Analyzer (A99A), a component of a larger suite of automated deception detection tools known as Agent 99 [9,53]. The A99A research stream developed a framework for studying text based-deception using the following linguistic categories: quantity, complexity, uncertainty, nonimmediacy, expressivity, diversity, informality, speci<sup>fi</sup>city, and affect. Cues in these categories were then used to classify messages as truthful or deceptive. Using a sample of 94 messages of student subjects communicating about the well-known but <sup>fi</sup>ctitious desert survival problem, overall test set classi<sup>fi</sup>cation accuracy (using standard ten-fold cross validation) ranged from 57.4% when using a decision tree as the classi<sup>fi</sup>cation tool, to 80.2% when utilizing arti<sup>fi</sup>cial neural network tools [52]. Another study, using only 18 real-world messages, achieved classi<sup>fi</sup>cation accuracy of 72% [43].

The other major stream of research in this area relies on the Linguistic Inquiry and Word Count (LIWC) tool to quantify cues to deception. Newman et al. [36] proposed that the language dimensions of self-references, negative emotions, and cognitive complexity that are part of LIWC could be associated with deception. The use of motion and exclusive words were proposed as indicators of cognitive complexity. Third person pronouns were also found to be predictors of deception. Using logistic regression, truthful and deceptive text samples were classi<sup>fi</sup>ed with 61% accuracy. Based on the work of Newman et al. [36], Bond and Lee [4] used LIWC to code the statements of prisoners. This study achieved an accuracy of 69.1% using logistic regression with the variables of Newman et al. In addition to the categories studied by Newman et al., Bond and Lee also used LIWC to code Reality Monitoring (RM) Terms. Using logistic regression, they had an overall accuracy rate of 71.1% using the RM cues available in LIWC as inputs to the model. Hancock and colleagues [23] have also examined the use of automated linguistic analysis in deception, though these studies did not incorporate classi<sup>fi</sup>cation models [24].

These studies using A99A and LIWC have implemented a number of different linguistic cues, yet there has not been a thorough analysis of relative cue importance in detecting deception, nor has there been systematic study regarding the ability of such cues to generalize across multiple domains. Additionally, there remains no consensus as to which stream of research (A99A, LIWC) may result in superior performance, though an exploratory study logically suggested that combining the best features of the two may be advantageous [19]. While this is not the only method of detecting deception in text, it is the only known method designed speci<sup>fi</sup>cally to do this task automatically and with minimal user training.

Cue classes and related deception detection methods

<table><tr><td>Cue class</td><td>Applicable methods</td><td>Drawbacks of methods</td></tr><tr><td>Nonverbal</td><td>Polygraph</td><td>Invasive, specialized equipment required, extensive training required, subjective results, requires structured interview</td></tr><tr><td>Paraverbal</td><td>Voice stress analysis</td><td>Inaccurate, subjective results</td></tr><tr><td rowspan="3">Verbal content</td><td>Scientific content analysis</td><td>Extensive training required, subjective results</td></tr><tr><td>Content based criteria analysis</td><td>Extensive training required, subjective results, not appropriate for use with suspect statements, requires structured interview</td></tr><tr><td>Automated text-based deception detection</td><td>New, not previously tested with real-world data</td></tr><tr><td>Mixed</td><td>Behavioral analysis interview</td><td>Extensive training required, subjective results, inaccurate, requires structured interview</td></tr></table>

2.2.2. Additional methods of detecting deception in verbal communication The following paragraphs identify some of the other methods that have been proposed for use in detecting deception in verbal communications.

Scienti<sup>fi</sup>c Content Analysis (SCAN) is a statement analysis procedure developed for use in criminal investigations that was created by Avinoam Sapir, a former Israeli police lieutenant, based on years of experience interrogating subjects[34,38]. The technique's accuracy has been compared to that of the polygraph, though speci<sup>fi</sup>c accuracy rates have not been reported [13]. It has been noted that the technique may not work when the subject is discussing multiple issues [13].

Statement validity analysis (SVA) is a technique for analyzing the verbal content of statements. It is made up of three components, one of which is Content Based Criteria Analysis (CBCA). CBCA, the SVA component which has received the most study, involves analyzing a statement according to 19 criteria. [45]. The criteria include items such as the inclusion of unusual or super<sup>fl</sup>uous details, which are not amenable to automated analysis. The results of past studies have shown that the technique's accuracy may vary widely, with reported accuracy ranging from 55 to 90% [46]. It has been suggested that due to its design, CBCA may not be appropriate for use with suspect statements [47], limiting its usefulness to security personnel.

The Behavioral Analysis Interview (BAI) is a method of deception detection that relies on observing suspect verbal and nonverbal behavior during a structured interview [28]. In one study utilizing this technique, four judges trained in using the technique reviewed 60 tapes of actual suspects that were interviewed using BAI. These judges were 86% accurate overall in identifying truthful and deceptive subjects, though this accuracy was achieved by eliminating any evaluations where the rater judged the behavior to be inconclusive, which occurred about 15.5% of the time. Overall, raters correctly identi<sup>fi</sup>ed truthful suspects with 78% accuracy and deceptive statements with 66% accuracy. A more recent study showed found that suspects' behavior in BAI interviews was not consistent with the types of behaviors predicted by the technique. The updated study did not assess the ability of rater's to distinguish between truthful and deceptive suspects [49]. Like CBCA and SCAN, this technique relies on a trained rater's assessments of various criteria.

## 2.3. Nonverbal and paraverbal detection deception

While the focus of this study is deception detection in text, it is worth mentioning other prevalent methods of deception detection for comparison purposes. Use of the polygraph is arguably the most wellknown lie detection method. The device measures changes in pulse, heart rate, blood pressure, respiratory rate, and galvanic skin response [17] and an examiner makes a veracity determination based on changes in these nonverbal cues during the course of an interview [46]. Estimates of polygraph accuracy in <sup>fi</sup>eld studies range from 72 to 92% [27,39,41]. Despite its use and accuracy, the polygraph is not without drawbacks. The results of the polygraph examination depend to an extent on the skill of the examiner [46]. Further, a trained examiner and the appropriate equipment must be present for the test to be used. Others have noted that the test is somewhat intrusive in that the subject must be connected to the machine [44].

The voice stress analyzer was introduced in the 1970s and touted as a possible replacement of the polygraph [40]. The voice stress analyzer measures changes in the speech signal in response to stress, putting it in the category of paraverbal deception detection methods. Like the polygraph, the results are heavily dependent on the skill of the operator when used as lie detectors. Despite its initial promise, the voice stress analyzer has failed to gain scienti<sup>fi</sup>c acceptance and a recent study showed that the voice stress analyzer did not show “any sensitivity to the presence of deception or stress.” [26] Like several of the verbal techniques, the polygraph and voice stress analyzer rely on trained users

## 2.4. Summary

In conclusion, with the exception of the aforementioned study with sample size of 18 [42], automated text-based deception detection has not been implemented in a so-called high-stakes, real-world domain. Additionally, automated text-based deception detection has the potential to accurately determine veracity using minimal resources.

Most deception detection studies have been conducted in experimental settings using student subjects [12,48], and thus a clear need exists for research using serious, or high-stakes, lies [12,18,33]. Also, given the two somewhat disparate linguistic cue set research streams, an attempt to build a more parsimonious approach could lead to more effective decision support system development of automated deception detection systems. Additionally, it is also important to explore various traditional classi<sup>fi</sup>cation tools as the underlying technology for the automated tool. Past results have suggested that the tool choice may impact performance [2], so a comparison of different tools is warranted. Finally, given the ‘high-stakes’ nature of deception detection, it is important to note decision support performance on additional metrics beyond just overall case accuracy. For instance, the accuracy of detecting lies will measure system ability to overcome the aforementioned ‘truth bias’. Similarly, given the high potential cost of a ‘false positive’, these results (percentage of truthful statements classi<sup>fi</sup>ed as lies) also need to be reported. The next section outlines the present research study designed to explore these important issues.

## 3. Methods

## 3.1. Data sample

A challenge of studying text-based deception is locating real-world data that can be accurately labeled as truthful or deceptive (i.e. establishing ‘ground truth’). Perhaps this is why past researchers have relied on laboratory created data. For this study, access to sets of “person of interest statements”, of<sup>fi</sup>cially known as a Form 1168, was provided from law enforcement personnel at participating military bases. Person of interest statements are of<sup>fi</sup>cial reports written by a subject or witness in an of<sup>fi</sup>cial investigation.

When recording a statement from a person of interest, investigators typically have the person come into the of<sup>fi</sup>ce where they are given the option to write a statement or type one into a computer. Statements are all recorded on the same of<sup>fi</sup>cial form (Form 1168) and are written in the presence of law enforcement personnel. If a person is a suspect, he or she is read both the Miranda rights and Article 32 of the Uniform Code Military Justice (UCMJ) prior to making a statement. Later, base law enforcement personnel then investigate the veracity of the statements about the incident. Negative consequences result in two ways. First, if the person-of-interest really did commit the offense and lied about it, she would receive very little leniency by her commander (in the case of non-judicial punishment) or a military court. Second, person-of-interest statements are “of<sup>fi</sup>cial statements” and creating a false of<sup>fi</sup>cial statement is punishable by court martial under the UCMJ. Thus, if a person-of-interest creates a false statement, he could be facing a second serious charge.

In the study, criteria were established to classify the statements as either truthful or deceptive (see Table 2). Law enforcement personnel on the bases used the criteria to label the statements as truthful or deceptive before delivering the statements to the researchers. Statements that base personnel could not conclusively be established as truthful or deceptive were not included in the sample. The statements described many different situations. For example, in a deceptive statement, the author might say that he or she did not purposefully leave a store with unpaid merchandise, though a security camera shows surreptitious behavior by the subject along with the subject deliberately concealing the merchandise.

Table 2  
Criteria for determining statement veracity

<table><tr><td>Statement type</td><td>Criteria</td></tr><tr><td>Deceptive statements</td><td>1. The subject later recanted the statement and recorded another statement, but was not charged with making a false official statement2. The subject was charged with making a false official statement3. Other evidence in the case showed that the statement could not be true4. An impartial witness, such as security force personnel, gave a statement substantially contradicting the subject&#x27;s statement</td></tr><tr><td>Truthful statements</td><td>1. Evidence in the case or result of the case corroborated the statement2. Statement is given by law enforcement personnel witnessing the incident. Law enforcement personnel are assumed to be impartial witnesses who would make every attempt to give reliable accounts</td></tr></table>

At the end of the data collection process, a total of 366 written, codeable statements were obtained from the participating military bases that were utilized in the subsequent analysis. More were collected, as some were not usable for inclusion in the study. Though suspects and witnesses have the option of typing a statement, most are written. Twenty-one typed statements were received, all classi<sup>fi</sup>ed as truthful. In order to try to avoid adding a potential confound to the study, these typed statements were dropped from the analysis. Additionally, two statements were received that were written on behalf of another person. They were eliminated from the analysis due to the importance of capturing the actual words used by the author. Finally, when extracting cues from statements as described in the next section, <sup>fi</sup>ve statements were excluded from further analysis due to length (too long or too brief). The 366 cases consisted of 79 deceptive statements and 287 truthful statements. According to law enforcement estimates, this distribution is representative of the approximate proportions in which truthful and deceptive statements actually occur (M. Bronin, personal communication, May, 31, 2007).

The original written statements were transcribed for text processing using standardized protocols developed by the research team. These procedures were quite detailed to ensure consistent and full statement transcription. As an example, information that might identify a person was blacked out by law enforcement. This information had to be replaced in a consistent manner so that the adjacent text could still be utilized. The fully transcribed statements were then entered into the message feature mining process described below.

## 3.2. Message feature mining

One of the goals of the study is to synthesize past research and build a decision support system to identify deceptive messages using linguistic-based cues. Message Feature Mining [1], outlined in Table 3, is a term previously used that describes the process followed in this study. Each statement was <sup>fi</sup>rst passed through the feature extraction phase. This entailed processing the text through appropriate programs in order to identify and quantify the levels of the linguistic cues present in the statements.

To extract cues from the statements, the combination of GATE and LIWC were used. In A99A, General Architecture for Text Engineering (GATE) [10,11] has been successfully employed in past studies, and LIWC was used to extract cues not covered by GATE. GATE and LIWC produce a value for each cue within each statement, so there were no missing values in the data set. Prior to classi<sup>fi</sup>cation, the values for each cue were transformed so that the range of values was from zero to one.

The manner in which the 366 cases were used in building classi-<sup>fi</sup>cations models is an important consideration in this study. There are a number of somewhat con<sup>fl</sup>icting criteria that must be considered in partitioning the data to be analyzed. First, the issue of creating training and testing sets, or hold out samples, is relevant. Data must be systematically partitioned in order to insure accurate results in terms of classi<sup>fi</sup>cation accuracy. In other words, the reported results must not be a function of how hold out samples are created. Second, a consideration must be given to attempt to obtain a more ‘balanced’ data set since the class of enhanced interest (deceptive statements) is in the minority [40]. Not considering some balancing of the datasets would most likely introduce a truth-bias into the techniques because of the disproportionate amount of truthful statements. Finally, given the dif<sup>fi</sup>culty in obtaining a large sample in a high-stakes situation, it is important to try to utilize all the available data in analysis.

To consider all of these criteria, the follow data sample partitioning process was used. Four different data sets were created using the 366 cases, due primarily to the approximate 1:4 ratio of deceptive to truthful statements. The truthful statements were randomly split into 4 equal partitions (72 cases, 71 in one of the partitions). They were each matched with the entire 79 deceptive cases to create the four datasets of 151 (or 150) cases each. This partitioning allowed all the statements to be utilized in the analysis. Additionally, using the average performance of the classi<sup>fi</sup>ers over the 4 partitions ensures that results are independent of the balanced set creation process. Finally, providing a classi<sup>fi</sup>er with a more balanced sample [2], will likely yield a better opportunity to ‘learn’ truthful and deceptive examples equally well. The fact that due to the proportional composition of the data set the resulting partitions have a few more deceptive than truthful statements does not impact the satisfaction of these desired characteristics of the analysis. For instance, this small difference is taken into account when assessing classi<sup>fi</sup>cation accuracy better than chance results later in the Results section.

The second portion of Message Feature Mining was to generate a classi<sup>fi</sup>cation model based upon the speci<sup>fi</sup>c combination of cue set and classi<sup>fi</sup>cation technique (see below for more detail) utilized for truthful/deceptive classi<sup>fi</sup>cation. Finally, after the classi<sup>fi</sup>cation models were developed, appropriate methods were used to determine the most important cues, or those which have the most in<sup>fl</sup>uence in classifying truthful and deceptive statements.

Several variable sets were used to develop alternate classi<sup>fi</sup>cation models in order to investigate ef<sup>fi</sup>cacy of the different linguistic cues discussed previously. Additionally, various classi<sup>fi</sup>cation models were also constructed using each of the four partitioned data sets and the different sets of cue inputs discussed below in response to the variability of technique performance from past studies.

## 3.3. Cue sets

The previous study using A99A included 22 linguistic based cues as classi<sup>fi</sup>cation inputs [52]. This is, to date, the largest cue set used for building classi<sup>fi</sup>cation models for deception detection. However, results showed that accuracy improved when the original set of 22 variables was reduced. Variables identi<sup>fi</sup>ed as important in classifying messages for at least 2 of 4 techniques used in the A99A study were

## Table 3

Message feature mining process

<table><tr><td>Message feature mining process</td></tr><tr><td>1. Select desired features or cues</td></tr><tr><td>2. Identify and quantify features in text using text processing tools</td></tr><tr><td>3. Select types of classification models to be built</td></tr><tr><td>4. Train and test models</td></tr><tr><td>5. Evaluate model performance</td></tr><tr><td>6. Identify important features</td></tr></table>

identi<sup>fi</sup>ed. These 14 variables (see Table 4) form the <sup>fi</sup>rst of the four cue sets used in this study, heretofore referred to as the Zhou/Burgoon cues. The Zhou/Burgoon cues showed reasonable accuracy previously in a non real-world domain, and will serve as an informal benchmark for the current work.

Developing theoretically based deception detection methods is important to the science of deception detection and motivated the selection of the second set of variables [37]. A set of deception constructs drawn from deception theories of Interpersonal Deception Theory, Interpersonal Manipulation Theory, Reality Monitoring, Four-Factor Theory, and the Self-Presentational Perspective [6,7,12,29, 35,55,56] was created. Then, Con<sup>fi</sup>rmatory Factor Analysis was used to validate this set of deception constructs (shown in Table 5). This represents a re<sup>fi</sup>nement of an earlier framework developed by Zhou, Burgoon and colleagues [8,51,52]. The use of this second, construct related cue set will measure the ef<sup>fi</sup>cacy of the theoretically determined variable set.

A third data set, termed the comprehensive cue set, was also used in the study. This set was an amalgamation of the <sup>fi</sup>rst two cue sets, incorporating the A99A studies, the validated framework cues, and previous studies implementing LIWC. This included a total of 31 cues. This cue set will facilitate simultaneously investigating the impact of the different cue subsets.

Finally, a feature selection procedure was used to develop the fourth cue set. The feature selection was applied to the comprehensive cue set to reduce the number of cues. When the number of variables is large relative to data set size in classi<sup>fi</sup>cation problems, there is risk of ‘over<sup>fi</sup>tting’ the data which could result in poor generalization [29]. Of the 120 studies investigated and reported by DePaulo et al [12], the largest sample size reported was 192. It is likely that real-world samples in deception studies will continue to be of comparable or smaller size due to the dif<sup>fi</sup>culty of establishing “ground truth” and other practical matters. Past studies in automated deception detection have also shown that results might be improved by reducing variable set size [52], likely due to correlation among variables and the risk of over<sup>fi</sup>tting the classi<sup>fi</sup>cation techniques.

Table 4 Cue sets

<table><tr><td>Cues</td><td>Zhou/Burgoon important Cues</td><td>Comprehensive cue set</td><td>Text-based deception construct cues</td><td>Feature selection cues</td></tr><tr><td>1st person plural pronouns</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>1st person singular pronouns</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>2nd person pronouns</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>3rd person pronouns</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Activation</td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>Average sentence length</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Average word length</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Bilogarithmic type-token ratio</td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>Causation terms</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Certainty terms</td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>Cognitive processing terms</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Content word diversity</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Emotiveness</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Exclusive terms</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Generalizing terms</td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>Imagery</td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>Lexical diversity</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Modal verbs</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Modifiers</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Motion terms</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Passive verbs</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Pausality</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Pleasantness</td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>Redundancy</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Sensory ratio</td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>Sentence quantity</td><td></td><td>X</td><td>X</td><td>X</td></tr><tr><td>Spatial ratio</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Temporal ratio</td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>Tentative terms</td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>Verb quantity</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Word quantity</td><td></td><td>X</td><td>X</td><td>X</td></tr></table>

Table 5  
Validated text-based deception framework

<table><tr><td>Construct</td><td>Brief description</td><td>Indicator</td></tr><tr><td>Quantity</td><td>Length of message</td><td>Word quantity, verb quantity, sentence quantity</td></tr><tr><td>Specificity</td><td>Amount and type of details in the message</td><td>Sensory ratio, temporal ratio, bilogarithmic type-token ratio</td></tr><tr><td>Affect</td><td>Emotions present in the message</td><td>Activation, imagery, pleasantness</td></tr><tr><td>Uncertainty</td><td>Relevance, directness, and certainty of message</td><td>Certainty terms, generalizing terms, Tentative terms</td></tr></table>

Sentence Quantity, Verb Quantity, Activation, Imagery, and Pleasantness were extracted using A99A. The remaining cues were extracted using LIWC.

This feature selection procedure utilized a simple F-statistic to determine relationship strength between cues and the dependent variable. Variables were then ranked on this measure, and the eight most important cues were retained to form the fourth cue set. The somewhat arbitrary cutoff of 8 variables was based upon speci<sup>fi</sup>c tool heuristics for neural networks that have previously been suggested [29]. The four cue sets are summarized in Table 4.

## 3.4. Classification

In considering the creation of an automated decision support tool for deception detection, three common classi<sup>fi</sup>cation methods were utilized; arti<sup>fi</sup>cial neural networks, decision trees, and logistic regression.

## 3.4.1. Artificial neural networks

An arti<sup>fi</sup>cial neural network is a system of connected units, or nodes, arranged in layers. Typically, an arti<sup>fi</sup>cial neural network has an input layer, a hidden layer, and an output layer. The nodes in the hidden layer combine the inputs from the previous layer into a single output value which is passed on to the next layer. Associated with each unit in the network is a weight. The weights in the network are determined by training the network on a portion of the data. The network performance is then tested on the remaining data, or holdout sample [2].

There are many different neural network architectures that could be used to analyze the data. This study utilizes perhaps the simplest method, but most common feedforward multilayer perceptron using backpropagation as the training approach [32]. A single hidden layer of three nodes was used in this study. The size of the input layer corresponded to the number of cues in each of the four cue sets. In the output layer, if the predicted value is less than 0.5, the record is predicted as false, while the record is <sup>fl</sup>agged as true if the predicted value is greater than or equal to 0.5.

Given the plethora of different types of neural networks, and even the innumerable parameters that are associated with feedforward neural networks, the results of this paper represent in essence a lower bound of potential classi<sup>fi</sup>cation accuracy. To be ‘fair’ to the other techniques, the study uses a more generic approach that likely could be improved with experimentation. It is possible if the models become too <sup>fi</sup>ne-tuned, it may limit their generalization [32]. But that is beyond the scope of the research at this time. The same statement could of course be made about decision tree techniques as well.

Though arti<sup>fi</sup>cial neural networks have been shown to be powerful classi<sup>fi</sup>ers whose performance may exceed other classi<sup>fi</sup>ers, in terms of accuracy, arti<sup>fi</sup>cial neural networks are widely considered to be ‘black boxes’ that do not readily give an explanation as to precisely how the classi<sup>fi</sup>cation decisions are made. For arti<sup>fi</sup>cial neural networks, a form of sensitivity analysis [15] may be used to calculate variable importance. In sensitivity analysis, the values of each input are systematically varied for each record in the testing data set in order to determine the effect of such changes on the output. Similar procedures have been applied to automated deception detection using linguistic analysis in the past [52].

## 3.4.2. Decision trees

Decision trees classify cases by dividing a set of records into successively smaller sets by applying a set of decision rules. There are a variety of criteria used to determine how to split the record set and an even larger set of algorithms possible. For this study, C5.0 was the speci<sup>fi</sup>c decision tree algorithm employed, using the maximum information gain criteria This algorithm builds a tree, then prunes it to produce a more generalizable tree [2]. The result of the decision tree algorithm is the classi<sup>fi</sup>cation of all cases as either truthful or deceptive and a set of if-then rules that can be used to explain how these classi<sup>fi</sup>cations were made and thus, determining variable importance.

As noted above with neural networks, the classi<sup>fi</sup>cation performance of the decision trees in this study represents a lower bound on potential performance. There are many different parameters and algorithms that can be utilized in building decision trees, but this study opted for a more generic approach realizing that further experimentation (outside the scope of this paper) may lead to increased classi<sup>fi</sup>cation accuracy.

## 3.4.3. Logistic regression

Logistic regression is a statistical technique appropriate for use with continuous independent variables and a binary dependent variable, and is typically thought to be superior to traditional discriminant analysis due to relaxed assumptions. Logistic regression does not predict the value of a variable, but predicts the probability of an event occurring. This value will range between zero and one. Similar to the neural network, a cut-off value between zero and one, 0.5 by default, is used to determine classi<sup>fi</sup>cation. In logistic regression, the Wald statistic can be used to assess signi<sup>fi</sup>cance of individual cues [22]. Here, the stepwise method was used to enter variables into the model. Using this method, cues are entered one at a time into the model. Each time a variable is entered, the signi<sup>fi</sup>cance of each cue in the model is evaluated. Any cue that is not signi<sup>fi</sup>cant at that step is eliminated. Further, standardized coef<sup>fi</sup>cients give an indication of variable importance.

SPSS Clementine was used for all classi<sup>fi</sup>cation algorithms and default parameters were used in each case to ensure consistent comparisons across the different techniques. As is standard when developing classi<sup>fi</sup>cation models, ten-fold cross validation was implemented on each of the four data sets. Each data set was <sup>fi</sup>rst partitioned into ten equal sections. Nine sections were used for training the appropriate model and the remaining section was used for testing the model. This process was repeated ten times, so that each of the ten sections of the data set was used once as the testing set. The partitions were strati<sup>fi</sup>ed so that the observations were split approximately equally between the two possible outputs, truthful and deceptive within each partition. Truthful and deceptive statements were randomly assigned to each of the ten partitions. Cross validation provides better estimations of the true error rate of the classi<sup>fi</sup>cation model than a single train-and-test experiment [50].The results of the ten experiments for the four data sets were aggregated to estimate the overall accuracy of each classi<sup>fi</sup>cation model.

Fundamental to the study is assessing classi<sup>fi</sup>cation accuracy of the cue/technique combinations. Overall accuracy assesses the proportion of statements, both truthful and deceptive, that are correctly classi<sup>fi</sup>ed. Sensitivity (percent accuracy of deceptive statements) and speci<sup>fi</sup>city (percent accuracy of truthful statements) will also be reported, as will the compliment of speci<sup>fi</sup>city, the false positive rate [5]. All of these measures will describe the different trade-offs (truth bias vs. penalty of calling a truthful person a liar) found in the various cue/technique combinations.

## 4. Results

## 4.1. Overall MANOVA results

MANOVA was used to assess any signi<sup>fi</sup>cant differences due to cue set, classi<sup>fi</sup>cation model, or interaction of factors using the various dependent measures, testing set accuracy, and the other speci<sup>fi</sup>c class accuracy rates. At the multivariate level, the overall model was signi<sup>fi</sup>cant. There was a signi<sup>fi</sup>cant main effect for cue set for sensitivity. Post hoc contrasts showed that the Construct cue set was better than the Feature Selection cue set, which was better than the Zhou/Burgoon dataset and the Comprehensive set. For the remaining measures, there were no signi<sup>fi</sup>cant main or interaction effects.

Table 6 summarizes the performance measures — overall test set accuracy, sensitivity, speci<sup>fi</sup>city and false positives. The average classi<sup>fi</sup>cation accuracy and standard deviations are shown across all different combinations of cue sets and models (classi<sup>fi</sup>cation techniques).

## 4.2. Overall testing result

From a statistical signi<sup>fi</sup>cance standpoint, the results did not signi<sup>fi</sup>cantly differ across the combinations of models and cue sets. This is due in part to the high variability found across the different partitions of the data set, which is the reason why the research study took great caution in designing the experimentation. Nonetheless, given the possible impacts of an incorrect decision in a high-stakes domain, there are some practical differences and some overall observations that the results provide. According to Press's Q statistic, the testing accuracy results were signi<sup>fi</sup>cantly better than what would be expected by chance, given the proportion of truthful and deceptive statements in the sample for all model and cue set combinations. Additionally, the maximum chance criterion shows that an accuracy of approximately 52% could be expected by chance, while our minimum testing set accuracy was about 67% for the Zhou/Burgoon logistic regression model [22].

Classi<sup>fi</sup>cation results summary

<table><tr><td rowspan="2">Measure</td><td colspan="3">Model</td></tr><tr><td>Logistic regression mean (Std Dev.)</td><td>Decision tree mean (Std Dev.)</td><td>Neural network mean (Std Dev.)</td></tr><tr><td colspan="4">Overall accuracy % (Test)</td></tr><tr><td>Zhou/Burgoon</td><td>66.93 (11.89)</td><td>69.59 (10.68)</td><td>69.89 (9.13)</td></tr><tr><td>Constructs</td><td>71.16 (10.41)</td><td>71.19 (11.21)</td><td>73.86 (8.23)</td></tr><tr><td>Comprehensive</td><td>70.51 (12.66)</td><td>67.12 (11.09)</td><td>70.46 (12.77)</td></tr><tr><td>Feature Selection</td><td>69.34 (11.39)</td><td>70.87 (10.80)</td><td>72.01 (11.53)</td></tr><tr><td colspan="4">False +</td></tr><tr><td>Zhou/Burgoon</td><td>30.76 (20.64)</td><td>29.29 (22.39)</td><td>31.30 (17.61)</td></tr><tr><td>Constructs</td><td>27.05 (15.32)</td><td>33.39 (18.11)</td><td>32.55 (15.67)</td></tr><tr><td>Comprehensive</td><td>30.54 (19.52)</td><td>38.57 (18.99)</td><td>29.33 (18.47)</td></tr><tr><td>Feature Selection</td><td>30.27 (18.19)</td><td>37.01 (17.02)</td><td>31.25 (18.89)</td></tr><tr><td colspan="4">Sensitivity</td></tr><tr><td>Zhou/Burgoon</td><td>65.00 (14.15)</td><td>68.75 (16.60)</td><td>71.03 (15.49)</td></tr><tr><td>Constructs</td><td>69.46 (16.05)</td><td>75.40 (19.45)</td><td>79.69 (12.81)</td></tr><tr><td>Comprehensive</td><td>71.47 (14.34)</td><td>72.28 (12.88)</td><td>70.49 (19.05)</td></tr><tr><td>Feature Selection</td><td>68.93 (16.36)</td><td>77.95 (16.33)</td><td>74.87 (15.49)</td></tr><tr><td colspan="4">Specificity</td></tr><tr><td>Zhou/Burgoon</td><td>69.24 (20.64)</td><td>70.71 (22.39)</td><td>68.71 (17.61)</td></tr><tr><td>Constructs</td><td>72.95 (15.32)</td><td>66.61 (18.11)</td><td>67.46 (15.67)</td></tr><tr><td>Comprehensive</td><td>69.46 (19.52)</td><td>61.42 (18.99)</td><td>70.67 (18.47)</td></tr><tr><td>Feature selection</td><td>69.73 (18.19)</td><td>62.99 (17.02)</td><td>68.75 (18.89)</td></tr></table>

Overall average statement classi<sup>fi</sup>cation accuracy approaches 74% in the best case scenario (Neural network used on the Constructs cue set). The lower bound for classi<sup>fi</sup>cation accuracy was approximately 67% (logistic regression and the Zhou/Burgoon cue set). This classi<sup>fi</sup>cation accuracy is close to the benchmark accuracy from the previous study that used non real-world data. Further, the results of this study are within the lower end of the range of accuracy one typically expects with the invasive polygraph approach. As described above, a standard ‘better-than-chance’ statistical test was executed on all results, and all accuracy measures were found to be statistically different from chance. Thus, the results indicate a ‘proof-of-concept for the ability of a DSS to accurately detect text-based deception.

## 4.3. Cue set observations

In terms of overall classi<sup>fi</sup>cation accuracy, while not a statistically signi<sup>fi</sup>cant difference, the performance of the classi<sup>fi</sup>ers seemed to be marginally better when using fewer cues. The Constructs cue set provided the highest overall accuracy <sup>fi</sup>gures for each of the three models, followed by the feature selection cue set. Perhaps the strongest statement that can be derived from the results is that there is NOT a loss of accuracy as we attempt to pare down a large set of cue variables to a more parsimonious set. This is encouraging for this research stream as DSS tools for text-based deception detection are further developed.

## 4.4. Model/classification technique observations

With the exception of the Comprehensive cue set, neural networks had marginally higher average overall correct classi<sup>fi</sup>cation accuracy than the other two models. The <sup>fi</sup>ndings here did not replicate past study results that found a poor performance by decision trees. The small differences between the three methods tend to come from the seemingly better ability of the neural networks and decision trees to accurately detect deception (Sensitivity), while the logistic regression models tend to be more accurate in predicting truthful statements (Speci<sup>fi</sup>city). Again, the differences are not statistically signi<sup>fi</sup>cant, but may be practically signi<sup>fi</sup>cant. There is a difference of almost 7% between the lowest testing data accuracy (66.93%) and the highest accuracy (73.86%). To both the witnesses and suspects writing these statements and the law enforcement personnel evaluating the veracity of the text, this increase in accuracy would certainly be notable. It is worth noting that within the Zhou/Burgoon and Constructs cue sets, the neural network average sensitivity exceeds the other classi<sup>fi</sup>cation techniques, and in all cases is above 70% (with the best average almost 80% for the Constructs cue set). For the remaining cue sets, including the Comprehensive and Feature selection cues, the decision tree has higher sensitivity. This provides some evidence that the non parametric approaches (neural networks and decision trees) may have more promise in detecting deception but at the expense of more false positives than what logistic regression may <sup>fi</sup>nd. Alternatively, one could say that logistic regression techniques may be more susceptible to the truth bias than the alternative approaches. In any event, all approaches show promise and add value as the underlying tools to a decision support system automating the detection of deceptive statements.

## 4.5. Summary of cue importance

In addition to analyzing the accuracy of the models, cue importance in each model was evaluated. For ease of reporting, the important cues are reported for the most accurate of the four data sets for each model and cue set combination. For each model, the level of importance of each cue within individual models was evaluated. Additionally, the number of times a cue appeared as important in the ten iterations of cross validation was also considered. For the logistic regression and decision tree models, only important variables are retained as the model is built. For these models, determining which variables are important is straightforward. For the neural network model, all variables are used in model development, making the determination of which cues are important more ambiguous. The results of sensitivity analysis include a relative importance value between zero and one for each cue. There is not a clear cutoff to determine which cues are important or not based on their relative importance, so the results of the other models in terms of number of cues retained was factored in cue importance determination for the neural network. The sensitivity analysis results were also evaluated to determine if a clear cutoff point emerged.

Table 7  
Summary of cue importance

<table><tr><td>Cue</td><td>NN</td><td>DT</td><td>LR</td></tr><tr><td>1st person plural pronouns</td><td>A2</td><td>Z2</td><td></td></tr><tr><td>1st person singular pronouns</td><td></td><td>Z2</td><td>A4</td></tr><tr><td>3rd person pronouns</td><td></td><td>F2</td><td></td></tr><tr><td>Activation</td><td></td><td>A2</td><td></td></tr><tr><td>Bilogarithmic type-token ratio</td><td></td><td></td><td>A4</td></tr><tr><td>Emotiveness</td><td>A2</td><td></td><td></td></tr><tr><td>Generalizing terms</td><td></td><td>A2, C2</td><td></td></tr><tr><td>Imagery</td><td>Z4</td><td>C2</td><td></td></tr><tr><td>Lexical diversity</td><td>A2</td><td></td><td>A4</td></tr><tr><td>Motion terms</td><td>A2</td><td></td><td>A4</td></tr><tr><td>Pleasantness</td><td></td><td>A2</td><td></td></tr><tr><td>Sensory ratio</td><td>C1</td><td>C2</td><td>A4, C1, F1</td></tr><tr><td>Spatial ratio</td><td></td><td>Z2</td><td></td></tr><tr><td>Temporal ratio</td><td>C1, A2, Z4</td><td></td><td>A4</td></tr><tr><td>Verb quantity</td><td>F4, Z4</td><td>Z2</td><td>A4, Z2</td></tr><tr><td>Word quantity</td><td>C1, F4</td><td>A2, C2, F2</td><td>F1, Z2, C1</td></tr></table>

Variables not important for any method: average sentence length, average word length, causation, certainty terms, cognitive processing terms, content word diversity, exclusive terms, modal verbs, modi<sup>fi</sup>ers, passive verbs, pausality, redundancy, second person pronouns, sentence quantity, tentative terms.  
Table indicates cue set (A = All, C = Construct, F = Feature Selection, Z = Zhou/Burgoon) and partition(1,2,3,4).

As word quantity, verb quantity, and sensory ratio were shown to be important across models, future studies might focus on these three variables. Thirteen additional cues are important for at least one model. As is shown in Table 7, <sup>fi</sup>fteen of the variables were not important in any of the models for any cue set.

Most of the variables found important in the Zhou/Burgoon classi-<sup>fi</sup>cation study [52] were also relevant in this study. The 2nd person pronouns and content word diversity were not found important in the present study in contrast with the earlier work. For this particular sample, it is not surprising that second person pronouns, the ‘you’ pronouns, were not important. In this case, the ‘you’ would be law enforcement personnel. As the statement is generally about a previous incident in which law enforcement were not present, it would not be logical to use these pronouns.

Several cues that were not included in the list of important variables from the original set of 22 variables in the Zhou/Burgoon study also failed to be among the most important in this study. This included: average sentence length, modal verbs, passive voice, and redundancy. For the Zhou/Burgoon desert survival study, approximately <sup>fi</sup>ve to seven cues emerged as important for each model. Here, two to seven cues were important per model. Thus, this provides even more evidence that an automated decision support approach can be effective with a very parsimonious cue set.

## 5. Discussion and conclusion

## 5.1. Summary of results

The results above provided evidence that an automated text based deception detection system can be built and provide value added results to a decision maker. Accuracy levels approaching 74% in the range (61–80%) of previous studies in automated linguistic based cues using laboratory data. Evidence also indicated that the search for a more parsimonious set of linguistic cues is reasonable and likely desired. Results were marginally improved with reduced cue sets, whether by classic factor analytic techniques or by using simple feature selection screening. Three variables (word quantity, verb quantity and sensory ratio) were effective for all of the classi<sup>fi</sup>cation models. Similar to past results, a range of two to seven variables were found important in the various models. Since the models are relying on far fewer variables than the total number available, it suggests that conducting automated deception detection with a parsimonious cue set is both possible and desirable. As evidence accumulates across domains as to which variable importance, this can assist in narrowing down the large list of potential cues.

For three of the four cue sets, the neural network models provided the highest test accuracy, though these results were not statistically signi<sup>fi</sup>cant. Given the high-stakes nature of these kinds of situations, though, we must underscore that the differences in classi<sup>fi</sup>cation accuracy may be practically signi<sup>fi</sup>cant. The persons-of-interest in our data set would have much to lose if their statements were incorrectly classi<sup>fi</sup>ed as deceptive. At this stage, though, there is not evidence of a superior classi<sup>fi</sup>cation technique, which differs from past research.

Neural networks and decision trees tended to be more accurate at classifying deceptive statements, while the level of false positives was consistently lowest for the logistic regression model. The results indicate that the manner in which models were trained and evaluated allowed the decision support system to overcome the truth bias inherent in humans. Also, results were presented for speci<sup>fi</sup>city and sensitivity, which allows explication of the possible trade-offs involved between the truth bias and the penalty of false positives.

## 5.2. Future directions

This study showed excellent accuracy in a <sup>fi</sup>rst major attempt to implement automated text-based deception detection using <sup>fi</sup>eld data. Nonetheless, there are likely re<sup>fi</sup>nements possible that could lead to improved results. As the results suggested better performance with smaller cue sets, considering and evaluating additional methods for choosing the best reduced cue set should be explored. The feature selection used here based on the F-statistic may complement logistic regression since it is a typical parametric statistical method relying on linear patterns. Feature selection methods that consider both linear and nonlinear relationships in a model may increase accuracy of the decision tree and neural network models.

Further, additional classi<sup>fi</sup>ers and classi<sup>fi</sup>er approaches such as radial basis function neural networks, random forests, boosted decision trees, and combined methods could improve prediction accuracy. Future studies should continue to use a number of different techniques to ensure that a decision support system uses the best available tools. Also, it is expected that relevant cues to deception will likely differ by domain [12,56]. Nonetheless, while there may not be a single set of cues that is generalizable to all domains, there may be some subset that will apply to other areas. Thus, other domains should be considered as well.

The largest time requirement in developing the system in the study was transcribing the written statements. Alternative methods of capturing written information should be explored as part of the DSS building process. Finally, the long term goal is to use the DSS tool in a predictive mode. To date, all statements received are labeled as truthful or deceptive by law enforcement. The trained models built here can be used to classify unlabelled statements. The tool can then be further re<sup>fi</sup>ned based on the success of classifying these truly unseen examples.

This study offers promise to those practitioners who could utilize a text-based decision support system to assist their deception detection tasks. This tool may also complement other decision support systems that have been introduced to aid law enforcement and other security personnel [5,30,31]. Opportunities for DSS use to support credibility assessment in domains such as <sup>fi</sup>nance, human resources (i.e. resume reviewing), and even the War on Terror (e.g. web site and email analysis) are possible. Investigators could easily and quickly scan textbased material and determine its veracity. Along parallel lines would be to consider studying deception detection in oral communications. Advances in voice recognition software capabilities suggest the need for studies to determine if audio segments could be automatically transcribed and analyzed with linguistic cue analysis. Finally, advances in language translation software may advance the possibility of cross-cultural analysis.

## 5.3. Limitations

The available sample size may have limited the classi<sup>fi</sup>cation accuracy obtained in this study. As previously mentioned, this is likely a continuing issue in deception detection, and it will heighten the importance of cue selection and parsimonious model building. A key factor limiting the sample size is the dif<sup>fi</sup>culty in determining ground truth. Here, every effort was made to correctly identify statements as truthful or deceptive, though this process cannot be foolproof. Also, some statements had to be discarded because they were typed or written by someone else. We could not rely on their authenticity or integrity and did not want to confound our data set. While this appears to have had a negligible impact on the outcome of the study, we cannot discount the possibility. Finally, default parameters were used when constructing the classi<sup>fi</sup>cation models, and it is possible that results could be improved with further <sup>fi</sup>ne tuning of the classi-<sup>fi</sup>cation algorithms.

## 5.4. Conclusion

This study used real word data to test the ability of text-based deception detection methods to support law enforcement decision makers to identify deceptive incident report statements. Analyzing four sets of linguistic cues and three decision support tools resulted in detecting deceptive statements, with an accuracy approaching 74% for military law enforcement person of interest statements. Given that many of the traditional deception detection tools require signi<sup>fi</sup>cant operator training and expertise, the decision support tool outlined in this study may be able to help reduce investigator case loads and provide for effective and ef<sup>fi</sup>cient decision support of credibility assessment tasks.

## References

[1] M. Adkins, D.P. Twitchell, J.K. Burgoon, J.F. Nunamaker, Advances in automated deception detection in text-based computer-mediated communication, Enabling Technologies for Simulation Science VIII, The International Society for Optical Engineering, Orlando, Florida, 2004.

[2] M.J.A. Berry, G.S. Linoff, Data Mining Techniques, 2 ed. Wiley Publishing, Indianapolis, Indiana, 2004.

[3] C.F. Bond, B.M. DePaulo, Accuracy of deception judgments, Personality and Social Psychology Reports 10 (3) (2006).

[4] G.D. Bond, A.Y. Lee, Language of lies in prison: linguistic classi<sup>fi</sup>cation of prisoners truthful and deceptive natural language, Applied Cognitive Psychology 19 (3) (2005)

[5] D.E. Brown, S. Hagen, Data association methods with applications to law enforcement, Decision Support Systems 34 (4) (2003).

[6] D.B. Buller, J.K. Burgoon, Interpersonal deception theory, Communication Theory 6 (3) (1996).

[7] D.B. Buller, J.K. Burgoon, A. Buslig, J. Roiger, Testing interpersonal deception theory: the language of interpersonal deception, Communication Theory 6 (3) (1996).

[8] J.K. Burgoon, T.T. Qin, D.P. Twitchell, The dynamic nature of deceptive verbal communication, Journal of Language & Social Psychology 25 (1) (2006).

[9] J. Cao, J.M. Crews, M. Lin, J. Burgoon, J. Nunamaker, Designing agent99 trainer: a learner-centered, web-based training system for deception detection, Lecture Notes in Computer Science: Proceedings of Intelligence and Security Informatics: ISI 2003, Springer, 2003.

[10] H. Cunningham, Gate, a general architecture for text engineering, Computers and the Humanities 36 (2) (2002).

[11l H. Cunningham D. Maynard K. Bontcheva V. Tablan C. Ursu M. Dimitroy M. Dowman, N. Aswani, I. Roberts, Developing Language Processing Components

with Gate Version 3 (a User Guide) Http://Gate.Ac.Uk/Sale/Tao/Index.Html#X1- 1710008.4. 2005 February 2, 2006 [cited 2006 February 15]; Available from: http:// gate.ac.uk/sale/tao/index.html#x1-1710008.4.

[12] B.M. DePaulo, J.J. Lindsay, B.E. Malone, L. Muhlenbruck, K. Charlton, H. Cooper, Cues to Deception, Psychological Bulletin 129 (1) (2003).

[13] L.N. Driscoll, A validity assessment of written statements from suspects in criminal investigations using the scan technique, Police Studies 17 (4) (1994).

[14] P. Ekman, M. O'Sullivan, Who can catch a liar? American Psychologist 46 (9) (1991).

[15] A.P. Engelbrecht, I. Cloete, J.M. Zurada, Determining the signi<sup>fi</sup>cance of input parameters using sensitivity analysis, From Natural to Arti<sup>fi</sup>cial Neural Computation, Springer-Verlag, Berlin, 1995

[16] T.H. Feeley, M.J. Young, Humans as lie detectors: some more second thoughts, Communication Quarterly 46 (2) (1998).

[17] E.B. Ford, Lie detection: historical, neuropsychiatric and legal dimensions, International Journal of Law and Psychiatry 29 (3) (2006).

[18] M.G. Frank, T.H. Feeley, To catch a liar: challenges for research in lie detection training, Journal Of Applied Communication Research 31 (1) (2003).

[19] C. Fuller, D.P. Biros, D. Twitchell, J. Burgoon, M. Adkins, An analysis of text-based deception detection tools, Twelfth Americas Conference on Information Systems, Association for Information Systems, Acapulco, Mexico, 2006.

[20] M. Gamer, H.G. Rill, G. Vossel, H.W. Godert, Psychophysiological and vocal measures in the detection of guilty knowledge, International Journal Of Psychophysiology 60 (1) (2006).

[21] J.F. George, B.T. Keane, Deception detection by third party observers, deception detection symposium, 39th Annual Hawaii International Conference on System Sciences, 2006.

[22] J.F. Hair, R.E. Anderson, R.L. Tatham, W.C. Black, Multivariate Data Analysis, 5 ed. Prentice-Hall, Inc., Upper Saddle River, New Jersey, 1998.

[23] J. Hancock, L. Curry, S. Goorha, M. Woodworth, Lies in conversation: an examination of deception using automated linguistic analysis, Annual Conference of the Cognitive Science Society, Taylor and Francis Group: Psychology Press, Mahwah, NJ, 2004.

[24] J.T. Hancock, L. Curry, S. Goorha, M. Woodworth, Automated linguistic analysis of deceptive and truthful synchronous computer-mediated communication, Proceedings of the 38th Annual Hawaii International Conference on System Sciences 2005.

[25] J. Hancock, J. Thom-Santelli, T. Ritchie, Deception and design: the impact of communication technology on lying behavior, Proceedings of the SIGCHI conference on Human factors in computing systems, ACM Press, Vienna, Austria, 2004.

[26] H. Hollien, J.D. Harnsberger, Voice Stress Analyzer Instrumentation Evaluation, University of Florida, 2006.

[27] C.R. Honts, D.C. Raskin, A <sup>fi</sup>eld study of the validity of the directed lie control question, Journal Of Police Science And Administration 16 (1) (1988).

[28] F. Horvath, B. Jayne, J. Buckley, Differentiation of truthful and deceptive criminal suspects in behavior analysis interviews, Journal Of Forensic Sciences 39 (3) (1994).

[29] M.K. Johnson, C.L. Raye, Reality monitoring, Psychological Review 88 (1) (1981).

[30] S. Kaza, Y. Wang, H. Chen, Enhancing border security: mutual information analysis to identify suspect vehicles, Decision Support Systems 43 (1) (2007).

[31] K.E. Kendall, B.A. Schuldt, Decentralizing decision support systems a <sup>fi</sup>eld experiment with drug and criminal investigators, Decision Support Systems 9 (3) (1993).

[32] M.Y. Kiang, A comparative assessment of classi<sup>fi</sup>cation methods, Decision Support Systems 35 (4) (2003).

[33] G. Kohnken, Speech and Deception of Eyewitnesses: An Information Processing Approach, in: F.L. Denmark, in: Social/Ecological Psychology and the Psychology of Women. (Elsevier Science Publishers, North-Holland, 1985).

[34] T. Lesce, Scan: deception detection by scienti<sup>fi</sup>c content analysis, Law and Order 38 (8) (1990).

[35] S.A. McCornack, Information manipulation theory, Communication Monographs 59 (1) (1992).

[36] M.L. Newman, J.W. Pennebaker, D.S. Berry, J.M. Richards, Lying words: predicting deception from linguistic styles, Personality and Social Psychology Bulletin 29 (5) (2003).

[37] National Research Council, The Polygraph and Lie Detection, The National Academies Press, Washington, DC, 2003.

[38] S. Porter, J.C. Yuille, The language of deceit: an investigation of the verbal clues to deception in the interrogation context, Law And Human Behavior 20 (4) (1996).

[39] D.C. Raskin, Methodolgical issues in estimating polygraph accuracy in <sup>fi</sup>eld applications, Canadian Journal of behavioral Science 19 (4) (1987).

[40] B. Rice, The new truth machines, Psychology Today 12 (1) (1978).

[41] A. Suzuki, K. Ohnishi, K. Matsuno, M. Arasuna, Amplitude rank score analysis of GSR in the detection of deception: detection rates under various examination conditions, Polygraph 8 (1979).

[42] D.P. Twitchell, D.P. Biros, M. Adkins, N. Forsgren, J.K. Burgoon, J.F. Nunamaker Jr., Automated determination of the veracity of interview statements from people of interest to an operational security force, Proceedings of the 39th Annual Hawaii International Conference on System Sciences, 2006.

[43] D. Twitchell, D.P. Biros, N. Forsgren, J. Burgoon, J.F. Nunamaker Jr., Assessing the veracity of criminal and detainee statements: a study of real-world data, Proceedings of the 2005 International Conference on Intelligence Analysis, 2005.

[44] D. Twitchell, M.L. Jensen, J.K. Burgoon, J.F. Nunamaker Jr., Detecting deception in secondary screening interviews using linguistic analysis, Proceedings of the 7th International IEEE Conference on Intelligent Transportation Systems, 2004.

[45] U. Undeutsch, J.C. Yuille, The development of statement reality analysis, Credibility Assessment, Kluwer Academic/Plenum Publishers, 1989.

[46] A. Vrij, Detecting Lies and Deceit: The Psychology of Lying and the Implications for Professional Practice, John Wiley & Sons, New York, 2000.

[47] A. Vrij, Criteria-based content analysis — a qualitative review of the <sup>fi</sup>rst 37 studies, Psychology Public Policy And Law 11 (1) (2005).

[48] A. Vrij, S. Mann, Telling and detecting lies in a high-stake situation: the case of a convicted murderer, Applied Cognitive Psychology 15 (2) (2001).

[49] A. Vrij, S. Mann, R. Fisher, An empirical test of the behaviour analysis interview Law & Human Behavior 30 (3) (2006).

[50] S.M. Weiss, C.A. Kulikowski, Computer Systems That Learn: Classi<sup>fi</sup>cation and Prediction Methods from Statistics, Neural Nets, Machine Learning, and Expert Systems, Morgan Kaufman Publishers, Inc., San Mateo, California, 1991.

[51] L. Zhou, J.K. Burgoon, J.F. Nunamaker, D.P. Twitchell, Automated linguistics based cues for detecting deception in text-based asynchronous computer-mediated communication: an empirical investigation, Group Decision and Negotiation 13 (1) (2004).

[52] L. Zhou, J.K. Burgoon, D.P. Twitchell, T.T. Qin, J.F. Nunamaker, A comparison of classi<sup>fi</sup>cation methods for predicting deception in computer-mediated communication, Journal Of Management Information Systems 20 (4) (2004)

[53] L. Zhou, D.P. Twitchell, T.T. Qin, J.K. Burgoon, J.F. Nunamaker Jr., An exploratory study into deception detection in text-based computer-mediated communication, Proceedings of the 36th Annual Hawaii International Conference on System Sciences, 2003.

[54] L. Zhou, D.S. Zhang, Typing or messaging? Modality effect on deception detection in computer-mediated communication, Decision Support Systems 44 (2007).

[55] M. Zuckerman, B.M. DePaulo, R. Rosenthal, Verbal and nonverbal communication of deception, Advances in Experimental Social Psychology, Academic Press, New York, 1981.

[56] M. Zuckerman, R.E. Driver, Telling lies: verbal and nonverbal correlates of deception, Multichannel Intergration of Nonverbal Behavior, Erlbaum, Hillsdale, NJ, 1985.

Dr. Christie M. Fuller is Assistant Professor of Computer Information Systems in the College of Business at Louisiana Tech University. Her primary research interests are deception detection and decision support systems. Dr. Fuller's work is published in Expert Systems with Applications, the International Journal of Management and Decision Making, and several conference proceedings.

Dr. David P. Biros is Assistant Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University and Adjunct Professor at Edith Cowen University in Australia. Dr. Biros is the author of numerous articles and conference proceedings related to information assurance, deception and computer-mediated communications. His work is published in MIS Quarterly, Group Decision and Negotiations, and other MIS journals. A retired Air Force Lieutenant Colonel, he previously served as Chief, Information Assurance Division for the AF Chief Information Of<sup>fi</sup>cer.

Dr. Rick L. Wilson is the W. Paul Miller Professor of Business Administration, a Professor of Management Science and Information Systems (MSIS) and the department head of the MSIS Department at the Spears School of Business at Oklahoma State University. Dr Wilson is the author or co-author of over 90 papers in journals, books and presentations at national conferences. His areas of expertise include sports and operations research, statistical-based data security techniques, and data mining approaches.
