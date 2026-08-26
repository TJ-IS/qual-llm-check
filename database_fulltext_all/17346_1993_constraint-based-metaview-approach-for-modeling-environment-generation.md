---
otero_id: 17346
otero_key: "M9BXAVVK"
title: "Constraint-based metaview approach for modeling environment generation"
authors: "Sung Joo Park; Hyoung Do Kim"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90045-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Constraint-based metaview approach for modeling environment generation

Sung Joo Park and Hyoung Do Kim

Korea Advanced Institute of Science and Technology, Daejon, South Korea

Modeling environments for decision support systems (DSS's) play an important role in improving the efficiency and effectiveness of model-related work. The task of developing such an environment, however, is complicated and time-consuming. To improve the productivity and quality involved in the development of modeling environments, a metaview approach for generating these environments is proposed in this paper. Specifically, a constraint-based modeling framework is designed to specify modeling environments and associated modeling activities. The framework is based on a metaview that any modeling environment is a constraint enforcement system. A prototype environment generator called MetaDSS has been implemented. The practical generation of a modeling environment, a structured modeling environment specifically, is demonstrated using the MetaDSS.

Keywords: Decision support system, Modeling environment, Conceptual framework, Software integration, Prototyping, Metaview approach, Structured modeling

![](/api/attachments/M9BXAVVK/fulltext/images/befcdfcb0e204c06ca1999e567b919d260270816098a78bacf5a7b6a4428d574.jpg)

Sung Joo Park is Professor of Information Systems in the Department of Management Science at the Korea Advanced Institute of Science and Technology (KAIST) in Seoul and Daeduck Science Park, Korea. He holds the B.S. degree in Industrial Engineering from the Seoul National University, the M.S. in Industrial Science from the Korea Advanced Institute of Science, and Ph.D. in Systems Science from the Michigan State University. He has been a senior researcher at the Software Development Center, KIST, during 1978-80, and a professor at the KAIST since 1980. His areas of research interests include the integration of software engineering and MS/OR/Simulation techniques, knowledge engineering, and database. He is currently on leave from the KAIST and visiting the Management Science at UCLA, and is working on modeling environments.

## 1. Introduction

Modeling environments have been proposed as a means of solving the productivity, quality, and acceptance problems frequently facing the MS/OR and DSS community $[18,20]$ . A modeling environment is an integrated set of computer-based tools supporting all the activities for applied model-based work. Compared with most modeling systems which deal with one or two particular phases, it aims to support the entire modeling life-cycle. To fulfill its purposes, it must also be able to accommodate multiple modeling paradigms and solvers $[20,37]$ .

Despite its potential for improving model-based work, developing such an environment is a complicated task requiring a large amount of time and effort. This partially explains why the field of modeling environments is still in its infancy and practical ones are yet to come. The existing efforts to develop modeling environments are mostly to integrate a set of computer-based tools based on a special package such as multifunction software $[21,37]$ , relational DBMS $[13,31]$ , and knowledge-based tools $[3,4,7,14,15]$ . Various issues regarding the more comprehensive conceptual framework, model operation, implementation, and the functionality of environments are still open questions.

![](/api/attachments/M9BXAVVK/fulltext/images/80dd8fbd001f8e7a113d96438dfe4881edfc6c4aa061f259e7500b97ab9e685e.jpg)  
Hyoung Do Kim is a Ph.D. candidate in the Department of Management Science at the KAIST. He received a B.S. degree in Industrial Engineering from the Seoul National University, a M.S. in Management Science from the KAIST. He is currently working on the implementation and application issues of DS S and modeling environments.

As a way of improving the productivity and quality involved in the development of modeling environments, an approach for generating modeling environments is proposed in this paper. The approach is based on a meta-modeling framework called constraint-based modeling. The meta framework is designed to be rigorous and general enough to specify the semantics of the conceptual modeling framework and modeling activities of a target environment. The concept of metaview approach is not new. It has been suggested to reduce the effort of implementing software environments in software engineering $[8,30,44,45]$ , data modeling $[23,34,41]$ , and knowledge engineering $[10,33,36]$ .

A modeling environment restricts and guides modeling activities. The restrictions secure models against inconsistency and incompleteness. The constraint-based modeling framework reflects this view that a modeling environment is a constraint enforcement system. As in a rule-based development environment $[32]$ , the evolution of a system is enhanced by the explicit separation of organizational policy from programming code. Rather than embedding modeling knowledge into individual tools, a collection of rules can encapsulate all the knowledge about modeling activities $[25]$ . This knowledge not only facilitates controlled management of resources, but also makes the modeling environment flexible and modifiable.

Based on the constraint-based modeling framework, a prototype environment generator called MetaDSS has been implemented. MetaDSS automatically generates a logic-based integrated modeling environment.

The remainder of this paper is organized as follows. The constraint-based modeling framework and its formalism for specifying a target modeling framework and associated modeling activities are presented in section 2. For an illustrative purpose, structured modeling is used as a specific target modeling framework throughout the paper. MetaDSS and the process of generating a logic-based environment from the specification of environment components and constraints are discussed in section 3. The generated structured modeling environment is illustrated with examples in section 4. In section 5, the summary of the experience with MetaDSS and suggestions for further study are given.

## 2. Constraint-based modeling approach

## 2.1. Overview

A modeling framework is the basis for the symbolic definition of a modeling environment. The modeling framework provides a clear and precise way of representing models while it is the major source of restrictions or constraints on model contents by nature. These constraints, in effect, secure model contents against inconsistency and incompleteness.

For the integrity of modeling environment, various modeling activities are needed besides model representations such as the change or analysis of the contents of a model by a series of function invocations. Relationships among these functions can be specified in the form of constraints.

It is our view that these constraints need be explicitly specified and maintained throughout the development process and subsequent evolution of modeling environment, thus permitting flexible changes in the requirements of the environment when needed.

Constraint-based modeling framework provides a way of capturing, analyzing, and maintaining the constraints as a central part of modeling environments. It consists of the following constructs and constraints to guide the definition of a modeling environment:

(i) structural constructs,

(ii) management function definitions,

(iii) static constraints, and

(iv) dynamic constraints.

Structural constructs provide the basic facilities to capture the information on the structure of models. They define what types of structures are allowed in the framework. Management functions are used to check, query, update, and report the information captured within structural constructs to ensure them being complete and consistent. Also, they are used for interfacing with stand-alone systems such as DBMS's and solver packages. Management function definitions specify the basic information such as function names and parameters. Constraints are explicitly specified to modify and extend the definitions of structural information and management functions. Static constraints and dynamic constraints refine the structural components and management function definitions, respectively. They add the semantic knowledge about structural constructs and the invocation of functions. These constraints with modifiability are the key for the evolutionary nature of the constraint-based modeling framework.

## 2.2. The structural constructs and static constraints

A model is defined by means of modeling constructs. Various modeling constructs have been developed based on different conceptual frameworks. For example, the modeling constructs in GAMS [6] are set, parameter, table, scalar, variable, equation, and so on. In Structured Modeling [18,19], the modeling constructs are primitive entity genus, compound entity genus, attribute genus, function genus, test genus, module, etc.

Maintaining modeling constructs is important for the consistency and completeness of a model specification. When a model changes, predefined analysis routines are normally invoked to check the completeness and consistency based on the modeling framework. These routines are useful, but they are the obstacles to the integration and flexibility of model management because of the rigidity of the routines. These analysis routines are often embedded in the programming code and it is difficult to change the requirements of completeness and consistency.

To overcome this limitation of rigidity, meta-modeling concept is used in this paper. In the meta-modeling framework, the modeling constructs of environments are defined in structural constructs and the requirements of consistency and completeness are defined in terms of static constraints.

## Structural constructs

Structural constructs in meta-modeling framework consist of objects and relationships. Structural objects are meta-object types, i.e., the types of object types. Meta-object types define the types of model components in the modeling environment. Structural relationships are associations among structural objects. They define the types of relationship types, i.e., meta-relationship types which restrict the modeling of relationship types in the environment. A structural object is defined to participate in a structural relationship with a specific role.

## Static constraints

Static constraints are defined to capture the semantics of a modeling framework which are not expressed in the structural constructs. These constraints are assertions that must hold between a number of structural objects or structural relationships. In general, they can be further defined in terms of integrity constraints and deduction constraints. Integrity constraints refer to the requirements of existence consistency among model components. Deduction constraints are used to derive new facts from existing facts or knowledge. They simplify the analysis of model and the specification of constraints.

## 2.3. Management function definitions and dynamic constraints

As a part of modeling activities, various functions are needed to check, query, update, and report the structural information of a modeling environment. Among these functions, primitive functions and management functions are distinguished in the constraint-based modeling framework.

Primitive functions check the static facts according to the predefined analysis such as comparing user requests with the existing facts and checking the domains of attribute values. Two primitive functions of insert and delete are defined. The invocations of the primitive functions trigger an analysis process for model contents by using the constraints. This means that the capability of the primitive functions is easily extended by modifying the constraints.

Management functions analyze and manage the contents of a model. Examples are semantic analysis, report generation, and interface with external systems such as database systems and solver packages $[37]$ . Management functions extensively use the primitive functions in updating the contents of a model. Each management function is specified by name, parameters, and constraints for the relationships between the required functions.

Dynamic constraints are defined to control the functions by imposing preconditions and postconditions on the activation of functions. A precondition is the requisite condition that must be satisfied before the activation of a function. A post-condition is the condition on the output of a function invocation and on the consequential activations.

To model activation requests explicitly, permission and modality constraints are provided. A permission constraint relates an activation request with preconditions that must be satisfied. A modality constraint describes when a function must be invoked. Modality constraints have either of the two types of preconditions for the automatic invocation of functions: the pattern of static facts and the result of function invocations. These constraints make it possible to actively respond to modeling activities and the changes of model contents as in active DSS's $[24,39]$ .

## 2.4. A constraint-based modeling language

## Design principles

In designing a language for the constraint-based modeling framework, we follow some design principles: simplicity, structuredness, uniformity, and completeness. A language for constraint specification should be powerful enough to express all types of constraints that are of interest $[12]$ .

Full BNF-type syntax of the constraint-based modeling language is given in Appendix A.

## Structural constructs

The specification of structural constructs is based on the object-relationship model $[38]$ . The object-relationship model is an irreducible data model used for representing the information about conceptual frameworks as atomic and primitive as possible. Atomic and primitive facts increase modeling precision and generality. They can be combined in an appropriate way to form reasonably higher level concept rather than having a fixed structure imposed on all facts $[5]$ .

Each structural object is specified by combining keyword ‘object’ and the object name in parentheses. Each structural relationship is specified by combining the relationship name and a series of roles in parentheses. A role is composed of a ‘role name’, ‘=’, and a ‘structural object’ or ‘value range’. In the language, the properties of a structural object can be specified by binary relationships such as ‘attribute-is’. The properties of a structural relationship are defined using value-bearable roles of the relationship. The property values can be an integer, real, date, string, or file name.

The simple object-relationship model promotes the design principles of simplicity and structuredness. The same structures are also used uniformly for the specification of management functions and constraints.

## Static constraints

A static constraint consists of two parts: condition and action. The action part must be performed when the condition part is satisfied. To analyze the semantics of constraints systematically, each condition and action is expressed by unit predications which define a relationship with identifiers. An identifier represents any one of the existence of relationship, the cardinality of relationship, the domain of relationship role, variable binding, and comparison. All identifiers are joined by conjunction, and additional identifiers can be nested within an identifier to represent the existence of another relationship. Each identifier has its identification level and specifies the free variables of its direct upper level.

A static constraint can have a conjunctive normal form of unit predications as its condition part. Its action part is restricted to a single unit predication. In particular, the action parts of deduction constraints are restricted to form a unit predication with no identifiers. These restrictions are needed to simplify the first-order logic implementation of modeling environments.

## Management function definitions

Management functions are specified by the same formalism as structural relationships, except that they are permitted with only the role names of in, out, and inout. This type of function specification facilitates the uniform structuring of both of the dynamic constraints and the static constraints.

## Dynamic constraints

A dynamic constraint consists of a pair of condition and action parts as in a static constraint. The condition part of a permission constraint consists of a conjunctive normal form of unit predications. The condition part of a modality constraint consists of either the conjunctive normal form of unit predications or the output pattern of function activation. The output pattern is specified in the form of a unit predication preceded with a function activation type: insert, delete, or activate. 'insert' and 'delete' are followed by the object or relationship types to be inserted or deleted. 'activate' is followed by a management function to be invoked. The action parts of permission and modality constraints are made up of a unit predication preceded with a function activation type. For simplicity, the action part of a permission constraint is restricted to have no identifier.

## Structured modeling

To illustrate the constraint-based modeling framework, structured modeling $[17,19]$ is used as a target conceptual modeling framework in this paper. Structured modeling is a unified modeling framework based on acyclic, attributed graphs to represent cross-references between elements of a model and hierarchies to represent levels of abstraction. A model schema is primarily defined in terms of genera which group a set of data elements based on definitional similarity. There are six (or five excluding variable attribute genus) genus types: primitive entity, compound entity, attribute, variable attribute, function, and test. Primitive entities are existential in nature. Compound entities refer to other entities already defined and have no value. Attributes associate a certain property value with an entity or a combination of entities. Variable attributes are attributes which must be determined by the model. Functions can have values depending on those of other functions or attributes. Their values are respectively determined by a generic rule. Tests are functions except that their values must be either true or false. Each genus except primitive entity genera has calling sequences which identify its definitional dependencies on other genera. The definitional dependency between genera is monotonically ordered so that any cyclic dependency is not allowed. Genera are grouped into modules based on their conceptual similarity. The result of grouping is the modular structure all of whose leaves are genera, and all of whose non-terminal nodes are modules. It allows users to view the model at different levels of abstraction $[17,19]$ .

## Illustration

In order to define a modeling environment based on the constraint-based meta-modeling framework, the consistency and completeness requirements of the target framework must be identified. These requirements or knowledge are not complete themselves by all means and provisions are needed for further modifications and extensions. Constraint-based modeling framework allows these modifications and extensions. The typical requirements for structured modeling are summarized in Appendix B.

The generic structure of structured model can be represented by nine structural objects and five structural relationships. Structural objects are six genus types, two generic rules, and a generic range. Structural relationships are 'calls', 'computes', 'compares', 'ranges', and 'indexes'. 'calls' relationship defines definitional dependencies between genera. 'computes' and 'compares' relationships are used to attach one generic rule to each of function and test genera. 'ranges' relationships identify the domains of attribute values. 'indexes' relationships are used to determine the indexing properties of each genus.

A structural object, primitive entity genus, is defined as:

## object(peGenus);

where peGenus is an abbreviation of primitive entity genus. In the constraint-based view, this definition means that an object type could be a member of structured model if it is a primitive entity genus. The following defines a 'calls' relationship between a compound entity genus and a primitive entity genus.

## calls càller = ceGenus)(callee = peGenus);

This definition means that a 'calls' relationship type could be a member of structured model if its 'caller' is a compound entity genus and if its 'callee' is a primitive entity genus. In the relationship definition, 'caller' and 'callee' identify the roles of structural objects. Note that the order of roles can be changed if its role names are specified. A part of the structural constructs of structured modeling are formally defined in Appendix C.

An integrity constraint for calls relationship types, requirement (3) in Appendix B, can be represented as follows:

```matlab
if isTypeOf(type = A)(metaType = X)
(id: X = ceGenus or X = aGenus or X = vaGenus
or X = fGenus or X = tGenus)
then MUST calls càller = A)(callee = B)
(id: CARD(B) >= 1);
```

In the above specification, the first 'if' part is condition and the second 'then' part is action. 'id' and 'CARD' denote identifier and cardinality, respectively. 'MUST' implies that the constraint is an integrity constraint. Note that the identifier in the condition part disjunctively compares free variable X with a list of meta-object types. To simplify specifications, disjunctions are allowed in the identifiers for variable binding, comparison, and the domain of relationship role. A literary interpretation of the above specification is stated as follows: "if a type A is meta-type of X where X is one of compound entity genus, attribute genus, variable attribute genus, function genus, or test genus, then (type) A must call (type) B where the cardinality of B is greater than or equal to one."

As a part of provisions for further modifications and extensions, deduction constraints are used. New relationships can be deduced from the existing relationships. For example, a new 'indirectlyCalls' relationship type can be derived by a deduction constraint as follows:

```lisp
if calls càler = A)(callee = B)
(id: isTypeOf(type = A)(metaType = X))
(id: isTypeOf(type = B)(metaType = Y))
(id: calls càler = B)(callee = C)
(id: isTypeOf(type = C)(metaType = Z)))
then DEDUCE indirectlyCalls càler = A)
(callee = C);
```

In the above specification, 'DEDUCE' implies that the new relationship should be deduced. This constraint facilitates the specification of the following integrity constraint for the acyclicity of generic structure:

```txt
if isTypeOf(type = A)(metaType = X)
  (id: X = peGenus or X = ceGenus or X = aGenus or
    X = vaGenus or X = fGenus or X = tGenus)
then MUST indirectlyCalls càler = A)
  (callee = A)
  (id: CARD (A) = O);
```

Cyclicity is not permitted by stating that the existence of an 'indirectlyCalls' is negated by zero cardinality.

The full constraint-based specification of the requirements of structured modeling is listed in Appendix D.

To develop a structured modeling environment, various modeling activities need be supported in addition to the specification of the modeling requirements. This is possible by using the management functions and dynamic constraints in the constraint-based modeling framework. Let's take some examples to illustrate this further.

In order to delete a primitive entity genus already defined, it should be checked whether it is not called by any other genus. In other words, the deletion can be permitted only if no genus calls the specific primitive entity genus. The following permission constraint specifies this situation:

```sql
if calls càller = B)(callee = A)
(id: CARD(B) = 0)
then PERMIT delete isTypeOf(type = A)
(metaType = peGenus);
```

The constraint states that the environment permits to invoke a delete function for a primitive entity genus only if the precondition that the genus has no caller is satisfied.

As an additional example of management function, the knowledge for generating the modular structure report are specified in the form of the following functions and constraints:

```matlab
msReport(in = Model);
gen_sm_irt(in = Model)(in = IRT);
gen_msReport(in = IRT)(in = MS);
if isTypeOf(type = A)(metaType = model)
    (id: contains(container = A) (member = B)
    (id: CARD(B) >= 1))
then PERMIT activate msReport(Model = A);
if activate msReport(Model = A)
then MUST activate gen_sm_irt(Model = A)
    (IRT = X)
    (id: X = CONCAT(A and '.irt'));
if activate msReport(Model = A)
then MUST activate gen_msReport(IRT = X)
    (MS = Y)
    (id: X CONCAT(A and '.irt'))
    (id: Y = CONCAT(A and '.ms'));
```

When a modeler requests an 'msReport' with an input variable "Model", the environment permits the function invocation if the model contains more than or equal to one member. When permitted, the environment automatically activates 'gen\_sm\_irt' and 'gen\_msReport' in sequence. 'gen\_sm\_irt' function generates an internal representation file of structured modeling where the name is concatenated with an extension '.irt'. This file becomes a means of interface with external management functions such as 'gen\_msReport'. Function 'gen\_msReport' produces the modular structure report file named with the concatenated extension of '.ms'.

The above examples illustrate how to support the various modeling activities defined by the management functions and dynamic constraints. They also show that these functions and constraints are specified uniformly, and possess the evolutionary feature in terms of the demonstrated modifiability and extensibility under the constraint-based meta-modeling framework.

## 3. Implementation of an environment generator: MetaDSS

Based on the constraint-based meta-modeling framework, a prototype generator of logic-based modeling environment called MetaDSS has been implemented under UNIX on SUN. In the MetaDSS, there are two levels of modeling: meta-level and environment level. At the meta-level, environment designers define the characteristics of a target environment. Figure 1 shows the process of defining a structured modeling environment. The defined characteristics can be analyzed using standard reports and simple queries. After completing the constraint-based specification and analyses, a logic-based modeling environment is generated. The generation process embeds the defined characteristics into the environment, sets up standard tools, and generates a modeling guide. At the environment level, DSS developers and decision makers use the generated environment, structured modeling environment in this specific case, to specify models and data required for decision making. The specified model or model instances will be analyzed by the generated modeling environment also.

![](/api/attachments/M9BXAVVK/fulltext/images/122bd17bd1d47d4bb986df1519890a1a8a445abd8ea1ccc8a46b314472562074.jpg)  
Fig. 1. MetaDSS modeling process for defining structured modeling framework.

## 3.1. Processing requirements

Modeling environments specified by the constraint-based modeling framework need knowledge-based reasoning mechanisms for the analysis of the constraint knowledge: forward and backward chaining. In forward chaining, a reasoning system generates all the reachable states by matching initial and intermediate facts with the conditions of its rules. In backward chaining, a reasoning system starts with a goal configuration, finds one or more general rules whose conclusion matches the goal to some extent, and formulates as a new goal the problems of satisfying all the conditions for applying the general fact $[22]$ .

Integrity constraints and modality constraints should be processed by the forward-chaining control strategy. This is because the action part of an integrity constraint must be activated when its condition part becomes true. Also, the function in the action part of a modality constraint must be invoked as soon as its condition part is satisfied.

The goal predicate in the action part of a deduction constraint must be evaluated true or false only when requested by users or another constraint. The condition part of a permission constraint must be checked only when the function in its action part is invoked. Therefore, these two types of constraints should be processed by the backward-chaining control strategy.

## 3.2. Logic modeling

MetaDSS adopts logic modeling as a logical foundation to construct modeling environments. Logic modeling provides a powerful tool to support model-related works of MS/OR and DSS by its rich expressive power, declarative representation, and deduction capability $[28]$ . First-order predicate logic is also very convenient for the verification of semantic completeness and consistency $[43,48]$ .

Interestingly, meta-level models can be constructed using the same facilities available for the object-level models in logic, which is analogous to the fact that a PROLOG meta-interpreter can be written in PROLOG [1]. For example, the embedded technique [2,7] applies the meta-level modeling features to MS/OR problems, and financial modeling by logic programming [35] intensively uses meta-level interpreters. Meta-level modeling, which embeds the knowledge about a conceptual framework into logic predicates, plays a central role in the generation of the constraint-based modeling environment.

## 3.3. Environment generation

Basically, all the constraints are embedded in logic predicates. Then the embedded knowledge is used to guide the modeling activities in the generated environment. Additionally, the backward-chaining control strategy of logic can be directly applied to deduction and permission constraints by generating legitimate logic expressions from the constraints.

A structural object is defined by a predicate called 'metaObjectType', e.g., the primitive entity genus is defined by metaObjectType(peGenus). Structural relationships are converted into permission constraints in logic-based environments to check the insertion of new relationship types. For illustration, the following 'constraint' predicate is generated from the 'ranges' meta-relationships:

```prolog
constraint(relCons4,permit,
(insert ranges(X1,Y1,X2,Y2)
:
X1 = attribute,
X2 = domain,
(isTypeOf(type,Y1,metaType,aGenus),
isTypeOf(type,Y2,metaType,gRange);
isTypeOf(type,Y1,metaType,vaGenus),
isTypeOf(type,Y2,metaType,gRange);
isTypeOf(type,Y1,metaType,fGenus),
isTypeOf(type,Y2,metaType,gRange))).
```

The predicate embeds the permission knowledge about the 'ranges' relationship types and has three parameters. The first parameter, 'relCons4', is the name of the constraint which MetaDSS has attached. The second one, 'permit', identifies the type of the constraint. The third one describes the contents of 'relCons4' constraint. The constraint is to check the precondition for inserting 'ranges' relationship types;

(i) Role names X1 and X2 must be attribute and domain, respectively.

(ii) Object types YI and Y2 must be a pair with (meta)types of aGenus and gRange, vaGenus and gRange, or fGenus and gRange.

All the explicit constraints are converted into logical expressions without significant modifications. For example, the constraint for requirement (3) in Appendix B is converted into the following predicate:

constraint(minCallee, must, (cardinalityThen(X1, calls càler, A, callee, X1), N1, 6, 1)

isTypeOf(type,A,metaType,X), member(X,[ceGenus,aGenus,vaGenus,fGenus,tGenus]))).

