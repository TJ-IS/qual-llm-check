---
otero_id: 17354
otero_key: "GDNXUXY6"
title: "Direct manipulation of graph-based decision models"
authors: "Ronald M. Lee"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90049-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Direct manipulation of graph-based decision models

Ronald M. Lee \*

Erasmus University, Rotterdam, The Netherlands

This paper builds on a long tradition in operations research and systems analysis: building models by drawing pictures. While pictorial representations are certainly useful as a communication medium, we focus on the learnability of modeling applications through graphical interfaces. Using the combined perspectives of direct perception (especially affordances) and direct manipulation, we focus on the dynamics of model building and model manipulation. The GX Shell is a DSS interface generator for direct manipulation of graph-based decision models, which are processed either by routines coded in Prolog or by external solvers.

Keywords: Direct perception, Affordances, Direct manipulation, Graph editors, Graph-based modeling systems.

![](/api/attachments/GDNXUXY6/fulltext/images/4f4da2793c1b8afbe5dd829c0e820c589b07fc8babe88650a9b25abb9580259b.jpg)

Ronald M. Lee is currently Director of the EURIDIS Institute of Erasmus University in the Netherlands, as well as Associate Professor of Information Systems at the Management Science and Information Systems Department at the University of Texas at Austin. He has a Ph.D. in Decision Sciences (Wharton, 1980), and has previously served as a research scholar at the International Institute for Applied Systems Analysis in Vienna and as Visiting Professor of Management at the Universidade Nova de Lisboa, in Lisbon. Current research focuses on applications of artificial intelligence to business; special focus is 'logic modeling', the use of formal logic representations for management science applications; current projects involve the use of logic modeling to represent and manage formal business communications systems focusing on (a) bureaucratic systems (formalized communications within institutions) and (b) electronic contracting systems (formalized communications between enterprises). Theoretical aspects include the role of deontic and illocutionary logic in representing formal business conversations. Practical value is the reduction of bureaucratic and legalistic red tape. This work also includes multilingual business communications, supporting structured communications between parties with different native languages.

\* Sincere thanks to James Baty and Sandra Dewitz for their editorial comments and suggestions, and to Leena Kudva and Candace Wilrich for their assistance in developing GX applications.

Correspondence to: R.M. Lee, EURIDIS Institute, Erasmus University, P.O. Box 1738, 3000 DR Rotterdam, the Netherlands (leer@tac.fbK.eur.nl).

## 1. Introduction

A decision support system (DSS) provides computational support to facilitate the decision-making processes of its users. For example, a DSS may provide easy, quick access to computational resources such as decision models and data bases. This function is an example of mechanical accessibility, which is achieved when a DSS makes it easy for users to identify data and models relevant to their problem and to quickly retrieve these from a number of sources. A second type of accessibility, conceptual accessibility, is achieved when a DSS makes it easy for a user to manipulate complex models and ideas by converting between the users' perhaps more intuitive representations and the formal representations of decision models and data bases.

Conceptual accessibility has two aspects: semantic and syntactic. The analytical disciplines contributing to DSS – operations research (OR), artificial intelligence (AI), and logic – emphasize the semantic aspect of representations, focusing on the mapping between the user's conceptual structure of the problem and the formal structure used for analyzing it. For example, in OR the items of a dinner menu may be mapped to the equational structure of a knapsack problem (e.g. to optimize nutrition); in AI this same menu might be represented as a frame (e.g. to recognize styles of cuisine); in logic it might be represented as a set of predicate assertions (e.g. for an expert database system on meal selection). However, the surface syntax of the user interface – whether the user types into a text window, uses pull-down menus, or points to actual images of food items – is usually regarded as outside the concerns of these areas.

