---
otero_id: 18256
otero_key: "ZBQGXGBS"
title: "The feature chart: A tool for communicating the analysis for a decision support system"
authors: "John P. Seagle; Salvatore Belardo"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90057-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Feature Chart: A Tool for Communicating the Analysis for a Decision Support System

John P. Seagle and Salvatore Belardo
School of Business, State University of New York at Albany BA,
310 Albany, New York 12222, USA

In developing information systems, analysts must communicate their understanding of the business problem to the user and must specify the proposed system to the designer. Over the years, various kinds of flow charts have been used to convey this information. Flow charts were originally developed when most programs either made scientific calculations or processed transactions. More recently, data flow diagrams have been used to document the analysis phase. A major point of this paper is that neither type of flow diagram is well suited to the development of interactive systems, particularly decision support systems. In an effort to address this problem, Sprague and Carlson developed the ROMC approach to the design of decision support systems. While their approach helps classify the components of a decision support system, it does not provide the analyst with a means of conveying the necessary information to the user or designer of a specific decision support system.

The feature chart, which is a synthesis of the ROMC model and structured analysis, is proposed as a graphic tool for analysis and communication. It serves the purpose of analysis in that tasks are defined and user interfaces shown. It also shows the controls available to the user and the ways the user can navigate through the system. The use of the feature chart is discussed for two applications: a geographic decision support system and a financial application using a generator.

Keywords: Feature chart, structured analysis, structured design, interactive systems, decision support systems, data flow diagrams.

## 1. Introduction

Systems of programs and hardware for computer applications are developed for a variety of purposes. From early systems that made scientific and engineering calculations, computer uses have expanded to include processing business transactions, controlling processes, and assisting decision makers. An application that assists decision makers is commonly called a decision support system (DSS). A DSS supports the decision maker by improving the effectiveness of the decision, espe-

![](/api/attachments/ZBQGXGBS/fulltext/images/5bfd52e0cabf2a450627ad346fbf0b424f8ebae0227b30e922613db57a43afd8.jpg)

John P. Seagle is Associate Professor in the Department of Management Science and Information Systems, State University of New York at Albany. His doctoral work at Stanford University involved application of mathematical models to space allocation. While on the faculty of the Buffalo campus of the State University of New York, he applied statistical methods to portfolio analysis and helped develop information systems for planning inventories and distribution of blood. Since coming to Albany in 1973, he has taught statistics, information systems design, and database management. He served as Chair of this department until 1985. In 1977-1978 he was a Fulbright lecturer at the University of Tehran. He is currently completing a book on structured programming in BASIC with Professor William K. Holstein.

![](/api/attachments/ZBQGXGBS/fulltext/images/0f4c826f2d12df6927caa98a271e89f477cf9965e2269a803cb36acb6ba1d277.jpg)  
ber of TIMS.

Salvatore Belardo is Associate Professor and Chairman of Management Science and Information Systems at the State University of New York at Albany. He is director of the Center for Disaster Management. He received his B.S. in mechanical engineering from Rochester Institute of Technology, an M.B.A. from the State University of New York at Albany, and an M.S. and Ph.D. from Rensselaer Polytechnic Institute. He is a consultant to business and government, and a memcially in semi-structured problems. Because it is a part of a decision process, a DSS must provide for interaction between the user and the computer. It is often necessary for a DSS to be adapted to the decision making style of the user [5].

Because it is both interactive and adaptable, tools for development of other types of systems are not necessarily well suited to a DSS. This study focuses on the definition or analysis phase of the system life cycle. This includes both feasibility assessment and information requirements analysis, and traditionally accounts for no more than 25% of the resources needed for system development [3]. However, the success of the completed system may well depend on the correctness of the results of this phase: a specification of the system to be designed. This must be communicated to the designer and must also be understood by the user in order to verify that the needs and environment were correctly interpreted. Narratives and computer aided techniques, such as PSL/PSA [13], are more suited to specification than verification because they do not provide a concise summary.

Builders of information systems recognize the value of graphic tools as a means of facilitating the analysis phase. ACT/1 [7], for example, helps analysts create prototype menus, screens, and dialogs. These tools communicate results of analyses in walkthroughs, which involve the user and help assure that the system is more acceptable to the user [1]. But such tools do not completely fill the analysts' needs, because real decision support systems provide the users with flexible access to data bases and model banks. Multiple screens and dialogs become unwieldy when trying to communicate the various paths available to a user of a DSS.

