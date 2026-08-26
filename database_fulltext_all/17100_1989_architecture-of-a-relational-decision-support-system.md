---
otero_id: 17100
otero_key: "JK8YY3UF"
title: "Architecture of a relational decision support system"
authors: "Carlo dell'aquila; Ezio Lefons; Filippo Tangorra; Luigi Colazzo"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90029-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Architecture of a Relational Decision Support System \*

Carlo DELL'AQUILA, Ezio LEFONS

and Filippo TANGORRA

Istituto di Scienze dell'Informazione, Università di Bari, I-70126
Bari, Italy

Luigi COLAZZO

Istituto di Informatica, Università di Trento, I-38100 Trento, Italy

The architecture of the POLD relational system for distributed data analysis is presented. POLD was designed as the kernel of a decision support information system. The peculiarity of POLD consists in allowing the user to view and analyze the data information as couple $\langle data, semantics \rangle$ , the semantics being a user's suitable classification of the data. This approach furnishes the user with a powerful tool for the semantic integration of data coming from different and/or distributed sources. Both semantics and user views are dynamically definable, that is, they may change with user, current time, and application. The POLD system supports an extended version of the relational operations in order to fit the proposed approach. Moreover, this system provides features for statistical analyses, reports and graphical representations.

Keywords: Data Semantics, Decision Support Systems, Relational Data Bases, Database Management.

![](/api/attachments/JK8YY3UF/fulltext/images/0a94c115c673a66478ae68fdf1fbc654b3d1f52fa1799fd654a3e8a8e250f8a4.jpg)

Carlo dell'Aquila is Associate Professor of Computer Science at the University of Bari, Italy. He received his degree in Physics in 1969 from the University of Bari, where he taught Physics in the Engineering and in the Science Departments. His research interests are in the area of database management, decision support systems, and computer based learning systems.

\* In memoriam of Professor Alberto Silvestri, the first proponent of the POLD system.

## 1. Introduction

Statistical and scientific information systems [22,33–35] and decision support systems [5] often require that large quantities of data be managed and manipulated. Some research fields (e.g., earth resource, meteorology, astronomy, nuclear physics) involve huge volumes of raw data and time series which must be automatically produced and collected.

The modelling and organizing of whole sets of data in a database is a storage and time-consuming effort, often useless for the actual current needs of the user, because, normally, the user's analysis/research is concerned with only a small part of the data.

The decisional analyses in non-scientific environments require that the user mainly accesses

![](/api/attachments/JK8YY3UF/fulltext/images/1c9848dbd49f8f99a5f754a0bd0dd78b04defd542b78c98a8bc74f6eaaee9ae5.jpg)

![](/api/attachments/JK8YY3UF/fulltext/images/3aa513fc9dda837d8c978167dd6fe4ddb9099228f1145bfadf0773ae67cbd614.jpg)

Ezio Lefons received his degree in Mathematics from the University of Pisa, in 1973. At the present time, he is Associate Professor of 'Information Organization Techniques' at the University of Bari, and Coordinator of the doctoral course of research on 'Science of Human Relations'. His current scientific interests include models of databases and analytic databases, many-valued logics, and human relational interaction system modelling.

Filippo Tangorra received his degree in Computer Science from the University of Bari, Italy, in 1975. He is currently Associate Professor of Computer Science at the same University. His research interests are in the area of database management systems, scientific and statistical database management, and decision support systems.

Luigi Colazzo received his degree in Computer Science from the University of Bari, Italy, in 1977. He is Research Assistant at the University of Trento, in the Institute of Information Science. His scientific interests regard conceptual models of analytic databases, and research activity support systems.

existing (structured) data, such as administrative data, in order to obtain basic statistical data. Moreover, the correlation and the integration of data coming from different sources often become necessary. Practically speaking, this may result in a physical, logical and/or semantic bottleneck [24,27,36].

Administrative as well as scientific data also cover very large sets: frequently this is the case when the data potentially useful to the current analysis are contained in collections gathered without a well-established or finalized purpose.

Naturally, the organization of all primary available data in a database is of a significant cost, and conceptual modelling, even when realistic, may be sometimes an unprofitable or a misleading ‘window on the real world’ for the user.

People may interpret data differently, even in the presence of a conceptual data model. Moreover, a data model can produce a distortion of reality because it forces the user to view reality as presented in that model [20]. The principle of semantic relativism of information, that is, allowing greater user flexibility in the interpretation of data and data model as compared to the real world (cf., e.g., [6]), must be extended for each scientific and decisional user. The data model has to adapt or derive from the user, not vice-versa [25].

Also, in the presence of a growing quantity of data, regardless of whether it comes from external databases or from off-line raw collections, the totality of the (distributed) data may not be reasonably viewed and conceptually modelled to form a representation of a captured slice of the real world. The same user may differently resolve semantic ambiguities existing in the data according to problems, data, bases of reference, space and time [25]. On the other hand, a conceptual data model generally has to be stable and suitable for more than one user. The fact remains that it is difficult to define reality and to define the rules for human interpretations [13].

Consequently, scientific/decisional users must be furnished with a ‘flexible’ tool for defining and manipulating personal interpretations of real world phenomena, provided that the interpretations are beneficial for the solution of the user's problem.

This paper describes our approach.

## 2. The 'Virtual Database' Approach

The conventional relational database systems (e.g., [2,8,19,30,37,38]) do not allow the user to assign an application-dependent semantics to the data. However, it must be said that these systems are not generally designed to answer the complex queries that decisional applications may involve.

![](/api/attachments/JK8YY3UF/fulltext/images/a73849071285a2d90b3ef4606cd1e6fdb95d59fa5c49c9609018520010a45ff6.jpg)  
Fig. 1. Definition levels of a real database.

