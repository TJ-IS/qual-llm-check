---
otero_id: 19204
otero_key: "YBECVBCZ"
title: "Intelligent database design using the unifying semantic model"
authors: "Sudha Ram"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00015-o"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intelligent database design using the unifying semantic model

Sudha Ram $^{1}$

Department of Management Information Systems, Eller School of Management, University of Arizona, Tucson, AZ 85721, USA

## Abstract

Research and development in the field of database systems has culminated in its widespread use. As usage has grown, the desire to link separate databases has resulted in substantial effort being directed towards the design of distributed database systems. A major research issue in designing such systems is the definition of a formal model that can be used to capture the semantics of the individual databases. This paper presents a semantic model called the Unifying Semantic Model (USM) and a software tool using it. The USM can be used for modeling the complex interrelationships and semantics found in a manufacturing environment. It is based on enhancements to existing semantic models. It can serve as a formal specification and documentation tool for databases. It can provide a means of specifying the Universe of Discourse for any interchange of information.

Keywords: Semantic modeling; Intelligent database design; Conceptual modeling; User interface; Graphical database design; Schema integration

## 1. Introduction

The goal of this research is to develop an intelligent database modeling toolkit. As part of this overall goal we define a semantic model that will allow users and designers to capture the meaning of a database. This model (called the Unifying Semantic Model – USM) serves as a formal specification of a mechanism for describing a Universe of Discourse. Thus, it provides a means of precise documentation and communication among users. It also provides the basis for developing a high-level user interface to one or more databases. This can be constructed as a front end in a heterogeneous database environment, thereby facilitating the process of identifying and retrieving relevant information from underlying databases.

The USM draws upon constructs found in several other semantic models. In particular, the models that have influenced the development of this model are NIAM [10], SDM [5], IDEF1X [8], and OSAM\* [23]. We believe that the USM synthesizes and extends constructs in a coherent manner.

## 2. Semantic models and tools for conceptual modeling

A semantic model essentially defines objects, relationships among objects, and, properties of objects. A large number of semantic models have been developed and described in literature; for example, [3,19,2,1,9,12]. Detailed surveys of several semantic models have been reported by others [7,11]. Semantic modeling provides a number of mechanisms for viewing and accessing the schema at different levels of abstractions. The USM is based on the traditionally used abstractions of classification, generalization, aggregation and association [21]. In particular, it proposes concepts to represent constraints on relationships between subclasses. It also distinguishes between the concepts of Composites and Groups/Aggregates.

A large number of tools have been developed for database modeling. These support various phases of database design ranging from natural language requirements collection to physical design and implementation; see for example – [22,15,6,4,20,14]. For a comprehensive survey of such tools the reader is referred to [14,18]. Of these tool development efforts, many provide support for conceptual modeling using a variation of the Entity-relationship model with translation to a relational schema. The quality of design output is dependent on the user/designers using the tool. Most of the tools do not provide any form of intelligent support. We contend that they should provide feedback to the designers thereby providing a complete and consistent schema with minimal conflicts among designers.

In this research we have attempted to address the problem of incorporating intelligence into a semantic modeling tool. In order to do so we must first develop a comprehensive semantic model. The rest of the paper describes the semantic model (USM) and the intelligent tool.

## 3. Fundamental concepts in the USM

The USM defines constructs that will allow the specification of a Universe of Discourse. It supports a relativist view of the world in that it attempts to support alternative ways of looking at the same information. The USM provides a conceptual basis for capturing the semantics and inter-relationships among objects in the real world. Objects are grouped together into object classes based on some common semantic characteristics. Objects classes are referred to by a name and are classified into several different types. There are two main types of object classes defined in the paper: Domain and Entity. Entity Classes may be considered to be Simple Classes, Interactions, Groupings or Composites. Several types of relationships are defined in the USM: Properties, Interactions, Set/Subset, Grouping and Composite. In order to illustrate the constructs of the USM the paper uses many examples adapted from the schema of Hammer and McLeod [5].

![](/api/attachments/YBECVBCZ/fulltext/images/4e0925d88ed3a0328e6b35ecfc2818afea7e9315dffcb510202dd81a5af974b6.jpg)  
Fig. 1. USM class symbols.

![](/api/attachments/YBECVBCZ/fulltext/images/21eb95e59e6074df0ffc03b4e586487a58b558c2074a8c78a40cde2a41a75623.jpg)  
Fig. 2. USM entity class symbols.

## 3.1. Elementary classes

Entity classes

All real world objects are referred to by the term ENTITY (see Fig. 1). A collection of entities for which common characteristics are to be modeled is called an ENTITY CLASS, which can also be termed an ENTITY TYPE or ENTITY SET. For purposes of this paper, we use the term ENTITY CLASS. Every one must have a unique name. An entity that belongs to an entity class can also be called a MEMBER or OCCURRENCE. Here, we will use the term MEMBER. Some ENTITY CLASSES contain others as their MEMBERS. Characteristics or properties of members of ENTITY CLASSES are called ATTRIBUTES. Associations between or among members of ENTITY CLASSES are called RELATIONSHIPS.

