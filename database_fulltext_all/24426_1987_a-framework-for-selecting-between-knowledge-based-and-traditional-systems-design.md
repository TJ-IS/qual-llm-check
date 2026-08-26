---
otero_id: 24426
otero_key: "459XWN6U"
title: "A Framework for Selecting between Knowledge-based and Traditional Systems Design"
authors: "Thomas J. Murray; Mohan R. Tanniru"
year: "1987"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1987.11517785"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Framework for Selecting between Knowledge-based and Traditional Systems Design

Thomas J. Murray & Mohan R. Tanniru

To cite this article: Thomas J. Murray & Mohan R. Tanniru (1987) A Framework for Selecting between Knowledge-based and Traditional Systems Design, Journal of Management Information Systems, 4:1, 42-58, DOI: 10.1080/07421222.1987.11517785

To link to this article: https://doi.org/10.1080/07421222.1987.11517785

![](/api/attachments/459XWN6U/fulltext/images/ccb3012859f8caabd12cc4881c96be1f420fe4da1e9a21540710e2a6c82aeba4.jpg)

Published online: 23 Dec 2015.

![](/api/attachments/459XWN6U/fulltext/images/47b0aae84945a20bbdb19fb8e2e8d6f762af411305fac1c87661777591739701.jpg)

Submit your article to this journal ↗

![](/api/attachments/459XWN6U/fulltext/images/c1a7ea24f93bc446cdc69b6e619282523174d91f5712a9f72660555d8e7f7908.jpg)

Article views: 1

![](/api/attachments/459XWN6U/fulltext/images/c23147f1527a94ae661569bb1e0c2bb89b8a9591e34e22d69994be4e06af008b.jpg)

View related articles ↗

![](/api/attachments/459XWN6U/fulltext/images/cbaec0cb679b5c0cdc2bb2d27fdf650e120756c1616e96e52db32b9ee0391d82.jpg)

Citing articles: 6 View citing articles ↗

# A Framework for Selecting between Knowledge-based and Traditional Systems Design

THOMAS J. MURRAY and MOHAN R. TANNIRU

THOMAS J. MURRAY is an associate professor of management information systems (MIS) at Syracuse University. He received his Ph.D. in 1973 from the University of Massachusetts. He has published in a number of journals and is the author of a recent book, Computer Based Information Systems.

MOHAN R. TANNIRU is an associate professor of MIS at Syracuse University. He received his Ph.D. in 1978 from Northwestern University. He has published in journals and presented papers at various meetings. His research interests are in the areas of systems analysis, decision support systems, and expert systems.

ABSTRACT: Extensive coverage of knowledge-based languages has appeared in the recent literature. However, there has been no discussion of the criteria to be used in selecting between a knowledge-based approach and a traditional, that is, non-knowledge-based, approach for a particular application. This paper presents a framework of application-based criteria to assist in this selection. It also applies this decision framework to a number of real and hypothetical applications.

KEY WORDS AND PHRASES: Knowledge-based language, systems design, expert system.

## Introduction

RECENT INTEREST IN THE USE of knowledge-based languages for business applications raises a question that has been asked whenever a new programming language is introduced—what benefits accrue to the designer or user by developing application systems in this new language? This basic question can be rephrased as follows: Under what conditions does it make sense to use a knowledge-based design approach over a non-knowledge-based (or traditional) approach? Knowledge-based design represents knowledge as rules and assertions and uses techniques such as inference mechanisms to manipulate that knowledge, while traditional design uses data and models for representation and algorithmic procedures for their manipulation. Given that only a limited number of applications have been successfully implemented using a knowledge-based system, it is difficult to draw generalizations from this limited set. However, one can develop “generic” application design characteristics that are not dependent on any particular implementation philosophy. This paper defines these characteristics and compares the way in which knowledge-based languages and traditional, that is, non-knowledge-based, languages handle these features. Such a comparison may facilitate a normative evaluation of these two approaches and can act as a guide in selecting one type of programming system over another in order to meet a specific application need.

