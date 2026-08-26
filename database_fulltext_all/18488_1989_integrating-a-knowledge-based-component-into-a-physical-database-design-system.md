---
otero_id: 18488
otero_key: "K63RHZEM"
title: "Integrating a knowledge-based component into a physical database design system"
authors: "Christopher E. Dabrowski; David K. Jefferson; John V. Carlis; Salvatore T. March"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(89)90009-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating a Knowledge-Based Component into a Physical Database Design System

Christopher E. Dabrowski and David K. Jefferson
Information Systems Engineering Division, National Bureau of Standards, Gaithersburg, MD 20899, USA

John V. Carlis and Salvatore T. March
University of Minnesota, Minneapolis, MN 55455, USA

Physical database design is a difficult and complex process. Algorithmic approaches are appropriate for design subproblems, such as record segmentation and access path selection, but are infeasible for global design. A major problem with algorithmic approaches is that, for realistic databases, the number of alternative schema possibilities that must be evaluated to generate an optimal design is extremely large. Our design system addresses this problem by combining a knowledge-based component with an algorithmic component. The knowledge-based component reduces the solution space to a reasonable size by producing a small number of efficient schema alternatives. The algorithmic component develops a low cost design for each alternative. An example of the application of the KBS component of the design system is presented.

Keywords: Database design, Knowledge-based systems, Performance evaluation.

![](/api/attachments/K63RHZEM/fulltext/images/5e3cd63794eca14e8db92188b28e604561929e21ec7c53b035a536aa7593063f.jpg)

Christopher E. Dabrowski is a Computer Scientist at the National Computer and Telecommunications Laboratory at the National Institute of Standards and Technology. He received has MS in Computer Science from Johns Hopkins University in 1983. Mr. Dabrowski is active in research in database management systems, knowledge-based systems, and artificial intelligence.

## 1. Introduction

Database design deals with organizing data within a computer system so that the information and processing requirements of a community of users can be effectively and efficiently met. Two

![](/api/attachments/K63RHZEM/fulltext/images/e580915cfe8871e26e01155fb36c6dd0dd9bc336718c0bef2b33a6115da6bd8d.jpg)

David K. Jefferson received a BS in Mathematics, in 1960, from the California Institute of Technology, and a PhD in Computer Science, in 1969, from the University of Michigan. He is responsible for directing all programs of work in the Information Systems Engineering Division. These programs include research, development of Federal Information Processing Standards and guidelines, participation in the development of American National Standards and International

Standards, certification that software products conform to standards, and assistance to other Federal agencies. Areas of work include data management, data administration, computer graphics, knowledge-based systems, hypertext, and programming languages.

![](/api/attachments/K63RHZEM/fulltext/images/55bc161bab24e47b75236e3abbc1f3271cfb8676f00cae3b64cdcee3ac330ce2.jpg)

John V. Carlis is Associate Professor of Computer Science at the University of Minnesota. His research interests include physical database design, conceptual data modeling, and query languages. He is active in the IEEE International Conferences on Data Engineering, having served as program chair and general chair. He received a Ph.D. from Minnesota in MIS and a M.S. and B.S. From Penn State in Computer Science.

![](/api/attachments/K63RHZEM/fulltext/images/999be26ba888bb64f1f98e830235d530c488213104c16d2eadef9a71fa66c4a1.jpg)

Salvatore T. March is an Associate Professor of MIS in the Department of Information and Decision Science, Carlson School of Management, University of Minnesota. He received his BS, MS, and PhD degrees in Operations Research from Cornell University. Dr. March is active in teaching, research, and consulting in Database Design and Information Resource Management. He has published widely in such journals as Information and Management, ACM Computing Sur-

veys, ACM Transactions on Database Systems, The Journal of MIS, Database, and Management Science. He is currently the Editor-in-Chief of ACM Computing Surveys.

levels of database design are typically distinguished: logical and physical (see, for example, [22]). Logical database design is concerned with effectiveness of the database; i.e., insuring that its information content is appropriate for the user needs [9,23].

Physical database design is concerned with efficiency; i.e., meeting those information needs at minimum cost. It defines: how data are organized in secondary memory, what algorithms will be used to store and retrieve that data, and what additional (system) data will be maintained to support those algorithms. The importance of physical database design and its difficulty have been widely discussed in the literature $[6,13,28,32,34]$ . Numerous physical database design approaches have been proposed (see, e.g., $[1,12,14,25]$ ).

Analytic techniques have been successfully applied to physical database design subproblems such as access path selection $[8,11,16,26]$ and record design $[10,20,27]$ . However, they are insufficient to address entire design problems. Such problems contain integer decision variables, nonlinear constraints, and discontinuous objective functions. Problem and solution characteristics affect system performance in ways that defy exact analysis. In particular, algorithmic approaches have difficulty in grouping data items at the logical level into physical record structures due to the combinatoric nature of the problem.

This paper presents extensions to work reported in $[3,17,18]$ . That work presented an interactive physical database design system made up of four modules: FORM, CONVERT, DESIGN, and SELECT. FORM uses a set of heuristics (based on the logical structure of the data) and interaction with the human designer to generate a set of alternative database schemas termed skeletons. Skeletons are made up of groupings of data items (representing attributes and relationship descriptors at the logical level) called canonical records. CONVERT transforms the logical retrieval and update workload into access requirements for each unique canonical record contained in any skeleton, thus defining a set of file organization design problem that are solved by the DESIGN module. DESIGN uses computer system cost and performance parameters in several mathematical optimization algorithms to choose a low cost design for each file organization. A file organization design has three components: a record segmentation, a memory management scheme, and a set of file structures or access paths. SELECT chooses the set of file organizations that most efficiently meets the logical database requirements.

A knowledge-based component has been added to our algorithmic database design system $[7]$ . The knowledge-based component replaces the module called FORM and can make many of the decisions previously made by the human designer. For larger and more complicated databases, the structure based heuristics in FORM proved to be insufficient; often the number of alternatives generated was too large to evaluate. Conversely, situations arose where the heuristics discarded good alternatives. The burden was placed on the human designer to override the heuristics and reduce or enlarge the solution space. Much human and computer effort was expended in determining when to override the heuristics and what alternatives to add or delete under various conditions. As a result, criteria were formalized for overriding the heuristics and a knowledge-based system (KBS) component added to the design system. The KBS component is implemented in Lisp and currently contains over 400 rules. The algorithmic component contains in excess of 12,000 lines of FORTRAN.

