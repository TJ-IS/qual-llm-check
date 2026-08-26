---
otero_id: 16955
otero_key: "4QGZGR6Y"
title: "Adapting demons to knowledge management environments"
authors: "C.W Holsapple"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90100-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Adapting Demons to Knowledge Management Environments

C.W. HOLSAPPLE

Purdue University, West Lafayette, IN 47907, USA

Decision support systems depend on a variety of knowledge management techniques. These range from data base management, programming, and spreadsheet analysis to rule set management and automated inference. One valuable knowledge management technique that has yet to find its way into the repertoire of decision support system developers is general-purpose demon management. This article identifies and explores the major issues pertaining to the integration of demon representation and processing into a knowledge management environment. These serve as a basis for design and implementation of more flexible and powerful environments for decision support.

Keywords: Decision Support Systems, Demons, Environments, Event-triggered Processing, Integration, Knowledge Management.

![](/api/attachments/4QGZGR6Y/fulltext/images/9826859051dca01e9a4bbeadf336cf9c6c05ddc616b417d81499f81eaed49d3e.jpg)

Clyde W. Holsapple is on the faculty of the Krannert Graduate School of Management at Purdue University. He was formerly Associate Professor of Business Administration at the University of Illinois (Champaign). His teaching and research interests are in the areas of data base management, decision support systems, knowledge management, software integration, and managerial applications of artificial intelligence. His books include Foundations of Decision Support Systems and Micro Database Management - Practical Techniques for Application Development from Academic Press, and Business Expert Systems from Richard D. Irwin. His research articles have appeared in numerous journals including Decision Sciences, Informations Systems, Operations Research, Policy Sciences, The Computer Journal, Information Society, and PC Tech Journal.

## 1. Introduction

Conventional techniques for managing knowledge are important for developing decision support systems. These techniques include data base management, spreadsheet analysis, programming, forms management, graphics generation, and text management. When the processing capabilities of such techniques are integrated into a single, unified environment for knowledge management, the result is a powerful generalized problem processor [2]. The techniques' respective knowledge representation capabilities define what is possible in the knowledge system of a decision support system (DSS) built in such an environment.

When artificial intelligence techniques are incorporated into these environments, developers can build much more powerful application systems for both decision support and record-keeping [3]. An important practical advance along these lines was made with Guru [4, 8], which integrates the technique of rule management into an environment that also furnishes familiar business computing capabilities. Fig. 1 illustrates the characteristics of this environment within the classic DSS framework. Rule management involves the representation of reasoning knowledge as sets of rules and the processing of rule sets via inference. That is, the problem processor has an inference capability and the knowledge system can accommodate rule sets.

It is extremely important to understand that the various problem processor capabilities identified in fig. 1. are fused into a single software tool. They are not isolated software tools or separate programs. The result is a synergy in which the total effect is much more than the sum of the effects that could be achieved with separate tools and in which no processing technique dominates any of the others. For instance, spreadsheet analysis can use rule management to infer the value of a cell. Conversely, rule management can use spreadsheet analysis in the midst of attempting to infer some advice in response to a consultation request. Similar synergy exists for other problem processor capabilities.

![](/api/attachments/4QGZGR6Y/fulltext/images/3a076618d479180929d88f83bceee29bb0455b80776865badbefc281fa376cae.jpg)  
Fig. 1. Existing Environment for Decision Support.

Beyond integral rule management, there are other contributions that artificial intelligence research can make to developers of decision support systems. The focus here is on one of these, namely the notion of demons. Following a brief introduction to demons, this article proposes that general purpose demon management facilities be synergistically integrated into a knowledge management environment. It proceeds to identify and explore the important issues that must be considered in order to accomplish such an integration. The discussion provides guidelines for incorporating demon management into a decision support system development tool, particularly a tool that serves as a full-scale environment for managing diverse types of knowledge in a coordinated fashion. The presented concepts are also intended to stimulate further research into the application of demons in decision support contexts.

## 2. Evolution of Demons

