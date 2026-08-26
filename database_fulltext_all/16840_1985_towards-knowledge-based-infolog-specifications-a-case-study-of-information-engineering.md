---
otero_id: 16840
otero_key: "CF4M8XDY"
title: "Towards knowledge-based infolog specifications A case study of information engineering"
authors: "Helder Coelho; António Rodrigues; Amilcar Sernadas"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90064-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards Knowledge-Based Infolog Specifications A Case Study of Information Engineering

Helder COELHO $^{\dagger}$ , António RODRÍGUES $^{\bullet}$ and Amilcar SERNADAS \*

$^{\dagger}$ Centro de Informatica, Laboratorio Nacional de Engenharia Civil, 101 Av. do Brasil, 1799 Lisboa Codex, Portugal; $\bullet$ DE-IOC, Faculdade de Ciencias, 58 Rua da Escola Politecnica, 1294 Lisboa Codex, Portugal; $*$ DICC, Faculdade de Ciencias, 58 Rua da Escola Politecnica, 1294 Lisboa Codex, Portugal

A radically new approach to computing, the so-called knowledge-based information processing is achieving striking success in supporting activities needing logical power, human judgement, reasoning and expertise. It offers universal applicability for problem-solving, in particular in more complex tasks than those presently handled by computer systems. The current state of the art and future prospects for the development of a computer system which either performs expert tasks automatically or is used interactively by experts to increase their productivity are reviewed. The weak points we need to look at, namely the lack of guidelines for building such systems, and some dead ends are indicated. Some new results are expected by applying this key technology to our case study, the construction of a Systems Specification Support System (S4). Its knowledge base written in PROLOG captures and encodes human expertise about the INFOLOG model and INFOLOG specifications, which is made available via consultation to formulate specifications and, possibly, advice. The architecture of the knowledge base is presented by discussing its abstraction levels. This investigation provides also a methodology in structuring a systems analyst's knowledge about an application. This means how to find out the main kinds of objects, including their relationships, in some problem domain.

Keywords: Infolog; Knowledge-base; Knowledge engineering; Information system design; Logic programming; Prolog

![](/api/attachments/CF4M8XDY/fulltext/images/ff449aff19135fcaae0787a90dc8e355e81c4330f59c00373ed91c4b6e9fb923.jpg)

A. Rodrigues received a degree in Applied Mathematics from the University of Lisbon, in 1982. Since then, he has been assistant lecturer at the Department of Statistics of the Faculty of Sciences of the University of Lisbon. In 1982/83 he worked as research assistant in the INFOLOG project on the development of an expert system for system specification support. He is now working for a M.Sc. degree in Operations Research and Systems Engineering at the Technical University of Lisbon. Meanwhile, he has produced several publications on methodological aspects of modelling and programming.

![](/api/attachments/CF4M8XDY/fulltext/images/3fa0ef965068a7fe434ad85e2b00d6f600327385368f23964977e190b540e0cf.jpg)

A. Sernadas received a degree in Electrical Engineering from the Technical University of Lisbon, in 1975, and a Ph.D. (Computer Science) from the University of London, in 1980. Later on, he received a doctoral degree from the University of Lisbon (1981). From 1973 to 1976 he was a research assistant at the Technical University of Lisbon, in the Laboratory of Plasma Physics. Afterwards he joined the Department of Applied Mathematics of the Faculty of Sciences of the University of Lisbon as a lecturer. In 1978 he was awarded a scholarship for studying abroad. He returned to the Faculty of Sciences two years later. He is now Professor at the Department of Computer Sciences (since he received the professorship degree in 1982, from the University of Lisbon). His current interests include database design, program and specification logics, and decision support system development.

![](/api/attachments/CF4M8XDY/fulltext/images/5b580b92c4d0533e09b1b097650d110658af10f48c5d6cb003813512dd87a286.jpg)

Helder Coelho joined the Laboratório Nacional de Engenharia Civil (LNEC, Lisboa) in 1973, after five years as Electronic Engineer in the Laboratório de Física e Engenharia Nucleares (Lisboa). From 1974-78, he studied Artificial Intelligence techniques at the Universities of Edinburgh and Aix-Marseille. In addition, from 1977-80, he was responsible for software development for man-computer communication in Portuguese. He received his Ph. D. in Artificial Intelligence from the University of Edinburgh, his degree of Specialist in Informatics from LNEC, in 1980, and a doctoral degree in Computer Science from Universidade Nova de Lisboa. He is coordinator of the Information Systems Sector at the Informatics Department of LNEC, and supervises several projects on Logic Programming.

## 1. Introduction

An approach to computing has emerged which will revolutionize the development and use of computer-based systems: Intelligent Knowledge-Based Systems (IKBS), has already achieved practical successes, governmental (Moto-oka, 1981; Alvey, 1983) and commercial support (ICOT, JRI, MCC). It contrasts classical computer software methodology which is limited to relatively uniform processing of presented data and answers only to specific inputs and situations included in the program design. Most intelligent knowledge-based systems, including the so-called expert systems, display utility, performance and transparency by supporting managers and professionals in activities requiring human judgement, reasoning and expertise. As a general principle, they reflect the decision-making processes of a human specialist and encapsulate a large body of organized knowledge (general facts, rules and principles) about a defined problem domain in a knowledge base. Under the control of their users, IKBS mechanize that knowledge, i.e., they simulate the reasoning processes of a human expert in the area, drawing deductions or inferences from the knowledge base and, typically, arrive at conclusions which advise users on appropriate actions.

Artificial Intelligence is defined as an empirical science: the data are programs, and the conclusions, derived upon studying them, include understanding the phenomenon of intelligent action itself. But, by constructing IKBS, arguments about what computers can do are replaced by demonstrations. So, this activity is providing major advances in Computer Science.

The applications investigated and developed so far constitute a guide for a new generation of IKBS. But, despite intensive work they are too domain dependent, and the central question of knowledge engineering remains on how to proceed, i.e., on the appropriate definition of guidelines, for building up the next IKBS. Thus, a case study of a methodology that has been extremely effective in the Information Systems domain was begun which can easily be adapted to other situations such as those in IKBS.

This paper presents the first steps taken when considering the construction of a Systems Specification Support System (S4). Section 2 reviews the current state of the art of knowledge engineering, from the perspective of the development of S4. Section 3 describes the environment of the case study, the INFOLOG project. Section 4 describes the S4 overall structure, emphasizing the three main components: decision support, information management, and computer-aided design. Section 5 describes the INFOLOG model and its specifications, and the problem faced by the design of a knowledge base for INFOLOG specifications. Section 6 concludes by pointing out one of the main goals of this research, the development of an IKBS taking into account the methodologies of Information Systems.

The use of this approach in the development of a pure (i.e., without a computer-aided design component) decision support system will be illustrated in a follow-up paper.

## 2. Knowledge Engineering: Current State of the Art

The current state of IKBS research is the outcome of work in Artificial Intelligence and Computer Science. Research has been directed towards technologies, capabilities, tasks and applications; concepts were put forward; high-level non-procedural languages suited to the knowledge representation and inferential problem-solving needs of IKBS were developed; relevant machines were designed and architectures tested. In fact:

(1) Research on internal capabilities of IKBS has provided methods of knowledge representation and means of problem-solving;

(2) Research on external capabilities has provided some techniques for speech and natural language analysis and synthesis, image and object handling;

(3) Research on tasks and on applications has identified forms of structuring knowledge, adjusted to the domains of those tasks.

However, it remains difficult to find means for helping the development of new IKBS, in particular as there is no guidebook for advising on suitable choices.

