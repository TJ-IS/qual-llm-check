---
otero_id: 23367
otero_key: "JWCCQPVC"
title: "Object-Oriented Application on Data Modelling and Knowledge Representation: A System Integration Approach"
authors: "Daniel T Lee"
year: "1989"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1989.35"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Object-Oriented Application on Data Modelling and Knowledge Representation: A System Integration Approach

Daniel T. Lee, Pan American University

Abstract: Traditional data modelling techniques of DSS and modern knowledge representation methodologies of ES are inconsistent. A new unifying model is needed for integrating the two systems into a unified whole. After a brief review of data modelling techniques and knowledge representation methodologies, the unifying model will be described and integrated systems will be used to exemplify the usefulness of the unifying model.

## Introduction

Decision Support Systems (DSS) have been evolved over two decades (Sprague and Carlson, 1982; Sprague, 1980; Keen and Scott-Morton, 1978; Lee, 1985). They are still in an infant stage. Recently, Expert Systems (ES) have quickly emerged as one of the decision support tools. Tremendous efforts have been made by both computer scientists and management scholars on how to combine both systems into a unified system. The two systems are developed in parallel but on different paths. The DSS has been built through traditional data modelling (DM) techniques while the ES is using knowledge representation (KR) methodologies. The data modelled by the DM techniques are basically static while the knowledge represented with KR methodologies are dynamic in nature. This is largely because the DSS is designed to support decision makers in their decision-making process while the ES is developed to support or to replace human decision makers. Ultimately, the ES will have to be equipped with the same level of knowledge as humans have. As we know, humans are equipped with tremendous ability to conceptualise and possess abstract ideas that are extremely difficult to describe and represent in the computer ready for manipulation. For this reason, the difficulties confronting system integration are compounded.

The integration effort, however, must be pursued because decision makers or end users require an integrated system at their finger tips. The decision makers are largely lay people. They become confused by multiple disintegrated systems. The purpose of this paper is to conduct a comparative analysis of data modelling techniques and knowledge representation methodologies for developing a data model which can be used to integrate DSS and ES into a unified whole (Holsapple et al., 1987; Harmon and King, 1985; Harmon et al., 1988; Goul et al., 1984; Lee, 1988(a); Lee, 1988(b)).

## Technology overlap

Recently, Klein et al. (1988) suggested nine categories of AI/DSS overlap which found many interfaces between ES and DSS; for example, the natural language processing which can be used to enhance dialog management of the DSS, the knowledge representation which is good for data management of the DSS, and the model evaluation and selection ES which is vital for model management. Turban (1988) also pointed out that integration of the DSS and ES is beneficial because ES is usually fit for applying to a narrow subject area while DSS is basically broader in scope. An ES could be used to support several DSS builders on model selection, thus reducing cost through sharing. An integrated system of DSS and ES can answer 'why'? whereas the DSS can only answer 'what if'? The two systems are basically complementary and should be integrated because the effect of an integrated system is larger than that of the sum of the individual technologies. Besides, individual technologies alone are inadequate for effective decision support.

Bonczek et al. (1981) describes the structure of a DSS as containing a language system (LS), a knowledge system (KS), and a problem-processing system (PPS) as shown in Figure 1.

![](/api/attachments/JWCCQPVC/fulltext/images/55da79ced0753f409b29a7feaf4c47ac2ae50760753751e63598652bd7c8fdda.jpg)  
Figure 1. The structure of a decision support system

The situation is very close to the following conceptual and physical interfaces as shown in Table 1.

<table><tr><td>Bonczek</td><td>DSS</td><td>AI/ES</td></tr><tr><td>LS</td><td>Dialog management</td><td>Natural language processor</td></tr><tr><td>KS</td><td>Data management</td><td>Knowledge base</td></tr><tr><td>PPS</td><td>Model management</td><td>Inference engine</td></tr></table>

Table 1. The conceptual and physical integration of DSS/ES

## Data models

Data models are used for defining the basic constructs of data management. As indicated earlier, traditional data models are inadequate for managing both static data and dynamic knowledge. Therefore, the criteria of model selection for discussion must have potential value in both data modelling and knowledge representation. In the following section, four aspects of data modelling capabilities are examined to lay down a practical and theoretical foundation for system integration of data modelling and knowledge representation.

## Database objects

