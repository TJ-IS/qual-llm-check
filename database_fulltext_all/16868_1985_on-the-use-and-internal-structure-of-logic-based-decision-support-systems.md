---
otero_id: 16868
otero_key: "8W3WH6BT"
title: "On the use and internal structure of logic-based decision support systems"
authors: "Michael C. Chen; Lawrence J. Henschen"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90240-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the Use and Internal Structure of Logic-based Decision Support Systems

Michael C. CHEN $^{+}$

and Lawrence J. HENSCHEN \*

Department of Electrical Engineering and Computer Science, Northwestern University, Evanston, Illinois, U.S.A.

A general decision support system based on first-order logic with desirable characteristics (for example, being semistructured, supporting, descriptive, effective, and evolutionary) will be presented. The proposed system improves the existing frameworks of Sprague and Bonczek, Holsapple, and Whinston in terms of flexibility and efficiency. A tool called the connection graph is used as a basis for pre-compiling queries for efficient response as well as for modifying pre-compiled queries in response to assumption analyses (such as handling “what-if” questions). Techniques for modifying existing programs derived from the connection graph are described. The notion of determined variables is extended to include the case of process literals. The class of allowable formulas is extended to include condition literals, which may include existential quantifiers.

Keywords: Decision Support Systems; Information Systems; First-order Logic; Databases

![](/api/attachments/8W3WH6BT/fulltext/images/4883d8a4a8b254e5d313e201521d2fdffdfb5c3d9d5da8e698ec76cc2690a27c.jpg)

Michael C. Chen is a member of technical staff at Bell Communications Research, New Jersey. He received a B.S. in Computer Science from National Chiao Tung University, Taiwan, an M.S. and Ph.D. in Computer Science from Northwestern University, Illinois. He held a summer research internship with Honeywell Corporate Computer Sciences Center, Minnesota. His research interests include decision support systems, database management systems, and artificial intelligence

gence.

![](/api/attachments/8W3WH6BT/fulltext/images/a41e164613e6afb218d67053b0561113dbbdaa47e4c25633c56adbcb2e6eabc7.jpg)

Lawrence J. Henschen is Associate Professor of Electrical Engineering and Computer Science at Northwestern University. He received a B.S., M.S., and Ph.D. in Electrical Engineering and Computer Science from University of Illinois at Urbana-Champagne. He published over 30 technical papers in Journal of the ACM, Communications of the ACM, IEEE Transaction on Computer, Automated Reasoning Journal, and Advances in Data Base Theory. His research interests include logic research, and artificial intelligence.

and databases, theorem proving, and artificial intelligence.

\+ Present address: Bell Communications Research, New Jersey.
\* To whom all correspondence should be addressed.

## 1. Introduction

Keen and Scott Morton [1] were the first to present the concept of decision support to management professionals. "Claims" about the benefits and capabilities of Decision Support Systems (herein denoted DSSs) are substantial. A DSS distinguishes itself (among management information systems, data processing systems, and operations research) with five characteristics: (CH1) semistructured as opposed to structured or unstructured; (CH2) supporting rather than replacing; (CH3) descriptive rather than prescriptive; (CH4) effective rather than efficient, and (CH5) evolutionary.

A DSS provides users with various techniques to examine alternative solutions with respect to their models. Table 1 shows the four typical kinds of questions users may want to ask in examining alternative solutions. Each one of four techniques has received attention by DSS builders in industry (for systems such as: Express, IFPS, System W, and Empire for mainframes; Visicalc and Lotus 1-2-3 for microcomputers).

The principal concern of this research focuses on the applications of logic and deduction to Decision Support Systems. In a logic-based DSS, the internal language for representing defined models and queries is a form of mathematical logic called clause form (see [2]). (Of course, the external language, that is the language by which the user communicates with the system can be anything, preferably something close to natural language.) The user-defined models represent combinations of data retrievals from a database and computations via routines in a model library (such as SPSS). Each logic formula represents one possible definition of a new relationship between data items. Such a definition could involve other defined relationships. Responding to a user request involves sorting out all the definitions as well as formulating and executing a sequence of retrievals from the database and calls to the library routines. More detailed discussions of the use of logic will be given below. We assume readers are familiar with [2].

Table 1. Assumption Analyses.

<table><tr><td>Assumption analysis</td><td>Example</td></tr><tr><td>What if</td><td>What is value-x if value-y were different?</td></tr><tr><td>Sensitivity</td><td>How sensitive is value-x to changes in value-y?</td></tr><tr><td>Impact</td><td>What is the impact of value-x? What is the impact on value-x?</td></tr><tr><td>Goal seeking</td><td>How to achieve a goal if value-x were given?</td></tr></table>

The goals of this research are twofold: to outline a logic-based system that would, at least in theory, incorporate desirable features required for decision making (such as being able to handle assumption analyses); and to show feasible, efficient techniques for achieving some of those desired features.

