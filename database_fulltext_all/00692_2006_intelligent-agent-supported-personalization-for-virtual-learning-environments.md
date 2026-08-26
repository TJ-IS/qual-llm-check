---
otero_id: 692
otero_key: "N4F3DUSJ"
title: "Intelligent agent supported personalization for virtual learning environments"
authors: "Dongming Xu; Huaiqing Wang"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.033"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intelligent agent supported personalization for virtual learning environments

Dongming Xu <sup>a,\*</sup>, Huaiqing Wang <sup>b,1</sup>

<sup>a</sup>UQ Business School, University of Queensland, Australia <sup>b</sup>Department of Information Systems, City University of Hong Kong, Hong Kong

Received 1 June 2004; received in revised form 15 March 2005; accepted 30 May 2005 Available online 11 August 2005

## Abstract

Virtual learning environments (VLEs) are computer-based online learning environments, which provide opportunities for online learners to learn at the time and location of their choosing, whilst allowing interactions and encounters with other online learners, as well as affording access to a wide range of resources. They have the capability of reaching learners in remote areas around the country or across country boundaries at very low cost. Personalized VLEs are those VLEs that provide a set of personalization functionalities, such as personalizing learning plans, learning materials, tests, and are capable of initializing the interaction with learners by providing advice, necessary instant messages, etc., to online learners. One of the major challenges involved in developing personalized VLEs is to achieve effective personalization functionalities, such as personalized content management, learner model, learner plan and adaptive instant interaction. Autonomous intelligent agents provide an important technology for accomplishing personalization in VLEs. A number of agents work collaboratively to enable personalization by recognizing an individual’s eLearning pace and reacting correspondingly.

In this research, a personalization model has been developed that demonstrates dynamic eLearning processes; secondly, this study proposes an architecture for PVLE by using intelligent decision-making agents’ autonomous, pre-active and proactive behaviors. A prototype system has been developed to demonstrate the implementation of this architecture. Furthermore, a field experiment has been conducted to investigate the performance of the prototype by comparing PVLE eLearning effectiveness with a non-personalized VLE. Data regarding participants’ final exam scores were collected and analyzed. The results indicate that intelligent agent technology can be employed to achieve personalization in VLEs, and as a consequence to improve eLearning effectiveness dramatically

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Intelligent agents; Virtual learning environment; Personalization; eLearning; Artificial intelligence application

## 1. Introduction

Virtual Learning Environments (VLEs) are computer-based environments that are relatively open systems, enabling interactions and encounters with other people and providing access to a wide range of resources [35]. VLEs can supplement face-to-face teaching methods, or totally replace these teaching methods in the case of distance learning. VLEs offer a number of advantages over traditional teaching environments in terms of convenience and flexibility [8]. There are no geographical boundary limitations for using VLEs. They are capable of reaching potential learners in remote areas around the world at very low cost. For these reasons, VLE is becoming one of the fastest growing areas in educational technology research and development. Many traditional colleges and universities, individually or in various forms of partnerships, are embracing information technologies to create new learning models that enhance the effectiveness and reach of their programs [2].

Researchers and developers are making rapid improvements in the design and implementation of VLEs, resulting in continuous progress toward successful VLEs. However, online learning is not always effective and sometimes fails to meet learning objectives because of the following limitations:

(1) Unstructured learning materials. Online learning materials are usually unstructured across different media, without any close associations with the eLearning processes [44]. Learning material is distributed without consideration for learners’ capacities and prior learning, and therefore lacks contextual and adaptive support [15];

(2) Insufficient flexibility. In many current VLEs, the content materials and choices have been predefined, regardless of the learning process and learners’ differences. Online learners have little flexibility to adapt the learning content and process to meet their individual needs [2,15,19].

(3) Insufficient interactivity. Studying online, by its nature, requires online learners to be more actively engaged and interact with their VLEs [12,14]. However, some current VLEs are not very interactive. There is less opportunity for receiving instant responses and feedback from the instructor or VLEs when online learners need support.

In summary, the current VLEs are one-fits-all solutions of instructional design that suffer from their passive nature. Online courses are currently delivered without consideration of learners’ backgrounds and needs [44]. VLEs are best able to achieve learning effectiveness when they can adapt the online instructions to the needs of individual learners [12]. VLEs should be able to identify learning needs and personalize solutions that foster successful learning and performance. Therefore Personalized VLEs (PVLEs) are defined as those VLEs that provide a set of personalization functionalities, such as personalized learning plans, learning materials and tests, and initiating interactions with the learner by providing advice, necessary instant messages, etc. PVLEs are becoming more promising for achieving eLearning effectiveness due to their individual and adaptive eLearning supports. The major challenge for achieving personalization in a PVLE is to recognize the individual learning pace and provide instructional reactions accordingly.

In the last 10 years, the field of Intelligent Tutoring Systems (ITS) research has been developing rapidly. It is the major research group on VLEs. Along with the growth of computing capabilities, more and more ITS researchers have focused on PVLEs to provide tailored learning materials, instructions and instant interaction to suit individual learners or a group of learners by using intelligent agent technology [4,6]. Intelligent agent technologies facilitate the interaction between the students and the systems, and also generate the artificial intelligence model of learning, pattern recognition, and simulation [10], such as the student model, task model, pedagogical model, and repository technology [31]. These models work together in a productive way to support students’ learning activities adaptively. Therefore, the properties of intelligent agents, i. e. autonomy, pre-activity, pro-activity and co-operativity, support PVLEs in recognizing online learners’ learning stage and in reacting with tailored instruction including personalized learning materials, tests, instant interactions, etc.

The authors of this research have been conducting research on intelligent agent supported online education for many years. For instance, the prototype systems, LearOOP [31] and SQL Tutor+ [32]; provide the necessary repository technology; to support multi-user co-operation and collaboration in complex ITSs. The

Intelligent Online Learning System (IOLS) demonstrated intelligent agent supported personalization facilities in the eLearning environment to give online learners adaptive support [38,40]. The current research is part of a continuing stream of research into application of intelligent decision-making agents for VLEs. In this study, a personalization model is developed, and based on this personalization model, intelligent decision-making agents are proposed to achieve the personalization in PVLEs by employing intelligent agents’ autonomous, pre-active and proactive behaviors, and a multi-agent based PVLE architecture is designed. For evaluating this approach, a prototype is implemented; and for investigating the effectiveness of eLearning utilizing this approach, an empirical experiment is conducted. The empirical experiment adapts a real development application used in a short-term online course. The performance of our prototype by registered online learners’ eLearning effectiveness is investigated through the online course. Finally this study demonstrates the impact of personalization model on system design and development, the impact of intelligent decision-making agents achieving personalization in PVLEs, and the impact of agents supported PVLE on effective eLearning achievements.

The organization of this paper is as follows. The following section briefly reviews the relevant literature on personalization for eLearning, intelligent agent supported VLEs, and the authors’ previous research in this area. After the personalization model is proposed in Section 3, the architecture of multi-agent supported PVLE is presented in Section 4. Section 5 describes the knowledge representation and inference in terms of the definitions of fuzzy epistemic logic, as well as the learner model, content model, and learner profile, and associated relations. The development of the prototype, Intelligent eLearning System (IeLS) is discussed in Section 6. The operation and empirical evaluation is addressed in Sections 7 and 8. The final section provides a conclusion and the implications of our work.

## 2. Background

Adaptive support for VLEs aims to use the Internet to support online learners in communicating and collaborating with each other as a pedagogical technique, rather than merely using Web pages for posting of materials, or using email or chat rooms for studentteacher messages [15]. Intelligent agent technologies facilitate the interaction between the students and the systems. We are clearly interested in developing systems suitable for handling real online courses using an adaptive and personalized approach that is tailored to individual online learner needs. Providing online learners with an adaptive learning plan and personalized learning instruction based on each individual’s background and ability are the main topics in PVLEs research.