In order to represent the constraints in logic, predefined predicates of 'cardinalityIf', 'cardinalityThen', 'domainIf', 'domainThen', 'bind', and 'comp' are provided in the generated modeling environment. Their meanings can be summarized as follows;

(i) CardinalityIf(X,Y,N) - the number of instances of X such that Y is provable is N.

(ii) CardinalityThen(X,Y,N,Comparator,Criterion) - cardinalityIf(X,Y,N) and comparing N with Criterion by Comparator must be true.

(iii) DomainIf(X,D) - the value of X must belong to one of the domain list D.

(iv) DomainThen(X,Y,D) - all the instances of X such that Y is provable must belong to one of the domain list D.

(v) Bind(X,Y,Exp) - all the instances of X such that Y is provable must be a member of Exp.

(vi) Comp(X,Y,Comparator,Criterion) - comparing each instance of X with Criterion by Comparator such that Y is provable must be true.

The modality constraints related with the activation of msReport are also embedded into the constraint predicate as follows:

constraint(generationOfIRT, must, (bind(X, gen\_sm\_irt('Model', A, 'IRT', X), [concatenation(C110, A, '.irt')]),

activate gen\_sm\_irt('Model',A,'IRT',X)
:-

activate msReport('Model',A)).

constraint(generationOfMS, must,

(bind(X,gen\_msReport('IRT',X,'MS',Y), [concatenation(C110,A,'.irt')]),

bind(X,gen\_msReport('IRT',X,'MS',Y),

[concatenation(C120,A,'.ms')]),

activate gen\_msReport('IRT', X, 'MS', Y)
:-

activate msReport('Model',A)).

MetaDSS also generates model components which can be derived from the constraints. Let's assume that a function genus must have one generic rule selected from a set of symbolic rules. If the set is {SUM, VSUM, NEGATIVE, PRODUCT, INVERSE, DOT}, the following integrity constraint can be defined:

if isTypeOf(type = A)(metaType = fGenus)

then MUST computes(function = A)(rule = B)

(id: B = 'SUM' or B = 'VSUM' or B

= 'NEGATIVE' or

B = 'PRODUCT' or B = 'INVERSE' or B = 'DOT')

From the constraint, MetaDSS generates the following model components:

computationRule('SUM').

computationRule('VSUM').

computationRule('NEGATIVE').

computationRule('PRODUCT').

computationRule('INVERSE').

computationRule('DOT').

This type of generation mechanism built in MetaDSS relieves modeler from the chores of modeling standard (derivable) object types.

## 4. Constraint-based structured modeling environment

In this section, the modeling process in the constraint-based structured modeling environment is illustrated with examples, and its advantages and disadvantages are discussed.

## 4.1. Two example problems

For an illustrative purpose, we use two problems. One problem is the oft-cited Hitchcock-

Koopmans transportation problem [13,17,31]. The other one is the production component of a strategic corporate planning problem of a large-scale iron and steel manufacturing company in Korea.

The transportation problem has two primitive entity genera, 'customer' and 'plant', corresponding to product consumer and producer, respectively. Each 'customer' has a minimum demand and each 'plant' has a maximum supply capacity. There is one compound entity genus, 'link', corresponding to transportation route. Each 'link' has a 'unitcost' value for transporting one unit from a 'plant' to a 'customer', and a 'flow' value to be determined by the model. In the above statement, 'demand', 'supply', and 'unitcost' are attribute genera and 'flow' is a variable attribute genus.

The strategic corporate planning problem is to support the analysis of the long-term and uncertain profile of the company. The production system of the large-scale iron and steel company with the capacity of more than ten million metric tons per year includes hundreds of plants and thousands of processes to produce more than one hundred thousand products or dozens of products in large groups. The model needs to span more than ten years of time horizon and should take into account the annual plans of the shutdowns, maintenance schedules, and new constructions of plants, etc. It is very complex to model such a large-scale production system and becomes a good example of the application of modeling frameworks [27]. By applying the structured modeling framework, the model is composed of three primitive entity genera: 'product', 'plant', and 'year', and six compound entity genera: 'y-prod', 'y-plant', 'ip', 'po', 'ipo', and 'unitflow'. A 'y-prod' and 'y-plant' are a 'product' to be produced or a 'plant' to be operative in a given 'year'. The other compound entities are used to specify the material flows.

## 4.2. Modeling processes

The structured modeling environment generated by MetaDSS is accessible directly in the first-order predicate logic. The generated modeling guide facilitates logic modeling activities by providing templates of object types, relationship types, and functions in changing the contents of a model or in activating other functions. Figure 2 shows a guided modeling process for inserting a 'calls' relationship type of the transportation problem.

![](/api/attachments/M9BXAVVK/fulltext/images/26f6e87e8c03313cc0a790b159aab53f219a444b2fe6a04530e229b9367787ea.jpg)  
Fig. 2. A guided modeling process in defining the 'transportation' model.

In the logic modeling, an object type is specified by a predicate isTypeOf(type,A,metaType,X) which is equivalent to X(A). Modeling requests are made by the predicate preceded with a function activation type. For example, a primitive entity genus of the transportation problem, 'product', can be added as follows:

?-insert peGenus(product).

NEW MODEL COMPONENT :: peGenus (product)

\*\*\* Checking Constraints

VIOLATION

POSITION :: DOMAIN :: satisfy(gmOrder(genus,product,mOrder,\_6))

VIOLATED CONSTRAINT gmOrderReqts
VIOLATION

POSITION :: CARDINALITY :: cardinalityIf (6, contains(container, \_6, member, product), 0)  
VIOLATED CONSTRAINT genusContainer

The modeling environment responds to the activation of the primitive function, i.e., the insertion of 'product' as a primitive entity genus in this particular case, with the identification of two violated constraints. The violated constraints mean that the 'product' should be characterized by 'gmOrder' and 'contains' relationship types. These messages guide what you should do in the next step to remove the violations. Relationship types are modeled in the same way. For example, a 'ranges' relationship for supply can be added as follows:

## ?- insert ranges(attribute,supply,domain,'R +').

Note that supply and 'R +' should be defined previously as an attribute genus and a generic range, respectively. If this is not true, the request is not permitted because it violates the permission constraint mentioned in Section 3. The complete and consistent specification of the transportation model is listed in Appendix E.

The contents of a model can be analyzed by management functions as well as logic queries. The modular structure report of the transportation model can be generated by the following request in MetaDSS:

![](/api/attachments/M9BXAVVK/fulltext/images/20608490382bb036c8fcd6b38256171b1e2ff3bd9da0ce4467bd54ba6e18535d.jpg)  
Fig. 3. A modular structure report of the 'transportation' model.

?-activate msReport('Model', transportation).

It is also possible to view and edit the report interactively under the modeling guidance as shown in Figure 3.

When the model schema is complete and consistent without any violations of constraints, an instance of the model can be specified based on the schema. The generated modeling environment supports two types of instance modeling: modeling based on constraints and syntax-directed editor/analyzer. For constraint-based instance modeling, a management function 'gen\_data\_cons' should be activated to generate the constraints on the components of model instances. The formalism of the constraints conforms to that of the static and dynamic constraints. For example, the following permission constraint is generated from the 'calls' relationship between 'link' and 'plant':

constraint(dataCons4, permit,

(insert data(D1,D2,D3,D4,D5,D6)

:-

D1 = relType,

D2 = calls,

D3 = link,

data(objType,link,instance,D4),

D5 = plant,

data(objType, plant, instance, D6)).

In the above constraint, 'data' predicate specifies the relationships between schema and instance components for data modeling.

Any domain-specific constraints on model instances can be added to the set of generated constraints. For example, in the production problem, the product type of a product, 'prType', must be either 'final' or 'in-process'. The integrity constraint for this case can be represented as follows:

constraint(prTypeCons, must,

(bind(D6,data(relType,contains,m\_yProd1,D4,prType,D6),[final,in-process])

true)).

Note that attribute values are specified using 'contains' relationship types.

Another method of instance modeling is to generate a syntax-directed editor/analyzer. An existing syntax-directed editor/analyzer generator [40] is used and the generation is made possible in the MetaDSS by issuing an interface file to the generator. The generated editor/analyzer supports direct checkings on attribute and relationship characteristics such as cardinality and domain. It maintains the instance data in a relational database. Figure 4 shows the process of editing the instance of the transportation model guided by the generated syntax-directed editor/analyzer.

![](/api/attachments/M9BXAVVK/fulltext/images/81ece90574def2fcc93d6b2d97d49102360667223afdf4702cf839475644ee5a.jpg)  
Fig. 4. Data modeling in a syntax-directed editor/analyzer.

In modeling a large-scale problem such as the integrated production system, modeling efficiency is very important. To illustrate this point, the modular structure report of the production model schema is given in Appendix F. In interactive modeling mode in MetaDSS, all the integrity constraints are checked to determine what constraints are violated and what causes the violation when a new model component is inserted. The checking after each component modeling becomes an impediment, however, to the rapid modeling. Intermediate checking process may be omitted provided that all the model components are checked in the final stage.

## 4.3. Discussion

The experiences with the constraint-based structured modeling environment can be summarized as follows:

(i) The knowledge about the structured modeling environment, embedded in logic predicates, plays an important role in guiding and checking modeling activities.

(ii) The generated environment is active in notifying users of the violated constraints and in automatic processing of directly related modeling activities.

(iii) Changes to the environment by MetaDSS are easy and rapid. Based on this rapid prototyping capability, an object-oriented reconstruction of the structured modeling framework [26] and the derivation of mathematical components from the conceptual components of a model schema [27] are being investigated.

In comparison with the structured modeling systems based on relational databases $[13,31]$ , the constraint-based environment is more active. The relational DBMS-based systems mainly depend on query languages in analyzing model contents. In spite of their powerful data analysis capability, these systems can not manage modeling activities and are limited in active responses to user requests. In comparison with FW/SM, a structured modeling environment based on a multi-function software package $[21,37]$ , the constraint-based environment is more flexible and integrated. FW/SM provides a large number of separately invokable functions for users not to perform multiple tasks when they need only one. However, the knowledge about the functions, e.g., the sequence relationships between the functions should be maintained by the users. In spite of the exhaustive error checking with respect to the underlying structured modeling framework, it cannot employ domain-specific knowledge. In comparison with the logic-based structured modeling language like LSM $[7]$ , the constraint-based environment realizes the application of the embedded knowledge in analysis and guidance. The knowledge embedded in the constraint-based environment can be extended to include the knowledge of utility and solver programs.

## 5. Concluding remarks

In this paper, we have proposed a meta-modeling framework as a way of improving the productivity and quality involved in the development of modeling environments. The proposed constraint-based meta-modeling framework is based on a view that any modeling environment is a constraint enforcement system. It also reflects the view that the explicit specifications of modeling knowledge in the form of constraint will enhance the evolution of modeling environments, i.e., the separation of knowledge and generation mechanism will enhance the maintainability and modifiability of the environments.

Based on the constraint-based modeling framework, a prototype environment generator called MetaDSS is implemented. MetaDSS supports the specification and analysis of knowledge for DSS modeling environments. The knowledge includes the definitional knowledge of the environment and the operational knowledge of the modeling activities within the environment. The knowledge specification is then embedded into logic expressions, where the required functionality is simulated.

The prototype implementation of the constraint-based metaview approach has shown the possibility for achieving the three challenges in the design and implementation of modeling environments, namely, the designing of conceptual modeling frameworks, executable modeling languages, and software integration approaches [20].

The experiences with MetaDSS suggest that the constraint-based environment generation is very efficient and useful in designing modeling environments. Constraint-based metaview to modeling environments are well suited for the specifications of the environment characteristics. Changes to the generated environments are updated quickly by changing the specification of the characteristics. By the virtue of the meta-framework, MetaDSS enhances the modifiability and maintainability of modeling environments. As modeling environments evolve under MetaDSS, existing models need to be transformed into the new environments. Such transformation knowledge [47] can also be defined by the constraint-based modeling framework, which will truly facilitate the evolution of modeling environments.

Since the major concern in the development of MetaDSS is to show the feasibility of generating modeling environments, other important aspects of practical systems are not fully taken into account. The computational efficiency and user interface need improvements for the practical use of MetaDSS. Also, consistent and unified storage for all the knowledge and data gathered is required for which implementation on an object-oriented database management system is being investigated.

## Appendix A

Syntax of the constraint-based modeling language

```toml
spec = [insert | delete][objSpec | relSpec | opSpec | consSpec]';
objSpec = 'object' ('<objName>')
relSpec = [unaryRelSpec | naryRelSpec]
unaryRelSpec = <relName>'('[<objName> | value]')
naryRelSpec = <relName>{ | '('<roleName>=' '[<objName> | value]')'} + value = [{integer} | <real> | <date> | <string> | <file>]
opSpec = <opName>{('roleType' = '<roleName>')'}*
roleType = ['in' | 'out' | 'inout']
consSpec = <consName>[integrityCons | deductionCons |
    modalityCons | permissionCons]
integrityCons = ('("if" = 'relCondSpec'))
    '("then" = "MUST' unitPredication')
deductionCons = ('("if" = 'relCondSpec'))
    '("then" = "DEDUCE' relExistence')
modalityCons = ('("if" = 'condSpec'))
    '("then" = "MUST' opActionSpec')
permissionCons = ('("if" = 'relCondSpec'))
    '("then" = "PERMIT' opActionSpec')
condSpec = [relCondSpec | opCondSpec]
relCondSpec = {unitPredication{'or' unitPredication}*} + unitPredication = relExistence{identifier}*
relExistence = [unaryRelExist | naryRelExist]
unaryRelExist = <relName>'('[<objName> | <varName> | value]')
naryRelExist = <relName>{('<roleName>=' ' 
    [{objName> | <varName> | value]')'} +
```

```txt
identifier = '(id:'[relExistence{identifier}* | cardCons |
    domainCons{'or' domainCons}* |
    varBinding/Comp{'or' varBinding/Comp}]*)'
opCondSpec = opActionSpec{identifier}* 
opActionSpec = [primitiveOpActivation | managerialOpActivation]
primitiveOpActivation = ['insert' | 'delete']relExistence
managerialOpActivation = 'activate' < opName>
{'('roleName>' = '[objName] | <varName> | value]}'* 
cardCons = 'CARD''('<varName>')'' = 'integer'
domainCons = 'DOMAIN''('<varName>')' = '
['INTEGER' | 'REAL' | 'DATE' | 'STRING' | 'FILE']
varBinding/Comp = <varName> comparator criterion
comparator = ['='|'< '']' < = '|'<'|'> = '|'>']
criterion = [<objName> | <varName> | concatenation | value]
concatenation = 'CONCAT''('[<varName> | <constant>]and'
[<varName> | <constant>])'
```

```txt
Legend
= definition of nonterminal token
'...' reserved token
<...> value-bearing token
{...} + one or more iterations of contents limited by the braces
[...] alternative items separated by vertical bars
{...}* zero or more iterations of contents limited by the braces
(...) optional item
```

## Appendix B

## Requirements summary for structured modeling

(1) A genus must belong to one of the six genus types.

(2) No primitive entity genus calls any other genus.

(3) Any genus of type other than primitive entity must call at least one genus.

(4) An attribute, variable attribute, or compound entity genus must call only entity genus.

(5) A function genus can call only (variable) attribute and function genera.

(6) Each test genus must call two other genera, one of which is a function genus or a variable attribute genus.

(7) Each of function and test genera must have one generic rule.

(8) Each of compound entity genera must be indexed by at least one primitive entity genus. Each of attribute, variable attribute, function, and test genera must be indexed by only one entity genus.

(9) Generic structure must be acyclic.

(10) A genus must be contained in a module or a model.

(11) No genus can contain another genus, a module, or a model.

(12) A genus must be associated with a unique value which defines its order in a modular structure.

(13) A module must be contained in another module or a model.

(14) Modular structure must be a rooted tree.

(15) Modular structure must be monotone.

## Appendix C

## Structural constructs of structured modeling

```matlab
Structural objects
object(peGenus); % Primitive Entity Genus %
object(ceGenus); % Compound Entity Genus %
object(aGenus); % Attribute Genus %
object(vaGenus); % Variable Attribute Genus %
object(fGenus); % Function Genus %
object(tGenus); % Test Genus %
object(computationRule); % Generic Rule for fGenus %
object(comparisonRule); % Generic Rule for tGenus %
object(gRange); % Generic Range of aGenus, vaGenus, and fGenus %
object(model); % Root Module %
object(module); % Grouping Unit in Modular Structure %

Structural relationships
% Definitional Dependency %
calls càler = ceGenus)(callee = peGenus);
calls càler = ceGenus)(callee = ceGenus);
calls càler = aGenus)(callee = peGenus);
calls càler = aGenus)(callee = ceGenus);
calls càler = vaGenus)(callee = peGenus);
calls càler = vaGenus)(callee = ceGenus);
calls càler = fGenus)(callee = aGenus);
calls càler = fGenus)(callee = vaGenus);
calls càler = fGenus)(callee = fGenus);
calls càler = tGenus)(callee = aGenus);
calls càler = tGenus)(callee = vaGenus);
calls càler = tGenus)(callee = fGenus);

% Indexing Property %
indexes(genus = ceGenus)(indexer = peGenus);
indexes(genus = aGenus)(indexer = peGenus);
indexes(genus = vaGenus)(indexer = peGenus);
indexes(genus = fGenus)(indexer = peGenus);
indexes(genus = tGenus)(indexer = peGenus);
indexes(genus = aGenus)(indexer = ceGenus);
indexes(genus = vaGenus)(indexer = ceGenus);
indexes(genus = fGenus)(indexer = ceGenus);
indexes(genus = tGenus)(indexer = ceGenus);
indexes(genus = fGenus)(indexer = model);
indexes(genus = tGenus)(indexer = model);

% Generic Rule of fGenus %
computes(function = fGenus)(rule = computationRule);

% Generic Rule of tGenus %
compares(test = tGenus)(rule = comparisonRule);
```

```matlab
% Generic Range of Values %
ranges(attribute = aGenus)(domain = gRange);
ranges(attribute = vaGenus)(domain = gRange);
ranges(attribute = fGenus)(domain = gRange);

% Modular Structure %
contains(container = module)(member = peGenus);
contains(container = module)(member = ceGenus);
contains(container = module)(member = aGenus);
contains(container = module)(member = vaGenus);
contains(container = module)(member = fGenus);
contains(container = module)(member = tGenus);
contains(container = module)(member = module);
contains(container = model)(member = peGenus);
contains(container = model)(member = ceGenus);
contains(container = model)(member = aGenus);
contains(container = model)(member = vaGenus);
contains(container = model)(member = fGenus);
contains(container = model)(member = tGenus);
contains(container = model)(member = module);
```

```matlab
% Order of Genera %
gmOrder(genus = peGenus)(mOrder = order);
gmOrder(genus = ceGenus)(mOrder = order);
gmOrder(genus = aGenus)(mOrder = order);
gmOrder(genus = vaGenus)(mOrder = order);
gmOrder(genus = fGenus)(mOrder = order);
gmOrder(genus = tGenus)(mOrder = order);
```

## Appendix D

## Static constraints of structured modeling

```txt
Requirement (3)
if isTypeOf(type = A)(metaType = X)
  (id: X = ceGenus or X = aGenus or X = vaGenus or X = fGenus or X = tGenus)
then MUST calls càler = A)(callee = B)
  (id: CARD(B) >= 1);

Requirement (6)
if isTypeOf(type = A)(metaType = tGenus)
then MUST calls càler = A)(callee = B)
  (id: CARD(B) = 2);

if isTypeOf(type = A)(metaType = tGenus)
then MUST calls càler = A)(callee = B)
  (id: isTypeOf(type = B)(metaType = X)
    (id: X = fGenus or X = vaGenus))
  (id: CARD(B) >= 1);
```

```verilog
Requirement (7)
if isTypeOf(type = A)(metaType = fGenus)
then MUST computes(function = A)(rule = B)
(id: CARD(B) = 1);

if isTypeOf(type = A)(metaType = tGenus)
then MUST compares(test = A)(rule = B)
(id: CARD(B) = 1);

Requirement (8)
if isTypeOf(type = A)(metaType = ceGenus)
then MUST indexes(genus = A)(indexer = B)
(id: CARD(B) >= 1);

if isTypeOf(type = A)(metaType = X)
(id: X = aGenus or X = vaGenus or X = fGenus or X = tGenus)
then MUST indexes(genus = A)(indexer = B)
(id: CARD(B) = 1);

Requirement (9)
if isTypeOf(type = A)(metaType = X)
(id: X = peGenus or X = ceGenus or X = aGenus or
X = vaGenus or X = fGenus or X = tGenus)
then MUST anyCalls càler = A)(callee = A)
(id: CARD(A) = 0);

if calls càler = A)(callee = B)
then DEDUCE anyCalls càler = A)(callee = B);

if indirectlyCalls càler = A)(callee = B)
then DEDUCE anyCalls càler = A)(callee = B);

if calls càler = A)(callee = B)
(id: isTypeOf(type = A)(metaType = X))
(id: isTypeOf(type = B)(metaType = Y))
(id: calls càler B)(callee = C)
(id: isTypeOf(type = C)(metaType = Z)))
then DEDUCE indirectlyCalls càler = A)(callee = C);

if calls càler = A)(callee = B)
(id: isTypeOf(type = A)(metaType = X))
(id: isTypeOf(type = B)(metaType = Y))
(id: indirectlyCalls càler = B)(callee = C)
(id: isTypeOf(type = C)(metaType = Z)))
then DEDUCE indirectlyCalls càler = A)(callee = C);

Requirement (10)
if isTypeOf(type = A)(metaType = X)
(id: X = peGenus or X = ceGenus or X = aGenus or
X = vaGenus or X = fGenus or X = tGenus)
then MUST contains(container = B)(member = A)
(id: CARD(B) = 1);
```

```verilog
Requirement (12)
if isTypeOf(type = A)(metaType = X)
    (id: X = peGenus or X = ceGenus or X = aGenus or
    X = vaGenus or X = fGenus or X = tGenus)
then MUST gmOrder(genus = A)(mOrder = B)
    (id: DOMAIN(B) = INTEGER);

if isTypeOf(type = A)(metaType = X)
    (id: X = peGenus or X = ceGenus or X = aGenus or
    X = vaGenus or X = fGenus or X = tGenus)
    (id: gmOrder(genus = A)(mOrder = B))
    isTypeOf(type = C)(metaType = Y)
    (id: Y = peGenus or Y = ceGenus or Y = aGenus or
    Y = vaGenus or Y = fGenus or Y = tGenus)
    (id: C<>A)

then MUST gmOrder(genus = C)(mOrder = D)
    (id: D<>B);

Requirement (13)
if isTypeOf(type = A)(metaType = module)
then MUST contains(container = B)(member A)
    (id: CARD(B) = 1);

Requirement (14)
if isTypeOf(type = A)(metaType = module)
then MUST anyContains(container = A)(member = A)
    (id: CARD(A) = 0);

if contains(container = A)(member = B)
then DEDUCE anyContains(container = A)(member = B);

if indirectlyContains(container = A)(member = B)
then DEDUCE anyContains(container = A)(member = B);

if contains(container = A)(member = B)
    (id: isTypeOf(type = B)(metaType = Y))
    (id: contains(container = B)(member = C)
    (id: isTypeOf(type = C)(metaType = Z)))
then DEDUCE indirectlyContains(container = A)(member = C);

if contains(container = A)(member = B)
    (id: isTypeOf(type = B)(metaType = Y))
    (id: indirectlyContains(container = B)(member = C)
    (id: isTypeOf(type = C)(metaType = Z)))
then DEDUCE indirectlyContains(container = A)(member = C);

Requirement (15)
if gmOrder(genus = A)(mOrder = B)
    (id: isTypeOf(type = A)(metaType = X))
    gmOrder(genus = C)(mOrder = D)
    (id: isTypeOf(type = C)(metaType = Y))
    (id: C<>A)
    (id: D > B)

then MUST anyCalls càller = A)(callee = C)
    (id: CARD(A) = 0);
```

## Appendix E

## Transportation model specification

:- insert model(transportation).

:- insert module(m\_plant).

:- insert contains(container,transportation,member,m\_plant).

:- insert module(m\_customer).

:- insert contains(container,transportation,member,m\_customer).

:- insert module(m\_link).

:- insert contains(container,transportation,member,m\_link).

:- insert module(m\_t\_demand).

:- insert contains(container,transportation,member,m\_t\_demand).

:- insert module(m\_t\_supply).

:- insert contains(container,transportation,member,m\_t\_supply).

:- insert peGenus(plant).

:- insert contains(container,m\_plant,member,plant).

:- insert gmOrder(genus,plant,mOrder,1).

:- insert aGenus(supply).

:- insert contains(container,m\_plant,member,supply).

:- insert gmOrder(genus,supply,mOrder,2).

:- insert calls càler,supply,callee,plant).

:- insert indexes(genus,supply,indexer,plant).

:- insert gRange('R +').

:- insert ranges(attribute,supply,domain,'R +').

:- insert peGenus(customer).

:- insert contains(container,m\_customer,member,customer).

:- insert gmOrder(genus,customer,mOrder,3).

:- insert aGenus(demand).

:- insert contains(container,m\_customer,member,demand).

:- insert gmOrder(genus,demand,mOrder,4).

:- insert calls càler,demand,callee,customer).

:- insert indexes(genus,demand,indexer,customer).

:- insert ranges(attribute,demand,domain,'R +').

:- insert ceGenus(link).

:- insert contains(container,m\_link member,link).

:- insert gmOrder(genus,link,mOrder,5).

:- insert calls càller,link,callee,plant).

