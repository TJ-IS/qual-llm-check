---
otero_id: 7982
otero_key: "JBF65J7S"
title: "Deriving knowledge representation guidelines by analyzing knowledge engineer behavior"
authors: "Cecil Eng Huang Chua; Veda C. Storey; Roger H.L. Chiang"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.038"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Deriving knowledge representation guidelines by analyzing knowledge engineer behavior

Cecil Eng Huang Chua <sup>a,</sup>⁎, Veda C. Storey <sup>b</sup>, Roger H.L. Chiang <sup>c</sup>

<sup>a</sup> Information Systems and Operations Management Department, University of Auckland Business School, The University of Auckland, Private Bag 92019, Auckland 1142, New Zealand <sup>b</sup> J. Mack Robinson College of Business, Georgia State University, Atlanta GA 30302-4015, USA

<sup>c</sup> Department of Operations, Business Analytics, and Information Systems, Carl H. Lindner College of Business, University of Cincinnati, Cincinnati, OH 45221, USA

## a r t i c l e i n f o

Article history: Received 7 July 2011 Received in revised form 6 April 2012 Accepted 21 May 2012 Available online 28 May 2012

Keywords: Knowledge engineering Knowledge representation Problem behavior graph Protocol analysis Theory of mental models

## a b s t r a c t

Knowledge engineering research has focused on proposing knowledge acquisition techniques, developing and evaluating knowledge representation schemes and engineering tools, and testing and debugging knowledge-based systems. Few formal studies have been conducted on understanding the behaviors and roles of knowledge engineers. Applying the theory of mental models, this paper describes a think aloud verbal protocol study to determine an empirical basis for understanding: (1) how knowledge engineers extract domain knowledge from textual sources; and (2) the cognitive mechanisms by which they engage various knowledge representation schemes to represent that knowledge acquired. The results suggest that knowledge representation is not simply a translation of acquired knowledge to a knowledge representation. Instead, it is an iterative process of selective querying of acquired knowledge, and continuous re<sup>fi</sup>nement of a model leveraging, not only on acquired knowledge from domain experts, but also from the knowledge engineer. From the <sup>fi</sup>ndings of empirical studies, a set of guidelines is derived to support the training and development of better knowledge representation schemes, representation processes, and knowledge engineering tools.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Knowledge-based systems fundamentally store organizational knowledge for retrieval and use, thus providing a way to preserve it independently of an organization's experts [2]. A fundamental challenge is the representation of knowledge to support reasoning and understanding [22], but knowledge representation continues to be a challenge [33].

Knowledge engineering, the process of developing a knowledgebased system, involves three main steps: knowledge acquisition, knowledge representation, and implementation [52]. Knowledge representation schemes capture knowledge in a form that can be used by an information system. Familiar types of knowledge representation include conceptual graphs [50] and ontologies [28].

Knowledge representation requires: (1) a domain expert who provides the knowledge, (2) a knowledge-based system where the knowledge is stored, and (3) a knowledge engineer who extracts and encodes the expertise [54,57]. The goal of knowledge representation is to organize knowledge obtained from domain experts into a knowledgebased system, making the knowledge engineer a critical part of the knowledge engineering process.

A knowledge engineer must represent acquired knowledge in such a way that a human can understand it and a computer system can process it [14]. These are, in essence, fundamentally opposing requirements because humans and computers function in distinct ways. Given that these con<sup>fl</sup>icting requirements have not been reconciled, empirical research in the <sup>fi</sup>eld is needed.

Empirical knowledge representation research has attempted to bridge the gap between human and machine representation of domain knowledge [54]. Traditionally, empirical knowledge engineering research has focused on: (1) evaluating knowledge acquisition techniques [45], (2) developing and evaluating knowledge representation languages and knowledge engineering tools [10,27,28], and (3) building and testing knowledge-based systems [11,15,44]. However, little research has studied how knowledge engineers actually perform knowledge representation work employing knowledge representation languages. Empirical research has been in the form of exploratory surveys [e.g., 8,36,61] or an analysis of researchers’ personal experiences and observations [e.g., 56,60].

Rigorous studies in a controlled environment, where researchers observe how knowledge engineers actually perform knowledge representation, are still needed. This research draws upon the theory of mental models [17,18,24] to explore the roles and behaviors of knowledge engineers in the knowledge representation process. The objectives of this research are to determine an empirical basis for understanding (1) how knowledge engineers extract domain knowledge and (2) the cognitive mechanisms by which they engage various knowledge representation schemes to represent the knowledge acquired. We <sup>fi</sup>nd that knowledge representation is not simply a translation of acquired knowledge into a knowledge representation. Instead, it is an iterative process of selective querying of acquired knowledge, and continuous re<sup>fi</sup>nement of a model leveraging not only on acquired knowledge from domain experts, but also from the knowledge engineer.

The paper proceeds as follows. Section 2 reviews existing work on knowledge representation and the theory of mental models. Section 3 presents our research method. Section 4 elaborates on the protocol analysis and the problem behavior graph derived from the empirical studies’ results. Section 5 discusses the <sup>fi</sup>ndings and proposes guidelines for the knowledge representation process and training of knowledge engineers derived from the empirical <sup>fi</sup>ndings. Concluding remarks are found in Section 6.

## 2. Knowledge representation

This section reviews prior research on empirical investigations of knowledge representation to demonstrate that systematic empirical work in the <sup>fi</sup>eld is required. We then draw upon research on the theory of mental models to outline an initial process model of knowledge representation.

## 2.1. Empirical knowledge representation research

Empirical work on knowledge representation is of two types: (1) exploratory surveys, and (2) personal case studies.

Exploratory surveys employ survey instruments and exploratory factor analysis. These studies abstract the results of numerous projects into a small number of dimensions. They, therefore, do not capture much of the rich information on what actually happens during the knowledge representation process. Although exploratory surveys can identify problems and mismatches between knowledge representation practice and theory, they are unable to critically examine why knowledge engineers encounter problems. Byrd [9], for example, discovered that knowledge engineers viewed knowledge acquisition as particularly challenging. However, his survey instrument could not identify ways to improve knowledge acquisition. Mykytyn et al. [36] identi<sup>fi</sup>ed four generic knowledge engineering roles: technical (designing and developing the knowledge‐based system), external (acting as a salesperson, troubleshooter), negotiation (communicating with the domain expert), and organizational (system documentation). Of these roles, only the technical role deals with knowledge representation per se. The other roles deal with managerial and non-technical aspects of the knowledge engineer's job.

Personal case studies provide rich insights into individual dif<sup>fi</sup>culties that researchers have using a knowledge representation scheme for a speci<sup>fi</sup>c project. Welty [60], for example, found that different knowledge engineers believe certain concepts should merit more details than others during knowledge representation. Stephens and Huhns [51] asked 55 subjects to represent the domain of ‘people using the DAML knowledge representation scheme. The subjects produced 55 distinct ontologies. Uschold et al. [55] found that fundamental differences between distinct knowledge representation schemes made them incompatible. Davis et al. [14] observed that many knowledge representation articles:

… contain claims of how the author was able, through a creative, heroic, and often obscure act, to get a representation to do something …

These observations suggest that knowledge representation schemes are not necessarily aligned with knowledge representation work [5].

Personal case studies, by their nature, re<sup>fl</sup>ect the subjective experiences of the researcher, and should be validated by rigorous studies.

## 2.2. Mental models of knowledge representation

The proper design of conceptual models requires understanding and representing human mental models [39,40]. The theory of mental models posits that humans think by forming representations of the world in their minds [17,18,24]. When humans are called upon to perform a task, they create incomplete models of the basic elements of the task problem and manipulate them in the mind. The end result of that manipulation guides human decision making [24]. Given knowledge representation can be regarded as a form of conceptual modeling so, in turn; mental models should in<sup>fl</sup>uence the knowledge representation task.

