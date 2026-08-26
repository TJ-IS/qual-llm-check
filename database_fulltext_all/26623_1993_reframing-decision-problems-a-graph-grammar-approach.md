---
otero_id: 26623
otero_key: "SXSAESCV"
title: "Reframing Decision Problems: A Graph-Grammar Approach"
authors: "Shimon Schocken; Christopher Jones"
year: "1993"
journal: "Information Systems Research"
doi: "10.1287/isre.4.1.55"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/SXSAESCV/fulltext/images/57f2f14cc245a5eddbf8c81ffc6bc721c5b3ea7d49a1ef62181a5fb40d95f908.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Reframing Decision Problems: A Graph-Grammar Approach

Shimon Schocken, Christopher Jones,

To cite this article:

Shimon Schocken, Christopher Jones, (1993) Reframing Decision Problems: A Graph-Grammar Approach. Information Systems Research 4(1):55-87. http://dx.doi.org/10.1287/isre.4.1.55

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1993 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/SXSAESCV/fulltext/images/b9edb1d16a2234c8215ea30a898a3e5a52c2379eb6ed62b82065e8c879832eee.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Reframing Decision Problems: A Graph-grammar Approach

Shimon Schocken

Stern School of Business

New York University

Christopher Jones

New York, New York 10006

Faculty of Business Administration

Simon Fraser University

Burnaby, British Columbia

Canada V5A 1S6

One fundamental requirement in the expected utility model is that the preferences of rational persons should be independent of problem description. Yet an extensive body of research in descriptive decision theory indicates precisely the opposite: when the same problem is cast in two different but normatively equivalent “frames," people tend to change their preferences in a systematic and predictable way. In particular, alternative frames of the same decision-tree are likely to invoke different sets of heuristics, biases and risk-attitudes in the user's mind. The paper presents a modeling environment in which decision-trees are cast as attributed-graphs, and reframing operations on trees are implemented as graph-grammar productions. In addition to the basic functions of creating and analyzing decision-trees, the environment offers a natural way to define a host of“debiasing mechanisms" using graphical programming techniques. Some of these mechanisms have appeared in the decision theory literature, whereas others were directly inspired by the novel use of graph-grammars in modeling decision problems. The modeling environment was constructed using NETwORKS, a new model management system based on a graph-grammar formalism. Thus, a second objective of the paper is to illustrate how a general-purpose modeling environment can be used to produce, with relatively little effort, a specialized decision support system for problems that have a strong graphical orientation.

Descriptive decision theoryDecision-trees—Decision-making under uncertainty—Graph-grammars—Model management-Model management systems

## 1. Introduction

esearchers and practitioners of management science use a variety of graphical Laides to'represent and analyze complex problems. Indeed, there exist many situations in which “a picture is worth a thousand words," as the familiar saying proclaims. Examples include PERT/CPM graphs, data-flow diagrams, influence diagrams, semantic networks, decision-trees, and game-trees. From a functional standpoint, the above representations are quite different from each other. Yet from a topological or syntactical perspective, they can all be seen as different instances of the same class. In particular, they are all special cases of attributed-graphs—graphs whose nodes and edges can be partitioned into different types.

Decision-trees represent an especially interesting case of attributed-graphs, because the mapping from decision problems to graphs is not unique: more often than not, the same decision problem can be cast in terms of several decision-trees that are topologically different, yet normatively equivalent. For example, consider a twostage gamble in which the first stage offers even chances to proceed to a second stage, in which there is an 80% chance of winning \$100 and a 20% chance of winning nothing. Viewed as a decision-tree, this prospect can be cast in two different ways. First, one can follow the given scenario and depict a 50/50% chance-node, leading to a second 80/20% chance-node of winning \$100. Alternatively, one can depict a single 40/60% chance-node of winning 100\$. Since both prospects entail precisely the same economic reward, rational agents should be willing to pay, at least in theory, the same amount of money to buy them. Yet experiments in descriptive decision theory reveal that the first representation tends to induce a more risk seeking behavior (Tversky and Kahneman 1974), a point which is taken up later in the paper. As Thaler (1980) has shown, such reframing biases can be used to manipulate consumer behavior in a wide range of examples.

In this paper, we define reframing operations as editorial manipulations that transform a tree t into a tree t' in such a way that leaves both trees normatively equivalent, i.e., U(t) = U(t'), U being a standard Von-Neumann Morgenstern utility function. The notions of reframing and equivalence in decision-trees have been discussed in the literature both from a normative perspective (Thompson 1972, Lavalle 1978, Lavalle and Fishburn 1987, Lavalle and Wapman 1986), as well as from a descriptive perspective, most notably by Tversky and Kahneman (1981). The normative approach, which is based on the standard “roll back" procedure for evaluating decisiontrees, focuses primarily on the axiomatic validity of various reframing operations. This approach describes how a rational person who follows the axioms of subjective probability and utility theory should evaluate the risky prospects that the tree represents.

It is an embarrassing fact of reality, however, that most decision-makers, experts and laymen alike, exhibit systematic violations of the classical axioms. This phenomenon, which was detected in numerous experiments, gave rise to a descriptive, or behavioral, branch of decision theory. This line of research concerns not how rational people ought to behave, but rather how ordinary people actually behave, when dealing with uncertain prospects and risky decisions. In particular, it has been shown that different (but normatively equivalent) frames of the same decision-tree invoke different sets of cognitive biases, leading to decision-making behavior which is often inconsistent with what expected utility theory would predict.

Our own treatment of reframing is based on the premise that users of decision-trees are not automatons, but rather human beings, guided by bounded rationality and equipped with limited computational devices (Simon 1957). Following Tversky and Kahneman (1981), we assume that users (a) will be unaware of the existence of alternative tree representations, (b) will not be willing to go through the trouble of constructing such presentations, and (c) will be incapable of comparing the impact of different (but normatively equivalent) representations on their decisions. The need for decision support arises here because “there is a human tendency to act on the most readily available frame, which may be attributed to the mental effort required to explore other alternatives." In order to address these problems, we have developed a formalism and a system that enables users to not only build and edit decision-trees graphically, but also detect the potential biases that certain tree patterns induce, and, if the user so desires, manipulate the trees in such a way that promotes reasoned and well-informed decisions. The system has been implemented in NETwORKS, an extended implementation of the graph-grammar formalism of Nagl (1976, 1987) and Göttler (1979, 1983, 1987). Built by Jones (1990) to facilitate rapid creation of graph-based models, NETwoRKs is a novel generator of model management environments. Hence, in addition to the decision theoretic theme of the paper, we also wish to expose the reader to the benefits and limitations of the graph-grammar approach to modeling, using decision-trees as a familiar domain of application.

Two points are in order here. First, we do not claim that graph-grammars provide a universal solution to all the biases reported in the literature, but rather to a limited (albeit critically important) set of distortions that emerge in certain manipulations of decision-trees. Our research does not address many other biases, e.g., insufficient adjustment, illusory correlation, misconceptions of regression, and insensitivity to predictability (Kahneman, Slovic and Tversky, 1982) that do not lend themselves naturally to a decision-tree analysis. We strongly believe that graphical aides can and will play a major role in correcting these distortions as well, but we do not make this claim in the present paper. Second, although we propose that our debiasing mechanisms can significantly ameliorate the adverse impact of certain biases, the effectiveness of our approach has not been tested empirically with human subjects. We will return to this validation issue in the discussion section, where we outline the experiments that can be carried out to test the debiasing potential of our approach.

The plan of the paper is as follows. The remainder of this section gives a brief overview of the NETwoRKS environment and user-interface. Section 2 presents a graph-grammar formalism for defining and evaluating decision-trees. Section 3 describes graph-grammar productions for building and maintaining decision-trees. This material sets the stage for §4, which describes graph-grammar productions for reframing decision-trees and presenting the same problems from different perspectives. Section 5 summarizes the research and outlines future research directions.

## The NETWORKS System

NETwoRKs is a generator of modeling environments for models that have a strong graphical orientation. The NETwoRKS approach to modeling is unique in that both models and operations on models are implemented as instances of the same type of object: attributed-graphs. This uniformity of expression provides extreme flexibility in terms of archiving, retrieving and combining models and meta-models of different types and purposes. The general architecture of the NETwoRKS environment is depicted in Figure 1, and a snapshot of its user-interface is depicted in Figure 2.

Like other modeling environment, NETwoRKs has two types of stakeholders: designers and users. The designer is the person who builds a specialized modeling environment for a certain family of models, say vehicle routing. The user (e.g., a transportation analyst) is the person who uses the environment to define, manipulate and solve specific transportation models. The designer must have some basic understanding of the user's world, but the user need know nothing about the world of graph-grammars. As far as the user is concerned, the modeling environment consists of an intelligent scratch pad that “understands" what it takes to build and analyze models in a certain, specialized domain. The intelligence of the system is embedded in a set of domain-specific productions, or graphical operators. For example, a specialized environment for vehicle routing will consist of a library of productions designed to assist transportation analysts and dispatchers in their typical tasks, e.g., adding and deleting customers, rerouting sub-tours, changing capacity and demand constraints, etc. These productions will be written in the NETwoRKs language by the system's designer, and will be available to the system's users through a windows-based GuI (graphical user-interface).

Schocken • Jones  
![](/api/attachments/SXSAESCV/fulltext/images/36badccf37dbed2fd43a0fb463d0b27d7ef5bc53b8ea52e3317352d5a0d9930c.jpg)  
FiGURE 1. The 'World of NETwoRKs :' the general development environment (bottom block) can be used to create a variety of specialized modeling environments, like the decision-trees package enclosed in the vertical block. Through this package, an end-user who knows nothing about NETwoRks can create and maintain a library of decision-tree models. All the models and the productions are archived in a modelbase and in a productions-base, respectively, which are managed by a model-management module (the vertical block on the left).

The uninitiated reader is advised that the graph-grammar formalism entails programming and modeling styles which are quite different from those of conventional languages. This formalism will be presented below gradually, as it unfolds in the context of constructing a graphical modeling environment for decision-trees. The environment, which is essentially a collection of graph-grammar productions, offers all the conventional services for building and analyzing decision-trees, as well as novel reframing techniques that were directly inspired by the graph-grammar formalism.

## 2. The Modeling Formalism

This section describes decision-trees as a special case of attributed-graphs. We seek such a definition not for formality's sake, but as a practical foundation for carrying out decision-theoretic analyses as graphical operations, using the language of graphgrammars.

![](/api/attachments/SXSAESCV/fulltext/images/50b07af4f4b8f73a886505bdfb274417c04691f463dc01c16f0638c66903946b.jpg)  
FiGURE 2. A Snapshot of a Typical NETwoRKs Session. The windows in the background contain two different, and possibly unrelated, target-graphs. The window in the foreground contains the productiongraph of con , shown also in Figure 11. The choice of the three graphs and the positioning of the windows are arbitrary.

A decision-tree graph is a directed, acyclical graph that consists of three types of nodes, denoted hereafter choice, chance and outcome, and of two types of edges, denoted hereafter echance and echoice. Choice nodes represent choices among alternative courses ofaction (echoice edges), whereas chance nodes represent different outcomes of random events (echance edgès). Outcome nodes represent final gains and losses, typically expressed in terms of monetary values or utilities. A typical decision-tree is illustrated in Figure 3. In the figure, each graph object (node or edge) is characterized by a set of domain attributes, e.g., value and probabi1- ity, and a set of graphical attributes, e.g., shape and size. The latter attributes are used to control the display characteristics of the graph. For example, in the case of decision-trees, we have set the shape attribute of every choice, chance, and outcome-node to the values rectangle, circle and diamond, respectively. These attributes cause NEtwoRKs to draw the corresponding objects in the specific shapes that appear in Figure 3.

