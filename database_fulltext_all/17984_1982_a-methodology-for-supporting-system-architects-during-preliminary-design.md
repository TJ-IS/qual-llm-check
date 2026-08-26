---
otero_id: 17984
otero_key: "ZR47GSYK"
title: "A methodology for supporting system architects during preliminary design"
authors: "Sid L. Huff"
year: "1982"
journal: "Information & Management"
doi: "10.1016/0378-7206(82)90006-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Methodology for Supporting System Architects During Preliminary Design

Sid L. Huff \*

Sloan School of Management, Massachusetts Institute of Technology, Cambridge, Massachusetts, USA

By and large, software engineering has concerned itself with relatively well structured problems, focusing on the detailed design and coding phases of the development cycle. However, there is substantial need today for improved understanding of those phases of the development cycle that are inherently fuzzy or lacking in structure. Pre-eminent among these fuzzy problem areas is the determination of a system's initial functional requirements and their decomposition into a set of design subproblems that will serve as the basis for detailed design. This paper presents a new methodology for aiding a system architect in carrying out these activities. Some experience with this methodology is also reported.

Keywords: System design, system architecture, design methodology, requirements specification, requirements decomposition.

![](/api/attachments/ZR47GSYK/fulltext/images/92cb36f0f668a0e2e437e5998d550bac0e9f111295d939fc0d6499f33e74a972.jpg)

Sid L. Huff is an Assistant Professor at the School of Business Administration, The University of Western Ontario. Formerly he taught at Queen's University, Kingston and at the Sloan School of Management, M.I.T. He has also worked as a management consultant with Woods, Gordon & Co., Toronto, and as a research engineer with Ontario Hydro. He holds B. Sc., M. Sc., and M.B.A. degrees from Queen's University, and a Ph.D. in Information Systems from M.I.T. His current research interests centre on management of the information systems function.

## 1. Introduction

You have been named project leader for XYZ project in your organization. XYZ is to be a large, multi-faceted batch-and-interactive information system based on a database management system; it will replace several smaller systems. You and a small team have laboriously developed, with extensive participation of various user groups, a Functional Requirements document for the new system. This document specifies the objectives of the target system in straightforward prose that both the preliminary design team and the users can understand. You have available a pool of programmers and system designers to work on XYZ. You are faced with the task of organizing them into small teams, partitioning the development project into 'design sub-problems', and starting detailed design.

You are well aware of the fact that early design decisions, such as the project partitioning, can and often do have a disproportionately large impact on the eventual success of the system. Yet, especially when compared to the abundance of literature concerning detailed system design, there is almost no published research directed at these early, fuzzy, inherently complex design decision processes. Thus you must use your best judgement and intuition, drawn from past projects, to uncover the most appropriate partitioning for this large, complex problem.

The creation of large, complex computer-based systems is extremely difficult and challenging work. Much of the difficulty stems from the inability of system designers to mentally grasp all, or even most, of a system's parts at one time. Decomposition of an overall system into subsystems must be carried out relatively early in the design process, so as to reduce the scope that any one designer must comprehend at one time.

The determination of a target system's initial, high-level functional requirements, and the partitioning of these requirements into subsets in an effective manner is often termed system architectural design. Essentially, the objective of architectural design is to provide a framework for logically subdividing the detailed design effort in a large system development project.

Unfortunately, the process of decomposition is not well known or understood. It is a process based almost entirely on personal judgement, which in turn is based mainly on past practice. No widely accepted measures or indices of 'good' preliminary decompositions exist. Nor have any explicit methodologies for decomposing large complex systems been previously explained or widely used. The Systematic Design Methodology (SDM), described in this paper, has been developed to provide a more coherent and better structured basis for guiding architectural design activities. SDM, then, is a first step toward meeting these needs.

## 2. Related Research

The Systematic Design Methodology was developed from two key sources of previous research.

Christopher Alexander, in the monograph Notes on the Synthesis of Form [1], presented some new ideas and techniques pertaining to structure design (i.e., conventional architecture). Alexander based his ideas on the centrality of a system's functional requirements and their interactions, and on the need for a systematic approach to manage the complexity of large system design effectively.