But surface syntax can significantly affect conceptual accessibility. For example, consider arithmetic. Using the surface syntax of Roman numerals, operations such as multiplication and division are quite difficult. Using Arabic numerals, however, these become much easier. This is not simply due to the introduction of the concept of zero, but also due to the notation itself: our manual algorithms for arithmetic involve manipulating the notation (e.g. carrying a one to the ten's column) in a way that is not possible with Roman numerals.

In this paper we address the conceptual accessibility of decision models in a DSS, focusing on the presentation and manipulation of their surface syntax. The class of models we consider are those that are graph-based, representable as nodes and arcs. A language and prototype implementation, called GX, is presented for creating interactive graphical interfaces to such models. The subsequent sections are organized as follows.

Section 2 discusses theories of perception and the relationships between users' perceptions and goals, while section 3 relates these theories to the requirements and benefits of direct manipulation interfaces. Section 4 applies the concepts of direct perception and direct manipulation to graph-based decision models. In section 5, the GX shell, a DSS interface generator, is described and its support of direct manipulation of graph-based decision models is discussed. Section 6 presents a series of applications using the GX shell, while section 7 summarizes our experience to date based on user feedback. Section 8 presents a brief review of other graphical interface generators for DSS, and section 9 is concluding remarks.

## 2. Direct perception

Conventional theories of perception, based on the information processing metaphor, treat human perception as the process of accepting bit-level sensory data as input (i.e., in the form of static snapshots) and then converting these data into meaningful chunks by cognitive computation. Gregory (1978) describes this theory of perception: "We are given tiny distorted up-side-down images in the eyes, and we see separate solid objects in surrounding space. From the pattern of stimulation in the retinas, we perceive the world of objects, and this is nothing short of a miracle". In contrast to this conventional theory of perception, an emerging theory, direct perception, treats recognition of meaningful patterns as occurring as a low-level, not a high-level, cognition.

Representative of direct perception theory are Michaels and Carello, who describe perception in the following manner: “Through the course of evolution, the anatomy and physiology of the animal became tailored to information as much as they became tailored to the more obvious aspects of the environment” (Michaels and Carello, 1981, p.45). For example, a fish is capable of depth perception under water in a way that humans are not. Winograd and Flores (Ch. 4, 1986) have a similar perspective. Citing the work of Maturana, et al (1960), they point out how the eye of a frog has evolved to be especially responsive to small dark spots surrounded by light, an appropriate feature for catching insects.

Direct perception emphasizes the environmental conditioning of perceptual patterns in two fundamental ways: (1) phylogeny, the genetic evolution of certain survival-related perceptual behaviors in a species, and (2) ontogeny, the conditioning of certain perceptual behaviors through experience. Unlike the conventional, information processing theory of perception, direct perception posits an intimate relationship between perception and action. Perception is not a series of independent snapshots, but is integrated with the activity being performed as the perception occurs. Central to this theory is the work of the psychologist Gibson (1979). To unify the notions of perception and action, he introduces the concept of an affordance: "The affordances of the environment are what it offers animals, what it provides or furnishes, either for good or ill". Perception is thus tied to the acts or behaviors permitted – "afforded" – by the objects, places, and events encountered by the organism. To Gibson, affordances are instrumental, we perceive those aspects of the environment that are most relevant to our goals of achievement or avoidance. Thus, babies learn that a glowing stove may afford it pain, that a bottle affords milk to drink, crying affords attention, etc. Similarly, when shopping (especially at Christmas) we are bombarded with information about the affordances of each manufacturer's new creations. Yet we ignore most of this information, attending to that information relevant to our purchase objectives.

Gibson uses the term resonance to describe the efficient interaction of the organism with its environment. This has two aspects, one selective, the other synchronic. The selective aspect is like a radio tuned to a particular frequency – its speakers resonate to the signals to a particular station, ignoring all others. The synchronic aspect emphasizes how the organism synchronizes its behavior with the environment. Consider riding a bicycle – one becomes selectively attuned to obstructions in the road surface, nearby traffic movement, etc. Also, their is a clear sense of synchronization between the actions of pedaling, shifting, braking, leaning on curves, all in intimate response to the environment.

The notions of affordance and resonance take on practical value in the design of tools. A tool is an artifact whose affordances are specifically designed for a particular task. A good tool is one that achieves resonance. For instance, a carpenter's claw hammer is designed with a certain weight and balance for pounding nails. If the nail bends, the claws of the hammer can be used to straighten it. If later the nail has to be removed, the claws of the hammer can be used to extract it. The hammer can also be used to tap a board lightly, to adjust its position, or to smash the board into pieces (if the board has to be removed, or if the carpenter becomes extremely frustrated).

The hammer is thus a multi-purpose tool. Other tools are more specific, for instance a “cat’s claw” – a ten inch long steel rod with claws like a hammer, but shorter and curved, and with a sharpened edge to the claws. The cat’s claw is used for extracting nails that are sunk below the wood surface. One uses a hammer to pound the claws down into the wood around the nail, enabling one to raise the nail high enough to be extracted by an ordinary hammer. The hammer and the cat’s claw thus illustrate differences in the versatility of tools – some, like the hammer, have a variety of uses; others, like the cat’s claw, have a specific and limited use. Both however are good tools in that they provide useful affordances.

The hammer and cat's claw also illustrate how tools and their affordances may interact. The cat's claw is almost useless without a hammer to pound it in. Similarly, a carpenter's square is typically used with a pencil to draw a line; a sawhorse is used to hold a board while sawing, etc. Indeed, mastery of these tools involves not only understanding their separate affordances, but in being able to integrate these affordances effectively to achieve resonance to the task of building.

## 3. Direct manipulation

"My favorite example of direct manipulation is driving an automobile. The scene is directly visible through the front window... To turn left, the driver simply rotates the steering wheel to the left. The response is immediate and the scene changes, providing feedback to refine the turn. Imagine trying to turn by issuing a command LEFT 30 DEGREES and then having to issue another command to see the new scene: but this is the level of operation of many office automation tools of today". (Schneiderman, 1987, pp. 180–181)

We now apply these notions of direct perception, affordances and resonance to the design of decision support tools. Unlike the carpenter, who achieves mastery over his/her tools through long experience, the manager using a DSS is likely to use it only intermittently, and even then in quite different ways, for a variety of problems and applications. A key issue, therefore, is ease of learning, being able to achieve resonance to a particular problem domain with a minimum of preparation and training. Addressing this issue, Schneiderman (1983, 1987), distinguishes a particular interface design philosophy he calls direct manipulation, which he characterizes as providing (1987, p. 201):

continuous representation of the object and actions of interest

physical actions or labeled button presses instead of complex syntax

rapid, incremental, reversible operations whose impact on the object of interest is immediately visible

Direct manipulation describes those features of an interface that allow the user to create and manipulate graphical objects and to perform actions on them that will be understood by the system. Essentially, direct manipulation uses a visual metaphor to represent a problem domain, thereby improving the ease with which users understand the system and sparing the users the burdensome task of memorizing an unintuitive command syntax.

According to Schneiderman, (1987, pp. 201–202) the benefits of direct manipulation systems are:

novices can learn basic functionality quickly, usually through a demonstration by a more experienced user;

experts can work rapidly to carry out a wide range of tasks, even defining new functions and features;

knowledgeable, intermittent users can retain operational concepts;

error messages are rarely needed;

users can immediately see if their actions are furthering their goals, and, if not, they can simply change the direction of their activity;

users experience less anxiety because the system is comprehensible and because actions are so easily reversible; and

users gain confidence and mastery because they are the initiators of action, they feel in control, and the system responses are predictable.

Elaborating on the concept of direct manipulation, Hutchins, Hollan and Norman (1986) contrast two principal styles or ‘metaphors’ of human-computer interaction. In the first style, called the ‘conversation metaphor’, human-computer interaction is treated as a dialogue in which the user converses with the computer via textual input and output (possibly including menus, dialogue boxes). In this style of interaction there is an assumed, but not explicitly represented world in which the conversation occurs. In contrast, the ‘model world metaphor’ treats the interface as a view of the problem domain shared by user and computer. A key concept in the model world metaphor is what Draper (1986) calls “inter-referential input/output” – that the same representational object is used as both an input and an output entity. This usually presupposes that the model world be presented visually and continuously, and that one can easily navigate within this visual representation using e.g. cursor controls or a mouse.

Direct manipulation of a model world has disadvantages as well as advantages. A principal disadvantage is that certain features of the problem or actions upon it may be difficult to represent in visual or iconic form. Another disadvantage is that the visual field is limited by screen size, limiting the complexity of what can be continuously presented.

Where these disadvantages can be overcome, there are distinct advantages in the ease by which a novice user can learn and become familiar with the model and how to manipulate it. This comes primarily through the principal of immediate and reversible feedback: one can try certain operations and see their effect, whereas with conversation style interfaces, where the model is hidden from view, one has to make explicit queries of the system to verify that what has occurred is actually what was expected. $^{1}$ In addition to these features, Hutchins, Hollan and Norman (1986) suggest that direct manipulation of a model world is also more intuitive, creating “a feeling of involvement directly with a world of objects rather than of communicating with an intermediary” because the output language presents representations of objects in forms that behave in the way that the user thinks of them behaving and that changes caused in the objects by the set of operations are depicted in the representation of the objects.

Software implementations that utilize direct manipulation can be divided into two subcategories: those that manipulate a visual image whose function is for display purposes only, and those where the visual image is actually understood by the system as constituting a model of some problem domain.

In the display manipulation systems, the shared “world” is an uninterpreted text or graphic image. For example, “WYSIWYG” (“What you see is what you get”) text editors immediately display the results of user actions, which are performed e.g., a mouse to move the cursor or to select text. Other examples of display manipulation systems are graphic systems such as MacDraw and MacPaint. These systems use visual metaphors such as a palette from which the user can select a color or design. The user chooses a tool (visually represented in the margin) and uses a mouse to draw shapes on the screen, which uses the visual metaphor of a sheet of graph paper to help the user perceive the spatial dimensions of the system world.

With model manipulation systems, by contrast, the visual image has further significance to the system. For example, the Macintosh (or MS Windows) Operating System allows the user to manipulate file icons with a mouse in order to open, close, copy, and delete files. Similarly, Hypercard allows the developer to create interactive 'notecards' and to use the mouse to position labels, edit fields, and activate buttons. Hypertext/Hypermedia systems (Conklin, 1987) create a screen-based world in which the user can navigate 'hyperspace' to retrieve information. (In these later examples it is primarily the developer or 'authoring' interface that has model manipulation features; the end user interface is primarily navigation and retrieval.)

The above remarks refer to the interface characteristics of a single program. With respect to learnability, one is also concerned with the interface similarities among a class of programs. For example, a frequently argued advantage of the Macintosh is the consistency of its interface across applications. (This applies both to conversational, command driven interfaces, as well as graphical, direct manipulation interfaces.) Even though these interfaces are not always as consistent as the advertising claims, the similarities are on the whole, quite useful. Perhaps a weaker concept, call it familiarity, is more appropriate.

Consider the automobile metaphor once again. The driver interface between the various makes and models is familiar, though not absolutely consistent. For instance, the controls for lights, radio or windshield wipers may be quite different from one car to another. On the other hand, the operation of these aspects can be quite easily learned through experimentation. The effect of a mistake for these aspects of the vehicle operation is small and easily reversible. However, fundamental functions, like steering, acceleration and braking, where mistakes may have drastic and irreversible consequences, are much more rigorously standardized. The auto rental industry relies on these learnability characteristics: seldom is a client given any operational training.

Again referring to the Macintosh, nearly every application has a FILE and and EDIT menu. These are not necessarily consistent in every application, but they are familiar. For instance, the

FILE menu may have options for loading different file types. Similarly, the COPY, CUT and PASTE commands of the EDIT menu may do slightly different things, say between document text, program text, and graphic images. However, the UNDO command of this menu, which reverses the effect of the previous editing action, allows rapid experimentation and adjustment to the differences.

## 4. Direct manipulation of graph models

Direct manipulation seems will suited to the decision support requirements of managers, who typically

use DSS intermittently,

do not like complicated syntax,

have strong domain knowledge, but may be unfamiliar with formal modeling representations.

These characteristics suggest that managers could benefit from the short learning curve and intuitive appeal of using a direct manipulation system to formulate problems, query models, and display results. Here we focus on the design of direct manipulation interfaces for graph-based decision models. These models generally employ “attributed” graphs (Jones, 1990a), with nodes representing entities or states and the arcs representing binary connections between them. Both nodes and arcs may be of multiple types and may have any number of associated attributes.

Graphical models can be used in several metaphors. One of the most common metaphors treats a graph as a geographical abstraction, e.g., a road map. This metaphor is especially useful in OR problems dealing with transportation, transshipment, and factory production. Another common metaphor treats a graph as a temporal abstraction, e.g., some variant of a time line, such as decision trees, PERT diagrams, Petri nets, and program/system flowcharts. Graphs can also be used effectively to represent physical connections, such as in circuit diagrams and data structure diagrams. Finally, graphs are also commonly used as a metaphor of logical relationships, such as those represented in semantic nets and logic graphs.

Typically, the most appropriate applications of graphical modeling are those which meet the following criteria:

The model can be characterized as an attributed graph, consisting of nodes and node attributes and arcs and arc attributes.

The graphical notation is significantly easier to comprehend than the syntax of the solution algorithm.

The graph has typing of nodes/arcs that ensure the grammatical correctness of the model.

Domain dependent notations are possible.

There is significant interaction with the graphical model, e.g., changing parameters and changing graphical structure.

## 5. The GX shell

The GX Shell is a specification language for generating direct manipulation interfaces for graph-based decision models. These decision models can be formulated and queried and their results displayed in graphical form. The actual processing of the model can be completed by algorithms coded in Prolog or by external solvers.

The visual vocabulary of GX consists of node shapes – circle, box, bar, icons, and user defined graphical shapes – and arc styles – line width and pattern. Planned but not yet implemented aspects of the visual vocabulary include regions and background images (e.g., geographical map in which distance is meaningful). Users perform actions with this visual vocabulary by using the mouse to point: e.g., to place a node, to draw an arc, and to select a subgraph. Users may also interact with the system through menus for commands, and dialogue boxes, which request input from the user (e.g. node and arc attributes). The primary forms of graphical output include highlighted nodes (to identify e.g., bottlenecks in a Petri net), highlighted arcs (to identify e.g. the shortest path on a PERT graph), and animation (e.g. iteratively redrawing nodes or connecting arcs between nodes).

The system performs syntax checking as the user builds a graph, displaying error messages if the user attempts to use the visual vocabulary incorrectly. For example, at the local level, the system checks the node types at each end of arc to determine than they are compatible; at the global level, the system may check the properties of the entire graph, e.g., testing for cycles. $^{2}$

Since GX is an interface generator, we need to describe two kinds of interface: one, the specification language used by the developer, and two, the resulting graphical interface for the end user.

The GX specification language consists of declarations and commands. Declarations provide the notations for defining the nodes, links, and tools of the system. The various node types are defined in the following notation:

nodetype(⟨shape⟩,⟨chr⟩,⟨nodetype⟩,⟨att-list⟩).

where,

$\langle \mathrm{shape}\rangle =$ name of the pictorial shape of the node

$\langle chr\rangle = a single character used to generate sequentially numbered node labels$

$\langle$ nodetype $\rangle$ = name for the type of the node in the model (this will be the predicate name for the node assertions generated)

$\langle \mathrm{att - list}\rangle =$ a list of the names of the attributes associated with the node

Link types are defined by declarations of the form:

type>,<att-list>).

