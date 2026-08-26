---
otero_id: 23350
otero_key: "4V6T75JE"
title: "An Overview of Intelligent Decision Systems"
authors: "Daniel T Lee"
year: "1989"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1989.17"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Overview of Intelligent Decision Systems

Daniel T. Lee, University of Texas-Pan American, Edinburgh, TX 78539

Abstract: System integration has been the goal for both academicians and practitioners for more than two decades. Tremendous efforts have been made toward the achievement of a unifying theory or at least a framework in system integration. Unfortunately, the goal has not been achieved because of the dynamic nature of the subject. The purpose of this paper is to conduct a systematic analysis of the related subjects in system integration and to develop a framework which can be used to guide researchers and practitioners in system integration development. Traditional data modelling techniques and knowledge representation methodologies will be reviewed first. Major emphasis will be placed on object-oriented system integration and hybrid knowledge representation methods for developing an integrated intelligent decision system for next generation decision making.

## Introduction

Computer decision support systems have evolved through two decades. They are still in an infant stage. Recent developments in computing indicate that an emerging pattern has arisen for meeting the new challenge. Traditionally, Decision Support Systems (DSS) have been developed and used for supporting decision makers in their decision-making processes. The emphasis is that DSS only supports rather than replaces decision makers. Recently, emerging technologies may change the entire picture. There may be a new name for this incoming system, i.e. the Intelligent Decision System (IDS). The IDS is different from the traditional DSS. The IDS is not only capable of supporting decision makers but also can be used to replace them. Through both DSS and IDS emphasize interactive and user-friendly processing, the difference lies in that the DSS utilizes mathematical models for analytical purpose, mainly 'What if' types of analysis. It is quantitative in nature. The IDS is mainly concerned with idea generation, reasoning, and heuristic decisions. It is basically qualitative. Actually decision making requires both types of support, analytical model analysis and idea generation thought processes (Lee, 1985; Mittra, 1986; Sprague and Carlson, 1982; Sprague and Watson, 1986).

Recently, Young (1989) hypothesized that human creativity in quantitative and qualitative analysis is associated with the functioning of the human brain. These two forms of support may be related to the functioning of the two hemispheres of the brain. The left side of the brain is more associated with quantitative analysis. The right side of the brain is more associated with holistic decisions. The computer can be characterized as being essentially a left-brained step-by-step process device. Though the goal of the DSS is to support semi-structured and unstructured decision making, it basically follows the left-brained analytical approaches for information processing. Idea generation for holistic decisions is affiliated with the right-brained forms of holistic thinking which is the main source of human creativity (Brodie, 1989; Ma and Lee, 1989).

Since DSS and IDS are two sides of the same coin, the integration of analytical capability and idea generation will naturally create new forms of support systems. As indicated earlier, the DSS is still in an infant stage and the IDS has just emerged as a decision support tool. There is a tremendous potential for this new form of decision systems. The addition of the IDS to the DSS is not just a technical extension of computer software tools. It actually represents a conceptual breakthrough in combining all related high technologies into a unified whole. This new integrated system will be the basis for the next generation of computing which will support intelligent decision systems in a network of heterogeneous systems (Lee, 1989).

The purpose of this paper is to conduct a relative analysis of data modelling and knowledge representation for conceptualizing a framework which can be used for developing integrated systems. This integrated system has many facets. It will be impossible to pursue every facet in a short paper. For practical purposes, the main focus of this paper will be placed on DSS/IDS integration. It will include AI/DB integration and object-oriented data/knowledge modelling and representation (Lee, 1988).

## Decision support trend

During the past four decades, computers have been successfully applied to structured tasks. However, the highest payoff the computer can make is not in transaction processing, but in decision making. Since the 1970s, Decision Support Systems (DSS) have been conceived to fill the gap by helping decision makers in solving basically unstructured or semi-structured problems. It has only partially fulfilled its goal because decision making is basically done through human cognitive process. Pure computer automation processing is inadequate to meet this dynamic process which involves both computer automation processing and human cognitive processing. This opens a new era which may be termed extended DSS, intelligent DSS, or expert DSS. Since the intelligent DSS is capable of replacing decision makers in making decisions, rather than just supporting them in their decision-making process, it may be called the Intelligent Decision System (IDS).

