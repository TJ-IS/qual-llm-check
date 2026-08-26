---
otero_id: 21387
otero_key: "K77CPECM"
title: "MIDA: An open systems architecture for model-oriented integration of data and algorithms"
authors: "M Holocher; R Michalski; D Solte; F Vicuña"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00064-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# MIDA: An open systems architecture for model-oriented integration of data and algorithms

M. Holocher, R. Michalski, D. Solte \*, F. Vicuña

FAW Ulm, Helmholtzstraße 16, 89081 Ulm, Germany

Accepted 9 September 1996

## Abstract

MIDA defines an architecture for building distributed Decision Support Systems by integrating high-level modeling approaches and implementation techniques for platform independent distributed client/server applications. One of the chief design goals is hiding of all infrastructural and system specific implementation details to users. MIDA covers solutions for model-oriented representation, administration, and (remote) access to both data and methods in distributed heterogeneous computer and networking environments. AMBAS-SOOM is an implemented variant of the MIDA architecture which has been developed at FAW. AMBAS-SOOM has two main components: the distributed operating platform AMBAS and the modeling environment SOOM, which implements concepts of Structured Modeling (SM) and Object Orientation. Models are developed using the graphical expert interface of SOOM and include formal descriptions of data types, of methods (functions, solvers) and relationships between data and methods. These models are translated automatically into executables for AMBAS. AMBAS contains an Object Request Broker mechanism to assign requests for data or methods from applications to services available within the network and, therefore, enables reuse of distributed data and methods to build up new models. © 1997 Elsevier Science B.V.

Keywords: Adaptive method base shell; Client server computing; Distributed platform; Execution environment; Model-oriented integration; Modeling environment; Open system; Operational programming; Structured modeling

## 1. Introduction

The MIDA project (Model-oriented Integration of Data and Algorithms) at FAW aims at developing an engineering and execution environment for distributed Decision Support Systems (DSS). The architecture of this framework covers aspects of high-level modeling approaches for DSS and implementation aspects of heterogeneous distributed client/server systems (cf. also [19]). By integrating these aspects into one system, the comfortable development of sophisticated platform independent and distributed Decision Support Systems can be supported. This includes the administration and remote provision of distributed data and methods (i.e. algorithms, functions, utilities, solvers, etc.) in a context of models. A model is seen as the specification which methods can be applied to what kind of data to produce other data of interest. Hence, models include the formal description of ontological components (data structures) and solution processes (methods), together with their interdependencies in (user-defined) application domains.

AMBAS-SOOM is an implemented prototype of the MIDA architecture developed at FAW. This paper introduces this prototype by describing main architectural concepts of MIDA.

AMBAS-SOOM consists of two main parts: AMBAS (Adaptive Method Base Shell [8,9]) is a distributed operating platform (execution environment), neutralizing heterogeneous operating systems, networks and other execution environments. SOOM (Structured and Object-oriented Modeling) provides a modeling environment for enhanced SML models (Structured Modeling Language [4,5]) consisting of data and functional dependencies (functions). These models are translated into executable data and methods by a generator, so that they can be handled by AMBAS and accessed transparently in the network. All data and methods available via AMBAS can be (re)used to build models of higher complexity using SOOM.

The MIDA project was influenced by contributions from several domains: approaches from structured modeling (cf. [4,5]), software engineering guidelines for modular and open systems (cf. [18]), a preference elicitation tool for decision analysis (cf. [22]), and several heuristics and specific optimization algorithms for project scheduling (cf. [1]). The current research activities take into account, and are built upon, many lines of earlier work concerning the model-oriented integration of data and methods, as discussed, e.g., in [3], [11], [14], and [17]. Following a multidisciplinary approach, this joint work has resulted in a prototype demonstration system for model management that covers many of the aspects and needs of a modem decision support system, as described in the mentioned papers, particularly, for application domains coming from applied mathematics and operations research (cf. [16]). AMBAS-SOOM covers major functionalities expected from a third generation decision support system. A major scenario handled by AMBAS-SOOM comes from the field of project scheduling, following the model framework outlined in [1].

In Section 2 we introduce the functional components of AMBAS-SOOM. These components are discussed in more detail in Sections 3–5. In Section 6 we outline that AMBAS-SOOM is build in an open systems architecture. Section 7 discusses future research directions.

## 2. The AMBAS-SOOM architecture

Fig. 1 shows the overall architecture of the AM-BAS-SOOM system.

On the top layer (dialog) of the architecture there are two alternatives of interaction with AMBASSOOM. First, there is the User Interface, that enables users to interact and work with pre-defined data and methods, taking direct advantage of the system's use of underlying methods and data structures. These users interact with the system via a graphical Request Dialog screen. The User Interface for the Requester Dialog allows users to communicate directly with AMBAS. One feature of this User Interface is that users have the possibility to specify what kind of output has to be produced from which resources instead of specifying directly which particular method has to be executed. Methods which have the ability to generate the desired output from the specified input are presented to the user for selection (cf. also Sections 4.2 and 5.1 for details of this selection process). Further work on the User Interface is intended to enhance the support for users to edit what is to be done by AMBAS, and not how this is to be done.

