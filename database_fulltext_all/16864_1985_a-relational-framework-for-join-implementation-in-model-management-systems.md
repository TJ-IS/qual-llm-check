---
otero_id: 16864
otero_key: "US9GC9WC"
title: "A relational framework for join implementation in model management systems"
authors: "Robert W Blanning"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90198-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Relational Framework for Join Implementation in Model Management Systems

Robert W. BLANNING

Owen Graduate School of Management, Vanderbilt University, Nashville, TN 37203, USA

Two important issues in the design of relational model banks are the degree to which they should be aggregated or disaggregated and the methods by which disaggregated model banks might be integrated in response to user queries. Three topics relevant to this issue are addressed in this paper. The first is whether a universal model and its projections may possess the lossy join property. We will show that they do not. The second is the development of a relational algebra for the specification of join implementation in model banks, and the third is the realization of such an algebra in a language similar to Query-by-Example.

Keywords: Model Management; Model Bank; Virtual Relation; Relational Projection; Relational Join; Functional Dependency; Lossy Join; Fixed Point; Relational Algorithms; Relational Language; Table Skeleton; Information Management.

![](/api/attachments/US9GC9WC/fulltext/images/b1de2d8e9cff1c0b4be31ffa2b8dc2d5756b59e0c30d6d42b2ec7fcb789963ab.jpg)

Robert W. Blanning is Associate Professor of Management at the Owen Graduate School of Management at Vanderbilt University. He holds a B.S. in Physics from the Pennsylvania State University, an M.S. in Operations Research from the Case Institute of Technology, and a Ph.D. from the University of Pennsylvania, specializing in Operations Research and Management Information Systems. His teaching and research interests are in information economics, model management systems, and expert systems for management, and he has published in Management Science, Decision Sciences, Naval Research Logistics Quarterly, Omega, Technological Forecasting and Social Change, and Long Range Planning.

## 1. Introduction

The field of DSS arose because of a widespread feeling that the established fields of management information systems and management science had emphasized structured management problems at the expense of semistructured and ill-structured ones [Carlson, 1977; Keen and Scott Morton, 1978; Keen and Wagner, 1979; Alter, 1980]. From an early concern about the emphasis on structured problems in systems design, the field has grown enormously; it now includes people working in artificial intelligence, model management, information economics, and individual and group behavior [Blanning, 1983b]. The published research in the field, as reflected for example in several recent collections of papers on DSS [Fick and Sprague, 1980; Ginzberg, Reitman, and Stohr, 1982; Bennett, 1983; House, 1983; Sol, 1983] presents a variety of approaches taken by workers in the field in an attempt to develop systems that help managers and analysts to solve problems that are not fully structured.

An important component of the literature on DSS is the literature on model management systems [Sprague and Watson, 1975; Will, 1975; Bonczek, Holsapple and Whinston, 1980b; Sprague, 1980; Sprague and Carlson, 1980; Konsynski, 1981, 1983]. A model management system is a software system that insulates its users from the physical aspects of model bank organization and processing, just as a database management system insulates its users from the physical aspects of database organization and processing. Thus, a model management system makes it easy for a user to assemble information from a variety of sources and thus, allows the user more flexibility in identifying and solving problems. Although there are at present no commercially available model management systems, it has been suggested that the systems that support financial planning languages, such as EMPIRE and IFPS [Naylor and Mann, 1982], are the forerunners of model management systems to come, just as the file processing systems of the 1950's and 1960's were the forerunners of the database management systems of the 1970's and 1980's.

There are three components of the model management literature. The first concerns the use of artificial intelligence techniques to determine how models and data files should be integrated in response to a user query [Bonczek, Holsapple and Whinston, 1980a, 1981a]. The principal techniques studied to date are AND/OR graphs that describe the conditions under which certain consequences of interest will occur [Bonczek, Holsapple and Whinston, 1979b, 1977] and the application of the resolution principle to analyze queries expressed in the first order predicate calculus [Bonczek, Holsapple and Whinston, 1981b, 1979a; Schell, 1983], and the use of semantic nets [Elam, Henderson, and Miller 1980], connection graphs [Chen, Fedorowicz, and Henschen, 1982], and frames [Dolk and Konsynski, 1982]. The second component is based on the CODASYL framework for data base systems. It is suggested that the CODASYL framework may be used not only to interface models with data bases, but also to describe some of the characteristics of the models themselves [Stohr and Tanniru, 1980; Konsynski and Dolk, 1982]. The third component of the model management literature, the one of interest here, is a relational component. It is suggested that a model may be viewed as a subset of the Cartesian product of a set of domains corresponding to its input and output attributes, just as a file is viewed in relational database theory as a subset of the Cartesian product of a set of domains corresponding to key and content attributes [Blanning, 1981a, 1982d, 1983c].

This paper is concerned with relational model management and its role in DSS. There are three components of the relational model management literature, which correspond to three major areas of research in relational data management. The first is the organization of relational model banks and specifically, the identification of normal forms based on anomalies that can arise in model execution [Blanning, 1982b]. The second is the identification of criteria for relational completeness of model query languages and the investigation of the properties of a relationally complete model query language [Blanning, 1983a, 1984]. The third is the implementation of joins. A join must be implemented in relational model management whenever more than one model is needed to respond to a user query and an input attribute of one or more of the models is an output attribute of one or more of the others. For example, the output of a market forecasting model may be an input to a distribution planning model, whose output in turn may be an input to a production scheduling model.

The subject of this paper is the last of these problems – the implementation of joins in relational model banks. In the following sections we examine three aspects of join implementation. The first is the possible existence of lossy joins [Aho, Beeri and Ullman, 1979; Ullman, 1980]. We will show that for all practical purposes, lossy joins do not arise in relational model management. The second is the development of an algebraic framework for implementing joins, based on Sanderson's [1980] relational framework for algorithms. The third aspect is the development, but not yet the implementation, of a language similar to Query-by-Example [Zloof, 1975] for specifying the way in which joins are to be implemented – that is, for specifying algorithms for finding fixed points.

The need to find a fixed points results from the fact that there may be cycles in the model set – for example, the output of one model may be the input to another model, and vice versa. To find a consistent solution for the model set a model management system must remove one or more of the input/output attributes and use an appropriate fixed point algorithm to find values for these attributes such that their posited input values are nearly equal, within preassigned limits, to their calculated output values [Blanning, 1982d]. In Section 4 we present a language whose purpose is to allow the user to specify both the attributes to be removed and the algorithm for finding the fixed point.

## 2. The Lossy Join Problem

The lossy join property and its complement, the lossless join property, are characteristics one of which will apply whenever a single relation is projected into two or more relations, presumably for the purpose of ensuring that the data base is in a normal form that eliminates certain update anomalies [Date, 1977; Ullman, 1980]. The properties obtain when information is lost (lossy join) or is not lost (lossless join) after the projection has taken place [Aho, Beeri and Ullman, 1979; Ullman, 1980]. It is clear that a lossy join will occur whenever one or more of the attributes in the original relation do not appear among the attributes of the projected relations, because information about that attribute would then be lost. A more subtle type of lossy join arises when no attributes are lost but the joining of the projections across their common attributes does not recover the original relation.

