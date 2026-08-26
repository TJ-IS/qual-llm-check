---
otero_id: 17687
otero_key: "6NKXMRP7"
title: "RMT: A modeling support system for model reuse"
authors: "O Byung Kwon; Sung Joo Park"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00006-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# RMT: A modeling support system for model reuse

O Byung Kwon \*, Sung Joo Park

Department of Management Science, KAIST, 373-1 Kusong Dong, Yusong Gu, Taejon 305-701, South Korea

## Abstract

The ability to reuse models is an important issue for DSS modeling productivity. This paper presents a prototype system to support model reuse called RMT (Reverse Modeling Tool). The system is based on a framework which promotes reusability of DSS models using an idea of reverse modeling. Contrary to the typical modeling life-cycle, reverse modeling focuses on the identification, extraction, and reorganization of model constructs from existing models. RMT consists of: (1) a meta system that defines meta models to capture generic knowledge on model building, (2) a model translator that translates models into reusable model constructs, and (3) a model base. An object-oriented database (OODB) is adopted as a model base, which identifies model constructs as objects. The prototype system is developed using ONTOS on a UNIX workstation.

Keywords: Decision support systems; Meta system; Model reuse; Modeling support system; Reverse modeling; Object-oriented model management

## 1. Introduction

Model reuse was intended to increase the productivity of MS/OR modeling in DSS $[8,15,24,27–29]$ . It designates an attempt to reuse the whole or parts of models that already exist in an organization and is crucial in MS/OR modeling for the following reasons. First, it is inefficient to formulate models from scratch. Second, different modelers develop almost identical models for similar purposes. This may not lead to wrong decisions, but it does contribute to organizational inefficiency $[9,20,36,41]$ .

Since modeling primarily concerns itself with the ongoing use and modification of models $[28]$ , taking advantage of existing models would reduce the amount of additional modeling efforts. For example, a new model can be derived by some modifications of the sample models that are available in textbooks or in modeling software.

One approach to model reuse is to design reusable model constructs, such as the model library approach $[27]$ , which intends to create model templates that can be instantiated. Another approach is to produce an executable model represented in a specific modeling language was also addressed. The public translator approach, a translator writing system, is an example $[28]$ of yet another approach where the number of model translators are reduced by the public translator. However, writing the high-level translator that is required for each modeling language would still be a time-consuming task. Moreover, in developing reusable model constructs, the models are not stored in reusable forms but as a mingled set of model constructs $[17]$ . Interpretation of the models and restructuring them into manageable model constructs are needed as an initial step for model reuse.

The purpose of this paper is to present a framework that facilitates rapid interpretation of models, extraction of model constructs on the basis of modeling reference, and model construction. Instead of formulating a model from scratch, we attempt to collect modeling knowledge that is explicitly or implicitly associated with existing models. This process of modeling will be called reverse modeling. Reverse modeling (RM) is a process of identifying and collecting model constructs and translating them into a reusable form. The central idea of RM is based on a meta system $[34]$ that generates the model translator in order to interpret the constructs embedded in a model. The model translator then inserts the model constructs into a model base.

The RM framework consists of: (i) a meta system, (ii) a model translator, and (iii) a model base. The meta system defines a meta model and generates model translators. The model translator then divides the model into model constructs which are translated into a set of objects. The model base contains model constructs in a form of object structure. Based on this framework, a prototype system called RMT (Reverse Modeling Tool) has been implemented. The RMT generates model translators and provides model constructs in a model base.

In this paper we will focus on the extraction of model constructs from mathematical programming models that are represented in certain modeling languages. After extraction of the model construct, model reuse is briefly addressed to show feasibility of the framework. The remainder of the paper is organized as follows: literature review on the model management system is delineated in section 2; section 3 discusses the RM process while the overall framework of RMT with a system architecture is described in section 4; an illustrative example that demonstrates reuse using RMT is shown in section 5; conclusions are put forth in section 6.

## 2. Research in model management system

Model Management System (MMS) is a specific body within the DSS field that has focused on building and using models in a problem-solving environment $[14]$ . MMSs have come to denote generalized software systems that offer a wide range of models and allow for flexible access update as well as change of the model base.

Research on MMS has benefited from several technologies in the computer science area: database management systems, artificial intelligence including machine learning, and object-oriented programming. There are two distinct issues concerning MMS: model representation and model manipulation. With regards to the first issue, data base modeling has been extensively studied since delineation of models in MMS is similar to data management issues $[11]$ . The relational approach to model management recognized the model as a data set within functional dependencies $[4–6]$ . This approach utilizes data manipulation functions such as relational algebra, relational calculus, and query processing. Furthermore, knowledge-based systems have also been adopted for model management; they applied logic $[12]$ , frame $[3]$ , AND/OR graph $[24]$ , semantic nets $[13]$ and hybrid knowledge representations $[11]$ to represent models. The knowledge-based approach treats a model as a problem declaration that contains domain specific knowledge.

The second issue in MMS is concerned with the selection and execution of models, as well as the analysis of outputs which are directly related to model representation. Data manipulation functions of the relational database management system based on relational algebra and relational calculus can be used for model manipulation of the relational model. Inference engine, daemons, or machine learning algorithms can be adopted in the model manipulations of knowledge-based model management [12,14,38].

Recently, object-oriented model management has been suggested $[10,21,23,40]$ . Although this model management lacks a theoretical base $[7]$ and tends to come from implementation issues, it possesses several advantages for model management. First, in the object-oriented approach it is possible to unify different models within a single modeling paradigm, since models, model constructs, and solvers can all be identified as objects. Second, the inherent reusability of the object-oriented approach is promising for model management; for instance, since objects encapsulate their own properties and methods, a modeler can easily manipulate them against ongoing changes. The methods in the object-oriented approach perform an intermediary function when executed; passing messages and creating an interaction between the objects. Class inheritance is also a useful concept for model reuse because instances of the class can directly utilize properties or methods without re-defining them.