Therefore, there are fundamental and challenging problems to be tackled at IKBS. Long-term research is needed on system capabilities for knowledge representation and inferential problem-solving, and particularly on planning and learning, natural language and image understanding. There are equally fundamental problems to be tackled, such as those of system design and architecture, of technologies, and of relating a system to its environment. The next generation of case studies must reflect on these problems in order to envisage concrete guidelines for improving the design of IKBS according to their problem domains.

In this section the basic concepts and notions relating to the design of an IKBS are introduced. The types of problems and of problem-solving methods are classified because their clarification is important to devise the intelligent machinery and the attached technologies. The achievement and the status of knowledge engineering are discussed, by pointing out the actual central issues and unexplored topics. This discussion is extended by choosing the programming language PROLOG as a tool. The stages of development of the existing IKBS, the so-called pragmatics of knowledge engineering, are analysed and it is found that the steps currently envisaged are considered only as an advice. Finally, some architecture principles are collected, suggested by different IKBS, and contradictory opinions are put forward, enhanced by the application domain themselves.

## 2.1. Basic Concepts and Notions

An Intelligent Knowledge Based System (IKBS) is a system which uses inference to apply knowledge to perform a task (Jones, 1982). Its main modules, a knowledge base (KB) and an inference engine, model the abilities of the best practitioners of some domain of problems. A third component, the user interface, provides a friendly communication channel to the system.

The knowledge base is the part of the system which contains information about problem-solving techniques. It is simply a data structure which cannot itself produce any advice unless it is interpreted by the inference engine (also called interpreter).

An expert system, a subclass of IKBS, can be thought of as a deductive data base of expert knowledge and of user-supplied information. The data base concept is viewed as a collection of assumptions (say, a theory), where queries are theorems to be proved from the assumptions, and specifications are interpreted as programs.

The characteristic property of a system with any intelligence is its ability to manipulate an arbitrary store of knowledge according to general inference procedures to carry out some broad task. In an application, knowledge can include facts, theorems, heuristics, equations, rules of thumb, assumptions, strategies, tactics, probabilities, advice, and causal laws. To manage these forms of knowledge one may adopt a representation scheme (a way to codify knowledge) and an inference scheme (a way to use knowledge to derive new knowledge). Such intelligent systems can be ranged in power according to the scale and variety of their knowledge, procedures and tasks (Jones, 1982):

(i) Systems with full intelligence: They are capable of carrying out very general tasks in very general ways, and they apply arguments to ideas to obtain ideas. Such a system may have more than 100 000 rules!

(ii) Systems with limited intelligence: They are capable of carrying out incompletely specified tasks in incompletely specified ways, and they apply inferences to knowledge to obtain knowledge. Currently, they are called intelligent knowledge-based systems (IKBS). Expert systems (ES) are a subclass of these systems. Such a system may have more than 10,000 rules!

(iii) Systems with no intelligence: They are capable only of carrying out very specific tasks in very specific ways, and they apply algorithms to data to obtain data.

IKBS differ from other large computer programs written to solve special decision-making problems on account of the use of knowledge, which is as important as reasoning. Rules are not implemented as subroutines or in any other part of the code of the program; instead, the rules for a particular task are written in a specialized language, which is then input by the program to produce an internal representation.

There is a clear separation of general knowledge about the problem (the rules forming the knowledge base, KB) from information about the current problem (the input data) and methods for applying the general knowledge to the problem (the rule interpreter). Any KB contains the expertise of some domain, i.e., cause-effect relationships, implications, heuristics, inferences, plans of action and analytic procedures. Therefore, an IKBS operates at four interrelated levels of knowledge processing: domain knowledge (application level); generic knowledge (task level); basic knowledge (capability level); and formal knowledge (technology level).

Applications determine individual task systems; tasks define subclasses of IKBS; capabilities are common to all IKBS; technologies serve other systems as well as IKBS.

## 2.2. Taxonomy of problem-solving types

The study of problem-solving is central for the construction of an IKBS. The analysis of the available implementations of IKBS, running on more than one hundred applications (Coelho, 1983a), allows the classification of the uses of knowledge already tackled, and suggests a taxonomy of problems and a taxonomy of solution methods. With these taxonomies it is possible to develop criteria to determine the best method for a given class of problems.

The general form of a problem statement is as follows:

Given a knowledge base KB, find a solution x which is well-formed within a system S, such that the problem conditions C are satisfied; both S and C are specified in terms of concepts that are given in the KB.

This form of statement and the types of problem-solving processes lead to the definition of a spectrum of problems, ordered by the degree to which the problem conditions directly control solution construction (Amarel, 1978).

There are three types of problem-solving processes depending on:

(1) The way in which the solution specifying system S is formulated;

(2) The nature of the problem conditions C;

(3) The degree of closeness between elements of S and the problem conditions C.

At the two ends of the spectrum we have derivation problems (e.g., finding a proof to a theorem in a formal system) and formation problems (e.g., synthesizing a program). At the middle of the spectrum we have combinatorial problems (e.g., assigning interpretations). Near the derivation problems we have planning problems (e.g., goal-directed reasoning in situations where several distinct goals must be achieved), and near the formation problems we have solution generation problems (e.g., forming programs that must satisfy a given set of input-output correspondence). Finally, interpretation problems (e.g., syntactic analysis for context-free languages) occupy different positions in the derivation-formation spectrum.

In derivation problems, conditions are given in the form of parts of a solution description, and the goal is to complete this description by using rules for solution construction from S. In formation problems, conditions are given in the form of properties that the solution as a whole must satisfy, and the goal is to generate a solution description within a language of solution structures where no choice of solution element or partial combination of solution elements can be determined directly from the given conditions.

The position of real problems in the spectrum depends on the amount of knowledge which is available about the relationships between solution structures and problem conditions. Also, the nature of this knowledge and of the tasks are issues for organizing this taxonomy.

The current IKBS involve three main uses of knowledge or problem-solving types:

(i) Diagnosis

\- interpretation

(ii) Data retrieval and organization

\- questioning

\- consultation

\- process control

(iii) Reasoning about consequences of actions – scheduling

\- management

\- process control

These uses determine how to separate/organize substructures of the domain knowledge. This last point is a central issue, because the effective use of knowledge depends on how it is organized. Also, organization depends on efficiency, focus and control in problem solving. Such interrelations suggest the need for a methodology for IKBS design, development and implementation.

## 2.3. Technology of Intelligent Knowledge-Based Systems

An IKBS specification defines the system's function in terms of its capability, task and application knowledge and procedures, and the system's implementation in terms of the software and hardware means for executing the function. Such a specification implies a broad body of technologies, some already under progress and development, others still beginning their first steps. Before attacking a new case study it is necessary to have a clear picture of the actual state of the art of knowledge engineering. In the following sections we present the main achievements and status, the central issues and the unexplored topics.

## 2.3.1. Achievements and Status

The current state of the art of IKBS technology is the outcome of work done mainly in Artificial Intelligence and Computer Science, supported by computing experience.

Artificial Intelligence has generated and tested ideas about the specific components of intelligent systems and about underlying mechanisms for knowledge representation and inference. Methods of knowledge representation (e.g., semantic networks, conceptual primitives, frames, predicate calculus), problem-solving paradigms (e.g., situation calculus, pattern-directed rule invocation) and means for characterizing processes (e.g., fuzzy logic, edge detection algorithms) were discovered. These were made available as tools to capture an expert's knowledge, and effectively use this knowledge in a complex set of computer programs.

Computer Science has provided formal tools for system building in view of the nature of datas process, control and system embodied in languages. These languages were able to characterize objects and structures of knowledge, for following local and global procedures, and for determining the behaviour of the system in parts and as a whole.

