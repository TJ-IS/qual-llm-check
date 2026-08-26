---
otero_id: 17396
otero_key: "4AG3A4YE"
title: "Developments in graph-based modeling for decision support"
authors: "Christopher V. Jones"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0031-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Developments in graph-based modeling for decision support \*

Christopher V. Jones

Simon Fraser University, Burnaby, BC V5A 1S6, Canada

The user interface has long been recognized as one of the key components of a decision support system (DSS). Much recent research has contributed theories, tools and techniques for user interface design and implementation for DSS. Graphs are widely used in DSS to represent complicated problems. Graph-grammars provide a theoretically grounded, practical tool for building user interfaces and some degree of functionality for problem domains where the problem can be represented as a graph. We discuss recent developments for one such line of research – graph-based modeling using graph-grammars.

Keywords: Model management systems; User interface management systems; User interface; Modeling; Graph-grammars; Integrated modeling environments

![](/api/attachments/4AG3A4YE/fulltext/images/5ea2f67b7d38d868ed39aab3ff564332f10f8b97e99d351e0e7ab7e3549a3e1b.jpg)

Christopher V. Jones is an Associate Professor of Management Information Systems and Management Science at the Faculty of Business of Simon Fraser University in Vancouver, Canada. He received his Ph.D. in Operations Research from Cornell University in 1985. Prior to joining the faculty at Simon Fraser, he was a faculty member in the Decision Sciences department of the Wharton School of the University of Pennsylvania. His research interests include user interfaces for modeling, analysis and decision support. He has published in Operations Research, IIE Transactions, Information Systems Research, Decision Support Systems, Annals of OR, and ORSA Journal on Computing. He is currently an area editor for ORSA Journal on Computing. Dr. Jones is a member of the Operations Research Society of America, The Institute of Management Science and the Association for Computing Machinery.

## 1. Introduction

The user interface has long been recognized as an important component of a decision support system (DSS). For example, in the framework for DSS proposed by Bonczek [3]; a DSS is comprised of a language system, problem processing system, and a knowledge system, with the language system being the user interface component. Frankly, in the early days of DSS, a congenial user interface generally meant a line-at-a-time dialog with the DSS using a command language or by responding to computerized questions. With the advent of better hardware and software, the user interface for DSS now often features direct manipulation, or natural language styles, which can provide a much more powerful interface.

Arguably, the user interface has significantly contributed to the success of more than a few DSS tools, systems and generators. Several recent award-winning papers provided sophisticated user interfaces for DSS $[1,24]$ . The success of spreadsheets further supports the argument. Spreadsheets provide no additional functionality beyond what can be provided by programming in FORTRAN. The power of a spreadsheet is that its functionality is made available in such a natural way through the user interface.

Yet building user interfaces, particularly the now ubiquitous multi-window, mouse driven user interfaces remains difficult. The field of user interface management systems (UIMS) has developed tools and techniques to facilitate the creation of user interfaces. As detailed in one of their early works [33], a user interface management system generally facilitates separation of user interface from functionality. Since the idea was formulated in the early 1980's [23], many commercial UIMS have become available, e.g., MacApp [37], NextStep (Weber, 1989), Prototyper [38]. Surveys of recent research in the field can be found in [28,34].

UIMS, almost by definition, are designed only for user interfaces; they do generally not provide functionality. In essence, a UIMS makes it easy, for example, to manipulate the windows in a multi-window user interface, but the application program must still define the behavior of the contents of the window. One approach to specifying behavior of the contents of a window comes from the field of syntax-directed editing $[35,36]$ . A syntax-directed editor functions as a “smart” editor (for text, usually). By smart, we mean that the editor understands the syntax and at least some of the semantics of the language being edited. It can ensure that semi-colons are placed properly, insert pre-defined templates, e.g., IF-THEN-ELSE, with a single keystroke, and even alert the user to undeclared identifiers. An editor generator $[36]$ is a tool to facilitate the construction of syntax-directed editors. The editor generator developed by Reps has been used to construct textual syntax-directed editors for modeling environments $[14,40]$ . As we shall show, an editor generator can provide a surprising degree of functionality in a syntax-directed editor for a particular DSS.

Most of the editor generators to date provide syntax-directed editing only for textual languages. A great many DSS models, however, rely on some type of picture, e.g., decision trees, PERT/CPM, vehicle routing, simulation languages, among others. Over the past several years, we have been developing a graphical editor generator to support such DSS models. The editor generator, NETWORKS, relies on the observation that most such pictorial models can be represented as a network or graph. As we have shown $[17–19,21,22]$ even pictures such as bar charts and Gantt charts, which do not have a readily apparent representation as a graph, can in fact be easily represented by a graph. The purpose of this paper is to discuss the most recent developments of that editor generator and its application to DSS.

## 2. Review of graph-grammar approach

The detailed theoretical underpinnings and extensive examples of the application of graph-grammars have been presented elsewhere. We present a more detailed, but brief review of NETWORKS and graph-grammars.

We assume that some problem holder needs a DSS to support a particular class of decisions. Although they may not have a precise description or model in mind when they begin, the problem holder believes that some form of picture, in particular a graph, can represent the problem at hand well. An editor generator must allow the problem holder or the DSS designer to specify the characteristics of the problem at hand. The graph-based editor generator that we have built, NETWORKS, relies on graph-grammars for this purpose. A graph-grammar consists of a set of operations or productions that can be applied to manipulate a graph. Assuming that the productions are designed properly, as long as the user only uses the defined productions to manipulate a graph, then the graph produced will satisfy the characteristics of the desired model.

The methodology has been developed extensively in previous papers [17-19]. Graph-grammars offer several advantages, including:

Power: Graph-grammars are Turing-complete, meaning that they are as powerful as any general-purpose programming language.

Formality: In a graph-grammar, all permissible manipulations are defined precisely and unambiguously, using a mathematical language.

