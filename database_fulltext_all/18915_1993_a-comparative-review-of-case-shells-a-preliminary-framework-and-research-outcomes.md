---
otero_id: 18915
otero_key: "NRAX28CD"
title: "A comparative review of CASE shells: A preliminary framework and research outcomes"
authors: "Pentti Marttiin; Matti Rossi; Veli-Pekka Tahvanainen; Kalle Lyytinen"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90022-l"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A comparative review of CASE shells: A preliminary framework and research outcomes

Pentti Marttiin, Matti Rossi, Veli-Pekka Tahvanainen and Kalle Lyytinen

University of Jyväskylä, Jyväskylä, Finland

Because of rigidity and weak support of the users' native methods and methodologies in existing CASE tools, there is a growing need for customizable CASE tools (CASE shells). The nature of CASE shells is different from ordinary CASE tools supporting a fixed set of methods. With CASE shells, organizations can define tools to support their own methods, instead of choosing a tool that supports them. Existing CASE shells have different features and architectural principles that make them appropriate for different tasks. Obviously, a framework for comparing them is needed. In this paper we develop one such framework. It takes into account different tasks in customization and the effectiveness of carrying out these tasks. We apply the framework to compare three CASE shells. We use the SMARTIE method as an example of some characteristics of current CASE shells, and suggest some future research directions.

Keywords: CASE shell; Meta-CASE; CASE tool; Metamodeling; Methodology; Methodology engineering.

![](/api/attachments/NRAX28CD/fulltext/images/db1d91a9f415c75637f581d1b0ba84077ec7c4889c45c63a2cb2b77d6a2f2707.jpg)

Pentti Marttiin is a doctoral student in the Department of Computer Science and Information Systems at the University of Jyväskylä, from which he received his M.Sc. in 1991. Articles of his have recently been published in ICIS and HICSS. His research interests are methodology engineering, CASE technology, and user interfaces. He is currently working as a researcher in the MetaPHOR research project, which focuses on computer aided methodology engineering.

The project is funded by the Academy of Finland.

Correspondence to: P. Marttiin, Department of Computer Science and Information Systems, University of Jyväskylä, P.O. Box 35, 40351 Jyväskylä, Finland, e-mail: ptma@tukki.jyu.fi.

![](/api/attachments/NRAX28CD/fulltext/images/95c01abc35c8dcc68f44989b5dc650d6e96559c16435dd8d333b306d30d1921d.jpg)

Matti Rossi is finishing his master's degree in the Department of Computer Science and Information Systems at the University of Jyväskylä. Articles of his have recently been published in ICIS and CAiSE. His research interests are methodology engineering and adaptive CASE tools. He is also currently working in project MetaPHOR, and is funded by the University of Jyväskylä.

![](/api/attachments/NRAX28CD/fulltext/images/88611562e83f6ec3012ba5004f625938d40ad7e9847689479991690a072bbd41.jpg)

Veli-Pekka Tahvanainen is a doctoral student in the Department of Computer Science and Information Systems at the University of Jyväskylä, from which he received his master's degree in 1992. He has co-authored several articles, most of which have appeared in refereed conferences. He has also co-edited (with Prof. Lyytinen) the book "Next Generation CASE Tools". He is currently working in project MetaPHOR along with the other authors of the present pa per. His research interests include introducing CASE technology in an organisation, and adapting tools and methods to individual development situations (Method Engineering).

![](/api/attachments/NRAX28CD/fulltext/images/78e9df7c55ae1bc4affa8f3cff4af5b92dd16ca05cf1086e44fef87949096ada.jpg)

Kalle Lyytinen is a full professor of Information Systems at the University of Jyväskylä, Finland. He holds a Ph.D. in Computer Science from the University of Jyväskylä. His previous positions include research positions in the University of Stockholm and London School of Economics. He has also acted as visiting professor in Copenhagen Business School. He is a vice-chairman of IFIP WG 8.2. "Information systems and organizations". He serves on the editorial boards of Journal of Information Systems, European Journal of Information Systems, Accounting, Management and Information Technology, MIS Quarterly, and Journal of Information Systems. His research interests include social theory based research into information systems, system design methodologies, information systems management, research strategies and their selection, and information system failures. He is currently the leader of the MetaPHOR research project.

## Introduction

Computer Aided Systems/Software Engineering (CASE) has experienced a notable growth in products during the last years. Unfortunately, the existing CASE tools support only a few methodologies $^{1}$ and a limited set of methods. The support can be defined as a tool's capability to derive and maintain models in a method that is included in the methodology. It is, however, obvious that all organizations' methods are not similar to those supported in CASE tools. Therefore, the problem in adapting CASE tools is that new methods and models must often be learned while introducing the tool. This requires considerable education and investments. One way to alleviate this problem is to develop CASE environments that can cover a variety of different methods and can thereby satisfy most organizations' different needs. This makes it necessary to apply CASE shells – tools, by which one can add new functionality into a CASE environment. According to Bubenko, “a CASE shell includes mechanisms to define a CASE tool for an arbitrary method or a chain of methods” [1].

We currently have a paucity of knowledge on the issue: “What kind of CASE environments are effective in use?”. The only way to probe this problem is to compare existing products and evaluate their strengths and weaknesses. Some comparisons of CASE tools $[2,3]$ and repositories $[4]$ have already been made, and general requirements for CASE tools are proposed $[5]$ . Also, to support integration of CASE tools, several standards (CDIF, IRDS and PCTE ${}^{2}$ ) are examined $[6]$ . One additional aspect to consider in a CASE environment is the possibility of modifying its method support and functionality. Therefore, there is a need to also examine the strengths and weaknesses of the CASE shells.

The goal of this paper is to evaluate and compare some CASE shells and to examine how they satisfy the need for enhanced method support and functionality. We present an evaluation framework and evaluate three CASE shells using it. We examine the functionality of these CASE shells by implementing a new method specification (a new meta model) in each of these CASE shells and drawing some conclusions from the resulting meta model and the process of developing it.

## Framework for comparing CASE shells

Our framework addresses two questions. The first is:

(I) What kind of tasks can a user do with a CASE shell?

The second probes the use of the CASE shells:

(II) Are the metamodeling tasks accomplished with the CASE shell appropriate and efficient, and is the tool easy to use?

(I) When tackling the first level question we distinguish three classes of CASE shell properties [7]:

(a) linguistic components,

(b) functions, and

(c) mechanisms of the CASE shell.

(a) The linguistic components of a CASE shell define the capabilities by which one can change method specifications (i.e., description languages, that defines the conceptual structure of a model and representations of these) in a CASE environment. The representations can be divided into textual, matrix and graphical representations [8]. Although we handle such method as a separate part of a methodology, connecting a new method to others is an important problem that must be addressed by the framework implicitly. Seven different levels of functionality for the linguistic facilities of a CASE shell can be distinguished:

\- notational modifiability defines a CASE shell's capabilities to modify representations in a description language; for example, symbols and aliases;

\- notational variation is the possible variation between graphical, lexical, and matrix representations, and the ability to support them simultaneously;

\- notational translation gives the abilities to translate a representation from one form to another; for example, from a graphical to a lexical representation, and vice versa;

\- syntactic extension provides support to extend the description language with new elements, such as new object, relationship, and property types;

\- syntactic definition gives the degree of support for defining new description languages to support new methods;

\- syntactic translation is the support for specifying a translation mechanism; for example, a mechanism to translate a data model into a database schema; and

\- type specification defines the support for specifying new data types, such as bit maps, sound, and other multimedia elements.