:- insert calls càller,link,callee,customer).

:- insert indexes(genus,link,indexer,plant).

:- insert indexes(genus,link,indexer,customer).

:- insert aGenus(unitCost).

:- insert contains(container,m\_link,member,unitCost).

:- insert gmOrder(genus,unitCost,mOrder,6).

:- insert calls càller,unitCost,callee,link).

:- insert indexes(genus,unitCost,indexer,link).

:- insert ranges(attribute,unitCost,domain,'R +').

:- insert vaGenus(flow).

:- insert contains(container,m\_link,member,flow).

:- insert gmOrder(genus,flow,mOrder,7).

:- insert calls càller,flow,callee,link).

insert indexes(genus,flow,indexer,link).

insert ranges(attribute,flow,domain,'R +').

insert fGenus(outFlow).

insert contains(container,m\_t\_supply,member,outFlow).

insert gmOrder(genus,outFlow,mOrder,8).

insert computationRule('SUM').

insert computes(function,outFlow,rule,'SUM').

insert calls càler,outFlow,callee,flow).

insert indexes(genus,outFlow,indexer,plant).

insert ranges(attribute,outFlow,domain,'R +').

insert tGenus(t\_supply).

insert comparisonRule('LE').

insert compares(test,t\_supply,rule,'LE').

