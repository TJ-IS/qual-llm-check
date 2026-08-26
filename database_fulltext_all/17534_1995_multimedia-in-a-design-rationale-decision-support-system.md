---
otero_id: 17534
otero_key: "SUT8T7BB"
title: "Multimedia in a design rationale decision support system"
authors: "Balasubramaniam Ramesh; Kishore Sengupta"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00060-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multimedia in a design rationale decision support system

Balasubramaniam Ramesh $^{a,*}$ , Kishore Sengupta $^{b}$

$^{a}$ Code AS / RA, Naval Postgraduate School, Monterey, CA 93943, USA

$^{b}$ Code AS / SE, Naval Postgraduate School, Monterey, CA 93943, USA

## Abstract

The capture and use of design rationale information is widely recognized to be essential for the design and maintenance of large systems. Design rationale information needs to be captured from a variety of sources and contexts. A design rationale management system should be capable of representing and reasoning with both formal and informal information. REMAP/MM is a hypermedia decision support system that facilitates the capture of different types of design rationale knowledge using multiple media. The design rationale knowledge is represented using a conceptual model that includes the Issue Based Information Systems (IBIS) designed to model deliberations, a primary source of design rationale. The system incorporates models of multimedia components of design rationale, thereby facilitating reasoning with this knowledge. Decision support for the various stakeholders in systems development is provided in the areas of management of system evolution, system maintenance with changing requirements, design replay, and fulfilling ad hoc information requirements.

Keywords: Design rationale; Multimedia; Decision support; Concept map; Argumentation

## 1. Introduction

The process of design involves a series of interdependent decisions resulting in the creation of a design solution represented by artifacts. Artifacts include any tangible output, such as design documentation, graphical drawings, prototype products, code, etc. Current approaches for documenting the design process stress the representation of the artifacts themselves, rather than the process of creating them. Recent research recognizes that capturing and representing information about the process of system design will significantly increase productivity in systems development and maintenance activities [5]. An important component of such process knowledge is information about the reasons behind the creation of artifacts, i.e., design rationale. Much of this knowledge involving deliberation on alternative requirements and design decisions is typically lost in the course of designing and maintaining systems.

Throughout this paper the term design refers to any activity that creates artifacts. Even during the early phases of the systems development life cycle intermediate artifacts are created and therefore, these are also considered design activities.

## 1.1. Why design rationale?

Capturing and maintaining design rationale knowledge is very important in large scale information systems development for the following reasons:

\- In large projects involving multi-person teams, maintaining multiple channels of communication for information exchange is difficult. Project teams often rely on one or more team members for maintaining communication of process knowledge and to facilitate coordination [5]. Risks inherent in reliance on such informal arrangements can be greatly reduced by explicit representation of design rationale.

\- In large projects, development teams change across phases and over time. In the absence of comprehensive design rationale, the context in which key design decisions were made may be lost [5].

\- Critical errors made in key design decisions are often unnoticed [32], [14]. With the availability of a corporate history of design rationale, project teams can greatly benefit from reviews of past decisions. Such reviews (in the same project or other projects) can help project teams identify and avoid errors that may have been committed.

\- Work groups often repeatedly discuss the same issues that had been resolved earlier, as there may exist no reliable record of these discussions [38]. These groups can avoid such unnecessary repetition of well understood design tasks and their resolution if design rationale are available.

\- In large projects, different project teams are commonly involved in different aspects of problem solving. In the absence of knowledge about design rationale, key design decisions are often misunderstood and misinterpreted [36].

A variety of stakeholders (such as end users, analysts, designers, project managers, maintenance personnel) involved in large software projects often have different sets of objectives and priorities. Decision support can be provided to each of the stakeholders by recording the history of a design in the form of design rationale. As the capture and maintenance of design rationale is an expensive activity, a decision support system (DSS) to support this process not only should facilitate easy and non-intrusive capture, but also provide automated reasoning with this knowledge. As the needs of various stakeholders vary widely, such a system needs to provide different types of services. The rationale information may be used by designers to represent and manage dependencies among various components and decisions. The maintenance personnel could access the history of evolution of a design solution to assess the impacts or side effects of proposed changes. Reuse of design components as well as process knowledge could be facilitated by the corporate memory on alternative solutions considered and the assumptions behind design decisions.

## 1.2. Our approach

Given the variety of information and support needs of various stakeholders, a successful design DSS should support capture, representation and reasoning with both informal and formal design rationale knowledge. In order to facilitate easy, complete and non-intrusive capture of knowledge, a design rationale DSS should use a variety of media that are best suited for capturing different aspects of design rationale, ranging from textual representations through multimedia capabilities.

Finally, it should be recognized that the primary purpose of capturing design rationale is for providing active assistance to various stakeholders. Capabilities for automated reasoning (beyond easy storage and retrieval) with relevant aspects of the design rationale knowledge would greatly enhance the viability of such a system.

The nature of formal and informal components of design rationale knowledge is discussed in the next section. A conceptual model used to represent various components of design rationale knowledge is presented in Section 3. In Section 4, we discuss the use of multiple media in capturing different types information in our DSS. The following section describes the capabilities of our DSS that provides various facilities for automated reasoning with design rationale knowledge to support system development activities. A detailed discussion on related research is provided in Section 6, followed by directions for future research.

## 2. Representing design rationale

## 2.1. Formal and informal representation of Design Rationale

