---
otero_id: 17311
otero_key: "3MF4PYG5"
title: "An object-oriented approach to model management"
authors: "Melanie L. Lenard"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90023-v"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An object-oriented approach to model management

Melanie L. Lenard

Boston University, School of Management, Boston, MA 02215, USA

In order to apply the object-oriented programming paradigm to Model Management, a model must be interpreted as a collection of “objects” which perform the various model management functions by receiving and responding to “messages”. The recently proposed Structured Modeling framework is used to identify the classes of objects which constitute a model. The protocols, or sets of messages, which would be needed to carry out a variety of model manipulations, are also described. The close correspondence between the representation of a Structured Model in terms of objects and an earlier proposal for its representation as a relational database suggests the possibility of using a relational DBMS to implement an object-oriented Model Management System.

Keywords: Model management, Object-oriented systems, Structured modeling, Modeling systems

![](/api/attachments/3MF4PYG5/fulltext/images/43cc87e602e39c5d5c06a150a3a58b8f12d84eafecda4407009184b0d4e6b6ef.jpg)

Melanie L. Lenard is an Associate Professor in the Management Information Systems Department of the School of Management at Boston University. She has also been a visiting faculty member at the Graduate School of Management at U.C.L.A. and a Visiting Scientist at the Operations Research Center at M.I.T. Professor Lenard received her B.S. in Chemistry from the University of Rochester and M.S. and Sc.D. degrees in Operations Research from

Columbia University. Her research focuses on the integration of optimization (and other kinds of Management Science models) with decision support systems and on the design of model management systems. Professor Lenard is a member of Operations Society of America, the Mathematical Programming Society, ACM and SIGMOD (Special Interest Group on the Management of Data), the IEEE Computer Society, and the International Society for Decision Support Systems.

Correspondence to: Melanie L. Lenard, Boston University, School of Management, 704 Commonwealth Avenue, Boston, MA 02215, USA.

## 1. Introduction

Model Management is (along with Data Management and Dialog Management) one of the three major areas of information technology which constitute the foundation of Decision Support Systems (DSS). According to Sprague and Carlson [13, Ch. 9], Model Management begins with a scheme for representing models and must provide for a variety of model manipulations, such as generating, restructuring, updating and obtaining the results of models. The software for the Model Management function must be tightly integrated with the data and dialog components of the DSS.

Although a number of proposals have been made for representing models, those which represent models as data, or in the same form as data in a knowledge base (for example, [5-7]), have the best prospects for achieving the desired level of integration with the data management component of the DSS. A recent proposal [10] represents models as a relational database with a logical structure based on Geoffrion's [8] Structured Modeling framework. How this relational database could (or should) be manipulated in order to implement the various model management functions is the subject of this paper.

Recent years have seen the identification of a number of programming paradigms (abstract types of programming languages). Among these is object-oriented programming, a paradigm which conceptualizes a program in terms of objects which respond to messages and inherit properties from a larger class of objects. In what follows, we will explore the consequences of approaching the problem of Model Management using the object-oriented programming paradigm.

We begin in the next section with an overview of object-oriented programming. Section 3 contains a proposal for representing a Structured Model as a collection of “objects”, and a discussion of the correspondence with the earlier proposal for representing a Structured Model as a relational database. Section 4 further explores the object-oriented paradigm by interpreting various model manipulation in terms of messages which could be sent to model objects. Finally, we discuss the possibility of implementing a Model Management System (MMS) based on this approach using the facilities of a Database Management System (DBMS).

## 2. Object-oriented programming

An article by Stefik and Bobrow [14] provides a good introduction to the concepts of object-oriented programming. The following discussion is based on that article.

The common element in object-oriented programming is the “object”. Objects are entities that combine the properties of procedures and data, in contrast with conventional programming languages where procedures and data are handled separately. All of the action in object-oriented programming comes from sending “messages” between objects. Instead of invoking a procedure to perform an operation on an object, one sends the object a message. Objects respond to messages using their own procedures or methods. Groups of similar objects are referred to as a “class”. Messages are usually designed in standardized sets of related messages called “protocols”.

In addition to message-sending, the second major idea in object-oriented programming is specialization, or class inheritance. Objects that are almost like other objects can be specified as subclasses which inherit the properties (in particular, the procedures) of their superclass and also have some special properties of their own. In most object languages, objects are divided into two major categories, classes and instances. The instances of a class are objects which are so similar that they share the same set of messages. In an object language, “integer” would be one sub-class of class “number”, while “3” and “4” would be instances of class “integer”.