The fifth generation of software, that is, knowledge-based software, has evolved primarily out of the artificial intelligence field $[1]$ . Whereas the first four software generations, that is, machine language, assembly language, higher symbolic languages, and fourth generation languages, showed dramatic shifts toward higher-level program statements and ease of use, knowledge-based software has broken with this trend. The fifth generation has evolved in part to provide more powerful knowledge representation and manipulation. As a result, the arguments for and against the use of a higher generation language that have been used to date cannot be directly applied to the fifth generation.

The successful development of a system relies heavily on an accurate description of a problem (specification) and an efficient design and coding of a program or a set of programs (implementation) that will address this problem $[18]$ . The specification of a problem requires an understanding of the underlying problem structure and a representation of the data inputs and outputs (data I/O) that will either influence or be influenced by the problem structure. The system implementation requires a language to model the problem structure and a storage structure to store/access information on the data I/O.

Knowledge-based languages are described as being well suited for the “problem specification” phase when the application problems are extremely complex and dynamic [7]. It is not clear, however, which of these language environments (knowledge-based or traditional) is most appropriate for the implementation of these application systems. Deciding when to use which language environment for an application system environment can make the difference between success and failure in the implementation of the system.

Bonczek, Holsapple, and Whinston [2] present a framework that classifies the problem environment using model and data environments. This classification can be used to select a specific “technical environment” for design and implementation in order to meet the needs of a given “problem environment.” Problem structure, to a large degree, will influence the technical environment that is chosen for system implementation. According to the data/model framework presented by Bonczek, Holsapple, and Whinston, a highly structured problem environment (such as “operations control”) may use an explicit definition of model logic and the associated data paths, while a semistructured to unstructured problem environment (such as “management control” and “strategic planning”) may prefer the flexibility afforded by the model-generating and data base procedures.

The literature on decision making shows that as one moves from a structured to an unstructured environment (lower-level to top management) data and model needs change rather significantly $[8, 11, 12, 19, 23]$ . This is due to the fact that data used in unstructured environments are generally more qualitative and the modeling less amenable for prescriptive approaches than data used in structured environments $[11]$ . Such unstructured decision-making environments, thus, need support for processing symbolic knowledge using inferential procedures. The framework suggested by Bonczek, Holsapple, and Whinston, while specific in the nature of the data and model environment needed to support structured and semi-structured environments, only hints at the possibility of the use of artificial intelligence techniques to support unstructured problems.

In this paper a set of design characteristics is used to illustrate how knowledge-based and traditional (procedure-based) languages can be used to implement an application system. These contrasting features will in turn allow the formulation of a set of guidelines for selecting a particular language environment to implement an application. The next section will briefly introduce the reader to knowledge-based languages. The third section will identify the major design characteristics used to implement an application and show how the two language environments support such design. The last section will take a set of implemented and one hypothetical application to show how these application design characteristics can be used to select a particular environment for an implementation.

## Knowledge-based Systems

A KNOWLEDGE-BASED LANGUAGE is a program (or a set of programs) which carries out “reasoning” to solve a problem. Essentially, a knowledge-based language uses knowledge, that is, facts and relationships (or rules), and heuristics stored in the system to infer new facts.

Certainly the most common application of the knowledge-based approach has been in expert systems [13]. An expert system is software that performs a highly specialized task that would normally require human expertise, and the representation and manipulation built into this system is primarily symbolic. The task or domain expertise is incorporated into the expert system.

Although the terms “knowledge-based system” and “expert system” are often used interchangeably, this is not quite correct. Expert systems can and have been implemented using traditional languages, for example, EXPERT, which was programmed in FORTRAN [24]. However, the power and ease of use of knowledge-based languages make them the usually preferred tool of choice. In addition, there are applications other than expert systems that can be implemented using the knowledge-based approach. In general, the application design characteristics should assist in the selection of the most appropriate approach. Figure 1 is a generalized representation of a knowledge-based system. Any particular system will probably have additional components. However, most will have the common subsystems shown in Figure 1.

![](/api/attachments/459XWN6U/fulltext/images/5ff543597c4bb26700543fa372787eb338ce9f8e99f688c19d4b82a86ac3d3dd.jpg)  
Figure 1. Generalized Knowledge-based System

