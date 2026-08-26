---
otero_id: 16952
otero_key: "XY2NCSB3"
title: "An investigation on the nature of decision support system software"
authors: "Michael Szu-Yuan Wang; Keh-Chiang Yu"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90099-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Investigation on the Nature of Decision Support System Software $^{1}$

Michael Szu-Yuan WANG \*

and Keh-Chiang YU \*\*

\* Institute for Information Industry, Taipei, Taiwan, Republic of China

\*\* Austin System Center, Austin, TX 78720, USA

Decision Support Systems (DSS) software is investigated and a conceptual model presented in this paper. The purpose of this model is to facilitate a better understanding of the nature of DSS software. The model is composed of six problem transformational processes linking up seven problem phases. The six transformational processes are: problem transforming system, problem mapping system, problem solving system, procedural program generation system, programming language compiling system, and code generation system. by identifying the seven problem phases this hierarchical provides a conceptual foundation for developing DSS software. Spun-off from this model is a framework for implementing knowledge-based DSS with automatic modeling capabilities. The structure of future DSS software to run on fifth generation computers is also addressed.

Keywords: Decision Support Systems, Model Management, Automatic Modeling, Knowledge Representation, Expert Systems, Formal Specifications, Canonical Forms, Knowledge Base, Program Automation, Fifth Generation Computer.

![](/api/attachments/XY2NCSB3/fulltext/images/720845ac31e92dd1e028b4ef8965c216babb765e70e2eef36e7d62f327353265.jpg)

Michael Szu-Yuan Wang is currently the Director of the Education and Training Division at the Institute for Information Industry in Taipei, Taiwan, Republic of China. Formerly, he held a faculty position during 1981–1987 at the Department of Management Science and Information Systems, The University of Texas at Austin. He received his Doctor of Business Administration in Information Systems from Texas Tech University in 1981. His present interests focus on decision support systems, strategic use of information technology, information systems management, microcomputers for managerial support, end-user computing, and office automation.

## 1. Introduction

The use of computers in modern information systems has evolved from data processing to information management, and finally decision support. The ultimate goal of an information system is to enhance the decision maker's effectiveness in using computers in decision-making processes. In the past few years, developments in the field of Decision Support Systems (DSS) have been rapid. Researchers and practitioners have presented frameworks for developing DSS, provided conceptual architectures for implementing DSS software, exploited the concept of model management, and incorporated artificial intelligence (AI) technique into DSS.

Sprague [25] has presented a conceptual model to organize decision support capabilities for developing DSS. In his conceptual model, the decision making system is the overall system consisting of a DSS and a manager/user who uses the DSS to confront a task in an organizational environment. The DSS consists of a data base, a model base, and a complex software system for linking the user to each of them. The DSS software system must have a set of capabilities which facilitates quick and easy configuration of a specific DSS and modification of the DSS in response to changes in the manager's requirements, environment, tasks, and cognitive approaches. It is comprised of three components: data base management software (DBMS), model base management software (MBMS), and the software for managing the interface between the user and the system,

![](/api/attachments/XY2NCSB3/fulltext/images/c643d7e2728a11772b8de3cdece76d9f0041a98adbd5c2a10726dd75bdb9be0b.jpg)

knowledge-based systems and automatic model formulation.

![](/api/attachments/XY2NCSB3/fulltext/images/9c8c79f5a239e70be844ca74d6601a5436eb97dd7c232cd92b6ec68b33458477.jpg)  
Fig. 1. The Operational Environment of a Junction Support System [27].

which he calls the dialogue generation and management software (DGMS). He identifies three types of systems designated as DSS: specific DSS, DSS generators and DSS tools. He views a specific DSS as a hardware/software system that allows a decision maker to deal with a specific set of related problems; a DSS generator as a 'package' of related hardware and software which provides a set of capabilities to quickly and easily build a specific DSS; and a DSS tool as a hardware or software element which facilitates the development of a specific DSS or a DSS generator.

Fig. 2.
A Hierarchical Model for Decision Support System Software.  
![](/api/attachments/XY2NCSB3/fulltext/images/19d82aa1d9f258e3cae531ce53e68a341e83b74b95417d27e7992bf78610c40d.jpg)

Wang and Courtney [27] have enhanced Sprague's framework for DSS and provided a description of the operational environment of Decision Support Systems. The operational environment of a DSS is a composed of a Decision Making System (DMS), a Decision Support System and DSS software. Fig. 1 exhibits the relationships among DMS, DSS, and DSS software. The inner box is the DSS software; the middle box is the DSS; and the outer box is the DMS.

