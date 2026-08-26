---
otero_id: 21555
otero_key: "ZYEYFCVY"
title: "An implementation of a graph-based modeling system for structured modeling (GBMS/SM)"
authors: "Kaushal Chari; Tarun K Sen"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00056-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An implementation of a graph-based modeling system for structured modeling GBMSž / <sup>r</sup>SM

Kaushal Chari <sup>)</sup>, Tarun K. Sen <sup>1</sup>

Department of Information and Decision Sciences, College of Business, James Madison UniÕersity, Harrisonburg, VA 22807, USA Department of Accounting, Pamplin College of Business, Virginia Polytechnic Institute and State UniÕersity, Blacksburg, VA 24061-0101, USA

## Abstract

This paper describes GBMS<sup>r</sup>SM, a graph-based modeling system based on structured modeling that supports model formulation, maintenance and solution. Key features of GBMS<sup>r</sup>SM include the following: 1 model construction usingŽ . graphical inputs, 2 modeling in multiple problem domains, 3 syntax-directed editing, 4 model views at different levelsŽ . Ž . Ž . of detail, 5 automation of model data acquisition, and 6 interfaces to solvers, spreadsheets and databases. This paperŽ . Ž . presents design and implementation details of GBMS<sup>r</sup>SM that are of general interest to graphical modeling system designers. Challenges that were encountered in the development of GBMS<sup>r</sup>SM are emphasized in this paper. q 1998 Elsevier Science B.V.

Keywords: Structured modeling; Graphical modeling systems; Model management

## 1. Introduction

GBMS<sup>r</sup>SM Graph-Based Modeling System forŽ Structured Modeling , belongs to the class of model-. ing systems that provide organizations the ability to create, store and solve models for decision-making. Models like data, are key organizational assets that need to be managed. A modeling system is therefore, crucial for supporting organizational decision-making. A modeling system’s utility is enhanced when it is able to support modeling in multiple problem domains and is user-friendly. Developing a userfriendly modeling system that provides broad support for organizational decision-making is the primary goal of this research. The development of

GBMS<sup>r</sup>SM is a significant step towards achieving this goal.

For the sole purpose of clarifying the contributions of this paper, a distinction is made between the approach used to develop GBMS<sup>r</sup>SM and the actual design and implementation of the GBMS<sup>r</sup>SM prototype. The GBMS<sup>r</sup>SM approach is based on the core concepts of structured modeling 19 . Structured <sup>w</sup> <sup>x</sup> modeling by Geoffrion provides a theoretically sound framework to support modeling in multiple problem domains. The GBMS<sup>r</sup>SM approach uses structured modeling as the basis to materialize a modeling system that is broad in scope, i.e., able to manage a variety of models including optimization models, AI models, statistical models, database models, spreadsheet models, etc.

The GBMS<sup>r</sup>SM approach uses an acyclic graph to represent a model schema. The theoretical basis for this is again, structured modeling. The GBMS<sup>r</sup>SM approach extends structured modeling to allow for a graphical model representation scheme that is computationally active. The use of a graphical model representation scheme facilitates user comprehension of models as well as user-friendly modeling systems. Models can be built in the ‘point and click environment of a graphical user interface using graphical inputs. Furthermore, the computationally active graphical model representation can be easily evaluated to obtain model solutions.

The GBMS<sup>r</sup>SM prototype provides the following attractive features to users: 1 a user-friendly inter- Ž . face for creating, maintaining and solving models; Ž . Ž . 2 support for modeling in multiple domains; 3 model construction using graphical inputs with little or no algebraic input; 4 syntax-directed editing to Ž . prevent the construction of incorrect models; 5Ž . model views at different levels of detail to facilitate better comprehension of models; 6 automation ofŽ . model instance data acquisition; 7 support for Ž . solvers; and 8 linkages to spreadsheets and Ž . databases to support query and analysis of model data.

T h e r e a r e s e v e r a l g r a p h ic a l 1 – <sup>w</sup> 3,13,14,18,24,28,31,36,38 and non-graphical <sup>x</sup> <sup>w</sup> <sup>x</sup> 4,10,15–17,20–23,25,29,30,33,37 modeling approaches, languages and systems. Non-graphical languages and systems by their inherent nature lack user-friendly features such as model construction using graphical inputs. The graphical systems listed above with few exceptions, are either domain-specific or support only some stages of a model’s life cycle such as model formulation. A notable graphical system of sufficient generality and capabilities that is similar to GBMS<sup>r</sup>SM is Networks<sup>r</sup>SM by Jones <sup>w</sup> <sup>x</sup> 28 . Networks<sup>r</sup>SM supports model formulation, maintenance and solution. However Networks<sup>r</sup>SM, which is based on graph grammar 26,27 , lacks the<sup>w</sup> <sup>x</sup> rich indexing facilities available in the GBMS<sup>r</sup>SM prototype. Furthermore, Networks<sup>r</sup>SM does not provide links to external solvers, databases and spreadsheets. Other notable graphical modeling systems of sufficient generality include IGOR 24 and <sup>w</sup> <sup>x</sup> MODASS 18 . IGOR is based on semantic data <sup>w</sup> <sup>x</sup> modeling concepts and primarily supports model formulation. MODASS uses an object-oriented language called BLOOMS 17 for representing models. <sup>w</sup> <sup>x</sup>

The model representation capability in MODASS depends on the model classes available in BLOOMS.

This paper describes in detail how the attractive features available to users described earlier are realized in the GBMS<sup>r</sup>SM prototype. Specific details on the GBMS<sup>r</sup>SM approach pertaining to the model representation scheme and the syntax of the modeling language are beyond the scope of this paper. These can be found in Ref. 11 . This paper presents <sup>w</sup> <sup>x</sup> design and implementation ideas pertaining to GBMS<sup>r</sup>SM prototype that are of general interest to graphical modeling system designers. These ideas can be used in developing commercial modeling systems.

