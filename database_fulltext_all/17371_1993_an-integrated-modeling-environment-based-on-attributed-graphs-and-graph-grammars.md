---
otero_id: 17371
otero_key: "XQFXX494"
title: "An integrated modeling environment based on attributed graphs and graph-grammars"
authors: "Chris Jones"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90063-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An integrated modeling environment based on attributed graphs and graph-grammars

Chris Jones

Simon Fraser University, Burnaby, BC, Canada

Different types of graphs are widely used to represent many types of management science models. Examples include vehicle routing, production planning, simulation and decision trees. In previous work, the author has developed tools and techniques based on graph-grammars to provide interfaces for such models. In this paper, we explore several such models with particular emphasis on integrating different graph-based models within a single environment. It is shown how the environment can combine a variety of visual models in different ways.

Keywords: Model management systems; User interface management systems; User interface; Modeling; Graph-grammars; Integrated modeling environments

![](/api/attachments/XQFXX494/fulltext/images/d598d41376b7cd3a4b2853fe1754f5ea7102c8ab7955658a098f04d05147a6f5.jpg)

Christopher V. Jones is an Associate Professor of Management Information Systems and Management Science at the Faculty of Business of Simon Fraser University in Vancouver, Canada. He received his Ph.D. in Operations Research from Cornell University in 1985. Prior to joining the faculty at Simon Fraser, he was a faculty member in the Decision Sciences department of the Wharton School of the University of Pennsylvania. His research interests include user interfaces for modeling, analysis and decision support. He has published in Operations Research, IIE Transactions, and ORSA Journal on Computing. Dr. Jones is a member of the Operations Research Society of America, The Institute of Management Science and the Association for Computing Machinery.

Correspondence to: Professor Chris Jones, Faculty of Business Administration, Simon Fraser University, Burnaby, BC V5A 1S6, Canada.

## 1. Introduction

Although models are frequently represented using text-based languages, models are also often represented, at least informally, as pictures. Many of those pictures involve different types of graphs or networks. Examples include project management (e.g., PERT and CPM), decision trees, minimum cost network flow, vehicle routing, systems analysis and design (e.g., flowcharts, data flow diagrams, structure charts). Most of these pictorial models have been specified in a more or less ad hoc fashion. Ad hoc does not necessarily imply imprecise; it implies that there is no generally accepted methodology for specifying pictorial, or more precisely, graph-based models. We seek in this paper, to illustrate a formal, theoretically powerful methodology for expressing and manipulating graph-based models. In particular, using a specific technique from research on formal languages, graph-grammars, we illustrate formally how graph-based models can be represented, constructed and changed. Such a formal specification methodology provides several benefits. It allows us to build visual, direct-manipulation interfaces ([27,55]) that have been developed for such models ([1,2,18,42,57]) but that remain difficult to construct [46,48]. It provides a theoretically powerful capability for operating on, i.e., building, combining, and changing graph-based models in non-trivial ways. It provides a great deal of support in preventing errors in model specification, since the model builder can be prohibited from performing operations that could yield invalid models. It allows us to specify such models rigorously, and like the models themselves, the specification itself is a graph-based model. By relying on a single representation framework for both one's models and useful operations on one's models, we provide quite easily a rich set of integrated functions to support model development and manipulation. These capabilities are provided because of our reliance on a theoretically powerful paradigm capable of manipulating a single, common representation format for models - attributed graphs.

In [28,30], the author developed in detail the theoretical foundations of the approach, as well as a prototype implementation, Networks. This paper seeks to illustrate how the research (and the implementation) can be applied to a variety of 'classic' models and techniques – decision trees, linear programming, critical path, and presentation graphics – and explores how the machinery can integrate these models and techniques in useful ways. To foreshadow the examples we shall illustrate, and integrate, consider the following (abstract) scenario:

A decision-making problem (of some sort) is amenable to analysis by a decision tree. The decision tree will be used to provide a high-level decision making framework for the decision process by representing a variety of scenarios concretely. The values of the leaves (as well as the probability values) of the decision tree, must be determined, of course. Those values are to be developed through a variety of techniques, e.g., from accounting data, from educated guesses, and from more formal modeling techniques such as linear programming. Also, although the decision tree (as well as other graph-based models), might be considered to be a lucid representation, other representation formats are desired. For example, for the decision tree, it is desired to present summaries of several of the different scenarios using traditional presentation graphics (such as bar charts). The modeling process itself must also be managed and controlled. Project management tools such as the critical path method have frequently been used to manage large projects, e.g., in software development and construction, and shall be used in this instance to manage the modeling project itself.

The above scenario, although abstract, illustrates several realistic requirements for integrated modeling, i.e., the need to support and link together a variety of models, the need to provide tools and techniques not traditionally considered a part of management science practice, e.g., presentation graphics, and the need to manage the modeling process itself. In this paper, we shall show the ability of Networks to allow modelers to link models together as well as recalculate and redisplay automatically the results of different models when the data changes. We shall further show that presentation graphics representations can be modeled as a particular type of graph, which thereby allows such capabilities to be constructed using graph-grammars. We shall also show how Networks can be used to construct graph-based models for the critical path method that can then be used to manage the development of other (graph-based) models within Networks itself.

In fig. 1, we show several of the models mentioned above that have been constructed using the machinery that has been developed. The figure comes from the prototype implementation. At the lower right is a linear programming model, whose optimal value is used as the value for a leaf in a decision tree model at the upper right. In the upper left corner, the expected values for each of the three possible choices in the decision tree have been plotted as a bar chart graph. In the lower left corner, a project management model (based on the critical path method) was used to represent interdependencies among these models, and also to capture the estimated time needed to construct each of the models. In this project management model, each task represents another model, some of which are displayed in the figure; in fact, those other models can be viewed and edited, essentially by selecting the appropriate task in the project management model, much like iconic operating systems provided on, e.g., Apple Macintosh computers.

In conclusion, in this paper, we discuss the ability of Networks to express a variety of traditional models as graphs, to link them together, and, in fact, to manage their development. The use of a rigorous, general, and theoretically powerful technique – graphgrammars – provides a basis for a variety of model management functions, including model construction, including a direct-manipulation, computer graphics interface, and model integration.

## 2. Outline of paper

We begin our discussion by presenting an overview of Networks (section 3). We then present in detail the graph-based models illustrated in fig. 1 (sections 4–7) that will then be used to illustrate model integration capabilities (section 8). In presenting the examples, we introduce graph-grammars, first applied to modeling in [30], which provide a convenient, syntax directed approach to specifying rules for constructing and editing different types of graph-based models. Moreover, we discuss extensions to the graph-grammar methodology originally presented in [30] that significantly extend the power of the approach. In section 9, we relate the model integration capabilities of Networks to other approaches to integrated modeling. We conclude the paper with directions for future research (section 10).

## 3. Overview of Networks

We now provide a brief overview of Networks, before turning to specific applications of Networks (and the integration thereof) in subsequent sections. Networks is a graph-based modeling system (GBMS) [30], which provides an environment for building user interfaces that support the construction and editing of specific types of attributed graphs (attributed graphs are merely graphs whose node and edges are partitioned into different types, for which each type defines a set of values (domains in a relational database sense) that we call attributes). In other words, Networks is an environment for building modeling environments. If a modeler wishes to use decision trees (see, e.g., [52]) to solve a particular problem, through Networks, a user interface for working with decision trees could be built quite quickly. Similarly, Networks could be used to build a user interface for other classes of graphs, e.g., critical path.

Networks supports at least two categories of users, a designer, and a modeler. The designer uses Networks to create specific instance editors, to be used by modelers to build specific instances of a particular type of graph. An instance editor for a decision tree would have features specific to the problem of editing and building decision trees. It would allow a modeler, e.g., to add new outcomes, insert new decisions, delete subtrees while continually ensuring that the graph instance remains a valid decision tree. The designer/modeler dichotomy is essentially analogous to the programmer/end-user dichotomy found in software development.

Networks relies heavily on graph-grammars ([43,44], [21,22,23]), a formal technique for specifying manipulations to attributed graphs. Graph-grammars provide several advantages for providing a graph-based modeling system. These include:

\- specific orientation to the manipulation of graphs, a widely used format for representing models;

\- a firm theoretical foundation based on the theory of formal languages that helps provide clear specifications for models expressed as graphs;

\- a convenient visual language representing the manipulations (called productions in graph-grammar parlance) that can be performed on a graph. In particular, productions can be represented as a graph;

\- theoretically sufficient power for any computable class of graphs;

