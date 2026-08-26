---
otero_id: 16948
otero_key: "XN5NGBYU"
title: "A modular user-oriented decision support for physical database design"
authors: "Dario Maio; Claudio Sartori; Maria Rita Scalas"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90074-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Modular User-Oriented Decision Support for Physical Database Design $^{1}$

Dario MAIO \*, Claudio SARTORI \*\*

and Maria Rita SCALAS \*

\* Dipartimento di Elettronica, Informatica e Sistemistica, Universita' di Bologna, Bologna, Italy and \*\* Centro di Studio per l'Interazione Operatore-Calcolatore, Consiglio Nazionale delle Ricerche, Italy

A decision support package for the design of indexes in a relational database environment is presented. It originates from the theoretical results collected inside the DATAID methodology. Its main features are a high level language user interface, an incremental description of the design environment, a forecasting of the execution I/O costs if the proposed solution is adopted and also a guidance for the access paths to be selected in the various operations.

Keywords: Relational databases, Physical design, Choice of indexes, High-level interface.

![](/api/attachments/XN5NGBYU/fulltext/images/267d78c063d4ee14d625343a27fd6936a2c4eb96e1b4d0cd345a36dfc8eadc21.jpg)

Dario Maio is Associate Professor at the Computer Science Department, University of Bologna, Italy. He has published in the fields of distributed computing systems, computer performance evaluation, database design and office information systems. Before joining the Computer Science Department, he received a fellowship from the CNR (Italian National Research Council) for the participation to the Air Traffic Control project. He received a degree in Electronic En

gineering from the University of Bologna in 1975.  
![](/api/attachments/XN5NGBYU/fulltext/images/c3f0bd1f99c7da3fdb901ed9b8dc14888f1fa096e7287240a83572b7ffc4c72e.jpg)

Claudio Sartori is Staff Scientist in the CNR (Italian National Research Council). He received a degree in Electronic Engineering from the University of Bologna in 1981. He has published in the fields of computer performance evaluation, database design and knowledge base design. Before joining the CNR he had a fellowship from the CNR for the participation to the automated database design project DATAID. His current research interests include data and knowledge base design and knowledge representation systems.

## 1. Introduction

In the last few years, database design has assumed remarkable interest owing to the increased popularity of general purpose DBMSs and consequently to the complexity of the applications involved. A joint five year project, called DATAID, supported by the Italian National Research Council, started in September 1979 with the participation of several working groups belonging both to the academic and the industrial environments. The aim of the project was mainly concerned with the definition of an automated methodology to assist the designer during the database development process, covering the user requirements specification, the conceptual modelling and the physical implementation [1, 6]. Inside the DATAID project we developed a set of tools which are able to provide practical guidance to the database administrator to make decisions and trade-offs, during the physical design phase. It must be remembered that in a relational DBMS environment, once the logical model has been derived, the physical design involves the choice of efficient access paths and ought to be followed by some performance prediction as a feed-back to the different project layers.

The aim of this paper is to describe the architecture and the main concepts of a modular user-oriented self-contained design decision support (DDS). DDS originates from the theoretical results and experimentations collected by means of IDEA (Index DEsign Algorithm) developed as the last step of the DATAID methodology for the relational environment [3,11]. Therefore, IDEA was not provided with a user interface, because its inputs were directly derived from the logical design tool.

![](/api/attachments/XN5NGBYU/fulltext/images/6f86108f44fa72e448076ff54e8a7d9a955e3135a89a3fafc46ff9dcd522ad89.jpg)  
research interests and experiences are on database management systems and in particular on relational database optimizers, join methods, access structures, database design and costs evaluations.

At the conclusion of the DATAID project, our effort was directed to extend the facilities offered by IDEA, designing a new stand alone tool which operates interactively in order to select an efficient set of access paths, taking into account the constraints imposed by the logical design and derived from the relational DBMS architecture. The new tool DDS contains IDEA and has been provided with a high level language user interface, allowing also an incremental description of the database subject to design and of the operations on it. The necessity of such a decision support is very strong, especially for the great number of database users who have at their disposal a commercial DBMS but not necessarily an integrated design tool. As an example we can mention Dbase III which supports the use of indexes but not their choice. In this situation DDS can be useful in the design of the indexes and application procedures.