The design and implementation of the GBMS<sup>r</sup>SM prototype contributes to the DSS literature in many ways. First and foremost, it demonstrates the feasibility of the GBMS<sup>r</sup>SM approach that includes: 1Ž . the use of computationally active acyclic graphs to represent models, 2 the synthesis of models using Ž . graphical inputs with little or no algebraic input; and Ž . 3 the use of relational constructs in a modeling language to support complex indexing and automation of model instance data acquisition. Second, the open systems architecture of the GBMS<sup>r</sup>SM prototype provides means to integrate multiple solvers with a modeling system. Third, the implementation details of GBMS<sup>r</sup>SM provide insights for developing a comprehensive graphical modeling system to support model construction, maintenance and solution.

This paper is organized as follows. Section 2 presents the basic principles underlying the GBMS<sup>r</sup>SM approach. Section 3 describes GBMS<sup>r</sup>SM from an end-user’s perspective. The architecture underlying GBMS<sup>r</sup>SM is presented in Section 4. Implementation details of GBMS<sup>r</sup>SM are presented in Section 5. Contributions of this paper, and challenges encountered during GBMS<sup>r</sup>SM implementation are presented in Section 6. Appendix A contains a description of the feed-mix model. This model is used to describe the GBMS<sup>r</sup>SM prototype.

## 2. Basic principles of the GBMS<sup>r</sup>SM approach

The GBMS<sup>r</sup>SM approach is based on some basic principles. These principles have one fundamental objective underlying them, i.e., to reduce the complexities involved in creating and manipulating models for problem-solving. They are described below.

## 2.1. Model data independence

Model data independence refers to the specification of a model schema that is independent of the data used for generating a model instance. An advantage of this independence is that a single model representation can be used to generate multiple model instances. Thus, a single model schema of a transportation model for instance, is all that is needed to be stored in the model library for generating multiple model instances of the transportation model.

## 2.2. Model-solÕer independence

Model-solver independence pertains to a model representation scheme that is solver-neutral and its expressive power unconstrained by any solver. This facilitates the use of multiple solvers in a modeling system.

## 2.3. Model representation scheme of sufficient generality

A model representation scheme of sufficient generality enables a modeling system to store and manage models belonging to a wide variety of domains such as artificial intelligence, databases, mathematical programming, statistics, etc.

## 2.4. Graphical model representation scheme

A graphical representation of a model schema allows users to synthesize models using graphical objects via a graphical user interface. The use of graphical objects can reduce algebraic inputs significantly. Furthermore, users have additional flexibility to visualize and define models.

## 2.5. Modular representation of models

A modular representation of model schema permits models to be viewed at various levels of detail. Similar concepts can be grouped together into higher level objects. This facilitates a simplified presentation of complex models to users.

## 2.6. Use of relational tables

The use of relational tables to store model schema, instance data, and solutions provides many advantages. First, data-driven processes are more efficient since relational operators can be used to manipulate data. Second, model data and solution can be easily transferred across many different environments such as solvers, spreadsheets, and databases for analyses and queries.

2.7. Modeling language support for relational constructs

A modeling language that supports relational constructs in addition to arithmetic and logical constructs allows model expressions to directly reference relational databases. This facilitates the automation of model instance data acquisition. Relational constructs also provide support for complex indexing in a modeling language.

## 2.8. Open systems architecture

Open systems architecture permits a modeling system to support various external systems such as solvers.

## 3. Users’ view of GBMS<sup>r</sup>SM

The GBMS<sup>r</sup>SM prototype is described in this section with the aid of the feed-mix model presented in Appendix A. The feed-mix model is a commonly used linear programming model found in the literature. A model schema in GBMS<sup>r</sup>SM is represented by a model graph 11 . Model graphs are directed <sup>w</sup> <sup>x</sup> acyclic graphs, whose nodes represent definitions, and edges represent definitional dependencies, i.e., a calling node’s Ž . tonode’s definition is dependent on the definitions of one or more called nodes Ž fromnodes.. In the feed-mix model graph presented in Fig. 1, the definition of quancost for example, is dependent on the definitions of quantity and unitcost.

![](/api/attachments/ZYEYFCVY/fulltext/images/d811df5f6a60952c84c34385fabe823727f7fabedcbe55c922ba7aa4ac2805f6.jpg)  
Fig. 1. Model graph representation of the feed-mix model at the greatest level of detail.

Model graph nodes are of six types: primitiÕe entity nodes, that represent the basic modeling entities; compound entity nodes, whose definitions depend on one or more primitive or compound entity nodes; attribute nodes, that represent attributes of primitive and compound entity nodes; function nodes, whose definitions are primarily based on arithmetic expressions; test nodes, that evaluate to true or false; and module nodes, that encapsulate a sub-graph containing a group of related nodes. These node types are illustrated using the feed-mix model. In Fig. 1, nutrnt and material are primitive entity nodes, m\_d\_requm, analysis, quantity, and unitcost are attribute nodes, analquan, quancost, nutleÕel and cost\_fm are function nodes, and tnut is a test node. A module node nutaÕail can be found in the model graph of Fig. 2. nutaÕail encapsulates analysis, analquan and nutleÕel, thereby, enabling a model graph representation of the feed-mix model at a lower level of detail.

![](/api/attachments/ZYEYFCVY/fulltext/images/66bbebdce11b3ed886bcddcfe427dd38500c694c1f153477a38f77a9bbe5dcb3.jpg)  
Fig. 2. Model graph representation of the feed-mix model using a module node.

An elemental detail table is associated with every model graph node except module nodes . In theŽ . general case, an elemental detail table consists of <sup>-</sup>index, Õalue<sup>)</sup> tuples, where index represents an index value and Õalue represents the corresponding node value. For example, the tuple <sup>-</sup>2, 20<sup>)</sup> in the elemental detail table associated with the node quantity represents the node value of 20 i.e., quantity Ž . corresponding to the material with the index value of 2.

Model graph edges are of three types: relation edges represent definitional dependencies that do not involve the transfer of <sup>-</sup>index, Õalue<sup>)</sup> tuples from the elemental detail tables of the called nodes to the calling node; index edges represent definitional dependencies that require the transfer of index values from the elemental detail tables of the called nodes to the calling node; Õalue edges represent definitional dependencies that require the transfer of <sup>-</sup> index, Õalue<sup>)</sup> tuples from the elemental detail tables of the called nodes to the calling node.