Consider the ‘universal’ relation

<table><tr><td>University</td><td>City</td><td>State</td></tr><tr><td>Vanderbilt</td><td>Nashville</td><td>TN</td></tr><tr><td>UT</td><td>Knoxville</td><td>TN</td></tr></table>

and its projection into the relations:

<table><tr><td>University</td><td>State</td><td>City</td><td>State</td></tr><tr><td>Vanderbilt</td><td>TN</td><td>Nashville</td><td>TN</td></tr><tr><td>UT</td><td>TN</td><td>Knoxville</td><td>TN</td></tr></table>

The join of these two projections is:

<table><tr><td>University</td><td>City</td><td>State</td></tr><tr><td>Vanderbilt</td><td>Nashville</td><td>TN</td></tr><tr><td>Vanderbilt</td><td>Knoxville</td><td>TN</td></tr><tr><td>UT</td><td>Nashville</td><td>TN</td></tr><tr><td>UT</td><td>Knoxville</td><td>TN</td></tr></table>

By performing the projections we have lost information about which university is in which city. Hence, the universal relation and it two projections possess the lossy join property. On the other hand, if we were to project the relation as follows:

<table><tr><td>University</td><td>City</td><td>City</td><td>State</td></tr><tr><td>Vanderbilt</td><td>Nashville</td><td>Nashville</td><td>TN</td></tr><tr><td>UT</td><td>Knoxville</td><td>Knoxville</td><td>TN</td></tr></table>

then the join would be lossless, for it would recover the original relation.

Whether the lossy or lossless join properties obtain in relational model management is in part a semantic question, because model tuples (as opposed to data tuples) do not exist in stored form. However, we will demonstrate several results that suggest that the model management analogue of the lossy join property does not exist. These results follow from one fundamental assumption: in projecting a universal model, output attributes are pairwise disjoint. For example, if one of the projections calculates net income, then that attribute cannot be calculated by any other projection: there can be only one net income. In the following, we will use X; Y, J, K and L to denote nonempty partwise disjoint sets of attributes. Any joins will be across the attribute sets J, K and L.

We begin by examining the case in which a universal relation is projected into two relations such that the input attributes of all three relations are identical and the output attributes of the projections are the result of a partitioning of the outputs of universal relation. For example, the input (J) to the universal model may be the investment policy of a firm and the output may be the future costs (X) and revenues (Y) resulting from the policy. Thus, the join is across the inputs of the projections. That the join is lossless in this case is demonstrated in:

## Theorem I

Consider the relation $U = \langle J, X, Y \rangle$ with functional dependency $J \to XY$ and its projections $R = \langle J, X \rangle$ and $S = \langle J, Y \rangle$ . Then $U, R$ , and $S$ possess the lossless join property. (See Appendix I.)

The lossless join property also obtains when the output of one of the relations is the input to the other relation. For example, a set of sale prices for various products (X) may be used to calculate the resulting sales volumes for the products (J), which are then used to calculate the production capacity needed to meet demand (Y). That the join is lossless in this case is demonstrated in:

## Theorem II

Consider the relation $U = \langle X, J, Y \rangle$ with functional dependencies $X \to J$ and $J \to Y$ and its projections $R = \langle X, J \rangle$ and $S = \langle J, Y \rangle$ . Then $U, R$ , and $S$ possess the lossless join property. (See Appendix II.)

The conditions described above do not apply when some of the inputs of each of the projections are contained in the outputs of the other projection. Consider, for example, an econometric demand model that calculates volume sold (possibly for several products in several regions) as a function of price and a supply model that calculates the supply prices as a function of demand; the problem is to find a consistent set of prices and volumes [Hogan, 1975; Ahn and Hogan, 1982]. That the lossy join problem does not arise in this case is demonstrated in:

## Theorem III

Consider the relation $U = \langle J, K, L, X, Y \rangle$ with functional dependencies $JK \to LX$ and $JL \to KY$ and its projections $R = \langle J, K, L, X \rangle$ and $S = \langle J, L, K, Y \rangle$ . Then U, R, and S possess the lossless join property. (See Appendix III.)

In this case K and L correspond to the price and volume of the above example, J is an input to the universal model, and X and Y are additional outputs. Although the lossy join problem does not arise here, there is another problem that can arise – that of nondeterminism with respect to the only exogenous attributes, those in the attribute set J. That is, a single value of J may result in more than one set of values of K, L, X, and Y for which the functional dependencies $JK \rightarrow LX$ and $JL \rightarrow KY$ obtain. On the other hand, there may be no values satisfying the functional dependencies. In that case the system would be inconsistent and therefore, would be trivially deterministic, because the universal relation and its projections would contain no tuples. Thus, the pairwise disjoint character of the output attributes of projected models does not guarantee consistency or determinism, it merely guarantees that if either inconsistency or nondeterminism should arise in the universal model, that property will also arise in the join of the projections, and vice versa. These problems are examined in detail in [Blanning, 1982c], and will not be examined here.

Thus, from a description of a universal model and its projections that appears to describe the real world of model management one can conclude that the lossy join problem does not arise. Because of this, in relational model management joins are transparent to the user and can be implemented by a model management system. This does not relieve the user of all responsibility with regard to joins, for the user may need to specify two aspects of the join implementation process. These two aspects and a relational algebra for their specification are examined below.

## 3. A Relational Algebra for Join Implementation

We begin by defining a model set as a set of models that are needed to respond to a specific query. The name, inputs, and outputs of each model must be defined in a model definition language (MDL) and the models in the model set must be specified in a model set specification language (MSSL) [Blanning, 1982c]. An example of a model set, which we will name CORP, appears in Fig. 1. The models in CORP are as follows:

![](/api/attachments/US9GC9WC/fulltext/images/61640f1ff4f63b48017bf4e074f4df64ee51aa3640043079d77a942dc8151edd.jpg)  
Fig. 1. The Model Set CORP.

1. A financial model (FIN) whose inputs are a sale price $(P)$ , a sales volume $(V)$ , and an expense $(E)$ and whose output is net income $(N)$ ;

2. A manufacturing model (MFG) whose input is V and a unit cost (U) and whose output is E;

3. A pricing model (PRI) whose input is V, E, and a price markup (M) and whose output is P;

4. A market model (MKT) whose input is P and whose output is V.

A numerical example of CORP describing the contents of the models and the resulting joins based on [Blanning, 1982c] will be demonstrated below. We first examine the two aspects of join implementation (discussed below) that the user may need to specify.

If a model set contains one or more cycles, a set of arcs, called a stationary set, must be removed so that no cycles remain and a fixed point must be found for the stationary set. The stationary set for CORP may be either P or V. (Removing E will break one of the cycles but not both of them.) For example, if P is removed, then a proposed value of P is entered into MKT, the resulting value of V is calculated, the value of V is entered into MFG, and the resulting value of E along with V are entered into PRI to give an outputted value of P. The two values of P are compared, and if they are not within a specified tolerance, a new value of P is proposed and the process repeated. Sophisticated algorithms for finding fixed points that converge in a variety of cases have been developed [Klein, 1973, ch. 7; Scarf, 1973; Filius, 1979], but it has been found that simple rules often converge rapidly [Hogan, 1975; Ahn and Hogan, 1982]. We note that this process is parameterized over the inputs U and M; that is, U and M are first entered into MFG and PRI, and the fixed point will depend on the values of these two attributes. Once a fixed point is found, FIN is executed to find the value of N.

