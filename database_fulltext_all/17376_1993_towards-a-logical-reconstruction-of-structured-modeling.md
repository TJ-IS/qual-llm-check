---
otero_id: 17376
otero_key: "6G32RPQM"
title: "Towards a logical reconstruction of structured modeling"
authors: "Srikanth Chari; Ramayya Krishnan"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90065-b"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards a logical reconstruction of structured modeling

Srikanth Chari
Netlab Inc., USA

Ramayya Krishnan

Carnegie-Mellon University, Pittsburgh PA, USA

Structured modeling (SM) is a modeling framework designed to represent a wide range of models. The ability to model a variety of data and mathematical relationships in it makes it interesting in the decision support system (DSS) context. This paper develops a logic-based executable modeling language called LSM for SM. Our approach differs from previous research on the development of languages and environments for SM in its ability to represent and manipulate information about structured models (e.g., assumptions). This has been achieved through the use of the embedded languages technique. We illustrate the representational features of LSM, and describe how functions defined in our formalism may be used to support model development.

Keywords: Structured modeling; Logic modeling; Embedded languages; Modeling environments

![](/api/attachments/6G32RPQM/fulltext/images/0e55c470f7d9ea8ca65c2ad5fd8ab51faa148174152acfaa16282cc7c3a7e8a2.jpg)

Ramayya Krishnan is an Assistant Professor for Management Science and Information Systems in the School of Urban and Public Affairs at Carnegie Mellon University. He has a B.Tech in Mechanical Engineering from the Indian Institute of Technology (Madras), a M.S. in Operations Research and a Ph.D. in Management Science and Information Systems from the University of Texas at Austin. His primary interests are logic modeling, model management, and semantic data modeling.

## 1. Introduction

Structured modeling (SM) [11,12] is a modeling framework designed to support the representation of a wide range of models from many disciplines. The ability to model a variety of data and mathematical relationships in SM makes it interesting in the context of decision support systems (DSS). At its core, SM is notation independent, and consequently, many different languages can be defined to support it. Examples include languages such as SML [14] and the visually interactive graph grammar approach of Jones [15].

While these languages support the representation of structured models, they do not appear to support either the representation or manipulation of information about the elements and structures that make up a structured model. However, it is this information about models and their elements that is used to support model development tasks such as model formulation, revision, integration, and validation $[2–7,16,17]$ . Some examples of the kind of information we have in mind range from “data dictionary” style information such as the date a model was defined, and by whom, to information required in model creation and revision such as the assumptions and approximations used by the model developer.

In this paper we develop a logic-based formalism to support the representation and manipulation of structured models as well as information about them. This has been achieved using the embedded languages technique $[2,4]$ . Specifically, this has involved the development of a language called LSM to represent structured models. To enable the representation of information about structured models declared in LSM, we embed LSM in a generic meta-modeling language called $L^{\uparrow}$ (read, Lup) $[2]$ . We also define functions in $L^{\uparrow}$ to manipulate structured models and information about them to support key model development activities such as model evaluation, validation, and maintenance. An important feature of our approach is its ability to incorporate readily modeling support functions defined in other model management contexts into an environment for SM.

The paper is organized as follows. We begin (section 2) with a brief introduction to the embedded languages technique. Following that (section 3) we introduce an attributed graph-based view of SM, and use it (section 4) to develop the LSM language. Examples are used to illustrate its features. We then describe (section 5) how information about expressions in LSM may be represented and manipulated in $L^{\uparrow}$ to support specific model development tasks. We conclude (section 6) with a brief description of our prototype implementation, and a discussion of future research issues.

## 2. The embedded languages technique

The embedded languages technique, due to Bhargava and Kimbrough [2,4], was developed to enable the representation and manipulation of information about expressions in a language $^{1}$ , called the embedded language, within a first-order-logic (FOL) language called the embedding language. It has been used to implement a model management system called TEFA [2].

The principal idea used to effect this embedding is the concept of a dual interpretation. That is, all object constants, function constants, and predicate constants that are part of the vocabulary of the embedded language are interpreted as object constants in the embedding language. Similarly, the logical constants of the embedded language are treated as functions in the embedding language. This idea is used to interpret well-formed formulae (wff) and expressions of the embedded language as terms $^{2}$ in the embedding language. The resulting benefit is the ability to predicate arbitrary kinds of information about expressions in the embedded language. Such information can be operated on by functions in the embedding language to support the various facets of model development.

Following [2], we have used a generic embedding language, called $L^{\uparrow}$ , to develop our formalism. We can illustrate the concept of a dual interpretation by considering a wff in an embedded language (in this case, LSM), and its interpretation as a term (functional expression) in $L^{\uparrow}$ .

Example. An assertion such as genus(resource) in LSM is interpreted as follows:

<table><tr><td></td><td>LSM Interpretation</td><td> $L^{\uparrow}$  Interpretation</td></tr><tr><td>genus</td><td>predicate constant</td><td>object constant</td></tr><tr><td>resource</td><td>object constant</td><td>object constant</td></tr><tr><td>genus (resource)</td><td>well formed formula</td><td>functional expression, written as genus.resource</td></tr></table>

The assertion in LSM is interpreted to mean that the object resource is of type genus. In this interpretation, the symbol genus is treated as a predicate constant in LSM. However, it is treated as an object constant in $L^{\uparrow}$ . This dual interpretation permits the wff genus(resource) in LSM to be treated as a functional expression, genus.resource, using the $\cdot$ (read, dot) function in $L^{\uparrow}$ . The ideas that we have described informally have been formalized within the technique as formal translation rules between expressions in the embedded language and their form in $L^{\uparrow}$ , the embedding language. The interested reader is referred to [2], [4] for details. We now briefly describe the language $L^{\uparrow}$ .

## 2.1. The Language $L^{\uparrow}$

$L^{\uparrow}$ is a FOL language that we use in our formalism to:

(a) specify the LSM language;

(b) to represent information about structured models declared in LSM; and

(c) to define functions that operate on this information about structured models to support model development tasks such as model evaluation, validation, and maintenance.

We restrict our comments here to the vocabulary of $L^{\uparrow}$ , making specific references to the relationships between its vocabulary and the vocabulary of an embedded language (in our case, LSM).

As with any FOL language, the vocabulary of $L^{\uparrow}$ can be defined in terms of a set C of object constants, a set F of function constants, a set R of relation constants, and a set V of variables. The sets C and F are related to the vocabulary of LSM as follows. If $\Delta C$ , $\Delta R$ , $\Delta F$ , $\Delta V$ are the object constants, predicate constants, function constants, and variables of LSM respectively, the set C of constants in $L^{\uparrow}$ is required to be

## $C\supset \Delta C\cup \Delta R\cup \Delta F\cup \Delta V.$

Thus all non-logical constants and variables of the embedded language are object constants in $L^{\uparrow}$ . Additionally, there can be other object constants in $L^{\uparrow}$ that are not related to the vocabulary of LSM. In fact a large proportion of the object constants used in the predication of information about expressions in LSM fall into this category.