The actual structure of a representation relies upon a human's prior experience and background in addition to the information given for the task problem. The representation itself may be in<sup>fl</sup>uenced by the presented structure of the problem (e.g., which words appear <sup>fi</sup>rst), but does not need to correspond to the problem structure. Thus, a person asked to remember “The animal ran towards the bush,” may instead recall “The wolf ran towards the bush” [17,18].

In knowledge representation, the person (analyst, designer, and modeler) must acquire knowledge about a domain and map it to a pictorial artifact. This is done using a conceptual modeling scheme, which is a language designed for that purpose. Human beings manipulate the world as mental models, suggesting that modelers do not map directly from an acquired domain to a model. Instead, modelers move through an intermediate step of representing the domain as a mental model, before translating that mental model into the artifact [37,62].

The intermediate step of mental model creation is likely to create distortions in acquired knowledge [17]. The mental models literature points out that: (1) mental models represent, not only information about the stated problem, but also the context and other information the problem solver draws upon based on his or her own experiences; and (2) mental models are simpli<sup>fi</sup>ed views of reality [25]. Thus, even if the modeler accurately captures knowledge from the domain, the mental model the modeler develops will include information from his or her own background, and exclude information the modeler deems irrelevant.

In addition, distortions to acquired knowledge result from incompatibilities between the mental model and conceptual modeling scheme. The problem space, or the mental model of a knowledge domain to be represented, is very different from the design space of the knowledge representation scheme [20,39,42]. An understanding of the problem space requires domain knowledge [6], whereas an understanding of the design space requires technical knowledge, such as knowing the syntax of the knowledge representation scheme [48]. The syntax of the conceptual modeling scheme can make the mapping of the mental model to the scheme more or less dif<sup>fi</sup>cult [46]. An ideal scheme should map as closely as possible to the mental model [34]. A one-toone correspondence between constructs in the modeling language and the mental model is preferred [43,59]. However, given our limited understanding of knowledge engineers’ mental models, the <sup>fi</sup>t between existing knowledge representation schemes and knowledge engineers mental models is likely to be poor.

Based upon the above discussion, Fig. 1 shows the process we infer that knowledge engineers follow when generating the knowledge representation artifact. Here, the knowledge engineer does not simply translate acquired domain knowledge into the artifact. Instead, the knowledge engineer combines his or her acquired domain knowledge with his or her prior experience to create a mental model. In the process of translating acquired knowledge into the mental model, some knowledge will be lost. The knowledge engineer's prior knowledge also shapes the mental model such that it differs from acquired domain knowledge. The knowledge engineer then attempts to translate the mental model to the knowledge representation artifact. Mapping irregularities in the process leads to further distortions.

![](/api/attachments/JBF65J7S/fulltext/images/46c1a38b24004e9176640138fd96aca056b135306b8e9709565145ec2cdfa0be.jpg)  
Fig. 1. Knowledge representation through mental models.

## 3. Research method

A protocol analysis study was developed and conducted to analyze how knowledge engineers perform knowledge representation work and to empirically validate the model in Fig. 1. Protocol analysis is a commonly employed technique to examine the interaction between humans and artifacts [16,29,53,58]. Subjects perform a prede<sup>fi</sup>ned task while thinking aloud (that is, verbalizing their thoughts and actions). These thoughts and actions are coded by the researchers as a set of protocols (i.e., standard actions) [16]. Protocols can be de<sup>fi</sup>ned a-priori through a review of the literature, or developed in a grounded manner by identifying common actions in the data [53]. Because protocol analysis is performed in a laboratory setting, it is typically applied to focused tasks, such as programming, or code comprehension [1,26,29,42,53].

One objective of protocol analysis is to reverse engineer subjects’ thought processes to generate a problem behavior graph (PBG). A PBG depicts the thinking of subjects when performing an activity. In a PBG, the protocols derived in the protocol analysis are linked by the frequencies of the protocols’ co-occurrences in temporal order [16,58].

A PBG depicts a set of processes, and, therefore, can be represented in any process notation. For example, von Mayrhauser and Vans [58] developed PBGs illustrating the processes of software maintenance, choosing to illustrate these as Finite State Automata (FSA). An illustrative process is their “integrate partially understood material” (see Fig. 2). The maintainer begins by reading code. If the maintainer does not understand the code, he or she chunks and stores what was read, and continues reading. Otherwise, the maintainer identi<sup>fi</sup>es a beacon, chunks and stores it, and then continues reading.

In our study, the problem behavior graph of knowledge representation process is generated as follows. Subjects are assigned knowledge representation work, and perform that work while articulating what they are thinking (i.e., ‘think aloud’). Researchers analyze the ‘think aloud’ transcripts, and translate them into protocols. Protocols are ‘think aloud’ quotes classi<sup>fi</sup>ed according to a coding scheme. The transitions between the protocols are then employed to generate the PBG. The protocols represent knowledge representation tasks, and the PBG empirically depicts the thought processes. The PBG resulting from the protocol analysis study are intended to provide an in-depth understanding of the knowledge representation process.

This research presents the PBG using two notations, a reversed Finite State Automaton (FSA), and a <sup>fl</sup>owchart. In the reversed FSA, states are represented as arrows, and processes as circles. This notation is used to present protocol analysis results such as the frequencies of the states alongside an identi<sup>fi</sup>cation of the processes. Flowcharts are used in-lieu of an FSA, because <sup>fl</sup>owcharts have explicit decision constructs, and, hence, convey human decision making more clearly. The empirical study comprised four steps as illustrated in Fig. 3.

## 3.1. Sample selection

To select appropriate knowledge representation schemes, three criteria are considered: subject cognitive constraints, potential fatigue, and appropriateness for the study's purpose. Protocol analysis is cognitively demanding on subjects [16,26] so an attempt was made to minimize the dif<sup>fi</sup>culties by employing knowledge representation schemes that are generally easy to use. Furthermore, the knowledge representation schemes needed to be from distinct families to avoid biases resulting from the unique characteristics of a particular scheme and the representation schemes needed to <sup>fi</sup>t the purpose of the study. Three knowledge representation schemes representing distinct groups of knowledge representation were selected to ensure that the concept of knowledge representation was captured. Hospitality management was selected because we needed a domain that was simultaneously easy to understand, yet one that that would not be familiar to the subjects. The domain needed to be easy to understand to reduce the possibility of knowledge being miscommunicated to subjects. At the same time, the domain needed to be unfamiliar to ensure that subjects would act more as a knowledge engineer, not a domain expert. Section 3.1 summarizes the selection of study samples.

## 3.2. Study procedure

A laboratory study was conducted to empirically investigate how knowledge engineers perform their knowledge representation work. Subjects were asked to represent the concepts in an article on hospitality management and to ‘talk aloud’ while doing so. The articles served as a surrogate for the domain knowledge that the knowledge engineer needs to represent. We preferred articles over human domain experts, because domain experts were more likely to vary in performance. With a domain expert, we could not guarantee that the same information would be disseminated to different knowledge engineers by one domain expert at identical levels of quality.

![](/api/attachments/JBF65J7S/fulltext/images/907dfad5cdb7ee0fd4e7f1ddad9cab5ca4ca243eef756f3dccb4c24d4a4b5ab6.jpg)  
Fig. 2. Integrate partially understood material (von Mayrhauser and Vans [58]).

![](/api/attachments/JBF65J7S/fulltext/images/eeae5d5cc4ec47cf54427b66c9927d6601ee0fb7108c3c6a25db6e12e1bbf10d.jpg)  
Fig. 3. Empirical study framework.

