---
otero_id: 17208
otero_key: "G7Z5J8X4"
title: "A knowledge representation language for university requirements"
authors: "Martin Charles Golumbic; Moshe Markovich; Michael Tiomkin"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90075-m"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A knowledge representation language for university requirements

Martin Charles Golumbic, Moshe Markovich and Michael Tiomkin
IBM Israel Scientific Center, Technion City, Haifa, Israel

Intelligent systems with applications in an academic environment are becoming a reality. Such systems can offer intelligent assistance in tasks ranging from interactive scheduling, academic planning, office automation, database management and computer assisted instruction. The problem of designing a general requirements model for university degrees is investigated. A method for expressing the structure of university requirements is described, and a representation language consisting of a subset of Prolog based on set theoretic primitives is suggested. This work has been motivated by our experience with the Academic Planning Environment (APE) expert system project [9] whose goal has been to study the use of knowledge-based techniques in the advising and assistance of university students in the planning of their studies towards an academic degree.

Keywords: Knowledge representation, Academic planning, Logic programming

![](/api/attachments/G7Z5J8X4/fulltext/images/e106e684e84d28f63013b41c472a2057e1488dae2850093da208539acca2512c.jpg)

![](/api/attachments/G7Z5J8X4/fulltext/images/ad1cc2f586e9ff9cfbafe71829e31937f10d519c9846b7ade6c7754efd5e9241.jpg)

Michael Tiomkin received his M.Sc. equivalent in Mathematics from the Moscow State University, USSR, and the D.Sc. degree in Computer Science from the Technion, Haifa, Israel. He is currently with IBM Science and Technology, Technion City, Haifa, Israel. Before joining IBM he was with the Department of Computer Science at the Technion, Haifa, Israel, etc. His research interests include performance evaluation, AI, nonstandard logics, program semantics, and intelligent user interface.

Moshe Markovich received the M.Sc. and B.Sc. degrees in computer science from the Technion–Israel Institute of Technology. From 1984 to 1987 he worked as a student staff member at the IBM Israel Scientific Center, Haifa, Israel. He is currently with Graphic Technologies, Herzliya, Israel. His current interests include distributed computing, logic programming, and knowledge-based systems.

## 1. Introduction

A knowledge-based expert system is a computer program which uses explicitly represented knowledge and separate computational inference procedures to solve problems normally requiring significant human expertise. In conventional programs, knowledge is scattered throughout the code, and changing a single fact may require changes in hundreds of lines of code in dozens of modules. In knowledge-based systems, rules, facts and relationships are separated from the flow of control.

Advances in knowledge-based techniques have opened new opportunities for creating computer systems with intelligent capabilities far beyond their predecessors. There is a growing demand for more powerful, higher-level techniques, tools and concepts to support reasoning capabilities, large knowledge bases and userfriendly interfaces. This

![](/api/attachments/G7Z5J8X4/fulltext/images/e1998a445f7b9847d1f7938f7d6e66986e289b1e63ba84d132f8c405f623edc8.jpg)

Martin Charles Golumbic is a research staff member at the IBM Israel Scientific Center and associate professor at Bar-Ilan University. He is the founding editor-in-chief of the series Annals of Mathematics and Artificial Intelligence, a member of the editorial board of the journal Discrete Applied Mathematics and on the advisory board of the International Journal of Expert Systems: Research and Applications.

in mathematics from Columbia University in 1975. Before moving to Israel in 1982, he served as assistant professor of computer science at the Courant Institute of Mathematical Sciences of New York University, visiting scientist at Universite de Paris and the Weizmann Institute of Science, and worked at Bell Telephone Laboratories.

He is the author of the book Algorithmic Graph theory and Perfect Graphs and many research articles in the areas of combinational mathematics, algorithmic analysis, expert systems, artificial intelligence, and programming languages. He has been a guest editor of Discrete Mathematics, associate editor of the volume "Approaches to Intelligent Decision Support", Annals of Operations Research 12, and editor of the forthcoming book Advances in Artificial Intelligence, Natural Language and Knowledge-based Systems.

His current area of research is in combinatorial mathematics interacting with real world problems in computer science and artificial intelligence. He is a member of the Phi Beta Kappa, Pi Mu Epsilon, Phi Kappa Phi, Phi Eta Sigma honor societies and is married and the father of four bilingual daughters.

<table><tr><td></td><td>Bible</td><td>Talmud</td><td>Jewish History or Jewish Philosophy</td><td>Jewish Philosophy or Talmud</td></tr><tr><td colspan="5">For students with no judaic studies as major or minor:</td></tr><tr><td>nonjew</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>male</td><td>4</td><td>8</td><td>2</td><td>2</td></tr><tr><td>female</td><td>4</td><td>4</td><td>2</td><td>4</td></tr><tr><td colspan="5">For students with the following judaic studies as major or minor, (take the minimum of each column entry that applies):</td></tr><tr><td>tanach</td><td>0</td><td>8</td><td>2</td><td>2</td></tr><tr><td>talmud</td><td>4</td><td>0</td><td>2</td><td>0</td></tr><tr><td>jewish hist.</td><td>4</td><td>8</td><td>0</td><td>2</td></tr><tr><td>jewish phil.</td><td>4</td><td>10</td><td>0</td><td>0</td></tr><tr><td>hebrew lang.</td><td>4</td><td>8</td><td>2</td><td>2</td></tr><tr><td>hebrew lit.</td><td>4</td><td>8</td><td>2</td><td>2</td></tr></table>

