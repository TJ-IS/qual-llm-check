---
otero_id: 18068
otero_key: "AP3G5F29"
title: "Computer-aided system for the database storage structure design"
authors: "Hemant K. Jain; John R. Krobock"
year: "1983"
journal: "Information & Management"
doi: "10.1016/0378-7206(83)90042-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computer-Aided System for the Database Storage Structure Design

Hemant K. Jain \*

Department of Industrial Engineering and Operations Research, Syracuse University, Syracuse, New York 13210, USA

and

John R. Krobock

School of Business and Public Administration, California State University, Sacramento, Sacramento, CA 95819, USA

An overview is given of a computer aided system for the design of a schema for a CODASYL DBMS. The system helps the designer to trade off between the conflicting objectives; short retrieval time for a user query, low database updating cost, small storage requirements, and low total cost of the system. Different relative weights can be assigned to each of the users query and update transactions, and the design objectives can be assigned different priorities. The model evaluates the performance of the database for a specified set of input parameters and finds the optimal location mode of each database record type. The designer can interactively change any of the design parameters, priority and weights while performing the analysis. The system has been tested on the design of a department store database.

Keywords: Database, Database Administrator, Schema Design, CODASYL DBMS.

\* The present address of the author is School of Business Administration, University of Wisconsin-Milwaukee, P.O. Box 413, Milwaukee, Wisconsin 53201, USA

## 1. Introduction

It is generally recognized that the initial design of the database is one of the most important factors affecting the success of an application of data base system. The logical database design deals with the design of a logical data structure which supports each of the user's information require-

![](/api/attachments/AP3G5F29/fulltext/images/1cd24b7d7d625b27cae92dcb58fe6f0f315160e547faf8289c8c85b016c62e1c.jpg)

Dr. Hemant K. Jain is an Assistant Professor of Industrial Engineering and Operations Research at Syracuse University. Starting from September 1983 he will be joining the faculty of Management Information Systems in the School of Business Administration, University of Wisconsin Milwaukee. He received his B.S. in Mechanical Engineering from University of Indore, (India) and a M. Tech and Ph.D. in Industrial Engineering from I.I.T. Kharagbur (India) and Lehigh Univer-

sity, Bethlehem, PA respectively. He has published several papers and has been consultant to several organizations. His primary areas of teaching, research and consulting are Database Design, Distributed Computer System, Computer Networking and Distributed Database Management Systems. He is a member of ACM, IEEE Computer Society, AIIE, TIMS and Sigma Xi.  
![](/api/attachments/AP3G5F29/fulltext/images/1e4f38bb8d86164bb988f7ce77e1a20c53641221e3f3d9747ee07066b2ea0a82.jpg)

Dr. John R. Krobock is a Professor of Management Information Science at California State University, Sacramento, Sacramento, California. He received his Ph.D. degree from Arizona State University in 1981. He has presented papers at various conferences. His research and consulting endeavors include data base design and utilization, and analysis, design, and evaluation of systems.

Before serving as an Associate Professor of Industrial Engineering at

Lehigh University, he was an Assistant Professor and Assistant Dean at Florida International University, Miami, Florida. His industrial experience prior to graduate school includes assignments as a group engineer, manager, and project director.

He is a member of several organizations including AIIE, TIMS, AIDS, ASEE, and AMA.

ments and is visible to the application programmer. The physical design deals with the organization of data in storage and is based on efficiency considerations. There is widespread agreement that logical and physical database design should be independent and any changes in the physical design should not necessitate changes in the application program. The 1978 CODASYL specification [2] provides such data independence by separating the storage schema (physical design) described by Database Storage Description Language (DSDL) from the schema (logical design) described by the Data Description Language DDL. This paper describes an interactive computer aided system (CASSED) developed to help the designer in mapping a schema (logical) to the storage schema.

CASSED system receives, as input, the logical schema derived by the analysis and integration of the user's information requirements without consideration of data volume and usage. The system includes techniques to help the designer in:

the collection of relevant input data and design parameters;

the analysis of anticipated user's query requirements and database updating transactions;

