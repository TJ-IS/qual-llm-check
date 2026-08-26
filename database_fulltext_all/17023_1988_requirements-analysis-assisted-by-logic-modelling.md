---
otero_id: 17023
otero_key: "CACQCQQD"
title: "Requirements analysis assisted by logic modelling"
authors: "Peter C. Scott"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90095-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Requirements Analysis Assisted by Logic Modelling

Peter C. SCOTT

RCA Government Communications Systems Division, Camden, NJ 08102, USA

Natural-language documents which express the requirements for a computer-communications system may be symbolized into a logic-based programming language at the beginning of the system development lifecycle. This provides an executable representation upon which automated tools for the analysis phase may operate. A paradigm is proposed for the application of analysis knowledge bases to the generation of a structured specification, and the paradigm is illustrated with an example taken from the field of military communications systems.

![](/api/attachments/CACQCQQD/fulltext/images/0a8cdc5813b9d0379687aa1f832032ce9f9c066fa8696b58c922417c565ff611.jpg)

Peter Scott has been with RCA Government Communications Systems Division since 1976, working on the systems engineering of message switching systems. From 1966 to 1976 he performed computer architecture for RCA's Advanced Technology Laboratories, and from 1961 to 1965 he was a development engineer with International Computers, Ltd. His current research interests are in the automation of the systems engineering process. Scott received his B.Sc. in physics from the University of Bristol, England, in 1961, and his M.S.E. in systems engineering and operations research from the University of Pennsylvania in 1967. He is a member of the IEE, the IEEE and the IEEE Computer Society, and is a UK Chartered Engineer.

## 1. Introduction

System development in a government contracting environment generally involves working from a number of natural-language requirements documents with limited opportunities for interaction with the eventual user. These documents may include a statement of work and a top-level system specification, supplied by the government customer, and a proposal, supplied by the contractor, and together they define the agreed requirements of a system to be delivered. In order to resolve ambiguity and facilitate automation, it is desirable to obtain an executable representation of these documents as early as possible in the system development lifecycle. Symbolizing the natural-language text into a logic programming language can provide this executable representation without altering the pertinent semantic relationships expressed. This approach was proposed by the Logic Programming Group at Imperial College, London, who symbolized most of the British Nationality Act into Prolog, demonstrated the iterative nature of the symbolization process, and concluded that the resulting formalization would support the mechanized analysis of the logical consequences of the act [1,2].

The eventual product of requirements analysis, the first major phase of the contractor's system development lifecycle, should be a self-consistent and unambiguous specification which describes the requirements as they will be presented to the group responsible for design and implementation. A number of tools are available to support the generation of such a specification, including PSL/PSA [3] and SREM [4], but the requirements have to be expressed in a special-purpose language defined for each tool. Perhaps the most widely used analysis and specification methodology is the Structured Analysis of DeMarco, who recommends a combination of data flow diagrams, 'minispecs' and a data dictionary to describe the requirements of a system [5]. These three components of a structured specification can all be expressed in a logic programming language, which is therefore appropriate for representing requirements from beginning to end of the requirements analysis phase. In addition, much of the expertise needed for performing requirements analysis can conveniently be expressed as a set of rules in the same logic programming language. Finally, it is particularly straightforward in a logic-based representation to include appropriate audit trails to facilitate traceability, which is the capacity to monitor development by keeping track of where requirements are met.

An existing tool which implements some of the above features is The Analyst, providing Prolog-based automated support for requirements analysis [6,7], and employing a methodology named CORE, for Controlled Requirements Expression [8]. Requirements are input to The Analyst in CORE format, using predefined symbols or a restricted subset of English ('constrained' English), and a knowledge base of Prolog facts is compiled to represent them. The CORE methodology is represented by a knowledge base of Prolog rules, which identify errors in the requirements. The output of The Analyst is a specification in CORE format with underlying Prolog representation.