## 2.1. The role of personalization

PVLEs are adaptive online learning environments, where individual learners can be uniquely identified, with content specifically presented and progress individually monitored, supported, and assessed. In order to keep online learners captivated and self-motivated as they achieve learning objectives, PVLEs should be able to identify learning needs and provide customized solutions that foster successful learning and performance, with or without an instructor to supplement instruction [23]. Therefore, to achieve learning effectiveness, a PVLE should be developed by adapting learning to online learners [1,17].

Generally speaking, an ITS can be viewed as a particular kind of intelligent system designed to support eLearning, which has a philosophy based on a more objectivist pedagogical view. Knowledge to be learned is pre-specified in the system and transferred to the learner during the instructional process [1]. Constructivist views of learning, on the other hand, emphasize an entirely different set of values and may require a different kind of intelligent system to support learning [18,25]. The constructivist approach sees knowledge as individually constructed from what learners do in their experiential worlds and unable to be objectively defined. Since what is known at a certain time is particular to the individual learner and is based on previously acquired knowledge, the designed instruction may need to be adapted to the individual characteristics of the learners during the instructional process.

Online learners can be highly diverse, from different backgrounds, and with a variety of different learning goals, motivations, learning skills and learning abilities. A one-fits-all learning material and teaching strategy is unlikely to lead to learning effectiveness across a broad spectrum. Learners differ in terms of their preferred learning styles. Instructional methods that match an individual’s learning style will be the most effective [18]. Russell [26] proposed that educators should identify and acknowledge learning differences and make <sup>b</sup>maximum use of the technology to serve them accordingly.<sup>Q</sup> Shute [28] suggested that a computer-based education system with a personalizing component might be superior to a <sup>b</sup>nonintelligent<sup>Q</sup> version. Martinez [21] claimed that learners enjoyed greater success in learning environments that adapted to and supported their individual learning orientation, and that the fundamental <sup>b</sup>one-on-one<sup>Q</sup> solution using reliable <sup>b</sup>meta-level<sup>Q</sup> learner-difference or performance-difference criteria would replace the <sup>b</sup>one-fits-all<sup>Q</sup> solution. This would result in an evolution from the current, passive VLEs to dynamic, adaptive PVLEs, leading to greater success in online learning. PVLE uses structured adaptive learning materials and teaching methods to meet each individual online learner’s needs, and provides two-way interaction with meaningful feedback and advice, thus potentially increasing online learners’ eLearning performance.

## 2.2. Intelligent agents for eLearning systems

Intelligent agents provide an important paradigm for use in Internet applications [11]. Wooldridge and Jennings defined an agent as a computer system that is situated in some environment, and is capable of autonomous action in that environment in order to meet its design objectives [36]. Furthermore, Wooldridge claimed that agents are able to act without the intervention of humans or with other systems; they have control both over their own internal state, and over their behavior [35]. Maes proposed agents as computing systems that inhabit some complex dynamic environment, sense, and act autonomously in the environment and by doing so realize a set of goals or tasks for which they are designed. In short, an intelligent agent can be viewed as a computing system designed to realize a set of goals or tasks while inhabiting, sensing and acting autonomously in a complex dynamic environment on behalf of a person or organization, and which is able to interact with its environment and with other agents. Although there is not a universally recognized definition for intelligent agents, and what constitutes an intelligent agent is open to discussion, agents are a natural extension of current component-based approaches and should at least be able to model the preferences, goals, or desires of their owners and to learn as they perform their assigned tasks [41,45].

Fuzzy sets and the related disciplines that constitute soft computing provide an appropriate tool for constructing these agents [41]. Because of the nature of online learner’s knowledge, the learning process contains imprecise, ambiguous, or uncertain information and situations with fuzzy value. Therefore, Fuzzy logic is used as a matched solution to model such knowledge in such eLearning modeling research [37].

Intelligent agent technology has much to offer with respect to VLEs. The agent metaphor provides a way to operate and simulate the <sup>b</sup>human<sup>Q</sup> aspect of instruction in a more natural and valid way than other controlled computer-based methods [8]. Intelligent agent technologies facilitate the interaction between online learners and VLEs, and also generate an artificial intelligence model for learning, pattern recognition and simulation [10,20], such as a learner model, a task model and a pedagogical model. Those models meet together in a productive way to support students’ learning activities adaptively. The previous research illustrates that intelligent agents can provide automated and personalized learning instruction to online learners [10,20].

In the early application of multi-agents in educational systems, intelligent agents were mostly designed as personal assistants, user guides, alternative help systems, dynamic distributed system architectures, human-system mediators, and so forth [4]. As shown in Table 1, the interest for an explicit representation of tutorial knowledge has been continuously growing: concepts like student models [12], pedagogical diagnosis [24] and tutoring expertise [7] have been widely discussed since their introduction into educational systems research. The information repository and student profiling system provide facilities and services to support the knowledge communication within a multiple agent system, and address several co-operative ITS for distance learning and online learning [16]. With repository support, ITSs are able to provide collaboration and cooperation services to both students and teachers that demonstrate that the repository technology is an appropriate technical solution to support multi-user co-operation and collaboration in complex ITS [32]. The most recent research has been focused on the implementation of multi-agent based online education systems where the individual function has been specified, such as content management systems [27], selfregulated systems [5], self-assessment systems [9], etc. However, most of the previous research is , in fact, based on the objectivist pedagogical approach that intelligent eLearning systems enable some components reflecting the values of the particular view among the nature of knowledge, learning and teaching. Those approaches have led to architectures that focus on representing the knowledge to be learned (domain knowledge), inferring the learner’s knowledge (learner model), and planning instructional steps to learning (teaching model) [1].

Table 1  
Related work on intelligent online education systems

<table><tr><td>Sources</td><td>Description</td><td>Application</td></tr><tr><td>Fletcher [12], Ohlsson [24], Burton and Brown [7]</td><td>Develop hybrid agent-based knowledge representation in computer-based instruction to understand students&#x27; learning status.</td><td>Student models, pedagogical diagnosis, and tutoring expertise.</td></tr><tr><td>Wang [31,32], Kwok et al. [16]</td><td>Propose and develop prototypes of multi-agent based ITS that support distance learning and online learning.</td><td>Information repository and student profiling system provide facilities in such applications, such as SQL Tutor +, LearnOOP, IOLS, etc.</td></tr><tr><td>Santos and Osorio [27]</td><td>Present an approach that integrates intelligent agents, user models and automatic content categorization in a virtual environment.</td><td>AdaptIVE: used to make educational content available. The division of the virtual environment is adopted according to the areas of the contents.</td></tr><tr><td>Conejo et al. [9]</td><td>Propose a computer adaptive testing tool that generates test questions intelligently to fit the student&#x27;s level of knowledge.</td><td>With SIETTE, teachers worldwide can define their tests, and their students can take these tests on-line.</td></tr><tr><td>Xu et al. [40], Biswas et al. [5]</td><td>Describe and develop agent-based systems that promote deep and individual learning and understanding. The prototypes have been used for laboratory experiments.</td><td>Betty&#x27;s Brain is a teachable agent system in the domain of river ecosystems that combines learning by teaching and self-regulation strategies. IOLS is a multi-agent based VLE.</td></tr></table>

In summary, Table 1 presents a history of intelligent online education systems starting from early learning model discussions, framework and architecture design and then implementation of prototypes with specified personalization functions, such as personalized content management, test systems, and a combination of an ITS and learning materials organized for adaptive presentation which is a starting point for research into PVLEs. Most of the prototypes only exist in the laboratory environment. This reveals a challenge of designing a comprehensive architecture, developing a fully functional PVLE, and investigating the effectiveness of eLearning in a real world application of PVLEs.

## 3. Personalization model

