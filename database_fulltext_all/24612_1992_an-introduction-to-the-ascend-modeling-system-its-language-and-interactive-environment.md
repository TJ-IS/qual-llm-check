---
otero_id: 24612
otero_key: "D75JQZGD"
title: "An Introduction to the ASCEND Modeling System: Its Language and Interactive Environment"
authors: "Peter Piela; Roy McKelvey; Arthur Westerberg"
year: "1992"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1992.11517969"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Introduction to the ASCEND Modeling System: Its Language and Interactive Environment

Peter Piela, Roy McKelvey & Arthur Westerberg

To cite this article: Peter Piela, Roy McKelvey & Arthur Westerberg (1992) An Introduction to the ASCEND Modeling System: Its Language and Interactive Environment, Journal of Management Information Systems, 9:3, 91-121, DOI: 10.1080/07421222.1992.11517969

To link to this article: https://doi.org/10.1080/07421222.1992.11517969

![](/api/attachments/D75JQZGD/fulltext/images/c0a725d811b419bf51d74c24b3f6a03f653af73b645ad56dec1770919efd7bc2.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/D75JQZGD/fulltext/images/88f567d9033ee762496c762c10e551bf70851509c49ef23a6351d2cc0c7f811b.jpg)

Submit your article to this journal ↗

![](/api/attachments/D75JQZGD/fulltext/images/1661686e8fe7eedb0332b31a98b59ecbf4121cc3d5a196ac13c365d5ccdf1d8b.jpg)

Citing articles: 8 View citing articles ↗

# An Introduction to the ASCEND Modeling System: Its Language and Interactive Environment

PETER PIELA, ROY MCKELVEY, AND ARTHUR WESTERBERG

PETER PIELA received his B.Sc. in chemical engineering from Imperial College of Science and Technology in 1979, and his Ph.D. from Carnegie Mellon University in chemical engineering in 1989. He has worked in the chemical industry for six years in the areas of process design and scientific computing. He currently holds the position of research faculty at the Engineering Design Research Center at Carnegie Mellon. His two major areas of research are computer environments for supporting people in the building and solving of equational models, and methodologies for involving users in the design and evaluation of computing systems.

ROY MCKELVEY is an Associate Professor of Design at Carnegie Mellon University. His research interests include many aspects of the design of human-computer interfaces: the visual communication issues of screen layout and sequencing information; user testing and observational evaluation of interfaces and interactive systems; and the design of user interfaces in the context of a basic research environment. These issues are the focus of Professor McKelvey's work with the ASCEND system at Carnegie Mellon's Engineering Design Research Center. Professor McKelvey's primary teaching responsibility involves the integration of computers and other advanced technologies in the graphic and industrial design process. He also teaches typography in the graphic design program.

ARTHUR W. WESTERBERG is currently the Swearingen University Professor of Chemical Engineering at Carnegie Mellon University. After receiving degrees at Minnesota, Princeton, and Imperial College (London), he worked for two years at Control Data, and nine years at the University of Florida before coming to Carnegie Mellon in 1976. He has served as Chemical Engineering Department Head, Director of the Design Research Center, and founding Director of the Engineering Design Research Center (an NSF-sponsored Engineering Research Center). He is a member of the National Academy of Engineering and recipient of several awards from AIChE and ASEE. His research interests are in engineering design, particularly in analysis, optimization, design synthesis, and computer environments.

ABSTRACT: Recently there has been a growing realization among researchers and practitioners that current technologies do not adequately support mathematical modeling “in the large.” In this paper we discuss a technology called ASCEND (Advanced

Acknowledgment: An earlier version of this paper was originally published in the Proceedings of the Twenty-Fifth Hawaii International Conference on System Sciences (IEEE Computer Society Press, 1992).

System for Computations in Engineering Design), which addresses this issue. We describe two aspects of the technology: a modeling language and an interactive model-building environment. The ASCEND language is structured, declarative, and strongly typed, and incorporates object-oriented extensions. The interactive environment is based on the notion of a concurrent set of tools that reflect the various phases of ASCEND modeling. These tools do not enforce a strict sequence of operations, but rather have been designed to support the flexible access implied by declaratively specified models. We claim that ASCEND offers solutions to several of the issues raised by Arthur Geoffrion in his article, “Computer-based modeling environments,” [21] and use categories introduced by him to frame this discussion.

KEY WORDS AND PHRASES: equation-oriented simulation, mathematical modeling, participatory design, structured modeling, user-centered design.

## 1. Introduction

IN A PAPER SUMMARIZING PLENARY ADDRESSES GIVEN AT THE IFORS '87 conference in Buenos Aires and the 1988 Canadian Operations Research Society Meeting, Arthur Geoffrion [21] addresses the shortcomings of current computer-based modeling environments. As an impetus to correcting these shortcomings, he proposes five characteristics that should be found in any system attempting to support the full spectrum of modeling activity. He then steps back from these characteristics and discusses the three main design challenges that stand in the way of realizing such systems. In his concluding remarks, he calls for the reader to consider these issues in light of their modeling environments and to begin work on closing the gaps between his admittedly ideal system and their own.

In this paper, we take up this challenge. We are particularly motivated by the fact that the system we are developing—an equational modeling environment called ASCEND—already possesses many of Geoffrion’s required features and seems a promising platform in which to address many of the others. Our aim is to discuss the ASCEND system—its modeling language and interactive environment—within the Geoffrion framework, and when appropriate, discuss how the ASCEND paradigm suggests alternative approaches to modeling systems. Further, we hope that the reader, after reading the paper, will have a good sense of the current ASCEND implementation and its use.

This paper is organized as follows: section 2 outlines the scope of the ASCEND project. Section 3 describes the dominant themes of the ASCEND approach; section 4 describes the ASCEND language in detail. Section 5 analyzes the language with respect to Geoffrion's points; sections 6 and 7 similarly discuss the details of the interactive ASCEND environment and their relation to Geoffrion's ideal.

## 2. Scope of the Project

IN "COMPUTER-AIDED MODEL CONSTRUCTION," Bhargava and Krishnan [2] suggest that model construction and solution can be thought of as a state transformation process that proceeds from an informal problem statement through the definition of a formal mathematical model to a phase of solving and debugging. At present, the scope of our work has been restricted to the later stages of modeling, specifically to the iterative process of defining a formal mathematical model, attempting to solve it, and if necessary debugging solution failure. Although limited in scope, we believe our work ideally complements existing efforts that are focused on supporting the process of turning an informal problem statement into a formal mathematical model, examples of which can be found in $[3, 31, 35, 40, 46]$ .

We support multiple disciplines (e.g., engineering, operations research, architecture) and multiple problem types (e.g., linear/nonlinear optimization, and differential equations). In contrast to this work, which exploits domain-specific knowledge to support people's decision making, our work has focused on the development of analyses that can be applied to many classes of mathematical problems. In this sense, our work is similar to Greenberg's work on ANALYZE [25]. However, we are concerned with both linear and nonlinear problems. A detailed discussion of the analyses available to the user of ASCEND is beyond the scope of the paper; examples, however, include: structurally based algorithms for aiding the user in correctly selecting and trading degrees of freedom; the computation of redundant relations as a part of diagnosing numerical singularity; and finding variables that are not incident in any relation.

## 3. The ASCEND Approach

IN COOPERATION WITH A GROUP OF ACADEMICS AND INDUSTRIALISTS we have developed a model description language and a computer system through which users can create and interact with models defined in the language. These tools form the basis of an experimental program in which observation of users solving problems and subsequent discussions are used to refine and evaluate the underlying technology. The stated goal for the ASCEND project is to create an environment in which engineers are able to produce complex equational models involving thousands of equations much more rapidly than possible with existing technology. The ASCEND system reflects certain hypotheses about how best to support large-scale mathematical modeling. These we will discuss in some detail.

## 3.1. Models Should Be Highly Structured

ASCEND is a structured approach to developing and solving equational models. By a structured approach we mean that the user is able to define groupings of equations and variables called models, and to manipulate these models using a set of language-defined operators.

