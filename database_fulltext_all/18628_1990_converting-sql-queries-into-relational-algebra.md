---
otero_id: 18628
otero_key: "WJT5T7A3"
title: "Converting SQL queries into relational algebra"
authors: "Mohammad Dadashzadeh; David W. Stemple"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90045-j"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Converting SQL queries into relational algebra

Mohammad Dadashzadeh

Department of Decision Sciences, The Wichita State University, Wichita, KS 67208, USA

David W. Stemple

Department of Computer and Information Science, University of Massachusetts, Amherst, MA 01003, USA

We present an algorithm for converting a semantically meaningful SQL query into an equivalent algebraic expression. The relational algebra we employ consists of the following operators: union, intersection, difference, Cartesian product, selection, and projection. The SQL queries we consider can have an arbitrary level of nesting but are restricted in three ways. We assume that they do not contain an ORDER BY or a GROUP BY clause, all SELECTs are in fact SELECT DISTINCTs, and that no aggregate functions are used. The first two assumptions are made in order to remain faithful to the definition of a relation as a set of rows. The last assumption is needed since there is no standard for incorporating aggregate functions into a relational algebra. The research results in this paper will be useful in implementing an SQL user interface for database management systems that internally employ relational algebra. They can also be used in optimizing the evaluation of SQL queries.

Keywords: SQL, Relational Algebra, Grouped Generalized Division, Query Languages, Query Optimization, Relational Database Management Systems.

![](/api/attachments/WJT5T7A3/fulltext/images/9bc568dce59605e459f75d06605b0cba7a27686d99935f55c8a4297379f8ea7e.jpg)

Mohammad Dadashzadeh is a graduate of MIT and University of Massachusetts. He has been affiliated with University of Detroit where he served as an Assistant/Associate Professor of management information systems, and is presently with The Wichita State University. Dr. Dadashzadeh has been an information systems consultant to many organizations here and abroad, and has written on relational algebra for Journal of Systems Management and Information Systems. He serves on the Editorial Review Board of Journal of Microcomputer Systems Management and is the Editor-in-Charge of Journal of Database Administration.

![](/api/attachments/WJT5T7A3/fulltext/images/ac570460696b130ddbf635b49785ab3725a69bea77061f8bb75d37bdf3ca4703.jpg)  
David W. Stemple is an Associate Professor of computer and information science at University of Massachusetts where he leads the ADABTPL project. He has published in ACM Transactions on Database Systems, IEEE Transactions on Software Engineering, Information Processing and Management, and several ACM conference proceedings.

## 1. Introduction and motivation

Amongst the many data manipulation languages that have been proposed for the relational data model, SQL has received the most attention. SQL has been adopted as an official standard by the American National Standards Institute (ANSI) [4], and is expected to be adopted as an international standard by the International Standards Organization (ISO) [16]. SQL continues to gain wide user acceptance, as witnessed by the numerous SQL-based products that are already available in the marketplace. Therefore, it is clear that database management system (DBMS) vendors must support SQL in order to remain competitive.

In this paper, we consider the problem of translating an SQL query into relational algebra. Our motivation for this work is twofold. First, the internal operations used by relational DBMSs, whether SQL-based or not, to evaluate user queries are those of a relational algebra (e.g., selection, projection, and join). Hence, by providing an algorithm to translate SQL queries into relational algebra, DBMS vendors can support an SQL user interface without needing to write an SQL interpreter/compiler.

Second, SQL is a block-structured language that allows nesting of one query block inside another. In a straightforward implementation of an SQL interpreter/compiler, query blocks are evaluated in the implied sequential order (from inside out) without any attempt at global reorganization $[5,22]$ . This can sometimes be very inefficient $[18]$ . Because of the large body of techniques developed for optimizing the evaluation of relational algebra expressions $[3,6,10,15,17,23–26]$ , it seems appropriate to consider the translation of an SQL query into an algebraic expression as the first step in the implementation of SQL.

Here, we present an algorithm for converting a semantically meaningful SQL query into an equivalent algebraic expression. The relational algebra we employ consists of the following operators: union, intersection, difference, Cartesian product, selection, and projection. The SQL queries we consider can have an arbitrary level of nesting but are restricted in three ways. We assume that they do not contain an ORDER BY or a GROUP BY clause, all SELECTs are in fact SELECT DISTINCTs, and that no aggregate functions (such as AVG) are used. The first two assumptions are made in order to remain faithful to the definition of a relation as a set of rows (i.e., no duplicate rows are allowed and the ordering of rows is immaterial). The last assumption is needed since there is no standard for incorporating aggregate functions into a relational algebra.

## 2. Notation and Terminology

A relational database consists of a collection of named, time-varying relations. Each relation is a subset of a Cartesian product space, $D_{1} \times D_{2} \times \cdots \times D_{n}$ , where the $D_{i}$ are sets of values called the domains of the relation. It is helpful to think of a relation as a table of data. Each column is identified by an attribute name in addition to a domain specification. Each row corresponds to an n-tuple. The ordering of rows is immaterial and all rows are distinct. These properties are immediate consequences of the fact that a relation is a set of rows or n-tuples.

A relational algebra provides a set of operators that can be used to construct any desired relation from those in the database and any intermediate (temporary) relations that may be required. In what follows, we define the relational operators. Preceding these definitions, however, we need to introduce some terminology. The logical symbols AND, OR, NOT, F\_ALL (for all), T\_EXT (there exists), ELM\_OF (element of), N\_ELM\_OF (not an element of), and | (such that) will be used with their usual meaning. We use theta to denote any one of the arithmetic comparison operators: .LT. (less than), .GT. (greater than), .LE. (less than or equal to), .GE. (greater than or equal to), .NE. (not equal to), and .EQ. (equal to). The following definitions will be needed.

Definition. Let R be a relation on the set of domains $\{D_{1}, D_{2}, \ldots, D_{n}\}$ and r ELM\_OF R.

1. The n-tuple r is designated by $\langle r_{1}, r_{2}, \ldots, r_{n} \rangle$ ; $r_{i}$ , the ith component of the tuple, is a member of $D_{i}$ , the domain associated with the ith column.