Wang and Courtney [27,29] have also provided a conceptual architecture for implementing generalized DSS software. Their DSS software architecture exploits the concept of 'macro' to extend the conventional meaning of 'model' in a DSS environment. It delivers a notion of three-level hierarchy of knowledge bases to share corporate knowledge (macros and data) and improve communications among organizational units. They suggest the use of the relational data model for interfacing the models and their data. Wang [28] also demonstrates how models can be formulated through relational data operation.

Bonczek et al. [9] provide a generic description of DSS, which views a decision support system as having three principal components: a language system, a knowledge system and a problem processing system. The language system is referred to as the sum total of all linguistic facilities made available to the decision maker by a decision support system. A language system may encompass either retrieval languages or computational languages, or both. A knowledge system is referred to as a decision support system's body of knowledge about a problem domain. The knowledge is expressed, according to a set of rules of the knowledge representation method, for purposes of retention within the decision support system. The mediating mechanism between expressions of knowledge in the knowledge system and expressions of problems in the language system is referred to as the problem processor or the problem-processing system.

Elam et al. [4] expand the concept of model management, previously introduced by Will [32]. They view a model management system as a system that dynamically constructs a decision aid in response to a particular problem. The process is accomplished by drawing on a knowledge base of models that reflect the technical expertise of a management scientist and the organizational experience with the activities involved in a given decision making environment. The knowledge can be diffused throughout the decision making environment and adapted as necessary to support a decision maker in structuring as well as analyzing a problem. The model management system can be characterized by knowledge representations, diffusions of knowledge, and adaptations of the knowledge in solving problems.

Konsynski and Dolk [18] propose the use of knowledge abstractions as a robust model representation form. The knowledge abstraction approach is a hybrid form, drawing on characteristics of predicate calculus, semantic networks and frame representation. A knowledge abstraction contains three basic components: data objects, operations and procedures, and assertions about the interaction of data and procedures. The assertions of specification is a knowledge base containing the relevant internal/external relations. They entail the description of a model as a data abstraction consisting of equations, elements, and solution procedures. Each of the model components is maintained in a model base and is characterized in the global directories.

Blanning [6] proposes a relational framework for model management in DSS. The framework stemming from the theory of relational data model provides a foundation for logical interface between the users of a model management system and the models themselves. In the framework a decision model is viewed as a properly restricted subset of the Cartesian cross product of its inputs and its outputs. His research provides a direction leading to a synthesis of data management and model management in a single relational framework. Such a synthesis may allow for more flexible and convenient support of decision processes.

Blanning [5] has done a survey on knowledge-based expert systems for managers (ESM). He identifies four areas in which ESM have been developed: (1) resource allocation, (2) problem diagnosis, (3) scheduling and assignment, and (4) information management. In each area, he briefs some extant systems in terms of their knowledge schemes, inference methods, acquisition strategies, validation procedures, and user interfaces.

Hwang [16] examines human decision making and model building from the points of view of MS/OR, DSS, and AI. He observes that the model building processes of AI and MS/OR/DSS are essentially the same, viewing, as they do, the knowledge base as a descriptive model of the expert's way of solving problems. He also surveys research related to automatic model building and concludes that most of the research work shows good ideas but narrow and primitive results; that there is a lack of guiding theory, and that most of the systems were implemented on a trial-and-error basis.

All of the prior work calls for a clearer understanding on the nature of DSS software. For this purpose, a hierarchical model of DSS software is presented below.

## 2. A Hierarchical Model for Decision Support System Software

As mentioned earlier, a decision support system is a man-machine system configured upon the DSS software to facilitate the activities of the decision-making system. The success of the DSS is greatly dependent on the 'smartness' and 'power' of DSS software. To fully understand the nature of DSS software, an architectural view is needed. Fig. 2 presents the authors' hierarchical model for DSS software. The hierarchical model encompasses six transformational processes (or systems) linking seven phases of problem status. Through the six transformational processes, the solution of the problem stated in natural language is yielded. Although the six transformational systems are discussed here in an 'interpretive' approach it should be noted that the actual implementation can adopt the 'compiling' approach, which means two or more contiguous transformational processes can be merged into one 'macro' process for purposes of efficiency.

## 2.1. Problem Transforming System

Current computer usage has been significantly hampered by computer oriented man-machine interfaces in that DSS users expect to state their problems directly in daily languages, without the aid of programming languages or programmers, while computers will solve the problems with good responsiveness [2]. Natural language thus represents a logical progression in this trend towards people-oriented man-computer interfaces. Computerized processing of natural language represents the ultimate in accommodating a user population; it would open the door to a wide range of computer services which are currently not viable [23]. However, a capacity to process natural language would not and should not replace technical programming languages where they are appropriate.