The inference engine contains certain built-in procedures for search and goal-seeking. It carries out searches of the knowledge base to satisfy a particular goal. The knowledge base consists of the facts and rules of the system. The rules are the mechanisms used to infer new facts. The explanation system, if it exists, provides a trail of reasoning to show how a goal or the result of an inquiry was obtained. This system differs from a simple trace function in that it eliminates false trails and backtracking. It provides a compact, clear chain of reasoning which starts at the problem statement and ends at the result.

The knowledge acquisition system provides the knowledge engineer with the ability to update the knowledge base. This system includes an I/O interface for the engineer to facilitate easy maintenance of the knowledge base. This is critical since the implementation of a knowledge-based system is highly iterative. Both the rules and facts may be changed by the knowledge engineer.

There are three main approaches to the design of knowledge-based systems. These are production systems $[22]$ , logic programming $[17]$ , and object-based systems $[6]$ . Other approaches such as semantic data models $[25]$ exist, as well as some hybrid systems that use a combination of the above-mentioned approaches.

## Production Systems

The rules of a production system are of the IF-THEN type. A series of rules is used to modify the data (or facts) in a working memory. The system makes a pass through the rules looking for rules that match a set of criteria. Out of those rules that match, one is selected and executed. The selection criteria are a function of the inference engine. The system makes multiple passes and on each pass new rules may be matched since working memory is, in general, changed on each pass. This sequence repeats until no matches occur. A well-known language for the implementation of a production system is ops5 [3].

As an example, the following simple rules might exist:

IF credit rating is good

and balance is not greater than 1000

THEN set approval to OK

and create an entry in orders outstanding.

There are references in this rule to, at least, four locations in working memory: credit rating, balance, approval, and orders outstanding. If the rule is matched and selected, then the contents of approval will be changed and a new entry will be made in orders outstanding. These changes may result in a different “match and select” result on the next pass.

## Logic Programming

Logic programming is an implementation of programming in the logic of the predicate calculus. The system uses the rules of formal logic to infer new facts. The inference engine carries out a search of the rules and facts of the system through a process called unification. The best known family of languages using logic programming is called PROLOG [5].

The following simple PROLOG statements may serve as an example:

(i) precedes (analysis, design).

(ii) precedes (design, coding).

(iii) precedes (X,Z):-precedes(X,Y),precedes(Y,Z).

Statements (i) and (ii) represent facts. Each fact defines a relationship between its two arguments. These facts can be interpreted to mean that (i) analysis precedes design, and (ii) design precedes coding. Statement (iii) is a rule. In most versions of PROLOG an argument beginning with an uppercase letter is a variable. This rule says that X precedes Z if X precedes Y and Y precedes Z. Unification is a process in which two expressions are made to look alike by finding a consistent set of bindings for the variables in these expressions. Through unification (carried out by the inference engine), PROLOG will infer from these two facts and the rule that analysis precedes coding.

## Object-based Systems

In an object-based system, entities in the “real world” are represented as objects in the system. An object has, in general, a list of attributes (or data values) associated with it along with executable procedures. Objects may also form broader classes; that is, they may hold a hierarchical relationship to each other. As an example, objects: TRUCK and AUTOMOBILE may be related to a higher-level object: VEHICLE. In an object-based system missing attributes or procedures of a lower-level object will result in a default of these attributes or procedures from a higher-level object. For example, attributes and procedures in the object: VEHICLE may be used in default by object: TRUCK or AUTOMOBILE. Messages are passed between objects identifying the procedures to be executed. Two well-known object-based systems are SMALLTALK [10] and FLAVORS [4].

## Application Design Framework

These design characteristics make up our selection framework. In general, any program written requires (or uses) some external input and stored data to produce some useful output using a set of transformations. These four components are shown in Figure 2. The framework for selecting between a knowledge-based and traditional approach is based on this figure. There are eight design characteristics that make up the selection framework. Each is discussed in turn below.

## Representational Similarity

The basic issue in the design of the input and output components of a system is the closeness of their machine-readable representations to the data of the problem environment. The failure to closely match the system I/O requirements with the problem environment may result in an overly complex and rigid data representation scheme.