## The Graph-Database

Each attributed-graph has an internal representation which we call the graph-database. The graph-database is a collection of node and edge terms, written in a Prologlike syntax. Specifically, each node in the graph is uniquely identified by the term node(GraphID, NodeID, NodeType), representing the graph-identifier, the node-identifier, and the node-type, respectively (the existence of the first argument

Schocken • Jones

![](/api/attachments/SXSAESCV/fulltext/images/e5a377a88e19b5f1c23fac1180add5ebb9781f9ab8b3aa9ba8a7a97c6764a9a4.jpg)  
FiGuRE 3. Left: A decision-tree that represents a familiar (and repetitive) urban dilemma: should I put money in the parking-meter? Parking-meters provide steady municipal revenues because most people prefer to pay, say, \$1 to avoid an expected loss of, say, \$10. Right: The same tree as an attributed-graph consisting of nine typed objects.

allows the system to manipulate multiple graphs, or models, simultaneously). Similarly, each edge is uniquely identified by the term edge (GraphID,EdgeID, EdgeType, FromNodeID, ToNodeID) , the two latter arguments referring to the nodes connected by the edge.

For example, the graph-database that drives the decision-tree depicted in Figure 3 is as follows:

node(treel,nodel,choice).

node(treel,node2,outcome).

node(treel,node3,chance).

node(treel,node4,outcome).

node(treel,node5,outcome).

edge(treel,edgel,echoice,nodel,node2).

edge(treel,edge2,echoice,nodel,node3).

edge(treel,edge3,echance,node3,node4).

edge(treel,edge4,echance,node3,node5).

(Throughout the paper, we follow the standard Prolog syntax for representing constants like tree1 by identifiers beginning with lower-case letters, and variables like GraphID by identifiers beginning with upper-case letters.)

It is important to emphasize that the graph-database is neither created, nor is it ever seen. by the model builder. The user draws his models on the screen through a graphical user-interface that manipulates node-images and edge-images directly. The graph-database is created and maintained by NETwORKS automatically, as a transparent side effect of the user's activities at the GuI level. Similarly, the software has the symmetric ability to convert graph-databases into bit-mapped images that the user can explore and edit through the GUI .

Unification. The node(·) and edge(•) terms play two different roles in the NETwoRKs implementation. In their “ground" version, when they involve constants only, thev serve as the building blocks of the graph-database, as seen above. In their “predicate" version, when they involve one or more variables, they are used to do pattern matching, Prolog-style (unification). This is illustrated in the following three examples, which refer to Figure 3.

ExAMPLE 1. The expression node (treel,node3,NodeType) will bind the variable NodeType to the type of node3 , which happens to be chance. In logic programming, such expressions are often used to "query" the values of variables terms beginning with upper-case letters

ExAMPLE 2. The expression node (treel,NodeID,outcome) will match all the outcome-nodes in treel by repetitively binding the variable NodeID to the labels node2, node4 and node5.

EXAMPLE 3. The expression edge (treel,-,—,node3,NodeID) will match all the children-nodes of node3, i.e., node4 and node5 . The two underscore characters indicate that in this particular predicate, the arguments EdgeID and Edge-Type are immaterial, meaning that they are allowed to match anything.

Attributes. Different node-types and edge-types are characterized by different sets of attributes, designed to capture the specific nature of the graph in question. In the case of decision-trees, nodes of type chance, choice and outcome are characterized by the attributes label , which represents the node's name, and value , which represents the current (expected) value of the sub-tree rooted at that node. Edges of type echoice are characterized by a single 1abel attribute, whereas edges of type echance are characterized by a label and a probability attribute.

To retrieve the attribute values of specific graph objects, one uses two general-purpose look-up functions: na (·) , for nodes, and ea (·) , for edges. The syntax of these functions is as follows:

$$
\text { na } (\text { AttributeID }, \text { GraphID }, \text { NodeID }, \text { NodeType })  ,\tag{1}
$$

$$
e a (A t t r i b u t e I D, G r a p h I D, E d g e I D, E d g e T y p e).\tag{2}
$$

The na(·) and ea(·) functions are designed to return values, much like function calls in a conventional language. For example, the function call ea(probability,treel,edge4,echance) will return the number 0.8—the probability associated with that edge (see Figure 3). In order to simplify the use of these functions, some of the variables in (1) and (2) are allowed to attain default values, representing the current-graph, the current-node and the current-edge. To illustrate, the function ea(probability,\*,\*,\*), or ea(probability) for short, returns the value of the probability attribute of the current-edge in the current-graph. The currency defaults are maintained automatically by NETwoRks.

The contents of an attribute can be either a constant, as in probability, or a formula, as in value . The formulas interact with other objects in the graph, resulting in a dynamic spread of activation similar to that of a spreadsheet program. (Unlike spreadsheet formulas, though, NETwORKs formulas understand the semantics of graph concepts.) To summarize, an attributed-graph is essentially a database of node and edge terms. These terms define a connected collection of typed objects, each characterized by a different set of user-defined attributes. The attribute values are computed “as-needed," to borrow a term from frame-oriented programming.

Formulas. The notion of graph-based formulas is central in our approach to modeling. In order to illustrate it, we describe how formulas are used to “evaluate" a decision-tree graph. First, recall that in a decision-tree, each sub-tree represents a prospect, or a lottery, whose outcome is governed by a known probability distribution. That is, the value attribute of each node x, denoted hereafter v(x), is set to the expected-value of the prospect represented by the sub-tree rooted at x. This value is calculated by “rolling the tree backward,"as follows. Suppose that x has $\pmb { n } \geq \mathbf { 0 }$ outgoing edges, leading to the children-nodes $x _ { 1 } , \ldots , x _ { n }$ . If x is an outcomenode $( \boldsymbol { n } \ = \ \mathbf { 0 } ) , \ \boldsymbol { v } ( \boldsymbol { x } )$ is a given constant. If x is a choice-node, v(x) is set to max $\{ v ( x _ { 1 } ) , \ldots \ldots , v ( x _ { n } ) \}$ , i.e., to the value of the course of action that offers the highest expected reward at the choice junction rooted in x. The graph-grammar implementation of this formula is:

$$
\text { imax } (\text { edge } (*, \text { Edge }, \text { echoice }, x, Y), \text { na } (\text { value }, *, Y, -)).\tag{3}
$$

(This formula will be explained shortly.) Finally, if x is a chance-node, v(x) is set to $\begin{array} { r } { \sum _ { j = 1 } ^ { n } p ( x , x _ { j } ) v ( x _ { j } ) } \end{array}$ , where $p ( x , x _ { j } )$ denotes the value of the probability attribute associated with the edge $( x , x _ { j } )$ This formula computes the expected-value of the random-variable represented by x. The graph-grammar implementation of this formula is:

$$
\begin{array}{l} \text { sum(edge(*,Edge,echance,x,Y)   ,} \\ \text { ea(probability,* ,Edge,echance)*na(value,* ,Y,-))   .} \end{array}\tag{4}
$$