Noam Chomsky, a leading American linguist, concluded that the learning and understanding of natural languages was too complex to be handled by computer systems and must rely on an inherited ability unique to humans. Many researchers also recommended abandoning further attempts to have computers understand natural languages in a totally unstructured way. Instead, attention was focused on context-dependent natural language communications [22]. The related research on natural languages has long formed an important field in artificial intelligence.

One indispensable factor of well-responsive DSS is the interaction between DSS software and the user. The user provides the problem transforming system, which is the interface between untrained users and the decision support system, with his problem description through context-dependent natural language statements. Using the 'knowledge' of the application area, the system then disambiguates and interprets the problem statements, and transforms them into precise formal specifications for the problem. The system may initiate questions to prompt the user to supply additionally needed information or missing information. Similarly, the user may inquire of the system as to the progress of the interaction.

Many systems have been designed to meet the user halfway by asking pointed questions or by offering alternatives to the user which can then be selected. This approach requires less typing at the terminal, and less preorganization of thoughts; thus, not only does the approach better accommodate and navigate naive users, it also allows many software modules to be preconstructed and stored in the system to improve the efficiency.

In brief, the problem transforming system converts a problem representation (problem statements in context-dependent natural language) into another representation (problem descriptions in domain-specific formal specifications). In other words, it only transforms a ‘what’ into another ‘what’ which will further be processed by the problem mapping system.

## 2.2. Problem Mapping System

Input to the problem mapping system is domain-specific formal specifications, which are a precise description, without language ambiguity, of what the configured DSS is intended to do. A specification is formal if it is expressed entirely in a language with explicitly and precisely defined syntax and semantics, e.g., first order predicate calculus or a programming language. The formal specifications can also be used by trained application programmers as direct input of a DSS software without natural language interface.

The problem mapping system uses the ‘knowledge’ of the application area to analyze the problem specifications and to structure the problem into a group of internal canonical frames aggregatively abstracting the same problem. Only these canonical forms are recognized by the problem solving system. The main advantage of using canonical forms is to allow the problem solving system to be implemented cleanly and efficiently without regard to specific applications for which it may be used.

in short, the problem mapping system converts an external problem representation (problem structures in domain-specific formal specifications) into an internal representation (problem descriptions in domain-specific canonical forms). So, the internal representation is still a 'what' form which will be solved by the problem solving system in an understood methodology.

## 2.3. Problem Solving System

The problem solving system accepts problem structures in canonical forms, subjects them to analysis, and uses knowledge about the application domain to generate a non-procedural solution of the problem. The notion of canonical form input is a powerful technique for constructing DSS problem solving systems. It can keep irrelevant knowledge from being accessed and allow canonical frames interact with each other in precisely specified ways. The problem space with which the problem solver must contend is greatly reduced and problem solving mechanisms can be cleanly and efficiently implemented [21].

The non-procedural problem solution is generated by the problem solving system through invoking specialist procedures associated with canonical frames. Since it specifies a task in terms of its behavior independently of any specific way accomplishing the task, this solution is a set of nonprocedural ‘how-specifications’. At this stage, the problem has actually been solved because the conversion from ‘what’ into ‘how’ is achieved. This transformation (from ‘what’ into ‘how’) is the technical core of DSS.

## 2.4. Procedural Program Generation System

The non-procedural how-specifications generated by the problem solving system can be typified by Very High Level Language (VHLL), which supports a 'very high level' form of behavior by primitive (as opposed to programmer-defined) types [31]. It enables the programmer to code problem solving programs in a less procedural fashion and allows him to omit many details that conventional programming languages demand of him. A well-known general-purpose VHLL is APL which has elaborate aggregate operations on arrays. Also, examples of special-purpose VHLL include GPSS and SIMULA.

Similarly, model commands used to control the invocation of models in a model-based system also represent a non-procedural problem solution. Each model command invokes a model to execute a sequence of procedural steps. Since they are concerned with specifying what is to be retrieved from a data base independently of how the object to be retrieved are represented in the data base, non-procedural relational data base query languages may be regarded as VHLL which support abstract accessing behavior for data bases.

Briefly speaking, the procedural program generation system converts the non-procedural problem solution into instructions of a procedural programming language ready for compilation and execution. For a fully understood application (e.g., VHLL and data base query languages), this transformation (from 'how-specification' to 'do-implementation') can be a mechanical process and hidden in a lower level conceptual blackbox.

## 2.5. Programming Language Compiling System