We define the set F of function constants in $L^{\uparrow}$ to include at least three categories. The first category is the set of functions needed to treat expressions of LSM as terms in $L^{\uparrow}$ . These include the logical constants (e.g., connectives such as and) of LSM and the dot (.) function. The second category is the set of mathematical operators (e.g., +, sin). These symbols have their traditional mathematical interpretation. We note that the arithmetic operators in $L^{\uparrow}$ are distinct from the arithmetic operators of LSM which are interpreted as object constants in $L^{\uparrow}$ . The third category is the set of functions that operate on the (meta) information about expressions in LSM to support model development. Examples include functions to perform model evaluation and validation. There may be several arbitrary functions in $L^{\uparrow}$ in addition to these three categories.

Analogous to the set F, we define the set R of predicate constants in $L^{\uparrow}$ to include at least three categories. The first is the set of predicate constants used to distinguish between the object constants in $L^{\uparrow}$ in terms of their interpretation in LSM. Examples include predicates such as variable and function. For example, the statement variable(cost) in $L^{\uparrow}$ is interpreted to mean that the object constant cost in $L^{\uparrow}$ is used as a variable in LSM. The second category is the set of predicates used to distinguish between terms interpreted as well formed formulae (wffs) or classes of mathematical expressions of LSM. Examples include predicates such wff and defE. For example, the statement wff(genus.resource) is interpreted to mean that the term genus.resource is a wff in LSM. We elaborate on these predicates when we specify LSM in $L^{\uparrow}$ . The third category is the set of predicates used to predicate arbitrary kinds of information about structured models.

## 3. Structured modeling

Structured modeling (SM) is a modeling framework introduced by Geoffrion [11]. In the following we will assume prior knowledge of SM. A brief quote from [13] summarizes the key features of SM: "In a nutshell, however, one can say that structured modeling aims to provide a formal conceptual framework of considerable generality for modeling, within the broader task of laying the foundation for a new generation of modeling environments. The framework uses hierarchically organized, partitioned, and attributed acyclic graphs to represent the semantic as well as mathematical structure of a model". The interested reader is referred to [11], and [12] for a detailed description of SM.

## 3.1. A graph-based view of SM

As introduced by Geoffrion, SM is a framework that is based on a detailed elemental structure. Higher conceptual units such as the generic and modular structures are defined using the elemental structure. We pursue an alternative strategy for defining structured models, analogous to those used in data and mathematical modeling. We begin by naming and relating the higher conceptual units, i.e., the genera and the modules, to create an abstract generic and modular structure. The named genera and then defined (instantiated) using an elemental structure. This strategy is similar to creating a model schema or a database schema before instantiating it. Finally, we exploit the graph theoretic structure underlying SM, and develop directed, attributed graphs to define our view of a SM model schema and instances. We use this graph-based view to develop the logic-based language for SM. We describe formally the three graph structures used in SM. A simple assignment problem given in appendix A is used to illustrate ideas.

A SM model schema S is a three tuple $\langle GS,MS,I\rangle$ . GS and MS are directed, attributed graphs which represent the generic and modular structures. I represents the structural constraints on GS and MS.

The graph GS is a two tuple $\langle NG,EG\rangle$ . NG is the set of nodes in the graph GS. Each node ng in NG is referred to as a genus node and is a four tuple $\langle name,type,range,expression\rangle$ . This is equivalent to stating that each named node in the graph GS has attributes that declare a type, a range of values (i.e., a domain), and a functional expression used to compute the values of its elements. EG is the set of arcs in the graph GS. Each eg in EG is an arc directed from the genus being called to the calling genus. Since the set of calls are segmented (c.f. the segmented tuple), each arc is a three tuple $\langle called-genus-node,calling-genus-node,segment-number\rangle$ .

Example: Figure 1a shows the graph GS for the assignment model. The node assignment represents the set of assignments of resources to tasks. This genus node is defined by the tuple $\langle$ assignment,ce, $\bot$ , $\bot\rangle$ . $^{3}$ The string assignment names the genus and ce is its type. An example of an arc is the tuple $\langle$ resource,assignment,1 $\rangle$ . The segment number is simply a means of ordering the arcs (cf. calls) emanating from a node. Another example is the node $\langle$ total-cost,f,R + ,sum(I) sum(J) cost(I,J)\* assignvar(I,J) $\rangle$ . The tuple declares a genus named total-cost of type f, with a value range R + (the set of positive real numbers), and an associated functional expression used to compute the value of its elements. Note that the expression is the same as the objective function of the assignment model.

![](/api/attachments/6G32RPQM/fulltext/images/d875a10c0482ae81e0e94534cb8781f658477d201ab911e355f65566a789b1e6.jpg)  
Fig. 1a. Graph GS for assignment model.

The graph MS is a rooted tree with leaf nodes in one to one correspondence with the nodes in GS. The non-leaf nodes are referred to as modules. Since each module is a collection of genera, the module nodes represent a partition of the nodes of GS. MS is a two tuple $\langle NM,EM\rangle$ , where NM is the set of nodes in MS and EM is the set of arcs in MS. Each nm in NM is a $\langle name\rangle$ and each em in EM is a three tuple $\langle parent-node-name,child-node-name,order-number\rangle$ .

![](/api/attachments/6G32RPQM/fulltext/images/bab4173ce5549681a7e678f10b3e5831babb2f4d11aadfdf34fc3940aef3022a.jpg)  
Fig. 1b. Graph MS for assignment model.

![](/api/attachments/6G32RPQM/fulltext/images/e6f327ce70a840bcc9c66a837f937ed35d0941da815a99b9ba5e4445adef136c.jpg)  
Fig. 1c. Fragment of graph ES for the assignment model.

Example: Figure 1b shows the graph MS for the assignment model. The node &adata is a module that represents a collection of assignment data such as the set of possible assignments, the assignment variables, and the assignment cost. The link between it and its child node, cost, is represented by <&adata, cost, 3>. The order-number performs a function similar to the segment-number.

Several model instances may be defined to correspond to a model schema S. Each of these instances is analogous to an instance of a database schema. A model instance SI of a model schema S is a directed, attributed graph, ES, such that GS is a condensation $^{4}$ of ES with respect to a partition defined by the genus nodes. ES is a two tuple $\langle NE,EE\rangle$ . NE is the set of nodes and EE is the set of arcs of ES. Each node ne in NE, referred to as an element node is a three tuple $\langle name,containing-genus-node,value\rangle$ . Similarly, each ee in EE is a three tuple $\langle called-element-node, calling-element-node,segment-number\rangle$ .

Example: Figure 1c is a fragment of the graph ES that is a model instance for the assignment model. The node denoted by $\langle r1, resource, \perp \rangle$ represents an element r1 that is contained in the genus node resource.

The graphs ES, GS, and MS form a successive condensation of detail, whereby the nodes of ES are collapsed into the nodes of GS, and the nodes of GS in turn collapsed into the nodes of MS. Having defined the graph structures ES, GS, and MS, we present I, the set of constraints placed on these structures. We impose these constraints to ensure that models defined using the graph structures are consistent with the SM framework.

## 3.2. Structural Constraints

The graph GS must satisfy the following constraints:

(1) the type associated with each node must be one (and only one) of $\{pe,ce,a,f,t\}$ . These are the valid types permitted;

(2) a node of type pe must have no incoming arc;

(3) nodes of type other than pe must have at least one incoming arc. This follows from the definitions of ce, a, f, and t elements as segmented tuples of other elements;

(4) nodes of type ce or a must have all incoming arcs from nodes of type pe or ce only. This follows from the definition of ce and a elements as segmented tuples of other entity elements;

(5) each node G in GS must have only one incoming arc in each segment (i.e., each genus node must call only one genus node per segment);

(6) the graph GS must be acyclic and closed (i.e., no arc must refer to a node that is not part of the graph).

Next consider the constraints that the module graph, MS, must satisfy:

(7) the graph MS must be a rooted tree. This means that:

(a) the root node must have no parent,

(b) each non-root node must have only one parent, and

(c) there must be a path from the root to every node;

(8) the terminal nodes of MS must be in one to one correspondence with the nodes in GS;

(9) the graph MS must be monotone in the following sense: For every ordered pair of distinct sibling nodes N1 and N2 in MS, where N1 comes before N2, no genus descendant G1 of N1 must call a genus descendant G2 of N2 in GS (G1 = N1 and/or G2 = N2 permitted). Recall that genus nodes are in 1:1 correspondence with the leaf nodes of MS. This constraint ensures that no forward references are made in defining a structured model.

The elemental structure must satisfy the following constraints:

(10) each node N in ES must be contained in one and only one node G in GS. This follows from the definition of genera as a mutually disjoint and exhaustive partition on the elements;

(11) all nodes in ES that are called in the same segment by a node must be in the same genus;

(12) for any two nodes in the same genus, calls in identical segments must be to nodes in identical genera;

(13) corresponding to each arc $\langle E, E1, S \rangle$ in ES where E is in genus G and E1 is in genus G1, there must be an arc $\langle G, G1, S \rangle$ in GS.

Thus, if $\langle E, G, V1\rangle$ and $\langle F, G, V2\rangle$ are nodes in ES that both belong to genus G in GS, and there are arcs $\langle E, E1, S\rangle$ , $\langle E, E2, S\rangle$ , $\langle F, F1, S\rangle$ (implying that E calls E1 and E2 in segment S and F calls F1 in segment S), then by rule 10, E1 and E2 must be in the same genus (say G1), and by rule 11, E1 and F1 must be in G1. By rule 12, there must be an arc $\langle G, G1, S\rangle$ in GS.

We now define the concept of a satisfiable schema, where a schema is constructed from generic and modular structures.

Definition 1. A model schema S = ⟨GS,MS,I⟩ is said to be satisfiable if there exists at least one model instance corresponding to it (i.e., a graph ES exists such that GS is a condensation of ES).

We now demonstrate that a schema created from a generic structure GS and a modular structure MS that satisfy the constraints 1–9 stated above is satisfiable.

Proposition 1. If two graphs GS and MS (as defined above) satisfy the integrity constraints 1–9 stated above, there exists a procedure to create a graph ES, such that GS is a condensation of ES, and ES satisfies conditions 10–13. That is a schema S, such that $S = \langle GS, MS, I \rangle$ is satisfiable.

Proof. Assume that two graphs GS and MS exist that satisfy conditions 1–9 above. Define a graph ES such that for each node ⟨Gname,Type,Range,Rule⟩ in GS, there is a corresponding node ⟨Ename,Gname,Value⟩ (Ename is said to belong to Gname) in ES; for each arc ⟨Gname,GName1,S⟩ in GS, define an arc ⟨Ename,EName1,S⟩ in ES (where Ename and Ename1 belong to Gname and Gname1, respectively). Assign some valid value within the appropriate range to each attribute element, and a valid rule to each function and test element.

Since this procedure defines only one element per genus, each node N is ES must be contained in a unique genus, thereby satisfying condition 10. Since each genus calls only one genus per segment (by rule 5), only one element is called in each segment, trivially satisfying condition 11. For the same reason, condition 12 must be satisfied since there is only node per genus. Condition 13 is satisfied by construction: the arcs is GS and ES are in 1:1 correspondence. Therefore for each arc $\langle E,E1,S\rangle$ in ES, there must be an arc $\langle G,G1,S\rangle$ in GS, where E is in G and E1 is in G1. □

We now use this graph-based view of SM, to develop a first-order logic (FOL) based formalism for SM.

## 4. Structured modeling and first-order logic

LSM is a FOL based representation language for SM. To enable the representation and manipulation of information about structured models, LSM is embedded in $L^{\uparrow}$ , the generic embedding language described in section 2. In the following, we develop LSM, and describe how it is specified in $L^{\uparrow}$ . Using the example in appendix A, we illustrate model representation in $LSM/L^{\uparrow}$ .

## 4.1. The language LSM

LSM is the language that provides a notation for describing the attributed graph-based structures that we developed in section 3. As such, the ontology of LSM assumes the following kinds of individuals. They are:

\- elements (nodes in the elemental structure; e.g. the task t1, the resource r1);

\- genera (nodes in the generic structure; e.g. the set of resources, the set of tasks);

\- modules (nodes in the modular structure);

\- type (associated with each element and genus node);

\- elemental structure (the collection of elements and their inter-relationships);

\- generic structure (the collection of genus nodes and their inter-relationships);

\- modular structure (the tree of modules);

\- structured model (the collection of an elemental, generic, and modular structure);

\- numbers (numeric constants that are values associated with genera);

\- strings (non-numeric constants that are values associated with genera);

As with any FOL language, the vocabulary of LSM consists of a set of object constants, predicate constants, and function constants. Object constants in LSM are used to name all the individuals in the LSM ontology except elements. Elements are referred to using functional expressions as explained below.

## 4.2. The vocabulary of LSM

The vocabulary of LSM consists of:

Object constants pe,ce,a,f,t,⊥,bool,real

In addition there may be countably many object constants including numbers and names for the individuals in our ontology.

Predicate constants genus/3 $^{5}$ , genus/4, genus/5, module, elem/2, elem/3, estruc, gstruc, mstruc, sm

In addition there may be countably many predicate constants including arithmetic relations such as equality, inequality

Function constants !, #, dom, agg, gping, spl

In addition there may be countably many function constants including arithmetic operators +, -, \*, /), algebraic functions such as sin, cos etc. The functions !, and # are described below. The function dom is used to refer to the domain of a pe genus. The functions agg, gping, and spl are data modeling functions that are used to model aggregation, grouping and specialization. Due to space limitations they are not further discussed in this paper. The interested reader is referred to [9].

Variables There are countably many variables.

The function constants !/2 and #/2 bear special mention. They are both applied to the same arguments (genus names and index values). While the ! function is used in LSM to refer to nodes in an elemental structure, the # function denotes numbers and is used to mirror the use of indexed variables in mathematical expressions. The symbol ⊥ is used as a placeholder. The predicates and functions used to represent the three graphs (i.e., the nodes, arcs, and type attributes) are introduced below 6. The notation used to represent mathematical expressions in LSM is introduced in section 4.3. In the following, all object, predicate, and function constants begin with a lowercase letter. Variables begin with an uppercase letter.

