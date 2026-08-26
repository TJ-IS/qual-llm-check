---
otero_id: 17151
otero_key: "EV7DGMEV"
title: "Knowledge representation in expert systems for process control"
authors: "Berndt Böhme; Ralf Wieland"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90026-n"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge Representation in Expert Systems for Process Control

Berndt BÖHME and Ralf WIELAND

Leipzig University of Technology, Department of Process Automation, Leipzig 7030, GDR

The application of so-called “higher automation functions” in complex systems is usually connected with considerable difficulties. In most cases these automation tasks can satisfactorily be solved only by the help of a suitable decision support system. Considering the knowledge base in process automation a special framework for knowledge representation in XPS for process control and an original inference strategy will be discussed. Features of quality and demands on knowledge representation components in real-time expert systems are formulated. The advantages of hybrid representation schemes utilizing algorithmic (deep) knowledge mainly in the procedural part of the knowledge base are pointed out. The presented solution was introduced developing the real-time expert system shell PROCON.

Keywords: Process Automation, Knowledge Based Control, AI-software, XPS-shell, Expert System, Knowledge Representation, Frame Hierarchy, Deep Knowledge, Fast Inference.

## 1. Introduction

Ralf Wieland received his PhD from the Leipzig University of Technology in 1988. His research activities include the development of AI-software tools for realtime operation and their integration into hierarchical process automation systems.

The development in microprocessor technology and computer science in the last ten years has caused substantial changes in process automation technology. Nowadays the new generation of decentralized process control systems which are sufficiently reliable and satisfy the requirements for high performance allows to an increasing extent the implementation of so-called “higher automation functions” such as

![](/api/attachments/EV7DGMEV/fulltext/images/5e9aadef803973129bcf9b07ece1b30402bcec5f77a207748bf1d8ea68209928.jpg)

Berndt Böhme received his PhD from the Moscow University of Chemical Engineering in 1975 and his D.Sc. degree from the Leipzig University of Technology in 1983. In 1988 he was appointed a full professor for automation at the Berlin University of Technology. His main area of research is concerned with higher automation tasks in process/production automation and the application of knowledge based methods to hierarchical control systems.

\- operation guidance,

\- process optimization,

\- production management,

\- emergency/security control,

\- emergency management,

where the last two tasks are designed to prevent hazards in processing units as well as in the whole plant by minimizing losses.

![](/api/attachments/EV7DGMEV/fulltext/images/aa8e540b75434f7d768cb33b1bffa6c6509ee422f521bdf0d7e6c20d79786940.jpg)

The application of these automation tasks to complex systems faces us usually with a lot of features making substantial trouble.

Such features are

\- markedly incomplete information on the system and the running processes,

\- fuzzy and/or confusing information,

\- important characteristics of the system cannot be fully formalized by classical methods,

\- multi-objective decision making,

\- disturbances are characterized by high amplitudes,

\- large volume of data,

\- the set of admissible control actions cannot be overlooked.

Due to these characteristics and the usually high complexity of the systems under consideration classical methods of mathematical modelling and control fail, mainly because of the enormous expenditure spent on the development and the strong real-time conditions.

There is no chance to overcome all these difficulties alone by revising conventional methods or creating and improving nonconventional methods of process automation and their application to automatic control systems. Past experience has shown that the application of the majority of higher automation functions is not reasonable without the decision maker (DM) and his central position in a process control system even in future.

Owing to the high responsibility of the DM, the features of the system to be controlled and the generally hectic conditions during decision making the DM needs a suitable decision support system for determining an effective control. Using expert knowledge it would be desirable to create an expert system (XPS) the roots of which lie in the field of artificial intelligence. Today the development in AI has reached a stage which to an ever increasing extent allows serious applications [1], [2], [3], [4].

The application of knowledge based methods in process automation is primarily connected with the following advantages:

1. They enable the creation of effective strategies especially for solving combinatorial problems.

2. Solutions are characterized by a high flexibility relating to a system enlargement and a high portability relating to new problems.

3. Due to the continuous increase in AI-tools (knowledge representation languages, shells, tool-kits) the effort for creating intelligent system solutions diminishes more and more.

