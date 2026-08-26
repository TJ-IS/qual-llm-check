---
otero_id: 17099
otero_key: "67Z4SWRA"
title: "Object-oriented information management"
authors: "Peter C. Lockemann"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90030-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Object-Oriented Information Management

Peter C. LOCKEMANN

Fakultät für Informatik, Universität Karlsruhe, Karlsruhe, West Germany

Current computer-based information systems offer very little in terms of semantic control of information processing because only very little of the application semantics can be mapped to descriptive information to be utilized during the processing. As recent results in several areas of computer science demonstrate, object orientation is a highly promising approach to remedy the situation. The paper introduces the notion of object orientation, surveys some of the recent directions and results in several areas of computer science, explores where a corresponding approach could profitably be applied to information system design and what benefits and problems could arise, and then demonstrates that object orientation in information system design and operation would find excellent support by the latest developments in information base management and information design environments.

![](/api/attachments/67Z4SWRA/fulltext/images/832252f981bb3cda67d2860c35dbe19f335a7ddd279fa5d3d36a5b11828fdb0c.jpg)

Peter C. Lockemann received diploma and doctoral degrees in Electrical Engineering in 1958 and 1963, respectively. Joined the California Institute of Technology from 1963 to 1970 as a Research Fellow and Senior Research Fellow in Information Science. Spent 2 years with GMD Bonn as a senior scientist. Since 1972 Professor of Informatics at the University of Karlsruhe and since 1985 also a director of the Computer Science Research Center at Karlsruhe. Current research interests are in the areas of engineering databases, their techniques and applications, in particular for CAD databases, software engineering databases, process control databases, image evaluation databases. Recent emphasis is also on knowledge-based database design techniques for these applications, and on object-oriented modelling techniques. Author of two textbooks and more than 60 research papers in journals and conference proceedings, editor of four books. Received numerous research grants from public institutions and private industry.

## 1. Introduction

The classical definition of ‘information’ is one that sees it as a trinity of physical representation (syntax) with which a speaker or recipient could associate a certain meaning in his or her real or mental world (semantics) such that in a given context it would elicit from him or her a certain course of action (pragmatics). This is also the definition that underlies the concept of “information system” as a system that acts as a repository of physical representations, accessible by many people in many different contexts, and to be manipulated in a variety of ways according to context.

Computer-based information systems are, by their very nature, restricted to the manipulation of symbols and, hence, to the syntactic aspects of information. Any association of the representations with real-world phenomena is up to the user of the information; if s/he misinterprets it, s/he may draw the wrong conclusions or take the wrong actions. And any manipulation of information, e.g., to compute or infer new information from it, is based purely on symbolic representations and thus again devoid of semantic considerations. After information has gone through one or more processing steps a user may often be unable to judge whether the result, even though it may by itself have a meaningful interpretation, has any semantic relationship to its origins (fig. 1). Take as a trivial example the computation of an income distribution over a certain population where unknown income has been marked by '0' and been included in the calculations as a value of zero.

Can one introduce a certain degree of semantic control into the processing of information in an information system such that, even after a number of independent processing steps, the user of the derived information may have confidence in its semantic relevance? This is the issue that will be addressed in this paper. In approaching it, we start from the premise that as part of our cognition of the real world we recognize small pieces and assemble these according to different and varying rules or, alternatively, start with a bigger picture and then discern more and more details. Hence, we associate meaning with representations not merely by considering them as strings of symbols but also by perceiving a certain structure in the representation. As a rule of thumb, by adding structural richness to a symbolic representation one may shift more and more of the semantics towards the representation (fig. 1). As an extremely trivial example, consider a date which may be represented as a six-character string or, alternatively, substructured into day, month and year.

![](/api/attachments/67Z4SWRA/fulltext/images/003459a4c5fc348bd10d654f2a90a402ad53cc6507892b368aaa8448bec73592.jpg)

![](/api/attachments/67Z4SWRA/fulltext/images/e1fa63d00fac9175af9c2a0712f3adff1652db925aa9417d9bfecc18ad0c71de.jpg)  
Fig. 1. Loss of information during a computational process. The upper figure illustrates the problem: only the representation is subject to processing so that the meaning must be reconstructed, and action be taken in the recipient's context. This raises the question of how the relationship between the original meaning or context and the new meaning or context can be preserved. The lower figure indicates the solution by structural enrichment: more of the meaning and context is encoded in the original representation and passed to the recipient for reconstructing meaning and context.

Can one introduce structure into representation in a way that from the user's perspective appears both systematic and natural for expressing semantic knowledge? We believe there is, in the form of what in computer science is collectively referred to as object-orientation. In order to back up our claim, and to present the basic concepts we examine a number of more recent results from computer science research. We then study what its consequences would be for information system design, and whether and how a similar approach could be given the necessary technical support. Finally we discuss where limitations of such an approach to information systems would have to be expected.

## 2. The Concept of Object

Central to the semantics of information is the notion of model: Information stored in an information system is considered to be a model of some phenomenon in a real or mental world. Management of the database in an information system has as its objective the maintenance of symbolic representations that at all times can be associated with current or potential real-world phenomena under a fixed set of interpretation rules. To express the pragmatics we introduce the notion of an object as the representation of a model for a phenomenon that is of current (and perhaps temporary) interest to a user.

To draw technical consequences, this intuitive view must be translated into a technical one. To express the property of model under the premise of structural enrichment, we define an object as a set of structurally interrelated symbols or, more formally and recursively, as an unstructured ('atomic') collection of symbols or a structured set of objects. To add the pragmatic aspects, an object is that structured or unstructured information out of a larger structured collection of information that a user, in a given context, wishes to consider as a unit. For example, take a personnel file that one user wants to process in its entirety, e.g., to collect some statistics, while another breaks it down to look at some of the individual records, e.g., to change addresses of marital status. Consequently, there are two aspects to the notion of object: structure, and choice of the level of abstraction within the structure.

There is, however, a further important consequence. The more complex the structure, the larger the variety of operations that may potentially be performed on an object ([Ditt87a]). However, only few of the operations will be meaningful, the majority will not. Take the previous example: It makes sense to compute the average of the salaries over all personnel records, but it is certainly nonsense to take the average of the marital status or the zip codes. Consequently, the introduction of structure must be counterbalanced by a restriction on the operations to be performed, or to express it more constructively, by a list of permissible operations. Hence, there is a third aspect to the notion of object: the set of operations accepted for it or, as it is often called, its behavior ([Ditt87b]). Since what constitutes an object is a pragmatic decision, establishing the behavior of an object is also a pragmatic affair.

![](/api/attachments/67Z4SWRA/fulltext/images/1482a9c122109c7161872333fbcda0b0c10ea402f814db6a26f769e735485e85.jpg)  
Fig. 2. Approaches to object-orientation.

Fig. 2 illustrates the various aspects. If we restrict ourselves to purely structural considerations, or to what is called structural object-orientation, an object is characterized by its structure and a set of operations that allows to manipulate the structure in a completely unrestrained way (fig. 2a). If we include behavior we obtain behavioral object-orientation in which an object is characterized by its structure and a limited but more meaningful set of operations (fig. 2b).

Clearly it is entirely uneconomical to decide on structure and behavior of each individual object while it is introduced into the information system. Rather a certain degree of preplanning has to go into the information system. Consequently, before objects are being introduced, the set of potential objects is classified into a number of distinctive object types. Objects of identical type agree in certain structural aspects and in the set of operations applicable to them. For example, all (structurally-oriented) objects of type personnel record agree in their fields and the domains from which field values are taken, and in the operations such as creating a record; entering field values; modifying field values subject to the restriction that marital status must not change from married to single and the first name not changed at all; deleting field values subject to the restriction that the last name is not to be deleted unless the entire record is to be dropped. All (behavioral) objects of type personnel file may be subjected to insertion and deletion of records and to operations such as computing sums, averages, maximum and minimum values of salaries or tax deductions.

This basic notion underlies all approaches in computer science to object-orientation. We briefly examine the different forms it takes, and the elaborate extensions that have evolved in recent computer science research before we study the ramifications of object-orientation for information system design.

## 3. Object-Orientation in Computer Science

## 3.1. Object-Orientation in Programming

## 3.1.1. Object-oriented programming

The concept of object-orientation has initially emerged from programming and has extensively been explored and refined in this context (for a survey on more recent results and a comprehensive bibliography see [Shri87]). There have been many different motivations for object-oriented programming, ranging from the purely technical one as a technique for organizing very large programs to the conceptual one for providing a filter for the interpretation of raw data ([Wegn87]). Since the latter coincides with our own motivation in this paper, we feel justified in using this chapter for a somewhat more detailed introduction of the basic concepts of object-orientation.

Due to the different reasons given for this style of programming there is no universally accepted notion of object. For our present purpose we use one given by Agha and Hewitt [Agha87] who consider objects as computational agents which carry out well-specified actions in response to incoming communications. Consequently, in object-oriented programming a problem is represented in terms of autonomous objects which function independently of each other save for interactions among well-defined communication channels. An agent is capable of receiving and transmitting information, storing information, and transforming information ([Beec87]). Hence, an object consists of a set of procedures (often also called methods) that describes its external behavior, a further set of internal, auxiliary procedures, and a private memory.

Fig. 3 illustrates this notion by way of an example from the image evaluation of traffic scenes. Suppose that for the purpose of this evaluation automobiles are modelled by computational objects. Such an object will simulate the observable behavior of real automobiles by methods such as pick\_up\_passengers, drop\_off\_passengers, stop\_by\_the\_curb, accelerate, slow\_down, proceed, change\_lane, turn, to name a few. To implement these operations we maintain in private memory representational information on the automobile, e.g., successive positions, shape, maximum number of passengers, but also on the street system within camera view, e.g., geometry of lanes and sidewalks, use of lanes, traffic lights and signs.

