---
otero_id: 17423
otero_key: "DWCJATFM"
title: "Approximate dependencies in database systems"
authors: "Aditya N. Saharia; Terence M. Barron"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0049-j"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Approximate dependencies in database systems

Aditya N. Saharia \*

University of Illinois at Chicago, Chicago, IL 60607, USA

Terence M. Barron

University of Toledo, Toledo, OH 43606, USA

Functional dependencies are the most commonly used approach for capturing real-word integrity constraints which are to be reflected in a database. There are, however, many useful kinds of constraints, especially approximate ones, that cannot be represented correctly by functional dependencies and therefore are enforced via programs which update the database, if they are enforced at all. This tends to make such constraints invisible since they are not an explicit part of the database, increasing maintenance problems and the likelihood of inconsistencies. We propose a new approach, cluster dependencies, as a way to enforce approximate dependencies. By treating equality as a fuzzy concept and defining appropriate similarity measures, it is possible to represent a broad range of approximate constraints directly in the database by storing and accessing cluster definitions. We discuss different interpretations of cluster dependencies and describe the additional data structures needed to enforce them. We also contrast them with an existing approach, fuzzy functional dependencies, which are much more limited in the kind of approximate constraints they can represent.

Keywords: Databases; Functional dependencies; Approximate dependencies; Fuzzy functional dependencies; Integrity constraints; Clustering

## 1. Introduction

A database system may be viewed as a computer-based representation of a real world system, where the real world objects (entities, events, and the associations among them) are represented by the information objects stored in the database. To avoid discrepancies between the real world objects and their representation in the database, at design time we not only identify the objects to be represented, but we also identify constraints the data items have to satisfy. Whenever possible, such constraints are incorporated within the database. Once a design incorporating these conditions has been developed, the database management system takes over the responsibility of enforcing them. In relational database systems, where real world objects are represented as tuples in relations, constraints are specified as func-

![](/api/attachments/DWCJATFM/fulltext/images/d8fec2005cb1e43ae9ac2888fedd5606331980ceaf9528a34be5a5c014c8bddf.jpg)

systems, Information Systems Research, Journal of Management Information Systems and IEEE Transactions on Knowledge and Data Engineering.  
![](/api/attachments/DWCJATFM/fulltext/images/da78abc1a7a36c8a903d244d3d3fe9691efbf11e5d06edd733c512d97b6e659a.jpg)  
Systems, and Journal others.

Terence M. Barron is Associate Professor of Information Systems at the University of Toledo. He received his Ph.D. in 1987 from the Graduate School of Business Administration, University of Washington (Seattle). His research interests include economics of information and organizations, economics of information system management, and information system analysis and design. His research has appeared in Information Systems Research, Decision Support of Organizational Computing, among tional dependencies. At design time, the semantics of the data items are used to discover functional dependencies; the functional dependencies are then used to arrive at normalized relations, so that guaranteeing uniqueness of tuples in each relation is sufficient to satisfy the constraints implied by the functional dependencies.

In the real world, the objects represented in the database will satisfy constraints more general than those which can be represented with conventional design tools such as functional dependencies or E-R modelling. For example, a manager may want to enforce the constraint “salaries of employees with similar job and similar experience are approximately equal.” Such a constraint cannot be conveniently represented as a functional dependency. The problem arises because in relational theory the only objects recognized are sets and predicates over these sets which take on binary values. Therefore the only constraints incorporated in the design are ones which can be naturally expressed in terms of these objects. A concept like “approximate equality” cannot be naturally represented in terms of predicates which take on binary values. The usual approach in database design has been to ignore such relationships and hope that they are taken care of by other data validation and/or audit techniques.

Two mechanisms for incorporating approximate relationships have been proposed previously: the fuzzy functional dependency framework of Raju and Majumdar [8] and the probabilistic dependency framework of Haux and Eckert [3]. In the fuzzy functional dependency framework, approximate equality is treated as a predicate which can take on non-binary values, and an approximate relationship is treated as a fuzzy implication. This imposes restrictions on the attributes of a tuple being inserted by comparing it with the existing tuples in the relation. Fuzzy functional dependencies provide a natural extension of the decomposition rules obtained in relational database theory. However, they impose conditions on data items which are even more stringent than the conditions implied by functional dependencies. Further, enforcing a fuzzy functional dependency may require that at each insertion, the tuple being inserted be compared with all the existing tuples in a relation.

In the probabilistic dependency framework, a tuple being inserted in a relation is validated by estimating the probability of that tuple occurring. If the calculated probability is less than some acceptable level, the entry is flagged for further validation. In the probabilistic dependency framework, we do not have to compare a new tuple to all the existing tuples; rather we have to calculate the probability of its occurrence. To the extent that such probability distributions can be efficiently maintained, the probabilistic dependency framework provides a more flexible approach to handle approximate relationships. The major drawback of this approach is that the distributions may not be known beforehand, requiring them to be determined from the realized data. This in itself may be a non-trivial problem, especially if the relation is being updated frequently.

We suggest that approximate relationships be represented as cluster dependencies. In the cluster dependency framework, the tuples in a relation are grouped into clusters (see $[1]$ ). An approximate relationship is then enforced on a cluster-by-cluster basis. By suitably defining the cluster membership and the meaning of the approximate dependency, the conditions a tuple has to satisfy can be determined only in terms of nearby clusters, rather than the entire relation as might be the case for fuzzy functional dependencies. As updates to the relation take place, definitions for only those clusters which are affected by the update will have to be revised. This is a considerable advantage over the probabilistic dependency framework where the probability distribution is defined over the entire relation and may have to be revised with each update.

In addition to providing a mechanism for enforcing the integrity constraint implied by an approximate relationship, the cluster dependency mechanism may also be used for approximate reasoning, especially for queries requiring statistical summaries (of the dependent attributes), since these summaries would be maintained for each cluster anyway. Also, the cluster dependency framework makes the constraints more visible since the cluster definitions and the allowed values of the dependent attribute for each cluster are stored as part of the database, rather than being stored invisibly in programs.

This paper is organized as follows. In section 2 we describe using functional dependencies to represent exact relationships and their limitations in representing approximate relationships. In section 3 we define approximate equality by allowing the predicate EQUAL to take non-binary values. We also define a similarity measure which describes how close two objects are to each other. The same similarity measure is then used to define fuzzy functional dependencies and cluster dependencies. In section 4 we describe approximate relationships as fuzzy functional dependencies and show that these dependencies are more restrictive than functional dependencies. In this section we also discuss the design implications and the additional steps which need to be incorporated in the database management system to enforce fuzzy functional dependencies. In section 5 we describe approximate relationships as cluster dependencies. We also discuss some possible mechanisms for defining the allowed values of the attributes of a tuple using neighboring clusters. Finally in section 6, we give a summary and conclusions.

## 2. Exact relationships as functional dependencies

In relational database systems, the real world constraints are modelled via functional dependencies (FDs for short). For example, the constraint that the value of the attribute EMPLOYEE-NUMBER is unique for each employee is enforced through functional dependencies such as:

EMPLOYEE-NUMBER determines
EMPLOYEE-NAME,

