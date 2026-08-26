---
otero_id: 17123
otero_key: "87XBF8WW"
title: "Model visualization: Graphical support for DSS problem structuring and knowledge organization"
authors: "William E. Pracht"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90011-f"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Model Visualization: Graphical Support for DSS Problem Structuring and Knowledge Organization

William E. PRACHT

The Fogelman College of Business and Economics, Memphis State University, Memphis, TN 38152, USA

Model visualization is proposed as an approach for business problem model development and use within a Decision Support System environment. The goal of model visualization is to allow the model builder/user to form clear mental images of a model's structure and function. A model visualization system is a display-based system that: (1) is designed for implementation in a managerially-friendly, interactive problem solving environment; (2) supports the creative task of discovering and modeling the structure of a complex problem; (3) provides the capability for modeling the behavior of a system through time and (4) may serve as the basis for the incorporation of heuristic rules appropriate for model-based reasoning procedures. Efforts are currently underway to design, develop, and implement a prototype model visualization system in Smalltalk/V.

Keywords: Model Visualization, Business Problem Modeling, Interactive Problem Solving, Interactive Graphics, Frames, Frame-based Knowledge Representation, Knowledge Organization, Problem Structuring.

![](/api/attachments/87XBF8WW/fulltext/images/c6d8ded1a28e4cb9761c79f16ac58d183d17f0e5f251ca7f43e8bf3dd3d93112.jpg)

William Pracht is presently an Associated Professor of Management Information Systems in the Fogelman College of Business and Economics at Memphis State University. He received a Ph.D. in Business Administration (Management Information Systems) from Texas Tech University in 1984. His experience includes positions of Numerical Fluid Dynamics Researcher at the Los Alamos National Laboratory, Systems Analyst and Visiting Assistant Professor at

Texas Tech University, and participant in the U.S. Army Summer Faculty Research and Engineering Program. His research interests include decision support systems, business expert systems, knowledge management systems, and the design and development of user-oriented interactive graphics systems. He has published in Decision Sciences, Decision Support Systems, IEEE Transactions of Systems, Man and Cybernetics, the Journal of Computational Physics, the Journal of Geophysical Research, and Physics of Fluids. He is a member of the Association of Computing Machinery, American Association for Artificial Intelligence, IEEE Computer Society, the Society for Information Management, and the Decision Sciences Institute.

## 1. Introduction

The current state of research and practice in decision support systems (DSS) provides the potential for adequate support in the information retrieval and problem analysis phases of decision-making efforts. However, much less support is offered for what perhaps are more critical phases of decision making: problem structuring and formulation. Problem structuring and formulation involve postulating what the elements or variables in a problem are and how these elements fit together and interact. Management researchers have placed far more emphasis on problem solving than on problem structuring [12]. As a result, DSSs typically provide an assortment of data retrieval techniques, pre-defined decision models, and analytical procedures but no tools to directly support problem structuring. These systems do indeed assist in the solution of decision problems, provided that the decision maker knows – a priori a fixed set of decision alternatives and is faced with the well-structured task of choosing the “correct” one. In many circumstances, the DSS requires the problem solver: (1) to already know what the problem is, and (2) to make the problem fit the available decision model or solution procedure. The following observation expresses the problem in terms of the focus of DSS design efforts: “The imposition of structure upon aspects of managerial problem solving rather than the discovery of a manager’s preexisting mental organization of a task has been the mode favored by most designers of DSS” [8, p. 206].

What is needed is a DSS modeling component that: (1) provides managers with the capability to participate in structuring the characteristics of the model they use; (2) provides a form of user-system communication that more closely matches the user's "mental model" terminology; (3) can be used by managers who are knowledgeable in their particular fields of expertise but have limited computer experience; and (4) allows managers to explore alternatives to decisions within a display-based, interactive computing environment.

Research in human memory and imagery [11,17,18,19,23] suggest the importance of images in problem solving, especially in the early, problem structuring phases. Our contention is that a decision modeling approach based upon the computer's capability for retaining and displaying images will provide a more natural means for capturing the way experts conceptualize problem situations. If this is so, then an image-based approach would offer considerably more potential for assisting in problem structuring and knowledge organization than text or formula-based systems. Research on knowledge representation in artificial intelligence [5,15] provides a means for working more directly with real-world concepts (most easily communicated in terms of images) in computer modeling. Research involving the use of expert systems concepts in the design of DSS [27] suggests the importance of integrating techniques for manipulating symbols (most easily communicated in terms of images) along with quantitative data. Our aim is to meld concepts from AI knowledge representation, expert systems related to DSS design issues, and business problem modeling to achieve a more integrative, adaptable, and user-oriented DSS component to support a wide range of problem solving tasks – from problem formulation to problem analysis.