However the ability of expert systems to operate under strong real-time conditions is limited by several factors.

In general this ability depends on the

\- size of the knowledge base,

\- inference strategy,

\- knowledge representation scheme and the structure of the knowledge base,

\- efficiency of the software solution,

\- version of on-line link and the real-time operating system,

\- organisation of the user dialogue including the explanation facilities,

\- performance of the computer used for execution.

If the preconditions are equal the representation scheme of a given knowledge base in connection with the chosen inference strategy is of primary importance for real-time operation.

In this paper a special framework for knowledge representation in process control systems and an original inference strategy will be discussed.

The presented solution was introduced developing the expert system shell PROCON at the Leipzig University of Technology [5].

## 2. The Knowledge Base in Process Automation

Knowledge in process automation systems is always characterized by a certain structure. In addition this structure is very often time-dependent and in this way carrier of essential process information. If we are now successful in obtaining and transforming this structure in a suitable framework, the efficiency of the inference process can be increased markedly.

The knowledge base in expert systems is usually divided in facts and rules where in real-time systems the descriptive knowledge includes current process information coming from both the process control system and the decision maker. With regard to its semantic background the knowledge base covers:

1. A copy of the objective reality - that is a mathematical model of the technological system to be supervised or controlled on the basis of nonconventional forms of description.

The so implemented knowledge of facts and rules reflecting mainly static but also dynamic features, characteristics and relations forms the declarative part of the knowledge base that could also be denoted as the technological knowledge base.

2. Strategies and procedures for solving the desired automation tasks (e.g. malfunction diagnosis, process monitoring, emergency management). This knowledge is based in a high degree on human experience and unformalized information about the process to be controlled.

This expert knowledge represents the procedural part of the knowledge base. It includes also instructions for applying the mathematical model stored in the declarative part of the knowledge base.

The components of the knowledge base discussed is illustrated in table 1.

Table 1  
The Knowledge Base in Process Automation.

<table><tr><td rowspan="2"></td><td rowspan="2">Knowledge represented by facts</td><td colspan="3">Knowledge represented by rules</td></tr><tr><td>Technology</td><td>Diagnosis</td><td>Control</td></tr><tr><td rowspan="3"></td><td>* topology (structure of the system)</td><td>* functional behaviour of the tech-nolog. process</td><td rowspan="2">knowledge for fault-finding detecting the reason causing the current or prognostic sys-tem state</td><td rowspan="2">reflection of all feasible control actions and their effects on the process (including emergency control)</td></tr><tr><td>* information concerning - class representatives - class boundaries - feasible valu. of state and control varia.</td><td>* relations to the external world</td></tr><tr><td>* instructions for system safety - alarms - criteria for danger-ous situations</td><td></td><td>also deep knowledge in the form of conventional mathematical models</td><td></td></tr><tr><td>Data from pro-cess control system or operator</td><td colspan="4">* system state - current input state, output and control variables - disturbances - prognostic data Technological knowledge declarative part of KB Expert knowledge procedural part of KB</td></tr></table>

A typical feature of the procedural knowledge base consists in its limited truth. In complex systems we are very often faced with uncertain or incomplete data and fuzzy expert knowledge. This situation can only partly be improved by an efficient knowledge acquisition component of the expert system. In general the fuzzyness of the expert knowledge and data should be taken into consideration for decision making.

There are three principal ways for solving this problem. The trustworthiness of expert knowledge (and also unreliable data) can be valued by

\- Bayesian probabilities,

\- certainty factors,

\- using fuzzy sets.

In our opinion the creation of a fuzzy knowledge base leads to a markedly reduced error risk and may be regarded as the most elegant solution. However, when applying the fuzzy set theory we are always faced with additional expenditure in the fields of knowledge acquisition and knowledge processing.

Furthermore should be mentioned that the derivation rules for logical deduction applied in the inference engine (e.g. modus ponens) are not valid for any realization of fuzzy variables. It can be shown that these deduction rules lose their tautological character in the case of fuzzy logic. This is a very interesting matter of fact which, however, has been investigated insufficiently so far.