Domain expert fatigue, personality interactions between a domain expert and a knowledge engineer, or other variables could have confounded results. By substituting an article for a domain expert, we could control that variability and, therefore, focus only on the dynamics of the knowledge engineer's work. The subjects’ verbalizations were recorded and transcribed. These transcripts were used to investigate the work performed by knowledge engineers and the possible roles they played during the knowledge representation process.

## 3.3. Coding scheme

Initially, the coding scheme for the protocol analysis was derived from the theoretical propositions in Section 2. However, these codes only partly re<sup>fl</sup>ected what actually occurred in the transcripts, so we needed to introduce new codes based on our transcripts before formally conducting the protocol analysis. Details on coding are provided in Section 3.3.

## 3.4. Protocol analysis

The protocol analysis was conducted to obtain <sup>fi</sup>ndings based on the roles of knowledge engineers and the knowledge representation process. Two independent raters mapped subjects’ talk aloud verbalizations to the coding scheme established. These two raters independently analyzed the transcripts using the coding scheme. They achieved a statistically satisfactory inter-rater agreement. The raters were then asked to reconcile their coding differences. A problem behavior graph (PBG) was generated from the reconciled coding results to depict the thought processes of subjects as they perform knowledge representation work. Section 3.4 elaborates on the analysis procedure, while Section 4 presents statistics, including inter-rater results.

Table 1 presents the activities performed in our study and the justi<sup>fi</sup>cation for each. The following subsections discuss the procedures undertaken in this research in detail.

## 3.5. Sample selection

The study employed a small sample size so that a thorough analysis could be carried out. This required special care to be taken to select subjects and treatments [35]. There are three types of samples in this study: (1) knowledge representation schemes, (2) the knowledge domain, and (3) subjects.

## Table 1

Study activities and their justi<sup>fi</sup>cation.

<table><tr><td>Study activity</td><td>Justification</td></tr><tr><td colspan="2">Sample selection</td></tr><tr><td>Three distinct representation schemes</td><td>Derive underlying construct (knowledge representation).</td></tr><tr><td>Three distinct hospitality management articles</td><td>Derive underlying construct (hospitality management). Subjects had no familiarity with domain.</td></tr><tr><td>14 PhD students in Information Systems</td><td>Information systems background.</td></tr><tr><td colspan="2">Laboratory procedure</td></tr><tr><td>Pre-treatment interview</td><td>Determine subjects&#x27; prior knowledge of knowledge representation</td></tr><tr><td>Instruction in think aloud</td><td>Necessary to determine sequence of subjects&#x27; actions</td></tr><tr><td>Subjects receive all three schemes and articles.</td><td>Repeated measures-boost sample size</td></tr><tr><td>Randomly determined knowledge representation scheme/hospitality management article</td><td>Control for order effect</td></tr><tr><td>No time limit during reading</td><td>Control for language differences in subjects</td></tr><tr><td>Subject uses scheme to represent article while talking aloud</td><td>Elicit sequence of steps subject follows while performing knowledge representation. 30-minute time limit for performing exercise</td></tr><tr><td>Recording played &#x27;Please talk aloud&#x27; during exercise</td><td>Remind subjects to talk aloud</td></tr><tr><td colspan="2">Coding scheme development</td></tr><tr><td>Initial coding</td><td>Based on theory of mental models</td></tr><tr><td>Refined coding</td><td>Partial open coding to more fully explore how knowledge engineers create and refine knowledge representations</td></tr><tr><td colspan="2">Protocol analysis</td></tr><tr><td>Pre-coding of transcripts conducted by researcher</td><td>Infer patterns from data</td></tr><tr><td>Inter-rater reliability using two blind raters</td><td>Ensures coding not biased by researchers</td></tr><tr><td>Reconciliation of coding difference</td><td>Generate final list of codes for analysis</td></tr><tr><td>Generate problem behavior graph</td><td>Derive findings and depict the knowledge representation process.</td></tr></table>

## 3.5.1. Knowledge representation schemes

Three representation schemes were chosen to represent diverse aspects of knowledge representation, because prior research has demonstrated that three instances are required to elicit a construct [4]. In addition, with three schemes, subjects should not be overburdened.

The chosen schemes were SHOE [21], conceptual graphs [50], and the Conceptual Knowledge Representation Scheme (CKRS) [12]. These schemes were selected based on four criteria.

1. The scheme had an accepted graphical notation so subjects would not be required to write copious amounts of text to represent captured knowledge.

2. The scheme represented one or more perspectives of knowledge representation.

3. The scheme was suf<sup>fi</sup>ciently disjoint from the others to capture a wide spectrum of knowledge representation mechanisms.

4. The scheme could be adequately comprehended by subjects in a short time.

We chose these knowledge representation schemes, instead of more complex languages such as OWL [47] or RDF [32] because we wanted to study the process of knowledge representation. In more complex, dif<sup>fi</sup>cult-to-use schemes, knowledge engineers would spend an increased amount of time coping with issues of scheme syntax. That cumbersome scheme syntax interferes with knowledge representation processes is already known [14,41,55].

Furthermore, we avoided using a complex representation language so that the study could fully reveal the knowledge engineers’ behaviors; otherwise, the empirical results would be biased and confounded by the complicated constructs and features of the chosen languages.

## 3.5.2. Knowledge domain

The domain of this study needed to be one in which subjects had little organizational familiarity, so subjects would have to extract and refer to knowledge provided by a domain expert to perform knowledge representation work. However, it had to be one where subjects could easily understand how the domain operated. Since all subjects could relate to travel and attendant services, hospitality management was selected as a suitable domain. Nevertheless, much of the hospitality management industry relies on specialized knowledge to survive and thrive. For example, the design of the Disney theme parks and hotels is based around a carefully considered understanding of items and activities that particular sub-segments of the tourist population desire. Furthermore, the hospitality management industry is often not considered for exercises in knowledge representation. Thus, hospitality management was both a relevant and unfamiliar domain to our subjects, and, consequently, ideal for this study.

We employed published works on hospitality management as a surrogate for knowledge. Three excerpts, two from textbooks, and one from a magazine article [7,13,23] were provided for the subjects to represent. We employed published works to maintain the constancy of knowledge disseminated to subjects. A real domain expert's ability to transmit expertise could vary based on time, or situation. Just as three representation schemes were employed to capture the diversity of representation schemes, three excerpts from distinct hospitality management sources were employed to adequately capture the domain knowledge of hospitality management.

## 3.5.3. Subjects

Fifteen subjects, PhD students from the information systems department of a large public university, volunteered for the study. One subject (subject 6) was eliminated, because of an inability to perform think-aloud in English.

## 3.6. Study procedure

The fourteen subjects used three distinct knowledge representation schemes to capture and represent knowledge about hospitality management in a repeated measures design. In other words, each subject performed the same experiment 3 times. Subjects ‘talked aloud,’ to describe their thinking and actions as they performed the knowledge representation work. The activities involved were: pretest, data collection and transcription.

## 3.6.1. Pre-test

Prior to the study's commencement, subjects were informed that they would be involved in a knowledge engineering study. To control for hypothesis guessing, subjects were not provided details of the study or expected <sup>fi</sup>ndings. A pre-treatment interview was conducted using structured interviews to assess the subjects’ understanding of knowledge representation. Subjects were only able to de<sup>fi</sup>ne ontologies as they pertained to qualitative research. For the purpose of this research, ontologies are a technology that captures terms and their relationships relating to a particular application domain [19]— the word ‘ontology’ has distinct meanings in different research communities. No subject could de<sup>fi</sup>ne knowledge representation, or conceptual graphs. Thus, excessive subject expertise on a particular knowledge representation scheme did not bias the results. Subjects were then trained in performing think aloud using instructions and exercises adapted from Ericsson and Simon [16].