The purpose of this paper is to propose a framework based on the concept of model visualization. By model visualization we mean a methodology which permits the interactive graphical display of model components; problem-domain level knowledge embodied within the model, relationships among model components; and model execution results. This approach promises to provide a DSS component that: (1) is designed for implementation in a managerially-friendly, interactive problem solving environment; (2) supports the creative task of discovering and modeling the structure of a complex problem: (3) provides the capability for modeling the behavior of a system; and (4) will serve as the basis for the incorporation of heuristic rules appropriate for model-based reasoning procedures.

The next two sections give brief discussions about the need for graphics support in business problem modeling and problem structuring. Next is a section that discusses a knowledge representation scheme that provides the capability for modeling the structure and behavior of a problem situation. Finally, the architecture of a model visualization prototype system is presented and its application illustrated by demonstrating the development and use of a simple profit model.

## 2. The Need for Graphical Support in Business Problem Modeling

Traditional use of modeling in decision making frequently involves making the problem fit the solution procedures rather than having the problem at hand dictate the use of a particular model [8, p. 206]. As a consequence, the user need only to concentrate on collecting and specifying descriptive information for the pre-defined model. (S)he need not be concerned with procedural information, which remained fixed, embodied within the model and inaccessible to the user. In a certain sense, this approach serves to structure the problem solving process and to guide the information gathering activities, since the choice of solution procedure has pre-determined the information needed to “solve” the problem. Unfortunately, the vast majority of unstructured problems faced by decision makers do not readily lend themselves to this type of parameterization.

An alternative approach to modeling offered by some DSSs provides a way of formulating interrelationships among the variables and specifying, to a limited extent, procedural information to be built into the model. These modeling languages provide various techniques to examine alternative solutions with respect to models representing particular systems. A manager might, for example want to do a “what if” or a “sensitivity” analysis. In this case, the user might wish to know what happens to the value of some quantity X, given a different value for quantity Y. A sensitivity analysis would answer the question, how sensitive is the value of X to changes in Y? Other model interrogations such as goal seeking and impact analysis are available in the more comprehensive modeling systems. Software supporting these models is available for both mainframe computers as well as microcomputers. Visicalc and Lotus 1-2-3 are examples of the spreadsheet-type modeling software available for microcomputers. The Interactive Financial Planning System (IFPS), Express, and Empire are instances of modeling languages for mainframe computers.

Modeling languages such as IFPS allow a user to set up a model that operates on a rectangular array of numbers representing characteristics of the financial picture over a series of time periods. The model consists of functions and relationships for calculating the numbers in the array. The principal advantage these languages provide is that they allow the user to specify procedural information for the model in terms more English-like than computer language-like. The modeler is able to specify procedural information for the model, telling it what to do (process oriented) without having to specify how to do it in computer terminology (procedure oriented). On the negative side, however, we note that the user communicates to the system in purely textual code and that the system reveals very little of its internal state to the user. The model builder must remember and manipulate a complex and abstract system structure with very little assistance from the computer in remembering how this system appears in its entirety.

Spreadsheet software remedies this situation somewhat by making use of graphics to show as much of the internal state as possible on the video display screen. Spreadsheets consist of rows and columns of cells, each of which can contain character strings, numbers, formulas, and functions. This software allows the user to work directly with the visual representation of the spreadsheet. Unfortunately, the true structure of the model in terms of elements and relationships between elements is not well represented by the spreadsheet format. A methodology for interactive model building that allows the model builder/user to manipulate model components directly must rely to an even greater extent on the use of interactive graphics.

## 3. The Need for Graphical Support in Problem Structuring and Knowledge Organization

It is well documented that the human brain is quite limited in its ability to process complex problems consisting of many variables and many interrelationships among variables [14,16,28]. One of the main purposes of a modeling component of a DSS is to provide a computer information processor which can maintain and manipulate models too complex for the human information processor to handle. Research in human memory, mental imagery and problem solving [9,11,17,18, 19,23,25,26] suggests that mental images and external representations are particularly useful during the early stages of problem solving (problem structuring).

In Greeno's theory, for example, when a person is presented with a problem to solve, (s)he first attempts to gain an understanding of the problem. He states that “...when the problem is understood, the subject has assimilated a structural network that represents the main relationships among the elements of the problem” [9, p. 106]. This structural network acts as the theoretical construct representing the way the subject organizes problem knowledge. This concept can be stated in a slightly different way: “Sketches, diagrams, and drawings are ways of generating representations that relate a problem directly to an individual’s knowledge of the world. They help reveal inconsistencies in this information and also serve as a set of external memory structures” [30, p. 621]. Understanding the structure of a complex problem is directly related to the process of constructing some sort of internal or mental model of the system. A visually-oriented form of problem representation of the computer information processor tends to more efficiently activate related knowledge stored in long-term memory of the human information processor. Consequently, the user can more readily apply this knowledge to a new or related problem situation [30, p. 623].

Images represent the user's mental model of a problem domain. If the visual constructs of these images are given precise meaning, the user's knowledge can be captured and stored in a knowledge base. If the user is provided with a way to work directly with a visual representation of the model or knowledge, then the power of the computer can be applied to knowledge structuring and acquisition in a manner more closely resembling the natural thought process.