insert gmOrder(genus,t\_supply,mOrder,9).

insert contains(container,m\_t\_supply,member,t\_supply).

insert calls càller, t \_supply, callee, outFlow).

insert calls càller,t\_supply,callee,supply).

insert indexes(genus,t\_supply,indexer,plant).

insert fGenus(inFlow).

insert contains(container,m\_t\_demand,member,inFlow).

insert gmOrder(genus, inFlow, mOrder, 10).

insert computes(function, inflow, rule, 'SUM').

insert calls càler, inFlow, callee, flow).

insert indexes(genus, inflow, indexer, customer).

insert ranges(attribute,inFlow,domain,'R +').

insert tGenus(t\_demand).

insert comparisonRule('GE').

insert compares(test,t\_demand,rule,'GE').

insert gmOrder(genus,t\_demand,mOrder,11).

insert contains(container,m\_t\_demand,member,t\_demand).

insert calls càller, t\_demand, callee, inFlow).

insert calls càller, t \_demand, callee, demand).

insert indexes(genus,t\_demand,indexer,customer).

insert fGenus(totalCost).

insert contains(container,transportation,member,totalCost).

insert gmOrder(genus,totalCost,mOrder,12).

insert computationRule('DOT').

insert computes(function,totalCost,rule,'DOT').