Computing experience has developed skills in system design and testing, i.e., in identifying system requirements, in translating external concepts in system code, in constructing system frameworks, and in evaluating system performance.

The work on IKBS can be organized on three ages of development, according to the state of the available technology: (1) case studies; (2) empirical observations; and (3) science. Actually, the status on how to build IKBS is still an art, and is positioned in the second age (Davis, 1982). Case studies are defined simply by testing one single dimension of a design, namely by pointing the key aspects of the design space: knowledge representation, control, system architecture and knowledge acquisition. Such a style of work allowed the settlement of a credo:

\- In knowledge lies the power;

\- The knowledge is often inexact, incomplete and ill-specified;

\- Amateurs become experts incrementally;

\- IKBS need to be flexible and transparent.

Empirical observations went a step forward by establishing the shape and character of the design space of an IKBS, i.e., which parts of the space make sense for which kinds of problems. A set of architectural principles was collected, such as:

\- Separate the inference engine from the knowledge space;

\- Use as uniform a representation as possible;

\- Exploit redundancy.

These principles work well in narrow domains of expertise. The available systems behave fragile at the boundaries of those problem domains, the knowledge representation languages are limited, and also the input/output is constrained.

Finally, the power of understanding which goes beyond the set of empirical observations it is up to science, in particular on the shape and character of the design space. Also, it is through science that we will obtain an answer to a central question:

‘Why a particular design is appropriate for a particular task?’

Therefore, the work in knowledge engineering is still in the beginning.

## 2.3.2. Central issues

In the design of an IKBS, before we devise the appropriate structure, it is important to clarify the internal and external system capabilities, by characterizing expertise in a range of behaviours. From these capabilities one may infer the central issues to work out.

As a matter of fact, the nature of expertise is associated to compiled experience and to varieties of knowledge beyond empirical associations. In general, internal capabilities for basic knowledge representation and inferential problem-solving include: classification, concept formation; summarising; abstracting; selection; retrieval; filtering; reasoning; use of heuristics; planning; modelling; learning; memorising; and explaining the results. And, external capabilities include: language analysis and production, image perceptual generation, and physical object sensing and moving.

From this extensive list of capabilities and the technical descriptions of the available IKBS we may conclude that much deeper and richer characterizations of capabilities are required that have so far been reached. Relating internal and external capabilities is a particular problem here. Some progress has been made in speech, image and object recognition, but less in speech and language, image and object understanding, Much more work is needed on the distinctive properties of task operations and on their interface with capabilities.

## 2.3.3. Unexplored Topics

There are fundamental and challenging topics to be tackled for pursuing the development of IKBS. But, the main ones remain how to choose problem areas that match the current state of the art and the elicitation of methodologies to design, build up and maintain IKBS. After two generations of IKBS, focussed solely on high performance, a third generation may deal with representation and reasoning power, tools for constructing more complex structural descriptions, techniques for using these descriptions to guide diagnosis, and causal models as a way of understanding behaviour.

High performance is a necessary, but not sufficient, aspect of usefulness. Human engineering issues are important for making the program understandable, for keeping experts interested, for making users feel comfortable. In what concerns elicitation of methodologies, several issues need to be worked out:

(1) Feasible approaches to a problem, beyond large collections of rules;

(2) Specialized and multiple representations; and

(3) Causal models as reasoning engines.

Long-term research is needed on system capabilities for knowledge representation and inferential problem-solving, and particularly on planning and learning, and on language and image understanding. Within these broad areas there are still many individual problems needing research; for example, robust parsing, plans and approximations, abstraction and hierarchies, analogies (formulating and using), temporal and spatial continuity, expectations and default knowledge (e.g., non-monotonic knowledge), forms of attention on facts and relations (e.g., context-sensitive mechanisms), propositional attitudes and modalities, large knowledge base management and rule induction. There are fundamental problems of whole system structure to be dealt with, notably the combination of hard and soft knowledge, and the coordination of distinct processes (e.g., conflicts in plans, strategies and methods). There are also problems in relating a system to its environment, specially in providing it with the ability to explain its behaviour and to monitor its performance.

The fundamental research in IKBS needs support from broader areas of processing technology (e.g., logic programming, theory of computation, data base management, program specification and parallel machines). There are also more immediate needs to be met for a practical system building (e.g., data base support for large dictionaries, good graphic display methods, mathematical data bases and cheap image processors). Tools for system building (e.g., pattern recognition on packages and plug-in natural language front end facilities) are also needed.

An analysis of the available case studies suggests a discussion on experimental methodology. Several different conceptual frameworks have been used with varying degrees of success. These systems have usually been developed as an experimental process without any guidelines. There are no scientific comparisons, as far as we know, among existing systems on efficiency and appropriateness of technologies to application domains.

A broad and open discussion on these matters is urgently required to define lines of inquiry concerned with how to make choices during a project. Such a need for a discussion is set up by some questions which clear up the relevant issues for such methodologies. As an example, we formulate some questions:

\- How does one determine the choice of the knowledge representation schema for some specific problem domain (representation vs structure; and formulation vs problem-solving performance)?

\- How does one fix a reasonable framework for encoding knowledge (approach to the acquisition of expert knowledge)?

\- What kind of design aids are needed for building expert models?

\- How does one break knowledge rules (what about exceptions)?

\- How does one verify consistency in a very large knowledge base?

\- What does the system need to know (kinds of knowledge)?

\- What does the system need to be domain-independent?

\- How should large amounts of knowledge be organized and structured (levels, layers and planes of information) to be accessed efficiently?

\- What does the deductive inference system need to be feasible and pragmatic to support an efficient search and to optimize the queries?

\- How does the system perform or use the available knowledge?

\- How does one verify and evaluate the sphere of expertise of an IKBS (content of the expert knowledge: quantity and quality of rules)?

\- How does one evaluate the performance of IKBS?

\- How does one evaluate a methodology for building up and developing IKBS?

Answers to these methodological questions may help, in the future, designers in their choice of tools, techniques and frameworks.

## 2.4. Knowledge Engineering with PROLOG

Artificial Intelligence, and knowledge engineering in particular, is characterized by the exploration of large program design spaces in which each point is itself a large and computationally intensive program. Traditional programming tools have not been adequate to meet the demands of this activity. The AI community has therefore taken a lead in developing powerful new computing techniques, such as those associated to the programming languages LISP and PROLOG. The first one has been used mainly in USA, and the second in Europe. After the choice made by the Japanese Fifth Generation Computer Systems Program in

1982, both languages are considered on equal ground terms. We favour PROLOG because it offers the significant advantages over LISP described by Coelho (1983b). For a comprehensive introduction to PROLOG see (Clocksin and Mellish, 1981).

Knowledge engineering with PROLOG is also an art because there is not a complete understanding of how to apply logic programming technology successfully to design an IKBS. The dispute around PROLOG and logic programming is over, and there is a consensus that the logical feature is necessary for knowledge engineering and for program engineering. Nevertheless, the logic programming community claims now in defense of accumulated experience not to worry about the search for a methodology in development of systems.

PROLOG has eight key problems for the intensive knowledge utilization and representation (Kurokawa, 1982):

(1) The out operator is dangerous as it destroys the equational property of a logical program (functional dependencies are better alternatives to cuts);

(2) Backtracking is not a good tool to implement non-deterministic search;

(3) Integer arithmetic operation breaks the harmony of the unification scheme;

(4) Lack of context-switching, pattern-directed process invocation and controlled pattern matching;

(5) Query optimization (a solution may be using cost functions to evaluate indexing schemes);

(6) No data abstraction support facility;

(7) Horn sets are not decidable (PROLOG is a Horn Clause theorem prover; i.e., PROLOG cannot decide whether an arbitrary query of its Horn clause logic follows from the data base or not) (Stabler and Elcock, 1983);

