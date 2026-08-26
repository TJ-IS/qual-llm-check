---
otero_id: 17316
otero_key: "FYNUKF43"
title: "Computer-aided model construction"
authors: "Hemant K. Bhargava; Ramayya Krishnan"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90025-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computer-aided model construction

Hemant K. Bhargava

Naval Postgraduate School, Monterey, CA 93943, USA

Ramayya Krishnan

Carnegie-Mellon University, Pittsburgh, PA 15213, USA

We examine ways in which the construction of mathematical models may be supported, and review several approaches for computer-aided model construction. The construction of complex models can be a challenging task even for expert modelers. The aim of computer-aided model construction systems is to simplify this task. We view model construction as a state transformation process, and suggest that the process can be facilitated by supporting the creation of certain representations or by transforming an existing representation to another. For example, declarative modeling languages facilitate the specification of an executable statement of the mathematical model, while knowledge-based model construction systems assist the creation of the mathematical formulation. Knowledge-based model construction systems are the focus of our review of existing systems. To facilitate a comparison of several such systems, we characterize them in terms of their cognitive bases, the representations developed in them, and the methods for transformation of these representations.

![](/api/attachments/FYNUKF43/fulltext/images/1a16c1b99c383798ee8632e2c8c0febebc83ec0aca0bc25b3d02dddc0278eaf4.jpg)

Hemant K. Bhargava is an Assistant Professor of Information Systems at the Naval Postgraduate School in Monterey, CA. He received the B.S. in Mathematics degree from the University of Delhi in 1984, the MBA from the Indian Institute of Management (Bangalore) in 1986, and the Ph.D. in Decision Sciences from the University of Pennsylvania in 1990. His research interests include logic modeling, formal languages and systems for mathematical modeling, fleet mix planning, decision support systems, and intelligent automated forces in combat simulation. His work on this paper was partially funded by the Naval Postgraduate School's research initiation program.

## 1. Introduction

The appropriateness of a mathematical formulation for a problem depends on several factors. How accurately does it represent the reality? Are its assumptions reasonable? Is the data required by the formulation available? Can it be solved and at what cost? Is the model understandable by the user? Are its results likely to be understood and accepted? Not surprisingly, effective model construction requires much creativity as well as knowledge about modeling paradigms and about the problem domain. However, many potential users of mathematical models do not possess the knowledge or the experience required to formulate models. Even for expert modelers the construction of complex models is a challenging task. The goal of computer-aided model construction systems is to simplify this task, by facilitating the creation of certain representations or by transforming an existing representation to another.

The construction of mathematical models involves the development of mathematical abstractions corresponding to selective aspects of a problem situation $[12,16,44]$ . While the final result is a validated and debugged mathematical model, several other representations are also developed in this process. In this paper, we examine the ways in which computer-based systems support the creation and transformation of these representations. Our review will focus on a group of systems generally known as knowledge-based model construction systems.

![](/api/attachments/FYNUKF43/fulltext/images/d76c62b0c77774203bcb1aea99b8033789347637c8c415659b4f283f4102d68c.jpg)  
Ramayya Krishnan is an Assistant Professor for Management Science and Information Systems in the Heinz School of Public Policy and Management at Carnegie Mellon University. He has a B. Tech in Mechanical Engineering from the Indian Institute of Technology (Madras), a M.S. in operations Research and a PhD in Management Science and Information Systems. His research interests are logic modeling, model management, and semantic data modeling.

Computer-aided support has also been investigated for other constructive problem solving [11] tasks. Two examples are systems for computer-aided design (CAD) [19] and software engineering (CASE) [35]. $^{1}$ CAD systems provide constructs for stating design constraints, and support the translation of high-level statements of design constraints into an explicit description of the structure of objects satisfying the constraints [49]. Several CAD systems, ranging from sophisticated drafting tools that assist the final stage of electronic circuit design, to knowledge based systems that attempt to support the early design process have been developed. CASE systems translate high-level requirements specifications to executable programs. One class of CASE tools is used to describe the structure of programs and to generate programs for very specific applications (e.g., report writers) [51]. A more sophisticated class of tools includes knowledge-based automatic programming systems which can translate high-level design specifications to executable code in some programming language [42].

As in the areas of design or software engineering, there are several kinds of computer-aided model construction systems. One of the aims of this paper is to clarify the kinds of rôles that computer-aided model construction systems can play, and the features that they must contain to do so. For example, modeling languages $[10,15]$ have greatly reduced the effort required to implement large and complex models – assuming these have been formulated – and also provide seamless access to a suite of efficient algorithms. Knowledge-based model formulation systems $[37,27,28]$ , on the other hand, aim to assist in the creation of the mathematical formulation given an initial non-mathematical, perhaps incomplete, problem description. In our review of support for model construction, we will elaborate on these rôles.

A few words on the scope of this paper. We are primarily concerned, and so are most of the approaches referenced in this paper, with the construction of the mathematical structure of mathematical programming models. (Some work has been done on simulation model construction [43]; we will not discuss that any further.) There are several other issues related to model construction that we will discuss only where they are directly relevant. For example, model construction is closely related to model maintenance, since the formulation of a model often results in several versions of the model. The interested reader is referred to [40] for a good treatment of model maintenance issues. Some researchers (e.g., [31,36]) have also examined an approach to model construction in which composite models are developed by linking existing ones such that outputs of one model are an input to another. We have not included a review of these approaches as they do not address the construction of the internal structure of individual models.

The rest of this paper is organized as follows. In section 2 we suggest that model construction can be treated as a state transformation process, illustrate the idea with an example, and discuss several ways in which this process is supported. To facilitate comparisons among a diverse set of existing model construction systems and approaches, we present a general characterization of model construction systems in section 3. In section 4 we apply this framework in our review of model construction systems, and identify strengths and weakness of different approaches. In section 5 we discuss limitations in current work in computer-aided model construction and propose some directions for future research.

## 2. Perspectives on computer-aided model construction

Over the last two decades, several systems have been developed to support various phases of the model construction process. These systems have been specialized to create and transform specific representations generated during model construction. To facilitate our analysis of these systems, and to classify them in terms of the representations they support, we present a generic model of the model construction process and illustrate it with an example.

## 2.1. Model development as a state transformation process

The mathematical modeling process is an iterative process that progresses from an informal description of the problem to a formally defined mathematical model which is then instantiated and solved (see Figure 1). Informal descriptions may include natural language problem statements, and pictorial representations such as engineering drawings. These representations are transformed into a mathematical statement of the variables and the relationships between them. During this process, several other representations (states) are generated. These include a formal qualitative problem description, the implementation of the model in an executable modeling language, a representation of the input data, an instantiated representation of the model, and the representation of the solution. Each of these representations have been labelled as shown in Figure 1.

An operation (or operations) applied to one or more of these representations is used to yield another. For instance, the compilation (an operation) of model specifications in the ASCEND [39] language yields an instantiated data structure representation of the problem. Applying a solver (another operation) to this instantiated representation yields a representation of the feedback om the solver. The feedback could be the solu-on itself or an indication that the solver failed to converge to a solution. Further operations such as re reconsideration of previous modeling decisions and modifications to existing representations may be made based on this feedback. To immarize, the view of model construction as a ate transformation process suggests that the rocess can be facilitated by making it easy for modelers to work with, and operate on, one or more of a variety of representations.

![](/api/attachments/FYNUKF43/fulltext/images/97d6d2a2cba750fde392fa9228f40ab76f7a99f7114967e7c6aefe5e4f194d13.jpg)  
Fig. 1. Multiple representations generated in the modeling process.

![](/api/attachments/FYNUKF43/fulltext/images/92c8f4dcbca0e9f6ed9c738bbd4d908400487e45bd86a8b9bc380123e6cf02ff.jpg)  
g. 2. A pictorial problem description.

## 2. Example: The Delco case