## 3.6.2. Data collection and transcription

Each of these 14 subjects participated in three separate sessions in a repeated measures design. In each session, a subject represented a randomly chosen article using a randomly assigned knowledge representation scheme. In total, 42 sessions were conducted and videotaped in the same room with identical instructions provided.

Subjects were given a 4-page tutorial detailing how to use each knowledge representation scheme. The tutorial was developed by the scheme's developers (e.g., [21,49]. As a manipulation check, subjects were asked to summarize the representation scheme and to represent either ‘Frog eats <sup>fl</sup>y’ or ‘Frog and <sup>fl</sup>y are animals’ using the scheme. Subjects were given a randomly chosen 3-page hospitality management article. After reading the article, subjects were asked to capture and represent knowledge in the article using the assigned knowledge representation scheme.

For each session, subjects had 30 min to represent the article while talking aloud. A reminder recording played ‘please talk aloud’ every 3 min. A thirty‐minute time limit was imposed to not overly inconvenience subjects. It was expected that subjects would not complete the whole exercise within the time frame. Subjects were allowed to end early if they desired. The researcher was not in the room for the exercise to prevent verbal or physical cues from contaminating the results.

On average, sixteen hours were required to transcribe each experiment session. A total of 457 pages of transcripts were recorded. These transcripts were the principal source of data for the protocol analysis.

## 3.7. Coding scheme

Fig. 1 presents our view of knowledge representation. From the model in Fig. 1, three protocols could be derived: (1) Employ Personal Knowledge, (2) Develop Mental Model and (3) Develop Artifact. The actual captured knowledge did not need to be in a code, given that it was represented in the article. In prior research on developing representations [1,42] argue that conceptual modelers not only create conceptual modeling artifacts, but also evaluate them for <sup>fi</sup>tness as well. This results in a fourth protocol, (4) Evaluate Model.

Our observations of the data revealed two additional protocols, as well as a re<sup>fi</sup>nement of the “employ personal knowledge” protocol. The two “grounded” protocols were derived from observations that subjects often interrogated the task, and chose between multiple criteria, thus leading to the (5) inquiry, and (6) choice protocols. The “employ personal knowledge” protocol was expanded, because we discovered subjects performing unexpected behaviors based on their personal knowledge. In protocol analysis studies, such re<sup>fi</sup>nements of protocols based on empirical data is well-accepted [53].

The final coding scheme, then, for the protocol analysis consisted of six protocols. Examples of verbalizations related to each protocol are presented in Table 2. Protocols were:

1. Personal Action. Originally, this code was “Employ Personal Knowledge.” We discovered from the data, however, that subjects not only would re<sup>fi</sup>ne the mental model based on personal knowledge (as predicted by the literature [17,18,24]), but would also deliberately omit acquired knowledge. Furthermore, we found subjects not only adapting their mental models, but also the knowledge representation scheme itself. Each of these three protocols (i.e., modifying mental model based on prior knowledge, omitting information, modifying knowledge representation scheme) by themselves occurred infrequently. We thus collapsed them into a single code.

2. Mental Model. The subject is translating the article into his or her mental model.

Table 2  
Example fragments and their assigned protocols.

<table><tr><td>Protocol</td><td>Subject</td><td>Scheme</td><td>Article</td><td>Fragment</td></tr><tr><td>1</td><td>14</td><td>1</td><td>2</td><td>Rooms and boards Tops and payments But then you don&#x27;t really get a sense of the growth</td></tr><tr><td>1</td><td>2</td><td>3</td><td>2</td><td>The interesting part is usually that a motel as opposed to a hotel would not offer dining Only one difference and besides its not in the article</td></tr><tr><td>1</td><td>5</td><td>1</td><td>2</td><td>Let&#x27;s say I don&#x27;t know geography</td></tr><tr><td>1</td><td>7</td><td>2</td><td>3</td><td>Ok so the travel manager is scared</td></tr><tr><td>2</td><td>10</td><td>3</td><td>3</td><td>Negotiate a deal Negotiate rental car objectives OK Procurement Manager Negotiates Negotiates Rental Car rental contract.</td></tr><tr><td>2</td><td>11</td><td>3</td><td>2</td><td>And Gerald Gerald Lattin writing Writing Write Write On history on history History</td></tr><tr><td>2</td><td>12</td><td>3</td><td>2</td><td>Lodging business Formed and or Influenced To say Political factors</td></tr><tr><td>3</td><td>13</td><td>1</td><td>1</td><td>To draw the whole tree I have a base ontology</td></tr><tr><td>3</td><td>14</td><td>2</td><td>3</td><td>Ok the first thing I&#x27;m going to do is find a way through here and highlight points that I want inside my conceptual graph I guess um</td></tr><tr><td>3</td><td>15</td><td>3</td><td>2</td><td>I identify some entities There&#x27;s no notation For their relationship</td></tr><tr><td>3</td><td>1</td><td>3</td><td>1</td><td>Ok So this is the resort hotel Is another concept</td></tr><tr><td>4</td><td>4</td><td>3</td><td>1</td><td>Let&#x27;s see if we can go back to convention hotels and make sure everything is there. Ok</td></tr><tr><td>4</td><td>7</td><td>1</td><td>1</td><td>This is incomplete the other one was incomplete too</td></tr><tr><td>4</td><td>8</td><td>2</td><td>2</td><td>That doesn&#x27;t make sense.</td></tr><tr><td>4</td><td>10</td><td>3</td><td>3</td><td>Oh I didn&#x27;t think I drew that right no I didn&#x27;t.</td></tr><tr><td>5</td><td>1</td><td>1</td><td>3</td><td>Single nation corporate ok?</td></tr><tr><td>5</td><td>2</td><td>2</td><td>1</td><td>What would be the term here?</td></tr><tr><td>5</td><td>3</td><td>1</td><td>3</td><td>Ok. What can I do? Where do I start?</td></tr><tr><td>5</td><td>4</td><td>2</td><td>3</td><td>What else?</td></tr><tr><td>6</td><td>5</td><td>2</td><td>1</td><td>Rather than running attribute as I did before I&#x27;ll say is</td></tr><tr><td>6</td><td>7</td><td>3</td><td>2</td><td>And this I consider it one domain and I should write it with a dotted line</td></tr><tr><td>6</td><td>8</td><td>3</td><td>3</td><td>So let me get rid of that.</td></tr><tr><td>6</td><td>9</td><td>2</td><td>2</td><td>Here I can&#x27;t draw it I would have the sign Here I would say repeat that option</td></tr></table>

3. Artifact. The subject is doing something related to developing a pictorial knowledge representation scheme.

4. Evaluate Model. The subject checks, reviews, or identi<sup>fi</sup>es something wrong with his or her work.

5. Inquiry. The subject is trying to discover something about the domain. He or she may be asking a question, or pondering an issue. It means that the subject identi<sup>fi</sup>es a problem.

6. Choice. The subject states that he or she is going to choose one of a set of alternatives. The alternatives may be implicit. This protocol was derived from the data.

All transcripts were coded at the fragment level. The following rules de<sup>fi</sup>ne a fragment:

• A fragment is a passage of the transcript that could be assigned one of the protocols.

• If two contiguous fragments have the same protocol, they are combined as one fragment.

• A fragment only has one protocol. If it has two protocols, it is split into two sub-fragments, each with only one protocol.

## 3.8. Protocol analysis

Two raters were recruited to code the transcripts independently using the coding scheme. The protocols assigned by raters were compared to determine the inter-rater reliability. The independent raters were asked to reconcile fragments with differing protocols. Raters continued to recode fragments with discrepancies until all discrepancies were resolved.