Today a majority of equational modeling is done with unstructured languages such as GAMS [8], AMPL [17], and LPL [28] which are based on algebraic notation. Although the use of these languages has led to significant improvements in productivity, we believe that their lack of a model management capability significantly limits the complexity of task that can practically be attempted. This view is shared by Muhanna and Pick [39] who write:

Present modeling tools do not support combining of models. This is a serious deficiency. By using existing models as “building blocks” for new composite models, the new model is developed with less effort than would be necessary if it were built from scratch. Furthermore, this enables a kind of “structured” model building in that small models may be independently built and debugged and then used as components in larger models. Traditionally models are developed (often from scratch) as stand-alone entities. As a result, model integration through direct model-to-model linkage is tedious and error-prone.

In the following sections we further support the need for a structured approach to mathematical modeling by giving a brief overview of three themes that we consider to be particularly important in the development of complex models. They are: hierarchical decomposition, evolutionary modeling, and debugging. In each, the model builder must be able to manipulate individual parts of a model structure.

## Hierarchical Decomposition

Our experience [43] and that of other workers in a number of disciplines [7, 39, 47, 51] suggest a need to support the building of hierarchically organized networks of equations. In chemical engineering, Westerberg and Benjamin [53] write: "Complex models are almost always built in a hierarchical fashion. An example is a distillation column which is built up of trays, flash units, splitters, mixers, heat exchangers, pumps etc. A flash unit is in fact a hierarchical structure." In their work on synthesis of electric circuits, Sussman and Steele [50] propose a language for describing hierarchical constraint networks in which compound models are defined in terms of existing parts. They write: "In this way we can build arbitrarily complicated compound objects in a hierarchical manner. The hierarchy allows the complexity at one level to be limited." In operations research, Geoffrion [22] demonstrates that a transhipment model can be hierarchically decomposed into two transportation models with a set of constraints that define resource limitations for the warehouses. Also, Muhanna and Pick [39] contend that an effective model management system must provide support for modular and hierarchical model development, and demonstrate a strategy for accomplishing this in their model development language MDL [38].

## Evolutionary Modeling

The batch-oriented nature of systems like GAMS [8] encourages users to try to solve a large problem in one attempt. However, Locke and Westerberg [37] write that “these large attempts fail more often than not,” and suggest that “a more efficient approach is to solve the large problem in stages, beginning with a few pieces of equipment and working up to a complete flowsheet.” $^{1}$

Another type of evolution occurs when a model builder first describes his or her problem in terms of simplified models that are robust and converge quickly. Based on these calculations, the model builder selectively specializes certain models to more rigorous representations, and re-solves the problem with the values generated by the simplified models as initial guesses. Locke and Westerberg [37] associate this style of modeling with movement along an axis of “model complexity.”

Modeling can also involve moving along an axis of “computational control” [37]. For example, a chemical engineer might initialize the flowsheet shown in figure 1 by guessing the recycle stream (S4), and separately solve the units MIX, REACT, and STILL in a sequence such that the outputs from one unit become the inputs to the next. The engineer can then alter the degrees of freedom (i.e., which variables are specified, and which are computed), and solve the entire flowsheet simultaneously.

## Debugging

Although Muhanna refers to the benefits of developing independently debugged models, model instances also need to be debugged during solving. In such situations we have found it helpful to be able to pick a troublesome part and work on it (e.g., rescale variables and equations) in isolation. This kind of debugging often involves working with a sequence of parts as the problem is traced back to its cause. Having corrected the problem, the model builder can then attempt to solve the complete instance structure.

## 3.2. Simulation is Best Represented as a System of Constraints

At present, most simulation in engineering design is done with parametric systems. In these systems, equations are specified and ordered for procedural computation. Although this approach is useful for routine problems that have established solution procedures and do not change frequently, nonroutine problems require the model builder to rewrite and reorder the model equations.

In response to the need for more flexible systems, there has been a growing interest in declarative equation-based techniques. Problem solving with equational models involves specifying the values of certain variables and computing the others with an independent solver. An important feature of this approach is that it allows users to examine different scenarios with one model structure by simply changing which variables are specified, and which are computed.

For example, in chemical engineering process simulation there are two major types of calculation: simulation and design. Simulation is considered the easier of the two calculations and requires the user to specify all input streams and equipment parameters (e.g., size). The solver will then compute the remaining intermediate and output streams. A design calculation is more or less the inverse; the user specifies variables in the output streams, and the solver computes either equipment parameters or input streams.

The design calculation is difficult for a number of reasons including the possibility of making a specification on an output stream that is physically impossible to achieve. Locke and Westerberg [37] suggest that the correct way to approach a design problem is to start out with a sequence of simulation calculations that generate converged solutions approaching the desired solution, and then to switch to the design calculation by altering which variables are fixed, and which are computed.

![](/api/attachments/D75JQZGD/fulltext/images/5357761ab3b10939d95802c64348f03e514526179b2fef49ceb04cda734c9761.jpg)  
Figure 1. A Simple Flowsheet with a Recycle Stream

## 4. The ASCEND Language

IN THIS SECTION WE WILL FIRST DISCUSS THE LANGUAGE in terms of related work and then give a brief introduction to the language itself.

## 4.1. Related Work

We consider model reuse via integration of model schemas to be the principal issue addressed by the ASCEND modeling language, and will use this theme to position our work in relation to the existing literature. By model integration we mean the linking of models to build composite models, and the structural transformation of existing models to yield new models better suited to specific tasks. Model integration has been addressed by a number of researchers including ourselves $[32]$ ; what follows is a selective summary of work done to date.

Several researchers have developed approaches to model integration that are based on existing theories of data management. For example, Elam employed the entity-relationship approach $[13, 14, 15]$ , Blanning adopted the relational approach $[5, 6]$ , and Konsynski and Dolk used the CODASYL approach $[11, 30]$ . In the case of Blanning's work, for example, a model is treated as a properly restricted subset of the Cartesian product of its inputs and outputs. A collection of models is then viewed as a set of virtual relations with input and output attributes. Model integration occurs in response to a user query requiring the value of an output variable from a model whose inputs are computed by another model. Integration is implemented by appropriately “joining” input and output attributes $[6]$ . Although this approach has a sound theoretical basis, it has been criticized on a number of fronts $[29, 34, 39]$ . For examples, the mathematical structure of a model is not explicitly represented, which is particularly problematic for models that contain nonlinear relationships; and the basic classification of a declaratively specified algebraic model in terms of inputs and outputs goes against the grain of equational modeling. One of the advantages of a declarative approach cited frequently in engineering design $[36]$ is that both simulation (computing with the direction of material flow) and design (computing against the direction of physical flow) can be accomplished with a single formulation. An example of the need to switch rapidly between simulation and design computations is given in section 3.3.

The problem of not explicitly representing the mathematical structure of a model was addressed in the design of algebraic languages like GAMS [8], AMPL [17], and LPL [28]. These languages were constructed to replace matrix generators, and allow a model builder to specify his or her model in a syntax similar to algebraic notation. However, to date, model integration has not been explicitly addressed in the design of these languages, and Fourier remarks that “for the language [AMPL] to be useful, it must be incorporated into a system that manages data, models, and solution” [17].

Recognizing the need for an approach to modeling that captures both the semantic and the mathematical structure of a model, Geoffrion has proposed a framework named Structured Modeling $[20]$ which has been realized in the modeling language SML $[23, 24]$ . In this framework, a model or class of models is represented as a hierarchically organized, partitioned, and attributed acyclic graph. Although SML provides a powerful formalism for defining individual model schema (a class of models), we are still left with the issue of how to combine multiple schemas in the construction of larger systems. In “Reusing structured models via model integration,” Geoffrion $[22]$ mentions the possibility of a language for integrating schemas or even fully specified models; however, he reports that no such language currently exists and proposes a five-step procedure for manually integrating schemas written in SML. Although parts of this procedure are amenable to automation, the model builder is expected to edit copies of existing definitions and deal with issues such as name conflicts.

