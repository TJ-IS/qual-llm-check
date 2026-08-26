---
otero_id: 1954
otero_key: "RAEAFM6N"
title: "Enabling flexible location-aware business process modeling and execution"
authors: "Xinwei Zhu; Seppe vanden Broucke; Guobin Zhu; Jan Vanthienen; Bart Baesens"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.12.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enabling flexible location-aware business process modeling and execution

Xinwei Zhu <sup>a,</sup>⁎, Seppe vanden Broucke <sup>b</sup>, Guobin Zhu <sup>a</sup>, Jan Vanthienen <sup>b</sup>, Bart Baesens <sup>b,c</sup>

<sup>a</sup> International School of Software, Wuhan University, Luoyu Road 37, Hongshan, Wuhan, Hubei, China

<sup>b</sup> Research Center for Management Informatics (LIRIS), KU Leuven, Naamsestraat 69, B-3000 Leuven, Belgium

<sup>c</sup> School of Management, University of Southampton, Highfield Southampton SO17 1BJ, United Kingdom

## a r t i c l e i n f o

Article history: Received 17 June 2014 Received in revised form 2 October 2015 Accepted 10 December 2015 Available online xxxx

Keywords: Business process management Geographic information systems Location-aware processes Geospatial processes Process modeling and execution Colored Petri nets

## a b s t r a c t

Business process management (BPM) has emerged as one of the abiding systematic management approaches in order to design, execute and govern organizational business processes. Traditionally, most attention within the BPM community has been given to studying control-flow aspects, without taking other contextual aspects into account. This paper contributes to the existing body of work by focusing on the particular context of geospatial information. We argue that explicitly taking this context into consideration in the modeling and execution of business processes can contribute to improve their effectiveness and efficiency. As such, the goal of this paper is to make the modeling and execution aspects of BPM location-aware, i.e. to govern and constrain controlflow and process behavior based on location-based constraints. We do so by proposing a Petri net modeling extension which is formalized by means of a mapping to colored Petri nets (CPNs). Our approach has been implemented using CPN Tools and a simulation extension was developed to support the execution of location-aware process models. We also illustrate the feasibility of coupling business process support systems with geographic information systems by means of an experimental case.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Throughout the past two decades, business process management (BPM) has emerged as one of the abiding systematic management approaches to align organizational business processes to the needs of clients [34]. BPM encompasses a broad scope, including the design, modeling, execution, monitoring and optimization of business processes — the so-called BPM life cycle [33]. The main driving rationale for BPM is that it enables organizations to be more efficient and more capable to react to changes. From this viewpoint, BPM regards processes as core strategic assets of an organization, which hence need to be understood, managed, and improved to increase the value added by products or services delivered to clients

The emergence of BPM has caused a shift in the realm of information systems and information technology from data-based information systems to process-aware ones, i.e. “Process-Aware Information Systems”, or PAIS. The support provided by PAIS — be it for the modeling, execution, validation or monitoring of business processes — is only able to capture and describe an idealized or simplified version of reality. Traditionally, most attention within the BPM community has been focused on studying control-flow aspects of business processes, i.e. the aspects governing the flow of business activities (i.e. the sequence in which activities can be performed). In recent years, however, integrating other perspectives and “contexts” within this view has received increased attention, as support systems which adopt a control-flowcentric view are unable to adequately capture human behavior due to lack of descriptions of possible constraints against activity modeling. Similarly, support systems focusing only on data aspects fail to capture the flow and sequence aspects of the data as it moves through a business process. As such, many scholars have shifted towards studying various approaches that integrate control-flow with other contexts. In this paradigm, processes can be rapidly changed and adapted to a new external data-governed context (e.g., location and weather). It is recognized that contextualizing processes in this manner allows for a more explicit consideration of the environmental setting of a process [30].

This paper contributes to the research field of BPM by focusing on the particular context of geospatial information, an aspect which is becoming more and more important in all information system related areas, given the increased usage of mobile devices and tracking as well as other recent developments such as the Internet of Things or sensorbased data gathering. We hence argue that taking this context into account in the various life cycle steps of BPM can contribute to improve the effectiveness and efficiency of process management. Especially in environments where a need arises to apply both process-aware and Geographic Information Systems (GIS), it is highly valuable to combine and integrate these two perspectives, instead of considering them in isolation [24]. The goal of this paper is thus to make the modeling and execution aspects of BPM “location-aware”. We do so by proposing business process modeling language based on a formal Petri net extension which incorporates location aspects and ways to constrain the execution of activities by location-based constraints. Next, we formalize the execution semantics of our extension by describing a unambiguous mapping to colored Petri nets. This also allows us to develop a prototype implementation of our approach using CPN Tools [17], with which a simulation extension was developed to support the execution and validation of models created using our approach and to illustrate the feasibility of coupling business process support systems with geographic information systems.

The remainder of this paper is structured as follows. Section 2 provides an overview of related work and preliminaries used throughout the paper. Section 3 outlines a running example which will be used to illustrate the developed artifacts. Section 4 introduces our proposed modeling language to design location-aware processes, after which Section 5 discusses the execution semantics of such models by means of a mapping to colored Petri nets. Section 6 discusses the developed implementation. Section 7 concludes the paper and provides outlines for future work.

## 2. Preliminaries

## 2.1. Related work

We regard location as one of the key variables in the wider context of a business process. In the layered process context model proposed by Rosemann et al. [30], location describes an important variable situated in the environmental context layer, which describes process-related variables that reside beyond the business network in which an organization is embedded, but still pose a contingency effect on the business processes. Scholars have argued that the inclusion of location contextual variables in business process management practices helps to improve dependency aspects (constraining activity executions based on location aspects, for instance) [10], increase the adaptability and flexibility of running processes (by reconfiguring and modifying models and tasks based on location aspects) [14,7,1,5], and improve the efficiency (performance and cost-effectiveness) of organizational processes [35]. Naturally, these concerns are of an even greater importance for processes where mobility (that is, tracking changes in locations and adapting processes to these changes) is deemed to be an important factor [19].

The notion of location-awareness centers around the basic idea that location and location-based services can be sensed and adapted to within processes. Location-aware business process management thus encompasses the ability for a business process to sense the current process status in a specific location and to be aware of the whole process situation. Based on this, process owners can react or dynamically change the process execution to adapt the goal of the process. Examples of location sensitive services and applications can be observed in areas such as navigation and travel, device and human tracking, geosocial networking, retail and real-estate services, mobile workforce deployment, and many others. However, works around the connection of location services with principles of business process management are relatively scarce in the literature. That is, many researchers focus on connecting spatialbased information with scientific workflows [23,2,15,31,3,22,18], but not with business-oriented workflows. As a notable exception, [21] discusses map metaphors that are used to visualize work items and resources in process-aware information systems (using the YAWL workflow language). This technique specifies that users could check geographical positions and distances based on a geographical map, but does not indicate how exactly geographical aspects can influence the flow of execution of the process. Decker et al. [10,11] have defined location constraints for individual workflow activities when modeling a workflow schema to restrict the location where an activity can be performed, but the location constraints lack comprehension and expressiveness. Our proposed modeling technique, on the other hand, is able to specify in an exact manner how location impacts the basic logical relationships in a process control-flow, i.e. sequence, parallel split/joins and exclusive choice split/joins.