We now illustrate the various problem-related representations mentioned above. Our example problem, (the “Delco case”, developed in [30]) concerns a production and distribution system lustrated in Figure 2. The case describes the reparation of a production plan for a refinery to operate at peak economic efficiency. The objective of this plan is to maximize profit, taking due account of the demand for the products. There are three production processes in the refinery: the distillation process, the catalytic cracking process, and the blending process. These processes use crude oil as a resource to produce regular gasoline, premium gasoline, and two kinds of by-products. The regular and premium gasoline are transported by pipelines. The decisions that need to be made are: (1) how much crude oil should be used? (2) how many different products should be produced? and (3) if the capacity of the distillation tower is increased, does a new pipeline need to be added to ship the gasoline products?

A detailed natural language description of the problem is given in Appendix A. A pictorial representation of the problem is depicted in Figure 2. A formalization of selective aspects of the natural language description in the problem specification language of a system called MFS [30] is shown in Figure 3. An instantiated mathematical

Max

$$
1 1. 8 0 X _ {3} + 1 9. 4 8 X _ {7} + 2 0. 1 0 X _ {8} - 3. 9 X _ {2} - 4. 6 X _ {6} - 1 2 X _ {1}
$$

$$
s. t.
$$

$$
5. 2 X _ {1} - X _ {2} = 0
$$

$$
5. 2 X _ {1} - 4. 2 X _ {3} = 0\tag{1}
$$

(2)

$$
X _ {2} - X _ {4} - X _ {5} = 0\tag{3}
$$

$$
2. 2 X _ {5} - X _ {6} = 0\tag{4}
$$

$$
2. 2 X _ {5} - 1. 2 X _ {7} = 0\tag{5}
$$

$$
X _ {4} - X _ {1 0} - X _ {1 1} = 0\tag{6}
$$

$$
X _ {6} - X _ {1 2} - X _ {1 3} = 0\tag{7}
$$

$$
8 6 X _ {8} - 8 4 X _ {1 0} - 9 4 X _ {1 2} = 0\tag{8}
$$

$$
9 2 X _ {9} - 8 4 X _ {1 1} - 9 4 X _ {1 3} = 0\tag{9}
$$

$$
X _ {8} - X _ {1 0} - X _ {1 2} = 0\tag{10}
$$

$$
X _ {9} - X _ {1 1} - X _ {1 2} = 0
$$

$$
X _ {2} \leq 6 0 0 0 0\tag{11}
$$

(12)

$$
X _ {6} \leq 2 0 0 0 0\tag{13}
$$

$X_{1}$ : quantity of crude input to distillation tower

$X_{2}$ : quantity of distillate output from distillation tower

$X_{3}$ : quantity of byproduct-1 output from distillation tower

$X_{4}$ : quantity of distillate input to blending

$X_{5}$ : quantity of distillate input to cracker

$X_{6}$ : quantity of gasoline stock output from cracker

$X_{7}$ : quantity of byproduct-2 output from cracker

$X_{8}$ : quantity of regular gasoline output from blending

$X_{9}$ : quantity of premium gasoline output from blending

$X_{10}$ : amount of distillate used in regular

$X_{11}$ : amount of distillate used in premium

$X_{12}$ : amount of gasoline stock used in regular

$X_{13}$ : amount of gasoline stock used in premium

Fig. 4. Delco mathematical model.

model is represented in Figure 4, and its implementation in a mathematical modeling language called GAMS [10] is shown in Figure 5.

As stated earlier, each of these figures denotes a state in the modeling process, and each state corresponds to a type of problem representation. Operations performed on a state result in the creation of a new state. While some of these operations need to be performed by a human modeler, others are executable on a computer. Consider for instance, the transition from the natural language description of the problem to the formalized qualitative description. Currently, no programs exist to perform this mapping. A human modeler is required to supply the qualitative description. However, computer-based assistance can be provided to check it for errors of omission or consistency. The mapping from the qualitative problem description to the mathematical model can be computed for specific domains and specific model classes. An example of an operator that performs such a mapping is the formulate model operator in the MFS system which transforms the qualitative description in Figure 3 to create the mathematical representation shown in Figure 4. Another example of an operator that can applied without any human intervention is the solve using OSL operator illustrated in the executable implementation of the mathematical model in GAMS (see Figure 5). It invokes the OSL implementation of the simplex method, and produces a tabular representation of the model solution.

## 2.3. Computer-based support for model development

In section 2.1 we identified seven problem-related representations (labelled A to G in Figure 1) and illustrated five of these with the Delco example. Let us now examine the ways in which the creation and transformation of these representations is supported in current modeling systems. We discuss three kinds of systems that support model construction.

1. Declarative modeling languages (and systems that use these languages) such as AMPL [15], NETWORKS [21,22], and ASCEND [39] facilitate the specification of an executable state-

## VARIABLES

```txt
X1 quantity of crude input to distillation tower
X2 quantity of distillate output from distillation tower
X3 quantity of byproduct-1 output from distillation tower
X4 quantity of distillate input to blending
X5 quantity of distillate input to cracker
X6 quantity of gasoline stock output from cracker
X7 quantity of byproduct-2 output from cracker
X8 quantity of regular gasoline output from blending
X9 quantity of premium gasoline output from blending
X10 amount of distillate used in regular
X11 amount of distillate used in premium
X12 amount of gasoline stock used in regular
X13 amount of gasoline stock used in premium
```

## EQUATIONS

```txt
OBJ defines objective function
CONST1 relationship between crude oil and distillate
CONST2 relationship between crude oil and byproduct-1
CONST3 flow balance of distillate
CONST4 relationship between distillate and stock at cracker
CONST5 relationship between distillate and byproduct-2
CONST6 flow balance of distilliate used in blending
CONST7 flow balance of stock used in blending
CONST8 belnding of regular gasoline, constraint on octane level
CONST9 belnding of premium gasoline, constraint on octane level
CONST10 quantity balance in blending of regular gasoline
CONST11 quantity balance in blending of preemium gasoline
COSNT8 constraint on distillate output
CONST9 constraint on gasoline stock output
CONST10 blend relationship
CONST11 blend relationship;

OBJECTIVE

OBJ.. Z =E= 11.8 * X3 + 19.48 * X7 + 20.1 * X8 - 3.9 * X2 - 4.6 * X6 - 12 * X1;

CONSTRAINTS

CONST1.. 5.2 * X1 - X2 =E= 0;
CONST2.. 5.2 X1 - 4.2 X3 =E= 0;
CONST3.. X2 - X4 - X5 =E= 0;
CONST4.. 2.2 * X5 - X6 =E= 0;
CONST5.. 2.2 * X5 - 1.2 * X7 =E= 0;
CONST6.. X4 - X10 - X11 =E= 0;
CONST7.. X6 - X12 -X13 =E= 0;
CONST8.. 86 * X8 - 84 * X10 - 94 * X12 =L= 0;
CONST9.. 92 * X9 - 84 * X11 - 94 * X13 =L= 0;
CONST10.. X8 - X10 - X12 =E= 0;
CONST11.. X9 - X11 - X12 = E= 0;
CONST12.. X2 =L= 60000;
CONST13.. X6 =L= 20000;

model BLENDING /all/;
solve BLENDING using OSL minimizing z;

Fig. 5. Delco Mathematical Model in GAMS.
```

ment of the mathematical model (Box F in Figure 1). They also provide transparent access to a suite of algorithms that are applied to produce a representation of a solution (Box G). Of course, even within this set, there are several differences in design philosophy and in the support for model construction. AMPL is designed to support modelers who work with the traditional algebraic notation; ASCEND supports such notation and also encourages a structured modeling $^{2}$ approach; NETWORKS, on the other hand, allows modelers to represent mathematical models as graphs. Another difference is in the feature set provided by the systems. ASCEND provides a suite of tools that suggest initial values, correctly set degrees of freedom of a system of equations, identify redundant equations, and verify dimensional consistency; other systems place the burden of these tasks on the modeler.

2. Analysis and debugging systems such as ANALYZE [18] guide the iterative reformulation of linear programming models. ANALYZE extracts model substructures that cause exceptions such as redundancy and infeasibility. It provides experts the ability to “navigate through the model in order to debug a run or, more generally, probe into the meaning of a solution.” The results of this analysis are used to refine the model, if necessary. With reference to Figure 1, ANALYZE operates on the representations in Boxes F and G.