Design Rationale can be represented in a variety of ways, from mathematically formal representations (e.g., transformations that can be used to derive one problem state from another) to very informal representations (e.g., design notebooks that record rationale in natural language) [21]. A primary benefit of formal representation is that it facilitates automated reasoning. The use of formal representation is feasible in domains that have formal domain models. Further, the semantics of the design tasks should be well defined. In the design of large scale systems where the size and complexity of design rationale knowledge can grow exponentially, automated inferencing can be extremely valuable.

However, attempts at formal representation of design rationale are constrained by several limitations. In design situations without well defined domain models, the acquisition of design rationale knowledge often occurs through informal means, e.g., videotapes of meetings. This process knowledge may then be “converted” to a formal representation. This conversion process is subject to two sets of problems. The process is extremely labor-intensive, and, therefore, may be infeasible to implement in many design situations. Second, the act of representation entails making judgments about the level of granularity at which the information should be represented. Overly large grained representations may result in the loss of useful detail, while overly fine-grained representations may create trivial knowledge wherein the benefits obtained from the finer grain do not warrant the cost of creating such knowledge. Existing literature does not offer demonstrably effective decision rules for making judgments about granularity.

More fundamentally, significant amounts of design rationale knowledge do not lend themselves to formal representation. Since design is primarily a collaborative process $[9]$ , informal design rationale knowledge often consists of deliberations among individuals engaged in the process. When individuals interact, they communicate through multiple channels. While some channels are explicit (e.g., talk), others are used in implicit ways. For example, the social significance and information content of gestures such as nods and looks have long been recognized to be an integral part of human communication $[15]$ . Communication is also effected through passive forms, such as awareness $[6]$ . Furthermore, design deliberation sessions often serve as a forum for the resolution of social and motivational issues such as conflicts among stakeholders. Such issues are often handled by groups through tacit or unconscious mechanisms that resist explicit representation $[9]$ . As Anderson et al. $[1]$ point out, attempts to represent informal knowledge through formal tools and notations can result in thin descriptions $[28]$ , with the consequence that much of the meaning embedded in such information is then lost.

Informal representations of design rationale can alleviate many of these problems. Since much design rationale knowledge is captured through informal means, mechanisms for informal representations make the task of creating design rationale much easier. Second, informal representations enable the retention of information in its most complete form, thereby facilitating the creation of thick descriptions $[11]$ . Recording human interaction in such forms allows access to the richness and complexity of social action, thereby allowing particular events to be scrutinized repeatedly and subjected to detailed inspection $[15]$ . Thick descriptions enable the user of design rationales to grasp the subtleties, tacit and mutual knowledge, and glean descriptions of work practices that are otherwise not made explicit $[16]$ . Finally, unlike formal representations, which can only be used by individuals who are familiar with the rigors of such formalisms, informal representations can be used by a wide set of users.

However, the classification, indexing, retrieval and use of informal representations can be problematic. Given the volume of knowledge generated in large projects, the lack of appropriate access and navigation mechanisms can constitute a significant impediment to the use of design rationale. Moreover, though understandable by humans, such information representations are not amenable to computation, i.e., unlike formal representations, automated inference and support can not be provided for informal representations. Thus, while informal representations hold much promise with respect to their information content and ease of capture, the difficulty of accessing and reasoning with such information can undermine their utility. In summary, then, formal and informal representations of design rationale complement each other in their respective strengths and weaknesses. Informal representations are easy to capture, whereas formal representations can be manipulated by well-defined inference procedures. Thus, effective schemes for the capture and use of design rationale should seek to combine the advantages of both forms of representations [29].

## 2.2. Media implications of informal representation of rationale

What does the combining of representations imply with regard to the use of media? Researchers in ethnography have long contended that informal knowledge should be represented in richer formats, such as through a combination of multiple media [12], [23], [26]. This view has been echoed in recent design rationale literature (e.g., [3], [18], [31]).

The use of multimedia in capturing informal knowledge provides three benefits $[12]$ . First, new media (e.g., graphics, animation, and sound) are more effective than text in conveying certain kinds of information such as two-and three-dimensional spatial relationships as well as processes, behaviors, and evolution of systems $[9]$ . Multimedia is particularly useful in capturing physical gestures, body language and other forms of implicit communication among members in design groups [15]. Besides, the capture mechanisms (e.g. passive video taping) are relatively non-intrusive, thereby allowing the design process to proceed uninterrupted while design rationale is recorded.

Second, the capture of knowledge though such media facilitates the creation of layered and contextualized narratives $[12]$ . Once captured, these narratives can then be used by different individuals for different purposes. For example, a user interested in the history of evolution of a particular artifact would use the videotape of a design session quite differently from a user interested in learning about the various points of view of the stakeholders.

Finally, the availability of such information in an unprocessed descriptive form provides a powerful context for ascertaining the semantics of communication $[7]$ , and thus, the interpretation of meaning $[11]$ . As Smircich $[30]$ argues, meanings do not exist in artifacts, symbols and practices, but rather are assigned by people who perceive and interpret their content and context. Also, design decisions are often characterized by assumptions that are not stated explicitly, but must be inferred from the context of the discussion. The analysis of representations, then, is an interpretive exercise in search of meaning $[11]$ . A richer context for understanding the collaboration mechanisms, process and culture in design groups can enable the user to interpret the rationale behind the creation of artifacts $[13]$ .

Thus, the provision of multimedia is critical to any effective scheme for representing informal knowledge. However, the usefulness of such information is greatly enhanced when they are linked to formal information that is relevant to the context.

## 2.3. Requirements of DSS for design rationale management