Some existing BPM tool suites allow for the definition and capture of additional variables in the modeling of business processes [28,29,19,1]. In theory, such attribute fields could be used to capture location-based information. For instance, in business process model and notation (BPMN) models, locations could theoretically be modeled through the use of swimlanes, text annotations or data elements. In event-driven process chain (EPC) models, location variables may be grouped via organizational objects and in yet another workflow language (YAWL) models, static attributes could be attached to work items as additional text information. However, in all these approaches, location-based elements exist only as secondary constructs or text-based annotations for readers to understand the graphical diagram, and do not impact the semantics or execution of the modeled process in a direct way.

Our approach aims to make location-based constructs first-class citizens in the modeling and execution of process models: meaning that it is possible to govern the execution of a process based on location-based properties, and to signal changes to location properties based on the enactment of activities within a running business process.

## 2.2. Definitions and notations

This section outlines preliminary concepts and definitions which will be utilized in the remainder of the paper.

Petri nets are a well-known representational language to model concurrent system, and have also been extensively applied to formalize business process model semantics [25,27].

Definition 1. Petri net. A Petri net is a triple (P, T, F) [25,27] with:

– P is a finite set of places, $P { = } \{ p _ { 1 } , p _ { 2 } , { \ldots } , p _ { | P | } \} ;$

– T is a finite set of transitions, $T = \{ t _ { 1 } , t _ { 2 } , \dots , t _ { | T | } \}$ , with P∩T=∅;

$- \ F \subseteq ( P \times T ) \cup ( T \times P )$ is a finite set of directed arcs (flow relation).

A place (drawn as a circle, see for instance Fig. 1) p∈P is called an input/output place of a transition (drawn as a box and labeled; unlabeled transitions are shown as a black box) t∈T if there exists an arc from p to t or from t to p respectively. •t and t• denote the set of input and respectively output places for a transition t∈T. Similarly, •p and p• define the set of transitions having p∈P as an input place and the set of transitions having p∈P as an output place respectively.

Definition 2. Marking, marked Petri net. A marked Petri net is a triple $\left( N , M , M _ { 0 } \right)$ with:

– N=(P,T,F) a Petri net (a marked Petri net can also be written in an expanded notation $( P , T , F , M , M _ { 0 } ) )$ ;

– M : P→Nþ is a marking function;

$\mathbf { \Sigma } - \mathbf { \Sigma } M _ { 0 } : \mathbb { P } \mathrm { \to } \mathbb { N } _ { 0 } ^ { + }$ is the initial marking function.

Places p∈P in a Petri net can contain zero or more “tokens” (drawn as black dots inside the places). The distribution of tokens over the places defines the state, denoted as the “marking” of the Petri net, represented by the marking function M, which maps each p∈P to a natural, positive number, representing the amount of tokens contained in that place. The multiplicity of a place p in a marking M, i.e. M(p), denotes the number of tokens that this place contains. The initial marking $M _ { 0 }$ is used to initialize all places with an initial token count (in most cases, the initial marking is defined as follows: $M _ { 0 } : p \in P \mapsto 1 { \mathrm { ~ i f } } \bullet p =$ ∅or 0 otherwise).

Definition 3. Petri net execution semantics. The number of tokens in a Petri net changes during the execution of a Petri net. The marking of a Petri net defines a state, based on which execution semantics can be formalized as follows:

– A transition t∈T is said to be enabled under marking M iff each of its input places contains at least one token: $\forall p \in \bullet t : [ M ( p ) > 0 ] ;$

Please cite this article as: X. Zhu, et al., Enabling flexible location-aware business process modeling and execution, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.12.003

X. Zhu et al. / Decision Support Systems xxx (2015) xxx–xxx

![](/api/attachments/RAEAFM6N/fulltext/images/5a94aaf8c56e9cf4dd05c79c7e0ad5ebbcc290c623cc742594cbf1b567779afa.jpg)  
Fig. 1. WF-net model of the “repair” process used as a running example throughout the paper. In its basic form, the process model is unable to explicitly include location based concerns in its design nor the take them into account during its execution.

– An enabled transition t∈T can be fired, which brings the Petri net from one state to another:

$$
M _ {1} \xrightarrow {t} M _ {2} \text {so that} \forall p \in P: [ \left\{ \begin{array}{l l} M _ {2} (p) = M _ {1} (p) & \text {if} p \not \in \bullet t \cup t \bullet \\ M _ {2} (p) = M _ {1} (p) - 1 & \text {if} p \in \bullet t \\ M _ {2} (p) = M (p) + 1 & \text {if} p \in t \bullet \end{array} \right. ].
$$

Scholars modeling control-flow dimensions of a business process often utilize a subclass of Petri nets, called workflow nets (or, WF-nets) [32]. A WF-net specifies the behavior of a single process instance in isolation.

Definition 4. WF-net. A Petri net (P,T,F) is a WF-net [32] when:

– There is a single source place i∈P such that $\bullet i = \varnothing ;$

– There is a single sink place o∈P such that $o \bullet = \varnothing ;$

– The net $( P , T \cup \{ t ^ { \prime } \} , F \cup \{ ( o , t ^ { \prime } ) , ( t ^ { \prime } , i ) \} )$ is strongly connected, i.e. every x∈P∪T lies on a path from i to o.

To define the execution semantics of our Petri net modeling extension, we will provide a formalized mapping to colored Petri nets (CPNs). CPNs are an extension of Petri net which are comparable to Petri nets, but add color sets to places and tokens to allow for tokens of multiple types, guard transitions to constrain the execution of transitions and arc expression to govern input and output flow of tokens [16]. Normally, guards and arc expressions are formalized in a particular language (CPN Tools for instances uses Standard ML to do so, a functional programming language). The definition we provide below is adapted from [16], but defined in language-agnostic form, meaning that we assume the general availability of a language which allows to define expressions which can be evaluated and yield a result when done so.

Definition 5. Colored Petri net. A CPN is a tuple $( P , T , A , \Sigma , C , V , N , G , E , M , I )$ with:

– P the set of places, $P { = } \{ p _ { 1 } , p _ { 2 } , { \ldots } , p _ { | P | } \} ;$

– T the set of transitions, $T = \{ t _ { 1 } , t _ { 2 } , \dots , t _ { | T | } \} , P \cap T { = } \emptyset ;$

– A the set of arcs, $A = \{ a _ { 1 } , a _ { 2 } , \ldots , a _ { | A | } \} ;$

– Σ the set of color sets defined within the model. A color set is a grouping of colors. A color is an attached value (i.e., a label) to a token. Regular Petri nets can be expressed as a CPN by defining a single color set with a single color value;

– V the set of variables used in the model, $V { = } \{ \nu _ { 1 } , \nu _ { 2 } , \ldots , \nu _ { | V | } \}$ . Note that we indicate the actual value (i.e., color) of a variable v∈V as $\boldsymbol { \nu } ^ { * } ;$

$- \ C : P { \mathsf { U } } V { \mathsf { U } } A \to \Sigma$ the function returning the color set associated to a place, variable, or arc in the CPN model; for arcs, the color set of the place associated to the arc is returned, i.e. $C : a { \in } A \mapsto C ( P \cap N ( a ) )$

$- \ P { \mathrm { : } } A {  } P { \times } T \cup T { \times } P$ the node function mapping arcs to a placetransition or transition-place flow expression. This function allows for the definition of multiple arcs between the same placetransition or transition-place pair;

– G:t∈T↦GExpr the guard expression function mapping a transition t∈T to a boolean expression GExpr, denoting whether the transition is permitted to fire. Evaluating this expression yields a boolean result value, indicated as $G E x p r ^ { * } \in \{ t r u e , f a l s e \}$ ;

– E:a∈A↦AExpr the arc expression function mapping an arc a∈A to an expression AExpr. Evaluating an arc expression yields a multiset of tokens, indicated as $A A E x p r _ { M S } $ which is to be produced (for transition to place arcs) or consumed (for place to transition arcs). The expression itself can use one or multiple variables in V, the color sets of the input and outputs of the arc expression must correspond to the color sets of the places the arcs connect to, formalized, the following holds: $\forall a \in A : [ \exists \sigma \in \Sigma : [ \forall \tau \in E ( A ) _ { M S } { ^ { * } } : [ \tau \in \sigma ] \land C ( P \cap N ( a ) ) =$ σ]];

$M { : p \in { P } { \mapsto } } C ( p ) _ { M S }$ the marking function, returning the multiset of tokens contained in a place with $\forall p { \in } P ; [ \forall \tau { \in } M ( p ) ; [ \tau { \in } C ( p ) ] ]$ ;

– I:p∈P↦IExpr the initialization function, this function initializes places in the model with a state, expressed as colored tokens. The evaluation of an IExpr yields a token multiset, indicated as $I E x p r _ { M S } ^ { * } \mathsf { w i t h }$ $\forall p { \in } P ; [ \forall \tau { \in } I E x p r _ { M \dot { S } } ^ { * } [ \tau { \in } C ( p ) ] ]$ .

The execution semantics of a CPN differ from those of a regular Petri net.

Definition 6. Colored Petri net execution semantics. Let $p { : } A \to P$ be a function returning the place attached to an arc and $t { \because } A {  } T { \sf a }$ function returning the transition attached to an arc, i.e. $t { \mathrel { : } } a { \in } A { \mapsto } T { \cap } N ( a )$ . For a transition t∈T to be enabled, the following criteria need to hold:

– All expressions of the incoming arcs should be satisfied: $\forall a \in A , t ( a ) = t \colon [ E ( a ) _ { M S } ^ { * } \neq \emptyset ] ;$

– The guard condition of the transition must evaluate to true, $G ( t ) ^ { * } =$ true.

Enabled transitions can be fired. Output and input places are updated accordingly given the input and output arc expressions. Firing an enabled transition brings a marking $M _ { 1 } \to ^ { t } M _ { 2 }$ as follows. Let $A _ { t } ^ { I } { = } \{ a { \in } A | N ( a ) { = }$ $( x , y ) \land y = t \} ; A _ { t } ^ { o } = \{ a \in A | N ( a ) = ( x , y ) \land x = t \}$ and $A _ { t } { = } A _ { t } ^ { I } { \cup } A _ { t } ^ { O }$ , then $\forall p \in P : [ M _ { 2 } ( p ) = M _ { 1 } ( p ) \uplus \{ \tau \in E ( a ) _ { M S } ^ { * } | a \in A _ { t } ^ { O } \land p ( a ) = p \} \backslash \{ \tau \in E ( a ) _ { M S } ^ { * } | a \in A _ { t } ^ { O } \land p ( a ) = p \} ] .$ $A _ { t } ^ { I } \wedge p ( a ) = p \} ]$