In satisfying the demands of real-time operation expert systems for process automation require the integration of conventional control software that could also be denoted as deep knowledge. The utilization of algorithmic procedures representing mathematical models as well as diagnosis and control algorithms on the basis of conventional forms of description is necessary or desirable for the following reasons:

1. Knowledge implemented in this way and reflecting the system behaviour especially in typical situations or events by well - adapted mathematical modells is sharper and mostly safer than the formalized expert knowledge.

2. This knowledge will be processed faster, thus improving the ability of the system to operate under real-time conditions.

3. In most of the industrial branches is a lot of well-tried conventional software that can be applied in expert systems without substantial alterations. By utilizing this software the expenditure for development could considerably be reduced, above all, in the phase of knowledge acquisition.

The creation of hybrid systems utilizing algorithmic (deep) knowledge mainly in the procedural part of the knowledge base is one of the most important features of expert systems in process automation. However the application of such systems requires suitable tools supporting the combination of AI-software with software modules on the basis of common (imperative) languages.

## 3. Knowledge Representation Schemes

Knowledge representation schemes can be subdivided in general into four common basic structures:

\- Predicate calculus,

\- Associative networks,

\- Production rule systems,

\- Frames.

Each of this basic structures is characterized by specific advantages and disadvantages and can be transformed into any other scheme.

However, by choosing a certain form with respect to a given structure of the knowledge base we should also take into account that this choice will have essential consequences concerning the software solution.

So knowledge described by predicate calculus can nearly ideally be implemented by PROLOG because its syntax is qualified without doubt for the conversion of such information structures. Furthermore PROLOG includes already essential components for knowledge processing so that using this language applications can be implemented fast and without problems worth mentioning.

However, choosing a certain PROLOG version you are in any case fixed with respect to the complete inference mechanism. Improvements that are intended to accelerate the operation speed in a given version are complicated and cannot be recommended also for other reasons.

An associative network is in principle a network of directed graphs in which the nodes represent semantic entities. Semantic entities, in turn, are used to describe physical things, processing units, important features, states, events, situations and so on. The arcs between the nodes in the network model represent more or less standardized binary relationships of the type

\- “is a”,

\- “is a subset of”,

\- “has property”.

The application of associative networks seems to be advantagously to represent systems in cases of a time-dependent structure or when the control causes structural changes and the system is characterized preferably by binary states and relations. In this connection power supply systems and manufacturing systems are very typical examples.

At present production systems are very popular and numerous applications can be found. Because of their basic structure

IF $\langle$ condition $\rangle$ AND $\langle$ condition $\rangle$

AND ... THEN $\langle$ action $\rangle$

production rules are an excellent way to formalize the procedural part of the knowledge base, especially to represent expert knowledge.

However production rules describe only the conditioned reflecting part of human reasoning; therefore they can be used only to represent simple facts and relations.

In general the description of complicated knowledge by the help of production rule systems or associative networks leads to a vast knowledge base that cannot be overlooked. In this case it will be very difficult to check the knowledge with regard to its completeness and consistency. In addition we get more problems to organize a time-efficient control of the inference process.

Besides production systems frames suggested by Minsky in 1975 becoming more and more important because of their excellent possibilities to create a well organized knowledge base.

Each frame consists of a set of slots representing characteristic features of the system, pointing to subframes or containing comments.

However, in the field of process automation it should be taken into consideration, that a framework using frames only is principally characterized by substantial disadvantages arising from the strongly pronounced declarative feature of this representation scheme. Summerizing our experience in this field we try now to formulate features of quality and demands on knowledge representation components in expert systems for process control:

(1) System-aided knowledge acquisition with effective solutions for

\- knowledge formalization and representation (enter-, alter-, insert- options, syntax checking routines, graphic support),

\- knowledge inspection (suitable visualization of relationships, consideration and check of elements, segments or classes with a high comfort),

\- knowledge verification (test for logical correctness, fidelity and completeness).

(2) An extensive explanation capability providing the transparency of the inference process. The usually defined HELP-, EXTEND-, WHY?- and HOW?-options in any case should be performed by different interpretation levels. The wanted or needed depth of interpretation can be selected by the user or is given automatically by the system in dependence on the user qualification and/or the time restrictions. Effective solutions support the man-machine dialogue and must be regarded as a necessary precondition for a pretentious learning component.

