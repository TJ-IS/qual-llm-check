---
otero_id: 16876
otero_key: "7WTA3S6S"
title: "Logic-based formula management strategies in an actuarial consulting system"
authors: "Taracad Sivasankaran; Matthias Jarke"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90244-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Logic-Based Formula Management Strategies in an Actuarial Consulting System

Taracad SIVASANKARAN and Matthias JARKE
Computer Applications and Information Systems Area, Graduate School of Business Administration, New York University, 90 Trinity Place, New York, NY 10012, USA

In many decision support systems, multiple decision methods and models must be combined for solving a complex problem. Expertise is required for selecting, adapting and coordinating appropriate models. This paper describes the design and implementation of a knowledge-based model management system called the Actuarial Consulting System (ACS). The ACS supports actuaries in making pricing decisions in the domain of life insurance. Actuarial knowledge is organized using a graph formalism called Formula Derivation Network (FDN), represented in Prolog as a hierarchy of predicates. On the user level, a Problem Analyzer converts a problem specification by the user into a search problem on the stored collection of FDNs. Using different search strategies, including human expert rules, the Surface Planner generates an efficient solution strategy (sequence of models). At the lowest level, a Plan Executor retrieves or requests model data and issues appropriate function calls to a subroutine library.

Keywords: Model Management; Logic-based Decision Support Systems; Actuarial Science; Life Insurance; Hierarchical Knowledge Base Management; Expert Systems

## 1. Introduction

A research effort at New York University investigates the integration of artificial intelligence (AI) methods into existing decision support systems (DSS) [1]. One part of the project studies the interaction between expert systems and large existing databases [2,3]; a second part studies specific aspects of business expert systems, focusing on expert systems for insurance underwriting [4]. This paper describes work on a third subproject that investigates the combination of AI methods with quantitative models, in particular, intelligent model management.

In complex decision situations, it will often be necessary to coordinate the application of multiple decision models for solving a problem. Decision Support Systems need a model management component $[5,6]$ that handles the tasks of identifying appropriate models from a problem description, sequencing their application, and instantiating them with the necessary data.

The paper describes the design and implementation of a prototype model management system that supports actuaries in their work. In an insurance company, actuaries are responsible for evaluating the risks of providing insurance for life contingencies, such as death, disability, or retirement. The system – called the Actuarial Consulting System (ACS) – structures life insurance problems by organizing appropriate formulas and models, evaluating premiums, and explaining possible solution methods. The focus of the present paper are the model selection and combination capabilities of the system; details of other features are provided in [7].

![](/api/attachments/7WTA3S6S/fulltext/images/d6f91da8c23949f5642a4f438380df7f8725a4fbdadc1607c5581ef96444944b.jpg)  
ment in actuarial consulting systems.

![](/api/attachments/7WTA3S6S/fulltext/images/e5dc03f751ca9e92684defb373302395a6ffe63e6cbd52768dd1f8968997141a.jpg)

Several other authors have addressed model management issues. Following [8], three stages of model management systems can be distinguished. In the simplest case, the user must procedurally state an algorithm to solve the problem at hand. In the second stage, the user may select among a set of pre-specified models provided by the system. Several high-level languages have been proposed for this purpose. A good example is relational model management [9] which views a model as a relation between input and output data and implements model sequences by joins between these relations.

The ACS uses a similar, although graph-based high-level model description but actually falls into the third category of [8]: it automatically selects a combination of models, guided by its knowledge base and by a high-level problem specification provided by the user. This approach requires the use of AI techniques. In principle, a pure resolution-based system such as Prolog [10] could be used for this task; see also [11] for an exploration of this option.

However, it has been observed that pure resolution systems do not provide sufficient control of the solution planning process [12]. For example, it may turn out to be very costly to execute models concurrently with the reasoning process if the results may subsequently have to be discarded due to backtracking.

Consequently, the ACS - although implemented in Prolog - employs a more hierarchical control structure. On a surface level, a planner selects applicable models and manipulates them into a feasible and efficient solution plan. This level uses a graph-based knowledge representation that facilitates the search for solution strategies and the evaluation of alternatives. No number-crunching is involved at this level and Prolog's unification capabilities, augmented by cost estimates for additional search space reduction, prove very helpful.