Next, we shift our attention to the formalization of locations. The definition of our concept of location corresponds with a so called “feature” as applied by most geographic information systems. A feature describes something that can be drawn on a map, i.e. something in the real world — a mountain, landmark or even moving objects such as cars. Additionally, it is reasonable to group certain features together if they share a number of properties. For example, China, Belgium and Germany can all be regarded as features of the type $\ " \mathrm { C o u n t r y } "$ . In addition, apart from a semantic description (a name and other properties), features can also be represented in physical terms, i.e. as a mathematical expression of an object's geometry in terms of points, lines, paths (multiple line segments) or polygons (associated with a well-defined coordinate reference system and scale or granularity).

Definition 7. Feature, feature type. Our definition of location corresponds with a so called “feature”. Features are defined in terms of a geometry, a feature type, and an arbitrary number of additional attributes (such as a human-readable name), i.e.:

– Let $F T _ { L }$ be a set of feature $\mathrm { t y p e s , } F T _ { L } { = } \{ f t _ { 1 } , f t _ { 2 } , \dots , f t _ { | F T | } \} ;$

– Let $F _ { L }$ be a set of features, $F _ { L } = \{ f _ { 1 } , f _ { 2 } , \dots , f _ { | L | } \} ;$

$\mathrm { L e t } T y p e \colon F _ { L }  F T _ { L }$ be a function mapping features to a type. In the visual modeling notation (e.g. in Fig. 2 later below), we will also denote this using the shorthand f:ft with $f \in F _ { L }$ and ft∈FT ;

Please cite this article as: X. Zhu, et al., Enabling flexible location-aware business process modeling and execution, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.12.003

X. Zhu et al. / Decision Support Systems xxx (2015) xxx–xxx

![](/api/attachments/RAEAFM6N/fulltext/images/6effae5df728810896614dd020f67cd43775307a26e8e64f83cf873e7063c201.jpg)  
Fig. 2. The running example of Fig. 1 remodeled using our location-aware approach. Location dependent transitions are shown with a flag, while location constraints are modeled as shaded boxes.

– Let Geometry: $f \in F _ { L } | \to g \hat { \mathbf { \mathfrak { c } } }$ function which returns the geometry g for a given feature $f \in F _ { L } ;$

– Let f<sup>a</sup> indicate some attribute a associated with a feature f∈F . This can be any type of data, e.g. a name, a date, a number or even other features.

Many standards and vendor implementations exist to define geometry types [26,20,8,9]. In our implementation, we define a geometry g to be one of the following types, but this can be extended or modified based on end-user needs:

• A “point”, a single coordinate: $( x \in \mathbb { R } , y \in \mathbb { R } )$

• A set of points, a “multipoint”: $\{ ( x _ { 1 } \in \mathbb { R } , y _ { 1 } \in \mathbb { R } ) , \ldots , ( x _ { n } \in \mathbb { R } , y _ { n } \in \mathbb { R } ) \}$

• A “linestring”, a sequence of points connected by line segments (note that linestrings can form a closed loop or not): $( ( x _ { 1 } \in \mathbb { R } , y _ { 1 } \in \mathbb { R } ) , \dots , ( x _ { n } \in \mathbb { R } , y _ { n } \in \mathbb { R } ) )$

• A set of linestrings, a “multilinestring”

• A “polygon”, defined by an closed outer boundary (described as a linestring) and zero or more closed inner boundaries:

• A set of polygons, a “multipolygon”.

Finally, we define the concept of a geospatial relationship. By establishing relationships over geometries, we are able to answer queries such as “Is one feature contained in another?” In some cases, geospatial relationships are categorized in separate sets, such as topological, measurement, sequential or complex relationships [36,35], but for the sake of simplicity, we define a “geospatial relationship” here by means of a single, global moniker as follows:

Definition 8. Geospatial relationship. A geospatial relationship is a function of the general form Relationship(fg[ $f g _ { 1 } , \ldots , f g _ { n } ] [ , a _ { 1 } , \ldots , a _ { n } ] )$ with:

– fg: the geometry used as the main function argument. If a feature is passed in $( { \mathrm { i } } . { \mathrm { e } } . f g { \in } F _ { L } )$ , the function is simply applied on Geometry(fg), the geometry of the feature;

