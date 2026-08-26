---
otero_id: 17731
otero_key: "GNWE85YY"
title: "An interactive-graphic environment for automatic generation of decision trees"
authors: "Tanguy Kervahut; Jean-Yves Potvin"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00030-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An interactive-graphic environment for automatic generation of decision trees

Tanguy Kervahut $^{a}$ , Jean-Yves Potvin $^{a,b,*}$

$^{a}$ Département d'informatique et de recherche opérationnelle, Université de Montréal, C.P. 6128, Succ. Centre-ville, Montréal, Qué., Canada H3C 3J7

$^{b}$ Centre de recherche sur les transports, Université de Montréal, C.P. 6128, Succ. Centre-ville, Montréal, Qué., Canada H3C 3J7

## Abstract

In this paper, a computerized assistant for the construction of decision trees is described. With this system, designers of automatic tree building algorithms can quickly and easily evaluate new algorithmic designs for solving specific decision problems. A generic algorithmic template, which is initialized by the designer of algorithms with his(her) own formulas, is the basic mechanism for creating new tree building algorithms. These algorithms can then be tested on different decision problems, using the interactive-graphic environment provided by the system.

Keywords: Decision trees; Inductive learning; Algorithmic design; interactive-graphic environment

## 1. Introduction

This paper describes a computerized assistant for the design of algorithms that automatically construct decision trees. These algorithms are members of a class of inductive techniques that learn classification procedures through examples [1]. Other well-known members of this class are neural network models [10,12] and genetic classifiers [3].

The system presented in this paper is based on a generic algorithmic template which is initialized by the designer of algorithms with his(her) own formulas, in order to obtain algorithmic behaviors that are fit to specific decision problems. The generic template unifies a large class of algorithms for generating decision trees, and greatly facilitates the design of new algorithms, as well as improvements or modifications to known algorithms. The template is embedded within an interactive-graphic environment aimed at facilitating the testing of new algorithms and the analysis of their behavior on different decision problems. In fact, the whole system can be viewed as a workbench for quickly exploring and refining new algorithmic ideas. Once a good algorithm is identified for the problems at hand, the final task of writing specialized (and fast) code can be done with the assurance that the underlying algorithm is a good one.

The paper is organized as follows. First, the contribution of the system for computer-aided decision making is underlined. Then, the classical ID3 algorithm [6], as well as a useful generalization [2], are briefly described. In Sections 4 and 5, the generic algorithmic template is introduced, as well as the interactive-graphic environment provided to the designer of algorithms. Finally, illustrative decision problems are presented to underline the benefits of this system.

## 2. Contribution of this work

Since the introduction of the Decision Support System (DSS) concept, many successes have been reported in the literature $[4,15–17]$ . However, a DSS is often designed with a specific application in mind, and many different types of systems have been implemented thus far. In particular, some DSSs stand as “traditional” support tools while others now take a more active part in the decision making process. For example, intelligent symbiotic and adaptive DSSs are currently the focus of intense research $[5,13]$ . These systems support decision making by making inferences, by selecting appropriate heuristics, rules or models, and by suggesting possible solutions to a problem. These capabilities are implemented through machine learning methods that are either supervised or unsupervised. Supervised learning strategies require the implication of an external agent during the learning process (e.g., to provide a target solution to the system). Among these methods, we find rote learning, instructional learning, and deductive learning. Conversely, unsupervised learning techniques can generate useful knowledge without benefiting from an external agent. Among the inductive techniques in this class, we find the algorithms for automatically generating decision trees from a set of decision examples.

In the broad spectrum of decision aids, the contribution of our system is two-fold. First, the system is intended to designers of algorithms (and not to end users). Hence, designers of algorithms are viewed as decision makers, because they must choose appropriate procedural components in order to solve a particular problem or class of problems. Since the current system supports the design of algorithms for automatically generating decision trees, this tool could be very useful for constructing intelligent DSSs. That is, a good tree-building algorithm for a particular class of decision problems could be designed with our system, and later incorporated within an intelligent DSS.

Second, the system is based on a model, known as the generic algorithmic template, which unifies and generalizes different methods for automatically generating decision trees. Through the initialization of the algorithmic template, a specific algorithm can be produced for a given problem or class of problems. Accordingly, there is no “built-in” algorithm within the system, but rather a broad spectrum of known (and yet unknown) tree-building algorithms. This approach is quite different from the traditional “black-box” approach, where the underlying problem-solving strategy is fixed once for all, so that only minor changes are allowed (e.g., modifications to parameter values). Although many good induction packages are now available on the market, like Ex-Tran, RuleMaster and C4.5, these packages are instances of the traditional “black-box” approach, because the basic algorithms cannot be interactively modified by the user.

Finally, it is worth noting that our system is really a support tool that does not provide any active aid to the user. That is, algorithms produced with this system are as good as the designer of algorithms who creates them, given the limitations of the generic algorithmic template.

## 3. Tree construction algorithms

In this section, a classical algorithm for generating decision trees is first presented. Then, a generalization of this algorithm is introduced. Finally, a means to process continuous attributes is discussed.

## 3.1. The ID3 algorithm [6]

ID3 is a well known procedure for inducing classification trees from examples. Each example, with a known classification, is described via a set of attribute values. Fig. 1 shows a typical set of examples. Here, each example is a member of class $c_{1}$ , $c_{2}$ or $c_{3}$ , and is described with two discrete attributes, namely $a_{1}$ with values $v_{11}$ , $v_{12}$ , $v_{13}$ , and $a_{2}$ with values $v_{21}$ , $v_{22}$ , $v_{23}$ .

<table><tr><td>Example</td><td> $a_1$ </td><td> $a_2$ </td><td>Class</td></tr><tr><td> $e_1$ </td><td> $v_{11}$ </td><td> $v_{21}$ </td><td> $c_1$ </td></tr><tr><td> $e_2$ </td><td> $v_{11}$ </td><td> $v_{22}$ </td><td> $c_2$ </td></tr><tr><td> $c_3$ </td><td> $v_{12}$ </td><td> $v_{22}$ </td><td> $c_2$ </td></tr><tr><td> $c_4$ </td><td> $v_{12}$ </td><td> $v_{23}$ </td><td> $c_1$ </td></tr><tr><td> $c_5$ </td><td> $v_{13}$ </td><td> $v_{21}$ </td><td> $c_3$ </td></tr><tr><td> $e_6$ </td><td> $v_{13}$ </td><td> $v_{22}$ </td><td> $c_3$ </td></tr></table>

Fig. 1. A set of examples for generating a decision tree.

ID3 uses a set of examples, like the one shown in Fig. 1, to generate a decision tree. The nodes of the decision tree are associated with different subsets of examples. During the tree-building procedure, the initial set of examples is recursively partitioned into smaller subsets of examples. An evaluation function, usually derived from an entropy or uncertainty measure, is applied to the subsets of examples to assess their “quality”. This function returns low entropy values for subsets of high homogeneity, that is, subsets whose examples are mostly members of the same class. In particular, a subset whose examples are all members of the same class has a null entropy (i.e., no uncertainty).

Starting with the root as the current node (which is associated with the whole set of examples), the ID3 algorithm can be described as follows.