In our approach, the whole distributed set of available raw data is called the 'virtual database' as opposed to a 'real database'. Whereas the real database concept may be similar to the external database one in the ANSI/SPARC architecture, the virtual database concept has no correspondent in standard architecture and simply refers to the totality of data, possibly un-modelized, from which each user can extract a suitable subset by using selection/aggregation processes. The subset, properly finalized to the application by the user (semantics assigned), can be updated and queried as in an effective database [fig. 1].

The real database, on the other hand, consists of one or more updatable 'sessions', each one corresponding to a particular semantic view of the data vs the application by the user.

## 2.1. The User's Session

More sessions can coexist within the same real database. For example, they can express alternative frames for interpreting the phenomena under investigation or they may contain the temporal versions of the phenomena. Finally, they may serve to separately analyze phenomena, which may be related subsequently.

The POLD system prototype that we utilized $[12]$ allows the user to construct as many sessions as he deems useful from the virtual database.

In order to furnish all the facilities for the query process, a user session consists of a set of objects called compounds. From the conceptual point of view, a compound corresponds to an interpreted phenomenon. From the logical point of view, the compound is a normalized relation [9] or a multirelation (i.e., duplication may occur). Physically, it consists of the following four files:

(a) The .Data. file. It is a sequential file and contains the primary data selected from the virtual database. In what follows, we assume that the .Data. file be a relation or, possibly, a multirelation.

![](/api/attachments/JK8YY3UF/fulltext/images/c5facf71d5746acbc80b043b11f42e17cfbb273234aa3292cfe9510bc4aa7945.jpg)  
Fig. 2. Example of urbanistic census compound.

(b) The .Schema. file. It is the usual schema, that is, it contains the description of the .Data. file: attribute names, primary keys, types and formats of the data.

(c) The .Test. file. This file contains the definition of suitable semantics that the user assigns to the primary data stored in the .Data. file. The semantics is specified by means of conditions of classification. The aim, as will be discussed later, is to furnish information for the creation of the .String. file.

(d) The .String. file. This is a file of bitstrings and is dense with respect to the .Data. file (that is, each bitstring refers to the corresponding tuple in the .Data. file). A bitstring is the result of the application of the classification (defined in the .Test. file) on the correspondent primary tuple. The .String. file represents all the information in the .Data. file that the user currently deems relevant to future queries.

## 2.2. Example of the Compound Structure

In order to clarify the structure of the compound, we will consider an example taken from a real application for the urbanistic planning of a town based on the census of buildings.

For the sake of simplicity, we consider a session composed of only the FLAT compound shown in fig. 2. A tuple in the FLAT.Data. refers to a flat in a building. Only the attribute names are shown in the related FLAT elevated Schema.. The FLAT.Test. contains the definition of the user's set of conditions of primary data classification that is considered relevant to a certain investigation. The FLAT.String. contains the relative boolean values of the classification conditions defined in the FLAT.Test. and applied to the FLAT.Data.. For instance, the second bit in the ith tuple of the FLAT.String. represents the truth value of the second condition (test #2) on the ith tuple of the FLAT.Data. file, or, in other words, whether or not the ith flat is located in the central district.

## 3. POLD Architecture Overview

Before discussing in detail the user's definition and manipulation of the real database, in this section we give an architecture overview of the POLD system. The architecture is shown in fig. 3.

![](/api/attachments/JK8YY3UF/fulltext/images/17b41e1ae5a1808b53d70461986fcabbf66f321ded78b5efc5c6f6c6a29ec6ab.jpg)  
Fig. 3. Architecture of the POLD distributed system.

![](/api/attachments/JK8YY3UF/fulltext/images/52f223fce294eb11498e684e39b0b6fc8b41aa791ae8d8088a0d42ce6823f20b.jpg)  
Fig. 4. Command menu of the POLD system.

The lowest layer consists of a network filing system utilized mainly for the transfer of sequential files belonging to any logical-physical level [fig. 3].

The second layer consists of the actual POLD subsystem and is subdivided in three modules:

(1) The Data Editor provides the user with the transfer of data from level 0 (virtual database) to level 1 (selected data relevant to the application).

(2) The Query Editor allows the user to define sessions, and, in particular, to assign the semantics to the data (i.e., to define .Test.

files). That is, it is used to transform data of level 1 in data of level 2.

(3) The Run module is devoted to the data manipulation and, in particular, to the (extended) relational manipulation of compounds.

The complete POLD command menu furnished to the user is shown in fig. 4.

## 3.1. The Data Editor

The Data Editor implemented performs the following functions:

\- Maintenance of appropriate catalogues of available data. In fact, the raw data are usually stored on off-line memories, and files sometimes span hundreds of tapes.

\- Transfer of catalogued files to direct access devices according to the selection/aggregation criteria defined by the user.

\- Creation of new files and/or updating of data.

\- Definition of the schemata of the selected data.

\- Data recovery.

A more detailed description of the Data Editor, or its equivalent module, cannot profitably be given because it strongly depends on the host operating system in use.

## 3.2. The Query Editor

The Query Editor is thoroughly described in [16]. It permits the user to define sessions and procedures for performing the subsequent relational queries. At this stage, the user must only be aware of the semantics of the data stored in the .Data. file.

The Query Editor performs the following functions:

\- Maintenance of the session catalogue. The catalogue contains the session and compound definitions grouped by user.

\- Creation and deletion of sessions.

\- Opening of the current session.

In particular, the Query Editor is subdivided in two submodules [fig. 4]:

(1) The Session manager works on the session catalogue, and manages the definition of all user sessions and compounds. It contains a Filer option that permits the user to construct a session starting from his other sessions, or from sessions owned by other users (provided that the proper authorization exists).

(2) The Procedure manager allows the user to define the classification conditions and the catalogued procedures (the .Test.file) by:

(a) Defining new classifications and procedures. This facility is performed by the Test management block.