(1) sm(Model) This predicate is used to name a structured model.

(2) gstruc(GSname, Model) This predicate names a generic structure to be part of a named structured model.

(3) mstruc(MSname,Gsname) This predicate names the modular structure defined on a named generic structure.

(4) estruc(ESname,Gsname) This predicate names an elemental structure that is an instance of a named generic structure.

(5) genus(G,pe,GS) G is the name of the genus; GS is the name of a genus structure; pe is the type of the genus.

(6) genus(G,ce,F,GS) G is the name of the genus; F is a functional expression of the form agg(L), gping(L); or spl(L) where L is the list of called genera; GS is the name of a genus structure; ce is the type of the genus;

(7) genus(G,T,L,Range,GS) G is the name of the genus, T is one of {a,f,t}; L is the ordered list of called genera; range is the range of values that the elements can take (e.g.,bool, the boolean set); GS is the name of a genus structure.

The list structure that contains the called genera implicitly represents arcs, and because elements in a list are ordered, the position in the list records the segment number.

(8) module(M, L, MS) M is the name of a module; L is an ordered list, $[N1, \ldots, Nk]$ , where each Ni is the ith child of M; MS is the name of a modular structure.

This predicate names a module node in a modular structure and names the list of nodes in the modular structure linked to it. The list structure implicitly records the order number.

(9) elem(G!I, ES) G is the name of the containing pe genus; I is the specific value of the index; ! is a function which is used refer to elements. It maps a genus name and index value (G!I) to a specific element in G; ES names an elemental structure.

(10) elem(G!I,L,ES) G is the name of the containing genus of type {ce,a,f,t}; I is the specific value of the index; L is a list structure of the form $[K1,\ldots,Kn]$ , where each Ki represents a called segment. Each Ki is in itself a list of the form $[E1,\ldots Em]$ , where an Ej represents an element; ES names an elemental structure.

The graph-based view of SM introduced in section 4 defined a model in terms of three attributed graph-based structures. The first four predicates name and relate these structures. Each structure was defined to consist of attributed nodes and arcs. The next three predicates represent genus nodes, their types, and the arcs in a generic structure. Of the next three predicates, the first predicate names and relates module nodes in a modular structure. The last two predicates represent and relate element nodes in an elemental structure.

## 4.2.1. LSM in $L^{\uparrow}$

We can specify the rules of formation of LSM as axioms in $L^{\uparrow}$ . Since LSM is a FOL language, these axioms correspond directly to the grammar of standard FOL languages with equality. Once again it is the treatment of the wffs of LSM as terms in $L^{\uparrow}$ (c.f., section 2) that allow us to specify the rules of formation of LSM in $L^{\uparrow}$ . We note that specifying LSM in $L^{\uparrow}$ enables syntactic validity of LSM expressions to be checked in $L^{\uparrow}$ . Some examples of axioms used to specify LSM are shown below.

Variables in these axioms are assumed to be universally quantified.

$$
\begin{array}{c} \text {term} (X) \Leftarrow \text {variable} (X) \lor \text {constant} (X) \\ \quad \lor \text {functional - expression} (X) \\ \text {wff} (R, X) \Leftarrow \text {relation} (R) \& \text {termlist} (X) \\ \text {wff} (\text {not} X) \Leftarrow \text {wff} (X) \\ \text {wff} (X \text {and} Y) \Leftarrow \text {wff} (X) \& \text {wff} (Y) \end{array}
$$

The logical constants (e.g., the symbol and) of LSM are treated as function symbols in $L^{\uparrow}$ . The predicate wff in $L^{\uparrow}$ is used to declare that an expression in LSM (treated as a term in $L^{\uparrow}$ ) is a well-formed formula (wff).

While the vocabulary and the grammar introduced above is sufficient to describe the graph structures and the type attributes of nodes, we require a notation to declare mathematical expressions (cf. rules associated with function and test genera). We now present a notation for declaring such expressions.

## 4.3. Mathematical expressions in LSM

The notation used to describe mathematical expressions in LSM is based on an existing algebraic modeling language called $L_{\downarrow}$ [2] which is similar to languages such as GAMS. This notation may be used to define the rules associated with the function and test genera.

In LSM all genera are treated as named individuals. However, mathematical relationships hold between the values associated with attribute, function, and test genera. Based on the #/2 function used in [2], we have introduced a similarly named function in LSM. It maps a genus name and a index value to a numerical value. As such, it can be used to mirror the use of indexed and unindexed algebraic variables in a mathematical expression. For instance, the total-cost expression from the assignment model in appendix A is given by

$$
\begin{array}{r l} \text { total   -   cost } & := \text { sum } (I) \text { sum } (J) \text { cost } \# [ I, J ] \\ & * \text { assign   -   var } \# [ I, J ] \end{array}
$$

We drop the use of the # function with unindexed algebraic variables in the interest of readability (e.g., total-cost# ⊥ will simply be total-cost).

Since the SM framework requires that elements of genera have values, we define axioms in $L^{\uparrow}$ that relate the value of elements to the value of # function introduced to obtain a more elegant syntax. An example is shown below.

