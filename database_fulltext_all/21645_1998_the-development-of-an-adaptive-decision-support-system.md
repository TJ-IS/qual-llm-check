---
otero_id: 21645
otero_key: "BQZ8PEBS"
title: "The development of an adaptive decision support system"
authors: "Ta-Tao Chuang; Surya B Yadav"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00065-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The development of an adaptive decision support system <sup>1</sup>

Ta-Tao Chuang <sup>a,)</sup>, Surya B. Yadav <sup>b,2</sup>

Department of Decision Sciences, Wichita State UniÕersity, Wichita, KS 67260, USA <sup>b</sup> Area of ISQS, Texas Tech. UniÕersity, Lubbock, TX 79409, USA

Accepted 16 September 1998

## Abstract

An integrated conceptual model of an adaptive decision support system ADSS is proposed by following a unified Ž . research methodology. Adaptive behaviors of the DSS are identified based on previous research into adaptivity of information systems. A variety of knowledge that enables the system to adaptively behave is recognized. The concept of a reflexive system and a conceptual framework of decision-making organization are adopted to structure various components. This model consists of several components at two levels: the meta-level and the basic-level. The components in the basic-level unit communicate with the user and carry out the task of decision support. The meta-level is a controlling unit capable of introspecting the system’s capabilities and limitations, and determining an appropriate action to adjust the capabilities of components in the basic-level unit. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Adaptive decision support systems; Decision support systems; Adaptive behavior; Knowledge level; Reflexive systems

## 1. Introduction

Today’s business environment is diverse and dynamic. A decision maker needs a system that can support him in different problem situations. In other words, we need a decision support system that adapts itself to the changing needs of a decision maker. This article proposes an integrated conceptual model of such an adaptive decision support system ADSS .Ž . This model incorporates architectural components that make the system amenable to self-learning and adaptation. The model builds upon the work done in the areas of learning, decision-making, and software agent. We use the concept of a feedback-driven learning process 15 , a conceptual framework of organization of decision-making 32 , and the con- <sup>w</sup> <sup>x</sup> cept of a reflexive system 21 in developing this<sup>w</sup> <sup>x</sup> model.

The article is organized in the following manner. First, the evolution of ADSS research is briefly presented and the need for an integrated model is discussed. Second, research in relevant areas is reviewed. After that, the development of the conceptual model is presented following a unified research methodology 4 . Finally, the model is validated by demonstrating how it works and by comparing it with extant models. This is followed by a discussion of our future research.

## 1.1. Background

The term ‘adaptive decision support systems Ž . ADSS ’ was coined by Holsapple et al. 25 to<sup>w</sup> <sup>x</sup> represent a category of decision support systems Ž . DSS capable of self-teaching, which is accomplished by equipping systems with unsupervised inductive learning methods. One distinguishing feature of the systems in this category is that they are able to generate a better solution to a problem by gradually refining an initial solution 25 . While this feature is <sup>w</sup> <sup>x</sup> beneficial to the decision maker, the systems defined by Holsapple et al. 25 fail to fulfil the potential of<sup>w</sup> <sup>x</sup> the concept of adaptivity because the other components, such as user interfaces, of a DSS have not been taken into consideration in defining ADSS.

A general notion about a DSS is that it is an interactive computerized system consisting of three major components: a dialog subsystem, a database subsystem, and a model base subsystem 57 ; or, an<sup>w</sup> <sup>x</sup> interface subsystem, a knowledge subsystem, and a problem processing subsystem 8,26 . With the<sup>w</sup> <sup>x</sup> knowledge and other capabilities embodied in these components, a DSS is intended to help a decision maker interactively solve managerial decision problems. The three-component architecture is capable of managing data; fitting data into models; and providing methods to reach decisions 2 . By manipulating<sup>w</sup> <sup>x</sup> models and data, the decision maker is able to examine various scenarios and their consequences. The user interface component, which may be individually tailored to the user’s preferences and expertise, lends itself to being a friendly and effective communication facility. The three components, as a whole, contribute to the quality of decisions that are taken by a decision maker.

Nevertheless, a system based on the above architecture mainly provides passive rather than active or intelligent support for decision-making 29,31 . A<sup>w</sup> <sup>x</sup> system which provides passive decision support barely achieves its design objectives as the user’s experiences, knowledge, and expertise change.

Changes in environments make a DSS that initially completely meets the design objectives obsolete. Furthermore, the increasing complexity and diversity of managerial environments require that a DSS not only take an active role, but also be able to adapt to changing needs of decision makers. These considerations have led to attempts to improve the usability and<sup>r</sup>or the functionality of a DSS by strengthening its three components.

With the advent of artificial intelligence AI andŽ . expert system ES techniques, it has been broadlyŽ . recognized that it is possible to empower a DSS by incorporating these techniques into the system <sup>w</sup> <sup>x</sup> 2,20,23,24,26,31,38,45,54 . Such techniques can be incorporated into each component of the DSS 25,54 ,<sup>w</sup> <sup>x</sup> and, accordingly, the performance of that strengthened component can be improved. For example, transition network and ES are suggested for designing an adaptive user interface 27 . More often, AI <sup>w</sup> <sup>x</sup> and ES techniques are integrated into the problem processing component in order to enhance the functionality of DSS 1,15,16,19,25,28,29,31,39,40,<sup>w</sup> 44,46,49 . ADSS is a variant of the resulting inte- <sup>x</sup> grated systems 1,15,16,25,28,44 . The design objec- <sup>w</sup> <sup>x</sup> tive of existing ADSS is to refine solutions to a given problem 25 or to induce decision rules from <sup>w</sup> <sup>x</sup> historical cases by using inductive learning methods <sup>w</sup> <sup>x</sup> 16 .

Nonetheless, the extant concept of and research in ADSS have several shortcomings. Conceptually, research in adaptive systems suggests that adaptive systems should be able to modify some aspects of their structure, functionality, or interface to meet different needs in their environments 6 . The current<sup>w</sup> <sup>x</sup> concept of ADSS exclusively focuses on the functionality of the DSS. This may fail to fulfil the potential of the concept of adaptation. Technically, even though it is possible to enhance the three components of the DSS with AI and ES techniques <sup>w</sup> <sup>x</sup> 25,54 , the existing research in ADSS emphasizes examining the feasibility of using an unsupervised inductive method as the adaptivity-enabling mechanism.

Following the notion of adaptive systems 6 , we<sup>w</sup> <sup>x</sup> define an ADSS as a DSS that is able to automatically or manually modify some aspects of its structure, functionality, or interface to meet different needs in its users. Based on this definition, the following sections formulate the research problem and indicate the research objective.

## 1.2. Problem statement

Paraphrasing the three points used by Atkinson et al. 3 to characterize the situation of object-oriented<sup>w</sup> <sup>x</sup> database systems, we can describe the status of ADSS research as follows: 1 it lacks a commonŽ . architecture; 2 it lacks theoretical foundations; andŽ . Ž . 3 it is application-dependent.

