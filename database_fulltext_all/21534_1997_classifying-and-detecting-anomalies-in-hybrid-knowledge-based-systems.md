---
otero_id: 21534
otero_key: "8QQWUX3T"
title: "Classifying and detecting anomalies in hybrid knowledge-based systems"
authors: "Ranadeep Mukherjee; Rose F. Gamble; Jennifer A. Parkinson"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00043-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Classifying and detecting anomalies in hybrid knowledge-based systems

Ranadeep Mukherjee <sup>a</sup>, Rose F. Gamble <sup>a,)</sup>, Jennifer A. Parkinson b

Department of Mathematical and Computer Sciences, UniÕersity of Tulsa, Tulsa, OK 74104, USA Department of Mathematics, UniÕersity of Kansas, Lawrence, KS 66045, USA

## Abstract

The increasing need for hybrid Knowledge-Based Systems KBS that accommodate more complex applications has ledŽ . to the need for new verification concerns that are more specific to the hybrid representation using objects and rule-based inference. Traditionally, verification of expert systems has focused solely on rule-based inference systems. Hybrid KBSs present additional verification problems not found in traditional rule-based systems. This paper is an investigation into the anomalies that may be present in a hybrid representation that warrant detection for the verification of the KBS. Many anomalies are due to the interaction of the component parts of the hybrid KBS. For example, subsumption anomalies arise due to an interaction between inheritance of objects and rule-based inference. In this paper, we extend the context of subsumption anomalies and introduce additional types of anomalies that may be present in the KBS. The goal of this research is to make hybrid KBSs more reliable by detecting such anomalies. q 1997 Elsevier Science B.V.

Keywords: Verification; Object-oriented; Rule-based; Expert systems

## 1. Introduction

Knowledge-based systems KBSs , sometimes called expert systems, are one of the most tangible products ofŽ . artificial intelligence research. Such systems can capture human reasoning in many domains, as well as integrate human interpretation with other computer programs to produce solutions to complex problems. As a requirement, these systems must be malleable in response to changing information and expert opinion. KBSs have been identified as necessary software components in many applications, including real-time and safety critical software. Due to their flexibility and embedded nature, the verification of the behavior of KBSs is extremely important if these systems are to be used confidently.

Traditionally, KBSs have been developed solely through the use of rule-based programming. Rules allow for easy modeling of expert reasoning. In addition, rule-based programs can be constructed quickly by individuals without extensive artificial intelligence or software engineering knowledge. With the proliferation of rule-based systems, an abundance of research has been performed to validate and verify these systems 22,26 . However,<sup>w</sup> <sup>x</sup> the power of rule-based systems is limited to narrow domains which do not have complex fact representation requirements and which are not computationally intensive.

Currently on the market are many KBS development shells, such as Kappa-PC <sup>2</sup>, that provide rapid development platforms for KBSs. The resulting systems are hybrid systems that combine the object-oriented and rule-based paradigms into a single KBS. The limited expressive power of production rules is supplemented with objects, which capture declarative knowledge in a hierarchy and provide for structural semantics among information. Inheritance is used to describe property sharing and abstractions in a class hierarchy. Methods are functions that allow for direct message passing between objects. Monitors are side-effect methods attached to attributes in objects that react to the accessing of values. Though verification concerns for traditional rule-based systems can form the appropriate foundation, the robustness and complexity of hybrid KBSs fosters additional verification problems. Thus, the established anomalies must be extended and new anomalies stemming from the interaction between the two paradigms must be identified. In addition, algorithms must be developed for automated detection.

In this paper, we consider an anomaly to be something that causes unexpected behavior during the execution of the system. Anomalies may result in inefficiency in terms of performance, maintenance, etc, as well as providing the cause for potential errors. Though all anomalies are not errors, many common KBS errors can be identified as resulting from anomalies. Because of the combination of paradigms, anomalies can occur in a hybrid KBS that are not present in the traditional rule-based KBSs. Our research has indicated two culprits that produce anomalies: inheritance and monitor interaction. Inheritance can cause subsumption anomalies due to mixed referencing of classes and instances in rules 10 . In addition, inheritance can cause anomalies within the<sup>w</sup> <sup>x</sup> objects themselves, such as duplicate attributes or identical names of different instances 17 . Because monitors<sup>w</sup> <sup>x</sup> are side-effect methods that are attached to attributes, they act as daemons, watching the attribute and activating when the attribute is accessed or changed. Interaction anomalies arise among monitors, such as circular referencing of attributes that also have monitors, and through interference with rule-based inference by activating unexpectedly.

In this paper, we concentrate specifically on subsumption anomalies and anomalies caused by monitor-rule interactions. Previous research in subsumption anomalies is critically examined and augmented to cover unexplored situations and conditions. In addition, we classify two types of monitor-rule interactions and define an algorithm to show how to detect these anomalies. A verification tool is still under construction that encompasses the detection of anomalies in a hybrid system. We have implemented a prototype system to detect subsumption anomalies by correcting and extending the algorithm proposed by Lee and O’Keefe 10 . We are in<sup>w</sup> <sup>x</sup> the process of implementing the algorithms to detect anomalies caused by monitor-rule interactions.

In Section 2, we present more detailed definitions of rule-based systems and hybrid KBSs, along with previous verification research. Section 3 presents the previous work on subsumption anomalies and the extension to this work. In Section 4, we define the anomalies that occur from monitor-rule interactions. Also, we provide algorithms for detecting these anomalies. Section 5 concludes the paper.

## 2. Knowledge-based systems

## 2.1. Rule-based systems

A simple rule-based system consists of three basic components: i a set of rules referred to as the knowledgeŽ . base, ii a set of content-addressable assertions referred to as working memory WM ; each element is called aŽ . Ž . working memory element WME , and iii an inference engine that may forward chain, backward chain orŽ . Ž .

both. A rule has a left-hand side LHS and a right-hand side RHS in the form LHSŽ . Ž . ™RHS. The LHS is composed of a conjunction of condition elements CEs and the RHS is composed of action elements AEs . AŽ . Ž . CE represents a template that is matched against WMEs to satisfy the LHS. An AE represents a change to the system state. If all positive CE’s can be matched against WM, and all the negative CE’s are not present in WM, then the actions can be performed. An AE may add, delete, or modify WME’s. In our presentation, those CE’s in the LHS that do not appear as AE’s in the RHS remain unchanged.

In this paper, we consider the execution of the rule processing component in Kappa-PC to be our model. This execution system consists of repeatedly executing a ‘match-fire’ cycle. In general, the match phase compares the LHS of a rule to working memory. If every CE is matched, the corresponding rule is instantiated and fired. If a match does not occur, another rule is selected for matching until no more selections are available. Firing the rule performs the AE’s in the RHS of the instantiation. The cycle continues until the match phase returns the empty set.

## 2.2. Verification of rule-based systems

Many current verification tools are applied to developed rule-based systems. Most tools will warn of problems and some will correct the knowledge base. In most verification research, these techniques generally address one or more of three broad theoretically-based criteria 16,26 . The first criteria establishes whether the<sup>w</sup> <sup>x</sup> knowledge base contains redundant knowledge. The second criteria determines if the knowledge is consistent, such that during execution conflicting information is not asserted into WM. The third criteria, completeness, addresses whether the knowledge is sufficient to cover the KBS specification. Simple forms of these criteria can be established by structural analysis of the system rules, while complex forms require semantic information about the conditions and actions of the rules 4,7,10,20,22,28 .<sup>w</sup> <sup>x</sup>

Many of the automated verification tools to detect the anomalies from the above criteria limit the rules and WMEs to propositions 2,9,11,14,24,27,29 , restricting their direct use in a hybrid system. In addition, some<sup>w</sup> <sup>x</sup> tools require a specific language in which the KBS must be built, such as ART 15 and OPS5 19 , or require <sup>w x</sup> <sup>w x</sup> only monotonic KBSs in which information cannot be deleted 8,12 . More general tools may rely on mapping<sup>w</sup> <sup>x</sup> rules to canonical formats for examination, such as decision tables 4,5,28 , Petrie nets 1 , and contradiction-<sup>w</sup> <sup>x</sup> <sup>w x</sup> tolerant truth maintenance systems CTMS 32 , or may simply perform multiple algorithmic checks for distinctŽ . <sup>w</sup> <sup>x</sup> anomalies 20,22 . Formal derivation, specification refinement, and theorem proving have also proved useful in<sup>w</sup> <sup>x</sup> verifying rule-based systems 23,25,30,31 .<sup>w</sup> <sup>x</sup>

## 2.3. Hybrid KBSs