In recent years, attempts have been made to structure the analysis phase. One tool for this purpose, the data flow diagram (DFD), has been widely accepted for business applications. It is graphic, focuses on interfaces, and enables the analyst to partition the system into manageable and easily understood component parts. The data flow diagram also provides for both specification and verification. The DFD has also been found useful for decomposing real time control systems into tasks and identifying concurrency [4]. However, data flows are not easily identified during the analysis phase of an interactive DSS nor are they of primary concern.

A graphic tool called the “Feature Chart” is presented in this paper to help in communicating the objectives and features of the proposed decision support system to both the designer and the user. Feature charts convey the flexibility necessary to support decision makers faced with semi-structured tasks.

## 2. Architecture of a Decision Support System

DSSs have been proposed for use in cases where the decision process is semi-structured. Typically such a process is not well enough understood for an analyst to be able to describe it before starting the design of the DSS. Sprague and Carlson [10] state that in these situations. “No process model can serve as a paradigm for systems analysis and design of decision support systems because DSS must be process independent.” Process independence allows a DSS to accommodate different decision making styles and the variety of specific decision situations for which a DSS may be used.

In response to this problem, Sprague and Carlson have developed the ROMC approach for delineating and classifying the components of a DSS. The four letters of ROMC stand for a type of component: "R" stands for representations of information; "O" refers to operations (from statistical analyses to complex simulations and forecasting algorithms); "M" is for memory aids (such as data bases, files, workspaces, and triggers or reminders); "C" are control mechanisms which enable the user to choose among the various features (menus, commands, and optional help messages).

The process independence of the ROMC approach is achieved by avoiding of any kind of specification that imposes a sequence on the decision maker's actions. In avoiding such a specification, however, the ROMC approach does not show how the user will interact with the system. In contrast, flow charts and data flow diagrams force a sequence: flow charts specify an ordering of actions, and data flow diagrams depict the operations performed on a group of data items.

To illustrate the ROMC concept, Sprague and Carlson present several figures. These help classify the four kinds of components, keeping each kind at a separate level: control aids at the top, representations at the next level, and so forth. Such a hierarchy suggests a single sequence of steps to each representation and operation. This may be the very process dependence that Sprague and Carlson have tried to avoid.

While a specific process for using the components should not be imposed by a DSS, neither is it feasible to allow the user to hop to any point. The options available and meaningful to a user may depend on some previous steps. The user and the designer need to know not only the specific controls, operations, and representations available, but also the various paths by which they can be reached. The methods discussed above do not serve this purpose. Neither do they provide a means of dividing the DSS into manageable modules for programming or for adapting the general tools of a DSS generator.

## 3. Analysis for a Decision Support System

Analysis in any project includes specification of functions to be performed and the description of all interfaces, both among components of the system and with whatever is outside the system under development [1]. As stated previously, a DFD is a graphic tool for communicating the results of the analysis phase; it depicts the flow of data through a possible sequence of transformations. All points at which the user enters, reviews, changes, or receives data are clearly shown, along with all accesses to files. Control is not shown on a DFD, but is left for the design phase. In a program to process data, controls are often internal to a program and are not involved with user or other interfaces. Similarly the representations of information (e.g., display vs. computational, record vs. array) are questions of how the defined functions will be accomplished.

In a DSS, however, the user controls and representations are the interfaces with the user. These interfaces, along with operations available to the user, need to be defined in the analysis phase just as much as do transforms in a conventional data processing application. Each specific representation, operation, and control needs to be specified by the analyst and communicated to the user, along with all possible paths from one to another. Specification of data stores (memory aids) is an analyst's responsibility in the development of any system, whether it is for data processing or decision support.

The data flow diagram allows for leveling, where a series of progressively more detailed diagrams lead eventually to functional primitives. These are transforms that are not broken down into finer components, but can be specified as a whole [1]. Other methods that provide for decomposition of complex tasks into simpler components include Sweden's ISAC approach [6] and Hierarchy plus Input-Process-Output (HIPO) [11]. The ability to decompose a complex task is no less necessary for a DSS than for the kinds of systems for which these methods are regularly used.

