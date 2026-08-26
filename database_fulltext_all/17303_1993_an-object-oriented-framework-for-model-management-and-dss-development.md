---
otero_id: 17303
otero_key: "6QG5CPZH"
title: "An object-oriented framework for model management and DSS development"
authors: "Waleed A. Muhanna"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90013-s"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An object-oriented framework for model management and DSS development \*

Waleed A. Muhanna

The Ohio State University, Columbus, OH, USA

Through various studies, a number of model management (MM) issues have been addressed in the literature. There is a need to consolidate the various proposals and the different interpretations of the notion of a model. Towards this end, this paper proposes an object-oriented framework which provides a unifying context for MM research and DSS development. The framework coherently integrates Geoffrion's structured modeling together with Muhanna and Pick's systems approach, thereby offering a methodology for both modeling-in-the-small as well as modeling-in-the-large. Further, we argue that an overall object-oriented approach can significantly contribute towards the integration of model management, data management, software engineering, and artificial intelligence.

Keywords: Model management, DSS development, Object-oriented systems, Structured modeling

![](/api/attachments/6QG5CPZH/fulltext/images/11519856dab1f39535a05e91a55d77215dbc823cf2913169d18384092234a944.jpg)

Waleed A. Muhanna is an Assistant Professor of Information Systems at The Ohio State University. He received the B.S. degree (with University Honors) in computer science from the University of Tulsa in 1981, and the M.S. degree in computer science and Ph.D. degree in management information systems in 1985 and 1987, respectively, from the University of Wisconsin–Madison. His current research interests are in the areas of distributed computing systems, deci

sion support systems, model and database management systems, scheduling, and performance modeling. His work has been published in IEEE Transactions on Software Engineering and ACM Transactions on Computer Systems. He is a member of TIMS, ORSA, ACM, and IEEE.

## 1. Introduction

During the past decade, the topic of Model Management (MM) has emerged as an important area of research. Much of the pioneering work in MM viewed a Model management System (MMS) as a component of a Decision Support System (DSS) [2-4,13,15,27,28,43,45,48,53]. Increasingly, however, a broader view is being advocated [11,12,14,16,30,31,34,36,37,49]. From this perspective, a MMS is viewed as an independent system with value beyond its traditional role and function in a specific DSS.

Indeed, interest in computer-based modeling and related supporting tools predates the emergence of the DSS field. Moreover, there is increasing realization that the support of modeling-related activities is an ongoing need that goes beyond the development of any specific DSS. Underlying this broad view of MM is the philosophy that: (1) Models, like data, constitute an organizational resource that should be managed as such. Furthermore, this resource, like any other resource, should be viewed from an organizational perspective and not within the context of a particular application or a specific subfunction within an organization; and (2) It is crucial to view modeling within an organization as an ongoing, cumulative set of activities that should be managed, integrated, and coordinated in order to avoid wasteful duplication, excessive cost, inconsistencies, and suboptimal decisions.

While different authors view the focus and functions of a MMS differently, most would agree with the general statement that a MMS is a software system which facilitates the development, storage, manipulation, control and effective utilization of models in an organization. Model development activities include problem elicitation, modeling selection, model formulation, model validation, and model verification. The model storage function concerns model representation, logical view, and physical storage. Model manipulation tasks include model retrieval, model synthesis and integration, model instantiation, and model sequencing and execution. Model control functions include configuration and evolution management, authorization control, and consistency and integrity maintenance. In other words, an effective MMS seeks to provide support for the various phases in the modeling life-cycle, forming the foundation for an integrated modeling support environment whose aim is to increase the productivities of decision makers, modeling experts, and DSS developers.

Various frameworks for MM have been proposed in recent years. These include frameworks based on relational database theory $[2]$ , FOPC $[4,13,43]$ , frames $[11]$ , conceptual graphs $[14,16,28]$ , and systems theory $[36,37,40]$ . This remarkable degree of diversity stems from the fact that the discipline of model management is relatively new, and researchers have varying focus regarding the role and function of a model management system. All these proposals are meritorious having each contributed in some way to our understanding of the problems, issues, and possible solutions to the problems of MM. However, none of these frameworks address the entire set of phases in the modeling life-cycle. For instance, the issues of model sharing, control, and evolution management, which are at the heart of MM, are dealt with only in a small subset of the proposals, notably, $[11]$ and $[40]$ .

Some proposals appear to be driven by implementation issues, while others are almost exclusively concerned with the issue of model representation. This explains, as Holsapple and Whinston [21] observed, the different conceptions in the literature regarding the notion of a 'model'. For instance, classical DSS literature treats models as computerized procedures to be managed [4,5,48]. A second view of models, which is particularly reflected in proposals based on AI knowledge representation schemes, treats them as problem statements [11,14,16]. Models have also been treated as data that are to be analyzed or input to solvers [25]. Yet another interpretation of the model notion is presented in [36,37], where models are viewed as systems (or 'glass boxes') which encapsulate their state and behavior and present well-defined interfaces to their outside environment.

