---
otero_id: 18735
otero_key: "23B6QXR5"
title: "Object-oriented databases and their impact on future business database applications"
authors: "Timothy J. Heintz"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90047-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Applications

# Object-oriented databases and their impact on future business database applications \*

Timothy J. Heintz

Department of Management, Marquette University, Milwaukee, WI 53233, USA

The relational data model cannot handle the increasingly complex data management requirements imposed by many of today's applications. The object-oriented database concept provides greater capabilities through the support of user defined abstract data types, complex data objects that may contain other objects, procedural attachment to attributes, inheritance, and a more flexible means of deriving values and representing constraints. Existing object-oriented development projects, besides developing systems from scratch, are extending relational systems to include user defined data types or expanding object-oriented languages to allow storage of complex objects on mass storage devices. They are, however, still evolving. An application involving product configuration and sales quotation generation is presented. It illustrates the advantages of using the object-oriented approach.

Keywords: Object-Oriented, Databases, Data Base Management Systems, Systems Design, Configuration, Sales Proposals, Intelligent Systems.

![](/api/attachments/23B6QXR5/fulltext/images/6981844448a106a822b7071a2ef0d7c58eca6b89af0ac29f6e52a81e79ba748b.jpg)

Timothy J. Heintz is an Associate Professor of Management at Marquette University. He received his DBA from Indiana University in Quantitative Business Analysis with a minor area in MIS. Since joining the Marquette Faculty in 1972, he helped develop their Information Systems program and served as Department Chairman for five years. He has been active as a researcher in applications of computing and simulation. In 1986, during a Sabbatical leave at Johnson Controls,

Inc., he became involved in the use of Artificial Intelligence techniques. He has recently focused on object-oriented systems design issues and on the design and use of systems to support group decision making. He has authored papers appearing in the Transportation Research Record, The Journal for Experiential Learning and Simulation, The Canadian Journal of operations Research, The Journal Systems Management and others. \* The work reported in this paper was supported in part by a

## 1. Introduction

Database Management Systems, which today are largely based on the relational data model, provide a valuable tool for the development of many business data processing applications. However, both computer and application technologies are rapidly changing. Large scale integration has produced very affordable computer chips that give us considerable processing power. Low cost primary and secondary storage and a variety of high quality but inexpensive peripheral devices is fostering the growth of new applications involving the use of complex graphics and the handling of voice and video. Applications often require the use of textual data and mathematical models. This changing environment creates a need to design systems capable of managing more than traditional record oriented data files.

Within the realm of traditional data processing, interest exists in developing intelligent front ends for databases. Such systems infer, from either a natural language statement or from a user-computer dialogue, the specific database query needed to extract the desired information. To accomplish this objective, we need software constructs that enable queries to be processed within the context of a particular situation. The relational model does not provide any explicit ways of accomplishing this task.

A current data base design consideration has been the capturing of the true meaning of data when modeling information in database applications. This concept of “data semantics” helps designers develop databases with proper structure and integrity controls, and it is also useful in designing intelligent front ends for databases. An excellent review of work in data semantics has been provided by Hull and King (1987).

Recently, discussion has appeared in the literature (Dittrich and Dayal, 1986) on the topic of object-oriented databases (OODB). The object-oriented approach represents data in forms other than single valued numbers or strings that are restricted by finite sets of well defined types. They also allow objects to be contained within other objects and support the definition of objects as specializations of other objects. This latter capability provides a richer schema definition methodology.

Data semantic issues are better handled with object-oriented approaches. Since these system allow for the management of varying types of data and because processing logic (behavioral descriptions) is placed within the database itself, complex applications are more easily developed. Also, a greater degree of program-data independence is realized. As a result, OODB systems can help both users and developers manage increasingly complex databases.

This increased capability does not come without costs. Application development and transaction processing can be more difficult. The well developed methodologies established for the relational model may be inadequate for applications implemented within an object-oriented system.

## 2. Alternative Approaches to Databases