the evaluation of the alternative storage structures with reference to the retrieval time for each user's query, database updating cost, storage requirements, and the total operating efficiency:

determining the optimal location mode of each record type.

Thus, CASSED, when used with logical database design techniques like EIDOS [12] and DESIGNER [3], will provide a comprehensive system for database design. The contribution of CASSED is in providing the database designer with a practical method for trade off analysis of various conflicting design objectives.

## 2. The Storage Schema Design Problem

The process of mapping a logical schema to a storage schema allows the designer to control the way data is to be organized and stored on the storage media available.

A significant amount of research has been dedicated to develop models for partial and/or specialized aspects of physical database design, such as file structuring [7,15], record segmentation and clustering [6,11,13], and index selection [1,5]. These models are reviewed by Schkolnick [14]. Although the above models give an insite into the problem of physical database design, they do not provide a comprehensive model for the storage schema design. Only a few database design aids, like Theory's Database Design Evaluator [16] and Gambino's Database Design Decision Support System [3] are available. The usual approach taken is to formulate the problem as minimization of cost over some solution space.

It is clear that the total design problem is quite intractable. The wide variety of design parameters like block/page size, index selection, link design, clustering of records, and file selection contributes to the difficulty. While the attention to individual design problems results in elegant solutions, it is quite possible that individual solutions will have to be perturbed when the system is integrated. There is thus a need to model the trade offs between these issues in view of the multicriteria nature of the design problem. A zero-one linear integer goal programming model has been used to help the designer in trade off analysis. The system assumes a 1978 CODASYL specifications, though similar models could be developed for other database models.

The CODASYL model uses a network approach, where the nodes of the network represent individual record types (a record type may have a number of record occurrences) and the edges represent the named relationship between record types, called the "set type." The database is logically partitioned into a number of "areas." The storage schema design allows the designer to specify the page size, number of pages allocated, and the number of buffers assigned to each area. A large page size decreases the number of accesses to secondary storage but increases the buffer (primary) storage required and volume of data transferred. The number of buffers assigned to the area allows a trade off between the probability of finding the required page in the buffer (thereby eliminating access to secondary storage) and primary storage required. The access paths through the database, which govern the efficiency of processing a particular query, are determined by set implementation strategy. A CODASYL set can be implemented by a combination of owner, prior, and next pointers. Each pointer combination reduces the access time of certain classes of accesses via a set type, at the expense of increased storage for the pointers involved, and usually increased update costs when set memberships are changed.

In a CODASYL database, the relative location of the record occurrences on the storage media are controlled by specifying the location mode (CALC, SEQUENTIAL, or VIA) of the record type. The CALC mode distributes the occurrences of a record over the area by using a randomizing algorithm, while the specification of SEQUENTIAL mode would result in the physical location of record occurrences in the order of key value. In case of VIA mode, member record occurrences related to an owner record are located near one another. A user query or updating transaction naturally runs faster if there are several required record occurrences on each page accessed from secondary storage. Since a record type can be assigned only one type of location mode, its choice usually optimizes one type of access at the expense of others, and therefore it should be based on the frequency and type of accesses required to process the user's query and updating transactions.

Certain other facilities, like clustering or partitioning of logical records for physical storage, are available but are not considered here to keep the problem tractable. The design parameters described above are interdependent, so the choice of one alternative will affect the choice of others, e.g., the combinations of pointers selected to implement the set will affect the total required storage space. To keep the model tractable, the following simplifying assumptions are made.

(1) Logical records map one-to-one to a physical record. Thus, a storage record is the same as a logical record.

(2) Sets are implemented as a chain of pointers and the sorted sets have an index.

(3) All pages within an area are of the same size. Each record occurrence is stored exactly once in the database and record occurrences do not span pages. Page overflow is neglected.

## 3. Description of the System