A more robust KBS representation is that of a hybrid system. Hybrid systems utilize object-oriented concepts along with rule-based inference, providing the flexibility and representational ease of rules with the benefits of encapsulation, reusability, and the active nature of objects. Within a hybrid system, objects have attributes which may have attached monitors. Objects form the foundation of working memory. Inheritance among objects places a structure and classification over working memory. Methods are used as global functions that can be accessed by objects via message passing and rules. Monitors are a particular type of method that are activated as side-effect functions when the value of the attribute is accessed or changed.

We focus on three distinct monitors: Access, Before-Change Ž . represented as B-C , and After-Change Ž .represented as A-C , which activate when the attribute to which it is attached is read, before the attribute is changed, and after the attribute is changed, respectively. For example, in Fig. 1, the Employee object has a Time-Worked attribute with an A-C monitor named Overtime attached. After the Time-Worked attribute is changed, the function Overtime is activated. This function adjusts the Salary attribute to reflect overtime pay if Time-Worked is greater than forty hours. Monitors can send messages to other objects, call other methods, and<sup>r</sup>or initiate rule-based inference over all or part of the objects in the system.

Object Class Name: employee

Name: ...

Salary: ...

Time-Worked: ... A-C Monitor: Overtime

If Time-Worked > 40

$$
\text { Then   Salary } := \text { Salary } + 1. 5 * \text { Hourly } * (\text { Time - Worked } - 4 0)
$$

Hourly: ...

Fig. 1.

## 2.4. Verification of hybrid KBSs

Research in the verification of hybrid systems is still in its early stages. O’Leary 17 describes how the<sup>w</sup> <sup>x</sup> traditional criteria of redundancy, consistency and completeness can be established within the structure of the object or frame, separate from the remainder of the KBS. Lee and O’Keefe 10 have developed an algorithm for<sup>w</sup> <sup>x</sup> the post-verification of subsumption anomalies in hybrid systems. Their research details the interactions between rules that use general object class information as condition and action elements and rules that use instances of object classes. We will present their research in more detail in Section 4, where we extend their approach to cover more anomalies. Additional research in the formal construction and refinement of hybrid systems has been undertaken from both the traditional viewpoint of program derivation 30 and the methodological viewpoint of <sup>w</sup> <sup>x</sup> prototyping 6 .<sup>w</sup> <sup>x</sup>

## 2.5. Notation

For presentation purposes, we will represent an object in a rule using a traditional tuple format without the associated monitors. The object class name appears first, followed by tuples representing attributes and their values. CEs and AEs in rules are separated by commas. For example, the object in Fig. 1 would be represented as

<sub>Ž</sub> <sub>.</sub> Employee Name Ž . Ž . Ž . Ž . x Time-Worked y Salary z Hourly w

To employ the use of frame-based predicates, such as Is-A and Has-A that form relationships between object classes, we allow the object class names to be instantiated in a rule, where

Is-A v, Employee Ž .

matches

Is-A Manager, Employee Ž .

provided that Manager is a subclass of Employee. The assertion of new relationships between objects or the creation of new WMEs as AEs are represented as positive predicates in the RHS of a rule, e.g.,

Is-a Object-Class , Object-Class . Ž .

AEs that modify newly asserted WMEs or existing WMEs are preceded by a Modify predicate, e.g.,

Modify Object-Class, Attribute, new value , <sub>Ž</sub> <sub>.</sub> Ž .

for each attribute modified. For example, the rule below

$$
\mathrm{Is} - \mathrm{A} (\mathrm{x}, \text { Audi }), (\mathrm{x} (\text { doors } 4) (\text { color   red }))
$$

$$
\text { Is } - \mathrm{A} (\mathrm{x}, \text { Sedan }), \text { Modify } (\mathrm{x} (\text { color   blue }))
$$

means that if there is an instance of Audi that is red with four doors, then make an instance of Sedan by the same name and change the color to blue.

When we discuss the attachment of monitors, we use the notation

Object-Class:Attribute

to represent the value of an attribute of a particular object class on which the monitor has some effect.

## 3. Subsumption anomalies

In hybrid KBSs, Lee and O’Keefe have previously defined one type of interaction called a subsumption anomaly <sup>w</sup> <sup>x</sup>10 and provide an extensive discussion of the effect of subsumption anomalies on hybrid systems. We discuss this anomaly in detail below.

We assume in the following examples that the whole object tuple is matched in the LHS of the rule. For brevity we omit this matching and concentrate only on the frame-based predicates that relate objects. Rules have been represented using literals of the form $\mathrm { P } ( x , \mathrm { A l } )$ . Here, P represents a predicate, such as Is-A or Has-A, Al is an object represented as a class in a hybrid system , and x is a variable which is bound to an object. TheŽ . common notation will be that upper case variables with letter–number combinations will be class variables, e.g., Al. Lower case letter–number combinations will be subclass variables, e.g., all. Lower case variables from the end of the alphabet, e.g., x, will be simple variables. Literals in the above form are combined together to represent rules as follows:

$$
\mathrm{Q} (\mathrm{y}, \mathrm{B} 1), \mathrm{P} (\mathrm{x}, \text { all }), \mathrm{Q} (\mathrm{y}, \mathrm{b} 1 1) \rightarrow \mathrm{R} (\mathrm{x}, \mathrm{t} 1 1)
$$

Consider the following example:

IF x is a student, x has taken Math1 AND x is a Senior THEN x can take Statistics

In the above rule, the variable x is instantiated with all the students who have taken the Math1 course and are seniors. The actions specified in the consequent are then asserted with the instantiated value of x. This rule can also be written as:

$$
\text { is - a(x, Student), has - taken(x, Math1), is - a(x, senior) }
$$

can-take x, Statistics Ž .

and in a generic form as the first rule of this section.

## 3.1. Definition of subsumption

Subsumption using objects has been defined in 10 as follows:<sup>w</sup> <sup>x</sup>

Subsumption: Atomic subsumption occurs when $\mathrm { P _ { k } } ( x , \mathrm { a _ { i j } } ) \Rightarrow \mathrm { P _ { k } } ( y , \mathrm { A _ { i } } )$ if there exists a substitution  and an i such that $x \sigma = y$ and $\mathbf { a } _ { i j } \in \mathbf { A } _ { i }$

The above definition indicates that the clause $\mathrm { P } _ { \mathbf { k } } ( x , \mathbf { a } _ { i j } )$ is subsumed by the clause $\mathrm { P _ { k } } ( y , \mathrm { A } _ { i } )$ since there exists a substitution $s = \{ y / x \}$ , that is, y can be substituted for variable x, and $\mathrm { a } _ { i j }$ is a subclass of $\mathbf { A } _ { i } . \mathbf { P } _ { k } ( y , \mathbf { A } _ { i } )$

is a more general statement that subsumes $\mathrm { P } _ { \mathrm { k } } ( x , { \mathbf { a } } _ { i j } ) .$ , a more specific statement. The above definition assumes an object hierarchy of two levels as follows:

$$
\text { Let } S = A _ {1} \cup A _ {2} \cup \dots \cup A _ {n}, \text { where } A _ {i} \{a _ {i 1}, a _ {i 2}, \dots , a _ {i j} \}
$$

Subsumption has further been classified as partial and complete subsumption, as follows:

Complete Subsumption: A conjunction of n subsuming literals subsumes a conjunction of n subsumed literals if there exists and for all n $( \mathrm { P } _ { n } ( \mathrm { x } , \mathrm { a } _ { i j } ) \Rightarrow \mathrm { P } _ { n } ( \mathrm { x } , \mathrm { A } _ { i } ) )$

The above definition implies that if every object constant used in the literal is a subclass of every object constant used in the corresponding literal, a conjunction of all subsuming literals completely subsumes the conjunction of all subsumed literals.

The taxonomy of subsumption related anomalies examined by Lee and O’Keefe 10 include redundant,<sup>w</sup> <sup>x</sup> conflicting semantically and structurally , subsumed, and circular rules, and unnecessary IF conditions. TheseŽ . anomalies have been defined differently in hybrid systems from traditional rule based systems due to the effectŽ . of subsumption.

## 3.2. Taxonomy of Õerification criteria for hybrid systems

This section is an overview of the approach taken by Lee and O’Keefe 10 . They have presented an<sup>w</sup> <sup>x</sup> approach to perform subsumption analysis and static checks for what they consider as consistency related anomalies in hybrid systems. This approach uses rule clustering to achieve gradual decomposition of rules and checking subsumption only among rules within a cluster using adjacent matrices. The subsumption information is then used to find other static anomalies in the rule base. Their procedure for identifying anomalies consists of the following steps:

1. Cluster the rule set and generate a rule connection graph.

2. Identify the subsumption relationship among conditions and actions.

3. Check for anomalies.

The following sections discuss the steps mentioned above in detail.

## 3.2.1. Rule clustering

Rule clustering or grouping improves modularity and can lead to substantial savings in time during the verification process 13 . One type of grouping is to measure the distance between two rules based on the <sup>w</sup> <sup>x</sup> criteria of relatedness. Relatedness is determined by calculating the distance between rules using the distance metric and clustering rules with a minimum distance.

The rule clustering technique proposed for hybrid systems is an extension of the method proposed by Mehrotra 13 . In order to incorporate structural semantics among objects, a concept of <sup>w</sup> <sup>x</sup> oÕerlapping literals has been used. These are literals that are either syntactically the same between a pair of rules as defined in Mehrotra’s distance metric or that hold the same predicate with hierarchically related object constants. The distance metric used by Lee and O’Keefe 10 is:<sup>w</sup> <sup>x</sup>

$$
\mathrm{D} _ {d f} \left(\mathrm{r} _ {i}, \mathrm{r} _ {j}\right) = \frac {\text { Total   \#   of   literals   in   the   consequent   of   r } _ {i} \text { and   antecedent   of   r } _ {j}}{\left(\# \text {   of   overlapping   literals   in   the   consequent   of   r } _ {i} \text {   and   antecedent   of   r } _ {j}\right)}
$$

where Ža of overlapping literals in the consequent of $\mathbf { r } _ { i }$ and the antecedent of $\mathbf { r } _ { j } ) = - 1$ for unrelated rules. After measuring the distance between two rules based on their relatedness, rules with the minimum distance are clustered together.

## 3.2.2. Subsumption relationship

A previously defined algorithm for subsumption analysis uses an adjacency matrix 10 . Subsumption <sup>w</sup> <sup>x</sup> relations among the literals used in a pair of rules is identified by transforming the conditions and actions into the matrix. Semantic information regarding object hierarchy is used to input matrix values, which are examined for the presence of subsumption among the rules. For example, we propose the following rules for analysis.

$$
\mathrm{R} 1: \mathrm{P} (x, \mathrm{A} _ {1}) \wedge \mathrm{Q} (y, \mathrm{A} _ {2}) \wedge \mathrm{T} (w, \mathrm{A} _ {3}) \rightarrow \mathrm{V} (x, \mathrm{g} _ {1 1})
$$

$$
\mathrm{R} 2: \mathrm{P} (x, \mathrm{a} _ {1 1}) \wedge \mathrm{Q} (y, \mathrm{a} _ {2 1}) \wedge \mathrm{T} (w, \mathrm{A} _ {3}) \rightarrow \mathrm{V} (x, \mathrm{g} _ {1 1})
$$

where ${ \bf a } _ { 1 1 }$ is a subclass of $\mathbf { A } _ { 1 }$ and $\mathbf { a } _ { 2 1 }$ is a subclass of $\mathbf { A } _ { 2 } . \mathbf { L e t }$ <sup>w</sup> <sup>x</sup> S be the adjacency matrix used for subsumption analysis, I be a set of indices for <sup>w</sup> <sup>x</sup> S , and $\mathbf { C } _ { i }$ be the set of objects used in rule $i . \mathrm { ~ I ~ } _ { x }$ is determined as:

$$
\mathrm{I} _ {x} = \left(\mathrm{C} _ {i} \cup \mathrm{C} _ {j}\right) - \left(\mathrm{C} _ {i} \cap \mathrm{C} _ {j}\right)
$$

<sup>w</sup> <sup>x</sup> S is subdivided into four submatrices according to the objects in the rule. Therefore, $\begin{array} { r } { S = \frac { S _ { 1 } } { S _ { 3 } } | _ { \frac { { S } _ { 2 } } { S _ { 4 } } } ^ { \frac { S _ { 2 } } { S _ { 4 } } } } \end{array}$ where $\mathbf { S } _ { 1 }$ and $\mathbf { S } _ { 4 }$ contain only the relationships between objects of the same rule, while $\mathbf { S } _ { 2 }$ and ${ \bf S } _ { 3 }$ contain information regarding the object relationships between the two rules. An entry of $\cdot _ { 1 } \cdot$ in the adjacency matrix <sup>w</sup> <sup>x</sup> S indicates a hierarchical relationship between the corresponding objects. The hierarchical relationship is defined as follows. If the column index is the same class or a subclass of the row index, $\mathrm { ~ a ~ } ^ { \cdot } 1 ^ { \cdot }$ is entered. Otherwise, a zero is entered. Subsumption between the pair of rules is identified by looking at submatrices $\mathbf { S } _ { 2 }$ and ${ \bf S } _ { 3 }$ . For all $i ,$ if $\mathbf { S } _ { 2 i i } = 1$ or $\mathbf { S } _ { 3 i i } = 1$ , then the two sets of clauses are in complete subsumption. Note that 1 the appropriate Ž . ordering of related objects as indices is necessary for correct analysis and 2 if there are multiple subclasses forŽ . a single class, then that class index must be repeated in the right order to have the correct diagonal in $\mathbf { S } _ { 2 }$ and ${ \bf S } _ { 3 }$

Consider the analysis of rules R1 and R2. In this case ${ \mathrm { I } } _ { x } = \{ { \bf A } _ { 1 } , { \bf A } _ { 2 } , { \bf a } _ { 1 1 } , { \bf a } _ { 2 1 } \}$ and the adjacency matrix is:

<table><tr><td></td><td> $A_{1}$ </td><td> $A_{2}$ </td><td> $a_{11}$ </td><td> $a_{12}$ </td></tr><tr><td> $A_{1}$ </td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $S = A_{2}$ </td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td> $a_{11}$ </td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $a_{21}$ </td><td>0</td><td>0</td><td>9</td><td>1</td></tr></table>

Analyzing $\mathbf { S } _ { 2 }$ and ${ \bf S } _ { 3 }$ , the above matrix shows complete subsumption between rules R1 and R2.

## 3.3. Addressing the problems with the current approach

In this section, we discuss some concerns with the approach by Lee and O’Keefe in detecting subsumption anomalies 10 . There are two areas of concern. The first concern involves the rule clustering approached used.<sup>w</sup> <sup>x</sup> The second involves the way that predicates are taken into account in the detection.

## 3.3.1. Rule clustering

The rule clustering approach described in Section 3.2.1 is useful when addressing the characteristics of systems with a hierarchical structure that are likely to contain a small number of disjoint rule groups. The use of such grouping in classification systems has been advocated 13 , since the fundamental characteristic of such<sup>w</sup> <sup>x</sup> systems is that flow of data takes place from the consequent of one rule to antecedents of other rules. Traditional rule-based systems consist of possibly multiple sets of disjoint rules, where rules in a set are related by the fact that the flow of data occurs from the consequent of one rule to the antecedent of another. This characteristic of rule-based systems allows the effective use of rule grouping. However, we have found that this method is not foolproof for the subsumption analysis of hybrid system rules. For example, consider the following rules:

$$
\mathrm{R} 3: \mathrm{P} (x, \mathrm{G} _ {1}) \wedge \mathrm{Q} (x, \mathrm{A} _ {1}) \rightarrow \mathrm{P} (x, \mathrm{g} _ {1 1})
$$

$$
\mathrm{R} 4: \mathrm{P} (x, \mathrm{G} _ {1}) \wedge \mathrm{Q} (x, \mathrm{a} _ {1 1}) \rightarrow \mathrm{P} (x, \mathrm{g} _ {1 1})
$$

where ${ \bf a } _ { 1 1 }$ is a subclass of $\mathbf { A } _ { 1 } , \mathbf { g } 1 1$ is a subclass of $\mathbf { G } _ { 1 }$ .

For the above rules, the distance metric as described in Section 3.2.1, $\mathrm { D } _ { d f } = 3$ . This means that the two rules, R3 and R4, would be put in the same group and would be connected. Given this type of relatedness, rules in a group are connected to at least one other rule in the same group. However, not all rules in a group are connected. In Lee and O’Keefe’s approach, only unconnected rules from the same group are taken up for pairwise analysis of subsumption. This means that the above rules rules R3 and R4 would not be analyzed forŽ . subsumption even though complete subsumption exists between the rules. Thus, the above method of clustering rules based on the antecedent and consequent may not appropriately identify all the rules that need subsumption analysis.

Rule clustering depends largely on the nature of the rule base. A more general clustering approach is needed to more cleanly partition the hybrid rules into related groups such that complete verification not just Ž subsumption analysis can be performed on select rule sets. .

## 3.3.2. Subsumption algorithm

The algorithm for subsumption analysis described in Section 3.2.2 was found to be restricted by the fact that it does not look at the predicates used in the rules. As shown earlier, complete subsumption among rules R1 and R2 is correctly identified. However, consider the following rule, R5 when examined with R2.

$$
\mathrm{R} 2: \mathrm{P} (x, \mathrm{A} _ {1}) \wedge \mathrm{Q} (y, \mathrm{A} _ {2}) \wedge \mathrm{T} (W, \mathrm{A} _ {3}) \rightarrow \mathrm{V} (x, \mathrm{g} _ {1 1})
$$

$$
\mathrm{R} 5: \mathrm{P} (x, \mathrm{a} _ {1 1}) \wedge \mathrm{Q} (y, \mathrm{a} _ {2 1}) \wedge \mathrm{U} (w, \mathrm{A} _ {3}) \rightarrow \mathrm{V} (x, \mathrm{g} _ {1 1})
$$

where ${ \bf a } _ { 1 1 }$ is a subclass of $\mathbf { A } _ { 1 }$ and $\mathbf { a } _ { 2 1 }$ is a subclass of $\mathbf { A } _ { 2 }$ .

In this case, $\mathrm { I } _ { x }$ and <sup>w</sup> <sup>x</sup> S would be exactly the same as in the analysis of R1 and R2, since the objects are the same. Hence, R2 and R5 would be identified as completely subsumed rules. However, because the predicates differ, there is no subsumption between these two rules. The analysis of partial subsumption also has the same drawback since $\mathbf { C } _ { i }$ and <sup>w</sup> <sup>x</sup> S are identified in the same manner.

## 3.3.3. Checking for anomalies

The anomaly checking procedure defined by the decision tree can be used to identify redundant, subsumed, and circular rules, and unnecessary IFs and conflicts. These anomalies can be detected using static pairwise analysis of rules. However, a number of other anomalies also exist in traditional rule based systems that have not been extended to hybrid systems. These include missing rules, unreachable goals, and dead end rules. These anomalies are also affected by subsumption and class hierarchy and thus need a different approach for their detection. In Section 3.4 we extend the definitions for these anomalies and discuss the effect of subsumption on these anomalies.

The drawbacks in the subsumption algorithm listed in Section 3.3.2 required the algorithm to be extended to handle cases that it previously could not. Section 3.4 presents the proposed extensions.

## 3.4. Extending the subsumption algorithm

We propose an extension of the subsumption algorithm that takes the objects and the corresponding predicates into account while analyzing rules to identify subsumption. This can be achieved by defining $\mathrm { I } _ { x }$ and <sup>w</sup> <sup>x</sup> S as follows. Let $\mathrm { P } _ { i }$ be the set of predicate <sup>r</sup>object pairs used in rule i. A predicate<sup>r</sup>object pair is represented as P, O , where O is an object and P is the predicate that O is associated with. The set of elements inŽ . $\mathrm { { I } } _ { x }$ is newly defined as:

$$
\mathrm{I} _ {x} = \left(\mathrm{P} _ {i} \cup \mathrm{P} _ {j}\right) - \left(\mathrm{P} _ {i} \cap \mathrm{P} _ {j}\right)
$$

The adjacency matrix <sup>w</sup> <sup>x</sup> S is created using $\mathrm { I } _ { x }$ as indices as described previously in Section 3.2.2. However, an entry of $\cdot _ { 1 } ,$ in the adjacency matrix <sup>w</sup> <sup>x</sup> S indicates a hierarchical relationship between the corresponding objects only if they are within the same predicate in the two rules. Complete subsumption between the pair of rules is identified in the same manner as in Section 3.2.2. This new approach allows us to identify common objects within the same predicates in the two rules, and correctly identifies subsumption relationships between the rules.Consider the example shown previously:

$$
\mathrm{R} 2: \mathrm{P} (x, \mathrm{A} _ {1}) \wedge \mathrm{Q} (y, \mathrm{A} _ {2}) \wedge \mathrm{T} (w, \mathrm{A} _ {3}) \rightarrow \mathrm{V} (x, \mathrm{g} _ {1 1})
$$

$$
\mathrm{R} 5: \mathrm{P} (x, \mathrm{a} _ {1 1}) \wedge \mathrm{Q} (y, \mathrm{a} _ {2 1}) \wedge \mathrm{U} (w, \mathrm{A} _ {3}) \rightarrow \mathrm{V} (x, \mathrm{g} _ {1 1})
$$

Previous analysis of rules R2 and R5 resulted in identifying them as completely subsumed rules. However, in this case, I is formed as follows.

$$
\begin{array}{l l}\mathrm{P} _ {1} \cup \mathrm{P} _ {5}&= \left\{ \right.\left(\mathrm{P}, \mathrm{A} _ {1}\right), \left( \right.\mathrm{Q}, \mathrm{A} _ {2}, \left(\mathrm{T}, \mathrm{A} _ {3}\right), \left(\mathrm{V}, \mathrm{g} _ {1 1}\right), \left(\mathrm{P}, \mathrm{a} _ {1 1}\right), \left(\mathrm{Q}, \mathrm{a} _ {2 1}\right), \left(\mathrm{U}, \mathrm{A} _ {3}\right)\left. \right\}\\\mathrm{P} _ {1} \cap \mathrm{P} _ {5}&= \left\{\left(\mathrm{V}, \mathrm{g} _ {1 1}\right) \right\}\\\mathrm{I} _ {x}&= \left\{ \right.\left(\mathrm{P}, \mathrm{A} _ {1}\right), \left( \right.\mathrm{Q}, \mathrm{A} _ {2}, \left(\mathrm{T}, \mathrm{A} _ {3}\right), \left(\mathrm{P}, \mathrm{a} _ {1 1}\right), \left(\mathrm{Q}, \mathrm{a} _ {2 1}\right), \left(\mathrm{U}, \mathrm{A} _ {3}\right)\left. \right\}\end{array}
$$

The resulting matrix S is described as follows.

<table><tr><td></td><td> $(P, A_1)$ </td><td> $(Q, A_2)$ </td><td> $(T, A_3)$ </td><td> $(P, a_{11})$ </td><td> $(Q, a_{12})$ </td><td> $(U, A_3)$ </td></tr><tr><td> $(P, A_1)$ </td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $(Q, A_2)$ </td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $(T, A_3)$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $(P, a_{11})$ </td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $(Q, a_{21})$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $(U, A_3)$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr></table>

The last entry in the diagonal of $\mathbf { S } _ { 2 }$ and ${ \bf S } _ { 3 }$ are 0 because even though the objects are the same, they belong to different predicates. These objects would not have been considered without the extended definition. The submatrices $\mathbf { S } _ { 2 }$ and ${ \bf S } _ { 3 }$ correctly indicate the absence of complete subsumption.

## 3.5. CoÕering additional anomalies

A method for static analysis of potential anomalies has been developed by Lee and O’Keefe 10 . The<sup>w</sup> <sup>x</sup> following is a list of anomalies to which their method applies.

Ž . 1 Subsumed rules: Subsumed rules arise due to the subsumption relationship between literals used in the rules.

Ž . 2 Redundancy: Redundancy arises as a direct consequence of subsumed rules.

Ž . 3 Semantic conflict: Semantic conflict occurs when any pair of rules which have the same conditions lead to semantically different actions, among which there exists partial or complete subsumption relationships.

Ž . 4 Structural conflict: Structural conflict is identified by subsumption relationships in the condition and action parts of the rules.

Ž . 5 Unnecessary conditions: In hybrid systems, unnecessary conditions can occur when an action in a rule is propagated to another rule as a condition and results in at least one subsumption relationship between a pair of literals in the condition clause.

Ž . 6 Unreachable goals: Unreachable goals may arise due to mutual exclusivity among objects used in the condition of the same rule.

Ž . 7 Circular rules: A cycle of rule actions. The definition of circular rules has been extended for hybrid systems.

The above anomalies typically require pairwise comparisons among rules in the rule base. We extend the subsumption analysis to the following anomalies that require the use of the whole rule base for their detection. Therefore, we cannot use the adjacent matrix approach. Instead, we need additional detection algorithms similar to those found in the rule-based system literature.

## 3.5.1. Dead end rules

Dead end rules in forward chaining systems are those that have actions that do not affect any conclusions Ž .i.e., are not goals and are not used by other rules to generate any other conclusion. In traditional systems, dead end rules can be detected by searching the rule-base for the presence of clauses that do not appear in the condition of any other rule. A syntactic comparison is enough to detect these anomalies. In hybrid systems, rules for traditional dead end rules do not apply, since subsumption may cause further chaining that is not possible in traditional systems. Dead end clauses in hybrid systems would occur if given a clause in the action of a rule which is not a goal, the same clause or its subsuming clause does not exist in the condition of another rule assuming forward-chaining inference. The presence of dead end rules may be an indication of unnecessary or missing rules.

The following example shows how dead end rules may be avoided due to subsumption.

$$
\mathrm{R6:Q} (x, \mathrm{a} _ {1 1}) \rightarrow \mathrm{P} (y, \mathrm{g} _ {1 1})
$$

$$
\mathrm{R} 7: \mathrm{P} (y, \mathrm{G} _ {1}) \rightarrow \mathrm{R} (x, \mathrm{T})
$$

Let RŽ .x, T be the goal. Given $\mathrm { Q } ( \boldsymbol { x } , \ \mathbf { a } _ { 1 1 } )$ in WM, if rule R6 fires, then rule R7 would fire because of subsumption relationship between clauses in the action and condition of R6 and R7 respectively. So even though the clause $\mathrm { P } ( y , \mathbf { g } _ { 1 1 } )$ is not present in the condition of any other rule, dead end condition is avoided due to the presence of a subsuming clause.

## 3.5.2. Unreachable rules

A rule is unreachable if it cannot be fired during the chaining process. In traditional systems, unreachable rules exist if the premise of a rule contains a clause that cannot be taken as input and is not asserted by any other rule. This can be detected by syntactically checking for the presence of clauses used in the condition part of the rule in the consequent of other rules in the rule-base. In hybrid systems, a rule is unreachable if it contains a clause in the premise that is either:

1. Not an input provided by the user.

2. Not present in the action part of any other rule.

3. Does not have a subsumed clause present in the action part of any other rule.

A rule satisfying the above conditions would be an unreachable rule in a forward-chaining system. This is equivalent to a dead end rule in a backward-chaining system. A rule is unreachable in a backward-chaining system if it contains a clause in the action part of the rule that is either:

1. Not a goal.

2. Not present in the condition part of any other rule.

3. Does not have a subsuming clause present in the condition part of any other rule.

## 3.5.3. Missing rules

Missing rules are characterized by a failure to cover all legal values of some input. These are identified by looking at input combinations that do not lead to the goal. In hybrid systems, given a set of inputs, inability to use these clauses or their subsuming clauses to infer the goal is an indication of a missing rule. Missing rules for traditional rule based systems has been defined in terms of deficiency in Ref. 21 .<sup>w</sup> <sup>x</sup>

Given an environment E is a non-empty set of clauses <sup>3</sup>. A goal environment $\mathrm { P _ { g } }$ , for a goal g is a set of clauses which are used to infer g. A goal is inferable from an environment E iff for all clauses ${ \mathrm { c } } \in { \mathrm { E } } , { \mathrm { c } } \in { \mathrm { P } } _ { \mathrm { g } }$ or $\mathrm { C } \in \mathrm { P } _ { g }$ , where C subsumes c. In other words, a goal g is inferable from an environment E if only the clauses in the environment E or their subsuming clauses can be used to infer goal g. An environment E is coÕered by rule set $\mathrm { R _ { g } }$ iff g is inferable from E. The function covered g,Ž $\mathrm { E } , \mathrm { R _ { \mathrm { g } } } )$ is true if E is covered by $\mathrm { R _ { g } }$ for a goal g. The rule set $\mathsf { R } _ { \mathrm { g } }$ is deficient for g if covered g,Ž $\mathrm { E _ { g } , R _ { g } ) }$ does not hold for some $\mathrm { E _ { g } \in U _ { g } }$ , where $\mathbf { \check { U } } _ { \mathrm { g } }$ is the set of all possible environments. Uncovered environments are an indication of missing rules.

## 3.6. Automatic Õerification tool

An automated tool for the verification of hybrid KBS anomalies has been developed. This system looks at rules from hybrid systems and checks for possible subsumption anomalies. A decision tree based approach has been developed in 10 that uses subsumption information to identify anomalies. This approach translates very <sup>w</sup> <sup>x</sup> well to an automated tool for anomaly checks. Identification of completeness anomalies is carried out separately as it requires a different detection procedure. The algorithm presented in Section 4.1 that extends the approach presented by Lee and O’Keefe is used for the subsumption analysis.

Rules, objects, goal states and the input states are specified in a generic format and is language independent. This information is then analyzed to find subsumption anomalies. The tool can check for redundant rules, subsumed rules, unnecessary conditions, structural conflict, semantic conflict and unreachable goals by pairwise analysis of rules in the rule base.

Completeness anomalies identified by the system include dead end rules, unreachable rules, and missing rules. These anomalies require analysis of the complete rule base. Pairwise comparison used for static analysis is not sufficient. In case of dead end and unreachable rules, the tool presently uses a brute force approach of comparing literals in the rules to check for their presence or absence in other rules. A dead end rule is identified by searching for literals that occur in the action of a rule, and are not used in the condition of any other rule, and is not the goal assuming a forward chaining scheme . The syntactic check required in the case for traditionalŽ . rule-based systems has been extended to accommodate checks for possible subsumption among rules. This is required because subsumption can cause rule chaining in hybrid systems that is not found in traditional rule-based systems. Thus, a rule that is a dead end rule in a traditional system may be prevented from being one in a hybrid system. The algorithm uses subsumption information to identify such cases and to identify all rules that lead to the dead end condition. The user specifies the goal states, which are needed to check the termination of the chaining process. The detection of unreachable rules uses a similar approach. The algorithm checks literals in the condition of a rule to see if they are asserted by other rules. Presence of an unassertable literal in the condition of a rule indicates that it is an unreachable rule. However, in hybrid KBSs, this rule may fire due to subsumption. Subsumption information is thus used to determine if the rule is actually unreachable. Information about input variables is also required in this case and must be provided by the user.

Detection of missing rules uses an extension of the approach proposed by Ref. 21 . This approach uses a set<sup>w</sup> <sup>x</sup> of inputs to find missing rules. The goal environment for a goal represents the set of literals needed to reach the goal from an input. Subsumption information is used to determine the goal environment in a hybrid KBS. The goal environment is then used to determine if the goal can be reached from a starting state. Inability to do so indicates missing rules. The algorithm developed creates the goal environment, and compares it with the input environment. A syntactic comparison of the goal environment and the input environment in traditional systems has been extended to search for the presence of subsumed literals. This process is described in Section 4.5.3 <sup>w</sup> <sup>x</sup> 21 . The input environment is created efficiently by starting with small sets of inputs, and then creating corresponding supersets. Detection of missing rules using a set of inputs excludes the need to continue with its supersets 21 . This approach saves the effort of not having to check all possible input combinations.

The system uses an internal representation for rules and the class hierarchy information. This has been done to achieve language independence in the algorithms used. We are currently identifying other automated methods used for verifying traditional rule-based systems that can be extended to more efficiently detect the anomalies in hybrid KBSs.

## 4. Interaction anomalies

There are many kinds of anomalies possible in a hybrid KBS. Subsumption anomalies are one kind that concentrate on the interaction between rules and inheritance in objects. In this section, we discuss anomalies caused by interactions between rules and monitors. In general, anomalies arise as a result of monitor-rule interactions when unexpected matching in the antecedent of a rule occurs or when unexpected changes or results occur out of the evaluation of a rule. The possible interactions and their detection depends on when the monitor executes with respect to the rule. In our model, a monitor executes immediately upon activation. This mode of execution means that the monitor may interrupt the rule matching, firing, or both. The immediate mode of executing triggers or daemons, such as monitors, is also commonly found in active databases, where similar anomalies can occur 18 .

## 4.1. Definition and example of interaction anomalies

There are two types of anomalies that can arise as a result of monitor-rule interaction: 1 altering theŽ . expected preconditions for the rule to fire and 2 altering the expected postconditions caused by rule firing. TheŽ . first anomaly type deals with interactions between only Access monitors and CEs, while the second deals with interactions between all monitor types and AEs. The interactions that can exist between a rule and a monitor execution is shown by the following hypothetical situation. The rule shown here checks the level of a tank and increases the level by a specific amount. Monitor M1 is an A-C After-Change monitor attached to attributeŽ . program:complete, where program is the object and complete is one of its attributes. M1 ensures that the level of the tank does not exceed 100 when the attribute is changed. Monitor M2 is an A-C monitor that changes the attribute tank:level-changed when executed.

R8: tank level x , program complete no <sub>Ž</sub> <sub>. Ž</sub> <sub>.</sub> Ž . Ž .

Modify tank level <sub>Ž</sub> <sub>. Ž</sub> <sub>.</sub> Ž . Ž . x <sup>q</sup> 50 , Modify program complete yes

M1: if tank:levelŽ .<sup>)</sup>100 then tank:level:<sup>s</sup>100