3. Knowledge-based model construction systems facilitate the transformation of the qualitative problem specification (Box C) and the data (Box D) to the mathematical model formulation (Box E). They provide languages in which a modeler can develop a problem specification in terms of domain-specific objects and their relationships. They also provide a collection of operations that apply a combination of domain knowledge and general modeling principles to effect the transformation. Once again, there are differences in how specific systems represent and transform qualitative specifications.

Of the seven problem-related representations mentioned earlier, the earliest phases are supported only in knowledge-based model construction systems, which are the subject of the rest of our paper. Due to the diversity of approaches even with this category, we begin by presenting a framework for studying knowledge-based model construction systems.

## 3. A framework for knowledge-based model construction systems

In recent years, there has been substantial research in knowledge-based computer-aided model construction. Such research includes the study of the cognitive process involved in model construction $[40,46]$ as well as the development of software tools for supporting this process $[37,33,28,40]$ . While there has been some progress in understanding the cognitive aspects of model construction as well as in implementing prototype systems, no evidence has been reported about the actual benefits or success of these systems in an operational environment. Understandably then, there is much diversity in this work; diversity in (a) the class of users and the level of expertise that they intend to support (e.g., novice $[40]$ vs. expert $[37]$ ), (b) the types of models constructed (e.g., linear programming $[9]$ vs. simulation $[43]$ ), (c) level of generality (domain-specific $[29]$ vs. domain-independent $[37]$ ), (d) the cognitive theories of model formulation assumed (e.g., analogical reasoning $[32]$ vs. first-principles $[40]$ ), (e) “user interface representations” emphasized (e.g., graphical $[23]$ vs. textual $[40]$ ) and (f) implementation approaches and methodologies used (e.g., rule-based $[27]$ vs. frame-based $[9]$ ). At the same time cross-fertilization among these various approaches, while fruitful, has hardly been explored.

While it is generally agreed that model construction can be viewed as a state space search, there are differences in detail in how this idea is operationalized. Specific issues that a designer of a model construction system must resolve include: What knowledge should the system possess? How should it be represented? What inforion should the modeler supply and in what
? What techniques should be used to com-
the system's knowledge with the user's in-
? We propose that differences and similar-
between different approaches can be well
erstood by examining them in terms of the
owing five categories.

## Cognitive basis

cognitive model of human model construction is a useful starting point for thinking about puter-aided model construction. In the con-of CAD systems, it is suggested that “… to useful adjunct to human performance, the s must closely match the cognitive processes ciated with various design activities. A psy-ogical model of the human designers is there-an essential prerequisite to any successful ementation of a computer based design assis-” [3]. While such a model may not be an ential prerequisite” in building model con-ction systems, it would provide designers an-s to several crucial questions: Do modelers with surrogate representations? What kinds? these representations in terms of domain repts or are they domain independent? Do elers apply general-purpose knowledge about ses of mathematical models to specific knowl-e about the problem? Do they reason by ogy? Do they move from a simplistic model more complicated ones, or vice versa? Do they develop mental pictures of the model? Currently, on understanding the cognitive underpin-s of model construction is in its infancy. e researchers have conducted protocol analy-13] to study how modelers construct models, have used these results to guide the design of r systems (see e.g., [47,40]). Others (e.g., [27]), he absence of a definitive cognitive theory of rel construction, have implicitly assumed a icular cognitive model. In either case, the nitive model guides the choice of surrogate esentation, and determines the process used transform the surrogate representation into target representation.

## Surrogate representations

Model construction involves the creation and simplification of a mathematical abstraction of a real world problem. However, most people have difficulty in directly conceptualizing problems in terms of their mathematical formulations. Surrogate representations are used to state the problem in non-mathematical terms, and serve as intermediate representations for the transformation from the modeler's view of the problem to its mathematical formulation. Various kinds of representations have been proposed to facilitate this transformation. Depending on the class of users the computer-based system intends to support, it uses domain concepts from particular problem domains or objects (such as activities and resources) underlying certain model classes. Surrogate representations that are fairly close to the real-world view of the problem make much use of domain semantics and tend to have a high degree of domain-specificity. It is suggested that users with little or no training in mathematical modeling but with a great deal of domain knowledge conceptualize their problems in terms of domain concepts [29]. Experts, on the other hand, conceptualize problems in terms of objects, activities, and transformation, and employ surrogate representations that capture the mathematical structure of the model independent of the domain [37,33]. Systems using representations of the latter sort may not be able to provide much support to users in problem specification. However, since they are domain-independent, they provide broader coverage and are not limited to specific domains as domain-specific surrogate representations are.

## 3.3. External representations

External representations are the representations supported by the system's user interface, and are the physical realizations of the surrogate representations. The same surrogate representation can have multiple external representations. For example, the surrogate representation for models in PM\* (in terms of domain objects and the relationships between them) [27] is externally realized as sentences of a logic language [29] or as an attributed graph [23]. Some external representations naturally lend themselves to particular surrogate representations. For example, the block and arrow notation of LPFORM naturally lends itself to a graphical implementation [33]. The external representations employed in most systems are textual, icon-based, and graphical. The choice of external representations is guided by theories of human computer interaction [45] and by beliefs about how close certain external representations are to people's mental views of problems. Recent work has examined use of new technologies, such as syntax-directed structure editing and hypertext, in this context [20,6].

## 3.4. Supporting the development of surrogate representations

The development of a surrogate representation involves transforming the modeler's mental view of the problem into a form that accurately represents the modeler's view and with which the system can begin reasoning. Some researchers have proposed capturing the user's view textually, and understanding and refining it based on recognition of domain concepts and semantic relationships [27,40]. Others have proposed capturing the user's view directly in terms of domain-independent representations [37]. Clearly, syntax-directed structure editors can be developed for either alternative. However, the domain-specific approaches can also use semantic information to provide additional support (e.g., ensuring consistency in the specification) during problem specification. A specific example is the consistency check provided in the PDM system [28]. Given a problem that involves storage of some item, the system uses domain knowledge to infer that the problem should also potentially refer to concepts such as inventory costs, shipment, purchasing and selling.

## 3.5. Transformation of the surrogate representation

The transformation of the surrogate representation to the target representation requires structural knowledge about classes of mathematical models, domain knowledge, as well as an ability to make decisions such as which assumptions are critical and which can be relaxed. The various techniques for making this transformation can broadly be classified into (a) methods based on analogical reasoning, and (b) synthesis-based methods. Analogical reasoning methods attempt to retrieve a target model “closest” (based on measures of similarity) to the features of the surrogate representation. This retrieved model is then suitably repaired, if needed, to achieve a suitable target representation. The synthesis approach does not retrieve a whole model from some library as does the analogical approach. Rather, pieces of the model are constructed separately from the surrogate representations and then brought together into a logical whole. This synthesis is controlled by model construction rules that are domain-independent. If the surrogate representation is domain-specific, an intermediate step is required to convert the domain-specific representation to some form where the domain-independent rules can be applied. While synthesis-based methods have been employed and tested in several systems, the application of analogical reasoning to model formulation has not been investigated as deeply.

## 4. Knowledge-based model construction: A review

In this section we apply the framework presented in section 3 to review research in knowledge-based model construction. (At the time of the writing of this paper, we are aware of several ongoing projects on computer-assisted model formulation (e.g., [47]). We have chosen to concentrate in our review on projects for which detailed descriptions have appeared in the open literature.) We noted in the previous section that analogy and synthesis are two alternative approaches that have been investigated in knowledge-based model construction. We begin our review with a discussion of the work of Liang [32], who has recently described an application of analogical reasoning to support model construction.

## 4.1. Liang

Observational studies of the human modeling process $[46,40]$ suggest that expert mathematical modelers are able to categorize a problem (irrespective of the application domain in which it arises) into known “model types” (e.g., the classical model types such as transportation, blending, or product-mix). They derive a mathematical formulation for their problem by modifying the structure of the identified model type. While no cognitive account of this categorization ability has been provided, analogical reasoning is a commonly cited hypothesis. The work by Liang is an attempt to apply analogical reasoning in the automated construction of linear programming models.