Section 2 introduces a background for relational DB physical design, summarizing the previous practical results obtained during the DATAID project and focusing attention on the requirements for an autonomous design tool. Section 3 explains in detail the organization of the designer decision support in terms of the three major phases: dialog, design and choice. Section 4 describes the system usage and a working example. Section 5 deals with more issues on user interfaces.

## 2. Background

The first objective of our participation to the DATAID project was the individuation and selection of a target relational DBMS. The features of a target system must be general enough to permit the construction of a behavioural model, allowing the implementation of a design tool useful for several commercial systems. The following assumptions were made:

(1) Each relation may be accessed by using a sequential scan or by using only one of the indexes built on the relation itself.

(2) The indexes are structured as B + trees and the leaves contain all the key values, each followed by the set of tuple identifiers (TIDs) where the value appears [7]. Furthermore, an index cannot be built by using compound keys. At most one index per relation may be recognized by the system as clustered, that is, built on a sorted column [12]. As an alternative, inverted lists can also be considered. In the following we will always use the term index, indicating one of the two previously mentioned access structures.

(3) An index cannot be used to access tuples for an update statement that modifies the indexed column, since this way might lead to hitting the same tuple more than once [12].

(4) Joins are performed according to separable or approximately separable methods [4,5,15,16, 18], and in particular

(a) by using the nested loop,

(b) assigning the relations to each nesting level by following the same order as they are referenced in the specification of the operations.

(5) The optimizer estimates execution costs assuming uniform distributions, i.e.,

(a) distribution of column values: the values of each column are uniformly distributed over the relation tuples; furthermore, column values are uniformly distributed over the domain, (b) distribution of the tuples with a given column value over the relation pages; two cases are considered for a given relation:

(b1) sorted column: where it exists, a correspondence between data pages and column values is forced,

(b2) unsorted column: column values are assumed to be uniformly distributed over the relation tuples and, consequently, over the data pages.

These last assumptions are justified since monitoring and maintaining statistics are complex operations, except for those cases that are easily represented by well-known distributions.

The assumptions 1, 2, 3 and 5 meet the requirements of many of the actual systems. The assumption 4 does not fit those systems which use other join methods, as for example systems which adopt the TID intersection algorithm. Furthermore, the hypothesis 4b, suitable for most of the relational DBMSs, is justified because it constrains the system to access relations in the same order specified by the user, an order that is presumably significant for the application. In any case the major reason for this assumption is that the separability concept allows the design tool to univocally split a join into a group of statements which act on a single relation. This results in a considerable reduction in the complexity of the solution generation procedure, described in [6]. Similar considerations lead us to neglect, at this design level, any effect produced by the concurrence of the operations in a real time environment.

On the basis of these assumptions, IDEA was developed to help the designer to choose an optimal set of indexes, for a given relational schema. The new tool DDS improves IDEA, by including a high level language interface available for the definition of the relational schema and workload. DDS may be applied both for relational DBMSs reflecting the above assumptions and for those systems (i.e., Dbase III) which, even allowing indexes, do not offer automatic optimizing facilities. In this latter case DDS provides the user with a practical guide to performing the index selection, being able to describe a general cost model.

## 3. Organization of the Designer Decision Support

The Designer Decision Support (DDS) presented in this paper is oriented to the choice of the optimal access structure for a large relational database. Its decision process can be seen to be composed of three major phases: dialog, design and choice. As a last remark, inside the DATAID project we have studied the possibility of integrating the physical design tool with a performance prediction tool, in order to build an integrated layered model able to capture the effects on resource consumption, throughput and response times of the various logical and physical DB design decisions [10]. This facility has not yet been included in DDS.

The dialog phase includes the acquisition of all the relevant information on the specific database structure and its expected utilization. We will refer to this information as a design environment. During the life-time of a database, data reorganization can occur and new requirements can also arise and produce changes in the frequency distribution of the queries and/or the introduction of new queries. Therefore, in order to make these changes easier, it is necessary to provide a user-friendly information handler supporting the input to the DDS.

In the design phase all the possible access paths are examined and their effectiveness for the expected utilization is evaluated. In other words a cost model is applied in order to forecast the effects of each possible index design choice, in terms of execution times and memory occupation.

Finally the choice is performed comparing the various configurations of access structures, taking into account the user's requirements. Both the design and choice components of the DDS constitute IDEA, an automated tool described in [11] and [6]. In fig. 1 the overall schema of the DDS is given.