Comprehensive representation of knowledge about design rationale requires that some components of this knowledge are formally specified and these should be linked to informal knowledge components that are unsuitable for formal representation. Management of such process knowledge requires facilities for constructing, querying and maintaining structured knowledge bases.

A design rationale DSS should also provide automatic inferencing to enable access to the knowledge and maintain the integrity of the knowledge base made up of interdependent components that get incrementally defined and modified. Such inferencing will be aided by mechanisms for aggregation, classification and generalization of knowledge components.

As the overhead involved in populating the design rationale knowledge base is a serious concern, the ability to make deductive inferences from the assertions in the knowledge base can be valuable. This feature can be used for modifying and inferring values of objects in the knowledge base based on the semantics of the relationships among them. Further, mechanisms to maintain and manage dependencies among various components of design rationale and artifacts would be very valuable. Deductive database capabilities for query processing, deductive rules and integrity enforcement will help maintain such a dependency network.

As easy access and user friendly presentation are important, a hypermedia interface for browsing the contents of the knowledge base will be useful. Such an interface could be used to interact with and incrementally modify an evolving knowledge base of design rationale.

Even when some of the components of a design rationale knowledge base contain informal information, a formal model of the salient characteristics of such components can be maintained. Besides facilitating easy access to these components, such a representation would also enable automated reasoning about those characteristics. Further, a concept map [17] that visually depicts the relationships among knowledge components would facilitate navigation through related fragments of knowledge. A tight integration of formal and informal aspects of the design rationale information will not only facilitate the capture of various types of information in a format that is most appropriate, but also help use/reuse the captured information in an efficient manner.

![](/api/attachments/SUT8T7BB/fulltext/images/6886fdf2a2f88c22f36ca999272abd2c25fb281148e611d0e40f11dd558cd9b5.jpg)  
Fig. 1. REMAP conceptual model.

As a software development project grows, the associated design rationale knowledge base can become quite large. As the information needs of various participants can vary widely, navigating the entire knowledge base to retrieve relevant information can be very difficult even with hypermedia like browsing capabilities. An ad-hoc querying capability can alleviate the problem of accessing relevant information.

## 3. REMAP: A model for capturing design rationale

We employ the REMAP (REpresentation and MAintenance of Process knowledge) model and tool to implement our ideas on the capture and use of design rationale $[25]$ . A major goal of REMAP is to provide a conceptual model and mechanisms for representing and reasoning with design rationale knowledge. REMAP model relates design rationale to the artifacts created during the systems development process. This model was developed using an empirical study of the requirements engineering process.

Fig. 1 shows the primitives of our conceptual model which is described in detail in [25]. In this model, requirements represent the goals to be satisfied by the design process. The design process involves the refinement, elaboration and modification of the initial requirements. The design deliberation process involves discussion and resolution of issues or concerns that must be addressed to satisfy user requirements. This argumentation is modeled by extending the Issue Based Information Systems [4] (IBIS) model. The primitives in the IBIS model are issues, positions and arguments, and relationships among them. These are shown in the dotted segment in Fig. 1. Issues are like questions or concerns, positions are alternatives that address an issue, and arguments either support or object to positions. In addition to IBIS primitives, the assumptions that underlay arguments are also explicitly represented. Decisions resolve issues by selecting one or more positions. In the context of systems design, decisions lead to constraints which define the characteristics of design artifacts or solutions. The iterative nature of the design process is represented by the feedback loop between requirements and decisions.

In the model, requirements and design objects represent the inputs and outputs, respectively, in the requirements engineering phase of the life cycle. These can be substituted with appropriate inputs and outputs to tailor the model for different phases of the life cycle.

## 3.1. Implementation

We have implemented a multimedia extension of REMAP. REMAP/MM is a prototype DSS environment supporting design and maintenance tasks. This DSS is built using ConceptBase, an implementation of the high level conceptual modeling language Telos [24]. The client-server architecture of the implementation facilitates distributed group work among design team members. This environment provides deductive object management system capabilities with mechanisms for defining deductive rules and integrity constraints. The user interface is based on the X11 windowing environment, using the Andrew toolkit that provides several tools for creating hypermedia documents. The DSS operates on a SUN-4 workstation.

## 4. Capturing design rationale with REMAP/MM

In this section, we describe the functionalities provided by REMAP/MM for the capture and reuse of design rationale knowledge. The functionalities are illustrated by describing various scenarios on the use of the system by different stakeholders in systems development activities.

First, we describe a design scenario drawn from a case study based on a detailed domain analysis of a large scale system in the utilities industry [25]. We employ this scenario to illustrate the use of REMAP/MM in capturing and using design rationale.

## 4.1. An example scenario

A design team is engaged in developing a system for a utility company that processes customer requests for various services. The system is intended to be used in a centralized telephone answering service center, connected by an online computer to a large number of field stations. The utility company services various types of clients (e.g., industrial and residential) and provides various types of services (e.g., gas/electric connections, appliance rental/repairs). It serves a very large geographical area spread across several counties. Various types of requests for service dealing with gas/electric outages, appliance repairs, changes in service locations, etc., are to be handled by the system. The primary requirements of the system are to provide quick processing of requests and accurate information to customers about the status of their requests for service.

## 4.2. Capturing design rationale

REMAP/MM supports the capture of design rationale knowledge by providing a graphical interface for design teams to conduct their deliberations. As the design deliberation proceeds, instances of the primitives of the model such as issues, positions, arguments, assumptions, decisions etc. are defined and modified by the users.