Both procedural and non-procedural languages can be used to define a front-end to an application. This front-end can deal with data inputs and outputs in a user-friendly manner. The closeness of the machine-readable form to the user's parametric data is very much dependent on the explicit interface design or the closeness of the language chosen.

The ability to easily represent complex data types (for example, list structures) and relationships relevant to the problem at hand is a significant advantage to the designer. In addition the user may be able more easily to interact with the software. Not only may data typing vary between languages but the ability to represent such concepts as a matrix or a relationship directly may or may not exist in a particular system. We will refer to the ability of a system to match the application I/O representational requirements as representational similarity.

Although the range and type of representations possible vary greatly with the design language, some general observations are possible. With a knowledge-based language, more qualitative data and relationships can be represented. However, the representation of numeric data is not natural to many of these languages. For complex or precise numeric data, traditional languages are more appropriate, since these languages already contain built-in arithmetic capabilities.

Guideline 1: If the data entered into and obtained from the system are primarily qualitative or represent relationships, use a knowledge-based language; if these data are primarily numeric, use a traditional language.

## Search Strategy

A major issue in the design of the storage component is the efficiency with which stored data can be accessed and updated. Since this efficiency is highly dependent on how these data are organized for search, this characteristic will

![](/api/attachments/459XWN6U/fulltext/images/3b3947459c6edbd737b23e4a0d5edab6102237fd35eae5dcf45e97dd622ca6ac.jpg)

be referred to as “search strategy.”

In addition to a straightforward search capability, some applications require a more general pattern-matching approach. For example, in logic programming, not only must the relationship name match, but the arguments must match either directly or through instantiation. This pattern matching (including instantiation through unification) is far more complex than a simple search. In addition, some search requirements may demand backtracking; that is, after one approach fails, the language should try additional approaches.

In traditional languages, the search is carried out using a key, that is, a data element which is used to match the stored data. Multiple logical search techniques are available to the designer. The time to search is a function of parameters such as file size, organization, number of records required, and so on.

In knowledge-based languages, the search is usually sequential in nature and uses some matching technique. The search is carried out by the inference engine, and control by the user is severely limited.

Guideline 2: If the search space is large, the pattern of matching is complex, and an inference engine exists that can meet the search requirements, use a knowledge-based language; if the search requires flexibility, that is, the ability to adapt to specific circumstances in the choice of a search strategy, then use a traditional language.

## Transformational Efficiency

Transformational efficiency refers to the number of central processing unit (CPU) cycles required to complete the transformation. Since this feature is very much dependent on the hardware configuration and since many new hardware devices are being introduced to meet specific applications (e.g., data base machines and Lisp machines), this feature is not included in our comparative evaluation. However, it is to be noted that, as the size of the problem increases, the issue of reducing the problem size to minimize the computer resources expended takes precedence. While increased problem size is handled in traditional environments by the use of powerful processors, knowledge-based languages allow one to reduce the problem size using heuristic rules defined by experts.

## Transformational Flexibility

Transformational flexibility is the ability to change, add, or delete the type and sequence of transformations as needed. Even though a system may be written which meets all requirements, there are many circumstances which may necessitate changes to that system. As examples, a changing operating environment, newly mandated legal or regulatory requirements, expansion of the scope of the system, “fine tuning” of the system, elimination of newly found “bugs,” and so on are all factors which can trigger system changes.

In a traditional system transformational flexibility is accomplished by explicit modularization of the programs. Modularization, as a design technique, attempts to partition a system into modules which are internally highly cohesive and which interact with other modules across well-defined, tightly controlled interfaces. This approach is highly consistent with a top-down design philosophy, which produces a system based on successively more refined specifications. This modularization allows a central module to call various other transformations as and when needed. The effects of a change to a well-modularized system will be restricted to the code in the changed module. Unintended side effects are minimized.

In a knowledge-based system, transformations are, in general, processed by pattern matching. Facts or rules may be added or deleted from a knowledge base easily by means of a well-designed knowledge acquisition subsystem. Using an analogy, it is as though the knowledge base has been modularized to such a fine granularity that each fact or rule acts as an individual module. A change has no impact on other facts or rules. (Obviously, the results of the transformation may differ since after a change a different set of facts and rules is in the knowledge base.) Only those rules or facts that are relevant to a problem will be used by the inference engine, and these will be located through pattern matching. Thus, a very high degree of effective modularity is an integral feature of knowledge-based systems.