We beg: with a discussion of a general DSS which accommodates the desirable characteristics and improves upon the existing frameworks (mainly Bonczek, Holsapple, and Whinston's [2]). The deficiencies of existing DSSs are pinpointed and explained. We then discuss some technical issues relating to the use of logic and the incorporation of various desirable DSS features into the proposed system. Among these issues are:

\- the extension of the class of logical formulas allowable to include more complicated conditions on the acceptability of answers derived by a logic-based DSS;

\- the determination of optimum orderings for evaluation of defined expressions in response to the user's request;

\- efficient handling of changes to defined models imposed by assumption analyses.

The underlying approach in all our work stems from the idea of compiling the ensemble of definitions into programs that handle each class of the user's requests [3]. In such an approach, the deduction is done before the system is made available to users by systematically analyzing each kind of the user's requests that the system expects to support. We illustrate this below, but the user is referred to [3] for the basic details of such a compiler for databases. Much of the rest of this paper is devoted to the extension of those techniques to logic-based DSSs.

We categorize research on DSSs into two distinct areas. One deals with issues from an organizational behavior point of view [1] while the other deals with issues more toward the aspects of computer science [2,4–8]. This work falls into the second category. Within the aspects of computer science, there are various approaches pursued by researchers, namely: logic and databases [5,6,9]; logic and theorem proving [2]; frame and abstraction [7]; and relational algebra and calculus [4]. The present work is related closely to that of logic and databases. We believe it offers a DSS design which is both more efficient and more flexible than other proposals, and we hope it will be more accessible to non-technical (i.e., non-computer-trained) users. We deem as equally important both aspects of research in this area: the solving of certain major technical problems in designing a DSS and the demonstration that logic is a reasonable language for use by non-technical people for expressing management problems. This work makes significant progress on the first of these.

Much more detail of the technical work described in this paper can be found in [5]. A familiarity with logic is required to understand this paper. A sufficient background can be obtained by reading [2] which presents illustrative examples of how logic is used to represent management information for DSSs. A deep understanding of automated theorem proving or resolution is not required. However, we assume the reader is familiar with logic concepts such as: well-formed formula (wff); clause; literal; resolution [10,11].

## 2. New Proposed System

This section commences with a generic description of the proposed DSS that will guide the remainder of our DSS research. Our generic description views a DSS as having five principal components (see Fig. 1): a Knowledge Representation System; a Database System; a Modeling System; an Assessment and Deduction System; and two Interface Systems.

We now discuss in detail some of the more important functions of the above subsystems. More detailed descriptions of these modules can be found in [5]. The main function of the Knowledge Representation and Dialogue System (KRDS) is to provide a convenient interface between the system and the user. We envision the user language to be something close to natural language, and KRDS will handle the transition between natural language and clause form. In the one direction, KRDS can help the user define models by querying the user about what he/she wants the model to do and developing the appropriate clauses. In the other direction, KRDS can transform information derived by the system back into natural language for output to the user.

![](/api/attachments/8W3WH6BT/fulltext/images/1eb02c17996ef0560373d082f81db1061826376f0ea2c59085a1835a0b5f1d06.jpg)  
Fig. 1. The Proposed Decision Support System.

In the Database System, system designer(s) or user(s) store a set of general rules (e.g., permanent rules for the whole enterprise). In logic-based database systems, this is called the intentional database, IDB. The actual data is stored in the extensional database, EDB, a traditional database. The IDB contains definitions of new relations in terms of EDB relations and other IDB relations. The tuples of IDB relations are not stored, but rather are computed as needed. Thus, queries over relations in the EDB are answered in the normal way while queries over the defined relations of the IDB are resolved through deduction on the formulas of the IDB as well as lookups in the EDB. A tutorial on logic and databases is given in [12] (pp. 3–30 and 149–177).

There are two kinds of models in the proposed system: those which have been coded in some traditional programming language and stored in a library (e.g., SPSS); and those which are defined by the user with clauses. The Modeling System maintains the first kind of model, those that have been programmed in the traditional way as library routines. Note that in the course of using the system, some user defined models (clauses) may be deemed more important than others and may be coded and transferred to the Model System. The reasons for having two kinds of models are: that a large volume of models to be used in a DSS are standard and can be purchased from vendors (and stored in the Modeling System); and that many models will be specific to the enterprise using the DSS and can be set up as clauses much more quickly than they can be programmed in the normal way. Further, as will be noted below, routines in the Modeling System are generally not subject to change; the user must taken them as they are. On the other hand, often a manager wishes to experiment with models, varying the definitions until the desired results are obtained. Models defined as clauses are very easy to experiment with in such a way.

The Assessment and Deduction System is the most complicated component. Among its primary responsibilities is the generation of clauses over the EDB relations to be evaluated in response to the user's queries. The reason for generating these clauses is to allow the user to have the ability to perform assumption analyses. The fundamental techniques for doing this have already been laid down in [3]. Suffice it to say here that query forms (e.g., given values for attributes 1 and 2, find all resulting values for attribute 3) are analyzed vis-a-vis the rules, and programs consisting of sets of evaluable expressions are derived. Because only the form of the query need be known and not actual values, such sets of evaluable expression can be derived ahead of time, before the system is brought up for use. (For example, given the obvious definition of GRANDPARENT(x, y), all queries of the form "find all grandparents of a person A" will be answered in the same way, namely, by finding A's parents and then their parents, regardless of what name is actually given for A.) Various kinds of assumption analyses (e.g., Table 1) and the like will require (temporary) changes to the definitions and consequently changes to these precompiled sets of evaluable clauses. Therefore parts of the compiler may be invoked by the user's requests for altered models.

## 3. On the Use of Logic in DSSs - Review and Critique

## 3.1. Logic and Decision Support System

Bonczek, Holsapple, and Whinston [2] (pp. 69–86 and 358–376) have proposed using logic as a tool for building DSSs. Their clauses define a combination of data retrievals and system routine calls that represent management models. The definition of one such model may also involve other defined models. Logically, a tuple in a relation of a relational database, say $\langle a1,\ldots,a n\rangle\in R$ , represents a logical relationship, namely $\mathbb{R}(a1,\ldots,a n)$ . This relationship is not written as a wff, but rather stored in a different form (in the database) and accessed when needed. In the logic and database literature, this set of tuples (i.e., the traditional database) is known as the extensional database (EDB). Similarly, a function or library system routine represents a relationship between tuples of inputs and the value of the function or output of the procedure. For example, $+(x,y)$ may be viewed as a 3-place predicate, $P(x,y,z)$ , which is true only for tuples such that $z=x+y$ . As with the EDB above, such relationships are not kept as logical formulae, but rather are computed as needed. This approach provides a smooth interface between the database, which would contain typical types of data used by enterprises, and the routines that perform calculations (e.g., regression and benefit/cost analysis).

We illustrate this logic-based approach with a very general example:

If industry practice (or general rule) for situation p is u, and corporate strategy (or user's option) under u is to choose q then management indicator is q.

If management indicator is q for situation p, and the DSS can retrieve data d3 with respect to inputs p and d2 from the database, and Model is run with input data d3 and indicator q with result r then the recommendation for the situation with data p and d2 is r.

A case for this general example is as follows: A product (p) with relatively low market share and high market growth is considered as a ‘problem child’ (u) (CONVENTION(p,u)). Suppose our company’s strategy for such a product is to build market share (q) (OPTION(u,q)). Therefore, whenever our company identifies a product in a position with relatively low market share and high market growth, we would build market share (Indicator(p,q)). From the database, the analyst can find the past history d3 of the product line p in territory d2 (DATA(p,d2,d3)). He/she, with building share in mind, can do a regression analysis on past history (d3) to see the optimal share increase (r) (Model(d3,q,r)). Then, the user will receive the optimal share increase (r) for the product line (p) in the territory indicated (d2) (Recommendation (p,d2,r)).

In terms of first-order logic, the statements above can be translated into two implications, namely:

1. CONVENTION(p,u) ∧ OPTION(u,q)

→ Indicator(p,q)

2. Indicator(p,q) ∧ DATA(p,d2,d3)

$$
\wedge \text { Model } (\mathrm{d} 3, \mathrm{q}, \mathrm{r}) \rightarrow \text { Recommendation } (\mathrm{p}, \mathrm{d} 2, \mathrm{r})
$$

In the spirit of theorem proving, the above two implications (1 and 2) can be translated into clauses as follows:

3. \~ CONVENTION(p,u)

\~ OPTION(u,q) Indicator(p,q)

$$
4. \sim \text { Indicator } (p, q) \sim \text { DATA } (p, d 2, d 3)
$$

$$
\sim \text { Model } (d 3, q, r) \text { Recommendation } (p, d 2, r)
$$

Note that, P → Q is equivalent to \~ P OR Q; here 'OR' is omitted, yielding just \~ P Q. A query of the form 'What is the recommendation for a specific situation in which p='SHOES' and d2='MIDWEST'?' could be issued by a manager. Such a query would be stated as: Recommendation('SHOES', 'MIDWEST',?) → , or in clause form suitable for a theorem prover:

## 5. \~ Recommendation('SHOES', 'MIDWEST',?)

The resolution process of the above three clauses (clauses 3, 4, and 5) yields:

$$
\begin{array}{r l} 6 (4, 5) & \sim \text { Indicator } (^ {\prime} S H O E S ^ {\prime}, q) \\ & \sim \text { DATA } (^ {\prime} S H O E S ^ {\prime}, ^ {\prime} M I D W E S T ^ {\prime}, d 3) \\ & \sim \text { Model } (d 3, q,?) \end{array}
$$

$$
\begin{array}{r l} & 7 (3, 6) \sim \text {CONVENTION} (^ {\prime} \text {SHOES} ^ {\prime}, \mathfrak {u}) \\ & \quad \sim \text {OPTION} (\mathfrak {u}, \mathfrak {q}) \\ & \quad \sim \text {DATA} (^ {\prime} \text {SHOES} ^ {\prime}, ^ {\prime} \text {MIDWEST} ^ {\prime}, \mathfrak {d 3}) \\ & \quad \sim \text {Model} (\mathfrak {d 3}, \mathfrak {q},?) \end{array}
$$

For a complete treatment of resolution, see [10,11].

Recalling that the EDB and model information are not stored as logical wffs, resolving a negative literal like \~DATA(A,B,d3) is avhieved by a database lookup, namely find value(s) for d3 such that (A,B,d3) is in the relation DATA. Similarly, given value for inputs d3 and q, resolving against a negative literal \~Model(d3,q,r) is achieved by actually calling the library routine Model with inputs d3 and q and then instantiating r with the output value. An important point, first noted by Reiter [13,14], is that the normal resolution process can be separated from these lookup/calculate resolutions and, in fact, can be done first. Thus, in DSS applications, the goal of the theorem prover is to produce a clause with only evaluable literals, that is, literals corresponding to data retrieval from the EDB or calculation by library routines. In the present example, CONVENTION, OPTION, and DATA can be determined by database lookup and Model can be handled by calling the corresponding library routine. Thus, a clause like 7 can (only) be reduced to empty by appropriate data retrievals and model evaluation. Such a clause is called an evaluable clause.

## 3.2. Critique of Systems Based on Theorem Proving and PROLOG

Bonczek, Holsapple, and Whinston view a DSS as having three principal components: a language system (LS); a knowledge system (KS); and a problem-processing system (PPS) [2]. The logic-based PPS is treated as a kind of theorem-proving system [10] in which the user's query is taken as a theorem that is to be proved from the existing axiom set; i.e., rules, data, and functions.

To respond to model evaluation requests (i.e., the statement of the goal), the theorem prover repeatedly searches for and derives definitions of requested models until a formula consisting only of data retrievals and calls to system routines is obtained.

PROLOG has also been suggested for use in DSSs [8] (pp. 37–45). The 'claims' are that PROLOG offers easily extensible features needed for DSSs. The Japanese have chosen it for their fifth-generation computers [15].

Both proposals involve the use of deduction to search for answers at the time the query is issued by the user. This approach has four serious drawbacks:

(1) Unlike the method to be presented below (Section 5), it involves the use of considerable deductive computation at query time, including the simple clerical overhead of finding potentially resolvable literals and calculating the resolvents, to the more serious problem of search. When the clause sets are relatively simple, this may not introduce much delay; but we can envision a considerable delay while PROLOG or a theorem prover performs its search for answers in a system with several thousand clauses.

(2) Because most such systems solve goals in a particular order, there will be a great many problems in which an incredible amount of redundant data retrievals will be performed. For example, in one formulation of the definition of ancestor, finding the ancestor of Evon would involve first finding and printing Evon's parents, then starting fresh and finding Evon's parents and their parents and printing those names, then finding Evon's parents again,...,etc. Such redundancy is factored out in the method below.

(3) In cases where all answers are required and there are recursive definitions, it is not clear that a termination condition can be given for an ordinary deductive search. Again, the method below guarantees termination.

(4) While PROLOG at least can be fixed up to handle most of these objections, to do so requires both extensions to PROLOG and the inclusion of more control information into the clauses that make up the definitions themselves. While extending PROLOG may be reasonable, we do not think it is in the spirit of logic-based DSSs to require (non-technical) users to have to learn how to embed control information into definitions. The whole point of non-procedural languages is to eliminate that need from the user.

## 4. Literal Evaluation

Our discussion in this section focuses on individual literal and clause itself. We show the evaluation criteria of a clause in Section 4.1. In Section 4.2, we describe a new kind of literal which allows for an extension to the kind of formulas previously allowed in logic-based databases and DSSs by allowing the limited use of existential quantifiers.

We classify literals into four categories: (1) process literals (P) such as Model; (2) data retrieval literals (R) such as DATA; (3) deduction literals (D or D') such as Indicator; and (4) condition literals (C\*) such as Highpay\* to be discussed in Section 4.2.

## 4.1. Determined Variables

In order for a clause to be evaluated, due consideration must be given to the input requirements of both the process and data retrieval literals as well as to the order of evaluating these literals. It is not always appropriate to evaluate all data retrieval literals first, as originally proposed in [2]. Consider clause 8:

$$
\begin{array}{r l} 8. & \sim P 8 (x, y) \sim R 8 (x, z) \sim P 9 (w, z) \\ & \sim R 9 (w, v) D 8 (y, v) \end{array}
$$

where P8 and P9 are process literals, with inputs x and w respectively, R8 and R9 are database relations, and D8 is a deduction literal. Suppose the user requests the proposed DSS to evaluate D8(?,K), i.e., let v = K and find values for y. Clearly the proposed DSS (particularly, the Assessment and Deduction System) cannot begin by evaluating P8(x,y), as in clause 8 above, because the Assessment and Deduction System does not have a value for x yet. The appropriate order for evaluating clause 8 is to use K to select values for w from relation R9, then to call process P9 with each of these values to obtain values for z, then to select values for x from R8, and finally apply P8 to each of the x-values. These remarks lead to a natural extension of the notion of determined variables in [3]. We say that, for a given request, the variables in the positive literal that receive values from the user's request are determined. If any variable in a data retrieval literal is determined, then all the remaining variables in that literal are determined. The rationale is that if any subset of attributes are specified, then a retrieval from that relation will yield a reasonable set of values for the remaining attributes. If all the input variables of a process literal are determined, then the output variables in that literal are determined. (Note that if some of the output variables of a process literal, P, are also determined by another literal of the clause, this represents a condition on the acceptance of values generated by P.) In order for a base clause, i.e., a clause with only data retrieval, process, and condition literals (see next section), to be evaluable in a given situation, all of its variables must be determined.

The notion of input variables may now be extended to the deduction literals. For a given clause with positive literal Ded(x1,...,xn), any minimal subset M of {x1,...,xn} such that providing values for all variables in M (i.e., if all these variables are determined) determines all the remaining variables in the clause is called an input set for this clause (i.e., for this definition of Ded). For clause 8, {v} is an input set but {y} is not. Clearly, the notion of determined variables may now also be extended to a clause containing deduction literals in its body by treating those as process literals and requiring some input set of each such literal to be determined. One can guarantee inductively that every base clause generated by resolution from a user request will be evaluable if the following restrictions are enforced.

(E1) Every clause must have at least one input set for its positive literal.

(E2) A user request is linked to a clause only if this request provides value(s) for some input set of the clause.

## 4.2. Condition Literals

In prior work on logic and databases, there were literals that contributed answers (data retrieval literals and, in our extension, process literals) and deduction literals (or defined relations in [3]). We have found the need for literals that do not contribute new values but rather serve as filters for tentative answers. These are literals all of whose variables are determined and represent tests that the proposed values must satisfy to be accepted as answers. While such literals do not appear to be required in most simple database applications using deduction literals (or defined relations), they appear to be quite natural and useful for DSSs. Some simple constraints can be handled easily in the normal way. For example, suppose we define a predicate, MajorDept, as a department with sales greater than \$1M. Using the relation DEPT(dept,sales) as an extensional relation, we could write:

$$
9. \sim \mathrm{DEPT} (x, y) \sim (y > 1 M) \text { MajorDept } (x)
$$

Then a query form like, 'Is Department D a major department?' (\~ MajorDept(D)) would yield the program:

$$
1 0. \sim \mathrm{DEPT} (\mathrm{D}, \mathrm{y}) \sim (\mathrm{y} > 1 \mathrm{M})
$$

which can be evaluated by looking up Department D's sales and comparing to \$1M. The later is performed like any other process literal evaluation.

However, consider now the condition that a department is major if its sales are greater than \$1M and all its employees earn annual income over \$30K. In full first-order form, we could write:

$$
1 1. \text {   FORALL   } x, y \{\text { DEPT } (x, y) \land y > 1 M
$$

$$
\wedge \operatorname{Highpay} ^ {*} (x) \rightarrow \operatorname{MajorDept} (x) \}
$$

and

$$
\begin{array}{l}1 2. \text { FORALL } u \{\text { FORALL } y, z [ \text { EMP } (u, y)\\\wedge \text { SAL } (y, z) \rightarrow z > 3 0 K ] \rightarrow \text { Highpay } ^ {*} (u) \}\end{array}
$$

However, in attempting to convert wff 12 to clause form, the FORALL y and FORALL z become EXIST y and EXIST z, for the → half of the definition of Highpay\*, which causes major problems for most aspects of logic-based DSSs and databases. (See [3] or [13] for discussions of why existential quantifiers are difficult to handle.) In this case, however, the intended use of the predicate Highpay\* allows a new kind of special handling to be described below. The important point here is twofold:

(1) We have discovered a new class of literals (condition literals) to be included in the logical representation of databases and decision-support problems; and

(2) This condition literal can significantly expand the kinds of formulas being used in DSSs.

We now consider clause 11 above in detail. The clause form is:

$$
1 3. \sim \mathrm{DEPT} (x, y) \sim (y > 1 M)
$$

$$
\sim \text { Highpay } ^ {*} (x) \text { MajorDept } (x)
$$

For the query form \~ MajorDept(D), the resolvent is:

$$
1 4. \sim \mathrm{DEPT} (\mathrm{D}, \mathrm{y}) \sim (\mathrm{y} > 1 \mathrm{M}) \sim \text { Highpay } ^ {*} (\mathrm{D})
$$

Thus, we see immediately the feature that will allow clause 12, the definition of Highpay\*, to be handled; namely, Highpay\* is intended to be used for specific values of u as opposed to being used to retrieve a value for u. In effect, Highpay\* is intended to answer only TRUE or FALSE. Leaving the quantifiers over x and y for the moment, and setting u to D in anticipation of resolving with clause 12, we have

$$
\begin{array}{l}1 5. \left\{\text { FORALL } y, z [ \text { EMP } (D, y) \wedge \text { SAL } (y, z) \right.\\\rightarrow z > 3 0 K ] \leftrightarrow \text { Highpay } ^ {*} (D) \}\end{array}
$$

Now, since we are only interested in the truth or falsehood of Highpay\*(D) and since FORALL y,z[EMP(D,y) ∧ SAL(y,z) → z > 30K] is a perfectly good (closed) relational expression, we could simply ask the database (which we assume can evaluate arbitrary relational expressions, i.e., is relationally complete) to evaluate FORALL y,z(EMP(D,y) ∧ SAL(y,z) → z > 30K). Notice the difference in usage between a condition literal and an ordinary defined relation or model. In the ordinary case, evaluation of the expression on the left of the → may be requested in cases where this expression is not closed with the intent to use values of the free variables as answers. Further, this expression may involve other defined predicates. Such a request may involve the use of general theorem proving in full first-order logic; hence the restriction in logic and DSSs is to have function-free clause form (i.e., no existential quantifiers in the Prenex Normal Form of the rules [10,11]). In the case of a condition literal, the expression to be evaluated is closed and normally should contain no other defined literals (except possibly other condition literals).

To summarize, a condition literal is a literal $C^{*}(x1,\ldots,xn)$ all of whose variables are determined by other literal(s) for each occurrence and for each query form supported. Further, if it is defined, the definition must be of the form:

$$
1 6. \text {   FORALL   } x 1, \dots , x n [ W (x 1, \dots , x n)
$$

$$
\leftrightarrow C ^ {*} (x 1, \dots , x n) ]
$$

where x1,...,xn are the only free variables in W(x1,...,xn). During the compilation process, resolution is not applied to W(x1,...,xn). Rather, the condition literal is simply marked and linked as part of the evaluable clauses generated by the compiler. When such a marked literal is encountered in evaluating a clause in response to a user query, the definiens is instantiated with the already retrieved values, say (a1,...,an) for (x1,...,zn), and the closed expression W(a1,...,an) is sent to the Database System.

## 5. Compiling Process

We describe here (by example) an alternative approach known as compiling queries [3]. This approach does make use of a theorem prover, but in a highly specialized way which can be done before users are allowed on the system. It is based on an analysis of generic query forms and generates sets of evaluable clauses form which all answers to a query can be obtained. There need be no deduction when the user actually issues a request. The reader is referred to [3,5] for full details.

## 5.1. General Procedure of Compiling

To see how this might be possible, consider again the general example of Section 3.1 represented by clauses 3 and 4. Suppose we consider a generic query form, say 'How should values for r be derived given values for p and d2 in clause 4?' Suppose we use dummy constants, A and B, for the given values. Clearly, the analogous resolutions can be made yielding clause:

$$
\begin{array}{r l} 1 7. & \sim \text { CONVENTION } (A, u) \sim \text { OPTION } (u, q) \\ & \sim \text { DATA } (A, B, d 3) \sim \text { Model } (d 3, q, r) \end{array}
$$

Now, when the request above, namely, 'Find r when A is 'SHOES' and B is 'MIDWEST' is given, we merely evaluate clause 17 with 'SHOES' and 'MIDWEST' substituted for A and B, respectively. Of course, clause 17 could be used for other requests of the same form as well; e.g., 'Find r for 'COMPUTER' and 'EAST'.

We now give brief indication of what is involved in forming the set of evaluable clauses for a generic query form. First, the set of all clauses is formed into a connection graph, with pairs of resolvable literals linked together. For example: Fig. 2 shows a recursive connection graph; Fig. 3 shows a non-recursive, tree-like connection graph; Fig. 4 shows a connection graph with two queries attached to it. Note, data retrieval and process literals are not linked because they are handled by look up and evaluation rather than ordinary resolution. Next, each query form is linked temporarily to the connection graph and all potential paths of resolution are explored. Those yielding evaluable clauses are saved. In case the graph has no cycles, exploring all paths is tantamount to searching a finite tree. In case there are cycles (which represent recursive definitions) the techniques in [3] can be applied. Note that in exploring potential resolution paths, the dummy parameters of the query forms are allowed to 'conditionally' match with other constants. For example, consider the query form, 'Find all suppliers of a given product' in the presence of the two rules, 'Every manufacturer of a product supplies that product' (clause 18) and 'Any hardware store supplies nuts' (clause 19).

18. \~ MFG(x,y) Supply(x,y)

$$
1 9. \sim \text { HARDWARE } (z) \text { Supply } (^ {\prime} N U T S ^ {\prime}, z)
$$

$$
2 0. \sim \text { Supply } (A,?)
$$

Two potential resolution paths are possible: \~ MFG(A,?) (clauses 18 and 20) and \~(A='NUTS') \~ HARDWARE(?) (clauses 19 and 20). Note the conditional nature of the second one. If these were the only rules in the system about suppliers, then all answers to any query of the given form could be obtained by evaluating the two clauses above, that is, by finding all manufacturers of the product and by finding all hardware stores if the product were NUTS.

![](/api/attachments/8W3WH6BT/fulltext/images/140d5bb7ed88c91bfbeba725774955259ad4a19fb13d778104aa7b3ccd71be97.jpg)  
Fig. 2. The Connection Graph 1.

![](/api/attachments/8W3WH6BT/fulltext/images/384ba2f825768caa04d93c7b6b80b27f6c6b62e2e99369462a309fe6847104f0.jpg)  
Fig. 3. The Connection Graph 2.

Finally consider a recursive example, the definition of subordinate (clauses 21 and 22) and a query: 'Find all subordinates of a given person' (clause 23).

21. $\sim$ BOSS(x,y) Sub(y,x)

$$
2 2. \sim \text { BOSS } (u, v) \sim \text { Sub } (w, v) \text { Sub } (w, u)
$$

23. \~ Sub(?,A)

The graph for this set of clauses has cycles because subordinate is recursive. While it is beyond the scope of this, brief review to give the details, [3] shows how to produce a sequence of evaluations (data retrievals) to answer such a query. In fact the program produced by [3] is the obvious one desired:

![](/api/attachments/8W3WH6BT/fulltext/images/3791c241b0a230d73bfdcbf90ff8fb7a7a456d31f7e7b24555d2c17371f4659b.jpg)  
Fig. 4. The Connection Graph 3.

(1) Find anyone for whom A is a boss,

(2) For each person x from step 1, find all the people for whom x is a boss, and

(3) Perform step 2 until no more retrievals are possible.

A major difficulty, to be addressed in later sections, is that a typical use of a DSS involves making temporary changes to rules and/or data in order to perform 'what-if' types of analyses. Such changes to the data and clauses could affect the precompiled programs for some of the generic query forms. We show below that such changes can be handled without losing the other benefits of the compiling approach.

## 5.2. Handling Assumption Analyses

It is the desire to perform assumption analyses on existing solutions that requires changing a literal (or a node) inside the connection graph. We show some examples to illustrate these changes. Suppose a manager were using a DSS with a rule:

## 24. $\sim \mathbf{P} \sim \mathbf{R} \sim \mathbf{D}' \mathbf{D}$

After running the DSS for a query $\sim$ D, he might wonder what the effect would be if $\sim$ P were replaced by a different process literal, say $\sim$ P". For example, P might be a linear programming model, P" an integer programming model, and he might wish to know how sensitive the answer was to the integer programming model. This experiment would be done using the modified rule:

## 25. $\sim \mathbf{P}''\sim \mathbb{R}\sim \mathbf{D}'\mathbf{D}$

In a similar vein, he might wish to try the same query with a different defined model, say $\sim$ D" or with data from a different table in the database, $\sim$ R". He might wonder how many of the answers would not have been given if an extra condition literal had been placed on answers, i.e., if he used the rule:

$$
2 6. \sim \mathrm{P} \sim \mathrm{R} \sim \mathrm{D} ^ {\prime} \sim \mathrm{C} ^ {*} \mathrm{D}
$$

Alternatively, he might wish to examine the effect if data in the database were different, for example, if sales last year had been \$15M instead of \$10M.

This is a different situation because it does not require changing any rules (although for reasons explained below, we will treat it as such). If the manager likes the results he sees, he may wish to make these changes permanent. On the other hand, having tried the experiment he may wish to go back to the original forms. Finally, he may wish to try the changes only for some queries (i.e., local change) or try them for all queries that use the given rule (i.e., global change). Each of these kinds of changes may invalidate some of the compiled programs. If the system had to stop and be recompiled for each such request, this approach to logic-based DSSs would lose most of the advantages cited in Sections 3 and 5.1. We give below a solution which allows efficient handling of the above kinds of changes required for assumption analyses and the like. This technique allows the system to isolate the changes required and perform them efficiently.

## 5.3. Handling Changes

Given the motivation above, we now discuss what is required when a user asks for a change. There are two areas that need attention: (1) the maintenance of the connection graph itself; and (2) the necessary modifications to precompiled programs. In the discussion that follows we will concentrate on modification to a single program, but the reader should remember that corresponding changes should be made to all programs that make use of an altered clause.

Concerning the connection graph, the maintenance is relatively simple. If the change involves either the addition or deletion of a $\sim$ D' literal, then the structure of the graph will change. As noted above, $\sim$ P, $\sim$ R and $\sim$ C\* literals do not involve links in the graph, so additions and/or deletions of such literals cannot alter the structure of the graph. Thus, whenever a negative literal is changed, the clause itself is changed in the obvious way and, if necessary, links are added or deleted. It may also be desirable to maintain other information about the graph and the clauses in it, like the numbers of literals of each kind in a clause, and this information can also be easily updated for each addition/deletion/modification. We remark that changes involving $\sim$ D' literals can transform non-recursive definitions into recursive ones and vice-versa. It is necessary to determine if this occurs in order to make the appropriate modifications to the precompiled programs as noted above. Finally, although it is unlikely that +D literals would be changed without corresponding changes in \~D literals, it is possible, and the above remarks apply equally well.

As to modifications to the programs, the main considerations are what are the types of the old and new literals and what are the structures of the old and new definitions. Suppose we have a program that uses a clause, and that a negative literal in the clause is changed to a different literal. First, the old literal and its descendants if any must be removed. If the old literal is a \~ P, \~ R or \~ C\* literal and this literal actually appears in the program, then it must be removed. If the old literal is a \~ D' literal, it does not appear in the program, but literals from other clauses will have been added to the program through the resolution process applied to the deleted \~ D' literal. These literals can be identified by the same analysis as that which led to their inclusion by the compiler, basically just tracing out the resolutions from \~ D' and deleting the \~ P, \~ R and \~ C\* literals that had been added. The exact reverse remarks apply to the new literal. If it is one without a link, it is simply added to the program, otherwise the resolution process must be applied.

In cases where the old or new literal is $\sim D'$ literal, the tracing process must take into account whether or not there is recursion. For example, if a $\sim D'$ literal is deleted from a recursive cycle, the tracing process stops at the end of the cycle, just as the original compiling process does (see [3]). Similarly, if the new literal is of the form $\sim D'$ , then the system must determine if the modified clause occurs in a cycle or not. Whichever is the case, the corresponding compiling process is applied starting from the new $\sim D'$ literal. In all cases, the resulting expressions in the new program form may have to be analyzed again to determine the proper order of evaluating the $\sim P$ and $\sim R$ literals, as described in Section 4.1.

We illustrate the above with some simple examples. Consider the graph in Fig. 2. If we change \~ P2 in clause 28 to \~ D10, then clearly any program that used clause 28 should no longer have the literal \~ P2, but rather the literals that are obtained by resolving \~ D10 wherever it can resolve. In Fig. 2, \~ D10 resolves only with clause 36, so all those programs should have the literal \~ P10 added. Note that this change does not break any old recursion or introduce any new recursion. Next consider changing \~ D2 in clause 28 to \~ R11. In this case, the cycle consisting of clauses 27, 28, 29 and 30 is broken. Of course, as in the previous examples, the literals from clauses 29 and 30 should be removed from the corresponding programs. But also the program format should be changed. The old program would have included iteration to account for the recursion (see [3]). The new program should not be iterative. In fact, the new program will consist of \~ P1, \~ R1, \~ P2, \~ R2, and \~ R11. Consider the graph in Fig. 3. If we change \~ D2 in clause 37 to \~ R11, then any program that had depended on clause 37 would have contained literals \~ P2, \~ P3, and \~ P4 (because of resolution on \~ D2 with clause 38 and \~ D3 with clauses 39 and 40) as well as literal \~ R6 (because of resolution on \~ D2 with clause 42). These should all be replaced by \~ R11.

To summarize, the required transformations of programs hinges on two pairs of criteria: (1) what kinds of literals are the old and new literals; and (2) what forms are the old and new graph. Each case has its own requirements which mimic directly the steps the compiler did/would take to process the corresponding graph. The full details of the algorithm as well as proofs of completeness and correctness can be found in [5]. The techniques for adding or deleting whole clauses as opposed to changing literals are directly analogous to the above.

## 5.4. Allowable Literal Transformations

Most changes involving literals in clauses are meaningful in a DSS. For example, changing a negative literal to another negative literal means that the user wants to try a different definition of the positive literal, as in the 'linear-vs-integer' example earlier in this section (clause 25). The user might wish to add or delete constraints, as in the 'major department' example in Section 4.2. The user might even request a change in the positive literal in a clause. For example, if the rule:

$$
5 4. \sim \mathrm{R1} (\mathrm{x}, \mathrm{y}) \sim \mathrm{R} (\mathrm{y}, \mathrm{z}) \mathrm{D1} (\mathrm{x}, \mathrm{z})
$$

were present, the user might want to make the values for y appear as well, thus requesting that the rule be changed to:

$$
5 5. \sim \mathrm{R1} (\mathrm{x}, \mathrm{y}) \sim \mathrm{R2} (\mathrm{y}, \mathrm{z}) \mathrm{D1} (\mathrm{x}, \mathrm{y}, \mathrm{z})
$$

Of course, one would normally expect the corresponding change to all the negative occurrences of D1 connecting to clause 55 as well. The reader can easily imagine situations where each of the kinds of literal transformations listed in Table 2 might be useful. In this table, we show the types of transformations we believe make reasonable sense. For example, we allow a process literal to be changed to a data retrieval literal but do not allow a positive literal (i.e., D literal) to be removed from the clause containing that positive literal. Throughout the text, we denote $\langle X,Y\rangle$ as a change of literal from literal type X to literal type Y.

Why don't other kinds of literal transformations make sense? The reasons are as follows: $\langle D, \bot \rangle$ , $\langle D, P \rangle$ , $\langle D, R \rangle$ , and $\langle D, D' \rangle$ yield negative clauses which will never be used in resolution or as a part of any program. In essence, these changes are not practical. $\langle \bot, D \rangle$ , $\langle P, D \rangle$ , $\langle R, D \rangle$ , and $\langle D', D \rangle$ will bring one more positive literal into the clause. This introduction violates our restriction to Horn clauses [14]. A condition literal has a value of either TRUE or FALSE. Except the constraint literal itself, none of the literals has the same property that literal $C^*$ has. Therefore, literal transformations like $\langle P, C^* \rangle$ , $\langle R, C^* \rangle$ , $\langle D, C^* \rangle$ , $\langle D', C^* \rangle$ , $\langle C^*, P \rangle$ , $\langle C^*, R \rangle$ , or $\langle C^*, D' \rangle$ are not legal.

Recalling the remarks of Section 5.3, we identify five classes of literal transformations -

class 1: $\langle P, P \rangle$ , $\langle R, P \rangle$ , $\langle P, R \rangle$ , $\langle R, R \rangle$ , and $\langle C^*, C^* \rangle$ ; class 2: $\langle P, D' \rangle$ and $\langle R, D' \rangle$ ; class 3: $\langle D', D' \rangle$ ; class 4: $\langle D', R \rangle$ and $\langle D', P \rangle$ ; class 5: $\langle D, D \rangle$ .

The distinguishing features of these classes is whether or not the deletion is simple and whether or not the addition is simple. We have shown by examples in the previous section how the first four classes are handled by our DSS. For the last class, there are two possibilities. First, all the corresponding negative D literals could be modified in the corresponding way as discussed earlier in this section. In this case there is no structural change to the graph and no additions or deletions of literals from the programs. There may be some minor changes to the programs required in order to account for the different number of variables; for example, additional variables may need to be included in print statements. The other possibility is that the user does not request the corresponding negative literals to be changed. We do not allow such changes because such a change has the potential of leaving all those negative literals undefined.

Table 2. Allowable Change of Literals

<table><tr><td></td><td>to from</td><td>Empty (⊥)</td><td>~ P</td><td>~ R,</td><td>~ D&#x27;</td><td>D</td><td>~ C*</td></tr><tr><td>1</td><td>Empty (⊥)</td><td>-</td><td>yes</td><td>yes</td><td>yes</td><td>no</td><td>yes</td></tr><tr><td>2</td><td>~ P</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td><td>no</td><td>no</td></tr><tr><td>3</td><td>~ R</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td><td>no</td><td>no</td></tr><tr><td>4</td><td>~ D&#x27;</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td><td>no</td><td>no</td></tr><tr><td>5</td><td>D</td><td>no</td><td>no</td><td>no</td><td>no</td><td>yes</td><td>no</td></tr><tr><td>6</td><td>~ C*</td><td>yes</td><td>no</td><td>no</td><td>no</td><td>no</td><td>yes</td></tr></table>

Note that we do not allow the simple deletion of the positive literal of a clause, i.e., $\langle D, \bot \rangle$ is not allowed. This makes semantic sense since the result would be a clause which does not define anything. A side benefit is that this insures that every clause in the EDB, IDB, and model base has at least one positive literal. This implies, in turn, that the whole system will always be logically consistent, so that we need never worry about reasoning from inconsistent hypotheses.

## 5.5. Local versus Global Changes

It is likely that a change in one clause will have a ripple effect on others. In our DSS, the ripple effect might happen when there are several answers to different queries referring to a same set of clauses; Fig. 4 in Section 5.1 shows how this is possible. Both queries A and B refer to the set of clauses labeled Z. Should we make any change in Z (such as change \~ D10 of clause 51 to \~ D9), answers to both queries A and B will be affected. We call this change a global change. On the other hand, if we wish to restrict the change inside set Z to only query A, an old and a modified set Z will have to be maintained in order to avoid the ripple effect to query B. Such a change to only one of the referring programs is called a local change. Notice that there are two clauses (46 and 48) in set X that refer to clause 51 in set Z.

Now if a user specifies that \~ D10 of clause 51 is to be changed to \~ D9 only for query A, the resulting connection graph will require separate copies of clause 51, one of which will then be modified. The unchanged clause 51 will be connected to clause 49 as before, the modified one, say clause 56, is connected to clauses 46 and 48 (see Fig. 5). Note that the system must prevent clause 49 from linking to the new clause 56, even though the literals D8 are unifiable. Similarly, it should also prevent clauses 46 and 48 from linking to clause 51. In other words, there should not be a linkage between literal \~ D8 in clauses 46 as well as 48 and D8 in clause 51 nor between literal \~ D8 in clause 49 and D8 in clause 56.

![](/api/attachments/8W3WH6BT/fulltext/images/c8f73df64be1138a7aa74e41f87eb2e7706ccf24e58d1f842182994df2a1056c.jpg)  
Fig. 5. The Connection Graph 4.

## 5.6. Temporary Changes to Database

Certain kinds of ‘what-if’ questions involve temporary changes to data in the database as opposed to changes in the rules. An example is, ‘What if sales last year were \$15M instead of \$10M?’. If the DSS, especially the Database System, were being used by only one person, then of course the system could simply alter the database. In a multi-user system, however, this is not desirable since other users would then temporarily have an incorrect view of the data. An alternative in this situation is to make a temporary copy of the database, but this is out of the question for any sizable database.

We propose to alter the programs using the temporarily modified database relation instead of doing anything to the database. Thus we handle the situation almost as if it were an $\langle R,D'\rangle$ change with the exception that the effects on the structure of the connection graph and related programs are small and quite well defined, leading to simplified techniques.

For example, suppose we wanted to temporarily assume the sales of the company for 1984 were different from the actual sales. (Say, if the sales of year 1984 had been y dollars, what would the company's per-share net have been?) We could make a new temporary defined relation, Temp-sales, and add the following two clauses to the Assessment and Deduction System:

$$
5 7. \sim (x = 1 9 8 4) \sim \text { PROMPT } (x, y) \text {   Tempsales } (x, y)
$$

$$
(\text { or   } 5 8. x = 1 9 8 4 \land \text { PROMPT } (x, y)
$$

$$
\rightarrow \text { Tempsales } (x, y))
$$

$$
5 9. \sim (x \neq 1 9 8 4) \sim \text { SALES } (x, y) \text { Tempsales } (x, y)
$$

$$
(\text { or   } 6 0. x \neq 1 9 8 4 \land \text { SALES } (x, y) \rightarrow \text { Tempsales } (x, y))
$$

Clause 57 (or 58) is a condition that if x is 1984 then Tempsales is whatever hypothetical sales (y) the user enters (PROMPT). (Alternatively, we could build the temporary change into the rule directly, for example, x=1984 → Tempsales-(x,\$15M).) Clause 59 (or 60) says that if x is any other year, then Tempsales is the same as SALES. Literals PROMPT and SALES are data retireval literals. Literal Tempsales is a deduction literal. Conceptually, we may now think of all references in the rules to SALES being changed to Temp4-sales. Therefore, the change has the form ⟨R,D′⟩. If we now suppose that Tempsales were used in the input of models everywhere that SALES had been used before (which can be accomplished by replacing SALES by Tempsales without making a separate copy of SALES), then queries would in effect have used the modified database. Thus we have avoided copying the database and still provided the capability for temporary changes to the database at the internal level. Note, this also involves changing all clauses referring to SALES, which is a uniform global change and our DSS could handle it. Moreover, a temporary change to the database does not really change the structure of a connection graph, i.e., it neither produces nor cuts a recursive loop.

As for the effect on already compiled programs, the required changes are particularly simple. If Tempsales were substituted everywhere for SALES in the set of clauses, then all references in the existing compiled programs would instead have referred to the deduction literal Tempsales. Of course, during the compilation process, these would all have been eliminated in favor of the resolvents with the above two clauses (clauses 57 and 59). In every case, the resulting two expressions denote that a hypothetical sales should be used if year is 1984 and the data inside the database should be used otherwise. To facilitate this temporary change, we use the tables to locate all the occurrences of SALES in all of the compiled programs.

## 6. Concluding Remarks

## 6.1. Evolutionary Nature

Many researchers, practitioners, and managers [1,8,16,17], consider evolution as one of the most important factors for successful DSS development. The reasons drawn from the case studies and literature review can be stated as follows:

(1) Requirement analysis of intended usage is an open ended process. The designers or users either lack the knowledge necessary to lay out the requirements or feel that such requirements can never be made.

(2) Successful development depends upon a flexible design approach which permits fast modification and smooth implementation.

In Section 5, we have offered a technology that achieves a high degree of evolutionary capability. In addition, our approach accommodates other design frameworks (like IBM's top-down approach, Ness' middle-out approach [16] (pp. 26–37), Sprague's three level technology [17], and the software life cycle concept) and yet provides a flexible design tool in which making various changes is possible.

## 6.2. Future Research

We believe logic-based DSSs will prove vastly superior to special purpose systems and even DSS Generators [17]. A logic-based DSS will be able to process all kinds of models relating to the various types of decisions made by managers because logic itself can express such a wide variety of concepts and definitions. Furthermore, this logic-based approach to building DSSs can accommodate the underlying frameworks of commercially available systems (labeled DSSs). The conceptual framework for all these systems (i.e., proposed DSS components) as well as simple database operations will be the same uniform, simple, and well-understood language – first-order logic. Thirdly, the underlying processes – forming the connection graphs, evaluating clauses, ..., etc. – are the same in all cases. Finally, we believe managers and non-technical users can, with but a modest exposure to logic, write their own definitions and models with the help of a user-friendly natural language interface; such is normally not the case with a ‘traditional’ DSS where knowledge of some programming language or the technical details of some system are required. This gives managers much greater flexibility to explore alternatives by trying different models, thus putting the full power and flexibility of the DSS directly into the hands of the people who need to use it.

Mainly because of the complexity of the problem, this paper concentrates only on one of the five DSS components, the Assessment and Deduction System. We offer below further potential for research in this and other aspects of logic-based DSSs.

(1) Knowledge representation itself is critical to the development of logic-based DSSs. This representation problem brings us to the issue where research on knowledge engineering is focused. In particular, we suggest that several different logic-based DSSs in different areas be developed and experimented with as an initial step in the direction of knowledge engineering and DSSs.

(2) The Assessment and Deduction System itself should be able to learn as the user learns and accumulate this learning in a form (e.g., a set of formal rules or axioms) representable in the Database System. Learning means the Assessment and Deduction System is more knowledgeable in terms of supporting aid in the user's problem domain. In essence, the DSS evolves or adapts. Thus the rudiments of evolution (or adaptability) are evident at this point. Suggestions of such capability have been posed by researchers in DSSs [16] (pp. 164 and 178). Research in this area includes investigating the kinds of things that the Assessment and Deduction System could learn.

(3) Two problems dealing with data inside the clause need to be addressed. One is data aggregation inside the clause, the other is data passing among literals of various kinds. For example, can we handle variables inside the clause in the form of vectors? Solution to these two problems will help our logic-based DSS integrate with additional software packages, e.g., SPSS with its myriad of parameters.

(4) Eventually, we would like to have a DSS which can ask questions. On the one hand, such a DSS could help the user conduct various kinds of assumption analyses. On the other hand, it could caution the user when the user neglects to make his point.

## Acknowledgements

We would like to acknowledge the financial support from the National Science Foundation under grant number: MCS-8306637 (1983–1984). Early investigation of this research was done while the first author was with Honeywell Corporate Computer Sciences Centers (summer 1983).

## References

[1] Keen, P.G.W. and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Cambridge, MA (1978).

[2] Bonczek, R.H., C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, NY (1981).

[3] Henschen, L.J. and S.A. Naqvi, On Compiling Queries in Recursive First-Order Databases, J. ACM 31 (1984) 47–85.

[4] Blanning, R.W., A Relational Framework for Model Management in Decision Support Systems, in: Trans. 2nd Int. Conf. Decision Support Systems, G.W. Dickson (ed.), pp. 16–28, San Francisco, CA (June 14–16, 1982).

[5] Chen, M.C., On The Use And Internal Structure of Logic-based Decision Support Systems, Doctoral Dissertation, Northwestern University, Evanston, IL (June 1984).

[6] Henschen, L.J., M.C. Chen, J. Fedorowicz, A. Rangaswamy, and A. Pantziris, Logic-based Decision Support Systems: Some Remarks on Implementations, Proc. IEEE Workshop on Languages for Automation, pp. 277–281, Chicago, IL (Nov. 7–9, 1983).

[7] Konsynski, B. and D. Dolk, Knowledge Abstractions in Model Management, in: Trans. 2nd Int. Conf. Decision Support Systems, G.W. Dickson (ed), pp. 187–202, San Francisco, CA (June 14–16, 1982).

[8] Sol, H.G. (ed.), Processes and Tools for Decision Support, North-Holland, Amsterdam (1983).

[9] Chen, M.C., J. Fedorowicz, and L.J. Henschen, Deductive Processes in Databases and Decision Support Systems, Proc. North Central Regional ACM 1982 Cong., pp. 81–100, Milwaukee, WI (Nov. 19, 1982).

[10] Chang, C-L., and R.C-T. Lee, Symbolic Logig and Mechanical Theorem Proving, Academic Press, New York, NY (1973).

[11] Nilsson, N.J., Principles of Artificial Intelligence, Tioga, Palo Alto, CA (1980).

[12] Gallaire, H. and J. Minker (ed.), Logic and Databases. Plenum, New York, NY (1978).

[13] Reiter, R., An Approach to Deductive Question-Answering, BBN Tech. Report No. 3649, Bolt, Beranek, and Newman, Inc., Cambridge, MA (Sept. 1977).

[14] Reiter, R., Deductive Question-Answering on Relational Data Bases, in: Logic and Databases, H. Gallaire and J. Minker (eds), pp. 149–177, Plenum, New York, NY (1978).

[15] Moto-oka, T. (ed.), Fifth Generation Computer Systems, North-Holland, Amsterdam (1982).

[16] Fick, G. and R.H. Sprague, Jr. (eds), Decision Support Systems: Issues and Challenges, Pergamon, Oxford (1980).

[17] Sprague, R.H., Jr. and E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ (1982).
