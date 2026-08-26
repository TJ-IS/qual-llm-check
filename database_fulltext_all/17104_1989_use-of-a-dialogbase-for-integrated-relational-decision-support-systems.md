---
otero_id: 17104
otero_key: "XVP79USW"
title: "Use of a dialogbase for integrated “relational” decision support systems"
authors: "Eui-Ho Suh; Hirohide Hinomoto"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90035-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Use of a Dialogbase for Integrated "Relational" Decision Support Systems

Eui-Ho SUH

Department of Management, Oklahoma State University, Stillwater, OK 74078, USA

Hirohide HINOMOTO

Department of Business Administration, University of Illinois at Urbana-Champaign, Champaign, IL 61820, USA

A traditional decision support system (DSS) is comprised of three subsystems: (1) database and database management, (2) modelbase and modelbase management, and (3) dialogue management. While the first two subsystems have their own "base," the dialogue subsystem does not. The relational view, among others, has been used to organize the database and the modelbase subsystems, however, there has been little progress in adopting a similar concept for the dialogue subsystem. In this paper, the concept of "dialogbase," a base for menu-driven dialogue using a relational framework, is suggested for an integrated "relational" decision support system

Keywords: Decision Support System, Relational View, Dialogbase.

![](/api/attachments/XVP79USW/fulltext/images/6f6da1d1b7e22149f520c3210ad6ca5e206749c33f72e40dd7c71b806a2ba984.jpg)

Eui-Ho Suh received a B.S. from Seoul National University, a M.S. from KAIS (Korea), a M.S. from Stanford University, and a Ph.D. from the University of Illinois at Urbana-Champaign. He was on the faculty of Department of Management at Oklahoma State University during 1987–1989 before joining the Pohang Institute of Science & Technology (POSTECH) in Korea. He is currently teaching MIS in the Department of Industrial Engineering at POSTECH.

His current research interests include decision support systems, object-oriented systems, databases, and expert systems.

![](/api/attachments/XVP79USW/fulltext/images/bdf140f161925176e0650df37448d8a06b7235388b23fe6f9acfac4ce5c69d5f.jpg)

Hirohide Hinomoto received a Ph.D. in industrial engineering from the University of Michigan in 1963. Since then he has been at the University of Illinois, where he is currently a professor of business administration. His research has been in the areas of capital capacity expansion, capital investment analysis, economic evaluation of information systems, and decision support systems.

## 1. Introduction

A DSS is characterized as an interactive computer-based system that helps decision makers utilize data and models to solve semi-structured problems [1,31]. The three words - interactive, data and models - in this definition are the key considerations in constructing a DSS.

The literature on designing DSS [2,31,34] identifies three “traditional” major functions or conceptual components of a DSS: management of data, management of models, and management of dialogue between the user and the system (fig. 1).

Each component of a DSS in fig. 1, except the dialogue component, consists of a base (storage) and a management system.

The obvious questions is, “If it is possible to develop a base and its management system for data or models, why not for dialogue, the third component of DSS?” Particularly, since a menu-driven dialogue has a distinct number of choices in each menu that could be stored separately, the dialogue system can have its own base (dialog-based). The main advantage of creating a dialog-base is that we can create a separate database for the dialogue, and the three bases (data, model, dialogue) can ultimately be integrated into a single

![](/api/attachments/XVP79USW/fulltext/images/c270ee045e17b8be1ecc9ff8d77b869013f223356ef15f425101d9c3952760ba.jpg)  
DBMS: Database Management System
MBMS: Modelbase Management System
DGMS: Dialog Generation and Management System

Fig. 1. Three Traditional Components of a DSS.

![](/api/attachments/XVP79USW/fulltext/images/d938310e066ddbea411590e216f257873902b4e9de0f5c325e5bd27eda18033c.jpg)  
DGB: Dialogbase  
DSMS: Decision Support Management System  
Fig. 2. Using a Single Framework in a DSS.

base. Therefore, a single software system, which is a relational one in our study, might be used for handling an entire DSS (fig. 2).

In fig. 2, the single software system, tentatively named Decision Support Management System (DSMS), replaces functions of DBMS, MBMS, and DGMS.

In developing the structure of database and modelbase with their corresponding management systems, the “relational concept,” owing to its user friendliness, has been used quite often. The relational representation of data has been the subject of much research $[12,17,18,20]$ . A similar concept for modelbase is currently under development as well $[3,4,5]$ .

There are apparent advantages in seeing the dialogbase within a relational framework. First, since many of the operations performed on dialogbase have counterparts in relational data and model managements, most concepts developed in those areas are easily applied. Second, as already mentioned, it is possible to develop a single relational software system of DSS to handle all three bases of data, model and dialogue.

