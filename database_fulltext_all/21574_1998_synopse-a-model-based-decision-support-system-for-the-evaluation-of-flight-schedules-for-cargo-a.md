---
otero_id: 21574
otero_key: "XKCQ83SX"
title: "SYNOPSE: a model-based decision support system for the evaluation of flight schedules for cargo airlines"
authors: "J. Antes; L. Campen; U. Derigs; C. Titze; G.-D. Wolle"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00027-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# SYNOPSE: a model-based decision support system for the evaluation of flight schedules for cargo airlines

J. Antes <sup>a</sup>, L. Campen <sup>a</sup>, U. Derigs <sup>a,)</sup>, C. Titze <sup>b</sup>, G.-D. Wolle <sup>b</sup>

<sup>a</sup> WINFORS, UniÕersity of Cologne, Pohligstr. 1, 50969 Koln, Germany ¨ Lufthansa Cargo AG, 60546 Frankfurt, Germany

Received 30 November 1997; revised 31 January 1998; accepted 28 February 1998

## Abstract

The ability to evaluate flight schedules, with respect to cost, revenue and contribution to profit, is essential for cargo airlines to respond properly to changing environments in this highly competitive and consumer-oriented market. In this paper, we introduce SYNOPSE, our model-based decision support system for the evaluation of flight schedules for cargo airlines, by describing the underlying planning situation, the data model and the decision models used, and the implementation, i.e., the development process, as well as the architecture. A small example illustrates the high complexity of the analysis process and the supporting qualities of our decision-support system DSS .Ž . q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Model-based decision-support system DSS ; Airline management; Evaluative models; ImplementationŽ .

## 1. Introduction

A cargo airline offers the conceptually simple service to transport a certain amount of goods from an origin to a destination within a certain time interval at a given price. For this purpose, the airline keeps a fleet of aircrafts and<sup>r</sup>or leases capacities from other companies, especially ground capacities for transporting goods to, from, and between airports.

The tactical planning problem of such airlines is to design a weekly flight schedule which allows the most Ž . profitable service of the unknown market-demand for the next period—the next six months in general—using the available capacities, i.e., aircrafts, ground transportation, and handling capacities at the airports.

So far, an algorithmic and fully automated generation of flight schedules seems to be infeasible, due to the extremely high complexity of the planning situation. Flight planning, as it is described above, has to take into account service intervals, is sequentially interdependent with other decisions on building rotations for singleŽ . aircrafts and crew assignments and, thus, the whole decision complex is beyond the possibility of becoming fully structurable into a complete and efficiently computable model 2 . Therefore, this planning and design <sup>w</sup> <sup>x</sup> problem can only be solved by an interaction between planner and computer, i.e., by a so-called Decision-Support System DSS 14 . Here, the use of evaluative models which allow the analysis of a plan with respect toŽ . <sup>w</sup> <sup>x</sup> different criteria seems to be an adequate approach for several reasons. It is quite common to design a new schedule by altering the plan, which is the basis for operations of the present period, by adapting service capacities to projected changes in customer demands and<sup>r</sup>or changes in fleet and airport characteristics. Moreover, the ability to evaluate a solution is a necessary prerequisite in a systematic search procedure for constructing solutions.

In this paper, we describe such a DSS called ‘SYNOPSE’ which has been developed at WINFORS Ž . University of Cologne in collaboration with the planning division of Lufthansa Cargo AG. SYNOPSE stands for ‘System zur Netzoptimierung und Planung Strategischer Entscheidungen’. According to the DDM-paradigm <sup>w</sup> <sup>x</sup> 12 of the DSS concept, the architecture of any specific DSS can be described by three modules: the data, model, and dialog components.

The data component of a DSS consists of a database and a database management system, with the database containing all the factual information necessary to describe a concrete planning situation. The model component contains one or more quantitative planning models associated with appropriate solvers. Here, a planning model is defined as a ‘constructive problem description’ by which the relationships between courses of actions and consequences are translated into the form of a ‘mathematical<sup>r</sup>computational problem’. The combination of models, data, and solvers is controlled by the model management system. The dialog component can be best interpreted as the language of interaction between planner and system, i.e., a so-called action-language describing the planners actions and a so-called presentation-language describing the computer’s presentation of results from model calculations 11 .<sup>w</sup> <sup>x</sup>

Given an estimated amount of service requests and a candidate flight schedule, our models calculate the maximal possible contribution to profit which can be obtained by fulfilling service requests according to the flight schedule. Thus, although the approach taken by SYNOPSE is evaluative, i.e., no plans are suggested, the models we use are optimization models which, given market-demand, transportation, and handling capacities, construct an optimal assignment between demand and capacities. To determine this assignment and its value complex mathematical programming problems are solved.

A system allowing such calculations can be used for analysis in different ways: 1 Based on a fixed demand,Ž . different flight schedules can be compared with respect to their contribution to profit. 2 The robustness andŽ . adaptability of a schedule with respect to changes in service requests can be evaluated through simulation. 3Ž . Bottlenecks with respect to transportation capacities offered by a flight schedule can be identified. 4 PotentialsŽ . for creating higher contribution to profit through the acquisition of additional market-demand can be identified.

The paper is organized as follows. In Section 2, we describe the planning situation, i.e., we represent the relevant concepts or object classes in the planner’s world of discourse and based on this conceptual schema we describe the logical relational schema of the SYNOPSE-database. In Section 3, we describe a family ofŽ . optimization problems which are elements of the model base. These models reflect planning problems at different levels of detail used at different stages in the planning process, i.e., we state purely volume-oriented models, neglecting time constraints, as well as a flexible model, taking into account these time considerations and restrictions to ground handling. In Section 4, we briefly describe the implementation of the DSS, its software and hardware components, and the development strategy. In Section 5, we finally describe the usage of SYNOPSE in a planning situation, i.e., we state the basic information needs that arise for a planner who is confronted with the evaluation of a schedule and the associated analysis strategies.

## 2. The planning situation: data model

