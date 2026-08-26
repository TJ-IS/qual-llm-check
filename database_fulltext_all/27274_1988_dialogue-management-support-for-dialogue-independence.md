---
otero_id: 27274
otero_key: "FCHNB5QJ"
title: "Dialogue Management: Support for Dialogue Independence"
authors: "Feng-Yang Kuo; Benn Konsynski"
year: "1988"
journal: "MIS Quarterly"
doi: "10.2307/249216"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Dialogue Management: Support for Dialogue Independence
Author(s): Feng-Yang Kuo and Benn Konsynski
Source: MIS Quarterly, Vol. 12, No. 3 (Sep., 1988), pp. 481-499
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249216

Accessed: 08/05/2014 23:52

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Dialogue Management: Support for Dialogue Independence

By: Feng-Yang Kuo
Information Systems
University of Colorado at Denver
1475 Lawrence Street
Denver, CO 80202

Benn Konsynski
Harvard Business School $^{1}$ Anderson 23
Boston, MA 02163

## Abstract

Dialogue management involves the application of systems in the design and delivery of user-system dialogues. This article describes a dialogue management environment that is based on a concept of dialogue independence: the separation of dialogue definition from dialogue execution. In this environment, software facilities provide building blocks for design and delivery of dialogues that are consistent, efficient, shareable, and portable. The environment supports multiple workstation and communication protocol environments. This environment is compared to those emerging in homogeneous hardware environments such as HyperCard.

Keywords: Dialogue management, dialogue independence, dialogue definition, dialogue manipulation, dialogue interoperability

ACM Categories: C.5.3, D.2.1, D.2.2, D.2.M, H.I

## Introduction

Dialogue management research has focused on understanding organizational, task, personal, and technological characteristics to provide effective communication and control in user-computer dialogues. In particular, increasing computing power and interface device capability that is employed to reduce costs and enhance productivity heightens interest in engineering modular software functions that support the development of user-friendly information systems. Like successful data management, successful dialogue management requires an understanding of task requirements, environmental attributes and user skills and capabilities. In the step-by-step refinement that is essential in the dialogue design process, the objective is to facilitate the development of an easy-to-use and easy-to-maintain system dialogue.

This article describes a dialogue management approach based on a concept of dialogue independence, similar to the data independence associated with database management. We first describe the user environment, with a focus on those concepts useful to the designers of online, interactive information systems, particularly the applications systems for personal computing and decision support. The establishment of a dialogue management environment establishes the building blocks for an online, interactive interface design that reduces the time and effort required to develop an effective and meaningful interface. The approach to dialogue design presented in this article has been applied in organizations developing systems across a variety of computer, workstation, and communications environments. The reality of multiple vendors and heterogeneous computer and communications devices heightens the interest in dialogue standards and dialogue support of interoperability.

Heterogeneity exists across host and back-end processors, communications linkages, workstation devices, and applications functions. Vendors have sought a variety of means for dealing with variance in the software and hardware, while seeking consistency in the dialogue, or interface. Many dialogue management solutions offer guidelines and support tools within the particular vendor's hardware and software architectures. Thus, Apple's HyperCard and IBM's Systems Application Architecture (SAA) each offer standards for application development within the structure of the vendor's hardware and software environment. Each seeks advantage of the vendor's architecture in provision of a common dialogue standard. Each guideline assists in the development of dialogues across applications, limited only by the vendor's hardware and software platform requirements.

Several provisions for software development presented in this paper have elements in common with vendor and architecture specific dialogue tools such as Windows, HyperCard and SAA. Each of these tool environments, or dialogue platforms, is subject to misuse if not applied carefully. The critical aspect is that application of the tool environments is not enough to guarantee an effective interface design and a maintainable system. The dialogue definitions must be logically derived from the user requirements and must be separated from the application processing, as is the case in data schema. The discussion of the software environment should prove useful to designers who wish to establish dialogue standards across various hardware environments.

The next part of this article presents an overview of the dialogue independence concept and the design approach that maintains dialogue independence. A detailed discussion of the two phases, dialogue definition and dialogue manipulation, is presented in the following two sections respectively. Conclusions and opportunities for future research are discussed in the last section. Throughout the article, details of the implementation of an electronic mail system using the approach are presented to illustrate the findings.

## Dialogue Independence

Dialogue independence refers to the separation of dialogue handling from the details of the delivery system implementation. The concept has been partly addressed in the work on “protective ware” by Partidge and James (1976), SYNICS by Edmonds (1981), the STAR graphics of Xerox by Liphie (1982), ADELE by Coutaz (1985), and the USE methodology by Wasserman (1985).

Research suggests two critical aspects of dialogue independence: the separation of dialogue definition from manipulation facilities and a further separation of manipulation facilities from the hardware and software that defines the processing and communications of the delivery system. The separation of dialogue definition from manipulation facilities offers significant advantages over the embedded dialogue functions in traditional information systems. Such independence allows the designer to concentrate on specifying business functions and user-oriented dialogues that meet the requirements of the business task with less concern for the implementation details and the delivery environment. With the aid of computer-based dialogue tools, the system dialogues can be experienced and examined prior to full-scale implementation. As a result of the separation of dialogue objects, their relationships and dialogue semantics, the system dialogues are easier to modify. More importantly, the separation allows experts in different specialities to work on different aspects of design (e.g., an artist for screen layout; an analyst for implementation).

From the software engineering viewpoint, the separation of dialogue manipulation facilities from the application system software encourages sharing both dialogue definitions and manipulation facilities among applications. This reusability and sharing of common dialogue objects results in more standardized dialogues across applications and reduces development costs over time. Also, because the manipulation facilities are no longer embedded in the application system software, the impact of changing dialogue definitions and manipulation facilities on the application system software can be minimized. This dialogue information “hiding” assists in the maintenance of systems. This approach enables the decoupling of the often dynamic dialogue handling from the relatively stable application system software functions (e.g., data manipulation).

