---
otero_id: 1256
otero_key: "ADTEUBXF"
title: "Visual support for work assignment in process-aware information systems: Framework formalisation and implementation"
authors: "Massimiliano de Leoni; Michael Adams; Wil M.P. van der Aalst; Arthur H.M. ter Hofstede"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.042"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Visual support for work assignment in process-aware information systems: Framework formalisation and implementation

Massimiliano de Leoni <sup>a,</sup>⁎<sup>,1</sup>, Michael Adams <sup>b</sup>, Wil M.P. van der Aalst <sup>a,b</sup>, Arthur H.M. ter Hofstede <sup>b,a</sup>

<sup>a</sup> Eindhoven University of Technology, P.O. Box 513, 5600 MB, Eindhoven, The Netherlands

<sup>b</sup> Queensland University of Technology, GPO Box 2434, Brisbane QLD 4001, Australia

## a r t i c l e i n f o

Article history: Received 12 July 2010 Received in revised form 1 May 2012 Accepted 21 May 2012 Available online 1 June 2012

Keywords: Process-aware information systems Work-list visualisation YAWL

## a b s t r a c t

Process-aware information systems, ranging from generic work<sup>fl</sup>ow systems to dedicated enterprise information systems, use work-lists to offer so-called work items to users. In real scenarios, users can be confronted with a very large number of work items that stem from multiple cases of different processes. In this jungle of work items, users may <sup>fi</sup>nd it hard to choose the right item to work on next. The system cannot autonomously decide which is the right work item, since the decision is also dependent on conditions that are somehow outside the system. For instance, what is “best” for an organisation should be mediated with what is “best” for its employees. Current work-list handlers show work items as a simple sorted list and therefore do not provide much decision support for choosing the right work item. Since the work-list handler is the dominant interface between the system and its users, it is worthwhile to provide an intuitive graphical interface that uses contextual information about work items and users to provide suggestions about prioritisation of work items. This paper uses the so-called map metaphor to visualise work items and resources (e.g., users) in a sophisticated manner. Moreover, based on distance notions, the work-list handler can suggest the next work item by considering different perspectives. For example, urgent work items of a type that suits the user may be highlighted. The underlying map and distance notions may be of a geographical nature (e.g., a map of a city or of<sup>fi</sup>ce building), but may also be based on process designs, organisational structures, social networks, due dates, calendars, etc. The framework proposed in this paper is generic and can be applied to any process-aware information system. Moreover, in order to show its practical feasibility, the paper discusses a full-<sup>fl</sup>edged implementation developed in the context of the open-source work<sup>fl</sup>ow environment YAWL, together with two real examples stemming from two very different scenarios. The results of an initial usability evaluation of the implementation are also presented, which provide a <sup>fi</sup>rst indication of the validity of the approach.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Process-aware information systems (PAISs) [14] are frequently applied in a variety of intra- and inter-organisational settings. Examples of such systems are work<sup>fl</sup>ow management systems, business process management systems, enterprise resource management systems (like SAP R/3), and e-business systems. Initially, these systems were mainly used to support administrative processes inside large organisations. Later their application was extended to cross-organisational processes. A PAIS is a special case of information system, as de<sup>fi</sup>ned in [3], in that it is driven by some process model. The model may be implicit or hidden, but the system supports the handling of cases in some (semi-) structured form. PAISs also have in common that they offer work to resources (typically people). The elementary pieces of work are called work items, e.g., “Approve travel request XYZ1234”. These work items are offered to the users via a so-called work-list handler. This system component takes care of work distribution and authorisation issues. Typically, PAISs use a pull mechanism, i.e., work is offered to all resources that qualify and the <sup>fi</sup>rst resource to select the work item will be the only one responsible for its execution. To provide decision support to users in choosing the right work items in the right order, basic information is provided, e.g., task name, due date, etc. However, given the fact that the work-list is the dominant interface the PAIS uses to interact with its users, it seems important to provide decision support that goes beyond a sorted list of items. If work items are selected by less quali<sup>fi</sup>ed users than necessary or if users select items in a non-optimal order, then the performance of the overall process is hampered. Hence, we propose to use richer interfaces that exploit contextual information.

In most organisations, where multiple resources have overlapping roles and authorisations and there is often a backlog of work, users will choose the next work item to perform by considering many aspects of the execution context. For instance, the choice could be driven by work items that should be completed more urgently as they may expire soon, or users may choose to perform those work items that should be executed closer to the physical location where they are positioned. Many other approaches are conceivable which may or may not depend on the speci<sup>fi</sup>c application domain.

To our knowledge, commercial as well as open source PAISs present work-lists simply as a list of work items, each with a short textual description. Some products sort the work items in a worklist using a certain priority scheme speci<sup>fi</sup>ed at design time and not updatable at run time. This approach is very similar to mail agents that list email in an inbox and allow them to be sorted based on simple criteria. No information is given about the context in which those emails were received, thus providing little or no decision support when selecting the next email to process.