The concept is to convert a problem description into a linear programming model by retrieving and, if need be, repairing a “similar” model from a library of models. There is no formal cognitive basis to the approach (nor claimed by the author) and the focus is on the development of a computational approach to analogical modeling. There are three important steps in the process. First, a problem is specified using three types of surrogate representations: the entity graph, the attribute heirarchy, and the feature grid. These representations are based on the structured modeling methodology introduced by Geoffrion [17] and are externally represented as tables. Second, elements in the entity graph associated with a problem are compared to the elements in the entity graph of a “case” (a previously encountered problem and its associated linear program) in order to determine “similarity”. The information in the attribute heirarchy and the feature grid is used to order candidates for analogical modeling by their degree of similarity to the problem under consideration. Finally, the linear programming model associated with the most analogous problem in the library is “transferred” and, if need be, heuristically “repaired”.

We now describe some of the details used to operationalize this approach computationally. Our review is based on the material in $[32]$ . The author describes a product-mix problem in terms of an entity graph, attribute heirarchy, and a feature grid. These representations taken from $[32]$ are shown in Figure 6.

No precise semantical description of the representations is provided, so we will use the author's informal discussions of these representations. The entity graph consists of objects that correspond to (sets) of primitive entities and compound entities in the problem. For example, product and resource are the primitive entity sets, while manufacturing is a compound entity set that is related to these primitive entities. The feature grid is a table which relates the problem entities (the Y-axis) to their attributes (X-axis). The entries in the table cells use the following convention. The capital letters correspond to variables with unknown values (e.g., Z, $X_{i}$ ), U is a special symbol used to denote that the relationship between the entity and the attribute is unspecified, and the lower case letters (e.g., $p_{i}$ ) denote parameters of the problem whose values are known. These representations are developed externally by the user and supplied to the system.

(a) FEATURE GRID

<table><tr><td>ATTRIBUTE ENTITY</td><td>TOTAL PROFIT</td><td>UNIT PROFIT</td><td>TOTAL CONSUMPTION</td><td>UNIT CONSUMPTION</td><td>PRODUCTION QUANTITY</td></tr><tr><td>ROOT</td><td>Z</td><td>U</td><td>U</td><td>U</td><td>U</td></tr><tr><td>PRODUCT</td><td>U</td><td> $P_1$ </td><td>U</td><td>U</td><td> $X_1$ </td></tr><tr><td>RESOURCE</td><td>U</td><td>U</td><td> $b_1$ </td><td>U</td><td>U</td></tr><tr><td>MANUFACTURING</td><td>U</td><td>U</td><td>U</td><td> $a_2$ </td><td>U</td></tr></table>

![](/api/attachments/FYNUKF43/fulltext/images/2eedc6772a1eab4825c8b7a4b08e00b50c13a8a3ed590498a9dce2fa64374667.jpg)

(c) Attribute Hierarchy  
![](/api/attachments/FYNUKF43/fulltext/images/eda4c49657bc7f00d80d1987fa75522f1da08ace26b2333ac1d0f8ed520b9dd4.jpg)  
Fig. 6. Surrogate representations for analogical approach.

The attributes in the feature grid are also related to one another using an attribute heirarchy. Relationships in the heirarchy are based on the measurement units associated with the values measured by the attributes. For instance, total-cost, whose dimension is currency is related to unit-cost whose dimension is currency per unit. Since they share a dimensional term, currency, they are represented as nodes in the same branch of the attribute heirarchy. The distance of a node in the attribute heirarchy from the root is based on the “simplicity” of the dimension of the values they measure. For instance, this rule is used in Figure 6 to position total cost closer to the root than unit-cost as currency, the measurement unit of the former is “simpler” than currency per unit quantity, the measurement unit of the latter. Since the rules of formation for the surrogate representation are only informally stated, it is not clear to us if the ordering rules described in the paper are general and will transfer beyond the set of examples described in the paper.

Given a new problem specified in terms of these representations, the approach used to transform it to a linear programming model consists of discovering similarity to a pre-existing case in a library. Similarity is determined by computing a similarity measure between the entities in a problem and the entities in a case. This measure is computed by matching a row in the feature grid representation of the problem with a row in the feature grid of a case. The formula used to compute the measure is based on a scale proposed by Tversky [50]). The formula used is:

$$
\text { similarity   measure } = \sum_ {i} \delta_ {i} / m.
$$

where $\delta_{i}$ is the similarity value assigned to a column i that is shared by the entities (rows) in the feature grid under consideration. The similarity value is 1 if the columns being compared have the same cell value, i.e., known, unknown, or unspecified, and 0 otherwise. When multiple mappings between rows in the feature grid are possible, the mapping with the highest similarity score is chosen. An example of a mapping between a product-mix problem and a process selection problem from the paper is given below. The elements being mapped to one another are the entities (row labels of the respective feature grids).

<table><tr><td>Product-mix</td><td>Process selection</td></tr><tr><td>ROOT</td><td>ROOT</td></tr><tr><td>PRODUCT</td><td>LINK(P,P)</td></tr><tr><td>RESOURCE</td><td>RESOURCE</td></tr><tr><td>MANUFACTURING</td><td>LINK(P,P,R)</td></tr></table>

For each pair of mapped entities, cell values in the feature grid are compared and paired together. Recall that cell values either are known (denoted by a lower case entry), unknown (denoted by a upper case entry), or unspecified (denoted by the symbol U). Cell values are compared using these interpretations of the entries. Since the cell entries appear in equations of the model associated with the case, establishing the mapping between cell entries enables transfer of those parts of the model which contain matching elements.

When the similarity mapping is perfect, this analogical transfer creates a complete model for the problem. When the similarity mapping is not perfect, the model may need to be repaired. A small collection of heuristics that help with model repair are introduced in the paper. However, the extent to which these heuristics are capable of autonomously repairing the model is not clear. As noted by the author, the user of the system is responsible for performing a final check on the model.

While the paper presents an interesting new approach, it also raises several questions that need to be thought through to create a robust implementation of the analogical method. For instance, given a library of cases, how should one choose among the several cases that may be candidates for analogical modeling? What is a systematic method to compute an overall similarity measure between a problem and a case? It is not clear how the proposed measure of similarity between entities can be used to compute such an overall similarity measure. The rules of formation for the three problem related representations need to be carefully studied to ensure that they are broadly applicable. Finally, there is no precise description of the scope of the system, i.e., what are the kinds of models that can and cannot be formulated or is this a truly domain independent approach.

## 4.2. Ma, Murphy, Stohr, and Asthana

The work of Ma, Murphy, Stohr, and Asthana adopts a fundamentally different LP model construction approach to that of Liang. While Liang applies anological modeling techniques, Ma et al. employ an approach that synthesizes the structure of the linear programming model. In $[37,33]$ , they discuss a philosophy for model construction, and present details of systems designed to assist users in the formulation of large linear programs. An initial version of the system, LPFORM, is described in $[37]$ , a graphics interface to the system is discussed in $[33]$ , and a more recent version called LPGRAPH is described by Asthana, Murphy, and Stohr in $[2]$ .

The key concept underlying their approach is the use of the structural properties of the problem in the construction process. While not based on a formal cognitive study, the approach prescribes an input problem specification in terms of blocks which denote activities such as production and blending, and links which represent transformations in space, or time. This input is then synthesized into an LP model using rules that encode the relationships between the known types of activities. Thus the block and links may up the surrogate representation used in this approach. In an early version of the system, LPFORM, the surrogate representation were realized externally as text. A recent version incorporates a graphics interface $[33,2]$ . Since the surrogate representation is not grounded in any specific domain, the system does not support problem specification as the domain-specific systems do. To obtain the target LP representation, the system employs a refinement strategy in which the blocks become successively more detailed. Synthesis rules that encode knowledge about the interactions between the various activity types and submodel structures are used to construct the mathematical formulation. The authors characterize this process as being similar to solving a puzzle.