In this approach the designers and maintainers can deal with various user requirements and hardware-dependent characteristics. As dialogues themselves become more dynamic and adaptive, this dialogue independence will prove essential.

## Design Approach

Figure 1 depicts the design approach based on dialogue independence. The design cycle begins with a definition of requirements through an analysis of the task and the user in order to define the requirements. Analyzing tasks facilitates the definition of the required processes, data, and control structures; analyzing users enables the definition of the behavioral implications critical to effective dialogue design.

The next two steps of the cycle are defining and implementing the application system's dialogues. Dialogue definitions include the specifications of dialogue objects, their dependency structure, and additional attributes to meet task and user requirements. Dialogue objects include data tables, command menus, text entry forms, and data/command languages. The dialogue definitions of an application system consist of a set of interrelated dialogue objects that require certain action for user input and system output. The attributes of a dialogue object include the object type, its dependency structure, and several additional attributes for image descriptions.

![](/api/attachments/FCHNB5QJ/fulltext/images/a6d279694caed9272d8b92a3fe3423cb2d6ce478092e24402a120a398f72f07c.jpg)  
Figure 1. A Dialogue Design Environment Based on Dialogue Independence

As the dialogue objects are defined, the definitions are incorporated in a design knowledge-base. In implementation, the library of dialogue manipulation actions accesses the object base and delivers the dialogue design on behalf of the application system. Immediate dialogue modification can be made by changing the dialogue object and relation definitions. Modifications can be made if there is a change in the system requirements or self-modification in adaptive dialogues.

## Dialogue Definition

The dialogue process of an application system can be described as a user-computer communication process involving the interchange of messages among a series of dialogue objects. Two aspects of dialogue design—task and user—must be considered in design of a user-computer interface. The task aspect requires the designer to specify dialogue objects that represent data, processes, and their dependency structures necessary to accomplish the functional tasks. Application systems may share dialogue objects if their purpose, process, and data requirements overlap.

The user aspect of dialogue design requires that the designer concentrate on human factors that assist in system and user guidance, learning and error recovery. For example, the dependency design is modified to match the user's view, or the mental metaphor (Carroll and Thomas, 1982), of the system operations to facilitate user learning. Help messages for command and data objects may also be needed to ensure that instant guidance is available. At the same time, analysis and review of the operation status and information currency provide the user with feedback for dialogue adaptation. Appropriate dialogue interaction techniques must be selected to meet the user requirements (e.g., a question/answer for novices or a form entry for skilled users). The language of the user interface must employ user-familiar terminologies associated with the problem domain. Finally, the quality of the interface may be improved by specialized video artists. These and other human factors are considerations discussed in Carey (1982), Carroll and Thomas (1982), Gaut (1985), Malone (1984), Morland (1983), and Norman (1983).

## Dialogue objects

In the design of system dialogues, a designer must first define the basic dialogue objects involved in the task domain. In the last few years the focus on object manipulation has been a key thrust in the design of interactive user interface (Lipkie, 1982; Snodgrass, 1983; Tesler, 1981). The emphasis on object design in the requirements analysis is also described by Booch (1986), Borgida (1985), and Bracchi, et al. (1984).

The object definitions must fulfil the task requirements (e.g., process, data, and control) and user requirements (e.g., learning and error recovery). Generally, in a typical business application, dialogue objects are defined for handling commands (an internal process or control transfer) and data (certain data entities and attributes). In addition, messages such as help, error, operation status, and data currency play a critical elemental role in enabling user learning and error recovery in the overall dialogue process. Thus, a dialogue object may be used to represent command, data, messages and other object forms.

In classifying the objects for the design of user interfaces, a variety of human factors must be considered. Miller and Thomas, in (1977) propose classifying the interfaces into user-guided, system-guided, user-free response, and user-forced choice. A taxonomy of dialogue techniques based on this classification is described in Table 1.

Consequently, dialogue objects can be classified according to their purpose (e.g., command, data or message handling) and to their human factor characteristics (e.g., free response or forced choice). A variety of common dialogue object types is presented in Table 2. A list of objects for handling mail creation in an E-Mail system appears in Table 3.

Table 1. A Taxonomy of Dialogue Techniques Based on Human Factor Characteristics

<table><tr><td rowspan="2">Initiation</td><td colspan="2">Choice</td></tr><tr><td>Free-Response</td><td>Forced-Choice</td></tr><tr><td>User-Guided</td><td>Database languageCommand languageData mnemonicsText (word) processing</td><td>Expert system questionsInput-in-the-context-of-output</td></tr><tr><td>System-Guided</td><td>Question/free answerForm filling</td><td>Question/forced answerCommand menu selectionData menu selection</td></tr></table>

Table 2. Common Dialogue Object Types

<table><tr><td>Type</td><td>Descriptions</td></tr><tr><td>a</td><td>Forced command choice type, such as menu and scroll menu</td></tr><tr><td>b</td><td>Free choice language type, such as command language</td></tr><tr><td>c</td><td>Forced choice data object, such as a menu of data items</td></tr><tr><td>d</td><td>Free response data object, such as a form data</td></tr><tr><td>e</td><td>Free response data object, such as a table of data</td></tr><tr><td>f</td><td>Free data entry data object, such as an unformatted document</td></tr><tr><td>g</td><td>Combinations of computer system prompts and the user&#x27;s answers</td></tr><tr><td>h</td><td>The help type for (many levels of) help messages</td></tr><tr><td>i</td><td>The error/status/currency type of messages</td></tr></table>

The examples are limited to a subset of the basic dialogue objects that occur in the electronic mail system used as an example in this discussion. For example, graphics objects such as bar charts are frequently used in many systems but are not included in the initial dialogue object list in Table 2. This limitation is, however, offset in the system by an ability to freely define new additional object types.

In dialogue object definition, common objects such as those in advanced windowing techniques are often used. In windowing, a dialogue object "owns" its view port (window), and all its operations affect only the view port. The result is a managed, layered hierarchy of viewports associated with the limited display (screen) involved in user-system communication.

## Dialogue dependency