If the model set does not contain any cycles, implementation of joins is straightforward. This was the case with the projected models described in the previous section. In Theorem I the two projections had common inputs, and join implementation consisted only of duplicating the input to the model set for entry into both models. In Theorem II the output of the first model was the input to the second, and join implementation consisted of transferring the output of the first model to the input to the second model. On the other hand, the projected models in Theorem III, like the models in CORP, contain a cycle. (CORP has two cycles – one involving PRI and MKT, and the other involving PRI, MKT, AND MFG.)

A model set is acyclic (i.e., contains no cycles) if it is partially ordered. Let $m_{1}\ldots m_{n}$ be the models in the set and let $\leqslant$ be the ordering relation such that $m_{i} \leqslant m_{j}$ whenever there is a chain of models ordered by their output–input attributes leading from $m_{i}$ to $m_{j}$ . For example, in CORP we have MFG $\leqslant$ MKT with PRI as the link in the chain, but we do not have FIN $\leqslant$ MFG. A model set M is partially ordered if for all $m_{i}, m_{j}, m_{k} \in M$ we have (1) $m_{i} \leqslant m_{i}$ , (2) if $m_{i} \leqslant m_{k}$ , and $m_{i} \leqslant m_{k}$ we have $m_{i} \leqslant m_{k}$ , and (3) if $m_{i} \leqslant m_{j}$ and $m_{j} \leqslant m_{i}$ then $m_{i} = m_{j}$ [Klein, 1973, ch. 3]. The model set CORP is not partially ordered because PRI $\leqslant$ MKT and MKT $\leqslant$ PRI, but PRI $\neq$ MKT. Methods have been developed for determining whether a set is partially ordered and one of these is applied to a model set similar to CORP in [Blanning, 1982d].

There are two aspects of the join process that a user may need to specify: the attributes in the stationary set and the algorithm that will be used to find the fixed point. In this section we present a relational algebra for specifying the arcs to be removed and the algorithm. This is based on Sanderson's [1980] relational framework for algorithm specification, which is summarized in the following two paragraphs.

Sanderson begins by presenting a primitive concept, a base set S, and defining a relator (or binary relation) as a subset of $S \otimes S$ . If A is a relator, we say that xAy if the tuple $\langle x, y \rangle$ is a member of A. This leads to the following definitions:

(1) A relator $A$ is deterministic if $\forall xyz(((xAy)\land (xAz))\Rightarrow (y = z))$ . Thus, a deterministic relator is a mapping from the first elements of its tuples to the second elements of its tuples.

(2) The identity relator $I$ is defined by $\forall xy((xIy) \Leftrightarrow (x = y))$ , the null relator $Z$ is defined by $\forall xy(\sim xZy)$ , and if there exist two elements $t$ and $f$ (denoting true and false) in $S$ , the true relator $T$ is defined by $\forall x(xTt)$ and the false relator $F$ is defined by $\forall x(xFf)$ .

(3) The composition $A \circ B$ of two relators $A$ and $B$ is a relator defined by $\forall xy((x(X \circ B)y) \Rightarrow \exists z((xAz) \land (zBy)))$ .

(4) For any $n \geqslant 0$ , the $n$ -th power of a relator $A$ is a relator defined by $A^{\circ} = I$ , $A^{1} = A$ , $A^{n+1} = A \circ A^{n}$ .

(5) The extension $A^*$ of a relator $A$ is defined by $\forall xy((xA^*y) \Leftrightarrow \exists n(xA^n y))$

(6) Consider a relator $P$ such that $\forall x((xPt) \vee (xPf))$ . We define three operators:

(a) If-then-else(P↑A/B): ∀xy((x(P↑A/B)y) ⇔ (((xPt) ∧ (xAy)) ∨ ((xPf) ∧ (xBy))))).

(b) While-do $(P?A): x_1(P?A)x_N$ if there is a sequence $x_1 \ldots x_N$ such that both $x_iPt$ and $x_iAx_{i+1}$ for $i = 1 \ldots N - 1$ and $x_NPf$ .

(c) Repeat-until $(A!P)$ : $x_{1}(A!P)x_{N}$ if there is a sequence $x_{1}\ldots x_{N}$ such that both $x_{i}Pf$ and $x_{i}\mathrm{iAx}_{i + 1}$ for $i = 1\dots N - 1$ and $x_{N}Pt$ .

These definitions lead to the following results:

(1) $I, Z, T$ , and $F$ are deterministic,

(2) If $A, B$ , and $P$ are deterministic, then the following are also deterministic: $A \circ B$ , $A^n$ (for any $n > 0$ ), $P \uparrow A / B$ , $P?A$ , and $P!A$ ,

(3) The While-Do and Repeat-Until operations can be defined (recursively) in terms of the elementary operations:

(a) $P?A = (P\uparrow A / Z)^{*}\circ (P\uparrow Z / I);$

(b) $A!P = A\circ ((P\uparrow F / T)?A),$

(4) If $P$ and $A$ are deterministic, then there is exactly one sequence of the form $x_{1} \ldots x_{N}$ for any $x_{1}(P?A)x_{N}$ and exactly one such sequence for any $x_{1}(A!P)x_{N}$ that satisfy the requirements of Definition 6 above.

We now develop a relational framework for specifying the implementation of joins. This framework need be used only if the transitive closure of the model set, as ordered by the input/output attributes of the models, is not partially ordered. (It is always preordered.) We define four relations which specify the implementation of joins. As before, we will use the letters J, K, and L to denote sets of attributes across which relations will be joined. We will illustrate these with the implementation of joins using CORP, in which the sale price P is the stationary set. A numerical example will follow.

The first relation is a mapping relation $A(X, J, K, Y)$ . Both J and K refer to the attributes in the stationary set: J refers to the values of the attributes of the stationary set (i.e., the value of P) entered into the model set, and K is the values (again, of P) calculated by the model set. X is the values of the attributes (M and U) inputted to the model set; and Y is the values of all other attributes (V, E, and N) calculated by the model set. Thus, the mapping relation describes the use of the model set during a single iteration of the search for a fixed point.

The second relation is the iteration relation $B(J, K, L)$ , which contains the decision rule for calculating at the end of one iteration the values of the attributes in the stationary set to be used as inputs to the model set for the next iteration. J and K have the same meaning as in the mapping relation, and L is the values of the new input attributes. For example, if the price in the next iteration is a convex combination of the prices entered into and calculated by the model set during the previous iteration, then we would have $L = \lambda J + (1 - \lambda) K$ for some $\lambda \in [0,1)$ . If $\lambda = 0$ , then L = K – that is, the input of the next iteration is the output of the previous iteration. We cannot have $\lambda = 1$ , because that would require that L = J, and the next iteration would be repeated with the same input of the previous iteration.

