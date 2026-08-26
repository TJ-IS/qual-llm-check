---
otero_id: 2126
otero_key: "PA7W7MGE"
title: "A decision support methodology for dynamic taxiway and runway conflict prevention"
authors: "Steven J. Landry; Xin W. Chen; Shimon Y. Nof"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.016"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support methodology for dynamic taxiway and runway con<sup>fl</sup>ict prevention

Steven J. Landry <sup>a</sup>, Xin W. Chen <sup>b</sup>, Shimon Y. Nof <sup>a,</sup>⁎

<sup>a</sup> School of Industrial Engineering, Purdue University, USA

<sup>b</sup> Department of Industrial and Manufacturing Engineering, Southern Illinois University-Edwardsville, USA

## a r t i c l e i n f o

Article history: Received 19 June 2010 Received in revised form 2 October 2012 Accepted 21 January 2013 Available online 27 January 2013

Keywords: Con<sup>fl</sup>ict detection Con<sup>fl</sup>ict resolution Air traf<sup>fi</sup>c Airport Network theory

## a b s t r a c t

Logic needed for decision support to detect and resolve airport surface con<sup>fl</sup>icts is de<sup>fi</sup>ned in this article based on complex network theory In this article conflicts in airport surface operations are defined along with a methodology to model and analyze airport surface constraints. The con<sup>fl</sup>ict detection and resolution logic take advantage of properties of complex con<sup>fl</sup>ict networks for effective con<sup>fl</sup>ict detection and resolution. It is demonstrated and validated with the case of a modeled Harts<sup>fi</sup>eld Atlanta International Airport. Further research will also include validation of the con<sup>fl</sup>ict detection and resolution logic with real airport surface operations data.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The U.S. National Aeronautics and Space Administration (NASA) and the Federal Aviation Administration (FAA) are interested in developing and implementing surface trajectory prediction-based con<sup>fl</sup>ict detection and resolution (CD&R) for aircraft and other vehicles. Surface trajectory prediction can be computed using surveillance data provided by Airport Surface Detection Equipment (ASDE-X) or Automatic Dependent Surveillance-Broadcast (ADS-B) equipment, which enable sharing of vehicle-based position and intent information among airborne and ground-based aircraft, ground transportation vehicles, and control authorities. There is an increasing number of runway incursion incidents, which are precursors to actual accidents [13]. Runway accidents can be among the most catastrophic, including the highest fatality aviation accident on record in Tenerife in 1977.

CD&R is a critical component of surface operation automation. CD&R attempts to ensure safety while increasing the ef<sup>fi</sup>ciency and throughput of surface operations. Previous research was focused mostly on CD&R for airborne aircraft, e.g., trajectory <sup>fl</sup>exibility preservation and constraint minimization [e.g., 14,20,22], although there has been an increasing amount of work focused on surface trajectory prediction and CD&R [6,12,21,31]; most of this work focuses on either trajectory prediction or on route optimization, with very little focused on automated decision support for CD&R [3]. Surface operation automation requires the detection (before or after occurrences) and resolution (alerts and advisories to prevent or resolve) of con<sup>fl</sup>icts between taxiing aircraft, ground transportation vehicles, and/or aircraft close to the airport surface. It is desired to prevent (before occurrences) and resolve all con<sup>fl</sup>icts. Ground-based surface CD&R expands the role of centralized control and provides essential information to the decentralized aircraft-based CD&R.

Con<sup>fl</sup>icts in airport surface operations can be de<sup>fi</sup>ned as cases in which prede<sup>fi</sup>ned three-dimensional and time-based (4D) constraints are not satis<sup>fi</sup>ed. That is, con<sup>fl</sup>icts are incompatibilities between combinations of constraints; constraints are based on 4D trajectory predictions. Con<sup>fl</sup>icts can arise under a number of conditions, including when new trajectories are added, resulting in new constraints, when aircraft deviate from their assigned clearance, or when trajectories are updated based on new information.

Given such a de<sup>fi</sup>nition, the four signi<sup>fi</sup>cant challenges of this decision support research are:

1 How can dynamically changing constraints due to moving aircraft and ground vehicles, and also due to necessary airport operations adjustments, be modeled to detect con<sup>fl</sup>icts?

2 How can relationships between constraints be captured and analyzed for effective CD&R?

3 When a con<sup>fl</sup>ict is detected, what are other con<sup>fl</sup>icts that might occur due to this con<sup>fl</sup>ict?

4 If an advisory is issued to prevent or resolve a con<sup>fl</sup>ict, will the advisory cause new con<sup>fl</sup>icts or will it resolve other con<sup>fl</sup>icts?

The research question is, “can a decision support system based on complex network theory detect and resolve ground con<sup>fl</sup>icts on taxiways and runways?” Based on this research question, this decisionsupport research models and analyzes 4D constraints from a complex network perspective [8–10] and develops CD&R logic to dynamically detect and resolve con<sup>fl</sup>icts.

## 2. Decisions based on constraint modeling and CD&R logic

In order to support the decision process for detecting and resolving con<sup>fl</sup>icts, it is necessary to have accurate predictions of the locations of the vehicles and the times at which it will reach those positions. For consistency with airborne trajectory prediction, these will be referred to as “4D” trajectory predictions, although the vertical dimension is ignored for ground traf<sup>fi</sup>c. The capability to create such trajectories is under developmen [6]. In this section, we will assume the availability of such 4D trajectory predictions, and identify and resolve con<sup>fl</sup>icts through the use of 4D con straint modeling and resolution.

Current 4D trajectory prediction technology for airborne traf<sup>fi</sup>c is not deterministic; the trajectory predictions are stochastic. The accuracy of the predictions is affected by various sources of error, including wind prediction, modeling error, and position error. Moreover, even if such error is minimized, predictions cannot account for control applied by pilots and air traf<sup>fi</sup>c controllers; in such cases, predictions, which are estimates of the future open-loop trajectories, could differ from the actual closed-loop trajectories that occur. (The latter case is not error, but simply differences that could not have been predicted.)

## 2.1. 4D constraints modeling

Con<sup>fl</sup>icts are de<sup>fi</sup>ned as cases where prede<sup>fi</sup>ned 4D constraints are not satis<sup>fi</sup>ed. A constraint describes how resources are utilized by aircraft and ground transportation vehicles. In the context of airport surface operations, resources include taxi ways and runways. Fig. 1 shows an example of two runways (27L/09R and 27R/09L) and four taxiways (A, B, C, and D). For the purpose of CD&R, each runway or taxiway may be divided into sections.

For example, runway 27L/09R is divided into three sections: 1. 2, and 3. (In a practical system, the sections would most likely be smaller than are used here.) Section 1 is between the departure end of runway 27L, which is also the arrival end of runway 09R, and the intersection of the runway and taxiway B. Section 2 is between two intersections: the intersection of runway 27L/09R and taxiway B, and the intersection of 27L 09R and taxiway C. Section 3 is between the intersection of runway 27L/09R and taxiway C, and the arrival end of runway 27L. In general, there are three types of resources S (a total of 22 in Fig. 1) in surface operations: taxiway segments, runway segments, and intersection segments. Symbolically:

• Taxiway resources: $T _ { A } ^ { 1 } , T _ { A } ^ { 2 } , T _ { B } ^ { 1 } , T _ { B } ^ { 2 } , T _ { C } ^ { 1 } , T _ { C } ^ { 2 } , T _ { D } ^ { 1 } , T _ { D } ^ { 2 }$

• Runway resources: R<sub>27L09R</sub><sup>1</sup> , R<sub>27L09R</sub><sup>2</sup> , R<sub>27L09R</sub><sup>3</sup> , $R _ { 2 7 R 0 9 L } ^ { 1 } , R _ { 2 7 R 0 9 L } ^ { 2 } , R _ { 2 7 R 0 9 L } ^ { 3 }$

• Intersection resources: I<sub>27L09R</sub><sup>A</sup> , I<sub>27L09R</sub><sup>B</sup> , I<sub>27L09R</sub><sup>C</sup> , I<sub>27L09R</sub><sup>D</sup> , I<sub>27R09L</sub><sup>A</sup> , I<sub>27R09L</sub><sup>B</sup> , I<sub>27R09L</sub><sup>C</sup> , I<sub>27R09L</sub><sup>D</sup> .