![](/api/attachments/SUT8T7BB/fulltext/images/dc5abcd158aa7b76f96ce4022c3f83d888ee2ec66fd67ec231d939a5affeda44.jpg)  
Fig. 2. Instance of design deliberation.

Fig. 2 illustrates the outcome of a design deliberation session. In this example, the design team engaged in discussing the requirement to process service orders for gas/electric services and appliances (process\_order) identifies two issues that need to be addressed. One issue concerns the procedure that needs to be used in prioritizing the orders before processing (priority\_scheme). The other is about the frequency with which orders will be processed (frequency).

In Fig. 2, instances of different primitives in the REMAP model are displayed as icons with different shapes and colors, and relationships are displayed as links. Table 1 provides the shapes and shades of different types REMAP objects in Fig. 2.

Context sensitive menus defined for different types of objects specify the various actions that can be taken by the user for conducting conversations. For example, the menu associated with an ISSUE node would provide options for defining positions to resolve the issue, retrieve and browse positions already defined by other users, retrieve and browse the requirement(s) it is generated from, define decision(s) that resolve it and so on. By choosing appropriate menu items, the designer may conduct a conversation by adding relevant REMAP objects such as issues, positions etc. or browse through the results of previous conversations.

In Fig. 2, three alternatives (i.e., positions) for resolving the issue on prioritizing orders are put forward by the design team. Prioritization of the service orders by the location (location), or the types of customers to be serviced (customer\_type) or the type of service to be performed (service\_type) have been suggested by various participants. Associated with each position are arguments supporting the position or objecting to it. Each argument in turn is supported by assumptions.

Table 1  
Shapes and colors of REMAP/MM objects

<table><tr><td>Primitive type</td><td>Shape</td><td>Color</td></tr><tr><td>Requirement</td><td>Circle</td><td>Light grey</td></tr><tr><td>Issue</td><td>Oval</td><td>Light grey</td></tr><tr><td>Position</td><td>Diamond</td><td>White</td></tr><tr><td>Argument</td><td>Circle</td><td>White</td></tr><tr><td>Valid assumption</td><td>Rectangle</td><td>White</td></tr><tr><td>Invalid assumption</td><td>Rectangle</td><td>Black</td></tr><tr><td>Decision</td><td>Rectangle</td><td>Grey</td></tr></table>

![](/api/attachments/SUT8T7BB/fulltext/images/855a45ad53da2fe5f124b277e2d3bf753bca2d7c76dd6adcde468b6b5a66544b.jpg)  
Fig. 3. Hypermedia document supporting an argument.

The argument that supports prioritization by location (service network compatibility) is based on the assumption that the current service network is spread out geographically such that servicing orders by location is very economical. A detailed discussion on this argument among the design team members follows. The details of the argument are provided in the hypermedia document (SNC document) shown in Fig. 3.

## 4.3. Adding multimedia objects

## Hypermedia editor

REMAP/MM supports hyperlinks among design deliberation records and MultiMedia Objects (MMOs). In our example, during the discussion on prioritization, a service engineer explains the geographical set up of the various service center facilities, the capabilities of each center and the areas that these centers service. This leads to a complex and detailed deliberation. Due to the critical nature of the decision to the overall system design, a video clip of this session is recorded. As Fig. 3 shows, the document contains a hyperlink to the video clip. This would facilitate the review and evaluation of the decision in future by replaying the multimedia segments of the design rationale.

The Hypermedia editor, based on the Andrew EZ editor, allows the creation and editing of hypermedia documents. Hypermedia documents can include text, audio clips, raster graphics, vector graphics, and tables. As the tool does not yet support video objects, video segments in documents are incorporated using an authoring system that can be readily invoked from any hypermedia document.

## Multimedia model

Many tools for creating multimedia objects provide facilities for annotating them (with text or attributes) to facilitate understanding and easy retrieval. REMAP/MM takes a much more comprehensive approach to representing the characteristics of MMOs. A unique feature of our approach is that formal definitions of the hypermedia objects are created when these objects are defined with the hypermedia editor. Each MMO is defined to have several attributes that are useful in classifying, retrieving and reusing them throughout the systems development process.

REMAP/MM also provides mechanisms for automatically inferring the values of various attributes of an MMO using deductive rules. For instance, say an MMO elaborates an argument. The argument addresses a position, which in turn responds to an issue. The subject attribute of the MMO could be declared to be the same as that of the issue. Navigating through Figs. 2 and 3, we can see that the subject attribute of the video segment (service center discussion) can get defined to be the same as that of the issue priority scheme. In a complex network of design rationale characteristic of large scale system development activities, such a facility for dynamically defining characteristics of MMOs will be extremely valuable.

If a single MMO is used in a variety of contexts (i.e., attached to different segments of the design rationale knowledge base), its subject attribute will be dynamically defined based on all such contexts. As arbitrary chaining of rules is possible, with the conclusion part of a rule becoming part of the condition part of another, interesting inferences can be drawn. Such a facility will enable the ready identification of all the relevant pieces of the design rationale knowledge base that are related to a subject, say for review by the project team. In our example, a deductive rule may be used to propagate the subject area of the video segment to all the MMOs that are related to it (e.g., service area map). Then, automated reasoning with such information about informal objects can be performed.

## Attributes of MMO