For example, “Queen Elizabeth II” is an entity and “SHIPS” is an entity class. “Queen Elizabeth II” is a member (ENTITY) of the entity class called “SHIPS”. “Hull-Number”, “Name”, and “Number of Engines”, are some possible attributes of SHIPS.

Entity classes may be one of two types: STRONG or WEAK (see Fig. 2):

1. STRONG ENTITY CLASSES: Members of a strong entity class can exist on their own. They do not depend on members of other classes for their existence. For example, SHIPS is an entity class. Each individual ship is a member of the entity class SHIPS. A ship can exist without a Navy or a crew.

2. WEAK ENTITY CLASSES: Members of a weak entity class depend on members of other class(es) for their existence. The latter class(es) can themselves be strong or weak. However, the dependency chain has to start in a STRONG ENTITY CLASS. For example, COURSE may be a strong entity class with SECTION as a weak entity class, the members of which depend on members of a COURSE, i.e., it is not possible to have sections of a non-existent course. Another example of a weak entity class is INSPECTIONS. These are performed on SHIPS. Members of INSPECTIONS depend on there being at least one member of SHIPS for their existence. Note: Since the members of a subclass of a strong entity class are the same as some or all members of the superclass, the subclass of a STRONG ENTITY CLASS is necessarily a STRONG ENTITY CLASS.

## Domain classes

A domain, as normally defined in mathematics, is a set of values of the same type. This is the pool of values from which attributes draw their values. A domain is a symbolic object with a datatype. If two attributes draw their values from the same domain, comparisons (etc.) between the attributes can be made. Conversely, if two attributes do not draw their values from overlapping domains, comparisons between them do not make sense. A domain can have one of several datatypes: Integer, Count, Measure, Currency, Real, Scaled, Boolean, Enumerated, Name,

![](/api/attachments/YBECVBCZ/fulltext/images/7e1a450f52af752d1dba2ee694c9a42cdf2de638844d77ddac495f60010a331d.jpg)  
Fig. 3. USM relationship symbols.

![](/api/attachments/YBECVBCZ/fulltext/images/6ce139107d2a079640a080d28ac77f9d183cf3f3fa690e6c9b808bb9516bdb82.jpg)  
Fig. 4. USM property relationships.

Text, Datetime, Bit-String, and Byte-String. These are defined below:

1. Integer: a numeric quantity which is known to have an exact integral value.

2. Count: a natural number.

3. Measure: a unit of measurement such as kilograms, pounds, inches.

4. Currency: monetary data (dollars, pounds, etc.) This is a special scaled datatype exact to two decimal places and having restricted arithmetic.

5. Real: scientific numbers, i.e. numbers that are neither known nor represented accurately, but approximated by a number of significant digits that represent the known or useful limits on the accuracy of a value for calculation purposes.

6. Scaled: numbers that are not integral but known to be accurate, or even exact to a given number of decimal places.

7. Boolean: one of two (or three) values: Yes/No/Undefined, or True/False.

8. Enumerated: a list of named values that may be represented by alphanumeric, numeric, or alphabetic characters or integer values.

9. Name: a character string whose purpose is to identify some object. It can be restricted by a maximum size, can be alphanumeric, alphabetic, or numeric. It can be used for comparison, sorting and other types of manipulations.

10. Text: a character string that is of variable length, with no maximum size constraint. It cannot be used for comparison, or sorting or other manipulations except for reading, storing, and printing.

11. Datetime: date and time of the day. It can have parametrizations i.e. accurate to the second, millisecond, etc.

12. Bit-string or Byte-string: This is similar to Text-string, except that the data is in binary form and understood only by the application. Therefore the functions that can be applied do not include any kind of string operations, except possibly append. In particular, it cannot be printed, and if it is unloaded from one machine and moved to another, it is not meaningful to perform character set translation on it.

![](/api/attachments/YBECVBCZ/fulltext/images/7084e155ded3c94ea6ba45ef88987cc63347348a2c170bbfdefb6796c798a3fc.jpg)  
Fig. 5. USM interaction relationships.

## 3.2. Relationships

## Property relationships

A PROPERTY RELATIONSHIP relates an entity class to a domain class (see Figs. 3 and 4). A property creates an attribute. A property cannot refer to classes of other entities. PROPERTY RELATIONSHIPS are always binary. They have names, but they do not generate new classes. They are always seen from the point of view of the entity class and not from the point of view of the domain. In other words, only an entity can have an attribute.

## Interaction relationships

An interaction relationship refers members of one ENTITY CLASS to members of one or more other ENTITY CLASSES (See Fig. 5). These may also be referred to as ASSOCIATION RELATIONSHIPS. They have names and may generate new classes. An INTERACTION relationship can be seen from the point of view of any of the entity classes taking part in the relationship. An Interaction relationship creates attributes relating members of each of the participating classes to members of each of the other participating classes. Attributes may also be created to describe an interaction relationship; these form a new entity class – the INTERACTION CLASS. It is related to the interaction relationship between the original entities taking part in the interaction relationship. All interactions classes are WEAK.