Unlike the traditional DSS model, which is based on the DMM paradigm 26,57 , ADSS does not have<sup>w</sup> <sup>x</sup> a widely accepted architecture. Even though several architectures or models of ADSS have been proposed 25,44 , they are mainly an extension to the <sup>w</sup> <sup>x</sup> traditional three-component architectures 26,57 ,<sup>w</sup> <sup>x</sup> which in turn are based on Simon’s decision-making model 50 . According to Angehrn and Jelassi 2 ,<sup>w</sup> <sup>x</sup> <sup>w x</sup> the wide employment of Simon’s model ‘has become an obstacle for the evolution of DSS theory and practice’ p. 269 . Recent research 2,31 indi-<sup>w</sup> <sup>x</sup> <sup>w x</sup> cates that in order to bring more support to the manager in a dynamic environment and promote DSS research, the intellectual base of DSS must be augmented and research should be done to provide a theory-laden framework. But there is no comprehensive framework available yet, let alone a theory-laden framework.

Most extant research into the adaptivity of DSS falls into one or two of the following areas: 1 theŽ . development of an ADSS supporting a particular application 1,14,25,44 ; 2 the knowledge level<sup>w</sup> <sup>x</sup> Ž . and<sup>r</sup>or design of an adaptive interface 18,34,<sup>w</sup> 35,37,55 ; 3 the design of an adaptive model and<sup>x</sup> Ž . <sup>r</sup>or knowledge base 14,16,25,44 ; 4 the design of an<sup>w</sup> <sup>x</sup> Ž . adaptive help system 34,51,55 ; and 5 the adaptive<sup>w</sup> <sup>x</sup> Ž . design of DSS 30,36 .<sup>w</sup> <sup>x</sup>

An investigation into previous research shows that each research effort has focused on only one or two facets of an ADSS to the exclusion of others.

## 1.3. Research objectiÕes and research issues

The objective of this research is to propose an integrated conceptual model of ADSSs adaptive to changes in environments. In particular, this article aims to address the following issues:

2. What knowledge and other capabilities are required of an ADSS to enable adaptive behavior?

3. What architecture is required to support these capabilities?

A unified approach to AI-related research 4 is<sup>w</sup> <sup>x</sup> followed to address these issues and to guide systematically the development of the conceptual model.

## 2. Related work

Research concerning ADSSs can be divided into four areas: adaptive user interface, adaptive problem domain knowledge, adaptive help facilities, and adaptive design. Research in adaptive design will not be reviewed here because an adaptive design process does not necessarily produce an adaptive system. Moreover, an adaptive design process may be accomplished through an adaptive interface 36,37 . <sup>w</sup> <sup>x</sup>

## 2.1. AdaptiÕe user interface

According to Totterdell and Rautenbach 52 , re-<sup>w</sup> <sup>x</sup> quirements for a system adaptive to the user include: an underlying theory associated user behavior to interface needs, an access to behavioral cues, a variety of user interface design, and models accumulating behavioral cues and representing a particular need. Previous research on adaptive user interface system has been focused on adaptation techniques and modeling issues. Various adaptation techniques have been proposed: genetic algorithm 53 ; adaptive<sup>w</sup> <sup>x</sup> scheduling and pattern matching 11,27,37,53,55 ;<sup>w</sup> <sup>x</sup> and discourse modeling and user modeling 53 .

Several kinds of knowledge are needed for the system to behave adaptively 10,18,27,35,37,43 .<sup>w</sup> <sup>x</sup> These kinds of knowledge are captured in the following models: 1 User models: capture knowledgeŽ . about the user for the system to respond to the needs of the user 11,18,35,42,55 . 2 Domain models:<sup>w</sup> <sup>x</sup> Ž . represent the features of a certain domain that is outside the system and that is interesting to the user <sup>w</sup> <sup>x</sup> 18,35,42,55 . 3 System models: hold the knowl-Ž . edge, capabilities, assumptions and limitations of the system itself 18,35,42 . 4 Task models: contain a<sup>w</sup> <sup>x</sup> Ž . static representation of tasks that can be done with the system and<sup>r</sup>or a dynamic interaction between the user and the system 35,42,55 . 5 Interaction<sup>w</sup> <sup>x</sup> Ž . models: possess the dynamic representation of the dialog between the user and the system 42 . <sup>w</sup> <sup>x</sup>

It should be noted that the static representation of tasks can be part of a domain model 6,7 . Also,<sup>w</sup> <sup>x</sup> dynamic interaction processes usually vary from one user to another and, thus, the dynamic interaction between the user and the system can be part of user models.

## 2.2. AdaptiÕe problem domain knowledge

The research into adaptive problem domain knowledge mainly examines the possibility of developing a DSS capable of self-teaching so as to acquire or refine knowledge with the least help from external agents 28 . A typical approach is to equip the prob- <sup>w</sup> <sup>x</sup> lem solving component of the DSS with a learning method 25 or to add an additional learning compo- <sup>w</sup> <sup>x</sup> nent to the extant DSS model 44 . Among these<sup>w</sup> <sup>x</sup> learning strategies suggested 38 , the inductive <sup>w</sup> <sup>x</sup> learning strategy appears to be the most promising <sup>w</sup> <sup>x</sup> 16,25,44 . By using this strategy, knowledge is inductively learned from examples, simulation results, or historical cases. Knowledge acquisition and refinement is the focus of this line of research. Similar concerns can be found in research in knowledgebased systems.

El-Najdawi and Stylianou 19 propose a model of <sup>w</sup> <sup>x</sup> an expert support system, which is a problem-solving community consisting of different experts. Various learning methods are suggested to make the system adaptive.

In addition to learning methods, learning automata 15 , neural networks 16 , and case-based<sup>w x</sup> <sup>w x</sup> reasoning 17 are used as alternatives for enabling <sup>w</sup> <sup>x</sup> knowledge-based systems to be adaptive.

Deng and Chaudhury 15 propose a conceptual<sup>w</sup> <sup>x</sup> model of adaptive knowledge-based systems by integrating a learning automata into the operational schema of the traditional expert system. The model assumes that the performance evaluation and the learning behavior of the system are stochastic processes in nature. Based on the previous state, previous experiences, and the evaluation results, the system is capable of adapting domain knowledge to external changes 15 . A disadvantage of this ap- <sup>w</sup> <sup>x</sup> proach is that knowledge states and state transition probability matrix must be available for the design of such systems. This may not be true.

Deng 16 proposes a connectionist inductive in-<sup>w</sup> <sup>x</sup> ference model, which combines a neural network and an inductive inference mechanism. The inductive inference mechanism consists of a feature-detecting module and a rule induction module. The feature-detecting module remedies the deficiency that the inductive learning method becomes time-consuming when the number of decision variables is large. However, the effectiveness of the feature-detecting technique decreases when decision regions largely overlap. The neural network module is used to overcome this shortcoming.

Deng 17 suggests that an adaptive case-based<sup>w</sup> <sup>x</sup> reasoning model is particularly appropriate for the decision-making context in which online interactive feedback is necessary for incorporating new information into the problem solving process. Instead of inducing decision rules from training cases, Deng’s model 17 directly works on the data file. A signifi- <sup>w</sup> <sup>x</sup> cant feature of this model is that it is capable of handling nominal and quantitative data.

## 2.3. AdaptiÕe help systems