Dependencies between dialogue objects are described as preceding and succeeding relationships, each of which is associated with particular conditions that are to be activated. Previously, extended state transition diagrams (STD) and Bacus Naur Forms (BNF) (Edmonds, 1981; Jacob, 1983; Parnas, 1969; Reisner, 1981; Rowand Shoens, 1983; Wasserman, 1985) have been used to represent the sequences of user inputs and system outputs, including such details as single-system response and associated transitions caused by user operations (see Figure 2).

The situation depicted in Figure 2 illustrates a common, yet undesirable, situation in dialogue development, requiring the designer to have an in-depth knowledge of various dialogue methods as well as a commitment to the method to be implemented. The problem is made worse if a substantial amount of user interface components have to be specified. In the initial design stage, implementation specifics increase design complexity and should only be introduced later in the implementation stage.

The dialogue development process proceeds through the definition of dialogue objects and the transitions and messaging among the objects, rather than a step-by-step description of the interactions required to manipulate each attribute and the transitions between the attributes of objects. As will be shown later in the section on dialogue manipulation, a manipulation function is dedicated to each dialogue object type in handling operations on dialogue objects. In this way, we reduce the amount of the definition of specific actions that are required for handling each dialogue object. In the following discussion, the STD is revised to include only the object definitions and their local interactions and interdependencies.

In the STD for creating a mail message (see Figure 3), for instance, a node represents a dialogue object. A node may also represent another level of STD, a cluster of dialogue objects at a more detailed level. A name is provided for each node/object. A labeled, directed arc is a conditional transition, with a label specifying the transition condition. Conversely, and unlabeled, an unlabeled, directed arc is an unconditional transition.

Table 3. Dialogue Objects for Mail Creation

<table><tr><td>Object Name</td><td>Type</td><td>Description</td></tr><tr><td>CREATE/SEND</td><td>Command “a”</td><td>Menu to invoke creating and sending mail</td></tr><tr><td>HEAD</td><td>Data “d”</td><td>Form for creating/modifying the letterhead</td></tr><tr><td>EDIT</td><td>Data “f”</td><td>Free entry form for creating/modifying mail</td></tr><tr><td>MBC BOX</td><td>Data “e”</td><td>Table for listing mail created</td></tr><tr><td>MBS BOX</td><td>Data “e”</td><td>Table for listing mail sent</td></tr><tr><td>MBC</td><td>Currency “i”</td><td>Area showing the current mail created</td></tr><tr><td>MBS</td><td>Currency “i”</td><td>Area showing the current mail sent</td></tr><tr><td>ERROR</td><td>Error “i”</td><td>Area showing the error messages</td></tr><tr><td>HELP</td><td>Help “i”</td><td>Area showing the help messages</td></tr><tr><td>CREATE/CURRENCY</td><td>Status “i”</td><td>Form for creating/modifying the letterhead</td></tr></table>

![](/api/attachments/FCHNB5QJ/fulltext/images/b512f4a4cf1520ab52f41a125b3e85fe75cf74f0eeb2784abcf95f4ba64837b9.jpg)

![](/api/attachments/FCHNB5QJ/fulltext/images/079ba344942215b2e3dc24573ea9cf2dace724221d8f22562363134aff93ee1c.jpg)

Notations:

<> Function key operations:

<Fn> nth function key

<N> NEXT item function key

<p> PREVIOUS item function key

<H> HELP function key

<E> EXECUTE function key

<A> ABORT function key “ ” Character/String input OR condition

![](/api/attachments/FCHNB5QJ/fulltext/images/a1ba24d6485c13dd8cf82debd7c8996685f972e89cb2007e3f3b86fb224bfd24.jpg)

Unconditional transition
Conditional transition associated with function key operations or character/string input

Process without user interaction, such as an internal process or listing help, error messages

![](/api/attachments/FCHNB5QJ/fulltext/images/767a2ce72cdbca13e133f6b6d3ac8bb2632725d64daec3085d74cc7e6adef1eb.jpg)

A stable state

![](/api/attachments/FCHNB5QJ/fulltext/images/41280ae0825092ccfc1003a0b4b847463cde597668ff400edf1cbff5bca030a0.jpg)  
Figure 2. An STD for a Menu Operation

Exit the diagram

The user presses function keys F1 to F3 or character "a" to "c" to select an option, then an EXECUTE key to invoke the internal process or an ABORT key to abandon the selection. Toggling between options is allowed by using the NEXT and PREVIOUS function keys. General and specific help messages are available at any time by pressing the HELP key.

MIS Quarterly/September 1988

![](/api/attachments/FCHNB5QJ/fulltext/images/68e059397fb00aa7cec148df1162cf9e79ac348b5b44d2bcd98a7ebf31db3484.jpg)

![](/api/attachments/FCHNB5QJ/fulltext/images/af98e25370f47c912e9168c7bec8be8a311042de383a4fbd321cfb90396b13b8.jpg)  
Figure 3. The Revised STD for Mail Creation

The meaning of a label (i.e., required user operations) can be described later in the implementation stage (e.g., NEW MAIL: = <F3> | "N" in Figure 3). The application system dialogues can thus be viewed as a hierarchy of STDs, or clusters of dialogue objects. Figure 4 illustrates a hierarchy of STDs used in the mail handling dialogue of the electronic messaging environment.

There is an important benefit in clustering subordinate dialogues: each dialogue object occupies its own view port and represents a set of closely related attributes meaningful to the user. Furthermore, each dialogue cluster represents a higher-level aggregation of the system's functions and can be processed on its own "logical screen";

that is, dialogue objects of different clusters will not be displayed on the screen at the same time, although there is only one “physical screen.” The ability to communicate to users in hierarchies of information chunks in distinct view ports and screens allows the designer to define dialogues that best match the user’s mental model of the system.

## Additional attributes

Additional attributes are necessary to complete the description of a dialogue object. A name is assigned to a dialogue object as the logical reference to that object. The spatial information—the