In the following we show the modular structure of the dialog phase, the user's demands that led us to choose such a structure and the integration with the existing module IDEA. The most outstanding features of IDEA will also be shown. For more details we refer to [11].

![](/api/attachments/XN5NGBYU/fulltext/images/7d5f13718401908eb52595c0774d7930ec0c98ce7ce05ce6310932374aa4919a.jpg)  
Fig. 1. DDS overall schema.

## 3.1. User Demands

First of all let us examine the information the user must provide as input to the DDS. It results from a preceding logical design and can be summed up as follows:

\- data structure description: for each table the relation cardinality, the tuple length, the physical page length and the filling factor are needed, and for each field of a relation the data type, the domain and the number of distinct values must also be provided [8,13,14,17],

\- workload description, defined as the collection of all the operations relevant to the design: this information can be part of the requirements specification directly supplied by the user [2], or can be deduced when the system is running, in the tuning phase, if a query monitor is available [9]; a weight is associated to each query, according to the relative frequency of the query itself during a significant observation period. The requirement of shorter response times on some queries and the consideration of particular execution bursts would need the use of performance evaluation techniques for a proper solution. Since, at present, the DDS does not include such a facility, these problems can find a partial solution by means of an adjustment of the weights for the critical queries.

The above information is very similar to that to be provided during the DB creation and manipulation. Therefore, for a rapid approach to the DDS, we chose for the user-system interface a language very close to the Data Definition and Data Manipulation Languages (DDL and DML) supported by DBMSs like System R. These languages are familiar to any DBMS user, and we think they can fulfil the requirements of simplicity and completeness.

Another requirement of the designer is to have the possibility of interrupting the working session at any moment. This feature was one of our leading aims during the design and development of the DSS because it enables the user to load the data structure and the workload description during distinct working sessions.

Moreover the resulting modularity of the structure can be used to fulfil the requirements of a dynamically growing database. In fact, often not all the relations and the queries are defined from the very beginning, but different levels of refinement are progressively introduced.

## 3.2. Working Session

In order to show how the DDS is modularized, we will first examine a working session from the functional point of view (Fig. 2).

![](/api/attachments/XN5NGBYU/fulltext/images/a7e720c4e39b13298cee4b26a103886bf4bbc3a8b4bf0b934f7a67ea034196dc.jpg)  
Fig. 2. Action flow in a DSS working session.

Two typical situations can be distinguished: new project definition or recall and modification of an old one. When the designer begins a new project a sequence of actions must be performed: the input of the dictionary and the workload. Both these operations can require corrections in case of error. Finally the design tool IDEA can be executed. At the end of each stage the working session can be stopped, saving the results of the operations performed. If the designer wants to work on an old environment, it is possible to separately recall an existing relational schema and a corresponding workload, or to directly execute IDEA if both already exist.

In general, before being allowed to perform any of the actions sketched in the boxes of fig. 2, it is necessary to define the working environment containing the information on the database project being processed. This can be done either by recalling an old environment, defined in a previous working session, or by initializing a new one. In addition, for an environment a processing state is defined, depending on whether both relations and queries, relations only or no data at all are available. The actions allowed at any time depend on the processing state of the current environment. Table 1 shows the actions that can be performed in any state.

## 3.3. Functions Description

Each action listed in table 1 corresponds to a function available for the DDS user. Let us now examine the features of each one.

Table 1
DDS functions. $^{a}$

<table><tr><td></td><td>No Data</td><td>Relations</td><td>Relations+ queries</td></tr><tr><td>1 Def. Env.</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>2 Crate R.</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>3 Modify R.</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>4 Create Q.</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>5 Modify Q.</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>6 Exe. Env.</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>7 Sav. Env.</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="4"> $^a$ Def. Env. = Definition of the current Environment,Create R. (Q.) = Create Relation (Query),Modify R. (Q.) = Modify Relation (Query),Exe. Env. = Execution of IDEA on the current Environment,Sav. Env. = Save the current Environment.</td></tr></table>

## 3.3.1. Definition of the Current Environment

With this action the user specifies the name of the environment he wants to work with. When this name refers to an old one the information (stored during previous working sessions) is loaded into the current environment. In other words, the associated description of the relations and, possibly, of the queries becomes available. If the name specified is a new one, an initialization is performed and the processing state becomes No Data. This action is necessary before going on with any other operation.

