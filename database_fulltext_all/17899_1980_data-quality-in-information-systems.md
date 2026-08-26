---
otero_id: 17899
otero_key: "F46JU9S6"
title: "Data quality in information systems"
authors: "Michael L. Brodie"
year: "1980"
journal: "Information & Management"
doi: "10.1016/0378-7206(80)90035-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Data Quality in Information Systems

Michael L. Brudie

Computer Science Department Department, University of Maryland, College Park, MD 20742, U.S.A.

Until recently, data quality was poorly understood and seldom achieved, yet it is essential to the effective use of information systems. This paper discusses the nature and importance of data quality. The role of data quality is placed in the life cycle framework. Many new concepts, tools and techniques from both programming languages and database management systems are presented and related to data quality. In particular, the concept of a database constraint is considered in detail. Some current limitations and research directions are proposed.

Keywords: Data reliability, semantic integrity, correctness, data quality, software engineering, software life cycle, design, specifications, verification, validation, programming languages, databases, data models, data structures, schemas, constraints, database management systems advances in design for reliability, integrating structure and behavior.

## 1. Evolution of data design for data quality

Incorrect, unreliable software is of little use. Although software integrity and reliability problems have received considerable attention (e.g., the focus of several international conferences [49-51,54,55,78]), these issues are not completely understood and lack a uniform, theoretical base. The increasing costs, complexity, and widespread use of software now make reliability and integrity explicit objectives

![](/api/attachments/F46JU9S6/fulltext/images/30222d0a6c53c49d9e40add163dcd0fbc709bd1e36e81d94aa3f6b8d121aef35.jpg)

Michael L. Brodie is an Assistant Professor in the Department of Computer Science and is cross-appointed to the Department of Information Systems Management, both in the University of Maryland at College Park, Maryland, U.S.A. Since 1972, Dr. Brodie has been an active researcher in the areas of database management systems, programming languages, and software engineering. Professor Brodie received his Ph.D.

(1978), M.Sc. (1973), and B.Sc. (1972) degrees from the University of Toronto from 1970 to 1978 except for one term in 1976 when he was a Visiting Professor in the Departamento Informatica at the Pontifical Catholic University of Rio de Janeiro. Before taking up his current appointment, Professor Brodie spent two terms as a Visiting Professor in the Fachbereich Informatik at the Universitat Hamburg, West Germany. Dr. Brodie has authored 15 papers on topics in his research area and three papers on social issues in computing. He has presented seminars in North America, Europe, and South America.

Current research activities include: semantic data models, data abstraction, semantic integrity, programming languages, database design relational data based, and schema mappings. He is currently the co-chairman, with Dr. J.W. Schmidt of the University of Hamburg, of the ANSI/X3/SPARC-DBSG task group on a relational database standard.

Dr. Brodie has been a consultant to private organizations and to agencies of the government of Ontario, Brasil, and the U.S.A. He is a member of the ACM (Including SIGMOD, SIGSOFT, and SIGPLAN) and of the Canadian Information Processing Society, in which he was a co-founder of the CIPS Computer Ombudsman Program. Dr. Brodie is a referee for the Communications of the ACM's Communications and Transactions on Data Base Systems, the International Journal of Computer and Information Science, International Processing Letters, and the CIPS INFOR Journal.

© North-Holland Publishing Company Information and Management 3 (1980) 245–258 which are at least as important as the traditional goals of efficiency and portability.

Data quality cannot be achieved without and equal emphasis on both structure and behavior. Structure refers to states of a system while behavior refers to state transitions. Although some application properties can be described in terms of structure or behavior (e.g., relations as tables [1], or functions [13,62]), each approach provides different ways of defining and analyzing software reliability and integrity.

The needed balance can be achieved by applying recent results from programming language and database research. For some time, programming language developments have improved reliability and integrity through behavior-oriented descriptions (e.g., monitors, improved control structures and procedural abstractions, structured programming, and the understanding of programming language semantics). However, there has been little emphasis on the data-related aspects – attributes, relationships, and entities.

The database area developed primarily to deal with the structural aspects of data. It, more than any other, has contributed to our understanding of data semantics and to our ability to deal with structure through data models, data languages, and the stored data definition concept. However, there has been little emphasis on behavioral aspects. Database reliability and integrity are poorly understood. In fact, data quality maintenance is a more severe problem than program reliability [32].

Although the developments of the programming language and database areas have been substantially independent [8], the two areas have many similarities [32]. For example, data independence (the ability to consider objects in the problem domain independent of their underlying representation and to change the representation while leaving the logical properties of the objects invariant) is a common, fundamental objective. This paper proposes, for designers, developers and users of complex informations systems, an integration of recent results from both areas to achieve data quality.

## 2. Terminology and goals for data quality

"Reliability", "integrity", and "data quality" are terms frequently used with reference to database software, however, no widely held definitions exist [51]. We therefore propose working definitions and some goals.

![](/api/attachments/F46JU9S6/fulltext/images/265052a708a2fbc93d308fe5a9fe861493bb93cf3950dd989fb61e852f899cd4.jpg)  
Fig. 1. Three levels of database description.