The study of programming language compiling systems and code generation systems belongs to the field of computer sciences; These systems can be viewed as blackboxes by DSS implementors. The compilation process is partitioned into five primary subprocesses by Aho and Ullman [1]. In our hierarchical model, the programming language compiling system is defined to perform the first four of the five subprocesses proposed by Aho and Ullman. They are lexical analyzing, syntax analyzing, intermediate code generation and intermediate code optimization.

The lexical analyzer separates characters of the source language into groups that logically belong together; these groups are called tokens. The output of the lexical analyzer consists of a stream of tokens which is passed to the next subprocessor, the syntax analyzer or parser. The syntax analyzer groups tokens together into syntactic structures (e.g., expressions or statements) which are often regarded as trees whose leaves are tokens. The intermediate code generator uses the structure produced by the syntax analyzer to create a stream of simple instructions called intermediate code. These instructions are similar to assembly macros. The primary difference is that the intermediate code need not specify the machine registers to be used for each operation. The intermediate code optimization is an optional subprocess designed to improve the efficiency of the intermediate code. It generates an output of another intermediate code program that does the same job as the original, but the object code produced from the optimized intermediate code perhaps runs faster and/or takes less memory space.

In brief, the programming language compiling system converts a program into the register-free intermediate code with some degree of portability.

## 2.6. Code Generation System

The code generation system in our model is defined to perform the fifth and last subprocess of Aho and Ullman's compilation processor - code generation. It converts intermediate code into a sequence of machine instructions by deciding on the memory locations for data, selecting code to access each datum, and selecting the registers in which each computation is to be done. Many computers have only a few high-speed registers in which computations can be performed particularly quickly. A good code generator would therefore attempt to utilize these registers as efficiently as possible to avoid redundant loads and stores of data between registers and the memory. This aspect of code generation, called register allocation, is particularly difficult to do optimally, but some heuristic approaches can give reasonably good results [1]. Generally speaking, designing a code generator that produces truly efficient object programs is one of the most difficult part of compiler design, both practically and theoretically.

## 3. Program Automation and the Hierarchical Model

The spectrum of programming systems is conventionally known to programmers in terms of the following categories, ranging from the most intelligent to least intelligent: automatic programmer, special purpose language translators, customizers, macro processors, and set of fixed modules [11]. In the following, we will show the generality of our hierarchical model which covers all of these categories.

The automatic programmer ‘permits a user to specify his problem in very high level, nonprogrammer user terms and to have the computer determine how to accomplish the tasks and then automatically generate the corresponding procedural programs to accomplish those tasks’. It actually performs the functions from problem mapping through procedural program generation as in our hierarchical model. The ‘automatic programmer’ (or the intelligent problem processor in the DSS context) is the aim of research on DSS software development. It is an ideal processor that understands user problems (in ‘what-to-do’ type of specifications), formulates models, extracts needed data and generates appropriate code. The generated code can then be executed to yield the solution to the problem.

Special purpose language translators only perform the procedural program generation function in our model. There are usually designed for a specialized discipline or a specific technology, or for narrow applications used across various disciplines. The output generated is a custom program coded in a general purpose language.

For customizers, canonical frames describing the target problem and corresponding problem solving mechanisms are pre-constructed and stored in the system. The system inputs 'formatted' specifications and accordingly decides which stored solvable problem type the target problem matches. Because the solving mechanism for each problem type is pre-decided, the corresponding code can be written and stored in advance. The primary function of program generation system is simplified to reproducing most of the stored code with required changes. Its degree of automation is lower than that of a special-purpose language translator because the latter uses less of canned code and generates more custom code. Apparently, customizers have limited flexibility and can only be applied to prescribed problems. Although customizers have more 'problem-oriented' knowledge than the programming language compiling system in our model, they are not as general as any programming language.

Both the macro processor and subroutine calling facility use canned code. They are very low-level program automation tools and are normally used as subroutine components in the programming language compiling system.

## 4. A Hierarchical Skeleton of Knowledge-based Decision Support System Software

Bonczek et al. [8]. point out that model usage within a DSS can be broadly classified as falling into one of the following categories:

(1) the DSS user gives a procedural specification of how the model is constructed,

(2) the DSS user gives a predefined model by name, or

(3) the DSS user states what data are desired and the DSS formulates a model(s) that can satisfy the request.

Although category 1 involves a relatively low-level language which requires procedural description, it does afford considerable flexibility in terms of the models that can be specified. The second category is nonprocedural, but has limited flexibility. The user does not need to indicate how a model is constructed, but merely names one of the group of available models. Each of these models was predefined during the design of the DSS.