In large projects involving multiple and often changing participants, examination of the source of design rationale is very important in ascertaining its validity, relevance and importance. This information may be represented as attributes of design rationale MMOs. Some examples of the attributes of a MMO are: its author, the other MMOs that it is linked to, the systems development project it is a part of, the type of media it is in, the task in the systems development process that it is intended for, the duration for which the object is “valid” and the stakeholders that have reviewed it, etc. Further, as the various stakeholders bring their unique perspectives and objectives, identification of the characteristics of the stakeholders that define design rationale may provide interesting insights. The following paragraphs discuss a few such characteristics that may be represented as attributes of MMOs.

Stakeholder role. The ways in which stakeholders interact with each other may provide valuable information on the group process. The phenomenon of “group think” may allow authority figures to influence the design team into making decisions that may not be appropriate. The participants’ search for social acceptance or approval from authority figures may be reflected in the rationale outcome. Therefore, explicit identification of the role of the source of design rationale is important.

Experience /background. The work habits of a participant depend on his/her experience and personal background. Whereas the rationale provided by a novice designer may have all the intermediate steps in reaching a simple decision, to an experienced designer, these steps may appear trivial and redundant to be documented. Identification of the stakeholder's experience level and background may improve the understanding and potential for reuse of rationale.

Temporal characteristics. The sequence or the order in which design issues are raised and discussed may provide valuable insights into the priorities and concerns of the design team. As REMAP/MM maintains temporal information on all the components of the design rationale (including MMOs), an analysis of such temporal characteristics of the problem solving process can be readily conducted.

Status. Tracing the status of various project activities can be facilitated by identifying “open issues”, assumptions that have not yet been “evaluated”, etc. REMAP/MM provides facilities for evaluating such characteristics of issues, assumptions, etc. For instance, a constraint can be specified to state that an assumption is considered to be evaluated only when all the parties have reviewed the multimedia objects associated with it. An integrity constraint in Telos specifies it as follows:

![](/api/attachments/SUT8T7BB/fulltext/images/95be3f43577f9580f2691c964cab62f2c978e9d762f9366adfa0c4c4056b67c2.jpg)  
Fig. 4. Concept map.

```prolog
CONSTRAINT with
rule
eval_assumption:
$forall a/ASSUMPTION
((exists h/HyperMediaObject
(h supports a) and
(a reviewed? no)
==>(a evaluated no))
)$
END
```

Specifically, the constraint states that if there exists a hypermedia object which has not been reviewed, the status of the assumption will be declared invalid (i.e., “no”). Any assertion into the knowledge base that leads to the violation of this constraint will be rejected by the system.

## Concept map

The process of information search in design rationale knowledge bases can create a significant cognitive overhead, especially in systems with a large number of nodes and links $[2]$ . This overhead can be reduced through the use of concept maps $[17]$ . The notion of concept maps, which originated in the Instructional System Design literature $[10]$ , refers to the notion of providing the user with a visual representation of the structure of the deliberation $[1]$ , $[27]$ . This representation specifies the logical paths among nodes and provides directions on which link to traverse next. Since a complete map specifying all links becomes too complex to be useful in navigation, concept maps should be provided at various levels of detail and from multiple points of view. For example, an end-user would seek to navigate the design rationale knowledgebase quite differently from a system designer.

![](/api/attachments/SUT8T7BB/fulltext/images/8b341d27af3993cfda7f060fe324187ade886680945b026f613607f0a13c3d31.jpg)  
Fig. 5. Service area map.

Table 2  
Legend of concept map

<table><tr><td>Multimedia object type</td><td>Shape</td><td>Color</td></tr><tr><td>Video</td><td>Circle</td><td>Black</td></tr><tr><td>Graphics</td><td>Diamond</td><td>Grey</td></tr><tr><td>Text</td><td>Rectangle</td><td>Light grey</td></tr><tr><td>Audio</td><td>Circle</td><td>Grey</td></tr><tr><td>Animation</td><td>Diamond</td><td>Black</td></tr><tr><td>Equation</td><td>Rectangle</td><td>Black</td></tr><tr><td>Postscript</td><td>Oval</td><td>White</td></tr><tr><td>Raster</td><td>Oval</td><td>Grey</td></tr></table>

In our example, as seen earlier, the SNC document provides hyperlinks to a video clip of the design deliberation session. This video segment may be supported by other MMOs such as a geographical map of the service area used in the discussion (service area map), a hypertext document containing the legislative requirements for utility services that need to be complied with (government regulations) and a hypertext document of the company policy (company policy) in accordance to which the system should be developed. Fig. 4 shows the concept map identifying the linkages among these MMOs. Table 2 identifies the shapes and colors of various MMOs supported. Thus, the concept map provides a graphical view of the MMObase. Hyperlinks between the MMOs facilitate navigation and retrieval. Fig. 5 shows such a hyperlink between service area map and the video segment that refers to it. While navigating through a concept map, by selecting any of the components of the objectbase, the user can review, edit or replay the contents.

## 5. Reasoning with design rationale

This section describes how design rationale captured in REMAP/MM can be used in system development activities to support the management of system evolution, system maintenance with changing requirements, design replay and ad-hoc queries to support the needs of various stakeholders.

## 5.1. Management of system evolution

REMAP/MM explicitly identifies the dependencies among the design rationale components and provides mechanisms for maintaining and reasoning with them. In our model, assumptions justify arguments. The belief in assumptions decide the validity of the arguments which in turn decide the validity of the positions. REMAP/MM supports the management of such a network of dependencies with a reason maintenance system.