Technological advancement has rapidly taken place in many areas and individual technologies are inadequate for meeting the new challenge. All high technologies have to be integrated to achieve a unified goal because the effect of an integrated system will be larger than the sum of its individual efforts. The traditional concepts of DSS have to be expanded. The basic components of the traditional DSS (as shown in Figure 1) have to be expanded to embrace the emerging high technologies (as shown in Figure 2) (Lee, 1986).

![](/api/attachments/4V6T75JE/fulltext/images/8ef1540920381ab863f723a5e803ae3cd7d41767f49fb60f270ff2228a14e4be.jpg)  
Figure 1. Architecture of traditional DSS

![](/api/attachments/4V6T75JE/fulltext/images/f9b152684c2c447ad12a1965192c60a05da86602ac639be9bf233c30c014ec89.jpg)  
Figure 2. Architecture of extended DSS

## Integration requirement

System integration is critical for the next generation of computing. It has already been started in a number of directions. The main incentive is that the effect of an integrated system is larger than the sum of the effects of its components. Besides, in an integrated system, each component may not reinforce one another, but actually offset each other's effects.

Bidgoli (1989) illustrates some existing examples of DSS/ES integrated systems such as GURU, by Micro Data Base Systems, Inc., which combines ES, DBMS, spreadsheet, graphics, communication and word processing programs. Holsapple and Whinston (1987) also praise the GURU for dramatically extending the conventional AI notions of knowledge representation and processing to include well-known business computing methods. There are many other systems, such as M-1, Knowledge Workbench, KEE, IFPS ..., etc. which basically integrate AI technologies with either database or modelling techniques. Bidgoli (1989) proposes an ideal diagram of expert DSS (EDSS) (as shown in Figure 3). Young (1989) also illustrates a diagram of an extended framework for DSS (as shown in Figure 4).

![](/api/attachments/4V6T75JE/fulltext/images/9f32b29e732850389f7e3ff2db2673d5c3ef282858efcd76e29eb566d0f0bfe0.jpg)  
Figure 3. A model for an EDSS

'Whole-brained' individual decision support

![](/api/attachments/4V6T75JE/fulltext/images/3c31212c6ebf8d5b29826df3192a9515778e806ae7db9fbbb518320158dcc477.jpg)  
Figure 4. An extended framework for DSS

Brodie (1989) indicates that future computing will require the integration of many currently disjointed technologies, including AI, DB, programming languages, operating systems, heterogeneous distributed systems, and communication. In particular, AI technology will be required for special-purpose and complex problems. DB technology will be required for managing data sources, such as object management and access in a network, whether those objects are in DBs, KBs, or other type of systems. He concludes that AI/DB technology will provide the basis for intelligent interoperability among systems. Even his survey results only emphasized two major disciplines, AI and DB. Since analytical models are usually also stored in DB, this technological integration really provides the basis for system integration (Mockler, 1989; Parsaye et al., 1989).

## Integrating methodologies

Traditionally, data is stored in DBs in accordance with data modelling techniques. Knowledge is represented in KBs in accordance with knowledge representation (KR) methodologies. Data modelling techniques and KR methodologies are inconsistent. A new methodology is needed to combine these two inconsistent methodologies into a unified whole.

Basically, data stored in DBs are generally simple objects and static. The knowledge represented in KBs are usually more complex objects and dynamic. DB/KB systems are good at heuristic and higher than first-order searches over small KBs. How can we make optimal use of DB and KB searches? One alternative is to use the DB system to reduce the search space for the KB system. According to Brodie (1989), it is an open problem as to how to decompose a search expression into these two parts, and on how to identify the object or components of an object which must be accessed to resolve an object reference and complete the operations associated with the reference.

In order to accommodate abstract knowledge, KB objects, represented with semantic nets and frames, are more complex and highly interrelated. KB objects are often defined in terms of their relationships to many other objects. This complexity may defeat current DB transaction processing and related optimizations based on grouping. Therefore, many DB assumptions must be re-examined to embrace such changes. AI may be able to contribute solutions to these DB problems.

Since DB techniques and KB technologies may be able to reinforce each other, a deep synthesis approach is needed in developing a framework for DB/AI integration. The synthesis approach is usually more difficult because it involves an overhaul of the theoretical foundation of DB and KB as well as the new entity of integration. Coupling is another alternative. It tries to provide DB capabilities in KB systems, and KB features in DB systems. This approach has been successful for heterogeneous distributed DB and loosely coupled DB/KB systems. Actually both the synthesis approach and coupling approach are required for systems integration efforts (Su, 1988; Ullman, 1988/89).