From the verbal description of an air-cargo service given in the introduction we can identify three basic entity types in our world of discourse:

AIRPORT, with a three letter identifier and a name

PRODUCT, with an identifier and a description and

TIME, with the only attribute time being a tuple composed of three domains:

day of week <sup>s</sup>  4 1, . . . ,7

```txt
hour = {0, . . . , 23}
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$minute = \{0, \ldots, 59\}.$
</div>

Unlike the situation a passenger airline faces, the goods transported by a cargo airline are extremely heterogeneous chapter 11 of Ref. 15 and chapter 12 of Ref. 7 with a precise description of all units to beŽ <sup>w</sup> <sup>x</sup> <sup>w x</sup>. transported being neither available during the planning phase nor relevant. Therefore, a catalogue of relevant attributes, like standard, express, hazardous, etc., has been developed to identify product types which require different handling. In that respect, PRODUCT is the class of all conceptually different product types and each good to be transported is assigned to at least one specific type.

The market-demand can be described as a set of estimated or booked service requests. Such a request has several attributes, with the origin and destination airport being the dominant characteristic. Therefore, these request objects are commonly referred to as ‘O&Ds’ or ‘O&D-pairs’. Conceptually, the object class OD can be modelled as a complex 5-ary recursive relationship-type between: Ž .

AIRPORT, playing the role of an origin and a destination, respectively;

TIME, playing the role of an availability and due time, respectively; and

PRODUCT.

with the additional attributes giving the quantity measured in kilogram and the yield or freight rate given in US\$ per kilogram.

Note that for each O&D, we require the origin to differ from the destination, as well as a positive difference between the due time and availability. Also, we do not consider the ‘volume’ criterion of a request in this planning phase.

The flight schedule, on the other hand, can be described as a set of so-called legs. Here, a leg is a direct flight between two airports offered at the same time every week during the planning period. In our schema we, model the object class LEG as a 4-ary recursive relationship-type between:Ž .

AIRPORT, playing the role of an origin from and the destination to , respectively, and Ž . Ž .

TIME, playing the role of a departure and arrival time, respectively, with the additional attributes of a flight designator for identification, the capacity of the leg measured in kilogram and the operating cost of the leg measured in US\$ per kilogram. Note that we require for each leg different origin and destination airports and a positive difference between arrival and departure time.

There are certain incompatibilities between product-types and legs, i.e., an express item should, in general, not be transported on leased capacities, etc. The validity of a leg, with respect to the different product types is modelled by a relationship-type FEASIBLE, associating entities from LEG and PRODUCT, i.e., every relationship element identifies a feasible assignment. The relevant information reflecting the ground handling, i.e., the import, export and transfer of the goods at the airports is modelled by a relationship-type HANDLING between the entity types AIRPORT and PRODUCT with the following attribute pairs:

Ž . imp\_time, imp\_cost giving the time and cost for import of a certain good, i.e., handling at the destination airport

Ž . exp\_time, exp\_cost giving the time and cost for export of a certain good, i.e., handling at the origin airport

Ž . trans\_time, trans\_cost giving the time and cost for transfer at an intermediate airport, i.e., unloading and reloading the goods

with times measured in minutes and cost measured in US\$ per kilogram.

Transportation, either real or planned, can now be described by an association between the object types LEG and OD, i.e., a relationship type LEG\_OD, reflecting the usage of a certain leg for a certain O&D by an attribute giving the amount measured in kilogram.

![](/api/attachments/XKCQ83SX/fulltext/images/53078230e443d835697edf2d4bc94d806fa7b216ab3b4aeac80dad057a868a39.jpg)  
Fig. 1. The entity relationship schema.

Given an instantiation of LEG\_OD, the contribution to profit can be derived by a simple arithmetical operation. It is the decision model which describes the optimal instantiation, i.e., an optimal choice of amount-values for the entities from LEG<sup>=</sup>OD.

Fig. 1 gives the graphical representation of our conceptual data schema, using the common symbols of the entity–relationship pp. 39–88 of Ref. 8 model. Taking into consideration the complexities of the relation-Ž <sup>w</sup> <sup>x</sup>. ship-types, which are unrestricted in all cases, the associated relational schema can be constructed via a standard transformation, i.e., introducing a basic relation for each entity-type and each relationship-type, introducing for relations representing relationship-types all the primary keys from associated entity types as foreign keys, and describing referential integrity conditions appropriately pp. 172–177 of Ref. 8 .Ž <sup>w</sup> <sup>x</sup>.

Note that in the logical data model, i.e., the relational schema, we use a standardized time description and represent all time-associations as attributes, i.e., we do not introduce a base relation TIME. This is a common approach.

## 3. The problem description: decision models

The following description of the evaluation of a flight schedule is based on the data schema given in Section 2, i.e., we assume that an instantiation of LEG, OD and FEASIBLE is given. Note that in the following, we use the notation which is commonly used in mathematical programming, i.e., we write oŽ . od , instead of the relational notation OD.o, for referring to the value of attribute o for an od-tuple. Also, we use the one-letter aliases given in Table 1, and denote the only derivable attribute of the schema, the amount for the LEG\_OD-type and base relation by x, i.e., x lŽ . ,od is the amount in kilogram of ‘good’ od<sup>g</sup>OD which is transported over leg l<sup>g</sup>L.

Table 1  
Aliases used in optimization models

<table><tr><td>Concept name</td><td>Alias</td></tr><tr><td>AIRPORT</td><td>A</td></tr><tr><td>LEG</td><td>L</td></tr><tr><td>FEASIBLE</td><td>F</td></tr><tr><td>PRODUCT</td><td>P</td></tr><tr><td>Yield</td><td>y</td></tr><tr><td>Cost</td><td>c</td></tr><tr><td>Flight designator</td><td>f</td></tr><tr><td>Capacity</td><td>u</td></tr><tr><td>Destination</td><td>d</td></tr><tr><td>Origin</td><td>o</td></tr></table>

Note that for the first two models, we neglect any time restrictions, making these models suitable for analyzing strategic aspects, i.e., questions concerning the capacitative balance between market-demand and fleet structure, the potentials for strategic alliances, etc.

Our first model is an immediate translation of the description given in Section 2, specifying integrity constraints for the amount-attribute through restrictions on x and introducing the contribution to profit value as objective function.

The first two models represent the planning alternatives as arc-flows in a network, with the airports being the nodes and the legs defining the arcs. While in the classical transportation problem the optimal distribution of one homogenous good is considered, here we have to consider different commodities, leading to the so-called multicommodity network flow problem chapter 17 of Ref. 1 .Ž <sup>w</sup> <sup>x</sup>.

In our first model, these commodities are the different O&Ds in OD, thus leading to the definition of the above decision variable.

Model 1. Multi-ODP-Commodity Flow Formulation MCF-ODP : Ž .

$$
\max \sum_ {\mathrm{od} \in \mathrm{OD}} \left(\sum_ {l \in L: o (l) = o (\mathrm{od})} y (\mathrm{od}) \cdot x (l, \mathrm{od}) - \sum_ {l \in L} c (l) \cdot x (l, \mathrm{od})\right)\tag{1}
$$

subject to:

$$
\sum_ {l \in L: o (l) = i} x (l, \mathrm{od}) - \sum_ {l \in L: d (l) = i} x (l, \mathrm{od}) \left\{ \begin{array}{l l} \leq q (\mathrm{od}) & \quad i = o (\mathrm{od}) \\ \geq - q (\mathrm{od}) & \quad i = d (\mathrm{od}) \\ = 0 & \quad \text { else } \end{array} \right. \quad \forall   i \in A, \mathrm{od} \in \mathrm{OD}\tag{2}
$$

$$
\sum_ {\mathrm{od} \in \mathrm{OD}} x (l, \mathrm{od}) \leq u (l)
$$

$$
\forall l \in L\tag{3}
$$

$$
\forall l \in L, \mathrm{od} \in \mathrm{OD}\tag{4}
$$

$$
x (l, \mathrm{od}) = 0
$$

$$
\forall l \in L, \mathrm{od} \in \mathrm{OD}:
$$

$$
(p (\mathrm{od}), l) \notin F\tag{5}
$$

Here, the objective function calculates the difference between total yield and operating cost. Constraints 2Ž . are the so-called flow balancing constraints, which restrict the amount of flow for any O & D to, at most, qŽ . od , and control that for each O&D the amount leaving oŽ . Ž . Ž . od is arriving at d od . Constraints 3 control that the usage of a leg does not violate the capacity constraint while 4 allows only nonnegative amounts to beŽ . transported and disallows infeasible association of O&Ds to legs.

In the second model, we work on an aggregated view. For every leg, we consider the OD-entities with the same destination and product as one object, i.e., in relational terms, we build the projection $\mathrm { D P } = \mathrm { P R O J } _ { \langle d , p \rangle } \mathrm { O D }$ and assign a variable x to each tuple or entity in $\mathrm { D P } \times L$ . Thus, we define:

x l Ž .,dp <sup>s</sup> amount in kilogram of product $p ( { \mathrm { d p } } )$ with destination $d ( \mathrm { d p } )$ transported on leg l.

With this aggregation, all O&Ds with the same destination and product are treated as one commodity.

To ease notation, we introduce two index sets.

$$
\mathrm{DP} (\mathrm{od}) = \left\{\mathrm{dp} \in \mathrm{DP} | d (\mathrm{od}) = d (\mathrm{dp}) \wedge p (\mathrm{od}) = p (\mathrm{dp}) \right\}
$$

gives, for every O&D, the associated entity in the projection while

$$
\mathrm{OD} (\mathrm{dp}) = \left\{\mathrm{od} \in \mathrm{OD} | d (\mathrm{od}) = d (\mathrm{dp}) \wedge p (\mathrm{od}) = p (\mathrm{dp}) \right\}
$$

gives the inverted view, i.e., it gives for every object in DP the entities from OD which have been aggregated. Model 2. Multi-DP-Commodity Flow Formulation MCF-DP Ž .

$$
\max \sum_{\text{od}\in \text{OD}}\left(\sum_{\substack{l\in L,\text{dp}\in \text{DP} (\text{od}):\\ o(l) = o(\text{od})}}x(l,\text{dp}) - \sum_{\substack{l\in L,\text{dp}\in \text{DP} (\text{od}):\\ d(l) = o(\text{od})}}x(l,\text{dp})\right)y(\text{od}) - \sum_{l\in L,\text{dp}\in \text{DP}}c(l)\cdot x(l,\text{dp})\tag{6}
$$

subject to:

$$
\sum_ {l \in L: o (l) = i} x (l, \mathrm{dp}) - \sum_ {l \in L: d (l) = i} x (l, \mathrm{dp}) \geq - \sum_ {\mathrm{od} \in \mathrm{OD} (\mathrm{dp})} q (\mathrm{od}) \quad \begin{array}{c} \forall i \in A, \mathrm{dp} \in \mathrm{DP} \\ i = d (\mathrm{dp}) \end{array}\tag{7}
$$

$$
0 \leq \sum_ {l \in L: o (l) = i} x (l, \mathrm{dp}) - \sum_ {l \in L: d (l) = i} x (l, \mathrm{dp}) \leq \sum_ {\mathrm{od} \in \mathrm{OD} (\mathrm{dp}):} q (\mathrm{od}) \quad \begin{array}{c} \forall i \in A, \mathrm{dp} \in \mathrm{DP}: \\ i \neq d (\mathrm{dp}) \end{array}\tag{8}
$$

$$
\sum_ {\mathrm{dp} \in \mathrm{DP}} x (l, \mathrm{dp}) \leq u (l)
$$

$$
\forall l \in L\tag{9}
$$

$$
x (l, \mathrm{dp}) \geq 0
$$

$$
\forall l \in L, \mathrm{dp} \in \mathrm{DP}\tag{10}
$$

$$
x (l, \mathrm{dp}) = 0
$$

$$
\forall l \in L, \mathrm{dp} \in \mathrm{DP}:
$$

$$
(p (\mathrm{dp}), l) \notin F\tag{11}
$$

The advantage of the DP-formulation over the ODP-formulation is the smaller size of an instantiation and, thus, the possibility to solve larger problem instances in shorter time. Yet, one has to pay for this advantage with the loss of ‘routing information’. Thus, the application of the second formulation is recommendable if flight schedules are evaluated on their contribution to profit-value only. If more information about the routing, the usage of legs, etc., is required, an associated ODP-solution has to be constructed. In our system, this is done by a routine ‘ROUTER’ which, given a DP-solution, pushes odp-units from their o-nodes to their d-nodes. Note that given a DP-solution, the ODP-solution need not be unique. A detailed description of the straightforward pushing process is beyond the scope of this paper.

Computational experiences have shown that the two-phase approach, i.e., solving the DP-formulation followed by ROUTER, is not only more efficient, with respect to memory-requirements, but also consumes less CPU-time than the single-phase ODP-approach.

Yet, for larger instances and<sup>r</sup>or the necessity to incorporate more constraints into the model, i.e., considering time-windows for the demand and cost as well as duration for ground handling, formulations based on the multicommodity-arc-flow model become intractable, and so called path-flow-formulations should be used Žchapter 17 of Ref. 1 .<sup>w</sup> <sup>x</sup>.

Path-models are based on the obvious fact that any unit transported from an origin to a destination has taken a sequence of legs possibly only one leg , a so-called path or itinerary connecting the origin with theŽ . destination. Note that in a solution to the problem for every od $\mathbf { \tau } \in \mathrm { O D }$ , the amount which is transported is usually split over several itineraries. These paths can be re- constructed through pushing routines similar to ROUTER. Ž .

If in the path formulation all possible itineraries are assumed to be given, then the optimization problem is simply to select the optimal combination of paths, which leads to a standard linear program. The advantage of this approach is the possibility to consider rather general and complicated constraints for feasibility of transportation in the path-construction phase, i.e., keeping this knowledge away from the optimization model, thereby reducing the complexity of the optimization phase and allowing the same standard LP- solution Ž . procedure for a wider range of different planning situations.

Moreover, this approach allows for scaling, i.e., it is not necessary to construct all possible paths. Working with a ‘promising subset’ of profitable paths only, reduces the size of the problem instance but may lead to solutions which are not optimal in general, yet highly acceptable in quality. Finally, an approach called column-generation allows the generation of feasible paths on the run during optimization and, thus, keeps the problem-size manageable throughout the optimization process 5,6 . <sup>w</sup> <sup>x</sup>

In the following, we first describe the concept of itineraries or paths more precisely.

A path for an od<sup>g</sup>OD is a sequence $s = ( l _ { 1 } , \ldots , l _ { n ( s ) } )$ of legs $l _ { i } \in L , n ( s ) \geq 1$ , with the following property

$$
\begin{array}{l} o (l _ {1}) = o (\mathrm{od}) \\ d (l _ {i}) = o (l _ {i + 1}) \qquad i = 1, \dots , n (s) - 1 \\ d (n (s)) = d (\mathrm{od}) \end{array}
$$

A path is called od-feasible if additional requirements are fulfilled, which vary with the problem definition. Here, we consider several types of constraints:

$$
\begin{array}{l l} \text {availability - time} & \text {avail (od) + exp\_time (o( od),p( od))\leq dep(l_{1})} \\ \text {due - time} & \text {arr (l(s)) + imp\_time (d( od),p( od))\leq due( od)} \\ \text {transfer - time} & \text {arr (l_{i}) + trans\_time (d(l_{i}),p( od))\leq dep(l_{i+ 1}) for i = 1,\ldots,n(s) - 1} \\ & \text {if f(l_{i})\neq f(l_{i+ 1}); i.e., the aircraft changes from l_{i} to l_{i+ 1}} \\ \text {product feasibility} & \left(l_{i}, p(\mathrm{od})\right)\in F. \end{array}
$$

For every od $\mathbf { \tau } \in \mathrm { O D }$ , we denote by SŽ . od the set of od-feasible itineraries. Note that a path may be feasible for many different O&Ds. In our model, we have to distinguish these roles and consider multiple copies of the same path assigned to different O&Ds.

Given an itinerary $s \in S ( \mathrm { o d } )$ , we can easily calculate the operating cost $c ( s )$ for transporting one unit Ž . kilogram on this path:

$$
\begin{aligned} c(s) = \sum_{i = 1}^{n(s)}c(l_{i}) + \exp \_ \text{cost}(o(\mathrm{od}),p(\mathrm{od})) \\ & + \sum_{\substack{i = 2:\\ f(l_{i - 1})\neq f(l_{i})}}^{n(s) - 1}\text{trans\_cost}(o(l_{i}),p(\mathrm{od})) + \text{imp\_cost}(d(\mathrm{od}),p(\mathrm{od})) \end{aligned}
$$

For the following model, we introduce for every $s \in S ( \mathrm { o d } )$ , od $\mathbf { \tau } \in \mathrm { O D }$ a decision-variable $x ( s ) = \mathrm { a m o u n t }$ Ž  in kilogram of od transported via. s.

Moreover, we define an indicator-variable : $L \times S \to \{ 0 , 1 \}$

$$
\delta (l, s) := \left\{ \begin{array}{l l} 1 & \text { if   leg } l \text { is   contained   in   path } s \\ 0 & \text { else } \end{array} \right.
$$

Then, the model for constructing a feasible combination of paths, giving maximal contribution to profit is as follows.

Model 3. Multi-Commodity Path Flow Formulation MCF-PATHŽ .

$$
\max \sum_ {\mathrm{od} \in \mathrm{OD}} \sum_ {s \in S (\mathrm{od})} (y (\mathrm{od}) - c (s)) \cdot x (s)\tag{12}
$$

subject to:

$$
\sum_ {s \in S (\mathrm{od})} x (s) \leq q (\mathrm{od})
$$

$$
\forall \mathrm{od} \in \mathrm{OD}\tag{13}
$$

$$
\sum_ {\mathrm{od} \in \mathrm{OD}} \sum_ {s \in S (\mathrm{od})} \delta (l, s) \cdot x (s) \leq u (l)
$$

$$
\forall l \in L\tag{14}
$$

$$
x (s) \geq 0
$$

$$
\forall s \in S (\mathrm{od}), \mathrm{od} \in \mathrm{OD}\tag{15}
$$

From an optimal solution to MCF-PATH, the following information can be obtained in a quite straightfor-Ž . ward way: a for each O & D, the set of itineraries used for transporting together with the associated amount,Ž . the total amount which is transported, as well as the amount which is left at the origin together with the associated revenue; b for each leg, the set of all O & Ds and the associated amount transported over the leg; c Ž . Ž . for each airport, the amounts of goods originating<sup>r</sup>destining<sup>r</sup>transferring; and d for each pair of airports, theŽ . amount of goods transported between them.

Also, the optimal dual solution gives important and helpful information to be used in the analysis: a TheŽ . value of the dual variable $\omega _ { l }$ for constraints 14 gives the increase of the objective function value per unitŽ . increase of the capacity $u ( l )$ Ž .of leg l. b The value of the dual variable $\sigma _ { \mathrm { o d } }$ Ž . for constraints 13 gives the increase of the objective function value per unit increase of the demand qŽ . Ž .od . c The reduced cost value $r ( s )$ for an itinerary $s \in S ( \mathrm { o d } )$ , defined by $r ( s ) = ( y ( \mathrm { o d } ) - c ( s ) ) - ( \sigma _ { \mathrm { o d } } + \Sigma _ { l \in L } \delta ( l , s ) \omega _ { l } ) .$ , gives for each itinerary which is not used more precisely for each non basic variableŽ Ž .. Ž .x s the amount by which the yield freight rate of this od has to be increased in order to make transportation of one unit of this od using s profitable.

Applying column generation to solve MCF-PATH, the reduced cost values for itineraries, which so far have not been introduced into the LP-model and, thus, could not be considered for optimization, indicate optimality of the LP-solution or potential improvements through the introduction into the LP-model. For a specific od, the k most promising paths in SŽ . od to be introduced into the LP-model can be constructed by computing the k-shortest constrained paths betweenŽ . o and d. A detailed description of the column-generation technique for solving MCP-PATH is beyond the scope of this paper. We will report on our implementation in another paper.

## 4. Implementation: development and architecture

In this section, we describe the implementation of SYNOPSE. We briefly discuss the development process, and outline its technological basis with the hardware and software tools, etc.

The work on SYNOPSE was initiated by the demand of a major scheduled cargo airline to evaluate the consequences of a very specific and complex change in their regular schedule, a task for which so far used manual and informal, expertise-based procedures and processes seemed to be not reliable enough. At the beginning of the project, a significant amount of time and effort was invested to get a precise definition of the concepts and business rules used in the cargo industry, i.e., to re- construct the assertions and termsŽ . communicated in the business language into a formal data schema describing the architecture of the database. Then, a comprehensive data analysis led to the specification of attributes and the identification of the information sources.

What is commonly called the ‘data problem’, e.g., the situation where relevant data is not available in the right quality, in the right level of detail, etc., turned out to be crucial throughout the whole project and has caused many ‘modeling compromises’. Also, at the beginning, the managers could not sufficiently describe their expectation for the functionality of the supporting system, mainly because of their lack of experience with model-based analysis.

Because of these two circumstances, an iterative development process p. 74 of Ref. 14 , through aŽ <sup>w</sup> <sup>x</sup>. sequence of prototypes, was the only feasible approach. In this early phase, we used the model MCF-ODP to evaluate the modeling approach in general, i.e., to demonstrate the consequences of incorporating constraints into the model and<sup>r</sup>or aggregating the model due to missing data, insufficient accuracy of data, etc. Quite a substantial discussion concerned the right definition of ‘operating cost’ for transporting all goods on individual legs and the handling of cargo at airports. So, for instance, our first models produced solutions, where a huge amount of freight was routed through very small airports. This was considered as inappropriate, because of the airports’ limited handling capacities. Therefore, we introduced into the model the concept of ‘hubs’ in a different manner from the conventional use within the airline company, i.e., we distinguished between airports for which transfer is possible<sup>r</sup>not possible.

For representing the models, we used the mathematical programming language AMPL 9 as a generator of<sup>w</sup> <sup>x</sup> the input to the linear programming solver CPLEX 4 . Using a mathematical programming language like <sup>w</sup> <sup>x</sup> AMPL was a necessary requisite to allow the iterative development and the many experiments with different model alternatives obtained through introduction<sup>r</sup>dropping of constraints in a timely manner, etc. After all, using AMPL was a success factor. With conventional modeling, i.e., the individual programming of matrix-generators, rapid prototyping would not have been possible.

The experience with the first prototypes resulted in the following insights for the management. a TheŽ . analyst’s first idea to evaluate and analyze schedules based on standardized and detailed reports is impractical, and representations allowing different uses at different levels of detail, as well as the support of different analytical processes with different views, is necessary. b The system should be able to assist evaluations at Ž . different stages during the entire planning process and should therefore also be able to work at a disaggregated level incorporating rather complex constraints

Due to the fact that the scheduling experts, because of the novelty of the approach, were not able to express a standard model for an analyzation process, we designed the presentation logic of SYNOPSE around the views which a planner can define for a given schedule, using these views as dimensions or directions during the analysis and allowing operations on these views. Thus, our development is very much in the flavor of the generally suggested ROMC-approach 3,13 . The analytical capabilities of SYNOPSE are described in more<sup>w</sup> <sup>x</sup> detail in Section 5.

Because of the analysts’ experience with PCs especially the Windows operating system and various end-userŽ tools, like spreadsheets and word processors the front end of SYNOPSE had to be implemented in a PC. environment. To allow a flexible workflow management, the use of UNIX-workstations for solving large scale models, as well as a future connectivity to corporate database servers, we designed SYNOPSE using the client–server architecture concept, which allows the distribution of functionality. In Fig. 2 we display the architecture of SYNOPSE.

We implemented the dialog and the data component on the client using MS ACCESS for Windows 3.11. For the model component, we used the modeling language AMPL together with the LP solver CPLEX. The AMPL–CPLEX pair was placed on the server together with the optimization models. During the development phase, we used an IBM RS 6000 model 540 with AIX 3.2.5 for the server. For the analysts, we combined server and client on a Pentium 166-MHz PC in order to have a stand-alone system.

![](/api/attachments/XKCQ83SX/fulltext/images/ebb949ed0c1c003eaa8e3818b95a9097cbc613baf6a7df331d0dba1f18d0b4a4.jpg)  
Fig. 2. The architecture of SYNOPSE.

## 5. Usage: analyzing freight flows and schedules

SYNOPSE is based on the conceptual idea that the evaluation of a given flight schedule can be performed on the basis of an associated optimal freight routing, i.e., the investigation of an associated routing giving maximal contribution to profit for a fixed estimated demand. Confronted with such an optimal freight routing, the analyst will after checking the plausibility of the solution by comparing the proposed routing with his experience, i.e.,Ž routings actually implemented in operation search for weaknesses and opportunities of the given schedule, as. well as investigate the sensitivity of the schedule’s quality with respect to changes in the demand. On the basis of the results of this first analysis, he will formulate changes in the schedule and<sup>r</sup>or in the demand pattern leading to a modification of the problem instance which has to be solved for further analysis.

Confronted with a schedule, the planner can take different views associated with the basic object classes legs, O&Ds, and airports, respectively, which can be thought of as defining the dimensions in a conceptual search space.

Weaknesses, like a capacity bottleneck or a capacity surplus, as well as opportunities, like profitable O&Ds, can be identified by studying critical objects from these classes, i.e., single legs, O&Ds, and airports, which themselves are identified through extreme indicator values in the model’s optimal solution. Here, the most important indicators are the leg’s load factors and the O&D’s production levels as well as certain values from the LP-dual. Here, the load factor of a leg l is the percentage of all units transported over l compared to total capacity. The production level of an O&D is the percentage of the amount which is actually transported compared to the demand quantity. Thus, to enable a determined investigation of a given schedule we provide listings of critical legs and critical O & Ds as starting points for the analysis.

Obviously, a completely used leg, i.e., a leg with a load factor of 100%, may indicate a capacity bottleneck. There are two ways of supporting the analysis of this fact. One way is to check the load factors on all parallel legs, i.e. those legs that are candidates for alternatively transporting the O & Ds transported on this leg. If every parallel leg has a load factor of 100% and one of the associated O&Ds is not completely produced, then the leg is a bottleneck and increasing the capacity between the origin and destination airport introducing an additional parallel leg, for instance, may increase total yield and contribution to profit. A second indicator for the relative shortage of capacity is the value of the dual variable associated with the leg’s capacity constraint 14 , i.e., theŽ . dual price of the leg. Here, large values indicate the potential that by only a small capacity expansion a relatively large increase in profit can be realized.

SYNOPSE supports this kind of analysis by the presentation of a list of fully used legs, together with their dual prices and the possibility to generate the list of parallel edges by a simple mouse click to an entry in the list.

On the other hand, a leg with an extremely low, or even zero, load factor seems to indicate a capacity excess, i.e., that the leg is superfluous and can be deleted from the schedule, thereby increasing profit. Yet, in most cases, such a simple conclusion is invalid, since the leg may be or become part of an aircraft routing, i.e., so-called flights with the other legs of the routing being heavily utilized. Here the analyst has to use his knowledge about existing flights to draw adequate conclusions.

Another indicator of a possible capacity shortage is an unsatisfied demand, i.e., the fact that a certain O&D has a production level below 100%. If in the optimal solution the demand quantity of a certain O&D is not completely transported, this indicates either a capacity shortage, i.e., that the schedule does not offer sufficient capacity and, with respect to the scarce transportation resources, other O&Ds are more profitable, or it indicates that another unit of the O & D is not profitable, i.e., the freight rate does not compensate for the cost of an additional unit, since one would have to use an itinerary which, although offering capacity, has operating cost exceeding the O&D’s yield.

![](/api/attachments/XKCQ83SX/fulltext/images/cfdd4315392ae0c76133ef90830e71d6f739b74c2ce533b0997f46f36b4c0810.jpg)  
Fig. 3. Example: the O & D listing.

Again, there are two approaches to support this kind of analysis. First, SYNOPSE presents a list of all unsatisfied O&Ds, and allows the generation of the associated itineraries via mouse click. Then, however, the analysis becomes quite complex. Following the sequence of legs of an itinerary, one can check the load factor of these legs as well as of their parallel legs and, thus, identify a capacity shortage, and one can identify the other O&Ds which are transported on these legs and thus are more profitable. This may lead to many alternative candidates for modifications. A second approach would be to look at the reduced cost coefficients of those itineraries for the O&D which are nonbasic, i.e., which are not used in the present freight flow. If these values are all strictly negative, this indicates the relative unprofitability of the O & D under consideration.

On the other hand, if an O & D is fully satisfied, this indicates a relative profitability. Again, in this case, a high value of the dual price of this O & D, i.e., the value of the dual variable for the O & D’s quantity constraint Ž . 13 suggests to increase the demand quantity, i.e., it suggests the acquisition of more demand for this specific O&D.

During the analysis of a critical object, the planner will encounter more critical objects of different types and, thus, change his view. Thus, the dialog management has to allow for the flexible evaluation along search paths of the dimensionality described above with the provision of memory aids and the possibility of freezing, versioning and backtracking to objects and situation descriptions constructed along the search path.

![](/api/attachments/XKCQ83SX/fulltext/images/62f74c3d9a64185568374bbe8443d76852446a7608a323159bfa0d1b27acd53c.jpg)  
Fig. 4. Example: SYNOPSE’s complex analysis screen.

We will briefly describe the associated features which are implemented in the present version of SYNOPSE.

During the analysis of a schedule, the planner may encounter several objects which he wants to analyze under certain aspects through a modification of their characteristics. SYNOPSE maintains a so-called change-list, into which the planner can insert candidates for later modifications. Finally, based on this list, the planner can generate a new problem instance which will then be solved again by SYNOPSE.

During the course of an analysis, the analyst may create several sets of modifications that he wants to have evaluated. To support this what-if analysis, as well as a systematic schedule evaluation and improvement through this kind of simulation, we implemented a versioning function. The initial schedule to be evaluated or to be improved is called the base schedule leading to an associated base solution, i.e., optimal freight flow. Each time a set of modifications is defined, and the resulting instance is solved via SYNOPSE, this creates a so-called version of the base schedule. Now, the analyst may want to create modifications of versions, i.e., sequences of modified instances to be evaluated and he may then want to undo certain modifications and restart analysis from a version created earlier in the simulation process. SYNOPSE keeps track of these versioning paths, and allows backtracking by maintaining a so-called version-tree. Starting with the base instance and solution as the root each, modification of an instance creates a new labelled node which is connected with the node of the old instance by an arc. In this way, it is possible to reconstruct any predecessor of an instance as, for example, the base schedule itself.

![](/api/attachments/XKCQ83SX/fulltext/images/db89fa643c06bdd3ed78b731c2d33ee4c21d078ea4e21576a31a8fbd2507ff8c.jpg)  
Fig. 5. Example: the leg listing.

To support the analysis of the effects of such modifications, i.e., to support the comparison of different versions of a base schedule, SYNOPSE allows to keep two problem instances active for analysis and presents the differences of the associated optimal freight routings. Obviously, the comparison in terms of key values as, for instance, contribution to profit, total yield, etc., can give only a first and rough idea of the impact of the changes. For a deeper and more detailed what-if analysis, SYNOPSE presents the differences between the versions in form of three so called -listings stating, for all common O&Ds, the difference in total yieldŽ . measured in US\$ and total transportation measured in units as well as, for every common leg, the difference inŽ . load factor, dual price, and idle cost.

In most cases, the modifications issued by the analyst will be rather small in order to reduce the complexity of the entire analysis. Often, yet not necessarily always, this will result in only a few local changes in the freight flow. In this case, a simultaneous presentation of the two freight flows in form of such a list of differences ranked by decreasing delta values gives a compact and easily readable view and enables a quick check whether some anticipated changes have materialized, and thus the new version should be kept for further analysis and modification. After a sequence of changes has been issued and the modifications have accumulated to a schedule, which is rather different from the base schedule, it may be advisable to declare this schedule to be a new base schedule.

![](/api/attachments/XKCQ83SX/fulltext/images/8935a90034912489b498d7e3c37a3a598c158d35beddac30997f5c49dc86be78.jpg)  
Fig. 6. Example: the new O&D listing.

## 5.1. A working example

In the following, we outline the analysis for a small, artificially constructed instance, displaying some of the associated presentations SYNOPSE screen-shots . Note that in SYNOPSE, the screens utilize GermanŽ . conventions for representation of decimals. Although this example is quite simple, it already demonstrates the high complexity of the analysis in general and the high volume of relevant information which has to be organized and presented properly to support the different views and navigation paths of the analysis.

From the ordered list of production levels Fig. 3 , the analyst is informed about unsatisfied demand by theŽ . optimal freight flow. In this case, he learns that only 2.97 tons of standard freight from Frankfurt to Abu Dhabi —i.e., for the O&D FRA–AUH–S is transported, which is a production level of only 4.47% and leads to a loss in yield of 82.560 DM. With a mouse click on the associated line, the analyst can activate the next screen Fig.Ž 4 , which gives information about the critical O&D under consideration and allows the analysis of the. corresponding itineraries. The screen shows that, in the present solution, only one itinerary FRA–BAH–AUH via Bahrain is used.

Now we assume that the analyst knows of an alternate itinerary for the critical O&D connecting FRA with AHU via KWI Kuwait . Further analysis reveals that the capacity on the leg KWI and AHU is fully used and,Ž . thus, this connection is the bottleneck. Knowing about a charter option of 20 tons, the expert may now introduce an additional leg connecting KWI and AHU with its chartered capacity into the change-list.

With this modification, he has created a new version which is solved. The old solution A and the newŽ . solution B can now be compared. Since the analyst is interested in the difference on the critical legs of theŽ . itinerary, he will start the analysis using the leg view and activate the screen shown in Fig. 5. He immediately sees that an amount of 20 tons is transported on the newly introduced leg flight no. 9999 . The O&D listingŽ . Ž . Fig. 6 shows that through this modification, the O&D FRA–AUH–S is satisfied with another 16 tons.

## 6. Final remarks

In this work, we have presented SYNOPSE, our model-based DSS for evaluation of flight schedules for cargo airlines by describing its conceptual as well as technological basis and our experiences during its development, as well as its analytical capabilities. SYNOPSE has evolved over time, as is common with all specific DSS, and even at the moment the system is under permanent revision. Through the work with the several versions of SYNOPSE, analysts have not only learned about the use of model-based DSS in concrete decision situations. The creation of new insights into the complex interdependencies of the planning situation extending the analysts expertise has probably a much larger effect on future planning than the creation of relevant information for a specific decision instance. Analysts are now in a much better position to specify their needs and to evaluate institutional computer-based planning systems developed for their department. Thus our work with SYNOPSE has again demonstrated that developing a Decision Support System is more a service task than the manufacturing of a product and that ‘the purpose of mathematical programming is insight, not numbers’ 10 .<sup>w</sup> <sup>x</sup>

## References

<sup>w</sup> <sup>x</sup> 1 R.K. Ahuja, T.L. Magnanti, T.L. Orlin, Network Flows: Theory, Algorithms, and Applications. Prentice-Hall, London, 1993.

<sup>w</sup> <sup>x</sup> 2 J. Antes, Structuring the process of airline scheduling. WINFORS Working Paper, University of Cologne, Germany, 1997, URL: http:<sup>rr</sup>www.informatik.uni-koeln.de<sup>r</sup>winfors<sup>r</sup>pub<sup>r</sup>ja-sor97-1.ps.

<sup>w</sup> <sup>x</sup> 3 Carlson, E., An Approach for Designing Decision Support Systems, Data Base 11, 1979.

<sup>w</sup> <sup>x</sup> 4 CPLEX, Using the CPLEX Callable Library, Version 4.0, CPLEX Optimization, Suite 279, 930 Tahoe Blvd., Bldg. 802, Incline Village, NV 89451-9436, USA, 1989.

<sup>w</sup> <sup>x</sup> 5 G. Dantzig, P. Wolfe, Decomposition principle for linear programs, Operations Res. 8 1 1960 101–111. Ž . Ž .

6 G. Dantzig, P. Wolfe, The decomposition algorithm for linear programs, Econometrica 29 4 1961 767–778. Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 R. Doganis, Flying Off Course: The Economics of International Airlines, 2nd edn., Harper Collins Academic, London, 1991.

<sup>w</sup> <sup>x</sup> 8 R. Elmasri, S.B. Navathe, Fundamentals of Database Systems, 2nd edn., Benjamin<sup>r</sup>Cummings, Redwood City, 1994.

<sup>w</sup> <sup>x</sup> 9 R. Fourer, D.M. Gay, B.W. Kernighan, AMPL: A Modeling Language for Mathematical Programming, Body & Fraser, 1993.

<sup>w</sup> <sup>x</sup> 10 A.M. Geoffrion, The purpose of mathematical programming is insight, not numbers, Interfaces 7 1 1976 81–92.Ž . Ž .

11 C.W. Holsapple, A.B. Whinston, Decision Support Systems: A Knowledge-Based Approach. West Publishing, Minneapolis, 1996.

<sup>w</sup> <sup>x</sup> 12 R.H. Sprague Jr., In: Sprague Jr., Watson 1993 Eds. , A Framework for the Development of Decision Support Systems, Chap. 1, Ž . Ž . 1986, pp. 3–28.

<sup>w</sup> <sup>x</sup> 13 R.H. Sprague Jr., E. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

<sup>w</sup> <sup>x</sup> 14 R.H. Sprague Jr., H.J. Watson, Decision Support Systems: Putting Theory into Practice, 3rd edn., Prentice-Hall, London, 1993.

<sup>w</sup> <sup>x</sup> 15 A.T. Wells, Air Transportation: A Management Perspective, 3rd edn., Wadsworth, Belmont, 1994.

![](/api/attachments/XKCQ83SX/fulltext/images/d45e03eefbe125ff9a9086231a0c95b19d39eb21c5754419f980c88acaf4955a.jpg)

Jurgen Antes studied computer science at the Rheinische Friedrich-Wilhelms Universitat Bonn with a specializa-¨ ¨ tion in parallel algorithms. He received his diploma in 1993. Since 1993 he has been a teaching and research assistant at the Seminar fur Wirtschaftsinformatik und Operations Research WINFORS at the Universitat zu ¨ ¨Ž . Koln. Jurgen Antes is a member of the Gesellschaft fur Informatik, the German computer science society and of¨ ¨ ¨ the Institute for Operations Research and the Management Sciences. His main interests fall in the application area of transportation and logistics. Presently, he is concerned with problems stemming from airline operations research. He is planning to get a PhD in 1998.

![](/api/attachments/XKCQ83SX/fulltext/images/990a378b58dca2d7215266a4419a04dd24d0d078002438b8fc0a54f3fb3b7d47.jpg)

Lenard Campen is a graduate student of Information Systems at the University of Cologne and hopes to finish a diploma degree by April 1998. Since 1994 he has been working as a project leader in several companies in the area of software engineering, especially in database design. His work at WINFORS started in 1995 and is mainly focused on the design and implementation of Decision Support Systems.

![](/api/attachments/XKCQ83SX/fulltext/images/da31d831f082ea31e9e0d0c96d923582313dae7d170e36bd57cddf0678f29d05.jpg)

Ulrich Derigs holds a chair in Information Systems and Operations Research and is director of WINFORS at the University of Cologne, Germany. He holds a PhD in Mathematics and a PhD in Economics, and has published numerous books and papers on Operations Research and Information Systems. His research interests include OR Modeling, Optimization, Heuristics and Data Modeling, and their use in Decision Support Systems. Ulrich Derigs is a member of ACM, GI, INFORMS, GOR and ISDSS. At present, he is president of GOR, the German Society for Operations Research.

![](/api/attachments/XKCQ83SX/fulltext/images/980f15668d82c98d60de0e97057b077a75d2c1bdf9803975d2c85a90f27e9e23.jpg)

Christoph Titze studied industrial engineering at the Technische Hochschule Darmstadt and finished his masters degree in 1990. In 1991, he began his job at Lufthansa as a project leader for the new Munich airport. He than moved to Lufthansa Technik as a controller and project leader for several EDP projects. Since 1995, he has been working for Lufthansa Cargo as a manager for network and fleet planning.

![](/api/attachments/XKCQ83SX/fulltext/images/e4b018a39fd8ea89727cd2799c58cbac1de6f497caeb0d23ba8125699216ebe6.jpg)

Gert-Dieter Wolle started an internal 3-year business training with Lufthansa in 1971. A job within the corporate auditing department followed, during which he studied economics at the Open University Hagen and received his masters degree in 1981. After that, he was appointed for several jobs in cargo route and yield management as wel as corporate strategy. Presently, he is General Manager of Network Controlling and Systems at Lufthansa Cargo. His main focus lays on the integration of EDP-based planning tools and cost-reduction programs.