Returning to our example in Fig. 2, the assumption that the design of the order processing system must be compatible with the service center network (compatibility essential) supports the argument (service network compatibility). This assumption has been ascertained to be valid by the design team based on the evaluation of available evidence. Note from Table 1 that this assumption is denoted as a valid assumption. (In contrast, assumptions that do not have valid justification are shaded in black; e.g., high process time). Our reason maintenance system propagates the belief status of assumptions to arguments, and then to positions. Therefore, the validation of the assumption compatibility essential leads to the argument service network compatibility and hence the position location becoming valid.

Similarly, assumptions that support arguments for prioritization by service type and customer type have been declared invalid. Such an evaluation of assumptions can be based on the review of evidence which may be recorded in the multimedia documents associated with the argument. If a future review of the evidence associated with an argument leads to revised beliefs in assumptions, then the system will automatically propagate the effects of such a change to validate or invalidate positions and decisions.

The mechanism for identifying positions that have valid justifications (i.e., those that are supported by current set of beliefs in relevant assumptions) will be very helpful to designers in determining whether an alternative can become part of a design solution. Also, the designer can perform “what-if” analysis by tracing the repercussions of a set of assumptions on the design solutions or by identifying changes in the set of valid assumptions that can provide valid support for an alternative.

## 5.2. System maintenance with changing requirements

Changes in requirements and assumptions are common reasons for system maintenance activities. Typically, maintenance activities are carried out at the level of implementation (i.e., code), without corresponding changes to process knowledge. We argue that the process of maintenance must be initiated by changes to process knowledge. In our environment, since dependencies among various components of the design rationale knowledge that lead to the design solution are maintained, changes to design solutions resulting from changed assumptions, decisions or requirements, will initiate the synthesis of a new design solution. For instance, changes to belief status of assumptions will automatically trigger changes in the belief status of design solutions, thereby suggesting redesign.

In our example, the design team may at a future date invalidate the assumption that service center network compatibility is a primary concern. Such a reevaluation (say, based on a review of associated MMOs by the design team) will result in the automatic propagation of this belief into making the position location lose support. This will further result in the identification of decisions and design solutions that select this position for reevaluation.

## 5.3. Design replay

Design teams often engage in retracing the steps taken during a design process when they encounter dead ends or identify errors made earlier. The design history information captured with our approach is useful in such (design) replay as it enhances the understanding of the evolution of the system. Further, it identifies various alternative steps that could have been taken in a design activity. The availability of this information reduces the need for rework. We also maintain temporal information (such as a time stamp) about assertions in the knowledge base, making chronological replay of the design process possible. Finally, instead of replaying the entire process, dependency information can be used to identify relevant components of the process that need to be replayed.

As discussed earlier, large scale design activities involve various stakeholders with different perspectives, viewpoints and expertise. Over the life cycle of large systems, the perspectives and viewpoints of the participants also keep evolving. Therefore, it is not uncommon for a design team to change significantly many critical decisions made during the earlier phases of a project. In the absence of comprehensive design records, design teams often engage in (an expensive and wasteful activity of) reconstructing earlier decisions and rationale behind them. Facilities of design replay, especially with comprehensive multimedia records, can greatly aid this task, saving time as well reducing chances of error. The reevaluation and reinterpretation of the multimedia segments in a changed context may lead to different assumptions and decisions.

## 5.4. Ad-hoc queries

REMAP/MM uses the deductive query language provided by ConceptBase to define various types of ad-hoc queries that could be used to retrieve information of interest to different stakeholders. Queries are defined as special classes whose instances are the answers to the query. The following is an example of a query in Telos to retrieve any hypermedia object that has hyperlinks to other hypermedia objects.

QueryClass RelatedMMOs isA HyperMediaObject with

constraint

\$ exists h/HyperMediaObject (this hyperlinks h)

end

Such a query will be useful to a design team in identifying all hypermedia objects that are related to a REMAP/MM object. The answer of the query could be used, say, by a design team in identifying the MMOs that need to be examined in reevaluating an assumption. Similar query classes can be defined to support various stakeholders' needs. An easy to use graphical interface is provided for displaying queries and retrieving desired information. Recursive queries are powerful tools for selective retrieval of information from a process knowledge base.

## 6. Related work

In this section, we compare our approach with several other models and systems to support the capture and use of design rationale.

## 6.1. gIBIS

The Software Technology Program of the Microelectronic Computer technology Corporation (MCC) created the gIBIS tool which provides a hypertext interface to the IBIS model. The primary focus of gIBIS is to facilitate the capture and presentation rather than automated reasoning with design rationale knowledge. Therefore, its design has been geared towards providing an efficient and easy to use interface, mechanisms for navigation through the knowledge base and efficient graphical display of the knowledge. This system has been found to be suitable for representing design deliberations in large software development activities $[37]$ .

gIBIS is constrained by the problems of IBIS, such as the lack of explicit representation of goals and the outcomes of the argumentation. Further, as it represents informal knowledge, it does not support automated reasoning with captured knowledge. These two issues have been addressed in the development of REMAP/MM.

## 6.2. IBE

IBE [19] is another hypertext system based on the IBIS model with functionalities and limitations similar to those of gIBIS. Discussing the need for future work, Lease et al. [19] state that argumentation network will be most useful only when the information is linked to artifacts created in the process. Another functionality they advocate is the availability of the history of the development of the artifacts to help the developer understand the thinking which went into their creation.

Our research addresses both these concerns. We provide two-way traceability between requirements and artifacts. By representing temporal information, an exhaustive history of the design process can be maintained and used in design replay.

## 6.3. SIBYL