Early notions of demons were developed to model pattern recognition in the context of a learning process [7]. Selfridge distinguishes between cognitive demons and decision demons. Each cognitive demon corresponds to a particular pattern and is able to 'view' images (e.g., an arrangement of data values). A cognitive demon computes a measure of the similarity between its pattern and the image being viewed. Computed similarity measures are monotonic and are referred to as 'shrieks'. For a given image, the cognitive demons perform their respective computations in parallel. The decision demon decides how to interpret an image, by choosing the pattern corresponding to the cognitive demon emitting the loudest shriek (i.e., highest similarity measure).

Winograd suggests that demons can be used as pattern understanding mechanisms during a parsing process [9]. They augment the customary proluctions used to characterize a language's grammar. For instance, a demon may be defined for a certain word in the grammar. This definition consists of specifying certain operations that are to be performed automatically whenever the word is encountered in the parsing process. Winograd maintains that demons of this kind provide a valuable mechanism for handling complex constructions and irregular cases when developing a system for linguistic analysis.

Demons have come to be regarded as an essential feature of frame management systems, where they offer a way of handling the notion of procedural attachment [1]. In such systems, an object or class of objects is represented as a frame. A frame is an aggregate of slots, each depicting some attribute of the object or class being represented. Procedures, in the guise of programs (typically in LISP), can be attached to a frame. Such a program is called a demon if it is automatically executed in response to a certain event having occurred for the frame. For instance, the event of filling values into the slots of a frame may cause the automatic execution of a program. This program is called the frame's 'if-filled' demon. Conversely, an 'if-needed' demon would be a program that is executed whenever the frame's slot values need to be examined or used in some way. Such a slot may be called a virtual slot or its demon may be called an 'active value'.

When a demon is attached to a frame representing a specific instance of an object, that demon is called a 'trap'. When attached to a frame representing a class of objects, it is called a 'trigger' [1]. A trigger demon is applicable to all instance frames related to the class frame in a frame hierarchy. Demons may be attached to individual slots as well as frames. The ability to specify demons is commonplace in today's frame management systems (e.g., Intellicorp's KEE). Thus, the feasibility of implementing demons has been demonstrated, although such systems do not treat demon management as a general-purpose technique that can be exercised outside of the confines of frame processing (i.e., in a decision support environment).

Limited kinds of demon specification are not unusual with more conventional systems for knowledge management. However, such specifications are neither thought of nor referred to as demons [6]. For example, there is a spreadsheet system that allows a user to designate special visual effects (reverse video and blinking) for the display of a cell value. Such a ‘when displayed’ demon can be specified in a conditional, but non-procedural, manner. Whenever it is time to display a cell’s value, that cell’s demon is processed. If conditions specified in the demon are met, the special effects become visible for that cell; otherwise normal display characteristics are used.

As another example, declaring a range of feasible values for a data base field can be regarded as specifying a nonprocedural ‘when-changed’ demon. Similarly, providing the expression for a virtual field is akin to specifying a nonprocedural ‘when-needed’ demon for that field. Programming languages that allow programmers to define a procedure of commands to be executed whenever an error condition arises are, in effect, providing a facility for ‘when-error’ demons.

Even though there are such surreptitious demon mechanisms, conventional software has yet to directly address the notion of general-purpose demon representation and processing. The potential benefits of providing general purpose demon management facilities to application developers are increased convenience and productivity. The existence of surreptitious demons is a testimony to their practical value. A general-purpose demon management capability will provide single, unified technique for dealing with the frequent application developer need of having some desired processing carried out without having to explicitly request it. This is the case regardless of whether the application system being built is a management information system, decision support system, expert system, or some combination of these.

## 3. Demon Management in a Knowledge Management Environment

Integrated knowledge management environments can be very valuable in development of management information systems, decision support systems and real time expert systems [6]. A knowledge management environment synergistically integrates [5] a broad range of knowledge representation and processing techniques into a single software tool. As fig. 1 suggests, the integrated techniques might include data base management, spreadsheet management, programming, form management, graphics generation, text management, rule management, and so forth. Rather than having a distinct tool for each technique, the developer has a single environment offering not only the capabilities of separate tools but also the many otherwise nonexistent capabilities that result from their fusion.