(3) Ability to learn. In a first stage this property should cover at least facilities detecting leaks of knowledge, faulty or useless knowledge. This learning arises from

\- new theoretical and practical findings

\- growing experience

\- technological changes

\- system expansion

\- modification of production goals

and requires in essence the above-mentioned capabilities to manipulate the knowledge base.

(4) Finally the software implementation properties to a high degree depending on the efficiency of the chosen programming language influence among other the attainable level of the

![](/api/attachments/EV7DGMEV/fulltext/images/085c446d5595bd9236915aaae42f9c88a18ec1973455aea199dc793c3b35b505.jpg)  
Fig. 1. Framework of Knowledge Representation in PROCON.

\- Software reliability and the

\- Fault tolerating ability

of the created expert system.

So we come to the conclusion that it would be desirable and useful to create hybrid knowledge representation schemes combining frames with the other representation forms. This leads to a special frame taxonomy, describing typical events, states, situations, plants, processing units up to elementary devices.

In such a scheme the slots represent the knowledge of facts respectively point to subframes whereas the expert knowledge for solving the automation task is integrated into the frames by production rules, associative networks or other forms.

In that way we obtain a well structured knowledge base leading for instance in the case of production rules to a drastic reduced set of this rules to be matched by the interpreter performing the inference process. Furthermore solutions for proving the knowledge base concerning its consistency as well as components for knowledge acquisition and learning become simpler because the expert knowledge is arranged semantically.

## 4. Knowledge Representation in the Shell PROCON

The idea discussed was applied in the shell PROCON as is illustrated in fig. 1. The inference strategy in PROCON performs two different stages. In a first stage – the diagnosis phase – the current system state is determined whereas in the second stage – the control phase – a corresponding control will be generated.

Obviously the effort for generating a control can be essentially reduced by a well designed diagnosis. At any rate a well balanced proportion between the diagnosis and control stages allows to speed up the inference process and in this way to improve one of the important features of expert systems in process automation – the ability to operate under more or less strong real time conditions.

In order to meet this requirement the diagnosis strategy in PROCON embodies an acceptable compromise between universality and time-behaviour.

Starting from a superframe representing the root of the frame-hierarchy each subframe (schema) can be reached. The number of subframes that can be directly linked with an upper frame as well as the depth of the tree is not limited in PROCON. Every schema contains expert knowledge in any form (e.g. production rules) reflecting the world with regard to the given level of taxonomy.

It should be underlined that in every schema conventional algorithmic procedures can be called and executed. Coming down in the frame hierarchy the integrated knowledge becomes more and more specialized from level to level.

Every diagnosis or action frame involves different kinds of knowledge:

(1) Documentary knowledge

\- specifications and comments

(2) Taxonomy knowledge - relations to the frames that are linked directly

(3) Declarative knowledge
- technological constants and variables of the typ number, string, boolean, time

(4) Functional knowledge

\- daemons to instantiate the variables

(5) Procedural knowledge

\- set of rules for problem solving

\- Derivation rules:

rules for selecting preferential frames in performing the search
- Proof rules:

rules for proving the selected subframe

(6) Control Knowledge

\- for consultation control (i.e. performing the problem solving procedure)

\- for report control (i.e. presentation of the consultation results)

As it is usual in frame hierarchies the knowledge representation and processing procedures in PROCON involve an effective inheritance mechanism.

This property is also used to provide PROCON with an original redundancy concept to replace faulty process variables.

## 4. The Inference Strategy in PROCON

Concerning the diagnosis phase the inference strategy in PROCON in principle can be characterized as a forward classification on the basis of a breath first top down search. A special hypothesis and test strategy in every classification step allows an effective search even in cases of uncertainty. The derivation process in PROCON can be briefly described as follows.

Utilizing the derivation rules defined in a given diagnosis frame we try to determine the subframe on the next lower level that fulfils the implemented hypothesis with the highest preference. The values of preference called CF-values are calculated by using the functions V and Y.