Since our proposed integrated system is object-oriented applications of semantic data, understanding the basic characteristics of an object is vital. According to Kroenke (1988), an object is a named collection of properties that sufficiently describes an entity in the user's work environment. An entity may have an infinite set of characteristics. Obviously, not every characteristic of an entity, needs to be represented in the data base or a knowledge base. An entity is something a user perceives as an independent unit, meaning it can stand on its own. An entity is a class of things that exist in the business world. Entities are perceptions and perceptions may or may not be physical. An entity instance is an occurrence of an entity. An object is a structure that represents an entity. An object instance is a particular object.

An object diagram can help the database or knowledge base developer to summarize the knowledge of an object and to represent it visually and unambiguously as shown in Table 2.

<table><tr><td>Department</td></tr><tr><td>Number</td></tr><tr><td>Name</td></tr><tr><td>Campus-Address (MV)</td></tr><tr><td>Phone</td></tr><tr><td>Chairperson</td></tr><tr><td>Total-Students</td></tr><tr><td>[College]</td></tr><tr><td>[Professor] (MV)</td></tr><tr><td>[Student] (MV)</td></tr></table>

Table 2. Department object diagram

The name of the object is on the top. Inside the box is a list of all the properties of the object. The first six properties are non-object properties. The last three, which are enclosed in brackets, are called object properties. An object property is actually another object. The object diagram describes objects in the user's world and their relationships to one another. Thus, one object can contain other objects. MV stands for multivalued because some properties are allowed to have at most a single value, while others are allowed to have multiple values.

The domain of a property is the set of all possible values the property can have. The description of a non-object property domain is different from that of an object property domain. The domain of a non-object property consists of both a physical and a semantic description. The physical description indicates the type of data. The semantic description describes the function or purpose of the property. It distinguishes this property from other properties that might have the same physical description.

The domain of an object property is a set of object instances. In some cases, the domain of an object property will only be a subset of the object. This is the basis for establishing views of an object. When we identify objects, we need to specify both the properties and the property domains. Typically, the object properties and domain names are listed with the object definition. Domain definitions are separate from object definitions. This helps reduce duplicate domain definitions because one domain may be used by many properties.

Since each application's view may be only a portion of the properties of an object, the system developer must consider the views of all applications in order to completely describe the object. The composite picture of the object is composed of putting together all the views. This final picture is the object diagram.

There are two ways of identifying and describing objects to be represented in the database or knowledge base. One approach is to examine the application outputs-reports and screen displays – and work backwards to derive the object structure indirectly. Another approach is to ask the user what objects he or she wants to keep track of and then to determine which properties need to be stored in the database or knowledge base. The best approach my be the combination of the two.

## There are five basic object types:

(a) Simple objects - contain only single-valued and non-object properties. It can be represented by a single relation with a fixed-length format.

(b) Composite objects - contain one or more non-object multivalued properties. This requires more than one relation for their representation because a relation cannot contain repeating groups. Each relation represents a portion of an object in the application environment. At least one of the relations cannot stand on its own. The key of each child relation contains the key of its parent.

(c) Compound objects - contain at least one object property. It requires at least two relations, one for each object. The relations that represent a compound object stand on their own while in a composite object, at least one of the relations cannot stand on its own. The keys of the relations representing a compound object have no attributes in common because they are totally separate and represent different and independent objects. This is a typical many-to-many relationship; an intersection relation is required. The key of the intersection relation is the combination of the keys of both its parents, and the intersection relation contains no non-key data.

(d) Association objects - are similar to M:N compound objects except it contains non-key data. An association object is an object that documents a relationship between two (or more) other objects. It is also an independent object.

(e) Aggregation objects – represent entity groups. It does not represent instances of an individual or event as the previous four types of objects do. Aggregation objects tell us that the user sees a group as an independent entity. The structure of an aggregation object has a very important property called inheritance. Each lower-level object within the aggregate object inherits properties from the aggregate object(s) to which it belongs. This property is vital for AI/ES applications because it plays a role connecting the traditional data modelling. Object-oriented applications, and advanced knowledge representation methodologies such as frames and semantic networks. Figure 2 shows the relational representation of the aggregation objects.

After defining the objects in the user's application environment, the system developer must materialize the object views by transforming object description into a set of relations, relationships, and constraints. It has to take advantage of software systems such as database management systems or knowledge base management systems for enforcing constraints including domain constraints, intra-relation constraints, and inter-relation constraints. It must be also augmented with other subroutines, attached procedures to enforce constraints not handled by the DBMS or KBMS products.