## Data modelling techniques

Data modelling techniques were developed after many years of DBMS research, and many early DBMS were in existence before the term data model was defined. Currently, there are generally three data models which are very popular, namely the hierarchical data model (HDM), the network data model (NDM), and the relational data model (RDM). Among these three data models, the RDM is the most promising model in either traditional data modelling (DM) or knowledge representation (KR) of complex and abstract knowledge. The basic concept and structure of the HDM and the NDM are still valuable for both DM and KR.

Currently, many researchers and manufacturers working on integrated systems are heading towards extending the RDM. This is because the basic constructs of the RDM are more appropriate for decision system development. For example, Imielinski and Lipski (1989) propose a semantically meaningful extension of the usual relational operators which can accommodate null values and incomplete information. They developed criteria and methodology for extending relational algebra operation onto tables with different types of null values and complex objects. Yao and Kim (1988) developed a methodology that transforms object-oriented KR formalisms (e.g. frame, script, etc.) to the relational data model. Chen et al. (1988) designed and implemented a Relational Knowledge Base System (RKBS) which utilizes the knowledge module as the basic unit of the knowledge base. The Relational Knowledge Base Management System (RKBMS) provides the user with a knowledge base developing environment including explanation facility, knowledge acquisition system, SQL query language, the inference engine (the RKB Interpreter) . . ., etc. The mass facts of the RKBS can be stored in RDBS. This is a typical extension of the RDM (Gibbs et al., 1983; Kroenke and Dolan, 1988; Su, 1988; Ullman, 1988/89; Parsaye et al., 1989).

## Knowledge representation methodologies

According to Luger (1989), the function of KR is to capture the essential features of a problem domain and make that information accessible to a problem-solving procedure. There are basically three categories of knowledge: permanent, static, and dynamic. As indicated earlier, traditional data modelling basically copes with static data that usually remains unchanged from one use of the application to the next, but the data is likely to change during the life of the application. Knowledge represented by the KR methodologies in the knowledge base (KB) is dynamic in nature. It will change from one use of the application to the next and it may change during the execution of the application. It is a characteristic of most computer programs that the knowledge contained within them is not represented explicitly and cannot be readily expanded or manipulated (Walters and Nielson, 1988). Currently, there are several KR methods which are widely used in KR such as formal logic, rule-based, semantic network, and frame-based. There are also some less popular methods such as model-based, blackboard, and multiple contexts. However, Object-Oriented Programming Language may be important for a hybrid system (Lee, 1988; Parsaye et al., 1989; Raju and Majundar, 1988).

Formal logic. Knowledge is represented in propositions that make logical inferences. Propositions are statements which can be regarded as either TRUE or FALSE. A relational DB can be regarded as already in FOL form. Each relation type corresponds to a predicate and each relation to a proposition. To map a domain onto First Order Logic, it must be possible to regard the domain as consisting of objects plus properties of, or relations between, the objects which can be designated as TRUE or FALSE. The advantage of formal representation is that there is a set of rules, called inference rules in logic, in which facts that are known to be true can be used to derive other facts that must also be true. Any new statement can be checked against the facts that are already known to be true. The advantage of this KR method is that the facts can be independently asserted, but when the system is large and complex, the performance of the system may be slow and inefficient (Grant, 1987; Naqui and Shalom, 1989; Pavelin, 1988; Turban, 1988; Zadeh, 1989).

Rule-based. The knowledge represented in an application KB can be structured as a set of rules. These rules establish relationships between facts in the KB and allow new facts or relationships to be derived. The problem may be solved by reasoning with these rules. Many existing expert systems (ES) are built with production rules because of their simplicity in construction and application. Typical examples of rule-based software ES development tools are EMYCIN, OPS5, M.1, S.1, EXSYS ..., etc. In each of these tool systems, rules are conceptually represented as IF/THEN statements. Multiple rule sets can be defined to control the execution of the rules. Backward-chaining and forward-chaining (or both) are often used by the inference engine during reasoning process. The problem with rule-based systems is that the rate structures may not be well suited for representing procedural information and complex abstract objects. When the rule sets become too large, execution and management of rules may become unmaintainable. (Pavelin, 1988; Walters and Nielson, 1988)

