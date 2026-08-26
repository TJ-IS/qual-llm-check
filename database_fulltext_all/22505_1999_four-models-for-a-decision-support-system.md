---
otero_id: 22505
otero_key: "YCUFK7CZ"
title: "Four models for a decision support system"
authors: "Dinesh Mirchandani; Ramakrishnan Pakath"
year: "1999"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00074-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Four models for a decision support system

Dinesh Mirchandani $^{a}$ , Ramakrishnan Pakath $^{b,*}$

$^{a}$ Management Department, Seidman School of Business, Grand Valley State University, Allendale, MI 49401-9403, USA $^{b}$ Decision Science and Information Systems, School of Management, C.M. Gatton College of Business and Economics, University of Kentucky, Lexington, KY 40506-0034, USA

Received 28 June 1995; accepted 23 July 1998

## Abstract

We examine four decision support system (DSS) models – the Symbiotic, Expert, Holistic, and Adaptive – and distinguish them in terms of the impact of their knowledge management styles on their problem-processing behavior. We draw upon existing notions of knowledge types and their management to develop a knowledge-oriented view. We use it to categorize the models as being either Static or Dynamic. From this perspective, the Holistic DSS may be regarded as being the most advanced, as it postulates holistic problem recognition and processing capabilities. While progress has been made on digitally simulating holistic recognition, much remains to be done in developing practical processors and truly holistic systems that couple such processors and recognizers. © 1999 Elsevier Science B.V. All rights reserved

Keywords: Symbiotic DSSs; Expert Systems; Holistic DSSs; Adaptive DSSs; Knowledge-oriented view; Static systems; Dynamic systems; Non-adaptive systems; Relative assessment

## 1. Introduction

Decision support system (DSS) models serve as guides by stating the key features, strengths, limitations, and application potential of various DSSs. Together with model classification schemes (e.g., [2, 20, 43]), they facilitate DSS builders by reducing wasted effort, cost, and time.

Relatively recent technological advances have facilitated the definition of many sophisticated DSS models. Here, we consider a set of models for modern DSSs (the Symbiotic, Expert, Holistic, and Adaptive) that emerged at different times over the last three to four decades. Much of the original documentation is technical and non-comparative, in that each views a particular model in isolation and uses terminology native to it. This paper seeks to highlight their conceptual distinctions using a non-technical, knowledge-management metaphor and an associated, Static-Dynamic, classification scheme. Together, the metaphor and scheme provide a framework for demonstrating the inherent differences in their knowledge management abilities that result in different problem-processing behaviors.

## 2. Knowledge types, knowledge management, and a DSS classification scheme

Holsapple and Whinston [19] define six types of knowledge a DSS could possess – descriptive, procedural, reasoning, linguistic, presentation, and assimilative. The first three are termed ‘primary’ types and the remainder are ‘secondary’ (i.e., derived from the primary).

Descriptive knowledge (also known as data or information) is information about past, present, future, and hypothetical states of relevance to a decision-making situation: it is concerned with ‘knowing what’. Procedural knowledge (procedures, steps, or strategies) is ‘knowing how’ and specifies step-by-step procedures for accomplishing tasks. Reasoning knowledge specifies what conclusions are valid under which circumstances: ‘knowing why’.

Presentation knowledge, which facilitates communication from one entity to another, consists of reasoning concerning alternative presentation modes, knowing how to implement a chosen mode during a given dialogue, and detailing the specifics of each mode. Linguistic knowledge helps in interpreting communication received. Assimilative knowledge helps ‘maintain’ a knowledge base.

Problem ‘processing’ is the activity following problem recognition and preceding solution presentation. (A complex problem is solved through a series of recognition–processing–presentation cycles.) Linguistic and presentation knowledge benefit recognition and presentation, respectively. Descriptive, procedural, and reasoning knowledge primarily guide processing. Assimilative knowledge supports all three activities. A DSS may be equipped to manage (i.e., acquire, store, process, and eliminate) any and all of these six knowledge types.

During processing, appropriate reasoning and procedural knowledge fragments act upon portions of existing descriptive knowledge to generate new knowledge. In more advanced DSSs, reasoning and procedural knowledge could also act upon themselves. The generated knowledge may be primary or secondary.

Here, we focus on detecting the possibilities for consequential changes in a DSS's processing behavior over time, as triggered by modifications (i.e., additions, deletions, and updates) to its procedural and reasoning knowledge contents. Such ‘novel’ modifications interest us because virtually any DSS is capable of changing behavior based on revisions to its descriptive knowledge base. During the course of executing a conventional 3GL-coded program, a computer’s current behavior is dictated by the outcomes of prior processing steps which cause changes to its descriptive knowledge content. However, in a fully debugged system, these do not result in novel, or even unanticipated, behavior patterns. Hence, one can fully debug such programs.

Novel alterations may occur either autonomously or through external agent (e.g., a developer) intervention. We classify systems that are capable of autonomous modifications as Dynamic systems. Generally, improved processing behavior, either not attainable or desirable through human intervention, is why one develops self-adjusting, Dynamic systems.

The converse is a Static system. Such invariant processors do not autonomously learn anything new from past experiences about how to enhance future support. Many real-world systems are Static systems. Dynamic systems constitute a comparatively smaller set as they are usually more sophisticated (i.e., advanced or complex) and are generally more difficult to create and operate.

## 3. Four DSS models - A relative assessment