## Database abstraction

The previous section describes the basic characteristics of an object and its basic application to database systems and knowledge base systems. This section will go up one level to describe the object abstraction for knowledge representation.

Smith and Smith (1989) propose a database abstraction model which describes two types of abstraction that are important in database design and usage: aggregation and generalization. Aggregation is an abstraction which turns a relationship between objects into an aggregate object without bringing to mind all details of the relationship. Generalization is an abstraction which turns a class of objects into a generic object. Codd's (1971) relational schema can simultaneously support both hierarchies of aggregation abstractions and hierarchies of generalization abstractions. It further describes a method for representing a generic hierarchy as a hierarchy of Codd relations. Inheritance can be fully applied to the hierarchies of Codd relations.

## Semantic description

Su (1988) indicates that the existing data models are not rich enough in semantic constructs for a database designer to define the semantic contents of a database. For this reason various semantic data models were proposed (Abiteboul and Hull, 1984; Hammer and McLeod, 1981; Kent, 1979; Kerschberg and Pacheco, 1976; King and McLeod, 1985; McLeod and Smith, 1980; Shipman, 1981). Su (1983; 1986) proposes a Semantic Association Model (SAM). There are two reasons he proposes the SAM instead of using the well-known models such as the database abstraction model (Smith and Smith, 1989), the entity-relationship model (Chen, 1976) the functional model (Shipman, 1981) or the semantic data model (Hammer and McLeod, 1981): (1) SAM contains semantic contracts that capture most of the semantic properties recognized in these popular models; and (2) The statistical aggregation operation of SAM can be used for evaluating database computers and for the analyzing abstract models.

![](/api/attachments/JWCCQPVC/fulltext/images/d95e01c08debba204bf39a19e6dd887a30570ac09d624ddf0333da965d6398aa.jpg)  
Figure 2. Aggregation objects of the university administration database

According to Su, the SAM defines a database with a network of concept/object types which is defined in terms of other concept/object types. Association is used for grouping concepts/objects. There are seven types of associations based on the structural properties, semantic constraints, and operation associated with these concept/object types. These association types are the basic semantic constructs for modelling the complex structural and semantic relationships among the data objects of a database. Figure 3 describes a graphic representation of a network of concept/object types.

This graphical representation represents an improvement over Figure 2, the relational representation of aggregation objects. In this graphical representation, it includes five association types. (1) The membership association type (M) defines a set of atomic concepts/objects. (2) The aggregation association type (A) defines a set of objects by their properties. An occurrence of the A node is a member of the Cartesian product. The word 'aggregation' corresponds to the independent entity type of the entity-relationship model. (3) The interaction association type (I) defines a set of facts that involve some action or interaction between two or more sets of objects. Semantic constraints and referential constraints are enforced by the underlying DBMS. (4) The cross product association type (X) defines a number of categories of objects by taking all the possible combinations of the values of some attributes, called category attributes in the statistical data processing field. An occurrence of an X node represents a category of objects rather than a single object. As a category, it is subject to statistical summarization that is modelled in SAM by a separate association type called summarization association. (5) The summarization association type (S) defines some statistical summaries of a single or a set of concept/object types.

This semantic or conceptual description of the graphical representation of the student database of Figure 3 should exemplify the structural properties, constraints, and operations that can be used to characterize a database. These semantic descriptions should be enforced by the DBMS. Unfortunately, with the present state of art in DBMS technologies, only a portion of them can be enforced by the underlying software such as DDL and DML of the DBMS, most of them still leaves to the application program to shoulder the burden in enforcing them.

![](/api/attachments/JWCCQPVC/fulltext/images/1b56c2a0d4fc32ecd28ed7277be368eb721ca0ca596d086a4c4b24a1ea0de63e.jpg)  
Figure 3. Graphical representation of a student database

## The formal semantic data model

Abiteboul and Hull (1984) declared that they developed a formal semantic database model, IFO. The IFO combines fundamental principles of semantic database modelling in a coherent fashion. Using a graph-based formalism, the IFO provides mechanisms for representing structured objects and functional and ISA relationships between them. In building a cohesive framework, types are used to model object structures; fragments incorporate functional relationships, and ISA relationships are used for inheritance. Five rules are established for enforcing restrictions on ISA relationships. Nested fragments provide natural modules of a schema.