Once a promising plan has been established, the execution level instantiates the required data values and executes the models selected by the planner. This level may need access to databases and mathematical libraries for which Prolog may not be the ideal programming tool; coupling with external systems may become necessary [1]. If not all required data are available, control is returned to the surface planner which may either try an alternative strategy, or invoke a fact acquisition subsystem designed to obtain missing information (or at least directions where to find it) from the user.

The remainder of this paper describes the ACS in more detail. Section 2 briefly reviews the range of actuarial problems to be supported by the ACS. Section 3 presents knowledge representations for actuarial concepts and problem solving strategies. In section 4, the layered architecture of the ACS is described; more details on the main model management component – the surface planner – are provided in section 5. Section 6 demonstrates the usage of the system by a comprehensive example and section 7 reviews the status of the system and outlines extensions currently under design.

## 2. Model Management in Actuarial Science

The statistical study of the contingencies of human life, such as death, disability, or retirement, forms the foundation of actuarial science. Experts in this field are called actuaries. The actuary must estimate the probabilities of occurrence of contingent events as a basis for calculating premiums, reserves, annuities, etc., for insurance and other financial operations. For the solution of problems involving these contingencies, an actuary requires some quantitative measure of their effects. In problems involving financial calculations, the actuary also requires a set of principles by which probabilistic measurements may be combined with interest functions to produce monetary values [13].

The actuarial domain deals with a large number of formulas, equations, and models, many of which are intertwined with one another. At several points of the actuarial problem-solving process, expertise is needed. First, the actuary must comprehend and formulate the problem in terms of insurance concepts, and of the available data, like mortality rates, interest rates, commutation function values and health-related risk scores. Expertise is also required for choosing, transforming and sequencing an efficient set of applicable formulas. Generally, the actuary must develop an overall solution plan before any actual computation, because many actuarial problems require several formulas to be transformed and combined in a particular sequence. Knowing the solution strategy beforehand helps avoid cycling and redundant computation. Knowledge is finally needed for deciding whether to access tables of pre-stored data, to compute these values, because direct computation is cheaper than accessing the tables (or even the only method), and when to override default value table access by user-specified data.

The ACS represents the different actuarial concepts, formulas, and heuristics of problem-solving in a carefully organized knowledge base. The knowledge base must support at least the following functions:

1. Compute the premium for an insurance benefit or mix of benefits;

2. Assess feasibility of the benefits;

3. Explain the result by showing which models were applied in which sequence;

4. Allow the user to modify the reasoning process;

5. If a certain problem cannot be solved, point out why; also, ask for values which, if supplied, can solve the problem.

The ACS is not intended to replace an actuary but to assist in life insurance problems by serving as a ‘intelligent calculator’, i.e., a decision support tool. It was built for expert users and may not be suitable for a user unfamiliar with the basic concepts of life contingencies theory.

## 3. Structural Model of Actuarial Domain Knowledge

Actuarial theory is usually represented as a conglomeration of interrelated actuarial concepts.

<table><tr><td>Concept</td><td>Notation</td><td>Description</td><td>Sample Value</td></tr><tr><td>Mortality rate</td><td> $q_x$ </td><td>Probabilitya life aged xwill die in one year</td><td>0.05</td></tr><tr><td>Reserve</td><td> $_tV_x$ </td><td>Net worth of a policyfor a life aged xin a pool of premiumreceipts as at the endof t-th year</td><td>$5000 $^{5}$ </td></tr></table>

Each actuarial concept has a unique notation representing an individual insurance-related idea which can take a numerical value. Two examples are provided below. This section will discuss the representation of actuarial concepts and their relationships in the ACS.

A hierarchy of formalisms called Formula Derivation Net (FDN), Individual Concept Structure (ICS), and Derivation Structure (DS) capture interrelationships among the actuarial concepts. FDNs, ICSs and DS are defined as directed labelled graphs. A FDN consists of a set of interconnected nodes with each node representing an actuarial concept. FDNs are of three types: One-Sided; Mutual; and Collective (Fig. 1).

One-sided link: If a concept is derivable from another one but not vice versa, such a relation is called a one-sided link. For example, in Fig. 1(a) the actuarial concept $l_x$ represents the number of people alive at age $x$ out of a group which started off with $l_0$ at age zero, $p_x$ is the probability that a life aged $x$ will survive $t$ years. $l_x$ cannot be computed from $p_x$ alone because two values ( $l_x$ and $l_{x+t}$ ) of the former concept are needed to compute the latter.