Unlike The Analyst, the paradigm described in section 2 starts out methodology-independent. Once the requirements for a target system have been symbolized into unambiguous and machine-analyzable form using Prolog, a knowledge base of rules about the specification domain will provide an initial indication of what appears inconsistent or incomplete, and will generate error reports, providing the opportunity for problems to be resolved. A knowledge base of rules about the chosen methodology will then transform the requirements into an early version of a structured specification, while the production of trace reports will allow for keeping track of what requirements are being addressed.

With Prolog as the implementation language, the paradigm is illustrated in section 3 by the analysis of a subset of the requirements for a military communications system. A target system of this kind generally consists of a network of computer-based nodes providing facilities for entering, transmitting, receiving, switching, storing, forwarding, editing, displaying and printing messages. A vocabulary of Prolog predicates and a set of analysis rules, both tailored to this application domain, have been developed and are included in the example.

## 2. Paradigm for a Requirements Analysis Expert System

The paradigm is represented by the data flow diagram of fig. 1. The input to the paradigm is the set of natural-language requirements from the user (customer), stored in the form of written documents. The first process, 'Symbolize' (section 2.1), expresses the requirements as Prolog 'facts' using a predefined vocabulary of Prolog predicates. The remainder of the paradigm may be thought of as a progression of Prolog facts, starting with the 'Analyze' process (section 2.2) to locate errors. Evaluation of these errors by the 'Interpret' process (section 2.3) closes the loop by correcting the Prolog version of the requirements. When the errors have been removed, the requirements are transformed by the 'Specify' process (section 2.4), whose output defines a set of data flow diagrams with which the designer can work, and from which trace reports can be extracted by the 'Trace' process (section 2.5). The examination of trace reports by a systems engineer may result in modifications to the Prolog version of the requirements.

The following subsections explain the five processes of the paradigm, and show how they support the needs of requirements analysis and traceability.

## 2.1. Symbolize

The Symbolize process is currently performed manually, and involves parsing the natural-language text of the written requirements documents, extracting the pertinent relationships using simple declarative sentences, and expressing each sentence as a Prolog clause using a predefined Prolog predicate. A limited vocabulary of predicates must be generated in advance for each application domain, taking into account the entities and relationships likely to occur, and it should evolve until it is adequate for symbolizing the requirements of any system in that domain. Most of the predicates will be common to a range of different domains, because many terms are common to the natural-language descriptions of the requirements of different kinds of systems, and also because many of the less common terms appear as arguments rather than as predicates. The resulting Prolog clauses will be referred to as the canonical requirements facts, and are entered into the requirements knowledge base.

![](/api/attachments/CACQCQQD/fulltext/images/ca2c1109796e6e4a6d7ca613048df68570c7a773ebe4de94755fcd0ac7e18e1c.jpg)  
Fig. 1. The Paradigm.

The following predicates used in the Symbolize process are a subset of the limited vocabulary needed for describing requirements of military communications systems, and include as entities the system being analyzed, external systems with which it communicates, and functions $^{1}$ of the target system. The last argument in each Prolog clause is a reference to the paragraph number and position within that paragraph where the corresponding simple declarative sentence originated, thus providing the key to traceability.

System(S, C)
Entity S is the system being analyzed.

Interface(S, C)
An entity S exists outside the system being analyzed.

Console(S, C)
S is the name of a console associated with the system.

Function(N, P, C)
N is the name of one of the functions of entity P.

Receive-messages(N, S, B)
Entity N receives messages from an outside source S.

Message-content(S, N, B)
Information N is included in messages from external source S or to external destination S.

Receive $(R, L, D, B)$

Entity D requires data L which originates from an outside source R.

Transmit-messages(N, D, B)
Entity N transmits messages to an outside destination D.

Transmit(D, L, S, B)
Entity S provides data L which is intended for an outside destination D.

Fetch(R, L, D, B)
Entity D requires data L from entity R.

Send(D, L, S, B)
Entity S provides data L to entity D.