The formal framework of the IFO can be used to investigate the characterization of object types and derived types. The object types can arise in a semantic model that incorporates aggregation, grouping, and generalization.

The derived types can have a natural free structure.

The framework can also be used to characterize the impact of a single update request in the context of the complex, interrelated relationships found in semantic database schemas.

The IFO model was devised to synthesize the concepts of prominent semantic models on semantic object types and object structuring. Two uniques of the IFO model are utilized in SNAP: the use of fragments as the building blocks of schemas, and the use of distinct vertices to serve as function ranges. The IFO model focuses on structures; data manipulation language and integrity constraints are largely ignored, but they can be added into the model in a natural and straightforward manner.

## Knowledge representation methodologies

Any computer program contains knowledge on how to employ the decision procedures in a particular set of circumstances. However, the knowledge stored in the conventional computer program is not represented explicitly and cannot be readily expanded or manipulated. The knowledge must be described and represented in such a way that it can be used to draw new conclusions by formally manipulating these descriptions. General knowledge about how knowledge is acquired, represented, and used has to be embodied in flexible systems which can be extended and the conclusions drawn can be explained. A knowledge representation language is vital for the domains of knowledge which can be described.

Currently, there are many knowledge representation (KR) methodologies proposed such as propositional calculus, predicate calculus, production rules, frames, and semantic networks. Most of the exiting ES are constructed with production rules because they are relatively simple and easy to implement. Unfortunately, some types of knowledge can not be represented as rules. The abstract concepts and aggregation objects require sophisticated KR methodologies such as fræs or semantic network.

The predicate calculus uses objects as the basic unit in a predicate logic. Statements about objects are termed predicates. The assertions the logic are either true or false. It is very difficult to express 'what is the condition of a situation?' Connectors can be used in a predicate logic for addressing more than one object. Compound expressions can be created and predicates may also be nested. Since objects are the basic units, object-oriented data modelling techniques discussed in the previous sections can be combined for unified application. Another weakness of the predicate calculus is that it is difficult to graphically express its data structure. Conceptual expression, aggregation, abstraction, and summarization abstraction are hard to describe. Inheritance is almost impossible in this KR method which is so vital for space saving in complex systems.

Production rules are popular in production systems. The basic form of production rules is basically a condition-action pair. Rules link the values with attributes of objects. The objects can be variables which allow the system to substitute for different facts. When a rule is invoked, the system checks to see if the O-A-V values in each condition clause are true. Integrity procedures and uncertainty factors can be attached to the facts and relationships. Since the basic units are also objects, object-oriented data modelling techniques can also be used in this KR method. As indicated earlier, the weakness of this method is that not all types of knowledge can be represented as rules.

The semantic network consists of nodes and links. The nodes store objects and descriptors. Objects can be physical or conceptual entities. Links are used to relate objects and descriptors. A link may represent any type of relationship. Common links are ISA and HSA. The ISA links are often used to represent class-occurrence relationships. The HAS links are used to represent part-subpart relationships and to identify nodes that are properties of some other node. New nodes and links can be added as needed. Inheritance is the one of the major strengths of this KR method. Property inheritance is one of the implications of the ISA relationship.

Nodes can be classified into three categories: objects, attributes, and values. Objects are ordered and related through trees and networks. The weakness of this KR method is that it is difficult to handle exceptions. When exceptions arise, procedures have to be developed. Integrity rules are not easy to enforce. Complicated networks can easily fall into tangled webs. Since the basic units in the network are also objects, the object-oriented data modelling techniques can also be easily integrated with this KR method.

Frames contains slots which store description about objects. Slots may also store attribute values, pointers, rules, or procedures. The slots can be nested. Therefore, frames can be viewed as a special case of semantic network. It is a complex KR method and more difficult to develop than other KR methods. Since the basic units of the whole constructs are also using objects, object-oriented data modelling techniques can also be combined for system integration development (Luger and Stubblefield, 1989; Tanimoto, 1987; Harmon and King, 1985; Tsichritzis, 1985).

## System integration

## Object-oriented applications

Object-oriented applications are receiving wide attention in many application areas such as database design, office automation, programming languages, and artificial intelligence/expert systems. Object-oriented systems have their roots in programming languages such as Smalltalk. Based on the discussions in the previous sections, the fundamental characteristics of an object-oriented application should include abstraction and generation of data, property inheritance, structural hierarchy, consistency of interaction, and encapsulation of data and operation.

