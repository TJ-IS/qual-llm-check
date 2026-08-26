---
otero_id: 21591
otero_key: "9EUFKAS4"
title: "A hypertext environment for linear optimisation"
authors: "Gérald Collaud"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00039-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hypertext environment for linear optimisation

Gerald Collaud ´ \*

Institute of Computer Science, Rue de Faucigny 2, UniÕersity of Fribourg, CH-1700 Fribourg, Switzerland

Received 1 December 1997; accepted 30 March 1998

## Abstract

In decision making, multiple model representations of linear optimisation models are gaining growing interest and importance. In information science, hypertext and scripting facilities, both of which expand the expressiveness of simple text and graphic documents, have also become an important issue. In previous work the author has developed a graphical tool for creating and solving linear programming models. In this paper, we present an environment that integrates this graphical tool, a textual representation of linear optimisation models and a hypertext system. Through a typical user session, it is also shown how users interact with the environment and how hypertext and scripting facilities can help users understand linear optimisation. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Linear programming; Hypertext; Graphical modelling; Integrated modelling environments

## 1. Introduction

In decision making, research on modelling languages and environments has become an important issue within the last decade. This is particularly true for Linear Programming LP where these environ-Ž . ments allow users to represent their models in a declarative and executable form. Examples of such languages are GAMS 6 , AMPL 16 , MIMI 8 and <sup>w x</sup> <sup>w</sup> <sup>x</sup> <sup>w x</sup> LPL 24 . Progress in user interface design and<sup>w</sup> <sup>x</sup> advances in microcomputer graphics have encouraged the emergence of new, interactive graphical modelling systems such as And–Or graphs 39 , <sup>w</sup> <sup>x</sup> Structured Modelling 17–19,23 , GBMS 26–28 , <sup>w</sup> <sup>x</sup> <sup>w x</sup> GBMS<sup>r</sup>SM 7 , NETFORMS 20 , GIN 44 , LP-<sup>w x</sup> <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> Form 32 , entity relationship diagrams 9 , or gLPS <sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> <sup>w</sup> <sup>x</sup> 14 . See Refs. 21,43 for a survey of algebraic languages, and Ref. 29 for a survey of graphical <sup>w</sup> <sup>x</sup> ones.

In information science, important investigations have been conducted in the area of hypertext. Hypertext, in its simplest form, expands the expressiveness of simple text and graphic documents by allowing users to jump from place to place usually by ‘clicking’ on a highlighted element 15 . AIMMS 5 , for<sup>w</sup> <sup>x</sup> <sup>w x</sup> instance, allows users to jump from one ‘page’ of a ‘project’ to another ‘page’ simply by clicking on a ‘button’. This basic hypertext concept has, however, several problems and limitations. For instance, basic hypertext does not allow for the automatic creation of links at runtime; all the links have to be created manually. Another problem is the network disorientation problem, also known as the ‘lost in hypertext problem; users of hypertext systems often do not know where they come from, where they are and where they can go. These problems and limitations, as well as others, have been identified and are discussed in, among others, Refs. 2,22,45 . To avoid<sup>w</sup> <sup>x</sup> these problems and limitations, some authors have proposed extensions to the basic hypertext concept. Ref. 4 for instance, proposes the notion of gener- <sup>w</sup> <sup>x</sup> alised hypertext. Basically, by using a standard format to declare system entities and by using generalisations of nodes, links and link traversal, generalised hypertext allows nodes, links and alternate views to be inferred or computed at runtime, thus reducing the cost of building hyperdocuments. Ref. 33 shares the <sup>w</sup> <sup>x</sup> same concerns about basic hypertext and, with WEBSs Woven Electronic Book System with Ž scripts , propose to extend the basic hypertext con- . cept with scripts, i.e., small programs attached to objects of the hypertext that modify the behaviour of the basic hypertext.

For many years, our research group at the Institute of Informatics of the University of Fribourg Ž . IIUF has been developing applications in both information science and decision making. We developed hypertext prototypes such as WEBSs 34,37,38 ,<sup>w</sup> <sup>x</sup> and modelling environments for LP such as LPL 25<sup>w</sup> <sup>x</sup> and gLPS 12 . The work presented in this article <sup>w</sup> <sup>x</sup> combines these two research threads into one application, gLPS for WEBSs gW , which makes up aŽ . new way of helping present and understand linear optimisation.

The purpose of this article is first, to describe gW, and second, to show how this environment could help perform more effectively optimisation modelling. The article is thus organised into the following sections. Section 2 focuses on the underlying concepts of gW. Section 3 defines the components of gW and presents their interface. Section 4, through an imaginary session, shows an example of the use of the environment. Finally, Section 5 concludes the paper by discussing directions for future developments.

## 2. Motivation and concepts

Trying to create and understand Linear Programming LP models is a complex process. Tradition-Ž . ally, books printed on paper have been used to convey knowledge. The book has several advantages. It can easily be transported, it does not require any additional hardware except in some cases, Ž glasses , and more importantly, it provides an inter- . face known and accepted by everyone. In addition, although its physical linear structure favours sequential access—sometimes not adapted to the learning of particular concepts, some cross-references, indexes, or table of contents allow more direct access to its content.

However, the static behaviour and rigid structure of books are not very well suited for scientific matters such as LP. For instance, relating the model, different data and different solutions is a complex task. Also, exercises are defined once for all; the reader does not have the opportunity to change the parameters in order to explore a model.

For several years, computers have been used to help provide the ability to solve such models. A user typically enters a model and the computer computes the optimal solution. Then, the user modifies some parameters and the computer computes the new optimal solution, if any. To perform optimisation modelling more effectively, however, simply solving models is not enough. A computerised system must fully take advantage of the interactive aspects of the computer. First, different users, different problems and different tasks clearly require different model representations. Many different model representations have been proposed plain text, algebraic,Ž block-structured, graphical, . . . but none can claim. to be best suited for all purposes and users. By showing different model representations of the same problem, computers allow users to select the one sŽ . which is are best suited to their needs. Second, theŽ . information needed to present, explain, model and then solve an LP model is generally dispersed throughout a document or even among several documents. Finding and relating all this information can be challenging. Hypertext simplifies the work required to explain or understand an LP problem by connecting together closely related information. As noted before, however, this notion has some problems and limitations. We propose the notion of extended hypertext, which adds multiple tables of contents, extensibility and annotation.

–Multiple tables of contents. In a traditional book, the information is usually presented independently of the reader’s experience level. Different readers need different explanations; e.g., an operations research expert does not need the same information as a student. One way of presenting the user with these different representations is through different tables of contents. A table of contents could list the documents needed by a student, while another lists the documents needed by an expert. Multiple tables of contents help present the same problem from different perspectives. Further, a table of contents is a form of overview that helps solve the ‘lost in hyper space’ problem.

–Extensibility. The creation of multiple tables of contents as well as the creation of many links is a complex and at times monotonous task. A computerised system should offer some tools to help these activities. Also, the standard behaviour of a hypertext is sometimes not precisely what a user needs. The system must thus be flexible enough so that it can be easily extended.

–Annotation. Last but not least, readers usually like to add comments such as marginal notes. A computerised system should offer the same capability.

