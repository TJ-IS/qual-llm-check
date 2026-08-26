---
otero_id: 22139
otero_key: "TR6MUJDG"
title: "Speech recognition in the human–computer interface"
authors: "Carl M. Rebman; Milam W. Aiken; Casey G. Cegielski"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(02)00067-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Speech recognition in the human–computer interface

Carl M. Rebman Jr., Milam W. Aiken<sup>\*</sup>, Casey G. Cegielski

School of Business, University of Mississippi, Mississippi, MS 38677, USA

Received 18 September 2001; received in revised form 28 April 2002; accepted 25 May 2002

## Abstract

Researchers have studied human speech interaction with computers for many years. Much of the focus in this area has been on creating better technical speech recognition (SR) systems, and almost all of the testing has centered on accuracy and productivity gains. However, there has been little study of other issues, such as user acceptance. This paper reports the results of an experiment investigating word generation rates, word error rates, and user acceptance of a speech recognition program as compared to typing. Although the subjects made more errors when using the speech recognition software, they were able to generate more than twice as much text in the same amount of time. However, this relative efficiency was not enough to overcome the inaccuracy and annoyance in fixing so many errors. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Speech recognition; Voice-based computing systems; Human–computer interface

## 1. Introduction

It is not difficult to understand the appeal of speech as a medium for human–computer interaction. Most people talk faster than they can communicate in any other way (e.g. typing or handwriting) [38]. Gesturing through sign language and taking dictation through shorthand or stenography may be just as fast, but few in the general population can utilize these communication modes. Therefore, speaking may be con sidered more natural and intuitive for the average computer user, leading many industry leaders to believe that human–computer interaction through speech will usher in a new era of user-friendly computing [33].

Automated speech recognition (SR) technology has been a topic of research since the 1950s (see Table 1), but advances in the quality of the software and the power of personal computers [19,23] only recently made it sufficiently effective for the trade press to notice it as a viable topic of discussion. The technology, designated SR here, digitizes spoken words, identifies individual sounds (phonemes), and uses mathematical models to select discrete words or complete phrases. When used for dictation, SR can automatically transcribe the selected text into word processors, reducing or eliminating the need to type and increasing the productivity of office work. Used in telephony, the technology may replace cumbersome touch–tone menus or reduce the number of live agents.

Table 1 Automated speech recognition product timeline

Late 1950s: Speech recognition research begins 1964: IBM demonstrates Shoebox for spoken digits at the New York World’s Fair 1968: The HAL-9000 computer in 2001—A Space Odyssey introduces the world to speech recognition 1978: Texas Instruments introduces the first single-chip speech synthesizer and the Speak and Spell toy 1993: IBM launches the first commercial speech recognition product, the IBM Personal Dictation System for OS/2 1993: Apple ships PlainTalk, a series of speech recognition and speech synthesis extensions for the Macintosh 1994: DragonSystems’ DragonDictate for Windows 1.0 is the first software only, PC-based dictation product 1996: IBM introduces MedSpeak/Radiology, the first real-time, continuous-speech recognition product 1996: OS/2 Warp 4 becomes the first operating system to include built-in speech navigation and recognition June 1997: DragonSystems ships NaturallySpeaking, the first general-purpose, continuous-speech recognition product August 1997: IBM ships ViaVoice Fall 1997: Microsoft CEO Bill Gates identifies speech recognition as a key technological advance

Source: http://www.zdnet.com/pcmag/features/speech/sb1.html.

Finally, SR can be used to control machinery, allowing hands-free operation and greater concentration on more important tasks.

Several studies have tested the accuracy of SR, but little research has been conducted on user acceptance of the technology and how the systems compare with the more traditional means of entering information into a computer, the keyboard [30]. The objective of this study was to investigate the accuracy and speed of a leading SR program along with user satisfaction when using the technology.

## 2. Speech recognition technology

## 2.1. Applications of SR

Automated speech recognition is being used in numerous areas, and 25% of the largest corporations in the United States have developed SR applications to improve productivity. SR is used primarily to facilitate dictation, but it can also be used for ‘‘hands-free’’ control (e.g. voice-directed picking at Wal-Mart warehouses improves inventory handling accuracy and speed).

In addition, communication through SR typically is much faster and more reliable than communication with a human telephone operator or a touch–tone system [37]. For example, Fidelity Investments has implemented an SR call center that can field an average of 250,000 calls per day with the capacity to handle 3–4 times that number on peak days [35]. SR systems may pay for themselves within 6–18 months in call centers with more than 50 agents, and approximately 30% of new automated lines in call centers may use SR by 2003. Currently, there are 79,500 or one-third fewer telephone operators than there were in 1990, due primarily to automated, touch–tone systems, and increased SR telephony could reduce this number still further.