SIBYL is a generic DSS that has been used for managing design rationale $[20]$ . SIBYL uses decision graphs for representing arguments for and against alternatives that satisfy a goal. SIBYL's primitives include goals, alternatives that may satisfy a goal, and claims that represent the arguments for choosing among alternatives.

SIBYL provides services such as viewpoint management, plausibility management and dependency management that are similar to those provided by REMAP/MM. In contrast to SIBYL which is a generic DSS based on primitives to represent any decision making process, our model was developed in a task specific context (i.e., systems development) using an empirical study. Though there are several similarities between REMAP/MM and SIBYL primitives, our model has additional primitives such as decisions, constraints, and design objects to explicitly represent the outcomes of the deliberation process. Finally, SIBYL does not support MMOs in its rationale management system.

## 6.4. SYNVIEW

SYNVIEW system supports indexing, evaluating, and synthesizing information [22]. This system supports a structured debate using a simplified version of the Toulmin's model of argumentation [33], [34], [35]. Though the model can be used to represent justifications for an assertion, it does not represent the context in which such justifications are made. Further, Toulmin's model does not relate the argumentation process to its outcomes.

## 6.5. Dedal

Our scheme for assigning attributes to multimedia objects is similar in spirit to the indexing scheme used in the Dedal System [3]. In Dedal, indexing patterns are formatted in the following categories: topic, subject, level of detail, media. Dedal uses queries to retrieve relevant multimedia objects from its database that closely match the request of the user.

Our work is distinct from Dedal in several ways. First, our multimedia objects are used as adjuncts to and in support of a model of design rationale. Therefore, a variety of information about the context in which these objects are part of a design record is available. The richness of the context (available in the form of various REMAP/MM model primitives) which can not be captured by a faceted indexing scheme enhances the usefulness and retrievability of MMOs.

## 6.6. Network-Hydra

Network-Hydra is a domain specific design decision support environment for the design of networks [8]. This tool focuses on providing decision support in areas such as critiquing specifications, cataloguing the solution space and simulation of usage scenarios. Our approach, instead, focuses on managing dependencies among design and process knowledge components and supporting system evolution.

Network-Hydra also uses a hypermedia based argumentation system. In addition to providing a similar facility supporting a suite of media choices, our system facilitates reasoning about such informal information by developing models about them.

## 7. Future Work

We are currently investigating several issues related to design rationale capture and management. Capturing process knowledge with minimal overhead is extremely important for a DSS to be successful. The use of multimedia electronic mail using a structured communication protocol based on REMAP/MM is under investigation. Integration of the design rationale environment with a networked multimedia conferencing system is another area of study. Providing a comprehensive set of pre-defined queries and support tools for various stakeholders would greatly enhance the usefulness of the captured knowledge. Finally, empirical evaluation of the usefulness of the design rationale knowledge components and various support mechanisms in large scale systems development projects is of significant interest.

## References

[1] R. Anderson, C. Heath, P. Luff, and T. Moran, The social and the cognitive in human-computer interaction, Technical Report EPC-91-126, Rank Xerox EuroPARC, Cambridge, UK (1991).

[2] I. Benest, An alternative approach to hypertext, Educational and Training Technology International, 28(4), pp. 341–346 (1991).

[3] C. Baudin, C. Sivard, and M. Zweben, Recovering rationale for design changes: A knowledge-based approach, In Proceedings: IEEE, Los Angeles, CA (1990).

[4] J. Conklin, and M. Begeman, Gibis: A hypertext tool for exploratory policy discussion, ACM Transactions on Office Information Systems, 6, pp. 303–331 (1988).

[5] B. Curtis, H. Krasner, and N. Iscoe, A field study of the software design process for large systems, Communications of the ACM, 31, pp. 1268–1287 (1988).

[6] P. Dourish, and S. Bly, Portholes: Supporting awareness in a distributed work group, In Proceedings: ACM Conference on Human Factors in Computer Systems CHI 1992, Monterey, CA (1992).

[7] H. Fellows, The Art and Skill of Talking with People: A New Guide to Personal and Business Success (Englewood Cliffs, NJ, Prentice-Hall, 1964).

[8] G. Fisher, A. Lemke, R. McCall, and A.I. March, Making argumentation serve design, Human-Computer Interaction, 6, pp. 393–420 (1991).

[9] G. Fisher, J. Grudin, A. Lemke, R. McCall, J. Ostwald, B. Reeves, and F. Shipman, Supporting indirect collaborative design with integrated knowledge-based design environments, Human-Computer Interaction, 7, pp. 281–314 (1992).

[10] R. Gagne, and R. Glaser, Foundations in Learning Research, In R. Gagne (Ed.), Instructional Technology: Foundations, pp. 49–84 (Lawrence Erlbaum Associates, 1987).

[11] C. Geertz, Thick Description: Toward an Interpretive Theory of Culture, Ch. 3, Interpretation of Cultures (New York, Basic Books, 1973).

[12] R. Goldman-Segall, Collaborative Virtual Communities: Using Learning Constellations: A multimedia research tool, Ch. 2, In E. Barrett (Ed.), Sociomedia: Multimedia, Hypermedia and the Social Construction of Knowledge (Cambridge, MA, MIT Press, 1992).

[13] J. Greenbaum, and M. Kyng, Design at Work: Cooperative Design of Computer Systems (Lawrence Erlbaum Associates, 1991).

[14] R. Guindon, and B. Curtis, Control of cognitive processes during software design: What tools would support

software designers?, In Proceedings: CHI-88, Washington, DC, pp. 263–268 (1988).