(8) Interface of logic programming systems with large relational data bases residing in a secondary memory.

Some of these problems motivated the proposal of new PROLOG-like logical programming languages, such as the japanese KUROLOG. However, the key problem consists in the availability of facilities to interface PROLOG to other specialized programming systems, allowing the easy assembling of modules written in different languages.

## 2.5. Stages of development

There are seven classical stages in the evolution of any IKBS intended to operate in a serve mode outside the Computer Science Community (Shortliffe et al., 1975):

(1) system design;

(2) system development;

(3) formal evaluation of performance;

(4) formal evaluation of acceptance;

(5) extended use in prototype environment;

(6) development of maintenance plans; and

(7) system relase.

But till now none IKBS has done beyond stage 3. And, in what concerns stages 1 and 2, there is no systematic way to explain how to proceed when a new case study is put forward. In general, lessons taken from other known case studies are not yet organized to support an efficient design. Accumulation of information on each case study suggests only some clues to be considered. For example, the following useful features of an IKBS may help to sophisticated a new design, but they can only be considered as design criteria:

(i) Explicating the conclusion that the system makes;

(ii) Tentative or experimental changing to a knowledge base;

(iii) Checking the knowledge base for syntactic and semantic correctness.

The four basic steps in developing an IKBS are the pragmatics of knowledge engineering. They can only be considered as advice on starting a project, on choosing system building tools or on making hardware options. Here are the basic steps:

(1) Characterizing the domain: What are the features of an intellectual task which make it more or less amenable to existing IKBS technology?

(2) Choosing a programming formalism: The programming techniques used in constructing IKBS differ markedly from those of conventional numerical and data processing. Therefore, the choice of a formalism can not come in a flash of insight. It is urgently needed a precise comparison of the various formalisms available (e.g., rules, semantic networks, frames, predicate calculus, and plans) and the facilities they provide for representing knowledge (data) and reasoning (control).

(3) Encoding an expert's knowledge: Techniques for debriefing experts; guidelines for rule base development; tools for defining and modifying knowledge bases; automated knowledge acquisition (learning) are only topics to follow up. But, the emphasis must be in explicating the knowledge, by identifying what is to be represented, rather than how to represent it. Much of the work involves identifying domain-specific concepts that are not apparent at first glance.

(4) Evaluating the system: Paradigms for comparing system performance with expert performance.

## 2.6. Architecture Principles

By reviewing the IKBS developed over the last years (Coelho, 1983a) it is possible to extract the architectural ideas and other relevant issues. This activity provides also the prescriptions for the organization of IKBS (Stefik et al., 1982).

The overall structure of an IKBS is supported by an appropriate virtual machine (Jones, 1982). In fig. 1 we sketch the most frequent structure, where the inference engine plays the role of an interpreter. In figure 2 we show the main modules of the basic architecture of an IKBS.

These figures point out the most adopted architecture paradigm, based upon the separation between the knowledge base and the inference engine. Along this paradigm, rules are the basic knowledge representation formalism, and the knowledge representation is separated from its use, i.e., it is an independent structure. This helps to decompose the knowledge base into smaller units and facilitates adding knowledge in the forms of new rules, i.e., construction and maintenance are easier. A separate and simple representation of the domain-specific knowledge is essential for successfully transferring expertise to a system. Therefore, this paradigm has two important advantages: generality and modularity, the inference mechanism containing heuristics to use knowledge efficiently for problem-solving. There are five advantages of partitioning (separation of the expert knowledge from general reasoning mechanism) and of general knowledge division into many separate rules:

![](/api/attachments/CF4M8XDY/fulltext/images/7ee181a4dfea8cfc3c5b6571439b10c663790c5fd1d077edbbb30bdf971e4aa1.jpg)  
Fig. 1. Overall structure of an IKBS

![](/api/attachments/CF4M8XDY/fulltext/images/5b1fc4fe0d9c8a65c88c26e702b685006a6de1207414e2c5d38170c5cfdc6247.jpg)  
Fig. 2. General architecture of an IKBS.

(i) Incremental development of the knowledge base over an extended time by letting the developers refine old rules and add new ones;

(ii) The same general system can be used for a variety of applications, essentially by unplugging one set of rules and plugging in another;

(iii) The same knowledge can be put to use in different ways (including teaching) by changing the rule interpreter;

(iv) The program can give simple and illuminating explanations of its behaviour merely by describing the rules it is applying (this also turns out to be a powerful way to debug faulty rules); and

(v) The possibility of developing systems that are introspective (e.g., able to check the consistency of their own rules) and evolutionary (e.g., able to modify their own rules and learn new ones).

However, the architecture principle on separability is not a general one, as some other case studies suggest, when more complex styles of reasoning are incorporated. There are at least two situations where that seems not to work out very well: large grain size of a rule (large chunks of knowledge) and sequential information.

The alternative paradigm considers overall knowledge systems, where knowledge and problem-solving are structured together. There is no separation between the knowledge base and the inference engine, and the overall system plays the role of a specialist of some type. In this paradigm, the decomposition is horizontal and along the line of problem-solving types. However, modularity is lost.

The architecture principle ‘use as uniform a representation as possible’ does not work well in some cases, when specialization is worth the cost of translation. Also, there is strong evidence to the contrary of the principle ‘keep the inference engine simple’, because it is not clear how one can maintain simplicity when allowing multiple representations.

Besides these two general paradigms, further analysis of the available IKBS suggests other organization techniques and modules. For example, agenda mechanisms permit experimentation with a wide variety of control structures. Separating subtasks into different categories permits some tasks to be avoided completely and other tasks to be ordered according to any kind of priority scheme; rule compilers greatly increase efficiency.

## 3. A Case Study

The IKBS technology has been applied to and developed within many domains of application, for example medical diagnosis and treatment, equipment diagnosis, legal decision making, electronic circuit and digital system design, business management, experiment planning in genetics, computer configuration, architecture, environment resource evaluation and geological prospecting.

The current state of the art suggests the use of the IKBS technology in the development of a workbench for information system designers. The logical complexity of some information systems which are nowadays developed and the increasing number of such systems is stressing to the limit the small resources available for information systems design.

Better mental and software information design tools are needed. The productivity of systems design teams must be improved. These are the main goals of the INFOLOG project which is described below.

## 3.1. Context: The INFOLOG Project

The main goal of the INFOLOG project is the development of mental and software tools for information systems design. The former include a suitable model for structuring information systems, a methodology for using this model and a verification logic. The latter include an interactive expert system for storing specifications and the associated validation modules. Basically, the objective is the development of a workbench for the systems analyst within a multiuser environment (for several people working on the same specification).

The proposed INFOLOG model (Sernadas, 1983a) capitalizes on the latest results on the subject, namely those presented at CRIS 1 (Olle, 1982) and the RM/T (Codd, 1979). The related work developed by the AI community on the problem of knowledge representation formalisms was also taken into account. For an illuminating comparison between the data base approach and the AI approach to information structuring see (Tsichritzis, 1981) and (Borkin, 1980).

The INFOLOG model is an integrated model of data and processes which features:

(i) Distributed logic approach: At the logical level a collection of interacting systems is recognized. No global state is assumed. Those systems may exchange information through messages.

(ii) Communication modelling: The structure of messages and the properties of the communication media and of the message supports (e.g., documents) are specified.

(iii) Data modelling: The information stored by each system is structured in a purely functional entity-oriented way. Naming problems are dealt with explicitly.

(iv) Change modelling: The atomic state transitions (events) of each system are described by pre- and postconditions.

(v) Evolution modelling: The temporal evolution of each system is governed by trigger/reaction rules. Each rule defines a process (transaction) type.