We believe that environments that use multiple model representations and integrate extended hypertext will help perform more effectively optimisation modelling. gW gLPS for WEBSs is such an envi-Ž . ronment 13 . It combines textual and graphical mod- <sup>w</sup> <sup>x</sup> elling and solution of linear optimisation models with extended hypertext facilities Fig. 1 . TheŽ . graphical modelling capabilities are supplied by gLPS, the textual modelling capabilities are based upon LPL and the extended hypertext capabilities are provided by WEBSs. WEBSs allows the creation of annotation documents and multiple tables of contents, and its standard behaviour can be extended by the use of small programs called scripts.

![](/api/attachments/9EUFKAS4/fulltext/images/fb69d9c2a5f5ecfa761110cdd8aedd6ed3f62a852ef5a055093933b5f01f658c.jpg)  
Fig. 1. Genealogy of $\mathrm { g W } .$ . gLPS for WEBSs is the result of the mixing of WEBSs information science , gLPS and LPL decisionŽ . Ž making ..

In order to differentiate from a traditional book, gW makes use of two terms: builder and information space. An Information Space Ž . IS extends the common notion of a book by taking into account the interactive aspects that the computer brings multiple Ž model representations or extended hypertext . In. other words, an IS is a collection, or coherent set, of documents, links and scripts on a given subject. Documents, links and scripts are called the components of an IS.

Builders are authors of an information space. They express their ideas using the hypertext concept and they fully take advantage of the interactivity of a computer. A reader initially uses the work of a builder e.g., follows the link created by a builder ,Ž . but he can grow into a full builder by creating additional links and making on the spot annotations at will. Note that although a reader can become a builder, he cannot destroy the work of a builder. In fact, components of an IS are meant to be private or public. A builder’s component is considered to be public and may be consulted but not modified byŽ . anyone within the IS created by the builder, while a reader’s component is private. That means that any reader can see a builder’s component whereas one individual reader cannot see another individual reader’s component.

Section 3 gives a detailed description of these components.

## 3. The components of an Information Space

Section 3.1 defines each one of the components of an IS, that is, documents, links and scripts. Section 3.2 describes the interface of these components.

## 3.1. Definitions

## 3.1.1. Documents

Our hypertext environment offers the following kind of documents: text, graphic, browser and model. Due to the specific nature of the models, we have grouped the first three kinds of documents into a category called standard documents.

Standard documents. A text document displays information in a readable form. A graphical docu ment displays some static picture or static image.

Browsers are used to organise the IS in a manner similar to the table of contents found in a traditional book. Browsers organise subsets of documents hierarchically. More precisely, a browser is a tree-like structure, where each node in the tree can be associated with one or more documents Fig. 2 .Ž .

Unlike most books though, an IS allows for an unlimited number of browsers. Further, it also allows both builders and readers to create them. This gives the opportunity to organise the same knowledge in different ways, depending on the type or experience level of users. For example, an experienced user may use a browser showing only high level models whereas a beginner may need a detailed browser with documents that explain each of the models.

Models. Models are documents that can be computed and that can augment the IS. They are usually mathematical in nature. gW contains two kinds of models: LPL and gLPL models.

–LPL Linear Programming Language is an al- Ž . gebraic language that tries to represent a problem in a form close to standard mathematical notation. In particular, LPL separates the representation into four distinct parts. The first three parts are used to define the different components of a problem: SET for the indexes, COEF for the data associated with each right hand side or coefficient and VAR for specifying the decision variables. Note that the SET and COEF parts are optional. The last part, namely MODEL, contains the constraints and the objective function.

![](/api/attachments/9EUFKAS4/fulltext/images/2930d216fcdee04f858e4e7444bfb653e481a6df2e78cb9d6a0709ba3259d794.jpg)  
Fig. 2. Two browsers. Browsers are used to organise the documents of an IS hierarchically.

–The gLPL graphical Linear Programming Lan-Ž guage notation is based on the Activity Constraint. Ž . AC-graph symbolism 42 . Basically, a gLPL model<sup>w</sup> <sup>x</sup> is a network whose nodes are either a square, a circle or a triangle. Each graphical symbol has its counterpart in the traditional mathematical notation. A gLPL model is thus composed of four distinct elements. A square designates a variable. A circle, and the square s connected to it by a coefficient line, refers Ž . either to the left-hand side of a constraint or to an objective function. Its label identifies its type: <sup>F</sup> , <sup>G</sup> , <sup>s</sup> , max or min. A triangle represents the right-hand side of a constraint and contains the associated data. Specific rules determine how these elements can be connected together to form a network. A more detailed description of gLPL is given in Appendix A. Ref. 14 presents a functional descrip-<sup>w</sup> <sup>x</sup> tion of gLPS, and Ref. 10 gives a complete descrip- <sup>w</sup> <sup>x</sup> tion of the gLPL notation and gLPS.

Within gW, LP problems may be modelled either with LPL or with gLPL. Since gLPL represents a subset of LPL, gLPL models can be converted into LPL models whereas the reverse is not true. When solving a gLPL model, the environment first converts it into a LPL model and then calls a solver aŽ description of the conversion process between gLPL and LPL can be found in Appendix B . The results. appear inside new text documents.

Note that all the documents, that is, gLPL and LPL models as well as the resulting text documents, are fully integrated into the environment. They can therefore be used as nodes for a table of contents Ž . Sections 3.1.1 and 3.2.1 . Furthermore, document elements—graphical tokens for gLPL models, strings of text for LPL models and for solution documents, can be linked together in a hypertext fashion Sec- Ž tions 3.1.2 and 3.2.3 ..

This structure has been implemented using an object-oriented approach and an object-oriented library MacApp 40 . This allowed us to implement Ž <sup>w</sup> <sup>x</sup>. each level as a specialisation of the previous one Ž . Fig. 3 .

![](/api/attachments/9EUFKAS4/fulltext/images/64c9ed17b82366d814d04810525b5cb8687871059b724c6f0b397b78a9c6668f.jpg)  
Fig. 3. Documents implementation. MacApp implements the general concept of document; WEBSs specialises it for hypertext documents and new models are just plugged in.

MacApp implements the general notion of documents with their basic commands like ‘Open’ and ‘Save’. WEBSs specialises the document concept by giving a framework for hypertext facilities and for the models. It also implements the basic and standard models. New kinds of models are regarded as distinct, specialised modules that inherit behaviour from existing modules.

## 3.1.2. Links

This is the basic feature of a hypertext. Links are a means to connect related information together. They allow users to jump from one location of the IS to another. They can be generated automatically by the environment, or created by a builder or a reader. Links are always bi-directional; it is always possible to return to the starting point of a link by following the link in reverse. The start or end point of a link is called a block. A block is always associated with a visible piece of a document, called the block extent. In a text document, the block extent is a string of text; in a graphic document, the block extent is any part of the picture; and in a gLPL model, the block extent is a graphical element or a group of graphical elements. Blocks might be used by several links. As a consequence, more than one link may be connected to the same information.