M2: tank:level-changed:<sup>s</sup>yes

Consider the execution of rule R8 with monitor M1 attached to the program:complete attribute. Assume that WM is as depicted in Fig. 2. We list the attributes in monitor format for clarity. Rule R8 increases the value of the attribute tank:level by 50 to 120. However, monitor M1 executes when program:complete is changed as an AE in R8. M1 changes the value of tank:level to 100. The initial and final state of the working memory resulting from the above interaction is shown in Fig. 2. The values in square brackets represent the values that would have resulted without the monitor attached to the rule.

As shown in Fig. 2, the value of attribute tank:level is different from what would have resulted from the rule execution without the monitor. Such an interaction results in an unpredictable state of WM and is therefore a potential anomaly. We say ‘potential’ because it may be the case that M1 is specifically created to keep the value at 100. However, it may also be the case that the monitor was created without knowledge of the rule causing the increase over 100, causing unexpected behavior. Even more serious can be an interaction that creates states with conflicting values, for example, the monitor setting attribute program:complete to no while the rule sets it to yes.

![](/api/attachments/8QQWUX3T/fulltext/images/d4c11b4f58ece7fb1cb8dc41ce696c81f6dc72ada0e167369fb4b19d5645414c.jpg)  
Fig. 2.

Fig. 3 shows the attributes modified as a result of executing rule R8. Dotted lines show the attributes that are modified by a monitor. This is an example of a poorly structured rule base in which rule and monitor interaction occurs. This is due to the fact that the same attribute, in this case tank:level, is modified by both the rule and the monitor, resulting in the interaction.