Semantic network. A network is a net or graph of nodes joined by links. The nodes in a semantic network usually represent facts, concepts, or situations. The links define relationships among the facts. Each node may point to a subnode. IS-A or HAS-A link allows facts to be attached to classes of objects and then inherited by subordinate objects in the class. Semantic nets are easy to understand through graphical representation of non-rule knowledge in hierarchies. The problem faced by this KR method is that the meaning attached to the nodes might be ambiguous and processing may be very complicated (Pavelin, 1988).

Frame-based KR. The knowledge in an application KB can be organized as a set of frames. These frames will contain the essential structural information with which the applications reasoning can be based. The frames can be related to each other. A frame can be viewed as a collection of related information on a subject problem. This information may be factual or procedural. A frame may represent a class of objects. Subclasses can inherit the properties of its parent class. Rule-based and procedural knowledge can operate efficiently on frame-base KR.

A frame is basically a structure holding various types of knowledge like a traditional data record. Each frame has a unique name and a set of properties. These properties are stored in slots in a variety of formats. Frames are useful in categorizing knowledge when the knowledge has some underlying structure such as a set of objects or concepts. The term class is used to denote a frame containing the knowledge about a set or class of objects of a given type. Each class represents a generalization of a subordinate class. The frames in a subclass represent a specialization of the class to which they relate. Class structures are used to organize the knowledge into class hierarchy which is often referred to as a taxonomy.

To arrange frames into a structural relationship has several advantages. The graphical representation of relationships between frames help designers understand the underlying structure of the knowledge and facilitate the development of the application. Not only facts and values can be stored in slots but also frame relationships, rules, and rule sets. This structure permits the unification of rule-based KR and frame-based KR into a unified whole. Slots may also contain functions, permitting procedural knowledge to be incorporated within the frame representation. This inclusion of a function within a slot provides a powerful means to integrate factual, procedural, and conceptual knowledge in an application. All the arrangements made above with respect to rule-sets and inheritance apply equally well for functions, procedural knowledge, and conceptual knowledge in an application.

Object-oriented programming is one of the most important techniques in KR. It tries to associate all data and functions with each object in the application system. Messages are sent to objects requesting that particular functions or services be performed. The object responds with certain action in accordance with methods sent with the message or stored with the object. Such message passing may be similar to function or subroutine calls. Each object can be represented as a frame, with the data about that object stored in slots of that frame. The various behaviours of the object are provided by methods that are also stored in the frame's slots. Messages are then exchanged between objects to provide a collection of behaviours of the system. This concept and mechanism have been implemented with Simula (Dahl and Nygaard, 1966) and SmallTalk (Goldberg and Robson, 1983).

Frame-based reasoning is very versatile. It provides a means for structuring a variety of types of data in the KB and a framework whereby not only the data but also the structure of those data can be reasoned about. It makes rules and procedures in an application to be generic, thereby reducing rule-set or procedure size and make KB easier to understand and test. It is so far one of the most promising KR methods not only for the IDS but also for the eventual integration of DSS/ES. Since frame-based reasoning using frame-based KB and object-oriented programming is new, there may be problems confronting designers due to its complexity. But once familiarized with the mechanisms, it can provide enormous benefits in KR and system modification. (Luger and Stubblefield, 1989; Tanimoto, 1987; Walters and Nielson, 1988).

## Object-oriented system integration

So far we have briefly discussed the basic concepts and mechanisms of traditional data modelling techniques and knowledge representation methodologies. From the above analysis, there is one unique construct which can be used as the basic fabric of the proposed integrated system, and that is the object. Shlaer (1988) defines an object as an abstraction of a set of real-world things which have the same characteristics and conform to the same rules. Meyer (1988) describes the object with two senses: at the design stage, the goal is to identify the classes of external objects whose behaviour the system will attempt to model; at the implementation stage, object-oriented languages ensure that systems are written as collections of internal object descriptions. Internal objects are simply like records. A record is a structure with properties called attributes or fields. A field in an object may refer to other objects. Furthermore, objects may be created dynamically through operations performed on objects. We may concentrate on the patterns that are common to a whole class of objects. A class is similar to a record type which describes the structure of a set of objects. All such object will be called instances of the class.