For example, SHIPS and OFFICERS are related to each other using a binary interaction relationship. Since the interaction can be described further by properties, such as Date-of-assignment, and Duration-of-assignment, a new entity class called ASSIGNMENTS is created with these two. This class is related to the interaction relationship between OFFICERS and SHIPS. It does not form a ternary relationship with SHIPS and OFFICERS. ASSIGNMENTS arises from the binary relationship between SHIPS and OFFICERS rather than existing on its own. However, contrast this with the following situation. Consider the example of STUDENTS, PROJECTS and ADVISORS. In this example, we may model a ternary relationship among the three entity classes. This interaction may be further described by attributes. These attributes will form a new entity class which is related to the interaction relationship. In some cases, ternary or higher order relationships can be modeled as a set of binary relationships depending on the user's preference.

CHARACTERISTICS OF INTERACTION RELATIONSHIPS

1. PARTICIPATION CARDINALITY: Depending on the number of entity classes participating in the interaction relationship, it may be binary or n-ary.

(a) Binary Interaction Relationship: A binary interaction relationship is one in which only two entity classes participate.

(b) N-ary Interaction relationship: An n-ary interaction relationship is one in which n entity classes participate.

2. INVERSE: In a binary interaction, exactly two attributes are created and each attribute is the INVERSE of the corresponding attribute created in the other entity class. This allows an interaction relationship to be viewed from the point of view of any of the entity classes taking part in the relationship. For example, consider a relationship between SHIPS and OFFICERS. From the point of view of OFFICERS: an officer signs-on a ship. From the point of view of SHIPS: a ship has an officer. The concept of inverse applies only to binary interactions.

3. RECURSIVE RELATIONSHIPS: A recursive relationship relates a member of an entity class to one or more members of the same entity class. For example, an officer may be manager of one or more other officers. Similarly an officer may be a subordinate to one or more other officers.

4. NAMING OF INTERACTION CLASSES: The class name of a binary interaction relationship is optional when the interaction is totally equivalent to the pair of attributes; i.e. when the relationship has no properties of its own. Otherwise the interaction class must have a unique name.

5. WEAKNESS: A WEAKNESS RELATIONSHIP is one in which members of an entity class depend on members of other entity class(es) for their existence; e.g., members of a weak entity class depend on members of other class(es) for their existence. Some relationships result in classes that are inherently weak. In some cases, classes are defined as weak classes by the user and weakness is an annotation on the interaction relationship that points to the stronger class on which the weak class depends.

## 3.3. Attributes

An attribute is a characteristic of an entity; i.e., it is the view possessed by members of an entity class of a relationship to members of some other domain or entity class, or possibly to specific other members of the same class. Attributes are created by Property, Interaction, Composite, and Grouping relationships. The VALUE of an attribute for a given entity is the corresponding entity or domain value in the class to which the attribute refers. It is possible that, for a given entity and attribute there is no corresponding value, in which case the attribute is said to be NULL VALUED for that entity. It is also possible that for some entities in a class a given attribute may have more than one value, in which case the attribute is said to be MULTIVALUED. When there is at most one value of the attribute it is said to be SINGLE-VALUED. As stated earlier, an interaction relationship creates attributes in the participating entity classes. Further, in a binary interaction exactly two attributes are created, one in each participating entity class. Each attribute is an INVERSE of the other attribute.

Attributes have the following characteristics:

CHARACTERISTICS OF ATTRIBUTES

1. MANDATORY/OPTIONAL: A mandatory attribute is one that is required to have a non-null value. For example, a ship which is a member of the entity class SHIPS may have a property relationship with an attribute called hull-number. A hull-number may be a mandatory attribute for a ship, i.e. each ship is required to have a non-null value for its hull-number. However a ship may not be required to have a name. Thus ship name is an optional attribute.

2. CHANGEABLE/NOT CHANGEABLE: If the value of an attribute can be altered then it is a CHANGEABLE attribute, otherwise, it is UNCHANGEABLE. For example, date-of-birth is an unchangeable attribute.

3. CARDINALITY: As stated earlier, an attribute can be single-valued or multivalued. The values can be further constrained to be unique or non-unique. An attribute can thus be single-valued unique (e.g., aircraft-number), multivalued unique (e.g., phone-numbers) single-valued non-unique (e.g., aircraft-type), or, multivalued non-unique (e.g., cargo-types). If an attribute is multivalued, it can be constrained by a maximum and/or minimum number of values. This is not the same as specifying the particular value(s) that can be assigned to an attribute.

4. ORDERING/DUPLICATES: If an attribute is multivalued, it may be constrained by allowing or not allowing ordering and duplication. An attribute may be a BAG (unordered collection, duplicates allowed), SET (unordered collection, no duplicates), or LIST (ordered collection, with or without duplicates).

