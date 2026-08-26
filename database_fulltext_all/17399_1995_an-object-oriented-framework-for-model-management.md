---
otero_id: 17399
otero_key: "JP6QAEN9"
title: "An object-oriented framework for model management"
authors: "Jian Ma"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0036-d"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An object-oriented framework for model management

Jian Ma

School of Computer Science and Engineering, University of New South Wales, Kensington, NSW 2033 Australia

## Abstract

This paper presents a new framework for the conceptual analysis of model management. The framework is object-oriented in the sense that it emphasizes the concepts of data abstraction, information hiding and inheritance. It consists of two parts, namely a conceptual structure for the specification of mathematical decision models and a set of high-level manipulation operators over the conceptual structure. The proposed framework helps to reduce redundancy and avoid inconsistency in the conceptual analysis of model management; as well, it provides a blueprint for building an object-oriented model management system.

Keywords: Decision models; Model management; Object-oriented framework; Operations research

## 1. Introduction

A mathematical decision model is an abstract simple representation of a decision making process, which consists of a set of variables and functions specifying the relationship among these variables $[8]$ . With its wide use in the economy, industry and management, the mathematical decision model has gained acceptance as a kind of information resource that should be efficiently managed in the same way as data. Model management is, then, a methodology for the efficient representation, storage and manipulation of mathematical decision models.

Current research for the conceptual analysis of model management can be classified in the following categories: the relational framework, which views a model as a virtual relation between input and output domains [1]; the entity-relationship approach, which treats a model as an entity comprising a number of attributes, and an interface among entities as a relationship [2,3]; the model abstraction approach, which adopts the concept of data abstraction in programming languages and encapsulates related operations on a common data structure within a model [7]; and the structured modelling method, which employs a hierarchically organized, partitioned, and attributed acyclic graph to represent relationships among model elements (i.e. entities, attributes and functions) [9].

The relational, entity-relationship and model abstraction approaches do not wholly support model sharing, hence redundancy exists and inconsistency is not avoided. Although the structured modelling method specifies the relationship among models in great detail, the resultant graphs do not correspond to real decision models and are thus hard to use and difficult to understand.

The purpose of this paper is to propose an object-oriented framework for the specification of mathematical decision models and the construction of model management systems. The framework consists of two major parts, namely a conceptual structure and a set of manipulation operations. Within the framework, a mathematical decision model is specified in a class which defines relevant functions together on a common data structure, and an inheritance mechanism allows a new class to be specified by making use of the existing ones. The framework is object-oriented in the sense that it emphasizes the concepts of data abstraction, information hiding and inheritance. It separates the specification of a decision model from its implementation and aims at reducing redundancy and avoiding inconsistency in the conceptual analysis of model management.

## 2. Conceptual structure of the framework

For our purposes, a domain is defined as a set of values with certain properties, and type is a synonym for domain used to protect an underlying representation from arbitrary or unintended use. Thus a function f can be defined as a mapping from a domain A to a co-domain B (denoted by f:A → B.) It is a set of pairs $\langle a, b \rangle \in A \times B$ such that if $\langle a, b1 \rangle \in f$ and $\langle a, b2 \rangle \in f$ , then b1 = b2. If $\langle a, b \rangle \in f$ , we write $f(a) = b$ and thus $f = \{\langle a, f(a) \rangle / a \in A\}$ .

This definition of a function differs from the “function” in a programming language where “function” is a rule for transforming an argument to a result.

Functions are widely used in modelling decision-making. Gass [8] claims that any decision model can be abstracted and represented in the form of functions.

EXAMPLE 1: In a production line, the Total Cost (TC) is linearly decided by the Production Volume (PV). If we use f and x to represent TC and PV respectively, the interrelationship between them can be described by:

$$
\mathrm{f} (\mathrm{x}) = \mathrm{a} + \mathrm{bx}\tag{1}
$$

where a and b are constants.

Typed $\lambda$ -calculus is a formal system for the study of functions, their definitions and applications [4,5,11]. It only uses functions to specify a decision model. Thus there are no side effects of passing values between functions [5] and the resultant model specification can be implemented easily using a functional programming language such as ML [15]. In this paper, typed $\lambda$ -calculus is used as a formal language to specify functions in the framework.

The basic typed $\lambda$ -calculus has the syntax:

$$
\begin{array}{l l} \mathrm {e:: = e(e)} & / ^ {*} \text {application} \\ \lambda \mathrm{x:} \tau . \mathrm {e(x):} \tau & / ^ {*} \text {abstraction} \\ \mathrm{x:} \tau & / ^ {*} \text {typed variable} \\ \mathrm{c:} \tau & / ^ {*} \text {typed constant} \end{array}\tag{2}
$$