As shown in fig. 2, we could store a set of relations of data (DB), a set of models (MB), and a set of relations for a menu-driven dialogue (DGB) in a DSS. Then, we could use a single relational DSMS to manage all of the three bases which may be thought of as corresponding to a single base because a model is equivalent to a relation under the relational modelbase concept [4].

In order to develop a relational dialogbase, we will develop a conceptual model and convert it into a set of relations with some propositions for this conversion.

## 2. Three "Traditional" Components of DSS

## 2.1. Database and Database Management

A database is a collection of related data which is organized so that useful information may be extracted for decision making and so that duplicate data collection is minimized. The effectiveness of a database is derived from the fact that much of the information that is relevant to a variety of organizational purposes may be obtained from one single, comprehensive data set.

Many articles in the literature list the advantages of the database concept which include, among others, integration and sharing of data along with data independence [13,35].

The management of a database, which maintains the factual basis of a DSS, requires a DBMS to have specific capabilities. This system just provides an access mechanism to the data, a data directory to maintain data definitions, and descriptions of the types and sources of data in the system; a query facility to interpret requests for data; and a staging and extraction function for accessing external sources of data and connecting the DSS with its relevant neighboring systems. DBMS is a central part of data management and a discussion of its generic needs $[15]$ is helpful in understanding a DBMS and how it is used. Since there has been some contention over which type of DBMS will best serve the objectives of user organizations, there has been some research conducted concerning that controversy $[28]$ . Also, there have been some studies on evaluations of data models and DBMS by McGee $[25]$ and Zahedi $[37]$ .

## 2.2. Modelbase and Modelbase Management

Research surveys have documented a marked growth in the use of corporate modeling in the past decade. These models, used as aids to planning activities, range from the very limited to the comprehensive. The development of computer-based modeling can be traced from its early stages which were characterized by a long communication chain between the decision maker and the computer, operational control problems, and primitive data handling methods. At this time, there was an emphasis on model management in management information systems (MIS) [30] and on relationships between models and managers [23]. This evolution of models in DSS has been discussed in detail by Bonczek, Holsapple and Whinston [6].

A systematic environment must be provided in order for managers to solve semi-structured problems using model units. Model units must be stored in an open model storage area easily accessible to managers so that they may become well aware of the existence and varieties of model units. This area is termed a “modelbase.” The modelbase concept considers a model as a data abstraction consisting of equations, elements, and solution procedures $[21]$ .

According to Ariav & Ginzberg [2], the ideal model management facility should provide: (1) a modelbase management system [MBMS] to generate, retrieve and update parameters, to restructure models, and to include a model directory for maintaining information about available models; (2) model execution to control the actual running of the model and to link models together when integration is needed; (3) a modeling command processor to accept and interpret modeling instruction as they flow out of the dialogue component and to route them to the MBMS or the model-execution function; and (4) a database interface to retrieve data items from the database for running models, and, eventually, to store model outputs in the database for further processing, perusal, or as input to other models. In contrast, the traditional view of modeling is the stand-alone model, in which the model is a “black box” and outputs are automatically generated from inputs.

A MBMS generates models through a model definition language and restructures or redefines a model in response to changes. It updates a model in response to changes in data such as a revised parameter estimate.

## 2.3. Dialogue Management

Whatever the form of use, DSS usage involved a dialogue between the user and the DSS. Buneman et al. [8] indicate that the most complicated mathematical models, the most comprehensive databases, or the most detailed instructions are all ineffective as decision support devices unless their methods, information, and results can be effectively communicated to the manager who must make the decisions. Even if a DSS provides extremely powerful functions, it may not be used if the dialogue is unacceptable. There have been some effective dialogue designs used to support DSS [8,10,22].

Functions of dialogue management are summarized as follows [31]: (1) it produces the output representations; (2) it enables user inputs that invoke and provide parameters for operations; (3) it enables user inputs that invoke and provide parameters for the memory aids; and (4) it provides the control mechanisms that enable the user to combine outputs and inputs into processes.

Dialogue style – the nature of the interface between the system and the user – includes question/answer (Q/A) style, command mode, input/output (I/O) form, and menu-driven dialogue. Some combinations of these are also possible. Q/A is very common in DSS, employing line-at-a time terminals. DSS asks the user a question and the user answers it until the DSS produces the answers needed to support the decision. MYCIN [14] is a known DSS using this style. Eason [16] suggests that Q/A tends to be one of the most successful styles for inexperienced or infrequent users who are unfamiliar with the problem to be solved. Command language mode involves verb-noun form. For complicated applications, it can become a programming language. Several DSS use this style [9]. I/O form provides input forms in which the user enters commands and data, and output forms on which the DSS produces responses. After viewing an output form, the user can fill in another input form to continue the dialogue. Query-By-Example [38] employs this type of dialogue.

Most DSS use menu-driven dialogue and it has been shown that the menu-driven dialogue is very efficient when human factors are considered $[26]$ . This type of dialogue is popular for DSS which utilize CRT terminals. It lets the user select from a menu of alternatives, such as report names or a computation command. Q/A style can become this type of dialogue if it has a finite number of answers for each question.

