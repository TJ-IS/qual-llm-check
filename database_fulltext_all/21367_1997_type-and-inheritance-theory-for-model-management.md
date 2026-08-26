---
otero_id: 21367
otero_key: "752XGSCH"
title: "Type and inheritance theory for model management"
authors: "Jian Ma"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00052-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Type and inheritance theory for model management

Jian Ma \*

Department of Information Systems, City University of Hong Kong, 83 Tat Chee Avenue, Kowloon, Hong Kong

Received 21 August 1995; revised 22 June 1996; accepted 22 August 1996

## Abstract

Model management is one of the important research areas in decision support systems (DSS). Similar to that in data management, the research activities in model management should include the representation of model base structures and design of model base systems. Object-oriented methods have been used for the representation of model base structures. Based on a proposed object-oriented framework, this paper presents the use of type rules and inheritance theory for the design of model base systems. Examples are used to illustrate that the proposed design theory can help to reduce redundancy and avoid inconsistency for the design of model base systems.

Keywords: Decision support systems; Model management; Model base systems; Object-oriented specification and design; Type; Inheritance theory

## 1. Introduction

By definition, a DSS is a software system designed to support semistructured or unstructured decisions in order to improve the effectiveness of decision making $[5]$ . One of the most commonly accepted frameworks for DSS $[16]$ is to classify it as comprising three sets of capabilities: data management capability, model management capability, and the management capability for an interface between users and the system. Data management is thought of as a well established research area because of the maturing technology in database modeling, database design and database management systems. However, model management is a relatively new field of research. Three important topics in model management include representation of model base structures, design of model base systems and the organizational environment of model management systems [1,2].

Several approaches have been proposed for the representation of model base structures. The relational approach $[2]$ views a decision model as a virtual relation between input and output domains. The entity-relationship approach $[6]$ treats a decision model as an entity comprising a number of attributes and an interface among entities as a relationship. These two approaches make use of the existing methods, but fail to wholly support the reuse of decision models. Whereas the model abstraction approach $[7]$ adopts the concept of data abstraction in modern programming languages and encapsulates data objects, procedures and assertions within a model abstraction. It separates the function specifications from their implementations in a decision model, but the relationships among decision models are not well specified. The structured modeling approach $[8]$ employs a hierarchically organized, partitioned and attributed acyclic graph to represent relationships in decision models. One of the hot research topics in DSS today is the application of object-oriented methodology to model management. Current object-oriented approaches $[10,15]$ view a decision model as a collection of objects which perform the various model management functions by receiving and responding to messages. These methods make use of the concepts in object-oriented programming languages. However, they emphasize the implementation details and lack a design theory to discover the inheritance relationship for the reuse of decision models.

The emphasis of this paper is on the design of model base systems. Thus the static properties or structures of decision models and the relationships among them will be studied. One of the current trends for the design of model base systems is the object-oriented approach. Burslal and Lamson [3] applied an algebraic approach to represent the concepts of data abstraction and information hiding. By definition, an algebra is formally a mathematical entity composed of sets of values and operations on these values. Signature is a method to define an algebra, which is a declaration of the types, constants and operations of interest. The main restriction of the algebraic approach is that it is first order; that is, functions are not first class values and can not be passed as inputs to other functions, returned from functions, or stored within data structures.

In order to provide a greatly enhanced degree of expressive power, a form of second order $\lambda$ -calculus was introduced. Mitchell and Plotkin [14] used an extended version of the second order $\lambda$ -calculus, called SOL, to represent data abstraction. Cardelli and Wegner [4] extended the second order $\lambda$ -calculus by introducing universal qualifications and information hiding (packaging) to model abstract data types and bounded qualifications to model subtypes and type inheritance. As a result, a language called FUN has been designed. The second order typed $\lambda$ -calculus supports the specification of data abstraction and information hiding, but it lacks the ability to specify inheritance relationships between two classes.

In model management, a decision model is an abstract simple representation of a decision making process, which consists of a set of variables and functions specifying the relationship among these variables [9]. In the proposed object-oriented model base structure [12,18], a class is a conceptual schema specifying a decision model. Based on a set of common data structures, it groups functions together in a fixed set. Class is the realization of data abstraction and information hiding concepts, within which functions are specified using typed $\lambda$ -calculus. Inheritance is then a mechanism to allow a new class to be defined by inheriting function properties from existing ones. Based on the proposed object-oriented framework, this paper proposes the type inheritance rules and inheritance theory for the design of model base systems.