Constraints are de<sup>fi</sup>ned to meet the requirement of surface operations. There are two types of constraints: trajectory time constraints and capacity constraints. Trajectory time constraints contain the predicted times of arrival for entering and exiting intersection segments, runway segments, and taxiway segments. Capacity constraints specify the acceptable number of vehicles, including aircraft and ground transportation vehicles, on a runway section, a taxiway section, or an intersection at a given time. For instance, the capacity constraint for any runway is de<sup>fi</sup>ned by regulation as 1.

Consider the following simple example, using the airport diagram shown in Fig. 1. Suppose an aircraft (N123) lands on runway 09R, Section 1 and is predicted to travel to the terminal through taxiway C. Trajectory prediction software can be used to identify trajectory time constraints a follows (Con indicates constraints):

$\bullet ^ { \underline { { { \mathrm { \tiny ~ t } } } } } C o n _ { R _ { 2 7 L 0 9 R } ^ { 1 } } ^ { N 1 2 3 } : \underline { { { t } } } \left( R _ { 2 7 L 0 9 R } ^ { 1 } , N 1 2 3 \right) = 1 \sharp$ 5 : aircraft N123 enters $R _ { 2 7 L 0 9 R } ^ { 1 }$ at t 15 s

$$
\cdot^ {\overline {{t}}} \operatorname{Con} _ {R _ {2 7 L 0 9 R} ^ {1}} ^ {N 1 2 3} = \underline {{\mathrm{t}}} \operatorname{Con} _ {I _ {2 7 L 0 9 R} ^ {B}} ^ {N 1 2 3}: \bar {t} \left(R _ {2 7 L 0 9 R} ^ {1}, N 1 2 3\right) = \underline {{t}} \left(I _ {2 7 L 0 9 R} ^ {B}, N 1 2 3\right) = 2 5:
$$

aircraft N123 exits $R _ { 2 7 L 0 9 R } ^ { 1 }$ and enters $I _ { 2 7 L 0 9 R } ^ { B }$ at t 25 s

$$
\cdot^ {\overline {{t}}} \operatorname{Con} _ {I _ {2 7 L 0 9 R} ^ {B}} ^ {N 1 2 3} = \underline {{t}} \operatorname{Con} _ {R _ {2 7 L 0 9 R} ^ {2}} ^ {N 1 2 3}: \bar {t} \left(I _ {2 7 L 0 9 R} ^ {B}, N 1 2 3\right) = \underline {{t}} \left(R _ {2 7 L 0 9 R} ^ {2}, N 1 2 3\right) = 2 7:
$$

aircraft N123 exits $I _ { 2 7 L 0 9 R } ^ { B }$ and enters $R _ { 2 7 L 0 9 R } ^ { 2 } \mathrm { a t } t = 2 7 s$

$$
\overline {{t}} C o n _ {R _ {2 7 L 0 9 R} ^ {2}} ^ {N 1 2 3} = \underline {{t}} C o n _ {I _ {2 7 L 0 9 R} ^ {C}} ^ {N 1 2 3}: \bar {t} \left(R _ {2 7 L 0 9 R} ^ {2}, N 1 2 3\right) = \underline {{t}} \left(I _ {2 7 L 0 9 R} ^ {C}, N 1 2 3\right) = 5 7:
$$

aircraft N123 exits $R _ { 2 7 L 0 9 R } ^ { 2 }$ and enters $I _ { 2 7 L 0 9 R } ^ { C } \mathrm { a t } t = 5 7 s$

![](/api/attachments/PA7W7MGE/fulltext/images/c95325dcb8913f2cdcc450963bb9d964f35cc9296416d714f210db476fac7153.jpg)  
Fig. 1. Resource examples in airport surface operations.

$$
\overline {{t}} C o n _ {I _ {2 7 L 0 9 R} ^ {C}} ^ {N 1 2 3} = \underline {{t}} C o n _ {T _ {C} ^ {2}} ^ {N 1 2 3}: \bar {t} \left(I _ {2 7 L 0 9 R} ^ {C}, N 1 2 3\right) = \underline {{t}} \left(T _ {C} ^ {2}, N 1 2 3\right) = 6 5:
$$

aircraft N123 exits $I _ { 2 7 L 0 9 R } ^ { C }$ and enters $T _ { C } ^ { 2 }$ at t 65 s

$$
\overline {{t}} C o n _ {T _ {C} ^ {2}} ^ {N 1 2 3} = \underline {{t}} C o n _ {I _ {2 7 R 0 9 L} ^ {C}} ^ {N 1 2 3}: \bar {t} \left(T _ {C} ^ {2}, N 1 2 3\right) = \underline {{t}} \left(I _ {2 7 R 0 9 L} ^ {C}, N 1 2 3\right) = 7 5:
$$

aircraft N123 exits $T _ { C } ^ { 2 }$ and enters $I _ { 2 7 R 0 9 L } ^ { C }$ at t 75 s

$$
\bullet^ {\overline {{t}}} C o n _ {I _ {2 7 R 0 9 L} ^ {C}} ^ {N 1 2 3} = \underline {{t}} C o n _ {T _ {C} ^ {1}} ^ {N 1 2 3}: \bar {t} \left(I _ {2 7 R 0 9 L} ^ {C}, N 1 2 3\right) = \underline {{t}} \left(T _ {C} ^ {1}, N 1 2 3\right) = 7 8:
$$

aircraft N123 exits $I _ { 2 7 R 0 9 L } ^ { C }$ and enters $T _ { C } ^ { 1 }$ at t 78s

$$
\bullet^ {\overline {{t}}} C o n _ {T _ {C} ^ {1}} ^ {N 1 2 3}: \bar {t} \left(T _ {C} ^ {1}, N 1 2 3\right) = 8 8: \text { aircraft   } N 1 2 3 \text {   exits   } T _ {C} ^ {1} \text {   at   } t = 8 8 \text {   s }
$$

where:

t S; i is the entry time of vehicle i into resource S

<sup></sup>t S; i is the exit time of vehicle i from resource S:

When a trajectory time constraint is not satisfied, a “conflict” occurs between a vehicle and a resource, i.e., the vehicle does not use the resource as speci<sup>fi</sup>ed by the constraint. (That is not to say that this would result in a safety problem, just that there has been non-compliance to a constraint.) We can specify such a con<sup>fl</sup>ict by indicating that the a constraint is not true $\mathbf { e . g . , } \lnot \ \overset { \mathrm { ~ t ~ } } { - } C o n _ { R _ { 2 7 L 0 9 R } ^ { 1 2 3 } } ^ { N 1 2 3 }$

The violation of a trajectory time constraint indicates that a vehicle will not use a resource as expected. Such a con<sup>fl</sup>ict is important because these constraints are related, in particular ways that can be depicted using network theory notation, to capacity constraints, which do identify when con<sup>fl</sup>icts are predicted to occur. The network structure can be used to simplify computation, among other bene<sup>fi</sup>ts.

For capacity constraints, we identify a function Occ(S,t) that identi<sup>fi</sup>es the number of vehicles occupying a given resource S. The occupancy functio is de<sup>fi</sup>ned as:

$$
O c c (S, t) = \sum_ {i = 1} ^ {n} _ {S} \chi_ {i} ^ {S} (t)
$$

where $s \chi _ { i } ( t )$ is an indicator function for resource S and vehicle i:

$$
{ } _ { S } \chi _ { i } ^ { S } ( t ) = \left\{ \begin{array} { l } 1 \text {~ if~ } \underline { { t } } ( S , i ) \leq t \leq \overline { { t } } ( S , i ) \\ 0 \text {~ if~ } \underline { { t } } ( S , i ) > t \text {~ or~ } t > \overline { { t } } ( S , i ) \end{array} \right..
$$

Entry and exit times are provided by trajectory prediction software. Assuming that all runway and taxiway segments allow only one vehicle at any time, the 10 occupancy constraints for surface operations in Fig. 1 are as follows (each constraint is ∀t):

$$
\text {(1)} ^ {\mathrm{Occ}} \operatorname{Con} _ {2 7 L 0 9 R}: \left(\sum_ {i = 1} ^ {3} \operatorname{Occ} \left(R _ {2 7 L 0 9 R} ^ {i}, t\right) + \operatorname{Occ} \left(I _ {2 7 L 0 9 R} ^ {A}, t\right) + \operatorname{Occ} \left(I _ {2 7 L 0 9 R} ^ {B}, t\right) + \operatorname{Occ} \left(I _ {2 7 L 0 9 R} ^ {C}, t\right) + \operatorname{Occ} \left(I _ {2 7 L 0 9 R} ^ {D}, t\right)\right) \leq 1
$$

$$
\text {(2)} ^ {\text {Occ}} C o n _ {2 7 R 0 9 L}: \left(\sum_ {i = 1} ^ {3} O c c \left(R _ {2 7 R 0 9 L} ^ {i}, t\right) + O c c \left(I _ {2 7 R 0 9 L} ^ {A}, t\right) + O c c \left(I _ {2 7 R 0 9 L} ^ {B}, t\right) + O c c \left(I _ {2 7 R 0 9 L} ^ {C}, t\right) + O c c \left(I _ {2 7 R 0 9 L} ^ {D}, t\right)\right) \leq 1,
$$

$$
(3) - (1 0) ^ {\text { Occ }} \operatorname{Con} _ {T _ {j} ^ {i}}: \operatorname{Occ} \left(T _ {j} ^ {i}, t\right) \leq 1; \forall i \in \{1, 2 \}; \forall j \in \{A, B, C, D \}.
$$

## 2.2. CD&R logic and relationships between conflicts

Once arrival information is received about an aircraft by the ground trajectory prediction software, a 4D trajectory for the aircraft is generated, and trajectory and capacity con<sup>fl</sup>icts are detected. Resolutions can then be applied using a rule-based method, similar to that applied in currently proposed airborne CD&R [24], except that fewer resolution maneuvers are available. Speci<sup>fi</sup>cally, in airborne resolutions speed restrictions, heading changes, altitude changes, and perhaps holding patterns are typically used; on the ground only speed restrictions and route changes can be used. In addition, for ground-based resolutions aircraft may be stopped (held) at particular locations rather than in holding patterns used for airborne delays. The rule base for ground-based resolutions is still in development, but would involve the identi<sup>fi</sup>cation of required times of arrival to particular resource segments. (Some required times of arrival for landing aircraft may impose a requirement for airborne delay; such requirements would need to be passed to an airborne trajectory management system such as the Traf<sup>fi</sup>c Management Advisor [27] for implementation.) An example implementation is given in a subsequent section.

As updates are received from airborne and ground surveillance, constraint violations are detected and constraints are updated. If any trajectory time con<sup>fl</sup>icts are detected, which indicate non-conformance to prior constraints, they may cause other time con<sup>fl</sup>icts or capacity con<sup>fl</sup>icts. Typically, constraints have relationships to each other. Resolutions to con<sup>fl</sup>icts must consider such relationships, or the resulting decision support system ma be ineffective [19,29,30].

For the notional airport diagram in Fig. 1, Fig. 2 shows a graph of the constraints for this surface problem, where each constraint is a node, and the relationship is an edge using network notation. The relationships are established by physical connections between the resources that form the basis for the constraints. In addition, each node in the network is connected to the constraints associated with their individual capacities, in the case of taxiway resources and intersections between taxiways (none of which exist in Fig. 1), or associated with their collective capacity, in the case of run ways and intersections of taxiways and runways.

![](/api/attachments/PA7W7MGE/fulltext/images/e97b9cbb7c21bae3335930afc4cfa1ac6e0a33714b27ff0081def1ed32624876.jpg)  
Fig. 2. Network graph of example airport layout.

The resulting network provides structure that can be used in solving CD&R problems. The following section discusses the relationships between the constraints and how that information can be used to simplify computation. (In addition, the representation of the airport as a network suggests an ef<sup>fi</sup>cient data structure.)

## 2.2.1. Conflict relationships

The graph in Fig. 2 is undirected. Given a set of predicted trajectories, the graph becomes directed, and certain links may be eliminated. The graph, of course, changes as predicted trajectories, change, are added, or are removed.

For example, suppose one aircraft (with call sign ABC123) is inbound to the airport shown in Fig. 1, and another (with call sign DEF456) is taxiing out for takeoff. In doing so, we assume that ABC123 will touch down just beyond the intersection of taxiway A and 27L09R, and DEF456 would takeoff prior to the intersection of taxiway D with 27R09L. Trajectory prediction produces the following set of trajectory time constraints, and the graph be comes directed as shown in Fig. 3:

$$
\left\{ \begin{array}{l} \underline {{\mathrm{t}}} C o n _ {T _ {A} ^ {1}} ^ {D E F 4 5 6} = 1 3 0; \overline {{\mathrm{t}}} C o n _ {T _ {A} ^ {1}} ^ {D E F 4 5 6} = \underline {{\mathrm{t}}} C o n _ {I _ {2 7 R 0 9 L} ^ {A}} ^ {D E F 4 5 6} = 1 4 2; \overline {{\mathrm{t}}} C o n _ {I _ {2 7 R 0 9 L} ^ {A}} ^ {D E F 4 5 6} = \underline {{\mathrm{t}}} C o n _ {R _ {2 7 R 0 9 L} ^ {1}} ^ {D E F 4 5 6} = 1 4 6; \overline {{\mathrm{t}}} C o n _ {R _ {2 7 R 0 9 L} ^ {1}} ^ {D E F 4 5 6} = \\ \underline {{\mathrm{t}}} C o n _ {I _ {2 7 R 0 9 L} ^ {B}} ^ {D E F 4 5 6} = 1 8 8; \overline {{\mathrm{t}}} C o n _ {I _ {2 7 R 0 9 L} ^ {B}} ^ {D E F 4 5 6} = \underline {{\mathrm{t}}} C o n _ {R _ {2 7 R 0 9 L} ^ {B}} ^ {D E F 4 5 6} = 1 9 0; \overline {{\mathrm{t}}} C o n _ {R _ {2 7 R 0 9 L} ^ {B}} ^ {D E F 4 5 6} = \underline {{\mathrm{t}}} C o n _ {I _ {2 7 R 0 9 L} ^ {C}} ^ {D E F 4 5 6} = 2 0 7; \overline {{\mathrm{t}}} C o n _ {I _ {2 7 R 0 9 L} ^ {C}} ^ {D E F 4 5 6} = 2 0 9 \end{array} \right\}
$$

and

$$
\left. \right.\left\{\begin{array}{l}\underline {{\mathrm{t}}} C o n _ {R _ {2 7 L 0 9 R} ^ {1}} ^ {A B C 1 2 3} = 1 4 5; \overline {{\mathrm{t}}} C o n _ {R _ {2 7 L 0 9 R} ^ {1}} ^ {A B C 1 2 3} = \underline {{\mathrm{t}}} C o n _ {I _ {2 7 L 0 9 R} ^ {B}} ^ {A B C 1 2 3} = 1 5 2; \overline {{\mathrm{t}}} C o n _ {I _ {2 7 L 0 9 R} ^ {B}} ^ {A B C 1 2 3} = \underline {{\mathrm{t}}} C o n _ {R _ {2 7 L 0 9 R} ^ {2}} ^ {A B C 1 2 3} = 1 5 5; \overline {{\mathrm{t}}} C o n _ {R _ {2 7 L 0 9 R} ^ {2}} ^ {A B C 1 2 3} =\\\underline {{\mathrm{t}}} C o n _ {I _ {2 7 L 0 9 R} ^ {C}} ^ {A B C 1 2 3} = 1 8 2; \overline {{\mathrm{t}}} C o n _ {I _ {2 7 L 0 9 R} ^ {C}} ^ {A B C 1 2 3} = \underline {{\mathrm{t}}} C o n _ {T _ {C} ^ {2}} ^ {A B C 1 2 3} = 1 8 7; \overline {{\mathrm{t}}} C o n _ {T _ {C} ^ {2}} ^ {A B C 1 2 3} = \underline {{\mathrm{t}}} C o n _ {I _ {2 7 L 0 9 R} ^ {C}} ^ {A B C 1 2 3} = 2 0 4; \overline {{\mathrm{t}}} C o n _ {I _ {2 7 L 0 9 R} ^ {C}} ^ {A B C 1 2 3} = 2 1 4\end{array}\right\}.
$$

Let ⊂ represent the inclusive relationship. Trajectory time con<sup>fl</sup>icts for the network diagram in Fig. 3 are related to one another in ways indicated by the directed graph. A particular trajectory constraint, if violated, is likely to have an effect on any other constraint to which it is a precursor, as indicated by that node “pointing to” another node. In addition, trajectory time con<sup>fl</sup>icts are related to occupancy time con<sup>fl</sup>icts for nodes that are along the path of the directed graph. For example, $\overset { \mathrm { t } } { - } C o n _ { R _ { 2 7 L 0 9 R } ^ { 1 } } ^ { A B C 1 2 3 }$ has the following relationships with other con<sup>fl</sup>icts:

![](/api/attachments/PA7W7MGE/fulltext/images/33f43f9b5c091745bba5ff520bc1bb677411da392b18744387c95adf2be97b4c.jpg)  
Fig. 3. Directed graph given the two example aircraft.

$$
\begin{array}{l} \underline {{t}}   C o n _ {R _ {2 7 L 0 9 R} ^ {1}} ^ {A B C 1 2 3} \subset \left\{ \begin{array}{l} \overline {{^ t}}   C o n _ {R _ {2 7 L 0 9 R} ^ {1}} ^ {A B C 1 2 3}, \underline {{^ t}}   C o n _ {I _ {2 7 L 0 9 R} ^ {i}} ^ {A B C 1 2 3}, \overline {{^ t}}   C o n _ {I _ {2 7 L 0 9 R} ^ {i}} ^ {A B C 1 2 3}, \underline {{^ t}}   C o n _ {R _ {2 7 L 0 9 R} ^ {2}} ^ {A B C 1 2 3}, \overline {{^ t}}   C o n _ {R _ {2 7 L 0 9 R} ^ {2}} ^ {A B C 1 2 3}, \\ \underline {{^ t}}   C o n _ {T _ {C} ^ {i}} ^ {A B C 1 2 3}, \overline {{^ t}}   C o n _ {T _ {C} ^ {i}} ^ {A B C 1 2 3}, \text {Occ} C o n _ {R _ {2 7 L 0 9 R}}, \text {Occ} C o n _ {T _ {C} ^ {i}} \end{array} \right\} \\ \forall i \in \{1, 2 \}; \forall j \in \{B, C \} \end{array}
$$

This means that $\overset { \mathrm { ~ t ~ } } { - } C o n _ { R _ { 2 7 L 0 9 R } ^ { 1 } } ^ { A B C 1 2 3 }$ , if violated, could affect these other constraints. So a trajectory time con<sup>fl</sup>ict can “ripple” through to other con-<sup>fl</sup>icts, but only those con<sup>fl</sup>icts included in the relationships need to be checked. Moreover, given a system where there are no occupancy con<sup>fl</sup>icts, a subsequent occupancy con<sup>fl</sup>ict can only occur when one of the precursor trajectory time constraints is violated. Given a complex network structure, this can reduce the computations and comparisons that must be performed, as well as storage requirements for data structures, when compared to a brute force method.

## 2.2.2. Alignment of conflict resolutions and trajectory predictions

This concept also works in reverse when applying con<sup>fl</sup>ict resolution. Imposing required times-of-arrival (RTA), as is often done in the resolution phase, will cause a “reverse ripple,” meaning that constraints that include the resource at which the RTA is applied may be affected.

However, identifying and applying a resolution do not immediately correct the occupancy constraint violation. If trajectory predictions are computed frequently, for example every 10–15 s as is done in the CD&R systems under development, then the occupancy time con<sup>fl</sup>ict will not disappear until the resolution is completely implemented, Moreover, many additional problems may have arisen in the time it takes to complete a resolution

$$
\neg^ {\text { Occ }} \operatorname{Con} _ {R _ {2 7 L 0 9 R}}
$$

$$
\text { for } \stackrel {{t}} {{-}} C o n _ {R _ {2 7 L 0 9 R} ^ {1}} ^ {A B C 1 2 3}
$$

$$
\underline {{\mathrm{t}}} C o n _ {R _ {2 7 L 0 9 R} ^ {1}} ^ {A B C 1 2 3}
$$

as the aircraft's trajectory was modi<sup>fi</sup>ed to conform to the RTA. The migration of $\overset { \mathrm { ~ t ~ } } { - } C o n _ { R _ { 2 7 L 0 9 R } ^ { 1 } } ^ { A B C 1 2 3 }$ could be monitored to ensure the con<sup>fl</sup>ict resolution was being implemented; the continuous violations during this period could otherwise be ignored.

## 3. CD&R decisions and complex network theory

In constructing the CD&R process in this way, network theory can be applied to provide ef<sup>fi</sup>cient decision support. In particular, network theory can be used to provide guidance on local and global con<sup>fl</sup>ict resolution and decisions.

## 3.1. Local and global conflict resolution

Runway safety is the highest priority for airports. Active runway intrusions are major safety concerns that must be detected and resolved. In addition, the number of aircraft arriving at and departing from the airport is an important indicator of the throughput of the airport. Global con<sup>fl</sup>ict resolution is often applied to con<sup>fl</sup>icts involving decisions on the use of runways whereas local con<sup>fl</sup>ict resolution is applied to decisions on con<sup>fl</sup>icts involving the use of taxiways. When a con<sup>fl</sup>ict involves the use of both runways and taxiways, activities on runways have higher priority during con<sup>fl</sup>ict resolution.

Global con<sup>fl</sup>ict resolution decisions resolve con<sup>fl</sup>icts by propagating them to less critical resources. For instance, there are trajectory time con<sup>fl</sup>icts for the use of a runway by an aircraft. These time con<sup>fl</sup>icts occur because surveillance data show that the aircraft does not satisfy trajectory time constraints. There may be trajectory capacity con<sup>fl</sup>icts for the use of a runway by an aircraft. These capacity con<sup>fl</sup>icts occur because 4D trajectory information shows that the use of certain interactions is not possible due to vehicles traveling on taxiways. Instead of adjusting the aircraft speed and trajectory to resolve the con<sup>fl</sup>icts, global con<sup>fl</sup>ict resolution decisions adjust the speed and trajectory for vehicles traveling on taxiways.

Local con<sup>fl</sup>ict resolution decisions resolve con<sup>fl</sup>icts by con<sup>fi</sup>ning them to the resources involved. For instance, two vehicles using a taxiway have trajectory capacity con<sup>fl</sup>icts. These con<sup>fl</sup>icts may be related to the use of an intersection that is part of another taxiway or runway. Local con<sup>fl</sup>ict resolution resolves these con<sup>fl</sup>icts by adjusting trajectory time constraints for one of the two vehicles or both without causing additional con<sup>fl</sup>icts. A more relaxed local con<sup>fl</sup>ict resolution may allow con<sup>fl</sup>ict propagation among all taxiways. Con<sup>fl</sup>icts on the use of a taxiway can be resolved by adjusting trajectory time constraints for vehicles traveling on other taxiways. If local con<sup>fl</sup>ict resolution is relaxed further, i.e., to allow con<sup>fl</sup>ict propagation among all resources, local con<sup>fl</sup>ict resolution becomes global con<sup>fl</sup>ict resolution.

In summary, there are at least three different con<sup>fl</sup>ict resolution decision approaches: 1) global con<sup>fl</sup>ict resolution for all resources. All resources have the same priority. Trajectory time constraints for all resources are randomly selected to resolve con<sup>fl</sup>icts; 2) local con<sup>fl</sup>ict resolution for all resources. Con<sup>fl</sup>icts are con<sup>fi</sup>ned to the resources involved. The underlying assumption here is the same as that for global con<sup>fl</sup>ict resolution for all resources: all resources have the same priority. It is not desired that con<sup>fl</sup>icts on the use of one resource propagate to other resources in local con<sup>fl</sup>ict resolution, whereas in global con<sup>fl</sup>ict resolution con<sup>fl</sup>icts are allowed to propagate; 3) hybrid approach: global con<sup>fl</sup>ict resolution for high priority resources, e.g., runways, and local con<sup>fl</sup>ict resolution for low priority resources, e.g., taxiways. Compared to local con<sup>fl</sup>ict resolution, global con<sup>fl</sup>ict resolution is more likely to <sup>fi</sup>nd a solution because of its large solution base, but con<sup>fl</sup>ict propagation poses safety risks and can be computationally challenging for large airports. Local con<sup>fl</sup>ict resolution minimizes safety risks, but can result in infeasible solutions. The hybrid approach for decision support is expected to provide feasible yet low risk solutions for higher throughput surface operations.