The design objective of an adaptive help system is to adjust ‘the help facilities to either the task context or to specific user preferences’ 34, p. 68 . This <sup>w</sup> <sup>x</sup> objective is similar to that of adaptive user interfaces. Consequently, adaptive help systems may be part of adaptive user interfaces. Previous research <sup>w</sup> <sup>x</sup> 11 on adaptive help systems is focused on user modeling and tailoring help facilities to meet users’ needs according to the level of the user’s knowledge about the system. Another research focus is on the characteristics of adaptive help systems. According to 5 , cited by 34 , adaptive help systems can be<sup>w x</sup> <sup>w</sup> <sup>x</sup> classified by the following dimensions: passive or active, context-independent or -dependent, and userindependent or -sensitive 34 . This classification is<sup>w</sup> <sup>x</sup> applicable to adaptive user interfaces.

This review shows that each research effort usually addresses one or two facets of adaptivity of the DSS. An integrated comprehensive model is needed for taking into account these facets.

## 3. Development of a conceptual model of an ADSS

Based on previous research into the adaptivity of the DSS, this section, first, identifies the adaptive behaviors of ADSS. Next, the knowledge and other capabilities driving the adaptive behaviors are presented. Finally, an integrated conceptual model of an ADSS is proposed based on the adaptive behavior and knowledge.

## 3.1. AdaptiÕe behaÕior of an ADSS

The major characteristic of the system behavior of ADSS is adaptation. This characteristic can be regarded as a general goal in the knowledge-level 41 . <sup>w</sup> <sup>x</sup> The ramifications of the general goal i.e., variousŽ adaptive behaviors should be identified so that dif-. ferent forms of knowledge required for achieving the general goal can be recognized.

As mentioned previously, much research 7,9,<sup>w</sup> 11,18,27,33,37,55 has been done in developing <sup>x</sup> adaptive user interfaces to accommodate the heterogeneity and evolution of user characteristics. One of the underlying assumptions for adapting a user interface to the user’s preferences is that the fit between both brings greater satisfaction to the user and thus improves the decision quality and the performance of the user. Based on the same rationale, an ADSS should demonstrate similar behavior in this respect. That is, an ADSS should be of multiple presentation modes.

In addition, previous research has suggested that an adaptive knowledge-based system or adaptive problem solving system should be able to adapt its knowledge to the dynamic of its environments 15, 16,44 or gradually refine a solution to a given problem 25 . The former perspective suggests that<sup>w</sup> <sup>x</sup> given a particular environment, there exists a corresponding knowledge state which tends to generate better solutions to a problem in that environment than do other knowledge states. As a result, an ADSS should have a variety of knowledge states in order to provide supports for decision makers facing various problem situations.

With the advent of information technology, the amount of data that is collected, stored, and retrieved is exploding. The aggregate of data allows the decision maker to induce decision rules 16 for similar<sup>w</sup> <sup>x</sup> problem situations or multidimensionally examine the underlying relationships among data 22 . Multi-<sup>w</sup> <sup>x</sup> dimensional analysis helps the decision maker explore business opportunities or formulate problems.

This feature is especially important during the initial stages of the decision-making process. At the early stages of the process, the decision maker needs more support in understanding the problem and exploring the opportunities. Problems or opportunities can be exposed by examining different underlying relationships among data, each of which represents a view of the data. Therefore, an ADSS should be of multiple views.

Finally, the design of an adaptive user interface system is affected by the problem domain, which is usually modeled as one component of the adaptive user interface system 18,55 . Consequently, when<sup>w</sup> <sup>x</sup> new knowledge for a novel problem situation is acquired, it appears necessary to adjust the user interface. An ADSS should provide support for designing such a user interface with the least help from the decision maker.

Based on the above discussion, the desired adaptive behavior can be summarized as follows.

Ž . 1 Multiple modes: An ADSS should be able to support multiple presentation modes to accommodate the heterogeneity of users. Given a particular user engaged in a particular problem situation, an individually tailored presentation mode should be provided for the user.

Ž . 2 Multiple views: An ADSS should be of multiple views for the user to explore different underlying relationships among data.

Ž . 3 Multiple scenarios: Like traditional DSS, an ADSS should be able to support the decision maker for performing ‘what if’ analysis of various scenarios.

Ž . 4 Different problem situations: With the least help from the user, an ADSS should be able to generate various knowledge states for various problem situations within the problem domain and support the decision maker in different problem situations.

Ž . 5 Self-moderation: After new knowledge is acquired and user interfaces for the problem situation are composed, an ADSS should be able to associate the new knowledge with the interfaces. Subsequently, the ADSS can adjust its presentation modes when the new knowledge is used in the problem situation.

These adaptive behaviors can be regarded as a set of subgoals of the general goal of adaptation in the knowledge level 41 . In order to achieve these goals,<sup>w</sup> <sup>x</sup> different kinds of knowledge should be captured in the system to perform the required actions for accomplishing the goals.

## 3.2. Knowledge and capabilities of an ADSS

It is generally agreed that the following categories of knowledge should be captured in an adaptive system: knowledge about the user, knowledge about tasks, knowledge about problem domains, and knowledge about the systems 1,6,7,10,18,35,42,43 .<sup>w</sup> <sup>x</sup> While a few of these forms of knowledge can serve the purpose of the present research, the meanings of these categories vary from one research effort to another. The following types of knowledge are required for supporting the identified behavior.

Ž . 1 Meta-knowledge: is ‘knowledge about what we know or can know, or knowledge about how to use the knowledge that we have’ 47, p. 14 . It is<sup>w</sup> <sup>x</sup> required for the system to be able to self-moderate, and to adapt itself to different problem domain situations. The meta-knowledge includes a range of types of knowledge about other forms of knowledge as well as knowledge about relationships between different types of meta-knowledge. Specifically, there are, at least, three types of meta-knowledge: iŽ . problem domain meta-knowledge, ii user interfaceŽ . meta-knowledge, and iii knowledge about the rela-Ž . tionship between problem domain knowledge and user interface knowledge.

Ž . 2 User knowledge: is knowledge about the user who is working on the problem domain with the ADSS. User knowledge is necessary for the system to be of multiple modes because the system must adapt its presentation modes to the current status of the user facing a particular problem situation. Specifically, user knowledge include: i knowledge aboutŽ . the user’s knowledge of the problem domain or the task 1,18,27 ; ii knowledge about the user’s exper- <sup>w</sup> <sup>x</sup> Ž . tise with the system 1,18 ; and iii Knowledge <sup>w</sup> <sup>x</sup> Ž . about the user’s preference for interface 1,18,55 .<sup>w</sup> <sup>x</sup>

Ž . 3 Interface element knowledge: is knowledge about interface elements. It is required for the system to compose user interfaces, which are used to support the behavior of multiple modes and multiple views. Interface elements can be classified into four levels: the component level, the collection level 13 ,<sup>w</sup> <sup>x</sup> the screen layout level, and the application level.