The integration of artificial intelligence-based knowledge management schemes in a DSS is a relatively recent trend. Such efforts have yielded at least four well-known DSS models – the Symbiotic, Expert, Holistic, and Adaptive. Here, we seek to use insights from Section 2 to contrast the four models, classify each model as being either Static or Dynamic, and provide a representative example of each. Table 1 summarizes these discussions. Fig. 1 contrasts the models in terms of their self-adjusting capabilities.

## 3.1. The Symbiotic DSS

The Symbiotic DSS (SDSS), a specialization of the more general Active DSS (ADSS) model, emerged during the late 80s. Jelassi et al. [22] view an ADSS as one that can “identify gaps in existing operations and suggest ways to strengthen the standing of the firm”. Manheim [28] offers a more focused definition that we adopt: a system that “operates in part almost completely independent of explicit direction from the user.” Here, the author is referring to the self-activation of specific support functions (e.g., independent time-series analysis of a data set) by an ADSS and not to routine operational functions (e.g., automated, periodic file backup).

Table 1
Knowledge-oriented relative assessment of four DSS models

<table><tr><td></td><td>Symbiotic</td><td>LRES</td><td>Adaptive</td><td>Holistic</td></tr><tr><td>Definition:</td><td>A system that can alter its support behavior to suit a user by monitoring the user&#x27;s cognitive and decision making styles</td><td>A system that can reason using stored knowledge that is fragmented in rule form</td><td>A system capable of inducing positive changes in itself to enhance its problem processing proficiency</td><td>A system capable of holistic problem (recognition and) processing</td></tr><tr><td>System type:</td><td>Static</td><td>Static</td><td>Dynamic</td><td>Highly Dynamic</td></tr><tr><td>Problem processing behavior:</td><td>Agent-dependent application of procedural knowledge to existing descriptive knowledge to generate new descriptive knowledge. Behavior is predictable</td><td>Primarily agent-independent, deductive inferencing by applying predefined reasoning knowledge to any primary knowledge type to generate new primary knowledge – in particular, descriptive. Behavior is predictable</td><td>Primarily agent-independent, inductive inferencing by applying reasoning knowledge to generate new primary knowledge – in particular, reasoning and/or procedural. Behavior not fully predictable</td><td>Agent-independent aggregation of knowledge into progressively larger knowledge modules to facilitate holistic reasoning. Behavior not fully predictable</td></tr><tr><td>Reasoning and/or procedural knowledge source:</td><td>Fully and explicitly predefined</td><td>Fully predefined. May be explicit or implicit</td><td>Predefined and discovered. May be explicit or implicit</td><td>Predefined and discovered. May be explicit or implicit</td></tr><tr><td>Knowledge base pruning:</td><td>Agent-induced</td><td>Agent-induced</td><td>Agent and/or self-induced</td><td>Agent and/or self-induced</td></tr><tr><td>Knowledge integrity:</td><td>Knowledge must be complete and non-conflicting</td><td>Knowledge must be complete and non-conflicting</td><td>Knowledge may be incomplete and conflicting</td><td>Knowledge may be incomplete and conflicting</td></tr><tr><td>Example systems:</td><td>[8, 22, 28, 29, 41]</td><td>[30, 42]</td><td>LIES: [24, 40]. GA-based: [5, 17]. Others: [44]</td><td>Holistic problem recognizers: Holographic: [10, 12, 21, 34, 38, 39]. ANN-based: [13]. Holistic problem processors: [1, 25, 26]</td></tr></table>

![](/api/attachments/YCUFK7CZ/fulltext/images/86492a751dfa58f7ef799c7fee0bf055611f5cd4537a638c58b19d17ada41357.jpg)  
Fig. 1. A Static/Dynamic DSS classification scheme.

The converse of an ADSS is a Passive DSS. An example is Portfolio Management System (PMS), developed in the early 1970s to assist with allocating investment resources to portfolios [23]. It allows a user to activate pre-defined operations like examining existing portfolio and security statistics, analyzing how well a potential security's profile fits in with a current portfolio's contents, etc.

ADSSs may differ in the timing of their active processing: it may occur in parallel with a user's efforts (each does its own, independent processing), in tandem (the ADSS follows the user's lead), and/or may be interleaved (each directs efforts alternately). A system could also differ in the type(s) of active support offered – it may behave as an associate, adviser, a critic, and/or stimulator.

A Symbiotic DSS (SDSS) is an ADSS that can alter its support behavior at run time to suit a user's cognitive and decision-making styles. 'Symbiotic' implies mutual dependence [11]. A symbiotic decision maker consists of a user and an SDSS. Experience in complex steel mill scheduling tasks [29] demonstrates that superior schedules could be developed with the help of an SDSS. Other Active/Symbiotic implementations are discussed in [8, 41].

The SDSS, while more advanced than a conventional DSS, is still a Static system: its behavioral changes are not (1) initiated independently and/or (2) based on any novel knowledge modifications. An SDSS only reacts based on projected user behavior given past actions. Procedures for historical assessments and projecting behavior are predefined. Behavior changes are effected by automatically triggering one or more of several built-in procedures.

## 3.1.1. A Symbiotic DSS in practice

Dolk and Kridel [8] describe an SDSS called Progressive EconometRic Modeling system (PERM), for econometric analysis. It consists of three main components: process managers; history processor; and a user interface. Process managers are of two kinds: user-directed (UDPM) and computer-directed (CDPM). The UDPM activates processes in response to commands issued directly by the user. The CDPM activates processes when prompted by the history processor as it attempts to provide active support.