![](/api/attachments/8QQWUX3T/fulltext/images/ace4fff45cd48514a0113a8e83d775168dc2393cb8754bbdb08fa8992c088427.jpg)  
Fig. 3.

![](/api/attachments/8QQWUX3T/fulltext/images/536f5eede5bbe54cdcde81704b18eafb11bc162be1780f3ebc57ef8a0775fbe5.jpg)  
Fig. 4.

The execution of rule R8 without M1 and only monitor M2 attached to tank:level does not cause any interaction anomalies. This can be seen in Fig. 3. As shown in Fig. 4, none of the attributes have multiple modifications during the course of execution of rule R8. Thus, no anomalies are present.

The monitor-rule interaction anomalies are characterized by the way that changes to WM can occur that invalidate the WM state over which a rule fires. Type 1 anomalies occur because monitor firing may changeŽ . WM to a different state than that assumed when the rule began the match phase. Type 2 anomalies occur whenŽ . a relationship between object and attribute prescribed by the rule is not present in WM and when a postcondition no longer holds as it would have if the rule executed without interference. We categorize each anomaly type into subtypes and provide an example of each subtype.

## 4.1.1. Type 1 : Altering the expected preconditions of rule firing( )

There are two cases of this anomaly.

Ž .a Inaccurate inhibition or incitation of rule firing:

A change is made to an object attribute x before the CE checks for attribute x. Given the previous rule R8 and an Access monitor attached to the attribute tank:level whose execution performs the assignment

program:complete: yes

a possible anomaly occurs because the monitor changes the state of program:complete during its match in the LHS of the rule. Thus, the rule will not match as it should because the monitor interrupts the matching process.

Ž . b Rule firing with a different WM that was initially matched: A change is made to an object attribute x after the CE that matches the attribute x.

Given the rule R8 above, this anomaly would exist if an Access monitor is attached to the attribute program:complete that continually decreased the level of the tank in tank:level during the execution of the KBS as in

tank:level:<sup>s</sup>tank:level-10

Interaction of this monitor with the rule will cause a change made to attribute tank:level after the CE has been matched in the rule, invalidating the match.

4.1.2. Type 2 : Altering the expected postconditions of rule firing ( )

There are three cases of this anomaly.

Ž .a Monitor change before rule modification: A monitor changes an object attribute on which an AE depends before the AE modification can be performed. This anomaly is shown using the following rule, R9

and the A-C monitor M3 attached to program:complete which executes the following statement:

M3: tank:level:<sup>s</sup>100

Without the monitor, the execution of R9 would set up the relationship that input:amount<sup>q</sup>70<sup>s</sup>tank:level. Because the tank:level attribute is changed, the input:amount attribute in the second AE of R9 will no longer have the expected value or relationship from the rule firing.

Ž . b Rule modification before monitor change: An AE modification is performed and then at least one of the object attributes on which the AE depended is changed by a monitor.

The following rule, R10,

$$
\text { R10: } \quad (\text { tank   (level,   x) }), (\text { program   (complete,   no) }), (\text { input   (amount,   y) })
$$

$$
\text { Modify } (\text { input } (\text { amount }, x + 7 0), \text { Modify } (\text { program } (\text { complete }, \text { yes }))
$$

along with monitor M3 as in 2a characterizes the anomaly. In this case, the input:amount value is as expected.Ž . However, the expected relationship between input:amount and tank:level is no longer valid.

Ž .c AE cover-up. A monitor covers the effect of an AE. The depiction of this anomaly is best seen in Fig. 2, because the monitor changes the value of the tank:level attribute after the same attribute has already been assigned a value in the rule.

## 4.2. Detection algorithm

We present an algorithm for the detection of the anomalies specified in Section 4.1. The algorithm first parses the rules and monitors to uncover the information required for the analysis. An intermediate representation for rules and monitors is produced. The result of joining the monitor and rule representations is then matched against templates of anomalies described in the previous section to determine if such anomalies exist in the KBS. To acquaint the reader with the procedure to detect monitor-rule interactions, we present the algorithm using the interaction between rule, R8, and monitor, M1, as an example. We repeat R8 and M1. Recall that M1 is attached to the attribute program:complete.

R8: tank level <sub>Ž</sub> <sub>.</sub> Ž . Ž Ž . x , program complete no

$$
\text { Modify } \left(\text { tank } \left(\text { level } x + 5 0\right)\right), \text { Modify } \left(\text { program } \left(\text { complete   yes }\right)\right)
$$

MI: IF tank:levelŽ .<sup>)</sup>100 THEN tank:level:<sup>s</sup>100

The steps involved in this process are as follows:

<sup>Ø</sup> Map monitors and rules to an intermediate representation.

<sup>Ø</sup> Create rule trees.

<sup>Ø</sup> Get new rule.

<sup>Ø</sup> Match new rule with anomaly template.

<sup>Ø</sup> Alert the user to the possible existence of anomalies.

## 4.2.1. Map monitors and rules to an intermediate representation

Note that different languages will require specific translators to the same intermediate representation. The mapping is designed to emulate how the hybrid KBS evaluates the intertwining of rules and monitors. Monitors and rules are transformed separately. Both rely on the monitor type predicates, Access object,attribute ,Ž . B-C object,attribute , and A-C object,attribute , in the intermediate representation that indicate a determinationŽ . Ž . of whether the object attribute in question has that type of monitor attached.

4.2.1.1. Mapping monitors. We first show how monitors are transformed to the intermediate representation. Each monitor is converted to the following form.

$$
\text {   If   } <   \text {   monitor - type   } > (\text {   object,   attribute   }) \text {   Then   } <   \text {   monitor - statements   } >
$$

where monitor-type is the type of the monitor i.e., Access, B-C, or A-C attached to the indicatedŽ . object-attribute, and monitor-statements are derived from the condition checks and assignment statements in a monitor as discussed below. Input and output statements are ignored since they do not take part in interaction. In Section 5, we discuss other statements in the monitors that we ignore at this time that may cause additional anomalies that are not the subject of this paper.

The following predicates are used as part of the monitor statements in the intermediate representation. These predicates are called action predicates.

check list of ordered pairs of the form object,attribute : This predicate replaces a single condition check in aŽ Ž .. monitor. The list of object attributes following the check predicate represents all the attributes involved in the condition. For example, if the condition were that obj1:attr1<sup>s</sup>obj2:attr2, then the predicate would be check obj1,attr1 , obj2,attr2 .ŽŽ . Ž ..

changes OBJ, ATTR; list of order pairs of the form object, attribute . This predicate replaces an Ž Ž Ž ... assignment in the monitor to an object attribute represented by OBJ, ATTR. If the new value depends on the values of other object attributes, these appear in the list of order pairs in the changes predicate. If the list is empty, then the change does not depend on any other object attributes.