Ž . 4 Problem domain knowledge: is knowledge about the problem domain upon which the system is designed and the user is seeking support for decision-making. Problem domain knowledge is obviously necessary for the system to fulfil its purpose. In addition, it is necessary for the system to adapt to different problem situations and to present multiple views among data. Problem domain knowledge include the following: i descriptive knowledge 26Ž . <sup>w</sup> <sup>x</sup> or structural knowledge 47 : refers to factual obser-<sup>w</sup> <sup>x</sup> vations about entities or objects in the problem domain and describes the types of entity or the state of the problem domain; ii reasoning knowledge: con- Ž . cerns the relationship between the entities in the problem domain and explains the cause–effect relationship by which a conclusion can be drawn given that a specified condition exists 26 ; and iii prob-<sup>w</sup> <sup>x</sup> Ž . lem domain procedural knowledge: concerns a stepby-step procedure for accomplishing certain tasks <sup>w</sup> <sup>x</sup> 26 and<sup>r</sup>or the knowledge about how to use the first two categories of problem domain knowledge to solve a particular problem in the domain 47 .<sup>w</sup> <sup>x</sup>

Ž . 5 Presentation knowledge: refers to the knowledge that the system uses to organize interface layout for a particular user engaged in a particular problem solving session. Presentation knowledge is necessary for the system to provide a presentation mode for a particular user in a particular problem situation. Thus, presentation knowledge helps realize the multiple modes behavior. Presentation knowledge accommodates the dual natures of prescriptive and descriptive knowledge. Given a problem situation, there exists a set of the most effective user interfaces for the system to communicate with the user who has certain characteristics. This may refer to prescriptive user interface in a given problem situation. However, the user may prefer another user interface to the prescriptive one. This particular user interface is descriptive in nature. Presentation knowledge might be derived from user characteristics knowledge, problem domain knowledge, and interface component knowledge.

Ž . 6 Learning-methods knowledge: is knowledge about the features and applicability of learning methods. Learning method knowledge is necessary for the system to exercise different learning strategies so as to acquire and refine knowledge. Regarding problem domain knowledge, learning may take place when a certain state of the problem domain knowledge is not sufficient to solve the problem in question. Similarly, learning may be necessary when the existing state of user knowledge cannot sufficiently represent the user’s current status. There are two categories of learning methods: machine learning and human learning methods 48 . This model mainly is equipped<sup>w</sup> <sup>x</sup> with human learning methods, which include: the object level learning, the association level learning, the exemplar level learning, the prototype level learning, the concept combination learning, and the problem solving level learning 48 .<sup>w</sup> <sup>x</sup>

Ž . 7 Interface composition method knowledge: is about how to compose a meaningful user interface by organizing interface elements. The system must have interface composition knowledge in order to compose various presentation modes for a particular problem domain. In order to adapt user interface to the user’s preference, the system should possess mechanisms for organizing interface elements. There are four different ways to create a user interface: iŽ . the component level, ii the collection level, iii the Ž . Ž . screen layout level, and iv the application levelŽ . <sup>w</sup> <sup>x</sup> 13 .

Ž . 8 Model knowledge: is knowledge about various models, which are usually generic problem solving models and<sup>r</sup>or instrumental models. Model knowledge is helpful when the system needs to adapt to different problem situations and<sup>r</sup>or present multiple views among data.

An ADSS utilizes these forms of knowledge to adjust its behaviors corresponding to the changing needs of the decision maker. In Section 3.3, we present an integrated conceptual model depicting the relationships among these forms of knowledge and describe how the model works.

## 3.3. A conceptual model of an ADSS

The conceptual model of an ADSS is proposed based on the criterion of relationship 32 and the<sup>w</sup> <sup>x</sup> concept of reflexive system 21 . The criterion of<sup>w</sup> <sup>x</sup> relationship suggests that the components part sys-Ž tems of a system can be organized and coordinated. together according to their relationship 32 . Based <sup>w</sup> <sup>x</sup> on this criterion, the part systems inside the ADSS are determined as follows: a problem-domain subsystem, an interface subsystem, and a system selfknowledge subsystem. We adopt a control perspective to coordinate these three units since ‘coordination is the control of the part systems of the decision-making system’ 32, p. 150 . The control perspective is consistent with that of a reflexive system 21 .<sup>w</sup> <sup>x</sup>

A reflexive system consists of a basic-level unit, a meta-level unit, and two operations: reification and denotation 21 . The basic-level unit is the operating<sup>w</sup> <sup>x</sup> unit capable of carrying out the decision made by the meta-level unit. The meta-level unit is a controlling unit capable of observing the activities taken by the basic-level unit, looking into the system’s own knowledge, and determining appropriate actions, which is carried out by the basic-level unit. The capability of the meta-level unit is called introspection. Reification refers to the operation that transfers the execution of the system from the basic-level unit to the meta-level unit. Conversely, denotation is the operation that transfers the execution of the system from the meta-level unit to the basic-level unit. Based on these concepts and that of a feedback-driven learning process 15 , we propose a conceptual model <sup>w</sup> <sup>x</sup> of an ADSS as in Fig. 1.

The rest of the section discusses functions of each component and how these components work together to provide support for decision-making. Given the current status of information technology, it is impossible for the system to automatically carry out each action described below. Thus, processes described below are synergistically carried out by the system and the user.

The different forms of knowledge identified in the last section are captured and stored in this model as shown in Fig. 1. It should be noted that knowledge about a particular form of knowledge, model, or data base i.e., meta-knowledge is stored with thatŽ . knowledge, even though Fig. 1 does not show this. The self knowledge in the meta-level unit includes: Ž . 1 all of the meta-knowledge in the basic-level unit, Ž . 2 knowledge about the relationships between various components, 3 knowledge about relationship Ž . between problem domain knowledge and presentation modes, and 4 knowledge about strengths andŽ . weaknesses of process components, such as learning strategies and interface composition methods in the formalizing system.

![](/api/attachments/BQZ8PEBS/fulltext/images/381cbbef90675001d1aadf6b25134050e8d8de8fca39452665dc119e234e3c70.jpg)  
Fig. 1. A conceptual model of an adaptive decision support system.

The learning system possesses different learning methods, including object level learning, association level learning, exemplar level learning, prototype level learning, concept combination learning, and problem solving level learning 48 . These learning<sup>w</sup> <sup>x</sup> methods correspond to different levels of knowledge structure: object level, relations between object pair level, category level, abstract concept level, complex concept level, and problem solving capability level. The invocation of these learning methods follows a hierarchical sequence 48 . The knowledge acquired <sup>w</sup> <sup>x</sup> by lower level learning methods is the basis for higher level learning methods to acquire higher level knowledge structure. In the process of knowledge acquisition, a learning method might be invoked following a learning method at the next lower level. When necessary, the human learning approach might be complemented by supervised and unsupervised machine learning strategies, such as learning by memorization, learning by induction, learning by deduction, and learning by analogy 38 . When the<sup>w</sup> <sup>x</sup> current knowledge in the system is not sufficient to solve the problem under study, depending on the nature of the problem, a particular learning method may access the data base, the model base, or the problem domain knowledge base to generate new knowledge, which is then assimilated into the problem domain knowledge base.

The problem processing system is similar to the inference engine in expert systems. Upon receipt of user input, it uses decision rules or heuristics in the problem domain knowledge base to solve the problem. When necessary, it also accesses the data base for historical data and<sup>r</sup>or model building blocks for appropriate models. Another function of the problem processing system is to transfer the execution of the system to the meta-level unit when no appropriate decision rules or heuristics are found to solve the problem under study. As Fig. 1 shows, the problem processing system communicates with the user via the dialog system.