Nodes and edges have attributes such as node\_expression and edge\_expression, respectively that contain expressions in a computer-executable language called MEL 11 . These expressions when evaluated,<sup>w</sup> <sup>x</sup> create elemental detail tables. In order to facilitate graphical input of model expressions, graphical objects such as nodes and edges encapsulate MEL expression templates. This is illustrated later.

GBMS<sup>r</sup>SM provides a friendly graphical user interface containing palettes, menus and dialog boxes for synthesizing models. The following example illustrates how the graphical user interface is used to synthesize models. In order to create a node such as cost\_fm in the feed-mix model graph, the user first selects the ‘sum’ icon from the palette. A dialog box as shown in Fig. 3 appears. After typing the name of the node, the user then drags the mouse to the location in the graph where cost\_fm node is to be displayed. The cost\_fm node is then displayed at that screen location.

In order to add an edge from the called node quancost to the calling node cost\_fm, the user selects the ‘Connect’ sub-option from the ‘Edit’ pop-up menu and then clicks the mouse left button at quancost followed by a mouse left button click at cost\_fm. A dialog box as shown in Fig. 4 appears. This dialog box has default values. These values are generated based on node connections and include the edge name which is Ž quancost, i.e., the calling node’s

![](/api/attachments/ZYEYFCVY/fulltext/images/abd7c68e5e6503f475c0d7e7ef7a9cb98058f931b4332d6b0427a5b13916fd4b.jpg)  
Fig. 3. Dialog box for specifying a new node name.

![](/api/attachments/ZYEYFCVY/fulltext/images/a8a45aad41ac627f2129bc9612a256b46381cbadad77f03b3d5dfc8f223019e3.jpg)  
Fig. 4. Dialog box for edge specifications.

name and the edge type. The user can then let the. system generate the edge expression @SELECT <sup>-)</sup>Ž . quancost automatically by clicking the mouse left button on ‘ Auto’. The system uses the default edge expression template @SELECT <sup>-)</sup> Žcalled node to generate this expression. The expression for . the edge from quancost to cost\_fm permits all tuples associated with the elemental detail table of quancost to be transmitted by the edge for use in the generation of the elemental detail table of the node cost\_fm. When the user clicks the mouse left button on ‘OK ’ followed by a click on the cost\_fm node, the edge from quancost to cost\_fm is defined in the graph.

![](/api/attachments/ZYEYFCVY/fulltext/images/948a09a4b9522fa7bab86f18f33346830603cbffd61a5460d7c431916e55a98e.jpg)  
Fig. 5. Dialog box for node definition.