Object-oriented systems employ objects as unifying constructs which model data and activities. Communications and actions can be triggered by message passing. Knowledge is distributed among entities which are materialized through objects. Therefore, objects are pillar stones in any integrated system development.

Banerjee et al. (1987) established an object-oriented data model extracted from a brief review of the basic object-oriented concepts of existing object-oriented systems. The basic concepts involving object-oriented systems consist of objects, classes, class lattice, methods, and inheritance. Then they developed three enhancements to the conventional object-oriented data model: the schema evolution, a composite object, and the version control. Concerning the schema evolution, they made a wide variety of changes to the existing database schema including class definition and the structure of the class lattice without requiring a database reorganization. The composite object is a collection of objects that encapsulate the relationships between objects including clustering of objects, semantics of composite objects, and integration of the overall constructs into a unified object-oriented data model in terms of schema definition. The version control discusses the semantics of versions and showed how they are integrated into the object-oriented data model.

All these basic concepts and enhancements are finally being incorporated into a prototype object-oriented database system named ORION which is being implemented in the database program at MCC as a research vehicle for object-oriented applications. The system is intended to support knowledge base system using Common LISP. The application interface to ORION then is an object-oriented extension to LISP, much as Object LISP (LMI, Inc., 1985) including all basic concepts of object-oriented systems such as message passing control, class lattice, and property inheritance along the class lattice. The ORION message-passing protocols are integrated with LISP function calls. Therefore, ORION application can view both ORION objects and LISP structures without having to move from one programming environment to another. This is one of the typical applications of object-oriented concepts.

As indicated earlier, rule-based systems are popular and widely used because they are easier to implement, not because they are the best. Many types of knowledge can not be represented with production rules. Frame-based systems have a great potential in developing large and advanced management decision-making systems because frame-based systems can be built on object-oriented concepts.

Smalltalk is a very versatile tool based on object-oriented concepts and was developed at Xerox's Palo Alto Research Center. The Smalltalk language is based on a hierarchical collection of objects. Each subclass of object inherits properties from its superclass ancestors. Each object has its own private variables, and many also share variables with other objects. The objects respond to messages from other objects by executing methods or procedures attached with the messages or objects.

A micro version of Smalltalk from Digitalk called Smalltalk/V is now available. It is also object-oriented and makes use of both rules and objects (or frames). Frames or objects are useful for organizing rules within large systems. Knowledge-based system rules are easily growing out of control. They need to be organized into small modules. Frame-based systems provide a natural means of grouping rules together into a class. This frame or object structure provides a basis for object-oriented programming. Frames can be manipulated singly or as a group. Therefore, Smalltalk/V is an excellent tool for prototyping small system development. It is also a tool with which to explore object-oriented programming (Mockler, 1989).

Another prototype named Observer has been implemented and linked with a programming environment named GARDEN (Hornick and Zdonik, 1987). GARDEN treats everything as an object, not only views the static program modules, statements, and variables as objects, but also the dynamic structures such as frames as objects. Future versions of GARDEN will make use of the ENCORE database system to take advantage of some of the more advanced features, such as version control. Hornick and Zdonik (1987) describe the basic data model of an object-oriented database and the basic architecture of the system implemented in accordance with the object-oriented concepts. In the ENCORE database system (Zdonik and Wegner, 1986), all objects are instances of some type that describes the behaviour of its instances. Types can be related to each other by means of a special property called ISA. The ISA property induces an inheritance relationship between types. Operations are active objects that are supported by code. Operation types correspond to a procedure definition, whereas instances of operation types correspond to procedure activations. Operations are associated with a type. Each type defines a set of operation types that can be instantiated and invoked on its instances. The concepts described above make up the kernel of the object-oriented database model.

## Distributed applications

Distributed AI systems (DAIS) are emerging as one of hot topics for discussion in the AI area. The basic concepts of the DAIS are that the DAIS tries to facilitate the simultaneous interaction of several intelligent agents working together in multiple locations. The intelligent agents share knowledge located in a distributed fashion and coordinate efforts for problem solving. Multiple Intelligence Node Document Services (MINDS) (Bonnel et al., 1984) is a distributed collection of knowledge-based systems for managing and retrieving documents in an office environment of networked workstations. The systems share knowledge and tasks and cooperate in problem-solving. According to Huhns et al., (Smith and Smith, 1989) MINDS is designed mainly for document management and query processing. Actually, its knowledge represented in each knowledge-based system should also be object-oriented in accordance with the theory and techniques of data modelling, knowledge representation, and object-oriented system application.

