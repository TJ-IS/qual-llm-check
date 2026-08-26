---
otero_id: 24504
otero_key: "ZDHA864Y"
title: "The Object-Oriented Entity-Relationship Model (O<scp>oerm</scp>)"
authors: "Kevin Gorman; Joobin Choobineh"
year: "1990"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1990.11517896"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Object-Oriented Entity-Relationship Model (Ooerm)

## Kevin Gorman & Joobin Choobineh

To cite this article: Kevin Gorman & Joobin Choobineh (1990) The Object-Oriented Entity-Relationship Model (Ooerm), Journal of Management Information Systems, 7:3, 41-65, DOI: 10.1080/07421222.1990.11517896

To link to this article: https://doi.org/10.1080/07421222.1990.11517896

![](/api/attachments/ZDHA864Y/fulltext/images/87ea9d6318524ea21ae1603eb28c8017b0dc3cfdbd68dd665b096cc9fae246cb.jpg)

Published online: 21 Dec 2015.

![](/api/attachments/ZDHA864Y/fulltext/images/cde33cbd1c608bf464425764a773927569bd145158ccc7039c8672be6186e457.jpg)

Submit your article to this journal ↗

![](/api/attachments/ZDHA864Y/fulltext/images/ea43cc26527cf2e8840b80d0d3d60a7e3ac6317343297bbbe28da55e874be16c.jpg)

Article views: 1

![](/api/attachments/ZDHA864Y/fulltext/images/3eb14fc801c3ba160380cd4cf6c56e911fbc5a3ec64269ebdfba7d5c2d9aba09.jpg)

View related articles ↗

![](/api/attachments/ZDHA864Y/fulltext/images/8f4acd8f6dc2a06bb57f93f76e2be77d56f47749450601e8a7358b2fc3760ea0.jpg)

Citing articles: 7 View citing articles ↗

# The Object-Oriented Entity-Relationship Model (OOERM)

KEVIN GORMAN and JOOBIN CHOOBINEH

KEVIN GORMAN is Assistant Professor in the Department of Management Information Systems and Operations Management at the University of North Carolina at Charlotte. He received his Ph.D. in management information systems from Texas A&M University in December 1990. He has an industry data processing background as a computer programmer and systems analyst. His research interests include database design, object-oriented modeling, database query languages, artificial intelligence, and expert systems. He is a member of the Association for Computing Machinery (ACM), IEEE Computer Society, The Institute of Management Science, Decision Sciences Institute, and Data Processing Management Association.

JOOBIN CHOOBINEH received his Ph.D. in management information systems from the University of Arizona, Tucson in 1985. He is Assistant Professor in the Department of Business Analysis and Research, College of Business Administration, Texas A&M University. Prior to joining the faculty at Texas A&M, he was Research Associate in the Department of Management Information Systems at the University of Arizona. His research interests include conceptual data modeling, integration of data and mathematical models, application of artificial intelligence techniques to database design process, and expert database systems. The results of his research have been published in IEEE Transactions on Software Engineering, Decision Support Systems, Information Systems, Journal of Management Information Systems, Information and Management, Omega, The International Journal of Management Science, IEEE Database Engineering, and numerous conference proceedings. He is a member of the Association for Computing Machinery (ACM), IEEE Computer Society, and The Institute of Management Science.

ABSTRACT: The Object-Oriented Entity-Relationship Model (OOERM) and its associated diagramming technique (OOERD) are presented as a natural extension to the ER approach for modeling the dynamics of entity classes. In addition to modeling static properties, OOERM incorporates concepts from the object-oriented programming (OOP) paradigm to model operational properties of entities. Relationships among entities are used in message passing to allow an entity to access the attributes and operations of other related entities. An OOERD is a graphical abstraction of an underlying OOERM scheme description that is used to depict the dynamics of message passing among entities. The synergy between OOP and ER concepts is also discussed. The syntax and semantics of the OOERM language are informally presented, along with the graphic notations and icons of the OOERD. Structural and operational modeling in OOERM is illustrated through examples.

An earlier version of this paper was originally published in the Proceedings of the Twenty-Third Hawaii International Conference on System Sciences (IEEE Computer Society Press, 1990).

KEYWORDS AND PHRASES: entity-relationship model, object-oriented programming paradigm, structure and dynamic modeling.

ACKNOWLEDGMENT: We thank the anonymous referees for their valuable comments. The quality of the presentation and the content has improved as a result of their suggestions.

## 1. Introduction

THE ENTITY-RELATIONSHIP MODEL (ERM) [5] OF DATA PROVIDED a user-oriented generalization of the three classical data models (hierarchical, network, and relational). It is closely identified with its pictorial design representation, the entity-relationship diagram (ERD).

The ER model is best thought of as a thin layer on top of the basic relational model $[8]$ . A set of entity-relationship diagrams maps directly to a relational scheme. Additionally, the inherent integrity constraints are very similar to the key constraints of the relational model. No operations were initially proposed for the ER model. Chen intended that ER model schemes be mapped to relational schemes $[5]$ .

The popularity of the model is attributed to the diagramming techniques $[8]$ and the “naturalness” of the representation $[4]$ . Disadvantages of the ER model include its lack of support for generalization and inheritance, operations, and explicit constraints $[4]$ .

Some of the structural features lacking in Chen's original model have been addressed in various extended entity-relationship models (EERM) (see, e.g., [1, 9, 18]). We propose the Object-Oriented Entity Relationship Model (OOERM), which overcomes the operational disadvantages of the ER model by incorporating concepts from the Object-Oriented Programming Paradigm (OOPP). OOERM includes support for both "traditional" and "object-oriented" data model operations.

Traditional data operations are of two types:

1. Simple operations: retrieval, insertion, deletion, or updating of extensional data.

2. Transactions: a series of simple operations treated as a unit and occurring upon the satisfaction of certain conditions (for example, an order entry process description).

Recently, the development of Object-Oriented Data Models and the popularity of Object-Oriented Programming (OOP) have added the following operational requirements:

