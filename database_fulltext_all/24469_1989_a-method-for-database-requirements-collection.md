---
otero_id: 24469
otero_key: "E4SZVJMD"
title: "A Method for Database Requirements Collection"
authors: "Veronica P. Tseng; Michael V. Mannino"
year: "1989"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1989.11517857"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Method for Database Requirements Collection

Veronica P. Tseng & Michael V. Mannino

To cite this article: Veronica P. Tseng & Michael V. Mannino (1989) A Method for Database Requirements Collection, Journal of Management Information Systems, 6:2, 51-75, DOI: 10.1080/07421222.1989.11517857

To link to this article: http://dx.doi.org/10.1080/07421222.1989.11517857

![](/api/attachments/E4SZVJMD/fulltext/images/a80d6350dda08a257ef31ecd8539c6ac4a46b895b1ebe510efd9280f6d929d68.jpg)

Published online: 22 Dec 2015.

![](/api/attachments/E4SZVJMD/fulltext/images/2169db64dedbace1e229eeb3cd1f7715f64fe43a58564e6e3aa880a3182ff939.jpg)

Submit your article to this journal ↗

![](/api/attachments/E4SZVJMD/fulltext/images/70769d99659c2e5c5617380158dd62078548b9b59243780c162cb45df983e4a3.jpg)

View related articles ↗

![](/api/attachments/E4SZVJMD/fulltext/images/f02bf5361265706680db5dac4daf0066684e2a091f49226ce14a8af24dde9260.jpg)

Citing articles: 5 View citing articles ↗

# A Method for Database Requirements Collection

VERONICA P. TSENG and MICHAEL V. MANNINO

VERONICA P. TSENG received her Ph.D. in Information Systems from the University of Texas at Austin in 1988. She was on the faculty of the Management Sciences Department, University of Massachusetts at Boston from 1987 to 1988. She joined IBM Rochester, MN, as Staff Programmer in July 1988. Currently, she is working on the Distributed Data Management architecture and its compliance testing. Her research interests include object-oriented programming, requirements collection, and user interface design.

MICHAEL V. MANNINO received his B.B.A. degree from the University of Cincinnati in 1978 and his M.S. and Ph.D. degrees from the University of Arizona, Tucson, in 1981 and 1983, respectively. He was Assistant Professor of Computer and Information Sciences at the University of Florida from 1983 to 1985. He is currently Assistant Professor of Information Systems in the Department of Management Science and Information Systems at the University of Texas at Austin. He has published in the areas of schema integration, database design, query optimization, data dictionary systems, and object oriented databases. His current research interests are in the areas of object oriented databases, database design, hypertext, and model management. He is a member of the ACM and the IEEE Computer Society.

ABSTRACT: We describe an approach for increasing user involvement in the collection of database requirements. The approach is based on a form definition system that makes inferences from examples of form instances. The system permits the user to state requirements directly or to provide examples of requirements. Inferences from examples are made from the bottom up by considering one example at a time using a collection of rules and heuristics. To control the burden of providing lengthy examples, the system generates some of its own examples, provides access to example histories, and offers informative feedback to help the novice user become an expert user. The inference strategies support the collection of application-specific requirements, such as the hierarchical structure of a form, and invariant properties, such as functional dependencies among form fields.

KEY WORDS AND PHRASES: Database requirements, database view modeling, end-user computing, form definition systems.

## 1. Introduction

DATABASE REQUIREMENTS CAN BE DIFFICULT TO OBTAIN. Traditionally, a database designer or systems analyst conducts interviews with end users to discover their requirements. This traditional approach can be costly and time consuming because end users must always successfully communicate their requirements through an intermediary. However, Martin [19] and De Marco [9] reported that the major problem with requirement definitions lies in communication. Systems analysts who are skilled in this intermediary role are scarce resources. One way to reduce the cost and time of requirements collection is to reduce the role of the intermediary and increase the role of the end user.

In this paper, we propose an alternative method for requirements collection, based on a form definition system that makes inferences from examples of form instances. Our method can supplement existing requirement collection techniques where forms constitute important uses of the database. By form we mean any structured collection of variables that are appropriately formatted to support both data entry and retrieval. This approach allows direct involvement in database requirements through defining the forms used in the office environment. The target users are familiar with the applications in the functional areas, but do not necessarily possess the database knowledge.

Our form definition system provides two modes: an expert mode where the requirements are stated directly, and a novice mode where the requirements are inferred from examples and a purposeful dialogue. A small collection of rules and heuristics is used to make inferences from examples. These rules are divided into groups depending upon the type of requirement to which they apply: hierarchical structure, node keys, and functional dependencies. To reduce the user's time in providing examples, the system generates some of its own examples and provides an example history facility. A dialogue supports requests for more examples and confirmation of system-generated examples. The system also provides a feedback facility that can be consulted during form definition by an end user, and later by a database designer to review the requirements collected.

This work extends a previous effort on view integration $[7]$ with a view modeling component. The view integration system features a collection of rules for grouping the fields on a form into aggregate objects (e.g., entities and relationships) and an algorithm for ordering a collection of forms for incremental view integration. The view definitions (i.e., the form definitions) were assumed to originate with a database designer. Our study proposes a method for view modeling with non-data processing users, and it does not deal with the integration aspects. Our approach is based on inferences from examples of form instances, while the previous work on integration did not make such inferences. Our prototype form definition system can be seen as the view modeling component for the view integration system. In a broader sense, our form definition system can serve as a view modeling component for other view integration approaches because it provides view definitions that are data model independent.

This paper is organized as follows. Section 2 compares our work to other proposals. Section 3 overviews this study including the form model, the strategy of learning from examples, and the system architecture. Section 4 describes the inference strategies for the form hierarchy, node keys, and dependencies. Section 5 describes the prototype implementation and preliminary testing with a small collection of users. Section 6 concludes this work.

## 2. Related Work

A VIEW IS A REPRESENTATION OF DATA THAT IS NECESSARY FOR A USER to accomplish some information processing tasks. The problem of eliciting a user's view (i.e., view modeling) has mainly been addressed as a byproduct of data model development. Typically, researchers have assumed that end users can understand and construct data model diagrams.

Our work [26, 27] is a study of the view modeling problem without the assumption that the user can understand and construct data model diagrams. Instead, our study is based on the form approach and inferences from examples of form instances. The form represents a user's view of a database and describes the requirements that the underlying database should satisfy. In the last few years, there have been related studies that address some but not all aspects of our work. These other studies provide alternative approaches for view modeling. They can be classified according to their emphasis on (1) learning from examples, (2) natural language, (3) structured input/output definitions, and (4) schema definitions given by users.

Using the learning approach, Borgida, Mitchell, and Williamson [3] applied learning from examples and explanation-based learning to the modification of an existing database schema and integrity constraints. Their techniques could suggest schema changes such as loosening integrity constraints, and adding subclasses and attributes. Their users were data processing professionals. Mannila and Raiha [17] devised an approach to generate example relations that preserve the Armstrong axioms [13]. Our approach for making inferences of node keys and functional dependencies is similar in that our generated form examples preserve the constraints of the form rather than Armstrong's axioms.