DODM (Distributed Object-Oriented Database Model) (Lyngback and McLeod, 1984) is a distributed version of ODM (Object-Oriented Database Model). It supports object sharing among individual workstations, imposes access control, and allows relationships to be established among objects in different databases. DODM provides location transparency and models the office environment as a logical network of workstations. Each workstation has a unique name and a directory of network databases. The convention is adopted to allow all resource sharing to be defined at the same level. For performance purpose, several workstations may be grouped together at the same physical node of a computer network. The network does not have to implement the same database model. They are only required to be identical from a network point of view. In other words, they must all provide the same network interface. Thus, the existing databases and computer information systems may be part of the network.

A DODM database is modelled as a collection of objects. Objects correspond to conceptual or physical entities which include audio, behavioural, image, and text objects. They may be structured or unstructured, formatted or unformatted. Abstract objects are used to model concepts that can naturally be represented in a database by a single identifier. They must be related to the abstract object via appropriate mappings. Objects and relationships are the basic concepts for information modelling. Each object in the database corresponds to a relation. The database can be represented as a directed graph in which the nodes are boxes labelled with object identifiers of the corresponding domain and range objects, and the edges are directed from domain objects to range objects and labelled with the object identifiers of the corresponding map objects.

From the above discussion, the object-oriented modelling techniques not only can be applied to the traditional data models, but also can be applied to the knowledge representation of knowledge-based systems as well as in a distributed environment. It is evident from a theoretical point of view that the object-oriented modelling techniques can be applied successfully to almost any type of information systems, either static data systems or dynamic knowledge systems. From a practical or physical point of view, it may still have some hurdles we have to overcome. Programming languages and language processors are urgently required for describing, representing, and processing the semantics of the objects corresponding to underlying entities and relationships. Currently, some progress has been made in the software and hardware to accommodate the new object types, especially on describing, representing, and processing abstract and unstructured data and knowledge.

NIKL (New Implementation of KLone) (Brachman, 1978) is a knowledge representation language. KIT (Knowledge-based Interaction Tools) is an approach used for interface construction. TINE (The Intelligent Noter of Expectations) is a knowledge acquisition tool. These three constructs represent a new generation of software tools for knowledge-based system development. They are a cross between semantic nets and frame-based knowledge representation mechanisms. Tremendous efforts and research are needed in the development of knowledge-based system construction tools (Neches, 1988).

## A unifying model

Based on the above discussion, we may conclude that a unifying model can be built with objects as the building blocks. The object can be used for representing concrete concepts or abstract ideas. As discussed earlier, objects are used to materialize the underlying entities which can be almost anything: basic data, aggregation abstraction, or generalization abstraction. According to the entity-relationship model, almost any system could be constructed with entities (objects) and relationships. The relationship is basically another form of entity. Following the basics of the database objects and the formal semantic data model, a unifying model can be built with object-oriented applications. The theory is sound and the mechanism is almost complete. The only thing left for us to do is to build the software and hardware systems which can be used to describe and represent data and knowledge in accordance with the convention of the unifying model and finally to operate the system for producing the information for decision-making.

## Integrated systems

Currently, there are several integrated systems such as Iris, DBMS, KNOs, and OBE. The Iris (Fishman et al., 1987) is a research prototype for next-generation DBMS intended to meet the needs of information requirements of office automation systems and knowledge-based systems. The Iris DBMS consists of a query processor that implements the Iris object-oriented data model, and a relational storage subsystem (RSS). The RSS is acutely a storage manager that performs access path control, concurrently control, backup, and recovery. The data model supports high-level structural abstractions, such as classification, generalization, aggregation, and behavioural abstraction. The Iris has also a collection of interactive interfaces which include an object-oriented extension to SQL.

