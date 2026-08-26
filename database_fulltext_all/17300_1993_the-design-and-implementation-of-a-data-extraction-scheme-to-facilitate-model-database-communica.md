---
otero_id: 17300
otero_key: "9Y5W5VNX"
title: "The design and implementation of a data extraction scheme to facilitate model-database communication"
authors: "Leslie L. Miller; Sree Nilakanta"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90012-r"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Organizational decision support systems The design and implementation of a data extraction scheme to facilitate model–database communication \*

Leslie L. Miller

Iowa State University, Ames, IA, USA

Sree Nilakanta

Iowa State University, Ames, IA, USA

The concept of organizational decision support and the criteria for designing such support systems (ODSS) have recently received a great deal of attention. In spite of major differences among the decision processes at the organizational, group, and individual levels, the requirements for securing data from the corporate database in an ODSS still remains a significant issue. In addition, the computer and communication technologies that integrate the subsystems of knowledge, data, and models assume increased relevance in the ODSS. Indeed, the richness of problems of making the most of such technologies becomes even more important in the ODSS environment. In the present work, the issues of integrating models and databases through the use of a data extraction scheme are examined. In particular, certain aspects of the query generation algorithms that allow the user or model to view the database as a single relation are described. The generated query is then translated into TQUEL, resulting in a temporal query reflecting the historical nature of the corporate database.

Keywords: Organizational decision support systems, Relational databases, Query generation, Hypergraphs, Models

## 1. Introduction

Recent advances in information and telecommunication technologies have enabled organizations to assess the role of decision support systems at a more higher and complex level, namely at organizational decision making. Organizational decision support systems (ODSS) appear to be the result of a natural evolution starting with personalized decision support systems (DSS) and group decision support systems (GDSS). While no consensus exists among researchers, it is widely believed that an ODSS is far more than a simple scaling up of prior DSS concepts [26]. Watson [52], for example, defines ODSS to consist of computer and communication technologies designed to support decision making across functional as well as hierarchical layers of the organization.

![](/api/attachments/9Y5W5VNX/fulltext/images/4f7f96069ebdbc15d848f2d300f8d06ff335ded376e33531b38ebd301a67ccf2.jpg)

Leslie L. Miller is currently an Associate Professor of Computer Science at Iowa State University. He received his Ph.D. in Computer Science from the Southern Methodist University in 1980. His areas of interest include object oriented databases, database support for organizational decision support systems, database machines, database design, and microcomputer applications. He is currently the editor of Microcomputer Applications and a member of the executive board of

the International Society for Mini and Microcomputers.  
![](/api/attachments/9Y5W5VNX/fulltext/images/475f1cdc77c0eb743efa402c5fce04d7dbc054bc626a17467dac32fa49fd0e75.jpg)

Sree Nilakanta is an Assistant Professor of Management in the College of Business Administration at Iowa State University. He received his Ph.D. in Management Information Systems from the University of Houston in 1985. His research interests include application of database design tools, DSS-database integration, expert systems and adoption/diffusion of information technology. His publications have appeared in Management Science, Journal of Information and Soft ware Technology, Systems Management, and Computers and Industrial Engineering.

The socio-technical modus operandi of organizational decision making differ vastly from that of both group and individual decision making. Social conflict becomes the norm in this environment [26]. Further, equivocality and information richness of messages and cues encountered by the decision maker contribute significantly in the design and later use of the support systems leading to better organizational performance [10,11]. ODSS will have to deal with these constraints and opportunities to be effective.

Historically, computer-based information systems were implemented to record and report the transactions of the enterprise. Over time, as organizations have realized the potential of the transaction data, resources were allocated to manage and exploit it. This evolution to data management now makes it possible for organizations to support decision makers with such systems as personal decision support systems and work group support systems. Much evidence of this can be seen in recent literature on organizational information processing where it is now suggested that organizations consider that it is but a natural extension to adopt existing computer and communication technologies for support of their decision making $[24,25,40]$ .

In this paper, we examine a specific design and implementation of a small portion of the ODSS environment, namely the interface between decision models and corporate database. In the next section, we illustrate the role of technology in ODSS design.

## 1.1. Components of ODSS

Reviewing the current body of literature on organizational decision support systems, George [20] provides a synthesis of what an ODSS might be. His synthesis comprises three dimensions, namely the concept, architecture, and technology. At the conceptual level, the focus of ODSS is: (a) on tasks, activities, and decisions that affect several organizational units or corporate issues; (b) on its pervasiveness across the hierarchies and functions; and (c) on different technologies needed to achieve this integration. Architecturally, an ODSS is to provide access to shared models and data with varying emphasis on how and where these are used. A wide range of technologies including computer and communication technologies form the third and vital dimension.

King and Star [26] argued that organizations need and can cope with social conflict through the use of appropriate regulatory mechanisms and facilities such as due processes and boundary objects. For example, GDSS designs incorporating communication supports and knowledge base schemes have been used in the past to address the problems of negotiation and conflict [47]. Unlike group decision making, because organizational decisions span levels of hierarchies as well as boundaries, the design and implementation of an ODSS necessitate the use of several different mechanisms that are wider in scope. Examples would include knowledge and decision gathering mechanisms, communication facilities, information management facilities, etc. Watson [52], for instance, articulates the need for setting up a multitude of such facilities while King and Star [26] advocate somewhat similar sentiments when they describe the general nature of boundary objects. In short, what we have is a collection of computer and communication technologies capable of facilitating the implementation of an ODSS. An architecture of the ODSS is shown in fig. 1.1.

![](/api/attachments/9Y5W5VNX/fulltext/images/4d56a777ac61d11f86f64a2b8a1d4d9c06f016944bdbc7d138cf118126524b38.jpg)  
Fig. 1.1. The ODSS architecture.

In discussing how an ODSS is utilized, it may be appropriate to draw parallels to the use of a DSS by a decision maker. Note that the difference between DSS and ODSS is in the context of the decision and it is believed that much of the technical design aspects of ODSS (e.g., data and model management capabilities and the interfaces among the subsystems) will not be very different. We believe, however, that the classical framework of DSS advocated by Sprague and Carlson [45] may not capture the ODSS context completely. Our model is somewhat closer to the framework espoused by Holsapple and Whinston [23]. Our model incorporates the notion that there are subsystems of knowledge, data, and models that interact over a rich and varied telecommunication backbone [29]. Also, the information these subsystems maintain within may come from the private or public domain [1,42]. Further, as the scope of the system could cover all levels of hierarchies and spans of control, the sources of these information could be within or outside its organizational boundaries.