To achieve learning effectiveness, an ideal PVLE should be built with reference to adapting learning theory. Whether in a face-to-face classroom or a VLE, students exhibit marked differences with respect to mental abilities, personalities, learning experiences and background knowledge. It is therefore necessary to develop tailored instruction in the VLEs via the application of flexible learning materials and individual learning plans. Fig. 1 demonstrates a personalization model in PVLEs.

The personalization of VLEs is grounded in the recognition that every online learner is an individual, with a distinct learning style, pace, and path [13,22]. The personalization model developed in this research is grounded on the constructivist pedagogical principle. The constructivist pedagogical principle views effective learning as a learner-centered and active process of knowledge construction. Learners can learn more effectively and meaningfully in a favorable environment where their ideas are explored, compared, criticized, and reinforced through talking with and listening to others [30].

![](/api/attachments/N4F3DUSJ/fulltext/images/0dae029d8a373dd116a94dc235b099de6b94f20c891d344e29f2d5a1ba98f1a2.jpg)  
Fig. 1. Personalization model in PVLEs.

Based on previously acquired knowledge, the designed instruction may need to be adapted to the individual characteristics of the learners during the learning process. Therefore, the personalization model will be able to recognize an individual’s learning pace, during the recognition stage, and provide instructional reaction correspondingly, during the reaction stage. The recognition stage includes receiving a learner’s current activities such as browsing path, learning time for each session, exercises, and examinations, which are recorded by the system for further processing; accessing the learner’s learning history in the profile, i.e. the historical learning activities and results; and analyzing the information in the profile to build and refine the learner’s model. The reaction stage involves the determination of appropriate instructional actions and their execution, such as presenting personalizing contents, initiating interaction, etc.

This personalization model provides guidance on identifying personalization functionalities and processes from an educational point of view. In this study, we employ intelligent agent techniques to achieve personalization in PVLEs based on this personalization model. In each step of the personalization process, intelligent agents work correspondingly to play a crucial role in providing the intelligent behavior of the system. A number of intelligent agents can work together to achieve the personalization tasks.

In the recognition stage, intelligent agents will record an individual online learner’s activities during their learning process, create their learner profile, and then develop or update individual online learner models. After each individual eLearning activity is specified, the corresponding instruction will be provided. In conjunction with the content model, an intelligent agent updates the individual learner plan that determines the appropriate instructional action based on the individual learner model. These instructional actions are executed including the personalization of reading materials for each individual learner to match the individual’s learner model; a self-evaluation quiz is personalized according to a diagnosis of the online learner’s learning problems; and individual learning advice that is distributed to a learner to increase interactions. This is regarded as the reaction state corresponding to Fig. 1.

By utilizing the properties of autonomy and cooperativity, the intelligent agents can support the recognition stage in the personalization in the PVLEs. By employing re-active and pro-active properties, the intelligent agents can support the PVLE in the reaction stage to adjust the next step in the learning plan and execute flexible instructional actions, in order to prevent unexpected learning problems and failures in the reaction stage.

## 4. Architecture design

Based on the personalization model, three-layer architecture of a PVLE is designed (shown in Fig. 2). It achieves the proposed personalization functionalities in PVLEs. The upper layer in the figure is the learner layer, which provides adaptive interface for online learners.

The middle layer contains a number of intelligent decision-making agents that support personalization.

![](/api/attachments/N4F3DUSJ/fulltext/images/52b8fd35d5e467efe00ccd46acc5603ddf4474a006dece64f4ae8c7177b64caf.jpg)  
Fig. 2. Three layer PVLE architecture.

These agents are designed based on our personalization model and fitted into two learning process stages.

<sup>!</sup> In the recognition stage, the Activity Agent records eLearning activities: Online learners’ learning activities, such as mouse action (time and target), learning duration on a particular task, test score, documents load/unload, etc. are captured and stored in the learner profile by the Activity Agent.

<sup>!</sup> The Modeling Agent abstracts learner models: The agent abstracts the learner model, based on the learner profile. As an example, the model may contain the information that <sup>b</sup>Tony studied the topic DFD Diagrams intensely on May 3, 2004.<sup>Q</sup>

<sup>!</sup> Based on the learner model, in the reaction stage, the Planning Agent updates the learning plan: The agent analyzes the current learning plan of the particular online learner based on the learner model and the content model, and then updates the learning plan. As an example, the topic sequence may be updated. Meanwhile, the planning agent is also able to exhibit goal-directed behaviors by using the pro-activity. For example, when the planning agent determines that the online learner may fail a topic, the agent may update his/ her learning plan to prevent this unexpected problem happening.

<sup>!</sup> The Learner Agent generates an adaptive interface: The agent dynamically assembles personalized instructional materials in terms of reading contents, quizzes and feedback for a particular online learner based on the learning plan. Such an assembling process includes the generation of the learning materials, the generation of quizzes, quizzes summary and instant messages. For example, because a particular online learner, Tony, has a current learning plan that requires him to study the topic <sup>b</sup>Constraints after DFD Diagrams,<sup>Q</sup> the materials for the topic <sup>b</sup>DFD Diagrams<sup>Q</sup> will be displayed on the webpage. When Tony clicks on the <sup>b</sup>next<sup>Q</sup> button, the material of the topic <sup>b</sup>Constraints<sup>Q</sup> will appear.

The lower layer is the repository layer that contains four components: Learner Profile, Learner Model, Learning Plan and Content Model. A knowledge repository is a database of specifications — it contains what is commonly referred to as meta-knowledge (knowledge about knowledge) and the meaning of this meta-knowledge. In providing meta-knowledge, the repository provides an opportunity for agents to deal with their interoperability problems [34]. Consequently, both dynamic knowledge relevant to the eLearning process (learner profile, model and plan), and static structured knowledge (course content) are stored in the knowledge repository for the knowledge manipulations.

It is essential to design a set of autonomous types of behaviors for the agents to achieve personalization, including <sup>d</sup>reactive<sup>T</sup>, <sup>d</sup>pro-active<sup>T</sup> and <sup>d</sup>cooperative<sup>T</sup> behaviors [31,33,36]. The autonomous behavior of agents allows agents to operate to achieve their goals without the direct intervention of humans. For instance, in eLearning systems, agents can record a learner’s learning activities based on predefined goal autonomously, and revise a learner’s learning plan, based on the situation changes, etc. The co-operative behavior enables agents to co-operate with other agents toward the achievement of certain objectives. As an example, the modeling agent and the planning agent work together to make a student’s dynamic learning plan. The reactive behavior of agents enables them to perceive their environments and respond in a timely fashion to changes that occur. As an example, when an interface agent notices some learning problems, it can send an instant pop-up message to the learner. The proactive behavior enables agents to not simply act in response to their environment, but to exhibit goal-directed behaviors by taking the initiative. For example, when the agents determine that a learner may fail the course, they may send a warning message to the learner in an attempt to prevent the failure.

![](/api/attachments/N4F3DUSJ/fulltext/images/62428d3a0f983857081f4627b944198a5db076c2cba29156af497088ad6ce311.jpg)  
Fig. 3. Agent architecture.

Agent architecture consists of an agent knowledge base, its operational facilities and its external interface facility (Fig. 3) [39]. It specifies agent behavior and its interactions with other agents and systems. The external interface component manages the communication between the agent and the outside world. The communication is message-based, and uses a simple and extensible language for communication among agents. The operational facility component is the central control and action part of an agent. It has reasoning facility and collaborating facility, respectively. The available functions are stored in the Knowledge Base component. The Collaborating Facility sub-component is responsible for the Collaboration with other agents.

An intelligent agent is a knowledge based software system, which includes domain level knowledge and meta level knowledge. Therefore, to develop intelligent agents for achieving recognition and reaction of personalization in PVLEs, knowledge representation and modeling is an essential part for generating a knowledge base in intelligent agents. Online learners and situations need to be modeled by using an appropriate knowledge representation scheme. In this study, fuzzy epistemic logic is employed to model and manipulate both the dynamic knowledge, such as learners and situations, and the static knowledge, such as content. The details will be addressed in the Next section.