With emphasis on natural language, Lanka $[16]$ described a method to infer a database schema automatically by using the strategy of learning from examples. The users were database designers who provided natural language sentences that described the usage of a database. The system applied generalization operators to form abstractions from the syntactic structure of these sentences. Bouzeghoub and Gardarin $[4]$ report the implementation of an expert system that uses limited natural language to derive a relational schema in 3rd Normal Form. De Antonellis and Demo $[8]$ , on the DATAID-1 project, described a manual methodology for collecting natural language requirements from a user. The natural language sentences are manually simplified and classified by data, operation, and event. Eick $[11, 12]$ , on the Annapurna Project, reported a similar approach with unrestricted natural language input from different user groups. One of his major results was a technique to unify the terminology of different user groups.

With emphasis on structured input/output, Gerritsen [15] employed a structured language named the Hierarchical Interactive Query Language (HI–IQ). Based on a collection of queries in this language, the design of a database structure was inferred. He required users to know a structured query language and to group fields into records in query language expressions. In contrast, our approach uses forms without pre-defined record boundaries and example data instead of query language statements. Choobineh [6] used a form approach to derive functional dependencies. The differences between his approach and ours are (1) his approach assumes that a form hierarchy is given; (2) his approach does not make inferences from examples; and (3) his approach provides more heuristic rules about form field names and origins. Moreover, his approach is intended for a database designer who responds to suggestions based on the properties of form fields, such as their name, origin, and position.

With emphasis on schema input, Wilson [29] designed a tool for defining requirements and generating a relational schema design. The input included the definitions of entities, events, attributes, relationships, and processes of an application. Using mapping rules, relations in a specified normal form were generated. The target users were database designers. Storey and Goldstein [24] described the View Creation System that uses the Entity-Relationship model and a purposeful dialogue with end users. In their study, users were required to differentiate entities from attributes. However, they reported that users were not always able to do so.

## 3. An Overview

OUR FORM DEFINITION SYSTEM SUPPORTS THE DEFINITION of two dimensional electronic forms consistent with proposals such as $[22, 23, 30]$ . To accommodate different types of users, our approach provides two modes: an expert mode where the requirements are stated directly, and a novice mode where the requirements are inferred from examples and a purposeful dialogue. In the expert mode of operation, this approach is very similar to previous studies, except that it also supports the definition of functional dependencies. In the novice mode, this approach is novel because it provides an inference component. In this section, the proposed architecture will be described. Before explaining the architecture, a brief review of the underlying form model and learning from examples is presented.

## 3.1. Form Model

A form consists of a title, form fields, and blank spaces or slots for accepting and displaying data values of form fields. When a blank form is filled with data values, it is a form instance. The form model supports hierarchically structured form fields because a form provides a hierarchical view of the underlying database. There is no limit to the number of levels or nodes within a level, although most forms have a shallow (i.e., few levels) and narrow (i.e., few nodes per level) structure. The form hierarchy is described by grouping form fields into nodes and by identifying the structure of the nodes. An underlying premise of this work is that there is a unique hierarchy to represent each form.

In this approach, the forms are defined before the underlying database. We include functional and multivalued dependencies as part of the form definition, because they can be useful in designing the underlying database and the form/database mapping. Since a form is used for both data entry and display, it provides an updatable view on an underlying database. Thus, the dependencies that hold on the form must also hold on the underlying database.

Other form properties include the origin of form fields and the flow of control among forms. These are not relevant here and details can be found elsewhere [7].

## 3.2. The Strategy of Learning from Examples

The basic ideas of learning from examples $[10]$ are to obtain examples from an information source and to apply generalization operators for learning the goal concept. Examples can be positive, describing the goal concept, or negative, contradicting the goal concept. The source of examples can be a teacher who knows the concept and generates examples, the learner who knows his/her own knowledge state but not the concept to be acquired, or the external environment, which is usually uncontrollable.

In this work, we emphasize inference from positive examples rather than generalization from examples. The primary source of examples is a form user who knows how to fill out a form but not necessarily the form properties. An example is simply a data value in a form. Since the examples are actual or simulated business data, they are positive examples. The system is a secondary source of examples. At certain times, the system can generate examples that can be positive or negative. An example accepted by a user is a positive example; otherwise it is negative. For example, a duplicate value of a key is a negative example. This approach to negative examples is chosen because a user may have difficulty directly generating negative examples. From these examples, a few inference rules and heuristics are applied to infer the goal concepts.

Generally speaking, the proposed approach is syntactic and can be described as single-concept, search-based inference. The syntactic approach is useful for this study because it is application independent. Hence, the same approach can be consistently applied to different forms. A complimentary semantic approach based on natural language input is described in $[18]$ .

## 3.3. System Architecture

Figure 1 illustrates the architecture of the Form Definition System. The Form Layout component provides a full screen editor for entering form field captions, form trim, and example values. The Command component provides functions such as saving, creating, and opening form definitions and displaying data. The Interface component provides a Macintosh-like environment with pull-down menus, a pointing device, and bit-mapped graphics. In addition, it provides both the expert mode and the novice mode. The collected requirements are stored in the Form Abstraction Base.

The Inference component supports the novice mode. It can be divided into two sub-components. The Hierarchy component makes inferences from examples about the grouping of form fields into nodes, the hierarchical relationship between nodes, and the node keys. The Dependency component makes inferences about functional dependencies (FDs), computational dependencies, and multivalued dependencies among form fields. Some dependencies can be implied by the hierarchical structure of a form, but others must be obtained through an analysis of examples. In both subcomponents, a dialogue is necessary to ask for examples and confirm user beliefs.

![](/api/attachments/E4SZVJMD/fulltext/images/64a2f926268817192bb5a695ee2e5c1747b4987abae1290619b8c513f9fa9913.jpg)  
Figure 1. System Architecture

Section 4 describes the design of the inference strategies for the hierarchical structure and functional dependencies.

When a user becomes sufficiently trained, the expert mode is preferable to the novice mode because requirements can be stated directly. To help the novice become an expert user, the Inference component provides explanatory feedback. Section 4.3 describes the design of the explanatory feedback.

As mentioned in the Introduction, the Form Definition System is the view modeling component for the Expert Database Design System $[7]$ . The results of a form definition are stored in the Form Abstraction Base and are then used by the Expert Database Design System. The layout, hierarchical structure, and node keys are used by the heuristic rules of the Expert Database Design System to make suggestions for grouping form fields into entity types and relationships. The functional and multivalued dependencies are used to normalize the resulting Entity-Relationship diagram and to ensure a correct diagram.

## 4. Inference Strategies

OUR INFERENCE TECHNIQUES USE A SMALL SET OF UNDERLYING DEFINITIONS and assumptions that are described in section 4.1. Based on these concepts, the rules and heuristics to infer the form hierarchy, node keys, and dependencies are presented in section 4.2. Section 4.3 describes how the inferencing results are presented to a user.

## 4.1. Basic Definitions and Assumptions

The terms to be defined include node, null field value, node key, missing node value, cardinality, and fully non-normalized data entry. These terms are defined according to the discussions of $[1, 5, 28]$ . To help explain the definitions, Figure 2 presents a form instance with annotations.

Definition 1. Node. A node is an independent group of one or more fields that have the same count of data values in a form instance. A node is also referred to as a record. For example, in Figure 2, SIZE, DIMENSION, PRICE, QTY, and TOTAL belong to the same node. The node without a parent is the root node. Otherwise, it is a dependent node. The nodes are numbered from top to bottom and from left to right starting from zero.