Ordinarily it is hoped that an ODSS makes full use of all three subsystems. But, as seen in practice and research relating to DSS, most often only one or two subsystems are actively employed at any one time. In spite of the work done on PLEXSYS $[28]$ integrating the subsystems is a goal which is yet to be achieved fully. Past research relating to DSS have either focused intensely on decision making or on certain aspects of DSS design namely the model and dialog subsystems $[2,5,6,27,32,33,38,43,50,51]$ . ODSS research on the other hand is still in its infancy but we feel some of the design features of DSS and GDSS can be easily adapted for ODSS.

1.2. Models in organizational decision support systems

When examining the use of models in ODSS, it is obvious that the DSS literature on models is useful in the development of ODSS. In order to design and implement effective decision support systems (DSS), not only are the developments of database and model components important but it is also necessary to incorporate adequate interfaces between them [7]. Some of these important interfaces are between user and models, user and data, and models and data. Further, the failure of computer-based models in organizational decision support may also be attributed to the lack of attention given to the design and use of data sources [46]. To overcome some of the inherent problems associated with the use of data, Sprague and Watson [46] suggested that there should exist mechanisms for extracting data from the corporate database along with a suitable user-system dialog component. A similar sentiment is expressed by Mylopoulos [39].

The user functions that must be supported by a model manager are problem identification, formulation, analysis, and interpretation $[17,53]$ . The intelligent agent technology advocated by Liu, Yun and Klein $[34]$ yields a reasoning interface between the user and the ODSS. Here, a user is assisted in the selection of appropriate models through a series of dialogues that are task dependent. The model may be built up from the primitive elements or could be retrieved from either a private or public collection of models. The knowledge base can also be utilized in the selection process.

A major assumption involved in the study of models is that of access to the database. Often, researchers as well as designers of ODSS (as well as designers of DSS) have taken for granted the availability of appropriate data. Many DSS have also been developed that utilized their own independent data sets. The use of an independent free standing database for DSS erodes away the notion of a corporate database that is accessible and sharable. In ODSS the data needs are more complex, but one expects the corporate database to play a critical role in providing data to the ODSS. Irrespective of the nature of the database (centralized or distributed), the existence of a corporate database is important for achieving a competitive edge. Designing an ODSS that relies on the corporate database for its data requires that the role played by data extraction and use be reconsidered. The successful implementation of a DSS (as well as an ODSS) entails the integration of the corporate database [4,12].

In recent years, much of the research in DSS has focused on the model management component. Since models represented procedural knowledge, most of these studies attempted to somehow capture the essence of the decision making process through such mechanisms as abstractions, automatic algorithm construction, extensible databases, etc $[3,14,15,16,30]$ . While these efforts often focused on the model building and maintenance aspects, the model-data interface concerns were more or less ignored. But, for an ODSS (or DSS) to effectively function, it is essential to have all components working synchronously. Conceptually, the need for integration was illustrated by Sprague and Watson $[46]$ . They cited the need for a data extraction scheme capable of allowing models to communicate directly with the corporate database. The retrieval procedure may be explicitly specified within the model or the model might invoke predetermined reports. Another method would be to direct retrieval statements to a general report generator that is independent of the data organization. Though the idea has been promulgated over a decade ago, very little has been done to implement and validate the mechanisms.

Recent advances in the database field give us an opportunity to empirically evaluate the validity of the notion suggested by Sprague and Watson [46] for the ODSS environment. The query generation mechanism discussed later allows us to have models direct requests for data to an interface module that communicates directly with the corporate database. An important aspect of the query generation is that the query may be created for any target database including temporal dbms. Many of the earlier attempts to integrate the database component within a DSS were restricted to the use of purely relational dbms. However, a number of models used in ODSS require historical data. When only relational operators are supported, the responsibility of providing the historical data is placed on the user. Without temporal support at the system level, the user must either provide access to archival files or the user's queries must support all of the required temporal operations. In the next section we examine the basic aspects of our approach to data extraction.

## 2. Data extraction

Our approach to the user interface is focused on the user interaction with the models. Concerns over use of the database have been minimized as much as possible. In our current design, we are only asking the user to contribute infor-

![](/api/attachments/9Y5W5VNX/fulltext/images/03c0e07ed197066301bf2520bc7394bba5ad5f5757a5959da2c0d95d060b301a.jpg)  
Fig. 2.1a. Data extraction in model-data interface.