The oldest and most well known graphical representation scheme for representing knowledge is the semantic net, which grew out of Quillian's work on semantic memory models [24]. A semantic net is composed of a collection of nodes and arcs. The nodes represent objects and descriptors. Objects can be physical or conceptual entities and descriptors contain additional information. Sales is an example of a conceptual object; 'Sales Val' (the numerical value of Sales) is one descriptor of Sales. Links between nodes represent predicates or attributes that indicate relationships between the objects shown in the nodes. ImpactsUpon could be a link relating Sales to GrossProfit. Semantic nets offer a flexible and graphically understandable method for discovering and representing the structure of a problem domain. Work reported on earlier by the author [20,21] on graphical interactive structural modeling is closely related to the work on semantic nets. However, model visualization and model-based reasoning require a way of organizing knowledge into chunks or clusters which are larger than single nodes or links in a semantic network in order to avoid the "combinatorial explosion" that can occur in large knowledge base systems.

## 4. Frame-Based Knowledge Representation

Because of the limitations of the semantic net, the present approach adopted a related, object-centered view of knowledge representation based on frames [15]. In this scheme, knowledge is partitioned into discrete structures called frames. Each frame has a set of slots for holding clusters of related knowledge. Grouping related knowledge together has several advantages for a model visualization system: (1) the system structures information in a much more organized and manageable fashion; (2) the system comes closer to modeling the real-world problem domain; and (3) the system comes closer to mimicking the way human beings remember and reason about the world. These benefits are succinctly summarized as follows: "They capture the way experts typically think about much of their knowledge, provide a concise structural representation of useful relations, and support a concise definition-by-specialization technique that is easy for most domain experts to use" [5, p. 904]. This same notion, expressed somewhat differently is: "When one encounters a new situation (or makes a substantial change in one's view of a problem), one selects from memory a structure called a frame. This is a remembered framework to be adapted to fit reality by changing details as necessary" [15, p. 95]. Graphical displays of frame "windows" provide a natural and convenient means for users to visualize and interact directly with the model components.

![](/api/attachments/87XBF8WW/fulltext/images/75c95d154dd0958d8a4554320b4e0cd3b1ba6ef7a1708534abe1e67779845e36.jpg)  
Fig. 1. Partial Frame with Slots Containing Numerical Values, Calculation Procedures, Descriptive Information, Hypotheses, and Linkage Information.

Structuring the model around problem-domain objects or frames allows the model builder to talk directly about the knowledge to be built into the model. Problem domain-level knowledge embodied within the model is referred to [1] as knowledge abstraction and the capability of manipulating and using problem knowledge as knowledge programming. Frames provide a mechanism for knowledge abstraction; an image-based approach provides a natural means for knowledge programming. The frame shown in fig. 1 illustrates the type of information that can be stored in the frame slots. This frame, named RetOnNetWorth, is taken from the example used in the remainder of the paper to illustrate the application of the model visualization system for developing a model to assist in analyzing a company's financial performance. As indicated in the figure, these slots can contain frame relationship (linkage) information, graphical display information, numerical values, procedures for deriving numerical values (procedural attachments), descriptive information, rules, and hypotheses about a situation.

Frame-based systems provide a natural means for organizing information into structures. This organization takes place at two levels. First, knowledge is clustered in individual frames, as is indicated in fig. 1. The second way frame-based systems provide for knowledge organization is that frames may be logically linked or related to each other. Relationships can be grouped into three classifications [2, p. 416]: generalization, aggregation, and association. These relationships are examined in more detail in the next section.

## 4.1. Frame Relationships

Generalization relationships form hierarchies of kinds (as opposed to hierarchies of parts, described next). Hierarchies of kinds form the familiar object and organism taxonomies where lower levels are related to upper levels by class inclusion. This form of knowledge organization corresponds to one the most fundamental aspects of human thought: the ability to perceive similarities and differences in objects and organisms, and to thereby group or classify them. This classification enables humans to reduce the number of entities in a given problem scenario to manageable proportions. Hierarchies of kinds (taxonomies) also provide the basis for (1) the inference of properties of certain frames or entities from knowledge of the category of that frame; and (2) communication of properties of that frame in an economical manner. In a frame-based representation scheme, the generalization relation is referred to as an IsA KindOf relationship. An example is, Fixed-Expense IsA KindOf Expense.

Aggregation relationships from hierarchies of parts. The aggregate or IsAPartOf-type relationships serve to separate entities into their structural components and to provide a basis for organizing knowledge in terms of components of structure. Decomposing a system into parts is one way individuals attempt to understand the relationship of structure to function and of linking the world of appearance to the realm of action [29 p. 189, 190]. A significant difference between hierarchies of parts versus hierarchies of kinds is that IsAPartOf relationships do not allow inferences of properties. Return on total assets, for example, can be decomposed into net profit margin and asset turnover (this example is discussed in more detail in a later section of the paper). Another way to express these relationships is, ProfitMargin IsAPartOf RetOnAssets and AssetTurnOver IsAPartOf RetOnAssets.