Data quality concerns preserving the meaning of data as perceived by designers and users of a database application. This meaning is expressed in three distinct descriptions (fig. 1) as follows. The desired properties of the application are defined and described informally as system requirements which are formalized in a system specification; the specification guides the implementation of the programs and schema, which, through execution, produce a database. Each level of description acts as an authoritative data quality standard for the level below.

A database application is constructed using a data model, a schema and a database (see fig. 2). A data model provides a collection of modelling tools; i.e., data structures such as trees, networks or relations, and their associated operations with which to construct schemes. A scheme is a particular organization of data structures and operations designed to model the entities, relationships, and operations of interest to an application. A schema results from data definition and defines the acceptable database. A database is a collection of data values which represent a state consisting of the entities and relationships defined in the schema.

## 2.1. Data reliability and semantic integrity

Data quality is a measure of the extent to which a database accurately represents the essential properties of the intended application. Data quality has three distinct components: data reliability, logical (or semantic) integrity, and physical integrity. Physical integrity, the correctness of implementation details, will not be discussed here; good surveys exist elsewhere [56,72].

![](/api/attachments/F46JU9S6/fulltext/images/8b0b6ce76659bcfe722fe87e759072d797f6ad19ca5eb0ea2542459293eda61a.jpg)  
Fig. 2. Conceptual framework for databases.

Data reliability is a (statistical) measure of the extent to which a database can be expected to exhibit the externally-observable structural properties specified for a database. The process of establishing data reliability, validation, involves checking that database values obey the properties defined in the schema. For example, the answer to the query "What is Mr. Watson's telephone number?" can be validated against the format for telephone numbers. Additionally, Watson's address might be used to validate the area code and exchange; however, the remaining numbers can be checked only outside the database (e.g., "ask or phone Mr. Watson").

For a database to exhibit semantic integrity each level of its description must be consistent and complete with respect to both the rules of the description language and the description at the next higher level. The process of establishing semantic integrity, verification, requires formal proof techniques. For example, the transactions on employee "hire", "promote", and "fire" plus the schema for employees must be verified with respect to the rules of the data and programming languages used, then with respect to the employee specification. Since requirements are not formally defined and since specifications cannot be formally compared with the designers' and users' understanding of the application, there is no absolute measure of semantic integrity [21].

Reliability is a measure of robustness (e.g., the absence of system failures) while integrity is a measure of correctness [48]. An incorrect system may be seen as reliable if the harmful effects of errors do not significantly affect data access. A database may be seen as unreliable regardless of its formal correctness.

## 2.2. Goals for data quality tools and techniques

Data quality requires concepts, tools, and techniques designed specifically to achieve data reliability and semantic integrity. Concepts (e.g., data type, entity, and transaction) motivate the development of tools and techniques. A software tool is an automated device used in software development and maintenance, e.g. programming and data languages. A software technique is a methodology for the use of software tools and concepts, e.g., structured programming. Frequently, tools evolve from techniques; however, this requires considerable experience with, and testing of, the underlying concepts and techniques to ensure:

Abstraction - Ability to concentrate on the essential aspects of a problem and to ignore non-essential details (e.g., representation). Abstraction is aimed at reducing software complexity and improving data independence [64].

Semantic expressibility - Ability to define essential properties to the desired degree of accuracy with respect to the application. Compare for example, the relatively simple properties of a vector to those of an employee.

Provability - Ability to validate and verify data quality through systematic analysis and proofs.

Integration - Integration of data quality and other software development facilities so that the result is uniform and comprehensive (also, usable, flexible, understandable, etc.).

Automatic maintenance - Automatic enforcement of user defined data quality through verification, validation, and error correction.

Efficiency - Effective use of resources such as storage, computation time, and software development time. This particularly severe database problem is due to the complexity of schemas and programs and to the volume of data and transactions. For example, static analysis should be used to reduce run time maintenance of data quality.

In addition to the above goals, data-specific (i.e., database) requirements must be accommodated. Data exists independently of programs that access it and is shared amongst many users with different views of the data. Also, any meaningful data relationship should be accessible. These data-specific requirements further complicate data quality problems.

To achieve these goals, a balance s needed between structure and behavior. Data structures are more appropriate for defining static properties than are procedural abstractions, which are appropriate for defining dynamic properties (i.e., state transitions). Procedures, which can be used to define all computable functions, are semantically richer than structures. Structures express fewer properties and are simpler, hence they are more amenable to the systematic, uniform analysis necessary for the efficient, automatic maintenance of data quality.

## 3. The role of data in software development

In order to control complexity, software development can be divided into six stages:

1. analysis and definition of requirements,

2. logical design and its specification,

3. implementation design,

4. implementation construction,

5. validation and verification, and

6. operation, maintenance, and evolution.

The stages support the three levels of description depicted in figure 1. The first stages produces the requirements. The second stage produces the specification. The remaining stages deal with the implementation. Each stage has a specific purpose which permits concentration, through specialized tools and techniques, on details essential to that stage. The first three stages are particularly important since it is here that the largest proportion of total systems errors are introduced [54].