An associated methodology has been practically experimented in banking applications. An illustration is presented in (Sernadas, 1983c): the IFIP test case (011e, 1982).

The underlying logic of events is an extension of a suitable temporal logic including causal relationships (Sernadas and Sernadas, 1982; Carmo, 1983). The relevance of temporal logic to systems modelling was first recognized in (Sernadas, 1980). Since then many authors have been presenting results on the subject (Castilho et al., 1982; Mays et al., 1982).

The Systems Specification Support System (S4) is an expert system now under development around the proposed model on a C-PROLOG/UNIX \* environment. Its description is the main objective of the subsequent sections of this paper.

## 3.2. The Systems Design Workbench

The main software tool under development is the expert system for storing the information system specifications. Its knowledge base should contain at least information about the INFOLOG model itself and the INFOLOG specifications. Such a system should provide the means for:

(a) Storing and updating specifications, either incrementally or by glumps.

(b) Examining any part of the stored specification.

(c) Controlling the access to the specification.

(d) Checking each insertion/update to the specification against the INFOLOG model (e.g. the destination of a message must be a system).

(e) On request, trivial checking of the global consistency and completeness of the specification developed so far (e.g. the domain of every attribute must be defined).

(f) Examining the diagnoses produced by global checkings.

(g) Organizing printed documentation.

On a later stage it is envisaged that the system should also provide the means for:

(h) Creating emulation scenarios for the specified systems.

(i) Emulating the evolution of the specified systems, eventually using the terminals for input and output of messages.

(j) Providing decision assistance in the accomplishment of the systems specification tasks.

(k) Examining any part of the information stored in each emulated system at any time during the emulation.

Plus:

(l) On request, non-trivial checking of the global consistency and completeness of the specification developed so far (e.g., deadlock of processes and invariants).

Finally, it would be useful for the research and development effort to allow modifications to the INFOLOG model itself, that is to say:

(m) Storing and updating models (e.g., RM/T instead of INFOLOG).

(n) Storing and updating patterns of interaction with the users (which are methodology-dependent).

(o) Examining any part of the currently adopted model.

These features would turn the system into a universal tool concerning modelling. No attempt will be made in this direction in the near future.

## 4. The Systems Specification Support System (S4)

Figure 3 shows a detailed picture of the primary architectural features of S4 and its basic components.

The S4 architecture is organized into three blocks: the second one dealing with design assistance; and the third one supporting decision-making activities.

The major components of S4 are the acquisition system, the global knowledge base and the inference engine.

A user of S4 communicates with the system through a simple control driver called monitor. The monitor coordinates the management of man-machine information flow. It accepts commands from the user, interprets them, passes control to other subsystems, and returns responses to the user.

A user may perform four objectives: querying; data stockings; data validation; and requesting an explanation.

The global knowledge base (working memory) is structured into three layers: the meta knowledge base (MKB); the specifications knowledge base (SKB); and the ground knowledge base (GKB). In data base terminology, MKB corresponds to the meta schema, SKB to the schema (intensional component) and GKB to the data base contents (extensional component). The emulator module processes the contents of the GKB, and the future model acquisition module will stock the contents of the MKB.

Each of these layers is divided into two components: the data base and the rule base. Naturally, the former is increasingly more important when one goes from the MKB towards the GKB.

The acquisition system is used to create and modify the information in the GKB (system acquisition) or the information in the SKB (specifications acquisition). The second mode can be supported by two channels according to the grain size or scope of stocking:

\- An interactive editor supporting the process of acquisition step by step;

![](/api/attachments/CF4M8XDY/fulltext/images/2451c70901f5d8a60916a670a77f4319864198db6d6d3fb0d77e3431e6f605eb.jpg)  
Fig. 3. S4 architecture.

![](/api/attachments/CF4M8XDY/fulltext/images/30861f474c53530144ec4d87916ce6cd340491d3d844f9071efe14af908bbaae.jpg)  
Fig. 4. Layer organization.

\- A language translator module, allowing the full storage in one step or by glumps.

The validation module supports the maintenance of KB consistency. This validation is trivial and only syntactical, without any theorem proving.

The inference engine has the appropriate control structures to manage and search the global knowledge base.

Note that S4 differs from more conventional computer programs on account of the separation of the expert knowledge (the rules forming the global knowledge base) from the general reasoning mechanism (the rule interpreter) within the inference engine.

## 5. Modelling and Representation Issues

In the previous section, three layers were identified in the conceptual structure of the S4 Specifications Knowledge Base (SKB). Correspondingly, the entities involved in an INFOLOG specification are organized in three levels:

(i) INFOLOG model categories;

(ii) application sorts;

(iii) occurrences.

Examples of these, in the same order, are (the present paper is the INFOLOG RR07 Research Report):

category 'message sort' / message sort 'report'
/ report 'RR07'

category ‘system sort’ / system sort ‘research group’ /

/ research group 'INFOLOG'

category 'data sort' / data sort 'integer' / integer '7'

A category, much like a data type, abstracts into a class all the sorts having in common certain operators and laws defined over them (type abstraction), while a sort is viewed just as the intensional characterization of a set of occurrences (set abstraction).

In this section, a somewhat detailed description of the data base component of the SKB conceptual structure is attempted, using the INFOLOG approach. Before that, a brief overview of the INFOLOG model and methodology will be presented. Unless explicitly indicated, all statements about the model are referred to the generic sorts involved (e.g., 'systems' should be understood as 'system sorts').

The main concepts of the model will be arranged in a network schema, in terms of which a PROLOG representation may be defined.

## 5.1. The INFOLOG Approach

## 5.1.1. Basic Concepts of the INFOLOG Model

Systems, messages, events, processes and archetypes are the five most important concepts of the INFOLOG model.

## Systems

A system is a relevant entity of the real world, already in existence or to be created, which is able to process information and to communicate (with other systems).

Systems can be decomposed into subsystems, thus forming a hierarchy. A system is considered atomic (i.e., non-decomposable) if it is an actual agent of information processing and communication, having a (logically centralized) local memory associated with it. Naturally, any system keeps information about itself, about its environment (systems with which it may communicate) and also about other entities, in a (local) valuation structure. Part of that information is organized in structures called archetypes. Basically, each archetype corresponds to the information a system retains about a class of entities. Systems may have archetype-valued and data sort-valued 'attributes', known as indicators and qualities, respectively.

## Messages

Communication between (atomic) systems is done by means of information structures called messages.

Information carried by messages is structured in fields, and to each field is assigned a data sort. Any message has, at least, the source and the destination fields, which identify the respective atomic systems. It is the source-system that takes the initiative of sending the message and the destination-system has no control on the moment of its arrival. Message occurrences of the same sort have origin (or destiny) in system occurrences of the same sort.

The communication medium of a message may be noiseless, conservative and monotone, have only some of these properties or even have none.

## Events

The life of a system consists of a sequence of events (atomic state transitions) beginning with a birth event.

The discrete meaning of the word ‘sequence’ implies non-simultaneity of event occurrences. At any moment, the state of a system is the sequence of its past events: its ‘history’. This is quite different from the usual notion of ‘state’, namely that of ‘current valuation’, which is a particular combination of values in the system’s memory.

Every event sort has an associated scope which specifies what can be affected in the valuation structure of the system by occurrences of that event sort.

The emission and the reception of messages are examples of events that do not change the valuation structure of a system. That change is done by inserting, modifying and deleting archetype occurrences and by modifying general “attributes” of the system.

Valuation changing events may have references to archetypes other than those directly involved. Apart from that, any event may have scalar (data sort-valued) attributes, named details.

## Processes