$\mathbf{R}_1$ (S#, P#, Q) $\mathbf{R}_2$ (S#, C) $\mathbf{R}_3$ (C, S)

where S# = supplier number, P# = part number, Q = quantity, C = city located in, S = status of city

Fig. 2.1. Supplier-Parts database.

mation on the temporal constraints and/or other constraints that he/she wishes to impose on the data used by the model. The remainder of the dialog with the user is centered on the choice of model and the results the user expects to receive from the model.

Figure 2.1a illustrates the basic scheme of our inquiry, namely the interface between models and databases. The user interacts with the model and as a result the model management system generates an output set comprising a list of attributes, predicates for these attributes, and their temporal constraints. Output from the model management system is fed to the data extraction scheme which in turn produces the desired database query.

It has been our intention to have our data extraction component communicate directly with the models. To provide this simplification, we have developed a query generation scheme as part of our data extraction component. The scheme is based on the use of hypergraphs and uses aspects of the translation scheme proposed in [41]. First, we look at some basic concepts of hypergraphs and overview the hypergraph model used in our translation process.

## 2.1. Hypergraph model

The reader is assumed to be familiar with the basic concepts of relational database theory, namely functional dependencies and the operations of relational algebra. We define a database scheme $R=\{R_{1}, R_{2}, \ldots, R_{m}\}$ to be a set of subsets of N, where N is a set of attributes. A hypergraph is a couple $H=(N, E)$ , where N is a set of vertices and E is a set of hyperedges which are non-empty subsets of N. There is a natural correspondence between database schemes and hypergraphs.

Besides the natural correspondence between hypergraphs and database schemes, many of the hypergraph theoretic notions simplify problems such as generating join sequences. For example, the notion of a set of hyperedges being connected provides a basic property of a lossless join. Clearly, the same notion can be expressed in other ways, but by using hypergraphs we have an economy of expression in both our algorithms and discussion.

A hypergraph $H=(N,E)$ is said to be $\gamma$ -acyclic if it contains no $\gamma$ -cycle which is a sequence of the form $(E_{1},x_{1},E_{2},x_{2},\ldots,E_{k},x_{k},E_{k+1})$ , where:

(i) $x_{1}, x_{2}, \ldots, x_{k}$ are distinct vertices in $N$ ;

(ii) $E_{1}, E_{2}, \ldots, E_{k}$ are distinct hyperedges in $E$ and $E_{k+1} = E_{1}$ ;

(iii) $k\geq 3$

(iv) $x_{i}$ is in $E_{i} \cap E_{i+1}, 1 \leq i \leq k$ ;

(v) if $1 \leq i < k$ , then $x_{i}$ is in no $E_{j}$ except $E_{i}$ and $E_{i+1}$ .

The database scheme is $\gamma$ -acyclic exactly when the underlying hypergraph is $\gamma$ -acyclic.

Fagin [18] has defined two additional types of acyclicity for hypergraphs that are of interest: $\alpha$ -acyclic and $\beta$ -acyclic. Graham's algorithm [35,48] repeatedly applies the following two steps on the hypergraphs until neither can be applied:

(1) if $x$ is a vertex that appears in exactly one edge $E_{i}$ , then delete it from $E_{i}$ ;

(2) delete $E_{i}$ if there is an edge $E_{j}, j \neq i$ such that $E_{i} \subseteq E_{j}$ .

The algorithm succeeds if it terminates with an empty set; otherwise it fails. A hypergraph is $\alpha$ -acyclic if Graham's algorithm succeeds. A hypergraph is $\beta$ -acyclic if every arbitrary sub-hypergraph is $\alpha$ -acyclic.

Fagin [18] has shown that $\gamma$ -acyclic $\Rightarrow \beta$ -acyclic $\Rightarrow \alpha$ -acyclic, but none of the reverse implications hold. Each type of acyclicity provides desirable properties for the corresponding database scheme. In particular, Fagin has shown that any arbitrary connected set of relation schemes in a $\gamma$ -acyclic database scheme defines an embedded join dependency. Note that an embedded join dependency enforces the constraint that the relation defined by the dependency can be losslessly joined.

Fagin et al. [19] use the hypergraph to model the full join dependency which defines the universal relation (UR). For example, the well known supplier-parts database given in fig. 2.1 is defined by the dependency set $\{*[R_1, R_2, R_3], S\# \to C, C \to S, S\# P\# \to Q\}$ . The join dependency (jd) $*[R_1, R_2, R_3]$ can be represented by the hypergraph of fig. 2.2. Fagin et al. have shown that the semantics of any database can always be represented by such a full join dependency and a set of functional dependencies (fds). Ullman [48] in his survey of universal relation assumptions denotes this as the UR/JD assumption.

![](/api/attachments/9Y5W5VNX/fulltext/images/0379cd9e101612506926fa7bafe3cc6417fc0af5694463b233c1b01e0d4f8e05.jpg)  
Fig. 2.2. Hypergraph representation of the supplier-parts database.

Two additional concepts related to hypergraphs, namely, the hinge [21] and maximal objects [36] are formalized in the remainder of this section. If $H$ is a reduced connected hypergraph with the vertex set $N$ and the edge set $E$ , then $E'$ is a complete subset of $E$ if and only if $E' \subset E$ and for each $E_i$ in $E$ if $E_i \subseteq \text{attr}(E')$ (where $\text{attr}(E')$ represents the union of the edges in $E'$ ), then $E_i$ belongs to $E'$ . $E'$ is said to be a trivial subset of $E$ if $|E'| \leq 1$ or $E = E'$ .

Let $E'$ be a complete subset of $E$ and $E_1$ , $E_2 \in E - E'$ . Then we say $E_1$ and $E_2$ are connected with respect to $E'$ if and only if they have common vertices not belonging to $E'$ .

Let $E'$ be a non-trivial complete subset of $E$ and $\Psi_1, \Psi_2, \ldots, \Psi_p$ be connected components of $E - E'$ with respect to $E'$ . Then $E'$ has the bridge-property if and only if for every $i = 1, 2, \ldots, p$ there exists $E_i \in E'$ such that $(\text{attr}(E') \cap N_i) \subseteq E_i$ , where $N_i = \text{attr}(\Psi_i)$ . $E_i$ is called a separating edge of $E'$ corresponding to $\Psi_i$ . A non-trivial complete subset of $E'$ of $E$ with the bridge property is called a hinge of $H$ [21].

Another notion of interest is the maximal object. Fagin, Mendelzon and Ullman [19] define a universal relation (when it has meaning) as

$$
u = \left\{\langle a _ {1}, a _ {2}, \dots , a _ {n} \rangle \mid P _ {1} \cap P _ {2} \cap \dots \cap P _ {k} \right\},
$$

where each $P_{i}$ is a predicate taking some set of $a_{j}$ 's as arguments (some of which may be null). From this definition, if $P_{i}$ involves $a_{j1}, a_{j2}, \ldots, a_{ji}$ , then the set of attributes $R_{i} = \{A_{j1}, A_{j2}, \ldots, A_{ji}\}$ is an object [36]. Maier and Ullman [36] go on to define maximal objects as sets of objects. They also provide an algorithmic means of generating maximal objects based on the set of functional dependencies and multivalued dependencies that hold for the corporate database. The result is that within one of Maier and Ullman's maximal objects, the relation schemes (hyperedges) that are subsets of a maximal object represent relations that can be joined losslessly.

In the next section, the notion of hypergraph is used to generate join sequences.

## 3. Query generation

In order to simplify the model's view of the database, we assume that the ODSS uses a single relation database (i.e., the universal relation [19,49]). As a result, the data request from a model is simply a listing of the attributes needed in the problem analysis, the required conditions on these or other attributes in the universal relation scheme and the time interval to be considered. The latter two come primarily from the user's description of the problem.

There are two principal issues that have to be discussed to motivate our data extraction component. First, an appropriate join sequence is required to map the list of attributes requested by the model into the real world database design. Generation of such a join sequence combined with the necessary selection conditions are sufficient to generate the non-temporal aspects of the query. The second phase of translation process examines the generation of the temporal constraints for the target query.