KNOs (Knowledge acquisition, dissemination, and manipulation Objections) (Tsichritzis et al., 1987) supports migration of its objects and operations to new environments. Its objects have the ability to acquire new operations dynamically. KNOs objects can learn by interface with other objectors or systems. Hybrid (Hierstrasz, 1985) is an object-oriented programming language under development. It attempts to unify a number of object-oriented concepts including KNOs. The basic concepts of KNOs and Hybrid are: data abstraction, multiple inheritance, aggregation, dynamic object binding, active objects, message passing, and distributed environments. The Zetalisp implementation of a KNO application provides a test for the integrated system concept.

## Summary

So far we have intensively investigated the traditional data modelling techniques with special emphasis on modelling the semantic description of objects. We have also carefully examined the knowledge representation methodologies with emphasis on how they can be integrated with the traditional data modelling techniques. The conclusion can be drawn that they can be integrated with object-oriented modelling mechanisms. A unifying model has been identified with rich capabilities and this new unifying model can be used for integrating both the traditional data models of DSS and the knowledge representation of ES into a unified whole.

This new unifying model can be also applied to distributed applications. A number of integrated systems under this unified modelling concept have been exemplified to give us confidence on the soundness of the unifying model. The only thing that remains for us to pursue is the development of programming languages which can be used to represent the description of objects in the computer, either concrete objects or abstract ideas, and the development of language processors which can be used to operate new databases or knowledge-based systems.

## References

Abiteboul, S. and Hull, R. (1984) IFO: A Formal Semantic Database Model. ACM, New York.

Banerjee, Jay, Chou, H.T., Garza, J.F., Kim, W., Woelk, D., Ballou, N. and Kim, H.J. (1987) Data model issues for object-oriented applications. ACM TOOIS, 5 (1) Jan.

Bonczek, Robert H., Holsapple, Clyde W. and Whiston, A.B. (1981) Foundations of Decision Support Systems. Academic Press, Inc.

Bonnel, R.D., Huhns, M.N., Stephens, L.M. and Mukhopadhyay, U. (1984) MINDS: Multiple Intelligent Node Document Servers. Proceedings IEEE 1st Int'l Conference on Office Automation, Dec.

Brachman, R. (1978) Structural Paradigm for Representing Knowledge. Bolt Beranek and Newman, Inc., Cambridge, Mass.

Chen, P.P.S. (1976) The entity-relationship model – toward a unified view of data. ACM Transaction on Database Systems 6 (1) March.

Codd, E.F. (1971) Further normalization of the database relational model. In Courant Computer Science Symposium 6: Data Base Systems. Prentice-Hall, Englewood Cliffs, N.J., May.

Fishman, D.H., Beech, D., Cate, H.P., Chow, E.C., Connors, R., Davis, J.W., Derrtt, N., Hoch, C.G., Kent, W., Lyngback, P., Mahbod, B., Neimat, M.A., Ryan, T.A and Shan, M.C. (1987) Iris: an object-oriented database management system. ACM TOOIS 5 (1) Jan.

Goul, M., Shane, B. and Tomge, F. (1984) 'Designing the expert component of a decision support system'. Paper delivered at the ORSA/TIMS National Meeting, San Francisco, May.

Hammer, M. and McLeod, D. (1981) Database description with SDM: a semantic database model. ACM Trans. Database Syst. 6 (3).

Harmon, Paul and King, David (1985) Expert Systems: Artificial Intelligence in Business. John Wiley & Sons.

Harmon, P., Mans, R. and Morrisey, W. (1988) Expert Systems: Tools and Applications. John Wiley and Sons.

Hierstrasz, O.M. (1985) HYBRID: A unified object-oriented system. IEEE Database Engineering (Dec.).

Holsapple, Clyde W., Tam, K.Y. and Whinston, A.B. (1987) Expert system integration. In B.G. Silverman (ed.) Expert Systems for Business, Addison-Wesley.

Holsapple, Clyde W. and Whinston, Andrew B. (1987) Business Expert Systems. Richard D. Irwin.

Hornick, Mark F. and Zdonik, Stanley B. (1987) A shared, segmented memory system for an object-oriented database. TOOIS 5 (1) Jan.

Huhns, Michael, ed. (1987) Distributed Artificial Intelligence. Morgan Kaufmann Publishers, Inc.

Keen, P.G.W. and Scott-Morton, M.S. (1978) Decision Support Systems, An Organizational Perspective. Reading, Mass., Addison-Wesley.

Kent, W. (1979) Limitations of record-based information models ACM Trans. Database Syst, 4 (1).