The reconciled protocols were employed to generate the problem behavior graph. Each of the six protocols represents a node in the PBG. Transitions between the protocols were measured in two ways: (1) simple count, and (2) average percentages.

## 3.8.1. Simple count

The number of times one protocol transitioned to the next was counted. For example, there were 169 transitions where “create or extend model” was followed by “inquiry,” and 154 transitions where inquiry was immediately followed by create or extend model.

• Average percentage: There was a high degree of variation in verbalizations across subjects. Some subjects were talkative; others were reserved. Some were native English speakers; others spoke English as a second language. A simple count could have been biased towards highly talkative, native English speakers. To adjust for this potential bias, the following measurement procedure was adopted. First, the total number of verbalization transitions for each subject/treatment combination was calculated. For example, subject 1/SHOE is one treatment combination, subject 1/conceptual graphs is another. Next, this number was employed as a baseline to convert all simple counts by subject/treatment to a percentage. For example, for subject 9/conceptual graphs, there were 17 transitions from ‘choice’ to ‘create/extend model’ out of 63 transitions. Thus, the average percentage of transitions from ‘choice’ to ‘create/extend model’ was 27.0% for this subject/treatment. The average percentage of verbalizations across subjects was then obtained.

## 4. Problem behavior graph

This section presents the protocol analysis results and the problem behavior graph derived from them. Subjects’ verbalizations were employed as qualitative evidence. A total of 2521 fragments were identi<sup>fi</sup>ed. After a pre-coding conducted by one of the researchers, fragments that did not map to the six protocols (e.g., fragments where subjects said “uh”) were eliminated. This resulted in 1748 fragments. These fragments were coded by the two independent raters. Inter-rater reliability was at acceptable thresholds (Kappa=0.832), clearly above generally accepted guidelines that kappa levels should be above 0.7 [31,35]. The raters reconciled the codes on fragments where they didn't agree. Of the 1748 fragments, 328 fragments had codes that were identical to the fragment immediately preceding them. Once these fragments were merged, 1420 fragments remained. Transitions between fragments were generated to calculate the frequency that each protocol transitioned to another.

The derived problem behavior graph was nearly saturated. Of the 30 possible kinds of transitions (i.e., 6 protocols can transition to 5 other protocols), 29 kinds of transitions were observed at least once. However, some transitions were substantially more frequently observed. For example, inquiry transitions to design space occurred 63 times. In contrast, inquiry transitions to evaluate the model occurred once. Table 3 presents simple counts and average percentage of transitions between protocols. Row values present the protocol transitioned from, and column values denote those transitioned to.

The correlation between simple counts and average percentages is 0.750. At the aggregate level (i.e., correlating Tables 3(a) and (b)), the correlation is 0.980. This result suggests there is no measurement bias in the simple counts. Fig. 4 shows the problem behavior graph derived from the protocol analysis results. It depicts the thought processes of subjects when performing knowledge representation work. Each protocol corresponds to a particular knowledge representation task. The derived PBG should be interpreted as follows. The protocol (knowledge representation task) ‘1. inquiry’ transitions to ‘4. problem space’ 74 times or about 6.7% of the time. Given that inquiry transitions to any non-inquiry protocol 192 times, if a subject was at inquiry, he or she is likely to then transition to ‘problem space’ 38.5% of the time.

Only transitions occurring more than 1% of the time are displayed in Fig. 4. The full PBG (i.e., including transitions of lower frequency) can be generated from the data presented in Table 3. However, the low frequency transitions are omitted, because they are insigni<sup>fi</sup>cant for the study. The analysis below elaborates on the <sup>fi</sup>ndings of each protocol. These <sup>fi</sup>ndings are representative across subjects. To illustrate and justify these <sup>fi</sup>ndings, subjects’ verbalizations are used as additional qualitative evidence. Quotes from separate subjects demonstrate the generality of the <sup>fi</sup>ndings. In the below section, we explain the manifestation of each protocol from left to right, top-down based on Fig. 4.

## 4.1. Inquiry (Protocol 5)

The protocol analysis study reveals that inquiry is important when subjects perform knowledge representation work. Inquiry takes up slightly more than 10% of the subjects’ knowledge representation work. The main function of inquiry appears to be directing subjects’ activities. Inquiry would often lead to three knowledge representation tasks: the choice (41 times), the mental model (74 times), and the knowledge representation (63 times). Inquiry appears to focus the subjects on particular aspects of knowledge to be represented, or speci<sup>fi</sup>c constructs in the knowledge representation scheme.

Table 3  
Satisfactory counts and average percentage of transitions.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td colspan="7">(a) Simple count</td></tr><tr><td>1</td><td></td><td>20</td><td>35</td><td>0</td><td>14</td><td>17</td></tr><tr><td>2</td><td>13</td><td></td><td>169</td><td>8</td><td>83</td><td>71</td></tr><tr><td>3</td><td>40</td><td>173</td><td></td><td>27</td><td>65</td><td>128</td></tr><tr><td>4</td><td>3</td><td>8</td><td>20</td><td></td><td>5</td><td>6</td></tr><tr><td>5</td><td>13</td><td>74</td><td>63</td><td>1</td><td></td><td>41</td></tr><tr><td>6</td><td>19</td><td>77</td><td>154</td><td>6</td><td>25</td><td></td></tr><tr><td colspan="7">(b) Average percentage</td></tr><tr><td>1</td><td></td><td>1.9</td><td>1.6</td><td>0</td><td>0.9</td><td>0.8</td></tr><tr><td>2</td><td>0.9</td><td></td><td>13</td><td>0.7</td><td>7.4</td><td>6.3</td></tr><tr><td>3</td><td>2.2</td><td>12.8</td><td></td><td>1.6</td><td>3.6</td><td>8.8</td></tr><tr><td>4</td><td>0.1</td><td>0.3</td><td>1.2</td><td></td><td>0.3</td><td>0.4</td></tr><tr><td>5</td><td>0.5</td><td>6.7</td><td>4</td><td>0</td><td></td><td>2.6</td></tr><tr><td>6</td><td>1.5</td><td>7.9</td><td>9.8</td><td>0.3</td><td>1.7</td><td></td></tr></table>

1 Personal action.  
2 Mental model.  
3 Artifact.  
4 Evaluate model.  
5 Inquiry.  
6 Choice.

Subject 3: What is medium of exchange?

Subject 13: How do I represent that?

The high percentage of inquiry transitions also suggests that sub jects take an active role in determining what knowledge to extract. Subjects generally capture and represent the knowledge of the assigned article in order of its presentation. That is, knowledge from the <sup>fi</sup>rst paragraph is represented <sup>fi</sup>rst, followed by knowledge from the second paragraph. However, subjects do not passively capture knowledge from the article. Instead, they raise questions about the article and the application domain, and then self-answer those questions to guide their knowledge representation process.

Subject 9: But Marks Clarks who's that? Mark Clark he's ah … and there's AVIS and supplier And Mark Clark works for AVIS. He sits with AVIS

The initial set of questions subjects ask has a strong in<sup>fl</sup>uence on the knowledge they choose to capture. Subjects employ a sampling technique similar to snowball sampling [30] by asking a question about the application domain, self-answering the question, and asking yet another question. The second question subjects ask would be highly related to the <sup>fi</sup>rst. Thus, knowledge that subjects have already represented will be used to identify further knowledge in the article to capture. Domain knowledge highly related to knowledge captured is, therefore, more likely to be captured than knowledge unrelated to what has already been captured.

The inquiry task also appears to be driven by the constructs provided by the knowledge representation scheme. The quote below illustrates the subject using conceptual graphs, which has two main constructs, concepts and conceptual relations (i.e., relationships). In the quote, subject 8 is looking for a conceptual relation to connect two concepts (‘rented by’ and ‘inn’). Thus, the subject is searching for something in the article, because the representation scheme suggests that something should be there.