These various frame relationships are useful in the problem structuring phase of model development. In many instances, the most important type of frame relationship is the aggregation relationship. This capability is especially useful in the early stages of model building because it provides a way to decompose the model into modules that exist in our mental model of reality and then to organize and structure knowledge so that it can be easily understood. This decomposition is made possible by the capability of frames to be composed of other frames.

An example of an application of this systems frame concept can be seen by noticing that the RetOnNetWorth frame shown in fig. 1 contains a slot called 'RetOnNetWorthProc'. The contents of this slot defines the procedure for calculating the numerical value of Return on Net Worth, contained in the slot named 'RetOnNetWorthVal'. The two terms found on the right-hand-side of this expression ('FinLeverageVal' and 'RetOnAssetVal') are actually contained in other frames, namely, FinLeverage and RetOnAssets, respectively. Links to these "subframes" are defined in slots called 'IsComposedOf'. These type of hierarchical relationships are referred to as IsComposedOf linkage, as in RetOnNetWorth IsComposedOf RetOnAssets and FinLeverage. Another related type of linkage information contained in frame slots is the IsAPartOf relationship, as in FinLeverage IsAPartOf RetOnNetWorth.

The benefits of such a relationships are that they enable the model developer to work at appropriate levels of abstraction. At any given level, all details of lower levels are hidden. Fig. 2 illustrates how this hierarchy of frames allows the user to work (from left to right) from higher level of abstraction to progressively lower levels. At each lower level in the hierarchy each frame contains more primitive objects. Finally, at the lowest level (not shown in the figure) frames describe data elements that would be either entered as "input" or be retrieved from a database.

![](/api/attachments/87XBF8WW/fulltext/images/bfe3841348acbe44f6131b7364d4d0473cba782a992c8e4389df513041abff7e.jpg)  
Fig. 2. Hierarchy of Frames Illustrating IsComposedOf and IsAPartOf Frame Relationships.

The object-centered, frame-based approach provides a convenient basis for direct user manipulation of frames and frame linkages, as will be explained in a later section. This capability, useful particularly in the early stages of problem structuring, is a natural outcome of using the object-centered paradigm because the paradigm also provides the basis for encoding and organizing image-based, user-interface constructs. Constructs such as interactive editors/browsers, graphical displays, multiple windows, and pop-up menus are essential for a truly user-oriented business problem modeling en environment.

## 5. Architecture of the Model Visualization Prototype System

As indicated in the preceding paragraphs, this paper proposes a DSS component designed to allow a model builder/user to form clear mental images of a model's structure and function and then assist in translating/transmitting this image to the computer model. Models are represented in the object-centered approach as a structured collection of communicating frames. Each object (or frame) has an internal state and an external, graphical representation. The model may undergo state changes and display dynamic behavior. Fig. 3 shows the framework for a graphics-based system that provides model builders/users with the capability for:

![](/api/attachments/87XBF8WW/fulltext/images/66f1f702addbac45f008959fe1bc6d627a25a448690d3ea7c7fcb5974e569c51.jpg)  
Fig. 3. DSS Architecture of the Proposed Model Visualization System for Problem Structuring and Knowledge Organization.

(1) modeling the structure of a problem situation; (2) defining the function and activities of the model components;

(3) executing and observing the dynamic behavior of the model; and

(4) deriving a set of rules for reasoning about the model.

We illustrate the discussion of the architecture of the model visualization prototype system with an example illustrating the need for tools to aid a manager of a manufacturing firm faced with the unstructured task of diagnosing the problem of decreasing profits. In this example, we assume that there may be some indications of problems evident from key elements of the firm's income statement and balance sheet, but no clear diagnosis of the problem is evident. We further assume that the manager has in mind, the conceptual notion of a model based on the DuPont Profit Model which captures key elements and combines them into a snapshot picture of the firm. The

DuPont Model was developed by the E. E. DuPont de Nemours Company in the early 1900's. Variations of this model, including the one in [10], which has been adapted for use in this paper, have been widely used as a diagnostic tool in business firms. The DuPont model provides some basis for structuring the problem, but the task of diagnosing the general problem of decreasing profits is by no means a structured task. A structured task is one for which clear rules can be defined, replacing the judgment of a decisionmaker. This is clearly not the case for the example at hand.

## 5.1. Structuring the Problem Domain

As in any problem-solving system, the user needs a representation of the problem situation and a language for describing the world as (s)he "sees" it. In the initial stages of the model development task, the user's first task is to develop the structure or framework for the model [13]. This activity consists first of identifying objects or conceptual entities of the problem environment being modeled. In the DuPont Profit Model, these abstract concepts or objects are such factors as; Return on Net Worth, Financial Leverage, Return

