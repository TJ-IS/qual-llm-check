---
otero_id: 17128
otero_key: "DC36JF3F"
title: "Deductive data modeling: A new trend in database management for decision support systems"
authors: "Arun Sen; Joobin Choobineh"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90013-h"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Deductive Data Modeling: A New Trend in Database Management for Decision Support Systems

Arun SEN and Joobin CHOOBINEH

Department of Business Analysis, College of Business Administration, Texas A & M University, College Station, TX 77843, USA

Researchers in the data base area are now placing more and more emphasis on deductive data base management systems (D-DBMS). This paper discusses the use of D-DBMS in decision support systems (DSS). A D-DBMS is an outgrowth of deductive systems in Artificial Intelligence (AI) and data base management systems (DBMS). Initially, the paper discusses deductive systems and evaluative systems. A framework is then presented which ties the two systems together. A macro definition of a deductive data model is also presented.

Keywords: Deductive Database, Data Modeling, Decision Support System (DSS), Artificial Intelligence.

![](/api/attachments/DC36JF3F/fulltext/images/5534661ae4f62c39131114ba3f9be2fc1d499984028fd07c33c2ded2af468e2f.jpg)

Arun Sen is an Associate Professor in the Department of Business Analysis and Research, College of Business Administration, Texas A&M University. Prior to joining the faculty at Texas A&M, he was an Associate Professor in the Management Science department in University of South Carolina at Columbia. He holds an M. Tech. degree in Electronics from the Center of Advanced Study in RadioPhysics and Electronics, Calcutta University (India); an M.S. in Computer Science and a Ph.D. in Business Administration (MIS) from Pennsylvania State University. His research interests include Data Base Management Systems, Deductive Data Bases, Decision Support Systems, Business Expert Systems and Distributed Networks. He has published extensively in different journals including Information Systems, Information Science, J. of MIS, Computers and OR, MIS Quarterly, Decision Support Systems, Information and Management, Simulation and Data and Knowledge Engineering. He has also published articles in different Conferences including DSI, ICIS, HICSS and IEEE Intl. Conf. on Man, Systems and Cyberntics.

## 1. Introduction

Database systems evolved in response to the need for efficient management of large amounts of data. Database systems, unlike file systems, are designed to be logically independent from the actual physical storage of data. The core of a database system is a data model. A data model is defined as an abstraction to represent and manipulate data at the logical level. A typical data model provides a representation mechanism, called DDL (Data Definition Lanaguage), and a manipulation mechanism, called DML (Data Manipulation Language).

Most of the earlier data models provide computer-oriented representation and manipulation techniques. For example, Relational Data Model [10] adhere to the table representation that is common in computing world. Hierarchical Data Model, on the other hand, organize data in simple tree structures. These traditional, record-oriented data models do not have facilities to represent complex information structures that are common in decision support systems and/or in knowledge base systems. They also do not support complex operations, which are more than data update and

![](/api/attachments/DC36JF3F/fulltext/images/9b7b837ba5ef39367c27c3b48d463349236ce116576fb9267a30249b2f4be874.jpg)

Transactions on Software Engineering, Database Engineering, Proc. 5th Intl. Conf. on Entity-Relationship Approach, and Proc. of the 19th, 21th, and 22 Hawaii Intl. Conf. on Systems Sciences, and Proc. 8th Intl. Conf. on Information Systems. Dr. Choobineh is a member of the Association for Computing Machinery (ACM), Decision Sciences Institute, IEEE Computer Society, and The Institute of Management Science.

Joobin Choobineh received the Ph.D. Degree in management information systems from the University of Arizona, Tucson in 1985. He is an Assistant Professor in the Department of Business Analysis and Research, College of Business Administration, Texas A&M University. Prior to joining the faculty at Texas A&M, he was Research Associate in the Department of Management Information Systems at the University of Arizona. His research has been published in IEEE retrieval. These models are more machine-oriented.

Table 1  
Conventional Database Problems.