Present-day decision support systems fall into the first two categories [9]. The third category involves system-formulated models. User needs are stated in a non-procedural manner. The degree of modeling offered by such a DSS is a function of model building knowledge available to the DSS. The manner in which application-dependent knowledge is incorporated into a DSS will determine whether that DSS can deal with only one problem domain or whether it is capable of being used in many problem domains.

Over the last ten years, the most significant and meaningful accomplishment in artificial intelligence of computer sciences has been the strong success of knowledge-based expert systems [15]. Expert systems have been developed for a number of different problem domains. Successful examples are medical consulting, molecular structures, oil and mineral exploration, computer configuration, and electrical circuits, etc. [20]. These systems fit the third category but are not the customary kinds of systems encountered in business applications [9]. It is of interest to speculate about why systems like those are not found in business settings. The ideas and features of such systems certainly look attractive, but in viewing current management systems there is nothing at this level. Applying the tools and technologies developed by these efforts in building and implementing decision support systems to fit the third category is a promising new direction for DSS research [13].

In this section, a hierarchical skeleton for implementing knowledge based automatic modeling DSS will be presented (see fig. 3). From the view of problem evolutionary process, this skeleton is a special implementation of the previously presented hierarchical model for general DSS software. This skeleton highlights the layered structure for implementing a special kind of DSS software – the one with automatic modeling capabilities. The top four systems presented in this skeleton correspond to the top four systems of the previous model. The bottom two systems in the previously described basic model are applicable to this skeleton without change. Therefore, the discussion of them is omitted.

Fig. 3.
A Hierarchical Skeleton of Knowledge-Based Decision Support System Software.

Problem Statements in Context-Dependent Natural Language
↓
PROBLEM TRANSFORMING SYSTEM
↓
Problem Descriptions in Domain-Specific Formal Specifications
↓
APPLICATION-DEPENDENT MODEL FORMULATING SYSTEM
↓
System-Formulated Problem Models
↓
GENERAL MODEL SOLVING SYSTEM
↓
Fundamental Activities of General Models
↓
PROCEDURAL ROUTINE GENERATION SYSTEM
↓
Procedural Routines and Instructions
↓
PROGRAMMING LANGUAGE COMPILING SYSTEM
↓
Register-Free Intermediate Code
↓
CODE GENERATION SYSTEM
↓
Executable Machine-Dependent Code

## 4.1. Problem Transforming System

This system is similar to the first system of the authors' previous model. The system uses knowledge of the application area to disambiguate and interpret the problem statements and to transform them into precise formal specifications for the problem. Because basic model types and methods are already known to the system, rather than being a complete operational specification, the formal specification can be greatly simplified and well-organized. The effort for defining specifications can be significantly reduced [3].

## 4.2. Application-Dependent Model Formulating System

The application-dependent model formulating system uses modeling knowledge to analyze the user's problem (in formal) specifications) and to generate the corresponding model for the problem, which will be solved by the next system – general model solving system.

The existence of a pool of general models serves as the starting point for the incorporation of modeling capabilities into a DSS. General models, also called modules or model building blocks, are models that can be applied either on a stand-alone basis or in tandem with other general models to form a more comprehensive model. For example, several general models can be integrated into a problem model to solve a problem; several problem models can be integrated into a functional model to serve a functional area; several functional models can be integrated into a corporate model for corporate planning, etc.

The application-specific modeling knowledge must be separated from general model solving system in order for the general model solving system to be flexible. The modeling knowledge means the required information for forming the comprehensive model and handling the mechanics of inter-model linkage. The system-formulated problem model is a conceptualized 'what' form, which means 'what to do' has been derived from 'what the problem is'.

## 4.3. General Model Solving System

The general model solving system solves the related modules and links their results together.

This system should be devised in such a way that its code does not need to change in order to support decision makers in various application areas $[8]$ . The general model solving system should also be invariant to changes in the modeling knowledge within a specific application area.

The general model solving system must have knowledge about how modules are tied together to solve a problem model in a DSS (e.g., module types and assumptions, data requirements, interrelationships between modules and data, etc.) [8]. Data base utilization by models should be accomplished automatically.

In brief, the general model solving system analyzes the user's problem model and relates it to fundamental activities of general models. The task of how to utilize the existent general models to solve the user's problem model has been accomplished.

## 4.4. Procedural Routine Generation System

The fundamental activities produced by the general model solving system are carried out by the procedural routine generation system. This system accesses a library that contains all shared basic routines (e.g., matrix manipulation functions or data query functions). These routines are shared by all modules in a standardized way. In essence, the system performs similar functions to those by procedural program generation system in the previous section.