Executability: The graph-grammar specifications can be implemented on a computer, so that model definitions can be directly executed.

Elegance: In a graph-grammar, both graphs and operations on graphs are defined in terms of a uniform language-graphs.

Extensibility: New productions can be easily defined to manipulate models in ways not envisioned by the original designer.

Generality: The graph-grammar formalism is a general-purpose modeling tool; it can be used to construct any type of graph.

The output of NETWORKS is a syntax-directed editor for a particular class of graphs, i.e., a user interface for representing a particular problem or set of problems. For example, Figure 1 displays four syntax-directed editors created using NETWORKS for four different decision problems (clockwise from the upper left, a bar chart, decision tree, linear programming and project management).

Users manipulate the models in each window using graph-grammar productions tailored for each model. The user can invoke a production simply by selecting it from a pull-down menu. Such editors have been built for a variety of decision science models [20], as well as for general purpose modeling languages such as structured modeling [21] and PM\* [22,25]. Note that graphs can also be used for pictures that are not apparently graphs, e.g., the bar chart of Figure 1.

Syntax-directed editors can provide not only a user interface but some degree of functionality. Powerful productions can be defined that provide a large measure of functionality, if that functionality involves manipulating a graph. For example, for PERT/CPM models, no external algorithm is required to solve the critical path problem; NETWORKS does it elegantly. The critical path displayed as thicker edges in the lower left window of Figure 1 was calculated entirely by NETWORKS. For those cases where a more efficient algorithm is desirable, NETWORKS provide the ability to include external algorithms that can both read from and write to the NETWORKS database, thereby updating the image seen by the user.

By representing both the objects of interest and the operations of objects using the same basic representation scheme, we are following the advice of several authors including $[2,12,15]$ who suggest that modeling environments should be based on a single, unified, theoretically grounded framework. In our case, the single unified framework has proved its mettle again and again. Some of the new features for NETWORKS described in this paper (see, e.g., section 3.1) rely on a graph-based model, e.g., a finite-state automaton. NETWORKS was used to build a syntax-directed editor for such a graph. The syntax directed editor was then included as part of NETWORKS itself, which required less than half a day to develop.

NETWORKS builds user interfaces for attributed graphs. An attributed graph is a graph whose nodes and edges are partitioned into types. In a decision tree application, for example, node types include decision, chance, and outcome; edge types include edecision and echance. Associated with each node and edge type are a collection of attributes, which are similar to domains in a relational database. For example, in a decision tree application, echance edges would have a probability attribute. Underlying attributes can be formulas to calculate the value of the attributes. These formulas are in the spirit of the formulas underlying cells in a spreadsheet. Unlike spreadsheet formulas, the formulas in NETWORKS are designed specifically to work with attributed graphs. NETWORKS provides facilities for defining node and edge types and their attributes. The specific syntax of these attribute formulas is defined in [19].

File Edit Calculation Design Display Debug Linear Programming 156  
![](/api/attachments/4AG3A4YE/fulltext/images/61083287c0479eb21dc77f6c041fa0f7b8115c8775dd2b1528ad114c9042df5c.jpg)  
Fig. 1. Four syntax-directed editors for common decision models. In the upper left is a bar chart, the upper right a decision tree, the lower left a project manager, and the lower right, a graph-based representation of a linear programming problem.

Different types of attributed graphs, however, impose different structural constraints on the allowable graphs. For example, a decision tree must be a tree, whereas many vehicle routing applications insist that the solutions contain cycles. For each type of attributed graph, we define a graph-grammar to enforce such structural restrictions. A graph-grammar consists of a set of operations called productions that can be performed on a graph. A set of graph-grammar productions defines the set of operations that a user can perform on a graph (or apply to a graph) in user interfaces developed using NETWORKS. By limiting the set of allowed operations that can be performed on a graph, one can enforce structural restrictions on the graph. In particular, if the graph-grammar is properly designed, productions, when applied to a graph that already obeys the structural restrictions, will continue to obey them after the production has completed.

We have based our graph-grammar formalism on the one developed originally by Nagl [30,32] and Göttler [6–11]. A graph-grammar production, in its simplest form when applied to a graph (that graph is called the target graph), replaces part of that graph, called the left-hand side, with another graph, called the right-hand side, and then connects the right-hand side to what remains of the target graph. In short, a graph-grammar production contains three parts, denoted $G^{L}$ , $G^{R}$ , and T, where $G^{L}$ is a graph called the left-hand side, $G^{R}$ is a graph called the right-hand side, T is the embedding transformation, which describes how to connect the right-hand side to the target graph. A production is applied to a target graph G, yielding graph $G''$ , in the following steps:

![](/api/attachments/4AG3A4YE/fulltext/images/814e02f86e8f7867b06e2410d855f61a1c5879481c6eb2adf858aa35058fa0d7.jpg)  
Fig. 2. Application of production in Figure 3 to decision node d in the graph on the left, producing the graph on the right.