Upon receipt of a message from the problem processing system, the introspection module in the meta-level unit consults the self knowledge and invokes a learning method appropriate for the current problem. The choice of a particular learning method depends on the nature of the problem and the selfknowledge. When there are significant changes in problem domain knowledge, another opportunity for reification occurs so as to update the self-knowledge.

In other words, when the system faces a novel problem, two passes of reification occur. On the first pass, the problem processing system passes the nature of the problem to the introspection module, which decides a learning method, according to the nature of problem and the self knowledge. The learning method may use historical cases in the data base, models from the model building blocks, and problem domain knowledge to generate new knowledge or decision rules. The generated knowledge is then assimilated into the domain knowledge base. When this occurs, the problem processing has to invoke the introspection module again and transfers the nature of the knowledge to the introspection module in order to update the self-knowledge. In addition, it may trigger denotation an interface compositionŽ . method in the formalizing system to update the knowledge of the presentation mode since the appropriateness of presentation modes depends on user profile, interface elements, and the nature of the problem domain knowledge. The performance of the problem processing system in supporting a particular decision should be evaluated and the evaluation results are feedback into the data base.

Triggered by the introspection module, an interface composition method in the formalizing system generates presentation knowledge depending on the user profile, interface elements, and the nature of new problem domain knowledge, which is conveyed to the triggered composition method through the denotation operation by the introspection module. The generated presentation knowledge is assimilated into the presentation knowledge base.

The dialog generation and management system Ž . Ž . DGMS performs several tasks: 1 it captures the user’s preferences, expertise, and skills, which are saved as a user model in the user profile; 2 itŽ . receives and interprets the user’s input, which is conveyed to the problem processing system; 3 it Ž . presents the results to the user; and 4 it triggers theŽ . introspection module when necessary. The purpose of most of these tasks is self-evident since how this model operates has been explained. However, the circumstances under which the introspection module should be invoked need to be further explained. In general, when the system faces a new user, the DGMS has to trigger the introspection, which consults the self knowledge to choose an interface composition method in the formalizing system to adapt the presentation knowledge according to the new user’s characteristics, preferences, experiences, and expertise. By ‘a new user’, we mean that there exists unconformity between the user and user models in the user profile such that there is no presentation knowledge available. A ‘new’ user may result from turnover, becoming more experienced, gaining more expertise, or changing his<sup>r</sup>her preferences. Two situations are associated with a new user: a new user with a new task and a new user with an old task. In the former case, the system will do the jobs in the problem-processing-unit first and then proceed to the jobs in the interface-unit because the result of problem solving or the problem domain knowledge partially determines the presentation mode appropriate for the results. In other words, the reification in the problem-processing-unit occurs earlier than does that in the interface-unit. In the case of a new user with an old task, only the reification in the interface-unit may occur because the domain knowledge is presumably available for an old task. Fig. 2 shows how the ADSS operates.

![](/api/attachments/BQZ8PEBS/fulltext/images/7707daa2b41b3c50e8dbeaf3b69dcaca4d0191237c4509061010a958ec30e4e4.jpg)  
Fig. 2. A system flowchart of the adaptive decision support system.

## 4. Validation of the conceptual model of ADSS

In this section, the proposed model will be logically validated by comparing certain features of the model with those of several ADSS models. Before that, we use an example to illustrate how this model works.

## 4.1. An illustration

A real estate agent uses an ADSS to find a best-matched house for a buyer. The overall goal of the agent is to meet her client’s needs as soon as possible while earning the highest possible commission.

The agent searches for a house based on the criteria provided by her client. Common criteria include: price, area, number of bedrooms<sup>r</sup>baths, condition, location, financing, structure, covered<sup>r</sup> uncovered garage, and down payment. Some criteria may conflict with one another and may be intangible in some cases. In order to resolve conflicting criteria, models of multiple criteria decision-making MCDMŽ . <sup>w</sup> <sup>x</sup> 58 are suggested by the system to the user for evaluating various alternatives against the client’s needs. Models of MCDM allow the agent to evaluate the client’s multiple conflicting criteria and reach the best decision. The system can accept relative weights for the criteria and produce an overall ranking. Also, the system is capable of performing a sensitivity analysis, changes in relation to weights of the criteria affecting the ranking. Data from the agent’s clients and related variables are kept in a database of the system. A local real estate board maintains a database on houses ‘for sale’. The agent’s system uses the same database structure as that of the real estate board database to organize its data.

In the past, the agent has successfully used various MCDM models to serve her clients. These models are saved as part of the problem domain knowledge. The agent’s experience tells her that most of her clients cannot weigh their criteria transitively or consistently. One of the significant features of these models is that they can shorten the search path and provide the highest possible commission subjected to various combinations of criteria. The user interface of the system is supported by various interface elements, including graphics, charts, tables, text, and multimedia. As an experienced user, the agent has been comfortable to describe conditions with such vague descriptions of real estate as good, average, or poor. Most of the time, the agent can reach good decisions very well with help from the system even though the system merely provides short textual descriptions of a transaction.

Occasionally, the agent comes across a good deal on a house, but because of various reasons e.g., theŽ remodeling needs , it is difficult to find buyers. In. order to capitalize her investment and maximize her profit, the agent decides to establish a brokerage firm, which allows her to buy, remodel, and sell estates. Now, the agent wants the system to provide some support in appraising the value of an estate, while the agent does not know how the system can help her in this aspect. The agent decides to explore the capabilities of the system and to understand how the system can help her decide the value of an estate. When necessary, she will build up specific models for real estate appraisal in the system. To do so, the agent describes the nature of the problem that faces her to the system and wants the system to recommend her possibly available alternatives. Based on the nature of this type of problems i.e., feature-de-Ž tecting problems , the system suggests a few learning. methods and<sup>r</sup>or models for solving features-detecting problems to produce appraisal knowledge from the historical cases. Therefore, the agent requests historical cases of real estate transaction data from the data base of the local real estate board. These cases have various attributes and transaction prices in each case. Because the system’s data base has the same data model and file structure as does the board’s data base, the agent imports painlessly the data directly into the system. The agent wants to evaluate the performance of the system. She retrieves each case to roughly estimate the relationship between the transaction price and the attributes. She also tries to identify those attributes which contribute most to the value of estates. After getting a general picture of the historical cases, she inputs a similar case, which also comes from the local real estate board’s data base, and asks the system to evaluate the value.