1. Operations on generalization hierarchies: operations that traverse the hierarchy, moving an entity instance up the hierarchy (generalizing it), or down the hierarchy (specializing it); enabling the modeling of stages of development of an entity, design alternatives, etc.

2. An abstract data typing (ADT) capability: operations (called methods) that are specifically defined for individual entity classes, making operations entity-type specific.

The OOP paradigm has several major features, including:

1. enforcement of the "information hiding" principle,

2. abstract data type encapsulation,

3. generalization and inheritance, and

4. polymorphism.

“Information hiding” means that operations are written with two independent and separable parts: a specification and a representation. Users of the operation know only the specification (what input is required, and what output is produced) and can’t write code that depends on the representation. Implementors of the operation are free to change the representation (e.g., to improve efficiency) but can’t change the specification (the part relied on by users).

Encapsulation means that the entity class description includes both its attributes and its methods. For example, a beam entity class description includes data attributes such as type, size, and material plus operational methods such as create, draw, and edit. Attributes model the state of an object, while methods define its behavior, i.e., how it changes state.

Generalization forms a higher level general entity class (called a superclass) by grouping similar lower level specialized classes (called subclasses). For example, the Employee superclass groups the Management and Staff subclasses. Property inheritance states that each subclass inherits both the general attributes and methods of the superclass, while adding special properties of its own.

Polymorphism means the ability to take several forms. In object-oriented programming, it refers to (potentially) different representations of the same property based on position in the generalization class hierarchy. For example, the “method” (pun intended) of gross pay calculation may depend on the subclass of Employee.

OOP has received considerable recent attention in software engineering, because the above features combine to yield the following advantages (over software development in other types of languages):

1. The ability to develop reusable software modules: entity class descriptions whose operations can be readily modified and expanded; and combined with various other entity classes to form new software [15].

2. Increased productivity and reduced maintenance costs [2, 6, 14].

ER modeling and OOP form a natural pairing. Both hold three common views on system development:

1. The modular decomposition of a system should be initially based on the entity classes the system manipulates as opposed to the functions the system performs. For example, an order processing system should be designed by first (partially) describing the customers, orders, and inventory classes. Later description of the order entry, filling, and posting functions may revise the entity class descriptions. The categories of entities on which the system acts are more stable over time than are the activities required of the system.

2. A specification by refinement approach is recommended to further define a system by building upon existing classes.

3. Entity class models have a direct and natural correspondence to real-world objects and processing, especially for problems of natural concurrency. The latter point is attested to by the fact that most simulation models are object-oriented. In process-oriented models, data is external to the processes, while in object-oriented models, processes are internal to objects, a more natural way of simulating concurrent activities.

The objected-oriented view is a natural extension of the entity–attribute–relationship view. When we think of an object or entity (e.g., a bicycle), we consider its attributes, such as color, manufacturer, cost, etc. But we also naturally consider the things we can normally do with it (ride it, lock it, carry it on a bikerack, etc.).

We therefore propose OOERM with its associated diagramming techniques as a natural extension to the ER approach for modeling the dynamics of entity classes. We begin with a model structurally equivalent to previous extended entity-relationship models (EERM), such as $[1, 9, 18]$ . Simple class operations are defined with their generalization hierarchy semantics. Application-specific transactions are modeled using ADT operations. Object-Oriented Entity-Relationship Diagrams (OOERDs) provide a graphical abstraction of processing described in OOERM schemes and user queries.

We informally discuss OOERM in this paper, highlighting model operations and their ER-like diagrammatic depiction. A more detailed and rigorous discussion of the model can be found in [10]. Forthcoming related papers will emphasize:

1. Model design—the incorporation of salient features from both semantic data models and object-oriented programming.

2. Theoretical basis—formal structural and operational mappings to the relational model.

3. Query language—the model's query language (informally introduced in this paper), its theoretical basis, and its (formal) syntax.

In section 2, we discuss the Object-Oriented Programming Paradigm (OOPP) with a comparison of OOP and ER terminologies. Sections 3 and 4 discuss OOERM, including both the syntax and semantics of the language as well as the graphic notations and icons of the associated diagrams (OOERDs). Section 3 focuses on structural modeling in OOERM, while section 4 addresses operational modeling. In section 5, a comparison is made between the OOERM and other relevant research. In the conclusion of the paper, section 6, we summarize the advantages of the model and the synergy between OOP and ER concepts.

## 2. The Object-Oriented Programming Paradigm (OOPP)

OBJECT-ORIENTED PROGRAMMING LANGUAGES, such as SMALLTALK, C $^{++}$ , and ADA, have vocabularies of their own to describe the constructs used in the object-oriented approach to program design. This section will provide definitions of these terms. The terms will be used in later sections. Terms are in italic type as they are introduced.

An object is a “package” of information and a description of its manipulation. In procedural programming terminology, this roughly corresponds to a set of (related)

variables and a set of operations on these variables. A message is a specification of one manipulation on an object. The specification consists of:

1. the receiver—the object to be manipulated,

2. the selector—the symbolic name of the manipulation, and

3. (optional) arguments—possible other objects taking part in the manipulation.

A message resembles a procedure call in procedural programming. It represents a request for some type of processing from a “sending” object, called a client or acquaintance, to the receiver. The receiver determines how the manipulation is accomplished. The sender merely knows what to expect in terms of a response (if any). A method is a description of a single type of manipulation, a procedure-like object. Methods are found in receiving objects and are “selected” in response to messages.

The object-oriented programming paradigm emphasizes the distinction between the “inside” and “outside” views of an object. The inside view is the implementation (the representation) by its programmer that determines how a request is handled, how a manipulation is accomplished. The outside view is the abstract behavioral view (the specification) of other client objects, i.e., what the request will accomplish. An object’s protocol is the set of messages to which the object will respond. An object’s variables and methods are individually declared to be either public or private, corresponding to the outside and inside views, respectively.