Definition 2. Cardinality. The count of data values of a form area is the field cardinality. The count of occurrences of a node is the node cardinality. A node cardinality is the same as the field cardinality of any of its constituent fields. This distinction between node and field cardinality facilitates the later discussions of the rules and heuristics.

Definition 3. Null Field Value. A field with an unknown or inapplicable value is considered to have a null field value. Special symbols, such as a dash (-) for value unknown and an at sign (@) for value inapplicable, are used to capture this information. When determining a field cardinality, null field values are counted.

Definition 4. Missing Node Value. A missing node value is either an implied or unneeded value. A node n has an implied value if its adjacent node at the direct right (i.e., node $n + 1$ ) has more occurrences than node n. The existence of an implied value results from the hierarchical nature of a form. Node m has an unneeded value if there are blanks and these blanks are not implied values. Unneeded values indicate a path change. When determining a node cardinality, missing node values are not counted. In Figure 2, both nodes one and three have missing node values where the blanks of the former are implied values and the blanks of the latter are unneeded.

Definition 5. Node Key. A node key is the concatenation of a local key with the node key of its parent. It uniquely identifies a node. Since the form model is hierarchical, the concatenation is necessary. A local key uniquely identifies occurrences within a parent occurrence. Therefore, key fields do not allow duplicates nor null values.

Definition 6. Fully Non-Normalized Data Entry. Data entry is fully non-normalized if in a one-to-many relationship, the parent occurrence is entered only with the first child occurrence. This definition is recursively applied to all dependent nodes. This format saves keystrokes because missing node values are implied rather than explicit.

<table><tr><td colspan="8">PRODUCT LIST FORM</td></tr><tr><td colspan="2">SUPPLIER</td><td colspan="2">DuraPavex, Inc.</td><td colspan="4">SUPPLIER NO 001</td></tr><tr><td>PRODUCT NAME</td><td>PRODUCT CODE</td><td>SIZE</td><td>DIMENSION</td><td>PRICE</td><td>QTY</td><td>TOTAL</td><td>COLOR</td></tr><tr><td rowspan="2">duralock</td><td rowspan="2">1</td><td>S</td><td>9*4*2</td><td>1.30</td><td>2000</td><td>2600.00</td><td>limestone</td></tr><tr><td>L</td><td>9*4*3</td><td>1.40</td><td>2000</td><td>2800.00</td><td>charcoal</td></tr><tr><td>durastar</td><td>2</td><td>L</td><td>8*8*2</td><td>1.50</td><td>2500</td><td>3750.00</td><td>autumn red</td></tr><tr><td rowspan="3">duracobble</td><td rowspan="3">3</td><td>S</td><td>4*2*2</td><td>0.40</td><td>1800</td><td>720.00</td><td>buda brown</td></tr><tr><td>M</td><td>4*2*2</td><td>1.05</td><td>4000</td><td>4200.00</td><td></td></tr><tr><td>L</td><td>--</td><td>1.40</td><td>4200</td><td>5880.00</td><td></td></tr><tr><td>duragreen</td><td>4</td><td>L</td><td>6*4*3</td><td>0.85</td><td>3000</td><td>2550.00</td><td></td></tr><tr><td rowspan="2">duracurb</td><td rowspan="2">5</td><td>L</td><td>9*3*8</td><td>2.85</td><td>1200</td><td>3420.00</td><td></td></tr><tr><td></td><td></td><td colspan="2">GRAND TOTAL</td><td>25920.00</td><td></td></tr><tr><td colspan="8">field cardinality:</td></tr><tr><td>5</td><td>5</td><td>8</td><td>8</td><td>8</td><td>8</td><td>8</td><td>4</td></tr></table>

Figure 2. An Instance of Product List Form with Annotations

For example in Figure 2, the first occurrence of node one <duralock, 1> is not repeated for the second occurrence of its child.

Three assumptions use these definitions and underly most of the rules described in sections 4.2 through 4.3. These assumptions are the conclusion from the analysis of form management systems such as [23]. The first assumption constrains the manner in which a user enters examples. The second and third assumptions involve the relative position of form fields within a node and the relative position of nodes.

Assumption 1: Users enter data in a fully non-normalized format.

Assumption 2: Except for the root node, fields of the same node are positioned together.

Assumption 3: Nodes on the same path are positioned adjacently from left to right where the left node is on a hierarchical level with a smaller value.

These assumptions make the inference problem tractable and are good rules of form design. Since the objective of this study is to define strategies to infer the technical properties of a form and not to teach principles of form design, these assumptions seem reasonable. Nevertheless, suggestions for form design are useful byproducts of the inference process. Relaxation of these assumptions and other issues of form design are subjects of further study.

## 4.2. Inference Rules and Heuristics

The proposed inference strategies use heuristics and rules. The heuristics suggest structures and assertions for a given example set. They are not provably correct because assertions cannot be proven from an example set. The heuristics are designed on the basis of rules that are theoretically proven correct $[26]$ , or on empirical analysis of many form instances. Inference rules are sometimes used to prove that an assertion cannot hold or to make further inferences from basic assertions.

## 4.2.1. Form Hierarchy

The system infers the form hierarchy in four steps. Firstly, cluster form fields into nodes. The FIELD CLUSTERING heuristics are applied to two fields in a left-to-right, top-to-bottom fashion until there are no more fields. Secondly, identify each path and determine its hierarchical structure. The PARENT-CHILD IDENTIFICATION heuristics and the PATH DETECTION rule are applied to two nodes in a similar fashion described in step one. Thirdly, identify the parent nodes of multi-path structures. The MULTI-PATH PARENT rule and heuristic are applied to each detected path. Lastly, refine the conclusion through additional instances and generalize to the hierarchy that covers all the examples. For each example, the system infers one hierarchy using the rules and heuristics of the first three steps. The rules and heuristics are designed to infer the simplest plausible hierarchy for an example. This is based on our philosophy that most forms will have a simple hierarchical structure. If more than one hierarchy is inferred for the collection of examples, the system chooses the hierarchy that covers all the examples. The process terminates when the same hierarchy is inferred for two consecutive examples.

Fields are clustered into nodes based on two rules. The first rule identifies the root node, while the second identifies the dependent nodes.

FIELD CLUSTERING RULES

if field $X$ belongs to the root node

then field X has at most one data value

if fields $F_{i},\ldots ,F_{n}$ belong to the same dependent node

then they are positioned adjacently and

have the same field cardinality and

there is a one-to-one mapping of data values of these fields

Based on these rules, FIELD CLUSTERING heuristics are proposed to help with the inferences of root and dependent nodes. These heuristics reverse the field clustering rules. When the conclusion in a FIELD CLUSTERING rule is true, it is assumed that the condition is true.

FIELD CLUSTERING HEURISTICS

if field $X$ has exactly one data value

then assume that X belongs to the root node

if fields $F_{i},\ldots,F_{n}$ are positioned adjacently and they have the same field cardinality of $Y$ and there is a one-to-one mapping among data values of these fields and $Y\geq 2$

then assume that $F_{i},\ldots,F_{n}$ belong to the same dependent node