## 2. Object-oriented framework for model base structures

A type is a set of values with certain properties. A function is then a mapping from one type into another. In the notation $f: \sigma \to \tau$ , the expression “ $\sigma \to \tau$ ” is called the type of function f, which denotes the set of all functions from type $\sigma$ to type $\tau$ . Typed $\lambda$ -calculus is used as a formal language to specify functions in the proposed object-oriented framework [11,12].

A class is a conceptual schema which groups relevant typed $\lambda$ -expressions together to specify a decision model. It is formally defined as:

$$
C = \left\{e _ {1}, e _ {2}, \dots , e _ {n} \right\},
$$

where $C$ is the global name of the class and each $e_i$ $(1 \leq i \leq n)$ is an expression local to $C$ .

Inheritance is a mechanism to allow a new class to be defined by inheriting function properties from existing ones. Let $C'$ be a new class which makes use of the expressions from existing classes $C_1, C_2, \ldots, C_n$ in a model base system, then it can be denoted by:

$$
C ^ {\prime} = \left\{e _ {1} ^ {\prime}, e _ {2} ^ {\prime}, \dots , e _ {m} ^ {\prime} \right\}
$$

$$
\text { inherit   from } C _ {1}, C _ {2}, \dots , C _ {n},
$$

where each $e_{i}^{\prime}\ (1 \leq i \leq m)$ is either an incremental modification of the corresponding expression in class $C_{i}\ (1 \leq i \leq n)$ or an expression which never appears in its superclasses.

In the proposed object-oriented framework, every expression is defined to be local to a class. Therefore the same expression name may appear in more than one class. In order to avoid this ambiguity in the inheritance case, the expression name should be explicitly distinguished by concatenating class name with “.” and the expression (e.g. C.e) when necessary.

Example 1. Inventory plays a vital role in the operation of an enterprise. It should be efficiently managed so that the total cost could be reduced. In the following inventory control model [16], we assume that the demand is known and steady. The notations used are:

$$
\begin{array}{l l} \text {Let} \\ Q & = \text {lot size per order}, \\ Q ^ {*} & = \text {optimal lot size per order}, \\ R & = \text {units required (demand) per unit time}, \\ C _ {0} & = \text {cost of ordering or setup per order placed}, \\ C _ {h} & = \text {cost of holding a unit of inventory per unit time}, \end{array}
$$

$C(Q) =$ total relevant cost (ordering + holding) per unit time for lot size $Q$ .

For a simplest optimal lot size model, the total relevant cost is decided by:

$$
C (Q) = C _ {0} \frac {R}{Q} + C _ {h} \frac {Q}{2}.
$$

Then the optimal lot size and the optimal relevant cost are determined by:

$$
\begin{array}{l} Q ^ {*} = \sqrt {\frac {2 R C _ {0}}{C _ {h}}}, \\ C (Q ^ {*}) = \sqrt {2 R C _ {0} C _ {h}} = C _ {h} Q ^ {*}. \end{array}
$$

Thus the simplest optimal lot size model can be specified in class INVS:

$$
\begin{array}{l l} \text {INVS} = \{\quad & C _ {0}: \text {REAL}; \\ & C _ {h}: \text {REAL}; \\ & Q ^ {*}: \text {REAL} \to \text {REAL}; \\ & Q ^ {*} = \lambda R. \text {SQRT} ((2 ^ {*} R ^ {*} C _ {0}) / C _ {h}), \\ & C Q ^ {*}: \text {REAL} \to \text {REAL}; \\ & C Q ^ {*} = \lambda R. \text {SQRT} (2 ^ {*} R ^ {*} C _ {0} ^ {*} C _ {h}) \\ & \}. \end{array}
$$

Where SQRT is a built-in function, $Q^{*}$ is the function to compute the cost of holding a unit of inventory per unit time and $CQ^{*}$ is the function to compute the total relevant cost per unit time for lot size Q. In reality, the inventory history should be considered. As a result, the problem refers to the optimal lot size model with uniform replenishment.

