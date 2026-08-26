---
otero_id: 17715
otero_key: "NAMQXEW7"
title: "An integrated approach for the specification of processes and related complex structured objects in business applications"
authors: "Andreas Oberweis"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00021-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An integrated approach for the specification of processes and related complex structured objects in business applications

Andreas Oberweis \*

Universität Karlsruhe, Institut AIFB, D-76128 Karlsruhe, Germany

## Abstract

An extension of high-level Petri nets, namely nested relation/transition nets (NR/T-nets), is described. NR/T-nets allow to model distributed processes and related complex structured objects in business applications. The paper focuses on the development of complex NR/T-net models. Due to their complexity high-level Petri net models are usually not developed in one single step. Therefore, two evolutionary development strategies are introduced: on the one hand incremental construction by iteratively evaluating, refining, formalizing and integrating net fragments, on the other hand adaptation of application-specific reference process and object models.

Keywords: Business process modelling; petri nets; complex objects

## 1. Introduction

Processes in business applications are collections of activities associated with a particular business function where the activities are related by the involved objects, persons or resources. Process models should include a specification of the following aspects:

1. activities and their synchronization,

2. roles and resources assigned to the activities,

3. business rules,

4. exception handling, and

5. temporal aspects (deadlines, durations, etc.).

Process models can be simulated and analyzed in order to reorganize and improve the described processes. They can be further used as a basis for the planning of resource allocations. A workflow management system may use a process model for monitoring and controlling ongoing workflows [10].

Several languages have been suggested for process modelling, most of them being based on textual programming languages or graphical notations such as dataflow diagrams, state transition diagrams, Petri-nets, or related notations [4,6-8,11-13,15,18,21,35,37,38].

In this paper we propose a high-level Petri net based approach for formal, implementation independent process modelling. This formal process modelling language serves as an intermediate stage between informal, application specific notations and (workflow) programming languages. Fig. 1 distinguishes between four different levels of process modelling, leading from a language which is understandable to business people to a machine oriented, executable language. The transformation of process models from one language level to another is usually to be done manually or semi-automatically. Only the step from formal notations to machine oriented programming languages can be completely automated.

![](/api/attachments/NAMQXEW7/fulltext/images/e2b967ab2c67c70e81a003fab3f75532be1408844848af7029803dc580ef12d4.jpg)  
Fig. 1. Four levels of business process modelling languages.

Petri nets [3] are a general purpose language for the graphical specification of synchronization aspects in distributed systems. A Petri net is a bipartite graph, consisting of two types of nodes, the places and the transitions. Places and transitions are connected by directed arcs. In general a place represents a local object (“token”) storage, and a transition represents an operation which removes some objects from the transition’s input places and which inserts some objects into the transition’s output places. An assignment of tokens to a place is denoted as marking of the place. Fig. 2 shows the graphical representation and some possible interpretations of the net components.

High-level Petri nets (e.g., predicate / transition nets (Pr / T-nets) [9] or coloured Petri nets [16]) support an integrated description of structural and behavioral system aspects: tokens in these nets are structured and have attributes to which values are assigned. In (strict) predicate/transition nets the marking of a place is a relation, and a transition represents a class of operations on the relations in its input and output places. However, the structure of tokens in Pr/T-nets is restricted to “flat” tuples: attribute values must be atomic and cannot be further structured.

In [25,27] we have therefore introduced an extension for Pr/T-nets, namely nested relation / transition nets (NR/T-nets) which integrate the concept of complex structured objects into the Petri net formalism. The marking of a place in an NR/T-net is a set of complex structured objects and a transition represents an operation on these objects. So-called filter tables are assigned to the arcs in a net to specify declaratively objects to be manipulated.

The focus of this paper is on modelling aspects. At the conceptual data design level semantic data models are used instead of the relational data model due to the more natural modelling constructs provided by semantic data models $[30]$ . This suggests a combination of NR/T-nets with semantic data modelling concepts: the structures of the places in an NR/T-net are specified by a semantic data model. For the development of large NR/T-net models two different strategies are proposed: on the one hand incremental construction by iteratively evaluating, refining, formalizing and integrating net fragments, on the other hand adaptation of application-specific reference process and object models.

![](/api/attachments/NAMQXEW7/fulltext/images/5d23dd57e2c734a849e80d8f5a37fc2714b060a010b16afb59d6a225ed0b1135.jpg)  
Fig. 2. Basic Petri net concepts.

The paper is structured as follows: In the next section, NR/T-nets are informally introduced. First the basic Petri net notation is surveyed. Then operations on complex structured objects are considered and filter tables are proposed to specify insert and delete operations on nested relations. NR/T-nets are defined by combining the concept of filter tables and high-level Petri nets. Section 3 describes evolutionary design concepts for NR/T-nets, Section 4 concludes the paper and surveys ongoing implementation work.

## 2. Nested relation / transition nets

## 2.1. Basic Petri net notation

A Petri net is a bipartite graph, consisting of two types of nodes, the places and the transitions. Places and transitions are connected by directed arcs.

Definition 1: Petri Net [3]

A Petri net is a triple $N = (PL, TR, F)$ where 1. PL is a finite set of so-called places,

2. TR is a finite set of so-called transitions, $PL \cap TR = \varnothing$ ,

![](/api/attachments/NAMQXEW7/fulltext/images/9717ca6430395ae2a50bb383bbafc2107b80176d89a820f9d387eb552edf0131.jpg)  
Fig. 3. Basic synchronization patterns in Petri nets.

3. $F \subseteq (PL \times TR) \cup (TR \times PL)$ is the flow relation of $N$ .

Places are graphically represented as circles, transitions as boxes and elements of the set F as directed arcs.

Fig. 3 shows the basic synchronization patterns, which can be represented in Petri nets:

1. sequence of activities: activity A2 requires an object produced by activity A1.

2. mutual exclusion of two activities which require the same object.

3. concurrent occurrences of activities A2 and A3 which require different objects produced by activity A1.

Example 1: Travel agency

Fig. 4 shows an example Petri net which semi-formally describes a part of the process of booking a journey in a travel agency. This is an extract from a larger net which also includes activities related to planning of a journey and accounting.

![](/api/attachments/NAMQXEW7/fulltext/images/154fc537f6e0ee2e3d0a431d6aae1d6060f31c824d2b4f871226bafe4f733716.jpg)  
Fig. 4. Example Petri net.

Each reservation request consists of a hotel request and a flight request. Both requests are processed independently of each other — possibly at different locations. A complete reservation is rejected if the hotel reservation or the flight reservation is rejected. If the flight (hotel) reservation was successful and the hotel (flight) reservation failed then the flight (hotel) reservation is also to be cancelled. A reservation is only successful if both flight and hotel reservation are successful.