Kerschberg, L. and Pacheco, J.E.S. (1976) A Functional Data Base Model. Pontificia Univ. Catolica de Rio de Janeiro, Rio de Janeiro, Brazil, Feb.

King, R. and McLeod, D. (1985) Semantic database models. In J.B. Yao (ed.) Design. Springer Verlag, New York.

Klein, G., Yun, D.Y.Y. and Liu, J.I.C. (1988) Artificial Intelligence in the Architecture of Decision Support Systems. Conference on the Impact of Artificial Intelligence on Business and Industry.

Kroenke, Donald A. (1988) Database Processing (3rd Edn). Science Research Associates.

Lee, Daniel R. (1985) Integrated systems for transactional processing and decision support. International Journal on Policy and Information 9 (2).

Lee, Daniel T. (1988a) Expert decision support systems for decision-making. Journal of Information Technology, 3 (2).

Lee, Daniel T. (1988b) Comparative analysis of object-oriented system integration for decision-making. International Journal on Policy and Information 12 (2) Dec.

LMI, Inc. (1985) ObjectLISP User manual. LMI, Cambridge, Mass.

Luger, G.F. and Stubblefield, W.A. (1989) Artificial Intelligence and Design of Expert Systems. Benjamin/Commings Publishing Co.

Lyngback, P. and McLeod, D. (1984) Objected management in distributed information systems. ACM TOOIS 2 (2) April.

McLeod, D. and Smith, J.M. (1980) Abstraction in databases. In Workshop on Data Abstraction, Databases, and Conceptual Modelling (Pingree Park, Col.)

Mockler, R.J. (1989) Knowledge-Based Systems for Strategic Planning. Prentice-Hall.

Malpas, J. (1988) PROLOG: A Relational Language and Its Applications. Prentice-Hall.

Neches, R. (1988) Knowledge-based tools to promote shared goals and terminology between interface designers. ACM Transactions of Office Information Systems 6 (3) July.

Ringland, G.A. and Duce, D.A. (1988) Approaches to Knowledge Representation. John Wiley & Sons, Inc.

Shipman, D. (1981) The functional data model and the data language ADAPLEX. ACM Trans. Database Ssyst. 6 (1).

Smith, J.M. and Smith, D.C.p. (1989) Database Abstraction: Aggregation and Generalization. Readings in Artificial Intelligence and Databases, Morgan Kaufman Publishing, Inc.

Sprague, R.H., Jr. (1980) A Framework for the Development of Decision Support Systems. MIS Quarterly Dec.

Sprague, R.H. Jr. and Carlson, E.D. (1982) Building Effective Decision Support Systems. Englewood Cliffs, N.J., Prentice-Hall.

Su, S.Y.W. (1983) SAM\*: A semantic associate model for corporate and scientific statistical databases. Journal of Information Sciences 29.

Su, S.Y.W. (1986) Modelling integrated manufacturing data using a semantic association model (SAM\*). IEEE Computers 9 (1) Jan.

Su, Stanley Y.W. (1988) Database Computers. McGraw-Hill.

Tanimoto, Steve L. (1987) The Element of Artificial Intelligence. Computer Science Press.

Tsichritzis, D.C. (1985) Objectworld. In D.C. Tsichritzis (ed.) Office Automation: Concepts and Tools. Springer-Verlag, Heidelberg, pp. 379–98.

Tsichritzis, D., Fiume, E., Gibbs, S. and Nierstrosz, O. (1987) KNOS: knowledge acquisition, dissemination, and manipulation objects. ACM TOOIS 5 (1) Jan.

Turban, E. (1988) Decision Support and Expert Systems. Macmillan Publishing Company.

Zdonik, S.B. and Wegner, P. (1986) Language and methodology for object-oriented database environments. In Proceedings of the Nineteenth Annual Hawaii International Conference on System Sciences (Honolulu) Jan.

## Biographical notes

Dr Daniel Lee is Professor in the School of Business Administration, and Director of MIS Program Development at the University of Texas-Pan American, USA. He has extensively researched expert decision-support systems, intelligent decision systems and object-oriented application of data modelling and knowledge representation. He has contributed many papers on these subjects to conferences and academic journals.

Address for correspondence: Professor Daniel Lee, School of Business Administration, MIS Program Development, Office of the Director, University of Texas-Pan American, 1201 West University Drive, Edinburgh TX 78539, Texas USA, Tel. 512-381-3367.