In order to explain (3) and (4), we first have to say a few words about the general functions imax(P,V) and sum $( \mathbb { P } , \mathbb { V } )$ The indexed maximum function imax $( \mathbf { \nabla } \mathbb { P } , \mathbf { v } )$ computes the largest value of the expression V, given all the possible instantiations of the predicate P. In the particular case of (3), P stands for the predicate edge (\*, Edge, choice, x, Y) , which is repeatedly instantiated to all the children-nodes, i.e., Y, of x in the current-graph. For each such instantiation, na(value, $^ { * , \pmb { \mathrm { Y } } , } - \pmb { \mathrm { \ell } }$ returns the value attribute of the child-node Y . (The type of the child-node is immaterial here, a fact which is denoted by the underscore character, indicating that NodeType in (1) can match anything.) The glue that holds the two arguments edge (·) and na (·) together is the shared variable Y and the unification logic of Prolog. In a similar vein, the function sum $( \mathbf { \nabla } \mathfrak { P } , \mathbf { \ v } )$ accumulates the sum of the v values, given all the possible instantiations of the predicate P . In (4), this function is used to compute the expected-value of the random-variable represented by x, namely $\begin{array} { r } { \sum _ { j = 1 } ^ { n } p ( x , x _ { j } ) v ( x _ { j } ) } \end{array}$ . We leave it to the reader to verify that the declarative expression (4) indeed carries out this algebraic computation. Note that both formulas are recursive: the computation of v(x) propagates from x all the way down to the leaves of the sub-tree rooted at x, where outcome-nodes that carry constant values v(•) are encountered. Hence, we see that recursive operations on trees such as “averaging out"and “folding back"(Raiffa 1968, Howard 1968) lend themselves nicely to declarative programming, in general, and to the NETwORKs language, in particular. Now, the fact that a Prolog-like language can be used to represent a set of nodes and edges is well-known. What sets NETwORKS apart from conventional logic programs is its ability to understand (1) that the nodes and the edges have an important graphical interpretation; (2) that the nodes and the edges have an important modeling interpretation; and (3) that these two interpretations are tightly interrelated.

Productions. A production is a general purpose piece of code, designed to operate on a wide variety of target graphs. Formally, a production is a triplet $\pmb { \mathcal { P } } = \tilde { \langle } G ^ { L } , G ^ { R } , T \rangle ^ { 1 }$ . When applied to a target-graph $G , \mathcal { P }$ checks if there is a subgraph $\bar { G } ^ { \underline { { { \tau } } } } \subset { \sigma }$ which is isomorphic to $G ^ { L }$ . If such a subgraph is found $\pmb { \mathcal { P } }$ transforms G into a new graph, in which $\bar { G } ^ { \bar { L } }$ is replaced with $G ^ { R }$ . This operation consists of two conceptual steps, as follows. First, the subgraph $\bar { G } ^ { L }$ as well as additional nodes and edges in its boundary (the left-side) are removed from G in order to create room, or embed, the new subgraph $G ^ { R }$ . The result is a “temporary" graph, denoted ${ \cal G } \backslash \bar { \cal G } ^ { L } ( { \cal G }$ with $\tilde { G } ^ { L }$ removed). Next, $G ^ { R }$ as well as a new set of connecting edges (the right-side) are implanted in ${ \cal G } \backslash \bar { \cal G } ^ { L }$ . The exact details of this tricky surgery are specified by the production's embedding transformation, denoted here T.

The nodes and the edges of production-graphs are similar, but not identical, to the target-nodes and edges on which they operate. To begin with, each production-object (node or edge) is characterized by all the user-defined attributes of its corresponding (matched) target-object. However, the contents of the attributes are somewhat different at the production level. Specifically, when a new node or edge is added to a target-graph by a production, the production must specify the formulas that will “reside" in the target attributes of the new object. This is done through attribute transformation expressions, which are essentially meta-formulas, as they calculates target-formulas, rather than constant values.

Production-graphs differ from regular target-graphs in two more ways. First, in addition to the mandatory attributes of its corresponding target-object, each object in a production-graph is characterized by special attributes, or labels, that act like programming switches. For example, a label named \$selectbefore indicates that the production-object must match a target-object that the user had selected before the production was applied. Similarly, a label named \$delete is used to signify whether the corresponding object should be deleted from or retained in the target-graph. Further, production-graphs can contain an optional applicability predicate that enables their operation in certain circumstances. The role of these production-specific features will become clearer in the following sections, which illustrate their use in specific examples. For now, suffice it to say that they provide all the necessary building-blocks for encoding the two essential ingredients of graph-grammar programming: (1) the pattern matching logic that identifies the graph pieces on which the production should operate, and (2) the manipulation logic that specifies the transformation that those graph pieces should undergo. As it turns out, the resulting programming formalism is Turing-complete (Nagl 1976)

The remainder of the paper presents a series of productions for constructing decision-trees (§3) and for manipulating and reframing decision-trees (§4). The description of each production is divided into two parts: the user's view of the production followed by its graph-grammar implementation. Readers who wish to focus only on the decision theory aspects of the paper can skip the implementation subsections without losing the thread of the paper. The implementation subsections are intended for readers who are interested in the unique graph-grammar approach to modeling

## 3. Model Definition Productions

As with database management, model management activities fall into two distinct categories: model definition and model manipulation. This section discusses graphgrammar mechanisms for defining, or rather building, graph-based decision-tree models.

In order for a graph to qualify as a decision-tree, it must obey certain constraints. The graph objects must be of certain types, and the graph topology must form a hierarchy, each node having at most one incoming edge. These constraints can be described declaratively, using a logic-based formalism, or syntactically, using a Backus-Naur (BNF) form. In this paper we take an alternative approach, inspired by the theory of formal languages (Hopcroft and Ullman 1979). Instead of specifying what it takes to be a decision-tree graph, we specify what it takes to build a decisiontree graph. More specifically, we wish to define a set of construction rules, or productions, that are guaranteed to produce and maintain valid decision-tree graphs. By "valid" we refer to attributed-graphs that obey the topological and typological constraints of “being a decision-tree."

We base our constructive approach to modeling on a branch of formal languages called graph-grammars. Whereas string-grammars specify how to build syntactically correct sentences in a certain language, graph-grammars specify how to design and maintain syntactically correct graphs using a predefined set of productions. Our basic premise is that graph-grammars are well-suited to support the building and maintenance of certain families of management science models; in this paper, we demonstrate this proposition in the case of decision-trees..

Since decision-trees represent a special case of attributed-graphs, we could have let users build them directly, by enabling unabridged access to a general-purpose graphical editor that allows the creation and connection of nodes and edges in a free-form fashion. However, this freedom of expression may well turn into chaos, as it would allow users to develop invalid models, namely attributed-graphs that violate the topological and typological constraints of decision-trees. Hence, rather than providing the user with a set of primitives for defining unconstrained graphs, we seek to develop higher-order construction operators that understand the special nature of decisiontrees. Our approach is related to the notion of syntax-directed editors, which are “aware" of the special nature of the target-texts on which they operate (Reps and Teitelbaum 1984). For example, programmable editors like EMACs can be used to custom-tailor specific editors to support Lisp, Pascal and C programming. These sorts of editors offer a variety of language-specific editing services like nested indentation, tests of variable declarations, and insertion of coND or IF templates with single keystrokes. Context-sensitive editors speed up the software development process, and, more importantly, promote the construction of readable and error-free programs.

Just as a specialized editor can be tailored to support the process of writing programs in a certain language, a specialized graphical environment can be tailored to support the process of building and maintaining decision-tree graphs. This is because decision-trees, like Pascal programs, are not born in a vacuum; they must obey a set of well-defined structural constraints. With that in mind, our approach to designing a graph-grammar environment for building decision-trees is based on three steps, as follows: (a) Enumerate all the generic operations that underlie the design and maintenance of valid decision-tree graphs; (b) Define each operation as a separate graphgrammar production; and (c) Wrap the resulting library of productions with a congenial user-interface.

## 3.1. Insertion

The construction of any decision-tree graph can be seen as'a sequential application of a subset of twelve generic insertion operations, as follows:

Insert a new { choice|chance|outcome } node as a child of an existing { choice|chance } node.

Insert a new { choice|chance } node as a parent of an existing { choice|chance|outcome } node

We assume that before an insertion production has been invoked, the user has selected some node in the target-graph (the graph on which the production operates), using a pointing device like a mouse. The selected node, which will become the production's “anchor," is denoted hereafter x. Each one of the above twelve insertion productions can be applied either uniquely, or repetitively, with respect to x. A unique insertion of a new node y as the child (parent) of x attaches one copy of y below (above) x. A repetitive insertion of a new node y with respect to x attaches one copy of y below (above) every node in the tree whose labe1 attribute is identical to that of x.2 To illustrate the resulting family of twenty four productions, we will describe one representative example—repetitive insertion of a new outcome-node as a child of an existing choice-node. This production was chosen because of its relative simplicity; as we introduce additional productions, we will gradually increase their level of complexity.

Consider a decision-tree in which a certain choice-node, labeled drillingdecision, leads to two children-nodes, labeled drill and no-dri11. Suppose that it is now required to refine this binary choice by adding to it a new node, labeled dri11 - test . If you were to carry out this editing operation using paper and pencil, how would you go about it? First, you would locate, or select, all the nodes in the tree that are labeled drilling-decision. Next, you would draw a new node labeled dri1l- test below one of the selected nodes, and connect both nodes with a new edge. Finally, you would repeat the exact same operation for each node selected in the first step. The production that carries out node insertion—called INS—operates in precisely the same manner.

The user's view of INs is implemented through a menu-driven GUI . To invoke the production, the user first identifies the target-nodes that ought to be extended, using a pointing device like a mouse. Having marked the nodes of interest, the user pulls down a menu and selects an entry entitled insert a new outcome-node. This entry will invoke the INs production, which will then go to work on the selected areas in the target-graph.

Graph-grammar Implementation:³ The logic of the INs production (Figure 4) is very similar to that of its paper and pencil version. Node x represents the choice-node that is about to be extended. Node y represents the new outcome-node that has to be connected to x. We assume that before the production has been applied, the user has already selected one or more nodes, denoted x, in the target-graph. (Note that we use an overbar to distinguish a node in the target-graph, e.g., x, from its corresponding node in the production-graph, e.g., x.)

![](/api/attachments/SXSAESCV/fulltext/images/c042c3104bd0d17633be34ef17caf83502a9cd88defd0a199bc49985244a7d26.jpg)  
FIGuRE 4. The insertion-production INs, designed to add a new outcome-node to a selected choicenode. Note that the shapes of the objects reflect their types.

The specific operation of INs is determined by the special labels that mark its objects. The selectbefore label indicates that x must have been selected by the user before the production was invoked. The find-al1 label specifies that the production will operate on all the nodes selected by the user. The add-all labels that mark the edge (x, y) and the node y are instructions to add copies of these generic objects to the target-graph. Specifically, they indicate that for each selected and found node x, the production should (a) create a new outcome-node y; and (b) connect x to y by a new echoice edge (x, y). In other words, one copy of each add-a11 object will be added to each find-al1 object that was actually found in the target-graph. (Note in passing that find-one and find-al1 translate roughly to the notion of ∃ and∀ in logic.)

## 3.2. Deletion

Deletion productions are designed to delete selected nodes from a decision-tree graph. As we did in the case of insertion, we assume that before a deletion-production is invoked, the user has already selected a certain target-node, denoted x, as a candidate for deletion. The user may want to delete x in two alternative ways: (a) delete the node X and all but one of its children-nodes, which should be reconnected to x's parent-node; or (b) delete node x and all the nodes that descend from it, i.e., the sub-tree rooted in x. This section demonstrates the latter operation, which is implemented by a single production called DEL . The execution of DEL is demonstrated in Figure 5, where the user is assumed to have applied it to the shaded node in the left decision-tree. When the production terminates its execution, the left tree is transformed into the right tree.

Graph-grammar Implementation. The production-graph of DEL is depicted in Figure 6. Node x. which is marked find-one and selectbefore in Figure 6, represents the root of the sub-tree that has to be deleted. The universal label attached to vallows this production-node to match target-nodes of any type, meaning that the production is insensitive to the type of the children of the deleted node. Nodes x and ν are connected by a path edge—a special production-level edge-type designed to match a directed path of indeterminate length in the target-graph. Finally, the label find - a11 which marks the path (x, y) as well as node y will cause the production to operate on all the paths, of any length, that emanate from x in the target-graph. In a similar vein, y will match all the nodes y that can be found along these paths.

Note that all the labels that were mentioned in the above paragraph are used in

![](/api/attachments/SXSAESCV/fulltext/images/40be76a18bd7c94fb3978b6a60a731fd465741089c545fcd8b38315413b8318d.jpg)  
FiGURE 5. A decision-tree before and after applying the DEL production to the shaded node. The shaded node marks the node selected by the user.

DEL for pattern matching only. In other words, these “passive" labels do not do anything—they just enable the operation of the production, similar to the condition part of an IF THEN rule. The only “active" instruction in DEL's definition is the delete labels. These labels will cause the production to delete the selected node (x), all the edges attached to it, as well as all the nodes that descend from it and their attached edges, thus accomplishing the original plan for this production.

## 3.3. The Optimal Path

A decision-tree that contains choice-nodes represents a set of choices among alternative courses of action, each leading to different sub-trees that contain further choices. When the tree is “rolled-back," the values of the sub-trees are computed, and one of them emerges as the course of action which offers the highest payoff in the decision junction under consideration. We call the edge that leads to that sub-tree the optimal choice edge, and the union of all these edges in the graph the optimal choice path. The optimal choice path is a road map that tells the user, in every choice junction along the way, which course of action will maximize his expected payoff.

Using a dynamic graphics technique, we have built a simple mechanism that continuously highlights the optimal choice path in any given decision-tree. Specifically, nonoptimal echoice edges are colored green, and optimal edges are colored red.

![](/api/attachments/SXSAESCV/fulltext/images/b0c5d7bc4ff2fb15ec5266d5305adf8fe86d7932ecbe3f9e19b746ffde1c28eb.jpg)  
FiGURE 6. The deletion-production, DEL , designed to delete a selected chance-node (x) and all the nodes and edges that descend from it. Note that (a) the edges attached to a node are automatically deleted when the node is deleted; and (b) an edge of type path matches any path of edges of any type,

This coloring scheme becomes particularly handy when doing sensitivity analysis. If the user wishes to examine the impact of different scenario assumptions on his decisions, all he has to do is select certain objects in the decision-tree graph and make the necessary changes to their value and probability attributes. These changes will propagate via the formulas (3-4) throughout the entire tree, causing the system to redraw automatically the optimal path implied by the new assumptions.

This example illustrates the general spirit of NETwORKs, in which images are automatically redrawn by formulas which are continually recalculated. The display characteristics of the graph are determined by special system-attributes, called bindings. which are automatically assigned to every node created by the user. The bindings have names like shape, color and position, and they contain either constant values or formulas, just like ordinary attributes. This flexibility gives the designer a great deal of control over the display characteristics of his objects.

Graph-grammar Implementation. Let x be a choice-node, and let y be a child of x. How can we tell whether or not edge $( x , y )$ is optimal? Recall that (3) sets the value of each parent choice-node to the maximum value of its children-nodes. Hence, if x is a parent of y and ${ \pmb v } ( { \pmb x } ) = { \pmb v } ( { \pmb y } )$ , the edge $( x , y )$ must be optimal. Using this observation, we have implemented the coloring scheme described above by setting the color binding of each echoice edge $( \mathbf { x } , \mathbf { y } )$ in the tree to the following formula:

$$
\begin{array}{l} \text {if((edge(*,*,echoice,X,Y) , na(value,*,Y,-) = na(value,*,Y,-)) ,} \\ \text {red,} \\ \text {green).} \end{array}
$$

The value of the function if (Condition, TrueExp, FalseExp) is TrueExp if Condition is true, and FalseExp otherwise. In the above example, Condition is a conjunction of the two expressions edge(\*, \*,echoice,X,Y) and na(value, \*,X,—) =na (value, \*,Y,—).4 The first expression binds variables x and y to the two nodes that reside at the end-points of the edge whose color we wish to determine. The second expression is true if the value of both nodes is equal, indicating that the edge is optimal. If both expressions are true , the value of the if expression will be red; otherwise, it will be green. Since the if expression is bound to the color attribute of edge $( x , y )$ , the edge will be drawn on the screen in that color. This can be seen in Figure 2, where the optimal-paths of the two trees in the background windows are drawn in bold face.

## 4. Model Manipulation Productions

The application of proper insertion and deletion productions is a necessary, but insufficient, condition for designing and maintaining good decision-tree graphs. Since the same problem can often be cast in several normatively equivalent but topologically different decision-trees, we wish to assist users in the task of exploring more plausible and cognitively appealing interpretations of the modeled problem. In order to do so, we have developed an arsenal of reframing operations which we divide into four categories: pruning, optimizing, consolidating and reversing. The remainder of the paper motivates the need for these operations, presents their conceptual definitions and provides their graph-grammar implementations.

## 4.1. Pruning

A decision-tree model describes a sequence of junctions. Choice junctions represent alternative courses of action, whereas chance junctions represent alternative contingencies. When some of the alternatives that emanate from the same node overlap, the result is typically an unnecessarily cluttered model. For example, consider a chance-node that branches into three probabilistic outcomes: a 50% chance of gaining \$100, a 25% chance of losing \$30 and a 25% chance of gaining \$100. Clearly, a more parsimonious description of the same prospect would be a two-way junction, representing a 75% chance of gaining \$100 versus a 25% chance oflosing \$30. When a chance (choice)-node has two or more outgoing edges that represent identical or similar contingencies (courses of action), we say that the node is superfluous.

Superfluous nodes arise because of three reasons. First, the decision problem that the tree represents may contain a genuine element of redundancy, in which case the “superfluous" nodes give an accurate picture of reality, and there is nothing wrong with them. Second, since superfluous nodes do not violate the topological restrictions of "being a tree," one can create them either unintentionally, or by bad design, through the use of valid tree-construction productions. Finally, superfluous nodes emerge as a degenerate side-effect of other tree-manipulation productions, as shall be discussed later in the paper.

Regardless of the reasons for their existence, it is useful to be able to detect superfluous nodes, and, if the user so desires, proceed to delete their redundant edges and sub-trees from the tree. We call this operation pruning. The following two problems motivate the need for a pruning production.

Problem 1. The following game begins by spinning a roulette wheel which is numbered 1 to 50. If the lucky number is 10, 20, 30, 40 or 50, you win \$100. Otherwise, you win nothing. How much are you willing to pay to play the game?

Problem 2. The following game begins by spinning a roulette wheel which is numbered 1 to 100. If the lucky number is between 1 and 10 (inclusive), you win \$100. Otherwise, you win nothing. How much are you willing to pay to play the game?

Note that both games represent the same prospect—a 10% chance of winning \$100, problem 2 being the pruned version of problem 1. Yet the problems “look" different, as the frame of game 1 seems to offer a better “spread," and thus a better chance, of winning. So which problem gives a better representation of the true odds for winning—1 or 2? We argue that at least on the grounds of parsimony and clarity, a pruned decision-tree is a better decision aide than a superfluous tree, provided of course that the pruning operation does not distort the original setting of the problem.⁵

The pruning logic is as follows. Let x be a node with n outgoing edges, leading to children-nodes $x _ { 1 } , \ldots , x _ { n }$ . Suppose, without loss of generality, that $x _ { 1 }$ and $\pmb { x _ { 2 } }$ are deemed redundant. Pruning consists of removing the edge $( x , x _ { 2 } )$ and the sub-tree rooted at $\pmb { x _ { 2 } }$ from the sub-tree rooted at x. If x is of type choice , this completes the pruning operation. If x is of type chance , the probability of the removed alternative, $P ( x , x _ { 2 } )$ , must be added to the probability of its remaining twin, namely to $P ( x , x _ { 1 } )$ . If node x contains more than two identical alternatives, the same procedure can be applied recursively. In what follows, the procedure that implements this operation is named PC. The users's view of the procedure is demonstrated in Figure $^ { 7 , }$ where the tree on the right represents the result of applying PC to the shaded node in the tree on the left.

![](/api/attachments/SXSAESCV/fulltext/images/2b6320cede7f1345bed7aa57f960b8d8729da1b290c0487fefc8985b86fd8631.jpg)  
FIGURE 7. Problem 1 (left) and Problem 2 (right).

Graph-grammar Implementation. Figure 8 depicts a graph-grammar production named PC1 , designed to prune a single node of type chance . The key players here are the chance-node, x, and its two children-nodes, $x _ { 1 }$ and ${ \pmb x } _ { 2 }$ (node y will be discussed later). The three nodes are marked find - one , meaning that a copy of each must be found in the target-graph in order for the production to be applied. The selectbefore and selectafter labels of x indicate that the user must select this node before the production starts, and that the node will remain selected after the production ends. The universa1 labels indicate that the production is insensitive to the types of $x _ { 1 }$ and $x _ { 2 } ,$ as long as they have the same type. Node $x _ { 2 }$ is marked for deletion, but only if it is deemed redundant to $x _ { 1 }$ . The redundancy test, which is not explicit in Figure 8, is stored in the production's applicability-predicate, to be discussed shortly.

Note that edge $( x , x _ { 1 } )$ , which is marked for deletion, will be immediately replaced with a new edge, marked add -one. This structural trick is required because of a technical reason. Recall that the probability value associated with the edge $( x , x _ { 1 } )$ should be incremented by the probability attribute associated with $( x , x _ { 2 } )$ . In NETwoRKs , however, a production can only change the attributes of objects that are added to the graph. That's the reason behind the deletion and immediate reincarnation of the edge $( x , x _ { 1 } )$

We now turn to discuss the applicability predicate that tests whether or not nodes $\pmb { x _ { 1 } }$ and $x _ { 2 }$ are redundant. In order for a production to be applied, two conditions must be satisfied. First, there must be a topological match between the objects marked find-one and find-al1 in the production graph, and corresponding objects in the target-graph. Second, the production's applicability predicate—a graph-level attribute which is unique to production-graphs only—must evaluate to true . The applicability predicate is essentially a logical expression that can be used to enforce additional constraints on the execution of a production. In the specific case of pC1, the applicability predicate consists of the following expression:

![](/api/attachments/SXSAESCV/fulltext/images/f6db1104c0e977902abe0e42236d2f54f2a34abf466cba9440fb8b07817c6c21.jpg)

![](/api/attachments/SXSAESCV/fulltext/images/e38308ab179f37967e045adae0a3d34de1b5d909e153113d5a5403c8250882a4.jpg)  
FIGURE 8. The pruning production PC1 (top) and the pruning program PC (bottom).

$$
\text { na } (\text { label }, *, \text { x1 }, -) = \text { na } (\text { label }, *, \text { x2 }, -).\tag{5}
$$

Recalling that the definition of the na function is na(AttributeID, GraphID, NodeID, NodeType), we see that (5) will true if and only if the targetnodes corresponding to $x _ { 1 }$ and $\pmb { x _ { 2 } }$ have the same label values, implying redundancy. The underscore characters in the fourth argument indicate that the node-types $\mathfrak { o f } x _ { 1 }$ and $\pmb { x _ { 2 } }$ are immaterial. It's important to emphasize that from a software engineering standpoint, other redundancy tests can be implemented with similar ease. For example, the application might render $x _ { 1 }$ and $x _ { 2 }$ redundant if $| v ( x _ { 1 } ) - v ( x _ { 2 } ) | < \epsilon ,$ for a certain evaluation function $v ( \cdot )$ and tolerance level $\epsilon > 0 .$ .Whichever redundancy test we choose to adopt, the test can be easily implemented via an applicability-predicate such as (5).

Let us suppose then that (5) evaluates to true . This will cause the PC1 production (top of Figure 8) to delete node x, and all the nodes that descend from it in the $\bar { x } _ { 2 }$ target-graph. The scope of the deletion operation is specified in the production-graph by the path edge $( x _ { 2 } , y )$ and the node y, which are both marked find-al1 and delete . Note, however, that PC1 is a single-step deletion operator. As written, it is programmed to delete one redundant edge from a selected node, provided that such an edge exists. The case of $m > 2$ redundant edges is handled by a program-graph that applies pC1 to the same node repetitively, until the node contains no further redundancy.

Program-graphs are the graph-grammar equivalent of flow-charts, except that their building blocks are productions, rather than instructions or subroutines (as in a procedural language). The flow of control of a program-graph is governed by the values that the productions return. Typically, each production is designed to either succeed, or fail: success indicates that the target-graph has been changed according to the production's specifications (right-side), whereas failure indicates that the production could not match its $l e f f - s i d e \left( G ^ { L } \right)$ with an isomorphic sub-graph in the targetgraph, and thus could not be applied. Using the truth values that the productions return. program-graphs enable the implementation of repetitive graph manipulations in the spirit of wHILE and REPEAT loops.

In the specific case of pruning, the repetitive application of PC1 to the same node is carried out by a program-graph named PC (bottom of Figure 8). The logic of PC is as follows. First. PC invokes PC1 , which then tries to detect a pair of duplicate nodes that emanate from the selected node. If such a pair is found, PC1. proceeds to delete one of its members, returning the value true. This causes PC to invoke PCl once again to the same node. (This is why $x _ { 1 }$ is marked both selectbefore and selectafter in PCl.) The cycle continues until PCl returns the value false, indicating that the selected node contains no further redundancy. This, in turn, will cause PC to terminate its execution.

We conclude this section with three comments on program-graphs. First, like wHILE and REPEAT constructs in a procedural language, they are theoretically not needed (Bunke 1982); however, it is frequently more convenient to use a concise program-graph instead of a single, but hopelessly complex, production that accomplishes the same task. Second, program-graphs are a special case of attributed-graphs. Therefore, they are built and edited by the standard graph-oriented machinery of NETwoRKs. Finally, program-graphs are invoked exactly the same way as graphgrammar productions: directly, from menu selections, or indirectly, from other program-graphs or productions.

## 4.2. Optimizing

Each node in a decision-tree, say x, represents a junction of alternatives whose value, v(x). depends recursively on the values of the children-nodes that emanate from x. Since v(•) represents an expected, rather than a determinate, value, it is clear that ${ \pmb v } ( { \pmb x } ) > { \pmb v } ( { \pmb y } )$ does not necessarily imply that x is a “better" prospect than y. For example, it might be that one of y's children represents a risky prospect whose potential value is significantly higher than any one of the values of x's children. In such a case, we say that x and ν are incomparable, because their relative attractiveness depends on subjective risk-attitudes that vary from one decision-maker to another.

There exist situations, however, in which it is possible to compare two siblingnodes, x and y, and conclude that x dominates y under all possible states of nature, and under all possible (Von-Neumann Morgenstern) utility functions. For example, consider the decision-tree depicted in the left of Figure 9. Node ${ \pmb a } _ { 1 }$ dominates node $\pmb { a _ { 2 } }$ because it represents a prospect whose most pessimistic outcome, 10, is better than the most optimistic outcome of $\pmb { a _ { 2 } } ,$ , which is 8. In a similar vein, $\pmb { a _ { 4 } }$ dominates ${ \pmb a } _ { 1 }$ , and ${ \pmb a } _ { \pmb S }$ dominates $\pmb { a _ { 4 } }$ . Note that neither $\pmb { a _ { 3 } }$ nor $\pmb { a _ { 5 } }$ dominates each other.

![](/api/attachments/SXSAESCV/fulltext/images/0d9795f8bb2ec55c4dd59a9c79f5dc9575507a3974725290c1188d9d71317a3d.jpg)  
FIGURE 9. A decision-tree with inferior alternatives: ${ \pmb a } _ { 1 }$ dominates $\pmb { a _ { 2 } } , \pmb { a _ { 4 } }$ dominates ${ \pmb a _ { 1 } } ,$ and ${ \pmb a } _ { \pmb S }$ dominates ${ \pmb a } _ { 4 } .$ The application of the oPT production to the shaded node would transform the left tree to the right tree.

This section presents a graph-grammar program, called oPT, for detecting and eliminating inferior sub-trees from a decision-tree graph. If the user were to apply opT to the shaded node in the left tree in Figure 9, he would end up with the tree on the right. Before proceeding with the details of this procedure, it should be emphasized that the act of deleting inferior nodes and sub-trees from a decision-tree should be handled with great care. This is because a sub-tree which is inferior under one set of contingencies may well become superior when a probability or a value assumption is changed elsewhere in the tree. Therefore, the deletion of inferior nodes and subtrees should be carried out only after the original tree has been saved, as the original tree might be necessary for subsequent sensitivity analyses.

In order to compute dynamically the notion of dominance (or inferiority), we have assigned to each node in the tree two attributes, named upperValue and 1owerValue, whose values are denoted hereafter ${ \pmb v } ^ { + } ( x )$ and $v ^ { - } ( x )$ , respectively. These values depend on the type of $x ,$ as follows. If x is an outcome-node, we define $v ^ { + } ( x ) = v ^ { - } ( x ) { \stackrel { \mathrm { d e f } } { = } } v ( x )$ ; if x is a chance- or a choice-node with children-nodes $x _ { 1 } , \ldots ,$ $x _ { n } ,$ we define

$$
v ^ {+} (x) \stackrel {\text { def }} {=} \max \left\{v ^ {+} (x _ {1}), \dots , v ^ {+} (x _ {n}) \right\} \quad \text { and } \quad v ^ {-} (x) \stackrel {\text { def }} {=} \min \left\{v ^ {-} (x _ {1}), \dots , v ^ {-} (x _ {n}) \right\}.
$$

The dominates relation can now be defined as follows: let x and y be two siblingnodes (children of the same parent). Node x is said to (strictly) dominate node $y ( x \succ y ) \operatorname { i f } v ^ { - } ( x ) > v ^ { + } ( y )$ . It is easy to show that the > relation is partial, irreflexive, transitive and antisymmetric.6 Hence, it forms a partial order on every set of siblingnodes in a decision-tree graph.

Graph-grammar Implementation. The graph-grammar formulas for upperValue and lowerValue for a nonoutcome-node x are as follows:

upperValue: imax $\{ { \mathrm { e d } } { \mathfrak { g e } } ( * , \ldots , - , * , \mathbf { x } )$ ,na(upperValue,\*,Y,\_)), (6)

lowerValue: imin(edge $( * , \ldots , * , \mathbf { x } )$ ,na(lowerValue $\cdot ^ { * , \pmb { x } , - \alpha } )$ . (7)

Given (6) and (7), the graph-grammar implementation of the relation $x _ { 1 } \succ x _ { 2 }$ is as follows:

$$
\text { na } (\text { lowerValue }, *, x 1, -) > \text { na } (\text { upperValue }, *, x 2, -).\tag{8}
$$

We see that (8) will be true if and only if the lowerValue of $\mathbf { \boldsymbol { x } _ { 1 } }$ is greater than the upperValue of $\pmb { x _ { 2 } }$ , implying that $x _ { 1 }$ dominates $x _ { 2 }$ (or, equivalently, that $x _ { 2 }$ is inferior $\mathbf { t o } \mathbf { \Gamma } _ { \mathbf { x } _ { 1 } } )$ . Hence, predicate (8) is essentially a detector of dominant and inferior nodes.

Once a set of nodes is found to be inferior in a certain sub-tree, it should be deleted from the graph. This operation is carried out by a production, named oPT1, and a program graph, named oPT, which are essentially identical to the pruning production PC1 and the pruning program PC, respectively, from §4.1 (see Figure 8). The only difference is that the applicability-predicate of OPT1 is (8) whereas that of PC1 is (5).

When the user applies OPT to a selected node, say x, OPT begins its execution by applying OPT1 to the same node. OPT1 then tries to find a pair of children-nodes, $x _ { 1 }$ and $x _ { 2 }$ , that satisfies (8). If such a pair is found, OPT1 proceeds to delete $\mathbf { \lambda } _ { x _ { 2 } }$ from the target-graph, returning the value true to its calling environment—OPT . This will cause OPT to apply OPT1 to x once again, until x contains no additional inferior edges. At that point, the OPT program will terminate its execution. Since the production-graphs of oPT and OPT1 are isomorphic to those of PC and PC1, respectively we will not describe them here.

Proof. Partial: Let $v ^ { + } ( x ) = 3 , v ^ { - } ( x ) = 2 , v ^ { + } ( y ) = 4 ,$ and $v ^ { - } ( y ) = 1$ . The data are such that neither $v ^ { - } ( x ) > v ^ { + } ( y )$ , nor $v ^ { - } ( y ) > v ^ { + } ( x )$ . Hence, x does not dominate y and y does not dominate x. Transitive: assume that $x \succ y$ and $y \succ z .$ Hence, $v ^ { - } ( x ) > v ^ { + } ( y )$ and $v ^ { - } ( y ) > v ^ { + } ( z )$ . Now, by definition, $v ^ { + } ( y )$ $\geq v ^ { - } ( y )$ ). Hence, we get $v ^ { - } ( x ) > v ^ { + } ( y ) \geq v ^ { - } ( y ) > v ^ { + } ( z )$ . Hence, $v ^ { - } ( x ) > v ^ { + } ( z )$ )and ${ \mathfrak { c } } \succ z .$ Antisymmetric: let $x \succ y .$ Assume that $y \succ x .$ . Hence, $v ^ { - } ( x ) > v ^ { + } ( y )$ and $v ^ { - } ( y ) > v ^ { + } ( x )$ . By definition, ${ \mathfrak { v } } ^ { + } ( x ) \geq { \mathfrak { v } } ^ { - } ( x )$ and $v ^ { + } ( y ) \geq v ^ { - } ( y )$ . Hence, we get $v ^ { - } ( x ) > v ^ { + } ( y ) \geq v ^ { - } ( y ) > v ^ { + } ( x ) \geq v ^ { - } ( x )$ , leading to $v ^ { + } ( x ) > v ^ { + } ( x )$ 4 which is a contradiction.

