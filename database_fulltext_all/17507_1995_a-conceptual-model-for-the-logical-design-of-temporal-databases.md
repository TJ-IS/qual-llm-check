---
otero_id: 17507
otero_key: "JHMVKJ32"
title: "A conceptual model for the logical design of temporal databases"
authors: "Debabrata Dey; Terence M. Barron; Veda C. Storey"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00044-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A conceptual model for the logical design of temporal databases

Debabrata Dey $^{a,*}$ , Terence M. Barron $^{b}$ , Veda C. Storey $^{c}$

$^{a}$ Department of Information Systems and Decision Sciences, Louisiana State University, Baton Rouge, LA 70803, USA $^{b}$ Department of Information Systems and Operations Management, University of Toledo, Toledo, OH 43606, USA $^{c}$ Graduate School of Business Administration, University of Rochester, Rochester, NY 14627, USA

## Abstract

Although widely advocated as a tool for the conceptual modelling of data, the Entity-Relationship (E-R) model $[4]$ and its extensions are generally lacking in constructs to model the dynamic nature of the real world, making them inadequate for designing temporal databases. This research first extends the E-R model to a Temporal Event-Entity-Relationship Model (TEERM), by introducing events as an additional construct. Second, a method is proposed for mapping this conceptual model into a temporal relational model for the logical design of temporal relational databases with a corresponding set of integrity constraints. The model is illustrated with an example and evaluated using a set of criteria proposed by Batini et al. $[2]$ . The model appears to be expressive, simple and easy to use, and should, therefore, aid the temporal database design process significantly.

Keywords: Temporal ER model; Conceptual design; Temporal database

## 1. Introduction

Recent years have seen a rapid growth of research interest in the area of temporal databases. Most of these research efforts have concentrated on representing temporal data by extending the relational model. However, the design process of temporal relational databases has not received much attention in the literature. On the other hand, the design process for conventional static or snapshot databases has been studied extensively [2,25,26,28]. In static database design, the designer starts with the well-known entity-relationship (E-R) model [4] for specifying the data requirements, and then transforms it into relational schemes according to a set of rules. This process has also been automated with the help of expert systems, such as the View Creation System [25]. Unfortunately, this process does not work for temporal relational databases. For example, consider the temporal relation shown in Table 1. The last column in this table, designated TS, represents the time-stamp attribute which is appended to a static relation scheme to capture the time-varying nature of the information. Although this scheme (without the time-stamp attribute) would have been an acceptable design for a static relational database, $^{1}$ it clearly suffers from data redundancy as a temporal relation scheme. Data redundancy is a serious problem in any database, since it poses problems in terms of preservation of data integrity and occupies extra storage. Hence, the above scheme is not a good design for a temporal relational database.

Table 1  
EMPLOYEE: A temporal relation

<table><tr><td>EMP#</td><td>ssn</td><td>LName</td><td>FName</td><td>salary</td><td>dept</td><td>TS</td></tr><tr><td>3025</td><td>086630763</td><td>Lyons</td><td>James</td><td>15K</td><td>dep1</td><td>[1,3)</td></tr><tr><td>3025</td><td>086630763</td><td>Lyons</td><td>James</td><td>15K</td><td>dep2</td><td>[3,5)</td></tr><tr><td>3025</td><td>086630763</td><td>Lyons</td><td>James</td><td>20K</td><td>dep2</td><td>[5,9)</td></tr><tr><td>3025</td><td>086630763</td><td>Lyons</td><td>James</td><td>22K</td><td>dep2</td><td>[9,13)</td></tr></table>

We attribute this problem to the lack of a design theory for temporal relational databases. For static databases, there exists a well-established design process, along with normalization theory to evaluate the quality of a design thus obtained. To develop a general theory for designing temporal databases, three issues have to be addressed: (i) representation of temporal data in a conceptual model, (ii) transformation of the conceptual model to a set of temporal relation schemes, and (iii) evaluation of the design using a temporal extension of the existing normalization theory. Dey [7] proposes a structure for temporal relations, and extends normalization theory to include temporal relations. However, the design process for temporal relational databases is not examined there.

Thus, the objectives of this research are to develop a temporal conceptual model, and to show how this model can be used for the logical design of temporal relational databases. To these ends, we propose an extension of the E-R model, which has been widely advocated as a tool for the conceptual modelling of data. The E-R model, however, can at best model a “snapshot” of the real world at any point of time; it does not contain specific constructs to model the dynamic aspects of the real world. As a result, the E-R model is an inadequate tool for temporal database design.

Schiel [22] makes a useful observation regarding the required constructs in a data model. He notes that there are three kinds of objects in the real world: (i) Entities, (ii) Relationships and (iii) Events. In the Entity-Relationship (E-R) model, data about objects are stored in two ways. Information about a single entity is captured in its attributes. Information about an association between two or more entities is captured in the relationship (and its attributes) that binds them. Because the viewpoint of the E-R model is the design of “snapshot” databases, i.e. those that reflect the state of affairs at a single time point (usually the present), it omits events. Informally, events are those occurrences that induce changes in one or more instances of an entity or a relationship; so they take on considerable importance when designing a temporal database. Furthermore, even in snapshot databases, knowledge of the relevant events is useful in defining transactions and some kinds of integrity constraints. Since events by nature belong to the time domain, their incorporation as an addition to entities and relationships must strictly increase the semantic expressiveness of the resulting conceptual modelling language.

This paper makes two contributions to the literature. First, we propose a temporal conceptual model, called the Temporal Event-Entity-Relationship Model (TEERM). The TEERM adapts the usual constructs of the E-R model (entities and relationships), with events added to enhance the semantic richness of the model. This model is thus a strict superset of the conventional E-R model, and allows us to model the dynamic behaviour of entities and relationships in addition to incorporating advanced modelling techniques such as aggregation, generalization and specialization that are available in Extended E-R modelling [28]. Second, we demonstrate how the TEERM can be used for the logical design of temporal relational databases by showing how to translate each construct of the TEERM into a temporal relational model. We believe that designers of temporal as well as snapshot databases will greatly benefit from the results of this research.

The remainder of this paper is organized as follows. A brief review of previous work on temporal conceptual models is presented in section 2. Section 3 formally describes the components of the model. Section 4 discusses the role of the TEERM in logical database design. The model is then illustrated with a banking example in section 5. Section 6 concludes the paper and offers suggestions for future research.

## 2. Previous research

Conceptual design has long been recognized as a crucial phase of database design $[2]$ , with the entity-relationship (E-R) model $[4]$ widely used for this purpose. The E-R model, however, is an inadequate tool for temporal database design.