It has been suggested that these different interpretations of the model notion reflect views at different levels of abstractions, from user-oriented to execution-oriented [29]. Regardless of the nomenclature, however, it should be clear that these different views usefully complement each other since all are relevant in the MM field. In light of this remark, we believe that a generic framework that embraces them all can offer a unifying context for research and development in the MM and DSS development areas. The Object-Oriented framework proposed in this paper is an effort towards that end.

While object-oriented concepts and systems have their roots in programming languages [42], this author feels that an object-oriented framework is well-suited for overall MM and DSS development. The framework permits us to uniformly treat entities in the environment as object. These entities could be users, concepts, models, subroutines, and even windows in a user interface. It should be noted, however, that the uniformity of treatment does not preclude keeping the important distinction between the notions of a 'model' as an abstraction of reality, the 'problem' or system one poses in terms of the model, and the 'solvers' used to solve the problem or emulate the behavior of the system [16]. Rather, objects reflects a 'natural' view of the world we are modeling (abstracting) in our databases, software, and, of course, in our analytical and simulation models.

Object-oriented concepts and technology are on the leading edge of programming language and database systems research, and their usefulness in those contexts have been successfully demonstrated elsewhere $[22]$ . The focus of this paper will therefore be on showing how object-oriented concepts can be refined and augmented with additional concepts and capabilities to represent models and capture the semantics of the modeling process in a modeling environment. In so doing, we find it useful to distinguish between issues and methodologies related to ‘modeling-in-the-small’ and those related to ‘modeling-in-the-large’.

Modeling in the small focuses on the conceptualization, formulation, representation, and validation of an individual model for a given decision making objective. With the exception of Geoffrion structured modeling formalism [16], most efforts in this area tended to be domain or paradigm specific (e.g., modeling languages [10,52], model analysis systems [19], and LP formulation assistants [24,41,44]).

Modeling in the large primarily concerns itself with the ongoing use of models as organizational assets. In the large, we focus on the organization and administration of model bases, and on model synthesis from existing reusable components, model-data linkage, solver integration, and model evolution and configuration management.

If we classify work in the area of modeling systems on the basis of the above dichotomy, two approaches stand out: Geoffrion's structured modeling [16], and Muhanna and Pick's systems framework [36,37]. The former furnishes a solid, domain-independent foundation for modeling-in-the-small, while the latter provides a sound, general framework for modeling-in-the-large. We contend that both are in spirit 'object-oriented'. And as such, our proposed object-oriented framework synergistically embraces both approaches, while at the same time providing the strongest evidence for the feasibility of integrating analytical modeling with both databases and application software.

The remainder of this paper is structured as follows: Section 2 provides further background discussion and motivation. Section 3 outlines core object-oriented concepts as manifested in various object-oriented programming languages and database systems. Section 4 discusses how structured models can be represented using object-oriented concepts. Section 5 shows how to augment the core object-oriented concepts with additional structuring principles from the systems framework (e.g., composite models and versions) so as to capture more of the semantics in a MM context. Section 5 also discusses how to integrate structured modeling concepts with the concepts from the systems framework within an overall object-oriented approach. Section 6 outlines our implementation efforts. Finally, a summary and conclusion is presented in Section 7.

## 2. Background and motivation

Object-oriented concepts and technology appear to be a natural basis for MM and DSS development environments. In object-oriented systems, all ‘real world’ entities (both concrete and abstract) are modeled as objects. Indeed, the first appearance of the notion of object as a conceptual and programming construct was in Simula, a language for programming simulation models [1].

The advantages of the object-oriented approach are well known $[9,22]$ . The fundamental idea behind the object-oriented approach is that of encapsulation: object-oriented systems exploit encapsulation in various interesting ways in an attempt to enhance productivities $[42]$ . For example, object-oriented approaches: (1) encourage the use of ‘modern’ software engineering principles (e.g., decomposition and step-wise refinement, information hiding, and data abstraction); (2) promote and facilitate reusability $[32]$ through mechanisms such as class inheritance; and (3) can, when done well, endow a system with maintainability, extensibility, and interoperability.

The application of object-oriented concepts is no longer limited to the realm of programming languages. Today, we are finding that object-oriented technology is useful not only for programming simulation models, but for data modeling $[54]$ , information systems analysis $[8]$ , information systems design $[6]$ , as well as prototyping and application development $[9,33,50]$ . Though exciting, this evolution should not (perhaps with the benefit of hindsight) be particularly surprising since there is a great deal of evidence indicating that it is easier for many people to view the ‘real world’ in terms of objects. In fact, AI knowledge representation schemes (e.g., semantic networks $[7]$ and frames $[35]$ ) frequently discuss knowledge in terms of ‘objects’. Interestingly also, semantic data models (e.g., SDM $[20]$ ) are often cited as the immediate precursors to object-oriented database systems (OODBSs).

This evolution suggests another important advantage of the object-oriented framework: it addresses a central issue in MM research, namely integration. Geoffrion [17] distinguishes between three types of integration: model integration, solver integration, and integration of various utilities. He further notes that there are four levels across which model integration can occur: specific models, model classes, modeling paradigms, and discipline-specific modeling traditions.

