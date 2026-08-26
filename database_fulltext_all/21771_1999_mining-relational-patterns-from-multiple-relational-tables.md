---
otero_id: 21771
otero_key: "A2NUC7JJ"
title: "Mining relational patterns from multiple relational tables"
authors: "Maytal Saar Tsechansky; Nava Pliskin; Gadi Rabinowitz; Avi Porath"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00043-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mining relational patterns from multiple relational tables

Maytal Saar Tsechansky <sup>a,)</sup>, Nava Pliskin <sup>b,1</sup>, Gadi Rabinowitz <sup>b,2</sup>, Avi Porath <sup>c,3</sup>

Department of Information Systems, Leonard N. Stern School of Business, New York UniÕersity, New York, NY, USA <sup>b</sup> Department of Industrial Engineering and Management, Ben-Gurion UniÕersity of the NegeÕ, Beersheba, Israel Department of Medicine, Ben-Gurion UniÕersity of the NegeÕ, Soroka Medical Center, Beersheba, Israel

## Abstract

In this paper, we present the concept of relational patterns and our approach to extract them from multiple relational tables. Relational patterns are analogous to frequent itemsets extracted by the Apriori algorithm R. Agrawal, H. Mannila, R. Srikant, H. Toivonen, A.I. Verkamo, Advances in Knowledge Discovery and Data Mining, AAAI Press, 1995. in the case<sup>x</sup> of a single table. However, for the multiple relational tables, relational patterns capture co-occurrences of attributes as well as the relationships between these attributes, which are essential to avoid information loss. We describe our experiences from a test-bed implementation of our approach on a real hospital’s discharge abstract database. This process raised issues, which were then implemented in order to enhance an analyst’s ability to explore patterns while preventing high diversity and abundance of available data from blurring subtle patterns of interest. Finally, we evaluate the usefulness of relational patterns in the context of the discharge abstract data as well in other possible domains. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Relational tables; Relational patterns; Association rules

## 1. Introduction

Hospitals maintain large administrative databases, which contain demographic information such as age, sex, and clinical information such as diagnoses and medical procedures performed. While these data are collected for administrative data processing, such as accounts receivable and payroll, taking advantage of these data for other value-added purposes is highly desirable. For example, administrative data may be used for quality assurance of medical care, to highlight practices embedded in the organization, or reveal interesting patterns among patients. Such data utilization is especially warranted in the face of harsh competition for limited resources among health care providers, which thrust to the forefront the pursuit for higher quality and lower costs of medical care.

The management of a major medical center in Israel approached the authors with these concerns, expressing growing frustration with the fact that the large databases in the hospital are hardly ever utilized to shed light on clinical or administrative practices within the hospital. Hospital management believed that such utilization of the databases would provide important input for decision making.

The area of Knowledge Discovery in Databases Ž . KDD was defined by Fayyad et al. 9 as the<sup>w</sup> <sup>x</sup> non-trivial process of identifying valid, novel, potentially useful and ultimately understandable patterns from data. As such, it is directly applicable to respond to the concerns above by offering new methods and tools to automatically extract knowledge and analyze useful patterns from databases.

One extensively studied issue in the KDD field is the problem of generating association rules <sup>w</sup> <sup>x</sup> 2,5,12,17 . Association rules seemed to be particularly suitable for incorporation into the hospital’s decision making process since they are expressive and relatively easy to comprehend.

Initially, we employed traditional technologies for extracting frequent itemsets, which are the precursors to association rules 2,3 . However, for reasons de-<sup>w</sup> <sup>x</sup> scribed in Section 4 of this paper, those technologies were ineffective for the current application, which involves multiple data tables. Domshlak et al. 6<sup>w</sup> <sup>x</sup> applied the Apriori algorithm 3 to an application <sup>w</sup> <sup>x</sup> which similarly involves multiple data tables, by first joining those tables. However, our experience showed that joining of tables can result in information distortion and loss see Section 4 .Ž .

This work introduces a new approach for extracting information from data distributed across multiple relational tables. We extract relational patterns, which capture, in addition to co-occurrences of attributes and their values, the relationships between those attributes. These relational patterns are analogous to the frequent itemsets extracted by the Apriori algorithm for a single table. Our bottom-up approach to extract relational patterns utilizes elements of the Apriori algorithm 3 , particularly the large itemsets<sup>w</sup> <sup>x</sup> generation phase, as well as the algorithm to extract sequential patterns suggested by Agrawal and Srikant <sup>w</sup> <sup>x</sup> <sub>4</sub> <sub>.</sub>

Many organizations maintain relational databases, and as relational patterns reliably portray patterns embedded within these databases, relational patterns can be beneficially utilized by organizations to support a variety of efforts from marketing to quality improvement by identifying leads on consumers behavior, flawed practices or other issues depending upon the nature of data collected.

The main contributions of this paper are that:

<sup>Ø</sup> We introduce relational patterns and an algorithm for their extraction;

<sup>Ø</sup> Unlike frequent itemsets 3 , these relational pat- <sup>w</sup> <sup>x</sup> terns are meaningful even in the case of multiple relational tables; and

<sup>Ø</sup> We describe a case study of a prototype to extract relational patterns from a hospital database, and discuss the challenges posed by domain-related issues.

The organization of this paper is as follows. In Section 2, we describe some preliminaries on the Apriori algorithm to extract association rules 3 , and<sup>w</sup> <sup>x</sup> the algorithm to extract sequential patterns proposed by Agrawal and Srikant 4 . In Section 3, we present<sup>w</sup> <sup>x</sup> the database organization for the problem. In Section 4, we discuss the issues posed by multiple relational tables, and in Section 5, we present relational patterns. We describe our approach and algorithm in Section 6. In Section 7, we delineate a test-bed prototype implementing the proposed approach to a real hospital database. We discuss the domain-related challenges posed by the application and the usefulness the patterns extracted. We conclude our study in Section 8.

## 2. Association rules and sequential patterns

The approach presented here employs Apriori algorithm 3 to extract frequent itemsets 2 , as well as <sup>w x</sup> <sup>w x</sup> the algorithm for sequential patterns proposed in Ref. <sup>w</sup> <sup>x</sup> 4 . It is thus helpful to describe the concepts of these algorithms and introduce the terminology that we adopt in this paper.

The Apriori algorithm aims at extracting association rules from a single table. Let $I = \{ i _ { 1 } , i _ { 2 } , \ldots , i _ { m } \}$ be a set of attributes also called items 3 , where anŽ . <sup>w</sup> <sup>x</sup> attribute can take any value from a discrete set of mutually exclusive values. A conjunction of conditions of the form ‘‘attribute <sup>s</sup> value’’ is called an itemset <sup>w</sup> <sup>x</sup> 3 . An association rule is an implication of the form A B, where A and B are mutually exclusive itemsets. For example, the rule Department $\begin{array} { r l } { = } & { { } \cdots \mathrm { E R } ^ { \prime } \ : \cdot } \end{array}$ $\begin{array} { l c l } { { \mathrm { A g e } } } & { { = } } &  { ^ { \cdot \cdot } 6 0 { - } 6 5 ^ { \circ } { } ^ { , } \} } \end{array} $ Length\_of\_ $. \mathrm { S t a y } = ^ { \cdot \cdot } 5 – 7 ^ { , , } \}$ means that a patient at the age of 60–65, who registered at the emergency room, is likely to stay in the hospital for 5–7 days.

Table 3

Let $D = \{ t _ { 1 } , t _ { 2 } , \ldots , t _ { N } \}$ be a relation consisting of N transactions i.e., records . A transactionŽ . t is said to satisfy an itemset if it contains this itemset. An association rule holds on a database D if its support and confidence are greater than some predefined thresholds 3 . The <sup>w</sup> <sup>x</sup> support of a rule, denoted by s, is the percentage of transactions in the database which contain the itemset A<sup>j</sup>B. All itemsets which satisfy the support threshold, called minimum support, are called large itemsets. During the core phase of the algorithm, all large itemsets are generated. The confidence of a rule, denoted by c, is the percentage of transactions which contain A that also contains B <sup>w</sup> <sup>x</sup> 3 . In the second phase of the algorithm, rules are generated from the large itemsets. Association rules are embedded within a single table and are therefore called intra-tuple patterns 3 . <sup>w</sup> <sup>x</sup>

Agrawal and Srikant 4 proposed another algo- <sup>w</sup> <sup>x</sup> rithm to extract sequential patterns from a single table containing discrete attribute values. In Ref. 4 ,<sup>w</sup> <sup>x</sup> a sequential pattern is an ordered list of itemsets. Consider the single table database in Table 1 whereŽ each customer can have only one transaction in a single date : each transaction can be viewed as an . itemset, and all the transactions pertaining to a single customer can be viewed as a sequence or an ordered list of itemsets. Table 2 shows a sequence version of the table in Table 1.