insert calls càler,totalCost,callee,unitCost).

insert calls càler,totalCost,callee,flow).

insert ranges(attribute,totalCost,domain,'R +').

## Appendix F

Modular structure report for the production model  
Modular outline for a structured model schema: posco

<table><tr><td></td><td>Level 0</td><td>Level 1</td><td>Level 2</td><td>Level 3</td><td>Level 4</td><td>Level 5</td></tr><tr><td>0</td><td>posco</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td>m_product</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td>product</td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td>m_year</td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td></td><td>year</td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td>m_plant</td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td></td><td>plant</td><td></td><td></td><td></td></tr><tr><td>7</td><td></td><td>m_yPlant</td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td></td><td></td><td>m_yPlant1</td><td></td><td></td><td></td></tr><tr><td>9</td><td></td><td></td><td></td><td>yPlant</td><td></td><td></td></tr><tr><td>10</td><td></td><td></td><td></td><td>capa</td><td></td><td></td></tr><tr><td>11</td><td></td><td></td><td></td><td>plType</td><td></td><td></td></tr><tr><td>12</td><td></td><td></td><td></td><td>plVarOO</td><td></td><td></td></tr><tr><td>13</td><td></td><td></td><td></td><td>plVarMat</td><td></td><td></td></tr><tr><td>14</td><td></td><td></td><td></td><td>plRawMat</td><td></td><td></td></tr><tr><td>15</td><td></td><td></td><td></td><td>plExpense</td><td></td><td></td></tr><tr><td>16</td><td></td><td></td><td></td><td>plDepre</td><td></td><td></td></tr><tr><td>17</td><td></td><td></td><td></td><td>plFixOO</td><td></td><td></td></tr><tr><td>18</td><td></td><td></td><td></td><td>plFixMat</td><td></td><td></td></tr><tr><td>19</td><td></td><td></td><td></td><td>plLabor</td><td></td><td></td></tr><tr><td>20</td><td></td><td></td><td></td><td>plVarCost</td><td></td><td></td></tr><tr><td>21</td><td></td><td></td><td></td><td>plFixCost</td><td></td><td></td></tr><tr><td>22</td><td></td><td>m_yProd</td><td></td><td></td><td></td><td></td></tr><tr><td>23</td><td></td><td></td><td>m_yProd1</td><td></td><td></td><td></td></tr><tr><td>24</td><td></td><td></td><td></td><td>yProd</td><td></td><td></td></tr><tr><td>25</td><td></td><td></td><td></td><td>prType</td><td></td><td></td></tr><tr><td>26</td><td></td><td></td><td></td><td>price</td><td></td><td></td></tr><tr><td>27</td><td></td><td></td><td></td><td>maxDem</td><td></td><td></td></tr><tr><td>28</td><td></td><td></td><td></td><td>prExpense</td><td></td><td></td></tr><tr><td>29</td><td></td><td></td><td></td><td>prDepre</td><td></td><td></td></tr><tr><td>30</td><td></td><td></td><td></td><td>prFixOO</td><td></td><td></td></tr><tr><td>31</td><td></td><td></td><td></td><td>prVarOO</td><td></td><td></td></tr><tr><td>32</td><td></td><td></td><td></td><td>prFixMat</td><td></td><td></td></tr><tr><td>33</td><td></td><td></td><td></td><td>prVarMat</td><td></td><td></td></tr><tr><td>34</td><td></td><td></td><td></td><td>prRawMat</td><td></td><td></td></tr><tr><td>35</td><td></td><td></td><td></td><td>prLabor</td><td></td><td></td></tr><tr><td>36</td><td></td><td></td><td></td><td>unitCost</td><td></td><td></td></tr><tr><td>37</td><td></td><td>m_ip</td><td></td><td></td><td></td><td></td></tr><tr><td>38</td><td></td><td></td><td>m_ip1</td><td></td><td></td><td></td></tr><tr><td>39</td><td></td><td></td><td></td><td>ip</td><td></td><td></td></tr><tr><td>40</td><td></td><td>m_po</td><td></td><td></td><td></td><td></td></tr><tr><td>41</td><td></td><td></td><td>po</td><td></td><td></td><td></td></tr><tr><td>42</td><td></td><td>m_ipo</td><td></td><td></td><td></td><td></td></tr><tr><td>43</td><td></td><td></td><td>m_ipo1</td><td></td><td></td><td></td></tr><tr><td>44</td><td></td><td></td><td></td><td>ipo</td><td></td><td></td></tr><tr><td>45</td><td></td><td></td><td></td><td>t/h</td><td></td><td></td></tr><tr><td>46</td><td></td><td></td><td></td><td>yr</td><td></td><td></td></tr><tr><td>47</td><td></td><td></td><td></td><td>h/t</td><td></td><td></td></tr><tr><td>48</td><td></td><td></td><td></td><td>1/yr</td><td></td><td></td></tr><tr><td>49</td><td></td><td>m_unitFlow</td><td></td><td></td><td></td><td></td></tr><tr><td>50</td><td></td><td></td><td>unitFlow</td><td></td><td></td><td></td></tr><tr><td>51</td><td></td><td></td><td>qty</td><td></td><td></td><td></td></tr><tr><td>52</td><td></td><td>m_yPlant</td><td></td><td></td><td></td><td></td></tr><tr><td>53</td><td></td><td></td><td>m_yPlant2</td><td></td><td></td><td></td></tr><tr><td>54</td><td></td><td></td><td></td><td>usedCapa</td><td></td><td></td></tr><tr><td>55</td><td></td><td></td><td></td><td>capaCons</td><td></td><td></td></tr><tr><td>56</td><td></td><td>m_ipo</td><td></td><td></td><td></td><td></td></tr><tr><td>57</td><td></td><td></td><td>m_ipo2</td><td></td><td></td><td></td></tr><tr><td>58</td><td></td><td></td><td></td><td>ipoQty</td><td></td><td></td></tr><tr><td>59</td><td></td><td>m_ip</td><td></td><td></td><td></td><td></td></tr><tr><td>60</td><td></td><td></td><td>m_ip2</td><td></td><td></td><td></td></tr><tr><td>61</td><td></td><td></td><td></td><td>inputQty</td><td></td><td></td></tr><tr><td>62</td><td></td><td></td><td></td><td>outputQty</td><td></td><td></td></tr><tr><td>63</td><td></td><td></td><td></td><td>prBalance</td><td></td><td></td></tr><tr><td>64</td><td></td><td>m_yProd</td><td></td><td></td><td></td><td></td></tr><tr><td>65</td><td></td><td></td><td>m_yProd2</td><td></td><td></td><td></td></tr><tr><td>66</td><td></td><td></td><td></td><td>prQty</td><td></td><td></td></tr><tr><td>67</td><td></td><td></td><td></td><td>demCons</td><td></td><td></td></tr><tr><td>68</td><td></td><td>totalProdCost</td><td></td><td></td><td></td><td></td></tr><tr><td>69</td><td></td><td>sales</td><td></td><td></td><td></td><td></td></tr><tr><td>70</td><td></td><td>fixCost</td><td></td><td></td><td></td><td></td></tr><tr><td>71</td><td></td><td>varCost</td><td></td><td></td><td></td><td></td></tr><tr><td>72</td><td></td><td>totalPlantCost</td><td></td><td></td><td></td><td></td></tr><tr><td>73</td><td></td><td>-varCost</td><td></td><td></td><td></td><td></td></tr><tr><td>74</td><td></td><td>contributionMargin</td><td></td><td></td><td></td><td></td></tr><tr><td>75</td><td></td><td>costBalance</td><td></td><td></td><td></td><td></td></tr></table>