These ideas lead him to propose a way to systematize the search for those “subsets of requirements that should be dealt with independently”. This Alexander viewed as a search for problem structure. In effect, he argued that one should search for subsets of system requirements that are closely related to each other but also relatively weakly related to other such subsets.

This line of reasoning bears a close resemblance to the other previous research results: the concepts of strength and coupling of program modules made prominent by Myers et al [2]. However, the software design ideas of these researchers are concerned with detailed program design, not system architecture. Myers, for example, has stated,

"If the product being developed is a system, rather than a single program, there is another design process that must occur... This process is called system design, and is the decomposition of the system into a set of individual subsystems or individual programs. Although some of the ideas of Composite Design may be appropriate here, Composite Design does not appear to be directly applicable to system design. Therefore, when designing a system, as opposed to an individual program, the designer must first partition the system into distinct subsystems" [2, pp. 6].

Nevertheless, the strength/coupling concepts themselves are quite general, and form the basis of the primary objective function for requirements decomposition in SDM.

## 3. Expressing Functional Requiremer.s

The first step in the SDM approach is for the system architect (chief designer) to express the target system's functional requirements in a set of requirement statements, that meet certain criteria. This is extraordinarily difficult to do well, as many experienced designers have noted. Sharer [3], for example, has pointed out:

● Sophisticated problem solving is required to produce good statements of requirements. Problems must be translated into corrective goals, which must be translated into solutions, which must in turn be reduced to functional terms. There is no guarantee that the functions will create the desired results.

● The articulation of requirements is unusually difficult. Functions and processes are not easily described.

● System requirements change, and the definition must be able to absorb these changes.

● Tools and techniques for optimizing the definition process are not generally available.

● Heavy user involvement can introduce interpersonal and project management problems.

\- User motivation is difficult because reinforcement for their work is traditionally postponed until the implementation stage, by which time they have laerned to expect disappointment.

● The definition process can become highly political.

\- Definition is mentally taxing.

● Compromises which will eventually disenchant some of the users and analysts are required.

\- We work no real yardstick other than the ultimate success or failure of the system; there is no way to judge the quality of our definition.

(In applying SDM to real design tasks, all these problems have in fact been observed.)

In an effort to improve upon the general quality and appropriateness of statements of functional requirements, various ways were investigated for guiding and constraining the expression of formal requirements, without unduly restricting the semantics (meaning) of what was being expressed.

As a point of departure, it was presumed that a system's requirements would be written, in natural language sentences. Furthermore the following three guidelines for the construction of requirement statements were adopted:

(a) implementation independence - each statement should be 'implementation free,' i.e., should specify what is required of the target system but not how that requirement is to be met:

(b) unifunctionality - each statement should describe a single function (not multiple functions) to be featured in the target system;

(c) common conceptual level - all requirement statements should be, to the extent possible, at the same level of abstraction.

Of the three, probably the most important characteristic is implementation independence. When faced with a complex design problem there is a strong tendency for the designer to break the problem into sub-problems that resemble other problems with which he or she has dealt in the past. Such a decomposition may well be a poor one from the system architecture viewpoint. In attempting to avoid this phenomenon, it is important to exclude statements that primarily express implementation mechanisms, as opposed to functions to be provided.

A system's functional requirements are not usually expressed in this fashion in practice. The usual format is extended prose, and often includes a mixture of functional and procedural information spanning a wide range of conceptual levels. The question thus arises as to how a set of SDM requirement statements might be derived from requirements expressed in other forms.

Some previous research on structuring the syntax and semantics of requirement statements has been carried out. The most widely known effort is PSL, the Problem Statement Language component of the ISDOS project at the University of Michigan [4]. However, this and other previous efforts have been oriented toward a lower (more detailed), and generally more procedural, design level.

Another source of material on this problem is published requirement specification documents. Such documents are written and published by many sources, the U.S. Government being perhaps the most frequent publisher.

In order for the SDM approach to be practical, it is necessary to have a means of 'translating' such functional specification statements into an appropriate form – i.e., a form exhibiting the three characteristics discussed earlier. An initial approach for producing such a mapping is proposed here.

## 4. Requirement Statement Templates

Careful study of a number of real system specification documents revealed that the number of different 'kinds' of statements being made was relatively small. This observation, together with a study of other schemes such as PSL, led to the idea of formulating a set of requirement statement types, or 'templates'. These templates could then be used as a kind of filter with which to translate a conventional requirement specification into a set of SDM statement embodying the three criteria cited earlier. Such a set of templates would:

(a) help to guide the thinking of the analyst in setting up the system specification for SDM analysis; and

(b) help to insure that the resulting statements met the appropriateness criteria outlined earlier.

It would also form the basis for further study and research of the requirements specification process generally.

By drawing on the results of earlier research on requirements semantics, as well as studying numerous real requirement specification documents, a set of six statement templates was distilled. Each template is a very general 'skeleton' from which an infinite variety of specific requirement statements can be constructed. This is a generalization of the PSL approach, in which statements can be constructed from a given set of keywords and user-defined variable names. However, it would be inappropriate at the preliminary design stage to attempt to limit the vocabulary of the designer in the way that PSL does, and the SDM statement templates do not do that.

The SDM templates found to be most useful are shown below. Items in angle brackets are generic descriptors. Each such descriptor is discussed in more detail below. For each template, either "can" or "will" must be chosen, depending on the appropriate imperative form.

## 4.1. SDM Requirement Statement Templates

A. Existence

There (can/will) be $\langle modifier\rangle\langle object\rangle$ .

B. Property
'Modifier》〈object〉(can/will) be〈modifier〉
'property》.

C. Treatment

<Modifier> <object> (can/will) be <modifier> <treatment>.

D. Timing

<Modifier> <object> (can/will) be <timing statement> <modifier> <object>.

E. Volume.

<Modifier> <object> (can/will) be <order statement> <measure>.

F. Relationship.

<Modifier> <object> (can/will) <relationship statement> <modifier> <object>.

Specific terms used in the template descriptions are defined below.

Object. Objects are defined to be of two types: items, and activities. Examples of item objects are: - (file) size

\- (interactive query) facility

\- (user) request.

Examples of activity objects include:

\- (system) set-up

\- (database) maintenance.

Modifier. Modifiers are strings of English adjectives that serve to further describe the associated object. Examples of modifier strings are shown above, in parentheses.

Property. A property is a word that describes some key feature of the associated object. Examples include:

\- self-documenting

\- queryable

\- distributed.

Treatment. Treatments are words that describe something that can be done to the associated object. Examples include:

\- saved

\- sorted

\- locked.

Timing Relationship. Pairs of activity objects may be temporally related via timing relationships. For example:

\- occurs before

\- triggers

\- occurs during.

Order Statement. An order statement specifies an order relation $(<, <, =, >, >)$ between an object and a measure (defined below). Typical order statements are:

\- less than

\- no more than (i.e., less than or equal to)

\- at least (i.e., greater than or equal to)

Measure. A measure consists of a parameter and a unit. The parameter may be either a constant or a variable, and the unit may be either a simple unit (e.g., hours, dollars) or a compound unit (e.g., person-months, or dollars-per-month). Examples of measures include:

\- 2 hours

\- 95 percent

\- M1 person-months

\- 120 characters-per-second.

Relationship Statements. Relationship statements serve to describe or define a relationship between two objects. Examples include:

\- be independent of

\- contain

\- control

Imperatives. Each template may occur in either of two basic verb forms, distinguished by the use of either 'can' or 'will'. The use of 'can' indicates that the target system is to be capable (have the potential) of supporting the requirement being described, but that in a particular implementation that feature may or may not be so utilized. In contrast, the use of 'will' indicates that the feature described in that requirement must be present, as described, in the target system. Generally speaking, only one form ('can', or 'will') makes sense in any given requirement statement.

## 4.2. Examples of SDM Template-Based Statements

An example of each of the six template forms is given below. These statements were obtained by 'translating' a specification document issued by the U.S. Government for the acquisition of a certain type of database management system.

## A. Existence

There will be $\underbrace{database-level security}_{modifiers}$ $\underbrace{facilities.}_{object}$

## B. Property

$\underbrace{\text{System}}_{\text{modifier}} \underbrace{\text{status}}_{\text{object}}$ will be $\underbrace{\text{queryable}}_{\text{property}}$

## C. Treatment

Database can be initialized using system utility. object treatment modifiers

D. Timing
Schema validation will modifier object
occur before database usage, timing modifier object relationship

## E. Volume

