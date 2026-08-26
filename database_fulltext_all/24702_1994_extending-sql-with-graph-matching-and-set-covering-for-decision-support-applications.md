---
otero_id: 24702
otero_key: "QQAC6WQT"
title: "Extending SQL with Graph Matching and Set Covering for Decision Support Applications"
authors: "Jorng-Tzong Horng; Gwo-Dong Chen; Baw-Jhiune Liu"
year: "1994"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1994.11518032"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Extending SQL with Graph Matching and Set Covering for Decision Support Applications

Jorng-Tzong Horng, Gwo-Dong Chen & Baw-Jhiune Liu

To cite this article: Jorng-Tzong Horng, Gwo-Dong Chen & Baw-Jhiune Liu (1994) Extending SQL with Graph Matching and Set Covering for Decision Support Applications, Journal of Management Information Systems, 11:1, 101-129, DOI: 10.1080/07421222.1994.11518032

To link to this article: https://doi.org/10.1080/07421222.1994.11518032

![](/api/attachments/QQAC6WQT/fulltext/images/c5490cce3f133c9436454ef784c5002d88740729086b3f5c40ca7b3b0c80fb64.jpg)

Published online: 14 Dec 2015.

![](/api/attachments/QQAC6WQT/fulltext/images/678e638e42370f3dd1e1fd14970f97d8632d0e6fd18caab18f753e27f87e95b8.jpg)

Submit your article to this journal ↗

![](/api/attachments/QQAC6WQT/fulltext/images/417f08f63c8c492628af39079bc9e1844068f3a175d51b22b6b584dc903f5890.jpg)

View related articles ↗

![](/api/attachments/QQAC6WQT/fulltext/images/d13790ddf6648c42f1dacd584d42bff0bf67fa1d3bee9d74b75f7ffb19d38d9b.jpg)

Citing articles: 1 View citing articles ↗

# Extending SQL with Graph Matching and Set Covering for Decision Support Applications

JORNG-TZONG HORNG, GWO-DONG CHEN, AND BAW-JHIUNE LIU

JORNG-TZONG HORNG is Associate Professor of Computer Science and Information Engineering at the National Central University, Chungli, Taiwan. He received his Ph.D. in computer science from National Taiwan University. His major research focus is on database systems, object-oriented databases, and combinatorial optimization.

GWO-DONG CHEN is Associate Professor of Computer Science and Information Engineering at the National Central University, Chungli, Taiwan. He received his Ph.D. in electrical engineering from National Taiwan University. His major research focus is on object-oriented databases, multimedia, and intelligent computer-assisted learning systems.

BAW-JHIUNE LIU is Professor of Computer Science and Information Engineering at the National Central University, Chungli, Taiwan. He received his Ph.D. in electrical engineering from National Taiwan University. His major research focus is on database systems, object-oriented databases, and hypertext.

ABSTRACT: Graph matching, set covering, and partitioning problems are both theoretically and practically important in decision support systems. Numerous decision support applications have been modeled as graph matching, set covering, and partitioning problems. These include applications in the areas of task assignment, marriage problem, airline crew scheduling, truck deliveries or vehicle routing, political redistricting, and the like. Currently, these applications are supported through programs written in external (to the database system) programming languages that use only the data in the database system. Thus, decision makers or application programmers require extra effort to get required decision support information. As opposed to database systems, the purpose of a model management system (MMS) is to make a wide variety of models available to decision makers so they can apply these models without having to become involved in technical and/or procedural aspects of implementation. The goal of this research is to integrate database systems and model systems for zero-one integer programming problems especially concerning graph matching, set covering, and partitioning problems. Users utilize a single integrated language for both problem

Acknowledgments: A grant from the National Science Council, NSC820408E008007, partially supported this research. We are grateful to Te-Son Kuo and Tak-Wai Chan for their contributions to this research. We would also like to thank our referees for their helpful comments and suggestions.

formulation and model execution. In order to achieve this goal, we extend relational operators and the query language SQL. The relational operators are extended with six operators, namely, match, maxmatch, cover, mincover, partition, and minpartition. Some of these operators may take a very long time to find an optimal solution. In this article, we adopted genetic algorithms to find a near-optimal solution of this kind of operators. We found they performed well both on the computational effort and on the quality of the solutions through a variety of test problems. These algorithms are bounded by a polynomial time. Therefore, they enable a DBMS to respond to queries involving proposed operators in a restricted amount of time.

KEY WORDS AND PHRASES: decision support systems, genetic algorithms, integer programming, model management systems, relational database, SQL.

## 1. Introduction

THE RELATIONAL MODEL IS THE MOST POPULAR DATA MODEL used in database management systems. Most of the database management systems now being introduced as products are based on relational models. Relational database languages, due to their flexibility, power, and simplicity, are playing an increasingly important role in the development of information systems. SQL [7, 8, 9, 29] is the best known of these and has become the ANSI standard for relational DBMS (ANSI X3.135–1986; also ISO/TC 97/SC21/WG3N143). It has been implemented by many manufacturers such as QINT/SQL, ORACLE, UNIFY, INGRES/SQL, SYBASE, and so on [29]. It allows one to ask ad hoc queries, relieving decision makers and their assistants of the need to write programs in procedural languages. By using SQL, application programmers or users need only specify what they want without regarding how the results are retrieved. Application development time is thus greatly reduced.

SQL, however, is not adequate for certain important application domains such as decision support systems. For example, let us explore a relation that records baseball players, positions played, and fielding averages for the positions played. In this example, we assume each player can play some subset of the positions and each position can be played by some subset of the players. In addition, each player has fielding averages for the positions played. A team coach might want to know how to assign a team of nine players with a maximum total fielding average for a game. In this team, each player plays only one position and each position is played by only one player. This question cannot be directly answered with SQL. However, this kind of query frequently appears in decision support environments. Four more typical examples are illustrated in the following paragraphs.