where,

$\langle linktype\rangle = name$ for the type of the arc in the model (this will be the predicate name for the arc assertions generated)

$\langle$ from-nodetype $\rangle =$ type of node at the origin of the arc

$\langle \text{to-nodetype} \rangle = \text{type of node at the target of the arc}$

$\langle \mathrm{att - list}\rangle =$ a list of the names of the attributes associated with the arc

Query tools are defined by

query(<call-term>,<tool-shape>)
where,
<call-term> = the Prolog predicate to be executed
when this tool is used
<tool-shape> = pictorial shape for this tool

![](/api/attachments/GDNXUXY6/fulltext/images/886bdc3f840d05eba60bf00f12c74489b5406ccc6321f15bf40fe62db1f668e3.jpg)

and specially defined shapes can be defined using the following notation:

```txt
shape-def(〈shape〉,〈tool-shape〉).
where,
〈shape〉 = name of a shape to be drawn
〈tool-shape〉 = shape of the symbol for the tool in the palette
```

GX commands are calls from Prolog that request the system to perform certain actions: e.g.,

```txt
hilite_nodelangle node-namerangle)
unlite_node(⟨node-name⟩)
hilite_link(⟨link-name⟩)
unlite_link(⟨link-name⟩)
redraw_node(⟨node-name⟩, ⟨shape⟩
where,
<node-name> = system generated identifier for a particular node
<link-name> = system generated identifier for a particular arc
<shape> = name of a shape to be drawn
```

In addition, there are various declarations to indicate how attribute values are to be elicited from the user:

```typescript
label<att-name>:'<prompt Sport'.
numeric<att-name>:'<prompt Sport'.
fact<att-name>:'<prompt Sport'.
category<att-name>:'<prompt Sport>:<list-of-choices>
where,
<att-name> = name of the attribute
<prompt> = a text string used to prompt the user
<list-of-choices> = a list of alternatives
```

![](/api/attachments/GDNXUXY6/fulltext/images/daf56c7f637db1d36992f1ed6332332741be65b834462c2dc42bef0f4775e6a9.jpg)  
Fig. 1. Sample graph window.

Attributes of type label have values that are an arbitrary string, e.g. the name of a city. Attributes of type numeric must have numeric values. Attributes of type fact have the values yes or no (a two-button dialog box), while category attributes require the user to choose from a menu of values.

The kind of interface generated by these specifications has a general appearance as shown in fig. 1.

The window is divided into three parts. The right hand area is the drawing area where the user draws the graph model. (This model can be saved/retrieved at any time through a menu command.) The lower left hand areas is the 'viewer' for repositioning the drawing area. Thus, the actual graph can be much larger than what is visible in the drawing area. The upper left hand area is the drawing palette, which contains the tools for drawing the graph.

![](/api/attachments/GDNXUXY6/fulltext/images/215e65cff489d425973522fbb145f8c744695e37f47bb43055e9d67971f87a55.jpg)

the select tool, used to select graphical elements for further manipulation, e.g. repositioning them.

the label tool, used for writing (uninterpreted) labels to the graph

the information tool; by selecting this tool, and clicking on another tool, the user is given help information about that tool. Similarly, by clicking on elements in the graph itself, information is also provided about them.

the eraser tool, used to delete graphical elements

the attribute tool, used to modify the value of an attribute (the user is prompted for the values of attributes to nodes or links as they are added to the graph)

Fig. 2.

![](/api/attachments/GDNXUXY6/fulltext/images/49c92dca5c6507259358e9dd93a71e05dde310b7cf3b8b55cdd63a551b7b6ba5.jpg)  
Fig. 3. GX interface for PERT graph (user is using 'select' tool to reposition node x1 by dragging it).

In an effort to obtain consistency, or at least familiarity, between GX applications, the following tools are standard to all GX interfaces (see fig. 2).