One language proposed by Muhanna and Pick [39] provides some of the model integration capabilities Geoffrion calls for. Their method involves defining a “model-type” that comprises a list of ports that are labeled either input or output. A port can denote a single algebraic variable or an array of variables. Input ports represent exogenously specified information whereas output ports contain variables computed by the model. The mappings between input ports and output ports are provided by linking ports to algebraic variables in model schemas that are defined using the Model Description Language (MDL). Model types are managed and organized using an object system, and composite models are constructed by instantiating model types and connecting them by equivalencing input and output ports. Hierarchical construction is achieved by repeatedly nesting instances of models as components in higher-level models.

Our work has much in common with that of Muhanna and Pick. Basically, we view the definition and integration of models as similar to the definition and manipulation of records in a strongly typed programming language such as Pascal or Modula. In ASCEND, a type (which for practical purposes can be thought of as a model or class of models) is a template for data that describes a number of slots, each of which has a name. A slot can denote an instance of a type (which we term a “part”), denote an array of instances, or define a mathematical relationship among parts. Our decision to make ASCEND a strongly typed language manifests itself in the fact that a slot is itself typed. That is, it is declared to denote an instance of a specified type (the basetype of the slot), or an instance of a type that specializes the basetype. By organizing types in inheritance hierarchies, and by imposing the constraints that inheritance be monotonic (in an additive sense) and that a type can only inherit from a single parent, we are guaranteeing that any type that either directly or transitively inherits from another is a valid substitute for it [45]. In addition to the declaration of slots, type definitions include constraints that determine both the actual instance and the type of instance that a slot denotes. These constraints are specified with the aid of a set of operators described below. The feasibility of these constraints is checked by a compiler during model compilation.

As stated above, the ASCEND language has much in common with MDL; here is an enumeration of some of the commonalities and some of the differences.

In MDL a model type specifies the input–output structure of a model and a “model version” specifies the model’s internal structure. This distinction does not exist in the ASCEND modeling language where the entire structure of a model defines its interface to the user.

In MDL a model type consists of a list of input ports and a list of output ports, a port denoting an algebraic variable or an array of variables. In ASCEND we do not distinguish between input and output variables as a part of model declaration. The reasons for this are given earlier in this section.

In MDL composite models are constructed by connecting the output ports of one model with the input ports of another. In ASCEND models are connected by equivalencing parts of one model with parts of another (described in section 4.2.9). A valid connection requires the parts to be type-compatible.

Both MDL and ASCEND support hierarchical construction by repeatedly nesting models in the construction of higher-level models.

## 4.2. An Overview of the ASCEND Language

What follows is a brief overview of what we consider to be the most important attributes of the ASCEND language, and how they relate to issues raised in the previous section. More detailed descriptions of the language can be found in $[43, 45, 56]$ , and discussions of formal properties of the language can be found in $[33, 43]$ .

ASCEND was originally designed to support the declarative and structured specification of large systems of equations that arise in engineering design; however, it has applicability to disciplines outside engineering. The domain of problems that can be expressed with the ASCEND language include: linear and nonlinear optimization (with integer variables), ordinary differential equations (both initial value and two point boundary problems), partial differential equations, and differential-algebraic systems. Examples of ASCEND modeling can be found in $[9, 43, 48, 56, 57]$ .

The language builds on concepts used in object-oriented programming and conventional strongly typed languages such as Pascal. We will discuss the ASCEND language using the benchmark examples of Geoffrion [22] which include the transportation and forecasting models. (Model definitions can be found in appendices A, B, and C.) Note that the structuring concepts and set of operators contained in the language are sufficient to define a set of basic schema (e.g., transportation and forecast) and perform the integrations posed in the paper without requiring manual alteration to the basic schemas [32].

## 4.2.1. Atoms and Models

There are two types of structured objects that can be defined in the ASCEND language: ATOMs and MODELs. Both atoms and models can optionally contain declarative and procedural information; however, these are separated in clearly defined sections of the model.

The declarative section of an atom contains some number of slots that are constrained to denote objects that are of elementary type (real, integer, boolean, symbol). In addition to user-defined slots, all atoms have an implicitly defined slot that holds the value of the atom. By convention, the name of an atomic object is synonymous with its value slot; for example, if x, y, and z denote atomic objects, then the relation $x = y + z$ can be thought of as being equivalent to x.value = y.value + z.value. The example atom declaration shows an optional declaration of dimensionality and default value:

## ATOM flow REFINES solver\_var DIMENSION M/T

DEFAULT 1000{tonne/year};

nominal := 1000{tonne/year};

END flow;

The declarative section of a model contains some number of slots that denote either instances of atoms, instances of other models, arrays, or mathematical relations. Because of the way models are structured, the user can decompose large problems into smaller parts that can themselves be represented as models. For example, the transportation model (shown below) is composed of a set of plants (p[plantId]), and a set of customers (c[customerId]). Each plant is itself a model containing product flows (f[customerId]) to a set of customers (customerId).

MODEL plant;

sup IS\_A supply\_capacity;

customerId IS\_A set OF integer;

maxCustomer IS\_A integer;

CARD(customerId) <= maxCustomer;

f[customerId], totalFlow IS\_A flow;

cost[customerId] IS\_A unitCost;

totalFlow = SUM(f[customerId]);

totalFlow <= sup;

```txt
shipmentCost IS_A cost;
shipmentCost = SUM(f[i]*cost[i] | i IN customerId);
```

END plant;

END transportation;

## 4.2.2. Information Hiding and Qualified Naming

There is no information hiding in ASCEND. One can gain access to any part of any model using qualified names (paths). For example, in the transportation model shown above, the total cost of shipping product from plant i is accessed using the name p[i].shipmentCost. Note that qualified naming eliminates the problem of ambiguous references which may result from name clashes within two separately defined components. However, it does not completely address the broader (semantic) issue of unique name violations that need to be resolved during model integration [1].

## 4.2.3. Physical Dimensions and Measurement Units

Every numeric value in an ASCEND model has an associated dimensionality that is implied by (1) a type definition (e.g., from the atom definition given in section 4.2.1, f IS\_A flow implies that f has dimensionality mass/time); (2) a units specification (e.g., f := 500{tonne/year}, 55{mile/hour}); or (3) propagation of dimensionality through relations.

Once the dimensionality of a variable is known, its value may be assigned or displayed in any set of compatible units (for example, $f := 20 \{kg/hour\}$ ).

In addition, the user can define his or her own measurement units in terms of the fundamental units associated with each dimension, or any previously defined derived units. For example,

```txt
UNITS
g := kg/1000;
lb := kg/2.20462;
N := kg*m/s^2;
J := N*m;
END;
```

One of the major benefits of explicitly handling dimensionality and measurement units in the modeling language is that the compiler can ensure that all mathematical relations are dimensionally consistent.

## 4.2.4. Arrays

Arrays of variables, relations, and models are indexed over sets of integers or symbols (or refinements of these). The contents of these index sets can be fixed during array declaration or computed as a part of the problem formulation. For example, in the transportation model (transportation) presented in appendix A, the set of plants from which customer i is to receive product is computed from the list of customers specified for each plant, c[i].plantId := [j IN plantId | i IN p[j].customerId].

## 4.2.5. Procedures

ASCEND models and atoms can optionally contain procedures. These are used to compute initial values, and set degrees of freedom (e.g., the assignment x1.fixed := FALSE states that the value of the variable can be assigned by a solver). Several alternate procedures might exist (e.g., procedure init\_example28a and init\_example28b shown below) that can be invoked selectively by the user prior to solution. Procedures are able to invoke other procedures defined locally or within visible parts.

```txt
MODEL example28;
x1, x2 IS_A unscaled_variable;
x1*x2 - 1 = 0;
x1*x1 + x2*x2 - 3 = 0;

INITIALIZATION
PROCEDURE assign_bounds;
x1.lower_bound := 0;
x1.upper_bound := 4.0;
x2.lower_bound := 0;
x2.upper_bound := 4.0;
x1.fixed := FALSE;
x2.fixed := FALSE;
END assign_bounds;

PROCEDURE init_example28a;
RUN assign_bounds;
x1 := 2;
x2 := 2;
END init_example28a;

PROCEDURE init_example28b;
RUN assign_bounds;
x1 := 4;
x2 := 2;
```