Subject 8: Can't figure out what to use between rented by and inn. Now that I switch my rented by to a concept I need something between rented by and inn

## 4.2. Choice (Protocol 6)

The protocol that most frequently transitions to and from choice is artifact. Choice transitions to artifact 154 times, and artifact transitions to choice 128 times. In contrast, choice transitions to and from the next most frequently transitioning task, mental model, 77 and 71 times respectively. Often, subjects follow the natural choice supported by constructs of the knowledge representation scheme. For example, SHOE encouraged subjects to think of knowledge in a hierarchical manner.

Subject 4: First of all try to organize categories try to categorize the things we learned from the article

Similarly, for conceptual graphs, subject 5 chooses to create (and therefore <sup>fi</sup>nd) separate relationships between the cities, because that is what conceptual graphs demand.

![](/api/attachments/JBF65J7S/fulltext/images/e986b778ca84bfd184fd05af12f8a3712a14acc5d13fda9c027f27aab68c873b.jpg)  
Fig. 4. Problem behavior graph of knowledge representation process.

Subject 5: I can't put all the cities on it because they're not related to the concept being represented. So I'll have to have a separate example relationship for each city.

That choice appears to transition to the artifact more than the mental model suggests the dif<sup>fi</sup>culty of translating mental models to the knowledge representation scheme (i.e., artifact); the decision making (i.e., choices) associated with absorbing knowledge and creating a mental model are straightforward, implicit, and thus are not uttered by subjects. In contrast, the decision making associated with translating a mental model into a knowledge representation artifact is dif<sup>fi</sup>cult, and hence explicit and uttered by subjects.

## 4.3. Personal action (Protocol 1)

Personal action is the second-least occurring knowledge representation task. It only appears 97 times. While it is not frequent, it is an interesting and signi<sup>fi</sup>cant behavior of knowledge engineers, because it suggests that subjects perform some type of action to defer solving the problem directly such as: (1) creating new notation not found in the knowledge representation scheme, (2) not representing something he or she knows is present, or (3) adding domain knowledge not found in the article. Adopting alternative solutions is a common reaction of humans.

## Subject 7: I missed one but don't worry about that

These actions often result from the knowledge representation scheme's constraints and limitations. Subjects often found it dif<sup>fi</sup>cult to use the assigned scheme to represent something. The most likely task to transition to personal action is the artifact (40 times). The next most likely task (choice) transitions to personal action 19 times. In other words, the artifact protocol is twice as likely to transition to personal action as the next most frequent task. Qualitative evidence also suggests that the knowledge representation scheme in<sup>fl</sup>uences what the knowledge engineer will capture. The quote below shows a subject deliberately not representing some knowledge, because it was dif<sup>fi</sup>cult to do so.

Subject 2: Here this seems kind of complicated. Complicated. Skip this for a while and go to monasteries.

As predicted by the mental models literature [24], subjects apply and include their own knowledge into the mental model and hence the knowledge representation artifact. In the below quote, subject 2 represented the distinction between a hotel and a motel according to the subject's own understanding of the domain, which is not in the assigned article.

Subject 2: The interesting part is usually that a motel as opposed to a hotel would not offer dining. Only one difference and besides it is not in the article.

## 4.4. Mental model (Protocol 2)

In examining the transitions between the mental model and artifact, subjects spend only slightly less effort overall on the mental model than the artifact. Furthermore, there are 157 (74+83) transitions between inquiry and mental model, but only 128 (63+65) transitions between inquiry and artifact. In other words, subjects are more likely to ask a question about the domain, than ask a question about how to represent it. In a world where subjects just translate knowledge to a knowledge representation scheme, this should not happen. That it does happen suggests the importance of subjects’ mental models.

We observed subject mental models impacting the knowledge representation process in three ways. First, subjects would prioritize knowledge in the text. The subject would be sensitized to certain ideas over others, which correspondingly biased the ideas the subject would capture in the knowledge representation.

Subject 1: the motel lodging place is a one interesting topic And the other one is that if we treat hotel the lodging place as the hotel motel the lodging place as the theme. The other interesting relationship well is the road is the vehicle

Second, in the same way subjects would ask related questions during inquiry, subjects would also expand on prioritized knowledge when developing their mental model. Thus, knowledge connected to existing knowledge was more likely to be represented than unrelated knowledge. In the quote below, the subject is searching the article for information on employees. The subject is expending effort <sup>fi</sup>nding this information instead of modeling something that can be quickly picked from observation.

Subject 15: I don't know what to say about employees … Traditional hotels offer their employees most challenging opportunities. …

Finally, subjects would reorganize knowledge in ways the text did not suggest.

Subject 2: Well maybe If we if we see hotel as the more general term we could include motel and everything inn as a synonym of [subject breaks into silent thinking]

Subjects frequently transition between the mental model and the artifact. This suggests that the two are closely intertwined. To accurately perform the technical task (i.e., artifact), subjects must <sup>fi</sup>rst understand domain knowledge. It appears as if it is not possible to be a knowledge engineer without <sup>fi</sup>rst having some basic knowledge of the target domain.

## 4.5. Artifact (Protocol 3)

The artifact protocol is the one most frequently encountered. Subjects most frequently enter or exit the artifact protocol via means of three other tasks, the inquiry (63+65), choice (35+40), or mental model (19+173). This suggests that subjects <sup>fi</sup>nd the other three tasks important for understanding and developing representations in the artifact.

The qualitative evidence supports this conjecture. Even when subjects enact the artifact protocol, they often raise issues related to inquiry, choice, or mental model. The three examples below are coded as the artifact by the independent raters. Nevertheless, one can observe aspects of inquiry, choice, or mental model in the quotes. Subject 9 is asking how one expresses a particular piece of knowledge using a representation scheme (i.e., inquiry):

## Subject 9: Not sure how to express that.

De<sup>fi</sup>nitely, the process of translating knowledge in the article into the knowledge representation artifact is non-trivial. Subjects often have to interpret and derive meaning from knowledge, before they can adequately represent it. In the example below, the subject has made a choice as to how such knowledge is represented.

Subject 11: I will interpret the one two three four five six five or five relationships to one whole relationships.

Finally, subjects’ own personal knowledge in<sup>fl</sup>uenced the representation. Subject 12, obviously, knows that an employer is a kind of person.

Subject 12: Ok maybe higher level than employer instead of employer we have people. People include …

This is not to say the artifact protocol was always qualitatively similar to the three other protocols. In most instances, subjects engaged in the artifact protocol enacted traditional behaviors associated with conceptual modeling such as generalizing or instantiating knowledge, or assigning certain kinds of knowledge as properties of other kinds of knowledge.

Subject 4: These resort hotels have large spreads, so that is another property

That subjects engaged in this kind of behavior was interesting, especially since the knowledge representation schemes often did not have these constructs.

## 4.6. Evaluate model (Protocol 4)

Although the subjects evaluated their representations, they spent very little time doing so. This may have been associated with the study design, since subjects had only 30 min to perform their knowledge representation work. However, the pattern of transitions to and from the evaluation model protocol suggests that model evaluation in knowledge representation is consistent with similar research in related <sup>fi</sup>elds [1,38]. Subjects iterated between the mental model and artifact to develop their knowledge representation. Subjects then reviewed their representations to identify gaps, or to determine if there were syntactic irregularities.

Subject 4: Let's see if we can go back to convention hotels and make sure everything is there. Ok.Subject 1: However I'm not very confident of the first one because for the first one all the relationships are the same but show them many many times.