## 2.2. SR categories

SR technology can be categorized in terms of speaker dependency and speech mode (as shown in Fig. 1) [29].

## 2.2.1. Speaker dependent or independent

Speaker-dependent SR technology requires a user to train the program to recognize his or her voice (the process is referred to as ‘‘enrollment’’). This type of SR is better for those with non-standard speaking patterns, dialects, or foreign accents [28]. Speakerindependent programs are designed to interpret any user’s voice with no enrollment, but this type of software is usually less accurate. If the software is speaker independent, a default set of discrete sounds or phonemes is provided, otherwise user enrollment creates a personalized set of phonemes for improved accuracy.

## 2.2.2. Continuous or discrete speech

Continuous-speech SR allows the user to talk normally in complete sentences while discrete-speech SR requires the user to pause after each word [17]. Continuous speech is usually considered to be more natural, less frustrating, and faster. In addition, being more complex, continuous-speech SR can recognize individual words (discrete speech) as well as entire phrases. Although some studies have suggested that discrete-speech SR is more accurate, others have shown the opposite to be true [16,25].

![](/api/attachments/TR6MUJDG/fulltext/images/b8a755cad26b3ffe7df9ba1f6e17d75ca07a2acc37a949c386a3181fd83378b0.jpg)  
Fig. 1. Implementation of SR.

## 2.3. The SR process

The speech recognition process follows five steps [21]:

1. Audio input: The human voice is transmitted through a microphone connected to a PC with a standard sound card.

2. Acoustic processor: The acoustic processor filters out background noise and converts the captured audio into a series of phonemes.

3. Word matching: The software attempts to match the sounds to the most-likely words in two ways. First, it uses acoustical analysis to build a list of possible matches that contain similar sounds. Then, it uses language modeling (the likelihood that a given word appears between those coming before and after it) to narrow the list to the best candidates. In addition, the word-matching process draws on the user-defined domain (the set of vocabularies, pronunciations, and word-usage models, as well as a model of the user’s speech and words). The user can extend the domain by adding new words and can create multiple domains for different applications. Finally, continuous-speech SR examines contextual information to predict what words should come next in the current phrase. This also helps the system to distinguish among homonyms.

4. Decoder: The decoder selects the most-likely word based on the rankings assigned during word matching and assembles the word along with those selected earlier into the most-likely sentence combination.

5. Text output: Some SR programs include their own word processors, but many also allow text transcription directly into a separate word processing program or a text box in an application, such as a web browser or e-mail program.

## 2.4. SR limitations

While SR requires less hardware (e.g. no keyboard is needed for input—especially advantageous for PDA’s) and people speaking can generate text faster than those typing, there are some significant limitations. Most important, the current state of the technology prevents transcriptions from achieving 100% accuracy because of slurred speech, mispronunciation, and background noise that becomes worse in crowded offices [24]. Enrollment can improve the accuracy somewhat, but this represents added startup cost.

## 3. Speech recognition testing

The accuracy of several SR systems has been shown in the literature. Some systems have been tested in a constrained domain (benefiting from a restricted vocabulary) and have achieved error rates of less than 20% [13,27], while other tests of commercial systems have been anecdotal and tuned by the software vendors to perform well on the particular test. Further, results from tests of SR programs can vary, based upon the complexity of the input [1].

## 3.1. Tests of multiple systems

Tests have shown that the accuracy for PC-based SR systems typically ranges from 80 to 99% [2,4]. While some of these tests are not directly comparable, because of differences in source text, efficiency and effectiveness measures, and testing periods, they give an indication of the current state of the technology.

Using standardized protocols and reference test sets developed by the National Institute of Standards [26], a mixture of research and commercially available systems were compared directly, as shown in Table 2. There was no statistically significant difference in the results of the first three systems and little difference in the first seven. However, the last five systems were clearly less accurate.

## 3.2. Tests of DragonSystems

DragonSystems is perhaps the US market leader of PC-based, continuous-speech, general-purpose SR software. In a test at PC Labs with five subjects using the software, an accuracy of 89.1% was achieved at 74 wpm as compared to 87.8% at 69 wpm with SR software from IBM.<sup>2</sup> In addition, anecdotal tests of DragonSystems have shown:<sup>3</sup>

A Summary of SR system accuracy tests (abstracted from [7,9,10,12,26,31,36])

<table><tr><td>System</td><td>Word error rate (%)</td></tr><tr><td>LVCR</td><td>12</td></tr><tr><td>SPHINX III</td><td>13</td></tr><tr><td>IBM</td><td>13</td></tr><tr><td>LIMSI</td><td>14</td></tr><tr><td>CU-HTK</td><td>14</td></tr><tr><td>DragonSystems</td><td>15</td></tr><tr><td>BBN</td><td>15</td></tr><tr><td>Phillips-RWTH</td><td>18</td></tr><tr><td>SPRACH</td><td>21</td></tr><tr><td>SRI</td><td>21</td></tr><tr><td>BYBLOS</td><td>21</td></tr><tr><td>OGI-FONIX</td><td>26</td></tr></table>