![](/api/attachments/87XBF8WW/fulltext/images/b09a9523ac7ce0bf74e83730bd384740d3b888c87083cf2a2c1167f616fb5090.jpg)  
Fig. 4. Developing a New Model Structure by Creating and Positioning Model Frames.

on Assets, Asset Turnover, Net Profit Margin and so forth. Typically, the objects identified in this step are nouns used in describing the problem space. During this problem structuring activity, the user communicates his or her representation of the problem to the system in terms of graphical representations of frames, as well as hierarchical relationships among frames. A graphics editor is used to create, edit, and view this model structure.

![](/api/attachments/87XBF8WW/fulltext/images/d3a00f19b2c00dc9cd1b2114c3243a8d121022d71e9897ecb324ed6099cc5da7.jpg)  
Fig. 5. Defining Linkage Functions. Functions are Defined in Frame Slots.

Fig. 4 illustrates the first few steps in developing the structural model for a new problem domain. The pop-up menu shown in the top left-hand corner indicates that the New Model selection has been highlighted, which produces the Profit Model work area. The pop-up menu on the right-hand side of this work area provides the functions for defining and manipulating the model frames to form the desired overall model structure. These frames are created by selecting the New Frame menu selection, positioning the cursor, and entering the new frame name. Only the frame name and location bullets are displayed during this phase of model construction. To complete the object-centered domain description of model structure requires the specification of additional frame information. This information, which is contained in frame slots, further defines each frame in terms of attributes, relationships (linkages), and interfaces for each frame. Fig. 5 illustrates how this process begins by first selecting a frame and then selecting the Frame Info option of the Frame Editing menu. This displays a work area for that particular frame, together with a Slot Editing menu for working with slots of the selected frame. Linkage information, slot names (attributes) and slot values may be entered directly into the work area. The frame work area, as well as the model work area, can be sized and moved about the screen to fit the model building needs of the user. In addition, the model area scrolls horizontally and vertically; the frame area scrolls vertically.

Slot values containing information about the 'IsComposedOf' and 'IsAPartOf' linkages are automatically entered by the system when the visual representation of frames are connected. For example, the relationship, RetOnAssets IsAPartOf RetNetWorth is established when the frames are connected by the following sequence of steps: highlight the Links To menu selection, move the cursor to the FinLeverage frame location, signal the system with a mouse click or other function key so defined, move the cursor to RetNetWorth, and once again signal the system. This process connects the two frames, enters the appropriate frame information into frame slots 'IsAPartOf' and 'IsComposedOf'.

This step in constructing the structure of the problem is critical for the model building effort, since the set of model formulations defines the dimensions of the functional problem space in which the decision maker (and ultimately the expert system component to reason about the model) searches for a diagnosis.

## 5.2. Defining the Model Functions

Once the basic structure is completed, the user must identify the functions and activities that will determine the model's behavior. In this step the model builder defines the operations to be performed on each frame and by each frame. The language for these procedures involves familiar mathematical and logical expressions, but is imbedded within the graphical representation of the model and completely accessible and understandable to the model builder.

The procedure for defining frame functions and activities follows the concept of top-down decomposition noted in an earlier section. The hierarchical organization of frames allows the model builder to work, at first, with the highest level of abstraction, ignoring lower levels of detail until later. In the Profit Model example, the highest level of abstraction is expressed as a percentage of net worth (Return on Net Worth) and serves as the first key indicator of profitability. Decomposing Return on Net Worth into its component parts yields the second level of abstraction, which indicates that Return on Net Worth is made up of Return on Total Assets and Financial Leverage, as shown in the expressions given below.

Return on Net Worth

= Financial Leverage × Return on Total Assets

$$
\text { or } \frac {\text { Net   Profit }}{\text { Net   Worth }} = \frac {\text { Total   Assets }}{\text { Net   Worth }} \times \frac {\text { Net   Profit }}{\text { Total   Assets }}.
$$

In this second level of abstraction, we see that a low value of Return on Net Worth can be a result of either a small Return on Total Assets or too low a value of Financial Leverage. Return on Total Assets can then be broken down into its component parts, revealing the next lower level of abstraction, as shown in the expressions below.

Return on Total Assets = Net Profit Margin

× Asset Turnover

$$
\text { or } \frac {\text { Net   Profit }}{\text { Total   Assets }} = \frac {\text { Net   Profit }}{\text { Total   Sales }} \times \frac {\text { Total   Sales }}{\text { Total   Assets }}.
$$

![](/api/attachments/87XBF8WW/fulltext/images/411be771fb6562cfec01a04d625ca9d2fcadcd3bf1d4bc6f5efd6850e4c2b08e.jpg)  
Fig. 6. Structured Hierarchical Representation Illustrating a Top-Down Decomposition of the Profit Model Factors (Adopted From Haueisen and Camp, 1982; \* indicates a link to a frame defined further down the hierarchy).

