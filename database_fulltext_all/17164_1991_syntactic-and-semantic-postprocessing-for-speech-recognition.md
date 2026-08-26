---
otero_id: 17164
otero_key: "ARZYMCWB"
title: "Syntactic and semantic postprocessing for speech recognition"
authors: "Hermann Krallmann; Ruth Marzi"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90042-a"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Syntactic and semantic postprocessing for speech recognition

Hermann Krallmann and Ruth Marzi

Institut für Quantitative Methoden, Technische Universität Berlin, D-1000 Berlin 10, Germany

In this paper we present part of a system, which is devised to direct systems controlling non-safety-sensitive functions of car, a voice-mailbox system and an integrated office environment by speech. The post-processing, which is discussed here, is based on methods from the area of Artificial Intelligence. The input is checked for its linguistic properties in order to determine the intended meaning of an utterance and to direct the execution of the resulting action.

Keywords: Information system, Speech processing, Natural language system, Linguistic processing.

![](/api/attachments/ARZYMCWB/fulltext/images/e33e7a2626253a7a22f70ab774c9aa88b1303400d9f8ce3333d282512060c1b8.jpg)

Prof. Dr. rer. pol. Hermann Krallmann got his doctorate from the University Mannheim in 1975. Since 1980 he is head of the research unit "System Analysis and EDP" at the department of Computer Science at the Technical University Berlin. Main areas of research are Computer Aided System Analysis (RSA) and Computer Aided Work Place (RAP). He is also editor of the magazine "CIM Management" (Oldenbourg Verlag, Munich). He is managing director of the Institute for nology (IMT Berlin GmbH).

Management and Technology (IMT Berlin GmbH).

![](/api/attachments/ARZYMCWB/fulltext/images/a64f46785dc2849e99f6d6b26f09402a6a06c4b24b0b8e4993080cdc87d75582.jpg)

M. Sc. (USA) Ruth Marzi studied Computer Science at Bonn University. With a scholarship for the University of Kansas, Lawrence, Kansas she got a Master of Science in Computer Science. For one year she worked as a lecturer in Computer Science at the University of Missouri, Kansas City. Since 1986 she has been working as an assistant at the Technical University Berlin in projects and teaching.

## Introduction

In this paper the portion of the program system VESPRA developed at the Institute of Quantitative Methods of the Technical University Berlin is presented. VESPRA (Verarbeitung von gesprochener Sprache mit einfacher Syntax und Semantik zur Steuerung von Informations- und Leitsystemem/Processing of Speech with Simple Syntax and Semantics for the Direction of Information-and Control-Systems) is a system that uses methods from several different areas to enhance the recognition of isolated words. So, pre-processing and post-processing algorithms for a speech recognizer were developed. Whereas the pre-processing deals with noise reduction, the post-processing is based on methods from the area of Artificial Intelligence. The input is checked for its linguistic properties in order to determine the intended meaning of an utterance.

The planned applications incorporate the control of non-safety-sensitive functions of a car, a voice-mailbox system and an integrated office environment. The system is implemented in Whitesmith's C [1] on a VME-Bus system under the operating system VersaDOS [2].

## 1. Architecture of the VESPRA-System

The program system VESPRA altogether consists of 12 functional units (FU) (fig. 1).

FU1 comprises the potential endusers. Depending on the actual application a user can be a car driver, a secretary, a clerk or a telephone user. The applications are developed by the industrial partners Daimler Benz, Nixdorf and SEL respectively. The speech signals enter through the microphones (FU2). The system manager (FU3), which is the master, calls up FU4 (noise reduction). Via a PCM line the signals reach the speech processor (FU5). This unit is capable of speech recognition as well as speech synthesis. Synthesized messages are output through a loud speaker (FU8). The flow of data and control is mainly directed by the system manager. FU6 is the intelligent part of the system. The input is checked for its syntax, semantics and pragmatism. The most likely meaningful and executable action is then passed on to the interface to the application (FU7). Two distinct environments are created. The first is for the ordinary use of the system, whereas the second is for testing the complete system or single components.

![](/api/attachments/ARZYMCWB/fulltext/images/53a4ceeb37deb2c3c61f9b803760d712f67874d300bd2a657d831d81c4fbcdd8.jpg)  
Fig. 1. Architecture of the VESPRA-System.

As long as the system is being tested, the responsible person (FU12) works in a specially designed environment (FU11), which is also part of the system manager. A specialist (FU10) designs the desired application. He is supported by a user friendly interface, the ADS (Application Development System, FU9). It resides on a PC-AT compatible system under MS-DOS. After generating the application using the ADS, the data is downloaded to the VME-Bus system under the operating system VersaDOS.

The main concern in this report lies in FU6, the part which deals with the intelligent post-processing of the spoken input, where the input is checked for its linguistic and pragmatical properties.