In defining the iteration relation, we have assumed that the only information used in calculating the input to the next iteration is the input and output of the previous iteration. Of course, the information from previous iterations of the model set may be used as well. However, recent experience suggests that a simple rule of the type given above leads to rapid convergence [Hogan, 1975; Ahn and Hogan, 1982], and we will rely on that experience here.

The third relation is the stopping signal relation $C(J, K, S)$ in which J and K are defined as before and S is a stopping signal used to determine whether the iterative process should continue. The stopping signal is a set of metrics on the attributes in the stationary set that measures the distances of the attributes in K from those in J. A common metric is the absolute values of the differences between the corresponding values of J and K. In the CORP example, we have $S = |J - K|$ . In other words, the stopping signal is the absolute difference between the price entered into the model set at the start of the previous iteration and the price calculated by the model during the previous iteration.

The fourth relation is a stopping rule relation, which maps the stopping signal into a decision rule to continue or to halt. The relation can take on either of two forms. The first is a continue relation $PC(S, Z)$ , in which S is the stopping signal, and Z takes on the value t if the iterative process is to continue and f if it is to halt. This will be used in a While-do operation for defining the stopping rule. The second is a halt relation $PH(S, Z)$ , which is the same as $PC(S, Z)$ , except that the t and f values are reversed. This will be used in a Repeat-until operation for defining the stopping rule.

If the stopping signal is a scalar, as it is in

CORP, the process will terminate whenever the stopping signal falls below a certain point. Let this point be denoted $\Pi$ . Then $PC(S, Z)$ will consist of tuples of the form $\langle S, t \rangle$ for $S > \Pi$ and $\langle S, f \rangle$ for $S \leqslant \Pi$ . Similarly, $PH(S, Z)$ will consist of tuples of the form $\langle S, t \rangle$ for $S \leqslant \Pi$ and $\langle S, f \rangle$ for $S > \Pi$ . We note that $PC$ and $PH$ are related by the If-then-else operations $PC = PH \uparrow F / T$ and $PH = PC \uparrow F / T$ .

The search for a fixed point is described by a single relation that consists of a combination of the four relations described above. The relation may be constructed in either of two ways, depending on whether the While-do or the Repeat-until operation is used to define the stopping rule. In each case the mapping relation is joined with the iteration relation to produce a single relation that describes the transformation of the inputted value of the stationary set at the start on one iteration to the inputted value at the start of the next iteration. In addition, the stopping signal relation is joined with one of stopping rule relations to produce a relation that describes whether the process will continue or halt. Finally, the two joins are combined using a While-do or Repeat-until operation to describe the entire search process. In the notation below, we will use a ◇ symbol to denote joins, which will be across any attributes common to the relations being joined.

The mapping relation is joined with the iteration relation as follows: $A(X, J, K, Y) \diamond B(J, K, L)$ . The result is a relation with tuples $\langle X, J, K, Y, L \rangle$ . For example, in CORP the types will be of the form $\langle M, U, J, K, V, E, N, L \rangle$ . We use $J, K$ , and $L$ to denote the values of $P$ that are:

(1) Inputted to the model set at the start of an iteration;

(2) Calculated by the model set during an iteration; and

(3) Inputted to the model set at the start of the next iteration if the next iteration is to be performed.

The stopping signal relation is joined with one of the stopping rule relations as follows: $C(J, K, S) \diamond PC(S, Z)$ or $C(J, K, S) \diamond PH(S, Z)$ . In either use the result is relation with tuples $\langle J, K, S, Z \rangle$ . Finally, we combine the two joins using a While-do operation (for the continue relation) or a Repeat-until operation (for the halt relation) as follows:

$$
\begin{array}{r l} & 1. (C (J, K, S) \diamond P C (S, Z))? (A (X, J, K, Y) \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad B (J, K, L)) \\ & 2. (A (X, J, K, Y) \diamond B (J, K, L))! (C (J, K, S) \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad P H (S, Z)) \end{array}
$$

In performing the While-do and Repeat-until operations, it is necessary to define $(A(X, J, K, Y) \diamond B(J, K, L))^{*}$ , which in turn requires that we define $(A(X, J, K, Y) \diamond B(J, K, L))^{n}$ for any integer $n \geqslant 0$ . To do this we must identify the pair of attributes over which relational composition is performed. The pair of attributes is $\langle J, L \rangle$ . In other words the power and hence, the extension, of the join of the mapping and iteration relations is defined in terms of the input to the model set at each iteration and the input (calculated by the iteration relation) at the following stage. This is illustrated in the numerical example below.

Let the models in CORP have the following functional forms:

1. FIN: $N = PV - E$

2. MFG: $E = 1000000 + UV$

$$
3. \mathrm{PRI}: P = M E \div V
$$

$$
4. \mathrm{MKT:} V = 8 2 7   2 0 0 - 4 4   0 0 0 P
$$

It is shown in [Blanning, 1982c] that when M = 1.1 and U = 8 there is a unique fixed point at P = 13.80, V = 220000, E = 2760000 and N = 276000. We will not address in this paper the possible nonexistence of fixed points nor the possible existence of multiple fixed points. We will use $\lambda = 0.1$ and $\Pi = 0.50$ in the calculation of the stopping signal and in the stopping rule.

The application of this approach to CORP with starting point P = 5.00 gives the relations shown in Fig. 2. In the notation of that figure, $P'$ is the price entered into the model set at an iteration, $P''$ is the price calculated by the model set during the iteration, and $P'''$ is the input for the new iteration. Thus, $P' = J$ , $P'' = K$ , and $P''' = L$ . We have illustrated only the tuples needed for a search for the optimum starting from P = 5.00. For example, the tuple $\langle 12, 11, 11.1 \rangle$ will appear in the iteration relation, even though it will not be needed for any search (because the search always proceeds towards the fixed point, not away from it). Similarly, the tuple $\langle 12, 11, 1 \rangle$ will appear in the stopping signal relation, even though it is not needed.