$f g _ { 1 } , \ldots , f g _ { n } { \mathrm { : } }$ additional geometry or feature arguments (optional). Just as with fg, if a feature is passed in, the function is applied on the geometry of the feature;

$a _ { 1 } , \ldots , a _ { n } { \mathrm { : } }$ additional arguments of any type other than features or geometry (optional);

Please cite this article as: X. Zhu, et al., Enabling flexible location-aware business process modeling and execution, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.12.003

Table 1  
Geospatial relationships considered in our approach. We apply these relationships as building blocks towards the construction of location constraints, as will be illustrated later.

<table><tr><td>Relation</td><td>Return type</td><td>Description</td></tr><tr><td>Centroid(fg)</td><td>Point</td><td>Returns the geometric center of a geometry fg.</td></tr><tr><td>Length(fg)</td><td>Length (m)</td><td>Returns the length of the geometry fg if it is a linestring or multilinestring.</td></tr><tr><td>Area(fg)</td><td>Area ( $m^2$ )</td><td>Returns the area of the geometry fg if it is a polygon or a multipolygon.</td></tr><tr><td>Perimeter(fg)</td><td>Length (m)</td><td>Return the length measurement of the boundary of fg if it is a polygon or multipolygon.</td></tr><tr><td>ClosestPoint(fg,fg1)</td><td>Point</td><td>Return closest point on or in fg1 that is closest to fg.</td></tr><tr><td>Distance(fg,fg1)</td><td>Length (m)</td><td>Returns the cartesian minimum distance between fg and fg1.</td></tr><tr><td>Equals(fg,fg1)</td><td>{true,false}</td><td>Returns true if the given geometries fg and fg1 represent the same geometry.</td></tr><tr><td>Disjoint(fg,fg1)</td><td>{true,false}</td><td>Returns true if the given geometries fg and fg1 have no points in common.</td></tr><tr><td>Intersects(fg,fg1)</td><td>{true,false}</td><td>Returns true if the given geometries fg and fg1 have at least one point in common.</td></tr><tr><td>Touches(fg,fg1)</td><td>{true,false}</td><td>Returns true if the given geometries fg and fg1 only touch edges and do not overlap in any way.</td></tr><tr><td>Crosses(fg,fg1)</td><td>{true,false}</td><td>Returns true if the given geometries fg and fg1 touches and overlap edges.</td></tr><tr><td>Within(fg,fg1)</td><td>{true,false}</td><td>Returns true if the given geometry fg1 is completely within fg (no touching edges).</td></tr><tr><td>Contains(fg,fg1)</td><td>{true,false}</td><td>Returns true if the given geometry fg contains fg1.</td></tr><tr><td>Overlaps(fg,fg1)</td><td>{true,false}</td><td>Returns true if the given geometries fg and fg1 have points in common but not all points in common.</td></tr><tr><td>Buffer(fg,fg1,a1)</td><td>Polygon</td><td>Returns a polygon geometry that represents all points whose distance from fg is less than or equal to distance a1.</td></tr><tr><td>ShortestRoute(fg,fg1)</td><td>Linestring</td><td>Returns a linestring geometry representing the shortest route from fg to fg1 based on routing topology.</td></tr></table>

– a return type which can be of any type, e.g. another feature, geometry, binary value, number or invariant.

Again, many definitions exist that catalog geospatial relationships. ISO19107 for instance defines a topological model based on the “geography markup language” [20], whereas other sources, such as the IntesaGIS project [4] base themselves on an authority database. Many of the most widely used GIS toolkits, i.e. GeoTools, PostGIS, ArcGIS, SQL Server etc. define geospatial relationships in accordance with the “Topic 8” standard proposed by the OpenGIS Consortium (OGC) [26]. In [6], a UML-based metamodel is proposed based on the same standard. In most cases, however, all standards include relations to describe the basic topologic geospatial relations between two geometries as described by de DE-9IM standard [8,9,12,13].

Table 1 provides a listing of all the geospatial relationships we consider in the remainder of our work and were also implemented in the developed prototype, described below, based on the DE-9IM, OGC Topic 8 and ISO19107 standards. These will be used as building blocks towards the construction of location constraints, as will be illustrated later.

## 3. Running example

To illustrate our location-aware modeling approach and its execution semantics, we will utilize a running example throughout this paper, extending an example provided in [11]. Looping and parallel behavior was added to show how our approach can be applied on more complex control-flow constructs. The basic process model (no location-awareness) is depicted as a WF-net in Fig. 1. The example process describes a technical maintenance service, which is executed as follows. The process is started once a customer call is received (receive customer call, RCC) and handled in a particular call center (accept customer call, ACC). The call center evaluates the complaint of the customer, based on which the user is remotely assisted for trivial problems (remote assist, RAS), or an inspector is dispatched from the call center to the customer's location to investigate the problem onsite (dispatch, DIS). Based on the results of the investigation (on-site inspection, OSI), the inspector can solve the problem while investigating (no repair required, NRR), or calls-in a mobile repair team to perform on-site repair work (call repair team, CRT and on-site work, OSW). If the repair cannot be performed on-site (e.g. due to some broken components), the repair team heads to a repair shop to perform repairs there (shop-floor repair, SFR), before returning to the customer and continuing the on-site work (this cycle can occur multiple times before the problem is fixed). After finishing the work, both repair team and inspector are released and sent back (release repair team, RRT and release inspector, RIN). Next, in case an inspector was sent out, they need to write up a report at the call center (write report, WRE). In case a repair was performed, a follow-up check is required as well (perform followup check, PFC). Finally, independent of the nature of the solution offered, some administrative follow-up work (Follow-up Administration, FUA) needs to be performed to close the case.

The description of this simple process highlights many locational aspects which cannot be captured by control-flow alone (see Fig. 1). In particular, we list the following locational concerns which the process needs to adhere to:

– Call centers may only handle customer calls when the customer is located within the region a call center is responsible for;

– Inspectors can only be dispatched when they are available, and only when their “home base” call center matches the call center that handles the customer call;

– Inspectors can only write their report when they are at their call center;

– Requests can only be made to repair teams which are located in the customer's region or 50 km around it. Naturally, a repair team which is already working for another customer cannot be requested;

– The same holds for repair teams performing a follow-up check, but a repair team different from the original one needs to perform the check

– Shop-floor repairs should be made in the repair station closest to the customer's location; this should be based on navigational routing information;

– The call center performing the follow-up work should be situated in a different region then the call center handling the customer call.

## 4. Location-aware process modeling

This section discusses our proposed modeling approach to model location-aware processes. Our methodology is based on an extension of Petri nets, incorporating two new constructs, namely location dependent transitions and location constraints.

Fig. 2 shows the running example modeled using our location-aware extension. Using this modeling method, transitions can be made location dependent (indicated visually with a flag, ), which means that a feature, belonging to a specified feature type, will be bound to the transition after executing. Modelers are free to decide which transitions should be made location dependent, but in general, the follow guidelines hold:

– Transitions which involve a location that should be bound by constraints should be made location dependent, so as to define location constraints over them.

– Transitions which involve a location that will be used in a following activity (i.e. to constrain it) should be made location dependent.

– Transitions of which their execution involves a change in the properties of a geospatial construct should be made location dependent, so as to track their bound feature.

Next, the shaded boxes in Fig. 2 represent location constraints, used to constrain the locations which can be bound to a location dependent transition, or to constrain the execution of non-location dependent transitions based on previously bound locations, without binding a location to those transitions themselves. Visually, the constraints are connected (using dashed arcs) with all the transitions of which their bound location will be used as an input in the constraint, and with the one transition which is bounded by the constraint.