Model formulation is a process of creating a model that is efficiently solvable by, say, a mathematical programming solution method $[42]$ . The largely prevailing approaches to formulating mathematical programming models involve specific modeling languages and domain knowledge representations. The block-link approach was proposed to intelligently support the formulation procedures $[31]$ and the design of an interface in graphical forms was described $[26]$ . A logic-based modeling language, RM\*, represents domain specific knowledge in logic forms and then procedural modeling knowledge treats the domain specific knowledge as an instance of modeling knowledge $[1,2]$ . A prototype system in the IMMPS project to support formulation, discourse, and analysis support was proposed $[16]$ . Case-based reasoning techniques were also applied to model formulation supports $[22,24,25]$ . The case-based reasoning aims to acquire modeling knowledge from the specific model cases and to prepare and refine a knowledge base to formulate models to be reused in the future. However, since it assumes that the model cases are organized in a specific format, efforts for translating and restructuring the model cases in the specific format initially are required, which may prohibit the efficient implementations in practical cases $[25]$ . Increasing model reusability is also considered to improve the efficiency and effectiveness of the model formulation work. The basic ideas for model reusability are modularity, generalization, and the separation of a specific modeling language used from individual models $[30]$ .

## 3. Reverse modeling process

A conventional concept of modeling is considered to be a set of interrelated sequential activities ranging from problem identification to model production. The range is as follows: problem identification, variable identification, data collection, model selection, and model instantiation $[41]$ . Recently, it has been established that modeling is mostly an opportunistic process $[37,43]$ , from goal establishment to data collection, a hierarchical process in that model constructs can be identified as structured objects that encapsulate local characteristics $[35]$ . Block-wise approach to modeling was also proposed $[44]$ .

The model constructs and their related knowledge contribute to the modeling processes. For example, name, description, and assumptions of a problem are discussed in the problem identification phase. Variable identification is related to the determination of index set, parameters, coefficients, and decision variables, while data values of the coefficients are collected in the data collection phase. Information of model and solver classifications are necessary in model selection and model instantiation phases, respectively; hence, a formulated model is an aggregation of model constructs. RM is defined as a scheme to capture the model constructs from existing models and it also performs processes to:

(i) identify model (identification of model name, model type, purpose of model, and modeling language involved),

```txt
subject to:
```

(ii) extract model constructs (extraction of model constructs and their relationships), and (iii) deliver them to a model base.

An expert modeler, who avoids formulating models from scratch, usually refers to existing models that he/she has developed previously to prevent reinventing the whole or parts of the model constructs. When modeling, the modeler first recapitulates the purpose of an existing model and decides what modeling syntax will be used to interpret the model in more detail. The modeler then analyzes which model constructs are amalgamated within the model and how the constructs are related to each other. It is during this time that the modeler makes use of his/her knowledge on mathematical modeling, for example, in determining whether an attribute has and index set or a constraint that consists of decision variables, parameters, and a relational operator. The modeler then determines whether the collected constructs can be reused for a new model. Thus, as mentioned earlier, an expert modeler often looks into existing models through the whole model formulation process.

As an illustration, a simple transportation model is given as follows:

given:

(1) a collection of source regions (SOURCE: i) distinguished by their locations;

(2) destination regions (DESTINATION: j) distinguished by their locations; and

(3) transportation links (SOURCE,DESTINATION: i,j) from sources to destinations.

The data for a specific instance are:

SUPPLY $_{i}$ = available supply quantity of source region i;

DEMAND $_{j}$ = required demand quantity at destination region j;

UNIT.COST $_{ij}$ = cost to transport one unit of blend from source region $i$ to destination region $j$ . The variables are:

TRANS\_QTY $_{iy}$ = blend transportation quantity from source region i to destination region j.

The transportation model is:

Minimize COST

$$
C O S T = \Sigma_ {i j} U N I T _ {-} C O S T _ {i j} ^ {*} T R A N S _ {-} Q T Y _ {i j},
$$

$S(i) = \Sigma_{i}TRANS\_TQY_{ij}\leq SUPPLY_{i},$ (Source availabilities), and

$$
D (j) = \Sigma_ {i} T R A N S _ {-} Q T Y _ {i j} ^ {j} \geq D E M A N D _ {j}, (\text { Demands }).
$$

Suppose that MODLER [16] is used to formulate and execute the transportation model. The 'TransportationModel' in MODLER format is given in Fig. 1.

Since a typical model tries to minimize transportation costs due to the restriction of supply and demand, the modeler may refer the model to other analogous problems such as a transshipment model and an assignment model. For example, in the descriptions on ‘SOURCE’ and ‘DESTINATION’, the relationships between the two are seen as a constraint, and the cost function raised from them for an objective function are examples of reusable constructs.

## 4. RMT: An implementation of RM

## 4.1. Architectural overview of the RMT

A prototype system, Reverse Modeling Tool (RMT), is implemented using C++ and ONTOS, an object-oriented DBMS, on a UNIX workstation to demonstrate the feasibility of the framework. Based on the RM concept, an architecture for model reuse is shown in Fig. 2 which entails the following:

![](/api/attachments/6NKXMRP7/fulltext/images/f240b2f07eb150c7fb477c4352501905d13faef7514c7b11c1cf040d96d623a5.jpg)  
Fig. 1. Example MODLER model: a transportation model.

(i) meta system,

(ii) model translator, and

(iii) model base.

![](/api/attachments/6NKXMRP7/fulltext/images/66529aacd0030859898dfc77547495ebc384a0b0850cab522fa197e3aa15538c.jpg)  
Fig. 2. Architecture for model reuse by reverse modeling with meta view.

Since the meta system enables an easier development of individual support tools due to the flexibility built in for the various application domains, it has been extensively applied in the development of information systems $[19,33,39,45]$ . A meta system is adopted to model the scope of RM; that is, what and how to interpret and reuse the existing models. The meta system determines the view of reusable model constructs and their relationships, for the meta system takes formal specifications of model constructs as input and then generates a model translator as output. The meta system in the prototype system has dual roles of creating a meta model and generating a model translator, and hence, it consists of a meta model editor and a model translator generator. The meta model editor allows the creation of the meta definitions and file structures and stores them in the model base.

The model translator generator is a program that generates the model translators that are based on the meta definition and syntax of a specific modeling language. In the prototype system, each model translator extracts model constructs from existing models and adds them to a model base with the help of a lexical analyzer and a parser generator, LEX and YACC. For the repository of the model base, the ONTOS database, an object-oriented database, is used.

## 4.2. Meta model