An important feature of this approach is the ability to specify large LP models using a combination of submodels and typed activities using graphical constructs that exploit the predominantly network sub-structures present in linear programming models. The complete model is built by separately developing and then combining several model pieces. The authors believe that such a system, when developed, would considerably automate model validation and documentation, improve the quality of sensitivity analysis, and assist in teaching linear programming. Finally, the system is domain-independent, and can potentially be applied in a variety of contexts.

We believe that this approach is best suited to the needs of modeling experts (also noted by the authors in [37]) since it requires the user to be able to describe a problem in terms of abstractions such the transformations in space, form, and time. Further, as noted by Binbasioglu and Jarke [9], “the structural knowledge (referring to the domain-independent approach) supports you in formulating a constraint but it does not tell you which constraint to formulate” (italics added). Given the range of users that model management systems aim to support, we believe that both domain-specific and domain-independent strategies are required.

The principal limitation of this approach (and one shared by all currently existing systems) is its use of a fixed set of terms (e.g., production, blending) which implicitly compile a collection of assumptions in model building rules. For instance, when a user declares a blending activity to be part of his problem, a pre-specified model associated with that type of activity is used by the system. The implicit set of assumptions associated with this model may not be appropriate for the user's problem. However, the system does not have access to the information required to diagnose and remedy this problem. An argument against representing and reasoning with assumptions has been that in general it is expensive and slow. While we agree with the argument, we believe that the system should have access to this detailed information, and be equipped to reason with it as required by the task at hand.

The work we have discussed thus far has been representative of domain-independent model construction approaches. We now turn to a discussion of the domain-specific model construction approaches.

## 4.3. Binbasioglu and Jarke

Binbasioglu and Jarke discuss a domain-specific approach to computer-assisted linear programming (LP) model construction in the production management domain [9]. While the approach is not based on a formal cognitive study, the cognitive model assumed consists of the following key steps:

\- context identification, or identifying the problem type from the problem description,

\- problem formulation, involving instantiating the context, and associating context variables with those of a stored LP model, and

\- model instantiation, involving accessing or computing the parameters for the model.

The surrogate representations consist of domain concepts and their inter-relationships stated using an object-oriented metaphor. While the prototype described in the paper supports a textual representation, a graphical external representation could be readily supported. Domain knowledge, represented using aggregation and generalization heirarchies, is used to guide users in problem specification. This interaction with the user helps the user identify the “boundary”

of the problem they wish to model. Problem specification is followed by problem decomposition in which a collection of meta rules which encode the structured design principle of “minimum coupling” and “maximum cohesion” are used. The mathematical model is then formulated using a collection of stored constraints that are part of the “structural knowledge” of the system. This process consists of binding symbolic objects (such as variables, parameters, and index sets) that make up the mathematical model with the domain objects. Following this instantiation, the parameters of the model are either accessed or computed to create the LP model instance.

To summarize, a defining characteristic of the Binbasioglu and Jarke approach is the use of semantic information in conjunction with the structural model building knowledge. This general principle is also seen in the work of Krishnan [27,28] and Raghunathan [40]. However, the use of the stored model fragments to define the structural model building knowledge appears to limit the scope of the system. When problem formulations require a model which is not available in the stored model base, the system has no recourse to deeper knowledge about how to construct the models.

## 4.4. Krishnan, Jones, and Bhargava

In [29,27,28,23,8], Krishnan, Jones and Bhargava discuss representation and reasoning issues in model construction. These papers are based on the initial work of Krishnan on domain-specific approaches for LP model construction in the production, distribution, and inventory planning domain. The authors discuss systems implemented using these ideas. The intended users are model builders who have a great deal of knowledge about their domain, but who lack the training in mathematical modeling to conceptualize their problems as mathematical models.

The concept underlying this approach is that model construction involves the transformation of a high level, qualitative description, stated in terms of domain concepts and their inter-relationships into an LP model. First, the qualitative problem specifications are classified by type, using a context-free grammar that encodes an inductive definition of the set of problem types known to the system. Currently these are a large set( widgets }
subtype( widgets,product)
ins-of(steel- widgets, widgets)
set(steel-plates)

subtype(steel-plates,resource)
relation(steel-used-to-produce- widgets)
domain(steel-used-to-produce- widgets,[steel, widgets])

function(widget-production-level)
domain(widget-production-level, widgets)
range(widget-production-level,real-number)

Fig. 7. A PM\* problem specification.

subset of production, distribution, and inventory planning problems. Once the problem type is identified, a set of domain-independent model building rules relevant to the problem type is applied to the problem specification to construct LP models. Currently only standard objectives such as cost minimization and profit maximization are known to the system. A small subset of a production planning problem specification in the PM\* language is shown in Figure 7.

While no formal cognitive study was conducted, the underlying cognitive model is that (a) intended users conceptualize problems in terms of domain concepts and inter-relationships, and (b) a small set of domain-independent model building rules can be applied to synthesize the mathematical structure of the model. These model building rules are primitive rules that embody a first-principles approach to model construction. An example of such a rule is material balance, which requires that the sum of a set of inputs to a system be greater than or equal to the sum of the set of outputs. The surrogate representation is in terms of domain concepts, such as products, raw-materials and their inter-relationships. While early versions of the system realized the surrogate representation as sentences of predicate logic languages [29], Jones and Krishnan [23] have employed attributed graphs to implement this representation in a graph-based modeling system. Since the surrogate representation is in terms of domain objects, domain knowledge is used to help the user in problem specification. For instance, if the user indicates that production is an activity relevant to his problem, the system would use its knowledge about the relationships between production, sales and storage to focus the user's attention on related processes. Further, in the graph-based implementation tion a syntax-directed editor is used to support problem specification.

An advantage of this approach is that it allows a user to define a problem in terms of domain objects. The context-free grammar which encodes the systems knowledge about problem types can be used to either classify a given problem into one of the known problem types, or to provide useful feedback on problems beyond its scope. For the class of problems within its scope, the model construction rules relevant to each problem type have been shown to be sufficient to construct “correct” models $[27]$ . This offers the potential to study the computational complexity of the key tasks in computer-assisted model construction.

We believe that the principal shortcoming of this approach is that it uses model building rules which compile a great deal of information. Human experts are aware of the assumptions underlying models and model building rules and are able to reason at the level of granularity demanded by the modeling task. To illustrate our point about information tacitly compiled into model building rules, consider the following rule in the PDM system [28].

IF F is the flow from a source S to a sink H AND the supply capacity at S is C AND the demand requirement at H is D THEN sum(I) F(I,J) ≤ C and sum(J) F(I,J) ≥ D

This rule encodes implicit assumptions such as a)

![](/api/attachments/FYNUKF43/fulltext/images/0861c381e0d272e9198dddb4895ae19276357d5c145fabdaf7f98f461732b9d4.jpg)  
Fig. 8. A model of the expert model formulation process.

there is only a single commodity, and b) there is no loss in shipment. This presents a problem when the system has to formulate models for which these implicit assumptions are not appropriate. In the absence of an explicit set of assumptions, and a calculus for reasoning with assumptions, the ability of the system to make and alter commitments to assumptions is limited.

## 4.5. Raghunathan

In [40], Raghunathan presents MODFORM, one of the most comprehensive computer-assisted model construction systems to date. It is domain-specific and is intended to support users untrained in mathematical modeling. There are several distinctive features of this work. One, this system is based on systematic cognitive modeling studies conducted with expert mathematical programmers. Two, unlike the other systems that were designed only to support LP model formulation, it can formulate linear programming, mixed integer linear programming, and non-linear programming models that arise in the production and distribution planning domain. Finally, a belief maintenance system is used to maintain justification for various modeling decisions and to support model maintenance [41].

scription (in terms of domain concepts) into an appropriate mathematical model. The cognitive model used in this approach is derived from protocols of model construction collected from expert modelers. It presumes that users conceptualize a problem in terms of domain objects and their inter-relationships, and that this problem description is converted into a qualitative model of constraints that need to be formulated, before domain independent model construction rules are applied to construct the mathematical model. The surrogate representation used in this approach is in terms of domain objects and their inter-relationships. Externally, it is realized in the implementation as a textual language.

