---
otero_id: 21349
otero_key: "7VHHWUHE"
title: "BLOOMS: A prototype modeling language with object oriented features"
authors: "Marco Gagliardi; Cosimo Spera"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00040-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# BLOOMS: A prototype modeling language with object oriented features

Marco Gagliardi $^{a}$ , Cosimo Spera $^{b,*}$

$^{a}$ Dipartimento di Statistiche, Probabilità e Statistiche Applicate, University of Rome “La Sapienza”, p.zzale A. Moro 8, 00185 Rome, Italy $^{b}$ Dipartimento di Metodi Quantitativi, University of Siena, Piazza S. Francesco, 53100 Siena, Italy

## Abstract

The success of a Decision Support System (DSS) can be mainly attributed to the language it uses. The language has to be: (1) powerful, so as to express a wide variety of problems; (2) flexible, so as to be managed and updated not only by the vendors but also by the end-users; and (3) user-friendly, so as to minimize the time necessary for learning how to model the problem and derive its solution if a well defined solution exists. Often the term “user-friendly” also means that the system provides graphical tools for the user, which constitute the Graphical User Interface (GUI). In this paper we introduce the reader to the implementation features of an Object Oriented language, called BLOOMS (Basic Language Object Oriented for Modeling Systems), designed by the authors. BLOOMS has to be viewed not only as a different implementation of Structured Modeling (SM) languages, but also as a possible extension of SM in the framework of Object Orientation.

Keywords: Optimization; Decision support systems; Modeling languages; Structured modeling; Object orientation

## 1. Introduction

Since most Decision Support Systems (DSSs) assist modelers (users with very little mathematical training) and Operations Research/Management Science (OR/MS) analysts in just a few phases of the modeling process, our objective is to provide additional tools to construct a well developed system which is able to help modelers during all phases of the modeling process. Like many researchers in this field, we face the problem of deciding between the following two alternatives: (a) should we design systems easy to use by the modelers or (b) should (OR/MS) analysts train the modelers before using their systems?

Even if it seems that the OR/MS community will benefit more if OR/MS analysts play a dominant role, we are convinced that OR/MS techniques will be more diffused when modelers interact with well developed systems because the more they learn the more demanding they become. To show how to construct such a system, in what follows, we motivate the choice of the modeling framework and discuss one possible representation of it.

In the past years two modeling frameworks have been intensively studied by many scholars: (1) the algebraic and (2) Structured Modeling (SM) frameworks. Conceptually, the algebraic framework is mainly based on set theory, but it is not rigorously defined so that the semantics of the languages based on it may vary considerably, as also shown by Vicuña [44]. What makes the algebraic languages so popular in the scientific OR/MS community is the almost complete adherence of the model's description to its algebraic notation. As an example let us consider the following problem, known in the OR/MS literature as the “single knapsack problem” (SKP): given a list of n objects, indicate with $p_{i}$ and $w_{i}, i = 1, \ldots, n$ respectively profits and weights, the aim is to decide which items have to be contained in a knapsack with $w_{0}$ capacity so to maximize its z value. The algebraic notation for this problem is:

$$
z = \max \sum_ {i = 1} ^ {n} p _ {i} x _ {i}\tag{1}
$$

subject to

$$
\sum_ {j = 1} ^ {n} w _ {i} x _ {i} \leq w _ {0},
$$

$$
x _ {i} = 0, 1, \quad i = 1, \dots , n,\tag{2}
$$

(3)

where $x_{i}$ represents a decision variable set to one if item i is included in the knapsack, zero otherwise.

AMPL-GAMS knapsack formulations

Two of the most popular algebraic languages, AMPL [16,17,14] and GAMS [6], allow the user to formulate the problem as shown in Table 1. The main advantage of these formulations, when compared to the matrix generator languages, is their closeness to the modeler's form rather than the algorithm form, [13]. Some comments and limitations on these representations can be found in [27,39]. Here we add two more observations:

Table 1

<table><tr><td rowspan="2" colspan="3">AMPL formulationknapsack.modset OBJECTS;</td><td>GAMS formulation</td></tr><tr><td>SET OBJOBJECTS/PENCIL,W-BOTTLE,MAP/;</td></tr><tr><td colspan="3">param p {OBJECTS} &gt; 0; # profitsparam w {OBJECTS} &gt; 0; # weightsparam w0 &gt; 0; # Capacityvar x {OBJECTS} binary;maximize Total_Value:sum {i in OBJECTS} p[i]* x[i];subj to Weight_Limit:sum {i in OBJECTS} w[i]* x[i] &lt;= w0;knapsack.datset OBJECTS := PENCILW-BOTTLEMAP;param: p w :=PENCIL 100 5W-BOTTLE 200 10MAP 50:= 14;param w0 := 14;</td><td>PARAMETERSCOST(OBJ)/PENCIL 100W-BOTTLE 200MAP 50/;WEIGHT(OBJ)/PENCIL 5W-BOTTLE 10MAP 1/;SCALAR TOTCAP /14/;VARIABLES X (OBJ)Z;BINARY VARIABLE X;EQUATIONSTOTCOST CAPACITY;TOTCOST.. Z = E = SUM (OBJ,X(OBJ)* COST(OBJ));CAPACITY.. SUM(OBJ,X(OBJ)* WEIGHT (OBJ)) = L = TOTCAP;MODEL KNAPSACK /ALL/;SOLVE KNAPSACK USING MIP MAXIMIZING Z;DISPLAY X.L, X.M;</td></tr></table>

\- Use of linear algebra notation. Although some algebraic languages allow the use of a “compact” notation to express special structures of the objective functions and/or constraint matrices [14,15], they do not support linear algebra operations. For example, many advanced users would like to express the constraint (2) in linear algebra notation as $w'x \leq w_{0}$ , where $w'$ and x are arrays of length n and $w_{0}$ is a scalar, so as to omit the indices.

\- Granularity of the model. The current implementations of algebraic languages do not allow block (sub-components) of the models to be extracted without violating their semantics. The direct consequence is that model integration appears to be difficult to achieve when these blocks have to be used in the integration process [19].

These general comments on the algebraic framework motivate the study of the SM framework, originally developed by Geoffrion [23,25]. This framework allows the user to see the model as a collection of objects, which may be self-defined (primitive entities) or have references to objects defined previously.

Five different types of objects exist: primitive, compound, attribute, function and test as shown in Table 2. If these objects were represented as nodes and their dependencies as direct arcs, the result would be a directed acyclic graph (DAG). The acyclicity is established by the fact that objects are not allowed to have direct or indirect self-references.

```txt
Table 2
Structured modeling type hierarchy
Primitive
Primitive Entity
Non primitive
Without value
Compound Entity
With value
Supplied by the user
Attribute
Computed value
Logical value
Test
Non-logical value
Function
```