## 5. Knowledge representation and inference

Personalization functionalities in PVLEs are based on knowledge about learning content, online learners, and situations and about their related issues. Formally, a number of models, such as content models, learner models and a situated plan must be designed to represent such knowledge. Given the nature of learner knowledge, learning progress contains imprecise, ambiguous, or uncertain information and situations with fuzzy values. Therefore, fuzzy logic is used as a suitable solution to represent such knowledge in our prototype system.

Yager presented an approach for using fuzzy representation for building intelligent agents. There are two steps in his fuzzy modeling process [41]. The first step is to partition the variables in terms of natural linguistic terms. This linguistic portioning, an inherent feature of what Zadeh [42,43] simply calls computing with words, greatly simplifies model building. The next step in this process is to represent these linguistic concepts in terms of fuzzy subsets. In fuzzy-logic based representation, a fuzzy term may be context dependent. For example, the term <sup>b</sup>good<sup>\_</sup>understanding<sup>Q</sup> would correspond to different standards at the beginning of the learning process and at the end of the learning process. Therefore, fuzzy-logic based representation would benefit from context reasoning formalized in knowledge representation.

In this research, we have developed a fuzzy epistemic logic to represent the learner’s dynamic knowledge state, while the static knowledge of course content or the domain knowledge is modeled by the concept of context from the field of knowledge representation [38,40].

## 5.1. Content model

Definition. A Curriculum is defined as a structure: $< C , S R , P R , I S T , D G >$

where

<sup>!</sup> C is the set of topics, such as {data<sup>\_</sup>base, data<sup>\_</sup> type, table, . . .}

$S R \subseteq C \times C$ is a relation, such as <sup>b</sup>data<sup>\_</sup>base, data<sup>\_</sup>type<sup>N</sup>

$P R \subseteq C \times C$ is a partial ordered relation, such that $S R \subseteq P R$ . A prerequisite is a PR. For instance, <sup>b</sup>data<sup>\_</sup>type, table<sup>N</sup> indicates that the topic data<sup>\_</sup>type is a prerequisite of table.

<sup>!</sup> IST is a function that maps each element of C to a subset of CL, the Context Language;

<sup>!</sup> DG is a function that maps each element C to a Fuzzy degree. The value of $D G ( c )$ indicates how long time should be taken to learn the topic of C.

## 5.2. Learner model

Definition. The learner model is a structure

hKS; <sup>T</sup>; PFi

where

<sup>!</sup> KS is a learner’s initial knowledge set, while CLK is the CL appending the modalities,

<sup>!</sup> \* is a revision function,

<sup>!</sup> PS is a behavior interpretation function that maps the current record of the learner’s behavior to new knowledge of the learner.

Given a learner i, the system will indicate an initial learner’s knowledge set $\Gamma _ { 0 } .$ After receiving a record D of the learner’s behaviors, the system uses the function PF and interprets the record D to be a new knowledge set $P F ( A )$ of the learner. By using the revision function \*, the system receives the new learner’s knowledge set, that is, ${ \cal T } _ { 0 } { } ^ { * } { \cal P } { \cal F } (varDelta )$

## 5.3. Learner profile

Definition. A learner profile is a set of the following pairs: <sup>b</sup>e, t<sup>N</sup>, where e is a behavior of the online learner, and t expresses the time during which the behavior occurs. The t could be a point of time or an interval of time. There are two main types of behaviors: learning a particular topic (symbolized by LN(c)) and making a choice in a quiz (symbolized by $A N S ( q ) )$ ).

## 5.4. Learning plan

A learning goal is a set of formulas with the form ${ { \bf { I } } ^ { \mathrm { { u } _ { j } } } } \left( i , c \right)$ . A learning plan toward a learning goal G is an ordered set D of behaviors such that

$$
G \subseteq \Gamma_ {0} ^ {*} P F (\Delta)
$$

where $\varGamma _ { 0 }$ is the learner’s current knowledge set.

Given a learning goal, we can derive a learning function that creates a learner learning plan from the learner model and content model.

## 5.5. Knowledge inference

The knowledge inference is based on Yager’s fuzzy modeling [43]. There are a number of Fuzzy rules in our system, with the following format:

If $V _ { 1 }$ is $A _ { \mathrm { i } 1 } , V _ { 2 }$ is $A _ { \mathrm { i } 2 } , . . . ,$ and $V _ { \mathfrak { p } }$ is $A _ { \mathrm { i p } } ,$ then U is $b _ { \mathrm { i } }$

The process of finding the output for a given input, $V _ { \mathrm { j } } { = } x ^ { * } { \mathrm { _ j } } ,$ is a simple two-step process:

1. Calculate each rule’s firing level:

$$
\lambda_ {i} = \min _ {j = 1, \Lambda , p} \left[ A _ {i j} \left(x _ {j} ^ {*}\right) \right]
$$

2. Calculate the model’s unique output $y ^ { * }$ as a weighted average of the firing levels and the consequents:

$$
y ^ {*} = \frac {\sum_ {i = 1} ^ {n} \lambda_ {i} b _ {i}}{\sum_ {i = 1} ^ {n} \lambda_ {i}}
$$

The conclusion will be based on the value of $y ^ { * }$ As an example, a set of such fuzzy rules has been implemented to determine the instant message for a learner Tony, based on his previous behavior Behavior P and the time he has spent on the current topic Spending T:

If Behavior P is poor and Spending T is short, then the Warning Level is Very High

If Behavior P is poor and Spending T is short, then the Warning Level is High

## 5.6. A simple example

In this session, a simple example is described to demonstrate the knowledge representation defined in this section. We assume that Tony is an online learner of our PVLE and he is learning an online course, <sup>b</sup>Introduction to Databases<sup>Q</sup>. The related knowledge representation is described as follows.

The topics C = {data<sup>\_</sup>base, data<sup>\_</sup>type, db<sup>\_</sup>table, table<sup>\_</sup>column, table<sup>\_</sup>row}

A topic db<sup>\_</sup>table has two sub-topics $S R =$ {<sup>b</sup>db<sup>\_</sup>table, table<sup>\_</sup>column<sup>Nb</sup>table, table<sup>\_</sup>row<sup>N</sup>}

A prerequisite PR = {<sup>b</sup>table<sup>\_</sup>column, table<sup>\_</sup>row<sup>N</sup>}, indicates that the prerequisite of table<sup>\_</sup>row is table<sup>\_</sup> column.

A piece of the learner Tony’s profile is as follows. It stores the fact that Tony learned the topic table<sup>\_</sup> column starting from 11:12:18 on August 24, 2004 and ending at 11:20:05 on the same day. He also did the quiz of table<sup>\_</sup>column for a certain period.

{Tony,<sup>b</sup>LN(table), [11:12:18/24/08/04, 11:20:05/ 24/08/04]<sup>N</sup>,<sup>b</sup>ANS(table<sup>\_</sup>colunm), [15:05:29/25/08/ 04, 15:22:48/25/08/04]<sup>N</sup>}

A part of Tony’s learner model is shown as below. He learned the topic data<sup>\_</sup>base well, learned data<sup>\_</sup> type poorly, learned db<sup>\_</sup>table very well, learned table<sup>\_</sup>column well, and learned table<sup>\_</sup>row nothing.

{<sup>b</sup>data<sup>\_</sup>base, 0.7<sup>N</sup>,<sup>b</sup>data<sup>\_</sup>type, 0.35<sup>N</sup>,<sup>b</sup>table, 0.9<sup>N</sup>, <sup>b</sup>table<sup>\_</sup>column, 0.7<sup>N</sup>,<sup>b</sup>table<sup>\_</sup>row, 0<sup>N</sup>}.