Guideline 3: If the application is subject to change down to the program statement level, use a knowledge-based language; if the application is subject to change only at a higher level, use a traditional language.

## Transformational Reasoning

Transformational reasoning refers to the system's ability to provide a logical justification (or explanation) on how the system's output has been derived. In a system using complex transformations, the relationship between the input and the output may be difficult for the user to perceive. For some applications, it may be useful (even necessary) for the user to validate (or to, at least, accept) the program's chain of reasoning.

In a traditional system, the presentation of a chain of reasoning is accomplished by either the careful insertion of output statements in the program by the designer or by the use of an automatic trace facility. In either case, the resulting output is, generally, too detailed and includes any false starts and backtracking carried out by the program. In addition, output is not presented in a compact form or in the domain language of the user.

In a knowledge-based system, an explanation system can present a chain of reasoning in a compact, domain specific form. False starts and backtracking can be eliminated and a logically correct line of reasoning between the starting point and the goal of the system can be presented clearly and completely.

Guideline 4: If a system requires a clean, consistent, and logical chain of reasoning of the input to output transformation, use a knowledge-based language; if a system requires, at the most, a trace function, use a traditional language.

## Transformational Representation

Transformational representation (or modeling) is similar to the representational similarity of input/output, except that it is concerned with the similarity between the user's problem definition and its internal representation. In the data/model or traditional environment, the closeness of the modeling logic to the problem environment depends to a large degree on the language used to define these transformations. A modeling language such as IFPS can provide a natural environment for problems in simulation, while linear or goal-programming packages can best assist optimization or multi-criteria decision-making problems.

As discussed above, the three major knowledge-based approaches are production systems, logic programming, and object-based programming. Applications that can be modeled on the basis of one of these approaches may be more easily implemented in a knowledge-based system based on analogous assumptions. However, an application suitable for a computational environment, for example, one that involves matrix manipulation, must be implemented by means of a traditional system.

Guideline 5: If a model of the transformation required in a system matches the model built into a knowledge-based language, use that language; otherwise, use a traditional language.

In addition to these characteristics in the design of applications, there are two other design support characteristics that are relevant. These are similarity of data and instructions and the use of meta-rules.

## Similarity of Data and Instructions

Instructions are the units of software used in a system. Data are the elements manipulated by these instructions. For many applications, the differentiation between these two elements, that is, data and instructions, is very clear. In other cases, there is such a close similarity in their treatment that the difference between them is less clear.

In traditional languages, there is a clear distinction between data and instructions. The program instructions are modularized and they access data only as required. In knowledge-based languages, there is a greater effective merging of the two elements. A production system shows the weakest degree of similarity. Rules are matched, selected, and executed by the inference engine in a sequence until a match is not available. The representation of facts and rules in logic programming is very similar. The inference engine passes through the knowledge base of facts and rules sequentially. In object programming, attributes (i.e., data) and procedures (i.e., instructions) are attached to objects in virtually the same way. In the extreme, the artificial intelligence language Lisp [26] treats data and instructions in a homogeneous manner.

Guideline 6: If there is homogeneity of data and instructions, use a knowledge-based language; if there is heterogeneity of data and instructions, use a traditional language.

## Use of Meta-Rules

A meta-rule is a rule about the use of rules. For example, if two rules apply in a particular situation, a meta-rule may decide which one of these rules to use.

In a traditional language, the program designer makes all rule decisions, and these are fixed for the duration of the program. Rules may be nested, but the incorporation of multiple levels of rules may quickly result in a relatively complex and intricate program logic.

In knowledge-based languages, meta-rules may be contained within the knowledge base or within the inference engine or both. The program designer has little, if any, control over inference engine meta-rules. The designer does, however, have control over the contents of the knowledge base by means of the knowledge acquisition subsystem. Because of the inherent modularity of a knowledge base, the addition and deletion of rules at any level is straightforward.

Guideline 7: If different levels of rules, that is, meta-rules, are required in the system, use a knowledge-based language; if required rules are conceptually all at the same level, use a traditional language.