## 3.2. Complex network theory for CD&R decisions

A typical airport has several runways and many taxiways. Multiple con<sup>fl</sup>icts may occur at the same time. Certain con<sup>fl</sup>icts are related to each other, e.g., trajectory time con<sup>fl</sup>icts have the inclusive relationship and may cause trajectory capacity con<sup>fl</sup>icts. All con<sup>fl</sup>icts must be resolved and con<sup>fl</sup>ict resolution sometimes generates new con<sup>fl</sup>icts, e.g., to resolve trajectory capacity con<sup>fl</sup>icts may cause trajectory time con<sup>fl</sup>icts. The CD&R logic must be able to detect and resolve multiple con<sup>fl</sup>icts simultaneously.

Another factor that contributes to the complexity of CD&R is the number of vehicles traveling on runways and taxiways. As this number increases, the number of con<sup>fl</sup>icts may increase exponentially. New con<sup>fl</sup>icts emerge as vehicles are traveling. The large number of vehicles and dynamic con<sup>fl</sup>ict emergences pose great challenges to CD&R. A typical, brute force method treats nodes independently, potentially requiring a much larger number of computations and a much larger data structure than would be needed for a network theory-based approach.

In addition to ef<sup>fi</sup>ciency considerations, there are other insights that can be gained from viewing this problem from the perspective of complex network theory [11]. Con<sup>fl</sup>icts in airport surface operations form a complex network. The classic model of network, the random network (RN), was <sup>fi</sup>rst discussed in the early 1950s [26] and was rediscovered and analyzed in a series of papers published in the late 1950s and early 1960s [15–17]. Two other types of networks that have been studied extensively and capture the topology of many real-world networks are: 1) scale-free network (SFN) [1,4,7,25] and 2) Bose–Einstein condensation network (BECN) [5], which was discovered in an effort to model the competitive nature of networks.