new generation of computing presents a tall order to fill, and computer scientists in diverse areas are rushing to stake their claim and start panning the waters. But dramatic innovations are required, and, as in any research discipline, the nuggets of gold will only come after the integration, refinement, and applied insight of those many bits of experimentation, design, implementation, examples and applications that are underway today.

This paper addresses the problem of designing a general requirements model for university degrees which will be applicable to a large number of institutions. There are a number of similarities between the requirements of different universities such as credit points, hours or other measures and a hierarchical structure of requirements according to administrative levels of the university, schools, faculties, departments, and specific programs in the department. However, the variety and complexity of requirements between different universities is overwhelming. Consider the following examples.

Example 1. A computer science student at the Technion is required to take 4 courses from each of 3 groups of electives selected from 6 eligible (non-disjoint) groups such that at most one course may be counted towards two of the groups and any course that is used to fulfill a core requirement may not be counted towards this requirement.

Example 2. A mathematics student at PSU is required to take 32 credits of general science courses including

\- 6 credits of chemistry but not Chem09 or Chem12,

\- 14 credits of physics including Phys201, Phys 202, either Phys203 or Phys 204, and one course numbered above 400 but not Phys410,

\- 3 credits in biological sciences,

\- not more than 2 courses in any other single department.

Example 3. A student at Bar-Ilan must satisfy the “core studies” requirement by taking the number of credits indicated in each column of the table above which applies to the status of the student. In this work we discuss some of the issues involved, describe a method for representing the structure of requirements and a possible way of expressing individual requirements. Our language for representing university requirements is a subset of Prolog $^{1}$ [4,16] which uses set theoretic primitives. Finally, we discuss the advantages and disadvantages of such an approach from an implementation point of view.

## 2. Specification for a general requirements language

At most institutions of higher education there are several levels of administration each of which may set degree requirements. There may be certain general university requirements such as overall minimum number of credits, basic courses, etc. This could be followed by school or college requirements involving foreign languages and distribution on the areas in which courses must be taken. Then each faculty will place further requirements and perhaps strengthen or otherwise modify requirements already set higher in the hierarchy. Thus, any representation must have the capability of overriding, superseding and exempting requirements.

In order to design a general requirements language, we must focus on techniques of knowledge representation as it relates to the academic environment. Knowledge representation is one of the central issues in artificial intelligence today. In contrast to the general purpose heuristic search techniques which constituted a major thrust in the 1970's, new knowledge handling facilities which are tailored to the special structure of an application are the debutante of the 1980's. Current research includes modeling objects and their attributes, relationships, exceptions and defaults, as well as expressing assertions and rules that can be used for multiple purposes, for example, information retrieval, deductive reasoning or semantic pattern matching.

We now describe four familiar and useful representation schemes and show instances of how they are used in an academic planning expert system. Each of these can be translated into our general requirement language in a straight forward manner, and are used extensively in the APE [9] system.

## 2.1. Logical Representation Schemes

Logical representation schemes use formulas in some logic (first or higher order, multi-value, temporal, Horn clause, default, fuzzy, etc.) to represent facts. For example, the fact that “a student majoring in physics is studying science” could be represented by the formula

$$
\forall x [ \text { physics - major } (x) \Rightarrow \text { science - student } (x) ].
$$

The knowledge base consists of a large collection of such logical formulas. The inference rules of the logic allow deduction to be carried out formally as proof procedures. Suppose our knowledge base contains the formulas

passed(88-130) or passed(88-135)

$\Rightarrow$ passed(calculus)

$$
\forall x [ \text { course } (x) \text {   and   grade } (x) \geq 6 5 \Rightarrow \text { passed } (x) ].
$$

We could then conclude that "if a student took the course 88–135 and received a grade of 80, then the student has passed calculus." Logical representations such as this have the advantage of providing a clean, well understood formal syntax and semantics (at least for logics close to first order.) The disadvantages of the logical approach are the relative difficulty of representing procedural knowledge and the overall lack of organizational principles necessary for a large knowledge base. The logic programming language Prolog [4,16] is an attempt to overcome these disadvantages by interpreting logical formulas in a procedural way.

## 2.2. Graphical Representation Schemes

Graphical or network schemes are an attempt to organize the concepts to be represented as a collection of objects (nodes) and binary relations (directed labelled edges) between them. The example in fig. 1 shows a graph which states a number of facts:

\- professors and students are persons,

\- 'golumbic' is one particular instance of a professor,

\- two kinds of students are graduates and undergraduates,

\- professors teach graduates,

and from which we can say that “golumbic teaches graduate students” is consistent with our knowledge base. The seminal work of Quillian [13] on semantic networks was originally developed to model the human memory. Subsequently, a variety of such models have been proposed and used many applications including natural language processing, object oriented programming, cognitive psychology. Recent work is surveyed in the articles in [7,2] and Sowa’s very interesting book [17].

## 2.3. Frame-based Representation Schemes

A frame is a data structure for representing a stereotypical object or situation. It may have