END init\_example28b;
END example28;

## 4.2.6. Operators

The language has only five operators: REFINES, IS\_A, IS\_REFINED\_TO, ARE\_THE\_SAME, and ARE\_ALIKE. The REFINES operator implements monotonic inheritance, IS\_A implements incorporation, IS\_REFINED\_TO implements refinement of model parts, ARE\_THE\_SAME implements a way of recursively equivalencing structured objects [7, 51], and ARE\_ALIKE implements grouping of objects that are constrained to be structurally similar.

## 4.2.7. Inheritance and Part Refinement

Inheritance is supported through the REFINES operator. It promotes reusability and organization through the building of inheritance hierarchies, and provides a mechanism for type checking. For example, in the integrated transportation/forecasting model shown in appendix C, a customer\_forecast model has been defined that locally inherits the attributes of the customer model, and is further specialized by adding an instance of a forecasting model and a relation that specifies that the demand (dem) will be computed using the forecasting model.

The transportation-with-forecasting model (trans\_forecast) is then defined as a refinement of the basic transportation model with two additional constraints. These constraints specify that the set of customers defined in the basic transportation model will be “refined” to customers whose demand will be predicted by a forecasting model (c[customerId] IS\_REFINED\_TO customer\_forecast), and that for each customer, demand will be predicted using an exponential forecast:

c[customerId].F IS\_REFINED\_TO expForecast.

This refinement of parts, supported through the IS\_REFINED\_TO operator, permits evolutionary modeling and improves the possibilities of model reuse. An example of part refinement is shown in the IS\_REFINED\_TO statement in the previous paragraph where the structure of a customer forecast is refined to an exponential forecast. Possible refinements are defined by the structure of the inheritance hierarchies, and the refinement process is validated by the language compiler.

## 4.2.8. Strong Typing

Strong typing, which requires that the user indicate the type of every part in every model, reduces the debugging effort (during solving) for complex models. The basetype of a part is declared using the IS\_A construct. Also, the type system provides a mechanism by which the user can define legitimate ways in which parts can be connected together. For example, in the case of the inheritance hierarchy shown in figure 2, it would be invalid to attempt to connect an instance of liquid\_stream to an instance of vapor\_stream because the liquid\_stream and vapor\_stream models are not conformable. (Two models are said to be conformable if one is the ancestor of the other.) Errors that might arise in an attempt to make such a connection are detected by the language compiler.

## 4.2.9. Equivalencing

The recursive equivalencing of structured objects is supported through the ARE\_THE\_SAME operator. This facility is used to connect complex models by selecting parts (connectors) within models through which the connection is realized, and making these parts equal. Equivalencing several connectors together results in a single equational structure that can be referenced by all naming schemes defined by the connectors. For example, the intent of making the statement p[i].flow[j], customer[j].flow[i] ARE\_THE\_SAME is that the numeric value of the flow of product from plant i to customer j is equal to the value of the flow that customer j receives from plant i. This could have been written p[i].flow[j] = customer[j].flow[i]; however, this would needlessly create an extra equation, and require the maintenance of a duplicate copy of the flow variable. By using ARE\_THE\_SAME, no equation is created. The reduction in resources achieved by using ARE\_THE\_SAME is especially important in engineering applications where connectors may contain several hundred equations.

## 4.2.10. Grouping

Propagation of structural variations is supported through the ARE\_ALIKE operator. For example, in the trans\_forecast model one could write the statement c[customerId].F ARE\_ALIKE, which expresses the intent that all customers will use the same type of forecasting model. A structural change made to any individual forecasting model will automatically propagate to the others.

## 5. A Discussion of the ASCEND Language

IN THIS SECTION WE EXPLICITLY RELATE CHARACTERISTICS of the ASCEND modeling language to some of the characteristics and design implications outlined by Geoffrion [21]. In some cases we directly evaluate the ASCEND language by a Geoffrion ideal; in others we question or modify the premise embodied by his ideal. We begin by focusing on the notion of “executability” proposed by Geoffrion as a necessary attribute of a flexible modeling environment.

## 5.1. What Is Meant by Executable?

Geoffrion writes: “the adjective ‘executable’ refers to functions that programs in the modeling environment should be able to perform upon receiving a model written in an executable modeling language.” If one reads the previous statement literally,

![](/api/attachments/D75JQZGD/fulltext/images/e6a1d270bdd38b18f0b7a9c791e0908d63721e1e554c4005c9f242727ef96498.jpg)  
Figure 2. An Inheritance Hierarchy for Describing Material Streams

ASCEND is not an executable language. At present, the only ASCEND program that reads model descriptions is a compiler, which takes a model description and generates a data structure that can be interrogated using a set of procedures that we provide. External programs such as graphers, solvers, and spreadsheets are integrated into the environment by writing software bridges that allow values in an ASCEND data structure to be accessed by the external program in a format that it requires, and vice versa. This approach has several benefits: (1) a single bridge can be written that will work with all models written in the ASCEND language; (2) the model builder composes and revises models using only the modeling language, the solver input is automatically regenerated by the bridge; (3) the external programs can be used “as is” without any internal modifications; and (4) a single bridge can be constructed for a family of programs (e.g., an MPS file generator).

## 5.2. Can One Language Support All Users?

Geoffrion writes that the modeling language should be “sufficiently natural that non-modeling professionals can understand it with only a modest amount of training.” Our experience suggests that this may not be achievable. An extensive discussion of our views on this topic can be found in Piela et al. [45].

Our research responds to criticisms of languages such as GAMS being too low-level and too inflexible for solving real-world problems $[10]$ . On the other hand, the use of structured modeling languages is currently outside the experience of many users.

We have been working with academic and industrial users in an attempt to understand, evaluate, and refine the hypotheses underlying ASCEND modeling. Two themes have recurred in feedback we have received from these users. First, people's unfamiliarity with object-oriented concepts contained in the ASCEND language caused difficulties, and second, most had never taken a structured approach to the formulation of equational models (as opposed to using flat lists of algebraic specifications).

We suggest that rather than try to make the modeling language intuitive for all users (the lowest common denominator), language developers should account for users' differing competencies by providing adequate support structures (e.g., help systems, coaching, worked examples) for different skill levels and requirements.

## 5.3. Evolutionary Modeling

Geoffrion writes: “Flexibility is important because few modeling professionals ever get a model or model-based system 100% right the first time. Even if by some miracle they do, the requirements usually change over time and thus will soon induce the need for revision. In any case, evolution will be necessary for genuine excellence.” We agree. The current ASCEND language supports model evolution in two related ways. First, there is model inheritance, which allows the user to define a model that locally inherits the entire structure (variables, relations, procedures, and default values) from a single parent model. The user can then add statements to the new model. This kind of inheritance organizes models hierarchically. Second, there is part refinement, which allows a user to change the type of a part of a model. The part can only be refined to a member of the set of models that inherit from the current model or any of its descendants. By adopting a strictly monotonic view of inheritance we are able to guarantee that refinement of parts will yield well-formed model structures.

## 5.4. Declarative and Procedural

Geoffrion writes that for a modeling language to be understandable and natural it should be “declarative rather than procedural and highly mnemonic rather than cryptic.” While we agree that a declarative representation is natural for equational modeling, we also included procedural notions in the definition of models. An ASCEND model is divided into two sections, both of which are optional. The first contains declarative statements that are used to specify the equational structure of the model. The second contains a set of procedures written in a small imperative language, which are used to compute initial values of variables, to specify which variables are fixed and which are to be computed. Whereas other modeling systems only provide mechanisms for importing externally computed values, we believe that the knowledge encoded in procedures should be an explicit part of a model formulation.

## 5.5. A Common Modeling Language

Geoffrion writes: “in a true modeling environment, there should be a lingua franca (common language) for model formulation that is very broadly applicable and not biased toward any particular problem domain, or solver technology.” We have adopted this approach in the development of ASCEND, and have worked with users to develop model libraries in several domains.