An important reason to view con<sup>fl</sup>icts from a network perspective is that certain properties of a system of con<sup>fl</sup>icts cannot be analyzed by dividing the system into components. One of the important properties of a RN is phase transition or bond percolation [2,23,26]. There is a phase transition from a fragmented RN for the mean degree no greater than one d≤1<sup> </sup> to a RN dominated by a giant component for the mean degree greater than one d > 1<sup> </sup>. The implication of this property is as follows: suppose con<sup>fl</sup>icts form an undirected RN with d > 1. If any con<sup>fl</sup>ict is detected, all other con<sup>fl</sup>icts will occur with a probability close to one. Resources involved in the con<sup>fl</sup>icts are close to their full capacity. Any disturbance (con<sup>fl</sup>ict) propagates throughout the network that makes CD&R dif<sup>fi</sup>cult.

The signature of ground-based CD&R decisions is the centralized approach, which identi<sup>fi</sup>es and stores all con<sup>fl</sup>icts and their relationships based on 4D trajectory information and surveillance data. (Of course, this information is imperfect; we intend this only as a distinction from a distributed system that has subsets of the con<sup>fl</sup>icts identi<sup>fi</sup>ed.) Since con<sup>fl</sup>ict networks are identi<sup>fi</sup>ed as vehicles traveling on runways and taxiways, these networks provide 1) roadmaps of what con<sup>fl</sup>icts will occur and what system-wide impacts are if one or more con<sup>fl</sup>icts are detected and 2) impact analysis of con<sup>fl</sup>ict resolution for coordinated con<sup>fl</sup>ict resolution decisions.

## 4. Example application

To demonstrate how the CD&R logic could be applied to a real example, a case study of a commercial airport is analyzed to illustrate how con<sup>fl</sup>icts in surface operations are detected and resolved. The performance of the decision support system with CD&R logic is compared with the performance of manual and computer integrated CD&R decisions for this example.

The layout of the Harts<sup>fi</sup>eld Atlanta International Airport is shown in Fig. 4. The airport has <sup>fi</sup>ve runways, four of which are shown, each of which allows landing or take-off from both directions. (Typically, however, the inside runways, those closest to the terminal, are used for takeoff, while the outside runways are used for landing.)

Only the southern half of the runway system will be analyzed in order to limit the complexity of the example. The example, and an overlay of the notation, is shown in Fig. 5. For legibility, we shall only use the runway notation for the one direction and omit the preceding zero (9R and 9L) rather than the full name of the runway (27L09R and 27R09L respectively), and refer to those runways in the subsequent description in the same manner.

In this example, there is an aircraft departing on runway 9L, an aircraft arriving on runway 9R, and two aircraft taxiing. The dashed arrows show the planned trajectories of the four aircraft. Two aircraft, <sup>fl</sup>ights 1000 and 2000 are utilizing runways 9L and 9R, respectively, with <sup>fl</sup>ight 1000 a takeoff and <sup>fl</sup>ight 2000 a landing. Flight 3000 has recently landed on 9R and is taxiing to parking; this aircraft will have to cross 9L. Aircraft 4000 has recently aborted its takeoff on 9L, rolled out to the end of the runway, and is taxiing back for a second takeoff attempt. The CD&R decision support should be able to detect and resolve con<sup>fl</sup>icts that might occur between the four aircraft.

![](/api/attachments/PA7W7MGE/fulltext/images/133486c4cd3e45e8b7d1d641cc6b0e2db9de3c6b4daf26df23caccb98ac6b867.jpg)  
Fig. 4. Harts<sup>fi</sup>eld Atlanta International Airport (image courtesy of Federal Aviation Administration).

![](/api/attachments/PA7W7MGE/fulltext/images/bfe6da998b4f6a2ec4b2b6535cd1f69ca1da0ace2f40a802698831e52a017cc6.jpg)

![](/api/attachments/PA7W7MGE/fulltext/images/708e0f0c7c3ac1616e61e8defbb034dbf0529c12e4985dcacc95ca100a648da6.jpg)  
Fig. 5. Example application: (a) mapping of example to Harts<sup>fi</sup>eld Atlanta International Airport diagram and (b) model notation for relevant portion of airport network (intersections have been omitted and runway notation shortened to one direction for legibility).

In this example we have the following resources:

• Taxiway resources: $T _ { D } ^ { 1 - 3 } , T _ { L } ^ { 1 - 8 } , T _ { M } ^ { 1 - 8 } , T _ { M 1 } ^ { 1 - 2 } , T _ { N } ^ { 1 - 3 } , T _ { N 6 } ^ { 1 } , T _ { N 1 0 } ^ { 1 } , T _ { D } ^ { 1 }$ N13<sup>1</sup>

$R _ { 9 R } ^ { 1 - 5 } , R _ { 9 L } ^ { 1 - }$ 8 • Runway resources:

• Intersection resources: I<sup>N6</sup>, $\bar { I _ { 9 R } ^ { N 1 0 } } , \bar { I _ { 9 R } ^ { N 1 3 } } , \bar { I _ { 9 L } ^ { M 1 } } , \bar { I _ { 9 L } ^ { D } } , \bar { I _ { 9 L } ^ { N 1 3 } } , \bar { I _ { L } ^ { D } } , \bar { I _ { L } ^ { M 1 } } , \bar { I _ { M } ^ { D } } , \bar { I _ { M } ^ { M 1 } } , \bar { I _ { N } ^ { D } } , \bar { I _ { N } ^ { D } } ,$ I<sub>N6</sub><sup>N</sup> , I<sub>N10</sub><sup>N</sup> .

Also, for this example we assume the following trajectory predictions (Table 1).

In addition, the directed graph for this system is shown in Fig. 6.

4.1. Decision support with CD&R logic

The constraints are as follows (∀ t):

$$
{ } ^ { \text {   O   c   c   } } C o n _ { 9 R } : \sum _ { i = 1 } ^ { 4 } O c c \left( R _ { 9 R } ^ { i } , t \right) + O c c \left( I _ { 9 R } ^ { N 6 } , t \right) + O c c \left( I _ { 9 R } ^ { N 1 0 } , t \right) \leq 1\tag{1}
$$

$$
{ } ^ { \text {   O   c   c   } } C o n _ { 9 L } : \sum _ { i = 1 } ^ { 6 } O c c \left( R _ { 9 L } ^ { i } , t \right) + O c c \left( I _ { 9 L } ^ { D } , t \right) \leq 1\tag{2}
$$

$$
{ } ^ { \text {   O   c   c   } } C o n _ { T _ { M } ^ { i } } : O c c \left( T _ { M } ^ { i } , t \right) \leq 1 ; \forall i \in \{ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 \}\tag{3}
$$

$$
{ } ^ { \text {   O   c   c   } } C o n _ { T _ { N } ^ { i } } : O c c \left( T _ { N } ^ { i } , t \right) \leq 1 ; \forall i \in \{ 2 , 3 \}\tag{4}
$$

$$
{ } ^ { \text {   O   c   c   } } C o n _ { T _ { D } ^ { i } } : O c c \left( T _ { D } ^ { i } , t \right) \leq 1 ; \forall i \in \{ 1 , 2 , 3 \}\tag{5}
$$

