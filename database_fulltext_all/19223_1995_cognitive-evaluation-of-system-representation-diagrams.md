---
otero_id: 19223
otero_key: "EK3WNQ8S"
title: "Cognitive evaluation of system representation diagrams"
authors: "Gerald L. Lohse; Daihwan Min; Judith Reitman Olson"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00024-q"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cognitive evaluation of system representation diagrams

Gerald L. Lohse $^{a,*}$ , Daihwan Min $^{b}$ , Judith Reitman Olson $^{c}$

$^{a}$ Department of Operations and Information Management, The Wharton School of the University of Pennsylvania, Philadelphia, PA 19104-6366, USA

$^{b}$ Department of Management, Korea University at Jochiwon, Jochiwon, Korea

$^{c}$ Computer and Information Systems Department, The University of Michigan, Ann Arbor, MI, USA

## Abstract

We evaluate diagramming techniques for systems analysts and programmers from a cognitive perspective. This focuses on how people process information from system diagrams and how diagrams support the cognitive limitations of systems analysts and programmers. The paper increases awareness of the analyst's need for different information views during the systems development process and provides steps for improving the comprehension and communication of diagrammatic information. The examples provide ways to develop better diagrams given current tools for their development. We hope that future diagramming tools will reflect the cognitive limitations of the analyst by actively highlighting and dynamically governing the flow of graphic information across multiple information processing views.

Keywords: Graphs; Tables; Time charts; Network charts; Diagrams; System views

IDT: Systems analysis and design; System diagramming methods; Motivation

## 1. Motivation

System analysts accumulate copious amounts of information about the functional requirements of the system and keep track of a myriad of system features. Unfortunately, limitations in human information processing capabilities may preclude effective system analysis. Humans are sequential information processors. People have a limited precision for detail when processing information, selective attention primed by expectations, a limited working memory capacity, and consequently, they make many errors in retrieving information from memory.

Many system representation tools attempt to cope with the information load of systems analysis and design (SA&D) and the numerous problems arising from poor definition and communication of requirements and standards. System representation tools are an essential component in system development. Systems analysts use diagramming tools to represent the requirements of an information system (IS), explore design alternatives and isolate critical design features. More importantly, system diagrams serve as a vehicle of communication among users, programmers, top management, and systems analysts [30]. As noted in a quote from a systems development engineer: “The ER diagram means that everybody speaks the same language. Developers, designers, human performance people, we all use the same language.... we could resolve all problems in terms of the diagram. [9]”

Many practitioners and researchers have evaluated tools for SA&D. IFIP Working Group 8.1 reviewed 13 IS design methodologies applied to a standard case [25], analyzed features of each design methodology [24], and suggested improvements for SA&D methodologies [26]. Colter [6] compares the similarities and differences of traditional and structured tools for SA&D. Shoval and Pliskin compare structured approaches to prototyping [29]. Yadav et al. [32] also compare two structured design methods. Martin and McClure [23] describe structured systems development techniques and critique the merits of each technique. Cougar [7] and Baylin [1] describe individual diagramming techniques in terms of their evolution, major characteristics, and suitability for each stage of systems development. Larsen and Naumann compare abstract and concrete representations [19].

In previous research, experience and intuition often served as the primary evaluation criteria. Theories of human information processing from cognitive science provide more objective and specific evaluation criteria. An information processing perspective enables us to identify what information to represent and how to display it. Although human information processing limitations are often cited as a problem in systems development [10], prior research has not evaluated how well SA&D representation tools support the cognitive limitations of the analyst.

We examine the fit between the analysts' cognitive limitations and SA&D diagramming tools. Some representations convey certain types of information better than others. By doing a task analysis of the systems analyst's work, we characterize what type of information to represent during various stages in the development process and describe the information conveyed by the more popular systems representation tools. The primary focus of the paper is to explain how people perceive information from these diagrams and how to create better diagrams for conveying information.

## 2. What does the systems analyst do?

Recent studies have focused on high-level software design practices because the most expensive errors to correct in a software development project are made during the initial design. Guindon examines knowledge exploited by experts during software design $[13]$ as well as top-down decomposition design processes $[14]$ . However, he examined individual developers rather than development teams, thus there was little need for diagrams to communicate information among team members. Olson et al. $[27]$ examined collaborative system design meetings for small teams, but they focused on system goals, design alternative, and design criterion rather than on diagramming tools used to present those ideas. Thus, we focus specifically on the use of SA&D representation diagrams in the systems development process.