## 4.3. Consolidating

Decision-trees often contain a series of two or more consecutive nodes of the same type. A sequence of two chance-nodes represents two consecutive random events. A sequence of two choice-nodes represents two consecutive decisions. If a sequence of nodes of the same type reflects an accurate description of the user's problem, then there is nothing wrong with it. For example, consider a chance-node labeled po11- results , followed by a chance-node labeled election- results . This sequence makes perfect sense in a certain context, and therefore it should not be altered. On the other hand, there exist situations in which a sequential presentation of nodes of the same type serves to befog, or even distort, an otherwise simple problem. The following example is a case in point:

Problem 3. You may enter a two-stage game of chance whose outcome depends on the number drawn from spinning a roulette wheel which is numbered 1 to 100. In the first stage of the game, the wheel is spun. If the lucky number is in the range 1–16, you enter the second stage of the game. Otherwise, the game is over and you win nothing. In the second stage of the game, the wheel is spun again. If the lucky number is even, you win \$500. Otherwise, you win nothing. How much are you willing to pay to play the game?

Problem 4. You may enter a game of chance whose outcome depends on the number drawn from spinning a roulette wheel which is numbered 1 to 100. If the lucky number is in the range 1–8, you win \$500. Otherwise, you win nothing. How much are you willing to pay to play the game?