$$
{ } ^ { \text {   O   c   c   } } C o n _ { I _ { L } ^ { D } } : O c c \left( I _ { L } ^ { D } , t \right) \leq 1\tag{6}
$$

$$
{ } ^ { \text {   O   c   c   } } C o n _ { I _ { M } ^ { D } } : O c c \left( I _ { M } ^ { D } , t \right) \leq 1\tag{7}
$$

$$
{ } ^ { \text {   O   c   c   } } C o n _ { I _ { N 1 0 } ^ { N } } : O c c \left( I _ { N 1 0 } ^ { N } , t \right) \leq 1\tag{8}
$$

$$
{ } ^ { \text {   O   c   c   } } C o n _ { T _ { N 1 0 } ^ { 1 } } : O c c \left( T _ { N 1 0 } ^ { 1 } , t \right) \leq 1 .\tag{9}
$$

Calculating these values, we <sup>fi</sup>nd that $\neg ^ { 0 \mathrm { c c } } C o n _ { I _ { n } ^ { 9 L } }$ between t=35 and t=36; also $\stackrel { 0 \mathrm { c c } } { \neg } C o n _ { I _ { M } ^ { D } }$ at t=57. These con<sup>fl</sup>icts occur between aircraft M 1000 and 3000 for $\neg ^ { 0 \mathrm { c c } } C o n _ { I _ { D } ^ { 9 L } }$ and between aircraft 3000 and 4000 for $\neg ^ { 0 \mathrm { c c } } C o n _ { I _ { M } ^ { D } \cdot } { \sf A }$ resolution for this con<sup>fl</sup>ict can be found, referencing the directed graph and using a rule-based method. (The rule-based method is still in development.) The directed graph indicates that $I _ { M } ^ { D }$ is contained by $I _ { 9 L } ^ { D }$ , which suggests that the resolution must be applied to a resource that contains $I _ { 9 L } ^ { D }$ . Since the trajectory of aircraft 3000 contains these points, an obvious resolution is to set an RTA: $\underline { { t } } \Big ( I _ { 9 L } ^ { D } , 3 0 0 0 \Big ) = 3 7$ . Depending on the availability of delay at particular <sup></sup>nodes, i.e. the amount of delay that can be taken in a particular node, nodes in the graph that contain the node at which the RTA is set may also need to be adjusted. The resolved trajectories are shown in Table 2.

In summary, this example provides an illustration of how this decision support with CD&R logic methodology can effectively 1) detect con<sup>fl</sup>icts before they occur, 2) resolve con<sup>fl</sup>icts to prevent them from occurring, 3) determine CD&R impact through the analysis of con<sup>fl</sup>ict networks, and 4) identify better con<sup>fl</sup>ict resolution decisions. Validation of this methodology is being pursued currently.

It is possible that con<sup>fl</sup>icts occur with little or no time to resolve the con<sup>fl</sup>ict. This methodology cannot resolve con<sup>fl</sup>icts if there is insuf<sup>fi</sup>- cient time to implement a resolution, as is the case with most, if not all, existing and proposed CD&R systems. A method to prevent the system from arriving at such a state has been proposed [22] and is being considered for integration with this methodology.

Table 1  
Trajectory predictions for ATL example. (The highlighted cells indicate con<sup>fl</sup>icts.)

<table><tr><td>Aircraft 1000</td><td> $R_{9L}^{1}$ </td><td> $R_{9L}^{2}$ </td><td> $R_{9L}^{3}$ </td><td> $R_{9L}^{4}$ </td><td> $R_{9L}^{5}$ </td><td> $R_{9L}^{6}$ </td><td> $I_{9L}^{D}$ </td><td></td><td></td><td></td><td></td></tr><tr><td>Enter</td><td>0</td><td>11</td><td>20</td><td>27</td><td>32</td><td>34</td><td>35</td><td></td><td></td><td></td><td></td></tr><tr><td>Exit</td><td>11</td><td>20</td><td>27</td><td>32</td><td>34</td><td>35</td><td>36</td><td></td><td></td><td></td><td></td></tr><tr><td>Aircraft 2000</td><td> $R_{9R}^{1}$ </td><td> $R_{9R}^{2}$ </td><td> $R_{9R}^{3}$ </td><td> $I_{9R}^{N6}$ </td><td> $R_{9R}^{4}$ </td><td> $I_{9R}^{N10}$ </td><td> $T_{N10}^{1}$ </td><td> $I_{N10}^{N}$ </td><td> $T_{N}^{3}$ </td><td> $I_{N}^{D}$ </td><td> $T_{D}^{1}$ </td></tr><tr><td>Enter</td><td>5</td><td>7</td><td>14</td><td>26</td><td>30</td><td>44</td><td>46</td><td>61</td><td>67</td><td>74</td><td>80</td></tr><tr><td>Exit</td><td>7</td><td>14</td><td>26</td><td>30</td><td>44</td><td>46</td><td>61</td><td>67</td><td>74</td><td>80</td><td>87</td></tr><tr><td>Aircraft 3000</td><td> $T_{N}^{2}$ </td><td> $I_{N}^{N10}$ </td><td> $T_{N}^{3}$ </td><td> $I_{N}^{D}$ </td><td> $T_{D}^{1}$ </td><td> $I_{D}^{9L}$ </td><td> $T_{D}^{2}$ </td><td> $I_{D}^{M}$ </td><td> $T_{D}^{3}$ </td><td> $I_{D}^{L}$ </td><td></td></tr><tr><td>Enter</td><td>-</td><td>4</td><td>10</td><td>17</td><td>23</td><td>30</td><td>36</td><td>51</td><td>57</td><td>61</td><td></td></tr><tr><td>Exit</td><td>4</td><td>10</td><td>17</td><td>23</td><td>30</td><td>36</td><td>51</td><td>57</td><td>61</td><td>67</td><td></td></tr><tr><td>Aircraft 4000</td><td> $T_{M}^{8}$ </td><td> $T_{M}^{7}$ </td><td> $I_{M}^{D}$ </td><td> $T_{M}^{6}$ </td><td> $T_{M}^{5}$ </td><td> $T_{M}^{4}$ </td><td> $T_{M}^{3}$ </td><td> $T_{M}^{2}$ </td><td> $T_{M}^{1}$ </td><td></td><td></td></tr><tr><td>Enter</td><td>-</td><td>27</td><td>57</td><td>63</td><td>78</td><td>98</td><td>130</td><td>152</td><td>186</td><td></td><td></td></tr><tr><td>Exit</td><td>27</td><td>57</td><td>63</td><td>78</td><td>98</td><td>130</td><td>152</td><td>186</td><td>216</td><td></td><td></td></tr></table>

Both manual and computer integrated CD&R decisions are either in use or being proposed for airport surface operations. Manual CD&R, where ground and tower controllers either visually or mentally project the future locations of aircraft and other vehicles moving on the surface of the airport, prevents con<sup>fl</sup>icts primarily through separation assurance rather than collision avoidance. For instance, when an aircraft is moving on a runway, no other vehicle can travel or cross that runway until the aircraft departs the runway. This is safe, but may be inef<sup>fi</sup>cient because the utilization of resources is low. Similarly, the utilization of separation assurance for taxiway and ramp operations is likely inef<sup>fi</sup>cient. In addition, it requires close manual monitoring of moving aircraft over long periods of time.

## 4.2. Manual and computer integrated CD&R decisions

In-use or proposed computer integrated CD&R systems would utilize 4D trajectory information and surveillance data to provide alerts. For instance, in the example described above, computer integrated CD&R issues a visual, sound, and/or other type of alert to the human controller regarding the con<sup>fl</sup>ict problem. Computer integrated CD&R should improve detection of con<sup>fl</sup>icts as compared to manual CD&R because it can track moving vehicles at all times without losses of vigilance known to accompany human performance at such tasks. However, such systems do not generally provide resolutions to detected con<sup>fl</sup>icts, and do not examine dependencies between multiple con<sup>fl</sup>icts/resolutions.

With a decision support system based on the CD&R logic described above, the de<sup>fi</sup>ciencies identi<sup>fi</sup>ed with manual and computer integrated CD&R are overcome. The decision support system with CD&R logic automates the decisions of detection, resolution, and prevention of con<sup>fl</sup>icts. Moreover, the CD&R logic considers dependencies between con<sup>fl</sup>icts/resolutions through the analysis of con<sup>fl</sup>ict networks, which should improve resolutions. Table 3 compares the three CD&R decision methods.