The traditional software life cycle is not directly applicable to database software, since traditional tools and techniques emphasize behavior and system structure with less concern for data. In the database area there is concern for data with less emphasis on other aspects of the life cycle. Most popular database approaches have only two stages, e.g., infological and datalogical [81], which do not permit an appropriate separation of concerns, nor do they facilitate the integration of database with software engineering technology. However, the development of a database application is a large software development project [76,81]. Data considerations must play a large role in each stage of the life cycle as follows:

Analysis and definition of requirements - The application is analyzed to develop a conceptual model of the application's entities, attributes and functions. The resulting requirements definition states, perhaps with graphical aids, what is needed for an acceptable solution.

Logical design and its specification - An abstract (implementation independent) solution is designed and defined in a formal, precise, unambiguous fashion. This provides a formal basis for data quality.

Implementation design - A particular data model is used to guide the design of a schema and operations from the specified logical properties. The design is expressed using specification languages and graphical aids.

Implementation construction - The schema and transactions are coded to produce an executable solution (a schema and programs). A high level programming language augmented by the data definition and data manipulation languages (DDL, DML respectively) is used.

Validation and verification - Data reliability is validated by demonstrating that structural and behavioral properties are satisfied (e.g., the database satisfies its schema). Semantic integrity is established by verifying the schema and programs.

Operation, maintenance, and evolution - Specifications change as the system is used and evolves. The system must be appropriately modified. Due to problems introduced in earlier stages, especially poor data quality, this stage generally accounts for two thirds of the development costs [54,55,83].

The main benefit of using of the software life cycle is its aid in managing complexity. These benefits require a complete development of each stage, validation and verification of each descriptive level, and feedback so that problems at one level (e.g., introduced during system evolution) can be resolved at the appropriate level. For example an apparent performance problem, if simple, may be resolved by altering the implementation; if more complex it may require a redesign of the implementation or even a respecification of the logical design.

## 4. Concepts, tools, and techniques for data quality

Most software tools and techniques aim at some aspect of integrity and reliability. This section presents a survey of recent contributions to data quality categorized by their role in the software life cycle. The operations and maintenance stage is not considered here; surveys of this area exists elsewhere [72,77].

## 4.1. Data quality in programming languages

## 4.1.1. Requirements, specifications, and design

The programming language and software engineering areas have contributed directly to improving data quality [54,55]. SOFTECH's structured analysis and design technique (SADT) [57] provides graphic tools to describe a system in terms of data as inputs to processes, and processes as data manipulators. Structured design (SD) [82] provides techniques for producing modules which are independent, single, well-defined functions and which communicate through parameters to which data flow analysis can be applied. SD also provides techniques for measuring software quality. Structured Systems Analysis [25] extends SD by considering data specific requirements for database design, such as data dictionary [6] and normalization [3], and some concern for consistency and completeness. Two popular program design techniques by Jackson [33] and Warnier [73] attempt to develop programs by considering the structural properties of input and output. Although these techniques emphasize a formal definition of structure and data flow analysis, there is little guidance for data quality and data specific requirements; both techniques emphasize data external to programs. A number of other techniques have also been introduced but are in limited use [44,47,48,80/I]. They support software specifications with some concern for precision, completeness, and reduced complexity.

The information systems area has produced other systems analysis tools and techniques [15,68] with primary emphasis on information analysis and documentation. Two such facilities are the information algebra and PSL/PSA. In the early 1960's the CODASYL Development Committee introduced the information algebra as a formal specification technique; PSL/PSA (Problems Statement Language/Problem Statement Analyzer) are tools used to define and analyze some properties of systems (e.g., system boundaries, entity types, and relationships). PSA is used to analyze properties defined in PSL for some forms of consistency and precision. The tools permit a designer to make some elementary data quality checks by means of queries and tables.

## 4.1.2. Design and implementation

The primary programming language concept for data quality is the data type: a set of values together with a set of operations over those values. Two main purposes of a data type are:

• to define structural and behavioral properties;

• to maintain those properties automatically.

These purposes are supported by many well-known methods, e.g., compile and run time tools for syntactic and semantic type checking, type coercion and type conversion.

Typically, data types are semantically weak. For example, stacks, queues, vectors, matrices, and lists are simple compared with the large number of attributes, relationships, and operations that must be represented for “real world” entities such as employees, bank accounts, and departments in an enterprise. To improve the semantic integrity of data types, several procedural tools have been developed. Error and exception handling tools [43], such as on units in PL/1 and COBOL, permit programs to detect abnormal or erroneous conditions and to call predefined actions. Over 40% of COBOL code is dedicated to this form of semantic integrity checking [24]. Fault tolerance [56] is a technique which is based on the principle that software should tolerate errors that are only symptoms of real errors. In one approach, recovery blocks provide alternative code to allow a task to complete after it has failed to meet some completion criteria. These general, procedural tools are semantically rich, but pose significant design and verification problems.

