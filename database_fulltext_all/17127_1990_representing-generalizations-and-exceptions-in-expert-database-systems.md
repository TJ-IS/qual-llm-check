---
otero_id: 17127
otero_key: "QY8427NH"
title: "Representing generalizations and exceptions in expert database systems"
authors: "Richard G. Ramirez; Ronald Dattero; Joobin Choobineh"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90012-g"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Representing Generalizations and Exceptions in Expert Database Systems

Richard G. RAMIREZ

Decision and Information Systems, Arizona State University, Tempe, AZ 85287, USA

Ronald DATTERO

Quantitative Business Analysis, Louisiana State University, Baton Rouge, LA 70803, USA

Joobin CHOOBINEH

Business Analysis and Research, Texas A & M University, College Station, TX 77843, USA

To further increase the decision support capabilities of database management systems, previous research has suggested the development of expert database systems by coupling expert systems to database management systems. One approach is to combine the capabilities of logic systems and relational databases. Logic allows the specification of general rules representing abstract knowledge, while database management systems provide efficient management of large masses of data representing specific facts. In many practical situations, general rules cannot or are not intended to describe every possible case, thus leading to the necessity of representing exceptions. A classification of exceptions is made in this paper, and their representation in expert database systems that combine logic and relational databases is discussed. In addition, a description is made of extensions needed to the relational language SQL to permit the specification of rules that allow exceptions.

Keywords: Expert Database Systems, Exceptions, Generalization Rules, Derived Relations, Views, Relational Databases.

![](/api/attachments/QY8427NH/fulltext/images/1882eba7fb5e85557653f14293bddb5ae685c14bb01b39d28d92194272df37cf.jpg)

Ronald Dattero is a visiting professor at Louisiana State University. Previously, he was on the faculty of Texas A&M University. He received his B.A. from Wayne State University, his M.S. from the University of California-Berkeley, and his Ph.D. from Purdue University. His research interests include artificial intelligence, database management, decision support systems, expert systems, and management science. He is a member of AAAI, DSI, IIE, ORSA, and TIMS.

## 1. Introduction

Combining database and knowledge base concepts can produce an expert database system -- "a database system, specifically a relational database system, to which a body of application-specific expertise is appended" [13], or as defined in [26]: "a system for developing applications requiring knowledge-directed processing of shared information". Smith [26] claims that "the majority of the applications where a DBMS is currently used today would benefit from such a tool". A number of systems have been proposed that interface some common tool of expert systems (usually logic) to a database system (usually a relational database) resulting in systems such as KM-1 [12] and PROSQL [5].

Adding logic capabilities to a database system provides an efficient way of dealings with facts and general rules (about the facts). General rules are a powerful modeling tool to represent knowledge at a high level of abstraction, as opposed to data representing specific facts that is handled by

![](/api/attachments/QY8427NH/fulltext/images/f41d4b476aa600a9458a62070739f8a891dc9768258f1b4bad92e53cb6856fac.jpg)

Joobin Choobineh received the Ph.D. degree in management information systems from the University of Arizona, Tucson, in 1985. He is an assistant professor of Information Systems in the Department of Business Analysis and Research at Texas A&M University. His research interests are in the areas of database design, semantic data modeling, expert database systems, and applications of artificial intelligence to business problems. Dr. Choobineh is a member of conventional database systems. “Rules are easier to input, occupy less space, and are easier to change” [14]. Generalizations are found in many situations and reflect prescriptive knowledge (such as minimum admission requirements for students) as well as knowledge learned inductively from examples or experience (such as criteria for disease recognition). The issue of interest in this paper is the representation of the knowledge that is expressed in the form of simple facts and general rules about those facts.

the Association for Computing Machinery and the IEEE Computer Society.  
![](/api/attachments/QY8427NH/fulltext/images/f369277233b46e02b33a1cf7a27c0974e2f3c7437c77d4e388b023af50ae32ad.jpg)  
Richard G. Ramirez's research interests focus on the interaction of databases, decision support systems, and artificial intelligence. Currently, an Assistant Professor of Computer Information systems at Arizona State University, he graduated from Texas A&M University.

A general rule serves two purposes depending on whether it is used independently or in conjunction with specific data. Consider for example the rule “all first-year Ph.D. students must take the Research Seminar”. This rule, so stated and without mention of any names, is an abstract statement defining a departmental policy. The rule can, however, also serve as a procedure that can be applied to the list of students currently enrolled to obtain the names of the students who will take the Research Seminar.

Exceptions are present in almost any generalization since it is “often neither feasible to anticipate, nor desirable to capture all possible situations in the world” [3], and even if it were possible to capture complete information about a situation, it is unlikely that it would remain valid for a long time as the world changes rapidly [24]. Exceptions do not necessarily invalidate the rule but rather complement it with the special cases not anticipated by the rule. Reiter [21,22], for example, in discussing default reasoning, has noted that most of what we know about the world is “almost always” true and has given the classical example of penguins and birds, saying that although penguins are birds that don’t fly, we still want it true of birds “in general” that they fly. In our example, there will be some PhD students that may not enroll in the Research Seminar in their first year or there may be a few exceptional MS students that will get special permission to enroll in this course. These “exceptional” students do not cause the rule to be considered invalid in the future, nor make a change in curriculum necessary, as there is a common understanding that the large majority of students will follow it. Modifying the rule to allow for all possible causes of exception would be impractical (perhaps impossible or requiring constant updates) and would obscure the reason for such rule.

The next section presents definitions of general rules and exceptions. Section 3 discusses their representations in expert database systems combining logic and relational databases. Section 4 discusses representative systems that integrate logic and relational databases and could be used to implement exceptions to rules. Section 5 introduces extensions to the SQL language to support rules and exceptions. The last section concludes the paper.

## 2. General Rules and Exceptions

Intuitively, a general rule is a statement that describes common features of individuals in a group. In Artificial Intelligence, a general rule is often found in learning [7] where the interest is to look at a group of objects in order to generalize (learn) something about them, and in default or non-monotonic reasoning, where a general statement is true in the absence of specific information against it [21]. Using different words, a general rule is a statement (a predicate) that is true for all (or most) of the individuals in a group.

It is customary to differentiate between two kinds of generalized statements: those about simple facts (classification or token-type relationship) and those about classes of objects (generalization or type-type relationship) [28]. As indicated before, this paper centers on general rules about simple facts (and exceptions to those rules). Accordingly, we use the following definition.

Definition. Given a set P, R is a classification rule if R is a predicate such that for some elements of P, R evaluates to true.

Usually the classification rule R is not defined over the set P but on a superset S that includes P as a subset. Intuitively, this happens because P is a (often implicit) sample of a larger population.

Intuitively we know that few, if any, rules of practical significance can describe a population in such a way that every individual in the population satisfies the rule and those individuals outside the population do not satisfy it. In other words, we expect “exceptions” to occur to for a given rule.