Links and blocks are based upon WEBSs implementation. Essentially, the hypertext facilities are obtained by subclassing some WEBSs classes and by defining some basic notions, such as for instance the extent of a block in a gLPL model.

## 3.1.3. Scripts

Scripts allow one to customise the IS. In its simplest form, a script is a list of commands that is executed automatically by the environment. Scripts may also include sequencing instructions such as loops and conditionals, as well as calls to predefined routines and other scripts.

There are two kinds of scripts: unbound scripts and triggered scripts. Unbound scripts are launched by an explicit user request. They allow a complex set of actions to be grouped into a single command and then played back at will in different contexts. Such a script could for instance automatically create a browser of all the documents for a specific reader. The script would filter the documents of the IS and collect only those that are owned by the reader.

Triggered scripts are launched automatically when a specific action is performed e.g., the opening of a Ž document . For instance, the standard behaviour. when a user selects a link is to show its endpoint. A script can be attached to a specific link so that when the user selects it, a message is displayed on the screen before jumping to the endpoint. Triggered scripts can be attached to virtually any component of the IS. Thus, triggered scripts allow the builder of an IS to obtain common behaviour from a group of objects with minimal effort. For example, it is easy to write a script which remembers all the text documents that have been opened this list may then be Ž used to display a history of all the textual documents visited ..

With these concepts at hand, we shall now discuss their implementation through the description of the interface.

## 3.2. Interface

gW has been implemented on an Apple Macintosh. On the operating system level, it consists of the gW application, the LPL Solver, one file for each IS and its various associated documents. Each IS file name ends with ‘.book’. This file stores the database of the IS. It includes the blocks and links, the scripts and the locations of all the documents of the IS. The documents are usually stored in a separate folder having the same prefix as the ‘.book’ file. Fig. 4 shows a typical organisation of these files.

![](/api/attachments/9EUFKAS4/fulltext/images/08fa925195684567d090b06e86e5db24dc054fa9cbbc657faebe3614062fc46d.jpg)  
Fig. 4. The gW environment at the operating system level. It consists of the $\mathrm { g W }$ application left , the LPL solver middle , theŽ . Ž . IS database top-right and a folder containing the related docu-Ž . ments bottom-right .Ž .

When starting the application, users are asked through a dialogue box to choose an existing IS or to create a new one. They are also asked if they wish to be the builder or a reader Fig. 5 . To become theŽ . builder of the selected IS, specifying ‘author’ as user name is sufficient. Any other user name indicates that the user will be a reader.

At this point, gW always launches a start-up script ‘Startup’ . This script can be used by buildersŽ . to configure their own working environment, for instance, by opening the script editor. Builders can also use this script to configure the reader’s environment, e.g., set a starting point for IS exploration by opening a specific browser.

Within the application, users can then either create new documents with one of the ‘New’ commands of the ‘File’ menu or open existing documents using the ‘Open’ command. Each document is shown in a window. Users act on documents by choosing commands from a menu. When users proceed from one window to another, menu commands that can act on a document change automatically, according to the type of document shown in the front-most window.

![](/api/attachments/9EUFKAS4/fulltext/images/fba70d33c113ef7e85249709e0f61e2119e0d1353cb2d515fe378e3431c4a484.jpg)  
Fig. 5. The initial dialogue. Users can choose the IS they want to use and the status they want to have builder or reader . Ž .

## 3.2.1. Standard documents

Text documents have the typical formatting commands for dealing with text, such as changing the typeface or modifying the font size. These commands are grouped under the menus ‘Text’ and ‘Format’.

In its current implementation, gW does not allow for the creation of graphic documents. To be viewed within gW, they have to be created using another tool, such as MacDraw or Canvas, and then copied and pasted, or imported, into gW.

Browsers possess all the commands necessary to maintain a structured table of contents. These commands are grouped into two menus: ‘Node’ and ‘Table’. The former shows commands that can modify the display of a specific browser node ‘Color’ orŽ ‘Shade’ , and the latter shows all the commands that. could change the content of the browser ‘DeleteŽ node’, ‘Expand node’, and so on . See Ref. 35 for a. <sup>w</sup> <sup>x</sup> survey of the commands of the environment. Fig. 6 displays a typical browser. The window is divided into two parts. The left part is called the palette and contains the drawing tools that are used to produce the hierarchical structured representation of the IS displayed on the right. Note that this hierarchical structure could also be created automatically by a script. The rectangle in the palette represents a browser node. The line is used to connect browser nodes together. A node with a document icon on its left indicates that this node has associated document s . To open the associated document s ,Ž . Ž . the user double-clicks on the node. Nodes may be contracted or expanded. Three dots in the bottom part of a node represent a node that can be expanded. For example, the node ‘Exercises’, on the right part of the window, can be expanded in order to show its subnodes.

![](/api/attachments/9EUFKAS4/fulltext/images/66b48eec0179d8342b44cb4ac4994457bd8d34e6afefe1dfb09dc93fa64e71d8.jpg)  
Fig. 6. A typical browser. The palette left part is used to create Ž . the elements nodes and lines shown in the right part; each node Ž . can be associated with one or many documents.

## 3.2.2. Models

gW supports two kinds of models: LPL and gLPL models. In order to describe them, we consider now the following simple LP problem:

A company owns one factory i , two distribution Ž . centers X, Y and has three main customers Ž . Ž . 1, 2, 3 . The factory has a limited production capacity and each of the customers has a precise demand. Each connection has a given cost. Find the quantities to be transported on each arc in order to satisfy the demands, assuming that the overall costs are minimised.

As stated in Section 3.1, a gLPL model is a graphical representation of a linear optimisation model. Each mathematical element corresponds thus to a graphical element. These elements are on the left side the palette of the gLPL window of Fig. 7. TheŽ . model is shown on the right part of the window theŽ view . The model is manually drawn by selecting. items from the palette, positioning them on the view and connecting them together. Before allowing two items to be connected together, the environment checks the correctness of the syntax and displays an error message if the items cannot be connected e.g.,Ž if one tries to relate a variable with another variable .. At creation time, a dialogue asks the modeller to define the item’s properties such as its name, its indices, etc. Once created, items can be edited, moved around the view without loosing their connections, and deleted. Coefficients and RHS data are specified either manually or by reading the data from a file. Indices can be created using gW interface or read from a file. A gLPL model with indexed elements gives the overall structure of a problem. To see more details, users can disaggregate elements, that is, instantiate one or more indices. Given the number of elements, a model view can become quite messy. Various options, such as ‘Hide RHS’ or ‘Create Local Map’, are provided in the ‘View’ menu to control the amount of detail shown. It is beyond the scope of this paper to present all the possible user interactions and the different steps of the creation of a gLPL model. Ref. 11 gives a complete list of the<sup>w</sup> <sup>x</sup> user interactions as well as a list and a short description of the gLPS specific commands. A gLPL model is created step by step in Ref. 10 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/9EUFKAS4/fulltext/images/a4e0528ecd8af5ffa167d7645290bde7a46d4f9364486dfcd4baba0c476ee175.jpg)  
Fig. 7. A gLPL model. This model is composed of two variables squares , three constraints circles and triangles and an objective function. Ž . Ž .