Fig. 4 contains the basic patterns of behaviour specification with nets: sequences, mutual exclusion and concurrency. For a given reservation request, the operations related to the flight reservation and the operations related to the hotel reservation may occur concurrently — due to their disjoint sets of input and output places. Complete-reservation, e.g., can only occur after Accept-hotel-reservation and Accept-flight-reservation have occurred. For a given flight request either Acceptflight-reservation or Reject-flight-reservation may occur.

A Petri net is only a semi-formal description of the process structure, there is no formal notion of system state or system behaviour. Therefore, Petri nets belong to the level-II languages in the 4-level hierarchy of process modelling languages shown in Fig. 1. However, there exist different approaches to extend the basic Petri net concept.

Predicate/transition nets [9] are high-level Petri nets where the places (predicates) represent relation schemes in first normal form (i.e., having only atomic attributes). The marking of the net represents a global system state. It assigns to each place a relation according to the respective relation scheme. Due to this interpretation of the places and their markings predicate/transition nets are closely related to the relational data model [5]. A transition represents a class of operations on the relations in the adjacent places. The formal occurrence rule for predicate/transition nets defines, when a transition may occur and what kind of operations are implied by a transition occurrence. A transition is enabled for a given marking, i.e., it may occur, if for the marking certain tuples are available in the input places and certain tuples do not yet exist in the output places. When a transition occurs, the respective tuples are removed from its input places and inserted into its output places according to the respective arc inscriptions. A logical expression may be assigned to a transition to specify certain additional conditions on the tuples to insert and to remove. A predicate/transition net together with an initial marking represents a set of possible processes of a (distributed) business application.

![](/api/attachments/NAMQXEW7/fulltext/images/6abb6359466b82080087e7e90c5178d19db05754903a4d5023cead514f6086ef.jpg)  
Fig. 5. Predicate/transition net.

## Example 2: Predicate/transition net

Fig. 5 shows a simple predicate/transition net which specifies the operation Accept-flight-reservation (compare Fig. 4). A relation is assigned to every place as initial marking.

A flight reservation is accepted, if there is still a seat available in the requested flight. Note that a further implicit pre-condition of Accept-flight-reservation to occur is that there does not already exist a reservation for the respective flight and the respective person. Formally, the transition Accept-flight-reservation is enabled for a given marking of it's input and output places, if

1. there exists a tuple $\langle F\#, N, D \rangle$ in place FLIGHT-REQUEST and a tuple $\langle F\#, A, D, P \rangle$ in place FLIGHT where A > 0, and

2. there does not exist a tuple $\langle F#, A', D, P \rangle$ in place FLIGHT where $A' = A - 1$ , and there does not exist a tuple $\langle F#, N, D, P \rangle$ in place FLIGHT-RESERVATION.

(Note, that uppercase letters in the arc and transition inscriptions denote variables. Further note, that equal variables in the environment of a transition must be equally instantiated.)

For the given initial marking in Fig. 5 Accept-flight-reservation is enabled with respect to the following instantiation of variables: F#←123, N←\`Smith', D←\`01/10/94', A←125, A'←124, P←1250. If the transition occurs for this instantiation then the respective instantiated tuples are removed from the input places and inserted into the output places.

Note that a transition occurrence is atomic, i.e., all operations related to a transition occur in one single step and there is no intermediate state reached during a transition's occurrence. The transition Accept-flight-representation corresponds to a collection of SQL-operations, which is to be executed in one step (as a single transaction):

![](/api/attachments/NAMQXEW7/fulltext/images/fdf4f09c0319e4f819bd3b9a9f4ee512b7572187fa1b8374947da0c53a67a613.jpg)  
Fig. 6. Nested relation/transition net (without inscriptions).

1. Join of a FLIGHT-REQUEST tuple and a FLIGHT tuple over matching FLIGHT#.

2. Deletion of a tuple from the relation FLIGHT-REQUEST.

3. Insertion of a tuple into the relation FLIGHT-RESERVATION.

4. Update of a tuple in the relation FLIGHT.

## 2.2. Filter tables and high-level petri nets

Due to their formal semantics predicate/transition nets belong to the level-III languages in the 4-level hierarchy of process modelling languages (compare Fig. 1). The problem with predicate/transition nets is that they only allow the manipulation of flat tuples with atomic attributes. In [25,27] we have, therefore, introduced an extension for predicate/transition nets, namely nested relation / transition nets (NR / T-nets) which integrate complex object structures into the Petri net formalism. The marking of a place in an NR/T-net is an unnormalized (“nested”) relation [36]. A transition now represents an operation on unnormalized relations. Unnormalized relations are hierarchically structured and attribute values may again be unnormalized relations. However, if unnormalized relations are allowed as markings of the places it is not clear how to access (insert, delete) set-valued attributes at the lower levels of the attribute hierarchy.

## Example 3: Nested-Relation/Transition-net (NR/T-Net)

Fig. 6 shows an NR/T-net (without arc inscriptions) where FLIGHT is given as an unnested relation type, having set-valued attributes PASSENGERS and AVAILABLE-SEATS.

If a seat is reserved, then the respective seat-number is removed from the AVAILABLE-SEATS set and the respective passenger is inserted into the PASSENGERS set of the FLIGHT tuple. In the corresponding NR/T-net the reservation of a seat is modeled by a transition, which accesses the places FLIGHT-REQUEST, FLIGHT, and FLIGHT-RESERVATION.

In the following we show how the net is to be inscribed in order to completely specify the transition Accept-flight-reservation.

An important new feature of NR/T-nets are so-called filter tables which are assigned to the arcs in a net to specify tuples to delete from places and to insert into places. In the following we only give a brief, informal overview about the basic concepts, for the theoretical foundations and formal definitions see $[25,33,34]$ .

Formally, filter tables can be considered as an extension of literals in 1st order predicate logic without function symbols. Such a 1st order literal may be interpreted as an “example tuple” consisting of constants and variables. A literal can be used very well to describe the insertion and deletion of data in a 1NF relational database (compare the graphical language Query-By-Example [39]). For example, a literal of the form $(X_{1},\ldots,X_{n})$ – where each $X_{i}$ is a variable or a constant – may specify the insertion (or deletion, respectively) of tuples which can be obtained by mapping the variables of the literal to constants of the respective domains. However, this simple mechanism is not appropriate for nested relations because it does not correspond to the hierarchical structure of nested relations: it is only possible to access values on the highest level of the attribute hierarchy.