The foregoing trend in broad application of object-oriented technology indicates that the generality of object-oriented concepts and structuring principles can significantly contribute towards coherently integrating the disciplines of database management, programming languages, software engineering, artificial intelligence, and management science (or operations research). At least, an object-oriented framework provides what seems to be the strongest evidence yet for the feasibility of not only model integration at all levels, but (as we shall see in Section 5) also solver integration. With the addition of the fact that object-oriented approaches have been proven useful in designing and building graphical user interfaces [46,51], this suggests that a unifying object-oriented framework is particularly well-suited not only for MM but also for DSS development.

## 3. Core object-oriented concepts

Despite considerable effort in this area, there is still no consensus regarding what constitutes an object-oriented system $[23,42]$ . For the purposes of this paper, an object-oriented system is considered to have the following characteristics: data abstraction/encapsulation; inheritance of properties, and persistency of objects. In this section, we briefly review core object-oriented concepts, which have been refined to suit this context. Subsequent sections show how we have extended these concepts to more fully capture the semantics of a modeling or DSS development environment.

Objects. In object-oriented systems, all entities (both conceptual or concrete) are uniformly modeled as objects. Each object has a state, which is made up of values for a collection of attributes (instance variables), and behavior, which is represented by methods for accessing and manipulating the state. Objects communicate by passing messages. The state and behavior encapsulated in an object can only be accessed by 'sending' messages to that object. The object itself then selects a corresponding method to execute the message received. These messages therefore constitute the public interface of an object. Also, associated with each object is a system-wide, unique identifier.

Classes. A class is an object which is used to create instances, where an instance is a specific thing or characteristic. More precisely, a class is a template, description, pattern, or 'blueprint' for a category of very similar items. Objects that belong to a class are called instances of that class. As such, the concept of a class captures the important semantic data-modeling concept called the instance-of relationship. To allow uniformity in handling messages, both classes and instances are normally viewed as objects. This way, an instance of a class could be created by sending a message to the class object.

Inheritance and Class Hierarchy. Inheritance is a reusability mechanism whereby a subclass acquires (shares) properties (attributes and methods) from its immediate superclass, and, by induction, from all of its antecedent superclasses. A class hierarchy arises when one restricts the number of superclasses a class can have to one. (If this restriction is relaxed to allow multiple inheritance, the result is a directed acyclic graph.) A class hierarchy captures the generalization (IS-A) relationship [47] between one class and a set of classes specialized from it.

Composite Classes and Class-Composition Hierarchy. Associated with each attribute of a class is a domain defining the values which that attribute may assume. The domain of an attribute may be any class: primitive or user-defined. A primitive class is one which has associated instances but no attributes (e.g., integer, string, and boolean classes). Often, a user-defined class is composite, in the sense that it has attributes each of whose domain is some arbitrary class. This permits nested definition of a class, which can be depicted by a directed acyclic graph of classes rooted at that class. This graph captures the aggregation relationship [47] between a class and its attributes, and gives rise to a class-composition hierarchy. For example, a composite class called VEHICLE may have an attribute called Engine whose domain is the ENGINE class. A class-composition hierarchy can also be used to represent the IS-PART-OF relationship, if instances of any composite class are not allowed to have (i.e., reference in their attributes) common objects as components.

## 4. Object-oriented representation of structured models

Geoffrion's structured modeling [16] provides a formalism for model specification in which the structure and semantics of models are represented as hierarchically organized, acyclic, attributed graphs. In what follows, we present an object-oriented view of structured models. Lenard [26] was first in noting that structured modeling has a lot in common with the popular 'object-oriented programming paradigm'. We present a more general and complete view in this section.

Due to its generality, the object-oriented framework seems to be at least as semantically rich as SML $[18]$ and attributed graphs notational styles for structured modeling. As such, object-oriented concepts and notations could be used to both think about and represent structured models, within an overall object-oriented framework for MM. To show this, it is presumed (by necessity) that the reader is familiar with basic structured modeling concepts $[16,18]$ .

Structured modeling formalizes the notion of a definitional system as a way of describing models. This is precisely what the object-oriented concept of a class and the class-composition graphs formalize. Using structured modeling terminology, a structured model consists of: (a) an element structure; together with (b) a generic structure; and (c) a monotone modular structure. There are five types of elements: primitive entities, compound entities, attributes, functions, and tests.

One way to represent a structured model, using object-oriented concepts, would be as follows: each grouping of similar elements (genus) is represented by a composite class. For example, a function element genus can be represented by a composite class having a method corresponding to the generic rule, plus the following attributes: an interpretation attribute whose domain is the primitive class string, and one attribute for each element in the generic calling sequence such that the domain of that attribute is the class representing that element. Other types of genera can be represented in a similar manner. This hierarchical class composition gives rise to an acyclic class-composition graph which corresponds with the genus graph of a structured model. Nodes in this graph are instantiated to represent the elemental graph for a specific model.

Taking this class composition process one step further, we aggregate (i.e., group) the classes (which correspond to genera) into higher-level composite classes which would correspond to the structured modeling notion of a module. Finally, the model itself is then represented by a composite class having attributes each of whose domain is a composite class representing one of the modules. The resulting class-composition graph represents the modular tree of the structured model.