## References

[1] T. Amble, Logic Programming and Knowledge Engineering (Addison-Wesley, Wokingham, 1987).

[2] H.K. Bhargava, and S.O. Kimbrough, On Embedded Languages for Model Management, Proceedings of the Twenty-Third Hawaii International Conference on System Sciences (1990).

[3] M. Binbasioglu, and M. Jarke, Domain Specific DSS Tools for Knowledge-based Model Building, Decision Support Systems 2, (1986) 213–223.

[4] R. Bonczek, C. Holsapple, and A. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management, Operations Research 29, (1981) 263–281.

[5] M.L. Brodie, On the Development of Data Models, in: On Conceptual Modeling: Perspectives from Artificial Intelligence, Databases, and Programming Languages (Springer-Verlag, New York, NY, 1984) 19–47.

[6] A. Brooke, D. Kendrick, and A. Meeraus, GAMS: A User's Guide (The Scientific Press, Redwood City, CA, 1988).

[7] S. Chari, and R. Krishnan, Towards a Logical Reconstruction of Structured Modeling, Proceedings of the Twenty-Third Hawaii International Conference on System Sciences (1990).

[8] M. Chen, J.F. Nunamaker, Jr. and E.S. Weber, The Use of Integrated Organization and Information Systems Models in Building and Delivering Business Application Systems, IEEE Transactions on Knowledge and Data Engineering 1 No. 3 (1989) 406–409.