## 3.1. Generating the join sequence

In addition to the source query hypergraph $(Q_{s})$ , the data extraction component requires information on the corporate database design. One can obtain the join sequence directly from the hypergraph representation of the database $(\mathcal{H}_{T})$ , but as in [41] we have chosen to operate on the complete intersection graph $(I_{R})$ for $H_{T}$ . Our

Hypergraph $(\mathfrak{H}_{\mathrm{T}})$

![](/api/attachments/9Y5W5VNX/fulltext/images/e9a85f1dab239b4d4766b2d2acdd07ce669d757045969d6572c7c5e0c90a73eb.jpg)  
Fig. 3.1. Sample target database design for the supplier parts database.

choice of the complete intersection graph representation of a hypergraph itself is simply based on ease of use. It is our feeling that edge labeled graphs are generally better understood than hypergraphs. In our opinion, such an advantage allows the development of more easily understood algorithms and examples.

It should be noted that edge labeled graphs (elgs) (which are a generalization of the complete intersection graphs) have been used in work on distributed databases to show what joins are available [8]. In [9], elgs are used to define a process to determine whether it is more economical to do the join directly than to use semijoins to reduce the communications costs. In such applications, the join sequence is fixed and the graph is simply used to optimize the movement of data. The relationship between the hypergraph and its complete intersection graph representation is given in fig. 3.1 for a supplier-parts database. To avoid confusion, we will use the term node when discussing sets of attributes for $I_{R}$ and the term vertex for single attributes in the hypergraph.

<table><tr><td>r</td><td>A</td><td>B</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>a1</td><td>b1</td><td>c1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>a2</td><td>b1</td><td>c2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td> $\pi_{AB}(r)$ </td><td>A</td><td>B</td><td> $\pi_{BC}(r)$ </td><td>B</td><td>C</td><td></td></tr><tr><td></td><td></td><td></td><td>a1</td><td>b1</td><td></td><td>b1</td><td>c1</td><td></td></tr><tr><td></td><td></td><td></td><td>a2</td><td>b1</td><td></td><td>b1</td><td>c2</td><td></td></tr><tr><td></td><td></td><td colspan="3"> $\pi_{AB}(r) * \pi_{BC}(r)$ </td><td>A</td><td>B</td><td>C</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>a1</td><td>b1</td><td>c1</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>a1</td><td>b1</td><td>c2</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>a2</td><td>b1</td><td>c1</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>a2</td><td>b1</td><td>c2</td><td></td></tr></table>

Fig. 3.2. A lossy join for the design $\{AB,BC\}$ when the data supported by the semantics is r.

The quality of the join sequence generated is an important consideration. Of particular concern is that the join sequence does not introduce extraneous tuples that are not supported by the underlying semantics. A join that introduces such tuples is called a lossy join (fig. 3.2), while one that does not be called a lossless join. To simplify our present discussion, we side step the issue by imposing the restriction that the target hypergraph is $\gamma$ -acyclic (basically no cycles). Fagin [18] has shown that the join of a set of relations is lossless when the relation's schemes are connected (in $I_R$ by edges with non-empty labels) and the underlying hypergraph is $\gamma$ -acyclic. Such a restriction can be easily removed by testing whether or not the join sequence defines a lossless join (as in [31]) and if not expanding the sequence to either a hinge [21] or a maximal object [36].

Our scheme uses a variation of the breadth-first search (BFS) to determine the join sequence. Our algorithm supplements BFS by including a label for each path in the search tree and a set called the adjustment set $(A)$ . The algorithm creates a search tree (we will call the tree an adjusted BFS tree [ABFS]) for each node in $I_{R}$ which contains an attribute of S (the set of attributes required by the model plus the attributes used in the conditions). The search tree labels are used to prune or delay the expansion of subtrees where the unused nodes that are adjacent to the current endpoint of the path do not contribute any new query attributes (from S) to the path label. Any nodes falling into this class are stored in the adjustment set $(A)$ with a pointer to the position where they could be added to the search tree.

The expansion continues until $S = \bigcup_{i=1}^{m} P_{i}$ , where $P_{i}$ represents a path label for each of the m paths. In the event that we can no longer expand the search tree and $S \neq \bigcup_{i=1}^{m} P_{i}$ , then we take nodes from A and restart the process. Examples 3.1 and 3.2 illustrate the user of the process for the database design and query given in fig. 3.1.

## Example 3.1.