\- At Raytheon, the average time to process a Material Requisition Form was reduced from 162 to 44 s (over 4 h per month) with the aid of voice macros.

\- An attorney’s staff increased their document preparation productivity by 25%.

\- An attorney generated text at 120 wpm with 95% accuracy using the software, and a nurse generated 138 wpm as compared to 40 wpm when typing.

\- Medical transcripts were produced in one-third of the time required when typing.

\- A doctor reduced turnaround time for medical transcriptions from 2 weeks to 1 day and reduced his variable transcript service cost from US\$ 150 per day to almost zero.

\- Total medical transcription charges of about US\$ 100,000 per year at a medical center were reduced by about 80%.

DragonSystems’ NaturallySpeaking Preferred, Version 4.01 was selected for our study. Other, perhaps more accurate, commercial SR systems, such as LVCR, LIMSI, and CU-HTK, are not readily obtainable, and as a market leader, use of the selected system makes the study more replicable.

## 4. The study

## 4.1. Research questions

Our study examined three issues related to the successful adoption of SR for business applications.

1. How accurate is text generated through SR as compared to typing?

Prior studies have indicated SR accuracies up to 99%, but no tests have compared the accuracy of subjects using SR and the keyboard to generate the same text. Although most college-age students (our subject population) know how to type, they vary in their skill. Nevertheless, we expected the subjects using SR to be less accurate than subjects using the keyboard.

H<sub>1</sub>. Subjects using SR are less accurate than subjects using a keyboard.

2. How fast can text be generated through SR as compared to typing?

A student typist may be able to type 13–41 wpm, a good typist may type from 61 to 90 wpm, and an excellent typist may type from 85 to 112 wpm, assuming five characters per word [8]. But people speak much faster than they type [32,34]. When limited by the necessity to generate free-form comments in conversational English, people typically speak at about 100–150 wpm [18]. A second study [20] found that a speaker with a normal speech rate produces about 150 wpm, but the maximum speech rate can be as much as 637 wpm [11]. Thus, we expected the subjects using SR to be able to generate text faster than subjects using the keyboard.

$\mathbf { H } _ { 2 } .$ Subjects using SR generate more text than sub jects using a keyboard.

3. What type of users will adopt speech recognition technology?

Some people might not use computers because of keyboard frustrations or an inability to understand the interface. We expected users with less keyboard experience would think that SR is easier to use and more efficient.

H<sub>3</sub>. Subjects with poor typing skills consider SR easier to use and more efficient than subjects with good typing skills.

## 4.2. Method

We conducted a series of eight tests across two levels of text difficulty (as measured by readability scores), two types of input (voice and keyboard), and two types of input patterns (continuous/discrete).

## 4.2.1. Subjects

A repeated-measures research design was developed [15], and 28 students completed a total of 112 different tests for extra credit toward their class grades. The subjects were mostly junior and senior business majors, and their computer and keyboard experience ranged from novice to expert. An a priori power test of sample size indicated a level of 0.80, considered to be adequate for experimental validity [6].

## 4.2.2. Tasks

The 28 subjects were divided into two groups and were given a passage of hard text (331 words, reading ease score ¼ 40:2, reading grade level ¼ 12) or easy text (418 words, reading ease score ¼ 82:4, reading grade level ¼ 3:8) to enter into the computer by speaking and typing [3]. All subjects were limited to 5 min for text entry. Each subject performed the following tests using their selected text:

\- Test 1: Subjects spoke in a normal voice and were not concerned with errors (speaking-maximum input).

\- Test 2: Subjects spoke in a manner to cause the least amount of error and were allowed to correct any errors by voice command (speaking-maximum accuracy). For example, subjects could say ‘‘scratch that’ to delete the prior word or phrase generated by the SR software. Thus, no typing was needed for editing.

\- Test 3: Subjects typed as fast as they could and were not concerned with errors (typing-maximum input).

\- Test 4: Subjects typed carefully and corrected any errors through the keyboard (typing-maximum accuracy).

## 4.2.3. Measures

This study examined user performance and perceptions with voice-based and traditional keyboard interfaces. Efficiency was measured by the number of words generated in the allotted 5 min, and effectiveness was measured by the number of misspelled words. A pre-tested questionnaire used in an earlier study of human–computer interaction [5] was used to capture subject perceptions and self-reported keyboard experience (Appendix A).

## 4.2.4. Procedures