In Figure 2, the first heuristic groups SUPPLIER, SUPPLIER NO, and GRAND TOTAL into the root node. The second heuristic produces the dependent nodes of <PRODUCT NAME, PRODUCT CODE>, <SIZE, DIMENSION, PRICE, QTY, and TOTAL> and <COLOR>. The number of the root node is zero. The dependent nodes are numbered in a depth-first manner.

After identifying the nodes, paths of nodes and the hierarchical position of nodes within a path are determined. Two adjacent nodes are either a parent–child combination or they lie on different paths. The PARENT–CHILD rule uses information about node cardinality and missing node values to handle the first case.

PARENT-CHILD IDENTIFICATION RULE

if there is a parent-child relationship between nodes $n$ and $n + 1$

then the cardinality of node $n \leq$ the cardinality of node $n + 1$ , each occurrence in node $n$ has an occurrence in node $n + 1$ , there may be missing node values between occurrences of node $n$

The following heuristics are designed on the basis of this rule and are used for inferences.

PARENT-CHILD IDENTIFICATION HEURISTICS

if the cardinality of node $n$ is $<$ cardinality of node $n + 1$ and each occurrence in node $n$ has an occurrence in node $n + 1$ and there are missing node values between occurrences of node $n$

then assume that node $n$ is the parent of node $n + 1$

if the cardinality of node $n$ is $<$ cardinality of node $n + 1$ and each occurrence in node $n$ has an occurrence in node $n + 1$ and there are no missing values between occurrences of both node $n$ and $n + 1$ .

then assume that node $n$ is the parent of node $n + 1$

In Figure 2, the cardinality of the node one <PRODUCT NAME, PRODUCT CODE> is five, which is smaller than the node cardinality of node two (i.e., eight), and there are implied missing values in node one. According to the first heuristic, node one is the parent of node two. In these heuristics, the case where two nodes have the same cardinality is excluded because the FIELD CLUSTERING heuristic covers it.

![](/api/attachments/E4SZVJMD/fulltext/images/a490eb1b47a1062310c4cdc3b41e3ccd513fd35cc88c71ca1c2dd685aa69e166.jpg)

<table><tr><td colspan="2">a)</td><td colspan="3">b)</td></tr><tr><td>R</td><td></td><td>R</td><td></td><td></td></tr><tr><td> $\underline{D_{1}}$ </td><td> $\underline{D_{2}}$ </td><td> $\underline{D_{1}}$ </td><td> $\underline{D_{2}}$ </td><td> $\underline{D_{3}}$ </td></tr><tr><td> $D_{11}$ </td><td> $D_{12}$ </td><td> $D_{11}$ </td><td> $D_{12}$ </td><td> $D_{13}$ </td></tr><tr><td></td><td> $D_{22}$ </td><td></td><td> $D_{22}$ </td><td> $D_{23}$ </td></tr><tr><td> $D_{31}$ </td><td> $D_{32}$ </td><td></td><td></td><td> $D_{33}$ </td></tr><tr><td></td><td></td><td> $D_{41}$ </td><td> $D_{42}$ </td><td> $D_{43}$ </td></tr></table>

![](/api/attachments/E4SZVJMD/fulltext/images/481d327b6d1fbe5556624587be404526a50da376196ad9927c1d3a88ab150525.jpg)  
Figure 3. Example Form Instances Representing One-path, Multi-level Structures

The iterative application of the first heuristic identifies the one-path, multi-level structures such as those shown in Figure 3. For simplicity, each letter represents one node in a form instance. R denotes the root node, $D_{j}$ denotes the dependent node j, and subscript ij denotes row i of node j.

Application of the first parent–child heuristic cannot deal with a parent–child relationship when there are no missing values between occurrences of node n, and the last occurrence of node n is followed by blanks. The blanks can be interpreted as either implied or unneeded values. If they are implied, a parent–child relationship exists. If they are unneeded, the nodes lie on different paths. Figure 4 depicts an example.

To deal with this ambiguity, we apply the second parent–child heuristic. It provides a conservative inference because it concludes that only one path exists. If the system later infers a structure with more paths, the user is asked to provide additional examples or to extend the ambiguous example.

If two adjacent nodes are not related as a parent–child combination, they must lie on different paths. The PATH DETECTION rule uses information about the positions of data values and node cardinality to decide that two nodes lie on different paths. This rule is defined as:

R  
![](/api/attachments/E4SZVJMD/fulltext/images/9929606805483bb646a52b51f8f5ac207351ae19fa3fdaf9248262f5de4243d6.jpg)  
Figure 4. An Example of One Form Instance Representing Different Tree Structures

## PATH DETECTION RULE

if there is not an occurrence of node $n + 1$ for each occurrence of node $n$ or the cardinality of node $n >$ the cardinality of node $n + 1$

then node $n$ and node $n + 1$ belong to different paths

In Figure 2, the cardinality of node two (i.e., <SIZE, DIMENSION, PRICE, QTY, TOTAL>) is not smaller than that of node three (i.e., <COLOR>), and for each occurrence of node two, there is not an occurrence for node three. Hence, the PATH DETECTION rule infers that node two and node three belong to different paths.

More generally, the PATH DETECTION rule can be used to detect the existence of different paths in any instances. For example, the existence of multiple paths in Figures 5 and 6 can be detected.

Once a new branch is detected, the PARENT-CHILD IDENTIFICATION heuristics are applied to identify the structure of a path. To decide the parent of node $n + 1$ , which lies on a different path than node $n$ , the following rule is used.

## MULTI-PATH PARENT RULE

if nodes $n$ and $n + 1$ belong to different paths and

node $m$ has an occurrence in row $i$ and

$$
m \leq n - 1 \text {   and   }
$$

node $n + 1$ has missing node values in row $i$

then node $m$ is not the parent of node $n + 1$

This rule eliminates nodes as potential parents. If node m contains a value in a row where node $n + 1$ does not, node m cannot be the parent of node $n + 1$ . If multiple parent nodes are still possible, the following heuristic is designed to make the most conservative inference.

## MULTI-PATH PARENT HEURISTIC

If multiple parents are identified by the MULTI-PATH PARENT rule then the parent on a hierarchical level of larger number is selected

Since a root node is relatively easy to identify and the rules and heuristics are designed to identify the parent of a node, the potential parent with the largest hierarchical level (i.e., lowest in the tree) is assumed initially. If the result of applying the MULTI-PATH PARENT rule and heuristic to a later instance contradicts this assumption, the upper level parent can always be selected until the root node is reached. The root node is never eliminated and is the default choice.

As an example of the PATH DETECTION and MULTI-PATH inferences, consider Figure 2. As discussed earlier, node two and node three belong to different paths. The candidate parents of node three are nodes zero and one. Since node three has a missing node value in row 7, but node one contains values (i.e., <duragreen, 4>) in that row, node one is disqualified and node zero is selected. The MULTI-PATH PARENT rule and heuristic can be used to identify both of the structures in Figure 6.

For each instance provided, we apply the previously discussed rules and heuristics to identify the simplest, plausible hierarchy that represents the given instance. However, the chosen hierarchy may not be the true one because there are multiple plausible hierarchies for any form instance. Our approach is to ask for at least two instances and then to select the hierarchy that covers all the instances. The process terminates when identical hierarchies have been inferred for consecutive instances.