One role of the systems analyst is to describe the future IS. The primary products of SA&D are the representations of the current and the future IS. The representation of the current IS shows 'What the IS is doing'. It serves as the basis for eliciting desirable changes, new requirements, and verification. The representation of the future IS shows 'What the IS is going to do after the changes'. It serves as the basis for validating and implementing the changes and requirements. The process of constructing the representations is now discussed.

Definitions of seven components

<table><tr><td>Basic Component</td><td>Analogy</td><td>Definition (Examples)</td></tr><tr><td>agent</td><td>who</td><td>a human or group of people (Jack Smith, systems analyst, IS department, customer)</td></tr><tr><td>object</td><td>what</td><td>things that are tangible or intangible as distinguished from human (data, computer, material, letter, report, tool, machine)</td></tr><tr><td>operation</td><td>how</td><td>any process that changes some characteristics of an agent/object (compute, compare, negotiate, transport, lift, draw, think, reason)</td></tr><tr><td>Supplementary Component</td><td>Analogy</td><td>Definition (Examples)</td></tr><tr><td>time</td><td>when</td><td>point in time, duration, frequency, or sequence (on Monday, 3 days, three times a day, first)</td></tr><tr><td>location</td><td>where</td><td>spatial position (Ann Arbor, plant, CEO&#x27;s office)</td></tr><tr><td>purpose</td><td>why</td><td>reasons/rationale for existence of the system or a component (improve efficiency, make profits, keep records, show trends)</td></tr><tr><td>volume</td><td>how much</td><td>size/amount of objects/agents (10 copies, 100 pounds)</td></tr></table>

## 2.1. Identifying components and relationships

The identification of system components and the interrelationships among them are a useful way to define a system. Common components include agent, object, operation, time, location, purpose, and volume. These are analogous to who, what, how, when, where, why, and how much in a good journalism report [33]. Table 1 shows definitions and examples of the components. Three of the seven components –agent, object, and operation –are the basic components. The other four are supplementary in the sense that time, location, purpose, and volume only contribute to the more specific descriptions of the three basic components.

Early in the SA&D process, analysts focus on structural relationships between identical components (i.e., agent-agent, object-object, and operation-operation). During SA&D, analysts identify: (1) agents and relationships among agents, (2) operations that agents perform, and (3) objects involved in each operation. Examples include: supervisor-subordinate relation between agents, assembly-component relation between objects, and work breakdown structure between operations.

## 2.2. Generating local views

There are potentially as many local views as the number of people using the system. Because each person forms a local view from a part of the whole system, it is neither possible nor desirable to gather all the views. When analysts gather data, they need to focus on the more important components and relationships, filter out the irrelevant data, and organize the relevant data.

The literature suggests four central sets of local views: environmental, behavioral, process-oriented information processing, and data-oriented information processing [31]. Environmental representations show the context of the IS, the purpose of the IS, and the boundary between the system and its environment. The other three views are internal. Behavioral views focus on observable behaviors, while others focus on information handling. Table 2 summarizes the emphasis of the local views.

Table 2  
Emphasis of Local Views

<table><tr><td>Local views</td><td>Emphasis</td></tr><tr><td>Environmental</td><td>Purpose</td></tr><tr><td>Behavioral</td><td>Agent-Operation</td></tr><tr><td>Process-oriented Information processing</td><td>Operation-Object</td></tr><tr><td>Data-oriented Information processing</td><td>Object-Operation</td></tr></table>

Agent-operation relationships show 'who does what', with the focus on agents. Some include time, location, and object in the more specific description of the operation. The behavioral views are more familiar to non-IS professionals, since they usually do not pay attention to information processing requirements of their behavior. These views are the basis of job redesign when the users and analysts consider changes and new requirements. Ignoring the behavioral perspective is often the reason for rejection of IS [21].

In contrast, information processing views do not explicitly represent agents. Rather, they represent operation-object relationships. Process-oriented representations emphasize operations while data-oriented representations emphasize objects. The main questions are: what information is involved in each operation? how is the information processed? and where is the information stored in the system? Different local representations create links between the behavioral and information processing views to aid the generation of global models.

## 2.3. Building global models

View integration is the process of merging the diverse local views into a single coherent set. Neither collecting the local representations nor superimposing the local representations will generate a global model. The result of the integration process must be a global model of the real system. From the global model, the analysts create other local views not included originally. Also, the systems analyst must use the global model to communicate with interested parties not active in the construction of the global model. Finally, the systems analyst examines the global model for opportunities to redesign the system.

## 3. What methods exist now?

Over the past several decades, many people proposed and developed methods for SA&D. Earlier methods did not alleviate the poor communication between IS professionals and non-professionals during SA&D [8,12]. Around 1970, people proposed structured analysis and design techniques as a remedy and claimed that their methods would give better insights for IS development. Later, SA&D tools added methodological rigor and structure. Gradually, systems analysts considered the possibility of using computers for the development of computer-based IS itself. As a result, CASE (Computer-Aided Software Engineering) methods emerged.

The previous literature identifies more than 80 methods and their variations used during the IS development [e.g., 1, [3], 7]. We identify methods used for SA&D in Table 3. Representations of the IS serve as a vehicle for communication among interested people and an aid to clear thinking during SA&D. In general, good representations help people understand problems and find solutions. Likewise good representations can improve productivity and effectiveness.

Each method has its own symbols and conventions for drawing diagrams/charts. Unfortunately, most methods do not provide specific guidelines for the generation of diagrams. Heuristics, such as top-down decomposition, hierarchical structure, and “limit the number of components to six per diagram” are often the only guidelines that aid diagram construction. As a result, representations may not convey much information to the viewer. This is because it is difficult to perceive their intended meanings. The lack of guidelines did not change with the advent of CASE tools. If the analyst is a poor diagrammer, the CASE tools only accelerate the generation of poor diagrams. Analysts also spend a great deal of time drawing and often need a graphic artist to generate the diagrams $[4,23]$ .

Two diagrams containing the same information may look very different and convey different messages or seem harder or easier to understand. We use examples from two systems to illustrate this point. One depicts a behavioral view and the other shows a process-oriented information processing view.

Fig. 1 is an example of the Business Information Analysis and Integration Technique (BIAIT) developed by Carlson [2]. This is a behavioral local view representing agent-operation relationships with an emphasis on agents. It describes who does what in the organization. The primary goal is to show the operations that change some characteristic of agents. In particular, the BIAIT network shows how the organization handles information for product flow, planning, and control. For example, within the Finance Department, the financial reporting operation helps control both the cost estimating and the budgeting operations and also helps plan cost allocations.

Table 3  
SA and D representation methods

<table><tr><td>SA and D process</td><td>Graphic representation methods</td></tr><tr><td colspan="2">1. Identifying components and relationships</td></tr><tr><td>Structural relationships</td><td>Organization chart, Work breakdown structure, System flowchart, Decision tree</td></tr><tr><td colspan="2">2. Generating local views</td></tr><tr><td>Environmental views</td><td>Narrative text</td></tr><tr><td>Behavioral views</td><td>Gantt chart, Linear responsibility chart, BIAIT Activity chart,Work distribution chart, BSP matrices</td></tr><tr><td colspan="2">Information processing views</td></tr><tr><td>Process-oriented</td><td>Data Flow Diagram, Process flowchart, Decision table, SADT-Actigram, Program flowchart, HIPO, Warnier-Orr diagram,</td></tr><tr><td>Data-oriented</td><td>SADT-Datagram, Forms flowchart, Flow diagram, Data structure chart, Entity-Relationship diagram</td></tr><tr><td>3. Integrating into global views</td><td>Aggregation of views in step 2</td></tr></table>

Fig. 2 is an example of a Data Flow Diagram (DFD) developed by Gane and Sarson [11]. This is an information processing view with an emphasis on processes. It shows the logical operation-object relationships. To avoid crossed data flow lines the notation permits duplicate appearances of data stores and external entities on the same diagram. It uses rounded rectangles to denote processes. Arrows represent data flows among processes, data stores, and external entities. The example describes a system for marketing and supplying books to individuals and librarians through a mail order service. For example, the data flow description payments describes the relationship between the external entity CUS-TOMERS and process number 4, “apply payments to invoices”.

The BIAIT network and the data flow diagram contain information relevant to SA&D, but it is not easy to perceive these relationships directly from the diagram. Redesigning the display can improve the communication and understanding of the information represented. Using a model of visual information processing, we can revise these to improve comprehension and communication.

## 4. How do people acquire information from diagrams?

Knowing how the eye decodes information from a diagram helps us present information more clearly in a diagram. Models of perception and cognition provide insight about the underlying human information processing mechanisms used to understand a diagram. Fig. 3 presents a model of perception and cognition for diagram comprehension adopted from Pinker [28].

![](/api/attachments/EK3WNQ8S/fulltext/images/7c1a94a2d321577d30f1e90585f9cd5456d685489575c3f49babae0a043c6de7.jpg)  
Fig. 1. Original business information analysis and integration technique (BIAIT) diagram.

![](/api/attachments/EK3WNQ8S/fulltext/images/202b1b5691c51c9063acd8f465d1cf14304fc9725198e059b9043affea8ead66.jpg)  
Fig. 2. Original Gane and Sarson data flow diagram (published with permission of the copyright owners).

LTM  
![](/api/attachments/EK3WNQ8S/fulltext/images/8e388ea140b7523f1a7cff2a03e2a6ee48874c22fe531584cf6546fdd91b3a2c.jpg)  
PERCEPTION STM
Fig. 3. Model of visual information processing for system diagram comprehension.

## 4.1. Overview of visual information processing

The model has several parts. Early visual processes form a visual array from the visual stimulus by detecting primitives such as shape, angle, color, length, and slope. Then visual encoding processes organize and map these primitives to form regional patterns. Gradual rescanning builds a visual description of the diagram.

The visual description may trigger the recognition of a diagram schema (DFD, BIAIT, etc.) stored in long-term memory (LTM) [18]. Diagram schemas contain the knowledge about the conventions and symbolic notation used in the diagram. These direct the search for additional pieces of information from the diagram. Subsequent scanning, rescanning, and decomposing, directed through a diagram schema, aids the assembly of a message from the diagram.

Often additional interrogation and inferential processing is necessary to translate the perceived message from the diagram into the answer to a specific question needed by the analyst. Theoretically there are no limits to the amount of interrogation and inferential processing. In practice, short-term memory (STM) limitations render certain types of information easier or more difficult to extract from the diagram. As a result, two diagrams that contain identical information can have significantly different comprehensibility. The greater the extent of the interrogation and inferential processing, the more difficult it will be to extract the information from the diagram.

Furthermore, we tend to ignore any information that must be inferred or transformed from the display [17]. Empirical evidence suggests that people readily adopt the information processing strategy imposed by the information format of the task in order to avoid the effort of transforming the information to another format. Human judgment and decision behavior can be adversely affected by adopting information processing strategies that are contingent on the format of the display.

## 4.2. Visual primitives

Many visual primitives symbolically encode information in a visual display. We perceive some more readily than others. Visual primitives such as texture [15] and color [16] are detected and organized simultaneously in parallel; other visual primitives, such as shape and containment, are detected and organized less efficiently via serial scanning (Fig. 4).

The BIAIT diagram contains information relevant to SA&D, but it is not easy to perceive these relationships directly from the diagram. Most of the information is encoded with visual primitives that people detect serially. To perceive the salient information, we rescan the diagram. For example, agents (Customers, Personnel Department, etc.) and operations (training, budgeting, etc.) are coded using the same visual primitives: containment, area, and shape. In Fig. 5, redundant coding of agent using shape and a visual primitive our eyes detect in parallel, gray scale, reduces the complexity of the diagram. Each department in the organization “pops-out” as one perceptual unit that simplifies the mental organization of information in the diagram. The new coding scheme resolves unintended ambiguities between agent and operations. Information about operations contained in various departments is easier to identify.

## 4.3. Detection

Visual primitives must have a certain minimal size. If visual primitives are too small or too dim they cannot be seen during an initial glance. Large differences in physical variation of a feature are more noticeable than subtle differences. For example, we detect dark objects before light ones and large objects before small ones. The greater the contrast between a feature and the background, the more readily we observe the feature.

Data flow diagrams are an information processing view of the system with an emphasis on process. This is difficult to detect. Processes are coded using object shape. A more efficient coding scheme would use a visual primitive that the eyes detect in parallel, such as gray scale or texture. Since dark objects are detected before light objects, we use a black box behind each process to help processes “pop-out” from the rest of the symbols.

![](/api/attachments/EK3WNQ8S/fulltext/images/c925e0793d92ac003de4887b13db264ae01d12c2af4af4a504c9fc1e23aacd22.jpg)  
Fig. 4. Some visual features are perceived in parallel; others are perceived by less efficient serial scanning.

![](/api/attachments/EK3WNQ8S/fulltext/images/7cc6084eca646b467fd22c8e4fb42dafc5d8a6701c3340347a824eb58a4f3b20.jpg)  
Fig. 5. Revised business information analysis and integration technique (BLAIT) diagram.

![](/api/attachments/EK3WNQ8S/fulltext/images/fff11e080f5ba10a03734b809a6b3f037a177e6f5a8e2699d2993db82d00dfd5.jpg)  
Fig. 6. Revised Gane and Sarson data flow diagram.

Data flow diagrams have four major components: processes, data stores, external entities, and data flows. It is hard to see these four distinct components in the original DFD. The symbolic notation used to represent these four is too similar. Greater variation among the symbols would help in identifying the distinct components. In Fig. 6, we present a revised DFD that enhances the distinction among processes, data stores, and external entities. We use circles embedded in a border to separate external entities from processes, data stores and data flows. Shaded rectangular boxes represent processes; a pair of bold parallel lines represents data stores.

## 4.4. Discrimination

Once detected, the viewer must discriminate and separate the visual primitives. Variations in size, texture, color, shape, value, and orientation convey information. If the variations are too subtle, the information encoded in the visual primitives will not be conveyed. A symbol used for one particular category of information must be discriminable from others. It is more difficult to distinguish between a rectangle and a rectangle with rounded corners than a rectangle and a circle. If the variations in the symbols seem ambiguous, errors in interpretation can result. Confusion and errors in cognitive processing result from interference among similar visual marks.

The BIAIT diagram shows the flows of information from operations within one department to operations elsewhere in the organization. These connections are difficult to perceive from the diagram. Lines depicting information flows and lines representing the boundaries of the departments are too similar to separate. Greater variation in the visual primitives encoding connections facilitates discrimination. In particular, different textured lines aid the identification of product flow, planning, and control.

## 4.5. Perceptual groups

Some combinations of visual primitives are perceived more readily than others because they are viewed simultaneously as one perceptual unit. The number of perceptual units that can easily be considered at one time defines the capacity limit of STM. Gestalt psychologists discovered laws that describe how we see perceptual units of a diagram rather than seeing each dot, line or mark. In Fig. 7a, we see three perceptual units, the three columns of visual features, rather than 36 individual circles and 36 individual lines. Proximity, similarity, continuation, common fate, closure, and separation of figure from ground are some of the more important laws determining the perceptual groupings in a diagram. These laws dictate how visual primitives form patterns.

The law of proximity states that visual primitives spatially closer to one another form perceptual groups. Thus, proximity links the symbols to form columns rather than rows. The law of closure says that the parts of a figure not present are filled in to complete the figure. The law of similarity dictates that similar visual primitives are more closely associated together to form perceptual groups. In Fig. 7b, the law of closure allows us to form O's from the C's and similarity links the filled shapes to form an "M". In Fig. 7c, similarity links the boxes to one another. The law of continuation allows us to view the squiggle as one element rather than a series of short line segments and curves.

## 4.6. Short-term memory

Working memory is the temporary storage area for synchronizing rapid perceptual processes with somewhat slower cognitive processes. The contents of working memory are lost by interference from similar items. The capacity limit of working memory is roughly four perceptual units. Diagrams exceeding working memory capacity are difficult to interpret. This constraint is particularly evident when a diagram contains too much information or when the legend forces the viewer to engage in an arduous memorization task. Diagrams with an efficient mapping of the perceptual groups to their intended meaning will be easier to understand.

In the original BIAIT diagram, departments are not readily viewed as perceptual units. Serial scanning is needed to separate information flow lines from lines depicting departmental boundaries. Lines defining departments and operations add to the ambiguity. We expend mental effort to resolve these ambiguities. The additional effort burdens STM with the extra step of finding the department before information flows among departments can be examined. Fig. 5 solves this problem using a more efficient coding scheme that reduces the STM information processing load.

## 4.7. Long-term memory inferencing

Familiarity with diagramming conventions can focus attention to particular areas of the diagram quickly. If a diagram does not match expectations, then it must be scanned slowly in a serial fashion for clues about how to process the information. Sometimes inconsistencies in a coding scheme invite the viewer to attribute meaning to variations in the diagramming conventions when no meaning was intended.

One common example is in the variation in label sizes. Often one department's label will be twice as long as another's. The visual impression to the viewer is that some departments are more important than others. Such inferences may distort the intended meaning. Inconsistencies in a coding scheme can also cause interference among similar items. For example, a color coding scheme that assigned grapes yellow, bananas red, and apples violet would be more difficult to understand than a scheme that matched the fruits to their real world colors. Even though inferential processing helps direct and re-focus attention to particular features in the diagram, it slows the speed at which information can be processed from the display. Diagrams which require rescanning and inferential processing are a puzzle to be “solved” by the reader, rather than information that is “viewed” by the reader.

The coding scheme used in the DFD to represent processes is inconsistent. Some symbols are larger than others. The size of the rounded rectangle depends on the length of the label associated with the symbol. This variation may make the viewer to associate size with importance to the process. Because similarity is important in forming perceptual units, each process symbol should be the same size. In Fig. 6, we use a consistent size for each symbol to avoid such inconsistencies in the symbolic notation.

![](/api/attachments/EK3WNQ8S/fulltext/images/53ec9b6246262dbf8d15a35cf1e3330b128e6131d760c6f896fc70d7b58e91e6.jpg)  
Fig. 7. Gestalt grouping laws.

## 4.8. Long-term memory storage

LTM is a permanent memory storage. Associations to information previously stored in LTM aids interpretation. Usually recognition is sufficient to trigger associations. Each part of a diagram should readily permit associations with previously stored information because recognition directs the process of decoding information. Prior knowledge of the conventions and symbolic notation in a particular type of diagram simplifies diagram comprehension. For example, highway signs convey a known meaning.

Humans process some information from a diagram using learned spatial patterns. Reading usually begins in the upper left-hand corner and proceeds from left to right in a top-to-bottom fashion. Of course, there may be cross cultural differences (e.g., most Arabic and Hebrew reading patterns are not right to left). Authority structures are another learned spatial pattern. The top of an organizational chart generally signifies the most powerful part of an organization; a lateral shift at a particular level defines equal authority. When a diagram is difficult to interpret, it is often because of violations of these learned spatial patterns.

Most SA&D diagrams have no spatial patterns to ease recognition. Most are complex networks of interrelated components. Generally, these must be navigated serially from one component to the next. This takes on meaning when we discover an arrangement that defines the relationships among the components and minimizes the number of meaningless intersections. The BIAIT diagram is an example of an information network. The flow of information from the customer, supplier, and environment is difficult to follow through department operations. A separate display for each type of information (product flow, planning, and control) would enhance the presentation of information flow.

Table 4  
Rank order of visual primitives for different types of information (adopted from Cleveland 1985 and MacKinlay 1986)

<table><tr><td>Quantitative</td><td>Ordinal</td><td>Nominal</td></tr><tr><td>position</td><td>position</td><td>position</td></tr><tr><td>length</td><td>value</td><td>color hue</td></tr><tr><td>angle</td><td>texture</td><td>value</td></tr><tr><td>slope</td><td>length</td><td>texture</td></tr><tr><td>area</td><td>angle</td><td>shape</td></tr><tr><td>volume</td><td>slope</td><td>connection</td></tr><tr><td>value</td><td>area</td><td>containment</td></tr><tr><td>color hue</td><td>volume</td><td>length</td></tr><tr><td>texture</td><td>color hue</td><td>angle</td></tr><tr><td>connection</td><td>connection</td><td>slope</td></tr><tr><td>containment</td><td>containment</td><td>area</td></tr><tr><td>shape</td><td>shape</td><td>volume</td></tr></table>

## 4.9. Viewer-to-viewer variation

Variations are contingent upon the user, diagramming expertise, and the task. System representation diagrams convey information to users, analysts, and programmers. Novices may lack the necessary schema to understand the symbolic notation. Programmers may lack a sufficient understanding of the business environment to convert the symbolic notation into an appropriate representation of the system. Practice and training can improve the strengths of the schemas associations and the ability to decode information.

## 4.10. Visual information processing summary

Using the grouping laws from Gestalt psychology, an understanding of human information processing and experimental data from the perception literature [5], we rank processing priorities for various visual marks in a diagram. Table 4 shows the processing priorities for encoding quantitative, ordinal, and nominal information from various types of visual marks.

From this, one can see that color is more effective for coding nominal data than for coding ordinal or quantitative data. We could therefore use color to depict different information flows, since it is more effective than texture for coding nominal information. However, color is not psychologically ordered along a continuum. Shifting color from orange to red does not convey “more of something” as effectively as changing the size from small to large. Shape is more efficient for coding nominal data than for coding ordinal or quantitative data. Redundant coding schemes that combine multiple shapes and colors are likely to be more effective for coding information than either would be alone.

## 5. Designing effective system representations

The model of visual information processing describing how people perceive information provides a basis for redesigning information displayed in a diagram to improve the comprehension and communication of the information represented. The following steps outline the design process:

1. Identify the requisite information components (agent, operation, object, time, location, purpose, and volume).

2. Choose the current local view that expresses the chosen information components (environment, behavioral, information processing).

3. Select a system diagramming tool that represents the chosen information components in a local view (DFD, BIAIT, SADT, decision tree,...) $^{1}$

4. Identify the category of information for each component in the display (agent is nominal, volume is quantitative).

5. Identify the most effective visual primitive (color, texture, shape, value,...) for each information component.

6. Identify the desired relationships among information components and organize the requisite information symbolically encoded in the visual primitive into a unified presentation.

7. Evaluate the display for unintended ambiguities.

Seemingly minor changes in how we code the information in a diagram can significantly change the ability of the viewer to perceive the intended message. Systems development diagrams should improve the human information processing capabilities of the analysts. Better coding of the information requirements will enhance the efficiency and the effectiveness of the analysts in their decoding of the information from the diagrams.

## 6. Summary

Large systems integration projects depend on extensive communication among various parties. Ideally, all members of the system development team must understand the system before the organization allocates a substantial amount of resources to further systems development. Early identification of design flaws or missing components are much less costly to correct than those found latter in the development process. A visual representation of the system helps communication and identification of potential problems. SA&D requires the analyst to assimilate copious amount of information. Detailed documentation of specifications become so voluminous that few people read them. For example, on one factory automation project, no member of the design team had read the 1,000 plus pages in the requirements documentation.

Diagrammatic displays are powerful tools for visualizing vast quantities of information. System diagramming tools aid the process by providing a picture of the interrelated components of the system. However, system representations present non-spatial information that is difficult to understand $[20]$ . Knowledge from system representations is lost rapidly over time and SA&D representations are too abstract. Our goal is to identify information components that the analyst needs to have represented and determine the best way to display this information. If the visual primitives in the diagram explicitly specify the information components required by the designer, the intended message is immediately evident. The value of any SA&D development technique depends on the appropriateness of the representation tool for the development task and on representation standards.

Good representations serve as intelligent information filters that selectively focus attention to salient components. Representations can expedite the discussion of system issues. Rather than provide static documentation, diagrammatic techniques provide a common language and mechanism for reasoned disagreement and evaluation. CASE tools have made the process of creating system representation diagrams more efficient. Nonetheless, if the analyst is a poor diagrammer, the CASE tools only accelerate the generation of poor diagrams. Further, SA&D representations only show one static, environmental, behavioral, or information processing view at a time. Often it is helpful to switch among different views as the emphasis changes among agent, operation, object, and purpose.

Intelligent diagramming support tools not only aid the graphic design component of the diagramming process but also support the dynamic flow of different views from multiple representations. Mackinlay [22] describes a technique for the automatic design of graphical presentations from a small set of visual primitives and a classification scheme for the information components. Existing CASE tools could be modified to support automatic presentation of information from SA&D representations. Functions could be added to highlight relations among various elements on a display, show particular data element linkages, or isolate specific information flows. Such additions to CASE tools could effectively circumvent some of the problems with static views in current SA&D representation diagrams.

## References

[1] Baylin, E.N. System Diagramming Methods: Which Works Best?, Journal of Information Systems Management, (4)3, (Summer 1987), 29.

[2] Carlson, W.M. Business Information Analysis and Integration Technique (BIAIT) - The New Horizon, Data Base, (10)4, (Spring 1979), 3.

[3] Chapin, N. Graphic Tools in the Design of Information Systems, in Systems Analysis and Design: A Foundation for the 1980's, 1980, pp. 121–162.

[4] Chikofsky, E.J., Rubenstein, B.L. CASE: Reliability Engineering for Information Systems, IEEE Software, (March 1988), 11.

[5] Cleveland, W.S. (1985). The Elements of Graphing Data. Monterey, CA: Wadsworth Publishing.

[6] Colter, M.A. A Comparative Examination of Systems Analysis Technique, MIS Quarterly, 8(1), (1984), 51.

[7] Couger, Daniel J., Colter, M.A., & Knapp, Robert W. Advanced System Development/Feasibility Techniques, John Wiley & Sons, New York, N.Y., 1982.

[8] Cronan, T.P. Application Systems Development: A Communication Model for Business Users and DP Personnel, Data Base, 15(4), (1984), 21.

[9] Curtis, B., Krasner, H., & Iscoe, N. (1988). A field study of the software design process for large systems. Communications of the ACM, 31(11), 1268–1287.

[10] Davis, G.B. Strategies for Information Requirements Determination, IBM Systems Journal, 21(1), (1982), 4.

[11] Gane, C. & Sarson, T. Structured Systems Analysis, New York, Prentice-Hall, 1979.

[12] Guinan, Development of Computer-Based Information Systems: A Communication Framework, Data Base, (Spring 1986), 3.

[13] Guindon, R. (1990). Knowledge exploited by experts during software system design. International Journal of Man-Machine Studies, 33, 279–304.

[14] Guindon, R. (1990). Designing the design process: exploiting opportunistic thoughts. Human-Computer Interaction, 5, 305-344.

[15] Julesz, B. (1981). Textons, the elements of texture perception and their interactions. Nature, 290, 91–97.

[16] Kahneman, D., & Henik, A. (1981). Perceptual Organization and Attention. In Kubovy M, & Pomerantz J R, Perceptual Organization. (pp. 181–211). Hillsdale, NJ: Lawrence Erlbaum Associates.

[17] Kleinmuntz, D.N., & Schkade, D.A. (1993). Information Displays and Decision Processes. Psychological Science, 4(4), 221-227.

[18] Kosslyn, S.M. (1985). Graphics and human information processing. Journal of the American Statistical Association, 80, 499–512.

[19] Larsen, T.J. & Naumann, J.D. (1992). An experimental comparison of abstract and concrete representations in systems analysis. Information and Management, 22, 29–40.

[20] Lohse, G.L., Biolsi, K., Walker, N., and Rueter, H. (1994). A classification of visual representations, Communications of the ACM, 37(12), 36–49.

[21] Lucas, H.C. Jr. Implementation: The Key to Successful Information Systems, Columbia University Press, New York, 1981.

[22] Mackinlay, J.D. (1987). Automating the design of graphical presentations of relational information. ACM Transactions on Graphics, 5(2), 110–141.

[23] Martin, J. & McClure, C. Diagramming Techniques for Analysts and Programmers, Englewood Cliffs, NJ: Prentice-Hall, 1988.

[24] Olle, T.W.; Sol, H.G.; & Tully, C. Eds. Information Systems Design Methodologies: A Feature Analysis, North-Holland, Amsterdam, (1983).

[25] Olle, T.W.; Sol, H.G.; & Verrijn-Stuart, A.A., Eds. Information Systems Design Methodologies: A Comparative Review, North-Holland, Amsterdam, (1982).

[26] Olle, T.W.; Sol, H.G.; & Verrijn-Stuart, A.A. Eds. Information Systems Design Methodologies: Improving the Practice, North-Holland, Amsterdam, (1986).

[27] Olson, G.M., Olson, J.S., Carter, M.R. & Storrosten, M. (1992). Small group design meetings: an analysis of collaboration. Human-Computer Interaction, 7, 347–374.

[28] Pinker, S. (1990). A theory of graph comprehension. In R. Freedle, (ed.) Artificial Intelligence and the Future of Testing. Hillsdale, NJ: Lawrence Erlbaum Associates.

[29] Shoval, P. & Pliskin, N. (1988). Structured Prototyping: Integrating prototyping into structured systems development. Information and Management, 14, 19–30.

[30] Walz, D.B., Elam, J.J., & Curtis, B. (1993). Inside a software design team: knowledge acquisition, sharing, and integration. Communications of the ACM, 36(10), 63–77.

[31] Wood-Harper, Information Systems Definition: the multiview approach, The Alden Press, Oxford, 1985.

[32] Yadav, S.B., Bravocco, R.R., Chatfield, A.T., & Rajkumar, T.M. A Comparison of Analysis Techniques for Information Requirement Determination, Communications of the ACM, 31(9), (Sep. 1988), 1090.

[33] Zachman, J.A. A Framework for Information System Architecture, IBM Systems Journal, 26(3), (1987), 276.

![](/api/attachments/EK3WNQ8S/fulltext/images/d940594b2e9419dacdb067783d4b25129abc19e9fba0b0a5380ffc769699896a.jpg)

Gerald L. Lohse is the Nelson Peltz Term Assistant Professor of Operations and Information Management at the Wharton School of the University of Pennsylvania. His interests include computational cognitive science, graphic knowledge representation, visualization, and decision support systems. He has published articles in Communications of the ACM, Human-Computer Interaction, Behavior and Information Technology, Journal of Economic Psychology

and other books and journals. Author's present address: The Wharton School of the University of Pennsylvania; 1326 Steinberg Hall –Dietrich Hall; Philadelphia, Pennsylvania 19104-6366; email: lohse@wharton.upenn.edu

![](/api/attachments/EK3WNQ8S/fulltext/images/21e712ff26faa481ee59dda1e6a2aa7554bf54b793e034a0976f38aa6fc7d549.jpg)

Daihwan Min is an Assistant Professor of MIS at Korea University at Jochiwon. His research interests focus on evaluating systems analysis and design methodologies. Author's present address: Department of MIS; Korea University at Jochiwon; 208 Seochang-Dong Jochiwon-Eup, Yonki-Gun, Chungnam; South Korea 339-800; email: mismdh@kusccgx.korea.ac.kr

![](/api/attachments/EK3WNQ8S/fulltext/images/eaf4472fbdede46c1ed8b7d7964ac1c4b05f4ba0c726c829dc22b4a7403a0154.jpg)

Judith S. Olson is Professor of Computer and Information Systems in the Business School and Professor of Psychology at the University of Michigan. Her research interests include collaborative technology for group work, systems development and human-computer interaction. She has served on many national committees and has published numerous articles in Human-Computer Interaction, Cognitive Psychology, IEEE Software, Behavior and Information

Technology, ACM Transactions on Information Systems and other books and journals. Author's present address: Department of Computer and Information Systems; 701 Tappan Street; The University of Michigan; Ann Arbor, Michigan 48109-1234; email: jolson@crew.umich.edu