All subjects received a standard 30 min enrollment session at the beginning of the experiment to train the SR software to recognize their voices and speech mannerisms. Subjects then completed two voicebased tests and two keyboard tests. No tutorial was provided for typing. After completing the tasks, subjects were asked to complete the questionnaire.

Table 3  
Word generation and accuracy results

<table><tr><td rowspan="2"></td><td colspan="2">Average total words</td><td colspan="2">Words per min</td><td colspan="2">Average misspelled words</td><td colspan="2">Average accuracy</td></tr><tr><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td><td>Mean (%)</td><td>S.D. (%)</td></tr><tr><td colspan="9">Easy text</td></tr><tr><td>Speaking/speed</td><td>425</td><td>119</td><td>85</td><td>24</td><td>109</td><td>37</td><td>73</td><td>10</td></tr><tr><td>Speaking/accuracy</td><td>62</td><td>37</td><td>12</td><td>7</td><td>7</td><td>6</td><td>85</td><td>17</td></tr><tr><td>Typing/speed</td><td>182</td><td>81</td><td>36</td><td>16</td><td>18</td><td>14</td><td>91</td><td>6</td></tr><tr><td>Typing/accuracy</td><td>185</td><td>54</td><td>37</td><td>11</td><td>3</td><td>3</td><td>98</td><td>2</td></tr><tr><td colspan="9">Hard text</td></tr><tr><td>Speaking/speed</td><td>313</td><td>79</td><td>63</td><td>16</td><td>82</td><td>29</td><td>74</td><td>7</td></tr><tr><td>Speaking/accuracy</td><td>101</td><td>119</td><td>20</td><td>24</td><td>27</td><td>24</td><td>62</td><td>23</td></tr><tr><td>Typing/speed</td><td>121</td><td>32</td><td>24</td><td>6</td><td>12</td><td>7</td><td>89</td><td>6</td></tr><tr><td>Typing/accuracy</td><td>121</td><td>37</td><td>24</td><td>7</td><td>3</td><td>3</td><td>97</td><td>4</td></tr></table>

## 4.3. Results

Table 3 shows the means and standard deviations for all of the accuracy and word generation tests, and Figs. 2 and 3 illustrate the differences between the SR and keyboard interfaces. Table 4 shows comparisons among different combinations of communication modes and text difficulty.

![](/api/attachments/TR6MUJDG/fulltext/images/30494b8c2cbaaee70460266d99bacff1703637bc5769855e09433a431de99e75.jpg)

On average, accuracy using SR was approximately 85% for the easy text and 62% for the hard text while accuracy for typing was about 98 and 97%, respectively. As one would expect, when concentrating on making as few mistakes as possible, typing and SR accuracy improved. In tests using easy and hard text for maximum accuracy and maximum speed, SR accuracy was consistently worse than typing accuracy. Therefore, we cannot reject Hypothesis $\mathrm { H } _ { 1 }$

## 4.3.1. Effectiveness

![](/api/attachments/TR6MUJDG/fulltext/images/ff555f9f3cde574510eccd92f827ebbe8b04912e546c49820221eeb268975333.jpg)

![](/api/attachments/TR6MUJDG/fulltext/images/6c93953c8169f2b3dbb5b25a57ccfcb0d69f81a852c787e2812542a711bf7fbd.jpg)

Fig. 2. Comparisons of accuracy.  
![](/api/attachments/TR6MUJDG/fulltext/images/bc26326eb4855f3928db63bb50d74915bc05e9b4f012a09f1fce5ec53bbb8a30.jpg)

Table 4  
![](/api/attachments/TR6MUJDG/fulltext/images/f63f8f31c251764fcfcbd4adb8416ee75e2fcc7d5b559c3ab368e536936543d7.jpg)  
Fig. 3. Comparisons of speed.

## 4.3.2. Efficiency

Overall, subjects using the SR system on average generated 149% more words than subjects when typing, an obviously significant difference. Using SR, subjects entered 85 wpm with the easy text, and 63 wpm with the hard text, as compared to 36 wpm with the easy text and 24 wpm with the hard text while typing. There was significantly more text generated using SR when subjects were concentrating on speed rather than accuracy, but there was no significant difference with typing. Using SR and typing, subjects generated more words when using the easy text while

Difference-of-means t-tests for word generation and accuracy rates