\- independence from any particular solution technique.

Networks allows a designer to limit the set of allowable changes a modeler can make to a graph. In fact, if correctly designed, those set of changes can prevent the modeler from constructing a syntactically invalid model (as we shall see in subsequent examples). This approach is in the tradition of syntax-directed editors, e.g., [53]. Originally conceived for the text-editing of computer programs, a syntax-directed editor understands the structure of the programming language, e.g., FORTRAN. Armed with that knowledge, the syntax-directed editor restricts the allowable changes that the user can make to the computer program, e.g., providing a single command to enter an If-Then-Else construct. By careful design of the changes the user is allowed to make in an instance editor, one can help the user construct only a syntactically correct computer program (though it still may have an infinite loop). In Networks, we are extending the range of applicability of the syntax directed approach both to management science models as well as to visual models.

Furthermore, the approach to modeling is not oriented specifically to techniques such as linear programming, decision trees, project management, or computer simulation. Rather, it provides support for how many people actually represent their models rather than for how people will eventually analyze their models. In fact, most of our discussion will be concerned not with algorithms used to analyze models, but with how to go about representing (and operating on) models. This will prove to be a key to being able to integrate models from widely different areas.

Finally, graph-grammars, despite their advantages, remain relatively unknown within the decision and management science and community. In this paper, in presenting the examples, we shall provide enough material to give an understanding of graph-grammars, but the reader is referred to $[30]$ for more detail.

We now discuss several models (individually) that are widely used in the decision and management sciences (sections 4–7). We will then proceed to show how those models can be combined within Networks to support many parts of the modeling life-cycle (section 8). Those models are decision trees (section 4), linear programming (section 5), and the critical path method (section 6). We also show how Networks can provide presentation style graphics (section 7). The linear programming model is used to determine values for one of the outcomes of the decision tree; the critical path model is used to organize the models. The presentation graphics model is used to summarize the results of the analyses.

## 4. Decision trees

Recall from the previous section that a designer uses Networks to construct an instance editor for a particular class of models. To create an instance editor for decision tree models, the designer would specify the different types of nodes and edges that should appear in the desired graph-based model as well as their attributes. For example, in a decision tree application, node types would include decision, probabilistic, and leaf nodes, where nodes of type decision represent choices to be made, nodes of type probabilistic represent uncertain events, and leaf nodes represent the leaves of the tree. Edge types would include choice, representing the possible alternatives at a decision node, and outcome, representing uncertain events that occur at probabilistic nodes.

## 4.1. Attributes

Underlying each node and edge type are attributes that are values chosen from a particular domain. For decision trees, each node has a name and value attribute. The value attribute gives the value of the subtree rooted at that node; similarly, each choice edge has a chosen attribute whose value equals 1 if that decision produces the highest expected value, and 0, otherwise. Attributes are similar to domains in a relational database, except that their values can be computed rather than determined simply by a table-lookup.

Furthermore, for many types of graph-based models, and certainly for decision trees, the values of attributes, e.g., the chosen attribute of choice edges or the value attribute of decision and probabilistic nodes, can be determined by formulas, much like the values of cells in a spreadsheet. The syntax and semantics of these formulas allow the designer to specify values based on the connectivity properties of the graph. For example, this allows the designer to define the formulas necessary to compute the expected value of decision trees and to solve critical path problems. The syntax of the formulas used in Networks is based on Prolog [12], and is described in more detail in [30]. Variables (unknowns) are denoted by alphabetic symbols whose first character is upper case, whereas knowns are denoted by alphabetic symbols whose first character is lowercase. Briefly, a node is stored as the predicate node(GraphID, NodeID, NodeType), and an edge is stored as the predicate edge(GraphID, EdgeID, EdgeType, FromNode, ToNode). The syntax provides the ability to determine the maximum value of an expression taken over a collection of nodes or edges with particular properties.

For example, attribute formulas can be used to "solve a decision tree", i.e. to determine the optimal decisions and the maximum expected value. For a decision tree, the value of the value attribute of a decision node is determined by the formula $imax(edge(*,Edge,choice,*,To),na(value,*,To,Any))$ where:

\- The expression $na(value, *, To, Any)$ returns the value attribute of node $To$ of type $Any$ in the current graph (denoted by \* in the expression).

The predicate na stands for “node attribute”, and similarly, the predicate ea stands for “edge attribute”;

\- the expression edge(\*,Edge,choice,\*,To) finds an edge (instantiated by Edge) of type choice emanating from the current decision node (denoted by the second \*). Variable To will be instantiated to one of the children of the current node;

\- the expression $imax(A,B)$ returns the maximum value for B for all possible values of A. So, in this particular case, the overall expression determines the maximum of all the value attributes of all the children of this node.

The formulas defining the values of the other attributes can be defined similarly. These formulas are used to determine the value attribute for probabilistic nodes, as well as the value of the chosen attribute for choice nodes. Note further that the values of attributes can refer to the values of attributes in other graphs. This provides one simple way to integrate different models.

This style of integration will be discussed in more detail in section 8.

## 4.2. Bindings

Each node or edge has a set of predefined attributes called bindings that control how the node or edge is displayed. Among the bindings for a node are shape, color, and position (x and y); for an edge the bindings include its color, width and shape of the edge. In a decision tree, the optimal choice edge emanating from a decision node can be colored red using the formula if(ea(chosen) = 1, red, green) to compute the color binding of the edge. Bindings allow the easy construction of presentation graphics, as will be shown in section 7.

## 4.3. Structural constraints

Different types of graphs place different restrictions on the allowable structure of a graph.

File Edit Calculation Design Display Debug Linear Programming 156  
![](/api/attachments/XQFXX494/fulltext/images/3ddecf8a7cc9140efe26fab77d5de8857953fcd5dcb376341d2dc66f2a8a291f.jpg)  
Fig. 1. A set of interrelated models. A critical path model is used to sequence and plan the entire modeling process (g89). The solution to a linear programming model (g3) is used to provide the outcome for the top-most leaf (lp1) of the decision tree (g94). A network flow model, not shown, is used to provide the outcome for another leaf of a decision tree (Outcome 2). The decision at the root of the decision tree is summarized using a bar chart (g93), which is actually a graph drawn so as to look like a bar chart.

For project management, the graphs must be acyclic. For vehicle routing, where vehicles must return to their point of origin, the graphs must be cyclic. Furthermore, modelers frequently require graph editing operations that are more complicated than adding and deleting a single node or edge at a time.

A decision tree, in particular, imposes several structural constraints on the allowed graph. The graph must be a tree, that is, the underlying undirected graph must be acyclic. Furthermore, leaf nodes cannot have any children. We now illustrate how graphgrammars, by careful specification of attributes, bindings, and graph-grammar productions, can capture the syntax and semantics of decision trees. We will not present a complete specification of all the productions needed to represent the structural constraints for decision trees (or for our other examples) but we will present a variety of particularly interesting or challenging graph grammar productions.

## 4.4. Graphgrammars

Graph grammars, ([43,44], [21,22,23]), arose out of the study of formal (text-based) languages [26]. In particular, a graph-grammar consists of a set of editing operations or productions that can be applied to a graph. By limiting the set of editing operations that can be applied to a graph, we enforce structural constraints on the types of graphs that can be created. The basic principle is that if the current graph is valid before the production is applied, it will remain valid after the production is applied.

We consider a very simple production for decision trees, where the modeler wishes to expand a simple outcome into a more complicated decision scenario. In graph terms, the user wishes to replace a leaf node by a decision node. Since decision nodes cannot be leaves of a decision tree, however, a new leaf node must be attached to the decision node (e.g., fig. 2).

In general, a production $\mathcal{P} = \langle G^{\mathrm{L}}, G^{\mathrm{R}}, T \rangle$ consists of three parts, two graphs, $G^{\mathrm{L}}$ and $G^{\mathrm{R}}$ called the left-hand side and right-hand side, respectively, and the embedding transformation $T$ , about which much more will be said later. Production $\mathcal{P} = \langle G^{\mathrm{L}}, G^{\mathrm{R}}, T \rangle$ is applied to graph $G$ in order to change the structure of $G$ . Briefly, when $\mathcal{P} = \langle G^{\mathrm{L}}, G^{\mathrm{R}}, T \rangle$ is applied to $G$ , $G^{\mathrm{L}} \subseteq G$ is to be replaced by graph $G^{R}$ and $G^{R}$ is connected to graph G with $G^{L}$ removed, denoted $G \setminus G^{L}$ , by ‘appropriate’ nodes and edges. These nodes and edges are determined by the embedding transformation, T, discussed in section 4.5. In the example, $G^{L}$ consists of a single leaf node, c, and $G^{R}$ consists of a decision node, f, connected to a leaf node, g, by a choice edge (fig. 3).