![](/api/attachments/ARZYMCWB/fulltext/images/c73a76421315d1419a6b23173a64b8e45bd82726ad9df1f08b8ae8f74607a939.jpg)  
Fig. 2. Components of the FU6.

## 2. Lexical, Syntactic, Semantical, Pragmatical Analysis

The FU6 is divided into 3 main modules (fig. 2):

1. Initialisation Module

2. Training Module

3. Postprocessing Module

These modules are called by the system manager depending on the state of the complete system (i.e. startup, training, ordinary use).

## 2.1. Initialisation Module

This module is called only once during the booting of the complete system. All data files necessary for the functioning of the FU6 are loaded. Furthermore, the data structures used are built and initialised.

## 2.2. Training Module

Before a speech recognition system can be used, all words have to be trained. The resulting patterns are stored as reference patterns in the system. Initially the whole vocabulary has to be trained. Later on the retraining of specific words might be necessary. The procedures for the training itself and the storing of new reference patterns are part of the speech processing unit. In FU6 it is decided, whether to start training/retraining at a specific point.

## 2.2.1. Training

Before a person can use the system, all the words necessary for a specific application have to be trained. For that purpose exists a file with the orthographic representation of the words. The user is given the words to be trained sequentially and has speak them once or several times. Depending on the speech recognizer, the whole vocabulary has to be trained in one session or can be trained in smaller chunks of words. Since the SEL speech processing unit [3] is used here, all words have to be trained contiguously in one session.

## 2.2.2. Retraining

Retraining can be started whenever it is obvious that certain words are generally not recognized well or often confused with other words.

Retraining can be initiated in two ways. The first way is for the user to indicate the desire for retraining of specific words, the other is for the system itself to initiate the retraining. In the latter case the main problem is to find criteria for the initiation of such a retraining. In order to determine whether a specific word needs retraining, some statistics have to be compiled. For this, three steps are necessary. First, the quality of the recognition of a word has to be measured, next the result has to be evaluated statistically and last, the retraining has to be initiated.

The data available here for any statistics is the scores of the hypotheses. The scores are measures for the distance of the recognized pattern from the reference pattern. In order to determine the quality of a set of hypotheses, a rating function is needed. Several aspects can be taken into consideration, such as the length of a word, or the relationship between the scores of the different hypotheses of one acoustic signal, or the absolute value of the score of one hypothesis.

There is a multitude of algorithms for the compilation of statistics [4]. For the kind of application here, methods such as arithmetic mean, method of gliding averages or exponential smoothing (levelling) seem to be suitable.

## 2.3. Postprocessing Module

This module is called most frequently, since it processes the spoken input during the ordinary use of the system (fig. 3).

After each acoustic signal a list of hypotheses is passed from FU5 to FU6 via the system manager. The control program within FU6 monitors the parallel processing of the hypotheses. It controls the storing of intermediate results and generates the data necessary for further processing. Control is then passed back to the system manager to fetch new data.

So, the input for this module is a list of hypotheses as to which word might have been uttered. This list is sorted according to the scores associated with the word hypotheses. Furthermore, the current state of the complete system is needed in order to determine which actions are possible at the given time.

The output from this module and its direction depend on the result of the processing of the recognized word sequence.

If a command is recognized correctly, the code for the resulting action is passed to FU7 (the interface to the current application). Correct recognition here means, the command is syntactically and semantically correct within the environment of the current application and the resulting action is executable according to the current state of the system. If for any reason it is not possible to determine a proper action from the utterance, a dialogue for clarification might have to be initiated and the output sentence has to be passed to the speech synthesis unit.

In general, speech synthesis takes place in FS5 (the speech processing unit). Certain applications, however, have their own speech synthesis unit. In this case the information as to the sentence to be output is passed to FU7.

![](/api/attachments/ARZYMCWB/fulltext/images/b974674d2a0bc32a67a97c6958e7d3b55c5967ccd73a0b4d8baf729fee8192a7.jpg)  
Fig. 3. The Postprocessing Module.

Structure

<table><tr><td colspan="2">IndexWord</td><td colspan="2">SynonymsIndexWord</td><td>SyntacticalInformation</td><td>SemanticalInformation</td></tr><tr><td>1</td><td>RADIO</td><td></td><td></td><td>type = object</td><td></td></tr><tr><td>2</td><td>CASSETTE</td><td>3</td><td>MUSIC</td><td>type = object</td><td></td></tr><tr><td>.</td><td>TWO</td><td></td><td></td><td>type = card__numb</td><td></td></tr><tr><td>.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>n</td><td>LOUDER</td><td></td><td></td><td>type = action</td><td>fits-to = RADIO,CASSETTE, MUSIC</td></tr><tr><td>.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>n + k</td><td>SWITCH_ON</td><td></td><td></td><td>type = action</td><td>fits-to = RADIO,CHANNEL;</td></tr><tr><td>.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>n + m</td><td>SWF1</td><td></td><td></td><td>type = channel_name</td><td></td></tr></table>