<table><tr><td>Mapping (A)</td><td>M</td><td>U</td><td>P&#x27;</td><td>P&#x27;&#x27;</td><td>V</td><td>E</td><td>N</td><td></td><td></td><td></td></tr><tr><td></td><td>1.1</td><td>8</td><td>5.00</td><td>10.61</td><td>607200</td><td>5857600</td><td>58576-</td><td></td><td></td><td></td></tr><tr><td></td><td>1.1</td><td>8</td><td>10.05</td><td>11.66</td><td>834981</td><td>4079847</td><td>407985</td><td></td><td></td><td></td></tr><tr><td></td><td>1.1</td><td>8</td><td>11.50</td><td>12.22</td><td>321350</td><td>3570797</td><td>357080</td><td></td><td></td><td></td></tr><tr><td></td><td>1.1</td><td>8</td><td>12.15</td><td>12.56</td><td>292582</td><td>3340653</td><td>334065</td><td></td><td></td><td></td></tr><tr><td>Iteration (B)</td><td>P&#x27;</td><td>P&#x27;&#x27;</td><td>p&#x27;&#x27;&#x27;</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>5.00</td><td>15.61</td><td>10.05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>10.05</td><td>11.66</td><td>11.50</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>11.50</td><td>12.22</td><td>12.15</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>12.15</td><td>12.56</td><td>12.52</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mapping◇Iteration(A◇B)</td><td>M</td><td>U</td><td>P&#x27;</td><td>P&#x27;&#x27;</td><td>P&#x27;&#x27;&#x27;</td><td>V</td><td>E</td><td>N</td><td></td><td></td></tr><tr><td></td><td>1.1</td><td>8</td><td>5.00</td><td>10.61</td><td>10.05</td><td>607200</td><td>5857600</td><td>585760</td><td></td><td></td></tr><tr><td></td><td>1.1</td><td>8</td><td>10.05</td><td>11.66</td><td>11.50</td><td>384981</td><td>4079847</td><td>407985</td><td></td><td></td></tr><tr><td></td><td>1.1</td><td>8</td><td>11.50</td><td>12.22</td><td>12.15</td><td>321350</td><td>3570797</td><td>357080</td><td></td><td></td></tr><tr><td></td><td>1.1</td><td>8</td><td>12.15</td><td>12.56</td><td>12.52</td><td>292582</td><td>3340653</td><td>334065</td><td></td><td></td></tr><tr><td>Stopping Signal (C)</td><td>P&#x27;</td><td>P&#x27;&#x27;</td><td>S</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>5.00</td><td>10.61</td><td>5.61</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>10.05</td><td>11.66</td><td>1.161</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>11.50</td><td>12.22</td><td>0.72</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>12.15</td><td>12.56</td><td>0.41</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Stopping rule:Continue (PC)</td><td>S</td><td>Z</td><td></td><td></td><td></td><td>Stopping rule:Halt (PH)</td><td></td><td>S</td><td>Z</td><td></td></tr><tr><td></td><td>5.61</td><td>t</td><td></td><td></td><td></td><td></td><td></td><td>5.61</td><td>f</td><td></td></tr><tr><td></td><td>1.61</td><td>t</td><td></td><td></td><td></td><td></td><td></td><td>1.15</td><td>f</td><td></td></tr><tr><td></td><td>0.72</td><td>t</td><td></td><td></td><td></td><td></td><td></td><td>0.72</td><td>f</td><td></td></tr><tr><td></td><td>0.41</td><td>f</td><td></td><td></td><td></td><td></td><td></td><td>0.41</td><td>t</td><td></td></tr><tr><td>Signal◇Continue(C◇PC)</td><td>P&#x27;</td><td>P&#x27;&#x27;</td><td>S</td><td>Z</td><td>Signal◇Halt(C◇PH)</td><td>P&#x27;</td><td>P&#x27;&#x27;</td><td>S</td><td>Z</td><td></td></tr><tr><td></td><td>5.00</td><td>10.61</td><td>5.61</td><td>t</td><td></td><td>5.00</td><td>10.61</td><td>5.61</td><td>f</td><td></td></tr><tr><td></td><td>10.05</td><td>11.66</td><td>1.61</td><td>t</td><td></td><td>10.05</td><td>11.66</td><td>1.61</td><td>f</td><td></td></tr><tr><td></td><td>11.50</td><td>12.22</td><td>0.72</td><td>t</td><td></td><td>11.50</td><td>12.22</td><td>0.72</td><td>f</td><td></td></tr><tr><td></td><td>12.15</td><td>12.56</td><td>0.41</td><td>f</td><td></td><td>12.15</td><td>12.56</td><td>0.41</td><td>t</td><td></td></tr><tr><td>The While-DoIterative Process:(C◇PC)?(A◇B)</td><td>M</td><td>U</td><td>P&#x27;</td><td>P&#x27;&#x27;</td><td>P&#x27;&#x27;&#x27;</td><td>V</td><td>E</td><td>N</td><td>S</td><td>Z</td></tr><tr><td></td><td>1.1</td><td>8</td><td>5.00</td><td>10.61</td><td>10.05</td><td>507200</td><td>5857600</td><td>585760</td><td>5.61</td><td>t</td></tr><tr><td></td><td>1.1</td><td>8</td><td>10.05</td><td>11.66</td><td>11.50</td><td>384981</td><td>4079847</td><td>407985</td><td>1.61</td><td>t</td></tr><tr><td></td><td>1.1</td><td>8</td><td>11.50</td><td>12.22</td><td>12.15</td><td>321350</td><td>3570797</td><td>357080</td><td>0.72</td><td>t</td></tr><tr><td></td><td>1.1</td><td>8</td><td>12.15*</td><td>12.56</td><td>12.52</td><td>292582</td><td>3340653</td><td>334065</td><td>0.41</td><td>f</td></tr><tr><td>The Repeat-UntilIterative Process:(A◇B)!(C◇PH)</td><td>M</td><td>U</td><td>P&#x27;</td><td>P&#x27;&#x27;</td><td>P&#x27;&#x27;&#x27;</td><td>V</td><td>E</td><td>N</td><td>S</td><td>Z</td></tr><tr><td></td><td>1.1</td><td>8</td><td>5.00</td><td>10.61</td><td>10.05</td><td>607200</td><td>5857600</td><td>585760</td><td>5.61</td><td>f</td></tr><tr><td></td><td>1.1</td><td>8</td><td>10.05</td><td>11.66</td><td>11.50</td><td>384981</td><td>4079847</td><td>407985</td><td>1.61</td><td>f</td></tr><tr><td></td><td>1.1</td><td>8</td><td>11.50</td><td>12.22</td><td>12.15</td><td>321350</td><td>3570797</td><td>357080</td><td>0.72</td><td>f</td></tr><tr><td></td><td>1.1</td><td>8</td><td>12.15*</td><td>12.56</td><td>12.52</td><td>292582</td><td>3340653</td><td>334065</td><td>0.41</td><td>t</td></tr></table>

\* Fixed point: $P = 12.15$

Fig. 2. The Fixed Point Relations for CORP.

Table 1  
Comparison of Iterative Processes

<table><tr><td>Value of  $\lambda$ </td><td>Number of Iterations</td><td> $P$ </td><td> $V$ </td><td> $E$ </td><td> $N$ </td></tr><tr><td>Any</td><td>0</td><td>5.00</td><td>607200</td><td>5857600</td><td>585760</td></tr><tr><td>1</td><td>4</td><td>12.15</td><td>292582</td><td>3340653</td><td> $334065^{+}$ </td></tr><tr><td>1</td><td>20</td><td>13.51</td><td>232758</td><td>2862061</td><td>286206</td></tr><tr><td>0</td><td>4</td><td>12.40</td><td>281656</td><td>3253248</td><td>325325</td></tr><tr><td>0</td><td>20</td><td>13.54</td><td>231243</td><td>2849942</td><td>284994</td></tr><tr><td>Any</td><td> $\infty$ </td><td>13.80</td><td>220000</td><td>2760000</td><td> $276000^{*}$ </td></tr></table>