![](/api/attachments/FCHNB5QJ/fulltext/images/3bc511eb9991c3fcf2d58dfc84b19d00b34350eb3b005352cb889b5aa9e03586.jpg)  
Figure 4. The Hierarchy of STDs for the E-Mail System

![](/api/attachments/FCHNB5QJ/fulltext/images/92784697177e251b4448ed35a1832d95bff85e2e674d3d997facdf1dec58cbb9.jpg)

## Figure 4. (continued)

location and size of a dialogue object—is determined by the task requirements (e.g., size of table, number of options in a menu, etc.). The lexical elements, such as options for a menu, messages for error indication, and column headings for a data table, are specified to convey “what, how, and why” the user needs to know in order to utilize the system. Video attributes such as reverse video or level of density are used to highlight certain parts (e.g., key fields, default options, etc.) of the dialogue object.

Ruler attributes (i.e., margins and line attributes) are given to the document type ("f") of a dialogue object (see Table 3). A buffer for type "a", "b", and "c" dialogue objects is created to store legal tokens or parsing rules. For type "h" and "i" objects, a buffer is required in storage of the contents of messages. A default option for the forced type ("a" and "c") of dialogue object can also be specified.

Since “d” and “e” type dialogue objects consist of fields, it is necessary to store information on the number of fields and field attributes. Field attributes (Bass, 1985a; 1985b) include the field’s logical name and its position, as well as its associated video attributes—length, format, default, clear character, and echo.

A level of visibility can be assigned to a dialogue object in a given dialogue cluster. Level of visibility is used to indicate when the object will be displayed, overlaid, or erased. For example, a more complex dialogue design may use Level 1 for “always visible,” Level 2 for “visible when active and staying visible unless overlaid or erased,” and Level 3 for “visible when invoked but disappearing when not active.”

In summary, a complete definition of a dialogue object includes information on the object type, dependencies between objects, and additional attributes for image descriptions. Figure 5 illustrates the definition of the dialogue object, "main menu."

![](/api/attachments/FCHNB5QJ/fulltext/images/7e96b376fab35051ec738d59e3346b2e27be0531040ebb751946c68299f8b306.jpg)  
Figure 4. (continued)

## Generation and management of dialogue definitions

One approach to specification of dialogue object definitions for an application system is through the use of software tools in dialogue generation and evaluation. Figure 6 depicts two major tools for dialogue generation and evaluation. To create and modify the definitions, the designer can use the dialogue definition generator (see Figure 7). The dialogue definition evaluator can then be used to assess the validity of dialogue definitions.

Dialogue consistency can be assessed through evaluation of dependency definitions (Reisner, 1981; 1984). However, this approach is not a complete substitute for user participation in the evaluation process. The result is a prototype of the dialogue specifications that can be tested by potential users. The designer records the findings on task completion (i.e., the relevance of the dialogue design to the actual task requirements) and user performance (e.g., efficient operation, learning, errors). The designer makes use of the prototype usage record to improve the dialogue design.

## Dialogue Manipulation

Dialogue manipulation—the handling of user, or system generated, command and user information entry—involves three basic operations: (1) selecting (e.g., moving) the “pointer” (e.g., “cursor”) to the desired location; (2) user input or selection indication; and (3) system interpretation of the signal in a decision for invocation or abortion of an action or operation. Table 4 summarizes these user operations that can be applied to the operation of a dialogue object or of an attribute within the object.

<table><tr><td>VISIBILITY: 1</td><td></td><td>/* Always visible */</td></tr><tr><td>OPTION 1:</td><td>At R+2 C+Cis “MAIN”to</td><td>/* Location relative to the UL position *//* The Syntax is MAIN *//* No transition is performed */</td></tr><tr><td>OPTION 2:</td><td>at R+3 C+2is “CREATE/SEND”to CREATE/SEND</td><td>/* Location relative to the UL position *//* The syntax is CREATE/SEND *//* Transition to the node CREATE/SEND */</td></tr><tr><td>OPTION 3:</td><td>At R+4 C+2is “READ”to READ</td><td>/* Location relative to the UL position *//* the syntax is READ *//* Transition to the node READ */</td></tr><tr><td>OPTION 4:</td><td>At R+6 C+2is “PROFILE”to PROFILE</td><td>/* Location relative to the UL position *//* The syntax is PROFILE *//* Transition to the node PROFILE */</td></tr><tr><td>OPTION 5:</td><td>At R+7 C+2is “LOCAL LIST”to LIST</td><td>/* Location relative to the UL position *//* The syntax is LOCAL LIST *//* Transition to the node LIST */</td></tr></table>

<table><tr><td colspan="4">Notations:</td></tr><tr><td>R:</td><td>Row</td><td>Size:</td><td>UL (R1 C2) LR (R9 C18)</td></tr><tr><td>C:</td><td>Column</td><td>Image:</td><td></td></tr><tr><td>UL:</td><td>Upper left</td><td></td><td>MAIN MENU</td></tr><tr><td>LR:</td><td>Lower right</td><td></td><td>----</td></tr><tr><td>At:</td><td>Specify the location of an option or item</td><td></td><td>----MAIN</td></tr><tr><td>Is -</td><td>Specify the syntax on an option or an item</td><td></td><td>----CREATE/SEND</td></tr><tr><td>To -</td><td>Specify the transition to another dialogue object</td><td></td><td>----READ</td></tr><tr><td>/* */</td><td>Comments</td><td></td><td>----PROFILE</td></tr><tr><td>Node Name:</td><td>Main</td><td></td><td>----LOCAL LIST</td></tr><tr><td>Type</td><td>“a”</td><td></td><td></td></tr></table>

Figure 5. The Definition of the Dialogue Object MAIN  
![](/api/attachments/FCHNB5QJ/fulltext/images/c616bc1776351036fb62cefbd76a3fcd9391e5a4aee95f32d095b0e4442348b3.jpg)  
Figure 6. Software Tools for Dialogue Generation and Evaluation