## 5.6. Consistency Checking

Geoffrion writes that “an executable modeling language should be able to perform extensive consistency checking.” We have dealt with this issue through the use of strong typing. One of the major rationales for a strongly typed language is to minimize the amount of debugging that must be done during solving due to the difficulty of providing diagnostic information $[42]$ . Adequate diagnostic information is difficult to provide because the mathematical decomposition employed by solvers is usually different from the physical decomposition favored by users.

ASCEND's type system enables the compiler to detect errors like trying to connect (equivalence), group, or refine incompatible parts. By making dimensionality an explicit part of the declaration of an ATOM (variable), we are able to report equations that are dimensionally inconsistent, and to validate numeric assignments made to variables. We also use the type system to define which objects an external program can operate on. For example, plotting programs will only extract data from instances of the "plot" model or any of its refinements.

## 6. The ASCEND Environment

WE NOW TURN OUR ATTENTION TO THE INTERACTIVE INTERFACE of the ASCEND system. We will provide a functional overview of the ASCEND environment as it exists now. This will be followed in section 7 by a description of the methodology we employed to design and evaluate the environment, and a discussion of some of the meta-level issues surrounding interface support for modeling which this work revealed.

Once a model has been specified with the ASCEND language, instances of those models are displayed, solved, and evolved through an interactive graphic interface. The interface uses the metaphors of a “toolbox” (figure 3) and “desktop” (figure 4). The toolbox is a permanent area of the screen that contains buttons symbolizing available toolkits, and buttons that organize the interface. The desktop occupies the remainder of the screen and contains toolkits currently in use. Underlying the ASCEND system is a database that stores both model definitions and any instances of model definitions created through the interface (simulations). Each toolkit implements a semantically different view of the problem being examined (e.g., source code, structural, mathematical, etc.), and these views are maintained concurrently with the underlying database. That is, a change made in one toolkit is immediately reflected in the others.

Our experience with ASCEND has shown that multiple views are required to support complex problem solving, and this has been suggested by other workers in the area of mathematical modeling (e.g., [12, 26, 29]). In keeping with a direct manipulation paradigm, the user is able to share information generated in one tool by exporting references to objects within that tool directly into others. It should be noted that, unlike a conventional “clipboard,” only references to objects are passed, and not the data within the object. Only one copy of any piece of data is stored in the database.

![](/api/attachments/D75JQZGD/fulltext/images/b8f305384baef0dfb6c0fb6ce171ea21b36d950512bfcc1baa7f4c5f5aa5cffd.jpg)  
Figure 3. The Toolbox Is Used to Control the Visibility of Toolkits on the Desktop

Following is a brief description of the currently implemented toolkits—the Library, Sims, Browser, Solver, Probe, Units, Display, and Script.

Tools in the Library toolkit are used to create, view, and manipulate the inheritance hierarchies in which model definitions are organized. These hierarchies are created by loading model definitions from text files. After loading, the user selects one of the models in the library to be compiled into a database of equations and variables called a simulation. A number of different simulations can co-exist; each is listed in the toolkit labeled Sims. Once created, a simulation can be “played with” in many ways by the other tools in the system.

The Browser tools are used to select objects of interest within a simulation either by incremental navigation or direct query. Other tools perform operations on these objects: for example, displaying attributes in order to verify structure, creation of new parts within the objects, and refinement of the objects in an evolutionary modeling process.

Since complex models are created by equivalencing parts using the ARE\_THE\_SAME operator, many parts of a simulation will have alternate names. One of the tools allows the user to display all the names for a part and to pick one of these as the current focus. Another tool in the Browser executes procedures defined in the INITIALIZATION section.

The primary functions of the Solver are: to apply a chosen algorithm to the system of relations contained within the object it is viewing (the current object); and to assist in the investigation of failures that occur during solving. The current object is continually analyzed to see if it forms a well-posed problem. If it does not, the user can return to the Browser and reset some of the variable flags to indicate that some of them are to be fixed rather than computed. If these flags are contained in the current object, ASCEND will immediately reanalyze and report the consequences. An effort to solve the system of equations defined by the current object can be attempted even if the system is not “square” (i.e., the number of equations is not equal to the number of variables).

One tool in the Solver is a debugger where the user can display the incidence matrix for the equations (rows of the matrix) versus the variables (columns) in the problem. Solving can be done by single-stepping or by executing until a maximum number of iterations or a time limit is exceeded. At present, the user can select any one of the following solving packages that is compatible with the current object. Only compatible selections are actively displayed.

\- SLV [54, 55] is our own solver for solving $n$ nonlinear algebraic equations in $n$ unknowns. It is based on a modified Marquardt method [52]. The variables can have bounds specified for them, which will cause the solver to restrict its search for solutions within the bounds. SLV partitions the nonlinear equations and solves the partitions in a precedence ordering.

![](/api/attachments/D75JQZGD/fulltext/images/9db26e11e9bc5f90fe0ecff740c20bad7d01e7814d6ebb9a9971ca16d5cf232e.jpg)  
Figure 4. A Typical Desktop Configuration

\- MINOS-Augmented [41] is a nonlinear optimization code capable of handling several thousand equality and inequality constraints. It is available from Stanford University.

\- SQP is a sequential quadratic programming solver available from L.T. Biegler (Chemical Engineering, Carnegie Mellon University). The current implementation is a dense version and more appropriate for small problems (on the order of one hundred constraints).

\- LSODE [27], as used in the ASCEND system, is for solving dynamic models that involve a mixture of ordinary differential equations and algebraic equations. It integrates the model over time or space from a known initial condition. It is available from the Lawrence Livermore National Labs.

The Probe provides the user with the capability of forming collections of variables, equations, or complex parts that are of interest from disparate locations in a simulation, and to monitor their values during solving. The Probe contains tools that allow the user to detect whether any variables listed in it are poorly scaled or near one of their bounds.

The Units toolkit allows the user to specify the measurement units in which the values of variables are displayed. The user can define sets of units that can be saved in text files for later reuse.

The Script can be used in two ways. First, it can read a set of instructions from a text file specifying a sequence of actions to be taken by the system (e.g., read a model definition file, create a simulation, solve a simulation, plot a graph). The user can choose which instructions are executed. During execution, the interface is animated as if the user were actually pressing the buttons. Second, the script can be used to record commands invoked through the interface which can be written to a text file for later replay. We intend the Script to be both a convenience for expert users and an aid in teaching new users about the system.

In addition to the toolkits described above, there are a number of support tools that can be invoked through the interface. For example, objects can be viewed and manipulated using a Unix spreadsheet program, plotted using a number of x-y and x-y-z plotting programs, and used to create high-quality reports (e.g., equipment specification sheets) using Postscript templates generated by standard drawing programs or word processors.

## 7. A Discussion of the ASCEND Environment

GEOFFRION'S DISCUSSION OF SYSTEM DESIGN ISSUES FOCUSES on choices of representation, language issues, system components, and the attributes of an ideal system. Little detail is provided concerning specific interface design, or issues of usability. In the following section we explore some of these questions in the context of our work on ASCEND.

## 7.1. A Methodology for Design and Evaluation

Before we discuss the implications of the ASCEND interactive environment as an artifact, it is important to review the methods by which it has come about. The interface to ASCEND was developed using an iterative design approach. Our process is closely aligned with what has become known as Participatory Design [4, 16], an approach to system development that emphasizes close and continuous interaction between developers and users, and techniques of rapid prototyping. An in-depth discussion of this design methodology and our interpretation of it is the subject of another paper [44]. What follows is a summary of some of that paper's major points.

The ASCEND project's primary focus is to investigate whether a design system based on a structured, declarative modeling language, and a supporting environment in which to work with the models that result, can improve modeling speed, reduce errors, expand the complexity of problems attempted, and support significant amounts of model reuse. While we believed that the underlying technology had the potential to achieve these aims, there was no way to test this without a functioning system and users to work with it. To this end, the ASCEND environment was created, not as an embodiment of how its developers expected the system to be used, but rather as an experimental apparatus to test the feasibility of the ASCEND paradigm and to provide input into its further development.