2. $\mathbf{r}[\mathbf{D}_{\mathrm{i}}]$ (or equivalently, $\mathbf{r.D}_{\mathrm{i}}$ ) denotes the ith component (value of $\mathbf{D}_{\mathrm{i}}$ ) of $\mathbf{r}$ , that is, $\mathbf{r}[\mathbf{D}_{\mathrm{i}}] = \mathbf{r}_{\mathrm{i}}$ .

3. Let A be a subset of $\{D_{1}, D_{2}, \ldots, D_{i}\}$ , r[A] (or equivalently, r.A) is a tuple containing only those components specified by A; r[\~A] denotes a tuple consisting of all components not in A.

Definition. Given the n-tuple $\mathbf{r} = \langle \mathbf{r}_1, \mathbf{r}_2, \ldots, \mathbf{r}_n \rangle$ and the m-tuple $s = \langle s_1, s_2, \ldots, s_m \rangle$ , the concatenation of $\mathbf{r}$ with $s$ is the $(n + m)$ -tuple $r^s s = \langle r_1, r_2, \ldots, r_n, s_1, s_2, \ldots, s_m \rangle$ .

Definition. Two sets of attributes are said to be union-compatible if they are of the same size and if the corresponding attributes have the same domain specification (data type). Two relations are said to be union-compatible if their attributes are union-compatible.

The first three relational operators we consider are the set operations of union, intersection, and difference. These operators are defined for union-compatible relations as follows. The union of two relations R and S, denoted R UNION S, is the set of tuples belonging to either R or S or both. The intersection of the two relations, R INTERSECTION S, consists of those tuples belonging to both R and S. Finally, the set of tuples belonging to R and not to S defines the difference between R and S, R DIFFERENCE S.

The next group of relational operators are used to derive any subset of a given relation. The projection operator, for example, performs a vertical subsetting of a table by discarding certain columns. In the process any duplicate tuples in the projected relation are also eliminated. More formally, the projection of relation R on the attribute list A is defined as:

$$
\underline {{\text { PROJECTION }}} _ {[ \mathrm{A} ]} (\mathrm{R}) = \{\mathrm{r} [ \mathrm{A} ] | \mathrm{rELM} _ {-} \mathrm{OF} \mathrm{R} \}.
$$

The selection operator is used to get tuples from the database relations that satisfy a propositional calculus predicate. The selection predicate consists of simple conditions of the form $\{A\ theta\ c\}$ combined with logical connectives, where A is an attribute of the relation and c is a constant value from the domain of the attribute. In addition, it is possible to specify a condition involving two compatible attributes of the same relation, e.g., A theta B. More formally, the selection on relation R using the selection predicate F is defined as:

$$
\text { SELECTION } _ {[ \mathrm{F} ]} (\mathrm{R}) = \{\mathrm{r} | (\mathrm{rELM} _ {-} \mathrm{OF} \mathrm{R}) \text { AND } \mathrm{F} (\mathrm{r}) \}.
$$

It is also possible to obtain a subset of a relation based on a qualification involving another relation. For example, when a user wants to obtain those tuples in a relation R whose value for a column (A) also appears (or does not appear) in a column (B) of a second relation S. These attributes, i.e., columns A and B, must be union-compatible. The restriction (semijoin) operator can express this requirement:

R RESTRICTION $_{[AINB]}$ S =

$$
\overline {{\{\mathrm{r} \mid (\mathrm{rELM} _ {-} \mathrm{OF} \mathrm{R}) \text {AND} (\mathrm{r} [ \mathrm{A} ] \mathrm{ELM} _ {-} \mathrm{OFPROJECTION} _ {[ \mathrm{B} ]} (\mathrm{S})) \}}}, \text {or}
$$

R RESTRICTION[ANOTINB] S =

$$
\overline {{\{\mathrm{r} \mid (\mathrm{rELM} _ {-} \text { OF } \mathrm{R}) \text { AND } (\mathrm{r} [ \mathrm{A} ] \mathrm{N} _ {-} \text { ELM} _ {-} \text { OF } \text { PROJECTION } _ {[ \mathrm{B} ]} (\mathrm{S})) \}}}.
$$

Consider now a different data selection problem such as “Find those subtuples in relation R whose associated set of values for attribute A (the ith domain of relation R) contains every distinct value in column B of relation S”. In the relational algebra, this operation is performed by the division operator:

$$
\mathrm{R} \underline {{\text { DIVISION }}} _ {[ \mathrm{A/B} ]} \mathrm{S} =
$$

$$
\overline {{\{\mathrm{r} [ \tilde {\mathrm{A}} ] | (\mathrm{r} \text { ELM\_OF } \mathrm{R}) \text { AND } (\mathrm{F} _ {-} \text { ALL } \mathrm{b} \text { ELM\_OF } \text { PROJECTION } _ {[ \mathrm{B} ]} (\mathrm{S})}}
$$

$$
\left. \left\langle r _ {1}, r _ {2}, \dots , r _ {i - 1}, b, r _ {i + 1}, \dots , r _ {n} \right\rangle E L M _ {-} O F R) \right\}.
$$

The next relational operator serves to combine data in different relations, in addition to data selection. The join of two relations R and S is constructed by taking each tuple from relation R, determining if it satisfies the join condition with each tuple of S and concatenating them if it does. The join condition is expressed as A theta B, where A and B are, respectively, union-compatible attributes of R and S. More formally, the theta-join operator is defined as:

$$
\mathrm{R~JOIN} _ {[ \mathrm{AthetaB} ]} \mathrm{S} =
$$

$$
\overline {{\{\mathrm{r} ^ {\wedge} \mathrm{s} | (\mathrm{rELM} _ {-} \mathrm{OF} \mathrm{R}) \text { AND } (\mathrm{sELM} _ {-} \mathrm{OF} \mathrm{S}) \text { AND } (\mathrm{r} [ \mathrm{A} ] \text { theta } \mathrm{s} [ \mathrm{B} ]) \}}}.
$$