![](/api/attachments/87XBF8WW/fulltext/images/9fbf4b8e4a7b48b7c4146b22469ee8c55bc60c49ef1381eac6a99c8a0a02e5ec.jpg)  
Fig. 7. Screen Showing "Input" Values ('VariableExpense Val' and 'FixedExpense Val') and "Calculated" Values ('Total/Expense Val') for Selected Frames During Model Verification.

The top-down decomposition of Return on Total Assets reveals the second and third key indicators of profitability; Net Profit Margin and Asset Turnover, respectively. It is clear from the model also that any improvement in margin management is multiplied by the Financial Leverage factor. The third key to profitability is asset management. The more effectively a firm uses its assets, the larger will be its profitability. Next, the factors driving Net Profit Margin and Asset Turnover are explored to reveal the next lower level of abstraction. These and additional levels of decomposition are illustrated in fig. 6.

Referring back to fig. 2, we can see how the expression for calculating the value for Return on Net Worth is entered into frame slot, 'RetOn-NetWorthProc'. Similarly, fig. 5 shows the procedure for calculating the value for Return on Assets in terms of Net Profit Margin and Asset Turnover. As noted previously and is usually the case, two terms on the right-hand side of the expression for Return on Net Worth ('FinLeverageVal' and 'Re-OnAssetVal') are found in frames specified in the 'IsComposedOf' slots. The same is true for terms on the right-hand side of the expression for calculating Return on Assets. The system will automatically retrieve these values necessary for the calculation when the model is executed, provided that the linkage information is completed and correct.

## 5.3. Executing and Observing the Behavior of the Model

Following the structural (conceptual) model formulation and the definition for all (at least all the essential - additional model enhancements follow model verification) model element operations is the process of model verification [3]. Entering data into the model and verifying the model by executing it with that data is accomplished in the following sequence of steps. First, values for primitive "input" variables are specified by entering numerical values into the appropriate slots. Fig. 7, for example shows that \$158,000 has been specified for slot 'VarExpenVal' and \$26,000 for 'FixedExpenVal.' Next, the user would execute the model and verify the results by displaying the frame information for selected, individual frames. Fig. 7 shows that the model has calculated a value of \$184,000 for 'TotalExpenVal' in the TotalExpense frame. If the model is to be executed through a sequence of steps, retrieving "input" from a database, as described in the next paragraph, the 'IsComposedOf' slots of the primitive variable frames would need to contain the name of the database frame.

![](/api/attachments/87XBF8WW/fulltext/images/9624fd3b828cfadd5db3bc8cabef3e8fcc7e1c2b9d0b15166402c821d4ae024c.jpg)  
Fig. 8. Instance of Quarterly Data Frame for the First Quarter of 1981.

The above procedure creates one instance of the given model, reflecting the model state at one particular point in time (e.g., the first quarter of 1981). In order to execute the model through a sequence of time steps to explore the model's dynamic behavior, it is necessary to integrate the model with a database whose frame instances contain values for the primitive or "input" variables for each of a sequence of time steps, say for each quarter. Fig. 8 illustrates one instance of a quarterly data database frame with values for the primitive variables having been either specified by the user or loaded from an external database. Also indicated are values for several variables ('Ret-NetWorthVal', 'RetOnAssetsVal', and 'TotalExpenVal') that have been calculated by the model. Dynamic execution of the model requires that the user specify linkage information (the name of the database containing the primitive variable frames) in the 'IsComposedOf' slots as noted above, as well as the particular sequence of quarterly data frame instances from which the data for the model is to be retrieved and to which the calculated model data is to be sent.

The behavior of the model for a wide variety of circumstances may be explored by examining different “what-if” type questions. For example, the procedure for deriving the numerical value for sales could be changed from simply retrieving values from the quarterly data database to retrieving the value and then increasing (or decreasing) it by, say, 15%. Another interesting “what-if” scenario might be to set the value of financial leverage to a constant, say, 10% above an average value as determined from an earlier run. Comparison with the earlier run would reveal how sensitive return on net worth is to changes in financial leverage.

Once the structure of the problem and the impact of the model elements on one another is clearly perceived and understood, a more compact method of displaying the result might be useful. A spreadsheet-type view of the “what-if” analysis results, for example would be a way to display the results of multiple “what-if” analysis model instances all on one screen rather than in multiple model instance windows. Alternatively, various other graphical options could be devised, as indicated in the following paragraph.

Results of the model execution can be displayed by displaying particular instances of the quarterly data frame and browsing through the data. A much more effective method for understanding the dynamic behavior of a model is to display selected values graphically by using a set of predefined images such as bar charts. These images can readily be attached to slots for particular frames and displayed at the end of a model execution. Fig. 9 depicts an artist's rendition of a such a display; made up of histograms attached to RetNetWorth, RetOnAssets, FinLeverage, and NetProfitMargin frames.