Kroenke and Dolan (1988) define an object as a named collection of properties that sufficiently describes an entity in the user's work environment. An entity is something a user perceives as an independent unit, meaning it can stand on its own. Entities are perceptions and may or may not be physical. An object is a structure that represents an entity. An object instance is a particular object. Object properties are used to describe the object. It can be non-object properties or object properties. A non-object property may have a single value or multiple values. In case of multiple values, they are actually repeating groups. An object-property is a characteristic of the entity that is actually another object. Thus, one object can contain other objects. This characteristic is vital for representing complex knowledge in our proposed integrated system. The domain of a property is the set of all possible values the property can have. The domain of a non-object property consists of both a physical and a semantic description. The domain of an object property is a set of object instances. When you identify objects, you need to specify both the properties and the property domains. Domain definitions are separate from object definitions. This helps reduce duplicate domain definitions because one domain may be used by many properties.

Kroenke and Dolan identify five common types of objects: a simple object contains only single-valued properties. All of the data about that simple object can be stored in a single relation. Composite objects contain one or more non-object properties. They require more than one relation for their representation because they contain repeating groups. The multi-valued attributes do not represent another object. At least, one of the relations cannot stand on its own. A compound object contains at least one object property. It will be represented by at least two relations, one for each object. The objects can stand on their own. Association objects contain non-key data. They define relationships between two other objects. It needs more than two relations to represent them. Aggregation objects represent an entity group. Members inherit properties of the group. This characteristic is vital for KR in either AI/ES systems or in our proposed IDS. The above logical system design mechanism can be readily applied to the KR and system integration with the RDM and the IDS (Banerjee et al., 1987; Hornick and Zdonik, 1987; Keene, 1989; Newton and Watkins, 1988; Simonian and Crone, 1988).

## Hybrid knowledge representation

Based on the above analysis, another phenomenon has also been shown. There is no single data modelling technique or knowledge representation method that can be completely adequate for system development or integration. The best alternative may be hybrid methodologies for synthesizing the various methods into a unified whole. Luger (1983) suggests rules, inheritance, and object-oriented systems are a good combination. Object-oriented knowledge bases are good for modelling the various behaviours of interacting objects while rules are good for reasoning and testing these objects. Similarly, objects may access the rule base as part of its methods. It is even easier to add things to the lisp-shell/OOPS hybrid environment. The OOPS uses a simple object-oriented programming language. The language defines three functions to do object-oriented programming in OOPS: object, method, and message. Def-object is used to define new objects. Def-method is used to bind methods to objects. Message passing between objects is effected by the function MESSAGE. When defining objects, def-object takes three arguments: the name of the object, the name of its parents, and a list of instance variable/value pairs. When defining methods, def-method also takes three arguments: the name of the object, the name of the method, and the definition of the method. When defining a message, it takes two or more arguments: the name of the object receiving the message and the name of the method. There are a number of commercially available ES tools that support this hybrid approach to KR such as KEE, ART, Knowledge, Craft, NEXPERT, and Goldworks.

Through these mechanisms, objects, rules, and procedures are integrated. Objects, in turn, are integrated with the relational database system and frame-based KR methodologies. At the present time, before a total new methodology is invented in system integration, this hybrid KR mechanism may be one of the most promising methodologies we can have (Newton and Watkins, 1988; Simonian and Crone, 1988).

Distributed system integration. Distributed processing is the future of the world. Data for practical purpose can not be stored in one place. They must be distributed to where they are needed the most. Tripathi and Aksit (1988) present the object-oriented constructs for communication and concurrent programming in the SINA programming language. It presents an object-oriented solution to various problems in interprocess communication, scheduling, and resource management. The SINA objects are active entities that they may contain multiple concurrent processes. SINA supports communication between objects using object pointers. This allows building systems in which the communication constructs can change dynamically.

In the object model of computing, objects are instances of abstract data type modules. The concept of encapsulating a shared resource as an active module which reacts to the messages from its clients constitutes the basis of an object-oriented concurrent and distributed programming. The mechanism for synchronizing concurrent operation on these dynamic abstract data type modules is implemented by the concrete representation of objects. Several concurrent and distributed programming languages and distributed operating systems are based on this methodology. This exemplifies another application of object-oriented integration method with distributed processing capabilities. Actually, this application can also be integrated with all other integration methodologies we have discussed. In other words, all integration mechanisms outlined in the paper can freely apply to various occasions, static or dynamic, single place or distributed over a large area.

Lyngback and McLeod (1984) describe a simple model for object sharing in distributed office information systems. The model provides a small set of operators for object definition, manipulation, and retrieval in a distributed environment. Relationships among objects can be established across workstation boundaries. Objects are relocatable within the distributed environment. It also provides access control and the dynamic sharing of objects among workstations. An object naming convention supports location transparency of object references. Actually, it is modelled as a logical network of workstations. An experimental prototype implementation of this model is described.