![](/api/attachments/67Z4SWRA/fulltext/images/4b191a67ee3ae9113039dfab7ea961823df6070656b71a8291a5e3757ad2bd08.jpg)  
Fig. 3. Graphical illustration of objects, encapsulation, delegation and classification. The boxes represent classes of objects, with the class name in the shaded area, the externally visible methods in the center of the box, and the variables of the hidden representation in the lower portion. The lines indicate delegation from the upper class to the lower classes.

Beyond these basic properties, the notion of object in programming includes a number of paradigmatic concepts: encapsulation, delegation, communication, classification, and inheritance. We shall cover these one by one.

## 3.1.2. Encapsulation

The early development of the concept of an object can be traced to the programming language Simula where an object was thought of a self-contained program having its own data and procedures ([Birt73]). In modern object-oriented programming languages such as Smalltalk an object contains both a private memory and a set of operations which can be validly applied to the contents of that memory ([Gold83]). Encapsulation collects the private data and the set of operations into a single entity. Furthermore, it hides the private memory and the internal procedures from the external world so that the only way of communicating with the object and influencing the state of the memory is by way of the external methods. In other words, encapsulation prevents an object from being manipulated except via its defined external operations, an effect referred to as 'information hiding'.

For example, in defining automobile as an object the only way of manipulating models of automobiles is by the methods listed in ch. 3.1.1. The state of an automobile, e.g., its position, will change in accordance with the execution of these methods, but will not become visible to the outside other than by the effects of changes on subsequent operations. The technical reasons for encapsulation are thus quite obvious: If one is only interested in behavior the representation can safely be ignored, and by divorcing the two the representation may be freely modified and adjusted to factors such as better algorithmic solutions or new hardware technology.

## 3.1.3. Delegation

From the viewpoint of system design, encapsulation can be viewed as an abstraction mechanism. The external operations serve as an interface, and outsiders do not need to know how the object implements the operations. Later, in the course of stepwise refinement, the representation, and hence the implementation of the operations, may be broken down. In particular, one may express part of the implementation in terms of 'lower-level' objects. In an object-oriented scheme one may interpret this kind of refinement as subcomputations that are passed by one agent to another to continue processing or, as Agha and Hewitt [Agha87] call it, as delegation.

In our example, the computation of the changes of the visual appearance of an automobile as it approaches or regresses from the viewpoint or turns in front of it may be delegated to an object that specifically deals with geometric shapes (fig. 3). In turn, shapes can be broken down into lines, edges, surfaces, etc., which may again exhibit certain behavior. Similarly, another object may deal with traffic lights that change their color in a fixed sequence at regular intervals.

## 3.1.4. Communication

Viewing objects as computational agents and thus as active elements has as its consequence that communication between objects must also be viewed as an activity. Consequently, an object delegating a computation must send a request to the delegate, and can itself proceed to accept further communication ([Agha87]). The delegate has no access to the current behavior of the requesting object other than the information passed with the request. In Smalltalk this kind of interaction has been formalized into a message-passing mechanism in which objects exchange messages between one another, where a message invokes an operation associated with the recipient object ([Gold83]).

## 3.1.5. Classification

Abstraction is perhaps the most powerful tool for managing complexity. It allows one to deal with high-level concepts and understand them, before proceeding to consider details of individual objects ('instances'). Hence, encapsulation and delegation can be seen as abstraction mechanisms. Another abstraction mechanism allows one to group instances according to perceived similarities (classification).

A class in an object-oriented system specifies the common properties of all its instances. It is thus an abstraction representing a particular collection of related properties but ignoring property values that are specific to instances ([Ossh87]). In combination with encapsulation and delegation a class may be viewed even more narrowly as a specification of the behavior of its instances ([Skar87]). Consequently, classes specify an interface of operations ([Wegn87]). This is what we essentially did in fig. 3 since we do not refer to an individual automobile but rather to the class of automobiles.

Technically speaking, the implementation of methods can be kept with classes, and the instances physically contain only the private memory. Since each object is considered to be an element of a class, the class becomes the suit of armor that protects a representation for an object from arbitrary or unintended use ([Card85]). In fig. 3, the class automobile includes the code for the methods and thus, by necessity, a declaration of the structure of the private memory of all its instances, whereas the automobile instances carry the data themselves. Skarra and Zdonik [Skar87] thus define a class as a specification of behavior, which describes a set of operations, a set of properties, and a set of constraints that pertain to any instance of the class. Similarly, Hailpern and

![](/api/attachments/67Z4SWRA/fulltext/images/47d7f34227d05f8c6415cf646efee98f758890614e29e1645a5433a9deb1ac7c.jpg)  
Fig. 4. Graphical illustration of a class hierarchy. As before, boxes represent classes. Only the methods are shown as the properties to be inherited. Inheritance is from top to bottom. The bottom is an example of multiple inheritance.

Nguyen [Hail87] view classes as templates for member objects and as repositories for methods shared by these objects.

A class helps organize objects (or data). If this organization of objects is carried across several levels of abstraction, the results is a hierarchy of classes such that each is an abstraction of all its descendants ([Agha87, Hail87, Maie87, Ossh87]). A typical example is the organization of knowledge in terms of a taxonomy. Consider fig. 4 where automobile is classified as a vehicle and may be differentiated into passenger cars and trucks, meaning that an arbitrary passenger car is both a passenger car and an automobile. A class in a hierarchy is referred to as a superclass of its descendant classes, obtained from them by generalization. In fig. 4 automobiles and streetcars have been generalized to vehicles. The descendants of a class are its subclasses, derived from it by specialization. For example, automobiles can be specialized into passenger cars and trucks. Hence, the superclass-subclass relationship allows to capture similarities among various classes of entities that are not totally identical in behavior.

Subclassing also provides a means to handle special cases without cluttering up the definition of the normal case. For example, if we also wish to deal with the few old streetcars converted into service vehicles we do not specialize the class streetcar into two subclasses but instead leave the regular streetcars as such and just add a subclass service car. In other words, a superclass is not necessarily the union of all its subclasses.

Object-oriented programming languages use the term class where the more traditional programming languages use the term type. Indeed, the literature is rather vague on what the differences between classes and types are, if any at all. For the purpose of this paper we will consider both terms as synonymous.

Conventional typed languages are based on the idea that objects are of a unique type (monomorphic languages). By contrast, in polymorphic languages objects may have more than one type. Class hierarchies introduce polymorphism because an object is an instance of all its direct and indirect ancestors. For example, individual passenger cars and trucks are of type automobile and, hence, also of type vehicle. The hierarchy may not always be tree-like. For example, in figure 4 pickup trucks qualify as both passenger cars and trucks.

## 3.1.6. Inheritance

Classification, the abstraction of common properties to a class or a superclass, gives rise to a phenomenon referred to as inheritance: Objects of a subtype can be uniformly manipulated as if belonging to their supertypes (but not vice versa). In other words, objects of the subtype inherit all the visible properties of the supertype, i.e., its methods. The objects may, in addition, have operations specific to the subtype. In fig. 4 passenger cars inherit the operations accelerate, slow\_down, proceed, and turn that are common to all vehicles, stop\_by\_the\_curb and change\_lane that are just common to automobiles, and add as their own operations pick\_up\_passengers and drop\_off\_passengers. Or to phrase it differently, class inheritance is a mechanism for composing a new interface from the interfaces of one or more inherited classes and the interface of the inheriting class ([Wegn87]). Inheritance is, therefore, a concept dual to classification. This conceptual view has given rise to an inheritance theory ([Card84]). Non-treelike hierarchies lead to what is called multiple inheritance. Pickup trucks are an example: they inherit the operations of passenger cars, trucks, automobiles, and vehicles.

From a technical standpoint inheritance may be further differentiated ([Hail87]). In external interface inheritance a subclass includes all the externally visible methods of the superclass, and can also provide additional methods. In code sharing a subclass can use the functions provided by the superclass as if they were defined in the subclass itself. Hence multiple copies of the same program are eliminated. In type theory inheritance a subclass contains all the variables of the representation of the superclass, and further ones of its own. Inheritance may be reduced to delegation by introducing the notion of a prototype ([Lieb86]). A prototype represents the default behavior of a concept. An object can use the information stored in a prototype or can specify how it differs from the prototype. When such an object receives a message, it first checks its own behaviors. If it cannot respond it forwards the message to its prototype.

## 3.1.7. An example: Smalltalk

Smalltalk-80 ([Gold83]) is based on a uniform use of objects and messages. All conceptual entities are modeled as objects. An object is a uniform representation of information and an abstraction of two capabilities, to store information in a private memory that holds its state, and to manipulate its stored information or to carry out some activity. A primitive object, such as an integer, only has a value, which is the object itself. More complex objects contain instance variables through which they reference other objects.

The behavior of an object is encapsulated in methods. Methods consist of code that manipulate or return the state of an object. Methods are part of the definition of the object. Objects can communicate with one another through messages. Messages constitute the public interface of an object. For each message understood by an object, there is a corresponding method that executes the message. An object reacts to a message by executing the corresponding method, and returning an object.

Objects that respond to the same messages in the same way are grouped together into a class. All objects belonging to the same class are described by the same instance variables and the same methods. They all respond to the same messages. Objects that belong to a class are called instances of that class. A class describes the form (instance variables) and the operations (methods) of its instances. In fact, an object has no methods of its own but inherits all of its methods from its class.