## 5. Implication of Fifth-Generation Computers on the Structure of Decision Support System Software

The principal application area for computer systems in the 1990's is predicated by the Japanese to be that of knowledge-based expert systems. Fifth-generation computer systems are to utilize 'knowledge bases' as the foundation of processing, beginning with inputs from the human system such as speech, natural language, pictures, or images, and extending to the comprehension of these inputs, synthesis and execution of programs around them, and generation of responses. These knowledge bases are to include knowledge of languages, images, and problem domains, as well as knowledge about the mechanisms and data expressions of the machine system. Some of the areas (identified by preliminary investigation [19]) that are likely to undergo significant changes because of the advent of fifth-generation computers are, systems for decision support, office automation, computer-aided engineering, and intelligent robots. This section investigates the problem evolutionary processes of decision support systems on fifth-generation computers – from problem statements in natural languages to final solutions of the problem.

All applications on fifth-generation computers are to be composed of interactive, processing and management systems, however, these three systems will differ proportionally from application to application. The interactive system interfaces with the user and directs the intelligent interface subsystem and the problem extraction subsystem to transform the original problem description to a ready-for-solving internal state. The processing system directs applied problem solving subsystems to generate non-procedural problem solutions. The management system acts like a knowledge manager and provides or stores all knowledge the interactive and processing systems use. The hierarchical model for DSS software on fifth-generation computers is presented in fig. 4.

## 5.1. Intelligent Interface Subsystem

The intelligent interface subsystem is used to support conversations with the computer. Such conversations are to be in the form of speech, graphics, natural languages, etc. – possibilities aimed at enabling the exchange of information in a form natural to humans.

The DSS user provides the problem description through natural language statements. The intelligent interface subsystem utilizes the knowledge inherent in languages to analyze the statements and converts them into an intermediate expression. This subsystem only serves as the language interface to DSS users. Its primary task is to disambiguate and interpret the problem statements and generate a structure composed of key terms. Only this structure (intermediate expression) can be analyzed by problem extraction subsystem for further processing. This subsystem is also responsible for converting the summarized answer into an external expression understandable to DSS users.

Fig. 4.
A Hierarchical Model for Decision Support System Software on Fifth-Generation Computers.

Problem Statements in Context-Dependent Natural Language
↓
INTELLIGENT INTERFACE SUBSYSTEM
↓
Intermediate Expression of the Problem
↓
PROBLEM EXTRACTION SUBSYSTEM
↓
Internal Problem Description
↓
APPLIED PROBLEM SOLVING SUBSYSTEM
↓
Non-Procedural Predicate Logic Solution

The human-computer natural language communication is context-dependent. The knowledge required for the communication is stored in a context-dependent knowledge base. The system is permitted to query the user for further information in order to clarify what it recognizes as ambiguity in the user's initial statements. Similarly, the user may inquire of the system as to the progress of the interaction.

In brief, the intelligent interface subsystem only converts a problem representation (problem statements in natural languages) into another representation (intermediate expression of the problem). It just generates a new 'form' of the problem that will easily be understood at the next stage.

## 5.2. Problem Extraction Subsystem

The problem extraction subsystem analyzes the intermediate expression in context and extracts from it an internal description of the problem. In other words, this subsystem tries to use knowledge about the application domain and understand the problem in essence, but not in form. The internal description is a ready-for-solve state which will be processed by the applied problem solving subsystem in the next stage.

## 5.3. Applied Problem Solving Subsystem

The applied problem solving subsystem receives the target representation of the problem (internal problem description) and uses its knowledge about the problem domains to generate the solution of the problem. This solution is a program of non-procedural predicate logic statements. In a predicate logic language, a program is a collection of logic statements of a restricted form (clauses) causing the execution of such a program to be a suitably controlled logical deduction from the clauses forming the program.

In fifth-generation computers, this kind of very high level language will be adopted as the kernel language directly supported by the hardware. Other languages, such as inquiry languages from knowledge bases and a knowledge representation language, will be implemented in terms of the kernel language, which may be seen as the machine language of the fifth-generation computer system.

Knowledge-based expert systems – programs that exploit special knowledge to solve difficult problems in specialized areas – are a key fifth-generation product. These expert systems embody modules of organized knowledge which support sophisticated problem solving and inference functions for the purpose of rendering the user intelligent solutions in specialized areas. Non-procedural logic programming languages are viewed by the Japanese as the most suitable languages for implementing expert systems.