The process of developing the surrogate representation is supported using domain knowledge, which encodes relationships between the various activities (e.g., selling and transportation) that characterize the domain. The process of constructing the appropriate mathematical model consists of two major steps and is based on detailed cognitive studies of expert mathematical programmers (see Figure 8).

The concept underlying Rahgunathan's approach is similar to Krishnan's [28], and involves the transformation of a high-level problem de-

First, the problem description is transformed into a qualitative model (see Figure 9). This transformation is accomplished using a set of rules that generate constraints about object types present in the problem statement. For instance, if an object of type resource is present in the problem statement, then a rule is used to infer the

1. utilization-of-light-oil ≤ availability-of-light-oil

2. utilization-of-heavy-oil ≤ availability-of-heavy-oil

3. outflow-of-premium-petrol ≤ inflow-of-premium-petrol

4. outflow-of-regular-petrol ≤ inflow-of-regular-petrol

5. functional relationship for amount of regular petrol produced

6. functional relationship for amount of premium petrol produced

7. quality relationship for premium petrol

8. quality relationship for regular petrol

9. quality-of-regular-petrol $\geq$ minimum-quality-of-regular-petrol

10. quality-of-premium-petrol ≥ minimum-quality-of-premium-petrol

11. IF utilization-of-light-oil ≥ 30000 THEN utilization-of-heavy-oil ≥ 50000

12. profit by selling regular petrol

13. profit by selling premium petrol

Fig. 9. Qualitative model.

constraint that resource utilization should be less than resource availability. Second, the qualitative model is transformed into the mathematical model using model construction rules. These are rules that assign variables and actually construct the mathematical forms that correspond to the constraints in the qualitative model.

Consider, for instance, the qualitative constraint,

$$
\text { t   i   l   i   z   a   t   i   o   n   -   o   f   -   l   i   g   h   t   -   o   i   l } \leq \text { a   v   a   i   l   a   b   i   l   i   t   y   -   o   f   -   l   i   g   h   t   -   o   i   l }
$$

This qualitative constraint follows from the eclaration that light oil is a type of resource. The mathematical formulation of this constraint is obtained by refining each of the terms in the constraint. Let us say that the problem description also stated that light oil is used to produce regular and premium gasoline and that availability of light oil is known. Since the availability is known, the term on the right hand side can be replaced by this number. However, the term on the left hand side needs to be refined to relate it to the utilization of light oil in the production of regular and premium gasoline respectively. This results in:

$$
\begin{array}{l} \text {   tilization   -   of   -   light   -   oil   } = \text {   utilization   -   of   -   light   -   oil   -   in   regular   -   gasoline   +   utilization   -   of   -   light   -   oil   -   in   premium   -   gasoline   } \end{array}
$$

The right hand side of these terms is further defined, and variables are assigned to attributes. A model building rule is used to formulate the expression

$$
^ {\prime} = \mathrm{A1} * \mathrm{X1} + \mathrm{A2} * \mathrm{X2},
$$

where Y is the utilization of light oil, A1 is the rate of utilization of light oil in the production of regular gasoline, A2 is the rate of utilization of light oil in the production of premium gasoline, and X1 and X2 are the production levels of regular and premium gasoline respectively.

Finally, the system documents the model building process, and associates with each component of the mathematical model, a dependency network of rationales for modeling decisions. These are the rationales that relate the components of the mathematical model to the underlying qualitative problem description. This explicit documentation of modeling rationale can be queried and used to promote model understanding, and provides the dependency information required to support model maintenance.

In summary, we find that this is the most systematic, broadly applicable, and in-depth domain-specific approach for computer-assisted model formulation. It combines coverage of several model classes, a model construction strategy based on insights gained from cognitive studies, and a robust system to manage the effects of changes to decisions made during the course of model construction. It shares with other approaches, however, a reliance on model-building rules that compile a great deal of modeling semantics into keywords such as blending and production. In fact, concepts such as blending and production can be thought of as a collection of several smaller substructures, each of which represent pieces of modeling knowledge in some given context or application domain. However, such keywords are atomic in this system, which means that the system does not have procedures to reason with the substructures implicit in those keywords. It is clear that to extend the coverage to a broader class of models and domains, the system must reason at a finer level of granularity than with these high-level keywords.

## 5. Discussion and extensions

Our review focused on knowledge-based model construction systems, but we also pointed out other mechanisms, e.g., algebraic modeling languages, for aiding model construction. Of course, a number of questions remain to be answered. Where exactly does the state of the art in computer-aided model construction stand? How should it be improved? What issues must be looked at in future research in computer-aided model construction? We examine these questions in this concluding section. Specifically, we note that research in computer-aided model construction has concentrated on two issues: understanding the cognitive aspects of model construction, and designing and implementing systems that support the construction of specific classes of mathematical models in particular domains. And a third, we believe, is crucial: validation of the usefulness of these systems. We summarize the results of research in these three categories, and raise issues for further investigation.

First, in the cognitive aspects of model construction, several experimental studies have examined the early stages of model formulation. These studies have mostly used variants of the thinking-aloud protocol technique $[13]$ , and have targeted the construction of mathematical programming models. In a typical experiment, subjects are given a specific model formulation task and are asked to verbalize their thought process in addressing the task. One result has been the identification of differences in the abilities of expert and novice mathematical modelers to recognize model classes (e.g., $[38]$ ). Another outcome is the development of “process models;” the knowledge-based model construction systems MODFORM $[40]$ and MFS $[26]$ are designed on the basis of such models. Therefore research in the cognitive issues of model construction has been useful in system design and in the validation of intuitions about the nature of the modeling process. However, several questions remain to be investigated, two of which we discuss below.

One, all the process modeling work on model construction has been based on protocols collected using textbook problems or cases. These textbook problems typically contain all the information necessary to formulate the model. This prevents the experiments from collecting data on processes that modelers use to make assumptions – something that modelers often have to do in practice. As we noted in our review, the collection of this data could help address a shortcoming of existing model construction systems – their inability to represent and reason with assumptions. A methodological question that needs to be addressed is how should the task environment be designed to collect this type of data.

Two, the scope of the process modeling work has been limited to the early stages of model construction. No work is reported on the tasks a modeler performs during model solution and debugging. The work most closely related to this is the study of debugging of computer programs $[24,48]$ . These studies have investigated debugging behavior using programs which either contain bugs planted by the researchers or which contain bugs caused by other programmers. Some work has also studied the debugging of self-generated errors by programmers $[24]$ . This research has led to characterizations of the debugging process in terms of bug evaluation episodes and the contexts in which they were triggered. These in turn have led to the development of tools to support the program debugging process. Similar studies need to be conducted in the mathematical modeling context to develop a more complete and detailed understanding of the modeling process. While fundamental differences between programming and mathematical modeling prevent direct application of the results, we believe that the approach used to study debugging in the programming context could provide a guiding framework. The interested reader is referred to $[25]$ for a more complete discussion.

Second, consider the design and implementation of prototype knowledge-based model construction systems. An area critical to the design of computer-aided model construction systems is the rôle of assumptions in the modeling process. A model is often defined as a collection of assumptions, in which case the ability to represent and reason with assumptions should be fundamentally useful in model construction. Yet, few modeling languages and model construction systems provide useful ways to represent, and to reason with, assumptions. Indeed, one of the chief drawbacks shared by the systems examined in this paper is their lack of attention to modeling assumptions. It then becomes relevant to ask how should assumptions be represented in a language for model management, and what inference mechanisms would yield the desired functionality? In [7] we argued that the process of reasoning with assumptions during model construction was non-monotonic: modelers make and revise assumptions, and a change in an earlier assumption might cause the invalidation of previous conclusions about the model's form. That paper suggested that non-monotonic reasoning techniques would better model the reasoning process, would provide better inferences to support model building, and would also be useful in introducing and maintaining modeling knowledge. That still begs the question of how, and at what level of detail, assumptions should be represented in a formal language. Recent work in the qualitative reasoning literature on systems for constructing large scale qualitative models address some of these questions. The work of Addanki et al. [1], and that of Falkenhainer and Forbus [14] are particularly relevant. In Addanki's work, models are created using different assumptions and organized into a graph of models. In these graphs the arcs represent changes in the assumptions required to switch from one model to another. Falkenhainer and Forbus specifically represent assumptions at different levels of granularity, and from different points of view. They then argue for the use of this information to help select models to answer specific questions.