A part of Tony’s learning plan contains a sequence of topics associated with time values as follows. The first task is to learn the topic db<sup>\_</sup>table with difficult<sup>\_</sup> level 0.9, i.e. very difficult, and to learn the topic table<sup>\_</sup>column with difficult<sup>\_</sup>level 0.4, i.e. easy, etc.

{<sup>b</sup>1, LN(table), 0.9<sup>N</sup>,<sup>b</sup>2, LN(table<sup>\_</sup>column), 0.4<sup>N</sup>, <sup>b</sup>3, LN(table<sup>\_</sup>row), 0.8<sup>N</sup>, (4, ANS(table), 0.8<sup>N</sup>)}.

From the sample above it can be seen that the Fuzzy logic based learner model and learning plan can be used to represent learners’ learning behaviors easily and precisely. The knowledge base in the intelligent agents in our PVLE is constructed based on this type of knowledge representation and inference.

## 6. Prototype development

Intelligent agents in PLVE are implemented based on the agent architecture, consisting of an agent knowledge base, its operational facilities and its external interface facility (shown in the Fig. 3). The external interface component manages the communication between the agent and the outside world, using SOAP. The operational facility component is the central control and action part of an agent. It has to subcomponents called Reasoning Facility (JESS inference engine) and Collaborating Facility (written in JAVA), respectively.

The system knowledge includes the configuration of the eLearning system. In order to achieve reasoning capability, a number of JESS rules are stored in the Knowledge Base. Based on such rules, the intelligent agents are able to perform many tasks. As an example, the activity agent has a number of forwardchaining JESS rules. Assume an activity, such as the learner’s quiz score on a particular topic is too low, is inserted into the agent’s working memory, and assume that there are other activities, such as the learner spent too little time on this sub-topic, in the working memory already, a JESS rule may be fired. The new conclusion <sup>b</sup>the learner may be failed on this sub-topic<sup>Q</sup> may be inferred. This conclusion will be passed to the planning agent’s working memory. Such an insertion will cause another inference in the planning agent. Such inferences may lead to a warning message. The Collaborating Facility sub-component is responsible for the Collaboration with other agents (written in Java).

![](/api/attachments/N4F3DUSJ/fulltext/images/fa03ace299dbc322fecebf216d423a6ecd7ca3ffba049e364797229fee7def83.jpg)  
Fig. 4. Implementation framework of PVLE.

Based on the knowledge representation described in the last section, the Intelligent eLearning System (IeLS), a prototype of multi-agent-based PVLE, has been implemented, see Fig. 2 before). At the lowest level, the operating system is Linux. The Web server component contains the Apache Web server, and Jakarta Tomcat. The DBMS Oracle 8i is used for building the repository, and XML is used to represent course contents, learner models, and learning plans. Four types of decision-making agents work collaboratively in a PVLE. The main components in an agent in our PVLE are a knowledge base and operational facilities (shown Fig. 4). But each different agent has a different knowledge base and operational facilities.

The implementation of the four components of the knowledge repository is based on the knowledge representation described in Section 5. The Content Model is a static model, which contains the definitions of each topic, the fuzzy relations between these topics, and a number of fuzzy functions described in Section 5. The Learner Profile is a database application. All online learners’ information is stored in the Learner Profile including static information, such as previous course grades, and the dynamic information, such as learning activities, and so forth. The Learner Model represents online learner’s dynamic learning behavior in fuzzy values that is updated during the learning process. The Learning Plan represents a sequence of topics associated with fuzzy values at the current time.

Fig. 5 shows a screen snap that demonstrates instant interaction between eTutor and an online learner in the IeLS.

![](/api/attachments/N4F3DUSJ/fulltext/images/42f679a666df2294d41c4eb76174dba67cb15e15c3a9f1ee9142c78568ea7b91.jpg)  
Fig. 5. A screen snap of IeLS.

## 7. Prototype system operation

In this section, a scenario is used to demonstrate the IeLS operation. It is assumed that Tony is an online learner. After he enrolls in the online course provided in IeLS, the operation process unfolds as follows (Fig. 6).

a. Initiation stage: After Tony enrolls in the online course, IeLS will create the Profile<sup>\_</sup>Tony with initial value; Tony’s Learner Model, Model<sup>\_</sup>Tony; and Tony’s initial Learning Plan, the LearningPlan<sup>\_</sup> Tony. The creation of such initial models is similar to the creation of a number of instances from some pre-defined classes. For instance, the <sup>b</sup>Learner<sup>\_</sup> Model<sup>Q</sup> is a pre-defined class with a number of attributes, such as the initial<sup>\_</sup>knowledge and learning<sup>\_</sup>behaviour. When the object <sup>b</sup>Model<sup>\_</sup>Tony<sup>Q</sup> is created, his pre<sup>\_</sup>test results will be put in the initial<sup>\_</sup> knowledge and his learning<sup>\_</sup>behaviour is an empty set. Similarly, the object <sup>b</sup>LearningPlan<sup>\_</sup>Tony<sup>Q</sup> is created. However, the initial value of the Learning Plan<sup>\_</sup>Tony is set based on the Model<sup>\_</sup>Tony.

b. Log-in stage: When Tony logs in to the IeLS, a learner agent, Rep<sup>\_</sup>Tony, will be generated by IeLS on the server side. The Rep<sup>\_</sup>Tony will manage the communication between IeLS and Tony.

![](/api/attachments/N4F3DUSJ/fulltext/images/ed1080fb804a4595eaf5a202083733084a27c02f764ca859ef5a927281b9912d.jpg)  
Fig. 6. Learning operation sequence.

c. Pre-test stage: If Rep<sup>\_</sup>Tony finds that Tony has logged in for the first time, it will show the pretest Web-page to Tony. After Tony completes the pre-test and submits it, Rep<sup>\_</sup>Tony will pass it to the Activity<sup>\_</sup>Agent.

d. Profiling stage: The Activity<sup>\_</sup>Agent will analyze Tony’s pre-test results and save the results to the Profile<sup>\_</sup>Tony. The Activity<sup>\_</sup>Agent will also pass such results to the Modeling<sup>\_</sup>Agent. As an example, an XML fragment of such a message is shown below. It is assumed that Tony spent 20 min on the pre-test of 13 questions, and he answered 8 correctly (i.e. 69%).

<sup>b</sup>Analyzing<sup>\_</sup>Result<sup>N</sup>

<sup>b</sup>Sender=<sup>b</sup>Activity<sup>\_</sup>Agent<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>Destination=<sup>b</sup>Modeling<sup>\_</sup>Agent<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>TimeStamp=<sup>b</sup>15/9/25/08/2001<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>LearnerName=<sup>b</sup>Tony<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>LearnerID=<sup>b</sup>990013<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>CourseID=<sup>b</sup>FB2500<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>Stage=<sup>b</sup>Afterpretest<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>Individual<sup>\_</sup>Summary Subject=<sup>b</sup>Pretest<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>Range=<sup>b</sup>Course<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>TimeSpent=<sup>b</sup>20m<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>HitCounts=<sup>b</sup>13<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>Percentage<sup>\_</sup>of<sup>\_</sup>correctness=<sup>b</sup>69<sup>Q</sup>/<sup>N</sup>

<sup>b</sup>/Analyzing<sup>\_</sup>Result<sup>N</sup>

e. Modeling stage: The Modeling<sup>\_</sup>Agent will modify Tony’s learner model, Model<sup>\_</sup>Tony, based on Tony’s pre-test results and a set of modification rules.

f. Planning stage: Based on the new version of Model<sup>\_</sup>Tony, the Planning<sup>\_</sup>Agent will update the LearningPlan<sup>\_</sup>Tony.