To better support users in learning the execution context and determining the most opportune subsequent work items, we introduce the metaphor of maps. A map may be a geographical map (e.g., the map of a university's campus), but any other type of map may be used, e.g., process schemas, organisational diagrams, Gantt charts, etc. Work items can be visualised by dots on the map. By not <sup>fi</sup>xing the type of map, but allowing this choice to be con<sup>fi</sup>gurable, different types of relationships can be shown, thus providing a deeper insight into the context of the work to be performed.

Our work-list handler provides functionalities similar to those found in car navigation systems. Such systems provide a suggestion for the best route to a certain destination, letting the driver decide the actual route she/he prefers to take. Similarly, our work-list handler simply suggests the most appropriate work item(s), but users are free to choose any as next to work on.

Moreover, on some maps, resources may also be shown, e.g., to re-<sup>fl</sup>ect the geographical position of users. Besides the map metaphor we also use the distance metaphor. Seen from the viewpoint of a particular resource, some work items are close while others are further away. This distance may be geographic, e.g., a <sup>fi</sup>eld service engineer may be far away from a malfunctioning printer at the other side of the campus. However, many other distance metrics are possible. For example, one can support metrics capturing familiarity with certain types of work, levels of urgency, and organisational distance.

Comparing again with car navigation systems, such systems can be con<sup>fi</sup>gured to suggest a route that takes less time, fewer kilometres or that is cheaper (e.g., toll-free) to drive. Here, similarly, users can customise the most suitable/preferred distance metric.

It should be noted that the choice of metric is orthogonal to the choice of map thus providing a high degree of <sup>fl</sup>exibility in context visualisation. Resources could, for example, see a geographical map where work items, whose positions are calculated based on a function supplied at design time, display their level of urgency. In this paper, we propose different types of maps and distance metrics. The framework has been fully implemented and integrated in YAWL,<sup>2</sup> an open source work<sup>fl</sup>ow management system based on the so-called work<sup>fl</sup>ow patterns [26,28]. However, the framework and its implementation are constructed in such a way that it can easily be combined with other PAISs having the concept of work-list. Note that not only work<sup>fl</sup>ow systems provide work-lists; case handling systems, enterprise resource planning systems, call centre systems, etc. also provide such work-lists.

This paper extends the work reported in [10] in the following ways: (i) the initial proof-of-concept implementation has become a full-<sup>fl</sup>edged plug-in for YAWL; (ii) better insight has been given in the intent of the various metrics; (iii) some metrics not formalised in [10] have been added; (iv) we have conducted empirical tests with 16 subjects, which have provided a <sup>fi</sup>rst indication that the metaphor is clearly understandable by users and that our framework improves the ef<sup>fi</sup>ciency of the work performed by process participants; and (v) additional related work is discussed and compared with our work. In addition, we have introduced several new screen shots that, on the one hand, show the actual integration with YAWL, and, on the other hand, show new maps that extend the initial example of emergency management. Finally, a new second example is provided that concerns a more classical business scenario. Many of the new illustrated maps could not be designed with the previous version of the environment reported in [10]; in fact, the implementation itself has been signi<sup>fi</sup>cantly extended as to support more complex XQueries.

The paper is structured as follows. Section 2 discusses related research: on the one hand, it positions this research work in the <sup>fi</sup>eld of Information and Decision Support Systems; on the other hand, it covers the state of the art in work-list and process visualisation in PAISs, both in research and in practice. To this end, this section discusses a number of research papers and systems related to the visualisation aspects of context-aware systems. It also reports on some tools that provide user-friendly interfaces to execute queries over databases and data streams. Section 3 provides a detailed overview of the general framework. Section 4 focusses on the implementation of the framework and highlights some design choices in relation to user and system interfaces. In Section 5 the framework is illustrated through two examples. Section 6 reports the empirical tests conducted to provide an indication that the examples proposed are actually workable and draws some conclusions and lessons learned from the tests' outcomes. Section 7 summarises the contributions of the paper and outlines avenues for future work aimed at improving the implementation of the framework.

## 2. Related work

The analysis of the related literature has been carried out along two main orthogonal directions. Section 2.1 positions our work in the <sup>fi</sup>eld of Information and Decision Support Systems, whereas Section 2.2 discusses the state of the art of visualisation, with special focus on business process management.

## 2.1. Visualisation framework as decision support

Steven Alter has pointed out in [2] that the focus of Decision Support Systems should be shifted from Decision Support System as artifact to decision support within a work system: “decision support is not about the tools per se, but rather, about making better decisions within work systems in organizations” [2, p.2]. Similar concepts are also expressed or implied in other recent works in computer and business science and in operational research, such as [6,12]. This vision is aligned with the visualisation framework proposed in this paper: instead of conceiving yet another Decision Support System, the visualisation framework is meant to provide an extension to process-aware information systems, thus improving support for process participants when choosing which work item to perform next.

The visualisation framework falls into the cluster of research that is collectively known in the literature as Group Decision Support Systems [11,23]. Group Decision Support Systems are a class of information systems that provide collaboration technologies designed to support meetings and group work. Group DSSs are distinct from computer supported cooperative work (CSCW) technologies as Group DSSs are more focused on task support, whereas CSCW tools mostly aim to provide a general platform to share information and support some less structured collaboration. To date, very little work has been conducted in de<sup>fi</sup>ning highly-visual tools aimed at providing run-time support for activity assignments within cooperative groups.

Most of the work has focused on providing techniques to analyse a posteriori the typical end-user behaviours when interacting with Group DSSs to perform cooperative work.

The relevance of this work with respect to Information Systems, in general, and to Decision Support, speci<sup>fi</sup>cally, is also con<sup>fi</sup>rmed in relation with the Work Systems principles outlined by Steven Alter [4]. The goal of the 24 principles developed is to help analyse systems using a terminology that is understandable by business analysts and aligned with technology-focused people. While many principles are already addressed by process-aware information systems, in general, and YAWL, in particular, the visualisation framework enforces some of them, such as:

• Principle #9: Match the work practices with the participants. Work practices well matched to some participants might be poorly matched to others with different capabilities. When the participants have signi<sup>fi</sup>cantly different capabilities and interests (e.g., preferring work items of certain tasks as opposed to those of other tasks), the design of the system should accommodate such differences. Indeed, the visualisation framework is able to highlight to users such differences through metrics. For instance, when choosing the metric Familiarity, users should not pick work items associated to dots that are white-coloured for them: such work items are less familiar to them than to other users. Users should select and execute work items that are associated with dots whose colour is near to black (i.e., very familiar work items).

• Principle #13: Provide information where it will affect action. In some systems, users are shown irrelevant information, while the required information is not provided. The visualisation framework positions work items as dots on maps of interest. If relevant maps are de<sup>fi</sup>ned, participants are given important information related to work items, and such information can be quite helpful when choosing the next work item to perform.

• Principle #24: Maintain the ability to adapt, change and grow. The environment in which processes operate may change over time and, thus, the system should be able to adapt and grow accordingly. The visualisation framework complies with such a principle, in that the framework is so <sup>fl</sup>exible that maps of interest can be de-<sup>fi</sup>ned without restriction. Moreover, at any point in time, new maps can be included in order to highlight new viewpoints that become relevant later during the execution of the performance of new instances of certain processes.

## 2.2. Visualisation

Little work has been conducted in the <sup>fi</sup>eld of work-list visualisation. Visualisation techniques in the area of PAIS have predominantly been used to aid in the understanding of process schemas and their run-time behaviour, e.g. through simulation [15] or process mining [27]. Although the value of business process visualisation is acknowledged, both in the literature [5,16,18,25,30] and in industry,<sup>3</sup> little work has been done in the context of visualising work items.

The aforementioned body of work does not provide speci<sup>fi</sup>c support for context-dependent work item selection. This is addressed though in the work by Brown and Paik [7], whose basic idea has similarities with our approach. Images can be de<sup>fi</sup>ned as maps and mappings can be speci<sup>fi</sup>ed between work items and these maps. Work items are visualised through the use of intuitive icons and the colours of work items change according to their state. However, the approach chosen does not work so well in real-life scenarios where many work items may have the same position (especially in course-grained maps) as icons with the same position are placed alongside each other. This may lead to a situation where a map is completely obscured by its work items. In our approach, these items are coalesced in a single dot of which the size is logarithmically proportional to their number. By gradually zooming in on such a dot, the individual work items can become visible again. In addition, in [7] there is no concept similar to our distance notion, which is an ingredient that can provide signi<sup>fi</sup>cant assistance to resources for work item selection. Finally, the work of Brown and Paik does not take the visualisation of the positions of resources into account.

Most PAISs present work-lists as a simple enumeration of their work items, their textual descriptions, and possibly information about their priority and/or their deadlines. This holds both for open source products, e.g. jBPM,<sup>4</sup> as for commercial systems, such as SAP Netweaver<sup>5</sup> and BPMone<sup>6</sup>. An exception is TIBCO's iProcess Suite which provides a richer type of work-list handler that partially addresses the problem of supporting resources with work item selection. Fig. 1 (from [24]) depicts a mash-up combining the iProcess client work-list handler with Google maps. In the bottom left corner a resource's work-list is shown, and above this the lengths of the work-lists of other resources are shown. By clicking on a work item, a resource can see its geographical location on Google Maps. The iProcess Suite also supports a kind of look-ahead in the form of a list of “predicted” work items and their start times. One can also learn about projected deadline expirations and exception <sup>fl</sup>ows. This is achieved through the use of expected durations speci<sup>fi</sup>ed at design time for the various tasks. Our visualisation framework is more accurate as it can take actual execution times of work items of a task into account through the use of log <sup>fi</sup>les when considering predictions for new work items of that task. Basically, the iProcess Suite provides support for some speci<sup>fi</sup>c views (geographical position, deadline expiration) but these are isolated from each other. Our approach allows these views (and others) to be combined (e.g. a geographical view where deadlines are also visualised) thus enabling the use of views that may prove useful in certain contexts. Our approach also generalises over the type of map and goes beyond support for a single map as in the iProcess Suite (a geographical map).

The inappropriateness of relying on a single visualisation perspective to meet all information needs of process participants is also observed by Schönhage et al. [21,22]. The work described in [21] allows the current status of the running business process instances to be visualised in 2D diagrams. These diagrams merge different viewpoints, as our framework aims to do. Unfortunately, the admissible diagrams are restricted to traditional bar charts and histograms meshed to process schemas, which are visualised as undirected graphs. This limitation means that users are unable to de<sup>fi</sup>ne speci<sup>fi</sup>c domain dependent maps, which convey richer contexts for particular classes of processes. The research work reported in [22] builds on [21] and, additionally, provides a 3D business process visualisation. It relies on the concept of 3D Gadgets, which are a set of graphical primitives that can be combined to de<sup>fi</sup>ne relevant diagrams. However, the possible alternative diagrams that can be obtained are quite restricted, since the number of available gadgets is limited and new ones cannot be de<sup>fi</sup>ned by users. In addition, Schönhage et al. [21,22] do not take into account the positioning of participants on the map, nor is a notion similar to distance considered. As far as 3D business visualisation is concerned, in theory our visualisation framework allows one to de<sup>fi</sup>ne 3D maps and position work items and resources on it, although our practical implementation is only targeted at 2D visualisation.

Also related is work on business process mash-ups, which is a technique for building applications that combine information from multiple sources with process data to create an integrated view. Nowadays, there is not a complete framework to mash up process data with those of external sources as this is non-trivial: it would be necessary to agree upon standard ontologies that need to be integrated with the process data perspective. Hence contemporary process mash-up solutions are still ad-hoc, developed either for speci<sup>fi</sup>c process speci<sup>fi</sup>cations or for certain data sources. For instance, for mashing up geographical information and process data, there exist several research papers [1,17] and even commercial products (e.g., SmallWorld mentioned before). Combining geographical information with business processes is only one of the usages that we allow for. The framework and the implementation proposed in this paper are not only restricted to mere geographical data: maps can be geographical but also other map types are allowed and for nongeographical maps the concepts of task and resource location take on completely different meanings. In addition, we are not interested in adding to our framework the typical features of Geographic Information Systems, such as annotating maps with objects, since we do not want to add something that is speci<sup>fi</sup>c to one class of maps, i.e. geographic maps.

![](/api/attachments/ADTEUBXF/fulltext/images/1c88c1fdb013589e5af7b4471a3a895ef763c546e320c3c33c16210ef70c42e1.jpg)

<table><tr><td>Queue</td><td>Tot</td><td>Unoper</td><td>1st Due</td></tr><tr><td>broker</td><td>2</td><td>0</td><td>0</td></tr><tr><td>rbTestGroup</td><td>1</td><td>0</td><td>0</td></tr><tr><td>swadmin</td><td>11</td><td>1</td><td>0 2006-09-0</td></tr><tr><td>swadmin</td><td>320</td><td>141</td><td>1 2006-07-2</td></tr><tr><td>Teller Supervisors</td><td>15</td><td>2</td><td>0 2005-01-2</td></tr><tr><td>Tellers</td><td>52</td><td>45</td><td>0</td></tr><tr><td>testgrp</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Undelivered</td><td>16</td><td>14</td><td>0</td></tr></table>

<table><tr><td colspan="4">Work Items</td></tr><tr><td>Case</td><td>Process</td><td>Step</td><td>Description</td></tr><tr><td>4872</td><td>ENGPROD</td><td>ANAIDE</td><td>Analisar Ide</td></tr><tr><td>5119</td><td>ENGPROD</td><td>ANAIDE</td><td>Analisar Ide</td></tr><tr><td>719</td><td>JDM1</td><td>FORM1</td><td>forms</td></tr><tr><td>720</td><td>JDM1</td><td>FORM1</td><td>forms</td></tr><tr><td>712</td><td>JDMTEST</td><td>FORM1</td><td>Form 1</td></tr><tr><td>2173</td><td>SEOFWD</td><td>STEP2</td><td>Step Numbe</td></tr><tr><td>465</td><td>TESTCN</td><td>STEP2</td><td></td></tr><tr><td>466</td><td>TESTCN</td><td>STEP1</td><td></td></tr><tr><td>467</td><td>TESTCN</td><td>STEP1</td><td></td></tr></table>

Fig. 1. TIBCO's iProcess Client. Taken from [24].

Outside the <sup>fi</sup>eld of Business Process Management, visualising contextual information has been widely recognised as being a worthwhile goal. There exist some tools that associate context-aware information with work items, such as the systems Taskmind and TIBCO, which have already been mentioned above. Unfortunately, different perspectives are not joined in a single display; consequently, context-aware systems do not provide the feature of merging multiple perspectives.

The map metaphor has been widely used to provide user-friendly Visual Query Languages to retrieve data from databases [8,9]. In particular, Chang [9] proposes the concept of sentient maps, which may be of any nature (e.g., geographic, document-based) and are conceptually similar to the metaphor we propose in our framework. Certain viewpoints are embedded in some sentient maps, on which objects are overlaid in meaningful positions. Users can use so-called gestures to interact with the maps and retrieve the information they are interested in. This approach shares some of the ideas used in our visualisation framework, even though it is intended for database querying and does not consider the process that retrieves and manipulates the date store in databases.

## 2.3. Final remarks

In summary, while there are a number of related approaches to visualisation, there are several areas where they fall short. Firstly, they are unable to handle large numbers of concurrent work items, and they provide no notion of distance or the ability to visualise available resources. Secondly, they are typically restricted to static geographic representations, and are unable to combine views or merge multiple perspectives. Thirdly, they do not incorporate any decision support, which, leveraging on historical information about past executions, can facilitate a participants' choice on the next work item to perform. These limitations motivate, and are addressed by, the approach discussed in this paper.

## 3. The general framework

The core of the proposed visualisation framework is based on a twolayer approach: (i) maps and (ii) the visualisation of work items based on a distance notion. A work item is represented as a dot positioned along certain coordinates on a background map. A map is meant to capture a particular perspective of the context of the process. Since a work item can be associated with several perspectives, it can be visualised in several maps (at different positions). Maps can be designed as needed. When the use of a certain map is envisaged, the relationship between work items and their position on the map should be speci<sup>fi</sup>ed through a function determined at design time. Table 1 gives some examples of contextual views and the corresponding work item mapping.

Several active views can be supported at the same time whereby users can switch from one view to another. Resources can (optionally) see their own position on the map and work items are coloured according to the value of the applicable distance metric. Additionally, it may be helpful to show executing work items as well as the position of other resources. Naturally, these visualisations are governed by the authorisations that are in place.

Our framework assumes a generic life-cycle model as described in [20]. First, a work item is created, indicating that it is ready for distribution. The item is then offered to appropriate resources. A resource can commit to the execution of the item, after which it moves to the allocated state. The start of its execution leads it to the next state, started, after which it can successfully complete, it can be suspended (and subsequently resumed) or it can fail altogether. During runtime, a work<sup>fl</sup>ow engine (in our case the YAWL engine) informs the framework about the life-cycle states of work items.

Examples of maps and mappings.

<table><tr><td>Process context view</td><td>Possible map and mapping</td></tr><tr><td>The physical environment where tasks are going to be performed.</td><td>A real geographical map (e.g., Google maps). Work items are placed where they should be performed and resources are placed where they are currently located.</td></tr><tr><td>The process schema of the case that work items belong to.</td><td>The process schema is the map and work items are placed on top of tasks that they are an instance of.</td></tr><tr><td>Deadline expiration of work items.</td><td>The map is a time-line where the origin is the current time. Work items are placed on the time-line at the latest moment they can start without their deadline expiring.</td></tr><tr><td>Temporal properties of the corresponding case.</td><td>The map is a time-line but now related to the case of an event. E.g., dots are placed on the time-line at the expected moment when the case linked to corresponding work items is expected to complete.</td></tr><tr><td>Clustering of case types showing which cases are similar or belong together.</td><td>Cases are classified (either through an explicit label or by using some clustering algorithm). For the visualisation a self-organising map or a dendrogram is used. Work items are positioned based on the class of the corresponding case.</td></tr><tr><td>The organisation that is in charge of carrying out the process.</td><td>The map is an organisational chart. Work items are associated with the role required for their execution. Resources are also shown based on their organisational position.</td></tr><tr><td>The materials that are needed for carrying out work items.</td><td>The map is a multidimensional graph where the axes are the materials that are needed for work item execution. Let us assume that materials A and B are associated with axes x and y respectively. In this case, a work item is placed on coordinates (x, y) if it needs a quantity of x of material A and a quantity y of material B.</td></tr><tr><td>Costs versus benefits in executing work items.</td><td>In this case, the axes represent Revenue (the amount of money received for the performance of work items) and Cost (the expense of their execution). A work item is placed on coordinates (x, y) if the revenue of its execution is x and its cost is y. In this case one is best off executing work items close to the x axis and far from the origin.</td></tr></table>

## 3.1. Fundamentals

In this section the various notions used in our framework, e.g. work item and resource, are de<sup>fi</sup>ned formally.

## De<sup>fi</sup>nition 1. Work item

A work item w is a tuple (c, t, i, y, e, l), where:

• c is the identi<sup>fi</sup>er of the case that w belongs to.

• t is the identi<sup>fi</sup>er of the task of which w is an instance.

• i is a unique instance number.

• y is the timestamp capturing when w moved to the “offered” state (optional).

• e is the (optional) expiry deadline of w.

• l represents the (optional) spatial coordinates where w should be executed.

Dimensions y and l may be undefined when work item w is not yet offered or no speci<sup>fi</sup>c execution location exists respectively. The e value concerns timers that may be de<sup>fi</sup>ned for work items. In YAWL, parts of a process may be selected to form a cancellation region, which de<sup>fi</sup>nes a set of tasks that will be cancelled on the completion of a certain nominated task that “owns” the region. Since a timer expiry for a work item triggers its automatic completion, an expiry also triggers any cancellation region de<sup>fi</sup>ned for the expired work item. Note that a work item can potentially be a part of more than one cancellation region and that this has implications for the de<sup>fi</sup>nition of e. In such a case we consider the latest completion time without any cancellation region being triggered.

## De<sup>fi</sup>nition 2. Resource

A resource r is a pair $( \mathrm { j } , \mathrm { l } ) ,$ , where:

• j is the identi<sup>fi</sup>er of the resource.

• l represents the (optional) coordinates where the resource is currently located.

The notation $w _ { x }$ is used to denote the projection on dimension x of work item w, while the notation $r _ { y }$ is used to denote the projection on dimension y of resource r. For instance, $w _ { t }$ yields the task of which work item w is an instance.

Work items w′ and $w ^ { \prime \prime }$ are considered to be siblings if $w _ { t } ^ { \prime } { = } w _ { t } ^ { \prime \prime } .$ The set Coordinates consists of all possible coordinates. Elements of this set will be used to identify various positions on a given map.

## De<sup>fi</sup>nition 3. Position function

Let W be the set of work items, and R be the set of available resources. Let M be the set of available maps. For each available map m∈M, there exists a function

position : W∪R↛Coordinates

which returns the current coordinates for work items and available resources on map m.

For a map $m \in M ,$ the function position may be partial, since some elements of W and/or R may not have an associated position. Consider for example the case where a work item can be performed at any geographical location or where it does not really make sense to associate a resource with a position on a certain map. As the various attributes of work items and resources may vary over time it is important to see the class of functions position as time dependent. In fact, function positio $\boldsymbol { \imath } _ { m }$ is evaluated in a particular context $( \mathrm { e . g . }$ , time, weather, etc.). This context is not made explicit as a parameter here, but needs to be taken into account when evaluating the function.

To formalise the notion of distance metric, a distance function is de<sup>fi</sup>ned for each metric that yields the distance between a work item and a resource according to that metric.

## De<sup>fi</sup>nition 4. Distance function

Let W be the set of work items, and R be the set of available resources. Let D be the set of available distance metrics. For each distance metric $d \in D ,$ , there exists a function

$$
\text { distance } _ {d}: W \times R \rightarrow [ 0, 1 ]
$$

that returns a number in the range [0,1] capturing the distance between work item $w \in W$ and resource r R with respect to metric d.

Given a certain metric d and a resource r, distance (w,r) can be seen as the priority to pick work item w that is the closest to r with respect to metric d. These metric functions are de<sup>fi</sup>ned in a way that 1 is the minimum distance and the distance is greater as the metric function value is closer to 0. Hence, it is better to think of distance (w, r) as “closeness”.

By showing distances, the user could be stimulated to pick up the work item that is closest. If w and w′ are two work items that can be performed by r, then distance<sub>d</sub>(w, r) > distance<sub>d</sub>(w′, r) implies that w is preferred over w′.

## 3.2. Available metrics

This section is aimed to give a formalisation of the metrics provided with the current implementation. In order to make explanations easier, some auxiliary functions are introduced.

• past\_execution(w,r) yields the weighted mean of the past execution times of the last h work items performed by r among all work item siblings of w, with h being a con<sup>fi</sup>gurable parameter. In this context, the past execution time of a work item is de<sup>fi</sup>ned as the duration that elapsed between its assignment to r and its successful completion. Let time (w,r) be the execution time of the i-th last work item among w's siblings performed by r, then:

$$
p a s t \_ e x e c u t i o n (w, r) = \frac {\sum_ {i = 1} ^ {h} \alpha^ {i - 1} \cdot t i m e _ {i} (w , r)}{\sum_ {i = 1} ^ {h} \alpha^ {i - 1}}
$$

where $\alpha { \in } [ 0 , 1 ]$ . Both h and α can be adjusted to re<sup>fi</sup>ne the desired distance notion. The intuition behind this de<sup>fi</sup>nition stems from the fact that more recent executions should be given more consideration and hence weighted more as they better re<sup>fl</sup>ect resources gaining experience in the execution of instances of a certain task. If resource r did not yet execute h siblings of work item w, the metric needs to be adjusted. Moreover, if there are no such siblings, then past\_execution(w,r)=ϒ where ϒ is a big value in comparison with the typical execution times.

res(w) returns all currently logged-in resources that have been offered w:

$r e s ( w ) = \{ r \in R |$ w is offered to r :

• best\_past\_execution(w) denotes the smallest value for past\_ execution(w,r) computed among all logged-in resources r quali<sup>fi</sup>ed for w. Speci<sup>fi</sup>cally:

$$
b e s t \_ p a s t \_ e x e c u t i o n (w) = \min _ {r ^ {\prime} \in r e s (w)} p a s t \_ e x e c u t i o n \left(w, r ^ {\prime}\right).
$$

• best\_distance(w) returns the minimum geographic distance between a given work item w and all quali<sup>fi</sup>ed resources:

$$
b e s t \_ d i s t a n c e (w) = \min _ {r ^ {\prime} \in r e s (w)} \left\| w _ {l} - r _ {l} ^ {\prime} \right\|
$$

where ‖w −r<sup>′</sup> ‖ stands for the Euclidian distance between the spatial coordinates where w should be executed and the spatial location of resource r. Function best\_distance(w) is not total since w may be unde<sup>fi</sup>ned for certain work items w.

Using these auxiliary functions the following metrics can be de<sup>fi</sup>ned:

• Familiarity. How familiar is resource r with performing work item w? This can be measured through the number of sibling work items the resource has already performed:

$$
\begin{array}{l} \text {distance} _ {\text {Familiarity}} (w, r) \\ = \left\{ \begin{array}{c c} 0 & \text {no sibling work items} \\ \frac {\text {best\_past\_execution} (w)}{\text {past\_execution} (w , r)} & \text {otherwise} \end{array} \right.. \end{array}
$$

If nobody has ever executed work items for task w (i.e., there are no resources available that executed a sibling work item at some point), the distance value is 0 for all resources. If someone executed work item siblings of w but r did not, then distance $\dot { \iota } _ { \mathit { F a m i l i a r i t y } } ( w , r ) = \epsilon$ where - is a very small positive number, compared with typical distance values.

• Popularity. The ratio of logged-in resources having been offered w to all logged-in resources. This metric is independent from resource r making the request. The intuition is that if many resources can perform w then it is quite distant from every resource. Indeed, even if a resource doesn't pick w, it is likely that someone else is able/eager to execute w. Therefore:

$$
\text { distance } _ {\text { Popularity }} (w, r) = 1 - \frac {| \text { res } (w) |}{| R |}.
$$

If every resource can perform w, then the distance is 0. If few resources can perform w, then the value is close to 1.

• Urgency. The ratio between the current timestamp and the latest timestamp when work item w can be started by r with a small chance to expire. This estimation relies on the past execution by r of w's sibling work items. Speci<sup>fi</sup>cally:

$$
\begin{array}{l} \text {distance} _ {\text {Urgency}} (w, r) \\ = \left\{ \begin{array}{c c} 1 - \frac {t _ {\text {now}}}{w _ {e} - \text {past\_execution} (w , r)} & w _ {e} \text {is defined} \\ 0 & w _ {e} \text {is undefined} \end{array} \right. \end{array}
$$

where $t _ { n o w }$ stands for the current time and $w _ { e }$ is the time at which w is going to expire (i.e. $t _ { n o w } { < } w _ { e }$ if $w _ { e }$ is de<sup>fi</sup>ned). We assume here $t _ { n o w }$ and w as measures of the number of time units (e.g., seconds) elapsed from a certain reference point in time (e.g., January, 1st, 1970).

• Relative Geographic Distance. How close is resource r to work item w compared to the closest resource that was offered w? For the closest resource this distance is 1. In case w does not have a speci<sup>fi</sup>c spatial location where it should be executed, this metric returns 1 for all resources. Its de<sup>fi</sup>nition is:

$$
d i s t a n c e _ {R e l a t i v e \_ G e o} (w, r) = \left\{ \begin{array}{c c} \frac {\text { best\_distance } (w)}{\| w _ {l} - r _ {l} \|} & w _ {l} \text { is   defined } \\ 1 & w _ {l} \text { is   undefined } \end{array} \right..
$$

• Relative Past Execution. The metric chosen combines the familiarity of a resource with a certain work item and the familiarity of other resources that are able to execute that work item:

$$
\text { distance } _ {\text { Relative\_Past\_Execution}} (w, r) = \frac {1 / \text { past\_execution } (w , r)}{\sum_ {r ^ {\prime} \in \text { res } (w)} 1 / \text { past\_execution } (w , r ^ {\prime})}.
$$

In order to show that the last metric is correctly de<sup>fi</sup>ned, given a certain work item w and two qualifying resources $r _ { i } , r _ { j } ,$ the following must hold:<sup>7</sup>

$$
\text { distance } (w, r _ {i}) > \text { distance } (w, r _ {j})
$$

if and only if, on average, r took less time than $r _ { j }$ to perform w in the past.<sup>8</sup>

## 4. Implementation

The general framework described in the previous section has been operationalised through the development of a component that can be plugged into the YAWL system [26]. The YAWL environment is an open source process-aware information system which is based on the work<sup>fl</sup>ow patterns<sup>9</sup> and uses a service-oriented architecture. The YAWL engine and all other services (work-list handler, web-service broker, exception handler, etc.) communicate through XML messages over HTTP. The YAWL work-list handler was developed as a web application. In its graphical interface different tabs are used to show the various work items. The visualisation framework is implemented as a Java Applet and can be accessed, when enabled, through a newly introduced toolbar button located within the standard work-list interface.

The position and distance functions represent orthogonal concepts that are combined to show work items and resources on maps. The position function for a map determines where work items and resources will be placed as dots, while the distance function will determine the colour of work items. Conceptually, work item information and resource information are split and represented in different layers. Users can choose which layers they wish to see and, in case they choose both layers, which of them should overlay the other.

## 4.1. Work item layer

Distances can be mapped to colours for work items through a function colour:[0,1]→C which associates every metric value with a different colour in set C. In our implementation, colour set C ranges from blank through brown and red, to orange, yellow and eventually to a bright white. When a resource sees a black work item, this could indicate, for example, that the item is very urgent, that it is one of those most familiar to this resource, or that it is the closest work item in terms of its geographical position. While the colour of a work item can depend on the resource viewing it, it can also depend on the work item's current life-cycle state. Special colours are used to represent the various states of the work item life-cycle and Table 2 provides an overview, where each row corresponds to a particular state and its visualisation.

Resources can <sup>fi</sup>lter work items depending on the state of items. This is achieved through the provision of a checkbox for each of the states listed in Table 2. Several checkboxes can be ticked. There is an additional checkbox which allows resources to see work items that they cannot execute, but they are authorised to see.

Resources may simultaneously be offered time work items having positions that are the same or very close. In such cases their visualisations may overlap, in which case they are grouped into a so-called “group dot”. The diameter of a grouped dot is proportional to the number of work items involved. More precisely, the diameter D is determined as D=d(1+logn), where d is the standard diameter of a normal dot and n is the number of work items involved. We use a logarithmic (log) scaling for the relative size of a group dot, to avoid cluttering the map with work items.

Concerning colouring, a group dot is divided in as many slices as the dots that are grouped. Every slice is linked to one of the original dots and <sup>fi</sup>lled in with the colour of the linked dot. E.g., if the composite dot groups four dots that are coloured green, black, purple and cyan, it is sliced in four parts that are <sup>fi</sup>lled in green, black, purple and cyan.

## 4.2. Resource layer

When a resource (i.e. a user) clicks on a work item the positions of the other resources to whom this work item is offered are shown. Naturally this is governed by authorisation privileges and by the availability of location information for resources for the map involved.

Resource visualisation can be customised so that a resource, dependent upon authorisation privileges, can choose to see a) only herself, b) all resources, or c) all resources that can perform a certain work item. The latter option supports the case where a resource clicks on a work item and wishes to see the locations of the other resources that can perform this work item.

Table 2  
Visualisation of a work item depending on its state in the life-cycle.

<table><tr><td>Work item state</td><td>Colour scheme used in the work-list handler</td></tr><tr><td>Created</td><td>Work item is not shown.</td></tr><tr><td>Offered to single/multiple resource(s)</td><td>The colour is determined by the distance to the resource with respect to the chosen metric. The colour ranges from white (distant) through various shades of yellow and orange, red, brown to black (close).</td></tr><tr><td>Allocated to a single resource</td><td>Cyan</td></tr><tr><td>Started</td><td>Green</td></tr><tr><td>Suspended</td><td>The same as for “Offered”, i.e., colour based on distance.</td></tr><tr><td>Failed</td><td>Grey</td></tr><tr><td>Completed</td><td>Work item is not shown.</td></tr></table>

## 5. Two running examples

In this section we illustrate a number of features of the visualisation framework by considering two example scenarios. The <sup>fi</sup>rst scenario concerns the management of the aftermath of an emergency (e.g., an earthquake), where teams are sent to the affected area to make an assessment and provide <sup>fi</sup>rst support to victims. Team members are equipped with a laptop and their work is coordinated through the use of a PAIS and some external applications.

The second scenario is more business oriented and deals with loan requests to banks. The process of obtaining a loan requires applicants to provide information about their current <sup>fi</sup>nancial status (e.g., type and salary of their jobs) and the necessary loan. On the basis of this information, the bank makes some evaluations and decides whether applicants are entitled to have the loan granted.

## 5.1. Emergency management

In this section we brie<sup>fl</sup>y describe a sample use case of the new work-list handler that concerns emergency management. The YAWL model of the work<sup>fl</sup>ow is shown in Fig. 2. The main process for assessing buildings is named Disaster Management. The <sup>fi</sup>rst task Assess the affected area represents a quick on-the-spot inspection to determine damage to buildings, monuments and objects. For each object identi<sup>fi</sup>ed as worthy of further examination, an instance of subprocess Assess relevant objects is executed.

The further examination starts with taking some emergency actions in case some people require <sup>fi</sup>rst-aid (task Take emergency actions). After that, some pictures need to be taken and a questionnaire to be <sup>fi</sup>lled in (tasks Take pictures and Compile a questionnaire). These actions are necessary to gain insight into the situation with respect to the speci<sup>fi</sup>c object of interest. The situation is later evaluated by executing task Evaluate results, which involves the analysis of the material available.

To illustrate our framework, we assume that an earthquake has occurred in the city of Brisbane, Australia. Hence a number of cases are started by instantiating the Emergency work<sup>fl</sup>ow described above, where each case is targeted at a speci<sup>fi</sup>c city area.

Figs. 3 and 4 show three screenshots of the Visualisation Designer Tool. The user interface of this tool is composed of several tabs, each showing one of the de<sup>fi</sup>ned maps. By interacting with these tabs, users can specify a work item's position on the corresponding map. The use of this tool starts with parsing the XML <sup>fi</sup>le of a certain YAWL process speci<sup>fi</sup>cation to learn which tasks require positioning. After the parsing phase, a Task List window appears (see Fig. 3), which contains a list of process tasks. The designer may then drag tasks from the Task List window and drop them onto the selected map. It is worth reiterating that, when a position is de<sup>fi</sup>ned for a given task, it applies to all work items of the task. The task coordinates can either be de<sup>fi</sup>ned as static values, e.g. (30, 40), or dynamically through two XQueries, i.e. one for the X and one for the Y axis. The list on the right summarises for which tasks a position has been de-<sup>fi</sup>ned. Moreover the tasks in the list are partitioned into two groups, i.e. the tasks with a static position and those with a dynamic position, respectively.

![](/api/attachments/ADTEUBXF/fulltext/images/7e3163f49ac3ae8363e7476b91a90a152a718743c7475702cfc9002e6cf91157.jpg)

![](/api/attachments/ADTEUBXF/fulltext/images/f1436f354d493f3ac2d111878f62460fc7535053d394a502f9c92d3a8abac7e3.jpg)  
Fig. 2. A YAWL model for emergency management. (a) The main process, (b) the Assess relevant object subprocess.

Fig. 3 shows the case of a process map: every task is positioned statically on the corresponding rectangle that denotes it in the graphical representation of the process.

Fig. 4(a) shows how to associate an XQuery expression with a task, thus de<sup>fi</sup>ning the dynamic positioning of every work item created for it. To achieve this, the user will right-click on the dot that denotes the task (or alternatively select the task from the list on the right-hand side), which shows a pop-up dialog. Then, the user selects the menu item Set Position; in this way, a window opens that allows users to de<sup>fi</sup>ne the XQuery over the variables de<sup>fi</sup>ned for the process (see Fig. 4(b)). This window comes with two text <sup>fi</sup>elds where users can insert the XQuery for each of the X and Y coordinates.

The Visualisation Designer assists the user in formulating an XQuery by providing a pop-up dialog that lists the variables de<sup>fi</sup>ned for the process. When the user selects a variable from the list, the XQuery is <sup>fi</sup>lled with the particular expression that refers to that variable. In addition, under each of the two text <sup>fi</sup>elds used to specify XQueries, a <sup>fi</sup>eld is con<sup>fi</sup>gured, which shows any errors encountered during the XQuery de<sup>fi</sup>nition for the X and Y coordinates. If the XQuery is correctly de<sup>fi</sup>ned, the <sup>fi</sup>eld previews the result of the evaluation of the XQuery, based on the current availability of cases of the process of which that task is a member. In addition, if the preview is available for both the X and Y coordinates, the dot is visualised on the map accordingly, thus revealing an insight into its possible position at run-time. It is also possible for several cases to be applicable for this preview; in these situations, the tool selects one at random and simulates the positioning accordingly. If a preview is not available, the task is only placed in the right-hand list and the corresponding element is written in red.

Two sets of variables exist. The <sup>fi</sup>rst set includes all variables that are speci<sup>fi</sup>c to the process (such as the locations of relevant objects in the emergency management example). The second set includes some work item properties, such as the timestamp when a work item became enabled, started or was allocated to speci<sup>fi</sup>c participants, as well as the identi<sup>fi</sup>er of the process de<sup>fi</sup>nition and of the process instance the work item belongs to. Timestamps are de<sup>fi</sup>ned as the number of seconds that elapsed from January 1st, 1970. In addition, XQuery expressions can make use of the special variable now, which denotes the current timestamp.

Listing 1 displays a possible XML document that will be returned at run-time when there is a need to retrieve the variable values to compute XQueries. The main element is always the same: variables. The <sup>fi</sup>rst sub-element corresponds to the variables de<sup>fi</sup>ned for the process speci-<sup>fi</sup>cation; in this example the child elements of Assess\_relevant\_ object. The other elements, from caseID to allocatedTime, are those which describe the properties that all work items have in common.

If the computation of the XQuery for a given work item returns a negative value for the X or Y coordinate, then it is assumed that no position is given for the work item (i.e., negative values are treated as missing values).

Listing 2 shows an example of an XQuery that de<sup>fi</sup>nes how to position work items of task Take emergency action on a time-line map. The Y coordinate is computed by multiplying the caseID (an integer number) by 10. In this way, every work item referring to the same case will be placed at the same height. It is important to highlight that the variables returned are treated as being of no speci<sup>fi</sup>c type. Therefore, they need to be converted explicitly into the type of interest; this involves the use of functions like number(), xs:date(), string(), etc. Work items that have the value 28 (or higher) for their X coordinate are considered to have expired. Conversely, if work items are going to expire in the future, the amount <sup>expireTime</sup> denotes the remaining time to expi- 600 now ration where the unit of measure is 10 min (e.g. value 1 means 10 min to the deadline, value 2.5 means 25 min). By multiplying this value by 48, we express the fact that moving a work item position 48 pixels to the right corresponds to 10 min before expiration. The <sup>fi</sup>nal integer division by 1 is a simple way to truncate the decimal part of the resulting number. When this XQuery is computed over the variable values from Listing 1, the result is the following:

```xml
<coordinate>
    <x>311</x>
    <y>70</y>
</coordinate>
```

It may happen that a certain work item cannot expire (i.e. variable expire has a value of 0). In this case the work item position has a negative value for the X coordinate. Consequently, the work item will only be inserted in the left-hand side list and not positioned on the map.

Fig. 5 shows the Standard Work-list Handler of the YAWL System. The Work Queues tab, which shows the queues of work items relevant for the user, is equipped with a special button to start the Visualisation Applet (highlighted in Fig. 5(a)). Fig. 5(b) shows an example of the Visualisation Applet. There are two menus that allow users to specify whether to show the work item and/or the resource layer, as well as to con<sup>fi</sup>gure some graphical aspects (e.g., the dot size) of the visualisation. Under the menu bar, several tabs are available, one for each map de<sup>fi</sup>ned (e.g., in Fig. 5(b) there are 5 tabs: Brisbane, Relevant Object, Timeline, Emergency, Organisational Chart). For each tab, four main screen zones can be identi<sup>fi</sup>ed:

North zone allows users to select the metric of interest, to zoom in and out of the map and to manually update the positions and metric values.

East–Central zone shows the image of the map, enriched with dots and triangles. Dots identify the work items for which a location is de<sup>fi</sup>ned, and they are coloured according to Table 2. The blue colour denotes the dot currently selected. When dots overlap, they are joined to form bigger dots, since otherwise some of them would be invisible. The diameters of such dots grow logarithmically with the number of work items amalgamated. With group dots, each is divided in as many slices as the number of dots it contains. Every slice is <sup>fi</sup>lled with the colour of the corresponding original dot that has been grouped.

![](/api/attachments/ADTEUBXF/fulltext/images/7eb26bcf6adaf4b3cee9d246a5d4434cdca8d7bbb3b949c36c9dcedaa2de283f.jpg)  
Fig. 3. Example of static positioning on a process speci<sup>fi</sup>cation map in the Visualisation Designer.

Triangles are associated with the positions of users. The sole green triangle denotes the position of the currently logged in user. Grey triangles denote the positions of other users.

South zone shows information for the currently selected work item. Here the case id, task id, task description, time of offering, etc. are shown.

(a)  
![](/api/attachments/ADTEUBXF/fulltext/images/406059690290af2b648423d61e1b7f71b093e36be62aecda7609c9cfb7a98f9d.jpg)

(b)  
![](/api/attachments/ADTEUBXF/fulltext/images/4529bcc2fba840609dc284b03c94a4aa5df6107718d7da21fc7e4fde8dca6605.jpg)  
Fig. 4. Example of dynamic positioning of a task on a time-line map in the Visualisation Designer. (a) Selecting a task for dynamic positioning, (b) speci<sup>fi</sup>cation of an XQuery

```txt
<variables>
    <Assess_relevant_object>
    <ok />
    <location>
    <x>200</x>
    <y>50</y>
    </location>
    </Assess_relevant_object>

    <caseID>7</caseID>
    <processID>Emergency</processID>
    <expireTime>1257521968</expireTime>
    <enablementTime>
    1257518368
    </enablementTime>
    <startedTime></startedTime>
    <allocatedTime></allocatedTime>
    <now>1257518424</now>
</variables>

Listing 1. An example of a data set.
```

West–Central zone lists every created work item for which no position is given on the map.

Looking again at Fig. 5(b), dots and list elements are coloured differently according to the degree the user is familiar with the various work items. For the group dot in the upper-left part, note that it is composed of four slices, each coloured differently. Speci<sup>fi</sup>cally, one of the slices is <sup>fi</sup>lled with a colour that is the closest to black among all dots in the map. That is the work item the user is most familiar with.

When the user clicks on a grey triangle denoting a different process participant, the pop-up list of work items relevant for that user is displayed (see Fig. 6(a)). This feature is driven by user privileges: only some privileged users are allowed to see the work-lists of others. Work items offered only to other people are coloured according to the metric currently selected. It is worth noting that most of the work items in this map are dynamically positioned. Let us consider the work item currently selected, namely Take emergency action, which has been circled in the <sup>fi</sup>gure. The position of the work item in this geographic map is de<sup>fi</sup>ned by the XQuery in Listing 3. When it is computed over the XML document in Listing 1, the following result is returned:

```txt
<coordinate>
    <x>
    {(28+48*(number(//expireTime)-number(//now)) div 600)
    idiv 1)}
    </x>
    <y>
    {number(//caseID)*10)}
    </y>
</coordinate>

Listing 2. An XQuery to compute the position for a time-line map.
```

```xml
<coordinate>
    <x>200</x>
    <y>50</y>
</coordinate>
```

Of course, the work-list handler's primary responsibility is to manage and carry out work items, as well as to accept new offers. These operations can be performed for a certain work item by rightclicking on a dot on the map (or, alternatively, on the item in the left-hand side list in the absence of a map position), which displays a pop-up menu showing all actions admissible for the associated work item. If the dot is a group, then the pop-up menu shows every action admissible for every work item that is part of this group (e.g., Fig. 6(b)). The admissible actions are grouped by work item.

Fig. 7(a) shows the admissible actions after two work items have been accepted and started. Suppose the user wants to view the input data associated with work item Take emergency actions. To achieve this, she selects View/Edit Data… of the work item from the menu, which causes a web form to be displayed (see Fig. 7(b)). The user may insert or modify the work item's data displayed on the form, as appropriate, and may then save the updated data or may save and complete the work item directly.

Fig. 8 illustrates a time-line map. In these screen shots, group dots are labelled with the number of dots that have been joined. This is a feature that allows users to see how many dots have been grouped and it can be switched on or off. Fig. 8(a) shows three work items that are about to expire. Since their expiration timestamp is very close, they have been grouped. In order to learn which of the three work items has the earliest expiration, it is necessary to zoom in, so as to disaggregate them. After zooming in the group dots are split as shown in Fig. 8(b). The leftmost dot in Fig. 8(a) is split into two dots in Fig. 8(b); one corresponding to two work items and one corresponding to a single work item. Zooming in more will reveal all work items as separate dots.

Fig. 9 depicts a screen shot of an organisational map; the emergency management process involves three roles, which are therefore present in the organisation chart: Rescue Worker is the more general role, which every participant belongs to; additionally, there are two roles, namely Coordinator and Camera, which are specialisations of the former. In this map, work items are (statically) positioned on the role that process participants need to play for their performance. This map also visualises resources, who are located on the most speci<sup>fi</sup>c role they can play.

## 5.2. Applying for a bank loan

This example is inspired by the process schema that also served as running example in [19]. The loan application process starts when an applicant submits an application (with the proposed amount). Based on the amount requested in the application, a monthly repayment amount is computed. Afterwards, a credit clerk checks whether it is complete. If not, the clerk requests additional information and waits until this information is received before proceeding. For a complete application, the clerk performs further checks to validate the applicant's income and credit history. Different checks are performed depending on whether the requested loan is large (e.g. greater than \$500) or small. The validated application is then passed on to a manager to decide whether to accept or reject the application. Finally, both in case of acceptance or rejection, the applicant is noti<sup>fi</sup>ed of the decision.

Besides the geographic map, every other map described for the Emergency Management scenario is also relevant for the loan applica tion process. Furthermore, some additional maps can be considered.

(a)  
![](/api/attachments/ADTEUBXF/fulltext/images/c24e263239d415086207172b881e4439ebf1eae35c516edebcf592d31588dedc.jpg)

(b)  
![](/api/attachments/ADTEUBXF/fulltext/images/8ea7ded771d69a1d1f40a7c7a74a7e5b30b19d432ff2b29557b51c6108cf277a.jpg)  
Fig. 5. The integration of the Visualisation Applet in YAWL. (a) The YAWL Standard Worklist Handler is equipped with a button, highlighted here with a dark (brown) circle, to start the Visualisation Applet. (b) The integration of the Visualisation Applet with the standard Worklist Handler is made in a speci<sup>fi</sup>c web page.

(a)  
![](/api/attachments/ADTEUBXF/fulltext/images/34d1827ecf597988d580b22bae66f69bc165aa51e1242e1cf57c5422cb57776c.jpg)

(b)  
![](/api/attachments/ADTEUBXF/fulltext/images/ce3794f15fe335cb63cc1cd350eab4b1a9148acf304b65e5123a962228fd5390.jpg)  
Fig. 6. Run-time examples of a geographic map for Emergency Management. (a) Triangles denote the process participants' positions. By right-clicking on a triangle, one can view the work items relevant for that participant. Work item elements are coloured according to their value for the Familiarity metric. (b) By clicking on a group dot, one can see all admissible actions for constituent work items.

Fig. 10 shows the use of two additional maps that can help process participants to decide whether to approve or deny the applications received.

The map of Fig. 10(a) is a graph where the axes denote the calculated monthly repayment for the loan amount requested (X-axis) and the salary of the applicant (Y-axis). Work items that refer to a certain application are positioned according to the salary and the amount of the monthly instalment required to repay the loan. From the viewpoint of the bank/organisation that supplies loans, the approval is more risky if the applicant is given a loan of which the monthly instalment amount is close to, or even exceeds, the salary. Consequently, an application is more likely to be successful when the work items of the associated case are well above the diagonal line in Fig. 10(a).

The second map in Fig. 10(b) considers the data of the payment of the last instalment and the employment type of the application (<sup>fi</sup>xed-term or permanent). For applicants who hold a permanent position, the relative work items are shown in the list on the left (i.e., no position on the map). For applicants who hold a <sup>fi</sup>xed-term position, the map area is divided in two parts, whether or not the requested loan expiry date is earlier or later than the end of the <sup>fi</sup>xed-term contract. In both cases, the X coordinate corresponds to the number of months after/before the contract ends. Clearly, applications for loans should in most cases be rejected when the expiry date requested is later than the end of the applicant's employment contract (if <sup>fi</sup>xed term). This last example shows the power of the approach: it is even possible that different work items for the same task may or may not have a position on the map, as this is determined on the basis of some variable values. Listing 4 shows the actual XQuery used to position work items on this map. It makes use of conditional statements (i.e. ) and relies on the fact that if at least one coordinate between X and Y has a negative value, the work item is not positioned on the map (but only shown in the left list). Speci<sup>fi</sup>cally, if the value of variable contractEndData is not de<sup>fi</sup>ned (i.e. the loan applicant holds a permanent position), the coordinates for the work items that refer to that application are set to (−1, −1). That causes these work items to be placed in the list on the left-hand side. Otherwise, coordinate x is given a value of 75 pixels multiplied by the time difference as absolute value in trimesters between the end of the <sup>fi</sup>xed-term contract and the last loan instalment. Since the origin of the coordinate system is 48 pixels from the border, a constant of 48 is added. The y coordinate is statically set either to 145 or 295, depending on whether the last instalment is after or before the contract-end date, respectively.

(a)  
![](/api/attachments/ADTEUBXF/fulltext/images/cb42a95a4fb4d4dd131284dad20bfd67ca38ae848cc180f542cc6da4fb1adda1.jpg)

(b)  
![](/api/attachments/ADTEUBXF/fulltext/images/bd577188f3d50a8b12b709d176fb26e3c028b82bc0857e1c79c9142ac8c2fec5.jpg)  
Fig. 7. An example of the completion of a started work item. (a) Detail of the pop-up menu of admissible actions when two work items are started. (b) An example of a web form used to execute work items. This form is dynamically generated to insert/view/modify work item data, as well as to complete the work item.

![](/api/attachments/ADTEUBXF/fulltext/images/4cbf34e12c656a5ebea17b911540708aac81b326bcb1a9e6f66844b9b135e1f4.jpg)

(a)  
![](/api/attachments/ADTEUBXF/fulltext/images/19cac35be91cfcc265aab6b8b160002d6091dc32ba4d7a31abca630bc6087643.jpg)

(b)  
![](/api/attachments/ADTEUBXF/fulltext/images/334fd49e3f24e1e11abe70cd6ccd404ccefe453f8a29918f0ab1b7b2b840f738.jpg)  
Fig. 8. Examples of a time-line map applied to Emergency Management. (a) Dots are placed according to the expiry times of the associated work items. Dots referring to work items that expire in close proximity to one another have been grouped. (b) When zooming in on the map, some dots overlap no longer. Zooming is a desirable feature to disaggregate dots

![](/api/attachments/ADTEUBXF/fulltext/images/2102b1baecfd7d783d525437b5c282e5815609f499055221ffd171f6e61169ce.jpg)  
Fig. 9. An example of an organisational map for Emergency Management. Work items are positioned on the role that a participant needs to play for their performance. Resources are positioned on the most speci<sup>fi</sup>c role they can play.

## 6. System evaluation

The previous sections have introduced the problem of supporting work assignment and proposed a system to address it. Section 5 has discussed two running examples to illustrate the practical feasibility of the approach.

This section is intended to go beyond the simple proof that the system can actually be built and to focus on its evaluation with end users. In particular, it reports on the outcomes of a set of empirical tests conducted to verify whether the metaphor is understandable by users and to what degree the approach proposed can meaningfully assist with choosing the most appropriate work items to perform. Finally, we provide a discussion which includes lessons learnt.

## 6.1. Co-operative evaluation

The empirical tests have been conducted using Co-operative Evaluation, which is a mature fully documented methodology in the <sup>fi</sup>eld of human–computer interaction [13]. This is a cost-effective technique for identifying usability problems in prototype products and processes. The technique encourages design teams and users to collaborate in order to identify usability issues and their solutions. Speci<sup>fi</sup>cally, a group of 16 subjects was chosen, consisting of 15 students and one post-doctorate researcher, all of Eindhoven University of Technology and with various backgrounds in computer science. They were asked to carry out some tasks of process instances of the Emergency Management example described in Section 5.1. While performing such tasks, subjects had to explain what they were doing by talking or ‘thinking-aloud’. Notes were taken of all behaviours exhibited by the subiects in order to measure the degree of efficiency and effectiveness observed during the empirical tests. In particular, for our tool, ef<sup>fi</sup>ciency refers to the percentage of work items picked as next that re<sup>fl</sup>ected the best choice. Of course, almost all combinations of maps and metrics imply a different concept of “best”. Hence, for each subject, we selected a certain number of different combinations and, for each combination, we tracked the number of work items chosen by users that re<sup>fl</sup>ected the best choice for that combination. In order to measure the degree of effectiveness, we kept track of the number of work items for which subjects needed some assistance or made some mistakes during the execution.

After each evaluation session with a subject, he/she had to <sup>fi</sup>ll in a questionnaire that concerned questions to collect her/his impressions and expectations as regards the tool. In summary, this approach provides a valuable means of verifying the effectiveness and ef<sup>fi</sup>ciency of the system, eliciting further possible improvements. This method is, therefore, an eminently formative evaluation method, rather than a summative one. It is useful for identifying those usability ‘bugs’ that can affect the effectiveness of the system being evaluated.

It is worth highlighting that, because of the user-intensive nature of this method, it is dif<sup>fi</sup>cult to run large numbers of experiments with users. Nevertheless, as documented in [13], past applications of such a method have shown that the careful choice of a group of subjects, even if relatively small, can help to reduce the problem of obtaining subjective results.

## 6.2. Evaluation outcomes and lessons learned

The administration of the tests has shown that our approach can meaningfully assist in choosing the best work items to perform. Fig. 11 depicts some of the most important results that have come out of the empirical tests. In particular, Fig. 11(a) shows that the tool can signi<sup>fi</sup>cantly increase the degree of ef<sup>fi</sup>ciency and effectiveness when performing process instances. The <sup>fi</sup>rst bar reports the number of work items that have altogether been carried out by the subjects involved in the evaluation.

The second and the third bar shows, respectively, the number of work items for which we needed to give some assistance to the subjects and the number of work items for which users made some mistakes during the execution. Typically, mistakes were concerned with carrying out a wrong action for reaching a certain objective; for instance, a mistake could be to choose to work on a certain work item, but, in fact, to perform actions on a different one (e.g. a user starts working on a certain work item whereas the intention was to start a different one).

As shown in the <sup>fi</sup>gure, altogether the number of work items that required assistance or for which mistakes were made, were 54 out of

(a)  
![](/api/attachments/ADTEUBXF/fulltext/images/0aa425c84d47ed39ad9cac5dddfd9e5354e8fd6486d3208a65273c93c8714a45.jpg)

(b)  
![](/api/attachments/ADTEUBXF/fulltext/images/eb9efd7ab6f4e18fb4590e4158168bdd93d097e5026dc19825a3852c09c4ac6b.jpg)  
Fig. 10. Examples of dedicated maps assisting in the handling of bank loans. (a) Work items are positioned on this map according to the applicant's salary and the monthly instalment amount. Work items under the line y=x refer to applications that should have less chance of being accepted. (b) Work items are placed according to the time difference between the date of the last loan instalment and the end of the <sup>fi</sup>xed-term contract of the applicant. Work items for cases of applicants holding permanent positions are put in the left list. Applications of cases whose work items are in the “after” zone (last instalment after contract end) should probably be reiected.

154 (35%). This value seems to suggest a degree of effectiveness which is not very high, but it is worth highlighting that the subjects performed the tests without receiving training. As a matter of fact all mistakes and requests for assistance occurred when the subjects were executing the <sup>fi</sup>rst work items; after a few interactions, the subjects did not need any further assistance and started mastering the interaction with the tool. The decision of giving no prior training was motivated by the fact that we wanted to check the subjects' initial reaction to the tool. Indeed, it is valuable to try to increase the usability to a level for which no training is needed, nor reading a manual or documentation.

The fourth bar reports the number of work items chosen by subjects that re<sup>fl</sup>ected the best choice: altogether 136 out of 154 (88%). This implies a quite high level of ef<sup>fi</sup>ciency of the tool: almost 9 times out of 10 the tool has meaningfully directed the subjects to the right choice of the work items to carry on as next. To the precise question posed in the questionnaire: Do you believe that the tool can meaningfully assist with choosing the “best” work item?, all subjects have answered much or very much. This con<sup>fi</sup>rms that the subjects also recognise the tool's ef<sup>fi</sup>ciency.

```txt
<coordinate>
<x>
{if (string(//contractEndDate)=' ')
    then -1
    else 
    (48+75*
    (abs((xs:date(//expireDate)-
    xs:date(//contractEndDate))
    div xs:dayTimeDuration('PT24H')) idiv 90))
}
</x>
<y>
{if (string(//contractEndDate)=' ')
    then -1
    else 
    if ((xs:date(//contractEndDate)-
    xs:date(//contractEndDate))
    div xs:dayTimeDuration('PT24H')>0)
    then 
    145
    else 
    295
}
</y>
</coordinate>
```  
Listing 4. An XQuery to compute work item positions for the map in Fig. 10(b).

Fig. 11(b) and (c) show the answers given by subjects to two of the most important questions in the questionnaire. The <sup>fi</sup>rst depicts the level of intuitiveness and usability of the tool as perceived by users: only 25% of the subjects answered that the tool was not very usable, and none answered that the tool was not usable at all. The answer that the tool is not very usable can perhaps be explained by the fact that we did not give any initial training to the users. Fig. 11(c) deals with the subjects' perception of the tool's maturity: 75% of the subjects found the tool to be at least suf<sup>fi</sup>ciently mature. The most critical responses were mainly related to the user interface. It was considered by some users to be quite unattractive and, in a few cases, slow in refreshing the maps and the dots on them (e.g., when around 100 work items were being offered at the same time). While we are planning to improve the interface's look-and-feel and the ef<sup>fi</sup>- ciency in refreshing the maps in case of changes, these critical responses do not negate the claim that our framework assists the decision of choosing the next work item.

As far as the metrics are concerned, the subjects recognised the signi<sup>fi</sup>cance of the metrics proposed; special interest was shown for urgency (75% of the subjects) and popularity (38%). A couple of subjects also suggested a new metric that takes into account the frequency of work items of a certain type: if a subject is offered a number of work items of the same type, their colour should approach black (i.e., to denote their closeness), thereby suggesting that the choice of those work items has urgency so that the potential of a process bottleneck at that point can be mitigated. The idea is really interesting and we are planning to extend the metrics' repertoire to include it.

While the experiment results indicate the general usefulness of the tool, they also raised areas for further improvements. The <sup>fi</sup>rst improvement concerned the mapping of the distance values to the colours. As described in [10], before conducting the experiments, the colours associated to values of distance metrics ranged from white (very far) to red (very close). Experiments have shown that some users encountered problems distinguishing work items on the maps whose distance value differed by up to 10–20%: the corresponding dots seemed to be <sup>fi</sup>lled with the same colour. And the phenomenon became more marked when dots were positioned further apart in the maps. The problem was caused by the original colour palette, which was too small. Hence, signi<sup>fi</sup>cant differences of distance values were mapped to colours too similar.

![](/api/attachments/ADTEUBXF/fulltext/images/14b3b214352d42fd1ebb9c9d0fab0f16b25cb65ecf41c978e1496ae58b43c092.jpg)

(b)  
![](/api/attachments/ADTEUBXF/fulltext/images/2e21d8f463b8f61244f75ee9c30d0e0d0cef3950b0ef0f884abc725566c573d2.jpg)

(c)  
![](/api/attachments/ADTEUBXF/fulltext/images/ef59b7e1172e46848c66101dba3a6cc7c9946eee6f18f648cd7dedf33683a47d.jpg)  
Fig. 11. Outcomes of empirical tests. (a) Degree of ef<sup>fi</sup>ciency and effectiveness measured during the user evaluation. (b) Intuitiveness and usability as perceived by users. (c) Maturity of the tool as perceived by users.

The second improvement concerned very colourful maps: the work item dots could be confused with the background image. Finally, in order to improve the effectiveness, users have suggested the introduction of a legend to gain a quick insight into the colours used for dots as well as to give an explanation of the metrics and their purpose.

Regarding the legend, we plan to introduce it in the near future. To make the difference in distance values clearer, the colour palette has been extended to allow for black (very close) and different shades of brown and purple, in addition to the original gradations of red, orange and yellow; white still signi<sup>fi</sup>es great distance.

In order to increase the contrast between dots and maps, the tool allows maps to become slightly transparent and/or shown in greyscale. The experiment subject group tends to agree that these features increase the contrast between a map and the work item dots shown on it, making recognition of the dots easier. Nevertheless, as a general guideline, it is advisable to use maps with unnecessary details removed (e.g. geographic maps should not have too many labels and point-of-interest descriptions).

In summary, the outcomes of the empirical tests show that the metaphor of maps and metrics underpinning the visualisation framework was clearly understood by the subjects interviewed. The fact that 88% of the work items chosen by subjects re<sup>fl</sup>ected the best choice indicates that the tool provides meaningful support when choosing the next work item to perform. It may be inferred from these outcomes that using the tool can result in increased ef<sup>fi</sup>ciency of work performance by process participants.

## 7. Conclusions

In this paper a general visualisation framework is presented that can aid users in selecting the right work item to work on next among a potentially large number of work items offered to them. The framework uses the map metaphor to show the locations of work items and resources. A distance metaphor is used to show which work items are “close” (e.g., urgent, similar to earlier work items, or geographically close). Both concepts are orthogonal and this provides a great deal of <sup>fl</sup>exibility when it comes to presenting work to people. For example, one can choose a geographical map to display work items and resources and use a distance metric capturing urgency. The framework has been implemented as a component that runs within the YAWL environment. By using well-de<sup>fi</sup>ned interfaces the implementation is generic so that in principle it could be exploited by other PAISs as well, assuming that they are suf<sup>fi</sup>ciently open and can be con<sup>fi</sup>gured/extended to provide the required interface methods. The component is also highly con<sup>fi</sup>gurable: users can switch from one distance metric to another when some aspects are more relevant than others, in addition they can change the map to gain a different perspective on the process. Resources can also be visualised on maps. This functionality is useful when determining how appropriate the choice of a particular work item is and which other resources are in close proximity. This assists the user in deciding which particular work item to choose to do next. Of course such information can only be viewed if the user has suf<sup>fi</sup>cient privileges.

The paper has also detailed two relevant examples coming from very different scenarios: the <sup>fi</sup>rst scenario is Emergency Management, which is mobile and pervasive, whereas the second concerns bank loans, which is more business-oriented. The applicability of our approach in both settings suggests the generality of our ideas. In fact, various types of maps could be shared among both applications. Interested readers can watch two videos that demonstrate the usage of the tool, using the Emergency Management example presented in this paper, at www.yawlfoundation.org/resources/videos. The visualiser tool itself can be downloaded from http://www.win.tue.nl/ \~mdeleoni/YAWLApplet.html and installed into the standard YAWL environment.

The implementation has also undergone an initial usability evaluation with end users. The evaluation outcomes, which are reported in the paper, have shown that the metaphor of maps and metrics is clearly understood and the tool provides meaningful decision support when choosing the next work item that a process participant should execute. However, in order to de<sup>fi</sup>nitively determine the validity of the framework and its operationalisation, it is necessary to conduct a thorough end-user evaluation in a real working environment. Through this thorough evaluation we also want to make our approach more operational, e.g. by providing guidelines and additional con<sup>fi</sup>guration support to users when they need to create new maps and associate positions to work items.

Further research aims at adapting the framework described in this paper for process mining. The goal of process mining is to use event data to extract process-related information, such as bottlenecks and other issues that may arise during execution. While there has been extensive development of automated techniques for process mining in the last decade, it is becoming increasingly evident that achieving more complex analyses involves a level of human interaction. Therefore, we aim at extending the features of process mining tools to combine automated analysis with interactive visualisations. In fact, we are going to focus on ProM [29], which we are more familiar with, and implement these features as new plug-ins for it. This would allow decision makers to combine their <sup>fl</sup>exibility, creativity, and background knowledge to develop an effective understanding of past executions of business processes. If the con<sup>fi</sup>guration of a map at a particular moment (i.e., the dots for work items and resources, and their positions on the map) corresponds to a “photo”, then the iterative replay of an event log can be seen as a “movie”. The insights obtained from such visualisations can be used to improve processes by removing inef<sup>fi</sup>- ciencies and addressing non-compliance and policy violations.

## Acknowledgements

The authors would like to thank Francesco Cardi and Giancarlo La Medica, former students of the Faculty of Computer Engineering, who contributed with their theses work to the development of the Visualisation Applet and the Visualisation Designer, respectively. Massimiliano also gratefully acknowledges Massimo Mecella, assistant professor at Department of Computer Science and Engineering of SAPIENZA — Università di Roma, for having opened the door to the two students to focus their theses on the respective topics. The authors also wish to thank the anonymous reviewer of earlier drafts of this article, and those who took part in the evaluation.

## References

[1] G. Alonso, C. Hagen, Geo-Opera: work<sup>fl</sup>ow concepts for spatial processes, Proceedings of the 5th International Symposium on Advances in Spatial Databases (SSD '97), Volume 1262 of Lecture Notes in Computer Science, Springer, 1997, pp. 238–258.

[2] S. Alter, A work system view of DSS in its fourth decade, Decision Support Systems 38 (2004) 319–327.

[3] S. Alter, De<sup>fi</sup>ning information systems as work systems: implications for the IS <sup>fi</sup>eld, European Journal of Information Systems 17 (2008) 448–469.

[4] S. Alter, R. Wright, Validating work system principles for use in systems analysis and design, Proceedings of the 30th International Conference on Information System (ICIS 2010), Saint Louis, USA, 197, AIS eLibrary, 2010.

[5] R. Bobrik, M. Reichert, T. Bauer, View-based process visualization, Proceedings of the 5th International Conference on Business Process Management (BPM 2007), Brisbane, Australia, Volume 4714 of Lecture Notes in Computer Science, Springer, 2007, pp. 88–95.

[6] E. Bonabeau, Decisions 2.0: the power of collective intelligence, MIT Sloan Management Review, 2009.

[7] R. Brown, H.Y. Paik, Multi-faceted visualisation of worklists, Journal on Data Semantics XII (2009) 153–178.

[8] K. Camara, E. Jungert, A visual query language for dynamic processes applied to a scenario driven environment, Journal of Visual Language and Computing 18 (2007) 315–338.

[9] S.K. Chang, The sentient map, Journal of Visual Language and Computing 11 (2000) 455–474.

[10] M. de Leoni, W.M.P. van der Aalst, A.H.M. ter Hofstede, Visual support for work assignment in process-aware information systems, Proceedings of the 6th International Conference on Business Process Management (BPM 2008), Milan, Italy, Volume 5240 of Lecture Notes in Computer Science, Springer, 2008, pp. 67–83.

[11] A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker Jr., D.R. Vogel, Information technology to support electronic meetings, Management Information Systems Quarterly 12 (1988) 591–624.

[12] S.R. Diasio, N. Agell, The evolution of expertise in decision support technologies: a challenge for organizations. Proceedings of the 13th International Conference on Computer Supported Cooperative Work in Design (CSCWD 2009), Santiago, Chile, IEEE Computer Society, 2009, pp. 692–697.

[13] A. Dix, J.E. Finlay, G.D. Abowd, R. Beale, Human–Computer Interaction, 3rd. edition Prentice Hall, 2003.

[14] M. Dumas, W.M.P. van der Aalst, A.H.M. ter Hofstede, Process-Aware Information Systems: Bridging People and Software through Process Technology, Wiley, 2005.

[15] G. Hansen, Automated Business Process Reengineering: Using the Power of Visual Simulation Strategies to Improve Performance and Pro<sup>fi</sup>t, Prentice-Hall, Englewood Cliffs, 1997.

[16] S. Jablonski, M. Götz, Perspective oriented business process visualization, in: Proceedings of BPM Workshops 2007, Brisbane, Australia, volume 4928 of Lecture Notes in Computer Science, (2008) pp. 144–155.

[17] D.S. Kaster, C. Bauzer Medeiros, H. Vieira da Rocha, Supporting modeling and problem solving from precedent experiences: the role of work<sup>fl</sup>ows and case-based reasoning, Environmental Modelling and Software 20 (2005) 689–704.

[18] P. Luttighuis, M. Lankhorst, R. Wetering, R. Bal, H. Berg, Visualising business processes, Computer Languages 27 (2001) 39–59.

[19] A. Rozinat, M.T. Wynn, W.M.P. van der Aalst, A.H.M. ter Hofstede, C.J. Fidge, Work<sup>fl</sup>ow simulation for operational decision support, Data & Knowledge Engineering 68 (2009) 834–850.

[20] N. Russell, W.M.P. van der Aalst, A.H.M. ter Hofstede, D. Edmond, Work<sup>fl</sup>ow resource patterns: identi<sup>fi</sup>cation, representation and tool support, Proceedings of the 17th International Conference on Advanced Information Systems Engineering (CAiSE 2005), Porto, Portugal, Volume 3520 of Lecture Notes in Computer Science, Springer 2005 pp. 216-232

[21] B. Schönhage, A. Eliëns, Management through vision: a case study towards requirements of BizViz, International Conference of Information Visualisation (AVI 2000), Palermo, Italy, IEEE Computer Society, 2000, pp. 387–392.

[22] B. Schönhage, A. van Ballegooij, A. Elliëns, 3D gadgets for business process visualization—a case study, Proceedings of the Fifth Symposium on Virtual Reality Modeling Language (Web3D-VRML 2000), Monterey, USA, ACM, 2000, pp. 131–138.

[23] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2002) 111–126.

[24] B. Silver, The BPMS Report: TIBCO iProcess Suite 10.6, Technical Report, Bruce Silver Associates, 2007.

[25] A. Streit, B. Pham, R. Brown, Visualization support for managing large business process speci<sup>fi</sup>cations, Proceedings of the 3rd International Conference on Business Process Management (BPM 2005), Nancy, France, Volume 3649 of Lecture Notes in Computer Science, Springer, 2005, pp. 205–219.

[26] A.H.M. ter Hofstede, W.M.P. van der Aalst, M. Adams, N. Russell (Eds.), Modern Business Process Automation: YAWL and its Support Environment, Springer-Verlag, 2010.

[27] W.M.P. van der Aalst, Process Mining — Discovery, Conformance and Enhancement of Business Processes, Springer, 2011.

[28] W.M.P. van der Aalst, A.H.M. ter Hofstede, B. Kiepuszewski, A.P. Barros, Work<sup>fl</sup>ow patterns, Distributed and Parallel Databases 14 (2003) 5–51.

[29] H.M.W. Verbeek, J.C.A.M. Buijs, B.F. van Dongen, W.M.P. van der Aalst, XES, XESame, and ProM 6, in: Proceedings of Information Systems Evolution (CAiSE Forum 2010), Hammamet, Tunisia, volume 72 of Lecture Notes in Business Information Processing, (2011) pp. 60–75.

[30] W. Wright, Business visualization adds value, IEEE Computer Graphics and Applications 18 (1998) 39.

Dr Massimiliano de Leoni is a post-doctoral researcher at Technische Universiteit Eindhoven, The Netherlands (TU/e). Previously, he performed post-doctoral research at SAPIENZA — Università di Rome, after earning a Ph.D. in Computer Science and Engineering there. He has also spent 6 months with the Business Process Management Group at Queensland University of Technology, Brisbane, and made a short visit to the Intelligent Agents group at RMIT University in Melbourne.

Dr Michael Adams is a Senior Lecturer in the Information Systems School. Science and Engineering Faculty, Oueensland University of Technology, Brisbane, Australia, and is a member of the Business Process Management Discipline there.

Prof, dr. ir. Wil van der Aalst is a full professor of Information Systems at the Technische Universiteit Eindhoven (TU/e). He is also an adjunct professor at Queensland University of Technology (QUT). His research interests include work<sup>fl</sup>ow management, process mining, Petri nets, business process management, process modelling, and process analysis. He is an elected member of the Royal Holland Society of Sciences and Humanities (Koninklijke Hollandsche Maatschappij der Wetenschappen) and the Academy of Europe (Academia Europaea).

Prof. Arthur ter Hofstede is a Professor in the Information Systems School in the Science and Engineering Faculty, Queensland University of Technology, Brisbane, Australia, and is Head of the Business Process Management Discipline. He is also a Professor in the Information Systems Group at Eindhoven University of Technology, Eindhoven, The Netherlands. His main research interests lie in the area of business process automation.