The relational model views a database as a set of tables, each with a fixed number of single valued attributes (columns). Record occurrences are represented as rows of the table (tuples). Each table or relation must have a key attribute or a set of attributes that uniquely identifies each tuple. Relationships between tables are established through cross-reference key attributes that link them together.

An OODB is described in terms of “objects” which are roughly equivalent to the relational “relations.” A “class” definition describes an object. Actual data records are “instances” of the class describing the object.

Table 1 contrasts the major differences between the relational and object-oriented approaches. A significant enhancement provided by the object-oriented model is in its added data typing. Within relational implementations, attributes must be strongly typed. This involves assigning attributes such data types as integer, floating point (double and single precision), string, boolean, and date. A predefined set of operators, such as the arithmetic ones for integer and floating point and relational ones for boolean, exist for each data type.

Object-oriented implementations usually allow for the database designer to define additional data types and operators on them. These “abstract data types” may be described in terms of a number of attributes of their own. For instance, we may wish to define a “time” data type as containing hour, day, month, and year. Two different time subtraction operators could then possibly be defined; one computes the time difference in hours and another in days.

A concept closely related to the “abstract data type" is the "complex data object." Within an OODB an attribute can refer to another object. For example, consider an order processing application. An object represents a line item in a customer order. An attribute within the line item indicates the product ordered. Within the relational model, this attribute would contain a value of a product relation key identifier, thus providing a cross reference from the order item to the product data. Within an object-oriented model, the same attribute would contain a reference to the product object itself. Thus we have an object that contains an instance of another object.

Table 1  
Comparison of relational versus object-oriented database concepts

<table><tr><td>Concept</td><td>Relational Implementation</td><td>Object-Oriented Implementation</td></tr><tr><td>Data Types</td><td>Fixed number of predefined data types and operators.</td><td>User defined “Abstract Data Types” and operators.</td></tr><tr><td>Attribute Contents</td><td>Single valued, printable data fields.</td><td>“Complex Data Objects” that can contain other objects.</td></tr><tr><td>Constraints or Derived Values</td><td>Some allow specification within schema for single relation.</td><td>Constraints can be an object type; message passing allows for attribute value computations across objects.</td></tr><tr><td>Procedural Attachment</td><td>Program logic separate from data base.</td><td>Procedures or functions can be assigned to attributes.</td></tr><tr><td>Inheritance</td><td>No explicit mechanism; specialized entities must be separately defined.</td><td>Class/Subclass definition allow inheritance of superclass attribute definitions.</td></tr><tr><td>Object Sharing</td><td>Relations are associated by identifier; updates to identifier must be made across all relations</td><td>Two objects can share a common object.</td></tr></table>

Indeed, if the attribute is restricted to contain only instances of a specific class of objects, we have declared that attribute to be of a type associated with the object class. In the example, by restricting the order item's product attribute to contain only instances of product, we are in effect saying that this attribute must be of type "product." We can now define operators for the abstract data type product. These operators might return or change values for product attributes, such as description, price, and amount on hand.

Another way that an OODB differs is in the representation of both behavioral and structural information. Some relational implementations support the definition of derived attributes that are computed from other attributes within the relation. This is a type of behavioral specification, but object-oriented implementations typically provide considerably more capability.

Many OODB systems allow procedures or what is called “methods” to be attached to attributes. This allows attribute values to be derived through complex logical operations that may involve branching and/or looping. Furthermore, since an object can refer to another object, a method defined in one object can perform an operation on that other object. This “message passing” concept can only be handled within a relational systems by writing externally defined programs.

Data integrity checking is an important function. Most relational implementations do allow certain types of integrity checks to be defined within the schema. These typically include attribute type and domain checks and some enforcement of relational constraints (e.g., attribute A must be greater than or equal to attribute B). Object-oriented implementations can provide integrity checking through procedural attachment to attributes. Some systems also allow the explicit definition of constraints on both individual instances or object classes.