The following definitions formalize the constructs of location dependent transitions and location constraints.

Definition 9. Location-aware WF-net (LAWF-net). A location-aware WF-net (LAWF-net) is represented as a tuple $( P , T , F , F _ { L } , F T _ { L } , T _ { L } , C _ { L } , C F _ { L } )$ with:

– P, T and F unchanged with regard to the definition of a WF-net (places, transitions and flows);

– $F _ { L }$ and $F T _ { L }$ the sets of features and their type (see Section 2.2);

$T _ { L } \subseteq T$ the set of location dependent transitions (shown visually with a flag and $1 f { : } f t$ label with $f \in F _ { L }$ and $f t { \in } F T _ { L } )$

$C _ { L }$ the set of location constraints (a set of expressions, shown visually as a shaded box);

$\mathbf { \Sigma } - \mathbf { \Sigma } C F _ { L } { \boldsymbol { \Sigma } } \left( T _ { L } { \times } C _ { L } \right) \cup ( C _ { L } { \times } T )$ a finite set of directed arcs linking location dependent transitions to a constraint (shown visually as a dotted arc).

We also overload the function Type: $T _ { L }  F T _ { L }$ introduced in Definition 7 to return the feature type for a location dependent transition and the function $M _ { L } { : } T _ { L } {  } F$ to get the feature bound to a particular location dependent transition (the “location marking”) so that $\forall t { \in } T _ { L } \colon [ T y p e ( M _ { L } ( t ) ) =$ $T y p e ( t ) \vee M _ { L } ( t ) = \emptyset ]$ . Initially, that is before execution of any transition, no locations are bound, i.e. $\forall t \in T _ { L } \colon [ M _ { L } ( t ) = \emptyset ]$

Definition 10. Location constraint. A location constraint is an expression $c \in C _ { L }$ so that:

– The constraint expression c evaluates to a boolean result, depicted as $c ^ { * } \in \{ t r u e , f a l s e \} ;$

– The constraint expression c involves exactly one output transition, i.e. $\forall c \in C _ { L } \colon [ \exists ! ( x , y ) \in C F _ { L } \colon [ x = c \land y \in T ] ] . \ C _ { L } ^ { t } = \{ c \in C _ { L } | ( c , t ) \in C F _ { L } \}$ is used as a shorthand to return all constraints defined on t∈T;

– The constraint expression c can involve zero or more location dependent input transitions $t _ { i } ^ { i n p u t } { \in } T _ { L }$ . The feature bound to such input transitions, given by $M _ { L } ( t _ { i } ^ { i n p u t } )$ will be used as an input for the expression at the time of evaluation. Note that it is possible, in theory, to use a location dependent transition as an input for the same transition.

Note that location constraints can be formulated directly in the form of a geospatial relationship (when the relationship returns a boolean result), though Fig. 2 contains one additional constraint of the form IsShortestRoute which is defined as follows: IsShortestRoute $: f g \in F _ { L } \times f g _ { 1 } \in F _ { L } \mapsto$ Length ShortestRoute fg; $f g _ { 1 } ) = f g _ { 2 } ^ { \mathrm { m i n } } F _ { L } |$ Length ShortestRoute fg; $f g _ { 2 } )$ :, i.e. this constraint return true when feature fg is the feature which lies on the shortest path to fg for all features of its type Type(fg ). Naturally, one can also define a similar constraint for the shortest cartesian distance, IsShortestDistance IsShortestDistance $\begin{array}{c} f g { \in } F _ { L } \times f g _ { 1 } { \in } F _ { L } { \mapsto } D i s t a n c e ( f g , f g _ { 1 } ) = \qquad { \mathrm { ~ f } } g _ { 2 } { \in } F _ { L } |  \\ { T y p e ( f g _ { 2 } ) = T y p e ( f g _ { 1 } ) } \end{array}$ Distance fg; Distance(fg $f g _ { 2 } )$

Fig. 2 also merges location constraints pertaining to the same output transition as a conjunction (∧) to keep the figure readable, but modelers are free to split these up into multiple, separate location constraints. To provide an additional example, in Fig. 2, the constraint $" C o n t a i n s ( c u s ^ { r e g i o n } , c a c ) "$ contains one output transition (ACC) and one input transition (RCC). Instead of using the full transition labels in the expression (i.e., writing $" M _ { L } ( R C C ) " )$ , we use a short name $( " c u s "$ or $" c a c " )$ as a way to indicate bound features for location dependent transitions directly. As we have defined a feature type for each location dependent transition, this means that, even when no constraints are modeled, an intrinsic $" T y p e ( M _ { L } ( t ) ) = T y p e ( t ) "$ constraint is present for any $t \in T _ { L } .$

Although the primary goal of LAWF-net is to provide a comprehensible modeling language, it is possible to define execution semantics, similar to those of a normal Petri net. That is, a transition $t \in T$ is enabled in a LAWF-net under a marking (M,M ) when: the control-flow properties for being enabled are satisfied (i.e. a token in all input places) and when all location constraints $c \in C _ { L } ^ { t }$ are satisfied. Note that evaluating the location constraints differs for location dependent and nonlocation dependent transitions. For a non-location dependent transition t∈ $T \backslash T _ { L }$ the constraints are satisfied iff $\forall c \in C _ { L } ^ { t } { : } [ c ^ { * } = t r u e ]$ . For a location dependent transition $t \in T _ { L }$ the constraints are satisfied iff there exists at least one candidate feature $f ^ { c a n }$ which can be bound to the transition, so that $T y p e ( f ^ { c a n } ) = T y p e ( t ) \land \forall c \in C _ { L } ^ { t } \colon [ c _ { M _ { L } ^ { c a n } } ^ { * } = t r u e ]$ . When evaluating candidate features, however, it is important to remark that the currently bound feature to the transition at hand reflects the previous (or unset, empty) feature, whereas the evaluation of the constraints requires a location marking where the candidate feature is bound to the location dependent transition. To solve this, every candidate feature is evaluated under a candidate location marking $M L ^ { c a n }$ where the candidate feature is bound to the transition under evaluation. Finally, the actual execution of a location dependent transition causes a normal token movement $M _ { 1 }  M _ { 2 }$ (see before) and additionally brings the location marking in a new state $M _ { L , 1 } $ $M _ { L , 2 }$ such that $\forall t ^ { \prime } \in T _ { L } \colon [ M _ { L , 2 } ( t ^ { \prime } ) = f ^ { s e l e c t e d } \mathrm { i f } t ^ { \prime } = t \mathrm { o r } M _ { L , 1 } ( t ^ { \prime } )$ otherwise] with $f ^ { s e l e c t e d }$ a satisfiable feature chosen to be bound to the fired location dependent transition.

## 5. Executing location-aware process models

Our LAWF-net modeling extension provides a straightforward and understandable means to merge location aspects with control-flow concerns. Although we have provided execution semantics in the section above in accordance with those of a WF-net, we also define a mapping from LAWF-nets to CPN models, driven by the following reasons. First, as we will see later, mapping LAWF-nets to CPN models enables to use existing tools to drive the execution of location-aware processes. Second, as we will show below, this also allows for easier integration with existing GIS platforms. Third, by providing an approach which is fully compatible with CPN, we can apply the existing body of work concerning validation of such models, both at run-time, i.e. ensuring the process runs as designed and constraints are being enforced during execution as discussed above, but also at design-time, by performing behavioral soundness checks which investigate whether a model is sound based on a number of conditions. For instance, a model is sound if it does not allow “deadlocks” to occur: states in which it is not possible anymore to finish a running case. Finally, formulating location-aware process models in terms of CPN models also allows for more straightforward integration with other contexts, i.e. timing or social (organizational) aspects.