(b) The functional components of a CASE shell define the variability of computer operations on the meta model. These concern mainly the essential data management facilities in a CASE environment:

\- query definition gives the ability to formulate ad hoc queries in different situations;

\- report definition describes the capability to build report specifications;

\- inference definition states the ability to make inferences on extracted descriptions;

\- storage definition is the support for different forms of descriptions (e.g. ASCII, binary, bitmap, PostScript) stored in the repository; and

\- usage definition defines ways to change the use of the environment; for example, to change access rights and access control.

These “support facilities” are of importance in the development of CASE tool properties. They do not support metamodeling in CASE shells. Our motivation in including them in our framework is that these facilities have to operate on new meta models, created or modified by a CASE shell.

(c) The last class of CASE shell properties falls in the mechanisms:

\- export/import definition allows to export system descriptions in a CASE environment for other environments (such as data dictionaries) or to import system descriptions from other environments. This may follow official or industry data interchange standards (such as CDIF);

\- data management definition for storing and managing system descriptions over a number of DBMS's;

\- user interface definition for use of different user interface environments, such as Presentation Manager, MS-Windows, or Motif;

\- data communication definition to support different data communication protocols, such as OSI or X.400; and

\- operating system definition to run on different operating systems like OS/2 or UNIX.

(II) The second question tackles the effectiveness and usability of the CASE shell. We are interested here in:

(a) the meta-metamodel (the fixed data model on which the CASE shell is based),

(b) the user interface of the CASE shell, and

(c) the design of metamodeling tasks and functions

(a) The linguistic components in our framework are closely connected with the meta-metamodel, which contains the data structure to define method specifications. If this conceptual model contains too much or unclear concepts, it is not easy to use. Otherwise if it has a limited set of concepts the “semantic power” of the meta-metamodel is weak in defining more complex method specifications. Moreover, our opinion is that large method specifications need to be modeled graphically, and matrix representation is very useful in many situations. Therefore, the meta-metamodel should be able to represent graphical, matrix and textual method specifications without a loss of information. To carry out a deeper analysis to describe the “semantic power” available in a CASE shell, we shall use the following four questions to compare the representation “effectiveness” of the CASE shells:

(1) What kind of semantic checks can be added to the object types and their connections?

(2) Is it possible to model methods that use decompositions?

(3) Is it possible to define links between different models or graphs?

(4) Is it possible to configure tables (matrices) and link them to other parts (e.g., to graphs) of the method?

(b) The use and effectiveness of the CASE shell largely depends on how the CASE environment (both CASE shell and tool) is implemented. A CASE environment needs primitives to handle representations. Those include, for example, facilities to rotate, zoom and preview representations, to apply multiple windows and operations to cut/copy/paste different kind of data. A graphical user interface (GUI) like MS-Windows or Motif is important, because it offers capabilities for building standardized functions of these operations.

(c) We examine also the usability of tasks when modeling a new method. The design of these tasks relates closely to the first two issues: how to use the meta-metamodel through the implemented user interface. We need to understand how method adaptation can be done effectively in different situations. For this we need wide experience in using the CASE shell. The basic ideas of metamodeling mechanisms, however, can be described by specifying an “typical” method. We have chosen to apply SMARTIE [9], which we adapted into chosen CASE shells in our comparison.

If a CASE tool offers querying or reporting facilities, the role of the CASE shell (or some other CASE environment tool) is to offer these to the user automatically. In $[10]$ we discuss the modeling requirements for data storage, transfer and maintenance in a CASE environment.

The task of configuring a CASE environment is quite difficult and has been mainly accomplished by CASE tool vendors. Letting the users define more tasks and functions in their environment necessitates a good and standardized design of the user interface.

## On classifying CASE shells

One criterion for a good CASE shell is to determine how the shell facilitates modification of the CASE tools. Four different approaches can be observed here [11]:

(1) database oriented,

(2) interface oriented,

(3) extension kit, and

(4) knowledge oriented approach.

The database oriented approach uses a meta-language to define the description languages associated with methods. Although the concept of meta models is much older, the first CASE shell in the modern sense of the word was SEM (System Encyclopedia Manager), which used an ER-model based metalanguage [12]. Similar architectural principles are followed in MetaPlex [13], MetaView [14], and QuickSpec™ (with MDM) [15]. Also, the early ANSI IRDS standardization efforts were ER-metasystem oriented [16]. We call this approach database oriented, because IS descriptions are here seen as a set of linearized statements produced by a set of textual or graphical tools included in a CASE environment. A second, interfacc oriented approach is to build a CASE environment around generic graphical notations. RAMATIC [17] is representative of this approach, because it uses generic routines, that can be associated with symbols. A third way is to build extension kits for existing CASE tools by which new description languages can be included into the CASE tool. This approach is limited. It can be either database or interface oriented, but it cannot modify the whole environment – only extend the functionality of a tool already available. An example of this approach is Index Technology's Customizer™ [18], which can be used to extend some linguistic features of the tool Excelerator™ [19]. We could also make a distinction between data and knowledge oriented tools (such as ConceptBase [20]). In these, the meta-metamodel is based on data models and logical rules.

Another way to classify CASE shells is to distinguish between those that modify only the linguistic elements, and those that generate a wholly new CASE environment. In the first, the CASE environment has separate shell and tool products; the CASE shells are useless without “bridges” to CASE tools. Such shells are the Customizer that modifies Excelerator, and the MDM that modifies QuickSpec and SA-RT. In the second, the CASE shell and the CASE tool are interwoven into the same product. An example of this approach is the RAMATIC tool. It combines all the facilities needed in a CASE environment within the same “product set”. This approach offers more flexibility, but for RAMATIC the task of configuring all parts of the tool in a way that is suitable for the end user, becomes more complicated.

![](/api/attachments/NRAX28CD/fulltext/images/3851d904b816f2282c4cf2af9ccbc3dca733ac9317be10a3995afcf6e8ab1562.jpg)  
Fig. 1. The metamodel of the SMARTIE method.

## The comparison

We originally chose three CASE shells for comparison: QuickSpec, RAMATIC and Customizer. The purpose of our study was to examine the architecture, functions, meta-metamodel, and the modeling procedure of the selected CASE shells, and to learn how a new method specification can be developed for each. Also, the facilities of these CASE shells were evaluated.

We used the SMARTIE method, because it is powerful enough to provide a realistic example and has a well-defined syntax and semantics. Most IS methods can be divided into three categories: process-oriented, data-oriented, and behaviour-oriented [21]. SMARTIE integrates these three categories: it has the process-oriented part Interaction Communication Diagram (ICD), the data-oriented part State Base Diagram (SBD) and the behavior-oriented parts Processor Transition Table (PTT), Bank Base Table and Channel Base Table.

The rough meta model of SMARTIE and examples of its three models are illustrated in Figures 1 through 4. ICD consists of modules with their interfaces. A module consists of processors, channels and banks and an interface consists of banks and channels. A processor is connected to a channel or bank with four relationships generates, receives, updates and looks up. These contain the special attribute time, which also appears in PTT. A processor can explode to a module. The content of a processor is stored as facts, and it activates messages. These are described in PTT per the four columns in Figure 4. Processor collects its information to be described in SBD, which contains entities with attributes, and asso-

![](/api/attachments/NRAX28CD/fulltext/images/5660f2edad313ad0b75dd50141d6a8013cd3ea65b895395fab0c536d3ee4b7e2.jpg)  
Fig. 2. Interaction communication diagram [9].