A “good” general rule is a predicate that evaluates to true for most of the elements in that group, while a “bad” general rule will be true only for some of those individuals. The idea of a classification rule is to describe a set P (a subset of S), but it is actually defining another set, composed of those elements in S which satisfy the rule. Following the standard terminology in databases, we will refer to this set as a “view” (i.e., a derived relation) and will provide the following definition:

Definition. Given a set S and a classification rule R, a view V on S is the subset of S for which R evaluates to true.

Fig. 1 shows the relationship of the sets S, P and V. Note that for a “good” classification rule, the sets V and P are identical or very close, and there are few or no exceptions at all.

A classification rule allows the description of the set P in a concise form without having to list explicitly each element in P. However, as can be seen in fig. 1, the rule defines a set V that does not match exactly the set P that the rule attempts to describe. Therefore, in order to fully describe P it is necessary to give the “rule plus the exceptions to the rule”, i.e., the rule plus an explicit listing of elements that should be omitted or added to the view defined by the rule. We will give the following definitions for exceptions:

Definition. Given a set S, a subset P of S, and a classification rule R, the set I of internal inclusions is the set of elements in P that do not satisfy the rule R.

Definition. Given a set S, a subset P of S, and a classification rule R, the set O of omissions is the set of elements in S - P (S difference P) that satisfy the rule R.

The sets I and O are collectively called exceptions. The sets of exceptions are shown in fig. 2. In standard set notation, the relationship between the sets can be seen in the following notation: Given a set S and a rule R,

![](/api/attachments/QY8427NH/fulltext/images/d540526ef105fbdef995baad90aab78166aefc7e5fdef946bf8fb625e44324b1.jpg)  
Fig. 1. The population P and the set V are not exactly the same.

![](/api/attachments/QY8427NH/fulltext/images/54575fbaca57da5d7b7897eed1d98cbc363d56d5963cad9a83b2c45207df2f7d.jpg)  
Fig. 2. The exceptions I and O correspond to the differences between P and V.

$$
\begin{array}{l} P \subset S, \\ I = \left\{i \mid i \in P, R (i) = \text { false } \right\}, \\ O = \left\{o \mid o \in (S - P), R (o) = \text { true } \right\}, \\ V = \left\{v \mid v \in S, R (v) = \text { true } \right\}, \\ D = V + I - O = P. \end{array}
$$

Using the sets of exceptions, the set P can be constructed by using the view V modified by the exceptions, and we will refer to this reconstructed set P as a derived relation with exceptions (DRE), defined as follows:

Definition. Given a set S, a subset P of S, a classification rule R on P, a view V on P, and sets of exceptions I and O (inclusions and omissions), a derived relation with exceptions D (DRE) is the set formed by $V + I - O$ (V union I difference O).