(1) For each attribute not yet selected at the current node do the following: Evaluate the entropy of each subset of examples produced by splitting the set of examples at the current node along all possible attribute values. Then, combine these entropy values into a global entropy value.

(2) Select the attribute that minimizes the global entropy, and apply this attribute to create the children of the current node. A child node is created for each value of the selected attribute, and contains the subset of examples that share the same value.

(3) Recursively apply this procedure to the children of the current node. The procedure stops at a given node, when the node is homogeneous, or when all attributes have been used along the path to this node.

This procedure will now be applied to the set of examples of Fig. 1, using the following entropy formula:

$$
E (S) = - \sum_ {C _ {k} \in C} P _ {S, C _ {k}} \log_ {2} P _ {S, C _ {k}},
$$

where S = the set of examples at the current node; C = the set of classes (or categories); $P_{S,Ck}$ = the proportion of examples in set $S$ belonging to class $C_k$ .

In order to evaluate the entropy of attribute $a_{i}$ , the set of examples S is partitioned into subsets $S_{ij}$ . Each subset $S_{ij}$ contains the examples in S that share the same value $v_{ij}$ for attribute $a_{i}$ . Then, the entropy values of the subsets $S_{ij}$ are combined to provide a single global value associated with attribute $a_{i}$ , namely:

$$
\begin{array}{l} E (a _ {i}, S) = \sum_ {v _ {i j} \in \operatorname{domain} (a _ {i})} \left(\frac {| S _ {i j} |}{| S |}\right) \times E (S _ {i j}), \\ \text { for   each   attribute } a _ {i}, \end{array}
$$

where $|S|$ is the cardinality of set $S$ .

The selected attribute minimizes $E(a_{i},S)$ . Using the set of examples of Fig. 1, the following results are obtained at the root node.

$$
\begin{array}{r l} S & = \left\{e _ {1}, e _ {2}, e _ {3}, e _ {4}, e _ {5}, e _ {6} \right\} \\ C & = \left\{c _ {1}, c _ {2}, c _ {3} \right\} \\ A & = \left\{a _ {1}, a _ {2} \right\} \\ E (a _ {1}, S) & = \frac {2}{6} \times E (S _ {1 1}) + \frac {2}{6} \times E (S _ {1 2}) \\ & + \frac {2}{6} \times E (S _ {1 3}) \\ & = \frac {2}{6} \times (- (0. 5 \log_ {2} 0. 5) - (0. 5 \log_ {2} 0. 5) \\ & - (0. 0 \log_ {2} 0. 0)) \\ & + \frac {2}{6} \times (- (0. 5 \log_ {2} 0. 5) \\ & - (0. 5 \log_ {2} 0. 5) - (0. 0 \log_ {2} 0. 0)) \\ & + \frac {2}{6} \times (- (0. 0 \log_ {2} 0. 0) \\ & - (0. 0 \log_ {2} 0. 0) \\ & - (1. 0 \log_ {2} 1. 0)) = 0. 6 6 6 6 \\ E (a _ {2}, S) & = \frac {2}{6} \times E (S _ {2 1}) + \frac {3}{6} \times E (S _ {2 2}) \\ & + \frac {1}{6} \times E (S _ {2 3}) = 0. 7 9 2 5 \end{array}
$$

Hence, attribute $a_{1}$ is selected and the children of the root are created accordingly. As shown in Fig. 2, one child is homogeneous (for $a_{1}=v_{11}$ ) and no more processing is needed. The two other children are not homogeneous, and the procedure is recursively applied to each one of them, using the remaining attribute $a_{2}$ . At the end, the full decision tree of Fig. 2 is created.

![](/api/attachments/GNWE85YY/fulltext/images/5b5c1a83f56ced998c6dcd2f887129dc99f9b69ddf9c12f2a55ae3d76f04d330.jpg)  
Fig. 2. Decision tree produced by ID3.

This tree encodes the following decision rules: if $a_1 = v_{11}$ then $c_3$ if $(a_1 = v_{12} \text{ and } a_2 = v_{22})$ or $(a_1 = v_{13} \text{ and } a_2 = v_{22})$ then $c_2$ if $(a_1 = v_{12} \text{ and } a_2 = v_{23})$ or $(a_1 = v_{13} \text{ and } a_2 = v_{21})$ then $c_1$

This algorithm is very sensitive to the entropy formula. In this example, selecting attribute $a_{2}$ before $a_{1}$ would create a different tree. Consequently, it is possible to generate many different decision trees by modifying the entropy formula.

The quality of a decision tree is based on both its accuracy and complexity. The accuracy is assessed by providing new examples with known classes, and by comparing these classes with the classes predicted by the tree. The complexity is related to the shape and size of the tree. Obviously, for the same accuracy, simple trees are preferred over complex ones.

One major weakness of ID3 is that a node is created for each value of a given attribute. In some cases, an attribute can get a good global evaluation, even if its entropy is good only for a few values among all its possible values (recall that the entropy of an attribute is a weighted sum over all values). Consequently, only the nodes associated with meaningful values should be generated. A modification along these lines is proposed in [2]. This is the topic of the next section.

## 3.2. A generalized ID3

In [2], the authors use “phantom attributes”, derived from the original attributes, to generate decision trees. To this end, they introduce a tolerance level parameter (TL), with a value between 1 and infinity, to identify meaningful attribute values. The algorithm works in the same way as ID3, but the selection of an attribute now requires two steps.

(a) Creating the phantom attributes.

For each attribute not yet selected at the current node, the entropy associated with each attribute value is computed. The minimal entropy value, thereafter called Entropymin, is recorded.

Using this minimal value, the following computation is performed for each attribute $a_{i}$ .

for each value $v_{ij}$ of attribute $a_{i}$ ,

if $\text{entropy}(S_{ij}) \leq \text{Entropymin} \times \text{TL}$ , then value $v_{ij}$ is added to the list of meaningful values of attribute $a_i$

otherwise, value $v_{ij}$ is added to the list of default values of attribute $a_{i}$ (meaningless values)

Then, a phantom attribute $a_i'$ is created. This attribute has one value for each meaningful value of $a_i$ , and a single default value associated to the meaningless values of $a_i$ .

(b) Selecting a phantom attribute.

The entropy formula is applied again on the phantom attributes $a_{i}^{\prime}$ . The phantom attribute with minimum entropy is selected to expand the tree.

It is worth noting that this algorithm can be seen as a generalization of the ID3 algorithm. If the tolerance level TL is set to a large value, all attribute values qualify as meaningful values, and the phantom attributes $a_{i}^{\prime}$ are the same as the original attributes $a_{i}$ . Consequently, the algorithm will behave as the ID3 algorithm. However, different types of behaviors are obtained by modifying the tolerance level.

## 3.3. Continuous attributes

The above algorithm can be further extended by allowing attributes with a continuous domain of values, as in C4 (which is based on ID3 [8,9]). Here, the domain of values is partitioned into non-overlapping intervals. A boundary between two intervals is selected in order to split the set of examples into two different subsets: one subset contains the examples with a value smaller than or equal to the boundary, and the other subset contains the remaining examples. All the boundaries are evaluated in turn, using the entropy function, in order to find the best boundary.