## 3.3.2. Creation of a Relation (Query)

The description of new relations (queries) is added to those (if any) concerning the current environment. As mentioned before, the description is effected in a high-level language. On the other hand the input to the automated tool IDEA requires transformation into an internal simplified form where both the dictionary and the workload are tabular structures and the queries are already decomposed into subqueries on the single relations [11]. Therefore this conversion is included in this module. The input procedure is designed to accept complete information units (relations and queries). These units are then translated separately: the syntactic and semantic analyses are performed and the internal form is generated. In case of error an explanatory message is notified and the wrong phrase is edited again until a valid definition is obtained. It must be noticed that the input of a query is allowed only if the descriptions of the referenced relations are already loaded, otherwise the semantic analysis of the query would not be possible.

## 3.3.3. Modification of Relations

Adding the description of a new relation is an intrinsic feature of the DDS, since the incremental definition of the dictionary in different working sessions is allowed and is obtained by the creation function. The modification facilities are the same as those generally allowed in a DBMS: deletion of an entire relation, adding and deletion of a field of a relation. The updating of the characteristics of a field can be easily obtained by means of a deletion and a successive adding.

## 3.3.4. Modification of Queries

The only modifications allowed are the adding (by the creation function), the deletion of queries and the change of the frequencies. The last one can become necessary when the weight of the query, with respect to the overall workload, changes.

## 3.3.5. Execution for the Current Environment

Once the database and workload description have been correctly loaded and transformed into the internal form, the execution of IDEA on these data can be requested. As previously mentioned this module includes both the design and choice phases.

In the design phase the estimation of the execution costs is effected by examining the workload derived from the decomposition into equivalent queries on single relations. For each query Q of the workload (on a relation R), the sequential access cost to R is computed; then, for each field of R, if there is in Q a selection predicate on the field, the data and index access costs are also evaluated. If the query implies modifications of R, that is an updating, deleting or inserting operation, the relation and index maintenance costs are also computed. So for each possible access path and for each query, two major cost functions are considered: I/O cost for retrieving relation tuples and for updating tuples and indexes (if requested). The expected effectiveness of an index is then computed by comparing its access cost with the sequential one, and by taking the updating cost as waste.

The choice phase takes, as input, the previous cost evaluations and chooses the set of indexes which globally maximizes the effectiveness for the entire workload, for imposed memory constraints.

## 3.3.6. Save the Current Environment

It is possible to save the description of the design environment on which the user is actually working. This feature enables the designer to use the information in future working sessions, in case of modifications or extensions of the current design environment.

![](/api/attachments/XN5NGBYU/fulltext/images/3650a33c8ab1f44f092ee5be3a14c027fa0e532df64bce512f6f9d432720c6e9.jpg)  
Fig. 3. Data flow in the dialog phase.

In fig. 3 the data flow in the dialog phase is shown.

## 4. A Working Example

In this paragraph a complete working session with DDS will be shown. Let us examine a portion of a conceptual schema taken from the banking environment. In this example we consider the customers of a bank, each customer having one or more contracts. Each contract has an address and is associated to a main contractor customer and, eventually, to many sub-contractors. Customers are initially inserted into the database as temporary customers and later can become definitive customers. Each definitive customer is classified as person or company and has an associated address.

It is not the aim of this paper to show the process leading to the final relational schema derived from the conceptual schema [6]. In table 2 we only make the list of the relations and of the corresponding component fields.

## 4.1. Environment Description

At the higher level, DDS asks the user for the activation of one of the functions listed in table 1. The first operation to be performed is the definition of the environment, that is labelling the DB

Table 2
Sample relations list.

```txt
CONTRACT (prog-num, type, addr-code, cust-code, init-date)
TEMP-CUSTOMER (cust-code, appl-date)
CUSTOMER (cust-code, birth-date, comp-type, heading, extinguish-date, activity, city, citizenship, pers-or-comp, fiscal-code)
CONTRACT-SUB-CONTRACTOR (cust-code, prog-num, type)
ADDRESS (addr-code, road, zip, city, district, state)
ADDRESS-TO-CUSTOMER (addr-code, cust-code, addr-type)
PERSON (cust-code, birth-city, birth-state, birth-date)
COMPANY (cust-code, foundation-date, comp-type, legal-seat)
```