![](/api/attachments/FCHNB5QJ/fulltext/images/f3d41b12b34c57bfcae71d5a626d8a672b67fd775b1b1b8ac00d33f72ffef071.jpg)  
Figure 7. The Interfaces of the Dialogue Generation Tool to Create Definitions for an E-Mail System

To support these user operations, a three-layered software architecture is used for constructing the manipulation processes library. The purpose of the library is similar to that of the “dialogue handler” proposed by Coutaz (1985). The lower-layer logical device driver (see Table 5) is used for machine-dependent operations. The middle-layer management functions (see Table 6) are used for managing single operations of attributes of a dialogue object. The higher-layer control functions (see Table 7) are used for invoking a series of dialogue operations for a dialogue object.

Several aspects must be considered in the definition of the dialogue manipulation library. First, from the human factor and cognitive psychology viewpoints, “keystroke” consistency is crucial to reducing user errors and learning effort (Bewley, et al., 1983; Card, et al., 1981; Reisner, 1981; 1984). Several problems that result from inconsistency and frequently occur in traditional software design, such as the “unintentional activation” and the “slipperiness” (the user’s confusion with similar but not identical operations), are discussed by Carroll (1982) and Norman (1983). These errors can be reduced if the user-interface software enforces keystroke consistency; that is, the keystrokes for “selection” (of an object or an attribute within an object), insertion and deletion of user entry (command or data), and execution or abortion of the user operation are standardized for

Table 4. User Interface Operations

<table><tr><td>Select</td><td>Select a character (digit), a word (data or option), a line (a group of data), or a chunk of text</td></tr><tr><td>Insert</td><td>Insert a character (digit), a word (data or option), a line (a group of data), or a chunk of text</td></tr><tr><td>Delete</td><td>Delete a character (digit), a word (data or option), a line (a group of data), or a chunk of text</td></tr><tr><td>Execute</td><td>To complete the operations to initiate the internal operation (e.g., saving data, control transfer)</td></tr><tr><td>Abort</td><td>To abort the operation, no changes are made</td></tr></table>

Table 5. Lower-Layer Dialogue Manipulation Software Functions

<table><tr><td rowspan="2">Function</td><td colspan="5">Attributes</td></tr><tr><td>Positions</td><td>Character</td><td>String</td><td>Video</td><td>Lines</td></tr><tr><td>Screen Maintenance</td><td>Set cursor Erase a line Erase part line Erase screen</td><td></td><td></td><td></td><td></td></tr><tr><td>Primitive I/O Buffer Handling</td><td></td><td>Read a character Put a character</td><td>Read a string Put a string Delete character from string Copy string Shift text string String concatenate Scan long string for short string</td><td></td><td></td></tr><tr><td>Video</td><td></td><td></td><td></td><td>Set reverse video on Set reverse video off Set density</td><td></td></tr><tr><td>Communication</td><td></td><td></td><td></td><td></td><td>Set term speed Set term echo</td></tr></table>

all types of dialogue objects. Such consistency can also improve user learning (Carroll and Mack, 1984; Gaines, 1981; Reisner, 1981).

In addition, the designer must consider three software engineering issues: reusability, flexibility, and portability in constructing software utilities to facilitate dialogue manipulation. Reusability refers to the ability to share the dialogue definitions across various application systems. Flexibility refers to the dialogue management's support of different levels of analyst or end-user programming needs (e.g., low-level machine dependent; high-level dialogue object manipulation). Finally, portability is important in the reduction of development costs in dialogues that must be transported to different workstations.

## Lower-layer logical device drivers

The lower-layer software is the “device agent” or “logical device driver” for cursor movement, screen erasure, input/output of characters and strings, and video and communication handling (e.g., speed and echo). These drivers are fundamental to the manipulation of the system output and user input. Since they are hardware dependent, different lower-layer functions are required for different workstations. It is possible, however, to build the ability to handle multiple workstations into one logical device driver by having a table of various workstation attributes available to the driver. The latter approach is more flexible but less efficient.

## Middle-layer management functions

Middle-layer functions are implemented to manage basic dialogue object operations. Such functions include those for managing space, object (text, icon, image, etc.) presentation, message, definition retrieval, user entry, and data conversion. These functions are built on top of the lower-layer functions.

Table 6. Middle-Layer Dialogue Manipulation Software Functions

<table><tr><td rowspan="2">Purpose</td><td colspan="3">Dialogue Object</td></tr><tr><td>General</td><td>Command &amp; Data</td><td>Message</td></tr><tr><td>Space Management</td><td>Create display area Erase display area Move dialogue object</td><td></td><td></td></tr><tr><td>Presentation Management</td><td>Display dialogue object image Display dialogue object result</td><td></td><td></td></tr><tr><td>Message Management</td><td></td><td>Retrieve command definitions Retrieve data definitions</td><td>Put error Put status Put currency Put help</td></tr><tr><td>Definition Retrieval</td><td></td><td></td><td>Retrieve help information Retrieve message</td></tr><tr><td>User Entry Data Conversion</td><td>Get a field Retrieve general definitions From char. to int. From int. to char. From real to char. From char. to real</td><td>Get a field for a dialogue object Convert record1 to record2</td><td></td></tr></table>

Space management functions designate the view area to a dialogue object. Presentation management functions are used to display and redisplay the image of an object before and after user operations. Message management functions invoke message objects for informing the user of possible mistakes, the status of operations, etc. The help message function also provides several levels of assistance when requested by the user. Definition retrieval functions provide access to the database that stores dialogue definitions.

User-entry management functions provide basic text editing capabilities used in most user-system interactions. The most basic function, “get a field," deals with editing a string of characters or digits, commands or data on the same line. In graphically based interfaces, this takes the form of icon or image identification. Using this function, other functions are developed for complicated, compound operations (e.g., menu, forms management, drawing, or word processing). Consequently, keystroke (or mouse-click) consistency can be enforced. Different operation modes (i.e., read or update only) are also available to these functions. Data conversion management functions offer means for converting data to the needed type to protect the system from erroneous data entry and to transfer data to and from the application software.

Table 7. Higher-Layer Dialogue Manipulation Software Functions