Fig. 4. Structure of the Lexicon.

The Postprocessing Module itself consists of three parts:

\- Parsing of the input using transition networks and a lexicon (syntax and semantics)

\- Solving of ambiguities (semantics)

\- Conflict recognition and conflict processing (semantics and pragmatism).

## 2.3.1. Lexicon

All words valid in a specific application are stored in a lexicon, which also contains associated syntactical and semantical information (fig. 4). The lexicon contains all the information necessary for the processing of words. Each entry contains the orthographic representation of a word, its index, synonyms, type, and semantical information.

Words are usually referenced by their index, which corresponds to the position of its entry in the reference list of the speech processing unit. Generally, all synonyms can be used interchangeably in the proper positions. The types of words do not follow the categories set in linguistics but can be chosen freely and are usually categorisations of the function a word has in a sentence. So, for example, the word 'close' has the type 'action'. Such type definitions allow words like 'louder' to be categorized as 'action', even though they are linguistically not verbs but adjectives in the function of an action (here the action of increasing the volume of, say, a radio). The purpose of semantical information is to recognize only meaningful sequences of words. Words do not have to carry any syntactical or semantical information.

Hidden from the user, associated with each entry are fields for statistics. They are necessary to determine time and extend of possible retrainings.

## 2.3.2. Networks

For the syntactic/semantic analysis of input transition networks (TNs) and reference objects (Refos) are used. Networks of complete sentences often have many branches, whereas those of ellipses are in general very simple (fig. 5) [5].

The networks consist of nodes and arcs. Each node represents a state in the parsing (not necessarily in a unique way). An arc denotes the transition between two nodes. The beginning node and the final nodes of a net are distinguished. Labels of arcs denote the condition under which a transition occurs. Such a condition can be the occurrence of a specific word in the input sequence or the membership of a word in a particular category. The nets are non-deterministic, meaning more than one arc can originate in a node.

If it is possible to successfully traverse a net from its beginning node to an accepting final node

General Net:

![](/api/attachments/ARZYMCWB/fulltext/images/3ef0664ce41590d55fded22447a474bfd25ebca565aee24b1c9183da881c3547.jpg)

General Net with
Specific Entries:

![](/api/attachments/ARZYMCWB/fulltext/images/bc6a50397a0566e7a7f24caf5bdfadc2e4b1cc2dfd0efde12d38addfa1b3d611.jpg)  
Fig. 5. Example of Networks.

using up the input sentence, the input is successfully parsed, and is considered to be correct.

During the processing of an input sentence temporary reference objects (refos) are built as side effects of a transition. These store vital information concerning the sentence so far parsed (fig. 6).

The parsing process is started as soon as the first list of hypotheses and scores is passed from

FU3 to FU6. All beginnings of possible paths in the networks are tried in parallel. The intermediate states reached after the successful traversing of paths are stored in a data structure. Control is then passed back to the system manager to enable it to fetch the next list of hypotheses. Due to syntactic or semantic constraints, paths in the networks can be abandoned during the further processing of words, whereas others can be ex-

Field: Contents:

Score

Score of the so far processed sentence

Sentence

Sequence of indices of words in the sentence

Flags

Internal flags for checking semantical consistency

Function Name    Name of the net connected with the sentence

Current Label Label of the current state in the net

Fig. 6. Structure of Reference Objects.

panded. Some networks can now be in a final accepting state. They represent the recognized sentences.

A command is considered to be complete, if an action can be initialised using the parsed words or if a timeout signal has been encountered.

The next step in the processing is to find out whether a recognized sentence represents an executable action.

## 2.3.4. Pragmatism

Once a sentence is parsed it has to be checked, whether the command is executable. The current state of the object affected by the input is inquired in order to find out whether the execution of the command is possible.

Associated with each command is the code, which represents the action to be initiated in the application. Is the recognized command executable, this code has to be passed to FU7, the interface to the application.

## 3. Conflict Processing

During every stage of the processing conflicts can be encountered. As far as possible they are solved.

## 3.1. Semantical Conflict

The user could have uttered an ellipsis referring to the previously spoken command (e.g. “louder”, “a bit further”). In order to be able to examine the pragmatic aspect of the command, it is necessary to complete such a sentence. The occurrence of an ellipsis is considered to be a semantical conflict, since the immediate processing of pragmatism is not possible.

To complete ellipses, a dialogue memory is used, where previously recognized utterances are stored. If it is possible to complete the utterance with the help of the dialogue memory, the pragmatism of the such completed sentence is examined.