The following definitions provides the formalization of the mapping from LAWF-nets to CPN.

Definition 11. LAWF-net to CPN mapping. A LAWF-net $( P ^ { L } , T ^ { L } , F ^ { L } , F _ { L } ^ { L } , F T _ { L } ^ { L } , T _ { L } ^ { L } , C _ { L } ^ { L } , C F _ { L } ^ { L } )$ is mapped to a CPN model $( P , T , A , \Sigma , C ,$ $V , N , G , E , M , I )$ as follows:

$- \ \Sigma = \{ U , F _ { L } ^ { L } \}$ with $U { = } \{ u n i t \}$ the color set containing one control-flow oriented color and $F _ { L } ^ { L }$ the set of features, which also acts as a color set (color sets);

Please cite this article as: X. Zhu, et al., Enabling flexible location-aware business process modeling and execution, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.12.003

X. Zhu et al. / Decision Support Systems xxx (2015) xxx–xxx

![](/api/attachments/RAEAFM6N/fulltext/images/19c7f152f926e040ff000cb068e6c2b6ca72492994667e96520b1bdbf4710282.jpg)  
Fig. 3. LAWF-net of Fig. 2 converted to a CPN model, running in tandem with a GIS system. The GIS system is able to impose geospatial constraints restricting the control-flow of the process and execution of activities can impose effects on features in the GIS system, displayed here through a map window superimposed over the model. Note that it is possible to directly model location-aware business processes as a CPN model, although the proposed LAWF-nets offer a better understandable and maintainable means to do ${ \sf S } 0 - { \sf a } { \sf S }$ evidenced by the complexity of the CPN model above.

– Each transition and place in the LAWF-net is also a transition in the CPN model: $\forall p \in P ^ { L } : [ p \in P ]$ with $C ( p ) { = } U . I ( p ) { = } \{ u n i t \} \mathrm { i f } { \cdot } p { = } \emptyset$ or ∅ otherwise and $\forall t \in T ^ { L } : [ t \in T ]$ (control-flow places and transitions); – For each location dependent transition in the LAWF-net, a location output place is created in the CPN model: $\forall t \in T _ { L } ^ { L } \colon [ p _ { L } ^ { t } \in P ]$ with $C ( p _ { L } ^ { t } ) = F _ { L } ^ { L }$ and $I ( p _ { L } ^ { t } ) = \emptyset$ (the places in the bottom row in Fig. 3) (location output places);

– For each feature type in the LAWF-net a location input place is created in the CPN model: $\forall f t \in F T _ { L } ^ { L } \colon [ p _ { L } ^ { f t } \in P ]$ with $C ( p _ { L } ^ { f t } ) = F _ { L } ^ { L }$ and $I ( p _ { L } ^ { f t } ) =$ $\{ f \in F _ { L } ^ { L } | T y p e ( f ) = f t \}$ (the places in the top row in Fig. 3) (location input places);

– All control-flow of the LAWF-net is also represented in the CPN model: $\forall ( x , y ) \in F ^ { L } : [ a _ { ( x , y ) } \in A ]$ with $N ( a _ { ( x , y ) } ) = ( x , y )$ and $E ( a _ { ( x , y ) } ) =$ unit (control-flow);

– A binding and overriding variable are created in the CPN model, used to bind a location to a location dependent transition and to override a previously bound transition respectively: $\boldsymbol { v _ { L } } \in \boldsymbol { V }$ with $C ( \nu _ { L } ) = F _ { L } ^ { L }$ and $v _ { O } \in V$ with $C ( \nu _ { O } ) = F _ { L } ^ { L }$ (binding and overriding variable);

– For each location dependent transition, four arcs are added: one bringing the feature from the input place to the transition, one bringing the feature to the output place, a return arc returning the feature to the input place, and an override arc to remove previously bound features present in the output place: $\forall t \in T ^ { L } \colon \mathsf { \hat { [ } } a _ { t } ^ { i n p u t } , a _ { t } ^ { r e \mathsf { \bar { t } } u r n } , a _ { t } ^ { o u t p u t } , a _ { t } ^ { o v e r r i d \hat { e } } \in A ]$ with $N ( a _ { t } ^ { i n p u t } ) =$ $( p _ { L } ^ { T y p e ( t ) } , t ) , N ( a _ { t } ^ { r e \bar { t } u m } ) = ( t , p _ { L } ^ { T y p e ( t ) } ) , N ( a _ { t } ^ { o u t p u t } ) = ( t , p _ { L } ^ { \bar { t } } )$ and $N ( a _ { t } ^ { o v e r r i d e } ) =$ $( p _ { L } ^ { t } , t ) . ~ E ( a _ { t } ^ { i n p u t } ) { = } E ( a _ { t } ^ { r e t u r n } ) { = } E ( a _ { t } ^ { o u t p u t } ) { = } \{ \nu _ { L } \}$ and $E ( a _ { t } ^ { o v e r r i d e } ) =$ ∅ if $M ( p _ { L } ^ { t } ) = \emptyset$ or M(p<sup>t</sup>) otherwise (this arc consumes the feature token from the output place if it is present) (input, output, return and override arcs);

– For each location dependent transition, the guard expression in the CPN model is defined as a conjunction of all the location constraints in the LAWF-net with this transition as the output: $\forall t \in T ^ { L } \colon [ G ( t ) =$ $\land _ { c \in C _ { I } ^ { u } } ( c ) ]$ (guards);

– For location constraints involving input transitions, a variable is defined as well as two arcs to move the feature from the respective output place to the constrained transition and move it back after firing the constrained transition: $\forall t \in T ^ { L } : [ \forall c \in C _ { L } ^ { L ^ { t } } : [ \forall ( x , y ) \in \{ ( x , y ) \in C F _ { L } ^ { L } |$ $x { \in } T _ { L } ^ { L } { \wedge } y { = } c \} : [ \nu _ { L } ^ { ( x , y ) } { \in } V , a _ { i } { } ^ { ( x , y ) } , a _ { 0 } { } ^ { ( x , y ) } { \in } A ] ] ]$ with $C ( \nu _ { L } { } ^ { ( x , y ) } ) = F _ { L } ^ { L }$ and with $N ( { a } _ { i } ^ { ( x , y ) } ) = ( p _ { L } ^ { x } , t )$ and $N ( a _ { o } ^ { ( x , y ) } ) = ( t , p _ { L } ^ { x } )$ . The expressions read: ${ E ( a _ { i } { } ^ { ( x , y ) } ) = E ( a _ { o } ^ { ( x , y ) } ) = \{ \nu _ { L } { } ^ { ( x , y ) } \} }$ (constraint input arcs).

Fig. 3 shows the result of the conversion of a LAWF-net to a CPN model. Note that it is possible to directly model location-aware business processes as a CPN model, although the proposed LAWF-nets clearly offer a better understandable and maintainable means to do so, while still offering execution and validation support by means of the mapping outlined above.

## 6. Implementation and system integration