## 3. Creation of Dialogbase

The logical dialogbase design is featured in two stages: (1) designing the conceptual schema, and (2) translating it into an object data model, in our case, relational model. We propose the decision–relationship (D–R) diagram, similar to the entity–relationship (E–R) diagram, to describe the conceptual schema, and the translation process of the schema from the decision–relationship model to the relational model, which will be explained later.

In designing the logical dialogbase, we concentrate on the case of menu-driven dialogue with quantifiable outcomes. Quantifiable outcomes imply that the outcomes generated from the DSS, after decision-makers choose alternatives from a series of menus, are quantifiable.

Fig. 3 shows a menu-driven tree which is conceptually drawn from a menu-driven dialogue. In this tree, with N number of menus, the ith menu will appear after decision maker chooses an alternative from the $(i - 1)$ th menu.

In this figure, squares represent decision points generating alternative decisions while circles indicate chance points generating alternative chances. We should note that the chances are determined by the state of nature, not the decision maker. However, since we are more interested in the retrieval of the intermediate outcomes and/or the final outcome, we reasonably assume that we can ask the question, “what would be the outcome if the chance is p?”

The E-R model, originally proposed by P. Chen [11], is now used to describe a conceptual schema. The detailed definition of the model is further described and formalized by Ng and Paul [27]. Wong and Katz [36] show how a relational schema may be derived from an entity–relationship diagram.

![](/api/attachments/XVP79USW/fulltext/images/c14aed2763886f82648b8de04f84436cf53a9c8a32d6c95be1676580a71f79b0.jpg)  
MENU 1 MENU 2....MENU N  
Fig. 3. Menu-driven Tree.

Similarly, a D–R diagram can be designed with some relevant definitions. Details of this process have been presented by Suh [32] and summarized as follows. This process includes the definitions of decision set, chance set and relationship set, and shows two types of D–R diagrams.

Definition 1 (Identical Level). Nodes are in the identical level if they are of the same depth. Arcs are in the identical level if they are generated from nodes in the identical level. From this point on, when the word “level” is used without any further clarification, it refers to the identical level associated with arcs rather than nodes.

Definition 2 (D-Set). A D-Set (or Decision Set) is a set of decisions in the same level and is denoted by $d_{i}$ ( $Id_{i}, d_{i1}, d_{i2}, \ldots, d_{in}$ ). $Id_{i}$ is an identifier of the D-Set where i is the level number while $d_{i1}, d_{i2}, \ldots, d_{in}$ are the non-identifier elements in the D-Set.

Definition 3 (C-Set). A C-Set (or Chance Set) is a set of chances in the same level and is denoted by $C_i$ ( $Ic_i$ , $c_{i1}$ , $c_{i2}, \ldots, c_{in}$ ). $Ic_i$ is an identifier of the C-Set where $i$ is the level number while $c_{i1}$ , $c_{i2}, \ldots, c_{in}$ are the non-identifier elements of the C-Set.

Definition 4 (E-Set). An E-Set is a global representation for a D-Set or a C-Set and is denoted by $E_{i}$ ( $Ie_{i}, e_{i1}, e_{i2}, \ldots, e_{in}$ ).

Definition 5 (R-Set). An R-Set (or Relationship Set) for a subtree with k-height is a $(k+1)$ tuple of $R(Ie_{1}, Ie_{2}, \ldots, Ie_{k}, p)$ while $Ie_{i}$ is the identifier of $E_{i}$ . $E_{i}$ denotes either $D_{i}$ or $C_{i}$ . The notation of p refers to the payoff or the outcome. One exception is that if i is 1, the first level, the elements of an R-set would be $Ie_{1}$ and p of the first level, which may be eliminated if we include p in the set $E_{1}$ . Thus, the definition of E-Set for the first level would be modified as follows.

Definition 6 (Modified E-Set). A modified E-Set is a set of decisions or chances of the same level and

is denoted by:

$$
\begin{array}{l} E _ {i} (I e _ {i}, e _ {i 1}, e _ {i 2}, \ldots , p _ {i}) \quad \text { where } i = 1, \\ E _ {i} (I e _ {i}, e _ {i 1}, e _ {i 2}, \ldots) \quad \text { where } i \geq 2. \end{array}
$$

Given these definitions, a possible D-R diagram which is essentially a sequential diagram could be constructed (fig. 4). A D-R diagram can be used as a basis for a unified view of decisions/chances. It also can be used as a framework from which a relational schema is derived. In fact, a D-R diagram is a specialization of an E-R diagram where the decision/chance sets are entity-set compatible.

In fig. 4, a right-half circle and a left-half circle represent a D-Set and a C-Set, respectively. An R-Set is represented by a diamond shape and the elements of each set are put in circles. It is obvious that $N + (N - 1)$ sets are represented here.