The approach used in this model does not employ one of the traditional high-level data models. It focuses on distributed information management on an object level. In addition to a simple model called ODM (object-oriented database model), a distributed version of ODM, called DODM is described. An ODM database is modelled as a collection of objects. Objects correspond to facts and concepts. Objects are used for modelling the structures and operations of data. ODM supports various kinds of objects such as structural, abstract, behavioural, text, audio, image, and descriptor objects. Objects and relationships are the basic concepts for modelling data in the ODM. Each object and relationship in the DB corresponds to relations. It is also appropriate to say that an ODM database can be thought of as a collection of relations. An ODM DB can be implemented straightforwardly by using existing DB technology.

The DODM is a simple extension of the ODM. The distributed office system can be thought of as a logical network of communicating databases. Relationships among objects can be established across DB boundaries. Objects can be copied and moved from one DB to another. Mechanisms are provided for access control and the dynamic sharing of objects among individual databases. There are three kinds of object identifiers: local, global, and transparent. A local object identifier uniquely identifies an object with the DB. A global object identifier uniquely identifies an object within the entire network of databases. A transparent object identifier denotes every object in a given set of databases that has the same local object identifier. In the experimental implementation of the DODM, each node in the DB network consists of a DB, a catalog manager, a communication subsystem, and an operation interpreter. These components allow users and programs at a given node to communicate, cooperate, and share objects with users and programs at other nodes in the network. In this architecture, the DB stores all the objects and relationships.

In the DODM, the unit of access control and sharing is a single object. However, a concept or a thing being modelled is not always described by a single object but by a collection of objects and relationships. The object taxonomy such as the five types of objects described by Kroenke (1988) is very useful. It has not only clearly described the types of objects but also the mechanisms of how to transform them into relational representation. Complex concepts or abstract data can be structured by using higher level objects structures such as complex and compound objects, or even by using association and aggregation objects. ODM and DODM lack higher semantic expressiveness. Mechanisms for integrity control and higher-level operations for DB integration are needed. The purpose here is to demonstrate a set of fundamental concepts to be used as a framework in the design and implementation of an integrated system which can be distributed in a wide area (Huhns, 1987; Ma and Lee, 1989).

## Integrated systems

Based on the existing technologies examined, individual know-how does exist. The problem remains how to integrate them into a unified whole. There are tremendous efforts undertaken by researchers and practitioners in system integration, especially in DSS/ES integrating area. Although a genuine model or theory has not yet developed for this important subject of system integration, a framework for unifying the various concepts and methodologies has gradually emerged as a guideline. The above analysis does provide us a set of rules with which a genuine model can be established in the near future.

There are several prototype or commercially available systems which can be declared as promising quasi-real integrated systems. The RKBMS designed and implemented by Chen et al. (1988) is one of the typical examples in system integration. In the RKBMS, Prolog is used as a declarative programming language. At the heart of the Prolog, there is a built-in database where facts and rules are stored. Prolog interpreter used these rules and facts to answer questions. KR can be programmed directly in Prolog.

The RKBMS is used to support KB development. There are six modules in the RKBMS (as shown in Figure 5). (1) Prolog interpreter: is used as the inference engine which consults the KB and DB for problem advising and explanation. (2) Knowledge acquisition module: acts as an interface between knowledge engineers and KB for knowledge input. (3) KB: consists of knowledge modules. (4) DB: is implemented in the RKBS which stores mass facts and constraint rules of relations. (5) User interface: is designed as a user-friendly pop-up menu system between users and the system. (6) Search engine: is built with B+ tree searching techniques for the better performance of the system.

The main features of this prototype integrated system are: (1) The extension of RKB with module facility and the integration of RKBMS with the RDBS. (2) Tightly coupling the Prolog interpreter with the database is different from the traditional convention of the RDBS. (3) The normal form of relations can be derived by using the normalization rule because some of the conventional normalization algorithms have been written in Prolog. The user has to input only the relational schema and the functional dependencies of relations. (4) The whole system is implemented in C language, except the system shell which is implemented in Prolog. They all can be executed on IBM-PC. It is easy to port to other computer systems.

![](/api/attachments/4V6T75JE/fulltext/images/0f6be5b8f2af8e0050613b4efe0a35474e2f17ed22d53284b9802557f46f29d7.jpg)  
Figure 5. The architecture of Relational Knowledge Base Management System (RKBMS)