\- slots for specific attributes with built-in default values.

\- relations between slots.

– procedures to be executed under certain conditions.

Frames were originally proposed by Minsky

![](/api/attachments/G7Z5J8X4/fulltext/images/0abd68da2787adb5c82ac15df8457711c064ca2966aa34e9f812e2fe827eb6ba.jpg)  
Fig. 1. A sample conceptual graph.  
[12] and continue to play a key role in current research in knowledge representation. Frames provide an organizational structure in which our expectations of a situation or object are influenced from its context. These concepts can be arranged in a hierarchy, similar to is-a of semantic networks, and properties or slot values may be inherited.  
In table 1, the COURSE-OFFERING frame is a specialization of the COURSE frame. The slots have been filled in with information for the course Biology 210 as might be found in the permanent university catalog and for the course offering Biology 210 Section 5 as might be found in this year's university timetable.

## 2.4. Production Rule Representation Schemes

A production rule is a statement of the form if condition then action. These condition-action pairs can be used to represent data-sensitive, unordered rules as the basic unit of computation, rather than the sequenced instructions of most procedural lan-

<table><tr><td colspan="2">Table 1A sample frame.</td></tr><tr><td colspan="2">COURSE Frame</td></tr><tr><td>Name:</td><td>Biology 210</td></tr><tr><td>Prerequisite-list:</td><td>Biology 110 and Biology 130</td></tr><tr><td>Corequisite-list:</td><td>Biology 200</td></tr><tr><td>Profile:</td><td>genetics, laboratory, hardness(4)</td></tr><tr><td>Recommendation:</td><td>Take second year</td></tr><tr><td colspan="2">COURSE-OFFERING Frame</td></tr><tr><td>Specialization-of:</td><td>COURSE</td></tr><tr><td>Name:</td><td>Biology 210 Section 5</td></tr><tr><td>Meetings:</td><td>Mon. 8–10, Wed. 8–9, Fri. 8–9</td></tr><tr><td>Instructor:</td><td>Prof. S. Benser</td></tr></table>

guages. The example in table 2 might be used to recognize a student whose record indicates that he is weak in calculus and to recommend that he try to fulfill his mathematics electives with a discrete mathematics course rather than an analysis course.

We conclude this section with a discussion of the features to be present in a general requirement language. The language should be rich enough to allow all reasonable requirements to be expressed, including the types of knowledge structures described above. This we would call completeness. Most requirements should be easily expressible and modifiable and facilitate representing exceptions, exemptions and other special case situations. The language must be implemented in an efficient manner so that processing requirements will be reasonable. Finally, the natural hierarchy and decomposability of the requirements should be preserved so that courses already taken can be processed properly.

## 3. A detailed description of our language

A set of finite set theory primitives is declared for evaluation (and description) of the requirements for receiving an academic degree. They enable the defining of sets by the use of predicates and the manipulation of other sets. Our approach has been motivated by the observation that real university requirements are written in a set theoretic style consisting of primitive sets, choosing subsets and various set operations. Some of the ideas used here have been inspired by the SETL programming language [14]. The requirements written in this language may be regarded as a Prolog program computing a set of courses which should be taken, where the following is allowed:

<table><tr><td>Table 2A sample production rule.</td></tr><tr><td>IF student is a computer science minorAND student is not a mathematics majorAND student is weak in calculusTHEN set priority of discrete math electives tohighAND set priority of analysis electives tolow</td></tr></table>

– referencing to the primitives (set theory, arithmetic, and university catalog data bases),

\- one rule procedures whose head arguments are different Prolog variables.

\- logic connectors: $\& (\mathrm{and}), |(\mathrm{or}), \Rightarrow (\mathrm{implies}), \neg (\mathrm{impossible})$ and if-then-else,

\- no recursion is allowed.

The finite set theory predicates used in our language include:

1. The usual set operations: $x \in S$ , $S_1 \subseteq S_2$ , $S = \phi$ , $S_1 \cup S_2$ , $S_1 \cap S_2$ , $S_1 \setminus S_2$ , $\bigcup S_i$ , $|S|$ .

2. A pseudo-random choosing of a subset of a given set.

3. The operators which create substantially new sets, namely $\{X|g(X)\}$ {the set which is defined by a formula \( g \)), and {one of \( Z \mid g(U, Z) \) for \( U \in X \}} (the partial image of the multifunction defined by the formula \( g \) on the set \( X \)), the latter being nondeterministic.

4. All the operators above defined on the multi-sets instead of sets.

## 4. Examples of using the language

## 4.1. Representing elementary requirements

We divide the requirements predicates into 3 types:

1. Core predicates which are the lowest level and should be viewed as a data base. These usually contain information about courses, lists of electives, compulsory courses, etc. The core predicates usually contain a very shallow body or none at all.

2. Requirement predicates are the main Prolog requirements rules. They contain access to the core predicates and result in a set of courses as the output parameter.

3. User defined predicates are new set theoretic predicates created for user convenience and are based on existing predicates.