Classes may be arranged into hierarchies reflecting the grouping of objects across several levels of abstraction. For a pair of classes on a class hierarchy; the higher level class is called a superclass of the lower level class, and the lower level class a subclass of the higher level class. The instance variables and methods (collectively called properties) specified for a class are inherited by all its subclasses. Additional properties may be specified for each of the subclasses. A class inherits properties only from its immediate superclass. Since the latter inherits properties from its own superclass, it follows by induction that a class inherits properties from every class in its superclass chain. The inheritance mechanism is based on naming, e.g., if a method selected in a message is not found in the receiver's class, the methods in its superclass are searched next, and so on.

Classes are themselves objects and may thus be grouped. To distinguish this kind of grouping from the class hierarchy the resulting classes are referred to as meta-classes. To give an example, automobile might be an object of a class computation\_model. Clearly, any method that automobile inherits from this class (such as store\_model) is not passed on to truck.

## 3.2. Object-Orientation in Database Systems

## 3.2.1. Clustering

Now that the principal aspects of object-orientation have been established we can restrict ourselves to a brief overview of which of these recur in some other areas of computer science. One of the basic tenets of database technology that is mostly adhered to even today is the strict separation between data including their structure, and use of the data. As a consequence, the predominant approach to database systems is structural object-orientation.

The concepts developed in ch. 3.1 are tailored to behavioral object-orientation. In structural object-orientation there is no notion of agent and hence no notion of delegation and communication. Encapsulation cannot refer to the hiding of

## AUTOMOBILE

<table><tr><td rowspan="3">id</td><td colspan="4">positions</td><td rowspan="3">no_of_pass.</td><td colspan="3">shape</td></tr><tr><td rowspan="2">x</td><td rowspan="2">y</td><td rowspan="2">z</td><td rowspan="2">t</td><td colspan="2">contour</td><td>surfaces</td></tr><tr><td>lines</td><td>t</td><td>: : : : : :</td></tr></table>

Fig. 5. Graphical representation of an NF $^{2}$ schema. The top level is a relation with attributes id, positions, no\_of\_pass. and shape. The position of each automobile is again represented by a relation with attributes x, y, z, and t. The shape of each automobile is a relation with attributes contour and surfaces, where each contour is described by a further relation containing the lines.

representations and is usually replaced by the weaker notion of data independence for hiding the details of physical realization. Classification and inheritance should emphasize structural aspects and thus correspond to what was called type theory inheritance in ch. 3.1.6. On the other hand, the pre-eminence of structure introduces three new concepts ([Ossh87]): clustering, decomposition, and highlighting.

Clustering (also called aggregation) is a form of abstraction that groups interacting entities into a cluster, associating with the cluster those properties that govern the interaction, and then regards the cluster as an atomic entity whenever possible. Hence, the difference between classes and clusters is that the former essentially confer properties on each of their instances whereas the latter regulate interactions between instances. The typical relationship underlying clusters is part-of (as opposed to is and is-a for classification), thus the members are referred to as components. Consider the example of figs. 5 and 6 where a street is composed of adjacent lanes, or a shape of contours and surfaces. Further relationships may enter into a cluster, e.g., the metric information for a geometric shape. In the literature clusters are referred to as molecules ([Bato84, Härd87]) or complex objects ([Ditt87b, Lori85]).

Decomposition is the dual principle to clustering: it disassembles an entity into its individual objects. Highlighting is a desirable consequence of clustering: it draws attention to a small number of important facts, even in the midst of a wealth of detail.

## 3.2.2. Approaches to object-oriented databases

Like in programming, the concept of type plays a pre-eminent role in database systems where it manifests itself in the form of a database schema. Nonetheless, the classical database management system – based on the network or the relational data models – cannot be considered structurally object-oriented since they exhibit none of the characteristics discussed above. Consequently, one should expect difficulties in reflecting natural phenomena directly in a database. Indeed, only the typical business and administrative applications with well-established manual information systems based on forms and spreadsheets find their natural counterparts in the records and tuples of these models. In other applications – office automation, automated design, manufacturing, traffic control – mapping of what would be considered natural objects becomes a tedious task. For example, the representation of an automobile in terms of its functional parameters and its refinement into smaller objects must be spread across a large number of relations (for an example from image evaluation see [Walt87]). It is equally cumbersome (and lengthy in time even if a database system does it) to reconstruct an object from all these relations. Inheritance and clustering is not being dealt with at all by these systems.

![](/api/attachments/67Z4SWRA/fulltext/images/0ab663ca31b32a2b8a5c97a8ab7aed206d592f9ba88b0ec77ef4674692452bae.jpg)  
Fig. 6. Graphical illustration of a CERM schema. The boxes represent entity types, the diamonds relationship types between entity types. The grey boxes indicate clustering of entities and relationships into new entities. The small circles describe attributes which may be associated with both elementary entities or clustered entities.

These shortcomings are being attacked on two fronts: structural object-orientation with heavy emphasis on clustering and less on inheritance, and – somewhat in contrast to traditional philosophy – behavioral object-orientation along the lines of Smalltalk. Two recent conference proceedings ([Ditt86, Ditt88]) give a good overview of these efforts. For more recent approaches to structural object-orientation see also [Atwo85, Bane87, Bato84, Dada86, Daya86, Ditt87a, Ditt87b, Härd87, Lori85, Ston86b], and to behavioral object-orientation see [Banc88, Care88, Fish87, Heil88, Kemp87, Kim87, Lecl88, Maie87, Stemp88, Ston87, Woel87b]. We give a few typical examples.

## 3.2.3. Structural object-orientation

In structural object-orientation, a fair number of researchers start from the relational model and extend it in suitable ways to impose clustering on the set of tuples. One way in which this is done is by introducing an abstract pointer mechanism for interconnecting the tuples (from one or more relations) that together make up a cluster object ([Lori85]). A very few operations are provided that retrieve in one step all the tuples belonging to a given object provided, however, the tuple arrangement is strictly hierarchical. Another approach avoids the pointers by directly building the tree structure into a relation: in contrast to the standard relational model where attribute values are atomic, these values may themselves be relations. Nesting of relations may thus occur to an arbitrary depth. This data model, called NF $^{2}$ (from Non-First-Normal-Form), provides a rich set of operations for composing objects, for retrieving entire objects, for selecting and thus highlighting subobjects, and for decomposing objects into subobjects although this latter operation is surprisingly cumbersome ([Dada86, Sche86]).

Other solutions start from the entity-relationship model (ERM). From a technical perspective this model could hardly be classified as object-oriented because all it does is introduce basic building blocks called entities, and establish relationships between these. Its success as a method for database design is due to the naturalness with which many real-world phenomena can be mirrored as entities and relationships. By grouping several entities, and relationships among them into a cluster, and treating the clusters again as entities one obtains a fairly general structurally object-oriented model that has proven particularly successful in a number of experimental database systems for capturing the essence of design applications. Two such examples are the complex-entity-relationship model (CERM [Ditt87b]) and Molecular Objects ([Bato84]). The former extends the ERM by concepts for organizing entities, and by time versions, and provides a rich set of operations for manipulating the structures and navigating through them. The latter goes even further by introducing parameterized structures, but avoids the issue of operations. Both are not restricted to tree-like structures.

To illustrate the structural approach, figs. 5 and 6 give simplified graphical NF $^{2}$ and CERM representations, respectively, for automobiles. Unfortunately, structural object-orientation does not deal satisfactorily with inheritance, and structure does not suffice to express all the semantics of an object (such as that an automobile may only change into an adjacent lane). Hence, structural approaches tend to provoke a large number of consistency constraints.

## 3.2.4. Behavioral object-orientation

Behavioral object-orientation of database systems has mostly originated from the programming area, with an attempt to extend programming languages in the direction of so-called persistent objects. Early approaches closely stuck to Smalltalk and, hence, are devoid of clustering concepts (see, e.g., [Maie86, Maie87]). More recent approaches adopt many of the ideas from Smalltalk but combine these with some clustering facilities (see, e.g., [Banc88, Bane87b, Woel87b]) or at least with the structuring facilities of classical database technology (see, e.g., [Stem88]). However, clustering is essentially restricted to assembling objects into sets so that much of the expressiveness provided by relationships is still missing. Since in all these cases object-orientation is dominated by the concepts introduced in ch. 3.1 the examples of figs. 3 and 4 carry directly over. Fig. 10 illustrates an augmentation by the part-of relationship.

## 3.2.5. Functional object-orientation

A middleground between structural and behavioral object-orientation is occupied by what one might call functional object-orientation. The essential ingredient missing from this approach is encapsulation. The approach uses objects, classes and functions as basic building blocks (see, e.g., [Fish87, Heil88]). Classes are described in terms of structural representation. They may be arranged in hierarchies, with a concomitant inheritance mechanism. Functions are defined in terms of classes but are treated as objects in their own right (note the influence of functional programming languages such as Lisp). For example, in fig. 3 the methods for automobile would (or could) be detached from the class automobile and maintained as separate objects. Since it is sometimes difficult to associate functions with just one class, or such an association is undesirable during the initial design phase, functional object-orientation is an interesting alternative. Its drawback is the lack of inheritance for methods.

## 3.2.6. Communication