(b) Utilizing existing definitions and procedures to easily produce more complex conditions of classification. This facility is performed by the Work Area block.

## 3.3. The Run Module

The Run module supervises the manipulation of the data contained in the current session. Generally, data manipulation operations at the internal level work on the compound .String. files. The materialization of the .String. file for a given compound can be directly requested by the user by utilizing the command menu. However, if the proper .String. files are not currently present, then the POLD system will automatically materialize them on the last version of the .Data. and .Test. files, before executing the user's relational manipulation involving those compounds. We chose to also furnish the user with an explicit (manual) command because the materialization of a .String. file may be time-consuming. Therefore, it might be useful for the user himself to decide the proper time to (re-)materialize the file.

The Run module performs the following functions:

\- Creation of the .String. file of a given compound.

\- Execution of relational operations on compounds.

\- Execution of user's application procedures (e.g., statistics, graphics, reporting), and of final data processing.

These operation are handled by the following submodules respectively:

(a) String Creation, which requires that the .Data. and .Test. files exist in the current compound.

(b) Relational Operations, which works on completely defined and materialized compounds.

(c) User Routines, which provides a standard interface for the user's applicative programs.

## 3.4. The POLD Distributed Environment

The main purpose of the POLD project was to design a tool for data analysis in a distributed environment. Therefore, the system has a multi-node architecture, each node having the structure illustrated in fig. 3.

The catalogued files may be stored in any nodes of the system network, and each user has access to the whole set of primary files. By using the Data Editor, the local or remote user can copy network files into his own .Data. files. He can also avoid transferring and duplicating extremely large files by directly using the network files.

The user may define sessions with compound files stored on one or more nodes. However, the session preparation will be facilitated if (copies of) the .Schema. and .Test. files are allocated on the local node.

Every user's operation is stored sequentially in a command file, called Run Status. For each operation, the Run Status also contains the session and node identifiers, the operation type, the involved compounds, and a status flag.

The aim of the Run Status command file is to process asynchronously each single relational or user-defined operation. In addition, it permits the recovery of the last defined operations in the case of system failure, time out, or any other interrupt cause.

The prototype system includes a microprocessor version, called POLT system [17] (see fig. 3). The microcomputer plays the role of an intelligent workstation linked to a master node by a local communication protocol. The intelligent terminal POLT allows the user to make final simple processing of the retrieved data without engaging the master resources. The POLT systems support the relational operations (join is not implemented in the present version) and simple statistical and graphical functions.

## 4. The User Classification of Data

The user's data view is performed by creating a set of elementary conditions of classification, that is, by creating the .Test. file.

Due to the unforeseeable evolution of the data analysis in scientific/decisional applications, the user classification (and, consequently, the .Test. file) must be easily modifiable at any time.

In the POLD system, a test can be a simple condition or simple test, a multiple condition or multiple test or a catalogued procedure. The syntax for the test definition is described in [16].

The syntax of the simple test requires the specification of:

\- The test identifier;

\- An attribute name;

\- A comparison (≤, =, <, >, ≥, ...) or a set membership (∈,∉) operator;

\- An operand. This can be an attribute name, a constant, an aggregate function defined on a set of attributes, a value set, or a value range;

\- An optional weight.

The multiple test corresponds semantically to a list of m simple tests. A multiple test permits the user to define multiple conditions in a simple and compact way, avoiding cumbersome sequences of simple tests. The possible syntactic forms for the multiple test are:

(a) Explicit list. The multiple conditions are specified by a list of simple test identifiers.

(b) Value list. The attribute (specified by its name) is compared to each item of an ordered value list (on the basis of a specified operator).

(c) Hystogram list. This form represents a compact way of classification and may have several syntactic specifications. The value range of a specified attribute is subdivided into a given number of classes, and the truth value of the test is whether or not the attribute value belongs to the class, for each class.

The conditions expressed by a multiple test can be mutually exclusive or not. For example, the age of a man can be partitioned into mutually exclusive classes of age. On the contrary, the classification per jobs of an employee cannot be a partition of the job set, if an employee can be currently assigned to more than one job.

There are two important reasons for defining multiple tests:

(1) The use of mutually exclusive multiple tests can drastically reduce the response time to queries since they require a minimal amount of storage (the response time depends strictly on the bitstring length).

(2) The possibility of defining many tests at the same time reduces the user's work preliminary to the query process.

The catalogued procedure is defined as boolean formula of existing simple tests. Therefore, the catalogued procedure can refer to one or many attributes.

The definition of the elementary conditions of classification by the user himself guarantees a higher degree of semantic consistence of data coming from different sources and obtained with different criteria. In fact, the user can define equivalences or similarities between sets of values by adopting appropriate classifications.

## 4.1. Example