Finally, we note that most model construction systems have been tested on a limited set of examples, and essentially are used by the authors themselves. There is little evidence of the operational impact of these systems, or of their use in a real model-building environment. That raises the question of whether such systems really increase modeling productivity, and highlights the need for empirical research in testing the usefulness of these systems. Would they or do they really help people build better models? Do they help modelers create better documentation of the process and its results? Do they help them build models faster? Clearly these questions can only be answered after rigorous and systematic testing, but it is an open question as to how one should evaluate systems for (such complex tasks as) model construction.

To our knowledge, the only prototype system that has been evaluated to some degree is MODFORM [40]. The evaluation involved a laboratory experiment in which students were given textbook problem sets, and were asked to build models with and without MODFORM. The models created by the students under each scenario were graded, and the system was evaluated in terms of the increase in grade assigned to the student. While this simple experiment did prove useful information about MODFORM, it raises questions about a general method to evaluate these types of systems. For most realistic problems, the “goodness” of “correctness” of a model is subjectively determined taking into account a variety of organizational constraints.

Recognizing these difficulties, Piela et al. [52] suggest that the usefulness of a technology designed to support complex tasks should be studied by observing people using it to solve real problems in their own workplace, rather than in controlled laboratory settings. Piela et al. summarize their point of view by stating that for tasks which are complex and for which an underlying theory is not established, the “traditional dichotomy between system development (with its emphasis on technology and the system designer) and system evaluation (with its emphasis on technology and the user) is inappropriate if the goal is to explore a technology that requires a user to significantly reconceptualize his or her understanding of a task.”

To summarize, computer support for model construction has been realized in a variety of forms and at several stages in the model construction process. In this paper, we have attempted to provide a general characterization of the ways in which the process of model construction can be facilitated, and have also analyzed specific systems that aim to provide such support. We have also raised several research questions that need to be investigated. Answers to these questions will contribute to the development of an empirically grounded theory of computer-aided model construction.

## Appendix A

The case of Delco

On January 15, 1979, Mr. Sam Watson, head of the Operations Analysis Division of Delco Oil Company was preparing a production plan for the company's refinery in Louisiana.

Background. Petroleum refining is one of the largest manufacturing industries in the United States. In 179, there were over 300 refineries in the United States processing a total of more than 18 million barrels of crude oil a day. Crude oil is a complex mixture of chemical compounds. The refining process separates crude oil into components that eventually yield gasoline, fuel oil, asphalt, jet fuel, lubricating oil, and many other petroleum products. Refineries strive to operate at peak economic efficiency, taking due account of the demand for these products.

At the end of 1978, Mr. Chauncey Andrews, Vice-President of Operations at Delco Oil Company, had examined the gasoline production process at the Louisiana refinery. He expressed some concern about the manner in which gasoline was separated from crude oil and about the allocation of end products. Andrews asked Sam Watson to study the situation.

The refining process. The refining process can be basically described as follows. Gasoline is produced from crude oil by either a distillation process alone or by a distillation process followed by a catalytic cracking process. The outputs of these processes are blended to obtain different grades of gasoline.

The distillation process at Delco's refinery separates gasoline from other components by heating crude oil under pressure until the gasoline vaporizes. The vapors are then collected and cooled in a condenser to produce distillate. Delco obtains crude oil at a cost of \$12.00 a barrel. The distillation tower uses 5.2 barrels of crude oil to produce one barrel of distillate and 4.2 barrels of other petroleum by-products. Delco currently sells these other products for \$11.8 a barrel. Delco's distillation tower can produce up to 60,000 barrels of distillate output. Some distillate will be blended into gasoline products; some will become "feedstock" for the catalytic cracker.

The catalytic cracking process utilizes high temperatures to break (or “crack”) heavy hydrocarbon compounds into lighter compounds. This process produces high quality gasoline stock from the feedstock. Delco’s catalytic cracker requires 2.2 barrels of distillate to produce one barrel of gasoline stock and 1.2 barrels of petroleum by products. These by products currently sell for \$19.48 a barrel. The catalytic cracker can produce up to 20,000 barrels of gasoline stock per day at an operating cost of \$4.60 per barrel output.

The Catalytic cracker unit also requires a coolant throughout its operation. The coolant costs \$2.00 per barrel and the cracker unit requires 20,000 barrels of the coolant throughout its operation. The octane rating of a gasoline measures its ability to burn smoothly without exploding. The distillate produced by Delco's distillation tower has an octane rating of 84, while the gasoline stock from the catalytic cracker has an octane rating of 94. Delco's gasoline refining process ends by blending distillate and cracker stock to form regular and premium gasoline, which have required octane ratings of at least 86 and 92 respectively. Delco sells its regular gasoline for \$20.10 per barrel and its premium gasoline for \$22.90 per barrel.

The final gasoline products are pumped from the Delco oil refinery in Louisiana via two small pipelines to several storage and distribution facilities in the eastern United States. One pipeline carries only regular gasoline and the other carries only premium gasoline. Each pipeline can handle up to 25,000 barrels a day. The pipelines are not owned by Delco and the amount of lease for these is \$25,000 per month per pipeline. The market has recently been such that Delco could sell as much of either gasoline as the pipes can carry and Watson expected this situation to continue in the near future.

Delco oil company has also decided to expand its distillation equipment. The purchase and installation of the new distillation equipment will cost \$700,000 and will increase the distillation tower's capacity to 75,000 barrels of distillate per day. The expansion would require an additional maintenance cost of \$2500 per day for distillation equipment.

But the increased capacity might require putting in one more pipeline. Since leased pipelines with fixed lease amounts are no longer available, Delco has decided to lease a pipeline with variable lease amount. The cost structure for the new pipeline is shown in exhibit 1. Since only one type of gasoline can be sent through a pipeline, the problem of what type should be sent through the new pipeline remains. Mr. Sam Watson decided to study the situation carefully to identify whether any OR techniques can be applied. He knows that suitable assumptions can be made before deciding on the model and that he can validate the assumptions with the management later.

## References

[1] Addanki, S., R. Cremonini, and J.S. Penberthy, “Reasoning About Assumptions in Graphs of Models,” in D.S. Weld and J. de Kleer (eds.), Readings in Qualitative Reasoning About Physical Systems, Morgan Kaufman, San Mateo, CA, 19990, pp. 546–552.

[2] Asthana, A., F. Murphy, and E. Stohr, “A Language for Formulating Linear Programs,” Working Paper, Information Systems Area, New York University, 1990.

[3] Baker, K., L. Ball, P. Culverhouse, I. Dennis, J. Evans, P. Jagodzinski, P. Pearce, D. Scothern, and G. Venner, “A Psychologically Based Intelligent Design Aid,” in [19], pp. 21–40.

[4] Bhargava, H.K., R. Krishnan, and S. Mukherjee, “On the Integration of Data and Algebraic Modeling Languages,” Annals of Operations Research, 1992, forthcoming.

[5] Bhargava, H.K., and S.O. Kimbrough, “Model Management: An Embedded Languages Approach,” Decision Support Systems, 1993, forthcoming.

[6] Bhargava, H.K., “A Logic Model for Model Management: An Embedded Languages Approach,” Ph.D. Dissertation, University of Pennsylvania, 1990.

[7] Bhargava, H.K., and R. Krishnan, “Reasoning with Assumptions, Defeasibly, in Model Formulation,” in J.F. Nunamaker Jr., (ed.), Proceedings of the Twenty-Fifth Annual Hawaii International Conference on System Science, Vol. III, IEEE Computer Society Press, Los Alamitos, CA, 1992, pp. 407–414.