![](/api/attachments/XQFXX494/fulltext/images/bcedfd7b30a581b0ffa729f60fb09968ae38e9fe9c8c5c072b7a3ec2444712d2.jpg)  
Fig. 2. Changing a leaf node (c) to a decision node (f) connected to a leaf node (g).

Graph $G^{L}$ would generally be selected by the user using a pointing device such as a mouse. A production (i.e., not the user) can also cause nodes and edges in $G^{R}$ (as well as nodes and edges associated with the embedding transformation) to remain selected after the production is applied. If no subgraph isomorphic to $G^{L}$ is found in G, then the production is not applied to G.

## 4.5. Embedding transformation

The tricky part of a production involves the embedding transformation, $T$ , which determines how $G^{\mathbb{R}}$ is to be connected $G \setminus G^{\mathbb{L}}$ . Although $T$ can be specified in many different ways, we use Jones's [30] adaptation of Nagl's [43] specification

![](/api/attachments/XQFXX494/fulltext/images/ea850de88c42550c2b07322768f197af814a97a63363b7d6cd2a39401810fb5f.jpg)

Fig. 3. Graphs $G^{L}$ and $G^{R}$ to replace a leaf node by a decision node plus a leaf node.

of T. Furthermore, as shown by Göttler [21], T can be represented by a graph.

In general, $T$ determines nodes in $G \setminus G^{\mathrm{L}}$ to be connected to nodes in $G^{\mathrm{R}}$ by edges of specified type. A given $T$ determines those nodes in $G \setminus G^{\mathrm{L}}$ by following paths (or more complicated graph 'pieces') from $G^{\mathrm{L}}$ into $G \setminus G^{\mathrm{L}}$ . The nodes and edges on these paths are called embedding nodes and edges. For the current example, $T$ traces a path consisting of a single choice edge from the selected leaf node, $c$ , to its parent decision node, $d$ . The embedding transformation, $T$ , would be specified by the designer as in fig. 4.

In general, however, we cannot guarantee that the parent of the selected leaf node will be a decision node; it might be a probabilistic node. Therefore, the designer would have had to specify the embedding transformation of fig. 4 to allow for this case. In particular, the revised embedding transformation (fig. 5) also traces out a path from the leaf node to any parent probabilistic node.

This mechanism for specifying productions has two important properties:

(1) It is visual. Not only is it visual, it relies on an attributed graph, and hence is supportable by graph-grammar productions. Networks allows the designer to edit productions in exactly the same way as any other graph.

![](/api/attachments/XQFXX494/fulltext/images/81041f689f946d30a3221b880db04976ae9ff75d704c1243b742618d263fcaf4.jpg)  
Fig. 4. Part of production to replace a leaf node by a decision node plus a leaf node. Here, $G^L$ consists of a single leaf node (c); the embedding consists of a single decision node (d) and a single choice edge (connecting d to c). $G^R$ consists of nodes f and g connected by a choice edge. $G^R$ is connect to $G \setminus G^L$ by a connecting edge of type choice (connecting node d to node f). Note the use of a ‘+’ that divides the figure into four quadrants. The ‘+’ diagram is sometimes used to identify nodes and edges as being part of the left-hand side, right-hand side, embedding or connecting, as indicated.

![](/api/attachments/XQFXX494/fulltext/images/138756b86275aed8f3890240db3c2c3192e2315b2a2b847356a01e0f9600e769.jpg)  
Fig. 5. Complete production to transform a leaf node into a decision node and a leaf node.

(2) It is theoretically as powerful as one could hope. In particular, Nagl [43] showed that this mechanism of specifying productions is as powerful as a Turing machine, indicating that any graph manipulation that can be expressed by a computer program can be expressed as a set of graph-grammar productions.

## 4.6. Path edges

Although theoretically powerful, Nagl and Göttler's original mechanism for specifying productions is sometimes not tremendously convenient. Several extensions have been developed (summarized in [28,30]) that help make productions more precise.

One (new) extension not described in [30] and [31] involves the use of path edges in a production graph. For decision trees, this extension makes the graph-grammar production to delete a subtree far more concise. In [29], we presented a mechanism for deleting a subtree that did not make use of path edges; it required two productions executed in sequence. The two productions required a total of 6 nodes and 4 edges as well as a program graph, to sequence the application of the productions appropriately. Using path edges the same operation can be expressed by a single production consisting of 4 nodes and 3 edges (fig. 6). In the production graph, it is assumed that the user has selected some node whose subtree is to be deleted. That selected node will be replaced by a leaf node, in order to maintain the integrity of the decision tree. In the production graph, node $a$ represents the node that has been se lected by the user. Node b represents all the children of a, as captured by the path edge connecting node a to b. Node c represents the parent of node a, and node d represents the leaf node that is to replace node a.

![](/api/attachments/XQFXX494/fulltext/images/31d80e1e308199d5de428ec62ea16215cd9377c3a0bbeaf5b2d355fa66758058.jpg)  
Fig. 6. Production graph to delete a subtree of a decision tree. Node a has been selected by the user. Node b represents all the descendants of a, as represented by the path edge connecting node a to b. The label on the path edge Probabilistic and Outcome refers to the finite state automaton of fig. 7, indicating the possible sequence of edge types allowable on the path. Node c represents the parent of node a, and node d represents the leaf node that is to replace node a.

In this case, the path can consist of a sequence of probabilistic or outcome edges in any order. Originally, we associated a regular expression [26] of edge types with the path edge, i.e., (probabilistic + outcome) +, indicating the sequence of edge types allowable on the path. However, any regular expression is equivalent to a finite state automaton [26], which can easily be represented as a graph. Therefore, we now restrict the sequence of edge types (and directions) using an associated finite state automaton graph (fig. 7). In the finite state automaton, each node represents a possible state. The initial state is marked start, the final state is marked stop. As a path is being formed, control passes from state to state when an edge in the target graph of appropriate type has been found. The appropriate type is specified by the label on any outgoing edge from the current state node. Edges labelled with \$ allow an immediate transition to another state, without any additional edges found in the target graph. For this example, once any edge of type probabilistic or outcome has been found, i.e., state a has been reached, then a valid path has been found for the production to delete a subtree.

![](/api/attachments/XQFXX494/fulltext/images/e5eb2c458d1f2bf04db82a565e347db8be055b68057b57f2313ab9f7224b581d.jpg)  
Fig. 7. Finite state automaton, Probabilistic and Outcome, to limit the allowable sequence of edge types along a path. In this case, the sequence must contain at one or more outcome or probabilistic edges.

## 5. Linear programming

We now assume that the value of a particular leaf node in the decision tree is to be calculated from some other model, for example, a linear programming model. We do not claim that this graph-based representation is better than the traditional LP tableau, merely that it presents a graph-based representation of any linear programming problem. This representation is based on the activity/resource flow diagram described in [56]. Research by Ma et al. [41] has defined a higher level graph to represent linear programming problems where each node represents a collection of constraints and decision variables. Research by [13] has defined a different graph-based representation for linear programming models similar to Schrage's representation. We are exploring the applicability of graph-grammars for these graph-based models. Viewing linear programming problems as graphs has proved useful in providing diagnostic support to linear programming models, as shown in [24].

We assume only equality constraints, with the standard trick of adding slack and surplus variables as needed to transform inequalities to equalities. Each variable is represented by a node of type variable; each row is represented by a node of type constraint. The activity of a particular variable in a particular constraint is represented by a coefficient edge connecting a variable node to a constraint node, forming a bipartite graph. Furthermore, a primalobjective node represents the value of the primal solution; the dualobjective node represents the value of the dual solution. Edges of type cost connect a primalobjective node to each variable node; edges of type bound connect each constraint node to each dualobjective node. For example, the linear programming problem:

![](/api/attachments/XQFXX494/fulltext/images/701749051c8b2ff0e43d5ba016fbd77f073a47901f462f69dda8e7f1982057ce.jpg)

could be represented by the graph in fig. 8.
Notes:

\- the value attribute gives the current value of each variable in the linear programming problem;

\- we use bindings when displaying coefficient edges to highlight the current basis. In the implementation, if the value of a coefficient edge is zero, the edge is displayed in white (i.e., invisible); if the value of a coefficient edge is one, the edge is colored red; otherwise the edge is colored black.