An even more effective means of visualization is to have graphical models of bar graphs or gauges tied to procedures within the frames to display current values in such a way that a change in the value of the variable would be immediately reflected by a change in the pictorial representation of that value. In this way, an animated sequence evolving through time in a sequence of motion picture-type frames could be displayed as a part of the process of exploring the dynamic behavior of the model. Procedures could also be incorporated to monitor changes and uses of certain instance variable values and to respond to interactive user queries concerning the model's current state. The capability for exploring the dynamic behavior of a model also provides a "hands-on" type of experience with the model useful as a beginning step for model-based reasoning.

![](/api/attachments/87XBF8WW/fulltext/images/aa8794e82acbf2d40f5e6c305cb06d72509b766bb0890803db08f5bc9fabc945.jpg)  
Fig. 9. Artists Rendition of a Screen Illustrating the Display of Various Histograms Reflecting the Behavior of the Profit Model Through a Sequence of Time Steps.

Exploring the behavior of the model for different circumstances enables the user to develop quantitative or qualitative rules and procedures that will serve as the basis for model-based reasoning, performed by the Reasoning System component (see fig. 3). One common use for the Reasoning System would be to infer (predict) likely consequences of a change in a given policy. This reasoning knowledge is expressed in the form of rules. The Model Manager component assists the user in organizing and incorporating these rules into the knowledge base.

## 5.4. Rules for Model-Based Reasoning

Rules tell the Reasoning System what to do, given a certain set of circumstances. The inference engine infers an answer to a query by applying a set of inferencing rules to a set of known or given facts. The facts are generated by executing the model to generate situations or scenarios that could occur from particular input data and management policies. Rules are conceptually of the form:

IF: conditional

## THEN: conclusion.

Rules are inserted into frame slots in a manner similar to that used for incorporating procedures described in an earlier section. In the case of the Smalltalk/V implementation, these rules are expressed in the form:

(Rule number: 1

condition: $\left[\# (\text{RetOnNetWorthVal} < 0.02)\right.$ isFact] action: $\left[\# (\text{RetOnNetWorth tooLow})\right]$ .

Procedures for allowing the user to interact visually with the system in developing and testing these rules fit nicely into the image-oriented, frame-based knowledge representation scheme presented in this paper. Ultimately, it would be possible to incorporate self-monitoring rules within the model to allow the system to alert the user whenever certain parameters exceed limits and to suggest a hypothesis about possible causes. These, more advanced aspects of a model visualization systems, are suggestive of the richness and variety of possible future research direction possible. The purpose of including this brief section on the Reasoning System is to indicate the suitability of the model visualization methodology for including model-based reasoning capability. This portion of the model visualization methodology is yet to be developed.

## 6. Concluding Remarks

Research is currently under way investigating possible schemes or languages for implementing a prototype of the model visualization model development environment described in this paper. Preliminary studies exploring the use of an object-oriented language called Smalltalk/V [4.6,7] have produced extremely promising results [22]. Object-oriented languages are oriented towards viewing the entities in a problem space as objects or frames that communicate with each other via messages. Each frame has associated with it procedures and definitions that provide information about that frame. Smalltalk/V provides an interactive graphical programming environment featuring bit-mapped graphics, multiple windows, and a source-level debugger. It runs on an IBM or compatible PC and offers many features available on highly specialized and costly knowledge engineering workstations.

Our initial design and development work indicate that the frame-based, model visualization approach represents a number of improvements over the textual modeling languages. First, a convenient and natural means is provided for a structured, holistic approach to the development of the models and their corresponding knowledge bases. The graphical representation itself is used to interactively encode facts, concepts, and relationships and the user is able to directly manipulate these objects and relationships. It is our contention that this capability to visualize and manipulate these model entities leads to a greater level of support for the sometimes very creative task of problem structuring than is possible with text-based, specialized modeling language. Second, the system reveals the internal state of the model, allowing the user to understand the structure of the model and to know first-hand that the model is not a "black box" that somehow produces "the answer." Third, the "hands-on" experience of the model builder affords a qualitative understanding of the dynamics of the system not available through typical quantitative analysis. Consequently, the user can gain confidence in his or her intuition about the behavior of the system. Fourth, the ability for interactively building the models and storing them in a knowledge base, or the capability for incorporating rules for reasoning processes requires a language as powerful and natural as visual images. Finally, the model(s) representing the structure of the problem domain could also serve as the basis for a rule model. These rule models, which are in reality just another form of abstract descriptions built from empirical generalizations, could be used to characterize a "typical" rule. The appropriate implementation of these rule models would allow the system to "know what is knows" and to "know what it does not know." The purpose for such a subsystem would be to check for consistency and conflict before adding new rules to the system.

## References

[1] Abbott, R.J. "Knowledge Abstraction." Communications of the ACM, vol. 30, no. 8, pp. 664–671, 1987.

[2] Blaha, M.R., W.J. Premerlani, and J.E. Rumbaugh. "Relational Database Design Using an Object-Oriented Methodology." Communications of the ACM, vol. 31, no. 4, pp. 414–427, 1988.

[3] Bosman, A. "Decision Support Systems, Problem Processing and Co-ordination," in Processes and Tools for Decision Support, pp. 79–92, Edited by Henk G. Sol, Amsterdam: North-Holland Publishing Company, 1983.

[4] Digitalk, Inc. Smalltalk/V: Tutorial and Programming Handbook, Los Angeles: Digitalk, Inc., 1986.

[5] Fikes, R. and T. Kehler. "The Role of Frame-Based Representation in Reasoning," Communications of the ACM, vol. 28, no. 9, 1985.

[6] Goldberg, Adele, SmallTalk-80: The Interactive Programming Environment, Reading: Addison-Wesley, 1984.

[7] Goldberg, Adele and D. Robson, Smalltalk-80: the Language and its Implementation, Reading: Addison-Wesley, 1983.

[8] Gorry, G.A. and B.B. Krumland. "Artificial Intelligence Research and Decision Support Systems." In Building Decision Support Systems, pp. 205–219. Edited by J.L. Bennett. Reading, MA: Addison Wesley, 1983.

[9] Greeno, J.G. "The Structure of Memory and the Process of Solving Problems." In R.L. Solso (Ed.), Contemporary Issues in Cognitive Psychology: The Loyola Symposium. New York: Wiley, 1973.

[10] Haueisen, W.D. and J.L. Camp. Business Systems for Micro-Computers, Englewood Cliffs, NJ: Prentice-Hall, Inc, 1982.

[11] Kaufmann, Geir. Imagery, Language and Cognition: Toward a Theory of Symbolic Activity in Human Problem-Solving, New York: Columbia University Press, 1980.

[12] Leavitt, H.J. "Beyond the Analytic Manager." California Management Review, vol 17 no. 3, pp. 5–12; vol 17 no. 4, pp. 11–21, 1976.

[13] McLean, J.M. and P. Shepherd. "The Importance of Model Structure." Futures, pp. 40–51, February, 1976.

[14] Miller, G.A., “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capability for Processing Information.” The Psychological Review, vol. 63, no. 2, pp. 81–97, 1956.

[15] Minsky, M. "A Framework for Representing Knowledge," Mind Design, edited by J. Haugeland, Cambridge, MA: The MIT Press, pp. 95–128, 1981.

[16] Newell, A.N. and H.A. Simon, Human Problem Solving, Englewood Cliffs, NJ: Prentice-Hall, Inc, 1972.

[17] Paivio, Allen. Imagery and Verbal Process. New York: Rhinehart and Winston, 1971.

[18] Paivio, Allen, “The Relationship between Verbal and Perceptual Codes.” in E.C. Carterette and M.P. Friedman, eds., Handbook of Perception. New York: Academic Press, 1979.

[19] Paivio, Allen, Mental Representations: A Dual Coding Approach. New York: Oxford University Press, 1986.

[20] Pracht, W.E. "An Experimental Investigation of a Graphical Interactive Problem Structuring Aid for Decision Support Systems." Ph.D. dissertation, Texas Tech University, 1984.

[21] Pracht, W.E. "GISMO: A Visual Problem Structuring and Knowledge Organization Tool," IEEE Transactions on Systems, Man, and Cybernetics, vol. 14, p. 265, 1986.

[22] Pracht, W.E. "An Object-Oriented Approach for Business Problem Modelling," Manuscript in preparation.

[23] Pracht, W.E. and J.F. Courtney, "Effects of a Computer- Graphics Based DSS to Support Problem Structuring", Decision Science, vol. 19, no. 3, pp. 598–621, 1988.

[24] Quillian, M.R. "Word Concepts: A Theory and Simulation of Some Basic Semantic Capabilities," Behavioral Science, vol 12. pp. 410-430, 1967.

[25] Richardson, John T.E. "Mental Imagery in Thinking and Problem Solving." in Jonathan S.B.T. Evans, ed. Thinking and Reasoning: Psychological Approaches. Boston: Routledge & Kegan Paul, 1983.

[26] Sanford, Anthony J. Cognition and Cognitive Psychology. New York: Basic Books, Inc., 1985.

[27] Sen A. and G. Biswas. "Decision Support Systems: An Expert Systems Approach," Decision Support Systems, vol. 1, pp. 197-204, 1985.

[28] Simon, H.A. "Information Processing Theory of Human Problem Solving," CIP Working paper No. 324, May 28, 1976.

[29] Tversky, B. and K. Hemenway, "Objects, Parts, and Cate-

gories," Journal of Experimental Psychology: General., vol. 113, no. 2, pp. 169–191, 1984.

[30] Weber, E. Sue. "Systems to Think With: A Response of 'A Vision for Decision Support Systems'." Proceedings of the Nineteenth Hawaii International Conference on System Sciences, vol. 1A, pp. 618–626, North Hollywood, CA: Western Periodicals, 1986.