![](/api/attachments/NRAX28CD/fulltext/images/642ee99eccb248bfc04342d72bf26ff983986f2110e761b5ce3ffb1ff2575d08.jpg)  
Fig. 3. State base diagram (SBD) [9].  
ciations between them. Entity can also contain subtypes like “black” customer in Figure 3.  
In the following, we take a closer look at the four questions relating to the “semantic power” of the CASE shell’s meta-metamodel and analyze them in conjunction with SMARTIE specifications as follows:  
Question 1: SMARTIE has in its ICD four kinds of connections. Does the tool support semantic checks for these connections?

Question 2: Can the tool make the decomposition A PROCESSOR IS EXPLODED TO A MODULE? (see Figure 1)

Question 3: Can the tool define and maintain semantic links between the ICD and the SBD? (Figures 2 and 3)

Question 4: Is it possible to formulate a table such as PTT (Figure 4) and link it to the ICD?

## QuickSpec

QuickSpec $^{3}$ was originally built to be a windows-based front-end tool to PSL/PSA, but it can also support other languages. PSL/PSA $^{TM}$ is a text-based CASE environment that can be used as a modeling tool and as a repository. It supports the analysis and design, and to some extent also the maintenance, of software. It is a part of the “product family” Meta Systems Tool Set. The other products in this family are a bridging and custom documentation tool RSI, a data modeling tool VIS, a Reverse Engineering toolkit, a PC-based graphics and analysis tool Structured Architect (SA-RT), and a Structured Architect Integrator for multiple SA-RT -tools.

<table><tr><td colspan="3">PROCESSOR TRANSITION TABLE</td><td colspan="3">MAIL ORDER COMPANY</td></tr><tr><td colspan="3">CONDITION</td><td colspan="3">PRODUCTION</td></tr><tr><td></td><td>actions</td><td>inspections</td><td>mutations</td><td>responses</td><td>time</td></tr><tr><td>1</td><td>order(c,p,q)</td><td>customer (c),- black (c),product (p),minq (p,x),q&gt;= x,...</td><td>+ cusorder (r)+ ordercust (r, c)+ orderprod (r, p),+ orderq (r, q),+ orderdate (r, d)</td><td></td><td></td></tr><tr><td rowspan="2">2</td><td>deliver (p),repeat (p),</td><td>deliverable (p, r),stock (p, s),ordercust (r, c),orderq (r, q)</td><td>+ delivered (r)- stock (p,s),+ stock (p, s-q)</td><td>+ delivery (r, c, p, q),repeat (p)</td><td>*~</td></tr><tr><td>deliver (p)</td><td>del-period (p, t)</td><td></td><td>deliver (p)</td><td>t</td></tr><tr><td>3</td><td>replenishment(b, p, q)</td><td>suporder (b),- received (b),stock (p,s)</td><td>+ received (b),- stock (p, s),+ stock (p, s+q)</td><td>deliver (p)</td><td>~</td></tr></table>

Fig. 4. Processor transition table [9].

New languages can be defined using the MDM tool – a real CASE shell component. This is a facility that can be used to define method specifications into QuickSpec and SA-RT. MDM has never been released as a product but is aimed for in-house method modeling. Meta Systems is now a part of the LBMS corporation. LBMS also designed an OS/2 based repository tool, LBMS's Information Manager [22], which was based on the functional structure of QuickSpec but never released.

## The architecture of QuickSpec

QuickSpec is derived from PSL/PSA; it had two parts: PSL (Problem Statement Language) and PSA (Problem Statement Analyzer). PSL is a formal language for modeling information systems. PSA maintains the specification database, provides a query system, and produces reports and other documentation. The IS specifications are kept in the database. The meta database of PSL/PSA contains the rules by which the IS specifications can be checked on entry. PSA has four functional components: the command language interface (CLI), the analyser for checking the integrity of modifications, the database management system, and a set of report models. Other tools are the interactive query system QS, the documentation tool QuickDoc, and the report specification processor RSI.

QuickSpec originally had a MS-Windows-based user interface for creating textual statements in the PSL language. It is not a drawing tool like RAMATIC and Excelerator. Its purpose is to make the formulation of correct PSL statements easy by letting the statements be selected from dialogue lists. However, it can be extended to accept statements in any language through its MDM component; it is the CASE shell component of the PSL/PSA family. MDM is a tool for creating method specifications.

The core of QuickSpec is the Metabase. It consists of a library of database access routines and a database management system. The library is divided into two sub-collections which interact with the target and meta databases. The models of target level and meta level are based on the data-model called OPRR. MDM is used for generating the meta database of QuickSpec and other Metabase-based tools.

![](/api/attachments/NRAX28CD/fulltext/images/7143c4d81c7f47b16c0bc09310a94f346d3f845aacf2712d6db68ee0a2a7d1c0.jpg)  
Fig. 5. The architecture of QuickSpec, PSL/PSA and MDM.

The architecture and connections between these tools are shown in Figure 5.

## The functions of QuickSpec and MDM

QuickSpec has four types of functions: database, encyclopedia, import/export and setting preferences.

Database creation and maintenance tasks are performed through the Database menu. It offers the usual commands for creating, opening, closing, and saving databases.

The Encyclopedia functions are used for IS descriptions entry and editing. Descriptions are created using the types included in the defined meta model. For example, PSL 6.0 contains 18 different object types, such as ATTRIBUTE, CONDITION and ELEMENT, a large set of relationship types between the object types, such as CONSISTS and FLOWS, and property types, such as DESCRIPTION and DOCUMENTATION. Changing the metamodel is done in Preferences. Entering new instances of types is accomplished by selecting types and naming them: first, the user chooses an object type and names an instance. After this he/she can choose among the legal relationship types for the created object instance, etc.

The Import/Export menu is used for transferring information across environments: between QuickSpec databases, and to and from the PSL/PSA system. The user can transfer the entire QuickSpec target database, the last changes he/she was made, or selected statements. The facility uses a special transfer language called ORIF.

MDM has two components: a Meta language processor and a XT table definition processor. The internal concepts and the structure of a meta model are made using the Meta language processor. The “XT table definition language” describes the external representations for object-, property-, and relationship types. The XT table definition processor connects an external representation to the meta database.

## The meta-metamodel of QuickSpec

QuickSpec is based on the OPRR- data model [23,24,25]. OPRR consists of four concepts:

\- object: A thing that exists on its own and is represented by its properties.

\- property: A description or qualifying characteristic associated with an object, a relationship, or a role.

\- relationship: An association between two or more objects. This can not exist if the associated object instances disappear.

\- role: The link between an object and a relationship: it clarifies how an object participates in a relationship.

The Metabase is constructed by using a limited version of OPRR (shown in Figure 6), in which roles cannot have properties and no more than four object types can participate in a relationship type.

## Using MDM to derive method specifications

The modeling process can be divided into two main tasks: to define a method in MDM and to implement it in the QuickSpec environment. The user has two different ways to cope with the first task.

First, we can follow the longer way. This is useful in most situations, especially when the user wants QuickSpec to use only the types of the new method or the methodology specification. The steps are:

![](/api/attachments/NRAX28CD/fulltext/images/1e959c0f4d48cc236015d0a31d0a2f66b4ef4cccb614b032dbaffc471a027348.jpg)  
Fig. 6. The meta-metamodel of QuickSpec.

(1) identify and formalize the method specification (for example using the OPRR concepts)

(2) express it in the MDM language

(3) compile the MDM language definition to create a meta database,

(4) prepare an XT table specification, and

(5) compile it in to the created database

The second way is to use a meta database that is created to contain PSL types. This is useful, when the new method can be modelled using PSL. Only steps 4 and 5 need to be done.