<table><tr><td></td><td>t-test</td><td>P-value</td></tr><tr><td colspan="3">Word generation</td></tr><tr><td>SR-easy text (maximum speed versus maximum accuracy)</td><td>10.93</td><td>&lt;0.001</td></tr><tr><td>SR-hard text (maximum speed versus maximum accuracy)</td><td>5.58</td><td>&lt;0.001</td></tr><tr><td>SR-maximum speed (easy versus hard text)</td><td>2.85</td><td>0.002</td></tr><tr><td>SR-maximum accuracy (easy versus hard text)</td><td>-1.20</td><td>0.115</td></tr><tr><td>Typing-easy text (maximum speed versus maximum accuracy)</td><td>-0.193</td><td>0.425</td></tr><tr><td>Typing-hard text (maximum speed versus maximum accuracy)</td><td>0</td><td>0.500</td></tr><tr><td>Typing-maximum speed (easy versus hard text)</td><td>2.63</td><td>0.004</td></tr><tr><td>Typing-maximum accuracy (easy versus hard text)</td><td>3.73</td><td>&lt;0.001</td></tr><tr><td>Easy text-maximum speed (SR versus typing)</td><td>6.36</td><td>&lt;0.001</td></tr><tr><td>Easy text-maximum accuracy (SR versus typing)</td><td>-7.17</td><td>&lt;0.001</td></tr><tr><td>Hard text-maximum speed (SR versus typing)</td><td>8.54</td><td>&lt;0.001</td></tr><tr><td>Hard text-maximum accuracy (SR versus typing)</td><td>-0.60</td><td>0.270</td></tr><tr><td colspan="3">Accuracy</td></tr><tr><td>SR-easy text (maximum speed versus maximum accuracy)</td><td>-2.28</td><td>0.001</td></tr><tr><td>SR-hard text (maximum speed versus maximum accuracy)</td><td>1.87</td><td>0.031</td></tr><tr><td>SR-maximum speed (easy versus hard text)</td><td>-0.31</td><td>0.379</td></tr><tr><td>SR-maximum accuracy (easy versus hard text)</td><td>3.01</td><td>0.001</td></tr><tr><td>Typing-easy text (maximum speed versus maximum accuracy)</td><td>-4.14</td><td>&lt;0.001</td></tr><tr><td>Typing-hard text (maximum speed versus maximum accuracy)</td><td>-4.15</td><td>&lt;0.001</td></tr><tr><td>Typing-maximum speed (easy versus hard text)</td><td>0.88</td><td>0.190</td></tr><tr><td>Typing-maximum accuracy (easy versus hard text)</td><td>0.84</td><td>0.200</td></tr><tr><td>Easy text-maximum speed (SR versus typing)</td><td>-5.78</td><td>&lt;0.001</td></tr><tr><td>Easy text-maximum accuracy (SR versus typing)</td><td>-2.84</td><td>0.002</td></tr><tr><td>Hard text-maximum speed (SR versus typing)</td><td>-6.09</td><td>&lt;0.001</td></tr><tr><td>Hard text-maximum accuracy (SR versus typing)</td><td>-5.61</td><td>&lt;0.001</td></tr></table>

Table 7  
Table 6 Hard text summary statistics  
Table 5 Easy text summary statistics

<table><tr><td>Variable</td><td>Mean</td><td>S.D.</td></tr><tr><td>TALKEASE</td><td>4.0</td><td>1.4</td></tr><tr><td>TALKCOMP</td><td>2.6</td><td>1.7</td></tr><tr><td>DATAENT</td><td>2.9</td><td>1.5</td></tr><tr><td>DEOVERALL</td><td>2.4</td><td>1.5</td></tr><tr><td>DESMWRDS</td><td>2.1</td><td>1.0</td></tr><tr><td>DESMCSTR</td><td>2.9</td><td>1.7</td></tr><tr><td>DECORREC</td><td>1.7</td><td>1.1</td></tr><tr><td>PEFFICENCY</td><td>3.2</td><td>1.4</td></tr><tr><td>KEYEXP</td><td>2.3</td><td>1.5</td></tr><tr><td>WILL2REP</td><td>3.0</td><td>1.1</td></tr><tr><td>WILL2ADD</td><td>2.4</td><td>0.9</td></tr></table>

Explanation of variables (questionnaire is shown in Appendix A)— TALKEASE: asked the subjects to rank how easy SR was to use; TALKCOMP: asked the subjects to compare using SR to using the keyboard; DATAENT: asked the subjects how easy they felt SR was to enter data; DEOVERALL: asked the subjects to compare how easy SR was to enter data in comparison to typing; DESMWRDS: compared data entry using SR to enter small words versus the keyboard; DESMCSTR: compared data entry using SR to enter small character strings versus the keyboard; DECORREC: compared correcting mistakes using SR versus the keyboard; PEFFICIENCY: asked the subjects to rank their perception regarding the efficiency of the SR; KEYEXP: asked the subjects to evaluate their keyboard experience in hours of use; WILL2REP: asked the subjects to determine their willingness to replace the keyboard with SR; WILL2ADD: asked the subjects to determine their willingness to use SR in addition to the keyboard.