## Framework Application Examples

THIS SECTION LOOKS at the implementation of a number of real systems and of one hypothetical system. Applicable selection criteria are identified and the resulting design environment is presented.

## XCON: A Computer Configuration System

XCON [21] is an expert system built by Carnegie-Mellon University for the Digital Equipment Corporation. It configures VAX computer systems. An order for a computer system is complex. A selection must be made from a set of hundreds of possible components which, in turn, must work together. In addition these components must be configured together into racks and connected by cables. The original approach was manual. Errors and omissions of necessary components were not uncommon.

The input to the system is a customer order and the output is an acceptable computer configuration. Because the number of possible combinations needed to assemble such a configuration is extremely large, the system searches for combinations that will produce a satisfactory solution rather than an optimal solution. A search strategy using heuristic rules is, thus, needed to obtain such a solution. Since the required output is an acceptable solution and since intermediate interaction with the user is not allowed, a system which incorporates extensive backtracking and trial-and-error capabilities is required.

Components and their joint constraints change as engineering changes and additional options are added to the VAX computer line. This requires significant modularity in the way the design rules are added to and deleted from the system, thus providing for flexibility in the definition of transformations.

Configuration constraints exist on combinations of hardware components, the placement of components, precedence in placement of components, and other features [20]. These constraints can in great part be easily represented by IF . . . THEN . . . rules.

In many of these configuration design decisions, a particular design may be guided by a set of rules. The exact rules chosen for such a design, however, may depend on additional (meta-) rules that are derived from factors such as physical size, networking needs, and so on.

The application characteristics of this problem are, as a result, search strategy, transformational flexibility, transformational representation, and the use of meta-rules. These characteristics suggest the use of a knowledge-based design approach. XCON was implemented using this approach with the OPS5 language.

## Help: A System to Assist a Software User

Although Help systems exist with many software packages [15], the following describes an approach to a hypothetical system. Current Help systems range from a simple retrieval of documentation on the software to information on the syntax and use of commands. Probably the main shortcoming of most such systems is that the user needs to know fairly well what he/she doesn't know. For example, a user may need to know the name of a command before information can be provided on that command. The hypothetical system should provide assistance to an inexperienced user on errors made or information needed.

A Help system that provides diagnostic assistance for a user should be able to infer a corrective action or a correct command from the immediately preceding commands and from the context of the user's interactions with the software. Different prior command sequences should assist the system in focusing on a smaller set of valid commands that are applicable to the user's interaction. The relation between a set of these command sequences and any associated valid command set may be expressed in the form of production or formal logic rules.

In addition a Help system should facilitate user learning. It should be able to provide a logical reason for a recommended course of action and to be able to clearly explain why an error has occurred.

The characteristics relevant to such a system are, thus, its ability to express the logical rules that relate context and commands and to explain the reasoning used in its recommendation. Although Help systems have been implemented using traditional approaches, the use of this framework suggests that a knowledge-based approach may be useful for a diagnostic/instructional Help system.

## Budget Reporting System

Although details may vary, budget reporting systems appear in almost all organizations. Budgets (usually on an annual basis) may be organized by accounts, projects, sub-units, or combinations of these. Essentially a budget reporting system shows actual versus budgeted expenditures. These reports appear at regular intervals, for example, monthly, and may provide information for the month and for the year-to-date. Variances and appropriate ratios may also be calculated.

A budget reporting system accepts input from the accounting system. This input is usually highly numerical in nature. Similarly, the output of the budget reporting system is almost always required in a tabular or graphical form of mostly numerical data.

The transformations consist of simple arithmetic operations on data stored in tabular or matrix form. This computational representation is very similar to the problem environment.

These observations support the conclusion that the characteristics that are significant for such a system are transformational representation and representational similarity. Because of these two dominant characteristics, the appropriate design approach is traditional.

## DSS to Manage Transportation

Gavish [9] describes a decision support system (Dss) designed to meet the transportation needs of a large corporation. This system is used for activities such as transportation trip forecasts, a schedule of trip requests to depots and vehicles, grouping of these trips to balance the load among transportation units, and decisions related to the location of vehicles that will be leased to transport the goods.