Our model is composed of two variables squares ,Ž . three constraints circles and triangles and an objec-Ž . tive function Fig. 7 . As with mathematical nota-Ž . tion, variables, coefficients and constraints can be indexed. The variable U identifies the quantities to be transported from the factory i to the distribution centers j. The variable V identifies the quantities to be transported from the distribution centers j to the customers k. The objective function obj, coupled with the coefficients $c _ { i , j }$ and $b _ { j , k } ,$ specifies that the overall cost has to be minimised. The constraints supply, distr and demand are self-explanatory.

To compute the optimal solution, a user chooses the ‘Solve’ option of the ‘gLPS’ menu. When a user issues the ‘Solve’ command, gW first converts the gLPL model into its LPL representation and then calls the LPL solver. The LPL representation and the results are displayed in new windows Fig. 8 . Note Ž . that these two new documents are completely integrated in gW; they can thus be saved on disk, used as nodes for a table of contents, and their text can be used for hypertext links. The LPL model is just a specialisation of a text document and can thus be edited, just like plain text. Since a LPL representation is a model though, it can be solved by issuing the ‘Solve’ command. As it can be seen in the left window, the SET, COEF and VAR parts of a LPL model define the elements of a LPL model, and the MODEL part defines the equations of the model. The notation used for the equations is very similar to the mathematical notation except from a few differences e.g., Ž Ý j is replaced by sum 4j .. The COEF part holds the data for each coefficient and RHS in the form: name $\AA / i n d i c e s = \AA < i n d e x _ { I } - i n d e x _ { n }$ Õalue <sup>)</sup>. With the values shown on the left of Fig. 8, the optimal solution calculated by the LPL solver is displayed in the right window.

## 3.2.3. Links

Within gW, each link’s start or end point i.e., aŽ block see Section 3.1.2 is displayed on the screen<sup>w</sup> <sup>x</sup>. as a black dot the size of a 12 point character. To jump from one location to another, users either double-click on the dot, or select it single click and Ž . choose the ‘Follow Link’ command from the ‘WEBSs’ menu. gW then displays the end point of the link. In Fig. 9 a new window containing the LPL code of the model focused on the variable V is displayed after the user double-clicked on the block whose extent is the variable V in the gLPL representation.

![](/api/attachments/9EUFKAS4/fulltext/images/bab3683264766c595091a5d0c45461508cf5dd4ead7cd40f5d916a8cb4ab9faf.jpg)  
Fig. 8. The LPL model and the solution document. After a user issues the ‘Solve’ command, gW generates two new windows containing the LPL model and the solution if any .Ž .

![](/api/attachments/9EUFKAS4/fulltext/images/461e5d7caceedf0a20699e15e7cbb927409ccc6b9d937ec087a11c023f9a1130.jpg)  
Fig. 9. Following a link. By double-clicking the black dot in the gLPL representation upper window , the end of the link is shown Ž . in the LPL model of the lower window.

## 3.2.4. Scripts

As stated in Section 3.1.3, scripts are either triggered or unbound. Unbound scripts are invoked by selecting them from a menu. Triggered scripts are launched automatically when a specific action is performed.

The script browser Fig. 10 provides access to allŽ . the scripts in an IS. It can be shown and hidden with the ‘Show Script Browser’ resp. ‘Hide Script Browser’ commands from the ‘Script’ menu.

The pop-up menu on the top left allows the user to select the type of script to visualise, either unbound or triggered. When ‘Unbound Scripts’ is selected in the pop-up menu, the left pane contains exactly one item, also named Unbound Scripts, which is automatically selected, and the right pane displays both unbound scripts’ name and scripts that have never been compiled successfully. If ‘Triggered Scripts’ is chosen in the pop-up menu, the left pane shows a list of objects to which scripts are attached. By choosing an item in this list, the attached scripts names are displayed in the right pane. The content of the script selected from the right pane list is displayed in the lower pane, where it can be edited.

Table 1 gives the complete script shown in the lower part of Fig. 10. This script looks for a gLPL element in the current gLPL model. The syntax of the scripting language is very similar to Pascal, including variable declarations and statements, with a few additions such as a dot notation to invoke methods on objects as in Object Pascal 41 andŽ <sup>w</sup> <sup>x</sup>. some loop constructs to repeatedly perform a given action or group of actions . A script consists of twoŽ . parts, the script header and the main block. For triggered scripts, the script header defines the object the script is attached to and the method that will trigger its execution. For unbound scripts, the script header only consists of the keywords ‘on execute’. The main block contains declarations of variables and a list of statements to be executed when the script is invoked. In Table 1, line 1 determines when this particular script has to be executed. Since this script is not attached to any object, line 1 only contains the statement ‘On execute’. Note that comments are given between brackets ‘ ’. Lines 2 to 64 declare variables that could be used throughout the main block. Lines 7 to 22 constitute the core of the script. Line 8 asks the user the name of the element to be looked for. Line 10 gets a reference to the current gLPL model. Line 13 gets the number of gLPL elements. Lines 15 to 18 scan through every element of the document until the searched element is found. Then, if the searched element is found, line 20 selects and displays it.

![](/api/attachments/9EUFKAS4/fulltext/images/820a0150052d572a8b57daea7a475adafea85a170d04c0c77167e029451092d3.jpg)  
Fig. 10. The script browser showing unbound scripts. The upper part shows the scripts’ names and type. The lower part allows the user to view and modify the content of the selected script.

```txt
The script of Fig. 10. This script finds a requested gLPL element in the current gLPL model
1 ON Execute; {Find gLPL element}
{variables declaration}
2 VAR nOfElements: INTEGER;
3 count: INTEGER;
4 element: gLPSElement;
5 mygLPSDoc: gLPSDocument;
6 name: STRING;
7 BEGIN
{ask the user the name of the element to be found}
{and if there is a name, start the search}
8 IF ReadString('Name of the element?', name, 'Give a name')
THEN
9 BEGIN
{get a reference to the current document}
10 mygLPSDoc: = AsUNIVObject(frontDocument);
11 mygLPSDoc.Select;
12 mygLPSDoc.DeselectAll;
{count the number of elements in the current document}
13 nOfElements: = mygLPSDoc.getNrOfEl;
14 count: = 1;
{look for the searched element}
15 REPEAT
16 element: = mygLPSDoc.At(i);
17 count: = count + 1;
18 UNTIL ((count <= nOfElements) OR (name <> element.GetElName));
{if the searched element is found, select and display it}
19 IF count <= numberOfElements THEN
20 element.SelectEl;
21 END;
22 END {Find gLPL element}
```

Such a script could be enhanced, for instance, by telling the user when no instances were found or by searching through all the gLPL models of an IS. 36 <sup>w</sup> <sup>x</sup> gives detailed information on scripts as well as other examples.

This section has defined and shown the interface of standard documents, models, links and scripts. These components are tightly bounded and constitute together the components of every IS.

Section 4 illustrates the use of gW as well as the interaction with our prototype IS for LP.

## 4. Prototype

This section illustrates gW by presenting a portion of the prototype IS for LP we created. The prototype contains several documents, models, links and scripts to help understand LP models. It also proposes several scripts to help potential builders extend the existing IS such as a script which creates a wholeŽ set of new documents gLPL model, terms, etc. forŽ . a new example ..