We have adopted the shorter way in our study, as represented in appendix 1. Following this, the SMARTIE concepts PROCESSOR, MODULE and TRANSITION are defined as PSL-processes. SMARTIE concepts BANK and CHANNEL are mapped to PSL-sets.

If we want to use OPRR as an MDM language, the SMARTIE concepts will be defined as OPRR-objects. The mappings between OPRR concepts and SMARTIE concepts are easier than those between PSL and SMARTIE concepts. However, creating the new MDM language takes time.

## Modeling SMARTIE with QuickSpec

We can now answer our four questions addressing the effectiveness of the approach. First, SMARTIE object and relationship types will retain their semantics. QuickSpec supports semantic checks for the creation of relationship types such as the LOOKS UP link. The mappings from SMARTIE-concepts to PSL-concepts, however, are difficult. Second, QuickSpec can support linear representations of decompositions. The third and fourth questions are not applicable, because QuickSpec uses only linear statements. Links between different linear models can be created, but graphs and tables cannot be configured.

## RAMATIC

RAMATIC is a CASE shell developed by SISU (Swedish Institut for Systems Development). It is also a CASE environment, because RAMATIC itself uses the method specifications it creates. The CASE environment is implemented using several description languages. RAMATIC has been in operational use since the end of 1987 in several Swedish organizations.

## The architecture of RAMATIC

The architecture and functions of RAMATIC are shown in Figure 7. The core is the design object database (DODB), which consists of the conceptual database (CDB) and the spatial database (SDB). CDB stores information about the developed methods; for example, their objects, the relationships between the objects, and their attributes. SDB contains information of how and where on the screen the conceptual objects are graphically represented. A graphical representation is not necessary for all objects.

![](/api/attachments/NRAX28CD/fulltext/images/65e0b2541fba6a6664cf63e4cea3d65891892819fc0bb178fe77f9e3a1cd142d.jpg)  
Fig. 7. The architecture of RAMATIC [17].

RAMATIC runs natively on SUN workstations under UNIX, but it can also run in some other environments. The database management of its OS/2 version (which we tested) is based on OS/2 Extended Edition DataBase Manager. The user interface runs under Presentation Manager.

## The functions of RAMATIC

RAMATIC aims to generalize the shell functions so that they can be used to support different methods. These CASE shell primitives are fixed functions that are instrumental in modeling variable methods, for example graphical functions (e.g. draw a line, draw an open curve), window management (create a screen), graphical groups, CDB management, symbol management, syntactical checking and picture management. The connections between menu items and the CASE shell primitives are defined using a menu description language.

Interaction management can be defined as management of the parts of the RAMATIC interface when it is used as a CASE tool. It contains a graphical editor, a menu manager, a syntax checker, a forms manager, an analyzer and a language transformer. The graphical editor is a window in which models are drawn. Every method has its own menus and forms connected to the graphical editor using managers. The syntactic checker checks the rules of a method.

RAMATIC has a large library of symbol types used in description languages. Moreover, the methodology engineer can create symbols for a new method using these types or define one using the symbol description language.

## The meta-metamodel of RAMATIC

The DODB meta-metamodel (parts CDB and SDB) is based on a binary-relationship model. It offers several concepts for sets and properties. It is shown in Figure 8. The object types in CDB are described by two base types: FREE-OBJECT and CONN-OBJECT (a relationship between two parts [to and from]). Every object type in CDB has a link to one or more object type(s) in SDB (spatial). Spatial object types have a link to their picture, to the symbol types in a symbol dictionary, and to groups. Object types can be grouped to a SET TYPE (set) or differentiated to a SUB TYPE (conceptual - sub).

![](/api/attachments/NRAX28CD/fulltext/images/dee22292c54345cfba0a2031fe07fbbdfd9150bd66225f69a3c5a63499a31811.jpg)  
Fig. 8. The meta-metamodel of RAMATIC [17].

FREE-OBJECTS exist on their own. They usually have a graphical presentation, but this is not necessary. Both CONN- and FREE-OBJECTS can have associations (attributes) stored with them. This binary-relationship core has been augmented. SET TYPES are used for grouping objects. A group can be modelled in a decomposition picture using an ENLARGE-COMMAND. That describes what relationships and objects from the original picture are transported to the decomposed picture.

## Using RAMATIC to derive method specifications

The new method is specified in RAMATIC by using Model, Symbol, Menu and Form description languages. The procedure advances as follows:

(1) create the conceptual metamodel,

(2) produce symbol definitions and link them to the concepts,

(3) produce menus and attach the concepts and symbols,

(4) produce forms for concepts, and

(5) define help texts for the method.

The Model description language contains the basis for other definition languages; thus its definition forms the first stage. The model consists of different object types (FREE), connections between them (CONN) and groups of them. The model description contains constraints and semantic checks and the connections between the model types.

When the model definition is ready the model engineer picks up the objects of the model and attaches available symbol definitions or make new ones using the Symbol description language. The symbols are defined by their shape, scale and labels.

When all objects have been attached to their respective symbols, the model engineer makes the menu definitions by creating the appropriate menus, which include items for drawing all object types and grouping and describing them. All menu items have also an attached shell function that is executed when the item is selected. The menus are defined using RAMATIC's Menu description language.

For complex information retrieval (eg. matrices, tables) forms for a method may be defined using the Forms definition language. They can be used for cross-referencing design objects and thus for validation.

## Modeling SMARTIE with RAMATIC

SMARTIE was modeled using the Model description language of RAMATIC, as shown in appendix 2. The object types of SMARTIE are defined as FREE-OBJECTS and the connections as CONN-OBJECTS. Only the modelled pairs of FREE-OBJECT can be connected.

RAMATIC supports semantic checks of connections defined between two named objects types, so semantic checks form a natural part of the definition. Our second question concerning decomposing SMARTIE's A PROCESSOR IS EXPLODED TO A MODULE-part is modelled in RAMATIC by the ENLARGE-COMMAND, which also describes the connections that are transported to the exploded graph. Thus, "semantic" explosion can be successfully modelled. The third problem concerns the linking of objects in two model types. In RAMATIC, SET-OBJECTS can connect objects in different model types. So, the A PROCESSOR EXPLODES TO MODULE-part can be handled by defining the process as a set. Fourth, forms handling in RAMATIC is quite powerful: it is driven by the Forms description language. The language allows one to create complicated link tables, such as a

![](/api/attachments/NRAX28CD/fulltext/images/04a82884301f3f64b36ec1c49dc9365768bfe4a88abcac705bf9d4607d14c8cd.jpg)  
Fig. 9. The architecture of Customizer [18].

Process Transition Table. Unfortunately, the Forms description language has no direct support for database operations, and the database access is handled using C functions. Therefore, RAMATIC can (in principle) be used to make the tables, but it is difficult because of the low level database programming needed.

## Excelerator and Customizer

Customizer $^{4}$ is a product for customizing Index Technology's workbench products: Excelerator and Excelerator/RTS. Excelerator $^{5}$ is a tool for system definition and analysis, and it offers also possibilities for prototyping. Excelerator/RTS contains some additional languages and associated analysis facilities.

## The architecture of Excelerator and Customizer

Excelerator partially supports both the SA and IE methodologies. Despite this, the user can define a local procedure when using the supported methods. Accordingly, Excelerator contains description languages (Data Flow Diagrams, Structure Charts and Data Models), and varied representations of these (Gane and Sarson and Yourdon DFDs) found in the methodologies.

The description repository in Excelerator is XLDictionary, which can be divided into several project databases. The description languages and forms of Excelerator can be modified by Customizer, which has a repository called System Dictionary containing descriptions of XLDictionary elements. Customizer consists of four facilities (Figure 9): Shape Editor for creating new symbols, System Dictionary for maintaining the repository, Screen Design for creating forms, and SLD Interface for sharing data among different System Dictionaries. Forms Library contains forms used in customized product.