In our opinion, the SM framework presents some advantages for the user over the algebraic framework. The most relevant is that it can represent a much wider range of models. In fact, many examples of non-optimization models expressed in SML (Structured Modeling Language), - a definitional SM language - are given by Geoffrion in [28,29]. Hence, SM is defined by a rigorous conceptual framework for which the semantics are well specified. Another advantage is the hierarchical structure of the model. This is expressed at three levels: elements, genera, modules. Similar elements are grouped into genera and these by semantic affinity are assembled into modules, so that the resulting modular structure is a tree having, as its root, the whole model. The hierarchical organization enables a variable granularity view of the objects constituting the model. This variable granularity view facilitates the development of procedures for model integration, as amply discussed in [21,19,30]. The possibility of realizing full integration among models should convince the reader of the potential that the SM framework offers.

The paper is organized as follows: Section 2 contains a short description of the implementation design, i.e. it describes the main modules of the language: from the features of the GUI to the communication with the solver. It also describes the steps taken by the user to model the single knapsack problem. Section 3 discusses how implementational details of the language: classes, indexing structure and internal/external inheritance of methods. Section 4 reports on conclusions and future extensions. Appendix A presents a simple recursive model which is expressed in BLOOMS.

## 1.1. SM languages and their implementations

Given the independent nature of the core concepts of SM, many language implementations have been proposed. Here we briefly review some of the most promising:

(a) Definitional text based. The language proposed by Geoffrion, SML [24,28,29,30], is constructed on four different levels of increasing expressive power. In fact, level 1 covers simple definitional systems, while level 4 covers sparse versions of mathematical programming problems. Its implementation, FW/SM [26], has been realized on top of FRAMEWORK [2]. An interesting use of some of the modules (SML Check, Interp\_CK, EDGEN and FcEval) from the FW/SM prototype for a research project funded by the Chilean government can be found in [31]. Moreover, Neustadter and Lin, respectively in [42,38], have introduced some relevant variations to improve readability and writability writof the model.

(b) Graph-based. The SM paradigm allows a natural development of graphical “features”. This has motivated the study and the implementation of graphical languages. Jones [35] applies his work on graph-based modeling to SM, producing a prototype called NETWORKS realized in Prolog with a visual interface. The main advantages of this approach is that many problems can be modeled as graphs. Some disadvantages concern the modeling of problems which cannot be seen as graphs and the choice of

Prolog which slows down the performance of the system $[34,36]$ . The graphical approaches taken by Chari and Sen $[7–9]$ focus on a model graph for representing a model class. Their implementation named GBMS/SM supports “all the stages of the model development life cycle” $[9]$ . Their Model Expression Language allows “expressions associated with the graphical construction” to be represented. A third graphical approach by Hamacher et al. $[32]$ adds some features from the entity-relationship model to the genus graph. Their prototype called IGOR (Integrated Graphics for Operations Research) is implemented in GRAPHTALK under Windows.

(c) Logic-based. Chari and Krishnan [10] proposed a logical based language named LSM. Its novelty is to link necessary information for managing the model with its definition. LSM appears to be useful if it is embedded in a Model Management System (MMS). LSM is partially implemented in

![](/api/attachments/7VHHWUHE/fulltext/images/15317755eae722a363aa2e8d8f5b9628e3151cbc37adc1f493a46c2a9b513764.jpg)  
Fig. 1. The structure of the BLOOMS modeling system.

Prolog. This achieves an elegant notation but limits its use for large scale problems.

(d) Object oriented. The success of Object Oriented (OO) computing lies in its particular approach to provide abstractions. Its philosophy can be summarized by this quotation by Blair et al. [5]:

The philosophy of object-oriented computing is to provide tools and techniques which are supportive of problem solving and hence implementation considerations are secondary.

Our motivations to pursue this approach comes from the commencement that Object Orientation allows to extend the SM definitional core concepts. To support the above claim, we give the “extended” definition of the 10th SM core concept (Generic Structure) [25]. Added words are emphasized.

A generic structure is defined on an elemental structure as a collection of partitions, one for each of the five types of elements. The associated mutually disjoint and exhaustive element sets are called genera. Genera have their own functionality: genera of the same type have the same operational behavior.

The next sections present the implementation of BLOOMS. Although our approach for BLOOMS defines the SM types as metaclasses (i.e. classes which create other classes), SM genera as typed classes and SM elements as objects created by the genera, the implementational approach does not fully match the theory. The reason for this choice is fully motivated in Section 3.

A different OO approach has been taken by Lenard [37], who uses the inheritance principle to rationalize the hierarchical modeling structure.

## 2. BLOOMS and its hosting modeling system

The user interacts with BLOOMS through the GUI. This also activates the modules of the MMS drawn in Fig. 1 as rectangles. There, data are represented as ellipses and arrows indicate exchanges of data or commands between modules and databases. A detailed description of this MMS and its implementation is provided in a companion paper [22].

As the system is designed to support model builders with little experience in OR/MS, the role of the GUI becomes crucial. A working session started by the user has four different chronological phases: 1. definition phase;

2. verification phase;

3. model instance creation phase;

4. solution phase.

## 2.1. Definition phase

Following the approach taken by other SM languages, BLOOMS allows the model builder to specify the model as a generic structure, i.e. as a collection of correlated genera belonging to the five predefined SM types. This level of abstraction is between the definition of all the model's details (elemental structure) and its hierarchical organization (modular structure).

Models are either defined from scratch or derived from other models through integration procedures.

Table 3  
Some available integration procedures

<table><tr><td>Name</td><td>Action</td></tr><tr><td>Delete_Node</td><td>Delete a selected genus (node) and all its reference arcs and if it occurs the other isolated genera (nodes).</td></tr><tr><td>Replace_in_arc</td><td>Replace the definitional dependence of a genus with the dependence to another genus.</td></tr><tr><td>Reuse</td><td>Use the output produced by a component of a model as input for another model.</td></tr><tr><td>Replace_attribute</td><td>Replace some features of the model with some features from another model.</td></tr><tr><td>Merge_P</td><td>Merge two or more primitive entity genera.</td></tr><tr><td>Merge_C</td><td>Merge two or more compound entity genera.</td></tr><tr><td>Merge_A</td><td>Merge two or more attribute genera.</td></tr><tr><td>Merge_F</td><td>Merge two or more function genera.</td></tr><tr><td>Extract_atomic_model</td><td>Extract a submodel which has only one genus at the highest rank.</td></tr></table>

An example of a model defined from scratch follows in the next subsection, while Table 3 reports a partial list of integration procedures with a brief description of the results they produce.

Before using these operations (procedures) the user activates the MODEL DATABASE module, which loads through its function model\_load the genus graph/s of the model/s to be modified, so as to obtain his target module.

## 2.2. Verification phase

In this phase the user checks the non violation of the SM core concepts and the syntactical correctness of the model by activating the function model\_verify embedded in the VERIFICATION module. To check the syntax of the model, model\_verify tests:

1. the coherence of the indexing functions;

2. the structure of the calling sequence;

3. the expressions of the rules in the function and test genera;

4. the calls to inherited methods;

5. the names of the variables.

When errors occur, these are reported to the user through the GUI with an indication of how to remedy them.

## 2.3. Model instance creation phase

In this phase the verified genus graph is passed to the BLOOMS COMPILER module to produce the C++ code for the genera of the model. This code together with the reference to external objects passed to the genera through inheritance is saved in a file. Then BLOOMS derives the modular structure so to obtain an “incompletely specified model” by using either an algorithm or assisting the user in its construction by hand. To this purpose advanced graphical tools are available.