A non-procedural approach to improving the semantic integrity of data types is through assertions [80/II]. Assertions in first order predicate calculus can be used to define a wide range of invariants and pre- and post-conditions for program segments. In some cases, assertions can be proven, with respect to the program text, otherwise the conditions must be tested at run time.

Structured programming [17] and data abstractions [28,37] can be used to improve data quality. Although structured programming includes concepts such as the successive refinement of programs and data, the emphasis is on behavior. One important data abstraction concept is the encapsulation of data values and their operations, thereby constraining data access through procedures that ensure data quality. To date, data abstraction methods are not yet in widespread use.

## 4.1.3. Verification and validation

The most important validation tools are those for static and dynamic type checking (e.g., compile and run time checking of type use, scope, aliasing [16,35] and the construction of a data type cross reference list). Early techniques, such as data preparation and pre-processing, check digit, and error correcting codes are also in widespread use. A more recent technique, data flow analysis [23], is a systematic way of scanning a program to see how variables are used and thus to infer particular properties of the program. Another widely used technique, for which a theory is evolving [80/II], is the use of test data. This includes the static and dynamic analysis of programs as well as symbolic execution of programs [31] to generate test data. Other validation techniques and tools exist for modules and module integration [80/II,83].

Of the various program verification techniques [31,80/II), the inductive approach is most widely used. Each block of code is bracketed by initial and final assertions about relations among program variables (so that each program loop is cut by an assertion). Mathematical induction is used to prove that if the initial assertion is true no logical path through the block can result in a violation of the final assertion. In this way, each block is verified so that the final output assertion will be true whenever the program terminates.

## 4. Data quality in databases

The most important database contribution is the database constraint. A database constraint is any property of the application that must be represented in the database to achieve an acceptable level of data quality [9,39]. Structural properties are state constraints while behavioral properties are state transition constraints.

The constraint concept can be used for data quality throughout the software life cycle. In the requirements stage, the perceived application properties must be described as constraints (e.g., what is constrained? By what? Under what conditions? What are the consequences of constraint violation?). Next, constraints must be specified formally and used to guide implementation design. Then, tools are used to implement the constraints. A schema and its related programs must represent and enforce all constraints that a database must satisfy. All constraints must be verified and validated. Finally, constraint violations must be handled during operation and maintenance and the constraints may need modification as the system evolves.

There are three types of constraints: inherent, explicit, and implicit [7]. Ideally, each programming and data language has some clearly defined constraints inherent in the structures and operations of the language; referred to as semantics of the programming language or data model, these inherent constraints cannot be violated within the language. Examples of inherent constraints are: the hierarchic properties of IMS; the uniqueness of tuples and properties of keys in the relational model; and the rules governing owner-coupled sets in the DBTG data model. Explicit constraints are those directly expressible using a programming or data language. They involve the specialization or particular use of inherent constraints, such as the properties of a particular data element. Implicit constraints are consequences of other constraints, e.g., side effects of procedures; inferences drawn from a set of assertions; and record access restrictions resulting from storage, removal, and set selection constraints on DBTG owner-coupled sets.

Two other database concepts contribute directly to data quality, the database administrator role and the data dictionary/directory. Among the many database administration tasks is the responsibility for data quality. Data quality must be maintained over the database for all applications, each of which may have a different set of constraints. Although it is not agreed exactly what is to be included in a data dictionary/directory, it is generally viewed as being a centralized description of the terminology and constraints to be applied in the database [6]. A data dictionary/directory is created in the requirements stage and may be used to guide each successive stage in achieving data quality.

## 4.2.1. Requirements

In the informal process of database requirements analysis, observation, intuition, interaction with users, and some data model concepts are used to develop an conceptual model of the application. Although the importance of data quality is recognized [67], only a few modelling methodologies [36,52,67,81] address these issues.

A database requirement should describe all constraints over the entities, attributes, and relationships that constitute the conceptual model. Relationships may be perceived between any combination of attributes, entities, and other relationships. Some examples of state constraints at this level are: Entities must be uniquely identifiable and may exist only under conditions defined in terms of specific attributes and relationships. Relationships may involve one set and its subsets defined by some membership rule (e.g., department managers within the employees of an enterprise) or two sets characterized by such constraints as: degree or functionality (e.g., 1:1, 1:N, N:M), direction (e.g., managers manage employees), dependence (e.g., a department must have a manger but an employee need not have a spouse), and some logical constraints (e.g., a student may be enrolled in a course under certain conditions). Additionally, applications may require relationships to be ordered (e.g., employees by department and name) or quantified (e.g., a department must have at least 5 and at most 15 employees).

State transition constraints may be used to ensure the correct manipulation of entities through pre-conditions (e.g., before a department manager is fired, a new manager must be appointed), post-conditions (e.g., employee count must be updated after a hiring or firing), and transition conditions (e.g., ages may not decrease). Access and security rules may be expressed separately or through state and state transition constraints.

## 4.2.2. Specification