The basic input to this system is numerical data associated with a trip a user wishes performed during the coming week. The output primarily consists of a significant number of numerically based reports that classify demand, number of requests, budget estimates, and other items.

Data from a significant number of relatively large files (trip requests, vehicle potential, location, nodes, coding tables, etc.) have to be accessed and merged to generate the needed output, thus requiring direct access to many of these files.

The problem domain is one of optimal resource allocation which lends itself effectively to mathematical modeling. The resource allocation can be performed using several optimization and heuristic algorithms. The resource allocation is, however, based on several sequential decisions, and each, by itself, can use a variety of algorithmic procedures. For this reason, modular design is used to provide flexibility in testing the appropriateness of different resource allocation models.

The application characteristics of this problem are representational similarity, search strategy, transformational flexibility, and transformational representation. The numerical nature of the input/output, direct access to large data bases, the modularity needed in defining transformations, and the mathematical nature of the transformations suggest the use of a traditional design approach. The system was implemented using data and model management concepts.

## DSS in a Public Sector

Henderson and Schilling [14] designed a decision support system to support the needs of a mental health and retardation board in Franklin County in Ohio. This system provides (1) a link between the board goals and the funds allocation decision, (2) better understanding of trade-offs among goals and impact of altering goal priorities, (3) easy incorporation of new restrictions, policies, and cost/service parameters into the decision model, and (4) training tools for board members. The presence of lay decision makers and other non-technical users favored a model structure that is intuitive and easy to understand, can explain its outcome, and will facilitate consensus seeking among board members using iterative decision making.

Numerical and statistical data from a large transaction data base have become the major input source. The decisions and supporting outputs are presented in a variety of representations such as tables, graphs, memos, and press releases.

In the public sector the government regulations, service priorities, and funding sources alter frequently. Any system that is to support decision making in such an environment should have the flexibility to incorporate these changes quickly and effectively.

The decision-making process takes precedence over the actual decision itself in the public sector. The process should be one of consensus seeking and should be explainable to the governing agencies. Thus, the reasons for reaching a decision become very critical.

The system used a traditional design approach using a goal-programming model to support multi-criteria decision making. Goal programming allows iterative decision making with appropriate information on why some goals have not been met. Note that the transformational flexibility and reasoning demands on such a system can make the knowledge-based approach very attractive as well. If the heavily numerical input and output representations and some of the algorithmic transformations can be supported with appropriate macros (defined in traditional languages), the knowledge-based approach could be used in assisting the model modification and reasoning processes.

The above case illustrates a situation where the decision to move to one or the other language environment for design and implementation is not clear. It is possible to take advantage of both environments if such is technically feasible.

So far, we have seen how the application design framework can be used to select a particular design approach. It is unusual to be able to make a design decision on the basis of a single characteristic. The identification of the relevant characteristics contained in the proposed framework and their application to the system requirements does, however, provide the systems designer with an organized means of making a decision for the knowledge-based versus the traditional environment.

Keen and Scott Morton [16] classify the problem environment as structured, semi-structured, and unstructured and suggest that decision making at the three levels of management (strategic planning, management control, and operational control) requires handling problems of all three types. The application systems to support the structured problems are referred to as electronic data processing (EDP) systems, those that support the semi-structured are called decision support systems (Dss), and the systems that support unstructured problems are humane systems, that is, those with significant human involvement. While it is not certain that knowledge-based languages can always support these unstructured problems, a classification of the problem using the application design characteristics, however, can provide assistance to the system designer in the selection of a particular language environment. This selection may be traditional for some applications and knowledge-based for others.

## Summary and Conclusions

THIS PAPER HAS LOOKED at two major systems design approaches. These approaches are the newer knowledge-based approach and the older traditional (non-knowledge-based or data/model) approach. It has addressed the question of how a system designer selects between these two approaches.

Using a generalized schematic of any system, the paper developed eight characteristics of all systems. These characteristics form a framework of selection guidelines.

This framework was then applied to a simple set of real and hypothetical systems. For any particular system, some required characteristics can be achieved especially well in either a knowledge-based or a traditional environment. The guidelines for the remaining characteristics were then applied to the system and a recommendation for a design approach was made. While some systems fall clearly either into the knowledge-based area or into the traditional area, some might reasonably be implemented in either environment.