The focus of this paper is the KBS component. Its task is to produce a reasonably small number of skeletons, retaining efficient ones, and discarding inefficient ones. It also contains a cost estimation module and rules to intelligently generate skeletons and provide a performance ranking. In this way the number of file organization design problems developed by CONVERT and solved by DESIGN can be more readily controlled.

## 2. A Model of Physical Database Design

## 2.1. Problem and Solution Descriptions

We require four types of information as input [4]:

(1) The logical structure and volume of the database (determined as a result of logical database design). To represent the database structure, we use a simple Entity-Attribute-Relationship model [5,29], termed a Logical Data Structure (LDS).

![](/api/attachments/K63RHZEM/fulltext/images/43b8110c38db08d4466d63f0a5c8c21543522c054bdab0fc3b05f2906ab7bdd6.jpg)  
Fig. 1. A Partial Logical Data Structure (LDS).

Dynamic aspects (such as integrity constraints) are reflected in the workload rather than in the data structure. An LDS has four major components: entity, attribute, relationship, and identifier. As in Fig. 1, entities are represented by ovals;

attributes (not shown in Fig. 1) by names connected to those ovals; relationships by arcs connecting entities; and identifiers by a symbol on the appropriate attribute(s) and relationship arc(s). Relationships are binary, connecting a pair of (not necessarily distinct) entities. Relationships cannot have attributes and only 1 to 1 and 1 to many relationships are allowed. The many side of a relationship is represented by a “chicken foot.” Many to many relationships and relationships with attributes must be converted into entities (this is what would happen during the normalization process in the relational approach). Since relationships are binary, each entity participating in a relationship may be viewed as both describing and being described by the other entity. Therefore a relationship has two relationship descriptors, reflecting the meaning of the relationship from the perspective of each entity. For example, the relationship between EMPLOYEE and DEPARTMENT in Fig. 1 has the relationship descriptors: EMPLOYEE-of-DEPARTMENT and DEPARTMENT-of-EMPLOYEE. Database volume is described by: entity cardinality (the number of instances); attribute length (encoding and compression can be treated separately); relationship descriptor degree (the cardinality of the “many” side of each relationship); and vocabulary size (size of the encoding alphabet) for each identifier attribute (required to evaluate hashing as a data storage and retrieval method).

```txt
{Retrieval 1}
SELECT EMPLOYEE_NAME, SSN, INSTITUTION_NAME, MAJOR
FROM EMPLOYEE,-- {FREQUENCY 500, PROPORTION 0.25}
EDUCATION-- {FREQUENCY 125000, PROPORTION 0.25}
WHERE EDUCATION-of-EMPLOYEE = SSN AND AGE < 30

{Retrieval 2}
SELECT *
FROM EMPLOYEE-- {FREQUENCY 1000, PROPORTION 1.0}

{Retrieval 3}
SELECT DEPARTMENT_NAME, EMPLOYEE_NAME, SSN, AGE
FROM DEPARTMENT,-- {FREQUENCY 500, PROPORTION 0.5}
EMPLOYEE {FREQUENCY 300000, PROPORTION 0.3}
WHERE DEPARTMENT-of-EMPLOYEE = DEPARTMENT_NAME AND AGE >50

{Retrieval 4}
SELECT EMPLOYEE_NAME, SSN, DEPARTMENT_NAME, START_DATE, END_DATE
FROM EMPLOYEE-- {FREQUENCY 10, PROPORTION 0.001}
EMPL_HISTORY {FREQUENCY 10, PROPORTION 0.001}
WHERE EMPLOYEE.SSN = ?
```  
Fig. 2. Partial Set of Retrievals for Fig. 1.

(2) The retrieval and update workload (estimated from expected or historical use). The retrieval workload is described by a set of retrieval activities, each being composed of some number of contexts. A context describes the activity at one entity and has selection, projection, and ordering criteria. Each context also has an associated frequency with which it is executed per unit time and an average proportion of instances selected during each execution of that context. Retrieval activity is forwarded from one context to the next. Fig. 2 shows part of the retrieval workload for the LDS of Fig. 1. Four retrievals are shown. Database Language SQL [31], augmented by some quantitative parameters, has been used in this example, because it is a commonly used, standard database language. Currently the system assumes that entities are navigated in the order specified in the query, e.g., (Retrieval 1) starts at EMPLOYEE and navigates to EDUCATION. Future work will develop a query optimization phase to transform SQL into an appropriate navigational form. Update workload is described by the frequency of insertion and deletion of entity-instances and the frequency of modification of attributes and relationships.

(3) The hardware environment description (specified by the hardware vendor or estimated from benchmark tests). The major parameters we require are: secondary memory access time (random and sequential), data transfer rate, maximum blocksize, cost of CPU and retrieval time, and cost of storage space. These parameters are used to evaluate the cost of storage, retrieval, and maintenance for a proposed design.

(4) The physical structures provided by the software environment. These constrain the solution space that can be considered. We model a generalized software environment based on frame memory $[3,19]$ that includes a wide range of record structures and access path variations. Files may be ordered to reduce retrieval and sorting costs. This solution space must be constrained to fit the target database management system.

A physical database design solution is defined as

(1) Record structures, the assignment of data items to physical records and the means of representing the necessary interconnections among those records, including any record aggregation and segmentation (or vertical partitioning) [15,21], as well as any data item duplication;

(2) Data set contents, the assignment of record instances to physical files (horizontal partitioning), and any data instance duplication;

(3) Access paths, algorithms and system data maintained for each data set to provide access to its physical data records; a primary access path (i.e., sequential, indexed, hashed, or clustered according to its relationship to some other record) determines the physical location of data records; secondary or auxiliary access paths (e.g., indexes or linked lists) support user requests that are not efficiently satisfied by the primary access path; and

(4) Maintenance mechanisms, algorithms and system data to manage secondary memory space, including allocation and management of overflow space and space for (partial) reorganizations, as required by the selected access paths.

A file organization is a single data set together with its associated access paths and maintenance mechanisms. A physical database is a set of interconnected file organizations.

## 2.2. Forming Canonical Records

A major set of decisions in physical database design involves how to represent relationship descriptors. These determine which relationship descriptors will become stored data items and which will not. Hence they (partially) define the database schema. Each relationship in an LDS must be represented in the physical database; however, since there are two relationship descriptors for each relationship, it is possible to represent only one relationship descriptor physically (i.e., as a stored data item) and infer the other from it via some access path. There are three ways in which relationship descriptors can be represented:

\- absorption, where the two entities of a relationship are stored in the same physical area; the relationship descriptor is represented by proximity; for example, a repeating group of EMPLOYEE instances within a DEPARTMENT instance (a common structure in CODASYL

DBMSs; such a physical structure is also available in the Relational DBMS Oracle [24]), or the replication of DEPARTMENT data for each EMPLOYEE instance (a pre-join of EMPLOYEE and DEPARTMENT tables),

\- symbolic pointer, where one entity contains the logical identifier of the other; for example, storing the dept-id value with EMPLOYEE (as in Relational DBMSs) or storing a repeating group of emp-id values with DEPARTMENT; and

\- direct pointer, where one entity contains the physical address of the other; for example, a repeating group of system pointers to EMPLOYEE instances within a DEPARTMENT instance (a set implemented by a pointer array with DEPARTMENT as owner and EMPLOYEE as member in a CODASYL DBMS), or a single system pointer to the DEPARTMENT instance for each EMPLOYEE instance.

Some of these representations may be used in combination. For example, both direct and symbolic pointers could be used to represent a single relationship descriptor (as in a CODASYL set with a STRUCTURAL clause). Similarly, both absorption and pointers could be used (as in hierarchic DBMS where the child is physically stored with the parent).

A canonical record is a physical grouping of one or more entities acyclically connected by absorption. Canonical records may be segmented during the detailed fine-tuning of file organization design. The number of canonical records for which file organizations are designed depends on the set of relationship representations chosen.

Choosing a small set of reasonably good representations is critical to our database design approach. For each relationship, at least one of its descriptors must be represented in at least one of the ways described above. Carlis [2] identified 23 feasible ways in which any one relationship (both of its descriptors) could be represented as shown in Fig. 3. He argued that embedded pointers within an absorbed record structure are not efficient, leaving 17 reasonable representations (cells labeled 1, 2, 3, 5, 10, and 15 are eliminated from Fig. 3). The number of skeletons for a database is then 17 raised to the number of relationships. For each skeleton, canonical records must be formed and for each canonical record a file organization designed. These latter steps of physical database

<table><tr><td></td><td>A</td><td>SP</td><td>DP</td><td>SP+DP</td><td>None</td></tr><tr><td>A</td><td>X</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>SP</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>DP</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>SP+DP</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td></tr><tr><td>None</td><td>20</td><td>21</td><td>22</td><td>23</td><td>X</td></tr></table>

Legend: A = Absorption  
SP = Symbolic Pointer  
DP = Direct Pointer  
None = No stored representation (implicit)

Fig. 3. Feasible Relationship Representations (X indicates Infesible).

design are amenable to algorithmic solution. However, the number of alternatives from the former step must be reduced to make this approach feasible.

Some sets of relationship representation allow us to divide an LDS into clusters where a cluster is a set of entities and relationships such that all relationships between entities in different clusters are fixed at a single non-absorbing representation. Multiple representations may be considered for relationships between entities within a cluster. Fixing representations for inter-cluster relationships allows us to vary representations independently within each cluster since there is no impact on the design of other clusters.

Since the number of alternatives for a cluster is exponential in the number of relationships, dividing an LDS reduces the number of skeletons from a product of products to a sum of products. In an LDS with 10 entities and 12 relationships, for example, there are of $17^{12}$ possible skeletons, one for each alternative relationship representation. If a set of relationships can be identified such that fixing representations for those relationships will divide the LDS into three clusters of, say 3, 3 and 4 entities each, then (assuming each of the clusters has three relationships with 17 alternatives each) there are $3 * 17^3$ possible skeletons. This number may be further reduced by reducing the number of alternatives considered for one or more of the relationships within a cluster. The number of unique canonical records (for which file organizations must be designed) is typically much lower than the number of skeletons since many skeletons may contain the same canonical record; however, reducing the number of skeletons will significantly reduce the number of unique canonical records.

To illustrate the complexity of the design problem, consider the relationship between EMPLOYEE and EDUCATION in Fig. 1. Its two relationship descriptors are: EMPLOYEE-of-EDUCATION and EDUCATION-of-EMPLOYEE. Since the identifier of EDUCATION contains the relationship descriptor EMPLOYEE-of-EDUCATION, EDUCATION is dependent on EMPLOYEE – an EDUCATION instance cannot exist without a corresponding EMPLOYEE instance. From this structure a human designer should conclude that absorption is a reasonable representation for EDUCATION-of-EMPLOYEE with EMPLOYEE-of-EDUCATION being represented implicitly. Substituting EMPLOYEE for Entity\_1 and EDUCATION for Entity\_2, this corresponds to the cell labeled 20 in Fig. 3. A relatively large EMPLOYEE file would result.

Examining the workload requirements could cause the designer to conclude differently. {Retrieval 2} of Fig. 2 represents a significant amount of large subset retrieval on EMPLOYEE that is not forwarded along EDUCATION-of-EMPLOYEE - EDUCATION is not required for the selected EMPLOYEES. This may lead the designer to represent EMPLOYEE-of-EDUCATION with a symbolic pointer and EDUCATION-of-EMPLOYEE implicitly (cell 9 in Fig. 3). The entities would be stored separately, resulting in a smaller EMPLOYEE file and a reduced cost for {Retrieval 2}.

{Retrieval 1} of Fig. 2 represents a substantial amount of large subset activity on EMPLOYEE which is forwarded along EDUCATION-of-EMPLOYEE. This information, together with the structural dependence of EDUCATION on EMPLOYEE, would argue for the absorption of EDUCATION into EMPLOYEE.

After considering all the facts, the designer would most probably want to try both representations and compare the results after designing detailed fine organizations. This would result in two skeletons and three canonical records. Skeleton 1 contains two canonical records: EMPLOYEE and EDUCATION. Skeleton 2 contains one, a hierarchical record with EDUCATION absorbed as repeating group into EMPLOYEE. A file organizations would be designed for each canonical record. Actual problems involve many more considerations and result in an enormous number of alternatives.

## 3. Using a KBS Approach in Physical Database Design

Our KBS approach incorporates techniques used by human designers to reduce the number of alternatives to be analyzed algorithmically. As discussed above, one such technique is to divide the LDS into clusters, such that structural and workload interrelationships are strong within clusters and weak among clusters. Relationships that connect clusters can be represented by pointers without significant degradation of performance of the composite design.

A second technique is to recognize and characterize small portions of the LDS with critical structural and workload features. Such units may be individual entities or relationships or small groups of entities and relationships. A simple example is an entity with a very large amount of large subset retrieval; a canonical record consisting of that entity alone should be considered. Such characterizations help a human designer to concentrate analysis and design on significant, problematic portions of the LDS and devote less effort to other areas that are less critical.