With reference to the surface attribute of the FLAT.Data. in fig. 2, all the instanced flats have different surface values. The four tests defined on this attribute (tests #6, #7, #8, and #9) specify only four classes of surface values significant for user investigation. For example, on the basis of test #6, the flats #3 (which has the original primary value of 45 m²), #4 (86 m²), #8 (23 m²), and #10 (100 m²) have been considered to produce equivalent surface information. (This is reflected in the Flat.String.; the 6th bit has value 1 in the 3rd, 4th, 8th, and 10th bitstrings, and 0 otherwise).

As an example of data integration, we can consider the problem of measure unit conversion. If the user wishes to relate data values expressed in unit a (e.g., centimetres) from source $\alpha$ , with data values referring to an homogeneous entity set expressed in unit b (e.g., inches) from source $\beta$ , then the respective .Data. $\alpha$ and .Data. $\beta$ are not directly comparable. The integration that reflects the desired classification of the user is obtainable by defining the proper classification in .Test. $\alpha$ (that is, with reference to ‘centimetres’) and the physically equivalent one (1cm = 0.3937 inches) in .Test. $\beta$ . It is to be observed that in this way, no real data conversion is performed (thus saving time and storage), and that the .String. files contain fully comparable and union-compatible data (information expressed by boolean values is independent of the measure unit).

## 5. The String File

The use of the .String. file in addition to the .Data. file must be carefully discussed, because this is a very important part of the system architecture.

Efficiently answering queries in very large databases normally requires the use of several kinds of indexes, for example: B-trees [14,21,28]; lists, multilists, inverted/binary lists, and pointer chains [3,4,15,21,23]; multiattribute combined indexes [26]; precomputed query/procedure answers or view indexes [29,31,32]; and generalized access path structures [18]. However, there are three serious disadvantages in using indexes when processing very large data sets in a distributed environment:

(1) The structure of the indexes is often strongly dependent on the system configuration at the physical level. Therefore, it is very difficult to maintain or to create the index structures for data sets resulting from relational operations when data are transferred from one node to another.

(2) Some relational operations derive from unpredictable query strategies, particularly frequent in decisional applications. In these cases, time-consuming sequential processing procedures may occur however.

(3) The virtual database approach, as described in section 2, does not require the maintenance of all the source data on direct access devices; therefore, casual/indexed access to files stored on sequential devices (e.g., tape devices) cannot be used.

To reduce query complexity, as an alternative to partitioning the data set by indexes, we propose to minimize the query response time by:

(a) Reducing the cardinality of data sets by appropriate selections at the session definition stage;

(b) Reducing the degree of the relations by appropriate projections, at the previous stage;

(c) Pre-defining all the elementary conditions of classification foreseen by the user at a given time for each relation, and applying and storing them in the bitstring form.

In many real cases, it is possible to obtain a high compression factor of the original data by using these procedures.

Even if operations (a) and (b) can be carried out in many relational systems by using indexes, the time required to create sets of indexes for a given user can be lengthy. On the contrary, the materialization of the bitstring corresponding to a given set of conditions for each tuple is a simple, often linear operation.

Only one bit is required in the bitstring of the .String. file for each simple test. On the contrary, the multiple test requires round( $\log_{2}(m+1)$ ) or m bits, according to whether the equivalent m simple conditions are mutually exclusive or not.

A catalogued procedure can be 'permanent' or 'stored' in the mode. A permanent catalogued procedure is recorded in the executable form (e.g., see the matrix form in fig. 2). In this case, no additional storage is required in the .String. file. On the other hand, a stored catalogued procedure requires one bit to be allocated in the bitstring. Consequently, queries involving stored catalogued procedures are executed very fast.

The time when the .String. file for given .Data. and .Test. files should be materialized is very important in order to guarantee the semantic integrity of the session at the query time. In fact, with time, the user may update both the .Data. or .Test. files. Consequently, it is important that the (re-)materialization of the .String. file be subsequent to the last modification of the .Data. or .Test. files.

## 6. The Relational Operations

The basic data manipulation which is furnished to POLD users consists of the union, difference, intersection, selection, join, and projection operations. These are extensions of the corresponding relational operations [9,10].

As in relational algebra [11], the data manipulation is performed under the direct control of the user in order to avoid overloads in the network and to control semantic inconsistencies.

To properly understand the extended relational operations, it is opportune to view the POLD relation as mainly constituted by the two following parts:

(a) The informative part, consisting of a set of tuples of certain property values (the .Data. file);

(b) The descriptive part, consisting of a set of boolean values of simple tests, multiple tests, or (stored) catalogued procedures (the .String. file).

There exists a 1-1 correspondence between the .Data. tuples and the .String. tuples in the compound.

Although the information contained in the .String. file might sometimes be considered redundant with respect to that in the .Data. file, the .String. file has the following advantages:

\- The .String. file represents the information in more compact way than the .Data. file because only the properties relevant to the user are coded (in binary format);

\- The .String. file is the classification made by the user. Therefore, the user can maintain better control of semantic ambiguities;

\- The .String. file is internally processed as a sequence of bits. (The representation as a binary sequence is machine independent).

The POLD system performs the relational operations on the basis of the descriptive part of a relation (i.e., on the basis of the .String. files).

## 6.1. The Semantics of the Relational Operations

Let $X = \langle X.Data., X.Schema., X.Text., X.String. \rangle$ be a compound. In what follows, we denote the generic tuple of X.Data. by $D_x$ , and the bitstring of X.String. corresponding to $D_x$ by $S_x$ .

## 6.1.1. Union, Difference, and Intersection

Let A and B be two compounds such that
A elevated = B.Schema.
A.Test. = B.Test.

The compound resulting from the operations of union, difference, and intersection is the compound C whose .Schema. and .Test. files are so defined:

$$
\text { C.   Schema. } = \text { A.   Schema. }
$$

$$
\text { C.Test. } = \text { A.Test. }
$$

In order to specify the resulting C.String. and C.Data. files we introduce the following sets:

$$
\overline {{{\mathbf {D}}}} _ {\mathrm{A}} = \left\{\mathbf {D} _ {\mathrm{a}} \mid \nexists \mathbf {D} _ {\mathrm{b}}: \mathbf {S} _ {\mathrm{a}} = \mathbf {S} _ {\mathrm{b}} \right\}
$$

$$
\overline {{{\mathbf {S}}}} _ {\mathrm{A}} = \left\{\mathbf {S} _ {\mathrm{a}} \mid \nexists \mathbf {S} _ {\mathrm{b}}: \mathbf {S} _ {\mathrm{a}} = \mathbf {S} _ {\mathrm{b}} \right\}
$$

UNION.

In the compound $C = A \cup B$ it results that:
C.String. = $\overline{S}_{A} \cup B$ .String.
C.Data. = $\overline{D}_{A} \cup B$ .Data.

DIFFERENCE.

In the compound $\mathbf{C} = \mathbf{A} - \mathbf{B}$ it results that:
C.String. = $\overline{\mathbf{S}}_{\mathbf{A}}$ C.Data. = $\overline{\mathbf{D}}_{\mathbf{A}}$ .

INTERSECTION.

The compound $\mathbf{C} = \mathbf{A} \cap \mathbf{B}$ is defined by: $\mathbf{C} = \mathbf{A} - (\mathbf{A} - \mathbf{B})$ .

## 6.1.2. Selection and Join

$t_{x}$ be a subset of tests in X.Test., $\beta(t_{x})$ be a catalogued procedure on $t_{x}$ , and $s_{tx}$ be the sub-string of $S_{x}$ corresponding to $t_{x}$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
6.1.3. Projection
Let
$l_x$ be a list of attributes in X Lanka.,
$t_x$ be the set of tests in X.Test. referring only to the attributes in $l_x$,
$s_{tx}$ be the sub-string of $S_x$ corresponding to $t_x$,
$d_{lx}$ be the usual projection of $D_x$ on $l_x$.
The projection of the compound A on the attribute list $l_A$ is the compound C defined as follows:
C Lanka. = A Lanka. reduced to $l_A$
C.Test. = A.Test. reduced to $t_A$
C.String. = $\{s_{tA}\}$
C.Data. = $\{d_{lA}\}$
</div>

(we assume that $\beta(t_x) \equiv \beta(s_{tx})$ ).

SELECTION.

The selection of the compound A with respect to the condition $\beta(t_{A})$ is the compound C defined by:

C elevated. = A.Schema.

JOIN.

The join of the two compounds A and B with respect to the join condition $\beta(t_{A}, t_{B})$ is the compound C, such that:

C elevated. = A.Schema. ∪ B.Schema.

$$
= \left\{\mathrm{D} _ {\mathrm{a}} \cdot \mathrm{D} _ {\mathrm{b}} \mid \mathrm{S} _ {\mathrm{a}} \cdot \mathrm{S} _ {\mathrm{b}} \in \mathrm{C}. \text { String. } \right\},
$$

where ‘·’ represents the usual concatenation of tuples.

In particular, the equijoin condition $\beta_{E}$ defined by

$$
\beta_ {E} (t _ {A}, t _ {B}) = . \text { true. } \Leftrightarrow S _ {t A} = s _ {t B}
$$

corresponds to the extension of the usual equijoin.

## 6.2. Example of Relational Operations

The first example considered refers to a selection operation on the FLAT compound in fig. 2. Suppose we are interested in selecting the 'luxury flats'. We may define the concept of 'luxury flat' in terms of a boolean form of the existing simple and multiple tests in the FLAT.Test., that is, by means of a catalogued procedure cp. For example: cp Luxury-flat:

(bath\_room no. ≥ 2)

(heating system ≠ none);

which is equivalent, in terms of tests, to:

The Luxury-flat condition may be defined as permanent or stored. If the permanent mode is chosen, then the query condition is recorded in form of query matrix. Otherwise, i.e., if the stored mode is chosen, the Luxury-flat condition is simply added to FLAT.Test. (e.g., as test #37), and the FLAT.String. has to be updated.

The query matrix is obtained from the minimal canonical disjunctive form of the query condition – each row of the matrix corresponding uniquely to an OR minterm. The values in the row are defined as follows: the ith value is '1' if the ith test is requested 'true' in the OR term, '0' if it is requested 'false', or '\*' if it is requested 'don't care' (that is, if the ith test is not involved by the OR term). In other words, the '\*' value appears for all classification tests that are not relevant to the user's luxury flat concept. The query matrix form of the luxury-flat catalogued procedure is shown in fig. 2.

The selection procedure uses a fast algorithm, based on a three-valued $(0, 1, *)$ logic [1,7]. The algorithm applies the query matrix, suitably coded in binary, to each tuple in FLAT.String., and produces the truth value without having to access the FLAT.Data. tuple. (In the example in fig. 2, only the 7th bitstring, and therefore the flat #7, satisfies the selection condition).

The .Data. file of the resulting compound will contain exactly the tuples of FLAT.Data. that correspond to the tuples selected in FLAT.String..

The selection operation can also be involved when applying statistical functions to compounds. For example, the query 'count flats where Luxury-Flat' requires an internal selection operation on the Flat compound. In these cases, the user may be interested in knowing only the count result and not in the actual compound resulting from the selection. Therefore the POLD user is allowed to opportunely specify whether or not the compound has to be actualized.

![](/api/attachments/JK8YY3UF/fulltext/images/c16b9195983fae1f737553b121a518f2397fff04ff44852f849332c7390a178c.jpg)  
Fig. 5. The compound of flats for sale.

![](/api/attachments/JK8YY3UF/fulltext/images/da6e8960fbc7a42baf5297fd477351cf6603ccc759648273c7ee997ef877d664.jpg)  
Fig. 6. The compound of possible buyers of flats.

Now, the join operation will be considered. Suppose that the proprietors of the instanced flats have instructed a real estate agency to sell their flats. By a suitable preliminary manipulation of (a copy of) the Flat compound, the agency classifies the flats into the following orthogonal (i.e., mutually exclusive) categories: de luxe flats, first-class flats, second-class flats, and economic ones, as shown in fig. 5. The actual criteria adopted by the agency are not relevant to the comprehension of the example, and therefore are not listed. The flats 1 and 7 have been classified as the luxe ones, the flats 2, 5, and 6 as first class, flats 4 and 9 as second class and the others as economic flats. Moreover, the agency has at its disposal data referring to potential buyers; the data include the code of the client and his available funds. In order to propose a selected list of adequate flats to each client, the agency states the following classification of the available funds (shown in the Client compound in fig. 6):

\- Very High Availability (V.H.A.) has been defined as available funds $\geq 140$ (therefore, clients 'a' and 'b' have V.H.A.);

\- High Availability (H.A.) is defined as available funds in [80,150] (therefore, client 'b' is classified both V.H.A. and H.A.);

\- Mean Availability (M.A.) is defined as available funds in [50,90] (therefore, clients 'c', 'e', and 'f' have M.A.), and, finally,

\- Economic Availability (E.A.) is defined as available funds in [30,50] (client 'd' has E.A.).

Defining the join of compounds Client and Flat in order to produce the association between each client and the possible flats he could buy, the agency has to establish the proper semantic correspondence between type of flat and type of client availability.

If the association based on the strict semantic correspondence given in table 1 is adopted, then the corresponding join condition (boolean form of the tests given in figs. 5 and 6) is:

$$
\left(\mathrm{f} _ {1} \wedge \mathrm{c} _ {1}\right) \vee \left(\mathrm{f} _ {2} \wedge \mathrm{c} _ {2}\right) \vee \left(\mathrm{f} _ {3} \wedge \mathrm{c} _ {3}\right) \vee \left(\mathrm{f} _ {4} \wedge \mathrm{c} _ {4}\right).
$$

With reference to only the client and flat codes, the resulting sale proposals are those reported in table 2.

On the other hand, if an enlarged semantics of association of flats to clients is adopted, or if the former fails to give the desired results, then table 1 must be properly extended. Table 3 shows a possible extension; it consists of relating each fund availability class to its immediate predecessor and successor.

Table 1  
Strict semantic correspondence between type of flat and fund availability.

<table><tr><td>Flat category</td><td>Fund availability</td></tr><tr><td>de luxe</td><td>V.H.A.</td></tr><tr><td>1st class</td><td>H.A.</td></tr><tr><td>2nd class</td><td>M.A.</td></tr><tr><td>economy</td><td>E.A.</td></tr></table>

Table 2  
Sale proposal of flats underlying the semantics in table 1.

<table><tr><td>Client code</td><td>List of proposable flats</td></tr><tr><td>a</td><td>(1, 7)</td></tr><tr><td>b</td><td>(1, 2, 5, 6, 7)</td></tr><tr><td>c</td><td>(4, 9)</td></tr><tr><td>d</td><td>(3, 8, 10)</td></tr><tr><td>e</td><td>(4, 9)</td></tr><tr><td>f</td><td>(2, 4, 5, 6, 9)</td></tr></table>

Table 3  
Extended semantic version of table 1.

<table><tr><td>Flat category</td><td>Fund availability</td></tr><tr><td>de luxe</td><td>V.H.A., H.A.</td></tr><tr><td>1st class</td><td>V.H.A., H.A., M.A.</td></tr><tr><td>2nd class</td><td>H.A., M.A., E.A.</td></tr><tr><td>economy</td><td>M.A., E.A.</td></tr></table>

On the basis of table 3, the join condition

$$
\begin{array}{c} \left(\mathbf {f} _ {1} \wedge \left(\mathbf {c} _ {1} \vee \mathbf {c} _ {2}\right)\right) \vee \left(\mathbf {f} _ {2} \wedge \left(\mathbf {c} _ {1} \vee \mathbf {c} _ {2} \vee \mathbf {c} _ {3}\right)\right) \\ \vee \left(\mathbf {f} _ {3} \wedge \left(\mathbf {c} _ {2} \vee \mathbf {c} _ {3} \vee \mathbf {c} _ {4}\right)\right) \vee \left(\mathbf {f} _ {4} \wedge \left(\mathbf {c} _ {3} \vee \mathbf {c} _ {4}\right)\right) \end{array}
$$

can be derived. The resulting sale proposals are listed in table 4.

Table 4  
Sale proposal of flats underlying the semantics in table 3.

<table><tr><td>Client code</td><td>List of proposable flats</td></tr><tr><td>a</td><td>(1, 2, 5, 6, 7)</td></tr><tr><td>b</td><td>(1, 2, 4, 5, 6, 7, 9)</td></tr><tr><td>c</td><td>(2, 3, 4, 5, 6, 8, 9, 10)</td></tr><tr><td>d</td><td>(3, 4, 8, 9, 10)</td></tr><tr><td>e</td><td>(2, 3, 4, 5, 6, 8, 9, 10)</td></tr><tr><td>f</td><td>(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)</td></tr></table>

It is interesting to notice that the semantics in table 1, or the corresponding join condition, expresses a nearly equi-join. The usual equi-join would be produced if the agency adopted a classification of the fund availability into orthogonal categories.

## 6.3. Performance Evaluation

We discuss the performance evaluation with regard to the selection operation on a very large data set, since selection is the most frequently used basic operation.

Let us suppose that the .Data. file in the current compound has N tuples, each one stored on n bytes. We also suppose that the user has defined

$K_{s}$ simple conditions,

$K_{m}$ multiple tests, each one consisting of $m_{i}$ orthogonal conditions (i = 1, 2, ..., $K_{m}$ ), and $K_{p}$ catalogued stored procedures.

Therefore, each tuple in the .String. file requires

$$
\mathrm{S} _ {\mathrm{b}} = \mathrm{K} _ {\mathrm{s}} + \sum_ {1} ^ {\mathrm{Km}} \text { round } (\log_ {2} (\mathrm{m} _ {\mathrm{i}} + 1)) + \mathrm{K} _ {\mathrm{p}}
$$

bits, or, equivalently,

$$
\mathrm{S} _ {\mathrm{B}} = \operatorname{round} \left(\mathrm{S} _ {\mathrm{b}} / \mathrm{N} _ {\mathrm{b}}\right)
$$

bytes, where 1 byte = N $_{b}$ bits.

The compression factor obtained by the .String. file with respect to the .Data. file is n/S $_{B}$ .

If we denote by $C_{B}$ the track capacity in bytes of the disk, then each track can contain $N_{S} = \text{trunc}(C_{B}/S_{B})$ bitstrings and the .String. file will require round $(N/N_{S})$ tracks. Since the .String. file is sequentially processed, we must consider the minimum seek time. Moreover, no seek operation is required to read all tracks in the same cylinder. Therefore, the mean seek time is negligible. If R denotes the disk revolution time, an entire track is transmitted in the mean time $1.5 \times R$ . Therefore, each bitstring is transmitted at the rate $t_{s} = 1.5 \times R/N_{S}$ .

Example. We suppose that

$$
\begin{array}{l} \mathrm {K_ {s}} = 1 0 0, \\ \mathrm {K_ {m}} = 1 0, \text { and } \mathrm {m_ {i}} = 2 0 0, \text { for   each } \mathrm{i} = 1, 2, \dots , \mathrm {K_ {m}}, \\ \mathrm {K_ {p}} = 2 0, \\ \mathrm {C_ {B}} = 2 5 0 0 \text { bytes,and } \\ \mathrm{R} = 2 5 \text { msec. } \end{array}
$$

Then, assuming $N_{b}=8$ , it results that $S_{b}=200$ bits, that is, $S_{B}=25$ bytes. Thus, each bitstring is transmitted at the mean time of $t_{s}=0.375$ msec and the transmission rate $(1/t_{s})$ of $10^{3}\div10^{4}$ strings per second can be reached.

The selection procedure consists in evaluating a boolean form of the test values in the bitstring. The problem is to evaluate the boolean form in a time comparable to the transmission time $t_{s}$ . The algorithm used is based on a three-valued logic selection method [1,7] largely tested in Physics experiments of high statistics. The boolean form evaluation is reduced to a boolean matrix operation on the bitstring, where the boolean matrix is obtained directly from the boolean form. The time $t_{B}$ required for testing one bitstring has the upper limit [1]:

$$
\mathrm{t} _ {\mathrm{B}} \leq \text { round } (\mathrm{S} _ {\mathrm{b}} / \mathrm{w}) \times \left(\mathrm{t} _ {\mathrm{AND}} + \mathrm{t} _ {\mathrm{COMP}}\right) \times \mathrm{N} _ {\mathrm{OR}},
$$

where

w is the capacity in bits of the machine-word,

$t_{AND}, t_{COMP}$ are the time to execute the AND and the COMPARE logical instruction between words respectively, and

$N_{OR}$ is the number of the OR minterms in the minimal distributive form of the selection condition.

With reference to the previous example, if we assume w = 32, $t_{AND} = t_{COMP} = 10 \mu sec$ , and $N_{OR} = 3$ , then we have $t_{B} \leq \text{round}(200/32) \times (10 + 10)\mu sec \times 3 = 0.42 \text{ msec}$ ; that is, the processing rate is of the order of magnitude of $10^{3} \div 10^{4}$ bitstrings per second, comparable to the transmission rate.

With adequate buffering techniques, the transmission and selection times can be partially overlapped, thus gaining a total processing time of the same order of magnitude as above.

Since the computing time derives strictly from the sequential processing, then the ordering and any other physical allocation parameters of the bitstrings are not relevant. Consequently, in a multiprocessor environment, the parallel processing of a suitable partition of the bitstring set presents no problems, and improves the performance noticeably.

## 7. Conclusions

The POLD system has been used on a few real cases (nuclear physics experiments, regional planning, meteorological and environmental data management). The experiments carried out have shown that the POLD structure can satisfy most of the requirements of a scientific user in a distributed environment.

On the other hand, we wish to point out that the system was not designed to fulfill all the functional requirements of a distributed database system. For example, the concurrent updating, and, consequently, the lock and unlock techniques have not been analyzed. Furthermore, the optimization of the distributed transactions is left to the user.

In the system design we favoured efficacy criteria rather than efficiency criteria on the basis of the following considerations:

(1) In decision support information systems, particularly if distributed, it is very important to provide the user with feasible strategies to answer complex queries, while also furnishing reasonable response time to common queries. The sequential scanning method provided by the system permits a response time which is acceptable and competitive in comparison to other methods. However, we deem that the response time to particular queries in scientific/decision support environments is not the most important need of the user (obviously, within certain limits).

(2) More sophisticated data architectures may require time and money for software maintenance, and additional time for recovery and restart procedures. Moreover, they often are unable to furnish an acceptable reliability. On the contrary, POLD utilizes serial organization of files (inverted lists, multilists, tree indexes, and so on, are not used). This lowers the performance only in some cases (for example, when queries qualify only a few tuples, not frequent however in statistical, scientific and decisional applications). The experimentally obtained selection rate of $10^{3} \div 10^{4}$ elements per second is acceptable for the majority of research applications.

## References

[1] N. Armenise, G. Zito, A. Silvestri, E. Lefons, M.T. Pazienza, and F. Tangorra, POL: an interactive system to analyze large data sets, Computer Physics Communications 16, Nr. 2 (1979) 147–157.

[2] M.M. Astrahan, M.W. Blasgen, D.D. Chamberlin, K.P. Eswaran, J.N. Gray, P.P. Griffiths, W.F. King, R.A. Lorie, P.R. McJones, J.W. Mehl, G.R. Putzolu, I.L. Traiger, B.W. Wade, and V. Watson, System R: relational approach to database management, ACM Transactions on Database Systems 1, Nr. 2 (1976) 97–137.

[3] A.T. Berztiss, Data Structures: Theory and Practice (Academic Press, New York, 1975).

[4] M.W. Blasgen and K.P. Eswaran, Storage and access in relational data bases, IBM System Journal 16, Nr. 4 (1977) 363–377.

[5] R.H. Bonczek, C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, 1981).

[6] M.L. Brodie, On the development of data models, in: M.L. Brodie, J. Mylopoulos, and J.W. Schmidt, Eds., On Conceptual Modelling (Springer Verlag, New York, NY, 1984) 19–47.

[7] V. Capasso, A. Circella, and A. Silvestri, Una logica a tre valori per il calcolo del valore di verità di funzioni booleane complesse, CSATA Report, Bari (1974).

[8] D.D. Chamberlin, M.M. Astrahan, M.W. Blasgen, J.N. Gray, W.F. King, B.G. Lindsay, R.A. Lorie, J.W. Mehl, T.G. Price, F. Putzolu, P.G. Selinger, M. Schkolnick, D.R. Slutz, I.L. Traiger, B.W. Wade, and R.A. Yost, A history and evaluation of System R, Communications of the ACM 24, Nr. 10 (1981) 632–646.

[9] E.F. Codd, A relational model of data for large shared data banks, Communications of the ACM 13, Nr. 6 (1970) 377–387.

[10] E.F. Codd, Further normalization of data base relational model, in: R. Rustin, Ed., Data Base Systems (Prentice-Hall, Englewood Cliffs, NJ, 1971) 33–64.

[11] E.F. Codd, Relational completeness of data base sublanguages, in: R. Rustin, Ed., Data Base Systems (Prentice-Hall, Englewood Cliffs, NJ, 1971) 65–78.

[12] L. Colazzo, C. dell'Aquila, E. Lefons, A. Silvestri, and F. Tangorra, POLD: un sistema relazionale distribuito di supporto alle decisioni, Rivista di Informatica XVII, Nr. 1 (1987) 17–37.

[13] L. Colazzo and E. Lefons, Analytic data base modelling. Proceedings of IV International Conference on Statistical and Scientific Database Management (1988) Vol. 2, 101–126.

[14] D. Comer, The ubiquitous B-tree. ACM Computing Surveys 11, Nr. 2 (1979) 121–138.

[15] C.J. Date, An Introduction to Data Base Systems (Addison & Wesley, Reading, MA, 1981).

[16] C. dell'Aquila, E. Lefons, A. Silvestri, and F. Tangorra, POLD/2: specifiche di utilizzo del Query Editor per la creazione delle sessioni e delle procedure di interrogazione, CNR/PFI Report, DATANET 18 (1983).

[17] V. Di Gesù, A. Machì, and A. Alfano, Il sistema POLD per l'analisi di dati distribuiti: specifiche di utente del terminale intelligente ITERM, CNR/PFI Report, DATANET 16 (1983).

[18] T. Haerder, Implementing a generalized access path structure for a relational database system, ACM Transactions on Database Systems 3, Nr. 3 (1978) 285–298.

[19] G.D. Held, M.R. Stonebraker, and E. Wong, INGRES: a

relational data base system, Proceedings NCC 44 (1975) 409–416.

[20] W. Kent, Data and Reality (North-Holland, Amsterdam, 1981).

[21] D.E. Knuth, The Art of Computer Programming. Vol. 3: Sorting and Searching (Addison-Wesley, Reading, MA, 1973).

[22] IEEE, Special section on Statistical/Scientific database management, IEEE Transactions on Software Engineering 11, Nr. 10 (1985) 1038–1091.

[23] D. Lefkovitz, File Structures for On-line Systems (Spartan Books, New York, 1969).

[24] E. Lefons and A. Silvestri, The use of multidatabase in decision support systems, in: F.A. Schreiber and W. Litwin, Eds., Distributed Data Sharing Systems (North Holland, Amsterdam, 1985) 25–41.

[25] E. Lefons, Modello di oggetti funzionali per basi di dati analitiche, Rivista di Informatica XVIII, Nr. 3 (1988) 305–339.

[26] V.Y. Lum, Multi-attribute retrieval with combined indexes, Communications of the ACM 13, Nr. 11 (1970) 660–665.

[27] L.B. Methlie, Data management for decision support systems, Data Base 12, Nr. 1–2 (1980) 40–46.

[28] S. Rao Kosaraju, Insertions and deletions in on-sided height-balanced trees, Communications of the ACM 21, Nr. 3 (1978) 226–227.

[29] N. Roussopoulos, View indexing in relational databases, ACM Transactions on Database Systems 7, Nr. 2 (1982) 258–290.

[30] J.B. Rothnie Jr., P.A. Bernstein, S. Fox, N. Goodman, M. Hammer, T.A. Landers, C. Reeve, D.W. Shipman, and E. Wong, Introduction to a system for distributed databases (SDD-1), ACM Transactions on Database Systems 5, Nr. 1 (1980) 1–17.

[31] L.A. Rowe and M.R. Stonebraker, The POSTGRES Model, Proceedings of the 13th VLDB (1987) 83–96.

[32] T.K. Sellis, Intelligent caching and indexing techniques for relational database systems, Information Systems 13, Nr. 2 (1988) 175–185.

[33] A. Shoshani, Statistical databases: characteristics, problems and some solutions, Proceedings of the 8th VLDB (1982) 208–222.

[34] A. Shoshani, F. Olken, and H.K.T. Wong, Characteristics of scientific databases, Proceedings of the 10th VLDB (1984) 147–160.

[35] A. Silvestri, Scientific database modelling, Memorie Società Astrofisica Italiana 56, Nr. 2–3 (1985) 491–525.

[36] R.H.Jr Sprague and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, NJ, 1982).

[37] M.R. Stonebraker and E.J. Neuhold, A distributed data base version of INGRES, Proceedings of the 2nd Berkeley workshop on Distributed Data Management and Computer Networks LBL (1977) 19–36.

[38] R. Williams et al., R\*: an overview of the architecture, P. Scheuermann, Ed., Proceedings of the 2nd International Conference on Databases: Improving Database Usability and Responsiveness (Academic Press, New York, 1982) 1–27.