The converted running example shown in Fig. 3 was implemented as a CPN model using the well-known CPN Tools program [17]. Due to some limitations of this tool, the CPN model in Fig. 3 contains some additional constructs which are not part of the formalization. First, the addition of “dummy” unlabeled transitions before some location dependent transitions. For CRT, for instance, this is necessary due to the fact that repair teams might take some time to be in the vicinity of the customer's site. However, CPN Tools only performs a check for transition enabling immediately after a marking change. The added unlabeled transitions can be used to refresh the marking (which is not actually changed in terms of token distribution) and force CPN Tools to perform the enabling check again. Second, as stated above, the execution of location dependent transitions might trigger events to be handled by an external system. The same reasoning holds for the assignment of features. Hence, we can add an arc expression to output arcs $a _ { t } ^ { o u t }$ for any $t \in T ^ { L }$ which still returns a multiset of tokens equal to $\boldsymbol { v } _ { L } ,$ but also triggers external events. This might be useful for logging purposes, or to dispatch updates to an underlying GIS system, for example to send a repair team on its way. Third, as it is not possible to formulate the expression for the $a _ { t } ^ { o \nu e r r i d e }$ arcs directly using CPN Tools, we instead initialize each location output place with a dummy (empty) placeholder, and add constraints to prevent this dummy feature to be used as an input for any transition using this feature as an input (we also explicitly perform a feature type check in the guard of each location dependent transition, but this is just for the sake of clarity).

Possibilities exist to extend a converted CPN model in a number of ways. If so desired, modelers might opt to use one global location input pool place instead of creating an input place per feature type (or group multiple input places). Such system would make it possible for instance to allow more than one feature type to become bound to location dependent transitions (the possible types can still be restricted by adding a constraint). Secondly, end users might opt to remove overriding a<sub>t</sub><sup>override</sup> arcs for some location dependent transition, for example to keep track of multiple bound transitions in the case of recurrent transitions. Finally, modelers might also desire for location dependent (or any) transitions to output additional features apart from the one being bound to the location dependent transition. This can also easily be achieved by adding more output places and formulating appropriate arc expressions.

Finally, the question remains how the various geospatial relationships were implemented in the CPN model. To do so, a simulation extension was developed using CPN Tools' RPC (remote procedure call) functionality. The reason this approach was chosen instead of using the built-in Standard ML language is twofold. First, both practitioners and academics are more familiar with Java (the language of the simulation extension) than Standard ML, allowing for easier understanding and extensibility. Second, this approach allows to easily integrate location-aware business process models with existing GIS systems, both for evaluating the geospatial relationships (constraining and driving the process) and to react to activities as they are being executed (within the GIS system). To illustrate this, we have created an experimental set-up using the GeoTools Java package,<sup>1</sup> which provides support for all geospatial relationships listed before.

Fig. 3 also 321 CPN Tools. The map was constructed using real-life shapefiles which were imported in the set-up. The GIS system is able to impose geospatial constraints restricting the control-flow of the process (some activities can only be started once the repair team is on-site, for instance), and execution of transitions in the process also drives changes in the GIS system, e.g. sending out a request to a repair team causes this repair team to head to the customer's location using the shortest route available (as is shown in the figure). This illustrates the feasibility and validity of our proposed methodology.<sup>2</sup>

## 7. Conclusions

For the most part, the modeling and execution of business process models has so far been confined to a rather limiting environment, focusing mainly on control-flow aspects only, without taking rich contextual aspects into account. In this paper, we have focused our attention towards making the modeling and execution of business processes location-aware, focusing on the particular context of geospatial information. A Petri net modeling extension was proposed which incorporates location aspects and ways to constrain the execution of activities based on location constraints. This approach was formalized by means of a formalized mapping to colored Petri nets and implemented in combination with an experimental GIS setup to illustrate the feasibility of coupling business process support systems with geographic information systems.

We believe our contribution to be a valuable step towards incorporating location aspects in business processes, with application areas in logistics, transportation and many others. Indeed, the ability to make processes flexible and adaptive in terms of their ability to react to road, traffic or weather conditions is put forward as a promising area of study. Regarding future work, we plan to set up a number of case studies and to further enable the application of our approach in reallife contexts. To do so, we aim to develop a visual modeling tool which allows for the design and execution of LAWF-nets, while providing information regarding potential design problems (by performing the mapping to CPN models in the background). Additionally, the tool should allow to supply domain-specific knowledge (definition of features, maps, etc.) in a user-friendly manner. Next, concerning modularity, it is worthwhile to investigate how the integration with GIS systems other than the one applied in this work can be facilitated. Finally, we

<sup>2</sup> Source code of the developed implementation together with additional documentation regarding the architecture can be found at: http://processmining be/locationaware

also plan to expand on our methodology, both by investigating more location-based patterns that play a role in business process environments (the focus here was mainly on geospatial constraints) and how these aspects can be combined with other contextual aspects other than geographic information as well.

## Acknowledgments

This work is supported by the National Key Technology R&D Program, China (grant 2012BAH01F02), the KU Leuven Research Council (grant OT/10/010) and the Flemish Research Council (Odysseus grant B.0915.09).

## References

[1] S. Ali, T. Torabi, H. Ali, Location aware business process deployment, Computational Science and Its Applications — ICCSA 2006, Int'l Conference, Glasgow, UK, May 8–11 2006, Proceedings, Part IV. Vol. 3983 of Lecture Notes in Computer Science. Springer 2006, pp. 217–225.

[2] G. Alonso, C. Hagen, Geo-opera: workflow concepts for spatial processes, Advances in Spatial Databases. Vol. 1262 of LNCS 1997, pp. 238–258.

[3] I. Altintas, C. Berkley, E. Jaeger, M. Jones, B. Ludascher, S. Mock, Kepler: an extensible system for design and execution of scientific workflows. In: Scientific and Statistical Database Management, 2004, Proceedings. 16th Int'l Conference on Jun 2004, pp. 423–424.

[4] G. Amadio, C. Cannafoglia, M. Corongiu, M. Desideri, M. Rossi, Intesagis: the basis for a national spatial data infrastructure, roceedings of the 10th EC-GI&GIS Workshop, Poland, Warsaw, 2004.

[5] N. Aoumeur, J.L. Fiadeiro, C. Oliveira, Towards an architectural approach to locationaware business processes, 13th IEEE Int'l Workshops on Enabling Technologies (WETICE 2004), Infrastructure for Collaborative Enterprises, 14–16 June 2004, Modena, Italy. IEEE Computer Society 2004, pp. 147–152.

[6] J. Brodeur, Y. Bédard, M.-J. Proulx, Modelling geospatial application databases using uml-based repositories aligned with international standards in geomatics, Proceedings of the 8th ACM Int'l Symposium on Advances in Geographic Information Sys tems. GIS'00 2000, pp. 39–46.

[7] D. Chakraborty, H. Lei, Pervasive enablement of business processes, Proceedings of the 2nd IEEE Int'l Conference on Pervasive Computing and Communications (PerCom 2004), 14–17 March 2004, Orlando, FL, USA. IEEE Computer Society 2004, pp. 87–100.

[8] E. Clementini, P.D. Felice, P. van Oosterom, A small set of formal topological relationships suitable for end-user interaction, SSD. Vol. 692 of Lecture Notes in Computer Science, Springer 1993 pp. 277–295

[9] E. Clementini, J. Sharma, M.J. Egenhofer, Modelling topological spatial relations: strategies for query processing, Computers and Graphics 18 (6) (1994) 815–822.