Extensions to the E-R model have been proposed that allow one to model temporal data to a limited extent. Klopprogge and Lockemann [18,19] attempt to extend the E-R model to include time based on perception and representation. Elmasri et al. [11–13] propose an extended E-R model for temporal data. They classify objects as conceptual and temporal. The former is used to capture the static nature of the world, whereas the latter materializes the active role that conceptual objects play in the temporal dimension. These researchers also discuss temporal constraints among the roles that an entity can play, and extend the GORDAS language for temporal E-R databases. Kouramajian and Elmasri [20] discuss how their temporal E-R model can be mapped into temporal extensions of the relational model. Ferg [14] proposes RAKE (Relationship-Attribute-Key-Entity) diagrams that represent temporal attributes as relationships between entities and attribute domains, and temporal relationships by introducing time as another entity participating in the relationship. Tauzovich [27] introduces the concepts of snapshot and lifetime cardinalities for representing temporal relationships.

While the above extensions are improvements over the traditional E-R model, none of them explicitly models events. The incorporation of events into the E-R model was first proposed by Dubois et al. [10] in their ERAE (Entity-Relation-Attribute-Event) data model. There are, however, some basic differences between that model and our proposal. The ERAE data model, designed primarily for requirement analysis, emphasizes instances, not types of entities, relationships and events. Since the designer of a temporal database is more concerned with the database schemes and hence with the classes of different kinds of objects, ERAE model is not directly useful for temporal database design. Furthermore, the ERAE model uses events only to express dynamic constraints, whereas we use events to provide an enriched view of the data in addition to expressing certain integrity constraints.

Theodoulidis et al. [29] use events as a type of object in their ERT (Entity-Relationship-Time) model. Events were also used in the context of active databases by Gehani et al. [16]. These researchers, however, use events to represent internal processes; they do not provide real world events as a data abstraction mechanism. Dey et al. [9] examine how real world events, in addition to capturing the temporal semantics of data, can provide useful information on the nature of data items and integrity constraints. Different types of event classification are described in terms of their significance within a data model.

## 3. Temporal event entity relationship model

This section describes the different components of the Temporal Event-Entity-Relationship Model (TEERM). The symbolic representations of these components are shown in Fig. 1. The following definitions are required. The term universe refers to the entire real world. The object system refers to the information system that is to be built, so the object system is the subset of the universe that represents the application at hand. We sometimes refer to the object system simply as the system. It is assumed that the time line is continuous, i.e., isomorphic to the set of real numbers. In other words, it is the metric space of $(0,\infty)$ . The time horizon of an object system refers to a subset of the time line during which the object system serves its useful purpose.

<table><tr><td>Symbol</td><td>Meaning</td></tr><tr><td></td><td>Entity</td></tr><tr><td></td><td>Static Relationship</td></tr><tr><td></td><td>Quasi-static Relationship</td></tr><tr><td></td><td>Temporal Relationship</td></tr><tr><td>—○ name</td><td>Static Attribute</td></tr><tr><td>—● ssn</td><td>Surrogate Attribute</td></tr><tr><td>—● last_check_no</td><td>Quasi-static Attribute</td></tr><tr><td>—● int_rate</td><td>Temporal Attribute</td></tr><tr><td></td><td>Composite Attribute</td></tr><tr><td>address city zip</td><td>Event</td></tr><tr><td>Promotion</td><td></td></tr></table>

Fig. 1. Basic symbols for temporal event entity relationship model

## 3.1. Components adapted from the E-R model

The three basic components are adapted from the E-R model: (i) entities, (ii) relationships, and (iii) attributes.

Entity An entity is a “thing” or an object that has a separate identity in the universe. Each entity typically possesses certain properties. An entity type is defined as a set of entities with a similar set of properties. For brevity, we refer to an entity type as an entity in the remainder of the paper; an entity instance is specifically distinguished from an entity type.

Relationship A relationship type is an association among two or more entity types. The number of entities that are associated is called the arity of the relationship. We will use the term relationship to refer to a relationship type, and, when appropriate, mention relationship instances specifically.

In order to formally describe the dynamic nature of certain relationships, we introduce the concept of a null relationship instance, which is a relationship instance of any arity whose entity instances are all null. $^{2}$ A change of a relationship instance is then defined as a change in some or all of the participating entities. Thus, a change in a relationship instance could be of three types:

(1) a birth, where all entity instances of a null relationship instance change to non-null values,

(2) a death, where all entity instances of a non-null relationship change to null values, and

(3) a transition, where some entity instances of a non-null relationship change to non-null values.

A relationship is static if none of its non-null instances changes over time (within the time horizon of the object system); otherwise it is dynamic. The relationship between a mother and a child is static, whereas the relationship between a manager and an employee is dynamic.

Each entity that participates in a relationship has min-max cardinalities attached to it. The minimum (maximum) cardinality represents the least (most) number of relationship instances in which any instance of that entity can participate at any given time point. The min-max cardinalities are typically written next to the line joining the entity with the relationship. A cardinality is represented by a “\*” if it is greater than 1 (i.e., many) and not known at design time.

Attribute: Attributes represent properties of entities and relationships. We consider only single-valued attributes, that is, any attribute can have at most one value at any time point. (Multivalued attributes are modeled as entities.)

![](/api/attachments/JHMVKJ32/fulltext/images/936f4d0b6f0af79cc16f2e00619c59ca09baeddd5dd9f7b02bd87783517df2ed.jpg)  
Fig. 2. Classification of relationships and attributes.

An attribute is static if it does not change over time (within the time horizon of the object system); otherwise it is dynamic. For example, "date-of-birth" is a static attribute, whereas "salary" is dynamic. An attribute may be composed of several elementary attributes. Such an attribute is referred to as a composite attribute, for example "address." If a set of one or more attributes uniquely identifies an entity, then it is called a candidate key of that entity. Components of any candidate key must be static. One such candidate key is chosen for the object system as a unique identifier of that entity, and is called the surrogate or the key.

Although dynamic attributes and relationships usually change over time, the history of only some of these attributes and relationships may be relevant for an object system. For example, it may be useless in a banking system to store the complete history of a customer's address. Any dynamic relationship or attribute whose history is not relevant for an object system is referred to as quasi-static. The remainder of the dynamic relationships and attributes, whose temporal behaviour is of interest for a given system, are referred to as temporal. $^{3}$ (Fig. 2).

Since an entity may be viewed as an aggregation of attributes, we assume that the temporal behaviour of an entity is expressible in terms of the time-dependency of its attributes, so it is not necessary to include any extra construct such as a temporal entity in our model.

## 3.2. Events in TEERM

In order to understand the nature of events and represent them correctly, different types of events must be defined and classified.

Definition 3.1 An event is an occurrence that results in changes in the states of one or more of the following within the object system: entity instances, relationship instances, and attribute values (of entity and/or relationship instances).

An event type is defined to be a set of event occurrences that induce changes in the same set of entities and relationships. For example, the event type “Promotion” represents the set of all promotions granted to the set of all employees during the time horizon of the system. In the remainder of this discussion, an event type is referred to simply as an event; an event occurrence is specified and clearly distinguished from an event type. An event type is represented as a rounded rectangle as shown in Fig. 1.