Many of the ideas behind object-oriented programming have roots going back to SIMULA. Object-oriented programming languages are ideal for simulation applications where it is necessary to represent collections of things that interact in unexpected ways. The first interactive display-based implementation was the SMALLTALK language [9]. Table 1 shows some of the classes and subclasses of objects provided in SMALLTALK. Over the past few years, object-oriented programming languages have become popular in the artificial intelligence community, often as add-ons to LISP, for example, the language LOOPS [1].

```csv
Table 1
Some SMALLTALK objects.
Magnitude
Character
Number
Float
Integer
Look-upKey
Association
(A Key-Value pair)
Collection
SequenceableCollection
ArrayedCollection
Array
String
OrderedCollection
SortedCollection
Bag
Set
Dictionary
(A Set of Associations)
```

## 3. Structured modeling

Structural Modeling (SM), developed by Geoffrion [8], is a formal framework for describing models. SM identifies the basic components of models, the relationships among these components, and conditions under which a model may be termed “structured”. It includes a language for describing a model schema (class of models) and prescribes data tables for capturing the details of model instances.

In what follows, we propose an “object-oriented” view of a Structured Model. Then, we compare this view with the proposal $[10]$ for representing a SM as a relational database.

## 3.1. Structured models as objects

Using the conventions of SMALLTALK, Table 2 enumerates the classes of objects in a SM. (See

<table><tr><td>Table 2Some objects in a structured model.</td></tr><tr><td>ElementEntityPrimitiveEntityCompoundEntityAttributeFixedAttributeVariableAttributeFunctionTest</td></tr><tr><td>Genus (A Set of Elements)EntityGenusPrimitiveEntityGenusCompoundEntityGenusAttributeGenusFixedAttributeGenusVariableAttributeGenusFunctionGenusTestGenus</td></tr><tr><td>Module (An Array of Genera)CompoundModule</td></tr><tr><td>AssociationElementalDependenceCompoundOfAttributeOfFunctionOfGenericDependenceGenericCompoundOfGenericAttributeOfGenericFunctionOfModularDependenceModularCompoundOf</td></tr><tr><td>DictionaryElementalCallingSequenceGenericCallingSequence</td></tr><tr><td>RootedTreeElementalStructureGenericStructureModularStructure</td></tr><tr><td>Composite-ObjectStructured-Model</td></tr></table>

[10, Section 2) for a brief overview of SM.) The basic objects are Elements, of which there are three subclasses: Entities (Primitive and Compound), Attributes (Fixed and Variable), and Functions (numerical or logical-valued, the latter being also known as “Test” Elements). Test is shown as a subclass of Function, indicating that it inherits the general properties of Function but that it also has some special ones (in particular, its value is always a logical “True” or “False”). The class Entity has two subclasses, PrimitiveEntity and CompoundEntity, indicating that both primitive entities and compound entities can have special properties, in addition to those they have in common.

Each Element, other than a PrimitiveEntity, has a calling sequence, that is, a list of Elements on which it is dependent. ElementalDependency is a subclass of Association (an Association is a Key-Value pair). ElementalDependency has three subclasses:

(1) A CompoundEntity is a “CompoundOf” other Entities;

(2) An Attribute is an “AttributeOf” some Entity;

(3) A Function is an “AttributeOf” some Entity and is a “FunctionOf” Attributes and other Functions.

(The inverse of the Associations “CompoundOf”, “AttributeOf”, and “FunctionOf” are “ComponentOf”, “IndexOf”, and “ArgumentOf”, respectively.)

The ordered set of dependencies for an Element is termed in SM an elemental calling sequence. In the object-oriented view, an ElementalCallingSequence is a Dictionary or Set of all ElementalDependence Associations in the model. For example, if LINK-AB is a CompoundEntity representing a (directed) transportation link from PLANT-A to CUST-B, then the ElementalCallingSequence includes the following two Associations: (LINK-AB, 1: PLANT-A) and (LINK-AB, 2: CUST-B), where “:” separates the Key from the Value of the Association.

At the next level of structure in a SM, Elements of the same type can be grouped into a Genus if they satisfy the property of “generic similarity”, namely, if one Element in GENUSA is dependent on (“calls”) some Element in GENUSB, then every Element in GENUSA “calls” some Element of GENUSB. Thus, there are several Genus subclasses, each of which is a Set of Elements of the corresponding type.