In brief, non-procedural problem solutions are produced by the applied problem solving subsystem in the form of predicate logic statements. A predicate logic language statement corresponds to an entire subroutine in a conventional programming language.

## 6. Conclusion

Rather than focusing on the architecture of DSS software, the focus of this paper is to provide a conceptual framework to develop DSS software which has the ‘intelligence’ to guide decision makers in the creative use of DSS. Our hierarchical view illustrates the process from how a problem is stated through how the results are obtained. Six transformational processes are introduced to link the seven phases of problem status.

The problem transforming system transforms a problem represented in a context-dependent natural language into a problem description in domain-specific formal specifications. The problem mapping system converts the formal specifications into domain-specific canonical forms which will then be processed by the problem solving system using pre-specified methodology. The problem solving system generates a non-procedural solution by invoking specialist procedures associated with canonical frames. When the non-procedural 'how-specification' solution is yielded, the problem is solved. The subsequent three processors – the procedural program generation system, programming language compiling system, and code generation system – can then be invoked to mechanically convert the non-procedural problem solutions into procedural programming language instructions, register-free machine-independent intermediate code and machine-dependent executable code. Finally the execution takes place to generate the results.

At the present time, most DSS software exists in the form of ‘procedural program generation systems’, which provides non-procedural modeling languages. Researchers and the DSS software industry have been studying the different problem evolutionary processes from original problem statements to final solutions. The hierarchical view of DSS software, presented in this paper, highlights the hierarchy of the evolutionary processes and provides a foundation for incremental implementation of DSS software. The incremental development of DSS software will proceed from the procedural program generation system, through the problem solving system and the problem mapping system, to problem transforming system. At each stage of development, a front-end system can be added-on to upgrade the user-system interface. As the evolution continues, the users of the DSS software will be allowed to state problems in less specific forms (shifting from ‘how-to-do’ to ‘what-to-do’).

The knowledge-based DSS software skeleton with automatic modeling capabilities is a special structure of our basic hierarchical model for DSS software. Because the special structure is for automatic model formulation and utilization, a special, important design issue is the selection of the knowledge representation and manipulation scheme that is best suited to the problem domain being considered. Predicate calculus [8], structured inheritance network [13] and hybrid forms [18] are suggested by different researchers. It is yet to be investigated as to which one is the best representation scheme for most business applications.

The design of knowledge-based DSS that simulate expert human modeling capabilities has been a new direction for DSS software development. The hierarchical skeleton presented in this study designates the layered structure of such implementation. To exhibit the power of such systems, modeling knowledge and model solving knowledge must be efficiently manipulated. Resorting to artificial intelligence technologies and tools seems to be a very promising approach. Yu [34] has developed a more specific framework for knowledge-based automatic modeling systems. Based on the framework, he has also implemented a knowledge-based automatic network modeling system for Production, Distribution, Inventory (PDI) problems.

The Japanese believe that the future belongs to expert systems and that conventional computers seem unable to satisfy the performance demands of applications such as knowledge-based expert systems. 'Fifth-generation computer systems will be knowledge-information processing systems based on innovative theories and techniques that can offer the advanced functions expected to be required in the 1990's, overcoming the technical limitations inherent in conventional computers' [19].

Based on the technology proposed for fifth-generation computers, decision support systems can be constructed like building ‘knowledge’ blocks, with each block possessing some knowledge for performing its task. A configuration of knowledge blocks forms a functioning DSS. In turn, functioning DSS’s can be used as building blocks for larger systems. In this way, the ‘DSS machine’ will be as accessible as today’s computer packages.

## References

[1] A.V. Aho and J.D. Ullman, Principles of Compiler Design (Addison-WEsley, Reading, MA, 1977).

[2] S.L. Alter, Why Is Man-Computer Interaction Important for Decision Support Systems, Interfaces 7, Nr. 2 (1977) 109–115.

[3] R. Balzer, An Alternative Approach to Software Automation, in: P. Wegner, ed., Research Directions in Software Technology (MIT Press, Cambridge, MA, 1979) 424–489.

[4] M. Binbasioglu, and M. Jarke, Domain-Specific DSS Tools for Knowledge-Based Model Building, Proceedings of the Nineteenth Hawaii International Conference on System Sciences (1986) 503–514.

[5] R.W. Blanning, Expert System for Management: Possible Application Areas, Transactions of the Fourth International Conference on Decision Support Systems (DSS-84) (April, 1984) 69–77.

[6] R.W. Blanning, A Relational Framework for Model Management in Decision Support Systems, Transactions of the Second International Conference on Decision Support System (DSS-82) (June, 1982) 16–28.