As specified in [20], the OO features allow the meaning of the modules of the modular structure to be extended viewing them as sets sharing common “semantics” properties. These sets constitute the blocks (components) which may be used later in the integration processes.

To obtain a “completely specified model” BLOOMS has to enumerate and specify in detail the element-objects belonging to the genera. The enumeration is carried out when the objects are created, while the object’s specification is done when all its value fields, including the calling sequence segments, are filled. Object fields can be filled either by loading the data through the GUI or from internal/external databases.

![](/api/attachments/7VHHWUHE/fulltext/images/47dab5eb134cdd33aa8aefa6f7a97fe7c0af2c3bcba57bc522c7298d01cd86a2.jpg)  
Fig. 2. The solver window.

Model instances are visible to the user by the suffix .pty added to the model name. Their structure is made up of three segments. The first stores the objects of the model: elements, genera and modules. The second contains the C++ code, which activates the executable modules of the system. The information in this segment is permanent. The third block stores the inherited classes of the model together with their dummy objects created at run time and used for the management of the inheritance.

## 2.4. Solution phase

Model instances are solved when the user activates the SOLVER module through the GUI, see Fig. 2. Through the GUI he specifies the objective function defined by convention as a singleton function genus, the variables of the problem as variable attribute genera, the constraints as test genera. This option has the advantage that the user may define alternative objective functions and/or constraints and be able to solve different versions of the model only by modifying the solve window.

One of the functions embedded in the SOLVER module is to translate the model's output into the algorithm's input. The current implementation support the translation into either a MPS format file or a network format file. The network format file matches the required input for NLPNET [12] and RELAXT-III [3,4], which are respectively two specialized nonlinear and linear network codes included in the solver-base. The MPS format file for the SKP, [1–3], fully defined later, is constructed as follows:

\- The NAME section is filled with the model name, supplied by the user;

\- The ROWS section contains the objective function and the constraints' identifiers. The information about the identifiers of the constraints' expressions is derived by the model\_verify function and embedded into the test genera of the model. By convention the objective function name and its identifier N appear at the beginning of the ROWS section followed by the constraint names and their identifier: L for "less than", E for "equal" and G for "greater than". All the names are obtained from the element-objects. When the label is left blank the system writes the genus name for the objective function or the genus name followed by a progressive number for the constraints.

\- The COLUMNS section is composed of field sequences. The first expresses the $\langle Variable\_Name\rangle$ , then successively, for linear programming problems, $\langle Row\_Name\rangle$ and $\langle Coefficient\_Value\rangle$ follow.

\- The information to fill the <Variable\_Name> column is obtained from the compiler. It looks at the variable attribute element-objects and if labels are missing it retrieves them from the first called objects.

\- The information to fill the $\langle Row\_Name\rangle$ and $\langle Coefficient\_Value\rangle$ is obtained from the VERIFICATION and SOLVER modules. The first retrieves the information to select the attribute genus whose attribute element-objects are used as coefficients in the expressions either for the objective function or the constraints. Then SOLVER scans the test (function) element-objects until it finds a test (function) element-object calling the variable attribute element-object $\langle Variable\_Name\rangle$ . In $\langle Row\_Name\rangle$ the system writes the identifier corresponding to this test (function) element-object. The test (function) element-object calls some variables and their coefficients as determined by the calling sequence segments. Since VERIFICATION has already verified the expression in the test (function) genus, the system knows the attribute element-objects (coefficients) associated to the variables. Therefore, in $\langle Coefficient\_Value\rangle$ it writes the corresponding numerical values.

\- The information on the attribute genus corresponding to the right-hand side of the problem is retrieved from VERIFICATION. The RHS section is filled with the right-hand-side values retrieved from the attribute element-objects belonging to the right-hand-side attribute genus and called by the test element-objects. Row names are retrieved as above.

\- The BOUNDS section eventually uses the information derived from the variable attribute genus (Table 4).

The output file produced by the solver and visible by the suffix .out added to the model name can be handled by the user. In fact he or she can edit and print it. Moreover the values of the optimal solution, variables and constraints are passed back to the corresponding genera and element-objects, using the same information structures derived to write the MPS input file.

<table><tr><td colspan="3">Table 4The MPS File for the SKP solved with OSL</td></tr><tr><td colspan="3">NAME KNAPSACK</td></tr><tr><td colspan="3">ROWS</td></tr><tr><td>N</td><td>TOT_PROF</td><td></td></tr><tr><td>L</td><td>CAPACITY</td><td></td></tr><tr><td colspan="3">COLUMNS</td></tr><tr><td>INT</td><td>‘MARKER’</td><td>‘INTORG’</td></tr><tr><td>PENCIL</td><td>TOT_PROF 100.0</td><td>CAPACITY 5.0</td></tr><tr><td>W-BOTTLE</td><td>TOT_PROF 200.0</td><td>CAPACITY 10.0</td></tr><tr><td>MAP</td><td>TOT_PROF 50.0</td><td>CAPACITY 1.0</td></tr><tr><td>INT</td><td>‘MARKER’</td><td>‘INTEND’</td></tr><tr><td colspan="3">RHS</td></tr><tr><td>BVEQ</td><td>CAPACITY 14.0</td><td></td></tr><tr><td colspan="3">RANGES</td></tr><tr><td colspan="3">BOUNDS</td></tr><tr><td colspan="3">ENDDATA</td></tr></table>

## 2.5. An example of BLOOMS formulation from scratch

Here we show how a BLOOMS user formulates the SKP, to allow the reader to compare BLOOMS with AMPL and GAMS, see Table 1. The definition of the model is obtained at the genus graph level, which is the level of abstraction used by BLOOMS for the model formulation. Another example which shows how to deal with a recursive non-optimization model is given in Appendix A.

## 2.5.1. The knapsack problem

The steps followed by the hypothetical users are not far from the following descriptions:

Step 1. There is a potential list of items characterized by two attributes: profits and weights.

Using this list as the base for the model, the user through the GUI selects a primitive genus to represent the items, see Fig. 3. Since profits and weights are values associated with each item, the user selects two attribute genera definitionally dependent on primitive genus ITEMS.

The keyword iso, appearing in the calling sequence, indicates how these values are associated with the items. This expresses the isomorphic relation between the element objects created by the genera when the model instance is created, see Fig. 4.

![](/api/attachments/7VHHWUHE/fulltext/images/be74a46c9362fcf1f1f6194aad11728ffbad0f571155884862d9ab1d8b2cee0c.jpg)  
Fig. 3. Knapsack model building: Step 1a.

![](/api/attachments/7VHHWUHE/fulltext/images/65052d4262213d14e68b9028ae133e21d1f1f192177b1211ed81010917a33f10.jpg)  
Fig. 4. Knapsack model building: Step 1b.

![](/api/attachments/7VHHWUHE/fulltext/images/a166dafa4c4de6e67a63eeb71d36dd7e71874cadf1e853b2d4cde648a76a1e50.jpg)  
Fig. 5. Knapsack model building: Step 2.

![](/api/attachments/7VHHWUHE/fulltext/images/74c4663f9b794b349246789a9a1198e989ec36822f912377ff985117119f7995.jpg)  
Fig. 6. Knapsack model building: Step 3.