The history processor consists of two parts: a history recorder which journals user inputs, and resultant outputs, in a history record, and a history inference processor (HIP) which attempts to model a user's understanding of the problem based on the history record. The interface allows activation of the UDPM and filtering of the outputs. The CDPM uses a special language called PERM control language (PCL) for communication. The HIP was developed by:

(a) using econometric analysis experts to build a library of PCL problem situation schemas;

(b) using modelers to identify and build a library of command sequence patterns likely in each of these situations; and

(c) creating a ‘demon’ procedure, which periodically examines the history record and tries to match the current command sequence with a pre-identified pattern.

A session with PERM proceeds as follows. The user initiates action via a command medium (a language, menu selection, mouse click, etc.). The UDPM activates one or more processes (e.g., a regression routine) to satisfy the command. The history recorder logs the command and resultant output in the history record. The inference processor scans the history record and attempts to infer the user's model of the problem through deduction, that is, pattern-matching with the command sequence library. If a match is made, control passes to the CDPM which invokes the processes associated with that model. If no model is identified, control is returned to the user along with the UDP output. Otherwise, the CDPM returns the UDP and CDP outputs to the user after executing its processes. This recognize-process–present cycle continues until the user terminates the session.

Though the PERM system demonstrates the promise of ADSS concepts, Dolk and Kridel acknowledge that a fully active system would possess the ability to create new schemas autonomously (from past experiences) and transform them into processes rather than having capabilities hard-wired.

## 3.2. The Expert System

The Expert System (ES) is the oldest of the four models: the earliest implementation was DENDRAL in the mid-60s. Since then, ESs have proliferated within a diversity of fields ([3, 6, 27, 40]). We view the ES as one kind of DSS because, just as with a human expert, one is free to use or disregard the expert's advice. (Some researchers regard the ES as a decision 'making' system (e.g., [45]).) Human expertise may be stored in a variety of ways. The traditional approach with ESs is to use independent knowledge fragments called productions or rules [18] of the form: [IF <the following condition(s) is/are true> THEN <execute the following action(s)>]. Rule-based ESs may be divided into two categories depending on the types of rules employed – Learn-by-Rote ESs (LRESs; discussed below) and Learn-through-Induction ESs (LIESs; see Section 3.4).

All of an LRES's expertise is culled from human experts. It applies predefined reasoning strategies to select and activate rules in turn. Through instructions encoded in a currently activated rule, the LRES operates on stored data, procedures, and other rules to generate new knowledge using deductive inferencing. Reasoning strategies are essentially ‘rule-chaining’ strategies: a system may be equipped with forward (rules are executed from left to right by instantiating the IF portions first), backward (rules are executed from right to left; akin to goal seeking), and/or bi-directional chaining capabilities.

An archetypal LRES is XCON (formerly R1) for configuring DEC VAX computer systems to meet customer requirements $[30]$ . The system currently makes use of ca. 12 000 rules and forward chaining to handle orders involving several hundred components.

An LRES differs from a conventional DSS and an SDSS as follows. First, unlike the DSS and SDSS that are computation-intensive, an LRES is deduction-intensive. Second, in a DSS, processing is initiated, and thereafter entirely controlled, by a user and essentially involves the application of procedures to data to generate new data. An SDSS is less reliant on a user: it also possesses some degree of in-built reasoning capabilities about when a particular procedure may be self-activated. An LRES, however, is capable of independently reasoning using any of the three primary knowledge types. An LRES consults a user only to obtain unknown input values and not for directions (explicit or implicit) on how to proceed next. Thus, while an LRES is a highly Active system (much more so than an SDSS), it has virtually no Symbiotic capabilities.

An LRES also belongs to the Static class because it cannot generate novel knowledge-base changes on its own. Given two rules [IF $\langle a\rangle$ THEN $\langle b\rangle$ ] and [IF $\langle b\rangle$ THEN $\langle c\rangle$ ], an LRES derives [IF $\langle a\rangle$ THEN $\langle c\rangle$ ] through transitivity. However, this wisdom is implicit in the two explicitly stated rules. This inability to autonomously generate consequential new insights is also true of any procedures that it might infer. Consequently, like DSSs and SDSSs, an LRES's behavior is fully predictable.

This ‘limitation’ is a consequence of the particular style of inferencing an LRES employs, namely, deductive or truth-preserving inferencing $[31]$ . This is also why, like a conventional 3GL program, one can fully verify and validate an LRES before its release. Section 3.3 discusses other potential drawbacks of LRESs.

## 3.2.1. An LRES in practice

Shpilberg and Graham [42] describe an LRES, called ExperTAX, developed by Coopers and Lybrand, the well-known US tax and audit firm. ExperTAX functions as an ‘intelligent’ questionnaire that guides a client through the information-gathering process necessary to conduct the tax accrual and planning functions of the client’s firm.

ExperTAX consists of four main components: a knowledge base; a knowledge base maintenance system; an inference engine; and a user interface.

The knowledge base consists of information and expertise (derived from knowledge engineering sessions conducted with over 20 senior tax and audit experts at Coopers and Lybrand) stored as ‘frames’ [47]. In general, each frame contains knowledge (some of which is encoded in ca. 1000 rules) on how and when to use the frame, what should happen next, and what to display or print.