There is also a program called XL/Programmers Interface for export/import definition [26]. It provides a library of programming functions that enable an access to data stored in Excelerator. These functions have to be included in the users' own C programs.

## The functions of Excelerator and Customizer

Excelerator is a graphical tool. It has functions for drawing models associated with description languages (Graphics) controlled by the XLDictionary, which supports some group-work in a multi-user environment. It has facilities for defining and changing “audit trail” -information of projects and users (Housekeeping), and for prototyping (Screens and Reports). Prototyping means that the user can build form and report models of system descriptions. The analysis functions (Analysis) verify the correctness of graphs, dictionaries, prototypes, and connections between different levels. Data produced in the Analysis phase can also be gathered and reported (Documentation). Also, text processing and project management programs can be used via the Documentation tool.

![](/api/attachments/NRAX28CD/fulltext/images/c49c6cbf32f592a3c54aacfa2f6155254c170fb1b2af39d217397d5c3979dc17.jpg)  
Fig. 10. The meta-metamodel of Customizer [18].

New symbols can be created by using the Shape Editor, with drawing primitives (such as “rectangle”, “circle”, “line”, and existing shapes). A symbol is connected to an object type in the System Dictionary, and to a form in the Screen Design. A System Dictionary provides direct access to each SD type’s attributes (see Figure 10). The user can examine, add, and modify these attributes or use the information as a basis for reports. Screen Design is used for creating the data entry screens in the customized product, based on the different kinds of templates available; e.g., the user can choose to use explosion paths for the decomposition. The SLD Interface allows the user also to copy system-level data from a customized product to other tools. It thus helps in transferring defined forms, metamodels, and SD types.

## The meta-metamodel of Customizer

System Dictionary is founded on the EAR model. The types used in the meta-metamodel (SD types) are: CONNECTION, ENTITY TYPE, FACILITY, GRAPH CONVENTION, MENU, SCREEN DESIGN, SHAPE, and SYSTEM DEFINITION. Five relationship types can be build between the SD types: CONTAINS, GOES TO, IS DEFINED BY, RUNS and USES. For example, GRAPH CONVENTION contains information of ENTITY TYPES, SHAPES and CONNECTIONS of the current method specification.

In Customizer, a new metamodel is defined as a graph type. The graph type is composed of two main components: GRAPH CONVENTION and

ENTITY TYPE. GRAPH CONVENTION specifies which MENUS, rules, and defaults are activated, when the user is creating or modifying this type of graph. An ENTITY TYPE determines how the tool will store and access individual instances.

## Using Customizer to derive method specifications

The next seven steps need to be followed in defining a new method for Excelerator:

(1) define symbols for the object types,

(2) define the data entry forms for object and relationship types,

(3) describe the ENTITY TYPES for a graph type and its object types,

(4) describe the CONNECTIONS between object types,

(5) describe the MENUS for ENTITY TYPES and CONNECTIONS,

(6) produce a GRAPH CONVENTION, and

(7) integrate the graph type to Excelerator's Graphics and XLDictionary.

GROUP CONVENTION contains ENTITY TYPES, SHAPES and CONNECTIONS. The metamodel itself and all its object types are defined as ENTITY TYPES. For example, SMARTIE itself and its object types (Processor, Bank and Channel) are ENTITY TYPES. Relationship types between these object types such as LOOKS UP, GENERATES, RECEIVES and UPDATES are defined as CONNECTIONS. PROCESSOR, BANK and CHANNEL have their own SHAPES and the four CONNECTIONS are represented by lines.

The symbols are created using the Shape Editor, and the forms using the Screen Design tool. The next steps operate directly on the System Dictionary. A new metamodel needs an ENTITY TYPE for saving and accessing data in Excelerator. When this has been created, ENTITY TYPES for all object types will be created. The fourth step is to make the CONNECTIONS and their representations. The data entry screens have to be associated with ENTITY TYPES and CONNECTIONS. After MENUS have been described, ENTITY TYPES, CONNECTIONS, their respective MENUS, and SHAPES are linked together in GRAPH CONVENTION. The last step is to integrate the method specification into Excelerator's available set of method specifications.

## Modeling SMARTIE with Customizer

We modeled SMARTIE with Excelerator so that the object types (in Figure 1) are represented as ENTITY TYPES and the relationship types are defined as CONNECTIONS. The list of these are shown in appendix 3.

The following observations were made. First, Customizer contains no specific information for CONNECTIONS of a new method. The semantic checks are made after drawing the model by using the lists in the Excelerator's Analysis tool. These lists can be made only for Excelerator's standard methods. Thus, we cannot restrict the creation of a LOOKS UP link only between a PROCESSOR and a BANK. Therefore, it is difficult to model exact methods in sufficient detail. Second, explode paths can be made from ENTITY TYPES to other graphs. This means that decompositions such as A PROCESSOR IS EXPLODED TO A MODULE can be graphically (not semantically) handled. Third, links from one type of graph to other types of graphs can be made in the same way as decompositions. The link from PROCESS (in Interaction Communication Diagram) to State Model Diagram is also an explosion without any semantics. Fourth, Customizer can only make forms for properties of ENTITY TYPES and CONNECTIONS. A form like the Process Transition Table cannot be defined.

## Discussion

First we analyze the coverage of and differences between the CASE shells support for CASE shell properties. Figure 11 summarizes this: a cross in the table denotes that the CASE shell has the property, while a circle denotes that the CASE shell can partially support the property. An asterisk is used in the case another tool in a tool set supports this capability.

In examining the linguistic aspects we can conclude that these CASE shells all allow creation of new notations for concepts, extension of method specifications and definition of new ones. In addition, RAMATIC and Customizer can change between graphical and linear representations, but they do not support matrices. QuickSpec can only handle linear representations. One limit of the customized CASE environments is their translation capabilities. None of these tools embody mechanisms to define new notational and syntactic translations. Only RAMATIC can make new kinds of lists and reports from graphically defined IS specifications. Customizer's report models are fixed. Although Excelerator can generate code, it does not offer that mechanism for new method specifications.

<table><tr><td>CASE shell properties</td><td>Quick-Spec</td><td>RAMATIC</td><td>Customizer</td></tr><tr><td>Not. modifiability</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Not. variation</td><td></td><td>o</td><td>o</td></tr><tr><td>Not. translation</td><td></td><td></td><td></td></tr><tr><td>Synt. extension</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Synt. definition</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Synt. translation</td><td></td><td></td><td></td></tr><tr><td>Type specification</td><td></td><td></td><td></td></tr><tr><td>Query definition</td><td> $x^{*}$ </td><td>o*</td><td>o*</td></tr><tr><td>Report definition</td><td> $x^{*}$ </td><td></td><td> $x^{*}$ </td></tr><tr><td>Inference def.</td><td></td><td></td><td></td></tr><tr><td>Data storage def.</td><td></td><td></td><td></td></tr><tr><td>Usage definition</td><td></td><td></td><td></td></tr><tr><td>Export/import def.</td><td></td><td></td><td> $x^{*}$ </td></tr><tr><td>Data management def.</td><td></td><td>x</td><td></td></tr><tr><td>User interface def.</td><td></td><td>x</td><td></td></tr><tr><td>Data comm. def.</td><td></td><td></td><td></td></tr><tr><td>Oper. system def.</td><td></td><td>o</td><td></td></tr></table>

Fig. 11.