The model evaluation task only occurs after the artifact is ‘moderately mature.’ By this, we mean that subjects do not evaluate their artifact design immediately after extending the result by a small amount. Instead, subjects will (for example) represent all the knowledge in one to three paragraphs before evaluating their artifact for readability. Model evaluation will also most frequently transition to and from the artifact protocol.

## 5. Discussion

The results of this study: (1) provide insight into the actual process of knowledge representation; (2) suggest hiring and training guidelines for knowledge engineers; and (3) generate guidelines for developing better knowledge representation schemes.

## 5.1. Knowledge engineering process

The protocol analysis results suggest that the protocol one most frequently transitions from is the mental model (over 28 percent). This protocol transitions mainly to inquiry, choice, and the artifact. Qualitative results of the protocol analysis also suggest that knowledge engineers would avoid representing designs if the design was dif<sup>fi</sup>cult to do in the scheme. Finally, evaluation of the model designed usually occurred after a design was enacted.

In short, the problem behavior graph derived from the <sup>fi</sup>ndings and our understanding of the nature of each protocol in the problem behavior graph suggests the process presented in Fig. 5. The <sup>fi</sup>rst thing a knowledge engineer asks is, “What knowledge do I need to represent?” (inquiry to mental model). Once the knowledge engineer captures knowledge, the knowledge engineer then asks whether the knowledge can be easily represented. If so, the knowledge engineer represents it using the scheme (artifact). If the knowledge cannot be easily represented, then the knowledge engineer decides whether captured knowledge must be changed to <sup>fi</sup>t the representation scheme, whether the representation scheme should be changed to <sup>fi</sup>t the knowledge, or whether the knowledge should be ignored (evaluate model, choice, and personal action). After a certain number of iterations with the scheme that varies across knowledge engineers, the knowledge engineer reviews the work performed, and corrects it.

The knowledge representation process derived from the empirical <sup>fi</sup>ndings suggests the complexity of the cognitive process in the knowledge engineer. The knowledge engineer does not just simply translate knowledge from the domain expert. The knowledge engineer must also make choices, function as a domain expert, and probe both the domain and design space with queries.

## 5.2. Hiring and training

The research <sup>fi</sup>ndings have signi<sup>fi</sup>cant implications on the hiring and training of knowledge engineers.

Our <sup>fi</sup>ndings suggest that knowledge engineers do not just trans late knowledge to the artifact, but that knowledge engineers are involved in organizing, prioritizing, and creating knowledge. These <sup>fi</sup>ndings suggest that organizations must not only consider the technical competence of the knowledge engineer, but also his or her domain knowledge. A knowledge engineer with a good understanding of a domain, but moderate to weak technical skills, may be better than one with strong technical skills, but little understanding of the domain. Because understanding a domain requires a great deal of effort, the time savings become signi<sup>fi</sup>cant. Furthermore, a knowledge engineer with domain knowledge would be better able to correctly organize, prioritize, and create knowledge. From a training perspective, the <sup>fi</sup>ndings suggest that knowledge engineers should be trained with appropriate techniques for soliciting knowledge. Improper inquiry will affect the scope and quality of the knowledge captured and presented.

## 5.3. Design of knowledge representation schemes

Our <sup>fi</sup>ndings suggest the following three distinct guidelines for the design of better knowledge representation schemes.