<table><tr><td rowspan="2">Purpose</td><td colspan="3">Dialogue Object</td></tr><tr><td>General</td><td>Command</td><td>Data</td></tr><tr><td>Input-OutputControl</td><td></td><td>Get forced commandGet free command</td><td>Get forced dataGet free form dataGet free table dataGet free text data</td></tr><tr><td>DisplayControl</td><td>InitiatedialogueobjectResume screen layout</td><td></td><td></td></tr><tr><td>InternalInterfaceControl</td><td>Create a record in databaseRetrieve nth attributeUpdate nth attributeInvoke model</td><td></td><td></td></tr></table>

## Higher-layer control functions

Higher-layer functions are devised to control sequences of user operations on a dialogue object. They include accepting and interpreting user input, interpreting conditions and actions, responding to the operation requests(i.e., selection, insertion, deletion), handling necessary message operations, and maintaining the overall image of the object. A function is developed for each object type (see Table 2). The internal details of these functions are transparent to the programmer.

In command processing, a function is used for "force-choice command" processing (type "a"). This function supports various conventional methods, such as selecting an option by typing the first letter of the option or by using specialized function keys. The selected option is passed back to the calling software. In addition, the keystrokes used to select text (e.g., select previous word/line, select the next word/line) can be used to select options. This arrangement accommodates variance in the current methods for selecting command and text. Another function is used to process the free command entry (type "b"). It also performs parsing and returns only meaningful command tokens back to the caller. While entering the commands, the user can apply regular text editing keystrokes to perform selection, deletion, and insertion.

For each data type ("c"- "g"), one higher-layer software function is designated. The function for type "c" is the simplest, similar to the "forced-choice command" function. The type "d" function is particularly useful for processing forms consisting of data items, such as an expense report. The type “e” function is useful for handling repeating items for a table and a record in the database. It also offers the selection and deletion of a line (a record occurrence or a tuple) by using the standard text editing methods of the type “f” function. The type “f” function is actually a full-capability window-oriented word processor. Type “d” through “f” functions can be made to satisfy “read” or “update” only requirements. The type “g” function displays a message (passed text) in the assigned area and accepts the entry for storage in the return buffer. The display and entry will be maintained within the object’s view port, including scrolling the lines if the area is full. It can also validate the user response against a requirement defined by the calling software.

Errors, status, currency, and help messages are also handled by the higher-level functions, which necessarily invoke middle-level message management functions.

In addition, there are general-purpose, higher-layer functions: display and internal interface control functions. Display control functions are used to manage the utilization of the display area by different dialogue objects. The display device has a physical display screen. Different dialogue clusters will use the same screen for objects that they are capable of handling. Each cluster is then said to have its own logical display screen. The display control functions perform four functions: (1) raising the logical screen and view ports; (2) activating dialogue objects; (3) deactivating dialogue objects; and (4) resuming and erasing the logical screen and dialogue objects.

The internal interface control functions are necessary to invoke database management and model computation functions, if these functions are available in the network environment. In order to interface with DBMS functions, interface control functions are needed to create a corresponding database record, to retrieve and update a particular field of the corresponding record of the dialogue object, and to access and update the corresponding record occurrences. By the same token, other functions are required to invoke computation models, file sorting programs, etc.

## Programming interface

Software development with the dialogue manipulation library is achieved through function calls. To develop the logic to manipulate a dialogue object, the designer uses the higher-layer functions. A function call by the application software will trigger all necessary operations on each attribute of an object, and the resulting commands or data will be transferred back to the calling software. In order to manipulate a dialogue cluster, the designer relies on the dependency information and repeats the process for individual objects. These higher-layer functions also keep track of current objects and the current dialogue cluster. Thus, programming for applications includes a series of calls to higher-level functions, beginning with the main (first) object. The handling of input/output, messages, etc., becomes transparent.

Middle- and lower-layer functions can also be used to satisfy specific design requirements. Some middle- and lower-layer functions can be invoked independently to develop application systems with unspecified dialogue definitions. For example, a report generation application that requires little dialogue, but relies heavily on database operations, can invoke the middle- and lower-layer functions for its own needs. It thus becomes more flexible and can meet different levels of end-user dialogue needs.

Application systems can share the library, resulting in improved software reusability. The software is also more portable, for if necessary, only the lower-layer software will be modified. Thus, variance in hardware on the network for the application system has a limited impact. In this way, heterogeneous workstation devices can operate under heterogeneous communications protocols, supporting interoperability.

Keystroke-level consistency is increased for application software that uses these higher-layer functions. For example, deletion, insertion, and cursor movement of a character (digit), a word (field), or a line (a record occurrence) are the same regardless of the difference in the object types. Several specialized function keys may be utilized to increase operational efficiency. The interpretation of key definitions is also standardized. Other means of interface, such as using a mouse, can easily be added to the library by adding lower-layer functions, without affecting the keystroke consistency of the higher-layer functions.

Finally, when the dialogue manipulation functions are invoked, a dialogue currency to indicate the currency dialogue object is maintained by these functions. The “dialogue currency” concept, which emphasizes that the effects of lower- and middle-layer functions apply only to the current dialogue object, is important in understanding the use of lower-layer functions. For example, when the “reverse video” function is called to manipulate the image of one object, subsequent calls to other functions on other objects will not be affected. This arrangement can further increase the dialogue developer’s productivity because the currency indicator is maintained automatically by the manipulation functions.

## Conclusions and Opportunities for Further Research

In summary, this article has presented a structured approach to dialogue management based on a concept of dialogue independence. The approach identifies responsibilities for two major design phases: dialogue definition and dialogue manipulation. This approach differs from the traditional dialogue design approach in two respects. First, the dialogue manipulation is no longer a part of the software of the application system and, second, dialogue object and relation definition is separated from the defined manipulation of dialogue objects. As has been discussed, the benefits include: (1) simplified design method by concentration on object definition; (2) ability to incorporate human factors into the design to satisfy user requirements; (3) easy-to-modify design; (4) division of design responsibilities among specialists; (5) shareable dialogue definitions and reusable software design to achieve more standardized dialogues across application systems; (6) more portable and flexible dialogue manipulation software for implementation on incompatible workstations; (7) support for adaptive and “learning” dialogues; and (8) the overall reduction of design and implementation costs.