Correspondingly, there is a subclass of Association, GenericDependence, recording that GENUSA is “generically dependent” on GENUSB. Also, there is a Dictionary of these Associations called GenericCallingSequence, which shows, for example, that the Genus LINK calls on PLANT and CUST Genera, in that order, by including the two Associations: (LINK, 1: PLANT) and (LINK, 2: CUST).

At the highest level of aggregation, an Array of one or more related Genera is termed a Module in SM. It is an Array rather than a Set because its elements must be at least partially ordered, that is, the ith Genus may call the jth Genus in the Module only if i is less than j. A CompoundModule is an Array whose elements are other Modules. This gives rise to a class of Associations between Modules, namely ModularDependence, and a Dictionary of these Associations, namely ModularContents. Each of the three Dictionaries may be represented as an edge-labeled (to indicate ordering of branches) RootedTree, and corresponds to one of the subclasses ElementalStructure, GenericStructure, and ModularStructure.

Finally, there is an object shown as a subclass of Composite-Object, termed Structured-Model. A Composite-Object contains a prescribed list of Objects from other Classes. In this case, a Structured-Model is a collection of one or more Elements, Genera, and Modules, together with the Dictionaries and their RootedTree representations.

## 3.2. Structured models as relations

In Table 3, we list the relations proposed for a database containing a SM. In the Elemental Relations, all instances of the classes Entity and FixedAttribute (having real, integer, or character values) are enumerated in the E and A (AREAL, AINT, and ACHAR) Relations, respectively. To complete the database, there should be relations listing all VariableAttributes and Functions as well, since they will be assigned values at some times. All instances of the class Module are enumerated in the MODULE Relation. All instances of the class Genus are enumerated in the GENUS Relation. The other attributes of MODULE, GENUS, E, AREAL, AINT, and ACHAR are, in object-oriented terminology, instance variables. For example, in GENUS, the tuple

```txt
Table 3
Structured modeling relations.

Modular Relations
    MODULE (ModName, Interp)
    CONTENT (ModName, Contains)

Generic Relations
    GENUS (GenusName, Type, Interp)
    CALLS (GenusName, SeqNo, CalledGenusName)
    RULES (GenusName, Rule)
    DATATYPE (GenusName, Dtype)

Elemental Relations
    E (GenusName, Index, Ename)
    CE (GenusName, Index, CalledGenusName, CalledIndex)
    AREAL (GenusName, Index, Value)
    AINT (GenusName, Index, Value)
    ACHAR (GenusName, Index, Value)
```

<table><tr><td colspan="2">Table 4Some SMALLTALK protocols.</td></tr><tr><td colspan="2">Class Protocols</td></tr><tr><td rowspan="2">Creating/Updating/Deleting</td><td>ClassVariable</td></tr><tr><td>ClassDescription</td></tr><tr><td>Accessing (NamesOf?, ValuesOf? NumberOf?)</td><td>MethodDictionary SubClass, SuperClass Instance InstanceVariable</td></tr><tr><td>Testing (IsIt[...]?, Includes[...]?, Accesses[...]?)</td><td></td></tr><tr><td colspan="2">Set Protocols</td></tr><tr><td>Adding/Deleting an Element Testing (NumberOf Elements?)</td><td></td></tr><tr><td colspan="2">Dictionary Protocols</td></tr><tr><td>Adding/Deleting an Association (Key-Value Pair) Accessing (ValueAt: [aKey]?) Testing (Includes: [aValue]?)</td><td></td></tr></table>

## (PLANT, pe, A list of plants)

conveys the information that one instance of the class Genus has the name PLANT, is in fact a PrimitiveEntityGenus ("Type" = "pe"), and has as its Interpretation ("Interp") the string "A list of plants". A partition of the GENUS Relation on the values of "Type" would emphasize the subclasses of class Genus. The CONTAINS, CALLS, and CE Relations are the representations of the Dictionaries, ModularContents, GenericCallingSequence, and ElementalCallingSequence, respectively.

The Relation DATATYPE contains instance variables (i.e. the data types) for AttributeGenera and FunctionGenera, while RULES contains instance variables (i.e. the function rules) for FunctionGenera only. If GENUS were partitioned on Type, these instance variables could be additional attributes on the appropriate partitioned relations.