Combining different pieces of analytical information to choose among alternate design structures is a third technique used by human experts. A small portion of the LDS consisting of one or more relationships and entities may have many conflicting characterizations. For example, workload requirements may include large subset retrievals with different ordering criteria or the same entity may be involved in many retrievals some of which require only instances of that entity, others of which require instances of other, related entities. Human experts can consider conflicting criteria when choosing representations and canonical records. The result is a deeper analysis and understanding than that which would be obtained by considering diverse characterizations in isolation.

KBS technology provides a way in which this type of expertise can be stored and applied by a computer program. We have transformed knowledge about physical database design into rule form. A rule is an IF - THEN pair. The IF part (or antecedent) lists one or more conditions; the THEN part (or consequent) lists conclusions which are reached if all the conditions of the antecedent are satisfied. These rules are represented in an internal knowledge-base and applied by an inference engine to physical design problems. A problem is represented internally as a database of facts to which the rules are applied. Application of rules results in the conclusion of new facts leading to decisions about which design actions are to be undertaken and in what sequence.

Along with its rules, our KBS also makes use of certainty factors which allow for inexact judgment and enhance the reasoning power of the system. Certainty factors are a numeric measure of the degree to which a fact, concluded by the application of a rule, is believed to be true (or false). Absolute certainty is 1.0; absolute denial is -1.0. Certainties are used to order or eliminate alternatives. For example, we can establish a certainty cut-off for carrying representations through to detailed design.

For complicated sequences of reasoning, certainties are derived from the certainty factors of the facts which satisfied the antecedent portion of the rules involved. The inference engine is responsible for the derivation of certainty factors. A number of algorithms exist for determining combined certainty [33]. We base our method on the Bernoulli formula [30]. Using this formula, if two certainty factors $C_{1}$ and $C_{2}$ are both positive or both negative and are associated with different rules concluding the same fact, then they are combined using the function $C_{3} = C_{1} + C_{2} * (1 - C_{1})$ . The final positive and negative factors are combined by simple summation. Certainty factors are useful in making judgmental conclusions, taking into account different and possibly conflicting evidence. Use of certainty factors allows the KBS to select from among several possible alternatives and to make “best guess” approximations.

The current KBS architecture is divided into: (1) a high-level or control module for overall control of the problem solving process and (2) a set of lower level modules each having a set of rules to perform certain design tasks. Both the control module and the lower-level modules operate via backward chaining.

## 3.1. The Control Module

The control module is responsible for overall control of the design process. It decides what types of design actions to perform on various portions of the LDS. Fig. 4 shows the possible design actions and identifies the subsections below in which each is explained.

When a problem is posed to the KBS, the first action taken is to characterize all entities and relationships by transforming numeric data into category data as required by the design rules. Entities are characterized by volume (e.g., large, small), type (e.g., independent, intersection, aggregate, dependent), and retrieval and update activities (e.g., large, small subset). Relationships are characterized by the direction and volume of retrieval and update activity. Next, an initial set of reasonable representations is specified for each relationship. The control module iterates over clusters (the entire LDS at first) applying design actions according to its rules. Three types of design actions are available: problem size reduction, canonical record formation, and cluster recombination. Two approaches are available for problem size reduction: (1) problem decomposition through division of the cluster, and (2) restriction

![](/api/attachments/K63RHZEM/fulltext/images/64a09eb57fe6d2a2a960a90ba2dac35ae989dc11833a513aeaaecfe061efe5c9.jpg)

\* Design actions for problem reduction
LDS Division
Direct problem size reduction

\* Design actions for canonical record formation
Enumeration of alternative skeletons
Selective generation of skeletons

\* Cluster recombination

Fig. 4. A Diagram of High-Level Design Actions.

of relationship representations within the cluster. Both actions reduce the number of skeletons for a cluster. If a cluster is divided, then each new cluster is considered for further design actions. Two approaches are also available for generating efficient canonical records in the chosen cluster: (1) complete enumeration for clusters with a small number of possible skeletons or (2) selective generation of a limited number of skeletons for clusters with many potential skeletons. Finally, cluster recombination combines (parts of) adjacent clusters and creates temporary clusters incorporating some of the entities and relationships from the adjacent clusters. These are considered for further design actions. This permits the identification of additional, potentially efficient canonical records that could not be found by processing the adjacent clusters individually.

## 3.1.1. Characterizing Entities and Relationships

One set of rules in the knowledge base is used to characterize entities and relationships according to structure and workload. These rules are applied once and the resulting facts characterizing the LDS are stored internally. They provide a basis for decisions made by other parts of the system in subsequent design work. The rules in Fig. 5 illustrate this characterization. Consider substituting the EDUCATION-EMPLOYEE relationship for ?Rel-id, EDUCATION for ?Entity, and EMPLOYEE for ?Other-entity. {RULE A} characterizes EDUCATION as a dependent entity. {RULE B} characterizes the relationship descriptor EDUCATION-of-EMPLOYEE as having a high level of activity (the frequency of activity from EMPLOYEE to EDUCATION exceeds half of the frequency of both entities combined). {RULE B} also characterizes the relationship descriptor EMPLOYEE-of-EDUCATION as having high activity. {RULE C} combines both characterizations into a complex characterization stating that the relationship is a possible design problem because it has high activity in both directions (from ?Entity to ?Other-entity and from ?Other-entity to ?Entity).

## 3.1.2. Selecting Relationship Representations

Another set of rules determines a set of reasonable representations for each relationship in the LDS. These rules rely heavily on the above characterizations. They are invoked to propose which representations should and should not be used, each with an associated certainty factor.

Several different possible representations may be concluded for a relationship and one or more representations may be rejected for the relationship. More than one rule may be invoked to make a positive or negative conclusion about a representation with each rule corresponding to a different reason for the conclusion. The same representation may be both concluded and rejected.