\- similarly, for cost edges, if the current cost attribute of the edge is zero, the edge is colored white. If it is positive, it is colored green; otherwise it is colored red. In a feasible optimal solution to a maximization problem, no cost edge will be green. We could also define a binding function to adjust the width of the edge based on the current value of the cost attribute.

![](/api/attachments/XQFXX494/fulltext/images/7403d5ebeab2470ed6c67b1628dd7be764cf762c149832e4e4c4ec3d205f8d6c.jpg)  
Fig. 8. A graph representing a linear programming tableau. Thicker coefficient edges represent coefficients with value equal to 1.

![](/api/attachments/XQFXX494/fulltext/images/ad7060696873cd0c346d503e9488aaf8beb366c3543438b1bb11fe435b81d37c.jpg)  
Fig. 9. Production to add a variable node. Node b represents the variable node to be added. Node a represents the primalobjective node in the graph. Node c represents all constraint nodes in the graph. In short, this production will add in a variable node (represented by b), connect it to the primalobjective node (represented by a) with a cost edge, and also connect it to all constraint nodes (represented by c) by coefficient edges.

\- edges of type bound are defined similarly to cost edges, i.e., they connect constraint nodes to the dualobjective node.

This graph-based representation could be used as the basis of a more elaborate system to provide an interesting animation of the operation of the simplex method. At any iteration, variable nodes with a single outgoing coefficient edge colored red would indicate the current basic variables. When all cost edges turn red, the solution would be optimal. Such a capability would require a tight linkage between an external linear programming solver (and resolver) that is not currently provided.

The variable and constraint nodes along with the coefficient edges form a bipartite graph. The production illustrated here, therefore, will be applicable to other graph-based models that rely on an attributed bipartite graph, e.g., the assignment problem and the transportation problem. We present the production to add a new variable node (fig. 9). The right-hand side contains a single variable node, b; the embedding finds each constraint node (represented by node c) and adds a coefficient edge to connect b to each c. Similarly, a cost edge is added to connect the new node, b, to the primalobjective node a.

![](/api/attachments/XQFXX494/fulltext/images/a0b6b8cdaaa0b5b20b46ec17ecab7ffc08f4d9f2fa227145ad68f58fc2200cf6.jpg)  
Fig. 11. Production to add a coefficient edges between selected variable and constraint nodes.

![](/api/attachments/XQFXX494/fulltext/images/9102993d7544161132d21ac975e8ff39b0cd2a416bacaf136e72eab47f7c0219.jpg)  
Fig. 10. Production to add a constraint node. Node b represents the variable node to be added. Node a represents the primalobjective node in the graph. Node c represents all constraint nodes in the graph. In short, this production will add in a variable node (represented by b), connect it to the primalobjective node (represented by a) with a cost edge, and also connect it to all constraint nodes (represented by c) by coefficient edges.

By making simple changes to the the production graph of fig. 9, e.g., changing the labels of and adding or deleting a few nodes and edges, one can obtain a variety of useful productions. For example, to add a constraint node (fig. 10), we relabel variable node b from fig. 9 to be an embedding node, and constraint node c to be in the right-hand side. Similarly, another useful production adds coefficient edges to connect selected variable nodes to selected constraint nodes (fig. 11). That production differs from the productions of figs. 9 and 10 since both variable node b and constraint node c are embedding nodes and have been labelled selectbefore, meaning that only those variable and constraint nodes that have been selected by the user (by pointing to them with a mouse) will participate in the production.

In short, general linear programming can be captured within the graph-based paradigm and graphgrammars enforce the required structure. Furthermore, for specific linear programming models, e.g., network flow models, one could consider developing specialized productions to work with such models.

## 6. Critical path

The actual decision making project will require several steps, including collecting data, building the models and preparing the final report, which we assume will require some presentation style graphics. In order to perform such co-ordination, we shall discuss a slight variation to a standard project management tool, the critical path problem, to help co-ordinate the different aspects of the project. In this project management tool, nodes will represent particular steps in the process. Associated with each node is a value giving the estimated amount of time required to complete the process. An optional attribute will indicate the graph-based model to be developed and analyzed for this particular step of the decision making process. This particular example illustrates the capability provided by Networks to support a simple hierarchy of graphs: nodes and edges can have attributes that are graphs, which can be opened and displayed just like any other attribute (see section 8).

To remind readers of the critical path problem, we adopt the notation used in $[15]$ (summarized in table 1). We associate each task with a node of type task, although an equivalently powerful model could be developed if one associates each task with an edge.

With respect to Networks, the critical path problem is of interest for at least three reasons:

(1) the solution to the critical path problem, e.g., $e(t)$ , $l(t)$ , can be computed solely by attribute expressions. In fact, bindings can be used to display automatically the critical path by coloring red the edges and nodes on the critical paths;

Table 1  
Notation for critical path problems

<table><tr><td>Notation</td><td>Meaning</td></tr><tr><td>p(t)</td><td>Processing time for task t</td></tr><tr><td>e(t)</td><td>Early start for task t</td></tr><tr><td>l(t)</td><td>Late start for task t</td></tr><tr><td>B(t)</td><td>Tasks that must complete before task t can begin</td></tr></table>

(2) critical path problems require that their graphs be acyclic. Since other graphs must also be acyclic, e.g., structured modeling graphs [19], the productions to enforce acyclicity have wider applicability;

(3) since nodes can reference other graph-based models, the critical path graph can be used by a modeler to manage a modeling project within Networks.

We first illustrate attribute expressions that determine the solution to the critical path problem, and then consider the key production to enforce acyclicity in such graphs.

## 6.1. Computing the critical path

The formula to compute $e(t)$ can be expressed as

$$
e (t) = \max _ {y \in B (t)} \left(e (y) + p (y)\right).\tag{1}
$$

The corresponding attribute expression is:

max(0,

$$
\begin{array}{c} \text {imax(edge(*,Edge,precedence,From,*),} \\ (n a (\text {earlystart}, *, F r o m, t a s k) + \\ n a (\text {processingtime}, *, F r o m, t a s k)))) \end{array}
$$

which can be interpreted as:

(1) compute the maximum of 0 and the maximum of the early start plus the processing time of all predecessors, i.e., $max(0, imax(\ldots))$ .

(2) The predecessors for step 1 are determined by indexing over all edges, (determined by edge(\*,Edge,precedence,From,\*)), yielding nodes instantiated by From.

(3) Given the predecessors, determine the maximum of the expression

$$
\begin{array}{l} n a (e a r l y s t a r t, *, F r o m, t a s k) + \\ n a (p r o c e s s i n g t i m e, *, F r o m, t a s k), \end{array}\tag{2}
$$

which corresponds to $e(y) + p(y)$ in eq. (1). Recall that na obtains the value of the specified attribute of the specified node.

So, in a manner similar to the way a formula can be specified for a spreadsheet cell, we can specify a formula for the value of the attribute for a node or edge. In this case, the attribute formulas will compute the values of the earlystart, earlyfinish, latestart and latefinish of all the tasks. This essentially solves the critical path problem.

![](/api/attachments/XQFXX494/fulltext/images/a081de9729f2f9333b9f2de41264054ccb6898d7553d15695e9933730b102508.jpg)  
Fig. 12. Production to add a precedence edge. Notice that the path edge labelled not indicating that the production should not be applied if a path exists between those two nodes.

## 6.2. Some productions for the critical path problem

Editing a critical path problem requires a set of productions, i.e., productions to add and delete task nodes and precedence edges. We discuss here the most challenging production needed, the production to add a precedence edge. This production is particularly challenging because in order for the values of $e(t)$ and $l(t)$ to be computable, the critical path graph cannot contain a cycle. The algorithm for evaluating attributes detects when such cycles occur, so one could rely on it to enforce the acyclicity constraint. It is also possible to do so using path edges provided by (our extensions to) graph-grammars, however.

Adding a precedence edge connecting some task node $n_{1}$ to task node $n_{2}$ will create a cycle if a path already exists from $n_{2}$ to $n_{1}$ . In terms of the production graph (fig. 12), one can represent this condition by a path edge connecting node $n_{2}$ to node $n_{1}$ . The path should consist of one or more edges of type precedence. The Precedence Only label refers to the quite simple finite state automaton graph of fig. 13, which limits the path to consist only of precedence edges. We also label that edge not to indicate that the production will not be applied (i.e., the precedence edge will not be added) if such a path exists. In general, a not edge in $G^{L}$ will not allow the production to be applied if the corresponding type of edge exists in the current graph.