The concept of objects being either specializations and generalizations of other objects is discussed in the semantic modeling literature, but not explicitly implemented with the relational model. In object-oriented systems, a “subclass” can be defined of the same type of its superclass, but containing additional attributes or operators. These additions describe a specialized structure and behavior for the objects belonging to the subclass. For instance, a savings account would be a specialization of a bank account, containing at least one additional attribute for storing or computing the amount of interest on the account. Nearly all OODB systems have a mechanism for defining class-subclass hierarchies.

The relational model provides more formalized methods for processing transactions (queries or updates) against the database. Relational algebra enables a user to extract selected attributes and tuples within a single relation and relational calculus facilitates the manipulation of two or more relations that have been defined for the relational model. Within an OODB, operations or methods can be defined to perform updates or queries using a message passing concept. However, a need still exists for developing standardized protocols for processing OODB's.

Many relational concepts apply to objects, but some do not. The relational join operation requires that two objects contain a matching identifier. This would be created by having an object possess an attribute containing the other object. Within object-oriented systems, a single instance of an object may actually be shared by many objects. Thus if any attribute associated with the referenced object is changed, this change is automatically propagated to all other objects that refer it.

This concept of shared objects insures the maintenance of “referential transparency.” Within the relational model, changes typically would not be allowed to the tuple’s primary key or identifier. However, within objects, references are made to other objects themselves rather than to their identifiers. An attribute that would be considered the object’s identifier can consequently be modified without any problems. To implement this type of update in a relational model, a search for and change of all relations containing the identifier would have to be performed.

In general, the relational model produces an effective and very simple means of maintaining a database, but the object-oriented model provides better representation of complex data domains. OODB concepts have been applied to CAD/CAM applications where graphical support, complex product structures and constraints necessitate the use of a sophisticated system. However, many business applications require the processing of documents, graphic images, mathematical models, and perhaps even representations of voice and video data. The relational model has limited capability to handle these.

Thus, although the OODB model provides very powerful data representation techniques, the current state of the art lacks the formalized design approach and generalizable query and update capability of the relational model. This fact, along with the inherit complexities associated with a large number of different data types and many levels of object references, may limit the initial acceptability and use of OODB's.

## 3. Existing object-oriented data base systems

Three strategies have been used in developing OODB systems; designing from scratch, extending existing relational systems by adding object handling capabilities, and extending existing object-oriented languages so that they can manage large amounts of data stored in secondary storage.

OODB software development projects typically address two major design tasks; (1) creating the logical front-end for the design and use of a database and (2) developing the physical implementation scheme on the back-end. The front-end includes both a user-oriented query language and the schema definition process. With the back-end, designers must address the physical storage of data, indexing, concurrency control, and backup and recovery.

Thus, in reviewing existing database projects, we will consider the development strategy and type of design tasks addressed by the project. In addition, we will identify what capabilities are or are not implemented in the various projects.

The Cactis System (Hudson and King, 1986 and 1988) represents an effort to develop an

OODB system from scratch. It focuses on deriving values from both attributes within the object itself and those in other objects. To access information external to an object, relationships have to be explicitly defined. Cactis does not support abstract data typing except by one object referencing another through a relationship link. Its schema definition supports the specification of constraints and class/subclass hierarchies. The Cactis project's major goal is to develop an efficient means of propagating attribute computations through a potential network of relationships. Included here is a capability to undo (rollback and recover) the effect of a change, providing a type of "what if" capability.

VBASE (Andrews and Harris, 1987) has recently become commercially available. It is built upon a schema definition language concept in which objects are defined as data types that have attributes or “properties”, each of which is declared as being of a specific type. In addition, objects can have operations defined for them, written in VBASE’s C-type language called COP. These types can be arranged within a class/subclass hierarchy. At present, VBASE has limited high-level query language capability.