5. DERIVED ATTRIBUTES: These are attributes of an entity class whose values are derived from other attributes of the same or other entity classes i.e. value of $A_{2}$ is derived from the value of one or more attributes represented by $A_{1}\ldots A_{n}$ ; Note that the latter attributes may be defined for other entity classes. The different ways of deriving an attribute value are:

(a) Mathematical derivation (such as total, sum, difference, product, power, division or any combination of these), (e.g., “age” from “date-of-birth” and “today’s-date”)

(b) Position based on ordering, (e.g., “most-recently-commissioned-officer” from “commission-date”),

(c) Operator based (equality, greater than, less than, maximum, minimum) (e.g., “salary-range” from “grade” and “level-in-grade”).

6. COMPOSED ATTRIBUTES: An attribute of an entity class can be related to another attribute using the matching concept. MATCHING provides a way of viewing n-ary relationships. Consider the entity class ASSIGNMENTS with three attributes – “officer” and “ship” and “sign-on-date”. This class indicates the officer(s) signed-on to a particular ship on a specific date. We could model a composed attribute called “captain” for the entity class SHIPS to indicate that the captain of a specific ship “QE2”, is equal to the value of the attribute “officer” defined for a specific member in ASSIGNMENTS whose ship is “QE2”. Formally, the value of an attribute $A_{1}$ for the member $M_{1}$ of entity class $C_{1}$ is defined as follows: A member $M_{2}$ of some specified class $C_{2}$ is found that has $M_{1}$ as its value of one of its attributes $A_{2}$ . The value of member attribute $A_{3}$ for $M_{2}$ is used as the value of $A_{1}$ for $M_{1}$ . $A_{1}$ is referred to as a composed attribute. If $A_{1}$ is a multivalued attribute, then it is permissible for each member of $C_{1}$ to match to several members of $C_{2}$ ; in this case the collection of $A_{3}$ values is the value of attribute $A_{1}$ .

7. IDENTIFIERS (often termed “keys”): are one or more attributes (or combinations of attributes) that may be used to identify individual members of an entity class. Any (single-valued or multivalued) unique attribute is qualified to be an identifier or a part of one. A combination of attributes that have a joint-uniqueness constraint is qualified to be an identifier. If the same attribute is used in more than one combination, the identifiers are called OVERLAPPING, otherwise they are NONOVERLAPPING. In some cases, identifiers of a weak entity class may consist of one or more attribute(s) for the weak entity class along with one or more attributes from the entity class(es) on which it depends. Note: Identifiers are useful for choosing the primary key for implementation purposes. They may also be used as indexing fields for more rapid searches for some queries.

![](/api/attachments/YBECVBCZ/fulltext/images/ca9c6e13832add8089547ec62c599f1039e7985448d154a877a3a01297dd05db.jpg)  
Fig. 6. USM attribute constraints.

![](/api/attachments/YBECVBCZ/fulltext/images/b0c92c7c80c83671b322bdf3563a770b75e11f7ec27dd4cdf37c7c48504b97a3.jpg)  
Fig. 7. USM subtype relationships.

8. INTER-ATTRIBUTE CONSTRAINTS (see Fig. 6): These constraints do not apply to the particular value of the attributes. They are constraints that determine whether the attribute values exist. Consider attributes $A_{1}$ or $A_{2}$ for an entity class.

(a) Implication: If $A_{2}$ exists then $A_{1}$ has to exist.

(b) Equivalence: If $A_{2}$ exists then $A_{1}$ has to exist and vice versa. This means that either both $A_{2}$ and $A_{1}$ exist, or neither does.

(c) Exclusion: If $A_{2}$ exists then $A_{1}$ must not. This means if $A_{1}$ exists then $A_{2}$ must not exist. It is possible that neither exists.

(d) Inclusion: At least one of $A_{1}$ and $A_{2}$ must exist.

(e) Alternation: Exactly one of $A_{1}$ and $A_{2}$ must exist.

(f) Joint Uniqueness: The pair of values $(A_{1}, A_{2})$ occurs at most once over all entities in the class. Note: (a), (b), and (c) are pairwise constraints, whereas (d), (e) and (f) may involve more than two attributes and have no pairwise equivalents in that case.

## 3.4. Class relationships

An entity class may be related to one or more other entity classes by means of a GENERALIZATION/SPECIALIZATION RELATIONSHIP. A generalization/specialization relationship between two entity classes defines a supertype/subtype (See Fig. 7). Generalization/specializations relationships do not have names. They do not generate any new classes. Entity classes related by means of this relationship have members of one or more other classes as their members. An entity class may have one or more subclasses. Subclasses in turn may have their own subclasses. These relationships can be defined on STRONG as well as WEAK entity classes. An entity class may be a subclass of two or more different entity classes thus forming a GENERALIZATION LATTICE.