![](/api/attachments/7VHHWUHE/fulltext/images/14cd0948a87d8d06dc4decc2e4e42fffc8bcd1522cba4232697d0a1a9850836c.jpg)  
Fig. 7. Knapsack model building: Inheritance of methods.

Step 2. Check if there is a subset of these items which fits in the knapsack.

The user needs to specify the decision variable associated with each item, thus definitionally dependent on ITEMS, which assumes value 1 if the corresponding item is in the subset, zero otherwise. To check if this subset does not violate the knapsack capacity, the user defines a test genus CAPACITY\_TEST, definitionally dependent on WEIGHT and CHOOSE, respectively attribute and variable attribute genera. The keyword all appearing in CAPACITY\_TEST's calling sequence indicates that the rule expressed by the method Result among the Features of the genus-object needs all the elements created by WEIGHT and CHOOSE to compute its singleton value, see Fig. 5.

Step 3: Consider as optimal solution, the subset which maximizes the value of the profit function.

To terminate the definition of the model, the user has to define the objective function by selecting a function genus, called TOT\_PROFIT, and filling the related fields of the object genus as shown in Fig. 6.

However many OR/MS analysts like to formalize the SKP in an array notation, as indicated by the following problem:

$$
\min z = p ^ {\prime} x\tag{4}
$$

$$
\mathrm{s.t.} w ^ {\prime} x \leq w _ {0}\tag{5}
$$

$$
x = 0, 1,\tag{6}
$$

where $p, x, w$ are arrays of length $n$ and $p'x$ and $w'x$ indicate the scalar product. BLOOMS allows a compact formulation (in linear algebra sense) for the SKP. In fact the genus-objects PROFIT, CHOOSE and WEIGHT (by means of the property of object identity) can be called by references as whole objects in the methods of the genus-objects TOT\_PROFIT and CAPACITY\_TEST, as arguments of their function rules.

The rule appearing in the genus TOT\_PROFIT calls PROFIT and CHOOSE to compute the scalar product indicated by the symbol $\langle\ldots,\ldots\rangle$ . This is an alias operator for the method Compute defined in the inherited class Scalar Product, see Fig. 7. Differently from the other Figures, in Fig. 7 the attribute #Element shows its value 1. This means that the user is looking at the code of the genus TOT\_PROFIT after the model has been instanced. "1" says that there is only one element linked with the genus.

```cpp
Table 3
C++ header for ScalarProduct class

class ScalarProduct
{
    //Check if the arrays to multiply have equal length.
    //This is a private method the parameters of which are pointers
    //to two value_bearing classes.
    int CheckLength (value_bearing * First, value_bearing * Second);
    //References to the classes//carrying the arrays to multiply.
    value_bearing * First;
    value_bearing * Second;
    //Compute the scalar product.
    float Compute (value_bearing * First, value_bearing * Second);
public:
    //Following is the constructor of ScalarProduct. It receives
    //two references as input and puts them into the appropriate
    //attributes First and Second.
    ScalarProduct (value_bearing * InputA, value_bearing * InputB);
    //These three operators are defined in order to construct the
    //interface of the class. They use the private method Compute
    //and define the alias operator used in BLOOMS
    float operator, (char * Input);
    float operator < (char * Input);
    float operator > (char * Input);
}
```

The class ScalarProduct has two attributes and two internal methods: the arrays to multiply (First and Second), the method to check that the arrays are of equal length (Check-Length) and the method to compute the scalar product (Compute). The public methods of the class serve as interface for the internal methods: these define the syntax of the alias operator and the constructor for the class. The header of ScalarProduct is listed in Table 5.

The same above argument applied for the rule in TOT\_PROFIT is valid for the rule in CAPACITY\_TEST. Tables 6 and 7 show the BLOOMS formulation for the SKP and its modified notation. Expert users, who like to bypass the GUI, may write them directly in BLOOMS using a text editor.

Table 6  
SKP BLOOMS formulation  
```txt
Genus ITEMS Primitive Genus PROFIT Attribute
Features Call (ITEMS: iso)
Item_Name: string Features
Show Item_Name: p: real
    Assertions p > 0
    Show p, Assertions;
Genus WEIGHT Attribute Genus CHOOSE Attribute
Call (ITEMS: iso) Call (ITEMS: iso)
Features Features
w: real x: boolean
Assertions w > 0 Show x;
Show w, Assertions;
Genus TOT_PROFIT Function
Call (PROFIT: all; CHOOSE: all)
Features
Z: real is
Result := SUM[ITEMS.INDEX] p * x
Show Z, Result;
Genus CAPACITY_TEST Test
Call (WEIGHT: all; CHOOSE: all)
Features
C_test: boolean is
Result := SUM[ITEMS.INDEX] w * x <= W0
Show C_test, Result;
```

```vhdl
Table 7
SKP modified genera for the compact BLOOMS formulation

Genus TOT_PROFIT Function
Inherit ScalarProduct
Call (PROFIT: all; CHOOSE: all)
Features
Z: real is
Result := <PROFIT, CHOOSE>
Show Z, Result;

Genus CAPACITY_TEST Test
Inherit ScalarProduct
Call (WEIGHT: all; CHOOSE: all)
Features
C_test: boolean is
Result := <WEIGHT,CHOOSE> <= W0
Show C_test, Result;
```

## 3. Some implementational aspects of BLOOMS

A BLOOMS class is constructed as a collection of three declarations:

1. Class Header;

2. Object Features;

3. Public Methods.

The first declaration brings the information on the genus type and its definitional dependencies; the second describes the features of the element objects created by the class; and the third defines the interface of the genus class according to the OO principle of data hiding. The syntax is described in Table 8.

## 3.1. The implementation of BLOOMS classes

BLOOMS classes are implemented in C + + [43], although it is a “hybrid” OO language, for the following reasons:

\- C++ seems to have become the “standard” OO language;

```txt
Table 8
BLOOMS class syntax

Class Header
[Genus] <Class_Name> <SM_Type_Identifier>
    [call <Calling_Sequence>]
    [inherit <List_of_Class_Name>]

Object Features
Features
(methods and attributes)
(common to all types)
[<Object_Label>: string]
[#element: integer]
(for compound entity genera)
    Connect (<Class_Name, ..., Class_Name)
    [expression])
    Require <Expression>
(for attribute genera)
    Value_Label: <Value_Type>
    Assertions <Expression>
(for function genera)
    Require <Expression>
    Result <Expression>
(for test genera)
    Require <Expression>
    Result <Boolean_Expression>

Public Methods
Show <Feature_List>;
```

Table 9  
C++ implementation

<table><tr><td>Theory</td><td>Implementation</td></tr><tr><td>SM types</td><td>C++ classes</td></tr><tr><td>Genus classes</td><td>Genus-object instances of C++ genus classes</td></tr><tr><td>Element objects</td><td>Element-object instances of C++ element classes</td></tr><tr><td>Inherited methods</td><td>By object references</td></tr></table>

\- the compilers are available for a large variety of hardware platforms.

On the contrary, $C++$ is not able to manage multiple instancing of classes, i.e. a class cannot be an instance of another class. Since a straightforward implementation of BLOOMS as described in [18] is not possible, two different implementational choices have been considered:

1. Write a pre-compiler that takes as input the definition of the BLOOMS genus classes and returns as output the corresponding C++ code. The code is passed to the C++ compiler to generate executable code for these classes;

Table 10  
Methods and attributes defined in BLOOMS classes

<table><tr><td>Inherited methods and attributes</td><td>Methods and attributes defined in the class</td><td>Note</td></tr><tr><td colspan="3">GENERAL class</td></tr><tr><td rowspan="8">none</td><td>Label: string</td><td>Attribute. The label field can be filled by the user in order to identify objects.</td></tr><tr><td>Inherit_list: list of string</td><td>Attribute. This list contains the identifiers of the inherited classes.</td></tr><tr><td>Inherit</td><td>Manage inheritance. On the basis of information contained into Inherit_list it creates references to dummy objects to “fake” inheritance relationships between classes.</td></tr><tr><td>Belonging_Objects: list of Objects</td><td>Attribute. This list contains the references to the element-objects belonging to the genus. It is used to manage relationships between the genus and its objects.</td></tr><tr><td>Edit_Belonging_Objects: list of Objects</td><td>Manage the Belonging_Object list.</td></tr><tr><td>Count_Element</td><td>Count the number of element-objects instanced by the user.</td></tr><tr><td>#Element</td><td>Attribute. It shows the number of called elements.</td></tr><tr><td>Show (list of string)</td><td>Manage the definition of public methods.</td></tr><tr><td colspan="3">NOT_PRIMITIVE class</td></tr><tr><td rowspan="2">Label, Inherit_list,Inherit, Belonging_Objects, Edit_Belonging_Objects, Count_Element, #Element Show (from GENERAL).</td><td>Segment: list of Objects; Calling_Sequence: array of Segments</td><td>Attributes. The calling sequence is a data structure composed by of array of segments. Each segment is a list.</td></tr><tr><td>Call (Calling_Sequence)</td><td>Manage the Calling_Sequence data structure.</td></tr><tr><td colspan="3">VALUE_BEARING class</td></tr><tr><td>Label, Inherit_list,Inherit, Belonging_Objects, Edit_Belonging_Objects, Count_Element, #Element, Show (from GENERAL); Segment, Calling_Sequence, Call (from NOT_PRIMITIVE)</td><td>Value_Type:deferred; Upperbound: deferred; Lowerbound: deferred IsInRange(Value): boolean</td><td>Attributes. The definition of the Value_Type of the attribute is deferred to the created genus-object together with the definition of its bounds. Check that the value lies within the range specified by Upperbound and Lowerbound.</td></tr></table>

2. Define the genus classes as objects derived from pre-defined C++ classes, one for each SM type. For its simplicity from a software perspective, the second approach is followed, even if it introduces

Table 11  
Methods and Attributes defined in BLOOMS classes corresponding to SM types

<table><tr><td>Inherited methods and attributes</td><td>Methods and attributes defined in the class</td><td>Note</td></tr><tr><td colspan="3">PRIMITIVE class. This class corresponds to the “Primitive” SM type.</td></tr><tr><td>Label, Inherit_list,Inherit,Belonging_Objects,Edit_Belonging_Objects,Count_Element, #Element,Show (from GENERAL).</td><td>Create</td><td>Create the primitive entity genus-objects.</td></tr><tr><td colspan="3">COMPOUND class. This class corresponds to the “Compound” SM type.</td></tr><tr><td>Label, Inherit_list,Inherit,Belonging_Objects,Edit_Belonging_Objects,Count_Element, #ElementShow (from GENERAL);Segment,Calling_Sequence,Call(from NOT_PRIMITIVE).</td><td>CreateConnect(list of string[;Expression])</td><td>Create the compound entity genus-objects.List of strings contains labels of the genus-objects called by a compound entity genus.Connectuses information in the list and in the Calling_Sequence to define the connections in the compound entity element-objects.TheRequiremethod introduces the constraints defined by the user for the connections. It is used for complex indexing structures.</td></tr><tr><td colspan="3">ATTRIBUTE class. This class corresponds to the “Attribute” SM type.</td></tr><tr><td rowspan="2">Label, Inherit_list,Inherit,Belonging_Objects,Edit_Belonging_Objects,Count_Element, #ElementShow (from GENERAL);Segment,Calling_Sequence,Call(from NOT_PRIMITIVE);Value_Type, Upperbound,Lowerbound, IsInRange(from VALUE_BEARING)</td><td>Create</td><td>Create the attribute genus-objects.</td></tr><tr><td>Assertions(Expression)</td><td>Check if the value fields of the element-objects are correctly filled.</td></tr><tr><td colspan="3">FUNCTION class. This class corresponds to the “Function” SM type.</td></tr><tr><td rowspan="3">Label, Inherit_list,Inherit,Belonging_Objects,Edit_Belonging_Objects,Count_Element,#Element, Show(from GENERAL);Segment,Calling_Sequence,Call(from NOT_PRIMITIVE);Value_Type, Upperbound,Lowerbound, IsInRange(from VALUE_BEARING)</td><td>CreateResult(Expression)</td><td rowspan="2">Create the function genus-objects.Carry the expression used to compute the value field.Similar to theAssertionsmethod of ATTRIBUTE. Using IsIn-Range, it checks the correctness of the values used to evaluate the function rule.</td></tr><tr><td>Require(Expression)</td></tr><tr><td>Eval</td><td>Check if the expression of the methodResultis correct.Evaluate the expression using the current value of the element-objects.</td></tr><tr><td colspan="3">TEST class. This class corresponds to the “Test” SM type.</td></tr><tr><td colspan="3">This class is similar to FUNCTION class. However, the Eval method is implemented differently and the value field type is always boolean.</td></tr></table>

![](/api/attachments/7VHHWUHE/fulltext/images/4b660926136273ea2669a454f71d8a69325b8df644e9fb1125079eebe6ef9d11.jpg)  
Fig. 8. Class hierarchy.

some problems because we are forced to “fake” some aspects of OO, like the inheritance.

A parallel between the theory and the implementation is presented in Table 9. Here SM types, which are theoretically treated as metaclasses, are implemented as C++ classes, the genus classes as object instances of these classes, element-objects as instances of C++ element classes. Each C++ element class inherits from the corresponding C++ SM type class: as an example, the Primitive\_Element class necessary to create primitive element-objects inherits from the Primitive class, used to create primitive genus-objects. The inheritance among genus classes is implemented through object references, as discussed in Section 3.3.

The C++ class hierarchy related to the taxonomy presented in Table 2 is drawn in Fig. 8. The directions of the arrows go from sub-classes to classes. For a better understanding of the methods and attributes embedded in the classes two tables are provided. Table 10 illustrates the BLOOMS classes hidden to the user, while Table 11 presents the BLOOMS classes visible to the user and corresponding to the five SM types.

## 3.2. Indexing structure management

The BLOOMS philosophy pursues the achievement of a semi-automatic indexing. The process for the definition of the indexing structures is performed in three steps:

1. The first step concerns the definition of the “base indices” of the model. This is done by associating to each primitive entity genus a symbolic index corresponding to a list of elements: these have a unique ordering.