The expression for cost\_fm can now be generated. The user can open the dialog box as shown in Fig. 5 by clicking the mouse right button at cost\_fm. Default values for node name, index clause, input port automatically appear in Fig. 5. Since the index variable associated with the incoming edge from quancost is $j ,$ the default summation index expression in the index clause is based on index $j .$ This expression: $j < 0 \colon - 1 >$ specifies the summation of values transmitted by the edge from quancost over all values of index $j .$ Upon clicking the mouse left button $\mathrm { o n } \ ^ { \cdot } A u t o ^ { \cdot }$ , the system automatically generates the node expression from the default expression template associated with the SUM function node type: @ SUM <sup>-</sup> filter\_clause <sup>) -</sup> index\_clause $>$ Ž . argument . The node expression $\ @ \operatorname { S U M } < > < j <$ $0 { : } - 1 > > ( \mathrm { q u a n c o s t } )$ , and the node index variable Ž . which is null due to summation are then displayed. Note, the filter clause, which represents a condition to filter out tuples from participating in the node operation, is null. In general, filter clauses need not be null, for instance, when the expression $\Sigma _ { i } ~ \Sigma _ { j }$ is evaluated for $i \neq j .$ . In this case, the filter clause is $\textstyle ( { a } \mathrm { { N E } } ( i , j )$

Sometimes default expression templates associated with various node types may not be suitable for a particular node expression. For example, in case of generic function node types, node expressions typically involve the nesting of arithmetic primitives, and are not generalizable. In such situations, node expressions can be synthesized graphically using primitive function node types or typed manually.

Syntax checking is done by the system when users create and interconnect graphical objects on the screen. Error messages are displayed in case of syntax violations. A sample error message is displayed in Fig. 6. In this case, the user attempts to connect the attribute node analysis to the attribute node quantity. This is not allowed since attribute nodes cannot call other attribute nodes follows fromŽ the core concepts of structured modeling ..

The complexity of a model graph can be reduced significantly by encapsulating sub-graphs in module nodes. The user can create a module node by clicking the mouse left button at the $" m '$ icon in the palette and then marking out the top left and the bottom right coordinates of an imaginary rectangle that covers the screen containing the nodes to be encapsulated. The system then hides all the nodes within this rectangle and then displays one module node instead, with proper edge connections to other nodes outside the module. The screen is therefore, less cluttered since a single module node representing a concept at a higher level of abstraction can replace a sub-graph of closely related nodes. In the feed-mix model graph of Fig. 2, the module node nutaÕail, representing the concept of nutrient availability encapsulates analysis, analquan and nutleÕel. This graph at a lower level of detail is less cluttered. A module node can be exploded anytime to reveal the encapsulated nodes. This is done by double clicking the mouse left button at the module node followed by a single mouse left button click.

![](/api/attachments/ZYEYFCVY/fulltext/images/7cef05b288a7bb644c4f59bdceb811ca19acd3c30141536ef55b70d71a7e4f38.jpg)  
Fig. 6. Message box displaying an error message, generated during syntax-directed editing.

![](/api/attachments/ZYEYFCVY/fulltext/images/7c1eaa32217183b88ffc565714ebee977df854f5b639b663ba9629965563b049.jpg)  
Fig. 7. Dialog box for specifying parameters used in the generation of a GAMS input file.

![](/api/attachments/ZYEYFCVY/fulltext/images/a22c790b3f8be8dc360d7ed45fe4ee48e7180c73c1490e932b5f98e0ad71ce71.jpg)  
Fig. 8. A screen of the GAMS input file representing a feed-mix model instance.

![](/api/attachments/ZYEYFCVY/fulltext/images/7e09d94eda2fa64cb0a0f9e1e224c8294b20705654cc71e9af8f1b72e7438af9.jpg)

GBMS<sup>r</sup>SM currently supports two different solvers: the internal MEL expression evaluator and GAMS 10 . GAMS is used when optimization is <sup>w</sup> <sup>x</sup> required to be performed to obtain a solution. For example, GAMS can determine the quantities of various materials values ofŽ . quantity node that minimize the total cost of material Ž . cost\_fm . The user can create a GAMS input file by selecting the GAMS sub-option in the ‘SolÕe’ pop-up menu. Another pop-up menu appears and the user then selects the ‘Create’ sub-option. The dialog box as shown in Fig. 7 appears. The user then specifies the entries required for the dialog box. A GAMS input file as shown in Fig. 8 is then generated based on the feed-mix model graph. Node expressions for primitive entities: nutrnt and material, and attributes: m\_d\_ reqm, analysis and quantity Žsee Table 1 in Appendix A contain relational constructs for model. instance data acquisition from external relational tables known as source database tables. Fig. 9 illustrates the source database tables used in the feed-mix example. The GAMS input file generation procedure retrieves the necessary model instance data from source database tables based on these relational constructs and creates a GAMS input file. A GAMS

Fig. 9. Source database tables for the feed-mix model.

solver can then be invoked to solve the model instance specified in the input file.

The internal MEL expression evaluator does not perform optimization but merely evaluates the MEL expressions associated with the nodes. This evaluator is invoked when the user chooses the SolÕe option on the menu and clicks on the option MEL EÕaluator. The MEL expression evaluator can be used when the values of all the attribute nodes are known and are retrieved from source database tables. The elemental detail tables in Fig. 10 are generated by the MEL expression evaluator when values of quantity are known.

Table 1  
MEL node expressions for the feed-mix model  
```txt
MEL node expressions for the feed-mix model
Node name Node expression in MEL
nutrnt @ADDINDEX < > (@PROJECT < > (r_nut;nid);i)
material @ADDINDEX < > (@PROJECT < > (r_mat;mid);j)
m_d_reqm @PROJECT < > (@JOIN < @EQ(nid,nid) > (nutrnt,r_nut);i,m_d_reqm)
analysis @PROJECT < > (@JOIN < @EQ(nid,nid) > (nutrnt,@JOIN < @EQ(mid,mid) > (material,r_anal));i,j,analysis)
quantity @PROJECT < > (@JOIN < @EQ(mid,mid) > (material,r_mat);j,quantity)
unitcost @PROJECT < > (@JOIN < @EQ(mid,mid) > (material,r_mat);j,unitcost)
analquan @ * < @EQ(j,j) > (analysis,quantity)
quancost @ * < @EQ(j,j) > (quantity,unitcost)
cost_fm @SUM < > < j < 0: - 1 > > (quancost)
nutlevel @SUM < > < j < 0: - 1 > > (analquan)
tnut @LE < @EQ(i,i) > (m_d_reqm,nutlevel)
nutavail
```  
nutaÕail has no expression since it is a module node.

![](/api/attachments/ZYEYFCVY/fulltext/images/0cc7805d4d44248b8e6d312f79c49f9fc892a943c4169f77e0f69e266ebd9cfb.jpg)  
Fig. 10. Elemental detail tables generated by the MEL expression evaluator.

The user can select the ‘Query’ pop-up menu to view node definitions and elemental detail tables. In order to view the definition of a particular node such as quancost for instance, the user first selects the ‘Display Node Defn.’ sub-option from the ‘Query’ pop-up menu and then clicks the mouse left button on the node whose definition is to be displayed Ž . quancost in this case . A child window as shown in Fig. 11 appears with the information on quancost. The user can open an elemental detail table associated with any node for further analysis in a database environment such as Paradox 8 or in a spreadsheet <sup>w</sup> <sup>x</sup> environment such as Quattro 9 . This is done by <sup>w</sup> <sup>x</sup> selecting the sub-option in the pop-up menu ‘Elemental Table’ under ‘Query’ and then clicking on the appropriate node. The elemental detail table associated with quancost opened in the Quattro environment is displayed in Fig. 12.

## 4. GBMS<sup>r</sup>SM implementation architecture

The architecture underlying GBMS<sup>r</sup>SM is illustrated in Fig. 13. The various sub-systems shown in Fig. 13 are classified into the following categories:

![](/api/attachments/ZYEYFCVY/fulltext/images/1d68ebcd8c2f8291c54598a557f6f025856725b1c371e465b4bda1948570709c.jpg)  
Fig. 11. Node information for quancost.

![](/api/attachments/ZYEYFCVY/fulltext/images/0f28954419f8f415c760f69ddb0672c5c815d8ccb69b37be85342269e921d067.jpg)  
Fig. 12. Elemental detail table of quancost opened in the Quattro environment.

![](/api/attachments/ZYEYFCVY/fulltext/images/ba6f07e31be4329a1e453d7b46cd8b8ac30a7a32f0c06e7716b139e1fb731d69.jpg)  
Fig. 13. Detailed architecture of GBMS<sup>r</sup>SM.

model editing, retrieval and storage, query, and solution.

## 4.1. Model editing

This sub-system includes the graph editor, the user interface module, the MEL expression builder, and the MEL index evaluator and parser. The graph editor logic and the graphical user interface logic are combined into a single module. This is done to facilitate seamless integration of the two. Operations supported by the graph editor include the following: creating nodes, connecting nodes via edges, deleting nodes and edges, moving nodes and edges, and encapsulating sub-graphs into module nodes. The graph editor also enforces syntax-directed editing. In case of syntax violations while editing graphs, error messages are displayed see Fig. 6 for an example . Ž . The conceptual framework of structured modeling provides the basis for syntax-directed editing. The graphical user interface logic provides tools such as palettes, menus and dialog boxes to create and edit models, retrieve and store models, obtain model solutions, and query model information.

As stated earlier, the graphical objects in model graphs encapsulate model expressions in MEL. Expressions in MEL are computer-executable and therefore, permit model graphs to be computationally active. When graphical objects are created and interconnected, the graph editor invokes the MEL expression builder module. This module automates model expression construction. The MEL expression builder uses predefined expression templates associated with various node and edge types to construct model expressions. While generating model expressions, the MEL expression generator also uses any information that is supplied by the user as well as information about the existing node interconnections. In order to prevent the user from specifying incorrect information, the graph editor provides list boxes with appropriate choices whenever possible. For example, while defining the attribute node unitcost in the feed-mix model, the attribute specification dialog box Fig. 14 incorporates a list box that contains allŽ . source database tables. The user is therefore, constrained to select a table from this list box for retrieving attribute values.

The graph editor invokes the MEL index evaluator and parser module for checking MEL expressions and generating index variable sets. Any syntactically incorrect MEL expression entered is trapped by this module, which then generates an appropriate error message. In order to realize processing efficiencies, the logic for index evaluation as well as MEL syntax checking is executed at the same time. The index variable set of a node is dependent on the node interconnections and the node type. The MEL index evaluator and parser module computes this set based on indexing rules that are associated with various node types. For example, in the case of the SUM function node nutleÕel Ž . Fig. 1 , the node expression @SUM<sup>-)-</sup>j<sup>-</sup>0:<sup>y</sup>1<sup>))</sup>Ž . analquan represents the summation over index j. The index variable set for nutleÕel is based on the rule associated with the SUM function node type and is computed as follows: $I _ { \mathrm { n u t l e v e l } } = I _ { \mathrm { a n a l q u a n } } - I _ { \mathrm { s u m m a t i o n } } = \{ i , j \} - \{ j \} = \{ i \}$