Due to the need to provide clear guidance for the development effort, natural-language requirements documents are normally written in short sentences, often approximating the simple declarative sentences which can be expressed in Prolog clauses. Most key words will either correspond to predicates in the vocabulary, or become arguments of those predicates. It therefore seems likely that the semantic problems involved in automating symbolization can be avoided, and that natural-language processing will eventually provide the means.

## 2.2. Analyze

The canonical requirements facts placed in the requirements knowledge base by the Symbolize process are first analyzed by means of a Prolog-implemented application-specific knowledge base containing rules about the application domain (military communications systems). The rules are designed to operate on the vocabulary of predicates generated for that domain, and they expect the same set of entities (system, external, function). The objectives of the analysis are to discover cases of inconsistency and incompleteness and produce error reports for the Interpret process. The Analyze process also converts the canonical requirements facts into less application-dependent form, examines their structure, and produces the baseline requirements facts from which the specification will be prepared.

The following predicates are used in the Analyze process to replace application-specific expressions, identify errors and display the structure of the requirements.

In(N, S, B)
Entity N has input from a source S outside the system, and requirement reference B.

Out(N, D, B)
Entity N has output to a destination D outside the system, and requirement reference B.

Error(N, D, B)
D is an error message concerning entity N,
whose requirement reference is B.

Level(N, M)
M is the number of ancestors $^{2}$ of function N.

Group(N, P)
N is a function whose ancestors are listed,
together with itself, in P.

The rules for analysis are contained in the application-specific knowledge base, which controls the Analyze process. Any error reports are produced by the Analyze process, which also adds to the canonical requirements facts to produce the baseline requirements facts. The following two rules serve to illustrate the detection of inconsistency and incompleteness.

error(N, 'function is part of entity which is neither the system nor another function', B): - function(N, P, B), not(function(P, R, C)), not(system(P, D)).

error(N, 'function has no input', C): -

function(N, P, C),

not(receive-messages(N, S, B))

not(fetch(R, L, N, D)),

not(send(N, M, T, E)).

The first rule indicates an inconsistency if N is a function of an entity P which is not a function of any other entity R and is not the system itself. The second rule indicates incompleteness if function N does not receive messages from any outside source S, does not require data from any other function R, and is not provided with any data by any other function T.

## 2.3.Interpret

Another manual process, Interpret involves determining which errors reported by the Analyze process should be acted upon, and providing any corrections for the Symbolize process to modify the canonical requirements facts. It is not necessary to remove all 'errors', as in many cases they may be intentional incompleteness reflecting a 'don't care' decision by the user, and offering flexibility to the designer. For example, a function may be decomposed by the user into two lower level functions, with no requirement as to how the two are related. The designer can later identify the interrelationships between them by specifying what data they exchange.

## 2.4. Specify

The baseline requirements facts are converted into structured specification facts with the aid of a Prolog-implemented technique-specific knowledge base. The technique rules embodied in this knowledge base represent a technique driver which depends on the methodology to be employed by the design and implementation group, such as the Yourdon-DeMarco methodology used here [5]. This methodology employs a hierarchy of data flow diagrams to represent the partitioning of a set of requirements into a structured specification. A data flow diagram is a network of processes which transform input data into output data. Each process may be partitioned into lower level processes, down to any level of detail. Supporting descriptions are required to define the data which appears in each input and output (data dictionary), and the transformations which are performed by each process ('minispec').

The Specify process described here includes the allocation of baseline requirements facts to a set of data flow diagrams, but the associated minispecs and data dictionary completing a structured specification are omitted in this discussion. Each component of the data flow diagrams is defined by one or more Prolog facts, which together represent the structure of the requirements as well as the graphics primitives. Each Prolog fact references all the paragraphs in the written requirements documents which led to the need for that component, therefore the resulting specification knowledge base includes the audit trail required for trace reports.

The following predicates are used in the Specify process to define components of a Yourdon–De-Marco specification.

Member(X, Y)