2. The second step concerns the definition of compound indexing structures, i.e. the indexing of all the genera having the calling sequence. At this stage there is a symbolic index associated with each genus, which is the alias for a tuple of indices. BLOOMS constructs these tuples by using the calling sequence methods. Therefore, if genus $G_{1}$ calls the genera $G_{2}$ and $G_{3}$ , its symbolic index $G_{1}$ . INDEX corresponds to the tuple $\langle G_{2}$ . INDEX, $G_{3}$ . INDEX $\rangle$ .

3. The third step concerns the definition of the complex relations among element-objects. These relations are stated by the calling sequence's clauses and specified by the Connect method.

In a completely specified model each element-object of a genus $G_{i}$ contains the actual values of its indexing tuple; moreover, it carries the method index\_value which establishes its order within the symbolic index associated to the genus. Therefore, a correspondence is set between the set of the values assumed by the symbolic index of the genus $G_{i}$ and the values assumed by the tuple of indices. Again, the calling sequence's clauses and the Connect method manage these correspondences.

To give an example, we consider the Classical Transportation Problem (CTM) as defined in $[23,18]$ . Here the main indexing structure is a sparse matrix corresponding to the links between plants and customers. In the first step, BLOOMS defines two symbolic indices connected to the genera PLANT and CUST:

Genus PLANT Primitive Features
Plant\_Name: string
Show Plant\_Name;

Genus CUST Primitive Features
Cust\_Name: string
Show Cust\_Name;

In the second step, the structure of the matrix is modeled through the compound entity genus LINK:

```txt
Genus LINK Compound
Call (PLANT: one; CUST: one)
Features
Link_Name: string
Connect (PLANT, CUST)
Show Link_Name, Connect;
```

The genus LINK calls PLANT and CUST with the modality expressed by clause one. This means that each element-object created by LINK calls one element of PLANT and one element of CUST.

When the third step is taken, and a model instance is created, the nth object of LINK has index values as represented in Table 12.

There the first line shows the methods of the object, the second line shows the symbolic indices corresponding to these methods, while in the third line i and j are numeric values corresponding to the element-objects of PLANT and CUST which characterizes the nth element of LINK. If the nth link is supposed to connect the second plant with the fourth customer, then i has to be set equal to 2 and j to 4. The Connect method in the LINK genus-objects carries information on the element-objects of PLANT and CUST tied by the element-objects of LINK.

The user may check a particular indexing structure by extending the Require method. For example, let us consider a set of links between plants and customers subject to an additional constraint: no plant can supply more than two customers. In this case the compound entity genus DOUBLE\_LINK has the following definition:

Genus DOUBLE\_LINK Compound

Call (PLANT: one; CUST: one)

Features

Link\_Name: string

Connect (PLANT, CUST)

Require Outdegree (PLANT) $< = 2$

Show Link\_Name, Connect, Require;

Outdegree is the identifier for a built-in function passed as parameter to the Require method. Outdegree computes the number of arcs connecting the ith plant with the related customers.

Table 12  
Indexing structure for element-objects belonging to LINK

<table><tr><td>index_value</td><td>1st Connect entry</td><td>2nd Connect entry</td></tr><tr><td>LINK.INDEX</td><td>PLANT.INDEX</td><td>CUST.INDEX</td></tr><tr><td>n</td><td>i</td><td>j</td></tr></table>

Moreover BLOOMS can perform iterated operations over the symbolic indices. In fact in our example the function genus, which expresses the objective function, is as follows:

```txt
Genus TOTAL_COST Function
Call (FLOW: all; COST: all)
Features
Z: real is
Result := SUM[LINK.INDEX] Cost * Flow
Show Z, Result;
```

SUM is done over all the elements of LINK, and in the above expression SUM[LINK.INDEX] Cost\*Flow corresponds to the algebraic expression $\sum_{i=1}^{n}\sum_{j=1}^{m}x_{ij}c_{ij}$ .

The supply constant is modeled as follows:

Genus T\_SUP Test

Call (FLOW: iso[SUP.INDEX]; SUP: iso)

Features

T\_Sup: boolean is

Result := SUM[CUST.INDEX]Flow <= Sup Show T\_Sup, Result;

and SUM is done over the symbolic index CUST.INDEX, corresponding to the index $j$ , leading the expression SUM[CUST.INDEX]Flow $<=$ Sup to be equivalent to the algebraic expression $\sum_{j=1}^{m} x_{ij} \leq \sup_i, i = 1, \ldots, n$

## 3.3. The inheritance of methods

Inheritance is one of the main features of OO. In fact there is not a comparative technique among the concepts of traditional programming. BLOOMS allows a genus class to inherit methods and attributes from:

1. other genus classes belonging to the same model or other models (“internal” inheritance);

Table 13  
Allowed inheritance relationships

<table><tr><td></td><td>P</td><td>C</td><td>A</td><td>F</td><td>T</td></tr><tr><td>P</td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>C</td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>A</td><td></td><td></td><td>X</td><td></td><td></td></tr><tr><td>F</td><td></td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>T</td><td></td><td></td><td></td><td>X</td><td>X</td></tr></table>

2. “external” classes, like mathematical classes, general library classes etc. (“external” inheritance).

Since BLOOMS follows the rules of SM, inheritance is not always permissible. As an example, a compound genus in not allowed to inherit from an attribute the methods managing the field value. Table 13 gives the allowed inheritance relationships among SM types (“X” indicates when it is possible).

It is clear that other constraints also apply when a genus inherits from an external class. For example compound entity genera cannot have mathematical function methods, therefore, they cannot inherit from a library of mathematical function classes.

Inheritance among genera which are definitionally dependent does not introduce cyclicity in the model schema. In fact, inheritance affects the methods and the attributes and these can be always thought of as members of external classes.

Inheritance is slightly more difficult to implement following the second approach of Section 3.1. Usually inheritance affects classes, and object inheritance (or delegation) is not allowed by many programming languages, C++ included [5]. Therefore, we have implemented the delegation through object references. To describe how this is done in BLOOMS we work out two examples for these two cases:

## (a) “Internal” inheritance

Let us consider again the CTM partially described in Section 3.2, and suppose that the user wishes to construct a link structure satisfying the following constraint: no plant can supply more than two customers and no customer can be supplied by more than two plants. Since the DOUBLE\_LINK genus satisfies only the first part of the constraint, it appears useful to redefine a new class which inherits DOUBLE\_LINK and extends its method. The new genus is named DOUBLE\_LINK\_2 and has the following definition:

Call (PLANT: one; CUST: one)

Inherit DOUBLE\_LINK

Require DOUBLE\_LINK.Require, Indegree (CUST) <= 2

where Indegree has a syntactical structure analogous to Outdegree.

Genus DOUBLE\_LINK\_2 is set to have an is a inheritance relation with DOUBLE\_LINK, and it shares its methods, unless they are modified, as in this case for the inherited Require method.

“Internal” inheritance is implemented as follows:

1. The Verification module recognizes the inheritance and search in the model base for the genus DOUBLE\_LINK. An error message is displayed if the genus is not found.