For instance, if the weight of an object is considered in a decision problem, many different intervals of fixed length are created, ranging from 0 to some maximal weight. If the length of each interval and the maximal weight are set to 10 and 50, respectively, the following intervals are created: [0,10], [10,20], [20,30], [30,40], and [40,50]. Consequently, boundaries 10, 20, 30, or 40 can be used to split the current set of examples into two different subsets. Assuming that the best boundary is 10, the current set of examples would be divided into two subsets: one subset would include all examples with a weight value in the interval [0,10], and the other subset would include the remaining examples, with a weight value in the interval [10,50]. It is worth noting that the subset associated with [10,50] can be considered later for further splitting, since boundaries 20, 30 and 40 are still available. Conceptually, four new attributes $weight_{10}$ , $weight_{20}$ , $weight_{30}$ , and $weight_{40}$ are created from the single attribute weight.

The algorithmic framework of the next section is based on Cheng's algorithm, and includes the processing of continuous attributes. However, it extends Cheng's algorithm by allowing the introduction of user-defined formulas.

## 4. The generic algorithmic template

The generic algorithmic template provides a flexible framework for designing and testing new tree building algorithms. The template is based on Cheng's algorithm, and includes various "slots" to be filled by the designer of algorithms in order to create new algorithms. In the following, the algorithmic template is described. Then, various functions available to the user are defined.

## 4.1. The algorithmic template

For the sake of simplicity, the algorithm presented in this section is restricted to discrete attributes only. The full description, for both discrete and continuous attributes, may be found in Appendix 1 at the end of the paper. Note also that the functions and parameters in italic in the pseudo-code description must be defined by the designer of algorithms.

## Notation

$S =$ initial set of examples

$A_{\mathrm{d}} =$ set of discrete attributes

$v_{ij}$ = jth value of discrete attribute $a_{i}$

$S_{ij} =$ subset of examples with value $\nu_{ij}$ for discrete attribute $a_i$

Generic algorithmic template

Main procedure (S)

Create the root
Assign the whole set of examples S to the root
Call Tree Expansion Procedure(root, $A_{d}$ )

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Tree expansion procedure (node, $A_d$)
Step 1. Check the stopping conditions
    If Stopping predicate is True or the default stopping condition applies to the set of examples in node then
    classify the node with Classification function and Exit
Step 2. Initialize the variables
    Entropymin $\leftarrow$ arbitrary large number
Step 3. Compute the minimum entropy
    For each attribute $a_i$ in $A_d$ do
    For each value $v_{ij}$ of attribute $a_i$ do
    evaluate Entropy($S_{ij}$) with Evaluation Function
    if Entropy($S_{ij}$) &lt; Entropymin then
    set Entropymin to Entropy($S_{ij}$)
Step 4. Create the phantom attributes
    For each attribute $a_i$ in $A_d$ do
    For each value $v_{ij}$ of attribute $a_i$ do
    if Entropy($S_{ij}$) $\leq$ Entropymin $\times$ TL then
    put $v_{ij}$ in the list $L_{i1}$ of individual values of the phantom attribute $a_i'$
    otherwise,
    put $v_{ij}$ in the list $L_{i2}$ of default values of the phantom attribute $a_i'$
</div>

Step 5. Validate the phantom attributes
Remove any phantom attribute with no meaningful values (i.e., no values in the list $L_{il}$ )

Step 6. Select a phantom attribute
Select the best phantom attribute $a_s$ ' with Selection Function

Step 7. Expand the current node
For each value $v_{sj}$ in the list $L_{s1}$ do
    create a child node
    assign the subset of examples $S_{sj}$ to the child node
Create a child node for the list of default values $L_{s2}$ , and assign the remaining examples to this node.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 8. Update the status of the selected attribute
If $L_{s2}$ contains a single attribute value then
remove $a_s$ from $A_d$
otherwise
set the list of values of $a_s$ to $L_{s2}$
Step 9. Recursion
For each child node do
call Tree Expansion Procedure(child node, $A_d$)
</div>

## 4.2. User-defined functions and parameters

Within the above template, the designer can specify the following functions and parameters:

(a) Evaluation function. This function evaluates the sets of examples, and is called in the first phase of the attribute selection process, when the phantom attributes are created. This function can also be called by the user within his(her) Selection Function, when a phantom attribute is selected (see below).

The Evaluation function has one parameter: the set of examples to be evaluated. The output of the function is a numerical value, namely the evaluation or entropy of the set.

(b) Selection function. This function selects a phantom attribute to further expand the tree. Typically, the Selection function calls the Evaluation function, as defined in point (a).

The Selection function has two parameters: the set of examples and the list of phantom attributes available at the current node. It returns the best phantom attribute in the list.

(c) Stopping Predicate. This function is used to stop the expansion process at the current node. The conditions expressed in the predicate are added to the default stopping condition, which is to stop when the node is homogeneous or when all available attributes have been used. Consequently, if the stopping predicate is set to NIL, only the default stopping condition applies.

This predicate has a single parameter, the set of examples in the current node, and returns either T (True) or NIL (False).

(d) Classification Function. This function puts a class label on a terminal node or leaf of the tree. The default behavior, which is applied when the function is set to NIL, is the following: if there is only one class in the node (i.e. homogeneous node), it returns this class, otherwise it returns NIL. Quite often, the classification function is based on the majority rule, and the selected class is the one with the largest number of examples in the node.

The Classification function has a single parameter, the set of examples in the leaf, and it returns a class.

(e) Tolerance Level (TL). This parameter is the threshold for identifying meaningful attribute values (see Section 3). It is set to a numerical value between 1 and infinity. If TL is set to NIL, it means infinity.

In order to create a specific tree building algorithm, only the above functions or parameter values need to be defined by the user. In the following sections, we show how classical tree building algorithms can be specified within the generic algorithmic template. To this end, some useful built-in functions for creating tree building algorithms are first introduced.

## 5. Initialization of the generic template

To facilitate the definition of new functions within the algorithmic template, a set of built-in primitives are available. These primitives can be used as building blocks in the construction of new function definitions, and are defined on top of the Common Lisp language [18]. Accordingly, the user of the system can avoid the primitives if he(she) wants so as to use the full power of the Common Lisp language.

The Common Lisp language was chosen for two main reasons. First, the availability of the Medley programming environment greatly facilitates the design of user-friendly interfaces. Second, and more importantly, the Common Lisp language can be interpreted (rather than compiled). Given that our system relies on the dynamic creation, modification and application of different algorithmic components, it is very important to avoid the compilation of the whole template after each modification. The Common Lisp language provides this flexibility.

The built-in primitives provided by the system can be divided into two classes, Access Functions and Utility Functions. They are briefly described below.

## 5.1. Access functions

Each entity within the system is implemented as an individual object, with its own set of characteristics. The main classes of objects are Attributes, Examples, and Nodes (of the decision tree). The access functions allow the user to get the value associated with any given characteristic of an object. There is a rich library of such functions in the system. We only give below a few examples. These functions are used in Section 5.3 and in Appendix 2.

P.PH-VALUES (phantom attribute)