focusing on speed and accuracy both. Finally, subjects using SR generated more text than subjects typing when focusing on maximum speed, but generated less text when focusing on maximum accuracy. Therefore, we reject Hypothesis $\mathrm { H } _ { 2 }$ when maximum accuracy is the focus.

## 4.3.3. User preferences

Tables 5 and 6 summarize subjects’ self-assessed responses. Subjects’ keyboard experience ranged from zero to more than 1000 h. Using difference-of-means t-tests comparing subject responses with the medians of the scales showed that subjects thought the SR program was neither easy nor difficult to use. However, in all of the other measures comparing SR and typing, SR was considered to be significantly worse. With the exception of ease of correcting mistakes, there was no statistically significant difference between poor and skilled typists’ perceptions with any of the other variables (Table 7). In particular, there were no significant differences between poor and skilled typists’ perceptions of efficiency and ease-ofuse. Therefore, we reject Hypothesis $\mathrm { H } _ { 3 } .$

<table><tr><td>Variable</td><td>Mean</td><td>S.D.</td></tr><tr><td>TALKEASE</td><td>3.8</td><td>1.4</td></tr><tr><td>TALKCOMP</td><td>3.1</td><td>1.5</td></tr><tr><td>DATAENT</td><td>3.6</td><td>1.7</td></tr><tr><td>DEOVERALL</td><td>2.9</td><td>1.6</td></tr><tr><td>DESMWRDS</td><td>3.3</td><td>1.3</td></tr><tr><td>DESMCSTR</td><td>3.1</td><td>1.5</td></tr><tr><td>DECORREC</td><td>1.2</td><td>0.4</td></tr><tr><td>PEFFICENCY</td><td>3.6</td><td>0.9</td></tr><tr><td>KEYEXP</td><td>3.2</td><td>1.4</td></tr><tr><td>WILL2REP</td><td>2.1</td><td>0.9</td></tr><tr><td>WILL2ADD</td><td>1.9</td><td>0.8</td></tr></table>

These poor results can be attributed primarily to the low accuracy rates of the SR transcriptions causing user frustrations. Additionally, there could be some reluctance to use new technology for computer input, as most subjects were accustomed to keyboard use.

There was one interesting result that contradicted our expectations. There was an inverse correlation between hard and easy text and user acceptance of SR. Subjects who were tested using the hard text reported a higher willingness to replace the keyboard $( \mathrm { m e a n } = 2 . 1 4 , \mathrm { S . D . } = 0 . 9 5 )$ than the easy-text subjects $( \mathrm { m e a n } = 3 . 0 0 , \mathrm { S . D . } = 1 . 1 1 )$

## 4.4. What kind of users will adopt speech recognition technology?

People might embrace SR because of its ease-of-use [14]. Because the results of this study have shown that keyboard experience does not necessarily affect perceived efficiency or ease-of-use, the novelty effect alone might not increase the number of its users.

Tests for effects by typing experience (P-value indicated is a higher bound)

<table><tr><td>Measure</td><td>Difficult text (F)</td><td>Easy text (F)</td><td>Pr &gt; F</td></tr><tr><td>Ease of entering characters</td><td>0.108</td><td>0.26</td><td>0.90</td></tr><tr><td>Ease of entering small words</td><td>0.581</td><td>3.2</td><td>0.07</td></tr><tr><td>Ease of entering small strings</td><td>0.650</td><td>2.76</td><td>0.09</td></tr><tr><td>Ease of correcting mistakes</td><td>1.286</td><td>7.64</td><td>0.01</td></tr><tr><td>Perceived efficiency</td><td>0.579</td><td>1.17</td><td>0.39</td></tr><tr><td>Overall ease-of-use</td><td>0.099</td><td>0.26</td><td>0.90</td></tr></table>

d.f.: (4, 13).

Subjects who used the hard text were more willing to replace the keyboard with the voice-based interface. They recognized that the speech system had less accuracy but considered it better than having to type specialized words with much punctuation. This was inversely correlated to the users who used the easy text and who felt that it was quicker and more accurate to use the keyboard when the text was not as difficult. Whenever the voice-based interface simplifies a more challenging task that the end user perceives will be easier to use and take less time, people might choose the speech recognition system. If the task appears to be relatively simple and the voice-interface too cumbersome, users might opt to use the keyboard [22].

The results of this experiment are encouraging for this new technology. Because it has the capability to capture a large amount of text, these systems could be utilized in many different data entry applications.

## 4.5. Limitations

It is evident that the system we tested was not yet sufficient to persuade users to accept this technology in place of traditional keyboard entry. The accuracy of the system is still significantly lower than that of traditional keyboard entry. Further work is necessary to raise the SR accuracy rate. Because some studies have shown that accuracy improves with user experience, one possible avenue is in additional user training.