A meta model is defined to capture the structure and semantics of model constructs. The definition of the structure of model constructs depends on the identification of the constructs and relationships between the constructs. It includes inheritance, instantiation, and aggregation, which are the basic principles of an object-oriented concept. The semantics are concerned with both the generic operations for model manipulation and the constraints.

An object-oriented model is chosen for a meta model, that is, all model constructs are identified as objects. The syntax of an object is defined as follows:

```txt
OBJECT object-name
[IS-A‘:‘({object-class-name‘,’‘)’)]
[INSTANCE-OF‘:‘({meta-object-name}‘)]]
[IS-AGGR-OF‘:‘({sub-object-name {‘,’sub-object-name}‘)]]
[ATTRIBUTES
[CONNECTORS‘:‘({association-name {‘,’association-name}‘)]]
[PARTICIPANTS‘:‘({source-object-name {‘,’target-object-name}‘)]]
[INVERSE‘:‘inverse-association-name]
[{user-defined-attribute-name‘:’object-property-name [‘ = ’default-value‘;’]}]
[OPERATIONS {operation-name({{signature }‘)}}]
[CONSTRAINTS {constraint-name {({{signature }‘)}}]
END_OBJECT.
```

Small letters are symbol elements and capital letters are reserved words. ‘[]’, ‘{}’, and ‘|’ means option, loop, and selection, respectively. A meta model has four groups to define: identification of structure, attributes, execution, and constraints. ‘IS-A’, ‘INSTANCE-OF’, and ‘IS-AGGR-OF’ relate to the identification of object structure. The ‘ATTRIBUTE’ defines ‘CONNECTORS’, ‘PARTICIPANTS’, ‘INVERSE’, and user defined attributes. ‘IS-A’ is defined so as to explicitly represent the inheritance hierarchy of a model construct. It is used when attributes or operations of the superclass are copied in a model construct. ‘INSTANCE-OF’ defines an object of an instance. It represents that ‘object-name’ is generated by the meta system with the ‘meta-object-name’. ‘IS-AGGR-OF’ represents the relationship of a model construct and its part. For example, a linear programming model is an aggregation of objective function and constraints, and a constraint is an aggregate of decision variables, parameters, relational operator, and RHS constant. 'CONNECTORS' enumerates associations that are related in meta objects. In case of associations, 'PARTICIPANTS' describes the source and target object names. 'INVERSE' defines an association that has an opposite meaning of the original association. User-defined attributes, as well as predefined attributes, can be defined and may have default values. 'OPERATIONS' specifies information on execution and generation of models. It includes operations to manipulate the constructs. 'CONSTRAINTS' explicitly defines modeling constraints.

![](/api/attachments/6NKXMRP7/fulltext/images/3d988fc729ac7fabb782ba550a91628cb1fa3f5d21be6806475216df00f7686b.jpg)  
Fig. 3. Structure of mathematical programming model.

The RMT creates, updates, and deletes the meta model including the syntax of modeling languages, if necessary. It also includes a compilation function to scan the two files and analyzes whether there are syntax errors in the files and displays error messages if necessary. When the compilation is finished successfully, model translators are generated. As an illustration, a mathematical programming model and a MODLER model are described below.

During the first stage, the mathematical programming model is composed of an objective function and constraints. Both are the aggregate of the left hand side (LHS) and right hand side (RHS) components. The LHS component is a set of terms that share the same summation sign for decision variables and coefficients with corresponding indices. The structure of mathematical programming models is depicted in Fig. 3. All constructs are defined in definitional language. A definition of “MathModel (mathematical programming model)” is shown as:

OBJECT MathModel
IS-AGGR-OF: (ObjectiveFunction, Constraint)
ATTRIBUTES
    model\_file\_structure: \*file
    name: string
    description: string
OPERATIONS
    putObject()
    deleteObject()
    generate(MathModel, model\_file\_structure)
    solve(MathModel)
CONSTRAINTS

![](/api/attachments/6NKXMRP7/fulltext/images/02c42ec9cf5d11816c612ae54d045e20acc36120804895000057d78641a50351.jpg)  
Fig. 4. Meta model edition.

message(MathModel, "must have at least one objective function")
message(MathModel, "must have at least one constraints")
message("Must be represented according to", MathModel, "syntax")
END\_OBJECT

(1).

“IS-AGGR-OF: (ObjectiveFunction, Constraints)” indicates the “ MathModel ” aggregate of “ ObjectiveFunction ” and “Constraints ”. The “ MathModel ” has a model file structure for model representation. “putObject( )” and “deleteObject( )” are concerned with the insertion and deletion of the instance of “ MathModel ”. “generate(MathModel, model\_file\_structure) ” shows the skeleton form of a “ MathModel ” in the specific modeling language syntax. The “ solve(MathModel) ” executes the mathematical programming model. There are several messages to be defined in the object. The meta model may be changed according to the modeler’s requirements. Fig. 4 represents the edit function of a meta model in RMT.

Meta specifications on the mathematical programming model are delineated in Appendix B. An object “MODLERModel” shown in (2) is a subclass of (1). It shows an example of meta definition for MODLER. The “MODLERModel” is a name of a model construct. It is an aggregate of several constructs called “Equation” that correspond to the information of objective function and constraints in the mathematical programming model. The “MODLERModel” refers to “Equation’s” as target objects and contains the name, original description and model file structure.

```python
OBJECT MODLERModel
IS-A: ()MathModel)
IS-AGGR-OF: (Equation, Equation)
ATTRIBUTES
    model_file_structure: * modler_file
    name: string
    description: string
OPERATIONS
    putObject()
    deleteObject()
    solve(MODLERModel)
    generate(MODLERModel, * modler_file)
CONSTRAINTS
    message(MODLERModel, “must have at least one equations”)
    message (“Must be represented according to ”, MODLERModel, “syntax”)
END_OBJECT
```

(2).

## 4.3. Model base construction

Basic processing for model base construction from language specific models consists of lexical analysis (LEX) and parser generation (YACC). LEX is a tool that assists the development of the source code routines by analyzing and interpreting an input stream. In RMT, the use of the lexical analyzer is as follows. First, it divides a source model (shown in Fig. 1, as an example) developed by a specific modeling tool into a set of generic model constructs, and second, it identifies the types of the model constructs. The definition of the types is provided by the meta model, in which the syntax of the modeling language is specified to identify the types of model constructs. Third, it appends additional characteristics, such as knowledge embedded in operations, constraints, and relationships to the constructs. Fourth, it stores the model constructs in the model base.