To help choose the covering hierarchy, we employ a simple taxonomy of form hierarchies. A form hierarchy X is less general than than a form hierarchy Y if every valid instance of X can be considered as a valid instance of Y. Informally, an instance of hierarchy X is also a valid instance of hierarchy Y if the blank values of X do not contradict Y. Only hierarchies with simpler structures (i.e., fewer levels, paths, or nodes) can be contradicted because blanks indicate boundaries between levels and paths (i.e., implied and unneeded values). Thus, a hierarchy with more levels, paths, and nodes can never be contradicted by an example. We formalize the less general relation using levels, paths, and nodes as follows:

$$
<   L, P, N > \xrightarrow {\mathrm{LG}} <   L + 1, P, N + 1 >
$$

$$
<   L, P, N > \xrightarrow {\mathrm{LG}} <   L, P + 1, N + 1 >
$$

where $L$ is the number of levels

$P$ is the number of paths

$N$ is the number of nodes

$\xrightarrow{\mathrm{LG}}$ means is less general than

the triplet $< L, P, N>$ defines a family of form hierarchies

R  
![](/api/attachments/E4SZVJMD/fulltext/images/54097326f37b6bbf434cd32e564a001a4ee924cb501f09de1970ae9977381919.jpg)  
D 31

![](/api/attachments/E4SZVJMD/fulltext/images/6277572047e6b42de0f112b0fa0e5bee2171a63b23f27a62a09669d3b68b42f5.jpg)

Figure 5. An Example Form Instance Representing a Two-level, Multi-path Structure

<table><tr><td>R</td><td></td><td></td><td></td><td>R</td><td></td><td></td><td></td></tr><tr><td> $\underline{D_1}$ </td><td> $\underline{D_2}$ </td><td><img src="/api/attachments/E4SZVJMD/fulltext/images/fb7129698adf515fef298649a5bf657209af38b2d7531b0f439e0a2f47bb0f81.jpg"/></td><td> $\underline{D_4}$ </td><td> $\underline{D_1}$ </td><td> $\underline{D_2}$ </td><td>[TZXY]</td><td> $\underline{D_4}$ </td></tr><tr><td> $D_{11}$ </td><td> $D_{12}$ </td><td> $D_{13}$ </td><td> $D_{14}$ </td><td> $D_{11}$ </td><td> $D_{12}$ </td><td> $D_{13}$ </td><td> $D_{14}$ </td></tr><tr><td></td><td> $D_{22}$ </td><td></td><td> $D_{24}$ </td><td> $D_{21}$ </td><td></td><td> $D_{23}$ </td><td> $D_{24}$ </td></tr><tr><td> $D_{31}$ </td><td> $D_{32}$ </td><td></td><td> $D_{34}$ </td><td> $D_{31}$ </td><td> $D_{32}$ </td><td> $D_{33}$ </td><td> $D_{34}$ </td></tr><tr><td></td><td> $D_{42}$ </td><td> $D_{43}$ </td><td> $D_{44}$ </td><td> $D_{41}$ </td><td></td><td></td><td> $D_{44}$ </td></tr></table>

![](/api/attachments/E4SZVJMD/fulltext/images/69796630412d33eec9c0f1ff47947abff42e477c7b86a098af0b0c43b219de39.jpg)

![](/api/attachments/E4SZVJMD/fulltext/images/081a106dc12e0cac6d375074b2db3b2981ed9addc6901b69a9381fe37e21f6cf.jpg)  
Figure 6. Examples of Multi-path, Multi-level Form Instances and Corresponding Structures

![](/api/attachments/E4SZVJMD/fulltext/images/bc249a29428071a412495dffec64f2afdb134cc82f28c019cfb13b5cd6905752.jpg)  
Figure 7. Inference Tree of Form Instances in Structures (Level, Path)

The $\xrightarrow{LG}$ relation defines conditions for families of form hierarchies rather than individual form hierarchies because the relation does not depend on the lengths of individual paths. Graphically, the $\xrightarrow{LG}$ relation can be depicted as in Figure 7. In addition, note that this relation is transitive. The length of a transitive path is only limited by the number of fields on a form.

The rules and heuristics of the first three stages are designed to select a hierarchy lower in this taxonomy (i.e., simpler structures). This fits with our thinking that most forms will be rather shallow and narrow because of inherent information processing difficulties with complex structures. When we compare two instances, we choose the most general hierarchy under consideration using the HIERARCHY INFERENCE RULE shown below. When combined with the rules and heuristics of the first three steps, the HIERARCHY INFERENCE RULE chooses the least general hierarchy that covers all the instances.

## HIERARCHY INFERENCE RULE

$T_{i}$ and $T_{j}$ are two inferred form hierarchies

then

and $T_{i}\xrightarrow{\mathrm{LG}} T_{j}$ directly or indirectly

$T_{j}$ is preferred over $T_{i}$

As an application of the form hierarchy taxonomy, consider the example in Figure 8 as an alternative to the example in Figure 3a. After applying the rules of the first three stages, a $<3$ , $2$ , $4>$ hierarchy is inferred compared to the $<3$ , $1$ , $3>$ of Figure 3a. The principle difference between the examples is that node $D_{2}$ has been split into $D_{2}$ and $D_{3}$ in Figure 8 because of the additional blanks. The PATH DETECTION RULE interprets these blanks as unneeded values. The HIERARCHY INFERENCE RULE makes the <3, 2, 4> the preferred hierarchy.

<table><tr><td colspan="3">R</td></tr><tr><td>D1</td><td>D2</td><td>D3</td></tr><tr><td>D11</td><td>D12</td><td>D13</td></tr><tr><td></td><td>D22</td><td></td></tr><tr><td>D31</td><td>D32</td><td>D33</td></tr><tr><td></td><td>D42</td><td>D43</td></tr><tr><td></td><td>D52</td><td></td></tr></table>

Figure 8. Additional Form Hierarchy Example

The HIERARCHY INFERENCE RULE cannot be applied to structures that are not connected by arrows. For example, there is an ambiguity between structures <4, 1, 4> (Figure 3b) and <3, 2, 4> (Figure 8) because the former contains more levels but fewer paths than the latter. A conflict arises when two examples are interpreted as form hierarchies that are not connected by arrows. To resolve a conflict, the user is requested to provide another example or to augment the given examples. Augmentation is suggested when an example matches the pattern of Figure 4. There is an ambiguity because the example only contains one contiguous collection of values under each column.

If the user does not want to provide another example, we give preference to the form hierarchy with more paths. This is because the form hierarchy with more paths is associated with at least one additional blank that is interpreted as an unneeded value. An unneeded value provides stronger evidence than an implied value, because it denotes a new path (i.e., break in a parent–child relationship), while an implied value may denote either a parent–child relationship or a new path. Thus, the interpretation of a blank as implied is less certain than its interpretation as unneeded. The rules and heuristics of the first three steps are designed to interpret implied values as a new parent–child relationship because of our conservative strategy. These beliefs are revised if a later example contains more unneeded values.

## 4.2.2. Node Keys

After a hierarchy is inferred, the local keys and node keys can be identified. Node keys are determined by identifying, ranking, and testing among potential candidate keys in a depth-first manner. A field in the root node is a potential key if (1) it has no duplicates across form instance examples, (2) it has no examples with null values, and (3) it is not a computed field. For dependent nodes, keys are formed by concatenating the key of its parent with its local key. A field in a dependent node is a potential local key if (1) it has no duplicates within its immediate parent, (2) it has no examples with null values, and (3) it is not a computed field.