The sets P and D (the DRE) are equivalent according to these definitions. However, there are assigned different interpretations. The set P is considered to be the population that the general rule attempts to describe. The DRE is considered the result of a (syntactical) manipulation of some sets regardless of meaning (see [19] for a discussion of interpretations). The distinction becomes important when the sets and operations are represented on a computer and the correspondence between the objects stored in the computer (character strings, records) and their original meaning (employees, parts) must be made by the user (or perhaps the user's programs).

## 3. Classification Rules and Expert Database Systems

The definition of classification rules does not specify an implementation vehicle. In this paper, we are concerned with expert database systems that are based on logic and relational databases. Logic is a natural choice for the representation of classification rules because they correspond naturally to predicates and because logic provides inferencing mechanisms from which statements can be combined and further knowledge obtained. Relational databases have a close relationship to logic [11] and represent the state of the art in commercial database systems. The combination of both has been discussed in many papers (see for example [4], [11], and [12]), as well as in the Japanese 5th Generation Project [10,17]. Therefore, in this section only a brief review of the relative strengths of both logic and relational databases is given to later focus on the specific issues associated with the representation of classification rules as well as the respective advantages and disadvantages of the available options.

## 3.1. Logic and databases

The strengths of logic for knowledge representation have been discussed in many places. Reiter [23] has given the following summary:

\- logic uses a simple notation and has a well defined semantics,

\- conceptual economy - each fact or deduction rule is represented once, independently of its different uses,

\- representational uniformity – facts, hypotheses, implications, queries and views are all expressed in the same language,

\- operational uniformity - proof theory is the sole mechanism for query evaluation,

\- generality of inference and proof procedures - new facts can be deduced using the inference and proof procedures.

On the other hand, database management systems (DBMSs) provide a number of facilities that are absent in logic and logic programming. Brodie and Jarke [4] discuss the following advantages of DBMSs over current implementations of PROLOG, the most popular implementation of logic programming.

\- efficient access to large fact bases,

\- multiple users using the database concurrently,

\- multiple views of the data,

\- database structure – efficient management and programming of large databases benefits from structuring,

\- set oriented optimization with management of permanent access paths (such as indexes),

\- data management, including recovery and security,

\- transactions.

Broadly speaking, logic systems provide powerful representation and inference mechanisms, while DBMSs provide efficient handling of large databases, constraint checking, and data management facilities. An ideal system would integrate the advantages of logic and database systems. Such is the premise for the Japanese Fifth Generation Computer Systems Project [17], but although it is possible to build systems that interface a logic systems and a relational database system (see, for example, [11], [12], [5]), a number of issues (such as query optimization, integrity constraints, and distribution of inference) are yet to be solved for an efficient partitioning of tasks among the two systems. A survey of these issues can be found in [4].

## 3.2. Representing Classification Rules in Logic and Database Systems

In the remainder of this section the specific problem of implementing classification rules and their associated populations will be discussed. From section 2, it can be recalled that there are three basic elements to be represented explicitly: (a) the classification rule R, (b) the source population S, on which the rule R is applied, and (c) the exceptions, inclusions (I) and omissions (O), to the rule. The view V and the population P do not need to be explicitly represented because they can be generated from the population S using the classification rule. In logic, V and P can be generated using the inference or proof mechanism, while in relational databases, they can be generated using the “view” mechanism. An example using PROLOG is given in the appendix, and section 5 shows the implementation using extension to the SQL database language.

If we assume that a system combining logic and relational databases (such as KM-1 [12] or PROSQL [5]) can be used, the following options are then available to represent classification rules and facts:

1. Storing the classification rule, the exceptions and the population S in the logic subsystem, i.e., no DBMS is used.

2. Storing the classification rule and the exceptions in the logic subsystem, and the population S in the DBMS. The logic subsystem processes exceptions and requests the original data from the DBMS to generate the view and the derived relation with exceptions.

3. Storing the classification rule in the logic subsystem, and the population S and the exceptions in the DBMS. The derived relation with exceptions is formed by the logic subsystem using the rule and requesting the data from the DBMS.

4. Storing the classification rule, exceptions and original facts in the DBMS. The DBMS processes exceptions and original facts and makes available the derived relation with exceptions.

Other options to store rules, exceptions and the population S may exist, such as storing the classification rule in the DBMS, and exceptions and population S in the logic subsystem, but they are either infeasible or impractical. Hence, only the above four options will be discussed.

The four options can be analyzed using several criteria. We are concerned with the following:

\- representation - ease and naturalness of representation,

\- inference - how the generation of $V$ and $D$ is made, and how classification rules are combined,

\- efficiency - how fast the generation of $V$ and $D$ is made as well as the ability to handle large populations,

\- integrity – how the data can be prevented from corruption by invalid or conflicting data,

\- data management - security and concurrency.

## 3.3. Alternative 1: Storing All Information in the Logic System

A first approach to supporting classification rules in expert database systems is to store both rules and data exclusively in the logic system. A logic programming language such as PROLOG allows the representation of the rules directly (as clauses or logic statements), and also the representation of simple facts as assertions.

From a representation viewpoint, this alternative is the best as rules and facts are represented directly in the same uniform language. From an inference viewpoint, this alternative is also the most complete; logic provides a well defined inference mechanism that can be used to generate the derived sets as well as to combine several rules to provide further deduction capabilities. Furthermore, the inference mechanism allows recursion. From an efficiency viewpoint, however, this alternative cannot access large databases as efficiency as a DBMS, and from a data management viewpoint, this alternative lacks the built-in features of a DBMS for integrity and security; there is also no (automatic) way of verifying contradictory or invalid exceptions as current implementations of logic programming do not support automatic integrity constraint checking. A contradictory exception occurs when a fact is considered simultaneously as an inclusion and an exception, or when a inclusion or omission refers to a fact not in the population S. In addition most logic programming implementations only allow a single user, rather than multi-user concurrent access.

## 3.4. Alternative 2: Storing Rules and Exceptions in the Logic System

Under this alternative, the DBMS is left to manage the (presumably large) collection of data representing the original population S. The logic system stores the classification rule and the exceptions to the rule. The logic system is also responsible for the generation of the derived populations V and P.

From a representation viewpoint, this is still a very good alternative, similar to Alternative 1. The rule is naturally represented in logic, while the basic facts are represented as tuples in the relational database. From an inference viewpoint, this alternative offers the same advantages as Alternative 1. From an efficiency viewpoint, this alternative offers the added advantage over Alternative 1 of handling the (large) number of facts through a relational database. The handling of these facts is more efficient and accessible to several simultaneous users. Alternative 2 does, however, adds to the efficiency problems of Alternative 1 the overhead caused by the communication between the logic and the database systems, as the inference mechanism is retained by the logic system. From the viewpoints of integrity and data management, Alternative 2 is an improvement over Alternative 1 with respect to population S. No such improvement exists over exceptions and there is also no (automatic) way of verifying contradictory or invalid exceptions.

This alternative seems convenient when a relational system is already managing a database, inference capabilities need to be added on top of the system, and the exceptions do not interfere with the programs using the database.

## 3.5. Alternative 3: Storing only the Rule in the Logic System

Alternative 3 goes a step beyond the previous alternative in that exceptions are considered basic data and are stored in the database together with the original population. This allows the building of a system where all simple facts are managed by the DBMS, while rules representing abstract and more generally information are handled by the logic system. The DBMS is now able, by using integrity constraint checking, of supplying some verification against contradictory exceptions.

From a representation viewpoint, this alternative is still convenient; the logic system allows easy representation of the rule and the DBMS easily represents simple facts. From an inference viewpoint, this alternative is similar to alternatives 1 and 2; the logic system is still responsible for forming the sets V and D and combining the classification rule with other logic statements. From an efficiency viewpoint, this alternative offers an increased potential for efficiency as all data handling is done by the DBMS. There are some efficiency problems because the logic subsystem uses its inference mechanism to generate the DRE. From the integrity and data management viewpoints, this alternative is an improvement over the previous alternatives. The DBMS, by using integrity constraint checking (either automatically or incorporated to update programs) is able to verify for contradictory exceptions.

This alternative differs from the previous alternatives in that exceptions (as well as the original population S) are stored in the DBMS. The logic system stores the classification rule and is responsible for the generation of the derived populations. Presumably, this option allows the representation of all abstract (data independent) knowledge in the logic system, while keeping all specific data in the DBMS.

## 3.6. Alternative 4: Storing All Information in a Database System

Under this alternative, the classification rule, the exceptions and the original population are all stored by the DBMS. The DBMS is also responsible for the generation of the derived relations.

From a representation viewpoint, this alternative is not the most effective. In contrast to logic and logic programming, a classification rule must be represented as a view using view definition statements of languages such as SQL or QUEL. From an inference viewpoint, there is a decrease in capability (in terms of the current state of the art DBMSs). First, a DBMS is typically not able to express recursive classification rules, and, second, the classification rule (now a view definition) cannot be automatically combined with other logic statements to provide more inference. On the other hand, from an efficiency viewpoint there is a net gain, as queries are answered and the view and the DRE are formed using only the DBMS query answering mechanisms with the full benefit of query optimization and set-oriented operations. From the integrity and data management viewpoints, this is also the best alternative. The DBMS can verify against contradictory exceptions and there is only one deposit of data (the database).

This alternative seems the most convenient when limited inference capability is all that is needed and/or there are large masses of data to be handled. Among the advantages are that most classification rules can be represented and the highest efficiency is obtained. There is also no need for an additional system other than the DBMS and therefore only one user interface needs to be supported. All the advantages of having a DBMS are retained such as concurrent access, security, and a variety of programming languages.

## 4. Available Implementation Alternatives

In this section we study the systems that have been proposed or are available in the market for the development of systems using logic and relational databases. Subsection 4.1 describes systems that interface a logic programming language with a DBMS. Subsection 4.2 describes some systems that extend logic programming systems with data management capabilities, while subsection 4.3 describes systems that extend DBMSs with logic capabilities. Our purpose is to describe representative systems rather than making an extensive survey. A brief description of the advantages and disadvantages of these types of systems in general has been made in sections 2 and 3 of this paper and a more detailed analysis can be found in [4].

## 4.1. Systems Interfacing Logic and Relational Databases

These systems are characterized by having two independent systems that are linked together through some interface. Typically the logic system controls all operations and uses a relational DBMS as a backend. The logic system issues requests for data from the DBMS as needed by the deductive process. The two systems can be linked or coupled in a tight or loose way [30]. In a tight coupling, the logic systems issues requests for DBMS data as needed in the deductive process. In a loose coupling, the logic system requests for data are executed once for each query or deductive plan.

What is perhaps the simplest link between a logic system and a DBMS is exemplified by the mechanism to link micro-PROLOG [15] and dBase II developed by Berghel [2]. This mechanism requires the conversion of dBase II files to micro-PROLOG “programs” that are then read by a PROLOG program and incorporated into the program’s working memory. The conversion is executed as an additional step and does not involve modification of either micro-PROLOG or dBase II.

A step further are systems such as PROSQL, developed by Chang and Walker [5]. PROSQL links a PROLOG interpreter with the SQL/DS database management system. The PROLOG program uses function calls to retrieve data from the DBMS. The function calls are similar to embedded SQL calls [8] except that PROSQL is able to read an entire relation (the result of a SQL SELECT query) into the PROLOG program's working memory as a collection of predicates.

Kellogg [12] has developed KM-1, a system using a logic-based deductive processor linked to a relational database machine. KM-1 runs on a Xerox 1100 Lisp machine and accesses an internal database as well as an external database system running on a Britton-Lee database machine. Relations are categorized according to their type: "deduce", "search" or "computed". Search relations are stored in one of the database systems, deduce relations are obtained through the logic system using other relations, and compute relations provide for arithmetic and other computations. A "deductive plan" is formulated for each query that contains the relations and operations necessary to answer the query. The database is accessed obtain the search relations needed only once per deductive plan and thus KM-1 is a loosely coupled system.

A hybrid system is exemplified by Arity Corporation's SQL Development Package [1]. This package is actually a PROLOG program that implements the SQL database language. The package can be run as a stand-alone program (although running under the control of the PROLOG interpreter), operating as a DBMS, but also, since it is written in PROLOG and runs under the control of the PROLOG interpreter it can also be included as part of a PROLOG program. The PROLOG program can issue SQL commands that are immediately executed (in a manner similar to PROSQL) but it also has access to all the data structures and facilities of the SQL implementation. While not intended as a production system, but rather as a research tool, the system is capable of running most SQL commands directly.

The availability of the above and similar system does not, unfortunately, indicate that logic programming and relational DBMSs can be easily interfaced. Zaniolo [31] lists the following issues remaining to be solved: (1) when should database goals be executed, (2) how should data be exchanged to and from PROLOG and the DBMS, (3) how can the translation of goals (queries) be optimized, and (4) how should recursive calls be supported. Zaniolo's "short-to-medium term solution" assigns a navigational interpretation to both PROLOG and database goals, and suggests using PROLOG as a navigational query language for a navigational DBMS, such as CODASYL-compliant and Entity-Relationship oriented DBMSs.

4.2. Systems Extending Logic Programming Implementations

The approach taken for these systems is to extend a PROLOG or other logic programming processor to incorporate DBMS capabilities. This approach is not popular as the interface, probably because it raises most of the problems of tight integration of PROLOG and a DBMS with potentially less capability [4]. For example, adding features such as data types would require programmer discipline and are likely to be less efficient than having the semantics implemented directly in the underlying system.

Tsur and Zaniolo [29] report the development of LDL (Logical Data Language). LDL extends logic programming beyond PROLOG in the following ways: (1) no sequential order of execution in a procedure (rule) is assumed, (2) sets are primitive data objects, (3) a form of negation based on set-difference replaces PROLOG's negation by failure, and (4) schema definition and update facilities are included in the language. LDL is reportedly at the prototype stage and work continues.

Sciore and Warren [25] also report the development of a prototype system. They isolated the following concepts to be added to a PROLOG system: (1) disk pointers, indicating the location of a tuple on disk (2) tuple formats, as PROLOG systems typically use a LISP-like format for tuples that is not as efficient as the record-oriented format, and (3) sophisticated buffer management.

## 4.3. Extending Relational DBMS

These systems do not completely provide the inferencing capability of logic programming as their query languages tend to stray afar from Horn clause logic, and research in this area seems to be focused on providing general abstract data type facilities to the query language [18]. Current offerings of relational DBMSs do not provide explicit support for deduction rules.

Stonebraker et al. [27] describe a proposed implementation for rules in the relational database system INGRES. While the proposal was considered potentially useful to provide alerting triggers, and to provide stored DBMS commands, it was also deficient in several important aspects. Some of these deficiencies were that the rule specification was extremely complex, and the result could depend on the order of execution.

Missikoff and Wiederhold [16] propose an evolutionary approach for database systems to have the full capabilities of (their description of) an expert database system. Their criteria for an EDS include that domain knowledge must be managed within the EDS and not delegated to outside procedures and a requirement for deductive power. The key feature of their proposal is a unified frame in which different forms of knowledge can be treated in the same fashion. This feature can only be achieved if there exists an underlying information model that can represent the different forms of knowledge in a homogeneous fashion. This information model is outlined in their paper.

A concrete mechanism for classification rules in a relational database system has been proposed by Ramirez [9]. The proposal extends the view mechanism in SQL to allow for derived relations with exceptions (DREs) and is discussed in the following section.

## 5. An Implementation of Classification Rules with Exceptions in Relational Database Systems

Roughly speaking, when using a relational database system, a relation represents a population and each tuple in the relation corresponds to a unique individual in the population. Queries on the relation allow the extraction of subsets of the relation, as well as other “transformation” such as projections (eliminating some attributes) and the creation of aggregates (sums and averages, for example). A relational view (i.e., a virtual or derived relation) is defined by storing a query definition.

To represent a classification rule R and its associated sets, the population S, on which R is defined, is represented by a relation that we name “source relation”. The classification rule is then represented as a view definition, and the “view V on S” is obtained by processing the view definition representing the classification rule. Since a classification rule is defined as a predicate, the view V is, in relational terms, a tuple subset of the source relation.

![](/api/attachments/QY8427NH/fulltext/images/3f732ec19c8f92de8f6e433c8834f7cec9807160bf74493f628a1188cf568267.jpg)  
Fig. 3. The Process to Obtain a View or Derived Relation.

The following two subsections show, first, how to extend relational views to represent classification rules and exceptions, and second, an implementation using the SQL language.

## 5.1. Extending Relational Views

Consider an arbitrary view definition in a relational database. It can be seen as having two components: a “view predicate” and a “transformation rule”. The view predicate selects tuples from a source relation, and thus defines a subset of the source relation. The transformation rule “transforms” the tuple subset into another table by eliminating some attributes (projection), or by computing aggregates (such as sums or averages). Fig. 3 shows this process.

For a classification rule, using the process shown in fig. 3, it is assumed that each tuple in the source relation represents an individual in the population S. The view predicate represents the classification rule (i.e., a predicate). The “transformation rule” has (for the purposes of classification rules and of this paper) no effect other than perhaps eliminating some attributes from the resulting derived relation.

![](/api/attachments/QY8427NH/fulltext/images/7079e4cf2ae60a99aeaa679297f1130e4ff80e0b64ce2bc7aff0baab1617bc0d.jpg)  
Fig. 4. The Process to Obtain Derived Relations with Exceptions.

By separating a view definition into subsetting and transformation components, it is possible to extend the concept of relational views to derived relations with exceptions (DREs) allowing for inclusions and omissions. Fig. 4 shows these extensions to fig. 3. Internal inclusions ( $S_{I}$ in fig. 4) are represented by tuples from the source relation which do not satisfy the rule (the view predicate) but must be added to $S_{V}$ to be included in the DRE. Omissions ( $S_{0}$ in fig. 4) are tuples from the source relation which satisfy the view predicate (and therefore are in $S_{V}$ ) but must not be included in the derived relation. The transformation rule is applied to the set $S_{V} + S_{I} - S_{O}$ (the set union of $S_{V}$ and $S_{I}$ difference $S_{O}$ ) to form a first derived relation. External inclusions are described by tuples not in the source relation (and therefore not in $S_{V}$ or $S_{I}$ ) that are included in the derived relation. Thus, the relation E is unioned to the result of “transforming” $S_{V} + S_{I} - S_{O}$ to form the final DRE. When $S_{I}$ , $S_{O}$ and E are empty relations, a DRE reduces to a conventional view, as the set $S_{V} + S_{I} - S_{O}$ will be the same as $S_{V}$ .

The reason for the term internal inclusions will now become clear. The relation $S_{I}$ defines tuples in the source relation that must be included in the DRE, and thus it corresponds to individuals in S that are also in P although they do not satisfy the classification rule. The mechanism shown in fig. 4 adds another relation, E, that corresponds to inclusion that are not present in the source relation. We call these external inclusions. The justification for introducing external inclusions lies in the additional flexibility they provide, particularly in the case where the transformation rule actually modifies the tuples of $S_{V} + S_{I} - S_{O}$ . Using this mechanism, it is possible to allow for exceptions in views that, for example, create aggregates such as sums and means from tuples in the source relation.

Internal inclusions $(S_{I})$ and omissions $(S_{O})$ do not need to be explicitly stored. Instead, they are more efficiently obtained by joining relations S with I and O, respectively. I and O are relations containing only the attributes needed to identify tuples in S, usually the primary key.

## 5.2. An Implementation Using SQL

The mechanism shown in fig. 4 can be implemented by extending the SQL language to allow the definition and processing of DRE's. A proposal for these extensions has been made in Ramirez et al. [20]. In this paper only the aspects that are relevant to classification rules are discussed. The reader unfamiliar with the SQL syntax should refer to [8] or [9].

A DRE is created or defined in a manner similar to the current CREATE TABLE or CREATE VIEW statements. Table 1 shows the form for the CREATE DRE statement, using a

```txt
Table 1
Syntax of the CREATE DRE Statement.

relation definition ::= create-table-statement
| create-view-statement | create-dre-statement

create-table-statement ::= <as defined in SQL>

create-view-statement ::= 
CREATE VIEW view-name [(view-attributes)]
AS subquery
... <as defined in SQL>

subquery ::= 
SELECT {source-attributes}
FROM {source-relation}
[WHERE view-selection-formula]

create-dre-statement ::= 
CREATE DRE dre-name [{dre-attributes}]
[BASED ON] VIEW view-name
[UPDATE [AS] update-option]
[KEY {key attributes}]
[INTERNAL [INCLUSIONS] internal-spec]
[EXTERNAL [INCLUSIONS] external-spec]
[OMISSIONS omission-spec]

update-option ::= 
VIEW | HYPOTHETICAL RELATION | NOT ALLOWED

internal-spec ::= {internal attributes} [FROM internal-table]

external-spec ::= 
YES | NO | [RELATION] external-table {{external-attributes}}]

omission-spec ::= {omission-attributes} [FROM omission-table]

internal-attributes ::= <subset of source-attributes>

omission-attributes ::= <subset of source-attributes>
```

Backus-Naur-like syntax. The different entries are as follows:

1. Names for the DRE and its attributes are given in a manner similar to the standard CREATE VIEW statement.

2. The parameter BASED ON VIEW is required, and relates the definition of the DRE to the name of the view representing the classification rule.

3. The UPDATE AS parameter defines the treatment of updates to the DRE. The options are (a) as a regular view, (b) as a hypothetical relation, or (c) no updates will be allowed. A DRE can be updated as a view if the BASEDON view is in itself updatable. Updating a DRE as a hypothetical relation results in no updates made to the source relation but, instead, updates are considered inclusions or omissions.

4. The KEY option allows the user to specify the attributes that define the key. It also specifies that all references (including internal inclusions and exclusions) to tuples will be made using the attribute selected as the key.

5. The INTERNAL INCLUSIONS and OMISSIONS parameters define the attributes that will be used to indicate these types of exceptions (in relations I and O). If the KEY option was used, this attribute must be defined over the same domain as the primary key of the BASED-ON view.

6. The EXTERNAL INCLUSIONS specification defines an optional table that will be unioned with the result of processing the BASED-ON view with the internal inclusions and omissions. As an example, consider the case described in

As an example, consider the case described in the appendix. A list of all customers is kept in the relation CUSTOMERS. Special discount promotions are made according to the rule “offer a promotion to customers whose last quarter purchasing volume was less than 70% of the forecast”. The list of customers obtained by applying this rule to the relation CUSTOMERS is modified with inclusions and omissions, reflecting the fact that the promotion (because of its cost) should only be made to those customers that are likely to be influenced in their future purchase decisions. Omissions indicate customers that satisfy the rule (i.e., they bought less than 70% of the forecast) but are not likely to increase purchases. Internal inclusions represent customers that do not satisfy the rule but are candidates to the promotion anyway. An additional relation, FOREIGN, stores data for individuals that are not current customers but to whom the promotion will be made.

The relation CUSTOMERS corresponds to the set S (the source relation), the relation ADDITION is used to represent the internal inclusions, the relation EXCLUSION for omissions, and the relation FOREIGN stores the external inclusions. These relations are defined using the standard CREATE TABLE statement. For simplicity, only the relation names and attributes are shown, as follows.

CUSTOMER (c#, name, forecast, actual, city, type)
ADDITION (name)
EXCLUSION (name)
FOREIGN (c#, name, forecast, actual, city, type)

The rule “offer a promotion to customers whose last quarter purchasing volume is less than 70% of the forecast” is represented by defining the view DECREASING as follows (SQL keywords are indicated by using uppercase letters, user-chosen names appear in lowercase):

CREATE VIEW decreasing

AS SELECT \*

FROM customer

WHERE actual < forecast \* 0.7;

The DRE can be easily defined using the CREATE DRE statement defined in table 1, as follows:

CREATE DRE promotions
BASED ON VIEW decreasing
INTERNAL INCLUSIONS name
OMISSIONS name
EXTERNAL INCLUSIONS RELATION
foreign

The DRE will be named "PROMOTIONS". The BASED ON VIEW clause established DE-CREASING as the view definition representing the rule. The INTERNAL INCLUSIONS and OMISSIONS clauses specify that these exceptions will be referenced using the attribute NAME. Finally, the EXTERNAL INCLUSIONS clause indicates that the relation FOREIGN contains that type of exceptions.

## 5.3. Retrieving Data from a DRE

The CREATE DRE defines a virtual relation that will be handled in a manner somewhat similar to a conventional view (i.e., a derived relation). Since SQL allows views to be treated almost in the same way as base relations, a view (and a DRE) can be used in (almost) any place that a base table can be used with no modification to the syntax of the data manipulation statements. For DREs in particular, the following change in the semantics of the operations must be made. First, the SELECT statement must be internally modified to retrieve a DRE using the process shown in fig. 3. A SELECT to retrieve data from a DRE is transformed into the UNION of two SELECTs. The first select is in turn the result of “merging” the original SELECT with the definition of the view modified for internal inclusions and omissions. The second SELECT is simply the original SELECT applied to the relation containing external inclusions, if applicable. Table 2 shows the logical processing of a SELECT on a DRE.

Any valid query on a standard view can also be applied to a DRE. No changes are needed in the syntax of SQL statements for this purpose. A SELECT statement on a query will perform in the following way:

query: SELECT \*
FROM promotions treated as: SELECT \*
FROM customer
WHERE (actual < forecast \*.7
OR name IN
(SELECT name
FROM AD-
DITION)
AND NOT name in
(SELECT name
FROM exclu-
sion)
UNION
SELECT \*
FROM foreign

<table><tr><td colspan="2">Table 2Retrieving from a DRE.</td></tr><tr><td colspan="2">dre-retrieval-rule ::=</td></tr><tr><td>SELECT</td><td>dre-attributes</td></tr><tr><td>FROM</td><td>modified-view</td></tr><tr><td>UNION</td><td></td></tr><tr><td>SELECT</td><td>dre-attributes</td></tr><tr><td>FROM</td><td>external-table</td></tr><tr><td colspan="2">modified view ::=</td></tr><tr><td>SELECT</td><td>view-attributes</td></tr><tr><td>FROM</td><td>source-relation</td></tr><tr><td>WHERE</td><td>(view-predicateOR internal-attributes IN(SELECT internal-attributesFROM internal-table))AND NOT omission-attributes in(SELECT omission-attributesFROM omission-table)</td></tr><tr><td>[GROUP BY</td><td>...]</td></tr><tr><td>[HAVING</td><td>...]</td></tr></table>

The semantics of the update statements in SQL must also be modified. When the view represents a classification rule as defined in this paper, the view is updatable if the source relation is updatable. In general, the source relation will be updatable if it is a base table or a row or column subset of a base table.

## 6. Concluding Remarks

This paper focused on classification rules in expert database systems. General rules are a powerful modeling tool to represent knowledge at a high level of abstraction. Classification rules represent the important case where a generalization is made on simple facts or objects. Exceptions are, however, present in almost any generalization. Formal definitions and examples of classification rules and exceptions were presented.

The formal definition of classification rules and exceptions does not specify any implementation vehicle. Four implementation alternatives that combine logic and relational database systems were assessed using several criteria. The alternatives ranged from totally using the logic system to totally using the relational database system with two alternatives coupling the two systems. Each alternative has its own advantages and disadvantages with no one alternative dominating the others.

Existing systems that implement some form of classification rules were described. A new approach that extends the relational language SQL to allow the specification of classification rules was detailed. This new approach extends the capabilities of relational views to include exception handling. Work is ongoing to fully explore the capabilities of this new approach.

## Appendix

## An Example Using Logic Programming

The definition of a classification rule as a predicate suggests that a language such as predicate calculus would be appropriate for the representation of classification rules and the population described by it. PROLOG [6] provides an implementation of a predicate calculus as well as extensions for conventional programming, and it will be used to provide an example. This appendix presents an example of a classification rule and its representation using logic programming. Section 5 of the paper uses this same example in the description of the proposed SQL extensions.

## A.1. Background

Consider the hypothetical situation of XYZ Paper Inc., a company selling computer paper to medium and large data processing shops. Customer purchases are relatively constant and are made on a monthly basis. XYZ schedules sale promotions in which special discounts are given to customers which have decreasing their purchase volumes.

The rule followed by XYZ is to offer a discount to “customers whose last quarter purchasing volume is less than 70% of the forecast”. The list of such customers is revised to exclude those for whom the promotion would not make difference (in order to avoid unnecessary costs). The list is also modified to include a few selected customers buying in excess of 70% of the forecast but who may increase purchasing volumes in the future.

This example is typical of the use of a classification rule. The rule defines the company's policy and provides a mechanism to obtain an initial list, while the final list is obtained by deleting some customers and including others.

Exceptions to the rule occur for many different reasons. The following cases may explain omissions: a customer may have announced already its intention of switching to another supplier and therefore the promotion will not result in increased sales in the future, a customer may already have a contract guaranteeing a discount in return for exclusivity or high purchasing volume, and a customer is in the process of decentralizing operations and purchases. For internal inclusions, the reasons can be that a customer is considering switching to XYZ as the sole supplier and the promotion may make a difference in the decision.

External inclusions correspond to the case of individuals that not current customers but to whom the promotion will be offered anyway.

## A.2. The Logic Programming Representation

The following correspondences exist between the situation depicted and the sets described in the article:

## SET CASE

S the list of all customers

V the subset of customers whose actual purchases are less than 70% the forecast

I internal inclusions: customers whose purchases exceed 70% the forecast but who will be offered the promotion

O omissions: customers whose purchases are less than 70% the forecast but who will not be offered the promotion

E external inclusions: individuals who are not currently customers, but to whom the promotion will be made

## A.2.1. Representing the Population S

As described above, the population S corresponds in this example to the list of all customers. It can be represented by coding a PROLOG assertion for each customer. All assertions have the same name and the same parameters.

<table><tr><td></td><td>C#</td><td>Name</td><td>Forecast</td><td>Actual</td><td>City</td><td>Type</td></tr><tr><td>customer(</td><td>100,</td><td>&#x27;John Jenkins&#x27;,</td><td>1200,</td><td>1000,</td><td>&#x27;Houston&#x27;,</td><td>4).</td></tr><tr><td>customer(</td><td>108,</td><td>&#x27;Jett Properties&#x27;,</td><td>600,</td><td>500,</td><td>&#x27;Bryan&#x27;,</td><td>3).</td></tr><tr><td>customer(</td><td>127,</td><td>&#x27;American Firearms&#x27;,</td><td>1300,</td><td>1500,</td><td>&#x27;Snook&#x27;,</td><td>3).</td></tr><tr><td>customer(</td><td>135,</td><td>&#x27;Magnolia Seafood&#x27;,</td><td>1200,</td><td>900,</td><td>&#x27;Phoenix&#x27;,</td><td>3).</td></tr><tr><td>customer(</td><td>182,</td><td>&#x27;Morgan Building&#x27;,</td><td>2100,</td><td>800,</td><td>&#x27;Houston&#x27;,</td><td>3).</td></tr><tr><td>customer(</td><td>210,</td><td>&#x27;Valley Utilities&#x27;,</td><td>7800,</td><td>10500,</td><td>&#x27;Snook&#x27;,</td><td>1).</td></tr><tr><td>customer(</td><td>215,</td><td>&#x27;City of Phoenix&#x27;,</td><td>5300,</td><td>3975,</td><td>&#x27;Phoenix&#x27;,</td><td>1).</td></tr><tr><td>customer(</td><td>218,</td><td>&#x27;Valley School D.&#x27;,</td><td>1200,</td><td>2000,</td><td>&#x27;Snook&#x27;,</td><td>2).</td></tr><tr><td>customer(</td><td>237,</td><td>&#x27;T &amp; L Roofing&#x27;,</td><td>150,</td><td>275,</td><td>&#x27;Tucson&#x27;,</td><td>3).</td></tr><tr><td>customer(</td><td>249,</td><td>&#x27;Southwest Printing&#x27;,</td><td>4982,</td><td>4000,</td><td>&#x27;Chicago&#x27;,</td><td>3).</td></tr><tr><td>customer(</td><td>382,</td><td>&#x27;Blake College&#x27;,</td><td>1200,</td><td>285,</td><td>&#x27;Tucson&#x27;,</td><td>2).</td></tr><tr><td>customer(</td><td>391,</td><td>&#x27;Long Valley Cy.&#x27;,</td><td>2200,</td><td>1500,</td><td>&#x27;Snook&#x27;,</td><td>1).</td></tr><tr><td>customer(</td><td>397,</td><td>&#x27;High Range City&#x27;,</td><td>4100,</td><td>2000,</td><td>&#x27;Range&#x27;,</td><td>1).</td></tr><tr><td>customer(</td><td>398,</td><td>&#x27;Swaggart College&#x27;,</td><td>20500,</td><td>18241,</td><td>&#x27;Orange&#x27;,</td><td>2).</td></tr></table>

## A.2.2. Representing the Rule and the View

The rule “offer a promotion to customers whose last quarter purchasing volume is less than 70% of the forecast” can be easily expressed in PROLOG by the clause.

promote(C#, Name, Forecast, Actual, City, Type)
if

customer(C#, Name, Forecast, Actual, City, Type),

Following the conventions of Clocksin and Mellish [6] for the PROLOG syntax, variable names are indicated by capitalizing their first letter (i.e., Name in the rule promote indicates a variable).

When the above rule is used to retrieve all facts satisfying it, we have the following view:

<table><tr><td></td><td>C#</td><td>Name</td><td>Forecast</td><td>Actual</td><td>City</td><td>Type</td></tr><tr><td>promote(</td><td>182,</td><td>&#x27;Morgan Building&#x27;,</td><td>2100,</td><td>800,</td><td>&#x27;Houston&#x27;,</td><td>3).</td></tr><tr><td>promote(</td><td>382,</td><td>&#x27;Blake College&#x27;,</td><td>1200,</td><td>285,</td><td>&#x27;Tucson&#x27;,</td><td>2).</td></tr><tr><td>promote(</td><td>391,</td><td>&#x27;Long Valley Cy.&#x27;,</td><td>2200,</td><td>1500,</td><td>&#x27;Snook&#x27;,</td><td>1).</td></tr><tr><td>promote(</td><td>397,</td><td>&#x27;High Range City&#x27;,</td><td>4100,</td><td>2000,</td><td>&#x27;Range&#x27;,</td><td>1).</td></tr></table>

## A.2.3. Representing Exceptions

To represent internal inclusions, assume that customers 'Valley Utilities' and 'T&L Roofing' will be offered the promotion. These customers are not included in the view. The representation can be made by listing their names (or another unique identifier such as customer number) in the following manner:

addition('Valley Utilities').

addition('T&L Roofing').

To represent omissions, assume that customers 'Blake College' and 'High Range City' will not be offered the discount although they qualify according to the rule. Note that these customers are included in the view. The representation can be made as follows:

exclusion('Blake College').  
exclusion('High Range City').

The assertion names “addition” and “exclusion” have, of course, no specific meaning in PROLOG. They were chosen only to make the example clear.

## A.2.4. The Modified Representation of the Rule

The representation of the rule must be modified to account for the internal inclusions and omissions. The modified representation becomes the following two statements:

promote(C#, Name, Forecast, Actual, City, Type)
if
    customer(C#, Name, Forecast, Actual, City, Type),
    Actual < Forecast \* 0.7,
    not exclusion(Name).

promote(C#, Name, Forecast, Actual, City, Type)
if
    customer(C#, Name, Forecast, Actual, City, Type),
    addition(Name).

The first statement can be interpreted as "a customer record will be selected if it satisfies the rule and it is not an exclusion". The second statement can be interpreted as "a customer record will be selected if it is a customer record and it is marked as an inclusion". Both statements will be used by the PROLOG processor, and a record will be selected if it satisfies either statement.

## A.2.5. Representing External Inclusions

External inclusions correspond to individuals not in the population S. Therefore all of their must be supplied. In PROLOG this representation can be easily made by using the same clause as for the rule:

<table><tr><td></td><td>C#</td><td>Name</td><td>Forecast</td><td>Actual</td><td>City</td><td>Type</td></tr><tr><td>promote(</td><td>105,</td><td>&#x27;Karen Holtz&#x27;,</td><td>1000,</td><td>0,</td><td>&#x27;Dallas&#x27;,</td><td>2).</td></tr><tr><td>promote(</td><td>128,</td><td>&#x27;Doris Shipman&#x27;,</td><td>2000</td><td>0,</td><td>&#x27;Flagstaff&#x27;,</td><td>3).</td></tr></table>

## A.2.6. Forming the Derived Relation with Exceptions

Using the statements given in section A.2.4 (the modified rule) and the external inclusion statements given in section A.2.5, the DRE can be obtained with the following PROLOG query:

promote(C#, Name, Forecast, Actual, City, Type)
giving as a result the following table:

<table><tr><td></td><td>C</td><td>Name</td><td>Forecast</td><td>Actual</td><td>City</td><td>Type</td></tr><tr><td>promote(</td><td>182,</td><td>&#x27;Morgan Building&#x27;,</td><td>2100,</td><td>800,</td><td>&#x27;Houston&#x27;,</td><td>3).</td></tr><tr><td>promote(</td><td>201,</td><td>&#x27;Valley Utilities&#x27;,</td><td>7800,</td><td>10500,</td><td>&#x27;Snook&#x27;,</td><td>1).</td></tr><tr><td>promote(</td><td>237,</td><td>&#x27;T&amp;T Roofing&#x27;,</td><td>150,</td><td>275,</td><td>&#x27;Tucson&#x27;,</td><td>3).</td></tr><tr><td>promote(</td><td>391,</td><td>&#x27;Long Valley Cy.&#x27;,</td><td>2200,</td><td>1500,</td><td>&#x27;Snook&#x27;,</td><td>1).</td></tr><tr><td>promote(</td><td>105,</td><td>&#x27;Karen Holtz&#x27;,</td><td>1000,</td><td>0,</td><td>&#x27;Dallas&#x27;,</td><td>2).</td></tr><tr><td>promote(</td><td>128,</td><td>&#x27;Doris Shipman&#x27;,</td><td>2000,</td><td>0,</td><td>&#x27;Flagstaff&#x27;,</td><td>3).</td></tr></table>

## References

[1] Arity Corporation, 1986, The Arity/SQL Development Package, Arity Corporation, Concord, Massachusetts.

[2] Berghel, H.L., 1985, Simplified Integration of PROLOG with RDBMS, Data Base, Vol. 16, No. 3 (Spring), pp. 3–12.

[3] Borgida, A., and Williamson, K.E., 1985, Accommodating Exceptions in Databases, and Refining the Schema by Learning from Them, Proceedings of VLDB 1985, Stockholm, Sweden.

[4] Brodie, M.L., and Jarke, M., 1986, On Integrating Logic Programming and Databases, in Expert Database Systems – Proceedings of the First International Workshop, L. Kerschberg (Ed.), The Benjamin/Cummings Publishing Company, Inc., Menlo Park, California, pp. 191–207.

[5] Chang, C.L., and Walker, A., 1986, PROSQL: A PROLOG Programming Interface with SQL/DS, in Expert Database Systems – Proceedings of the First International Workshop, L. Kerschberg (Ed.), The Benjamin/Cummings Publishing Company, Inc., Menlo Park, California, pp. 233–246.

[6] Clocksin, W.F., and Mellish, C.S., 1981, Programming in PROLOG, Springer-Verlag, Berlin, West Germany.

[7] Cohen, Paul R., and Feigenbaum Edward A., 1982, The Handbook of Artificial Intelligence Vol. 3, Kaufmann Inc., Los Altos, CA.

[8] Date, C.J., 1985, A Guide to DB2, Addison-Wesley Publishing Company, Reading, Massachusetts.

[9] Date, C.J., 1986. An Introduction to Database Systems:

Vol. 1, 4th edition, Addison-Wesley Publishing Company, Reading, Massachusetts.

[10] Furukawa, K., Takeuchi, A., Kunifuji, S., Yasukawa, H., Ohki, M., Ueda, K., 1984, Fifth Generation Computer Systems 1984: Proceedings of the International Conference on Fifth Generation Computer Systems 1984, North-Holland, Amsterdam.

[11] Gallaire, H., and Minker, J. (Eds.), 1978, Logic and Databases, Plenum Press, New York.

[12] Kellogg, C., 1986, From Data Management to Knowledge Management IEEE Computer, Vol. 19, No. 1, pp. 75–84.

[13] Kerschberg, L., 1985, Expert Database Systems (Workshop Review), Proceedings of ACM SIGMOD 1985, ACM SIGMOD, pp. 414–417.

[14] Kowalski, R., 1978, Logic for Data Description, in Logic and Databases, Gallaire, H., and Minker, J. (eds.), Plenum Press, New York.

[15] McCabe, D., and Clark, K., 1982, micro-PROLOG: Programming in Logic, Logic Programming Associates, London.

[16] Missikoff, M., and Wiederhold, G., 1986, Towards a Unified Approach for Expert and Database Systems, in Expert Database Systems – Proceedings of the First International Workshop, L. Kerschberg (Ed.), The Benjamin/Cummings Publishing Company, Inc., Menlo Park, California, pp. 383–400.

[17] Moto-Oka, T. (Ed.) 1981, Fifth Generation Computer Systems: Proceedings of the International Conference on Fifth Generation Computer Systems, North-Holland, Amsterdam.

[18] Parker, D.S., Carey, M., Golshani, F., Jarke, M., Sciore, E., and Walker, A., 1986, Logic Programming and Databases, in Expert Database Systems – Proceedings of the First International Workshop, L. Kerschberg (Ed.), The Benjamin/Cummings Publishing Company, Inc., Menlo Park, California, pp. 35–48.

[19] Ramirez, R.G., 1987, Derived Relations with Exceptions, Ph.D. dissertation Texas A&M University.

[20] Ramirez, R.G., Dattero, R., and Choobineh, J., 1986, Extensions of Relational Views to Derived Relations with Exceptions, submitted for publication.

[21] Reiter, R., 1978, On Reasoning by Default, Proc. TINLAP-2, Theoretical Issues in Natural Language Processing-2, University of Illinois at Urbana-Champaign, pp. 210–218, reprinted in Readings in Knowledge Representation, Brachman, R.J., and Levesque, H.J., Morgan Kaufmann Publishers, 1985.

[22] Reiter, R., 1980. A Logic for Default Reasoning, Artificial Intelligence, Vol. 7, No. 2, pp. 81–132.

[23] Reiter, R., 1984, Towards a Logical Reconstruction of Relational Database Theory, in On Conceptual Modeling, Brodie, M.L., Mylopoulos, J., and Schmidt, J.W. (Eds.), Springer-Verlag, New York.

[24] Rich, E., 1983. Artificial Intelligence, McGraw-Hill, New York.

[25] Sciore, E., and Warren, D.S., Towards an Integrated Database-PROLOG System, in Expert Database Systems - Proceedings of the First International Workshop, L. Kerschberg (Ed.), the Benjamin/Cummings Publishing Company, Inc., Menlo Park, California, pp. 293–305.

[26] Smith, John Miles, 1986, Expert Database Systems: A Database Perspective, in Expert Database Systems – Proceedings of the First International Workshop, L. Kerschberg (Ed.), The Benjamin/Cummings Publishing Company, Inc., Menlo Park, California, pp. 3–15.

[27] Stonebraker, M., Woodfill, J., and Andersen, E., 1983, "Implementation of Rules in Relational Data Base Systems", IEEE Data Engineering, December 1983.

[28] Tsichritzis, D., and Lochovsky, F., 1982, Data Models, Prentice-Hall, Englewood Cliffs, NJ.

[29] Tsur, S., and Zaniolo, C., 1986, LDL: A Logic-Based Data-Language, MCC Technical Report Number DB-026-86, February 11, 1986.

[30] Vassiliou, Y., Clifford, J., and Jarke, M., 1985. Access to Specific Declarative Knowledge by Expert Systems, Decision Support Systems Vol 1 (1985), pp. 123–141.

[31] Zaniolo, C., 1986, PROLOG: a Database Query Language for All Seasons, in Expert Database Systems – Proceedings of the First International Workshop, L. Kerschberg (Ed.), The Benjamin/Cummings Publishing Company, Inc., Menlo Park, California, pp. 233–246.