## 5. Object-oriented concepts for modeling-in-the-large

One of the approaches proposed for model management is the systems framework $[36,37]$ . Designed to address issues related to modeling-in-the-large and inspired by concepts from systems theory, the systems framework provides a rich and intuitively satisfying view of models, together with a collection of structuring principles that are fundamental for capturing the semantics and structural relationships in a modeling environment. Moreover, it provides a graph-oriented, nonprocedural, and hierarchical approach for model composition and solver integration.

Although powerful, the core object-oriented concepts (Section 3) are not adequate for capturing some semantic concepts that we believe to be important for modeling-in-the-large, namely, composite models and model versions. In this section, we show how the concepts and structuring principles of the systems framework form a natural and useful object-oriented extension to the core concepts presented in Section 3. The scope of this paper does not allow full background discussion of these concepts and their advantages. The reader is best advised to consult [36,37] for details. Our aim here is to cast the basics of the systems framework in object-oriented terms to give an overall object-oriented approach to integrating Geoffrion's structured modeling (Section 4) with the systems framework's concepts and structuring principles for modeling-in-the-large.

In the systems framework, a model is defined and constructed to mirror (as much as possible) the reference system it represents. We view a model of a reference system as itself a system expressed in a formal language and synthesized from representations of selected elements of the reference system and the inter-relationships among them. The view of a model as a system is very natural; it is object-oriented. It is also useful because it allows powerful systems concepts and structuring principles (e.g., the notions of system, subsystem, interface, modularity, hierarchical design, step-wise refinement) to be brought to bear on the problem of model development and management.

In what follows, we shall understand a model schema to mean a specification of a class of systems or problems. A model schema formally describes aspects of the system (problem) being modeled—its external interface, the structural relationships between its elements, and its intended behavior (i.e., the set of operations or transformations that it performs). A solver, on the other hand, is an executable program capable of solving an instantiated model or realizing it so that it behaves as the specification demands.

Three principles underly the systems approach to model management: (1) model-solver independence: the separation of model specification (model schema) from implementation (solver); (2) model-data independence: the separation of a model schema from sets of data values that instantiate schema variables and coefficients; and (3) the division of a model schema specification into two parts: the external (interface) specifications comprising what we call a model-type; and the internal (structural and behavioral) specifications which constitute what shall be called a model-version. This way a model is seen as a glass box for which the interface (inputs and outputs) are known, while the contents (i.e., its internal structure and operations) are available for inspection, if and whenever they are needed.

We view the abstraction afforded by the concept of glass box as advantageous. It affords us both an external and an internal view of a model. The external view focuses on what the model does and on the sources of the model's input and the destination of its output. The internal view focuses on the model's internal structure (i.e., the relationships between its elements) and operations.

Externally, models are uniformly viewed as boxes with clear boundaries at which each presents a well-defined interface to the outside world (environment). A model's interface consists of a set of input ports and a set of output ports. It is only through these ports that communications between the model (system) and its environment are mediated. By interconnecting the output ports of one model with the input ports of others, individual models can be coupled to assemble larger models. Model built this way are called composite, while those without components are called atomic.

At the external level (also called the model-type level), the interface features of a composite model are indistinguishable form an atomic model, so a composite model may itself be used as a component in the assembly of even larger models. Hierarchical construction is made possible by repeatedly employing (nesting) models as components in higher level models.

It is the nature of the internal specification (i.e., model version) that distinguishes composite models from atomic ones. Composite model versions are specified by means of configuration scheme (described later), whereas atomic models are specified using some modeling language.

Model specification should be written in a formal, unambiguous, but still comprehensible language. Geoffrion's structured modeling formalism, owing to its rigor and sufficient generality, is an excellent basis for such a language. Our object-oriented representation of structured models permits us to integrate structured modeling (as a methodology for modeling-in-the-small) with the systems framework (as a methodology for modeling-in-the-large).

The basic idea revolves around the principles stated above. Instead of specifying the model schema in one module, as done using structured modeling notations such as SML [18] or using the object-oriented concepts of Section 4, we divide the specification into the two separate but related parts discussed above: external (model-type) specification and internal (model-version) specification. The interface specifications identify a model type. One may associate different internal specifications with a given model type. Various internal specifications that share (inherit) a common interface are versions of that type. Thus, using the terminology of structured modeling, genera names, type declarations, and interpretations would make up the interface specification—a model type. An atomic model-version specifies particular calling sequences (structure) and, as appropriate, generic rules (behavior) for the genera defined in a corresponding model type.

The MMS is therefore seen as managing a collection of objects which are semantically related in various ways. These objects include:

Model types (from general to decision-specific), model versions (both atomic and composite), and model instances.