However, many element redundancies in R-Set exist. For example, $R_{i}$ includes identifiers from $E_{1}$ to $E_{i}$ while $R_{i-1}$ has identifiers from $E_{1}$ to $E_{i-1}$ . (i-1) elements are essentially redundant. This could be a critical problem when we have a tall menu-driven tree. Also, it may lead to an inefficient relational schema after conversion. For these reasons, a modified D-R diagram is proposed by making a modified definition of R-Set, as shown in fig. 5.

Definition 7 (Modified R-Set). A modified R-Set is a set of 5-tuple denoted by: $R_{i}$ ( $m_{i}$ , $Ie_{i}$ , $m_{j}$ , $Ie_{j}$ , $p_{j}$ ) while $R_{i}$ represents the relationship between the set i and the set j. The indices of i and j are a pair of adjacent numbers ( $j = i + 1$ ). $m_{i}$ is the mth appearance of the ith decision/chance in the leftmost-child-right-sibling (LCRS) sense. This uniquely identifies any specific decision/chance appearing on the tree even though they belong to the same decision/chance set.

![](/api/attachments/XVP79USW/fulltext/images/f49bcd7456d07a99dd2e003b62d5bca21456def5877eff086ef625786fbee3ae.jpg)  
Fig. 4. Decision-Relationship Diagram.

![](/api/attachments/XVP79USW/fulltext/images/042aabef819f5a1d4a648b325ec738ced9005f2d1bdb53efd01e2abc06a83bd1.jpg)  
Fig. 5. Modified Decision-Relationship Diagram.

Definition 8 (Availability). Availability in decisions/chances denoted $a_d^i$ is the number of decision/chances available in the $i$ th level. Availability in payoff (outcome) denoted $a_p^i$ is the number of payoffs (outcomes) available in the $i$ th level. In general, $a_p^i = a_d^{i-1} * a_d^i$ , assuming each decision/ chance point generates the same kinds of decisions/chances in a given level. $Ie_i^j$ denotes the $j$ th available decision/chance in the level $i$ while $p_i^j$ is the $j$ th available payoff (outcome) in the level $i$ . The value of $j$ is determined in the LCRS sense.

## 4. Relational View of Each Base

## 4.1. Database

The relational view of a database is well described by Date [13] as “given a collection of sets, R is a relation on those n sets if it is a set of ordered n-tuples $d_{1}, d_{2}, \ldots, d_{n}$ such that $d_{1}$ belongs to $D_{1}$ . Sets $D_{1}, D_{2}, \ldots, D_{n}$ are the domains of R.” A relation is simply a two-dimensional table that has several properties. The first is that the entries in the table are single-valued. Second, the entries in any column are all the same type. Finally, no two rows in the table are identical. The order of the rows and columns is immaterial.

Several modification anomalies are suggested that should be considered when designing a relational database. Decomposition of a universal relation [19] might be necessary in order to this. Deletion anomalies arise when we are losing more information than we want to. We lose facts about two entities with one deletion. This characteristic is considered undesirable because it is usually unintended. Insertion anomalies occur when we gain facts about two entities with one insertion; or, stated negatively, we cannot insert a fact about one entity until we have an additional fact about another entity. Updating anomalies are also to be considered.

Codd [12] defined first, second, and third normal forms (1NF, 2NF, 3NF) to avoid those anomalies. Later, Boyce–Codd normal form (BCNF) was postulated, and then fourth and fifth normal forms were defined [18].

However, none of these could be considered perfect until Fagin [17] defined a new normal form called DK/NF. Fagin showed that a relation in DK/NF is free from all modification anomalies, regardless of their type.

## 4.2. Modelbase

A relational view of a modelbase was developed by Blanning $[3,4,5]$ . In his view, domains are inputs and outputs, and it is assumed that a model may be viewed as a relation whose attributes are the inputs and outputs of the model, just as a file may be viewed as a relation whose attributes are the key and contents of the file.

Fig. 6 shows the similarity of the retrievals between the database and the modelbase using IBM-developed SQL query language.

However, some of processing anomalies do exist, which leads to three types of normal forms, called alpha, beta, and gamma form.

DATABASE

MODELBASE

SELECT ACT

SELECT x

FROM STUDENT

FROM RLP

WHERE SID=100

WHERE A = A\*

and $b = b^{*}$

and $\mathbf{c} = \mathbf{c}^{*}$

(Query: What is the student activities taken by student 100?)

(Query: What is the output values of x when inputs are A\*, b\* and c\*?)

Fig. 6. Queries in DB and MB.

These anomalies are input, search and output anomalies. The concepts of those are following [4]:

(a) Input anomalies: An input anomaly occurs whenever a use, requiring an output of a model to be calculated, must enter at least one input that is not needed for the calculation of that output. Input anomalies are similar to (but not identical with) the anomalies that lead to the second normal form in relational data management.