Potential keys are ranked as follows. First, fields with unique values are ranked the highest. Second, those fields with unique values are ranked by their data type: (1) integer, (2) character, and (3) real. Third, ties are broken by the left-to-right position of fields in a form, because keys are usually specified before nonkey fields.

In Figure 2, GRAND TOTAL is eliminated because it is a computed field. SUPPLIER NO is ranked before SUPPLIER because SUPPLIER NO is an integer. In the next node, PRODUCT CODE is ranked ahead of PRODUCT NAME because both do not have duplicates nor null values, and PRODUCT CODE is an integer. In node 2, DIMENSION and TOTAL are eliminated because the former has a null value and the latter is computed. Further, QTY is eliminated because there are duplicate values of 2000 within the same the parent value.

After ranking, additional examples are generated to eliminate potential keys by repeating the last value of the field under question. The idea is to force the field under question to have duplicates. The user is inquired about the validity of the generated example through a dialog. If the user accepts the duplicate value, the potential key is eliminated from consideration. For example, testing of node 2 involves the testing of SIZE, DIMENSION, and PRICE. To test SIZE, the system generates a new example with its last value (i.e., 5), while holding constant the values of PRODUCT NAME and PRODUCT CODE.

For a given node, the fields are tested in the ranked order. Testing stops when all the fields have been tested or when the user indicates. The database designer can use the feedback facility to see a history of the fields tested and the keys identified.

## 4.2.3. Dependencies

Functional and multivalued dependencies are assertions about the real world [28]. A functional dependency (FD) $A \rightarrow B$ means that for a given value of A, at most one B value is possible. Multivalued dependencies always occur in pairs. The multivalued dependency (MVD) $A \rightarrow B \mid C$ means that each A value is associated with a collection of B and C values and the B and C value collections are independent. Further, an MVD is embedded if the relation containing A, B, and C also contains another collection of attributes that are not part of A, B, or C.

Some FDs and MVDs can be inferred from the hierarchical structure, the node keys, and the mathematical formulas. A node key determines the other fields in its node. For the root node, the node key is simple because the form is fully non-normalized. For dependent nodes, a node key is composite because of the concatenation between the local key and the node key of its parent. If there are several candidate node keys, there is a mutual dependence among them. Functional dependencies can also be implied by mathematical formulas given by the user. A formula specifies a dependency between the computed field and the fields in the formula. That is, a computation dependency has a composite determinant.

Multipath structures imply MVDs (possibly embedded). If $D_{j}$ and $D_{k}$ are siblings with common parent $P_{i}$ , the MVD $P_{i}.NK \rightarrow D_{j}.LK \mid D_{k}.LK$ holds where NK represents the node key and LK the local key. See [26] for the proof. This rule can be applied iteratively across a level and recursively down a hierarchy. Multipath structures are not common because of the existence of MVDs. Users cannot grasp wide multipath structures because of the independence among fields collections.

The remaining FDs are between fields of a node. In the root node, FDs among non-key fields are not implied by the node key. In dependent nodes, FDs between any two fields are not implied by the node key. The number of remaining single determinant FDs in a node is $P_{2}^{N}$ where N is the number of form fields for dependent nodes and the number of non-key fields for the root node. There are also composite determinant FDs that are not implied by the node keys or mathematical formulas. Because these FDs occur rather infrequently and lead to a combinatorial explosion of examples, we do not provide example inference strategies for them.

To capture the remaining FDs, our inference strategy initially eliminates FDs by applying the equality test to examples in instances. An example eliminates the FD: $A \rightarrow B$ if two rows agree on the same A value but differ on the B value. Users can augment the initial examples with new examples so that more FDs can be eliminated. All the example values of a node are collected and presented as a normalized table. The user is instructed to provide examples according to the following guidelines:

Do not create a duplicate entry.

Do not create a totally different entry.

The idea is to maximize the amount of information an example provides. The user can stop providing examples and allow examples to be generated for testing the remaining FDs. In addition, the HISTORY function is designed to help a user generate examples. The user can cut and paste examples from related forms or other instances of the same form using the HISTORY function.

The remaining FDs are sorted by the left-to-right position of the determinant field. The system generates examples by holding the determinant constant and generating a new value for the determined field. The new value is the first different value encountered in the example of the determined field. The user confirms the truth of the generated examples according to their understanding of the form.

Obviously, the system can generate examples to test all remaining dependencies. If this proves too much of a burden, the user can stop at any point. It may be more practical not to try for exhaustive requirements collection directly from the user. The designer can later examine the state of the testing process using the feedback facility and take appropriate action. In particular, the designer should add composite determinant dependencies that are not a consequence of node keys. From the augmented set of dependencies, a synthesis algorithm $[2, 20]$ can be used to compute a minimal cover and search for redundancies.

As an example of testing for functional dependencies, consider node 3 from Figure 2. Assume that SIZE is the only local key. Since TOTAL is a computed field, it is excluded from the inference. There are 12 remaining FDs (i.e., $n(n - 1) = 4 \times 3$ ). The equality test eliminates all FDs where the determinant is SIZE or QTY. For example, the first two rows of Figure 2 eliminate the dependencies QTY → PRICE, DIMENSION, SIZE. Likewise, the second and third rows eliminate the dependencies with SIZE as the determinant. To test the FDs with a determinant of DIMENSION, the user can either supply additional examples or the system can generate additional examples. The system would generate examples with the last value of DIMENSION ('9\*3\*8') paired with values of SIZE ('M'), PRICE ('0.85'), and QTY ('3000') encountered in previous rows. Each of these values is displayed one at a time so that a potential FD can be eliminated.

## 4.3. Feedback Facility

One of our long-term goals is to upgrade novice users to expert users so that they can state directly the requirements for database design. This goal is supported by providing informative feedback to the user. The explanations provided are in two categories: the background knowledge for inferring form properties, and the properties inferred for the current form. For the background knowledge, the system provides the definitions of the important terms such as field, field cardinality, node, root node, dependent node, numbering scheme for nodes, and so on. Visual displays are used for explaining concepts related to the hierarchical structure of a form.

The system offers explanatory feedback for all of the form properties that it infers. The feedback is organized by major (hierarchical structure, keys, dependencies) and minor categories (e.g., node clustering and parent–child relationships within hierarchical structure). Within each category, there are multiple levels of detail. The highest level of detail provides a summary of the results. The next level of detail presents the rules and heuristics applied during the inferencing process. The lowest level lists a complete trace of the inferencing steps. Consider the parent–child relationship as an example. The highest level explanation describes the parent and child nodes. Then, the rules and heuristics that were applied are shown. Finally, the trace of the rules and heuristics as applied to comparing two nodes at a time are displayed.

To further depict our feedback capability, the node clustering inference of Figure 2 is used as an example. The system presents the following feedback for the lowest level of detail.

(1) Form Title: PRODUCT LIST

(2) Root node: node 0 has fields SUPPLIER and SUPPLIER NO because each has a field cardinality of 1.

(3) Dependent node: all the fields of a dependent node are positioned together and have the same cardinality.

Node 1 has fields PRODUCT NAME and PRODUCT CODE because each has a field cardinality of 5.