Note that problems 3 and 4 (see Figure 10) offer the same prospect—an 8% chance of winning \$500. Yet, in spite of this normative equivalence, descriptive decision theory predicts that most people who are given this option would prefer to play game 3 to game 4. If this is indeed the case, the seller of the game could make it appear more attractive if he could cast it in terms of problem 3, rather than in terms of problem 4. Once again, we see that the frame of the problem—the topology of its decision-tree plays a significant role in forming the user's preferences.

There may be several reasons why people prefer game 3 to game 4. First, it can be argued that game 3 is simply more interesting than game 4; although both games offer exactly the same value, the former game offers more excitement along the way. A more compelling explanation, inspired by Tversky and Kahneman's (1974) "pseudocertainty effect," goes as follows. When people are presented with a sequence of two risky prospects, they tend to evaluate each prospect separately. As a result, the second prospect in game 3 is analyzed with a false feeling of certainty. In other words, the 50% chance of winning in the second stage tends to overshadow the fact that there is only a 16% chance of reaching that stage in the first place.

How can we eliminate, or at least reduce, the adverse impact of the pseudocertainty effect? Taking a graph-grammar approach, we provide the user with an optional production designed to detect paths that contain series of two or more consecutive chance-nodes, and, if the user so desires, collapse them into single chance-nodes. Formally speaking, let x be a node of type chance with n outgoing edges, leading to the children-nodes $x _ { 1 } , \ldots , x _ { n }$ . Without loss of generality, assume that $\pmb { x _ { 1 } }$ is also of type chance, and denote its children-nodes $x _ { 1 1 } , \ldots , x _ { 1 m }$ . Our goal is to remove $\pmb { x } _ { 1 }$ from the sub-tree rooted in $x ,$ and reconnect all of $x _ { 1 } ^ { \prime } { \mathsf { s } }$ children directly to $x .$ The probability value of each reconnected edge, $( x , x _ { 1 i } ) , j = 1 , \ldots , m$ , should be set to the product $p ( x , x _ { 1 } ) \cdot p ( x _ { 1 } , x _ { 1 j } )$ (the joint-probability that both $x _ { 1 }$ and $x _ { 1 j }$ have occurred). We call this operation consolidation.

![](/api/attachments/SXSAESCV/fulltext/images/0b6b964f3a0c83469a89ac56d041b8332deafa998a399ce1796acc375b2c91ea.jpg)  
FiGURE 10. Problem 3 (top) and Problem 4 (bottom). The middle tree is an intermediate result, discussed in the paper.