It should be noted that the relational operators defined above are not independent; that is, some can be expressed in terms of the others. For instance, the theta-join operation can be expressed by the Cartesian product and the selection operations as the following identity indicates:

$$
\mathrm{R} \underline {{\text { JOIN }}} _ {[ \mathrm{AthetaB} ]} \mathrm{S} = \underline {{\text { SELECTION }}} _ {[ \mathrm{AthetaB} ]} (\mathrm{R} \times \mathrm{S}).
$$

In fact, it can be shown that an independent set of relational operators (in terms of which all other operations can be expressed) consists of only five operators: union, difference, Cartesian product, selection, and projection [2,12,24]. In Figure 1 we give the somewhat more complex equivalent expressions for the restriction operation.

For economy of thought and expression, we introduce here the following relational operation to be used in our algorithm. Suppose R(A, B, C) and S(X, Y, Z) are relations such that attribute lists A and B are union-compatible with, respectively, Y and Z. Let THETA be one of the following comparison operators: EQUALS, DOES NOT CONTAIN, and IS NOT IN. The Grouped Generalized Division of relation R, grouped by A, on B by relation S, grouped by Y, on Z is defined formally by:

$$
\begin{array}{l} \text {R} \underline {{\mathbf {G G D}}} _ {[ (\mathrm{A}) \mathrm{BTHETAZ(Y)} ]} \mathrm{S} = \\ \{\mathrm{r} | (\mathrm{rELM} _ {-} \mathrm{OF} \mathrm{R}) \text {AND} \\ \underline {{(\text {PROJECTION} _ {[ \mathrm{B}})}} (\underline {{\text {SELECTION}}} _ {[ \mathrm{A.EQ.r.A} ]} (\mathrm{R})) \\ \text {THETA} \\ \underline {{\text {PROJECTION} _ {[ Z ]}}} (\underline {{\text {SELECTION}}} _ {[ \mathrm{Y.EQ.r.A} ]} (\mathrm{S}))) \}. \end{array}
$$

In procedural terms, the Grouped Generalized Division operation may be carried out by first grouping (sorting) tuples of relation R on the basis of their value for attribute A. Similarly, the tuples of relation S

![](/api/attachments/WJT5T7A3/fulltext/images/797743547e86ed7f299d0bec8b20f35c6a011c2897c0dbf906c6dbc0cbada6fd.jpg)

b) R(A, B, C) RESTRICTION[A NOT IN Y] S(Y, Z)

![](/api/attachments/WJT5T7A3/fulltext/images/33c5bb83c605b67af5ab57659882abbaff6226ca5b3afe1ff7ce490f7e2f1742.jpg)  
Fig. 1. Restriction operator expressed in terms of other relational operators.

are grouped (sorted) on the basis of their value for attribute Y. Two groups of tuples, one from relation R, and the other from relation S, are said to be matching if they share the same value, respectively, for attributes A and Y. Next, for each group of tuples in relation R (the groups of tuples are distinguished by the fact that each group has a unique value for attribute A) the set of B values is determined. If there is a matching group of tuples in relation S, then the set of Z values appearing in that group is also determined. Now, if and only if the two sets of values (i.e., B values and Z values) satisfy the set comparison condition specified by THETA, that group of tuples from relation R are passed to the result relation for the Grouped Generalized Division operation. Otherwise, they are filtered out and would not appear in the output relation.

To clarify further, let us give the algebraic formulation of a query with and without the Grouped Generalized Division operator. Consider the following database of suppliers and parts.