The second alternative for interacting with AM-BAS is the Expert Interface (cf. also Section 3.2), which allows experts to interact with the modeling environment SOOM. This modeling environment includes options to reuse existing structured models (i.e., manipulate or enhance a model's data and available solvers), and to create new models and integrate them (i.e., include the corresponding data structures and associated methods) transparently into AMBAS. The integration of new data structures and methods into AMBAS is supported by a language to describe models. These models are translated automatically into an implementation following the rules of the AMBAS Programming Interface (described in Section 4).

![](/api/attachments/K77CPECM/fulltext/images/674f3526a2b80b20f5cf564ec93402325b477af26561add94a724e12b1587e2d.jpg)  
Fig. 1. AMBAS-SOOM architecture.

The second layer of the architecture is the execution environment, implemented by AMBAS. The execution environment reduces dependencies of applications and the technical computing environment, especially for heterogeneous client/server applications. AMBAS constitutes a middle ware for distributed heterogeneous environments considering aspects of OSF/DCE [23] and CORBA [24], and fulfils specified needs of industry as documented in [10]. AMBAS includes a request broker and a knowledge base for dynamic allocation of resources needed for the transparent remote access to all data and remote execution of all methods. In AMBAS-SOOM data and methods are developed as structured models in the SOOM modeling environment. In this context, AMBAS can be seen as a data and method base management system (as an enhancement to database management systems) for distributed heterogeneous systems.

As one important feature in contrast to systems like OSF/DCE, AMBAS follows a neutralization strategy that allows the concurrent use of other execution environments simultaneously. This gives users the opportunity to use AMBAS today as a neutralizing platform, independent from ongoing (and partly incompatible) standardization efforts in different standardization bodies. To achieve this potential, AMBAS is designed as a knowledge-based execution environment. Based on information about the communication technologies available on connected computers, AMBAS automatically performs needed protocol transformations. AMBAS is operational at FAW since 1991.

As shown in Fig. 1, all information used by AMBAS to perform its operating functions is stored in the underlying AMBAS Knowledge Base. The AMBAS-Knowledge Base is used as the runtime repository for the execution environment and forms the repository for model development on top of

AMBAS. The design of the knowledge base allows workflow modeling and execution as well to support the design of Support Systems for Decision Processes. The AMBAS Knowledge Base includes:

\- models (formal descriptions of data, methods, dependencies and relationships);

\- knowledge about the implementation of data and methods within a computer environment (infrastructural knowledge, including location of data and methods, representation details, needed computer resources, etc.);

\- knowledge concerning access to data and methods (communication techniques, including network addresses, protocols, needed representation transformations, etc.);

\- organizational knowledge (users, computers, organizational hierarchies, etc.).

## 3. The AMBAS-SOOM user interfaces

## 3.1. The user interface for a request dialog

The User Interface is designed following the major goals of AMBAS: supporting users in finding appropriate solutions for their problems and hiding technical complexity of accessing data and executing methods in heterogeneous networks.

This user interface addresses more closely the difficulties faced by users working with computers. Indeed, a common scenario is that users are experts in their specialized fields, but not necessarily computer experts. Modern day computers have the potential to provide powerful support to the experts' work. However, to use computers effectively, specific knowledge of the computer system is expected; for example, knowledge about file systems, environment settings, etc. Hence, users often have to give up on any sophisticated computer support because they lack this computer-specific knowledge. Moreover, the users' technical difficulties increase when computers are connected to computer networks which, at the same time, allow even more sophisticated computer support (like remote procedure calls, for example).

For the reasons mentioned above, the User Interface of AMBAS-SOOM is built following the idea that a user only gives a description of his aims (in more abstract terms) to the computer system, and then the system itself assists the user to find the appropriate method(s) $^{1}$ , then executes these method(s) and, finally, presents the results back to the user in a reasonable form. In our approach, the description of what has to be done consists of (1) the specification of the data structure to be used as input for a method, and (2) the specification of the data structure to be produced as output from the method. The User Interface allows users to edit these data structure specifications (within the meaning of semantic data types) by offering the possibility to select from all of the data structures administrated in the knowledge base. The system, in turn, presents to the user all methods available in the knowledge base and fulfilling this requirements.

This interface is a first simple version implementing the idea of a strictly functional access to data and services and is not yet a satisfying specification and selection frame. Current work enhances the User Interface by (1) a finer classification scheme for methods by the use of taxonomies [20], (2) the use of preference functions to further restrict the collected set of fitting methods [22,13], and, (3) the implementation of Eigenmodel-based collection mechanisms [15].

## 3.2. The expert interface SOOM

The Expert Interface includes both the front-end user interface and the back-end kernel of the modeling environment prototype SOOM (Structured and Object-Oriented Modeling). SOOM is a computerized environment for model-based work which implements the Structured Modeling Language (SML) for defining models and data. SML [4] is an implementation of Structured Modeling (SM), a general modeling paradigm. In the SM worldview, the representation of reality (given as a structured model) is separate from the task to be done (the intention of the model manipulation), and also from the manipulation process itself (the solver, method, utility, etc.).

The objectives of SOOM are to handle models from a wide variety of domains, to integrate a wide variety of solvers, and to provide a comfortable graphical user interface for experts from different modeling domains. In particular, SOOM is designed as a generator for decision support systems for different domains; for example applied mathematics and operations research. Indeed, SOOM can be tailored, via changes to its front-end user interface and to its set of available solvers, to look like a specialized decision support system for various domains, like project scheduling, distribution, etc.

SOOM is implemented using AT&T C++2.1 on a Sun SPARCstation. The front-end user interface is implemented using XVT and OSF/Motif. The different functionalities of SOOM (e.g., the evaluator of mathematical expressions written in SML) comply with the AMBAS-Programming Interface. The models, the data, and the solvers in SOOM are maintained transparently by AMBAS. AMBAS provides the technology to help users select the most appropriate solver for the current model.

SOOM provides several functionalities: (1) it supports a wide variety of design and decision models, because SML has a wide scope of applicability; (2) it provides model error checking, by checking the syntactical and semantical correctness of a model; (3) it provides built-in evaluation without constant recompilation – that is, the function and test elements of an SML model can be evaluated without necessitating recompilation when the data is changed; (4) it provides, for a given SML model, automatically deduced data structures, which are derived directly from the model; (5) it provides interfaces to various solvers from different domains; (5) it provides a remote execution capability, which is automatically available from AMBAS.

Future enhancements of the modeling capabilities of SOOM will be in the direction of allowing different styles of composition of SML models. In particular, the usage of inheritance is being considered for the creation of SML models, as well as other influences coming from the world of object-oriented modeling.

## 4. The AMBAS programming interface

In this chapter, we describe the main concepts to implement data and methods to be administrated by

AMBAS. These concepts form the basis for system assisted method selection and for the platform independent implementation of distributed client/server systems.

## 4.1. The operational programming paradigm

A fundamental concept of AMBAS is a software engineering approach built on top of an object-oriented design, called “operational programming”, which was first introduced in $[18]$ . The operational programming approach consists essentially of a standard that defines the style and character of (programmed) concepts (data structures and methods), and which also gives rules for implementing the interfaces of methods. Following these guidelines, it is possible to access data and methods in a standard (and uniform) way. Furthermore, the common standard interface allows AMBAS to provide access strategies of arbitrary complexity for the selection of appropriate methods in response to specific user requests.

From a mathematical perspective, operational programming can be understood as an implementation of concepts from category theory, where data structures correspond to categories and methods to functions between objects within those categories (cf. [18]). This perspective coincides with the classical AI approach, where modeling is based on symbols and actions correspond to symbol manipulations (i.e., mapping between symbols). In operational programming, data structures correspond to symbols and methods to symbol manipulation processes.

## 4.1.1. Operational programming of data structures

To implement a standard for accessing data structures and, also, to keep methods separate from the physical implementation of the data structures used as input or output, a set of interface operators is included in each data structure. The data structure is then encapsulated, together with the interface operators, in a structure named “data class”, in analogy to the object-oriented terminology. The five interface operators that have to be provided for each data class are

\- create,

\- delete,

\- access,

\- assign, and

\- link.

These interface operators are used for the following purposes: (1) the creation of an object of the given class in the memory space (create); (2) the deletion of the object (delete); (3) accessing the object already created in memory space (access); (4) assigning the given object with values from another one, where this assignment represents an actual copy of memory values (assign); and (5) linking two objects, where only the references to the objects are copied (link). For technical reasons we also need two additional operators, export and import, that transform an object from its internal representation in memory into an external, machine independent representation and vice versa. This format transformation is necessary in order to be able to copy objects from one machine to another over a network.

In the current AMBAS prototype, data structures are implemented and administered as C++ classes because this language, with its object-oriented features, supports the encapsulation of the interface operators of data and method classes and, furthermore, allows the use of all object-oriented features (inheritance, overloading, etc.) for the specification of data structures. The operational programming standard defines a basic style of C++ classes. A data class with several data components has two sections: the first section consists of the (private $^{2}$ ) declaration of the data components; and the following section consists of the (public $^{3}$ ) member functions which represent the required interface operators.

All data classes intended to be directly integrated into AMBAS have to be implemented according to this concept. Data structures which are not originally implemented in this way can still be integrated, if a so-called bridge algorithm (cf. [3]) is implemented. The bridge algorithm has to provide a mapping from the original, external, representation of the data structure, to an internal C++ class written in operational programming style. By proceeding in this way, external data structures can be handled internally in the same way as data classes.

## 4.1.2. Operational programming of methods

The encapsulation of methods (functions, solvers) is similar to the encapsulation of data classes. By interpreting every method as a mapping from an input data structure to an output data structure, methods are seen as relations between the input structure $Y_{i}$ and the output structure $Y_{o}$ . In particular, all parameters used as input for a method are combined in a single data structure that is implemented in operational programming style, and all output parameters are represented by only one data structure also implemented in operational programming style. Input and output have to be implemented in physically separate data structures, so that methods can work free of side-effects. All methods with identical input/output structures are conceptually linked together in a structure that is encapsulated with the same interface operators as those of data classes. The structure which combines method(s) with the same input/output structure, together with the interface operators required by the paradigm of operational programming (i.e., create, delete, access, assign, and link), is named a “method class”, and is identified by the corresponding input and output structures.

After the declaration of the private part of the method class, the public interface operators for the class have to be declared. Particular emphasis is put on the difference between the functionalities of the interface operators of a method class and those of a data class: for a method class, the assign and link operators are restricted to the assignment and linking of the input object $O_{i}$ , and there is no public assign or link operator for the output object $O_{o}$ . The assignment to the output object $O_{o}$ is performed indirectly via the methods declared private in the method class. This assignment is performed by an activation of the access operator of the method class, in two steps: in the first step, the access operator executes the desired method (the desired method is specified using an accessing key); in the second step, the access operator assigns the output object $O_{o}$ with the output returned by the method, and gives access to the instantiated $O_{o}$ .

A method not implemented in operational programming style (because it is implemented in other languages, for example) needs to use bridge algorithms to map the method's input and output data structures to input and output structures represented in operational programming style. Via these bridges, it is consequently possible to integrate external methods into method (functions, solvers) classes which can be handled by AMBAS.

## 4.2. The benefits of operational programming

In AMBAS-SOOM, classification of methods is used as a criterion for the selection of methods. Methods are classified by their input and output structures, and referring to this classification criteria permits AMBAS to choose “fitting” methods by looking for a requested mapping from an input structure to an output structure. Further, the strict separation between input and output for each method allows the sequential execution of several methods, where the output of one method is used as input for the following method. If individual methods work correctly, the sequential execution of them will also work correctly because, as far as other methods are concerned, each method is free of side-effects.

Another aspect of the operational programming paradigm is that it permits the uniform access of data and methods in a distributed heterogeneous environment. The strict specification of data and method interfaces allows the design of a general access mechanism for these components, using only one class of servers on the local machines where the data and methods actually reside. These servers provide access to data classes and method classes, using the standard interface operators to create, to manipulate (access, assign, and link), and to delete objects of these classes. The operational programming style forces a rather large amount of overhead. The extra code required by operational programming techniques should be seen as the cost incurred for implementing applications in a highly declarative way, producing reusable code, and for using data structures and methods quite easily over distributed heterogeneous networks. This overhead has, however, not to be dealt with by programming; it is instead produced by a generator, that translates models into operational data and method classes.

## 5. AMBAS

AMBAS takes the part of a distributed operating system (execution environment) that provides mechanisms to access data and methods implemented following the operational programming paradigm. In AMBAS, methods can be executed independent of their location in the network, the location of their input, or the destination of their output. AMBAS manages data classes and method classes in an underlying knowledge base, which stores all the information that is necessary for the operation of the system.

## 5.1. The operating model of AMBAS

AMBAS can be seen as a distributed heterogeneous data and method base management system implemented on top of several standard operating systems (currently UNIX, VM/CMS, VMS, OS/2, WindowsNT). AMBAS applications can access data structures and methods administrated by AMBAS. To access data and methods, an application issues a request to AMBAS using the Requester API. To create a solution from a given problem AMBAS follows the steps shown in Fig. 2.

If a problem is passed to AMBAS by an application through the Requester API, all appropriate methods $^{4}$ are collected (COLLECT). In the next step, named SELECT, AMBAS presents all selectable methods to the user, or AMBAS may use arbitrary complex decision criteria and mechanisms, depending on the application domain, to identify the method that is most appropriate (called “optimal” method) with respect to the current problem instance and the user’s preferences.

This selection is needed and useful if a set of different solution algorithms is available for a given problem and no full order on this set can be specified by the user. For example, to solve the problem of adding two integers, the user will choose the method $add(N^{2} \rightarrow N)$ itself and no system support is needed (and this selection will be stable for ever). The AMBAS selection mechanism uses the input/output structure as a first selection criterion for appropriate methods. Of course, this criterion would be to weak if used isolated. More complex selection mechanisms are needed. The main concepts followed at the FAW are described in detail in $[15]$ and $[22]$ , aiming at a knowledge-based selection triggered by a computer-based evaluation of user preferences.

For example, the following problem is given: Send a note to another user. AMBAS will first collect all matching methods for this problem, e.g. fax, e-mail, phone, letter. Perhaps, the user even does not know all available technologies (a new fax-card support was installed yesterday evening by the administrator), but this infrastructure and communication knowledge is stored and maintained in the AMBAS Knowledge Base. The user's preferences could be given by: prefer cheap to fast, prefer safe to fast, and prefer fast to quality. Using these preferences a personal preference profile can be evaluated and transformed into a preference function to determine the estimation of different methods by the user. This SELECT component is implemented in the FAW Preference Elicitation Tool, but not yet fully integrated in the existing AMBAS prototype.

As a last step to get the problems solution, AMBAS executes the selected method(s), by giving a corresponding request to specific servers in the network (EXECUTE). EXECUTE can be seen as a kind of remote procedure call (RPC), where the necessary procedures are filled by AMBAS, not by the application. Usually, AMBAS itself refers to some technology dependent underlying RPC, suitable for the respective infrastructure situation.

## 5.2. The AMBAS Requester API

The Requester API is the interface for applications to access data and methods administrated by AMBAS. The Requester API follows the idea that it is not the concrete method but the available input and the desired output of the method that has to be specified. The Requester API uses an object of the class problem as input and returns an error code to the requesting application. The class problem is defined as follows:

![](/api/attachments/K77CPECM/fulltext/images/88367e250817a4d169212e88afc3fa64460b1c6cf6859b86eb895875ede8dff5.jpg)  
Fig. 2. The operating model of AMBAS.

class problem {

private: // private data members of the class
String Input\_Class\_Type;

String Output\_Class\_Type;

String Input\_Object\_Name;

String Output\_Object\_Name;

String Input\_Instance\_Name;

String Output\_Instance\_Name;

String Method\_Name;

public: // Set of public interface operators};

The first two components of the data class problem represent the input and output structure of the method intended to be executed. The next two components of the data class problem are user-given names identifying objects of the corresponding structures in memory. The naming of objects makes it easier for users to reuse objects and concatenate methods; for example, the object that is output by a method can be used as an input object for a following method. The third pair of components in the data class problem specifies the name of the input instance that will be represented by the input object (stored in the underlying Knowledge Base), and the name under which the output of the method is stored back into the Knowledge Base. The last component in the problem structure specifies the name of the method that is to be executed by the AMBAS System. This method has to perform the transformation from the input structure to the output structure, as specified by the first two components of the structure problem. This component can be left empty. If no method is specified, the system uses the COLLECT/SELECT operators mentioned in the previous subsection to identify an appropriate method to accomplish the desired transformation (i.e., a transformation from the input to the output structure).

## 5.3. The technical architecture of AMBAS

Fig. 3 shows a diagram of the technical architecture of AMBAS.

The main components of this architecture are the Request Broker, the EXECUTE component, the Object Servers, and the AMBAS Knowledge Base.

![](/api/attachments/K77CPECM/fulltext/images/8477da98865206d88fcf27b005e0eea84b2f4b3e19de6a30dc46127e15b6c451.jpg)  
Components of an AMBAS Object Server providing data and methods  
Fig. 3. Technical architecture of AMBAS.

The Request Broker is the component which receives the applications requests through the Requester API. The Request Broker performs the described COLLECT/SELECT mechanism and activates the interfaces of those data and method classes that are necessary to process the request following the operational model of AMBAS.

An Object Server is an active server process that is constantly waiting for requests from clients, using a specific communication technique (the Server API defined by the operational programming paradigm). Object Servers are serving data and method classes. Object Servers can be implemented as iterative (single access at one time) or concurrent (multiple access) servers [7]. An iterative server is used if the server provides access to hardware components that have to be addressed sequentially. However, a concurrent server is preferred when this concept can be implemented in a reasonable way, because this server architecture allows providing simultaneous services to many clients. Each Object Server provides access to the Server API given by five public operators (create, delete, access, assign, link; cf. Section 4.1) of each data and method class implemented on this computer.

Concepts of inter-process communication are used by the Request Broker to activate the routines of the AMBAS Server API. A special object-oriented inter-process execution command, named EXECUTE, has been implemented (cf. [6], [7]). EXECUTE provides a mechanism, actually combining different execution architectures like DCE, NAS, SNA, RPC, etc., that allows the execution of tasks in distributed heterogeneous environments (cf. [21]). The Object Servers receive the desired input values by using pipe-oriented forms of communication, depending on the requesting and requested process, where, e.g., binary or the XDR representation standard for data can be used as a data transfer protocol. The task of the Object Server is to use an appropriate bridge algorithm to translate the used representation into the locally used representation of the data structure, whenever needed. Secondly, the selected method is executed and, third, the output of the executed method has eventually to be translated back into the representation needed for communication, if the output object is located on another computer platform. This implementation allows the use of programs that are resident on different machines covering also problems of heterogeneous processors (Intel, Motorola) and codes (ASCII, EBCDIC).

Another feature of this architecture is that methods which are used by an Object Server to solve a request are allowed to form additional requests, that again have to be solved by AMBAS.

Therefore, this architecture is truly a multi-client /server architecture, because Object Servers can also act as clients, giving requests to AMBAS, and clients (Request Brokers) are addressed as servers by these Object Servers. Applications or users giving requests to AMBAS are called “requesters”.

Because objects created on an Object Server can be named by the requester (cf. the definition of the class problem given above), objects can be reused by subsequent requests. Objects are kept in memory of an Object Server until the session is terminated, or until they are explicitly deleted by the owners. AM-BAS includes mechanisms to provide access to objects limited to the requester that created them. On the other side, shared objects can allow public access by requesters.

The AMBAS Knowledge Base stores the information needed for execution of methods in heterogeneous, distributed environments. The AMBAS Knowledge Base defines an information model for representing the needed information. This information model includes concepts for representing data and methods together with knowledge about the enterprise's organization and knowledge about the technical infrastructure and security aspects. Additionally, instances of data classes (values that have once been represented by an object in the memory) are stored permanently in the AMBAS Knowledge Base, providing a basis for statistical evaluations and for their reuse.

The information of the Knowledge Base is also used for the above mentioned automatic selection of “optimal” methods for a given problem. Therefore, the Knowledge Base provides for each method semantic information (the model), computational attributes (for example average need of CPU time), and the specification of the runtime environment (necessary communication links, needed workstation characteristics, etc.). The current Knowledge Base for AMBAS is implemented on ObjectStore, an object-oriented database. The Knowledge Base is the central repository for all Request Brokers. Current work has enhanced the repository functionalities with distribution mechanisms, so that data can be distributed over several heterogeneous autonomous data management systems (cf. [2]).

## 6. Open systems architecture

AMBAS-SOOM is implemented as an open systems architecture. AMBAS-SOOM is open for integration of new data structures and methods. Additionally, AMBAS-SOOM can easily be extended for new inter-process communication technologies, data management concepts, or user interfaces. This kind of openness is a main objective of the systems architecture. Another kind of openness is the possibility that distributed AMBAS Systems can communicate together.

An important aspect of openness within the AM-BAS-SOOM approach is the possibility to extend the system with new data structures and methods, without the need to recompile the whole system entirely. The integration of new data structures and methods is a desirable procedure to enrich AMBAS-SOOM with new capabilities. Indeed, since such extensions could occur quite often, it would be quite disadvantageous for the use of the system if every single integration attempt would require the recompilation of the whole system. The integration of data structures and methods can be accomplished only by enhancing the AMBAS Knowledge Base with the necessary entries. Although requesters working with AMBAS-SOOM are not affected at all, they do not get access to the new components during their running session. Access to the new data structures or methods is, however, available to those requesters on future sessions.

The AMBAS Knowledge Base, which contains the data structures and methods handled by this system, will hopefully be enhanced constantly by new external data structures and methods implemented even on machines not integrated yet in the system and, possibly, implemented using languages other than C + +, which has been the mainly used language until now. Therefore, it is necessary to have a concept as part of the given open systems architecture to communicate with other systems, in the sense of openness in the framework of a heterogeneous distributed system. The integration of new communication technologies and execution environments is rather easy in the AMBAS System, because all communication activities are separated into the EXECUTE component and, therefore, the integration of new communication technologies can be restricted to enhance the EXECUTE component.

All the communication aspects are essentially integrated by storing communication paths and other information about the environment in attributes of the data and method classes. This includes all information concerning the identification of the computer systems and networks used, and information about how to connect the runtime system with the target systems.

## 7. Future directions

A major topic of current work on MIDA is the full integration of AMBAS and a knowledge-based selection mechanism that supports users to select an “optimal” method from a set of methods having the same input/output structure (improvement of the COLLECT/SELECT operators of AMBAS). The fact that an AMBAS request does not consist of a specification of a specific method, but consists of a description of the structural behavior of the desired symbol transformation, is of primary importance in many fields. This concerns, in particularly fields that address NP-complete problems (e.g. combinatorial optimization) where no generally appropriate solvers exist and a choice might be needed among hundreds of different approaches to handle a problem, given certain individual constraints. In these fields, for the solution of a given problem, no fixed algorithm is appropriate to solve the problem, due to the often unbearable runtime. For such problems, typically a number of heuristics are available and their use has to be controlled in an intelligent way by evaluating structural information concerning the current problem’s instance (e.g. stochastic versus deterministic modeling approaches in scheduling). In a lot of cases, only statistical experience (including statistical learning of the system itself) is a basis to define or identify “best” methods.

Another important aspect of the choice of a method are user intentions and personal preferences (a fast response versus an as good as possible objective function value). This aspect is in particular relevant by using AMBAS-SOOM as an environment to build a DSS (Decision Support System). For this purpose available methods have to be used in a suitable way to adapt the systems behavior to the requesters intention and preferences (cf. [12], [13]).

With respect to the software engineering concept of operational programming previously described, a model in SOOM can be seen as a collection of ontological components (data structures) and their specification as either input or output. Output is evaluated by an access to AMBAS specifying the needed input structure (functional dependencies) together with an input object and an instance. This adds to SOOM the potential of a dynamic access to all methods evaluating the desired output. If the method base is enhanced with a new method, this method is directly executable in the structured modeling framework, because of the dynamic accessibility. In particular, there is no need to edit or change the model structure. The user can select the new method and – more than that – a statistical evaluation of its quality can be done by the system itself in various forms (using stored examples, on-line weight randomization, etc.). This forms one source of information for automatically choosing appropriate methods.

Another kind of information that can be used are preferences of the requester (mainly the human requester itself). For example, if a user wants to have results fast (i.e., fast answers are more important than a relative good objective function value), a fast heuristic may be the best choice. Making use of a preference function by eliciting preference information with appropriate tools (cf. [22]) yields a basis for the evaluation of a reasonable order relation between methods that adapts the behavior of AMBAS to a particular user without modifying the model itself. This will be an important feature because the user can modify (or even indirectly modify in an automated way without necessarily knowing) the system's behavior towards his personal interests without changing structures.

Such basic properties of the chosen architecture will be used in later stages of the AMBAS-SOOM system development to add learning features to this system, building on a systems' Eigenmodel [15].

Hopefully, this will lead to some (statistical) kind of classification of problem instances with respect to the appropriate use of special methods.

## 8. Conclusion

The AMBAS-SOOM architecture constitutes a powerful approach implementing an open systems architecture. AMBAS is able to communicate with other types of administration systems over networks, to use external knowledge (data and methods), and can be enhanced quite naturally by new data structures and methods. From our viewpoint, with the AMBAS-SOOM approach, one more step towards the improvement of model-oriented development for heterogeneous client server applications has been done.

AMBAS-SOOM provides a distributed platform to generate distributed decision support systems. It covers important features of modern software engineering environments and gives the user the possibility to use in an easy way all data and methods already existing in a distributed heterogeneous environment without the need of having any deeper computer specific knowledge. Further, AMBAS-SOOM gives experts the possibility to work comfortably with data and methods by using all the features of structured modeling. The AMBAS-SOOM architecture covers aspects of automatic, user-specific system adaptations, based on individual preference functions as a control instrument for the prioritization of appropriate methods. Using AMBAS-SOOM as a programming environment also gives the user the possibility to naturally extend his local AMBAS Knowledge Base with new data structures and methods.

In addition to that, the modular architecture of AMBAS-SOOM, as well as the strict object orientation, makes it comparatively easy to extend the system with different kinds of individually designable interfaces. The software engineering concept of operational programming, as the underlying basis of representation, leads to an easy reuse of already defined data structures and already administrated methods, thus speeding up the process of rapid prototyping, especially in application fields from applied mathematics and operations research. The open systems architecture approach chosen also allows a comparatively easy integration of software implemented by other groups.

## References

[1] M. Bartusch, R. Möhring, F.J. Radermacher, Scheduling project networks with resource constraints and time windows, Annals of Operations Research 16 (1988) 201–240.

[2] M. Endrikat, R. Michalski, The WINHEDA prototype; knowledge based access to distributed heterogeneous knowledge sources, in: M. Schuler (Ed.), Analysing and Modelling Data and Knowledge, Springer, Berlin, 1991.

[3] R. Felter, Decision Support Assistant, Deutscher Universitätsverlag, Leverkusen 1989.

[4] A.M. Geoffrion, An introduction to structured modeling, Management Science 33 (5) (1987) 547–588.

[5] A.M. Geoffrion, The SML language for structured modeling, Working Paper 378, Western Management Science Institute, UCLA, 1990.

[6] K.D. Heerklotz, D. Solte, Knowledge based management of distributed resources, FAW-TR-91001, Research Institute for Applied Knowledge Processing, FAW Ulm, 1991.

[7] M. Heimann, Inter-process communication in heterogeneous networks, Master's Thesis, University of Ulm, 1991.

[8] M. Holocher, Conception and implementation of a system for problem oriented access to computer-based solvers, Master's Thesis, University of Ulm, 1992.

[9] M. Holocher, D. Solte, AMBAS - An adaptive method base shell, in: C.J. Petrie Jr. (Ed.), Enterprise Integration Modeling, MIT Press, Cambridge, MA, 1992.

[10] M. Holocher, M. Heimann, D. Solte, AMBAS - A CIMOSA compliant execution environment, FAW-TR-94019, Research Institute for Applied Knowledge Processing, University of Ulm, 1994.

[11] M. Jarke, F.J. Radermacher, The AI potential of model management and its central role in decision support, Decision Support Systems 4 (4) (1989) 387–404.

[12] T. Kämpfe, F.J. Radermacher, P. Wolf, Supporting preference elicitation – the FAW preference elicitation toll, Decision Support Systems 9 (1993) 381–391.

[13] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives, Preferences and Value Tradeoffs, Wiley, New York, 1976.

[14] R. Krishnan, A logic modeling language for modeling construction, Decision Support Systems 6 (1990) 123–152.

[15] R.H. Möhring, R. Müller, F.J. Radermacher, Advanced DSS for scheduling: software engineering aspects and the role of Eigenmodels, in: Proceedings of the 27th Hawaii International Conference on System Sciences, Wailea, Hawaii, January 4–7, 1994, pp. 290–299.

[16] R. Müller, D. Solte, How to make OR-results available: a proposal for project scheduling, Annals of Operations Research 55 (1995) 439–452.

[17] P. Piela, ASCEND, an object oriented computer environment

for modeling and analysis, Ph.D. Thesis, Department of Chemical Engineering, Carnegie-Mellon University, 1989.

[18] D. Solte, Open Systems – A Learning Framework for the Computer-Supported Development of Operations Research Solvers, VDI-Fortschrittsberichte, Reihe 16, Nr. 38, VDI-Verlag, Düsseldorf, 1987.

[19] D. Solte, A software engineering paradigm as a basis for enterprise integration in (multi-)client/server-environments, to appear in: P. Ladet, F.B. Vernadat (Eds.), Integrated Manufacturing Systems Engineering, Chapman & Hall, London.

[20] B. Steffen, T. Margaria T., B. Freitag, Module configuration by minimal model construction, Technical Report MIP-9313, Department of Mathematics and Computer Science, University of Passau, 1993.

[21] W. Stevens Richard, UNIX Network Programming, Prentice-Hall, Englewood Cliffs, NJ, 1990.

[22] P. Wolf, Computer-based elicitation of multi-attributive preference structures, Ph.D. Thesis, University of Ulm, 1992.

[23] OSF/DCE Introduction to DCE, OSF/DCE V1.0. Open Software Foundation, 1993

[24] The common object request broker: architecture and specification, OMG Document Number 91.12.1 Revision 1.1. Object Management Group (OMG), 1992

![](/api/attachments/K77CPECM/fulltext/images/598180e4b2456777686c0c39baa73a31b3ab9468506d35729cf75f1a75e58df5.jpg)

Markus Holocher received his degree in mathematics with focus on economics and computer science (1992) from the University of Ulm (FAW). His work at FAW is mainly focused on an integrated software engineering and execution architecture. He was considerably involved in the design and implementation of an engineering and execution environment for client/server applications. M. Holocher's research interests are focused on all questions in the field of

enterprise integration. He led several projects at FAW in the area of software engineering, distributed computing and information management, including different consulting activities for banking organizations. He published papers in several conference proceedings.

![](/api/attachments/K77CPECM/fulltext/images/7916959f83c811bebb062405b281159c212b21df7c63be94b8456ab1b7902f68.jpg)

Ralf Michalski received his degree in Business Engineering and Computer Science from the University of Karlsruhe. He joined FAW in 1988. His major research area is that of open heterogeneous systems. In particular, he is interested in the development of concepts for the integration of data and algorithms coming from different system domains. The integration is based on a collection of conceptual environment models. He was project leader for

several research projects dealing with distributed databases, scheduling and telecommunications. Additionally, he has been involved in the implementation of the heterogeneous hardware and software environment at FAW.

![](/api/attachments/K77CPECM/fulltext/images/3e686c04bdc62031e9bd0f7f7bd8a1d356a94874405c93f9ea43f77afcb5dbbd.jpg)

Dirk Solte received his doctoral degree after studying business engineering with focus on operations research and computer science at the University of Karlsruhe. Since 1988, he has been a senior scientist at FAW, heading the Department of Communications Systems and Industrial Software Production, and coheading the Department of Enterprise Integration and Decision Support Systems. He is also responsible for the sophisticated technical infrastructure of

FAW. This focuses his work in these domains to solutions in heterogeneous distributed environments. Dr. Solte has published several papers in these fields, directed a number of ambitious research and software development projects and consulted industry.

![](/api/attachments/K77CPECM/fulltext/images/c65373d5416a09412f9ce6e3977fe71545f6e101574b4d157c47fb214f61bda9.jpg)

Fernando Vicuña received his Ph.D. in Computer Science from the University of California at Los Angeles (UCLA). He is currently the Project Manager for Tandem Chile, leading the telecommunications team, concentrating in developing telephony and computer solutions such as Advanced Intelligent Networks, Video on Demand, Network Management, Value-Added Services, etc. Dr. Vicuña's primary research interests include intelligent decision support sys tems, structured modeling, and intelligent telecommunication and network applications. He has been involved in different research activities at UCLA and FAW on software engineering, decision support systems, and networking. He published several papers in these fields.