[9] C. Ching, R.G. Ramirez and R.D. St. Louis, Model-Data and Model-Solver Mappings: A Basis of Implementing an Extended DSS Framework, Proceedings of the 1990 International Society for Decision Support Systems Conference (1990) 283–312.

[10] R. Davis, and B.G. Buchanan, Meta-Level Knowledge:

Overview and Applications, Proceedings of the Fifth International Joint Conference on Artificial Intelligence (1977).

[11] G. DeSanctis, and R.B. Gallupe, A Foundation for the Study of Group Decision Support Systems, Management Science 33, No. 5 (1987) 589–609.

[12] F. Dignum, T. Kemme, W. Kreuzen, H. Weigand, and R.P. van de Riet, Constraint Modeling Using a Conceptual Prototyping Language, Data & Knowledge Engineering 2, No. 3 (1987) 213–254.

[13] D.R. Dolk, Model Management and Structured Modeling: The Role of an Information Resource Dictionary System, Communications of the ACM 31, No. 6 (1988) 704–718.

[14] D.R. Dolk, and B.R. Konsynski, Knowledge Representation for Model Management Systems, IEEE Transactions on Software Engineering 10, No. 6 (1984) 619–628.

[15] A. Dutta, and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer 17, No. 9 (1984) 89–97.