Thus, in $[25,27,34]$ a generalization of this approach has been proposed, the so-called filter tables. This extension can be characterized as follows:

1. Filter tables have a hierarchical structure corresponding to an underlying nested relation scheme. A filter table contains a set of tuples. Each tuple consists of terms, which may be variables (uppercase letters), atomic constants (lowercase letters) or again filter tables. Each term represents values of the domain of the corresponding attribute. The hierarchical structure of filter tables allows to access values which are located on a lower level of the attribute hierarchy.

2. By filter tables, in general, sets of tuples are specified instead of single tuples. This also corresponds to the structure of nested relations and allows to specify and access set-values.

3. It is distinguished between two types of set-valued terms in filter tables: open terms and closed terms. Syntactically, closed terms are marked by an overline whereas open terms are unmarked. Semantically this expresses the difference between sub-tuples and “autonomous” tuples: a closed term, e.g., the variable $\overline{X}$ , represents an access to a whole, indivisible set-value. This variable must be instantiated by a whole set-value which exists in a tuple. On the other hand an open term describes the access to subsets, i.e., the term can be instantiated with a subset of an existing set. Note, that for every composite (i.e., non-atomic) attribute it is locally specified (i.e., independently from all other attributes) whether to access the respective values only as a whole or to access also subsets of these values.

The distinction between open and closed terms implicitly defines an ordering on nested relational instances. This ordering induces a lattice structure with a union, intersection, and complement operation on instances. Then, the insertion of an instantiated filter table into another instance is simply the union of both, and the deletion of an instantiated filter table I1 from another instance I2 is the intersection of I2 with the complement of I1.

Thus, values which are obtained by instantiating a closed term are treated as atomic values, and a tuple can be deleted as a whole only if all set-valued terms are closed. Otherwise, if there exists at least one open term, only the values of the open terms can be removed from the corresponding tuple in an instance. The insertion is inverse to the deletion of tuples, and it is uniquely defined how set-values are grouped together by an insert operation. If a term is closed then the value to be inserted must appear as a whole in the resulting instance, otherwise the value can be grouped together with an already existing value.

In the following we will show the usage and expressiveness of filter tables as an inscription language for Petri nets by giving some examples.

![](/api/attachments/NAMQXEW7/fulltext/images/eb2a6bdf6de8540304e3a969638cee599bca1773d063f34b1896e23f185446e1.jpg)  
Fig. 7. Filter table as arc inscription (I).

![](/api/attachments/NAMQXEW7/fulltext/images/0ebaa55313c5673d79ac285d8ab918ffed4a17a0055bb95a91962b4afed4138a.jpg)  
Fig. 8. Filter table as arc inscription (II).

Example 4: Filter tables as arc inscriptions

Figs. 7–10 show some example applications for filter tables to specify insert and delete operations. A nested relation FLIGHT is given, having set-valued attributes PASSENGERS and AVAILABLE-SEATS.

The transition in Fig. 7 represents the deletion of the whole tuple of flight 124 in the place FLIGHT, i.e., it reflects a situation where flight 124 is cancelled. Both set-valued terms Pa (for

PASSENGERS) and A (for AVAILABLE-SEATS) in the filter table are marked by an overline, hence the variables Pa and A are to be instantiated by the whole PASSENGERS and AVAILABLE-SEATS values of flight 124. An occurrence of transition Cancel flight 124 changes the initial marking M $^{0}$ of place FLIGHT into the follower marking M $^{1}$ as shown in Fig. 7.

The transition in Fig. 8 represents an insert operation of the tuple

![](/api/attachments/NAMQXEW7/fulltext/images/b82f23d99fb2b143c0f5aa64559bb646c3e4648cd96eb58c61e2141c0b09244a.jpg)  
Fig. 9. Filter table as arc inscription (III).

$$
\langle 1 3 5, \{\langle 1 2 1, \text { Newman } \rangle \}, \{\}, 8 2 0, 1 1 / 1 5 / 9 4 \rangle
$$

into the FLIGHT relation. This does not mean that the tuple is to be inserted as a new “autonomous” tuple into the relation but that the tuple is to be merged with the already existing tuple of flight 135. To indicate this, the PASSENGERS term in the filter table is open. An occurrence of transition Insert passenger Newman changes the initial marking M $^{1}$ into the follower marking M $^{2}$ as shown in Fig. 8.

Note that the flight reservation is not yet completed since the AVAILABLE-SEATS value also must be updated. This operation is specified by the transition in Fig. 9. In the filter table the AVAILABLE-SEATS term is open, hence the respective value 121 is removed from the existing AVAILABLE-SEATS instance in the relation FLIGHT. An occurrence of transition Delete seat 121 changes the initial marking M $^{2}$ into the follower marking M $^{3}$ as shown in Fig. 9.

The transition in Fig. 10 finally specifies an insert operation for a new flight 224, initially having an empty set of passengers and a set of 180 available seats. Note that in this special case the overlines of both set-valued terms (for PASSENGERS and AVAILABLE-SEATS) in the filter table may also be omitted without modifying the result of the operation. An occurrence of transition Insert flight 224 changes the initial marking $M^{3}$ into the follower marking $M^{4}$ .

## 2.3. Nested relation / transition nets

## 2.3.1. Basic idea

In the previous section we discussed single insert and delete operations on nested relations. In NR/T-nets, transitions denote composite operations on nested relations. One single transition may involve several insert and delete operations, which are to be executed in one atomic step. The net structure defines the synchronization between different composite operations.

In the following, nested relation/transition nets are defined. These high-level nets extend the basic net model by three different concepts: the places are interpreted as “containers” for nested relations. Filter tables are assigned to the arcs in the net to specify (sub-) tuples to be removed from a transition’s input relations and (sub-) tuples to be inserted into a transition’s output relations. Transitions may be inscribed by logical formulas which define further restrictions on the tuples to be removed and on the tuples to be inserted.

![](/api/attachments/NAMQXEW7/fulltext/images/e755b8879f09dc452692992a391da19e389967168c1fdafbce62a4a242bbbdcf.jpg)  
Fig. 10. Filter table as arc inscription (IV).

Definition 2: Nested Relation/Transition-net
A nested relation/transition net (NR/T-net) is a 4-tuple $NRT = (NN, AI, TI, M^{0})$ such that 1. $NN = (PL, TR, F)$ is a net where the places are interpreted as nested relation schemes.

2. AI is a function which assigns to each element f in F a filter table. The structure of the filter table $AI(f)$ corresponds to the scheme of the place adjacent to arc f.

3. $TI$ is a function which assigns to some transitions in $TR$ a logical formula.