## 6. GX applications

This section presents several sample applications of the GX DSS interface generator in order to illustrate the types of affordances and the degree of direct manipulation GX's visual vocabulary can support.

## 6.1. PERT graphs

A common decision support application is a PERT graph, which consists of a single node type, drawn in GX as a box, and a single directed arc type. Nodes in PERT graphs do not have attributes; however, arcs are labeled with the name of the activity represented and the duration of that activity. Queries to this model generally request the shortest or longest path through the

![](/api/attachments/GDNXUXY6/fulltext/images/0f0bc27b13738086032932e162406e47fb10a80375048b9752b4d7de03b291d3.jpg)  
Fig. 4.

the node tool, for inserting nodes

the link tool, for inserting links (arcs) between nodes

the query tool, for specifying a PERT analysis between two specified nodes.

PERT graph. These queries require the user to specify a starting node and an ending node. The graphical interface requirements are the following:

1. Formulate the Model:

\- draw nodes and arcs

\- add attribute information

2. Query the Model:

\- select starting and ending nodes

3. Present the Results:

\- highlight the (shortest, longest) path

\- display numeric results in the results window

The GX specification for this interface is as follows:

/\*PERT.GX\*/

/\*query tools\*/

query(go(\_, \_), qpath).

/\*parameters\*/

label act\_name:'Name for this activity':

numberic time: 'What is duration?'.

/\*declarations\*/

nodetype(square,x,substrate,[]).

linktype(activity,substate,substate,[act\_name,

time]).

The screenshot in fig. 3 illustrates how a PERT problem is drawn using this interface. In addition to the standard tools, three other tools are included that are specific to this interface (see fig. 4).

Fig. 5 illustrates a completed design for a PERT problem and shows how the query tool is used to select the starting and ending nodes. Fig. 6 shows the graphical results of this query. Note that the critical path has been highlighted and that early and late times have been added to the nodes.

![](/api/attachments/GDNXUXY6/fulltext/images/511482a7308887eeab23aa1bc28d230bedf8ad31f7171d0dc1477a85773afbc3.jpg)  
Fig. 5. Completed PERT graph (user has used the Query tool to specify a search from x0 to x3, shown as a dotted line).

## 6.2. Decision trees

Another common type of graph-based decision model is a decision tree. Decision trees are usually conceptualized as having two types of nodes, choice nodes, drawn as boxes and used to indicate a choice by the decision maker, and outcome or 'branch' nodes, drawn as circles and used to indicate probabilistic outcomes. To terminate the graph, we will introduce a third type of node, a result node, which will also be drawn as a box. Result nodes will have two attributes, a description of the result and the amount of the return received.

The links of the decision tree graph are of two types. The first, called xtrans, connects a choice node to a branch node and has two attributes: the name of the action taken and its cost. The second type of link, called ptrans, connects a branchnode to either a choicenode or a resultnode and also has two attributes: the name of the outcome and its probability. The graphical interface requirements for decision trees are as follows:

1. Formulate the Model

\- draw nodes and arcs

\- add attribute information

2. Query the Model

\- select starting choice node

![](/api/attachments/GDNXUXY6/fulltext/images/1cfc4c8100cec1b8e6b1e2a912325ff3c9748e67fb3f90a3982bdf7cc27aabd2.jpg)  
Fig. 6. Results of Query to PERT (critical path is highlighted).

Fig. 7.  
![](/api/attachments/GDNXUXY6/fulltext/images/4ddb97585479d8a69be2646fa896039035c4c6c9fe7a09c91c4e9ca9a564f9a2.jpg)

![](/api/attachments/GDNXUXY6/fulltext/images/796f49e6e632b08d181fd1d57da1fcc22628b4a5aac24d35babec69e04b1c4cd.jpg)

for choice nodes

![](/api/attachments/GDNXUXY6/fulltext/images/65929ea466973bbb2f320bfb727ca0975b65df4aa49911d2b47e4d0842f5b467.jpg)

for result nodes

for branch (outcome) nodes

for links (either xtrans or ptrans)

![](/api/attachments/GDNXUXY6/fulltext/images/40719ca5c022fe0e9bcc32ad013b5f946a7ce2dc513da779bd03dee44a5247f2.jpg)

to execute a query; when the user selects this tool and clicks on a node, e.g. c1, the routine decide(Node) is called and the graph results are reported.

3. Present the Results

\- highlight the decision path

\- print the numeric result, i.e., the total expected value

The graphical interface specifications for this model are as follows:

/\*DTree.GX\*/

/\*declarations\*/