g. Learning stage: Different types of learning materials are provided to Tony by the Rep<sup>\_</sup>Tony, based on the LearningPlan<sup>\_</sup>Tony. Assuming that the Topic<sup>\_</sup>X<sup>a</sup>C should be presented to Tony based on the LearningPlan, the Topic<sup>\_</sup>X has two prerequisites, Topic<sup>\_</sup>A<sup>a</sup>C and Topic<sup>\_</sup>B<sup>a</sup> C, which Tony has studied already. The function ISTknow <sup>a</sup> IST is the function of the knowledge level of a topic. The function ISTt <sup>a</sup> IST is the function of the time spent on a topic. Therefore, we have:

IST<sub>know</sub>(Topic<sup>\_</sup>A) <sup>a</sup> [0, 1]

IST<sub>know</sub>(Topic<sup>\_</sup>B) <sup>a</sup> [0, 1]

IST<sub>t</sub>(Topic<sup>\_</sup>A) <sup>a</sup> [0, 1]

IST<sub>t</sub>(Topic<sup>\_</sup>B) <sup>a</sup> [0, 1]

The overall knowledge level of prerequisite topics can be calculated by:

KnowingP=Min(ISTknow(Topic<sup>\_</sup>A), ISTknow (Topic<sup>\_</sup>B))

The overall time spent on prerequisite topics can be calculated by:

SpendingT =Max(ISTt(Topic<sup>\_</sup>A), ISTt(Topic<sup>\_</sup>B)) SpendingT=Max(ISTt(Topic\_A), ISTt(Topic\_B))

A set of fuzzy rules has been implemented to determine the suitable level of Topic\_X for Tony, based on KnowingP and SpendingT:

If KnowingP is good and SpendingT is short, then the SuitableLevel is abstract.

If KnowingP is good and SpendingT is average, then the SuitableLevel is abstract.

If KnowingP is good and SpendingT is long, then the SuitableLevel is regular.

If KnowingP is average and SpendingT is short, then the SuitableLevel is regular.

If KnowingP is average and SpendingT is average, then the SuitableLevel is regular.

If KnowingP is average and SpendingT is long, then the SuitableLevel is detailed.

If KnowingP is poor, then the SuitableLevel is detailed.

h. Quiz stage: The quiz is generated dynamically by Rep<sup>\_</sup>Tony, based on LearningPlan<sup>\_</sup>Tony.

i. Quiz analysis stage: The Activity<sup>\_</sup>Agent will analyze the answers to the quiz. Such analysis is based on the match between the correctness of the quiz and the LearningPlan<sup>\_</sup>Tony. The outputs are the achievement degree of the LearningPlan<sup>\_</sup>Tony, which is a portion of the Profile<sup>\_</sup>Tony.

The example below demonstrates how to generate a warning message, which is based on the student’s learning profile. Basically, a set of fuzzy rules have been implemented to determine the possible fail of Tony, based on QuizP, the quiz score of Tony on the current topic, and SpendingT, he time he has spent on the current topic:

If QuizP is VeryPoor, then the Fail is VeryPossible

If QuizP is Poor, then the Fail is Possible

If QuizP is BelowAverage and SpendingT is Short, then the Fail is Possible

If Fail is VeryPossible then WarningLevel is Very-High

If Fail is Possible then WarningLevel is High

As described before, after Tony completes a quiz, his quiz score will be calculated automatically and will be inserted into the knowledge base. Insertion will cause a serious forward-chaining rule firing. For instance, if Tony’s score is below average and he spent too little time, a medium level warning message will be sent to him.

## 8. Empirical investigation

The evaluation of eLearning systems can serve as a tool to further research development in the field of VLEs by providing suggestions for the overall improvement of the architecture and the behavior of the eLearning system [29]. Siemer and Angelides [29] proposed <sup>b</sup>internal evaluation<sup>Q</sup> to provide a clear picture of the architecture of the VLE and to determine how this architecture generates the behaviors of the systems and <sup>b</sup>external evaluation<sup>Q</sup> to assess the impact the VLE has on online learners. Following up this evaluation approach, in this study, the <sup>b</sup>internal evaluation<sup>Q</sup> of our prototype is addressed in the previous sections in terms on Knowledge Level Analysis, Program Process Analysis and Tutorial Domain Analysis. The <sup>b</sup>external evaluation<sup>Q</sup> is adopted to examine whether IeLS has been successful in the sense that it is accepted by the learners and helps them to achieve greater eLearning effectiveness. The areas of personalized learning facilities and eLearning effectiveness are investigated.

In the first experiment, the first prototype was demonstrated to 100 students in February 2001 and their feedback was collected in terms of system functionalities and perceptions for further development [40]. Based on the feedback, the second prototype system, IeLS, was developed and a field experiment was conducted to open an incentive four-day online course to undergraduate students with free registration in April 2002. In this experiment, participating students’ performance and perceptions were investigated.

The field experiment was designed to adopt two parallel learning groups with repeated measures to vary two learning environments, which are regular eLearning System (eLS) and Intelligent eLearning System (IeLS). The personalization functionalities were developed in the IeLS, and the eLS remained as a control eLearning environment without personalization features, but keep other features the same as in IeLS. The personalization functionalities include personalized learning materials, personalized self-evaluation, personalized learning pace and instant interaction between online learner and the eTutor from IeLS. Both systems deliver the same subject, Introduction to the Oracle Database, which is a four-chapter online course. A total of 228 students participated and were assigned to the two eLearning systems randomly, completing the course work during the experiment, which lasted 4 days. 117 of them used IeLS and 111 used eLS. At the beginning of the experiment, students were required to take a pre-test, and then move on to the learning procedure. They received the instructions directly from the respective eLearning system to which they were assigned, took quizzes after each chapter, and then took the final exam.

## 8.1. Learning achievement evaluation

The main objective of our experiment was to investigate the students’ learning achievements when using IeLS and their perceptions of the personalization facilities. The participants took the pre-test before the online course started, quizzes after each chapter, and then the final exam. All of the tests are set 100 marks.

SPSS was used for data analysis. Through an Independent Samples Test, we derived the learning performance comparison of the two groups of students. The data analysis results indicate that there is no difference between the two groups of students in the pre-test. It indicates that the students were assigned to two systems randomly, indicated in Table 2 and Fig. 7. There is no significant difference in terms of students’ learning achievements in the first quiz, which might be due to the fact that students were not yet familiar with the system facilities, and the learning time was too short to achieve a learning difference. But from Chapter 2 on, the learning performance between the two groups differed significantly; the students using IeLS achieved statistically significantly higher scores than the students using eLS. This indicates that the IeLS can provide a better VLE, which can help students to achieve greater learning effectiveness.

Table 2  
Learning achievements comparison

<table><tr><td>System (sample size)</td><td>Pre-test score (mean)</td><td>Chapter 1 quiz (mean)</td><td>Chapter 2 quiz (mean)</td><td>Chapter 3 quiz (mean)</td><td>Chapter 4 quiz (mean)</td><td>Final exam (mean)</td></tr><tr><td>IeLS (117)</td><td>55.7</td><td>66.1</td><td>83.0</td><td>76.8</td><td>74.4</td><td>83.8</td></tr><tr><td>eLS (111)</td><td>54.9</td><td>71.3</td><td>75.6</td><td>70.2</td><td>65.1</td><td>72.3</td></tr><tr><td>t (p-value)</td><td>0.246 (0.806)</td><td>-1.583 (0.115)</td><td>2.228 (0.027)</td><td>2.080 (0.039)</td><td>2.586 (0.011)</td><td>3.316 (0.001)</td></tr></table>

![](/api/attachments/N4F3DUSJ/fulltext/images/fa547a80b3ff4e8ba52a258684db5ad618b8f413743809939ec5fe5f6202fc3f.jpg)  
Fig. 7. Learning achievements.

## 8.2. Learning perception investigation