value(G!I,X,ES) if value(G#I,X,ES)

This axiom states that the value of a genus element (G!I) under any elemental structure X is given by the value of the expression G#I.

This use of # function has two major advantages. First, mathematical models may be represented in LSM in conventional algebraic notation. More importantly, it clearly separates the notation used to represent mathematical expressions and the notation used to describe the graph structures of SM. This permits existing mathematical modeling languages to be incorporated (as we have, with modifications, the language $L_{\downarrow}$ ) into environments for SM. It also clearly brings out the value added by SM, i.e., that of explicitly modeling structural relationships between problem objects in a manner akin to data models.

We now present a few axioms in $L^{\uparrow}$ that define the rules of formation for mathematical expressions in LSM. These axioms have been adapted from those used to specify $L_{\downarrow}$ [2].

(1) alg-variable(A#I)← genus-name(G) & function(#) & index-variable(I)

An algebraic variable in LSM is a functional expression created by combining a genus name, an index variable and the # function. A special case is when the variable is unindexed. For notational convenience, we drop the # function in the case of unindexed variables.

(2) $\operatorname{def}\mathrm{E}(A := B) \Leftarrow \operatorname{alg}\text{-variable}(A) \& \operatorname{fun}\mathrm{E}(B)$

An expression of the form $A := B$ is a definitional expression if $A$ is an algebraic variable in LSM and $B$ is a functional expression. An example of definitional expression in LSM is:

total-cost := operating-cost + maintenance-cost.

Here total-cost is a algebraic variable and the expression operating-cost + maintenance-cost is referred to as in functional expression. The symbol := is used to define. It is distinct from =, which is used to denote equality. funE and defE are predicates in $L^{\uparrow}$ used to identify an expression as a functional expression and definitional expression respectively. alg-variable is a predicate used to identify a symbol used as an algebraic variable in LSM.

Indexed expressions such as the one shown below are also examples of definitional expressions.

forall( I,supply#[I] := sum(J,demand#[I,J]))

(3) $\operatorname{conE}(X < Y) \Leftarrow \operatorname{funE}(X) \& \operatorname{funE}(Y)$

This axiom states that any two functional expressions related by the < relation is a conditional expression. Conditional expressions are commonly used to state constraints in equational models. An example is

$\operatorname {sum}(I,\operatorname {assign}\# [I,J] <   1)$

4.4. An example in LSM

In this section we represent fragments of the assignment problem given in appendix A in LSM. The interpretation of the important predicates and functions in LSM is also detailed below.

Comments are enclosed using "/ \* \* /".

sm(assign\_model)

/\* This declares that assign \_model names a structured model. \*/

gstruc(assign\_struc, assign\_model)

/\* This asserts that assign \_struc is a generic structure of the structured model named assign \_model. \*/

genus(resource,pe,assign\_struc)

genus(task,pe,assign\_struc)

/\* This assertion names the genus node resource and declares its type to be pe, and relates it to assign \_struc generic structure \*/

genus(assignment,ce,agg([resource,task]),

assign\_struc)

/\* This assertion names the ce genus assignment and declares it to be the aggregation of the resource and task genera in the assign\_struc generic structure. This data modeling feature of LSM can only be used with ce genera declaration \*/

genus(assign-var,a,[assignment],int(0,1),

genus(cost,a,[assignment],pos(real),assign\_struc)

/\* This assertion names the a genus cost and relates it to the assignment genus that it calls in assign \_struc generic structure. The term pos(real) is used to declare the range of values (the set of positive real numbers) that elements of this genus can take \*/

genus(total-cost,f,[assign-var,cost],pos(real), assign\_struc)

/\* This assertion names the f genus total-cost and relates it to the cost and assign-var genera that it calls in assign \_struc generic structure. \*/

total-cost := sum(I in dom(resource)) sum(J in dom(task)) cost#[I,J] \* assign-var#[I,J]

/\* The expression shown above is a definitional expression. The syntax is similar to conventional algebraic syntax. We note the use of the # function in LSM to represent indexed variables. It takes a genus name and a specific index value as arguments. \*/

genus(t:avail,t,[assign-var],bool,assign\_struc)

forall(I in dom(resource),sum(J in dom(task),assign-var#[I,J] ≤ 1))

genus(t:dem,t,[assign-var],bool,assign\_struc)

forall(J in dom(task),sum(I in dom(resource),assign-var(I,J)=1))

/\* These mathematical expressions correspond to the constraints of the assignment model. These are a class of conditional expressions in LSM \*/

The generic structure can be organized using a modular structure. A modular structure is a rooted tree whose leaf nodes are 1:1 with the genera. The interior nodes are the modules.

mstruc(assign\_model, assign\_struc)

/\* This assertion declares that the modular structure assign\_model is a modular structure associated with the generic structure assign\_struc. \*/

module(&adata,[assignment,assign-var,cost], assign\_model)

/\* This assertion declares that the module node &adata is in the modular structure assign\_ model and is an ordered set consisting of the genus nodes named in the second argument.
\*/

The example thus far has represented information about the schema of the assignment model. We note that the declaration of the definitional and conditional expressions in LSM map quite clearly to the mathematics of the assignment model. We present a few examples of elemental detail associated with the assignment problem.

estruc(assign\_scene, assign\_struc)

/\* This assertion declares that the elemental structure named by assign\_scene is associated with the generic structure named by assign\_struc. \*/

dom(resource, assign\_scene) = [r1, r2, r3, r4]
dom(task, assign\_scene) = [t1, t2, t3, t4]

/\* These declare the elements in a pe-genus in a given elemental structure \*/

elem(resource![r1],assign\_scene)
elem(task![t1],assign\_scene)

We have adopted a uniform notation to represent elements of genera. They are each referred to using the function !. However, since the elements of the pe genera are declared using the dom function, the element declarations for the pe genera, such as those shown above can be inferred. This prevents redundant element declarations for pe genera from having to be supplied by the modeler. The axiom in $L^{\uparrow}$ used to infer the elem declarations for the pe genera is

$\operatorname {elem}(\mathbf{G}![I],\mathbf{A})$ if $\operatorname {dom}(G,A) = L$ & member $(I,L)$

Elements of genera of other types (i.e., ce, f, a, and t) are declared using the elem predicate as shown below.

elem(assignment![r1,t1],assign\_scene)
elem(cost![r1,t1],assign\_scene)

We have illustrated how structured models are declared in LSM. One feature of structured models we have not represented in LSM are elemental values $^{7}$ . They are declared in $L^{\uparrow}$ , where they are used directly in model evaluation. We describe their representation and use in section 5. We have also noted earlier that LSM is embedded in $L^{\uparrow}$ . In the following section, we illustrate briefly how the example in LSM is embedded in $L^{\uparrow}$ .

## 4.5. The example in $L^{\uparrow}$

All declarations in LSM are translated into $L^{\uparrow}$ . Essentially, this is done by translating all expressions and wffs of LSM to terms in $L^{\uparrow}$ . First, all atomic wffs of LSM are translated into terms using the dot function in $L^{\uparrow}$ . All compound wffs are translated into terms by treating logical connectives in LSM as functions in $L^{\uparrow}$ . We note that this translation can be automated. $^{8}$

Once translated into $L^{\uparrow}$ , axioms stated in $L^{\uparrow}$ may be used to manipulate LSM expressions and information about them. We present examples of meta information and model management (manipulation) functions in section 5. In the following we present fragments of the example presented in section 4.4 in their translated form as statements in $L^{\uparrow}$ .

The assertion genus(resource,pe,assign \_struc) in LSM is stated in $L^{\uparrow}$ as

## wff(genus.resource.pe.assign\_struc)

This follows from the dual interpretation discussed earlier. All wffs of LSM are treated as terms in $L^{\uparrow}$ . The predicate wff in $L^{\uparrow}$ is used to assert that the term is a wff in LSM. Note the use of the dot function to create a term.

defE(total-cost := sum(I in dom(resource))sum(J in dom(task))cost#[I,J]\*assign-var#[I,J]), 'This defines the total-cost function to be used as a objective function in the assignment problem', assign\_struc)

Mathematical expressions declared in LSM are translated and stated in $L^{\uparrow}$ using predicates such as defE to represent definitional expressions, conE to represent conditional expressions and so on. An example of a conditional expression in LSM stated in $L^{\uparrow}$ is shown below.

conE(forall(J in dom(task),sum(I in dom(resource)) assign-var#[I,J]=1, 'This is a constraint function in the assignment problem', assign\_struc)

All conditional expressions declared in LSM are stated in $L^{\uparrow}$ using the predicate conE.

These brief examples are illustrative of the approach used to embed LSM expressions in $L^{\uparrow}$ . Once the wffs of LSM are represented as terms in $L^{\uparrow}$ , arbitrary kinds of information can be predicated about them. This information can be operated on by the functions defined in $L^{\uparrow}$ .

## 5. Meta information and manipulation in $L^{\uparrow}$

The information that can be represented in $L^{\uparrow}$ range from managerial information (e.g., who created the model, when was it created, its version status etc.) to mathematical (e.g., the functional expression A in model M is a piece-wise linear approximation of a non-linear functional expression B). This information, of and about structured models, can be used to support a variety of model development tasks. In the following we present functions to support model evaluation, dimensional validation, and model maintenance. We begin with model evaluation to illustrate a conventional kind of functionality supported by most current modeling environments.

## 5.1. Model evaluation

Models are evaluated by evaluating their associated mathematical expressions. This involves evaluating an expression consisting of variables under a particular value assignment. Thus, we need to be able to assign values to the algebraic variables and define axioms to perform evaluation. Consider a simple example.

$$
\text { total - cost } := \text { holding - cost } + \text { purchase - cost }.
$$

Recall that total-cost, holding-cost, and purchase-cost are algebraic variables in LSM. We assign values to them under specific elemental structures in $L^{\uparrow}$ . For example, we may assign the value of 30 to holding-cost and a value of 60 to purchase-cost as follows.

$$
\begin{array}{l} \text {value(holding - cost,30,assign\_scene)} \\ \text {value(purchase - cost,60,assign\_scene)} \end{array}
$$

/\* These are values assigned to the variables that make up a mathematical expression. The values of elements in a elemental structure are inferred from these values. \*/

Under this assignment, we need to be able to evaluate total-cost to 90. We define a function called eval in $L^{\uparrow}$ to evaluate expressions using values assigned to the variables in them. We present a subset of the axioms used to define eval. We note that the implementation of our formalism in PROLOG directly employs the axioms used in the definition.

/\* eval/3 is a predicate in $L^{\uparrow}$ . Its interpretation is described below. \*/

eval(Exp, Value, Elemental-Structure)

/\* eval is interpreted as "Value is the value of the expression Exp evaluated under the elemental structure Elemental-Structure \*/

An axiom that is part of the definition of eval and used to perform simple arithmetic is shown below.

$\operatorname{eval}(\mathrm{T},\mathrm{V},\mathrm{ES}) \Leftarrow \operatorname{defE}(T := \operatorname{Exp}), \operatorname{eval}(\operatorname{Exp},\mathrm{V},\operatorname{ES})$

This axiom states that if there is a definitional expression of the form $T := Exp$ , the value of T is given by the value of Exp. An axiom that evaluated expressions of form $X + Y$ is given below.

eval(X + Y, V, ES) ← eval(X, A, ES) &  
eval(Y, B, ES) & V := A + B

This axiom states that the value of any expression of the form $X + Y$ under a value assignment given by an elemental structure is the sum of the values of the component expressions. The axiom can be applied recursively to complex component expressions.

eval(X,V,ES) $\Leftarrow$ value(X,V,ES)

This axiom states that an expression X evaluates to V if it is assigned a value V (using the value predicate).

Using these two axioms, the example problem of computing the value of total cost from purchase cost can be computed. The values of the elements of the genera associated with this variable are obtained using the axiom shown below.

value(G!I,V,ES) $\Leftarrow$ value(G#I,V,ES)

This axiom states that the value of an element, $G!I$ , in an elemental structure is the value of the variable, $G\#I$ , in the same elemental structure.

The axioms we have described can be used to evaluate a series of non-simultaneous definitional expressions. However, it is often necessary to determine if a set of conditional expressions are satisfied (i.e., evaluate to true) under a particular value assignment. We introduce a function feasible/2 in LSM and specify axioms in $L^{\uparrow}$ to evaluate it.

Informally, the function is defined in the following way. feasible(A,ES) = 1 if the conditional expressions associated with the model named by A are satisfied under a value assignment specified in the elemental structure named by ES. The function is assigned a value of zero otherwise.

eval(feasible(A,ES)) = 1

$\Leftrightarrow \operatorname{conE}(A, L) \& \operatorname{satisfied}(L, \operatorname{ES})$

The axiom states that the value of the function is 1 iff the list of conditional expressions L in the model A are satisfied under a value assignment specified in the elemental structure ES.

satisfied(H.L,ES) $\Leftarrow$ satisfied(H,ES)& satisfied- $(L,\mathrm{ES})$

satisfied(Exp1 ≥ Exp2, ES) ← eval(Exp1, V1, ES),

eval(Exp2, V2, ES), V1 ≥ V2

satisfied(Exp1 R Exp2,ES) ⇔ eval(Exp1,V1,ES), eval(Exp2,V2,ES),V1 R V2

These axioms are a subset of those that specify the function satisfied. It takes two arguments: A set of conditional expressions and a named elemental structure ES. One type of conditional expression in LSM consists of two expressions standing in some relation R with one another. An example of the relation R we have in mind is the relation $\geq$ . A conditional expression ARB is defined to be satisfied if the evaluation of the expression A stands in relation R to the evaluation of expression B.

A feature closely related to model evaluation is sensitivity analysis. This is the process of trying to understand the sensitivity of the model under varying value assignments, especially to specific exogenous parameters. To manage this process, we exploit our ability to name the elemental structures under which value assignments are made. We use this feature to record the similarities and differences between elemental structures (and value assignments) in $L^{\uparrow}$ . Note that this information is clearly information about the model being recorded in $L^{\uparrow}$ .

We illustrate this feature with an example. We may have two elemental structures that are ‘essentially’ the same but for a few differences in the values that elements are assigned. We introduce the predicate similar/3 to record this information.

## similar(es1,es2,[value(cost![r1,t1]])

This assertion states that two elemental structures associated with the same generic structure are similar except for the value of the elements in the list.

We may also infer this information about similarity by comparing elemental structures in $L^{\uparrow}$ . An axiom that may be used to infer similarities is shown below.

graph-similar(G1,G2)

$\Leftarrow$ node-set $(S,G1)$ , node-set $(T,G2)$ , similar-set $(S,T)$ ,

/\* The axiom states that two elemental structures are similar if they have similar node sets and arc sets \*/

similar-set([], List)

similar-set( A.List1,List2)

$\Leftarrow$ member(A,List2),

/\* This is a definition of the similar set predicate assuming the unique names assumption [5] \*/

## 5.2. Model Integrity

Models declared in LSM have to satisfy the constraints defined in section 3. We refer to these constraints as integrity constraints. These constraints can be stated as axioms in $L^{\uparrow}$ . These axioms have been implemented in our environment to ensure that a collection of LSM wffs represent valid structured models. We provide some examples of these constraints. The constraints are first stated in English and then as axioms in $L^{\uparrow}$ .

(1) Genus nodes of type ce must only call genera of type pe or ce.

valid-wff(genus.G.ce.f(L).GS)

The axiom states that if there is a LSM wff that asserts that a genus G is of type ce, then each element of list L of genera called is either a genus of type pe or ce.

(2) The generic structure graph GS must be acyclic and closed.

acyclic(GS)

$\Leftarrow \mathrm{wff}(\mathrm{genus.G.T.GS})\& \neg (\mathrm{path}(\mathrm{G},\mathrm{G},\mathrm{GS}))$

A generic structure GS is acyclic if there is no genus in it that directly or indirectly refers to itself.

path(G,H,GS)←wff(gcalls-dir.G.H.K.GS)

path(G,H,GS) $\Leftarrow$ wff(gcalls-dir.G.L.K.GS) & path(L,H,GS)

The wff gcalls-dir(A,B,C,D) is interpreted as "the genus A calls the genus B in segment C in generic structure D"

Acyclicity is checked by ensuring that there is no path from any node to itself. The path between two nodes is checked recursively.

wff(gcalls\_dir.G.G1.K.GS)

$\Leftarrow \exists S1\exists T1$ wff(genus.G1.S1,T1.GS)

This axiom states that the collection is closed if every G1 that is called by any node G is also a node in the graph.

Note that these axioms can only be applied after the entire structured model is declared in LSM. This is contrast to the previous axiom that can be used to detect inconsistencies immediately on declaration.

(3) Each genus should have a type that is one of $\{pe,ce,a,f,t\}$

valid-wff(genus.N.T.L.GS)

$\Leftarrow$ valid-type $(T)$ valid-type (ce)

The axiom ensures that the type of the attribute used in genus declarations belongs to the valid set of types. This is once again an axiom that can be used immediately to provide feedback to the modeler.

(4) In addition to these kinds of constraints, specific domain constraints may need to be enforced. For instance in the assignment problem of appendix A, we may require that each resource and each task should be part of at least one assignment. In effect, this requires that we consider each element of the genus resource (task)

and ensure that it is called by some element of the assignment genus. This is readily stated as an axiom in $L^{\uparrow}$ . Clearly this sort of checking can be performed only after the entire model has been specified.

∀I in dom(resource) valid\_wff
(elem(resource!I,ES))←∃J in dom(task)
wff(elem(assignment![I,J],ES)

## 5.3. Model description

One of the principal advantages of the embedded languages technique is the ability to represent arbitrary pieces of information about models. Examples of the kinds of information we have in mind include historical information about models, information used to assign model development responsibilities, to control access, and to support features such as version control. We provide illustrative examples of how these kinds of information may be represented in $L^{\uparrow}$ .

Model development is often a group effort with responsibilities assigned to different individuals. We may represent information about who created the various model structures and when they were created in $L^{\uparrow}$ . This kind of information is often used to control model development efforts.

created-by(assign\_struc,"R.Krishnan",07061989)
created-by(assign\_scene,"Srikant Chari",07111989)

/\* These assertions declare that the structures named by assign\_struc and assign\_scene were created by the named individuals on a particular date. \*/

version(assign\_model, human-factors-group, "A5.3")

permit-access(Version,Model,Person) $\Leftarrow$ version(Model,Group,Version) &
authorized(member(Person,Group))

/\* Information about versions and who has access to them may also be represented. This axiom provides access to any member of a group that created a version of the model \*/

Oftentimes, modelers develop insights and experience over the course of a project about the reliability of sources of data used in the model and about the various versions of a model developed using different assumptions. This information can also be rendered in $L^{\uparrow}$ and used to support the model developer in model selection.

data-source(cost, assign\_scene, db-file(cost-param, cost-est), "acctg-dept", noisy)

/\* This assertion declares that the cost parameter in the assign\_scene element structure was obtained from a named database file prepared in the accounting department and that the data was noisy. \*/

model-source(assign\_model,"Geoffrion's Collection")

/\* This assertion declares the source from which the model was obtained. \*/

version(assign\_model, manufacturing, "5.2M", robust)

/\* This assertion declares that this particular version of the model is robust. \*/

Given a situation where the quality of data in an application is known to be poor (e.g., a forecasting application using sensor data), the information about the robustness of a model can be used to support model selection.

choose-model(X,P)←version(X,P,robust) & data-source(P,noisy)

/\* This rule suggests model X for problem P if it is robust and the data for the problem is noisy \*/

Models have to be communicated to model users and to model developers. While several alternatives have been proposed, SM can support the model communication at varying levels of detail via its graph structures. Since the declaration of the structured model in LSM is essentially an encoding of the graph structures, model communication can be facilitated by drawing the graphs corresponding to the LSM declarations. The graphs in figs. 1a, 1b and 1c illustrate what we have in mind. Graph drawing functions implemented in other system such as [15] can be incorporated into $L^{\uparrow}$ to support such features.

Modular structures are a unique feature of SM that permit the presentation of model features at varying levels of detail. As described in section 3, several alternative modular structures can be defined on a generic structure. Since modular structures are named in $L^{\uparrow}$ , information can be predicated about them. For instance, if the level of detail associated with a modular structure is represented, this information could be used in structuring a report at a level of detail most suited to the model user. For example, the modular structure used to communicate the model to a manager would contain little detail compared to a modular structure used to communicate the model to another modeler.

level-of-detail(assign\_mod, assign\_struc, high)
This asserts that the assign\_mod modular structure associated with the assign\_struc generic structure contains a lot of detail.

level-of-detail(manager\_model, assign\_struc, low) On the other hand, the manager\_model structure associated with the same generic structure has a low degree of detail.

The level of detail associated with modular structures may be used to select modular structures based on a user profile. For instance, if type of user is manager then the modular structure containing the low degree of detail would be most suitable.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
choose-model-view(A,M,U)
 $\Leftarrow$  type-of-user(U,T), profile(T,D),
level-of-detail(A,M,D)
</div>

The axiom relates the modular structure to be selected to the profile of the user for whom the model is being selected.

Most of the examples that we have described above can be used to support a wide variety of queries about models. This, we believe, is a useful, yet, simple feature that can be used to improve modeling productivity.

## 5.4. Model validation

Models need to be validated both prior to and after model solution. Most systems ensure syntactically valid models. Our intention here is to describe how some degree of semantic validity may be enforced. Work has been reported by several researchers including ourselves on topics related to semantic validity $[7]$ such as quiddity $[6]$ and dimensional validation $[1]$ . Our intent here is to note that we can incorporate these approaches within our formalism and to sketch how this is done in the case of dimensional validity.

In LSM, dimensions and units of measurement may be associated with the variables that are associated with the a, f, and t genera. These dimensions and a few axioms to manipulate them are shown below.

dimension(cost, currency)

/\* This assertion declares the dimension of the variable cost \*/

units-of-measurement(cost,\$)

/\* These assertions declare the units of measurement of cost \*/

dim-valid(X + Y)

$\Leftarrow\dim(X,A),\dim(Y,B),\dim-\text{equivalent}(A,B)/^{*}$ this axiom declares the expression $X+Y$ to be dimensionally valid if the dimension of X and Y are equivalent up to some transformation \*/

dim-valid(X = Y)

$\Leftarrow \dim (X,A),\dim (Y,B)$ , dim-equivalent $(A,B)$ /\* this axiom declares $X = Y$ to be dimensionally valid if $X$ and $Y$ have equivalent dimensions\*/

$\dim (X^{*}Y,A)$

$\Leftarrow\dim(X,L),\dim(Y,M),\dim-\text{multiply}(L,M,A)$ /\* this axiom defines the dimension of the expression $X^{*}Y$ to be the dimensional product of the dimensions of X and Y, respectively \*/ These axioms define a dimensional calculus that can be used to ensure dimensional validity.

Ensuring the consistency of the units of measurement in mathematical models is a time consuming and error-prone task. Axioms and laws of conversions between units can be used to automate this task. These laws of conversion are well known and have been encoded within TEFA [3]. We can provide similar support within our environment.

## 5.5. Reasoning with assumptions

Mathematical models rest on assumptions. However, assumptions are not part of the mathematics of the model. They represent information about models. Changing an assumption results in changes to the mathematical form of the model. In fact over the course of a project, assumptions often change, resulting in a model maintenance problem of having to keep track of the alternative sets of models developed to solve a particular problem.

We illustrate the use of assumptions by taking an example that involves the type and form of mathematical approximation used in model creation. Consider the following scenario. A mathematical model is developed of an inherently nonlinear system. Now one might develop a model of this non-linear system by approximating the nonlinearities with linear functions. Let the set of equations be part of a named generic structure in LSM, say alp. Now, one might also develop another model using a different approximation. Let this be part of another named generic structure nlp. We can declare that the functional expressions employed in each of these generic structures is an approximation in $L^{\uparrow}$ using the predicate approx.

approx(A := 3B + C, alp, A := sin(B))

approx(A := B^2, nlp, A := sin(B))

/\* These assertions declare that the definitional expression in the first argument is an approximation of the definitional expression in the third argument. The second argument names the generic structure. \*/

Information about available approximations can be useful in reformulation. A modeler may wish to change an approximation to create, say, a more tractable model. Using its knowledge about the computational properties of approximations, the system can suggest alternative approximations. For instance, given the two approximations shown above, the linear approximation is clearly more tractable than the non-linear approximation.

more-tractable-approx(New, Current, Phenom) $\Leftarrow$ approx(Current, Phenom) &
    approx(New, Phenom) &
    more-tractable(New, Current)

/\* This suggests that the approximation New can be used to replace the Current approximation for the phenomena being modeled as the New approximation is more tractable \*/

Additionally, information about approximations may be used to infer that two generic structures are essentially the same except for differences in the type of approximation used. Such an axiom in $L^{\uparrow}$ is

$\text{approx}(F1,F3,\text{AGS}) \& \text{approx}(F2,F3,\text{BGS}) \Rightarrow \text{gapprox}(F1,\text{AGS},F2,\text{BGS})$

The above axiom states that a function F1 in the generic structure AGS and the function F2 in the generic structure BGS are both approximations of the same function F3.

Since the interpretation of the results obtained from model evaluation is closely related to the model assumptions, approximations can be used to explain models and their results. This is particularly useful when we have two models that employ different assumptions to model the same problem.

## 6. Conclusions

In this paper, we have introduced a graph-based view of SM and developed a logic-based language called LSM to represent structured models. The language provides a semantic account of the SM framework. By embedding LSM in $L^{\uparrow}$ , we have also demonstrated how a variety of information may be predicated about structured models, and provided examples of model manipulation functions that use such information to support model evaluation, validation, and maintenance.

We have developed a prototype environment for SM using the formalism discussed in the paper. The system is implemented in C-PROLOG and runs on DEC 3100 workstation. The implementation supports the representation of the three graph structures used to define a structured model, and automatically enforces all the constraints that are part of the formal SM model discussed in section 3. The function for expression evaluation has also been implemented, and can evaluate non-simultaneous unindexed systems of equations. Finally, the implementation supports a wide variety of queries using the rules and information described in section 5.

Philosophically, the paper represents the integration of two alternative paradigms, SM and the embedded language technique, that are currently being used to develop modeling environments. We believe that this integration is particularly beneficial as it readily permits modeling support functions defined in other model management contexts to be incorporated into an environment for SM.

## References

[1] S. Abiteboul and R. Hull, IFO: A Formal Semantic Database Model, ACM Transactions on Database Systems 12, No. 4 (1987) 525–565.

[2] H. Bhargava, A Logic Model for Model Management, Unpublished PhD Dissertation, University of Pennsylvania, Pittsburgh, PA, 1990.

[3] H. Bhargava, M. Bieber and S. Kimbrough, Oona, Max and the WYWWYWI principle: Hypertext and Model Management in a Symbolic Programming Environment, Proceedings of the Ninth International Conference on Information Systems (1988) 179–191.

[4] H. Bhargava and S. Kimbrough, Model Management: An Embedded Languages, forthcoming in Decision Support Systems.

[5] H. Bhargava and R. Krishnan, A Formal Approach to Model Formulation in Model Management Systems, in the Proceedings of the Twenty Third Hawaii International Conference on System Sciences, Kona, HI (1989).

[6] H. Bhargava, S. Kimbrough and R. Krishnan, Unique Names Violations: A Problem for Model Integration or You say Tomato, I say Tomahto, ORSA Journal on Computing 3, No. 2 (1991) 107–120.

[7] G. Bradley and R. Clemence, A Type Calculus for Executable Modeling Languages, IMA Journal of Mathematics in Management 1, No. 1 (1987) 277–292.

[8] S. Chari, Structured Modeling and Logic, Unpublished Dissertation, University of California at Los Angeles, Los Angeles, CA, 1988.

[9] S. Chari and R. Krishnan, A Logical Reconstruction of Structured Modeling, Working Paper, Decision Systems Research Institute, School of Urban and Public Affairs, Carnegie Mellon University, 1991.

[10] R. Hull and R. King, Semantic Data Modeling: Survey, Applications, and Research Issues, ACM Computing Surveys 19, No. 3 (1987) 201–258.

[11] A. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (1987) 547–588.

[12] A. Geoffrion, Formal Aspects of Structured Modeling, Operations Research 37, No. 1 (1989) 30–51.

[13] A. Geoffrion, Reusing Structured Models via Model Integration, Proceedings of Hawaii International Conference on the System Sciences (IEEE Press, 1990).

[14] A. Geoffrion, SML: A Model Definition Language for Structured Modeling, Working Paper 378, Western Management Science Institute, University of California, Los Angeles, CA, 1990.

[15] C. Jones, Attributed Graphs, Graph Grammars, and Structured Modeling, forthcoming in Annals of Operations Research.

[16] R. Krishnan, Automated Model Construction: A Logic Based Approach, Annals of Operations Research, 21, (1988) 195–226.

[17] R. Krishnan, A Logic Modeling Language for Model Construction, Decision Support Systems 6, (1989) 123-152.

[18] N. Nillson and M. Genesereth (1987), “Logical Foundations of Artificial Intelligence”, Morgan Kaufman Publishers, Los Altos, Ca 94022.

## Appendix A

Consider the simple assignment model shown below.

I: set of resources

J: set of tasks

assign-var(I,J): binary variable whose value is 1 if a resource r in I has been assigned to a task t in J.

cost(I,J): cost of assigning a resource r in I to a task t in J.

MIN sum (I) sum(J) assign-var(I,J) \* cost(I,J)
s.t.

sum(J) assign-var(I,J) ≤ 1 ∀I ... T-avail (availability constraint)

sum(I) assign-var(I,J)=1 ∀J ... T-dem (demand constraint)