Model type. A model type is an object that specifies the structural interface of a model class. It describes how a class of models (e.g., all production-mix models) can be used: it defines its function (what it does) and specifies a set of connection points, called ports, which form the interface between a model instance and its environment. Ports assume dual roles: As interface connection points for external (inter-model) communication and as internal model variables. Ports are either input ports or output ports. Input ports represent variables or conditions that may be supplied (or are determined) by the environment external to the model. Attribute and compound entity elements in the structured model definition make up the input ports in that model's structural interface. Each endogenous variable (e.g., variable, test, and function elements in a structured model specification) is associated with an output port. Ports, just like variables in a programming language, are typed. A data-type defines the structure and semantics of data or control signals passing through a port and the range of values they may assume.

The specification of a model type uses object-oriented notations as described in Section 4, except that the attributes specifying calling sequences and generic rules (for function and test elements) are not included. Through the object-oriented mechanism of inheritance, these attributes are defined as part of the model version specification, without causing unnecessary redundancy.

Also, through inheritance, model type classes can be specialized, giving rise to a model type hierarchy. For instance, the production-mix model type class is a subclass formed by specializing the linear programming model type class. The production-mix model type class can in turn be specialized for a given decision context (e.g., coffee-blending production mix model), and so on. Specialization of a model type class normally involves changing of the model name, possibly renaming the model's ports and associating a unit of measure with each port to reflect the semantics of a specific decision. All other properties are inherited (shared).

Model version. Whereas a model type specifies the interface of a model, the object called a model version specifies the model's internal structure and behavior (i.e., the relationships between the model elements and the set of operations that the model performs). A model version describes how the model is built; a model type describes how the model can be used. A given model type may have one or more model versions associated with it, each specifying a different way of realizing that type. For instance a forecasting model-type could have two model versions associated with it: One that uses a regression model, and another that uses a univariate time-series model.

![](/api/attachments/6QG5CPZH/fulltext/images/843735d0ca6636077e28d22d8dd39de7d191e50669381b8d88966af5e9a5a408.jpg)  
Fig. 1. A Composite model version.

The term of version generalization is used to describe the relationship between versions and their model types since a model type is an abstraction of the common features of the corresponding model versions. A model version is therefore a class which inherits all the properties of its corresponding model type, keeping the interface properties unchanged while adding specification for the behavior (e.g., generic rules in function test elements). Versions may be substituted for one another (i.e., they are 'plug compatible') since they are externally indistinguishable.

Versioning and version history management are critical for effective MM, in view of the fact that the model development process tends to be both iterative and tentative $[37,40]$ . We distinguish between two classes of versions: Alternatives and revisions. Alternatives are independent realizations of the same model type class. Revisions are versions resulting from modifications to incomplete, invalid, or obsolete model versions.

Inheritance is used here to permit the derivation of new model versions from existing ones.

Composite Versions and Solver Integration. The notions of model types and model versions endow a MMS with the qualities of modularity and extensibility. In particular, models can be composed hierarchically in terms of (independently developed) component models by interconnecting the output ports of one model with the input ports of another. Fig. 1 shows a specific production-mix model (PMIX) which was constructed by coupling a Prod-Mix-LP model version with a forecasting model version (Forecast) and other components to get the remaining data from a database or the user. The model solves the following LP problem: MAX $_{x}$ z = cx, subject to Ax ≤ b, Ix ≤ s, and x ≥ 0. The output variable y denotes a vector of product shadow prices. The vector of product demand, s, is computed by the forecast model which takes as input a matrix, h, representing the historical demand of the products.

Any composite model may itself be employed as a component in the composition of another model. A trace of this hierarchical decomposition/composition process may be represented by a tree with a root corresponding to the composite model version, with leaves corresponding to the low level instances of atomic versions of component models, and where each interior node is a composite model version resulting from the coupling of its descendant nodes. An atomic model version realizes a model type by explicitly supplying an internal specification (and, optionally, designating a particular solver) for that model type. A composite model version, on the other hand, is specified by means of a configuration scheme.

![](/api/attachments/6QG5CPZH/fulltext/images/1483e41baa8fed3330244d7707eab828e909d693107571a41dc4e66b7581773c.jpg)  
Fig. 2. Attribute inheritance graph.

A configuration scheme specifies how instances (copies) of component models are coupled to form a higher-level composite model. Instantiation allows multiple copies of the same model version to be used in the construction of a new higher-level model. Each instance is a distinct replica that has its own set of input ports, output ports, and internal state. The coupling is defined by a set of unidirectional (communication) links. At run-time, each link behaves like a pipe carrying the results placed on some output port of one model instance and delivering them to some input port of another model instance. Since instances of models are also bound to solvers at run-time, the data-flow paradigm embodied in this view provides a mechanism for solver integration.

Instantiation, like version generalization, involves attribute inheritance. An instance of a type or version inherits all of the attributes of that type or version, respectively. This relationship also places a restriction (an integrity constraint) on the update, creation, and deletion of model types and associated versions. Fig. 2 summarizes the notions of inheritance between model types, model versions, and their instances. The figure shows only a one level specialization hierarchy (between general model types and decision-specific model types). We should note, however, that, as discussed above, there is no restriction on the depth of the class hierarchy.