We used an ethnographic approach in which we studied how users worked with the evolving technology in their own workplaces, and on their own problems. This is in contrast to the more common practice of evaluating a system by examining system performance on a standard set of example problems in a contrived experimental setting. We have employed three intertwined sources of data in our analyses. The first comes from conversations in work situations, in which users articulate issues associated with their problem solving. Although we value people's opinions about what they would like to see in the environment, we have found that conversations referring to local problems are more reliable indicators of their needs. As we discuss these problems with users, we not only learn about their immediate concerns, but can extract from these cases general lessons that impact on the system design as a whole. The second source comes from observation of people as they work on problems. Observation is particularly valuable for catching the kind of problems that lie just below the surface of people's consciousness (and thus tend not to be articulated) yet undermine their work. The final source of information comes from studying the outcomes of modeling efforts—the partial or complete solutions to a wide range of modeling tasks. For example, we were interested in whether people found ASCEND's "glass box" models (whose entire internal structure was accessible) difficult to work with, and used the high degree of nestedness in the models written by some users as evidence that the approach was not inherently unmanageable. We maintain careful records of the conversations and observations (using videotape or audiotape when possible), and of the work users have accomplished with the system. This allows us to study the records collaboratively, to add robustness to our analyses, and to get a longitudinal perspective on the system's development.

The system has been under continual evaluation and evolution for the last three years. Its users have come from a wide range of academic disciplines (chemical engineering, operations research, physics, architecture) and also include a number of industrial users. The development team has consisted of a faculty member of the Chemical Engineering Department who is expert in the area of mathematical modeling, a researcher whose thesis work was directly tied to the project, two representatives of the Design Department with experience in human factors, graphic design and user-interface issues, an expert in document design and on-line help systems, and two undergraduate programmers.

## 7.2. Interface Design Issues

Here we focus on some meta-level issues relevant to the support of modeling activity that have emerged from the development process described above. We isolate five basic features of the ASCEND environment and discuss their derivation, their implementation, and when possible, their effect on actual problem solving behavior. These features are:

1. A high degree of integration and behavioral consistency among tools;

2. Support for flexible interaction among modeling phases;

3. Support for arbitrarily fine access to models, instances, equations and variables;

4. Support for user-configurability of system organization and behavior;

5. Domain-independence.

## 7.2.1. Tool Design and Integration

ASCEND modeling can be conceptualized as a set of phases, each implying several distinct activities. These are: model formulation, loading of models into the system, model instantiation, browsing and selection of instance structures, solution, and display of results. Through our analysis of system use, we have seen that these activities can vary widely in frequency, sequence, and duration. Further, they can vary depending on both the type of problem being attempted, and people's modeling style. As we began to develop interactive mechanisms to support ASCEND's various modeling phases, it became clear that each suggested a different view of the data with its own set of supporting operators. For example, browsing of instance structures requires a view of that structure and a series of operators that provide means for navigating through it. The Solver, on the other hand, should display characteristics of the problem in terms of numbers of equations and variables, and provide operators that assist in bringing the model to convergence.

To represent the different phases we adopted the toolbox/toolkit approach as described in section 6. This approach has allowed us to isolate each modeling phase into its own context. We define an ASCEND toolkit (see figure 5) as consisting of three parts: a frame, a set of menus, and a view. A frame, which defines a toolkit's size and location, includes the toolkit's name, mechanisms for repositioning and resizing the toolkit, and access to a set of user-definable attributes that determine its meta-level behavior. For instance, the Browser can be set to display subitems at a depth greater than one, or it can be set to display objects of a given grain size, such as showing only instances of models while ignoring specific equations and variables. The view is a display that shows objects of a relevant data type to the toolkit in a particular format. For example, in the Library the view shows those models loaded into the system in the form of an inheritance hierarchy. The menus hold all tools that operate directly on the data element(s) currently in the view. In creating this abstracted tool definition, we can easily bring a high level of consistency to all modeling phases, and provide what Geoffrion calls a “conceptual unity” [21] to the system.

Given this framework, there still remains the problem of affiliating specific functions (tools) with the different phases (toolkits). Although certain tools can have only one logical home (e.g., the invocation of the solving algorithms clearly belongs in the Solver toolkit), others seem to have more than one possible affiliation. For example, a number of tools are used to analyze different aspects of the instance structure and, depending on when the user chooses to perform an analysis, individual tools may seem to belong most appropriately to the Browser, the Probe, or even the Solver. As we learn more from users' modeling experience with ASCEND we get a better idea of which placement best supports the most common practices.

## 7.2.2. Flexible Interaction

Although users will eventually encounter each of the modeling steps mentioned in section 7.1, the sequence of different steps is not preordained by the model declaration. As mentioned above, we have seen widely varying approaches to the modeling process. For example, once a simulation has been instantiated, users may decide to solve individual parts before addressing the whole, or in debugging a simulation, they may inspect several aspects of the problem in order to make sense of diagnostic information provided by the solving algorithm.

We have frequently witnessed users employing multiple toolkits to make decisions, and thus require that the information within the various views of these toolkits be up-to-date, reflecting the current state of the database. Tools that maintain this degree of communication are said to be concurrent [18]. ASCEND tools have a concurrent implementation so that any change to the database made by one is immediately broadcast to the others. Users take advantage of concurrency when they fix a variable within the Browser and watch for its effect on the block structure of the problem within the Solver. However, communicating a notion of concurrency to our users has not always been easy. The notion of a set of multiple tools “hovering” over a single model database is contrary to the more familiar “cut & paste” paradigm presented by many systems, and has proved confusing for some.

Another aspect of ASCEND modeling to be accommodated is support for the user in shifting between the representations in building and solving models. These representations include the model code, the model hierarchies maintained by the Library, and the instance structure that results from model compilation. When we have observed the need for quick reference between specific representations, we have provided functions to simplify the interaction. For example, in browsing an instance structure, it is typical to want to view the code that defines a specific object. The code description of a model is normally accessed through invoking a "show code" function in the Library. To simplify this, we have partially automated this procedure so that a mouse-click on the current object's type indicator (in figure 5, this is the area that reads "IS\_A heat\_exchanger") will result in focusing the Library view on that type definition.

![](/api/attachments/D75JQZGD/fulltext/images/a13b62684332b7683ee974f396c195b96a98c1c4683cc8a5dfa5431e50aad1b9.jpg)  
Figure 5. The Browser Exemplifies the Design of a Prototypical ASCEND Tool

Although the flexibility in sequencing activities has been positively exploited by ASCEND users, there is a downside to the lack of predictability: it makes it difficult to diagnose when a problem has occurred and thus difficult to provide support. For example, when the system is reported as “underspecified” (too few variables fixed for the number of equations), it may be indicative of a bona fide problem for the user, or rather a modeling style in which procedures that would make the system “square” are run relatively late in the modeling process. This unpredictability makes the job of preparing help or training materials more difficult than it would be for a system where a standard sequence was always employed.

## 7.2.3. Flexible Data Access

The ASCEND approach is predicated on the belief that users require access to all parts of a model, down to specific equations and variables. Having decided what is of interest, the user may need to alter the views presented by the toolkits to reflect this interest. The system provides various mechanisms for locating specific objects. These include manual navigation (browsing), search by name, and search by model type.

Once located, objects can be incorporated into toolkit views in a number of ways. For example, the Probe allows the model builder to create arbitrary lists of objects from disparate locations in the problem structure. This toolkit has been used extensively, and has undergone several revisions. Although it was originally conceived to support the passive observation of variables and their values, it has proved to be a convenient place to locate certain tools for analyzing the problem data. These include tools that check whether variables are properly scaled, or jammed against their bounds.

## 7.2.4. User-configurability

A natural outcome of the decision to cast ASCEND into a multitool, multiwindow form was the need to provide a high degree of user control over the environment. For example, if a simulation is being investigated to determine the details of its structure, a user might want the Browser to occupy the whole screen, with a view of as much of the instance structure as possible; in other situations, the Browser might simply be used to select a variable and require relatively little screen space. Thus, users are able to manage their screen layout to suit both their problems and their preferences.