It is unfortunately not possible to describe at the same time, the work of the builder, the work of a reader, and all the documents, links and scripts we created. Therefore, after highlighting two important mechanisms we developed Section 4.1 , we chose toŽ . take a reader’s perspective and show several steps of her consulting process Section 4.2 . This journeyŽ . will give sufficient insights to acquire a global understanding of gW and its IS for LP. However, simulating a dynamic environment with explanations on paper can only be done to some extent a differ-Ž ent conclusion would be an unexpected outcome of this research . Therefore, we recommend that you try. gW by yourself. gW runs on Macintoshes with system software 7.0 or greater and is available by anonymous file transfer from ftp-iiuf.unifr.ch. The environment is in the directory ‘pub<sup>r</sup>softeng<sup>r</sup>gW’ and the IS for LP is in the directory ‘pub<sup>r</sup>softeng<sup>r</sup>gW<sup>r</sup>books’ under the names ‘optimisation.book’ and ‘optimisation’.

## 4.1. Basics

Scripts support a wide range of tasks, such as automatically creating a table of contents for all the examples of the IS, copying the documents and links of an example and so on. The potential of scripts is only limited by the user’s imagination. For example, one can create a script that automatically connects each decision variable of a gLPL or LPL model with its value in the optimal solution. In this subsection, we describe two concepts, document layout and document hierarchy, which could not have been realised without the help of scripts.

<table><tr><td>gLPL</td><td>Terms</td></tr><tr><td>Solution</td><td>Modeling</td></tr><tr><td colspan="2">Dashboard</td></tr></table>

Fig. 11. The layout of the example’s documents. This layout is used for every example in the IS for LP as in Fig. 16 for Ž example ..

![](/api/attachments/9EUFKAS4/fulltext/images/c648fc98bf67dbf0ff4dad5d5c5b43aee40b5d17f3a36a23f6e17718cabad079.jpg)  
Fig. 12. A hierarchy of documents. The associated pseudo-scrip specifies that closing any document closes all linked documents that are at a lower level in the hierarchy.

## 4.1.1. Document layout

Our prototype for LP is divided into three main parts: theory, examples and exercises. The layout of the different documents depends on which part the user is currently viewing. For the theory part, we always place text on the left and figures and graphics on the right. For the examples and exercises, we divide the screen into five distinct windows Fig.Ž 11 . The gLPL model is shown on the upper left, the. terms of the problem on the upper right, the explanation of the modelling process on the lower right and the values of the solution on the lower left of the screen. Furthermore, a window containing a dashboard is attached to each example. A dashboard, or anchor document, provides a starting point from which users can access example models. This dashboard is always displayed at the bottom of the screen. Note that a fifth window containing suggestions to the reader may sometimes be present. It then appears in the middle of the screen.

Before opening any example’s model, scripts always check, and possibly modify, the location of the model’s window. These scripts use what we call template documents. Template documents memorise the location at which builders want the different documents of an example to appear on the screen. Builders place on the screen one template document for each window of an example. Scripts then ensure

![](/api/attachments/9EUFKAS4/fulltext/images/cb33a19823b236ca96e6850f619dab11bc9f247844769b15337c6e38edc0a1d8.jpg)  
Fig. 13. The first two windows of an example. Opening a node from the table of contents of this IS always displays the example’s dashboard Ž . Ž . lower window and the terms of the problem upper window .

![](/api/attachments/9EUFKAS4/fulltext/images/4935c621d88556f04c210035d05b850e041e8096908c21226dba6b7df8b32a4a.jpg)  
Fig. 14. Following the gLPL link from the dashboard displays the gLPL model in the top left corner of the screen.

that, given the template document location, each example window is positioned at the right place. Note that such a script has less than 10 lines of code.

This mechanism ensures a consistent layout across all the examples and exercises of the IS and across different screen sizes. Furthermore, this mechanism allows the builder to modify the layout of every example just in modifying the template documents.

![](/api/attachments/9EUFKAS4/fulltext/images/0a5bd5d8b3e6644340482ae899987ee401d5184181fc51b95480682d781c3876.jpg)  
Fig. 15. Choice of the link to be followed. Double-clicking a block having several links brings up a dialogue where users choose the link they want to follow.

![](/api/attachments/9EUFKAS4/fulltext/images/ccb7d97560e35822a2791d173a3a04ef54e830ad3867f42a95b08eef13fb3a30.jpg)  
Fig. 16. Following the modelling link attached to the variable V opens a new window.

Note that these template documents are also used when a builder creates a new example with theŽ script ‘New example’ . This script generates auto- . matically a collection of empty documents and places them on the screen according to the templates the builder gave. In addition, this script also adds an entry in the table of contents and creates the appropriate links between the documents and the anchor document.

## 4.1.2. Document hierarchies

In a hypertext environment, documents are often linked together in many ways without a specific structure. Making them rely on others could be useful. For instance, a builder might want to prevent the opening of a document if another document has not yet been read. Builders could also create a script to specify that closing a document closes a specific collection of related documents. A straightforward way would specify the name of every document that relies on a given document. However, given the number of documents and the number of dependencies in an IS, this would quickly become tedious.

![](/api/attachments/9EUFKAS4/fulltext/images/bb4a383c6783990e508be1fdd1ad924a47bb669e2f658f78d839c3626c12edf5.jpg)  
Fig. 17. The disaggregation dialogue box. Users choose in this dialogue the level of disaggregation of a selected element, in this case, $V _ { j , k }$

Another, more general procedure must be found. We introduce the notion of hierarchies of documents. When linked documents depend on others, a hierarchy and a script are created. The script specifies the action to be accomplished and the hierarchy defines the interdependence of the linked documents. In Fig. 12, document B is at level I, documents K, L at level II and documents U, V, W, X at level III. The pseudo-script specifies that closing any document in the hierarchy implies that all the documents that are below will also be closed; closing document K will close documents U and V. In order to make a new document rely on another, the builder just has to attach the new document to the proper location in the hierarchy.

![](/api/attachments/9EUFKAS4/fulltext/images/b11d09a109a5fbb8f5005a8036f61850626220880ae91bfdeba5ecddc3d6a7d9.jpg)  
Fig. 18. Some disaggregations. The upper part shows the gLPL model as originally created by the builder. The lower part shows three of its instantiations.

## 4.2. Tracy’s session

## 4.2.1. Step 1: Opening an example

After having started the application, given her user name and selected the IS for LP ‘optimisation’ ,Ž . Tracy sees the table of contents created by the builder Fig. 6 . Since she already has some notionsŽ . of LP, she discards the theory part of the IS and concentrates her exploration on the models. She is particularly interested in the Transport model and decides to explore it. She thus opens it by clicking twice on the Transport node. Two new windows appear on the screen Fig. 13 . The upper windowŽ . contains the terms defining the problem and the lower window contains the example’s dashboard. The dashboard includes five blocks that link to the documents of the example, plus two blocks that link to help documents; one on gLPL and one providing a general help.