The forward-chaining inference engine makes use of a frame manager, stored facts, and a rule interpreter. The frame manager controls frame activation. The rule interpreter uses facts to fire rules contained in active frames. The inference engine keeps track of the inference chain created by the successive firing of rules and can, thus, ‘explain’ its behavior.

The user interface includes a system of nested menus that allow substantial control of the inference process. At virtually any point, the user can return to a menu that allows for an orderly interruption of the process or for the resumption of the process at a different session or frame. Outputs include printed reports, audit trails of all questions asked and answers received, and specialized forms issued for additional documentation.

The knowledge base maintenance system enables one to modify and/or expand the base. It includes a frame editor, a rule interaction display that allows one to observe all frames impacted by changes to a frame, and a logic evaluator that identifies possible conflicts between rules being currently edited and existing rules.

During a consultation, ExperTAX is capable of sifting through issues and tailors additional information requests to a client's situation. It can explain why a question is being asked and why a response is relevant. It keeps track of any unanswered questions and documents all questions, answers, and user-generated ‘marginal notes’.

## 3.3. The Holistic DSS

The LRES model has its detractors. We now summarize key assumptions of the model and their associated criticisms.

Assumption 1: One can always represent reasoning knowledge as independent rules and intelligent decision making as the logical derivation of truths from known facts using rules. Criticism: Human experts, often think holistically [9], axiomatize their knowledge in inconsistent ways (because available information is often conflicting and incomplete) and reason in the face of such uncertainty $[14]$ . They display intelligence through effectively combining relatively simple processes to resolve complex problems $[33]$ .

Assumption 2: Experts reason in focused (i.e., carefully controlled and guided) ways. Criticism: Much expert reasoning is unfocused [48].

Assumption 3: Requisite domain and other knowledge are completely and accurately known a priori. Criticism: Often, knowledge must be incrementally acquired during problem solving ([33, 36, 48]).

Assumption 4: Problem environments remain relatively static. Criticism: Environments are usually dynamic with many problems tightly coupled to them [36].

The Holistic DSS (HDSS) seeks to address the drawbacks in Assumption 1. While we have coined this term, explicit reference to ‘holistic systems’ that work seemingly like an advanced human mind without relying upon predefined, rule-based inferencing appears in Dreyfus and Dreyfus [9]. They view human expertise as occupying a spectrum ranging from the ‘novice’ to the ‘expert’ and we attempt to characterize HDSSs using their scheme.

A Novice system's behavior is guided entirely by memorized, ‘context-free’ elements (facts) and rules (not necessarily productions) for fact-based action. It is completely analytical in its approach to sifting through facts and making action choices (i.e., in recognition and processing) with zero judgmental abilities (i.e., a Static system).

An Advanced Beginner system can recognize ‘situational’ elements (i.e., clues for behavior modification) in the current context and accordingly modifies pre-programmed behavior. Its context-sensitivity comes with experience (i.e., it is not taught). It, too, is completely analytical (but is a Dynamic system).

A Competent system can analytically assess the relative worth of both context-free and situational elements and generate/select action plans, judge their relative merits, and apply a chosen plan. Thus, it can behave in non-preprogrammed ways, including a capacity to plan a course of action. It exercises (some) judgment based on analyses alone (i.e., a more Dynamic system).

A Proficient system can ‘intuitively’ match a current situation with similar, previously-encountered situations and can analytically search through, select/generate, and trigger an action plan similar to one that had succeeded before. Because similarity recognition is seemingly effortless, it demonstrates holistic abilities in problem recognition. Action plan selection and execution, however, is highly deliberative and analytical. Both involve judgment. Thus, judgment is based on intuition and analyses (i.e., a highly Dynamic system).

Lastly, a truly Expert system is one that is capable of intuition-based (i.e., holistic) recognition and action. Any deliberation is not based on analysis. All judgment is intuition based. It is a very highly Dynamic system. We call such systems ‘holistic systems’ or ‘HDSSs’.

Dreyfus and Dreyfus contend that human experts evolve from the Novice stage to the Expert (i.e., Holistic) stage through experience. Here, we view the HDSS label as representing both systems that evolve holistic processing (and recognition) abilities with time and those that are holistic to begin with. Given its holistic abilities, an HDSS is much more advanced than a conventional DSS, an SDSS, and an LRES, all of which are highly analytically deliberative systems.

## 3.3.1. HDSSs in practice

Building HDSSs is not always necessary. In computation-intensive tasks, for example, there is not much to be gained through holistic processing abilities – the action planning activity constitutes a relatively much smaller, easily programmable fraction of the total task. Even so, truly holistic DSSs for the appropriate situations may be regarded as an elusive endgoal of DSS research.

Dreyfus and Dreyfus cite the example of using optical holography to ‘instantaneously’ pick out all occurrences of a particular alphabet in a document without having to scrutinize the document, a line at a time. This is an instance of holistic similarity recognition by a non-human (i.e., optical) device. Similarity recognizers created using computational devices are called Distributed Associative Memories (DAMs). They may be simulated on present day, electronic digital computers using one of two broad designs: the holographic; and neural net approaches.

The holographic approach is essentially a mathematical modeling of an optical recognizer. Available models include the Matrix Model ([21, 38]), the Search of Associative Memory Model ([12, 39]), the Theory of Distributed Associative Memory Model [34], and the Composite Holographic Associative Model [10].