![](/api/attachments/4AG3A4YE/fulltext/images/c9505bc2b785c4e97d7f69c927589a106bcfd59700b87fd993e3f1a01a552c04.jpg)  
Fig. 3. One production to add a new outcome node(y) as a child of a decision node (originally x, replaced by $x'$ ).

1. Find $G^{\mathrm{L}} \subseteq G$ .

2. Add $G^{R}$ to G, yielding graph $G'$ .

3. Use $T$ to add nodes and edges to connect $G^{\mathbb{R}}$ to $G \setminus G^{\mathbb{L}}$ , yielding $G''$ .

4. Remove $G^{L}$ from $G''$ , yielding $G'''$ , the final result.

The tricky part of a graph-grammar production is the embedding transformation. The graph-grammar formalism connects $G^{\mathbb{R}}$ to $G \setminus G^{\mathbb{L}}$ by considering how $G^{\mathbb{L}}$ is connected to $G \setminus G^{\mathbb{L}}$ . Essentially, the embedding transformation traces paths from nodes in $G^{\mathbb{L}}$ to nodes in $G \setminus G^{\mathbb{L}}$ , and then adds edges (and nodes), called connecting edges and nodes, to connect the nodes found in $G \setminus G^{\mathbb{L}}$ to nodes in $G^{\mathbb{R}}$ .

Consider a production (Figure 3) from a decision tree application to add an outcome node as a child of a decision node, e.g., as shown in Fig. 2.

Note that in Figure 3, the labels find-one, add-one, find-all, and add-all refer to nodes and edges in the left-hand side, right-hand side, embedding transformation, and connecting, respectively. The use of these labels differs slightly from previous work. These new labels are being introduced because they are quite arguably more descriptive than the terms “left,” “right,” “embedding,” and “connecting.”

In this production, outcome node y is to be added as a child to decision node x. Node x is in $G^{L}$ . It will be replaced by a new decision node, $x'$ , which will serve as the actual parent of node y. Node $x'$ is in $G^{R}$ , since it is to be added to the graph. Nodes w and z represent the possible parents of node x. They are part of the embedding transformation (and are labelled find-all) since the parent of node x should be made the parent of node $x'$ . Since the parent of x may be either a decision or a chance node, two nodes are required. The edges from w to $x'$ and from z to $x'$ are connecting (add-all) edges, since they should be added to the graph, if either some node w or z serves as a parent of x. Similarly, the children of x should also be the children of $x'$ . Those children are represented by nodes a, b and c, which are labelled find-all, since they form part of the embedding transformation. The edges emanating from x are labelled find-all, since they are also part of the embedding transformation. The edges from $x'$ to a, b and c are labelled add-all, since they should be added to connect $x'$ to the children of x.

Nagl's original graph-grammar formulation was as theoretically powerful as one could hope [32], in that it is just as powerful as any programming language. As shown with the production of Figure 3, it is not always easy to use, or convenient for many decision support applications. The productions required can be very large. In [18,19], we presented numerous extensions to Nagl's graph-grammar approach that allowed for far more concise productions. For example, the production to add a new outcome node as a child of a decision node, using Jones's extensions appears in Figure 4.

One of Jones's extensions allowed nodes and edge in $G^{\mathrm{L}}$ to be "non-deletable," meaning that they would remain in the target graph after the production is completed. Using that extension allows the much more concise production of Figure 4.

![](/api/attachments/4AG3A4YE/fulltext/images/52878321cf71b805c46742002ca531dce0133117d077507da604fa341a5a4773.jpg)  
Fig. 4. Production to add an outcome node as a child of a decision node using Jones's extensions. Compare to the production of Figure 2.

Since the publication of those papers, further extensions have been developed. The purpose of this paper is to discuss the most recent work to date on NETWORKS and its underlying graph-grammar formulation. This research was inspired by specific, though difficult, examples. These examples seemed to be “naturals” for the graph-grammar approach: the models were graphical, and their structure was easily described in simple English. Although Jones’s (and even Nagl’s) approach could certainly provide the needed capabilities, the solutions developed were less than satisfactory. Therefore, we felt that the extensions presented in the next section were justified, useful, and interesting.

## 3. Extensions

To address the problems discussed in the previous section, several new features have been added, or are being added to NETWORKS. These include:

\- Path edges, which are useful in enforcing acyclicity, as well as for working with trees (Section 3.1).

\- Object-oriented extensions, which support the re-use of productions (Section 3.2).

\- Multiple fragments, which provide capabilities for graph-grammar productions analogous to parentheses for logical (and other types of) expressions (Section 2.3).

## 3.1. Path edges

Some types of graph-based models, e.g., project management problems, forbid cycles. Others require them, e.g., solutions to simple vehicle routing problems. Enforcing acyclicity, using the graph-grammar formulation presented originally in $[18,19]$ was cumbersome at best. In one proposed solution, dummy edges were required to represent the fact that a path existed between the adjacent nodes. Any production that then added or deleted a node or edge had to add and delete the dummy edges, as appropriate. This typically required several productions, each carefully sequenced by a program graph.

![](/api/attachments/4AG3A4YE/fulltext/images/20aef07e768e126a4e67f4ade0f2fe940e96d52c7d9c58ca61684006449c96d2.jpg)  
Fig. 5. Production to add an edge and ensure acyclicity.

The solution was quite simple. Every production now can include edges of a special type, path. Such an edge represents a path between its adjacent nodes. The production to add an edge between two nodes, but preventing any cycles, becomes as shown in Figure 5.

The path edge from y to x labelled not enforces acyclicity. A single edge will be added to connect node x to y if and only if no path exists from y to x. Nodes x and y must have been selected by the user by pointing to them with a mouse or by using another pointing device. Note that we are also using what we hope is a more transparent labelling scheme for the nodes and edges than in the original version (e.g., Jones [18,19]). Instead of the labels left, right, embedding, and connecting, we are using labels given their rough meaning, find-one, add-one, find-all, and add-all, respectively.

Path edges also prove useful in other contexts. When developing a syntax-directed editor for decision trees, it seemed useful to provide a manipulation to delete a subtree. In the original formulation (see Jones [17]), deleting a sub-tree required executing one production repeatedly. That production selected the children of a selected node, and then deleted the selected node.

![](/api/attachments/4AG3A4YE/fulltext/images/deae6bbe1af4de17bbac81b3c25d94443f655509e19349710938ea8ad0a106cb.jpg)  
Fig. 6. Production to delete a subtree using path edges.

Using a path edge, the same manipulation can be provided with the single production shown in Figure 6.

Path edges, by default, only find directed paths. One variation of a path edge allows undirected paths to be found. Such a construct proves useful, for example, if the user wants to delete a connected component of a graph. If we assume the user points to a node in the component to be deleted, then the production to delete the connected component containing that node appears in Figure 7.

Path edges, by default, do not make distinctions about the length of the path or the type of the edges on the path. It is sometimes useful, however, to restrict both. This problem arose when implementing structured modeling $[12]$ using graph-grammars $[21]$ . It was necessary to detect a path consisting of an alternating sequence of incoming edges of one type (next) and outgoing edges of another (inmodule). Again, it would be possible to perform this operation using a (large) set of productions sequenced by a program graph, but a more elegant solution was desired. The solution implemented allows the sequence of edge types on a path to be restricted to a regular expression $[16]$ . Regular expressions are a topic in formal language theory and are used quite often to specify syntax, for example, of numbers and identifiers for programming language compilers. The Unix utility 1 ex generates programs that recognize specific types of regular expressions, i.e., detecting an illegal identifier.

![](/api/attachments/4AG3A4YE/fulltext/images/763703ae8d754eb6e74f9f838370242f5bebb1f621084188360f71c8f45a97ff.jpg)  
Fig. 7. Production to delete a connected component of a graph.

![](/api/attachments/4AG3A4YE/fulltext/images/c8f25c012a2a9ec922fb02d81b343958df44fce1dd5ce0bf9815f356ffea4c8c.jpg)  
Fig. 8. Example of a finite-state automaton used for path edges.

Regular expressions can also be recognized using a finite state automaton, an abstract model of computation, which can conveniently be represented by a graph. The finite state automaton for the structured modeling problem appears in Figure 8.

The graph in Figure 8 is not a production graph. Rather, as a path is being traced by a path edge, imagine a single token moving from node to node in the above graph. The token is positioned first on the node labelled start. The token can only move if there exists an outgoing edge in the above graph whose label (identifying an edge type and direction), matches an edge in the target graph having that type and direction. When the token reaches the node in the above graph labelled stop, then the current path is returned. The \$ label on an edge in the above graph allows the token to make an immediate transition to the adjacent node. In short, the above finite state automaton finds paths starting with at least one incoming edge of type next, and then consisting of alternating series of outgoing inmodule edges and incoming next edges.

Finite state automatons have theoretically less computational power than a Turing machine, but even so, combined with the existing graph-grammar machinery, they can be used to specify complicated graph manipulations. Note that since a finite state automaton is simply another type of graph, NETWORKS can be used to produce a syntax-directed editor. We used NETWORKS to do just that.

## 3.2. Object-oriented extensions

Consider the Hitchcock–Koopmans transportation problem from the field of mathematical programming. Such models can be defined as a set of sources and a set of sinks, each source having a given supply, each sink having a given demand. The unit transportation cost from each source to each sink is also given. The goal is to determine the least cost set of shipments from sources to sinks to satisfy demand while not exceeding supply. In NETWORKS, such a model can be defined quite easily. The sources and sinks are represented by different types of nodes, the source nodes having a supply attribute, the sink nodes having a demand attribute. The unit costs, represented by edges of type link, connect source nodes to sink nodes. The assignment problem is a special case of the transportation problem, with the supply and demands all having value 1. The node and edge types and productions required for an assignment problem, and the node and edge types for a transportation problem are essentially identical. Yet, NETWORKS, as currently designed, does not allow the re-use of elements defined for one type of graph in another type of graph. When one considers the fact that the transportation problem is actually an example of the more general minimum cost network flow problem, which itself is an example of a linear programming problem, one can see that many models could benefit from re-using components from other models.

We seek, therefore, to promote the re-use of node and edge types, as well as productions in NETWORKS. Object-oriented programming has been touted as providing a rich metaphor for promoting software re-use. Although no precise definition exists for object-oriented programming, it has generally come to mean a programming language or system that provides at least the following three characteristics (see, e.g., [26]):

Encapsulation: objects are defined not only by their associated data, but also by the procedures or methods that can operate on the data.

Inheritance: objects can derive methods and data from other types of objects through hierarchical inheritance.

Polymorphism: objects of different types can respond to the same messages.

Software re-use in object-oriented programming is promoted mainly through inheritance. In the network flow example at hand, if a generic network flow model were defined, then to define a special type of network flow model, e.g., the Hitchcock–Koopmans transportation problem, the designer could build on the generic network flow model. The transportation model would inherit the characteristics of the generic model, but could override characteristics of the generic model with versions specific to the transportation problem.

One can trace the roots of object-oriented programming to a variety of sources, including the simulation language, SIMULA, as well as frame-based representation schemes for knowledge representation. Object-oriented programming techniques were first widely adopted in the Smalltalk programming language [5], though now such concepts have been added to traditional third generation programming languages such as C (e.g., C++ [27]).

Object-oriented programming concepts have perhaps had their widest application in user interface development. Modern, multi-window, direct manipulation user interfaces are notoriously difficult to develop. Such interfaces must respond to a variety of possible inputs, both from users, and from other programs, both quickly, and in an easy-to-use manner. Yet, using a traditional third-generation programming language, even the simplest operations can require hundreds of lines of code. Many authors and commercial software vendors have proposed or developed object-oriented tools to facilitate user-interface development. Research tools include $[13,28]$ . Among currently available commercial offerings, these include MacApp $[37]$ , Interface Builder $[41]$ , Object Vision $[4]$ , among others. Object-oriented methodologies provide great economies of scale, since the programmer need not develop standard protocols for moving windows, scrolling information, or printing documents, for example. The objects defined for new applications can inherit those behaviors from pre-defined objects. The programmer needs only to implement the distinguishing behavior of the new application.

Object-oriented programming has also seen use in model-management. Hong, Mannino and Greenberg [15] have developed an object-oriented knowledge representation scheme for mathematical models. They define a hierarchy of models, each descendant inheriting, as in object-oriented programming, the characteristics of the ancestors. For example, at the top of the hierarchy could be a general non-linear mathematical programming problem. One level down in the hierarchy could be linear programming. Further down could be minimum cost network flow problems, then the Hitchcock–Koopmans transportation problem, then the assignment problem. Hong et al. [15] defined formal, useful operators for manipulating the model representations.

Given the above overview of object-oriented programming, we now turn to exploring how to introduce such concepts into NETWORKS. Note that we will not discuss here the use of an object-oriented language such as C++ or Smalltalk to implement the existing capabilities of NETWORKS, or even enhanced capabilities. Rather, since NETWORKS itself is an environment for building user-interfaces, we seek to describe how object-oriented concepts can be introduced into the NETWORKS environment. Whether these extensions are implemented using an object-oriented language or by using a traditional third-generation language is an interesting question, but one that will not be addressed here.

Surprisingly, NETWORKS already adopts some of the ideas of the object-oriented metaphor in certain, specific places. The “object-oriented” features currently existing in NETWORKS, however, are quite far from most existing notions of object-oriented programming. In particular, a simple one-level inheritance mechanism is provided. When a designer specifies a node or edge type, that edge type defines the characteristics of the nodes or edges of that type, respectively. For example, in a transportation problem, a source node type might define its shape to be a circle and its supply to be 0, by default. The user of the instance editor can override those basic definitions for specific source nodes, as desired, for example, to change the supply attribute to a specific value. Similarly, a small measure of encapsulation is provided. Productions are defined for a specific graph-type, and can function only for that graphtype. As such, they appear similar to methods in object-oriented programming, which can operate only on their associated objects. Finally, productions include a universal node and edge type. In the complicated pattern matching that occurs in productions, universal nodes and edges can match any node or edge in the target graph at all. As such, they function as the original ancestor of all node and edge types in the target graph. In other words, they provide a limited form of polymorphism, since they can take on the characteristics of nodes and edges of any type.

We now discuss in more detail our proposal for extending NETWORKS with object-oriented concepts. In particular, recall that a graph type $G = \langle N, E, S \rangle$ in NETWORKS is defined as a 3-tuple consisting of a set of node types, N, a set of edge types, E, and a set of structural constraints S, imposed on the graph. In NETWORKS, S consists of an initial graph and a set of graph-grammar productions for manipulating graphs of that type. In our proposed object-oriented version of NETWORKS, we define a graph subtype of G, G, $H_{G} = \langle N_{G}, E_{G}, S_{G} \rangle$ , to be a graph type, consisting of a set of node types, $N_{G}$ , edge types, $E_{G}$ , and structural constraints, $S_{G}$ , where $H_{G}$ is related to G in the following way:

\- Each node type $n$ in $N$ is the parent of one or more corresponding node types in $N_G$ .

\- Each node type $m$ in $N_G$ is the child of only one node type in $N$ .

\- Children inherit the parent's attribute definitions.

\- Children can change the default formula for an inherited attribute.

\- Children can add new attributes to their attribute definitions.

\- The edge types in $E_G$ are related to the edge types in $E$ , in a similar way.

\- $S_{G}$ can inherit production from $S$ .

\- $S_{G}$ can override productions from $S$ .

\- $S_{G}$ can include new productions.

\- $S_{G}$ can forbid the application of productions from $S$ .

\- Some of the productions in $S$ and $S_G$ can be private, i.e., not visible to the user.

We now illustrate these concepts through an example. Consider a general NETWORKS model for minimum cost network flow problems. The designer might define a minimum cost network flow graph type, M, having single node type, netnode, with shape $\bullet$ , having attributes name and dual, and a single edge type, netedge, with shape →, having attributes cost, capacity and flow.

![](/api/attachments/4AG3A4YE/fulltext/images/7f867e82655d7b0d33e5ea1225dc5b89b5bfa4e6ad9d0a26f43eb0b3f39d0b1f.jpg)  
Fig. 9. Production to add a netedge.  
Fig. 10. Production to delete a netnode.

![](/api/attachments/4AG3A4YE/fulltext/images/f32322d517f8a92637e19cdc2953122143870abffbc00bd727e25af637fff21b.jpg)  
find one,
selectbefore,
delete

Four productions are defined, to add and delete a single node or edge, respectively. The production to add a netedge appears in Figure 9.

The production to delete a netnode appears in Figure 10. The other two productions are equally simple.

A transportation problem graph type can now be defined as a sub graph type, $H_{M}$ , of M. Graph type M defines two types of nodes, source, having shape ○, and sink, having shape □, each having a netnode as a parent, and one type of edge, link, whose parent is a netedge. Source nodes have a new demand attribute and sink nodes have a new supply attribute.

The production to delete a node can be simply inherited, since the behavior for nodes (source or sink) in transportation graphs is the same as for the more general case. The production to add a new edge must be overridden, however, because no edges are allowed to connect two source or two sink nodes. Rather, edges can only connect a source to a sink node. That production appears in Figure 11. Note that it is essentially equivalent to the parent's version, but the "from-node" has type source, and the "to-node" has type sink.

In a transportation graph, when a source is added, the modeler might wish to connect it to all the other sink nodes. Similarly, when a sink is added, it might be useful, on occasion, to connect it to all the other source nodes. To do so, we therefore include two productions to add source and sink nodes. The production to add a source and connect it to all sinks is shown in Figure 12. The other production is similar.

![](/api/attachments/4AG3A4YE/fulltext/images/167275c86fd4e4344c787d8ff171e4eaf684eadd26359e55cfac9bb49511ebf4.jpg)  
Fig. 11. Production to add a link edge.

![](/api/attachments/4AG3A4YE/fulltext/images/9ca8dc7257bcb5c8488aafb50f6ee147ebfcf1e92d8b724b78136856538f6e27.jpg)  
Fig. 12. Production to add a source node.

Since productions can be inherited, and the node and edge types of a child graph type need not be the same as the node and edge types in the parent graph type, the pattern matching machinery in graph-grammar productions must be altered. For example, the production to delete a netnode that is inherited by transportation problem graphs specifies a netnode, not a source or sink. Yet, since source and sink nodes are children of netnodes, the matching should occur. More specifically, a production should match node n in a production graph to node $n'$ in a target graph if node $n'$ has the same type as n or if an ancestor of $n'$ has the same type as n. Note that if node n in a production graph is of a descendant type of node $n'$ in the target graph, no match should occur.

As is common in object-oriented programming, we define a universal graph type to be a common ancestor for all graph types. The universal graph type defines a single universal node type and a single universal edge type, which form the parents of all other node and edge types. Note that the universal node and edge types are specifically meant to correspond to the current universal node and edge types used in graph-grammar productions in NETWORKS. Four productions are provided, to add and delete a single node or edge at a time, essentially equivalent to those defined for a general minimum cost network flow model. In fact, the network flow model would simply inherit those productions from the universal graph type.

The above currently represents a basic design of an object-oriented version of NETWORKS. It has not yet been implemented. We note here, however, that inheritance hierarchies can be conveniently represented as a graph. For example, a simple hierarchy of graph-types might appear as in Figure 13.

![](/api/attachments/4AG3A4YE/fulltext/images/1dbe519f5eaaba7cf79dd244a434ca1aa9d2ea8d37ac1bfa4ab1ac88604b31e4.jpg)  
Fig. 13. Fig. 13. Possible graph representing inheritance hierarchies among graph-types.

Given NETWORKS's facility with constructing interfaces for the manipulation of graphs, we are encouraged that we will be able to provide congenial interfaces quickly for these object-oriented extensions.

## 3.3. Fragment graphs

Consider a seemingly simple operation to duplicate a two-level tree such as shown in Figure 14.

One might expect that the corresponding graph-grammar production would be quite simple. In fact, one might expect the production to appear as in Figure 15.

Node $r'$ represents the root of the tree, and node $x'$ represents all the children of $r'$ . Node $r''$ represents the duplicated root and node $x''$ represents the duplicated children. The above production does not work as expected, however. The reason is buried within the detailed definition of how productions are applied (see [19]). The add-all label on $x''$ roughly translates to: "For the find-all nodes and edges in the production graph that are connected to $x''$ , find all the corresponding nodes and edges in the target graph and add a node corresponding to $x''$ to the target graph,". Node $x''$ is not connected to any find-all nodes or edges at all, least of all node $x'$ . Therefore, no new nodes or edges are added to the graph. One solution is to add an additional edge to the production to accomplish this, e.g., Figure 16.

![](/api/attachments/4AG3A4YE/fulltext/images/88b28b81d9e69b35bedb2046139a2f0b334205fc239ed3e31fa528d362b5547c.jpg)  
Fig. 14. A simple two-level tree.

![](/api/attachments/4AG3A4YE/fulltext/images/9390983b98090c83fe443784b058325f5ea9ab36d903c8e4ab23739ceee53d1a.jpg)  
Fig. 15. Proposed production to delete a two-level tree.

Edge $(x''', x')$ accomplishes the task of associating $x''$ to each $x'$ found in the target graph. Its add-all label implies that one such edge be added for each node corresponding to $x'$ found in the target graph. Certainly such edges should not remain in the target graph. We therefore augment the label on edge $(x'', x')$ with the delete label, since that edge should not remain after the production completes. This seemingly contradictory construction has been implemented and used in NETWORKS.