She reads the terms of the problem and tries to build the gLPL model. Building a gLPL model includes the creation of a new gLPL document, the creation of indices and elements, and the specification of the data. She then decides to see the gLPL model given by the builder.

## 4.2.2. Step 2: Opening the gLPL model

She selects the dashboard and follows the link to the gLPL model by double-clicking the corresponding block. She obtains a new window showing the model in the top left corner of the screen Fig. 14 .Ž . Note that this document layout remains the same between all examples and regardless of the screen size see Section 4.1.1 .Ž .

In order to understand the meaning of the variable V, she decides to follow the link attached to it.

## 4.2.3. Step 3: Exploring a Õariable

She double-clicks on the corresponding block and obtains the dialogue shown in Fig. 15. This dialogue gives her the choice of the link she wants to follow. The first link opens the solution document and the second link opens the modelling document. She chooses to follow the modelling link and a new window, explaining the elements of the model, is displayed on the screen Fig. 16 .Ž .

This explanation incites Tracy to look for the transportation costs of the variable V.

## 4.2.4. Step 4: More exploration

To see, and modify, the transportation costs of $V _ { j , k }$ , she could select the coefficient line $( c _ { j , k } )$ and choose the ‘Data’ option of the ‘gLPS’ menu. A table would then appear in a dialogue letting her see and modify the values. Another option is to disaggregate the variable. She thus selects the variable V, chooses the ‘Disaggregate’ option of the ‘gLPS’ menu, and clicks the ‘Select All’ button in the appearing dialogue Fig. 17 . Ž .

The lower left part of Fig. 18 shows the result of this disaggregation. Note that gW does not propose any layout algorithm; disaggregated elements are simply positioned to the right of the parent element. Tracy has now a direct access to the transportation costs of $V _ { j , k } .$ . Coefficients and right hand sides hold the data of the model. They can be browsed and

![](/api/attachments/9EUFKAS4/fulltext/images/b44e82a07a4d2cd95218657dc59d9863c26a6c8e5de582ce404b1eb967879f37.jpg)  
Fig. 19. A restricted disaggregation. The disaggregation will proceed with only one index Ž . k , and only for k <sup>s</sup> 1.

![](/api/attachments/9EUFKAS4/fulltext/images/abd1fc07d099b3742d78ee4e6df1b204c8a34def4fc4375c9c35f28ecbab6a06.jpg)  
Fig. 20. This dialogue box allows users to choose a script they want to execute.