1. Suppose suppliers and parts are stored in the SP(s#, p#) relation. The relationship between them indicates that a supplier can supply some subset of the kinds of parts and each kind of part can be supplied by some subset of the suppliers. We might want to find the largest number of parts that can be supplied, with the restrictions that one supplier supplies only one kind of part and one kind of part is supplied by only one supplier.

2. Using the SP relation in (1), we could then consider such problems as determining the set of suppliers with minimum total cost who can supply all kinds of parts. In this example, we assume a cost is associated with a supplier for some subset of the parts he or she supplies. Moreover, we not only require the set of suppliers with minimum total cost who can supply all kinds of parts, but we also require that no two of them supply the same kind of part.

3. Assume that suppliers, parts, and quantities are stored in the SPQ(s#, p#, qty) relation. The relationship among them is that the specified suppliers (s#) supply the specified parts (p#) in the specified quantities (qty). Now we want to find a set of (s#, p#) pairs in which each supplier exactly supplies one kind of part, and each kind of part is exactly supplied by one supplier. In addition, the sum of the quantity of all kinds of parts that have been supplied is maximum.

4. A manager might want to find a minimal cost project team that represents all the skills necessary for a certain job from a collection of employees, each with a different set of skills and labor cost.

In investigations from the above examples we found these situations can be modeled as (weighted) bipartite graph matching, set covering, and partitioning problems. Graph matching, set covering, and partitioning problems are both theoretically and practically important in decision support systems. Numerous situations have been modeled as graph matching, set covering, and partitioning problems $[17, 33, 35, 45]$ . These include applications in the areas of assignment problem, airline crew scheduling, truck deliveries or vehicle routing, political redistricting, and the like. Basically, there are three approaches to directly acquiring the results of these problems from a system: (1) add greater modeling capabilities to the database systems, (2) add greater data management capabilities to the model systems, or (3) provide a better interface between the database system and modeling system.

Currently, relational database systems support these applications merely by providing some programming languages that are used to write the programs associated to the data. Thus, decision makers or application programmers require extra efforts to get required decision support information.

The purpose of a model management system (MMS) is to make a wide variety of models (e.g., linear programming, forecasting, regression, simulation) available to decision makers so they can apply these models without having to become involved in technical and/or procedural aspects of implementation [24, 25]. The MMS serves as a bridge between the decision maker's problem environment and the appropriate models and data residing in the system.

The goal of this research is to integrate database systems and model systems for zero-one integer programming problems, especially concerning graph matching, set covering, and partitioning problems. Users utilize a single integrated language for both problem formulation and model extraction. As far as the users are concerned, data extraction and execution of mathematical models are all performed in one step. In this case, certain decision support capabilities are supported directly by the database systems, leading to benefits of improved data independence, increased productivity, and better performance.

The approach presented here deals with a special class of queries that involves the properties of graph matching, set covering, and partitioning problems. Rather than define a new language, we identify primitive operators for these important applications and extend the necessary features to the SQL database language. We propose six operators—namely, match, maxmatch, cover, mincover, partition, and minpartition. We incorporate these new operators into the “WHERE” clause of SQL statements. Therefore, users with knowledge of SQL can easily take advantage of the increased decision support capabilities without learning a new language.

Model storage is implemented using subroutine libraries of algorithmic solution procedures. Algorithmic solution procedures for graph matching are well developed in graph theory $[4, 33, 35]$ and integer programming $[17]$ , and those for set covering and partitioning problems are also developed in the work $[2, 17, 22, 31, 45]$ . Some of the proposed operators are used to find optimal solutions. It may take a very long time to find these optimal solutions so genetic algorithms $[22, 31]$ are used to find near-optimal solutions. We found that our genetic algorithm approach for extended operations and query optimization performed well on both the computational effort and the quality of the solutions through a variety of test problems. This approach makes it possible for a DBMS to respond to queries involving the proposed operators in a predicate restricted amount of time.

This article is organized as follows. Some related research is reviewed in section 2. In section 3 we define the terminology, including graph matching, set covering, and partitioning problems, which are key concepts here. In section 4 the extended SQL operators are defined. First, the semantics and syntax of the extended operators are described. We then give a number of motivating examples. In section 5, we discuss algorithms used by access routines to implement the proposed operators. Section 6 presents some conclusions.

## 2. Literature Survey

IN THIS SECTION WE REVIEW PREVIOUS RESEARCH ON SQL EXTENSIONS and relevant work on model management systems.

## 2.1. Extended Database Query Languages

To extend the benefits of the database approach to other areas, in recent years there has been an emphasis on extending the power and features of database query languages. Many researchers have designed extensions to existing database languages which are better suited for the new application areas. Examples of existing extended languages are enumerated as follows: QUEL\* [46] and POSTQUEL [43] are extensions of QUEL. STBE [37, 38] is an extension of QBE. SQL/NF [42] and SQL for NF $^{2}$ relations [32, 39, 40] are extensions of SQL. Mannino and Shapiro [34] extended query languages to support graph traversal problems. Eder [12] extended SQL to support general transitive closure. OSQL [14] extended SQL to support object-oriented queries. Dattero et al. [10] implemented the SQL database language for support of decision support capabilities. SQLMP [6] extended SQL to represent and formulate linear mathematical models. From these extensions we can distinguish three types of extension to SQL: (1) add greater data structure capabilities, (2) add greater control structure capabilities, and (3) add greater modeling capabilities.

SQL/NF [42] and SQL for NF $^{2}$ relations, HDBL [32, 39, 40], are extensions of SQL. All these query languages extend the nested relational model by encompassing such extensions as duplicates, ordering, functions, and recursive queries. Eder [12] proposed an extension of the database language SQL for the processing of recursive structures. This extension defined new constructs that are integrated in the view definition mechanism of SQL. Object SQL interface [14] extends SQL to accommodate the object model and a more functional style and is used as a query language. As SQL, OSQL serves as a data description, data manipulation, and query language. This type of extension is to enhance data structure capability of nested relation, recursive structure, and object-oriented structure.

A new database construct—Derived Relations with Exception (DRE) [10]—was developed that extends the decision support capabilities of relational database systems. DREs are a superset of relational views that provide greater decision support capabilities in that they handle exceptions to general rules and can operate in a hypothetical mode that provides an easier way to experiment with alternative scenarios in a what-if fashion [41]. DREs were implemented by extending the SQL database language. This type of extension extends the control structure capabilities of relational database systems.

A new language, SQLMP (SQL for mathematical programming), is introduced by Choobineh [6] for model description and manipulation. SQLMP is the result of endowing SQL with additional constructs for the definition of the objective functions and the constraints of optimization models. Basically, four stages can be identified in applying mathematical programming to business problems [6]. The first stage is to formulate the model scheme. This stage is followed by instantiation of the model with data. The next stage is solving the model instance and obtaining an optimal solution. The last stage is postsolution analysis. This type of extension is used for managing these stages. The extension is aimed at overcoming the development of large, complex, linear programming problems using databases. In other words, the purpose of this type of extension is to add greater modeling capabilities to the database systems for model definition and manipulation.

In contrast to Choobineh's SQLMP, our extended SQL is similar to SQLMP. SQLMP distinguishes between an algebraic model scheme and its data. A model's scheme is independent of its data; the same scheme can be instantiated with different data. However, our extension to SQL does not distinguish a model scheme and its data. The data needed in solving graph matching, set covering, and partitioning problems are stored in databases directly. Thus, when these problems are executed, the data are extracted from databases without being instantiated with their model. SQLMP is an SQL-based language for the development of large, complex, linear programming problems while our extension to SQL is to enhance decision support capabilities of database systems. The extension belongs to adding greater modeling capabilities to the database systems for certain decision support capabilities. Our extended SQL is introduced for zero-one integer programming problem formulation and model execution instead of model definition and manipulation.

## 2.2. Model Management Systems

Many tools and languages have been devised for either data or mathematical model description and manipulation. Examples of the languages and tools for mathematical modeling include $[6, 15, 36]$ . Two types of integration of data and mathematical models are possible $[6]$ . In loose integration, a query language is used to retrieve data that will be used as input to a mathematical optimizer. Data will then be stored in an extraction file, possibly reformatted to satisfy the particular requirements of the solver being used, and then fed to the solver. The output from the solver is sent back to the database for utilization and permanent storage. An example of this approach was adopted in the GMIS project $[11]$ . In tight integration, data management and mathematical optimization/analysis are integrated into one system. Users utilize a single integrated language for both data management and mathematical analysis. Examples of this approach were adopted in $[6]$ and $[30]$ .

Model management systems have been proposed to provide generalized support for organizational decision making $[1, 5, 13]$ and to provide centralized management of organizational models $[3, 24, 25, 26, 27, 28]$ . Two classes of MMS have been identified to meet these two objectives $[1]$ . These are: (1) decision processing MMS, and (2) model processing MMS.

Decision processing MMS $[1, 5, 13]$ are MMS that serve the primary function of organizational decision support $[1]$ . These systems function to provide a flexible, modeling component for a decision support system. Applegate, Konsynski, and Nunamaker $[1]$ described the use of a framework to design an MMS for support of planning decisions within an organization. Geoffrion $[18, 19]$ introduced structured modeling, which aims to provide a formal mathematical framework and computer-based environment for conceiving, representing, and manipulating a wide variety of models.

Model processing MMS [3, 24, 25, 27, 28] are MMS that serve the primary function of the management and control of organizational models in a centralized model base. These systems function to ensure the integrity, consistency, currency, and security of an organizational model base in a manner to a centralized DBMS.

Many optimization techniques $[2, 4, 17, 22, 31, 33, 35, 45, 47]$ have been applied successfully to implement our proposed operators. To implement an operator, the database must choose an appropriate model. We incorporate some capabilities of an MMS such as model storage and extraction in the query optimization phase. Therefore, users can easily get required decision support information from databases. Proposed operator and model availability expands the domain of decision support applications that a database system can support.

## 3. Terminology

IN THIS SECTION, WE REVIEW THE DEFINITION OF GRAPH MATCHING, set covering, and partitioning problems. For a more detailed description, see [4, 17, 33, 35, 45].

Definition 1: A graph $G = (V, E)$ is called bipartite if there exist sets $V_{1}$ and $V_{2}$ such that

$$
V _ {1} \cup V _ {2} = V, V _ {1} \cap V _ {2} = \varnothing
$$

and every edge of $G$ is incident to one vertex of $V_{1}$ and one vertex of $V_{2}$ .

For example, a bipartite graph is shown in figure 1a.

Definition 2. A matching M on a bipartite graph $G(V_{1}, V_{2}, E)$ is a set of edges of $E(G)$ , no two of which have the same end. M is a maximum matching if G has no matching $M'$ with $|M'| > |M|$ .

For example, a maximum matching that is obtained from figure 1a is indicated in figure 1b.

Definition 3. A matching M on attributes X and Y in relation R is a set of tuples over X and Y, no two of which have the same instance of X or Y. M is a maximum matching if R has no matching $M'$ with

$$
\begin{array}{c c c c c} \text { SELECT } & \text { COUNT(*) } & > & \text { SELECT } & \text { COUNT(*) } \\ \text { FROM } & M & & \text { FROM } & M \end{array}
$$

For example, a relation and two maximum matchings that are obtained from the relation are depicted in figure 2a and 2b, respectively.

Definition 4. A set $I = \{1, \ldots, m\}$ , and a set $P = \{P_1, \ldots, P_n\}$ , where $P_j \subseteq I, j \in J = \{1, \ldots, n\}$ . A subset $J^* \subseteq J$ defines a cover of $I$ if

$$
\bigcup_ {j \in j ^ {*}} P _ {j} = I.
$$

If, in addition,

$$
j, k \in J ^ {*}, j \neq k \Rightarrow P _ {j} \cap P _ {k} = \emptyset .
$$

$J^{*}$ defines a partition of $I$ . In other words, a cover $J^{*}$ of $I$ is described as a partition of $I$ if it has the additional property that all distinct pairs of elements of $J^{*}$ are disjoint. For example, consider the set covering and partitioning problems having $I = \{1, 2, 3, 4\}$ , and $P_{1} = \{1, 3, 4\}, P_{2} = \{2\}, P_{3} = \{3, 4\}, P_{4} = \{1, 2\}$ . The set $\{P_{1}, P_{2}\}$ is a cover as well as a partition of $I$ . Similarly, the set $\{P_{3}, P_{4}\}$ is also a cover as well as a partition of $I$ while the set $\{P_{1}, P_{4}\}$ is a cover of $I$ but it is not a partition of $I$ .

Definition 5. Let a cost $c_{j} > 0$ be associated with every $j \in J$ . The total cost of the cover $J^{*}$ is Q. Let $A$ be an $m \times n$ binary matrix, $c$ an $n$ -dimensional nonnegative vector, and $x$ an $n$ -dimensional binary vector, with $cx$ the inner product of the two, and $l$ an $m$ -dimensional column vector of ones. The set covering problem [17] is to find a cover of minimum cost and can be written as the zero-one integer programming

(1)

$$
\text { minimize   (over } x) c x\tag{2}
$$

$$
\text { subject   to } A x \geq 1\tag{3}
$$

$$
x _ {j} = 0, 1, j = 1, \dots , n
$$

![](/api/attachments/QQAC6WQT/fulltext/images/732538bb30a6f8f1ee0b8029a7a5a6b51275db4d2a138a75e879c40d95686f2d.jpg)  
1a. A Bipartite Graph

![](/api/attachments/QQAC6WQT/fulltext/images/3b2b7da7744fdbbe81f95925266c53270359dfc20bafc8401376b0aa0c36ffde.jpg)  
1b. A Maximum Matching  
Figure 1. A Bipartite Graph and a Maximum Matching

R

<table><tr><td>s#</td><td>p#</td></tr><tr><td>s1</td><td>p1</td></tr><tr><td>s1</td><td>p2</td></tr><tr><td>s1</td><td>p3</td></tr><tr><td>s2</td><td>p4</td></tr><tr><td>s3</td><td>p2</td></tr><tr><td>s3</td><td>p4</td></tr><tr><td>s4</td><td>p1</td></tr><tr><td>s4</td><td>p2</td></tr></table>

<table><tr><td>s#</td><td>p#</td></tr><tr><td>s1</td><td>p3</td></tr><tr><td>s2</td><td>p4</td></tr><tr><td>s3</td><td>p2</td></tr><tr><td>s4</td><td>p1</td></tr></table>

2b. A Maximum Matching of R  
2a. Relation R  
Figure 2. A Relation and its Maximum Matching

where

$$
x _ {j} = \left\{ \begin{array}{l l} 1 & \text { if   } j \text {   is   in   the   cover } \\ 0 & \text { otherwise } \end{array} \right.
$$

$$
a _ {i j} = \left\{ \begin{array}{l l} 1 & \text {   if   } i \in P _ {j} \\ 0 & \text {   otherwise   }. \end{array} \right.
$$

Similarly, the set partitioning problem is obtained by replacing (2) with

$$
\text { subject   to } A x = 1.\tag{2a}
$$

Any $x$ satisfying (2) and (3) (or 2a and 3) is called a cover (partition) solution. As an example, consider the set covering problem having $I = \{1, 2, 3, 4\}$ , and $P_1 = \{1, 3, 4\}, P_2 = \{2\}, P_3 = \{3, 4\}, P_4 = \{1, 2\}$ . The set covering problem can be formulated as the following zero-one integer programming if the costs are (2, 3, 6, 1).

$$
\begin{array}{c} \text {[ 2 3 6 1 ]} \\ \left[ \begin{array}{l} 1 0 0 1 \\ 0 1 0 1 \\ 1 0 1 0 \\ 1 0 1 0 \end{array} \right] \times \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right] \geq \left[ \begin{array}{l} 1 \\ 1 \\ 1 \\ 1 \end{array} \right]. \end{array}
$$

In this example, the optimal cover solution of the set I is $x = (1, 0, 0, 1)$ and the cost is 3. Using the same data, the optimal partition solution is $x = (1, 1, 0, 0)$ and the cost is 5.

## 4. Operators for Graph Matching, Set Covering, and Partitioning Problems

IN THIS SECTION WE DESCRIBE THE FORMULATION of graph matching, set covering, and partitioning problems in SQL. We define special operators for the “WHERE” clause of SQL expressions to give a shorthand notation of such problems. Six constructs—match, maxmatch, cover, mincover, partition, and minpartition—were defined. The semantics and syntax of the extended operators are described first. A number of motivating examples is then given.

## 4.1. Definition of the Extended Operators in SQL

A query language can be extended to support graph matching, set covering, and partitioning problems by utilizing two approaches $[34]$ . One method of extension is to add some form of iteration or recursion. In procedural query languages, graph matching, set covering, and partitioning problems can be solved through iteration or recursion. Another method is to add one or more special operators, each of which solves a class of problems without specifying a procedure. Language extensions using this approach instead of explicit iteration or recursion are likely to be nonprocedural because iteration or recursion cannot be encoded. Since SQL is a nonprocedural language, we extend SQL to support graph matching, set covering, and partitioning problems by adding special operators, each of which solves a class of problems. In this section we identify primitive operators for the applications of these problems and also extend the necessary features to the SQL database language. We propose six operators: match, maxmatch, cover, mincover, partition, and minpartition. We incorporate these new operators directly into the “WHERE” clause of SQL statements.

## 4.1.1. The Match Operation

If we want to restrict objects with a many-many relationship in a pair of attributes to a one-one relationship, we cannot formulate this kind of query by using SQL statements directly. For example, in a certain company, $n$ workers $W_{1}, W_{2}, \ldots, W_{n}$ are available for $n$ jobs $J_{1}, J_{2}, \ldots, J_{n}$ , each worker being qualified for one or more of these jobs. Can all the men be assigned, one man per job, to jobs for which they are qualified? This is the assignment problem. For convenience, we introduce a special construct for such selection. The construct can be used in the “WHERE” clause of SQL statements. The syntax of the construct is defined as follows:

SELECT attribute-list

FROM relation-name

WHERE MATCH((X, Y)).

Where X and Y are two attributes of the given relation relation-name.

The match operation of relation R on attributes X and Y,

R WHERE MATCH((X, Y)),

is a relation with the same heading as R and with a body consisting of the set of all tuples t of R such that the maximum matching “t.X and t.Y” is satisfied. The operator effectively yields a horizontal subset of a given relation, that is, that subset of the tuples of the given relation for which a maximum matching is satisfied. For example, the following SP relation gives a shipment of parts of kind p# by the supplier s# and the shipment quantity is qty. Now we might want to find the largest number of kinds of parts that can be supplied with the restrictions that one supplier only supplies one kind of part and one kind of part is only supplied by one supplier.

Example of MATCH((s#, p#)

<table><tr><td colspan="3">SP(s# p# qty)</td><td colspan="3">match((s#, p#)) (s# p# qty)</td></tr><tr><td>s1</td><td>p1</td><td>2</td><td>s1</td><td>p3</td><td>2</td></tr><tr><td>s1</td><td>p2</td><td>1</td><td>s2</td><td>p4</td><td>3</td></tr><tr><td>s1</td><td>p3</td><td>2</td><td>s3</td><td>p5</td><td>2</td></tr><tr><td>s2</td><td>p4</td><td>3</td><td>s4</td><td>p2</td><td>3</td></tr><tr><td>s3</td><td>p2</td><td>4</td><td>s5</td><td>p1</td><td>2</td></tr><tr><td>s3</td><td>p4</td><td>4</td><td>s6</td><td>p7</td><td>3</td></tr><tr><td>s3</td><td>p5</td><td>2</td><td>s7</td><td>p8</td><td>4</td></tr><tr><td>s4</td><td>p2</td><td>3</td><td>s8</td><td>p6</td><td>2</td></tr><tr><td>s4</td><td>p6</td><td>1</td><td></td><td></td><td></td></tr><tr><td>s5</td><td>p1</td><td>2</td><td></td><td></td><td></td></tr><tr><td>s5</td><td>p7</td><td>5</td><td></td><td></td><td></td></tr><tr><td>s6</td><td>p7</td><td>3</td><td></td><td></td><td></td></tr><tr><td>s7</td><td>p8</td><td>4</td><td></td><td></td><td></td></tr><tr><td>s8</td><td>p6</td><td>2</td><td></td><td></td><td></td></tr></table>

It has to be noted that the result of an extended operation may have multiple solutions. The system can display a certain set of solutions (for example, five or ten) in a time constraint or can display all solutions. The latter case may need a very long time to evaluate the following sequential operations and then display all solutions when the extended operators are integrated with other operators of relational algebra. This is because the result of an extended operation is a set of subsets of all tuples of the given relation. In this example, only one maximum matching is found.

We use entity-relationship diagrams to illustrate the semantics of the construct. The ER diagrams are shown in figure 3.

![](/api/attachments/QQAC6WQT/fulltext/images/494d01d42845c97641ee4a0501582ad9b7d6afd3ad159026632bc0b1b3abc46e.jpg)  
Figure 3. The ER Diagrams for Match Operation

## 4.1.2. The Maxmatch Operation

The match operator is an efficient way of determining a maximum matching, if one exists, between a pair of attributes. However, one may, in addition, wish to take into account the effectiveness of the various relationships between a pair of attributes. As an example, consider the assignment problem again. One may take into account the effectiveness of the workers in their various jobs (measured, perhaps, by the profit to the company). In this case, one is interested in an assignment that maximizes the total effectiveness of the workers. The problem can be solved by using the maxmatch operator in SQL. The syntax of the construct is defined as follows:

SELECT attribute-list

FROM relation-name

WHERE MAXMATCH((X, Y), Z).

In the given relation relation-name, attributes X and Y uniquely identify attribute Z. The maxmatch operation of relation R on attributes X, Y, and Z,

## R WHERE MAXMATCH((X, Y), Z),

is the set of all tuples t of R such that the matching “t.X and t.Y” is satisfied and the sum of the corresponding t.Z is maximum.

As an example, a suppliers–parts relation SP is shown in figure 4a. Now we want to find a set of pairs (s#, p#) in which each supplier exactly supplies one kind of part, and one kind of part is exactly supplied by one supplier. Furthermore, the sum of the quantity of all kinds of parts that have been supplied is maximum. One maximum weighted matching is shown in figure 4b.

In this maximum weighted matching, each supplier exactly supplies one kind of part and each kind of part is exactly supplied by one supplier. The sum of the qty in the matching is 1,400.

<table><tr><td colspan="6">A. Relation SP</td><td colspan="6">B. One result after applying the MAXMATCH</td></tr><tr><td>SP</td><td>(s#</td><td>p#</td><td>qty</td><td>j#</td><td>e#)</td><td>MAXMATCH ((s#, p#), qty)</td><td>(s#</td><td>p#</td><td>qty</td><td>j#</td><td>e#)</td></tr><tr><td></td><td>s1</td><td>p1</td><td>300</td><td>j1</td><td>e1</td><td></td><td>s1</td><td>p4</td><td>400</td><td>j3</td><td>e2</td></tr><tr><td></td><td>s1</td><td>p2</td><td>500</td><td>j2</td><td>e2</td><td></td><td>s2</td><td>p1</td><td>200</td><td>j4</td><td>e4</td></tr><tr><td></td><td>s1</td><td>p3</td><td>500</td><td>j1</td><td>e3</td><td></td><td>s3</td><td>p3</td><td>400</td><td>j2</td><td>e1</td></tr><tr><td></td><td>s1</td><td>p4</td><td>400</td><td>j3</td><td>e2</td><td></td><td>s4</td><td>p2</td><td>100</td><td>j4</td><td>e3</td></tr><tr><td></td><td>s1</td><td>p5</td><td>100</td><td>j2</td><td>e1</td><td></td><td>s5</td><td>p5</td><td>300</td><td>j4</td><td>e2</td></tr><tr><td></td><td>s2</td><td>p1</td><td>200</td><td>j4</td><td>e4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s2</td><td>p2</td><td>300</td><td>j3</td><td>e1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s2</td><td>p4</td><td>200</td><td>j2</td><td>e2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s2</td><td>p5</td><td>200</td><td>j1</td><td>e3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s3</td><td>p1</td><td>200</td><td>j4</td><td>e1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s3</td><td>p2</td><td>400</td><td>j3</td><td>e2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s3</td><td>p3</td><td>400</td><td>j2</td><td>e1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s3</td><td>p4</td><td>100</td><td>j1</td><td>e2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s4</td><td>p2</td><td>100</td><td>j4</td><td>e3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s4</td><td>p3</td><td>100</td><td>j2</td><td>e4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s5</td><td>p1</td><td>100</td><td>j1</td><td>e2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s5</td><td>p2</td><td>200</td><td>j3</td><td>e2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s5</td><td>p3</td><td>100</td><td>j2</td><td>e1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s5</td><td>p4</td><td>300</td><td>j1</td><td>e3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s5</td><td>p5</td><td>300</td><td>j4</td><td>e2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Figure 4. Example of MAXMATCH((X, Y), Z)

It should be noted that the solution is not unique. For example, the following is also a solution. The sum of the qty in this matching is also 1,400.

<table><tr><td>s#</td><td>p#</td><td>qty</td><td>j#</td><td>e#</td></tr><tr><td>s1</td><td>p4</td><td>400</td><td>j3</td><td>e2</td></tr><tr><td>s2</td><td>p1</td><td>200</td><td>j4</td><td>e4</td></tr><tr><td>s3</td><td>p2</td><td>400</td><td>j3</td><td>e2</td></tr><tr><td>s4</td><td>p3</td><td>100</td><td>j2</td><td>e4</td></tr><tr><td>s5</td><td>p5</td><td>300</td><td>j4</td><td>e2</td></tr></table>

We will sometimes choose to minimize rather than maximize. This causes no difficulty, since we can first add a negative sign to the values of Z and then find the maximum weighted matching. Figure 5 shows the semantics of this construct by using ER diagrams.

## 4.1.3. The Cover and Partition Operations

We sometimes want to get specific objects of an attribute in a relation that relates to the objects of an attribute in another relation; we can formulate this query in SQL by means of a special construct. The syntax of the construct is defined as follows:

![](/api/attachments/QQAC6WQT/fulltext/images/bc40759cebf5b0af6e6dbea04e7804c2ea97dab7d37657f261f0322e526186db.jpg)  
Figure 5. The ER Diagrams for Maxmatch Operation

$$
\begin{array}{l l} \text {SELECT} & \text {attribute - list} \\ \text {FROM} & R _ {1}, R _ {2} \\ \text {WHERE} & \text {COVER} ((R _ {1}. X, R _ {1}. Y _ {1}), R _ {2}. Y _ {2}). \end{array}
$$

Where attributes $Y_{1}$ in $R_{1}$ and $Y_{2}$ in $R_{2}$ are defined on the same domain. Relation $R_{1}$ describes the relationship between the instances of attributes X and $Y_{1}$ . The relationship between them is that each instance of X is related to a set of instances of $Y_{1}$ and each instance of $Y_{1}$ is also related to a set of instances of X. Each distinct instance of $Y_{1}$ in $R_{1}$ has a corresponding instance of $Y_{2}$ in $R_{2}$ . The semantics of this construct are formally defined as finding a cover of a set.

The cover operation of relation $R_{1}$ on attributes X and Y and relation $R_{2}$ on attribute Z,

$$
R _ {1}, R _ {2} \quad \text {   WHERE   COVER } ((R _ {1}. X, R _ {1}. Y), R _ {2}. Z),
$$

is a relation with the heading (X) and a body consisting of the set of the smallest number of tuples $(X:x)$ such that the set of tuples $(X:x, Y:y)$ appears in $R_{1}$ for all tuples $(Z:z)$ appearing in $R_{2}$ .

For example, a query uses an Employee Database with three relations (where underlined attributes are keys) EM(ename, skill), PROJECT(p#, skill), and SALARY(ename, salary), which are shown in figure 6. The relation EM gives employees and their skills. The relation PROJECT gives the skills that are required by a certain project. A manager now needs to assign a project team to perform the project. The project team must have all the skills needed for the project.

<table><tr><td>ename</td><td>skill</td></tr><tr><td>Johnny</td><td>Account</td></tr><tr><td>Johnny</td><td>S/W</td></tr><tr><td>Jack</td><td>Sales</td></tr><tr><td>Gary</td><td>Planning</td></tr><tr><td>Gary</td><td>Sales</td></tr><tr><td>Gary</td><td>Coordinate</td></tr><tr><td>George</td><td>Planning</td></tr><tr><td>George</td><td>H/W</td></tr><tr><td>Susan</td><td>Account</td></tr><tr><td>Susan</td><td>Secretary</td></tr><tr><td>Jane</td><td>Secretary</td></tr><tr><td>Henry</td><td>Purchase</td></tr><tr><td>Bush</td><td>H/W</td></tr></table>

Figure 6. The Employee Database with Relations EM, PROJECT, and SALARY

Example of Cover: COVER((EM.ename, EM.skill), PROJECT.skill)

ename
Johnny
Gary
George
Susan
Henry

One project team is shown above. The project team has four combinations. Each of all these four project teams is composed of five employees and has all the skills needed for the project. Any project team that is less than five employees cannot perform the project in this example.

The partition operation is similar to the cover operation. The partition operation of relation $R_{1}$ on attributes X and Y and relation $R_{2}$ on attribute Z,

$$
R _ {1}, R _ {2} \text {   WHERE   PARTITION } ((R _ {1}. X, R _ {1}. Y), R _ {2}. Z),
$$

is a relation with the heading (X) and a body consisting of the set of the smallest number of tuples $(X:x)$ such that the set of tuples $(X:x, Y:y)$ , where the set of all tuples $(Y:y)$ are different, appears in $R_{1}$ for all tuples $(Z:z)$ appearing in $R_{2}$ .

Consider the above project team example again. A manager now plans to assign a project team to perform the project. The project team not only has all the skills needed for the project but also all employees in the project team must have different skills.

Example of Partition: PARTITION((EM.ename, EM.skill), PROJECT.skill)

Only one such project team is found in this example. The five employees not only have all the skills needed for the project but also have different skills.

## 4.1.4. The Mincover, Sumcover, Minpartition, and Sumpartition Operations

The cover operator is an efficient way of determining a minimum cover (the smallest number of sets) of a set, if one exists. However, one may, in addition, wish to take into account the cost of a cover. In this case, one is interested in a cover that minimizes the total cost of the cover. The mincover operator is to find a cover of minimum cost. Finding an optimum solution of this operation is an NP-complete problem. It may take a very long time to find such solution. Hence, we provide an alternative operator for users. The alternative operator is to find feasible solutions instead of optimal solutions. The syntax of the construct is defined as follows:

$$
\begin{array}{l l} \text { SELECT } & \text { attribute - list } \\ \text { FROM } & R _ {1}, R _ {2}, R _ {3} \\ \text { WHERE } & \text { MINCOVER } ((R _ {1}. X, R _ {1}. Y), R _ {2}. Y, R _ {3}. Z), \text { or } \\ \text { SUMCOVER } ((R _ {1}. X, R _ {1}. Y), R _ {2}. Y, R _ {3}. Z) <   \text { constant   value }. \end{array}
$$

Every distinct instance of X in $R_{1}$ has a corresponding instance of Z in $R_{3}$ that is used as a cost of the instance. The semantics of the mincover operation is formally defined as finding a cover of minimum cost, and that of the sumcover operation is formally defined as finding a cover whose cost is less than the given constant value. For example, consider relations EM, PROJECT, and SALARY in figure 6 again. The relation SALARY gives the salary of each employee. Now a manager might want to know how to assign a project team with minimum salary to perform the project.

Example of Mincover: MINCOVER((EM.ename, EM.skill), PROJECT.skill, SALARY.salary)

<table><tr><td>ename</td></tr><tr><td>Johnny</td></tr><tr><td>Gary</td></tr><tr><td>Susan</td></tr><tr><td>Henry</td></tr><tr><td>Bush</td></tr></table>

The project team with minimum salary is composed of Johnny, Gary, Susan, Henry, and Bush. The total salary is 148k.

As another example, consider relations EM, PROJECT, and SALARY in figure 6 again. If we assume the project has only 150k budget, how many project teams can be considered under the budget?

Example of Sumcover: SUMCOVER((EM.ename, EM.skill), PROJECT.skill, SALARY.salary) < 150k

<table><tr><td>ename</td><td>or</td><td>ename</td></tr><tr><td>Johnny</td><td></td><td>Johnny</td></tr><tr><td>Gary</td><td></td><td>Gary</td></tr><tr><td>Susan</td><td></td><td>Jane</td></tr><tr><td>Henry</td><td></td><td>Henry</td></tr><tr><td>Bush</td><td></td><td>Bush</td></tr></table>

In this example, two project teams can be considered. Their total salaries are 148k and 149k respectively.

The minpartition and sumpartition operations are similar to the mincover and sumcover operations. As an example, using the data in the relations EM, PROJECT, and SALARY, which are shown in figure 6. The result of the following operation is shown below:

MINPARTITION((EM.ename, EM.skill), PROJECT.skill, SALARY.salary)

ename
Johnny
Gary
Jane
Henry
Bush

The project team has all the skills needed for the project and all employees in the project team have different skills. In addition, the project team minimizes salary.

## 4.2. Examples

In this section we use some examples to illustrate the operators we defined.

Example 1: Consider the COURSE relation in figure 7a. A variety of preferences and constraints are needed to be taken into consideration in assigning courses to professors. Preferences are used to deal with the conflict that arises in assigning a course to one of the several professors who can teach the course. The chairman might want to know how to assign all courses of maximum total preferences with the restrictions that one course can only be assigned to one professor and one professor can only be assigned with one course.

We can use the maxmatch operator to solve the problem. The query can be specified in SQL as follows:

SELECT    \*
FROM    COURSE
WHERE    MAXMATCH((professor, course), preference).

The result is shown in figure 7b. An optimal solution is found in this example—that is, the chairman can assign all courses of maximum total preference, one course per professor and one professor per course.

Example 2: The query uses a Baseball Database with two relations which are given in figure 8a. The relation PLAYER gives the batting average of each player. The relation BASEBALL gives each player that plays certain positions. Now the team coach wants to find a team of nine players with maximum batting average, one player per position and one position per player, for a game. The query can be answered by using the following statements of SQL:

SELECT player, position
FROM BASEBALL
WHERE MATCH((player, position))

Many matchings can be found in this example. Then, the team coach uses the ba attribute in the relation PLAYER to choose one team with maximum batting average

COURSE

<table><tr><td>professor</td><td>course</td><td>preference</td></tr><tr><td>Johnny</td><td>Computation</td><td>5</td></tr><tr><td>Johnny</td><td>Algorithm</td><td>5</td></tr><tr><td>Johnny</td><td>P. L.</td><td>3</td></tr><tr><td>Jack</td><td>Algorithm</td><td>5</td></tr><tr><td>Jack</td><td>Database</td><td>3</td></tr><tr><td>Jack</td><td>P. L.</td><td>3</td></tr><tr><td>Gary</td><td>D.S.P.</td><td>5</td></tr><tr><td>Gary</td><td>Neural</td><td>3</td></tr><tr><td>Abrham</td><td>Arch.</td><td>5</td></tr><tr><td>Abrham</td><td>Compiler</td><td>4</td></tr><tr><td>George</td><td>A.I.</td><td>4</td></tr><tr><td>George</td><td>Logic P.L.</td><td>4</td></tr><tr><td>Hwang</td><td>Network</td><td>5</td></tr><tr><td>Hwang</td><td>Algorithm</td><td>3</td></tr><tr><td>Lee</td><td>Arch.</td><td>5</td></tr><tr><td>Lee</td><td>A.I.</td><td>4</td></tr><tr><td>Hsu</td><td>A.I.</td><td>5</td></tr><tr><td>Hsu</td><td>Neural</td><td>3</td></tr><tr><td>Henry</td><td>Algorithm</td><td>5</td></tr><tr><td>Shao</td><td>Robotics</td><td>5</td></tr><tr><td>Shao</td><td>A.I.</td><td>3</td></tr><tr><td>Robinson</td><td>Arch.</td><td>5</td></tr><tr><td>David</td><td>Database</td><td>4</td></tr><tr><td>David</td><td>Logic P.L.</td><td>5</td></tr></table>

<table><tr><td>professor</td><td>course</td><td>preference</td></tr><tr><td>Johnny</td><td>Computation</td><td>5</td></tr><tr><td>Jack</td><td>P. L.</td><td>3</td></tr><tr><td>Gary</td><td>D.S.P.</td><td>5</td></tr><tr><td>Abrham</td><td>Compiler</td><td>4</td></tr><tr><td>George</td><td>Logic P.L.</td><td>4</td></tr><tr><td>Hwang</td><td>Network</td><td>5</td></tr><tr><td>Lee</td><td>A.I.</td><td>4</td></tr><tr><td>Hsu</td><td>Neural</td><td>3</td></tr><tr><td>Henry</td><td>Algorithm</td><td>5</td></tr><tr><td>Shao</td><td>Robotics</td><td>5</td></tr><tr><td>Robinson</td><td>Arch.</td><td>5</td></tr><tr><td>David</td><td>Database</td><td>4</td></tr></table>

7b. The result of Example 1  
7a. Database on COURSE

Figure 7. The COURSE Assignment Example

from the matchings. One of the matchings is shown in figure 8b.

Example 3: The query uses an Airline Database with three relations, which are depicted in figure 9. The relation CREW gives the cost of each crew for a certain flight leg. The relation AIRLINE gives each crew that flies certain flight legs. The relation FLIGHT contains the information of each flight leg. Assume crew members are allowed to be passengers on certain flights. How does the airline company schedule a set of crews that can fly all flight legs? In addition, the cost of the set of crews must be less than 135k.

The query can be specified in SQL as follows:

SELECT AL.name, AL.flight-leg, AL.descrip.

FROM CREW, AIRLINE AL, FLIGHT FT

With the result:

<table><tr><td>Name</td><td>Flight-leg</td><td>Descrip.</td></tr><tr><td>Jack</td><td>f2</td><td>d5</td></tr><tr><td>Jack</td><td>f4</td><td>d6</td></tr><tr><td>Jack</td><td>f5</td><td>d7</td></tr><tr><td>Gary</td><td>f1</td><td>d8</td></tr><tr><td>Gary</td><td>f6</td><td>d9</td></tr><tr><td>Susan</td><td>f3</td><td>d14</td></tr></table>

PLAYER

<table><tr><td>player</td><td>ba</td></tr><tr><td>Parmenter</td><td>180</td></tr><tr><td>Baker</td><td>250</td></tr><tr><td>Hope</td><td>280</td></tr><tr><td>Everett</td><td>250</td></tr><tr><td>Collins</td><td>330</td></tr><tr><td>Moorman</td><td>270</td></tr><tr><td>Wise</td><td>350</td></tr><tr><td>Brown</td><td>210</td></tr><tr><td>Bishop</td><td>280</td></tr><tr><td>Bailey</td><td>330</td></tr><tr><td>Miler</td><td>170</td></tr><tr><td>Newcatle</td><td>210</td></tr></table>

BASEBALL  
![](/api/attachments/QQAC6WQT/fulltext/images/fd7b85f8bd3b52267a0213efe957f6a63e58fcb8a3cca6b93daa6c2cb499b401.jpg)

<table><tr><td>player</td><td>position</td></tr><tr><td>Everett</td><td>Left</td></tr><tr><td>Collins</td><td>Center</td></tr><tr><td>Moorman</td><td>Right</td></tr><tr><td>Wise</td><td>Short</td></tr><tr><td>Brown</td><td>Pitcher</td></tr><tr><td>Bishop</td><td>Catcher</td></tr><tr><td>Bailey</td><td>2nd</td></tr><tr><td>Baker</td><td>1st</td></tr><tr><td>Hope</td><td>3rd</td></tr></table>

8b. One Result of Example 2  
8a. Database on PLAYER and BASEBALL Relations

## Figure 8. The Baseball Team Assignment Example

The set of crews {Jack, Gary, Susan} with minimum cost, 130k, can fly all flight legs.

Example 4: The query uses a District Database with three relations, which are depicted in figure 10. A set of counties can be formed in a district if they meet the requirements on population, contiguity, compactness, and so forth. Each district has some measure of unacceptability, which is described in the relation DISTRICT. The relationship between the districts and the counties is described in the relation DIS-COU. The relation COUNTY contains information about counties. How do we achieve the districting plan minimizing the unacceptability?

The districting plan can be achieved by the minpartition operator. The query can be specified in SQL as follows:

SELECT DIS-COU.district-name, DIS-COU.county-name

FROM DISTRICT, DIS-COU, COUNTY

WHERE minpartition((DIS-COU.dname, DIS-COU.county-name), COUNTY.county-name, DISTRICT.unacc-meas)

The result is:

CREW

<table><tr><td>c#</td><td>name</td><td>age</td><td>cost</td></tr><tr><td>c1</td><td>Johnny</td><td>32</td><td>110k</td></tr><tr><td>c2</td><td>Jack</td><td>27</td><td>60k</td></tr><tr><td>c3</td><td>Gary</td><td>34</td><td>30k</td></tr><tr><td>c4</td><td>George</td><td>33</td><td>120k</td></tr><tr><td>c5</td><td>Susan</td><td>33</td><td>40k</td></tr><tr><td>c6</td><td>Jane</td><td>25</td><td>30k</td></tr><tr><td>c7</td><td>Henry</td><td>32</td><td>80k</td></tr></table>

AIRLINE

<table><tr><td>name</td><td>flight-leg</td><td>descrip.</td></tr><tr><td>Johnny</td><td>f1</td><td>d1</td></tr><tr><td>Johnny</td><td>f3</td><td>d2</td></tr><tr><td>Johnny</td><td>f5</td><td>d3</td></tr><tr><td>Johnny</td><td>f6</td><td>d4</td></tr><tr><td>Jack</td><td>f2</td><td>d5</td></tr><tr><td>Jack</td><td>f4</td><td>d6</td></tr><tr><td>Jack</td><td>f5</td><td>d7</td></tr><tr><td>Gary</td><td>f1</td><td>d8</td></tr><tr><td>Gary</td><td>f6</td><td>d9</td></tr><tr><td>George</td><td>f2</td><td>d10</td></tr><tr><td>George</td><td>f4</td><td>d11</td></tr><tr><td>George</td><td>f5</td><td>d12</td></tr><tr><td>George</td><td>f6</td><td>d13</td></tr><tr><td>Susan</td><td>f3</td><td>d14</td></tr><tr><td>Jane</td><td>f2</td><td>d15</td></tr><tr><td>Jane</td><td>f4</td><td>d16</td></tr><tr><td>Henry</td><td>f1</td><td>d17</td></tr><tr><td>Henry</td><td>f3</td><td>d18</td></tr><tr><td>Henry</td><td>f6</td><td>d19</td></tr></table>

FLIGHT

<table><tr><td>f#</td><td>flight-name</td></tr><tr><td>f1</td><td>Tai-NY</td></tr><tr><td>f2</td><td>NY-CA</td></tr><tr><td>f3</td><td>Seoul-NY</td></tr><tr><td>f4</td><td>SA-CA</td></tr><tr><td>f5</td><td>TX-NJ</td></tr><tr><td>f6</td><td>LA-NY</td></tr></table>

Figure 9. Airline Database  
DISTRICT

<table><tr><td>d#</td><td>dname</td><td>unacc-meas</td></tr><tr><td>d1</td><td>East-1</td><td>2.0</td></tr><tr><td>d2</td><td>Taipei</td><td>3.5</td></tr><tr><td>d3</td><td>Middle-1</td><td>2.8</td></tr><tr><td>d4</td><td>Middle-2</td><td>2.7</td></tr><tr><td>d5</td><td>East-2</td><td>1.8</td></tr><tr><td>d6</td><td>East-3</td><td>1.9</td></tr><tr><td>d7</td><td>South</td><td>3.4</td></tr><tr><td>d8</td><td>Middle-3</td><td>2.6</td></tr></table>

DIS-COU

<table><tr><td>dname</td><td>county-name</td></tr><tr><td>East-1</td><td>Hwa-Lane</td></tr><tr><td>East-1</td><td>I-Lan</td></tr><tr><td>Taipei</td><td>Taipei</td></tr><tr><td>Middle-1</td><td>Taichung</td></tr><tr><td>Middle-1</td><td>Chung-Hwa</td></tr><tr><td>Middle-2</td><td>Taichung</td></tr><tr><td>Middle-2</td><td>Nan-Tou</td></tr><tr><td>East-2</td><td>Hwa-Lane</td></tr><tr><td>East-2</td><td>Tai-Dong</td></tr><tr><td>East-3</td><td>Tai-Dong</td></tr><tr><td>South</td><td>Kaochung</td></tr><tr><td>Middle-3</td><td>Nan-Tou</td></tr></table>

COUNTY

<table><tr><td>c#</td><td>county-name</td></tr><tr><td>c1</td><td>Hwa-Lane</td></tr><tr><td>c2</td><td>I-Lan</td></tr><tr><td>c3</td><td>Taipei</td></tr><tr><td>c4</td><td>Taichung</td></tr><tr><td>c5</td><td>Chung-Hwa</td></tr><tr><td>c6</td><td>Nan-Tou</td></tr><tr><td>c7</td><td>Kaochung</td></tr><tr><td>c8</td><td>Tai_dong</td></tr></table>

Figure 10. District Database  
dname
East-1
East-1
Taipei
Middle-1
Middle-1
East-3
South
Middle-3  
county-name
Hwa-Lane
I-Lan
Taipei
Taichung
Chung-Hwa
Tai-Dong
Kaochung
Nan-Tou

Six districts of minimum total measure of the unacceptability are formed to cover eight counties. The total measure of the unacceptability is 16.2.

## 5. Access Routines for Query Processing

A RELATIONAL DBMS MUST INCLUDE METHODS, OR ALGORITHMS, for implementing the proposed operators that can appear in a query execution strategy. For each such operation, one or more access routines are written to execute the operation. In this section we discuss typical algorithms used by access routines to implement the proposed operations.

## 5.1. Implementing the Match Operation

Relation R on attributes X and Y,

$R(X,Y),$

can be transformed into a bipartite graph $G(V_{1}, V_{2}, E)$ with bipartition $(V_{1}, V_{2})$ . Two sets of distinct instances of attributes X and Y in R correspond to two disjoint vertex sets $V_{1}$ and $V_{2}$ in G. A tuple $(v_{i}, v_{j})$ over attributes X and Y in R represents an edge $(v_{i}, v_{j})$ in E, for vertices $v_{i} \in V_{i}$ and $v_{j} \in V_{j}$ . One example of transformation from relation R on attributes X and Y into a bipartite graph $G(V_{1}, V_{2}, E)$ is shown in figure 11.

The match operation of relation R on attributes X and Y,

$$
\operatorname{MATCH} ((X, Y)),
$$

can be implemented by first transforming relation R on attributes X and Y into a bipartite graph and then the Hungarian Algorithm [4] is executed.

## 5.2. Implementing the Maxmatch Operation

Relation $R$ on attributes $X, Y$ , and $Z$ ,

$R(X,Y,Z),$

can be transformed into a weighted bipartite graph $G(V_1, V_2, E)$ with bipartition $(V_1, V_2)$ . A tuple $(v_i, v_j, w_k)$ over attributes $X, Y$ , and $Z$ in $R$ , where attributes $X$ and $Y$ uniquely identify attribute $Z$ , represents an edge $(v_i, v_j)$ with weight $w_k$ in $E$ , for vertices $v_i \in V_i$ and $v_j \in V_j$ . One example of transformation from relation $R$ on attributes $X, Y$ , and $Z$ into a weighted bipartite graph $G(V_1, V_2, E)$ is shown in figure 12.

The maxmatch operation of relation $R$ on attributes $X, Y$ , and $Z$ ,

$$
\text { MAXMATCH } ((X, Y), Z),
$$

can be implemented by first transforming relation R on attributes X, Y, and Z into a weighted bipartite graph and then the Kuhn-Munkres algorithm [4] is executed.

![](/api/attachments/QQAC6WQT/fulltext/images/6ccef45435e1c9d359ee97ff58d883cdc8120f7c42acb9f6fb3e7a4a1aa697b2.jpg)  
Figure 11. The Transformation from a Relation into a Bipartite Graph

## 5.3. Implementing the Cover, Mincover (Sumcover), Partition, Minpartition (Sumpartition) Operations

The set covering and partitioning operations—cover, mincover, sumcover, partition, minpartition, and sumpartition—are expensive to implement. Let us recall the definition of a set covering problem. A set $I = \{1, \ldots, m\}$ and a set $P = \{P_1, \ldots, P_n\}$ , where $P_j \subseteq I, j \in J = \{1, \ldots, n\}$ . A subset $J^* \subseteq J$ defines a cover of $I$ if

$$
\bigcup_ {j \in j ^ {*}} P _ {j} = I.
$$

Relation $R_{1}$ on attributes X and $Y_{1}$ and relation $R_{2}$ on $Y_{2}$ , where attributes $Y_{1}$ in $R_{1}$ and $Y_{2}$ in $R_{2}$ are defined on the same domain, can be transformed into a set covering problem. The instances of $Y_{2}$ in $R_{2}$ constitute set I and the relationship between attributes X and $Y_{1}$ in $R_{1}$ constitutes set P. The transformation from relation $R_{1}$ on attributes X, $Y_{1}$ and relation $R_{2}$ on $Y_{2}$ into the set covering problem is depicted in figure 13. In the transformation, all costs are treated as unit cost. Similarly, the set partitioning problem is obtained by replacing the inequality ( $\geq$ ) in figure 13 with equality (=). The cover and partition operations are implemented by first transforming the related relations into set covering and partitioning problems and then the search algorithm [45], enumeration algorithm [17], Pivot and Complement [2], or genetic algorithm [22, 31] is executed to find a cover or partition solution

Relation $R_{1}$ on attributes $X_{1}$ and Z, relation $R_{2}$ on attributes $X_{2}$ and $Y_{1}$ , and relation $R_{3}$ on $Y_{2}$ , where attributes $X_{1}$ in $R_{1}$ and $X_{2}$ in $R_{2}$ are defined on the same domain and attributes $Y_{1}$ in $R_{2}$ and $Y_{2}$ in $R_{3}$ are defined on the same domain, can be transformed into a set covering problem. The instances of $Y_{2}$ in $R_{3}$ constitute set I, the relationship between attributes $X_{2}$ and $Y_{1}$ in $R_{2}$ constitutes set P, and the instances of Z in $R_{1}$ constitute the cost of the sets. The transformation from relation $R_{1}$ on attributes $X_{1}$ and

![](/api/attachments/QQAC6WQT/fulltext/images/5d3cf6dae7febf833dd39dd7231c212aa2113fd32bc636904447a33d43de931c.jpg)  
Figure 12. The Transformation from a Relation into a Weighted Bipartite Graph

Z, relation $R_{2}$ on attributes $X_{2}$ and $Y_{1}$ , and relation $R_{3}$ on $Y_{2}$ , into the set covering problem is depicted in figure 14.

Similarly, the set partitioning problem is obtained by replacing the inequality ( $\geq$ ) in figure 14. The mincover, sumcover, minpartition, and sumpartition operations are implemented by first transforming the related relations into set covering and partitioning problems and then executing the search algorithm [45], enumeration algorithm [17], Pivot and Complement [2], or genetic algorithm [22, 31] to find a cover or partition solution.

## 5.4. Genetic Algorithms for Implementing Cover, Mincover, Sumcover, Partition, Minpartition, and Sumpartition Operations

Finding a solution of the cover, mincover, partition, or minpartition operation is an NP-complete problem. Most of the cost is spent on CPU time. If we assume the numbers of constraints and variables are m and n, respectively, then CPU and I/O costs will be exponential and $m*n+n$ , respectively. The latter n is the time to read the cost of all variables.

Some of the proposed operators are defined to find optimal solutions. It may take a very long time to find these optimal solutions so genetic algorithms $[22, 31]$ are adopted for the implementation of access routines for the proposed operators. We found that our genetic algorithm approach performed well on both the computational effort and the quality of the solutions through a variety of test problems. This approach makes it possible for a DBMS to respond to queries involving the proposed operators in a predicate restricted amount of time.

Genetic algorithms $[20, 21]$ are general-purpose optimization algorithms (somewhat akin to simulated annealing in that sense). They were developed by Holland $[21]$ to search irregular, poorly characterized spaces. Genetic algorithms are stochastic adaptive algorithms that start with a population of randomly generated candidates and “evolve” towards better solutions by applying genetic operators such as crossover, mutation, and inversion, modeled as natural genetic inheritance and Darwinian survival-of-the-fittest principle. Over the past years, genetic algorithms have been applied to a variety of functional optimization problems, and have been shown to be highly effective in searching large, complex search space even in the presence of high-dimensionality, multimodality, and discontinuity. The genetic algorithm does not necessarily find an optimal to any one problem, but it does find good solutions to problems that are resistant to most other known techniques. The outline of a genetic algorithm is shown in figure 15.

![](/api/attachments/QQAC6WQT/fulltext/images/1702d98bb9624bbb3d0b17540df87aff7a5907817a7fb718eb22e9d463be2ef1.jpg)  
Figure 13. The Transformation from Relations into a Zero-One Integer Programming with Unit Cost

![](/api/attachments/QQAC6WQT/fulltext/images/af7c0d6af2064e7091bb8912913849e8d9eb6bb99b95dcbfad3e71e51d189d78.jpg)  
Figure 14. The Transformation from Relations into a Zero-One Integer Programming with Different Cost

Liepins et al. [31] developed genetic algorithms for set covering problems. Genetic algorithms with two types of crossover operators were investigated in conjunction with three penalty function and two multiobjective formulations. Pareto multiobjective formulation and greedy crossover are suggested well.

We modify the penalty function and use greedy crossover to solve set covering problems. In addition, we define a penalty function and use the same greedy crossover to solve set partitioning problems. We found they performed well on both the computational effort and the quality of the solutions through a variety of test problems. The computational complexity of the algorithm for set covering problems is $O(m*n)$ , where m and n are the numbers of constraints and variables (i.e., the numbers of rows and columns of matrix A), respectively. The genetic algorithm for set partitioning problems requires at most $O(m_{1}*n_{1}*m*n)$ , where $m_{1}$ is the population size, and $n_{1}$ is the maximum value of the sum of ones in all populations. The value of $n_{1}$ will be less than that of n. The algorithms are bounded by a polynomial time. The detail of the algorithms is given in [22].

Simulations have been performed for the set covering problem on 18 test problems, and for the set partitioning problem on 15 test problems. The problem size of set covering problems was obtained from [44]. Some problems in [44] come from real-world applications such as American Airlines, and some were randomly generated. The problem size of set partitioning problems 1–5 was obtained from [2]. These problems come from American Airlines. The remaining ten problem sizes were designed by the authors. The examined instances have been generated as follows. The A matrix for all set covering and set partitioning problems was obtained from a matrix generator. All the test problems have coefficient matrices whose density is from 10 percent. If a row or a column of A does not contain 1 in the row or the column, then one 1 is added in any entry of the row or column. That is, each row or column must contain at least one 1. Following the work of [2], the coefficient of the objective function was equal to the number of ones in the corresponding column plus a random variable between 0 and 1. Information on these test problems, as well as on the computational results, is presented in Tables 1 and 2. The genetic algorithms were programmed in C and run on a DEC station 5000/200.

We also ran our genetic algorithms on two set covering problems: $A_{27}$ , $A_{45}$ whose optimal solutions are known. Problems $A_{27}$ and $A_{45}$ are taken from [16]. These two problems are difficult set covering problems [16]. Table 3 shows the test problems, the size of the best known cover for each, and the size of the cover obtained from the proposed genetic algorithms. From the table, we can find that good solutions can be obtained from queries involving the extended operators.

In the following we explain the meaning of the CPU times in Tables 1 and 2. To illustrate our explanation, we refer to the schema of figure 6 once more, especially to the EM relation. We illustrate the CPU time by using the following example operation:

(OP1): MINCOVER((EM.ename, EM.skill), PROJECT.skill, SALARY.salary)

<table><tr><td>Initialize the parameters of the genetic algorithm;Randomly generate the old_population;for generation := 1 to max_generationClear the new_population;Compute the fitness of each individual in the old_population;Copy the highest fitness of each individual in the old_population;While the no_of_individual population_size doSelect two parents from the old_population based on their fitness values;</td></tr></table>

Figure 15. The Outline of GAs

Table 1 Computational Results with Genetic Algorithm for Set Covering Problems

<table><tr><td>No. of test</td><td>m</td><td>n</td><td>CPU time* (seconds)</td></tr><tr><td>1</td><td>15</td><td>32</td><td>0.060</td></tr><tr><td>2</td><td>30</td><td>30</td><td>0.156</td></tr><tr><td>3</td><td>30</td><td>40</td><td>0.218</td></tr><tr><td>4</td><td>30</td><td>50</td><td>0.316</td></tr><tr><td>5</td><td>30</td><td>60</td><td>0.339</td></tr><tr><td>6</td><td>30</td><td>70</td><td>0.476</td></tr><tr><td>7</td><td>30</td><td>80</td><td>0.546</td></tr><tr><td>8</td><td>30</td><td>90</td><td>0.437</td></tr><tr><td>9</td><td>200</td><td>300</td><td>17.281</td></tr><tr><td>10</td><td>200</td><td>413</td><td>24.580</td></tr><tr><td>11</td><td>50</td><td>450</td><td>4.402</td></tr><tr><td>12</td><td>36</td><td>455</td><td>3.706</td></tr><tr><td>13</td><td>104</td><td>498</td><td>10.731</td></tr><tr><td>14</td><td>200</td><td>500</td><td>23.350</td></tr><tr><td>15</td><td>46</td><td>683</td><td>7.921</td></tr><tr><td>16</td><td>26</td><td>777</td><td>4.890</td></tr><tr><td>17</td><td>50</td><td>905</td><td>12.041</td></tr><tr><td>18</td><td>134</td><td>1642</td><td>62.554</td></tr></table>

\* DEC station 5000/200.  
m = number of constraints; n = number of variables.

Table 2 Computational Results with Genetic Algorithm for Set Partitioning Problems

<table><tr><td>No. of test</td><td>m</td><td>n</td><td>CPU time* (seconds)</td></tr><tr><td>1</td><td>13</td><td>87</td><td>0.269</td></tr><tr><td>2</td><td>13</td><td>63</td><td>0.191</td></tr><tr><td>3</td><td>14</td><td>71</td><td>0.246</td></tr><tr><td>4</td><td>12</td><td>75</td><td>0.292</td></tr><tr><td>5</td><td>13</td><td>88</td><td>0.312</td></tr><tr><td>6</td><td>50</td><td>200</td><td>20.049</td></tr><tr><td>7</td><td>100</td><td>300</td><td>102.908</td></tr><tr><td>8</td><td>100</td><td>400</td><td>108.020</td></tr><tr><td>9</td><td>100</td><td>50</td><td>127.571</td></tr><tr><td>10</td><td>100</td><td>60</td><td>159.875</td></tr><tr><td>11</td><td>150</td><td>700</td><td>696.775</td></tr><tr><td>12</td><td>200</td><td>800</td><td>773.126</td></tr><tr><td>13</td><td>200</td><td>900</td><td>830.743</td></tr><tr><td>14</td><td>100</td><td>1000</td><td>476.942</td></tr><tr><td>15</td><td>200</td><td>1000</td><td>1996.273</td></tr></table>

$m =$ number of constraints; $n =$ number of variables.  
\* DEC station 5000/200.

To illustrate this, consider OP1 and assume that the EM relation consists of m distinct employees and n distinct skills. Also, assume that the relation has $lm*n*0.1$ (the density of ones is 10 percent) tuples. For example, test 9 in Table 1 consists of 300 distinct employees and 200 distinct skills and has 6,000 tuples. The CPU time to find a set of employees with minimum total salary that represent all the skills necessary for a certain job is 17.281 seconds. From the CPU times in Tables 1 and 2, we find that the time of database access for set covering and partitioning problems is acceptable.

## 6. Conclusion

GRAPH MATCHING, SET COVERING AND PARTITIONING PROBLEMS are both theoretically and practically important in decision support systems. Numerous applications have been modeled as graph matching, set covering, and partitioning problems. We have discussed the integration of database systems and model systems for zero-one integer programming problems, especially concerning graph matching, set covering, and partitioning problems. We integrate both problem formulation and model execution in a single integrated language. Users can directly use the language to get the required decision support information from the database.

Table 3 Problem Set

<table><tr><td>Problem</td><td>Integer program variables/constraints</td><td>Genetic algorithm</td><td>Optimal value</td></tr><tr><td colspan="4">Value</td></tr><tr><td> $A_{27}$ </td><td>27/116</td><td>18</td><td>18</td></tr><tr><td> $A_{45}$ </td><td>45/330</td><td>31</td><td>30</td></tr></table>

We described formulation of graph matching, set covering, and partitioning problems in SQL. We define special operators for the “WHERE” clause of SQL expressions to give a shorthand notation of such problems. Six operators—match, maxmatch, cover, mincover, partition, and minpartition—are defined. These operators can be used in the “WHERE” clause of SQL statements. Hence, users with knowledge of SQL can easily take advantage of the increased decision support capabilities without learning a new language.

Some of the proposed operators are defined to find optimal solutions. It may take a very long time to find these optimal solutions so genetic algorithms are adopted for the implementation of access routines for the proposed operators. We found that our genetic algorithm approach performed well on both the computational effort and the quality of the solutions through a variety of test problems. This approach makes it possible for a DBMS to respond to queries involving the proposed operators in a predicate restricted amount of time.

## REFERENCES

1. Applegate, L.M.; Konsynski, B.R.; and Nunamaker, J.F. Model management systems: design for decision support. Decision Support Systems, 2 (1986), 81–91.

2. Balas, E., and Martin, C.H. Pivot and complement—a heuristic for 0–1 programming. Management Science, 26, 1 (1980), 86–96.

3. Blanning, R.W. A relational framework for model management in decision support systems. Decision Support Systems (June 1982), 16–22.

4. Bondy, J.A., and Murty, U.S.R. Graph theory with applications. London: Macmillan Press, 1976.

5. Bonczek, R.H.; Holsapple, C.W.; and Whinston, A.B. A generalized decision support system using predicate calculus and network data base management. Operations Research, 29, 2 (1981), 263–281.

6. Choobineh, J. SQLMP: a data sublanguage for representation and formulation of linear mathematical models. ORSA Journal on Computing, 3, 4 (Fall 1991), 358–375.

7. Codd, E.F. The Relational Model for Database Management, Version 2. Reading, MA: Addison-Wesley, 1990.

8. Date, C.J. An Introduction to Database Systems, vol. 1, 5th ed. Reading, MA: Addison-Wesley, 1990.

9. Date, C.J. A critique of the SQL database language. In C.J. Date (ed.), Relational Database: Selected Writings. Reading, MA: Addison-Wesley, 1986. [Originally published in ACM SIGMOD Record, 14, 3 (1984).]

10. Dattero, R.; Ramirez, R.G.; and Choobineh, J. Derived relations with exceptions: decision support capabilities. Journal of Management Information Systems, 6, 4 (Spring 1990), 83–101.

11. Donavan, J. Database system approach to management decision support. ACM Transactions on Database Systems, 1, 4 (1976), 344–369.

12. Eder, J. Extending SQL with general transitive closure and extreme value selections. IEEE Transactions on Knowledge and Data Engineering, 2, 4 (1990), 381–390.

13. Elam, J.J.; Henderson, J.C.; and Miller, L.W. Model management systems: an approach to decision support in complex organizations. Proceedings of the First Conference on Information Systems, 1980.

14. Fishman, D.; Beech, D.; Cate, H.P.; Chow, E.C.; Connors, T.; Davis, J.W.; Derrett, N.; Hoch, C.G.; Kent, W.; Lyngbaek, P.; Mahbod, B.; Neimat, M.A.; Rayn, T.A.; and Shan, M.C. Iris: an object-oriented database management system. ACM Transactions on Office Information Systems, 5, 1 (1987), 48–69.

15. Fourer, R.; Gay, D.; and Kernighan, B.W. AMPL: a mathematical programming language. Management Science, 36, 5 (1990), 519–554.

16. Fulkerson, D.R.; Nemhauser, G.L.; and Trotter Jr., L.E. Two computationally difficult set covering problems that arise in computing the 1-width of incidence matrices of steiner triple systems. Mathematical Programming Study, 2 (1974) 72–81.

17. Garfinkel, R.S., and Nemhauser, G.L. Integer Programming. New York: John Wiley, 1972.

18. Geoffrion, A. M. An introduction to structured modeling. Management Science, 33, 5 (1987), 547–588.

19. Geoffrion, A. M. FW/SM: A prototype structured modeling environment. Management Science, 37, 12 (1991), 1513–1538.

20. Goldberg, D.E. Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley, 1989.

21. Holland, J.H. Adaptation in natural and artificial systems. Ann Arbor: University of Michigan Press, 1975.

22. Horng, J.T.; Chen, G.D.; and Liu, B.J. A team-oriented query language. Department of Computer Science and Information Engineering Technical Report, National Taiwan University, Taiwan, 1992.

23. Karmarker, N.; Resende, M.G.C.; and Ramakrishnan, K.G. An interior point algorithm to solve computationally difficult set covering problems. Mathematical Programming, 52 (1991), 597–618.

24. Klein, G. Developing model strings for model managers. Journal of Management Information Systems, 3, 2 (Fall 1986), 94–110.

25. Klein, G.; Konsynski, B.; and Beck, P. A linear representation for model management in DSS. Journal of Management Information Systems, 2, 2 (Fall 1985), 40–54.

26. Konsynski, B. Model management in decision support systems. In C.W. Holsapple and A.B. Whinston (eds.), Data Base Management: Theory and Applications. Boston: D. Reidel, 1983.

27. Konsynski, B., and Dolk, D. Knowledge abstractions in model management. Decision Support Systems (1982).

28. Konsynski, B., and Dolk, D. Knowledge representations for model management systems. IEEE Transactions on Software Engineering, 10, 6 (1984), 619–628.

29. Lans, R.F. van der. Introduction to SQL. Reading, MA: Addison-Wesley, 1988.

30. Liang, T. Integrating model management with data management in decision support systems. Decision Support Systems, 3, 1 (1985), 221–232.

31. Liepins, G.E.; Hilliard, M.R.; Richardson, J.; and Palmer, M. Genetic algorithms applications to set covering and traveling salesman problems. In D.E. Brown and C. White, III (eds.), Operations Research and Artificial Intelligence: The Integration of Problem-Solving Strategies.

Operations Research and Artificial Intelligence: The Integration of Problem-Solving Strategies. Kluwer, 1990, pp. 29–57.

32. Linemann, V. Non first normal form relations and recursive queries: an SQL-based approach. Proceedings of the Third International Conference on Data Engineering, Los Angeles, 1987, pp. 591–598.

33. Lovasz, L., and Plummer, M.D. Matching Theory. New York: Elsevier Science Publishers, 1986.

34. Mannino, M.V., and Shapiro, L.D. Extensions to query languages for graph traversal problems. IEEE Transactions on Knowledge and Data Engineering, 2, 3 (1990), 353–363.

35. McHugh, J.A. Algorithmic Graph Theory. Englewood Cliffs, NJ: Prentice-Hall, 1990.

36. Murphy, F., and Stohr, E.A. An intelligent system for formulating linear programs.

Decision Support Systems, 2 (1986), 39–47.

37. Ozsoyoglu, G.; Ozsoyoglu, Z.M.; and Matos, V. Extending relational algebra and relational calculus with set-valued attributes and aggregate functions. ACM Transactions on Database Systems, 12, 4 (1987), 566–592.

38. Ozsoyoglu, G.; Matos, V.; and Ozsoyoglu, Z.M. Query processing techniques in the summary-table-by example database query language. ACM Transactions on Database Systems, 14, 4 (1989), 526–573.

39. Pistor, P., and Anderson, F. Designing a generalized NF2 model with an SQL-type language interface. Proceedings of the 12th Very Large Data Base Conference, Kyoto, Japan, 1986, pp. 278–285.

40. Pistor, P., and Traunmueller. A database language for sets, lists, and tables. Information Systems, 11, 4 (1986), 323–336.

41. Ramirez, R.G.; Kulkarni, U.R.; and Moser, K.A. Performance analysis of "what-if" database using independently updated views. Journal of Management Information Systems, 9, 1 (Summer 1992), 185–203.

42. Roth, M.A.; Korth, H.F.; and Batory, D.S. SQL/NF: a query language for 1NF relational databases. Information Systems, 12, 1 (1987), 99–114.

43. Rowe, L.A., and Stonebraker, M. The POSTGRES data model. In Proceedings of the 13th Conference on Very Large Databases, Brighton, 1987, pp. 83–96.

44. Salkin, H.M., and Koncal, R.D. Set covering by an all integer algorithm: computational experience. Journal of ACM, 20, 2 (1973), 189–193.

45. Salkin, H.M., and Mathur, K. Foundations of Integer Programming. New York: Elsevier Science Publishing, 1989.

46. Stonebraker, M.; Anton, J.; and Hanson, E. Extending a database system with procedures. ACM Transactions on Database Systems, 12, 3 (1987), 350–376.

47. Zheng, W.M. A novel rotating orthogonal method for combinatorial optimization. Proceedings of the Systems, Man, and Cybernetics, New York, 1992, pp. 1185–1188.