EMPLOYEE-NUMBER determines
EMPLOYEE-DEPARTMENT,
EMPLOYEE-NUMBER determines
EMPLOYEE-MANAGER.

Thus, in a relation referring to employees, two tuples which match on EMPLOYEE-NUMBER must also match on other attributes (EMPLOYEE-NAME, EMPLOYEE-DEPARTMENT, etc.) which are functionally dependent on (or determined by) the attribute EMPLOYEE-NUMBER. More formally, an FD is a statement $X \Rightarrow A$ where $X$ and $A$ are sets of attributes. A relation $r$ defined on a scheme $R$ is said to satisfy the $\mathrm{FD}X \Rightarrow A$ , where $X \cup A \subseteq R$ if for any two tuples $t$ and $t'$ in $r$ , $t[X] = t'[X]$ implies $t[A] = t'[A]$ . Thus in the relation $r$ , each value of attribute X is associated with only one value of the attribute A. In drawing a parallel with the discussion in the following sections, we associate the symbol “=” with a binary relation $EQUAL_{X}$ defined on the scheme $(X, X)$ . A tuple $\langle x_{1}, x_{2} \rangle$ belongs to $EQUAL_{X}$ if and only if $x_{1}$ and $x_{2}$ are identical. In other words, $EQUAL_{X}(.,.)$ stands for a predicate which takes on the value 1 if both the arguments are identical, and 0 otherwise.

The FDs are enforced by including only “normalized” relations in the design. A given normal form restricts the type of FDs a relation can satisfy. For example, a relation is said to be in 3rd normal form if no non-key attribute is functionally dependent on sub-key attributes or other non-key attributes. To normalize a relation r defined on a scheme R and satisfying a set of FDs G, a set of decomposed relations $r_{1}, r_{2} \ldots r_{k}$ is constructed with the relation $r_{j}$ defined on the scheme $R_{j} \subseteq R$ such that $R_{1} \cup R_{2} \ldots \cup R_{k} = R$ . Each decomposed relation $r_{j}$ satisfies a smaller subset of FDs $G_{j} \subseteq G$ . For example if r satisfies an FD $g: X \Rightarrow A$ where A is a non-key attribute and X consists of either sub-key attributes or non-key attributes, then r is replaced by the relations $r_{1} = \pi_{R_{1}}(r)$ and $r_{2} = \pi_{R_{2}}(r)$ , where $R_{1} = R - A$ , $R_{2} = (X, A)$ , and $\pi$ is the projection operator. The FD g is not included in the set of FDs to be satisfied by the relation $r_{1}$ , whereas $r_{2}$ does satisfy the FD g. A decomposition is said to be lossless if a natural join $r_{1} | \times | r_{2} | \times | \ldots | \times | r_{k} = r$ for every r. Once we have arrived at the normalized relations $r_{1}, r_{2}, \ldots, r_{k}$ we do not include the original relation r in the database since for a lossless decomposition r can be reconstructed from the decomposed relations. If a relation $r_{j}$ is such that the only non-trivial FDs included in $G_{j}$ are the ones in which a non-key attribute is dependent on the key attributes $K_{j}$ , the real life constraints implied by the FDs in $G_{j}$ are satisfied by ensuring that for each key value there is at most one tuple in the relation. This can be efficiently done via an index or a hashing scheme: before inserting a new tuple, the value of the key is used to retrieve and examine the contents of the physical storage location where the new tuple is to be stored. See [6] for a review of relational database design theory.

In the real world, data items stored in a database system will satisfy constraints more general than those which can be represented by FDs.

For example, a manager may want to enforce the constraint “salaries of employees with similar job and similar experience are approximately equal”, which cannot be conveniently represented as a functional dependency. The problem of representing approximate relationships in conventional relational databases arises because the data items are drawn from domains which satisfy the rules of set theory. A relation represents a crisp association between the elements of the sets on which it is defined. In other words, a relation r, defined on the scheme $R = A_{1}, A_{2}, \ldots, A_{n}$ , represents an n-place predicate $r(a_{1}, a_{2}, \ldots, a_{n})$ such that each tuple included in the relation makes the predicate r TRUE. Since the only objects which are recognized in the relational theory are sets, relations, and predicates which take on binary values, the real world constraints allowed are the ones which can be naturally expressed in terms of these objects. On the other hand, approximate relationships cannot be naturally represented by predicates which take on binary values. We start by defining approximate equality as a fuzzy concept and then treat approximate relationships as fuzzy implications.

## 3. Equality as a fuzzy relation

Following Zadeh [11] and others (see [4] and references therein), we allow for approximate equality by treating it as a fuzzy concept. In other words, for a domain X, we define a fuzzy equivalence relation $EQUAL_{X}$ on the scheme $(X, X)$ such that a tuple $(x_{1}, x_{2})$ belongs to $EQUAL_{X}$ with a membership function $\mu_{\mathrm{EQ}_{X}}(x_{1}, x_{2})$ where $0 \leq \mu_{EQ_{X}} \leq 1$ . Also, to make $EQUAL_{X}$ correspond to the standard definition of equality, $\mu_{EQ_{X}}$ is chosen so that $\mu_{\mathrm{EQ}_{X}}(x, x) = 1$ . When the members of the set X represent categorical values, the membership function is defined as