![](/api/attachments/ZYEYFCVY/fulltext/images/cf80e6a9d42e69aa558668273130bbd494532573dd6d6da4d48810de9a35c24f.jpg)  
Fig. 14. Dialog box for defining an attribute node.

## 4.2. Model retrieÕal and storage

Modules in this sub-system include the model library interface modules for model retrieval and storage. Three relational tables support the model library: nodetab, edgetab and graphtab, where nodetab stores node information, edgetab stores edge information and graphtab stores graph information. The model retrieval module obtains model information from nodetab, edgetab and graphtab and stores them in appropriate data structures accessible to the graph editor. The graph editor then generates and displays the appropriate graphical image. Model information is saved in the model library by the model storage module, which takes model data and saves it in nodetab, edgetab and graphtab. The use of relational tables to store the model library makes it possible to analyze and query model information in GBMS<sup>r</sup>SM as well as in external environments such as Paradox and Quattro.

## 4.3. Model queries

Query interface modules support query facilities in GBMS<sup>r</sup>SM. One module displays answers to queries related to value-based information from elemental detail tables. While another query module displays answers to queries related to model-based information using model information stored in the system data structure. Other modules provide interfaces to external database and spreadsheet environments. The use of relational tables for storing elemental detail tables makes it possible to analyze and query model instance data over many different environments.

## 4.4. Model solution

Model solution activity modules include solver interface and constraint checker modules. The constraint checker is invoked before model expressions are evaluated. The need for constraint checking arises since syntax-directed editing during graph editing ,Ž . does not check for certain constraint violations. This is done primarily to improve run-time performance. The constraint checker module checks for acyclicity and connectivity constraint violations. In case of constraint violations, appropriate error messages are displayed and the system does not permit the solution process to proceed. Various solver interface modules invoke the constraint checker.

A solver interface module is specific to a solver. It is responsible for retrieving model graph and MEL expressions from the system data structure, evaluating MEL expressions, retrieving model instance data from source database tables, generating elemental detail tables, translating a model instance to a solver-specific format, launching the solver, and finally returning the solution generated by the solver to the elemental detail tables.

A solver interface module can evaluate MEL expressions to create elemental detail tables by processing model graph nodes. A model graph node can be processed only when all the nodes it calls have been processed. The processing step typically involves generating an elemental detail table for the node, based on values retrieved from source database tables or values obtained via mathematical computations. When optimization is performed, the processing step also includes the generation of an appropriate solver-specific input file for use by a solver. In order to process nodes in the proper sequence, an appropriate procedure is required. This procedure can sort nodes in the proper sequence and then evaluate each node one at a time in that sequence. Other variations can also be used. Module nodes are not evaluated since the nodes encapsulated by them get evaluated.

In order to evaluate each node, a recursive procedure EÕaluate can be used. The example in Fig. 15 illustrates how EÕaluate works. In this example, a call to EÕaluate is made with the node expression ${ \ @ ^ { * } < > ( \ @ \mathbf { S U M } < > < i < 0 \ d : - 1 > > ( a ) , b ) }$ as the input parameter. The EÕaluate procedure parses the Ž input parameter into two sub-expressions since ) is a binary construct and makes two recursive calls. with expressions $\ @ \mathrm { S U M } < > < i < 0 : - 1 > > ( a )$ and b as input parameters. In the case of parameter b, the EÕaluate procedure determines b to be an edge having the default name b Ži.e., the name of the fromnode. with the edge expression: @SELECT<sup>-</sup> $\textcircled { a } \mathrm { E Q } ( j , 1 ) > ( b )$ . The edge name b is then replaced by the edge expression $\circledcirc \mathrm { S E L E C T } < \circledcirc \mathrm { E Q } ( j , 1 ) >$ Ž . b and a recursive call is made again. Note that the argument of the edge expression is the name of node b and therefore, the input parameter in the recursive call to EÕaluate has the node name b. The recursion continues till the input parameter of EÕaluate is a number, node name, or source database table name.

![](/api/attachments/ZYEYFCVY/fulltext/images/dcc09329a36070db41d3e3801a7827325639b138bd091d2fa23709ec04e8b1f0.jpg)  
Fig. 15. Function calls in the evaluation of a sample MEL expression.

When the input parameter is a number, the numeric value associated with the number is returned. In the case of node name, the data from the elemental detail table associated with the node stored as aŽ relational table created earlier is returned to the. EÕaluate procedure’s data structure. When the input parameter is a source database table name, the entire table is dumped into the EÕaluate procedure’s data structure.