<table><tr><td>Problems</td><td>Description</td><td>References</td></tr><tr><td>Incomplete Data</td><td>Case-1: Disjunctive dataCase-2: Null ValuesCase-3: Negative dataCase-4: Fuzzy data</td><td></td></tr><tr><td>Disjunctive Data</td><td>The data appears as (Q OR R)(For example, emp-age is 40 OR 42.)</td><td>[20,33]</td></tr><tr><td>Null Values</td><td>(a) Value at present unknown, but it belongs to one of the finite set of possible values. (Example: emp-age is 40 OR 41 OR ... 60.)(b) Value at present unknown, yet not necessarily one of some finite set of known possible values.(Example: EMP-PROJ (name, pid) can have a tuple where pid can be null.)(c) Relationship between attributes known, yet actual values of attributes unknown.(Example: YOUNGER (younger-emp, older-emp) known without knowing either person&#x27;s age.)</td><td>[20,30,45]</td></tr><tr><td>Negative Data</td><td>An attribute has negative value. (Example: emp-age is NOT 42.)</td><td>[20,33]</td></tr><tr><td>Fuzzy Data</td><td>An attribute does not have a quantitative value. (Ex: emp-age is middle age.)</td><td>[35]</td></tr><tr><td>Query Optim.</td><td>Additional reduction in query processing cost can be obtained by using higher-level info. (syntactic/semantic) over statistical information.</td><td>[23]</td></tr><tr><td>Extensions to Query Language</td><td>Extend the query language using natural language concepts</td><td>[20]</td></tr></table>

Table 1 (continued)

<table><tr><td>Problems</td><td>Description</td><td>References</td></tr><tr><td>Incremental Query Formulation</td><td>System helps the user construct the query</td><td>[11]</td></tr><tr><td>Integrity Constraints</td><td>Constraints modelled in first-order logic and checked</td><td>[20]</td></tr><tr><td>Database Design</td><td>Logical design of data base Formalization of dependencies in pred. logic</td><td>[8,20]</td></tr></table>

The need to organize and manipulate data for a more complex environment had led researchers to develop semantic data models. These models are rich in abstracting the semantics of the environment that affect the data. There are several approaches: Entity–Relationship (ER) model [7], Functional data model [40], Semantic Data Model (SDM) [22], extensions of Relational Model (like generalization and aggregation [41], RM/T [12]), Concept–Relationship model [15], and Enterprise model [38]. The extent of semantics captured by each of these data models varies, with ER being the lowest and Enterprise model the highest.

Current trend in database research [26,27] is to adopt the AI techniques for “deduction.” We do this, even when there are some fundamental differences between the two technologies [2]. In database, representations tend to be biased toward a large number of instances of a small number of formatted data types. Knowledge representations in AI are designed to deal with a small number of instances of a much larger variety of types and classes. Knowledge bases are usually specially tailored toward an application, while databases are often constructed to help a community of users. Heuristics play a major role in the AI systems, while they are virtually non-existent in databases.

There are some existing problems that cannot be solved unless we exclusively use “deductions.” A list of these problems is provided in table 1. This includes representation of null values, query optimization, and extensions to the query languages. A list of references is also provided in the table.

Table 2
New Database Problems.

<table><tr><td>Problems</td><td>Description</td><td>References</td></tr><tr><td>Complex Object</td><td>An object is composed of attributes, which can be atomic, or other objects. A complex object has attributes that are complex. (Ex: in “employee” object, only grad. year is kept for high school grads, while a degree descrpn. with major and grad-yr. is kept for coll-grad.)</td><td>[46]</td></tr><tr><td>Virtual Data Types</td><td>Some information may not be explicitly stored in the database. (Example: FATHER (x, y), which denotes x is a father of y, is a base relation. ANCESTOR rules can be added to get a virtual relation, ANCESTOR (x, y).)</td><td>[6]</td></tr><tr><td>Recursive Queries</td><td>How do we design stopping rules for Recursive Query?</td><td>[6]</td></tr><tr><td>Degrees of Plausibility</td><td>Answer to queries can be approximate Premises can have diff. degrees of plausibility</td><td>[24,25]</td></tr><tr><td>What-if Queries</td><td>Decision Support System (DSS) can have these types of queries</td><td>[24,25]</td></tr><tr><td>Explanation Facility</td><td>The system supplies evidence for or against the answer</td><td>[24,25]</td></tr><tr><td>Heuristic Representat.</td><td>Database should allow heuristics</td><td>[44]</td></tr><tr><td>Integrity Relaxation</td><td>Query does not need to be rejected if it does not satisfy integrity constraints totally</td><td>[19]</td></tr></table>

There are still other problems that are new. They arise from the current research in extending database capabilities. Table 2 provides another list of these problems and some references. The list includes representation of complex objects, definition of virtual data types, introduction of plausible reasoning in databases, what-if queries, and explanation facilities.

The objective of this paper is to provide a basis for proposing a “deductive data model.” A deductive data model is a “deductive” extension of a conventional data model. Like conventional data models, it must provide representation and manipulation techniques. However, these techniques will be far more complex in nature as the data base will do more than just data retrieval and update. This area of deductive data modeling can only be understood if we discuss some underlying issues clearly. They are:

(i) What is deduction? What constitutes a deductive system?

(ii) What is evaluation? What constitutes an evaluative system?

(iii) How do we accomplish the integration of deductive and evaluative components in a deductive data base management system?

Section 2 discusses deduction and the components of a deductive system. Section 3 deals with the evaluation. Section 4 involves the unification and describes the basic ingredients of a deductive data model. Finally, we conclude this paper in section 5.

## 2. Deductive Systems

According to Barr and Feigenbaum [1], when a system is required to do something that it has not been explicitly told how to do, it must reason - it must figure out what it needs to know from what it already knows. Reasoning is the very basis of human problem solving. There are various kinds of reasoning that humans use [1,21].

A widely investigated reasoning technique is Deduction. It is defined as a method of inference where a conclusion is arrived from given premises. That is, new facts are generated from known facts. To illustrate, suppose we have a knowledge base of personnel information for a company and we want to know whether there is any programmer who earns more than a vice-president earns [13]. Let us suppose that we do not have any specific salary information for each employee. Instead, we may have general information about classes of employees, such as:

(i) All vice-presidents are managers.

(ii) All programmers are professionals.

(iii) All professionals earn less than all managers.

From this information, we can deduce that no programmer earns more than any vice-president, although we have no information about the exact salary of any employee. Typically, we use “modus ponens” or “modus tolens.” Modus ponens suggest that if A implies B, and A is a true statement, then B is true. Modus tolens is defined as if A implies B, and B is a false statement, then A is also a false statement.

Other reasoning techniques include induction, analogical reasoning, probabilistic, inexact, meta-level, and nonmonotonic. A complete treatment of different types of reasoning and further references can be found in [1,21].

Some AI systems have been designed to see if the computer programs can deduce like humans. AI techniques that are used include: predicate logic systems, production systems, frame systems, procedural systems and semantic networks. Typically, a Deductive system (AI system that does deductions) has the following components:

(a) Knowledge Representation: It is an abstract representation of facts and heuristics of an expert. In a logic system, well-formed formulas (predicates, variables, constants, and functions) form the components of a knowledge structure. In rule or production systems world, the representation is in the form of “if-then” rules. other forms are frames, semantic nets and procedures.

(b) Control Structure: It guides the search process that is inherent in any AI system. There are different kinds of control. They include:

a. Forward chaining (begin from the start states),

b. Backward chaining (begin from the goal states),

c. Bidirectional (begin from both ends), and

d. Opportunistic (bidirectional but begin from an intermediate position).

(c) Inferencing Scheme: It is a technique to reason in a deductive system. Various types of inferencing techniques exist. For example, in predicate logic, resolution algorithm has been used along with modus ponens and modus tolens.

Rule-based systems have used modus ponens, coupled with improved search techniques and good pattern-matching (as in OPS-5 [18]). Dempster-Shafer [39] is an example of inexact inference technique used in a deductive system. Conflict resolution and consistency enforcement of the intermediate and final results are also important in inferencing.

(d) Heuristics: They are backbone of any AI system. A heuristic is a technique that improves the efficiency of a search process, possibly by sacrificing completeness. Heuristics are tour guides. Some heuristics help to guide a search process without sacrificing any claims in completeness that the process might previously have had. Others may occasionally cause an excellent path to be overlooked. But, on the average, they improve the quality of the paths that are explored.

(e) Searching: It is another important aspect of any AI system. Every search process can be viewed as a traversal of a directed graph in which each node represents a problem state and each arc represents a relationship between states represented by nodes it connects. There are many types of searches including hill climbing, generate and test, breadth first, depth first, and beam. Traditionally, all searches in a deductive system are in-core searches.

(f) Pattern Matching: The method of pattern matching between the current state and the preconditions of the rules uses the entire collection of rules and extracts those that can be applied at a given point. Pattern matching facilities do two major tasks: finding entries in data set and choosing which procedure to execute next. Typically, a pattern is a structure with variables embedded in it, and it matches another structure if it could be made identical to that structure by replacing variables with some values. There are several ways this can be accomplished. They include: indexing, matching with variables, and approximate matching.

## 3. Evaluative Systems

In order to understand the use of deduction in databases, we need to explore how we use database systems and where it differs from a “deductive” system. A DBMS is an “evaluative” system and not a “deductive” system. Taking the earlier example in section 2, if the same query (“we want to know whether there is any programmer who earns more than a vice-president earns”) is now asked against a database, the system will simply find the salary of each programmer and compare it with the salary of every vice-president. No deduction is involved in this process and it is purely evaluative.

If we look at the components of such an evaluative system, we find that it has two major categories: logical and physical. The physical part deals with the actual files and file accesses. The main emphasis here is on the record structuring, access patterns, and secondary storage searching.

The logical part has been introduced to effectively implement the independence from the file systems. The components of the logical category are as follows [42].

(a) Data Structure: It is an abstract representation of data. Examples range from relations (relational data model) to graphs (semantic data model).

(b) Constraints: They are the logical restrictions on data. A constraint is a property which, for an object or a collection of objects, is either true or false. Constraints are required in the data base for semantic and integrity reasons. In terms of semantics, they permit schemas to more accurately reflect the real-world situation. In terms of integrity, they permit the DBMS to restrict the possible data base states that can be generated from a given schema to those that meet the constraints. Thus, if in the real world no employee is allowed to earn more than his or her manager, then by means of suitable constraints we are able to express this requirement in the schema.

(c) Selection: Selection selects a part of the database to which an action is to be applied. There are various types of selection processes: (i) Logical position, (ii) Value of the contents of the database, and (c) Relationships among the data. We can select data based on their logical position in a table or a node in a graph. Data may not need to be ordered in the data model, but it certainly has an order at the time of implementation. This order can be exploited to provide selection by the logical position in a table or node in a graph. Thus, we may be able to select the first, last, next, prior, or nth row in a table. This is selection thru currency. Another way the selection can be done is through the content addressibility. We can select data according to the values in a row of a table or a node in a graph. Finally, we can also select data according to logical relationships with other data. This is called data relatability. For example, if there is relationship type OWNERSHIP between entity types PERSON and CAR, we can select all people who own cars or all cars owned by people.

(d) Action: Once the place has been selected in the database, the action specifies what is to be done. Traditionally, an action in record oriented databases is one of, or a combination of, five generic operations: (i) Set currency, (ii) Retrieve, (iii) Insert, (iv) Delete, (v) Update, and (vi) Connect to or disconnect from other record types. Selection and action taken together form “operation.”

(e) Database Procedure: This is a type of operations in the data base that does not follow the selection and action types. A data base procedure consists of a series of operations which are executed upon the satisfaction of certain conditions. For example, consider an “integrity mechanism” which is triggered when particular data is selected. The integrity mechanisms can potentially check many data objects to verify a constraint. Since the condition can be general, the procedures may be triggered automatically without the user intervention.

## 4. Toward A Unifying Architecture: A Deductive Data Model

From tables 1 and 2, we see that researchers have attacked different types of deductive database problems. This has caused some confusion and it is difficult to precisely define a deductive database system. To clear up this problem, we will first categorize the intelligent database research, and then proceed to discuss deductive database management issues in a DSS context.

## 4.1. Spectrum of Intelligent Database Research

Following Missikoff and Widerhold [32], Vassiliou et al [43] and Lafue and Smith [31], we find that the intelligent database research can be categorized as follows.

(1) Database within a Deductive System: The whole population of specific declarative knowledge (i.e., the data base) can be represented directly in the knowledge base formalism of the deductive system. These fomalisms include semantic networks, frames, and rules. This strategy assumes that all the facts reside in the main memory during the operation of the system. However, it presents an obvious limitation on the size of the declarative knowledge population.

(2) Generalized Database within a Deductive System: Often a very large population of specific knowledge is required by a deductive system. A generalized DBMS (needed to manage it) may be implemented as a sub-process of such a deductive system. If another generalized DBMS is already in place managing this database, it may be very costly to maintain a separate copy just for the deductive system.

(3) Enhancement of the Deductive System with Database Features: This means that an existing deductive system is expanded with some database features. For example, one can extend a deductive system with constraint management techniques or expand a PROLOG-type programming language with a secondary storage access capability.

(4) Intelligent Database Interface: This approach exemplifies a system that can be interfaced with a traditional DBMS. Depending on the nature of communication between the two independent systems (deductive systems and DBMS), there are two types of strategies: loose coupling and tight coupling. Conceptually, loose coupling of a deductive system with an external DBMS is enforced by extracting a snapshot of the required data from the DBMS when the deductive system begins to work on a set of related problems. This portion of the database is stored in the internal database of the deductive system. Loose coupling assumes that an intelligent mechanism exists which can figure out in advance which portion of the database is required for extraction. It is inefficient when different portions of the database are needed for the deductive system at different times. In the tightly coupled interface, a large database exists under a generalized DBMS. The deductive system needs to consult this database at various points during its operation. In this case, an online communication channel between the deductive system and DBMS is required. Queries can be generated by and transmitted to the internal knowledge representation. Thus, in tight coupling, the deductive system must know both when and how to consult the DBMS, and must be able to understand the answers.

(5) DBMS Enhancement with Knowledge System Features: This effort includes extending an existing DBMS to use some of the facilities needed by Knowledge base systems. Related to this effort are attempts to integrate knowledge modeling features such as generalizations into the relational data models; heuristic query optimization; and incremental query formulation and understanding.

(6) Deductive DBMS: Deductive database management system (D-DBMS) can be seen as an evolution of DBMSs, both in terms of type of objects managed and functions performed. Additional functions and new object types aim to endow the deductive database with the ability to manage knowledge and obtain the deductive power of AI systems.

This research is concerned with the last approach. It is the most complex of all the categories mentioned above. The D-DBMS is a de novo approach and is difficult to design. The reasons are:

(i) Data Representation: A D-DBMS must be able to represent data in some type of knowledge structure. $^{1}$ This means one must require a D-DBMS to provide a data definition language that allows a representation of knowledge, rather than simple formatted record-oriented data. It should also be able to represent complex objects [46].

(ii) Constraint Specification and Enforcement: Integrity constraints need to be specified and enforced in a D-DBMS, for virtual data as well as explicitly stored data.

(iii) Traditional Database Operations: A D-DBMS should be able to provide traditional database operations (including selection and action), like modify, delete, insert etc. It should also provide database procedures as options.

(iv) Multiuser Environment: Like traditional DBMS, a D-DBMS will be used by several users. Each may have different external views. These views can be simple data views or complex knowledge views. Data views involve user requirements for explicitly stored data. However, knowledge views are user requirements for data that can be deduced.

![](/api/attachments/DC36JF3F/fulltext/images/2fff9c4debf73b0674cef833f400a754107b9d5facca193bf81f34ee311ff735.jpg)  
Fig. 1. Different Data Types in a DSS.

(v) Security: As the D-DBMS will be used by a group of users, the security of data is of vital importance. This involves the security of both explicit and virtual data.

(vi) Efficient Physical Design: The D-DBMS should have efficient access strategies and file design.

(vii) Logical Design: Like all traditional DBMSs, a D-DBMS should have a database design process to define its data requirements. This means a D-DBMS should have some data model that can be used to model different views – both data and knowledge. D-DBMS also needs ways to integrate these different views to form a global view. The logical database design process [34] should be extended for D-DBMS.

(viii) Application Independence: The D-DBMS should be a general purpose system with a spectrum of applications covering a large set of application domains.

(ix) Expandability: D-DBMS should be designed in such a way that it can be expended easily when new information arrives. This new information can be temporal data, geometric data, text information, or recursive predicates [14].

(x) Deductive Power: This is vital and comes from the expert system technology. The D-DBMS should implement large set of functions that are related to deduction. This includes modus ponens, modus tolens, Dempster-Shafer, and fuzzy reasoning.

(xi) Deductive Toolkit: The D-DBMS is a general purpose system. Hence, it should provide different types of control structures, inference techniques, knowledge representation tools and search strategies.

(xii) Explanation Facility: The system must be able to explain during its processing and once it has found a solution, the reasoning by which it reaches any state.

(xiii) Heuristics Representation: The D-DBMS makes use of several types of heuristics, like search direction control, search reduction, and application-specific. These heuristics should be properly represented.

## 4.2. Deductive Data Base Management System and DSS

Every conventional DBMS is based on a data model. Systems, like INGRES and SQL/DS, are developed from the relational data model [10]. A D-DBMS also needs a deductive data model (DDM). We now discuss a framework for DDM.

A new trend in decision support system (DSS) is to use a data base management system with deductive power. The term first appeared in journal articles and in conferences in early 1970s [3]. Computers were usually integrated into such systems as support mechanism; as a whole, these came to be known as Decision Support System.

A DSS is defined as a collection of several tools: data management, analytical techniques, report generators and graphics [37]. Moreover, these tools need to communicate with one another so that they can collectively support managerial decision-making process.

![](/api/attachments/DC36JF3F/fulltext/images/3c6da7d0170f4d348fd0e12430e0a56a3f905f160b7a8b35e8a97802762f0ad7.jpg)  
Fig. 2. Different Categories of $d^{v}$ Data Types.

The traditional definition and the design considerations of a DSS have gone through a metamorphosis over the past decade particularly because of users' insistence to make the software more and more "user-friendly." This trend can be seen in the works of Donovan [16], Elam [17], Bonczek et al. [3], Konsynski [28], Lee [29] and others. The trend is toward building a smart DSS, using the notions of artificial intelligence. As DSS needs a database system, this new impetus in DSS has forced researchers to look into deductive database management systems.

A DSS can be modeled as a D-DBMS whose data types are shown in fig. 1. Three kind of data types are common in a DSS. They are: explicit data types ( $d^{e}$ ), virtual data types ( $d^{v}$ ) and displayed data types ( $d^{d}$ ). The explicit data types are typically stored in a traditional database. There are two types of $d^{e}$ : simple and complex. Examples of simple $d^{e}$ are EMPLOYEE and STUDENT. The complex $d^{e}$ resemble complex objects [46]. Examples of complex objects $d^{e}$ are line drawings of CAD, graphics and object with conditional attributes. The virtual data types are not explicitly stored in the database and are deduced (symbolic computation) or computed (numeric computation) in the derivation phase (fig. 1). The $d^{e}$ and $d^{v}$ data types can be displayed by report writer or graphics programs (the display phase in fig. 1). The $d^{d}$ are data types that are displayed.

![](/api/attachments/DC36JF3F/fulltext/images/e8a975425990bb2cf7cebf476a89c14ca7f5d618e5fb1580d8cc8f8d82b2f34f.jpg)  
Fig. 3. Different Categories for $d^{d}$ Data Types.

Fig. 2 depicts the categories of virtual data types. We broadly classify $d^{v}$ into types derived by numeric computation and types derived by symbolic computation. The numerically computed data types include – arithmetic, optimization, and statistical subtypes. Symbolically computed data types can be classified into two categories depending upon the complexity of the deduction process. First is simple derivation which includes: functional and inheritance (is-a). The complex derivation includes: logical, imprecise, and procedural.

Finally, the categories of displayed data types, $d^{d}$ , are shown in fig. 3. $d^{d}$ data types are typically obtained from either $d^{e}$ or $d^{v}$ or both. Some type of display operations are performed on these data types. The categories in fig. 3 reflect some of them.

## 4.3. The Deductive Data Model (DDM)

At a macro level, the DDM consists of a set of generating rules G and a set of operations 0. The set of generating rules can express the static properties of DDM. It defines the allowable structures for the data within the data model. The structures are specified in two complementary ways. The allowed objects or relationships are specified using generic rules for the definition of their categories. Disallowed objects or relationships are excluded by defining restrictions, called constraints.

The set of operations 0 define the dynamic properties of the world. There are five types of operations in a DDM. First, the set of allowable actions, like insert, delete, retrieve and modify, that can be performed on $d^{e}$ under traditional data models. Second, a set of allowable operations that work on $d^{v}$ . Third, a set of truth maintenance operations that act on $d^{e}$ to check the validity of constraints. Fourth, a set of operations that can derive $d^{v}$ data types. Finally, a set of operations for $d^{d}$ data types that can reformat $d^{v}$ or $d^{e}$ data type instances for display.

DDM can now be described as

$$
\begin{array}{l} \text {DDM can flow be described as} \\ \mathrm{DDM} = \left[ \mathrm{G} (\mathrm{d} ^ {\mathrm{e}}), \mathrm{O} (o _ {1}, o _ {2}, o _ {3}, o _ {4}, o _ {5}) \right], \quad \text {where} \\ o _ {1}: \text {traditional database operations on d} ^ {\mathrm{e}} \\ o _ {2}: \text {deductive database operations on d} ^ {\mathrm{v}} \\ o _ {3}: \mathrm{d} ^ {\mathrm{e}} \Rightarrow (\text {true, false}) \quad \text {truth maintenance} \\ o _ {4}: \mathrm{d} ^ {\mathrm{e}} \Rightarrow \mathrm{d} ^ {\mathrm{v}} \quad \text {deduction} \\ o _ {4}: \mathrm{d} ^ {\mathrm{e}} \text {or d} ^ {\mathrm{v}} \Rightarrow \mathrm{d} ^ {\mathrm{d}} \quad \text {display} \end{array}
$$

The $\Rightarrow$ sign denotes a multi-step process. For example, in truth maintenance, each time an instance needs to be inserted, its validity will be checked automatically to keep the data base consistent. This process may take several steps to finish. Similar examples can be demonstrated for $o_{4}$ and $o_{5}$ .

This multi-step process needs various kinds of knowledge bases (KB). They include: domain laws, structural laws, procedural knowledge, application-specific knowledge, and enterprise knowledge [9,44].

Domain and structural laws are considered general laws. We define general laws as real world rules which should be followed. These laws are typically common knowledge and are available to everybody. Domain laws are a set of rules that maintains the integrity of the domain of the object types. Examples are: integers, reals, time etc. Structural laws are defined to be the knowledge we have about dependencies and constraints among the data, restricting ourselves to general and intensional information. An example of a structural knowledge concept is a functional dependency constraint like employee → department.

Procedural knowledge is the knowledge about appropriate methods and procedures, given some set of data. Many decisions must be made to select and properly invoke the computational procedures which will produce the desired result for a query. Making the wrong choice can lead to processing failures, errors in the result, and wasted resources.

Application-specific knowledge is potentially a large body of knowledge that is associated with each application.

Enterprise knowledge is the knowledge at the highest level of abstraction. It involves rules that are typically used by the strategic planners.

There are three other components that indirectly contribute to $o_{3}$ and $o_{4}$ . They are: control structure (CS), numeric computation (NC), and symbolic computation (SC). We define the control structure as a mechanism that actually guides the search process that is inherent in any AI-oriented system. Different types of control structures were described in Section 2. Numeric computation technique includes arithmetic computations, optimizations and so on. Symbolic computation technique or deduction defines the method in which the deduction is to be carried out. For example, in predicate logic, one typically uses resolution principle. IN rule-based systems, researchers have used improved search techniques coupled with good pattern-matching. For inexact reasoning, certainty factor and Dempster-Shafer techniques have been used. Hence, DDM can be rewritten as

$$
\mathrm{DDM} = \left[ \mathrm{G} \left(\mathrm{d} ^ {\mathrm{e}}\right), \mathrm{O} \left(\mathrm{o} _ {1}, \mathrm{o} _ {2}, \mathrm{o} _ {3}, \mathrm{o} _ {4}, \mathrm{o} _ {5}\right) \right], \quad \text { where }
$$

$$
\begin{array}{l l} \mathrm{o} _ {1}: \text {traditional   database   operations } \\ \mathrm{o} _ {2}: \text { deductive   database   operations } \\ \mathrm{o} _ {3}: \mathrm{d} ^ {\mathrm{e}} \xrightarrow [ K B , C S , N C , S C ]{} (\mathrm{t}, \mathrm{f}) & \text { truth } \\ \mathrm{o} _ {4}: \mathrm{d} ^ {\mathrm{e}} \xrightarrow [ K B , C S , N C , S C ]{} \mathrm{d} ^ {\mathrm{v}} & \text { maintenance } \\ \mathrm{o} _ {5}: \mathrm{d} ^ {\mathrm{e}} \text { or } \mathrm{d} ^ {\mathrm{v}} \xrightarrow [ K B , C S , N C , S C ]{} \mathrm{d} ^ {\mathrm{d}} & \text { display } \end{array}
$$

This macro definition of a deductive data model conforms to what Gallaire et al. [20] call a definite deductive data model. The elementary facts are the instances of $d^{e}$ data types. The deductive laws correspond to $o_{4}$ . The integrity constraints are included in KB and mapped by $o_{3}$ .

## 4.4. Deductive Data Model and Formal Logic

There has been a tendency in the deductive database research to embrace logic as the main tool. It is true that logic, as a prime candidate for deductive databases, has several unparallel advantages. They are [36]:

(i) Logic is precise and unambiguous.

(ii) Logical data models provide a very high level of abstraction because there are no database operations. They are entirely nonprocedural.

(iii) A logical data model is transparent. All and only knowledge being represented is open for inspection, including assumptions that might otherwise be buried in procedurally oriented data models.

(iv) Because they are specifications, logical data models can be realized in a variety of ways by procedurally oriented data models. Such data models can be proven correct and complete with respect to the logical specifications that they realize.

There are, however, strong oppositions [4,5,13,24,25,36] that have been raised against the application of logic in deductions and deductive data models. Early AI systems demonstrated the general-purpose nature of mechanized logic but suffered from severe performance problems. The problem becomes more perverse, as deciding whether or not a sentence in first-order logic is a theorem is unsolvable. Even if we restrict the language practically to the point of triviality by eliminating the quantifiers, the decision problem, though now solvable, does not appear to be solvable in anywhere near reasonable time. Many AI researchers are now looking at techniques that are perhaps more limited, but are more efficient. It has been argued that First Order Logic perhaps should only be used if there are doubts about the clear semantics of new data base concepts.

## 4.5. FLEX: A Deductive Database Management System

In this section we describe the architecture of FLEX, a deductive database management system, which we are presently in the process of design and implementation. The following criteria are established for the development of FLEX:

1. support of inferencing and truth maintenance;

2. efficient processing of recursive queries;

3. support for non-normalized relations;

4. support for plausible reasoning which implies that the facts in the database are no longer 100% true;

5. ability to explain why and how questions, that is, why the system is pursuing this information, and how did it arrive to this state;

6. facilities to retrieve, insert, delete, and update facts, and rules.

Facts in FLEX will be represented as non-normalized relations which can be organized into various abstraction hierarchies. The objects, which are represented as non-simple tuples, are further augmented by rules of behavior which are called general laws and heuristics [9].

Two types of implications will be supported in FLEX. The situation-action rules are used for their side effects in enforcing integrity constraints and implementing triggers and alerters. The general rules are used for deriving values for virtual fields from the explicitly stored data. General rules are similar to view definition of modern relational DBMS but they can also be used to define recursive relationships.

In answering queries, as in KM-1 [24,25], the control mechanism of FLEX uses forward chaining (what if), backward chaining (find), and bi-directional (given-find) techniques. The deduction techniques are based on resolution and inheritance.

We will use SQL as our basic user interface and augment it with new data definition and manipulation constructs in order to be able to accommodate the above criteria. SQL is chosen due to its popularity as a database language.

The software environment will be homogeneous. A tight coupling will be employed. There will be one language which is used for both evaluation and deduction. The system will be tightly integrated; data and rules use each other as the need may arise.

Fig. 4 depicts the architecture of the FLEX. Users interact with the system through a common interface which include Data Definition, Data manipulation, Rule definition and Rule Manipulation. A planning component manages the distribution of user requests through three engines. The evaluative engine can search through various knowledge components for retrieval of explicitly stored knowledge. The deductive engine performs inferential search to satisfy deductive queries which involve derived facts. Upon an insert, delete, or update of any of the knowledge bases, the truth maintenance engine searches knowledge components for violation of constraint rules, conflicts in stored knowledge, and derivability of the new request from the knowledge bases.

![](/api/attachments/DC36JF3F/fulltext/images/76c088bca0aa0fdbf286c21c0f0a65e482fb547b2f5e32ea325bc2beb67a06d7.jpg)  
Fig. 4. The Architecture of FLEX.

The knowledge base of a system developed through FLEX will be composed of four components. The Data Dictionary contains description of data such as their types, domains, derived or explicit, keyes, and indexes. The Database contains the explicitly stored data. The General Laws Base contains the integrity constraint rules triggers and alerters as well as the deductive laws for inference of derived facts. The Heuristics Base contains the experts' knowledge about the procedures, application domain, and organization. This knowledge is typically judgemental.

## 5. Conclusions

A very important ingredient of a decision support system (DSS) is a database management system (DBMS). Over the last two decades, research and development in the database area have resulted in efficient management of large stored data with the subsequent benefits to the DSS community. Recent implementations of expert systems and artificial intelligence techniques have influenced the database community to pursue research on integration of some of these techniques into the database management systems.

The paper attempts to explore the unification of these three areas: database, artificial intelligence, and decision support systems. In particular, we focused on the deduction aspect of intelligent systems and its integration with databases in a decision support context.

A macro deductive data model (DDM) has been developed. The nature and components of the deductive and evaluative systems had to be examined in detail before proposing the DDM. The DDM models various types of data including virtual data types (which are not explicitly stored in the database but rather are derived through various techniques). One important technique for derivation of virtual symbolic data is formal logic with all its inherent drawbacks.

Implementation of a deductive database management system in the context of DSS requires further research. Some other knowledge representation techniques such as semantic networks may be used instead of logic to represent the symbolically derived data. We feel that this area of research will become more important as we move toward integrating different tools with database systems to build more effective decision support systems. An overview of our planned implementation was also presented.

Acknowledgement. The current research was partially supported by the Knowledge Base Research Grant from the Research Excellence Fund of Texas A&M University.

## References

[1] Barr, A. and E.A. Feigenbaum, The Handbook of Artificial Intelligence, Vol. 1, William Kaufmann Inc., Los altos, 1982.

[2] Bic, L. and J.P. Gilbert, "Learning form AI: new trends in database technology," Computer, March 1986, pp. 44–54.

[3] Bonczek, R.H., C.W. Holsapple and A.W. Whinston, Foundations of Decision Support Systems, Academic Press, New York NY, 1981.

[4] Brachman, R.J. and H.J. Levesque, "What makes a knowledge base knowledgeable? A view of databases from the knowledge level," Expert Database Systems, The Benjamin/Cummings Publishing Co. Inc., Reading, Massachusetts, 1986.

[5] Brodie, M.L., J. Mylopoulos and J.W. Schmidt (eds.), On Conceptual Modelling, Springer-Verlag, New York, 1984.

[6] Chang, C.L., "DEDUCE2: Further investigations of deductions in relational databases," Logic and Databases (edited by H. Gallaire and J. Minker), Plenum Press, New York, 1978.

[7] Chen, P.P., “The entity-relationship model: A basis for the enterprise data definition,” ACM Trans. on Database Systems, 1, 1976, pp. 9–36.

[8] Choobineh, J., M. Mannino, J. Nunamaker and B. Konsynski, "Expert database design system based on analysis of forms," IEEE Trans. on Software Engineering, 14, 2, February 1988, pp. 242-253.

[9] Choobineh, J. and A. Sen, "A framework for deductive database design in decision support systems," Proc. of International Conference on Information Systems, pp. 241-251, 1987.

[10] Codd, E.F., "A relational model of data for large shared data banks," Communications of ACM, 13, 1970, pp. 377–387.

[11] Codd, E.F., "Seven steps to randevous with the casual user," Data Base Management (edited by J.W. Klimbie and K.L. Koffman), North Holland, 1974.

[12] Codd, E.F., "Extending the database relational model to

capture more meaning," ACM Trans. on Database Systems, 4, 1979, pp. 397–434.

[13] Cohen, P.R. and E.A. Feigenbaum, The Handbook of Artificial Intelligence, Vol-3, William Kaufmann Inc., Los Altos, California, 1982.

[14] Dayal, U. and J.M. Smith, "PROBE: A knowledge-oriented database management system," in On Knowledge Base Management Systems (M.L. Brodie and J. Mylopoulos, editors), Springer-Verlag, New York, 1986, pp. 227–257.

[15] De, P., A. Sen and E. Gudes, “A new model for data base abstraction,” Information Systems, 2, 1, 1982, pp. 1–12.

[16] Donovan, J.J., "Data base systems approach to management decision support," ACM Trans. Database Systems, 1, 1976, pp. 344-369.

[17] Elam, J.J., "Model management system: A framework for development," Tech Report #79-02-04, Department of Decision Sciences, The Wharton School, Univ. of Penn, USA, February 1979.

[18] Forgy, C. and J. McDermott, "OPS: A domain-independent production system language," Proc. Intl. Jt. Conf. on Artificial Intelligence, 5, 1977, pp. 933-939.

[19] Fox, M.S., Constraint-directed Search: A Case Study of Job-Shop Scheduling, Tech Report CMU-RI-83-22, 1983.

[20] Gallaire, H., J. Minker and J.M. Nicolas, "Logic and Databases: a deductive approach," Computing Surveys, 16, 2, June 1984, pp. 153–185.

[21] Glass, A.L. and K.J. Holyoak, Cognition, Random House, New York, 1986.

[22] Hammer, M. and D. McLeod, "The semantic data model: a modeling mechanism for database applications," Proc. ACM SIGMOD International Conference on Management of Data, Austin, Texas, pp. 25–47.

[23] Jarke, M. and J. Koch, "Query optimization in database systems," Computing Surveys, 16, 2, June 1984, pp. 111-152.

[24] Kellogg, C., “The transition from data management to knowledge management,” Proc. Intl. Conf. on Data Engg., Los Angeles, April 24–27 1984, pp. 467–472.

[25] Kellogg, C., "From data management to knowledge management", Computer, January 1986, pp. 75–84.

[26] Kerschberg, L. (ed.), Expert Database Systems, The Benjamin/Cummings Publishing Co. Inc., Reading, Massachusetts, 1986.

[27] Kerschberg, L. (ed.), Proc. of First Intl. Conf. on Expert Database Systems, 1986.

[28] Konsynski, B.R., "On the structure of a generalized model management system," Proc. Fourteenth Annual Hawaii Conference on Systems Sciences, 1980, pp. 630–638.

[29] Lee, R., "Database inferencing for decision support," DSS, 19085, pp. 57–68.

[30] Levesque, H., "The logic of incomplete knowledge bases," in On Conceptual Modelling (edited by M.L. Brodie, J.Mylopoulos and J.W. Schmidt), Springer-Verlag, New York, 1984, pp. 165–186.

[31] Lafue, G.M.E. and R.G. Smith, "Implementation of a semantic integrity manager with a knowledge representation system," in Expert Database Systems (edited by L. Kerscheberg), The Benjamin/Cummings Publishing Co. Inc., Reading, Massachusetts, 1986, pp. 333-350.

[32] Missikoff, M. and G. Widerhold, "Towards a unified

approach for expert and database systems", First Intl. Workshop on Expert Database Systems, 1984.

[33] Naqvi, S., “Negation in knowledge base management systems,” in On Knowledge Base Management Systems (M.L. Brodie and J. Mylopoulos, editors), Springer-Verlag, New York, 1986, pp. 125–146.

[34] Navathe, S.B. and M. Scholnick, “View representation in logical data base design,” Proc. ACM-SIGMOD, 1978, pp. 144–156.

[35] Negoita, C.V., Expert Systems and Fuzzy Systems, Benjamin/Cummings Publishing Company, Inc., Reading, Massachusetts, 1985.

[36] Reiter, R., “Towards a logical reconstruction of relational database theory,” in On Conceptual Modelling (edited by M.L. Brodie et al.), Spring-Verlag, New York, 1984.

[37] Sen, A. and G. Biswas, "Decision support systems: an expert systems approach," DSS, 1, 1985, pp. 197-204.

[38] Sen, A. and L. Kerschberg, “Enterprise modeling for database specification and design,” Data and Knowledge Engineering, 2, 1987, pp. 31–58.

[39] Shafer, G., A Mathematical Theory of Evidence, Princeton University Press, NJ, 1976.

[40] Shipman, D.W., "The functional data model and the data language DAPLEX," ACM Trans. on Database Systems, 1, 1981, pp. 140–173.

[41] Smith, J.M. and D.C.P. Smith, "Database abstractions: aggregation and generalization," ACM Trans. on Database Systems, 2, 1977, pp. 105-133.

[42] Tsichritzis, D.C. and F.H. Lochovsky, Data Models, Prentice-Hall Inc., Englewood Cliffs, New Jersey, 1982.

[43] Vassiliou, Y., J. Clifford and M. Jarke, “Access to specific declarative knowledge by expert systems: The impact of logic programming,” DSS, 1, 1985, pp. 123–141.

[44] Widerhold, G., "Knowledge and database management," IEEE Software, January 1984, pp. 63–73.

[45] Zaniolo, C., “Incomplete database information and null values: an overview,” Proc. of the Advanced Seminar on Theoretical Issues in Data Bases, Cetraro, Italy, Sept. 1981.

[46] Zaniolo, C., “The representation and deductive retrieval of complex objects,” MCC Report & mcc/db/kbs/77/Rev.1/850506, Austin, Texas, 1985.