```powershell
(RULE A)
IF RELATIONSHIP?Rel-id ?Entity ?Other-entity ?Rel-name
PRIMARY-IDENTIFIER ?Entity ?Identifier
EQUAL ?Rel-name ?Identifier
THERE-IS --> ATTRIBUTE ?Entity ?Att-name NON-IDENTIFIER
THEN
DEPENDENT-ON ?Entity ?Other-entity

(RULE B)
IF REL-ACTIVITY ?Rel-id ?Entity ?Other-entity
?Subset-size ?Rel-frequency
ENTITY-ACTIVITY ?Entity ?Entity-frequency
ENTITY-ACTIVITY ?Other-entity ?Other-entity-frequency
GREATER-THAN ?Rel-frequency 1/2 (SUM ?Entity-frequency ?Other-entity-freq)
THEN
CHARACTERIZE ?Rel-id ?Entity ?Other-entity HIGH-ACTIVITY

(RULE C)
IF CHARACTERIZE ?Rel-id ?Entity ?Other-entity HIGH-ACTIVITY
CHARACTERIZE ?Rel-id ?Other-entity ?Entity HIGH-ACTIVITY
THEN
POSSIBLE-DESIGN-PROBLEM ?Rel-id HIGH-BI-DIRECTIONAL-ACTIVITY
```  
Fig. 5. Example Rules for Entity and Relationship Characterization.

```txt
(RULE D)
IF RELATIONSHIP ?Rel-id ?Ent1 ?Ent2 ?Rel-name
DEPENDENT-ON ?Ent2 ?Ent1
THEN
POSSIBLE REPRESENTATION ?Ent1 ABSORBS ?Ent2
CERTAINTY FACTOR 0.5

(RULE E)
IF RELATIONSHIP ?Rel-id ?Ent1 ?Ent2 ?Rel-name
DEGREE ?Rel-id ?Ent1 to ?Ent2 is 1 to M
THEN
POSSIBLE REPRESENTATION ?Ent2 SYMBOLIC-POINTS-TO ?Ent1
CERTAINTY FACTOR 0.5

(RULE F)
IF ACTIVITY ?Rel ?Ent1 to ?Ent2 is HEAVY
THEN
POSSIBLE REPRESENTATION ?Ent1 ABSORBS ?Ent2
CERTAINTY FACTOR 0.25

(RULE G)
IF ACTIVITY ?Rel-id ?Ent1 to ?Ent2 is HIGH
DEPENDENT-ON ?Ent2 ?Ent1
ABSENT --> DEPENDENT-ON ?Any-entity ?Ent2
THEN
PREVENTS REPRESENTATION ?Ent2 SYMBOLIC-POINTS-TO ?Ent1
CERTAINTY FACTOR 0.25
Fig. 6. Rules for Selecting Representations.
```

An overall determination about using a particular representation is concluded by other rules that combine the positive and negative information. The certainty factor associated with this combined determination is calculated from the certainty factors of the invoked rules as discussed above. Those relationship representations which have a certainty factor of sufficient strength are regarded as reasonable representations. These are retained for use in subsequent design actions.

Fig. 6 shows example rules for selecting relationship representations. Continuing the EMPLOYEE-EDUCATION example, since EDUCATION is dependent on EMPLOYEE, {Rule D} proposes absorption as a possible representation and {RULE E} proposes an M to 1 symbolic pointer. Absorption is also recommended by {RULE F} based on a high activity level. Using the Bernoulli method, we combine the certainty factors for {RULE D} (0.5), and {RULE F} (0.25) to obtain a combined certainty for absorption of 0.625 (0.625 = 0.5 + 0.25 \* (1.0 - 0.5)). {RULE E} recommends an M to 1 symbolic pointer with a certainty of 0.5. The certainty of using a symbolic pointer is decreased to 0.25 (0.25 = 0.5 - 0.25) by {RULE G} which provides a negative certainty factor. This rule states that an M to 1 symbolic pointer should not be used if there is high retrieval activity in the 1 to M direction, if dependency exists along the relationship, and if there are no entities dependent on the M entity. Although absorption has a higher associated certainty, both representations have sufficient certainty to warrant further examination.

## 3.2. Design Actions for Problem Reduction

Because real database design problems have too many reasonable alternative schemas for exhaustive enumeration, the size of the problem must be reduced. There are two types of design actions to reduce the problem size: (1) iterative division of the LDS into clusters and (2) reduction of the number of chosen representations for relationships in a cluster.

## 3.2.1. Dividing the LDS

Dividing an LDS (or an LDS cluster) reduces the problem size by forming smaller, independent problems which sum to the larger problem. Division is done if the LDS is found to contain a large number of entities and relationships which can be processed as smaller, separate clusters. The goal is to produce a few clusters of moderate size in which the amount of workload complexity within the clusters significantly exceeds the complexity on relationships which connect the clusters.

Dividing an LDS requires the use of a division rule set. This rule set determines a set of breakpoints, that is, relationships such that the problem is subdivided when they are fixed at some non-absorbing representation (representations 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, or 23 in Fig. 3). Representing a relationship by absorption (representations 1, 2, 3, 4, 5, 10, 15, and 20) requires that both entities belong to the same cluster.

Fig. 7, for example, shows the division of the LDS using the relationship between DEPARTMENT and DATA-CENTER and the relationship between DATA-CENTER and DRAWING as breakpoints. Fixing each of these relationships to any non-absorbing representation divides the LDS into three clusters. In this example, DATA-CENTER-of-DRAWING and DATA-CENTER-of-DEPARTMENT are represented by symbolic pointers. DRAWING-of-DATA-CENTER and DEPARTMENT-of-DATA-CENTER are represented implicitly (no data items are stored for these relationship descriptors).

![](/api/attachments/K63RHZEM/fulltext/images/7ef00d2adde4b64d10bc7b4704959106395b572fa70cb09bcf6eeb24405873af.jpg)  
Fig. 7. A Three Cluster Division of the LDS of Fig. 1 (SP indicates a symbolic pointer).

Division rule sets are segregated according to predetermined criteria for breakpoint selection established by the human designer. These criteria specify different levels of workload characterizations at which a relationship would qualify as a potential breakpoint. Less restrictive criteria will generate more breakpoints and fewer alternative representations; the problem is easier to solve but efficient representations may not be considered, resulting in less than satisfactory solutions. Therefore these rule sets are applied in order of the degree of restrictiveness in their breakpoint selection criteria, with the most restrictive rule set being applied first. This ordering facilitates the goal of having clusters with high workload on relationships relating entities within a cluster and low workload on the relationships connecting clusters.

Fig. 8 shows examples of breakpoint selection rules. {RULE H}, {RULE I}, and {RULE J} are examples of rules which indicate that a relationship should not be used as a breakpoint due to the relationship being characterized as a “possible design problem.” Such relationships are termed bondpoints. {RULE K} is a breakpoint selection rule associated with a rule group for a certain restriction level. The restrictiveness criterion associated with this level is given by the negation of the three types of bondpoints. The sixth clause specifies the unique condition associated with this particular breakpoint rule: the relationship activity characterization of LOW-PERCENTAGE-FORWARDED-ACTIVITY. This means that a low percentage of the activity focusing on ?Ent1 is forwarded along the relationship ?Rel-id.