Maximum recovery time will be modifier object no more than 24 hours order measure statement

## F. Relationship

Record selection criteria can modifier contain relationship statement object boolean modifiers expression. object

## 5. Interdependency Analysis

Once the requirement statements have been generated, the system designer must examine each pair of statements in turn, and make a decision as to whether a significant degree of interdependence between the two requirements exists. This is determined by considering how each of the requirements might be implemented in the target system, then determining whether substantial interaction (either interference, or support) between them is expected in the course of performing the implementation. A scale factor may also be assigned to represent the strength of interaction between each requirement pair. This process is called interdependency analysis.

Thus, while the requirement statements themselves are intended to be free of implementation bias, the assessment of interdependencies demands consideration of alternative modes of implementation. Considerable designer intuition and judgement is required in performing the interdependency assessment. It should be noted that this activity must be performed, in some way, by the designer, whether using the SDM or not. SDM, in effect, serves to bring this process 'out into the open.' An important advantage of the SDM approach is that requirements may be treated a pair at a time, thus greatly reducing the complexity of the overall task, at the cost of some additional analysis.

The requirement statements, together with the interdependency assessments, are then used to create a weighted interaction matrix. Each row and column of the interaction matrix corresponds to one of the requirement statements. Entries in the body of the matrix are numbers representing the strength of interdependency between each pair of requirements.

The data stored in the interaction matrix may be depicted as a non-directed graph, or set of nodes and links. Each node is a requirement statement, and each link represents an interdependency between a pair of requirement statements. The next step in the SDM process involves decomposing this global requirements graph into a set of subgraphs in the most effective manner. There are two key analytical problems here:

(a) how to measure the quality of a given decomposition;

(b) how to find the best (or at least close to the best.) decomposition.

These are discussed further below.

## 6. Network Decomposition

The first problem centers on exactly what software designers mean by a 'good' architecture for a software system. There is no broad consensus for the answer to this question among software design theoreticians. Different concepts of structure goodness have been proposed, each of which possesses its own positive and negative features. Major drawbacks common to all the proposed criteria in varying degrees, include:

(a) the difficulty of quantification;

(b) the problem of specifying how the criterion is to be achieved.

It is common wisdom, for example, that large systems should be constructed in a “modular” fashion. However, those who argue this generally do not specify how the measure the degree of “goodness” of a given system design, nor do they indicate concrete steps that system architects can follow to ensure their designs meet the criterion of modularity.

In attempting to overcome these drawbacks, SDM incorporates a quantified measure of structure goodness. This measure is based upon the concept of module strength and inter-module coupling. A number of authors have argued convincingly that a good software (detailed) design is one that consists of modules that possess high strength, or internal binding, and are also weakly interconnected [2,5]. SDM elevates this principle to the level of architectural design. The strength/coupling criterion is quantified in the following way. Suppose the graph representation of the target design problem has been decomposed into a set of non-overlapping subgraphs:

$$
\left\{G _ {1}, G _ {2}, \dots , G _ {n} \right\}.
$$

Then if $S_{i} =$ the strength of subgraph $G_{i}$ , and $C_{i,j} =$ the coupling between subgraphs $G_{i}$ and $G_{j}$ , define:

$$
M = \sum_ {i = 1} ^ {n} S _ {i} - \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} C _ {i j}.
$$

This index M may be used as a figure of merit for the decomposition.

The subgraph strength and coupling factors $S_{i}$ and $C_{ij}$ are themselves defined in terms of the subgraph structure. The following definitions have proved the most useful in SDM research to date:

$$
S _ {i} = \frac {l _ {i} - (n _ {i} - 1)}{\frac {n _ {i} (n _ {i} - 1)}{2} - (n _ {i} - 1)} * \frac {W _ {i}}{l _ {i}},
$$

$$
C _ {i j} = \frac {l _ {i j}}{n _ {i} n _ {j}} * \frac {W _ {i j} ^ {\prime}}{l _ {i j}} = \frac {W _ {i j} ^ {\prime}}{n _ {i} n _ {j}},
$$

where

$l_{i}$ = the number of links contained in subgraph i.

$l_{ij}$ = the number of links between subgraphs i and j.

$n_{i} =$ the number of nodes within subgraph $i$ ,

$W_{i} =$ the sum of the weights on links in subgraph $i$ ,

