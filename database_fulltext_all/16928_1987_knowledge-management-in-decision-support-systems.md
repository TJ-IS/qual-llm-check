---
otero_id: 16928
otero_key: "JETB9S3D"
title: "Knowledge management in decision support systems"
authors: "Sheldon Shen"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90031-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge Management in Decision Support Systems

Sheldon SHEN

The Ohio State University, Columbus, OH 43210, USA

This paper discusses a framework for knowledge management in a DSS. We assume decision making is based mainly on numerical data processing. Thus, we abstract data and knowledge as relations, and decision models as relators. Based on these two constructs, our framework allows a user to compose and experiment decision models interactively; it also provides decision information nonprocedurally through a knowledge processor.

Keywords: Decision Support Systems, Database Management, Relations, Frames, Knowledge Processing, Rules, Virtual Databases, Artificial Intelligence.

![](/api/attachments/JETB9S3D/fulltext/images/5f73edff41923cf7694f01e829afa6a9307b87d252bd90e13594f7bbd7f78cd8.jpg)

Sheldon Shen received the B.S. degree in Physics from the National Tsing-Hua University, 1973; MBA in International Business from the University of South Carolina, 1978; Ph.D. in Management Information Systems from Purdue University, 1981.

work, artificial intelligence.

He is an Assistant Professor in Accounting and MIS, and in Computer Science at The Ohio State University. His research interests are management information systems, database management, local area net-

## 1. Introduction

Several approaches have been proposed in the literature for design of Decision Support Systems (DSS): the system approach, for example, emphasized the environment, components, resources, and their structural relationships of a DSS [2]; the cognitive approach, on the other hand, examined the nature and different types of decision situations related to a DSS [11,18], and the functional approach investigated tools, components, and technologies required by a DSS [6,7].

In the functional approach, a DSS is considered as a set of generalized software tools for building decision supporting information including data and models. The components of a DSS are then characterized as database management, knowledge or model management, and dialogue or user interface management [2,6,7,23]. Database management in a DSS is used primarily for storing and retrieving data; model management for representing decision models to analyze and process data, and dialogue management for providing nontechnical users an easy access to the system.

As an example, suppose a decision requires supports from statistical analysis on sample data. Then in the functional approach, a DSS would include a database to store sample data, and a knowledge base to represent statistical ‘knowledge’ or models. Upon receiving a query request (via some user interface), the system retrieves data from the database, performs data analysis, displays results, and if challenged by a user, also justifies its decisions. All these activities are executed automatically by the system.

Among the three components, database management has been extensively studied and many database models have been proposed. A comparison of the three popular models: network, hierarchical, and relational, can be found in $[15,25]$ . The relational database model, because it is conceptually simple and theoretically sound, has become the most popular; consequently, it is also the primary database management system in DSS's.

User interface management is a relatively new research area; yet impressive progress has been made in recent years. First, a query language is declarative rather than procedural, meaning that a user can request information in terms of what he wants rather than how he wants. Second, because of research in office automation, a user can now use a mouse, a voice interface, a micro pad, finger-touch, icons, menus, and high resolution graphic displays to interact with a system. These facilities enable a user to execute commands by pointing rather than writing or composing commands.

Knowledge management, on the other hand, is the least understood component in a DSS, although it is of critical importance for the success of a DSS. The obvious argument is that there is no suitable mechanism for representing decision models. There are, however, more fundamental reasons for lacking of a suitable mechanism: (1) decision knowledge is difficult to define or conceptualize, and (2) so far no one has postulated a theoretically correct decision model for all applications.

The remedy for the first seems to restrict the application domain of a DSS: if the domain of a DSS is too broad, then knowledge representation becomes too complex; if the domain is too narrow, knowledge representation can be managed, but then the DSS might not be very useful. A carefully chosen domain thus is critical in the design of a DSS. The remedy for the second is to abandon fixed, 'built-in' decision models and require a DSS to provide an easy, flexible means for the user to compose decision models at his will. Thus, a user can at least experiment with different hypothetical decisions, when no built-in model in the system is satisfactory. Based on these observations, we make the following assumptions in this paper:

(1) we assume decision models to be represented in a knowledge base are numerical analysis models, and

(2) we assume decision models or decision making processes are unknown when a system is designed.

The first assumption enables us to use a simple construct, called relations, to represent data. Notice that if decision models require symbol processing, rather than numerical analysis, then lists in LISP or production rules [20] in Artificial Intelligence are a better choice as a basic construct. Furthermore, if both symbol processing and numerical analysis are required, then frames [5,8,24] are a better construct. But, as discussed earlier, we need to restrict application domains to simplify model constructions. General constructs like frames are not suitable for constructing decision models, as will be discussed in the next section.