![](/api/attachments/4AG3A4YE/fulltext/images/3883d888b0a1d496ee0d8d5cac9c2fb639dadf784febafc80c7c39910388db01.jpg)  
Fig. 16. Production to duplicate a two-level using the add-all, delete construction.

This example points out a more general problem, however. If one were using formal logic, as one could, to specify manipulations on graphs, well-formed formulas (WFFs) would be constructed using atoms and predicates as well as logical connectors ∧ (and), ∨ (or), ¬ (not), the logical quantifiers ∀ (for all) and ∃ (there exists), and, most importantly for the problem at hand, parentheses to group WFFs into larger WFFs. In our version of graph-grammar productions, we have constructs similar to atoms, predicates, logical connectors and logical quantifiers. Nodes and edges correspond to atoms; labels such as find-all and find-one correspond to ∀ (for all) and ∃ (there exists); careful construction of the production graphs can mimic the and, or and not connectives.

What is missing from the current graph-grammar formulation used in NETWORKS, however, is a general notion of grouping, such as provided by parentheses. In the most recent example, if one could group $x''$ and $x'$ together, then one need not use an additional edge with its rather awkward add-all/delete label. The current grouping construct in NETWORKS is based on the notion of a fragment. A fragment, roughly, consists of a maximally connected set of nodes and edges having either the label find-all or add-all. Nodes (but not edges) having labels find-one and add-one are allowed in fragment graphs, but they cannot be used to connect find-all and add-all nodes and edges together into one fragment. See Jones [19] for the complete definition. In the production of Figure 15, there are two fragments, i.e., Figure 17.