![](/api/attachments/XQFXX494/fulltext/images/b09df17addd9b4859c8101ac9c5cb276edd0e7b287f8ac22e0e167006f7973b4.jpg)  
Fig. 13. Finite state automaton, Precedence Only, associated with production of figure 12 to restrict a path to consist of one or more precedence edges.

![](/api/attachments/XQFXX494/fulltext/images/2e8850dd4faefc04a380bd4397efd5bb726142237015d4851b408588a0832781.jpg)  
Fig. 14. A graph drawn as a bar chart using bindings.

This production is significantly more concise than the original mechanism for specifying this production, as described in [29], which required a production with more nodes and many more edges.

## 7. Presentation graphics

It may appear that graphs, although pictorial, are not well suited to providing presentation graphics capabilities similar to those found in spreadsheets, and other decision support systems. However, not only can graphs support presentation graphics, graph-grammars allow one to specify formally how they can be constructed. The bar chart of fig. 14 is actually a graph whose “bars” are nodes whose height has been scaled through the use of bindings to be proportional to the associated value attribute of the node. Furthermore, the graph contains several hidden edges (of type next) that arrange the bars in order. Fig. 15 displays those hidden edges. Finally, a special hidden node of type tail indicates the end of the “linked list” of bars (also shown in fig. 15). Through the use of attribute expressions, the horizontal position of each bar can be determined based on the position of its predecessor bar (as determined by an incoming next edge).

A simple graph-grammar production provides the capability to add a single bar (in the right-most position). That production, in fig. 16, consists of a single tail node (c), and two bar nodes, a and b. Bar node a is an embedding node representing the right-most bar. Bar node b is part of the right-hand side, and will be added to the graph by the production. The next edge connecting node a to node c will be deleted (as indicated by its label). The next edges connecting nodes a to b and b to c will be added to the graph by the production since they are connecting edges. At least one other production would be necessary to provide a complete set of useful productions, i.e., a production to delete a bar (though other productions may also be useful, e.g., a production to insert a bar in an arbitrary location).

![](/api/attachments/XQFXX494/fulltext/images/7873cc861fe9829d024cf1352102e59a7966465c0bf2ca9c1b7c1cba64b5ac2d.jpg)  
Fig. 15. A graph drawn as a bar chart using bindings, with the hidden nodes and edges displayed.

## 8. Integrating the example models

We have now presented four different graph-based models as individuals. We now discuss how they can be integrated. Integration is essentially provided using two different (though closely related) techniques:

(1) Attribute values can depend on the values of other attributes in other models. Changes made to attribute values are automatically propagated (section 8.1).

(2) Attributes in one model can refer to other models, not just other attributes. One capability thus supported is that we can construct an iconic interface such as provided in certain types of graphical operating environments, e.g., on the Apple Macintosh (section 8.2). Moreover, that iconic interface, itself a model, can provide useful support for organizing and managing a collection of models.

![](/api/attachments/XQFXX494/fulltext/images/90a2e0d5c9e24406610f9c5f2c4adf9c7baa8266e6ea077783fa7d12b09f3282.jpg)  
Fig. 16. A production to add a bar to a bar chart graph.

Certainly other capabilities are also useful in support of model integration, see, e.g., [4,5,6,7,20,34]. In section 9, we shall discuss the capabilities cited by these authors in more detail. We now discuss in more detail both of these two specific capabilities provided by Networks.

## 8.1. Linking attributes

Networks allows formulas underlying attributes and bindings to reference the values of attributes and bindings of nodes and edges in other models. Recall that the first argument of the node( $\cdot$ ) and edge( $\cdot$ ) predicates and the second argument of the na( $\cdot$ ) and ea( $\cdot$ ) predicates is a unique identifier for the graph associated with the node or edge. Through this simple mechanism, one can link attributes from one graph instance to attributes in another graph instance. Furthermore, attribute values are automatically updated (using a variation of topological sort) when the modeler makes a change to an attribute in a graph or applies a production to a graph.

For example, for a decision tree model, the value of the value attribute of a leaf node can be determined by the objective function value of a linear programming problem. The formula to do that, which underlies the leaf node in the upper right-hand corner of fig. 2, is

imax(node(g3,Node,primalobjective),

na(value, g3, Node, primalobjective))

where:

\- the linear programming graph has unique identifier g3;

\- we use the indexed maximum function, imax, to search for the single primalobjective node (identified as Node) in the linear programming graph. The expression node(g3,Node,primalobjective) finds that primalobjective node;

\- the value attribute of the primalobjective Node is specified as $na(value, g3, Node, primalobjective)$ .

When the linear programming model is changed and re-optimized, the decision tree is automatically updated, which recomputes the optimal decision strategy.

Similarly, the capability to link attributes from other models also facilitates the integration of presentation graphics. For example, the values determining the height of the bars in the bar chart example are determined by formulas that reference attributes in the decision tree model.

Note that a capability that would be useful in supporting this style of model integration is the type of “dimensional analysis” and “quiddity” checking developed in the research of Bradley and Clemence [10] and Bhargava et al. [7]. In that research, additional information is associated with attributes, to make certain that dimensional units and other information (the quiddity or “essential essence” of the attributes) are maintained consistently as attributes are combined in computing values from expressions. Bhargava and Kimbrough show how such information, for example, could in addition be used to generate automatically the link between the decision tree and the linear programming model. In particular, if two attributes have the same quiddity, then at least potentially, those attributes are the same. Networks does not currently provide such dimension or quiddity checking of the sort proposed in [10] or [5]. Such a capability is obviously a desirable extension to Networks.

## 8.2. Model references

The critical path model was originally introduced to manage large projects, and remains widely used for that purpose. Why not use the technique to manage modeling projects? Within Networks, it is relatively easy to use such a critical path model to manage other models. The key is to allow attributes to refer specifically to other models. Although the ability to link variables described in the previous section provides a version of this capability, it dealt only with attributes in other models, not the models themselves. In particular, we have added a model attribute to each task node. As always, the modeler can point to any task node (or any other node or edge) to see and perhaps edit the values of the attributes for that node. When the user does so, the value of the model attribute will be displayed, indicating the name of the graph corresponding to the current task node. The user can choose to open that graph for display and editing simply by pressing a button on the attribute list. In fig. 1, the names of the associated models are indicated on top of the critical path graph. Therefore, all models discussed are represented as task nodes in the critical path graph. This provides an iconic style interface for a model collection, similar to the graphical operating systems found on such systems as the Apple Macintosh. In short, we are able to co-ordinate the development of a variety of models through the use of standard project management techniques, e.g., critical path. This capability was possible because we allow attributes in models to refer to other models directly.

## 9. Integrated modeling environments, model integration and Networks

In the previous sections, we presented several examples of how Networks can be used to build models, and further, how those models can be combined in a useful fashion. In this section, we compare the integrated modeling capabilities provided by Networks to related research. We base our presentation on the framework for considering integrated modeling environments proposed by Geoffrion [20] (section 9.1). We then provide a detailed discussion of how well Networks fits into that framework (sections 9.2–9.4). Of course, throughout the presentation, we also discuss related research on integrated modeling environments.

## 9.1. Geoffrion's framework

Geoffrion [20] partitioned the capabilities needed in an integrated modeling environment into three main levels, “support for models, support for solvers, and utilities (tools) of various sorts”, where models are simply formal descriptions of problems of interest, solvers analyze models to produce useful information, and utilities such as text-editors, and presentation graphics provide a variety of additional support believed useful in an integrated modeling environment. Geoffrion further partitioned support for models into four sublevels, each subsequent level allowing the integration of more and more diverse model types. The four sublevels, in increasing order of the variety of models to be integrated, are (quotations are from [20]):

Specific models “A ‘specific model’ is a completely definite instance of a model, including all data values (e.g., a particular Hitchcock–Koopmans transportation model).”

Model classes “A ‘model class’ is a collection of conceivable, similar specific models; it is definite neither as to data values nor as to the identity or even number of items of various types, but otherwise is quite specific as to mathematical form (e.g., the class of all Hitchcock–Koopmans transportation models).”

Modeling paradigms “A ‘modeling paradigm’ is a collection of similar model classes that has established its conceptual value and influence (e.g., the class of all network flow models).”

Modeling traditions “A discipline-specific ‘modeling tradition’ is a collection of modeling paradigms that tend to be associated with one another in the academic and practitioner communities owing to similarities of the technical apparatus they commonly involve. Of particular interest are the distinct modeling traditions of MS/OR, database management, computer programming languages, and artificial intelligence.”