project in such a way that all the internal files of DDS may record it for successive runs. Then the user may activate function nr. 2 in order to create the relational schema. A DDL (Data Definition Language) is provided to this purpose. For instance the PERSON relation will be defined as follows:

create table PERSON
CUST-CODE :char [10, alphanum].. 150000
BIRTH-CITY :char[30, name] .. 1600
BIRTH-STATE :char[2, alpha] .. 50
BIRTH-DATE :date
with tuples 150000

For each attribute the user defines the type and the expected number of distinct values. DDS distinguishes two cases:

a) the cardinality of an attribute is very close to the cardinality of the relation (i.e. CUST-CODE does not present duplicate values);

b) the cardinality of an attribute is lower than the number of tuples (i.e. BIRTH-STATE).

Analogously, each query relevant to the workload must be described, by using function nr. 4, where a description SQL-like language is available. For example:

select \*
from CUSTOMER
where FXTINGUISH-DATE > value
and ACTIVITY = mvalue

Moreover the user must add information about the frequency of the query, as mentioned in section 3.

Functions 1, 2 and 4 produce the internal dictionary that is used in function nr. 6 for the choice phase. A remark is perhaps in order: the internal representation of the relation and workload characteristics could be translated straightforwardly into a specific language for a particular DBMS. Therefore DDS could be easily adapted to many relational DBMS environments.

The declared environment can be saved and partially modified during later design sessions. For each run of function nr. 6, DDS produces an output similar to the one in table 3.

Table 3
Sample DDS output.

<table><tr><td colspan="5">SECONDARY INDEXES</td></tr><tr><td colspan="3">Relation</td><td>Index on</td><td>Index Space</td></tr><tr><td colspan="3">CONTRACT</td><td>prog-num</td><td>526</td></tr><tr><td colspan="3">CONTRACT</td><td>cust-code</td><td>197</td></tr><tr><td colspan="3">CONTRACT-SUB-CONTRACTOR</td><td>prog-num</td><td>133</td></tr><tr><td colspan="3">CUSTOMER</td><td>cust-code</td><td>94</td></tr><tr><td colspan="3">CUSTOMER</td><td>heading</td><td>282</td></tr><tr><td colspan="3">ADDRESS</td><td>address-code</td><td>76</td></tr><tr><td colspan="3">ADDRESS TO CUSTOMER</td><td>cust code</td><td>984</td></tr><tr><td colspan="3">TOTAL DATA SPACE</td><td>:7424</td><td></td></tr><tr><td colspan="3">TOTAL INDEXES SPACE</td><td>:2298</td><td></td></tr><tr><td colspan="3">INCREASING</td><td>:30.95%</td><td></td></tr><tr><td colspan="5">EXPECTED EXECUTION COSTS</td></tr><tr><td>Query nr.</td><td>Weight</td><td>Access path</td><td>Cost</td><td>Primary Cost</td></tr><tr><td>1</td><td>125</td><td>PRIMARY</td><td></td><td>529</td></tr><tr><td>2</td><td>75</td><td>prog-num</td><td>6</td><td>529</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td colspan="5">EXPECTED I/O SAVING: 79.10%</td></tr></table>

## 4.2. More Issues on the Dialog Phase

The whole DDS, and therefore also the dialog module, is implemented in Pascal for VAX/VMS systems. The user interface consists of three main modules. The first two perform the interpretation of the input (parsing) and the transformation into an internal form (semantic analysis). Each execution of one of the dialog functions listed in table 1 implies the activation of the first module. The second one is activated for the functions concerning the input or modification of queries. In the case of error detection from one of the two previous modules, the third one is activated and requests a new correct input from the user.

As far as the workload analysis is concerned, some additional considerations are useful on the recognition and translation of the logical expressions containing the predicates that usually characterize an operation in relational environments. These expressions can be very complex and contain several level of parentheses. In these cases the evaluation of a query execution can become complex and the design module of IDEA does not perform such a deep analysis, discarding some possible access paths because it is not able to evaluate their effectiveness. On the other hand also the optimizers of many relational systems are not able to make the best choice to find out the best access path when a query presents too complex predicates. For example, the selection predicate

not (P1 or P2),

where P1 and P2 are simple predicates, may be rewritten as