YACC reads the tokens and assembles them into language constructs for programming language compilation. For instance, the constructs of a programming language describe how keywords, identifiers, and expressions can be combined to form statements which are meaningful sequences for model restructuring. As a main body of the meta system, the model translator generator generates a lexical analyzer (LEX) and a parser generator (YACC) using the meta model and the model file structure as inputs. First, the generation rule for lexical analyzer consists of three parts: writing regular expressions for tokens, token type definitions, and main routine. Writing regular expressions scans all tokens in the model file structure and writes token types. Token type definition assigns the identification number to every token. The main routine is concerned with the starting a lexical analysis.

The generation rule for a parser generator also consists of three parts: token type definition, symbol definition, and main programs. The token type definition identifies tokens if they are terminal elements.

Symbol definition consists of a condition part and an action part, for each token in model file structure, the condition part identifies attributes. There are four attributes of the tokens: syntactical elements (a set of nonterminal symbols), tokens (a set of terminal symbols), optional nonterminal, and loop nonterminal. The action part refers to the meta specifications corresponding to the condition part. The main program writes the main routine to start parsing. The code generation skeleton rules of lexical analyzer and parser generator are shown in appendix A(a) and A(b), respectively.

Representation of model constructs as objects in an object-oriented model base has several advantages. First, a model construct as an object can be either generalized or specialized when necessary. For example, “PLANT”, “SOURCE” and “DESTINATION” in Fig. 1 can be generalized as “REGION”, and therefore common properties such as location are moved to “REGION”. Moreover, “MODLERModel” inherits “MATHModel” in that the model constructs and their relationship to the mathematical programming model can also be adopted in the MODLER model. Only information of specific syntax to MODLER is required additionally. Therefore “MATHModel” is a class of “MODLERModel”. Second, instances are naturally collected in an object that represents their model construct. It is clear that manipulations of instances are easier when they are stored in data base than in files.

![](/api/attachments/6NKXMRP7/fulltext/images/38c4556f11b767cee71070baf7559eeddf898c881ae640ceffe1540f017b4f08.jpg)  
Fig. 5. Model constructs in model base.

Third, overall information of a model construct can be encapsulated. Also additional operations and properties can be appended to model constructs, a feature needed for version control. Finally, model reuse at model formulation prevents inconsistency in managing model constructs by providing query processing for the information of existing model constructs.

## 4.4. Model reuse using object-oriented database

There are two ways to reuse model constructs in RMT: (i) using an ONTOS utility, and (ii) using model query procedures in RMT. To begin with, RMT interacts with ONTOS systems: database design tool, database administration tool, SQL session, and utilities (see Fig. 5). In particular, the DBDesigner can handle objects and their instances with a graphic user interface and displays a schema window, a type window, an instance list window, as well as an instance window. The schema window (left window of Fig. 5) shows the hierarchy of objects in the database. By using the create menu, a new construct that is inherited from an existing construct can be produced and enrolled as an object. The type window (right-upper window of Fig. 5) helps a modeler to put, delete, modify, and display objects on the screen.

![](/api/attachments/6NKXMRP7/fulltext/images/a954db57e9c498b05630cfe294389c82a4045db6df975e7d4f4fb018945186cd.jpg)  
Fig. 6. Model reuse with object-oriented database.

The window also shows and creates instances. The instance list window (right-lower window of Fig. 5) is shown for browser option on the schema window. The window lists all instances of a selected object in a separate window. Moreover, an instance window can browse over a selected instance that contains the name of the instance, the object of the instance, and public properties. Furthermore, it is possible to modify and add instances in the window. The capacity to browse and manipulate the object and instance is extremely beneficial for identifying the reusable components of a model.

The second way to reuse model constructs in RMT is that the RMT provides the modeler with the facility of query command generation to refer model constructs. Diverse manipulation commands illustrated by an object-oriented structured query language can be adopted $[18]$ . Fig. 6 shows how to reuse model constructs stored in the model base. The “Model-File” menu opens a specific model skeleton file.

After model reuse and formulation, verification and validation of the new model must be considered. Model verification refers to the proper building of the models and the inspection for consistency and completeness. The RMT enhances verification by allowing a modeler to develop a model with instantiation of a model skeleton. Providing model skeletons for standard model classes guides the model formulation. Model validation examines the usefulness of the developed model and refers to building the right models and can be conducted by comparing real and model-predicted data.

In RMT, full utilization of modeling information and meta models may increase the model validity. There are several methods to enhance the verification and validation as follows:

(i) checking the relationships between constructs,

(ii) browsing through the descriptions of constructs, and

(iii) showing help messages in meta models.

Once model construct extraction through RMT is successful, model reuse can be accomplished by the facilities in the object-oriented database management system. The capabilities of query processing make it especially possible to manipulate model constructs and to facilitate model formulation by utilizing information defined in the meta models. The use of the model base management capabilities implemented in the object-oriented database management system will increase model reusability.

## 5. An example with RMT

To show the concept's feasibility, a transportation model shown in Fig. 1 is selected as an example. To interpret the transportation model, the meta definition and model file structure for MODLER are used in the model translator. The translator receives a MODLER formatted model, “TransportationModel”, and slices the model in tokens and identifies token types. Token types are determined in the model translator generator. Using the existing model in Fig. 1 as an illustration, “SETS”, “TABLES”, etc. are identified as reserved words, “SOURCE”, “DESTINATION”, etc. are model constructs, and “source”, “region”, etc. are descriptive words.

The relationships of tokens are identified in terms of matching patterns provided by a parser. Table 1 shows the enumeration of extracted model constructs with their relationships from the transportation model example.

The parser then restructures the objects that come out of the RMT (as in Table 1) as a specific schema before loading a database. The internal window in Fig. 7 shows a result of model translation from the “TransporationModel”.

The model constructs are put into the ONTOS database (see Fig. 5) as persistent objects. The classify utility of ONTOS database performs this function. Classify utility reads a set of object definitions found in C++ header files and constructs database types, property types, and procedures that correspond to the classes, data members, and member functions found therein [32].