A sequence or sequential pattern $\{ s _ { 1 } , s _ { 2 } , \ldots , s _ { n } \}$ is said to be contained in another sequence $\{ t _ { 1 } , t _ { 2 } , \ldots , t _ { m } \}$ $m \geq n ,$ , if there exist integers $j _ { 1 } < j _ { 2 } < \ldots < j _ { n } ,$ , such that $s _ { 1 } \subseteq t _ { j _ { 1 } } , s _ { 2 } \subseteq t _ { j _ { 2 } } , . . . , s _ { n } \subseteq t _ { j _ { n } } ,$ . The ‘‘strength’’ of a sequence is again measured by its support. For the database in Table 1, e.g., the support measure is the percentage of customer sequences which contain a certain sequence. Also, a sequence S is said to be large if it is contained in, at least, minimum support of the customers sequences 4 . The algorithm is<sup>w</sup> <sup>x</sup> composed of five phases. In the first phase, the database is sorted such that all transactions pertaining to a single customer appear consecutively sorted by date of transaction. In the second phase, the Apriori algorithm 3 is applied to extract large item-<sup>w</sup> <sup>x</sup> sets. However, when measuring the support for an itemsets, the counting for support is performed per customer and not per transaction as in Ref. 3 . The<sup>w</sup> <sup>x</sup> set of large itemsets defines a set of large sequences of length 1, called 1-sequences. Each 1-sequence is mapped to an arbitrary unique integer. Table 3a shows all large itemsets extracted from the database in Table 1. In the third phase, the table is transformed into a transformed database $D _ { \mathrm { T } }$ , where each transaction is replaced by the set of large itemsets contained in that transaction. Table 3b shows the transformed database $D _ { \mathrm { T } }$ . In the fourth phase, also called the sequence phase, large sequences of size $n \geq 2 \ { \mathrm { ( i . e . } }$ , n-sequences, $n \geq 2 )$ are extracted, where the key observation is that large sequences must be comprised of large itemsets. The transformed database $D _ { \mathrm { T } }$ constitutes the fundamental structure on which the operations to extract n-sequences $n \geq 2$ are performed. Lastly, the fifth phase of the algorithm, called maximal phase, deletes all subsequences contained in other sequences, since these patterns are redundant.

Table 1  
A sequence version a supermarket table

<table><tr><td>Customer ID</td><td>Items purchased</td></tr><tr><td>1</td><td> $\langle \{A,B,C\} \{D,E\} \rangle$ </td></tr><tr><td>2</td><td> $\langle \{F,G\} \{H\} \rangle$ </td></tr><tr><td>3</td><td> $\langle \{B,C\} \{E\} \rangle$ </td></tr><tr><td>4</td><td> $\langle \{G\} \{I\} \{H\} \rangle$ </td></tr></table>

Table 2  
Supermarket purchase database

<table><tr><td>Customer ID</td><td>Day of purchase</td><td>Items purchased</td></tr><tr><td>1</td><td>January 12, 1998</td><td>A, B, C</td></tr><tr><td>1</td><td>January 25, 1998</td><td>D, E</td></tr><tr><td>2</td><td>February 28, 1998</td><td>F, G</td></tr><tr><td>2</td><td>February 10, 1998</td><td>H</td></tr><tr><td>3</td><td>May 15, 1998</td><td>B, C</td></tr><tr><td>3</td><td>June 15, 1998</td><td>E</td></tr><tr><td>4</td><td>March 11, 1998</td><td>G</td></tr><tr><td>4</td><td>April 28, 1998</td><td>I</td></tr><tr><td>4</td><td>May 21, 1998</td><td>H</td></tr></table>

Building the transformed database $D _ { \mathrm { T } }$

<table><tr><td colspan="2">(a) All extracted large itemsets</td></tr><tr><td>Large itemset</td><td>Mapped to</td></tr><tr><td>(B)</td><td>1</td></tr><tr><td>(C)</td><td>2</td></tr><tr><td>(E)</td><td>3</td></tr><tr><td>(G)</td><td>4</td></tr><tr><td>(H)</td><td>5</td></tr><tr><td>(B, C)</td><td>6</td></tr></table>

Ž . b The transformed database $D _ { \mathrm { T } }$

<table><tr><td>Customer ID</td><td>Items purchased</td></tr><tr><td>1</td><td> $\langle \{ 1,2,6\} \{3\} \rangle$ </td></tr><tr><td>2</td><td> $\langle \{4\} \{5\} \rangle$ </td></tr><tr><td>3</td><td> $\langle \{1,2,6\} \{3\} \rangle$ </td></tr><tr><td>4</td><td> $\langle \{4\} \{5\} \rangle$ </td></tr></table>

## 3. Database schema for the problem

Before describing the database schema for the problem, it is helpful to consider the sample relational database shown in Table 4. Relation $R _ { 1 }$ contains one tuple for each admission to the hospital, and its key is Patient ID. Relation $R _ { 2 }$ contains details pertaining to the patient in each department in which a patient stayed during the related hospitalization, and its key is composed of Patient ID and Department. One patient may stay in one or more departments. Relation $R _ { 3 }$ contains information on procedures performed for a certain patient while staying in a certain department, and its key is Patient ID, Department and Procedure. It is possible that no procedure is performed for a patient while in a certain department.

This sample database is similar to the real hospital database we used in the test-bed application presented in Section 7, which similarly includes three main tables, except that the real database includes many more fields per table.

In the relational model, we say that if relation $R _ { i }$ includes, among its attributes, relation $R _ { j } ^ { \mathrm { ~ , ~ } } \mathrm { s }$ primary key, then a tuple $t _ { 1 }$ in $R _ { j }$ and a tuple $t _ { 2 }$ in $R _ { j + 1 }$ refer to one another if $t _ { 1 } \mathrm { [ F o r e i g n \_ K e y ] } ^ { \prime } =$ $t _ { 2 } [ \mathrm { P r i m a r y \_ K e y } ]$

A hierarchical model, in which each table is a node i.e., record type and a parent–child relation- Ž . ship is an arc in the tree, can be used to represent this database.

For the hierarchical model representation, any two relations with the same primary key can be represented as a single node. Relation $R _ { i } ,$ , that includes as a foreign key relation $R _ { j } ^ { \mathrm { ~ } , } \mathrm { ~ s ~ } \left( i \neq j \right)$ primary key

Table 4

An example for hospitalization discharge abstracts database

$$
R _ {1}:
$$

<table><tr><td>Patient ID</td><td>Age group</td><td>Sex</td><td>Cost ($)</td></tr><tr><td>100</td><td>60–65</td><td>M</td><td>7–9 K</td></tr><tr><td>200</td><td>5–7</td><td>F</td><td>5–7 K</td></tr><tr><td>300</td><td>60–65</td><td>F</td><td>7–9 K</td></tr><tr><td>400</td><td>10–12</td><td>M</td><td>2–5 K</td></tr></table>

$R _ { 2 } { \mathrm { : } }$ Departments

<table><tr><td>Patient ID</td><td>Department</td><td>LOS $^a$ </td></tr><tr><td>100</td><td>Internal</td><td>2–3 days</td></tr><tr><td>100</td><td>ER</td><td>1 day</td></tr><tr><td>200</td><td>Pediatric</td><td>2–3 days</td></tr><tr><td>300</td><td>Surgery</td><td>3–5 days</td></tr><tr><td>300</td><td>ER</td><td>5–7 h</td></tr><tr><td>400</td><td>ER</td><td>1–2 h</td></tr><tr><td>400</td><td>Pediatric</td><td>1 day</td></tr><tr><td>400</td><td>Orthopedic</td><td>5–7 days</td></tr></table>

$R _ { 3 } { \mathrm { : } }$ Medical procedures and tests

<table><tr><td>Patient ID</td><td>Department</td><td>Procedures and tests</td></tr><tr><td>100</td><td>ER</td><td>Blood count</td></tr><tr><td>100</td><td>ER</td><td>ECG</td></tr><tr><td>200</td><td>Pediatric</td><td>X-ray</td></tr><tr><td>200</td><td>Pediatric</td><td>Blood count</td></tr><tr><td>300</td><td>ER</td><td>Blood count</td></tr><tr><td>300</td><td>ER</td><td>ECG</td></tr><tr><td>400</td><td>ER</td><td>Blood count</td></tr><tr><td>400</td><td>Pediatric</td><td>X-ray</td></tr><tr><td>400</td><td>Pediatric</td><td>Fixation</td></tr></table>

<sup>a</sup> Length of stay: h for hours.

Ž . a one-to-many relationship , is represented with a parent–child relationship, i.e., an arc from $R _ { i }$ to $R _ { j } { \mathrm { : } }$

$R _ { i } \stackrel { 1 : n } {  } R _ { j } . \mathrm { ~ A ~ }$ ‘path’ refers to a sequence of connected nodes in the tree $R _ { i } , R _ { i + 1 } , \ldots , R _ { n }$ with consecutive increasing subscript indices, such that between any two consecutive relations, a parent–child relationship:

$$
R _ {j} \stackrel {{1: n}} {{\to}} R _ {j + 1} \text {   exists.   }
$$

In this paper, we consider a tree with a single path; for instance, the database depicted in Table 4 may be represented as a tree with the following single path: $R _ { 1 } \stackrel { 1 : n } {  } R _ { 2 } \stackrel { 1 : n } {  } R _ { 3 }$

![](/api/attachments/A2NUC7JJ/fulltext/images/598c79d2f26a1686a97e72c72cd0b400ca04ad0e4604868356fd361011606d92.jpg)  
Fig. 1. An occurrence tree comprising tuples corresponding to a single hospitalization.

In addition, all the tuples across tables that referŽ . to one another constitute an occurrence tree or a hierarchical occurrence <sup>w</sup> <sup>x</sup> 7 . An occurrence tree in the database depicted in Table 4 constitutes a comprehensive collection of tuples and references pertaining to a single hospitalization. Fig. 1 shows a possible occurrence tree, where each tuple is represented with a node. The notation $t _ { i } ^ { k }$ refers to tuple $t _ { i }$ in relation $R _ { k }$ . For simplicity, we say that an occurrence sub-tree, with the root node corresponding to tuple $t _ { j } ^ { k } ,$ is tuple $t _ { j } ^ { k } \mathrm { } ^ { , } \mathrm { s }$ sub-tree. In addition, level i in an occurrence tree refers to the level of tuples from relation $R _ { i } .$ An arc from $t _ { i } ^ { k }$ to $t _ { j } ^ { k + 1 }$ connects tuples that refer to one another from relations $R _ { k }$ and $R _ { k + 1 }$ between which a parent–child relationship:

$R _ { k } { \stackrel { 1 : n } { \to } } R _ { k + 1 }$ exists.

## 4. Issues posed by multiple relational tables

The Apriori algorithm to extract association rules was designed by Agrawal et al. 3 for a single table.<sup>w</sup> <sup>x</sup> Domshlak et al. 6 attempted to apply the Apriori <sup>w</sup> <sup>x</sup> algorithm on a ‘‘virtual’’ natural join they avoidedŽ the actual join operation and performed a ‘‘virtual join’’ of multiple relational tables. However, as we . show in this section, the discovered patterns may not accurately reflect the database and<sup>r</sup>or capture mere partial information.

We are interested in examining the large i.e.,Ž frequent itemsets generation phase in the Apriori.

algorithm 3 , i.e., the core phase in the algorithm. <sup>w</sup> <sup>x</sup> Large itemsets are important, as they are precursors to association rules and contain all the information that are eventually incorporated into association rules apart from the implication structure.

Assume that we join the three tables in the database depicted in Table 4, as shown in Table 5, and then apply the large itemsets phase of the Apriori algorithm 3 to extract large <sup>w</sup> <sup>x</sup> <sup>r</sup>frequent itemsets.

One obstacle that becomes clear from the table is the redundancy of attributes in various tuples corresponding to the same patient. This causes a significant bias over the large itemsets generation phase. An itemset is extracted only if it is contained in at least a predefined percentage i.e., minimum sup-Ž port of the tuples. Since attributes of different pa-. tients are multiplied in the joined tables by different proportions, these attributes’ count of support may not reflect the true state of the world as provided by the original database. For instance, the demographic attributes of a patient being transferred through more departments and<sup>r</sup>or having more procedures and tests performed than another patient will be multiplied by a larger proportion than those of the other patient. Consequently, the demographics of this patient will have a greater ‘‘weight’’ than that of other patient’s demographics, impeding the generated large itemsets from reflecting the true state of the database.

Assume that the minimum support threshold is 26%. The itemset Age 4 <sup>s</sup>10–12 is obtained in one out of four patients see tablesŽ $R _ { 1 }$ . in Table 4 . However, since the proportions of attributes have been changed in the joined table, and the itemset  4 Age<sup>s</sup>10–12 is now contained in more than 25% of the tuples, Apriori will generate this itemset as a large itemset. An opposite example concerns the itemset Sex 4 <sup>s</sup>F . This itemset is obtained in two out of four patients in the database. If the minimum support required is 50%, it ought to be considered large. However, since in the joined table only two out of 11 tuples contain this itemset, it will not be considered large by Apriori.

<table><tr><td>Patient ID</td><td>Age group</td><td>Sex</td><td>Cost ($)</td><td>Department</td><td>LOS</td><td>Procedures and tests</td></tr><tr><td>100</td><td>60–65</td><td>M</td><td>7–9 K</td><td>Internal</td><td>2–3 days</td><td>null</td></tr><tr><td>100</td><td>60–65</td><td>M</td><td>7–9 K</td><td>ER</td><td>1 day</td><td>Blood count</td></tr><tr><td>100</td><td>60–65</td><td>M</td><td>7–9 K</td><td>ER</td><td>1 day</td><td>ECG</td></tr><tr><td>200</td><td>5–7</td><td>F</td><td>5–7 K</td><td>Pediatric</td><td>2–3 days</td><td>X-ray</td></tr><tr><td>200</td><td>5–7</td><td>F</td><td>5–7 K</td><td>Pediatric</td><td>2–3 days</td><td>Blood count</td></tr><tr><td>300</td><td>60–65</td><td>F</td><td>7–9 K</td><td>Surgery</td><td>3–5 days</td><td>nil</td></tr><tr><td>300</td><td>60–65</td><td>F</td><td>7–9 K</td><td>ER</td><td>5–7 h</td><td>Blood count</td></tr><tr><td>300</td><td>60–65</td><td>F</td><td>7–9 K</td><td>ER</td><td>5–7 h</td><td>ECG</td></tr><tr><td>400</td><td>10–12</td><td>M</td><td>2–5 K</td><td>Pediatric</td><td>1 day</td><td>X-ray</td></tr><tr><td>400</td><td>10–12</td><td>M</td><td>2–5 K</td><td>Pediatric</td><td>1 day</td><td>Fixation</td></tr><tr><td>400</td><td>10–12</td><td>M</td><td>2–5 K</td><td>Orthopedic</td><td>5–7 days</td><td>null</td></tr></table>

Another difficulty emerges as patterns extracted by the Apriori algorithm 3 from the table depicted<sup>w</sup> <sup>x</sup> in Table 5 include information pertaining to, at most, one department in which the patient stayed and a single procedure<sup>r</sup>test performed for the patient in that department. It is preferable, however, that a pattern will capture information pertaining to the overall hospitalization process.

To allow patterns capture information pertaining to the hospitalization process, an alternative to the joined table may be to pool together all attributes pertaining to one patient to construct a single record in a table i.e., so that a single table is constructed ,Ž . avoiding repetitions of attributes, if such exist. The Apriori algorithm may be applied over the constructed table to extract large itemsets. However, these patterns may be plagued with ambiguity. Consider the following set of attributes that may be generated from such table: AgeŽ . Ž <sup>s</sup>60–65 , Department <sup>s</sup> ICU , Department. Ž . Ž <sup>s</sup> ER , Procedure <sup>s</sup> ECG , length of stay. Ž . <sup>s</sup> ID . Both fields ‘‘Length of4 stay’’ and ‘‘Procedure’’ are associated with a certain department. However, one cannot deduce from this pattern which department the attribute ‘‘length of stay <sup>s</sup> 1D’’ corresponds to. Similarly, this pattern does not indicate in which department the ECG procedure is performed.

The absent information is embedded in the references between tuples across different tables. We thus conclude that it is important to capture not only frequent sets of attributes but also the references between the tuples from which these attributes are extracted.

## 5. Relational patterns

To address the issues raised above, we suggest mining relational patterns. Relational patterns are equivalent to large itemsets generated by Apriori 3<sup>w</sup> <sup>x</sup> for a single table. However, as concluded in Section 5, relational patterns capture both co-occurrences of attributes and references between the tuples from which these attributes were extracted.

![](/api/attachments/A2NUC7JJ/fulltext/images/ddeba1c157fa4ccdee5562ec76e0f712df14128479014e0fec877943527e12d8.jpg)  
Fig. 2. A relational pattern underlined italic embedded in an Ž . occurrence tree.

![](/api/attachments/A2NUC7JJ/fulltext/images/319632b24a396f86457cb2a4a3d359830c68f37ff1efc6085e67ab68a61f54de.jpg)  
Fig. 3. A relational pattern.

A relational pattern can be represented as a tree that is a sub-tree of an occurrence tree 7 in the<sup>w</sup> <sup>x</sup> database. By sub-tree, we mean that it constitutes the node structure of a sub-tree, and each node contains a sub-set of the items in the corresponding node of the occurrence tree. For instance, the hospitalization occurrence tree shown in Fig. 2 is contained in the database example of Table 4. The underlined italic attributes, along with the references represented by the arcs, constitute the relational pattern shown in Fig. 3. This relational pattern describes patients between the ages of 60 and 65, who stay in the Emergency Room where their blood count and ECG are tested.

Relational patterns are extracted with respect to Ž . wrt a certain relation $R _ { i }$ called the root relation, and can include attributes from relation $R _ { i }$ and<sup>r</sup>or from any of $R _ { i } ^ { \ , } { \bf s }$ descendant relations.

A relational pattern $T ^ { \prime }$ wrt $R _ { i }$ is said to be contained in tuple $t _ { j } ^ { k } \mathrm { \Delta s }$ sub-tree, denoted by $T ,$ , if each node in $T ^ { \prime }$ is an itemset that is contained in the corresponding node in $T .$ For instance, the relational pattern shown in Fig. 3 is contained in the occurrence sub-tree shown in Fig. 2.

We also adopt the concept of support suggested by Agrawal et al. 2 to be applied to relational <sup>w</sup> <sup>x</sup> patterns. A relational pattern wrt relation $R _ { i }$ holds on a database and is said to be large if it is contained in more than minimum support of the sub-trees of tuples in $R _ { i }$ . Minimum support is a predefined percentage parameter.

For example, Fig. 4 depicts all tree occurrences in the database described in Table 4. Fig. 5 shows a relational pattern extracted wrt relation $R _ { 1 }$ . This pattern describes male patients who are hospitalized in the Emergency Room, where their blood count is tested. Assuming that the minimum support threshold is 30%, this pattern is also large, since more than 50% of the sub-trees of tuples in $R _ { 1 }$ contain this pattern.

![](/api/attachments/A2NUC7JJ/fulltext/images/726372a4dad442e1bde2e714778c1a5e0f94ac5fb2255b556421ed093c2e1cb5.jpg)  
Fig. 4. Tree occurrences of all hospitalization instances in the database of Table 4.