The guidelines making up the selection framework are meant to be a tool for the system designer. This tool assists the designer in selecting either the knowledge-based or the traditional development environment.

## REFERENCES

1. Barr, A., and Feigenbaum, E. A. The Handbook of Artificial Intelligence. Vol. 1. Los Altos, CA: William Kaufmann, 1981.

2. Bonczek, R. H.; Holsapple, C. W.; and Whinston, A. B. The evolving roles of models in decision support systems. Decision Sciences, 11, 2 (April 1980), 337–356.

3. Brownston, L.; Farrell, R.; Kant, E.; and Martin, N. Programming Expert Systems in OPS5. Reading, MA: Addison-Wesley, 1985.

4. Cannon, H. A non-hierarchical approach to object-oriented programming. Unpublished paper, MIT, Artificial Intelligence Laboratory, 1982.

5. Clocksin, W. F., and Mellish, C. S. Programming in Prolog. 2nd ed. New York: Springer-Verlag, 1984.

6. Cox, B. J. Object Oriented Programming. Reading, MA: Addison-Wesley, 1986.

7. Doyle, J. Expert systems and the myth of symbolic reasoning. IEEE Transactions on Software Engineering, SE-11, 11 (November 1985).

8. Ford, F. N. Decision support systems and expert systems: A comparison. Information and Management, 8, 1 (January 1985), 21–25.

9. Gavish, B. A decision support system for managing the transportation needs of a large corporation. AIEE Transactions (March 1981), 61–85.

10. Goldberg, A., and Robson, D. Smalltalk-80: The Language and Its Implementation. Reading, MA: Addison-Wesley, 1983.

11. Gorry, G. A., and Krumland, R. B. Artificial intelligence research and decision support systems. In Bennett, J. L. (Ed.), Building Decision Support Systems. Reading, MA: Addison-Wesley, 1983.

12. Gorry, G. A., and Scott Morton, M. S. A framework for management information systems. Sloan Management Review, 13, 1 (Fall 1971), 55–70.

13. Hayes-Roth, F.; Waterman, D. A.; and Lenat, D. B., eds. Building Expert Systems. Reading, MA: Addison-Wesley, 1983.

14. Henderson, J. C., and Schilling, D. A. Design and implementation of decision support systems in the public sector. MIS Quarterly, 9, 2 (June 1985), 157–170.

15. Houghton, R. C., Jr. Online Help systems: A conspectus. Communications of the ACM, 27, 2 (February 1984), 126–133.

16. Keen, P. G. W., and Scott Morton, M. S. Decision Support Systems: An Organizational Perspective. Reading, MA: Addison-Wesley, 1978.

17. Kowalski, R. Logic for Problem Solving. New York: North Holland, 1979.

18. Kowalski, R. Logic as a computer language. In Clark, K. L., and Tarnlund, S. A., eds. Logic Programming. London: Academic Press, 1982.

19. McCosh, A. M., and Scott Morton, M. S. Management Decision Support Systems. New York: John Wiley, 1978.

20. McDermott, J. A rule-based configurer of computer systems. Technical report, Department of Computer Science, Carnegie-Mellon University, Pittsburg, PA, 1980.

21. McDermott, J. R1: The formative years. AI Magazine, 2, 2 (Summer 1981), 21–29.

22. Nilsson, N. J. Principles of Artificial Intelligence. Palo Alto, CA: Tioga, 1980.

23. Sprague, R. H., and Carlson, E. D. Building Effective Decision Support Systems. Englewood Cliffs, NJ: Prentice-Hall, 1982.

24. Weiss, S. M., and Kulikowski, C. A. EXPERT: A system for developing consultation models. Proceedings of the International Joint Conference on Artificial Intelligence, 6 (1979), 942–947.

25. Winston, P. H. Artificial Intelligence. 2nd ed. Reading, MA: Addison-Wesley, 1984.

26. Winston, P. H., and Horn, B. K. P. Lisp. 2nd ed. Reading, MA: Addison-Wesley, 1984.