We also collected participants’ perceptions of the eLearning system used based on the question, <sup>b</sup>What one or two things about your eLearning experience did you like the most?<sup>Q</sup> In total, 91 comments were received from the students from IeLS (total 117 students), and 75 comments were received from the students from eLS (total 111 students). These comments were carefully analyzed and categorized into seven constructs, which reflect the systems’ functions: System Feedback, Content presentation, Quiz generation, BBS, Interface, Learning Location and Learning Time. The descriptions of these seven constructs and the data analysis are presented in Table 3.

Table 3  
Students’ feedback on their positive eLearning experiences

<table><tr><td>Construct</td><td>Summarized students&#x27; comments</td><td>No. of response from IeLS (91 in total) (%)</td><td>No. of response from eLS (75 in total) (%)</td></tr><tr><td>System Feedback</td><td>System provided sufficient advice in the quiz summaries and the instant feedbacks in learning.</td><td>22/24</td><td>3/4</td></tr><tr><td>Content Presentation</td><td>Learning material comprehension was organized in a good way, and the information contained is useful and precise.</td><td>20/22</td><td>12/16</td></tr><tr><td>Quiz Generation</td><td>Quiz comprehension is appropriate. The detailed explanations and reference notes are useful.</td><td>16/18</td><td>12/16</td></tr><tr><td>Interface</td><td>The interface is user friendly. It&#x27;s easy to use and understand the system functions.</td><td>7/8</td><td>5/6</td></tr><tr><td>BBS</td><td>Discussion Board and Keywords searching are useful.</td><td>0/0</td><td>2/2</td></tr><tr><td>Learning Location</td><td>It&#x27;s quite convenient for learners to access the course anywhere.</td><td>11/12</td><td>15/20</td></tr><tr><td>Learning Time</td><td>It&#x27;s quite convenient for learners to access the course anytime.</td><td>15/16</td><td>27/36</td></tr></table>

In conclusion, from Table 3, it is clear to see that the students in IeLS had more positive perceptions of the system feedback, personalized content presentation and quiz generation than was provided by eLS. These comments are indicative of the commonly held opinion that PVLEs provide a <sup>b</sup>good learning environment<sup>Q</sup> because IeLS provided personalized eLearning facilities to give learners tailored instruction. It includes instant feedback regarding their learning status, personalized learning materials to meet learning pace, and personalized quizzes to help learners’ self evaluation. <sup>b</sup>The materials are well-organized and the flow of presenting the material is logical and clear<sup>Q</sup> and <sup>b</sup>easy to understand<sup>Q</sup>. <sup>b</sup>It is well organized and precise<sup>Q</sup>. I think the eTutor is very helpful to make me pay more attention on the study and to make me study effectively and efficiently<sup>Q</sup>. <sup>b</sup>The immediate feedback from eTutor is very helpful, which makes my learning easier<sup>Q</sup>. Some students also were also impressed by the <sup>b</sup>format of quiz<sup>Q</sup>, <sup>b</sup>the comprehension analysis after quizzes<sup>Q</sup> and <sup>b</sup>to know the schedule and progress of the course<sup>Q</sup>. The comments also indicate that the students in IeLS were highly motivated by the personalization facilities in the IeLS. Motivation is the energy that drives a learning society forward and its significance should never be underestimated [40]. Motivation is often equated with quantitative changes in behaviour in terms of higher achievement, more time spent on task, etc. [3]. During the learning process, the more students are motivated, the greater learning effectiveness they will achieve.

The Interface, and the BBS and the Keywords Searching functions were implemented in both systems identically. Both systems could be accessed at any time and any location during the experiment. The participants who used IeLS were similarly or less excited about these three functions compared to the counterparts who used eLS. We suggest that this is because it appears that the students who used eLS did not find that they had a special experience other than with respect to flexible learning location and time. In contrast, the participants who used IeLS had a lasting impression that personalization gave them tailored instruction to meet their needs during their online study. For those who gave negative comments about the eLS such as <sup>b</sup>not interesting at $a l l ^ { \prime } { \bar { \mathbf { \Gamma } } } _ { \mathrm { { ; } } }$ <sup>b</sup>boring<sup>Q</sup> and <sup>b</sup>no comments<sup>Q</sup>, etc., is clear that these students are more likely to lose their motivation to study. Therefore, one might conclude that personalization could lead to positive learning effects on eLearning performance.

## 9. Conclusion and implications

This study demonstrates that intelligent agents supported PVLEs can overcome the limitations of one-fits-all instructional VLEs. Learning material is structured and delivered to online learners with consideration of the learner’s capacities, prior learning and the learning process. Feedback from eTutor enables two-way interaction, which increases the sufficiency of interaction and has positive impact on learners’ achievement. The contributions of this research to the research literature are as follows:

<sup>!</sup> The personalization model: It is a conceptual model for the design and development of personalization functionalities. It defines eLearning process in two stages, recognition and reaction, and provides the ability to understand the personalized learning process. This personalization model focuses on the dynamic properties of the learning process, which includes decision making to sequence situation and activities in learning processes and the decision making to sequence domain knowledge and instructional steps.

<sup>!</sup> Intelligent decision-making agents: The personalization can be achieved by intelligent agents’ decision-making capability, through recognizing individual eLearning pace and reacting correspondingly. Based on the personalization model, a number of decision-making agents in IeLS were designed and developed. Prototype of multi-agent supported PVLE, IeLS, was designed and developed. In IeLS, online learners can be uniquely identified, course contents are specifically presented, learning progress is individually monitored, supported, and assessed, and a learning situation is afforded.

<sup>!</sup> Field experimental investigation: This cross-disciplinary approach provides a scientific method to evaluate the novel approach through a real world application. The previous research doesn’t show that intelligent agent based eLearning applications have been used in real world environments. In this research, IeLS was developed and used for a real online course, and its effectiveness was investigated in an empirical experiment. The evaluation results indicate that the IeLS makes great improvements in the personalization and has the capability of greatly enhancing learning effectiveness.

In short, this study leads to a new and more general perspective on the use of intelligent decision-making agents to support PVLEs. We believe our research findings will lead to a new stage of technologymediated distance learning. The results of this study highlight the fact that the important concepts, including the conceptual model, the agent technologies, and the architectural considerations required for developing a personalized virtual learning environment, can assist personalized eLearning from a distance education perspective. With the new techniques and methodologies, the personalized virtual learning environments can have significant impact on distance education.

In future research, we will focus on the following: (i) to update our personalization model by looking at interactive effect between recognition and reaction. The Learner’s planning in reaction stage may have interactions with the learner’s model in the recognition stage. When updating the learner’s new plan, more information may be required from the learner’s model or even from the profiling state. Therefore, the data or information flow between these stages and the updated personalization model will become bi-directional. It will provide more flexibility to meet the dynamic eLearning situation, (ii) to develop advanced intelligent agent and multi-agent architecture based on the new personalization model, and (iii) to develop a real-world application followed by a field experiments.

## Acknowledgements

The authors would like to thank Mr. Jiarui Ni who provided valuable help in system development, and Dr. Maggie Wang who gave valuable discussion in intelligent agent applications.

## References

[1] F.N. Akhras, J.A. Self, Beyond intelligent tutoring systems: situations, interactions, processes and affordances, Instructional Science 30 (1) (2002) 1– 30.

[2] M. Alavi, D.E. Leidner, Research commentary: technologymediated learning — a call for greater depth and breadth of research, Information Systems Research 12 (1) (2001) 1 – 10.

[3] C. Ames, Classrooms: goals, structures, and student motivation, Journal of Educational Psychology 84 (3) (1992) 261 – 271.

[4] L. Aroyo, P. Kommers, Intelligent agents for educational computer-aided systems, Journal of Interactive Learning Research 10 (3/4) (1999) 235–242.