$W_{i,j} =$ the sum of link weights on links between subgraphs $i$ and $j$ .

These definitions possess a number of nice properties. For instance, both $S_{i}$ and $C_{i}$ , fall in the range [0,1] (assuming the individual link weights are selected from [0,1]). Also, the $S_{i}$ terms are normalized with respect to minimum connectedness of the corresponding subgraph. That is, $S_{i}$ measures the extent to which the strength of subgraph i exceeds the minimum necessary to form a connected subgraph. A number of alternate formulations for S, and C, have been investigated: the foregoing forms have been found to be most effective in generating good design decompositions.

The second problem, that of locating the best decomposition of a given graph, is an interesting problem in its own right. The problem may be formulated as a highly nonlinear integer programming problem. Unfortunately, no mathematical techniques are available to solve the problem optimally except for trivial cases. Therefore, heuristic methods must be used in attempting to determine near-optimal decompositions. Two basic strategies are available. First a partitioning strategy may be used, that seeks to break up the graph into subgraphs until the best decomposition (according to the value of M) is located. Second, a clustering strategy may be followed, wherein a similarity measure between all pairs of graph nodes is defined, then clusters of nodes are generated by applying one of many possible clustering algorithms (e.g., complete linkage) to the similarity matrix.

A set on interactive software tools has been developed to assist in the routine data-handling aspects of SDM, and to carry out graph decompositions using a variety of partitioning and clustering heuristics [10]. Using these software tools, a good (high M) partition may be determined. Then the resulting sets of requirements must be interpreted, or framed, by the designer as design subproblems.

## 7. Design Subproblem Interpretation

The interpretation phase also requires substantial designer judgement. In essence, the system architect must answer two questions for each requirement subset:

(a) why should the requirements in the subset be grouped together, and,

(b) what does the subset of requirements represent in terms of the target system?

In cases where either (a) or (b) is unclear, the designer can refer to the interdependency file to see why the individual requirements within the subset were judged to be interdependent in the first place.

![](/api/attachments/ZR47GSYK/fulltext/images/85b25a23c4d1012f0e03b6abb5ded0427b6d507a0e07b134d0bc47e19f05190b.jpg)  
Fig. 1. Phases in the Systematic Design Methodology.

The interpretation phase (and to a lesser extent, the earlier phases) often leads to a reassessment of both requirement statements and interdependencies. In particular, during the final sub-problems interpretation phase it is common for the designer to discover missing requirements. Consequently, in applying SDM to real design problems, a two pass approach has generally been used. The first pass is used mainly to gather the bulk of the necessary design information and to produce a 'first cut' at the problem structure. The second pass incorporates any missing requirements identified during the first pass, as well as changes to the original requirements and/or interdependencies. In the SDM applications to date, the second pass decomposition has been significantly better (higher M, more straightforward interpretation) than the preliminary one.

Fig. 1 schematically illustrates the phases of SDM.

## 8. SDM Application Experience

A number of different applications of SDM have been carried out to date. Andreu, drawing on a set of requirements issued by a U.S. Government agency as part of a procurement process, successfully used SDM to develop an architectural design for a database management system [6].

Holden applied SDM to the design of a small software operating system [7]. This test differed from Andreu's in that the target system already existed (as a pedagogical case study in a textbook on operating systems [8]), together with substantial descriptive material including the assembly code for the system implementation. The design produced by Holden using SDM resembled the original design in most respects. While this is perhaps not surprising, given that Holden started with a finished system, it was encouraging to see that, at least in this case, SDM was 'stable'.

The most recent SDM application was carried out jointly by the author and a team of three system designers from the M.I.T. Administrative Information Systems office [9,10]. The target system was a new Institute-wide planning and budgeting application system. The new system was to be capable of supporting both batch and interactive usage modes, and was to use a DBMS (at that point unselected) for most of its data handling.

High-level functional requirement statements for the new system were developed out of existing requirements documentation and from information in the heads of the designers. At various points during this phase of the work, user representatives would review the requirement statements for both accuracy and completeness. The statement templates were used to good advantage in framing the requirement statements.