Table 1
Extracted model constructs

<table><tr><td>OBJECT</td><td>INSTANCE-OF</td><td>IS-AGGR-OF</td><td>ATTRIBUTES</td></tr><tr><td>SOURCE</td><td>primitive index</td><td></td><td>connectors: (.,SUPPLYof,SOURCEof) description: “source region”</td></tr><tr><td>DESTINATION</td><td>primitive index</td><td></td><td>connectors: (.,DEMANDof,DESTINATIONof) description: “destination region”</td></tr><tr><td>LINK</td><td>compound index</td><td></td><td>connectors: ((TRANS_QTYof, UNIT_COSTof),LINKof)</td></tr><tr><td>SUPPLY</td><td>primitive coefficient</td><td></td><td>connectors: (SUPPLYof) inverse: (SOURCEof) description: “available supply”</td></tr><tr><td>DEMAND</td><td>primitive coefficient</td><td></td><td>connectors: (DEMANDof) inverse: (DESTINATIONof) description: “required demand”</td></tr><tr><td>UNIT_COST</td><td>primitive coefficient</td><td></td><td>connectors: (UNIT_COSTof) inverse: (LINKof) description: “cost to transport 1 unit of blend”</td></tr><tr><td>TRANS_QTY</td><td>decision variable</td><td></td><td>connectors: (TRANS_QTYof) inverse: (LINKof) description: “blend transports”</td></tr><tr><td>Slhspieceof</td><td>lhspiece</td><td>(.,TRANS_QTY)</td><td></td></tr><tr><td>Dlhspieceof</td><td>lhspiece</td><td>(.,TRANS_QTY)</td><td></td></tr><tr><td>COSTlhspieceof</td><td>lhspiece</td><td>(UNIT_COST, TRANS_QTY)</td><td></td></tr><tr><td>Srhspieceof</td><td>rhspiece</td><td>(SUPPLY)</td><td></td></tr><tr><td>Drhspiece</td><td>rhspiece</td><td>(DEMAND)</td><td></td></tr><tr><td>COSTrhspiece</td><td>rhspiece</td><td>(.)</td><td></td></tr><tr><td>S</td><td>constraint</td><td>(Slhspiece, Srhspiece)</td><td>description: “limits supply at source”</td></tr><tr><td>D</td><td>constraint</td><td>(Dlhspiece, Drhspiece)</td><td>description: “required demand at destination”</td></tr><tr><td>COST</td><td>objective function</td><td>(COSTlhspiece, COSTrhspiece)</td><td>description: “total transportation cost”</td></tr><tr><td>SUPPLYof</td><td>coefficientof</td><td></td><td>participants: (SUPPLY, SOURCE)</td></tr><tr><td>DEMANDof</td><td>coefficientof</td><td></td><td>participants: (DEMAND, DESTINATION)</td></tr><tr><td>UNIT_COSTof</td><td>coefficientof</td><td></td><td>participants: (UNIT_COST, LINK)</td></tr><tr><td>TRANS_QTYof</td><td>decisionvariableof</td><td></td><td>participants: (TRANS_QTY, LINK)</td></tr><tr><td>TransportationModel</td><td>mathmodel</td><td>(COST,(S,D))</td><td>description: “assign source and destination to minimize transportation cost”</td></tr></table>

Assume that a modeler wants to build a transshipment problem by reusing the existing transportation model. Transshipment problem has additional features of allowing a shipment to pass transiently through other sources and destinations before it ultimately reaches its destination.

Since our example is to formulate a MODLER formatted model, the “\*modler\_file” is retrieved as shown in the upper-left window of Fig. 6. Internally, the following query command is executed.

SELECT Generate( TransshipmentModel, \*modler\_file)

FROM MathModel.

![](/api/attachments/6NKXMRP7/fulltext/images/56e7604f12e26c750d9d495f12ad7fd88373bbd8c47d5bb20938e2be8a4f4ab0.jpg)  
Fig. 7. Model translation.

The “\*modler\_file” is a MODLER syntax file based on BNF-grammar, a file already specified when the model file structure for MODLER was defined. “Generate(TransshipmentModel, \*modler\_file)” generates the skeleton form of a transshipment model in the MODLER syntax. The “skeleton” means that model constructs are not instantiated. The result is displayed in the upper-left window of Fig. 6. “Model\_query”, one of the sub-menus of “Database” menu, executes a model query support window (the upper-right window of Fig. 6). A modeler can explore a schema window and an instance window (the lower-left and lower-right of Fig. 6, respectively) to refer reusable constructs. For example, a modeler may search instances of “PrimitiveIndex” to find the desired indices, “SOURCE” and “DESTINATION”, and corresponding properties that identify the instances. Then the modeler may put them in the middle box of the model query support window. The operation instantiates “middle\_node” and “end\_node” in the transshipment skeleton file as “SOURCE” and “DESTINATION”.

The relationships between constructs are investigated through query command. For example, a modeler can decide whether or not “SOURCE” is appropriate for “middle\_node” in the transshipment model through query commands. The queries retrieve model constructs related to “SOURCE” as follows:

```sql
SELECT D.name
FROM DecisionVariable D, Index I
WHERE I.name = "SOURCE" AND
D.connectors() = I.connectors().
SELECT C.name
FROM Coefficient C, Index I
WHERE I.name = "SOURCE" AND
C.connectors() = I.connectors().
SELECT M.name
FROM MathModel M, Index I
WHERE I.name = 'SOURCE' AND
M.is_aggr_of().is_aggr_of().is_aggr_of().connectors() = I.connectors().
```

It displays “Trans\_qty” as decision variable, “Supply” and “Unit\_cost” as coefficient, and “TransportationModel” as model, respectively. Descriptions for each construct can be displayed as needed. For instance, a modeler can use a query command to seek relevant indices to formulate the transshipment model as follows:

## SELECT Name, Description

FROM Index.

The result of the query will be displayed as the following, since they already exist in the “TransportationModel” (see Fig. 1).

<table><tr><td>Name</td><td>Description</td></tr><tr><td>SOURCE</td><td>source region</td></tr><tr><td>DESTINATION</td><td>destination region</td></tr></table>