Mutual link: If two concepts may be derived from each other, we have a mutual link. For example, in Fig. 1(b), ir and dr are the interest and discount rates respectively. As shown in the figure, if either ir or dr is known, one can find the other using the formula indicated above the arrow. Not all mutual links have to be stored explicitly since the system supports certain simple algebraic formula transformations similar to those in MACSYMA.

Collective link: Here we have a situation where a concept can be expressed in terms of more than one other concept. This is represented by an AND graph [14]. Consider the formula in Fig. 1(c) where $A_x$ represents the present value of \$1 insurance on a life aged $x$ and $a_x$ represents the present value of a life annuity payable at the beginning of each year.

The different FDNs that compute the same goal concept are combined into an Individual Concept Structure (ICS). The ICS defines the different paths through which a goal concept can be derived. The overlay of all ICSs is a state-space representation of the stored actuarial knowledge that will be referred to as the Derivation Structure (DS). The DS represents the total static knowledge of a particular implementation of the expert system. A portion of a DS is shown in Fig. 2.

![](/api/attachments/7WTA3S6S/fulltext/images/553deaa3218a2ad507b96b66aafd8b0bf3c15875b010114fbd7054b1b9eaac16.jpg)  
Fig. 1. Links in Formula Derivation Networks.

Each FDN is represented in Prolog using a 'can-find' predicate at the surface level and an 'evaluate' predicate at the execution level. The general structure of these predicates is as follows:

![](/api/attachments/7WTA3S6S/fulltext/images/7165c66d4b5c87d958846760918684f902f88b835709163d95d7775469df724d.jpg)  
Fig. 2. A Simple Derivation Structure.

can find (Goal\_category\_concept, Computation\_procedure\_identifier, if\_known (Required\_concepts)).

evaluate ( Computation\_procedure\_identifier, Required\_concepts, Result).

For example, consider the above FDN for $A_x$ (denoted [cap,a,X] in Prolog). The 'can find' predicate, shown below, stores the knowledge that the concepts $A_x$ , $a_x$ ; and $dr$ interrelated, in particular, that $A_x$ can be solved for, if the other two are known. The predicate also keeps an identifier denoting the formula connecting these concepts (0311 in the example below). The 'evaluate' predicate represents a procedure which instantiates the concepts numerically and invokes the formula execution. In this simple example, the computation can be easily expressed in Prolog itself and no external function call is necessary.

can find ([001, cap, a, X], 0311, if known ([012, a, tremma, X], [503, dr]])).

evaluate (0311, Dr, A\_tremma\_x, Cap\_a\_x):-member ([012,a,tremma,X,is,Val1], Concepts\_with\_value,Rest 1), member ([503, dr, is, Val2], Concepts\_with\_value,Rest2), Cap\_a\_x is (1 - Dr\*A\_tremma\_x).

Knowledge representations similar to the ones proposed here have been used in expert systems for organic synthesis and geology. Expert systems in the area of synthesis of organic compounds, such as LHASA [15], SECS [16] and SYNCHEM [17] use synthesis trees to organize the body of knowledge about chemical reactions. Synthesis routes that create the desired target molecule are viewed as AND/OR branches of the synthesis tree. The tree descends from the goal node representing the compound to be synthesized, to the terminal nodes representing the starting chemical compounds. The branches connecting the nodes represent possible chemical reactions.

In PROSPECTOR [19], an expert system in the field of geology, domain knowledge is represented in a so-called inference network. The nodes represent assertions about entities in the domain. The arcs between the nodes represent either inference rules or provide a context for testing another assertion. The system propagates the user's initial assertions through the inference network and on that basis selects one of its pre-stored geological models to guide its search for discovering what minerals can possibly be identified.

An interesting distinction between the data structures used in organic synthesis systems and the ACS is that the insurance data structure can automatically insert derived links (see section 5) between nodes, without requiring the explicit representation of each possible type of link between the different nodes representing the actuarial concepts. A major difference between the data structures in geology and insurance is that in the insurance domain the relationships among the nodes are exact formulas, whereas in geology the inference rules have uncertainty factor measures associated with them. On the other hand, the number of possibly interacting actuarial functions seems to be larger than in the very modular PROSPECTOR system.

## 4. Implementation Model of Actuarial Domain Knowledge

An actuary, when faced with an insurance problem, often goes about structuring a solution

Table 1
Comparison of Knowledge Representations