If we analyze the functions these CASE shells cover we note that only query and report definitions are well supported. QuickSpec supports these with limitations. When the user creates methods in MDM using PSL-types, s/he can export system descriptions to PSL/PSA and use QS to make queries and RSI to make reports. If the metalanguage is different from PSL, this capability is lost, however. RAMATIC can create different forms and retrieve information from graphical nodes. It has weak reporting facilities, and it does not support the report definition. Excelerator has a facility named Screen and Reports to define different report models and to use queries. Because these shells are based on data models instead of logical rules, their capabilities to make inferences are weak. Data storage and usage definitions are needed in a CASE shell to be effective. Also a distributed multi-user environment supporting group-work is required.

The third class of properties are mechanisms of CASE shells. Meta Systems (and LBMS) has not developed support for mechanism facilities in the configuration we examined. The only export/import definition is the ORIF language. RAMATIC can employ different kinds of DBMS based on binary associations, but it can be replaced by a relational DBMS. RAMATIC uses an interactive graphics interface and can manage several graphical window environments. It was developed on UNIX, but can be run on other operating systems. InTechs XL/Programmers Interface support import/export definitions for methods developed using Customizer.

Next we summarize the efficiency and the usability aspects of CASE shells. First, in terms of relative “modeling power”, the CASE shells examined offer quite different ways to model a method. If the available meta-metamodel contains powerful primitives, definition of a method is more difficult but more exact. QuickSpec and RAMATIC have sufficiently powerful meta-metamodels to deal with SMARTIE. RAMATIC’s meta-metamodel, however, has concepts that were developed as needs arose to extend the concept set. Therefore its modeling language is unsystematic and nonuniform. Customizer is based on a simple meta-metamodel; this is not powerful enough and offers weak semantic checks. If we compare the completeness of SMARTIE metamodels, then RAMATIC’s and QuickSpec’s models outperform that of Customizer. The main limitation of QuickSpec is that it uses only linear specifications. In our opinion, using graphical and matrix specifications in addition to the textual ones is a powerful and desirable feature of CASE shells. Thereby the effectiveness of handling large specifications and analyzing complicated dependencies between objects is much more easy. However, a complete support for kinds of representations is not available in these CASE shells.

The second comparison concerns the user interface (UI) of the CASE environments as a shell and a tool. If we look at the UI's of these shells, then Customizer's forms-based environment is more advanced than MDM's or RAMATIC's, which do not offer any editors for metamodeling.

But none of the CASE shells offer standard guidelines. Of the modified CASE tools QuickSpec is build on MS-Windows and RAMATIC on Presentation Manager (on OS/2), whereas customized Excelerator uses its own UI.

QuickSpec is used by selecting items from dialogues and lists, whereas RAMATIC and customized Excelerator use AutoCAD-style graphical editors. QuickSpec follows standards (SAA CUA guidelines) better than customized Excelerator or RAMATIC. Customized Excelerator has one critical limitation because it lacks support for windowing.

Third, in comparing the procedures followed when developing SMARTIE specification: “modeling” graphics needs one or two steps more than “modeling” mere textual specifications. As Customizer deals mostly with graphical notations and offers very little semantic checking its modeling procedure is quite straight forward. On the other hand QuickSpec has no graphics; this makes its procedure simple. Because RAMATIC has both, its use is the most complicated. So from the viewpoint of the IS developer RAMATIC provides the best support, but from the methodology engineer’s viewpoint it is the most difficult.

To summarize: the more powerful the tool for metamodeling and methodology support, the more difficult it will be to use in defining the desired environment. When building a new method, the lack of metamodeling knowledge will cause problems. It is likely that this will be a critical issue in using powerful tools. The usability of the CASE shell depends largely on the organizational competence and on the domain where the customized CASE tool will be used. Who will or can do the complex part of the method engineering – the CASE vendor, the methodology engineer of the IS department, or the IS designer?

Also: Who are optimal clients for CASE shells? There are at least the following: organizations that have long used their own methodologies, organizations which have difficulties to find a powerful tool to support certain methodology, and organizations that have done experimentations with fixed CASE tools and failed. However, the customized CASE environments have to offer the same information manipulation and managing facilities as the fixed ones in order to be successful.

## Summary

In this paper we have suggested a framework to compare CASE shells. The framework takes into account both facilities and usability aspects of the CASE shell. The facilities are linguistic components, functions, and mechanisms. To clarify usability of the tools we examine the meta-metamodel, the user-interface and the way of modeling, as suggested by the CASE shell. To demonstrate the viability of our approach we analyzed three CASE shells and evaluated their value by using the framework.

Currently most CASE shells do not meet all requirements of our framework. The greatest support is for the linguistic component. Current technology allows CASE shells to be more powerful and diversified. The current meta-metamodels of the CASE shells set limits to define complete methods, and they need to be enhanced. The efficiency and the usability of the CASE shell is important both at the shell and tool level. These also need to be improved in future.

## Acknowledgements

We wish to thank SISU, LBMS and Index Technology for their support in accomplishing this comparison.

## Appendix 1

SMARTIE definition in QuickSpec using PSL as XT Table language

OBJECT ATTRIBUTE;
OBJECT CONDITION;
OBJECT ELEMENT;
TAG FOR Attribute “Attribute”;
OBJECT ENTITY;
TAG “Entity”;
TAG FOR Message “Message”;
TAG FOR Fact “Fact”;
OBJECT EVENT;
OBJECT GROUP;
OBJECT INPUT;
OBJECT INTERFACE;
TAG “Interface”;
OBJECT MEMO;
OBJECT OUTPUT;
OBJECT PROCESS;
TAG FOR Processor “Processor”;
TAG FOR Module “Module”;
TAG FOR Transition “Transition”;
OBJECT PROCESSOR;
OBJECT RELATION;
TAG FOR Relationship “Relationship”;
OBJECT REQUIREMENT;
OBJECT RESOURCE;
OBJECT SET;
TAG FOR Bank “Bank”;
TAG FOR Channel “Channel”;
OBJECT SYSTEM-PARAMETER;
TAG FOR Delay-Time “Delay-Time”;
OBJECT UNIT;

PROPERTY CONTROL-PROCEDURE;
PROPERTY DERIVATION;
PROPERTY DESCRIPTION;
TAG "Description";
PROPERTY DISTRIBUTION;
PROPERTY DOCUMENTATION;
PROPERTY FALSE-WHILE;
PROPERTY LAYOUT;
PROPERTY LONG-NAME;
PROPERTY PROCEDURE;
PROPERTY TRUE-WHILE;
PROPERTY VOLATILITY;
PROPERTY VOLATILITY-MEMBER;
PROPERTY VOLATILITY-SET;

PROPERTY synonym; TAG "Code Number";

RELATIONSHIP associated-data-relation;
TAG FOR associated-with-part “Associated Attributes” WITH ROLE 1 associated-data-part “Attributes”; TAG FOR associated-data-part “Associated to Relationship” WITH ROLE 1 associated-with-part “Relationship”;

RELATIONSHIP collection-relation;
TAG FOR collection-part “Entities in Bank” WITH ROLE 1 collected-part “Entity”;
TAG FOR collected-part “Collected in Bank” WITH ROLE 1 collection-part “Bank”;

RELATIONSHIP composition-relation;
TAG FOR composed-part “Composed Of” WITH ROLE 1 composing-part “Composed of”; TAG FOR composing-part “Component In” WITH ROLE 1 composed-part “Component in”;

RELATIONSHIP consists-relation;
TAG FOR container-part “Consists Of” WITH
ROLE 1 contained-part “Consists of”;
TAG FOR contained-part “Contained In” WITH
ROLE 1 container-part “Contained in”;