![](/api/attachments/PA7W7MGE/fulltext/images/52b1ddcecd6d49f9e62e0fc156bcbb394bca0fe52495913bf5c117039e5a5ab5.jpg)  
Fig. 6. Directed graph for ATL example

Table 2  
Resolved trajectories for ATL example.

<table><tr><td>Aircraft 1000</td><td> $R_{9L}^{1}$ </td><td> $R_{9L}^{2}$ </td><td> $R_{9L}^{3}$ </td><td> $R_{9L}^{4}$ </td><td> $R_{9L}^{5}$ </td><td> $R_{9L}^{6}$ </td><td> $I_{9L}^{D}$ </td><td></td><td></td><td></td><td></td></tr><tr><td>Enter</td><td>0</td><td>11</td><td>20</td><td>27</td><td>32</td><td>34</td><td>35</td><td></td><td></td><td></td><td></td></tr><tr><td>Exit</td><td>11</td><td>20</td><td>27</td><td>32</td><td>34</td><td>35</td><td>36</td><td></td><td></td><td></td><td></td></tr><tr><td>Aircraft 2000</td><td> $R_{9R}^{1}$ </td><td> $R_{9R}^{2}$ </td><td> $R_{9R}^{3}$ </td><td> $I_{9R}^{N6}$ </td><td> $R_{9R}^{4}$ </td><td> $I_{9R}^{N10}$ </td><td> $T_{N10}^{1}$ </td><td> $I_{N10}^{N}$ </td><td> $T_{N}^{3}$ </td><td> $I_{N}^{D}$ </td><td> $T_{D}^{1}$ </td></tr><tr><td>Enter</td><td>5</td><td>7</td><td>14</td><td>26</td><td>30</td><td>44</td><td>46</td><td>61</td><td>67</td><td>74</td><td>80</td></tr><tr><td>Exit</td><td>7</td><td>14</td><td>26</td><td>30</td><td>44</td><td>46</td><td>61</td><td>67</td><td>74</td><td>80</td><td>87</td></tr><tr><td>Aircraft 3000</td><td> $T_{N}^{2}$ </td><td> $I_{N}^{N10}$ </td><td> $T_{N}^{3}$ </td><td> $I_{N}^{D}$ </td><td> $T_{D}^{1}$ </td><td> $I_{D}^{9L}$ </td><td> $T_{D}^{2}$ </td><td> $I_{D}^{M}$ </td><td> $T_{D}^{3}$ </td><td> $I_{D}^{L}$ </td><td></td></tr><tr><td>Enter</td><td>-</td><td>4</td><td>10</td><td>17</td><td>23</td><td>37</td><td>43</td><td>64</td><td>70</td><td>74</td><td></td></tr><tr><td>Exit</td><td>4</td><td>10</td><td>17</td><td>23</td><td>30</td><td>43</td><td>58</td><td>70</td><td>74</td><td>80</td><td></td></tr><tr><td>Aircraft 4000</td><td> $T_{M}^{8}$ </td><td> $T_{M}^{7}$ </td><td> $I_{M}^{D}$ </td><td> $T_{M}^{6}$ </td><td> $T_{M}^{5}$ </td><td> $T_{M}^{4}$ </td><td> $T_{M}^{3}$ </td><td> $T_{M}^{2}$ </td><td> $T_{M}^{1}$ </td><td></td><td></td></tr><tr><td>Enter</td><td>-</td><td>27</td><td>57</td><td>63</td><td>78</td><td>98</td><td>130</td><td>152</td><td>186</td><td></td><td></td></tr><tr><td>Exit</td><td>27</td><td>57</td><td>63</td><td>78</td><td>98</td><td>130</td><td>152</td><td>186</td><td>216</td><td></td><td></td></tr></table>

## 5. Conclusions and future research

The CD&R logic for decision support has been developed, demonstrated, analyzed and applied for an example of the Harts<sup>fi</sup>eld Atlanta International Airport. In the next phase of this research, a rule-based resolution method will be completed, and the resulting CD&R decision support system will be validated with real life data. In addition, it may be desirable to employ case-based reasoning to the rule-set in order to improve computational ef<sup>fi</sup>ciency [18,28]. Empirical validation will examine the performance of decision support with the CD&R logic in comparison to manual and computer integrated CD&R decisions. Several system-wide performance metrics are planned:

• Maximum capacity: the number of aircraft serviced (aircraft that land or take off) within a time period, e.g., 24 h, under excessive service requests. Maximum capacity partly re<sup>fl</sup>ects the ef<sup>fi</sup>ciency of the airport as a result of better CD&R decisions.

• Conflict detection horizon: a nonnegative number that is the amount of time before a con<sup>fl</sup>ict occurs when it is detected. The con<sup>fl</sup>ict detection horizon is zero if a con<sup>fl</sup>ict has already occurred when it is detected. This metric indicates the responsiveness of con<sup>fl</sup>ict detection decisions. With larger horizon, con<sup>fl</sup>ict detection is more responsive and provides more time for resolution decisions.

• Conflict/resource ratio: quotient of the number of con<sup>fl</sup>ict decisions divided by the number of resources. The con<sup>fl</sup>ict/resource ratio changes over time because (i) the number of resources changes, e.g., shutdown of a runway, and (ii) the number of con<sup>fl</sup>ict decisions changes. This metric indicates how effectively resources are utilized as a result of CD&R decisions. The smaller the ratio is, the more effectively resources are utilized in the airport.

• Conflict/vehicle ratio: quotient of the number of con<sup>fl</sup>ict decisions divided by the number of vehicles traveling on the airport surface. Similar to the con<sup>fl</sup>ict/resource ratio, the con<sup>fl</sup>ict/vehicle ratio changes over time because the number of con<sup>fl</sup>ict decisions and vehicles changes. The con<sup>fl</sup>ict/vehicle ratio indicates the airport's capability of handling vehicles with the help of decision support with CD&R. With smaller ratio, the airport has higher capability and more vehicles may be allowed to travel in the airport.

Also of interest is the nature of the dynamic network under realistic conditions. Speci<sup>fi</sup>cally, what types of networks arise during normal and abnormal operations, and can insight be gained into the behavior of the system?

The CD&R decision support function is of great importance to safe and ef<sup>fi</sup>cient airport surface operations. A con<sup>fl</sup>ict between aircraft and/or ground vehicles may be life-threatening, and often cause severe property damage and economic loss. With the ever increasing number of aircraft and ground transportation vehicles, surface operations must be automated with the support of CD&R decision support functions. This research identi<sup>fi</sup>es different types of con<sup>fl</sup>icts in airport surface operations, presents a new approach to model and analyze 4D constraints, and develops the CD&R logic for decision support that takes advantage of properties of complex networks for effective CD&R.

## Acknowledgment

The authors wish to thank partial support for this research by the PRISM Center for Production, Robotics, and Integration Software for Manufacturing & Management at Purdue University. The authors also wish to thank the excellent comments by the reviewers.

Table 3  
Comparison of the three CD&R decision methods.

<table><tr><td>Capability</td><td>Manual CD&amp;R</td><td>Computer integrated CD&amp;R</td><td>DSS with CD&amp;R logic</td></tr><tr><td>Conflict detection</td><td>No</td><td>Manual with automatically generated alerts</td><td>Automated</td></tr><tr><td>Conflict resolution/prevention</td><td>Manual through separation assurance</td><td>Manual</td><td>Automated</td></tr><tr><td>Resource utilization/efficiency of surface operations</td><td>Low</td><td>Medium</td><td>High</td></tr><tr><td>Consideration of dependencies between conflicts/resolutions</td><td>Manual</td><td>No</td><td>Automated through the analysis of conflict networks</td></tr></table>

## References

[1] R. Albert, H. Jeong, A.L. Barabasi, Internet: diameter of the world-wide web, Nature 401 (1999) 130–131.

[2] M. Angeles Serrano, P. De Los Rios, Interfaces and teh edge percolation map of random directed networks, Physical Review E-Statistical, Nonlinear, and Soft Matter Physics 76 (2007) 56–121.

[3] J.A.D. Atkin, E.K. Burke, S. Ravizza, The airport ground movement problem: past and current research and future directions, 4th International Conference on Research in Air Transportation, 2010, pp. 131–138, (Budapest, Hungary) www.icrat.org.

[4] A.L. Barabasi, R. Albert, Emergence of scaling in random networks, Science 286 (1999) 509–512.

[5] G. Bianconi, A.L. Barabasi, Bose–Einstein condensation in complex networks, Physical Review Letters 86 (2001) 5632–5635.