An important concept associated with subclasses is that of attribute INHERITANCE. Since an entity in the subclass represents the same real world entity from the superclass, it should possess values for its specific attributes as well as values of its attributes as members of the superclass. Therefore it is said that the entity which is a member of a subclass inherits the attributes of all its superclasses.

## 3.5. Subclass definition

Subclasses may be defined in one of three ways:

1. ATTRIBUTE-DEFINED: The subclass has some attribute defined for the superclass so that its value can be used to determine the members of the subclass. These subclasses inherit all the attributes defined for their superclass.

2. ROSTER-DEFINED: The subclass has membership determined only by examining a roster; i.e., a list of members. These subclasses inherit all the attributes of their superclass.

3. SET-OPERATION-DEFINED: A subclass may be defined as either the difference or the set-intersection of two or more entity classes. Members of an intersection subclass of two or more entity classes will be members of each of the participating classes. The resulting subclass will inherit all attributes that are common to the two classes. Members of the difference subclass of two entity classes, will consist of those members of the first entity class which are not members of the second entity class. In this case attributes of only the first entity class will inherit by the subclass. Note: The union of two or more entity classes forms an entity class that is a superclass of the entity classes rather than a subclass.

![](/api/attachments/YBECVBCZ/fulltext/images/0a2fffc31d9c0c6b551c140654106efbd1b435befafea7d71c3fb535f792cd24.jpg)  
Fig. 8. USM constraint representation.

![](/api/attachments/YBECVBCZ/fulltext/images/1a7846cbe82d973f3f043942016aa297efbb58fbd96eb6601a58b713d48a1cd5.jpg)  
Fig. 9. USM class constraints.

## Relationships among subclasses

Three types of relationships can exist among subclasses of a common superclass (see Figs. 8 and 9).

1. EQUAL SUBCLASSES: If an entity class has 2 subclasses that have exactly the same members, then the subclasses are EQUAL. This is the case where the two subclass names synonyms of the same entity class.

2. MUTUALLY EXCLUSIVE: Subclasses of an entity class are mutually exclusive if members of subclass 1 cannot be members of subclass 2.

3. OVERLAPPING: Subclasses are overlapping if there may be members that are common to the subclasses.

## Collections of subclasses

Two kinds of relationships can exist among collections of subclasses of a common superclass:

1. TOTALLY EXHAUSTIVE: A collection of subclasses of an entity class is totally exhaustive if every member of the entity class must be a member of at least one of the subclasses in the collection. That is, the entity class is the UNION of all the subclasses in the collection.

2. PARTITIONS: A partition is a collection of subclasses of an entity class, such that the collection is totally exhaustive of the entity class and every pair of the subclasses is mutually exclusive.

## 3.6. Grouping relationships

## Composites

A COMPOSITE relationship defines a new class that has other classes as its members (See Fig. 10). It must have a name. All such classes are strong. Specifically, a member of a COMPOSITE class is the set of members of some other class taken as a whole. The classes that are members may be subclasses of a common superclass, in which case they

![](/api/attachments/YBECVBCZ/fulltext/images/0c6896bffdd34ee69d4bd06d17aea70d4fd9ceac71e89d4198aa282c934d85fa.jpg)  
Fig. 10. USM composite relationships.

are said to be homogeneous, or they may not, in which case they are said to be heterogeneous. COMPOSITE classes are needed to define “class attributes” or properties that describe a whole class (or subsets of a class) rather than each individual entity in an entity class. For example, attributes such as “total-number-of ships”, or “fastest-ship” can be defined as an attribute of a COMPOSITE class called “SHIP-TYPES”. When a COMPOSITE class is defined, it always has at least one attribute called Contents defined for it, which refers to the members of each of its classes. Obviously, Contents is a multivalued attribute; It may or may not be unique. If it is, an entity cannot belong to more than one member of the composite class.

![](/api/attachments/YBECVBCZ/fulltext/images/ea78d3df2932f066b90889883589dcd5934ae5416aeaf3a482807a757059bf98.jpg)  
Fig. 11. USM grouping and aggregate relationships.

![](/api/attachments/YBECVBCZ/fulltext/images/e2e412a870a6cd3e560f4667068801fae06f9f09e261808eaefff62037e129a1.jpg)  
Fig. 12. USM metamodel: constructs in the USM.

Note: COMPOSITE relationships are not generalizations or specializations of other entity classes. COMPOSITE classes can be defined on strong as well as weak entity classes. They can also be generalized or specialized.

There are two kinds of COMPOSITES: Selected and Enumerated.

1. SELECTED: Given an entity class C with some attributes $A_{1},\ldots,A_{n}$ (among others), we can define an attribute-defined composite class based on C as having as its members those subclasses of the class C in which all members have identical values for the attributes $A_{1},\ldots,A_{n}$ . That is, we can envision a set of attribute-defined subclasses of C defined by the tuple of values of $(A_{1},\ldots,A_{n})$ and the composite class has those subclasses as its members. The attributes $A_{1},\ldots,A_{n}$ are called the Selection attributes of the COMPOSITE relationship and they are also the attributes of the COM-