Until recently [7,22,39] database systems have not been formally specified; however, some specification techniques are widely used. Bachman's structure diagrams and its variants [25,46], relational schemes [70], and generalization and aggregation hierarchies [64] permit a graphic, somewhat abstract definition of the constraints in a scheme. Functional and multivalued dependencies [3] permit a formal specification of specific types of constraints. Some formal techniques based on set theory and the relational data model are also used [68,77].

## 4.2.3. Implementation design

Several approaches to database design provide tools and techniques for data quality. Perhaps the most effective [67] and widely used are interviews with potential database users over schema design to ensure that the scheme fulfills their requirements. Another technique is the use of functional dependencies to synthesize a relational schema which is free from certain update, insert, and deletion anomalies [5]. Due to the relatively limited semantics of functional dependencies, this technique is best used to augment other design techniques. Finally, some semi-automated design tools, notably the Data Base Design Aid [18], can be used to ensure a degree of consistency and that certain data model rules are satisfied.

## 4.2.4. Implementation construction

Most data quality tools and techniques exist at the implementation stage to construct representations with properties that “simulate” some specified properties of entities, attributes, and relationships. The most important aid is the data model underlying the languages being used, since the inherent constraints or semantics of the data model establish the framework for constraint representation [12]. The principle explicit constraint tools available in DDLs and DMLs are data types, subschema definition, and state assertions for state constraints, and locking, transactions, and transition assertions for state transition constraints.

Data types. Most data models include concepts for relationships defined in term of entities which are in turn defined in terms of attributes which are based on value sets or domains. Hence, DDLs provide base types for representing domains and rules for constructing attribute types (e.g., fields) from base types, entity types (e.g., segment and record types) from attribute types, and relationship types (e.g., relations, owner-coupled sets, and hierarchies) from entity types.