A class is an object type, a description of a set of similar objects, including both its variables and its methods (encapsulation). An instance is a token, an object of a particular class. Class variables are private variables shared by all instances of a class. Inheritance allows for the creation of generalization hierarchies. Subclasses automatically inherit both the methods and variables (except class variables) of superclasses in the hierarchy. Subclasses can both add new methods or variables, and modify any inherited method or variable specification.

## 2.1. The Analogy between OOP and ERM

We briefly describe the ER model in order to compare it to the OOPP. In the ER model the world is viewed as consisting of entities and relationships among them [5]. Entities and relationships are characterized by their attributes. Each entity plays a role in any relationship that it participates in. Figure 1 depicts an ER diagram.

Rectangular nodes represent entity sets, circular nodes represent attributes, and diamond-shaped nodes represent relationships. Arcs in the diagram may be labeled with appropriate role names. Maximum cardinalities are indicated for the entity sets by the number or letter on each side of the relationship node. Thus, in the figure, the CUSTOMERS and ORDERS entity sets participate in a "Submit" relationship set. In the "Submit" relationship, the role names for CUSTOMERS and ORDERS are "ORDERING\_CUSTOMER" and "ORDERS\_FOR\_CUSTOMER," respectively. Each customer may submit many order entities, a one-to-many relationship. Each entity set and relationship set has its own set of attributes with their associated domains, called value sets in the ER model.

![](/api/attachments/ZDHA864Y/fulltext/images/76831dc3f5b0d3fd3cbb55a59c8a238bdebf3ea1a6bffafca79b38516e118c06.jpg)  
Figure 1. Entity-Relationship Diagram

![](/api/attachments/ZDHA864Y/fulltext/images/a8243037d4cedede85f728584a563d5ae9163090427fecfd673e60fde3097245.jpg)  
Figure 2. Structural OOERD Example

A summary of terminological analogies that can be drawn between the OOPP and the ER model is provided in Table 1. Since the primary concern of OOP is operations, while that of the ER model is structure, each comparison represents more of an analogy rather than a direct correspondence.

A class or object type in OOP corresponds to an ER entity set. An instance corresponds to an ER entity. In OOP, the object's set of variables and methods corresponds to an entity's set of attributes in the ER model. In OOP, "attributes" or properties of an object may be internally represented as either variables or methods. As will be demonstrated with the examples of section 4, the outside view of an object in OOP does not recognize the distinction.

In object-oriented design, there is a need to establish the “visibility” of an object in relation to others, i.e., what objects it can access, and what objects it can be accessed by [2]. In the ER approach, this is accomplished by establishing the relationships among objects.

Table 1 OOP and ER Analogies

<table><tr><td>OOP</td><td>ER</td></tr><tr><td>Class or object type</td><td>Entity set</td></tr><tr><td>Instance</td><td>Entity</td></tr><tr><td>Variables</td><td>Attributes</td></tr><tr><td>Methods</td><td>None</td></tr><tr><td>Object “visibility”</td><td>Relationships</td></tr><tr><td>Sending &amp; receiving objects</td><td>Roles</td></tr></table>

Message passing makes use of established relationships (object visibility). This allows a sending object to access the variables and methods of another related object, the receiving object. The sending object (also called a client or acquaintance) and the receiving object thus play reciprocal roles in the ER model sense. Section 3 shows how relationships and role names are represented in the structural portion of an OOERM scheme. Section 4 illustrates the use of role names in message passing.

## 3. Structural Modeling in OOERM

IN THIS SECTION WE WILL DISCUSS THE LANGUAGE CONSTRUCTS and their associated graphical representations for modeling structures in OOERM. We illustrate the constructs using an order-entry processing example, graphically depicted in Figure 2. CUSTOMERS submit orders containing line items. Each line item represents an order for a specific quantity of a particular inventory item.

An OOERM scheme description is a collection of entity classes representing “relevant abstractions” in a particular application environment. The structural description is based on the Semantic Data Model (SDM) [12] with modifications and extensions for closer conformity to the ER model and a natural interfacing to OOP.

Example 1 shows the OOERM description of the ORDERS entity class. Letter case variation accents the semantic distinctions (discussed in the paragraphs that follow). Class and class reference names are shown in all uppercase letters. Attribute and class attribute names are shown in upper and lower case. All other features are shown in all lowercase letters.

Each class is optionally described with three types of structural properties:

1. Attributes: naming the stored values of each class instance, e.g., attributes Order\_Number and Order\_Date for the class ORDERS.

2. Class references: associating related classes, e.g., the class reference name ORDERING\_CUSTOMER associates the related classes ORDERS and CUSTOMERS.

3. Class attributes: describing properties of a class taken as a whole, e.g., Last\_In-

```txt
ORDERS
attributes :
Order_Number : order_numbers
may not be null
not changeable
Order_Date : dates
class references :
ORDERING_CUSTOMER : CUSTOMERS
may not be null
inverse : ORDERS_FOR_CUSTOMER
LINE_ITEMS_FOR_ORDER : LINE_ITEMS
multivalued
identifiers:
Order_Number
```

Example 1. ORDERS Class Scheme

voice\_Number, a class attribute of the class INVOICES (see Example 2, described later in this section).

Identifiers are combinations of attributes and class references serving as logical keys to identify uniquely class instances, e.g., Order\_Number of the ORDERS class.

Each structural property has a set of defining features or constraints. The first feature specified is the domain or object type. Syntactically, the domain is given after the colon following the property name; i.e., informally, the syntax is “property name: domain.” Attribute and class attribute domains consist of system-defined primitive types: strings, integers, reals, money, etc., or named restrictions of these such as order\_numbers (integers less than 10,000) for attribute Order\_Number. Class reference domains consist of entity classes, e.g., domain CUSTOMERS for the class reference ORDERING\_CUSTOMER.