Evidently, it is a very crude system at the present time because many things have not yet been implemented such as the inexact reasoning mechanism which is actually easy to be directly implemented in Prolog. The main feature of this prototype system is that it can be used to exemplify the concept of system integration with the latest methodologies. So far, the latest technological development in system integrating including data modelling techniques, relational data base systems, knowledge representation methodologies, object-oriented system integration, hybrid knowledge representation, and distributed system integration have been examined. It has been clearly shown that system integration is not only feasible but also imperative. The next generation of computing, especially the development of the integrated decision systems, largely depends upon the completion of the concepts and methodologies in system integration of knowledge information systems (Fishnan et al., 1989; Parsaye et al., 1989; Tsichritzis, 1987).

## Conclusion

So far, the decision trend and the requirements of integrated systems have been presented. Various integration methodologies have been analysed to exemplify that object-oriented system integration mechanisms have become unifying constructs in the proposed integrated intelligent decision system. Object-oriented system integration cannot only be applied in simple systems but also in a distributed computing and decision environment. Among the various system integration methodologies, hybrid knowledge representation combined with relational data modelling and object-oriented system integration is the best approach with the present state of the art. We conclude that integrated IDS is not only feasible but also imperative for the next generation of computing.

## References

Banerjee, Ja, Hong-Tai Chou, Jorge F. Garza, Won Kim, Darrell Woelk, Nat Ballou and Hyoung-Joo Kim. (1987) Data model issues for object-oriented applications. ACM Transactions on Office Information Systems, V, 1 (Jan.).

Bidgoli, H. (1989) Decision Support Systems. West Publishing Company.

Bonczek, R. H., Holsapple, C.W. and Whinston, A.B. (1981) Foundations of Decision Support Systems. Academic Press, Inc.

Brodie, M.L. (1989) Future intelligent information systems: AI and database technologies working together. In J. Mylopoulos and M.L. Brodie (eds) Artificial Intelligence and Databases. Morgan Kaufmann Publishers, Inc.

Chen, Fong Rong, Hsin Huei, Wang, John Shyurng Chen, and Sin Min Tsai (1988) Design and Implementation of A Relational Knowledge Base System, Proceedings of International Computer Symposium

Dahl, O.J. and K. Nygaard (1966) Simula-An algol-based simulation language. Communications of the ACM, 9.

Fishnan, D.H., Beech, D., Cate, H.PO., Chow, E.C., Connors, T., Davis, J.W., Derrett, N., Hoch, C.G., Kent, W., Lynghaek, P., Mahbd, B., Neimat, M.A., Ryan, T.A. and Shan M.C. (1989) Iris: an object-oriented database management system. ACM Transactions on Office Information Systems, 5, 1.

Gibbs, Simon and Dionysis Tsichritzis (1983) A data modeling approach for office information systems. ACM Transactions on Office Information Systems, 1, 4 (Oct.).

Goldberg, A. and Robson, D. (1983) Smalltalk-80: The Language and Its Implementation. Addison-Wesley, Reading, Mass.

Grant, J. (1987). Logical Introduction to Databases. Harcourt Brace Jovanovich.

Holsapple, C.W. and Whinston, A.B. (1987) Business Expert System. Irwin.

Hornick, M.F. and Zdonik, S.B. (1987) A shared, segmented memory system for an object-oriented database. ACM Transactions on Office Information Systems, 5, 1 (Jan.).

Huhns, M.N. (1987) Distributed Artificial Intelligence. Morgan Kaufmann Publishers, Inc.

Imielinski, T. and Lipski, W. Jr (1989) Incomplete information and relational databases. In J. Mylopoulos and M.L. Brodie (eds) Artificial Intelligence and Databases. Morgan Kaufmann Publishing, Inc.

Keene, S.E. (1989) Object-Oriented Programming in COMMON LISP. Addison-Wesley.

Kroenke, D.M. and Dolan, K.A. (1988) Database Processing. Science Research Associates, Inc., 3rd edition.

Lee, D.T. (1985) Integrated systems for transactional processing and decision support. International Journal on Policy and Information, 9, 2.

Lee, D.T. (1986) Technology Survey of Information System Development for Transactional Processing and Decision Support - A Comparative Analysis Approach. Oxford Survey in Information Technology, Vol. 3.

Lee, D.T. (1988) Expert decision support system for decision-making. Journal of Information Technology, 12, 2.