<table><tr><td>Domain</td><td>Name of Data Structure</td><td>Nodes</td><td>Connecting Links</td></tr><tr><td>Organic Synthesis</td><td>Synthesis Tree</td><td>Compounds</td><td>Chemical Reactions</td></tr><tr><td>Geology</td><td>Inference Network</td><td>Assertions</td><td>Inference Rules</td></tr><tr><td>Insurance</td><td>Derivation Structure</td><td>Actuarial concepts</td><td>Actuarial Formulas</td></tr></table>

![](/api/attachments/7WTA3S6S/fulltext/images/a1dc8bc43318dbd47558971ca166136718266fb038d289da527c7a3dab801607.jpg)  
Fig. 3. The Model of Model Management.

strategy intuitively. Computerizing this task requires an understanding of the actuarial problem solving process. Rather than relying on a collecof the values stored within the Prolog knowledge base. External storage of table values, and access to customer data will be provided through a Prolog-database connection [2,3].

Knowledge Base: The knowledge base component (Fig. 6) contains static and dynamic rules used by the previously described subsystems. Static rules identify the types of insurance benefits, actuarial notations and table values of interest, as well as textbook formulas. Dynamic rules deal with the knowledge about developing efficient problem-solving strategies by selecting and manipulating formulas, evaluating alternative solution methods and computing them.

Blackboard: This is a working space which serves as a scratchpad for the Problem Analyzer, the Surface Planner and the Plan Executor. It helps to create data structures, erase them and modify them dynamically during the process of problem solving. The original problem statement, its analyzed version, intermediate steps during a long search and intermediate results can all be stored for future references.

![](/api/attachments/7WTA3S6S/fulltext/images/f1c27f79e6a39608cac5d11e8476030d1d4c266e06519e07a02ef75a8f85f2c8.jpg)  
Fig. 4. The Solution Planner Component.

into three parts: the goal category insurance concept; the type of insurance benefit; and the constraints set by the user. Such interpretation of the problem will be referred to as generating a problem context. Later, it will be seen that the user has the opportunity to impose further constraints or to restate existing ones during the problem-solving process.

Suface Planner: The task of the Surface Planner is to develop a workable solution strategy for the problem context generated by the Analyzer. Using the set of 'can find' predicates in the knowledge base together with cost estimates for formula execution, it develops an optimal network of derived links from the Derivation Structure that will symbolically solve the problem (Fig. 4). A derived link associates different actuarial concepts transitively through one or more mediating concepts. For example, in Fig. 5, the dotted lines indicate the derived link. Although originally $A_x$ is represented in terms of $dr$ and $a_x$ and each in turn is represented in terms of $ir$ and $a_x$ , it is possible to use these sequential dependencies to derive a new link that directly connects $A_x$ to $ir$ and $a_x$ .

Plan Executor: This component inherits the solution method developed in the previous step. It then accesses the knowledge base and selects the 'evaluate' predicates corresponding to the formulas to be used. It instantiates the parameters with numeric values and carries out the computations in order to get the result. It can also access data base values if necessary, or request missing data from the user (see section 6.4).

Database: The database consists of numerical values for actuarial concepts and other important factors, such as interest rates. The ACS contains a specialized data dictionary facility to manage those tion of individual expert rules, a general implementation model of this process was developed. This 'model of model management' (as shown in Fig. 3) also serves as the control structure for the ACS. It has the following components:

![](/api/attachments/7WTA3S6S/fulltext/images/0b97ec361e9c4567cadf5458198639d9b097f6e4c174a8535d4b3eed1ea6298d.jpg)  
Fig. 5. A Derived Link.  
KNOWLEDGE BASE  
Fig. 6. Structure of Knowledge Base.

(1) Problem Analyzer

(2) Surface Planner

(3) Plan Executor

(4) Database

(5) Knowledge Base

(6) Blackboard

We shall briefly discuss each of these components:

Problem Analyzer: This component accepts a problem statement from the user and attempts to determine what the user is trying to solve for, and what constraints have to be kept in mind while developing a solution. In interpreting a problem statement, the Problem Analyzer searches for a set of key words. The problem statement is broken

Knowledge about the user interface

Types of goal category concepts

STATIC

Types of insurance benefits

Actuarial notations

Formulas

Formula Derivation Nets

Evaluation/computation procedures

Data base (table) values

Rules on problem recognition