RELATIONSHIP employs-relation;
TAG FOR employer-part “Looks up” WITH ROLE 1 employed-part “Bank”; TAG FOR employed-part “Looked up by” WITH ROLE 1 employer-part “Processor”;

RELATIONSHIP flows-relation;
TAG FOR flow-part “Message Transported” WITH
ROLE 1 qualifier-part “After (optional)”, 
ROLE 2 from-part “From”, 
ROLE 3 to-part “To”;

TAG FOR to-part “Message From” WITH
ROLE 1 qualifier-part “After (optional)”, 
ROLE 2 flow-part “Message”, 
ROLE 3 from-part “From”; 
TAG FOR from-part “Message To” WITH
ROLE 1 qualifier-part “After (optional)”, 
ROLE 2 flow-part “Message”, 
ROLE 3 to-part “To”; 

RELATIONSHIP generates-relation;
TAG FOR generator-part “Output Channel” WITH
ROLE 1 generated-part “Channel”; 
TAG FOR generated-part “Output from Processor” WITH
ROLE 1 generator-part “Processor”; 

RELATIONSHIP links-relation;
TAG FOR linked-part “Defines” WITH
ROLE 1 linked-to-part “Defines”; 
TAG FOR linked-to-part “Defined by” WITH
ROLE 1 linked-part “Defined by”; 

RELATIONSHIP modifies-relation;
TAG FOR modifying-part “Mutates” WITH
ROLE 1 modified-part “Fact”, 
ROLE 2 modified-in-part “In Bank”; 
TAG FOR modified-part “Mutated” WITH
ROLE 1 modifying-part “Mutator”, 
ROLE 2 modified-in-part “In Bank”; 
TAG FOR modified-in-part “Fact Mutation” WITH
ROLE 1 modifying-part “Mutator”, 
ROLE 2 modified-part “Mutated Fact”; 

RELATIONSHIP receives-relation;
TAG FOR receiving-part “Input Channel” WITH
ROLE 1 received-part “Channel”; 
TAG FOR received-part “Input to Processor” WITH
ROLE 1 receiving-part “Processor”; 

RELATIONSHIP references-relation;
TAG FOR referencing-part “Inspects” WITH
ROLE 1 referenced-part “Fact”, 
ROLE 2 referenced-in-part “In Bank”; 
TAG FOR referenced-part “Inspected” WITH
ROLE 1 referencing-part “Inspected by”, 
ROLE 2 referenced-in-part “In Bank”; 
TAG FOR referenced-in-part “Fact Inspected” WITH
ROLE 1 referencing-part “Inspected by”, 
ROLE 2 referenced-part “Fact Inspected”; 

RELATIONSHIP relates-relation;
TAG FOR related-to-part “Related To” WITH
ROLE 1 related-with-part “Related to”, 
ROLE 2 relation-part “Through (Optional)”;

TAG FOR related-with-part “Related With” WITH ROLE 1 related-to-part “Related with”, ROLE 2 relation-part “Through (Optional)”;

RELATIONSHIP subparts-relation;
TAG FOR superpart-part “Subpart” WITH ROLE 1 subpart-part “Subpart is”;
TAG FOR subpart-part “Part” WITH ROLE 1 superpart-part “Part of”;

RELATIONSHIP updates-relation;
TAG FOR updater-part “Updates” WITH ROLE 1 updated-part “Updates”;
TAG FOR updated-part “Updated” WITH ROLE 1 updater-part “Updated by”;

RELATIONSHIP value-relation;
TAG FOR valued-part “Value” WITH
ROLE 1 value-part “Value is”;

## Appendix 2

SMARTIE definition using RAMATIC's model definition language

MODELTYPE SMARTIE\_PROCESS
FREE PROCESSOR PROC\_SYM SETAUTO ID = NA
NAME = (MANDATORY, DUPLICATE\_MODELTYPE)
FREE CHANNEL CHAN\_SYM SETAUTO ID = NA NAME =
(MANDATORY, DUPLICATE\_MODELTYPE)
FREE BANK BANK\_SYM SETAUTO ID = NA NAME =
(MANDATORY, DUPLICATE\_MODELTYPE)
FREE SYSTEM SYS\_SYM ID = NA NAME = (MANDATORY, DUPLICATE\_MODELTYPE)
FREE INTERFACE INT\_SYM ID = NA NAME = (MANDATORY, DUPLICATE\_MODELTYPE)

CONN LOOKS\_UP BANK PROCESSOR ID = NA NAME = NA
CONN UPDATES BANK PROCESSOR ID = NA NAME = NA
CONN RECEIVES CHANNEL PROCESSOR ID = NA NAME = MANDATORY
CONN GENERATES CHANNEL PROCESSOR ID = NA NAME = MANDATORY

SET SYS SYSTEM MODULE NOT\_EMPTY
SET SYS SYSTEM INTERFACE NOT\_EMPTY
SET MOD MODULE PROCESSOR SYMBOL NOT\_EMPTY
SET INTERF INTERFACE CHANNEL NOT\_EMPTY
SET INTERF INTERFACE BANK NOT\_EMPTY

ENLARGE MODULE 2 MOD\_SYM
ENLARGE INTERFACE 2
ENLARGE PROCESSOR 2 PROC\_SYM
ENLARGE CHANNEL 2
ENLARGE BANK 2

<table><tr><td colspan="5">ENTITY TYPES:</td></tr><tr><td>Display text</td><td>Selector</td><td>Associated Type</td><td>Entity: Name</td><td>Explodes</td></tr><tr><td>Processor</td><td>P</td><td>SHP</td><td>PROCESSOR</td><td>SBD</td></tr><tr><td>Channel</td><td>C</td><td>SHP</td><td>CHANNEL</td><td></td></tr><tr><td>Bank</td><td>B</td><td>SHP</td><td>BANK</td><td></td></tr><tr><td colspan="5">CONNECTIONS:</td></tr><tr><td>Display text</td><td colspan="2">Selector</td><td>Associated Type</td><td>Entity: Name</td></tr><tr><td>Generates</td><td colspan="2">G</td><td>CON</td><td>SOLID</td></tr><tr><td>Looks_up</td><td colspan="2">L</td><td>CON</td><td>SOLID</td></tr><tr><td>Receives</td><td colspan="2">R</td><td>CON</td><td>SOLID</td></tr><tr><td>Updates</td><td colspan="2">U</td><td>CON</td><td>SOLID</td></tr></table>

MODELTYPE SMARTIE\_DATA
FREE ENTITY ENT\_SYM ID = NA NAME = (MANDATORY, DUPLICATE\_MODELTYPE)
FREE VALUE VAL\_SYM SETAUTO ID = NA NAME =
MANDATORY, DUPLICATE\_MODELTYPE)

CONN ASSOCIATES ASS\_SYM ENTITY ENTITY ID = NA NAME = NA
CONN SUBTYPES SUB\_SYM ENTITY ENTITY ID = NA NAME = NA

SET HAS\_ATTRIBUTE ENTITY VALUE SETAUTO NOT\_EMPTY
SET LINKS PROCESSOR ENTITY OWNER = SMARTIE\_PROCESS NOT\_EMPTY