```txt
{RULE H}
IF POSSIBLE-DESIGN-PROBLEM ?Rel-id HIGH-BI-DIRECTIONAL-ACTIVITY
THEN
    BOND-POINT ?Rel-id HIGH-BI-DIRECTIONAL-ACTIVITY

{RULE I}
IF POSSIBLE-DESIGN-PROBLEM ?Rel-id HIGH-LARGE-SUBSET-RETRIEVAL
THEN
    BOND-POINT ?Rel-id HIGH-LARGE-SUBSET-RETRIEVAL

{RULE J}
IF POSSIBLE-DESIGN-PROBLEM ?Rel-id HIGH-NON-FORWARDING-ACTIVITY
THEN
    BOND-POINT ?Rel-id HIGH-NON-FORWARDING-ACTIVITY

{RULE K}
IF SELECTED-BREAK-RULE-GROUP RESTRICTION-LEVEL-1
RELATIONSHIP ?Rel-id ?Ent1 ?Ent2 ?Rel-name
NOT << BOND-POINT ?Rel-id HIGH-NON-FORWARDING-ACTIVITY >>
NOT << BOND-POINT ?Rel-id HIGH-LARGE-SUBSET-RETRIEVAL >>
NOT << BOND-POINT ?Rel-id HIGH-BI-DIRECTIONAL-ACTIVITY >>
CHARACTERIZATION ?Rel-id LOW-PERCENTAGE-FORWARDED-ACTIVITY
THEN
BREAK-POINT ?Rel-id RESTRICTION-LEVEL-1
```  
Fig. 8. Examples of Breakpoint Selection Rules.

## 3.2.2. Restricting Relationship Representations

Dividing and LDS into clusters is one way to reduce the number of skeletons (and hence canonical records) generated. Restricting the number of representations for a relationship within a cluster is another. As already discussed, there are 17 possible ways to represent a relationship. Different representations are suited to different structure and workload characteristics. The significance of choosing an inappropriate representation for a relationship also depends on the workload volume. This design action identifies critical relationships, those for which there are a number of appropriate representations (as indicated by the workload characterization) and for which choosing an inappropriate representation would have a significant impact on the performance of the system. A set of alternative representations is generated for each critical relationship. The remaining relationships are restricted to the representation having the highest certainty factor. Since a unique skeleton exists for each alternative representation of each relationship, this action results in a reduction of the number of skeletons and canonical records.

## 3.3. Design Strategies for Forming Canonical Records

Our KBS includes two strategies for forming canonical records: complete enumeration and selective generation. Both use a skeleton cost estimation function which accepts a skeleton description and workload information and returns an estimated retrieval and update cost for each entity and relationship in the skeleton. The cost estimator is relatively simplistic and makes numerous assumptions about the design. Its importance is not in generating accurate cost estimates (this is done in detailed design), but in providing a general ranking of skeletons to help establish which are potentially efficient. Alternately, we could invoke the DESIGN module and actually do detailed design for selected skeletons at this point. More accurate cost estimates would be made for the designed file organizations, but due to computational expense, fewer alternatives would be evaluated.

## 3.3.1. Enumeration of all Alternative Skeletons

For clusters having a small number of alternative relationship representations, the resultant skeletons are enumerated and canonical records formed. As skeletons are enumerated, the cost estimation function is applied to each skeleton. Then, the skeletons are ranked by cost and a set of low-cost skeletons is selected. The canonical records of these skeletons are retained for detailed design. High-level rules exist to choose this design action for smaller clusters which have first undergone relationship restriction, or for small clusters having few skeletons. It is too time consuming for clusters having a large number of critical relationships.

## 3.3.2. Selective Generation of Records and Skeletons

For clusters with many alternate relationship representations, the combinatoric explosion is averted by selectively generating skeletons. The goal of this strategy is to identify a small number of skeletons having good performance characteristics without enumerating all of the alternatives. The canonical records of these skeletons are selected for detailed design.

The selective generation of skeletons employs a generate and evaluate strategy. The knowledge base has a set of rules to support this process. First, costs are estimated for an initial skeleton having relationship representations chosen on the basis of highest certainty factors. Subsequently, different rules are invoked which selectively vary relationship representations to produce new skeletons and cost estimates. These rules combine the structure and workload characteristics with previously estimated costs to identify relationships which should be varied based on estimated high workload cost or on the existence of problems.

The process of selecting relationships to vary is aided by identification of efficient canonical records and representations previously generated in other skeletons. Similarly, high-cost structures which should not be regenerated may be identified. Selection of relationships to be varied is followed by the invocation of rules which pick an appropriate representation for each.

Once the relationship representations have been selected, a new skeleton is generated and its costs estimated. The new skeleton and its canonical records are added to an internal list of skeletons for the LDS cluster. If the cost of the new skeleton is too high, it will be pruned from the search space. The cost breakdown serves as a basis for identification of high-cost and low-cost relationship representations and canonical records in the new skeleton that will be used when varying relationship representations in subsequent actions. The selective skeleton generation process proceeds as follows:

(1) The control module selects a skeleton from the list for the cluster.

(2) Relationships and alternative representations are selected using cost information, initial characterizations, and previously identified efficient and inefficient canonical records (labeled good and bad records). The conclusions are stored with the design information for the current skeleton.

(3) A new skeleton is generated using the altered relationship representations.

(4) The new skeleton is evaluated and efficient and inefficient relationship representations and canonical records, if any, are identified. The new skeleton is added to the cluster skeleton list.

(5) A new skeleton or relationship in the same skeleton may be selected for further design; or work on the current cluster may be terminated and low-cost skeletons and canonical records selected.

## 3.4. Recombination of Divided Clusters

Cluster recombination, in part, compensates for the shortcomings of dividing an LDS. When an LDS is divided into clusters, a single non-absorbing representation is chosen for each relationship between entities in different clusters. These are chosen on the basis of certainty factors. Representations for these connecting relationships cannot be varied when doing work on a cluster (to do so would necessitate considering the two clusters together, thus negating the benefits of having initially created the clusters). However, maintaining separate clusters and not varying breakpoint relationships can result in overlooking good designs. This is especially so where less restrictive criteria for workload complexity were used in breakpoint selection.

