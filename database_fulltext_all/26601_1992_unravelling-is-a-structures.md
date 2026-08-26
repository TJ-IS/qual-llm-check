---
otero_id: 26601
otero_key: "F6JCJ6UN"
title: "Unravelling Is-a Structures"
authors: "Robert C. Goldstein; Veda C. Storey"
year: "1992"
journal: "Information Systems Research"
doi: "10.1287/isre.3.2.99"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.105.215.146] On: 16 September 2016, At: 21:05 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## H4R

## Information Systems Research

![](/api/attachments/F6JCJ6UN/fulltext/images/5849dce67f66e9efd576f78cedc56995e7fe47e5ba850dbb40b3b3c34a3fc2e6.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Unravelling Is-a Structures

Robert C. Goldstein, Veda C. Storey,

## To cite this article:

Robert C. Goldstein, Veda C. Storey, (1992) Unravelling Is-a Structures. Information Systems Research 3(2):99-126. http:// dx.doi.org/10.1287/isre.3.2.99

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1992 INFORMS

Please scroll down for article—it is on subsequent pages

## informs

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

Unravelling Is-a Structures

Robert C. Goldstein Fuculty of Commerce and Bustness Admunıstratton

Unversity of British Colunbia

2053 Main Mall

Vancouver, British Colunbia. Canada V6T 1Z2

Veda C. Storey W illiam E–Sion Graduate School of Busiess Admintstration

Unversity of Rochester

Rochester, New York 14627

Is-a relationships are widely recognized as conveying important information for database design. Although these relationships are implicitly hierarchical in nature, it is not uncommon to find collections of is-a relationships that form nonhierarchical structures. This paper formally defines is-a structures and classifies and interprets them. It illustrates how is-a structures can be used to identify possible database design errors or inefficiencies and to produce a database design that incorporates more of the semantics of an application

Database design—1s-a relatonships—Lattices --Integrıty constraints

## 1. Introduction

he need to augment database designs in order to capture more of the semantics of applications has been widely recognized. For example, according to Meersman (1988): “. . . databases sorely need the ability to incorporate much more semantics from present-day applcation domains into the represented information structures " One well-known technique for accomplishing this is the use of data abstractions (see for example, Smith and Smith 1977). In general, an abstraction is a simplified description, or specification, of a system that emphasizes some of the system's details or properties while suppressing others (Shaw 1984). Inclutsion is the class of abstractions that deals with subset relationships and is generally denoted by is-a  In a relationship A is-a B. B is referred to as the generic entity type and 1, the specitic entity type. Alternatively, one can say that 1 is a specialization of B (Peckham and Maryanski 1988). The well-known inheritance property of ts-a relationships states that something which is true of a generic entity type must also be true of its specific entity types (Brachman 1983). Database designers can take advantage of this property to reduce redundancy by representing each fact at its highest level of generalization and by eliminating from specific entity types properties that can be inherited from their generic entity type(s).

This paper strives to present a comprehensive, coherent analysis of the use of is-a structures in database design. Specifically, the objectives of the research are to:

• define, illustrate, and classify is-a relationships and discuss their semantic significance.

• provide a framework, along with guidelines, for the proper incorporation of is-a relationships into database design methodologies.

• show how the existence of certain is-a structures can be used to infer possible database design problems and semantic integrity constraints.

The analysis is intended not only for database designers, but also for automated database design tools. A number of such tools have been developed including expert systems (for example, SECSI (Système Expert en Conception d’Informations) (Bouzeghoub et al. 1985); EDDS (Expert Database Design System) (Choobıneh 1985; Choobineh et al. 1988); CARS (Computer Aided Requirements Synthesis) (Demo and Tilli 1986): View Creation System (Storey 1988; Storev and Goldstein 1988, 1990) and other knowledge-based approaches (for example, A VIS (Automated View Integration System) (Wagner 1989): Modeller (Tauzovich 1989, 1990).2 Examples of ones that incorporate ts-a relationships include: (1) the E-R Translator (Briand et al. 1985), an expert system for translating an entity-relationship diagram into a database; (2) Modeller (Tauzovich. 1989, 1990), an expert system for conceptual database design which is part of a larger project to develop an intelligent database design assistant; and (3) SECSI (Bouzeghoub et al. 1985), an expert system that creates a relational model from the user's description of an application that includes is-a relationships.

The rules for identifying the various cases presented in the analysis should be explicit enough so that they could be programmed. Once an ts-a structure is recognized as matching one of the general cases, the rules specify how this structure should be modified either to correct a design error or improve efficiency. In certain cases, semantic integrity constraints can also be generated automatically.

The contribution of this research is a detailed analysis of is-a relationships that shows how this semantic relationship should be interpreted by database design methodologies. The use of is-a relationships to identify certain semantic integrity constraints is also illustrated.

This paper is divided into nine sections. §2 defines various types of is-a structures. §3 discusses database design and introduces a case study that will be used for the examples in the rest of the paper. A framework for analyzing ts-a structures is then presented that classifies the structures into four cases which are examined in detail in §4, §5, §6, and §7. respectively. §8 discusses the limitations of the analysis. A summary and concluding remarks are found in §9.

![](/api/attachments/F6JCJ6UN/fulltext/images/854d4812bf650690d52737139f4425b82dfcd3154a89b26044204d7af7087095.jpg)  
FiGURF1 Sumple A-A Relatonship

## 2. Definitions

In this research, ts-a structure is used as a generic term. Before analyzing such structures in detail, it is important to distinguish among s-a relationshıps, s-a hierarchies, and ¿s-a lattices.

## 2.1. Is-A Relationships

Throughout this paper, the following definitions are used:

• X is-an A means that every occurrence of X is also an occurrence of A (Schneider and Trepied 1989). This is known as an inclusion dependence (Arisawa and Miura 1986). For example, Instructor ts-a Faculty implies that every instructor is a faculty member. X is-an A is denoted as:

## XC.1.

Note that X is a strict subset of A. The reason that equality is not considered is that it would result in synonyms, and hence redundancy, in the design.

In a relationship, 4 ts-a B, A is called the specific entity type and B, the generic entity type. This relationship is represented diagrammatically by an arrow from the specific to the generic entityv type as shown in Figure 1 (Sehneider and Trepied 1989; Teorey et al. 1989).

• The meaning of an is-a relationship should not depend on any other relationships that either the specific or generic entity types participate in. Thus. if two s-a relationships, (X is-an A) and (X is-a B). are given, this must mean that every occurrence of X is an occurrence of both .1 and B. This is denoted as:

$$
X \subset (A \cap B).
$$

For example, Graduate\_Student is-a Student and Gruduate\_Student is-a Person imply that every Graduate\_Student is both a Student and a Person.

2.1.1. Properttes. Although ts-a relationships are usually defined as above, it is possible to provide a more formal definition in terms of the property sets of the participating entities. Let $\boldsymbol { { \cal P } } _ { \mu }$ . called the property set of entity type .1. be the set of properties common to all occurrences of the entity type .1. Then. for entity types 4 and B, A ts-a B if and only if $P _ { \ell }$ is a proper subset of $P _ { \mu }$ (see Wand 1989):

![](/api/attachments/F6JCJ6UN/fulltext/images/1f824e8fefe60f13f0dd1e6d63ccacdc9cbd0bcb5e7af466161648c66ae4b5fd.jpg)  
FIGURE 2. Sımple I-4 Hierarchy.

$$
I. e.: (A \subset B) \quad \text {   iff   } \quad (P _ {b} \subset P _ {a}) \quad \text {   and   } \quad P _ {a} \neq P _ {b}.
$$

We rule out the case of $P _ { a } = P _ { b }$ because it implies that the entity types A and B are absolutely indistinguishable, that is, that two labels are being applied to the same thing. In database design, it is important to maintain a one-to-one correspondence between concepts in the real world and terms in the database.

Because they will be used later in the paper, the following relationships concerning the property sets of unions and intersections are also introduced. The property set of the union of entity sets is the intersection of their property sets:

$$
I. e.: (A \cup B) \text {   has   the   property   set   } (P _ {a} \cap P _ {b}).
$$

The property set of the intersection of entity sets is the union of their property sets:

$$
I. e.: (A \cap B) \text {   has   the   property   set   } (P _ {a} \cup P _ {b}).
$$

## 2.2. Is-A Hierarchies

Given a relationship, A is-a B, it is possible, of course, that the generic entity type B can be the specific entity type in another relationship, $B \ i s { a \ C }$ , producing an is-a hierarchy as illustrated in Figure 2. In a hierarchy, a node cannot have multiple parents nor can it be its own ancestor. That is, cycles are not permitted. A more complex is-a hierarchy is shown in Figure 3. Note that the $A _ { \iota } \mathrm { \Sigma } _ { \mathrm { { S } } }$ represent distinct entity types, not occurrences of the single entity type A

## 2.3. Is-A Lattices

Database design examples have appeared in the literature (e.g., Maryanski and Hong 1985; Greenspan et al. 1982) in which an entity type, X, is the specific entity type in more than one is-a relationship, X is-an $A _ { 1 } , X$ ts-an $A _ { 2 } , . . .$ . as shown in Figure 4.3 When this occurs, the resulting structure is no longer a hierarchy, but rather a lattice. A lattice is an acyclic, directed graph (see, for example, Banerjee et al

![](/api/attachments/F6JCJ6UN/fulltext/images/12fd1f5e7c881778b92065c83c6265d6c173ea2bf2b188b3dfcc17743f59642a.jpg)  
FIGURE 3. Complex 1-A Hicrarchy

1987; Stefik and Bobrow 1986). It is a more general structure than a hierarchy in that it allows a node to have multiple parents. However, like a hierarchy, it excludes the possibility of a node being its own ancestor.

## 3. Database Design

In their work on semantic data models. Maryanski and Hong (1985) suggest that a database designer begin the design process by drawing an ts-a diagram that identifies the entity types of an application and depicts the subset-superset relationships. After this high level specification is complete, details about the entities can then be obtained. In other words, they suggest starting with a diagram of all entity types that can be related through ¿s-a relationships. The examples used in this paper are based on the University database discussed in Maryanski and Hong (1985) but expanded to provide a richer basis for analysis.

![](/api/attachments/F6JCJ6UN/fulltext/images/8f73a39c1eb01df2df35c73b624f6ca4318ba934c1f2a42c796206c2a2337664.jpg)  
FiGuRE 4. General Form of -A Lattice.

## 3.1. Inheritance

The inheritance property of ts-a relationships implies that, if A is-a B, all of the properties of B must be attributable to A4 (Brachman 1983, Tanimoto 1987). In, for example, a relational database design, any (nonkey) attributes of B, that also appear in A, can be deleted from .4 because A can simply “inherit" them from B. This improves the efficiency of a design because it helps to minimize redundancy and thus, avoid update problems when information that needs to be changed (for example, an address) is stored in more than one place in the database.

A University database design might include the following is-a relationships:

E.g:

Student is-a Person

Foreign-Student is-a Student.

A relational implementation would include:

Person. [SSN, name, address, phone, birthdate]

Student. [SSN, student-number, department, program]

Foreign-Student: [SSN, citizenshıp, visa-status]

In this example, Student inherits the attributes “name," “address," “phone," and “birthdate"from Person. Foreign-Student inherits the attributes “student-number," “department," and “program" from Student, along with the attributes that Student inherits from Person Such inheritance is possible because of the transitivity of is-a relationships (Reiter 1984, Tanimoto 1987).

Object-oriented systems allow for the possibility of inheritance exceptions (Stefik and Bobrow 1986, Touretzky 1986). For example, the Student entity might have an attribute “work-assignment" which could not be inherited by Foreign-Student 4 In conventional database managemcnt, inheritance would probably be implemented by defining user views in which all relevant attributes (including the inherited ones) of each entity type are explicitly included (Date 1986). This would make it essentially impossible to permit inheritance exceptions. Therefore, for the remainder of this analysis, we assume that an is-a relationship implies full property inheritance.

## 3.2. Potential Design Problems

Certain is-a structures indicate possible database design problems. For example, in some cases, is-a lattices are valid and arise during the normal course of developing a conceptual database design. In other cases, however. multiple parents for a node appear because of a design error or as an artifact of the design methodology as illustrated below.

• Each entity type in a relationship plays a particular and distinct role (Goldstein 1985). For example, students take courses; courses do not take students. An inexperienced designer can easily confuse the concept of a “specific" entity type with that of a role. For example, one might specify the relationships, Instructor is-a Faculty-Member, and Instructor is-a Graduate-Student, thereby implying that Instructor is a specific entity type of both Faculty-Member, and Graduate-Student Yet, it is certainly not true that each instructor is both a faculty member and a graduate student. In this case, it is clear that “Instructor" is merely a role that can be plav ed by either of these entity types. If there are unique properties associated with being an instructor, then a separate Instructor entity type should be defined. However, its relationship to Facultv-A1ember and Graduate-Student should be something other than 1s-a

• An ts-a lattice can be produced during the view integration process if an entity type appears as the specific entity type in different relationships in different views. One user view, for example, might have a relationship Graduate Student ts-a Student whereas another view might have a relationship Graduate Student is-a Person If these views were simply combined without any consideration given to the relationship between the generic entity types, then Graduate Student would appear as a specific entity type of both Student and Person when an ts-a hierarchy would have been appropriate.

• Automated database design tools usually identify relationshıps one at a time. This lack of a global perspective can easily lead to the specification of a set of ts-a relationships that give rise to a lattice.

The existence of an is-a lattice in a database design may indicate erroneous or missing relationships. It is a signal that the particıpating relationships should be investigated to ensure that the design is correct. The /s-a structures analyzed in §4, §5, §6, and $\ S 7$ provide database designers (or design tools) with a framework that can be used to identify and correct such errors. Specifically, the framework provides a complete way to categorize ts-a relationships so that they can be examıned for design errors or inefficiencies. Then rules are provided for dealing with each case so that a design will be obtained that properly reflects the application semantics with minimal redundancy.

## 3.3. Framework for Analyzing Is-a Lattices

The general form of the structure being investigated in this paper is the ts-a lattice shown in Figure 4. The proper interpretation of such a structure depends critically upon understanding the correct relationship among the generic entity types. Specifically, the framework used for analyzing these structures consists of four cases:

• C’ase I. There exists a nesting of the generic entity types . 1, . In other words, the generic entity types can be ordered such that:

$$
A _ {i} \subset A _ {i + 1} \quad \forall i, \quad 1 \leq i <   n.
$$

This case is illustrated in the University database where all Graduate-Students are Students and all Students are People.

• Case II. There is some overlap among all of the generic entity types:

![](/api/attachments/F6JCJ6UN/fulltext/images/a0f1be04430027edf5800c9763e9dc84b73bbd838e7d5c83300da9eeb9ae17bd.jpg)  
FiGURE 5. Case 1: Initial Scheme

$$
\bigcap_ {i = 1} ^ {n} A _ {i} \neq \varnothing .
$$

In a University, some Students are also Employees, for example, Research-Assistants. However, the overlap is only partial since there are also Students who are not Employees and vice versa.

• Case III. The $\cdot 1 _ { \iota }$ 's can be arranged into $k$ groups such that the jth group $( A _ { 1 } ^ { j } , \ldots ,$ $A _ { n _ { i } } ^ { \textit { \prime } } )$ has the nesting property of Case I and the most specialized $\mathcal { A } _ { \iota } \mathbf { \dot { s } }$ from each group $( . \dot { 1 } _ { 1 } ^ { \prime } \dot { \bf s } )$ are mutually exclusive:

$$
A _ {1} ^ {l} \cap A _ {1} ^ {l} = \emptyset , \quad \forall j \neq l, \quad 1 \leq j, \quad l \leq k.
$$

This is illustrated by the university example where no Instructor can be more than one of the generic entity types.

• Case IV. Combinations of Cases I, II, and III.

## 4. Case I—-Nested Generic Entity Types

The first case to consider is an ts-a lattice of the form X is-an $A _ { i } \colon 1 \leq i \leq n$ , and suppose that the generic entity types can be ordered such that:

$$
A _ {i} \subset A _ {i + 1} \quad \forall i, \quad 1 \leq i <   n.
$$

This is illustrated in Figure 5 where each Graduate-Student is-a Student and each Student is-a Person (so A, = Graduate-Student; $A _ { 2 } = { \ o { S t u d e n t } { ; } { \mathcal { A } } _ { 3 } } = { \ o { P e r s o n } { ) } }$

All but one of the original is-a relationships, X is-an A, , must either be redundant or incorrect. An ts-a relationship is redundant if it is implied by other relationships An is-a relationship is incorrect if it implies something that is not true; for example, an invalid property inheritance. (See Atzeni and Parker (1986) for further discussion on redundant and incorrect relationships.)

## 4.1. Incorrect Relationship

It is possible that some of these is-a relationships are not correct. Since the $\textstyle A _ { t } ^ { \star }$ s are ordered by the nesting property, $A _ { i } \subset A _ { i + 1 }$ , the following is true (by the law of transitivity (Atzeni and Parker 1986, Tanimoto 1987)):

$$
(X \not \subset A _ {j}) \Rightarrow (X \not \subset A _ {j - i}, \forall i, 1 \leq i <   j).
$$

Let / denote the minimum i such that $X \subset . 4 ,$ . Then the incorrect relationships (X is-an $A _ { i } , 1 \le i < l )$ should be removed

![](/api/attachments/F6JCJ6UN/fulltext/images/36ec2eb1ed0870b4843d2e600122c6b21605f4271e6a3dcbc7538706c185f2b9.jpg)  
FiGURE 6. Abstract Solution to Case I

## 4.2. Redundant Relationship

In terms of Figure 4, if $X \subset \cdot 4 _ { t } .$ , then, by the law of transitivity, the following also holds:

$$
X \subset A _ {i}, \quad \forall i, \quad l <   i \leq n.
$$

Thus, it is redundant to include X ts-an $A _ { \iota } , l < \iota \leq / \iota$ , since these are implied. The redundant relationships should be removed, resulting in a simple hierarchical structure as shown in Figure 6.

## 4.3. Application to Example

In the University example of Figure 5, if there can be some foreign students who are not graduate students, then the relationship Foreign-Student $\lambda . 5 \AA$ Graduate-Student is incorrect. Similarly, the relationship Foreign-Student is-a Person is redundant and can. thus, be deleted. Foreign-Student can still inherit the properties of Person via the relationship Student is-a Person. Removal of these relationships results in the solution shown in Figure 7

## 4.4. Case I: Database Design Implications

• The specific entity type, X, cannot, of course, inherit any properties via the incorrect relationships. The transitivity property ensures that X can inherit all properties that would have been inherited via the redundant relationships.

## 5. Case II—All Generic Entity Types Overlap

Case Il reflects situations where all of the generic entity types overlap simultaneously; that is:

$$
\bigcap_ {i = 1} ^ {n} A _ {i} \neq \varnothing .
$$

The $A _ { \iota } { \bf \dot { s } }$ can be organized into h groups and ordered within each group so that the nesting property holds. The number of $. { \bf \dot { d } } _ { i } \dot { \bf \Phi } _ { \bf S }$ in the /th group is $n _ { \mathrm { \Omega } _ { i } }$ . That is:

$$
\begin{array}{l} A _ {i} ^ {j} \subset A _ {i + 1} ^ {j} \quad \forall i, \qquad 1 \leq i <   n _ {j} - 1, \quad \forall j, \qquad 1 \leq j \leq k \qquad \text { and: } \\ \sum_ {j = 1} ^ {k} n _ {j} = n. \end{array}
$$

![](/api/attachments/F6JCJ6UN/fulltext/images/c810cd065ecf5865a98c71e27aa41e7f17c1907a7c2ab26002e803bdb5416cc0.jpg)  
FiGuRE 7 Case I: Corrected Seheme

Therefore, the groups are:

$$
\left(A _ {1} ^ {1} \subset A _ {2} ^ {1} \subset \dots \subset A _ {n _ {1}} ^ {1}\right), \left(A _ {1} ^ {2} \subset A _ {2} ^ {2} \subset \dots \subset A _ {n _ {2}} ^ {2}\right), \dots ,
$$

1st group

$$
\begin{array}{c} \text { 2nd   group } \\ (A _ {1} ^ {j} \subset A _ {2} ^ {j} \subset \dots \subset A _ {n _ {t}} ^ {j}), \ldots , (A _ {1} ^ {k} \subset A _ {2} ^ {k} \subset \dots \subset A _ {n _ {k}} ^ {k}). \end{array}
$$

/th group

h th group

Each group $1 . 1 1 1$ is essentially an example of Case I. Grouping the $. 1 , \mathrm { \dag } \mathrm { s }$ in this manner allows one to consider only the most deeply nested entity type of each group. namely, $. 1 { } _ { 1 } ^ { \prime }$ Also note that none of the $\mathbf { { 1 } } _ { 1 } ^ { \prime } \mathbf { \bar { s } }$ is a subset of any other:

$$
A _ {1} ^ {p} \not \subset A _ {1} ^ {q} \forall p \neq q, \quad 1 \leq p, \quad q \leq k.
$$

Thus, it suffices to relate the specific entity type X to these $. 1 _ { 1 } ^ { \prime } \mathrm { { \dot { s } } }$ rather than relating it to each $. 1 , \ 1 \ \leq \ l \leq n$

Case II can then be broken into the following subcases:

1. The specific entity type is contained in the intersection of the generic entity types.

2. The specific entity type is not contained in the intersection of the generic entity types, but is contained in their union.

5.1. Case II.A: Specific Entity Type Contained in Intersection of Generic Entity Types

Case II.A is characterized by the following initial state:

1. X is-an $4 , \forall \mathit { l } , \ l \leq \mathit { i } \leq \mathit { n }$ (initial lattice).

2. All of the. $\mathbf { i } , \mathbf { \bar { s } }$ intersect; that is, $\bigcap { } _ { t = 1 } ^ { n } \ldots { } _ { t _ { i } } \neq \emptyset$ (Case II assumption.)

3. X is contained in the intersection of the $\mathbf { i } , \mathbf { \dot { s } } .$

Then the $\mathbf { \nabla } _ { \cdot } \mathbf { i } _ { \mathbf { \nabla } _ { I } } \mathbf { \dot { s } }$ can be organized into k nested groups. Sınce all of the generic entity types overlap and the specific entity type, X, is contained in their intersection, X must also be contained in the intersection of the most deeply nested generic of each group:

$$
\left(\lambda \subset \bigcap_ {i = 1} ^ {n} A _ {i}\right)\rightarrow \left(\lambda \subset \bigcap_ {j = 1} ^ {k} A _ {j} ^ {i}\right).
$$

In other words. $( . \Upsilon \subset . 1 _ { 1 } ^ { \prime } )$ holds simultaneously $\forall \ j = 1 , 2 , \ldots , k$ . Then, after grouping and re-ordering the $\mathrm { . } \mathrm { i } _ { \mathrm { , } } \mathrm { s . }$ the original lattice can be redrawn as shown in Figure 8.

Unravelling Is-a Structures  
![](/api/attachments/F6JCJ6UN/fulltext/images/e6b5677e84afbd277424c3ceb1a0ed2b2e173895713c31a8c43bcc10a2ecbf70.jpg)  
FiGuRE 8. Abstract Solution to Case Il A Speeific Fntity Iype in Intersection of Generie

Note that we take a “strict constructionist" approach to interpreting -a relationships. That is. each one is assumed to be always true, and, therefore, w hen a group of them appear together, all of them are assumed to be always true.

## 5.2. Case II.A: Example

Suppose that in a particular university environment, a Graduate Fellow is a Ph.D Student who is required to be both a Teachng Assistant (T 1) and a Research . 1sststant (R.1). Assume that the following relationships appear in a database design:

1. Graduate Fellow is-a Student

2. Graduate Fellow is-an Employee

3. Graduate Fellow is-a Researcher

4. Graduate Fellow is-a RA

5. Graduate Fellow is-a TA

6. Graduate Fellow is-a Teacher

7. Graduate Fellow is-a Staf

8. Graduate Fellow is-a Ph.D. Student.

This is illustrated in Figure 9. Note that the generic entity tvpes. Student. Emplovee, Researcher, R. 1, T 1, Teacher, Staff and Ph.D Student, can all overlap. thus requiring a Case Il analysis.

Goldstein · Storey

![](/api/attachments/F6JCJ6UN/fulltext/images/0bed2af75bf6f17b069aa37197349088e066be8bce90279c4d8f91008e31b5d0.jpg)  
FiGURE 9. Case II.A: Graduate Fellow Example

The first step is to organize the generics into nested groups as in Case I. There are four such groups, each containing two of the original generic entity types:

1. Staff is-an Employee

2. RA is-an Researcher

3. TA is-a Teacher

4. Ph.D. Student is-a Student.

$A _ { 1 } ^ { \ 1 } \ = \ S t a f f , \ A _ { 1 } ^ { 2 } \ = \ R A , \ A _ { 1 } ^ { 3 } \ = \ T A , \ A _ { 1 } ^ { 4 } \ = \ P h . D .$ . Student are all intersecting and X = Graduate Fellow is contained in the intersection. The modified lattice appears as shown in Figure 10.

This example illustrates that an zs-a lattice does not necessarily indicate a design error. However, a necessary condition for it to be correct is that there must exist a higher-level, “more generic" entity type to which all of the specified generics are related. Note that this “super-generic" (which might be Person in the University example) need not be included in the database design ifit is not considered necessary; however, it must exist.

![](/api/attachments/F6JCJ6UN/fulltext/images/fcd9eb814dbe04b01776090e4514e2fb5d34ba42efbfe9ce17a81f15f15cdf3d.jpg)  
FiGURE 10. Case II.A Solution: Graduate Fellow Example.

## 5.3. Case II.A: Database Design Implications

1. Each explicit relationship X is-an $\boldsymbol { A } _ { \iota } ^ { \phantom { \dagger } }$ for $2 \leq i \leq n _ { \iota } , 1 \leq \iota \leq k$ , should be deleted as it can be inferred via the X $l . 5 \ – \ a n \ A _ { \mathrm { ~ l ~ } } ^ { \prime }$ relationship.

2. The specific entity type, X, is simultaneously a specific entity type of each A{ . It can, therefore, inherit properties from all of the $. 1 _ { 1 } ^ { \prime } \mathrm { { { \dot { s } } } }$ and, transitively, from all other $A _ { \iota } ^ { \prime } , 1 < i \leq n _ { \iota } , 1 \leq j \leq k$

In the example, Graduate Fellow is truly a specific entity type of the Staff, RA, TA, Ph.D. Student, Employee, Researcher, Teacher and Student generic entity types; thus, it can inherit properties from all of them.

3. The following semantic integrity constraint holds:

• The specific entity type, X, must have an explicit /s-a relationship to each $\boldsymbol { \mathcal { A } } _ { 1 } ^ { j }$ Graduate Fellow must have an 1s-a relationship to Staff, R4, T'1, and Ph D Student in order for the design to reflect properly the semantics of the application.

5.4. Case II.B: Specific Entity Type Contained in Union of Generic Entity Types

For Case II.B, the initial state is described by:

1. X is-an A, $\forall i , 1 \leq i \leq n$ (initial lattice).

2. All of the $A _ { t } ^ { \cdot } \mathbf { s }$ intersect; that is, $\bigcap _ { t = 1 } ^ { n } A _ { t } \neq \varnothing$ . (Case Il assumption.)

In Case II.B, however, the specific entity type, X, is contained in the union of the generic entity types, but not their intersection; that is:

$$
X \subset \bigcup_ {i = 1} ^ {n} A _ {i}, \quad X \not \subset \bigcap_ {i = 1} ^ {n} A _ {i}
$$

Thus, the first initial condition notwithstanding. $\textit { X i s - a n - 1 } _ { i }$ is not true in general. $\forall i , 1 \leq i \leq n$ . This is the common case of a designer relating a specific entity type to a number of generic types when the correct semantics are that each instance of the specific type is related to one (or more) of the generics. but not to all of them.

Even though X is not in the intersection of all the $\mathbf { 4 } _ { i } { \bar { \mathbf { s } } } .$ it may be in the intersection of some of them. Thus, the first step is to group and re-order the $\cdot \mathbf { i } _ { \cdot } \mathbf { \dot { s } }$ as described previously. If X is-an A  for some $\jmath , 1 \leq \jmath \leq k$ , then X is a subset of each generic entity type in the jth group; that is:

$$
(X \subset A _ {1} ^ {j}) \Rightarrow X \subset A _ {i} ^ {j} \quad \forall i, \quad 1 <   i \leq n _ {j}.
$$

Assume that $X$ is in the intersection of $m$ of the groups. The groups can then be renumbered for convenience such that these are numbered from 1 to m and the remaining groups are numbered m + 1 to k. Obviously. it is possible for some of the $A _ { \mathrm { ~ i ~ } } ^ { \prime } \Im \mathrm { f o r } \ j > m$ to overlap separately from the overlap among the first m groups. The case of multiple overlapping groups is handled by a straightforward extension of the proposed algorithm, but because the notation becomes excessively messy, the extension will not be illustrated. Assuming no overlaps among the last k – m groups, we have:

![](/api/attachments/F6JCJ6UN/fulltext/images/cf6ba205cf20fa9ee6eb433e8bec870aa41e68f3b706568641762dbd0af896b7.jpg)  
FiGURE 11. Abstraet Solution to Case 11 B

$$
X \subset \bigcap_ {j = 1} ^ {m} A _ {1} ^ {j},
$$

$$
X \subset \bigcup_ {j = m + 1} ^ {k} A _ {i} ^ {j},
$$

$$
X \not \subset A _ {1} ^ {\prime} \cap A _ {1} ^ {\prime} \quad \forall i \neq j, \quad m <   i, \quad j \leq k.
$$

Clearly, (X is-an A {) need not hold for all $j > / / l$ . Then it is necessary to relate $X$ to some higher level entity type, Y, that represents the union of these .1. If such an entity type does not exist, then either: (1) it has to be created by defining it to be the generalization of $\cdot 1 _ { \textrm { l } } ^ { \prime } , \forall \ j > \ m ; \mathrm { o r } \left( \ 2 \ \right)$ has to be related to an entity type still higher in level that contains the desired generalization.

Since X may be a specific entity type of any of these $. 1 _ { 1 } ^ { \prime } \mathrm { \hat { S } } .$ the only properties that can always be inherited are those that are common to all of them. In fact, as noted earlier, the property set of a union is the intersection of the property sets of its constituents, so Y will have precisely the properties that are common to these ${ \bf 4 } _ { 1 } ^ { j } { \bf ^ { \ell } S } .$ If there already exists another entity type Z such that $\diagup ^ { \prime } , \supset \ P _ { \ n , \bullet } ^ { \prime } , \forall \jmath > \ m$ , then X can be related directly to Z instead of creating the new entity type Y. The general solution is presented in Figure 11. Note that the left-hand side of the figure, representing the first m groups, reduces to a Case II.A situation.

Unravelling Is-a Structures  
![](/api/attachments/F6JCJ6UN/fulltext/images/a76563d2c97f1ffd0324a6ef943f16c464680bf89fa92570fde1d35809c5cc34.jpg)  
FiGURE 12. Case II B: Teaching Assistant I xample

## 5.5. Case II.B: Example

Consider the lattice shown in Figure 12 where the following relationships hold:

1. Teaching Assistant is-a Ph.D. Student

2. Teaching Assistant is-an Employee

3. Teaching Assistant is-a Teacher

4. Teaching Assistant is-a Course Taker

5. Teaching Assistant is-a Course Marker

6. Teaching Assistant is-a Student.

The generics can all intersect so a Case Il analysis is required

1. Irrange into nested groups The first step is to arrange the generics into four nested groups:

(a) Ph.D. Student is-a Student

(b) Teacher is-an Employee

(c) Course Taker

(d) Course Marker.

2. Delete incorrect relationships. There are no incorrect relationships.

3. Delete redundant relationshups. In this example, the following are redundant and can, therefore, be deleted:

(a) Teaching Assistant is-a Student.

(b) Teaching Assistant is-an Employee.

4. Identify groups such that X is in the intersecton –The .1{s are: (1) Ph D Student, (2) Teacher. (3) Course Taker, and (4) Course Marker Since Teachung . 1ssistant will always be both a Ph D Student and a Teacher, these form the 1/'s for which Teaching .Issistant is in the intersection.

5. Identify groups such that X ts in the unon (but not the tntersecuon) –It is assumed that a Teachng Asststant will always be a: (1) Course lahet or (2) Course Marker (and may, of course, be both)

![](/api/attachments/F6JCJ6UN/fulltext/images/d4f888a669c9d15a9f57c8495308d1f79f75f054d658e1ad4230e792dded4d3b.jpg)  
FiGURE 13. Case II.B Solution: Teaching Assistant Example

6. Identify higher-level generic for X in unton. It is necessary to identify an entity type which is the union of the smallest generic entity types, $\mathcal { A } _ { 1 } ^ { m + 1 } , \ldots , \mathcal { A } _ { 1 } ^ { k } . \mathcal { A } _ { 1 } ^ { m + 1 }$ corresponds to Course Taker and $A _ { \mathrm { ~ i ~ } } ^ { m + 2 } ~ ( = A _ { \mathrm { ~ l ~ } } ^ { k } )$ corresponds to Course Marker. A suitable candidate is Course Affiliate which is defined to be someone who is involved in a course in any capacity.

The solution to this problem is shown in the ts-a structure in Figure 13.

## 5.6. Case II.B: Database Design Implications

1. Each explicit relationship X is-an A' for $2 \leq i \leq n ,$ should be deleted as it can be inferred via the X is-an A{ relationship (as in Case II.A).

2. The specific entity type, X, can inherit properties from the higher-level entity type, Y, but not from the original generic entity types, $4 \ : _ { 1 } ^ { \prime } . \dot { \jmath } > n \eta$

For example, since Teachıng Assistant can be a Course Taker or a Course Marker only properties that are common to both of them can be inherited by Teaching Assistant.

3. Each occurrence of X will have a corresponding occurrence of at least one of the $A _ { \mathrm { ~ l ~ } } ^ { \prime } \mathbf { \hat { s } }$ for $j > m$

For example, a Teaching Assistant who is taking a course and marking a course will be represented by occurrences of both the C’ourse Taker and C’ourse Marker entity types.

## 5.7. Design Heuristics

Cases II.B deals with a structure in which one entity type is a specific entity type of the union of a number of other entity types. One possibility is that the problem has been improperly conceptualized and the is-a relationships are actually upside down. Suppose, for example, that the original design had included the relationships Course Affiliate is-a Course Taker and Course Affiliate is-a Course Marker. A given Course Affiliate need not be both a Taker and a Marker, so this is a Case II.B example where the specific would be contained in the union of the generics. However, as the preceding solution demonstrates, the problem is simply that the relationships are upside down. In general. the appearance of a Case II.B situation can signal the need to invert the relationships.

![](/api/attachments/F6JCJ6UN/fulltext/images/d0455607ff6f494c1f41b84c9b70e617c9e50cc91991de8856303d8ca5cbf5dc.jpg)  
FiGuRE 14. Case II B Example: Initial Lattice—-Role Confusion

Another possible explanation of Case Il.B is that a role is being modeled as an is-a relationship. For example, given Instructor is-a Faculty Member and Instructor is-a Graduate Student (clearly a Case II.B situation), the correct explanation is that instructing is a role which can be played by either a faculty member or a graduate student. The “role" construct, however, cannot be captured by ts-a relationships. This is shown in Figure 14 where the lattice implies that an Instru tor is a Faculty Member and a Graduate Student, simultaneously. This role cannot be captured by turning Figure 14 upside down because that solution, as illustrated in Figure 15, implies that every faculty member and every graduate student must be an instructor. Rather, the figure needs to be changed as shown in Figure 16 where the relationships are no longer is-a relationships. The cardinalities are added to indicate the minimum and maximum number of each entity type that can be related to each occurrence of the other entity type in the relationship (Tsichritzis and Lochovsky 1982). These are usually omitted for is-a relationships since the semantics make clear that they must be (0, 1) for the generic entity type and (1, 1) for the specific. In this case, Faculty Member (0, 1) can-be Instructor (0, 1) indicates that some Fac ulty Members will be Instructors and some Instructors will be Faculty Members. The fact that the cardinalities do not match those expected for an s-a relationship is one more indication that this is not the correct construct for this situation.

## 6. Case III—Mutually Exclusive Generic Entity Types

Case III deals with a situation where the 1,'s can be arranged into k groups such that each group $( . 4 _ { 1 } ^ { \prime } , \cdot \cdot \cdot _ { ^ { \prime } } ^ { \prime } )$ has the nesting property of Case I and the most specialized $A _ { \iota } { \bf \dot { s } }$ from each group $( . 4 _ { 1 } ^ { \prime } \mathrm { { ' } } \mathrm { { s } ) }$ are mutually exclusive.

![](/api/attachments/F6JCJ6UN/fulltext/images/fe2157ac8bdba669f16f7325bf1366a5cf366c280d568e707598c8dedda1eca7.jpg)  
FIGuRE 15 Case II.B F xample. Role Cannot be Correctlv Represented by Inverting

![](/api/attachments/F6JCJ6UN/fulltext/images/a611ad926838284b74b295bd7d833f406d0cfcf627cdf6d53fb6977d1f0aa5ce.jpg)  
FiGuRE 16 Case II.B Example. Represented by ca-he Relationships

In Case Ill, then, some of the generics would be subsets of other generics but if two generics do not have a subset-superset relationship. they do not overlap at all. In order to deal with Case III, first arrange the . 1, 's from the original lattice into k groups as described for Case Il and delete redundant relationships as described earlier. That is, delete all relationships described by:

$$
X \text {   is - an   } A _ {i} ^ {j}, \quad \forall i, j, \quad i > 1, \quad 1 \leq j \leq k.
$$

As in Case II, only the specific entity type's relationship with the most specialized entity type of each group, A, needs to be considered. Since the .1 are mutually exclusive, it is impossible for the specific entity type. X, to simultaneously be a specialization of each of the $\mathbf { 1 } \mathbf { \Gamma } _ { 1 } ^ { \prime } \mathbf { \bar { s } } .$ . There must, therefore, be an error in the design. The following distinct causes can be identified:

1. Only one of the is-a relationships is correct.

2. There are really different kınds of the specific entity type, each having some unique properties.

3. There is only one kind of the specific entity type, but its occurrences can be related to different generic entity types.

## 6.1. Case II.A: Incorrect Is-A Relationships

The simplest case is where all but one of the nonredundant -a relationships, X ¿s-an A, are incorrect. The solution in this case is simply to delete all of the incorrect relationships.

In the portion of the University Example shown in Figure 17, it appears that laboratory instructors are (simultaneously) full-time graduate students, visiting faculty members, full-time faculty members, and teaching fellows, which. in order to illustrate Case Ill, are taken to be mutually exclusive. Suppose that, in fact, laboratory instructors are only full-time graduate students. Then the solution is as shown in Figure 18 where all but one of the $l . 5 { - } d$ relationships have been removed.

## 6.2. Case HII.B: Different Kinds of Specific Entity Types

Another possibility, of course, is that the entity type X has been (incorrectly) used to model several distinct things; that is, there may actually be k different kinds of the specific entity type X. say, $X ^ { \prime } \cdot \ s \ = \ 1 , 2 \ldots \ldots , k \colon$

Unravelling Is-a Structures  
![](/api/attachments/F6JCJ6UN/fulltext/images/b0db96b08e7e5ac3a40e91183e0a93e70f07950df5e09f29e9e26ef8fc33d7bd.jpg)  
FiGuRE 17. Portion of University Example

$$
X = \bigcup_ {j = 1} ^ {k} X ^ {\prime}
$$

and each X/ is related (by an ts-a relationship) to one of the $. 1 _ { \mathrm { ~ l ~ } } ^ { \mathrm { ~ / ~ } } \mathrm { S } .$

To illustrate this case, suppose that in the university example, there were only two entity types to consider—Full\_Time (Graduate Student) and Faculty Member as shown in Figure 19. There could actually be two kinds of the entity type Instructor, namely, Laboratory Instructors, who are full-time graduate students and Course Instructors, who are faculty members. Then the situation should be represented as illustrated in Figure 20. In this case, Laboratory Instructor would have properties that are distinct from Course Instructor and vice versa

6.2.1. .1lternate Solutton to Case III.B. As above, suppose that there are really k different kinds of X, call them $\smash { \xi ^ { 1 } , \ldots , \xi ^ { k } }$ . There could be properties that are common to all X'. Let these be retained in the entit tvpe λ. Then the relationships X' ts-a X, 1 ≤ j ≤ k, must be added. X now acts as a higher-level generic entity type that includes all of the $X ^ { \prime } \zeta$

In the university example, the properties that are common to both types of instructors should be represented by an entity type, Instructor. of which Laboratory Instructor and Course Instructor are specific entity types. Instructor, in turn, becomes a specific entity type of Person Γhis solution is illustrated in Figure 21.

6.2.2. Compartson of Case III.B Solutions Figure 20 and Figure 21 differ in the following sense. In Figure 20, the properties that are common to all instructors appear in both entity types, Laboratory Instructor and Course Instructot–Laboratory

![](/api/attachments/F6JCJ6UN/fulltext/images/a46f51c03805b317a57db633b2f26262ad2e3f9ee2b820acdeeb07a69c607ee6.jpg)  
FiGuRE 18. Case III.A Solution: Laboratory Instructor 1s-a Full-Tumne Graduate Student

Instructor, for example, contains all the properties of both Full\_T'ime (Graduate Student) and Instructor. In Figure 21, the common Instructor properties have been abstracted out. Therefore, in Figure 21, Laboratory Instructor contains only those properties that are unique to laboratory instructors. Similarly, Course Instructor contains only those properties that are unique to course instructors. This solution would generally be preferred because it facilitates the processing of queries that refer to properties common to the various types of instructor.

6.2.3. Case III.B: Database Design Implication. For the solution illustrated in Figure 21, the following database design implication holds.

• Each X can inherit properties from A (and, indirectly, from all the other generic types in the /th group $\{ A _ { \iota } ^ { \prime } , 2 \leq \iota \leq n _ { \iota } \} \}$ and from the new X.

For example, Laboratory Instructor can inherit properties from both Full\_Time (Graduate Student) and Instructor, Course Instructor can inherit properties from Faculty Member and Instructor.

## 6.3. Case III.C: One Kind of Specific But from Different Domains

The third possibility is that there is only one kind of the specific entity type, but each occurrence of it is related to one, and only one, of the possible generic entity types:

$$
(x \in X) \Rightarrow A _ {1} ^ {\prime} \quad \text {   for   only   one   } j, \quad 1 \leq j \leq k.
$$

In the university example of Figure 17, there is only one kind of Instructor(X), but each occurrence of Instructor (X) is either a Full\_Time\_Graduate\_Student

![](/api/attachments/F6JCJ6UN/fulltext/images/a294e1f7672fbf3041cf694c3858838f6f0c6853f4a924dd0fb6fe717febc724.jpg)  
FiGuRE 19. Instructor in Relationshıp to Full-lume Graduate Student and Facult

Visiting, Tenured, Untenured, or Teaching Fellow. The basic Case IIl assumption that the generic entity types, A/, are mutually exclusive means that a single occurrence of X cannot correspond to more than one of the generics. In order to model this situation using is-a structures, lower-level entity types, $\lambda ^ { \prime } \langle s .$ . are created that represent an entity tvpe that is both an X and an A. The diagram is modified as shown in Figure 22.

The Instructor entity type will contain all of the Instructor properties. Since it is assumed that there is only one kind of instructor, there are no unique properties associated with the lowest level entity types (Full-T'ime Instructor,

![](/api/attachments/F6JCJ6UN/fulltext/images/d7dbcbc2ffd9f79dbb562a027c7822e68e85718aeb990ade031f936937c2629f.jpg)  
FiGURE 20. Solution III.B Two Different Kinds of Instrut tory

![](/api/attachments/F6JCJ6UN/fulltext/images/c9006444d4322ea5b466ca398891943947fd44eda57cec2245cb2ab3e48d811c.jpg)  
FiGuRE 21. Alternative Solution III B Common Insttcto Properties

Visiting-Instructor, etc.); instead, they serve only to connect each occurrence of Instructor to an occurrence of one of the other generic entity types. Note the distinction between this case and Case III.B where the lowest level entity types (Laboratory Instructor and Course Instructor) represent different kinds of things and, therefore, would have unique properties.

6.3.1. Case III.C: Database Design Impltcatons The implications of this solution are:

• An integrity constraint is required to ensure that each occurrence of X is related to exactly one of the A{'s.

![](/api/attachments/F6JCJ6UN/fulltext/images/8ca98492d91986ca4bbd6ec1845d9d5f43089b5a3487c6a8e24777100cba3d96.jpg)  
FiGURE 22. Solution to Case III C

![](/api/attachments/F6JCJ6UN/fulltext/images/3c21da5b37463b0e95c81518991754d8cca34f4ce1032daebeee33b6556c9518.jpg)  
FiGURE 23 Musıe Teacher F xample

In the university example, this constraint ensures that each occurrence of Instructor is related to exactly one of Full\_Time, V’isting, Tenured. U'ntenured or Teaching Fellow'

• If there appear to be any properties of the X/'s other than those inherited from the A {'s (or their ancestors) or X. then this probably signals a design error.

For example, Tenured-Instructor should not have properties other than those inherited from Tenured, Instructor, and Person

## 7. Case IV—Combinations of Other Cases

Case IV deals with combinations of Cases I, II and III. This reflects situations where some of the generic entity types overlap and some do not. Also, this case deals with the possibility that relevant generic entity types are missing from the original lattice.

## 7.1. General Approach to Case IV

To resolve a Case IV lattice, the following steps need to be performed

1. Apply the solution to Case I; that is. organize the 1,'s into groups of nested generic entity types. Delete redundant or incorrect relationships. Allow for the possibility that a needed generic entity type(s) is missing.

2. Examine the lattice for instances of Case Il and Case III structures. Resolve each as previously described.

## 7.2. Case IV Example

Because the semantics of Case IV are particularly complex, it is impossible to illustrate them realistically within the context ofthe University application. Figure 23 shows the problem that will be addressed in this section where Atstc Teacher appears as a specialization of Person. Performer, Professional Ausician. .Amateur Mustcian, and Music Lover.

Case I Analvsts. The generic entity types are arranged into nested groups. Note that Person is the generic of Performer, Professional Ausıcian, .Amateur Mustctan, and Music Lover. Therefore, the groups become as shown ın Figure 24 (assuming no missing generic entity types).

Case I/III Analvsis Note first that Professional Musician and . 1mateur Musician are mutually exclusive. This is an instance of Case III. Following the procedure outlined in §6.2. this case is resolved by adding two additional entity types,

![](/api/attachments/F6JCJ6UN/fulltext/images/5a04a26c7e35c25e8b03fa48c8ccc7eabd28e1d7d6814171a1a35f99a5a7eda0.jpg)  
FiGURE 24. Musıc Teacher Example: Case I Analysıs.

Professional Musician—Music Teacher and Amateur Musician—Music Teacher. The Music T'eacher entity type is modified to contain just those properties common to all types of music teachers, amateur or professional. This results in the structure shown in Figure 25.

Musıc Teacher is still a specific entity type of Performer and Musıc Lover. Since these two can certainly overlap, this is an instance of Case II. If it is assumed that each music teacher is both a performer and a music lover, this is an example of Case II.A. Then no change is required to the solution of Figure 25. If, however, this assumption cannot be made, Case II.B analysis is applied, resulting in the solution shown in Figure 26.

## 8. Limitations

The main limitation of the preceding analysis is that, although is-a relationships capture important application semantics, they are not sufficient to depict all useful meaning. This research has identified a number of situations where additional mechanisms are required:

1. When the specific entity type is contained in a union of generics, the specific must be is-a related to the union rather than to the individual generic entity types (Case II.B).

2. When occurrences of the specific entity type are related to one of several mutually exclusive generic entity types, new, lower-level entity types should be created to distinguish the sets of occurrences of the specific that are associated with each generic (Case III).

![](/api/attachments/F6JCJ6UN/fulltext/images/29d7a9f4f8e82e379e9a8e3fc1a02a10817471f3eb8617896d0fe5b5b6e70ddb.jpg)  
FiGuRE 25 Musie Teacher Example: Case IIl Analysıs

3. Is-a relationships cannot be used to reflect accurately the semantics of an application when, for example, all but one of the is-a relationships hold; that is. when the specific entity type, X, is all but one of three generic entity types $X _ { \mathfrak { i } } , X _ { \mathfrak { i } }$ , or X3 Restrictions of this type must be expressed using integrity constraints.

4. Is-a structures are not appropriate for representing the concept of a role; that is, they cannot be used to indicate that different specific entity types can adopt the role suggested by the generic entity type.

5. The need to add a specific entity type to a database design can be identified in various ways. Urban and Delcambre (1986) recognize the following types of specializations:

(a) attribute-defined—for example, specified on the “sex" property of the Person entity.

(b) user-specified—for example, Good-Book is a subtype of Book and its content must be explicitly specified by someone (such as a book critic) (Peckham and Mar yanski 1988).

(c) set operator-defined—a specific entity type is defined by performing set operations, such as intersection, union, or difference, over other entity types: for example Male-Student is the intersection of Male and Student

(d) existence-defined—a specific entity type is existence-defined if its instances appear as property values of another entity type. This corresponds to the notion of a weak entity in the Entity-Relationship model ( Peckham and Maryanski 1988). For example, Book-Review may be defined as the specialization of Revtew for which each occurrence has a corresponding occurrence of Book

![](/api/attachments/F6JCJ6UN/fulltext/images/09f97fd026e7c334281b4f8ed508a1eafc1f6949f20db064f4a0c54cf8d826a3.jpg)  
FiGuRE 26 Musıe Teacher Example Case II.B Analysıs

## 9. Summary & Conclusion

Various types of ¿s-a structures that can appear in a database design have been classified and analyzed. Is-a relationships are usually thought of as representing strictly hierarchical structures. In this research, it has been shown that nonhierarchical is-a structures can somctimes be perfectly correct. In other cases, however, such structures signal the existence of incorrect or inefficient designs. Nonhierarchical is-a structures have been examined and the modifications appropriate to cach case described. The database design implications of cach such modification have also been specified.

Three types of is-a lattices have been analvzed. The first was an -a structure that had either redundant or incorrect relationships. The second case had a specific entity type that was related to overlapping generic entity types and showed how, depending upon the semantics of an application, the design should be modified—cither for clarity or to reflect more of the semantics of the application. The third case concerned situations where the most deeply nested generic entity types are mutually exclusive. In this situation, a design error exists which can be classified into one of three possible categories. Each of these was subsequently analyzed. The final case considered combinations of previous cases.

The results of the analysis should be applicable to both manual approaches and automated tools for database design in order to highlight design errors, more clearly capture some of the semantics of a database application, and identify integrity constraints.\*

Acknowledgements. This research was supported by the Information Systems Research Bureau, Faculty of Commerce and Business Administration, University of British Columbia and the William E. Simon Graduate School of Business Administration, University of Rochester. The authors wish to express their thanks to Yair Wand, University of British Columbia, for useful discussions on this research and to Debabrata Dey, University of Rochester, for his assistance in formalizing the notation and preparing the figures for this paper.

## References

Arisawa, H and T Miura, “On the Properties of Fxtended Inclusion Dependencies," I.EE I'tansactions on Sottware Engmneermg, SE-12, 11 (November 1986), 1098-1101

Atzenı, P and D. S. Parker, “Formal Properties of Net-Based Knowledge Representation Schemes," Proceedings of Conference on Data Engineerung, 1986, 700–706.

Banerjee, J., H.-T. Chou, J. F Garza W Kım, D Weolk, N. Ballou and H -J Kim. "Data Model Issues for Object-Oriented Applications," 1 M I'ransadttons on Office Informatton Srstems, 5, 1 (January 1987) 3-26

Batinı. C , S Ceri and S B Navathe, Conceptual Database Desıgn 1n Entity-Relattonshp 1ppoach. The Benjamin/Cummings Publishing Company. Ine , Redwood Cits Calfornia, 1992

, M. Lenzerinı and S B Navathe, “A Comparative Analy sis of Methodologies for Database Schema Integration," 1CA1 Computung Survers, 18, 2 (December 1986) 323–364

Bouzeghoub, M., G Gardarın and 1 Metais, "Database Design Tools An 1 pert System Approach," Proceedings ot the 1 Uth Internattonal Conference on Very La ge Databases, Stockholm, Sweden, Morgan Kaufmann Pub , Los Altos, Calfornia, 1985, 82–95

Brachman. R J., "What IS-A I and Isn't: An Analvsıs of Γaxonomue I inks in Semante Networks," Computet (October 1983), 30-36

Briand, H , H. Habrias, J.-F. Hue and Y. Sımon, "F xpert System for Translatıng an E-R Diagram into Databases." Proceedtngs of 4th L-R Conterence, 1985, 199–206

Chen & Associates, Ine., L-R Mode//er. Los Angeles, CA, 1987

Choobineh, J., "Form Driven Conceptual Data Modeling," Ph D. Dissertation. Dept Management Information Systems, University of Arizona, 1985

, B. R Konsynskı, M V Mannıno and J F Nunamaker. • An Expert System Based on Forms,' IEEE fransactons on Software Engueering, 14, 2 (February 1988). 242–253.

Date, C. J , 1n Inttoductton to Database Svstems I of 1, (4th Ed ), Addison-Wesley, Reading, MA, 1986

Demo, B and M lillı, “Expert System Functtonalities for Database Desıgn Tools," ın D Sriram and R. Adey (Eds ), Applcatons of . tifuaal Inettigence in Engueerng Problems Proc cedings of the 1 st Internattonal Conference Southampton University Aprıl 1986, Springer-Verlag, Berlin and New York. 1986, 1073–1082

Elmasrı, R. and S Navathe, Fundaentals of Database Srstens, Benjamin/Cummngs Publishing Co Inc , Redwood City, Californıa 1989

Goldstein, R. C., Database Technology and Management, Wiley. New York, 1985

Greenspan, S J., J. Mylopoulos and A Borgıda, "Capturing More Woıld Knowledge in the Requirements Speeiheaton," Proreedings 6th Internattonal Conference on Softn e I'ngueenng. Tokyo, 1982, 225– 234.

Hammer, M and D McLeod, “Database Descripton with SDM A Semantie Database Model," 1CV Ttunsactions on Database Systems, 6, 3 (1981)

Korth, H F and A. Silberschatz, Database Systen Conepts (2nd 1 d) MeGraw-Hll, Inc., New York. 1991

Lloyd-Williams, M., “I xpert Systems for Database Design," Working Paper, Department of Computer Studies, Polvtechnic of Wales, February 1991

Maryanskı, F and S Hong, “A Tool for Generating Semantie Database Applications IEE E (O MPS 1C Ptoceedtngs. Chicago. 11, October 1985, 368–375

Meersman, R , “Preface," Data and Knowledge (DS-2), Meersman, R and Sernadas, A C ( Eds.) North-Holland, Amsterdam, 1988, vı-xu

, “Knowledge and Data A Survey in the Margin of the IFIP DS-2 Conference  In Spaccapietra, S (Ed), Entttv-Relattonshıp Approach. Flsevier Seience Publshers B V (North-Holland), New York and Amsterdam. 1987. 25–34

Motschnig-Pitrik, R. and J. Mylopoulos, “Classs and Instances," Internattonal Journal of Intelligent and Cooperative Svstems, 1, 1 (1992).

Peckham, J. and F. Maryanskı, "Semantıc Data Models," 4CM Computing Surveys, 20, 3 (September 1988), 153-189

Ram, S . “Automated Tools for Database Design: State of the Art," Working Paper, Dept. of MIS, College of Business and Publıc Adminıstration, University of Arizona, 1989

Reiter, R., “"Towards a Logical Reconstruction of Relational Database Theory," in Brodie, M. L., Mylopoulos, J., and Schmıdt, J W. (Eds.), On C'onceptual Modelling. Sprınger-Verlag, Berlın and New York, 1984, 191–233

Schneider, M. and C Trepied, “A Graphical Query Language Based on an Extended E-R Model," Proceedings of 8th International Conference on Entity-Relationshıp Approach, Toronto, Canada, October 1989, 248-262.

Shaw, M., "The Impact of Modelling and Abstraction Concerns on Modern Programming Languages," 1n Brodie, M., Mylopoulos, J and Schmıdt. J. W. (Eds.), On Conceptual M1odelling. Springer-Verlag, Berlın and New York, 1984, 19–47

Smith, J. M. and D. C. P. Smith, “Database Abstractions: Aggregation and Generalization," ACM Transactons on Database Systems, 2, 2 (June 1977), 105–133

Stefik, M and D. G. Bobrow, "Object-Oriented Programming: Themes and Variations," The 4I Magazine, 6, 4 (Winter 1986), 40–62

Storey, V. C , “Relational Database Design Based on the E-R Model," Data and Knowledge Engineering. North-Holland, Amsterdam, 7. 1 (1991), 47–83

, V’tew C'reatton An Expert S1 stem for Database Desıgn Ph.D. Dissertation, Faculty of Commerce and Business Admınistration, University of British Columbia, Vancouver, Canada, ICIT Press, Washington, DC, 1988

and R. C. Goldsteın, “Knowledge-Based Approaches to Database Design," Workıng Paper. University of Rochester, 1991

and - , “Design and Development of an Expert Database Design System," Internatonal Journal of Expert Systems Research and 1ppltcattons, 3, 1 (1990), 31–63

- and - , “A Methodology for Creating User Views in Database Design," AC'M Transactons on Database Systems, 13, 3 (September 1988), 305–338.

Tanımoto, S. L , The Elements of 1ruftctal Intelligence An Introduction Using LISP, Computer Science Press, 1987

Tauzovich, B.. “An Expert System Approach to Database Design," Proceedings Ist Internattonal Confer ence on Datubase and Expert Systems Applicattons (DEX 1). 1990, 322–326.

. “An Expert System for Conceptual Data Modelling." Cognos Inc . Ottawa, Canada, Proceedings of 8th Internattonal Conference on Entity-Relatonshıp 1pproach, Toronto, Canada, October 1989, 329-344

Teorey, T J , D. Yang and J P. Fry, "A Logical Design Methodology for Relational Databases Using the Extended Entity-Relationshıp Model," ,1C'M C'omputing Survers. 18, 2 (June 1986).

Touretzky, D S , Ihe Mathenattcs of Inheritance Systems, Morgan Kaufmann Publıshers, Inc., Los Altos, California, 1986,

Tsichrıtzis, F. and F. Lochovsky. Data Model, Prentice-Hall, Englewood Cliffs, NJ, 1982.

Urban, S. D and L M. L. Delçambre, "An Analysıs of the Structural, Dynamic. and Temporal Aspects of Semantic Data Models," Proceedings International Conference on Data Engineering, IEEE Computer Society. 1986, 382–389.

Wagner, C., “View Integration in Database Design," Ph.D. Dissertation, Faculty of Commerce and Business Administration, Unıversitv of Britısh Columbia, Vancouver, Canada, 1989.

Wand, Y., “A Proposal for a Formal Model of Objects." in Object-Oriented Concepts, Databases, and Applcation, Lochovsky, F. and Kim, W (Eds ). ACM Press, Addison-Wesley, Reading, MA, 1989, 537-559