Class reference names directly correspond to ER model role names. The inverse specification identifies an associated class's symmetric class reference. For example, ORDERS\_FOR\_CUSTOMER is a class reference of the CUSTOMERS class whose domain is ORDERS. The inverse thus provides a reciprocal role name in the ER model sense (see Figure 1).

Other defining features of structural properties that may be optionally specified include: "single valued" (default) or "multivalued"; "may not be null"; and "not changeable." Constraints specifiable for attributes are also specifiable for relationships among entities (modeled by class references). Thus, an ORDERS class instance must have an ORDERING\_CUSTOMER (may not be null), and can have several LINE\_ITEMS\_FOR\_ORDER (multivalued).

```makefile
REJECTED_ORDERS : ORDERS where specified
ACCEPTED_ORDERS : ORDERS where specified
INVOICES : ACCEPTED_ORDERS where specified
attributes :
Shipping_Charges : money
Order_Discount : money
derivation :
Result := ORDERING_CUSTOMER.Discount_Amount (Order_Total)
Invoice_Number : invoice_numbers
derivation :
Result := Last_Invoice_Number + 1
class attributes :
Last_Invoice_Number : invoice_numbers
```  
Example 2. ORDERS Subclasses Scheme

Figure 2 includes a generalization hierarchy for the superclass ORDERS. The double arrows represent subclasses, with the head of the arrow pointing to the higher level class. The “hollow” tail represents a subclass that is a subset of the higher level class (with no additional properties). The “filled-in” tail represents a subclass that is a specialization of the higher level class (with its own additional properties).

Example 2 is an OOERM scheme description of the subclasses shown in Figure 1. Subclasses are specified using various types of predicates applied to instances of the defining class. Among these are user-controllable subclasses, which employ the predicate “where specified.” Membership in the class occurs as a result of an operation during processing.

Property inheritance is also illustrated by the generalization hierarchy for ORDERS. All subclasses of ORDERS inherit the properties of the superclass ORDERS. Class attributes (if any) are not inherited. Additionally, the subclass may add properties of its own. Thus, the INVOICES subclass of ACCEPTED\_ORDERS has three new attributes. (We explain the derivation feature (shown with the Order\_Discount and Invoice\_Number attributes) under operations modeling in section 4.2.)

## 4. Operations Modeling in OOERM

IN THIS SECTION WE DISCUSS THE LANGUAGE CONSTRUCTS and their associated graphical representations for modeling operations in OOERM.

## 4.1. Methods and Message Passing

Example 3 illustrates the basic object-oriented programming concepts for methods discussed in section 2, in the syntax of OOERM. The entity type INVENTORY\_ITEMS is described, including some of its attributes and operations or methods.

```txt
INVENTORY_ITEMS
attributes :
-
-
Quantity_On_Hand : integer
Item_Backorder : integer
Unit_Cost : money { Private }
-
-
operations :
Item_Rejected (quantity : integer) : boolean
actions :
Result := (quantity > Quantity_On_Hand)
Order_Item (quantity : integer)
prerequisites : not Item_Rejected (quantity)
actions :
Quantity_On_Hand := Quantity_On_Hand - quantity
Backorder_Item (quantity : integer)
actions :
Item_Backorder := Item_Backorder + quantity
```

Example 3. INVENTORY\_ITEMS Class Scheme

Formal syntax is provided in [10]. Informally, the syntax of the methods may be described as:

Method\_Name (optional parameters): optional returned domain value(s)

prerequisites: optional set of assertions

actions:

set of messages or assignments.

In Example 3, Item\_Rejected is a method for determining if there is insufficient stock on hand to fill an order for a given item. It returns a Boolean (true or false) "Result." ("Result" is a key word for the domain value(s) being returned by the method.) Order\_Item and Backorder\_Item are methods for changing the state of the item based on whether the item is being ordered or backordered, respectively. Prerequisites are Boolean expressions that must be satisfied before the actions can be executed. To use INVENTORY\_ITEMS, a client class (say LINE\_ITEMS) would declare a class reference of domain INVENTORY\_ITEMS, as illustrated by Example 4.

Declaring class reference ITEM\_ORDERED of domain INVENTORY\_ITEMS allows access to the attributes and operations of the INVENTORY\_ITEMS class through message specifications. These messages would appear in methods of the

```txt
LINE_ITEMS
attributes :
-
-
Order_Quantity : integer
class references :
-
-
ITEM_ORDERED : INVENTORY_ITEMS
operations :
Submit_Order
actions :
If ITEM_ORDERED.Item_Rejected (Order_Quantity)
then
ITEM_ORDERED.Backorder_Item (Order_Quantity)
Else
ITEM_ORDERED.Order_Item (Order_Quantity)
Endif
```

Example 4. LINE\_ITEMS Class Scheme

LINE\_ITEMS class, such as the Submit\_Order method. (This method will be discussed in detail in section 4.3.) Example messages are:

```txt
ITEM_ORDERED.Order_Item (5000)
ITEM_ORDERED.Backorder_Item (Order_Quantity)
PRINT ITEM_ORDERED.Quantity_On_Hand.
```

Informally, using the terms introduced in section 2, the message syntax for invoking all operations in OOERM may be described as:

receiver. selector (optional arguments).

The client class LINE\_ITEMS has an outside view of the methods contained in the INVENTORY\_ITEMS class. In these examples, only the specification of the attribute and method is visible for public attributes and methods (those not explicitly declared private, such as Unit\_Cost in Example 3). The representation, i.e., the derivation or action, is not visible to the client entity. Thus, the client knows only what arguments are required and what object types will be returned (if any). The client is unaware of how the request is handled. This is the implementation or inside view. The client class is in fact unaware of whether Quantity\_On\_Hand, e.g., is an attribute or a method without parameters. It is the choice of the implementing class as to whether the Quantity\_On\_Hand value is a stored attribute of every instance of the class, or computed by a method using a list of previous transactions.

```txt
ORDERS
attributes :
-
class references :
LINE_ITEMS_FOR_ORDER : LINE_ITEMS
multivalued
-
operations :
Order_Total : money
actions :
Result := sum (LINE_ITEMS_FOR_ORDER.Extension)
Example 5. Order_Total Method Example
```