$$
\mu_ {\mathrm{EQ} _ {X}} \left(x _ {1}, x _ {2}\right) = \left\{ \begin{array}{l l} 0 & \text { if } x _ {1} \neq x _ {2} \\ 1 & \text { if } x _ {1} = x _ {2} \end{array} . \right.\tag{1a}
$$

When the members of the set X represent numeric values, the membership function can be defined in terms of the distance between two points. The membership function is chosen so that it is monotonically decreasing in distance. Thus, if the distance between the pair $(x_{1}, x_{2})$ is larger then the distance between the pair $(x_{1}^{\prime}, x_{2}^{\prime})$ then $\mu_{\mathrm{EQ}_{x}}(x_{1}, x_{2}) \leq \mu_{\mathrm{EQ}_{x}}(x_{1}^{\prime}, x_{2}^{\prime})$ . Raju and Majumdar [8] suggest, using the following functional form, to represent the membership function:

$$
\mu_ {\mathrm{EQ} _ {X}} \left(x _ {1}, x _ {2}\right) = \frac {1}{1 + b _ {x} \left| x _ {1} - x _ {2} \right|},\tag{1b}
$$

where the parameter $b_{x}(b_{x}>0)$ is a scaling factor used to make the membership values for different domains comparable. Again to make EQUAL $_{X}$ corresponding to the standard definition of equality, we impose a further restriction on the membership function for the relation EQUAL $_{X}$ :

$$
\mu_ {\mathrm{EQ} _ {X}} \left(x _ {1}, x _ {2}\right) <   1 \quad \text { for } \quad x _ {1} \neq x _ {2}.
$$

Note that this condition is satisfied for the definition (1b) as long as $b_{x}$ is positive definite.

We can now make concrete the notion of an approximate match between two objects. For this we use a similarity measure which determines how close two objects are, based on comparisons of one or more attributes. Assuming that objects under consideration are represented as tuples in a relation r, defined on the scheme R, the similarity between the two tuples t and $t'$ based on a single attribute $X \in R$ is defined as

$$
S _ {X} (t, t ^ {\prime}) = \mu_ {\mathrm{EQ} _ {X}} (t [ X ], t ^ {\prime} [ X ]).
$$

If X consists of more than one attribute, i.e. $X = \{A_{1}, A_{2}, \ldots, A_{k}\}$ , we adopt the following standard fuzzy set convention:

$$
S _ {X} (t, t ^ {\prime}) = \min _ {A _ {i} \in X} \left[ S _ {A _ {i}} (t, t ^ {\prime}) \right],
$$

i.e., the similarity between two tuples based on X is the minimum of the similarity between them based on any of the individual attributes $A_{i}$ in X. Raju and Majumdar [8] use the term “membership in resemblance relation” rather than the term “similarity” for $S_{X}$ . We prefer the latter since it is commonly used in the clustering literature (see, for example, Aldenderfer and Blashfield [1]) to describe how close two objects are in the multidimensional space of attribute values. Other measures of similarity have also been used in the clustering literature. For example, in the context of document retrieval, where each document is represented as a point in the multidimensional space of frequencies for each key words, Salton and McGill [9] suggest using a “cosine” measure to define similarity between two points.

We use the above definition of similarity for describing both fuzzy functional dependencies and cluster dependencies.

## Example 1

Table 1 shows a relation called EMPLOYEES defined on the scheme (E\_ID, JOB, EXP, SAL), where dom(E-ID) is a set of strings, up to 4 characters long, giving the unique identifier for an employee; dom(JOB) = {Engineer, Manager, Secretary}; dom(EXP) is the set of integers in the range 0 to 30, giving experience of an employee in years; and dom(SAL) is the set of real numbers in the range 20000 to 100000, giving the annual salary of an employee.

Since the attribute E\_ID is categorical, the relation EQUAL $_{E-ID}$ is a crisp relation in the sense that $\mu_{\text{EQ}_E\_ID}(e_1, e_2) = 1$ if $e_1 = e_2$ and is 0 otherwise. In other words, a tuple $\langle e_1, e_2 \rangle$ is included in EQUAL $_{E-ID}$ if and only if $e_1$ and $e_2$ match. Similarly, EQUAL $_{JOB}$ is a crisp relation. On the other hand, the equivalence relations EQUAL $_{EXP}$ and EQUAL $_{SAL}$ are fuzzy relations, the membership functions for them being given by

$$
\mu_ {\mathrm{EQ} _ {\mathrm{EXP}}} \left(x _ {1}, x _ {2}\right) = \frac {1}{1 + b _ {\mathrm{EXP}} \left| x _ {1} - x _ {2} \right|}
$$

where $b_{\mathrm{EXP}} = 1$

$$
\begin{array}{r l} \mu_ {\mathrm{EQ} _ {\mathrm{SAL}}} (s _ {1}, s _ {1}) & = \frac {1}{1 + b _ {\mathrm{SAL}} | s _ {1} - s _ {2} |} \\ \text { where } b _ {\mathrm{SAL}} & = 1 / 2 0 0 0 \end{array}
$$

Thus $\mu_{EQ}$ for the attributes EXP and SAL is unity only when the two values match, and is decreasing monotonically as the distance between the two values increases. The similarities between each pair of tuples (which are identified by the attribute E-ID) based on the set of attributes {JOB, EXP} and the attribute SAL are given by table 2.

For example, the similarity between the pair of tuples E2 and E4 based on {JOB, EXP} is 1/2, whereas the similarity based on SAL is 2/3. □

Table 1
EMPLOYEES

<table><tr><td>E-ID</td><td>JOB</td><td>EXP</td><td>SAL</td></tr><tr><td>E1</td><td>Engineer</td><td>10</td><td>50000</td></tr><tr><td>E2</td><td>Manager</td><td>15</td><td>40000</td></tr><tr><td>E4</td><td>Manager</td><td>14</td><td>41000</td></tr><tr><td>E5</td><td>Engineer</td><td>8</td><td>52000</td></tr></table>

Table 2

<table><tr><td></td><td>E1</td><td>E2</td><td>E4</td><td>E5</td></tr><tr><td>E1</td><td>-</td><td>0, 1/6</td><td>0, 2/11</td><td>1/3, 1/2</td></tr><tr><td>E2</td><td>0, 1/6</td><td>-</td><td>1/2, 2/3</td><td>0, 1/7</td></tr><tr><td>E4</td><td>0, 2/11</td><td>1/2, 2/3</td><td>-</td><td>0, 2/13</td></tr><tr><td>E5</td><td>1/3, 1/2</td><td>0, 1/7</td><td>0, 2/13</td><td>-</td></tr></table>

## 4. Approximate relationships as fuzzy functional dependencies

Following the fuzzy extension of first order logic [11], the relationship embodied by the statement “if tuples t and $t'$ approximately match on attribute X, then they must also approximately match on attribute A,” is interpreted as a fuzzy implication and is taken to mean that

$$
S _ {X} (t, t ^ {\prime}) \leq S _ {A} (t, t ^ {\prime}).\tag{2}
$$

Raju and Majumdar [8] interpret such a restriction as a fuzzy functional dependency (FFD). A relation $r$ , defined on a scheme $R$ , is said to satisfy the FFD $X \approx \Rightarrow A$ , where $X \cup A \subseteq R$ , if for every pair of tuples $t$ and $t'$ in $r$ , condition (2) is satisfied. This interpretation of approximate dependencies has the desirable property that an FFD always implies a corresponding FD. Thus the rules of relational theory which hold in the presence of FDs also hold in the presence of FFDs. However, a consequence of this property is that FFDs are even more restrictive than FDs and therefore allow us to incorporate only limited types of dependencies. We illustrate these issues through examples and discussion below.

## Example 2

The relation EMPLOYEES in example 1 satisfies the following FDs:

$$
\mathrm {E\_ID} \Rightarrow \mathrm{JOB},\tag{3a}
$$

$$
\mathrm {E\_ID} \Rightarrow \mathrm{EXP},\tag{3b}
$$

$$
\mathrm {E\_ID} \Rightarrow \mathrm{SAL}.\tag{3c}
$$

In addition it satisfies the following FFD:

$$
\{\text { JOB }, \text { EXP } \} \approx \Rightarrow \text { SAL }.\tag{4}
$$

This can be easily verified by comparing the similarity between each pair of tuples based on the set of attributes {JOB, EXP} with the similarity based on the attribute SAL. For example, the similarity between the 2nd and the 3rd tuples based on {JOB, EXP} is 1/2, whereas the similarity based on SAL is 2/3. Similarly, if we attempt to insert tuple $\langle E6, Engineer, 6, 42000\rangle$ in the table EMPLOYEES, it will be rejected since the similarity between the new tuple and the last tuple based on {JOB, EXP} is 1/3, whereas the similarity based on SAL is 1/6. ☐

With the restriction that $\mu_{\mathrm{EQ}} < 1$ whenever its arguments do not match, an FFD $X \approx \Rightarrow A$ implies that whenever two tuples $t$ and $t'$ match exactly on independent attributes $X$ , (i.e. $\mu_{\mathrm{EQ}_X}(t[X], t'[X]) = 1$ ) we must have, because of condition (2), $\mu_{\mathrm{EQ}_A}(t[A], t'[A]) = 1$ and hence $t$ and $t'$ must match exactly on the dependent attribute $A$ . Thus the FFD $X \approx \Rightarrow A$ incorporates the FD $X \Rightarrow A$ . In the relation EMPLOYEES of example 1, the FFD {JOB, EXP} $\approx \Rightarrow$ SAL incorporates the FD {JOB, EXP} $\Rightarrow$ SAL. Enforcing this FFD will thus require that all the employees with the same job and the same experience must have exactly the same salary!

Since the FFD $X \approx \Rightarrow A$ implies the FD $X \Rightarrow A$ , we can extend the decomposition rules developed in the normalization theory to the case of FFDs. Thus if an FFD $X \approx \Rightarrow A$ holds in a relation r defined on a scheme R where X is not the minimal key of r, then we can decompose r into relations $r_{1}$ , defined on the scheme $R_{1} = R - A$ , and $r_{2}$ , defined on the scheme $R_{2} = (X, A)$ . Note that the attributes X will constitute the key of the relation $r_{2}$ . The FFD $X \approx \Rightarrow A$ (and hence the FD $X \Rightarrow A$ ) is to be enforced only against the relation $r_{2}$ . Also as in the case of FDs, we do not include r in the database since it can be obtained by a join of $r_{1}$ and $r_{2}$ .

## Example 3

This example illustrates how restrictive FFDs are. Since the FFD (4) implies the corresponding FD, the relation EMPLOYEES in example 1 can be decomposed into relations EJX and JXS which are the projections of EMPLOYEES over (E-ID, JOB, EXP) and (JOB, EXP, SAL). Corresponding to the instance of EMPLOYEES given in example 1, the relations EJX and JXS are given by tables 3 and 4.

The relation EJX satisfies the FDs (3a) and (3b).

Table 3
Relation EJX

<table><tr><td>E-ID</td><td>JOB</td><td>EXP</td></tr><tr><td>E1</td><td>Engineer</td><td>10</td></tr><tr><td>E2</td><td>Manager</td><td>15</td></tr><tr><td>E4</td><td>Manager</td><td>14</td></tr><tr><td>E5</td><td>Engineer</td><td>8</td></tr></table>

The relation JXS satisfies the FFD (4). Note that the FD (3c) can be derived from the FDs (3a) and (3b) and the FFD (4) and will be satisfied by the join of EJX and JXS. A transaction attempting the insertion of the tuple $\langle E6, Engineer, 6, 42000\rangle$ in EMPLOYEES will be executed as two separate insertions: an insertion of tuple $\langle E6, Engineer, 6\rangle$ in EJX and an insertion of tuple $\langle Engineer, 6, 42000\rangle$ in JXS. The entire transaction will be rejected since the insertion in JXS will cause the FFD (JOB EXP) $_{≈}$ $\Rightarrow$ SAL to be violated. ☐

Once we have arrived at a design where the only non-trivial FFDs to be enforced in a relation are of the type $X \approx A$ , where the attributes X constitute the key of the relation and A is a non-key attribute, ensuring the uniqueness of key values (i.e. ensuring that for each key value there is at most one tuple) guarantees that the FD $X \Rightarrow A$ is satisfied. However, the uniqueness of key values does not guarantee that the relation satisfies the FFD $X \approx A$ since in this case we have to guarantee that condition (2) is satisfied between every pair of tuples. Thus if a tuple is inserted in such a relation we have to not only guarantee that there is no other tuple with the same key value but also that condition (2) is satisfied between the new tuple and all the existing tuples, so that the entire relation may have to be scanned whenever an insertion occurs. Fortunately, if the membership functions $\mu_{\mathrm{EQ}_{X}}(x_{1}, x_{2})$ and $\mu_{\mathrm{EQ}_{A}}(a_{1}, a_{2})$ are monotonically decreasing functions of the scaled scalar distances $b_{x}|x_{1}-x_{2}|$ and $b_{A}|a_{1}-a_{2}|$ , respectively, (as is the case when the membership functions are given by equation (1b)), then condition (2) requires that $b_{x}|x_{1}-x_{2}|\geq b_{A}|a_{1}-a_{2}|$ . In such a case it is sufficient to compare a tuple to be inserted with the innermost tuples enclosing the new tuple. This is shown pictorially in Figure 1 where X is a single attribute. Note that efficiently determining the innermost tuples enclosing the new tuples may require maintaining additional data structures (e.g. an index); maintaining and searching through these data structures may be just as hard as a complete scan. See also the discussion below on design implications of FFDs.

Table 4
Relation JXS

<table><tr><td>JOB</td><td>EXP</td><td>SAL</td></tr><tr><td>Engineer</td><td>10</td><td>50000</td></tr><tr><td>Manager</td><td>15</td><td>40000</td></tr><tr><td>Manager</td><td>14</td><td>41000</td></tr><tr><td>Engineer</td><td>8</td><td>52000</td></tr></table>

The regions defining the allowed values of the attributes X and A are bounded by pairs of lines with slope $\pm b_{x}/b_{A}$ passing through each of the points corresponding to the existing tuples. When a new tuple t arrives, the value of t[X] is used to determine $t_{1}$ the tuple (if any) just to the left of t (i.e. $t_{1}[X] < t[X]$ and there is no other tuple $t'$ such that $t_{1}[X] < t'[X] < t[X]$ ) and $t_{r}$ , the tuple (if any) just to the right of t (i.e. $t_{r}[X] > t[X]$ and there is no other tuple $t'$ such that $t_{r}[X] > t'[X] > t[X]$ ). If the point $(t[X], t[A])$ lies in the parallelogram obtained by the intersection of the right region of allowed values for $t_{1}$ and the left region of allowed values for the tuple $t_{r}$ , it will be accepted; otherwise it will be rejected. If the tuple is accepted for insertion, the parallelogram defined by tuples $t_{t}$ and $t_{r}$ will be pinched at point $(t[X], t[A])$ so as to give two new regions of allowed values; one defined by the tuples $t_{1}$ .

![](/api/attachments/DWCJATFM/fulltext/images/96240921e2feabb33e7f13d6f11d718f11e69d1f5c2ab2ca61f34bbf33807378.jpg)  
Fig. 1. Regions of allowed values for the pair $(x, a)$ based on FFD $X \approx A$ . Dots denote tuples already in the relation, crosses denote tuples to be inserted. The slopes of lines defining the regions of allowed values are $\pm b_X / b_A$ . When a tuple is inserted, it has to be compared with at most two tuples, one to its right and the other to its left. Based on these comparisons, the tuple $t$ will be accepted but tuple $t'$ will be rejected.

![](/api/attachments/DWCJATFM/fulltext/images/b49bab7a465d0d62e60c7eb8a039193f7c94d71caf5db5ac08b7e7e3c034c6e9.jpg)  
Fig. 2. Regions of allowed values for the pair $(x, a)$ based on FD $X \Rightarrow A$ . Dots denote tuples already in the relation.

and t and other by the tuples t and $t_{r}$ . We also note in the limit when $b_{x} = \infty$ , EQUAL $_{X}$ reduces to the standard equality since then $\mu_{\mathrm{EQ}_{X}}(x_{1}, x_{2}) = 1$ if $x_{1} = x_{2}$ , so the FFD $X \approx A$ is replaced by the FD $X \Rightarrow A$ . This is shown pictorially in Figure 2. In this case the slopes of the lines defining the valid regions become infinite and, therefore, the region of allowed values for the pair $(x, a)$ is the entire region $dom(X) \times dom(A)$ , except for the cuts given by the values of the attribute X for the existing tuples. Thus in a new tuple, the attribute A can take on any legal value as long as the attribute X for this tuple does not match that of any existing tuple.

## Example 4

The relation JXS in example 3 satisfies the FFD (4). Let $t = \langle \text{Engineer}, 9, 51000 \rangle$ denote a new tuple to be inserted in JXS. Since the attribute JOB takes on categorical values, the standard definition of equality holds for this attribute. We have to compare the tuple with only those existing tuples for which JOB = Engineer. The tuples with attribute EXP just below and just above the value of 9 (the value of the attribute EXP in the new tuple) are given by $t_t = \langle \text{Engineer}, 8, 52000 \rangle$ and $t_r = \langle \text{Engineer}, 10, 50000 \rangle$ . The slopes of the lines defining the allowed regions are given by $\pm b$ , where $b = b_{\text{EXP}} / b_{\text{SAL}} = \$2000$ per year. The tuple $t$ will be accepted since it lies in the intersection of the right allowed region for $t_1$ and the left allowed region for $t_r$ . Another tuple $t' = \langle \text{Engineer}, 9, 49000 \rangle$ has the same two tuples $t_1$ and $t_r$ surrounding it. However, this tuple does not lie in the intersection of the right allowed region for $t_1$ and the left allowed region for $t_r$ and, therefore, will be rejected.

The design implications of FFDs are minimal in the sense that we have to enforce an FFD only in the relation where the corresponding FD is satisfied. We, therefore, normalize relations using the explicit FDs as well as the FDs implied by the FFDs. In addition, we need to define data structures to maintain definitions of the membership functions $\mu_{EQ}$ for the equivalence relations for the set of attributes participating in FFDs. This could be done using a functional form as in equation (2) or using a table to maintain the relations EQUAL explicitly. (Obviously we can do this only for an attribute which is drawn from a finite domain.) We also need to incorporate procedures in the DBMS to compare a tuple which is being inserted with the existing tuples using these similarity measures.

## 5. Approximate relationships as cluster dependencies

To allow for more general relationships, we suggest use of a clustering scheme to group the tuples in a relation into clusters such that members of a cluster have similar values for the independent attribute mentioned in the relationship. The approximate relationship is then taken to mean that all members of a cluster have approximately similar values for the dependent attribute. Such a mechanism allows us to restrict the value of the dependent attribute in terms of those of the neighboring tuples without imposing the restriction that for a given value of the independent attribute there be just one allowed value of the dependent attribute. A relation r defined on a scheme R is said to satisfy a cluster dependency (or CD for short) $X \Rightarrow_{C} A$ where $X \cup A \subseteq R$ if for a tuple t in r which belongs to a cluster $\beta$ (based on attribute X), $t[A]$ is similar to typical values for attribute A in the cluster $\beta$ . In case the tuple belongs to more than one cluster, the above condition must be satisfied for all such clusters.

In enforcing a cluster dependency, we would define allowed values for the dependent attributes so that when an entering tuple is examined, the values allowed by the neighboring clusters are given more importance than the values allowed by distant clusters. To facilitate this, we treat “belongs to the cluster $\beta$ ” as a fuzzy relation $BELONGS_{\beta}$ on $dom(X)$ , even when the clustering method leads to well-separated clusters. A tuple t then belongs to cluster $\beta$ with a membership $\mu_{\mathrm{BELONGS}_{\beta}}(t)$ where $0 \leq \mu_{\mathrm{BELONGS}_{\beta}} \leq 1$ , and the allowed values are chosen so that the clusters for which $\mu_{BELONGS_{\beta}}$ is close to 1 provide relatively tight bounds, whereas the clusters for which $\mu_{BELONGS_{\beta}}$ is close to 0 provide relatively liberal bounds. Note that “belongs to a cluster” is to be distinguished from “contained in a cluster”; the former is used to indicate how close the entering tuple is to a cluster whereas the latter is used to denote the membership in the set of tuples used in defining the cluster. We assume that overlapping clusters are not allowed, so that each tuple is contained in exactly one cluster, whereas it belongs to all clusters with different levels of membership function. We also use the cluster name $\beta$ to denote the set of tuples used to define $\beta$ and use standard set theory notation $t \in \beta$ to denote that t is contained in $\beta$ .

Following the discussion in section 3, we use a similarity measure between $t[X]$ and a tuple $\bar{x}_{\beta} \in dom(X)$ , called the centroid for cluster $\beta$ , to define the membership function $\mu_{\text{BELONGS}_\beta}$ :

$$
\begin{array}{r l} \mu_ {\mathrm{BELONGS} _ {\beta}} (t) & = S _ {X} \big (t [ X ], \bar {x} _ {\beta} \big) \\ & = \min _ {A _ {i} \in X} \Big [ S _ {A _ {i}} \big (t [ X ], \bar {x} _ {\beta} \big) \Big ] \\ & = \min _ {A _ {i} \in X} \Big [ \mu_ {\mathrm{EQ} A _ {i}} \big (t [ A _ {i} ], \bar {x} _ {\beta} [ A _ {i} ] \big) \Big ]. \end{array}
$$

Different measures of similarity than the one given above can be used. If an attribute $A_{i} \in X$ is categorical a clustering method would group only those tuples in a cluster which take on the same value for $A_{i}$ ; hence we set $\bar{x}_{\beta}[A_{i}]$ to this common value. If an attribute $A_{i} \in X$ takes numerical values, we may set $\bar{x}_{\beta}[A_{i}]$ to $t'[A_{i}]$ for some $t' \in \beta$ . However, this requires that we either maintain the set $\overline{X}_{\beta}$ of the realized values of the attributes X for the cluster $\beta$ , or maintain the list of tuples contained in $\beta$ . We suggest using the arithmetic mean of values of attributes X for all the tuples in the cluster since these are used in the clustering method which we suggest (hierarchical agglomeration with average linking), and therefore would be maintained anyway for each cluster:

$$
\bar {x} _ {\beta} [ A _ {i} ] = \frac {1}{| \beta |} \sum_ {t ^ {\prime} \in \beta} t ^ {\prime} [ A _ {i} ],
$$

where $|\beta|$ is the cardinality of the set $\beta$ . Note that if $dom(A_{i})$ is a subset of the integers, then we have to allow $\bar{x}_{\beta}[A_{i}]$ to be drawn from the set of rational numbers.

In a similar vein, we treat the term “similar to the typical values of A” to mean that if $a = t[A]$ and $\bar{a}_{\beta}$ is a typical value of the attribute A for the cluster $\beta$ , then the tuple $\langle a, \bar{a}_{\beta} \rangle$ belongs to the fuzzy relation EQUAL $_{A}$ with a membership function $\mu_{\mathrm{EQ}_{A}}(a, \bar{a}_{\beta})$ which is larger than some pre-specified value $\alpha$ where $0 \leq \alpha \leq 1$ . The typical value $\bar{a}_{\beta}$ may be set to $t'[A]$ for some $t' \in \beta$ . This would require that we either maintain the set $A_{\beta}$ of the realized values of the attributes A for the cluster $\beta$ , or maintain the list of tuples contained in $\beta$ . Again we suggest using the arithmetic mean of values of the attribute A for all the tuples in the cluster:

$$
\bar {a} _ {\beta} = \frac {1}{| \beta |} \sum_ {t ^ {\prime} \in \beta} t ^ {\prime} [ A ].
$$

Thus given the centroid $\bar{t}_{\beta}$ of the tuples contained in $\beta$ , when a tuple t is inserted, $t[X]$ is compared with $\bar{t}_{\beta}[X]=\bar{x}_{\beta}$ to determine the degree with which t belongs to the cluster $\beta$ , and $t[A]$ is compared with $\bar{t}_{\beta}[A]=\bar{a}_{\beta}$ to determine if $t[A]$ is similar to the typical values of the attribute A for the cluster $\beta$ which are given by $S_{A}(t,\bar{t}_{\beta})=\mu_{\mathrm{EQ}_{A}}^{\beta}(t[A],\bar{a}_{\beta})\geq\alpha$ . We choose the same functional form for $\mu_{EQ_{A}}$ as in section 3, but allow the scaling parameter to be given by the degree with which the incoming tuple belongs to the cluster $\beta$ :

$$
\begin{array}{l} \mu_ {\mathrm{EQ} _ {A}} ^ {\beta} (t [ A ], \bar {a} _ {\beta}) \\ = \frac {1}{1 + b _ {A} ^ {\beta} | t [ A ] - \bar {a} _ {\beta} |} \\ = \frac {1}{1 + b _ {A} (S _ {X} (t [ X ] , \bar {x} _ {\beta})) ^ {p} | t [ A ] - \bar {a} _ {\beta} |}. \end{array}\tag{5}
$$

The term $(S_{X}(t[X],\bar{x}_{\beta}))^{p}$ in equation (5) acts as a weight, so that by choosing p the designer can determine the relative importance of “nearby” and “distant” clusters. Small values of p give distant clusters considerable influence, while large values of p heavily discount distant clusters compared to nearby ones. Figure 3 gives a schematic representation of the regions of allowed values of the dependent attribute for different values of the independent attribute for a cluster dependency when p=2. Based on comparisons with the centroids, the tuple t will be accepted but tuple $t'$ will be rejected. In a hierarchical clustering method (for example the agglomerative method described below) where a cluster at a lower level is subsumed by a cluster at the next higher level, we may allow $\alpha$ and $b_{A}$ to be level-dependent. This may allow us to identify a tuple which is unacceptable at a high level in the hierarchy; we go to the next lower level only if the value of the dependent attribute is found to be acceptable at the previous level.

![](/api/attachments/DWCJATFM/fulltext/images/74f20137645a0246e1545a665afb6a38fbe7b1442c0057431ded9c6a932a5603.jpg)  
Fig. 3. Regions of allowed values for the pair $(x, a)$ based on $\mathrm{CD}X \Rightarrow_{C} A$ for $p = 2$ in eq. (5). Dots denote tuples already in the relation, crosses denote tuples to be inserted, circles with crosses denote the cluster centroids. The attributes of a centroid are determined by taking the arithmetic mean of the attributes for all tuples contained in the cluster. The membership function for the relation EQUAL $_{A}$ is chosen so that only comparisons with nearby clusters are meaningful. Based on these comparisons, the tuple $t$ will be accepted but tuple $t'$ will be rejected.

In using CDs to enforce approximate dependencies, we have to choose a clustering method to arrive at an initial set of clusters. In addition, we have to define a mechanism to identify the clusters with which the incoming tuple is to be compared, identify the cluster which will contain it (if the insertion is allowed), and define a mechanism to revise cluster definitions as the updates to the relation take place. We address these issues next.

As pointed out by Salton and McGill [9], the two characteristics generally considered important for any classification method are that the method be stable, and that the method should be well defined. Stability requires that small perturbations in the data (either changes in the number of objects or changes in the attributes) cause only minor changes in the set of clusters. The well defined condition requires that a given set of tuples should produce a single classification. In addition, for the classification scheme to work well, the minimum and maximum number of clusters, their sizes, and the overlap between them should be controllable. Thus the number of clusters should be greater than one but much smaller than the number of tuples. Similarly, even when we allow the clusters to overlap, a tuple should only be contained in a very small number of clusters. Finally the cluster generation algorithm has to allow for efficient search algorithms. Unfortunately, not all clustering methods perform equally well along all dimensions. (See Aldenderfer and Blashfield [1], Raghavan and Ip [7], and Salton and McGill [9] for discussion of evaluation of clustering methods.) Here we describe a hierarchical agglomerative method using average linkage which provides generally good performance on these dimensions. In this method all the objects are initially treated as individual clusters. At each successive step, the clusters that are closest to each other, as determined by centroid–centroid similarity, are merged together. The attributes of the centroid for a cluster are given by the arithmetic mean of the attributes for tuples contained in the cluster. We have preference for the average linkage method over other methods such as the single linkage method or the complete linkage method since it tends to produce natural groupings of objects [1]. The similarity between two objects (tuples or clusters) is obtained by following the approach suggested in section 3: take a minimum of the membership functions for the equivalence relation for each participating attribute.

## Example 5

Let the relation EMPLOYEES in example 1 be extended to include another attribute, EDU, where dom(EDU) is the set of integers in the range 0 to 20 and gives number of years of college education completed by an employee.

Table 5
EMPLOYEES (extended)

<table><tr><td>E-ID</td><td>JOB</td><td>EXP</td><td>EDU</td><td>SAL</td></tr><tr><td>E1</td><td>Engineer</td><td>10</td><td>4</td><td>50000</td></tr><tr><td>E2</td><td>Manager</td><td>15</td><td>6</td><td>40000</td></tr><tr><td>E4</td><td>Manager</td><td>14</td><td>4</td><td>41000</td></tr><tr><td>E5</td><td>Engineer</td><td>8</td><td>10</td><td>52000</td></tr><tr><td>E6</td><td>Engineer</td><td>6</td><td>4</td><td>40000</td></tr><tr><td>E7</td><td>Engineer</td><td>15</td><td>2</td><td>45000</td></tr><tr><td>E8</td><td>Manager</td><td>14</td><td>6</td><td>47000</td></tr><tr><td>E9</td><td>Engineer</td><td>2</td><td>4</td><td>30000</td></tr><tr><td>E10</td><td>Engineer</td><td>5</td><td>4</td><td>35000</td></tr><tr><td>E11</td><td>Manager</td><td>14</td><td>4</td><td>36000</td></tr><tr><td>E12</td><td>Engineer</td><td>2</td><td>4</td><td>32000</td></tr></table>

The equivalence relation $EQUAL_{EDU}$ for the attribute EDU is a fuzzy relation with the membership function given by

$$
\begin{array}{r l} & \mu_ {\mathrm{EQ} _ {\mathrm{EDU}}} (d _ {1}, d _ {2}) = \frac {1}{1 + b _ {\mathrm{EDU}} | d _ {1} - d _ {2} |}, \\ & \text { where } b _ {\mathrm{EDU}} = 2. \end{array}
$$

The relation EMPLOYEES, in addition to satisfying the FDs given by (3a)-(3c), also satisfies the FD:

$$
\mathrm{E-ID} \Rightarrow \mathrm{EDU}.\tag{3d}
$$

and the FFD{JOB, EXP} ≈ ⇒ SAL is replaced by the CD

$$
\{\text { JOB }, \text { EXP }, \text { EDU } \} \Rightarrow_ {\mathrm{C}} \text { SAL },\tag{4'}
$$

which corresponds to the approximate relationship that employees with the same job, similar experience, and similar level of education earn approximately the same salary. Based on the equivalence relations defined above and in example 1, the similarity between each pair of tuples is given by the matrix in table 6 (which we have organized in a block diagonal form to emphasize that tuples for different values of a categorical variable are not at all similar to each other).

Table 6

<table><tr><td></td><td>E1</td><td>E5</td><td>E6</td><td>E7</td><td>E9</td><td>E10</td><td>E12</td><td>E2</td><td>E4</td><td>E8</td><td>E11</td></tr><tr><td>E1</td><td>-</td><td>1/13</td><td>1/5</td><td>1/6</td><td>1/9</td><td>1/6</td><td>1/9</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E5</td><td>1/13</td><td>-</td><td>1/13</td><td>1/17</td><td>1/13</td><td>1/13</td><td>1/13</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E6</td><td>1/5</td><td>1/13</td><td>-</td><td>1/10</td><td>1/5</td><td>1/2</td><td>1/5</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E7</td><td>1/6</td><td>1/17</td><td>1/10</td><td>-</td><td>1/14</td><td>1/11</td><td>1/14</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E9</td><td>1/9</td><td>1/13</td><td>1/5</td><td>1/14</td><td>-</td><td>1/4</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E10</td><td>1/6</td><td>1/13</td><td>1/2</td><td>1/11</td><td>1/4</td><td>-</td><td>1/4</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E12</td><td>1/9</td><td>1/13</td><td>1/5</td><td>1/14</td><td>1</td><td>1/4</td><td>-</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>1/5</td><td>1/2</td><td>1/5</td></tr><tr><td>E4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1/5</td><td>-</td><td>1/5</td><td>1</td></tr><tr><td>E8</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1/2</td><td>1/5</td><td>-</td><td>1/5</td></tr><tr><td>E11</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1/5</td><td>1</td><td>1/5</td><td>-</td></tr></table>

![](/api/attachments/DWCJATFM/fulltext/images/8e2d28cdd5b8dc0a79981a74843ff2b7f674d380f03c31dcd3a269013f283522.jpg)  
Fig. 4. The agglomeration tree (Dendrogram) for the tuples given in the relation EMPLOYEES in example 5. The scale on the left hand side gives the relative ordering of the thresholds of similarity for which a fusion of two or more clusters or tuples takes place. The similarity between two clusters is defined by the similarity between the centroids. The attributes of a centroid are determined by taking the arithmetic mean of the attributes for all tuples contained in the cluster.

The clusters obtained for different levels of thresholds of similarity are given by the Dendrogram (agglomeration tree) in Figure 4. For example, at a threshold of 0.5, the clusters are: $\{E1\}$ , $\{E7\}$ , $\{E5\}$ , $\{E6, E10\}$ , $\{E9, E12\}$ , $\{E2, E8\}$ , and $\{E4, E11\}$ . The next threshold is at $2/9$ when the clusters $\{E6, E10\}$ , $\{E9, E12\}$ will be merged. The centroid of the merged cluster will be $\mathrm{JOB} = \text{Engineer}$ , $\mathrm{EXP} = 15/4$ and $\mathrm{EDU} = 4$ . The rows and columns for the original clusters are deleted from the similarity matrix and a new row and a new column are added for the merged cluster which give the similarity of the merged cluster with other clusters. The next threshold will be at $1/5$ when the clusters $\{E2, E8\}$ and $\{E4, E11\}$ are merged together, and so on. The clusters obtained for thresholds of $1/2$ and $1/6$ are given in Figure 5. Although for this example the complete Dendogram is given in Figure 4, we stop at the threshold of $2/9$ to avoid grouping objects which are very dissimilar. The table CLUSTERS below gives, for each cluster, values of the independent and dependent attributes for the centroid, and COUNT, which represents the number of tuples contained in the cluster. We need COUNT to recalculate the centroid after an insertion or deletion affecting the cluster takes place. Note that for each value of the independent attributes there will be only one cluster. Therefore, we do not have to keep the attribute C-ID explicitly, we do it here to make the reference to individual clusters easier. As discussed earlier, the attributes EXP and EDU in table 7 (CLUSTERS) are drawn from the set of rational numbers even though in the relation EMPLOYEES these were drawn from the set of integers. A tuple $\langle E3, Engineer, 8, 5, 57,000\rangle$ which is a candidate for insertion in the relation EMPLOYEES belongs to C1 with membership of 1/3, to C2 with membership of 0, to C3 with membership of 0, to C4 with membership of 1/11, to C5 with membership of 4/21, and to C6 with a membership of 1/8. Using (5) (with p = 2), the value of SAL for this tuple is similar to the value of the SAL for C1 with membership (in the relation EQUAL $_{SAL}$ ) of 18/25 = 0.72. Thus if we use $\alpha = 3/4$ to define the acceptable values of the attribute SAL, the tuple will be rejected because it is not similar to the typical values of SAL for the cluster C1 (although comparisons with other clusters would allow this tuple since (5) for these clusters would provide more liberal limits on SAL). ☐

![](/api/attachments/DWCJATFM/fulltext/images/182e00481d00d607dcf1310ec604ad896aa4038b61b0729b5342370a1b2374d2.jpg)  
Fig. 5. Clusters obtained using different levels of the similarity threshold for the table 5 (EMPLOYEES) in example 5. E denotes a tuple with JOB = Engineer and M denotes a tuple with JOB = Manager. We use centroid-centroid similarity to merge the two clusters at each step.

Table 7
CLUSTERS

<table><tr><td>C-ID</td><td>JOB</td><td>EXP</td><td>EDU</td><td>SAL</td><td>COUNT</td></tr><tr><td>C1</td><td>Engineer</td><td>10</td><td>4</td><td>50,000</td><td>1</td></tr><tr><td>C2</td><td>Manager</td><td>29/2</td><td>6</td><td>43,500</td><td>2</td></tr><tr><td>C3</td><td>Manager</td><td>14</td><td>4</td><td>38,000</td><td>2</td></tr><tr><td>C4</td><td>Engineer</td><td>8</td><td>10</td><td>52,000</td><td>1</td></tr><tr><td>C5</td><td>Engineer</td><td>15/4</td><td>4</td><td>34,250</td><td>4</td></tr><tr><td>C6</td><td>Engineer</td><td>15</td><td>2</td><td>45,000</td><td>1</td></tr></table>

To facilitate the search for close by clusters, an index tree can be built. Each node in the index tree would maintain, either explicitly or implicitly (as is done in a B-tree), the centroids of the clusters at the next lower level. The tree can be searched in a top-down fashion. If we use equation (5) to determine the allowed values, the branches which have clusters with low values of $\mu_{BELONGS}$ will not be searched further. For example, if table 7 (CLUSTERS) in example 5 had such an index, the comparisons (of the tuple to be inserted for which JOB = ENGINEER) with the branches for clusters with JOB = MANAGER could be ruled out at the top level. Further, we can allow the parameters $\alpha$ and $b_{A}^{\beta}$ used for defining the acceptable values of the dependent attribute to be level-dependent and keep these values with each node in the index. This may allow us to reject a tuple with an unacceptable value of the dependent attribute at a high level in the index tree. In agglomerative methods, the index tree can be combined with the Dendogram and can be defined as the initial clusters are generated. Once the tuple is found to be acceptable, it is natural to place it in the cluster for which the membership function $\mu_{BELONGS}$ is largest at the highest possible threshold. If centroids are being used to determine the cluster-cluster similarity, the attribute values of the centroid (of the cluster receiving the tuple) will have to be recalculated with each insertion or deletion. Such recalculation can possibly change the thresholds at which merger would have taken place. However, to the extent the relative rankings of the thresholds do not change, the agglomeration tree would not be affected significantly, and hopefully such effects can be confined to the lower levels of the tree. When using an agglomerative method, overlap between the clusters is not allowed (though by definition, the clusters are nested), so the incoming tuple will be placed in at most one cluster at the lowest level. If we follow some other method where overlapping clusters are allowed, an update would potentially affect more than one cluster. In such a case identifying all the clusters which are affected by an update, revising the centroid attributes, and updating the index tree may be very expensive. Determining appropriate strategies for maintaining clusters for more general clustering methods is a topic for future research.

A CD does not incorporate the corresponding FD unless of course each cluster contains just one tuple. The CDs, therefore, do not lead to decomposition rules in the same way that the FDs and FFDs do. Instead, to enforce a CD we modify the database to include the cluster definitions and the definitions of the “typical values” for the dependent variable for each cluster, and modify the DBMS to (1) include the procedures to determine the clusters to which an incoming tuple belongs, and (2) determine whether the value of the dependent attribute is similar to the typical values of the dependent attribute for these clusters.

## 6. Summary and conclusions

In this work we have provided a discussion of methods for incorporating approximate dependencies in database systems. Two methods, fuzzy functional dependencies and probabilistic dependencies have been proposed by other authors, while we propose cluster dependencies. For each method, we identify its limitations and describe the added data structures and procedures which have to be incorporated in the database system.

In the cluster dependency framework, the tuples in a relation are classified into clusters based on the independent attribute mentioned in the approximate relationship. The restrictions on the values of the dependent attribute are then given in terms of the values of the attribute for tuples in the nearby clusters. We suggest using similarity with cluster centroids to determine if a new tuple has acceptable values for the dependent attribute. The similarity function we suggest includes a discounting factor so that comparisons with distant clusters will provide liberal bounds whereas comparisons with nearby clusters will provide tight bounds. We suggest using an agglomerative clustering scheme with average linkage to arrive at an initial set of clusters. The cluster dependency framework also does not lead to decomposition rules the same way the fuzzy dependency framework does. However, it allows us to incorporate a much wider class of approximate relationships. It requires that the cluster centroids and the similarity measures used to enforce a cluster dependency be maintained. Note that once the database has been augmented in such a manner, the cluster dependency may be used for approximate reasoning, i.e. to infer the approximate values of the dependent attribute for a given value of the independent attribute. This is similar to maintaining conditional frequency distributions in the presence of probabilistic dependencies and using them to estimate the moments of the conditional probability distribution [5]. Developing inference rules using cluster dependencies, similar to those in the presence of probabilistic dependencies [10] or fuzzy functional dependencies [2,8,11], is another interesting extension of this work. Another issue which we have not addressed here is whether the centroid definitions of the affected cluster(s) should be revised with each update or periodically. We plan to address these and other issues in a future paper.

As a closing note, we mention that we have implicitly assumed that enforcing an approximate constraint can be economically justified. In real life situations the cost of enforcing an approximate constraint may be much higher than the cost associated with erroneous data entry. This will be the case especially when enforcing an approximate constraint requires scanning a large dataset. In such a case off-line audit procedures may be preferable doing validation checks at the time of data entry. In a future paper, we plan to study the trade-off between the cost of using erroneous data and the cost of enforcing approximate relationships to arrive at guidelines on when and how to enforce approximate constraints.

## References

[1] M.S. Aldenderfer and R.K. Blashfield, Cluster Analysis, Sage University Paper Series on Quantitative Applications in Social Sciences, 07-044 (Sage Publications, Newbury Park, 1984).

[2] W. Buckles and F. Petry, Uncertainty Models in Information and Database Systems, Journal of Information Science: Principles and Practice 11 (2) (1985) 77–87.

[3] R. Haux and U. Eckert, Nondeterministic Dependencies in Relations: An Extension of the Concept of Functional Dependency, Information Systems 10 (2) (1985) 139–148.

[4] G.J. Klir and T.A. Folger, Fuzzy Sets, Uncertainty and Information (Prentice-Hall, Englewood Cliffs, 1988).

[5] E. Lefons, A. Silvestri and F. Tangorra, An Analytic Approach to Statistical Databases, Proceeding of the 9th International Conference on Very Large Data Bases (1983) 260–274.

[6] D. Maier, The Theory of Relational Databases (Computer Science Press, Rockville, 1983).

[7] V.V. Raghavan and M.Y.L. Ip, Techniques for Measuring the Stability of Clustering: A Comparative Study, in: Lecture Notes in Computer Science, 146: Research and Development in Information Retrieval eds. G. Salton and H.-J. Schneider, (Springer-Verlag, New York, 1982) 209–237.

[8] K.V.S.V.N. Raju and A.K. Majumdar, Fuzzy Functional Dependencies and Lossless Join Decomposition of Fuzzy Relational Database Systems, ACM Transactions on Database Systems 13 (2) (1988) 129–166.

[9] G. Salton and M.J. McGill, Introduction to Information Retrieval (McGraw-Hill, New York, 1983).

[10] E. Wong, A Statistical Approach to Incomplete Information in Database Systems, ACM Transactions on Database Systems 7 (3) (1982) 470–488.

[11] L.A. Zadeh, A Theory of Approximate Reasoning in: Machine Intelligence, Volume 9, eds. L.. Hayes, D. Michie and C.I. Mikulichi, (Ellis Horwood, Sussex, 1979).