Knowledge representation schemes must allow iteration and refinement. Knowledge engineers iterate both between the mental model and artifact, and between the artifact and evaluation. This means that the knowledge representation scheme must be easily editable. Other research (e.g., [14,51] suggests that knowledge representation schemes are not easily editable. For example, one must often restructure large segments of hierarchical schemes such as taxonomies when new knowledge is added.

Knowledge representation schemes must be ‘knowledge neutral.’ The scheme must provide enough constructs so that the knowledge engineer can easily represent any kind of knowledge he or she wishes to represent. A failure to do this means that the knowledge engineer will engage in aberrant behavior. The knowledge engineer may avoid representing some kinds of knowledge, or may introduce new notation to represent what he or she is trying to capture. Evidence from prior research suggests that knowledge representation schemes are not ‘knowledge neutral’ [55,56]. It is easier to represent some kinds of knowledge in certain schemes than in others.

Knowledge representation schemes must be easy to use. It is not suf-<sup>fi</sup>cient for a knowledge representation scheme to be knowledge neutral. The constructs in the scheme must also be easy to use, or the same problems of aberrant behavior will arise. It should not be necessary for knowledge engineers to engage in ‘heroic’ practices [14] to represent what they want to represent.

## 5.4. Study characteristics and limitations

This study was conducted under laboratory conditions. The problem and limitations of a controlled environment include the fact that the setting lacks realism (traded off against control and precision). The subjects worked from a paper description. The subjects spent, at most, 30 min on their work, so it is possible that they would behave differently if they had no time limit and could interact with a true domain expert. However, most systematic studies of information systems design (e.g., the use of Entity–Relationship models, data <sup>fl</sup>ow diagrams, etc.) have successfully adopted a similar research design [3]. The subjects themselves were PhD students, serving as surrogates for ‘real’ knowledge engineers. Indeed the PhD subjects may be more representative than existing studies, because all our subjects have either mastered basic developer skills on-the-job, or through prior coursework. Similar studies employ student subjects [3].

![](/api/attachments/JBF65J7S/fulltext/images/6a7dfb320f6a2e77589667548cef622528f85609d59486345c3feb29ade39570.jpg)  
Fig. 5. Knowledge representation process.

The study employed a small subject pool. However, protocol analysis studies typically employ a small number of subjects. For example, Krahmer and Ummulen [29], Purao et al. [42], and von Mayrhauser and Vans [58] employed 10, 3, and 1 subjects respectively. In contrast, this study employs 14 subjects, each of whom received three treatments for a total of 42 subject-treatments.

## 6. Conclusion and future research

This research has studied knowledge engineers working with different knowledge representation schemes. The results suggest that knowledge engineers are not simply technicians who take knowledge and transform it into a knowledge representation. Instead, they inquire about both the domain space and design space, make choices, and function as limited domain experts. Future research is needed to experiment with the development of knowledge representation schemes that incorporate the <sup>fi</sup>ndings obtained from this study. Both <sup>fi</sup>eld observations and laboratory studies would further our understanding of this important design process.

The current empirical study is a <sup>fi</sup>rst step towards understanding the roles of knowledge engineers and how knowledge representation needs to be performed. The high-level empiricism of the current study may overlook or signi<sup>fi</sup>cantly oversimplify what our experiment in fact can investigate and thus limits its value and potential contributions. This research can be extended and enhanced by <sup>fi</sup>rst establishing a new theoretical model according to the learning theory literature, and then re-conceptualizing the effect of our current study and analysis to reveal more interesting and rigorous understanding of the roles and behaviors of knowledge engineers in conducting knowledge representation.

## Acknowledgment

Support for this research came from the J. Mack Robinson College of Business, Georgia State University.

## References

[1] B. Adelson, E. Soloway, The role of domain experience in software design, IEEE Transactions on Software Engineering 11 (1985) 1351–1360.

[2] M. Alavi, D.E. Leidner, Review: knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly 25 (2001) 107–136.

[3] A. Bajaj, D. Batra, A. Hevner, J. Parsons, K. Siau, Information technology and systems—I systems analysis and design: should we be researching what we teach? Communications of the Association for Information Systems 15 (2005) 478–493.

[4] P.A. Bekker, A. Merckens, T.J. Wansbeek, Identi<sup>fi</sup>cation, Equivalent Models, and Computer Algebra, Academic Press, 1994.

[5] C. Brewster, K. O'Hara, Knowledge representation with ontologies: the present and future, IEEE Intelligent Systems 19 (2004) 72–81.

[6] R. Brooks, Towards a theory of the comprehension of computer programs, International Journal of Man-Machine Studies 39 (1983) 237-267

[7] R.A. Brymer, Hospitality Management: An Introduction to the Industry, Kendall/Hunt Publishing Company, Dubuque, Iowa, 1995.

[8] T.A. Byrd, Implementation and use of expert systems in organizations: perceptions of knowledge engineers, Journal of Management Information Systems 8 (1992) 97–116.

[9] T.A. Byrd, K.L. Cossick, R.W. Zmud, A synthesis of research on requirements analysis and knowledge acquisition, MIS Quarterly 16 (1992) 117–138.

[10] J. Cardoso, The semantic web vision: where are we? IEEE Intelligent Systems 22 (2007) 84–88.

[11] Y.-J. Chen, Development of a method for ontology-based empirical knowledge representation and reasoning, Decision Support Systems 50 (2010) 1–20.

[12] Cecil Eng Huang Chua, Veda C. Storey, Roger H. L. Chiang. Knowledge representation: a conceptual modeling approach. Journal of Database Management 23 (1) (January/March 2012) 1–30.

[13] A. Cohen, European car rental, gas hike shifts buyers' gears, Business Travel New 17 (2000) 12.

[14] R. Davis, H. Schrobe, P. Szolovits, What is a knowledge representation? AI Magazine 14 (1993) 17–33.

[15] T.C. Du, F. Li, I. King, Managing knowledge on the web—extracting ontology from HTML web, Decision Support Systems 47 (2009) 319–331.

[16] K.A. Ericsson, H.A. Simon, Protocol Analysis: Verbal Reports as Data, MIT Press, 1993.

[17] A. Garnham, Mental Models as Representations of Discourse and Text, Ellis Horwood Ltd., West Sussex, UK, 1987.

[18] A. Garnham, Mental Models and the Interpretation of Anaphora, Psychology Press, East Sussex, UK, 2001.

[19] T.R. Gruber, Translation approach to portable ontology speci<sup>fi</sup>cations, Knowledg Acquisition 5 (1993) 199–220.

[20] W. He, S. Erdelez, F.-K. Wang, C.-R. Shyu, The effects of conceptual description and search practice on users’ mental models and information seeking in a case-based reasoning retrieval system, Information Processing and Management 44 (2008) 294–309.

[21] J. He<sup>fl</sup>in, J. Hendler, S. Luke, SHOE: A Knowledge Representation Language for Internet Applications, University of Maryland at College Park, 1999.

[22] L.B. Holder, Z. Markov, I. Russell, Advances in knowledge acquisition and representation, International Journal on Arti<sup>fi</sup>cial Intelligence Tools 15 (2006) 867–874.

[23] K.M. Iverson, Introduction to Hospitality Management, Van Nostrand Reinhold, 1989.

[24] P.N. Johnson-Laird, Mental Models: Towards a Cognitive Science of Language, Inference, and Consciousness, Cambridge University Press, Cambridge, UK, 1983.

[25] P.N. Johnson-Laird, P. Legrenzi, V. Girotto, How we detect logical inconsistencies, Current Directions in Psychological Science 13 (2004) 41–45.

[26] A. Karahasanovi, U.N. Hinkel, D.I.K. Sjoberg, R. Thomas, Comparing of feedback-collection and think-aloud methods in program comprehension studies, Behaviour & Information Technology 28 (2009) 139–164.

[27] S. Kaza, H. Chen, Evaluating ontology mapping techniques: an experiment in pub lic safety information sharing, Decision Support Systems 45 (2008) 714–728.

[28] C.R. Kothari, D.J. Russomanno, Enhancing OWL ontologies with relation semantics, International Journal of Software Engineering 18 (2008) 327–356.

[29] E. Krahmer, N. Ummelen, Thinking about thinking aloud: a comparison of two verbal protocols for usability testing, IEEE Transactions on Professional Communication 47 (2004) 105–117.

[30] A.J. Kuzel, Sampling in qualitative inquiry, in: B.F. Crabtree, W.L. Miller (Eds.), Doing Qualitative Research, Sage Publications, Newbury Park, CA, 1992, pp. 31–44

[31] J.R. Landis, G.G. Koch, The measurement of observer agreement for categorica data, Biometrics 22 (1977) 79–94.

[32] O. Lassila, Web metadata: a matter of semantics, IEEE Internet Computing 2 (1998) 30–37.

[33] N. Leone, G. Pfeifer, W. Faber, T. Eiter, G. Gottlob, S. Perri, F. Scarcello, The DLV system for knowledge representation and reasoning, ACM Transactions on Computational Logic 7 (2006) 499–562.

[34] K. Lyytinen, Different perspectives on information systems: problems and solutions, ACM Computing Surveys 19 (1987) 5–46.

[35] M.B. Miles, A.M. Huberman, Qualitative Data Analysis: An Expanded Sourcebook, Sage Publications, 1994.

[36] P.P. Mykytyn Jr., K. Mykytyn, M.K. Raja, Roles of the knowledge engineers and their relationship to systems analyst, Information Resources Management Journal 11 (1998) 14–26.

[37] I.M. Neale, Modelling expertise for KBS development, Journal of the Operational Research Society 41 (1990) 447–458

[38] L. Nguyen, P.A. Swatman, Complementary Use of Ad Hoc and Post Hoc Design Rationale for Creating and Organizing Process Knowledge, 33rd Hawaii International Conference on System Sciences. 2000

[39] S.J. Payne, Users' mental models: the very ideas, in: J.M. Carroll (Ed.), HCI Models, Theories, and Frameworks: Toward a Multidisciplinary Science Morgan-Kaufman, San Francisco, 2003.

[40] C. Peugeot, Conceptual Model and Mental Model, 3rd European Conference on Information Systems, Athens, Greece, 1995.

[41] H.S. Pinto, A. Gomez-Perez, J.P. Martins, Some Issues on Ontology Integration, IJCAI-99 Workshop on Ontologies and Problem-Solving Methods: Lessons Learned and Future Trends, 1999, pp. 7.1–7.12.

[42] S. Purao, M. Rossi, A. Bush, Towards an understanding of the use of problem and design spaces during object-oriented system development, Information and Organization 12 (2002) 249–281.

[43] J. Recker, M. Rosemann, J. Krogstie, Ontology- versus pattern-based evaluation of process modeling language: a comparison, Communications of the Association for Information Systems 20 (2007) 774–799.

[44] G. Schreiber, H. Akkermans, A. Anjewierden, Knowledge Engineering and Management: The Commonkads Methodology, MIT Press, Cambridge, MA, 1999.

[45] N. Shadbolt, K. O'Hara, L. Crow, The experimental evaluation of knowledge acquisition techniques and methods: history, problems and new directions, International Journal of Human Computer Studies 51 (1999) 729–755.

[46] G. Shanks, E. Tansley, J. Nuredini, D. Tobin, R. Weber, Representing part-whole relations in conceptual modeling: an empirical evaluation, MIS Quarterly 32 (2008) 553–573.

[47] M.K. Smith, C. Welty, D.L. McGuinness, OWL Web Ontology Language Guide, 2004.

[48] E. Soloway, K. Ehrlich, Empirical studies of programming knowledge, ACM Transactions on Software Engineering 10 (1984) 595–609.

[49] J.F. Sowa, Conceptual Structures: Information Processing in Mind and Machine, Addison-Wesley Publishing Company, 1984.

[50] J.F. Sowa, Knowledge Representation: Logical, Philosophical, and Computational Foundations Brooks Cole Publishing Co. 2000

[51] L.M. Stephens, M.N. Huhns, Consensus ontologies: reconciling the semantics of web pages and agents, IEEE Internet Computing 5 (2001) 92–94.