POSITE class. A collection of values of the Selection attributes uniquely identifies a member of the COMPOSITE class, i.e. one of the subclasses of C. Attribute-defined COMPOSITE CLASSES are necessarily homogeneous. For example, the entity class called SHIP-TYPES, a grouping of the class SHIPS, may be based on common value of an attribute called Type-of-ship. Each member of the class SHIP-TYPES is itself a class (say $C_{n}$ ). Thus members of SHIP-TYPES are the classes $C_{1}$ , $C_{2}$ , etc. $C_{1}$ in turn consists of a number of members, each of which is a member of the class SHIPS. The COMPOSITE class SHIP-TYPES really consists of a number of classes each of which is a subclass of the class SHIPS. If Type-of-ship is a single-valued attribute, the classes which are members of the class SHIP-TYPES are mutually exclusive. Consider a COMPOSITE class called CARGOTYPE-GROUPS, defined on the underlying class SHIPS using the attribute Cargo-type (which is a multivalued attribute). Then, a ship may belong to more than one class in the class CARGO-TYPE-GROUPS.

![](/api/attachments/YBECVBCZ/fulltext/images/20ec3d60bcfab9f7ae6cafbfab4f3adf5222cf482046ae2a20e3ae29dbb4dea7.jpg)  
Fig. 13. USM metamodel: relationships in the USM.

![](/api/attachments/YBECVBCZ/fulltext/images/7d4f3f01716de528af10912bd9d710ba5bf8f7d24ab6f08b7f1e3e5fd813f4c2.jpg)  
Fig. 14. Architecture of unibase-modeler.

2. ENUMERATED: An enumerated composite class is defined by listing its members, that is, by naming as its members other classes which appear in the model. Members of an enumerated COMPOSITE class can be heterogeneous. Consider a composite entity class called SHIP-STATUS-CLASSES defined on the entity class called SHIPS. It may consist of four classes as its members: SHIPS-IN-PRODUCTION, SHIPS-IN-SERVICE, SHIPS-IN-REFIT, and SHIPS-TO-BE-RETIRED. Each class that is a member of the composite class may have a number of attributes defined for it. An enumerated composite class that has exactly one member, i.e., one entity class, is a special composite class. All attributes of this composite class are really “class attributes” of the member entity class; that is, attributes are possessed by the entity class as a whole rather than by its members individually.

![](/api/attachments/YBECVBCZ/fulltext/images/ab00b1c37e588c8f79647b49b7105a609d6459cc9c948e4dcc0c55b759a207be.jpg)  
Fig. 15. Binary relationship definition (entity selection).

## Groupings

Members of a GROUPING class are collections of members from some other class. A GROUPING class may be heterogeneous or homogeneous (see Fig. 11). In a heterogeneous grouping class, (also known as an AGGREGATE class), each member entity is composed of one member from each of several different “component” classes. Each member is known as an AGGREGATE. It is a unique collection of its components; a change in any one of them refers to a different entity. Conversely, a component of an AGGREGATE does not exist by itself. In a homogeneous grouping class (also known as a GROUPING class), each member entity is a collection of members from a single other entity class called the “component” class. Each member of a grouping class is called a GROUP, which may be a set or list (with or without duplication). By definition a grouping is unique; i.e., semantically a member of a grouping or aggregate class is the collection of members of the component class(s) and therefore the collection uniquely identifies the group or aggregate entity.

![](/api/attachments/YBECVBCZ/fulltext/images/e5159f042ed679a137bd9d470402fb0d71c52ec9f300be201f8ea665d1711342.jpg)  
Fig. 16. Interaction relationship definition (relationship selection).

GROUPINGS and AGGREGATES are not generalizations or specializations of entity classes. They are not COMPOSITES of one or more entity classes. For example consider the relationship between the entity classes JOURNEY and ITINERARY. An itinerary is a collection of journeys. In this case the ordering of the journeys is important. Duplication is allowed in this example, although it is not a requirement of grouping entity classes. Subclasses, superclasses and/or composite classes may be defined on grouping classes. All grouping classes are weak. When a GROUPING class is defined, it always has at least one attribute called Contents defined for it; which refers to the members of each of its groups.

Obviously, Contents is a multivalued attribute; it may or may not be unique.

An object that is a combination of aggregate and group, must be modeled as the aggregate of several classes, some of which are groups; e.g., A car is a frame, a chassis, an engine, seats, and a wheel set, where a wheel set is a group of four wheels. The Grouping construct is analyzed in detail elsewhere $[17]$ .

## 3.7. The USM metamodel

Figs. 12 and 13 depict the USM in terms of itself. The first shows a comprehensive definition of the USM represented in terms of the constructs. The relationships in USM are depicted in Fig. 13. A formal grammar for the USM has been developed and implemented.