(b) Search anomalies: A search anomaly occurs whenever there is a transitive dependency in a relation, for example, of the form (price → sales volume, sales volume → production cost). This requires that the user who wishes to determine the production cost resulting from a given sales volume enter different values of the price until that volume is realized, and with it the corresponding production cost. This anomaly is equivalent to the one which leads the third normal form in relational data management.

(c) Output anomalies: They are nondeterministic response to a user query. One cause of non-determinism is the presence of two or more identical output attributes in different models (e.g. in two models, both of which calculate production cost). The elimination of such anomalies leads to a normal form in which the output attributes of all of the models are pairwise disjoint.

Some criteria for relational completeness in a modelbase are optimization and sensitivity analysis, as well as selection, which is used in database management. By optimization, the user identifies a nonvoid subset of the input attributes of a relation, a single output attribute, and a maximum or minimum designator. In sensitivity analysis, the output is not a relation but rather a set of sensitivity measures of an output attribute with respect to an input attribute.

Implementation issues are discussed including some issues in regard to the implementation of joins. TQL, a model query language based upon the domain relational calculus, has been proposed by Blanning [3].

## 4.3. Dialogbase

The following rules for translating the D-R diagram into a relational schema for dialogbase are proposed.

1. Each D-Set or C-Set has an explicit identifier which represents the set uniquely in the relational schema, which is called a key.

2. Attributes are the non-identifier elements and the key.

3. The key of a set (either D-Set or C-Set or R-Set), along with all the non-key attributes forms a relation.

4. The key of an R-Set is composite and forms a relation with the non-key attributes, p.

5. The number of tuples in each relation of D-Set/C-Set is equal to the number of decision/ chances in the set.

6. The tuples in an R-Set form a certain subset of the Cartesian product of the previous set and the following set.

From these mapping steps, in fig. 7, we construct a relational schema corresponding to the fig. 5. $N + (N - 1)$ relations are presented.

The following propositions are suggested in reference with the above mapping rules:

Proposition 1. A set of relations in a relational schema is called “properly established” if the corresponding menu-driven tree with N-height satisfies the condition that f is one-to-one mapping from the set $\{\tilde{S}/\tilde{D}, \tilde{C}, \tilde{R}\}$ to each relation, $f(\tilde{S})$ . The total number of relations is $N + (N - 1)$ .

Proof. This is derived from Definitions 1, 2, and 3. Decision/Chance sets are unique. Thus they exist and are distinguishable. As for the R-Set, assume that we are able to make a relation for $R_{i}$ and $R_{j}$ sets, say, $R_{ij}$ ( $m_{i}, Ie_{i}, m_{j}, Ie_{j}, p_{j}, m_{k}, Ie_{k}, p_{k}$ ). The key is ( $m_{i}, Ie_{i}, m_{j}, Ie_{j}, m_{k}, Ie_{k}$ ). However, since $P_{k}$ depends upon the portion of the key,

relation DECISION 1 (ld $_{1}$ , d $_{11}$ , d $_{12}$ , ..., p $_{1}$ )
relation DECISION 2 (ld $_{2}$ , d $_{21}$ , d $_{22}$ , ...)
•
•
relation CHANCEm (lc $_{m}$ , C $_{m1}$ , C $_{m2}$ , ...)
•
•
relation CHANCEN (lc $_{N}$ , C $_{N1}$ , C $_{N2}$ ...)
•
•
relation RELATIONSHIP1 (m $_{1}$ , ld $_{1}$ , m $_{2}$ , ld $_{2}$ , p $_{2}$ )
•
•
relation RELATIONSHIP (N-1) (m $_{N-1}$ , ld $_{N-1}$ , m $_{N}$ , ld $_{N}$ , p $_{N}$ )
Fig. 7. Relational Schema.

$(m_{j}, Ie_{j}, m_{k}, Ie_{k})$ , this is in 1NF, not in 2NF causing some modification anomaly problems.

We would check if the underlying relational schema satisfies the lossless join property in order to be a proper schema. Relational algebraic operators in Ullman [35] are used for standardized notational convention. We also use the tree terminology without clarification.