Example 2. Let $R' = \text{maximum production possible per unit time } (R' > R)$ , and $v = 1 - R / R'$ , the solution then becomes:

$$
\begin{array}{l} Q ^ {*} = \sqrt {\frac {2 R C _ {0}}{C _ {h} v}}, \\ C (Q ^ {*}) = \sqrt {2 R C _ {0} C _ {h} v} = C _ {h} v Q ^ {*}. \end{array}
$$

The improved inventory control model can inherit properties from class INVS and is then specified in class INVUR:

$$
\begin{array}{l}\text {INVUR = \{\quad Q^{*} :(REAL\to REAL) \times REAL}\\\qquad \qquad \qquad \qquad \rightarrow \text {REAL;}\\\qquad \qquad \qquad Q ^ {*} = \lambda \text {INVS.} Q ^ {*},\\\qquad \qquad \qquad \lambda v. (\text {INVS.} Q ^ {*} / \text {SQRT} (v)),\\\qquad \qquad C Q ^ {*}: (\text {REAL} \to \text {REAL}) \times \text {REAL}\\\qquad \qquad \qquad \rightarrow \text {REAL;}\\\qquad \qquad \qquad C Q ^ {*} = \lambda \text {INVS.} C Q ^ {*},\\\qquad \qquad \qquad \lambda v. (v ^ {*} \text {INVS.} C Q ^ {*})\\\qquad \qquad \qquad \}\\\text {inherit from INVS.}\end{array}
$$

Where INVUR. $Q^{*}$ and INVUR. $CQ^{*}$ are improved functions from the incremental modification of INVS. $Q^{*}$ and INVS. $CQ^{*}$ with the consideration of uniform replenishment.

Reuse is encouraged because it helps to reduce the redundancy and avoid the inconsistency in an object-oriented design of model base systems. However there are exceptions that a new class can be defined from scratch in order to achieve the best performance.

Inheritance provides a mechanism to specify the relationship for reuse of classes in a model base system. However there is still a need to develop a formal theory for the conceptual design of model base systems. For this purpose, Section 3 and Section 4 present the type rules and inheritance theory respectively.

3. Type rules for discovery of inheritance relationships between classes

In the proposed framework, class is a basic unit for specifying a decision model. Within a class, most of the expressions are typed functions with the form: $f: \rho \to \tau$ , for $x: \rho$ and $e(x): \tau$ . Thus the type rules for functions can be derived.

Rule 1. If there exist types $\rho \supset \rho'$ and the function $f: \rho \to \tau$ , then $f: \rho' \to \tau$ is a specialized function of $f: \rho \to \tau$ .

In mathematics, a function is defined to be a mapping from a type to a new type, then for any value $x \in \rho' \subset \rho$ , there exists $f(x) \in \tau$ . Thus the specialized function $f: \rho' \to \tau$ shares the same function implementation with $f: \rho \to \tau$ .

Example 3. In the simplest optimal lot size inventory model of Example 1, R is an integer, denoting the units required per unit time. Hence the optimal lot size function becomes:

$Q^{*}:\mathrm{INTEGER}\rightarrow \mathrm{REAL};$

$$
Q ^ {*} = \lambda R. \mathrm{SQRT} \left(\left(2 ^ {*} R ^ {*} C _ {0}\right) / C _ {h}\right).
$$

Since INTEGER ⊂ REAL, $Q^{*}$ : INTEGER → REAL is a specialized function of $Q^{*}$ : REAL → REAL in class INVS.

Rule 2. If there exist types $\tau \supset \tau'$ and the function $f: \rho \to \tau$ , such that $f: \rho \to \tau'$ is meaningful, then $f: \rho \to \tau'$ is a specialized function of $f: \rho \to \tau$ .

The condition that $f: \rho \to \tau'$ is meaningful means that for any value $x \in \rho$ , there exists $f(x) \in \tau'$ . Then the mathematical explanation of the definition can be stated as: given any value $x \in \rho$ , there exists $f(x) \in \tau' \subset \tau$ . Thus $f: \rho \to \tau'$ shares the same function implementation with $f: \rho \to \tau$ .