[7] R.W. Blanning, Model Structure and User Interface in Decision Support Systems, Transactions of the First International Conference on Decision Support System (DSS-81) (June, 1981) 1–7.

[8] R.H. Bonczek, C.W. Holsapple, and A.B. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management, Operations Research 29, Nr. 2 (1981) 263–281.

[9] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Future Directions for Developing Decision Support Systems, Decision Sciences 11, Nr. 4 (1980) 616–631.

[10] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, The Evolving Roles of Models in Decision Support Systems, Decision Sciences 11, Nr. 2 (1980) 337–356.

[11] A.F. Cardenas, Technology for Automatic Generation of Applications Programs - A Pragmatic View, MIS Quarterly 1, Nr. 3 (Sept., 1977) 49–71.

[12] R.O. Duda and J.G. Gaschnig, Knowledge-Based Expert System Come of Age, Byte 6, Nr. 9 (Sept., 1981) 238–281.

[13] J.J. Elam and J.C. Herderson, Knowledge Engineering Concepts for Decision Support System Design and Implementation, Proceedings of the Fourteenth Hawaii International Conference on System Sciences (Jan., 1981) 639–643.

[14] J.J. Elam, J.C. Henderson and L.W., Miller Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of the First International Conference on Information Systems (Dec., 1980) 98–110.

[15] E. Feigenbaum, The Art of Artificial Intelligence: Themes and Case Studies of Knowledge Engineering, Proceedings of the Fifth IJCAI (1977) 1014–1029.

[16] S. Hwang, Automatic Model Building Systems: A Survey, Transactions of the Fifth International Conference on Decision Support Systems (DSS-85) (1985) 22–32.

[17] P. Kinnucan, Artificial Intelligence: Making Computer Smarter, High Technology (1982) 60–70.

[18] B. Konsynski and D. Dolk, Knowledge Abstractions in Model Management, Transactions of the Second International Conference on Decision Support Systems (DSS-82) (June, 1982) 187–202.

[19] T. Moto-Oka et al., Challenge for Knowledge Information Systems, Proceedings of International Conference on Fifth-Generation Computer System (Oct., 1981).

[20] D.S. Nau, Expert Computer Systems, Computer, IEEE (Feb., 1983) 63–85.

[21] G.S. Novak, Representations of Knowledge in a Program for Solving Physics Problems, Proceeding of the Fifth International Joint Conference on Artificial Intelligence (Aug., 1977) 286–291.

[22] M. Peltu, Artificial Intelligence – Key to the Fifth Generation, Datamation (Jan., 1982) 114–115.

[23] R.C. Schank and W. Lehnert, Review of Natural Lan-

guage Processing, in: P. Wegner, ed., Research Directions in Software Technology (MIT Press, Cambridge, MA, 1979) 750–766.

[24] R.H. Sprague, Jr. and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, NJ, 1982).

[25] R.H. Sprague, Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly 4, Nr. 4 (Dec., 1980) 1–26.

[26] P.C. Treleaven and I.G. Lima, Japan's Fifth-Generation Computer Systems, Computer, IEEE (Aug., 1982) 79–88.

[27] M.S.Y. Wang and J.F. Courtney, A Conceptual Architecture for Generalized Decision Support System Software, IEEE Transactions on Systems, Man and Cybernetics 14, Nr. 5 (Sept., 1984) 701–711.

[28] M.S.Y. Wang, Bridging the Gap between Modeling and Data Handling in a Decision Support System Generator, International Journal on Policy and Information 7, Nr. 2 (Dec., 1983) 87–93.

[29] M.S.Y. Wang and J.F. Courtney, Design and Implementa-

tion of the MAGIC/ROC Decision Support System Generator, Transactions of the Second International Conference on Decision Support Systems (DSS-82) (June, 1982) 37–49.

[30] A.I. Wasserman and S. Gutz, The Future of Programming, Communication of ACM 25, Nr. 3 (March, 1982) 196–206.

[31] P. Wegner, Programming Languages - Concepts and Research Directions, in: P. Wegner, ed., Research Directions in Software Technology (MIT Press, Cambridge, MA, 1979) 424-489.

[32] H.J. Will, Model Management Systems, in: E. Grochla, N. Szyperski, and W. de Gruyter, Eds., Information Systems and Organization Structure (Berlin, 1975).

[33] W.A. Wulf, Trends in the Design and Implementation of Programming Languages, Computer, IEEE (Jan., 1980) 14–24.

[34] K.C. Yu, Knowledge-Based Automatic Network Modeling, Unpublished dissertation, The University of Texas at Austin (1987).