In some DDLs, conventional data types (e.g., fixed, designing such facilities is to modify tools and techniques from programming languages and software engineering to meet database requirements [9,11,22, 25,39,58,59,64,65,74,76,81]. This approach is leading towards a mutual concern for structural and behavioral aspects of databases. In the remainder of this section, data quality limitations and research directions are discussed for each stage of the software life cycle.

```txt
type daytype = 1..31;
    monthtype = (January, February, March, April, May, June, July, August,
    September, October, November, December);
    yeartype = 1900..2000;
    datetype = monthtype
    " "
    daytype
    " "
    yeartype;
```  
Fig. 3. Constraints expressed in data types.

## 5.1. Requirements analysis and definition

Database requirements analysis is perhaps the most difficult and least constrained development task due, in part, to our limited knowledge of data semantics. Research in this area [52,67] deals more with modelling methodologies than with establishing an authoritative standard for data quality. Database requirements may be kept in a data dictionary, although there is little consensus as to its purpose or form.

## 5.2. Specifications

A formal specification not only guides design and implementation, it also provides a basis for semantic integrity verification. Formal specifications for programs and schemas are not widely used. Techniques currently used [44] are still problematic [28,41] and have not yet been shown to be practical for large scale systems. However, database specification languages are being developed together with related techniques for design and verification [7,22,39,65].

## 5.3. Design

Design aids are required for data quality. Formal techniques, such as normalization, tend to produce semantically weak schemas. Informal techniques are largely intuitive and tend to lack specific data quality facilities resulting in schemas that may be hard to analyze for data quality. Some combination of the two techniques should be used to enumerate alternatives and evaluate them with respect to data quality. Current research projects for database design include: the development of a theory of database design [16,36]; constructing automated design tools [27]; and the application of software engineering tools and techniques to database design [74,76,81]. Goals for this research include those of data quality.

## 5.4. Implementation

The primary limitations of tools at the implementation stage concern the weak semantics of data models and data types, and the generality of procedures needed to specify constraints not expressible using the model. Database semantic integrity is limited by the inherent constraints of the data model being used. For given applications, some data models are too restrictive (e.g., representing N : M relationships in hierarchies) while others are too general (e.g., the semantic overloading of relations) [34]. Consequently, new data models are being developed [12] to achieve semantically rich tools which support abstraction. A number of contributions in this regard concern the extension of the data type concept. These include: generalization [64], which may be used to define hierarchies of subtypes (e.g., student, tutor, and professor as subtypes of person); strong domain definition by means of string specifications [42]; strong typing to restrict type compatibility [35]; a partial solution for dealing with null or missing values [71]; and a rich set of data structuring rules, called a data type algebra which includes generalization, predicate calculus expressions, and absolute quantification [7,8]. These type extensions provide a rich set of inherent constraints and greater control over representations in order to improve data quality.

Frequently, the data types and operations (i.e., the data model) of a programming language used to access a database differ distinctly from those in the data model underlying the database. The translation or interface needed between the two may adversely affect data quality since design, implementation, and verification may involve two data models. To reduce these problems, database and programming language concepts are being integrated to provide database access through the data types of high level programming languages [58,59,75].

Typically, large numbers of constraints are expressed using procedural tools such as triggers and database procedures. Due to the low level, unconstrained access provided by procedures and the lack of a uniform "procedure schema", these constraints are difficult to design, code, and modify consistently, let alone to understand, optimize, and verify. Further these constraints are validated at run time. Indeed, conventional procedural tools satisfy few of the goals for data quality tools. Assertions, however, meet most of those goals. The potential use of data abstraction to combine the advantages of data types and procedures is dealt with later.

## 5.5. Validation and verification

Currently, data quality checking relies heavily on run time validation. Although it is an open problem as to what must be checked at run time and what can be checked statically, the objective is to increase the use of both verification at the implementation and specification levels and optimization of run time validation. Various compile time, run time, and post-execution time methods for the execution of semantic integrity constraints are being developed and evaluated for efficiency [2,30]. Improvements in program verification are being made through better type checking and other compilation techniques [16,35] and through the development of formal techniques [26]. While formal verification techniques are not yet practical [21], they do lead to a greater understanding of programs and data.

An area that requires research is schema verification. Schemas containing procedure entries and representational details, as do DBTG schemas, are more difficult to analyze than are those expressed in more abstract terms such as relations, functional dependencies, and predicate calculus assertions. Schema verification techniques for the more abstract schemas are being developed in terms of normalization theory $[20,40]$ and logical calculus $[7,45]$ . These techniques can also be used to deduce implicit constraints and to answer queries.

## 6. Integrating structure and behaviour for data quality

Although verification techniques, formal data semantics, and data model theory may aid significantly in achieving data quality, practical results from these theoretical areas are not immediately forthcoming [21,26]. Practical solutions can be expected sooner from research that addresses limitations of existing data quality tools and techniques, e.g., the integration of structural and procedural tools for constraint definition through data abstraction. Over the past few years, advantages have been claimed for data abstraction facilities in programming languages [28, 37,38,61]. Recently, these results have been applied to databases [11,22,58,60,74,76].

In terms of database constraint implementation, there is a need for integrating structural and behavioral descriptions of applications. Constraint definition tools are either structural or procedural. Neither type satisfies all the goals given in section 2. Procedural tools are semantically rich and are essential for state transition constraints. However, they are difficult to verify and analyze for consistent and efficient constraint maintenance, and they do not address data specific requirements. Structural tools can be used to define a much smaller class of constraints related to the data specific requirements, however, their simple, abstract nature makes them more amenable to verification and optimization.

In most data languages, structural and procedural tools for constraint definition are poorly integrated. High level entity types, such as employees, can be accessed through low level, unconstrained operations, such as insert, update, and delete. In order to ensure that all related entities remain consistent, access should be restricted to meaningful operations, such as "hire", "promote", and "fire", which implement the appropriate constraints, such as checking current salary scales and altering related employee information in the department entity. The entity type employee together with its meaningful operations is an example of a data abstraction. Experience with data abstraction tools in programming languages [38,61] suggests that structural and procedural tools can be integrated to combine their individual benefits and to permit the construction of semantically rich data types.

Data abstraction has been investigated most extensively in the programming language area in terms of abstract data types [37]. An abstract data type is a user defined class of objects which is completely characterized by a representation-free specification of the operations available on those objects. This notion includes concepts for both the specification and implementation levels [41]: first, a type specificatin, which names the operations for the type and formally defines their properties, and second, an implemented data type that satisfies the specification. This separation of concepts gives a degree of data independence which provides a basis for abstraction, verification and optimization.

To achieve data abstraction for databases through abstract data types, several problems [41] and potential conflicts must be resolved. Current specification techniques require mathematical sophistication and pose difficulties for constraint definition. The resulting specifications tend to be complex and difficult to modify. Abstract data types do not address the data specific requirements. Behavioural properties are defined explicitly and formally while the abstract structural properties of objects are only implied. The database need for data relatability seems to conflict with the modularity of abstract data types. Also, major problems arise from the complexity of database applications: specification and verification of large systems of complex types; communications between large numbers of modules; and the design and many highly integrated abstract objects.

The use of abstract data types in databases would result in changes such as the inclusion in the schema of constrained operations which define the behavioral properties of the data types. This extended schema would then be a collection (e.g. library [38] of data abstractions and would include all constraints on the database. A database would be a collection of instances of the data abstractions – structured values accessible only through meaningful operations. Data abstraction tools to define these extended schemas would require the integration of current data model and programming language concepts and tools.

This paper has presented many of the concepts being exploited in database abstraction which are drawn from the areas of databases, programming languages, information systems, and software engineering. The database abstraction approach to the design and development of complex database-intensive applications is being actively and fruitfully pursued. The bibliography contains references to much of this work [7-13,22,39,42,58,69,62,64,65,74-76,81].

## References

[1] M.M. Astrahan et al., System R: relational approach to database management. ACM TODS 1, 2 (June 1976).

[2] D.Z. Badal and G.J. Popek, Cost and performance anal-

ysis of semantic integrity validation methods, in [53].

[3] C. Beeri, P.A. Bernstein and N. Goodman, A sophisticated's introduction to database normalization theory. in [79].

[4] C. Beeri and P.A. Bernstein, Computational problems related to the design of normal form relational schemas. ACM TODS 4, 1 (March 1979).

[5] P.A. Bernstein, Synthesizing third normal form relations from functional dependencies. ACM TODS 1, 4 (Dec. 1976).

[6] The British Computer Society Data Dictionary Systems working Party Report. SIGMOD RECORD 9, 4 (Dec. 1977).

[7] M.L. Brodie, Specification and verification of database semantic integrity. Ph.D. diss., CRSG-91, University of Toronto, March 1978.

[8] M.L. Brodie, Data types and databases. IFSM TR No. 37, University of Maryland, Dec. 1978.

[9] M.L. Brodie, The application of data types to databases. Semantic integrity. Information Systems 5, 4 (1980).

[10] M.L. Brodie, Axiomatic definitions of data model semantics. IFSM TR No. 41, University of Maryland, Feb. 1979.

[11] M.L. Brodie and J.W. Schmidt, What is the use of abstract data types? in [43].

[12] J. Bubenko, Data models and their semantics. INFO-TECH STATE-OF-THE-ART Report on data design, Sept. 1979.

[13] P. Buneman and R.E. Frankel, FQL - A functional query language, ion [53].

[14] CODASYL Data Description Language Committee, Journal of Development 1978.

[15] J.D. Couger, Evolution of business systems analysis. ACM Computing Surveys 5, 3 (Sept. 1973).

[16] P. Cousot and R. Cousot, Static determination of dynamic properties of generalized type unions. SIGPLAN Notices 12, 3 (March 1977).

[17] O.-J. Dahl, E.W. Dijkstra and C.A.R. Noare, APIC Studies in Data Processing No. 8: Structured Programming, Academic Press, New York, 1972.

[18] Data Base Design Aid: Designer's Guide IBM No. GH20-1627.

[19] Data Management System (DMS 1100) Scheme Definition, Univac No. UP-7907.

[20] U. Dayal and P.A. Bernstein, On the updatability of relational views, in [79].

[21] R.A. De Millo, R.J. Lipton and A.J. Perlis, Social Processes and proofs of theorems and programs. Comm. ACM 22, 5 (May 1979).

[22] H. Ehrig, H.J. Kreowski and H. Weber, Algebraic specification schemas for data base systems. In [43].

[23] L.D. Fosdick and L.J. Osterwell, Data flow analysis in software reliability. ACM Computing Surveys 8, 3 (Sept. 1975).

[24] J.P. Fry and E.H. Sibley, Evolution of database management systems. ACM Computing Surveys 8, 1 (March 1976).

[25] C. Gane and T. Sarson, Structured Systems Analysis: tools and techniques, Prentice-Hall, Englewood Cliffs, N.J., 1979.

[26] S.L. Gerhart, Program verification in the 1980's: Problems, perspectives, and opportunities. ISI/RR-78-71, University of Southern California, Aug. 1978.

[27] R. Gerritsen, Steps towards the automation of database design, in [52].

[28] J.V. Guttag, Notes on Type abstraction, in [51].

[29] M.M. Hammer and D. McLeod, A framework for data base semantic integrity, in [50].

[30] M. Hammer and S.K. Sarin, Efficient monitoring of database assertions, Proc. ACM-SIGMOD 1978 Int'l. Conf. on Management of Data, ACM, N.Y., (May 1978).

[31] S.L. Hantler and J.C. King, An introduction to proving the correctness of programs. ACM Computing Surveys 8, 3 (Sept. 1976).

[32] C.A.R. Hoare, Data reliability, in [49] and [80/IV].

[33] M.A. Jackson, Principles of Program Design. Academic Press, New York, 1975.

[34] W. Kent, Limitations of record-based information models. ACM TODS 4, 1 (March 1979).

[35] B.W. Lampson, J.J. Horning, B.L. London, J.G. Mitchell and G.J. Popek, Report on the programming language EUCLID. SIGPLAN Notices 12, 2 (Feb. 1977).

[36] B. Lungefors, Information systems theory. Information Systems 2, 209–219 (1977).

[37] B.H. Liskov and S.N. Zilles, Specification techniques for data abstractions. IEEE Trans. on Software Engineering 1, 1 (March 1975) also in [80/I].

[38] B.H. Liskov, A. Snyder, R. Atkinson and C. Schaffert, Abstraction mechanisms in CLU. Comm. ACM 20, 8 (Aug. 1977).

[39] P.C. Lockemann, H.C. Mayr, W.H. Weil and W.H. Wohlleber, Data abstractions for database systems. ACM TODS 4, 1 (March 1979).

[40] D. Maier, A. Mendelson and T. Sagiv, Testing implications of data dependencies, to appear ACM TODS.

[41] M.E. Majster, Data types, abstract data types, and their specification problem, to appear in Theoretical Computer Science.

[42] D.J. McLed, High level domain definition in a relational database system. Proc. Conf. on data: abstraction, definition and structure, SIGPLAN Notices, Vol. II 1976 special issue.

[43] P.M. Melliar-Smith and B. Randell, Software Reliability: the role of programmed exception handling, in [78].

[44] P.M. Melliar-Smith, Tutorial on System-Specifications, IEEE Computer Society, April 1979.

[45] J, Minker and G. Zanon, Consistency and integrity in databases. TR-723, Computer Science, University of Maryland, 1979.

[46] I. Palmer, Practicalities in applying a formal methodology to data analysis, in [52].

[47] D.L. Parnas, A technique for software module specification with examples. Comm. ACM 15, 5 (1970).

[48] D.L. Parnas influence of software structure on reliability, $\therefore 4.1$ and in [80/I].

[49] Proc. 1975 Int'l. Conf. on Reliable Software. SIGPLAN Notices 10, 6 (June 1975).

[50] Proc. 2nd Int'l. Conf. on Software Engineering, San Francisco, CA, October 1976.

[51] Proc. Specifications of Reliable Software, IEEE Computer Society, May 2–4, 1979.

[52] Prov. NYU Symposium on Database Design. New York University, New York, May 1978.

[53] Proc. ACM-SIGMOD 1980 Int'l. Conf. on Management of Data, ACM N.Y., May 1979.

[54] C.V. Ramamoorthy and H.H.So, Software requirements and specifications: status and perspectives, in [55].

[55] C.V. Ramamoorthy and R.T. Yeh, Tutorial: Software methodology, IEEE Computer Society, 1978.

[56] B. Randell, P.A. Lee and P.C. Treleaven, Reliability issues in computing system design. ACM Computing Surveys 10, 2 (June 1978).

[57] D.T. Ross, Structured Analysis (SA): A language for communicating ideas. IEEE Trans. on Software Engineering 3, 1 (Jan. 1977).

[58] L.A. Rowe and K.A. Shoens, Data abstractions, views and updates in RIGEL, in [53].

[59] J.W. Schmidt, Some high level language constructs for data of type relation. ACM TODS 2, 3 (Sept. 1977).

[60] J.W. Schmidt, Type concepts for database definition, in B. Schneiderman (Ed.), Databases: Improving Usability and Responsiveness, Academic Press, New York, 1978.

[61] M. Shaw, W.A. Wulf and R.L. London, Abstraction and verification in ALPHARD. Comm. ACM 20, 8 (Aug. (1977).

[62] D. Shipman, The functional data model and the data language DAPLEX, to appear in ACM TODS.

[63] J.M. Smith, Comments on papers "A software engineering view of database management" by A.I. Wasserman and "A software engineering view of database systems" by H. Weber, in [79].

[64] J.M. Smith and D.C.P. Smith, Database abstractions: Aggregation and generalization. ACM TODS 2, 2 (June 1977).

[65] J.M. Smith and C.D.P. Smith, A database approach to software specification. Computer Corp. of America, CCA-79-17, (April 1979).

[66] M. Stonebraker, Implementation of integrity constraints and views by query modification. Proc. ACM-SIGMOD 1975 Int'l. Conf. on Management of Data.

[67] B. Sungren, Data base design in theory and practice: Towards an integrated methodology, in [79].

[68] W.M. Taggart and M.O.A. Thorp, A survey of information requirements analysis techniques. ACM Computing Surveys 9, 4 (Dec. 1977).

[69] D. Tsichritzis and A. Klug (Eds.), The ANSI/X3/SPARC DBMS Framework. Report of the Study Group on Database Management Systems. Info. Systems 3, 4 (1978).

[70] J.D. Ullman, Theory of Relational Databases, forthcoming book.

[71] Y. Vassiliou, Null values in database management: a

denotational semantics approach, in [53].

[72] J.S.M. Verhofstad, Recovery techniques for database systems. ACM Computing Surveys 10, 2 (June 1978).

[73] J.D. Warnier, Logical Construction of Programs. Van Nostrand Reinhold, New York, 1974.

[74] A.I. Wasserman, A software engineering view of database management, in [79].

[75] A.I. Wasserman, The data management facilities of PLAIN, in [53].

[76] J. Weber, A software engineering view of database systems, in [79].

[77] G. Wiederhold, Database design. McGraw-Hill, New York, 1977.

[78] D.B. Wortman (Ed.), Proc. An ACM Conf. on Language Design for Reliable Software, in SIGPLAN Notices 12, 3 (March 1977).

[79] B. Yao (Ed), Proc. 4th Int'l. Conf. on Very Large Data Bases. West Berlin, Germany, Sept. 13–15, 1978.

[80] R.T. Yeh (Ed.), Current Trends in Programming Methodology. Prentice Hall, Englewood Cliffs, N.J.
Vol. I: Software Specifications and Design, 1977.
Vol. II: Program Validation, 1977.
Vol. IV: Data Structuring, 1978.

[81] R.T. Yeh, A. Araga and Chang, P., Software and database engineering – towards a common design methodology. SDBEG-6, Computer Science, University of Texas, March 1979.

[82] E. Yourdon and L.L. Constantine, Structured Design. Yourdon Press, 1978.

[83] M.V. Zelkowitz, A.C. Shaw and J.D. Gannon, J.D. Principles of Software Engineering and Design. Prentice-Hall, Englewood Cliffs, N.J., 1979.