![](/api/attachments/4QGZGR6Y/fulltext/images/389a131d0b83b5311d6761e0076fa2bea1ff645e2655df540808e00aa3abd02c.jpg)  
Fig. 2. Incorporating Demons into the Environment.

The introduction of demon management capabilities into such an environment (see fig. 2) multiplies its value to a developer. How to accomplish this raises many issues. The results of resolving these issues could also be applied to introducing general-purpose demon management into more limited development tools. The overriding requirement for integrating demon management into an environment is adherence to the principle of synergy. This means that a demon can make use of other knowledge management capabilities and each of these other capabilities can make use of a demon

Just as traditional barriers between spreadsheet processing and data base management disappear in an environment, so too do the barriers between demon processing and data base management vanish. Demon processing may involve data base management and data base management may involve demon processing. For instance, a triggered demon may retrieve or alter data base contents as it carries out its work. The triggering itself may or may not have been due to a data base operation. Conversely, when an attempt is made to alter a field's value, a demon may be triggered to ensure the validity of the change, to log the change, to make consistent changes to a spreadsheet, etc.

Similarly, demons may be operative for spreadsheets, forms, programs, text, templates, graphs, and so forth. At the same time, the processing that a demon performs may work on or with spreadsheets, forms, programs, text, templates, graphics, and so on. This synergy implies that, like other objects in the environments, a demon can be defined independently of the act of defining other objects. It is neither subservient nor superior to other kinds of objects in a knowledge system.

In a knowledge management environment, a demon is an object that defines some event-triggered behavior. Whenever the environment detects an occurrence of the event, the corresponding demonic behavior is enacted. Within this broad mandate, there are several important issues about demon representation and processing that need to be resolved, including types of events that can trigger a demon, objects with which demons can be affiliated, binding demons to objects, demon activation, and the definition of demonic behavior. These issues are now explored in this sequence.

## 4. Events in a Knowledge Management Environment

By its very nature, a demon's processing is never explicitly requested by a user of the environment or by an object in the environment. That is, the environment's language interfaces will contain no commands or options for carrying out the processing embodied in a demon. Thus a demon is very different than other objects such as programs and rule sets whose embedded processing is carried out as the result of explicit invocation. The processing of programs or rule sets is actively triggered by commands rather than by events.

There are two basic types of events that can trigger a demon. They will be referred to as ‘when-changed’ and ‘when-needed’ events. The former means that when something changes an appropriate demon is triggered (i.e., the processing is carried out). Similarly, the latter means that when something is needed an appropriate demon is triggered. Demons can be classified according to which kind of event can trigger them, giving a basic distinction between when-changed demons and when-needed demons.

Each of these categories may be further partitioned as shown in fig. 3. The when-changed demons span different kinds of changes including creation of something new, alteration of something that exists (its structure, content, or location), and deletion of something that exists. When-needed demons include those that are triggered only when something is needed but unknown, those triggered whenever something is needed regardless of whether it is already known, and those triggered only when the needed something is known. For a particular something, it may be desirable to have a demon of each type, thereby allowing different demons to be triggered for the various events that can be experienced.

It should be noted that demons can be further distinguished with respect to the timing of their triggering. For example, one when-changed demon may be triggered immediately on completion of the change (e.g., a demon that logs an event), while another when-changed demon is triggered as soon as the change is imminent but before it is actually made (e.g., a demon that checks for event validity). A similar temporal distinction can be made for when-needed demons.

![](/api/attachments/4QGZGR6Y/fulltext/images/67cb2ce4e9912f74c7db408b1f18ed290271b37604ec9bcc4930fbf77fe8b234.jpg)  
Fig. 3. Types of Demon Triggering Events.

Both when-changed and when-needed demons (and their variants) can be triggered by relevant events occurring anywhere and anytime within the knowledge management environment. For instance, they may be triggered in the midst of a rule set consultation, during a program execution, while browsing through a relational data table, within the processing of an SQL query, when working on a piece of text, as user responses are entered into a form, when a spreadsheet cell's value is calculated, during the generation of a report from a template, and so forth. Any event that triggers a demon is an event that happens to something. But what is that something? Clearly, it must be some object (or group of objects) that exists in the knowledge management environment.