As indicated before, until recently there has been no notion of agent in database systems. This seems to change now, with the concept of an active database system gaining wider interest. In contrast to the approach in programming, communication between objects is not based on message passing but on the mechanism of event sharing. The basic idea is as follows. Interaction is described by a set of event-condition-action rules. A procedure or method that wishes to delegate some activities raises an event (the method acts as an alerter). For all rules activated by this event the condition is evaluated. If the condition is satisfied the corresponding action is triggered (executed). Although this technique has long been known to information system design (see several papers in [Olle82]) it is fairly recent to database systems because of implementation problems (for examples, see, e.g., [Daya88a, Daya88b, Kotz88, Ston86a]).

3.3. Object-Orientation in Knowledge-Based Systems

## 3.3.1. Basic approaches

Knowledge-based systems are a fairly recent topic in computer science and are an outgrowth of much earlier artificial intelligence research in semantic networks and deductive question-answering. In short, knowledge-based systems allow to organize the combined explicit knowledge of experts on a given universe of discourse and, beyond retrieving the explicit knowledge, to extract implicit knowledge by means of an inference mechanism.

The general notion of object in the sense of modelling real-world phenomena, then, clearly applies to knowledge-based systems as well: Experts identify the entities of interest in the universe, and state facts and general rules about them. As in programming and in databases, however, an object is just a concept given by a name, and the real challenge is the proper organization of a collection of objects.

According to Mylopoulos ([Mylo84b]), knowledge representation considers the world as a collection of individuals and as a collection of relationships that exist between them. The collection of all individuals and relationships at any one time constitutes a state, and there can be state transformations that cause the creation and destruction of individuals, or that can change the relationship among them. Depending on whether the starting point for a representation scheme is individuals/relationships, true assertions about states, or state transformations, we have a network, logical or procedural scheme.

## 3.3.2. Unstructured representation

We first turn to the last two kinds of schemes. Logical representation schemes employ the notions of constant, variable, function, predicate, logical connective, and quantifier to represent assertions about states as logical formulas ([Mylo84b]). An important advantage of these schemes is the availability of inference rules in which one can define proof procedures for information retrieval, semantic constraint checking, and problem solving. Also, since these schemes restrict themselves to a single concept, they result in a uniform representation with, in general, clean, well-understood and well-accepted formal semantics. Thirdly, the mechanism is so general that it easily subsumes state characteristics such as classification, inheritance, clustering, general relationships, and others if so desired, and allows logical inferences on these by interpreting the statements as deduction rules. The archetype of this approach is Prolog ([Cloc84, Ster86], for a critical review see [Tich87]). A Prolog representation states facts about the problem area as a set of (somewhat restricted) logical axioms. The Prolog interpreter is a theorem prover that accepts a problem, formulated as a logical statement, and tries to find a constructive proof for it. If successful, the proof binds existentially quantified variables in the logical problem statement. The variable bindings are the desired results. Prolog queries are declarative in much the same way as modern database queries are, but their interpretation is much more powerful because it utilizes not just the information explicitly contained in the database but also the implicit one that is derivable from it.

The most serious drawback from an information management standpoint is that the approach is completely unstructured. The lack of organizational principles keeps structure from being imposed on the set of axioms so that a (flat) knowledge base of, say, several thousand axioms becomes unintelligible to a reader. Even the time-honored mechanism of typing objects cannot be applied (projects for a 'typed' Prolog are currently under way).