## 4.2. Methods Versus Attribute Derivations

Values returned by methods are procedurally obtained through “actions” specification. For example, consider the action specification of the ORDERS class method Order\_Total shown in Example 5. The method returns the sum of the Extension attribute (or method) values for all LINE\_ITEMS instances related to the given instance of the Order class. Note that the specification “LINE\_ITEMS\_FOR\_ORDER.Extension” (termed a mapping in SDM) represents a message in OOERM. (Functions such as “sum,” “count,” and “average” operate on multivalued attributes (or methods) arguments. A method returns a single value or a set of values of a particular domain.)

Similarly, attribute values can be procedurally derived through “derivation” specification. The INVOICES class (see Example 2) illustrates two attribute derivations. An arithmetic expression derives the Invoice\_Number value, while a message derives the Order\_Discount value. Message specification is a more general procedural derivation than built-in numeric calculations using arithmetic operators and functions such as “sum” and “count.” As with all message specifications, the sending object merely knows what to expect in terms of the returned value’s domain. It has no knowledge of how that value is derived. In this example, the message specification could conceivably represent retrieval of a value from an array or table or any other type of method or procedure invocation. We will further address attribute derivation in section 4.5.

Note the following semantic distinction between attributes with derivations and operations that return values. In OOERM, derivations assign an attribute's initial value at object creation. Thus, when an INVOICES class instance is created, attribute derivations provide initial values for attributes Order\_Discoun and Invoice\_Number. Operations may later modify these values. On the other hand, method actions are executed at every object reference to determine any returned value(s). Thus, every reference to Order\_Total (logically) results in a new procedure execution.

![](/api/attachments/ZDHA864Y/fulltext/images/244bfe750593a1ab6aa8806d1fd040d65152bbfae54ed8fbd282adf6ebce20f3.jpg)  
(i, j, or k is an integer representing the sequence number for an operation)  
Figure 3. OOERD Dynamic Icons

## 4.3. Object-Oriented Entity-Relationship Diagram (OOERD)

In this section we introduce Object-Oriented Entity-Relationship Diagrams (OOERD). In later sections we will extend and further apply them. Figure 3 shows the dynamic icons for modeling methods. Methods are modeled by ovals with the method name enclosed. Message passing is indicated by arrows with dotted-line "tails." The optional parameters being sent are shown above the arrow tail, while optional results being returned are shown below the arrow tail. Conditional branching is indicated by arrows "forking" from the message path, based on the condition being true (T) or false (F). The ordinal position of a message in the sequence of messages is represented by an integer enclosed in parentheses.

Figure 4 is an OOERD for the inventory item ordering example of section 4.1. The relevant structural constructs are augmented with the dynamic icons for modeling operations. The Submit\_Order method of the LINE\_ITEMS class of Example 4 represents a request from the LINE\_ITEMS class to order a specific quantity i is an integer representing the sequence number for the operation.)

![](/api/attachments/ZDHA864Y/fulltext/images/fc9a3a1e386aba5d95fac03c871f25e88dde8716bd2d211cb39d86df1aea551f.jpg)  
Figure 4. OOERD Example of Message Passing

![](/api/attachments/ZDHA864Y/fulltext/images/7aa49180d028c6209045744900bcf0225403c2c792a1087eaf7e6764e2dfde16.jpg)  
Figure 5. Predefined Operations

(Order\_Quantity) of a particular instance of the INVENTORY\_ITEMS class, indicated by the class reference (role name) ITEM\_ORDERED.

Because of the prerequisite of the Order\_Item method of the INVENTORY\_ITEMS class (shown in Example 3), Submit\_Order issues the following sequence of messages:

(1) A message requesting the Item\_Rejected method to determine if the order can be filled, based on the value of the Order\_Quantity attribute being passed.

(2) A true or false (T or F) value is then returned.

(3) Based on the value returned, a message requesting an order (if F) or a backorder (if T) is sent to the INVENTORY\_ITEMS class.

Methods are shown as properties of the entity attached by a solid line, similar to attributes. The values passed (indicated by dotted lines) by the sending or client entity are usually those of its attributes or methods. The diagram represents the “outside view” of the client entity, in this case the LINE\_ITEMS class.

## 4.4. Predefined Operations

Five predefined operations are implicitly specified properties of all entity classes. These five operations, listed in Figure 5, have the same default definition for all classes. We will discuss the first four of these in this section. Database queries using Select will be discussed in section 4.7.

Graphically, a predefined operation is represented by a method oval superimposed over the entity class to which it applies. As indicated in Figure 5, the first letter of the operation is placed in the right portion of the oval. The default definition, applying to all classes, may be augmented by additional operations specific to a particular class. The ordinal position of the predefined operation in a sequence of operations and messages is enclosed in parentheses and placed in the left-hand portion of the oval.

Messages invoking predefined operations can be specified either interactively by the user, or in the action portion of methods. An example of interactive use is the message: ORDERS.Create entered by the user to initiate the process of entering orders.

To identify specific class instances to which the operation applies, a “where” clause can be added to the predefined operations. This is similar to the “where” clause in SQL [8] and is particularly useful for interactive use of the operations. Informally, the “where” clause syntax is: where predicate. An example is the following: REJECTED\_ORDERS.Delete where Order\_Date < ‘900716’.

The Create operation has no arguments, and is used to assign values to the attributes and class references of an entity instance. Attributes that do not have a derivation feature have their values supplied by the user or invoker of the operation. Using the definition of the Create operation, the process of entering orders can be invoked using the message ORDERS.Create. In Example 6, we show additional parts of the ORDERS class scheme. Other components of the ORDERS scheme were depicted in Example 1.