Graph-grammar Implementation. The production that carries out this transformation is called con (Figure 11). The production-graph consists of three nodes: x and $\pmb { x } _ { 1 }$ , representing the two connected chance-nodes, and $y ,$ a typical child of $x _ { 1 }$ . Node x is marked selectbefore, selectafter and find-one, indicating that (a) it must be selected before the production starts; (b) it will remain selected after the production has ended; and (c) only one such node is sought after in the target-graph. Node $x _ { 1 }$ is marked find- a11 and delete , indicating that all such nodes should be found and then deleted from the target-graph. Note that the types of x and $x _ { 1 }$ must be the same in order for the production to execute. This constraint is specified graphically in con's graph, where both nodes appear as circles.

![](/api/attachments/SXSAESCV/fulltext/images/1e14c750d73edc157713084eaf495d1c5e8c9f4c25480e3f80f42073f14ba89f.jpg)  
FiGuRE 11. The consolidation production coN, designed to consolidate two consecutive chance-nodes into a single chance-node

The typical child of the deleted node is represented in the production-graph by y. The universa1 label indicates that the type of this node is immaterial for the production. The add-al1 label for edge $( x , y )$ indicates that this is a new edge, to be added to the graph by the production. The value of the probability attribute of edge $( x , y )$ should be set to the product of the probability attributes of the edges corresponding to $( x , x _ { 1 } )$ and $( x _ { 1 } , y )$ in the target-graph. This is achieved through the following attribute transformation expression:

$$
\begin{array}{l} \text {ea(probability,*, (x,x1),echance)*} \\ \text {ea(probability,*, (x1,y),echance).} \end{array}\tag{9}
$$

The consolidating example (Figure 10) illustrates how the “output" of one production can be piped into another production as “input." Denoting the trees in the figure from top to bottom $t _ { 1 } , t _ { 2 }$ and $t _ { 3 } ,$ , the overall graph manipulation can be described in terms of the chain $t _ { 1 } \xrightarrow { \mathrm { c o n } } t _ { 2 } \xrightarrow { \mathrm { p c } } t _ { 3 } ,$ , or in terms of the functional form t3=PC (CoN (t1)). Such combinations are possible because the inputs and outputs of all productions (as well as the productions themselves) are instances of the same thing—attributed-graphs.

## 4.4. Reversing

Let t be a decision-tree. If t' is the decision-tree obtained from t by (1) pruning all the nodes of t (§4.1); and (2) consolidating all the branches of t (§4.3), then t' contains only alternating sequences of choice-nodes and chance-nodes. In other words, the decision-tree that emerges from pruning and consolidating operations has the normal game-theoretic form of a 2-player game, in which a person (choicenodes) plays against nature (chance-nodes). Typically, the order of the nodes is dictated by temporal constraints: player 1 makes the first move, player 2 makes the second move, player 1 makes the third move, and so on. In other words, the sequence of decisions and consequences unfolds in a fixed order which is determined by the rules of the game. There exist situations, however, in which there is a certain degree of latitude regarding the ordering of the moves. In these cases, the user would benefit from a production that enables him to reverse the direction of some nodes and edges in a sensible way, without violating the essential characteristics of the underlying decision problem.

Further, most decision-trees are not cast, at least initially, in their normal form. As was mentioned elsewhere in the paper, many trees contain genuine sequences of chance-chance or choice-choice branches that the user may not want to consolidate, perhaps in order to preserve the original setting of the problem. Here, too, it may be desirable to reverse the order of some nodes, for two different reasons. First, node-reversal is a useful editing operation that comes handy in correcting or modifying the structure of an existing tree. Second, node-reversal is an effective analytic tool; with it, the user can create alternative frames of the same decision problem, gaining new insights into the problem's structure.

With that in mind, we seek to provide the user with four generic reversal operations, as follows:

(1) reverse a chance-chance sequence,

(2) reverse a choice-choice sequence,

(3) reverse a choice-chance sequence,

(4) reverse a chance-choice sequence.

Although the four operations are equally important from a functional standpoint, some are more interesting than others from a graph-grammar perspective. (1) is interesting because it involves recalculation of probabilities, using Bayes rule. (2) is a deterministic version of (1). (3) is interesting because it reverses nodes of different types, whereas (4) is the inverse of (3). Technically speaking, each one of the four operations represents a graph manipulation that is significantly more complex than what we have seen thus far in this paper. Therefore, and because of space limitations, we will present here the implementation of one illustrative example—reversing a chance-chance sequence. The need for this operation can be motivated by the following example:

Problem 5. A seasonal virus is known to infect one predisposed person out of every 100 people in the population. The virus causes a mild illness that lasts one week. You have just undergone a test which came out positive, indicating that you are predisposed. The test's hit-rate (positive result when the person is predisposed) is 80%. The test's false alarm-rate (positive result when the person is not predisposed) is 20%. How much are you willing to pay to purchase a vaccine that completely eliminates the virus attack?

The top left tree in Figure 12 gives a compact description of the problem's data showing clearly the clinical characteristics (type I and II errors) of the test. At the same time, the tree fails to answer the key question here, which is not clinical, but diagnostic, in nature: what are the chances that I am predisposed, given that the test comes out positive? In order to answer this question, one has to transform the tree from its present, clinical frame (top left tree in Figure 12) into its dual, diagnostic frame (bottom left tree in Figure 12). As we see, the chance of being predisposed if the test says so is strikingly low—less than 4%.

This is not to say that the top left tree in Figure 12 is invalid or misleading. In its present frame, the tree serves the interests of one party, namely the vaccine's manufacturer. The other party involved—the prospective user who is considering taking the test—can learn little from the tree about the actual validity of the test. In order to make a reasoned decision, the user must reverse the sequence of the nodes predisposed and test-results to the sequence test-results, followed by pre- disposed . This reversal operation, which involves a delicate graph manipulation and an application of Bayes rule, is clearly beyond the bounded rationality of most decision-makers. Hence, an automated aide, in the form of a reversal production, is called for. This is yet another example in which the given frame of a decisiontree does not lend itself to answering all the relevant questions that may be posed against it. In other words, even though the tree contains all the raw information necessary for reaching a reasoned decision, key parts of this information are implicit and not readily accessible.

![](/api/attachments/SXSAESCV/fulltext/images/cb45d3dc460fbd257923a29e193de15b9b9cda2b166c6e84774da4d7fd660042.jpg)  
FiGuRE 12. Reversing a chance-chance sequence, PD and TR refer to the random-variables predisposed and test-result, respectively (problem 5). Shaded nodes are nodes that have been selected. first by the user and then by the productions. Shaded edges (lower right) represent edges that have been deleted by the productions.

The general case of node reversal is depicted in Figure 13. Let t be a sub-tree with a root-node of type chance , denoted x. Node x has n outgoing edges, (x, y), i = 1, . . . , n, each leading to a chance-node y,. The edges are parameterized by the probability distribution of $X , \mathbf { i . e . , }$ , by the set of values $P ( x _ { i } ) , i = i , \ldots , n$ . Each of the $y _ { i } ^ { \star } { \mathsf { \pmb s } }$ has m outgoing edges, $( y _ { i } , z _ { i j } ) , j = 1 , \ldots , m$ , leading to a node $z _ { i j }$ which may be of any type. Note that each of the $y _ { i } { \mathrm { : } }$ 's represents the same random-variable $\mathbf { \mathit { r } } ,$ whose probability distribution is conditioned on the occurrence of the random event $\pmb { \chi }$ . Hence, each edge $( y _ { i } , z _ { i j } )$ is parameterized by the conditional probability $P ( y _ { j } | x _ { i } ) , j = 1$ $\dots , m , i = i , \dots , n$ . For the sake of brevity, we denote this tree $\mathbf { \nabla } t = ( q , x , y , z ) ($ qand z are nodes of any type, whereas x and $_ y$ must be of type chance). With this notation, the goal of the reversal operation is to transform the sub-tree $t = ( q , x , y , z )$ into the sub-tree $t ^ { \prime } = ( q , y ^ { \prime } , x ^ { \prime } , z )$ and, of course, carry out all the necessary probability calculations implied by the reversal. It's important to remember that t will typically be embedded in a larger tree, adding to the complexity of this manipulation. The productions that implement this manipulation are quite simple, but they involve several graph-grammar tricks that have not been presented yet. In order to avoid clutter, we delay the step-by-step description of these productions to a technical appendix at the end of the paper.

![](/api/attachments/SXSAESCV/fulltext/images/0961002eac45670cf503b39f747de0b1d1ee003a4a8c70e9130f062f913c372d.jpg)  
FiGuRE 13. The goal of the reversal operation is to reverse the order of two consecutive chance-nodes, $\mathbf { i . e . , }$ to transform the top tree, denoted $( q , x , y , z )$ , to the bottom tree, denoted $( q , y ^ { \prime } , x ^ { \prime } , z )$ . q and z may be of any type, whereas x and y are assumed to be of type chance.

## 5. Conclusion

This section summarizes the paper along the two dimensions that characterized our research: graph-grammars and decision theory. We conclude with an outline of future research in the areas of experimentation and game-trees.

## Graph-Grammar for Decision Support

Generic families of models (like decision-trees) can be built and manipulated in two different ways: through general-purpose languages, like Pascal or C, or through dedicated packages, like Arborist or Supertree (McNamee and Celona 1987). Each implementation vehicle offers a different set of pros and cons. General-purpose languages are flexible, but hard to use, whereas specialized packages are user-friendly, but functionally limited. In this paper we presented an interim solution to model building, in the form of a Graph-Based Modeling System (GBMs ). We argue that the GBMs approach offers both the flexibility of free-form programming, on the one hand, and the predictability and ease of use of specialized modeling environments, on the other.

In particular, the graph-grammar approach to modeling entails the following tangible benefits.

Flexibility: graph-grammars are Turning-complete, meaning that they are just as powerful as any general-purpose programming language.

Formality: the use of graph-grammars enables one to define all the permissible manipulations on a certain family of models precisely and unambiguously, using a mathematical language

Executability: the graph-grammar specifications can be implemented on a computer, so that model definitions can be directly executed.

Elegance: in a graph-grammar, both graphs and operations on graphs are defined in terms of a uniform language—graphs

Modularity: New productions can be easily defined to manipulate models in ways not envisioned by the original designers.

Generality. The graph-grammar formalism is a general-purpose modeling tool; it can be used to construct any attributed-graph, not just decision-trees. Hence, decision-tree models built in a GBMs can be archived and managed along with other graph-grammar models, forming a model-base.

The latter point is quite important. In addition to its ability to support the construction and manipulation of decision-trees, NETwoRKS can be applied to many other modeling domains, e.g., influence diagrams, game trees and mathematical modelling. Moreover, the system allows models from different paradigms not only to coexist, but also to interact. For example, the contents of a value attribute of an outcome-node in a decision-tree model might be calculated by another model, e.g., the optimal objective function of a linear programming problem. The link between the two models can be easily established, as the attributes of one graph are allowed to refer to attributes in any other graph in the model-base. This connectivity, along with the ability to work on different models in multiple windows, enable the implementation of many ideas in model management that up to now were considered quite abstract.

The decision-tree system that resulted from this research was implemented in NETwORKS in about one week. NETwORKS runs on Macintosh computers and requires at least 4 MB of main memory. It is written in AAIS Prolog, and can interface with native Prolog code.

## Decision Theory