Although the ASCEND interface makes no assumptions about tool size, shape, location, or even presence, it has been designed to prevent catastrophic failures such as “losing” a tool, or reshaping it to an unmanageable state (i.e., where important controls cannot be accessed). In anticipating such problems, however, we have been careful not to introduce unnecessary constraints on tool management, following Suchman’s advice that an interface should support “the negotiation of trouble rather than trying to preclude trouble” [49]. The management of tools is facilitated by the presence of the Toolbox which allows them to be easily removed from the screen and restored to their previous size, location, and state.

We also provide users with the means to store personally designed screen configurations for later retrieval. Typically, new users will create a tiled layout in which all tools can be monitored simultaneously. However, as they gain experience, their default layouts consist of fewer tools and usually anticipate a specific modeling task.

The ASCEND environment does not borrow the entire screen—it coexists freely with other processes and windows. For example, since attempts to solve model instances often reveal deficiencies in the original formulation, it is commonplace for users to edit the text files that contain these formulations using their favorite text editor in the midst of an ASCEND modeling session. Such coexistence gives people added flexibility in working with ASCEND as well as in accomplishing other nonmodeling tasks. This is a fairly loose integration of applications, but we have seen that people take advantage of it. Although Geoffrion proposes a high degree of integration for optimal communication between tools, we claim that too tight an integration can also overly restrict users whose work goals can never be entirely predicted by us.

## 7.2.5. Domain Independence

The goal in designing the ASCEND system was to enlist collaboration from multiple disciplines. Thus, an initial decision was made to keep the environment domain-independent. A second decision was to develop an “engineer’s interface” [19] that as much as possible explicitly revealed ASCEND’s underlying organization to the user. Since our goal in system development was an investigation of a new paradigm for modeling, the point of this approach was to elicit responses from users at the level of basic concepts. The implementation of the engineer’s interface requires a particularly sophisticated design treatment, because instead of hiding the underlying complexity, it must be presented in a clear and comprehensible fashion.

Thus the ASCEND system deliberately avoids “real-world” metaphors and domain-specific semantics, although users do introduce their own semantics in naming components of the models they build. We have, however, encountered some complaints about the overgenerality of ASCEND. These have come particularly from industrial users, who are most familiar with environments that are customized for specific applications. We acknowledge this problem, and are currently investigating how domain-specific layers might be added to the basic ASCEND “engine.”

## 8. Conclusion

IN THIS PAPER WE HAVE ARGUED FOR THE NEED for a structured approach to mathematical modeling, distilling user requirements into three major categories: hierarchical decomposition, evolutionary modeling, and debugging. We described the syntax and semantics of the language that resulted from our attempts to support these needs. Our experience so far indicates that it supports the rapid writing of complex models. However, there is also a cost involved in learning the language, because the approach is foreign to most users.

In designing the interactive environment to this language, it has been important to support the kind of flexible interaction that is implied by equational models. We have argued that this means decomposing the modeling process into distinct subtasks and providing toolkits that are designed specifically to support them. Although we have reified the modeling process to this extent, we have avoided prescribing a strict order in which these tasks must be carried out.

Our experience has shown that model builders need a dynamic view of large and complex sets of data. By dynamic, we mean both changing content and changing levels of detail. By data, we refer to model code, instance values, and the structures by which they are organized. We argue that this means allowing people a high degree of control over their environment.

We have been encouraged by the success of users who have taken vastly different approaches to formulating and solving problems with ASCEND, and by the degree to which features have been utilized in actual practice. We see this as evidence for the efficacy of the ASCEND technology.

## NOTE

1. A flowsheet is a collection of pieces of equipment connected in such a way that they describe a complete chemical process.

## REFERENCES

1. Bhargava, H.; Kimbrough, S.; and Krishnan, R. Unique names violations: a problem for model integration or you say tomato, I say tomahto. ORSA Journal of Computing, 3, 2 (1991), 107–121.

2. Bhargava, H.K., and Krishnan, R. Computer-aided model construction. Decision Support Systems (1992), forthcoming.

3. Binbasioglu, M., and Jarke, M. Domain specific DSS tools for knowledge-based model building. Decision Support Systems, 2 (1986), 213–223.

4. Bjerknes, G.; Ehn, P.; and Kyng, M. Computers and Democracy. England: Avebury, 1987.

5. Blanning, R.W. A relational framework for model management in decision support systems. DSS-82 Transactions (1982), 16–28.

6. Blanning, R.W. A relational framework for join implementation in model management systems. Decision Support Systems, 1, 1 (1985), 69–81.

7. Borning, A. ThingLab: a constraint oriented simulation laboratory. Ph.D. dissertation, Stanford University, 1979.

8. Brooke, A.; Kendrick, D.; and Meeraus, A. GAMS: A User's Guide. Redwood City, CA: Scientific Press, 1988.

9. Dee, K.C. CEPHDA: chemical engineering process hierarchical design with ASCEND. Technical Report, Engineering Design Research Center, Carnegie Mellon University, Pittsburgh, 1992.

10. Dhar, V., and Ranganathan, N. Integer programming vs. expert systems: an experimental comparison. Communications of the ACM, 33, 3 (1990), 323–336.

11. Dolk, D.R. Model management in organizations. Paper presented at ORSA/TIMS Conference, San Francisco, 1984.

12. Dolk, D.R. A generalized model management system for mathematical programming. ACM Transactions on Mathematical Software, 12, 2 (1986), 92–125.

13. Elam, J.J. Model management systems: an overview. Working Paper 79–12–04. Decision Sciences, The Wharton School, University of Pennsylvania, 1979.

14. Elam, J.J. Model management systems: a framework for development. Proceedings of the 1980 SE AIDS, 1980, 35–38.

15. Elam, J.J.; Henderson, J.C.; and Miller, L.W. Model management systems: an approach to decision support in complex organizations. Proceedings of the First International Conference on Information Systems, 1980, 98–110.

16. Floyd, C.; Mehl, W.M.; Reisin, F.M.; Schmidt, G.; and Wolf, G. Out of Scandinavia: alternative approaches to software design and system development. Human-Computer Interaction, 4 (1989), 253–350.

17. Fourer, R.; Gay, D.M.; and Kernighan, B.W. A mathematical programming language. Management Science, 36, 5 (1990), 519–554.

18. Garlan, D. Views for tools in integrated environments. Ph.D dissertation, Department of Computer Science, Carnegie Mellon University, 1987.

19. Gentner, D.R., and Grudin, J. Why engineers (sometimes) create bad interfaces. Proceedings of CHI'90: Human Factors in Computing Systems, Seattle, 1990, 277–282.

20. Geoffrion, A. M. An introduction to structured modeling. Management Science, 33, 5 (1987), 547–588.

21. Geoffrion, A. M. Computer-based modeling environments. European Journal of Operations Research, 41 (1989), 33–43.

22. Geoffrion, A. M. Reusing structured models via model integration. Proceedings of the Twenty Second Hawaii International Conference on the System Sciences. IEEE Press, 1990, 601–611.

23. Geoffrion, A. M. The SML language for structured modeling: levels 1 and 2. Operations Research, 40, 1 (1992), 38–57.

24. Geoffrion, A. M. The SML language for structured modeling: levels 3 and 4. Operations Research, 40, 1 (1992), 58–75.

25. Greenberg, H.J. A functional description of ANALYZE: a computer-assisted analysis system for linear programming models. ACM Transactions on Mathematical Software, 9 (1983), 18–56.

26. Greenberg, H.J., and Murphy, F.H. Views of mathematical programming models and their instances. Technical Report, Mathematics Department, University of Colorado at Denver, 1991.

27. Hindmarsh, A.C. LSODE and LSODI, two new initial value ordinary differential equation solvers. ACM-Signum Newsletter, 15 (1980), 10–11.

28. Hurlimann, T. Reference Manual for the LPL Modeling Lanuage (Version 3.1). Institute for Automation and Operations Research, University of Fribourg, CH-1700 Fribourg, Switzerland, 1989.