Lee, D.T. Comparative analysis of object-oriented system integration for decision-making. International Journal on Policy and Information, 12, 2 (Dec.).

Luger, G.F. and Stubblefield, W.A. (1989) Artificial Intelligence and the Design of Expert Systems. Benjamin/Cummings Publishing Company, Inc.

Lyngbaek, P. and McLeod, D. (1984) Object management in distributed information systems. ACM Transactions on Office Information Systems, 2, 2 (April).

Ma, Yung-sheng and Lee, D.T. (1989) A Framework of DSS/ES Integration. Conference Proceedings, Western DSI.

Meyer, B. (1988) Object-Oriented Software Construction. Prentice Hall.

Mittra, S. (1986) Decision Support Systems. John Wiley & Sons, Inc.

Mockler, R.J. (1989) Knowledge-Based Systems for Strategic Planning. Prentice-Hall.

Naqvi, S. and Shalom, T. (1989) A Logical Language for Data and Knowledge Base. Computer Science Press.

Newton, M. and Watkins, J. (1988) The combination of logic and objects for knowledge representation. Journal of Object-Oriented Programming, 1, 4 (Nov/Dec.).

Parsaye, Kamran, Chignell, M., Khoshafian, S. and Wong, H. (1989) Intelligent Databases. John Wiley & Sons, Inc.,

Pavelin, C. (1988) Approaches to Knowledge Representation, edited by G.A. Ringland and D.A. Duce. Research Study Press Ltd.

Purdy, A., Schuchardt, B. and Maier, D. (1987) Integrating an object-server with other worlds. ACM Transactions on Office Information Systems, 5, 1 (Jan.).

Raju, K.V.S.V.N. and Arun, K. Majundar (1988) Fuzzy function dependencies and lossless join decomposition of fuzzy relational database systems. ACM Transactions on Database Systems, 13, 2 (June).

Ringland, G.A. and Duce, D.A. (ed.) (1988) Approaches to Knowledge Representation. Research Studies Press, Ltd.

Shlaer, S. and Mellor, S.J. (1988) Object-Oriented Systems Analysis. Prentice-Hall.

Simonian, R. and Crone, M. (1988) InnovAda: true object-oriented programming in ADA. Journal of Object-Oriented Programming, 1, 4 (Nov/Dec.).

Sprague, R.H. Jr. and Carlson, E.D. (1982) Building Effective Decision Support Systems. Prentice-Hall.

Sprague, R.H. Jr. and Watson, H.J. (1986) Decision Support Systems. Prentice-Hall.

Su, Stanley, Y.W. (1988) Database Computers. McGraw-Hill.

Tanimoto, S.L. (1987) The Elements of Artificial Intelligence. Computer Science Press, Inc.

Tripathi, A. and Aksit, M. (1988) Communication, scheduling, and resource management in SINA. Journal of Object-Oriented Programming, 1, 4 (Nov/Dec.).

Tsichritzis, D., Fiume, E., Gibbs, S. and Nierstrasz, O. (1987) KNOs: Knowledge acquisition, dissemination, and manipulation objects. ACM Transactions on Office Information Systems, 5, 1 (Jan).

Turban, E. (1988) Decision Support and Expert Systems. Macmillan.

Ullman, J.D. (1988/89). Principles of Database and Knowledge-Base, Vol. I & II. Computer Science Press, Inc.

Walters, J.R. and Nielson, N.R. (1988) Crafting Knowledge-Based Systems. John Wiley & Sons, Inc.

Yao, Hsiu-Hsen and Haw Soo Kim (1988) The Aspect of Relational Data Model to Object-Oriented Knowledge Representation Formalism. Proceedings of International Computer Symposium.

Young, L.F. (1989) Decision Support and Idea Processing Systems. Wm. C. Brown Publishers.

Zadeh, L.A. (1989) Knowledge representation in fuzzy logic. IEE Transactions on Knowledge and Data Engineering, 1, 1.

## Biographical notes

Dr Daniel Lee is Professor in the School of Business Administration, and Director of MIS Program Development at the University of Texas-Pan American, USA. He has extensively researched expert decision-support systems, intelligent decision systems and object-oriented application of data modelling and knowledge representation. He has contributed many papers on these subjects to conferences and academic journals.

Address for correspondence: Professor Daniel Lee, School of Business Administration, MIS Program Development, Office of the Director, University of Texas-Pan American, 1201 West University Drive, Edinburgh, Texas USA.