DYNAMIC

Rules on selecting the formulas

Rules on manipulating the formulas

Rules on creation and deletion of intermediate strategies/results

## 5. Surface Planning Strategies

Three types of strategies have been incorporated in the Surface Planner: basic breadth-first search; cost-based search; and human expert rules. Prolog's standard depth-first search appears less suitable for most actuarial problems since many problems will have solutions which are only a few steps deep but not immediately obvious.

The basic breadth-first search contains a simple heuristic that attempts first to use formulas in which a partial match between given data and required values exists. The objective of using breadth-first is to limit the total number of formulas to be employed by trying directly applicable formulas upfront. Only when it is realized that no direct formula exists, the problem is decomposed into layers of subgoals. In other words, different lines of reasoning are examined in parallel at each step in the decomposition of the problem and no commitment is made to any specific strategy right from the beginning.

If the user is unhappy with the proposed solution strategy displayed after the basic breadth-first search, the Planner employs a cost-based search for alternative solution plans. The idea is to find a solution method which would be the cheapest for the Plan Executor to work with. Cost estimates are based on the number of formular needed in each solution method, the number of input concepts and the amount of computation involved in using each. Thus, a solution sequence which involves more formulas might be preferred to a shorter sequence with costly computations.

While these two basic methods employ backward chaining, the Surface Planner can also make leaping conclusions like a typical human expert, based on certain rules of thumb or experience used by actuaries. This may be called shortcutting the plan development and is simply implemented by adding new FDNs for the expert rules. While the scheme chosen for knowledge representation makes the implementation of these rules easy, the more difficult part is the precise statement of the circumstances under which these shortcuts (often approximations) are applicable. For example, consider the computation of a premium for a pension plan subject to the condition that in the event of death the premiums be returned with interest. An expert actuary can use a 'tricky' factor $a_{x+n}/s_{n}$ , obviating a long sequence of computations (see the

Appendix for an explanation). Such heuristics have to be used with care and only if the problem context warrants them.

## 6. An Example

Since the user interface has not been the primary concern of this research to date, input is provided to the system following a relatively simple structured English format:

FIND <goal category concept> FOR <type of insurance benefit>

[ GIVEN <constrained concept values> ].

The key words FIND and FOR are essential while GIVEN is optional (indicated by the square brackets), depending on whether the user wishes to specify some concepts or constrained values to be used during the problem solving stage. All the possible goal category concepts, types of insurance benefits and constrained concepts are stored with their input patterns in the knowledge base. Slots are provided to store numeric parameter values supplied in the problem specification.

In Prolog, these concepts take the form of predicates. A few sample predicates are shown below. The capital letters indicate instantiable variables. The numbers are concept identifiers provided for control purposes and may be ignored for now.

Goal category concepts:

possible\_goal([net, single, premium]).

possible\_goal([reserve, at, the, end, of, T, years]).

possible\_goal([amount, of, paid, up, insurance, at, duration, T]).

Types of benefit:

possible\_benefit([613], [F, dollar, N, year, endowment, payable, at, the, end, of, year, of, death]).

possible\_benefit([615], [F, dollar, whole, life, annuity, payable, at, the, end, of, year, of, death, with, payments, guaranteed, for, N, years]).

Constrained concept values:

possible\_value([012], [a, tremma, X, is, Val]).
possible\_value([501], [interest, rate, is, Val]).

possible\_value([609], [commission, C, pc, of, gross, premium]).

In the sequel, the solution of a particular actuarial problem concerning a whole life insurance premium will be traced through the components of Problem Analyzer, Surface Planner, and Plan Executor.

## 6.1. Problem Analyzer

The Problem Analyzer breaks the problem into its three parts. Each is understood by matching the input with the pre-stored ‘possible’ patterns, and then converted into the appropriate actuarial notations. The Analyzer shows the generated problem context (i.e.: the Goal; the type of Benefit; and the Constraint definitions) and stores them on the blackboard for future reference. Suppose the user submits the following problem (user inputs are italicized):

## | ?-problem.

: find the net single premium for a 10000 dollar whole life insurance payable at the end of year of death given age is 35, a tremma 45 is 8,10 v 35 is 1 and ir is 10 pc.

Goal = net single premium

Benefit = 1 10000 dollar whole life insurance payable at the end of year of death

Given concepts are