[6] C. Brinton, J. Krozel, B. Capozzi, Improved taxi prediction algorithms for the surface management system, AIAA Guidance, Navigation, and Control Conference and Exhibit, American Institue of Aeronautics and Astronautics, Monterey, CA, 2002.

[7] A. Broder, R. Kumar, F. Maghoul, P. Raghavan, S. Rajagopalan, R. Stata, A. Tomkins, J. Wiener, Graph structure in the web, Computer Networks 33 (2000) 309–320.

[8] X.W. Chen, Prognostics and diagnostics of con<sup>fl</sup>icts and errors with prediction and detection logic, School of Industrial Engineering, Purdue University, West Lafayette, IN, 2009.

[9] X.W. Chen, S.Y. Nof, A decentralized con<sup>fl</sup>ict and error detection and prediction model, International Journal of Production Research 48 (2010) 4829–4843.

[10] X.W. Chen, S.Y. Nof, Interactive, Constraint-Network Prognostics and Diagnostics to Control Errors and Con<sup>fl</sup>icts, Pending U.S. Patent Application, Purdue Research Foundation (PRF) 65241.00.US.

[11] X.W. Chen, S.Y. Nof, Con<sup>fl</sup>ict and error prevention and detection in complex networks, Automatica 48 (2012) 770–778.

[12] V. Cheng, G. Sweriduk, Trajectory design for aircraft taxi automation to bene<sup>fi</sup>t trajectory-based operations, Asian Control Conference, IEEE, Hong Kong, China, 2009, pp. 99–104.

[13] G.L. Dillingham, in: U.S.G.A. Of<sup>fi</sup>ce (Ed.), Runway Safety: Progress on Reducing Runway Incursions Impeded by Leadership, Technology, and Other Challenges (Report # GAO-08-481T), U.S. Government Accounting Of<sup>fi</sup>ce, Washington, D.C., 2008.

[14] J. Dwyer, S.J. Landry, Separation assurance and collision avoidance concepts for the next generation air transportation system, Human–Computer Interaction International Conference, Springer, San Diego, CA, 2009, pp. 748–757.

[15] P. Erdos, A. Renyi, On random graphs, Publicationes Mathematicae Debrecen 6 (1959) 290–291.

[16] P. Erdos, A. Renyi, On the evolution of random graphs, Magyar Tudományos Akadémia Matematica Kutato International Kozlony 5 (1960) 17–61.

[17] P. Erdos, A. Renyi, On the strength of connectedness of a random graph, Acta Mathematica Academiae Scientiarum Hungaricae 12 (1961) 261–267.

[18] K.M. Guptaa, A.R. Montazemib, A connectionist approach for similarity assessment in case-based reasoning systems, Decision Support Systems 19 (1997) 237–253.

[19] R.C. Hicks, The no inference engine theory — performing con<sup>fl</sup>ict resolution during development, Decision Support Systems 43 (2007) 435–444.

[20] H. Idris, R. Vivona, J.-L. Garcia-Chico, D. Wing, Distributed traf<sup>fi</sup>c complexity management by preserving trajectory <sup>fl</sup>exibility, Proceedings of the 26th AIAA/IEEE Digital Avionics Systems Conference, 2007, (pp. 2.B.6-1-3.B.6-13).

[21] Y.C. Jung, G.A. Monroe, Development of surface management system integrated with CTAS arrival tool, in, AIAA 5th Aviation, Technology, Integration, and Operations Conference, American Institute of Aeronautics and Astronautics, Arlington, VA, 2005.

[22] S.J. Landry, A. Lagu, J. Kinnari, State-based modeling of continuous human-integrated systems: an application to air traf<sup>fi</sup>c separation assurance, Reliability Engineering and Safety Science 95 (2010).345-353.

[23] M.E.J. Newman, A.L. Barabasi, D.J. Watts, The Structure and Dynamics of Networks, Princeton University Press, Princeton, N.J., 2006.

[24] R.A. Paielli, H. Erzberger, D. Chiu, K. Heere, Tactical con<sup>fl</sup>ict alerting aid for air traf<sup>fi</sup>c controllers Journal of Guidance Control and Dynamics 32 (1) (2009) 184–193

[26] R. Solomonoff, A. Rapoport, Connectivity of random nets, Bulletin of Mathematical Biophysics 13 (1951) 107–117.

[25] D.J.D.S. Price, Networks of scienti<sup>fi</sup>c papers, Science 149 (1965) 510–515.

[27] H. Swenson, T. Hoang, S. Engelland, D. Vincent, T. Sanders, B. Sanford, K. Heere, Design and operational evaluation of the traf<sup>fi</sup>c management advisor at the Fort Worth Air Route Traf<sup>fi</sup>c Control Center, 1st USA/Europe Air Traf<sup>fi</sup>c Management R&D Seminar, EUROCONTROL, Saclay, France, 1997.

[28] K.P. Sycara, Machine learning for intelligent support of con<sup>fl</sup>ict resolution, Decision Support Systems 10 (1993) 121–136.

[29] S.W. Yoon, S.Y. Nof, Demand and capacity sharing decisions and protocols in a collaborative enterprise network, Decision Support Systems 49 (2010) 442–450.

[30] S.W. Yoon, J.D. Velasquez, B.K. Partridge, S.Y. Nof, Transportation security decision support system for emergency response: a training prototype, Decision Support Systems 46 (2008) 139–148.

[31] Q. Zheng, Y. Zhao, B. Capozzi, Time-of-arrival taxi conformance monitoring for surface operations, Journal of Guidance Control and Dynamics 34 (2011) 750–760.

![](/api/attachments/PA7W7MGE/fulltext/images/a9fe830a6f17d20d97fdbccab7f5460cced79ae1e11e73161bc4cb40ea01383b.jpg)

Steven J. Landry, Ph.D., is Associate Professor and Associate Head in the School of Industrial Engineering, Purdue University. His Ph.D. is in Industrial and Systems Engineering from Georgia Tech, his S.M. is in Aeronautics and Astronautics from MIT, and his B.S. is in Electrical Engineering from WPI. He was formerly an aerospace engineer at NASA's Ames Research Center and a USAF C-141B pilot with over 2500 <sup>fl</sup>ight hours. He conducts research and publishes on systems engineering and human factors, primarily within the air transportation domain. He is co-author of the forthcoming textbook Introduction to Human Factors and Ergonomics for Engineers, 2nd Edition, and has written three book chapters on human factors in aviation. He is a member of IEEE, AIAA, IIE, and HFES.

![](/api/attachments/PA7W7MGE/fulltext/images/17269322055713bffa9c1cff0abec33ff263e0a825adc8a614ed4ac295953252.jpg)

Xin W. Chen, Ph.D., is an Assistant Professor of Industrial and Manufacturing Engineering at Southern Illinois University Edwardsville. His research focuses on network- and knowledge-centric collaborative control. He received a B.S. in Mechanical Engineering from Shanghai Jiao Tong University, an M.S. and a Ph.D. in Industrial Engineering from Purdue University. He is a member of the IIE (Institute of Industrial Engineers), INFORMS (Institute for Operations Research and Management Sciences), and Sigma Xi, The Scienti<sup>fi</sup>c. He is a Subject Matter Expert of the Knowledge Management Laboratory at the Collaborative Agent Design Research Center.

![](/api/attachments/PA7W7MGE/fulltext/images/b81019af8e3c08dafed4d9bacb9fdf58700859c986ed2eb30904ef04e50beb30.jpg)

Shimon Y. Nof, PhD, DHC, is Professor of Industrial Engineering. Purdue University, and held visiting positions at MIT and at universities in Chile, EU, Hong Kong, Israel, Japan, and Mexico. He is the Director of the NSF-industry supported PRISM Center for Production, Robotics and Integration Software for Manufacturing & Management (established 1991) and its associated PGRN, PRISM Global Research Network; recent Chair of the IFAC Coordinating Committee “Manufacturing & Logistics Systems”, recent President of IFPR (International Federation of Production Research), Fellow of the IIE (Institute of Industrial Engineers), and inaugural member of Purdue's Book of Great Teachers (1999). He is the author, co-author and editor of twelve books, including the Handbook of Industrial Robotics 1st and

2nd editions, the International Encyclopedia of Robotics (both winners of the “Most Outstanding Book in Science and Engineering”,) Information and Collaboration Models of Integration, Industrial Assembly, and Springer Handbook of Automation. His current research thrusts are collaborative control theory and networked robotics