One limitation of our study is that it was conducted with young university students who might be more apt to accept new technology than older professionals. In addition, the text selected for input might not be representative of the material that the users would normally enter.

One possible impediment towards acceptance of this technology is that users might not like to use a microphone headset for inputting text. However, it is doubtful that this is a serious barrier. The headset has existed for over 100 years, and widespread use of audio devices, such as the Sony’s ‘‘walkman,’’ could lead to higher user acceptance. In addition, the customer service industry segment is such a large consumer of SR-related technology that many ergonomic devices have been created to diminish their negative effects.

## 5. Conclusion

Speech recognition has the potential to be a significant factor in the future of human–computer interaction. Many computer users prefer an easier interface and might be willing to tolerate more errors when tasks are perceived as too time consuming. With further improvements in the technology, users will become more productive in text generation and computer control, especially when incorporated into PDA’s.

This study is perhaps the first rigorously to compare speech recognition technology with the traditional means of computer input—typing. As expected, relatively untrained, first-time users made more errors when using the technology than when typing. Although subjects generated more text using SR than when typing in some cases, they generated less in others. Because of the poor accuracy relative to typing, subjects’ perceptions of the technology were relatively poor. Finally, these perceptions did not vary to a great extent between poor and skilled typists.

## Acknowledgements

This research was supported by a grant from the Hearin Foundation. In addition, we would like to thank two anonymous reviewers for their constructive comments.

## Appendix A. Questionnaire

Overall ease-of-use (1) In general using the talking program was (1) Extremely difficult (2) Difficult (3) Fairly difficult (4) Neither easy or difficult (5) Fairly easy (6) Very easy (7) Extremely easy

## Appendix A. (Continued )

(2) Overall, compared with the talking program, using the keyboard appears to be
(1) Very much easier
(2) Easier
(3) A little easier
(4) About the same
(5) A little harder
(6) Harder
(7) Very much harder

Data entry
(1) Using the talking program I found that entering words was
(1) Extremely difficult
(2) Difficult
(3) Fairly difficult
(4) Neither easy or difficult
(5) Fairly easy
(6) Very easy
(7) Extremely easy

(2) Compared to the talking program, entering words (overall) with the keyboard is
(1) Very much easier
(2) Easier
(3) A little easier
(4) About the same
(5) A little harder
(6) Harder
(7) Very much harder

(3) Compared to the talking program, entering small words with the keyboard is
(1) Very much easier
(2) Easier
(3) A little easier
(4) About the same
(5) A little harder
(6) Harder
(7) Very much harder

## References

[1] M. Aiken, Z. Wong, M. Vanjani, in: Proceedings of the Allied Academies International Conference on Speech Complexity and Automatic Recognition Accuracy, Nashville, TN, 4–7 April 2001.

[2] S. Alexander, Speech recognition, Computer World 33 (45), 1999, pp. 65.

[3] R. Anderson, A. Davison, Conceptual and Empirical Bases of Readability Formulas, Bolt Beranek and Newman Inc., New York, 1986.

[4] H. Bethoney, Speech products: the talk of the town, PC Week 8, 1999, pp. 5.

[5] R. Briggs, A. Dennis, B. Beck, J. Nunamaker, Whither the pen-based interface? Journal of Management Information Systems 9 (3), 1992/1993, pp. 71–90.

[6] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, 2nd Edition, Lawrence Erlbaum Associates, Hillsdale, NJ, 1988.

[7] S. Colbath, D. Liu, A. Srivastava, J. Makhoul, Integrated technologies for indexing spoken language, Communications of the ACM 43 (2), 2000, pp. 48–56.

[8] W. Cooper, Cognitive Aspects of Skilled Typewriting, Springer, New York, 1983.

[9] S. Furui, K. Ohtsuki, Z. Zhang, Japanese broadcast news transcription and information extraction, Communications of the ACM 43 (2), 2000, pp. 71–73.

[10] J. Gauvain, L. Lamel, G. Adda, Transcribing broadcast news for audio and video indexing, Communications of the ACM 43 (2), 2000, pp. 64–70.

[11] The Guinness Book of World Records, Guinness Media, Stamford, CT, 1999.

[12] G. Herb, M. Schmidt, Text-independent speaker identification, IEEE Signal Processing Magazine, October 1994, pp. 18–32.

[13] P. Jang, A. Hauptmann, Learning to recognize speech by watching television, IEEE Intelligent Systems 14 (5), 1999, pp. 51–58.

[14] E. Karahanna, D. Straub, The psychological origins of perceived usefulness and ease-of-use, Information and Management 35 (4), 1999, pp. 237–250.

[15] G. Keppel, Design and Analysis: A Researcher’s Handbook, 3rd Edition, Prentice-Hall, Upper Saddle River, NJ, 1991.