In contrast, the production of figure 16, with its additional edge, has a single fragment, i.e., Figure 18.

![](/api/attachments/4AG3A4YE/fulltext/images/52aa55224139c25efa52075bc1dac2fe08749ebae539f36dc966424f8b52def8.jpg)  
Fig. 17. The two fragments of the production in Figure 15.

![](/api/attachments/4AG3A4YE/fulltext/images/b8ec4911dc1df533a02ab35376868519ad82cc4e9dae92f2d08bb33436f9092c.jpg)  
Fig. 18. The single fragment of the production in Figure 16.

Fragments group nodes and edges together because find-all and add-all labels are associated only with the nodes and edges in a fragment. This explains why the originally proposed production of Figure 15 did not work properly. Nodes $x''$ and $x'$ were in different fragments.

This problem arises because fragments are only determined by the structural properties of the production graph. Although this mechanism is usually exactly what is desired, as seen in this example we might want to override that mechanism. In particular, we propose adding a new class of label to nodes and edges in a production graph, the fragment identifier. Its default is 0, indicating that the traditional fragment identification procedure should be applied. If non-zero, however, all nodes and edges in the production graph sharing that non-zero identifier should be considered to be part of the same fragment. The production to duplicate a two-level decision tree, with this additional construct, therefore becomes as is indicated in Figure 19.