For message execution, "message()" operation in "CONSTRAINTS" part of the meta model, for example, may be used for model validation:

SELECT Message()

FROM MathModel

WHERE MathModel.name = "TransshipmentModel".

Executing the above query retrieves messages in (1) of section 4.2 such as “TransshipmentModel must have at least one objective function’ that can assist the modeler as a help message.

In this way, objects about indices (“SOURCE”, “DESTINATION”), coefficients (“DEMAND”, “UNIT\_COST”), decision variables (“TRANS\_QTY”), and constraints (“D”) of transportation model are used in the transshipment model. In addition, corresponding internal objects such as “Dlhspieceof”, “Drhspieceof”, “DEMANDof”, “TRANS\_QTYof” are also used to identify the relationship between the reused objects. Fig. 8 displays a newly formulated transshipment model and shows how the “Trans-

NAME TransshipmentModel
SETS
PLANT plant region
SOURCE source region
DESTINATION destination region
TABLES
SUPPLY\_P(PLANT) available supply
DEMAND (DESTINATION) required demand
UNIT\_COST\_P\_S (PLANT, SOURCE) unit cost
UNIT\_COST (SOURCE, DESTINATION) unit cost
ACTIVITIES
TRANS\_QTY\_P\_S (PLANT, SOURCE) transports from plant to source
TRANS\_QTY (SOURCE, DESTINATION) transports from source to destination
EQUATIONS
TRANSSHIPMENT\_COSTS(PLANT, SOURCE) = UNIT\_COST\_P\_S(PLANT, SOURCE) \*
TRANS\_QTY\_P\_S(PLANT, SOURCE) + UNIT\_COST(SOURCE, DESTINATION) \*
TRANS\_QTY(SOURCE, DESTINATION)
TRANSSHIP\_S(PLANT) = TRANS\_QTY\_P\_S(PLANT, SOURCE) <= SUPPLY(PLANT)
D(DESTINATION) requires demand at (DESTINATION) = TRANS\_QTY(SOURCE, DESTINATION)
>= DEMAND(DESTINATION)
EQUAL(SOURCE) = TRANS\_QTY\_P\_S(PLANT, SOURCE) - TRANS\_QTY(SOURCE, DESTINATION) = 0

Fig. 8. Output for transshipment model.

portationModel" is reused. Constructs in boldface with underline are reused and the remaining parts are added by the modeler. Reserved words for a certain specific modeling language such as "SETS", "TABLES", "ACTIVITIES" are provided by the generated skeleton file. These prevent a modeler from reinventing similar or identical models.

In this paper, we have shown how the reverse modeling concept is applied for linear programming models. However, the concept may be extended to other model classes such as simulation, econometrics, and stochastic models if a meta definition can be specified. For instance, a simulation model contains the nodes for creation, queue, activity and termination of job tokens. The nodes have attributes, operations, and constraints. These can be specified as a meta model to identify the reusable constructs within simulation models. For example, a meta model for a simulation model can be given as (3):

```txt
OBJECT SimulationModel
IS-AGGR-OF: (Create_node, Queue_node, Activity_node, Terminate_node)
ATTRIBUTES
model_file_structure: *file
name: string
description: string
OPERATIONS
putObject()
deleteObject()
generate(SimulationModel, model_file_structure)
solve(SimulationModel)
CONSTRAINTS
message(SimulationModel," must have at least one creation node and terminate node")
END_OBJECT
```

(3).

## 6. Conclusion

Issues on model reuse have emerged in model management as a result of the desire to increase the productivity and efficiency of DSS modeling. The fact that numerous modelers in an organization develop and maintain a considerable number of identical models $[9]$ implies that enriching the model share and maintenance for later use would enhance modeling work.

One way of model reuse through the extraction of reusable model constructs from existing models has been presented in this paper. The reverse modeling is a concept to take a model specification written in a specific modeling language syntax and interpret it as a set of objects that can be acquired in model base for further reuse. Meta concept was also considered in order to capture the general knowledge on how to reuse the models. A prototype system for model reuse, RMT, is implemented and is based on reverse modeling with a meta system. It interprets an existing model represented in a specific modeling language and transforms it into a set of objects to be stored in an object-oriented model base. The database functions such as data definition and data manipulation through query processing can be used for model management. The RMT supports an expert modeler to build the model library from existing models represented in a specific modeling language syntax. Even though the concept of reverse modeling has inherent limitations, such as the Tomato problem $[8]$ , application of queries may detect and confirm the possible limitations. In addition, applying the reverse modeling concept to other modeling classes such as econometrics, simulation, queuing theory, etc. remains as future research. In short, by reusing model constructs, the proposed RMT has shown the possibility of increasing the modeling productivity.

## Appendix A. Skeleton rules for model translator generation

```c
/*
INPUTS: model file structure (keyword names)
*/
Begin
read model file structure
/* writing regular expression for tokens */
begin
for all token types (tti)
case tti of
NUMBER:
print [\t] + ;[0-9] + [[0-9] + \.[0-9] + |\.[0-9] + |\.[0-9] + {return NUMBER;}
STRING:
print \"[^\\"\n]*[\\"\n] {return STRING;}
keywords:
print "keyword name" {return keyword name;}
carriage-return:
print \n {return "\n";}
endcase
endfor
end
/* token type definition */
begin
initialize token number = 0
```

for all token types (tti)
print #define tti + + token number
end
/\* main routine \*/
begin
print main program
end
End
/\*
OUTPUTS: lexical analyzer for model translation
\*/
(a) Skeleton rules to generate lexical analyzer

```txt
/*
INPUTS: model file structure, meta specification
*/
Begin
read model file structure
print %{C declarations %}
/* token type definition */
for all token types (tti)
print %token tti
print%%
/* symbol definition */
for all token types (tti)
case tti.attribute of
syntax element: /* nonterminal */
print tti
keyword: /* terminal */
print tti
option: /* optional nonterminal */
print tti|null
loop: /* loop nonterminal */
print tti:tti
endcase
read meta specification
for all token types (tti)
print {action part}
print%%
/* main programs */
print main program
End
/*
OUTPUTS: parser generator for model translation
*/
(b) Skeleton rules to generate parser generator
```