## 5. Objects in a Knowledge Management Environment

Many prefabricated classes of objects exist in a knowledge management environment [5]. As the knowledge system in fig. 1 shows, these include tables, forms, spreadsheets, programs, text, templates, rule sets, variables, and so forth. Methods for processing each kind of object are furnished as part of the environment and can be used to process specific instances of the objects. Of the many kinds of objects, variables are the most granular. In the course of working within an environment variables are continually needed and subject to change. As a starting point, consider the events pertaining to variables as the basis for demon triggering.

Many kinds of variables are available in a knowledge management environment including fields, spreadsheet cells, program variables, array elements, inference variables, environment variables, utility variables, and internal variables. The last three deserve a bit of explanation, while the others are well-known. An environment variable is one whose value governs some aspect of the environment's behavior, such as which background color should appear on the console screen. A utility variable is one whose value may be altered by the environment to reflect the current state of processing, such as an indication of the most recently encountered error (if any). An internal variable is one whose value can be examined functionally, such as an indicator of the most recent keystroke. In addition, fuzzy (i.e., multi-valued) variables may be allowed and certainty factors may be permitted for variable values [6].

The integration of demon management into an environment should allow a demon to be affiliated with any variable. If a when-changed demon is affiliated with a variable, that demon is triggered whenever the variable's value is changed. $^{1}$ Similarly, if a when-needed demon is affiliated with the variable, that demon is triggered whenever the variable's value is needed. It should be kept in mind that a variable's value can be contingent on the values of several other variables. That is, its value may change only when values of all of these others have changed. Thus, a demon can in effect be affiliated with an entire group of variables and be triggered only when all have changed.

Some variables have additional facets, beyond the notion of a value. For instance, a cell has not only a value but also a definition that controls how its value is to be computed. Working variables used in programs and rule sets can have certainty factors that accompany their values. Fields can have other facets such as pictures and labels. Conceivably, these other facets of variables could be subjected to when-needed or when-changed demons.

Aggregate objects composed of variables are also candidates for being affiliated with demons. From a frame perspective, variables serve as slots in these more encompassing objects. They include records, blocks of spreadsheet cells, blocks of array elements, entire spreadsheets, and arrays. At a still higher level, an entire table could have affiliated demons. Other objects in a knowledge management environment that could meaningfully be affiliated with when-changed and/or when-needed demons include pieces of text, forms, templates, macros, menus, graphs, programs, and rule sets. Even demons themselves could be affiliated with other demons.

Another interesting possibility, reminiscent of Winograd's notion of parsing demons, is the affiliation of 'when-needed' demons with specific commands supported by the environment. Whenever the environment needs to execute a command (e.g., the SQL SELECT command), that command's when-needed demon is triggered. Here, demons are affiliated not with objects, but with the methods available for processing objects.

## 6. Binding Demons to Objects

When a demon is to be affiliated with some object, the environment must provide some mechanism for this binding to take place so that the object becomes possessed by the demon. Conceivably, there are two basic approaches to binding. They can be characterized as static and dynamic. A mixture of the two approaches is also conceivable, allowing dynamic bonds to override static bonds.

The static approach requires that binding be established at object definition time. This may be during either the definition of the possessed object or the definition of the demon object. As an example of the former, when a field is being defined, a when-changed demon for validation may be specified as part of the field definition activity. This binds the demon to the field so that whenever a change is made to the field, this demon is triggered. Alternatively, a demon is defined independently of other objects (as discussed further below). In this case, the static binding happens as the demon is being defined. The object (or objects) that it is to possess is listed along with an indication of whether the demon is to play a when-changed or when-needed role.

A dynamic approach to binding requires that a bond be established after both the demon and the object that it is to possess have been defined. This is accomplished with a command that cites the demon by name, and lists all objects that are to be bound to it, and possibly indicates the type of event that can trigger the demon for these objects. Alternatively, the event type (e.g., when-changed) could be specified as part of the demon definition process. A similar command is available to unbind or 'exorcise' a demon from an object to which it has been dynamically bound.