Node 2 has fields SIZE, DIMENSION, PRICE, QTY because each has a field cardinality of 8.

Node 3 has a field COLOR because it is the only field remaining and its field cardinality, 4, is different from that of node 2.

The feedback facility may be invoked after the examples of an instance are entered. It can be used by a form user to understand how inferences are made and by a database designer to understand the current state of the form design.

![](/api/attachments/E4SZVJMD/fulltext/images/a8346634940e59f601dc284db4072717395d89a69107962a5c005bec437c1191.jpg)

<table><tr><td>Form</td><td>Next</td><td>Back</td><td>First</td><td>Last</td><td></td><td></td></tr><tr><td>Instance</td><td>Next</td><td>Back</td><td>First</td><td>Last</td><td></td><td>New Instance</td></tr><tr><td>Row</td><td>Next</td><td>Back</td><td>First</td><td>Last</td><td>Edit Row</td><td>New Row</td></tr></table>

Figure 9. Blank Form

## 5. Prototype Implementation and Testing

A PROTOTYPE FORM DEFINITION SYSTEM WAS IMPLEMENTED on a Macintosh SE in Lightspeed Pascal [25]. The interface of the prototype was designed according to the guidelines reported by Foley and Sibert [14] and Schneiderman [21]. The standard features of the Macintosh environment such as pull-down menus, dialogue boxes, windows, and help messages greatly facilitated the interface design.

Figure 9 displays a blank form with the pull-down menus at the top of the screen. The form menu has the traditional filing functions related to forms: open a new form, select an existing form instance, save an instance, and quit. The Edit menu supports cutting and pasting of form instances. The Layout menu allows a user to define form fields and to enter examples after all fields are defined. It features several dialogue boxes for defining form fields. The Mode menu allows the user to select the expert or novice mode for defining requirements. Within the novice mode, the user can invoke a function from the EgGen (Example Generation) menu. The user can allow the system to generate additional examples or select previous examples using the history option. The Requirement menu displays the inferred results of the form hierarchy, keys, and dependencies. If the inference is incomplete, the system will ask the user for more examples. The Feedback menu provides general background about terminology and a trace of the inferencing process as described in section 4.3.

A preliminary study of the system was made using subjects from the Computing Services Division of the University of Massachusetts at Boston. The purpose of the study was to collect evidence about the usefulness and usability of the system, not to make rigorous empirical conclusions. We wanted to collect evidence about the types

1. Do you think the example generation facilities improve the ease of use? How to improve the design of these facilities? Other comments and/or suggestions.

2. Can you understand the information provided in the Help facilities and the Feedback menu? Please check the following topics.

<table><tr><td>Yes</td><td>No</td><td></td></tr><tr><td>—</td><td>—</td><td>field</td></tr><tr><td>—</td><td>—</td><td>field cardinality</td></tr><tr><td>—</td><td>—</td><td>node</td></tr><tr><td>—</td><td>—</td><td>node cardinality</td></tr><tr><td>—</td><td>—</td><td>hierarchy</td></tr><tr><td>—</td><td>—</td><td>local key</td></tr><tr><td>—</td><td>—</td><td>node key</td></tr><tr><td>—</td><td>—</td><td>key dependency</td></tr><tr><td>—</td><td>—</td><td>functional dependency</td></tr><tr><td>—</td><td>—</td><td>multivalued dependency</td></tr><tr><td>—</td><td>—</td><td>computation dependency</td></tr></table>

How to increase your understanding?

3. Can you state directly those requirements inferred by the Form Definition System without using it? Please check the following topics.

<table><tr><td>Yes</td><td>Maybe</td><td>No</td></tr><tr><td>—</td><td>—</td><td>— node</td></tr><tr><td>—</td><td>—</td><td>— hierarchy</td></tr><tr><td>—</td><td>—</td><td>— local key</td></tr><tr><td>—</td><td>—</td><td>— node key</td></tr><tr><td>—</td><td>—</td><td>— key dependency</td></tr><tr><td>—</td><td>—</td><td>— functional dependency</td></tr><tr><td>—</td><td>—</td><td>— multivalued dependency</td></tr><tr><td>—</td><td>—</td><td>— computation dependency</td></tr></table>

If your answer is maybe, please provide the reasons, e.g., additional information is required.

Figure 10. Questionnaire

of mistakes made, the ability of novice users to provide examples of requirements, and the completeness of collected requirements.

Four subjects were asked to perform two tasks. Since we were most interested in the performance of novice users, three of the subjects had little or no database knowledge. The fourth subject had some programming and database design experience. He provided feedback from an expert user's perspective. In the first task, the subjects provided additional examples for a common form. This allowed us to compare the performance across the four subjects easily. In the second task, the subjects designed their own form and provided example instances. The second task allows us to collect evidence of usability and usefulness on a more complex, but less controlled task.

The testing procedure consisted of the following steps. First, the subjects were given an overview of the prototype and were instructed to go through each menu and its help facility. Second, for the controlled task, the subjects were given a paragraph describing the Product List Form and the instance of Figure 2. This provided us with a common basis to detect the mistakes made and identify the problem areas of the design. This session also served as a training session. Third, the users were asked to design their own forms by using this prototype. The facilities used and mistakes made were observed and recorded. After these tasks, the subjects were requested to answer questions listed in Figure 10. The first two questions are for collecting evidence on usability, and the third question on usefulness.

The results of the study are summarized in Table 1. In general, we observed only minor errors with using the system and with the generated requirements. For the usability issue, all of the users initially made mistakes in differentiating between a new form type and a new form instance. However, none of the users repeated their mistakes. The results of the questionnaire indicated that the example generation facilities improved ease of use for the novice user, but not the expert. For the requirements issue, not all the users indicated that both SUPPLIER and SUPPLIER NO and PRODUCT NAME and CODE were keys. This seems more a matter of problem interpretation than a reflection on our approach. All of the users did not completely specify the dependencies. This is partly due to the limited length of time for the tasks and the fact that our prototype did not have a resume function.

We also observed that the prototype system was useful in educating users and collecting requirements. After one terminal session, they were able to understand some of the concepts explained in the help facilities and the explanatory feedback. Without using the prototype, they could only state directly the requirements such as node clusters and computation dependencies. In addition, one user commented that this prototype would be most useful if the data processing professional and the end user could use it together at the beginning. This is because the prototype provides something concrete for these two groups to discuss mutual needs and cooperation. Then, this prototype can be put into the hands of the end users.

## 6. Conclusions

WE DESCRIBED AN APPROACH TO DATABASE REQUIREMENTS COLLECTION based on the inference component of a form definition system. The form definition system supports character-oriented, hierarchically structured forms. In the expert mode, the form properties are stated directly. In the novice mode, the inference component infers the form properties and functional dependencies through examples. We described the design of the inference component for inferring the hierarchical structure of a form and functional dependencies between form fields. We also briefly described user interface aspects that provide informative feedback to the user and reduce the number of user keystrokes. A preliminary testing of a prototype Form Definition System was conducted to collect evidence on its usability and usefulness. The preliminary data suggested that the proposed approach is feasible, usable, and useful.

Table 1 Summary of Test Sessions