$^{+}$ This is the solution in Fig. 1  
\* This is the exact solution

The iterative process described above results in a 12–33% error in the calculated values of P, V, E, and N. The error for a given model set is determined by: (1) the stationary set; (2) the starting point for the values of the attributes in the stationary set; (3) the rule for calculating the new values of the attributes in the stationary set (in this case, the value of $\lambda$ ); and (4) the stopping rule (in this case, the value of $\Pi$ ). A surrogate for the latter consideration is the number of iterations, which determines the cost of implementing the iterative process. In Table 1 we present the outcome of several iterative processes with different values of $\lambda$ and of the number of iterations. Reducing $\lambda$ to zero and increasing the number of iterations to 20 decreases the errors to the 3–19% range. The reason that the error is reduced by a decrease in $\lambda$ is that the process always proceeds towards the fixed point – therefore, the best value of $P''' : s$ in the range ( $P', P''$ ). This might not be the case when there is more than one attribute in the stationary set, because a movement of one attribute towards the fixed point may cause another attribute to move away from the fixed point, and the value of $\lambda$ leading to the most rapid convergence may be in the interior of the unit interval.

We summarize this formulation by applying Sanderson's results in:

## Theorem IV

Let $G = (C \diamond PC)?(A \diamond B)$ and $H = (A \diamond B)!(C \diamond PH)$ . Then:

(1) $G$ and $H$ are deterministic;

(2) For any $x_{1}Gx_{N}$ there is a unique sequence $x_{1}, x_{2} \ldots x_{N}$ , such that $x_{i}Gx_{i+1}$ for $i = 1, 2 \ldots N - 1$ ; and

(3) For any $x_{1}Hx_{N}$ there is a unique sequence $x_{1}, x_{2} \ldots x_{N}$ such that $x_{i}Hx_{i+1}$ for $i = 1, 2 \ldots N - 1$ .

(See Appendix IV.)

The tabular description of the search procedure described above suggests that a table-based relational language, such as Query-by-Example, might be useful in defining the search procedure. The syntax and hence, the tabular representation of such a language are specified below.

## 4. A Relational Language for Join Implementation

In [Blanning, 1983a] it is shown that the first order predicate calculus is relationally complete for model management and that it is possible to extend the syntax of Query-by-Example (QBE), a query language for data management based on the domain predicate calculus [Zloof, 1975], to model management. The resulting language, called TQL (Table Query Language), is a tabular language in which table skeletons represent model relations and special symbols are used to represent execution of the models, optimization, and sensitivity analysis. TQL is extended below to specify the procedures for implementing joins, using some of the representation procedures of SBA [Zloof and de Jong, 1977] which is an extension of QBE used to specify certain calculation procedures.

The extended TQL, which we will call ETQL, consists of five table skeletons, one for each of the five relations described in the previous section. Only four of the five skeletons need be defined for a particular iterative process, because the PC and PH relations are isomorphic. We now define the five table skeletons and illustrate their use in join specification by using them to specify the process described in the previous section.

The mapping table skeleton contains a column for each input to the model set and for the attributes in the stationary set. The latter columns contain the starting values for these attributes. For example, in CORP the mapping table skeleton is as follows:

<table><tr><td>M</td><td>U</td><td>P</td></tr><tr><td>1.1</td><td>8</td><td>5.00</td></tr></table>

The iteration table skeleton contains the iteration rule in formula form using example elements of the type used in QBE and SBA. We have not underlined the example elements here because all variables are example elements. For example, in CORP the iteration table skeleton is

<table><tr><td> $P'$ </td><td> $P''$ </td><td> $P'''$ </td></tr><tr><td>x</td><td>y</td><td> $(0.1 \times x) + (0.9 \times y)$ </td></tr></table>

The stopping signal table skeleton also uses example elements:

<table><tr><td> $P'$ </td><td> $P''$ </td><td>S</td></tr><tr><td>x</td><td>y</td><td>ABS(x-y)</td></tr></table>

The stopping rule table skeletons use equality and inequality relationships of the type used in QBE and SBA to select data tuples. Then the continue table skeleton is:

<table><tr><td>S</td><td>Z</td></tr><tr><td>&gt;0.5</td><td>t</td></tr><tr><td> $\leqslant 0.5$ </td><td>f</td></tr></table>

and the halt table skeleton is:

<table><tr><td>S</td><td>Z</td></tr><tr><td> $\leqslant 0.5$ </td><td>t</td></tr><tr><td> $>0.5$ </td><td>f</td></tr></table>

A model management system receiving these inputs would produce the following output:

<table><tr><td>P</td><td>V</td><td>E</td><td>N</td></tr><tr><td>12.15</td><td>292 582</td><td>3 340 653</td><td>334 065</td></tr></table>

## 5. The Integration of Data Bases and Model Banks

The literature on model management systems and DSS has long recognized that an important purpose of these systems is to facilitate the integration of a variety of information sources, which may be grouped into two major categories, data and models [Will, 1975; Sprague and Watson, 1975: Donovan, 1976]. It has also been suggested that existing non-relational frameworks for data base management be extended to encompass the description of model banks and of the relationships between data bases and model banks [Stohr and Tanniru, 1980; Konsynski, 1981; Pan, Pick and Whinston, 1982], and this notion is implicit in the development of 'DSS generators' – that is, building blocks for DSS that encompass a variety of data management, data analysis, and modeling procedures [Sprague, 1980; Sprague and Carlson, 1982; Wang and Courtney, 1982]. It has been observed that managers and analysts often view data and models as complementary sources of information [Blanning, 1981b], and this has led to the development of a language for data and model management based on a comprehensive view of information management in DSS [Blanning, 1982b, 1982f, 1979] and a comparison of the relational views of data and of models [Blanning, 1982e].

The eventual outcome of this type of research is not yet clear, but it is clear that the existing fragmentation of perspectives concerning information representation in decision support is counterproductive. The need to partition and integrate data relations is now well understood, and the research reported here (along with that reported in [Blanning, 1982b, 1982c]) is an attempt to identify the same needs with regard to decision models. This may lead to a more thorough understanding of the way in which information – regardless of how it is stored or calculated – may be effectively represented for decision making.

## Acknowledgement

This research was supported by the Deans's Fund for Faculty Research of the Owen Graduate School of Management, Vanderbilt University.

## References

Ahn, B.-h. and W.W. Hogan, On Convergence of the PIES Algorithm for Computing Equilibria, Operations Research 30 (March–April 1982) pp. 281–300.

Aho, A.V., C. Beeri and J.D. Ullman, The Theory of Joins in Relational Databases, ACM Transactions on Database Systems, 4 (Sept. 1979) pp. 297–314.

Alter, S.L., Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley, Reading MA (1980).

Bennett, J.L. (ed) Building Decision Support Systems, Addison-Wesley, Reading MA (1983).

Blanning, R.W., Language Design for Relational Model Management, in: Management and Office Information Systems, S.K. Chang ed., pp. 217–235 Plenum Press, New York (1984).

Blanning, R.W., A Decision Support Language for Corporate Planning, Policy Analysis and Information Systems, 6 (Winter 1982) pp. 313–323 (b).