The distinction among events, entities and relationships depends largely on the perception of the user. It is possible that a few events may be viewed as entities (or relationships) by certain users. For example, an event “Sale” may also be viewed either as an entity “SALE,” or as a relationship “sale” between two entities “CUSTOMER” and “PRODUCT,” implying that there might not exist any unique representation of an object system. This, however, need not be considered as a shortcoming of the model. It is well-known that, in the E-R model, the distinction between entities and relationships is not always clear [2,17]. For instance, consider the following relationships that can also be modeled as entities:

```txt
Relationships Entity
EMPLOYEE works on PROJECT ASSIGNMENT
CUSTOMER buys PRODUCT SALE
PATRON borrows BOOK LOAN
```

Clearly, the E-R model does not possess the uniqueness property; $^{4}$ neither does the relational model, since an E-R representation of a system could result in several alternative relational schema. As a general guideline, we recommend that, in cases where an entity or a relationship can also be represented as an event, it should be modeled as an event. This is because events can specify useful integrity constraints in addition to providing an alternative view of data.

![](/api/attachments/JHMVKJ32/fulltext/images/5ac1af916a298e0c19fa8144bf3ad2ec6230fe9d15deb9c6647d21c1f9911396.jpg)  
Fig. 3. Classification of events.

Each event must have a time attribute representing the time of occurrence of event instances. Certain events may also have attributes other than the time attribute. For example, the event “Promotion” may have “granting-Manager,” “promoted-employee,” etc. as attributes. Since events have indeterminate lifetimes, their properties are independent of time $[10]$ , therefore, all attributes of an event must be static. Event attributes are denoted in a fashion similar to entity and relationship attributes.

## Classification of events

We classify events based on the instances of the different entities needed to model the system, as shown in Fig. 3. Each event can be classified as either singular or recurrent for every entity relative to the system being modeled.

Definition 3.2 An event V is said to be singular for an entity E associated with the event V, relative to system X, if and only if during the lifetime of every instance $e \in E$ within X, at most one event instance $v \in V$ occurs.

Definition 3.3 An event V is said to be recurrent for an entity E relative to system X if and only if it is not singular for E relative to X.

The distinction between singular and recurrent events depends on the entities associated with the events. As a result, an event may be recurrent with respect to some entity while it is singular for some other. For example, the event “Publication of books” has associated entities “BOOK,” “AUTHOR” and “PUBLISHER.” For every instance of a book, $^{5}$ there exists only one occurrence of publication, although there may be more than one occurrence of publication for a specific author or publisher instance. As a result, this event is singular for the entity “BOOK,” but recurrent for the entities “AUTHOR” and “PUBLISHER.”

Recurrent events can again be divided into two classes. Periodic events have a fixed time interval between any two successive event occurrences; aperiodic events do not have this property. Monthly payroll processing is an example of a periodic event, whereas transfer of employees among departments may be considered as an aperiodic event.

## Connection of events with other components

Events are connected to other components of the model. These connections capture the semantics of the data and are classified as:

Event-to-event: An arrow from one event to another implies that every occurrence of the former is accompanied by an occurrence of the latter. Similarly, a double-sided arrow between two events implies that they occur simultaneously. Such connections may lead to useful integrity constraints. For example, an arrow from “Promotion” to “Pay-raise” indicates that every promotion is accompanied by an increase in salary.

Event-to-entity: Event-to-entity connections are represented by a line. Typically, a connection between an event and an entity indicates that the entity takes part in the event. The letter (within a circle) on the line joining the event to the entity indicates whether the event is singular or recurrent for that entity, with “S” representing singular and “R,” recurrent. As shown in Fig. 4, the event “Pay Revision” is recurrent for the entity “PH.D. STUDENT.”

![](/api/attachments/JHMVKJ32/fulltext/images/f21c850116f9c4ac54a683b7c5cb5214c615a34b28337e9dd0af3ace7ebc132b.jpg)  
Fig. 4. Connections between events and attributes.

Event-to-relationship / attribute: A dashed arrow from an event to a relationship (or an attribute) represents that the event causes the relationship (or the attribute) to change. For instance, a dashed arrow from “Pay-raise” to “salary” implies that salary changes with pay-raise. Similarly, an event “Project Assignment” might change the relationship “EMPLOYEE works on PROJECT.”

Relationship /Attribute-to-event: A dashed arrow from a relationship (or an attribute) to an event represents the fact that a change in the relationship (or the attribute) causes the event to occur. For example, if the stipend of a Ph.D. student is determined based on his/her grade point, then a change in the grade point should result in revising the stipend. This is modeled by a dashed arrow from the attribute “grade-point” to the event “Pay Revision,” and another dashed arrow from the event “Pay Revision” to the attribute “stipend” as shown in Fig. 4. This connection implies that a report should be generated for pay revision every time the grade point of a student changes. Since we assume that the temporal nature of an entity is completely expressible in terms of its attributes and relationships, it suffices to consider only relationship-to-event and attribute-to-event connections; we do not have to consider entity-to-event connections.

Data modelling techniques such as aggregation, generalization and specialization can also be used with events. For example, a generalization hierarchy of events where every instance of a “Transaction” event could be either a “Deposit,” a “Withdrawal,” or a “Fund Transfer” may be useful in a banking system.

## 3.3. Design implications of events in the TEERM

Each event that interacts with (or occurs within) the system affects the internal states of some information objects in the system. These changes take effect by changing one or more attributes or relationships. Thus, each event can be used effectively to identify some of these attributes and relationships that might be overlooked otherwise. Furthermore, as discussed below, more information about these attributes and relationships is available from studying the nature of these events. The following design implications are easily verified:

Implication 3.1 Let $V_{1}, V_{2}, \ldots, V_{n}$ be the only events that affect an attribute $A$ of entity $E$ . If $V_{1}, V_{2}, \ldots, V_{n}$ all occur simultaneously, and if $V_{1}$ is singular for $E$ , then $A$ is static.

An example is “date\_of\_birth” of a person. The only singular event that affects this attribute is the birth of a person.

Implication 3.2 Let R be a relationship connecting entities $E_{1}, E_{2}, \ldots, E_{n}$ . If V is the only event that affects R, and if V is singular for at least one $E_{i}, I \leq i \leq n$ , then R is a static relationship.

An example of a static relationship is that between the entities “MOTHER” and “CHILD;” the associated event is “Child Birth.” This event is singular for the entity “CHILD,” whereas it may be recurrent for the entity “MOTHER”.

Implication 3.3 A static attribute or a static relationship must not be updated.

Implication 3.4 If an attribute or a relationship is affected by two or more events all of which are not simultaneous, then it is dynamic.