Definition 8 (Proper Extension). Proper extension of one step, denoted $EX$ (a relation), is a sequential join of two adjacent relations in “properly established” set of relations. Proper extension of $n$ steps, denoted by $EX_{n}$ (a relation), is a sequential join of $n + 1$ consecutive relations. In another word, $EX$ ( $f(R_{i})$ ) is $f(R_{i-1}) \propto f(R_{i})$ . $EX_{n}(f(R_{i}))$ is $f(R_{i-n} \propto \ldots \propto f(R_{i-1}) \propto f(R_{i})$ , where $i$ is the sequential index for the R-Set's.

Proposition 2. In the R-Set relations, a parent relation is a subset (not necessarily proper subset) of the proper extension of the descendant relation: $f(R_{i-1}) \subseteq EX(f(R_i))$ . In other terms, $f(R_{i-1}) = \pi_{\tilde{k}} EX(f(R_i))$ . $\tilde{k}$ : associated columns for $R_{i-1}$ .

## A lemma is the following:

Lemma 1. The universal relation $(U)$ is obtainable from proper extension of $N - 2$ steps in a relational schema with $N - 1$ R-Set relations: $U = EX_{N - 2}(f(R_{N - 1}))$ .

Proof of Proposition 2 and Lemma 1. Let $I_n$ be any subset of an instance $I$ for this relational schema. To satisfy the lossless join property, It can be obtained from of $I$ through projection operation, namely, $I_n = \pi_{\bar{k}}(I)$ . If $f(R_{i-1}) \not\subseteq EX(f(R_i))$ , then since we are losing certain tuples in $EX(f(R_i))$ and $f(R_i)$ has its own unique tuples, $U = EX_{N-2}(f(R_{N-1})) = f(R_1) \infty f(R_2) \infty \ldots \infty f(R_{i-2}) \infty EX(f(R_i)) \infty f(R_{i+1}) \infty \ldots \infty F(R_{N-1})$ is lossy.

This proposition is significant since, even if the modified R-Set in Definition 5 is defined in terms of the previous set and the following set, the universal relation could be obtained by the sequential joining operation. This finding leads to the next proposition.

Proposition 3. If a series of decisions/chances are given up to any level, it is possible to retrieve the intermediate payoff (outcome) from the defined relational schema.

Proof. Let $U_{t}$ be the universal relation for that subtree involved in the series of decisions/chances. Since the proposition 2 suggests U is not lossy, $U_{t}$ is obtainable from $\tilde{\pi}_{k}(U)$ . $p_{t}$ is retrievable from $U_{t}(m_{1}, Ie_{1}, m_{2}, Ie_{2}, \ldots, m_{t}, I_{t}, p_{t})$ .

## 5. Discussion for a Simple Dialogue

In this section, we illustrate the use of the relational framework for a simple dialogue to show how to implement a dialogbase. The example dialogue has the following properties:

a. Three levels (Three D-Set's): $D_{1}, D_{2}, D_{3}$ (all decision sets).

b. Two elements in each level consisting of identifier and a non-identifier element: $E_1(Id_1, d_{11}, p_1), E_2(Id_2, d_{21}), E_3(Id_3, d_{31})$ .

c. Availability in each set is $2(a_{d}^{i} = 2)$ : $IE_{i}^{1}, IE_{i}^{2}$ .

![](/api/attachments/XVP79USW/fulltext/images/5a866513d3e4b1d0f4e37d87a14a41ff5a153abdbd44d3478d349195538ffc49.jpg)  
Fig. 8. Menu-driven Tree.

![](/api/attachments/XVP79USW/fulltext/images/91f499e660b6514a63ff44244614d491974b8b6577f81ac0be8087f3f3ae3d2c.jpg)  
Fig. 9. D-R Diagram.

The corresponding menu-driven tree is in fig. 8.

d. Two R-Set's: $R_{1}(m_{1}, Ie_{1}, m_{2}, Ie_{2}, p_{2}), R_{2}(m_{2}, Ie_{2}, m_{3}, Ie_{3}, p_{3})$ .

The modified D-R diagram will be fig. 9.

The corresponding relational schema with five relations is in fig. 10.

The instantiated relations of Relationship1 and Relationship2 are shown in fig. 11.

$f(R_{1})\subset EX(f(R_{2})) = f(R_{1})\infty f(R_{2})$ can be readily proven from the above instantiated relations. It is important to note that this is not always the case in a relational database.

One step proper extension $(n-2=3-2=1)$ of $f(R_{2})$ , $EX(f(R_{2}))$ , is, in fact, the universal relation. Given a series of decisions $(Id_{1}, Id_{2}, Id_{3})$ , the payoff (outcome) is immediately retrieved from $EX(f(R_{2}))$ . Only the series of decisions will be used as a key to retrieve the entire tuple information.

The highlight of this process is that a user only provides the series of decisions, whereas the DSMS operates on the join of $f(R_{1})$ and $f(R_{2})$ using the attributes m and Id.

relation DECISION1 $(\mathrm{Id}_1, \mathrm{d}_{11}, \mathrm{p}_1)$

relation DECISION2 (Id₂, d₂₁)

relation DECISION3 (Id₃, d₃₁)

relation RELATIONSHIP1 (m₁, ld₁, m₂, ld₂, p₂)

relation RELATIONSHIP2 (m₂, ld₂, m₃, ld₃, p₃)

Fig. 10. Relational Schema.

<table><tr><td> $m_{1}$ </td><td> $ld_{1}$ </td><td> $m_{2}$ </td><td> $ld_{2}$ </td><td> $p_{2}$ </td></tr><tr><td>1</td><td> $ld_{1}^{1}$ </td><td>1</td><td> $ld_{2}^{1}$ </td><td> $p_{2}^{1}$ </td></tr><tr><td>1</td><td> $ld_{1}^{1}$ </td><td>2</td><td> $ld_{2}^{2}$ </td><td> $p_{2}^{2}$ </td></tr><tr><td>1</td><td> $ld_{1}^{2}$ </td><td>1</td><td> $ld_{2}^{1}$ </td><td> $p_{2}^{3}$ </td></tr><tr><td>1</td><td> $ld_{1}^{2}$ </td><td>2</td><td> $ld_{2}^{2}$ </td><td> $p_{2}^{4}$ </td></tr></table>

Relationship1 (f(R₁))

<table><tr><td> $m_{2}$ </td><td> $ld_{2}$ </td><td> $m_{3}$ </td><td> $ld_{3}$ </td><td> $p_{3}$ </td></tr><tr><td>1</td><td> $ld_{2}^{1}$ </td><td>1</td><td> $ld_{3}^{1}$ </td><td> $p_{3}^{1}$ </td></tr><tr><td>1</td><td> $ld_{2}^{1}$ </td><td>1</td><td> $ld_{3}^{2}$ </td><td> $p_{3}^{2}$ </td></tr><tr><td>1</td><td> $ld_{2}^{2}$ </td><td>2</td><td> $ld_{3}^{1}$ </td><td> $p_{3}^{3}$ </td></tr><tr><td>1</td><td> $ld_{2}^{2}$ </td><td>2</td><td> $ld_{3}^{2}$ </td><td> $p_{3}^{4}$ </td></tr><tr><td>2</td><td> $ld_{2}^{1}$ </td><td>3</td><td> $ld_{3}^{1}$ </td><td> $p_{3}^{5}$ </td></tr><tr><td>2</td><td> $ld_{2}^{1}$ </td><td>3</td><td> $ld_{3}^{2}$ </td><td> $p_{3}^{6}$ </td></tr><tr><td>2</td><td> $ld_{2}^{2}$ </td><td>4</td><td> $ld_{3}^{1}$ </td><td> $p_{3}^{7}$ </td></tr><tr><td>2</td><td> $ld_{2}^{2}$ </td><td>4</td><td> $ld_{3}^{2}$ </td><td> $p_{3}^{8}$ </td></tr></table>

Relationship2 (f (R₂))  
Fig. 11. An Instance of Relationship1 and Relationship2.

## 6. Conclusion

We have introduced the concept of dialogbase to store a menu-driven dialogue and created a relational view of it. It is obvious that there are abundant advantages in doing this since a DSS is viewed in terms of three components and there have been some relational views of the other two components.

Some additional characteristics of the relational dialogbase organization should be considered. First, joining is unique. In relational database, any two relations may join together if needed. However, in relational dialogbase, it is not true since joining of R-Set relations can be done using two adjacent R-Set relations. Second, single tuple updating is not always guaranteed in relational dialogbase management. One single tuple updating may affect some other tuples in another relation. It results from the hierarchical property of a menu-driven tree. Third, there are some special operations such as optimization of choices, analysis of sensitivity by changing choice, and others in relational dialogbase management [33]. These operations could be handled by a query language which is not only relationally complete but computationally complete.

As for implementation, a menu-driven dialogue for a prototype example could be programmed and tested for the dialogue between the user and the system in comparison with a corresponding relational schema with a DBMS. A statistical test may be applied to compare the average time and the average errors of both cases to see statistically if either of the two methods is more effective and time-saving on a certain condition.

Finally, considering the ability of our concept to be generalized for other forms of dialogue may be worthwhile. Menu-driven dialogues are attractive in human factors standpoint $[29]$ and fit the relational concept quite well due to its nature of a distinct number of choices in each menu. We can generalize the idea to different forms of dialogue only when the numbers of commands (command node), or answers (Q/A style) are finite. I/O form may not fit our idea at all.

## References

[1] Alter, Steven L., Decision Support Systems-Current Practice and Continuing Challenges, Addison-Wesley, 1980.

[2] Ariav, Gad & Michael J. Ginzberg., “DSS Designing: A Systematic View of Decision Support,” Communications of the ACM, Vol. 28, October, 1985.

[3] Blanning, Robert W., "TQL: A Model Query Language Based On the Domain Relational Calculus," IEEE Workshop on Languages for Automation, November 7–9, 1983.

[4] Blanning, Robert W., "Issues in the Design of Relational Model Management Systems," AFIPS-Conference Proceedings, 1983.

[5] Blanning, Robert W., "A Relational Framework for Join Implementation in Model Management Systems," Decision Support Systems, Vol. 1, March, 1985.

[6] Bonczek, Robert H., C. Holsapple & A. Whinston, "The Evolving Roles of Models in Decision Support Systems," Decision Sciences, Vol. 11, No. 2, 1980.

[7] Bonczek, Robert H., C. Holsapple & A. Whinston, "A Generalized Decision Support Systems Using Predicate Calculus and Network Data Base," Operations Research, Vol. 29, No. 2, 1981.

[8] Buneman, O. Peter et al., “Display Facilities for DSS Support: The Daisy Approach”, Data Base, Vol. 8, No. 3, 1977.

[9] Carlson, Eric D., "An Approach for Designing Decision Support Systems," Data Base, Vol. 10, No. 3, 1979.

[10] Carlson, Eric D. et al., "The Design and Evaluation of an Interactive Geo-data Analysis and Display System," Information Processing, North-Holland Pub., 1974.

[11] Chen, Peter P., “The Entity-relationship Model-Toward a Unified View of Data,” ACM Transactions on Database System, 1976, Vol. 1, No. 1.

[12] Codd, E.F., “A Relational Model of Data for Large Shared Databanks,” Communications of the ACM, Vol. 13, No. 6, June, 1970.

[13] Date, C.J., An Introduction to Database Systems, 3rd Ed. Addison-Wesley, 1982.

[14] Davis, Randall, "A DSS for Diagnosis and Therapy," Database, Vol. 8, No. 3, 1977.

[15] Donovan, John J., "Database System Approach to Management Decision Support," ACM Transaction on Database System, Vol. 1, No. 4, 1976.

[16] Eason, K.D., "Understanding the Naive Computer User," The Computer Journal, Vol. 19, No. 1, February 1976.

[17] Fagin, Ronald, “A Normal Form for Relational Databases that is based on Domains and Keys,” Transactions on Database Systems, Vol. 6, No. 3, 1981.

[18] Kent, William, "A Simple Guide to Five Normal Forms in Relation Database Theory," Communications of the ACM, February, Vol. 26, 1983.

[19] Kent, William, “Consequences of Assuming a Universal Relation,” ACM Transactions on Database System, Vol. 6, No. 4, Dec. 1981.

[20] Kim, Won, “Relational Database Systems,” Computing Surveys, Vol. 11, No. 3, 1979.

[21] Konsynski, Benn R., "On the Structure of a Generalized

Model Management System," Proceedings of the Hawaii International Conference on Systems, 1981.

[22] Lee, Sang M. & Lori Sharp Franz, "An Interactive Decision Support System for Solving Multiple Objective Problems," Working Paper, 1983.

[23] Little, John D.C., “Models and Managers: The Concept of a Decision Calculus,” Management Science, Vol. 16, April, 1970.

[24] Lusk, Ewing L. & Ross A. Overbeek, "A DML for Entity-Relationship Models," International Conference on ERA, 1980.

[25] McGee, William C., “On User Criteria for Data Model Evaluation,” ACM Transactions on Database Systems, Vol. 1, 1976.

[26] Moreland, D. Verne, "Human Factors Guidelines for Terminal Interface Design," Communications of the ACM, Vol. 26, 1983.

[27] Ng, P.A. & J.F. Paul, "A Formal Definition of Entity-relationship Models," Proceedings of International Conference on Entity-relationship Approach, 1980.

[28] Perry, Robert, “Relational DBMS takes off,” Computer Decisions, February, 1985.

[29] Shneiderman, Ben, Designing the User Interface, Addison-Wesley, 1987.

[30] Sprague, Ralph H. & Hugh J. Watson, "Model Management in MIS," 7th Annual Meeting of the AIDS, Cincinnati, Ohio, 1975.

[31] Sprague, Ralph H. & Eric D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, 1982.

[32] Suh, Eui-Ho, “A Relational Framework for Interaction-base Management in Three-component Decision Support System,” Unpublished Ph.D. Thesis, University of Illinois at Urbana-Champaign, 1987.

[33] Suh, Eui-Ho, “Management of Relational Database for Menu-driven Dialogue,” Proceedings of the 1987 Annual Meeting of the Decision Sciences Institute, Boston, Massachusetts, 1987.

[34] Turban, Efraim, “Decision Support System (DSS): A New Frontier for Industrial Engineering,” Computers & Industrial Engineering, Vol. 7, No. 1, 1983.

[35] Ullman, Jeffrey D., Principles of Database Systems, Computer Science Press, 2nd Ed., 1982.

[36] Wong, E. & R.H. Katz, "Logical Design and Schema Conversion for Relational and DBTG Database," Proceedings of International Conference on Entity-relationship Approach, 1980.

[37] Zahedi, Fateweh, “Database Management System Evaluation and Selection Decisions,” Decision Sciences, Vol. 16, 1985.

[38] Zloof, M.M., "Query By Example," Proceedings of the National Computer Conference, 1975, AFIPS Press, Montvale, N.J., 1975.