The action specification for the Create operation given in the ORDERS class scheme is considered to be an addition to the predefined Create operation. Thus, after assigning values to the ORDERS object through the predefined Create operation, the other action specifications are executed. The specification requests a “credit check” of the ORDERING\_CUSTOMER, passing the Order\_Total value to the CUSTOMERS class. Based on the returned Boolean value, the ORDERS object is added to either the REJECTED\_ORDERS or ACCEPTED\_ORDERS subclass. Graphically, this operation is depicted in Figure 6.

The Add\_To\_Subclass operation syntax is: Subclass.Add\_To\_Subclass. The operation identifies a class instance as a member of a subclass defined using the predicate "where specified." In Example 6, the operation indicates which ORDERS instances belong to the subclasses REJECTED\_ORDERS and ACCEPTED\_ORDERS. Both of these subclasses are subsets of the base class.

```txt
ORDERS
attributes :
-
-
-
class references :
ORDERING_CUSTOMER : CUSTOMERS
may not be null
inverse : ORDERS_FOR_CUSTOMER
LINE_ITEMS_FOR_ORDER : LINE_ITEMS
multivalued
operations :
Order_Total : money
actions :
Result := sum (LINE_ITEMS_FOR_ORDER.Extension)
Create
actions :
If ORDERING_CUSTOMER.Order_Rejected (Order_Total)
then
REJECTED_ORDERS.Add_To_Subclass
Else
ACCEPTED_ORDERS.Add_To_Subclass
Endif
```

Example 6. Predefined Operations Example

The Add\_To\_Subclass operation pertains to all subclasses of a class including those that form a generalization hierarchy. As an example, the INVOICES entity class of Example 2 is a subclass of ACCEPTED\_ORDERS, which has its own additional attributes. An example of a message to invoke the predefined operation is:

INVOICES.Add\_To\_Subclass

where in ACCEPTED\_ORDERS and Order\_Date = '900401'

The “range predicate”: in ACCEPTED\_ORDERS restricts the class instances included in the operation. The Add\_To\_Subclass operation assigns values to the additional properties (similar to the Create operation) as part of the process of making it an instance of the subclass.

The Remove\_From\_Subclass and Delete operations have no arguments. The remove operation removes the object from membership in its current subclass and any descendant subclasses of which it is a member. For example, the object message: ACCEPTED\_ORDERS.Remove\_From\_Subclass would remove the object from membership in ACCEPTED\_ORDERS and in INVOICES (if applicable). The object would retain its membership in ORDERS, a higher level class. The Delete operation removes an object from all subclasses in a hierarchy (both higher and lower level) of which it is a member.

![](/api/attachments/ZDHA864Y/fulltext/images/4ee96969df9f48c801264f8117a41d6dbd3b4bb23ee55798dac13d7f1870bfdc.jpg)  
Figure 6. OOERD Example of Predefined Operations

## 4.5. Attribute Derivation

In this section we illustrate the use of OOERDs in modeling the operational dynamics of attribute derivation. Consider attribute Order\_Discount of the INVOICES class (previously shown in Example 2):

Order\_Discount : money

derivation :

$$
\text { Result } := \text { ORDERING\_CUSTOMER.Discount\_Amount(Order\_Total) }
$$

A discount is to be applied based on the Order\_Total value. A message determines the derivation of the attribute's value. Figure 7 depicts the procedural value assignment. The Add\_To\_Subclass operation is applied to the INVOICES subclass, a specialization of the ACCEPTED\_ORDERS class. The operation sends a message passing the Order\_Total value to the Discount\_Amount method of the CUSTOMERS class. The method returns a value to the Order\_Discount attribute.

The attribute Quantity\_Shipped of the LINE\_ITEMS object class of Example 7 illustrates the use of a rule to assign attribute values at the time of object creation. The If statement predicate is a message whose requested method returns a Boolean value.

Figure 8 is the OOERD for the derivation rule assignment of Example 7. In this figure, the Create operation is applied to the LINE\_ITEMS class. The operation sends a message to the Item\_Rejected method to determine if the order can be filled based on the value of the attribute Order\_Quantity being passed. A true or false (T or F) value

![](/api/attachments/ZDHA864Y/fulltext/images/35af85cda3493269f68df2debaa0821662a82b10263d36eb3149da6d80c68fc5.jpg)  
Figure 7. Derivation Procedure Example

![](/api/attachments/ZDHA864Y/fulltext/images/6af47406ec53cd9d5b1f0b4216ed3d8e384347185f30d161fdecb496149c4de6.jpg)  
Figure 8. Derivation Rule Example

```autohotkey
LINE_ITEMS
attributes :
-
-
Order_Quantity : integer
Quantity_Shipped : integer
derivation :
If ITEM_ORDERED.Item_Rejected (Order_Quantity)
then
Result := 0
Else
Result := Order_Quantity
Endif
class references :
ITEM_ORDERED : INVENTORY_ITEMS
```

Example 7. Derivation Rule Example Schedule

is returned. Based on the value returned, the value of the attribute Quantity\_Shipped is set to 0 (if T) or to the value of the attribute Order\_Quantity (if F).

## 4.6. Process Modeling with OOERDs

In the previous sections, OOERDs illustrate the dynamics of individual methods and attribute derivations. Each diagram requires sequencing only two messages. Modeling a particular application process (e.g., order-entry) requires sequencing several messages. Figure 9 presents an OOERD for an example order-entry process. It embodies a combination of the Create ORDERS operation (Figure 6), the Create LINE\_ITEMS operation, and Submit\_Order operation (Figure 4). In Figure 9, the Create LINE\_ITEMS operation results from the Create ORDERS operation. The LINE\_ITEMS Create method invokes the Submit\_Order method. (For simplicity, the earlier example ORDERS and LINE\_ITEMS scheme descriptions did not include the latter two steps.) Note the sequence of operations in the overall process.

OOERDs are intended to model individual application processes encoded in the data model scheme description. The graphic model contributes a pictorial view of state changes resulting from process execution. For example, Figure 9's order-entry process model reveals that:

1. each created ORDERS class instance is classified as being ACCEPTED or REJECTED based on Order\_Total;