![](/api/attachments/A2NUC7JJ/fulltext/images/20c1be141030bbabcac9dc2b3c31cc4b80704ce9d8e9f29a531c717806424f66.jpg)  
Fig. 5. A descendant pattern wrt relation $R _ { 2 }$

## 6. Our approach and algorithm

Assume that we wish to extract relational patterns wrt an arbitrary relation $R _ { i - n } ,$ where the leaf relation $R _ { i }$ is n levels downward in the path. Thus, the relations composing the path under consideration are $R _ { i - n } , R _ { i - n + 1 } , \ldots , R _ { i } .$

Our bottom-up approach extracts relational patterns starting from the leaf relation $R _ { i }$ up to relation $R _ { i - n } .$

Before we specify the algorithm, we first present some definitions and notations.

Ž . 1 $\mathrm { A L } _ { j } ^ { i - n }$ is the set of integers corresponding to all frequent itemsets contained in relation $R _ { j }$ extracted wrt relation $R _ { i - n }$

Ž . 2 $\mathrm { J o i n } _ { j } ^ { i - n }$ is a set of integers representing frequent Join patterns extracted at the level of relation $R _ { j }$ wrt relation $R _ { i - n }$ . These patterns are relational patterns that:

Ž .a are contained in sub-trees of tuples in relation $R _ { i } ,$ and

Ž . b include a root node corresponding to a tuple in $R _ { j }$

Ž .3 The set $S _ { j } ^ { i - n }$ contains integers representing Sibling patterns extracted at the level of relation $R _ { j }$ wrt relation $R _ { i - n } .$ A Sibling pattern is composed of $n \geq 1$ relational patterns, each of which is contained in the sub-tree of a different tuple $t _ { i }$ in $R _ { j }$ , such that the tuples $t _ { i } , ~ i = 1 , \ldots , n$ are Siblings i.e., have aŽ common parent tuple in relation $R _ { j - 1 } )$

Ž . 4 $\mathrm { D S } _ { i } ^ { i - n }$ is the set of integers representing frequent relational patterns, called Descendent patterns. Patterns in $\mathrm { D S } _ { i } ^ { i - n }$

Ž .a are contained in sub-trees of tuples in relation $R _ { j - 1 } ;$ and