To summarize then, the correspondences between the object-oriented and the relational views of a SM are: (1) the Module, Genus, and Element classes of SM objects (and their subclasses) are instantiated as tuples in the MODULE, GENUS, and four of the five Elemental Relations, respectively; (2) the Association and Dictionary classes of SM objects (and their subclasses) are instantiated in the CONTAINS, CALLS, and CE Relations, respectively; and (3) a Structured Model is a Composite-Object whose instances correspond to instances of the relational database shown in Table 3.

## 4. Model manipulations as messages

An Object has, in addition to its class and instance variables, a set of Methods for responding to Messages it may receive. Given an interpretation of a SM as a collection of objects, the next step is to interpret model manipulations as messages.

Often, messages can be arranged in standardized groups known as Protocols. For example, every Class must have a Protocol for Creating, Updating, or Deleting its instances, its place in the hierarchy, and its MethodDictionary. In addition, every Set must have a Protocol for Adding and Deleting its elements.

Table 4 shows a number of the Protocols for the class Dictionary in the SMALLTALK language. In addition to Protocols for Creating/Updating/Deleting, there are various Protocols for Accessing or Testing which, in database terminology, are queries. At a minimum, then, the SM Objects should be able to respond to any or all of the Protocols to which its superclass (be it a Set, an Array, or a Dictionary) can respond.

As an illustration, the SM class Attribute-Genus, as a subclass of Set, should respond to Messages for Creating/Updating/Deleting instances and instance variables, for Adding/Removing Elements from its instances, and for Accessing/Testing the number or names of instances and their elements. (See Table 5.) Thus, many model manipulations such as “Change the Datatype of the Attribute SUPPLY-AT-PLANT to Integer” or “Delete PLANT-101 from the list of Plants" can be accomplished by implementing the equivalent of the SMALLTALK Class and Set Protocols.

However, there are other higher-level model manipulations, such as restructuring by integration or aggregation, which have no immediate analog in the SMALLTALK protocols. Therefore, it will be necessary to add to the Methods known to the StructuredModel so that it could respond to a Message such as “IntegrateWith: [a Model] by a Join over: [aGenusName]”. The Method would include the sending of a variety of Messages (test/access/create/update/delete) to the components of the Models being integrated.

Another category of high-level model manipulations are those which assign values to VariableAttributes and Functions by “evaluating”, “solving”, or “optimizing” the model. (These correspond to applying what are popularly known as “what if?”, “what works?”, and “what’s best?” methodologies, respectively). We will call model manipulations of this kind “value assignments”. For example, “optimizing” a model means assigning values to all the VariableAttributes so that the value of every Test is “True” and some Function is maximized or minimized. This is usually accomplished by invoking a numerical procedure such as the Simplex algorithm for linear programming. Therefore, the Model should have a Method for responding to a Message such as “Minimize: [aFunction]”. The Method will normally include preparing input to and processing output from an optimization software package.

An alternate way to implement value assignment manipulations would be to create a new Class of Composite-Objects. For example, an LP-Model would be a Composite of Rows, Columns, Coefficients, Right-Hand Sides, and Bounds. Then, an instance of the class Module would respond to a Message “AsLPModel” by transforming itself to an instance of LPModel, if possible, while only the class LPModel would respond to a Message such as “Minimize: [aRow]”.

A subclass of LPModel could be SolvedLP-Model differing from its superclass in that values have been assigned to Rows and Columns (namely the primal and dual activity levels resulting from the solution of the linear program). In turn, there would be a subclass of Structured Model, called OptimizedModel, again differing from the superclass only in that values have been assigned to Functions and Attributes. To complete the process, then, a SolvedLPModel would respond to a Message “AsOptimizedModel” by transforming itself from a “Rows, Columns” representation to a “Modular, Generic” representation as an “OptimizedModel”.

## 5. Implementation issues

A possible route to implementation is to build a Model Management System using an object-oriented language such as LOOPS. (This is the approach being taken by Oldford and Peters [11].) However, to achieve integration with the Data and Dialog components, the entire DSS would need to be coded in the same way.

The alternative is to exploit the correspondence between Objects and Relations, so that the Methods can be written in one or more of the languages of a relational DBMS. Thus, the object-oriented paradigm will suggest the form and functional structure of the MMS without necessitating the use of an object-oriented language. Furthermore, the integration of Model Management and Data Management will be straightforward.

Among the many proposals that have been made for extending the original relational data model (some of which are discussed in [2]), there is one [4] which takes an object-oriented view of transactions in a relational database. The implementation of a relational MMS will extend some of the proposals contained therein.