2. each ORDERS class instance creates a set of LINE\_ITEMS class instances;

3. each LINE\_ITEMS class instance "submits an order" requesting an Order\_Quantity of a particular INVENTORY\_ITEMS class instance;

![](/api/attachments/ZDHA864Y/fulltext/images/239a52c3d2c83c0a406847ad7da6729edbbe644b3d0c44f32e1c74a2a1959148.jpg)  
Figure 9. OOERD of Order Entry

4. each request results in an "ordered" or "backordered" item based on Order\_Quantity.

Given this purpose, the following rules should be followed in OOERD construction:

1. One diagram should be drawn for each application process. For example, in order processing, separate diagrams would depict order-filling, order-posting, etc.

2. Each diagram should contain only the structural and operational details relevant to the process. Only the classes, attributes, and operations directly involved in the process should be depicted in the diagram.

We may consider Figure 9 as presenting a middle level of dynamic detail. More detailed diagrams could include attribute derivations. As discussed earlier, derivation code execution assigns initial attribute values for new class instances. These occur through Create and Add\_To\_Subclass operations. Less detailed diagrams might only include methods that execute the predefined class operations. Thus, a less detailed diagram of order-entry would not include the Submit\_Order method and the three methods called by it.

![](/api/attachments/ZDHA864Y/fulltext/images/edc0525579665cec51ea9ff9ad8a5de434d1c90489d0e350f0d183aa27817c3c.jpg)  
Figure 10. OOERD Query Example

## 4.7. Queries

Users can query the database in a syntax reminiscent of SQL. Attributes can be retrieved as well as being referenced in a query's predicate(s). Informally, the syntax of a basic OOERM query is:

Select set of attributes or methods where predicate.

“Select” is a predefined operation of all entity classes. As an example, consider a query to list the order number and discount amount for all accepted orders that have not been invoiced. The explicit message specification of this query viewed as an operation of the CUSTOMERS class is:

CUSTOMERS.SelectORDERS\_FOR\_CUSTOMER.Order\_Number,

Discount\_Amount(ORDERS\_FOR\_CUSTOMER.Order\_Total) where ORDERS\_FOR\_CUSTOMER in ACCEPTED\_ORDERS and not in INVOICES.

The attributes and methods of the ORDERS class are explicitly qualified by the class reference associating the related ORDERS class entity. By default, unqualified references belong to CUSTOMERS, the class invoking the operation. The class reference ORDERS\_FOR\_CUSTOMER is also used in the where clause to indicate the entity instances being referenced.

This query provides an illustration of arguments that can themselves be messages, a recursive property of messages in OOERM.

Figure 10 graphically depicts the query. In parentheses below the attribute and method properties is an indication of whether the value is “retrieved” (R) (part of the Select clause), “evaluated” (E) (part of the where clause), or both. In the query, entity class membership is evaluated with the predicates “in” and “not in.” The value being returned by the method is indicated as being retrieved (R).

The explicit message specification of the above query viewed as an ORDERS class operation is:

ORDERS.Select Order\_Number,

ORDERING\_CUSTOMER.Discount\_Amount(Order\_Total)

where in ACCEPTED\_ORDERS and not in INVOICES.

The Discount\_Amount method is qualified by the class reference associating the related CUSTOMERS class entity.

As the example illustrates, the class references identify the classes of the attributes and methods referenced in the query, as well as the associations among the classes involved in the query. Thus, the class references in an OOERM query serve the purposes of the “from” clause and “join predicates” in an SQL query.

The necessary associations are normally modeled explicitly in the OOERM scheme. Attribute and method names are normally unique (since “join predicates” are not used per se) in OOERM. Therefore, the class references need not be specified, and the previous query becomes:

Select Order\_Number, Discount\_Amount(Order\_Total)

where in ACCEPTED\_ORDERS and not in INVOICES.

The user can thus replace the longer explicit versions of the query with a shorter implicit specification. This capability is known as logical access path independence (since class references designate a logical access path). The theory underlying implicit query specification is dealt with in [11].

The OOERD representation in Figure 10 can aid the user by providing a diagram of the system's understanding of the query. This can be particularly helpful when the user receives unexpected results from a query, or when the user submits a meaningless or ambiguous query. The latter case occurs when multiple logical access paths exist between the classes involved in the query. In this case, the system can display the parts it understands and the user can be prompted to clarify the remainder.

As an example of a method used in a query predicate, consider the following query, which lists all orders that could be filled from current stock:

Select Item\_Number, Quantity\_On\_Hand, Order\_Number, Order\_Quantity
where not Item\_Rejected (Order\_Quantity)
order by Item\_Number.

Item\_Rejected is a method that returns a Boolean value (see Example 3). Similar to SQL, the "order by" clause sorts the result before its display.

The use of operations in queries allows users to obtain additional useful information while retaining the principle of “information hiding.”

## 5. Comparison to Related Works

IN THIS SECTION WE COMPARE OOERM to two related works with a decade time span between them. Many other related research work occurs in between. The interested reader is encouraged to compare OOERM with the many semantic and object-oriented models that are superbly examined in [13] and [16].

One of the earliest data models that can be considered object-oriented is the functional data model $[17]$ and its accompanying language DAPLEX. In this model, the relationships between objects and their properties, and among objects themselves are represented by functional mapping. A diagramming convention accompanies the model. A box represents an object type. Arrows between boxes represent a function that maps from the object at its tail to the object at its head. A single-headed (double-headed) arrow represents a one-to-one (one-to-many) association.

Although the object-oriented terminology was not used in the functional model, some of its features can be considered object-oriented. Notable features of the functional model include:

(a) the use of nested function reference, and

(b) the use of derived functions to represent methods, allowing application semantics to be encoded in the data description.

The OOERM corresponding features are:

(a) the dot notation for specifying a logical access path, and

(b) method specification through the “operations” component of an object scheme.