## 7. Demon Activation

In a knowledge management environment, all objects may not be actively in use at all times. In the interest of processing speed and efficient memory utilization, those objects not of immediate interest can remain inactive until they are to be processed. Because a demon is an object, the same should be true of it. To this end, the environment will support commands for activating and deactivating demons. Once a demon is activated, the environment will carry out the demon's defined processing behavior whenever it is triggered. Inactive demons cannot be triggered, nor can dynamic binding and unbinding be accomplished for inactive demons.

Demon activation raises the question of how many demons can be active simultaneously for a given object. Clearly, a demon can be concurrently active for multiple objects if they all have been bound to it. It is also clear that an object can have an active when-needed demon and an active when-changed demon at the same time. However, a conflict occurs if an attempt is made to have two active when-changed demons for a given object. One resolution is to disallow an activation or binding attempt that would produce such a state of affairs. Another is to employ only the most recently bound or activated when-changed demon for the object.

If multiple active when-changed demons are to be permitted for an object, an ordering and a termination criterion must be established for them. One way to handle the ordering is to allow a priority and/or a cost to be specified for each demon as it is defined. The environment carries out demon processing on a highest priority, lowest cost basis. The demon processing may terminate simply when all applicable demons have been exhausted. Alternatively, there may be an environment variable to control how exhaustive the processing will be.

Demon activation and dynamic binding can become onerous in applications where there are very large numbers of demons and objects. Therefore, it is desirable for an environment to furnish a way for referring to many demons as a whole when activating or dynamically binding them at the same time. This may imply a logical structuring, physical structuring, or indexing of demons. For instance, it should be possible for a single command to activate all demons statically bound to cells of some spreadsheet or to the input elements of some form.

Table 1
Design Options.

<table><tr><td rowspan="3"></td><td colspan="2">Trigger Timing</td><td colspan="12">Object Type</td></tr><tr><td rowspan="2">Pre</td><td rowspan="2">Post</td><td colspan="8">Variable</td><td colspan="4">Aggregate</td></tr><tr><td>Field</td><td>Cell</td><td>Prg</td><td>Elem</td><td>Inf</td><td>Env</td><td>Util</td><td>Intern</td><td>Record</td><td>Table</td><td>Block</td><td>SpSheet Array</td></tr><tr><td>When-Changed Creation Alteration Deletion When-Needed Unknown Known Either</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 8. Defining a Demon

When a demon is defined (or altered), the behavior that it will exhibit when triggered is specified. In a knowledge management environment, this specification consists of a sequence of any commands generally supported for processing objects. They might involve commands for program execution, data base retrieval, spreadsheet analysis, rule set consultation, graphics generation, remote communications, and so on. Caution must be exercised when handling potentially recursive situations. For example, a demon may have been triggered as a result of changing the value of a field in the current record of some table. It may be undesirable for the demon itself to change the table's currency indicator or change the same field before normal processing resumes. In the first case, the table may become inconsistent. In the second case, the demon would be triggered from within itself, possibly resulting in an infinite regress.

In addition to judicious use of usual knowledge management commands, new commands concerned with demon termination will also appear in a demon specification. The most obvious of these is a command for the environment to immediately abandon its execution of the demon process and resume execution at the point following the triggering of the demon. A second kind of termination resumes executing by restarting the event that triggered the demon. Such a termination would, for instance, be important for a demon that does validity checking. Upon detecting an invalid attempt to make a change, the demon could terminate its processing by giving the user another chance to make a valid change.

As noted earlier, it should be possible to define (and alter) a demon independently from defining other kinds of objects. Syntactically, such a definition might have the following kind of appearance:

$$
\begin{array}{l} \text { DEMON   demon - name   demon - type } \\ \text {[priority][cost]} \\ \text { object - list } \\ \text { command - list } \\ \text { ENDDEMON } \end{array}
$$