Two subclasses of unsupervised artificial neural networks (ANNs), (i.e., those that learn without the assistance of a trainer), called feedforward-only nets and feedback nets, have been used to construct DAMs. Feedforward ‘associative memory nets’ include the Linear, Optimal Linear, Sparse Distributed, and Fuzzy nets. The Discrete Bidirectional, Adaptive Bidirectional and Temporal nets are examples from the feedback subclass. Discussions on some of these may be found in $[13]$ .

DAMs, being holistic recognition devices, represent a further step in the search for HDSSs. While recognition is also a ‘problem’ that a system must resolve through related processing activities, to date, we are unaware of any viable implementations where all processing (i.e., including those following recognition) is holistic. There is some consensus that creating truly holistic systems may require more than that which present-day digital machines can offer (see Section 4).

DSSs equipped with holographic or neural net-based recognizers result in Static systems. In general, virtually all real-world neural net implementations adapt (or evolve) during a dedicated training phase, which may or may not be supervised. Real-time, autonomous adaptation has proven computationally very expensive for realistic applications ([35, 46]).

## 3.4. The Adaptive DSS

The Adaptive DSS (AdDSS) represents yet another step in the quest for an HDSS. One popular manifestation of this model $[16]$ has its roots in the early work on artificial adaptation $[15]$ . DeJong $[7]$ defines adaptive systems as those “that are capable of making changes to themselves over time with the goal of improving their performance on tasks confronting them in a particular environment". In our terminology, an AdDSS is one that can self-induce positive changes to its reasoning and/or procedural knowledge contents, resulting in enhanced processing proficiency (i.e., efficiency and/or effectiveness). It relies on inductive inferencing to guide critical portions of its processing efforts, in addition to conventional computational processing and, perhaps, other forms of reasoning.

While deductive inferencing is truth preserving, inductive inferencing is falsity preserving [31]. Using rules as an example, given [IF $\langle a\rangle$ THEN $\langle b\rangle$ ], $\langle b\rangle$ is such that we are able to conclude that if $\langle a\rangle$ is false then $\langle b\rangle$ must also be false. However, we must remain noncommittal about $\langle b\rangle$ when $\langle a\rangle$ is true. (e.g., $\langle a\rangle = \langle$ the room is brightly lit $\rangle$ ; $\langle b\rangle = \langle$ the lights are on $\rangle$ ). If the room is not brightly lit, the lights cannot be on. However, if it is lit, the lights may not be on but the sun may be shining through.) Such a rule is called an unsound rule of inference (i.e., an invalid implication). Viewed differently, induction involves backward or reverse reasoning wherein we attempt to infer a sound (i.e., valid) rule's premise given that its conclusion is known/assumed to be true. The unsound rule in our example may be expressed as a valid implication by merely interchanging $\langle a\rangle$ and $\langle b\rangle$ such that the rule reads: [IF $\langle b\rangle$ THEN $\langle a\rangle$ ]. (Thus, if the room is brightly lit, the system must 'test' the hypothesis whether this is due to the lights being on, and others, before rendering a conclusion.)

Induction enables a system to be innovative, but there always is scope for inference error. Builders may try to reduce error potential by equipping AdDSSs with induction mechanisms that exploit problem domain knowledge (e.g., abduction or constructive induction) and a suitable inductive bias (i.e., a facility for keeping the system focused on discovering the more desirable kinds of hypotheses) [32]. We discuss illustrative instances of rule-based and non-rule-based AdDSSs below. Numerous other illustrations are cited in [44].

## 3.4.1. The Learn-through-Induction ES

A Learn-through-Induction Expert System (LIES) augments rote-learned reasoning knowledge through induction. In a rule-based ES, the process is termed rule induction. While they do not currently enjoy the widespread success of LRESs, they are an important subclass of the rule-based ES model with success potential.

An archetypal implementation is R1-SOAR [40], which is an attempt to expand the R1 system's capabilities by using an induction procedure called chunking. Chunking [24] is a way of aggregating existing knowledge chunks into progressively larger chunks over time. Beginning with an initial, base knowledge set (i.e., the consultation goal and operators for achieving the goal), R1-SOAR, generates rule chunks, at run time, that guide the search process to the goal state.

An LIES possesses most of the virtues of the LRES and it can evolve over time. Although rule-based, it is more of a general problem solver than a specific, focused expert system (i.e., an LRES). It mitigates the burden of having to depend entirely on human experts. The end product could perhaps be better than an LRES designed for the same task: the system may discover better rules than human experts.

However, LIESs typically exhibit less processing efficiency, at least initially, while some of the requisite knowledge is being acquired. Portions of this may be irrelevant or incorrect; for example, R1-SOAR, would chunk even when not beneficial and would over-generalize by creating impractical, ‘broad’ rules. For such reasons, currently, human experts must invariably be involved in periodically pruning/amending an LIES’s knowledge base – present implementations are not as agent-independent as desired.

The susceptibility to acquiring useless and/or incorrect knowledge is shared by virtually all systems that utilize induction including the well-known genetic algorithm-based systems and ANNs. However, some approaches compensate by autonomously pruning away knowledge perceived as less useful over time and, thereby, enhance processing correctness without human intervention.

## 3.4.2. The Genetic Algorithm-driven AdDSS