S(S#, Sname, Status, City)

P(P#, Pname, Color, Weight)

$\overline{\mathrm{SP(S\#, P\#, QTY)}}$

$\mathrm{SYP}(\mathrm{S}\# ,\mathrm{Year},\mathrm{P}\#)$

The relation SYP maintains historical information by recording for each year the types of parts (part numbers) supplied by the various suppliers. Sample data values for the following two subsets of relation SYP corresponding to the years 1980 and 1972 are depicted in Figure 2:

SYP80 := SELECTION[Year.EQ.1980] (SYP), and

SYP72 := $\overline{\text{SELECTION}}_{[\text{Year.EQ.1972}]}$ (SYP).

To list the supplier numbers for those suppliers who supplied in 1980 exactly the same parts which they supplied in 1972, we can pose the following sequence of algebraic operations:

Temp1 := PROJECTION $_{[S\#, P\#]}$ (SYP80)
Temp2 := PROJECTION $_{[S\#, P\#]}$ (SYP72)

<table><tr><td>SYP80</td><td>SYP72</td></tr><tr><td>S1 1980 P1</td><td>S1 1972 P1</td></tr><tr><td>S1 1980 P2</td><td>S1 1972 P2</td></tr><tr><td>S1 1980 P3</td><td>S1 1972 P3</td></tr><tr><td>S1 1980 P5</td><td>S1 1972 P4</td></tr><tr><td></td><td>S1 1972 P5</td></tr><tr><td>S2 1980 P1</td><td>S2 1972 P1</td></tr><tr><td>S2 1980 P2</td><td>S2 1972 P2</td></tr><tr><td>S2 1980 P3</td><td></td></tr><tr><td>S3 1980 P1</td><td>S3 1972 P2</td></tr><tr><td>S4 1980 P1</td><td>S4 1972 P1</td></tr><tr><td>S4 1980 P2</td><td>S4 1972 P2</td></tr><tr><td>S5 1980 P5</td><td></td></tr><tr><td></td><td>S6 1972 P5</td></tr><tr><td></td><td>S6 1972 P6</td></tr></table>

Fig. 2. Sample data values for two subsets of relation SYP.

Temp3 := Temp1 DIFFERENCE Temp2

$$
\text { Temp4 } := \text { Temp2   DIFFERENCE   Temp1 }
$$

$$
\text { Temp5 } := \text { Temp3 } \overline {{\text { UNION   Temp4 }}}
$$

$$
\text { Temp6 } := \text { SYP80 } \overline {{\text { RESTRICTION }}} _ {[ \text { S } \# \text { NOTINS } \# ]} \text { Temp5 }
$$

$$
\text { Result } := \text { PROJECTION } _ {[ S \# ]} (\text { Temp6 }),
$$

or equivalently using the Grouped Generalized Division operator:

Temp1 := SYP80 $\underline{\mathbf{GGD}}_{[(S#)P#EQUALSP#(S#)]}$ SYP72

$$
\text { Result } := \text { PROJECTION } _ {[ S \# ]} (\text { Temp1 }).
$$

The family of operators (one for each interpretation of THETA) defined by the Grouped Generalized Division operation can be expressed in terms of the other relational operators as follows:

![](/api/attachments/WJT5T7A3/fulltext/images/10d2b5013d8d2b78a65cefcea14647574f13f0d024c7623064790b3c337067e1.jpg)

where, $REL_{1} = RESTRICTION_{[AINY]}$ (S), and $OP_{1}$ , $OP_{2}$ , $REL_{2}$ , and $REL_{3}$ are defined for each interpretation of THETA as follows:

EQUALS

$$
\mathrm{OP} _ {1} = \text { RESTRICTION } _ {[ \text { ANOTINY } ]}
$$

$$
\mathrm{OP} _ {2} = \text { SYMMETRIC   DIFFERENCE }
$$

$$
\mathrm{REL} _ {2} = \overline {{\text { PROJECTION }}} _ {[ \mathrm{A}, \mathrm{B} ]} (\mathrm{R})
$$

$$
\mathrm{REL} _ {3} = \overline {{\text { PROJECTION } _ {[ Y , Z ]}}} (\mathrm{S})
$$

DOES NOT CONTAIN

$$
\mathrm{OP} _ {1} = \underline {{\text { RESTRICTION }}} _ {[ \mathrm{AINY} ]}
$$

$$
\mathrm{OP} _ {2} = \text { DIFFERENCE }
$$

$$
\mathrm{REL} _ {2} = \overline {{\text { PROJECTION }}} _ {[ Y, Z ]} (S)
$$

$$
\mathrm{REL} _ {3} = \overline {{\text { PROJECTION }}} _ {[ \mathrm{A}, \mathrm{B} ]}\tag{R}
$$

IS NOT IN

$$
\mathrm{OP} _ {1} = \underline {{\text { RESTRICTION }}} _ {[ \mathrm{AINY} ]}
$$

$$
\mathrm{OP} _ {2} = \text { DIFFERENCE }
$$

$$
\mathrm{REL} _ {2} = \overline {{\text { PROJECTION }}} _ {[ \mathrm{A}, \mathrm{B} ]} (\mathrm{R})
$$

$$
\mathrm{REL} _ {3} = \overline {{\text { PROJECTION }}} _ {[ Y, Z ]}\tag{S}
$$

where, the symmetric difference of two sets R and S is defined as:

$$
R \text { SYMMETRIC   DIFFERENCE } S = (R \text { DIFFERENCE } S) \text { UNION } (S \text { DIFFERENCE } R).
$$

A close derivative of Grouped Generalized Division, which will also be used in our algorithm, is the following operation which we denote by GD. Suppose R(A, B, C) and S(W, X, Y, Z) are relations such that attribute lists B and Z are union-compatible. Then,

R $\mathbf{G}\mathbf{D}_{[(\mathrm{A})\mathrm{B}\mathrm{T}\mathrm{H}\mathrm{E}\mathrm{T}\mathrm{A}\mathrm{Z}]}$ S =

$\overline{\{r\}}(\text{R ELM\_OF R})$ AND

$$
(\text { PROJECTION } _ {[ \mathrm{B} ]} (\text { SELECTION } _ {[ \mathrm{A.EQ.r.A} ]} (\mathrm{R}))
$$

THETA

$$
\text { PROJECTION } _ {[ Z ]} (S)) \}.
$$

This operation can be expressed in terms of the Grouped Generalized Division operation, GGD, as follows:

![](/api/attachments/WJT5T7A3/fulltext/images/6fd8c28a157e2b674c40f35f6fbd9a8f366934e74a68c34d0c8a3cc64352b1cf.jpg)

## 3. A Guided Tour of the Conversion Algorithm

SQL and its close derivatives are mapping oriented languages $[1,8,9,11,13]$ . The concept of mapping is best explained by example. Suppose the user wants to retrieve the names of “LONDON” suppliers who supply part “P2”. The desired values for the attribute Sname are found in the tuples of relation S which have the known value “LONDON” for the attribute City and are further qualified by the condition that their S# value must be in the set of supplier numbers who supply part “P2”. This latter set can be made known by another mapping which retrieves the S# value from the tuples of relation SP which have the known value “P2” for the attribute P#. This formulation of the request is expressed in SQL as:

```sql
SELECT Sname
FROM S
WHERE (City = "LONDON")
AND
(S# IN (SELECT S#
FROM SP
WHERE P# = "P2")).
```

(Q1)

For the purposes of this paper, an SQL mapping, or query block, has the general form:

SELECT select-list

FROM from-list

WHERE where-predicate

As the example above illustrates, SQL permits queries to be nested. That is, a query can be used in the where-predicate of an SQL query block. Such a nested query is referred to as a subquery and may or may not involve an interblock reference.

To convert an SQL query into an equivalent algebraic expression we require that all attribute names in the query be first properly qualified. This can readily be done by assigning a unique number to each query block (signified by a SELECT clause); distinguishing the relations named in the from-list with the block number; and qualifying the attribute names in the block by the name of the relation from which they come. The result of such a renaming process for our example query is:

SELECT S1.Sname

FROM S1

AND

(S1.S# IN (SELECT SP2.S#

FROM SP2

We proceed to construct the equivalent algebraic expression for Q1 by considering each conjunct of the where-predicate separately. That is, the algebraic tree for the query is viewed to consist of an intersection operator for the root node and left and right subtrees corresponding to the original query with the conjuncts of the where-predicate separated. (Figure 3a)

The heart of our algorithm is reduction rules for SQL query blocks containing a simple where-predicate. For the left query block above, the predicate is of the form “attribute-list theta value”, where theta denotes one of the arithmetic comparison operators. Such query blocks are reduced to:

PROJECTION $_{[select-list]}$ (SELECTION $_{[attribute-list theta value]}$ (F)), where F denotes the Cartesian product of relations in the from-list. (Figure 3b)

For the right query block above, the predicate is of the form “attribute-list IN subquery”. In this case, the query block is reduced to:

Finally, the remaining subquery is reduced resulting in the complete tree shown in Figure 4 below.

INTERSECTION  
![](/api/attachments/WJT5T7A3/fulltext/images/cf89e8eda932e798a6ef35408918dc66053907e904c629780a14a0b20bc70d99.jpg)  
a)

SELECT S1.Sname
FROM S1
WHERE S1.S# IN
(SELECT SP2.S#
FROM SP2
WHERE SP2.P# = "P2")

b)

PROJECTION[S1.Sname]
    |
    SELECTION[S1.City="LONDON"]
    |
    S1

c)

PROJECTION[S1.Sname]
    |
    SELECTION[S1.City="LONDON"]
    |
    S1

INTERSECTION  
![](/api/attachments/WJT5T7A3/fulltext/images/82297afe0177e5ec6e7c90a95eeabae2878662e5c2199e2171d9a70e763cc68a.jpg)

SELECT SP2.S#
FROM SP2
WHERE SP2.P# = "P2"

Fig. 3. Stage in the reduction of Q1.

## INTERSECTION

![](/api/attachments/WJT5T7A3/fulltext/images/e2898b2654440df9a73b7fef4b1d8f2ff175fbac7d5df31ee2278e445a8aca9e.jpg)  
Fig. 4. The equivalent algebraic tree for Q1.

The request to list the names of “LONDON” suppliers who supply part “P2” can also be formulated in the following, decidedly different manner.

```sql
SELECT Sname
FROM S
WHERE (City = "LONDON")
AND
("P2" IN (SELECT P#
FROM SP
WHERE S# = S.S#)).
```

(Q2)

Here we have an example of a subquery involving an interblock reference. The initial steps in the reduction of this query block are similar to the previous case. (Figure 5a)

In this case, the right query block has a predicate of the form “value IN subquery”. The semantics of SQL require that the subquery in such a predicate be correlated, that is, involve a reference to a relation named in the from-list of the main block. We reduce such queries to:

a)  
![](/api/attachments/WJT5T7A3/fulltext/images/c07454e1d25b9253f5d8fe4378b3bcc5920626944098dbc04ace17dde88380af.jpg)

b)  
![](/api/attachments/WJT5T7A3/fulltext/images/9f9c3a2a95ef64b73e6bc9508b3bb46d271a12b0881184fab3a8269d2366aee6.jpg)

c)  
![](/api/attachments/WJT5T7A3/fulltext/images/db541b06fe319f3e3246e4a10ce86d09cb7882caab7dd0455459d55639de2185.jpg)  
Fig. 5. Stages in the reduction of Q2.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
PROJECTION $_{[select-list]}$ 
(SELECTION $_{[value=subquery-select-list]}$  (F2 × modified-subquery)),
</div>

where F2 denotes the Cartesian product of relations in the from-list excluding the referenced relation; and modified-subquery represents the subquery with the attributes of the referenced relation appearing in the select-list of the main block appended to its select-list and the referenced relation included in its from-list. (Figure 5b)

Finally, the remaining subquery which has a predicate of the form “attribute-list theta attribute-list” is reduced to:

PROJECTION[select-list]

(SELECTION[attribute-list theta attribute-list] (F)). (Figure 5c)

## 4. Reduction Rules for Simple SQL Query blocks

We now present our reduction rules for SQL query blocks involving a simple where-predicate. A where-predicate is said to be simple if it is not the logical and, or the logical or of predicates. An SQL query block is called simple if its associated where-predicate is simple.

Proposition. The following are the only types of simple where-predicate permitted in SQL. Furthermore, given a simple SQL query block of the form:

SELECT select-list

FROM from-list

WHERE simple-where-predicate,

the following reduction rules, one for each type of predicate, reduce the level of nesting by one while preserving the meaning of the query.

(a) attribute-list theta value

where attribute-list is a set of attributes belonging to the same relation, and theta is one of the arithmetic comparison operators: $<, <=, >, >=, < >$ , and = (equality).

RULE: PROJECTION[SL] (SELECTION[attribute-list theta value] (F)),

where SL is the select-list, and F is the Cartesian product of the relations in the from-list.

(b) attribute-list theta attribute-list

RULE: PROJECTION[SL]

(SELECTION[attribute-list theta attribute-list] (F)).

(c) attribute-list theta uncorrelated-subquery

RULE: PROJECTION[SL] (SELECTION[attribute-list theta sl] (F × E)),

where sl is the select-list of, and E is the algebraic expression for, the uncorrelated-subquery.

(d) attribute-list IN uncorrelated-subquery

RULE: PROJECTION[SL] (SELECTION[attribute-list = sl] (F × E)).

(e) attribute-list NOT IN uncorrelated-subquery

RULE: PROJECTION[SL]

where R1 is the relation to which attribute-list belongs, and $U_{R1}$ denotes the attributes of R1. F1 is the Cartesian product of the relations in the from-list excluding R1.

(f) value theta correlated-subquery

$$
\text { RULE: } \underline {{\text { PROJECTION }}} _ {[ \mathrm{SL} ]} (\underline {{\text { SELECTION }}} _ {[ \text { value   theta   sl } ]} (\mathrm{F2} \underline {{\times}} \mathrm{M1})).
$$

Let R be the referenced relation and $R_{SL}$ denote the attributes of R appearing in SL. F2 is the Cartesian product of the relations in the from-list excluding R, and M1 is the algebraic expression for the correlated-subquery which is modified by appending $R_{SL}$ to its select-list and including R in its from-list.

(g) value IN correlated-subquery

$$
\text { RULE:   PROJECTION } _ {[ \mathrm{SL} ]} (\text { SELECTION } _ {[ \text { value } = \mathrm{sl} ]} (\mathrm{F2} \times \mathrm{M1})).
$$

(h) attribute-list theta correlated-subquery

$$
\underline {{\text { RULE: }}} \underline {{\text { PROJECTION } _ {[ S L ]}}} (\underline {{\text { SELECTION } _ {[ a t t r i b u t e - l i s t t h e t a s l ]}}} (F 2 \times M 2)).
$$

Let R1 be the relation to which attribute-list belongs. R1 may or may not be the same as the referenced relation, R. M2 is the algebraic expression for the correlated-subquery which is modified by appending $R_{SL}$ (or the union of $R_{SL}$ and attribute-list, if R is the same as R1) to its select-list and including R in its from-list.

(i) attribute-list IN correlated-subquery

$$
\text { RULE: } \underline {{\text { PROJECTION }}} _ {[ \mathrm{SL} ]} (\underline {{\text { SELECTION }}} _ {[ \text { attribute - list   =   sl } ]} (\mathrm{F2} \times \mathrm{M2})).
$$

(j) attribute-list NOT IN correlated-subquery

$$
\underline {{\text { RULE: }}} \underline {{\text { PROJECTION }}} _ {[ \mathrm{SL} ]} (\text { F } \underline {{\text { GGD }}} _ {[ (\mathrm{U} _ {\mathrm{R}}) \text { attribute - list   NOT   IN   sl } (\mathrm{U} _ {\mathrm{R}}) ]} \text { M3 }),
$$

where $U_{R}$ denotes the attributes of the referenced relation, and M3 is the algebraic expression for the correlated-subquery which is modified by appending $U_{R}$ to its select-list and including R in its from-list.

(k) value NOT IN correlated-subquery

$$
\underline {{\text { RULE: }}} \underline {{\text { PROJECTION }}} _ {[ \mathrm{SL} ]} (\mathrm{F2} \underline {{\times}} (\mathrm{M3} \underline {{\mathbf {G D}}} _ {[ (\mathrm{U} _ {\mathrm{R}}) \mathrm{sl} _ {1} \text { DOESNOTCONTAIN } \mathrm{sl} _ {2} ]} \mathrm{E}).
$$

The set of constant(s) specified by value is treated as a query block of the form: SELECT attribute-id FROM set-id, henceforth referred to as the uncorrelated subquery. $sl_{1}$ and $sl_{2}$ denote, respectively, the select-list of the correlated and uncorrelated subqueries. E is the algebraic expression for the uncorrelated subquery.

(1) EXISTS(correlated-subquery)

$$
\underline {{\text { RULE: }}} \underline {{\text { PROJECTION } _ {[ \mathrm{SL} ]}}} (\text { F   RESTRICTION } _ {[ \mathrm{U} _ {\mathrm{R}} \text { IN } \mathrm{U} _ {\mathrm{R}} ]} \text { M3 }),
$$

where $U_{R}$ denotes the attributes of the referenced relation, R, F is the Cartesian product of the relations in the from-list, and M3 is the algebraic expression for the correlated-subquery which is modified by appending $U_{R}$ to its select-list and including R in its from-list.

(m) NOT EXISTS(correlated-subquery)

$$
\underline {{\text { RULE: }}} \underline {{\text { PROJECTION } _ {[ S L ]}}} (\text { F   RESTRICTION } _ {[ U _ {R} \text { NOT   IN } U _ {R} ]} \text { M3 }).
$$

(n) attribute-list theta ANY correlated-subquery

RULE: Treat the predicate as EXISTS(SELECT \* FROM fl WHERE wp AND attribute-list theta sl), where fl is the from-list, wp is the where-predicate, and sl is the select-list of the correlated subquery.

(o) attribute-list theta ALL correlated-subquery

RULE: Treat the predicate as NOT EXISTS(SELECT \* FROM fl WHERE wp AND NOT attribute-list theta sl).

We end this section with two examples illustrating some of the reduction rules which were not demonstrated in the previous section.

a)  
![](/api/attachments/WJT5T7A3/fulltext/images/f95ae3e08b1ee219f2ca27d63cc3763d73cdb96b1a8fb9c245776b98d519df91.jpg)

b)  
![](/api/attachments/WJT5T7A3/fulltext/images/985ad38c852b6f80edbcc17e993caf5cdb7939d0386239727b4d38007fae3443.jpg)  
where, $U_{S1} = \{S1.S\# , S1.Sname, S1.Status, S1.City\}$

Fig. 6. Stages in the reduction of Q3.  
![](/api/attachments/WJT5T7A3/fulltext/images/22f904932acef58fe93739348cda5cd47d69d690d6f1d046cfb6e55c6a1d54c4.jpg)  
where, $U_{S1} = \{S1.S\# , S1.Sname, S1.Status, S1.City\}$

Fig. 7. The equivalent algebraic tree for Q3.

```sql
SELECT S1.Sname, SP1.P#
FROM S1, SP1
WHERE S1.S# = SP1.S#
AND
SP1.P# NOT IN (SELECT SP2.P#
FROM SP2
WHERE SP2.S# <> S1.S#).

The reduction of this query is illustrated in Figures 6 and 7.
Example 2. Consider the employee relation E(E#, Ename, Salary, Manager#), and the request to list the names of employees earning more than the manager of their manager. This query may be formulated as:
SELECT E1.Ename
FROM E1
```

Example 1. Suppose we are interested in suppliers who supply a part that is not supplied by any other supplier. Specifically, we wish to know the names of such suppliers along with the part number of the part which is exclusively supplied by them. This request can be formulated in SQL by:

```sql
PROJECTION[E1. Ename]
SELECTION[E1.Salary > E2.Salary]

SELECT E2.Salary, E1. Ename, E1.Salary
FROM E2, E1
WHERE E2.E# = ( SELECT E3.Manager#
FROM E3
WHERE E3.E# = E1.Manager# )
```

```txt
b)
PROJECTION[E1. Ename]
SELECTION[E1.Salary > E2.Salary]

PROJECTION[E2.Salary, E1. Ename, E1.Salary]
SELECTION[E2.E# = E3.Manager#]
X
E2
SELECT E3.Manager#, E1. Ename, E1.Salary
FROM E3, E1
WHERE E3.E# = E1.Manager#
```  
Fig. 8. Stages in the reduction of Q4.

```txt
PROJECTION[E1. Ename]
SELECTION[E1.Salary > E2.Salary]

PROJECTION[E2.Salary, E1. Ename, E1.Salary]
SELECTION[E2.E# = E3.Manager#]

X
E2

PROJECTION[E3.Manager#, E1. Ename, E1.Salary]
SELECTION[E3.E# = E1.Manager#]

X
E3 E1
```

Fig. 9. The equivalent algebraic tree for Q4.  
```txt
WHERE E1.Salary > (SELECT E2.Salary FROM E2
WHERE E2.E# = (SELECT E3.Manager# FROM E3
WHERE E3.E# = E1.Manager#)).
```

(Q4)

The reduction of Q4 to its equivalent algebraic tree is shown in Figures 8 and 9.

## 5. The Algorithm

The following is our recursive algorithm for converting a semantically meaningful SQL query into an equivalent algebraic expression. The input to the algorithm is an SQL query, without an ORDER BY or a GROUP BY clause, in which no aggregate functions are used. The output of the algorithm is a semantically equivalent algebraic tree which may contain the Grouped Generalized Division (GGD), Generalized Division (GD), and/or the RESTRICTION operators. In a postprocessing phase these operators in the tree are expanded in terms of the operators UNION, INTERSECTION, DIFFERENCE, ×, SELECTION, and PROJECTION as already described.

STEP 1. If the query is not of the form “query $_{1}$ UNION query $_{2}$ ” go to step 2. Otherwise, return the tree shown below, where tree $_{1}$ and tree $_{2}$ represent the algebraic trees corresponding to query $_{1}$ and query $_{2}$ .

![](/api/attachments/WJT5T7A3/fulltext/images/edc64ed4f00a6a285d1af58890d5067f648db2cf10d77dc1e94611447986cc16.jpg)

STEP 2. We reach here with query blocks of the general form:

SELECT select-list

FROM from-list

WHERE where-predicate.

If the query block does not contain the WHERE clause go to step 4. If the where-predicate is simple go to step 3. (A theta-predicate that is preceded by NOT is replaced by its logical complement.) Otherwise, let the where-predicate be of the form:

$$
\left(\mathrm{W} _ {1 1} \text { OR } \mathrm{W} _ {1 2} \text { OR } \dots \text { OR } \mathrm{W} _ {1 p _ {1}}\right) \text { AND }
$$

$$
\left(\mathrm{W} _ {2 1} \text { OR } \mathrm{W} _ {2 2} \text { OR } \dots \text { OR } \mathrm{W} _ {2 p _ {2}}\right) \text { AND }
$$

$$
\left(\mathrm{W} _ {\mathrm{q} 1} \text { OR } \mathrm{W} _ {\mathrm{q} 2} \text { OR } \dots \text { OR } \mathrm{W} _ {\mathrm{qp} _ {\mathrm{q}}}\right),
$$

where $W_{ij}$ is a simple where-predicate. Return the tree represented by the following algebraic expression:

$$
\left(\mathrm{WT} _ {1 1} \text {UNION} \mathrm{WT} _ {1 2} \text {UNION} \dots \text {UNION} \mathrm{WT} _ {1 p _ {1}}\right)
$$

$$
\left(\mathrm{WT} _ {2 1} \underline {{\text { U   N   I   O   N }}} \mathrm{WT} _ {2 2} \underline {{\text { U   N   I   O   N }}} \dots \underline {{\text { U   N   I   O   N }}} \mathrm{WT} _ {2 p _ {2}}\right)
$$

$$
\left(\mathrm{WT} _ {\mathrm{q} 1} \underline {{\text { U   N   I   O   N }}} \mathrm{WT} _ {\mathrm{q} 2} \underline {{\text { U   N   I   O   N }}} \dots \underline {{\text { U   N   I   O   N }}} \mathrm{WT} _ {\mathrm{qp} _ {\mathrm{q}}}\right),
$$

where $WT_{ij}$ denotes the algebraic tree for the following SQL query block:

SELECT select-list

FROM from-list

WHERE $W_{ij}$ .

STEP 3 We reach here with query blocks involving a simple where-predicate. Apply the appropriate reduction rule from the PROPOSITION given in the previous section.

STEP 4. We reach here with query blocks of the general form:

SELECT select-list

FROM from-list.

Return the tree represented by the following algebraic expression:

PROJECTION[select-list] (Cartesian product of relations in from-list).

## 6. Comparison with Related Research

There have been only a few other works on translation of SQL queries. Luk and Kloster [20] describe a system which, when given a SEQUEL2 query, will display its meaning in English. Kim [18] proposed transformations in SEQUEL2 for the purpose of converting nested queries into simpler ones. Ceri and Gottlob [7] and Dadashzadeh [10] provide the only algorithms for converting SEQUEL2 queries into relational algebra. Ullman [24] gives an algorithm for converting from QUEL to relational algebra. Given that QUEL does not have many of the complexities of SQL, that conversion algorithm is rather simple.

Our work is similar to $[20]$ , $[10]$ , and $[7]$ in its syntax-directed approach to translation of SQL queries as well as providing the definition of the semantics of SQL. It is similar, in spirit, to $[18]$ and $[7]$ in classifying the possible types of nesting in SQL and of associating a reduction rule to each type. Our algorithm is more comprehensive than those presented by Dadashzadeh $[10]$ and Kim $[18]$ . It is limited, when compared to $[7]$ , by not addressing aggregate functions. However, the use of two major phases (SEQUEL2 to restricted SEQUEL2 to relational algebra) in the translation algorithm of Ceri and Gottlob $[7]$ corresponds to a significant loss of efficiency when compared to our single-pass algorithm.

## 7. Summary and Suggestions for Future Research

Amongst the many data manipulation languages that have been proposed for the relational data model, SQL has received the most attention. SQL is a block-structured language based on a mixture of relational calculus and relational algebra that has become the standard language for relational database manipulation. SQL's English-like commands and template-like query block structure make it easy for the new user to begin to use the language; and its nesting of query blocks permits the formulation of complex queries by means of stepwise refinement.

In a typical implementation of a nested SQL query, query blocks are evaluated in the implied sequential order (from inside out) without any attempt at global reorganization. For certain queries (e.g., Q2, Q3, and Q4 in this paper), those in which an inner block references an attribute value belonging to a candidate tuple obtained in an outer block, this processing order cannot be strictly applied. These queries are evaluated by tuple substitution $[25]$ , that is, the inner block is re-evaluated for every candidate tuple of the referenced outer block $[5,18,22]$ . Unfortunately, this can sometimes be very inefficient $[10,18]$ .

Because of the large body of techniques developed for optimizing the evaluation of relational algebra expressions $[3,6,10,15,17,23–26]$ , and because of the opportunities afforded by data driven relational algebra database machines $[17]$ , it seems appropriate to consider the translation of an SQL query into an algebraic expression as the first step in the implementation of SQL-like languages.

To that end, we have given a single-pass algorithm for converting an arbitrary query from a large subset of SQL into an equivalent algebraic expression. Two other important applications of our algorithm are in proving equivalence between SQL queries and in allowing DBMSs that internally employ relational algebra to support an SQL user interface without the necessity of developing a separate SQL interpreter/compiler.

We note in conclusion that the limitation of our algorithm presents a promising avenue for future research. Specifically, our restricting the relevant SQL queries to those without aggregate functions, stems from lack of generally accepted guidelines for incorporating aggregate functions into relational algebra. However, there exist a number of proposals for extending relational algebra with features to support aggregate functions $[7,19,21]$ . We expect that adopting any one of the proposals should make it possible to extend our algorithm to encompass arbitrary SQL queries.

## References

[1] Ageloff, R. A Primer on SQL. St. Louis, MO: Times Mirror/Mosby, 1988.

[2] Aho, A.V., and Ullman J.D. Universality of data retrieval languages. Proceedings of the Sixth ACM Symposium on Principles of Programming Languages, (1979), 110–120.

[3] Aho, A.V., Sagiv, Y., and Ullman, J.D. Efficient optimization of a class of relational expressions. ACM Transactions on Database Systems, 4, 4 (December 1979), 435–454.

[4] American National Standards Institute, Database Language SQL, Document ANSI X3.135, 1986.

[5] Astrahan, M.M., and Chamberlin, D.D. Implementation of a structured English query language. Communications of the ACM, 18, 10, (October 1975), 580–587.

[6] Blasgen, M.W., and Eswaran, K.P. Storage and access in relational databases. IBM Systems Journal, 16, 4 (1977), 363–377.

[7] Ceri, S., and Gottlob, G. Translating SQL into relational algebra: optimization, semantics, and equivalence of SQL queries. IEEE Transactions on Software Engineering, 11, 4 (April 1985), 324–345.

[8] Chamberlin, D.D., et al. SEQUEL2: a unified approach to data definition, manipulation, and control. IBM Journal of Research & Development, 20, 6, (November 1976), 560–575.

[9] Chamberlin, D.D., et al. A history and evaluation of System R. Communications of the ACM, 24, 10 (October 1981).

[10] Dadashzadeh, M. On estimation of the cost of relational query evaluation plans. Unpublished Ph.D. dissertation, University of Massachusetts, Amherst, August 1985.

[11] Date, J.C. A guide to DB2. Reading, MA: Addison-Wesley, 1984.

[12] Date, C.J. An Introduction to Database Systems: Volume I. Reading, MA: Addison-Wesley, 1985.

[13] Date, C.J. A Guide to the SQL Standard. Reading, MA: Addison-Wesley, 1987.

[14] Furtado, A., and Kerschberg, L. An algebra of quotient relations. Proceedings of ACM SIGMOD International Conference on Management of Data, (August 1977), 1–7.

[15] Hall, P.A.V. Optimization of single expressions in a relational database system. IBM Journal of Research & Development, 20, 3 (1976), 244–257.

[16] International standards Organization, Database Language SQL Addendum-2, Document ISO/TC97/SC21/WG3 N143, 1986.

[17] Jarke, M., and Koch, J. Query optimization in database systems. ACM Computing Surveys, 16, 2 (June 1984), 111–152.

[18] Kim, W. On optimizing an SQL-like nested query. ACM Transactions on Database Systems, 7, 3 (September 1982), 443–469.

[19] Klug, A. Equivalence of relational algebra and relational calculus query languages having aggregate functions. Journal of the ACM, 29, 3 (July 1982), 699–717.

[20] Luk, W.S., and Kloster, S. ELFS: English language from SQL. ACM Transactions on Database Systems, 11, 4 (December 1986), 447–472.

[21] Ozsoyoglu, G., Ozsoyoglu, Z.M., and Matos, V. Extending relational algebra and relational calculus with set-valued attributes and aggregate functions. ACM Transactions on Database Systems, 12, 4 (December 1987), 466–592.

[22] Selinger, P.G., et al. Access path selection in a relational database management system. Proceedings of ACM SIGMOD International Conference on Management of Data, (May 1979), 23–34.

[23] Smith, J.M., and Chang, P.Y. Optimizing the performance of a relational algebra database interface. Communications of the ACM, 18, 10 (October 1975), 568–579.

[24] Ullman, J.D. Principles of Database Systems. Rockville, MD: Computer Science Press, 1982.

[25] Wong, E., and Youssefi, K. Decomposition: a strategy for query processing. ACM Transactions on Database Systems, 1, 3 (September 1976), 223–241.

[26] Yao, S.B. Optimization of query evaluation algorithms. ACM Transactions on Database Systems, 4, 2 (June 1979), 133–155.