Some projects have extended existing database systems by adding object-oriented functionality. The POSTGRES system (Stonebraker et al, 1987 and 1988) allows the database designer to define specialized data types and operators for manipulating them. It also provides a way for attributes to be linked to a procedure. A query language for POSTGRES called POSTQUEL is implemented much like traditional relational query languages, but able to access the newly defined procedures and operators. POSTGRES, however, does not provide true object functionality. The heavy reliance on the relational model, has simplified the design and use of the system. This has been at the expense of not implementing a truly object-oriented system. For instance, the abstract data types defined for POSTGRES objects cannot contain other objects or share common objects.

Two other extensible DBMS projects, GENESIS (Batery et al, 1988) and EXODUS (Carey et al, 1986) do not attempt to produce a complete DBMS, but provide software modules to manage the storage and accessing of abstract data types. By providing a library of types and corresponding operators, they allow for the customization of a

DBMS for a particular application. Within the EXODUS system, a software “toolkit” is provided. It includes tools for defining new data types, for handling storage, record locking, and recovery functions, and for developing database queries and user front-ends.

The PROBE (Dayal and Smith, 1986) system extends a functional data modeling concept. It is a refinement of a query language called DAPLEX (Shipman, 1981), which, although described in terms of entities and functions, has much of the same functionality as can be found in an object-oriented systems. This includes implementation of a class/subclass hierarchy and referential transparency of entities. Continuing work on the PROBE system focuses on developing a data modeling approach for implementing a query algebra that can be used in designing user front-ends.

Work on extending existing languages has produced GEMSTONE (Maier et al, 1986, Purdy et al, 1987). This may be the most complete of the commercially available OODB systems. GEMSTONE is based upon the Smalltalk language (Goldberg and Robson, 1983), and extends the Smalltalk language by permanently storing objects maintained by the language. A Smalltalk-like language called OPAL provides the logical front-end. Since capabilities such as abstract data typing, creation of complex objects, and object sharing are inherent in the Smalltalk language, GEMSTONE is a full implementation of an OODB.