One fundamental requirement in the normative theory of decision-making is that the preferences of rational persons should be independent of problem description.

The expected utility model and the theory of subjective probability provide mathematical tools that are completely devoid of any "graphical" or “presentation" contexts. However, numerous studies on actual (rather than normative) decision-making under uncertainty revealed a persistent and predictable framing effect. Tversky and Kahneman (1981), who studied this phenomenon in detail, have summarized their findings as follows:

“Individuals who face a decision problem and have a definite preference (i) might have a different preference in a different framing of the same problem, (ii) are normally unaware of alternative frames and of their potential effects on the relative attractiveness of options,() would wish their preferences to be independent of frame; but (iv) are often uncertain how to resolve detected inconsistencies. In some cases, the advantage of one frame becomes evident once the competing frames are compared, but in other cases it is not obvious which preferences should be abandoned."

We argue that this view should motivate the development of a new breed of decision support systems—systems that not only support the technical aspects of building decision models, but are also sensitive to the cognitive limitations and biases that creep into their normal use. The intelligent decision-tree package presented in this paper is a step in this direction. In addition to the standard functions of building, editing and analyzing decision-trees, we have developed a library of productions that enable the user to manipulate decision-trees and create alternative frames of the same problem, thus gaining more insight into the problem's structure and into the decision-maker's own set of preferences

To summarize, the reframing productions presented in the paper fall into four categories: pruning, consolidating, optimizing and reversing. Pruning consists of removing superfluous nodes and edges from an otherwise well-structured tree. Consolidating is the act of collapsing a branch of two or more nodes of the same type into a single node. Optimizing consists of removing sub-trees that have no impact on the optimal choice path. Reversing deals with altering the order of nodes and edges in the tree. One additional operation that we have not implemented yet can be termed joining—the act of combining two separate decision-trees into a single tree. This graph manipulation will be a powerful debiasing mechanism, as it would allow users to overcome a natural difficulty to analyze concurrent decisions, a bias that was reported elsewhere (Tyersky and Kahneman 1981). Joining graphs is a challenging operation from a graph-grammar perspective, and we intend to report about it in future work.

## Experimentation

The study of graphical decision aides will not be complete until the effectiveness of the proposed tools is tested in controlled experiments with human subjects. Although it is plausible to assume that multiple (but equivalent) views of the same problem are likely to promote more informed and reasoned decisions, it remains to be seen whether an environment that enables such “explorations" will indeed improve the quality of decision-making under uncertainty. This section describes the outline of a series of experiments that can be used to test whether our graph-grammar approach will help users overcome certain presentation and framing biases.

The typical experiment will involve two different frames of the same prospect, denoted $f _ { q }$ and $f _ { r }$ (e.g., problems 1 + 2 or 3 + 4 in this paper), and four groups of subjects, denoted $X _ { q } , X _ { r } , C _ { q }$ and $C _ { r }$ . All subjects will be allowed to use a NETwoRks - based decision-tree system, with one major difference. The X subjects will have access to the complete system, whereas C subjects will use a version of the system in which the reframing production under investigation will be disabled. Groups $X _ { q }$ and $C _ { q }$ will be exposed to the prospect through the $f _ { q }$ frame, and groups $X _ { r }$ and $C _ { r }$ through the $f _ { r }$ frame. The two frames will describe the same prospect—e.g., a risky investment decision or a medical treatment—cast in two different but normatively-equivalent representations. Each subject will be asked to specify the price at which he or she will be willing to buy the prospect, i.e., the certainty-equivalence of the prospect.

Let the average answer to this question in the four groups be $\overline { { \boldsymbol { X _ { q } } } } , \overline { { \boldsymbol { X _ { r } } } } , \overline { { \boldsymbol { C _ { q } } } } ,$ and $\overline { { C } } _ { r } .$ The first hypothesis of interest will be $\begin{array} { r } { \overline { { C _ { q } } } = \overline { { C } } _ { r } } \end{array}$ . The rejection of that hypothesis would entail a strong framing effect. That is, a significant difference between $\overline { { C _ { g } } }$ and $\overline { { C } } _ { r }$ would indicate that $f _ { q }$ and $f _ { r }$ (which are two different descriptions of the same problem) have caused the subjects to reach significantly different decisions. If such a difference were detected, the next hypothesis of interest will be $\overline { { { X _ { q } } } } - \overline { { { X _ { r } } } } = \overline { { { C _ { q } } } } - \overline { { { C _ { r } } } }$ . If this hypothesis were rejected in favor of the alternative hypothesis $\overline { { { X _ { q } } } } - \overline { { { X _ { r } } } } < \overline { { { C _ { q } } } } - \overleftarrow { C } _ { r } ,$ one would have to attribute the difference (if it were significant) to the reframing production under investigation. Recall that the only difference between the X and the $c$ groups was that the former had access to the production “treatment" and that the latter had not. Thus, if the two X groups were significantly more consistent than the two $c$ groups, one could argue that the production had successfully mitigated the framing effects induced by $f _ { q }$ and $f _ { r }$

By varying the problems, the frames, and the productions under investigations, one could test systematically the effectiveness of all the debiasing mechanisms that we have described, as well as a great variety of other graphical decision aides, yet to be specified. We hope that this might be the first step toward a new research program to investigate the full potential of computer-graphics in debiasing decision-making under uncertainty.

## Game Trees

One logical extension to this work involves game-trees, a graphical aide designed to describe the structure and unfolding of multiplayer competitive games (Von Neumann and Morgenstern 1953, Luce and Raiffa 1957). Like decision-trees, gametrees consist of choice, chance and outcome-odes. To allow for multiple players, however, the choice-nodes are assigned to different decision-makers (each node is assigned to exactly one person). Further, in some games, players may not be aware of the prior decisions of other players. To handle such information hiding, distinct sets of choice-nodes assigned to a particular player are grouped into information-sets. To the other players, the choice-nodes in an information-set are indistinguishable. That is, the players do not necessarily know the exact paths taken previously by the other players to reach choice-nodes in their respective information-sets.

Graph-grammars and NETwoRKs are perfectly suited to provide a user-interface for building and manipulating such game-trees. This would be a natural follow-up of our research on decision-trees. First, choice-nodes would require an additional attribute to identify the player associated with each decision. At least one additional edgetype, say information\_set , would be required to connect choice-nodes that appear in the same information set. Second, graph-grammar productions would be used to enforce additional restrictions on the structure of game-trees. For example, information-sets would be allowed to contain only choice-nodes of the same player. Finally, a series of productions could be written to identify the strategies of the various players, convert games-trees (extensive form) to payoff matrices (normal form) and vice versa, and provide simulations of actual games with different probability and payoff scenarios.\*

Acknowledgements. This research has been supported in part by National Science Foundation Grant SES-8917966 and by a grant from the National Science and Engineering Research Council of Canada. The authors thank the associate editor and two anonymous referees for many useful comments.

\* Steven O. Kimbrough, Associate Editor. This paper was received on January 9, 1992, and has been with the authors 3 months for 1 revision.

## Appendix: Node-Reversal Productions

The overall reversal operation is carried out by a graph-grammar program, named RCC, which applies two productions, named RCC1 and RCC2 , to the target-graph (see Figure 14). We assume that before the program has been invoked, the user has selected a certain target-node, denoted x, as the operation's anchor, ${ \bar { x } } ,$ or pivot. If x has no child-node of type chance , the RCc1 production will fail to match its left-side on the target-graph. As a result, the production as well as the RCC program will terminate their execution (see bottom of Figure 14), and the tree will remain intact. If RCc1 succeeds to match the sequence x, y on the $\pmb { x } ,$ target-graph, it will proceed to create a reversed copy of this pair, denoted $( \boldsymbol { y } ^ { \prime } , \boldsymbol { x } ^ { \prime } )$ in the production-graph. The second production—RCc2 —links the edges that emanate from the newly created node $x ^ { \prime } 1 0$ the children of the old node $_ { y , }$ and then deletes the old sequence $x , y$ from the target-graph.

The productions RCc1 and RCc2 , whose respective graphs are depicted in Figure 14, are designed to reverse the order of two consecutive chance-nodes in a decision-tree graph—a transformation which is depicted symbolically in Figure 13. With that figure in mind, the RCC1 production performs the following operations:

(1) Create node ${ \pmb y } ^ { \prime } .$

(2) Create nodes $x _ { j } ^ { \prime } , j = 1 , \dotsc , m$ . (Each of the m new nodes is a copy of the old x node.)

(3) Create edges 1V $( y ^ { \prime } , x _ { i } ^ { \prime } ) , j = 1 , \ldots , m$

(4) Set the probability attribute of each edge $( \pmb { y } ^ { \prime } , \pmb { x } _ { j } ^ { \prime } )$ to $P ( y _ { j } ^ { \prime } )$ via the formula $\Sigma _ { i = 1 } ^ { n } P ( y _ { j } | x _ { i } ) P ( x _ { i } )$

The second production, RCC2 , performs the following operations (see Figure 13 and bottom right of Figure 14):

(1) For each new node $x _ { j } ^ { \prime } , j = 1 , \dotsc , m$ , create a new set of edges, $( x _ { j } ^ { \prime } , z _ { i j } ) , i = 1 , \ldots , n .$

(2) Set the probability attribute of each edge $( x _ { j } ^ { \prime } , z _ { i j } )$ to $P ( x _ { i } ^ { \prime } | y _ { j } ^ { \prime } )$ via the formula $P ( y _ { j } | x _ { i } ) \cdot P ( x _ { i } ) / $ $P ( y _ { j } ^ { \prime } ) , j = 1 , \dots , m , i = 1 , \dots , n$ (Bayes rule).

(3) Delete the old x node and its outgoing edges $( x , y _ { j } ) , j = 1 , \ldots , m .$

## Production RCCl

The production (top of Figure 14) begins its operation by looking for an edge $( { \bar { x } } , { \vec { y } } )$ in the target-graph such that X was selected by the user and both X and y are of type chance . The edge and its two end-nodes are labelled find -one and retain , since only one instance of them should be found in the target-graph, and they should not be deleted (at least temporarily, as we will see shortly). Node x is labelled selectbefore, since it must have been selected before the production can proceed, and selectafter, in preparation for the second production (RCc2).

After x and v have been matched with corresponding nodes in the target-graph, the production proceeds to add a new node, denoted ${ \boldsymbol { \mathbf { \mathit { y } } } } ^ { \prime } ,$ to the graph. The node is labeled selectafter (root $) - \mathbf { a }$ label which will help the next production (RCC2) distinguish between the old root x and the new root y', which are $y ^ { \prime } ,$ both selected (root is an arbitrary label chosen by the production designer). Since at the end of the reversal operation $\pmb { y } ^ { \prime }$ must inherit the parent of x, both nodes are connected to q (a node of any type, i.e., universal)in the production-graph.

The node a and its outgoing edges are labeled find-all and add-all, rather than find-one and add - one , because of a subtle contingency. The problem is that X might be the root of the overall decisiontree. in which case a will not match any node in the target-graph. In such an event, if q were labeled find - one , the production would fail to match and thus terminate its operation. The find- a11 label, on the other hand, is more liberal, as it instructs the production to seek 0, 1, or more such nodes in the target-graph. 0 would imply that the node is the tree's root; 1 would imply that the node is a regular, nonroot node. Any number greater than 1 will not be possible because each node in a decision-tree has exactly one parent.