To create the monitor-statement in the intermediate representation, we use the following steps: 1 Map everyŽ . condition check to a check predicate. 2 Precede every check predicate with an Access object,attribute forŽ . Ž . every object,attribute pair involved in the check. This represents the possibility of an Access monitor attachedŽ . to that attribute. 3 Map every assignment to a changes predicate. 4 Precede every changes predicate with aŽ . Ž . B-C object, attribute for the attribute found in the LHS of the assignment i.e., the attribute being changed .Ž . Ž . This represents the possibility of a B-C monitor activating before the new value is set for that attribute. 5 ForŽ . every object, attribute on which an assignment depends i.e, any attribute found in the RHS of an assignment ,Ž . Ž . precede the changes predicate with Access object, attribute . This represents the possibility of an AccessŽ . monitor activating while the assignment is being made. 6 Succeed every changes predicate with anŽ . A-C object, attribute for the attribute found in the LHS of the assignment. This represents the possibility of anŽ . A-C monitor activating after the attribute has been changed.

Using the above information, monitor M1 is mapped to the following representation:

If A-C program.complete Ž .

Then Access tank, level , check tank, level Ž . Ž .

B-C tank, level , changes tank, level; , A-C tank, level Ž . Ž . Ž .<sub>Ž .</sub>

## 4.2.1.2. Mapping rules. Each rule is converted to the form

If intermediate representation of CEs Then intermediate representation of AEs ² : ² <sup>)</sup>

where the allow for the inclusion of the intermediate representation of monitor types and rule action ² : predicates defined below.

cond list of ordered pairs of the form object, attribute : This predicate replaces a single CE in a rule. TheŽ Ž .. list of object, attribute pairs following the Ž . cond predicate represents all the attributes involved in the CE. This is analogous to the check action predicate for a monitor.

modifies OBJ, ATTR; list of ordered pairs of the form object, attribute : This predicate replaces a Modify Ž Ž Ž ... AE in the rule to the object attribute OBJ, ATTR. If the new value depends on the values of other object attributes, these appear in the list of order pairs in the modifies predicate. If the list is empty, then the change does not depend on any other object attributes. This is analogous to the changes predicate for monitors.

There are no action predicates for the assertion or deletion of frame-based predicates which can create new WMEs as well as establish new object to object relationships. This absence is because they do not cause monitor firing. Similarly, we do not address the presence of negative CEs in the rule.

To form the intermediate representation of a rule, execute steps 1 - 6 presented for mapping monitors,Ž . Ž . substituting the cond predicate for the check predicate and the modifies predicate for the changes predicate. Performing this transformation, rule R8 is converted to the following format.

If Access tank, level , cond tank, level , Ž . Ž . <sub>Ž</sub> <sub>.</sub>

Access program, complete , cond program, complete Ž . Ž . <sub>Ž</sub> <sub>.</sub>

Then B-C tank, level ,Access tank, level , modifies tank, level ; tank, level , A-C tank, level , Ž . Ž . Ž . Ž . <sub>Ž</sub> <sub>.</sub> <sub>Ž</sub> <sub>.</sub>

B C program, complete , modifies program, complete ; , A-C program, complete Ž . Ž . Ž .<sub>Ž .</sub>

## 4.2.2. Create rule trees

The intermediate representations of the monitors and rules are used to create rule trees. Each rule has independent two trees that are created: one for the rule’s If portion and one for the rule’s Then portion. The If and Then pieces of the rule are separated due to how the monitors interfere with the condition and actions parts of the rule, i.e., the intermediate representation is more complicated for the Then portion than it is for the If portion. The monitor attachment and subsequent execution becomes embedded in the rule execution within the intermediate representation. Thus, the trees are designed so that a postorder traversal of them will produce the correct sequence of all commands that the KBS executes. For each rule, trees are created in the following manner.

For the If portion of the intermediate rule representation: 1 Create a root node called If. 2 In the order thatŽ . Ž . they are listed, make each of the monitor types and action predicates in the If portion a child of the root. 3 ForŽ . each child: a If it is an action predicate, then do not expand this node. b If it is a monitor type, then i if noŽ . Ž . Ž . such monitor exists, do not expand this node. ii If such a monitor exists, create nodes for each of the monitorŽ . statements from the Then portion of the intermediate monitor representation and, in the order that they appear, make them children of the monitor node. Repeat step 3 for each of the newly created children until all nodesŽ . have been examined.

For the Then portion of the intermediate rule representation: 1 Create a root node called Then. 2 PerformŽ . Ž . steps 2 and 3 above, using predicates from the Then part of the representation instead of the If part in step Ž . Ž . Ž . 2 .

Using rule R8 and monitor M1, this step produces the rule tree in Fig. 5 with the action predicates in bold font.

## 4.2.3. Get new rule

This step creates a new rule in which we will detect the possible presence of an interaction anomaly. We perform post-order traversal on the rule trees, retaining only the action predicates shown in bold font in Fig. 5. This traversal retrieves the actions of the KBS in the order of occurrence, according to the immediate mode execution model for monitors. We place the action predicates from the If tree in the LHS of the new rule and the actions from the Then tree in the RHS of the new rule. Returning to our example, performing post-order traversal on the rule trees from Fig. 5 gives the following new rule:

cond tank, level , cond program, complete <sub>Ž</sub> <sub>. Ž</sub> <sub>.</sub>Ž . Ž .

modifies tank, level ; tank, level , modifies program, complete; , <sub>Ž .Ž . Ž .</sub>Ž . Ž .

check tank, level , changes tank, level; <sub>Ž</sub> <sub>. Ž</sub> <sub>.</sub> Ž . Ž .

![](/api/attachments/8QQWUX3T/fulltext/images/3cd012ea30874f057a2d9d4d9d87db57ee2d88e7ef3f5e804b02b5eb108cec51.jpg)  
Fig. 5.

## 4.2.4. Match new rules with anomaly templates

The anomaly templates described below are detailed representations of the anomalies defined in Section 4.1. Each of the new rules is matched against these templates. A successful match indicates a possible anomaly.

Ž . 1a Inaccurate inhibition or incitation of rule firing: For any object attribute x mentioned in the LHS of the new rule, changes x; . . . precedes cond list and x is an element of list.Ž Ž .. Ž .

Ž . 1b Rule firing with a different WM than initially matched: For any object attribute x mentioned in the LHS of the new rule, cond list precedes changes x; . . . and x is an element of list.Ž . Ž Ž ..

Ž . 2a Monitor change before rule modification: For any object attributes x and y mentioned in either part of the rule, changes x, . . . precedes modifies y, list and x is a member of list. Ž Ž .. Ž Ž ..

Ž . 2b Rule modification before monitor change: For any object attributes x and y mentioned in either part of the rule, modifies y, list precedes changes x, . . . , x is a member of list.Ž Ž .. Ž Ž ..

Ž . 2c AE cover-up: For any object attribute x in the RHS of the new rule, modifies x, list precedesŽ Ž .. changes x, . . . .Ž Ž ..

In our example, the only anomaly that matches is 2c . Ž .

## 4.2.5. Alert the user to the possible existence of anomalies End algorithm.

## 4.3. Discussion

The detection algorithm described in Section 4.2 analyzes the rules and monitors for possible interactions. It uses an internal representation that embeds monitor actions inside rule conditions and actions to determine the execution of rules with monitors attached to them, thus uncovering any possible anomalies from interactions. Work is underway to automate the algorithm and to blend with the automated verification tool discussed in Section 3.6.

There are currently some limitations on the hybrid KBS for it to be suitable for analysis by the algorithm. First, we do not consider KBSs with looping structures in the monitors. The static nature of our analysis makes it impossible to fully analyze looping or branching statements that depend on values determined at run-time. Second, we assume that all rules and monitors in the KBS do not contain function calls or go to statements. Third, we dissallow the initiation of rule-based inference from a monitor. Finally, we require that the KBS be free of monitor–monitor interaction anomalies prior to detection. For example, if two monitors are involved in circular execution, the tree created by the algorithm would result in infinitely expanding nodes that contain attributes and monitors participating in the circularity. Research is currently being performed to define and detect monitor–monitor interactions 3 .<sup>w</sup> <sup>x</sup>

## 5. Conclusion

Hybrid KBSs provide a convenient platform for developing rule-based systems. Object-oriented features help in developing an efficient representation and usage of domain information. Rule-based features are used for encoding human expert knowledge. However, interactions among these two powerful concepts can lead to possible anomalies in the resulting implementation. These anomalies are not apparent by looking only at the rule base. Thus, novel methods for their detection are required.