We now discuss model integration at each of Geoffrion's three levels, i.e., the model (and its sublevels), solver, and utility level. Furthermore, throughout the discussion, we compare Networks to the related research on integrated modeling environments.

## 9.2. Model integration

In discussing model integration, we rise up the hierarchy of model levels proposed by Geoffrion, from specific model integration through modeling tradition integration. We conclude with a discussion of research on performing such integration automatically or at least supporting the user in performing such integration.

## 9.2.1. Specific model integration

Integration of specific models is commonly provided by systems that support a specific modeling technique, e.g., linear programming, or decision trees. Frequently, it is used to generate aggregate information concerning the performance of a collection of similar models. With respect to Networks, we assert that the models presented in sections 4–7 illustrate well the ability of Networks to provide linkages across different model instances.

## 9.2.2. Model class integration

One can distinguish at least two different forms of model class integration, which we shall call decomposable, and non-decomposable. In decomposable model class integration the component model classes remain clearly identifiable, to the point that each could be analyzed by an appropriate solver, with the results combined to produce the same result as if the integrated model class were analyzed by a single solver. Decomposable model class integration occurs, for example, when the output of a linear programming model is used as input to a decision tree model. Bhargava [4] calls this model composition. Kottemann and Dolk [34] call this pipelining. In non-decomposable model class integration, the integrated model class must be analyzed by a single solver. This style of model integration would occur, for example, when a Hitchcock–Koopmans transportation model is combined with a linear programming production planning model. In order to prevent suboptimization (and infeasibility), one cannot solve the transportation model independently from the production planning model.

With respect to Networks, although it supports decomposable model class integration quite well (since attributes among models can be linked), non-decomposable model class integration is less well supported. A (naive) approach to non-decomposable model class integration might simply concatenate the node and edge types and the graph-grammar productions for the component model classes. With additional productions, or editing existing productions, it should be possible to integrate more than one model into a new model class. This topic will be discussed in more detail in section 9.2.5, where we discuss research that has attempted to provide such integration automatically or semi-automatically.

Ideas such as inheritance from object-oriented programming might also be introduced to Networks to provide such model class integration. For example, in a linear programming application it might be useful to partition the variable nodes into different classes, representing different types of variables, e.g., one class representing production, another inventory. This type of relationship is easily modeled using the idea of inheritance from object-oriented programming. One could define the notion of a general variable node, and then define “descendant” node types, inventory and production that would, in some fashion, inherit the properties (e.g., the attributes) of variable nodes, and yet remain distinct. Such an inheritance hierarchy, of course, could also be represented conveniently as a type of graph, which Networks is eminently capable of doing. The use of object-oriented techniques within the style of modeling environment provided by Networks is a promising area for further research.

## 9.2.3. Modeling paradigm integration

Model paradigm integration occurs either when two model classes from two different paradigms are integrated, e.g., when a simulation model is linked to a mathematical programming model or when the two paradigms themselves are integrated, e.g., integrating mathematical programming and stochastic analysis techniques to generate a new paradigm such as stochastic linear programming.

Much less work has been accomplished in this direction, though work by Dolk [16] has explored the use of Geoffrion's structured modeling, which has been shown to support a wide set of different model classes from different paradigms, to support simulation models. The work of Bhargava and Kimbrough [6] supports stochastic models, as well as traditional mathematical programming models. With respect to Networks, the models illustrated in the example come from widely different paradigms, from project management to presentation graphics to linear programming, though currently the applicability of Networks to stochastic models has not been addressed.

## 9.2.4. Modeling tradition integration

A common example of this style of integration is the integration of mathematical programming technology with database technology or with artificial intelligence. This is also becoming increasingly common with the development of consistent, window-based user interfaces, where the ability to cut and paste information across widely varying applications is becoming increasingly common.

A closely related approach advocates that traditional analytical modeling tools should be based on well-established paradigms such as spreadsheet modeling or relational database technology $[54,11]$ , since so many people are familiar with these tools. Clearly, ideas from artificial intelligence have much to offer to model management. Notable examples include $[38,39,49]$ .

With respect to Networks, just in defining and implementing Networks, we have made some progress in integrating different modeling traditions. In particular, the work comes from the tradition of formal language theory. Furthermore, since Networks is written in Prolog, we claim a degree of integration with the AI tradition. With Networks' ability to perform database style queries on a network (see [30] for the details), we also claim a degree of integration with the database tradition. We have also begun to explore the integration of Networks with other integrated modeling frameworks, including structured modeling [32] and PM\* [33], that claim to provide a large degree of integration at each of the levels in Geoffrion's framework for model integration.

## 9.2.5. Automatic model integration

A great deal of the research on model integration has attempted to perform the various types of model integration automatically or, at least, semi-automatically. Given a collection of models, and information about them, for a given question posed by some problem holder, the goal of this research is to develop techniques to determine or construct the appropriate models to be run so as to provide an appropriate answer. Much of the research has focused on integrating decomposable models. Bradley and Clemence [9] allow models to be integrated using rewriting rules to combine variables from disparate models, along with a type-calculus to check that combined values have the same dimensional units and meaning [10]. Bhargava and Kimbrough [6], proposed the “embedded languages technique”, which, through the use of concepts adopted from formal logic provide a rich set of capabilities to use outputs from different models as inputs to other models automatically, as long as certain conditions hold. They have applied their approach to the problem of providing consistency checking of variables, using the “quiddity” or essential meaning of model variables, similar to the work of

Bradley and Clemence [10], when combining different models [5]. Liang [40] used a graph-based representation of models, with nodes representing data, and arcs representing possible models; details of how to assess the quality of such automatically derived inferences was unclear. Blanning [8] used approaches from database theory to provide similar capabilities, with similar problems with respect to ensuring model validity.

For non-decomposable model class integration, several researchers have addressed the question of integrating models automatically. Like the research on integrating independent model instances, their research has focused on automatically or semi-automatically combining two or more generic models. Ma et al. [41] have focused on combining fragments of linear programming models specified in a high-level textual language or as a set of graphs. Krishnan's work [35,36,37], on building models from qualitative specifications involves the construction of larger models from smaller model templates. Liang's work on analogical reasoning [40] attempts to construct models from similar model templates, thereby combining models semiautomatically.

Although much of the research on model integration has concerned itself with combining models automatically to do useful work, in this paper we are not proposing in Networks techniques for automatic combination of models. We do believe, however, that the graph-grammar paradigm has something to contribute on that score. Based on Krishnan's work on qualitative model specification, in [33], we show that the manipulation capability provided by graph grammars can be used to provide useful model combination operations.

## 9.3. Solver support

Several researchers have begun to explore how best to integrate solvers into modeling environments [6], [17], [34]. Certainly, any integrated modeling system that claims the name must provide some mechanism to allow models to be analyzed. Exactly how that should occur is the question. One generally accepted tenet for providing solver support has been that good modeling practice should separate the models, i.e., problem specifications, from the solvers, i.e., the means to analyze them. There are several cogent arguments in support of this recommendation, see, e.g., [19]. Yet, when this separation is provided, there still must be a mechanism for allowing solvers to analyze the model as specified. Furthermore, perhaps the appropriate analysis method for a particular problem should be composed out of a collection of solvers, in perhaps intricate ways, e.g., using decomposition methods for mathematical programming. Several researchers have begun to explore how to integrate solvers into integrated modeling environments. Eck et al. [17], have developed a language to integrate external solvers with structured modeling. Geoffrion provides linkages to several solvers in his prototype implementation of structured modeling [19]. The work of Kimbrough [5], provides links to external solvers including GAMS and an external database. Kottemann and Dolk [34], inspired by simulation languages and research on communicating sequential processes, have proposed that solver integration must take into account execution of solvers that might occur in a complicated sequence requiring careful synchronization. They identify three important components to solver integration, including variable correspondence, i.e., linkages among model variables, sequentiality, i.e., the order in which solvers (and other model manipulators) must be executed, and synchronization, e.g., the ability to interleave of the execution of several solvers given that solvers can run in parallel. As Kottemann and Dolk note, essentially all work to date (including Networks) has only allowed for straightforward sequential execution of solvers.