where $\tau$ is a type with the syntax:

$$
\begin{array}{r l}\tau : :=&\text { INTEGER / BOOLEAN / CHARACTER }\\&/ \text { REAL } /\\&/ \dots / \tau \times \tau / \tau \rightarrow \tau / (\tau).\end{array}\tag {1}\tag{3}
$$

Typed expression (abbreviated as expression, thereafter) e is a typed function used to represent basic operations in a decision model. For simplicity, we use $f:\tau\to\tau$ ; $f=\lambda x.e(x)$ to represent function abstraction $f=\lambda x:\tau.e(x):\tau$ . As a shorthand, we also allow $e'$ where $x:\tau=e$ to represent function abstraction $\lambda x:\tau.(e')(e)$ .

In its purest form, typed $\lambda$ -calculus does not have built-in functions (e.g., +) and composite types (e.g., ARRAY). But as our intentions are practical, we extend the typed $\lambda$ -calculus to support arithmetical operations on array type, i.e., $A^{-1}$ , $A^{T}$ and $A + B$ stands for the inversion, transposition and addition of the matrixs respectively.

EXAMPLE 2: In Equation 1, x is a variable; $a + bx$ is an expression in which x is free, and must either be defined globally in the expression or be undefined:

$$
\begin{array}{c} \text { f:REAL } \to \text { REAL }; \\ f = \lambda x. (a + b x) \end{array}\tag{4}
$$

where x is bounded by the $\lambda x$ with type REAL and $\lambda x.(a + bx)$ is an abstraction with type REAL.

In order to allow various users to use decision models conveniently, their relevant functions should be specified together on a common data structure. This ensures the quality of decision model specification. In the literature of object-orientation [4,5], record structure has been used to specify the concepts of data abstraction and information hiding, where each field is a function abstraction. We modify this concept to suit the requirements of model management.

DEFINITION 1: A class is a conceptual schema specifying a decision model. Based on a set of common data structures, it groups relevant expressions together in a fixed set:

$$
\mathrm{C} = \left\{e _ {1}, e _ {2}, \dots , e _ {n} \right\};\tag{5}
$$

where C is the global name of the class and each $e_i (1 \leqslant i \leqslant n)$ is an expression local to C.

Within a class, expressions are unordered and not duplicated due to the fact that a class corresponds to a set [14]. A class allows a mathematical decision model to be specified by a set of abstract functions. It emphasizes the essential characteristics while suppressing implementation details. Hence it enhances modularity and reduces coupling by keeping the specification simple and limiting unintended interactions. Class is the realization of data abstraction and information hiding concepts.

EXAMPLE 3: Linear programming (LP) [8] is a basic decision model in operations research or management science (OR/MS), where the simplex method algorithm is commonly used to compute the optimal solutions. Sensitivity analysis is then performed. If we use GOAL representing the function to perform the simplex method algorithm, SOLUTIONs to display solution reports and RANGE to do the sensitivity analysis, then the LP model is specified in the following class schema:

$$
\begin{array}{l}\text {c:} R _ {n};\\\quad / ^ {*} \text {coefficient vector c}\\\text {A:} R _ {n} ^ {n};\\\quad / ^ {*} \text {constraint matrix A}\\\text {b:} R _ {n};\\\quad / ^ {*} \text {resource vector b}\\\text {GOAL:} R _ {n} \rightarrow \text {REAL};\\\quad \text {GOAL = MIN \{c^T* where X:R_n =}\\\quad A ^ {- 1};;\end{array}
$$

$$
\begin{array}{l}\text {/* use simplex method algorithm}\\\text {to solve the problem}\\\text {SOLUTIONs: R_{n}};\\\text {SOLUTIONs = X;}\\\text {/* print standard solution report}\\\text {RANGE: R_{n} \rightarrow R_{n}};\\\text {RANGE = \lambda X.X^{*} A^{-1} b)}\\\text {/* to test the range of X, while}\\\text {still keep the optimal result}\\\};\end{array}
$$

where c, A and b are the cost coefficient vector, constraint matrix and resource vector respectively. The vectors have a n-ary REAL type $R_{n}$ and the matrix $n \times n$ -ary REAL type $R_{n}^{n}$ .

In this object-oriented framework, a class schema specifies a mathematical decision model, but its instance is represented by an object.

DEFINITION 2: An object is an instance of a class, denoting a special case of the model class. Being defined, it uses all the functions in that class. Formally, if an object O is an instance of class C, it is denoted by O:C.

EXAMPLE 4: To determine what is the best yield obtainable from investing one million US\$ in projects AA and/or BB is an object, INVEST, belonging to class LP. Object INVEST is specified by INVEST:LP. It uses all functions defined in class LP, e.g. INVEST.GOAL, to execute the simplex method algorithm in order to get optimal solutions.

In model management, incremental modification is a technique to compose a modifying function with an existing one by the operator “ $\odot$ ”. In typed $\lambda$ -calculus, it is represented by:

$$
\mathrm{sc} = \lambda \mathrm{p}, \lambda \mathrm{x}. \mathrm{m} \odot \mathrm{p} (\mathrm{x}) = \lambda \mathrm{p}, \lambda \mathrm{x}. \mathrm{m} (\mathrm{p} (\mathrm{x}))\tag{6}
$$

where sc, p and m are new, existing and modifying functions respectively. If $\mathrm{p}(\mathrm{x})$ has function type $\tau \rightarrow \tau$ , sc must have the composite function type $(\tau \rightarrow \tau) \rightarrow \tau$ .

In some cases, m may be the identity function, i.e. $m = \lambda y.y$ , resulting in sc being the same as p. In other words, sc is a direct copy of p. However, in most cases, m is an expression acting on the values returned by p.

DEFINITION 3: If some expressions in a class $C' = \{e_{1}', e_{2}', \ldots, e_{m}'\}$ are either direct copies or incremental modifications of the corresponding expressions in a class $C = \{e_{1}, e_{2}, \ldots, e_{n}\} (m \geqslant n)$ , then $C'$ is a subclass of C and C is a superclass of $C'$ .

DEFINITION 4: Inheritance is a mechanism to allow a new class to be defined by inheriting function properties from existing ones. Formally, if $\mathbf{C}' = \{\mathbf{e}_1', \mathbf{e}_2', \ldots, \mathbf{e}_m'\}$ is a subclass of a set of classes $\{\mathbf{C}_1, \mathbf{C}_2, \ldots, \mathbf{C}_n\}$ (where $\mathbf{C}_i = (\mathbf{e}_{i1}, \mathbf{e}_{i2}, \ldots, \mathbf{e}_{ir_i}\}$ , for any $i$ in $1 \leqslant i \leqslant n$ ), then it can be denoted by:

$$
\mathbf {C} ^ {\prime} = \left\{\mathrm{e} _ {j 1} ^ {\prime}, \mathrm{e} _ {j 2} ^ {\prime}, \dots , \mathrm{e} _ {j k} ^ {\prime} \right\}
$$

$$
\text { inherit   from } \mathrm{C} _ {1}, \dots , \mathrm{C} _ {\mathrm{n}};\tag{7}
$$

where each $e_{jl}^{\prime}$ ( $1 \leqslant jl \leqslant m$ ) is either an incremental modification of the corresponding expression in class Ci ( $1 \leqslant i \leqslant n$ ) or an expression which never appears in its superclasses.

In this paper, every expression is defined to be local to a class. Therefore, the same expression name may appear in more than one class. In order to avoid this ambiguity in the inheritance case, the expression name should be explicitly distinguished by concatenating the class name with “.” and the expression (e.g. C.e) when necessary.

EXAMPLE 5: In the multi-objective linear programming model (MOLP), each objective function has a weight. One possible approach to determine the weights for each objective function is to use the fuzzy delphi mathematics (FDM) method, which can be implemented in the class FDM below.

$$
\begin{array}{l l} \text { FDM } = \{\quad & \text { Rwt }: R _ {n} ^ {m}; \\ & \quad / ^ {*} \text { m } \times \text { n - ary   real   matrix   of   the } \\ & \quad \text { raw   weights } \\ & \text { W }: R _ {n} ^ {m} \to R _ {n}; \\ & \quad \text { W } = \lambda R w t. ((\sum_ {j = 1} ^ {m} R w t _ {i j}) / m); \\ & \quad / ^ {*} \text { evaluate   proper   weights   for } \\ & \quad \text { each   objective   function } \\ & \}; \end{array}
$$

where Rwt is a matrix storing raw weights and W is a function to evaluate raw weights for different objective functions.

With the proper weights for corresponding objective functions, MOLP model can then be specified in the class MOLP:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
MOLP = {b:R$_{n}$;
A:R$_{n}^{m}$;
cc:R$_{n}^{m}$;
Rwt:R$_{n}^{m}$;
W = λRwt.((Σ$_{j=1}^{m}$Rwt$_{ij}$)/m);
wc:R$_{n}$ × R$_{n}^{m}$ → R$_{n}$;
wc = λW,λcc.(W$^{T}$C);
/* to combine the weight with each
objective function
GOAL:R$_{n}$ → REAL;
GOAL = MIN {wc$^{T}$ where X:R$_{n}$ =
A$^{-1}$;;
/* use simplex method algorithm to
solve the problem
SOLUTIONs:R$_{n}$;
SOLUTIONs = X;
/* print standard solution report
RANGE:R$_{n}$ → R$_{n}$;
RANGE = λX.(X * A$^{-1}$* b);
/* to test the range of X, while still
keep the optimal result
},
</div>

where b, A, GOAL, SOLUTIONs and RANGE are direct copies of corresponding expressions in class LP. Rwt and W are direct copies of the expressions from class FDM. cc and wc are new functions to input cost coefficient matrix and to assign weights to the corresponding cost coefficient vectors respectively. Hence class MOLP can be abbreviated by specifying it to inherit function properties from class LP and FDM:

$$
\begin{array}{l l} \text {MOLP = \{\quad cc: R _ {m} ^ {n} ;} \\ \text {wc: R _ {m} \times R _ {n} ^ {m} \to R _ {n} ;} \\ \text {wc = \lambda W, \lambda cc.(W^{\mathrm{T}} C);} \\ \text {/* combine the weight} \\ \text {with each objective function} \end{array}
$$

Inheritance specifies the relationship for the reuse of decision models, which helps to reduce redundancy and avoid inconsistency among classes, hence it improves the quality of class schema. Class and inheritance together constitute the object-oriented framework for the conceptual specification of mathematical decision models in model management.

## 3. Manipulation operations of the framework

The proposed object-oriented framework is a conceptual framework for the representation of mathematical decision models. In order to allow users to manipulate the classes at an abstract level, while neglecting detailed implementation of functions within classes, and to provide an efficient minimum subset of the language that can express enough things to make a model management system useful, a set of high-level manipulation operations for the framework needs to be defined.

It will be recalled that a class is a conceptual schema specifying a mathematical decision model, which defines relevant expressions together on a common set of data structures in a fixed set. An inheritance mechanism then allows a new class to be defined by making use of existing function properties from superclasses. As a result, the relationships among classes in a model base system can be well represented in a directed graph data structure. Therefore, the manipulation operations for the object-oriented framework should include three parts, namely:

```txt
class ::= class-name = { expr-list } [inherit-from class-name]
oprt ::= find / project / insert / delete / modify / infix-op
find ::= FIND target-list WHERE condition
target-list ::= class-name / expr-list
project ::= PROJECT class-name WITH expr-list
insert ::= INSERT class-name WITH expr-list
delete ::= DELETE class-name
modify ::= MODIFY expr WITH expr IN class-name
expr-list ::= expr / expr-list, expr
expr ::= ename : type
class ::= class infix-op class
infix-op ::= UNION / INTERSECT / DIFFERENCE
condition ::= condition op condition / class-name cmp-op constant / ename cmp-op constant / type cmp-op constant
cmp-op ::= < / ≤ / = / > / ≥
op ::= AND / OR / NOT
class-name ::= string
ename ::= string
```  
Fig. 1. A BNF grammar for manipulation operations in the object-oriented framework.

<table><tr><td>Manipulation operation commands</td><td>Results</td></tr><tr><td>FIND class-name WHERE ename=&#x27;GOAL&#x27;</td><td>class-namesLPIPMOLP</td></tr><tr><td>FIND class-name WHERE cname=&#x27;GOAL&#x27;AND type=(&#x27; $R_n^n \times R_n \to R_n$ )→ REAL&#x27;</td><td>class-namesLP</td></tr><tr><td>FIND expr-list WHERE class-name=&#x27;FDM&#x27;</td><td>expr-listRwt: $R_n^m$ ;W: $R_n^m \to R_n$ </td></tr></table>

Fig. 2. Examples of FIND operations.

(1) the traditional set operations: UNION, INTERSECTION and DIFFERENCE. They are defined in the usual manner.

(2) the special operations: FIND, PROJECT, and

(3) the update operations: INSERT, DELETE and MODIFY.

Operations in part (2) and (3) are defined as follows:

FIND: to select class names or expression lists in a model management system, whenever some conditions are met;

FIND target-list WHERE condition.

PROJECT: to form a new class with the extracts of expressions from a specified class;

PROJECT class-name WITH expr-list.

INSERT: to create a new class in a model management system;

INSERT class-name WITH expr-list.

DELETE: to delete a specified class in a model management system;

DELETE class-name.

MODIFY: to update the expressions in a specified class;

MODIFY expr WITH expr IN classname. The syntax of the manipulation operations can be defined as shown in Fig.1.

Retrieval is one of the most important functions of high level manipulation operations to the object-oriented framework. If we suppose defined classes of OR/MS exist in the conceptual analysis of model management, some examples of FIND are given in Fig.2.

The FIND operation as just defined permits only a simple comparison in the WHERE clause. However, it is possible to extend the definition by allowing the predicate to consist of an arbitrary Boolean combination of such simple comparisons, as is indicated by the following equivalents:

1. FIND expr-list WHERE condition1 AND condition2 is defined to be equivalent to

(FIND expr-list WHERE condition1) INTERSECT (FIND expr-list WHERE condition2).

2. FIND expr-list WHERE condition1 OR condition2 is defined to be equivalent to

(FIND expr-list WHERE condition1) UNION (FIND expr-list WHERE condition2).

3. FIND expr-list WHERE NOT condition is defined to be equivalent to

expr-list DIFFERENCE (FIND expr-list WHERE condition).

Henceforth we assume that the predicate in the WHERE clause of a FIND consists of such an arbitrary Boolean combination of simple comparisons. Such a predicate is said to be a restriction predicate; and the FIND operation is referred to as a restriction operation.

The implementation of manipulation operations depends on the data structure for the representation of the object-oriented framework. Detailed discussions for the implementation of object-oriented model management systems can be found in [14].

To summarize, the proposed operations are high level operations designed for the retrieval, update and access of model classes in a model management system. A commercial model management system may include many other operations for a user friendly interface, but the designed grammar rules can meet the minimum requirements for manipulation operations in designing an object-oriented model management system.

## 4. Conclusions

An object-oriented framework has been proposed for the conceptual analysis of model management. It consists of two major parts: a conceptual structure, within which a mathematical decision model is specified as a class and an inheritance mechanism allows a new class to be built by making use of function properties from existing classes; and the manipulation operations over the conceptual structure, which are high-level manipulation operators for the retrieval, update and access of classes in designing a model management system.

The framework helps to reduce redundancy and avoid inconsistency in the conceptual analysis of model management; it also provides a blueprint for building a model management system.

## References

[1] R.W. Blanning, Model Management Systems, in: R.H. Sprague, JR and H.J. Watson Eds., Decision Support Systems: putting theory into practice, 2nd edition, (Prentice-Hall, Inc., 1988), 156–169.

[2] R.W. Blanning, An Entity-Relationship Approach to Model Management, Decision Support Systems 2, (1986), 65–72.

[3] Y.S. Chen, An Entity-Relationship Approach to Decision Support and Expert Systems, Decision Support Systems 3, (1988), 365–377.

[4] W. Cook and J. Palsberg, A Denotational Semantics of Inheritance and its Correctness, Proceedings of ACM Conference on Object-Oriented Programming Systems, Languages and Applications, (1989), 433–443.

[5] L. Cardelli and P. Wegner, On Understanding Types, Data Abstraction, an Polymorphism, Computing Surveys 17, 4, (1985), 471–522.

[6] S. Danforth and C. Tomlinson, Type Theories and Object-Oriented Programming, ACM Computing Survey 20, 1, (1988), 29–72.

[7] D.R. Dolk, Data as Models: An Approach to Implementing Model Management, Decision Support Systems 2, (1986), 73–80.

[8] S.I. Gass, Decision Making, Models and Algorithms (John Willey and Sons, Inc., 1985).

[9] A.M. Geoferion, An Introduction to Structured Modelling, Management Science 33, 5, (1987), 547–588.

[10] T.P. Liang, Integrating Model Management with Data Management in Decision Support Systems, Decision Support Systems 1, (1985), 221–232.

[11] L. Allison, A Practical Introduction to Denotational Semantics (Cambridge University Press, 1986).

[12] P.C. Lockeman, Object-Oriented Information Management, Decision Support Systems 5, (1989), 79–102.

[13] B. Meyer, Object-Oriented Software Construction (Prentice Hall, Inc., 1988).

[14] J. Ma, An Object-Oriented Approach to Model Management (D.Eng. Dissertation, Asian Institute of Technology, Bangkok, Thailand, 1991).

[15] R. Miller, A Proposal for Standard ML, Proceedings of the Symposium on LISP and Functional Programming (ACM, New York, 1984), 184–197.

![](/api/attachments/JP6QAEN9/fulltext/images/271c8b9aea04ceb2a1d45fc69459154f0840abef0f0d47dc878b81c94b74c72a.jpg)

Jian Ma is a lecturer in the School of Computer Science and Engineering at the University of New South Wales. He received his Doctor of Engineering degree in computer science from Asian Institute of Technology in 1991. His current research interests include object-oriented systems and development methodologies for data management and model management.