Every call to EÕaluate returns an elemental detail table associated with the input parameter for that call Ž . Fig. 16 . Arithmetic, logical, and relational operations are performed on the elemental detail tables at various levels of recursion based on the outermost MEL construct in the input parameter of the current call to EÕaluate. In the expression above for edge b, the unary construct SELECT returns the elemental detail table of the construct argument after filtering out rows based on the specified filter clause. The binary construct ‘<sup>)</sup> ’ returns the elemental detail table t0, which is a product of elemental detail tables t1 and t2.

![](/api/attachments/ZYEYFCVY/fulltext/images/208765d74afa3e0164dacc704d7f8f035c75286d38b986563ade83d6552909a6.jpg)  
Fig. 16. Elemental detail tables created for the example in Fig. 15.

## 4.5. Basic principles supported by the architecture

The basic principles underlying the GBMS<sup>r</sup>SM approach described in Section 2 are supported by Ž . the GBMS<sup>r</sup>SM Architecture. The use of model graphs for representing model schemata provides model data independence since model graph representations are unconstrained by model instance data. Model graphs are also capable of representing models belonging to various problem domains and allow users to synthesize models using graphical objects. Furthermore, model graphs support module nodes. Model-solver independence is also supported. The GBMS<sup>r</sup>SM architecture provides a clean separation between solvers and models. Model schema representations based on model graphs are not constrained by any solvers.

The use of MEL to represent model graph expressions provides many benefits. First, complex indexing is supported. Second, the automation of model instance data acquisition is possible since MEL supports relational constructs that directly reference relational database tables. Thus, a solver interface module on evaluating a MEL node expression can retrieve model instance data from source database tables without user intervention.

In the GBMS<sup>r</sup>SM architecture, model library, source database tables and elemental detail tables are represented by relational tables. Since elemental detail tables are relational tables, they provide a solver-neutral format for storing model instance data. Theoretically, any solver can be used with GBMS<sup>r</sup>SM. What is required is a solver-specific interface module. The GBMS<sup>r</sup>SM architecture permits all solver interface modules to access model graphs and related MEL expressions stored in the system data structure in a uniform manner.

## 5. The GBMS<sup>r</sup>SM implementation

The implementation of GBMS<sup>r</sup>SM prototype aims to incorporate the three characteristics of a modeling environment proposed by Neustadter et al. <sup>w</sup> <sup>x</sup> 34 . These are: support for multiple modeling paradigms; support for different categories of tools such as math programming solvers, spreadsheets and databases; and support for all phases of the modeling life cycle. The current implementation of GBMS<sup>r</sup>SM incorporates the first two characteristics completely while the third characteristic is partially implemented.

The GBMS<sup>r</sup>SM prototype has been implemented for Windows 3.1 using Borland C<sup>qq</sup> 3.1 5 and<sup>w</sup> <sup>x</sup> Paradox Engine 3.0 7 . The Object Windows Li-<sup>w</sup> <sup>x</sup> brary OWL 6 available with Borland CŽ . <sup>w</sup> <sup>x</sup> <sup>qq</sup> 3.1 is used extensively to implement the graph editor. Paradox Engine calls allow the C<sup>qq</sup> application to retrieve and store model data in Paradox tables and to create elemental detail tables. Windows’ API calls allow the C<sup>qq</sup> application to link with the Paradox database 8 and Quattro spreadsheet 9 environ- <sup>w x</sup> <sup>w x</sup> ments. The translation of model data from one format to another is avoided while transferring it across multiple environments such as C<sup>qq</sup> and Quattro. This is made possible by using software products from the same vendor, i.e., Borland.

An object-oriented approach is used in the implementation of the GBMS<sup>r</sup>SM prototype. Advantages of this approach include the reusability of code and the use of class libraries. Significant portions of the code pertaining to the graph editor<sup>r</sup>interface are obtained from OWL. Methods associated with the classes derived from OWL are used to wrap GBMS<sup>r</sup>SM application-specific code.

Model graph components also reuse code. There are primarily two generalization classes 32 defined <sup>w</sup> <sup>x</sup> in the system: node and edge. The node generalization class had six specialization sub-classes: primitive entity, compound entity, attribute, function, test, and module. These specialization sub-classes inherit properties from the generalization class, node. The edge generalization class also has three specialization sub-classes: relation, value, and index. When a GBMS<sup>r</sup>SM model is constructed, node and edge class instance objects are created.

Graphical constructs such as node and edge class instance objects encapsulate certain properties. The generalization node class stores information common to all node types such as the node’s identification, name, screen x–y coordinates, etc. Specialization node sub-classes, in addition to inheriting properties from the generalization node class, have additional properties, such as the node symbol. Edge classes define relationships between a fromnode object representing the called node and a tonode object representing the calling node. Additionally, edge classes also define the name, type and associated expression for the edge.

The current implementation of GBMS<sup>r</sup>SM supports two solvers: the MEL expression evaluator and GAMS. In the case of MEL expression evaluator, the actual solver and its interface module are both combined into a single module. The MEL expression evaluator is invoked when optimization is not required for obtaining model solutions. In this case, values of all the attribute nodes are known and retrieved from source database tables. The values of function and test nodes are then computed using appropriate operators to obtain model solutions i.e.,Ž instantiations ..

The GAMS interface module is used when a model’s solution is required to be obtained via optimization using a GAMS solver. This module creates elemental detail tables, retrieves model instance data into these tables and then creates a GAMS input file. This file is used by a GAMS solver to obtain a model solution. The current implementation of this module does not launch the GAMS solver nor does it return solutions from the GAMS solver into elemental detail tables. These features can be easily incorporated with additional programming effort.

## 6. Conclusion

In this paper, a prototype of a graph-based modeling system for structured modeling is presented. This system called GBMS<sup>r</sup>SM, supports model formulation, maintenance and solution. GBMS<sup>r</sup>SM allows users to create models graphically with reduced textual input using a mouse and graphical tools such as a palette and a menu. GBMS<sup>r</sup>SM has links to databases and spreadsheets, and also supports solvers such as GAMS.