query(decide(\_, qnode).

nodetype(square,c,choicenode,[]).

nodetype(square,r,resultnode,[result\_name, return]).

nodetype(circle,x,branchnode,[]).

linktype(xtrans,choicenode,branchnode,[action, cost]).

linktype(ptrans,branchnode,choicenode,[outcome, probability]).

linktype(ptrans,branchnode,resultnode,[outcome, probability]).

/\*parameters\*/

label action: 'What action is taken?'.

numeric cost: 'What is cost of this action?'.

label outcome: 'Which outcome?'.

numeric probability: 'What is probability of this outcome?'.

label result\_name:'What kind of result?'.

numeric return: 'What is the return?'.

The application specific tools in this palette are the following (see fig. 7).

An example decision tree drawn using this interface is shown in fig. 8.

![](/api/attachments/GDNXUXY6/fulltext/images/648e2ddc98332f45f26128bf417052c129468f6962b86195979701e1f7755ca5.jpg)  
Fig. 8. Completed decision tree with results of query (subgraph for recommended decision is highlighted).

![](/api/attachments/GDNXUXY6/fulltext/images/7ce60dabcd6b9721873010fba0f3bc813798daf0a2148a7179cb189c2ad9a68a.jpg)  
Fig. 9. Completed Petri net.

## 6.3. Petri nets

Petri nets, another type of bi-partite graph, have two node types: place nodes, which are drawn as circles, and transition nodes, which are drawn as vertical bars. When a Petri net is executed, tokens are moved between places. Specifically, when a transition 'fires', tokens are removed from its input places, and added to its output places. Thus, unlike the previous two applications, where the execution was a single analysis, here the execution is more like a simulation, showing the change in markings at each step.

The GX interface specifications for a Petri net model are as follows:

/\*Petri.GX\*/

/\*graph interface declarations\*/
query(go,'\*').

nodetype(empty\_place,s,place\_node,[]).

nodetype(bar,t,trans\_node,[]).

linktype(transin,place\_node,trans\_node,[],).
linktype(transout,trans\_node,place\_node,[],).

![](/api/attachments/GDNXUXY6/fulltext/images/1e053a6dd7308fe8dc64c7ad1a09d49f5dee94cb82c5d77de7c96f34fe0b0178.jpg)  
Fig. 10. A step in the execution of the Petri net.

```txt
machine(m2,mbusy) = 6.2
```

linktype(placeplace, place\_node, place\_node, []) shape\_def(empty\_place, circle).

Here, a new command, called shape\_def, appears. This command is used when specially defined shapes are given for the nodes. In this specification, an empty place node is assigned the shape of a circle. In this example, however, we go beyond the predefined shapes of circles and boxes and introduce customized shapes, in order to draw marked or 'filled' place nodes. These shapes are made possible by a special shape editor, which presents an interface much like the main graph editor, but which is used to define special node shapes (it is thus an example of display manipulation rather than model manipulation). An example of a Petri net specification is shown in fig. 9.

After this graph is executed, place markings will appear as heavy circles in the places, as shown in fig. 10.

## 6.4. Simulation

The limited animation capabilities used for Petri nets can be used more generally to provide simulations that have graphical characteristics customized to the problem domain. For example, the following GX specification defines the interface for a robotic queueing system consisting of waiting-to-process places (intray), processing places (machine), and waiting-to-load places (out-tray):

/\*Robot.GX\*/

/\*graph interface declarations\*/

query(go,'\*').

query(set(\_), '@').

nodetype(ipend\_arrive,i,intray,[inter\_arr\_time]).

nodetype(mwait\_load,m,machine,[process\_

nodetype(owait\_load,o,outtray,[inter\_dep\_time]).

linktype(onload,intray,machine,[]).

linktype(transfer,machine,machine,[]).

linktype(offload,machine,outtray,]).

shape\_def(ipend\_arrive,icon(17149)).

shape\_def(mwait\_load,icon(4242)).

shape\_def(owait\_load,icon(25119)).

numeric process\_time:'Mean process time?'.

numeric inter\_arr\_time: 'Mean inter-arrival time?'.

numeric inter\_dep\_time: 'Mean inter-departure time?'.

![](/api/attachments/GDNXUXY6/fulltext/images/e1d926829d1d35f41224a567126e2c4bb481b7723d59efe2de26d6b84a0527d4.jpg)  
Fig. 11. Simulation graph.

In this specification, shape \_def is used to define the shape of the three types of nodes in the simulation: e.g., icon(17149) is the intray node shape. A sample formulation of this simulation structure includes two input trays and three machines in parallel. The simulation graph is shown in fig. 11.

After the user gives the go command (either as a menu command, or as tool in the palette), the simulation shows the flow of jobs through the network. A sample snapshot of the state of the network part way through the execution is shown in fig. 12.

The ongoing numeric results are simultaneously displayed in the results :

Time = 6.2

intray(i1,ipend\_arrive) = 4.634

intray(i1,iwait\_unload) = 1.566

```txt
intray(i2,ipend_arrive) = 3.89
```

```txt
intray(i2,iwait_unload) = 2.31
```

machine(m1,mbusy) = 6.2

machine(m3,mbusy) = 3.08

```matlab
machine(m3,mwait_load) = 3.12
```

```txt
outtray(o1,opend_depart) = 0.359999999
```

outtray(o1,owait\_load) = 5.84

The final status of the simulation is shown in fig. 13.

Again, the results are displayed in a window:

```txt
Time = 11.775
```

intray(i1,ipend\_arrive) = 5.001

intray(i1,iwait\_unload) = 6.774

![](/api/attachments/GDNXUXY6/fulltext/images/219eaec22a183ef416a4756f363836a414bb7049f6c76deb75b70fe1fe79f21e.jpg)  
Fig. 12. Simulation graph during execution.

intray(i2,ipend\_arrive) = 4.078

intray(i2,iwait\_unload) = 7.697

$$
\text { machine } (\mathrm{m1}, \text { mbusy }) = 1 1. 7 7 5
$$

$$
\text { machine } (\mathrm{m2}, \text { mbusy }) = 1 1. 7 7 5
$$

$$
\text { machine } (\mathrm{m3}, \text { mbusy }) = 8. 6 5 5
$$

$$
\text { machine } (m 3, m \text { wait\_load }) = 3. 1 2
$$

$$
\text { outtray } (o 1, \text { opend\_depart }) = 1. 2 3
$$

$$
\text { outtray } (o 1, \text { owait\_load }) = 1 0. 5 4 5
$$

## 6.5. External solvers

In this section the use of GX to develop a graphical interface for an external solver, e.g. for linear programming, is illustrated. The graphical interface requirements are the following:

1. Formulate the Model

\- draw nodes and arcs

\- add attribute information

![](/api/attachments/GDNXUXY6/fulltext/images/2f5e513a88c8776c79f41be79dfe32da225be8c073071b708009dd67a143c19b.jpg)  
Fig. 13. Final state of the simulation network.

2. Query the Model

\- convert from graphical syntax to solver syntax

3. Present the Results

\- pass parameter file to the solver (Mac-Lingo)

\- display the textual output from the solver

In this application, we also illustrate the use of the icon editor, used previously to develop images for the tool palette, but used here for graphical images as well. The icon editor is a simple graphic editor, as illustrated in the following screenshot (fig. 14).

The example used here is from Hillier and Lieberman (1974, p. 109), a transportation problem involving a pea canning company, which must ship its product from various canneries (sources) to various warehouses (sinks). The interface program consists of three parts: (1) the usual specifications of the direct manipulation graphical symbols and their attributes, (2) a program to convert from the graphical syntax to the solver syntax, and (3) a special command go to process the model in the solver. The first part, specification of graphical interface, is given below:

/\*Transport.GX\*/

/\*parameters\*/

label can\_loc: 'Location of cannery?'.

label ware\_loc: 'Location of warehouse?'.

numeric output: 'What is output for this cannery?'. numeric allocation: 'What is quota for this warehouse?'.

![](/api/attachments/GDNXUXY6/fulltext/images/8cade3dbe5fd116b07fd3afb8ce1c01b5239cd755ee2a155b43b3d544413a798.jpg)  
Fig. 14.

```prolog
numeric ship_cost: 'What is shipping cost per truckload for this route?'.  
/*graph declarations*/  
query(go,'*').  
nodetype(icon(18403),c,cannery,[can_loc,output]).  
nodetype(icon(16909),w,warehouse,[ware_loc,allocation]).  
linktype(route,cannery,warehouse,[ship_cost]).
```

The second part of the interface program gives the instructions for interpreting the graphical symbols and for solving the model.

```txt
/*document template for LINGO*/
doc transport.
SETS:
    CANNERY/{textlist(C,cannery(C,_,_),',')}/:OUTPUT;
    WAREHSE/{textlist(W,warehouse(W,_,_)','')}/:ALLOC;
    ROUTES(CANNERY,WAREHSE):COST,VOLUME;
ENDSETS
MIN = @SUM(ROUTES:COST*VOLUME);
@FOR(WAREHSE(J):
    @SUM(CANNERY(I):VOLUME(I,J)) >ALLOC(J));
```

```txt
@FOR(CANNERY(I):
    @SUM(WAREHSE(J):VOLUME(I,J)) < OUTPUT(I));
DATA:
    OUTPUT = {textlist(N,cannery(C,_,N),")};
    ALLOC = {textlist(N,warehouse(W,_,N),")};
    COST = {textlist(N,(cannery(C,_,_),warehouse(W,_,_),
    route(LID,C,W,N)),")};
ENDDATA
!!!
```

The third part of the interface program, the go program, passes the parameter file to the solver and captures the solver's output for display in the results window:

```prolog
/*go*/
go:-document('LINGO',transport).
/*textlist*/
textlist(X,PP,Sep,TextAtom):
    findall(X,PP,L),
    concat_list(Sep,L,TextAtom).
concat_list(Sep,[X],X):-!.
concat_list(Sep,[X | L],TextAtom):
    concat_list(Sep,L,RestAtom),
    concat(X,Sep,Atom0),
    concat(Atom0,RestAtom,TextAtom).
```

![](/api/attachments/GDNXUXY6/fulltext/images/78aaf35d0876ae8d467e59e3071ecc7f275f4df14b6adeae78ada9bfe780a7a3.jpg)  
Fig. 15. The pea cannery LP model.

Fig. 15 illustrates the use of this interface for the pea cannery problem. In this example, the solver's task is to find the best transportation route, i.e., the route that minimizes the cost of transporting the peas from the canneries to the warehouses. As Figure 10 shows, the routes (i.e., links) from each cannery to each warehouse have different cost attributes associated with them. Also, each cannery has a specified production capacity; each warehouse, a specified storage capacity.

When the graphical representation of the problem is ready, the user clicks on the ‘\*’ tool, which executes the go program to generate the following output screen:

```matlab
SETS:
CANNERY/c1,c2,c3/:OUTPUT;
WAREHSE/w1,w2,w3,w4/:ALLOC;
ROUTES(CANNERY, WAREHSE):COST,
VOLUME,
ENDSETS
MIN = @SUM(ROUTES:COST * VOLUME);
@FOR(WAREHSE(J):
@SUM(CANNERY(I):VOLUME(I,J)) > 
ALLOC(J));
@FOR(CANNERY(I):
@SUM(WAREHSE(J):VOLUME(I,J)) < 
OUTPUT(I));
DATA:
OUTPUT = 75 125 100;
ALLOC = 80 65 70 85;
COST = 464 513 654 867 352 416 690 791
995 682 388 685;
ENDDATA
```

After saving this screen to a file, it is loaded into the solver, 'MacLingo', to produce the following output:

```matlab
MacLINGO 1.04L (30MAR89)
ROWS = 8 VARS = 12 NO.INTEGER VARS = 0
NONZEROES = 43 CONSTRAINT NONZ = 24(24ARE + -1)DENSITY = 0.413
SMALLEST AND LARGEST ELEMENTS IN ABSOLUTE VALUE = 1.00000
995.000
NO. < :3NO. =: 0, NO.4,OBJ = MIN,GUBS <= 4
SINGLE COLS = 0
```

```txt
MIN 464 VOLUME(C1,W1) + 513 VOLUME-
(C1,W2) + 654 VOLUME(C1,W3).
+ 867 VOLUME(C1,W4) + 352 VOLUME-
(C2,W1) + 416 VOLUME(C2,W2)
+ 690 VOLUME(C2,W3) + 791 VOLUME-
(C2,W4) + 995 VOLUME(C3,W1)
+ 682 VOLUME(C3,W2) + 388 VOLUME-
(C3,W3) + 685 VOLUME(C3,W4)

SUBJECT TO
2] VOLUME(C1,W1) + VOLUME(C2,W1)
+ VOLUME(C3,W1) >= 80
3] VOLUME(C1,W2) + VOLUME(C2,W2)
+ VOLUME(C3,W2) >= 65
4] VOLUME(C1,W3) + VOLUME(C2,W3)
+ VOLUME(C3,W3) >= 70
5] VOLUME(C1,W4) + VOLUME(C2,W4)
+ VOLUME(C3,W4) >= 85
6] VOLUME(C1,W1) + VOLUME(C1,W2)
+ VOLUME(C1,W3) + VOLUME
C1,W4) <= 75
7] VOLUME(C2,W1) + VOLUME(C2,W2)
+ VOLUME(C2,W3) + VOLUME(C2,
W4) <= 125
8] VOLUME(C3,W1) + VOLUME(C3,W2)
+ VOLUME(C3,W3) + VOLUME(C3,
W4) <= 100

END

The Lingo output gives all the usual details of
a linear problem solver, as shown in the continua-
tion of output in table 1.
```

## 7. Discussion

The GX Shell, while currently operational, is still undergoing revision and refinement. As suggested earlier in section 2, the principal intellectual challenge is to identify necessary and useful affordances, and package them in such a way that the user achieves a certain resonance with the model building process. In developing the GX Shell, and in testing it in MBA classes, we have learned that resonance depends on a variety of factors.

Some of these factors are hardware dependent. Among these, the most important is screen size. This system was developed using a double page screen (15" × 12"), whereas most of the MBA's used it on a small screen (7" × 5.5"), which tended to limit them to smaller size prob-

Table 1

<table><tr><td colspan="3">LP OPTIMUM FOUND AT STEP 7 OBJECTIVE VALUE = 152535.000</td></tr><tr><td>VARIABLE</td><td>VALUE</td><td>REDUCED COST</td></tr><tr><td>OUTPUT(C1)</td><td>75.00000</td><td>0.00000</td></tr><tr><td>OUTPUT(C2)</td><td>125.00000</td><td>0.00000</td></tr><tr><td>OUTPUT(C3)</td><td>100.00000</td><td>0.00000</td></tr><tr><td>ALLOC(W1)</td><td>80.00000</td><td>0.00000</td></tr><tr><td>ALLOC(W2)</td><td>65.00000</td><td>0.00000</td></tr><tr><td>ALLOC(W3)</td><td>70.00000</td><td>0.00000</td></tr><tr><td>ALLOC(W4)</td><td>85.00000</td><td>0.00000</td></tr><tr><td>COST(C1,W1)</td><td>464.00000</td><td>0.00000</td></tr><tr><td>COST(C1,W2)</td><td>513.00000</td><td>0.00000</td></tr><tr><td>COST(C1,W3)</td><td>654.00000</td><td>0.00000</td></tr><tr><td>COST(C1,W4)</td><td>867.00000</td><td>0.00000</td></tr><tr><td>COST(C2,W1)</td><td>352.00000</td><td>0.00000</td></tr><tr><td>COST(C2,W2)</td><td>416.00000</td><td>0.00000</td></tr><tr><td>COST(C2,W3)</td><td>690.00000</td><td>0.00000</td></tr><tr><td>COST(C2,W4)</td><td>791.00000</td><td>0.00000</td></tr><tr><td>COST(C3,W1)</td><td>995.00000</td><td>0.00000</td></tr><tr><td>COST(C3,W2)</td><td>682.00000</td><td>0.00000</td></tr><tr><td>COST(C3,W3)</td><td>388.00000</td><td>0.00000</td></tr><tr><td>COST(C3,W4)</td><td>685.00000</td><td>0.00000</td></tr><tr><td>VOLUME(C1,W1)</td><td>0.00000</td><td>15.00000</td></tr><tr><td>VOLUME(C1,W2)</td><td>20.00000</td><td>0.00000</td></tr><tr><td>VOLUME(C1,W3)</td><td>0.00000</td><td>84.00000</td></tr><tr><td>VOLUME(C1,W4)</td><td>55.00000</td><td>0.00000</td></tr><tr><td>VOLUME(C2,W1)</td><td>80.00000</td><td>0.00000</td></tr><tr><td>VOLUME(C2,W2)</td><td>45.00000</td><td>0.00000</td></tr><tr><td>VOLUME(C2,W3)</td><td>0.00000</td><td>217.0000</td></tr><tr><td>VOLUME(C2,W4)</td><td>0.00000</td><td>21.00000</td></tr><tr><td>VOLUME(C3,W1)</td><td>0.00000</td><td>728.0000</td></tr><tr><td>VOLUME(C3,W2)</td><td>00.00000</td><td>351.0000</td></tr><tr><td>VOLUME(C3,W3)</td><td>70.00000</td><td>0.00000</td></tr><tr><td>VOLUME(C3,W4)</td><td>30.00000</td><td>0.00000</td></tr></table>

<table><tr><td>ROW</td><td>SLACK ORS SURPLUS</td><td>DUAL PRICE</td></tr><tr><td>1</td><td>152535.0</td><td>1.000000</td></tr><tr><td>2</td><td>0.0000000</td><td>-449.0000</td></tr><tr><td>3</td><td>0.0000000</td><td>-513.0000</td></tr><tr><td>4</td><td>0.0000000</td><td>-570.0000</td></tr><tr><td>5</td><td>0.0000000</td><td>-867.0000</td></tr><tr><td>6</td><td>0.0000000</td><td>0.0000000</td></tr><tr><td>7</td><td>0.0000000</td><td>182.0000</td></tr></table>

lems. The ability to scroll and shift the drawing pane using the viewer do not compare to the impact of having the entire graph image present on the screen. (A zoom capability, shrinking the image, was also tried, but too much detail was lost.) A secondary hardware factor is speed of response. On the smaller machines, which are also slower, delays of 1-3 seconds sometimes occur. This is enough to distract the user away from the drawing activity, as they impatiently wait to regain control. A third hardware factor is resolution. While initially, users find the (Macintosh) resolution level adequate, as they move to more complex models, they seek to refine their artistry beyond what is presently available.

Software factors we encountered divide into three categories: screen layout, interaction dynamics, and tool functionality.

Screen layout refers to the visual image the user has produced for the graph model. This is partly a matter of aesthetics, since a common use is to copy the graph image into a textual report or slide images for transparencies. Beyond aesthetics, however, the visual cohesiveness and balance of the graph are important for the user's visual verification and subjective analysis of the model. For instance, when a user draws an arc, he/she needs only hit some part of the source and target nodes, and the system computes where the ends of the arc attach to the node image. As can be seen from the preceding screen snapshots, getting the arc to actually touch the image (especially where the node has an irregular shape), and doing so at the proper angle are aspects needing further refinement. Another aspect of screen layout is the positioning of attribute data for nodes and arcs. Often this can begin to crowd the screen, making it difficulty to see which arc/node the data applies to. At present, the user is able to re-position this data (using the select tool) as well as change its size and font (using the FONT menu). Planned extensions are to be able to rotate the attribute fields to fit them better on angled arcs. Another approach to the presentation of attribute data is suggested by Kendrick (1990a,b), is to maintain this data in separate, tabular windows). (See also Jones, 1990b for a discussion of screen layout issues in his Network system.)

The second category of software factors is the dynamics of the interaction. This includes the mechanical actions the user is allowed to make, as well as the visual feedback cues provided by the system. At present, the basic graphical actions are all done using a single button mouse, allowing click (or double click) at a point, and dragging the mouse (with button down). The visual cues provided by the system are: to highlight the selected tool, to change the cursor image (e.g.

from arrow to crosshair), to put small square around the outline of selected objects, and to show a gray line when dragging (called a 'rubber band' for lines, a 'marqui' for rectangular shapes).

The simplest manipulation is to add a node, which is to select the node tool and click in the desired location in the drawing area. The eraser tool requires a double click anywhere on the graphical object to be removed. Bar shaped nodes (e.g. for Petri nets) allow the user to control the length of the bar by dragging the mouse vertically. In using the arc tool, one clicks on the starting node and the cursor changes to a cross-hair indicating that the system has identified the node. As the user slides the mouse to the target node, a gray line is drawn to indicate where the arc will appear. The user can draw the arc as a broken line, clicking at each line segment, finally double clicking on the target node. In addition, the user can copy or delete whole sub-graphs using the select tool plus copy, cut and paste operations.

The primary deficiency we find here (which is actually a hardware shortcoming) is that the system is oriented towards a one-handed user. Since these interfaces are primarily graphical, there is very little, if any, keyboard contact (mainly to type in attribute values). Thus, the user controls the mouse with one hand, while the other hand remains idle. Considerably more functionality and control could be achieved if the user had a second mouse, possibly with different functions (such as rotation). For example, at present the user frequently shifts the mouse from the drawing pane to the tool palette, e.g. to draw an arc, then reposition its attribute label. With a second mouse, the user could use one for tool selection and the other for drawing.

The third category of software factors is defining the functionality, i.e. affordances, of the various tools. We regard our present tool kit as adequate for an initial version, but anticipate further innovations. The functionality we presently offer is essentially to portray connectedness between objects in the model. The next level of challenge is to provide abstraction mechanisms for dealing with the complexity of more elaborate models. Since most graphical representations can (with minor extensions) support subgraphs, a 'packaging' tool might be provided to collapse some selected region of the graph into a subgraph reference, which is then displayed in another graph window.

## 8. Other systems and approaches

The use of graphical interfaces, and consequently interface developments aids, is becoming popular in various areas such as CAD/CAM, Hypertext/Hypermedia systems, and Computer Aided Instruction. The following brief review focuses on the growth of these tools in the DSS area.

A number of graphical interface tools have been developed to aid in the formulation of linear programming problems. An early effort, specific to transportation/transshipment problems, is the VERGIN system of Fisher, Greenfield and Jaikumar (1982). A more recent system, covering a broader range of LP problems is LPFORM, by Ma, Murphy and Stohr (1989). This system, written in Prolog for an IBM PC/AT, does extensive analysis of the LP formulation, but does not support direct manipulation. A comparable system is Choobineh (1991).

Another LP oriented system is PTS by Kendrick (1990a,b), which focuses on production and transportation system modeling (using GAMS as an external solver). This system, written in C for an IBM PC/AT, does support direct manipulation graphics. In addition, it provides ‘parallel representations’ of the problem, e.g. both graphical and the tabular GAMS format, which are isomorphic; changes in either representation are reflected in the other.

Several efforts at developing more general graph-based modeling systems (GBMS's) include Wolfberg (1969), Delgrande (1980), Dao et al (1986), Göttler (1983, 84, 87, 89) and Jones (1990a, b, 1991a, b, c). In the latter two, the emphasis is on the development of 'graph grammars' that describe the well-formedness of graph representations for a particular problem domain, as well as the modifications that may be made to it, in the form of graph grammar productions. In the NETWORKS system of Jones, implemented in Prolog on a Macintosh, these productions (e.g. "move a customer from one route to another") are presented to the user in a menu-driven command language, rather than the direct manipulation style suggested here. A unique feature of this system is that the developer interface (which we present as Prolog assertions) is also presented in graphical form. An application of NETWORKS to production, distribution, and inventory (PDI) problems is described in Jones and Krishnan (1989).

Another aspect is the coding of solution algorithms. In GX at present, these are either coded in Prolog $^{3}$ (e.g. (PERT, Decision Trees) or, for numeric algorithms, passed to an optimization package. Recent developments in Constraint Logic Programming (CLP) promise to incorporate such optimization techniques in a more integrated fashion. CLP is a generalization of logic programming that replaces the process of unification of terms with a more general technique of constraint resolution. For symbol (non-numeric) terms, the process is much the same. However, for numeric formulae, CLP uses a simplex algorithm to resolve constraints (see e.g. Lassez, 1987; Jaffar and Michaylov, 1987; Colmerauer, 1990; Cohen, 1990). With this capability, a much better integration of graphic interfaces, symbolic processing and numeric optimization is possible.

Although the GX shell provides only limited animation capabilities, there is a growing literature that points to interesting new possibilities in this direction as well. See for instance, Brown and Sedgwick (1984), Myers (1986), Bentley and Kernighan (1987), and Bell, Taseen and Kirkpatrick (1990).

## 9. Concluding remarks

Graphics programming can be very time consuming. However, things are getting better: developing this interface generator took about the same time as developing an application specific graphics interface just four years ago. $^{4}$ As the implementation difficulties become less daunting, design issues will no doubt become more focused. In the present design, we have explored a direct manipulation philosophy, with an effort to maintain a certain amount of consistency and familiarity in the tool design from one problem domain to another. We are aware, however, that this is only a draft version of these tools, and anticipate subsequent improvements based on further experience.

At present, the theory of interface design is more or less in the “I know one when I see one” stage. Using the concepts of affordance and resonance, we have tried to sketch the outlines of what a more tractable theory might look like. Reversing the perspective, the subject area of interface design may also prove fruitful for the study of direct perception, providing a limited and focused context for experimentation. $^{5}$

## References

[1] G. Avrahami, K. Brooks and M. Brown, A Two-View Approach to Constructing User Interfaces, SIGGRAPH (1989).

[2] P.C. Bell, A.A. Taseen and P.F. Kirkpatrick, Visual Interactive Simulation Modeling in a Decision Support Role, Computers and Operations Research No. 17, 5 (1990) 447–456.

[3] J.L. Bentley and B.W. Kernighan, A System for Algorithm Animation: Tutorial and User Manual, Computer Science Technical Report No. 132 (ATT Bell Labs, Murray Hill, NJ, 1987).

[4] I. Bratko, Prolog Programming for Artificial Intelligence, 2nd ed. (Addison-Wesley, Rading, MA, 1990).

[5] M.H. Brown and R. Sedgwick, A System for Algorithm Animation, Computer Graphics 18, No. 3 (1984) 177–186.

[6] J. Choobineh, A Diagramming Technique for Representation of Linear Models, Omega No. 19, 1 (1991) 43–51.

[7] J. Cohen, Constraint Logic Programming Languages, CACM 33, No. 7 (July 1990) 52–68.

[8] A. Colmerauer, An Introduction to Prolog III, CACM 33, No. 7 (July 1990) 69–90.

[9] J. Conklin, Hypertext: An Introduction and Survey IEEE Computer (Sept. 1987) 17–41.

[10] M. Dao, M. Habib, J.P. Richard and D. Tallot, CABRI: An Interactive System for Graph Manipulation, in: Tinhofer, G. and Schmidt, G. (Eds), Graph-Theoretic Concepts in Computer Science (Springer-Verlag, Berlin, 1986).

[11] J.P. Delgrande, A Graph-Theoretic Language Extension for an Interactive Computer Graphics Environment, Computers and Graphics 5 (1980) 13–22.

[12] S. Draper, Display Managers as the Basis for User-Machine Communication, in: Norman, D. and Draper, S., Eds. User Centered System Design – New Perspectives on Human-Computer Interaction (Lawrence Erlbaum, Hillsdale, NJ, 1986) 339–352.

[13] M. Fisher, A. Greenfield and R. Jaikumar, A Decision Support System for Vehicle Scheduling, Working Paper No. 82-06-02 (Department of Decision Sciences, Wharton School, University of Pennsylvania, Philadelphia, PA, June 1982).

[14] J. Gibson, The Ecological Approach to Visual Perception (Houghton Mifflin, Boston, MA, 1979).

[15] H. Göttler, Attributed Graph Grammars for Graphics, in: Ehrig, H., Nagl, M. and Rozenberg, G., Eds. Graph Grammars and Their Application to Computer Science (Lecture Notes in Computer Science 153) (Springer-Verlag, Berlin, 1983) 130–142.

[16] H. Göttler, Implementation of Attributed Graph-Grammars, Proceedings of the International Workshop on Graph Theoretic Concepts in Computer Science (Universitätsverlag Rudolf Trauner, Linz, 1984).

[17] Göttler, H. Graph-Grammars and Diagram Editing, in: Ehrig, H., Nagl, M., Rozenberg, G. and Rosenfeld, A., Eds, Graph Grammars and Their Application to Computer Science (Springer-Verlag, Berlin, 1987) 130–142.

[18] H. Göttler, Graph-Grammars, a New Paradigm for Implementing Visual Languages, in: Deshowitz, N., Ed., Rewriting Techniques and Applications (Lecture Notes in Computer Science 355) (Springer-Verlag, Berlin, 1989).

[19] F. Halasz, Reflections on Notecards: Seven Issues for the Next Generation of Hypermedia Systems, CACM 31, No. 7 (1988) 836–852.

[20] F. Hillier and G. Lieverman, Operations Research (Holden-Day, San Francisco, CA, 1974).

[21] G. Huber, Managerial Decision Making (Scott-Foresman, Glenview, IL, 1980).

[22] E. Hutchins, J. Hollan and D. Norman, Direct Manipulation Interfaces, in: Norman, D. and Draper, S., Eds., User Centered System Design – New Perspectives on Human-Computer Interaction (Lawrence Erlbaum, Hillsdale, NJ, 1986).

[23] K. Itoh, K. Muramatsu, M. Matsui and S. Suzuki, Graphical Editing and Analysis System for Network System (GEANS), Computers and Graphics 6, No. 2 (1982) 47–61.

[24] J. Jaffer and S. Michaylov, Methodology and Implementation of a Constraint Logic Programming System, Proceedings of the Fourth International Conference on Logic Programming (MIT Press, Cambridge, MA, 1987).

[25] C. Jones, An Example-Based Introduction to Graph Grammars for Modeling, Proceedings of the Hawaii International Conference on System Sciences, Vol. III (Jan. 1990a) 433–442.

[26] C. Jones, An Introduction to Graph-Based Modeling Systems, Part I: Overview, ORSA Journal on Computing 2, No. 2 (1990b) 136–151.

[27] C. Jones, An Introduction to Graph-Based Modeling Systems, Part II: Graph-Grammars and the Implementation, ORSA Journal on Computing 3, No. 3 (1991a) 180–206.

[28] C. Jones, An Integrated Modeling Environment Based on Attributed Graphs and Graph-Grammars, forthcoming, Decision Support Systems (1991b).

[29] C. Jones, Attributed Graphs, Graph-Grammars, and Structured Modeling, Annals of Operations Research (1991c) forthcoming.

[30] C. Jones and R. Krishnan, A Visual, Syntax-Directed Environment for Automated Model Development, Working Paper 89-12-10 (Department of Decision Sciences, Wharton School, University of Pennsylvania, Philadelphia, PA, April 1990).

[31] D. Kendrick, Parallel Model Representations, Working Paper 89-01, (Center for Economic Research, University of Texas, Austin, TX, Jan. 1990a).

[32] D. Kendrick, A Graphical Interface for Production and Transportation System Modeling: PTS, Working Paper 89-08, (Center for Economic Research, University of Texas, Austin, TX, March 1990b).

[33] C. Lassez, Constraint Logic Programming, Byte (Aug. 1987).

[34] P-C, Ma, F. Murphy and E. Stohr, A Graphics Interface for Linear Programming, CACM 32, No. 8 (Aug. 1989) 996–1012.

[35] H. Maturana, J. Lettvin, W. McCulloch and W. Pitts, Anatomy and Physiology of Vision in the Frog, Journal of General Physiology, No. 43 (1960) 129–175.

[36] C. Michaels and C. Carello, Direct Perception (Prentice-Hall, Englewood Cliffs, NJ, 1981).

[37] B. Myers, Visual Programming, Programming by Example and Program Visualization; A Taxonomy, Proceedings of SIGCHT86: Human Factors in Computing Systems (Boston, MA, April 13–17, 1986).

[38] B. Myers, Encapsulating Interactive Behaviors, Proceedings of the Conference on Computer Human Interaction (Austin, TX, 1989) 319–324.

[39] F. Newbery, An Interface Description Language for Graph Editors, IEEE Workshop on Visual Languages (1988) 144–149.

[40] J.L. Peterson, Petri Net Theory and the Modeling of Systems (Prentice-Hall, Englewood Cliffs, NJ, 1981).

[41] B. Schneiderman, Direct Manipulation: A Step Beyond Programming Languages IEEE Computer (Aug. 1983) 57–69.

[42] B. Schneiderman, Designing the User Interface: Strategies for Effective Human-Computer Interaction (Addison-Wesley, Reading, MA, 1987).

[43] R. Stamper, A Logic of Social Norms for the Semantics of Business Information in: Steel, T. and Meersman, R. Eds, Proceedings of IFIP WG 2.6 Conference of Database Semantics (North-Holland, Amsterdam, 1985) 105–133.

[44] L. Sterling and E. Shapiro, The Art of Prolog (MIT Press, Cambridge, MA, 1986).

[45] E. Tufte, The Visual Display of Quantitative Information (Graphics Press, 1983).

[46] T. Winograd and F. Flores, Understanding Computers and Cognition (Ablex Publishing Company, Norwood, NJ, 1986).

[47] M.S. Wolfberg, An Interactive Graph Theory System, Unpublished Ph.D. Dissertation (University of Pennsylvania, Philadelphia, PA, 1969).