[10] M. Decker, Modelling location-aware access control constraints for mobile workflows with uml activity diagrams UBICOMM'09 Oct 2009 pp. 263–268.

[11] M. Decker, H. Che, A. Oberweis, P. Sturzel, M. Vogel, Modeling mobile workflows with bpmn, Mobile Business and 2010 9th Global Mobility Roundtable (ICMB-GMR), 2010 9th Int'l Conference on Jun 2010, pp. 272–279

[12] M.J. Egenhofer, R.D. Franzosa, Point-set topological spatial relations, International Journal of Geographical Information Systems 5 (2) (1991) 161–174

[13] M.J. Egenhofer, J. Herring, A mathematical framework for the definition of topological relationships, 4th Int'l Symposium on Spatial Data Handling. Zurich, Switzerland 1990, pp. 803–813.

[14] K. Georgoulias, N. Papakostas, G. Chryssolouris, S. Stanev, H. Krappe, J. Ovtcharova, Evaluation of flexibility for the effective change management of manufacturing organizations, Robot. Comp.-Integr. Manuf. 25 (6) (2009) 888–893.

[15] O. Günther, Environmental information systems, SIGMOD Rec. 26 (1) (1997) 3–4. [16] K. Jensen, Coloured Petri Nets, Springer, 1987.

[17] K. Jensen, L.M. Kristensen, L. Wells, Coloured Petri nets and CPN tools for modelling and validation of concurrent systems, International Journal on Software Tools for Technology Transfer 9 (3–4) (2007) 213–254.

[18] E. Jäger, I. Altintas, J. Zhang, B. Ludäscher, D. Pennington, W. Michener, A scientific workflow approach to distributed geospatial data processing using web services SSDBM05. SSDBM 2005, pp. 87–90.

[19] J. Jing, K.E. Huff, B. Hurwitz, H. Sinha, B. Robinson, M. Feblowitz, WHAM: supporting mobile workforce and applications in workflow environments, Proceedings of the 10th Int'l Workshop on Research Issues on Data Engineering: Middleware for Mobile Business Applications and E-Commerce, San Diego, California, USA, February 27–28, 2000. IEEE Computer Society 2000, pp. 31–38.

[20] R. Lake, D.S. Burggraf, M. Trninic, L. Rae, Geography Mark-up Language (GML), Foundation for the GeoWeb, Wiley, Chichester, 2004.

[21] M. Leoni, W. Aalst, A. Hofstede, Visual support for work assignment in processaware information systems, Business Process Management. Vol. 5240 of LNCS 2008, pp. 67–83.

[22] B. Ludäscher, I. Altintas, C. Berkley, D. Higgins, E. Jaeger, M. Jones, E.A. Lee, J. Tao, Y. Zhao, Scientific workflow management and the kepler system, Concurrency and Comput, Pract, Exp, 18 (10) (2006) 1039-1065

[23] C. Medeiros, G. Vossen, M. Weske, Geo-wasa-combining GIS technology with workflow management Computer Systems and Software Engineering, 1996. Proceedings of the 7th Israeli Conference on Jun 1996 pp. 129–139

[24] W.L. Meeks, S. Dasgupta, Geospatial information utility: an estimation of the relevance of geospatial information to users, Decision Support Systems 38 (1) (2004) 47–63.

[25] T. Murata, Petri nets: properties, analysis and applications, Proceedings of the IEEE. Vol. 77 1989, pp. 541–580.

[26] OGC, The Opengis Abstract Specification — Topic 8: Relationships Between Features, 1999.

[27] J.L. Peterson, Petri Net Theory and the Modeling of Systems, Prentice-Hall, Inc., New Jersey, 1981.

[28] J.C. Recker, “Modeling with tools is easier, believe me”: the effects of tool functionality on modeling grammar usage beliefs, Information Systems 37 (3) (May 2012) 213–226.

[29] J.C. Recker, M. Rosemann, M. Indulska, P. Green, Business process modeling: a comparative analysis, Journal of the Association for Information Systems 10 (4) (Apr 2009) 333–363.

[30] M. Rosemann, J.C. Recker, C. Flender, Contextualisation of business processes, International Journal of Business Process Integration and Management 3 (1) (2008) 47–60.

[31] L.A. Seffino, C.B. Medeiros, J.V. Rocha, B. Yi, Woodss—a spatial decision support system based on workflows, Decision Support Systems 27 (1) (1999) 105–123.

[32] W.M. van der Aalst, The application of Petri nets to workflow management, J. Circuit Syst. Comput. 8 (01) (1998) 21–66.

[33] W.M.P. van der Aalst, A.H.M.t. Hofstede, M. Weske, Business process management: a survey, Proceedings of the 2003 Int'l Conference on Business Process Management. BPM'03. Springer-Verlag, Berlin, Heidelberg 2003, pp. 1–12.

[34] J. Vom Brocke, M. Rosemann, Handbook on Business Process Management: Strategic Alignment, Governance, Springer, People and Culture, 2010.

[35] X. Zhu, J. Recker, G. Zhu, F. Santoro, Exploring location-dependency in process modeling, Business Process Management Journal 20 (6) (2014)

[36] X. Zhu, G. Zhu, P. Guan, Exploring location-aware process management, Geoinformatics in Resource Management and Sustainable Ecosystem. Vol. 399 of Communications in Computer and Information Science. Springer Berlin Heidelberg 2013, pp. 249–256.

Xinwei Zhu received a PhD in Software Engineering from Wuhan University, China (ranked number five of the best universities there) after obtaining a Master's degree in the same field. Currently, she is working on topics such as business process management, business process modeling, geospatial-based process innovation, and flexible process design. She has published in various internationally renowned journals.

Seppe vanden Broucke received a PhD in Applied Economics at KU Leuven (Catholic University Leuven), Belgium in 2014 after obtaining a Master's degree (magna cum laude) in Business Economics: Information Systems Engineer from the same institution. Currently, he is working as a postdoctoral researcher at the Department of Decision Sciences and Information Management at KU Leuven. His research interests include business data mining and analytics, machine learning, process management, and process mining. His work has been published in well-known international journals and presented at top conferences.

Guobin Zhu received his doctorate from the Ben-Gurion University of the Negev, Israel. Currently, he is working as a professor in the International School of Software, Wuhan University, China. He is a member of the Association of American Geographers (AAG), the Israeli Society for Photogrammetry and Remote Sensing (ILSPRS) and a member of the Chinese Association of Photogrammetry and Remote Sensing. He is working on largescale geographic information systems topics, involving spatial data standards, spatial databases and so on. He has published more than thirty articles in renowned journal and international conferences.

Jan Vanthienen received his PhD degree in Applied Economics from KU Leuven, Belgium. He is a full professor of Information Systems with the Department of Decision Sciences and Information Management, KU Leuven. He is the author or co-author of numerous papers published in international journals and conference proceedings. His current research interests include information and knowledge management, business intelligence and business rules, and information systems analysis and design.

Bart Baesens is a full professor at KU Leuven, Belgium, and a lecturer at the University of Southampton, United Kingdom. He has done extensive research on predictive analytics, data mining, web analytics, fraud detection, and credit risk management. His findings have been published in well-known international journals and presented at international top conferences. He is also co-author of the book Credit Risk Management: Basic Concepts, published in 2008. He regularly tutors, advices and provides consulting support to international firms with respect to their data mining, predictive analytics, CRM, and credit risk management policy.