Used to define a member X of a list Y.

External(N, D, C)
A box with name N on diagram D and with requirement reference C.

Process(N, P, C)
A bubble with name N on diagram P and with requirement reference C.

Dataflow(L, S, D, C)
An arc with name L, source S, destination D and requirement reference C.

These predicates include one which will be used to define a Prolog construct (member), one which will be used to generate individual data flow diagrams according to the conventions of structured analysis (diagram), and three which are involved in the actual modeling of the requirements being analyzed.

The rules for specification constitute a subset of the technique-specific knowledge base, which controls the Specify process, and produces structured specification facts in a form which can be used to generate data flow diagrams. The following three rules employ the predicates defined above to show how the process works.

diagram(N, M): -
function(N, \_, \_), function(-, N, \_),
level(N, M).

process(N, P, C): -

function(N, P, C).

dataflow(N, X, Y, B): - fetch(S, N, D, B), group(S, G), member (X, G), group(D, F), member(Y, F), function(X, P, \_), function(Y, P, \_), X \ = Y.

The first rule specifies a diagram with name N at level M, given a function N which has level M and has at least one subfunction. The second rule specifies a process (bubble representing a function) with name N on diagram P, given a function P with a subfunction N. The third rule specifies a data flow (arc representing a transfer of data) with name N from process X to process Y, given that X and Y are distinct subfunctions of the same function P, and a lower level function D of Y requires data N from S, a lower level function of X. D is recognized as a lower level function of Y because its ancestors are listed in F, which has Y as a member. S is recognized as a lower level function of X because its ancestors include X.

## 2.5. Trace

A systems engineering group, in monitoring compliance, may wish to query the specification knowledge base to determine where in the design a particular requirement is met, or to what requirements a particular specification feature is responding. The Trace process accepts a Prolog trace query in the form of a structured specification fact with either the entity name missing (for a forward trace) or the requirement reference missing (for a backward trace). A trace report is generated which supplies the missing argument, thus identifying either the entity or the requirement. This may expose a problem with the symbolization, leading to modifications of the canonical requirements facts.

## 3. Illustration of the Paradigm

An extract from a written requirements document has been used to illustrate the paradigm. The following subsections present the extract, the corresponding Prolog canonical requirements facts, the error reports, the baseline requirements facts, the structured specification facts and examples of trace queries and trace reports. Also shown is the graphic equivalent of the structured specification facts in the form of a set of data flow diagrams. The Prolog syntax used is that of the University of Edinburgh [9].

## 3.1. Requirements Document Excerpt

The following excerpt includes the original paragraph numbering, so that the incorporation of traceability information can be illustrated.

'3.7.2 Characteristics of Event Analyzer Functional Areas. The event analyzer functional areas are divided into Communications and Processing.'

'3.7.2.1 Communications Functions. The Communications functions shall handle the reception of messages containing information on events from sensors. Also, the transmission and reception of messages from/to the backup event analyzer and transmission of messages to user A and user B shall be performed. The Communications functions include communications line interface handling and message retention.'

‘3.7.2.2 Processing Functions. The Processing functions are Message Validation and Analysis. The received sensor messages shall be validated. The valid messages shall be analyzed to determine if a reported event is significant. The significant events shall be correlated with planned responses.’

Information about the context of the event analyzer is not included, since it is distributed throughout the source document.

## 3.2. Corresponding Canonical Requirements Facts

The Prolog facts listed below begin by defining the system of interest ('event-analyzer') and its interfaces with the environment. They continue as a symbolization of the indicated paragraphs of the natural-language requirements document extract in the previous subsection.

/\* System environment \*/

system(event-analyzer, environment).

interface(sensor, environment).

interface(user-b, environment).

interface(user-a, environment).

interface(backup-event-analyzer, environment).

/\*3.7.2 Characteristics of Event Analyzer Functional Areas \*/ function(communications, event-analyzer, '3.7.2-a').