Create the search tree for the node CS of the $I_{R}$ of fig. 3.1, where $S = \{S\#, S, M, P\#\}$ .

$$
\begin{array}{c} \text {CS} \{S \} \\ \{S \# P \# S \} S \# P \# Q S \cdot \Big / \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \\ S \# C \{S \# S \} \\ \Big / \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \\ S \# P \# D \# \{S \# P \# S \} \\ D \# M \{S \# P \# S M \} \end{array}
$$

Adjustment set $(A)$ (parent in parentheses) $\{S\# Y(S\# P\# QS)\}$ .

Notice to expand $S\#P\#QS$ with either $S\#Y$ or $S\#P\#D\#$ is of no value (i.e. we add no new S attributes to the path label) in this tree, but by saving $S\#P\#D\#$ in the adjustment set we are able to use it in the expansion of $S\#C$ .

## Example 3.2.

Create the search tree for the node $S\# P\# \mathrm{QS}$ of the $I_R$ given in fig. 3.1 where

$$
S = \left\{S \# P \# S M \right\},
$$

$$
\cdot S \# P \# Q S \{S \# P \# S \}.
$$

Adjustment set $(A)$

$$
\begin{array}{c} \{S \# Y (S \# P \# Q S), S \# P \# D \# (S \# P \# Q S), \\ C S (S \# P \# Q S), S \# C (S \# P \# Q S) \}. \end{array}
$$

The process stalls without adding any new nodes to the search tree since we do not have any nodes in A that can add new attributes and $D\#M$ cannot be reached. To continue, we choose an element from A and continue the process. We have

$$
\{S \# P \# S \} S \# Y \cdot \begin{array}{c} S \# P \# Q S \{S \# P \# S \} \\ \cdot \\ \cdot \\ S \# P \# D \# \{S \# P \# S \} \\ \Bigg | \\ D \# M \{S \# P \# S M \} \end{array}
$$

as the resulting tree.

From the examples, it is clear that the adjustment set plays two roles in the expansion of the ABFS tree. First, it is used to retain nodes where the desired expansion is simply a matter of the order in which the nodes are examined (Example 3.1). Second, it is used to restart the expansion of the ABFS tree when our pruning does not allow creation of a tree which includes all the query attributes (S). In [41], it is shown that this process may be required to generate the ABFS tree for a given root.

Once the ABFS tree is created, we need to be able to determine the join sequence defined by the tree. Our approach is to take the root and a set of paths connected to the root such that the union of path labels includes the attributes found in S. Based on this approach the set of ABFS trees and their assigned weights (number of joins) for the $I_{R}$ of fig. 3.1 are given in fig. 3.3. Note that a node like S#Y, that is only adjacent to nodes containing a superset of the S attributes found in S#Y, is assigned the weight MAX to remove it from consideration. The join sequence defined by one of the ABFS trees having the minimum weight is taken as the appropriate join sequence for the target design. As a result, the interface will join the relations $S\#P\#QS$ , $S\#P\#D\#$ and $D\#M$ in the example. The order of the joins is dependent on the physical characteristics of the relations and as such is left to the optimizer of the DBMS used.

![](/api/attachments/9Y5W5VNX/fulltext/images/a2c3caee4758716c3e253bdabeed8515eac405048d1f1eda9a6d234556aea1fb.jpg)  
Fig. 3.3. The ABFS trees and weights produced for the target design in fig. 3.4 and $S = \{S\#, P\#, S, M\}$ .

Once the join sequence has been determined, the generation of the QUEL portion of the query is straight forward. Our system uses a query template that generates a range statement for each relation used in the join. The attribute list in the retrieve statement is created from the list of attributes required by the model. The where condition is generated by appending the required join conditions onto the conditions passed to the data extraction module by the model. The following example provides a more detailed look at the process.

Example 3.3: Generation of a query for the supplier / parts database

Model supplied information

QUEL query generated

range of $a$ is $e4$

range of $b$ is $e5$

range of $c$ is $e6$

retrieve $a.S\# ,a.P\# ,c.M$

where $a.S > 10$ and $a.S\# = b.S\#$ and

c.D#.

The remaining issue is the generation of the temporal constraints. We examine the basic issues of handling temporal constraints in the next subsection.

## 3.2. Temporal constraints

Our approach for including temporal support is based on the assumption that the user is the only reliable supplier of temporal restrictions. It does not seem reasonable that the system can be used to determine the appropriate interval of time that the user wishes to analyze. Since the user must supply the temporal information as part of the problem specification, we start our discussion by looking at the approach used to collect temporal information in our interface. Our strategy for developing temporal constraints has been based on a top-down approach. We began by trying to isolate what we saw as the typical user needs. In addition, we sought to maintain our philosophy that the user interface be simple to use. The result is that we have chosen to limit our view of time in the dialog with user.

Snodgrass and Ahn [44] have defined the complete taxonomy of time to include valid time, transaction time and user defined time. Of these three, valid time which provides a history of the real world in terms of the database, seems to be the most useful to the general user trying to incorporate historical data into his/her study. Transaction time provides a history of the database, and as such appears to be less useful to the general user. User defined time is rather specialized and as a result does not seem useful in the majority of the applications we visualize.

Based on these assumptions, we have designed an interface that presents the user with a means of directly specifying valid time. For simplicity, we have chosen to base our discussion on the assumption that the user presents the interface with a time interval or a single point in time. Such an interval or point in time is called the user defined interval or time. This assumption is not restrictive and the interface design can easily be extended to allow other input values such as defining a starting point in combination with a time span in which to evaluate the query.

We have identified three types of temporal constraints:

(1) The user defined interval is completely contained in the tuple interval, where tuple interval refers to the valid time interval defined by a tuple in the corporate database;

(2) The tuple interval overlaps some portion of the user defined interval;

(3) The user defined interval is completely outside the tuple interval.

In addition for the user's convenience, we have added three special cases of the second option:

(4) The start of the tuple interval starts before the user defined time;

(5) The end of the tuple interval precedes the user defined time;

(6) The user defined time precedes the start of the tuple interval.

In our view, the set of six options give the average user sufficient control over the temporal constraints for most applications. However, to make our interface more appealing and to allow the user to incorporate the other two forms of time (transaction and user defined time) we have made it possible for users to apply more sophisticated temporal constraints. Such users can use the query generation portion of our interface in one of two ways. First they can enter their TQUEL [44] query directly, in which case the model is able to use the user query directly. As a second alternative the user can use an expanded form of the interface that allows the option of appending temporal constraints on to one of the six system generated constraints.

Such an approach provides the user with a comprehensive use of temporal constraints without complicating either the use or the design of the query generation portion of the interface. The system generated temporal constraints (options 1 through 6) require only a template constraint applied to each of the join relations (determined by the algorithm described in Section 3.1). For example, once the user has chosen option 1 it is only required that $t_1 > = t_2$ , $t_4 > = t_3$ , where $(t_1, t_4)$ is the tuple $(t)$ interval and $(t_2, t_3)$ is the user defined interval. To implement such a constraint in TQUEL we simply generate start of $t$ precedes $t_2$ and $t_3$ precedes end of $t$ for each tuple variable in the query and add it to the when clause portion of the query.

Similarly, when option 2 is chosen by the user, it can be handled by enforcing the condition $t_{3} > = t_{1}$ and $t_{4} > = t_{2}$ . The option only requires that start of t precedes $t_{3}$ and $t_{2}$ precedes end of t be added to the when clause portion of the query for each relation in the join sequence (fig. 3.4). The temporal constraints for the remaining options can be generated in a similar fashion.

Another approach has been described by De et al. [13]. They use a natural language interface for a DSS that incorporates the notion of temporal support. Their approach allows the user to view the corporate database as a component of the (O)DSS in a manner similar to our approach. Under such an interface, the (O)DSS views the corporate database as a single relation and there must be a translation mechanism such as the one proposed in this paper to generate the queries required to access the stored database.

```txt
Range of a is e1
Range of b is e2
Range of c is e3
Retrieve (a.Part#, c.status)
where a.Qty > 100
and a.supplier#=b.supplier#
and b.city=c.city
when a overlap b
and b overlap c
and start of a precedes Dec 31 1989
and Jan 1 1984 precedes end of a
and start of b precedes Dec 31 1989
and Jan 1 1984 precedes end of b
and start of c precedes Dec 31 1989
and Jan 1 1984 precedes end of c
```  
Fig. 3.4. TQUEL query for option two - overlap some portion of the interval.

The query generation portion of our interface has an efficient implementation. The algorithm described in Section 3.1 has been shown to be polynomial $(\mathrm{O}(n^{3}))$ , where n is the number of nodes in the complete intersection graph for the database design [41]. The temporal extension proposed here only has an $\mathrm{O}(n)$ time requirement leaving the overall process with an $\mathrm{O}(n^{3})$ time requirement.

## 4. A comprehensive example

Boone Cannery has been actively using electronic data interchange (EDI) during the last few years for doing business with hundreds of its customers. Recently, they have added several trading partners from the transportation industry. These partners represent a number of different modes of transport (e.g., rail, road, water, etc.). With the escalation of gasoline prices, Boone Cannery is forced to pursue different alternatives of its current use of own truck fleet. EDI has made it possible for the Firm to avail more time and information to allow it to do freight consolidation, compare carriers, consider alternate modes of transportation, negotiate and do other tasks.

Several issues are relevant here. At the organizational level, the decision affects a number of people at various functional and hierarchical levels. Changing modes of transport may force packaging changes or may cause shifts in 'power' balances among the various organizational units. Negotiating with outside carriers may now require the involvement of one or more organizational units who have to schedule these activities into their routine. Also, organizational norms and policies need to be enforced or changed. At the departmental or functional unit level, inter-unit communication becomes a necessity. Communication infrastructures and protocols must be established so that conflicts are reduced. Because of self preservation tendencies organizational units may suboptimize or act in discordance with the overall objective of the firm. At the individual decision maker level, the user needs access to information on prices, freight capacity, model features, etc. These data are processed with respect to a decision model of choice to generate plausible alternatives. The models could be analytic or heuristic and they may in turn invoke a class or subclass of models and data. The data requirements for a model may be satisfied by a corporate database. One such case is illustrated here for the Boone Cannery where the decision involved is to analyze the feasibility of outsourcing its freight handling and moving.

Table 1

<table><tr><td>Boone Cannery database (shipping portion)</td></tr><tr><td>CANNERY (cannery#, cannery_name, address, available_supply)</td></tr><tr><td>WAREHOUSE (warehouse#, name, address, storage_capacity, current_storage)</td></tr><tr><td>JUNCTION (junction#, name, address)</td></tr><tr><td>TRUCK_ROUTE (trucker#, route#, cost_of_route, exp_delivery_time)</td></tr><tr><td>ROUTE (source, destination, route#)</td></tr><tr><td>TRUCKER (trucker#, name, address, telephone)</td></tr></table>

For example, one of the building blocks in the trucking decision is the expected cost of hiring sufficient carriers to replace Boone Cannery's trucking fleet. Since the transportation division has routinely used independent truckers to back up its own fleet, the necessary data are available in the corporate database to estimate the cost. The shipping portion of the Boone Cannery corporate database is shown in table 1.

We start the discussion by looking at the requirements of the cannery's transportation division. Boone Cannery has two canneries and three warehouses located in several sites throughout the midwestern united states. In addition, officials have designated three sites known as junctions to allow shipments to be transferred from one truck to another. The junctions will prove to be quite useful if the decision to drop Boone Cannery's own fleet is adopted, since no single carrier serves the entire area covered by the canneries and the warehouses. The problem given here is a minor modification of the translation of the transshipment problem into a transportation problem given in [22, pp. 146–151].

Since extraction of data from the corporate database is the focus of this presentation, we will assume that the user chooses the required model and enters the appropriate temporal restrictions as described in Section 3.2. For the sake of discussion, we assume that the user interval is defined by current time. To provide a more interesting picture of our approach to data extraction, we assume that the user of the ODSS has requested two types of information: (1) The cost of hiring all of the carriers; and (2) a list of the carriers chosen for the various routes.

The model chosen by the user must generate the necessary information to set up the equations. In our example, the model must start by determining the transportation cost for each route. The task requires two steps. First, the necessary data must be obtained from the corporate database. In Boone Cannery database, this is accomplished by the model generating and passing the following universal query to the data extraction component.

retrieve source, destination, route#, cost-of-route when t overlaps current-time.

(1)

The expanded format of the query produced by our data extraction component is shown in fig. 4.1. The expanded query reflects the stored database's design and is the one that must actually be executed against the stored database.

The result of the execution of the query is that the model has the source, destination and cost for each route that can be used. The relation may still have multiple truckers that serve a particular range of a is CANNERY
retrieve cannery#, available\_supply
when a overlaps current\_time

Fig. 4.2. Expanded form of query (2).

range of b is WAREHOUSE
retrieve warehouse#, storage\_capacity, current\_storage when b overlaps current\_time

Fig. 4.3. Expanded form of query (3).

route and the ODSS model software must choose the cheapest carrier for each route (if the decision is based solely on cost). In the Boone Cannery database, it is possible to use a slightly more complex decision process by requiring the routes to be minimized by the time required and by cost only when there are ties. A sample table of data resulting from decision process chosen by the user is given in table 2. We have chosen to show the cost information in a more compact form as opposed to simply giving the resulting relation for the readers' convenience.

For use in providing the final list of carriers, the ODSS software produces a temporary relation Temp 1 (route#, trucker#) that relates the trucker# of the carrier chosen for each route.

To fill out the remainder of the information required for setting up the equations for the transportation problem, the ODSS passes the following two universal queries to the data extraction component:

retrieve cannery#, available\_supply

when $t$ overlaps current\_time,

(2)

range of a is TEMP1
range of b is ROUTE
range of c is TRUCKER
retrieve source, destination, a.trucker#, c.name, c.address
where a.route# = b.route# and a.trucker# = c.trucker#
when a overlaps current\_time and
    b overlaps current\_time and
    c overlaps current\_time

Fig. 4.4. Expanded form of query (4).

and

retrieve warehouse#, storage\_capacity,

current\_storage

(3)

when t overlaps current\_time.

The expanded form of the queries (2) and (3) reflecting the stored databases are shown in figs. 4.2 and 4.3, respectively. A sample result of the two expanded queries is shown in table 3.

With the information in hand, the ODSS software can setup the transportation equations and solve the problem. The cost of hiring the carriers can then be determined from the objective function directly. The problem of providing the list of information about the carriers requires going back to the database. The ODSS software simply passes the following universal query to the data extraction component.

retrieve source, destination, trucker#,

truckername, trucker\_address

(4)

when $t$ overlaps current\_time

The expanded form of the query is shown in Figure 4.4. Notice that the data extraction unit uses the temporary relation (Temp 1) when translating the universal query. The nature of the ODSS decision process must be able to continually incorporate new information into the process in order to keep up with the manner in which organizations make decisions.

Table 2  
Sample result of the first stage

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">CANNERY</td><td colspan="3">JUNCTION</td><td colspan="3">WAREHOUSE</td></tr><tr><td>1</td><td>2</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td rowspan="2">CANNERY</td><td>1</td><td>-</td><td>150</td><td>840</td><td>360</td><td>610</td><td>...</td><td>400</td><td>123</td></tr><tr><td>2</td><td>150</td><td>-</td><td>...</td><td>950</td><td>410</td><td>310</td><td>510</td><td>346</td></tr><tr><td rowspan="3">JUNCTION</td><td>1</td><td>840</td><td>...</td><td>-</td><td>260</td><td>111</td><td>190</td><td>510</td><td>600</td></tr><tr><td>2</td><td>360</td><td>950</td><td>260</td><td>-</td><td>380</td><td>...</td><td>450</td><td>430</td></tr><tr><td>3</td><td>610</td><td>410</td><td>411</td><td>380</td><td>-</td><td>360</td><td>195</td><td>512</td></tr><tr><td rowspan="3">WAREHOUSE</td><td>1</td><td>...</td><td>310</td><td>190</td><td>...</td><td>360</td><td>-</td><td>511</td><td>460</td></tr><tr><td>2</td><td>400</td><td>510</td><td>510</td><td>450</td><td>195</td><td>511</td><td>-</td><td>390</td></tr><tr><td>3</td><td>123</td><td>346</td><td>600</td><td>430</td><td>512</td><td>460</td><td>390</td><td>-</td></tr></table>

Sample Cannery production and warehouse allocation for the example

<table><tr><td>Cannery</td><td>Production</td><td>Warehouse</td><td>Allocation</td></tr><tr><td>1</td><td>150</td><td>1</td><td>75</td></tr><tr><td>2</td><td>200</td><td>2</td><td>130</td></tr><tr><td></td><td></td><td>3</td><td>145</td></tr></table>

## 5. Conclusion

The design of the data extraction portion of a user interface for an ODSS has been presented. The design has been developed using a top-down approach. We started our design process by determining what we felt would constitute typical data requests. The result is a model interface that allows even a user possessing little or no knowledge of the logical database design can generate sophisticated data requests for use within the ODSS environment. For example, the user could interact with the ODSS using an interface like the natural language model proposed by De et al. [13]. Such an approach can then view the corporate database as a single relation and use the proposed data extraction algorithm to generate the required queries against the stored database.

Currently, we are in the process of implementing the portion of the model interface described in this paper. Our current effort is a preprocessor to the INGRES dbms that converts a universal relation query into an appropriate QUEL query. The preprocessor is written in C and it generates an EQUEL program that is then executed against the INGRES database. In its current format, it generates the join sequence and uses the technique given in $[37]$ to test whether or not the resulting join sequence is lossless. We are now working on extensions that allow us to expand sub-hypergraphs when the test for losslessness fails for $\gamma$ -cyclic hypergraphs. In addition, we have developed software that allows the generation of temporal constraints. Our goal is to incorporate the two pieces of software to form the data extraction component described in this paper. Based on what we have learned during this implementation phase, we expect to develop an expanded user interface based on the ORACLE database management system. In addition, we are looking at the IBM AS/400 database facility as another means of developing a testbed for our project.

## References

[1] D.A. Adams and D.P. Hale, GMMS: Global Model Management System A Conceptual Design Framework for Model Management Systems for Distributed Decision Support Systems. Proceedings of the Twentysecond Hawaiian International Conference on System Sciences, IEEE (1988).

[2] L.M. Applegate, B.R. Konsynski and J.F. Nunnamaker. Model Management Systems: Design for Decision Support. Decision Support Systems 2, 1, 81–91 (1986).

[3] R. Blanning, A Relational Framework for Model Management in Decision Support Systems. DSS-82 Transactions, 16–28 (1982).

[4] R.W. Blanning, Model-based and Data-based Planning Systems. OMEGA 9, 2, 163–168 (1981).

[5] R.W. Blanning, Conversing with Management Information Systems in Natural Language. Communications of the ACM 27, 3, 201–207 (1984).

[6] R.W. Blanning, An Entity-Relationship Approach to Model Management. Decision Support Systems 2, 1, 167–172 (1986).

[7] R.H. Bonczek, C.W. Holsapple and A.B. Whinston. Future Directions for Developing Decision Support Systems. Decision Sciences 11, 616–631 (1980).

[8] S. Ceri and G. Pelagatti. Distributed Data bases: Principles and Systems (McGraw-Hill, 1984).

[9] M.-S. Chen and P.S. Yu. Using Join Operations as Reducers in Distributed Query Processing. Proceedings of the Symposium on Databases in Parallel and Distributed Systems, 116–123 (1990).

[10] R.L. Daft, and R.H. Lengel. Information Richness: A New Approach to Managerial Information Processing and Organization Design. In Research in Organizational Behaviour. Staw and Cummings Ed. JAI Press., Greenwich, CT. (1984).

[11] R.L. Daft, R.H. Lengel and L.K. Trevino. Message Equivocality, Media Selection and Manager Performance: Implications for Information Systems. MIS Quarterly 11, 3, 355–366 (1987).

[12] P. De and A. Sen. Logical Database Design in Decision Support Systems. Journal of Systems Management. 32, 28–33 (1981).

[13] S. De, S. Pan and A. Whinston. Temporal Semantics and Natural Language Processing in a Decision Support System. Information Systems 12, 1, 29–47 (1987).

[14] D.R. Dolk, Model Management and Structured Modeling: The Role of an Information Resource Dictionary System. Communication of the ACM 31, 6 (1988).

[15] D.R. Dolk and B.R. Konsynski. Knowledge Representation for Model Management Systems. IEEE Transactions on Software Engineering SE-10, 6 619–628 (1984).

[16] J.J. Elam, J.C. Henderson and L.W. Miller. Model Management Systems: An Approach to Decision Support in Complex Organization. Proceedings of the First International Conference on Information Systems, 98–110 (1980).

[17] J.J. Elam and B.R. Konsynski Using Artificial Intelligence Techniques to Enhance the Capabilities of Model Management Systems, Decision Sciences 18, 3, 487–502 (1987).

[18] R. Fagin, Degrees of Acyclicity for Hypergraphs and Relational Database Schemes, Journal of ACM 30, 514–550 (1983).

[19] R. Fagin, A.O. Mendelzon and J.D. Ullman. A Simplified Universal Relation Assumption and Its Properties, ACM Transactions on Database Systems 7, 343–360 (1982).

[20] J.F. George, The Conceptualization and Development of Organizational Decision Support Systems, Proceedings of the Twenty-fourth Annual Hawaii International Conference on System Sciences, IEEE Computer Society Press, 57–64 (1991).

[21] M. Gyssens and A. Paredaens. A Decomposition Methodology for Cyclic Databases, Advances in Database Theory, Gallaire, Minker and Nicolas ed. (1984).

[22] F.S. Hillier and G.J. Lieberman, Introduction to Operations Research, Holden-Day, Inc. San Francisco (1980).

[23] C.W. Holsapple and A.B. Whinston, The information jungle: a quasi-novel approach to managing corporate knowledge (Dow Jones-Irwin. Homewood, Ill, 1988).

[24] G.P. Huber, Organizational Information Systems: Determinants of their Performance and Perception, Management Science 28, 2, 138–155 (1982).

[25] G.P. Huber and R.R. McDaniel Jr. Exploiting Information Technologies to Design More Effective Organizations, In Managers, Micros and Mainframes. Jarke Ed. (Wiley, New York, 1986).

[26] J.L. King and S.L. Star. Conceptual Foundations for the Development of Organizational Decision Support Systems Proceedings of the Twentythird Hawaiian International Conference on System Sciences, IEEE, 143–151 (1990).

[27] G. Klein, Developing Model Strings for Model Management, Journal of Management Information Systems 3, 2, 94–110 (1986).

[28] B.R. Konsynski, J.E. Kottemann, J.F. Nunamaker and J.W. Stott. PLEXSYS-84: An Integrated Development Environment for Information Systems, Journal of Management Information Systems 1, 3, 64–104 (1984).

[29] R.M. Lee, A.M. McCosh and P. Migliarise, eds. Organizational Decision Support Systems (1988).

[30] M.L. Lenard, Representing Models as Data, Journal of Management Information Systems 2, 4, 36–48 (1986).

[31] J. Leuchner, L.L. Miller and G. Slutzki. A Polynomial Time Algorithm for Testing Implications of a Join Dependency and Embodied Functional Dependencies, Proceedings of the SIGMOD, 218–224 (1988).

[32] T.P. Liang, User Interface Design for Decision Support Systems, Information & Management 12, 4, 181–193 (1987).

[33] T.P. Liang and C.V. Jones, Meta-Design Considerations in Developing Model Management Systems. Decision Sciences. 19, 1, 72–92 (1988).

[34] J.I.C. Liu, D.Y.Y. Yun and G. Klein, An Agent for Intelligent Model Management, Journal of Management Information Systems 7, 1, 101–122 (Summer 1990).

[35] D. Maier, The Theory of Relational Databases. Computer Science Press (Rockville, Maryland, 1983).

[36] D. Maier and J.D. Ullman, Maximal Objects and the Semantics of Universal Relation databases, ACM Transactions on Database Systems 8, 1–14 (1983).

[37] L. Miller, J. Leuchner, S. Kothari and K. Liu, Testing Arbitrary Subhypergraphs for the Lossless Join Property, Information Sciences 51, 95–110 (1990).

[38] R.P. Minch, Logic Programming as a Paradigm for Financial Modeling, MIS Quarterly 13, 1, 65–84 (1989).

[39] Mylopoulos, Expert Systems and Databases. In Expert Systems: Integration With Databases and Real\_time Systems, The 34th IEEE Video Conferences Seminars via Satellite, IEEE (March 28, 1990).

[40] C.I. O'Reilly, The Use of Information in Organizational Decision Making: A Model and Some Propositions, In Research in Organizational Behaviour, Cummings and Staw Ed. JAI Press., 103–139 (Greenwich, CT., 1983).

[41] O.M. Owrang and L.L. Miller, Query Translation Based on the Hypergraph Model, The Computer Journal 31, 2, 155–164 (1988).

[42] M. Pagani and A. Belluci, An Organizational System for Telletra's Top Management, In Organizational Decision Support Systems. Lee, McCosh and Migliarese Ed., 3–13 (North-Holland., Amsterdam., 1988).

[43] L.G. Sanders and J.F. Courtney, A Field Study of Organizational Factors influencing DSS Success, MIS Quarterly 9, 1, 77–93 (1985).

[44] R. Snodgrass and I. Ahn, A Taxonomy of Time in Database, Proceedings of the SIGMOD, 236–246 (1985).

[45] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, 1982).

[46] R.H. Sprague and H.J. Watson, A Decision Support System for Banks, OMEGA 4, 657–671 (1976).

[47] M.R. Tanniru and H.K. Jain, Knowledge-Based GDSS to Support Reciprocally Interdependent Decisions, Decision Support Systems 5, 287–301 (1989).

[48] J.D. Ullman, Principles of Database Systems, Computer Science Press (Rockville, Maryland, 1982).

[49] J.D. Ullman, The Universal Relation Strikes Back, Proceedings of the ACM Symposium on the Principles of Database Systems, 10–22 (1982).

[50] H.J. Watson and H.H. Carr, Organizing for Decision Support System Support: The End-user Alternative, Journal of Management Informatin Systems 4, 1, 83–95 (1987).

[51] H.J. Watson, A. Lipp, P.Z. Jackson, A. Dahmani and W.B. Fredenberger, Organizational Support for Decision Support Systems, Journal of Management Information Systems 5, 4, 87–110 (1989).

[52] R.T. Watson, A Design for an Infrastructure to Support Organizational Decision-Making, Proceedings of the Twentythird Hawaiian International Conference on System Sciences, 111–119 (1990).

[53] E.S. Weber and B.R. Konsynski, Problem Management: Neglected Elements in Decision Support Systems, Journal of Management Information Systems 4, 3, 64–81 (Winter 1987/88).