not (P1) and not (P2)

allowing the recognition of two Boolean factors, and, therefore, two possible indexed access paths.

In order to be able to deal with arbitrarily complex predicate expressions, the module ODEFIL (Optimizer DEcomposer Filtering Loader) has been developed. In this module each logical expression is reduced into a minimal form by means of successive transformations, which find out all the Boolean factors that compose the expression and put together predicates on the same field. Details on ODEFIL will be shown in forthcoming paper.

The minimized form of the queries generated by ODEFIL could also be utilized as a feed-back to the designer to suggest equivalent forms of the queries having the same semantic, but a lower complexity. These forms can be proficuously substituted for the previous ones for the normal operations on the database.

## 5. Conclusions

In this paper we described the architecture and the main concepts of a modular user-oriented self-contained design decision support (DDS). The decision support is addressed to the great number of database users who have at their disposal a commercial DBMS but not an integrated design tool. Its main features are (a) a high level language user interface allowing an easy description of the database structure and workload, (b) an incremental description of the design environment, providing a good flexibility, (c) a forecasting of the execution I/O costs if the proposed solution is adopted and also a guidance for the access paths to be adopted in the various operations (useful for systems which do not provide this facility). Future work will be devoted to the building of an integrated layered model able to capture the effects on resource consumption, throughput and response times of the various logical and physical DB design decisions [10].

## References

[1] A. Albano, V. De Antonellis and A. Di Leva, eds., Computer-aided Database Design (North-Holland Publ. Comp., Amsterdam, 1985).

[2] P. Bertaina, A. DiLeva and A. Giolito, Logical Design in CODASYL and Relational Environment, in: [6] 85–117.

[3] R. Bonanno, D. Maio and P. Tiberio, An Approximation Algorithm for Secondary Index Selection in Relational Database Physical Design. The Computer Journal 28, 2 (1985) 398–405.

[4] F. Bonfatti, D. Maio, M. Spadoni and P. Tiberio, An Indexing Technique for Relational Data Bases, in: Proc. IEEE COMPSAC (Chicago, IL, 1980) 784–791.

[5] F. Bonfatti, D. Maio and P. Tiberio, A Separability Based Method for Secondary Index Selection, in: [6] 149–160.

[6] S. Ceri, ed., Methodology and Tools for Database Design (North-Holland Publ. Comp., Amsterdam, 1983).

[7] D. Comer, The Ubiquitous B-tree, Computing Surveys 1, 2 (1979) 397–434.

[8] S. Cristodulakis, Estimating Record Selectivities, Information Systems 8, 2 (1983).

[9] D. Ferrari, A Performance Oriented Procedure for Mod-

elling Interactive Workload, in: D. Ferrari and M. Spadoni, eds., Experimental Computer Performance and Evaluation (North-Holland Publ. Comp., Amsterdam, 1981).

[10] D. Maio and C. Sartori, A Queueing Network Model Approach for Evaluating Relational Data Base Performances, Paper presented at 4-th IASTED Int. Symposium and Course on Modelling and Simulation, Lugano, Switzerland (1983).

[11] D. Maio, C. Sartori and M.R. Scalas, Architecture of a Physical Design Tool for Relational DBM Ss., in: [1] 115-130.

[12] M. Schkolnick and P. Tiberio, A Note on Estimating the Maintenance Cost in a Relational Database, ACM Transactions on Database Systems 10, 2 (1985) 398–405.

[13] T.J. Teorey, J.P. Fry, Design of Database Structures (Prentice-Hall, Engelwood Cliffs, NJ, 1982).

[14] S.J. Waters, Hit Ratios, Computer Journal 19, 1 (1986) 21–24.

[15] K.Y. Whang, G. Wiederhold and D. Sagalowicz, Separability - An Approach to Physical Database Design, IEEE Transactions on Computers C-33, 3 (1984) 20–222.

[16] K.Y. Whang, G. Wiederhold and D. Sagalowicz, The Property of Separability and its Application to Physical Database Design, in: Query Processing in Database Systems (Springer-Verlag, Berlin; forthcoming).

[17] G. Wiederhold, Database Design (McGraw-Hill, 1983).

[18] E. Wong and K. Youssefi, Decomposition - A Strategy for Query Processing, ACM Transactions on Database systems 1, 3 (1976) 223-241.