![](/api/attachments/SXSAESCV/fulltext/images/52404098278bca679306a3ac036718f7be0c580cdb121b5f5d209d25ce4d22a2.jpg)

![](/api/attachments/SXSAESCV/fulltext/images/f123ed4cd09f8c266910dda6bc31f2b85fb31d3e8155beeb288b19a7464e15a9.jpg)

RCC:  
![](/api/attachments/SXSAESCV/fulltext/images/0c427672923067055b9a4a7f444f47e1edda07687a20408e7011120c1b08e954.jpg)  
FiGURE 14. The RCC program (bottom), designed to reverse a chance-chance sequence. This program consists of two productions, Rccì (top), and RCc2 (middle) executed in sequence.

Recalling that nodes x and y represent two random-variables, our next task is to link every possible outcome (outgoing edge) of y to an identical copy of x. The reversed nodes are denoted y' and x', and the $\pmb { y } ^ { \prime }$ $\pmb { x } _ { \pmb { \cdot } } ^ { \prime }$ reversal logic is carried out by the three edges $( y , z ) , ( y ^ { \prime } , x ^ { \prime } )$ , and $( x ^ { \prime } , z )$ . The labels of these edges cause the production to enumerate (find-al1) the possible contingencies of y, copy them (add-al1) to y', and ${ \pmb y } _ { \pmb { \imath } } ^ { \prime } ,$ then attach their corresponding outcomes to $\pmb { x } \prime .$ The curious pair of labels (add-al1, delete) which marks $( x , z )$ forces the system to add one copy of x' to each (found) outcome of y.

The value of the labe1 attribute of edge $( \boldsymbol { y } ^ { \prime } , \boldsymbol { x } ^ { \prime } )$ is set to the value of the label attribute of edge $( y , z )$ by the attribute transformation expression:

$$
\text { ea } (\text { label }, *, (y, z), \text { choice }).\tag{10}
$$

Finally, the value of the probability attribute of $( y ^ { \prime } , x ^ { \prime } )$ (for a certain outgoing edge j), which represents $P ( y _ { j } ^ { \prime } )$ , is calculated according to the following formula:

$$
P (y _ {j} ^ {\prime}) = \sum_ {i = 1} ^ {n} P (x _ {i}) P (y _ {j} | x _ {i}).\tag{11}
$$

The graph-grammar implementation of this formula is as follows:

$$
\begin{array}{l} \text {sum((edge(*,Edge1,echance,x,Y) , edge(*,Edge2,echance,Y,Z) , ea(label,* ,Edge2,echance) = ea(label,*,(y',x'),echance)) , ea(probability,* ,Edge1,echance)*ea(probability,* ,Edge2,echance)).} \end{array}
$$

In shorthand, this is essentially a sum $( \mathbb { P } , \mathbb { V } )$ function in which the selector P consists of the three boolean conjuncts edge, edge, and ea=ea, and v is the numeric expression ea\*ea. The function sums up all the eaea values for which the three conjuncts are true, where:

(1) The first conjunct, edge (,Edgel,echance $\mathbf { \mu } , \mathbf { x } , \mathbf { y } )$ , finds a child Y of x . This corresponds to the event $\pmb { x } _ { t }$

(2) The second conjunct, edge $( \ast , \mathtt { E d g e 2 } ,$ ,echance, $, \pmb { \check { \tau } } , \pmb { \check { z } } )$ , finds a child z, of the Y which was found above. This corresponds to the conditional event $y _ { j } \dag x _ { i } .$

(3) The third conjunct insists that the 1abe1 of the edge $\scriptstyle ( y , z ) ( { \tt E d g e 2 } )$ be equal to that of $( \boldsymbol { y } ^ { \prime } , \boldsymbol { x } ^ { \prime } )$ Recalling that we are calculating $P ( y _ { j } )$ for some j, this conjunct assures that we only use those conditional probabilities, $P ( y _ { k } | x _ { i } )$ , for which $k = j .$

(4) Given the nodes and edges that the selectors have matched, the expressions ea (probability, $^ { \bullet , }$ ,Edgel,echance) and ea(probability,\*,Edge2,echance) correspond to the probabilities $P ( x _ { i } )$ and $\pmb { P } ( y _ { j } | \pmb { x } _ { i } )$ , respectively.

Hence, the overall sum function evaluates to the value of (11)

## Production RCC2

Once production RCc1 has completed, a new node, represented by y’, will have been added to the graph. $y ^ { \prime } ,$ In addition, new edges will have been added to the graph, leading from y' to x', one edge for each possible $\pmb { y } ^ { \prime }$ $\mathbf { \boldsymbol { x } } _ { \flat } ^ { \prime }$ outcome of y. Further, the probability values of each of those edges (the $P ( y _ { I } ) ^ { * } { \mathsf { s } } )$ will have been calculated. What remains to be accomplished is to connect the x's to the children of the original y. This operation is $y .$ carried out by RCC2.

If the selected nodes x and y' are matched in the target-graph, the production deletes the former and $\pmb { y } ^ { \prime }$ retains the latter. Next, the production proceeds to match the edges $( y , z ) , ( x ^ { \prime } , z )$ , and $( \boldsymbol { y } ^ { \prime } , \boldsymbol { x } ^ { \prime } )$ . The find-all and $\tt a d d - a l 1$ labels ensure that all the children of y(the z's) will be reconnected to $\mathbf { \Delta } _ { \mathbf { \lambda } ^ { X } , } ^ { \prime }$ subject to the requirement that edge $( y , z )$ has the same label as edge $( \boldsymbol { y } ^ { \prime } , \boldsymbol { x } ^ { \prime } )$ , This is forced through the applicability predicate:

$$
\text { ea } (\text { label }, *, (y, z), \text { echance }) = \text { ea } (\text { label }, *, (y ^ {\prime}, x ^ {\prime}), \text { echance }).\tag{12}
$$

Next, the labels that emanate from node x' are bound to the original labels that emanate from x. This is $\pmb { x } ^ { \prime }$ done by setting the labe1 attribute of the edge $( x ^ { \prime } , z )$ to the following attribute transformation expression:

$$
\text { ea } (\text { label }, *, (x, y), \text { echance }).\tag{13}
$$

Finally, the probability attribute o $ { \mathrm { f } } ( x ^ { \prime } , z )$ , which corresponds to $P ( x _ { i } \mid y _ { j } )$ for some $i \mathsf { a n d } j ,$ , must be calculated through Bayes rule:

$$
P (x _ {i} \mid y _ {j}) = P (x _ {i}) P (y _ {j} \mid x _ {i}) / P (y _ {j}).
$$

Now, the values $P ( x _ { i } ) , P ( y _ { j } | x _ { i } )$ , and $P ( y _ { j } )$ are already stored in the graph in the probability attributes of the edges $( x , y ) , ( y , z )$ and $( \boldsymbol { y } ^ { \prime } , \boldsymbol { x } ^ { \prime } )$ ), respectively (the latter was computed by the RCcl production). Hence, RCc2 computes the probability of (x', z) through the following attribute transformation expres- $( x ^ { \prime } ,$ sion:

ea(probability),\*,(x,y),echance)\* ea(probability,\*,(y,z),echance)/ ea(probability,\*,(y',x'),echance).

(14)

Since the topology of the production takes care of all the necessary matchings, the indices associated with each of these edges match up automatically, and there is no need to write any explicit matching predicates (as we have done in RCCl).

## References

Arborist Decision-tree Software, Texas Instruments, Inc. (1982), PO Box 2909, Mail Station 2240, Austin. TX 78769.

Bunke, H., “On the Generative Power of Sequential and Parallel Programmed Graph-Grammars," Com puting, 29 (1982), 89–112.

Göttler, H., “Semantical Description by Two-level Graph-Grammars for Quasihierarchical Graphs," Ap plied Computer Science, 13 (1979), 207–209.

-, “Attributed Graph-Grammars for Graphics," in H. Ehrig, M. Nagl and G. Rozenberg (Eds.), Graph-Grammars and Their Application to Computer Science, Lecture Notes in Computer Science 153, G. Goos and J. Hartmanis (series Eds.) Springer-Verlag, Berlin, 1983.

, “Graph-Grammars and Diagram Editing," in H. Ehrig, M. Nagl, G. Rozenberg and A. Rosenfeld (Eds.), Graph-Grammars and Their Application to Computer Science, Springer-Verlag, Berlin, 1987.

Hopcroft, J. E. and J. D. Ullman, Introduction to Automata Theory, Languages and Computation, Addison-Wesley, Reading, MA, 1979.

Howard, R. A., “The Foundations of Decision Analysis," IEEE Transactions on Systems Science and Cybernetics, SSC-4 (1968), 211–219.

Jones, C. V., "An Introduction to Graph-based Modeling Systems, Part I: Overview," ORSA Journal on Computing, 2, 2 (1990), 136–151.

—, “An Introduction to Graph-based Modeling Systems, Part II: Graph-Grammars and the Implementation," ORSA Journal on Computing, 3 (1991), 180–206.

Kahneman, D., P. Slovic and A. Tversky (Eds.), Judgement under Uncertainty: Heuristics and Biases. Cambridge University Press, Cambridge, 1982.

Lavalle, I. H., Fundamentals of Decision Analysis, Holt, Reinhart & Winston, Inc., New York, 1978.

– and P. C. Fishburn, “Equivalent Decision-trees and Their Associated Strategy Sets," Theory and Decision, 23 (1987), 37–63.

— and K. R. Wapman, "Rolling Back Decision-trees Requires the Independence Axiom," Management Science, 32 (1986), 382–385.

Luce, R. D. and H. Raiffa, Games and Decisions: Introduction and Critical Survey, John Wiley and Sons, New York, 1957.

McNamee, P. and J. Celona, Decision Analysis for the Professional with Supertree, Scientific Press, Palo Alto, CA, 1987.

Nagl, M., "Formal Languages of Labelled Graphs," Computing, 16 (1976), 113–137.

-, “Set Theoretic Approaches to Graph-Grammars," in Graph-Grammars and Their Application to Computer Science, H. Ehrig, M. Nagl, G. Rozenberg and A. Rosenfeld (Eds.), Springer-Verlag, Berlin, 1987, 41–54.

Raiffa, H., Decision Analysis, Random House, New York; 1968, 129.

Reps, T. and T. Teitelbaum, “The Synthesizer Generator," Proc. ACM Sigsoft/Sigplan Symposium on Practical Software Development Environments, ACM Sigplan Notices, 19, 5 (1984), 42–48.

Simon, H. A., Models of Man: Social and Rational, Wiley, New York, 1957

Slovic, P. and A. Tversky, "Who Accepts Savage's Axiom?" Behavioral Science, 19, 34 (1974), 368–373.

Thaler, R., "Toward a Positive Theory of Consumer Choice," J. Econ. Beh. Organ. 1 (1980), 39–60.

Thompson, G. L., "Simplification of Games in Extensive Form," Internat. J. Game Theory, 1 (1972), 147-159.

Tversky, A. and D. Kahneman, “Judgement under Uncertainty: Heuristics and Biases," Science, 185 (1974), 1124–1131.

and , "The Framing of Decisions and the Psychology of Choice," Science, 211 (1981), 453-458.

Von Neumann, J. V. and O. Morgenstern, Theory of Games and Economic Behavior, Princeton University Press, Princeton, NJ, 1953.