4. $M^{0}$ is a function which assigns to each place an initial marking, i.e., a (nested) relation corresponding to the respective scheme.

## Example 5: NR/T-net

Fig. 11 shows an example for a simple NR/T-net $NRT = ((PL, TR, F), AI, TI, M^0)$ which specifies a variant of the transition Accept flight-reservation in Fig. 5.

$$
\begin{array}{r l} & P L = \left\{\text { FLIGHT - REQUEST,FLIGHT, } \right. \\ & \quad \left. \text { FLIGHT - RESERVATION } \right\} \\ & T R = \left\{\text { Accept - flight - reservation } \right\} \\ & F = \left\{\left(\text { FLIGHT - REQUEST,Accept } \right. \right. \\ & \quad \left. \text {-flight - reservation}\right), \\ & \left(\text { FLIGHT,Accept - flight } \right. \\ & \left. \text {-reservation}\right), \\ & \left(\text { Accept - flight - reservation, } \right. \\ & \left. \text { FLIGHT }\right), \\ & \left(\text { Accept - flight - reservation, } \right. \\ & \left. \text { FLIGHT - RESERVATION }\right) \end{array}
$$

$$
\begin{array}{r l} & A I (\text {   FLIGHT - REQUEST,   Accept   -   flight   } \\ & \quad - \text {   reservation)   } = \boxed {\mathrm{F} \#, \mathrm{N}, \mathrm{D}} \end{array}
$$

$$
\begin{array}{r l} & A I (\text { Accept   -   flight   -   reservation }, \\ & \text { FLIGHT   -   RESERVATION }) = \boxed {\mathrm{F} \#, \mathrm{N}, \mathrm{D}, \mathrm{P}} \end{array}
$$

![](/api/attachments/NAMQXEW7/fulltext/images/f55b929691f6622d313b956947166c67186a81089cee268edd932fb60a1ed9f2.jpg)  
Fig. 11. Example NR/T-net.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
AI(Accept-flight-reservation,
FLIGHT) = expla36 F#, S#, P, D
AI(FLIGHT, Accept-flight
- reservation) = F#, S#, N, P, D
M$^{0}$(FLIGHT-REQUEST)
= {(135, Newman, 11/15/94)}
M$^{0}$(FLIGHT) = {(135,
{(1,Ford),(2,Jones),(3,Smith),...,
(120,Green)},
{(121),(122),...,(235)},
820,11/15/94)}
M$^{0}$(FLIGHT-RESERVATION) = {}
</div>

FLIGHT is now a nested relation type as already given in Fig. 6. Accept-flight-reservation combines the operations shown in Figs. 8 and 9 and additionally includes the respective operations on the relations in the places FLIGHT-RESERVATION and FLIGHT-REQUEST. The initial marking $M^0$ of the places FLIGHT-REQUEST and FLIGHT consists of one single tuple. The place FLIGHT-RESERVATION is marked by the empty set.

## 2.3.2. Occurrence rule for transitions in nested relation / transition nets

Transitions represent schemes of (local) marking changes or classes of activities. The so-called occurrence rule for transitions in Petri nets consists of two parts: the first part defines, when a transition is enabled, i.e., when it may occur. The second part defines the effects of a transition occurrence.

I. A transition t is enabled for a given marking and a given instantiation of the variables in t's environment, i.e., t may occur, if

1. the instantiated terms at the incoming arcs are contained (w.r.t. the underlying ordering of the corresponding filter table; this ordering is specified by open and closed terms in the filter table) in the marking (instances) of their respective adjacent places. This implies that instantiated closed terms must be contained as a whole in the marking of a place, and open terms must be a “sub-structure” of the marking.

2. the instantiated terms at the outgoing arcs are not contained (w.r.t. the underlying ordering of the corresponding filter table) in the marking of their respective adjacent places.

3. the logical formula inscribed to the transition t evaluates to “true”.

A transition which is enabled may occur. If an enabled transition occurs, tuples are removed from its input places and tuples are inserted into its output places.

II. The occurrence of a transition t for a given marking M and an instantiation $\Theta$ of the variables in t's environment implies that M is changed to a new marking $M'$ which is defined as follows:

1. the tuples specified by the filter tables of the incoming arcs with respect to the instantiation $\Theta$ are deleted from the corresponding instances. Speaking formally, a deletion is an intersection of the instance with the complement of the instantiated filter table. This operation depends on the underlying ordering of the corresponding filter table.

2. the tuples contained in the filter tables of the outgoing arcs with respect to the instantiation $\Theta$ are inserted into the markings of the output places. Formally, an insertion is a union of the instance with the instantiated filter table (with respect to the underlying ordering of the corresponding filter table).

3. for every place not belonging to the environment of t the marking remains unchanged.

## Example 6: NR/T-net (continued)

In Fig. 11 the transition Accept-flight-reservation is, for example, enabled for the flight request of passenger Newman, flight 135 and seat 121 (note, that the variable S may be instantiated by an arbitrary value in the set of available seats). If the transition occurs, the following insertions and deletions are executed:

1. the tuple $\langle135,$ 'Newman', '11/15/94' is deleted from place FLIGHT-REQUEST, the value $\langle121\rangle$ is deleted from the set of seats of flight 135 in place FLIGHT.

2. the tuple $\langle135,\text{'Newman'}\text{'11/15/94',820}\rangle$ is inserted into place FLIGHT-RESERVATION, the tuple $\langle121,\text{'Newman'}\text{'}\rangle$ is inserted into the set of passengers of flight 135 in place FLIGHT.

## 2.3.3. Aspects of concurrency in NR / T-nets

Two transitions in a predicate/transition net may occur concurrently, i.e., independently from each other, if both transitions concern a disjoint set of tuples. Each transition represents a class of possible occurrences, i.e., for a given marking there may exist different possible occurrences of the same transition. Hence, different extensions of the same transition may also occur concurrently if they concern different tuples.

In NR/T-nets the notion of concurrency is slightly modified, due to the fact, that different transitions may access different set-valued components of the same tuple concurrently. Concurrent access is possible for set-valued attributes where the respective terms in the filter tables are open. Concurrent access is not possible if the respective term in at least one filter table is closed. This distinction reflects the difference between shared and exclusive access to complex structured objects (e.g., office documents, document folders, or spreadsheets)

## Example 7: Concurrency in NR/T-nets

Fig. 12 shows a net where two activities (transitions) Hotel-reservation-1 and Hotel-reservation-2 access a nested relation HO-TEL. Both transitions may occur concurrently for the same hotel, if different rooms are to be reserved, i.e., removed from the AVAILABLE-ROOMS set. This reflects a situation, where different employees in a travel agency (or in different travel agencies) book rooms in the same hotel at the same time.

The transition Remove-Hotel on the other hand accesses the attribute AVAILABLE-ROOMS of the HOTEL relation by a closed term. Concurrent accesses of Remove-Hotel and, e.g., Hotel-reservation-1 to the same hotel tuple is not possible. However, concurrent accesses to different hotel tuples are still possible.

This notion of concurrency in NR/T-nets is a natural extension of the notion of concurrency in predicate/transition nets. Concurrent accesses on a single unnormalized tuple in an NR/T-net place correspond to concurrent accesses on a set of normalized tuples in a predicate/transition net place. Note, however, that in predicate transition nets problems arise, if concurrent accesses on different normalized tuples are to be prohibited such as in Example 7 where Hotelreservation-1 and Remove-Hotel must not occur concurrently for the same hotel. In NR/T-nets this can be simply expressed by marking at least one set-valued term in the respective arc inscriptions by an overline.

![](/api/attachments/NAMQXEW7/fulltext/images/3264f4bd04dad2ecc7d5ea15b0df3857e7ca5a2b2a7da066c235d220dd0b48b5.jpg)  
Fig. 12. Concurrency in NR/T-nets.

## 2.4. Related works

Several variants of Petri nets have been proposed in literature especially for the modelling of office procedures, workflows and information system behaviour (for example $[6,7,11-13,15,18,32,35,37]$ ). Some of these approaches combine semantic data modelling with Petri net based behaviour modelling $[6,12,18,32,37]$ . However, with these approaches problems arise when modelling the behaviour of complex structured objects due to the fact that it is not possible to model concurrent accesses to different components of the same complex structured object. An example was given in the previous section where different activities concurrently accessed the same hotel object.

## 3. Evolutionary development of large NR/T-net models

Specifying complex business processes with NR/T-nets is a complicated task that cannot be done in one single step. There exist two different strategies for the development of an NR/T-net process model: on the one hand incremental construction of nets by iterative application of evaluation, refinement, formalization and integration steps, on the other hand stepwise adaptation of available net based reference process models and reference object models to the requirements of a specific application.

3.1. Constructing a net model by evaluating, refining, formalizing and integrating informal net fragments

Fig. 13 shows the structure and basic steps of an evolutionary development method for complex NR/T-net based business process models. The given sequence of steps may vary for different development processes and some steps may be omitted occasionally. In the following the development steps are described in detail and some examples are given.

![](/api/attachments/NAMQXEW7/fulltext/images/97931e485244a5b9a47aae212858bf0cde225e777e091ce101fe7eb4c85f2954.jpg)  
Fig. 13. Evolutionary development method for net based process models.

## - Constructing informal net fragments

The development of an NR/T-net starts with a set of (usually) incomplete and informal net fragments each of them describing one single system activity. Each activity is described together with its input and output objects. This step may include the integration of certain elementary net building blocks from an existing Petri net library, e.g., to model pre-defined temporal relationships between activities such as during, overlapping, etc. [24].

Places in the net fragments are inscribed by an informal textual description of the respective object structures and transitions by a textual description of the transition's functionality.

It is useful to first concentrate on some system activities which are regarded as being important, and to abstract from exceptional system behaviour in the early design stages.

A single transition in a net fragment may be refined by a new net fragment in order to specify the respective activity in more detail. Formal rules for admissible, behaviour preserving refinements of nets have been proposed, e.g., in [16,18].

Example 8: Informal net fragment and refinements

Fig. 14 shows an informal net fragment for the processing of a reservation consisting of a hotel and a flight reservation. The transition Process-hotel-request is refined by a net consisting of two transitions Accept-hotel-reservation and Reject-hotel-request. The transition Process-flight-request is refined by a net consisting of two transitions Accept-flight-reservation and Reject-flight-request.

![](/api/attachments/NAMQXEW7/fulltext/images/2b4dd344b4128e7b92dd8df744024df0e15d7109f6d219b659a9e78a94b4c9be.jpg)  
Fig. 14. Informal net fragments.

![](/api/attachments/NAMQXEW7/fulltext/images/cd5204448b3a1668f15f2c60f09cfcf292c261893c645594f7866be374348fba.jpg)  
Fig. 15. Structuring concepts for object modelling.

## - Modelling object structures

For the places in the net fragments the local object structures are to be formally specified in a data model. It is suggested to use a semantic data model, which supports complex object structures, e.g., the Semantic Hierarchy Data Model, SHM, of [2].

![](/api/attachments/NAMQXEW7/fulltext/images/6348ae2ba1209ab99813daff87daa283b388aaa078505dfcad6f93e96505ab5d.jpg)  
Fig. 16. Local object structure of the places FLIGHT-REQUEST, REJECTED-FLIGHT-REQUEST, FLIGHT-RESERVATION and FLIGHT.

![](/api/attachments/NAMQXEW7/fulltext/images/9ed9d23f2d91ccef14112e9e43bfc5d0e6501fd645d22db163a4511b246c2b03.jpg)  
Fig. 17. Assigning nested relation schemes to the places in a Petri net.

The object structures are then (automatically) mapped to unnormalized relation schemes. It should be noted that the object structures defined in SHM must fulfil certain restricting conditions such that the nested relation representation is equivalent (cf. [17]). This step may be supported by (rapid) prototyping to validate the modeled object structures. Certain object structures which are available in an object library may be reused.

## Example 9: Modelling object structures

We use a graphical notation adopted from $[17]$ for the Semantic Hierarchy Data Model, SHM (see Fig. 15), which supports the structuring concepts aggregation, specialization and grouping. Fig. 16 shows the graphical description of the structure of place FLIGHT.

The nested relation schemes can be automatically derived from the respective local SHM schemes. Fig. 17 shows the net fragment for the activity Process-flight-request and the respective nested relation schemes in a tabular representation.

## - Formalizing net fragments

First the respective filter tables are defined which select the objects to remove from and to insert into places. Additionally, transitions may be inscribed by logical expressions to further select objects.

The formalization of net fragments may include another refinement of transitions and places. Furthermore, this formalization step may include the insertion of additional transitions and/or places into the given net fragments.

The formalization step can be supported by net simulation in order to validate the functionality of the resulting net model. Furthermore formal reachability analysis is possible for single net fragments.

![](/api/attachments/NAMQXEW7/fulltext/images/63b787dcb9401a8865adcda5506ea8745dd5649dab67b022ba549b51fef465f4.jpg)  
Fig. 18. NR/T-Net inscribed with filter tables.

![](/api/attachments/NAMQXEW7/fulltext/images/103a19631f170cbe638bc7696416332a1c1a77a9f57c69118054757bad5c61f4.jpg)  
Fig. 19. Exceptional situations.

## Example 10: Formalizing net fragments

Fig. 18 shows the nested relation/transition net where the arcs are inscribed by filter tables.

## - Defining exceptions and exception handling mechanisms

Exceptions are unusual, atypical, or unexpected situations which may occur in a business application. Their description should not disturb the description of the regular system behaviour (cf. [1]). In a nested relation/transition net exceptional situations can be modeled by exceptional transitions having a special semantics: an exceptional situation is indicated by a marking, where the corresponding exceptional transition is enabled. However, an enabled exceptional transition will never occur, i.e., it will never change the current marking. Instead an exception handling mechanism is defined in a separate Petri net for each exceptional transition. This exception handling net is triggered and executed when the underlying exceptional transition is enabled.

Example 11: Defining exceptions and exception handling mechanisms

We define two exceptional situations:

1. a state, where a flight could be reserved and the respective hotel request failed (Fig. 19a),

2. a state, where a hotel room could be reserved and the respective flight request failed (Fig. 19b).

REJECTED-HOTEL-REQUEST and HOTEL-RESERVATION consist of the attributes (RES#, CUST-NAME, HOTEL-NAME, ARR-DATE, DEP-DATE).

Fig. 20 shows two informal net fragments for the exceptions in Fig. 19. In case of exception (a), another hotel is selected from the hotel database and in case of exception (b) another flight is selected from the flight database. Note that the exception handling mechanisms may require interaction (e.g., a phone call) with the client of the travel agency. This interaction can be modeled in a further refinement of the transitions Find-other-hotel and Find-other-flight.

![](/api/attachments/NAMQXEW7/fulltext/images/aba73175d5c6aeb68eb8fce0b6945333123b5f82aa4cfb43abdfae180d58cd70.jpg)  
Fig. 20. Informal specification of exception handling mechanisms.

## - Including business rules, organizational aspects and temporal constraints

Business rules, organizational aspects and temporal constraints should not be hidden in a procedural description of business processes. Instead a specific view for each of these aspects should be provided in order to improve maintainability of business process models.

Business rules restrict business processes in a declarative way. They exclude certain states or state sequences. In Petri nets state related business rules can be modeled as so-called fact transitions (see e.g., [9]), whose enabledness indicates a violation of the respective rule. To distinguish fact transitions from regular transitions, fact transitions are inscribed by the symbol F in the graphical representation. State sequence related business rules can be modeled by sequences of fact-transitions.

## Example 12: Modelling business rules

Fig. 21 shows a simple state related rule for the example travel agency business process. It is expressed that credit cards are only accepted if the amount is less than 2000 US\$. The fact transition ft1 is activated if there exists a payment by credit card where the amount is greater than 2000 US\$. Payment is modeled as a relation with attributes (RES#, DATE, AMOUNT, MODE-OF-PAYMENT), where the value of MODE-OF-PAYMENT is either “cheque”, “credit card” or “cash”.

Organizational aspects include restrictions concerning resources which are needed for certain activities (e.g., fax, printer, scanner). Organizational aspects also concern the assignment of certain roles or responsibilities to the activities in a process model and the assignment of concrete employees to the roles.

![](/api/attachments/NAMQXEW7/fulltext/images/d46231a062e570193088dad98510740a638ff7e608e1d9d08fb06d6794516110.jpg)  
Fig. 21. Declarative representation of a business rule.

## Example 13: Representation of roles

Let us assume that in the travel agency certain roles are assigned to the employees. Each employee only processes flight-requests for a pre-defined set of destinations, e.g., for destinations in Europe and Asia. The travel agency information system must therefore select for each flight request an employee who is responsible for the respective continent. In Fig. 22 this selection is modeled by introducing a further input-place to the transition Accept-flight-reservation and by additionally inscribing the transition appropriately. Note, that the predicate FLIGHT is extended by an additional attribute DESTINATION. EMPLOYEE is a nested relation type with attributes (EMP#, RESPONSIBILITY(CONTINENT), CUSTOMER(NAME)). The transition Accept-flight-reservation inserts the customer name into the CUSTOMERS-attribute value of the selected employee.

Temporal constraints concern, e.g., earliest starting times for activities, deadlines for activities, holidays or weekends without business activities (see, e.g., [24]).

Example 14: Modelling of temporal aspects. Fig. 23 shows how to model an earliest occurrence time for an activity. The transition t1 can only occur, if the current date D (which is contained in a place CALENDAR) is not earlier than a predefined earliest occurrence time ET.

Deadlines, i.e., latest occurrence times for activities, can be declaratively modeled in NR/T-nets by fact transitions.

## - Integrating net fragments

The net fragments are then integrated to one single global net model. This step is again supported by simulation. Usually the resulting net is too large for complete graphical visualization. However, it can be used as input for a Petri net simulator $[20]$ or for process enactment with a Petri net based workflow engine $[7,23]$ .

<table><tr><td rowspan="2">EMP#</td><td>RESPONSIBILITY</td><td>CUSTOMERS</td></tr><tr><td>CONTINENT</td><td>NAME</td></tr><tr><td>1</td><td></td><td></td></tr><tr><td>2</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td></tr></table>

![](/api/attachments/NAMQXEW7/fulltext/images/525367a044d26d576a79b14e6f9ac9971df53a7b779f3039bebca1baf6b518e4.jpg)  
Fig. 22. Representation of organizational aspects.

Example 15: Integrating net fragments. Fig. 24 shows a part of the global net model of the reservation process (filter tables have been omitted in the graphical representation). Irregular situations are indicated by exceptional transitions.

## - Completing the net model

The described steps are optionally repeated for exceptional behaviour which is to be described in separate nets.

![](/api/attachments/NAMQXEW7/fulltext/images/2fe6c7b3c6a564d73aa9dd8d01e059946ecd005eabc77ef9c6c86e7a109fc86a.jpg)  
Fig. 23. Representation of a temporal restriction.

## 3.2. Adaptation of reference process models and reference object models

In Section 3.1 we have described a concept of incrementally synthesizing complex net models from small informal net fragments. Alternatively one might also develop process models and the corresponding object models by adaptation (“customization” or “tailoring”) of NR/T-net based reference models. Such reference models are, for example, available in the area of software development processes (see, e.g., [23]), or for certain business processes such as office equipment purchasing or personnel management. A similar concept is described in [31], where so-called “reusable process chunks” are introduced. These process chunks capture generic process knowledge in the context of requirements engineering.

The adaptation of reference models consists of four different steps which are briefly surveyed in the following.

## Step 1: Selection, analysis and validation of reference process and data models

First, it must be checked whether the available reference models are complete with respect to the process of the specific application area. If different reference models are available, one of them must be selected. This checking and selecting step can be supported by prototyping object structures and simulating processes in order to validate consequences of alternative choices.

## Step 2: Deleting objects and activities which are not needed

Then the generic model is tailored to the needs of the specific application. It must be decided which parts of the selected models are not required by the specific application. Tailoring can be supported by prototyping object structures and simulating processes. This step ends with a quality check to ensure that all objects which are required in the process model are defined in the object model and that all required operations are still contained in the process model.

## Step 3: Modifying naming of objects and activities

Names of objects and activities must be adopted to the requirements of the specific application environment. Again quality checks are necessary to ensure that the new naming is consistent.

![](/api/attachments/NAMQXEW7/fulltext/images/c9c317d5f87d269e2109fd4cd95c6a0faba64ce520622481d367bdf78314e120.jpg)  
Fig. 24. Global net model (excerpt).

## Step 4: Modifying object and net structures

This step does not only include modifications of existing object and net structures but also the definition of new objects and activities. This step can be supported by prototyping and simulation to evaluate the achieved models.

Both concepts to develop Petri net models as proposed in Section 3.1 and 3.2 can be combined for large process modelling projects. A part of the process model may be incrementally synthesized, whereas another part of the process model may be developed by customizing an available generic process model.

## 4. Conclusion and outlook

In this paper we have described an extension of high-level Petri nets, namely nested relation/transition nets (NR/T-nets). This novel type of nets allows system analysts to model the synchronization of operations on complex structured objects in distributed business applications.

Very large high-level Petri net models are usually not developed in one single step. We have, therefore, described concepts for the evolutionary development of NR/T-models:

\- constructing a global net model by iteratively evaluating, refining, formalizing and integrating informal net fragments,

\- adaptation of generic, net based reference process models and reference object models.

Both concepts are currently integrated into INCOME which is a commercial system for business process modelling, simulation and analysis [14,28]. The underlying concepts have been developed at the University of Karlsruhe [19]. INCOME extends the CASE\* environment of ORACLE [26] for information system development by Petri net based methods and tools. The basic components of the INCOME environment are

1. INCOME / Dictionary: database for development documents, which provides several quality checking facilities.

2. INCOME / Designer: graphical editor and visualization tool for high-level Petri nets which may be hierarchically structured.

3. INCOME / Simulator: simulation tool for Petri nets [20,22].

4. INCOME / Generator: generates C-code with embedded SQL statements from Petri nets, Entity/Relationship diagrams and some additional design information.

These tools are to be appropriately extended to support NR/T-nets.

Our current interest is especially in the area of developing Petri net based reference process models for important business areas. First experiences showed that these reference process models can help to reduce the process modelling effort significantly.

Another area of current research work is the integration of communication models and business process models. First results are described in [29]. The basic idea is to assign so-called conversation nets to some transitions in a given NR/T-net process model. By this it is expressed that a certain kind of conversation is related to an activity in the business process.

## Acknowledgements

I wish to thank Peter Sander, Wolffried Stucky and Jens Küsters for many fruitful discussions on NR/T-nets. Also, thanks to the anonymous referees for their useful comments and suggestions on an earlier version of this paper.

## References

[1] A. Borgida, Language Features for Flexible Handling of Exceptions in Information Systems, ACM Transactions on Database Systems 10(4) (1985) 565–603.

[2] M.L. Brodie and D. Ridjanovic, On the Design and Specification of Database Transactions, in: M.L. Brodie, J. Mylopoulos and J.W. Schmidt (Eds.), On Conceptual Modelling (Springer-Verlag, Berlin, 1984) pp. 278–306.

[3] W. Brauer, W. Reisig and G. Rozenberg (Eds.), Petri Nets: Central Models and Their Properties, Advances in Petri Nets 1986, LNCS 254 (Springer-Verlag, Berlin, 1987).

[4] C. Bussler and S. Jablonski, Process Modeling and Execution in Workflow Management Systems, in: A.R. Hevner and N.N. Karmel (Eds.), Proceedings of the

Third Annual Workshop on Information Technologies and Systems WITS'93, Orlando, FL, 1993, pp. 152–161.

[5] E.F. Codd, A Relational Model for Large Shared Data Banks, Communications of the ACM 13(6) (1970) 377-387.

[6] J. Eder, G. Kappel, A.M. Tjoa and A.A. Wagner, BIER: The Behaviour Integrated Entity Relationship Approach, in: S. Spaccapietra (Ed.), Proceedings of the 5th International Conference on Entity-Relationship Approach, Dijon, France, 1986 (North-Holland, 1987) pp. 147–168.

[7] C.A. Ellis and G.J. Nutt, Modeling and Enactment of Workflow Systems, in: M.A. Marsan (Ed.), Proceedings of the 14th International Conference on Application and Theory of Petri Nets 1993, Chicago, LNCS (Springer-Verlag, Berlin, 1993) pp. 1–16.

[8] S.J. Greenspan, A. Borgida and J. Mylopoulos: A Requirements Modeling Language and its Logic, in: M.L. Brodie and J. Mylopoulos (Eds.), On Knowledge Base Management Systems. Integrating Artificial Intelligence and Database Technologies (Springer-Verlag, Berlin, 1986) pp. 471–502.

[9] H.J. Genrich, Predicate/Transition Nets, in: W. Brauer, W. Reisig and G. Rozenberg (Eds.), Petri Nets: Central Models and Their Properties, Advances in Petri Nets 1986, LNCS 254 (Springer-Verlag, Berlin, 1987) pp. 207–247.

[10] D. Georgakopoulos, M. Hornick and A. Sheth: An Overview of Workflow Management: From Process Modeling to Workflow Automation Infrastructure, Distributed and Parallel Databases, September 1994.

[11] V. Gruhn and R. Jegelka, An Evaluation of FUNSOFT Nets, in: J.C. Derniame (Ed.), Proceedings of the Second European Workshop on Software Process Technology, LNCS (Springer-Verlag, Berlin, 1992).

[12] C.A. Heuser, E.M. Peres and G. Richter, Towards a Complete Conceptual Model: Petri Nets and Entity-Relationship Diagrams, Information Systems 18(5) (1993) 275–298.

[13] A. Horndasch, R. Studer and R. Yasdi, An Approach to (Office) Information System Design Based on General Net Theory, in: Proceedings IFIP TC8.1 TFAIS85 (North-Holland, 1985).

[14] INCOME User Documentation, INCOME/Designer, INCOME/Dictionary, INCOME/Generator, INCOME/Simulator. PROMATIS Informatik, Karlsbad/Germany, 1994.

[15] H. Ishii and K. Kubota, Office Procedure Knowledge Base for Organizational Office Work Support, in: B. Pernici and A.A. Verrijn-Stuart (Eds.), Office Information Systems: The Design Process (North-Holland, 1989) pp. 55–72.

[16] K. Jensen, Coloured Petri Nets. Basic Concepts, Analysis Methods and Practical Use, Vol. 1 (Springer-Verlag, Berlin, 1992).

[17] G. Lausen and H.J. Schek, Semantic Specification of complex objects, in: Proceedings IEEE-CS Symposium on Office Automation, Gaithersburg/USA, 1987.

[18] G. Lausen, Modelling and Analysis of the Behaviour of Information Systems, IEEE Transactions on Software Engineering 14(11) (1988) 1610–1620.

[19] G. Lausen, T. Németh, A. Oberweis, F. Schönthaler and W. Stucky, The INCOME Approach for Conceptual Modelling and Prototyping of Information Systems, in: CASE89. The First Nordic Conference on Advanced Systems Engineering, Stockholm/Sweden, 1989.

[20] T. Mochel, A. Oberweis and V. Sänger: INCOME/STAR: The Petri Net Simulation Concepts, Systems Analysis — Modelling-Simulation, Journal of Modelling and Simulation in Systems Analysis 13 (1993) 21–36.

[21] R. Medina-Mora, T. Winograd, R. Flores and F. Flores, The Action Workflow Approach to Workflow Management Technology, in: Proceedings of the Conference on Computer-Supported Cooperative Work CSCW'92 (acm Press, 1992) pp. 281–288.

[22] A. Oberweis, Checking Database Integrity Constraints while Simulating Information System Behaviour, in: Proceedings of 9th European Workshop on Application and Theory of Petri Nets, Venice/Italy, 1988, pp. 299–308.

[23] A. Oberweis, Workflow Management in Software Engineering Projects, in: S. Medhat (Ed.), Proceedings 2nd International Conference on Concurrent Engineering and Electronic Design Automation, Bournemouth/UK, 1994, pp. 55–60.

[24] A. Oberweis and G. Lausen, On the Representation of Temporal Knowledge in Office Systems, in: C. Rolland, M. Leonard and F. Bodart (Eds.), Proceedings AFCET/IFIP-TC8 Conference on Temporal Aspects in Information Systems (TAIS), Sophia-Antipolis/ France, North-Holland, 1988, pp. 131–145.

[25] A. Oberweis and P. Sander, The Specification of Complex Object Behaviour by High-Level Petri Nets, Forschungsbericht 254, Institut AIFB, Universität Karlsruhe, Karlsruhe/Germany, September 1992.

[26] ORACLE\* CASE User's Guide and Reference: CASE\* Dictionary, CASE\* Designer, CASE\* Generator. Oracle Corporation, Redwood City, 1992.

[27] A. Oberweis, P. Sander and W. Stucky, Petri Net Based Modelling of Procedures in Complex Object Database Applications, in: D. Cooke (Ed.), Proceedings IEEE Seventeenth Annual International Computer Software and Applications Conference COMPSAC 93, Phoenix/Arizona, 1993, pp. 138–144.

[28] A. Oberweis, G. Scherrer and W. Stucky, INCOME/STAR: Methodology and Tools for the Development of Distributed Information Systems, Information Systems 19(8) (1994) 643–660.

[29] A. Oberweis, T. Wendel and W. Stucky, Teamwork Coordination in a Distributed Software Development Environment, in: B. Wolfinger (Ed.), Proceedings GI-Fachgespräch Communication and Coordination in Distributed Corporate Application Systems, IFIP'94 Workshop, Hamburg/Germany (Springer-Verlag, Berlin, 1994) 423–429.

[30] J. Peckham and F. Maryanski, Semantic Data Models, ACM Computing Surveys 20(3) (1988) 153–189.

[31] C. Rolland and N. Prakash, Reusable Process Chunks, in: V. Marik, J. Lazansky and R.R. Wagner (Eds.), Proceedings 4th International Conference Database and Expert Systems Applications DEXA'93 (Springer-Verlag, Berlin, 1993) 655–666.

[32] H. Sakai, A Method for Entity-Relationship Behaviour Modeling, in: C.G. Davis, S. Jajodia, P.A. Ng and R.T. Yeh (Eds.), Entity-Relationship Approach to Software Engineering (North-Holland, 1983) pp. 111–129.

[33] P. Sander, Boolean Lattices of Nested Relations as a Foundation for Rule-Based Database Languages, Data and Knowledge Engineering 8(2) (1992) 93–130.

[34] P. Sander, Eine ordnungsbasierte Regelsprache für NF2-Relationen, Doctoral Thesis, Institut AIFB, Universität Karlsruhe, Verlag Shaker, Aachen/Germany, 1993 (in German).

[35] A.W. Scheer, Architecture of Integrated Information Systems. Foundations of Enterprise Modelling (Springer-Verlag, Berlin, 1992).

[36] H.-J. Schek and M. Scholl, The Relational Model with Relation-Valued Attributes, Information Systems 11(2) (1986) 137–147.

[37] A. Solvberg and C.H. Kung, On Structural and Behavioral Modelling of Reality, in: T.B. Steel and R. Meers

man (Eds.), Database Semantics (North-Holland, 1986) 205–221.

[38] E.S.K. Yu, An Organization Modelling Framework for Information Systems Requirements Engineering, in: A.R. Hevner and N.N. Karmel (Eds.), Proceedings 3rd Annual Workshop on Information Technologies and Systems WITS'93, Orlando, FL, 1993, pp. 152-161.

[39] M.M. Zloof, Query-By-Example: The Invocation and Definition of Tables and Forms, in: D.S. Kerr (Ed.), Proceedings International Conference on Very Large Data Bases, Framingham, MA, 1975, pp. 1–24.

![](/api/attachments/NAMQXEW7/fulltext/images/34d131bea4f718f012a15b50bfe42789e767df5e6264d3fc1dd85de55e264edd.jpg)

Andreas Oberweis received the Diploma degree in Industrial Engineering from the University of Karlsruhe, Germany. He received the PhD degree from the University of Mannheim, Germany, in 1990 and finished his inaugural dissertation at the University of Karlsruhe in 1995. Since December 1995 he is Professor for Information Systems at the University of Frankfurt/Main. His current research interests include busi-

ness process modeling, Petri nets, information system development and workflow management systems.