Anomalies in hybrid KBSs arise due to the nature of its components and the interactions among them. In this research, we examine the interactions among the object-oriented and the rule-based components of hybrid KBSs. Anomalies from these interactions manifest themselves in two ways: by the effect of class hierarchy and inheritance on rule chaining and by the effect of monitors on rule execution. Possible cases of such anomalies are identified in this paper. Since the rule base is separate from these other components, i.e., the class hierarchy and the monitors, the resulting anomalies are not apparent by looking at the rule base. Specialized techniques for their detection are developed that use the rule base along with the required information. Class hierarchy and objects were used to determine subsumption among rules. A previous method for detection of subsumption anomalies 10 is extended to better handle all cases. Additionally, monitors in the system are analyzed to detect<sup>w</sup> <sup>x</sup> rule-monitor interaction anomalies. An algorithm developed for this purpose looks at the execution sequence of a rule along with that of the monitors attached to it. Possible interactions due to monitors can thus be detected. An automated tool for the analysis of such anomalies is being developed.

Presence of the anomalies mentioned above can lead to errors in the KBS. In other cases, it leads to inefficient performance or maintenance problems. The development of efficient and reliable hybrid KBSs requires specialized verification procedures that are different from traditional rule-based systems. The anomalies identified in this paper and their detection mechanism provide a starting point for such verification. Other areas like monitor circularity, monitor redundancy, etc., need to be investigated to cover all possible areas of verification of hybrid systems.

## References

<sup>w</sup> <sup>x</sup> 1 R. Agarwal, M. Tanniru, A Petrie-net based approach for verifying the integrity of production systems, Int. J. Man-Machine Studies 36 Ž .1992 447–468.

<sup>w</sup> <sup>x</sup> 2 A.T. Bahill, M. Jufar, R.F. Moller, Tools for extracting knowledge and validating expert systems, IEEE Trans. Systems, Man, Cybernetics 18 2 1987 857–862.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 D.M. Baughman, R.F. Gamble. Monitor anomalies in hybrid KBSs. Technical Report UTULSA-MCS-95-2, Department of Mathematical and Computer Sciences, University of Tulsa, March 1995.

<sup>w</sup> <sup>x</sup> 4 C.L. Chang, J.B. Combs, R.A. Stachowitz, A report on the expert system validation associate EVA , Expert Systems with Ž . Applications 1 1990 217–230. Ž .

<sup>w</sup> <sup>x</sup> 5 B.J. Cragun, H.J. Steudel, A decision table-based processor for checking completeness and consistency in rule-based expert systems, Int. J. Man-Machine Studies 26 1987 633–648.Ž .

<sup>w</sup> <sup>x</sup> 6 R.F. Gamble, D.M. Baughman, A methodology to incorporate formal methods in hybrid KBS development, Int. J. Human–Machine Studies 44 1996 213–244.Ž .

7 R.F. Gamble, G.-C. Roman, W.E. Ball, H.C. Cunningham, Applying formal verification techniques to rule-based programs, Int. J. Expert Systems 7 3 1994 203–238.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 A. Ginsberg, A new approach to checking knowledge bases for inconsistency and redundancy, in: 7th National Conference on Artificia Intelligence, 1988, pp. 585–589.

<sup>w</sup> <sup>x</sup> 9 Y. Kang, A.T. Bahill, A tool for detecting expert system errors, AI Expert, February 1990, pp. 42–51.

<sup>w</sup> <sup>x</sup> 10 S. Lee, R.M. O’Keefe, Subsumption anomalies in hybrid knowledge based systems, Int. J. Expert Systems 6 3 1993 299–320. Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 N.K. Liu, T. Dillon, An approach towards the verification of expert systems using numerical Petrie nets, Int. J. Intelligent Systems 7 Ž .1991 255–276.

<sup>w</sup> <sup>x</sup> 12 S. Loiseau, M.-C. Rousset, Formal verification of knowledge bases focused on consistency: Two experiments based on ATMS techniques, Int. J. Expert Systems 6 3 1993 273–298.Ž . Ž .

<sup>w</sup> <sup>x</sup>13 M. Mehrotra, Rule groupings: A software engineering approach towards verification of expert systems, Technical report, NASA Contractor Report 4372, Washington, DC, 1991.

<sup>w</sup> <sup>x</sup> 14 P. Meseguer, Verification of multi-level rule-based expert systems, in: 9th National Conference on Artificial Intelligence AAAI-91 ,Ž . 1991, pp. 323–328.

<sup>w</sup> <sup>x</sup> 15 T.A. Nguyen, Verifying consistency of production systems, in: IEEE Conference on AI Applications, 1987, pp. 4–8.

<sup>w</sup> <sup>x</sup> 16 R.M. O’Keefe, D.E. O’Leary, Expert system verification and validation: A survey and tutorial, AI Rev. 7 1993 3–42. Ž .

<sup>w</sup> <sup>x</sup> 17 D.E. O’Leary, Verification of frame and semantic network knowledge bases, in: AAAI-89 Workshop on Knowledge Acquisition for KBSs, 1989.

<sup>w</sup> <sup>x</sup> 18 A.V. Pai, Verifying the rule processing component of active databases, MS thesis, University of Tulsa, Department of Mathematical and Computer Sciences, September 1995.

19 G.R. Prakash, H.N. Mahabala, SVEPOA: A tool to aid verification and validation of OPS5-based Al applications, Int. J. Expert Systems 6 2 1993 193–236.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 A. Preece, Towards a methodology for evaluating expert systems, Expert Systems 7 4 1990 215–223. Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 A.D. Preece, A new approach to detecting missing knowledge in expert system rule bases, Int. J. Human–Machine Studies 38 1993 Ž . 661–688.

<sup>w</sup> <sup>x</sup> 22 A.D. Preece, R. Shinghal, A. Batarekh, Verifying expert systems: A logical framework and a practical tool, Expert Systems with Applications 5 1992 421–436.Ž .

<sup>w</sup> <sup>x</sup> 23 G.-C. Roman, R.F. Gamble, W.E. Ball, Formal derivation of rule-based programs, IEEE Trans. Software Eng. 19 3 1993 277–296. Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 M.-C. Rousset, On the consistency of knowledge bases: The COVADIS system, in: ECAI-88, 1988, pp. 79–94.

<sup>w</sup> <sup>x</sup> 25 J. Rushby, R.A. Whitehurst, Formal verification of AI software, Technical report, SRI International, Computer Science Laboratory, February 1989.

<sup>w</sup> <sup>x</sup> 26 T.M. Shaft, R.F. Gamble, Knowledge <sup>q</sup> based system reliability: A theoretical basis for assessment and a survey of techniques, Tech. Rep. UTULSA-MCS-93-3, Dept. of Mathematical and Comp. Sciences, Univ. of Tulsa, 1993.

<sup>w</sup> <sup>x</sup> 27 R. Stachowitz, J. Combs, Completeness checking of expert systems, Technical Report A-60, Lockheed Missiles and Space, 1990.

<sup>w</sup> <sup>x</sup> 28 R.A. Stachowitz, J.B. Combs, Validation of expert systems, in: 20th Hawaii International on Systems Sciences, January 1987, pp. 689–695.

<sup>w</sup> <sup>x</sup>29 G. Valiente, Verification of knowledge base redundancy and subsumption using graph transformations, Int. J. Expert Systems 6 3Ž . Ž .1993 341–355.

<sup>w</sup> <sup>x</sup>30 A. Vermesan, Specification refinement of object-oriented KBSs, in: IJCAI-95 Workshop on Verification and Validation of KBSs, August 1995.

<sup>w</sup> <sup>x</sup> 31 R.J. Waldinger, M.E. Stickel, Proving properties of rule-based systems, Int. J. Software Eng. Knowledge Eng. 2 1 1992 121–144. Ž . Ž .

<sup>w</sup> <sup>x</sup> 32 N. Zlatareva, CTMS: A general framework for plausible reasoning, Int. J. Expert Systems, 1992, In press.

Ranadeep Mukherjee is a software engineer at Schlumberger Geoquest in Houston, TX. He received a M.S. degree in computer science at the University of Tulsa and a B.S. degree in computer engineering from Regional Engineering College, India. His interests include user interfaces, database, and expert systems.

Jennifer Parkinson is a graduate student in mathematics at the University of Kansas, where she received a B.S. also in mathematics. Ms. Parkinson was a summer undergraduate research assistant at the University of Tulsa as part of the CRA Distributed Mentoring Program.