[16] R.D. Eck, A. Philippakis and R. Ramirez, Solver Representation for Model Management Systems, Proceedings of the Twenty-Third Hawaii International Conference on System Sciences (1990)

[17] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (1987) 547–588.

[18] A.M. Geoffrion, Integrated Modeling Systems, Working paper no. 343 (Western Management Science Institute, University of California, Los Angeles, CA, November 1988).

[19] A.M. Geoffrion, The Formal Aspects of Structured Modeling, Operations Research 37, No. 1 (1989a) pp. 30–51.

[20] A.M. Geoffrion, Computer-based Modeling Environments, European Journal of Operational Research 41, No. 1 (1989b) pp. 33–43.

[21] A.M. Geoffrion, FW/SM: A Prototype Structured Modeling Environment, Working paper no. 377 (Western Management Science Institute, University of California, Los Angeles, CA, May 1990).

[22] L. Henschen, Reasoning, in: S.C. Shapiro and D. Eckroth, eds., Encyclopedia of Artificial Intelligence, Vol. 2 (Wiley, New York, 1987) 822–827.

[23] S. Hong, and F. Maryanski, Using a Meta Model to Represent Object-oriented Data Models, Proceedings of the Sixth International Conference on Data Engineering (1990) 11–19.

[24] M.T. Jelassi, K. Williams and C.S. Fidler, The Emerging Role of DSS: From Passive to Active, Decision Support Systems 3 (1987) 299–307.

[25] G.E. Kaiser, P.H. Feiler, and S.S. Popovich, Intelligent Assistance for Software Development and Maintenance, IEEE Software 5 (1988) 40–49.

[26] H.D. Kim, and S.J. Park, An Object-Oriented Modeling Environment Based on Structured Modeling, Proceedings of the Korea Management Information System Conference (1991a) 95–104.

[27] H.D. Kim, and S.J. Park, Model Formulation Support in an Object-Oriented Structured Modeling Environment, Working paper (Department of Management Science, Korea Advanced Institute of Science and Technology, Seoul, 1991b).

[28] S.O. Kimbrough, and R.M. Lee, Logic Modeling: A Tool for Management Science, Decision Support Systems 4, No. 1 (1988) 3–16.

[29] R. Krishnan, A Logic Modeling Language for Automated Model Construction, Decision Support Systems 6, No. 2 (1990) 123–152.

[30] A. Lamsweerde, M. Buyse, B. Delcourt, M. Delor, M. Ervier, and M.C. Schayes, The Kernel of a Generic Software Development Environment, ACM SIGSOFT/SIGPLAN (1986) 208–217.

[31] M.L. Lenard, Representing Models as Data, Journal of Management Information Systems 2, No. 4 (1986) 36–48.

[32] P. Loucopoulos, and P.J. Layzell, Improving Information System Development and Evolution Using a Rule-based Paradigm, Software Engineering Journal (September 1989) 259–267.

[33] M. Lowry, and R. Duran, Knowledge-based Software Engineering, in: A. Barr, P.R. Cohen and E.A. Feigenbaum, eds., The Handbook of Artificial Intelligence, Vol. 4, (Addison-Wesley, Mass., 1989).

[34] L. Mark, and N. Roussopoulos, Metadata Management, IEEE Computer 19, No. 12 (1986) 26–36.

[35] R.P. Minch, Logic Programming as a Paradigm for Financial Modeling, MIS Quarterly (1989) 65–84.

[36] R. Neches, W.R. Swartout, and J.D. Moore, Enhanced Maintenance and Explanation of Expert Systems through Explicit Models of Their Development, IEEE Transactions on Software Engineering 11, No. 11 (1985) 1337-1351.

[37] L. Neustadter, A.M. Geoffrion, S. Maturana, Y. Tsai and F. Vicuna, The Design and Implementation of a Prototype Structured Modeling Environment, Working paper no. 380, (Western Management Science Institute, University of California, Los Angeles, CA, November 1990).

[38] G.M. Nijssen, and T.A. Halpin, Conceptual Schema and Relational Database Design (Prentice Hall of Australia Pty Ltd., Sydney, 1989).

[39] M.P. Papazoglou, P.O. Bobbie and C. Hoffmann, Active Information Systems in Support of Decision Making, in Proceedings of the Twenty-Fourth Hawaii International Conference on System Sciences (1991).

[40] S.J. Park, H.D. Kim and G.J. Kim, K-Meta System: A Meta System for Software Development Environments, Proceedings of the Korea Information Science Society Conference (1991) 361–364.

[41] W.D. Potter, R.P. Trueblood, and C.M. Eastman, Hyper-semantic Data Modeling, Data & Knowledge Engineering 4, No. 1 (1989) 69–90.

[42] W.R. Rosenblatt, J.C. Wileden, and A.L. Wolf, OROS: Toward a Type Model for Software Development Environments, Proceedings of OOPSLA '89 Conference (1989) 297–304.

[43] P.C. Scott, Requirements Analysis by Logic Modeling, Decision Support Systems 4, No. 1 (1988) 17–25.

[44] P.G. Sorenson, J.-P. Tremblay, and A.J. McAllister, The Metaview System for Many Specification Environments, IEEE Software 5, No. 2 (1988) 30–38.

[45] D. Teichroew, P. Macasovic, E.A. Hershey III, and Y. Yamamoto, Application of the Entity-Relationship Approach to Information Processing Systems Modeling, in: P.P. Chen, ed., Entity-Relationship Approach to Systems Analysis and Design 1980. (North-Holland, Amsterdam).

[46] L. Tung, R.G. Ramirez, and R.D. St. Louis, Model Integration in an Object-Oriented Model Management System, Proceedings of the Twenty Fourth Hawaii International Conference on System Sciences (1991).

[47] S. Twine, Mapping between a NIAM Conceptual Schema and KEE Frames, Data & Knowledge Engineering 4, No. 2 (1989) 125–155.

[48] X. Zhang, A. Umar and D. Teichroew, A Verifier for Semantic Completeness and Consistency of Software Specification, Proceedings of CASE Studies 1987 (1987).
