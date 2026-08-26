---
otero_id: 26661
otero_key: "R9SUQWV8"
title: "Model Integration Using Metagraphs"
authors: "Amit Basu; Robert W. Blanning"
year: "1994"
journal: "Information Systems Research"
doi: "10.1287/isre.5.3.195"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.255.6.125] On: 18 September 2016, At: 03:11 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## H4R

## Information Systems Research

![](/api/attachments/R9SUQWV8/fulltext/images/00cdeb853bbdc4384442700c835b32bf37ad2f64732a7eff1f97c488c1ef7f8c.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Model Integration Using Metagraphs

Amit Basu, Robert W. Blanning,

## To cite this article:

Amit Basu, Robert W. Blanning, (1994) Model Integration Using Metagraphs. Information Systems Research 5(3):195-218. http://dx.doi.org/10.1287/isre.5.3.195

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1994 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/R9SUQWV8/fulltext/images/22d62a0b097b5b9a40e5db0fd5411d1656797bd5f0417c973c18623df60b7507.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Model Integration Using Metagraphs

Amit Basu

Owen Graduate School of Management

Vanderbilt University

Robert W. Blanning

Nashville, Tennessee 37203

Owen Graduate School of Management

Vanderbilt University

Nashville, Tennessee 37203

The availability of a large and diverse collection of stored modules such as data relations and decision models is a desirable feature in a decision support system (DSS). However, it is usually infeasible to design a DSS in which every problem instance can be solved using a single module. Instead, it may be necessary to combine several stored modules into an integrated model that is sufficient to solve the given problem. We show that modules such as data files and decision models in a DSS can be usefully represented by a metagraph. a graph-theoretic construct that captures relationships between pairs of sets of elements. In addition to the visualization benefits that graphical representation offers, we show that many useful questions faced by the designers and users of DSS can be addressed by exploiting analytical properties of metagraphs. In particular, we show that the process of model integration can be significantly facilitated by exploiting certain connectivity properties in metagraphs.

Graph theory—Model management—Modeling—Decision support systems

## 1. Introduction

n important purpose of a decision support system (DSS) is to help a decision maker to access and utilize information resources such as stored data and decision models (note that we use the term “model" in this paper to refer to a relationship between a set of domain variables, such as sales, pressure, weight, rather than an algorithmic procedure such as the simplex algorithm or a general-purpose computational model such as the m/g/1 queuing model). In this regard, the sophistication and effectiveness of a DSS is determined largely by the level of support it provides for various data management and model management functions. Since DSS are usually applied to ill-structured problems, it is generally not known at the start of the decision support process which data and model resources will be needed and how they will be utilized. Thus, we can view a DSS as a set of modules, each of which is a data relation or a decision model, along with procedures for accessing and integrating these modules to provide decision support for a specific problem instance.

Although in some cases an individual module such as a stored model or data relation is sufficient to formulate a model for a problem, in general, multiple modules may have to be used. An integrated model is a collection of modules, each of which is a stored model or a data relation, that is formed in response to a user query. Model integration is the process of selecting the specific modules that make up the integrated model, and determining how the different modules interact.

The complexity of the model integration process is due to three major factors. First, in a large DSS with many modules, the search for a candidate integrated model (i.e., one in which all the component modules can be executed using only the given inputs, to obtain the desired outputs) can be a combinatoric problem of significant complexity. Second, in such a system, it is likely that a specific set of desired outputs could be computed using several alternative integrated models. Thus, it may also be necessary to support the process of choosing among multiple integrated models for a given problem instance. The third problem is that choosing among alternative integrated models requires the consideration of a variety of factors, such as cost, reliability, generalizability, scope and ease of use, many of which are qualitative and subjective. In fact, different integrated models will often yield different values of the outputs, since they may be based on different assumptions.

In this paper, we will restrict our attention to the impact of input/output dependencies between modules upon the construction of integrated models. The purpose of the paper is to present a graph-based approach that exploits the structural and analytical properties of a construct called a metagraph to address some important questions in model integration. These include the following:

## 1. Directed search for integrated models

(a) Backward search: given specific desired outputs (e.g., profit, price), what collection of modules comprises a candidate integrated model?

(b) Forward search: given specific inputs (e.g. costs, labor rates), what can I compute from this, using the available modules?

2. Models for given sets of inputs and outputs

(a) Given specific information, and a desired set of outputs, what integrated model can produce these outputs using the available information?

(b) As above, but with the specific requirement that one or more specific inputs must be used in the computations.

(c) As in (a) above, but excluding one or more specific modules (for instance, if these modules are known to be unreliable, inaccurate, or expensive).

3. Additional benefits of metagraphs in model integration

(a) If a specific module is removed, can all the desired outputs still be computed?

(b) If there are multiple integrated models that can be used to compute a set of variables $X _ { 2 }$ given values of a set of variables $X _ { 1 } ,$ , are there any modules that must be used, regardless of which integrated model is selected?

(c) Given an integrated model for a specific set of desired outputs, are there additional outputs that are also produced, and if so, what are they?

This paper is organized in five sections. In §2 we review some of the existing approaches to graph based modeling in DSS. In §3, we define metagraphs, contrast them with graphs and hypergraphs, and define paths and metapaths in metagraphs In Section 4 we show how the structural and analytical properties of metagraphs can be used to answer many of the questions in model integration posed above. Finally, §5 outlines directions for future research.

## 2. Approaches to Model Integration

Early research on model management emphasized the integration of models as an essential function of a model management system (Sprague and Watson 1975. Will 1975, Bonczek et al. 1976). Three approaches have been suggested for doing this. One is a relational approach in which stored models are viewed as virtual relations whose tuples do not exist in stored form but are computed on demand, and model integration is accomplished by performing joins across the virtual relations (Blanning 1985). The second is a graph-based approach in which stored models are viewed either as nodes or arcs in a graph (Greenberg and Maybee 1981, Liang 1988, Muhanna and Pick 1988). The third approach is to view stored models as components of a knowledge base and model integration as inference (Bonczek et al. 1981, Dutta and Basu 1984, Binbasioglu and Jarke 1986, Ma et al. 1989, Krishnan 1991, Kottemann and Dolk 1992, Banerjee and Basu 1992). While it is generally accepted that full automation of the model integration process is unrealistic, these research efforts have demonstrated that the integration process can be facilitated by exploiting structural and contextual information about DSS modules and intelligently linking them to relevant problem characteristics.

Although these three approaches appear quite different, there are substantial similarities. The relational approach to model management, like the relational approach to data management, is a user view of information modules in which the integration mechanism is hidden from the user. The graphical approach provides a lower-level approach in which the linking of modules is made explicit and is controlled by the user. The knowledge-based approach is an intermediate in which the network of modules is presented to the user (e.g., in the form of rules or frames), but much of the integration is accomplished by an inference engine under the control of the user, In the remainder of this section, we will focus on the graphical approach.

## 2.1. Visualization and Analysis

There are two principal ways in which graphical methods are used in model integration. The first is as a visual tool, where the graph construct is used primarily to help the user understand the structure of a system. Examples of this include functional dependency diagrams (Date 1990), entity-relationship diagrams (Chen 1976). data flow diagrams (Senn 1989) and higraphs (Harel 1988). The first three ap proaches are used almost exclusively for visualization. On the other hand, higraphs have a formal specification that does permit analysis. In a higraph, modules are represented as "blobs," which may contain other modules (called "subblobs"), and the higraph is a hierarchical arrangement of blobs, along with a set of edges connecting some of the blobs. Since higraphs and metagraphs are similar in some ways, we discuss them further in §3.5.

The second use of graphical methods, as suggested above, is analytical. The purpose is to derive interesting properties of a graphical structure and to apply these properties in the model integration process. Examples are found in the TIMMS system developed by Liang (1988) and the SYMMS system developed by Muhanna and Pick (1988, 1993) and further refined by Muhanna (1994). Liang's approach is based on AND/OR graphs, in which AND relationships describe multiple required inputs to a module and OR relationships represent alternative modules, any one of which will produce a required result (e.g., alternative forecasting techniques). It is assumed that a graph describing relationships among modules is acyclic (e.g., if the output of one module is an input to a second module, then the output of the second module cannot be an input to the first module). Liang presents a heuristic for selecting modules to produce a desired output.

The Muhanna/Pick approach is similar, but with one major difference—there is a hierarchical relationship among modules, similar to the blob/subblob structure of higraphs. However, the hierarchical arrangement is intended to organize models based on model (or algorithm) type—for instance, models that can be solved as linear programs. Thus, the selection of certain modules also entails selection of certain components, and the purpose of this approach is to integrate both the modules and their components into appropriate models.

The two approaches described above, visual and analytical, are sometimes combined in a single software tool. An example is FW/SM (Geoffrion 1991), which implements structured modeling (Geoffrion 1987). Structured modeling is an approach to model construction that is particularly suited to mathematical progràmming models. It provides a visual/intuitive framework as well as a software development environment for describing the relationships among real world entities being modeled (e.g., factories and warehouses), the components of the model describing them (e.g., objectives and constraints), and supporting data files (e.g., cost and capacity data). The relationship among these constituents is assumed to be acyclic.

A related area in computer science is that of dataflow architectures (Dennis 1980) and languages (Ackermann 1982). (These and other papers are collected in Thakkar (1987).) In dataflow systems, as opposed to control flow systems, instructions with specified inputs and outputs (e.g., X = Y + Z) await the availability of their inputs and execute, often in parallel, as the inputs become available. This is efficient for performing computations that form a network of simple calculations, but is less efficient for handling data structures. Although graphical structures have been developed for representing dataflow computations (Davis and Keller 1982), they are based on directed graphs in which the instructions are nodes and the relationships between them are edges. Unfortunately, as applied to model integration, this would require that a single edge may have to represent several variables and a single variable may have to represent several edges. Dependency diagrams (or dependency graphs), which are used to capture logical dependencies between literals in knowledge-based systems (Gallaire and Minker 1978, Ullman 1988), also suffer from similar limitations, since they do not distinguish between dependencies based on the specific rules that create them.

Another important issue is the validation of integrated models. This is a very difficult problem to formalize, since it involves consideration of a large variety of factors, some of which are qualitative and/or subjective. There has been relatively little work reported in the literature on this issue. There has been some work reported on validation of individual models (modules) (e.g., Brennan and Elam (1986), Finlay and Wilson (1987), Schneeweiss (1987)), but the extension of these efforts to more complex integrated models is still an open question.

Metagraphs have many of the features of the methods discussed here. However, the motivation for using metagraphs in model integration is based on three factors that distinguish this approach from the others. First, metagraphs provide a uniform basis for representing different types of modules in a DSS, such as data relations, decision models, and even rules (Basu and Blanning 1993). Thus, candidate integrated models that include both data relations and decision models can be identified using metagraphs. Second, the application of metagraphs to model integration is based upon the effective use of connectivity-related properties of metagraphs, and such properties have not been used to the same extent in alternative approaches. Third, the metagraph approach is consistent with, and complements, some of the existing approaches. For instance, the focus of the relational approach (Blanning 1985) is on representation of modules as virtual relations, and reasoning about them using relational theory. However, procedures for model integration are not explicitly addressed. That is, methods for identifying candidate virtual relations for integration into models are not developed, although the actual combination of selected virtual relations can itself be effected easily through relational join operations. Since the representation of modules as metagraph edges is consistent with the relational representation, metagraph-based model integration complements the relational approach.

## 2.2. Viewing Modules as "Black Boxes"

In dealing with model integration, each module can be represented as either a "black box" relating specific inputs to specific outputs, or with more detailed specifications that include attributes of the internal structure of each module (such as cost, reliability, range, accuracy, and the functional form of the relationships between inputs and outputs). Since metagraphs represent modules based on the former approach, it is worth discussing the role of such approaches.

To start with, we distinguish between the following two questions that arise in model management—"What combinations of modules should we consider as candidates for model integration?", and “How can we construct an integrated model from several component modules?" The first question requires understanding and manipulation of the interrelationships between modules, while the latter also requires understanding of the internal structure of each module.

The primary role of black box views of modules (or any systems. in general) is to focus on the interrelationships between different modules and facilitate understanding and use of these relationships. For instance, in the box structured methodology for systems analysis and design (Mills et al. 1986), the black box view is used to determine system requirements, and in processes such as box replacement, while clear box (and state box) views are used for analysis of internal structure and design refinement. Similarly, in módel management systems such as ASCEND (Krishnan et al. 1993) and FW/SM (Geoffrion 1991), consideration of relationships between models is based on "ports", which provide a black box view of each model. Such constructs, like metagraphs, are ideal for designing automated support facilities for model integration processes dealing with the identification of candidate collections of modules from a large model and data base. Since both data relations and decision models can be represented as edges in a metagraph, this has the added advantage of facilitating inclusion of relevant instances of both types of modules in integrated models.

Furthermore, black box views of modules have been used in a number of approaches to model integration. These include the logic-based approach in Dutta and Basu (1984), TIMMS (Liang 1988), SYMMS (Muhanna and Pick 1988), Muhanna (1994), and the process-oriented approach in Kotteman and Dolk (1992). In addition to these formal approachés, black box views are also used as pictorial representations of modules, even when they are not the basis for formal analysis in model integration.

Thus, the "black box" assumption is a useful one in methods to search through large model bases and identify candidate sets of modules for integration into models for specific problems. However, it is limited in that some of the identified candidates may have to be rejected due to their content and structure (cost, accuracy, validity, assumptions, etc.), and evaluation of such factors cannot be made based on a view that only considers inputs and outputs.

<table><tr><td colspan="4">TABLE 1The Example DSS</td></tr><tr><td colspan="4">MODELS</td></tr><tr><td>Name</td><td>Type</td><td>Input</td><td>Output</td></tr><tr><td>Acc</td><td>Accounting Model</td><td>m, r</td><td>g</td></tr><tr><td>Fin</td><td>Financial Model</td><td>g, s</td><td>n</td></tr><tr><td>Frc</td><td>Forecasting Model</td><td>c, i, p</td><td>n</td></tr><tr><td>Mkt</td><td>Marketing Model</td><td>i, p</td><td>r, v</td></tr><tr><td>Ohd</td><td>Overhead Model</td><td>c</td><td>s</td></tr><tr><td>Prd</td><td>Production Model</td><td>v</td><td>c, m</td></tr><tr><td>Sls</td><td>Sales Model</td><td>p, v</td><td>r</td></tr></table>

VARIABLES: c = capacity, g = gross income, i = economic indicator, m = manufacturing cost, n = net income, p = product price, r = revenue, s = selling and administrative expense, v = sales volume.

It should be recognized that most approaches to model integration that utilize black box views can be extended to include (or already have) additional features that allow internal structural information to be specified, so that the questions of formulating integrated models can also be addressed. This is exemplified by ASCEND and SYMMS. Similarly, metagraph-based model integration could also be enhanced through either extension of metagraph features with attributes and other qualifiers, as well as integration of metagraphs with appropriate algebraic representations of module structure and content.

## 3. Metagraphs and Their Properties

## 3.1. Metagraphs and Paths

In order to introduce metagraphs, compare them with graphs and hypergraphs, and examine their properties. We present an example. Consider a simple DSS consisting of seven stored models with a total of nine input and output variables. The models and variables are described in Table 1. This may be represented in graphical form, by means of a directed graph (or digraph). A directed graph is a set of elements and a set of edges, which are ordered pairs of elements (Berge 1985). In a pictorial representation the elements would be dots or other small icons and the edges would be arrows connecting the dots.

There are two ways in which this system might be represented as a digraph. First, the models could be elements with the variables as edges. The problem with this representation is that the same variable might appear as several edges and two elements might be connected by more than one edge. A second possibility is for the variables to be elements with the edges as models. However, some information would be lost in this representation. If a variable was at the end of two edges, it would not be clear whether the variable was determined by means of a single module or by means of two separate modules. The reason is that a directed graph describes pairwise relationships only and not relationships between three or more variables. Although attributed digraphs (Jones 1990, 1991; Schocken and Jones 1993) can overcome some of these limitations, they suffer from the drawback that the identity and form of a single module having m inputs and n outputs is distributed across m × n attributed edges

Another possibility is to use an AND/OR graph, in which edges incident to a node are combined with AND or OR designations. However, this is clumsy if a single module has several outputs. That is, the resulting representation would have multiple edges for a single module. For instance, the marketing model (Mkt) and the production model (Prd) in our example would each have separate AND-edges to each of their outputs, which would require the use of some label to identify the two edges as corresponding to the same module. Similarly, if a single variable is contained in the outputs of several modules having some common inputs, visualization of the different modules can be confusing.

The relationships between sets of elements can also be represented by a hypergraph, which is a set of elements and set of edges, each of which is a set containing one or more of the elements (Berge 1989). In a hypergraph, unlike a digraph, each element must appear in one or more of the edges. In this case the elements would represent variables and the edges would represent the modules. But the directionality of the relationship (i.e., the separation of inputs from outputs) would not be represented.

These disadvantages are overcome by the use of metagraphs, which allow more than two elements to participate in an edge while capturing the direction of the input-to-output relationship among the elements. A metagraph is defined as follows.

DEFINITION 1. Given a finite generating set $X = \{ x _ { i } , i = 1 , \dots , I \}$ , a metagraph on X is an ordered pair $S = \langle X , E \rangle$ , in which $E = \{ e _ { k } , k = 1 , \ldots , K \}$ .Each edge $\pmb { e _ { k } } \in \pmb { E }$ is an ordered pair of sets $e _ { k } \dot { = } \langle \dot { V _ { k } } , \dot { W _ { k } } \rangle$ in which $V _ { k } \subseteq X$ is the invertex of $\scriptstyle { e _ { k } }$ and $W _ { k } \subseteq X$ is the outvertex. We require that $\dot { V _ { k } } \cup W _ { k } \not = \emptyset$ for $k = 1 , \ldots , K .$

The metagraph for our example is illustrated in Figure 1. The marketing model is $\mathbf { M k t } = \langle \{ i , p \} , \{ v , r \} \rangle$ and the production model is $\mathbf { P r d } = \langle \{ \boldsymbol { v } \} , \{ m , c \} \rangle$ . The relationship between these edges is represented by the connectivity between edges. For example, since $W _ { \mathrm { M k } } \cap V _ { \mathrm { P r d } } = \{ v \}$ , one of the outputs of the marketing model is an input to the production model. We note that it would be difficult to describe this using AND/ OR graphs, since two of the edges, Mkt and Prd, have multiple elements in their out vertices.

The concept of a path is an important one in graph-based model integration. However, this concept is more complicated as applied to metagraphs than as applied to digraphs and hypergraphs. We begin by examining a type of path similar to that found in digraphs and hypergraphs.

DEFINITION 2. Given a generating set $\pmb { X } ,$ a metagraph $\scriptstyle { S = \langle X , E \rangle }$ , and two distinct elements $\pmb { a } \in \pmb { X }$ and $b \in X ,$ , a simple path from a to b is a sequence of edges h(a, b) $= \langle e _ { 1 } ^ { \prime } \cdots e _ { L } ^ { \prime } \rangle$ such that:

1. $a \in V _ { 1 } , b \in W _ { L } ,$

2. $W _ { l } \cap V _ { l + 1 } \neq \emptyset$ for $l = 1 , \ldots , L - 1 ;$ , and

3. $\left\{ e _ { l } ^ { \prime } , l = 1 , \ldots , L \right\} \subseteq E .$

The coinput of a in $\pmb { h } ( \pmb { a } , \pmb { b } )$ is $\{ \cup _ { l = 1 } ^ { L } V _ { l } ^ { \prime } \backslash \cup _ { l = 1 } ^ { L } W _ { l } ^ { \prime } \} \backslash \{ a \}$

and the cooutput of b in $\pmb { h } ( \pmb { a } , \pmb { b } )$ is $\cup _ { l = 1 } ^ { \bar { L } } \bar { W } _ { l } \backslash \{ \bar { b } \}$

For example, there is a path $h ( i , m ) = \left. \mathrm { M k t , P r d } \right.$ from i to m, with {p} as coinput, and $\{ c , r , v \}$ as cooutput. Thus, if we know the value of the economic indicator we can determine the value of the manufacturing cost as long as we know the sale price (coinput), and we also determine the values of capacity, revenue, and volume (cooutput) as a byproduct. This is done by executing the market model and then the production model. In general, if there exists a path between two elements a and $\mathbf { \delta } _ { \mathbf { \delta } }$ then it is possible to compute a value for $\begin{array} { r } { \pmb { b } , } \end{array}$ starting with a as input, and executing the modules corresponding to the edges in the path in a strict sequence based on their positions in the path. As the modules are executed, coinputs may be needed, and cooutputs may be calculated as well.

Although the notion of a simple path can be used in many cases to identify a module sequence for a given problem instance, it is in general too limited to be used as a basis for model integration. There may be circumstances in which it is advisable to execute a set of models that cannot be arranged in a sequence. For example, one may have identified a set of available input elements and may wish to find one or more output elements. The problem is to identify a set of models (edges) that will determine all of the desired outputs without requiring any external inputs other than those available in the given input set. It is possible that the set of edges will be a path from one of the inputs to one of the outputs such that the coinputs are in the given input set and the cooutputs cover all of the remaining desired outputs. However, it may be necessary to invoke a set of edges that does not form a sequence, and hence is not

a path.

For example, there are three simple paths from v to n: $\langle \mathbf { S l s } , \mathbf { A c c } , \mathbf { F i n } \rangle$ with coinput $\{ p , m , s \} , \langle \mathrm { P r d } , \mathrm { A c c } , \mathrm { F i n } \rangle$ with coinput $\{ r , s \}$ , and (Prd, Òhd, Fin) with coinput $\{ \pmb { g } \}$ But there is another alternative—to execute the set {Acc, Fin, Ohd, Prd, Sls}, which requires $\{ p \}$ as coinput and produces $\{ c , g , m , s , v \}$ as cooutput. In other words, it is possible to arrive at n given only p and $v ,$ which is not apparent from the three simple paths. The set of edges needed to do this cannot be ordered to form a simple path. Thus, we need a more sophisticated notion of paths in metagraphs to represent this alternative.

DEFINITION 3. Given a generating set $\scriptstyle { \pmb { \chi } } ,$ a metagraph $S = \langle X , E \rangle$ , and two disjoint subsets $\pmb { A } \subseteq \pmb { X }$ and $B \subseteq X ,$ , a metapath from A to B is a set of edges $\begin{array} { r } { \dot { M } ( A , B ) = \left\{ e _ { l } ^ { \prime } , l = 1 \right. } \end{array}$ $\cdots , L \} \subseteq E$ such that:

1. For each $l = 1 , \ldots , L$ there is a simple path ${ \pmb h } _ { \pmb { k } } ( { \pmb a } , { \pmb b } )$ from some a $\iota \in A$ to some $\pmb { b } \in$ B such that $e _ { t } ^ { \prime } \in$ set $h _ { l } ( a , b ) ) \subseteq M ( A , B )$ (where set( ) is a mapping from a sequence to a set, $\mathbf { i . e . , }$ set $\langle \langle y _ { i } , j = 1 , \ldots , J \rangle \rangle = \{ y _ { j } , j = 1 , \ldots , J \} \rangle ,$

2. $\alpha ( M ) = \dot { \bigcup } _ { l = 1 } ^ { L } V _ { l } ^ { \prime } \backslash \cup _ { l = 1 } ^ { L } \dot { W } _ { l } ^ { \prime } \subseteq A ;$

$$
3. B \subseteq \beta (M) = \cup_ {l = 1} ^ {L} W _ {l}.
$$

In our example metagraph, if $A = \{ p , v \}$ and $B = \{ n \}$ , there is a metapath $M ( A , B )$ $= \{ \operatorname { A c c } , \operatorname { F i n } , \operatorname { O h d } , \operatorname { P r d } , \operatorname { S l s } \}$ from A to B with $\alpha ( M ) = \{ p , v \}$ and $\beta ( M ) = \left\{ c , g , m , n , r , \right.$ $^  s \} { }$

There are two features of metagraphs that are important in addressing the problems of model synthesis but are not found in other graphical structures. The first feature is coinputs and cooutputs of simple paths. Although simple paths $( \mathbf { i . } \hat { \mathbf { e . } } ,$ , sequences of edges) are found in these other structures, notions of coinput and cooutput are found only in metagraphs. The second feature is metapaths. In other graphical structures paths are restricted to sequences of edges, and there is no convenient way of representing nonsequential interactions between edges.

We note two additional characteristics of metapaths:

1. For any metapath $M ( A , B )$ , if an edge $e \in E$ is not contained in some path $h ( a , b )$ with ${ \pmb { a } } \in \pmb { A }$ and $\boldsymbol { b } \in \mathcal { B } ,$ then $e \not \in \mathbf { M } ( A , B )$

2. If M(A, B) is a metapath from A to B and there are two subsets A'. $B ^ { \prime } \subseteq X$ with $\alpha ( M ) \subseteq A ^ { \prime }$ and $B ^ { \prime } \subseteq \beta ( M ) .$ , then $M ( A , B )$ is also a metapath from $\pmb { A } ^ { \prime }$ to $\pmb { B } ^ { \prime }$

In other words, if we wish to construct a metapath from A to B, we can begin by $\pmb { B } ,$ removing from consideration those edges that are not on any path from some ${ a } \in A$ to some $b \in B .$ 3. Similarly, if we wish to determine whether certain sets of edges constitute such a metapath, we can eliminate candidates that contain an edge that is not on any path from some $\pmb { a } \in \pmb { A }$ to some $\boldsymbol { b } \in \mathbf { B } .$ The second observation is that any metapath M(A, B) from A to B is also a metapath from any superset of $\pmb { \alpha } ( M )$ to any subset of $\beta ( M ) .$

Furthermore, information about known metapaths may be useful in constructing new metapaths. Given a set of known metapaths $\{ M _ { l } ( A _ { l } , B _ { l } ) , l = 1 , \ldots , L \}$ , a metapath from C to D might be identified from this information. We might begin by searching for $\pmb { A _ { b } } , \pmb { B _ { l } }$ pairs such that

$$
\alpha (M _ {l} (A _ {l}, B _ {l})) \subseteq C \quad \text { and } \quad D \subseteq \beta (M _ {l} (A _ {l}, B _ {l})).
$$

In this case, $M ( A _ { b } \ B _ { l } )$ is also a metapath from C to D. An easier but less effective method is to search for a pair $\pmb { A _ { b } } , \pmb { B _ { l } }$ such that $\boldsymbol { A } _ { l } \subseteq C$ and $D \subseteq B _ { l }$

Since metapaths represent sufficient sets of edges to traverse a metagraph from one set of elements to another, they can be used to construct alternative candidate models for determining a desired set of output parameters from a specified set of input parameters. In general, there could be several (and possibly a large number of) such metapaths. The number of metapaths between two sets of elements A and B is likely to increase as A is enlarged, and is likely to decrease as B increases. In the remainder of this section, we present and discuss some properties of metapaths that are useful in identifying candidate integrated models, and in reasoning about such models, as discussed in the next section.

## 3.2. Dominant Metapaths

While every metapath from A to B represents a candidate set of models for computing the elements in B given values for elements in A, some of these metapaths are $\mathbf { \delta } _ { \mathbf { \delta } _ { \mathbf { \delta } _ { \mathbf { \delta } _ { \mathbf { \delta } _ { \mathbf { \delta } _ { \lambda } } } } } } \mathbf { \delta } _ { \mathbf { \delta } _ { \mathbf { \lambda } _ { \mathbf { \delta } _ { \lambda } } } }$ undesirable; for instance, they may include superfluous models, or may utilize more inputs than necessary. In order to provide a basis for distinguishing between the different metapaths, we next define some special classes of metapaths, and show how they can be used in model synthesis.

DEFINITION 4. Given a generating set $\pmb { X } ,$ a metagraph $\pmb { S } = \langle \pmb { X } , \pmb { E } \rangle$ , two distinct elements $a , b \in X ,$ , and two disjoint element sets A, $B \subseteq X ;$

1. Two metapaths M1 and M2 between A and B are said to be edge disjoint if $\pmb { M _ { 1 } }$ $M _ { 2 }$ $M _ { 1 }$ n $M _ { 2 } = \mathcal { D }$

2. A metapath $M ( A , B )$ is said to be edge dominant if there is no metapath M'(A. B)⊂M.

3. A metapath $M ( A , B )$ is said to be input dominant if there is no set of elements A' C A such that there is a metapath $M ^ { \prime } ( A ^ { \prime } , B )$

4. A metapath $M ( A , B )$ is said to be dominant if it is both input dominant and edge dominant.

5. An edge e in a metapath $M ( A , B )$ is said to be nonredundant if it lies on every metapath $M ( A , Y ) \subseteq M ,$ where $\mathbf { { \boldsymbol { Y } } } \subseteq \mathbf { { \boldsymbol { B } } } .$ . Otherwise, it is redundant. Also, a metapath M is cyclic if there is a path $h ( x , x )$ such that $s e t ( h ) \subseteq M$ Otherwise, M is acyclic.

![](/api/attachments/R9SUQWV8/fulltext/images/ef8c9be77b145adad4b6438001370a09a8dd7547c3e3654259ea1623170aef63.jpg)  
FIGURE 1. A Metagraph.

Based on these properties, we have the following useful theorem.

THEoREM 1. A metapath is edge-dominant iff each of its edges is nonredundant (Proof in the Appendix).

An edge-dominant metapath is not necessarily acyclic. This can be proved easily by counterexample. Consider the metapath consisting of the following edges:

$$
e _ {1}: \left\langle \left\{x _ {1}, x _ {2} \right\}, \left\{x _ {3} \right\} \right\rangle , \quad e _ {2}: \left\langle \left\{x _ {3}, x _ {4} \right\}, \left\{x _ {5}, x _ {6} \right\} \right\rangle , \quad e _ {3}: \left\langle \left\{x _ {6} \right\}, \left\{x _ {4} \right\} \right\rangle .
$$

If $\mathbf { \dot { A } } = \left\{ x _ { 1 } , x _ { 2 } \right\}$ , and $B = \{ x _ { 5 } , x _ { 6 } \}$ , then $\boldsymbol { M } = \left\{ \boldsymbol { e } _ { 1 } , \boldsymbol { e } _ { 2 } , \boldsymbol { e } _ { 3 } \right\}$ is an edge-dominant metapath. However, it contains a cycle through x4 and x6. This is quite different from directed $\pmb { x _ { 4 } }$ $x _ { 6 } .$ graphs, where paths that contain cycles can always be reduced to acyclic paths by removing one or more edges.

## 3.3. Bridges

An important issue in connectivity is whether there are edges that are essential to that connectivity, Specifically, if two elements or sets of elements are connected, we would like to know whether there are any edges which if removed would disrupt this connectivity, We do this by defining a bridge between the pair of elements or pair of sets, and examining the properties of such bridges.

DEFINITION 5. Given a generating set X, a metagraph $\scriptstyle { \pmb { X } } ,$ $S = \langle X , E \rangle$ , two distinct elements $a , b \in X ,$ and two disjoint element sets $A , B \subseteq X ;$

1. $\pmb { a }$ is connected to b (denoted ${ a  b } )$ if there is a path $\pmb { h } ( \pmb { a } , \pmb { b } )$ from a to $\pmb { b ; }$

2. A is connected to B (denñoted $A  B )$ if there is a metapath $M ( A , B ) ;$

3. an edge e is a bridge between a and b if $a  b \mathrm { i n } S ,$ but not in $\dot { S ^ { \prime } } = \langle X , E \setminus \{ e \} \rangle ;$

4.. an edge e is a bridge between A and $B \mathrm { i f } A  B \mathrm { i n } S ,$ but not in $S ^ { \prime } = \left. X , E \backslash \{ e \} \right.$

ExAMPLE. In Figure 1, we see that i is connected to both s and $n ( \mathrm { i . e . , } i \to s \mathrm { a n d } i \to$ $\pmb { n } )$ ). However, while there is no bridge between i and n, each of the edges Mkt, Ohd, $\pmb { n } ,$ Prd is a bridge between i and s. Similarly, consider the sets $\{ i , p \}$ and $\{ n \}$ . It is clear that $\{ i , p \} \to \{ n \}$ in the given metagraph. Now, if either of the edges $\mathbf { M k } \mathbf { t } ,$ Prd is removed, is would no longer be possible to compute $\{ n \}$ from $\{ i , p \}$ , and thus these edges are bridges between the two given sets. On the other hand, the edges Acc, Fin, Frc, Ohd, Sls are not bridges in this case, since they do not disrupt the relevant connectivity. □

The following theorem relates the concept of edge-dominant metapaths defined in the previous subsection to the concept of a bridge defined here.

TíEOREM 2. Let A and B be two disjoint sets of elements A and B in a metagraph such that $A  B ,$ If there is no bridge between A and B, then there are at least two edge-dominant metapaths from A to B (Proof in the Appendix).

We note that connectivity is transitive, as stated in the following lemma, the proof of which is left to the reader.

LEMMA. Given three pairwise disjoint sets of elements, A, $B , C \subseteq X , i f A \to C$ and $c \to B$ then $A  B .$

Finally, we state three results concerning bridges:

THEOREM 3. Given a generating set X, a metagraph $S = \langle X , E \rangle$ , two disjoint sets $A , B \subseteq X$ such that $A  B ,$ and a bridge e between À and B:

1. For any set $C \subseteq X$ such that $\pmb { A }  \pmb { C }$ and $C \to B ,$ , e is a bridge between either A and $c ,$ or between C and B.

2. $H M _ { 1 } , M _ { 2 }$ are two metapaths from A to $\mathbf { \delta } _ { B , \delta }$ then $e \in M _ { 1 } \cap M _ { 2 }$ and thus, no two metapaths from A to B are edge disjoint.

3. For any two sets A', B' such that $A ^ { \prime }  B ^ { \prime } , A ^ { \prime } \subseteq A a n d B \subseteq B ^ { \prime }$ , e is a bridge between A' and B'.

(Proof in the Appendix.

## 3.4. Adjacency Matrices

In the following section, we will find it useful to invoke the concept of an adjacency matrix for metagraphs (Basu and Blanning 1994). The adjacency matrix of a metagraph contains one row and one column for each element in the generating set. We denote the adjacency matrix by A and the component of A in row i and column j by $a _ { i j } .$ Each component consists of zero or more triples, one for each edge connecting the ordered elements, consisting of the coinput, cooutput, and the edge itself. For example, the adjacency matrix of the metagraph of Figure 1 appears in Figure 2. We have $a _ { p v } = \{ \langle \{ i \} , \{ r \} , \langle \mathbf { M } \mathbf { k } \mathbf { t } \rangle \rangle \}$ , since there is one edge, Mkt, connecting p to v; the coinput of p is {i}, and the cooutput of v is {r}. On the other hand, there are two edges, Mkt and Sls, connecting p to r, and ap is the set consisting of two triples $a _ { p r }$ $\langle \{ i \} , \{ v \} , \langle \mathbf { M } \mathbf { k } \ t \rangle \rangle$ and $\big \langle \{ \pmb { v } \} , \pmb { \phi } , \big \langle \pmb { \mathbb { S } } \mathbf { \mathsf { l s } } \big \rangle \big \rangle$ , each containing as its first two components the coinputs and cooutputs of the appropriate edge and as its third component the edge itself. On the other hand, many of the components of A are null, since most pairs of elements are not connected by any edges. For example, there is no edge connecting r to c, so $\pmb { c } ,$ $\pmb { a } _ { r c } = \pmb { \mathcal { D } }$

It is also possible to define a multiplication operation for metagraph adjacency matrices, which can be used to calculate powers of the matrix. Each component of $A ^ { n }$ will consist of zero or more tuples, one for each path of length n from the first indexed element of the component to the second. For example, there is one path of length two from v to s consisting of $h ( v , s ) = \langle \mathrm { P r } \mathrm { d } , \mathrm { O h d } \rangle$ . Therefore, $a _ { v s } ^ { 2 } = \smash { \bar { \{ \zeta \phi , \{ c , m \} } } $ , (Prd, $\mathrm { o h d } \rangle \rangle \}$ . The first component of the triple is the coinput, φ, of v on this path, the $\phi ,$ second is the cooutput of s, and the third component is the path. ${ \pmb S } ,$

The closure of the adjacency matrix is the sum $A ^ { * } = A + A ^ { 2 } + A ^ { 3 } + \cdots$ , in which addition is performed by taking the union of the triples in $A , A ^ { 2 } , A ^ { 3 } ,$ , etc. Each component of A\* consists of zero or more triples, one for each path of any length from the $\pmb { A } ^ { * }$ first indexed element of the component to the second indexed element. This is illustrated in Figure 3. For example, there are two paths from c to n: a path of length one $( \tt i . e .$ , an edge), (Frc>, and a path of length two, <Ohd, Fin). Thus an consists of two $a _ { c n } ^ { * }$ triples, containing the coinputs, cooutputs, and paths.

We have demonstrated elsewhere that metapaths can be derived from a subset of the triples in A\* (Basu and Blanning 1993). All metapaths from a set $\pmb { A } ^ { * }$ $X _ { 1 } \subseteq X \operatorname { t o } X _ { 2 } \subseteq X$ can be calculated as follows:

1. List the triples ${ \pmb a } _ { \mathbf { x } \mathbf { y } } ^ { * }$ for all $x \in X _ { 1 } , y \in X _ { 2 } .$

2. Determine the power set of these triples.

3. For each member of the power set, let α be the union of the first components of the triples (i.e., the coinputs), β be the union of the second components (i.e., the $( \mathbf { i . e . } ,$ $\pmb \beta$ $( \tt i . e . ,$ cooutputs), γ be the union of the second indices y of all a\*y from which the set of $\pmb { \gamma }$ $_ y$ $\pmb { a } _ { \mathbf { x } \mathbf { y } } ^ { * }$ triples was constructed, and δ be the union of the edges in the third components $( \overrightarrow { 1 } . \overrightarrow { 0 } . ,$ the set of edges in the paths in the triples). If $\ O ^ { \cdot } \alpha \backslash ( \beta \cup \gamma ) \subseteq \dot { X _ { 1 } }$ and $X _ { 2 } \subseteq ( \beta \cup \gamma )$ , then δ is a metapath from $X _ { 1 }$ to $X _ { 2 } .$

ExAMPLE. Consider the metagraph in Figure 1. Let $X _ { 1 } = \{ c , m , r \}$ and $X _ { 2 } = \{ n \}$ From Figure 3, we see that there are four triples, corresponding to four simple paths ${ \mathfrak { 3 } } ,$ from elements of X, to those of X, all of which have nonnull coinputs. If we consider $X _ { 1 }$ $\mathbf { { \mathit { X } } _ { 2 } } ,$ the triples

$$
\langle \{g \}, \{s \}, \langle \text { Ohd,   Fin } \rangle \rangle \text { contained   in } a _ {c n} ^ {*}, \quad \text { and }
$$

$$
\langle \{r, s \}, \{g \}, \langle \text { Acc,   Fin } \rangle \rangle \text { contained   in } a _ {m n} ^ {*},
$$

we compute the union of the coinputs: ${ \boldsymbol { \alpha } } = \{ { \boldsymbol { g } } , { \boldsymbol { r } } , { \boldsymbol { s } } \}$ , the union of the cooutputs: $\pmb \beta$ $= \{ \pmb { g } , \pmb { s } \}$ , the union of the destinations of the selected simple paths: $\gamma = \{ n \}$ , and the set of edges occurring in these paths: $\delta = \{ \sf A c c , $ Fin, Ohd}. Since $\alpha \setminus ( \beta \cup \gamma ) . = \{ r \} \subseteq X _ { 1 } ,$ and $X _ { 2 } \subseteq ( \beta \cup \gamma ) = \{ g , n , s \}$ , we conclude that $\delta = \{ \mathbf { A c c } , \mathbf { \tilde { F } i n } , \mathbf { O h d } \}$ is a metapath from $X _ { 1 }$ to $X _ { 2 }$ .□

This procedure is not very efficient, since the power set grows exponentially with the number of triples. However, the relevant triples are restricted to those found in an appropriate subset of A\*. We use this feature in a more efficient algorithm in the $\pmb { A } ^ { * }$ following section.

We conclude this section by noting that metapaths cannot be found from the adjacency matrix of a directed graph and its closure. The adjacency matrix of a directed graph consists of ${ a } _ { x y } = 1$ if there is an edge connecting x and y and 0 otherwise. Then a"y is the number of paths of length n connecting x and y, and ay is $\pmb { a } _ { \mathbf { x } \pmb { y } } ^ { n }$ ${ \pmb y } _ { \pmb \nu }$ $\pmb { a } _ { x y } ^ { * }$ the number of paths of any length connecting x and y. However, there are two $\pmb { x }$ $\pmb { y } .$ problems with using A\* to identify metapaths. First, the components of A\* do not $\pmb { A } ^ { * }$ $A ^ { * }$ identify specific paths, but only disclose the number of paths. Second, these components do not contain coinput and cooutput information. Thus, although digraphs contain a limited amount of connectivity information, it is not possible to construct a similar algorithm from the A and A\* of a digraph. $A ^ { * }$

<table><tr><td></td><td>c</td><td>g</td><td>i</td><td>m</td><td>n</td><td>p</td><td>r</td><td>s</td><td>v</td></tr><tr><td>c</td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{\langle\{i,p\},\phi,\langle\mathrm{Frc}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{\langle\phi,\phi,\langle\mathrm{Ohd}\rangle\rangle\}$ </td><td> $\phi$ </td></tr><tr><td>g</td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{\langle\{s\},\phi,\langle\mathrm{Fin}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td></tr><tr><td>i</td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{\langle\{c,p\},\phi,\langle\mathrm{Frc}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\{\langle\{p\},\{v\},\langle\mathrm{Mkt}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\{\langle\{p\},\{r\},\langle\mathrm{Mkt}\rangle\rangle\}$ </td></tr><tr><td>m</td><td> $\phi$ </td><td> $\{\langle\{r\},\{\phi\},\langle\mathrm{Acc}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td></tr><tr><td>n</td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td></tr><tr><td>p</td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{\langle\{c,i\},\phi,\langle\mathrm{Frc}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\{\langle\{i\},\{v\},\langle\mathrm{Mkt}\rangle\rangle, \langle\{v\},\phi,\langle\mathrm{Sls}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\{\langle\{i\},\{r\},\langle\mathrm{Mkt}\rangle\rangle\}$ </td></tr><tr><td>r</td><td> $\phi$ </td><td> $\{\langle\{m\},\{\phi\},\langle\mathrm{Acc}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td></tr><tr><td>s</td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{\langle\{g\},\phi,\langle\mathrm{Fin}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td></tr><tr><td>v</td><td> $\{\langle\{\phi\},\{m\},\langle\mathrm{Prd}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{\langle\{\phi\},\{c\},\langle\mathrm{Prd}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{\langle\{p\},\{\phi\},\langle\mathrm{Sls}\rangle\rangle\}$ </td><td> $\phi$ </td><td> $\phi$ </td></tr></table>

<table><tr><td></td><td>c</td><td>g</td><td>i</td><td>m</td><td>n</td><td>p</td><td>r</td><td>s</td><td>v</td></tr><tr><td>c</td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{ \langle \{ g \}, \{ s \}, \langle \text {Ohd, Fin} \rangle \rangle , \langle \{ i, p \}, \phi , \langle \text {Frc} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{ \langle \phi, \phi , \langle \text {Ohd} \rangle \rangle \}$ </td><td> $\phi$ </td></tr><tr><td>g</td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{ \langle \{ s \}, \phi , \langle \text {Fin} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td></tr><tr><td>i</td><td> $\{ \langle \{ p \}, \{ m, r, v \}, \langle \text {Mkt, Prd} \rangle \rangle \}$ </td><td> $\{ \langle \{ m, p \}, \{ r, v \}, \langle \text {Mkt, Sls, Acc} \rangle \rangle , \langle \{ p \}, \{ c, m, r, v \}, \langle \text {Mkt, Prd, Acc} \rangle \rangle , \langle \{ m, p \}, \{ r, v \}, \langle \text {Mkt, Acc} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\{ \langle \{ p \}, \{ c, r, v \}, \langle \text {Mkt, Prd} \rangle \rangle \}$ </td><td> $\{ \langle \{ m, p, s \}, \{ g, r, v \}, \langle \text {Mkt, Sls, Acc, Fin} \rangle \rangle , \langle \{ p, s \}, \{ c, g, m, r, v \}, \langle \text {Mkt, Prd, Acc, Fin} \rangle \rangle , \langle \{ g, p \}, \{ c, m, r, s, v \}, \langle \text {Mkt, Prd, Ohd, Fin} \rangle \rangle , \langle \{ p \}, \{ c, m, r, v \}, \langle \text {Mkt, Prd, Frc} \rangle \rangle , \langle \{ m, p, s \}, \{ g, r, v \}, \langle \text {Mkt, Acc, Fin} \rangle \rangle , \langle \{ c, p \}, \phi , \langle \text {Frc} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{ \langle \{ p \}, \{ v \}, \langle \text {Mkt, Sls} \rangle \rangle , \langle \{ p \}, \{ v \}, \langle \text {Mkt} \rangle \rangle \}$ </td><td> $\{ \langle \{ p \}, \{ r \}, \langle \text {Mkt} \rangle \rangle \}$ </td></tr><tr><td>m</td><td> $\phi$ </td><td> $\{ \langle \{ r \}, \{ \phi \}, \langle \text {Acc} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{ \langle \{ r, s \}, \{ g \}, \langle \text {Acc, Fin} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td></tr><tr><td>n</td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td></tr><tr><td>p</td><td> $\{ \langle \{ i \}, \{ m, r, v \}, \langle \text {Mkt, Prd} \rangle \rangle \}$ </td><td> $\{ \langle \{ i, m \}, \{ r, v \}, \langle \text {Mkt, Sls, Acc} \rangle \rangle , \langle \{ i \}, \{ c, m, r, v \}, \langle \text {Mkt, Prd, Acc} \rangle \rangle , \langle \{ i, m \}, \{ r, v \}, \langle \text {Mkt, Acc} \rangle \rangle , \langle \{ m, v \}, \{ r \}, \langle \text {Sls, Acc} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\{ \langle \{ i \}, \{ c, r, v \}, \langle \text {Mkt, Prd} \rangle \rangle \}$ </td><td> $\{ \langle \{ i, m, s \}, \{ g, r, v \}, \langle \text {Mkt, Sls, Acc, Fin} \rangle \rangle , \langle \{ i, s \}, \{ c, g, m, r, v \}, \langle \text {Mkt, Prd, Acc, Fin} \rangle \rangle , \langle \{ g, i \}, \{ c, m, r, s, v \}, \langle \text {Mkt, Prd, Ohd, Fin} \rangle \rangle , \langle \{ i \}, \{ c, m, r, v \}, \langle \text {Mkt, Prd, Frc} \rangle \rangle , \langle \{ i, m, s \}, \{ g, r, v \}, \langle \text {Mkt, Acc, Fin} \rangle \rangle , \langle \{ c, i \}, \phi , \langle \text {Frc} \rangle \rangle , \langle \{ m, s, v \}, \{ g, r \}, \langle \text {Sls, Acc, Fin} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{ \langle \{ i \}, \{ v \}, \langle \text {Mkt, Sls} \rangle \rangle , \langle \{ i \}, \{ v \}, \langle \text {Mkt} \rangle \rangle , \langle \{ v \}, \phi , \langle \text {Sls} \rangle \rangle \}$ </td><td> $\{ \langle \{ i \}, \{ c, m, r, v \}, \langle \text {Mkt, Prd, Ohd} \rangle \rangle \}$ </td></tr><tr><td>r</td><td> $\phi$ </td><td> $\{ \langle \{ m \}, \{ \phi \}, \langle \text {Acc} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{ \langle \{ m, s \}, \{ g \}, \langle \text {Acc, Fin} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td></tr><tr><td>s</td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\{ \langle \{ g \}, \phi , \langle \text {Fin} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td></tr><tr><td>v</td><td> $\{ \langle \{ \phi \}, \{ m \}, \langle \text {Prd} \rangle \rangle \}$ </td><td> $\{ \langle \{ m, p \}, \{ r \}, \langle \text {Sls, Acc} \rangle \rangle , \langle \{ r \}, \{ c, m \}, \langle \text {Prd, Acc} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\{ \langle \{ \phi \}, \{ c \}, \langle \text {Prd} \rangle \rangle \}$ </td><td> $\{ \langle \{ m, p, s \}, \{ g, r \}, \langle \text {Sls, Acc, Fin} \rangle \rangle , \langle \{ r, s \}, \{ c, g, m \}, \langle \text {Prd, Acc, Fin} \rangle \rangle , \langle \{ g \}, \{ c, m, s \}, \langle \text {Prd, Ohd, Fin} \rangle \rangle \}$ </td><td> $\phi$ </td><td> $\{ \langle \{ p \}, \{ \phi \}, \langle \text {Sls} \rangle \rangle \}$ </td><td> $\{ \langle \{ \phi \}, \{ c, m \}, \langle \text {Prd, Ohd} \rangle \rangle \}$ </td><td> $\phi$ </td></tr></table>

![](/api/attachments/R9SUQWV8/fulltext/images/c77425cc02346dca9911ec2fc677738c8c4d2ccd672ceae522ced65ed0fd2c5a.jpg)  
FIGURE 4. Some Symbols Used in State Charts.

## 3.5. Metagraphs and Higraphs

As mentioned in §2, the graphical construct most similar to a metagraph is the higraph (Harel 1988). Now that we have described the basic structure of metagraphs, we can compare these constructs.

To start with, it is important to realize that most of the existing applications of higraphs are based on different extensions of higraphs, rather than on the basic structure of higraphs specified by Harel (1988). One such extension is the state chart (Harel 1987), which has been used for visually specifying complex reactive systems (Harel et al. 1990). Another extension is constraint (and instance) pictures used for visual specification of security mechanisms in computer systems (Heydon et al. 1990. Wing 1990). Each of these extensions involve many additional features, some of which are illustrated in Figure 4. Some of these features have different semantics in the different extensions. Thus, methods developed for each of these extensions cannot easily be generalized to the others. In order to make a fair comparison (since such application-specific extensions can be made to metagraphs as well), we will restrict our attention in this discussion to the original formalization of higraphs in (Harel 1988).

Consider the simple metagraph shown in Figure 5(a), which might represent three modules, $e _ { 1 } , e _ { 2 }$ and $e _ { 3 } ,$ between the elements $a , b , c , d , e .$ This model base could also be represented as a higraph, as shown in Figure 5(b); the dotted lines denote vertices (or blobs) corresponding to conjunctive relationships. From a visualization standpoint, the two constructs appear to be equivalent. In fact, higraphs allow a wider array of edge structures, including edges from within biobs, and “hyperedges" (edges linking more than 2 blobs). These additional types of edges convey more information for visualization purposes. However, the expressive power of higraphs can itself make visualization and interpretation difficult and ambiguous, as Harel has observed (1987, 1988), since there are often multiple ways of representing the same relationship.

![](/api/attachments/R9SUQWV8/fulltext/images/d17ff5d86dd0a56e1642b181319e7a18ec6fb64adfae04e6c8022b899ede79de.jpg)  
(a) Metagraph

![](/api/attachments/R9SUQWV8/fulltext/images/c771ec9389958f3adad953aa3f7520cca1563e3886dc77dee83c7b494caa6a65.jpg)  
FIGURE 5. Metagraph and Higraph.  
(b) Higraph

From an analytical perspective, however, properties such as reachability, connectivity and transitive closure, and formal procedures to test these properties have not been formally developed for higraphs, although algorithms to test for reachability have been developed for certain specializations such as state charts (Harel et al. 1988). On the other hand, by formally defining the adjacency matrix for a metagraph, and an algebraic basis for the closure, we have a general, nonprocedural formalism that precisely defines properties such as reachability, connectivity and transitive closure, and can be used to identify coinputs and cooutputs of paths, as well as metapaths. For instance, we have algebraic operators that can be used to identify the metapath between ${ \pmb a } ,$ b and e in Figure 5(a) (using a specific portion of the $A ^ { * }$ matrix). Similarly, we can easily determine that for the path $\langle e _ { 1 } , e _ { 2 } \rangle$ from a to $\pmb { e } _ { \pmb { \mathscr { s } } }$ the coinput is d and the cooutput is c. There are no comparable methods in higraphs.

This raises the obvious question, why not simply develop corresponding operators and methods for higraphs? In developing a matrix algebra for metagraphs, an important assumption is the predefined generating set for each metagraph. In other words, adding edges to or modifying edges in a metagraph does not change the indices of the adjacency matrix, merely its contents. On the other hand, a fundamental assumption in higraphs is that the basic set of elements is the set of blobs, each of which may be either atomic or composed of subblobs. Thus, the indices of a higraph adjacency matrix would be the blobs, and since this set is not predetermined and can change as new edges are defined on the same set of atomic blobs (the generating set), the matrix structure and operators would be far more complex, since the indices would change as new relationships are discovered and specified.

Furthermore, the semantics of higraphs explicitly distinguish between two types of blobs, those representing disjunctions (the default), and those representing conjunctions (with the orthogonal components). Note that with metagraphs, since the implicit assumption is that elements of a vertex are conjunctively related and disjunction is realized through separate edges, we do not need two types of vertices. Also, even if we were to restrict the indices of a higraph adjacency matrix to the atomic blobs, some additional syntactical operator would be needed in the adjacency matrix to deal with edges between blobs and their own subblobs, or with hyperedges. For example, for the higraphs in Figure 6, such operators would be essential to distinguish between the two higraphs. Finally, the semantics of hyperedges is unclear without adding edge labels and attributes. We can speculate that metagraphs with edge and node attributes could have comparable expressive power, but that is outside the scope of our current work.

In summary, what we find is that higraphs represent a very powerful tool for graphical visualization of system behavior and structure. However, the rich set of features incorporated in higraphs make it difficult to develop the kinds of algebraic properties that form the basis for metagraph analysis. Thus, we can think of metagraphs as a specialization of higraphs for which these formal analytical operators and properties have been developed, and which are suitable for the type of model analysis we have presented in this paper. Perhaps, future work with attributed metagraphs and further development of higraph semantics could lead to a convergence of the two constructs.

![](/api/attachments/R9SUQWV8/fulltext/images/d80ddab80ea0f55e36234ccd38fb2e27d69fe0ddd8c55e04f9b70a1fe8c87791.jpg)  
FIGURE 6. Similar Higraphs That Complicate Adjacency Matrix

## 4. Using Metagraphs in Model Integration

A metagraph edge can be used to represent a decision model, with the invertex corresponding to the model inputs, and the outvertex corresponding to the model outputs. Similarly, an edge can also be used to represent a database relation, with the invertex representing the relation's key attributes and the outvertex representing the content (or nonkey) attributes. If a metagraph representation of the stored modules in a DSS is available, identification of a candidate integrated model can be achieved by exploiting the notion of a metapath. In fact, connectivity properties of metagraphs can be used to address all the model integration questions posed in §1, as shown $\ S 1$ below. Wherever possible, we will illustrate the applications using the example metagraph in Figure 1, and the corresponding A and A\* matrices in Figures 2 and 3 $\pmb { A } ^ { * }$

We assume that variable names in different modules are compatible (that is, synonyms and homonyms do not exist). We recognize that naming incompatibilities can occur in practice. However, this problem is a general one in any model management approach, and can be dealt with either through manual arbitration or methods developed elsewhere (e.g., Bhargava et al. (1991)).

## 4.1. Directed Search

A common situation in practice is where the user (decision maker) wants to evaluate specific parameters, and wants to know what integrated models can be used to generate these parameters as outputs. The possibilities for this range from extraction of explicitly stored values in a database to instantiation and execution of one or more stored decision models. If the desired output parameters correspond to elements of the generating set of the metagraph for the DSS, then the available alternatives can be identified using the $\pmb { A } ^ { * }$ matrix. In the simplest case where there is a single output parameter, say X, the candidate integrated models correspond to the triples in the $\scriptstyle x _ { j }$ $\boldsymbol { x } _ { j }$ column of the A\* matrix, since these are all models that have x, as one of the outputs. $A ^ { * }$ $x _ { j }$ For instance, in the DSS corresponding to the metagraph in Figure 1, if the desired output is the manufacturing capacity c, this can be computed using the Prd module. $\pmb { c } ,$ given the value of the production volume v. It can also be obtained using the combination of Mkt and Prd, given the values of price p and economic indicator i. Note that $\mathbf { \nabla } : \pmb { p }$ this information is readily obtained from the c column of the corresponding $A ^ { * }$ matrix in Figure 3.

In the more general situation where more than one output parameter is desired (say, the set $X _ { 2 } ) _ { : }$ , then the applicable integrated models correspond to combinations of triples in the columns indexed by elements of $X _ { 2 } ,$ such that at least one triple from each such column is chosen. Thus, if the output parameters of interest were m and $r ,$ then any set of modules that appear in the path component of triples in the two columns $( m , r ,$ respectively) of the $A ^ { * }$ matrix would qualify. We see that two out of the three triples in the m column are qualifying candidates corresponding to the modules Mkt and Prd. The cooutput set of either triple includes $\pmb { r } ,$ and thus, even without examining the r column, we can conclude that these triples are valid choices. Note that in cases where there are several such combinations, additional factors such as the number of modules in each combination, the computational complexity of the modules, and their reliability, can be used to choose between them. Although in this paper, we do not address the consideration of such factors, they can also be incorporated in a metagraph-based approach by supplementing the metagraph edges with appropriate attributes (see Liang (1988), Jones (1990, 1991), Schocken and Jones (1993) for examples of such an approach using directed graphs).

An alternative situation is where the user would like to know what can be computed from given specific parameters. For example, the user might know the production capacity of a plant, applicable labor rates and average processing time for the product, and would like to know what other parameters can be computed from this. Again, the $\ b { A } ^ { * }$ matrix can be used to address this question. Since any parameter $x _ { j }$ that is affected by a specific parameter $x _ { i }$ must have a nonnull triple in $\pmb { a } _ { i j } ^ { * } ,$ for every set of parameters $X _ { 2 }$ that can be computed given values for a set of elements $X _ { 1 }$ , there is a metapath from $X _ { 1 }$ to $X _ { 2 }$ in the corresponding metagraph. Furthermore, we know from §3 that any triple occurring in a metapath from $X _ { 1 }$ must be in $\pmb { a } _ { i j } ^ { * }$ for some $x _ { i }$ $\in X _ { 1 } .$ . Thus, any combination of such triples such that the inputs net of the outputs is a subset of $X _ { 1 }$ is a qualifying metapath, and the union of the outputs of the triples forms a set of parameters that are determined by $X _ { 1 } .$

From Figure 3, we see that given values for the two parameters c and ${ \mathfrak { v } } ,$ corresponding to volume and capacity respectively, we can compute values for m and s. Note that c and v are not sufficient for computing ${ \pmb g } ,$ n and $\pmb { r } ,$ even though the corresponding cells in $A ^ { * }$ are nonempty. The reason for this is that the triples in those cells include coinputs other than c and v.

## 4.2. Integrated Models for Specific Inputs and Outputs

A more constrained but common situation is where the user knows the values of a set of parameters $X _ { 1 } ,$ and would like to compute the values of another set $X _ { 2 } 、$ . Since any integrated model for which $X _ { 1 }$ is sufficient to compute all the elements of $X _ { 2 }$ must correspond to a metapath from $X _ { 1 }$ to $X _ { 2 } ,$ the $\pmb { A } ^ { * }$ matrix can be used to identify alternative candidate integrated models. Furthermore, since the only triples that need to be considered are those in cells $a _ { i j } ^ { * }$ such that $x _ { i } \in X _ { 1 }$ and $x _ { j } \in X _ { 2 } ,$ , the search for relevant metapaths can be limited to a specific and possibly small part of the $\ b { A } ^ { * }$ matrix.

In our example DSS, if the desired outputs are r and ${ \pmb S } _ { \pmb 5 }$ and the available inputs are p and ${ \mathfrak { v } } ,$ then we only need to examine the four cells $a _ { p r } ^ { * } , a _ { p s } ^ { * } , a _ { v r } ^ { * }$ and $a _ { v s } ^ { * } .$ The only qualifying integrated model is the set of modules {Ohd, Sls}. Note that this is not immediately obvious from the visual representation of the metagraph: of course. it would be even more difficult from a digraph or other alternative graphical visualization framework.

The above search can be further constrained in situations where the user wants to limit it to integrated models that necessarily exclude a specific module. Such situations may arise when a module is perceived to be highly undesirable, due to low accuracy, reliability, and/or usability, or high cost. The A\* matrix again provides a $A ^ { * }$ simple and intuitive basis, since now, any triples that have the undesirable edge in their path component can be excluded. For instance, if the variables i, p and s are $i , p$ known, and the desired outputs are n and r, and further, if we do not want to use the $\pmb { r } ,$ Acc module, then one possible integrated model is the set of modules {Frc, Mkt, Prd} (in fact, in this case it is the only model).

A somewhat similar situation is when the user wants to test the impact of a set of specific inputs X, on the relevant outputs (where $X _ { t }$ $\textstyle X _ { t } \subseteq X _ { 1 }$ , the set of known inputs). In other words, the qualifying metapaths must include X, in their inputs. In this case, the $X _ { t }$ combinations of triples that are eligible for consideration must include at least one triple from each row $\textstyle x _ { t } \in X _ { t }$ . Thus, if $X _ { t } = \{ m , v \}$ $X _ { 1 } = \{ i , m , p , v \}$ , and $X _ { 2 } = \{ g \}$ , then $\{ \mathbf { A c c } , \mathbf { S l s } \}$ is a valid integrated model—that is, an integrated model that will calculate $X _ { 2 }$ given only $X _ { 1 } .$ . On the other hand, $\left\{ \mathbf { A c c } , \mathbf { M k t } \right\}$ is not a valid integrated model, even though it represents a metapath from $X _ { 1 } 1 0 X _ { 2 } ,$ because it does not use ${ \mathfrak { v } } _ { \mathfrak { p } }$ which is one of the elements of $X _ { t }$

In situations where there are multiple integrated models that are potentially candidates for a given problem, a variety of factors must be used to choose among them; these factors include cost, efficiency, reliability, and generalizability. Consideration of such factors requires metagraphs with attributed edges, which is outside the scope of this paper.

## 4.3. Additional Benefits of Metagraphs in Model Integration

A useful consideration in model integration is whether there are one or more critical modules. In other words, if we want to compute X2 from X, $X _ { 2 }$ $X _ { 1 } ,$ are there any modules that have to be used, regardless of which integrated model is selected? Such critical modules can be easily identified from the A\* matrix, since they correspond to $A ^ { * }$ edges that are in every qualifying triple in the relevant cells (i.e., in rows correspond- $( \texttt { i . e . }$ ing to X1) of some column corresponding to X2 elements. For example, Acc is a $X _ { 1 } )$ $X _ { 2 }$ critical module for computing g (which is easy to see, since it is the only module with g in its outvertex). However, if we set $X _ { 1 } = \{ c , i , p \}$ , then so are Mkt and Prd, since they are in all qualifying triples (the second triples in a, and a, respectively). On the $\pmb { a } _ { i g } ^ { * }$ $\pmb { a } _ { p g } ^ { \ast }$ other hand, the module Sls is not a critical module.

Another issue that can arise, especially when updating the resources in the DSS. is testing the impact of excluding or dropping a specific module ek. Given the A\* ma- $\boldsymbol { e } _ { k } .$ $\pmb { A } ^ { * }$ trix, this is easily verified, by deleting any triples containing e, and then checking if $\pmb { e _ { k } }$ any cell aj becomes empty. This test can also be set within the scope of a specific set of $\pmb { a } _ { i j } ^ { * }$ outputs X2 (i.e., by checking whether any cell in the columns corresponding to $X _ { 2 }$ $X _ { 2 }$ become empty if the triples containing ek are deleted). Thus, in our example, if the $\pmb { e _ { k } }$ module Sls is removed, none of the parameters is rendered unreachable. However, if Prd is removed, then c and s (the latter if we assume that c is not provided) cannot be computed using any of the available modules.

Another useful feature of metagraphs, in the context of model representation, is that they facilitate information about coinputs and cooutputs to be maintained. For instance, it is common for a module to have a number of outputs. When modules are integrated into a model for a problem, these outputs are accumulated as the cooutputs of the paths through the different component modules. Thus, given an integrated model with a corresponding metapath, it is easy to compile the entire set of outputs generated by that model and its component modules, simply by computing the union of the cooutputs on all the component paths (as represented by triples in $\pmb { A } ^ { * } )$ . Here the two metapaths $M _ { 1 } , M _ { 2 }$ described earlier provide a striking contrast, since $M _ { 1 }$ produces just n as an output, while $M _ { 2 }$ produces the entire set $\{ c , g , m , n , r , s ,$ v} as outputs.

Similarly, even though a user may start with an assumption that a set of inputs $X _ { 1 }$ is needed to be able to compute the elements in $X _ { 2 } ,$ in fact there may be metapaths that do not utilize all these inputs. Again, it is easy to identify unnecessary inputs, simply by identifying those elements in $X _ { 1 }$ that are not in the union of the inputs of the triples in the metapath. Thus, while $M _ { 2 }$ might have been identified as a metapath from $\{ c , i ,$ $p \}$ to $\{ n \}$ . the parameter c is really not needed as an input for this integrated model.

## 4.4. Construction of Metapaths

In the above discussion, we have demonstrated how metagraph representation for DSS modules, and the $A ^ { * }$ matrix for such a metagraph can significantly facilitate many tasks in model integration. In this section, we show how the $A ^ { * }$ matrix can also be used to speed up the search for metapaths between given sets of inputs $X _ { 1 }$ and desired outputs $X _ { 2 }$

One of the biggest benefits of metagraph representation is that searches for metapaths can be localized to potentially small portions of the $\pmb { A } ^ { * }$ matrix. In effect, any metapath from $X _ { 1 }$ to $X _ { 2 }$ must consist of edges based on a combination of triples from cells $a _ { i j } ^ { * }$ such that $x _ { i } \in X _ { 1 }$ and $x _ { j } \in X _ { 2 }$ . This is a very useful property, since it reduces the search space from the entire metagraph to a potentially small subset of it. Furthermore, the efficiency of the search procedure now becomes a function of the number of simple paths between $X _ { 1 }$ and $X _ { 2 } ,$ rather than the size of the entire metagraph.

Another useful observation is that if there is a metapath from $X _ { 1 }$ to $X _ { 2 } ,$ , then there should be triples composed of these edges in $\ b { A } ^ { * }$ in every column j such that $x _ { j } \in X _ { 2 } .$ Also, in constructing metapaths from triples in $A ^ { * }$ , even though there is at least one triple in every output column of $A ^ { * }$ (columns corresponding to elements of $X _ { 2 } ) ,$ , it is not always necessary to examine all these triples explicitly. This is because the triples in the matrix include information about coinputs and cooutputs, which can be useful. Another observation is that if we always consider a minimal number of rows, then the metapaths obtained are always input dominant. Based on these, a simple heuristic procedure to construct a metapath from $X _ { 1 }$ to $X _ { 2 }$ can be used. The intuition behind the procedure can be explained as follows:

1. Select a candidate set of input rows I such that $x _ { i } \in X _ { 1 } \forall i \in I .$ Start with single rows, and repeat with larger sets progressively in successive iterations

2. I $\mathrm { f } \exists x _ { j } \in X _ { 2 }$ such that $a _ { i j } ^ { * } = \phi \forall i \in I ,$ , then there is no metapath from $\{ x _ { i } | i \in I \}$ to $X _ { 2 } .$ Return to step 1 and repeat with another candidate set I.

3. Find a candidate set of triples in cells $\pmb { a } _ { i j } ^ { * }$ such that $i \in I$ and $x _ { j } \in X _ { 2 }$ that comprises a cover for $X _ { 2 }$ (a cover for $X _ { 2 }$ is a set of triples $c$ such that $X _ { 2 } \subseteq \cup _ { c \in C }$ path(c)). If such a cover is found, then it comprises an input dominant metapath from $X _ { 1 }$ to $X _ { 2 }$ (or actually from $\{ x _ { i } | i \in I \}$ to $X _ { 2 } ) ;$ Stop.

## 4. Otherwise, return to step 1 for an alternative candidate set I.

This procedure is a slight modification of the metapath construction procedure described in §3. By following a conservative strategy represented by step 1, it identi- $\ S 3 .$ fies input-dominant metapaths. Also, this strategy results in the initial iterations being relatively quick, since they consider smaller sets of triples.

ExAMPLE. For the metagraph in Figure 1, if $X _ { 1 } = \{ c , m , r \}$ and $X _ { 2 } = \{ n \}$ , the procedure progresses as follows:

ITERATION 1: $I = \{ c \} , a _ { c n } ^ { * } \neq \emptyset ,$ , no cover found in step 3.

ITERATION 2: $I = \{ m \} , a _ { m n } ^ { \ast } \neq \emptyset$ , no cover found in step 3.

ITERATION 3: $I = \{ r \} , a _ { r n } ^ { * } \neq \emptyset _ { \cdot }$ , no cover found in step 3.

ITERATION 4: $I = \{ c , m \} , ( a _ { c n } ^ { * } \cup a _ { m n } ^ { * } ) \neq \emptyset$ , the two triples $\langle \{ g \} , \{ s \} , \langle 0 \mathrm { h } \mathrm { d } , \mathrm { F i n } \rangle \rangle$ and $\langle r , s \} , \{ g \} , \langle \mathbf { A c c } , \dot { \mathbf { F i n } } \rangle \rangle$ form a cover for $X _ { 2 } ,$ and thus $\{ \mathbf { A c c } , \mathbf { F i n } , \mathbf { O h d } \}$ is an input-dominant metapath for the given $X _ { 1 }$ and $X _ { 2 } ,$ □

As mentioned earlier, the advantage of using a procedure such as the above is that it exploits the properties of metapaths and the A\* matrix to significantly reduce the $\pmb { A } ^ { * }$ complexity of the metapath construction process, as compared to a traditional search procedure such as backward or forward search. Thus, the A\* matrix is a useful way to $\pmb { A } ^ { * }$ organize structural information about the data and model resources in the DSS, and to utilize it in addressing different model integration tasks.

## 5. Conclusion

Model integration can be a difficult unstructured process, especially in a DSS containing a large number of modules. While automation of model integration is clearly beyond the state of the art today, we have shown in this paper that useful insight into the input/output relationships between modules can be gained through their metagraph representation, and structured procedures for identification of candidate integrated models for specific user problem instances can be constructed. Furthermore, we believe that information gained through metagraph analysis can be augmented with other economic and subjective considerations to achieve a comprehensive model integration process. One possible approach is the use of attributed metagraphs, in which edges are labelled with internal attributes of modules such as cost, reliability and efficiency.

The metagraph approach introduces three important and useful concepts—the notion of coinputs and cooutputs, the concept of a metapath, and the A and $\pmb { A } ^ { * }$ matrices; these concepts have not been explicitly developed and used in any existing approaches. Also, the metagraph approach is complementary to many of the existing approaches to model integration such as relational model management and the knowledge-based system approach (for instance, the use of metagraphs in rule-base management has been described in Basu and Blanning 1993). Thus, it serves as a useful extension to the existing body of research based on these approaches as well.

There are additional research issues in the theory of metagraphs and their application to systems analysis. These include the further development of metagraph theory in terms of properties such as planarity, duality and connectedness, and analysis of cyclic behavior in metagraphs. Some of the properties of metapaths, such as input dominance and edge dominance, may also have interesting and useful applications. For instance, if there are two integrated models that can be used to compute a set of parameters $X _ { 2 } ,$ corresponding to the metapaths $M _ { 1 } ( X _ { 1 } , X _ { 2 } )$ and $M _ { 2 } ( X _ { 1 } , X _ { 2 } )$ , then $\mathrm { i f } X _ { 1 }$ $\subset X _ { 1 } ,$ it may be desirable to choose $M _ { 1 }$ since it requires fewer inputs than $M _ { 2 } ( \mathbf { i } . \mathbf { e } . , M _ { 1 }$ input-dominates $M _ { 2 } )$ . Of course, input dominance is a desirable but not sufficient property, since the input dominant metapath may be poorer in other respects, as shown in the following example. Consider the following two metapaths (and thus integrated models) from $X _ { 1 } = \{ c , i , p \}$ to $X _ { 2 } = \{ \mathfrak { n } \}$

$$
M _ {1} = \{\text { Frc } \}, \quad M _ {2} = \{\text { Acc,   Fin,   Mkt,   Ohd,   Prd } \}.
$$

$M _ { 2 }$ is formed by combining the triples

$$
\begin{array}{r l} & {\langle \{m, p, s \}, \{g, r, v \}, \langle \mathrm{Mkt}, \mathrm{Sls}, \mathrm{Acc}, \mathrm{Fin} \rangle \rangle \quad \text { and }} \\ & {\langle \{g, p \}, \{c, m, r, s, v \}, \langle \mathrm{Mkt}, \mathrm{Prd}, \mathrm{Ohd}, \mathrm{Fin} \rangle \rangle} \end{array}
$$

in $\pmb { a } _ { i n } ^ { * } .$ While $M _ { 1 }$ appears simpler, since it only has one component module, actually $M _ { 2 }$ is input dominant, since it only requires i and $\pmb { p }$ as inputs. This also demonstrates that in general, individual criteria such as size of integrated model (in terms of number of components, or even complexity of individual modules) and input dominance may not be adequate determinants of choice between integrated models by themselves.

Also, in terms of applications, the use of metagraphs for representation of hierarchical systems and the use of metagraph transformations (such as aggregation, reduction and decomposition) to multilevel systems analysis are particularly interesting. Finally, the ability to visualize a system in terms of its metagraph representation, combined with the analytical procedures enabled by this representation, motivate the development of a computer-based tool based on metagraphs. We are currently working on the development of such a tool, for both database system design as well as model integration in DSS.\*

Acknowledgement. This research was supported by the Dean's Fund for Faculty Research of the Owen Graduate School of Management of Vanderbilt University.

\* Daniel R. Dolk, Associate Editor. This paper was received on June $^ { 1 2 , }$ 1992, and has been with the authors 11 months for 2 revisions.

Appendix: Proofs of Theorems

THEoREM 1. A metapath is edge-dominant iff each of its edges is nonredundant

PRooF. Since the metapath is nonredundant, removal of any of its edges will result in at least one of the elements B being disconnected from A. Thus, every edge is essential for the metapath, which is thus edge-dominant. Q.E.D.

TíeOREM 2. Let A & B be two disjoint sets of elements in a metagraph such that $A \to B .$ If there is no bridge between A and $\mathbf { { \delta } } _ { \mathbf { { \delta } } } \mathbf { { \delta } } _ { \mathbf { { \delta } } } \mathbf { { \delta } } _ { \mathbf { { \delta } } } \mathbf { { \delta } } _ { \mathbf { { \delta } } } \mathbf { { \delta } } _ { \mathbf { { \delta } } }$ then there are at least two edge-dominant metapaths from A to B.

PROOF. Since ${ \pmb A }  { \pmb B } ,$ there has to be at least one edge-dominant metapath (say $M _ { 1 } )$ from A to B. However, none of the edges in $\pmb { M _ { 1 } }$ are bridges, so $\pmb { A }  \pmb { B }$ (say through metapath $M _ { 2 } )$ even if any single edge $e _ { i } \in M _ { 1 }$ is removed. However, since $M _ { 1 }$ is edge-dominant, $M _ { 2 } \not \in M _ { 1 }$ Since every metapath can be reduced to an edge-dominant metapath, it follows that $M _ { 2 }$ can be reduced to an edge-dominant metapath from A to B that is distinct from $M _ { 1 } ,$ which proves the result. Q.E.D.

THEOREM ${ \mathfrak { s } } .$ Given a generating set $\pmb { \chi } ,$ a metagraph $\pmb { S } = \langle \pmb { X } , \pmb { E } \rangle$ , two disjoint sets $A , B \subseteq X$ such that $\pmb { A }  \pmb { B } ,$ and a bridge e between A and B:

1. For any set $c \leqslant X$ such that $\pmb { A }  \pmb { C }$ and $C \to B ,$ e is a bridge between either A and $^ { c , }$ or between C and B.

$2 , I f M _ { 1 } , M _ { 2 }$ are two metapaths from A to $\pmb { B } ,$ then $e \in M _ { 1 } \cap M _ { 2 }$ and thus, no two metapaths from A to B are edge-disjoint.

3. For any two sets A', B' such that $A ^ { \prime } \to B ^ { \prime } , A ^ { \prime } \subseteq A$ and $B \subseteq B ^ { \prime } ,$ e is a bridge between A' and B'.

PRooF (Part 1) Proof by contradiction. Assume that e is not a bridge between either A and C, or C and B This implies that in the metagraph $S _ { 1 } = \langle X , E \setminus \{ e \} \rangle$ , we still have $\pmb { A }  \pmb { C }$ and $C  B ,$ and thus $\pmb { A }  \pmb { B } ( \mathbf { \hat { o } y }$ the lemma). This in turn implies that e is not a bridge between A and B.

(Part 2) Since e is a bridge between A and B, it must occur in every metapath from A to B: hence $e \in M _ { 1 }$ $\cap M _ { 2 } ,$ and the result follows.

(Part 3) Proof by contradiction. Note that a metapath from A' to B' is also a metapath from A to B. Thus. if there is no bridge between A' and B', then there must be at least one metapath from A' to B' (and hence between A and B) in $S _ { 1 } = \langle X , E \backslash \{ e \} \rangle$ >, which implies that e is not a bridge between A and B. O.E.D.

## References

Ackermann, William B., "Data Flow Languages," IEEE Computer, 15, 2 (February 1982), 15–24

Banerjee, Snehamay and Amit Basu, "Model Type Selection in an Integrated DSS Environment." Decision Support Systems, 9, 1 (1992), 75–89.

Basu, Amit and Robert W. Blanning, “Enterprise Modeling Using Metagraphs," in Decision Support Systems: Experiences and Expectations, T. Jelassi, M. R. Klein, and W. M. Mayon-White (Eds.). Elsevier, NY, 1992(a).

- and “A Graph-Theoretic Approach to Analyzing Knowledge Bases Containing Rules, Models and Data," Working Paper, Owen Graduate School of Management, Vanderbilt Univ. Nashville, TN, 1993.

- and , "Metagraphs: A Tool for Modeling Decision Support Systems," Management Science (to appear), 1994.

Berge, Claude, Graphs (2nd Ed.), North-Holland, Amsterdam, 1985.

, Hypergraphs, North-Holland, Amsterdam, 1989.

Bhargava, Hemant K., Stephen Kimbrough, and Ramayya Krishnan, “Unigue Names Violations: A Problem for Model Integration or You Say Tomato, I Say Tomahto," ORSÀ Journal of Comnuting 3 2 (1991), 107–121.

Binbasioglu, Meral and Matthias Jarke, "Domain Specific DSS Tools for Knowledge-Based Model Build. ing," Decision Support Systems, 2, 3 (September 1986), 213–223.

Blanning, Robert W., "A Relational Framework for Join Implementation in Model Management Svstems," Decision Support Systems, 1, 1 (January 1985), 69–82

Bonczek, Robert H., Clyde W. Holsapple, and Andrew B. Whinston, "Data Base Management Techniques for Mathematical Programming," Proceedings of the SIGMAP Bicentennial Conference on Mathematical Programming, November 1976.

, Foundations of Decision Support Systems, Academic Press, Orlando, FL, 1981.

Brennan, J. J. and J. J. Elam, "Understanding and Validating Results in Model-Based Decision Support Systems," Decision Support Systems, 2 (1986), 49–54.

Chen, Peter P., “The Entity-Relationship Model: Toward a Unified View of Data." ACM Transactions on Database Systems, 1, 1 (March 1976), 9–36.

Date, C. J., An Introduction to Database Systems, Vol. I (5th Ed.) Addison-Wesley, Reading MA 199o

Davis, Alan L. and Robert M. Keller, "Data Flow Problem Graphs," IEEE Computer, 15, 2 (February 1982), 26–41.

Dennis, Jack B., "Data Flow Supercomputers," IEEE Computer, 13, 11 (November 1980), 48–56. 48 -30

Dutta, Amitava and Amit Basu, “An Artificial Intelligence Approach to Model Management in Decision Support Systems," IEEE Computer, 17, 9 (September 1984), 89–97.

Finlay, P. N. and J. M. Wilson, "The Paucity of Model Validation in Operational Research Projects." Journal of the Operational Research Society, 38, 4 (1987), 303–308.

Gallaire, Herve and Jack Minker (Eds.), Logic and Data Bases, Plenum Press, NY, 1978.

Geoffrion, Arthur M., "An Introduction to Structured Modeling," Management Science, 33, 5 (May 1987), 547–588.

"FW/SM: A Prototype Structured Modeling Environment," Management Science, 37. 12 (Dec. 1991), 1513–1538.

, "Reusing Structured Models via Model Integration," in Current Research in Decision Suppor Technology, Robert W. Blanning and David R. King (Eds.), IEEE Computer Society Press, Los Alamitos, CA, 1992, 25–55.

Greenberg, Harvey J. and John S. Maybee, Computer-Assisted Analysis and Model Simplification. Academic Press, New York, 1981.

Harel. David, “Statecharts: A Visual Formalism for Complex Systems," Science of Computer Programming, 8 (1987), 231–274. ming, 8 (1987), 231–274.

"On Visual Formalisms," Communications of the ACM, 31, 5 (May 1988), 514–530. On

Hagi Lachover, Amnon Naamad, Amir Pnueli, Michal Politi, Rivi Sherman, and Aharon Shtull-Tauring, "STATEMATE: A Working Environment for the Development of Complex, Reactive Systems." Proceedings of the Tenth IEEE International Conference on Software Engineering, Síngapore, April 1988. pore

Rivi Sherman. Aharon Shtull-Tauring, and Mark Trakhtenbrot, “STATEMATE: A Working Environment for the Development of Complex, Reactive Systems," IEEE Transactions on Software Engineering, 16, 4 (April 1990), 403–414.

Heydon, Allan, Mark W. Maimone, J. D. Tygar, Jeannette M. Wing, and Amy M. Zaremski, "Miro: Visual Specification of Security," IEEE Transactions on Software Engineering, 16, 10 (October 1990), 1185-1197. 1185-1197.

Huber, George P., “The Nature and Design of Post-Industrial Organizations," Management Science, 30, 8 (August 1984), 918–951. (August 1984), 918

Jones. Christopher V., “An Introduction to Graph-Based Modeling Systems, Part I: Overview," ORSA Journal on Computing, 2, 2 (Spring 1990), 136–151. Journal on Computing, 2, 2

"An Introduction to Graph-Based Modeling Systems, Part II: Graph Grammars and the Implementation," ORSA Journal on Computing, 3, 3 (Summer 1991), 180–206. mentation,

Kottemann. Jeffrey E, and Daniel R. Dolk, "Model Integration and Model Languages: A Process Perspective," Information Systems Research, 3, 1 (March 1992), 1–16. tive," Informai

Krishnan, Ramayya, "PDM: A Knowledge-Based Tool for Model Construction," Decision Support Systems. 7. 4 (November 1991), 301–314. tems.

Peter Piela, and Arthur Westerberg, "Reusing Mathematical Models in ASCEND," in Recent Developments in Decision Support Systems, Clyde W. Holsapple and Andrew B. Whinston (Eds.), Springer-Verlag, Berlin, 1993, 275–293. Springei

Liang, Ting-Peng. "Development of a Knowledge-Based Model Management System," Operations Research 36. 6 (Nov,-Dec. 1988), 849–863. 99

Ma. Pai-Chun, Frederic H. Murphy, and Edward A. Stohr, "Semantic Structures in Linear Programs," Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, Vol III: Decision Support and Knowledge-Based Systems Track, January 1989, 459–466.

Mills, Harlan D., Richard C. Linger and Alan R. Hevner, Principles of Information Systems Analysis and Design, Academic Press, Orlando, FL, 1986.

Muhanna, Waleed A, and Roger A. Pick, "Meta-Modeling Concepts and Tools for Model Management: A Systems Approach." Working Paper, College of Business, The Ohio State University, Columbus, OH, 1993. 1993.

and. "Composite Models in SYMMS," Proceedings of the 21st Hawaii International Conference on System Sciences, Vol. III, Jan. 1988, 418–427. Conference on Syste

"SYMMS: A Model Management System That Supports Reuse, Sharing and Integration," to appear in European Journal of Operational Research, 72, 2 (January 1994), 214–242. appear in Europea

Robinson, J. Alan, "A Machine Oriented Logic Based on the Resolution Principle," Journal of the ACM, 12. 1 (January 1965), 23–41. 12. 1 (January 1965), 23–41.

“Logic and Logic Programming," Communications of the ACM, 35, 3 (March 1992), 40–65.

Schneeweiss, C., "On the Formalization of the Process of Quantitative Model Building," European Journal of Operational Research, 29 (1987), 24–41. of Operatione

Schocken, Shimon and Christopher Jones, "Reframing Decision Problems: A Graph-grammar Approach." Information Systems Research, 4, 1 (March 1993), 55–87.

Senn. James A., Analysis and Design of Information Systems, (2nd Ed.), McGraw-Hill, New York, 1989.

Sprague, Ralph H., Jr, and Hugh J. Watson, "Model Management in MIS," Proceedings of the Seventeenth National AIDS. November 1975, 213–215.

Thakkar, S. S. (Ed.), Selected Reprints on Dataflow and Reduction Architectures, IEEE Computer Society Press. 1987,

Ullman, J. D., Principles of Database and Knowledge-Base Systems, Voł. 1, Computer Science Press, Rockville, MD, 1988. Rock

Will, Harmut J., “Model Management Systems," in Information Systems and Organization Structure, E. Grochla and N. Szyperski (Eds.), Walter de Gruyter, Berlin, 1975, 468–482.

Wing, Jeannette M., "A Specifier's Introduction to Formal Methods," IEEE Computer, 23, 9 (September 1990), 8–24.