Another object-oriented programming language, Trellis-Owl, has been developed by Digital Equipment. As with GEMSTONE, this language has been extended into a database system (O'Brien et al, 1986).

## 4. An Object-Oriented Database Application

The emergence of object-oriented DBMS's raises the question of the utility of using them in solving business problems. This approach provides additional functionality and greater flexibility in developing databases, but can this capability be applied to real applications? What is the value added of this approach?

To address these issues, a problem is considered in which a database was used to generate sales proposals for plastic blowmolding extruder machines. These machines are used to produce plastic bottles.

The main objective of this configuration problem is to select an extruder unit with a motor, an arrangement of extrusion heads, and clamp that holds these heads in place. This configuration should be able to produce a specific bottle at a given production volume. It should also maximize the utilization of the extruder and motor while minimizing costs.

As part of this process, a customer sales proposal is prepared. This proposal contains the recommended configuration, pricing and some standard sales presentation text. The configuration is composed of a machine, a clamp that holds an arrangement of bottle molds, and a motor to drive the extruder. Alternative head (mold) arrangements vary with the type of bottle and the number of bottles produced per production cycle. The combination of machine and motor determines the cycletime. Constraints limited the valid combinations of machine, motor, clamps, and head arrangements.

The solution process is similar to the R1 system (currently called XCON) used by Digital Equipment Corporation to configure VAX computer systems (McDermott, 1982). XCON uses a production (rule) system to edit and develop configuration specification for incoming customer orders. However, the extruder configuration system differs from XCON in a couple of ways. Instead of just editing and configuring a customer order, it uses a customer's bottle specifications and production requirements to generate a specific recommendation. It also produces a finished quotation that can be edited by a word processor and sent directly to the customer.

The extruder configuration system, which has been called GENIE, was developed by the author with the assistance of Dr. Kasim Sinnamoheedin and the support of Johnson Controls, Inc. The initial prototype uses a microcomputer-based relational DBMS. The knowledge on how the components can be combined and what valid options can be included within the configured system are represented as rules within a backward chaining expert systems shell language. The textual data for the proposal is stored within the database and procedures were written to extract selected textual data and generate a customer proposal. These procedures were written in the database command language.

A number of problems became evident during the implementation of this approach. The representation of configuration knowledge within the rule system is clumsy and difficult to maintain. Rules describing constraints on how different components can be configured and inferring the requirements imposed by the customer's bottle are stored in a common knowledge base. Furthermore, since the configuration problem required some searching for a "best" fit, a set of rules had to be included with procedural code embedded within them. Under these circumstances, maintaining rules by simply adding or deleting them could easily lead to some undesirable side effects.

Also, since the relational database implementation used forced fields to contain single valued attributes and to be of fixed length, difficulties existed in implementing procedures for maintaining and storing textual information within the database.

Thus, an object-oriented approach was examined as a means of providing a more effective method of developing the next generation system. The object-oriented implementation allows us to move the configuration knowledge down to the database level. This would make it easier to develop a general configuration algorithm and would facilitate the maintenance of the knowledge component of the system. Also, by associating textual information with the system components, it is easier to develop and maintain a system to generate the final quotations.

Table 2  
Attribute definitions for the Bottle object

<table><tr><td>Attribute</td><td>Data Source</td></tr><tr><td>Weight</td><td>Specified by Customer</td></tr><tr><td>Height</td><td>Specified by Customer</td></tr><tr><td>Width</td><td>Specified by Customer</td></tr><tr><td>PartLine</td><td>Specified by Customer</td></tr><tr><td>ProductionVolume</td><td>Specified by Customer</td></tr><tr><td>Cycletime</td><td>Computed: F{Weight, ProductionVolume}</td></tr><tr><td>RequiredShot</td><td>Computed: Weight * (HeadSet NumberHeads)</td></tr><tr><td>RequiredRating</td><td>Computed: F{RequiredShot, Cycletime}</td></tr><tr><td>MinNumberHeads</td><td>Computed: F{Cycletime, ProductionVolume}</td></tr><tr><td>HeadSeparation</td><td>Computed: F{Width, PartLine}</td></tr><tr><td>HeadSet</td><td>Object Reference: Specified by Configurer</td></tr></table>

To illustrate the application of the object-oriented approach to this problem, specific extruder configuration data are provided in Tables 2 through 4. Within these tables attribute values are determined through three general types of data sources: (1) those external to the data base (e.g. a customer, an engineer, or the configuration algorithm – the “Configurer”), (2) computed values including constraints, and (3) other objects. Values determined by passing a message to another object are indicated by placing the object-attribute pair in parenthesis, and the notation, F{...}, denotes the use of a mathematical function.

Table 3  
Attribute definitions for the Configuration object

<table><tr><td>Attribute</td><td>Data Source</td></tr><tr><td>CostGoal</td><td>Specified by Customer</td></tr><tr><td>ExtruderEfficiency</td><td>Specified by Customer</td></tr><tr><td>MotorEfficiency</td><td>Specified by Customer</td></tr><tr><td>Cost</td><td>Computed: F{(Extruder Cost), (Motor Cost), (Clamp Computed: F{(Cost), (HeadSet Cost)}</td></tr><tr><td>Bottle</td><td>Object Reference: Specified by Customer</td></tr><tr><td>Components:</td><td></td></tr><tr><td>Extruder</td><td>Object Reference: Specified by Configurer</td></tr><tr><td>Motor</td><td>Object Reference: Specified by Configurer</td></tr><tr><td>Clamp</td><td>Object Reference: Specified by Configurer</td></tr><tr><td>HeadSet</td><td>Object Reference: Specified by Configurer</td></tr><tr><td>Constraints:</td><td></td></tr><tr><td>CostConstraint</td><td>Cost &lt;= CostGoal</td></tr><tr><td>ExtruderLimit</td><td>(Bottle RequiredShot)/(Extruder ShotSize) &lt;= 1</td></tr><tr><td>ExtruderGoal</td><td>(Bottle RequiredShot)/(Extruder ShotSize) &gt; ExtruderEfficiency</td></tr><tr><td>MotorLimit</td><td>(Bottle RequiredRating)/(Motor Rating) &lt;= 1</td></tr><tr><td>MotorGoal</td><td>(Bottle RequiredRating)/(Motor Rating) &gt; MotorEfficiency</td></tr><tr><td>ClampWidthReq</td><td>(Clamp width) &gt;= F{(Bottle Width), (HeadSet NumberHeads)}</td></tr><tr><td>ClampHeightReq</td><td>(Clamp height) &gt;= (Bottle Height) + 3</td></tr></table>

Table 4
Attribute definitions for component objects

<table><tr><td>Object</td><td>Attribute</td><td>Data Source</td></tr><tr><td rowspan="3">Extruder</td><td>Model</td><td>Specified by Engineering</td></tr><tr><td>ShotSize</td><td>Specified by Engineering</td></tr><tr><td>Cost</td><td>Specified by Engineering</td></tr><tr><td rowspan="4">Motor</td><td>Model</td><td>Specified by Engineering</td></tr><tr><td>Rating</td><td>Specified by Engineering</td></tr><tr><td>Cost</td><td>Specified by Engineering</td></tr><tr><td>ValidExtruders</td><td>Collection Specified by Engineering</td></tr><tr><td rowspan="6">Clamp</td><td>Length</td><td>Specified by Engineering</td></tr><tr><td>Width</td><td>Specified by Engineering</td></tr><tr><td>Height</td><td>Specified by Engineering</td></tr><tr><td>Cost</td><td>Specified by Engineering</td></tr><tr><td>ValidExtruders</td><td>Collection Specified by Engineering</td></tr><tr><td>ValidHeadSets</td><td>Collection Specified by Engineering</td></tr><tr><td rowspan="3">HeadSet</td><td>NumberHeads</td><td>Specified by Engineering</td></tr><tr><td>CenterDistances</td><td>Specified by Engineering</td></tr><tr><td>Cost</td><td>Specified by Engineering</td></tr></table>

For this discussion, the data has been simplified and many technical details left out. Also, we are initially considering only the configuration of the base system. Methods for using textual information to generating the final proposals are briefly discussed at the end of this section, and the procedures for selecting optional equipment are omitted.

The configuration process is driven by the bottle requirements given in Table 2. The weight of the bottle limits the production capacity or cycle-time. This in turn establishes the number of extrusion heads (one per bottle) that can be placed on one machine. The bottle size determines the distance between heads.

A configuration algorithm generates “Configuration” objects illustrated in Table 3. The combination of number of heads and head separation is used to define the head arrangement (or “HeadSet” in Tables 2 and 3). The clamp, which is used to hold the extrusion heads, can only handle certain head arrangements and fit on certain machines. Required width and height dimensions for the clamp are determined by the bottle size and number of heads. A generalized algorithm uses the constraints specified with the configuration class definition to generated feasible configurations composed of the components given in Table 4. The OODB thus separates the knowledge of how to configure components from the procedure to determine and select feasible configuration. This allows for the maintenance of this knowledge within the database.

In reviewing this illustration the additional power of the object-oriented model becomes evident. Generally, objects correspond to relations and their attributes. Features not typically supported in relational implementations include the multi-value attributes, such as ValidExtruders and ValidHeadSets and the definition of a complex data object in the “Configuration” object. The configuration object contains references to the “Bottle” object and the various component objects. Messages are sent through these objects to compute derived attributes or evaluate constraints. For instance, total configuration cost is determined by asking each component for their individual cost. Extruder efficiency limits are determined sending messages to the bottle and extruder to determine the bottle’s required shot and the extruder’s shot size.

The reference to objects within objects provides the context in which a configuration is determined. For instance, selection of an extruder requires the evaluation of a bottle's required shot size. However, to determine this value, the bottle needs to know the HeadSet for the current configuration (see Table 1). Thus the configuration algorithm must establish HeadSet as a subgoal, and select it for the bottle, prior to determining the extruder. This results in a inferencing scheme similar to that found in backward chaining expert systems. The main difference is that the knowledge, typically represented in rules within expert systems, is depicted in the OODB as constraints and derived attributes.

The configuration activity can also be viewed as a process of querying the database for needed components. By enforcing constraints, only those items that would fit the current design goals, bottle specification, and partial configuration will be generated by the system. By placing the constraint knowledge at the database level, constraints can be easily added, removed, or changed without producing undesirable side effects.

Textual data can be easily added to configuration objects to enable the generation of a finished quotation for the customer. Two new objects would be added: a “QuotationDocument” and a “Text-Line.” The QuotationDocument contains standard quotation text and a collection of TextLines. The configuration objects would have an attribute referring to its QuotationDocument, and each component with a configuration would refer to its own TextLines instances. As components are selected, the QuotationDocument and component would share these text lines.

Instances of the TextLine object contain attributes indicating the sequence, the format (the extruder system quotations were presented in an outline form), methods for inserting component related values, and the text itself. The component related values are computed using the message passing concept. A collection of object-attribute pairs, representing messages to be sent to configuration objects, provide a specification for producing values to be placed in specially marked locations within a TextLine. For instance, one of the lines describing a clamp would look like, "A xx inch by xx inch platen." Values indicating the length and width of the clamp would be obtained by storing the two pairs: "Clamp Length" and "Clamp Width". Thus a generalizable quotation generation routine can be easily written that would compose a finished text line by sending the indicated messages to the proper component within the configuration object.

Textual information may depend only on the existence of any component or may vary with each specific instance of a component. The clamp related text given above would appear whenever a clamp is included in the configuration regardless of what clamp is chosen. Only the width and height values would change from clamp to clamp. In another situation, an optional piece of equipment, such a chiller unit, can be added to the extruder system for the purpose of cooling the bottles. Each chiller unit has its own unique description that can be displayed only if that component is selected.

Within an OODB both of these types of descriptions are efficiently handled. The clamp message is associated with the object class, “Clamp”, and inherited by all instances of that class. In a sense it becomes part of a meta-object or schema. On the other hand, the chiller unit description would be established at the instance level. At either level, the message passing protocol for inserting component values within the text can be implemented.

Thus this illustration demonstrates the ability for an object-oriented database to place more “intelligence” down at the database level. Information on how components can be configured, on criteria used to select components, and on how to display configuration information are now part of the database as opposed to being incorporated within program code. This produces a primary benefit of making it easier to maintain configuration and quotation related knowledge, but it also makes it easier to develop generic programs to handle the configuration and quotation generation tasks.

## 5. Conclusions

This paper develops the concept of an object-oriented database, contrasts it with the relational database, and demonstrates for a specific application how this new approach can be applied. The OODB concept offers great potential to the development of increasing complex applications that require a greater degree of “intelligence” to be incorporated with them. However, many issues still need to be resolved.

The major difficulty is the lack of a standard for object-oriented DBMS. This is still an evolving technology and commercial products are now just becoming available. Research has taken different paths toward OODB development and implementation. The application presented here has only been prototyped within an object-oriented language; a specific OODB package has not been used because of package availability and uncertainty. There may well evolve multiple standards with certain types of applications, lending themselves to certain types of object-oriented DBMS implementations.

More experience is needed with differing types of object-oriented application designs. This paper presents one such approach. The growth of OODB applications may be slowed by complexities inherit in problems that are good candidates and the lack of an established design methodology. However, with a broader base of applications, a classification scheme could possibly be developed that would enable us to map problem needs to OODB capabilities.

The most critical issue affecting successful object-oriented DBMS implementation may be the user interface design. Within relational implementations there are standardized query languages. In addition, most systems support the capability to position data attribute values on a formatted screen for the purposes of display and update. Since, within an object-oriented DBMS, attributes may be multi-valued or refer to other objects, we no longer have easily displayable data types.

Object-oriented languages handle this problem by using multiple pane windows in which the user can use a pointing device (such as a mouse) to select an attribute or object. Upon selection, a separate window or pane is displayed containing the contents of the “subobject.” Unfortunately, the design of these displays may be very application dependent. Again, more experience is needed to determine if generalizable interface designs can be effectively used within an OODB environment.

The OODB technology can potentially open up to computerization a vast array of new applications and enable existing ones to be implemented more effectively. We need to investigate how to take advantage of this potential. It presents both an opportunity and challenge for the development of future business applications.

## References

Andrews, T. and C. Harris. "Combining Language and Database Advances in an Object-Oriented Development Environment." OOPSLA 1987 Proceedings, pp. 430–440.

Batory, D.S., Leung, T.Y. and Wise, T.E. "GENESIS: A Project to Develop an Extensible Database Management System." ACM Transactions on Database Systems, September, 1986, pp 231–262.

Carey, M., D. DeWitt, D. Frank, G. Graefe, M. Muralikrishna, J. Richardson, and E. Shekita. "The Architecture of the

EXODUS Extensible DBMS." Proceedings of The First International Workshop on Object-Oriented Databases, September, 1986, pp. 52–65.

Dayal, U., and J. Smith "PROBE: An Knowledge-Oriented Database Management System." in M.I.. Brodie and J. Mylopoulos (eds.), On Knowledge Based Management Systems: Integrating Artificial Intelligence and Database Technology, Springer-Verlag, 1986, pp. 227–257.

Dittrich and U. Dayal, eds. Proceedings of the 1986 International Workshop on Object-Oriented Database Systems. Computer Society Press, September, 1986.

Goldberg, A. and D. Robinson. Smalltalk-80: The Language and Its Implementation. Addison Wesley, Reading, MA, May, 1983.

Hudson, S., and R. King. “CACTIS: A Database System for Specifying Functionally-Defined Data.” Proceedings of The First International Workshop on Object-Oriented Databases, Sept, 1986, pp. 26–37.

Hudson, S, and R. King. "The Cactis Project: Database Support for Software Environments." IEEE Transactions on Software Engineering, Vol. 14, No. 6, June, 1988, pp. 709-715.

Hull, R, and R. King. "Semantic Database Modeling: Survey, Applications, and Research Issues." ACM Computing Surveys, Vol. 19, No. 3, September, 1987, pp. 201–260.

Maier, D., J. Stein, A. Otis, and A. Purdy. “Development of An Object-Oriented DBMS.” ACM SIGPLAN, Vol. 21, No. 11, November, 1986, pp. 472–482.

McDermott, H. "R1: A Rule-based Configurer of Computer Systems." Artificial Intelligence Magazine, Vol. 2, No. 2, 1982, pp. 21–29.

O'Brien, P., B. Bullis, and C. Schaffert. "Persistent and Shared Objects in Trellis/Owl." Proceedings of The First International Workshop on Object-Oriented Databases, September, 1986, pp. 113–123.

Purdy, A., B. Schuchardt, and D. Maier. “Integrating an Object Server with Other Worlds.” ACM Transactions on Office Information Systems, Vol. 5, No. 1, January, 1987, pp. 27–47.

Shipman, D.W., “The Functional Data Motel and the Data Language DAPLEX.” ACM Transactions on Database Systems, Vol. 6, No. 1, March, 1981, pp 140–73.

Stonebraker, M., J. Anton, and E. Hanson. “Extending a Relational Data base System with Procedures.” ACM Transactions on Database Systems, September, 1987.

Stonebraker, M., E. Hanson, and S. Potamianos, “The POST-GRES Rule Manager.” IEEE Transactions on Software Engineering, Vol. 14, No. 7, July 1988, pp. 897–907.