Holsapple et al. [17] describe an AdDSS for static scheduling of FMSs that employs genetic algorithms (GAs) as a means for non-rule-based, constructive induction. A GA is an artificial adaptation of the survival and procreation processes of natural species for evolving ‘good’ solutions to complex decision problems through constructive or empirical (i.e., without domain knowledge) induction.

In this AdDSS, a GA-driven job-sequencing module acts as an intelligent assistant to a job-scheduling module by repeatedly generating and feeding sequences of progressively higher quality to the latter. For each sequence received, the scheduling module utilizes a rote-learned algorithm for schedule generation, assesses schedule quality, and provides a feedback to the sequence-generation module to help in its improvement.

The AdDSS implicitly encodes and stores job-sequencing knowledge (i.e., sequencing heuristics or heuristic combinations) in the form of explicit job sequences (i.e., a sequence is the manifestation of some heuristic combination). It uses existing knowledge to develop new sequencing heuristics that result in new job sequences. A human scheduler and the system designer are absolved of the responsibilities of identifying appropriate heuristics, trying out alternate heuristic combinations, and deciding how many combinations to examine before choosing one. Given fixed storage capacity, it tries to retain the more useful heuristic knowledge by retaining the more promising job sequences and discarding the others.

Simulation results for a problem of practical size indicate that both schedule quality and search effort using this hybrid approach (i.e., using a GA in combination with a conventional scheduling algorithm) are superior to that using just rote-learned procedures.

## 3.4.3. A relative assessment

Features of the two illustrative AdDSS implementations are now used to illustrate key characteristics of the AdDSS model that distinguish it from the LRES and the SDSS.

First, AdDSSs can incrementally expand their incomplete knowledge bases over time (e.g., by acquiring system configuration rules and discovering job-sequencing heuristics). Second, all AdDSSs pursue unfocussed reasoning to one extent or another. In both illustrations, what knowledge is acquired is not fully predictable. Also, neither system follows a predefined plan on how to exploit the discovered knowledge advantageously: subsequent processing steps are a function of the currently available knowledge set; for example, encoded sequencing heuristics or rule chunks. Third, some AdDSSs have the capability of discarding relatively useless knowledge (e.g., poorer job sequences (and embedded heuristics)) based on time-dependent priorities. Fourth, some AdDSSs (like the genetics-driven scheduler), by not storing knowledge as rules, are not susceptible to the drawbacks of rule-oriented, fragmented thinking. Fifth, AdDSSs demonstrate the ability to perform consequential knowledge aggregation and derivation. The genetics-driven AdDSS combines several ‘simple’ sequencing heuristics into progressively more complex ‘meta’ sequencing procedures. R1-SOAR chunks sets of existing configuration rules into meta rules.

Sixth, because they use induction, AdDSSs do not attempt to follow logically deduced lines of reasoning and must act on the basis of incomplete and, perhaps, conflicting information. In both examples, the knowledge bases are incomplete to begin with. In the genetics-driven AdDSS, the system repeatedly hypothesizes, tests, and accepts or discards reasoning knowledge based on existing information. This information is conflicting for two reasons. First, the same heuristic could be ascribed different quality measure values at different times. Second, a simple heuristic that works well when used within a meta heuristic may fail when used as part of other meta heuristics. Given such complicating circumstances, with changing evidence, a previously highly-valued hypothesis may be subsequently devalued (or even discarded). Ultimately, only heuristics that have overwhelming evidence in their favor are retained. Likewise, R1-SOAR could generate rules that conflict with existing rules. Lastly, numerous genetics-driven AdDSSs, for example, abound, where the systems are designed to operate under dynamic conditions $[5]$ .

In sum, the AdDSS explicitly addresses and mitigates weaknesses of the LRES model. Like an LRES, an AdDSS is also a reasoning-intensive system. Unlike an SDSS, its emphasis is not on becoming more ‘appealing’ to an end user with repeated exposure but on improved problem-solving proficiency with time. In comparison to ADSS/SDSS, the AdDSS is hardly Symbiotic but is certainly a highly Active system. Its active behavior, however, is not restricted to choosing from a set of preconceived behavior options.

## 4. Concluding remarks

This paper presents a relative assessment of four DSS models - the Symbiotic, Expert, Holistic, and

Adaptive – in terms of their ability to perform independent knowledge management and display novel processing behavior. Conceptually, the HDSS may be regarded as being the most advanced as it postulates holistic recognition and processing capabilities. Progress on realizing the holistic ‘ideal’, has occurred on two fronts. First, success at simulating DAMs on digital computers suggests that holistic recognizers are viable. Second, successful AdDSS implementations suggest that viable, though not holistic, alternatives to the popular LRES exist. However, much work still remains in developing truly holistic systems that couple holistic processors and recognizers.

The current consensus is that the promise of HDSSs may not be realized using digital machines. Digital computers process information sequentially and are superior to humans for performing voluminous, single task-related calculations. However, the human brain, with its richly interconnected set of a trillion, 200 operations/second processors, can perform holistic feats that a digital super computer cannot. The two processing models have very distinct strengths. It currently seems unlikely that even a multiprocessor-based digital system, could adapt to a holistic state comparable to that of a human.

The answer to developing practical HDSSs could lie in ongoing efforts aimed at developing new kinds of computers called nano and DNA computers. These attempts draw on nanotechnology – the technology related to the design and construction of nano-scale machines using molecules as the building blocks. Adleman [1] foresees the beginning of an entire genre of machines that may be categorized as Chemical, Catalytic, Organic, and Inorganic computers. Prototypes have already been constructed for solving the Directed Hamiltonian Path Problem and any class NP problem ([25, 26]). Lipton [4] opines that a practical, super-parallel DNA computer (with a trillion processors) would occupy a bathtub and cost around \$100 000. Experts, however, disagree in their assessments of when practical implementations are likely: the earliest estimate is in 15 years.