[[601, age, 35], [12, a, tremma, 45, is, 8], [124, 10, v, 35, is, 1], [501, ir, is, 10]]

yes

## 6.2. Surface Planner

The Surface Planner first retrieves the problem context from the blackboard and removes numeric values for specific insurance concepts temporarily, in order to conduct a purely symbolic planning process. Then, it identifies the actuarial problem to be solved by combining the goal category concept and the type of insurance benefit. In our example, the Planner combines the goal category concept 'net single premium' with the type of insurance benefit 'whole life insurance payable at the end of year of death' to form the corresponding uniquely identifiable actuarial goal 'cap\_a\_x'. For this purpose, the knowledge base contains a class of predicates called ‘notation equivalents’ which determine what type of goal categories can be combined with which type of insurance benefits to yield feasible actuarial concepts. The predicate selected for our example is shown below.

notation\_eqvt([net, single, premium], [F, dollar, whole, life, insurance, payable, at, the, end, of, year, of, death], [001, cap, a, x]).

Once the actuarial goal has been precisely identified, the Planner tries to find ways of solving for it using the given concept constraints (without values). It searches through the can-find ([001, cap, a, X], ..., if \_known (...)) predicates. Each predicate either represents a directly applicable formula for computing cap\_a\_x or a manipulated form which can be used to compute cap\_a\_x if the proper algebraic transformations are applied. In our example, the Planner has three choices available in the knowledge base (first three lines below).

can find([001, cap, a, X], 0311, if known([[012, a, tremma, X], [503, dr]])).

can find([001, cap, a, X], 0305, if known([[075, cap, m, X], [036, cap, d, X]])).

can find([001, cap, a, X], 0312, if known([[011, a, X], [501, ir]])).