Certain conflicts cannot be solved without the help of the user. In that case a dialogue is started to clarify the meaning of the utterance in question.

In some situations it might be advantageous not to attempt solving occurring conflicts at all. For example, if the utterances themselves are fairly short or an intelligent way of solving the conflict is not possible and therefore only standard dialogues are initiated. Furthermore, it could take comparatively long to solve the conflict, therefore in some cases it might be more advisable and acceptable to ask the user to repeat the utterance.

## 3.2. Dialogue Memory

In the dialogue memory the commands spoken by a user and later on executed are stored. Is it also possible to direct an application with input devices such as mouse, table, light pen u.s.f. these actions might have to be stored as well, since they can be referenced by the user (fig. 7).

![](/api/attachments/ARZYMCWB/fulltext/images/d9724e5940edcebc01ea47e1f6c74c5f98bada85bea1dba484148f35f7e42740.jpg)  
Fig. 7. Dialogue Memory.

## 3.2.1. Structure

The Dialogue Memory (DM) is a data structure, which contains varied informations.

Access routines to the DM are defined. Besides elementary operations, such as initialisation, there are operations to manipulate the structure itself, mainly to append new information and to extract or destroy existing information.

## 3.2.2.Contents

The Dialogue Memory is used to represent the sequence of previously recorded utterances. Each element in the DM represents one recognized and subsequently executed command. An element contains all necessary information on the specific sentence, such as the words appearing in the sentence, information of syntactical and semantic nature, and the network name and accepting node reached in the parsing of the sentence. All this information is needed to determine, whether this sentence has been referenced by an uttered ellipsis.

The Dialogue Memory is necessary to enable the processing of incomplete sentences. These sentences can be either syntatically or semantically incomplete. Syntactically incomplete sentences (ellipses) refer to previously uttered commands. In order to process ellipses, they have to be made syntactically complete. In order to achieve this, the DM is needed. With the currently uttered ellipsis and the knowledge of previously excited commands it is possible to fill in the missing components of the sentence.

A sentence, which is semantically incomplete, is ambiguous. Ambiguity can be resolved in two ways. One is use the DM for completing the sentence. The other is to assume default values. Default assumptions have to be determined empirically, since there is no guarantee that in all cases the speaker's intention is met. In the majority of cases though it might enable fast processing and avoidance of unnecessary clarification dialogues.

## 4. Utilities

In order to eliminate access to datafiles during run time, programs have been written to generate C source code, which can be compiled and linked beforehand into the system.

This way, execution time is not unduly slowed down by file accesses, on the other hand application-dependent data can be changed easily.

Besides the generation of smaller routines, lexicon and nets specifically are treated this way.

## 4.1. Lexicon Compiler

The lexicon can be generated and edited using an ordinary editor. After generation, the lexicon is compiled by a lexicon compiler either into binary form or into C source code. The latter solution is appropriate for applications, which do not have a hard disk available. The lexicon is loaded during initialisation of the VESPRA system, or linked as a module.

## 4.2. Netcompiler

The networks for a particular application are compiled from a net-oriented representation into C-source code by a program. The name of the network, the states and the condition for the traversing of an arc have to be given. Additional parameters, side effects or actions can be given, too. Standard-code necessary for the correct processing of the networks is incorporated during the compilation process. The result is C-source code, which is linked together with all the other modules necessary for one application.

## 5. Conclusions and Acknowledgements

This report describes the work of an ongoing project. Not all the ideas presented here have been completely incorporated and implemented. Especially the area of conflict solving requires still a considerable amount of work.

The research underlying this report was partially funded by the Federal Ministry of Research and Technology of the Federal Republic of Germany (BMFT Förderungskennzeichen 413-5839 ITM 8701A9). Project partners are Daimler Benz AG, Stuttgart, SEL AG, Stuttgart, and Nixdorf AG, Berlin; subcontractor is the Technical University Berlin, subcontractors thereof the Technical University Karlsruhe and the Fraunhofer Gesellschaft (FhG/IAO), Stuttgart.

The responsibility for the contents of this report lies solely with the authors.

## 6. References

[1] C Language Manual, Whitesmiths Ltd., Version 3.2, August 1987.

[2] Motorola Microsystems, Technical Documentation Versa-DOS, September 1986.

[3] Beschreibung und Bedienungsanleitung der SEL-Sprach-

verarbeitungseinheit, Stuttgart, Februar 1988, internal document.

[4] Erwin Kreyszig, Statistische Methoden und ihre Anwendungen, van den Hoek & Ruprecht Verlag, Göttingen, 4. Auflage 1973.

[5] Patrick H. Winston, Artificial Intelligence, Addison Wesley, 1979.