In view of the fact that both digital and nano computers have strengths, some experts have suggested hybrid systems that harness their respective strengths, for example, combining conventional semiconductors with light-sensitive switches made from specific proteins [37].

Three other issues may be also brought up in conclusion. First, we have emphasized benefits of utilizing agent-independent systems. There are ‘costs’ involved in having a system learn mainly from its mistakes. Second, the inability of current agent-independent DSSs to explain their novel behavior patterns is a concern in some contexts. Third, in practice, it may be desirable to integrate two or more models (e.g., [45]) for economic and technical reasons.

## Acknowledgements

We extend our profound thanks to Prof. Ed Sibley and the anonymous reviewers whose efforts have significantly enhanced this paper.

## References

[1] L.A. Adleman, Molecular computation of solutions to combinatorial problems, Science 266, 1994, pp. 1021–1024.

[2] S.L. Alter, Decision Support Systems: Current Practices and Continuing Challenges, Addison-Wesley, Philippines, 1980.

[3] A. Barr, E.A. Feigenbaum (Eds.), The Handbook of Artificial Intelligence 2, Morgan Kaufmann, Los Altos, CA, 1982.

[4] T.A. Bass, Gene, Gene. Wired, 1995, p. 114–168.

[5] L.B. Booker, D.E. Goldberg, J.H. Holland, Classifier systems and genetic algorithms, Artificial Intelligence 40, 1989, pp. 235–282.

[6] J.S. Chandler, T. Liang, (Eds.), Developing Expert Systems for Business Applications, Merrill, Columbus, OH, 1990.

[7] G. DeJong, Genetic Algorithm-based Learning, In: Y. Kodratoff, R.S. Michalski (Eds.), Machine Learning: An Artificial Intelligence Approach 3, Morgan Kaufmann, San Mateo, CA, 1990 pp. 611–638.

[8] D.R. Dolk, D.J. Kridel, An active modeling system for econometric modeling, Decision Support Systems 7, 1991, pp. 315–328.

[9] H. Dreyfus, S. Dreyfus, Why expert systems do not exhibit expertise, IEEE Expert 1(2), 1986, pp. 86–90.

[10] J.M. Eich, A composite holographic associative recall model, Psychological Review 89(6), 1982, pp. 627–661.

[11] J. Elam, M. Mead, Designing for creativity: Considerations for DSS development, Information and Management 13(5), 1987, pp. 215–222.

[12] G. Gillund, R.M. Shiffrin, A retrieval model for both recognition and recall, Psychological Review 91(1), 1984, pp. 1–67.

[13] M.H. Hassoun, Associative Neural Memories: Theory and Implementation, Oxford University Press, 1993.

[14] C. Hewitt, The Challenge of Open Systems, BYTE, 1985, pp. 223–242.

[15] J.H. Holland, Adaptation in Natural and Artificial Systems, The University of Michigan Press, Ann Arbor, MI, 1975.

[16] C.W. Holsapple, V.S. Jacob, R. Pakath, J.S. Zaveri, Learning by problem processors: Adaptive decision support systems, Decision Support Systems 10(2), 1993, pp. 85–108.

[17] C.W. Holsapple, V.S. Jacob, R. Pakath, J.S. Zaveri, A genetics-based hybrid scheduler for generating static schedules in flexible manufacturing contexts, IEEE Transactions on Systems, Man and Cybernetics 23(4), 1993, pp. 953–972.

[18] C.W. Holsapple, A.B. Whinston, Business Expert Systems, Irwin, Homewood, IL, 1987.

[19] C.W. Holsapple, A.B. Whinston, Knowledge-based organizations, The Information Society 5(2), 1987, pp. 77–90.

[20] C.W. Holsapple, A.B. Whinston, Decision support in multi-participant decision makers, Journal of Computer Information Systems 31(4), 1991, pp. 37–45.

[21] M.S. Humphreys, J.D. Bain, R. Pike, Different ways to cue a coherent memory system: A Theory of episodic semantic and procedural tasks, Psychological Review 96(2), 1989, pp. 208–233.

[22] M.T. Jelassi, C. Fidler, K. Williams, The emerging role of DSS: From passive to active, Decision Support Systems 3, 1987, pp. 299–307.

[23] P.G.W. Keen, M.S. Scott-Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

[24] J.E. Laird, A. Newell, P.S. Rosenbloom, SOAR: An architecture for general intelligence, Artificial Intelligence 33(1), 1987, pp. 1–64.

[25] R.J. Lipton (1994) Speeding Up Computations via Molecular Biology, Ftp://ftp.cs.princeton.edu/pub/people/rjl/bio.ps..

[26] R.J. Lipton, DNA Solution of Hard Computational Problems, Science 268, 1995, pp. 542–548.

[27] M. Mahmood, M. Gowan, S. Wang, Developing a prototype job evaluation expert system: A compensation management application, Information and Management 29(1), 1995, pp. 9–28.

[28] M.L. Manheim, Issues in Design of a Symbiotic DSS, In: R.W. Blanning, D. King (Eds.), Proceedings of the 22nd Annual Hawaii International Conference on Systems Sciences 3, 1989, pp. 14–23.