function(processing, event-analyzer, '3.7.2-b).

/\*3.7.2.1 Communications Functions \*/
receive-messages(communications, sensor, '3.7.2.1-a').

message-content(sensor, events, '3.7.2.1-b').

receive-messages(communications, backup-event-analyzer, '3.7.2.1-c').

transmit-messages(communications, backup-event-analyzer, '3.7.2.1.-d').

transmit-messages(communications, user-a, '3.7.2.1-e').

transmit-messages(communications, user-b, '3.7.2.1-f').

function(line-interface, communications, '3.7.2.1-g').

function(message-

retention, communications, '3.7.2.1-h').

/\*3.7.2.2. Processing Functions \*/

function(message-validation, processing, '3.7.2.2-a').

function(analysis, processing, '3.7.2.2-b').

receive(sensor, received-sensor-

messages, message-validation, '3.7.2.2-c').

fetch(message-validation, valid-sensor-

messages, analysis, '3.7.2.2-d').

function(evaluation, analysis, '3.7.2.2-e').

function(correlation, analysis, '3.7.2.2-f').

send(correlation, significant events, evaluation, '3.7.2.2.-g').

The last argument of each clause is the paragraph number in the source document followed by an alphabetic sequence letter.

## 3.3. Error Reports and Baseline Requirements Facts

Analysis by the application rules generates error reports and baseline requirements facts, some of which are shown below. The first two lines are self-explanatory error reports. The remainder are facts which, when added to the canonical requirements facts, complete the baseline requirements made available to the Specify process.

Error reports

evaluation: function has no input. Reference 3.7.2.2-e

processing: function has no output. Reference 3.7.2-b

Baseline requirements facts

in(communications, sensor, 3.7.2.1-a).

out(communications, user-a, 3.7.2.1-e).

fetch(communications, received-sensor-messages, message-validation, 3.7.2.2-c).

level(evaluation, 3).

level(correlation, 3).

group(correlation, [correlation, analysis, processing, event-analyzer]).

The last two lines identify the function ‘correlation’ as being at level 3 in the hierarchy, under ‘analysis’, ‘processing’ and ‘event analyzer’.

## 3.4. Structured Specification Facts

Specification using the technique rules generates the structured specification facts, some of which are shown below.

Diagram: context (Level: context).

Diagram: event-analyzer (Level: 0).

External: sensor on context diagram. Reference environment

Process: event-analyzer on context diagram. Reference environment

Dataflow: received-sensor-messages has source communications and destination processing. Reference 3.7.2.2-c

Dataflow: received-sensor-messages has source connector and destination message-validation. Reference 3.7.2.2-c

Dataflow: events has source sensor and destination event-analyzer. Reference 3.7.2.1-a

Dataflow: events has source connector and destination communications. Reference 3.7.2.1-a

The facts identify the diagrams in the structured specification, and the externals, processes and data flows which appear on the diagrams. It would be relatively straightforward to automate the translation of one formal representation (Prolog facts) to the other (data flow diagrams), but here it has been done manually. A set of data flow diagrams corresponding to the structured specification facts appears in fig. 2, where the incompleteness of the structure is immediately apparent.

An example of inferencing is provided by the addition of the data flow received-sensor-messages to the event-analyzer diagram. The canonical requirements facts state that this data is needed by the message-validation function, and that the communications function receives messages from the sensor. The Analyze process infers that this data must be sent to the message-validation function by the communications function. The Specify process then infers that, since the parent of message-validation is processing, which is on the same diagram as communications, the data flow must enter processing.

## 3.5. Trace Queries and Reports

Two examples of trace queries and the responses are given below.

![](/api/attachments/CACQCQQD/fulltext/images/b8d5b50f40eb21e493cca9f08b093f6f9c5c220fe0be4bc7562e8d02ebaffd03.jpg)  
Fig. 2. The Structured Specification.

?- process(A, B, '3.7.2.1-h').

A = message-retention

B = communications

More (y/n)? y

no

?- process(correlation, -, A).

$$
\mathbf {A} = 3. 7. 2. 2 - \mathbf {f}
$$

$$
\text { More } (\mathbf {y} / \mathbf {n})? \mathbf {y}
$$

no

The first query is a forward trace to determine what processes implement requirement 3.7.2.1-h, which reads: 'the communications functions include message retention'. The response identifies one process, message-retention, whose parent process is communications. The second query is a backward trace to determine what requirement is responsible for the existence of the process called correlation. The response identifies requirement 3.7.2.2-f, which reads: 'the significant events shall be correlated with planned responses'.

## 4. Conclusions

The simple illustration described in section 3 serves to explain the operation of the paradigm defined in section 2, but the impact of such an approach on the development of large, complex systems is expected to be dramatic. A logic programming language such as Prolog can be used to represent all the relevant requirements of a computer-communications system in analyzable form right from the beginning of a development program, facilitating the mechanization of the entire lifecycle from requirements analysis to software maintenance. The full benefits have yet to be recognized, let alone exploited, but it is expected that they will easily outweigh the cost of routine symbolization.

The benefits include the possibility of detecting more errors in the requirements analysis phase, where they typically cost an order of magnitude less to correct than in the design phase [10]. Also the first version of a graphic form of the specification, which is the form usually preferred for manual analysis, can be produced immediately the requirements documents have been symbolized. Finally, any changes to the requirements (or to the application or technique rules) immediately ripple through to the specification, avoiding delays which might affect the entire development team.

In order to develop the existing paradigm into an expert system with serious breadth and depth, the following issues are among those which need to be pursued.

While symbolization can be done manually by a non-analyst, steps towards automating this process are available on the basis of recent progress in natural-language processing.

The vocabulary of predicates to be recognized by the application rules within any selected application domain should be small enough to ensure that the paradigm is generic, yet rich enough to permit the symbolization of the requirements of a variety of systems in that domain.

The application-specific knowledge base must be extended by the capture of more rules describing how analysts work; for example, they take into account implied requirements, constraints, and criteria for optimization.

Existing programs for generating data flow diagram layouts from descriptions of their components (processes, data flows, externals, connectors and stores) may be adapted to Prolog.

## References

[1] Kowalski, R., AI and Software Engineering, Datamation (Nov. 1, 1984) 92–102.

[2] Sergot, M.J., F. Sadri, R.A. Kowalski, F. Kriwaczek, P. Hammond and H.T. Cory, The British Nationality Act as a Logic Program, Comm. ACM, 29, 5 (May, 1986) 370–386.

[3] Techroew D. and E.A. Hershey, PSL/PSA: A Computer-aided Technique for Structured Documentation and Analysis of Information Processing Systems, IEEE Trans. Software Eng. SE-3, 1 (Jan., 1977) 41–48.

[4] Alford, M.W., A Requirements Engineering Methodology for Real-time Processing Requirements, IEEE Trans. Software Eng., SE-3, 1 (Jan., 1977) 60–69.

[5] DeMarco, T., Structured Analysis and System Specification (Prentice-Hall, Englewood Cliffs, NJ, 1978).

[6] Stephens M.R. and K. Whitehead, The Analyst – An Expert Systems Approach to Requirements Analysis. Proc. 3rd Seminar on Application of Machine Intelligence to Defence Systems (June, 1984).

[7] Stephens M.R. and K. Whitehead, The Analyst - A Workstation for Analysis and Design, Proc. 8th International Conference on Software Engineering, London (Aug., 1985) 364–69.

[8] Mullery, G.P., CORE - A Method for Controlled Requirement Specification, Proc. 4th International Conference on Software Engineering (1979) 126-135.

[9] Clocksin W.F. and C.S. Mellish, Programming in Prolog (Springer, New York, NY, 1984).

[10] Boehm, B.W., Software Engineering Economics (Prentice-Hall, Englewood Cliffs, NJ, 1981).