![](/api/attachments/4AG3A4YE/fulltext/images/318bc275d507b915d4d3e98dad3c8861f49d142ba8994a686abbae0e25722869.jpg)  
Fig. 19. Production to duplicate a two-level tree using fragment identifiers.

![](/api/attachments/4AG3A4YE/fulltext/images/7ead3079a08f74d686000e5bb15573cb8e9584ceb507b4bd89df5e3e5a641767.jpg)  
Fig. 20. A three-level tree.

Fragment identifiers allow more general grouping capabilities, however. Consider the slightly more difficult problem of duplicating a three-level tree, e.g., as shown in Figure 20. One might propose the production in Figure 21 to perform this duplication.

The production in Figure 21, if applied to the graph of Figure 20, however, would produce the graph of Figure 22, which is not the desired result at all. Although the proper number of leaves were constructed by the production, there should only be three nodes at level two in the tree. The problem arises because all the find-all nodes and edges are in the same fragment. If we recast the production of Figure 21 so that nodes $a'$ and $a''$ are in a common fragment different from fragment 1 (Figure 23), the production will have the desired effect.

![](/api/attachments/4AG3A4YE/fulltext/images/53d5e6afcb7925251c0a57e19bc0461eca4eb0b4003c5e4275f27a69c5343135.jpg)  
Fig. 21. Proposed production to duplicate a three-level tree.