## Appendix B. Meta specification of MODLER model

OBJECT Index
// "Index" can be classified as "PrimitiveIndex" and "CompoundIndex" //
ATTRIBUTES
CONNECTORS: (DecisionVariableOf,CoefficientOf,IndexOf)
name: string
description: string
END\_OBJECT

OBJECT PrimitiveIndex
IS-A: (Index)
ATTRIBUTES
CONNECTORS: (DecisionVariableOf,CoefficientOf,IndexOf)
name: string
description: string
END\_OBJECT

OBJECT CompoundIndex
// "CompoundIndex" is compound of multiple "PrimitiveIndex" // IS-A: (Index)
ATTRIBUTES
CONNECTORS: (DecisionVariableOf,CoefficientOf,IndexOf)
name: string
description: string
CONSTRAINTS
message(CompoundIndex,"has two or more primitive indices")
END\_OBJECT

OBJECT DecisionVariable
// "DecisionVariable" is a decision variable for model output // ATTRIBUTES
CONNECTORS: (DecisionVariableOf)
name: string
description: string
CONSTRAINTS
message("Types of",DecisionVariable,"are numeric")
END\_OBJECT

OBJECT Coefficient
// "Coefficient" is an input variable such as LHS coefficient and RHS constants // ATTRIBUTES
CONNECTORS: (CoefficientOf)
name: string
description: string
CONSTRAINTS
message("Types of",Coefficient,"are numeric")
END\_OBJECT

OBJECT PrimitiveCoefficient
IS-A: (Coefficient)
ATTRIBUTES
CONNECTORS: (CoefficientOf)
name: string
description: string
CONSTRAINTS
message("Types of", PrimitiveCoefficient, "are numeric")
END\_OBJECT

OBJECT CompoundCoefficient
// "CompoundCoefficient" is a composition of some "PrimitiveCoefficient's" // IS-A: (Coefficient)
ATTRIBUTES
CONNECTORS: (CoefficientOf)
name: string
description: string
CONSTRAINTS
message("Types of", CompoundCoefficient, "are numeric")
message(CompoundCoefficient, "has two or more primitive coefficients")
END\_OBJECT

OBJECT LHSPiece
IS-AGGR-OF: (Coefficient, DecisionVariable)
ATTRIBUTES
name: string
description: string
END\_OBJECT

OBJECT RHSPiece
IS-AGGR-OF: (Coefficient)
ATTRIBUTES
name: string
description: string
END\_OBJECT

OBJECT Constraint
IS-AGGR-OF: (LHSpiece, RHSpiece)
ATTRIBUTES
name: string
description: string
END\_OBJECT

OBJECT ObjectiveFunction
IS-AGGR-OF: (LHSpiece, RHSpiece)
ATTRIBUTES
name: string
description: string
END\_OBJECT

OBJECT DecisionVariableOf
ATTRIBUTES
PARTICIPANTS: (DecisionVariable, Index)
INVERSE: (IndexOf)
name: string
description: string
END\_OBJECT

OBJECT CoefficientOf
ATTRIBUTES
PARTICIPANTS: (Coefficient, Index)
INVERSE: (IndexOf)
name: string
description: string
END\_OBJECT

OBJECT MathModel
IS-AGGR-OF: (ObjectiveFunction, Constraint)
ATTRIBUTES
model\_file\_structure: \* file
name: string
description: string
OPERATIONS
putObject()
deleteObject()
generate(MathModel, model\_file\_structure)
solve(MathModel)
CONSTRAINTS
message(MathModel, " must have at least one objective function")
message(MathModel, " must have at least one constraints")
message("Must be represented according to", MathModel, "syntax")
END\_OBJECT

## References

[1] H.K. Bhargava and S.T. Kimbrough, On Embedded Languages for Model Management, The 24th Hawaii International Conference on System Sciences, (1990) 443–452.

[2] H.K. Bhargava and R. Krishinan, A Formal Approach for Model Formulation In a Model Management System, The 24th Hawaii International Conference on System Sciences, (1990) 453–462.

[3] M. Binbasioglu and M. Jark, Domain Specific DSS tools for Knowledge-based Model Building, Decision Support Systems 2, No. 3 (1986) 213–223.

[4] R.H. Blanning, A Relational Theory of Model Management, Owen Graduate School of Management, Vanderbilt University, Nashville, Tennessee, Working Paper No. 85-106 (1985).

[5] R.H. Blanning, A Relational Framework for Join Implementation in Model Management, Decision Support Systems 1, No. 1 (1985) 69–82.

[6] R.H. Blanning, A Relational Theory of Model Management, in: Clyde W. Holsapple and Andrew B. Whinston, Eds., Decision Support Systems: Theory and Application, Chapter 2 (Springer-Verlag, Berlin, 1987).

[7] R.H. Blanning, Model Management Systems: An Overview, Decision Support Systems 9, No. 1 (1993) 9–18.

[8] H. Bhargava and R. Krishinan, Unique Names Violations: A Problem for Model Integration or You Say Tomato, I Say Tomatho, ORSA Journal on Computing 3, No. 2 (1991) 107–120.

[9] P.B. Cragg and M. King, Spreadsheet Modeling Abuse: An Opportunity for OR?, Journal of Operational Research Society 44, No. 8 (1993) 743–752.

[10] M.A.H. Dempster and A.M. Ireland, Object-oriented Model Integration in a Financial Decision Support System, Decision Support Systems 7, No. 4 (1991) 329–340.

[11] D. Dolk and B. Konsynski, Knowledge Representations for Model Management Systems, IEEE Transactions on Software Engineering 10, No. 6 (1984) 619–628.

[12] A. Dutta and A. Basu, An Artificial Intelligence Approach to Model Management Systems, IEEE Computer 17, No. 9 (1984) 89–97.

[13] J.J. Elam, J. Henderson and L. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of the First Conference on Information Systems, (Society for Management Information Systems, Chicago, IL, 1980).

[14] J.J. Elam and B. Konsynski, Using Artificial Intelligence Techniques to Enhance The Capabilities of Model Management Systems, Decision Sciences 18, No. 3 (1987) 487–502.

[15] A.M. Geoffrion, Reusing Structured Models via Model Integration, Proceedings of the 22th Hawaii International Conference on System Sciences, (1989) 601–611.