2. When the DOUBLE\_LINK\_2 genus-object is created in the model instance creation phase, the BLOOMS COMPILER also creates the genus-object DOUBLE\_LINK. Then the BLOOMS COMPILER sets a reference from DOUBLE\_LINK\_2 to DOUBLE\_LINK.

3. Each time the genus-object DOUBLE\_LINK\_2 is asked to execute the inherited method, it sends a message to DOUBLE\_LINK and asks it to execute its encapsulated method.

(b) “External” inheritance

An example of external inheritance has already been given in Section 2.5.1, where a function genus-object TOT\_PROFIT inherits the external class ScalarProduct which computes the scalar product of two arrays. For this example, “external” inheritance is implemented in the system as follows:

1. The “Verification” module interprets the inheritance and sets a flag for the inheriting genus TOT\_PROFIT.

2. When the model instance has to be created, the BLOOMS Compiler creates the genus-object TOT\_PROFIT and a dummy object d which encapsulates the methods defined in ScalarProduct. However the compiler sets a reference from TOT\_PROFIT to ScalarProduct.

3. During the execution of the model each time the genus-object TOT\_PROFIT has to be computed it sends a message to d to execute the methods encapsulated in it.

## 4. Summary and final remarks

The focus of this paper has been on the implementation issues of BLOOMS. We have chosen to omit many technical details, reported in companion technical reports, to point out why we believe that the SM-OO approach to modeling deserves to be pursued. This may become relevant in introducing many practitioners from the real word to OR/MS techniques.

BLOOMS was originally designed and partially implemented in EIFFEL [40]. The main reason for this choice lies in the “multiple instancing of classes”. Nevertheless, at the time we started the design and implementation of MODASS [22], we decided to move to C++ for the reasons expressed early in the paper.

Moreover the GUI is implemented in Visual Basic for MS-DOS/Windows operating systems and is currently under implementation for Unix operating systems. It may also be used as graphical interface for other SM languages with very few changes.

Some of the modules to check the syntax and to verify the coherence of the semantics have been implemented in standard C. Solvers are limited to few public domain codes available in OR/MS literature although the system has been designed to match solvers like Cplex [11], OSL [33] and MINOS [41].

![](/api/attachments/7VHHWUHE/fulltext/images/3438b6550b87f5a60da53639667a8b640162c7c6b55c2d7205e18f5e58a5e549.jpg)  
Fig. 9. Non-recursive rule.

![](/api/attachments/7VHHWUHE/fulltext/images/882193440f73f3e904f22a3569c57d11ba4ee12453c24993b3b1e164d3c67305.jpg)  
Fig. 10. Non-SM recursive rule.

As a partial goal, we are planning to make the system accessible through the Internet so to get reactions and comments from users, colleagues and other researchers in this area in order to improve the features that it offers. As ultimate goal, we would like to see our system interacting with users with a very little knowledge of OR/MS techniques to solve real world large scale problems.

## Acknowledgements

Support by 60% MURST funds is gratefully acknowledged. The authors wish to thank Professor Arthur M. Geoffrion for helpful comments and an anonymous referee for the suggestions received, which have improved the quality of the paper. All eventual existing errors must, however, be considered the sole responsibility of the authors.

## Appendix A. A recursive function model

Although BLOOMS, at this stage, focuses on mathematical programming models in this appendix, we show how a very simple recursive non-optimization model is treated.

Let us consider the function genus FACTORIAL indexed over k, which computes the factorial of a given integer $1 \leq n \leq k$ . The algebraic recursive formulation is:

$$
n! = \left\{ \begin{array}{l l} 1 & n = 1 \\ n \cdot (n - 1)! & \text { otherwise }. \end{array} \right.\tag{A.1}
$$

The corresponding non-recursive formulation is:

$$
n! = 1 \cdot 2 \dots n.\tag{A.2}
$$

The elemental graph for this non-recursive formulation is shown in Fig. 9.

If we try to compute the value assumed by the nth element of the recursive function using a direct approach, we state the following rule in the Features section of the function genus FACTORIAL (details of the model and parts of the function genus are omitted):

Features

fact: integer is

Result := if FACT.INDEX = 1 then 1 else FACTORIAL[INDEX - 1].fact \* FACT.INDEXShow fact;

Here we violate the 9th SM core concept [25], which states that definitional dependencies among elements belonging to the same genus are not allowed. The graph of elements is shown in Fig. 10.

A possible way to proceed is to transform the recursive function in its non-recursive representation; alternatively it is possible to follow the approach briefly described below, implemented in BLOOMS. At evaluation time, a constant value replaces the value corresponding to the term FACTORIAL[INDEX - 1].fact, thus the function value modifies as:

$$
\text { FACTORIAL } (n) \cdot \text { value } := c (n - 1) * n.
$$

![](/api/attachments/7VHHWUHE/fulltext/images/8cbc374cf7f43f7784d537eb484de9b803981532120cba8f4fe2db64bf3e76c1.jpg)  
Fig. 11. Constant substitution.

This approach requires that the evaluation is done by indexing order, i.e. the $(n-1)$ th element is evaluated before the nth element. The elemental graph for this model is shown in Fig. 11. BLOOMS gives the possibility to define recursive functions also through ad hoc methods. How the methods are defined is not analyzed here; the interested reader is directed to [18,20].

## References

[1] A. Andronico, L. Cossa, M. Gagliardi and C. Spera, An Object Oriented Approach to a Model Management System: Characteristics and Examples, in: AUTOMATION, Atti 36 Convegno Nazionale ANIPLA, 16–18 November 1992, Genoa, Vol. 3, pages 334–349 (Bottaro e Pirella, 1992).

[2] Ashon-Tate, 20101 Hamilton Ave., Torrance, CA 90502, Framework III.

[3] D.P. Bertsekas and P. Tseng, RELAX: A Computer Code for Minimum Cost Network Flow Problems, Annals of Operations Research 13 (1988) 127–190.

[4] D.P. Bertsekas and P. Tseng, RELAXT-III: A New and Improved Version of the RELAX Code, Laboratory for Information and Decision Systems Report p-1900, M.I.T., Cambridge, MA (1990).

[5] G. Blair, J. Gallagher, D. Hutchison and D. Shepherd, Object-Oriented Languages, Systems and Applications (Pitman Publishing, 1991).

[6] A. Brooke, D. Kendrick and E. Meeraus, GAMS: A User's Guide (The Scientific Press, Redwood City, CA, USA, 1988).

[7] K. Chari and T. Sen, A Graphical Approach to Structured Modeling: Model Graphs and Model Instantiations, Technical Report, Department of Accounting, Virginia Tech., Blacksburg, VA (1993).

[8] K. Chari and T. Sen, GBMS/SM: A Graphical Modeling Environment, Technical Report, Department of Information and Decision Sciences, James Madison University, Harrisonburg, VA (1995).

[9] K. Chari and T. Sen, A Graph Based Modeling System for Structured Modeling, Technical report, Department of Information and Decision Sciences, James Madison University, Harrisonburg, VA (1995).

[10] S. Chari and R. Krishnan, Toward a Logical Reconstruction of Structured Modeling, Decision Support Systems 10, No. 3 (1993) 301–317.

[11] Cplex Optimization, Inc., Using the Cplex Callable Library (1994).

[12] R.S. Dembo, NLPNET User's Guide, Working Paper 81, School of Organization and Management, Yale University (1983).

[13] R. Fourer, Modeling Language versus Matrix Generators for Linear Programming, ACM Transactions on Mathematical Software 9 (1983) 143–183.

[14] R. Fourer, Algebraic Modeling Language for Mathematical Programming: A Tutorial, in: TIMS/ORSA Joint National Meeting, Chicago (May 1993).

[15] R. Fourer and D.M. Gay, Expressing Special Structures in an Algebraic Modeling Language for Mathematical Programming, ORSA Journal on Computing 7, No. 2 (1995) 166–190.

[16] R. Fourer, D.M. Gay and B.W. Kernighan, A Mathematical Programming Language, Management Science 36 (1990) 519–554.

[17] R. Fourer, D.M. Gay and B.W. Kernighan, AMPL: A Modeling Language for Mathematical Programming, Student Edition (The Scientific Press, Redwood City, CA, USA, 1993).

[18] M. Gagliardi and C. Spera, Blooms: A Basic Language Object Oriented for Modeling Systems, Working Paper 10, Department of Quantitative Methods, University of Siena, Piazza S. Francesco 17, 53100 Siena, Italy (1994). Revised version December 1995, submitted for publication.

[19] M. Gagliardi and C. Spera, Some New Results in Model Integration, in: J.F. Nunamaker and R.H. Sprague, Eds., Proceedings of the XXVIII Annual Hawaii International Conference on System Sciences, Vol. 3, pages 398–407 (IEEE Press, Los Alamitos, CA, USA, January 1995).

[20] M. Gagliardi and C. Spera, The Syntax of Blooms, Part I: Introduction, Working Paper 11, Department of Quantitative Methods, University of Siena, Piazza S. Francesco 17, 53100 Siena, Italy (1995). Revised version July 1995.

[21] M. Gagliardi and C. Spera, Toward a Formal Theory of Model Integration, in: I. Maros and G. Mitra, Eds., Applied Mathematical Programming and Modeling II, No. 58 in Annals of Operations Research, 405–440 (Baltzer Publishing, 1995).

[22] M. Gagliardi and C. Spera, MODASS: A Modeling System to Manage Structured Models, forthcoming in Proceedings of the First INFORMS Conference on Information Systems and Technology, Washington, D.C. (May 5–8, 1996).

[23] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science 33 (1987) 547–589.

[24] A.M. Geoffrion, Computer-Based Modeling Environments, European Journal of Operational Research 41 (July 1989) 33–43.

[25] A.M. Geoffrion, The Formal Aspects of Structured Modeling, Operations Research 37 (1989) 30–51.

[26] A.M. Geoffrion, FW/SM: A Prototype Structured Modeling Environment, Management Science 37 (1991) 1513–1538.

[27] A.M. Geoffrion, Indexing in Modeling Languages for Mathematical Programming, Management Science 38, No. 3 (1992) 325–344.

[28] A.M. Geoffrion, The SML Language for Structured Modeling: Levels 1 and 2, Operations Research 40, No. 1 (1992) 38–57.

[29] A.M. Geoffrion, The SML Language for Structured Modeling: Levels 3 and 4, Operations Research 40, No. 1 (1992) 58–75.

[30] A.M. Geoffrion, Structured Modeling: Survey and Future Research Directions, ORSA CSTS Newsletter 15, No. 1 (1994).

[31] A.M. Geoffrion and S. Maturana, Generating Optimization-Based Decision Support Systems, in: J.F. Nunamaker and R.H. Sprague, Eds., Proceedings of the XXVIII Annual Hawaii International Conference on System Sciences, Vol. 3, pages 439–448 (IEEE Press, Los Alamitos, CA, USA, January 1995).

[32] S. Hamacher, P. Dejax and L. Lustosa, A Diagram Representation for Conceptual Models of Operations Research Problems, to appear in International Transactions of Operational Research). Also available as technical memorandum 07/93, Centro Técnico Científico, Departamento de Engenharia Industrial, Pontifícia Universidade Católica do Rio de Janeiro, Brazil.

[33] M.S. Hung, W.O. Rom and A.D. Waren, OSL: Optimization with IBM OSL (Boyd and Fraser, 1994).

[34] C. Jones, An Integrated Modeling Environment based on Attributed Graphs and Graph Grammar, Decision Support System 10, No. 3 (1993) 255–277.

[35] C.V. Jones, Attributed Graphs, Graph-Grammars, and Structured Modeling, in: B. Shetty, H.K. Bhargava and K. Krishnan, Eds., Model Management in Operations Research, No. 38 in Annals of Operations Research, 281–324 (Baltzer Publishing, 1992).

[36] C.V. Jones, Development in Graph-Based Modeling for Decision Support, Decision Support Systems 13 (1995) 61–74.

[37] M. Lenard, An Object-Oriented Approach to Model Management, Decision Support Systems 9 (January 1993) 67–73.

[38] S. Lin, Subscript Free Modeling Languages: An Improvement Basis for Integrating Models and Data in Decision Support Systems, Ph.D. Thesis, Department of Decision and Information Systems, Arizona State University (1993).

[39] S.V. Maturana, Issues in the Design of Modeling Languages for Mathematical Programming, European Journal of Operational Research 72, No. 2 (1994).

[40] B. Meyer, Object Oriented Software Construction, (Prentice Hall International Series in Computer Science, 1988).

[41] B.A. Murtagh and M.A. Saunders, MINOS 5.1 User's Guide, Report sol 83-20R, December 1983, revised January 1987, Stanford University (1987).

[42] L. Neustadter, Simplifying SML: A Proposal, Informal Note, Anderson School of Management, UCLA, Los Angeles, CA (1992).

[43] B. Stoustrup, C++ Programming Language (Addison-Wesley, 1986).

[44] F. Vicuña, Semantic Formalization in Mathematical Modeling Languages, Ph.D. Thesis, Computer Science Department, UCLA (1990) (WMSI Reprint 255).

![](/api/attachments/7VHHWUHE/fulltext/images/5ec2d0d40a6a8028fef19dd6020c01520d2c3489ca12253b5e9be97b14d50a52.jpg)

Marco Gagliardi is a Ph.D. candidate in Operations Research at the University of Rome “La Sapienza”. He received his Laurea degree in Statistics from the University of Siena. His research works appear in Annals of Operation Research, European Journal of Operational Research and International Journal of Computers and Industrial Engineering. His current research interests include the development of model management systems and particularly the

object oriented approach to this field, and the definition of decision support systems based on natural language.

![](/api/attachments/7VHHWUHE/fulltext/images/f0f2660f1f8d22ea2164d6f18b231175bba157de67ebc9ae2ce4cc0a6e7a10c4.jpg)

Cosimo Spera is an assistant professor of Operations Research at the Department of Quantitative Methods, University of Siena. His research interests include the definition of object oriented languages for mathematical programming problems and theoretical and empirical analysis of algorithms. His current work appears in Mathematical Programming B, Computational Economics Annals of Operation Research, European Journal of Operational Research and International Journal of Computers and Industrial Engineering.