The CASSED is an interactive system developed on a DECsystem-1060 computer. One of the principal design criteria was to keep the software as transportable as possible. The programs are strictly modular and the programming language is ANSI standard FORTRAN. The system is designed to be self-instructive. It guides the database designer through the design process by appropriate prompts and questions. When a choice or decision is needed, it presents either a yes or no question or a menu of alternatives. Embedded in the system are help and instructional aids. These allow the designer to examine current input data and receive explanations whenever the system is awaiting either data or an impending decision. The designer can change a single design or input parameter and obtain a new design along with the results of the evaluation on the terminal screen. The system consists of four modules. Fig. 1 provides an overview of the entire system.

![](/api/attachments/AP3G5F29/fulltext/images/5c19797f90b41161d59fde30b06fb159a42c98ff15ee050fcd7cd4f4755727f5.jpg)  
Fig. 1. An Overview of the CASSED System.

3.1. Input data and Design Parameter Specification Module

This module provides a systematic way of collecting and specifying the input data. It has two parts. The first asks for input of logical schema information (record types and set types, set a membership conditions, set order, area assignment, etc.). It also collects information on hardware and software parameters, cost parameters, and data volumes. The second part allows the designer to specify or change storage schema design parameters like size of a database page (block) for each area, number of buffers assigned to the area, owner and/or prior pointers for the sets, and packing factor for the areas. Based on the input and design parameters specified, this module also calculates the values of the following variables to be used by the evaluation module:

for each set type, the average number of member record occurrences for a set occurrence;

for each record type, the space required to store an occurrence of the record, including pointers; the effective page size;

the number of pages in each area;

for each record type, the number of pages required to store all of its occurrences sequentially;

for each record type, the maximum number of record occurrences that can be stored on a page (SEQUENTIAL or VIA location mode).

## 3.2. Accessing and Updating Requirements Specification Module

This module helps the designer in analyzing each of the distinct user query requirements and in identifying the access path through the database to satisfy the query. Any user query can be represented by a combination of one or more of the following access operations:

(1) Keyed Access - to one particular occurrence of a record type based on the key value of the record.

(2) All Member Access - to all member record occurrences in an occurrence of the set.

(3) One Member Access - to one particular member record occurrence for a set occurrence.

(4) Owner Access - to the owner record of a set occurrence from a member record occurrence.

(5) Access to All Occurrences - to all the occurrences of a record type.

As an example, for the schema shown in Fig. 2, the query “Which vendors service a particular inventory item?” can be satisfied by following access operations.

(1) Keyed Access - to one particular Inventory-Record occurrence based on its key value. Frequency - One

(2) All Member Access - to all Vendor-Item-Record occurrences for an occurrence of Inven-Set

Frequency - One

![](/api/attachments/AP3G5F29/fulltext/images/839739d6b0345c754322a9bac0e6ff8e8c08a667a7568746543d2b40eb919abb.jpg)  
Fig 2 Logical Schema of Department Store Database.

(3) Owner Access – to owner record occurrence of Vendor-Set from an occurrence of Vendor-Item-Record.

Frequency - Number of occurrences of Vendor-Item-Record in an occurrence of Inven-Set.

The frequency specified above represents the number of times the specified operations are to be performed in answering the query.

Similarly, each update transaction is represented by a combination of one or more of the following update operations:

(1) Delete one occurrence - based on its key value.

(2) Delete all member occurrences - of a particular record type in an occurrence of the set.

(3) Delete all occurrences - of a record type.

(4) Store a record occurrence - in the database.

(5) Modify non-keyed data items - in a particular

record occurrence.

(6) Modify key data item - of a particular record occurrence.

The estimated frequency of each query and update transaction is also specified. The database designer can assign weights to each of these query and update transactions. The assignment of weights should be based on such considerations as their relative importance, their frequency, and response time requirements.

## 3.3. Design Evaluation Module

This Module uses the inputs to evaluate the storage structure design. For each query requirement, the software derives an expression of expected time required to access data from secondary storage [10]. As any query can be represented by a combination of the five access opera-

![](/api/attachments/AP3G5F29/fulltext/images/51f22cdb549dbe999466803d8bb160e924af765a5be3bf4327c9cbbe5f0426c0.jpg)  
Fig. 3. Menu of Choices.