can find([011, a, X], 0210B, if known ([012, a, tremma, X]).

can find([012, a, tremma, X], 0506B, if known ((([[012, a, tremma, Y], [124, T, v, X]])): save-problem-context(Z), member ([012, a, tremma, Y], Z), member([124, T, v, X], Z), Y is X + T.

In the absence of particular ‘expertise’ providing immediate shortcuts, the Planner tests the applicable rules with the heuristic of focusing the search on predicates where parts of the necessary values are known from the input data. Thus, since ir (interest rate) is known from the input data, the third rule is chosen and ‘a\_x’ is set as a subgoal. The fourth rule above is applied in turn and a new subgoal ‘a\_tremma\_x’ is created. After examining several alternatives of finding ‘a\_tremma\_x’ (not shown above), the fifth rule is applied successfully. Note that this rule refers to a manipulated form of the textbook formula ‘t\_V\_x = 1 - a\_tremma\_x + t/a\_tremma\_x’. The successful paths finally form a complete solution strategy.

| ?-soln-plan.

We have to find [1, cap, a, 35]
We know values of [501, ir]
We need values of [11, a, 35]
- then we can use formula/s:

$\mathbf{cap\_a\_x} = [1 - \mathrm{i}r.a\_x] / 1 + \mathrm{i}r$

Note that We can find [12, a, tremma, 35]
if known([[12, a, tremma, 45], [124, 10, v, 35]])

using t\_v\_x = l\_a\_tremma-x + t/a\_tremma\_x
Note that

We can find [11, a, 35] if known ([12, a, tremma, 35])

using a\_tremma-x = 1 + a-x

yes

## 6.3. Plan Executor

The Plan Executor first retrieves the solution strategy developed by the Planner, represented on the blackboard as a list of formula identifiers. Letters are attached to the formula numbers to identify transformation to be applied to the textbook formulas. In our problem, the solution strategy is represented by the predicate, strategy ([0506B, 0210B, 0312]). The numeric part of the first identifier 0506B indicates to the Plan Executor that the textbook formula is 't\_V\_x = 1 - a\_tremma\_x + t/a-tremma-x' in a manipulated form. The Plan Executor calls the corresponding evaluation predicates one at a time. Each 'evaluate' predicate contains or calls the procedure for computing the corresponding formula and can retrieve the numerical inputs either from the problem context or from the data base. Finally, the computed values are combined and the numerical solution to the problem is computed.

## 6.4. Fact Acquisition

If not enough information is available to solve a problem, the above procedure will notice this either at the Surface Planning or at the Execution level. In either case, the system will ask for additional information. Three cases can be distinguished (Fig. 7). In the first case, the user does not care how the problem is to be solved or where the input data come from. For example, a user may just ask for the premium for a standard policy. In this case (denoted I in Fig. 7), the system will only fail if the goal set by the user cannot be computed from any data available in the database. The fact acquisition subsystem of the ACS [7] will make an educated guess which data the user might be able to provide; if that fails again, the Surface Planner will develop an alternative plan and ask for its missing data until either a solution is found or the user decides to give up.

![](/api/attachments/7WTA3S6S/fulltext/images/c01d523c17b9e5fb49cab0d18b55842435e583eb4151744587f33a41d235f2b7.jpg)  
Fig. 7. Model of Fact Acquisition.

In case II, the user specifies which concepts are constrained but wishes to use default values for the constraints. The defaults should be available from the database; if not, the system will ask the user for data. However, there is no need for the system to look for alternative strategies without being told so since that would be against the wishes of the user.

Finally, in case III, the user provides at least some of his own data to override default values (e.g., mortality rates) stored in the database. Two possible problems may occur in this case. On the one hand, the user may forget to specify a certain concept or to mention it at all; the above procedures can be used to add the missing information. On the other hand, the problem may be overconstrained, leading to contradictions and leaving the problem unsolvable. For example, the user may put upper limits to the premium payment capability and lower limits to the policy amount that are not compatible. The fact acquisition system will in this case try to point out where the contradiction lies so that the user can correct the input.

## 7. Conclusions

The ACS has demonstrated the usefulness of a layered knowledge base architecture for model management even in a logic programming environment. The performance advantages obtained by this kind of architecture increase if the models are more complex than the simple examples shown in the paper. The architecture of the system has also proven a good tool to combine exact mathematical knowledge (as in the textbook formulas) with human expert problem-solving heuristics.

The current prototype of the ACS has a repertoire of 95 actuarial concepts and 175 formulas which covers approximately 80% of all actuarial concepts applicable to single life policies [13]. The approx. 600 formulas for the multiple-life case are being added to the system. Most of the fact acquisition subsystem described in section 6.4 is also operational. Both this part and the human expert shortcut rules are being expanded, based on experience with using the system. Experiments with a number of textbook and real-world actuarial problems have demonstrated that the system is capable of finding and explaining rather ‘clever’ solutions to some problems, in some case solutions that the expert posing the problem had not thought of before.

One of the major next steps in this work is to improve the user interface so that it can be used with less training. In particular, we are focusing on the development of an interface for tutoring actuarial students in their preparations for the official actuarial exams. Some initial experiments with the existing prototype have already shown that the ACS can support this process effectively by permitting the student to compare multiple possible solution strategies in terms of their elegance and computational costs. However, the system will need more flexibility in its user interface to become a usable tutoring tool.

## Acknowledgments

The authors are grateful to Jim Clifford for many useful suggestions in the early phases of this work. Thanks are also due to the referees whose comments greatly improved the presentation of this material.

## Appendix

Explanation of the Factor $a_{\ddot{x} + n} / s_{\ddot{n}}$

Problem: Find the net annual premium payable for n years for a pension cover of \$1 per annum issued to a life aged x, with the first pension payment n years after date of issue and with the provision that, if the insured dies within the n year period, the net premiums paid are to be returned with compound interest to the end of the year of death.

(i) The mathematical solution is shown below:

$$
\begin{array}{r l} P (N _ {x} - N _ {x + n}) & = N _ {x + n} + P \sum_ {t = 1} ^ {n} S _ {i} C _ {x + t - 1} \\ & = N _ {x + n} + P / d \left[ (1 + i) ^ {t} v ^ {x + t} d _ {x + t - 1} \right. \\ & \quad \left. - C _ {x + t - 1} \right] \\ & = N _ {x + n} + P / d \left[ v ^ {x} (1 _ {x} - 1 _ {x + n}) \right. \\ & \quad \left. - (M _ {x} - M _ {x + n}) \right] \\ & = N _ {x + n} + P / d \left[ D _ {x} - (1 + i) ^ {n} D _ {x + n} \right. \\ & \quad \left. - D _ {x} + d N _ {x} \right. \\ & \quad \left. + D _ {x + n} - d N _ {x + n} \right] \\ & = N _ {x + n} + P (N _ {x} - N _ {x + n}) \\ & \quad \left. - P / d. D _ {x + n} [ (1 + i) ^ {n} - 1 ] \right. \\ & \text { Thus: } \\ P s _ {n} D _ {x + n} & = N _ {x + n} \\ P & = a _ {x + n} / s _ {n} \end{array}
$$

(ii) Alternative heuristic reasoning:

Imagine the insured survives the n years to age $x + n$ . The same pension benefit if issued at age $x + n$ will cost $a_{x+n}$ dollars. Suppose the prospective pensioner while at age x decides to wait till age $x + n$ and then buy the pension coverage at this cost. However, let him create a sinking fund by depositing an amount P annually into a bank account, P being so chosen that over n years the annual deposits would accumulate with interest to $a_{x+n}$ . According to the theory of compound interest, in order to accumulate 1 over n years with interest, the annual deposit should be $1/s_{n}$ . Hence, to accumulate $a_{x+n}$ dollars, P has to be $a_{x+n}/s_{ij}$ :

\$P is the solution to our problem since:

1. If such an amount is deposited annually it will accumulate over n years to the price of the pension plan at age $x + n$ which amount can be used then to buy the pension benefit;

2. In case he/she dies before reaching age $x + n$ , the annual deposits of \$P made until then can be withdrawn as if they had gone into a bank account.

## References

[1] Jarke, M. and Y. Vassiliou, Coupling Expert Systems with Database Management Systems, in: W. Reitman (ed.) Artificial Intelligence Applications for Business, Ablex, Norwood NJ (1984).

[2] Vassiliou, Y., J. Clifford and M. Jarke, Access to Specific Declarative Knowledge in Expert Systems: The Impact of Logic Programming, Decision Support Systems 1 (1985).

[3] Jarke, M., J. Clifford and Y. Vassiliou, An Optimizing Prolog Front-End to a Relational Query System, Proc. ACM-SIGMOD Intl. Conf. Management of Data, Publ. Boston MA (1984).

[4] Clifford, J., M. Jarke and H.C. Lucas, Designing Expert Systems in a Business Environment (1985) in: L.F. Pau (ed.) Artificial Intelligence in Economics and Management, North-Holland, Amsterdam (1986).

[5] Elam, J.J., J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proc. First Intl. Conf. Information Systems, ACM, New York (1980).

[6] Sprague, R.H. and E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs NJ (1982).

[7] Sivasankaran, T., Intelligent Model Management in an Actuarial Consulting System, Ph D Thesis, New York University, New York NY (1984).

[8] Bonczek, R., C. Holsapple and A.B. Whinston, The Evolution from MIS to DSS: Extension of Data Management to Model Management, in: M. Ginzberg, E.A. Stohr W. Reitman (eds.) Decision Support Systems, North-Holland, Amsterdam (1982).

[9] Blanning, R., Language Design for Relational Model Management, in: S.K. Chang (ed.) Management and Office Information Systems, Plenum Press, New York NY (1982).

[10] Clocksin, W.F. and C.S. Mellish, Programming in Prolog, Springer-Verlag, Berlin (1981).

[11] Bonczek, R., C. Holsapple and A.B. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management, Operations Research 29 (1981) 2.

[12] Dolk, D.R. and B.R. Konsynski, Knowledge Representation for Model Management Systems, Working Paper, University of Arizona, Tucson AZ (1983).

[13] Jordan, C.W., Life Contingencies, The Society of Actuaries, Chicago IL (1975).

[14] Nilsson, N., Principles of Artificial Intelligence. Springer-Verlag, Berlin (1982).

[15] Corey, E.J. and W.T. Wipke, Computer Assisted Design of Complex Organic Synthesis, Science 166 (1969).

[16] Wipke, W.T., H. Braun, G. Smith, F. Choplin and W. Sieber, SECS - Simulation and Evaluation of Chemical Synthesis: Strategy and Planning, in: W.T. Wipke and W.J. House (eds.) Computer Assisted Organic Synthesis, American Chemical Society, Washington DC (1977).

[17] Gelernter, H.L., A.F. Sanders, D.L. Larsen, K.K. Agarival, R.H. Boivie, R.H. Spritzer and J.E. Searleman. Empirical Explorations of SYNCHEM, Science 197 (1977).

[18] Duda, R., J. Gaschnig, P. Hart, K. Konolige, R. Reboh, P. Barrett and J. Slocum, Development of the PROSPECTOR consultation system for mineral exploration, SRI Projects 5821&6415, SRI International, New York NY (1978).