The second assumption motives another construct, called relators, to allow the system to compose or construct decision models at users' requests at run time. In the following, we will focus on the representation issue of numerical decision models, based on relations and relators.

## 2. Background

Although there are many ways to build computer software for decision support systems, none of them by themselves are suitable or satisfactory. This section briefly reviews strengths and weaknesses of Database Management, Virtual Databases, Programming Languages, and Artificial Intelligence in DSS applications.

## 2.1. Database Management

The basic notion in the relational model is that data can be represented as a two-dimensional table called a relation. Data retrieval can then be made very simple: in fact, three primitive operations - Select, Join, and Projection - are all it requires to retrieve any data. In actual practice, the query language is further simplified to be nonprocedural, meaning that a user does not have to know how these operations are combined to retrieve data [25].

Since database management has been fully developed and a powerful database interface does exist for data storage and retrieval, it is possible and sometimes attempting to use database management for knowledge management. For example, in the previous problem where a decision requires statistical analysis on sample data, a database approach would put sample data, means, variances, and other statistical information all in the database. Thus, upon a query request, the means and variances can be retrieved directly from the database to support decisions.

This approach is certainly simple and straightforward, but several criticisms may be leveled against it:

(1) There are many and varied decision models; it is impossible to specify a database that supports a wide range of possible decisions. For example, there could be many different statistical models, and consequently, many different means and variances.

(2) Even if all possible models can be predicted, storing all the data for these uses in a database introduces redundancies and thus creates insertion, deletion, and update anomalies [25]. In the above example, data and their means and variances are redundant in a sense that means and variances can be derived from data. Redundancies in a database may at times expedite query processing, but in general they add difficulties in maintaining the overall integrity of the database. For example, if data need to be modified then means and variances need also to be corrected; otherwise, inconsistency of data arises.

(3) In the above example, raw data are clearly important, but so are the means and variances. if redundancies are to be avoided, a database approach will have difficulty to decide which should be included in the database.

Clearly, mixing decision information (e.g., means and variances) with raw data results an inadequate DSS which not only has redundancies but also requires constant remodeling when decision models change. Database management alone therefore is not suitable for knowledge management.

## 2.2. Virtual Databases

Part of the problems in the above can be resolved by using the Virtual Database approach [21]. In this approach, data are modeled as relations, as in the relational database model. But unlike the relational database model, a relation in a virtual database needs not to have actual data stored in the physical database, and is thus called a virtual relation. Because no actual data are stored for virtual relations, redundancies can be avoided.

A virtual relation therefore is particularly useful for representing derived information such as means and variances. To obtain means and variances, data processing routines that can be called at run time are predefined and stored in the system library. Upon a query request, the system then calls the routines to generate derived information to support decisions.

Notice that virtual relations are also part of the conceptual database and can be used in a query directly (see, for example, virtual query processing in [21]). Virtual relations thus improve database management in several ways: (1) data redundancies are reduced, (2) data processing is integrated into database management, and (3) nonprocedural query languages can still be maintained, because the data in virtual relations are created by the system automatically [21].

The problem of using virtual database for knowledge management is that data processing routines must be predefined and stored in the system program library. Thus, system designers in fact must anticipate users' decision models in advance to be able to code them in the system library. When decision models are not prestored in the system, there is no simple mechanism, other than programming languages, in a virtual database for a user to construct decision models.

## 2.3. Programming Languages

Programming seems natural and straightforward for organizing data processing routines and decision models required in a DSS. Based on sound software engineering principles, we can write programs consisting of modular procedures with their parameters to be substituted at run time. Since the decision making process is not known in advance, these procedures must be implemented in a way that they can handle a variety of parameters to anticipate different decision requirements. To use such a system, a user mixes a database query language with a programming language: the query language is used for retrieving data from the database; the programming language is used for declaring data types, converting data suitable for these procedures, and finally calling these procedures. Obviously, mixing two languages has many disadvantages: for example, the program semantics is not clear, combination of procedures relies on a complex parameter passing machinery, modular design is difficult to accomplish due to unknown decision models, the complex programming syntax complicates knowledge modifications, automated problem solving is difficult to achieve, and furthermore, the complexity of such a system makes design of a friendly user interface almost an impossible task.

## 2.4. Artificial Intelligence

Admittedly, no other techniques are as powerful as Artificial Intelligence today for building DSS's: in A.I., a system designer can concentrate on modelling or representing knowledge of a problem and is freed from programming details.

There are several techniques for modeling knowledge (e.g., predicates [20], semantic networks [14], frames [5,8,24]). Only predicate calculus has been suggested for knowledge management in a DSS [6,7,9], although it has been widely criticized for lacking the expressive power to represent complex objects [10]. Today, the most powerful construct for representing knowledge is considered as the frames [5,8], and the best currently available means for capturing experts' problem solving knowledge is the rule-based approach [12,13,22]. Frames and rules are autonomous constructs and can be used independently; many systems, however, do adopt both and become highly powerful hybrid knowledge representation systems [1,17,24].