Blanning, R.W., TQL: A Model Query Language Based on the Domain Relational Calculus, in: Proc. IEEE Workshop on Languages for Automation (Nov. 1983) pp. 141–146 (a).

Blanning, R.W., What is Happening in DSS, Interfaces, 13 (Oct. 1983) pp. 71–80 (b).

Blanning, R.W., Issues in the Design of Relational Model Management Systems, in: Proc. National Computer Conference (June 1983) pp. 395–401 (c).

Blanning, R.W., Normal Forms for Relational Model Banks, Owen Graduate School of Management, Vanderbilt University, Nashville TN (1982) (b).

Blanning, R.W., The Existence and Uniqueness of Joins in Relational Model Banks, Owen Graduate School of Management, Vanderbilt University, Nashville TN (1982) (c).

Blanning, R.W., A Relational Framework for Model Management in Decision Support Systems, DSS-82 Transactions (June 1982) pp. 16–22 (d).

Blanning, R.W., Data Management and Model Management: A Relational Synthesis, Proc. 20th Annual Southeast Regional ACM Conference (April 1982) pp. 139–147 (e).

Blanning, R.W., Ambiguity and Paraphrase in a Transformational Grammar for Decision Support Systems, Proc. 15th Hawaii International Conference on System Sciences, 1 (Jan. 1982) pp. 765–774 (f).

Blanning, R.W., Model Structure and User Interface in Decision Support Systems, DSS-81 Transactions (June 1981) pp. 1–7 (a).

Blanning, R.W., Model-based and Data-based Planning Systems, Omega 9 (Feb. 1981) pp. 163–168 (b).

Blanning, R.W., The functions of a Decision Support System, Information and Management, 2 (Sep. 1979) pp. 87–93.

Bonczek, R.H., C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York (1981) (a).

Bonczek, R.H., C.W. Holsapple and A.B. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management, Operations Research, 29 (March–April 1981) (b) pp. 263–281.

Bonczek, R.H., C.W. Holsapple and A.B. Whinston, Future Directions for Developing Decision Support Systems, Decision Sciences 11 (Oct. 1980) (a) pp. 616–631.

Bonczek, R.H., C.W. Holsapple and A.B. Whinston, The Evolving Roles of Models in Decision Support Systems, Decision Sciences 11 (April 1980) (b) pp. 337–356.

Bonczek, R.H., C.W. Holsapple and A.B. Whinston, The Integration of Network Data Base Management and Problem Resolution, Information Systems, 4 (1979) (a) pp. 1:3–154.

Bonczek, R.H., C.W. Holsapple and A.B. Whinston, Computer-based Support of Organizational Decision Making, Decision Sciences, 10 (April 1979) (b) pp. 268–291.

Bonczek, R.H., C.W. Hoisapple and A.B. Whinston, Processing Deep Structures in a Generalized Intelligent Query Processor for Decision Support, paper no. 612, Institute for Research in the Behavioral, Economic, and Management Sciences, Krannert Graduate School of Management, Purdue University, West Lafayette IN (1977).

Carlson, E.D. (ed.), Proceedings of a Conference on Decision Support Systems, Data Base, 8 (Winter 1977).

Chen, M.C., J.E. Fedorowicz and L.J. Henschen, Deductive Processes in Databases and Decision Support Systems, Proc. North Central ACM 82 Conference, pp. 81–100 (1982).

Date, C.J., An Introduction to Database Systems, 2nd edn, Prentice-Hall, Englewood Cliffs NJ (1977).

Dolk, D.R. and B.R. Konsynski, Knowledge Representation for Model management Systems, Naval Postgraduate School, Monterey CA (1982).

Donovan, J., Database System Approach to Management Decision Support, ACM Transactions on Database Systems, 1 (Dec. 1976) pp. 344–369.

Elam, J.J. and J.C. Henderson, Knowledge Engineering Concepts for Decision Support System Design and Implementation, Proc. 14th Hawaii International Conference on System Sciences, 1 (Jan. 1980) pp. 639–643.

Elam, J.J., J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proc. First International Conference on Information Systems (Dec. 1980) pp. 98–110.

Fick, G. and R. Sprague, Decision Support Systems: Issues and Challenges, Pergamon Press, Oxford (1980).

Filius, L., Combinatorial Fixed Point Algorithms, in: Game Theory and Related Topics, O. Moeschlin and D. Pallaschke eds., North-Holland, Amsterdam, New York (1979) pp. 165–172.

Ginzberg, M.J., W. Reitman and E.A. Stohr (eds.) Decision Support Systems, in: Proc. NYU Symp. Decision Support Systems, North-Holland, Amsterdam, New York (1982).

Hogan, W.W., Energy Policy Models for Project Independence, Computers and Operations Research, 2 (Dec. 1975) pp. 251–271.

House, W.C. (ed.) Decision Support Systems: A Data-Based, Model-Oriented, User-Developed Discipline, Petrocelli, New York (1983).

Keen, P.G.W. and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading MA (1978).

Keen, P.G. and G.R. Wagner, DSS: An Executive Mind-Support System, Datamation, 25 (Nov. 1979) pp. 117–122.

Klein, E., Mathematical Methods in Theoretical Economics, Academic Press, New York (1973).

Konsynski, B., Model Management in Decision Support Systems, in: Data Base Management: Theory and Applications, C.W. Holsapple and A.B. Whinston, eds., pp. 131–154, Reidel, Dordrecht (1983).

Konsynski, B.R., On the Structure of a Generalized Model Management System, Proc. 14th Hawaii International Conference on System Sciences, 1 (Jan, 1981) pp. 630–638.

Konsynski, B.R. and D. Dolk, Knowledge Abstractions in Model Management, DSS-82 Transactions (June 1982) pp. 187–202.

Naylor, T. and M. Mann, Computer Based Planning Systems, Planning Executives Institute, Oxford OH (1982).

Pan, S.S., R.A. Pick and A.B. Whinston, A Formal Approach to Decision Support, Krannert Graduate School of Management, Purdue University, West Lafayette IN (1982).

Sanderson, J.G., A Relational Theory of Computing, Springer-Verlag, Berlin, New York (1980).

Scarf, H.E., The Computation of Economic Equilibria, Yale University Press, New Haven CT (1973).

Schell, G.P., Knowledge Representation and Knowledge Manipulation in Decision Support Systems, PhD Thesis, Purdue University, West Lafayette IN (1983).

Sol, Henk G. (ed.) IN Processes and Tools for Decision Support, North-Holland, Amsterdam, New York (1983).

Sprague, R.H., Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly, 4 (Dec. 1980) pp. 1–26.

Sprague, R.H., Jr. and E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs NJ (1982).

Sprague, R.H., Jr. and H.J. Watson, Model Management in MIS, Proc. 7th National AIDS (Nov. 1975) pp. 213–215.

Stohr, E.A. and M. Tanniru, A Database for Operations Research Models, Int. J. Policy Analysis and Information Systems, 4 (1980) pp. 105–121.