During the process, the dialog generation and management system DGMS captures the usage pat-Ž . tern of the agent and notices that the agent uses a great deal of images of the estate. Thus, the DGMS updates the agent’s preferences for presentation in its user model in the user profile. Meanwhile, the DGMS conveys the problem to the problem processing system. Because this problem is new, the problem processor finds no appropriate knowledge available in the knowledge base to evaluate the value of the estate. Consequently, the problem processing system conveys the characteristics to the introspection module. Upon receiving the message from the problem processing system, the introspection module consults the self-knowledge and examines the nature of the problem. It finds that this is a feature-detecting problem and determines that the inductive learning method is capable of detecting critical features of estates in estimating the value of an estate. Hence, the introspection denotes the inductive learning method. The inductive learning method accesses the data base for the historical cases and model building block base for linear models. Consulting the MCDM models in the problem domain knowledge base, the inductive learning method derives one or more appraisal models. The generated knowledge is then assimilated into the problem domain knowledge base. Since the knowledge is new, the problem processing system invokes the introspection module to update the self-knowledge. Meanwhile, as the knowledge is now available, the problem processing system proceeds to evaluate the new case. The results are sent to the DGMS and are ready to be presented to the agent. To decide on an appropriate presentation mode, the DGMS looks into the user profile and the presentation mode knowledge base to decide upon the most appropriate mode in which to present the results. The DGMS decides to trigger the introspection module since the results are new and the user model shows that the user’s expertise about the problem domain and preferences for interface have changed i.e., the agent prefers images to text de-Ž scription about houses . Hence, the introspection. conveys necessary knowledge to an interface composition mechanism. The composition mechanism looks up the user model and the interface elements to generate new presentation knowledge i.e., associat- Ž ing the user behavior with graphical presentation .. The new presentation knowledge is then assimilated into the presentation model knowledge base. With the knowledge, the DGMS proceeds to present the results.

## 4.2. Comparison with other models

In this subsection, we compare the ADSS model with others on a set of criteria. We choose the following architectures 25,27,37,44 because they<sup>w</sup> <sup>x</sup> are explicitly labeled ADSS or are representative ADSS in some facets. Table 1 shows the comparison.

Adaptivity in interaction refers to the system’s capability to adapt during a decision-making session. This results from domain knowledge refinement. Adaptivity in improving decision quality means that the decision quality of similar decisions can be improved because knowledge about a class of decisions is accumulated. Accumulation of knowledge about a class of decisions directly results in the adaptivity in domain knowledge base. However, it should be noted that vice versa is not necessarily true. Adaptivity in user interface refers to the system’s capability of adapting to the changes in the user. Synergy between user interface and domain knowledge means the impact of interaction between user interface and domain knowledge on the decision quality.

Table 1  
Feature comparison of ADSS models

<table><tr><td>Features</td><td>Our model</td><td>Ref. [44]</td><td>Ref. [25]</td><td>Ref. [37]</td><td>Ref. [27]</td></tr><tr><td>Adaptivity in interaction</td><td>X</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Adaptivity in improving decision quality</td><td>X</td><td>X</td><td> $X^a$ </td><td></td><td></td></tr><tr><td>Adaptivity in domain knowledge base</td><td>X</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Adaptivity in interface</td><td>X</td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>Synergy b/w interface and domain knowledge</td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Multiple-learning methods</td><td>X</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Adaptivity in self-knowledge</td><td>X</td><td></td><td></td><td></td><td></td></tr></table>

<sup>a</sup> This model may indirectly improve the quality of similar decisions or problems as, according to the authors, ‘‘adaptation occurs during the course of a particular problem processing episode . . . it is possible to generalize the knowledge acquired through such adaptation . . . ’’ Ref.<sup>w</sup> <sup>w x</sup> <sup>x</sup> 44 , p. 94 .

Feature comparison between our model and other models shows that our model is an integrated model in that it is multiple-component adaptive, while other models are either interface-adaptive or problemprocessing capability adaptive.

The model in this article is more comprehensive than other models in that it provides an adaptive interface as well as an adaptive knowledge base. Fig. 3 shows an ADSS architecture proposed by Piramuthu et al. 44 . Based on a generic DSS frame-<sup>w</sup> <sup>x</sup> work 8 , this architecture is proposed for designing <sup>w</sup> <sup>x</sup> an ADSS for flexible manufacturing systems FMS Ž . and has the following components: a language system LS , a problem processing system PPS , aŽ . Ž . knowledge system KS , and a learning and refiningŽ . system LRS . Comparison between the architectureŽ . in Fig. 3 and that proposed in Fig. 1 leads to the conclusion that the former is a part of the latter. Piramuthu et al.’s model 44 corresponds to the<sup>w</sup> <sup>x</sup> combination of the problem-processing-unit in Fig. 1 and an interface. Moreover, the knowledge about the relationship between the user knowledge and the problem domain knowledge in the self-knowledge base empowers the introspection component to facilitate better communication between the user and the system.

Another ADSS architecture proposed in 25 is <sup>w</sup> <sup>x</sup> similar to that of 44 . The major difference is that <sup>w</sup> <sup>x</sup> the one proposed in 25 uses a schedule generation<sup>w</sup> <sup>x</sup> system rather than simulation to produce the input material for inductive learning, which is called the sequence discovery system in 25 . The input materials produced by the schedule generation system are evaluated by a schedule evaluation system before they are sent to the sequence discovery system unit. One significant feature of this architecture is that the cyclic process from the schedule generation system, the schedule evaluation system, to the sequence discovery system assures that a better solution can be discovered 25 . This process can be achieved by <sup>w</sup> <sup>x</sup> carrying out the process in the problem-processingunit in our model.

Two other models for adaptive interface proposed in 27,37 are characterized by the dependency of <sup>w</sup> <sup>x</sup> presentation mode interface on the user model. Ž . This characteristic has been incorporated in the interface-unit in our model. However, the models in Refs. <sup>w</sup> <sup>x</sup> 27,37 do not explicitly take into account the fact that changes in domain problem knowledge may affect the effectiveness of the presentation mode. The functions of each of the two models corresponds to those of interface-unit in our model.

In brief, the proposed conceptual model is 1Ž . comprehensive in the sense that it embraces the features of other architectures and, 2 adaptive inŽ . that the introspection is capable of consulting the self-knowledge and adopting various learning strategies and<sup>r</sup>or mechanisms to accommodate the knowledge base and interface.

![](/api/attachments/BQZ8PEBS/fulltext/images/d85926a95be05956af11f68f72735bcc008418f69598dd72afe4cb7e5306fb90.jpg)  
Fig. 3. An ADSS architecture in Ref. 44 p. 132 . <sup>w</sup> <sup>x</sup> Ž .

## 5. Conclusion and future research

We have proposed a conceptual model of ADSS in this article. We use a framework for the organization of decision-making and the concept of a reflexive system in developing the conceptual model. The conceptual model consists of a meta-level unit and a basic-level unit. The meta-level is capable of introspecting the system’s capabilities and limitations, and determining an appropriate learning method. The components in the basic-level unit communicate with the user and carry out the task of decision support.

This model opens several research areas: 1 theŽ . mechanisms of reification and denotation; 2 theŽ . relationship among the problem domain knowledge, the presentation knowledge, and the user knowledge; and 3 the introspection mechanism, including theŽ . maintenance of self-knowledge. In addition, the conceptual model is characterized by a variety of knowledge, intense message passing, and a highly modular structure. These features introduce certain issues regarding design and implementation of the conceptual model. In general, different knowledge representation formalisms are required for various kinds of knowledge. When different types of knowledge are maintained in a complex system like the proposed one, a critical issue is how to coordinate different knowledge representation schemes. According to Vranes and Stanojevic 56 , the blackboard frame-<sup>w</sup> <sup>x</sup> work is a promising choice for the coordination mechanism of multiple knowledge representations and reasoning techniques in multiparadigm systems. Finally, design issues concerning message passing and modular structure are another research area. We have developed an agent-based architecture 12 in<sup>w</sup> <sup>x</sup> order to cope with these issues. The authors are currently pursuing several of these areas.