Contains the primitives and the logical connectors of the language. A Prolog implementation of set theoretic predicates is given in the appendix.  
```txt
X ∈ S: X is member of the set S.
S₁ ⊆ S₂: S₁ is a subset of S₂ (a test only).
subset(Sub,N,Set): “Sub” is a subset of “Set” of size N.
subset(S₁,N₁,S₁,N₂,Set): S₁ and S₂ are two disjoint subsets of sizes N₁ and N₂, respectively.
φ(S): S is the empty set.
num-of-el(S,N): |S| = N.
setof(S,X,Goal): S = {X | Goal}.
setofr(S,Z,U,X,Goal): S = {one of Z | Goal(U,Z) for U ∈ X},
(Choose, for every U ∈ X, an element Z
such that Goal succeeds, and put these elements in S.)
union(Y,X): Y{z | z ∈ Z and Z ∈ X}.
union(S₁,S₂,S): S₁ ∪ S₂ = S.
inter(S₁,S₂,S): S₁ ∩ S₂ = S.
differ(S₁,S₂,S): S₁\S₂ = S.
set(Multiset,Set): Translates ‘Multiset’ into ‘Set’
sum(Set,Sum): Sum = Σ z
z ∈ Set
A ⇒ B: For all examples of A, B is true, (equivalent to ¬(A&¬B)).
∃A: There exists a solution of A.
if A then B else C: The usual ‘if-then-else’ operator.
```

The following course axiom will associate the course id with its properties. In this example, the properties are department, course type (e.g., lab, lecture, siminar) and number of credit points.

course(04100, ee, lab, 1). course(04103, ee, sem, 3).
course(23109, cs, lec, 3). course(10110, mt, lec, 3).

The access to the course axioms will be via predicates such as:

```prolog
laboratory(Course) ← course(Course, *, lab, *).
seminar(Course) ← course(Course, *, sem, *).
lecture(Course) ← course(Course, *, lec, *).
```

that check if a course is of a certain type, and system used in any specific academic institute. The number of fields and their content may be changed and the field dependency may be used for shortening the number of axioms. We can specify a set of courses by using their properties. For example, the set of seminars in the computer science faculty:

cr-points(Course, Points) ← course(Course, \*, \*, Points).

which gives the number of credits of a course. Note that the symbol \* has the meaning of Don't Care and unifies with anything. The user may define the course axioms to fit the requirement setof(CS-seminars, Seminar, course(Seminar, cs, sem, \*)).

Another example, the set of all courses in electrical engineering that have more than 3 credit points:

setof(EE-more-than-3, Course, course(Course, ee, \*, N) & N > 3).

A computer science compulsory list of courses is given next, and the student must take them all. In some of these courses the student may choose the required course from a given sublist. For example, an algebra course can be one of two suggested courses 10133 and 10134. The rule is given as follows:

cs-compulsory-cs({10003, 10005, 11071, 12040, 23113, 32001, 39001, Algebra, 10004, 10131, 11072, 23115, English2, 11032, 39001, 10132, 10130, 11073, 04105, 04145, 23144, 11033, Probability, 04126, 04130, 23218, 23246, 04262, 23116, 04150, 04147, 04151, 04267, 23315, Advanced-project, 04169, 23328})

$\leftarrow$ Algebra $\in \{10133, 10134\}$ & English2 $\in \{32002, 32118\}$ & Probability $\in \{10024, 09268\}$ & Advanced-project $\in \{04168, 23327, 23323, 23326, 23329, 04265, 23503, 23140\}$ .

The next example is of a predicate to evaluate the sum of credit points of a given set of courses. The meta predicate “setofr” is used in here for creation of a list of points from a given list of courses and the predicate “sum” gives an arithmetic sum of the list elements.

```txt
cr-points(Courses, Points)
```

← setofr(Set-of-points, Point, Course, Courses, cr-points(Course, Point)) & sum(Set-of-points, Points).

## 4.2. Computer science requirements coded in the set theory language

Example 4. In this example, the course set C which is to satisfy the computer science requirement for three years of study consists of the union of the four sets CC which are compulsory, CA which are chosen from lista, CB which are chosen from listb and CF which are free electives.

```txt
cs-three-years(C)
```

```txt
← cs-compulsory-3(CC) &
```

/\* From the list given by the predicate "ca-lista" the student should take courses

/\* with the sum of at least 18 credits, including one lab and one seminar or two labs.

cs-lista(LA) &

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\mathbf{X}\in \mathbf{LA}\&amp;$ laboratory(X)&amp;
</div>