Networks provides some solvers (currently, three) to perform analyses on models. First, Networks provides an evaluation capability in the tradition of spreadsheets, which, in the examples, was used to solve critical path problems. Networks does not currently allow for the solution of a simultaneous set of equations. A second solver in Networks, as described in [30], provides the capability to perform database query capabilities, though specifically oriented towards graphs. Finally, we have linked an external minimum cost network flow algorithm (written in Pascal) to provide network flow solution capability. Other solvers, e.g., linear programming, symbolic mathematical manipulation, would certainly be useful additions to Networks. With respect to Kottemann and Dolk's framework, Networks provides variable correspondence capability and assumes only simple sequential execution of models but does not support the intricate synchronization that they advocate. One might note, however, that many simulation languages, e.g., SLAM [51], SIMAN [47], as well as many computer science tools for analyzing communicating sequential processes, e.g., petri nets, admit a natural graph-based representation. This provides hope that tools to support communicating sequential processing in support of model management could be added to Networks.

Finally, graph-grammar productions can provide support for building solvers. For example, in a vehicle routing example (described in more detail in [30]), many solvers for finding good (or even optimal) solutions involve moving a customer from one route to another. That manipulation can easily be described by a graph-grammar production. Rather than coding such a manipulation in a programming language, one could easily allow a solver designer to specify such a manipulation directly as a graph-grammar production.

## 9.4. Utilities

Although Networks does not provide built-in capabilities for presentation graphics, such as provided by spreadsheets, we have shown how Networks might be used to produce at least simple versions of such graphics. Furthermore, the ubiquitous use of graphs and Networks as a problem representation provides hope that it will be possible to provide a consistent interface to the variety of utilities that are needed to support modeling. For example, the icons representing files and programs on an iconic operating system such as found on an Apple Macintosh could be considered as nodes in a particular graph. The contents of the files would simply be attributes of the nodes. The ability to 'open' a model underlying a task in a project management graph as described in section 6, indicates that such a capability is feasible.

Another utility cited by Geoffrion was text editing. Although Networks does not currently provide support for text editors, such support could be provided simply as a special type of attribute of a node or edge. Alternatively, one could use graphs as an internal representation for text. For example, Nagl et al. [45] applied graph-grammars to provide syntax-directed editing capabilities for text-based languages. What is required is an “unparser” to translate a graph-based representation of text into an appropriate text-based representation.

Still another potentially useful utility is hypertext [14], wherein information is densely linked along with a corresponding user interface to navigate through the information. For example, the system of Bhargava, et al. [5], provides automatic text-based explanation capabilities for model components using a hypertext style interface. One can view (basic) hypertext user interfaces as one form of 'browser' for a particular type of attributed graph, which might indicate that Networks could provide support for hypertext style interfaces; Networks, however, currently does not provide the type of automatic, dynamic, construction of hypertext links as described in [5].

## 10. Conclusions

The key (or, at least, one key) to providing an integrated modeling environment seems to be the ability to use a single, powerful, representation format – in our case, graphs – for expressing models independent of a particular solution technique. Once one's models are expressed in the particular format, all supporting machinery provided for such representations comes for free. In our research, this includes graphical syntax-directed editing for different models, as well as the capability to combine models in a variety of ways.

More powerfully, if the same representation format can be used to express operations to be performed on the models themselves, e.g., editing, combination, decomposition, then great economies are possible (and demonstratable in the case of Networks) in providing richer functionality for modeling. Economies occur because the machinery used to manipulate models can also be used to manipulate operations on those models. If one does not follow this approach, then entirely new machinery must be designed (and implemented) to support representing (and manipulating) operations on models. Furthermore, designers must receive at least two levels of training, one in the models themselves, the other in the operations on those models. Using a single representation format for both should make the designer's job easier. In the case of Networks, since graph-grammar productions can be represented as a graph, they can be supported by Networks just like any other graph, i.e., with visual syntax-directed editing provided for free, and the ability to link productions to other graphs. The potential savings of this approach, of course, depends on the ability of the paradigm to represent operations on models. However, if the paradigm claims to provide support for a variety of models, why not for operations on the models themselves?

The usefulness of representing both one's models and models of models using a single representation format has been developed more precisely as the embedded languages technique by [4,6] using techniques from formal logic. Other researchers rely on other paradigms, e.g., [19]. By relying on the ability to represent one's models in a unified, theoretically powerful framework, one can then begin to build supporting machinery to provide useful functionality for working with a variety of models.

Using classic management science models, we have introduced attributed graphs and graph-grammars as a basis for a modeling environment that we call a graph-based modeling system, with a research prototype, Networks, illustrating the idea. Since graphs are a widely used representation format, but many types of graphs are used to model different situations, a modeling environment that promotes the use of different types of graphs appears attractive. Such an environment, however, must provide the capability to support semantic (structural) constraints on the appropriate structure of a graph, e.g., acyclicity, bipartiteness. Graph grammars provide a rigorous, yet practical, means to support such semantic constraints. Since they can be represented as a graph, a visual language is possible for graph-based modeling environments (and has been developed and implemented). Moreover, that visual language, since it can be represented as a graph, can be represented (and operated on) within the same paradigm.

Since a variety of graph-based models can be represented within the same system, among other useful capabilities, we are able to provide a large degree of support for integrating those models to perform useful work. That integration allows variables across models to be linked, with the values of attributes updated automatically (though the linkages themselves are not specified automatically), and with models capable of referencing (and therefore managing) other models.

Fruitful areas for additional research include:

\- Exploration of hierarchical graphs [50], hypergraphs [3] or higraphs [25] for modeling Frequently, graph-based models involve some form of organization where groups of nodes and edges are collected into a single entity, itself often thought of as a node. Since this form of modeling is quite widely used, exploration of how to support such models would be fruitful.

\- Modeling by Example In order to use graph grammars, the designer must learn how to use graph-grammars. Perhaps it would be possible to allow the designer to demonstrate the particular production desired by adding and deleting nodes and edges as desired. The system would then infer an appropriate production.

\- Application of graph grammars to other models Examples include minimum cost network flow, Geoffrion's Structured Modeling [19], Ma et al.'s LPFORM [41] and Krishnan's PM\* [35].

\- Building Solvers Since many graph-based models, e.g., flowcharts, have a natural procedural implementation, and many solvers are implemented procedurally, graph-grammars and Networks might provide a congenial environment for building solvers. Similarly, many solvers for traditionally “graph-based” models, e.g., vehicle routing, might make good use of graph-grammar productions to specify low level manipulations on graphs.

\- Asynchronous Solver Execution Currently, Networks assumes that solvers run in careful sequence, without interruption. As shown in Dolk and Kottemann, many useful modeling functions are not readily supported in this fashion. The ability of Networks to represent non-sequential execution shows promise for using such models to control solver execution.

In short, we believe that a modeling environment based on graphs and graph grammars can provide practical, useful integrated support for a wide variety of models.

## Acknowledgements

This research has been supported in part by National Science Foundation Grant SES-8917966 and by a grant from the Natural Science and Engineering Research Council of Canada. The author would like to thank Professor Steven Kimbrough, and the editor of the special issue for many inspiring discussions and thoughtful comments.

## References

[1] Arborist Decision Tree Software, Texas Instruments, Inc., PO Box 2909, Mail Station 2240, Austin, TX 78769.

[2] A. Babin, M. Florian, James-Lefebvre and Spiess, EMME/2: an interactive graphic method for road and transit planning, Publication No. 204, Centre de Recherche sur les Transports, Université de Montréal, 1982.

[3] C. Berge, Graphs and Hypergraphs (North-Holland, Amsterdam, 1973).

[4] H.K. Bhargava, A Logic Model for Model Management: An Embedded Languages Approach, unpublished PhD. dissertation, Department of Decision Sciences, the Wharton School, The University of Pennsylvania, 1990.

[5] H. Bhargava, M. Bieber and S.O. Kimbrough, Oona, Max and the WYWWYWI Principle: Hypertext and Model Management in a Symbolic Programming Environment, Proceedings of the Ninth International Conference on Information Systems, December 1988.

[6] H.K. Bhargava and S.O. Kimbrough, On embedded languages for model management, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, Vol. III, 1990.

[7] H. Bhargava, S.O. Kimbrough and R. Krishnan, 1991. Unique Names Violations: A Problem for Model Integration or You Say Tomato, I Say Tomahto, ORSA Journal on Computing, 3, 2 (1991) 107–120.

[8] R. Blanning, An Entity-Relationship Approach to Model Management, Decision Support Systems, 2, 1 (1986).

[9] Bradley, G.H. and R.D. Clemence, Jr., Model Integration with a Typed Executable Modeling Lanauge, Proceedings of the Twenty-First Hawaii International Conference on System Sciences (1988) 403–410.

[10] G.H. Bradley and R.D. Clemence, Jr., A Type Calculus for Executable Modeling Languages, IMA Journal of Mathematics in Management, 1 (1988) 227–291.