Implication 3.5 If event V is recurrent for entity

E, and if V affects attribute A of E, then A is a dynamic attribute.

“Salary” is an example of a dynamic attribute of the entity “EMPLOYEE” and “EMPLOYEE” works on “PROJECT” is an example of a dynamic relationship. Events such as “Promotion” and “Pay-raise” affect “salary,” whereas the relationship “works on” is affected by the event “Project Assignment.” Existence of dynamic attributes and relationships usually imply that there are some events that affect these attributes and relationships. This could be used for checking the completeness of a design.

Implication 3.6 If there exists a set of attributes affected by the same set of simultaneous events, then these attributes have the same time-dependency (i.e., when they change, they all change simultaneously).

For example, whenever a person moves to a new address, all of the attributes constituting the address (i.e., street, city, state, zip) change. Of course, if the attributes constituting the address do not change together, then the recurrent event “moving” may be partitioned into several events such as moving to a new state, moving to a new city, moving to a new street, etc.

Implication 3.7 If a connection exists from event $V_{1}$ to $V_{2}$ ( $V_{1} \rightarrow V_{2}$ ), and if only $V_{i}$ affects the attribute $A_{i}, i = 1, 2$ , then a change in $A_{1}$ of some entity or relationship instance is accompanied by a change in $A_{2}$ of that (or some other) entity or relationship instance.

Since every occurrence of $V_{1}$ is accompanied by an occurrence of $V_{2}$ , a change in $A_{1}$ (which implies an occurrence of $V_{1}$ ) is accompanied by a change in $A_{2}$ . For example, if every “Promotion” comes with a “Pay-raise”, then a change in “rank” would imply a change in “salary.”

Implication 3.8 If two entities $E_{1}$ and $E_{2}$ are connected to the same event V, then usually there is a relationship that connects $E_{1}$ and $E_{2}$ .

For some applications, a few events may be of primary importance. For example, consider the event “Flight” of a specific airline, having associated attributes flight#, city\_from, city\_to, departure\_time, arrival\_time, equipment, etc. Such events are typically modeled as entities in the E-R model. Other examples include events such as marriages, births, and matches between any two sports teams. In general, if an event has attributes of interest, this indicates that it is of considerable importance to the system.

## 4. Logical design for temporal relational databases

This section discusses how the TEERM can be used for the logical design of temporal relational databases. In order to design such a database, two major decisions are required. First, we must decide on the structure (or the view) of the temporal relations; and second, we must decide on how to represent each component of the TEERM in the temporal relational model.

Two major approaches have been proposed for the structure of temporal relations: (i) the tuple time-stamping (or, 1NF) view [3,24,21] which the time-stamps are part of each tuple and characterize the whole tuple, and (ii) the attribute timestamping (or, non-1NF) view [5,15] where the time-stamps are associated with every attribute. Both approaches have their merits and limitations. This research employs the tuple timestamping (1NF) view because it is very close to the view of relations in the traditional relational model. Several other reasons for favouring the tuple time-stamping method can be found in [23,21,7]. Dey [7] proposes a structure for temporal relations based on tuple time-stamping that is used as the target model for this research. As Ahn [1] shows, however, the above two views of temporal relations are equivalent in the sense that one can be transformed into the other without loss of information. We first describe briefly the formal structure of temporal relations and then discuss how the TEERM can be mapped into that structure.

## 4.1. Formalization of relations

This subsection summarizes the approach adopted in this research. It is assumed that the time space is formed by one or more orthogonal time lines. For example, if both transaction time and valid time are supported, then these time lines serve as the basis vectors of the two-dimensional time space. An elementary subset of the time space is formed by the union of a finite number of time intervals and time points. Let T denote the family of all elementary subsets of the time space. The time-stamp attribute is denoted by TS and assumes values in T.

A relation scheme R is a set of attribute names $\{A_{1}, A_{2}, ..., A_{n}\}$ , only one of which may be a timestamp TS. Corresponding to each attribute name $A_{i}$ , is a set $D_{i}, 1 \leq i \leq n$ , called the domain of $A_{i}$ . If $A_{i} = TS$ , then $D_{i} = T$ . Let $D = D_{1} \times D_{2} \times ...D_{n}$ . D is called the domain of R. Then, a tuple x over R is a function from R to its domain D.

Two tuples $x$ and $y$ on a relation scheme $R$ are value-equivalent (written $x \simeq y$ ) if for all $A \in R$ , ( $A \neq TS \Rightarrow y(A) = x(A)$ ) holds. Value-equivalent tuples are not allowed in a legal temporal relation; they must be coalesced into a single tuple. This is analogous to the elimination of duplicates in the relational model. The coalescence operation (denoted by $\oplus$ ) on two value-equivalent tuples, $x$ and $y$ , on relation scheme $R$ produces a tuple $z$ on $R$ given by:

$$
\begin{array}{r l} z = x \oplus y & \Rightarrow (x \simeq y) \wedge (\forall A \in R (A \neq T S \Rightarrow z (A) \\ & = x (A)) \wedge (T S \in R \Rightarrow z (T S) \\ & = x (T S) \cup y (T S)) \end{array}
$$

A relation r on the scheme R is a finite collection of tuples x on R, such that no two of its members are value-equivalent.

The usual meaning of a candidate key as a minimal object surrogate is retained. In other words, a candidate key of a relation of this structure is one that is a candidate key (in the usual static sense) of all possible snapshots derivable from that relation. This implies that a candidate key, as in the static case, is time-invariant. Only one of several candidate keys is chosen as the primary key. A primary key no longer uniquely identifies each tuple (which represents only one of several possible states of an object). A combination of primary key and time-stamp TS can however uniquely identify each tuple. Let r be any relation on scheme R with primary key K. The following constraints on r and K are imposed:

(1) For all $x, y \in r$ , $x(K) = y(K) \Rightarrow (x = y) \vee (TS \in R \Rightarrow x(TS) \cap y(TS) = \emptyset)$ . This implies that no object can exist in two temporal states simultaneously. For static relations, this condition reduces to key uniqueness for each tuple.

(2) For all $x \in r$ , $x(K)$ cannot be null. This ensures that information is stored only for the identifiable objects.

(3) For all $x \in r$ , $TS \in R \Rightarrow x(TS) \neq \text{null}$ . In other words, information is not stored for any temporal state of an object if that state cannot be identified.

Definition 4.1 (Temporal Dependency) Let $r$ be a relation on scheme $R$ , $TS \in R$ , and let $K$ be its primary key. Let $X, Y \subset (R - \{TS\})$ . The relation $r$ is said to satisfy the temporal dependency (TD) $X \stackrel{T}{\to} Y$ if there exist tuples $t_1, t_2 \in r$ such that (i) $t_1(K \cup Y) = t_2(K \cup Y)$ and (ii) $t_1(X) \neq t_2(X)$ . The temporal dependency is trivial if $Y \subset K$ .

Existence of temporal dependencies implies that values of certain attributes must be duplicated across tuples even when they do not change. This will result in redundancy and extra storage. Such problems can be avoided by restricting relations to be in temporal normal form as defined below.

Definition 4.2 (Temporal Normal Form) Let R be a relation scheme, and let F be a set of functional, multi-valued and temporal dependencies over R. R is in temporal normal form (TNF) with respect to F if R is in 4NF with respect to F and all temporal dependencies implied by F over the attributes of R are trivial.

## 4.2. Conceptual modelling

In this section, we suggest a step-by-step process of conceptual modelling leading to development of the temporal event-entity-relationship diagram for the application. Note that this is not a one-pass procedure. Sometimes, identification or analysis of a construct at some step may lead to a revision of the results from a prior step. In other words, the process is iterative. The basic steps are:

Step 1. Identification of entities and their attributes: As in the case of static database design, the modelling starts with identification of the relevant entities and their attributes. Attributes of an entity describe its relevant properties. It is not always clear whether a real-world object should be modeled as an entity or as an attribute and a good heuristic is that, if several properties could be associated with an object, it should be modeled as an entity [2]; the associated properties become attributes of the entity. If the object is single-valued with an atomic structure, it should be modeled as an attribute. Multi-valued or repeating attributes are modeled as entities [25].

Step 2. Identification of relationships and their attributes: In this step, we find the relationships among the relevant entities and the min-max cardinalities of these relationships. Some of these relationships may have attributes of their own. It is possible that this step may lead to discovery of new entities. The designer should verify whether relationships of arity greater than two could be broken into several binary relationships. It is also necessary that all the redundant relationships be removed from the model. For example, consider the three relationships shown in Fig. 5. Clearly, the relationship “resident of” between entities “PERSON” and “STATE” is redundant. For, once we know the name of the city in which a person lives in and the state to which that city belongs to, the state of residency for that person is automatically known. The relationship between “PERSON” and “STATE” is then redundant and must be removed from the model.

Step 3. Identification of events: In this step, the relevant events are identified and then classified according to the scheme presented in Fig. 3. Various connections (namely, event-to-event, event-to-entity, event-to-relationships and event-to-attributes) are established. If an event can also be modeled as an entity or as a relationship, it should be modeled as an event. Identification of events may lead to discovery of entities, relationships and attributes that might have been overlooked during the earlier steps. This may, in turn, lead to identification of other missing events.

![](/api/attachments/JHMVKJ32/fulltext/images/1e4dcef5c0765f2241be4c6332320f97b686d65bfae09a0afc52d91cdc3761fb.jpg)  
Fig. 5. A redundant relationship.

Step 4. Classification of relationships and attributes: In this step, all the relationships and attributes identified so far should be classified into static and dynamic. Further classification of dynamic relationships and attributes into temporal and quasi-static should be postponed till later. The design implications of events, as outlined in section 3.3, could be used in this step to analyze the nature of the relationships and the attributes.

Once these steps are applied repetitively, to the satisfaction of the designer, an integrated view of the application will result in the form of a TEER diagram. This diagram could now be used to obtain the logical scheme of the database. We recommend application of the following guidelines before the formal mapping is carried out.

(1) Decompose all composite attributes into their more elementary components. Identify any multi-valued or repeating attributes, and convert them to entities.

(2) Infer any integrity constraints that can be derived from the TEER diagram; for example, a static attribute can never be changed.

(3) Classify all dynamic relationships and attributes as temporal and quasi-static. Note that such a classification is often based on the trade-off between the cost of storing extra data and the benefit of having more information. More discussion on such trade-off analysis is found in [8].

(4) Verify that all relationships have min-max cardinalities specified for all participating entities.

(5) Retain only those events that have attributes (other than the implicit time attribute) of their own, and delete all other events.

(6) Determine whether it is possible to represent some of the attributes of the remaining events as attributes of other entities and relationships. If so, check whether the event view is a natural view for the user. If not, eliminate these events also. Note that a representation that has events might have some kind of redundancy due to the duality between event and entity representations. In some applications, such redundancies may be desirable; however, there should be proper enforcement of a set of integrity constraints to account for this type of redundancy.

## 4.3. Mapping of the TEERM components

This section discusses how different components of the TEERM can be mapped into the above temporal relational model.

## Representation of entities and events

Let E be an entity that has one or more temporal attributes. We represent E as

$E:\left[\underline{SA},CA,TA\right]$

where the set SA constitutes the surrogate (the unique identifier of each instance of E); CA is the set of static and quasi-static attributes; and TA is the set of temporal attributes. The possibility that CA and/or TA might be empty is not excluded. The set TA is now partitioned into k smaller subsets $TA_{i}, 1 \leq i \leq k$ , i.e.,

$$
\bigcup_ {i = 1} ^ {k} T A _ {i} = T A, \bigcap_ {i = 1} ^ {k} T A _ {i} = \varnothing .
$$

Here each $TA_{i}, 1 \leq i \leq k$ , is a set of attributes that have the same time dependency; in other words, all attributes contained in set $TA_{i}$ can change only simultaneously. Now the entity E can be transformed into the following temporal relational schemes.

$E:\left[\underline{SA},CA\right]$

$$
E T _ {i}: \left[ \underline {{{{S A}}}}, T S, T A _ {i} \right], \forall_ {i}, 1 \leq i \leq k.
$$

The underlined attributes in each relation scheme represent the primary key for that scheme.

## Integrity constraints

The following integrity constraints should be enforced:

Existence constraint: Any relation instance on the schemes E and $ET_{i}$ , $1 \leq i \leq k$ , cannot have null values for SA and TS.

Referential constraint: There should be a referential constraint from a relation on scheme E to a relation on scheme $ET_{i}$ , SA being the foreign key of $ET_{i}, 1 \leq i \leq k$ . This is because $ET_{i}, 1 \leq i \leq k$ , may be viewed as a weak entity, and its existence is dependent on E.

Others: Static attributes should not be updated.

Events can be treated in a fashion similar to entities for representation in the temporal relational model. For each event, we create a relation on a scheme that contains all the attributes of that event including the time attributes. As noted earlier, events can have only static attributes. Thus, the relation resulting from an event will always be a static relation, with a user-defined time attribute as the event time.

There are several important issues in the representation of events in a relational model that are discussed bellow:

Primary key: Most relevant events typically have some artificial surrogate to identify each occurrence uniquely. For example, "transaction\_no" is a surrogate for the event "Transaction" and "flight\_no" is a surrogate for the event "Flight." However, there may be other events that do not have such artificial surrogates. Event time and/or keys of entities participating in the event may be used as the primary key. For instance, "ssn" of a husband and a wife could be used as the primary key of the event "Marriage". $^{6}$

Event-to-entity connections: If an event is represented as a relation, then the relevant event-to-entity connections should be represented for navigational purposes. If the primary key of the participating entity already occurs as an attribute of the event, then the link is automatically established. Otherwise, a new relation is created whose primary key is the concatenation of the primary keys of the entity and event relations. For example, the connection between the event “Flight” and the entity “PASSENGER” is represented by creating a new relation with “flight\_no” and “ssn” as its primary key.

Redundancy and integrity constraints: Representing events in relations often causes data redundancy, because the same facts may be stored twice – once in an event occurrence, and a second time in the history of attributes or relationships. Proper integrity constraints should be enforced to ensure that the redundant data are consistent.

## Representation of relationships

The transformation rules for relationships largely depend on the number of entities that participate in the relationship, the min-max cardinalities, and whether the relationship is temporal or static, as outlined below.

Unary /binary static and quasi-static relationships: Consider a binary relationship of the form “ $E_1$ verb phrase $E_2$ .” The possibility that $E_1 = E_2$ is not excluded, that is, unary relationships are considered as a special case. If the min-max cardinalities of an entity that participates in a binary relationship are (1,1), then the relationship is represented by adding the surrogate of the other entity as a foreign key (if it does not already exist) in the scheme of the relation that represents the entity with the (1,1) cardinalities. When neither entity has (1,1) cardinalities, a separate relation is created to represent the relationship. The primary key of this relation consists of the concatenation of the surrogates of the participating entities; the relationship attributes are non-keys. $^7$

Other static and quasi-static relationships: Relationships involving more than two entities should be represented by creating a new relation whose primary key is formed by concatenating the surrogates of all the entities that take part in the relationship. $^{8}$

Temporal relationships and relationship attributes: Let $R$ be a temporal relationship involving entities $E_i, 1 \leq i \leq n$ . Let $SA_i$ be the surrogate attribute of $E_i$ . $R$ is then represented by creating a new relation whose scheme is given by $R: [\underline{SA_1}, \underline{SA_2}, ..., \underline{SA_n}, TS]$

If R has attributes, they could be partitioned into two sets: a set CA of static and quasi-static attributes and a set TA of temporal attributes. We do not exclude the possibility that CA and/or TA might be empty. The static attributes of the relationship can simply be added to the relation scheme that represents the relationship R.

$$
R: \left[ \underline {{S A _ {1}}}, \underline {{S A _ {2}}},..., \underline {{S A _ {n}}}, T S, C A \right]
$$

The set TA is then partitioned into k smaller subsets $TA_{i}, 1 \leq i \leq k$ , i.e.,

$$
\bigcup_ {i = 1} ^ {k} T A _ {i} = T A, \bigcap_ {i = 1} ^ {k} T A _ {i} = \varnothing .
$$

Here each $TA_{i}, 1 \leq i \leq k$ , is a set of attributes that have the same time dependency. We now create k new relations on the relation schemes given by

$$
R T _ {i}: \left[ \underline {{S A _ {1}}}, \underline {{S A _ {2}}},..., \underline {{S A _ {n}}}, T S, T A _ {i} \right] \forall i, 1 \leq i \leq k
$$

## Integrity constraints

The following integrity constraints should be enforced:

Existence constraint: Any relation instance on the schemes R and $RT_{i}, 1 \leq i \leq k$ , cannot have null values for $SA_{j}, 1 \leq j \leq n$ , and TS.

Referential constraint: There should be a referential constraint from a relation on scheme $E_{j}$ to a relation on scheme R, with $SA_{j}$ being the foreign key of R, $1 \leq j \leq n$ . There should also be a referential constraint from a relation on scheme R to a relation on scheme $RT_{i}$ , with $\{SA_{1}, SA_{2}, ..., SA_{n}\}$ being the foreign key of $RT_{i}$ , $1 \leq i \leq k$ .

Others: The following additional integrity constraints are easily derived:

(1) Statistic attributes should not be updated.

(2) If a static relationship is represented using a foreign key, then the foreign key should not be updated.

(3) If a static relationship is represented by a new relation, then no tuple of that relation should be deleted.

## 4.4. Temporal normal form and the TEERM

We will now show that the proposed design method results in temporal relations that are in temporal normal form. This further demonstrates the usefulness of this approach.

Theorem 4.1 Let R be a relation scheme produced using the representation scheme outlined above. If R is in fourth normal form, then R is in temporal normal form.

Proof. The scheme R could be produced from any one of the several different TEERM constructs using the above representation scheme. Let us first consider the case that R is produced from an event. Since events do not have dynamic attributes, $TS \notin R$ , so R must be in TNF if it is in 4NF. A similar argument is true about event-to-entity connections, because these associations are also static. It follows that we need to consider relation scheme R that is produced only from either temporal attributes or temporal relationships. Let $X, Y \subset R$ . Assume that the non-trivial TD $X \xrightarrow{T} Y$ exists. This means that there are $t_1, t_2 \in r$ such that $t_1(K \cup Y) = t_2(K \cup Y)$ and $t_1(X) \neq t_2(X)$ , where $r$ is a relation on $R$ . Clearly, the attributes in $X$ and $Y$ have different time-dependencies, i.e., they do not necessarily change simultaneously. In our design approach, they must belong to different relation schemes. Therefore, no non-trivial TD could be satisfied by $R$ . Since $R$ is in 4NF, it is also in TNF.

![](/api/attachments/JHMVKJ32/fulltext/images/4cca95726ab27152200455cc16a7cf8ad6c0a54d7cb033b9eb160a88dfa4a698.jpg)  
Fig. 6. A portion of a TEER diagram for a banking database.

## 5. Illustration of the TEERM

The model has been successfully applied to several simulated cases. This section illustrates the use of the extended model through an application to a banking example.

## 5.1. A case study: banking database

Consider a portion of a banking database as shown in Fig. 6, having five basic entities, and four relationships.

The two “is-a” relationships show the generalization from SAVINGS and CHECKING to ACCOUNT. The relationship “CLIENT has ACCOUNT” is static because the only event that affects this relationship is singular for the entity “ACCOUNT.” Lastly, “SAVINGS is paid INTEREST” is a temporal relationship because the status of a savings account may change over time, and the rate at which interest is paid would change accordingly. All of the attributes of the relevant entities are illustrated by the small circles, with the names appearing next to the circles. The only composite attribute is “address.” Three events, Transaction, Opening of Account and Change of Interest Rate, are shown. Transaction is recurrent for both CLIENT and ACCOUNT. Opening of Account is recurrent for CLIENT, but singular for ACCOUNT, assuming that an account is not reallocated to a different client after the owner of that account chooses to close it. Change of Interest Rate is recurrent for INTEREST. For the sake of clarity, we do not show the event-to relationship/attribute connections. The attributes and relationships affected by these events are given in Table 2.

Table 2  
List of attributes and relationships affected by different events

<table><tr><td>Event</td><td>Attribute</td><td>Relationship</td></tr><tr><td rowspan="3">Transaction</td><td>balance (SAVINGS)</td><td>SAVINGS is paid</td></tr><tr><td>balance (CHECKING)</td><td>INTEREST</td></tr><tr><td>last_check_no</td><td></td></tr><tr><td rowspan="2">Opening of account</td><td>account_no</td><td>CLIENT has</td></tr><tr><td>date_opened</td><td>ACCOUNT</td></tr><tr><td>Change of interest rate</td><td>int_rate</td><td></td></tr></table>

Table 3

<table><tr><td colspan="2">Relational schemes for the example banking database</td></tr><tr><td>client:</td><td>[ssn, street, city, zip]</td></tr><tr><td>client_name:</td><td>[ssn, TS, name]</td></tr><tr><td>account:</td><td>[account_no, date_opened]</td></tr><tr><td>account_balance:</td><td>[account_no, TS, balance]</td></tr><tr><td>savings:</td><td>[account_no, min_balance]</td></tr><tr><td>checking:</td><td>[account_no, last_check_no]</td></tr><tr><td>interest:</td><td>[account_status, TS, int_rate]</td></tr><tr><td>transaction:</td><td>[transaction_no, event_time, event_date, type, amount, from_account_no, to_account_no]</td></tr><tr><td>account_owner:</td><td>[ssn, account_no]</td></tr><tr><td>interest_schedule:</td><td>[account_no, account_status, TS]</td></tr></table>

## 5.2. Design of banking database

This section illustrates the design process using the above banking example. The following changes are made to the TEER diagram in Fig. 6:

(1) The attribute “balance,” being common to both “SAVINGS” and “CHECKING” is propagated to be an attribute of the entity “ACCOUNT.”

(2) The attribute “address” is identified as a quasi-static attribute, and is also decomposed into the constituent elementary attributes.

(3) "Transaction" is the only event with attributes such as "transaction\_no," "time," "date," "type," "amount," "from\_account\_ no” and “to\_account\_no.” Therefore, all events other than “Transaction” are eliminated. The view of this event is perceived as being a natural view to the user and, therefore, is retained. The only relevant event-to-entity connection is the one between “Transaction” and “ACCOUNT.” However, since “Transaction” already has “from\_account\_no” and “to\_account\_no” as attributes, no additional navigational link is necessary.

Application of the mapping rules outlined above results in the schemes shown in Table 3. The entities CLIENT, ACCOUNT, SAVINGS, CHECKING and INTEREST are represented by the relation schemes client, account, savings, checking and interest, respectively. The relation scheme client\_name represents the temporal attribute "name" of entity CLIENT. Similarly, the relation scheme account\_balance represents the temporal attribute "balance" of the entity ACCOUNT. The temporal attribute "int\_rate" was simply appended to the relation scheme interest since it had only the key attribute "account\_status." The relationships "CLIENT has ACCOUNT" and "SAVINGS is paid INTEREST" are represented by the relation schemes account\_owner and interest\_schedule respectively. The scheme transaction represents the only relevant event Transaction.

## Integrity constraints

Existence constraint: No relation instance on the above schemes can have null values for key attributes and TS. For example, a relation on the scheme account\_balance cannot have null values for account\_no and TS.

Referential constraint: The following referential constraints should be enforced:

(1) client to client\_name (foreign key: ssn)

(2) account to account\_balance (foreign key: account\_no)

(3) account to savings (foreign key: account\_no)

(4) account to checking (foreign key: account no)

(5) account to account\_owner (foreign key: account\_no)

(6) client to account owner (foreign key: ssn)

(7) account to interest\_schedule (foreign key: account\_no)

(8) interest to interest\_schedule (foreign key: account\_status)

Others: There is some redundancy in the design, because the relation on the scheme transaction stores information that is also in the relation on the scheme account\_balance. The following additional integrity constraints are needed. For every tuple $x$ in the relation on the scheme transaction, there must be two tuples, $y_1$ and $y_2$ in the relation on the scheme account\_balance such that $x(\text{amount}) = |y_1(\text{balance}) - y_2(\text{balance})|$ and one and only one of the following two holds

(1) $x(\text{event\_time}) \in y_1(TS)$ and

$$
x (\text { event\_time }) \in c l (y _ {2} (T S))
$$

(2) $x(\text{event\_time}) \in y_2(TS)$ and

$$
x (\text { event\_time }) \in x \{c l \} (y _ {1} (T S)).
$$

Here, $|a|$ denotes the absolute value of a real number $a$ . The closure (denoted as “cl”) of a set $b$ is defined as: $cl(b) = b \cup b'$ , where $b'$ is the set of all of limit points of $b$ . For example [1,9] represents the closure of the interval [1,9).

## 6. Conclusion

Although considerable amount of research has been carried out in the area of temporal databases, the topic of temporal database design has not received much attention in the literature. The design process for static databases does not work for temporal databases because of lack of a temporal conceptual model and a step-by-step procedure for converting that model into a logical database scheme. This work makes two contribution. First, it proposes a conceptual model, called the Temporal Event-Entity-Relationship Model (TEERM). The TEERM is based on the E-R model, and uses events as additional constructs. Although the representation of events can introduce some redundancy into the model, it allows one to capture the dynamic behaviour of entities, relationships and their attributes. Second, this research also formally describes how the TEERM can be used for the logical design of temporal relational databases, and demonstrates the conceptual and logical design process with the help of an example.

Batini et al. [2] suggest four desirable properties of conceptual models: (i) expressiveness, (ii) simplicity, (iii) formality and (iv) minimality. We believe that our model possesses all of these properties. The TEERM is at least as expressive as all the other conceptual data models found in the literature. It retains the expressive power of the extended E-R model, and adds to it by capturing the dynamic nature of entities and relationships using events as an additional construct. It allows us to specify dynamic constraints and provide an alternate view of data. Batini et al. [2] also suggest two desirable properties for graphical representation schemes: (i) graphic completeness and (ii) ease of reading. The TEERM graphical representation is complete as well as easy to read.

The issue of completeness of a conceptual data model is mainly an empirical proposition. Consider, for example, the E-R model. A long history of use and refinement (for example, the introduction of data abstractions such as aggregation, generalization and specialization) of the model has shown that the extended E-R model $[28,2]$ can reasonably model most real world situations as snapshots. The temporal extension of the E-R model proposed here is believed to have the potential to be a useful conceptual model.

Various types of future research are possible. One direction is the development of a query language such as GORDAS for this model. Another possibility is to describe formally how integrity constraints can be generated using the TEERM. The new construct event would be useful in automated verification of consistency and completeness of the conceptual design.

## References

[1] Ahn, I., Towards an Implementation of Database Management Systems with Temporal Support, Proceedings of the Second International Conference on Data Engineering, pp. 374–381, February 1986.

[2] Batini, C., S. Ceri, and S.B. Navathe, Conceptual Database Design, Benjamin/Cummings, 1992.

[3] Ben-Zvi, J., The Time Relational Model, Ph.D. Diss., UCLA, 1982.

[4] Chen, P.P.-S., The Entity-Relationship Model - Toward a Unified View of Data, ACM Transactions on Database Systems, 1(1), pp. 9-36, March 1976.

[5] Clifford, J. and A.U. Tansel, On an Algebra for Historical Relational Databases: Two Views, ACM SIGMOD Record, 14(4), pp. 247–265, December 1985.

[6] Date, C.J., Relational Database: Selected Writings, Addison-Wesley, 1986.

[7] Dey, D., Temporal Relations and Temporal Normal Form, Working paper, Louisiana State University, 1994.

[8] Dey, D., T.M. Barron, and A.N. Saharia, Logical Design of Temporal Databases: A Decision Theoretic Approach, Working paper, University of Rochester, 1994.

[9] Dey, D., T.M. Barron, and V.C. Storey, Events in Representation of Temporal Data, Proceedings of the Second Annual Workshop on Information Technologies and Systems, pp. 255–261, Dallas, Texas, December 1992.

[10] Dubois, E., J. Hagelstein, E. Lahou, F. Ponsaert, A. Rifaut, and F. Williams, The ERAE Model: A Case Study, in Information Systems Design Methodologies: Improving the Practice, T.W. Olle, H.G. Sol and A.A. Verrijn-Stuart (eds.), Elsevier Science Publishers B.V., North Holland, pp. 87–105, 1986.

[11] Elmasri, R. and G.T.J. Wuu, A Temporal Model and Query Language for ER Databases, Proceedings of the Sixth International Conference on Data Engineering, pp. 76–83, February 1990.

[12] Elmasri, R., I. El-Assal, and V. Kouramajian, Semantics of Temporal Data in an Extended ER Model, Entity-Relationship Approach: The Core of Conceptual Modelling, H. Kangassalo (ed.), Elsevier Science Publishers B.V., North Holland, pp. 239–254, 1991.

[13] Elmasri, R., G.T.J. Wuu, and V. Kouramajian, A Temporal Model and Query Language for EER Databases, in Temporal Databases, A. Tansel et al. (ed.), Benjamin/Cummings, 1993.

[14] Ferg, S., Modelling the Time Dimension in an Entity-Relationship Diagram, Proceedings 4th International Conference on Entity-Relationship Approach, Chicago, pp. 280–286, October 1985.

[15] Gadia, S.K., A Homogeneous Relational Model and Query Languages, ACM Transactions on Database Systems, 13(4), pp. 418–448, December 1988.

[16] Gehani, N.H., H.V. Jagadish, and O. Shmueli, Event Specification in an Active Object-Oriented Database, ACM Sigmod Record, 21(2), pp. 81–90, 1992.

[17] Goldstein, R.C., Database: Technology and Management, John Wiley, 1985.

[18] Klopprogge, M.R., Term: An Approach to Include the Time Dimension in the Entity-Relationship Model, Entity-Relationship Approach to Information Modelling and Analysis, P.P. Chen (ed.), pp. 477–512, 1981.

[19] Klopprogge, M.R. and P.C. Lockemann, Modelling Information Preserving Databases: Consequences of the Concept of Time, Proceedings of the Ninth International

Conference on Very Large Data Bases, pp. 319–416, November 1983.

[20] Kouramajian, V. and R. Elmasri, Mapping of 2-D Temporal Extended ER Models into Temporal FNF and NFNF Relational Models, Proceedings of the Tenth International Conference on Entity-Relationship Approach, pp. 671–689, San Mateo, CA, October 23–25, 1991.

[21] Navathe, S.B. and R. Ahmed, A Temporal Relational Model and a Query Language, Information Sciences, 49, pp. 147–175, 1989.

[22] Schiel, U., The Time Dimension in Information Systems, Information Systems: Theoretical and Formal Aspects, A. Sernadas, J. Bubenko and A. Olivé (eds.), Elsevier Science Publishers B.V., North-Holland, 1985.

[23] Segev, A. and A. Shoshani, The Representation of a Temporal Data Model in the Relational Environment, Proceedings of the Fourth International Working Conference on Statistical and Scientific Database Management (SSDBM), M. Rafanelli, J.C. Klensin and P. Svensson (eds.), Rome, Italy, June 1988.

[24] Snodgrass, R., The Temporal Query Language TQuel, ACM Transactions on Database Systems, 12(2), pp. 247-298, June 1987.

[25] Storey, V.C., View Creation: An Expert System for Database Design, ICIT Press, 1988.

[26] Storey, V.C., Relational Database Design Based on the Entity-Relationship Model, Data and Knowledge Engineering, 7, pp. 47–83, 1991.

[27] Tauzovich, B., Towards Temporal Extensions to the Entity-Relationship Model. Proceedings of the Tenth International Conference on Entity-Relationship Approach, T.J. Teorey (ed.), San Mateo, CA, pp. 163–179, October 23–25, 1991.

[28] Teorey, T.J., Database Modelling and Design: The Entity-Relationship Approach, Morgan Kaufmann, 1990.

[29] Theodoulidis, C., P. Loucopoulos, and B. Wangler, A Conceptual Modelling Formalism for Temporal Database Applications, Information Systems, 16(4), pp. 401–416, 1991.

Debabrata Dey is Assistant Professor of Information Systems and Decision Sciences at the College of Business Administration at Louisiana State University. He received his Ph.D. degree in Computers and Information Systems from the William E. Simon Graduate School of Business Administration at the University of Rochester. His current research interests are in temporal and probabilistic data models and performance evaluation of database systems. Dr. Dey has published articles in Information Systems Research and other conference proceedings.

Terence M. Barron is Associate Professor of Information Systems and Operations Management at the College of Business Administration, University of Toledo. Before this, he was at the William E. Simon Graduate School of Business Administration, University of Rochester. His research interests include economics of information, economics of information system management, and the impacts of information technology on organizations and markets. His research has appeared in Information Systems Research, Decision Support Systems, Journal of Organizational Computing, and other journals and conference proceedings.

Veda C. Storey is Assistant Professor of Computers and Information Systems at the William E. Simon Graduate School of Business Administration, University of Rochester. She has research interests database management systems and artificial intelligence. Her research has been published in ACM Transactions on Database Systems, Information Systems Research, Management Information Systems Quarterly, Data and Knowledge Engineering, and the Very Large Data Base Journal. She is the author of View Creation: An Expert System for Database Design, a book based on her doctoral dissertation, and published by ICIT (International Centre for Information Technology) Press in 1988. Dr. Storey received her doctorate in Management Information Systems from the University of British Columbia, Canada, in 1986.