Requirement interdependencies were derived in the course of five meetings of roughly two hours each. While it might have been possible to generate a first cut at the interdependencies in substantially less time, much of the analysis time was directed at adjusting the requirements themselves. Essentially, in the course of the interdependency analysis the designers had to think carefully and repeatedly about individual requirements and their implementation-level interrelationships; the designers consequently learned much more about the nature of the problem and the real implications of the various requirements. This new learning was fed back into the SDM analysis through modification to requirement statements and previously constructed interdependencies.

The final requirements graph had 77 nodes and 385 interdependencies. The decomposition algorithms led to a best decomposition possessing 11 sub-graphs and 21 inter-subgraph linkages, with an objective function value M = 0.85. Interpretation of the design sub-problems and linkages was completed, and the resulting system design architecture emerged as shown in Figure 2. While some of the terminology used in the figure is problem-specific, most of the representation is easily grasped. Each sub-problem and linkage is described in greater detail in [10].

Using SDM does involve a time penalty, principally in the interdependency analysis phase. The penalty is not as bad as might appear however, because the interdependency matrix is usually quite sparse. To what extent the benefits of SDM, in terms of better system architectures, exceed these costs is a challenging problem for further research. The MIS literature generally suggests that more time and effort ought to be devoted to the early stages of system development, but how to do so most profitably is the question.

Research on the SDM approach is continuing, with emphasis along two tracks. One track address real-world applications of SDM, the other concerns the use of SDM as a developmental methodology in support of other research. For example, the MIT Infoplex project seeks to determine design parameters for a large-scale multi-microprocessor database machine [11]. SDM is being used to assist in structuring the architecture of the Infoplex.

![](/api/attachments/ZR47GSYK/fulltext/images/e8f29076c6bfd91775c8c7d7aa00be72e899c8c0314aebab611ae048728cb85d.jpg)  
Fig. 2. SDM-derived Architecture for MIT Planning and Budgeting System.

## 9. Summary

The Systematic Design Methodology has been created to assist designers of large complex systems in carrying out the preliminary, or architectural design process. SDM uses graph decomposition techniques to structure a system's high-level functional requirements into subsets, called 'design sub-problems,' from which detailed design may progress.

The input to SDM is a specification of the proposed system's functional requirements. In order to create a set of SDM statements from a given specification, a template approach has been proposed. By constructing functional requirement statements based on the SDM templates, the system architect can more derive a set of statements embodying the principles of independency, unifunctionality, and consistent abstraction level. Such statements then form a suitable basis for further SDM decomposition and creation of an optimum system architecture.

## References

[1] C. Alexander, Notes on the Synthesis of Form, Harvard University Press, 1964.

[2] G. Myers. Composite/Structured Design, Van Nostrand Reinhold, 1978.

[3] L. Scharer, "Pinpointing Requirements," DATAMATION, Vol. 27, No. 4, April 1981.

[4] D. Teichroew and E. Hershey: "PSL/PSA: A Computer Aided Technique for Structured Documentation and Analysis of Computer-based Information Systems." IEEE Trans. on Software Engineering, Vol. 3, No. 1, January 1977:

[5] J. Stevens, et al.: "Structured Design," I.B.M. Systems Journal, vol. 13, no. 2, April 1974.

[6] R.C. Andreu and S.E. Madnick: "An Exercise in Software Architectural Design: From Requirements to Design Problem Structure," Report P010-01-05, M.I.T. Center for Information Systems Research, Cambridge Mass., USA, November 1977.

[7] Timothy Holden, "A Systematic Approach to Designing Complex Systems: Application to Software Operating Systems," Report P010-7805-05, M.I.T. Center for Information Systems Research, Cambridge Mass., USA, May 1978.

[8] S.E. Madnick and J. Donovan, Operating Systems, McGraw-Hill, 1975.

[9] S. Huff and S. Madnick: "Software Architecture and the Semantics of Requirements." M.I.T. Center for Information Systems Research, Cambridge, Mass., USA, 1979.

[10] S.L. Huff: "A Systematic Methodology for Designing the Architecture of Complex Software Systems," Ph.D. dissertation, Sloan School of Management, M.I.T., Cambridge Mass, USA, May 1979.

[11] S.E. Madnick: "INFOPLEX: Hierarchical Decomposition of a Large Information Management System Using a Microprocessor Complex," Proc. 1975 NCC AFIPS Press, Montvale New Jersey, 1975.