[16] R. Klevans, R. Rodman, Voice Recognition, Artech House, Boston, 1997.

[17] C. Lee, F. Soong, K. Paliwal, Automatic Speech and Speaker Recognition: Advanced Topics, Kluwer Academic Publishers, Boston, 1996.

[18] E. Lenneberg, Biological Foundations of Language, Wiley, New York, 1967.

[19] C. Lindquist, Speak easy, PC World 17 (10), 1999, pp. 185– 195.

[20] H. MacKay, C. Osgood, Hesitation phenomena in spontaneous English speech, Word 15, 1959, pp. 19–44.

[21] J. Markowitz, Using Speech Recognition, Prentice-Hall, Upper Saddle River, NJ, 1996.

[22] K. Mathieson, M. Keil, Beyond the interface: ease-of-use and task/technology fit, Information and Management 34 (4), 1998, pp. 221–230.

[23] S. Miastkowski, Latest speech software gets you up and running faster, PC World 11, 1999, pp. 63–66.

[24] B. Moore, Sound advice on speech technology, Material Handling Engineering 54 (6), 1999, pp. 4–8.

[25] J. Niccolai, First speech-recognition e-mail announced, InfoWorld 11, 1997, pp. 57.

[26] D. Pallett, J. Garofolo, J. Fiscus, Measurements in support of research accomplishments, Communications of the ACM 43 (2), 2000, pp. 75–79.

[27] H. Quastler, Studies of human channel capacity, in: C. Cherry (Ed.), Information Theory, Butterworths, London, 1956

[28] L. Rabiner, J. Biing-Hwang, Fundamentals of Speech Recognition, Prentice-Hall, Englewood Cliffs, NJ, 1993.

[29] R. Rodman, Computer Speech Technology, Artech House, Boston, 1999.

[30] A. Sankar, R. Gadde, F. Weng, SRI’s broadcast news system—toward faster, smaller, and better speech recognition, in: Proceedings of the DARPA Broadcast News Workshop, 1999, pp. 281–286.

[31] K. Seymore, S. Chen, M. Eskenazi, R. Rosenfeld, Language and pronunciation modeling in the CMU 1996 Hub 4 evaluation, in: Proceedings of the Spoken Language Systems Technology Workshop, Morgan Kaufmann, Los Altos, CA, 1997.

[32] T. Sticht, J. James, Listening and reading, in: P. Pearson (Ed.), Handbook of Reading Research, Longman, New York, 1984.

[33] B. Stone, Look who’s talking now, Newsweek 2, 1999, pp. 48–51.

[34] S. Taylor, Listening, National Education Association, Washington, DC, 1964.

[35] M. Thyfault, Voice gets reliable, Information Week 2, 1999, pp. 113.

[36] H. Wactlar, A. Hauptmann, M. Christel, R. Houghton, A. Olligschlaeger, Complementary video and audio analysis for broadcast news archives, Communications of the ACM 43 (2), 2000, pp. 42–47.

[37] F. Westall, R. Johnston, A. Lewis, Speech Technology for Telecommunications, Chapman & Hall, New York, 1998.

[38] W. Willis, Speech recognition: instead of typing and clicking, talk and command, THE Journal 1, 1998, pp. 18– 22.

![](/api/attachments/TR6MUJDG/fulltext/images/d6df8b290ce772aa907b126bf9af0e8efa65d2bcf775a1e2d527b6623841b521.jpg)

Carl M. Rebman Jr. received BFA degrees from the University of Arizona in Media Management and Photography/ Graphic Design and MBA and PhD in MIS from the University of Mississippi. He is currently an Assistant Professor of IS and Electronic Commerce and Director of the Information Technology Management Institute at the University of San Diego. His research interests are

in the areas of Group Support Systems, computer self-efficacy, network management, and voice recognition.

![](/api/attachments/TR6MUJDG/fulltext/images/099b894b5a5477ad6b4e7c01870a20df2d3823765ceb88b51b1c18ea1b0f8eea.jpg)

Milam W. Aiken received BS in Engineering and MBA from the University of Oklahoma, BA in Computer Science and BS in Business from the State University of New York, and PhD in MIS from the University of Arizona. He is currently an Associate Professor of MIS at the University of Mississippi and has published over 170 journals and proceedings articles in the areas of Group Support Systems and neural networks.

![](/api/attachments/TR6MUJDG/fulltext/images/5704f9d604097f03e3b262f19f0ac2adbfb73a5b5ba4a92f9cab6d0d46d915e2.jpg)

Casey G. Cegielski received BA and Master of Accountancy from the University of Alabama and PhD in MIS from the University of Mississippi. He is currently an Assistant Professor of MIS at Auburn University. His research interests include innovation diffusion, IT strategy, voice recognition, and emerging information technologies.