![](/api/attachments/YBECVBCZ/fulltext/images/f895be8fe7335a313e8736c94420ac01fd58c52a147d251206980cc54611c7cd.jpg)  
Fig. 17. Interaction relationship view.

## 4. Intelligent tool for semantic modeling using the USM

We have developed a prototype system called Unibase-Modeler at the University of Arizona. The architecture of the tool is shown in Fig. 14. It runs on a network of IBM PS/2 machines under the Microsoft Windows environment. The software is written using Visual Basic and C.

The components of the tool are:

· Intelligent Dialog: The user interacts with Unibase-Modeler using a graphical user interface. It conducts the dialog with the user.

\- Inference Engine: The dialog is controlled by an inference engine. In developing a conceptual schema, the user is asked to define entity classes, attributes, and relationships.

\- Knowledge Base: Intelligence in the system is stored in a knowledge base in three parts: A rule base, an application-specific fact base, and an organization-specific fact base.

\- Design Repository: The definition of the schema is stored in the design repository. This is currently implemented using the Paradox relational database management system.

A unique feature is that it allows users to define the USM schema in a Group Environment. This allows users to work on their own individual workstation and view/modify the definitions of other designers simultaneously. The system thus allows collaborative design. One of the important functions performed by the tool is view integration.

![](/api/attachments/YBECVBCZ/fulltext/images/0b3cad4a6a789b7aec8e6a47c7a682e4270c14c339256bf2894c459b69375f8d.jpg)  
Fig. 18. Attribute view.

Appendix 1 shows some screens from a typical design session using the UNIBASE-Modeler. A typical session starts after the users log on to the system. They describe the application using some keywords, which open the appropriate application-specific fact base. Users then start designing the USM schema with the system providing design guidance. The dialog is controlled by the inference engine which uses the knowledge base components. The rule base checks for correctness of the schema; e.g., a rule ensures that any time a WEAK entity class is defined, the user specifies the STRONG entity class on which it is dependent. There are other rules to guide the users to define attributes and their properties. The application specific fact base contains information on the typical entity classes, their attributes and types of relationships one would expect to find within a particular application domain. For instance, if the user is defining a “Hospital” application, the system would open its fact base specific to this application and inform the user of previously defined entity classes, such as Physicians, Nurses, Operations, and Treatment. The user is thus able to start from an existing base of information and modify it as required. Thus the system assists users in improving the completeness of the conceptual schema. The organization-specific fact base contains information on synonyms and abbreviations specific to a company. As far as possible the system advises users to be consistent in their naming scheme.

![](/api/attachments/YBECVBCZ/fulltext/images/7c86577d91935e4a18bb82cbb531c396ab1502ca2e7345449cf4f0424b66c209.jpg)  
Fig. 19. Full screen view.

The tool performs view integration, assisted by the organization-specific fact base. Users can use the “Message” and “Phone” facility to exchange information with each other and clarify and resolve conflicts during the conceptual schema definition. We have found this to be very useful $[13]$ . Currently we are in the process of conducting a large scale validation of the system.

## 5. Conclusion

This paper has defined a conceptual model called the Unifying Semantic Model to depict the meaning of a real world situation that is to be captured in a database. An intelligent design tool called Unibase-Modeler was described. The USM is a synthesis of existing semantic models with several enhancements and new constructs. It provides an abstract information modeling mechanism and can support a means of specifying the universe of discourse for any interchange of information. It can also provide a mechanism for developing an interface for distributed databases. This model is being used to define the global conceptual schema for the IMDAS distributed database system at the National Institute of Standards and Technology [16]. Further work will include defining constructs to capture temporal aspects of an application as well as rules for insertions/deletions and updates in the the model. We are also developing an SQL based language for using the USM as the global model in a heterogeneous environment. We are also extending the tool to perform schema integration in a heterogeneous database environment.

## Appendix A

Figs. 15–19: Sample screens from Unibase-Modeler

## References

[1] Abiteboul, S. and R. Hull. “IFO A Formal Semantic Database Model”, ACM Transactions on Database Systems, Vol. 12, No. 4, Dec. 1987.

[2] M.L. Brodie, J. Mylopoulos, and J.W. Schmidt (Eds.) “On Conceptual Modeling”, Springer Verlag, New York, 1984.

[3] P.P. Chen. “The Entity Relationship Model – Toward a Unified View of Data”, ACM Transactions on Database Systems, Vol. 1, No. 1, March 1976, pp. 9-36.

[4] J. Choobineh, M.V. Mannino, and V.P. Tseng. “A Forms-Based Approach for Database Analysis and Design”, Communications of the ACM, Feb. 1992, pp. 108–120.

[5] M. Hammer and D. McLeod. “Database Description with SDM: A Semantic Database Model”, ACM Transactions on Database Systems, Vol. 6, No. 3, Sept. 1981, pp. 351–386.