These OOERM features are more in line with the modern literature than those of the DAPLEX. In addition, the OOERD and the language of OOERM are more expressive in that they support conditional branching.

A more recent related work is that of [7], where a graphical data manipulation language for an extended conceptual entity-relationship (ECER) model is developed. The ECER diagramming convention is very similar to the OOERD. Both can model generalization and specialization as well as the other features of the ERDs. The ECER, however, is not object-oriented. It does not provide for specification of ADT methods encapsulated within the objects. It is a graphic interface for specifying queries and data manipulation commands only. The OOERM includes general purpose operations as well as data manipulation and query commands.

In summary, OOERM extends the popular ER approach for modeling object structure with a set of simple class operations as well as application-specific ADT operations. OOERDs enable the modeling of object dynamics for all operations: class, ADT, and query. OOERDs provide a graphical abstraction of an underlying OOERM scheme description, encompassing both structural and behavioral characteristics of an application.

## 6. Conclusions

WE HAVE PRESENTED AN OVERVIEW OF THE Object-Oriented Entity-Relationship Model (OOERM). OOERM is a natural extension to the ER approach for modeling the dynamics of entity classes. The ER approach models object statics by defining entities, attributes, and relationships. OOERM extends the modeling capability by capturing the operations that define object behavior and the dynamics of how it changes state.

The natural pairing of the OOP and ER approaches is highlighted by the fact that the object-oriented approach views operations as being entity-type specific. Thus, the operations or methods represent a property of the entity, much like attributes. Further, message passing makes use of established relationships among entities. The relationships determine “object visibility,” i.e., which entities a given entity can access and be accessed by. Class references (ER model role names) are used in sending messages between objects.

The associated Object-Oriented Entity-Relationship Diagram (OOERD) graphically depicts the compatibility of OOP and the ER model. Methods are modeled as properties of entity classes. The dynamics of message passing is shown as occurring among the methods of related entities. The predefined entity class operations are shown as methods superimposed over the classes to which they apply.

Generalization hierarchies are modeled both structurally and dynamically with operations that traverse the hierarchy. These “subclass” operations represent semantically meaningful ways of performing state transitions on objects.

Generally, graphics are considered best for presenting simple descriptions, while structured text is best for detailed descriptions. In line with this philosophy, the OOERD is intended to provide a graphical abstraction of an underlying OOERM scheme description. An OOERD summarizes the entities, attributes, relationships, methods, and message passing used to accomplish an application process. The diagram is a visual means of quickly examining a process, details of which can be found in the OOERM scheme. Thus, OOERDs provide a tool to aid in user verification of design correctness.

We informally presented the OOERM, its data definition, and its data manipulation languages. The model is based on SDM [12], Eiffel [14], and SQL [8]. The following related set of beliefs guides our further research efforts:

1. Object-oriented data modeling has advantages for a broad range of applications, including typical business applications.

2. The associated OOERD modeling techniques are adaptable to other object-oriented data models.

3. The diagrams can be generated automatically from scheme descriptions.

4. OOERD modeling can be beneficially employed in a CASE tool supporting an object-oriented data model.

The ER model has achieved great popularity in modeling data structures. OOERM can fill the need of extending the ER model to capture dynamics, particularly as object-oriented data models and programming styles gain popularity and prominence.

## REFERENCES

1. Batini, C.; Lenzerini, M.; and Navathe, S. A comparative analysis of methodologies for database schema integration. ACM Computing Surveys 18, 4 (December 1986), 323–364.

2. Booch, G. Object-oriented development. IEEE Transactions on Software Engineering SE-12, 2 (February 1986), 211-221.

3. Borgida, A. Features of languages for the development of information systems at the conceptual level. IEEE Software 2, 1 (January 1985), 63–72.

4. Brodie, M. On the development of data models. In On Conceptual Modeling, M. Brodie et al., eds. Berlin: Springer-Verlag, 1984, 19–47.

5. Chen, P. The entity-relationship model—toward a unified view of data. ACM Transactions on Database Systems 1, 1 (March 1976), 9–36.

6. Cox, B. Message/object programming: an evolutionary change in programming technology. IEEE Software 1, 1 (January 1984), 50–61.

7. Czejdo, B.; Elmasri, R.; Rusinkiewicz, M.; and Embley, D. W. A graphical data manipulation language for an extended entity-relationship model. IEEE Computer, 23, 3 (March 1990), 26–36.

8. Date, C. An Introduction to Database Systems, vol. 2, 4th ed. Reading, MA: Addison-Wesley, 1985.

9. DeAntonellis, V., and DiLeva, A. DATAID-1: a database design methodology. Information Systems 10, 2 (February 1985), 181–195.

10. Gorman, K. An Object-Oriented Semantic Data Model. Ph.D. dissertation, Dept. of Business Analysis and Research, Texas A&M University, College Station, TX, 1990.

11. Gorman, K., and Choobineh, J. Logical access path independence using a semantic data model. Submitted for publication.

12. Hammer, M., and McLeod, D. Database description with SDM: a semantic database model. ACM Transactions on Database Systems 6, 3 (September 1981), 351–386.

13. Hull, R., and King, R. Semantic database modeling: survey, applications, and research issues. ACM Computing Surveys, 19, 3 (September 1987), 201–260.

14. Meyer, B. Eiffel: programming for reusability and extendibility. ACM SIGPLAN Notices 22, 2 (February 1987), 85–99.

15. Meyer, B. Reusability: the case for object-oriented design. IEEE Software 4, 2 (March 1987), 50–64.

16. Peckham, J., and Maryanski, F. Semantic data models. ACM Computing Surveys, 20, 3 (September 1988), 153–189.

17. Shipman, D. W. The functional data model and the data language DAPLEX. ACM Transactions on Database Systems, 6, 1 (March 1981), 140–173.

18. Teorey, T.; Yang, D.; and Fry, J. A logical design methodology for relational databases using the extended entity-relationship model. ACM Computing Surveys, 18, 2 (June 1986), 197–222.