A frame is a structured representation of an object. The frame-based languages are powerful because they provide various constructs for organizing frames into taxonomies. For example, a frame can be a member of a class of frames, and a class can be a subclass of other classes. Special deduction algorithms are developed to exploit these taxonomic relationships of frames to perform inferences (e.g., properties of a class are inherited by its subclasses). Another automatic inference is constraints checking, where values of a slot or field of a frame are automatically checked to maintain overall semantic integrity (e.g., Week-regular-work-hours must be less than 40). In addition, procedures called active values and methods can be attached to a slot: active values are procedures automatically evoked to update other frames when values in some slot are updated; methods are procedures to be called by other frames [10].

A rule, on the other hand, is a 'if CONDITIONS then X' construct, which means if CONDITIONS are true, then X is inferred if X is a conclusion, or X is taken if X is an action. The rule-based approach is important in knowledge engineering because: (1) it effectively emulates reasoning characteristic of experts, (2) knowledge can be incrementally added or modified, since each rule represents a modular unit of knowledge, (3) the system is capable of explaining its reasoning process [13].

Notice that frames are useful in problems where knowledge processing is classificatory in nature. If knowledge processing requires data processing, then the frame-based languages use the concepts of active values and methods. But implementing active values and method generally require knowledge about LISP and thus they are low level constructs from a user point of view. Thus, although the frame-based languages are powerful for knowledge representation, they are suitable for knowledge system designers rather than end users.

## 3. Knowledge Organization

The objective of this paper is to discuss a knowledge base for organizing knowledge of numerical analysis in a decision supporting system. In our framework, a knowledge base includes data, data processing routines, and a problem solving mechanism. We will use relations to represent data and relators to represent data processing routines. There terms are explained in this section.

A relation is an aggregation of attributes. It includes a relation schema to define the attributes and actual instances or occurrences related to that relation. The actual occurrences associated with a relation is called the model of that relation, a term used in logic. A model of a relation should be distinguished from a decision model: the former consists of data associated with a relation, and the latter consists of data processing routines to generate decision making information. In a DSS, the model of a relation can be obtained in two ways: First, if the model is stored in the database, then it can be retrieved by the database, using the existing database interface. Second, if the model is not in the database, then it can be created by the knowledge base, using the data processing routines. The purpose of a knowledge base, therefore, is to store these routines to instantiate models of various relations for decision making.

To instantiate a relation, a knowledge base relies on a set of data processing routines and a problem solving mechanism to control and execute these routines: together they process data and create models of relations. Since system designers cannot foresee and store decision models, it is important that the system provide routines for the users to compose decision models. Furthermore, the synthesis of routines to become a decision model should not require a user to recourse to programming languages. In this paper, we propose primitive routines called relators.

Specifically, a relator is a procedure to process a relation. But unlike a procedure defined in a programming language, the application of a relator requires no variable declarations and therefore a user does not need to know complex parameter passing mechanisms such as passing by values or passing by addresses. In fact, the use of relators does not require a programming language, although they can also be used in a language. An example of a relator is SORT, which can be used to process a structured file directly without a programming language. In other words, a relator is like a command operator that can be directly operate on its operands, namely, relations. In contrast, to use a procedure in a programming language, we generally need to declare variables, pass variables by values or by addresses, and also adhere to the syntax of a language.

The other examples of relators are Select, Join, and Project: three relational operators in the relational database model. Notice that relators can also be combined to create higher level relators. For example, in database management, a data retrieval operator can be defined by combination of Select, Join, and Project.

Design of routines which can be easily synthesized to become a high level routine is, of course, not new in the programming circle. Backus, for example, has long advocated a programming style called functional programming [3]; in operating systems, much of the success of UNIX can be at least attributed to easy combination of basic utility programs [26]; in database management, the query language is achieved by the three basic operations: Select, Join, and Project, which can be arbitrarily combined to operate on any relation to yield the desirable effect of data retrieval. Notice that synthesizing routines without recourse to programming (and therefore no variable declarations and parameter passings from the users) is possible only if there is a uniform basic object to be applied in all the applications: for example, in Backus's functional programming, the basic object is a list, a UNIX operating system, a sequential file of bytes, and in database management, a relation.

Advantages of using relators, compared to traditional programming procedures, to implement decision models are considerable:

(1) Its semantics is clear: there is no need to declare variables and therefore no state transitions involved to obscure the meaning of a program.

(2) There is no arguments named in the relators; thus, they are completely general and can be applied to any relation without procedure declarations and parameter passing mechanisms.