$\mathbf{Y} \in \mathbf{LA} \& (\text{seminar}(\mathbf{Y}) | \neg \mathbf{X} = \mathbf{Y} \& \text{laboratory}(\mathbf{Y}) \&$

/\* The rest of the credits not taken from "cs-lista", to a maximum of 31, can be taken from the list "cs-listb" \*/

M is 31-NA & tolerance(Tol) & $\mathbf{M}_2$ is $\mathbf{M} + \mathrm{Tol}$ &

$\operatorname{subset}(\mathbf{CB}, *, \mathbf{LB})$ & cr-points(CB, Pts) & $\mathbf{M} \leq \mathbf{Pts} \leq \mathbf{M}_2$ &

/\* At most 10 credits can be taken from free electives.

take-free(CF, 10) &

union(C, {CC, CA, CB, CF}).

take-free(Free. Tail, N) ← N₁ is N-1 & take-free(Tail, N₁) & course(Free, \*, \*, \*) & ¬ Free ∈ Tail.

← Function-theory ∈ (10122, 10025) & Biology ∈ {13136, 13193}.

Example 5. We conclude with the specific requirement that was given in the introduction as Example 1.
/\* Choose a subset of 3 groups from a list of 6 numbered 1, 2, ..., 6.
cs-four-years(C)
← cs-compulsory-4(CC) &
subset(Groups 3, {1, 2, 3, 4, 5, 6}) &
/\* From each chosen group, at least 4 courses needed to be taken.
/\* The core predicate “cs-gp” associates a set of courses of each group number.
setofr(Set-of-sets, GPcourses, Group, Groups,
cs-gp(Courses, Group) & subset (GPcourses, N, Courses) & N ≤ 4) &
/\* From any two chosen groups at least 7 courses need to be taken and
/\* from all the 3 groups at least 11 courses need to be taken.
union(UU, Set-of-sets) & num-of-el(U, NN) & NN ≥ 11 &
(subset(Sub, 2, Set-of-sets) ⇒ (union(U, Sub) & num-of-el(U, NNN) & NNN ≥ 7)) &
union(GPcourses, Set-of-sets) & cr-points(GPcourses, Ngp) & unionm(CC, GPcourses, CC2) &
if Ngp ≥ 57 then (CourgpAB = φ)
else (Nelect is 57-Ngp &
choosegAB(CourgpABall) & differ(CourgpABall, CC2, CourgpAB2) &
tolerance(Tol) & Nelect2 is Nelect + Tol & subset(CourgpAB, \*, CourgpAB2) &
cr-points(CourgpAB, Pts) & Nelect ≤ Pts & Pts ≤ Nelect2) &
unionm(CourgpAB, GPcourses, Electives) &
∃(X ∈ Electives & Y ∈ Electives & laboratory(X) & seminar(Y)

|subset(Labs, 2, Electives) & X ∈ Labs ⇒ laboratory(X)) & take-free(CF, 10) & union(C, {CC2, CourgpAB, CF}).

cs-gp({10131, 23292, 23304, 23309, 23310, 23311, 23314, 23506, 23701, 23711, 23714, 23707}, 1).

cs-gp({04800, 23334, 04753, 04850, 23702, 23507, 23315, 23328, 23352}, 2).

cs-gp({23328, 23315, 23327, 23319, 23220, 23501, 23325, 23326, 23329, 23503}, 3).

cs-gp({09179, 23322, 23323, 23324, 09040, 09041, 09113}, 4).

cs-gp({23301, 23320, 10130, 23336, 23220, 23326, 09113, 23330}, 5).

cs-gp({09113, 09242, 09128, 09042, 09187, 23301, 23317, 23507}, 6).

cs-compulsory-3(Set)

← cs-first-2-semesters(Set, {04262, 10131, 11043, 11081, 23107, 23218, 23246, 09268, 11073, 11082, 23116, 23209, 23138, 23308, 23343}).

cs-compulsory-4(Set)

← cs-first-2-semesters(Set, {04262,11043, 11081, 23218, 23246, 10131, Choice, 04267, 11082, 11073, 23116, 09268, 23107, 23209, 23308, 23138, 23343}) & Choice ∈ {10134, 23292, 23330}.

## 5. Advantages and disadvantages

The syntax of this language does not appear at first to be very natural, however, in spite of this, we except it will be easy for a knowledge engineer to translate a natural language description of the requirements to an expression in this set theoretic language. The reason for our unusual optimism is the great semantic similarity between this language and the real requirements found in the university catalogs. To be sure, it is not intended to be human friendly enough for a university clerk to write the requirements directly. A more friendly human interface language between the natural language description and the set theoretic language can be designed in the development of such a project.

Since our language is based on set theory, its expressive power is sufficient for most requirements to be written concisely. Moreover, since the requirements language is actually a Prolog program, any legal requirement given in this language could be directly computed and give as a result a correct set of courses that the student should take. For students not in their first semester of studies, the suggested set of courses must include the courses already taken. So we can write

taken(T) & degree-requirement(S) & T ⊆ S,

## where

(1) taken(T) gives the taken courses,

(2) degree-requirement(S) results in a set of courses that satisfies the requirements for the degree,

(3) $\mathbf{T} \subseteq \mathbf{S}$ insures that the suggested courses will cover the courses that student has already taken.

Although the scheme suggested above is correct from a computation point of view, execution of the program in a naive manner as is, would require an impractical amount of computation time. The reason is that the program is written in a nondeterministic fashion and backtracking often occurs for cases where it is not necessary.

Our solution to this problem is to isolate predicates in the requirements corresponding to “Generate & Test” patterns. These can be easily determined since our language is a functional one and, for a given appearance of a variable, we can check if it gets a value or has an existing value to be tested. The optimization is done by mixing the test step with the generation step.

We divide the backtracking into two levels. A higher level backtracking will happen in the activation line between the conjunctives (2) and (3) above if the chosen set does not match the courses already taken. The lower level backtracking is that of the requirement itself and is caused by the nondeterministic choices inside the requirement.

In order to reduce the time complexity we need to minimize the backtracking where it is not necessary. This reduction will be done in two phases. In the first phase we will take care of the lower level backtracking by replacing blind choices where the program first does the choosing and then checking with a more sophisticated step that looks ahead to see if a partial choice made previously has a chance of success before it goes on to complete the choosing. For example: choosing m groups from a set of n groups such that in each group we will have at least 4 members. Direct computation will try every possible choice of m groups and then will check whether these m groups have 4 members each. In the optimized version, after each group is chosen, the check will be done separately and it will be added to the groups if it has 4 members. This optimization reduces time complexity from exponential to polynomial in n.

The second phase of optimization is to minimize backtracking in the higher level. Our goal in this optimization is that most of the time the first set produced in (2) will match the taken courses. This optimization stage will use the fact that each variable can be associated with a type. Since no mixture of different types occurs, we can generate a priority level for each item from its type by a bottom-up search procedure. After each item is assigned with its type and priority, the elements in the predicates with the highest priorities will be chosen first.

## 6. Experience and concluding remarks

A requirements description language has been designed which uses logical, metalogical and set theoretic predicates. The proposed language may be viewed as a universal tool for the expression of events in a world of finite typed sets. We have found the style of university requirements to be readily expressible in this language, and suggest that it may be useful for other purposes. In addition, a number of optimization techniques have been developed, however, more work would be needed before implementing a serious optimizer.

This work has been motivated by our experience with the Academic Planning Environment (APE) expert system project [9]. The goal of this project has been to study the use of knowledge-based techniques in the advising and assistance of university students in the planning of their studies towards an academic degree. As part of this study, a prototype system was successfully designed, implemented and tested at Bar-Ilan University, one of the seven institutions of higher education in Israel.

Our knowledge based system has the capability of planning a program of courses which meets the student's remaining degree requirements and is sensitive to his preferences and strengths. It is able to give correct advice on prerequisites, exemptions, and the like. The system will interactively suggest alternatives, verify and accept the student's requests, and schedule the desired courses.

In addition, our system includes many features of what might be considered an “on line catalog”. The system can answer such queries as, “When is course 88–215 being offered this year?”, “What are the prerequisites for 88–215?” and “What are my outstanding prerequisites for 88–215?” But unlike most on line catalogs, the answer from our system are generated directly from the knowledge base rather than from some textual version of the catalog. Thus, answers immediately reflect the most recent changes.

During a session with our system, the student is presented with an initial plan satisfying his most immediate requirements, and an interactive cycle is entered in which alternative plans and schedules are generated. These can be saved and retrieved at a later time. The system accepts a variety of time constraints, and, when no schedule exists for chosen plan of courses, will help select a partial solution which can then be completed. Various tools for checking and updating the departmental knowledge bases also exist.

The knowledge representation schemes surveyed in the preceding section are combined and adapted as needed to serve our purposes, just as data structures are selected and modified in traditional programming. During a typical session there are approximately 1750 Prolog axioms in the rule base – 1000 from the program itself, 150 from the initial Prolog set up, 300 for course and timetable data and 300 from student information and derived facts. For those who like to measure programs by the number of lines of code, our program has 5000 lines of code.

A large scale experiment of the Academic Planning Environment expert system was carried out in the mathematics and computer science department for students studying mathematics, statistics or computer science either as a major or as a minor. Two advising centers were set up – one staffed by faculty members (the human advisors) and the other “manned” by computer terminals running the computer advising system and monitored by one or two members of our team. Approximately 100 students used the computer advising system, (25% of the department.) A typical session took 15 minutes – 5 minutes for choosing courses and 10 minutes for playing with schedules. This compares favorably with the faculty interview. The system was most helpful for first year students who did not understand many of the rules in the catalog, and for second year students who had a large number of alternatives to choose from. Most third year students knew what they wanted to take, had prepared schedules in advance and were not particularly interested getting advice – neither human nor machine assisted! When problems occurred for third year students, they usually involved requests for special permission, which only the human advisor could give.

Both the time-table scheduling data and the student's grades are taken directly from the university database. For security reasons, only one special departmental account had permission to access this information. One member of the monitoring team, logged on to this account, would submit a batch request for the student's grades. Within two minutes the grade file was available and the student begins his session. The student advising system itself can be run interactively from any account, and any student is free to experiment with hypothetical situations.

A number of obstacles inherent in advising create logistical difficulties in providing the timely availability of the system. These include last minute changes imposed by a faculty mostly on vacation during the summer, routine computer maintenance or shutdowns during the crucial days before registration when the students actually plan their schedules, and bureaucratic coordination between the registrar and the faculties. These “administrivia” require constant attention in order to assure success of the scientific accomplishments.

It is our conclusion that a successful large scale implementation of such a computer advising system requires central university backing. This is currently the case for registration, and would also facilitate the creation of an automatic computer registration capability. After all, much of the real-time information about which sections are filled as well as the latest timetable changes are already in the university computer, which we download periodically to our system for scheduling purposes. Of course, other issues such as concurrency would have to be addressed if input were really coming from many sources as in the case of airline reservation systems.

In this paper we have addressed the knowledge representation issues involved with university degree requirements and have presented our general purpose language developed for this application area. In a companion work $[5,6]$ , we report on a comparative investigation of heuristic scheduling techniques under prioritized time constraints and course sections.

## Acknowledgments

The authors gratefully acknowledge the participation and help of our Bar-Ilan colleagues Moshe Ben Tzion, Baruch Muskat, Uri J. Schild, Ronen Feldman, Dennis Grinberg and David Krumbine.

## References

[1] A. Barr and E. Feigenbaum, eds., "Handbook of Artificial Intelligence", Volume 1, William Kaufman, Los Altos, Calif., 1981.

[2] M.L. Brodie, J. Mylopoulos and J.W. Schmidt, eds., "On Conceptual Modeling", Springer-Verlag, New York, 1984.

[3] L. Brownston, R. Farrell, E. Kant and N. Martin, "Programming Expert Systems in OPS5: An Introduction to Rule-based Programming", Addison-Wesley, Reading, Mass., 1985.

[4] W.F. Clocksin and C.S. Mellish, “Programming in Prolog”, Springer-Verlag, Berlin, 1981.

[5] R. Feldman and M.C. Golumbic, Constraint satisfiability algorithms for interactive student scheduling, Proc. Eleventh Int'l. Joint Conf. on Artificial Intelligence (IJ-CAI-89), August 1989, 1010–1016.

[6] R. Feldman and M.C. Golumbic, Interactive scheduling as a constraint satisfiability problem, Annals of Mathematics and Artificial Intelligence 1 (1990, 49–73).

[7] N.V. Findler, "Associative Networks: Representation and Use of Knowledge by Computer", Academic Press, New York, 1979.

[8] M.C. Golumbic, Knowledge-based techniques in an academic environment, Proc. Int'l. Conf. on Courseware and Design and Evaluation, Symposium on Artificial Intelligence and Education, Ramat Gan, Israel, April 1986, pp. 355–362.

[9] M.C. Golumbic, M. Markovich, S. Tsur and U.J. Schild, A knowledge-based expert system for student advising, IEEE Trans. on Education E-29 (1986), 120–124.

[10] F. Hayes-Roth, D. Waterman and D. Lenat, eds., “Building Expert Systems”, Addison-Wesley, Reading, Mass., 1983.

[11] D. Michie, ed., "Expert Systems in the Micro-electronic Age", Edinburgh Univ. Press, 1979.

[12] M. Minsky, A framework for representing knowledge, in P. Winston, ed., "The Psychology of Computer Vision", Mc-Graw-Hill, New York, 1985, pp. 211–277.

\*/

[13] M.R. Quillian, Semantic memory, in M. Minsky, ed., "Semantic Information Processing", MIT Press, Cambridge, Mass, 1968, pp. 227–270.

[14] J.T. Schwartz, “On programming, An interim report on the SETL project”, Courant Institute, New York University, 1973.

[15] M. Shaw, ed., "The Carnegie-Mellon Curriculum for Un-

dergraduate Computer Science", Springer-Verlag, New York, 1985.

[16] L. Sterling and E. Shapiro, "The Art of Prolog", M.I.T. Press, Cambridge, Mass., 1986.

[17] J.F. Sowa, “Conceptual Structures: Information Processing in Mind and Machine”, Addison-Wesley, Reading, Mass, 1984.

## Appendix

Prolog implementation of set theoretic predicates

$$
\mathrm{op} (\in , \mathrm{lr}, 7 0).
$$

$$
\mathrm{op} (\text { then }, \mathrm{rl}, 4 4).
$$

$$
\mathrm{op} (\subseteq , \mathrm{lr}, 6 5).
$$

$$
\mathrm{op} (e l s e, \mathrm{rl}, 4 4).
$$

op(beyond, lr, 60).

$$
\mathrm{X} \in (\mathrm{X}, \text {   Set }).
$$

$$
\mathrm{X} \in (*, \text { Set }) \leftarrow \mathrm{X} \in \text { Set }.
$$

$$
\mathrm{S} _ {1} \subseteq \mathrm{S} _ {2} \leftarrow \neg (\mathrm{X} \in \mathrm{S} _ {1} \& \neg \mathrm{X} \in \mathrm{S} _ {2}). / ^ {*} \text { i.e., } \mathrm{X} \in \mathrm{S} _ {1} \Rightarrow \mathrm{X} \in \mathrm{S} _ {2}
$$

$$
\text { subset } (\text { Sub }, \text { N }, \text { Set }) \leftarrow \text { var } (\text { N }) \& / \&
$$

$$
\mathbf {S} _ {1}, \mathbf {S} _ {2} \subseteq
$$

$$
\left| \mathrm{S} _ {1} \right| = \mathrm{N} _ {1}, \left| \mathrm{S} _ {2} \right| = \mathrm{N} _ {2}
$$

$$
\mathrm{S} _ {1} \cap \mathrm{S} _ {2} = \phi
$$

$$
\operatorname{subset} \left(\mathrm{S} _ {1}, \mathrm{N} _ {1}, \mathrm{S} _ {2}, \mathrm{N} _ {2}, \text {Set}\right) \leftarrow \operatorname{subset} \left(\mathrm{S} _ {1}, \mathrm{N} _ {1}, \text {Set}, \text {Tail}\right) \& \operatorname{subset} \left(\mathrm{S} _ {2}, \mathrm{N} _ {2}, \text {Tail}, ^ {*}\right).
$$

$$
\leftarrow \text { Max } > 0 \& /
$$

$$
\text { num - of - el - v } (*. S, N) \leftarrow /
$$

```prolog
num-of-el-(*.S,N) ← N > 0 & M is N - 1 & num-of-el-(S,M).
num-of-el-(nil,0).

setofp(S,X,P) ← setofpm(SS,X,P) & set(SS,S).

setofpm(Z.S,U,X,Pred) ← cons(Pred.U.Z.nil,Goal) & Goal & / & setofpm(S,X,Pred).
setofpm(S,*X,Pred) ← setofpm(S,X,Pred).
setofpm(nil,nil,Pred).

setofr(U.S,Z.X,Pred) ← cons(Pred.Z.U.nil,Goal) & Goal & setofr(S,X,Pred).
setofr(nil,nil,*).

setofr(Z2,S,Z,U,U2.X,Goal) ← / & copy-term(Goal.U.Z,G.U2,Z2) & G & setofr(S,Z,U,X,Goal).
setofr(nil,*,*nil,*).

setof(S,X,Goal) ← setof-(Multiset,X,Goal) & / & set(Multiset,S).    /* The real setof axiom    */
setof-(S,X,Goal) ← addax(setof-(e, *),1) & Goal & addax(setof-(a,X),1) & fail.
setof-(S,X,Goal) ← relax(setof-(E,V)) & setof--(E,V,S).
setof--(a,X,X.Tail) ← / & relax(setof-(E,V)) & setof--(E,V,Tail).
setof--(e,* ,nil).

setof-(b,b) ← fail.    /* A dummy axiom for setof-
union(Y,X) ← union-m(YY,X) & / & set(YY,Y).

/* union-m(Y,X): Y is the multiset of z such that z ∈ Z and Z ∈ X
union-m(Z.Y,(Z.XX).X) ← / & union-m(Y,XX.X).
union-m(Y,nil.X) ← / & union-m(Y,X).
union-m(nil,nil).
union(S₁,S₂,S) ← unionm(S₁,S₂,S₃) & set(S₃,S).
inter(S₁,S₂,S) ← interm(S₁,S₂,S₃) & set(S₃,S).
differ(S₁,S₂,S) ← differm(S₁,S₂,S₃) & set(S₃,S).

    set-operator(G) ← var(G) & / & fail.    set-operator(X ∈ Y).
    set-operator(X ⊆ Y).    set-operator(num-of-el(S,N)).
    set-operator(subset(Sub,N,Set)).    set-operator(subset(Sub,N,Set,Tail)).
    set-operator(subset(S₁N₁,S₂,N₂,Set)).    set-operator(inter(S₁,S₂,S)).
    set-operator(union(S₁,S₂,S)).    set-operator(φ(X)).
    set-operator(differ(S₁,S₂,S)).    set-operator(setofp(S,X,Pred)).
    set-operator(setofpm(S,X,Pred)).    set-operator(setofr(S,X,Pred)).
    set-operator(setofr(S,Z,U,X,Goal)).    set-operator(setof(S,X,Goal)).
    set-operator(setof(S,X,Goal)).    set-operator(union(Y,X)).
    set-operator(union-m(Y,X)).    set-operator(unionm(M₁,M₂,U)).
    set-operator(interm(M₁,M₂,I)).    set-operator(differm(M₁,M₂,D)).
    set-operator(∈(X,S,N)).    set-operator(set(Mset,Set)).
/* multiset operations ....
set(X.Multiset,X.Set) ← del-all(X,Multiset,Multitail) & set(Multitail,Set).
set(nil,nil).
unionm(X,A,B,X,C) ← unionm(A,B,C).
unionm(nil,B,B).
interm(X.A,B,X,C) ← delete(X,B,NB) & / & interm(A,NB,C).
```

```prolog
interm(*,A,B,C) ← interm(A,B,C).
interm(nil,*,nil).

differm(A,nil,A) ← /.

differm(X.A,B,C) ← delete(X,B,NB) & / & differm(A,NB,C).
differm(X.A,B,X.C) ← differm(A,B,C).
differm(nil,*,nil).

/* 'memberm (X,Set,N)' means that X appears N times in Set
memberm (X,X.A,N) ← / & memberm (X,A,N₁) & sum(N₁,1,N).
memberm (X,*,A,N) ← memberm (X,A,N).
memberm (X,nil,O).

sum(N.Tail,Num) ← int(N) & /& sum(Tail,Num1) & sum(Num1,N,Num).
sum(*.Tail,Num) ← sum(Tail,Num).
sum(nil,O).

delete(X,X.Tail,Tail) ← /.

delete(X,A.Tail,A.Tail2) ← delete(X,Tail,Tail2).

del-all(X,X.Tail,Tail2) ← / & del-all(X,Tail,Tail2).
del-all(X,A.Tail,A.Tail2) ← del-all(X,Tail,Tail2).
del-all(X,nil,nil).

N beyond M ← N ≥ M & Diff is N - M & tolerance(Maxdiff) & / & Diff ≤ Maxdiff.
tolerance(15).

A ⇒ B ← A & ¬B & / & fail.
A ⇒ B.

∃A ← A & /.

if A then B else C ← A & / & B.
if A then B else C ← / & C.
if A then B ← A & / & B.
if A then B ← /.

if A else C ← A & /.

if A else C ← / & C.
```