where demon-name is a unique name that will be used when activating or editing this demon and demon-type indicates whether this is a when-needed or when-changed demon. The optional priority and cost are relevant only if multiple demons of the same type are allowed to be active simultaneously for the same object. If static binding is allowed, the object-list is simply a list of the objects to which this demon will be bound whenever it is activated. As a convenience, it may be advisable to allow demon definitions (or references) to be embedded in definitions of other objects. In such a case the object-list would be omitted. The command-list consists of any sequence of knowledge management commands that can be used in the environment. An additional clause in the demon specification might be used to denote the demon's physical location or logical group.

## 9. Concluding Observations

Traditional DSS development tools have no unified and comprehensive way for addressing a very common processing need: namely, event triggered processing. With the possible exception of a few piecemeal facilities for event triggered processing, it is generally up to the DSS developer or user to explicitly monitor the occurrence of events and take appropriate actions. Demon management provides an interesting alternative.

<table><tr><td colspan="8">Other</td><td colspan="3">Binding</td></tr><tr><td>Text</td><td>Form</td><td>Template</td><td>Menu</td><td>Graph</td><td>Program</td><td>Rule Set</td><td>Macro</td><td>Static</td><td>Dynamic</td><td>Both</td></tr></table>

Integration of demon representation and processing capabilities into knowledge management environments can significantly increase the value of such environments to developers of both management information and decision support systems. Rather than explicitly invoking procedures or consulting rule sets every time certain events occur, demons become part of a knowledge system and a developer can rely on the environment to automatically carry out desired processing whenever those events happen. The emphasis here has been on general-purpose demon management, rather than limited or specialized renditions of the demon technique.

Results of the integration proposed here are the incorporation of this useful artificial intelligence technique into the mainstream of business computing and the enrichment of the technique itself. The diverse kinds of actions that can be specified when defining a demon, coupled with the diverse contexts in which demons can be triggered, go well beyond the usual scope of demons that do not participate in extensive knowledge management environments (e.g., those involved in frame systems). Given that demon processing has already been implemented in more restrictive ways, relaxation of these restrictions along the lines suggested here does not in principle present insurmountable implementation obstacles.

The issues identified and explored in this article provide a basis for designing and implementing an environment that offers a general-purpose demon management capability. The chart in table 1 summarizes many of the design options. Which options are chosen depends largely on implementation constraints, the purpose of the environment (e.g., is spreadsheet processing necessary), and how ambitious the environment's creator is.

Beyond the practical design issues, perhaps this article's seminal ideas about demon management and its integration into DSS development tools will stimulate and engender further DSS research into event triggered processing. On the theoretical side, such research can amplify the issues identified here and possibly identify other significant related issues. In an applied vein, future research may investigate demon implementation methods beyond those already existing in frame systems and formal languages for demon specification. In any event, the concepts introduced here provide a starting point for both implementors and researchers.

## References

[1] D.G. Bobrow and T. Winograd, An Overview of KRL, a Knowledge Representation Language, Cognitive Science 1, nr. 1 (1977).

[2] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Developments in Decision Support Systems, in: M. Yovits, ed., Advances in Computers (Academic Press, New York, 1984).

[3] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, 1981).

[4] Guru Reference Manual, vols, 1–2. MDBS Inc., Lafayette, IN (1985).

[5] C.W. Holsapple and A.B. Whinston, Knowledge Representation and Processing for Management and Economics. Conference on Integrated Modeling Systems, Austin, TX (1986).

[6] C.W. Holsapple and A.B. Whinston, Business Expert Systems, Irwin, Homewood, IL (1987).

[7] O.G. Selfridge, Pandemonium: A Paradigm for Learning, Proceedings of the Symposium on Mechanisation of Thought Processes, U.V. Blake and A.M. Uttley, eds., Her Majesty's Stationary Office, London (1958).

[8] M. Williamson, In Guru. the Business World Finally Has Its First, True AI-Based Micro Package, PC Week 3, nrs. 11–14 (1986).

[9] T. Winograd, Understanding Natural Language (Academic Press, New York, 1976).