```txt
TABLE SMARTIE_BEHAVIOUR
FORM "PROCESSOR TRANSITION TABLE"
FIXED LABEL = "MODEL" get_func = GET_MODELNAME
LABEL "CONDITION"
LABEL "PRODUCTION" DISPLAY_LENGHT = 45
TABLE DISPLAY_HEIGHT = 20 RROW = 19 MEMBER = ATTR OPTION =
BOX OPTION = SEQUENCE
FIXED LABEL = "DISPLAY_LENGHT = 7 GET_FUNC = get_number"
FIXED LABEL = "ACTIONS" COL = 10 DISPLAY_LENGHT = 30 GET_FUNC = get_acts
FIXED LABEL = "INSPECTIONS" COL = 42 DISPLAY_LENGHT = 30 GET_FUNC = get_insps
FIXED LABEL = "MUTATIONS" COL = 75 DISPLAY_LENGHT = 20 GET_FUNC = get_muts
FIXED LABEL = "RESPONSES" COL = 100 DISPLAY_LENGHT = 20 GET_FUNC = get_resps
FIXED LABEL = "COL = 122 DISPLAY_LENGHT = 7 GET_FUNC = get_delay"
END TABLE
END FORM
```

## Appendix 3

SMARTIE definition in Customizer

Interaction Communication Diagram (ICD)

State Base Diagram (SBD):

<table><tr><td colspan="5">ENTITY TYPES:</td></tr><tr><td>Display text</td><td>Selector</td><td>Associated Type</td><td>Entity: Name</td><td>Explodes</td></tr><tr><td>Entity</td><td>E</td><td>SHP</td><td>ENTITY</td><td></td></tr><tr><td>Value</td><td>V</td><td>SHP</td><td>VALUE</td><td></td></tr><tr><td>Subtype</td><td>S</td><td>SHP</td><td>SUBTYPE</td><td></td></tr><tr><td colspan="5">CONNECTIONS:</td></tr><tr><td>Display text</td><td colspan="2">Selector</td><td>Associated Type</td><td>Entity: Name</td></tr><tr><td>Attributes</td><td colspan="2">A</td><td>CON</td><td>SOLID</td></tr><tr><td>Associates</td><td colspan="2">C</td><td>CON</td><td>SOLID</td></tr><tr><td>Subtypes</td><td colspan="2">S</td><td>CON</td><td>SOLID</td></tr></table>

## References

[1] Bubenko, J., jr., “Selecting a strategy for computer-aided software engineering (CASE)”, SYSLAB, University of Stockholm, SYSLAB Report No 59, June 1988.

[2] Crozier, M., Glass, D., Hughes, J., Johnston, W., McChesney, I., “Critical analysis of tools for computer-aided software engineering”, Information and Software Technology, 31, 9 (November 1989) pp. 486–496.

[3] Vessey, I., Jarvenpaa, S.L., Tractinsky, N., “Evaluation of Vendor Products: CASE Tools as Methodology Companionships”, Communications of the ACM, 35, 4 (April 1992) pp. 90–105.

[4] Vessey, I., Jarvenpaa, S.L., Tractinsky, N., “Where do repositories come from”, CASE Outlook, 4 (December 1989) pp. 20–27.

[5] Misra, S., “CASE system characteristics: evaluative framework”, Information and Technology, 32, 6 (July–August 1990) pp. 415–422.

[6] Chen, M., "CASE Data Interchange Format (CDIF) Standards: Introduction and Evaluation", In Procs. of 26th Annual Hawaii Int. Conference on System Sciences vol. III (eds. J.F. Nunamaker jr. and R.H. Sprague jr.) IEEE Computer Society Press, Los Alamitos, California, January 1993, pp. 31–39.

[7] Lyytinen, K., Smolander, K., Tahvanainen, V.-P., “Modelling CASE environments in systems development”, Procs. of CASE89, The First Nordic Conference on Advanced Systems Engineering, Stockholm, 1989.

[8] Chen, M., Nunamaker jr., J.F., Weber, E., “Computer-Aided Software Engineering: present status and future directions”, Data Base, 20, 1 (January 1989) pp. 7–13.

[9] Dietz, J., “A Communication Oriented Approach to Conceptual Modelling of Information Systems”, In Procs. of the Int. Working Conference on Dynamic Modelling of Information Systems, Noordwijkerhout, Netherlands, April, 1990.

[10] Marttiin, P., Lyytinen, K., Tahvanainen, V.-P., Rossi, M., Smolander K., Tolvanen, J.-P., “Modeling requirements for future CASE: issues and implementation considerations”, In Procs. of the 13th Int. Conference on Information Systems (ed. J.I. DeGross, J.D. Becker and J.J. Elam) Dallas, Texas, December 1992, pp. 9–20.

[11] Smolander, K., Lyytinen, K., Tahvanainen, V.-P., Marttiin, P., “MetaEdit – A Flexible Graphical Environment for Methodology Modelling”, In Procs. of the CAiSE\*91 conference, Advanced Information Systems Engineering (eds. R. Andersen, J.A. Bubenko jr., A. Solvberg) Springer-Verlag, 1991, pp. 168–193.

[12] ISDOS, “An Introduction to the System Encyclopedia Manager”, ISDOS Ref No. 81 SEM-0338-1, ISDOS Project, Department of Industrial and Operations Engineering, The University of Michigan, Ann Arbor, Michigan, 1981.

[13] Chen, M., Nunamaker jr., J.F., “MetaPlex: an integrated environment for organization and information systems development”, In Procs. of the 10th Int. Conference on Information Systems (eds. J.I. DeGross, J.C. Henderson and B.R. Konsynski) ACM Press, New York, NY, 1989, pp. 141–151.

[14] Sorenson, P.G., Tremblay, J-P., McAllister, A.J., “The Metaview system for many specification environments”, IEEE Software, 30, 3 (March 1988) pp. 30–38.

[15] Meta Systems Ltd., QuickSpec - User's Guide (version 1.0.) Meta Systems Ltd., Ann Arbor, Michigan, 1989.

[16] Dolk, D.R., Kirsch II, R.A., “A Relational information resource dictionary system”, Communications of ACM, 30, 1 (January 1987) pp. 48–61.

[17] Bergsten, P., Bubenko, J., Dahl, R., Gustafsson, M., Johansson, L.-Å., “RAMATIC – a CASE shell for implementation of specific CASE tools”, TEMPORA T6.1, SISU, Stockholm, 1989.

[18] Index Technology Corporation, Customizer Reference Guide, Index Technology Corporation, Cambridge, USA, 1987.

[19] Index Technology Corporation, Excelerator Reference Guide, Index Technology Corporation, Cambridge, USA, 1987, 1989.

[20] Rose, T., Jarke, M., “A Decision-Based Configuration Process Model”, In Procs. of 12th International Conference on Software Engineering, Nice, France, 1990, pp. 316–325.

[21] Olle, T., Hagelstein, J., MacDonald, I., Rolland, C., Sol, H., Van Assche, F., Verrijn-Stuart, A., Information Systems Methodologies – A Framework for Understanding, IFIP, Addison-Wesley Publishing Company, 1988.

[22] LBMS, Information Manager User's Guide, Pre-Released Version 1.01, February 1991.

[23] Welke, R., Forte, G., “Meta systems on meta models”, CASE Outlook, 4 (December 1989) pp. 35–45.

[24] Smolander, K., “OPRR – A model for modelling systems development methods”, Next Generation of CASE tools (eds. K. Lyytinen and V.-P. Tahvanainen) Studies in Computer and Communication Systems, IOS press, Amsterdam, 1992, pp. 224–239.

[25] Welke, R., Metabasc - “A Platform for the next generation of meta systems products”, In Procs. of CASE Studies 1988, Meta Systems, Ann Arbor, May 1988, Meta Systems, Meta Ref. No. C8824, 1988.

[26] Index Technology Corporation, XL/Programmer Interface, Index Technology Corporation, Cambridge, USA, 1987.