[6] S. Hayne, and S. Ram. “Multi-User View Integration Systems (MUVIS): An Expert System for View Integration”, Proceedings of the Sixth International Conference on Data Engineering, February 1990, LA, pp. 402-409.

[7] R. Hull and R. King. “Semantic Database Modeling” Survey, Applications, and Research Issues”, ACM Computing Surveys, Vol. 19, No. 3, Sept. 1987, pp. 201–260.

[8] M. Loomis, M. “Data Modeling – The IDEF1 × Technique”, Proceedings of the IEEE Conference on Computers and Communications, Phoenix, Arizona, March 1986, pp. 146–151.

[9] L. Mark. “Defining Views in a Binary Relationship Model”, Information Systems, Vol. 12, No. 3, 1987, pp. 281–294.

[10] G.M. Nijssen and T.A. Halpin. “Conceptual Schema and Relational Database Design – A Fact Oriented Approach”, Prentice Hall, Australia, 1989.

[11] J. Peckham and F. Maryanski. “Semantic Data Models”, ACM Computing Surveys, Vol. 20, No. 3, Sept. 1988, pp. 153–189.

[12] Potter, W. and Trueblood, R.P. “Traditional, Semantic, and Hyper Semantic Approaches to Data Modeling”, IEEE Computer, 1988.

[13] S. Ram and V. Ramesh. “A Blackboard Architecture for Schema Integration”, forthcoming, IEEE Expert, 1995, 25pp.

[14] S. Ram. “: An Expert Systems Approach for Deriving Functional Dependencies from the Entity-Relationship Model”, forthcoming, Communications of the ACM, 1995, 25pp.

[15] S. Ram and S. Curran. “An Automated Tool for Relational Database Design”, Information Systems, Vol. 14, No. 3, 1989 pp. 247–259.

[16] S. Ram and E. Barkmeyer. “A Unifying Semantic Model for Integrating Multiple Heterogeneous Databases in Manufacturing”, Proceedings of IMS'91 – First International Workshop on Interoperability Among Databases, Kobe, Japan, April 1991, pp. 212–216.

[17] S. Ram and V. Storey. “Grouping and Composite: Extending the Realm of Semantic Modeling”, Proceedings of the 26th Hawaii International Conference on System Sciences – HICSS-26, Maui, Jan 1993, pp. 212–218.

[18] D. Reiner. “Database Design Tools”, in “Conceptual

Database Design: An Entity Relationship Approach", Benjamin Cummings Publishing Company, 1992, pp. 411-452.

[19] D. Shipman. “The Functional Data Model and Data Language DAPLEX”, ACM Transactions on Database Systems, Vol. 6, No. 1, March 1981, pp. 140–173.

[20] P. Shoval. “An Integrated Methodology for Functional Analysis, Process Design, and Database Design”, Information Systems, Vol. 16, No. 1, pp. 49–64, 1991.

[21] J.M. Smith and D. Smith. “Database Abstractions: Aggregation and Generalization”, ACM Transactions on Database Systems, Vol. 2, No. 2, March 1977, pp. 105–133.

[22] V. Storey and R. Goldstein. “A Methodology for Creating User Views in Database Design”, ACM Transactions on Database Design, Vol. 13, No. 3, Sept. 1988, pp. 305–338.

[23] S.Y. Su, V. Krishnamurthy, and H. Lam. “An Object-Oriented Semantic Association Model”, AI in Industrial Engineering and Manufacturing: Theoretical Issues and Applications, edited by S. Kumara, R. Kashyap, and A.L. Soyster, 1988.

![](/api/attachments/YBECVBCZ/fulltext/images/e1db293c353bc09f13704056788d940922931e26a9062d6dd527549b70436663.jpg)

Sudha Ram is Associate Professor of Management Information Systems at the University of Arizona. She received a B.S. degree in mathematics, physics and chemistry from the University of Madras in 1979, PGDM from the Indian Institute of Management, Calcutta in 1981 and a Ph.D. from the University of Illinois at Urbana-Champaign, in 1985. Dr. Ram has published articles in such journals as Communications of the ACM, IEEE Expert, IEEE Transactions on

Knowledge and Data Engineering, Information Systems, Information Science, and Management Science. She has also presented here research at several conferences such as International Conference on Informations Systems, International Conference on Data Engineering and other IEEE and ACM conferences. She was the guest-editor for the December 1991 issue of IEEE Computer "Heterogeneous Distributed Database Systems". Dr. Ram's research deals with modeling and analysis of database and knowledge based systems for manufacturing, scientific and business applications. Her research on distributed databases has been funded by IBM, NCR, US ARMY, and NIST. Specifically, the research deals with Semantic Modeling, Data Allocation, Schema and View Integration, and Tools for database design. Dr. Ram is the Director of the Graduate Program in MIS at the University of Arizona. She serves as a member of the editorial board of the Journal of Database Management, associate editor of Journal of Systems and Software, editor for the IEEE Computer Society Press. She is a member of ACM, IEEE Computer Society and TIMS.