[5] G. Biswas, K. Leelawong, K. Belynne, K. Viswanath, D. Schwartz, J. Davis, Developing learning by teaching environments that support self-regulated learning, Proceedings of Intelligent Tutoring Systems, Springer-Verlag, Berlin, 2004, pp. 730 – 740.

[6] P. Brusilovsky, Course sequencing for static courses? Applying its techniques in large-scale web-based education, Proceedings of Intelligent Tutoring Systems, Montreal, Canada, 2000, pp. 525–535.

[7] R.R. Burton, J.S. Brown, A tutoring and student modelling paradigm for gaming environments, in: P. Lorton Jr. (Ed.), Computer Science and Education, vol. 8, ACM SIGCSE Bulletin, 1976, pp. 236– 246.

[8] C.I.P.d. Carrillo, Intelligent Agents to Improve Adaptivity in a Web-based Learning Environment, Doctoral, University of Girona, 2004.

[9] R. Conejo, E. Guzman, E. Millan, M. Trella, J.L. Perez-De-La-Cruz, A. Rioz, SIETTE: a web-based tool for adaptive testing, International Journal of Artificial Intelligence in Education 14 (2004) 29 – 61.

[10] A. Dufresne, ExploraGraph: improving interfaces to improve adaptive support, Proceedings of International Workshop on Adaptive and Intelligent Web-based Educational Systems, San Antonio, Texas, USA, 2001, pp. 306 – 313.

[11] P. Ehlert, Intelligent user interfaces: introduction and survey, research DKS03-01/ICE 01, Faculty of Information Technology and Systems, Delft University of Technology, 2003.

[12] J.D. Fletcher, Modeling of learner in computer-based instruction, Journal of Computer-Based Instruction 1 (1975) 118 – 126.

[13] T. Govindasamy, Successful implementation of eLearning: pedagogical considerations, The Internet and Higher Education 4 (3–4) (2001) 287– 299.

[14] S.R. Hiltz, M. Turoff, What makes learning networks effective, Communications of the ACM 45 (4) (2002) 56– 59.

[15] S.R. Hiltz, J. Fjermestad, L. Floydlewis, Introduction to the special issue on collaborative learning via Internet, Group Decision and Negotiation 8 (5) (1999) 367–369.

[16] J. Kwok, H.Q. Wang, S. Liao, J. Yuen, F. Leung, Student profiling system for agent-based educational system, Proceedings of American Conference on Information Systems, L.A. USA, 2000, pp. Online.

[17] P. Lassey, Developing a Learning Organization, Kogan Page, London, 1998.

[18] D.E. Leidner, S.L. Jarvenpaa, The use of information technology to enhance management school education: a theoretical view, MIS Quarterly 19 (3) (1995) 265– 291.

[19] J.C. Lester, B.A. Stone, G.D. Stelling, Lifelike pedagogical agents for mixed-initiative problem solving in constructivist learning environments, User Modeling and User-Adapted Interaction 9 (1–2) (1999) 1 – 44.

[20] J.C. Lester, S. Towns, P. FitzGerald, Achieving affective impact: visual emotive communication in lifelike pedagogical agents, International Journal of Artificial Intelligence in Education 10 (1999) 278 – 291.

[21] M. Martinez, Mass customization: designing for successful learning, International Journal of Educational Technology 2 (2) (2001) 3 – 20.

[22] M. Martinez, C.V. Bunderson, Foundations for personalized web learning environments, ALN Magazine 4 (2) (2000) (December, pp. online).

[23] M. Martinez, D.V. Bunderson, Building interactive world wide web (Web) learning environments to match and support individual learning differences, Journal of Interactive Learning Research 11 (2) (2000) 163–195.

[24] S. Ohlsson, Some principles of intelligent tutoring, Instructional Science 14 (1986) 293–326.

[25] M. O’Loughlin, Rethinking technology: beyond Piagetian constructivism toward a socio-cultural model of teaching and learning, Journal of Research in Science Teaching 29 (8) (1992) 791–820.

[26] T. Russell, Technology wars: winners and losers, Educom Review 32 (2) (1997) 44–46.

[27] C.T. Santos, F.S. Osorio, Integrating intelligent agents, user models, and automatic content categorization in a virtual environment, Proceedings of Intelligent Tutoring Systems, Springer-Verlag, Berlin, 2004, pp. 128 – 139.

[28] V.J. Shute, SMART: student modeling approach for responsive tutoring, User Modeling and User-Adapted Interaction 5 (1) (1995) 1 – 44.

[29] J. Siemer, M.C. Angelides, A comprehensive method for the evaluation of complete intelligent tutoring systems, Decision Support Systems 22 (1) (1998) 85 – 102.

[30] C.C. Tsai, Relationships between student scientific epistemological beliefs and perceptions of constructivist learning environments, Educational Research 42 (2) (2000) 193– 205.

[31] H. Wang, LearnOOP: an active agent-based educational system, Expert Systems with Applications 12 (2) (1997) 153 – 162.

[32] H. Wang, SQL Tutor+: a co-operative its with repository support, Information and Software Technology 39 (1997) 343– 350.

[33] H. Wang, C. Wang, Intelligent agents in the nuclear industry, IEEE Computer 30 (11) (1997) 28 – 34.

[34] H. Wang, J. Mylopoulos, S. Liao, Intelligent agents and financial risk monitoring systems, Communications of the ACM 45 (3) (2002) 83– 88.

[35] M. Wooldridge, Intelligent agents, in: G. Weiss (Ed.), Multiagent Systems, The MIT Press, London, England, 1999, pp. 25–77.

[36] M. Wooldridge, N. Jennings, Intelligent agents: theory and practice, The Knowledge Engineering Review 10 (2) (1995) 115 – 152.

[37] D. Xu, Intelligent Agent Supported Personalization for Virtual Learning Environments, Ph.D., City University of Hong Kong, 2003.

[38] D. Xu, H. Wang, Intelligent student profiling with fuzzy models, Proceedings of 35th Annual Hawaii International Conference on System Sciences, Hawaii, USA, 2002, p. 81b.

[39] D. Xu, H. Wang, Multi-agent collaboration for B2B workflow monitoring, Knowledge-Based Systems 15 (8) (2002) 485– 491.

[40] D. Xu, L. Ge, D. Ni, H. Wang, An intelligent online learning system: development and evaluation, Proceedings of Seventh Americas Conference on Information Systems, Boston, USA, 2001, pp. 134 – 137.

[41] R.R. Yager, Target on E-commerce marketing using fuzzy intelligent agents, IEEE Intelligent System 15 (6) (2000) 42 – 45.

[42] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1965) 338 – 353.

[43] L.A. Zadeh, Fuzzy logic = computing with words, IEEE Transactions on Fuzzy Systems 4 (2) (1996) 103– 111.

[44] D. Zhang, J.K. Nunamaker, Powering E-learning in the new millennium: an overview of e-learning and enabling technology, Information Systems Frontiers 5 (2) (2003) 207– 218.

[45] Z. Zhang, C. Zhang, Agent-Based hybrid intelligent systems, in: Jorg. Siekmann (Ed.), Lecture Notes in Artificial Intelligence, 1 ed., Springer-Verlag, Berlin, 2003.

Dongming Xu received his PhD degree from the City University of Hong Kong in 2004. Currently, she is a lecturer in the Business School at the University of Queensland. Her research interests include applications of artificial intelligence on business information systems, in particular, specializing on Web-based intelligent agents and their applications, such as workflow management systems, knowledge management systems, models of virtual markets, intelligent virtual learning environments and intelligent Web services.

Huaiqing Wang is a professor in the Information Systems Department at the City University of Hong Kong. He specializes in research and development of business intelligence systems, intelligent agents and their applications (such as multiagent supported financial information systems, virtual learning systems, knowledge management systems, and conceptual modeling). He received his PhD in computer science from the University of Manchester in 1987.