modified at every level of disaggregation. In the lower left part of Fig. 18, for instance, the transportation cost between X and 1 is instantly visible $( b _ { k , 1 }$ <sup>s</sup>5. and could thus be modified directly. If the values are not displayed on the graph, i.e., the element is not fully instantiated, a dialogue displays a table where the values can be modified. To explore a specific variable or a group of specific gLPL elements, the disaggregation process could also be restricted. The lower right part of Fig. 18 shows two successive restricted disaggregations. First, the first element of the index k kŽ . <sup>s</sup>1 for the variable V and the constraint demand has been instantiated Fig.Ž 19 . Then, the resulting variable. $V _ { j , I }$ has been disaggregated further.

Now that Tracy has a better understanding of the variable V, she decides to add her own explanation of variable.

## 4.2.5. Step 5: Creating an annotation

She first selects the variable V in the model. Then, she executes the script ‘Create annotation’ from the list of available scripts Fig. 20 —dis- Ž . played by choosing the ‘Execute Other Script’ item of the ‘Script’ menu.

gW then opens her personal annotation document and creates a link between the selected variable Ž . V and this document. She can now add her own comments Fig. 21 .Ž .

Now that she has a better understanding of the model, she decides to experiment with it. Note that since readers are not allowed to modify builders documents these documents are available to allŽ readers , Tracy must first copy the gLPL model. She . can either copy the given gLPL model into a new document with the ‘Copy–Paste’ commands, or use the ‘Save $\mathrm { A s } '$ command to create a copy of the current model, or use the script ‘Copy example provided by the author. This script not only copies all the documents of one example into a dedicated folder but it also copies all the links between the example’s documents.

![](/api/attachments/9EUFKAS4/fulltext/images/df9b4490bfb3d562f0b501c4529c6a45f3f9e15967c7119c9ab0ecb8bc707035.jpg)  
Fig. 21. Tracy’s annotation document. Using the ‘Create annotation’ script, users can automatically link any part of the IS to their persona annotation document. Note that, in future sessions, since Tracy created a new link, the dialogue box of Fig. 15 will then propose 3 links.

![](/api/attachments/9EUFKAS4/fulltext/images/47743c7969fefd777ad39d1063765e267a0737e64ca28dcbb641d7a943d560ee.jpg)  
Fig. 22. A new optimal solution. Given the new values on the left, gW computes the new optimal solution displayed on the right.

## 4.2.6. Step 6: Experimenting with the model

She wants to see how the modification of customers’ demand could affect the optimal solution. She thus disaggregates demand , gives new values to the right hand sides and compiles the new model by selecting the ‘Solve’ option of the ‘gLPS’ menu.

The new optimal solution along with the values Tracy entered are displayed in Fig. 22.

All the windows that she has opened become to clutter her screen. She thus decides to clean it.

## 4.2.7. Step 7: Reducing screen clutter

She can close all the windows of the example simply by closing the associated dashboard Fig. 23 .Ž .

All the documents of the example have been added by the builder to a specific hierarchy, with the dashboard being at the outermost level SectionŽ 4.1.2 . Closing the dashboard thus closes all the. other documents of the hierarchy, that is, all the documents of the example. Her screen now shows her personal annotation document, her version of the gLPL model and all the documents resulting from the solving of the model. To finally clean the screen, she can use the script ‘Close all documents’ provided by the builder. gW asks her if she wants to keep the modifications. If necessity, gW stores blocks and links in the database, and saves the new documents.

![](/api/attachments/9EUFKAS4/fulltext/images/1970bc5f709cf1e7aaf494a6714b9294da7e6f27717f7300789ce774740d1a03.jpg)  
Fig. 23. Closing an example dashboard. Clicking the top left box of a dashboard window closes the dashboard as well as all of the documents in the example.

## 4.2.8. Step 8: Terminating the work

She selects the ‘Quit’ item of the ‘File’ menu.

In this session, we have shown how the components documents, models, links and scripts interactŽ . to help a reader understand LP modelling. Although presented through a reader’s perspective, these components are available to any user of the environment, be he a reader or a builder.

## 5. Future developments

In this paper, we have presented both an environment allowing the creation of information spaces for linear programming and a prototype of its use. At present, the information space prototype mainly consists of several scripts and models, each model being associated with documents containing their respective terms, explanations and suggestions. In order to be fully functional, we plan to supplement our information space with new models and new theory documents, dealing with linear optimisation in general, as well as LPL and gLPL. There is also much room for improvement for gW itself, and future developments could explore at least the following issues.

–Scripts are a valuable aid in the gW environment but creating new scripts is not always easy. In order to reduce the work of any builder, the number of existing scripts should be extended. In addition, in the current implementation, scripts acting directly on gLPL models and gLPL elements are rather limited. Providing more actions, such as a ‘move gLPL element’ command, which could be used in a layout script of a gLPL model, would improve the environment.

–Our environment suffers from early implementation choices. Given present standards, showing start and end link points as underlined text, as is done in the World Wide Web WWW , or coloured boxedŽ . areas in pictures would have been a better choice.

–Like other environments that attempt to integrate multiple model representations for example,Ž GIN 44 , gW supports two modelling languages.<sup>w</sup> <sup>x</sup>. While a step in the right direction, the use of more than two different model representations could be even more helpful. See MIMI<sup>r</sup>G 30 for an exam-<sup>w</sup> <sup>x</sup> ple, and Ref. 1 or Ref. 31 for some work and<sup>w x</sup> <sup>w</sup> <sup>x</sup> discussions along those lines.

–Our implementation is limited to the Macintosh operating system. In this regard, the work of Bhargava et al. 3 , who investigate the possibilities of <sup>w</sup> <sup>x</sup> using decision support services over WWW is of great interest, since browsers for the Web are available for all common operating systems the Ž DecisionNet WWW page is at: http:<sup>rr</sup> dnet.sm.nps.naÕy.mil <sup>r</sup>..

–Similarly, the use of Java, a language that allows programs to be run independently of the operating system, is of great interest. We are currently investigating this option and a first limited version of a gLPS modelling tool is available at: http:<sup>rr</sup>wwwiiuf.unifr.ch<sup>r</sup>groups<sup>r</sup>sde<sup>r</sup>users<sup>r</sup>collaud<sup>r</sup>gLPL\_ JaÕa.html.

From a broader perspective, this research may be seen as exploring the application of computer technology to help use OR techniques more effectively. It is our hope that our environment, through the use of hypertext, scripts and multiple model representations, will help people understand linear optimisation and modelling languages. gW, as well as our information space prototype, is currently being tested with advanced OR students at the Institute of Informatics of the University of Fribourg. Although further investigation is in progress, the preliminary responses are encouraging.

## Acknowledgements

The author would like to thank Prof. Christopher V. Jones for his helpful guidance during the redaction of this paper and Prof. Jacques Pasquier for his insightful comments. This research has been partially supported by Swiss National Science Foundation Grant 11-37219.93.

## Appendix A

## A.1. A gLPL

Every LP consists of at least one variable, one constraint and one objective function. Withing gLPL, these elements are represented by the following symbols:

![](/api/attachments/9EUFKAS4/fulltext/images/7716e439ed605adfd0fc07616091ff482038b34db454267c89cea7ed78873b7a.jpg)  
Fig. A.1. Standard formulation of a general LP model.

The square designates a variable (e.g. the quantity of robots of a given type to be produced).

The circle, associated with the square(s), refers to the left hand side (LHS) of a constraint or to an objective function. It can be labelled in different ways, depending on its type : '≥', '≤', '=', 'Min' or 'Max'.

∇ The triangle represents the right hand side (RHS) of a constraint and contains the associated data. ①

G Value The coefficient line always relates a square and a circle and, therefore, is used to define a part of either a constraint LHS or an objective function. It contains the associated data

The RHS line always relates a triangle and a circle, thus defining a constraint RHS.

gLPL is a direct translation of the classical mathematical notation Fig. A.1 . As in the mathematicalŽ . notation, the constituting elements of a gLPL model can thus have indices. Fig. A.2 illustrates a con-

![](/api/attachments/9EUFKAS4/fulltext/images/58a2b5e62f22f4ad01e84bbadad169fa0319aa6bdf0731df5275cf11c2a18181.jpg)  
Fig. A.2. A gLPL constraint.  
Table 2

Function compileToLPL: write ‘SET’ to output for every indice in the list of indices of the model: write its name and its sub-indices to output write ‘COEF’ to output for every triangle or coefficient line in the model: write its name, its indices and data to output write ‘VAR’ to output for every square in the model: write its name and its indices to output write ‘MODEL’ to output for every circle in the model start: write its name, its indices and ‘:’ to output for every square connected to this circle: write coefficient name, square name and indices to output write circle type to output write connected triangle’s name to output end every circle do almost the same for the objective function write ‘END’ to output

straint from the example in Section 3.2.2 usingŽ . indices and the above symbolism.

## Appendix B. Conversion from gLPL to LPL

Table 2 shows in pseudo code the process of translating the gLPL representation into the LPL representation.

## References

<sup>w</sup> <sup>x</sup> 1 D. Baldwin, Exploring Multiple Views: Examples from Accounting, Mathematical Modeling and Systems Analysis, unpublished, Department of Accounting, Virginia Polytechnic Institute and State University, 1992.

<sup>w</sup> <sup>x</sup> 2 H.K. Bhargava, M. Bieber, S.O. Kimbrough, Oona, Max, and the WYWWYWI Principle: Hypertext and Model Management in a Symbolic Programming Environment, Proceedings of the Ninth International Conference on Information Systems, Minneapolis, MN, December 1988.

<sup>w</sup> <sup>x</sup> 3 H.K. Bhargava, R. Krishnan, D. Kaplan, On Generalized

Access to a WWW-based Network of Decision Support Services, Proceedings of the Third ISDSS Conference, Hong Kong, June 1995.

4 M. Bieber, S.O. Kimbrough, On generalizing the concept of hypertext, MIS Quarterly 16 1 1992 77–93.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 J. Bisschop, R. Entriken, AIMMS The Modeling System, Paragon Decision Technology, Haarlem, The Netherlands, 1993.

<sup>w</sup> <sup>x</sup> 6 A. Brooke, D. Kendrick, A. Meeraus, GAMS a User’s Guide, Scientific Press, Redwood City, CA, 1988.

<sup>w</sup> <sup>x</sup> 7 K. Chari, T. Sen, GBMS<sup>r</sup>SM: a Graphical Modeling Environment, Working Paper, Dept. of Information and Decision Sciences, James Madison University, Harrisonburg, VA, USA, 1995.

<sup>w</sup> <sup>x</sup> 8 Chesapeake Decision Sciences, MIMI: Manager for Interactive Modeling Interfaces: User’s Manual, New Providence, NJ, 1993.

<sup>w</sup> <sup>x</sup> 9 J. Choobineh, A diagramming technique for representation of linear programming models, Omega 18 1 1991 43–51.Ž . Ž .

<sup>w</sup> <sup>x</sup>10 G. Collaud, Modelisation et optimation lineaire, un systeme´ ´ \` graphique de creation et de gestion des modeles gLPS , PhD´ \` Ž . Thesis, Fribourg, Switzerland, 1993.

<sup>w</sup> <sup>x</sup> 11 G. Collaud, gLPS for WEBSs User’s Guide: Creating, Documenting and Solving LP Models, Internal publication 94-13, Institute of Informatics, University of Fribourg, Switzerland, 1994.

<sup>w</sup> <sup>x</sup> 12 G. Collaud, J. Pasquier, gLPS: a graph-based system for linear problem modeling, in: T. Hurlimann Ed. , Modeling ¨ Ž . Tools for Decision Support, University of Fribourg Series in Computer Science 2, 1993, 83–100.

<sup>w</sup> <sup>x</sup> 13 G. Collaud, J. Pasquier, gLPS for WEBSs: A Scriptable Object Oriented Hypertext System for Learning Linear Optimisation, LEARNTEC’94 Europaischer Kongress fur Bil- Ž ¨ ¨ dungstechnologie und betriebliche Bildung , Tagungsband, . Uwe Beck and Winfried Sommer Hrsg. , Springer, Berlin, Ž . 1995, 309–319.

<sup>w</sup> <sup>x</sup> 14 G. Collaud, J. Pasquier-Boltuck, gLPS: a graphical tool for the definition and manipulation of linear problems, European Journal of Operational Research 72 2 1994 277–284.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 J. Conklin, Hypertext: An introduction and survey, IEEE Computer 2 9 1987 17–41.Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 R. Fourer, D.M. Gay, B.W. Kernighan, A modeling language for mathematical programming, Management Science 36 5Ž . Ž .1990 519–534.

<sup>w</sup> <sup>x</sup> 17 A.M. Geoffrion, Computer-based modeling environments, European Journal of Operational Research 41 1989 33–43.Ž .

<sup>w</sup> <sup>x</sup> 18 A.M. Geoffrion, The SML language for structured modeling: Levels 1 and 2, Operations Research 40 1 1992 38–57.Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 A.M. Geoffrion, The SML language for structured modeling: Levels 3 and 4, Operations Research 40 1 1992 58–75.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 F. Glover, D. Klingnan, N. Phillips, Netform modeling and applications, Interfaces 20 4 1990 7–27.Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 H.J. Greenberg, F.H. Murphy, A comparison of mathematical programming modeling systems, Annals of Operations Research 38 1992 177–238.Ž .

<sup>w</sup> <sup>x</sup> 22 F.G. Halasz, Relections on notecards: Seven issues for the

next generation of hypermedia systems, Communications of the ACM 31 7 1988 836–855.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 S. Hamacher, P. Dejax, L. Lustosa, P. Hamacher, A Diagram Representation for Conceptual Models of Operations Research Problems, Cahiers d’Etudes et de Recherche No. 93-04A, Laboratoire Productique Logistique, Ecole Centrale Paris, France, 1994.

<sup>w</sup> <sup>x</sup> 24 T. Hurlimann, J. Kohlas, LPL: A structured language for¨ linear programming modeling, OR Spectrum 10 1988 55–Ž . 63.

<sup>w</sup> <sup>x</sup> 25 T. Hurlimann, LPL: A mathematical programming language, ¨ OR Spectrum 15 1993 43–55.Ž .

<sup>w</sup> <sup>x</sup> 26 C. Jones, An introduction to graph-based modeling systems: Part I. overview, ORSA Journal on Computing 2 2 1990Ž . Ž . 136–151.

<sup>w</sup> <sup>x</sup> 27 C. Jones, An introduction to graph-based modeling systems: Part II. Graph-grammars and the implementation, ORSA Journal on Computing 3 3 1991 180–206.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 C. Jones, Attributed graphs, graph-grammars, and structured modeling, Annals of Operations Research 38 1992 281–324.Ž .

<sup>w</sup> <sup>x</sup> 29 C. Jones, Visualization and Optimisation, ORSA Journal on Computing 6 3 1994 221–257.Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 C. Jones, T.E. Baker, MIMI<sup>r</sup>G: a graphical environment for mathematical programming and modeling, Interfaces 26 3Ž . Ž . 1996 90.

<sup>w</sup> <sup>x</sup> 31 D. Kendrick, Parallel Model Representation, Expert Systems with Applications 1 4 1990 383–389. Ž . Ž .

<sup>w</sup> <sup>x</sup> 32 P.C. Ma, F.H. Murphy, E.A. Stohr, A graphics interface for linear programming, Communications of the ACM 32 8Ž . Ž .1989 996–1012.

<sup>w</sup> <sup>x</sup> 33 J. Monnard, J. Pasquier, An Object-Oriented Scripting Environment for the WEBSs Electronic Book System, in Proceedings of the ACM Conference on Hypertext ECHT’92, ACM Press, 1992, 81–90.

<sup>w</sup> <sup>x</sup> 34 J. Monnard, J. Pasquier, WEBSs: an Electronic Book Shell with an Object-Oriented Scripting Environment, in: N. Magnenat Thalmann, D. Thalmann Eds. , Virtual Worlds andŽ . Multimedia, Wiley, 1993.

<sup>w</sup> <sup>x</sup> 35 J. Monnard, A User’s Guide to the Woven Electronic Book System with Scripts, Working Paper 207, Institute of Informatics, University of Fribourg, Switzerland, 1993.

<sup>w</sup> <sup>x</sup> 36 J. Monnard, WEBSs, un environnement de scriptage pour hypertextes, PhD Thesis, Institute of Informatics, University of Fribourg, Switzerland, 1993.

<sup>w</sup> <sup>x</sup> 37 J. Pasquier-Boltuck, G. Collaud, J. Monnard, An Object-oriented Approach to Conceptualising and Programming an Interactive System for the Creation and Consultation of Electronic Books, in: J. Pasquier Ed. , Electronic Books andŽ . their Tools, Lang, New York, 1992, 23–38.

<sup>w</sup> <sup>x</sup>38 J. Pasquier-Boltuck, J. Monnard, Livres electroniques, De´ l’utopie a la realisation, Presses Polytechniques et Universi- \` ´ taires Romandes, Lausanne, Switzerland, 1995.

<sup>w</sup> <sup>x</sup> 39 S. Raghunathan, An Intelligent DSS for Model Formulation, Working Paper, University of Pittsburgh, KS, USA, 1987.

<sup>w</sup> <sup>x</sup> 40 L.S. Rosenstein, D. Shafer, D.A. Wilson, Programming with MacApp, Addison-Wesley, 1990.

<sup>w</sup> <sup>x</sup> 41 K.J. Schmucker, Object-Oriented Programming for the Macintosh, Hayden Book, 1986

42 L. Schrage, Linear, Integer, and Quadratic Programming with LINDO, Scientific Press, Palo Alto, CA, USA, 1986.

<sup>w</sup> <sup>x</sup> 43 D. Steiger, R. Sharda, LP Modeling Languages for Personal Computers: A Comparison, unpublished, College of Business Administration, Oklahoma State University, 1991.

<sup>w</sup> <sup>x</sup> 44 D. Steiger, R. Sharda, B. LeClaire, Graphical interfaces for network modeling: A model management system perspective, ORSA Journal on Computing 5 3 1993 275–291.Ž . Ž .

<sup>w</sup> <sup>x</sup> 45 A. Van Dam, Hypertext ’87: Keynote address, Communications of the ACM 31 7 1988 887–895.Ž . Ž .

Gerald Collaud is currently a researcher at the Center New´ Technologies and Higher Education at the University of Fribourg —Switzerland. He received his PhD in computer science in 1993 from the University of Fribourg. He also holds a master degree in economics. Dr. Collaud spent 18 months at Simon Fraser University where he worked on visual representations, especially of the WWW. His research interests include graphical representations, hypertext and hypermedia, object oriented programming and distance education.