An event occurrence may trigger the generation of other event occurrences. A trigger is, therefore, an event to which the system reacts by producing some events causally related to the former.

The activities of an atomic system may be decomposed into subactivities. The atomic activities are called processes. Hence, a process is an activity for which it is possible to identify (i) the trigger, and, clearly, (ii) the triggered sequence of reaction events. Most processes are triggered by message reception events, but not necessarily.

A process sort is specified by a trigger/reaction rule and each of the involved reaction event sorts are specified (as a function of the trigger) by generation equations. These equations state the attribute values of the reaction events.

The concept of process sort is close to that of transaction type, in the terminology associated to database intensive applications. However, a process sort may be implemented interactively or in a batch framework.

## Archetypes

An atomic system uses structures called surrogates to represent (and keep information about) internal and external entities, specially the systems with which it communicates.

Surrogates are just a kind of general local information structures - the previously mentioned archetypes. Other archetypes appear, during the specification activity, by combining or restricting archetypes already existent.

The other standard kinds of archetypes considered in the INFOLOG model are:

\- Particularizations, a form of restricting the set of occurrences of an archetype sort under a particular designation, through a discriminant property;

\- Generalizations, a form of grouping several archetype-sorts under a general designation;

\- Characteristics, a form of handling one-to-many relationships (in the data base terminology);

\- Relations, a form of normalizing many-to-many relationships.

To support these and other connections between archetypes, mappings called designators are used. In a sense, designators are archetype-valued 'attributes' of archetypes. Scalar (data sort-valued) 'attributes' of archetypes are known as properties.

## 5.1.2. Using the INFOLOG Model

Some basic mental tools have already been defined to support the development of an information system specification according to the INFOLOG model:

\- A methodology, indicating what should be defined, how, and under what criteria or heuristic principles;

\- A pictorial notation, including forms layouts, and diagrams to describe the communication flow; the conceptual data structures local to a system, processes causality, and archetypes life cycles;

\- A formal notation, used to express several kinds of rules about the dynamics of the information system (change rules, reduction rules, generation rules and transition rules).

It is most convenient to consider the following classification of the INFOLOG model structures:

\- Static structures

\- global (systems, messages, ...)

\- local (archetypes, properties, designators, ...)

\- Dynamic structures

\- change (events, details, references, ...)

\- behaviour (processes, generators, ...)

The global static modelling is related with communication: identification of communication agents, flow and objects (and description of the latter). The local static modelling is concerned with the memory organization of each system sort.

The change modelling regards the identification and description of events and their effect on the memory of the respective systems. Finally, the behaviour (or evolution) modelling refers mainly to the identification, description and synchronization of the activities of each system.

Methodologically, it is not advisable to develop a specification as a sequence of four distinct stages, corresponding to the above levels. However, it is reasonable to proceed in three main (but somewhat overlapping) steps of increasing detail:

(1) Preliminary analysis: decomposition of systems and local activities and identification (plus description) of messages;

(2) Local analysis: for each system sort, definition of the data and process structures, and description of the associated event sorts;

(3) Formalization of most of the identified sorts, chiefly through rules.

S4, being an information system, may and will be specified according to the INFOLOG approach. This report presents some aspects of that specification, namely the informal identification of S4 subsystems (in Section 4) and the conceptual data diagram of the S4 Specifications Knowledge Base (see next subsection).

Part of the conceptual data schema of a system sort may be pictured as a diagram, presenting the involved archetype sorts, the respective property sorts and key mappings (in case they exist), and the designators establishing the connections.

A greatly simplified notation, depicted in Fig. 5, will be used. A surrogate archetype sort is denoted by a box including its identification (say, $\alpha$ ) and the symbol 'X' (Fig. 5a). A particularization archetype sort $\beta$ of archetype sort $\alpha$ is represented as shown in Fig. 5b. Figure 5c shows the representation of a generalization (archetype sort) of $n$ archetype sorts. For characteristic or relation archetype sorts the notation is similar, except for the symbol 'G', which should be replaced by 'C' or 'R', respectively.

Two archetype sorts may also be (or have to be) connected, by:

\- a total designator (Fig. 5d: every occurrence of $\alpha_{1}$ must designate an occurrence of $\alpha_{2}$ ); or,

\- a partial designator (Fig. 5e: there may be occurrences of $\alpha_{1}$ not referring to any occurrence of $\alpha_{2}$ ).

![](/api/attachments/CF4M8XDY/fulltext/images/a4843b7692b5468442bd6a88046dfc1db3b586898eb280f31a425348042488b1.jpg)  
Fig. 5. Simplified notation for conceptual data diagrams.

## 5.2. Conceptual Schema of the Specifications Data Base

S4 is an atomic system having its memory structured into qualities, indicators, archetypes, properties and designators, as usual. These contain information namely about INFOLOG specifications and S4 users.

Specification sorts may be organized as shown in Fig. 6 and 7 \*, where the different categories of the INFOLOG model are represented as connected archetypes, according to the model itself. The diagrams involve only some of the possible connections: particularizations, generalizations, one-argument characteristics, one-argument relations and total designators. In general, the particle 'sort' is not included in the archetypes boxes, for simplification purposes.

Most of the total designators shown are self-explicit and/or refer to mapping codomains. Nevertheless, and whenever convenient to enhance clarity, an identifier is placed next to the arrow.

Concepts not introduced in subsection 5.1.1 may be found in (Sernadas and Sernadas, 1983b).

The global static structures of a system specification, depicted on top of fig. 6, may be described

as follows:

\- A system sort is either an atomic system sort or a composite one, where each component is itself a system;

\- For each message sort, two atomic system sorts (source and destination) must be indicated, besides its physical support and its communication medium (this could, alternatively, be considered as a property of the archetype 'message sort');

\- Several field sorts may correspond to each message sort, and each one has a data sort as codomain.

## 5.3. The PROLOG Representation of INFOLOG Specifications

Some solutions will now be advanced about how to implement the SKB in PROLOG. Clearly, the building blocks of the SDB schema shown in Fig. 6 and 7 will serve as the basis of much of the implementation. Every connection in those blocks is functional, hence binary. This suggests the use of a binary representation approach which indeed presents significant advantages over other representation schemes. On the other hand, any rule in the SRB (the rule base component of the SKB) will also be translated into PROLOG. This raises no difficulties since Horn clauses are a complete subset of the predicate calculus, assuming that those rules are written in such a calculus. Problems raised by temporal and modal operators are not discussed in this paper. This and other matters, namely notation and efficiency problems, will be discussed below.

![](/api/attachments/CF4M8XDY/fulltext/images/3627bb25e803470de85d880dc7b6ef2d880a883c06c6a69e066af9e5efef51f1.jpg)  
Fig. 6. Conceptual schema of the SDB (static structures).

![](/api/attachments/CF4M8XDY/fulltext/images/e5a571bedc216cc3bd1b2469539157a4c8355d7f37d57db14af61d4ee3759845.jpg)  
Fig. 7. Conceptual schema of the SDB (dynamic structures).

```javascript
"category-("<sort-id>","<category-id>)".
```

## 5.3.1. Categories, Sorts and Occurrences

The abstraction levels defined by categories, sorts and occurrences (Fig. 8) may be connected by one-to-many relationships, which we shall represent by PROLOG predicates 'sort-' and 'category-'.

For instance, the clauses

sort-(rr07, research-report).

and

category-(research-report, message).

express that 'rr07 is an occurrence of sort research-report' and that 'research-report is a sort of category message'.

In general, the declaration of specification occurrences and sorts is done according to the formats:

“sort-("<occurrence-id>","<sort-id>).”

To increase legibility and express the functional nature of predicates like the above, we include, by convention, a dash at the end of their names. The first argument of the predicate is, then, taken as the functional argument and the second argument behaves as the functional result.

The sorts and most of the occurrences of a specification have names, but they should not be used as key identifiers:

\- Different entities of the real world may have the same name;

\- Each entity may be known by different names (“synonyms”);

\- Occurrences of some sorts do not have any name (e.g. occurrences of a relation sort).

Clearly, every entity of a specification (a sort or an occurrence) present in the data base should be identifiable in an unequivocal, permanent way, by some kind of code like a data base key. Further, those keys should be generated and controlled by the system itself, being invisible to the users (Codd, 1979).

![](/api/attachments/CF4M8XDY/fulltext/images/0bd1517d7d430b353383f079086191709b8e542ff15f253b19fd5b5aca634ef3.jpg)  
Fig. 8. Abstraction levels.

Meanwhile, names could be used, in a natural and less formal way, in the communication between S4 and the users. Every query to the knowledge base would be preceded by something like a codification and would be followed by an appropriate decodification. The simplest kind of data base keys would be integers, which can be easily generated and used.

For instance, we could have the following clauses:

category-(134, message).

name(134, research-report).

name(134, rr).

sort-(209, 134).

occname(209, rr07).

## 5.3.2. PROLOG Facts and Rules

PROLOG data structures are composed of a predicate and n arguments, and these may themselves be structured. Either the predicate, or each of the arguments, may be (the identifier of) an object, an attribute or a value.

It is convenient to restrict this too much general formalism in order to enhance the expressiveness, organization and modularity of the information. These goals can be attained using binary relations (and, thus, two-argument PROLOG structures) in a systematic way.

N-ary relations can be re-expressed through binary relations. However, when compared with generalized n-ary representations, binary ones present advantages concerning:

\- Expressiveness: being less compact, the meaning of their predicates and respective arguments is more explicit;

\- Organization: they set a more uniform format for clauses;

\- Modularity: they make it easier to include new knowledge, ignore unknown information or express, intensively, general rules.

For instance (italicized names stand for the appropriate data base keys),

message(134, research-report, research-group, person).

could advantageously be rewritten to:

category-(134, message).

name (134, research-report).

source-(134, research-group).

destination-(134, person).

Nevertheless, binary representations should be regarded as a methodological basis and not as a universal formalism, since many relationships have a more natural expression through generalized n-ary relations.

For example, the components of a relation sort 'authorship' between a system surrogate 'person' and an object surrogate 'book' could be referred in the following way (italicized names stand for the appropriate data base keys):

rel2(authorship, person, book).

Occurrences of this relation sort would, then, be declared like this:

rel2-occ(401, 201, 301).

where:

sort-(401, authorship).

sort-(201, person).

sort-(301, book).

Thus, the most adequate semantic unit depends on the particular concept being represented.

Also, unary predicates can be useful for classification purposes: a unary predicate may be used to declare that some object has a certain property – for example, 'message (research-report)' or 'conservative(rr07)'. This is just the simplification of underlying binary predicates, and should be used only in a redundant way, for efficiency reasons (see below).

Legibility can be enhanced, with a minor loss of efficiency, by using infix operators (Coelho, 1983b), e.g.:

S is-successor-of N:— S is N + 1.

Here, 'is-successor-of' should be declared as an operator, while 'is' and '+' are PROLOG built-in operators.

The last clause is an example of a non-unit clause involving variables. This kind of clauses is, in particular, used to implement the rules in the MRB (the rule base component of the meta knowledge base), namely to express inheritance (deduction rules) or to validate a specification (integrity rules).

The following are examples of deduction rules:

$$
\begin{array}{c} \text {system(X): - (atomic - system(X) ;} \\ \text {composite - system(X)) .} \end{array}
$$

(something is a system as long as it is either an atomic system or a composite system);

$$
\begin{array}{c} \text { medium - occ - (Mo, X): - sort - (Mo, M), } \\ \text { medium - (M, X). } \end{array}
$$

(The communication medium X of a message occurrence Mo is the same of the respective sort M; this law could, alternatively, be used in the context of an integrity rule.)

Examples of integrity rules are:

$$
\begin{array}{l} \text {complete(message(M)): - name(M, - )}, \\ \quad \text {source - (M, - )}, \\ \quad \text {destination - (M, - )}, \\ \quad \text {medium- (M, - )}, \\ \quad \text {support - (M, - )}. \end{array}
$$

(the information about a message sort is considered, in some sense, complete, if the five indicated attributes are defined, whatever values they might have);

$$
\begin{array}{l} \text {consistent (source - occ - (Mo, So)): - sort - (Mo,M),} \\ \text {sort - (So,S),} \\ \text {source - (M,} \\ \text {S).} \end{array}
$$

(if a message occurrence Mo and an atomic system occurrence So are related by the fact that the latter is the source of the former, then, at the meta level, the same relation should be valid between the respective sorts.)

Now, it should be clear that the use of individual predicates – that is to say, grouping all the information about an object in a PROLOG structure having the object identifier as predicate – is not suitable. First, smaller semantic units are required to enhance modularity and flexibility. Second, variable predicates are not allowed, and, in particular, it would not be possible to express certain rules and facts in intensive form (Warren, 1981a).

Another class of rules is required in a decision support environment. Those are the rules related to the forecasting of attribute values in the specifications and the generation of scenarios.

As an illustration, consider that the publisher of a monthly journal wants to estimate the profit on sales, for the following quarter simply as a function of four decision (controllable) variables: cover price, investment in publicity, and the number of pages reserved for editorial or for advertising matters. Then, one could define, in the Specifications Rule Base (SRB), the relation ‘estimate’, such as:

estimate(Profit, Price, Publicity,

Editorial, Advertising):— ...

where, in the right side of the rule, averages and forecasts (by linear regression for instance) would be computed from the data recorded in the Specifications Data Base (SDB), namely considering the effects of different combinations of the values of the decision variables about past issues of the journal. Rules like the one above could be included in the Ground Rule Base (GRB) if they were modifiable by the users of the specified system. Scenarios would be derived not only by different alternative choices of the input (decision) values but also by different weighings of the factors relevant to those forecasts. With this purpose, one may take advantage of the PROLOG facility for generating different solutions for a unique query or goal.

It is also possible in PROLOG to use the arguments of some relations in a dual manner: unlike most programming languages, arguments may sometimes be either input or output ‘parameters’, depending upon which of them are instantiated. The relation ‘estimate’ could, thus, be defined such that the expenditure in publicity could also be estimated, once given the values of the remaining arguments, including the wanted profit on sales, or assuming some values by default. However, ‘optimum’ short-term decisions are usually not appropriate and, besides, they do not depend only on the behaviour of a couple of systems (in the case, the publishing company and the public). Hence, emulation of the evolution of these and other relevant systems (e.g., market competitors) during some period would be advisable.

Specification of more complex procedures by means of PROLOG rules (Horn clauses) should then be done in a highly modular way. This means that the chaining of PROLOG relations, when viewed as procedures, should be transparent, logically architectured and easily modifiable.

## 5.3.3. Efficiency Issues

Some implementations of the PROLOG language support the indexing of clauses not only by the predicate, but also by the principal functor of the first argument of the clause's head (when that term is non-variable) (Warren, 1981b). That allows a faster search of the clauses which match a goal clause, thus yielding a high degree of associativity to the data base. In that case, if there is enough memory available, manipulation times may be decreased significantly, through redundancy – namely by including, whenever convenient, predicates (and thus clauses) corresponding to the inverses of pre-existent relations in the data base.

In C-PROLOG, the version which is used in the present project, that feature of double indexing is not available. However, even with simple indexing (i.e., indexing by the predicate), we would like to access, in a more or less direct way, the attribute values associated to a data base object, once knowing an identifier of that object (a name or a data base key).

To illustrate how a simple redundant predicate could be practical in that way, consider the clause:

message(research-report).

in addition to the previously referred clause:

category-(research-report, message).

The added clause restates that 'research report is a (sort of category) message. However, the unary predicate 'message' allows a more direct access to message sorts.

To conclude, we summarize some pragmatic guidelines which may contribute for a better use of the PROLOG programming language in knowledge engineering:

\- Use PROLOG in conjunction with different knowledge representation methods in different applications;

\- Adopt, in principle, a binary representation scheme for unit clauses;

\- Include, by redundancy, the inverses of predefined predicates, whenever convenient;

\- Use PROLOG infix operators to enhance legibility, if required;

\- Capture knowledge and encode general facts through deduction rules (non-unit clauses);

\- Place unit clauses before non-unit ones;

\- Avoid more than two levels of nesting on PROLOG structures;

\- Reorder the clauses and the goals of a query, if possible, so that those easier to satisfy are first considered (thus reducing the backtracking effort);

\- Use special predicates to control the types and domains of objects and values to be inserted in the knowledge base;

\- Organize objects, domains and relations into hierarchical structures;

\- Use mode declarations, when available (constraining some predicate arguments to be only input or output);

\- Prefer the use of the meta-predicate 'bagof' rather than the similar, but less efficient, meta-predicate 'setof' (when available).

These guidelines are only a first step to build up a methodological basis for knowledge engineering with PROLOG.

## 6. Conclusion

By selecting a case study from the Information Systems (IS) problem area we intend to approach knowledge engineering (KE) taking into account two major goals:

(1) Extend the list of applications already tackled by KE methods, tools and techniques, and therefore testing and evaluating them; and

(2) Import to KE IS methodologies in order to apply them on the process of knowledge base development.

We defend that the lack of sensibility to this latter goal justifies the lack of efficiency of the IKBS development process and the variety of ad hoc procedures taken in almost existing systems.

This experimental work envisaged the definition of the KB kernel, by specifying the required knowledge for both computer-aided design and decision support tasks in a system development environment. Only static issues were dealt with so far, although it is expected that dynamic considerations may affect the structure of the KB. Moreover, the implementation of the KB in PROLOG was achieved taking into account several criteria.

Further work is needed for mapping the INFOLOG rule base into PROLOG, namely on temporal and causal rules. Another interesting line of research in the use of the proposed tools and ideas is the development of a decision support system following the solutions sketched in the design of the decision support system component of the S4.

## References

Alvey, J., A Programme for Advanced Information as Technology, Department of Industry, London (1983).

Amarel, S., Basic Themes and Problems in Current AI Research, The State University of New Jersey, Technical Report CBM-TR-91, Newark NJ (1978).

Borkin, S.A., Data Models: A Semantic Approach for Database Systems, MIT Press, Cambridge MA (1980).

Buchanan, B.G., Research on Expert Systems, Heuristic Programming Project, Report no. HPP-81-1, Stanford CA (1981).

Carmo, J., INFOLOG: Formal Semantics of the Triggering Logic, INFOLOG RR03, Fac. Ciências, Univ. Lisbon, Lisbon (1983) in press.

Castilho, J.M.V., M.A. Casanova and A.L. Furtado, A Temporal Framework for Database Specifications, Proc. 8th Int. Conf. Very Large Data Bases (1982).

Chandrasekaran, B., Towards a Taxonomy of Problem Solving, The AI Magazine, 4(1) (1983).

Clocksin, W.F. and C.S. Mellish, Programming in PROLOG, Springer-Verlag, New York (1981).

Codd, E.F., Extending the Database Relational Model to Capture More Meaning, ACM TODS 4(4) (1979) pp. 397–434.

Coelho, H., Catálogo dos Sistemas Práticos de IA, Psicologia (1983).

Coelho, H., The Art of Knowledge Engineering with PROLOG INFOLOG RR06, Fac. Ciências, Univ. Lisbon, Lisbon (1983).

Coelho, H., J.C. Cotta and L.M. Pereira, How to solve it with PROLOG, 3rd. edn, LNEC, Lisbon (1983).

Havis, R., Expert systems: Where are we? And where do we go from here? The AI Magazine 3 (1982).

Jones, K.S., Intelligent Knowledge Base Systems: Papers for the Alvey Committee, University of Cambridge, Cambridge U.K. (1982).

Kurokawa, T., A Logic Programming Language for Knowledge Utilization and Realization, Proc. PROLOG Conf., Tukuba, (1982).

Mays, E., B. Webber and A. Joshi, Temporal Logic for Competent Data Base Monitors, Proc. Logical Bases for Data Bases Workshop ONERA-CERT, Toulouse (1982).

Moto-Oka, T. et al., Challenge for Knowledge Information Processing systems, Proc. Int. Conf. Fifth Generation Computer Systems, JIPDEC, Tokyo (1981).

Newell, A., The Knowledge Level, The AI Magazine 2(2) (1981).

Olle, T.W., H.G. Sol and A. Verrijn-Stuart, eds., Information Systems Design Methodologies: A Comparative Review, North-Holland, Amsterdam, New York (1982).

Parasaye, K., Database Management, Knowledge Base Management and Expert System Development in PROLOG, Proc. Logic Programming Workshop '83, Univ. Nova de Lisboa, Lisbon (1983).

Sernadas, A., Temporal Aspects of Logical Procedure Definition, Information Systems 5(3) (1980) 167–187.

Sernadas, A., J. Carmo and C. Sernadas, Software Behaviour Specification with Triggering Logic, INFOLOG RR02, Fac. Ciências, Univ. Lisboa, Lisbon (1982).

Sernadas, A. and C. Sernadas, INFOLOG: An Integrated Model of Data and Processes, INFOLOG RR05, Fac. Ciências, Univ. Lisboa, Lisbon (1983).

Sernadas, C. and A. Sernadas, Introdução à metodologia INFOLOG, INFOLOG RR04, Fac. Ciências, Univ. Lisboa, Lisbon (1983).

Sernadas, C. and A. Sernadas, INFOLOG: the IFIP test case,

INFOLOG RR10, Fac. Ciências, Univ. Lisboa, Lisbon (1983).

Sernadas, A. and C. Sernades, Capturing Knowledge About the Organization Dynamics, IFIP Wg8.3 Conference on Knowledge Representation for Decision Support Systems, Durham, 24–26 July, 1984.

Shortliffe, E. and R. Davis, Some Considerations for the Implementation of Knowledge-Based Expert Systems, SIGART Newsletter 55 (1975) pp. 9–12.

Stabler, E.P. and E.W. Elcock, Knowledge Representation in an Efficient Deductive Inference System, Proc. Logic Programming Workshop '83, Univ. Nova de Lisboa, Lisbon (1983).

Stefik, M. et al., The Organization of Expert Systems: A Prescriptive Tutorial, Research Report VLSI-82-1, Xerox, New York (1982).

Stefik, M. and L. Connay, Towards the Principal Engineering of Knowledge, The AI Magazine, 3(3) (1982).

Tsichritzis, D.C. and F.H. Lochovsky, Data Models, Prentice-Hall, Englewood Clifss NJ (1981).

Warren, D.H.D., Higher-Order Extensions to PROLOG – Are They Needed? Dept. of Artificial Intelligence, Res. Paper No. 154, Univ. of Edinburgh, Edinburgh (1981).

Warren, D.H.D. Implementing PROLOG – Compiling Predicate Logic Programs, Vol. 1, Dept. of Artif. Intelligence, Res. Report No. 39, Univ. of Edinburgh, Edinburgh (1981).