Composite model versions and version generalization are distinct concepts, whose semantics are not captured by the core object-oriented concepts presented in Section 3. The core construct of a composite class can be used to represent the IS-PART-OF or CONSISTS-OF relationship, but not the nature of the coupling specified in a configuration scheme for a composite model version. The concept of version generalization is also distinct from the IS-A (or Smith and Smith's generalization [47]) modeling construct in which a generic object class is formed from the union of two or more classes. A model type class is not formed by the union of two or more model versions.

## 6. The implementation

We are incorporating the ideas presented above into an a prototype model management system, called SYMMS (for SYstem-oriented Model Management System). We have originally designed and implemented SYMMS to demonstrate the feasibility of the systems concepts. Consisting of approximately 12000 lines of code, SYMMS (1) supports the hierarchical construction of composite models; (2) provides facilities for the storage, search, and retrieval of model types and model versions, and for the execution of both atomic and composite models; (3) manages model versions and revisions histories; (4) supports parameterization in both atomic as well as composite model versions; (5) makes explicit the relationships and dependencies between model types and versions, and uses it to maintain the consistency, security, and integrity of the model base. Details of SYMMS design and implementation are given elsewhere [38,40].

Associated with SYMMS is a description language, called MDL, which embodies the systems framework's concepts. MDL is not a programming language; it is a mechanism for formally defining model types, atomic model versions, and composite model versions. For example, the composite model version PMIX of fig. 1 is defined using the following MDL module.

## COMPOSITEVERSION MODULE PMIX;

IDENTIFICATION

AUTHOR: waleed;

DESCRIPTION: {This version accesses the corporate database to obtain matrices A, b, and c.};

ASSUMPTIONS {parameter assignments are consistent with the database schema.};

END IDENTIFICATION;

```matlab
CONFIGURATION
COMPONENTS: Prod-Mix-LP[1.0], Get-Mat[1.0], Get-Vec[1.0]:2, Forecast[2.0];

ParameterSettings for Get-Mat[1.0];
    dbname = "/usr/CorpDB";
    relname = "needs";
    rowattrname = "resource";
    colattrname = "product";
    elemattrname = "amount";
end;
ParameterSettings for Get-Vec[1.0]:1;
    dbname = "/usr/CorpDB";
    relname = "products";
    elemattrname = "cmargin";
end ParameterSettings;
ParameterSettings for Get-Vec[1.0]:2;
    dbname = "/usr/CorpDB";
    relname = "resources";
    elemattrname = "onhand";
end;

LINKS
COUPLING
Prod-Mix-LP.A ← Get-Mat.mat;
Prod-Mix-LP.c ← Get-Vec:1.vec;
Prod-Mix-LP.b ← Get-Vec:2.vec;
Prod-Mix-LP.s ← Forecast.s;
END COUPLING;
INTERFACE
Forecast.h == PMIX.h;
PMIX.x == Prod-Mix-LP.x;
PMIX.y == Prod-Mix-LP.y;
PMIX.z == Prod-Mix-LP.z;
END INTERFACE;
END LINKS;
END
(PMIX.)
```

Users submit MDL modules for registration and storage in the model base managed by SYMMS. Users basically check-in MDL and solver modules for storage. To preserve integrity, both inter- as well as intra-module checking are performed before a module is accepted for storage. To modify an existing module, an authorized user submits a check-out request. SYMMS uses locking to control concurrent access to the same object. The modified module may later be checked back in. If the module being checked back in is for an MDL model version, the old version is not updated in place. Instead, the system creates a new version and releases the lock.

SYMMS automatically handles the loading, sequencing, execution, and communication between components of composite models. To run a composite model, its composition tree is first flattened in order to express it directly in terms of instances of atomic model-versions. At run-time, these instances are viewed as data-flow objects which are bound to specific solvers. Various instances communicate uniformly by passing messages across communication channels (links). This topology is specified by the coupling subschema which is supplied in the MDL module that defines the composite model version. Since each instance now encapsulates a thread of control, the result is a network of communicating processes.

We are currently extending SYMMS in various ways. The current definitions of MDL's model type and atomic-version modules do not employ any structured modeling notations. We plan to modify the language definition to permit the specification of model types and atomic model versions using object-oriented notations for structured modeling as described in Section 5. We are also exploring the possibilities of writing parts of SYMMS itself and solver interfaces in the object-oriented language C++ [50] and extending it to operate in a distributed environment [39]. Moreover, the possibility of replacing SYMMS's storage manager by an object-oriented database management system is being considered.

## 7. Summary and conclusion

In this paper, we presented an object-oriented framework for model management and DSS development. We began by presenting a number of core object-oriented concepts, showing, where appropriate, how they have been refined to suit the application in this area. Next, it was shown how two proposals, namely Geoffrion's structured modeling and Muhanna and Pick's systems framework, can be cast in terms of object-oriented concepts. The significance of this is that Geoffrion's structured modeling provides a good methodology for modeling-in-the-small, while Muhanna and Pick's systems framework furnishes a number of concepts and structuring principles which are fundamental for capturing the semantics in a modeling environment and addressing issues related to modeling-in-the-large. Both methodologies are mutually supportive, and the proposed object-oriented framework synergistically integrates them.

It appears also that the object-oriented framework can contributed significantly towards coherently integrating the myriad of proposals in the MM area and the different interpretation of the model notion in the literature. The significance of the object-oriented framework extends beyond its promise to promote and facilitate reusability and enhance maintainability and extensibility. Rather, the object-oriented approach major contribution lies in that it reflects a ‘natural’ view of the world we are modeling in our databases, software, and analytical models.

Thus, in applying the object-oriented framework, we should strive for an overall object-oriented approach. In this type of approach, each methodology, tool, modeling technique, and software engineering activity is either object-oriented or supportive of an object-oriented approach. More specifically, the object-oriented approach provides a framework for analytical modeling, database modeling, solver implementation, and general application development. The benefits of the object-oriented approach would be enhanced if it is applied consistently throughout. Besides the conceptual integrity it affords, this consistency could provide the value-added benefit of simplifying integration both within and across the following categories: models, solvers, databases, and various support utilities.

To that end, we are extending SYMMS, our prototype model management system which is based on the systems framework, to serve as a platform for exploring the object-oriented approach. The goal is to obtain an object-oriented MMS which coherently and seamlessly integrates data, models, solvers, and utilities. This MMS would in turn form the foundation for an effective DSS development environment.

## Acknowledgement

I wish to thank Art Geoffrion, his students Laurel Neustadter and Swati Desai, and the anonymous refrees for comments and suggestions that helped improve the content and presentation of the paper.

## References

[1] G.M. Birtwistle, O.-J. Dahl, B. Myhrtag, and K. Nygaard, SIMULA Begin (Auerbach Press, Philadelphia, 1973).

[2] R.W. Blanning, Data Management and Model Management: A Relational Synthesis, Proceedings of the ACM 20th Annual Southeast Regional Conference, pp. 139–147 (April 1982).

[3] R.W. Blanning, A Relational Framework for Join Implementation in Model Management Systems, Decision Support Systems 1, 1, pp. 69–81 (January 1985).

[4] R.H. Bonczek, C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems, (Academic Press, New York, 1981).

[5] R.H. Bonczek, N. Ghiaseddin, C.W. Holsapple, and A.B. Whinston, The DSS Development System, Proceedings of the National Computer Conference, pp. 421–435 (1983).

[6] G. Booch, Object-Oriented Design (Addison-Wesley, Reading, Massachusetts, 1991).

[7] R.J. Brachman, On the Epistemological Status of Semantic Networks, pp. 3–50 in Associative Networks: Representation and Use of Knowledge by Computer, ed. (N.V. Findler, Academic Press, 1979).

[8] P. Coad and E. Yourdon, Object-Oriented Analysis (Yourdon Press, New York, 1990).

[9] B.J. Cox, Object-Oriented Programming: An Evolutionary Approach, (Addison-Wesley, Reading, Massachusetts, 1986).

[10] B. Dimsdale and H.M. Markowitz, A Description of the SIMSCRIPT Language, IBM Systems Journal 3, 1, pp. 57–67 (January 1964).

[11] D.R. Dolk and B.R. Konsynski, Knowledge Representation for Model Management Systems, IEEE Transactions on Software Engineering SE-10, 6, pp. 619–628 (November 1984).

[12] D.R. Dolk, Data as Models: An Approach to Implementing Model Management, Decision Support Systems 2, 1, pp. 73–80 (1986).

[13] A. Dutta and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer 17, 9, pp. 89–97 (September 1984).

[14] J.J. Elam, J.C. Henderson, and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of The First International Conference on Information Systems, pp. 98–110 (December 1980).

[15] J. Fedorowicz and G.B. Williams, Representing Modeling Knowledge in an Intelligent Decision Support System, Decision Support Systems 2, 1 pp. 3–14 (1986).

[16] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science 33, 5, pp. 547–588 (May 1987).

[17] A.M. Geoffrion, Integrated Modeling Systems, Computer Science in Economics and Management 2, 1, pp. 3–15 (1989).

[18] A.M. Geoffrion, The SML Language for Structured Modeling, Working Paper No. 378, Western Management Science Institute, University of California, Los Angeles (August 1990).

[19] H.J. Greenberg, A Functional Description of ANALYZE: A Computer-Assisted Analysis System for Linear Programming Models, ACM Transactions on Mathematical Software 9, 1, pp. 18–56 (March 1983).

[20] M. Hammer and D. McLeod, Database Description with SDM: A Semantic Database Model, ACM Transactions on Database Systems 6, 3, pp. 351–386 (September 1981).

[21] C.W. Holsapple and A.B. Whinston, Model Management Issues and Directions, Working Paper No. 7, Department of Decision Science and Information Systems, University of Kentucky (November 1988).

[22] W. Kim and F.H. Lochovsky, eds., Object-Oriented Concepts, Databases, and Applications (Addison–Wesley, Reading, Massachusetts, 1989).

[23] W. Kim, Object-Oriented Databases: Definition and Research Directions, IEEE Transactions on Knowledge and Data Engineering 2, 3, pp. 327–341 (September 1990).

[24] R. Krishnan, A Logic Modeling Language for Automated Model Construction, Decision Support Systems, pp. 123–152 (May 1990).

[25] M.L. Lenard, Representing Models as Data, Journal of MIS 2, 4, pp. 36–48 (1986).

[26] M.L. Lenard, An Object-Oriented Approach to Model Management, Proceedings of the 20th Annual Hawaii International Conference on System Sciences, pp. 509-515 (January 1987).

[27] T.-P. Liang, Integrating Model Management with Data Management in Decision Support Systems, Decision Support Systems 1, 3, pp. 221–232 (1985).

[28] T.-P. Liang, Development of a Knowledge-Based Model Management System, Operations Research 36, 6, pp. 849–863 (1988).

[29] T.-P. Liang, Reasoning in Model Management Systems, Proceedings of the 21st Annual Hawaii International Conference on System Sciences, pp. 461–470 (January 1988).

[30] T.-P. Liang, Modeling by Analogy: A Case-Based Approach to Model Construction, Working Paper 89 - 1524, College of Commerce and Business Administration, University of Illinois at Urbana - Champaign (September 1989).

[31] M.V. Mannino, B.S. Greenberg, and S.N. Hong, Model Libraries: Knowledge Representation and Reasoning, ORSA Journal on Computing 2, 3, pp. 287–301 (Summer 1990).

[32] B. Meyer, Reusability: The Case for Object-Oriented Design, IEEE Software 4, 2, pp. 50–64 (March 1987).

[33] B. Meyer, Object-Oriented Software Construction (Prentice-Hall, Englewood Cliffs, New Jersey, 1988).

[34] L.W. Miller and N. Katz, Model Management Systems to Support Policy Analysis, Decision Support Systems 2, 1, pp. 55–63 (1986).

[35] M. Minsky, A Framework for Representing Knowledge, pp. 211–280 in The Psychology of Computer Vision, ed. P.H. Winston (McGraw-Hill, 1975).

[36] W.A. Muhanna and R.A. Pick, Composite Models in SYMMS, Proceedings of the 21st Annual Hawaii International Conference on System Sciences, pp. 418–427 (January 1988).

[37] W.A. Muhanna and R.A. Pick, Meta-Modeling Concepts and Tools for Model Management: A Systems Approach, Working Paper No. 91-1 (submitted for publication), College of Business, The Ohio State University (1990).

[38] W.A. Muhanna, SYMMS: Design and Implementation Notes, Working Paper, The Ohio State University (1990).

[39] W.A. Muhanna, Issues in Distributed Model Management Systems, Proceedings of The Eleventh Annual International Conference on Information Systems, pp. 231-242 (December 1990).

[40] W.A. Muhanna, On the Organization of Large Shared Model Bases, Annals of Operations Research (forthcoming, 1992).

[41] F.H. Murphy and E.A. stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2, 1, pp. 39–47 (1986).

[42] O.M. Nierstrasz, A Survey of Object-Oriented Concepts, in Object-Oriented Concepts, Databases, and Applications, ed. W. Kim and F. Lochovsky (Addison-Wesley, Reading, Massachusetts, 1989).

[43] S.-S. Pan, R.A. Pick, and A.B. Whinston, A Formal Approach to Decision Support, in Management and Office Information Systems, ed. S.K. Chang, Plenum (1984).

[44] R.A. Pick and M. Sklar, A Knowledge Engineered Linear Programming Formulation Assistant, Proceedings of the 23rd Annual Hawaii International Conference on System Sciences, pp. 269–278 (January 1990).

[45] M.J. Shaw, P.-L. Tu, and P. De, Applying Machine Learning to Model Management in Decision Support Systems, Decision Support Systems 4, pp. 285–305 (1988).

[46] R. Sheifler and J. Gettys, The X Window System, ACM Transactions on Graphics 5, 2, pp. 79–109 (April 1986).

[47] J.M. Smith and D.C.P. Smith, Database Abstractions: Aggregation and Generalization, ACM Transactions on Database Systems 2, 2, pp. 105–133 (June 1977).

[48] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, New Jersey, 1982).

[49] E.A. Stohr and M. Tanniru, A Database for Operations Research Models, International Journal of Policy Analysis and Information Systems 4, 1, pp. 105–121 (1980).

[50] B. Stroustrup, The C++ Programming Language (Addison-Wesley, Reading, Massachusetts, 1986).

[51] M.A. Tarlton and P. Nong Tarlton, Pogo: A Declarative Representation System for Graphics, in Object-Oriented Concepts, Databases, and Applications, ed. W. Kim and F. Lochovsky (Addison–Wesley, Reading, Massachusetts, 1989).

[52] J.S. Welch, Jr., PAM—A Practitioner's Approach to Modeling, Management Science 33, 5, pp. 610–625 (May 1987).

[53] H.J. Will, Model Management Systems, pp. 467–482 in Information Systems and Organization Structure, ed. E. Grochla and N. Szyperski (Walter de Gruyter, Berlin, Germany, 1975).

[54] S.B. Zdonik and D. Maier, Readings in Object-Oriented Database Systems, (Morgan Kaufmann, San Mateo, California, 1990).