$$
V _ {F, i} ^ {n} \left(m _ {1}, m _ {2}, \dots , m _ {n}\right)\rightarrow \left(z _ {1}, z _ {2}, \dots , z _ {k}\right).
$$

F - name of the frame,

$$
i \quad - \text {   index   of   the   function,   } i = 1, 2, \dots , I,
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
n - number of features in the given function,  $n \in N$ ,
</div>

$m_{j}$ – features of the type $s_{j}$ , characterizing the process state and stored in a dynamic data base, $j = 1, 2, \ldots, N$ ,

k - number of subframes, directly linked with $F$ ,

$$
\begin{array}{l} Y _ {F, i} = Y _ {F, i - 1} + V _ {F, i} ^ {n}, \qquad i = 1, 2, \ldots , I, \\ Y _ {F, i} = \left\{a _ {1}, a _ {2}, \ldots , a _ {k} \right\}, \\ Y _ {F, 0} = \left\{0, 0, \ldots , 0 \right\}. \end{array}
$$

Each derivation rule combines a function V representing a certain process condition with a preference vector that can be used for testing the membership of a subframe. In this way every subframe on a given level is assigned a preference value from each derivation rule. Performing the recursive function Y all CF-values are added step by step for each subframe. After exceeding an upper CF-level for a certain subframe the derivation process is stopped and the selected subframe will be verified by using the proof rules. If the result is positive then the classification step will be executed, otherwise the subframe is excluded from further investigations and the derivation process is continued. In doing so we determine, at last, a subframe with a high (or the highest) preference and now we are able to carry out the next search step.

If no subframe can be verified (because all CF-values are too low) the inference process is interrupted and the associated action frame will be performed (if an action frame is assigned), otherwise a message is given to the decision maker. The described diagnosis strategy is characterized by some excellent properties such as high flexibility and speed of knowledge processing compared with hypothesis and test strategies known.

After terminating the diagnosis phase the inference procedure switches over to the control phase to perform the selected control frame. There are some possibilities in PROCON to generate a suitable control.

First of all there is a rule interpreter to process the implemented expert rules. In order to speed up the determination of the control in certain cases PROCON provides the opportunity for starting and processing of conventional control software written in TURBO-PASCAL, C, FORTRAN as well as PROLOG-modules on the basis of TURBO-PROLOG or other modifications. In this way PROCON satisfies the demands of real-time mode defined in chapter 2.

In addition PROCON has an external interface for smooth integration of dBASE III solutions allowing a read and write file access.

## 6. Concluding remarks

PROCON is implemented in GCLISP and runs on advanced PC (AT and 100% compatibles).

There is no doubt that LISP is extraordinarily suited for implementations of frame based knowledge representation schemes. Using LISP all mechanisms for knowledge processing have to be created by the system designer. This allows the integration of original ideas in all components of the expert system, especially in connection with

\- the internal information representation,

\- the organisation of the matching process,

\- search strategies above all in hybrid schemes. Here are at present the main reserves in expert systems with regard to the running time.

Compared with other PC-shells known, PROCON has a powerful inference engine, a sophisticated knowledge representation system, an advanced environment for development and user support and a real-time interface allowing the full access to a process automation system.

Especially for diagnosis and control tasks in complex systems PROCON allows the creation of serious expert systems.

## References

[1] KOMMTECH'88. 5th European Congress Fair for Technical Automation. Essen, June 7–10, 1988. Congress III "Expert systems in planning and production".

[2] 10ht IFAC World Congress on Automatic Control. Munich, July 27–31, 1987. Preprints, subject area 15.1 (vol. 6).

[3] GI-Kongress Wissensbasierte Systeme. München 20./21. Oktober 1987. Informatik Fachberichte 155. Springer Verlag Berlin, Heidelberg, New York, Tokyo.

[4] INFO'88. 4. Kongress der Informatiker der DDR. Dresden, 22.-27. Februar 1988.

[5] Böhme, B., Balzer, D., Wieland, R., May, V. PROCON I – Ein Expertensystem-Shell für die Prozesssteuerung. In [4], Proceedings pp. 195–197.