[29] M.L. Manheim, S. Srivastava, N. Vlahos, J. Hsu, P. Jones, A Symbiotic DSS for Production Planning and Scheduling, In: J.F. Nunamaker (Ed.), Proceedings of the 23rd Annual Hawaii International Conference on Systems Sciences 3, Computer Society Press of the IEEE, Washington, D.C., 1990, pp. 383–390.

[30] J. McDermott, R1: A rule based configurer of computer systems, Artificial Intelligence 19(1), 1982, pp. 39–88.

[31] R.S. Michalski, Understanding the Nature of Learning: Issues and Research Directions, In: Machine Learning: An Artificial Intelligence Approach 2, Morgan Kaufmann, San Mateo, CA, 1986 pp. 3–25.

[32] R.S. Michalski, Y. Kodratoff, Research in Machine Learning: Recent Progress, Classification of Methods, and Future Directions. In: Machine Learning: An Artificial Intelligence Approach 3, Morgan Kaufmann, San Mateo, CA, 1990, pp. 3–30.

[33] M. Minsky, The Society of Mind, Simon and Schuster, NY, 1986.

[34] B.B. Murdock, A theory for the storage and retrieval of item and associative information, Psychological Review 89(6), 1982, pp. 609–626.

[35] K.S. Narendra, Adaptive Control of Dynamical Systems Using Neural Networks, In: Handbook of Intelligent Control: Neural, Fuzzy, and Adaptive Approaches, Van Nostrand Reinhold, NY, 1992, pp. 141–183.

[36] D. Partridge, The scope and limitations of first generation expert systems, Future Generation Computer Systems 3, 1987, pp. 1–10.

[37] D. Pescovitz, The Future of Nanotechnology, Wired, 1995, p. 58.

[38] R. Pike, Comparison of convolution and matrix distributed memory systems for associative recall and recognition, Psychological Review 91(3), 1984, pp. 281–293.

[39] J.G.W. Raaijmakers, R.M. Shiffrin, Search of associative memory, Psychological Review 88, 1981, pp. 93–134.

[40] P. Rosenbloom, J. Laird, J. McDermott, A. Newell, E. Orciuch, R1-SOAR: An Experiment in Knowledge-intensive Programming in a Problem Solving Architecture. In: Proceedings of the IEEE Workshop on Principles of Knowledge Based Systems (Denver), Computer Society Press of the IEEE, Washington, D.C., 1984, pp. 65–71.

[41] V. Salas-Fumas, Strategic Planning: Implications for the Design of DSS, In: Decision Support Systems: Theory and Applications, NATO ASI Series F, 31, Springer-Verlag, NY, 1987, pp. 429–449.

[42] D. Shpilberg, L.E. Graham, Developing ExperTAX: An expert system for corporate tax accrual and planning, Auditing: A Journal of Practice and Theory 6(1), 1986, pp. 75–94.

[43] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[44] P.A. Stefanski, J. Wnek, J. Zhang, Bibliography of Recent Machine Learning Research: 1985–1989. In: Y. Kodratoff, R.S. Michalski (Eds.), Machine Learning: An Artificial Intelligence Approach 3. Morgan Kaufmann, San Mateo, CA, 1990, pp. 685–789.

[45] E. Turban, P.R. Watkins, Integrating expert systems and decision support systems, MIS Quarterly 10, 1986, pp. 121–136.

[46] P. Werbos, T. McAvoy, T. Su, Neural Networks, System Identification, and Control in the Chemical Process Industries. In: Handbook of Intelligent Control: Neural, Fuzzy, and Adaptive Approaches, Van Nostrand Reinhold, NY, 1992, pp. 283–356.

[47] P.H. Winston, Artificial Intelligence. Addison Wesley, Reading, MA, 1992.

[48] L. Wos, R. Overbeek, E. Lusk, J. Boyle, Automated Reasoning, Prentice Hall, Englewood Cliffs, NJ, 1984.

Dinesh Mirchandani is a doctoral candidate at the University of Kentucky. He will be joining Grand Valley State University, Michigan, in January 1999, as an Assistant Professor in the Seidman School of Business. His other research interests include global IS planning and electronic commerce. He has published in Communications of the ACM, Journal of Organizational Computing and Electronic Commerce, and in the proceedings of the Decision Sciences Institute and the Association for Information Systems conferences.

Ram Pakath is an Associate Professor of Decision Science and Information Systems at the C.M. Gatton College of Business and Economics, University of Kentucky. His research focuses on (a) designing and implementing efficient processors that use hybrid and adaptive problem processing techniques, and (b) assessing the impacts of support systems that utilize multimedia technology on user productivity. His work has appeared in such forums as Behaviour and Information Technology, Computer Science in Economics and Management, Decision Sciences, Decision Support Systems, European Journal of Operational Research, IEEE Transactions on Systems, Man, and Cybernetics, Information and Management, Information Systems Research, and Journal of Computer Information Systems. He is author of the book Business Support Systems: An Introduction, 2nd Edition, published by Copley and has contributed refereed material to several books. He served as Director of the MIS Research Lab of the college from 1993–1997. He is an Associate Editor of Decision Support Systems and an Editorial Board Member of Journal of End User Computing and Management. His research has been funded by IBM, Ashland Oil, the Gatton College, and the University of Kentucky.