<table><tr><td>Create/Update/Delete an AttributeGenusName: [anIdentifier]Interpretation: [aString]Dtype: [aDomain]</td></tr><tr><td>Create/Update/Delete GenericAttributeOf AssociationAttribute Genus: [anAttributeGenus]is Generic Attribute of: [anEntityGenus]</td></tr><tr><td>Create/Update/Delete an AttributeElementElement of: [anAttributeGenus]Attribute of: [anEntity ElementIndex]Value: [aValue]</td></tr><tr><td>Accessing AttributeGenusWhatIs: Interpretation? Dtype?NumberOf: Elements?</td></tr><tr><td>Accessing AttributeElementWhatIs: Value?</td></tr></table>

A relational DBMS provides “objects” such as relations, attributes, domains, keys, and tuples having as defined operations (methods) all of the capabilities of the Query Language (e.g. SELECT or PROJECT), the Data Definition Language, (e.g. CREATE and DELETE relations, DEFINE attributes) and the Data Manipulation Language (INSERT, UPDATE, DELETE tuples). Additionally, most RDBMS provide access to more Primitive classes of objects such as Numbers and Characters, along with operations such as elementary mathematical and string manipulation functions. New objects can be defined in terms of the primitive objects of the database following the classification scheme shown in Table 2.

## 6. Concluding remarks

In summary, we have shown that the object-oriented programming paradigm may be profitably applied to Model Management. By taking an object-oriented view of the Structured Modeling framework and its representation as a relational database, the implementation of a Model Management System as a function of a relational DBMS becomes a feasible alternative.

As the theme of a 1984 conference [3] emphasizes, artificial intelligence, database management, and programming languages, although usually considered separate disciplines, do share many common intellectual themes which come under the general heading of “conceptual modeling”. Thus, it is reasonable to expect that there will continue to be a transfer of technology among these fields.

Quite apart from the technical advantages, the object-oriented approach to Model Management may facilitate the human-machine interaction at the heart of computer based modeling. In keeping with the “direct manipulation” favored by Shneiderman [12], the model builder and user will work with objects with prescribed behaviors (or methods of responding to messages). Thus, working with mathematical models will appear as a less abstract process, more like working with physical models of the system under study.

## References

[1] D.G. Bobrow and M. Stefik, The Loops Manual, Tech, Rep. KB-VSLI-81-13, Knowledge Systems Area. Xerox Palo Alto Research Center (1981).

[2] M.L. Brodie, On the development of data models, in: On Conceptual Modeling, ed. M.L. Brodie, J. Mylopoulos and J.W. Schmidt (Springer-Verlag, NY, 1984).

[3] M.L. Brodie, J. Mylopoulos and J.W. Schmidt, On Conceptual Modeling, (Spring-Verlag, NY, 1984).

[4] M.L. Brodie and Ridjanovic, On the design and specification of database transactions, in: On Conceptual Modeling, ed. M.L. Brodie, J. Mylopoulos and J.W. Schmidt (Springer-Verlag, New York, 1984).

[5] D.R. Dolk and B.R. Konsynski, Knowledge representation for model management systems, IEEE Transactions on Software Engineering. SE-10, 6 (November, 1984) pp. 619–628.

[6] J.J. Elam and J.C. Henderson, Knowledge engineering concepts for decision support system design and implementation, Proceedings, Fourteenth Annual Hawaii International Conference on System Sciences (Western Periodicals, North Hollywood, CA, 1980) pp. 639–643.

[7] J. Fedorowicz and G.B. Williams, Representing modeling knowledge in an intelligent decision support system, 2, 1 (1986) pp. 3–14.

[8] A.M. Geoffrion, An introduction to structured modeling, 33, 5 (1987), pp. 547–588.

[9] A. Goldberg and D. Robson, Smalltalk-80 (Addison-Wesley, Reading, MA, 1983).

[10] M.L. Lenard, Representing models as data, Journal of Management Information Systems, 2, 4 (1986) pp. 36–48.

[11] R.W. Oldford and S.C. Peters, DINDE: Toward more statistically sophisticated software, Technical Report No. 55. MIT Center for Computer Research in economics and Management Science, Cambridge, MA (1985).

[12] B. Shneiderman, Direct manipulation: A step beyond programming languages, IEEE Computer (1983) pp. 57–69.

[13] R.H. Sprague, Jr. and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, NJ, 1982).

[14] M. Stefik and D.G. Bobrow, Object-oriented programming: Themes and variations, The AI Magazine 5 (1986) pp. 40–62.