[8] Bhargava, H.K., and R. Krishnan, “A Formal Approach for Model Formulation in a Model Management System,” in J.F. Nunamaker Jr. (ed.), Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, Vol. III, IEEE Computer Society Press, Los Alamitos, CA, 1990.

[9] Binbasioglu, M., and M. Jarke, “Domain Specific DSS Tools for Knowledge-based Model Building,” Decision Support Systems 2, pp. 213–223, 1986.

[10] Bischop, J., and A. Meeraus, “On the Development of a General Algebraic Modeling System in a Strategic Planning Environment,” Mathematical Programming Study 20, 1982, pp. 1–29.

[11] Chandrasekharan, B., J. Smith, and J. Stott, “Use of Generic Task Languages for Modeling Domain Knowledge and Problem Solving for Knowledge System Construction,” Communications of the ACM, September 1992, forthcoming.

[12] Clements, R.R., Mathematical Modeling: A Case Study Approach, Cambridge University Press, New York, NY, 1989.

[13] Ericson, K.A., and H.A. Simon, Protocol Analysis: Verbal Reports of Data, MIT Press, Cambridge, MA, 1984.

[14] Falkenhainer, B., Forbus, K., “Setting up Large-Scale Qualitative Models,” Proceedings of the American Association of Artificial Intelligence, pp. 01–306, 1988.

[15] Fourer, R., D. Gay, and B.W. Kernighan, “A Mathematical Programming Language,” Management Science 36:5, 1990, pp. 519–554.

[16] Gass, S., “Managing the Modeling Process: A Personal Reflection,” European Journal of Operations Research 3:1, 1987.

[17] Geoffrion, A.M., “An Introduction to Structured Modeling,” Management Science 33:5, (1987).

[18] Greenberg, H.J., “A Functional Description of ANALYZE: A Computer-assisted Analysis System for Linear Programming Models,” ACM Transactions on Mathematical Modeling Software 9:1, 1983, pp. 18–56.

[19] Hagen, P.J.W. ten, and P.J. Veerkamp (eds.), Intelligent CAD Systems III: Practical Experience and Evaluation, Springer Verlag, New York, 1991.

[20] Holsapple, C.W., S. Park, and A.B. Whinston, Framework for DSS Interface Development, Research report, MSIS, University of Texas, Austin.

[21] Jones, C.V., “An Introduction to Graph Based Modeling Systems, Part II: Graph Grammars and the Implementation,” ORSA Journal on Computing 3:3, 1991, pp. 180–206.

[22] Jones, C.V., "An Introduction to Graph Based Modeling

Systems, Part I: Overview," ORSA Journal on Computing 2:2, 1990, pp. 136–151.

[23] Jones, C., and R. Krishnan, “A Visual Syntax Directed Environment for Automated Model Development,” SUPA Working Paper, Carnegie Mellon University, 1992.

[24] Katz, I., and J. Anderson, “Debugging: An Analysis of bug-location Strategies,” Human Computer Interaction, Vol. 3, pp. 351–399, 1988.

[25] Krishnan, R., P. Piela, and D. Steier, “Interactive Debugging of Mathematical Models,” Working Paper, Engineering Design Research Center, Carnegie Mellon University, 1992.

[26] Krishnan, R., X. Li, and D. Steier, “Development of a Knowledge-based Model Formulation System,” Communications of the ACM, forthcoming, September 1992.

[27] Krishnan, R., “A Logic Modeling Language for Model Construction,” Decision Support Systems 6, pp. 123–152, 1990.

[28] Krishnan, R., “PDM: A Knowledge-based Tool for Model Construction,” Decision Support Systems 7, pp. 301–304, 1991.

[29] Krishnan, R., “Automated Model Construction: A Logic-based Approach,” Annals of Operations Research, Vol. 21, pp. 195–226, 1989.

[30] Li, X., R. Krishnan, and D. Steier, “MFS: A Study of Model Formulation in SOAR,” Working Paper 5–91, SUPA, Carnegie-Mellon University, revised, August 1991.

[31] Liang, T.P., “Development of a Knowledge-based Model Management System,” Operations Research, Vol. 36, No. 6, pp. 849–863, 1988.

[32] Liang, T.P., “Modeling by Analogy: A Case-based Approach to Automated Linear Program Formulation,” in Proceedings of the Twenty-Fourth Hawaii International Conference on System Sciences, pp. 276–283, Kuaui, Hawaii, 1991.

[33] Ma, P., F. Murphy, and E. Stohr, “A Graphics Interface for Linear Programming,” Communications of the ACM, Vol. 32, No. 8, pp. 996–1012, 1989.

[34] Martin, J., and C. Mcclure, Structured Techniques: The Basis for CASE, Prentice-Hall, Englewood Cliffs, NJ, 1988.

[35] McClure, C., CASE is Software Automation, Prentice-Hall, Englewood Cliffs, NJ, 1989.

[36] Muhanna, W., “A Systems Framework for Model Management in Organizations,” Ph.D. thesis, University of Wisconsin, Madison, 1987.

[37] Murphy, F., and E. Stohr, “An Intelligent System for Formulating Linear Programs,” Decision Support Systems 2, pp. 39–47, 1986.

[38] Orlikowski, W., and V. Dhar, “Imposing Structure on Linear Programming Problems: An empirical investigation of Expert and Novice Modelers”, Proceedings of the National Conference on Artificial Intelligence, Philadelphia, PA, 1986.

[39] Piela, P., R. McKelvey, and A. Westerberg, “An Introduction to ASCEND: Its Language and Interactive Environment,” in J.F. Nunamaker Jr. (ed.), Proceedings of the Twenty-Fifth Annual Hawaii International Conference on System Sciences, Vol. III, IEEE Computer Society Press, Los Alamitos, CA, 1992, pp. 449–461.

[40] Raghunathan, S., “An Artificial Intelligence Approach to

the Formulation and Maintenance of Models," Ph.D. thesis, University of Pittsburgh, 1990.

[41] Raghunathan, S.J. May, and R. Krishnan, "Computer-based Model Development: A Belief Maintenance Approach," Working Paper, Artificial Intelligence Laboratory, University of Pittsburgh, 1992.

[42] Rich, C., and R.C. Waters, “Automatic Programming: Myths and Prospects,” Computer Vol. 21, No. 8, pp. 40–51.

[43] Robertson, D., A. Bundy, M. Ufschold, and B. Muetzelseldt, “The Synthesis of Simulation Models from High-level Specifications,” Department of Artificial Intelligence Research Paper No. 313, University of Edinburgh, U.K., 1987.

[44] Saaty, T., and J. Alexander, Thinking with Models: Mathematical Models in the Physical, Biological, and Social Sciences, Pergamon Press, New York, NY, 1981.

[45] Schneiderman, B., Designing the User Interface, Addison-Wesley, Reading, MA, 1987.

[46] Sklar, M.M., R.A. Pick, G.B. Vesprani, and J.R. Evans, "Eliciting Knowledge Representation Schema for Linear Programming." D.E. Brown and C.C. White (eds.), Oper-

ations Research and Artificial Intelligence: The Integration of Problem Solving Strategies, Kluwer, 1990, pp. 279–316.

[47] Sklar, M.M., and R.A. Pick, “A Knowledge Engineered Linear Programming Formulation Assistant,” in J.F. Nunamaker Jr. (ed.), Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, Vol. III, IEEE Computer Society Press, Los Alamitos, CA, 1990, pp. 269–278.

[48] Spohrer, J., E. Soloway, and E. Pope, “A Goal-Plan Analysis of bugy PASCAL Programs,” Human Computer Interaction, Vol. 1, pp. 163–207, 1985.

[49] Treur, J., “A Logical Framework for Design Processes,” in [19], pp. 3–20.

[50] Tversky, A., “Features of Similarity,” Psychological Review 84:4, pp. 327–352.

[51] Xenakis, J., "CASE: Many Tools, Limited Choices," Information Week, Dec. 10, 1990, pp. 22–28.

[52] Piela, P., B. Katzenberg, R. Mckelvey, “Integrating the User into Research on Engineering Design Systems”, Forthcoming in Research on Engineering Design.