```markdown
Which design parameter do you want to change
(Type 0 for list or type input code)

> 0

The following options are available:

INPUT CODE DESCRIPTIONS
1. Prior Pointers
2. Owner Pointers
3. Area Assignment
4. Page Size and Buffers
5. Hardware Parameters & Software Parameters
6. Cost Parameters
7. Set Order
8. Record Membership
Condition (Optional/Mandatory)

> 1

Please type the serial number of the set in which you want to specify or change prior pointer
(Type "!" for information on stored data and serial numbers)

> 10

Please type
1 - for Prior Pointer
0 - for No Prior Pointer

Do you want to specify or change prior pointer in any other set.
If yes type "Y" else type "N"

• N

Do you want to change any other input parameters?
If yes type "Y" else type "N"

> Y

Fig. 4. Specifying or Changing Values of Design Parameters.

What operation do you want to perform?
(Type 0 for list or type operation number)

> 0

The following options are available:

OPERATION NO. DESCRIPTIONS
1 Add a new users query type
2 Modify existing user query type
3 Add a new database updating transaction
4 Modify an existing updating transaction
5 Modify or assign priorities to different objectives and relative weights to users query and updating transactions.

> 1
```  
Fig. 5. Menu of Options Provided by Module 2.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\therefore m = \frac{3}{11}$
</div>

What operation do you want to perform? (Type 0 for list or type operation number)

$\Rightarrow$ 1

The serial number of the users query type you will be adding is 2. Please type the name (upto 10 characters) of the query type

## V-I-LIST

Please input the frequency of report generated per month using this query type

40

that type of access to database is required to generate one instance of users query type V-1-LIST.

(Type 0 for list of accesses available or type access code)

```txt
→ 0
```

The following accesses are available:

<table><tr><td>ACCESS CODE</td><td>DESCRIPTIONS</td></tr><tr><td>1</td><td>Keyed access to one particular occurrence of a record type</td></tr><tr><td>2</td><td>Access to all the member record occurrences through a set</td></tr><tr><td>3</td><td>Access to one particular member record occurrence through a set</td></tr><tr><td>4</td><td>Access to owner record occurrence through a set</td></tr><tr><td>5</td><td>Access to all the occurrences of a record type</td></tr></table>

The frequency of this access type required for generating one instance of users query is given by

<table><tr><td>SERIAL. NO.</td><td>DESCRIPTIONS</td></tr><tr><td>1</td><td>Number of occurrences of a record in a set of which it is a member</td></tr><tr><td>2</td><td>All the occurrences of a record</td></tr><tr><td>3</td><td>An absolute value</td></tr></table>

(Please type the serial number applicable)

## → 3

Please input the frequency of this access type required for generating one instance of users query type V-1-LIST

→ 1

Please type the serial number of record type whose occurrence is to be accessed using a key value

5

Any more access to data base required for generating user query type V-I-LIST?

(If yes type "Y" else type "N")

$\Rightarrow$ Y

Fig. 6. Specifying a Query.

tions described before, the expression of the expected access time can be obtained by combining the access time expressions of each operation. These expressions are derived in terms of the following 0–1 variables representing the record

placement strategy.