Rule 3. If there exist types $\tau \supset \tau'$ , $\rho \supset \rho'$ and the function $f: \rho \to \tau$ , such that $f: \rho' \to \tau'$ is meaningful, then $f: \rho' \to \tau'$ is a specialized function of $f: \rho \to \tau$ .

This rule is in fact the combination of Rules 1 and 2. As a result, $f: \rho' \to \tau'$ shares the same function implementation with $f: \rho \to \tau$ .

Example 4. Given two integer constants a and b, if we let the production volume x be an integer, the total production cost f is determined by:

$f\colon \mathrm{INTEGER}\to \mathrm{INTEGER};$

$$
f (x) = \lambda x. (a + b ^ {*} x),
$$

which denotes a mapping, INTEGER → INTEGER, and is a specialized function of f:REAL → REAL.

The inheritance relationship between two classes can be derived from the type inheritance rules for specialized functions. Therefore we have the following definition.

Definition 1. For a given class $C = \{e_1, e_2, \ldots, e_n\}$ , and a new class $C' = \{e_1', e_2', \ldots, e_m'\}$ , where $m \leq n$ . If expression $e_i'$ (for some $i$ in $(1 \leq i \leq n)$ ) is a specialized function of the corresponding expression $e_i$ in class $C$ , $C'$ is then a subclass of $C$ , which inherits functions from its super-class $C$ . Formally, we write

$$
C ^ {\prime} = \left\{e _ {j 1} ^ {\prime}, \dots , e _ {j k} ^ {\prime} \right\}
$$

inherit from $C$ ,

where $e'_{ji}$ ( $1 \leq ji \leq m$ ) is not a specialized function of the corresponding expression in the superclass C.

Example 5. In the integer programming (IP) model, IPGOAL is an incremental modification of GOAL in class LP [17]. Hence, IP is a subclass of LP, which can be specified by inheriting function properties from LP.

$$
\begin{array}{l}\mathrm{IP} = \left\{\text {IPGOAL}: \left(\left(R _ {n} ^ {n} \times R _ {n} \times R _ {n} \rightarrow R _ {n}\right)\rightarrow \mathrm{IR} n\right)\right.\\\rightarrow \text {REAL} \Big \}\end{array}
$$

inherit from LP,

where IPGOAL is a composite function which extends the function GOAL in the class LP to generate integer optimal results.

An inheritance rule checking system (IRCS) has been developed for the object-oriented design of model base systems [13]. The IRCS is to check the correctness of the model class specification and to discover the inheritance relationship between two classes.

## 4. Inheritance theory for design of model base systems

In the proposed object-oriented framework, class and inheritance are used to specify decision models and their relationships respectively. Classes and inheritance relationships are the most important components in a model base system. We introduce the following concepts to help understand the relationships among classes.

\- Elements: classes;

\- Inheritance assertions: ordered pairs of elements;

\- Inheritance paths: sequences of elements with length greater than two.