Procedural representation schemes view a knowledge base as a collection of active agents or processes ([Mylo84b). In doing so they deal with two issues: the activation mechanism offered for processes, and the control structures for them. As to the first issue, for example, a knowledge base contains assertions and a collection of demons that watch over it and are activated whenever the database is modified and searched. Activation is on the basis of patterns that are associated with the demons and are matched against the assertions. Pattern matching is also the basis for a second kind of approach based on production rules. Rules are tried out in some order until one is found whose pattern matches the database, and an associated action is then executed. The control structures have to do with the communication between rules, and with search and backtracking strategies. Again as a drawback, procedural schemes are difficult to understand and modify.

## 3.3.3. Structured representation

Structure, on the other hand, requires a certain number of distinctive concepts that allow to impose differentiation on an otherwise disorderly body of knowledge. Usually one strives for a set of concepts that facilitate clear graphical representations of knowledge. The concepts introduced in chs. 3.1 and 3.2 by and large met this requirement. Network representation schemes proceed along the same lines ([Mylo84b]). In its most basic form, a semantic network represents knowledge in terms of a collection of objects (nodes) and binary assertions (directed labelled edges), the former standing for individuals (or concepts of some sort), and the latter for binary relationships over these. Many of the concepts mentioned before such as classification, generalization, inheritance, or aggregation have, in fact, arisen in semantic networks earlier or at the same time as in the other disciplines (for a thorough review see [Brac79]).

These structured approaches have evolved into frame-based representation languages. Today's frame languages are the result of nearly twenty years of research in semantic nets. The terminology basically is as follows. A frame is a complex data structure for representing a stereotypical situation. The frame has slots for the objects that play a role in the stereotypical situation, as well as relations between these slots. Attached to each frame are different kinds of information such as how to use it, what to do if something unexpected happens, default values for slots. More technically speaking, a frame is nothing more than a record, i.e., a named collection of information. The record fields are called the slots. Slots have names and contain values. The values can be, for instance, symbols, lists, names of functions, sets of production rules, or links to other frames. The latter unidirectionally connect pairs of frames and correspond to the traditional relations. Frames thus may be viewed as a clustering mechanism, albeit a rudimentary one because it does little more than collecting relationships and, in particular, does not directly include a part-of concept.

What differentiates frame languages from database languages is inheritance. Inheritance is the notion of providing a frame with implicit slots and values that are obtained from other frames. The is-a relation are the paths over which these inherited items travel. Simple inheritance means that each frame can inherit via at most one path; multiple inheritance is the generalization to multiple paths. In the latter case rules must be provided to resolve conflicts and ambiguities.

What also distinguishes frame languages from database languages is that certain inference mechanisms can be associated with frames, and automatic classification of new objects may be provided. What distinguishes them from object-orientation in programming is that there is no clear notion of encapsulation and, since there are no agents, no notion of delegation. On the other hand, the inheritance concept is much more sophisticated, as we demonstrate below.

![](/api/attachments/67Z4SWRA/fulltext/images/f2ee6b16422a1d0491cb629211738062e5d0ea1b33cf78e68e22d47055892bd0.jpg)  
Fig. 7. Knowledge representation using KL-ONE. Explanations see text.

Fig. 7 graphically illustrates an example from our traffic analysis, with KL-ONE underlying as the frame language. Only slots (called roles in KL-ONE) that reflect relationships are shown (in the form of directed edges). The edges are labelled by role name, a value restriction (v/r) and a cardinality constraint. The solid black arrows reflect the is-a relationship. Roles are inherited along these arrows in a direction opposite to the arrow. The inheritance may be restricted. For example, a vehicle has one person as a driver or none at all, and may have between zero and eight occupants. A motor car inherits the roles subject to the restriction that only the owner may drive the car. An auto inherits the roles including this restriction, and may itself be subject to further restrictions. In the example, an auto may have only zero or one passenger in the front (excluding the driver), and between zero and three passengers in the back. Note that some of the semantics (such as a driver is an occupant but not a passenger) is not explicated in the structure.

Frame languages are not particularly useful if they are merely tools for representation, making just available operations such as to create and delete frames and slots dynamically, and to read and write the values in the slots. To utilize these languages in knowledge bases, existing inference mechanisms must be adapted to them or special ones must be developed.

## 3.3.4. Hybrid organizations

Clearly, for the purpose of object-oriented knowledge representation both the unstructured and the structured approaches have their merits, thus a combination of these seems desirable. Several modern knowledge programming systems and expert system development environments are indeed hybrid. An example for such a programming language is LOOPS ([Bobr81]). A general survey on programming with objects in Artificial Intelligence can be found in [Stef86]. Examples of environments are BABYLON ([DiPr85]) and KEE ([KEE86]).

## 3.4. Object-Orientation in Office Systems

## 3.4.1. Basic approaches

Office automation is a fairly recent development and as such had the fortune of being able to draw on the most modern concepts of computer science and system analysis methods and techniques. It is also a particularly attractive subject area because it combines a clear object-orientation with well-established office procedures. Depending on which aspects are given priority, the following approaches to the conceptual modelling of office information systems can be distinguished ([Barb85, Brac84]).

\- Data-based models. Their main purpose is to represent the office from the viewpoint of objects manipulated by office workers (agents), in a way similar to traditional offices where work is primarily based on documents. Thus, the main emphasis is placed on data; the basic elements are data types and data manipulation operations (storage, retrieval, manipulation, transmission); all office activities are modeled as operations on data. Generally, data are represented by forms which are similar to paper forms in the traditional office.

\- Process-based models. They analyze and describe office work by looking at different activities performed concurrently by the users and the system. The goal is to represent office activities in a coordinated way. Hence, the emphasis is on producing an integrated vision of all the activities that are performed in an office in order to execute certain tasks, and to describe the flow of control within office work, and the rules which must be satisfied by activities.

\- Agent-based models. The office is modeled from the viewpoint of the functions performed by active elements of the office environment (the agents). Such a model describes the office by associating with the different agents a set of functions: the different roles they take in performing their tasks, the domain within which they are authorized to act, and the set of relationships that link them to other agents.

This list exhibits many of the phenomena of object-orientation encountered before. Depending on the model preferred, the emphasis should be more on structural object-orientation (as in the case of data-based models), functional and behavioral object-orientation (as for agent-based models), or some sort of communication model based on events and flow control (as for process-based models), although any approach will have to incorporate elements of all three.

## 3.4.2. Modelling and programming concepts

Gibbs ([Gibb85]) points out the many similarities between the requirements of office modeling and semantic networks. In particular, he argues that modeling should be based on objects with properties (modeling, above all, documents), abstraction mechanisms (classification, aggregation, generalization, specialization), semantic integrity constraints (assertions). In addition, events and triggers should be provided in order to mirror agents and activities, since the office is considered to be largely event-driven. In [Gibb83] he gives an example of an object-oriented conceptual structure that encompasses many of the elements just discussed. Fig. 8 gives a graphical illustration. Nierstrasz ([Nier85]), in discussing the programming system Oz for implementing office systems, dwells on the suitability of the concepts of ch. 3.1 for office systems. He suggests to employ encapsulation, object behavior, classification, delegation, generalization, specialization and inheritance. Like Gibbs he also includes events and triggers among his programming concepts.

![](/api/attachments/67Z4SWRA/fulltext/images/d165905e019b9f754a0d2f5bd696f7f8b42455661ee88af4c2280cfc1ce8711c.jpg)  
Fig. 8. Graphical representation of an object-oriented description of an office that includes organizational aspects (department), agents (employee), customers (student), and various document media. Thin arrows identify external range of functions; solid arrows represent is-a relationships.

## 3.4.3. Database concepts

Many authors treat office system design as an extension of database design work. A typical example is the work of Woelk and others ([Woel86, Woel87a, Woel87b]) on multimedia databases, i.e., databases for text, sound, digitized images and vector graphics. Objects are documents in various (multimedia) forms including memos, scratchpads, notebooks, diagrams, images, voice; dossiers of documents, office equipment such as desks, waste baskets; agents; and activities. These may be visualized by, e.g., powerful user interfaces such as the one on the Apple Macintosh. It includes the structural aspects of clustering objects into larger ones (e.g., header, body, trailer, diagrams are all parts of a memo), generalization (is-a hierarchies), inheritance, historical evolution (version mechanism), typing, general relationships between objects. As another example, [Lyng84] distinguishes for the purpose of object management the following kinds of objects: descriptor objects that are solely identifiable by a string of characters; structural objects that model a relationship among several objects; behavioral objects that embody operations and are executable; text objects for variable-length character strings; image objects for digitized images for graphics devices; and audio objects for digitized voice. Several authors stress the importance of additional control elements and precedence relationships ([Barb85, Hora85, Lock88]).

## 4. Object-Orientation for Information Management

## 4.1. Object-Oriented Information System Design

We observe a close convergence of the concepts of object-orientation in all four areas we visited. We thus summarize. An object is some clearly identifiable entity in the universe of discourse. We may associate a certain structure with it that is due to properties, relationships to other objects, or clustering of subobjects. We may state assertions about objects. We may also confer a certain behavior on it in the form a set of operations that could be applied to the object, and encapsulate the object. We may establish delegation and communication between objects using messages, or events that trigger actions which in turn execute operations on objects. Objects are classified into types where a type determines the principal structure and behavior. Object types may be subtypes of more general types and inherit static and dynamic properties from these, perhaps under certain restrictions. Object-orientation does not prescribe what should be considered an object in a given situation and, in fact, even short-duration events may sometimes be usefully treated as objects.

Because of the convergence just mentioned one would expect information system design to profit from object-orientation as well. Of course it imposes a strict discipline on the design activities: Start by identifying the object types of interest in the universe, then use object-orientation as a framework within which to organize the knowledge on the information system. The question is whether there is a place in information system design for such an approach.

We may break the question down into a set of smaller questions:

\- At what stage in the design process could the approach be applied?

\- Does the approach come naturally to the designer?

\- Is any particular background needed to apply it profitably?

\- Are there any positive experiences?

If we follow the information life cycle in [Olle88], the design phase encompasses strategic study, information system planning, business analysis, system design, and construction design. The first stage is clearly non-technical in nature. The second stage determines the broad nature of the information requirements of an entire enterprise, what business objectives have been identified or should be identified for further work, whether there exists an information system strategy. This stage is again very global in character, with much emphasis on broad outlines and judgments rather than technical rigor. The third stage, business analysis, includes an analysis of the business activities performed in an area of interest irrespective of whether they are or are to be executed manually or by computer. The analysis of information flow in the organization and the associated analysis of material flow are both classical techniques. The next stage, system design, deals with components that are to be introduced into or changed in the information system, and augments them by those properties that were left open during business analysis. Typically, data design and process design are combined during this stage. The fifth stage, construction design, involves how the system is to be constructed, and requires a knowledge of the tools and resources to be used. Foremost among these are software development environments and database systems so that there is a natural tendency towards object-orientation.

Consequently, we face the situation that as we come along the design we move from statements of policy and goals, across crude prescriptions of the tasks to meet them, to an equitable consideration of processes and data, and finally to a data-based construction philosophy. It would appear, then, that system design and, to some extent, business analysis are prime candidates for object-oriented modeling.

Natural as it may seem, object-orientation does not even come easily to computer scientists if they have been exposed to the more classical control flow techniques over a longer time. On the other hand, object-orientation has allowed to introduce a level of semantic control into programming and databases that widely improved the quality of programs and data-intensive applications. Even though one should expect a fair amount of retraining of business analysts before they become comfortable with the rigors of object-orientation, similar benefits should accrue. Since there is no straightforward way to construct the control or process flow from the object design, techniques would have to be devised that allow to switch back and forth between control flow and object views, and to maintain consistency between the two (for first attempts in this direction see [Ober86]). Indeed, as shown in [Olle 88], there is already a certain amount of object-orientation in business analysis techniques. One may argue that similar considerations apply to system design since it basically calls for a refinement fo the results of business analysis. Gains in quality of the design could be expected if the same methods and techniques are used throughout both stages.

Judging from the literature, those most comfortable with object-orientation seem persons with a background in databases. Add to these the future graduates with backgrounds in modern programming techniques and in knowledge-based systems. Hence, there will be a new generation of analysts available to which object-oriented design techniques are no more alien; they will tend to push these techniques towards the earlier design stages.

An excellent though not altogether complete survey on information system design methodologies can be found in [Olle82]. Among the 13 methodologies discussed, roughly 7 may be classified as inherently object-oriented. Only one (USE) has strong elements of behavioral object-orientation. The remainder takes a structural approach, with generalization included but no inheritance rules, and sometimes with derivation rules, assertions and constraints added. Among them, a fair number superimpose a flow, event, function, or action structure in order to express some dynamics, but they do not directly associate these with the objects. Only two of the seven have gone beyond the research stage. To summarize, although to a degree object-orientation has entered into information system design, there seems to be as yet little practical experience with this approach.

## 4.2. Object-oriented information base management

Our goal was to exert a larger degree of semantic control on information processing in order to gain more confidence in its performance. Suppose now that the desired level of control has been formulated during information system design by following the paradigm of object-orientation. What we are looking for is an information base management system that will enforce this level of control or, in other words, that offers the corresponding object-oriented concepts. Clearly, because of the longevity of information in general, an essential component of such a system is a database management system. Therefore, we take a look at three more recent developments that extend database technology towards object-orientation: one that restricts itself to structural object-orientation, a second that includes elements of knowledge processing, and a third that emphasizes behavioral object-orientation. All of these developments still are experimental in nature, nonetheless they demonstrate that suitable support for object-oriented information management is not too far off.

## 4.2.1. Structural object orientation

An example of structural object-orientation is the complex-entity-relationship model (CERM) mentioned before, which has been realized in the DAMOKLES database system prototype ([Ditt 87a]). DAMOKLES has been developed as the basic information management component for a software engineering environment. CERM is an extended entity-relationship data model which, since it is no longer just a semantic framework, includes a full-fledged set of operators. The main structural features of CERM include the following:

\- molecular entities (called structured objects) which may be built recursively and which may also overlap (i.e., a subentity is part of two or more superentities),

\- versions of structured objects,

\- arbitrary n-ary relationships between objects of any structure or versions; cardinalities are supported.

Structured objects. CERM objects consist of a descriptive and a structural part. The descriptive part is composed of a number of attributes. One or more of these attributes may be designated to be the object key and as such must be unique within the set of current database objects of the respective type, at any point in time. The structural part reflects clustering, it includes a set of subobjects (perhaps with relationships among them) which, in turn, are objects in their own right and may again be structured. A simple CERM object, like records or tuples in classical data models, has only a descriptive part, a structured object also has a structural part. Take fig. 6. Position is a simple object which has four attributes. By contrast, automobile is a structured object whose two attributes id and max\_no\_passengers form the descriptive part whereas the simple objects shape and position together with the relationship has\_position between them determine the structural part: shape and position are its subobjects. Similarly, street\_geometry has lanes as its subobjects.

In the database schema, the descriptive part of an object is specified as usual by enumerating the desired attribute names and their associated value sets. For the structural part (if any) the type names of the desired subobjects are listed. As there are no further restrictions.

\- recursive objects may occur using their own object type within their structure,

\- structured objects need not always be simple hierarchies but may overlap in arbitrary ways.

(Fig. 6 does not contain examples of these two cases. However, one could very well imagine that lanes are not only part of superobject street\_geometry but also of a layout of a street intersection, resulting in an overlap of objects street\_geometry and street\_intersection.)

Instances of structured object types originate in two ways. First, an object of a subobject type may be created together with a given instance of (one of) its superobject types. Second, an existing subobject may dynamically be inserted into its superobject. Subobject removal and automatic subobject deletion upon superobject deletion are also supported. Operators for objects further include

\- locating in sequential order the objects of a given type,

– retrieval based on attribute values,

\- individual or joint attribute retrieval and modification,

\- navigation within structured objects to the next subobjects of a given type,

\- locating the next structured object in which a given object participates (remember that structured objects may overlap).

\- copying object attributes or entire objects.

Object versions. Object versions allow to represent multiple instances of the (semantically) same object. The main characteristics of the CERM version concept are as follows:

\- Versions are always associated with objects; more precisely, each version belongs to exactly one object, its generic object.

\- Both, the generic object as a whole and its individual versions, may have a descriptive and a structural part. Those of the generic object are inherited to all its versions, but each version may have additional attributes and subobjects of its own.

\- Generally, versions can be treated as objects in their own right.

\- Operators on versions sequentially locate versions in a version graph, locate the generic object of a given version, insert and remove a version into/from the version graph of a generic object.

Relationships. Relationships are n-place (n ≥ 1) bidirectional associations of objects. Each place is characterized by a role attribute, and relationships in their entirety may possess further attributes. Similar to objects, the database schema describes relationship types. As a consistency constraint the user may specify a minimum and a maximum cardinality for each role. It defines how often an object at least must or at most may participate in a role of a given relationship type. Relationship types in figure 6 are has\_position, in and adjacency. Cardinalities and role attributes are not shown. However, role attributes would be necessary for adjacency in order to distinguish which lane is to the right or left of a given lane, and cardinalities (0, 1) would have to be added to indicate that at most one lane may exist on either side of a given lane (fig. 7 shows further examples of cardinalities).

Relationships play a major part in defining clustering: like subobjects, they may be included in them. Obviously, objects of any level, generic objects and individual versions may all be used to define relationships. Thus all kinds of inter-object or intra-object associations may be defined, and a powerful set of operators (similar to those for objects) allows to exploit them.

## 4.2.2. Knowledge processing

Fig. 9 gives an example of a system architecture for processing a knowledge base for traffic analysis. This system (called EPEX for EPisode Extraction [Walt87]) has as its objective to extract from a sequence of images taken by a camera actions of a high semantic content (episodes) such as 'waiting for a streetcar', 'parking an automobile', or 'travelling from one direction to another'.

The system roughly works as follows. The general knowledge on the types, properties and constraints of objects to be observed are entered manually in the form of object classes into the object section. Also added manually are class hierarchies determining inheritance, relationships, and restrictions on these. An image processing system derives from the images the objects observed in the image scene, together with their attributes and trajectories (geometries scene description, GSD). These are stored in the object section of the database as object specimens. At present only moving objects are automatically recognized whereas still objects such as parking bays, traffic lanes, houses must be identified manually. Likewise, the classification of objects into classes is still is a manual endeavour. The object section is structurally represented using an extended KL-ONE notation; fig. 7 gave an example.

![](/api/attachments/67Z4SWRA/fulltext/images/f65654d17e3f1e8e7048b132cba0ab00aac91ca75b8d159b7df382a2c3c67cb9.jpg)  
Fig. 9. Architecture of the knowledge-based episode extraction system EPEX.

In order to derive episodes from the temporal sequence of object specimens, general knowledge on the kinds of expected episodes must be available. Consequently, there is a second, process section in the database. It includes a set of process classes that describe the various subprocesses from which an episode may be composed, alternative sequences of these subprocesses, which subprocesses are a mandatory part and which may occur optionally, and various constraints to be observed in order to recognize an episode as legal. For example, 'parking an automobile' has a fair number of variations, such as driving directly to the curb, or backing up to the curb, or turning into a parking lot; also there is a constraint that the car must not be moved for, say, two minutes or more because otherwise this would be construed as just stopping the car. Clearly, episode classes refer to object classes. One may treat episodes as objects, and give KL-ONE representations for episodes classes in the form of object classes. However, the representation is somewhat less natural due to a lack of direct concepts for clustering and variations.

Episode classes can be considered templates from which to construct individual episodes, by observing the object specimens that are individuals of the object classes referred to in the process classes. In other words, episode classes and sequences of object specimens are linked via the object classes in such a way that individual episodes are recognized. These may then be communicated to the user or stored as process specimens in the process section. The linking is done by inference. Consequently, rule knowledge is needed as a third component of the database. An interpreter accepts a .user query, selects appropriate rules and starts or controls the inference process.

Knowledge representation concepts are usually not considered data models that are to be supported by an information base management system. Hence, there does not yet exist a well-established set of operators on KL-ONE objects. Walter et al. ([Walt87]) introduce such a set in order to enter, modify, delete, and interrogate the object and process section of the EPEX information base.

## 4.2.3. Behavioral object orientation

Smalltalk-80 was one of the earliest and most promising behavioral object-oriented programming languages. As a consequence, it has served as a model to the development of behaviorally object-oriented database management systems. One such development is GemStone ([Maie86]). However, we briefly survey a second system, ORION ([Bane87b, Woel87]), since it extends the Smalltalk concepts by clustering, resulting in structured objects called composite objects.

In ORION, all conceptual entities are modeled as objects. An ordinary integer or string is as much an object as is a complex assembly of parts, such as an aircraft. Following the paradigm of encapsulation, an object consists of some private memory of instance variables that hold its state, and a set of methods that manipulate or return the state of an object. The domain of an instance variable is a class. Methods are part of the definition of the object. Objects communicate with one another through messages. A primitive object, such as an integer, only has a value, which is the object itself. Similar objects are grouped together into a class, and classes organized into class hierarchies. Inheritance involves the instance variables and methods specified for a class.

![](/api/attachments/67Z4SWRA/fulltext/images/bf6e1c0b0be0e6f5f3af666a18b0fbb8ccd01d867c95946a2d63e3588cf27c15.jpg)  
Fig. 10. Graphical illustration of a class lattice and a composite object schema schema in ORION.

In ORION a class can have more than one superclass, generalizing the class hierarchy to a lattice. In a class lattice, a class has multiple superclasses and thus inherits properties from each of the superclasses (multiple inheritance). Name conflicts between a class and its superclasses are resolved by giving precedence to the definition within the class over that in its superclasses. For example, in fig. 10 the weight of a submarine is the one in the definition of the class submarine. If an instance variable or a method with the same name appears in more than one superclass of a class C, the one chosen by default is that of the first of the (immediate) superclasses of C in the order specified by the application. For example, in fig. 10 the class submarine has to inherit its size either from the superclass water\_vehicle or from superclass nuclear\_powered\_vehicle (which inherited it from its superclass motorized\_vehicle). If in the definition of the class submarine, nuclear\_powered\_vehicle was specified as the first superclass, size will be inherited from it.

For clustering, ORION introduces the notion of composite object that captures the is-part-of relationship between an object and objects it references. A composite object has a single root object, and the root references multiple children objects, each through an instance variable. Each child object can in turn reference their own children objects, again through instance variables. A parent object exclusively owns children objects, and as such the existence of children objects is predicated on the existence of their parent. Children objects of an object are thus dependent objects. The instances that constitute a composite object belong to classes that are also organized as a hierarchy. This hierarchical collection of classes is called a composite object schema. It consists of a single root class and a number of dependent classes. Fig. 10 gives an example for root class vehicle.

## 4.3. Design Environments

It is well-accepted these days that the complexity of modern design methodologies and design concepts require sophisticated technical aids and automated support in order to safeguard the design against inconsistencies, to concentrate on partial problems, and to integrate partial solutions into a whole. Object-oriented information system design is no exception to this. In addition, however, and especially with the advent of object-oriented information management systems, tools should also provide automated transformation of designs into the appropriate database structures and operations, or database objects, so that the designer can almost exclusively concentrate on the conceptual design job as such.

According to a survey in [Lock86] what is fairly advanced today are editors – preferably graphical – that permit the building of designs in a stepwise fashion, do a good amount of semantic checking for, e.g. terminological conflicts, inconsistencies, ambiguous interpretations, redundancies, and may also guide the user's actions or suggest therapies for conflicts. Such editors could certainly be adapted to deal with object-oriented designs. Complete design environments of the functionality discussed before, however, are still the subject of research. We mention two.

## 4.3.1. Smalltalk-80

The beauty of Smalltalk-80 is that it comes complete with an interactive programming environment ([Gold84]). It relies on workstations with a high-resolution bitmapped display screen, a typewriter keyboard, and a pointing device (mouse). The display is used to present graphical and textual views of information in multiple windows. New actions are often indicated by selecting an option from a pop-up menu. Basically, the Smalltalk-80 system was the first one to introduce the techniques that have become the standard in today's workstations. Indeed, one should insist that information system design environments run with exactly the same type of system.

Programming in the Smalltalk-80 language consists of creating new classes, creating instances of classes, and specifying a sequence of message exchanges between all of these objects. Among the tools that support the programming process in the integrated environment are the following.

\- Text editor, form editor, and bit editor for editing text, drawing pictures, and creating pixel patterns, respectively.

\- Inspectors for examining and modifying the internal state of an object, and for support of testing new classes and messages added to the system. Inspectors are created by sending a corresponding message to the object in question.

\- System browsers give access to all the class descriptions available in the system, including comments about the classes, comments about the methods, and examples of how to use many of the classes. They also permit the modification of existing classes and the creation of new classes. Again, system browsers may be created on demand and associated with an object. One may thus obtain, e.g., system category browsers, class browsers, message category browsers, message browsers, class hierarchy browsers.

\- Message-set browsers determine which methods send a particular message, which classes implement a particular message, or which messages reference a particular variable.

\- Notifiers provide a simple description of an activity or process at the time that the activity was interrupted, e.g., on execution error or on purpose.

\- Debuggers allow to explore the methods associated with the interrupted activity, to make needed changes, and then to proceed. Notifiers and debuggers in tandem support the incremental testing of programs, and are again created dynamically.

\- Explanations. When displaying methods during browsing or debugging, tokens within the text may be selected, and an explanation about the corresponding syntactic or semantic part of the method may be requested.

\- Templates. Whenever the system knows something about the form in which information should be provided, a default solution (template) is provided. The user edits the templates, and thus need not remember the syntax.

\- Examples. Messages can be associated with classes that consist of examples of how to interact with instances of the class.

The Smalltalk-80 environment does not support mapping to databases, or database design. However, this appears more as a technical issue, since the concepts should easily extend to information system design. And indeed, the GemStone system mentioned before is a first attempt to extend Smalltalk into a database language, and to provide run-time database management support.

## 4.3.2. Taxis

The Taxis project ([Mylo84a]) is concerned with the development of languages, tools and methodologies for the design of interactive information systems. It is based on several premises:

\- The design of databases is an integral and inseparable part of the design of information systems and, hence, includes transactions, user interfaces etc. in order to cover all aspects of information system design, not just those dealing with the storage of data.

\- Information system design is the development of a model of the enduser's conceptual perception of the world. Information system development should then be much easier and more successful if it begins at the conceptual level.

\- Information systems are software and, hence, important precepts of software engineering are applicable to information system engineering.

The focus of the Taxis project is the Taxis programming language which supports the description of information systems at the conceptual level. In a nutshell, Taxis offers an entity-based framework and supports generalization, classification and aggregation as abstraction mechanisms. Its features include multiple inheritance of attributes, is-a hierarchies of transactions, metaclasses, typed attributes, a procedural exception-handling mechanism, and an iteration construct based on the abstraction mechanisms supported.

In a little more detail, Taxis provides for the description of the entities of the world and their interrelationships through the notions of objects, related by properties/attributes. Individual objects are organized into classes which describe commonalities of their instances in the form of constraints, e.g., properties applicable to them, the valid ranges of values of such properties. Classes themselves are objects and, hence, can be members of meta-classes; therefore, classes can have their own properties. Furthermore, classes are organized into a hierarchy, with general classes located above their specializations. An important consequence of this organization is that properties can be inherited from superclass to subclass.

In addition to modeling data, Taxis supports the development of information systems by providing language features to model the activities in the world. For short-term activities, Taxis provides the notion of transaction as the basic unit of integrity and recovery maintenance. A transaction (essentially a procedure or function) consists of an initial group of preconditions which check the applicability of the operation at this point, followed by a sequence of actions described in traditional procedural notation, and concludes with postconditions. Transactions are themselves treated as objects. Taxis does not use encapsulation because transactions are not directly associated with the objects but are maintained in separate classes. By typing the transaction parameters with the corresponding classes, the same degree of semantic control can be achieved, though. Advantages are that transaction classes can be declared, and new operations can more easily be added.

To model persistent activities, e.g., activities with prolonged duration such as attending university, Taxis supports the notion of scripts. A script is built around a Petri-net skeleton of states connected by transition arcs, which are augmented by condition-action rule pairs. Finally, an extension of Taxis allows designers to describe user interfaces to information systems, e.g., the query language, in the same uniform framework of objects with properties in classes. Such an extension permits a direct link to be established between the referring expressions used in the query and their referents in the database.

Taxis draws its name from taxonomic programming, or stepwise refinement by specialization. Generalization is the appropriate principle to exploit when the difficulty of modeling is due to a large number of details rather than algorithmic complexity; a hierarchy of classes organized along this dimension guides the attention of the designer, and provides a convenient structure for distributing information and associating it where it most naturally belongs. We note that the same argument holds for other design environments such as Smalltalk-80.

An interactive environment for creating and trying out Taxis programs includes a class-oriented editor whose commands and functionality are centered on Taxis classes; a semantic consistency verifier which ensures that Taxis programs conform to the semantic rules of Taxis; an interpreter for simulating execution of Taxis programs; and a debugger for assisting the designer in validating the model. The design environment also provides various other aids to the user such as an online help facility, a documentation generator, and a way of keeping track of multiple versions of models.

The environment provides aids for some design automation. For example, a compiler for Taxis programs has been implemented ([Nixo87]). Its premise is that the conceptual schema must not only be checked for a certain syntactic and semantic well-formedness of definitions and expressions, but must also be available during runtime when expressions might require retrieval with respect to the conceptual schema rather than the database. The target language for the compiler is Pascal augmented with relational database facilities. Taxis data hierarchies are translated into relational schemata, and hierarchies of transactions are translated into the block structure of Pascal. The output of the compiler is a program containing definitions of all classes and transactions, routines to enforce constraints, a database interface, and a near-empty database.

## 5. Conclusions

The central premise of this paper has been that object-oriented information management gives coherence to the information system life cycle, especially system design, construction design, system operation and maintenance; that it adds to the design and operation a degree of semantic control that exceeds what has been available so far; and that there are modern developments in design aids and data management facilities that promise particularly efficient support. Fortunately, as the examples in the paper drawn from computer science, information management systems and design environments have shown, a consensus seems to evolve on what an object is or at least what its technical aspects are, so that a rich body of experience can be drawn upon.

Object-orientation in information system design is but one of a large number of design methodologies. It is certainly not sufficient to claim that object-orientation is competitive or has a distinctive role in design – one must prove it empirically. The structural and semantic richness and complexity of concepts associated with the notion of object could easily become a barrier to widespread use. Also, as pointed out before, object-orientation has its place more in the later design stages where there must be a way of complementing it by dynamic considerations such as flow of control, analysis of transactions and causal dependencies. An interesting topic for further research (and dealt with by some current research) is combining dynamic analysis methods with object-orientation.

The strong point of object-orientation is that modern database technology places heavy emphasis on it. This is reflected both in appropriate data models and in special implementation techniques that guarantee a much more efficient retrieval and update of objects than in today's database systems. Consequently, a design methodology that results in information description in terms of objects makes for a much easier or even straightforward mapping of this information to database management, and a system performance that is tuned to the particular information system application.

Finally, some of the most promising developments in information system design environments are predicated on object-orientation. Design methodologies that emphasize object-orientation could thus benefit from parallel developments or ready availability of modern, comfortable-to-use, computer-based information system development environments. Add to this the rapid evolution of knowledge-based systems with the concomitant development of knowledge acquisition environments and expert system shells.

In summary, the benefits available in the near future should make it highly rewarding to explore in more depth object-oriented information system design methodologies and their applicability to the information system life cycle.

## References

[Agha87] G. Agha, C. Hewitt: Actors: A Conceptual Foundation for Concurrent Object-Oriented Programming. In [Shri87], 49–74

[Atwo85] T.M. Atwood: An Object-Oriented DBMS for Design Support Applications. Proc. IEEE Compint 1985, 299–307

[Banc88] F. Bancilhon, G. Barbedette, V. Benzaken, C. Delobel, S. Gamerman, C. Lecluse, P. Pfeffer, P. Richard, F. Velez: The Design and Implementation of $O_{2}$ , an Object-Oriented Database System. In [Ditt88], 1–22

[Bane87a] J. Banerjee, H.-T. Chou, J. Garza, W. Kim, D. Woelk, N. Ballou, H.J. Kim: Data Model Issues for

Object-Oriented Applications. ACM Trans. on Office Info. Syst. 5 (1987), 3–26

[Bane87b] J. Banerjee, W. Kim, H.-J. Kim, H.F. Korth: Semantics and Implementation of Schema Evolution in Object-Oriented Databases, Proc. ACM SIGMOD 1987, 311–322

[Barb85] F. Barbic, S. Ceri, G. Bracchi, P. Mostacci: Modeling and Integrating Procedures in Office Information System Design. Information Systems 10 (1985), 149–168

[Bato84] D.S. Batory, A.P. Buchmann: Molecular Objects, Abstract Data Types, and Data Models: A Framework, Proc. 10th Internatl. VLDB Conf. 1984, 172–184

[Beec87] D. Beech: Groundwork for an Object Database Model. In [Shri87], 317–354

[Bobr81] D.G. Bobrow, M. Stefik: The LOOPS Manual. Tech. Rep. KB-VLSI-81-13, Xerox Palo Alto Research Center, 1981

[Brac79] R.J. Brachman: On the Epistemological Status of Semantic Networks. In N.V. Findler (ed): Associative Networks: Representation and Use of Knowledge by Computers. Academic Press 1979, 3–50

[Brac84] G. Bracchi, B. Pernici: The Design Requirements of Office Systems. ACM Trans. Office Info. Syst. 2 (1984), 151–170

[Card84] L. Cardelli: The Semantics of Multiple Inheritance. Proc. Conf. on the Semantics of Datatypes. Lect. Notes Comp. Science, Springer 1984, 51–66

[Card85] L. Cardelli, P. Wegner: On Understanding Types, Data Abstraction, and Polymorphism. ACM Computing Surv. 17 (1985), 471–522

[Care88] M.J. Carey, D.J. DeWitt, S.L. Vandenberg: A Data Model and Query Language for EXODUS. Proc. ACM SIGMOD Conf. 1988, 413–423

[Cloc84] W.F. Clocksin, C.S. Mellish: Programming in Prolog. 2nd ed., Springer 1984

[Dada86] P. Dadam, K. Küspert, F. Andersen, H. Blanken, R. Erbe, J. Günauer, V. Lum. P. Pistor, G. Walch: A DBMS Prototype to Support Extended NF2-Relations: An Integrated View on Flat Tables and Hierarchies. Proc. ACM SIGMOD Conf. 1986, 356–367

[Daya86] U. Dayal, J.M. Smith: PROBE: A Knowledge-Oriented Database Management System. In: M.L. Brodie, J. Mylopoulos (eds.): On Knowledge Base Management Systems. Springer 1986, 227–258

[Daya88a] U. Dayal: Active Database Management Systems. Proc. 3rd Internatl. Conf. on Data and Knowledge Bases, Morgan-Kaufman 1988, 150–169

[Daya88b] U. Dayal, A.P. Buchmann, D.R. McCarthy: Rules are Objects Too: A Knowledge Model for an Active, Object-Oriented Database System. In [Ditt88], 129–143

[DiPr85] F. Di Primio, G. Brewka: BABYLON: Kernel System of an Integrated Environment for Expert System Development and Operation. Proc. 5th Internatl. Workshop for Expert Syst. and Their Applications, 1985

[Ditt86] K.R. Dittrich, U. Dayal (eds.): Proc. 1986 International Workshop on Object-Oriented Database Systems. IEEE Computer Society Press, 1986

[Ditt87a] K.R. Dittrich, W. Gotthard, P.C. Lockemann: DAMOKLES - A Database System for Software Engineering Environments. Lecture Notes on Comp. Science 244, Springer 1987, 421-440

[Ditt87b] K.R. Dittrich, W. Gotthard. P.C. Lockemann: Complex Entities for Engineering Applications. Proc. 5th ER Conference, 59–78

[Ditt88] K.R. Dittrich (ed.): Advances in Object-Oriented Database Systems. Lect. Notes in Comp. Science 334, Springer 1988

[Fish87] D.H. Fishman, D. Beech, H.P. Cate, E.C. Chow, T. Connors, J.W. Davis, N. Derrett, C.G. Hoch, W. Kent, P. Lyngbaek, B. Mahbod, M.A. Neimat, T.A. Ryan, M.C. Shan: Iris: An Object-Oriented Database Management System. Proc. ACM Trans. on Office Info. Syst. 5 (1987), 448–469

[Gibb83] S. Gibbs, D. Tsichritzis: A Data Modeling Approach for Office Information Systems. ACM Trans. Office Info. Syst. 1 (1983), 299–319

[Gibb85] S.J. Gibbs: Conceptual Modelling and Office Information Systems. In D. Tsichritzis (ed.): Office Automation, Springer 1985, 193–225.

[Gold83] A. Goldberg, D. Robson: Smalltalk-80, The Language and Its Implementation. Addison-Wesley, 1983

[Gold84] A. Goldberg: Smalltalk-80, The Interactive Programming Environment. Addison-Wesley, 1984

[Hail87] B. Hailpern, V. Nguyen: A Model for Object-Based Inheritance. In [Shri87]. 147–164

[Härd87] T. Härder, K. Meyer-Wegener, W. Mitschang, A. Sikeler: PRIMA - a DBMS Prototype Supporting Engineering Applications. Proc. 13th Internatl. VLDB Conf. 1987, 433-441

[Heil88] S. Heiler, S. Zdonik: Views, Data Abstraction, and Inheritance in the FUGUE Data Model. In [Ditt88], 225–241

[Hora85] W. Horak: Office Document Architecture and Office Document Interchange Formats: Current Status of International Standardization. Computer 18 (1985), no. 10, 50–60

[KEE86] KEE Software Development System User's Manual, KEE Version 3.0. Intellicorp, Mountain View, CA 1986

[Kemp87] A. Kemper, P.C. Lockemann, M. Wallrath: An Object-Oriented Database System for Engineering Applications. Proc. ACM SIGMOD Conf. 1987, 299–311

[Kotz88] A.M. Kotz, K.R. Dittrich, J.A. Mülle: Supporting Semantical Rules by a Generalized Event/Trigger Mechanism. EDBT '88, Lecture Notes in Comp. Science 303, Springer 1988, 76–91

[Kim87] W. Kim, H.-T. Chou, J. Banerjee: Operations and Implementation of Complex Objects. Proc. 3rd Internatl. Conf. on Data Engng. 1987, 626–633

[Lec188] C. Lecluse, P. Richard, F. Velez: $O_{2}$ , An Object-Oriented Data Model. Proc. ACM SIGMOD Conf. 1988, 424–433

[Lieb86] H. Lieberman: Using Prototypical Objects to Implement Shared Behavior in Object Oriented Systems. ACM Conf. on Object-Oriented Programming Systems, Languages and Applications 1986, 214–223

[Lock86] P.C. Lockemann, H.C. Mayr: Information System Design: Techniques and Software Support. Information Processing 86, North-Holland 1986, 617–634

[Lock88] P.C. Lockemann: Multimedia Databases: Paradigm, Architecture, Survey and Issues, Univ. Karlsruhe, Fak. f. Informatik 1988, Tech. Rep.

[Lori85] R. Lorie, W. Kim, D. McNabb, W. Plouffe, A. Meier: Supporting Complex Objects in a Relational System for Engineering Databases. In: W. Kim, D. Reiner, D. Batory (eds.): Query Processing in Database Systems, Springer 1985

[Lyng84] P. Lyngbaek, D. McLeod: Object Management in Distributed Information Systems. ACM Trans. Office Info. Syst. 2 (1984), 96–122

[Maie86] D. Maier, J. Stein, A. Otis, A. Purdy: Development of an Object-Oriented DBMS. In [Ditt86], 472–482

[Maie87] D. Maier, J. Stein: Development and Implementation of an Object-Oriented DBMS. In [Shri87], 355–392

[Mylo84a] J. Mylopoulos, A. Borgida, S. Greenspan, H.K.T. Wong: Information System Design at the Conceptual Level - The Taxis Project. Database Engineering 7, No. 4, 1984, 4–9

[Mylo84b] J. Mylopoulos, H.J. Levesque: An Overview of Knowledge Representation. In M.L. Brodie, J. Mylopoulos, J.W. Schmidt (eds.): On Conceptual Modelling, Springer 1984, 3–17

[Nier85] O.M. Nierstrasz: An Object-Oriented System. In D. Tsichritzis (ed.): Office Automation, Springer 1985, 167–189

[Nixo87] B. Nixon, L. Chung, D. Lauzon, A. Borgida, J. Mylopoulos, M. Stanley: Implementation of a Compiler for a Semantic Data Model: Experiences with Taxis. Proc. ACM SIGMOD 1987, 118–131

[Ober86] A. Oberweis, F. Schönthaler, G. Lausen, W. Stucky: Net Based Conceptual Modelling and Rapid Prototyping with INCOME. Proc. 3rd Conf. Software Engineering, AFCET, Paris 1986, 165–176

[Olle82] T.W. Olle, H.G. Sol, A.A. Verrijn-Stuart (eds): Information System Design Methodologies - A Comparative Review. North-Holland 1982

[Olle88] T.W. Olle, J. Hagelstein, I.G. Macdonald, C. Rolland, H.G. Sol, F.J.M. van Assche, A.A. Verrijn-Stuart: Information Systems Methodologies - A Framework for Understanding. Addison-Wesley 1988

[Ossh87] H.L. Ossher: A Mechanism for Specifying the

Structure of Large, Layered Systems. In [Shri87], 219–252

[Sche86] H.-J. Schek, M.H. Scholl: The Relational Model with Relation-Valued Attributes. Information Systems 11 (1986), 137–147

[Shri87] B. Shriver, P. Wegner (eds.): Research Directions in Object-Oriented Programming. The MIT Press Series in Computer Systems 1987

[Skar87] A.H. Skarra, S.B. Zdonik: Type Evolution in an Object-Oriented Database. In [Shri87], 393–415

[Stef86] M. Stefik, D.G. Bobrow: Object-Oriented Programming: Themes and Variations. The AI Magazine, Winter 1986, 40–62

[Stem88] D. Stemple, A. Socorro, T. Sheard: Formalizing Objects for Databases using ADABTPL. In [Ditt88], 110–128

[Ster86] L. Sterling, E. Shapiro: The Art of Prolog. MIT Press 1986

[Ston86a] M. Stonebraker: Triggers and Inference in Database Systems. In: M.L. Brodie, J. Mylopoulos (eds.): On Knowledge Base Management Systems. Springer 1986, 297–314

[Ston86b] M. Stonebraker, L. Rowe: The Design of POST-GRES. Proc. ACM SIGMOD Conf. 1986, 340–355

[Ston87] M. Stonebraker, J. Anton, E. Hanson: Extending a Database System with Procedures. ACM Trans. on Database Syst. 12 (1987), 350–376

[Tich87] W.F. Tichy: What Can Software Engineers Learn from Artificial Intelligence? Int. Rep. 14/87, Fak. f. Informatik, Univ. Karlsruhe 1987

[Walt87] I. Walter, P.C. Lockemann, H.-H. Nagel: Database Support for Knowledge-Based Image Evaluation. Proc. 13th Internatl. VLDB Conf. 1987, 3–11

[Wegn87] P. Wegner: The Object-Oriented Classification Paradigm. In [Shri87], 479–560

[Woel86] D. Woelk, W. Kim, W. Luther: An Object-Oriented Approach to Multimedia Databases. Proc. ACM SIGMOD 1986, 311–325

[Woel87a] D. Woelk, W. Luther, W. Kim: Multimedia Applications and Database Requirements. Proc. IEEE Comp. Soc. Office Automation Symp. 1987, IEEE Comp. Soc. Press 1987, 180–189

[Woel87b] D. Woelk, W. Kim: Multimedia Information Management in an Object-Oriented Database System. Proc. 13th Internatl. VLDB Conf. 1987, 319–329