[16] H.J. Greenberg, A Primer for MODLER: Modeling by Object-Driven Linear Elemental Relations, University of Colorado at Denver (Denvor, Feb. 1991).

[17] K.M. Hee, L.J. Somers and M. Voorhoeve, A Modeling Environment for Decision Support Systems, Decision Support Systems 7, No. 3 (1991) 241–251.

[18] S.Y. Huh, Modelbase Construction with Object-Oriented Constructs, Decision Sciences 24, No. 2 (1993) 409–434.

[19] ISDOS Inc., Language Definition Manager User Manual SEM/LDM Version 1.4 (Jun. 1985).

[20] D. Keane and D. Mason, Beyond \$spread\$heet\$: dollars and sense, Interfaces 19, No. 1 (Nov. 1989) 33–35.

[21] B. LeClaire and R. Shadra, An Object-Oriented Architecture for Decision Support Systems, Proceedings of International Symposium on Decision Support Systems (1990) 567–586.

[22] J.K. Lee and M.Y. Kim, Case-Based Learning for Knowledge-based Optimization Modeling System: UNIK-CASE, Expert Systems with Applications 6, No. 1 (1993) 87–95.

[23] M.L. Lenard, An Object-Oriented Approach to Model Management, Decision Support Systems 9, No. 1 (1993) 67–73.

[24] T.P. Liang, Modeling By Analogy: A Case-Based Approach to Automated Linear Program Formulation, The 25th Hawaii International Conference on System Sciences, (1991) 276–283.

[25] T.P. Liang, Analogical Reasoning and Case-Based Learning in Model Management Systems, Decision Support Systems 10, No. 2 (1993) 137–160.

[26] P.C. Ma, F.H. Murphy and A. Stohr, A Graphics Interface for Linear Programming, Communications of the ACM 32, No. 8 (Aug. 1989) 996–1012.

[27] M.V. Mannino, B.S. Greenberg and S.N. Hong, Model Libraries: Knowledge Representation and Reasoning, ORSA Journal on Computing 2, No. 4 (1990) 287–301.

[28] S. Maturana, A Translator Writing System for Algebraic Modeling Languages, Western Management Science Institute, University of California, LA, No. 383 (1990).

[29] W.A. Muhanna, An Object-Oriented Framework for Model Management and DSS Development, Decision Support Systems 9, No. 2 (1993) 217–229.

[30] W.A. Muhanna, SYMMS: A Model Management System that supports Model Reuse, Sharing, and Integratrion, Decision Support Systems 10, No. 2 (1994) 214–242.

[31] F.H. Murphy and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2, No. 1 (1986) 39–47.

[32] ONTOS Inc, ONTOS DB 2.2 Developer's Guide (1992).

[33] S.J. Park, A Study on the Development of Intelligent Integrated CASE Tool Generator, Dept. of Management Science, KAIST (1992).

[34] S.J. Park and H.D. Kim, Constraint-based metaview approach for modeling environment generation, Decision Support Systems 9, No. 4 (1993) 325–348.

[35] S. Raghunathan, Planning Aids: An Intelligent Modeling System for Planning Problems based on Constraint Satisfaction, IEEE Trans. on Knowledge and Data Engineering 4, No. 4 (1992) 317–335.

[36] J. Schofield, Beware of Spreadsheets, Management Today, (Feb. 1987) 39–40.

[37] A. Sen, A. Vinze and S.T. Liou, Construction of a Model Formulation Consultant: The AEROBA Experience, IEEE Trans. Systems, Man and Cybernetics 22, No. 5 (1992) 1220–1232.

[38] M.J. Shaw, P.L. Tu and P. De, Applying Machine Learning to Model Management in Decision Support Systems, Decision Support Systems 4, No. 3 (1988) 285–305.

[39] D. Teichroew and E.A. Hershey, PSL/PSA: A Computer-aided Technique for Structured Documentation and Analysis of Information Processing Systems, IEEE Transactions on Software Engineering SE-3, No. 1 (1977) 41–48.

[40] L. Tung, R.G. Ramirez and R.D. Louis, Model Integration In An Object-Oriented Model Management System, The 24th Hawaii International Conference on System Sciences, (1991) 284–290.

[41] E. Turban, Decision Support And Expert Systems: Management Support Systems (Maxwell MacMillan International Editions, 1990).

[42] A. Vinze, A. Sen and S.T. Liou, AEROBA: A Blackboard Approach to Model Formulation, Journal of Management Information Systems 9, No. 3 (1993) 123–143.

[43] A. Vinze, A. Sen and S.T. Liou, Operationalizing the Opportunistic Behaviour in Model Formulation, International Journal of Man-Machine Studies 38, (1993) 509–540.

[44] J.S. Welch, PAM: A Practitioner's Approach to Modeling, Management Science 33, No. 5 (1987) 610–625.

[45] Y. Yamamoto, An Approach to the Generation of Software Life Cycle Support Systems, Ph.D. Dissertation, Univ. of Michigan, Ann Arbor, 1981.

![](/api/attachments/6NKXMRP7/fulltext/images/499a7ff33c531bbef208b7822ce0bdb7c31a081f9bf050936ee2578595d80561.jpg)

Sung Joo Park is Professor of Information Systems in the Department of Management Science at the Korea Advanced Institute of Science and Technology (KAIST) in Daeduck Science Park, Korea. He holds a B.S. degree in Industrial Engineering from the Seoul National University, an M.S. in Industrial Engineering from the Korea Advanced Institute of Science, and Ph.D. in Systems Science from the Michigan State University. He has been a senior researcher at the Software Development Center, KIST, and a professor at the KAIST since 1980. His areas of research interests include the integration of software engineering and MS/OR techniques, integrated modeling environments, and intelligent information systems.

![](/api/attachments/6NKXMRP7/fulltext/images/e43d7d320787eaa5bfa715cf6d2b1205b579f602edebeca43721901a3e9c5911.jpg)

O Byung Kwon is a Ph.D. candidate in the Department of Management Science at the KAIST. He received a B.A. degree in Business Administration from the Seoul National University, an M.S. in Management Science from the KAIST. His areas of research interests include the modeling environments, simulation, and software engineering.