[15] C. Heath, and P. Luff, Explicating Face-to-face interaction, Ch. 2, In G. Gilbert (Ed.), Researching Social Life (London, Sage, 1992).

[16] B. Jordon, Technology and social interaction: Notes on the achievement of authoritative knowledge in complex settings, Technical Report IRL92-0027 (Palo Alto, CA, Institute for Research on Learning, 1992).

[17] M. Kidd, Applying hypermedia to medical education: An author's perspective, Educational and Training Technology International, 29(2), pp. 143–151 (1992).

[18] F. Lakin, J. Wambaugh, L. Leifer, D. Cannon, and C. Sivard, The electronic design notebook: Performing medium and processing medium, Visual Computer: International Journal of Computer Graphics, 5, pp. 214–226 (1989).

[19] M. Lease, M. Lively, and J. Leggett, Using an issue-based hypertext system to capture the software life-cycle process, Hypermedia, 2(1) (1990).

[20] J. Lee, Sibyl: A qualitative decision management system, In P. Winston and S. Shellard (Eds.), Artificial Intelligence at MIT: Expanding Frontiers, Ch. 5, pp. 106–133 (Cambridge, MA, MIT Press, 1990).

[21] J. Lee, Design rationale capture and use, AI Magazine, 14 (1993).

[22] D.G. Lowe, Co-operative structuring of information: The representation of reasoning and debate, International Journal of Man-Machine Studies, 23, pp. 97–111 (1985).

[23] M. Mead, Anthropology in a Discipline of Words, Ch. 2, In P. Hockings (Ed.), Principles of Visual Anthropology (Paris, Mouton Publishers, 1975).

[24] J. Mylopoulos, A. Borgida, M. Jarke, and M. Koubarakis, Telos: Representing knowledge about information systems, ACM Transactions on Information Systems, 8, pp. 325–362 (1990).

[25] B. Ramesh, and V. Dhar, Supporting systems development using knowledge captured during requirements engineering, IEEE Transactions on Software Engineering (1992).

[26] J. Rochelle, R. Pea, and R. Trigg, Videonoter: A tool for exploratory video analysis, Technical Report IRL90-0021 (Palo Alto, CA, Institute for Research on Learning, 1990).

[27] D. Russell, IDE: The Interpreter, In: J. Psotka, L. Massey, and S. Mutter (Eds.), Intelligent Tutoring Systems: Lessons Learned, pp. 323–349 (Hillsdale, NJ, Lawrence Erlbaum Associates, 1988).

[28] Ryle, Concept of Mind (Harmonds Worth, 1949).

[29] S. Shum, and N. Hammond, Argumentation-based design rationale: From conceptual roots to current use, Technical Report EPC-93-106, Rank Xerox Limited, Cambridge EuroPARC, Cambridge, CB2 1AB, UK (1993).

[30] L. Smircich, Beyond Method: Strategies for Social Research (Beverly Hills, CA, Sage, 1983).

[31] R. Stults, Experimental uses of videotapes to support

design activities, Technical Report ss1-89-19, Xerox Palo Alto Research Center, Palo Alto, CA (1988).

[32] H. Thimbleby, Delaying Commitment, IEEE Software, pp. 78–86 (1988).

[33] S. Toulmin, R. Rieke, and A. Janik, An Introduction to Reasoning (New York, NY, MacMillan, 1984).

[34] S. Toulmin, Reason in Ethics (Cambridge, UK, 1950).

[35] S. Toulmin, The Uses of Arguments (Cambridge, UK, 1958).

[36] C. Wild, and K. Maly, Towards a software maintenance support environmer, In Proceedings: Conference on Software Maintenance, Washington, pp. 297–306 (1988).

[37] K.B. Yakemovic, and J. Conklin, The capture of design rationale on an industrial development project, Technical Report STP-279-89, Microelectronic Computertechnology Corporation, Austin, TX (1989).

[38] K.B. Yakemovic, and E.J. Conklin, Report on a Development Project Use of Issue-Based Information System, In Proceedings: Conference on Computer Supported Cooperative Work, pp. 105–118 (1990).

![](/api/attachments/SUT8T7BB/fulltext/images/06ea5b075f47f3e65cd2c17d3e24afd1200cf2462cde8855d1bd8ee6310e6f8b.jpg)

Balasubramaniam Ramesh is Assistant Professor of Information Systems at the Naval Postgraduate School in Monterey, California. He received his PhD in Information Systems from New York University. His research focuses on developing and applying knowledge representation and reasoning models to support systems design and maintenance. His research interests include computer supported cooperative work, requirements engi-

neering and traceability, and supporting design and planning processes with process knowledge. His research appears in IEEE Transactions on Software Engineering, IEEE Expert, Decision Support Systems, several conference proceedings and books. Professor Ramesh is a member of the AAAI, ACM, IEEE and TIMS.

![](/api/attachments/SUT8T7BB/fulltext/images/2b237297e4531f026dcc62152aa741d2e87754510b8cadb1122a91a088442304.jpg)

Kishore Sengupta is Associate Professor of Information Systems at the Naval Postgraduate School in Monterey, California. He received his PhD in Management Information and Decision Systems from Case Western Reserve University. Dr. Sengupta's research interests are in decision support for dynamic tasks, multimedia and intelligent tutoring, and computer supported cooperative work. His research appears in IEEE Trans-

actions on Software Engineering, Management Science MIS Quarterly, and other journals, conference proceedings and book chapters.