(3) Combination of these operations is simple and hierarchical.

Fig. 1 is an example in which the programming approach and the relator approach are compared to retrieve data from a relation. Notice that the example and the program are all oversimplified. Yet it is clear that variable declarations and parameter passing between procedures tend to obscure the meaning of a program. When a program gets larger, the program codes would become even more complex. The composition of the relators, in contrast, is conceptually simple, functionally powerful, and yet elegant in style.

```prolog
STUDENT(Name, Address, Major, So-S-No, Tel)
1. Use relators to retrieve John's address:
OPEN STUDENT
Select(Name = John)
Project(Address)
2. Use the programming approach to retrieve John's address:
Variable x: record of STUDENT;
y: array of char;
Procedure Find(Filename: file, Key: array of char);
Main
OPEN STUDENT;
x := Find(STUDENT, John);
y := x.Address;
END
```

We can now formalize a knowledge base, which consists of:

(1) a set of relations,

(2) a set of primitive relators.

## 3.1. Relations

A relation schema $R = (A, K)$ is an ordered pair consisting of a finite set of attributes $A\{A1, A2, \ldots, An\}$ , and a finite nonempty set of key attributes $K = \{K1, K2, \ldots, Kn\}$ , where $K \subset A$ . The values for the attributes come from a set $D$ of domains, $D = \{D1, D2, \ldots, Di\}$ , each $Di$ being any nonempty set. We let $\cup D$ denote the union of these domains, that is, $\cup D = D1 \cup D2 \cup \ldots \cup Di$ . To relate the attributes with their domain, we assume that $S$ is the set of all the attributes, and that there is a function DOM: $S \dashrightarrow D$ which maps each attribute onto its corresponding domain, that is, $\text{DOM}(Ai)$ is the domain of the attribute $Ai$ . We say that a relation $r$ on a relation schema $R = (A, K)$ is a finite set of mappings $\{r1, r2, \ldots, rn\}$ , where each $ri$ is a function from $A$ to $\cup D$ such that $ri(Aj) \in \text{DOM}(Aj)$ for all $ri \in r$ and $Aj \in A$ , and for any distinct tuples $ri$ and $rj$ in $r$ , $ri(K) \neq rj(K)$ .

For a relation $r$ on $R = (A, K)$ , if $X \subset A$ and $ri \in r$ , by $ri(X)$ we mean the restriction of $ri$ to $X$ and we call $ri(X)$ an instance or occurrence of $X$ in $r$ . We sometimes use the notation $r(R)$ to mean $r(A)$ , that is, we use the name of the schema, $R$ , to stand for the set, $A$ , of all its attributes. We call $r(R)$ the model of $R$ , and $r(Ai)$ , the model of $Ai$ .

A relation in a knowledge base can be interpreted in three ways:

(1) If a relation can be instantiated from the database, i.e., all its data or occurrences are stored in the database, then this relation represents a set of data. In this case, set theoretic operations such as union and intersection can be applied to relations.

Example: Let CIS470(Student, So-S-No) and CIS530(Student, So-S-No) be two relations representing students enrolled in CIS470 and CIS530 respectively. Then CIS470 ∩ CIS530 represents the students enrolled in both classes.