## 4. The Feature Chart

The feature chart shows the features of the system with which the user interacts. These features are the representations, operations, and controls, as well as the supporting memory aids. The feature chart uses standard flow chart symbols for the representations and operations used by the decision maker. The user's controls are shown in a manner similar to the structure chart of structured design [8,12,14]. The feature chart serves the purposes of analysis in that the tasks to be performed by the system are defined and the user interfaces shown.

Standard physical device symbols are used for representations. Whether a representation is on a terminal screen or a printed report is part of DSS analysis, not a physical detail to be left for the final phase of a project. The style of the user and the nature of the decision problem should determine the form of the representation, as well as whether controls will be by menu choices or commands. These are decisions of the analysis phase. On the other hand, the particular hardware or program structure that produces a representation or control need not even be apparent to the user, and thus is not a concern in the analysis phase.

The symbols which represent the ROMC components – representations, operations, memory aids, and controls – are shown in Figure 1. Standard ANSI flow chart symbols are used for physical devices important in specifying user interfaces. Examples are a terminal screen, a paper report, and a keyboard where it is used for extensive data entry. The standard input-output parallelogram is used in a non-standard way: for menus with which the user selects features. User initiated transfers of control, such as those made from a menu, are represented by solid arrows, and data flows are represented by dotted lines. Menus are not the only form of control; commands in operations can transfer control to other operations or to menus.

![](/api/attachments/ZBQGXGBS/fulltext/images/8b307c1a64208f59e0fc93511862fb3319442ed12c25923b21703f37e9b40169.jpg)  
Figure 1. Symbols Used in Feature Charts. Note: Based in Part on ISO Standard 1028 and American National Standard ANSI X3.S-1970.

An example of a feature chart for a large decision support application is shown in Figure 2. The decision maker supported is a dispatcher of trucks delivering merchandise to approximately 1500 stores spread over several states. The first user interface, shown at the top, is a main menu with four numbered choices. The first choice, at the upper left, is for entering the weight and volume to be delivered to each store on a particular day. These requirements are obtained from a mainframe vehicle scheduling program (VSP), input through a keyboard and stored in the Store File. The VSP presents deliveries collected into routes, each of which is the group of stores receiving deliveries from a single truckload. Routes are recorded in the Route File. The Cycle File serves as an index to the Route File, enabling several complete sets of routes to be saved and compared. The objective of the decision support system is to help the dispatcher plan routes that are cheaper than the ones presented by the VSP, and that are feasible under current conditions.

Moving across the top of the chart from left to right, one encounters two minor choices from the main menu. These choices are placed here in order to keep the center of the chart free for the more complex second choice. Choice 3 allows premanent information about a store to be modified, and Choice 4 allows selected groups of stores to be analyzed. The most complex choice, Build Routes (2), is next, and occupies most of the remainder of the chart. This is the decision support part of the system; it helps the dispatcher analyze the current set (or cycle) of routes and improve them by moving stores from one route to another.

The main menu choice of “Build Routes” leads to another menu, from which five more choices are available. The first, “Select Cycle #’s”, allows the user to pick a set of routes, such as that provided by the VSP, for modification. The modified routes may then be stored on another cycle. Should be modified routes prove unsatisfactory, the user can go back to an older cycle and begin modifying again.

The next choice (2) from the Build Routes Menu prints a summary of all routes on the current cycle. Among other things, this report tells the dispatcher which trucks are overloaded or underloaded. We also describe the fifth choice at this time because it is relatively straightforward. Choice 5 produces a printed store detail report, giving data the driver needs to execute a planned route.

Choice 3, “Select Map”, yields another menu that allows the user to display any of a variety of stored maps, or to plot a map of an area that completely covers one or more routes. Once a map has been displayed, a menu on the map shows the user a wide variety of options, including “Zooming” to an enlarged view of a part of the current map. These map changing options make no sense unless a starting map is already on the user’s graphic display screen. The feature chart shows the dependency among the three map menus.