29. Hurlimann, T. Modeling tools. Working Paper No. 200, Institute for Automation and Operations Research, University of Fribourg, CH-1700 Fribourg, Switzerland, 1992.

30. Konsynski, B., and Dolk, D. Knowledge abstractions in model management. DSS-82 Transactions (1982), 187-202.

31. Krishnan, R. Automated model construction: a logic based approach. Annals of Operations Research, 21 (1989), 195–226.

32. Krishnan, R.; Piela, P.; and Westerberg, A.W. Reusing mathematical models in ASCEND. In A. Whinston and C. Holsapple (eds.), Proceedings of the NATO ASI on Decision Support Systems. Il Ciocco: Springer-Verlag, 1991, forthcoming.

33. Krishnan, R., and Piela, P. A formal analysis of the ASCEND modeling language. Draft Technical Report, The H. John Heinz III School of Public Policy and Management, Carnegie Mellon University, Pittsburgh, 1992.

34. Liang, T.P. Integrating model management with data management in decision support systems. Decision Support Systems, 1, 3 (1985), 221–232.

35. Liang, T.P. Modeling by analogy: an approach to automated linear program formulation. Working paper, Krannert Graduate School of Management, Purdue University, West Lafayette, IN, 1990.

36. Locke, M.H. A CAD tool which accommodates an evolutionary strategy in engineering design calculations. Ph.D. dissertation, Department of Chemical Engineering, Carnegie Mellon University, 1981.

37. Locke, M.H., and Westerberg, A.W. The ASCEND-II system—a flowsheeting application of a successive quadratic programming methodology. Computers and Chemical Engineering, 7, 5 (1983), 615–630.

38. Muhanna, W.A., and Pick, R.A. Composite models in SYMMS. Proceedings of the 21st Annual Hawaii International Conference on System Sciences, 1988, 418–427.

39. Muhanna, W.A., and Pick, R.A. Meta-modeling concepts and tools for model management: a systems approach. Working Papers Series 91–1, College of Business, The Ohio State University, 1991.

40. Murphy, F.H., and Stohr, E.A. An intelligent system for formulating linear programs. Decision Support Systems, 2 (1986), 39–47.

41. Murtagh, B.A., and Saunders, M.A. MINOS user's guide. Technical Report SOL 83–20, Systems Optimization Laboratory, Department of Operations Research, Stanford University, 1985.

42. Perkins, J.D. Equation-based flowsheeting. In Arthur W. Westerberg and Henry H. Chien (eds.), Proceedings of the Second International Conference on Foundations of Computer-Aided Process Design. Snowmass, CO, 1983.

43. Piela, P. ASCEND: an object-oriented computer environment for modeling and analysis. Ph.D. dissertation, Carnegie Mellon University, 1989.

44. Piela, P.C.; Katzenberg, B.; and McKelvey, R.D. Integrating the user into research on engineering design systems. Research in Engineering Design, 3 (1992), 211–221.

45. Piela, P.; Epperly, T.; Westerberg, K.; and Westerberg, A. ASCEND: an object-oriented computer environment for modeling and analysis: the modeling language. Computers and Chemical Engineering, 15, 1 (1991), 53–72.

46. Raghunathan, S.; Krishnan, R.; and May, J.H. MODFORM: a knowledge based tool to support the modeling process. Technical Report, Artificial Intelligence in Management Laboratory, University of Pittsburgh, 1992.

47. Sapossnek, M. Research on constraint-based design systems. Proceedings of the 4th International Conference on Applications of AI in Engineering. Cambridge, UK, 1989.

48. Smith, O. Solving optimal control profiles as algebraic equations. Technical Report, Engineering Design Research Center, Carnegie Mellon University, 1988.

49. Suchman, L. Common sense in interface design. Techne: Journal of Technological Studies (June 1987).

50. Sussman, G.J., and Steele, G.L. CONSTRAINTS—a language for expressing almost-hierarchical descriptions. Artificial Intelligence, 14 (1980), 1–39.

51. Sutherland, I. Sketchpad: a man-machine graphical communications system. Technical Report No. 296, MIT Lincoln Laboratory, 1963.

52. Westerberg, A.W., and Director, S.W. A modified least squares algorithm for solving sparse $n \times n$ sets of nonlinear equations. Computers and Chemical Engineering, 2, 2/3 (1978), 77–81.

53. Westerberg, A.W., and Benjamin, D.R. Thoughts on a future equation-oriented flowsheeting system. Computers and Chemical Engineering, 9, 5 (1985), 517–526.

54. Westerberg, K.M. Development of software for solving systems of linear equations. Technical Report, Engineering Design Research Center, Carnegie Mellon University, Pittsburgh, 1989.

55. Westerberg, K.M. Development of software for solving systems of nonlinear equations. Technical Report, Engineering Design Research Center, Carnegie Mellon University, Pittsburgh, 1989.

56. Woodbury, R.F. Variations in solids: a declarative treatment. Computers and Graphics, Special Issue on Features and Geometric Reasoning, 14, 2 (1990), 173–188.
57. Zaher, J. Developing reusable libraries in the ASCEND environment. Technical Report, Engineering Design Research Center, Carnegie Mellon University, Pittsburgh, 1991.

## APPENDIX A: The Transportation Model

```txt
IMPORT transportation_atoms;
MODEL plant;
sup IS_A supply_capacity;
customerId IS_A set OF integer;
maxCustomer IS_A integer;

CARD(customerId)<= maxCustomer;

f[customerId], totalFlow IS_A flow;
cost[customerId] IS_A unitCost;
totalFlow = SUM(f[customerId]);
totalFlow<= sup;

shipmentCost IS_A cost;
shipmentCost = SUM(f[i]*cost[i] | i IN customerId);
END plant;

MODEL customer;
dem IS_A demand;
plantId IS_A set OF integer;
f[-trained] IS_A flow;
SUM(f[-trained]) = dem;
END customer;

MODEL transportation;
plantId, customerId IS_A set OF integer;
p[-trained] IS_A plant;
c[-trained] IS_A customer;
FOR i IN customerId CREATE
    c[i].plantId := [j IN plantId | i IN p[j].customerId];
END;
FOR i IN plantId CREATE
    FOR j IN p[i].customerId CREATE
    p[i].flow[j], customer[j].flow[i] ARE_THE_SAME;
    END;
END;
obj : MINIMIZE SUM(p[i].shipmentCost | i IN planId);
END transportation;
```

## APPENDIX B: Forecasting Models

```txt
IMPORT forecast_atoms;
MODEL product;
Tf IS_A integer;
dem[1..Tf] IS_A demand;
END product;
MODEL forecast;
Tf IS_A integer;
D[1..Tf] IS_A demand;
E[1..Tf] IS_A expectedValue;
S[2..Tf] IS_A smoothedValue;
F[2..Tf] IS_A forecastedValue;
END forecast;
MODEL expForecast REFINES forecast;
alpha IS_A dimensionlessConstant;
E[1] = D[1]
FOR i IN [2..Tf] CREATE
    E[i] = alpha*D[i] + (1-alpha)*E[i-1];
    F[i] = E[i] + S[i]/alpha;
END;
S[2] = E[2] - E[1];
FOR i IN [3..Tf] CREATE
    S[i] = alpha*(E[i]-E[i-1]) + (1-alpha)*S[i-1];
END;
END expForecast;
```

IMPORT transportation;
IMPORT forecast;

MODEL forecastedProduct;
p IS\_A product;
f IS\_A forecast;
p.Tf, f.Tf ARE\_THE\_SAME;
p.dem, f.D ARE\_THE\_SAME;
END forecastedProduct;

MODEL customer\_forecast REFINES customer;
F IS\_A forecast;
dem = F.E[F.Tf];
END customer\_forecast;

MODEL trans\_forecast REFINES transportation;
c[customerId] IS\_REFINED\_TO customer\_forecast;
c[customerId].F IS\_REFINED\_TO expForecast;

END trans\_forecast;