Elements are derived from real world classes. They can be distinguished by signs such as positive (+), negative (−) or neutral (#) respectively. For example, +LP refers to the class of a linear programming model, and +MOLP to the class of a multiobjective linear programming model.

We introduce $\Phi$ to denote the set of all classes with three signs (e.g. +, -, #) referred to in a model base system. Then the inheritance assertions are elements of $\Phi$ , i.e. they are ordered pairs of elements. In the design of model base systems, there are three kinds of well formed ordered pairs. Thus the set of ordered pairs can be represented as fixed labels and a directed graph called an inheritance graph. The well-formed ordered pairs can be represented by three kinds of links, called IS-A, IS-NOT-A and NO-CONCLUSION links. If we let the variables $x$ and $y$ represent the elements of $\Phi$ , then the correspondence between ordered pairs and inheritance graph links is shown in Fig. 1.

For example, the assertion “IP is a subclass of LP” is represented by $< +IP, +LP>$ , and the negative assertion “MOLP is not a subclass of IP” is represented by $< +MOLP, -IP>$ . Note that the first element of an inheritance assertion is always positive, while the second element may be either positive, negative or neutral. The three kinds of ordered pairs listed in Fig. 1 are the only ones to be used in the conceptual design of model base systems, because they represent the complex relationships among model classes in a model base system. The three kinds of ordered pairs can be represented as different links in an inheritance graph as shown in Fig. 2.

![](/api/attachments/752XGSCH/fulltext/images/7d6bddeb8ea4dc68eb7704bebbd1613c74839148436184572abba854d3d8112e.jpg)  
Fig. 1. Ordered pairs and inheritance graph links in a model base system.

![](/api/attachments/752XGSCH/fulltext/images/9c963fd6f811e67782ea989f902e1a62a5ee4ee7e64490534969c25df5035dfd.jpg)  
Fig. 2. The three kinds of links in an inheritance graph.

In Fig. 2, each IS-A link in the inheritance graph is drawn as an arrow with a closed head. Each IS-NOT-A link arrow has railroad tracks and each NO-CONCLUSION link is an arrow drawn with a double dashed line.

Example 6. Let class LA represent the linear algebra model for addition and multiplication operations on a matrix, LP is then a subclass of LA. Taking the consideration of previous classes in management science or operations research (MS/OR), an inheritance path is formed as shown in Fig. 3.

The sequences of length greater than two describe the path through the inheritance graph. In general, a sequence $< y_{1}, \ldots, y_{n}>$ can be treated as chains of nonmonotonic inferences. For example, let +TP be the class of the transportation programming model, the sequence $< +\mathrm{TP}, +\mathrm{IP}, +\mathrm{LP}>$ may be read as "TP which is a subclass of IP is therefore a subclass of LP".

Design of classes is the main concern for building model base systems. Now let $l = <c_{1}, \ldots, c_{n}>$ denote an inheritance path in a model base system $\Phi$ , it means that the pairs $< +c_{1}, +c_{2}>$ , $\ldots$ , $< +c_{n-1}, +c_{n}>$ are all in $\Phi$ . The “+” sign is often omitted when the meaning is clear.

![](/api/attachments/752XGSCH/fulltext/images/bcc2211ca4417f7ddab9124a181fd5e5a29f8b2d238bcd50ed2b4bc3e14f82d8.jpg)  
Fig. 3. Description of an inheritance path in OR/MS.

Definition 2. The conclusion set of a model base system $\Phi$ , written as $C(\Phi)$ , is the set of all pairs $<c_i, c_j>$ such that a sequence $<c_i, \ldots, c_j>$ appears in $\Phi$ .

The conclusion set $C(\Phi)$ helps to find the inheritance relationship between two classes in the sequences of a model base system $\Phi$ .

Example 7. If a model base system $\Phi$ contains the sequence $<\mathrm{TP},\mathrm{IP},\mathrm{LP}>,$ then its conclusion set $C(\Phi)$ contains the sequence $<\mathrm{TP},\mathrm{LP}>.$

Definition 3. A model base system $\Phi$ contradicts the sequence $< c_{1}, \ldots, c_{n}>$ if and only if $< c_{1}, -c_{i} > \in C(\Phi)$ for some $i$ in $1 \leq i \leq n$ .

The notion of contradiction can be used to prevent any new sequence from appearing in a model base system $\Phi$ that would conflict with what is already in $\Phi$ .

Example 8. The sequences $<\mathrm{TP}, \mathrm{LP}>$ and $<+\mathrm{TP}, -\mathrm{LP}>$ are mutually contradictory. If a model base system $\Phi$ contains $<\mathrm{TP}, \mathrm{LP}>$ , the sequence $<+\mathrm{TP}, -\mathrm{LP}>$ will contradict the one that already exists in $\Phi$ and thus should be eliminated.

Definition 4. A sequence $l = <c_1, \ldots, c_n >$ is inheritable in a model base system $\Phi$ if and only if $n > 2$ , $\Phi$ contains both $<c_1, \ldots, c_{n-1}>$ and $<c_2, \ldots, c_n>$ , and $\Phi$ does not contradict the sequence $l$ .

Example 9. If a model base system $\Phi$ contains two sequences $<\mathrm{TP},\mathrm{IP},\mathrm{LP}>$ and $<\mathrm{IP},\mathrm{LP},\mathrm{LA}>,$ then $<\mathrm{TP},\mathrm{IP},\mathrm{LP},\mathrm{LA}>$ is inheritable in $\Phi$ , as shown in Fig. 4.

Inheritance allows us to form a new class by modifying functions from existing classes. This can bring exceptions to the inheritance paths. Hence simple concatenation of sequences $<c_{1},\ldots,c_{i}>$ and $<c_{i},\ldots,c_{n}>$ can not guarantee to be inheritable in $\Phi$ .

Definition 5. A model base system $\Phi$ is closed under inheritance if and only if $\Phi$ contains every sequence inheritable in $\Phi$ .

![](/api/attachments/752XGSCH/fulltext/images/18296f261a33d52e064e7c8a6bc95bf41e305eac482947452f37c1d4c39c0b70.jpg)  
Fig. 4. An inheritable sequence of classes in MS/OR.

The redundancy among model classes can be reduced if every sequence in the model base system $\Phi$ is inheritable.

Theorem 1. If a model base system $\Phi$ is closed under inheritance and contains the sequence $< c_{1}, \ldots, c_{n}>$ , then it also contains all contiguous subsequences $< c_{i}, \ldots, c_{j}>$ for $1 \leq i < j \leq n$ .

Proof. For $n = 2$ , $\Phi$ contains a sequence $< c_1, c_2 > (1 \leq i \leq n)$ . Now, for all sequences of length equal to $n (n > 2)$ , $\Phi$ contains $< c_1, \ldots, c_n >$ . By definition, $\Phi$ contains $< c_1, \ldots, c_{n-1} >$ and $< c_2, \ldots, c_n >$ . Thus, by the inductive hypothesis, $\Phi$ also contains $< c_i, \ldots, c_j >$ for $1 \leq i < j \leq n$ , as was to be shown.

Example 10. In Example 9, every sequence is inheritable in a designed model base system $\Phi$ , therefore $\Phi$ is closed under inheritance. Since $\Phi$ contains the sequence $<\mathrm{LA}, \mathrm{LP}, \mathrm{IP}, \mathrm{TP}>$ , it also contains the sequence $<\mathrm{LP}, \mathrm{IP}>$ .

Inconsistency can be caused by contradiction of the class inheritance sequences in a model base system. Hence consistency can be defined as an absence of contradiction.

![](/api/attachments/752XGSCH/fulltext/images/d51f6bb1dbf86937dad611638137f04c0954ba820b684edea18aae3afcad4c86.jpg)  
Fig. 5. $\Phi$ is inconsistent.

![](/api/attachments/752XGSCH/fulltext/images/0d582ed16db8f33440cd03a42cc1e5114f690c5212d55d1375d703c0848fee9b.jpg)  
Fig. 6. $\Phi$ is consistent.

Definition 6. A model base system $\Phi$ is consistent if all the sequences in it contradict none of their elements.

Example 11. If a model base system $\Phi$ contains the sequence $< c_{1}, c_{2}, c_{3}, c_{4}, c_{5}>$ , and $< c_{1}, -c_{3} > \in C(\Phi)$ , then $\Phi$ contradicts the sequence $< c_{1}, -c_{3}>$ and is inconsistent. This is shown in Fig. 5.

Example 12. In designing a model base system $\Phi$ for decision models in MS/OR, $\Phi$ contains sequences $<\mathrm{MOLP}, \mathrm{LP}>$ , $<\mathrm{MOLP}, \mathrm{FDM}>$ and $<\mathrm{LP}, \mathrm{LA}>$ , where FDM refers to the fuzzy Delphi model. In its practical semantics, there exists a sequence $<\mathrm{FDM}, -\mathrm{LA}>$ which does not contradict any existing sequences, thus $\Phi$ is consistent. This is shown in Fig. 6.

Two of the main objectives in the design of model base systems are to reduce redundancy and avoid inconsistency. If every class in $\Phi$ is in its simple form and $\Phi$ is closed under inheritance, then $\Phi$ is the resultant model base system.

Example 13. If we are to build a model base system for the subset of decision models in OR/MS, the classes and their inheritance relationships can be depicted as shown in Fig. 7.

![](/api/attachments/752XGSCH/fulltext/images/ea7be6f797d22342bddeb98ef7c30c7e71f55400ae614a81b2e1123c0a163bf0.jpg)  
Fig. 7. A subset of decision models in OR/MS in a model base system.

In Fig. 7, every class is in its simple form, and there is no sequence which contradicts the others. Thus $\Phi$ is consistent and can be treated as the final design for building the model base system.

## 5. Summary

Based on a proposed object-oriented framework for the representation of model base systems, this paper proposes the type rules and inheritance theory for the design of model base systems. Type rules are first used to discover the specialized functions between classes. Inheritance theory is then designed to define formally the relationships among classes in a model base system. They are illustrated with the examples in MS/OR. The proposed object-oriented design method emphasizes the concepts of data abstraction and inheritance, it is to reduce redundancy and avoid inconsistency when designing model base systems.

## Acknowledgements

This research was supported by the 1994 Strategic Research Grant of the City University of Hong Kong (project no. 700-392), 1996 Hong Kong Earmarked Grant for Research (project no. 9040232) and the 1996 Hong Kong Industrial Support Fund (project no. AF/7/96).

## References

[1] R.W. Blanning, Model Management Systems: An Overview, Decision Support Systems 9, pp. 9–18 (1993).

[2] R.W. Blanning, Model Management Systems, in: R.H. Sprague, Jr. and H.J. Watson, Eds., Decision Support Systems: Putting Theory into Practice, pp. 156–169 (Prentice-Hall, 1989).

[3] R. Burslal and B. Lamson, A Kernel Language for ADTs and Modules, in: G. Kahn, Ed., Semantics of Data Types (Springer-Verlag, 1984).

[4] L. Cardelli and P. Wegner, Understanding Types, Data Abstraction and Polymorphism, Computing Survey 17, No. 4, pp. 471–522 (December 1985).

[5] A. Chang, C.W. Holsapple and A.B. Whinston, Model Management Issues and Directions, Decision Support Systems 9, pp. 19–37 (1993).

[6] Y.S. Chen, An Entity-Relationship Approach to Decision Support and Export Systems, Decision Support Systems 4, pp. 225–234 (1988).

[7] D.R. Dolk and B. Konsynski, Knowledge Representation for Model Management Systems, IEEE Transactions on Software Engineering 10, No. 6, pp. 619–628 (1994).

[8] D.R. Dolk, Model Management and Structured Modeling: The Role of an Information Resource Dictionary System, Communication of the ACM 31, No. 6, pp. 704–718 (1988).

[9] S.I. Gass, Decision Making, Models and Algorithms (John Wiley and Sons, Inc., 1985).

[10] M.L. Lenard, An Object-Oriented Approach to Model Management, Decision Support Systems 9, pp. 67–73 (1993).

[11] A. Lloyd, A Practical Introduction to Denotational Semantics (Cambridge University Press, 1986).

[12] J. Ma, An Object-Oriented Framework for Model Management, Decision Support Systems 13, pp. 133–139 (1995).

[13] J. Ma, IRCS: An Inheritance Rule Checking System for Model Management, in: DSS, Journal of Computer and Information Systems 1, No. 1, Special Issues: Proceedings of the 6th International Conference on Computing and Information, pp. 1141–1159 (1994).

[14] J. Mitchell and G. Plotkin, Abstract Types have Existential Type, Proceedings of 12th Annual ACM Symposium on Principles of Programming Languages, New York (1985).

[15] W.A. Muhanna, An Object-Oriented Framework for Model Management and DSS Development, Decision Support Systems 9, pp. 217–229 (1993).

[16] R.H. Sprague, Jr., A Framework for the Development of Decision Support Systems, in: R.H. Sprague, Jr. and H.J. Watson, Eds., Decision Support Systems: Putting Theory into Practice, pp. 7–31 (Prentice-Hall, 1989).

[17] R.E. Trueman, Quantitative Methods for Decision Making in Business (CBC College Publishing, 1981).

[18] V. Wuwongse and J. Ma, An Object-Oriented Approach to Model Management, Advanced Information Systems Engineering, pp. 525–539 (Springer-Verlag, 1991).

Jian Ma is an Assistant Professor in the Department of Information Systems at the City University of Hong Kong. He received his Doctor of Engineering degree in Computer Science from the Asian Institute of Technology in 1991. His current research interests are in the areas of group decision support systems, object-oriented systems and development methodologies for data and model management, and assessment of problem-based learning in engineering and business education. His past research has appeared in Decision Support Systems, Computers and Education and IEEE Transactions on Education.