The fourth choice, “Change Routes in Current Cycle”, interacts heavily with the maps displayed by the third choice. Choice 4 allows the user to select two routes for analysis and tentative revision. Stored data from the Route and Store files are read but not changed, as there are no arrows leading to these files. Details of the two routes are displayed on a text screen, and these routes may be plotted on the current map at any time. Stores may be moved from one active (displayed) route to another, but these changes are saved to the Route and Cycle files only when the command to "Save Active Routes" is given.

![](/api/attachments/ZBQGXGBS/fulltext/images/856b9438f5bb47d05f6c448670916d5f86d0ba39297ee9813e17a5cf51662b2f.jpg)  
Figure 2. Feature Chart for Vehicle Routing System.

A user who has plotted the active routes may return and continue making changes, and also has the option to call for the “Menu on Map,” which gives access to all the map options available when the map had been displayed after the “Select Map” menu. Such a crossing over from one low level feature to another saves effort in using the system, but is difficult to communicate. The feature chart shows all the options available at any step in using the system, and how to navigate to any desired feature of the system. The system itself is complex, and we do not pretend that Figure 2 can be quickly understood. However, it conveys the essentials of the analysis phase to the user or designer.

Just as the data flow diagram serves as the transition to the design stage, so does the feature chart. The shape is already suggestive of the structure chart. To demonstrate the transformation of the feature chart to a structure chart, we use a simplified feature chart, Figure 3, which is a subset of the features of Figure 2. Figure 3 may then be compared to its corresponding structure chart, Figure 4. There are some subtle differences between the two charts, even though they are somewhat similar in appearance. Plotting of active routes is not a subordinate module to “Change Routes”, as the control path from operation to operation on the feature chart would indicate. The

![](/api/attachments/ZBQGXGBS/fulltext/images/8e5dd42776d3b173c575f88c256cf6743130c15c83b85920d3fb7c9ef2029b1b.jpg)  
Figure 3. Feature Chart for Build Routes Option From Vehicle Routing System.

![](/api/attachments/ZBQGXGBS/fulltext/images/f4bafa8da77a5307db7fcf1c26e71e295e1f65e44066f3ece5ed3806ec3209d6.jpg)  
Figure 4. Structure Chart for Build Routes Option from Vehicle Routing System.

feature chart shows only the user's controls, not how the designer chose to implement them. In this case, the designer chose to keep all plotting modules subordinate to the high level graphics module "Display Maps". Program control is passed up the structure chart and back down to the module "Plot Active Routes". Data identifying the active routes is passed along the same control path, using the short arrow symbols of the structure chart.

A strength of the data flow diagram is the ability to level, decomposing a transform into the several more primitive transforms that constitute it. Once an operation has been specified on the feature chart, the full range of structured analysis tools may be applied. The operation, along with its inputs, file references, and outputs to representations, may be used as a context diagram. Data flow diagrams of all levels would form the specifications for the operation.

The development of high level or fourth generation languages has the potential to greatly reduce the effort required to develop specific decision support systems. To the extent that an operation, control, or representation specified in a feature chart is part of a high level language, then no further design is required. The analyst can implement the activity as a stored function, or the decision maker can implement it with commands from the high level language.

## 5. Feature Charts and Decision Support System Generators

While there may be considerable debate concerning the definition of a decision support system generator, for purposes of discussion we will include the software package “FCS-EPS” in this category $[2,9]$ . FCS-EPS provides the sytem designer and user with a non-procedural language for decision support activities. It has over forty commands including “Graph” and “Sensitivity Analysis”, along with 150 functions that allow the user to perform calculations, such as discounted cash flow and net present value. We now illustrate the use of a feature chart to specify how the user can apply the capabilities of FCS-EPS to a specific decision support system. We have chosen a financial problem that uses the FCS-EPS functions to calculate the present value of a stream of cash flows, sensitivity analysis to compare alternative investment policies, and graphical representation of the results.

![](/api/attachments/ZBQGXGBS/fulltext/images/5a836302f7d2c23e3dc9fbeb67c6e31766607a07a208c74d02faf446829d47e7.jpg)  
Figure 5. Feature Chart with DSS Generator.