$X_{1}(I) = \left\{ \begin{array}{ll}1, & \text{if the location mode of Ith record}\\  & \text{type is CALC},\\ 0, & \text{otherwise}. \end{array} \right.$

```txt
What operation do you want to perform?
(Type 0 for list or type operation number)

⇒ 5

Please assign distinct priorities to the following objectives

SERIAL NO. DESCRIPTIONS
1 Minimize operating cost of the system
2 Minimize total storage space needed
3 Minimize weighted access time
4 Minimize weighted updating time

Please type the serial number of objective to which priority needs to be assigned or changed

⇒ 4

Please indicate the priority of objective 4 to be used in optimization model
(One indicates the highest priority, Two indicates lower than one and so on)

⇒ 3

Do you want to assign or change the priority of any other objectives?
(If yes type "Y" else type "N")

⇒ N

Do you want to assign or change weights of different user query?
(If yes type "Y" else type "N")

⇒ Y

Please type the serial number of users query to which weightage needs to be assigned or changed

⇒ 1

Please indicate the weight to be assigned to the CUST-SALE query type.
(1.0 is the normal weight, higher number will indicate the higher weight, while a number lower than 1.0 will indicate a lower weight)

⇒ 2.0

Do you want to assign or change the weight of any other user?
(If yes type "Y" else type "N")

⇒ N
```  
Fig. 7. Assigning Priorities and Relative Weights.

You have an option of either finding the optimal location mode or specifying the location mode to be used for evaluating the design. Do you want to find the optimal location mode?
(If yes type "Y" else type "N")

1 Total storage space required in thousands of words is = 1262.81430

2 The cost of the system in dollars per month is - 458.35 (includes storage and accessing cost only)

2\* The buffer space required per user using all the areas is =

3 The expected access time in milliseconds for the generation of one instance of a query

<table><tr><td>QUERY TYPE</td><td>ACCESS TIME</td></tr><tr><td>CUST-SALE</td><td>57.20361</td></tr><tr><td>V-I-LIST</td><td>11325.08300</td></tr><tr><td>I-V-LIST</td><td>1424.14580</td></tr><tr><td>PAY-COST</td><td>382570.63000</td></tr><tr><td>DEPT-SALE</td><td>382570.63000</td></tr><tr><td>EMP-DEPT</td><td>60.78024</td></tr><tr><td>EMP-SALES</td><td>1912.66310</td></tr><tr><td>SALES-EMP</td><td>68.03558</td></tr><tr><td>DUE-ACCT</td><td>196698.19000</td></tr><tr><td>ITEMS-TRAN</td><td>138.07116</td></tr><tr><td>TRANS-ITEM</td><td>112.93638</td></tr><tr><td>TRAN-DETAL</td><td>211.23972</td></tr></table>

WEIGHTED SUM OF ACCESS TIME = 24373.27400

4 The expected access time in milliseconds for generating one instance of an updating transaction

<table><tr><td>TRANSACTION TYPE</td><td>ACCESS TIME</td></tr><tr><td>NEW-SALE</td><td>1302.00920</td></tr><tr><td>DEL-SALES</td><td>489.39098</td></tr><tr><td>NEW-ITEM</td><td>3974.22810</td></tr><tr><td>DEL-ITEM</td><td>2541.20960</td></tr><tr><td>NEW-VEND</td><td>67551.06000</td></tr><tr><td>DEL-VEND</td><td>17534.99500</td></tr><tr><td>NEW-EMP</td><td>129.17036</td></tr><tr><td>DEL-EMP</td><td>1973.44340</td></tr><tr><td>NEW-ACCT</td><td>390.24025</td></tr><tr><td>DEL-ACCT</td><td>375.47572</td></tr><tr><td colspan="2">EIGHTED SUM OF UPDATING TIME = 19440.08300</td></tr></table>

Fig. 8. Results of Storage Schema Evaluation and Optimization.

## LOCATION MODES OF RECORD TYPE

<table><tr><td>RECORD TYPE</td><td>LOCATION MODE</td></tr><tr><td>ACCT-REC</td><td>CALC</td></tr><tr><td>CUST-REC</td><td>CALC</td></tr><tr><td>C-S-REC</td><td>CALC</td></tr><tr><td>ZIP-REC</td><td>CALC</td></tr><tr><td>VENDOR-REC</td><td>CALC</td></tr><tr><td>V-I-REC</td><td>VIA VENDOR-SET SET</td></tr><tr><td>INVEN-REC</td><td>CALC</td></tr><tr><td>SALES-REC</td><td>CALC</td></tr><tr><td>SALE-ITEM</td><td>CALC</td></tr><tr><td>PAY-REC</td><td>CALC</td></tr><tr><td>DEFT-REC</td><td>SEQUENTIAL</td></tr></table>

INFORMATION ON SET TYPES

<table><tr><td>S. NO.</td><td>SET TYPE</td><td>OWNER RECORD</td><td>MEMBER RECORD</td><td>OWNER POINTER</td><td>MEMBERSHIP CONDITION</td></tr><tr><td>1</td><td>CUST-REC</td><td>ACCT-REC</td><td>CUST-REC</td><td>NO</td><td>MANDATORY</td></tr><tr><td>2</td><td>BAD-C-SET</td><td>ACCT-REC</td><td>CUST-REC</td><td>NO</td><td>OPTIONAL</td></tr><tr><td>3</td><td>CHARGE-SET</td><td>ACCT-REC</td><td>SALES-REC</td><td>YES</td><td>OPTIONAL</td></tr><tr><td>4</td><td>ZIP-SET</td><td>ZIP-REC</td><td>CUST-REC</td><td>YES</td><td>MANDATORY</td></tr><tr><td>5</td><td>C-S-SET</td><td>C-S-REC</td><td>CUST-REC</td><td>YES</td><td>MANDATORY</td></tr><tr><td>6</td><td>VENDOR-SET</td><td>VENDOR-REC</td><td>V-I-REC</td><td>YES</td><td>MANDATORY</td></tr><tr><td>7</td><td>INVEN-SET</td><td>INVEN-REC</td><td>V-I-REC</td><td>YES</td><td>MANDATORY</td></tr><tr><td></td><td></td><td></td><td>SALE-ITEM</td><td>YES</td><td>MANDATORY</td></tr><tr><td>8</td><td>ITEM-SET</td><td>SALES-REC</td><td>SALE-ITEM</td><td>YES</td><td>MANDATORY</td></tr><tr><td>9</td><td>COMM-SET</td><td>PAY-REC</td><td>SALES-REC</td><td>YES</td><td>OPTIONAL</td></tr><tr><td>10</td><td>DEPT-SET</td><td>DEPT-REC</td><td>SALES-REC</td><td>YES</td><td>MANDATORY</td></tr><tr><td></td><td></td><td></td><td>PAY-REC</td><td>YES</td><td>MANDATORY</td></tr></table>

PRIOR POINTERS AND SET ORDER

<table><tr><td>SERIAL NUMBER</td><td>SET_TYPE</td><td>PRIOR POINTER</td><td>SET_ORDER</td></tr><tr><td>1</td><td>CUST-SET</td><td>NO</td><td>UNSORTED</td></tr><tr><td>2</td><td>BAD-C-SET</td><td>NO</td><td>UNSORTED</td></tr><tr><td>3</td><td>CHARGE-SET</td><td>YES</td><td>SORTED</td></tr><tr><td>4</td><td>ZIP-SET</td><td>YES</td><td>UNSORTED</td></tr><tr><td>5</td><td>C-S-SET</td><td>YES</td><td>UNSORTED</td></tr><tr><td>6</td><td>VENDOR-SET</td><td>YES</td><td>UNSORTED</td></tr><tr><td>7</td><td>INVEN-SET</td><td>YES</td><td>UNSORTED</td></tr><tr><td>8</td><td>ITEM-SET</td><td>YES</td><td>UNSORTED</td></tr><tr><td>9</td><td>COMM-SET</td><td>YES</td><td>UNSORTED</td></tr><tr><td>10</td><td>DEPT-SET</td><td>YES</td><td>UNSORTED</td></tr></table>

Fig. 9 (to be cont'd).

<table><tr><td colspan="6">AREA INFORMATION</td></tr><tr><td>SR. NO.</td><td>AREA AREA</td><td>PAGE SIZE</td><td>NO. OF BUFFERS</td><td>NO. OF PAGES</td><td>PACKING FACTOR</td></tr><tr><td>1</td><td>CUST-AREA</td><td>1024</td><td>3</td><td>239.0181</td><td>0.8000</td></tr><tr><td>2</td><td>INVN-AREA</td><td>2048</td><td>3</td><td>178.6320</td><td>0.8000</td></tr><tr><td>3</td><td>SALES-AREA</td><td>2048</td><td>3</td><td>321.4071</td><td>0.8000</td></tr><tr><td>4</td><td>EMP-AREA</td><td>512</td><td>3</td><td>14.9312</td><td>0.8000</td></tr><tr><td colspan="6">AREA ASSIGNMENT</td></tr><tr><td>SERIAL NUMBER</td><td colspan="2">AREA NAME</td><td>RECORD NAME</td><td colspan="2">RECORD SERIAL NUMBER</td></tr><tr><td rowspan="4">1</td><td rowspan="4" colspan="2">CUST-AREA</td><td>ACCT-REC</td><td colspan="2">1</td></tr><tr><td>CUST-REC</td><td colspan="2">2</td></tr><tr><td>C-S-REC</td><td colspan="2">3</td></tr><tr><td>ZIP-REC</td><td colspan="2">4</td></tr><tr><td rowspan="3">2</td><td rowspan="3" colspan="2">INVN-AREA</td><td>VENDOR-REC</td><td colspan="2">5</td></tr><tr><td>V-1-REC</td><td colspan="2">6</td></tr><tr><td>INVEN-REC</td><td colspan="2">7</td></tr><tr><td rowspan="2">3</td><td rowspan="2" colspan="2">SALES-AREA</td><td>SALES-REC</td><td colspan="2">8</td></tr><tr><td>SALE-ITEM</td><td colspan="2">9</td></tr><tr><td rowspan="2">4</td><td rowspan="2" colspan="2">EMP-AREA</td><td>PAY-REC</td><td colspan="2">10</td></tr><tr><td>MPT-AFC</td><td colspan="2">11</td></tr><tr><td colspan="6">Do you want the previously preferred type displayed?(If yes type &quot;Y&quot; else type &quot;N&quot;)→ NDo you want this design stored as the preferred design&#x27;(If yes type &quot;Y&quot; else type &quot;N&quot;)→ YDo you want to perform any other operation?(If yes type &quot;Y&quot; else type &quot;N&quot;)→ N</td></tr></table>

Fig. 9. Present Storage Scheme Design.

$X_{2}(I,J) = \left\{ \begin{array}{ll}1, & \text{if location mode of } I \text{th record}\\  & \text{type is via set type } J,\\ 0, & \text{otherwise.} \end{array} \right.$

$$
X _ {3} (I) = \left\{ \begin{array}{l l} 1, & \text { if   the   location   mode   of   Ith   record } \\ & \text { type   is   SEQUENTIAL }, \\ 0, & \text { otherwise }. \end{array} \right.
$$

Similar expressions are derived for each of the updating transactions. The evaluation module also derives the expressions of storage space required and operating cost (accessing, updating, and storage) of the system in terms of the above variables.

## 3.4. Optimization Module

The previously generated set of expressions represent the objectives of the storage structure design in terms of input parameters and the decision variables (record placement strategy). These will be conflicting in nature. The optimization module uses the multiple criteria Zero-One-Linear integer goal programming model [8] to get the optimal record placement strategy for each record type. For the purpose of the goal programming model, the design objectives have been grouped as to minimize:

(1) weighted access time to satisfy queries.

(2) operating cost.

(3) weighted access time for update.

(4) the storage space required.

The database designer can assign preemptive priorities to them as described in [9].

## 4. An Example

The design of a department store database is described here to demonstrate the use of CASSED and its results.

The Problem: A database system is to be developed to help manage the retail mail order and showroom operations of a store selling a wide variety of consumer products. Previously, the Database Administrator has analyzed the information and database updating requirements: twelve user queries and ten database updating transactions were defined. Based on the user's information requirements, a logical schema was derived (see Figure 2). It contains 11 record types and 10 set types.

The following conventions hold in this illustration: all prompt or output messages emanate either from CASSED or from the TOPS-20 operating system; the database designer's responses consist only of upper case letters and are underlined. The TOPS-20 prompt character is "@". The CASSED system's prompt character is "⇒".

The DBA loads the CASSED system by a RUN CASSED command. The system responds with a greeting and a menu of 3 choices (see Figure 3). The specification of code 1 will take the designer to module 1 of the system while a response of 2 will read the previously stored input data and go to module 2 of the system. A response of 3 will evaluate and/or optimize the current design. The DBA's interaction with each of these modules are now briefly described.

## 4.1. Module I

Here, the CASSED system prompts the DBA for the number of record types and set types, record names and set names, and set membership. For each record type, the DBA also specifies record size and expected number of occurrences. Next, module 1 requires the specification of design parameters. The DBA can specify or change any single design parameter by providing an appropriate input code (see Figure 4).

## 4.2. Module 2

This allows the designer to specify or change each query and update transaction. It also allows the designer to assign priorities to design objectives and relative weights to the queries and update transactions (see Figure 5). For each query, query name, expected frequency, and type of access operations required to satisfy the query are entered (see Figure 6). Similar information is entered for each update transaction, figure 7 illustrates assignment of priorities and weights.

## 4.3. Modules 3 and 4

Module 3 provides the designer with the results of the evaluation (see Figure 8). It then calls module 4 (if desired) to find the optimal location mode of record types (see Figure 9).

Now, after comparing this design with any previous ones, the designer can return to module 1 and change any of the design parameters, etc. This process can thus be repeated until a satisfactory solution is obtained.

## 5. Conclusions

A computer-aided system (CASSED) for database design is described. The validity of the mathematical models used in the CASSED system were tested by comparing the performance of the database estimated by the CASSED system with the actual performance of the 3000 page database created for this purpose [9]. On-going research is concerned with expanding and further improving the evaluation module. Currently, one-to-one mapping has been assumed between storage and logical record types, the evaluation model of the CASSED system can be extended to allow the storage record type (defined in the DSDL) to be represented as a subset or union of logical record types for efficiency considerations.

## References

[1] H.D. Anderson and P.B. Berra, "Minimum Cost Selection of Secondary Indexes for Formatted Files," ACM TODS, Vol. 2, No. 1, March 1977.

[2] CODASYL Data Description Language Committee, Data Description Language Journal of Development, Hull, Quebec: Secretariat of Canadian Government EDP Standards Committee, 1978.

[3] T.J. Gambino and R. Gerritsen, "A Data Base Design Decision Support System," Proc. of Third International Conference on Very Large Data Bases, Tokyo, Japan, October 1977.

[4] R. Gerritsen, "A Preliminary System for the Design of DBTG Data Structures," Communications of ACM, Vol. 18, No. 10, 1975.

[5] M. Hammer and A. Chan, "Index Selection in a Self-Adaptive Data Base Management System," Proc. ACM SIGMOD, 1976.

[6] J.A. Hoffer and D.G. Severance, "The Use of Cluster

Analysis in Physical Database Design," Proc. of First International Conference on Very Large Databases, September 1975.

[7] D. Hsiao and F. Harary, "A Formal System for Information Retrieval from Files," Communications of ACM, Vol. 14, No. 2, February 1970.

[8] J.P. Ignizio, Goal Programming and Extensions, Lexington Books, Massachusetts, 1976.

[9] H.K. Jain, "The CASSES: A Computer Aided System for the Storage Structure Design of CODASYL Databases," Ph.D. Dissertation, Lehigh University, 1981.

[10] H.K. Jain, "The CASSES: A Computer Aided System for the Storage Structure Design of CODASYL Databases," Working Paper #81-012, Dept. of Industrial Engineering and Operations Research, Syracuse University.

[11] S.T. March and D.G. Severance, "The Determination of Efficient Record Segmentation and Blocking Factors for Shared Data Files," ACM TODS, Vol. 2, No. 3, September 1977.

[12] K. Nemovicher, "The EIDOS System: A Computer-Aided Methodology for Database Design," Ph.D. Dissertation, Lehigh University, 1981.

[13] M. Schkolnick, "A Clustering Algorithm for Hierarchical Structures," ACM TODS, Vol. 2, No. 1, March 1977.

[14] M. Schkolnick, "A Survey of Physical Database Design Methodology and Techniques," Proc. of Fourth International Conference on Very Large Data Bases, West Berlin, Germany, 1978.

[15] D.G. Serverance, "A Parametric Model of Alternative File Structures," Information Systems, Vol. 1, No. 2, 1975.

[16] T.J. Teorey and L.B. Oberlander, "Network Database Evaluation Using Analytical Modeling," AFIPS Conference Proceedings, 1979 National Computer Conference, New Jersey.