Ullman, J.D., Principles of Database Systems, Computer Science Press, Potomac NJ (1980).

Wang, M.S.Y and J.F. Courtney, Jr., Design and Implementation of the MAGIC/ROC Decision Support System Generator, DSS-82 Transactions (June 1982) pp. 37–49.

Will, H.J., Model Management Systems, in: Information Systems and Organization Structure, E. Grochla and N. Szyperski, eds. pp. 468–482 Walter de Gruyter, Berlin (1975).

Zloof, M.M., Query by Example, Proc. national Computer Conference (June 1975) pp. 431–438.

Zloof, M.M. and P.S. De Jong, The System for Business Automation, (SBA): Programming Language, Communications of the ACM, 20 (June 1977) pp. 385–396.

## Appendixes

In the first three appendixes, we will use X, Y, J, K, and L to denote non-empty pairwise disjoint sets of attributes. Any joins will be across the attribute sets J, K, and L.

## Appendix I

We prove Theorem I: Consider the relation $U = \langle J, X, Y \rangle$ with functional dependency $J \to XY$ and its projections $R = \langle J, X \rangle$ and $S = \langle J, Y \rangle$ . Then U, R, and S possess the lossless join property.

Proof: Let $J_{1}$ be any value of the attribute set J. Since J is a key in U, there is only one tuple in U containing $J_{1}$ . Let this be $\langle J_{1}, X_{1}, Y_{1} \rangle$ . Hence, $\langle J_{1}, X_{1} \rangle$ is the only tuple in R containing $J_{1}$ , and $\langle J_{1}, Y_{1} \rangle$ is the only tuple in S containing $J_{1}$ : Thus, the only tuple containing $J_{1}$ in the join of R and S is $\langle J_{1}, X_{1}, Y_{1} \rangle$ . Since this is true of every $J_{1}$ in J, the join of R and S is U, and U, R, and S possess the lossless join property. QED

## Appendix II

We prove Theorem II: Consider the relation $U = \langle X, J, Y \rangle$ with functional dependencies $X \to J$ and $J \to Y$ and its projections $R = \langle X, J \rangle$ and $S = \langle J, Y \rangle$ . then $U, R$ , and $S$ possess the lossless join property.

Proof: Let $J_1$ be any value of the attribute set $J$ . Consider all tuples in $U$ containing $J_1$ . These will be of the form $\langle X_1, J_1, Y_1 \rangle, \langle X_2, J_1, Y_2 \rangle \ldots \langle X_N, J_1, Y_N \rangle$ . Since $J$ is a key in $S$ , we must have $Y_1 = Y_2 = \ldots Y_N$ . Also $\langle X_1, J_1 \rangle, \langle X_2, J_1 \rangle \ldots \langle X_N, J_1 \rangle$ are the only tuples in $R$ containing $J_1$ . Hence, the only tuples containing $J_1$ in the join of $R$ and $S$ are $\langle X_1, J_1, Y_1 \rangle, \langle X_2, J_1, Y_2 \rangle \ldots \langle X_N, J_1, Y_N \rangle$ . Since this is true of every $J_1$ in $J$ , the join of $R$ and $S$ is $U$ . Hence, $U, R$ , and $S$ possess the lossless join property. QED

## Appendix III

We prove Theorem III: Consider the relation $U = \langle J, K, L, X, Y \rangle$ with functional dependences $JK \to LX$ and $JL \to KY$ and its projections $R = \langle J, K, L, X \rangle$ and $S = \langle J, L, K, Y \rangle$ . Then U, R, and S possess the lossless join property.

Proof: Consider a value $J_{1}$ of J and all of the tuples in U containing $J_{1}$ . Within this set of tuples K uniquely determines L and L uniquely determines K. Therefore, K and L are bijective. Therefore, there are $N \geqslant 1$ distinct values of $K(K_{1} \ldots K_{N})$ , N distinct values of $L(L_{1} \ldots L_{N})$ , N values of $X(X_{1} \ldots X_{N})$ , not necessarily distinct, and N values of $Y(Y_{1} \ldots Y_{N})$ , not necessarily distinct, such that the set of tuples in U containing $J_{1}$ is the set $\langle J_{1}, K_{n}, L_{n}, X_{n}, Y_{n} \rangle n = 1 \ldots N$ . Thus, the set of tuples in R containing $J_{1}$ is the set $\langle J_{1}, K_{n}, L_{n}, X_{n} \rangle$ , $n = 1 \ldots N$ , and the set of tuples in S containing $J_{1}$ is the set $\langle J_{1}, L_{n}, K_{n}, Y_{n} \rangle$ , $n = 1 \ldots N$ .

Hence, the set of tuples in the join of $R$ and $S$ across $J, K$ , and $L$ containing $J_1$ is the set $\langle J_1, K_n, L_n, X_n, Y_n \rangle$ , $n = 1 \ldots N$ , which corresponds to the set of tuples in $U$ containing $J_1$ . Since this is true for all values of $J$ in $U$ , the join of $R$ and $S$ is $U$ . QED

## Appendix IV

We prove Theorem IV: Let $G = (C \diamond PC) ? (A \diamond B)$ and $H = (A \diamond B)! (C \diamond PH)$ . Then (1) $G$ and $H$ are deterministic, (2) for any $x_1 GxN$ there is a unique sequence, $x_1, x_2 \ldots x_N$ , such that $x_i Gx_{i+1}$ for $i = 1, 2 \ldots N - 1$ , and (3) for any $x_1 Hx_N$ there is a unique sequence $x_1, x_2 \ldots x_N$ such that $x_i Hx_{i+1}$ for $i = 1, 2 \ldots N - 1$ .

Proof: The Theorem would follow from Sanderson's results if A, B, C, PC, and PH were deterministic. B is deterministic because it is a single-valued mapping from the input and output values of the attributes in the stationary set for one iteration to the input values for the following iteration, C is deterministic because it is a single-valued mapping from the inputs and outputs of an iteration to the value of the stopping signal, and PC and PH are deterministic because the decision to continue or to halt is uniquely determined by the stopping signal. Therefore, we need only show that A is deterministic. In other words, we must demonstrate that a partially ordered set of deterministic models is deterministic.

Let a partially ordered model set $M$ contain $N$ models. Any finite partially ordered set contains at least one minimal element - that is, an element $m \in M$ such that $m \leqslant m'$ for all $m' \in M$ [Klein, 1973, Remark 3.4]. We can also see that removing a minimal element from a partially ordered set preserves the partial ordering - that is, $M \cap \overline{m}$ is a partially ordered set and thus, also contains a minimal element. Consider a sequence of model set $M_1 \ldots M_N$ such that $m_N = M$ and $M_i$ is generated from $M_{i+1}$ by removing a minimal element from $M_{i+1}$ . $M_1$ is deterministic because it contains a single deterministic model. If $M_i$ is deterministic, so also is $M_{i+1}$ , because $M_{i+1} \cap \overline{M}_i$ is a deterministic model which is an input to some or all of the models in $m_{i+1}$ but does not have among its inputs any outputs of the models in $M_i$ . Hence $M_N = M$ is deterministic. QED