Ž . b do not include nodes corresponding to tuples in $R _ { j - 1 }$ itself $( \mathrm { i . e . }$ , these patterns may include only nodes corresponding to tuples from descendent relations of $R _ { j - 1 }$ along the path ..

Ž . 5 The set $\overline { { \mathrm { D S } } } _ { j + 1 } ^ { i - n }$ includes members of the form $\langle \mathrm { P I D } , \{ P _ { \mathrm { P I D } } \} \rangle$ , where PID is the ID $( \mathrm { i . e . }$ . , the key of a tuple t in $R _ { j }$ , and the set $\{ P _ { \mathrm { P I D } } \}$ contains all integers corresponding to descendant patterns in $\mathrm { D S } _ { j + 1 } ^ { i - n }$ that are contained in $t ^ { \prime } s$ sub-tree. Each member of $\overline { { \mathrm { D S } } } _ { j + 1 } ^ { i - n }$ corresponding to tuple t in $R _ { j }$ is thus $\langle t \mathrm { P I D } , \{ d \bar { s } \in$ $\mathrm { D } \mathsf { S } _ { i } ^ { i - n } | d s$ is contained in $t ^ { \prime } s$ sub-tree .4:

At each relation along the path, our approach suggests four phases to be performed with someŽ exceptions for the leaf and root relations . At each. level along the path, we start with a seed set of frequent relational patterns and then ‘‘expand’’ them by adding new nodes. Large items constitute the building blocks of relational patterns; thus for each relation along the path, we first extract these primitives. We then examine the possible expansion of frequent relational patterns along two dimensions. First, we extract ‘‘join’’ patterns in an attempt to expand relational patterns depth-wise by joining a relational pattern in the form of a single node from the current relation to another frequent relational pattern that includes nodes from lower relations along the path. Second, in an attempt to expand patterns width-wise, we extract Sibling patterns by joining relational patterns contained in sub-trees of Sibling nodes from the current relation.

We now describe each phase in detail. Assume that we are at an arbitrary relation $R _ { j }$ along the path. At each phase, we accompany the descriptions with an example. For the example, assume that we extract relational patterns from the hospital database depicted in Table 4, wrt relation $R _ { 1 }$ . Also assume that the minimum support parameter s is 30%, and that we are now at the level of relation $R _ { 2 }$ along the path.

## 6.1. Phase 1: constructing the building blocks

At each relation along the path, we first extract frequent itemsets 3 that constitute the building<sup>w</sup> <sup>x</sup> blocks of relational patterns. For this purpose, we employ the Apriori algorithm 3 . However, differ- <sup>w</sup> <sup>x</sup> ently from Apriori, we increase the support count of an itemset per tuple in $R _ { i - n }$ that this itemset is contained in any one of its descendent tuples in $R _ { j } .$ Each large itemset is then mapped to a unique integer and stored in $\mathrm { A L } _ { j } ^ { i - n }$

In our example, the support for each itemset in $R _ { 2 }$ is computed as the percentage of patients that their descendent tuples in $R _ { 2 }$ contain this itemset. All large itemsets extracted from relation $R _ { 2 }$ wrt relation $R _ { 1 }$ are shown in Table 6.

## 6.2. Phase 2: extracting join patterns

In this phase, we extract Join patterns. A Join pattern extracted at level j is represented with an ordered list of two members $\langle a , d s \rangle$ , where $a \in$ $\mathrm { A L } _ { j } ^ { i 1 - n }$ and $d s \in \mathbf { D S } _ { j + 1 } ^ { i - n }$ . In order to generate candidates for Join patterns, we join all descendant patterns in $\mathrm { D S } _ { j + 1 } ^ { i - n }$ with all the itemsets in $\mathrm { A L } _ { j } ^ { i - n }$ . We then compute the support of each candidate. A Join pattern generated by joining an itemset $a \in \mathrm { A L } _ { j } ^ { i - }$ yn and a descendant pattern $d s \in \mathbf { D S } _ { j + 1 } ^ { i - n }$ is contained in tuple $t ^ { \prime } s$ sub-tree where Ž t is in $R _ { j } )$ , if the following are satisfied:

## 1. t contains a; and

2. there exist $\langle \mathrm { P I D } , \{ P _ { \mathrm { P I D } } \} \rangle \in \overline { { \mathrm { D S } } } _ { j + 1 } ^ { i - n }$ , such that PID $= t . \mathrm { I D }$ , and $d s \subseteq \{ P _ { \mathrm { P I D } } \}$ , where t.ID is tuple $t ^ { \prime } s$ ID.

Large itemsets extracted from relation $R _ { 2 }$ wrt $R _ { 1 }$

$$
\overline {{\mathrm{AL} _ {2} ^ {1}}}
$$

<table><tr><td>Large itemsets</td><td>Mapped to</td></tr><tr><td>{(Department = ER)}</td><td>5</td></tr><tr><td>{(Department = Pediatric)}</td><td>6</td></tr><tr><td>{(LOS = 1 day)}</td><td>7</td></tr><tr><td>{(LOS = 2–3 days)}</td><td>8</td></tr></table>

A Join pattern extracted wrt relation $R _ { i - n }$ is said to be large if it is contained in more than the minimum support of the sub-trees of tuples in $R _ { i - n } .$ Each large Join pattern is then mapped to a unique integer and stored in the set Join<sup>i n</sup>.<sub>j</sub>

<sup>1</sup> For our example, the sets DS and $\overline { { \mathrm { D S } } } _ { 3 } ^ { 1 }$ extracted at the level of relation $R _ { 3 }$ and utilized in this phase are shown in Fig. 6. We generate candidates for Join patterns by joining all members of the set $\mathrm { D S } _ { 3 } ^ { 1 }$ with those of ${ \bf A L } _ { 2 } ^ { 1 }$ . Table 7 shows the set $J _ { 2 } ^ { 1 }$ containing all the large Join patterns mapped each to a unique integer.

If $R _ { j }$ is a leaf relation, its tuples have no descendants and thus, we skip this phase.

## 6.3. Phase 3: extracting sibling patterns

At this phase, we extract Sibling patterns. We represent a Sibling pattern with a set of integers, each represents a relational pattern. In order to extract Sibling patterns, we employ an adjustment of the algorithm for sequential patterns proposed by Agrawal and Srikant 4 . This algorithm employs two <sup>w</sup> <sup>x</sup> key features. First, transactions can be grouped by some attribute e.g., in Table 1, tuples are grouped Ž by customer ID . Second, within each group, transac- . tions are ordered by some temporal attribute e.g., Ž date of purchase in Table 1 ..

We employ this algorithm with some changes. Consider, for example relation $R _ { 2 }$ in Table 4, where there are no temporal attributes and thus, no sequential patterns are defined. Tuples in $R _ { 2 }$ may be grouped by their mutual parent tuple in relation $R _ { 1 } ,$ i.e., we group Sibling tuples. In addition, whereas in Ref. 4 a customer-sequences is ordered by some <sup>w</sup> <sup>x</sup> temporal attribute, Sibling tuples are unordered. A group of Sibling tuples is called a Sibling Collection, which corresponds to customer-sequence in Ref. 4 .

In Ref. 4 , a transformed<sup>w</sup> <sup>x</sup> $D _ { \mathrm { T } }$ database is constructed and utilized to extract sequential patterns. The table is transformed such that each entry is replaced in $D _ { \mathrm { T } }$ by a set of integers representing all large itemsets contained in that entry. In this paper, we create an equivalent table from which we subsequently extract Sibling patterns. We transform relation $R _ { j }$ into a table denoted $D _ { \mathrm { T } _ { i } } ^ { i - n }$ , such that each tuple in $R _ { j }$ is replaced with integers representing all large relational patterns contained in that tuple’s sub-tree. To be included in $D _ { \mathrm { T } _ { i } } ^ { i - n }$ , we consider all patterns in $\mathrm { A L } _ { j } ^ { i - n }$ , Join $\mathfrak { l } _ { j } ^ { i - n } .$ , and $\mathrm { D S } _ { j + 1 } ^ { i - n } .$ , as these patterns constitute all possible large relational patterns wrt relation $R _ { i - n } ,$ contained in sub-trees of tuples in $R _ { j }$ . The sub-tree of a tuple t in $R _ { j }$ is said to contain a descendent pattern $d s \in \mathrm { D S } _ { i + 1 } ^ { i - n }$ if there exists $\langle { \mathrm { P I D } } , \{ P _ { { \mathrm { P I D } } } \} \rangle \in { \overline { { \mathrm { D S } } } } _ { j + 1 } ^ { i - n }$ , such that PID<sup>s</sup> t.ID, and $d s \subseteq \{ P _ { \mathrm { P I D } } \}$ , where t.ID is tuple $t ^ { \prime } s$ ID. Similar to Ref. 4 , where a sequence of<sup>w</sup> <sup>x</sup> n itemsets is called an n-sequence, a Sibling pattern of n relational patterns is called n-Sibling.

<table><tr><td colspan="2">Patient Dept. ID</td><td>Set of patterns</td></tr><tr><td>100</td><td>ER</td><td>1, 2, 4</td></tr><tr><td>200</td><td>Pediatric</td><td>1, 3</td></tr><tr><td>300</td><td>ER</td><td>1, 2, 4</td></tr><tr><td>400</td><td>ER</td><td>1</td></tr><tr><td>400</td><td>Pediatric</td><td>3</td></tr></table>

<sup>1</sup> Fig. 6. The set of descendant patterns DS and the set $\overline { { \mathrm { D S } } } _ { 3 } ^ { 1 }$

A Sibling collection is represented by a un-Ž ordered list of sets of 1-Siblings. As in Ref. 4 , if a. <sup>w</sup> <sup>x</sup> tuple in $R _ { i }$ does not contain any 1-Sibling, it is dropped from the transformed database $D _ { \mathrm { T } _ { i } } ^ { i - n }$ . In addition, if none of the tuples of a Sibling collection contains any 1-Sibling, this Sibling collection is discarded from $D _ { \mathrm { T } _ { i } } ^ { i - n }$ , but it still contributes to the count of total number of Sibling collections in $D _ { \mathrm { T } . } ^ { i - n }$

In our example, the transformed database $D _ { \mathrm { T } _ { \gamma } } ^ { 1 }$ is constructed for relation $R _ { 2 }$ as shown in Table 8. Each entry in $D _ { \mathrm { T } _ { 2 } } ^ { 1 }$ corresponds to a patient in relation $R _ { 1 }$ and contains a Sibling collection represented by a list of sets of integers. These integers represent relational pattern from the sets: $\mathrm { D S } _ { 3 } ^ { 1 } , ~ \mathrm { A L } _ { 2 } ^ { 1 }$ , and $J _ { 2 } ^ { 1 } .$

The set $J _ { 2 } ^ { 1 }$ of Join patterns

<table><tr><td colspan="2"> $J_{2}^{1}$ </td></tr><tr><td>Join patterns</td><td>Mapped to</td></tr><tr><td> $\langle 5,1\rangle$ </td><td>9</td></tr><tr><td> $\langle 5,2\rangle$ </td><td>10</td></tr><tr><td> $\langle 5,4\rangle$ </td><td>11</td></tr><tr><td> $\langle 6,3\rangle$ </td><td>12</td></tr></table>

In order to extract Ž . n <sup>G</sup> 2 -Sibling patterns from $D _ { \mathrm { T } _ { i } } ^ { i - n }$ , we apply the sequence phase in Ref. 4 . At <sup>w</sup> <sup>x</sup> this stage, we need to specify when a Sibling pattern is contained in a Sibling collection. We thus say that a Sibling pattern p is contained in a Sibling collection b if there exists an injective i.e., one-to-oneŽ . function $f \colon p \to b ,$ , such that:

1. $\forall x \in p , f ( x ) \in b$ and $x \subseteq f ( x )$

2. $\forall x _ { 1 } , \ x _ { 2 } \in p , \ x _ { 1 } \neq x _ { 2 }  f ( x _ { 1 } ) \neq f ( x _ { 2 } )$

For instance, the Sibling pattern Department ²Ž <sup>s</sup> ER , LOS . Ž . <sup>s</sup> 1 day , Department 4  <sup>s</sup> Internal is .4: composed of two sets: DepartmentŽ . Ž <sup>s</sup>ER , LOS<sup>s</sup>1 day and Department .4 Ž . <sup>s</sup> Internal . This pattern is 4 contained in the Sibling collection in $R _ { 2 }$ corresponding to patient with ID 100.

Each extracted large Ž . n <sup>G</sup> 2 -Sibling pattern is mapped to a unique integer. The set $S _ { j } ^ { i - n }$ contains all large Ž . n <sup>G</sup> 2 -Sibling patterns extracted at level j of the path wrt relation $R _ { i - n } .$

In our example, no large Sibling patterns are discovered from $D _ { \mathrm { T } _ { \gamma } } ^ { 1 }$ . Consider the transformed database $D _ { \mathrm { T } _ { 3 } } ^ { 1 }$ constructed for the leaf relation $R _ { 3 }$ as shown in Table 10. Since $R _ { 3 }$ is a leaf relation, only large itemsets from the set ${ \bf A L } _ { 3 } ^ { 1 }$ , shown in Table 9, are used to construct $D _ { \mathrm { T } _ { 3 } } ^ { 1 }$

<table><tr><td colspan="2">Table 8The transformed database  $D_{\text{T}_2}^1$ </td></tr><tr><td> $D_{\text{T}_2}^1$ </td><td></td></tr><tr><td>100</td><td> $\langle \{8\}\{1,2,4,5,9,10,11\} \rangle$ </td></tr><tr><td>200</td><td> $\langle \{1,3,6,8,12\} \rangle$ </td></tr><tr><td>300</td><td> $\langle \{1,2,4,5,9,10,11\} \rangle$ </td></tr><tr><td>400</td><td> $\langle \{1,5,9\}\{3,6,12\} \rangle$ </td></tr></table>

One Sibling pattern is extracted from $D _ { \mathrm { T } _ { 3 } } ^ { 1 }$ , and stored in the set $S _ { 3 } ^ { 1 }$ shown in Table 10.

Phase 3 is not applied for the root relation $R _ { i - n }$ since tuples in $R _ { i - n }$ have no parent tuples with respect to which Sibling patterns are extracted.

The adjustment we introduce here to the algorithm for sequential patterns suggested by Agrawal and Srikant 4 increases the theoretical complexity <sup>w</sup> <sup>x</sup> of determining whether a Sibling collection contains a Sibling pattern. However, as was the case in the database we used, if the average length of Sibling collections is not large in our database, the averageŽ is approximately two , there is no significant impact. on the application running time. We believe that for many databases, this indeed is the case; however, this posits a weakness when most tuples have a fairly large number of immediate descendants.

We do not employ the maximal phase described in Ref. 4 for sequential patterns, since we attempt <sup>w</sup> <sup>x</sup> to expand patterns extracted at this phase by adding further nodes to the sub-tree they represent. As any subset of a maximal n-Siblings has equal or larger support than the n-Sibling itself, considering only maximal Siblings inhibits the possible expansion of any of its subsets, and if we fail to expand one due to lack of support, we would also not consider possible expansions of any of its subsets.

## 6.4. Phase 4

In this phase, we construct the sets $\mathrm { D S } _ { j } ^ { i - n }$ and $\overline { { \mathrm { D S } } } _ { j } ^ { i - n }$ . The set $\mathrm { D } \mathbf { S } _ { i } ^ { i - n }$ contains all patterns contained in the sets $\mathrm { D S } _ { j + 1 } ^ { i - n } , \ S _ { j } ^ { i - n }$ and $\mathbf { J o i n } _ { j } ^ { i - } { } ^ { - } { } ^ { n }$ . The set $\overline { { \mathrm { D } \mathrm { S } _ { i } ^ { i - n } } }$ is composed of members of the form $\langle \mathrm { P I D } , \{ P _ { \mathrm { P I D } } \} \rangle ^ { \prime } \in$ $\overline { { \mathrm { D S } } } _ { j } ^ { i - n } ;$ each corresponds to a tuple t in relation

Large itemsets extracted from $R _ { 3 }$

<table><tr><td colspan="2"> $\mathrm{AL}_{3}^{1}$ </td></tr><tr><td>Large itemsets</td><td>Mapped to</td></tr><tr><td> $\{(Proc = Blood Count)\}$ </td><td>1</td></tr><tr><td> $\{(Proc = ECG)\}$ </td><td>2</td></tr><tr><td> $\{(Proc = X-ray)\}$ </td><td>3</td></tr></table>

The transformed table $D _ { \mathrm { T } ; } ^ { 1 }$ and the set $S _ { 3 } ^ { 1 }$ of Sibling patterns <sup>1</sup> D<sub>T</sub>

<table><tr><td colspan="3"> $D_{\mathrm{T}_{3}}^{1}$ </td></tr><tr><td>Patient ID</td><td>Department</td><td>Sibling collections</td></tr><tr><td>100</td><td>ER</td><td> $\langle \{1\}, \{2\} \rangle$ </td></tr><tr><td>200</td><td>Pediatric</td><td> $\langle \{1\}, \{3\} \rangle$ </td></tr><tr><td>300</td><td>ER</td><td> $\langle \{1\}, \{2\} \rangle$ </td></tr><tr><td>400</td><td>ER</td><td> $\langle \{1\} \rangle$ </td></tr><tr><td>400</td><td>Pediatric</td><td> $\langle \{3\} \rangle$ </td></tr><tr><td colspan="3"> $S_{3}^{1}$ </td></tr><tr><td>Sibling patterns</td><td>Mapped to</td><td></td></tr><tr><td> $\langle \{1\}, \{2\} \rangle$ </td><td>4</td><td></td></tr></table>

$R _ { j - 1 } .$ The set $\{ P _ { \mathrm { P I D } } \}$ contains all descendant patterns in $\mathrm { D } \mathsf { S } _ { j } ^ { i - n }$ that are contained in $t ^ { \prime } s$ sub-tree. Specifically, this set is composed of all the patterns incorporated in members of $\overline { { \mathrm { D S } } } _ { j + 1 } ^ { i - n }$ corresponding to $t ^ { \prime } s$ descendants in $R _ { j } ,$ all patterns in Join that are contained in sub-trees of $t ^ { \prime } s$ descendants in $R _ { j } ,$ and all $\left( n \geq 2 \right)$ -Sibling patterns in $S _ { j } ^ { i - n }$ that are contained in $D _ { \mathrm { ~ T ~ } _ { \mathrm { ~ * ~ } } } ^ { i - n }$ entry corresponding to t. The sets <sup>1</sup> DS and $\overline { { \mathrm { D S } } } _ { 2 } ^ { 1 ^ { \prime } }$ are shown in Fig. 7.

The relational patterns resulting from phases one to four are: $\cup _ { j } \mathrm { A L } _ { j } ^ { i - n } , \cup _ { j } S _ { j } ^ { i - n } , \mathbf { \bar { \cup } } _ { j } J _ { j } ^ { i - \bar { n } }$ , where j goes from the leaf relation’s index i to $i - n .$

We differentiate between relational patterns extracted at different levels, since it is also important for the interpretation of these patterns. For example, the same representation of a Sibling pattern extracted at different levels represent different patterns. For the database depicted in Table 4, assume that we extracted the following Sibling pattern at the level of relation $R _ { 3 }$ wrt $R _ { 1 } { \mathrm { : } }$ Procedure²Ž . <sup>s</sup> ECG ,4 Ž . Procedure<sup>s</sup>Blood Count . This 2-Sibling pat-4: tern contains two sets, each corresponding to a different tuple in $R _ { 3 }$ with a mutual parent tuple in $R _ { 2 }$ The interpretation of this pattern, shown in Fig. 8a, is that the two procedures are performed on a patient at the same department. However, the same pattern representation extracted at level 2 from the transformed database $D _ { \mathrm { T } _ { 2 } } ^ { 1 } .$ , shown in Fig. 8b, includes two sets of patterns each contained in a sub-tree of a different tuple in $R _ { 2 }$ , both of which have a mutual parent tuple in $R _ { 1 }$ . This pattern means that each procedure is performed on the patient while staying at a different department.

![](/api/attachments/A2NUC7JJ/fulltext/images/8f5bf885aed34dd11664f315a9d69236d26ec3cf39870937221f6b4f57724a77.jpg)  
<sup>1</sup> <sup>1</sup> Fig. 7. The sets DS and DS . <sub>2 2</sub>

At this stage, note that among the patterns extracted, some are contained in others, thus, comprising redundant information. For some applications, it may be useful, therefore, to present only relational patterns that are not contained in others. We thus propose the following simple procedure to identify all such redundant patterns. We use the set $\mathrm { D S } _ { i - n } ^ { i - n }$ contains integers representing all large relational patterns, from which we will remove all redundant patterns. Since patterns are represented with consecutive integers, a sub-tree T is represented by a larger integer than any of its sub-trees. We can thus examine patterns in descending order of their integer representation. For each pattern, we can apply the following: if it is an itemset, we remove all its subsets see Ref. 3 ; if it is a Join pattern, we first Ž <sup>w</sup> <sup>x</sup>. remove its two components and then recursively check for each component whether it contains other patterns. Similarly, if it is a Sibling pattern, we remove each of its components i.e., the patternsŽ composing the Sibling set , and then recursively . check for each Sibling starting with the one represented with the largest integer, whether it contains other patterns. If we find that all components of an examined pattern have been already removed earlier, we remove this pattern. To apply this procedure, we only need to ensure that when generating candidates for Join patterns, we choose descendent patterns in increasing order of their integer representation.

## 7. Implementation and experience

The approach presented in Section 6 was implemented in a prototype. The data source for the prototype was hospital discharge abstract data about 80,000 hospitalizations collected in 1995. Similar to the database in Table 4 above, the database includes three main relations.

Ž . 1 The hospitalization relation — this contains one tuple for each admission to the hospital. The hospitalization table includes 25 different fields. These are patients’ demographic data e.g., age, mar- Ž ital status, country of birth, etc. as well as attributes. pertaining to the hospitalization process such as length of stay and status in discharge e.g., releasedŽ to another medical facility, released home, deceased, etc ..

![](/api/attachments/A2NUC7JJ/fulltext/images/aaecaa44fa0382c3e0ae9a72ffd1af9d415af8c80881ed661bad947271594a63.jpg)  
Fig. 8. Examples of Sibling patterns.

Ž .2 The department relation — this contains 25 different fields pertaining to the patients’ stay in each department e.g., cost, date of admission, etc. Ž . during the course of his<sup>r</sup>her hospitalization. This table contains one tuple for each department in which a patient stayed, where a patient may have stayed in one or more departments.

Ž . 3 Procedures and diagnoses relation — lists all diagnoses and procedures performed on a patient while staying at a certain department. Diagnoses and procedures in unstructured text form are coded in the hospital using the ICD-9-CM International Classifi-Ž cation of Diseases, Ninth Revision, Clinical Modification code 21 by medical officers specially trained. <sup>w</sup> <sup>x</sup> for the task. This table contains 10 different fields such as department name, diagnosis code, and rank of diagnosis i.e., primary, minor, etc. . The database Ž . includes several additional tables that are all used for code interpretations.

The prototype with which we experimented comprises the following modules.

The data learning and Õisualization module performs simple statistical tasks for preliminary data exploration and visualization. The module includes the ability to graphically present distributions of a single database field, joint distributions of two distinct fields, and simple SQL queries. These features support the user’s preliminary investigation and data exploration, and may help inspire new ideas and investigations.

The knowledge discoÕery module takes the user’s specifications, via a graphical user interface, as input for the discovery task. These specifications are used to extract relational patterns. The presentation module presents the resulted analyses and inquiries in a comprehensible manner.

We implemented our approach on a Pentium 200 MHz computer with 128 MB RAM. When focusing the analysis on 22 K complete hospitalization cases Ž . children with ages between 2 to 12 incorporating tuples from all three relations 3.2 MB and for Ž .

minimum support of 3%, we generated 527 relational patterns in 152 s. For the same population of patients and minimum support, when employing only two relations hospitalization and department 2.4 MB ,Ž . Ž . 354 patterns where extracted in 73 s. Similarly, for a different group of 51 K patients 4.8 MB for mini-Ž . mum support of 5%, we generated 420 relational patterns incorporating all three relations in 331 s. Although the algorithm performs well for these ‘real world’ data, execution time significantly increases with the number of cases processed; it may thus be appropriate to sample the cases to be analyzed when the dataset is very large and fast response time is required.

Our experiments with the prototype generated relational patterns that demonstrate the advantages in our approach. When focusing the analysis on patients above 55 years old, 174 relational patterns were extracted. A representative example is the relational pattern shown in Fig. 9a. This pattern describes female patients who stay in the Internal Medicine Department where they are diagnosed with CongestiÕe Heart Failure. In addition, these patients stay in another department that is not identical for all theŽ patients satisfying this pattern , where they are diag- . nosed with Obesity and Essential Hypertension.

This pattern demonstrates three things. First, it incorporates two episodes of diagnosis determination: one when the diagnosis for CongestiÕe Heart Failure was determined, and the other when Essential Hypertension and Obesity were determined. If large itemsets were extracted from a joined table, instead of relational patterns, as shown in Section 4, no large itemset would include more than a single diagnosis. Second, clarity is provided by the differentiation between these two episodes. Third, this relational pattern contains references between tuples across various tables from which attributes were extracted. For instance, this pattern shows that the diagnosis for CongestiÕe Heart Failure was given in the Internal Medicine Department.

The pattern shown in Fig. 9b was extracted for the same population group. This relational pattern similarly shows that a patient is diagnosed with Diabetes Mellitus and in another department, a diagnosis for Anemia is determined. However, no pattern was found regarding the departments in which these two episodes occur.

![](/api/attachments/A2NUC7JJ/fulltext/images/68e8600d4cdd96fa33db03c39721ae228ec403abdeef387f61e077856478dfa7.jpg)  
Fig. 9. Examples for extracted relational patterns.

These examples demonstrate that relational patterns allow the incorporation of attributes across tables pertaining to a complete hospitalization process. In addition, these patterns leave no ambiguity regarding the information they convey.

In our prototype, a relational pattern is presented such that each of its nodes is presented by a numbered itemset accompanied by a number pointer to its ‘‘parent’’ itemset. This representation is equivalent to a tree structure.

## 7.1. Utilization of relational patterns

The value conveyed by relational patterns stems from two sources: they explore the data not via the traditional hypothesis testing approach, and they span all data related to the examined entity e.g., hospital-Ž ization cases ..

Traditional analysis tools used in the hospital are database queries and statistical reports. For example, reports are generated to answer questions such as: What is the percentage of patients with a certain diagnosis for which a certain surgery<sup>r</sup>diagnostic test was performed and who have been readmitted to the hospital? Common to these reports is that they are specifically directed to the space where an answer to a certain concern is expected to be found. The central issues examined are prespecified to verify or reject a hypothesis.

Particularly interesting and widely studied indicators in health care are length of stay and readmission. The traditional approach to these problems is to suggest a hypothesis and then examine its support over the data. Relational patterns, on the other hand, may suggest hypotheses. Extracted relational patterns are not restricted to exhibit any particular relationship and may be viewed as a result of an ‘‘open’’ question, thus can tap areas of the hypotheses space that may not have been explored via the traditional hypothesis setting and testing paradigm. This can only be allowed since relational patterns may incorporate all hospitalization-related data.

To illustrate how relational patterns may induce a particular direction of inquiry, consider the following example. The relational pattern describing patients hospitalized for appendectomy removal of the ap-Ž pendix who stay at the hospital longer than 7 days. may imply that complications subsequent to the procedure had occurred, leading to longer stays. Since complications are relatively rare, it is possible that the pattern flags low quality of medical care. These suggestions may induce further investigation to verify whether for the majority of the cases there is an objective justification for the unexpected length of stay. If this pattern went unnoticed by the medical staff, such a relational pattern tapping the possible flaw from the data can be used to initiate an examination.

Whereas the example discussed above implies a possibility and induces hypotheses to be tested, relational patterns may also convey stronger statements in the form of direct observations on various practices. For instance, some diagnostic procedures are recommended as hospital policy for patients exhibiting a set of symptoms that, if performed early, may significantly increase the likelihood for recovery. For example, for patients that may suffer from abdominal aortic aneurysm expansion of the abdominal aorta ,Ž . it is important to conduct an ultrasonography test as early as possible to ascertain the necessity for a surgery replacing the damaged segment and prevent a fatal rupture of the aorta at the site. If the hospital’s policy in these cases is to conduct the test while the patient is at the emergency room when the patient Ž indeed goes through the ER , the relational pattern . shown in Fig. 10, revealing that for some patients the diagnostic procedure is not performed in the Emergency Room but rather later on in the process, shows a medical practice that can be improved by emphasizing to physicians in the Emergency Room the recommended practice.

Relational patterns, however, do not comprise of any aggregate features and do not incorporate aggregate values averages, sums across patients, etc. .Ž . Thus, for the discharge abstract data, relational patterns describe frequent characteristics of individual hospitalizations. In terms of quality-related analysis, one can only infer about quality indicators pertaining to indiÕidual hospitalizations.

As in health care, relational patterns can be used in various service organizations for two generic purposes. First, suggest data-driÕen hypotheses regarding the nature of the service or internal operations. Second, as we showed earlier, by helping to identify internal practices, relational patterns can support quality improvement by highlighting flawed practices, as well as by learning of processes that are not entirely understood by or even known to the organizations. But relational patterns may be also employed in other domains, such as marketing, by identifying leads on consumer behavior and preferences. For instance, an international hotel chain can track patterns characterizing their customers and utilize them to promote and improve their services. The pattern shown in Fig. 11 describes women guests registering at a Florida beach hotel where they order fresh flowers to their rooms and join a diving class. These guests also book a single room at a French Rivera hotel, where they register for a water-ski sport activity. This pattern can be used by the chain to promote the French Rivera Florida beach hotelŽ . among their single women customers who stay at the Florida French Rivera hotel and register for aŽ . diving course water-ski . It may also offer theseŽ . guests a package including a water-ski activity di-Ž ving course and possibly accommodate them with . fresh flowers in their rooms.

Because of their clarity and comprehensiveness, relational patterns may support various activities such as quality improvement and marketing discussed above, depending upon the nature of data stored and type of organization, by either suggesting hypotheses to be further examined or by floating practices that can be beneficially utilized.

![](/api/attachments/A2NUC7JJ/fulltext/images/fa8eba824d192cdc4fc47feb446acc15212065eefb9e1f3e8a3285fdca0cfcb0.jpg)  
Fig. 10. A relational pattern implying a flawed practice.

## 7.2. Implementation issues

Some implementation issues emerged when experimenting with the prototype. One important issue is related to the high diversity among the various hospitalization instances in the database. For example, chronic patients are substantially different from obstetric or pediatric patients. For the following reasons, it is often ineffective to extract patterns from such extremely heterogeneous populations.

First and most important, the extraction process is based on the statistical strength or ‘‘support’’ of the patterns, and patterns embedded within some subpopulations may not be discovered at all when the specified minimum support threshold is applied with respect to the overall population of patients in the database. For instance, assume that a salient pattern is embedded within the population of diabetic patients, which constitute 3% of the population of patients. If the minimum support threshold employed is 5%, this pattern is bound not to have enough ‘‘support’’. Therefore, the ‘‘support’’ or strength of a pattern ought to be evaluated with respect to the relevant population.

Second, different populations induce different courses of investigation. Thus, an analyst would rather conduct an investigation on a sub-population that is more homogeneous than the entire population of patients, and should be able to change the focus of investigation back and forth to different groups as the investigation unfolds. It is therefore essential to enable the analyst to specify the population i.e., theŽ set of hospitalization instances for analysis..

A different dimension by which the analyst ought to be able to restrict the analysis is by specifying the database fields e.g., age, diagnoses, length of stay,Ž etc. to be included. The set of available fields is. overwhelming, and not all attributes are useful for every analysis. In some instances, irrelevant fields may even hamper the analysis by introducing unnecessary ‘‘noise’’. Restricting the potential attributes thus allows the analyst to focus attention on what appears to be relevant for a particular coarse of analysis.

The specification of the sub-population of interest and of the relevant fields is also helpful in another important way: When mining patterns from the entire population, the number of extracted patterns is sometimes too large, thus rendering an examination of each rule infeasible. An analyst practically cannot consider thousands or even hundreds of patterns. This is a well-known problem, in particular in relation to link analysis 11,16,18,19 . Reducing the dimensionality of the database in our experiments enabled us to substantially reduce the number of extracted patterns.

Even following such reduction, many of the extracted patterns were known and<sup>r</sup>or of no interest to the analyst. Several studies have been done on interestingness of patterns 16,18,19 . Some of these stud-<sup>w</sup> <sup>x</sup> ies are based on incorporating domain knowledge or beliefs 16 which are then used to extract only<sup>w</sup> <sup>x</sup> patterns that are not already known and<sup>r</sup>or patterns that embed useful knowledge which may trigger some action i.e., actionability 1,13,14 . In order toŽ <sup>w</sup> <sup>x</sup>. employ these ideas, medical and managerial knowledge needs to be extracted from hospital personnel to be then represented in a beliefs or rules base. Future study may examine the employment or adjustment of these methods to the method presented here.

![](/api/attachments/A2NUC7JJ/fulltext/images/a519598c25f4ec3b1772dfa3e0ca927aba197a4de5c4fecd5ae45d9f0911fb10.jpg)  
Fig. 11. A relational pattern from a hotel chain database.

A somewhat related concern pertains to continuous and discrete ordered attributes. Assume that a certain pattern exists among cardiac patients between ages 40 and 50. Considering age discretely may impede patterns from being discovered, since this pattern is now replaced by several patterns one forŽ each 1-year long age bracket , each of which is most. likely to have less support than has the more generalized pattern. It may therefore be useful to consider more meaningful age ranges. As attributes are assumed by the algorithm to be discrete, it is important to consider the various tradeoffs when considering the employment of automatic discretization methods proposed in the literature e.g., Refs. 8,10 . FromŽ <sup>w</sup> <sup>x</sup>. our experience with the prototype, we learned that different courses of analysis, even on the same population, may induce different background knowledge, and thus entail different discretization schemes. When analyzing diabetic patients, for instance, the relevant age brackets will most likely differ from those relevant for obstetric patients. Moreover, the same population may be subjected to different discretization schemes depending on the purpose and course of the analysis. Automatic discretization is thus not always appropriate. However, not all attributes are as susceptible to entail different sets of intervals as is age. Moreover, one important advantage of exploring databases by identifying patterns is that patterns characterize the world as it is reflected in the database with little or no restrictions set by the analyst. By ignoring any prior knowledge in the domain, patterns extracted in this manner are also more likely to foster unexpected findings. Automatic discretization is more susceptible to exploit these advantages by identifying intervals as these emerge from the data. For example, Srikant and Agrawal 20 have sug-<sup>w</sup> <sup>x</sup> gested a discretization algorithm particularly designed for ordinal domains where the distance between values bears no implications. Miller and Yang <sup>w</sup> <sup>x</sup> 15 propose another algorithm that allows the identification of natural intervals that are dense enough and distant enough from other intervals. This mechanism allows intervals to reflect ‘‘natural’’ clusters emerging from the data by conferring importance to the distance between different data points.

The above observations imply that automatic discretization conveys important advantages, and at the same time, depending on the purpose of the analysis and the attribute on which discretization is applied, it is sometimes also useful to allow the analyst to manually define other discretization schemes based upon one’s domain knowledge and the particular purpose of the analysis.

## 8. Summary and conclusions

In this paper, we presented relational patterns and an approach to extract them from multiple relational tables. Relational patterns capture co-occurrences of attributes from data distributed across multiple relational tables, along with the genuine references among the tuples from which these attributes are extracted. These patterns are analogous to the frequent itemsets mined by the Apriori algorithm 3 for the case of a single table.<sup>w</sup> <sup>x</sup>

Our bottom-up approach extracts patterns that are incrementally extended. Starting with patterns at the leaf level tuple, Descendent patterns are encapsulated and incorporated in their respected parent tuples, transformed to contain patterns rather then raw attributes. These patterns are extended width-wise and depth-wise alternately, up to the root tuple.

We implemented our approach and applied it to a real database. These experiments demonstrated the followings. First, our approach can extract patterns that are comprehensive in scope, and can incorporate any attribute pertaining to a complete hospitalization process. Second, relational patterns introduce no ambiguity regarding the information they convey.

The experiments also helped bring to the forefront issues of concern. Measures for coping with these issues were proposed and implemented in order to enhance an analyst’s ability to explore patterns while preventing high diversity and abundance of available data from blurring subtle patterns of interest. As patterns are extracted based on a measure of their support with respect to the examined population, utilizing all the available data may decrease the strength of underlying patterns and may inhibit their discovery. This phenomenon is particularly salient for highly diverse data.

Finally, in knowledge-intensive domains as health care, there exist tradeoffs for employing automatic discretization for continuous numeric attributes. Whereas for some attributes this may be rendered inappropriate when different courses of investigation induce different sets of knowledge implying different discretization schemes, in the more general case, automatic discretization conveys important advantages by identifying natural clusters in the data.

## Acknowledgements

The authors wish to thank Alex Tuzhilin, Edward Stohr and the anonymous reviewers for their helpful comments and suggestions that helped improve this paper. This research was conducted with the support of the Israeli Ministry of Science and Technology Infrastructure Fund.

## References

<sup>w</sup> <sup>x</sup> 1 G. Adomavicius, A. Tuzhilin, Discovery of actionable patterns in databases: the action hierarchy approach, in: Proc. of the Third International Conference on Knowledge Discovery and Data Mining, KDD 97, 1997.

<sup>w</sup> <sup>x</sup> 2 R. Agrawal, T. Imielinski, A. Swami, Mining association rules between sets of items in large databases, in: Proc. of the ACM SIGMOD Conference on Management of Data, 1993, pp. 207–216.

<sup>w</sup> <sup>x</sup> 3 R. Agrawal, H. Mannila, R. Srikant, H. Toivonen, A.I. Verkamo, Fast discovery of association rules, in: U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy Ž . Eds. , Advances in Knowledge Discovery and Data Mining, AAAI Press, 1995.

<sup>w</sup> <sup>x</sup> 4 R. Agrawal, R. Srikant, Mining sequential patterns, in: Proc. of the 11th Int. Conf. Data Eng., 1995.

<sup>w</sup> <sup>x</sup> 5 D.W. Cheung, V.T. Ng, Y. Fu, Efficient mining of association rules in distributed databases, IEEE Transactions on Knowledge and Data Engineering 8 6 1996 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 C. Domshlak, D. Gershkovich, E. Gudes, N. Liusternil, T.

Meisels, S. Shimony. FlexiMins — a flexible platform for KDD research and application construction, Fourth International Conference on Knowledge Discovery and Data Mining, KDD 98, 1998.

<sup>w</sup> <sup>x</sup> 7 R. Elmasri, S.B. Navathe, Fundamentals of Databases Systems, Addison-Wesley, 1994.

8 U.M. Fayyad, K.B. Irani, Multi-interval Classification Learning, IJCAI-93, 1993, pp. 1022–1027.

<sup>w</sup> <sup>x</sup> 9 U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, From data mining to knowledge discovery: an overview, in: U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy Ž . Eds. , Advances in Knowledge Discovery and Data Mining, AAAI<sup>r</sup>MIT Press, 1996.

<sup>w</sup> <sup>x</sup>10 R. Kerber, ChiMerge: discretization of numeric attributes, Proc. 10th Natl. Conf. Artificial Intelligence, AAAI Press<sup>r</sup>MIT Press, 1992, pp. 123–128.

<sup>w</sup> <sup>x</sup> 11 M. Klemettinen, H. Mannila, P. Ronkainen, H. Toivonen, A.I. Verkamo, Finding interesting rules from large sets of discovered association rules, in: Proc. of the Third International Conference on Information and Knowledge Management, 1994, pp. 401–407.

<sup>w</sup> <sup>x</sup> 12 H. Manila, H. Toivonen, A. Verkamo, Effecient algorithms for discovering association rules, in: Proc. AAAI Workshop Knowledge Discovery in Databases, July 1994, pp. 181–192.

<sup>w</sup> <sup>x</sup> 13 C.J. Matheus, G. Piatetsky-Shapiro, D. McNeill, An application of KEFIR to the analysis of health care information, AAAI Workshop on Knowledge Discovery in Databases, July 1994, pp. 441–452.

<sup>w</sup> <sup>x</sup> 14 C.J. Matheus, G. Piatetsky-Shapiro, D. McNeill, Selecting and reporting what is interesting: the KEFIR application to health data, Advances in Knowledge Discovery and Data Mining, AAAI<sup>r</sup>MIT Press, 1995, pp. 495–516.

<sup>w</sup> <sup>x</sup> 15 R.J. Miller, Y. Yang, Association rules over interval data, ACM SIGMOD 26 2 1997 452–461.Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 B. Padmanabhan, A. Tuzhilin, a belief-driven method for discovering unexpected patterns, in: Proc. of the Fourth International Conference on Knowledge Discovery and Data Mining, KDD 98, 1998, forthcoming.

<sup>w</sup> <sup>x</sup> 17 A. Savasere, E. Omiecinski, S. Navathe, An effecient algorithm for mining association rules in large databases, in: Proc. 21st Int. Conf. Very Large Data Bases, September 1995, pp. 432–444.

<sup>w</sup> <sup>x</sup> 18 A. Silberschatz, A. Tuzhilin, On subjective measures of interestingness in knowledge discovery, in: Proc. of the First International Conference on Knowledge Discovery and Data Mining, 1995, pp. 275–281.

<sup>w</sup> <sup>x</sup>19 A. Silberschatz, A. Tuzhilin, What makes patterns interesting in knowledge discovery systems, IEEE Transactions on Knowledge and Data Engineering. Special Issue on Data Mining 5 6 1995 970–974.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 R. Srikant, R. Agrawal, Mining qualitative association rules in large relational tables, SIGMOD ’96, Montreal, Canada, June 1996.

<sup>w</sup> <sup>x</sup> 21 U.S. Public Health Service, Health Care Financing Administration, The International Classification of Diseases, 9th Revision, Clinical Modification PHS, 80-1260, Washington, DC, 1980.

![](/api/attachments/A2NUC7JJ/fulltext/images/afcfe70d6801ed80407898e1caf317fdf47356e0dfed66a0db2148b68ea376e8.jpg)

Maytal Saar Tsechansky is a PhD student at the Information System Department, the Stern School of Business, at New York University. She acquired her BSc and MSc from Ben-Gurion University, Israel. Her research interests are knowledge discovery and data mining in databases, induction of regularities in databases to support decision making, and automatic construction of user’s profile.

![](/api/attachments/A2NUC7JJ/fulltext/images/8da359eaf9b3df59c97a92bf646b05d309ab58d001298eb2ff28f8be3d8b2788.jpg)

Gad Rabinowitz is Senior Lecturer in the Industrial Engineering and Management Department at Ben-Gurion University, and obtained his PhD in Operations Research from Case Western Reserve University. His research interests focus on the theory and practice of operation and scheduling of production and logistics systems; modeling of quality engineering and management issues; and the design and operation of multi-quality water supply systems. He also serves as

![](/api/attachments/A2NUC7JJ/fulltext/images/d9981d422f8d5185bf9f5a9a273f6df347b0ffe5887db77c1e38dbceda344f56.jpg)

Nava Pliskin is an Associate Professor at the Department of Industrial Engineering at Ben-Gurion University in Beer-Sheva, Israel. Previously, she was a Thomas Nenry Carroll Ford Foundation Visiting Faculty Member at Suffolk University, Babson College, and Bolston University. She acquired her PhD and SM degrees from Harvard University. Her research, focused on longitudinal analysis of Information-Technology impacts at the global, national, organiza-

tional, and individual levels, has been published in such journals as Information and Management, Database, Information and Software Technology, IEEE Transactions on Engineering Management, ACM Transactions on Information Systems, The Information Society, Communications of the ACM, Information Technology and People, Business Horizons, The Australian Journal of Information Systems, the Asia Pacific Journal of Human Resources, The Computer Journal, Journal of Engineering Valuation and Cost Analysis, and International Journal of Information Management.

the academic advisor of the quality program of the Soroka Medical Center.

Avi Porath, MD, MPH, is an Associate Professor of Medicine, Ben-Gurion University of the Negev. He is a director of Medical Department 6 at the Soroka Medical Center, Beer-Sheva, Israel. Research interests: quality assurance of medical care, clinical decision making, study of diseases specific to the Negev region. Research projects: knowledge discovery in hospital medical databases, quality and performance indicators of medical care in the community.