![](/api/attachments/4AG3A4YE/fulltext/images/b75740f9c19e10f963f27998a1c9b23649042a0a0ebed9c40c1836c4929e3ae4.jpg)  
Fig. 22. Resulting graph after application of production in Figure 21 to the graph in Figure 20.

The production of Figure 23 translates roughly to: “Find the root, $r'$ , in the graph. Next, find all children, $x'$ , of the root. Then, for each child, $x'$ , add a copy, $x''$ to the target graph. Furthermore, find all of the children of $x'$ , represented by $a'$ , and add one copy, $a''$ , for each child found.”

The best alternative to this production would require several productions executed in a sequence controlled by a program-graph.

Fragment identifiers have not yet been implemented in NETWORKS.

![](/api/attachments/4AG3A4YE/fulltext/images/e0604306ea0e19a79e00a6db830d25391c7aebe82e017a4d3b537c4c4149e9fb.jpg)  
Fig. 23. Correct production to duplicate a three-level tree.

## 4. Conclusions

NETWORKS provides capabilities for easily building syntax-directed, visual editors for the wide variety of DSS problems that can be represented as a graph. Graph-grammars, at the heart of NETWORKS, provide sophisticated tools for manipulating models represented as graphs. Although graph-grammars provide theoretically as much computational power as possible to manipulate graphs, they are not always convenient. This paper has presented some examples of where they are inconvenient, and three extensions to the original graph-grammar formulation originally used in NETWORKS to facilitate several common, yet originally difficult situations.

The first extension, path edges, facilitated enforcement of acyclicity in project management applications, as well as for providing manipulations such as deleting subtrees for decision trees. The second extension, based on ideas from object-oriented programming, has the potential to allow graph type definitions and graph-grammar productions to be re-used in a careful, principled manner. The last extension, graph-grammar fragment identifiers, provides capabilities analogous to simple parentheses in many textual languages, e.g., those for formal logic.

Path edges have been implemented in NETWORKS. The other two extensions are currently being implemented. Further extensions such as those presented here might very well be useful for specific contexts, not yet envisioned.

## References

[1] Angehrn, A.A., and Lüthi, H.-J., Intelligent Decision Support Systems: A Visual Interactive Approach, Interfaces, Vol. 2, No. 6, 1990, pp. 17–28.

[2] Bhargava, H.K. and Kimbrough, S.O., On Embedded Languages for Model Management, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, ed. by Jay F. Nunamaker, IEEE Computer Society Press, Los Alamitos, CA, 1990, pp. 443–452.

[3] Bonczek, R.H., Holsapple, C.W., and Whinston, A.B., Foundations of Decision Support Systems, Academic Press, New York, 1981.

[4] Turbo Pascal For Windows: Windows Programming Guide, Borland International, Inc., Scotts Valley, CA, 1991.

[5] Goldberg, A. and Robson, D. Smalltalk-80 - The Language and its Implementation, Addison-Wesley, Reading, MA, 1983.

[6] Göttler, H., Semantical description by two-level graph-grammars for quasihierarchical graphs, Applied Computer Science, Vol. 13, 1979, pp. 207–209.

[7] Göttler, H., Attributed graph-grammars for graphics in: Graph-Grammars and their Application to Computer Science, 1983, pp. 130–142. ed. by Ehrig, H., Nagl, M. and Rozenberg, G. Lecture Notes in Computer Science, Vol. 153, Springer-Verlag, Berlin.

[8] Göttler, H. Implementation of attributed graph grammars, in: Proceedings of the WG '84 International Workshop on Graphtheoretic Concepts in Computer Science, Universitätsverlag Rudolf Trauner, Linz, 1984.

[9] Göttler, H., Graph-grammars and diagram editing, in: Graph-Grammars and their Application to Computer Science, ed. by Ehrig, H., Nagl, M., Rozenberg, G., Rosenfeld, A. Springer-Verlag, Berlin.