## References

<sup>w</sup> <sup>x</sup> 1 W. Accola, S.P. Agrawal, C.W. Hosapple, Adaptive decision support systems for evaluating risk and uncertainty in capital investment decisions: opportunities for future research, Managerial Finance 21 3 1995 1–16.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 A.A. Angehrn, T. Jelassi, DSS research and practice in perspective, Decision Support Systems 12 1994 267–275.Ž .

<sup>w</sup> <sup>x</sup> 3 M. Atkinson, D. DeWitt, D. Maier, F. Bancilhon, K. Dittrich, S. Zdonik, The object-oriented database system manifesto, in: W. Kim, J.-M. Nicolas, S. Nishio Eds. , Deductive and Ž . Object-Oriented Databases, Elsevier, North-Holland, 1990, pp. 223–240.

<sup>w</sup> <sup>x</sup> 4 D. Baldwin, S.B. Yadav, The process of research investigations in artificial intelligence—a unified view, IEEE Transactions on Systems, Man and Cybernetics 25 5 1995 852–Ž . Ž . 861.

<sup>w</sup> <sup>x</sup> 5 J. Bauer, T. Schwab, Propositions on help-systems, Research Report FB-INF-86-36, WISDOM-Verbundprojekt, 1986.

<sup>w</sup> <sup>x</sup> 6 D. Benyon, D. Murray, Adaptive systems: from intelligent tutoring to autonomous agents, Knowledge-Based Systems 6 Ž . Ž .4 1993 197–219.

<sup>w</sup> <sup>x</sup> 7 D. Benyon, D. Murray, Developing adaptive systems to fit individual aptitudes, Proceedings of the 1993 International Workshop on Intelligent User Interfaces, ACM Press, 1993.

<sup>w</sup> <sup>x</sup> 8 R.H. Bonczek, C.W. Holsapple, A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, NY, 1981.

<sup>w</sup> <sup>x</sup>9 D. Browne, M. Norman, D. Riches, Why build adaptive Systems?, in: D. Browne, P. Totterdell, M. Norman Eds. , Ž . Adaptive User Interface, Academic Press, San Diego, CA, 1990, pp. 15–57.

<sup>w</sup> <sup>x</sup> 10 D. Browne, M. Norman, D. Adhami, Methods for building adaptive systems, in: D. Browne, P. Totterdell, M. Norman Ž . Eds. , Adaptive User Interface, Academic Press, San Diego, CA, 1990.

<sup>w</sup> <sup>x</sup> 11 D.N. Chin, KNOME: Modelling what the user knows in UC, in: A. Kobsa, W. Wahlster Eds. , User Models in Dialog Ž . Systems, 1989.

<sup>w</sup> <sup>x</sup> 12 T.-T. Chuang, S.B. Yadav, An agent-based architecture of an adaptive decision support system ADSS , Proceedings of the Ž . Third Americas Conference on Information Systems, Indianapolis, IN, August 15–17, 1997.

<sup>w</sup> <sup>x</sup> 13 K. Cox, D. Walker, User Interface Design, Simon and Schuster Asia , Singapore, 1993.Ž .

<sup>w</sup> <sup>x</sup> 14 N.P. Dalal, S.B. Yadav, The design of a knowledge-based decision support system to support the information analyst in determining requirements, Decision Sciences 3 1992 1373–Ž . 1388.

<sup>w</sup> <sup>x</sup> 15 P.-S. Deng, A. Chaudhury, A conceptual model of adaptive knowledge-based systems, Information Systems Research 3 Ž . Ž . 2 1992 127–149.

<sup>w</sup> <sup>x</sup> 16 P.-S. Deng, Automating knowledge acquisition and refinement for decision support: a connectionist inductive inference model, Decision Sciences 24 2 1993 371–393.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 P.-S. Deng, An adaptive case-based reasoning model for decision support in dynamic environments, Proceedings of IEEE International Conference on Systems, Man and Cybernetics 2 1994 1874–1879.Ž .

<sup>w</sup> <sup>x</sup> 18 B.L. Dos Santos, C.W. Holsapple, A framework for designing adaptive DSS interfaces, Decision Support Systems 5 Ž .1989 1–11.

<sup>w</sup> <sup>x</sup> 19 M.K. El-Najdawi, A.C. Stylianou, Expert Support Systems: Integrating AI Technologies, Communication of the ACM, Vol. 36, No. 12, pp. 55–65, 103.

<sup>w</sup> <sup>x</sup> 20 P.N. Finlay, C.J. Maritn, The state of decision support systems: a review, OMEGA 17 6 1989 525–531.Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 G. Frederic, A. Jacqueling, Logical reorganization of DAI systems, in: M.J. Wooldridge, N.R. Jennings Eds. , Intelli- Ž . gent Agents: ECAI-94 Workshop on Agent Theories, Architectures, and Languages, Springer-Verlag, Berlin, 1994.

<sup>w</sup> <sup>x</sup> 22 S.R. Hedberg, The Data Gold Rush, Byte, October, 1995, pp. 83–88.

<sup>w</sup> <sup>x</sup> 23 J.C. Henderson, Finding synergy between decision support systems and expert systems research, Decision Sciences 18, 333–349.

<sup>w</sup> <sup>x</sup> 24 C.W. Holsapple, A.B. Whinston, Management support through artificial intelligence, Human Systems Management 5 1985 163–171.Ž .

<sup>w</sup> <sup>x</sup> 25 C.W. Holsapple, R. Pakath, V.S. Jacob, J.S. Zaveri, Learning by problem processors: adaptive decision support systems, Decision Support Systems 10 1993 85–108.Ž .

<sup>w</sup> <sup>x</sup> 26 C.W. Holsapple, A.B. Whinston, Decision Support Systems: A Knowledge-Based Approach, West Publishing, St. Paul, MN, 1996.

<sup>w</sup> <sup>x</sup>27 P.R. Innocent, Towards self-adaptive interface systems, International Journal of Man–Machine Studies 16 1982 287–Ž . 299.

<sup>w</sup> <sup>x</sup> 28 V.S. Jaco, R. Pakath, J.S. Zaveri, Adaptive decision support systems: incorporating learning into decision support systems, Proceedings of 1990 ISDSS conference, Sep. 1990, pp. 313–330.

<sup>w</sup> <sup>x</sup> 29 M.T. Jelassi, K. Williams, C.S. Fidler, The emerging role of DSS: from passive to active, Decision Support Systems 3 Ž .1987 299–307.

<sup>w</sup> <sup>x</sup> 30 P.G.W. Keen, Adaptive design for decision support systems, Data Base 12 1Ž . Ž . <sup>r</sup>2 1980 15–25.

<sup>w</sup> <sup>x</sup> 31 P.G.W. Keen, Decision support systems: the next decade, Decision Support Systems 3 1987 253–265.Ž .