Major contributions of this paper are many folds. First, the implementation of the GBMS<sup>r</sup>SM prototype demonstrates the feasibility of the GBMS<sup>r</sup>SM approach that is worthy of a commercial application. This approach materializes a system that allows graphical inputs during model formulation, represents model schema using computationally active graphs, automates model instance data acquisition, and supports model formulation, maintenance and solution. Second, the GBMS<sup>r</sup>SM architecture provides a basis to integrate multiple solvers to a modeling system. Third, the implementation of GBMS<sup>r</sup>SM provides insights for developing a comprehensive graphical modeling system to support model construction, maintenance and solution.

Several challenges were encountered during the development of GBMS<sup>r</sup>SM. Developing a framework to support a graphical modeling system with the performance objectives outlined in Section 1 was the first challenge. Although structured modeling is used as the basis for GBMS<sup>r</sup>SM, it had to be extended in order to allow graphical inputs for model specifications.

Developing a modeling language that is 1 com- Ž . puter executable, 2 able to represent models in Ž . various domains, and 3 able to support expressions Ž . that directly reference relational database tables, was another challenge. The design and specifications of MEL provided a response to this challenge.

The ability to let users draw a graph in order to specify a model with minimum algebraic input is at the core of GBMS<sup>r</sup>SM. Accomplishing this was challenging. Although model graphs and the graphical user interface of GBMS<sup>r</sup>SM support this notion, eliminating algebraic input totally could not been achieved. Users still need to know MEL for the purposes of using the graphical primitives correctly, specifying filter clauses, and verifying the validity of the model expressions generated by the system. Therefore, MEL could not be totally ‘hidden’ from the user.

Developing a system that seamlessly integrates modules to support graph editing, model retrieval and storage, query capability, and interfaces to solvers had been a challenging task. The appropriate choice of the implementation platform and the use of an object-oriented approach provided a way to overcome this challenge.

GBMS<sup>r</sup>SM software and user manual 12 can be<sup>w</sup> <sup>x</sup> obtained for research purposes from the authors. Further details on model graphs and MEL can be found in Ref. 11 . Examples of model graph repre- <sup>w</sup> <sup>x</sup> sentations can also be found in Ref. 35 .<sup>w</sup> <sup>x</sup>

## Appendix A. Feed-mix model example

The feed-mix model is a popular linear programming problem. It involves determining the appropriate quantities of feed materials that contain nutri-Ž ents at lowest cost such that a daily nutrient require-. ment is satisfied. An algebraic representation of the feed-mix model is as follows:

$$
\begin{array}{l l} Z = & \text {Min} \sum_ {j \in J} C _ {j} Q _ {j} \\ & \sum_ {j \in J} A _ {i j} Q _ {j} \geq R _ {i} \quad \forall i \in I \\ & Q _ {j} \geq 0 \quad \forall j \in J \end{array}
$$

where J is the set of materials that contain nutrients.; I is the set of nutrients.; $C _ { j }$ is the unit cost of material $j \in J ; ~ Q _ { i }$ is the quantity of material j purchased.; $A _ { i j }$ is the amount of nutrient i contained in one unit of material $j . ; \ R _ { i }$ is the daily minimum requirement for nutrient i.

Node expressions in MEL for the model graph representation of the feed-mix model are given below in Table 1. It should be noted that in Table 1, the arguments in the expressions refer to source database tables beginning with ‘rŽ . \_’ , edge names and MEL expressions. Calling node expressions do not directly refer to the called nodes but instead refer to the edge names. Edge expressions, which are of the form: @SELECT<sup>-)</sup>Ž . fromnode in the feed-mix model, provide tuples associated with the elemental detail table of the called nodes i.e.,Ž . fromnode to the calling node i.e.,Ž . tonode .

## Acknowledgements

The authors are extremely grateful to Art Geoffrion for providing valuable comments during the course of this research. The authors would also like to thank the anonymous referees for their valued comments.

## References

<sup>w</sup> <sup>x</sup> 1 A.A. Angehrn, H. Luthi, Intelligent decision support systems: a visual interactive approach, Interfaces 20 6 1990Ž . Ž . 17–28.

<sup>w</sup> <sup>x</sup> 2 T.E. Baker, Graph-Based Modeling with MIMI<sup>r</sup>G, Chesapeake Decision Sciences, New Providence, NJ, 1992.

<sup>w</sup> <sup>x</sup> 3 A. Basu, R.W. Blanning, Metagraphs: a tool for modeling decision support systems, Manage. Sci. 40 12 1994 Ž . Ž . 1579–1600.

<sup>w</sup> <sup>x</sup> 4 H. Bhargava, S. Kimbrough, Model management: an embedded languages approach, Decision Support Syst. 10 1993 Ž . 277–299.

<sup>w</sup> <sup>x</sup>5 Borland International, C<sup>qq</sup> User’s Guide, Version 3.1, Scotts Valley, CA 95067-0001, 1992.

<sup>w</sup> <sup>x</sup> 6 Borland International, ObjectWindows for C<sup>qq</sup> User’s Guide, Scotts Valley, CA 95067-0001, 1991.

<sup>w</sup> <sup>x</sup> 7 Borland International, Borland Paradox Engine, Database Framework Reference, Version 3.0, Scotts Valley, CA 95067-0001, 1992.

<sup>w</sup> <sup>x</sup> 8 Borland International, Paradox for Windows, Version 4.5, Scotts Valley, CA 95067-0001.

<sup>w</sup> <sup>x</sup> 9 Borland International, Quattro Pro for Windows, Version 5.0, Scotts Valley, CA 95067-0001, 1993.

<sup>w</sup> <sup>x</sup> 10 A. Brooke, D. Kendrick, A. Meeraus, GAMS, A User’s Guide, The Scientific Press, Redwood City, CA, 1988.

<sup>w</sup> <sup>x</sup> 11 K. Chari, T.K. Sen, An integrated modeling system for structured modeling using model graphs, INFORMS J. Comput. 9 4 1997 397–416.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 K. Chari, T.K. Sen, GBMS<sup>r</sup>SM: User Manual and Tutorial, Department of Information and Decision Sciences, James Madison University, Harrisonburg, VA 22807, 1995.

<sup>w</sup> <sup>x</sup> 13 J. Choobineh, A diagramming technique for representation of linear models, OMEGA 19 1 1991 43–51.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 G. Collaud, J. Pasquier-Boltuck, gLPS: a graphical tool for the definition and manipulation of linear problems, Eur. J. Oper. Res. 72 2 1994 277–286. Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 D.R. Dolk, A generalized model management system for mathematical programming, ACM Trans. Math. Software 12 Ž . Ž .2 1986 92–126.