![](/api/attachments/K63RHZEM/fulltext/images/3eb9b3dcde22fe56ff4b4f4bf0ee6a22e989116e363cb8bc4d2751570a4e6a98.jpg)  
Fig. 9. A New Cluster Created from Combining Portions of Two Clusters in Fig. 7. (SP indicates symbolic pointer).

In cluster recombination, a temporary cluster is created from portions of adjacent clusters. The new hybrid cluster consists of the connecting relationships between the original clusters together with limited portions of those clusters corresponding to low-cost canonical records involved in the connecting relationships. The new hybrid cluster then becomes the subject of further design activity. Fig. 9 shows a such new cluster. The control module determines which adjacent clusters should be combined, initiates and controls the design actions to form canonical records in the hybrid cluster, and analyzes the results of these actions by comparing the canonical records having a low estimated cost in the hybrid cluster with the canonical records of the originals. The result may lead to an adjustment in the canonical records submitted for detailed file organization design.

## 4. An Example of KBS Physical Database Design

A simplified example using cluster 1 from the LDS and the given workload illustrates the cumulative effect of invoking the selective skeleton generation rules. An initial set of reasonable relationship representations is shown in Fig. 10. The EMPLOYEE-DEPARTMENT relationship (REL\_1) has three alternative representations, and the EMPLOYEE-EDUCATION (REL\_2) and

![](/api/attachments/K63RHZEM/fulltext/images/37b20ba8785bfc6635d7ba19b6afe9b487219e2f1bb26df01bec61ec3ab1bbd5.jpg)  
Fig. 10. An Initial Set of Reasonable Representations.

EMPLOYEE\_EMP\_HISTORY (REL\_3) relationships each have two, for a total of $(3 \times 2 \times 2) = 12$ skeletons. Actual clusters are typically much larger and contain many more relationships, reasonable representations, and alternative skeletons.

Figs. 11 and 12 show two skeletons (numbered 1 and 2, respectively) and their estimated costs. The cost of an entity is the sum of the retrieval and update costs for all activities in which it is involved. The cost of a relationship is the sum of the cost to process updates on that relationship and to traverse that relationship in all the retrievals in which it is involved.

In skeleton 1, EDUCATION and EMPL-HISTORY are absorbed into EMPLOYEE, which in turn is absorbed into DEPARTMENT, creating a single three-level hierarchical canonical record (canonical record 1). In skeleton 2, there are two canonical records. DEPARTMENT is the single entity in canonical record 2 while EDUCATION and EMPL-HISTORY are absorbed into EMPLOYEE forming canonical record 3, a two-level hierarchical record.

Both skeletons have 0 cost for EDUCATION and EMPL-HISTORY. There is no retrieval activity on either of these entities that does not begin at EMPLOYEE and both entities are absorbed into EMPLOYEE in both skeletons. Therefore there is no additional cost to retrieve EDUCATION or EMPL-HISTORY beyond that which is expended to retrieve the EMPLOYEE data. However, absorbing EDUCATION and EMPL-HISTORY into EMPLOYEE results in a significant cost for EMPLOYEE since the EMPLOYEE record is so big.

![](/api/attachments/K63RHZEM/fulltext/images/38993c289ee636a2dc3b1a42e19c78220ce1c13debfdd20d6af17b0993820ec8.jpg)  
Fig. 11. Skeleton 1.

<table><tr><td>Cost (DEPARTMENT)</td><td>=</td><td>108</td></tr><tr><td>Cost (EMPLOYEE)</td><td>=</td><td>1614</td></tr><tr><td>Cost (EDUCATION)</td><td>=</td><td>0</td></tr><tr><td>Cost (EMPL-HISTORY)</td><td>=</td><td>0</td></tr><tr><td>Cost (REL_1)</td><td>=</td><td>0</td></tr><tr><td>Cost (REL_2)</td><td>-</td><td>0</td></tr><tr><td>Cost (REL_3)</td><td>=</td><td>1</td></tr><tr><td colspan="2"></td><td>1723</td></tr></table>

![](/api/attachments/K63RHZEM/fulltext/images/f576dd6ff062f1061352bfa65789720e5db7086551486d40b712be171b5f0f32.jpg)  
Fig. 12. Skeleton 2.

![](/api/attachments/K63RHZEM/fulltext/images/1f0807148324e32e8cbda889b321fa82322d0718d0ad3a451ae7c54ec589986b.jpg)  
Itemized Costs for Entities and Relationships  
Fig. 13. Skeleton 3.

REL\_1 also has a high cost in both skeletons. In skeleton 2, REL\_1 is represented with a symbolic pointer from EMPLOYEE to DEPARTMENT and has a retrieval frequency of 300,000 (see {Retrieval 3}). REL\_1 has a significant, but much lower cost in skeleton 1. This is due to the fact that EMPLOYEE is absorbed into DEPARTMENT requiring employee data to be physically moved when an EMPLOYEE changes DEPARTMENTS. It is somewhat offset by the additional DEPARTMENT cost incurred because EMPLOYEE (and EDUCATION and EMPL-HISTORY) data must be transferred when DEPARTMENT data is required.

The following sequence of actions illustrated how the KBS would attempt to generate a better skeleton.

Step 1. Select a skeleton for processing. Skeleton 1 is selected based on its lower cost.

Step 2. Choose a relationship representation to be varied. Rules for selection of relationships to be varied are applied to the problem. Since the representation for REL\_1 has already been varied (in skeleton 2, resulting in a high relationship cost), it is not considered again. The high cost of the hierarchic EMPLOYEE record (and associated relationships) triggers a rule that selects a relationship along which to decouple the absorbed entities and reduce the size of the canonical record. REL\_3 is recommended because it is traversed less frequently than REL\_2.

Step 3. A symbolic pointer from EMPL\_HISTORY to EMPLOYEE is selected for REL\_3.

Step 4. As shown in Fig. 13, skeleton 3 is created with two new canonical records labeled 4 and 5. The cost is lowered to 1723.

Skeleton 3 is added to the list of skeletons for this cluster and may itself become the subject for further design activity. At the conclusion of processing, the more efficient canonical records in skeleton 3 would be chosen for file organization design over those of skeletons 1 and 2.

## 5. Conclusion and Directions for Further Research

Augmenting our algorithmic database design system with a KBS component is a significant advance in developing effective physical database design tools. The strictly algorithmic approaches are appropriate for design subproblems, such as record segmentation and access path selection, but are infeasible for global design. Our KBS component uses rules and an inference engine to address a major problem of algorithmic approaches: how to reduce the large number of alternative schema possibilities (or skeletons) that must be evaluated to generate a near optimal design. Each skeleton defines a number of file organization design problems, each of which is solved by the algorithmic component.