<sup>w</sup> <sup>x</sup> 32 W.J.M. Kickert, Organization of Decision-Making: A Systems-Theoretical Approach, North-Holland Publishing, Amsterdam, The Netherlands, 1980.

<sup>w</sup> <sup>x</sup> 33 A. Kobsa, W. Wahlster Eds. , User Models in Dialog Sys-Ž . tems, Springer-Verlag, Berline, 1989.

<sup>w</sup> <sup>x</sup> 34 M. Krogsaeter, G.C. Thomas, Adaptivity: system-initiated individualization, in: R. Oppermann Ed. , Adaptive UserŽ . Support: Ergonomic Design of Manually and Automatically Adaptable Software, Lawrence Erlbaum Associates, Publishers, Hillsdale, NJ, 1994.

<sup>w</sup> <sup>x</sup>35 M. Krogsaeter, R. Oppermann, G.C. Thomas, A user interface integrating adaptability and adaptivity, in: R. Oppermann Ed. , Adaptive User Support: Ergonomic Design ofŽ . Manually and Automatically Adaptable Software, Lawrence Erlbaum Associates, Publishers, Hillsdale, NJ, 1994.

<sup>w</sup> <sup>x</sup>36 T.-P. Liang, C.V. Jones, Design of a self-evolving decision support system, Journal of MIS 4 1 1987 59–82.Ž . Ž .

<sup>w</sup> <sup>x</sup> 37 T.-P. Liang, User interface design for decision support systems: a self-adaptive approach, Information and Management 12 1987 181–193.Ž .

<sup>w</sup> <sup>x</sup> 38 T.-P. Liang, Research in integrating learning capabilities into information systems, Journal of Management Information Systems, Vol. 9, No. 4, pp. 5–15.

<sup>w</sup> <sup>x</sup> 39 J. McGovern, D. Samson, A. Wirth, Knowledge acquisition for intelligent decision systems, Decision Support Systems 7 Ž . 1991 263–272.

<sup>w</sup> <sup>x</sup> 40 F. Mili, Dynamic view of decision domains for the design of active DSS, Proceedings of 22nd Annual Hawaii International Conference on Systems Sciences, 1989, pp. 24–31.

<sup>w</sup> <sup>x</sup> 41 A. Newell, The knowledge level, Artificial Intelligence 18 Ž . 1982 82–127.

<sup>w</sup> <sup>x</sup> 42 A.Y. Norcio, J. Staley, Adaptive human–computer interfaces: a literature survey and perspective, IEEE Transactions on Systems, Man and Cybernetics 19 2 1989 399–408.Ž . Ž .

<sup>w</sup> <sup>x</sup> 43 R. Oppermann, Introduction, in: R. Oppermann Ed. , Adap- Ž . tive User Support: Ergonomic Design of Manually and Automatically Adaptable Software, Lawrence Erlbaum Associates, Publishers, Hillsdale, NJ, 1994.

<sup>w</sup> <sup>x</sup> 44 S. Piramuthu, N. Raman, M.J. Shaw, S.C. Park, Integration of simulation modeling and inductive learning in an adaptive decision support system, Decision Support Systems 9 1993Ž . 127–142.

<sup>w</sup> <sup>x</sup> 45 F.J. Radermacher, Decision support systems: scope and potential, Decision Support Systems 12 1994 257–265. Ž .

<sup>w</sup> <sup>x</sup> 46 S. Raghavan, D. Chand, Exploring active decision support: the JANUS project, Proceedings of the 22nd Annual Hawaii International Conference on Systems Sciences, Vol. 3, 1989, pp. 33–45.

<sup>w</sup> <sup>x</sup> 47 H. Reichgelt, Knowledge Representation: An AI Perspective, Ablex Publishing, Norwood, NJ, 1991.

<sup>w</sup> <sup>x</sup> 48 M. Rohatgi, A Human Learning Approach For Designing Adaptive Knowledge-Based Systems, Unpublished doctoral dissertation, Texas Tech. University, 1994.

<sup>w</sup> <sup>x</sup> 49 A. Sen, G. Biswas, Decision support systems: an expert systems approach, Decision Support Systems 1 1985 197–Ž . 204.

<sup>w</sup> <sup>x</sup> 50 H. Simon, The New Science of Management Decision, Harper and Row, New York, NY, 1977.

<sup>w</sup> <sup>x</sup> 51 D. Sleeman, UMFE: a user modeling front–end subsystem, International Journal of Man–Machine Studies 23 1985Ž . 71–88.

<sup>w</sup> <sup>x</sup> 52 P. Totterdell, P. Rautenbach, Adaptation as a problem of design, in: D. Browne, P. Totterdell, M. Norman Eds. ,Ž . Adaptive User Interfaces, Academic Press, San Diego, CA, 1990, pp. 59–84.

<sup>w</sup> <sup>x</sup> 53 P. Totterdell, P. Rautenbach, S.O. Anderson, Adaptive interface techniques, in: D. Browne, P. Totterdell, M. Norman Ž .Eds. , Adaptive User Interfaces, Academic Press, San Diego, CA, 1990.

<sup>w</sup> <sup>x</sup> 54 E. Turban, P.R. Watkins, Integrating expert systems and decision support systems, MIS Quarterly 10 1986 121–135.Ž .

<sup>w</sup> <sup>x</sup> 55 S.W. Tyler, J.L. Schlossberg, R.A. Gargan, Jr., L.K. Cook, J.W. Sullivan, An intelligent interface architecture for adaptive interaction, in: J.W. Sullivan, S.W. Tyler Eds. , Intelli-Ž . gent User Interfaces, Addison-Wesley Publishing, Reading, MA, 1991.

<sup>w</sup> <sup>x</sup> 56 S. Vranes, M. Stanojevic, Integrating multiple paradigms within the blackboard framework, IEEE Transactions on Software Engineering 21 3 1995 244–262.Ž . Ž .

<sup>w</sup> <sup>x</sup> 57 H.J. Watson, R.H. Spragure, Jr., The components of an

architecture for DSS, in: R.H. Sprague, Jr., H.J. Watson Ž . Eds. , Decision Support Systems: Putting Theory into Practice, 3rd edn., Prentice-Hall, Englewood Cliffs, NJ, 1993.

58 M. Zeleny, Multiple Criteria Decision Making, McGraw-Hil Book, New York, NY, 1982.

Ta-Tao Chung is an Assistant Professor of Management Information Systems at Wichita State University, Wichita, KS. His research interests include: Decision Support Systems, Information Systems Development, Computer-Supported Cooperative Work, and Management of Organizational Interdependence.

Dr. Surya B. Yadav is currently the James and Elizabeth Sowell Professor of Telecom Technology and Area Coordinator in the College of Business Administration, Texas Tech. University, Lubbock, TX. He has over 15 years of teaching, research, and consulting experience in the area of Management Information Systems. He received his B.S.E.E. degree in Electrical Engineering from Banaras University, M. Tech. degree in Business Information Systems from Georgia State University. His research interests include information requirement determination and adaptive Internet-based systems. He has published in several journals including Communications of the ACM, IEEE Trans. on Software Engineering, IEEE Trans. on Systems, Man, and Cybernetics, Decision Support Systems, Decision Sciences, and Information Systems.