<sup>w</sup> <sup>x</sup> 16 R. Fourer, D.M. Gay, B.M. Kernighan, A modeling language for mathematical programming, Manage. Sci. 36 5 1990 Ž . Ž . 519–554.

<sup>w</sup> <sup>x</sup> 17 M. Gagliardi, C. Spera, BLOOMS: a prototype modeling language with object oriented features, Decision Support Syst. 19 1 1997 1–21.Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 M. Gagliardi, C. Spera, MODASS: A Modeling System to Manage Structured Models, Proceedings of the First IN-FORMS Conference on Information Systems and Technology, Washington, DC, May 5–8, 1996, pp. 80–89.

<sup>w</sup> <sup>x</sup> 19 A.M. Geoffrion, An introduction to structured modeling, Manage. Sci. 33 1987 547–588.Ž .

<sup>w</sup> <sup>x</sup> 20 A.M. Geoffrion, FW<sup>r</sup>SM: a prototype structured modeling environment, Manage. Sci. 37 1991 1513–1538.Ž .

<sup>w</sup> <sup>x</sup> 21 A.M. Geoffrion, The SML language for structured modeling: levels 1 and 2, Oper. Res. 40 1 1992 38–57.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 A.M. Geoffrion, The SML language for structured modeling: levels 3 and 4, Oper. Res. 40 1 1992 58–75. Ž . Ž .

23 H.J. Greenberg, A Primer for MODLER, Mathematics Department, University of Colorado, Denver, CO, 1990.

<sup>w</sup> <sup>x</sup> 24 S. Hamacher, P. Dejax, L. Lustosa, P. Hamacher, A Diagram Representation for Conceptual Models of Operations Research Problems, Cahiers d’ Etudes et de Recherche No. 93-04A, Laboratoire Productique Logistique, Ecole Centrale Paris, France.

<sup>w</sup> <sup>x</sup> 25 T. Huerlimann, Reference Manual for the LPL Modeling Language, Version 3.9, Institute of Informatics, Working Paper No. 94-06, University of Fribourg, Fribourg, Switzerland, 1994.

<sup>w</sup> <sup>x</sup> 26 C.V. Jones, An introduction to graph based modeling systems: Part I. Overview, ORSA J. Comput. 2 2 1990Ž . Ž . 136–151.

<sup>w</sup> <sup>x</sup> 27 C.V. Jones, An introduction to graph based modeling systems: Part II. Graph grammars and the implementation, ORSA J. Comput. 3 3 1991 180–206.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 C.V. Jones, Attributed graphs, graph grammars, and structured modeling, Ann. Oper. Res. 38 1992 281–324.Ž .

<sup>w</sup> <sup>x</sup> 29 R. Krishnan, A logic modeling language for automated model construction, Decision Support Syst. 6 1990 123–152.Ž .

<sup>w</sup> <sup>x</sup> 30 M. Lenard, An object-oriented approach to model management, Proceedings Twentieth Hawaii International Conference on System Sciences, Vol. 1, 1987, pp. 509–515.

<sup>w</sup> <sup>x</sup> 31 P. Ma, F.H. Murphy, E.A. Stohr, An implementation of LPFORM, INFORMS J. Comput. 8 4 1996 383–401.Ž . Ž .

<sup>w</sup> <sup>x</sup> 32 R. Mattison, M.J. Sipolt, The Object-Oriented Enterprise, McGraw-Hill, New York, 1994.

<sup>w</sup> <sup>x</sup> 33 W. Muhanna, SYMMS: A model management system that supports model reuse, sharing, and integration, Eur. J. Oper. Res. 72 2 1994 214–242.Ž . Ž .

34 L. Neustadter, A. Geoffrion, S. Maturana, Y. Tsai, F. Vicuna, The design and implementation of a prototype structured modeling environment, Ann. Oper. Res. 38 1992Ž . 453–484.

<sup>w</sup> <sup>x</sup> 35 T.K. Sen, K. Chari, A graphical modeling system: applications in organizational model management, OMEGA 25 2Ž . Ž . 1997 241–253.

36 D.M. Steiger, R. Sharda, B. LeClaire, Graphical interface for network modeling: a model management perspective, ORSA J. Comput. 5 3 1993 275–291.Ž . Ž .

<sup>w</sup> <sup>x</sup> 37 J.S. Welch, PAM—a practitioner’s approach to modeling, Manage. Sci. 33 5 1987 610–625.Ž . Ž .

<sup>w</sup> <sup>x</sup> 38 G.K. Yeo, J. Hu, VMS<sup>r</sup>SM, A two-tiered visual modeling system, Working Paper No. TR 21<sup>r</sup>96, The National University of Singapore, 1996.

![](/api/attachments/ZYEYFCVY/fulltext/images/6261b00fa8984347d0745180c5bbd70f2447fa926cbea10f770167779567906f.jpg)

Tarun K. Sen is an Associate Professor of Accounting Information Systems at the Pamplin College of Business in Virginia Tech. He received his PhD in MIS from the University of Iowa in 1985. His teaching and research interests are in database management systems, model management systems, neural network applications in financial prediction tasks and building decision support systems using data warehouses. His articles have appeared in Management Science, IN-

FORMS Journal on Computing, Omega, IEEE Transactions on Systems Man and Cybernetics, and International Journal of Intelligent Systems in Accounting Finance and Management.

![](/api/attachments/ZYEYFCVY/fulltext/images/2c5baf698050b18c210c5072c47a30e8477b96d68da88550a8734f89753fb067.jpg)

Kaushal Chari is currently an Associate Professor of Computer Information systems at James Madison University, VA. He obtained a B. Tech. in Mechanical Engineering from the Indian Institute of Technology Kanpur, followed by an MBA and PhD from the University of Iowa. His research has been published in journals such as INFORMS Journal on Computing, Telecommunication Systems, European Journal of Operational Research, Computers and Operations

Research and Omega. His research interests include telecommunications network design, model management systems, software agents and intelligent systems.