An implication of the approach is the separation of individual dialogues, permitting multiple dialogues for each application. The result may mean an increase in the overall productivity of endusers. A typical end-user environment frequently involves many incompatible workstations, each equipped with a variety of systems and application packages from different vendors. Users are required to employ application systems with confusing dialogue standards. They may also be forced to use different workstations at various times. This situation poses a serious threat to user interface design because, often, similar functional software systems have to use different dialogues in adapting to a specific workstation's features. Such dialogues are particularly confusing to novice users (Eason, 1984; 1976; 1980; Paxton and Turner, 1981). Moreover, the cost of training every user in various application systems on any workstation will be prohibitive unless dialogue standards are developed.

Through adoption of the approach presented, interoperable dialogues in a heterogeneous workstation environment can be created. Dialogue definitions of different application systems are developed and evaluated in a central location, and application systems can share dialogue objects without much difficulty. Furthermore, the manipulation software can be transported easily to different workstations. The development of application systems relies on a dialogue manipulation software with ensured keystroke consistency. Dialogue standards for common physical and functional interfaces across different system settings result in dialogue interoperability.

From the information systems professional's viewpoint, the approach facilitates dialogue sharing and reusability that should prove important in the reduction of development and maintenance costs. With the aid of software tools for dialogue definition and manipulation, the designer's productivity can be improved with a significant impact on the reduction of development time and effort. Dialogue designs should prove to be more reliable and more responsive to changes, and new applications can be added without affecting the overall dialogue consistency. Finally, designers of successful decision support systems can follow the approach to develop easy-to-learn, easy-to-use, and easy-to-recover dialogues. The object-oriented framework discussed might be used in a description of dialogues across proprietary dialogue managers, such as Apple's

Hyper Card and IBM's SAA programmer support environment.

The concepts discussed in this article are being utilized in the study of adaptive user interfaces and the construction of a generalized dialogue manager (or the Dialogue Socket (Coutaz, 1985)). Dialogue definitions can be tailored to meet the needs of different users. The study of adaptive user interface will emphasize formal grammars for transforming different user requirements into the specifications of objects and their dependencies. Furthermore, a generalized dialogue manager, as with database management systems, can be a powerful software tool for user interface design. The dialogue design concepts discussed earlier are being used to develop languages and associated software tools for describing the dialogue schema and for manipulating dialogues.

## References

Andriole, S. Interactive Computer-Based Systems Design and Development, Petrocelli Books, New York, 1983.

Bannon, L., Cypher, A., Greenspan, S. and Monty, M. "Evaluation and Analysis of Users' Activity Organization," CHI '83 Proceedings, 1983, pp. 54-57.

Bass, L. "An Approach to User Specification of Interactive Display Interfaces," IEEE Transactions on Software Engineering (SE-11:8), August 1985a, pp. 686-698.

Bass, L. "A Generalized User Interface for Application Programs," Communications of the ACM (28:6), June 1985b, pp. 617-628.

Benbasat, I. and Dexter, A. "An Experimental Study of the Human/Computer Interface," Communications of the ACM (24:11), November 1981, pp. 752-762.

Bewley, W., Roberts, T., Schroit, D., and Verplank, W. "Human Factors Testing in the Design of Xerox's 8010 STAR Workstation," CHI '83 Proceedings, 1983, pp. 72-77.

Booch, P. "Object-Oriented Development," IEEE Transactions on Software Engineering (SE-12:2), February 1986, pp. 211-221.

Borgida, A., Greenspan, S. and Mylopoulos, J. "Knowledge Representations as the Basis for Requirements Specifications," Computer (18:4), April 1985, pp. 82-90.

Bracchi, G., Pernici, B. and Milano, P. "The Design Requirements of Office Systems," ACM Transactions on Office Information Systems (2:2), 1984, pp. 151-170.

Card, S., Moran, T. and Newell, A. "The Keystroke-Level Model for User Performance

Time with Interactive Systems," Communications of the ACM, (23:7), July 1981, pp. 396-410.

Card, S., Moran, T. and Newell, A. The Psychology of Human-Computer Interaction, Lawrence Erlbaum Associates, Hillsdale, NJ, 1983.

Carey T. "User Differences in Interface Design," IEEE Computer (15:11), November 1982, pp. 14-20.

Carlson, E., Metz, W., Muller, G., Sprague, R. and Sutton, J. Display Generation and Management Systems for Interactive Business Applications, Fridr. Vieweg & Sohn, Braunschweig, Wiesbaden, 1981.

Carroll, J. and Thomas, J. "The Adventure of Getting to Know a Computer," Computer (15:11), November 1982, pp. 49-58.

Carroll, J. and Thomas, J. "Metaphor and the Cognitive Representation of Computing Systems," IEEE Transactions on Systems, Man, and Cybernetics, 12, 1982, pp. 107-116.

Carroll, J. and Mack, R. "Learning to Use a Word Processor: By Doing, By Thinking, and By Knowing," in Human Factors in Computing Systems, J.C. Thomas and M. Schneider (eds.), ABLEX, Norwood, NJ, 1984, pp. 13-51.

Carroll, J. and Carrithers, C. "Training Wheels in a User Interface," Communications of ACM (27:8), August 1984, pp. 800-806.

Coutaz, J. "Abstractions for User Interface Design," Computer, September 1985, pp. 21-38.

Dean, M. "How a Computer Should Talk to People," IBM System Journal (21:4), 1982, pp. 424-453.

Dehning, W., Essig, H. and Maass, S. The Adaptation of Virtual Man-Computer Interfaces to User Requirements in Dialogs, Springer-Verlag, Berlin, Heidelberg, New York, 1981.