<table><tr><td colspan="5">CIS570(Name, Midterm, Final) STUDENT(Name, So-S-No,</td></tr><tr><td>SA</td><td>63.5</td><td>74</td><td>SA</td><td>123456789</td></tr><tr><td>SBV</td><td>58</td><td>86</td><td>SB</td><td>111111111</td></tr><tr><td>SC</td><td>75</td><td>88</td><td>SC</td><td>222222222</td></tr></table>

Fig. 2.

(2) If part of all the data for a relation cannot be found in the database, then data processing is required to instantiate this relation. In this case, a relation represents a virtual relation which needs relators to instantiate unknown models.

Example: Let SCORE(Student, Course, Midterm, Final, Average) be a relation where Average is not part of the database. In this case, SCORE needs a procedure to retrieve Student, Course, Midterm, and Final from the database and then calculate Average.

(3) A relation represents a predicate. Depending on the results from the database and/or data processing operations, a true or false value can be assigned to a relation. Also, as a predicate, a relation can be defined by other relations using logical expressions.

Example: We can define SCORE(Student, CIS430, Midterm, Final, Average > 80) --> GRADE(Student, Course, A), meaning that in CIS430, if Average is greater than 80, then the grade is an A.

## 3.2.Relators

Suppose relations $R1 = (A1, K1), \ldots, Rn = (An, Kn)$ are in a database $DB$ , and a decision to be made is based on $R = (B, k)$ , which is not in $DB$ , but can be derived from $DB$ . We call the conversion from $R1, \ldots, Rn$ to $R$ a decision model, and use $O(.)::[R1, \ldots, Rn] \to R$ to denote that $R$ is created by $O$ from $R1, \ldots, Rn$ , where $O$ is a relator and (.) is an abbreviation of parameters in $O$ .

Since relators can be combined to create higher level relators, we need only to discuss primitive relators. There are two type of primitive relators: one type, called E-relators, creates a relation by extracting data from existing relations, and the other, called P-relators, by processing data from

Notations:

R: the name of a relation.

ri: an occurrence or tuple of R.

$r(R)$ : the model of R.

Ai: the name of a data item or field in a relation.

$f\langle ri\rangle(Ai,\ldots,Aj)$ : an algebraic expression, or a mathematical function $f$ which operates on an occurrence of $Ai,\ldots,Aj$ in $R$ . $f\langle r\rangle(Ai)$ : a mathematical function $f$ which operates on the model of $Ai$ .

Fig. 3.

existing relations. Existing relations, of course, are not necessarily in the database, since they can be temporarily created in the working memory by other relators. In the following, we assume there are two relations in the database (Fig. 2). Also, the notations used are summarized in Fig. 3.

## 3.2.1. E-relators

E-relators extract data from relations; thus operators in the relational database management systems can be used. We review some of them here, based on our notations.

(1) SELECT(C)::[R-->R']
/\* SELECT occurrences in R where a condition C is satisfied \*/
Example: SELECT(Final > 70)::[CIS570-->CIS570']
Results: CIS570' (Name, Midterm, Final)
SA 63.5 74

(2) JOIN(C)::[R1, R2-->R3]
/\* JOIN R1, R2 based on a condition C \*/
Example: JOIN(CIS570.Name = Student.
Name)::[CIS570, STUDENT-->R]
Results:
R(Name, Midterm, Final, So-S-No, Major)
SA 63.54 74 123456789 CIS
SB 58 86 111111111 EE
SC 75 88 222222222 Math.

(3) PROJECT(Ai, ..., Aj)::[R--→R']
/\* PROJECT R on fields Ai, ..., Aj \*/
Example: PROJECT(Midterm)::[CIS570--→R]
Results: R(Midterm)
63.5
58
75

(4) SORT(A, Ki, ..., Kj)::[R-->R'] /\* SORT R on keys Ki, ..., Kj in an ascending order \*/

/\* A replaced by D means in a descending order \*/

Example: SORT(A, Midterm)::CIS570-->R]

<table><tr><td colspan="3">Results: R(Name, Midterm, Final)</td></tr><tr><td>SA</td><td>63.5</td><td>74</td></tr><tr><td>SB</td><td>58</td><td>86</td></tr><tr><td>SC</td><td>75</td><td>88</td></tr></table>

(5) PARTITION(m, n)::[R-->R']  
/\* Partition the occurrences in R in m groups, and select the nth group. When exact partition is not possible, the system rounds off the numbers in a partition. \*/  
Example: Partition(3,1)::[CIS570-->R]  
Results: R(Name, Midterm, Final)  
SA 63.5 74

(6) Append::[R1,..., Rn-->R]
/\* Occurrences in R1,..., Rn are attached together and put in R, assuming R1,..., Rn have the same number of attributes of the same data types. \*/

These six relations give the basic operations to extract and rearrange data in existing relations. Other useful E-relators are DIFFERENCE and DIVISION in the relational database models [25]. We will not discuss them here, since they can be implemented by the other relators.

## 3.2.2. $P$ -relators

Given a relation $R = (A, K1)$ , a new relation $ER' = (B, K2)$ can be created by executing some numerical oriented data processing routines. Some routines require only simple algebraic operations such as addition, subtraction, multiplication, and division; others require complex numerical analysis. Most systems, however, provide, for example, trigonometric functions, present value calculations, and other basic functions. Functions, just like relators, can be easily combined into high level functions, if they are implemented to operate on one object only (e.g., lists) [3]. In this paper, we assume basic functions operating on lists are available to be used by P-relators.

To crease $R'$ , we use $ri(Bi) = f\langle ri\rangle(Ai, \ldots, Aj)$ and $ri(Bi) = f\langle r\rangle(Ak)$ to represent two ways that an occurrence of $Bi$ can be created from $R$ . In the former case, $ri(Bi) = f\langle ri\rangle(Ai, \ldots, Aj)$ , an occurrence of $Bi$ is created by applying a list-processing function $f$ on $ri(Ai, \ldots, Aj)$ , an instance of $Ai, \ldots, Aj$ in $r$ . In the latter case, $r(Bi) = f\langle r\rangle(Ak)$ , an occurrence of $Bi$ is created by applying $f$ to $r(Ak)$ , the entire model of $Ak$ . Notice that $ri(Ai, \ldots, Aj)$ and $r(Ak)$ all represent a list of data: the elements of $ri(Ai, \ldots, Aj)$ are from different attributes while the elements of $r(Ak)$ are from the same attribute.

## Examples:

Assume SUM, COUNT, MIN, MAX are functions in the system library, then:

SUM $\langle ri\rangle(Ai,\ldots,Aj)$ computes the sum of an occurrence of $Ai,\ldots,Aj$ in R.

COUNT $\langle r\rangle(Ai)$ counts the number of occurrences in the model of Ai in R.

MIN $\langle r\rangle(Ai)$ finds the minimum of the model of Ai in R.

MAX $\langle r\rangle(Ai)$ finds the maximum of the model of Ai in R.

Thus, functions are applied to either tuples or models of attributes. To call these functions, we have two P-relators: ADDF and ADDR. In the following, $r\langle ri\rangle$ is abbreviated as f in ADDF, since functions called by ADDF apply to tuples only. Similarly, $f\langle r\rangle$ is abbreviated as f in ADDR, for it applies to models only.

(1) ADDF(Ak = f(Ai, ..., Aj))::[R--→R'] /\*ADDF adds a field Ak in R where Ak = f(Ai, ..., Aj) \*/

Example: ADDF(Average = (Midterm + Final)/2)) [CIS570-->R]

Results: R(Name, Midterm, Final, Average)

$$
\begin{array}{c c c c} \text {SA} & 6 3. 5 & 7 4 & 6 8. 7 5 \\ \text {SB} & 5 8 & 8 6 & 7 2 \\ \text {SC} & 7 5 & 8 8 & 8 1. 5 \end{array}
$$

(2) $\mathbf{ADDR}(Bi = f(Ai),\ldots ,Bj = f'(Aj))[R\dashrightarrow R']$ /\* ADDR creates a relation $R^{\prime}$ from $R,Bi$ in $R^{\prime}$ is created from the model of $Ai$ in $R$ by f, and BVj in $R'$ is created from the model of Aj in R by $f'$ . \*/
Example: ADDR((Mid-Ave = (SUM-(Mid-term))/(COUNT(Midterm))):[CIS570-->CLASS\_AVE]
Results: CLASS\_AVE(Mid-Ave)
65.5

## 4. Problem Solving

The purpose of a knowledge base in a DSS is to capture experts' problem solving knowledge. This section demonstrates how relators can be used in constructing a knowledge base. We assume the above basic relators are implemented as primitive commands in a DSS, just like Select, Join, and Project being part of database management system primitives.

Assume a database contains a relation: SCORES(CLASS, STUDENT\_NAME, MIDTERM, FINAL), which stores students' examination scores in each class. To determine a student's academic performance in each class, examination scores alone are not sufficient. In general, a grade in a class is determined by a grading policy, based on the average examination scores and the grade distribution in that class. A general grading program suitable for all the instructors, however, is difficult to construct, as each instructor would like to make his grade decisions based on his own grading policy. Thus, while each individual grading program seems easy enough, there are, unfortunately, infinite number of them to be included in a general program.

Example 1: Four grades “A”, “B”, “C”, and “D” are evenly given in the CIS570 class, depending on the distribution of the average. The average is computed as Average = (Midterm + 2Final)/3.

Example 2: Four grades “A”, “B”, “C”, and “D” are given to CIS670. Students with their averages greater than the class average get at least a “B”. Among them, the upper half get “A’s”. For students below the class average, half of them get “C’s”, and the other half, “D’s”. The average is (Midterm + Final)/2.

```rust
1. SELECT(CLASS = "CIS670")::[SCORES--> CIS670]
```

```txt
2. ADDF(Average = (Midterm + Final)/2)::CIS670-->CIS670']
```

There are two ways relators can be used in constructing these grading decision models: first, relators are used interactively at the command level; second, relators are stored in a knowledge base to be processed by a query processor.

The following is an example where a user, at the system prompt, uses relators interactively to create CIS570\_GRADE to support his decisions.

```rust
1. SELECT(CLASS = "CIS570")::[SCORES--> CIS570]
2. ADDF(Average = (Midterm + 2Final)/3)):: [CIS570--> CIS570']
3. SORT(D, Average)::[CIS570'--> TEMP]
4. PARTITION(4,1)::[Temp--> GRADEA]
5. PARTITION(4,2)::[Temp--> GRADEB]
6. PARTITION(4,3)::[Temp--> GRADEC]
7. PARTITION(4,4)::[Temp--> GRADED]
8. ADDF(GRADE = "A")::[GRADEA--> CIS570A]
9. ADDF(GRADE = "B")::[GRADEB--> CIS570B]
10. ADDF(GRADE = "C")::[GRADEC--> CIS570C]
11. ADDF(GRADE = "D")::[GRADED--> CIS570D]
12. APPEND::[CIS570A, CIS570B, CIS570C, CIS570D--> CIS570_GRADE]
```

In the above, CIS570 is created first to derive CIS570', which contains the weighted average examination scores. CIS570' is then sorted by Average in a descending order to create TEMP. TEMP, in turn, is partitioned into four relations, with each relation attached a filed of "A", "B", "C", and "D", respectively. And finally, GRADEA, GRADEB, GRADEC, and GRADED are appended as CIS570\_GRADE, which consists of all CIS570 students and their grades. Similarly, for example 2, we have the following:

$$
\begin{array}{l} \text {3.ADDR(Class - ave = SUM(Average) / COUNT} \\ \text {(Average)::[CIS670^{\prime} \dashrightarrow} \\ \text {CLASSAVE]} \end{array}
$$

4. SELECT(Average > CLASSAVE.Class-ave):: [CIS670'-->GRADEAB]

5. SELECT(Average < CLASSAVE.Class-ave)):
[CIS670'-->GRADECD]

6. PARTITION(2,1)::[GRADEAB-->CIS670A]

7. PARTITION(2,2)::[GRADEAB-->CIS670B]

8. PARTITION(2,1)::[GRADECD-->CIS670C]

9. PARTITION(2,2)::[GRADECD-->CIS670D]

CIS670' is derived from CIS670 to include the weighted averages. A relation CLASSAVE is created with only one field, Class-ave and the occurrence of this field is the class average in the CIS670 class. Select relators in 4 and 5 select occurrences in CIS670' with Average greater than or equal to CLASS-ave for GRADEAB, and with Average less than Class-ave for GRADECD. GRADEAB is then partitioned to two groups, the first group has grade "A", and the second group, "B". Similarly, GRADECD is partitioned to GRADEC and GRADED.

Notice that an English-like language for using these relators is possible. For example, instead of $O(.)::[R1,\ldots,Rn\dashrightarrow R]$ , we can use "APPLY $O(.)$ FROM $R1,\ldots,Rn$ TO $R$ ".

The second possibility of using relators is to store the relators representing a decision model in a knowledge base. For example, twelve relators in the above example 1 constitute a decision model and are stored in the knowledge base. The following relations are then presented to users in the data dictionary:

SCORES(CLASS, STUDENT\_NAME, MIDTERM, FINAL)
CIS570(CLASS, STUDENT\_NAME, MIDTERM, FINAL)
CIS570'(CLASS, STUDENT\_NAME, MIDTERM, FINAL, AVERAGE)
CIS570A(CLASS, STUDENT\_NAME, MIDTERM, FINAL, AVERAGE, GRADE)
CIS570B(CLASS, STUDENT\_NAME, MIDTERM, FINAL, AVERAGE, GRADE)
CIS570C(CLASS, STUDENT\_NAME, MIDTERM, FINAL, AVERAGE, GRADE)
CIS570D(CLASS, STUDENT\_NAME, MIDTERM, FINAL, AVERAGE, GRADE)
CIS570\_GRADE(CLASS, STUDENT\_NAME, MIDTERM, FINAL, AVERAGE, GRADE)

Notice that except SCORES, the other relations are all virtual relations: they don't have actual occurrences in the database. To a user, however, there is no difference between a real relation and a virtual relation. He can still pose a query regardless of what a relation is. As an example, the following is a query to request student names who get "B" in CIS570:

SELECT STUDENT\_NAME FROM CIS570\_GRADE WHERE GRADE = "B". Upon this query request, the query processor first determines that a virtual relation is requested, and therefore passes controls to the knowledge processor. The knowledge processor looks up all the relators in the knowledge base and find CIS570\_GRADE in the APPEND relator. To apply APPEND to create CIS570\_GRADE, however, four relations CIS570A, CIS570B, CIS570C, and CIS570D are required. Therefore, the next step is to look up these four relations. The same backtrack reasoning applies to other relators, and eventually SCORES is found in the SELECT relator. Since SCORES can be obtained from the database, SELECT is applied to create CIS570. The instantiation of CIS570 then invokes ADDF, which in turn calls other relators, and finally CIS570\_GRADE is derived. Notice that the execution of the relators representing a decision model in a DSS is similar to the execution of data processing routines in virtual databases: in both cases, the objective is to construct a control sequence to instantiate (virtual) relations. Detail discussions on the generation of executable plans in query processing can be found in [21].

## 5. Conclusions

This paper discusses a framework for organizing decision models in a DSS. Decisions to be supported in this paper are assumed to be based on numerical data analysis. This assumption allows us to simplify knowledge representation, as one simple construct, called relations, is sufficient for representing both data and decisions. Furthermore, the representation of a decision model is also simplified, as it becomes essentially a sequence of operators to convert relations representing data to relations representing decisions.

We discussed two basic types of operators for manipulating and deriving relations: E-relators and P-relators. A user can use relators directly to compose and experiment different decision models, or alternatively, interacts with the system through a query processor, which retrieves and processes relators representing decision models from a knowledge base.

The applications of this framework are business problems where decisions are largely based on numbers: sales reports, income statements, inventories, etc. Decision models in these problems generally require these numbers to be aggregated, divided, and sometimes statistically analyzed. Our framework simplifies the construction of such decision models.

Three areas remain to be studied in the future research: (1) to organize a set of functions as a supporting layer for the P-relators, and (2) to integrate other knowledge processing (e.g., inferences based on taxonomies) in a DSS, and (3) from the practical point of view, a friendly user interface.

## References

[1] Aikins, J.S., A representation scheme using both frames and rules, in: B.G. Buchanan and E.H. Shortliffe, eds., Rule-based Expert Systems, Addison-Wesley, Reading, MA (1984) 424–3440.

[2] Ariav, G., and M.J. Ginzberg, DSS Design: A system view of decision support, CACM 28, No. 10 (Oct., 1985) 1054–1052.

[3] Backus, J., Can programming be liberated from the von Neumann style? A functional style and its algebra of programs, CACM 21, No. 8 (Aug., 1978) 613–641.

[4] Bennett, J.L., ed., Building Decision Support Systems, Addison-Wesley, Reading, MA (1983).

[5] Bobrow, D.G., and T. Winograd, An overview of KRL, a knowledge representation language, Cognitive Science 1,1 (Jan., 1977) 3–46.

[6] Bonczek, R.H., C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York (1981).

[7] Bonczek, R.H., C.W. Holsapple and A.B. Whinston, The Evolution from MIS to DSS: extension of data management to model management, in: M.J. Ginzberg, W.R. Reitman and E.A. Stohr, eds., Decision Support Systems, North-Holland, Amsterdam (1982) 61–78.

[8] Brachman, R.J., and J.G. Schmolze, An Overview of the KL-ONE Knowledge representation system, Cognitive Science 9,2 (April, 1985) 171–216.

[9] Dutta, A., and A. Basu, An artificial intelligence approach to model management in decision support systems, IEEE Computers (Sept., 1984) 89–97.

[10] Fikes, R., and T. Kehler, The role of frame-based representation in reasoning, CACM 28, No. 9 (Sept., 1985) 904–920.

[11] Gorry, G.A., and M.S. Scott-Morton, A Framework for management information systems, Sloan Management Review 13, 1 (Winter, 1971) 50–70.

[12] Hayes-Roth, F., D.A. Waterman and D.B. Lenat, Building Expert Systems, Addison-Wesley, Reading, MA (1983).

[13] Hayes-Roth, F., Rule based systems, CACM 28, No. 9 (Sept., 1985) 921–932.

[14] Hendrix, G.G., Encoding knowledge in partitioned networks, in: N.V. Finder, ed., Associative Networks: Representation and Use of Knowledge by Computers, Academic Press, New York (1979) 51–92.

[15] Holsapple, C., S. Shen and A. Whinston, Data base management, in: Gavriel Salvendy, eds., Handbook of Industrial Engineering, Wiley, New York (1982).

[16] Keen, P.G.W., Adaptive design for decision support systems, Data Base 12, 1–2 (Fall, 1980) 31–40.

[17] Kehler, T.P., and G.D. Clemenson, An application development system for expert systems, System Software 3,1 (Jan., 1984) 212–224.

[18] Little, J.D.C., Models and managers: The concept of division calculus, Management Science 16,8 (April, 1970) B466–B485.

[19] Moore, J.H. and M.G. Chang, Design of decision support systems, Data Base 12, 1–2 (Fall, 1980) 8–14.

[20] Nilsson, N.J., Principles of Artificial Intelligence, Tioga, Palo Alto, CA (9179).

[21] Shen, S., Design of virtual databases, Information Systems 1 (1985) 27–35.

[22] Shortliffe, E.H., Computer Based Medical Consultations: MYCIN, Elsevier (North-Holland), New York (1976).

[23] Sprague, R.H., Jr., and E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ (1982).

[24] Stefik, M., D.G. Bobrow, S. Mittal and L. Conway, Knowledge programming in LOOPS: report on an experimental course, Artificial Intelligence 4,3 (Fall, 1983) 3–14.

[25] Ullman, J.D., Principles of Database Systems, Computer Science Press, Potomac, MD (1980).

[26] UNIX Programmer's Manual, Vol. 1 & Vol. 2, Bell Laboratories, Murray Hill, NJ (1983).