[10] Göttler, H., Graph grammars, a new paradigm for implementing visual languages, Presented at SOFSEM '88, Zotavovna ROH Petr Bezruç, Beskydy, Czechoslovakia, 27 November – 9 December, 1988.

[11] Göttler, H., Graph grammars, a new paradigm for implementing visual languages, in: Rewriting Techniques and Applications, ed. by N. Dershowitz, Lecture Notes in Computer Science, Vol. 355, Springer-Verlag, Berlin, 1989.

[12] Geoffrion, A.M., An Introduction to Structured Modeling, Management Science, Vol. 33, 1987, pp. 547–588.

[13] Green, M., The University of Alberta User Interface Management System, Computer Graphics, Vol. 19, No. 3, 1985, pp. 205–213.

[14] Holsapple, C.W., Park, S., and Whinston, A.B., Generating Structure Editor Interfaces for OR Procedures, Technical report, Center for Robotics and Manufacturing Systems, University of Kentucky, Lexington, KY, 1989.

[15] Hong, S.N., Mannino, M.V., and Greenberg, B.S., Inheritance and Instantiation in Model Management, Proceedings of the 23rd Hawaii International Conference on System Sciences, Vol. III, 1990, pp. 424–432.

[16] Hopcroft, J.E., and Ullman, J.D. Introduction to Automata Theory, Languages, and Computation, Addison-Wesley, Reading, MA, 1979.

[17] Jones, C.V., An Example Based Introduction to Graph-Based Modeling, Proceedings of the Twenty-Third Annual Hawaii Conference on the System Sciences, Kona, HI, 1989, pp. 433–442.

[18] Jones, C.V., An Introduction to Graph-Based Modeling Systems, Part I: Overview, ORSA Journal on Computing, Vol. 2 No. 2, 1990, pp. 136–151.

[19] Jones, C.V., An Introduction to Graph-Based Modeling Systems, Part II: Graph-Grammars and the Implementation, ORSA Journal on Computing, Vol. 3, No. 3, 1991, pp. 180–206.

[20] Jones, C.V., An Integrated Modeling Environment Based on Attributed Graphs and Graph-Grammars, Decision Support Systems, Vol. 10, 1993, pp. 255–275.

[21] Jones, C.V., Attributed Graphs, Graph-Grammars, and Structured Modeling, Annals of OR, Vol. 38, 1992, pp. 281–324.

[22] Jones, C.V., and Krishnan, R., A Visual, Syntax-Directed Environment for Automated Model Development, Technical Report, Faculty of Business Administration, Simon Fraser University, Burnaby, BC, Canada, 1990.

[23] Kasik, D.J., A User Interface Management System, Computer Graphics, Vol. 16, No. 3, 1982, pp. 99–106.

[24] Kimbrough, S.O., Pritchett, C.W., Bieber, M.P., and H.K. Bhargava, The Coast Guard's KSS Project, Interfaces, Vol. 20 No. 6, 1990, pp. 15–16.

[25] Krishnan, R., A Logic Modeling Language for Model Construction, Decision Support Systems, Vol. 6, 1990, pp. 123–152.

[26] McGregor, J.D., and Korson, T., Object-Oriented Design, Comm. of the ACM, Vol. 33 No. 9, 1990, pp. 39–60.

[27] Mullin, B., Object-oriented Program Design with Examples in C++, Addison-Wesley, Reading, MA, 1989.

[28] Myers, B.A., User Interface Tools: Introduction and Survey, IEEE Software, Vol. 6 No. 1, 1989, pp. 15–23.

[29] Myers, B.A., Guise, D.A., Dannenberg, R.B., Vander Zanden, B., Kosbie, D.S., Pervin, E., Mickish, A., and Marchal, P., Garnet: Comprehensive Support for Graphical, Highly Interactive User Interfaces, IEEE Computer, Vol. 23 No. 11, 1990, pp. 71–85.

[30] Nagl, M., Formal languages of labelled graphs, Computing, Vol. 16, 1976, pp. 113–137.

[31] Nagl, M., A tutorial and bibliographical survey on graph-grammars, in: Graph-Grammars and their Application to Computer Science and Biology, ed. by V. Claus, H. Ehrig, and Rozenberg, G. 1979, pp. 70–126, Lecture Notes in Computer Science 73, G. Goos and J. Hartmanis (eds.), Springer-Verlag, Berlin.

[32] Nagl, M., Set theoretic approaches to graph grammars, in: Graph-Grammars and their Application to Computer Science, ed. by Ehrig, H., Nagl, M., Rozenberg, G., and Rosenfeld, A. Springer-Verlag, Berlin, 1987, pp. 41–54.

[33] User Interface Management Systems, ed. by Pfaff, G.E., Springer-Verlag, Berlin, 1985.

[34] Rathnam, S., and Mannino, M.V., User Interface Management Systems: Themes and Variations – A Review of the Literature, Proceedings of the 24th Annual Hawaii International Conference on the System Sciences, 1991, pp. 489–498.

[35] Reps, T. and Teitelbaum, T. The Cornell Program Synthesizer: A Syntax-Directed Programming Environment, Comm. of the ACM, Vol. 24 No. 9, 1981, pp. 563–573.

[36] Reps, T.W., Generating Language-Based Environment, The MIT Press, Cambridge, MA, 1986.

[37] Schmucker, K.J., Object-Oriented Programming for the Macintosh, Hayden Book Company, Hasbrouck Heights, NJ, 1986.

[38] Prototyper, Portland, OR, Smethers-Barnes, 1989.

[39] Turban, E., Decision Support and Expert Systems: Managerial Perspectives, MacMillan, New York, 1990.

[40] Vicuña, F., Semantic Formalization in Mathematical Modeling Languages, unpublished Ph.D. Thesis, Computer Science Department, UCLA, 1990.

[41] Webster, B., The NeXT Book, Addison-Wesley, Reading, MA, 1989.