[11] Choobineh, J., SQLMP: A Data Sublanguage for Representation and Formulation of Linear Mathematical Models. ORSA Journal on Computing 3, 4 (1991) 358–375.

[12] W.F. Clocksin and C.S. Mellish, Programming in Prolog (Springer-Verlag, Berlin, 1985).

[13] G. Collaud, gLPS: Un système graphique interactif de modélisation de problèmes d'optimation linéaire, Technical report No. 170. Institut pour l'Automation et la Recherche Opérationnelle, University of Fribourg, Fribourg, Switzerland, 1989.

[14] J. Conklin, Hypertext: An Introduction and Survey, IEEE Computer, (1987) 17–41.

[15] R.W. Conway, W.L. Maxwell and L.W. Miller, Theory of Scheduling (Addison-Wesley, Reading, MA, 1967).

[16] Dolk D.R., Structured Modeling and Discrete Event Simulation, presented at the Winter Simulation Conference, 1990, also available as a working paper, Department of Administrative Science, Naval Postgraduate School, Monterey, CA, 1990.

[17] R.D. Eck, A. Philippakis and R. Ramirez, Solver Representation for Model Management Systems, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, Vol III, 1990, 474–483.

[18] M.L. Fisher, A. Greenfield and R. Jaikumar, 1982. VERGIN: A Decision Support System for Vehicle Scheduling, Working Paper 82-06-02, Department of Decision Sciences, The Wharton School, University of Pennsylvania, Philadelphia, PA, 1982.

[19] A.M. Geoffrion, An introduction to structured modeling Management Science 33 (1987) 547–588.

[20] A.M. Geoffrion, Integrated modeling systems. Computer Science in Economics and Management 2 (1989) 3–15.

[21] H. Göttler, Semantical description by two-level graph-grammars for quasihierarchical graphs. Applied Computer Science 13 (1979) 207–209.

[22] H. Göttler, Attributed graph-grammars for graphics. In Graph-Grammars and their Application to Computer Science, pp. 130–142. H. Ehrig, M. Nagl, and G. Rozenberg (eds.), Lecture Notes in Computer Science 153, G. Goos and J. Hartmanis (series eds.) (Springer-Verlag, Berlin, 1983).

[23] H. Göttler, Graph-grammars and diagram editing. in: H. Ehrig, M. Nagl, G. Rozenberg and A. Rosenfeld, Eds., Graph-Grammars and their Application to Computer Science, Eds., (Springer-Verlag, Berlin, 1987).

[24] H. Greenberg, ANALYZE: A Computer-Assisted Analysis System for Linear Programming Models, Operations Research Letters 6 (1987) 249–255.

[25] D. Harel, On visual formalisms. Communications of the ACM, 31 (1988) 514–530.

[26] J.E. Hopcroft and J.D. Ullman, Introduction to Automata Theory, Languages and Computation, (Addison-Wesley, Reading, MA, 1979).

[27] E.L. Hutchins, J.D. Hollan, and D.A. Norman, Direct Manipulation Interfaces, in: D.A. Norman and S.W. Draper, Eds., User Centered System Design: New Perspectives on Human-Computer Interaction, (Lawrence Erlbaum, Hillsdale, NJ, 1986) 87–124.

[28] C.V. Jones, Applications of a graph-based modeling system (GBMS), Working paper No. 88-10-03, Department of Decision Sciences, The Wharton School, The University of Pennsylvania, 1988.

[29] C.V. Jones, An Example Based Introduction to Graph-Based Modeling, Proceedings of the Twenty-Third Annual Hawaii Conference on the System Sciences, Kona, HI (1990) 433–442.

[30] C.V. Jones, An introduction to Graph-Based Modeling Systems, Part I: Overview, ORSA Journal on Computing, 2, 2 (1990) 136–151.

[31] C.V. Jones, An Introduction to Graph-Based Modeling Systems, Part II: Graph-Grammars and the Implementation, ORSA Journal on Computing, 3, 3 (1991) 180–207.

[32] Jones, C.V., Attributed Graphs, Graph-Grammars, and Structured Modeling, Annals of OR, forthcoming, 1992.

[33] C.V. Jones, and R. Krishnan, A Visual, Syntax-Directed Environment for Automated Model Development, Technical Report, Faculty of Business Administration, Simon Fraser University, Burnaby, BC, Canada, 1990.

[34] J.E. Kottemann, and D.R. Dolk, Model integration and modeling languages, Working Paper, Department of Administrative Sciences, Naval Postgraduate School, Monterey, CA, 1990.

[35] R. Krishnan, PDM: a knowledge-based tool for model construction, In: R. Blanning and D. King, Eds., Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, Vol III (1989) 467–474.

[36] R. Krishnan, (1990) A Logic Modeling Language for Model Construction, Decision Support Systems, 6 (1990) 123–152.

[37] R. Krishnan, PDM: A Knowledge. Based Tool for Model Construction, Decision Support Systems, forthcoming, 1991.

[38] J.K. Lee, Artificial Intelligence and Optimization. working paper, Center for Integrated Manufacturing Decision Systems, The Robotics Institute, Carnegie-Mellon University, Pittsburgh, PA, 1990.

[39] J.S. Lee, Structure Frame Based Model Management System, unpublished PhD dissertation, Department of Decision Sciences, the Wharton School, The University of Pennsylvania, Philadelphia, PA, 1990.

[40] T. Liang, Modeling by Analogy: A Case-based Approach to Model Construction. BEBR Faculty Working Paper No. 89–1524, University of Illinois at Urbana-Champaign, 1989.

[41] P. Ma, F.H. Murphy and Stohr, E.A., 1989. Design of a Graphics Interface for Linear Programming, Communications of the ACM, 32, 8 (1989) 996–1012.

[42] McNamee, P. and J. Celona, Decision Analysis for the Professional with Supertree (Scientific Press, Palo Alto, CA, 1987).

[43] Nagl, M., Formal languages of labelled graphs, Computing, 16 (1976) 113–137.

[44] Nagl, M., Set theoretic approaches to graph grammars. In: H. Ehrig, M. Nagl, G. Rozenberg and A. Rosenfeld, Eds., Graph-Grammars and their Application to Computer Science, 41–54 (Springer-Verlag, Berlin, 1987).

[45] M. Nagl, A software development environment based on graph technology. In: Ehrig, H., Nagl, M. Rozenberg, G. and A. Rosenfeld (eds.), 458–478, Springer-Verlag, Berlin.

[46] D.R. Olsen, D. Kasik, J. Rhyne and J. Thomas, ACM SIGGRAPH Workshop on Software Tools for User Interface Management, Computer Graphics 21, 2 (1987) 71–72.

[47] C.D. Pegden, Introduction to SIMAN with Version 3.0 Enhancements, Systems Modeling Corporation, Calder Square P.O. Box 10074, State College, PA 16805-0074, 1985.

[48] G.E. Pfaff, Ed., User Interface Management Systems, (Springer-Verlag, Berlin, 1985).

[49] R.A. Pick, and M.M. Sklar, A software system that emulates LP formulation experts, working paper, University of Cincinnati, Cincinnati, OH, 1990.

[50] T.W. Pratt, Definition of programming language semantics using grammars for hierarchical graphs, In: V. Claus, H. Ehrig, and G. Rozenberg, Eds., Graph-Grammars and their Application to Computer Science and Biology (1979) pp. 389–400, G. Goos and J. Hartmanis, Eds., Lecture Notes in Computer Science 73 (Springer-Verlag, Berlin, 1979).

[51] A.A.B. Pritsker, Introduction to Simulation and SLAM II (Halsted Press, New York, 1984).

[52] H. Raiffa, Decision Analysis (Addison-Wesley, Reading, MA, 1968).

[53] T. Reps and T. Teitelbaum, The synthesizer generator, Proceeding of the ACM Sigsoft/Sigplan Symposium on Practical Software Development Environments, ACM Sigplan Notices 19, 5 (1984) 42–48.

[54] Savage, S.L., Mathematical modeling databases, presentation at the TIMS/ORSA Joint National Meeting, Las Vegas, NV, May 7–9, 1990.

[55] Shneiderman, B., Direct manipulation: a step beyond programming languages, IEEE Computer 16, 8 (1983) 57–69.

[56] L. Schrage, Linear, Integer and Quadratic Programming with LINDO, 3rd Edition (The Scientific Press, Palo Alto, CA, 1986).

[57] C.R. Standridge, Performing simulation projects with the extended simulation system (TESS), Simulation 45, 6 (1985) 283–291.