<table><tr><td>user no.</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>type</td><td>secretary</td><td>consultant</td><td>programmer</td><td>user manager</td></tr><tr><td>application</td><td>travel expenses</td><td>computer account</td><td>hardware list</td><td>software inventory</td></tr><tr><td>database knowledge</td><td>none</td><td>extensive</td><td>little</td><td>none</td></tr><tr><td>mistakes made</td><td>new form vs. new instance new form vs. field</td><td>new form vs. new instance</td><td>new form vs. new instance</td><td>new form vs. new instance</td></tr><tr><td colspan="5">used copy/paste and/or history functions</td></tr><tr><td></td><td>no</td><td>no</td><td>no</td><td>yes</td></tr><tr><td colspan="5">used commands aliases</td></tr><tr><td></td><td>no</td><td>no</td><td>no</td><td>no</td></tr><tr><td colspan="5">repeated the same mistakes</td></tr><tr><td></td><td>no</td><td>no</td><td>no</td><td>no</td></tr><tr><td colspan="5">deviations in the requirements of the controlled form</td></tr><tr><td>hierarchy</td><td>no</td><td>no</td><td>no</td><td>no</td></tr><tr><td>key</td><td>yes</td><td>no</td><td>no</td><td>yes</td></tr><tr><td>dependency</td><td>yes but incomplete specification</td><td>no but incomplete specification</td><td>yes but incomplete specification</td><td>yes but incomplete specification</td></tr><tr><td colspan="5">representativeness of requirements for the new forms</td></tr><tr><td>hierarchy</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td></tr><tr><td>key</td><td>yes</td><td>yes</td><td>yes</td><td>yes</td></tr><tr><td>dependency</td><td>yes but incomplete specification</td><td>yes and complete specification</td><td>yes and complete specification</td><td>yes but incomplete specification</td></tr></table>

The approach proposed here is an alternative method for the acquisition of database requirements. It is appropriate where forms are important uses of the database and end users are accustomed to form-based work. Our method can be combined with more traditional methods for requirements that are not based on forms. The primary limitation of our method is the quality and completeness of example sets provided by target users of forms. We have carefully designed our system so that the burden of generating examples is minimized. A secondary limitation is if unimportant forms are used, our approach will generate extra user views and dependencies that the underlying database need not support. However, this limitation is common to any approach to requirements definition where superfluous inputs generate superfluous outputs. With our approach, if a form is later determined as not necessary, the related user view and dependencies can be removed easily.

We thank Ron Lee and Bruce Porter for helpful discussions of our ideas.

## REFERENCES

1. Atre, S. Data Base: Structured Techniques for Design, Performance, and Management. New York: John Wiley & Sons, Inc., 1980.

2. Bernstein, P. Synthesizing third normal form relations from functional dependencies. ACM Transactions on Database Systems 1, 4 (December 1976), 247–298.

3. Borgida, A.; Mitchell, T.; and Williamson, T. Learning to live with exceptions to constraints in databases and knowledge bases. In On Knowledge Base Management Systems, Michael Brodie and John Mylopoulos, eds. Heidelberg: Springer-Verlag, 1986, 193–219.

database design. In Proc. Intl. Conf. Very Large Data Bases (VLDB), Stockholm, August 1985, 82–95.

5. Bradley, J. Introduction to Data Base Management in Business. CBS College Publishing, 1986.

6. Choobineh, J. A form-based expert systems approach for derivation of functional dependencies. Technical Report, Department of Business Analysis and Research, Texas A&M University, 1988.

7. Choobineh, J.; Mannino, M.; Nunamaker, J.; and Konsynski, B. An expert database design system based on analysis of forms. IEEE Trans. on Software Engineering, 14, 2 (February 1988), 242–253.

8. De Antonellis, V., and Demo, B. Requirements collection and analysis. In Methodology and Tools for Data Base Design, S. Ceri, ed. Amsterdam: North-Holland, 1983, 9–24.

9. De Marco, T. Structured Analysis and System Specification. Yourdon Press, 1979.

10. Dietterich, T., and Michalski, R. A comparative review of selected methods for learning from examples. In Machine Learning: An Artificial Intelligence Approach, R. S. Michalski, et al., eds. Tioga Publishing Company, 1983.

11. Eick, C. From natural language requirements to good database definition—a database design methodology. In Proc. Intl. Conf. Data Engineering, IEEE, Los Angeles, CA, April 1984, 324–331.

12. Eick, C., and Lockeman, P. Acquisition of terminological knowledge using database design techniques. In Proc. ACM SIGMOD Conf., Austin, TX, May 1985, 84–94.

13. Fagin, R., and Vardi, M. Armstrong databases for functional and inclusion dependencies. Information Processing Letters 16 (1983), 13–19.

14. Foley, J., and Sibert, J. How to design user-computer interfaces. Human Factors in Computing Systems, CHI'83, Tutorial 1, 1983.

15. Gerritsen, R. A preliminary system for the design of DBTG data structures. In Communications of the ACM, 18, 10 (October 1975), 551–557.

16. Lanka, S. Automatically inferring database schemas. In Proc. of the Ninth International Joint Conference on Artificial Intelligence, 1 (August 1985), 647–649.

17. Mannila, H., and Raiha, K. Design by example: an application of Armstrong relations. Journal of Computer and System Sciences 33, 2 (1986), 126–141.

18. Mannino, M.; Choobineh, J.; and Hwang, J. Acquisition and use of contextual knowledge in a form-driven database design methodology. In Proc. 5th Intl. Conf. Entity-Relationship Approach, November 1986, Dijon, France.

19. Martin, J. Applications Development Without Programmers. Prentice-Hall, Inc., 1982.

20. Ram, S., and Curran, S. The synthesis approach for relational database design: an expanded perspective. In Proc. 21st Intl. Hawaii Conf. System Sciences, Vol. II: Software Track, January 1988, 571–580.

21. Schneiderman, B. Designing the User Interface: Strategies for Effective Human-Computer Interaction. Addison-Wesley Publishing Company, 1987.

22. Shu, N.; Lum, V.; Wong, H.; and Chang, C. Specification of forms processing and business procedures for office automation. IEEE Trans. on Software Engineering SE-8, 5 (September 1982), 499–511.

23. Shu, N. Formal: a forms-oriented, visual-directed application development system. IEEE Computer, August 1985, 38–49.

24. Storey, V., and Goldstein, R. A methodology for creating user views in database design. ACM Trans. Database Systems 13, 3 (September 1988), 305–338.

25. Think Technologies. Lightspeed Pascal: User's Guide and Reference Manual, Version 1, 1st Edition, 1986, Lexington, MA.

26. Tseng, V. Inferring Database Requirements from Examples in Forms. Ph.D. Dissertation, Dept. of Management Science and Information Systems, The Univ. of Texas at Austin, May 1988.

27. Tseng, V., and Mannino, M. Inferring database requirements from examples in forms In Proc. 7th International Conference on Entity-Relationship Approach, November 1988, Rome, Italy, 251–265.

28. Ullman, J. Principles of Database Systems. Computer Science Press, Inc., 1982.

29. Wilson, M. A requirements and design aid for relational data bases. In Proc. IEEE Conf. Software Engineering, 1982, 283–293.

30. Yao, B.; Hevner, A.; Zhongzhi, S.; and Luo, D. FORMANAGER: an office forms management system. ACM Trans. on Office Information Systems, 2, 3 (July 1984), 235–262.