Eason, K. "The Manager as a Computer User," Applied Ergonomics (5:1), 1974, pp. 9-14.

Eason, K. "Understanding the Naive Computer User," The Computer Journal (19:1), 1976, pp. 3-7.

Eason, K. "Dialogue Design Implications of Task Allocation Between Man and Computer," Ergonomics (23:9), 1980, pp. 881-891.

Edmonds, E. “Adaptable Man/Machine Interfaces for Complex Dialogues,” Proceedings of the European Computing Congress, 1978, pp. 639-646.

Edmonds, E. "Adaptive Man-Computer Interfaces," in Computing Skills and the User Interface, M.J. Coombs and J.L. Alty (eds.), Academic Press, London, 1981, pp. 389-426.

Foley, J. and Wallace, V. "The Art of Natural Graphic Man-Machine Conversion," Proceedings of the IEEE, April 1974.

Gaines, B. "The Technology of Interaction-Dialogue Programming Rules," International Journal of Man-Machine Studies (14:), 1981, pp. 133-150.

Gait, J. "An Aspect of Aesthetics in Human-Computer Communications: Pretty Windows," IEEE Transactions on Software Engineering (SE-11:8), August 1985, pp. 714-717.

Jacob, R. "Using Formal Specifications in the Design of a Human-Computer Interface," Communications of the ACM (26:4), April 1983, pp. 259-264.

Kasik, D. "A User Interface Management System," Computer Graphics (16:3), July 1982, pp. 99-106.

Kieras, D. and Polson P. "An Integrated Approach to Designing Business Systems," Working Paper No. 2, University of Arizona, October 1, 1982.

Lipkie, D. "Star Graphics: An Object-Oriented Implementation," Computer Graphics (16:3), July 1982, pp. 115-123.

Malone, T. "Heuristics for Designing Enjoyable User Interfaces: Lessons from Computer Games," in Human Factors in Computing Systems, J.C. Thomas and M. Schneider (eds.), ABLEX, Norwood, NJ, 1984, pp. 1-12.

Miller, G. “The Magic Number Seven, Plus or Minus Two: Some Limits On Our Capacity for Processing Information,” The Psychology of Communication, Allen Lane, London, 1968.

Miller, L. and Thomas, J., Jr. "Behavioral Issues in the Use of Interactive System," International Journal of Man-Machine Studies (9), 1977, pp. 509-536.

Moran, T. "The Command Language Grammar: A Representation for the User Interface of Interactive Computer Systems," International Journal of Man-Machine Studies (15), 1981, pp. 3-50.

Morland, V. "Human Factors Guidelines for Terminal Interface Design," Communications of the ACM (26:7), July 1983, pp. 484-494.

Mozeico, H. "A Human/Computer Interfaces to Accommodate User Learning Stages," Communications of the ACM (25:2), February 1982, pp. 100-104.

Norman, D. "Design Rules Based on Analysis of Human Error," Communications of the ACM (26:4), April 1983, pp. 254-258.

Parnas, D. "On the Use of Transition Diagrams in the Design of a User Interface for an Interactive Computer System," Proceedings of 24th National ACM Conference, 1969, pp. 379-385.

Partridge, D. and James, E.B. "Compiling Techniques to Exploit the Pattern of Language Usage," Software-Practice and Experience, No. 6, 1976, pp. 527-539.

Paxton, A. and Turner, E. "The Application of Human Factors to the Needs of the Novice Computer User," International Journal of Man-Machine Studies (20), 1981, pp. 137-156.

Reisner, P. “Formal Grammar and Human Factors Design of an Interactive Graphics System,” IEEE Transactions on Software Engineering (SE-7:2), 1981, pp. 229-240.

Reisner, P. "Formal Grammar as a Tool for Analyzing Ease of Use: Some Fundamental Concepts," in Human Factors in Computing Systems, J.C. Thomas and M. Schneider (eds.), ABLEX, Norwood, NJ, 1984, pp. 53-78.

Roach, J. and Nickson, M. “Executable Logic Specifications for Modeling and Developing Human/Computer Interfaces,” technical paper, Virginia Polytechnic Institute & State University, Blacksburg, VA, 1984.

Row, L. and Shoens, K. "Programming Language Constructs for Screen Definition," IEEE Transactions on Software Engineering (SE-9:1), 1983, pp. 31-39.

Snodgrass, R. "An Object-Oriented Command Language," IEEE Transactions on Software Engineering (SE-9:1), 1983, pp. 1-12.

Sprague, R. "Decision Support Systems: A Tutorial," DSS Conference, 1981.

Tanner, P. and Buxton, W. “Some Issues in Future User Interface Management System (UIMS) Development,” technical paper, University of Toronto, Toronto, Canada, 1983.

Tesler, L. "The Small Talk Environment," Byte (6:8), August 1981, pp. 90-147.

Thimbleby, H. "Dialogue Determination," International Journal of Man-Machine Studies (13), 1980, pp. 295-304.

Wasserman, A.I. and Shewmake, D.T. "Rapid Prototyping of Interactive Information Systems," ACM Software Engineering Notes (7:5), 1982, pp. 171-180.

Wasserman, A. "Extending State Transition Diagrams for the Specification of Human/Computer Interaction," IEEE Transactions on Software Engineering (SE-11:8), 1985, pp. 699-713.

Wong, P. and Reid, E. "FLAIR—User Interface Dialogue Design Tool," Computer Graphics (16:3), July 1982, pp. 87-98.

## About the Authors

Feng-Yang Kuo is an assistant professor of information systems in the Graduate School of Business, University of Colorado at Denver. He received his Ph.D. degree in management information systems from the University of Arizona. His research interests include the design of user-computer interfaces, office automation, database management, and expert systems.

Benn R. Konsynski received the Ph.D. degree in computer sciences from Purdue University. He is currently at the Harvard Business School and is a professor on leave from the Management Information Systems Department at the University of Arizona. His research interests include model management, inter-organizational systems, computer-aided systems analysis and design and group decision support. His current research focus is on the role of information technologies in innovative organizational and systems design.