Return the list of values of phantom attribute (if it is a discrete attribute)

P.PH-TYPE (phantom attribute).

Return DISCRETE or CONTINUOUS

P.CHILDREN (node).

Return the list of children of node.

P.NB-EX (node)

Return the number of examples in node P.EX (node).

Return the list of examples in node

## 5.2. Utility functions

These functions are useful to build decision trees, and are provided as primitives. We give below a few examples.

P.CLASSES ().

Return the list of classes or categories of the current decision problem

P.NBEX-CLASS (set, class)

Return the number of examples in set with the specified class.

P.PH-SPLIT (set, phantom attribute).

Return the list of subsets of examples created by splitting the set of examples, using the values of phantom attribute.

P.SUBSET (set, attribute, values)

Return the subset of examples in set with an attribute value in the list of values.

P. ENTROPY (set).

Returns the entropy of the set of examples, using the ID3 formula.

## 5.3. ID3

In the following, we illustrate the initialization of the generic template to create the ID3 algorithm. As mentioned before, four different functions, as well as the TL parameter value, must be defined.

Evaluation Function. Here, we assume that the function defined by the user for evaluating a set of examples according to the ID3 formula is called EVAL-ID3. The definition of this function in Common Lisp is given below.

(DEFUN EVAL-ID3 (SET)

(P.ENTROPY SET)

Hence, this function simply calls P.ENTROPY on SET. However, without the availability of P.ENTROPY as a built-in primitive, EVAL-ID3 could be implemented in the following way (with a lot of comments!).

(DEFUN EVAL-ID3 (SET)

/create local variables NBEX, CLASSES, SUM and RATIO. Initialize NBEX and CLASSES/

(LET ((NBEX (LENGTH SET))

(CLASSES (P.CLASSES))

SUM RATIO)

/set variable SUM to 0/

(SETQ SUM 0)

/iterate over the list of CLASSES with local variable C/

(DOLIST (C CLASSES)

/compute proportion of examples in class C/

(SETQ RATIO (/ (P.NBEX-CLASS SET C) NBEX))

/if there are examples in class C then compute the entropy formula for this class and add it to SUM/

(IF (> RATIO 0)

(SETQ SUM (+SUM (\*-1 RATIO (LOG RATIO 2))))))

/return SUM, the final entropy value / (RETURN-FROM EVAL-ID3 SUM)

Obviously, this function definition requires some knowledge of Common Lisp, but the use of built-in functions (with the prefix P.) greatly facilitates the user's task. Here, the local variables NBEX, CLASSES, SUM and RATIO are first declared. NBEX is set to the number of examples in the set, while CLASSES is set to the list of classes in the decision problem. Then, the entropy is computed and the final value is returned in the RETURN-FROM statement (the entropy being stored in the SUM variable).

Since intermixing English comments and Lisp code produces very long function definitions, we will restrict ourselves to English-like descriptions in the following. However, the Lisp code for each function can be found in Appendix 2 at the end of the paper.

Selection Function. In this example, the function defined by the user for selecting a phantom attribute is called SELECT-ID3. The definition of this user-defined function is given below.

SELECT-ID3 (SET of examples, PHANTOM-ATTRIBUTES)

initialize BESTVAL with an an arbitrary large number;

![](/api/attachments/GNWE85YY/fulltext/images/8235eb1ac43e0c38d7eb9df93b0e4d3b15644207c3458a6ea7a3c0f58d0ceb9b.jpg)  
Fig. 3. The main screen.

for each PHANTOM-ATTRIBUTE in PHANTOM-ATTRIBUTES do

set VAL to 0;

for each value of PHANTOM-ATTRIBUTE do:

identify the SUBSET of examples in SET with this attribute value;

$$
V A L \leftarrow V A L + \left(\frac {| S U B S E T |}{| S E T |} \times \right.
$$

$$
E V A L - F N (S U B S E T) \Bigg);
$$

if VAL is less than BESTVAL then

set BESTVAL to VAL;

set BESTATT to PHANTOM-ATTRIBUTE;

endor

return the best phantom attribute BESTATT.

In this definition, $|S|$ stands for the cardinality of set S and EVAL-FN refers to the name of the function stored in the Evaluation Function slot of the algorithmic template. Hence, the call to EVAL-FN with the argument SUBSET is equivalent to a call to EVAL-ID3 in this example.

Stopping Predicate. The user-defined Stopping Predicate is set to NIL (the default stopping criterion applies).

Classification Function. The user-defined Classification Function is called CLASS-MAJORITY, and implements the “majority rule”: the class selected is the one with the largest number of examples in the set.

CLASS-MAJORITY (SET of examples)

set NBEX-MAX to 0;

for each class C do

if the number of examples in class C within SET is greater than NBEX-MAX then

set CLASS-MAX to C;

set NBEX-MAX to the number of examples in class C;

endfor

return CLASS-MAX;

Tolerance Level. The tolerance level is set to NIL (i.e., infinity).

Using this initialization, the behavior of ID3 is obtained. Of course, many different behaviors can be produced by modifying the function definitions and the TL parameter value. In the last sections, we show how the system can be used to easily generate different trees.

## 6. An interactive-graphic environment

In order to be a valuable workbench for designing and testing tree building algorithms, our Lisp-based system was implemented within a rich interactive-graphic menu-driven environment. As mentioned before, the system exploits the Medley programming environment available on the Sun workstations. Fig. 3 shows a typical screen. The Promptwindow in the upper left corner shows warning messages to the user. The executive window just below, allows the user to interact with the Lisp interpreter. The large window in the upper right corner displays decision trees. Finally, the window just below displays various information about the decision trees.

The main menu under the Executive window contains the interactive commands. We now go through some of these commands in order to illustrate a typical working session with the system.

(a) LOAD SPECIFICATIONS. The first step is to load a specification file. This file identifies the various attributes, as well as their characteristics. For a continuous attribute, the characteristics are the domain's lower bound and upper bound, and the length of each interval within the domain. For a discrete attribute, it is the list of all possible values. The file also identifies the various classes or categories.

In Section 7, Fig. 6 shows the specification file CONTACT-LENSES.SPEC for the problem of deciding if a patient can wear contact lenses, and if he(she) can, what type of contact lenses is appropriate. There are four discrete attributes to describe a patient, and the three decision classes are: nothing (no contact lenses), soft lenses or hard lenses.

![](/api/attachments/GNWE85YY/fulltext/images/99ba01fd524e216725e63b425848b2476fc0a818df9ae72e60fb0bcfb9b02b34.jpg)  
Fig. 4. Algorithmic template.

(b) LOAD EXAMPLES. A file of examples, associated with the above specification file, must be defined. This file contains the description of a set of examples. In Section 7, Fig. 6 shows the example file CONTACT-LENSES.EX, which is associated with CONTACT-LENSES.SPEC.

(c) CREATE ALGORITHM. Once the decision problem is defined, the user can design his(her) tree building algorithm. That is, the generic algorithmic template can be initialized with user-defined functions.

![](/api/attachments/GNWE85YY/fulltext/images/15b6e623ae6a52509d7f466288e95c3524ba2159d8d234c929c2adba2e877fb2.jpg)  
Fig. 5. Evaluation function.

When the CREATE ALGORITHM command is applied, the dialog window shown in Fig. 4 is displayed.

Three command buttons are found in the upper part of the window: OK to confirm the current initialization of the template, CANCEL to go back to the previous initialization, and ALGORITHMS to access a list of previously stored initializations.

The lower part of the window includes the functions and parameters to be defined by the user. In the dialog window, the names of the current user-defined functions appear in the large rectangular area beside Evaluation Function, Selection Function, Stopping Predicate and Classification Function. The definition associated with each user-defined function can be accessed and modified by clicking on the function name with the mouse.

For example, the window shown in Fig. 5 is displayed when EVAL-ID3 is chosen. Its definition is in the lower part of the window. In the upper part, a list of names of (previously) created evaluation functions is displayed. Here, two user-defined functions are available under the names EVAL-ID3 and EVAL-GINI. EVAL-ID3 encodes the entropy formula of ID3 (as described in the previous section). EVAL-GINI is the name of some other evaluation function. Note that the current function EVAL-ID3 is highlighted with a black triangle in front of its name.

In the upper right corner of the window, a menu offers different commands. Among these commands, EDIT is used to interactively edit the current function definition. Once modified, the new definition can be saved under the same function name, or under a new name, using the CREATE command.

The current evaluation function is available for generating decision trees as soon as the window is closed with the OK command. This is a great benefit of the Common Lisp language: there is no need to recompile and link function definitions before using them.

(d) RUN ALGORITHM. Once defined, the algorithm can be applied to the current set of examples to generate a decision tree. The resulting tree is displayed in the large window in the upper right corner (see Fig. 3). The black nodes are the leaves or terminal nodes and are labelled with a class. The white nodes are non terminals, and are labelled with the attribute used to generate their children.

(e) PRUNE. This command implements the pessimistic tree pruning algorithm [7]. The aim of this procedure is to reduce the size of a decision tree, without compromising its accuracy. It is mainly a built-in algorithm. However, the user can modify the value of the pessimistic correction for the misclassification rate.

(f) TEST. This command tests the current tree with new examples (with known classification). After specifying the name of an example file, each example is processed in turn by the tree and its classification is compared with the real classification. Statistics are provided in the information window (like the proportion of correctly classified examples).

## 7. A simple decision problem

This section shows how the system can be used to generate different decision trees for a simple decision problem. The problem consists of deciding if a person can wear contact lenses and if he(she) can, what type of lenses is appropriate.

Four attributes are used to describe a patient, as shown in the specification file of Fig. 6: age (young, middle-age or old), prescription (myopia or hypermetropia), astigmatism (yes, no) and tear production rate (normal, below-normal). The three decision categories are: nothing (no contact lenses), hard lenses and soft lenses. The set of examples for inducing the decision trees is also listed in Fig. 6.

SPECIFICATION FILE: CONTACT-LENSES SPEC

<table><tr><td colspan="6">ATTRIBUTES</td></tr><tr><td>DISCRETE</td><td>AGE</td><td>3</td><td>YOUNG</td><td>MIDDLE-AGE</td><td>OLD</td></tr><tr><td>DISCRETE</td><td>PRESCRIPTION</td><td>2</td><td>MYOPIA</td><td>HYPERMETROPIA</td><td></td></tr><tr><td>DISCRETE</td><td>ASTIGMATISM</td><td>2</td><td>YES</td><td>NO</td><td></td></tr><tr><td>DISCRETE</td><td>TEAR</td><td>2</td><td>NORMAL</td><td>BELOW-NORMAL</td><td></td></tr><tr><td colspan="6">CLASSES</td></tr><tr><td>NOTHING</td><td>HARD</td><td>SOFT</td><td></td><td></td><td></td></tr><tr><td colspan="6">EXAMPLE FILE: CONTACT-LENSES EX</td></tr><tr><td>1</td><td>YOUNG</td><td>MYOPIA</td><td>NO</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>2</td><td>YOUNG</td><td>MYOPIA</td><td>NO</td><td>NORMAL</td><td>SOFT</td></tr><tr><td>3</td><td>YOUNG</td><td>MYOPIA</td><td>YES</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>4</td><td>YOUNG</td><td>MYOPIA</td><td>YES</td><td>NORMAL</td><td>HARD</td></tr><tr><td>5</td><td>YOUNG</td><td>HYPERMETROPIA</td><td>NO</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>6</td><td>YOUNG</td><td>HYPERMETROPIA</td><td>NO</td><td>NORMAL</td><td>SOFT</td></tr><tr><td>7</td><td>YOUNG</td><td>HYPERMETROPIA</td><td>YES</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>8</td><td>YOUNG</td><td>HYPERMETROPIA</td><td>YES</td><td>NORMAL</td><td>HARD</td></tr><tr><td>9</td><td>MIDDLE-AGE</td><td>MYOPIA</td><td>NO</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>10</td><td>MIDDLE-AGE</td><td>MYOPIA</td><td>NO</td><td>NORMAL</td><td>SOFT</td></tr><tr><td>11</td><td>MIDDLE-AGE</td><td>MYOPIA</td><td>YES</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>12</td><td>MIDDLE-AGE</td><td>MYOPIA</td><td>YES</td><td>NORMAL</td><td>HARD</td></tr><tr><td>13</td><td>MIDDLE-AGE</td><td>HYPERMETROPIA</td><td>NO</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>14</td><td>MIDDLE-AGE</td><td>HYPERMETROPIA</td><td>NO</td><td>NORMAL</td><td>SOFT</td></tr><tr><td>15</td><td>MIDDLE-AGE</td><td>HYPERMETROPIA</td><td>YES</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>16</td><td>MIDDLE-AGE</td><td>HYPERMETROPIA</td><td>YES</td><td>NORMAL</td><td>NOTHING</td></tr><tr><td>17</td><td>OLD</td><td>MYOPIA</td><td>NO</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>18</td><td>OLD</td><td>MYOPIA</td><td>NO</td><td>NORMAL</td><td>NOTHING</td></tr><tr><td>19</td><td>OLD</td><td>MYOPIA</td><td>YES</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>20</td><td>OLD</td><td>MYOPIA</td><td>YES</td><td>NORMAL</td><td>HARD</td></tr><tr><td>21</td><td>OLD</td><td>HYPERMETROPIA</td><td>NO</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>22</td><td>OLD</td><td>HYPERMETROPIA</td><td>NO</td><td>NORMAL</td><td>SOFT</td></tr><tr><td>23</td><td>OLD</td><td>HYPERMETROPIA</td><td>YES</td><td>BELOW-NORMAL</td><td>NOTHING</td></tr><tr><td>24</td><td>OLD</td><td>HYPERMETROPIA</td><td>YES</td><td>NORMAL</td><td>NOTHING</td></tr></table>

Fig. 6. Specification file and example file.

![](/api/attachments/GNWE85YY/fulltext/images/6772535b7c1c50e78a5f947710f614ee37ccc7c2c2620ae9b8031f43385cd41f.jpg)  
Fig. 7. Decision tree generated with ID3.

Fig. 7 shows the decision tree generated by ID3, as specified within our algorithmic template (c.f., Section 5). In this figure, the values for attribute Tear are N = Normal, BN = Below-Normal; attribute As stands for Astigmatism; attribute Pr stands for Prescription with values H = Hypermetropia, M = Myopia; finally, the values of attribute Age are Y = Young, M = Middle-age, O = Old.

In order to generate a different tree, the formula for evaluating the entropy of attribute $a_{i}$ was modified as follows:

$$
\begin{array}{l} E (a _ {i}, S) ^ {\text { new }} \\ = \frac {\sum_ {v _ {i j} \in \operatorname{domain} (a _ {i})} \left(\frac {| S _ {i j} |}{| S |}\right) \times E (S _ {i j})}{\sum_ {v _ {i j} \in \operatorname{domain} (a _ {i})} \left(\frac {| S _ {i j} |}{| S |}\right) \times \log_ {2} \left(\frac {| S _ {i j} |}{| S |}\right)}. \end{array}
$$

This modification is proposed in [6], and is aimed at reducing the bias of ID3 in favor of attributes with a larger range of values during the selection process. Hence, the function SELECT-ID3 was interactively modified (using the EDIT command), and the new definition was saved under the name SELECT-ID3-NEW.

SELECT-ID3-NEW (SET of examples, PHANTOM-ATTRIBUTES)

initialize BESTVAL with an an arbitrary large number;

for each PHANTOM-ATTRIBUTE in PHANTOM-ATTRIBUTES do

set NUMERATOR to 0;

set DENOMINATOR to 0;

for each value of PHANTOM-ATTRIBUTE do

identify the SUBSET of examples in SET with this attribute value;

NUMERATOR

$$
\begin{array}{l} \leftarrow \text { NUMERATOR } \vee + \left(\frac {| S U B S E T |}{| S E T |} \right. \\ \times E V A L - F N (S U B S E T) \Bigg); \end{array}
$$

$$
\begin{array}{l}\text { DENOMINATOR }\\\leftarrow \text { DENOMINATOR } \lor\\+ \left(\frac {| S U B S E T |}{| S E T |} \right.\\\times L O G 2 \frac {| S U B S E T |}{| S E T |}\left. \right);\end{array}
$$

endfor

![](/api/attachments/GNWE85YY/fulltext/images/a31c00f1b875535293b549a44ed75632d5c262653227319ba551f21af7683548.jpg)  
Fig. 8. A decision tree produced with the new algorithm.

Table 1

$$
\text { set   VAL   to } \frac {\text { NUMERATOR }}{\text { DENOMINATOR }};
$$

if VAL is less than BESTVAL then set BESTVAL to VAL;

set BESTATT to PHAN1OM-ATTRIBUTE;

endfor

return the best phantom attribute BESTATT.

Using the new selection function SELECT-ID3-NEW, the tree shown in Fig. 8 was produced. Note that the test on the Prescription attribute is now applied before the test on the Age attribute in the lower part of the tree.

Here, both trees correctly classify all examples in the file of Fig. 6. Since this set of examples is exhaustive, both trees are equally accurate. In situations where the set of training examples represent only a small sample of all possible examples (as it is usually the case), the trees generated by the user can be tested on additional examples with know classification, in order to identify the decision tree with the best generalization properties.

## 8. A more realistic application

This section presents another application of the system in the vehicle dispatching domain. Here, customers call a central dispatch office for some service (e.g., carrying express mail from one location to another in an urban area). After receiving a call, the dispatcher must choose a particular vehicle from a fleet of vehicles in movement to service the new request. Here, twelve attributes were used to describe the suitability of a vehicle for servicing a new request, like the vehicle's type, the distance between the current location of the vehicle and the location of the new request, the detour for servicing the new request, the service delay introduced in the planned route of the vehicle by the insertion of the new request (for other requests already allocated to this vehicle, but not serviced yet), etc.

Hence, the problem is to decide if a vehicle is suitable (or not) for servicing a request based on its current attribute description. Accordingly, only two classifications are possible for each vehicle: positive (suitable) or negative (not suitable). In this experiment, the values of the numeric attributes were normalized between 0 and 1, and the unit interval was divided into ten non-overlapping subintervals (see Section 3.3).

A file of service requests from a typical operations day was obtained from a courier service company operating in the city of Montreal. Based on this file, the evolution of the operations and the movement of the fleet of vehicles were simulated, using an interactive-graphic vehicle dispatching system $[14]$ . During the simulation, a dispatcher identified the most suitable vehicle(s) for each new request. Although many vehicles could be identified as suitable for a given request, the dispatcher assigned only one vehicle at the end, so as to allow the simulation to proceed. At the end, 1,680 different attribute descriptions were available, as well as their classification. Given that only a fraction of the vehicles were suitable for each new request, the total number of negative examples was much larger than the total number of positive examples. Accordingly, the 380 positive examples were all kept, and 380 negative examples were randomly chosen. Then, the 760 examples were divided into three different training sets (each with 280 positive and 280 negative examples) and testing sets (each with 100 positive and 100 negative examples). The training and testing sets were obtained by selecting three disjoint sets of 100 examples for testing, and by using the remaining examples in each case for training.

Using our system, we tested ID3, ID3-NEW, and the GINI algorithm [1], which were all easily implemented within our algorithmic template. The resulting trees are very deep, even after the application of the pruning procedure, and are not shown here. However, the average performance of the pruned trees on the testing set are reported in Table 1.

Since most attributes are real-valued, the set of examples is often split in two along the boundaries of the real domains. Accordingly, both ID3 and ID3-NEW were equally effective, with about 89% (87%) of correctly classified positive (negative) examples. GINI was outperformed by the two previous methods, but the percentage of correctly classified examples was still well over 80%. The best tree produced by ID3-NEW just happened to be the best tree over all methods and testing sets. It is characterized by an early test on the service delay attribute, which measures the service quality, as well as the detour attribute, which measures the operations cost (e.g., a long detour implies high fuel consumption). This tree has since been incorporated within the vehicle dispatching system, in order to focus the attention of the dispatcher on the most interesting vehicles when a new request must be dispatched.

Average % of correct classification on the testing sets of dispatching examples

<table><tr><td>Class</td><td>GINI</td><td>ID3</td><td>ID3-NEW</td></tr><tr><td>Positive</td><td>86.3%</td><td>89.0%</td><td>89.3%</td></tr><tr><td>Negative</td><td>83.6%</td><td>87.3%</td><td>87.3%</td></tr></table>

This example, and the previous example in Section 7, illustrate how the system can be used to quickly design different tree building algorithms for a particular decision problem. Here, we applied algorithmic ideas found in the literature, but any new idea that fits into the generic framework can be tested to produce different and (hopefully) better decision trees for a given problem.

## 9. Limitations of the system

The current system was not developed for commercial exploitation, and it still exhibits serious limitations that should be addressed in the future. First, the system does not support, uncertain or unknown data. This is a serious concern in many real-world problems, and different solution avenues based on probabilistic methods have already been proposed [8]. Another concern is the design of a common algorithmic framework for simplifying decision trees. This task is difficult, given that some algorithms simplify the decision tree at the same time as it is constructed (by deciding not to divide a subset of examples any further), while others prune the tree after it is constructed. Even among pruning algorithms, important discrepancies are observed. For example, the minimal cost-complexity pruning algorithm does not produce a single tree but rather a sequence of trees [1]; some pruning algorithms rely on alternative testing sets to estimate the misclassification rate; etc.

With respect to the size of the problems that can be handled by the system, there is really no (practical) limitations in terms of number of attributes per example or number of examples per application. This is related to the choice of the platform, a Sun workstation with a large virtual memory. However, it is clear that this choice, along with the choice of the Medley programming environment, greatly limit the number of potential users.

Finally, additional features like windowing, automatic rule production [9], and structured induction [11] could be implemented as well in the future.

## 10. Conclusion

The main contribution of this work concerns the development of a computer system that does not incorporate any built-in algorithm. Rather, the system offers a generic algorithmic template, from which a broad spectrum of user-defined tree construction algorithms can be created and tested on different decision problems.

Although the current system simply provides tools for quickly creating and testing new (or known) tree building algorithms, it would be interesting to develop an intelligent DSS or even an expert system in this domain. Such a system would take a specification file and an example file as input, and would suggest a good tree-building algorithm from a close analysis of the characteristics of the decision problem. We are still far from such a system, but our environment could help to develop this expertise by allowing the designers of algorithms to freely experiment with different algorithms.

## Acknowledgements

Financial support for this work was provided by the Natural Sciences and Engineering Research Council of Canada (NSERC) and by the Quebec Fonds pour la Formation de Chercheurs et l'Aide à la Recherche (FCAR).

## Appendix 1. The generic algorithmic template

In the following, a complete description of the generic algorithmic template for both discrete and continuous attributes is provided.

## Notation

$S =$ initial set of examples $A_{\mathrm{d}} =$ set of discrete attributes $A_{\mathrm{c}} =$ set of continuous attributes $A_{\mathrm{c}}*$ $=$ set of attributes derived from $A_{\mathrm{c}}$ $v_{ij} =$ jth value of discrete attribute $a_i$ $S_{ij} =$ subset of examples with value $v_{ij}$ for discrete attribute $a_i$ $b_{ij} = j$ th boundary of continuous attribute $a_i$ $b\inf_{i} =$ lower bound on the domain of continuous attribute $a_i$ $b\sup_{i} =$ upper bound on the domain of continuous attribute $a_i$ $S_{ij1} =$ subset of examples with values in the interval $[b\inf_{i},b_{ij}]$ for continuous attribute $a_i$ $S_{ij2} =$ subset of examples with values in the interval $[b_{ij},b\sup_{i}]$ for continuous attribute $a_i$

Main procedure (S)

Create the root

Assign the whole set of examples S to the root
Call Tree Expansion Procedure(root, $A_{d}$ , $A_{c}$ )

Tree expansion procedure (node, $A_{d}, A_{c}$ )

Step 1. Check the stopping conditions
If Stopping predicate is True or the default stopping condition applies to the set of examples in node then

classify the node with Classification function and Exit
Step 2. Set the initial value of the variables $A_c * \leftarrow$ empty set
For each attribute $a_i$ in $A_c$ do
For each boundary $b_{ij}$ of attribute $a_i$ do
create attribute $a_{ij}$ and add it to $A_c*$ Entropymin $\leftarrow$ arbitrary large number
Step 3. Compute the minimum entropy
/Discrete attributes/
For each discrete attribute $a_i$ in $A_d$ do
For each value $v_{ij}$ of attribute $a_i$ do
evaluate Entropy $(S_{ij})$ with Evaluation Function
if Entropy $(S_{ij}) <$ Entropymin then
set Entropymin to Entropy $(S_{ij})$ /Continuous attributes/
For each continuous attribute $a_{ij}$ in $A_c*$ do
evaluate Entropy $(S_{ij1})$ with Evaluation Function
if Entropy $(S_{ij1}) <$ Entropymin then
set Entropymin to Entropy $(S_{ij1})$ evaluate Entropy $(S_{ij2})$ with Evaluation Function
if Entropy $(S_{ij2}) <$ Entropymin then
set Entropymin to Entropy $(S_{ij2})$ Step 4. Create the phantom attributes
/Discrete attributes/
For each discrete attribute $a_i$ in $A_d$ do
For each value $v_{ij}$ of attribute $a_i$ do
if Entropy $(S_{ij}) \leq$ Entropymin $\times$ TL then
put $v_{ij}$ in the list $L_{i1}$ of individual values of the phantom attribute $a'_i$ otherwise,
put $v_{ij}$ in the list $L_{i2}$ of default values of the phantom attribute $a'_i$ /Continuous attributes/
For each continuous attribute $a_{ij}$ in $A_c*$ do
if Entropy $(S_{ij1}) \leq$ Entropymin $\times$ TL then
put $[binf_i, b_{ij}]$ in the list $L_{ij1}$ of individual values of the phantom attribute $a'_{ij}$ otherwise,
put $[binf_i, b_{ij}]$ in the list $L_{ij2}$ of default values of the phantom attribute $a'_{ij}$ if Entropy $(S_{ij2}) \leq$ Entropymin $\times$ TL then
put $[b_{ij}, bsup_i]$ in the list $L_{ij1}$ of individual values of the phantom attribute $a'_{ij}$ otherwise,

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
put $[b_{ij}, bsup_i]$ in the list $L_{ij2}$ of default values of the phantom attribute $a_{ij}'$

Step 5. Validate the phantom attributes
Remove any phantom attribute with no meaningful values (i.e., no values in the list $L_{il}$ or $L_{ij1}$)
Step 6. Select a phantom attribute
Select the best phantom attribute $a_s'(a_{st}')$ with Selection Function
Step 7. Expand the current node
/Discrete attribute/
If discrete attribute $a_s'$ is selected then
For each value $v_{sj}$ in the list $L_{s1}$ do
create a child node
assign to the child node the subset of examples $S_{sj}$
Create a child node for the list of default values $L_{s2}$
Assign the remaining examples to that node /Continuous attribute/
If continuous attribute $a_{st}'$ is selected then
Create two child nodes
Assign the subset of examples $S_{st1}$ to the first node
Assign the subset of examples $S_{st2}$ to the second node
Step 8. Update the status of the selected attribute /Discrete attribute/
If discrete attribute $a_s'$ is selected then
if $L_{s2}$ contains a single attribute value then
remove $a_s$ from $A_d$
otherwise
set the list of values of $a_s$ to $L_{s2}$
/Continuous attribute/
If continuous attribute $a_{st}'$ is selected then
remove $a_s$ from $A_c$
if there is a boundary between $binf_s$ and $b_{st}$ then
add attribute $a_{s1}$ to $A_c$
set $binf_{s1}$ to $binf_s$ and $bsup_{s1}$ to $b_{st}$
if there is a boundary between $b_{st}$ and $bsup_s$ then
add attribute $a_{s2}$ to $A_c$
set $binf_{s2}$ to $b_{st}$ and $bsup_{s2}$ to $bsup_s$
Step 9. Recursion
For each child node do:
call Tree Expansion Procedure(child node, $A_d$, $A_c$)
</div>

## Appendix 2. Function definitions using Lisp code

In the current implementation of the system, function definitions must be written using Lisp code. Here, we provide the code for the functions EVAL-ID3, SELECT-ID3, CLASS-MAJORITY found in Section 5.3 and the function SELECT-ID3-NEW found in Section 7.

## Section 5.3

EVAL-ID3:
(DEFUN EVAL-ID3 (SET)
(P.ENTROPY SET)
or
(DEFUN EVAL-ID3 (SET)
(LET ((NBEX (LENGTH SET))
(CLASSES (P.CLASSES))
SUM RATIO)
(SETQ SUM 0)
(DOLIST (C CLASSES)
(SETQ RATIO (/ (P.NBEX-CLASS SET C) NBEX))
(IF (>RATIO 0)
(SETQ SUM (+SUM (\*-1 RATIO (LOG RATIO 2))))))
(RETURN-FROM EVAL-ID3 SUM)
)

SELECT-ID3:
(DEFUN SELECT-ID3 (SET PH-ATTRIBUTES)
(LET((NBEX (LENGTH SET))
(BESTVAL MOST-POSITIVE-FIXNUM)
BESTATT NBEX-SUBSET RATIO-SUBSET VAL)
(DOLIST (PH-ATT PH-ATTRIBUTES)
(SETQ VAL 0)
(DOLIST (SUBSET (P.PH-SPLIT SET PH-ATT))
(SETQ NBEX-SUBSET (LENGTH SUBSET))
(SETQ RATIO-SUBSET (/ NBEX-SUBSET NBEX))
(SETQ VAL
(+VAL (\*RATIO-SUBSET (EVAL-FN SUBSET))))))

(IF (<VAL BESTVAL)
    (SETQ BESTVAL VAL BESTATT PH-ATT)))
(RETURN-FROM SELECT-ID3 BESTATT)

CLASS-MAJORITY:
(DEFUN CLASS-MAJORITY (SET)
(LET ((CLASSES (P.CLASSES))
NBEX-CLASS NBEX-MAX NBEX-CLASS)
(SETQ NBEX-MAX 0)
(DOLIST (C CLASSES)
(SETQ NBEX-CLASS (P.NBEX-CLASS SET C))
(IF(> NBEX-CLASS NBEX-MAX)
(SETQ CLASS-MAX C NBEX-MAX NBEX-CLASS)))
(RETURN-FROM CLASS-MAJORITY CLASS-MAX)
)

Section 7

SELECT-ID3-NEW:
(DEFUN SELECT-ID3-NEW (SET PH-ATTRIBUTES)
(LET((NBEX (LENGTH SET))
(BESTVAL MOST-POSITIVE-FIXNUM)
BESTATT NBEX-SUBSET RATIO-SUBSET NUM DENOM VAL)
(DOLIST (PH-ATT PH-ATTRIBUTES)
(SETQ NUM 0 DENOM 0)
(DOLIST (SUBSET (P.PH-SPLIT SET PH-ATT))
(SETQ NBEX-SUBSET (LENGTH SUBSET))
(SETQ RATIO-SUBSET (/ NBEX-SUBSET NBEX))
(SETQ NUM
(+NUM (\*RATIO-SUBSET (EVAL-FN SUBSET))))
(SETQ DENOM
(+DENOM (\*RATIO-SUBSET (LOG RATIO-SUBSET 2))))
(SETQ VAL (/ NUM DENOM))
(IF (<VAL BESTVAL)

(SETQ BESTVAL VAL BESTATT PH-ATT))
(RETURN-FROM SELECT-ID3 BESTATT)
)

## References

[1] L. Breiman, J.H. Friedman, R.A. Olshen and C.J. Stone, Classification and Regression Trees (Wadsworth, 1984).

[2] J. Cheng, U.M. Fayyad, K.B. Irani and Z. Qian, Improved Decision Trees: A Generalized Version of ID3, In: Proceedings of the Fifth International Conference on Machine Learning (1988) 100–106.

[3] J.H. Holland, Adaptation in Natural and Artificial Systems (The MIT Press, 1992).

[4] P.G.W. Keen and M.S. Morton, Decision Support Systems: An Organizational Perspective (Addison-Wesley, NY, 1978).

[5] M.L. Manaheim, Issues in the Design of a Symbiotic DSS, In: Proceedings of HICSS-22, IEEE Computer Society (1988) 14–23.

[6] J.R. Quinlan, Induction of Decision Trees, Machine Learning 1 (1986) 81-106.

[7] J.R. Quinlan, Simplifying Decision Trees, International Journal of Man-Machine Studies 27 (1987) 221-234.

[8] J.R. Quinlan, Probabilistic Decision Trees, In: Y. Kodratoff and R. Michalski, Eds., Machine Learning: An Artificial Intelligence Approach, Vol. III (Morgan Kaufmann, 1990) 140–152.

[9] J.R. Quinlan, C4.5: Programs for Machine Learning (Morgan Kaufmann, 1993).

[10] D.E. Rumelhart and J.L. McClelland, Parallel Distributed Processing: Explorations in the Microstructure of Cognition (The MIT Press, 1986).

[11] A.D. Shapiro, Structured Induction in Expert Systems (Addison-Wesley, 1987).

[12] S. Schocken and G. Ariav, Neural Networks for Decision Support: Problems and Opportunities, Decision Support Systems 11 (1994) 393–414.

[13] M.J. Shaw, Guest Editor, Decision Support Systems 10, Special issue on Machine Learning Methods for Intelligent Decision Support (1993).

[14] Y. Shen, J.Y. Potvin, J.M. Rousseau and S. Roy, A Computer Assistant for Vehicle Dispatching with Learning Capabilities, Technical Report CRT-939, Centre de recherche sur les transports, Université de Montréal.

[15] R.H. Sprague, A Framework for the Development of Decision Support Systems, MIS Quarterly 4 (1980) 1–26.

[16] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, 1982).

[17] R.H. Sprague and H.J. Watson, Decision Support Systems: Putting Theory into Practice (Prentice-Hall, 1986).

[18] G.L. Steele, Common Lisp: The Language, Second Edition (Digital Press, 1990).

![](/api/attachments/GNWE85YY/fulltext/images/97e6a8ba6ddfc6c73496c8c43e5a01ca7db811c734337e5743eeedfb59c786de.jpg)

Jean-Yves Potvin is Associate Professor at the Centre de recherche sur les transports and at the Department of computer science and operations research of Montreal University. He received a PhD degree in computer science from Montreal University in 1987. Then, he completed a postdoctoral fellowship at Carnegie-Mellon University in 1988. His current research interests are in the application of tabu search and genetic algorithms for solving complex

vehicle routing and scheduling problems.

![](/api/attachments/GNWE85YY/fulltext/images/d4b0a9dfd7268f5562bc7866b0729ceccce28a64343d78b7d909c9d096cc073f.jpg)

Tanguy Kervahut received his MSc degree in computer science from the Department of Computer Science and Operations Research of Montreal University in 1992. He is now working as programmer-analyst at Giro Inc., a software company specialized in vehicle routing and scheduling applications. He is involved in particular in the development of routing and scheduling software for municipal services and postal applications.