Figure 5 illustrates how a feature chart might be used in the situation described above. Once the user has called a specific logic sequence, the user is presented with a menu listing several operations. The operations are routines written in the FCS-EPS language and saved by an analyst or the user as a logic file. Saved routines contain the powerful commands and functions described above, and can be invoked directly or from other saved routines containing menus. Saved routines are noted on the feature chart by a horizontal line near the top, below the library name of the file.

In the specific decision support system described above, the user can choose the discounted cash flow function from a menu. The selection brings into memory the logic and data necessary to calculate the discounted present value of a stream of cash inflows and outflows over time. The command “calculate” causes the logic to perform the intended operations on the data. Once the user examines the discounted cash flow results, he or she may issue a command to graph the cash flows or perform a sensitivity analysis to examine the impact of changes in revenues or interest rates. Commands to perform these two functions are part of the FCS-EPS language, and are not programmed in advance for this application. Note that they are not shown as saved routines, but they are called from the FCS-EPS system. The user may then return to the main menu to produce a previously formatted report, or return to the FCS-EPS system to create a special report.

## 6. Conclusion

The feature chart is presented as an adaptation of several existing graphic tools to synthesize the

ROMC model with structured analysis. The feature chart addresses concerns of analysis that apply to interactive systems, particularly decision support systems. This tool can be used for analysis of systems to be created using general purpose procedural languages, and for analysis and partial design of applications using decision support system generators. In the latter case, the chart distinguishes between stored routines developed for a specific DSS and features of the generator itself.

The feature chart describes the system as seen by the user. It will help assure that the analyst understands the user's needs, and that the user understands what the analyst is specifying. The feature chart shows the interfaces, paths, and flexibility of a proposed system. The level of detail is specific: the feature chart shows no detail beyond the point where user interaction stops. Standard methods of structures analysis are applied to non-interactive parts of the system.

Finally, the feature chart leads naturally into the structure chart of design. In general, the user controls at the top of the feature chart become the high level control modules of the structure chart. The designer is free to implement a feature chart in a variety of ways, but the very nature of a decision support system requires that some physical aspects of the system be specified in the analysis phase.

## References

[1] DeMarco, T. Structured Analysis and System Specification, (A Yourdon Book) Prentice-Hall, Englewood Cliffs, N.J., 1979.

[2] E.P.S. Inc. Introductory Guide FCS-EPS, E.P.S. Inc., Windham, N.H., Feb. 1983.

[3] Ginzburg, M.J. "Early Diagnosis of M.I.S. Implementation Failure," Management Science, Volume 27, Number 4, 1981, pp. 459-478.

[4] Gomaa, H. "A Software Design Method for Real Time Systems," Communications ACM, Volume 27, Number 4, 1984, pp. 938-949.

[5] Keen, P.G.W., and Scott-Morton, M.S. Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, Mass., 1978.

[6] Lundeberg, M., Goldkuhl, G., and Nilsson, A. "A Systematic Approach to Information Systems Development-II, Problem and Data Oriented Methodology," Information Systems, Volume 4, Number 2, pp. 93-118.

[7] Mason, R.E.A, and Carey, T.T. "Prototyping Interactive Information Systems," Communications of the ACM, Volume 26, Number 5, 1983, pp. 347-354.

[8] Page-Jones, M. The Practical Guide to Structured Systems Design, Yourdon Press, New York, N.Y., 1980.

[9] Sprague, R.H. Jr., “A Framework for the Development of Decision Support Systems,” Management Information Systems Quarterly, Volume 4, Number 4, Dec., 1980, pp. 1-26.

[10] Sprague, R.H. Jr., and Carlson, E.D., Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, N.J., 1982.

[11] Stay, J.F., “HIPO and Integrated Program Design,” IBM Systems Journal, Volume 15, Number 2, 1976, pp. 143-154.

[12] Stevens, W., Myers, G., and Constantine, L. Structured Design, I.B.M. Systems Journal, Volume 13, Number 2, May, 1974. pp. 115-139.

[13] Teichroew, D., and Hershey, E.A. III, “PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems,” IEEE Transactions on Software Engineering, Volume SE-3, Number 1, January 1977, pp. 41-48.

[14] Yourdon, E., and Constantine, L. Structured Design: Fundamentals of Computer Program and Systems Design, Prentice-Hall, Englewood Cliffs, N.J., 1979.