Future research will include an evaluation and refinement of both the KBS and algorithmic components of the database design system through application to a number of database design problems. We expect to identify additional rules and meta-rules as such problems are addressed and the solutions compared with those of database design experts. For example, additional rules for cluster recombination will be sought and included in the KBS component. Other areas of future research include using SQL to describe the workload and adding rules for query optimization. While this will add a great deal of complexity to the rule set, in the KBS approach such rules can be included without drastic modifications to the architecture of the system. We expect the addition of such rules to significantly enhance the utility of the system.

## References

[1] M.L. Brodie and Nesson, S., “Physical Design Advisor (PDA): An Expert System Design Aid for the Physical Design of Model 204 Databases,” Computer Corporation of America, March 1987.

[2] Carlis, J.V., “An Investigation into the Modeling and Design of Large, Logically Complex, Multi-user Databases,” Ph.D. thesis submitted to University of Minnesota, Minneapolis, Minnesota 55455, December 1980.

[3] Carlis, J.V. and March, S.T., "A Computer Aided Physical Database Design Methodology," Computer Performance (4,4), December 1983, pp. 198–214.

[4] Carlis, J.V. and March, S.T., "A Descriptive Model of Physical Database Design Problems and Solutions", Proceedings International Conference on Data Engineering, IEEE, April 24–27, 1984, Los Angeles.

[5] Chen, P.P., “The Entity-Relationship Model – Toward a Unified View of Data,” ACM Transactions on Database Systems, (1,1) March 1976, pp. 9–36.

[6] Christodoulakis, S., "Implications of Certain Assumptions

in Database Performance Evaluation," ACM Transactions on Database Systems, (9,2) June 1984.

[7] Dabrowski, C.E. and Jefferson, D.K., A Knowledge-Based System for Physical Database Design, NBS Special Publication 500-151, National Bureau of Standards, February 1988.

[8] Fedorowicz, J., "Database Performance Evaluation in an Indexed File Environment," ACM Transactions on Database Systems, Vol 12, No 1, March 1987.

[9] Fong, E.N., Henderson, M.W., Jefferson, D.K., and Sullivan, J.M., Guide on Logical Database Design, NBS Special Publication 500-122, National Bureau of Standards, February, 1985.

[10] Hammer, M. and Niamir, B., “A Heuristic Approach to Attribute Partitioning,” Proc ACM SIGMOD, Boston, May 30-June 1, 1979.

[11] Hoffer, J.A. and Kovacevic, A., “Optimal Performance of Inverted Files,” Operations Research, (30,2), March–April 1982.

[12] Hubbard, G.U., Computer Assisted Data Base Design, Van Nostrand-Reinhold DP Series, 1981.

[13] Jefferson, D.K., “The Development and Application of Data Base Design Tools and Methodology,” Proceedings of the Very Large Data Base Conference, Montreal, October 1–3, 1980.

[14] Kao, S., “Decides: An Expert System Tool for Physical Database Design,” Proceedings of the IEEE Data Engineering Conference 1985.

[15] March, S.T., “Techniques for Structuring Database Records,” ACM Computing Surveys (15,1), March 1983.

[16] March, S.T., “A Mathematical Programming Approach to the Selection of Access Paths for Large, Multiuser Databases,” Decision Science (14,4), Fall 1983.

[17] March, S.T. and Carlis, J.V., “Physical Database Design: Techniques for Improved Database Performance,” in Kim, W., Reiner, D., and Batory, D. (eds.), Query Processing in Database Systems, Springer-Verlag, 1985.

[18] March, S.T. and Carlis, J.V., “On the Interdependencies Between Record Structure and Access Path Design,” Journal of MIS, Vol 4, No 2, Fall 1987.

[19] March, S.T., Severance, D.G., and Wilens, M., “Frame Memory: A Storage Architecture to Support Rapid Design and Implementation of Efficient Databases,” ACM Transactions on Database Systems, Vol. 6, No. 3, September 1981.

[20] March, S.T. and Scudder, G.D., “On the Selection of Efficient Record Segmentations and Backup Strategies for Large Shared Databases,” ACM Transactions on Database Systems, (9,3), September 1984.

[21] Navathe, S., Ceri, S., Wiederhold, G., and Dou, J., “Vertical Partitioning Algorithms for Database Design,” ACM Transactions on Database Systems, (9,4), December 1984.

[22] Navathe, S.B. and Schkolnick, M., "View Representation in Logical Database Design," Proceedings of the SIGMOD International Conference on Management of Data, Austin TX, May 31–June 2, 1978.

[23] Olle, T.W., Sol, H.G., and Verrijn-Stuart, A.A., eds., Information Systems Design Methodologies: A Comparative Review, New York: North-Holland Publishing, 1982.

[24] Oracle Database Administrators Guide, Version 5.1, Belmont CA, August 1986.

[25] Reiner, D. et. al., “A Database Designer’s Workbench,” Proceedings of the Fifth International Conference on Entity-Relationship Approach, Dijon, France, November 17–19, 1986.

[26] Schkolnick, M., “The Optimal Selection of Secondary Indexes for Files,” Inf Syst, (1), 1975.

[27] Schkolnick, M., "A Clustering Algorithm for Hierarchical Structures," ACM Transactions on Database Systems, (2,1), March 1977.

[28] Schkolnick, M. and Tiberio, P., “Estimating the Cost of Updates in a Relational Database,” ACM Transactions on Database Systems, Vol 10, No 2, June 1985.

[29] Senko, M.E., “DIAM as a Detailed Example of the ANSI SPARC Architecture”, in Nijssen, G.M., (ed.), Modelling in Database Management Systems, Proc. IFIP-TC-2

Working Conference, Freudenstadt, Germany, North-Holland Publishing Co., Amsterdam, January, 1976.

[30] Shafer, G., A Mathematical Theory of Evidence, Princeton University Press, Princeton, 1976.

[31] ISO-ANSI (working draft) Database Language SQL2, ANSI X3H2-89-001, ISO DBL SYD-2a, October, 1988.

[32] Teorey, T. and Fry, J., Design of Database Structures, Prentice-Hall, Inc, Englewood Cliffs, 1982.

[33] Thompson, T.R., “Parallel Formulation of Evidential Reasoning Theories”, Proceedings of the Ninth International Joint Conference on Artificial Intelligence, Los Angeles, CA, 1985.

[34] Wiederhold, G., Database Design, McGraw-Hill Book Company, New York, 1983.
