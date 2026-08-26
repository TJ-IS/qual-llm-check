---
otero_id: 17380
otero_key: "3FCFVFWG"
title: "Independence and mappings in model-based decision support systems"
authors: "Richard G. Ramirez; Chee Ching; Robert D. St. Louis"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90067-d"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Independence and mappings in model-based decision support systems

Richard G. Ramirez

Iowa State University, Ames IA, USA

Chee Ching and Robert D. St. Louis
Arizona State University, Tempe AZ, USA

Independence of applications from logical and physical data structures is one of the cornerstones of modern database systems. Similar concepts may be applied to model management in a decision support system (DSS) to facilitate model portability, sharing, and multi-purpose application. In this paper we define the concepts of model/data and model/solver independence, present an extended architecture for DSS, and show its implementation. The architecture supports separate solver, model, and data bases and uses mappings to integrate them. Computationally-equivalent solvers support portability, while non-computationally-equivalent solvers allow a model to be used without modification for different purposes (what if, goal seeking, optimization). The implementation integrates an SQL database system with a mathematical modeling language.

Keywords: Model management; Linear programming; Data independence; Structured modeling; Decision support systems

![](/api/attachments/3FCFVFWG/fulltext/images/aeb37e88e4b7a6a013f37a316210f50c8b0c560ef2b2f0c76d3a389ed4b9364d.jpg)

Chee Ching is an Assistant Professor of Decision & Information Systems in the College of Business at Arizona State University. She received her Ph.D. degree from Purdue University in 1988. Her research interests are organizational computing and model management systems and has published research on coordination and organizational learning, and distributed decision making.

Correspondence to: Dr. Richard G. Ramirez, College of Business, Iowa State University, Ames, IA 50011-2065, USA.

## 1. Introduction

A typical implementation of a decision support system (DSS) is a single package that integrates the functionality of the three subsystems in the traditional framework for DSS: Database, model base, and user interface or dialog. Popular systems such as Lotus 1-2-3 and IFPS use this approach. Users learn a single language and need not be aware of the DSS internals. This approach is very effective in many applications, particularly those developed from scratch or involving a single user.

As decision problems increase in complexity, the single-package approach becomes less effective and the DSS must support the data compo-

![](/api/attachments/3FCFVFWG/fulltext/images/d26c2dca29589a2c6e7348c979249e2417c84a4741b2da307cbaf2613e368ba6.jpg)

Richard G. Ramirez is an Assistant Professor of Information Systems at Iowa State University. He received his Ph.D degree from Texas A&M in 1986. His current research interests are the integration of mathematical programming languages and databases for decision support systems. He has published research on relational views and expert databases. He is a member of ACM, IEEE Computer Society and TIMS.

![](/api/attachments/3FCFVFWG/fulltext/images/f0e9da49ad57e2d64f0441d1cdd746b241681c7d31a0f8e975178e4c3bbbbbee.jpg)

Robert D. St. Louis is an Associate Professor of Decision & Information Systems in the College of Business at Arizona State University. He received his Ph.D degree from Purdue University in 1912. Dr. St. Louis currently is conducting research in the areas of productivity measurement, MIS design and DSS design. He has published articles in a variety of journals, including the Academy of Management Journal, Industrial and Labor Relations Review, and the Journal of Human Resources.

nent as a separate system, so that DSS applications now run concurrently with 'pure' database applications. Many databases contain a large number of data files, some of them very large, and users increasingly need to access corporate data and share results with other users and applications. Commercial systems respond to this need by providing interfaces to the more popular DBMSs, such as 1-2-3 links to ORACLE, INFORMIX, and dBase IV, SAS interfaces to IMS and DB2, and IFPS interfaces to ORACLE. This approach has the advantage of bringing to the DSS all the capabilities of a generalized database management system. Note, however, that most of these interfaces do little other than upload and download data, and the DSS must still include the data management subsystem.

As important as shared access and full DBMS functionality are, the separation of the data component from a DSS has far more important consequences for DSS researchers and users. Since the DSS no longer 'owns' the database, interfaces (or mappings) must be designed to relate the dialog and model components to the database. Bonczek et al. [2] introduced three interfaces: The user/model interface, the model/data interface, and the user/data interface. Sprague and Carlson [20] identified model/data and model/dialog interfaces. These interfaces were, however, proposed as part of a more general framework and did not provide enough guidelines for implementation. Liang [14] proposed model/data, schema/model, and model/tool 'links' in more detail. He used an "external model schema" to define a model's inputs and outputs. Inputs are described using a relational table with two columns: Model name and "input" variable. A similar table defines outputs. By consistently using the same names in models and database tables, it is possible to map model variables to database tables and columns.

A distinction is made between a model (or model schema) and the data values that instantiate elements in the model such as coefficients, parameters, and variables. A model together with these data values is a model instance. The data values are part of a dataset stored as a collection of tables or files in a database. The separation of model and dataset specifications is referred to model/data independence $[9,3,16]$ . We propose the notion of mappings to allow models to be reused without change with multiple datasets, possibly having different file formats, and also allow a dataset to be used with multiple models and computer programs. Models can be more easily integrated because the outputs of one model can become the inputs of another without changing any model specifications. Different levels of model/data independence exist. We characterize them as value, dimension, and data structure independence in section 2.

We show how the concept of independence is carried over to solvers. A solver is a computational procedure (e.g., a computer program) used to apply the model to some dataset. In systems with little or no independence such as spreadsheet software, the program becomes the model and the model becomes the program. Because programs must be updated continuously to reflect current assumptions and obtain new results, the program's code often replaces other formulations of the model as a communication tool. It is not uncommon in practice to find discussion about the model being made by looking at the program's listing, and not at an algebraic or graphical representation. This situation forces modelers and users to become 'programmers' and to depend on a particular software package. Such dependence limits model sharing to those users having access to the same package, and model integration to models written using the same package. A higher level of model/solver independence allows a model to be used for different purposes without changing the model representation. The same model may be used in optimization mode to estimate the 'best' production schedule for a factory, in "what-if" mode to determine the effect of specific scheduling decisions, and in "goal-seeking" mode to determine the necessary actions to reach predetermined production goals. These and other modes may be necessary in a single session, as the decision maker tries to understand the situation in the real world and explores alternatives.

This paper presents the data and algebraic management system (DAMS) that implements model/data and model/solver independence. Flexible mappings between solvers, models, and datasets are defined. DAMS is built on top of the INGRES relational database system and provides model and data management facilities for a DSS. DAMS supports the SM/DB modeling language and a superset of SQL to provide model and data management capabilities.

The following section defines model/data and model/solver independence. The DAMS system is introduced in section 3, and the SM/DB language for modeling is described in section 4. In section 5 the differences between model definitions in SM/DB and SML [8,11] are briefly described. Finally, we conclude the paper and discuss further research directions in section 6.

## 2. Model independence from data and solvers

A model representation is a computer-readable formalization of a user's problem [after 13]. Models have different representations according to their use. Our use of the term corresponds to the modeler's form of Fourier [6]. This form is meant to be used by people and must be must be understandable, concise, general, and symbolic [6]. A model representation includes entities such as variables, constants, parameters, and coefficients. The solver's form (or algorithm's form), on the other hand, is convenient (to the solver) rather than understandable, redundant rather than concise, specific rather than general, and numeric rather than symbolic. The solver's form should be obtainable by a translation process that instantiates entities in the modeler's form with values stored in a dataset.

Independence from actual data and solver separates the modeler's form from the solver's form. In this section, we first discuss model/data independence giving the necessary conditions and illustrate using algebraic notation for a linear program. Second, we discuss model/solver independence, giving the necessary conditions and illustrating them with examples from a few popular modeling languages.

## 2.1. Model / data independence

In its simplest form, model/data independence means that data can be stored in files external to the model. With the exception of spreadsheet software such as Lotus 1-2-3 and EXCEL, most modeling software provides this simple form of model/data independence, allowing the data to reside in either an internal file (managed by the modeling system), an external file (managed by the operating system), or files in a database system such as DB2 or ORACLE. Unfortunately, most modeling software requires that the data files be designed specifically for the model being processed, and thereby impose constraints on the format of the files. For example, a model for sales commissions may require a 12-month sales history to be stored as 12 values per record. Alternatives such as one record per month or one file per month are not allowed or require modifying the model representation. This is a very limited form of model data independence.

## 2.2. Sufficient conditions for model / data independence

We define model/data independence by postulating value independence, dimension independence, and data structure independence as sufficient conditions. The first two are adapted from Geoffrion [9]. If these conditions are satisfied, then any dataset in a DSS may be modified or replaced without affecting the model representation, and the model representation can be changed without affecting the dataset.

Value independence This condition states that the data values for a variable or a constant can be changed without affecting the model representation. In a model to compute student grades, value independence implies that the names of the students, the assignment scores of the students, and the weighting of the students' assignment scores can be changed without affecting the model representation.

Dimension independence This condition states that the number of variables and the number of values a variable takes on can be changed without affecting the model representation. In the grade book example, dimension independence implies that the number of students and the number of assignments can be changed arbitrarily without having to change the model.

Data Structure Independence, the third condition, requires the following:

(1) Separate specification of names and types Variable names and data type (e.g., integer, decimal) of entities in the model can be different from the ones in the dataset. A mixed integer programming model may specify some of its variables as integer, but all variables may be stored as character strings. It is possible that the conversion between data types may cause some integrity problems when the model is solved. However, this condition stipulates that models should not dictate the storage form of data values for model/data independence to exist.

(2) Separate specification of logical record and file structures The model representation imposes no constraints on the format of the files in the database. As a consequence, the record structure for an entity in the model can be very different from its counterpart in the dataset. A matrix in a model may be stored in the database using a single record for the entire matrix, a record for each row of the matrix, or a record for each element of the matrix.

(3) Separate specification of base entities Entities in the model do not necessarily correspond to physically stored ('base') entities in the database. Values of entities in the model may come from 'virtual' records generated at run time. For example, entities in the model can be obtained by accumulating values from multiple records, such as total product sales from individual invoices.

## 2.3. An illustration of model / data independence

The following examples show algebraic representations of a model with varying degrees of model/data independence.

No model / data independence No separate dataset exists. The model representation combines the model and specific data values. The dataset cannot be modified without also changing the model representation.

$$
\begin{array}{l l} \max & Z = 3 x + 5 y, \\ \text { s.t. } & 5 x + 2 y \leq 1 2, \\ & 7 x - 3 y \leq 1 5, \\ & x, y \geq 0. \end{array}
$$

Value independence only The model and the dataset exist separately. The dataset can be modified without affecting the model representation. However, the dimensions of the model are restricted to the limits shown in the model representation, i.e., only two variables and two constraints.

$$
\begin{array}{l l} \max & Z = c _ {1} x _ {1} + c _ {2} x _ {2}, \\ \text {s.t} & a _ {1 1} x _ {1} + a _ {1 2} x _ {2} \leq b _ {1}, \\ & a _ {2 1} x _ {1} + a _ {2 2} x _ {2} \leq b _ {2}, \\ & x _ {1}, x _ {2} \geq 0, \\ \boldsymbol {c} = \binom {3} {5}, \quad \boldsymbol {a} = \left( \begin{array}{c c} 5 & 2 \\ 7 & - 3 \end{array} \right), \quad \boldsymbol {b} = \binom {1 2} {1 5}, \quad \boldsymbol {x} = \binom {?} {?} \end{array}
$$

Dimension and value independence The model representation exists separately from the dataset and allows an arbitrary number of variables and constraints. Although the dataset is similar to the previous case, additional variables and constraints can be added (or dropped) without having to change the model representation. The representation in this example is fully-dimension independent since there can be an arbitrary number of both variables and constraints.

$$
\begin{array}{l l} \max & \sum_ {j = 1} ^ {n} c _ {j} x _ {j}, \\ \text {s.t.} & \sum_ {j = 1} ^ {n} a _ {i j} x _ {j} \leq b _ {i}, \quad i = 1, \ldots , m, \\ & x _ {1}, x _ {2}, \ldots , x _ {n} \geq 0, \\ \boldsymbol {c} = \binom {3} {5}, \quad \boldsymbol {a} = \left( \begin{array}{c c} 5 & 2 \\ 7 & - 3 \end{array} \right), \quad \boldsymbol {b} = \binom {1 2} {1 5}, \quad \boldsymbol {x} = \binom {?} {?} \end{array}
$$

Data structure independence This condition of independence allows any file format for storing the dataset. The model representation and data in these examples are the same as for dimension and value independence, only the file formats used for the dataset vary. A model representation that explicitly or implicitly requires a fixed format fails to satisfy data structure independence.

(1) Store each vector and matrix in a separate file.

<table><tr><td>c</td><td>Column 1</td><td>Column 2</td><td>b</td></tr><tr><td>3</td><td>5</td><td>2</td><td>12</td></tr><tr><td>5</td><td>7</td><td>-3</td><td>15</td></tr></table>

(2) Store all vectors and matrices in a single file.

<table><tr><td>Vector</td><td>Column 1</td><td>Column 2</td></tr><tr><td>c</td><td>3</td><td></td></tr><tr><td>c</td><td>5</td><td></td></tr><tr><td>a</td><td>5</td><td>2</td></tr><tr><td>a</td><td>7</td><td>-3</td></tr><tr><td>b</td><td>12</td><td></td></tr><tr><td>b</td><td>15</td><td></td></tr></table>

(3) Store vectors c and b together in one file. Store matrix a in a separate file, one element per record with explicit subscripting.

<table><tr><td>Vector</td><td>Value</td></tr><tr><td>c</td><td>3</td></tr><tr><td>c</td><td>5</td></tr><tr><td>b</td><td>12</td></tr><tr><td>b</td><td>15</td></tr></table>

Matrix a

<table><tr><td>Row</td><td>Column</td><td>Value</td></tr><tr><td>1</td><td>1</td><td>5</td></tr><tr><td>1</td><td>2</td><td>2</td></tr><tr><td>2</td><td>1</td><td>7</td></tr><tr><td>2</td><td>2</td><td>-3</td></tr></table>

## 2.4. Model / solver independence

A solver is a computer program in a language suitable for direct execution, or execution after automatic compilation, interpretation, and/or linking. Two solvers are computationally equivalent if they provide essentially the same results and allow one to substitute for the other. Solvers that are strongly computationally equivalent can be substituted for one another transparently to the user. For example, the new release of a solver may have a faster algorithm for matrix inversion but still provide identical numerical results. Or a solver may run on a Cray supercomputer using floating-point vector processing, while an otherwise identical version may run on an IBM PC using software emulation for floating point computations. Solvers that are strongly computationally equivalent may produce results that differ in numeric precision. In practice, many solvers are weakly computationally equivalent, and obtain results that are similar in purpose but not in form. For example, SAS/OR, LINDO, and MPSX all solve linear programming problems represented in the MPS format but do not provide outputs for exactly the same variables and their listings are very different in form.

Model/solver independence allows a model instance to be processed without modification using solvers that are not necessarily computationally equivalent. This facilitates model portability, sharing and multi-purpose application.

Typical purposes are what-if (or “evaluation”), goal-seeking, simulation, optimization, and others. We postulate selection, purpose, and representation independence as sufficient conditions for model/solver independence. If these conditions exist, then the solver may be modified or replaced without affecting the model, and the model may be fully utilized with any given set of solvers.

Representation independence This condition states that the model representation cannot be affected by changes in the solver's code. It requires the model representation to be separated from the solver, and makes it possible to modify the solver's code in any manner without affecting the model representation.

Selection independence This condition states that the model representation imposes no constraints on the choice of the solver. This makes it possible to process the model using any one of a collection of solvers, choosing the more appropriate to the particular situation.

Purpose independence This condition states that the model representation imposes no constraints on the “direction of computation” by describing relationships among model elements rather than computational steps. This makes it possible to process the model in any feasible mode that is useful to the decision maker.

Representation independence requires solvers and models to be represented and manipulated as two different entities. Changes made to the solver should not necessarily require a change in the model.

Selection independence extends representation independence by allowing multiple solvers for the same model. The model representation may not, implicitly or explicitly, require a particular solver. Note that representation independence alone is not enough to allow a substitution of solvers that are not strongly-computationally equivalent, since a model may still require a specific solver to be used.

Purpose independence allows users to explore relationships among model elements in multiple modes such as “what-if”, “goal-seeking”, or “optimization” provided the requisite data and solvers exist. Purpose independence relates to the concept that a model representation should not specify the time of instantiation of variables and parameters. That is, it should not classify its entities as being part of input or output subsets. An entity is in the input subset if it must be instantiated before the solver can be used to process a model instance. The output subset is formed by those entities that are instantiated as a result of processing the model instance with a solver.

```txt
DOUBLE PRECISION P, F, I
100 READ (INPUT, *, END = 900) F, I, N
P = PRESVAL (F, I, N)
PRINT P
GO TO 100
900 STOP
END
DOUBLE PRECISION FUNCTION PRES-
VAL (F, I, N)
DOUBLE PRECISION F, I
PRESVAL = F/(1 + I) * * N
RETURN
END
```

## 2.5. An illustration of model / solver independence

We first illustrate model/solver independence with dedicated modeling systems written in Fortran and similar programming languages. These systems make no attempt to explicitly separate model and solver. We show how, statements in the solver for functions such as reading external data, printing reports, displaying results on the screen, or controlling the flow of execution, prevent the solver from adequately representing the model. We then discuss two levels of modeling systems that include packages such as SAS and SPSS and “executable modeling languages” such as GAMS and IFPS. We show that even in this cases the amount of information related to computer execution detracts considerably from a straightforward model specification.

Modeling with programming languages Conventional programming languages make no distinction between the notions of model and solver. Consider a financial model to obtain the present value of a future payment, with the following algebraic formulation: $P = F/(1 + i)^{n}$ where P is the present value, F is the future payment in dollars, i is the annual interest rate (a percentage), and n is the number of years. Consider now the following Fortran program to describe and solve the model.

DOUBLE PRECISION P, F, I, DENOM

READ F, I, N

DENOM = (1 + I) \* \* N

$\mathbf{P} = \mathbf{F} / \mathbf{DENOM}$

PRINT P

END

In this example there is no separate representation of the model being manipulated. If the statement $DENOM = (1 + I) * * N$ is changed to $DENOM = (1 + I / 100.0) * * N$ (to allow percentages to be typed as integer), the model representation has changed. Because there is no separate model representation, there also is no choice with respect to the solver, and even the uses of the model are limited. The solver can only compute the value of P given F, I and N. It is not possible to use this model representation to compute the value for I given values for P, F and N. This example shows no model/solver independence: None of the necessary conditions being satisfied.

Modeling with subroutines Subprogram facilities may be used in conventional programming languages to isolate the model specification from other statements and provide representation independence. The following Fortran program uses a function subprogram to describe the present-value model while the main program deals with reading and printing data. The program also allows an arbitrary number of present-value problems to be solved.

Although the model specification appears in a separate subroutine, there is still no model representation apart from the code of the subroutine. For simple models such as this one, the subroutine code may serve as the model representation. For models of realistic complexity, the code becomes so convoluted and difficult to follow that the model representation is lost. This is the case for subroutine libraries such as IMSL and IBM's OSL. Such libraries provide solvers for commonly-used models, while leaving the coding of input-output routines and other environmental procedures to the users. In practice, these libraries cannot be used as model representations at all and their vendors do not offer them as such.

Using subprograms to represent models also fails to provide purpose independence since the “direction of computing” is predefined. Consequently, the solver still can only compute the value of P given F, I and N. It is not yet possible to use the model to compute the value for I given P, F and N.

High level languages. High-level languages provide a higher degree of model/solver independence than conventional programming languages. These languages attempt to provide a model specification as simple as possible, and also to require minimal programming knowledge on the part of the user. Consider for example the regression model $Y_{i} = \beta_{0} + \beta_{1} X_{1} + \beta_{2} X_{2} + \cdots + \beta_{4} X_{4} + \epsilon_{i}$ and the SAS statements that compute the $\beta$ coefficients for the ‘best’ subset of the X’s.

DATA;

INPUT Y X1 X2 X3 X4;

CARDS;

10 12 45 67 49

12 10 37 60 92

PROC STEPWISE;
MODEL Y = X1 X2 X3 X4/forward;

The forward specification indicates the variable selection method that will be used to obtain the 'best' subset of X's. In addition to forward, SAS provides backward, stepwise, maxr, and minr. Each variable selection method is a distinct solver.

Some separation between models and solvers is achieved in high-level languages. Unfortunately, solver choices are limited to the subroutines available in the system, typically only one for each possible case. Moreover, although the model specification appears as a separate statement, there is no model representation apart from the language statements (the SAS code in the example) that very often include input and output options that are not part of the model.

Modeling languages Modeling languages, such as GAMS and IFPS, attempt to separate the model from the solver and thereby achieve some purpose independence, i.e., they do not predefine the direction of computation. Modeling languages differ from “high-level languages” in that they attempt to provide a complete description of the model rather than just simplify the programming task. In GAMS the user defines a model as a collection of “equations”, with each equation defined on some “variables”. To solve a model, the user explicitly states both the model and the “solution procedure” (i.e., the solver) to be used. For example, the following statements define a transportation model (variable and other definitions have been omitted for brevity).

(variable, set, and parameter definitions)

EQUATIONS

EQUATIONS
COST the objective function
SUPPLY(I) supply from plant I
DEMAND(J) demand at location J
COST..Z = E = SUM((I, J), C(I, J) \* X(I, J));
SUPPLY(I)..SUM(J, X(I, J)) = L = A(I);
DEMAND(J)..SUM(I, X(I, J)) = G = B(J);
MODEL TRANSPORT/COST, SUPPLY,
DEMAND/;

To solve this model, the user issues the statement

SOLVE transport USING p MINIMIZING z;

where lp is the name of a solution procedure (i.e., the solver). GAMS provides lp for linear programming, nlp for nonlinear, mip for mixed integer, and rmip for relaxed mixed integer programming.

IFPS explicitly allows the use of a model for different purposes. The SOLVE command evaluates all functions and formulas for a given set of inputs. The WHAT-IF option of SOLVE allows temporary modification of formulas and variables in the model. The GOAL-SEEKING option allows the user to specify values for the 'output' variables, IFPS then determines the values of the input variables necessary to obtain those outputs.

The separation of model and solvers in modeling systems such as GAMS and IFPS still leaves the following problems unsolved:

(1) As a single modeling paradigm is assumed, extensions are often awkward. For example, GAMS assumes mathematical programming and IFPS assumes a spreadsheet format. The model representation uses a specialized language that, because of the single-modeling paradigm, often includes assumptions, defaults, and terminology that may differ considerably from common usage in other paradigms.

(2) Only those solvers provided in the system or especially-written are available. Thus, while the GAMS program may be augmented with user-written solvers (not a trivial task), it cannot easily utilize SAS or non-customized Fortran subroutines as additional solvers.

(3) In the interest of increased modeling power, modeling languages allow the mixing of data an model manipulation statements together with model definition statements. A consequence is that a 'model' in these languages usually includes not only the model itself but also statements to read data from external files, solver the model, manipulate the results provided by the solver, and display the outputs. Models begin to resemble conventional programs.

For these reasons, unless very strict programming (modeling) discipline is enforced, model representations defined in languages such as GAMS and IFPS should be considered computer programs rather than model specifications. This is perhaps the reason that GAMS uses the term “program” to refer to a complete set of statements, which include one or more “model” statements [4].

## 3. The DAMS data and model management system

The Data and Algebraic Management System, DAMS, is an integrated data and model management system that supports model/data and model/solver independence [18]. In particular, DAMS provides:

(1) mappings to support model/data and model/solver independence;

(2) multi-purpose use of models through a separate solver base and a modeling language that is independent of solvers;

(3) a manipulation language that adds model-specific operations to a generalized DBMS;

(4) an implementation architecture that allows compatibility with commercial database and modeling software.

## 3.1. The DAMS languages

At the heart of DAMS are the sublanguages shown in fig. 1. All sublanguages share a common syntax and a common programming interface. They can be mixed arbitrarily in an interactive session or invoked from a program by making calls to C subroutines.

![](/api/attachments/3FCFVFWG/fulltext/images/b54320841ea5edae10248ed448fdbca97b3666167c35c9e14549d56fb812028f.jpg)  
Fig. 1. The DAMS languages.

DAMS uses SQL and SQL/OBJ as its database languages. In DAMS, a database statement that is not a SQL/OBJ statement is, by default, a “host SQL” statement. Host SQL statements are not processed directly by DAMS but only passed on to the host DBMS. Outputs from the host are displayed by the DAMS interface. SQL/OBJ is a nested relation extension to SQL $[15]$ that supports matrices, arrays, and nested relations. These extensions facilitate the manipulation of data such as the hierarchical dataset for steel mills in Fourier $[7]$ .

The modeling language, SM/DB (structured modeling/data base) [19], supports a modeling environment. Table 1 summarizes the SM/DB statements. The MDL sublanguage allows the definition of new models. DSL defines model instances and maps them to relational tables. DSL also facilitates the browsing and display of tables containing model data. MML provides commands to solve models. The DISPLAY statements are a subset of MML that provide access to model information without using SQL.

## 3.2. Synergy of integration

The integration of modeling and database languages provides DAMS with considerable synergy. One aspect of this synergy relates to two extreme approaches to modeling and application development, shown in table 2. The model-centric approach assumes that the model is the object of interest and that data exists only as it pertains to the model; the modeling language provides statements to manipulate the data. Two models share data only by replicating it. The data-centric approach takes the opposite view: Data is the object of interest and is shared by multiple models. No model 'owns' the data; models are treated as 'programs' that are external to the database. A data language exists rather than a modeling language.

<table><tr><td colspan="2">Table 1SM/DB statements</td></tr><tr><td>MDL statements</td><td>CREATE/DROP MODELALTER MODELCREATE SOLVER REPCREATE/DROP EXECUTABLE</td></tr><tr><td>DSL statements</td><td>CREATE/DROP INSTANCEALTER INSTANC_EVALIDATE INSTANC_EVALIDATE GENUSSTORE GENUS</td></tr><tr><td>MML statements</td><td>EVALUATE MODELEVALUATE INSTANCEEVALUATE GENUSSOLVE</td></tr><tr><td>DISPLAY statements</td><td>DISPLAY GENUSDISPLAY MODELDISPLAY INSTANCEDISPLAY STATUS</td></tr></table>

DAMS supports the data- and model-centric approaches plus any mixture of both. DAMS makes no explicit difference between both approaches, and allows them to be mixed at any time. A modeler interested in a single model will follow the model-centric approach, without concern for the structure of the database or even for the existence of a database system. DAMS will automatically generate the table formats and translate references to model variables to database elements.

The data-centric approach is mostly beneficial to users of multiple models based on mostly the same data and/or models with large datasets that require extensive manipulation and reporting. The data-centric approach is supported by allowing relational tables to be created and manipulated independently from any model. The user must specify the mappings between model elements and relational tables.

## 3.3. The implementation environment of DAMS

DAMS is implemented using a relational database system (DBMS). All database query languages and interfaces (such as query by forms) are available to the user. The relational system is called the “host” system. DAMS is similar to GPLAN $[1]$ in that both allow the host DBMS query language to be used to manipulate the data used in models. Fig. 2 shows the architecture of DAMS. In the current implementation the host is INGRES version 6.03 running on a VAX under VMS. DAMS is written in C and uses embedded SQL to access the host DBMS.

IDAMS, or interactive DAMS, is the component that deals with interactive users. Conceptually, its functions are very simple. It reads SM/DB and SQL statements from the user and sends them to the language processor. It then displays whatever output is received from DAMS. IDAMS only checks that the initial keywords (i.e., the name of the command) are correct and that the command is properly finished (semicolon and/or END clause). IDAMS maintains a buffer with the last command typed the user. The command may be edited, printed, saved to a file, resubmitted, or erased. IDAMS also supports “immediate” statements, for functions such as creating a log file and browsing the output from a command.

Model-centric and data-centric approaches to modeling

<table><tr><td>Approach</td><td>Characteristics</td><td>Manipulation</td></tr><tr><td>Model-centric</td><td>A model is defined. Data for the model is collected and then stored.The model defines the format of the data.</td><td>The database is accessed through the modeling language, or by importing and exporting it to an external database system.</td></tr><tr><td>Data-centric</td><td>A database already exists, possibly shared by multiple users.A portion of the database will be used in a model. The database cannot be changed to accommodate the model.</td><td>The modeling language is treated as an external program, in the same way that a COBOL program.The database cannot be guaranteed to conform to model specifications, e.g. inconsistencies may arise.</td></tr></table>

![](/api/attachments/3FCFVFWG/fulltext/images/c0c90e3e65a4a0c5d0ce6be2648b97c44a1a4895a1fb04cb9dedd72648160952.jpg)  
Fig. 2. The DAMS system.

There are two other interfaces. The DAMS application program interface (API) is a collection of subroutines written in C that can be called from any application program. The application program generates a command and sends it to the language processor. The syntax of commands is the same as for IDAMS but the user's program is responsible for all user interaction. The spreadsheet interface is in development and it allows users to issue SM/DB statements and view model data from a spreadsheet.

The DAMS language processor receives statements from any of the interfaces and determines their processing. Database statements are sent to the host DBMS without further processing. SM/DB statements are sent to the DAMS query processor. Output from the host DBMS or the DAMS query processor is returned to the calling interface.

Communication between user programs and DAMS (as well as between DAMS modules) uses the DAMS communication area (DAMSCA). DAMSCA is similar to the SQLCA communication area, it stores execution codes and error messages. Currently, the SQLCA also stores the execution code for SM/DB commands but it was decided to have a separate area for portability.

## 4. Modeling with DAMS and SM/DB

DAMS supports a number of modeling objects. An object in DAMS is a named entity with an existence of its own. Objects are created using a CREATE statement such as CREATE TABLE or CREATE MODEL. A DROP statement is used to delete objects, and an ALTER statement modifies object definitions. The supported objects are:

<table><tr><td>SQL objects</td><td>Modeling objects</td></tr><tr><td>Tables</td><td>Models</td></tr><tr><td>Views</td><td>Model instances</td></tr><tr><td>Other as supported by the host system (procedures, constraints, etc.)</td><td>Solver representationsModel/solver mappingsExecutable models</td></tr></table>

## 4.1. Defining models in DAMS

Modeling definition in DAMS is based on structured modeling [10] and utilizes the same basic concepts. A model in DAMS corresponds to the notion of model schema in structured modeling. Models are defined using the CREATE MODEL statement. An example using the classical FEEDMIX model [8] is given in fig. 3. Models are defined by aggregating genera. There are five genus types: Primitive entities (PE), compound entities (CE), attributes (ATT or VA), functions (FUNC), and tests (TEST). Modules are syntactical groupings of genera and are optional. Genera may be grouped in modules in any desired fashion.

Fig. 3 illustrates the major points of model definition in SM/DB. While SM/DB is not case sensitive, uppercase has been used to denote SM/DB keywords and lowercase for user-defined names. The first genus, NUTR, is a primitive entity. The second genus, MIN, is an attribute of NUTR and is said to be indexed by NUTR. The indexing genus is shown in parentheses. ANALYSIS is indexed by both the NUTR and MATERIAL primitive entities. An attribute, function, or test without an index specification may be instantiated by a single value.

```sql
CREATE MODEL feedmix
WITH CANONICAL INSTANCE
BEGIN
    MODULE nutrients BEGIN
    PE nutr CHAR(8);
    ATT min (nutr) REAL;
END MODULE nutrients;

MODULE materials BEGIN
    PE material CHAR(10);
    ATT ucost (material) REAL;
    ATT analysis (nutr, material) REAL;
END MODULE materials;

MODULE formulas BEGIN
    VA q (material) REAL;
    FUNC nlevel (nutr; analysis, q) := SUM(analysis * q);
    TEST tnlevel (nutr; nlevel, min) := nlevel >= min;
    FUNC totcost (; ucost, q) := SUM(ucost * q);
END MODULE formulas;

END MODEL feedmix;
```  
Fig. 3. CREATE MODEL for the FEEDMIX model.

Each function or test is defined with an algebraic expression following the := symbol. Tests are Boolean functions that return TRUE or FALSE. Functions and tests require the specification of the parameters used in the algebraic expression. Parameters are indicated in the parentheses after the indexing genera following a semicolon. The function NLEVEL requires the values of ANALYSIS and Q and is indexed by NUTR. TOTCOST is an unindexed function with parameters UCOST and Q.

## 4.2. Model instances and datasets

Model instances can be created at the time a model is defined or at any time after. They are given a name and are objects on their own. A model instance in DAMS is formed by a pair $\langle$ model, dataset $\rangle$ . A dataset is a table subset of a relational database (or nested relational). Tables may be virtual relations (views) or base tables. Multiple instances for the same model can be created. Datasets are not necessarily disjoint. A database will usually store datasets for multiple models. A dataset is not an object in DAMS and thus it cannot be created or dropped in the same sense as a model or an instance. It is possible, however, for DAMS to automatically create and drop the tables used in a given instance.

Note that the term “model instance” refers only to an SM/DB object that associates a model and a dataset. There is no requirement that data actually exists in the dataset or that these data satisfy any constraints implied in the model (VALIDATE can be used to verify correctness of the instance). This usage of the term instance may seem strange. It is, however, consistent with the SQL usage, where CREATE TABLE defines a new empty table.

<table><tr><td>NUTRIENT</td><td>MINIMUM</td><td>NLEVEL</td><td>TNLEVEL</td></tr><tr><td>Protein</td><td>16</td><td>15.00</td><td>FALSE</td></tr><tr><td>Calcium</td><td>4</td><td>4.50</td><td>TRUE</td></tr><tr><td colspan="4">MATERIALS</td></tr><tr><td>MATERIAL</td><td>UCOST</td><td>QTY</td><td></td></tr><tr><td>standard</td><td>1.20</td><td>2.00</td><td></td></tr><tr><td>additive</td><td>3.00</td><td>.50</td><td></td></tr><tr><td colspan="4">ANALYSIS</td></tr><tr><td>NUTRIENT</td><td>MATERIAL</td><td>ANALYSIS</td><td></td></tr><tr><td>Protein</td><td>standard</td><td>4.00</td><td></td></tr><tr><td>Protein</td><td>additive</td><td>14.00</td><td></td></tr><tr><td>Calcium</td><td>standard</td><td>2.00</td><td></td></tr><tr><td>Calcium</td><td>additive</td><td>1.00</td><td></td></tr><tr><td colspan="4">TOTCOST</td></tr><tr><td colspan="4">TOTCOST</td></tr><tr><td colspan="4">3.90</td></tr></table>

Fig. 4. The sample dataset for the FEEDMIX model.

The clause WITH CANONICAL INSTANCE in fig. 3 creates a canonical instance with the same name as the model. Canonical indicates that the dataset tables are created automatically. These tables are initially empty and the modeler must insert data using SQL and/or SM/DB commands. Tables and columns for a canonical instance are created according to an algorithm that essentially groups genera with the same indexes in the same table and uses the genus names as column names. Functions and tests are assigned to tables separate from attributes. Model/data mappings for a canonical instance are automatically generated. The canonical instance created in fig. 3 would have the following tables and columns (table names are actually prefixed to avoid duplication; the actual name for the table NUTR will be something like XX35NUTR):

<table><tr><td>Table</td><td>Columns</td></tr><tr><td>NUTR</td><td>NUTR, MIN</td></tr><tr><td>MATERIAL</td><td>MATERIAL, UCOST</td></tr><tr><td>ANALYSIS</td><td>NUTR, MATERIAL, ANALYSIS</td></tr><tr><td>Q</td><td>MATERIAL, Q</td></tr><tr><td>NLEVEL</td><td>NUTR, NLEVEL, TNLEVEL</td></tr><tr><td>TOTCOST</td><td>TOTCOST</td></tr></table>

An instance can also be defined using a dataset created independently of the model. The model/data mapping must be explicitly given. Consider fig. 4 (double lines separate key and non-key attributes). This dataset differs from the canonical instance in several aspects. The names of columns and tables do not coincide with the corresponding genera. The tables Q and NLEVEL are no longer used. The SM/DB statement that creates an instance and the model/data mapping for the FEEDMIX model:

CREATE INSTANCE sample\_instance

FOR MODEL feedmix

MAP nutr TO nutrients (nutrient),

MAP min (nutr) TO nutrients (minimum, nutrient),

MAP material TO materials (material),

MAP ucost (material) TO materials (ucost, material),

MAP analysis (nutr, material)

TO analysis (analysis, nutrient, material), MAP q (material) TO materials (qty, material), MAP nlevel (nutr) TO nutrients (nlevel, nutrient), MAP tnlevel (nutr) TO nutrients (tnlevel, nutrient),

MAP totcost TO totcost (totcost);

## 4.3. Default instances and partial model / data mappings

One of the model instances is the default instance. This allows users to issue SM/DB commands without explicitly indicating the instance using statements such as SOLVE and DISPLAY (explained later). The canonical instance of fig. 3 becomes the default instance since it is the only instance defined for that model. Unless otherwise specified, the instance last created is the default instance.

Instances may be created in which the model/data mapping is only partially specified. For example, a dataset may be defined to store only the inputs to a linear programming solver without any table or column assigned to store solver outputs. This is a common situation when the solver's outputs are sent directly to a printer or to the screen but are not stored in the database. If some genera must be instantiated prior to their use with a specific solver, an error message will be issued when attempting to use this solver.

It is also possible to define a model/data mapping where some of the tables already exist and others must be automatically generated for this instance. Assume, for example, that there exists a dataset for NUTR, MIN, MATERIAL, UCOST and ANALYSIS. The following SM/DB command uses the REST AS CANONICAL clause to automatically create three tables: Q, NLEVEL, and TOTCOST to store the genera not listed in a MAP clause.

CREATE INSTANCE mixed\_instance

FOR MODEL feedmix

MAP nutr TO nutrients (nutrient),

MAP min (nutr) TO nutrients (minimum, nutrient),

MAP material TO materials (material),

MAP ucost (material) TO material (ucost, material),

MAP analysis (nutr, material)

TO analysis (analysis, nutrient, material),

REST AS CANONICAL;

All instances are dropped when their base model is dropped. Tables for a canonical instance are dropped when the base model is dropped, as are tables created using the REST AS CANONICAL clause. Tables referenced in a MAP clause are not dropped automatically.

## 4.4. Supporting the model-centric approach

The model-centric approach is supported in DAMS by essentially 'hiding' the database manipulation statements. In a pure model-centric approach, the modeler defines a model and creates a single canonical instance using CREATE MODEL. Data are inserted and manipulated in the instance using SM/DB commands. No SQL commands are needed. Since a canonical instance has its dataset and model/data mapping automatically created, there is no need for the modeler to explicit refer to any relational table. In addition, for each session, DAMS maintains a model as the 'current' model and interprets unqualified references to a genus as pertaining to the current model.

The DISPLAY GENUS statement is used to retrieve model data. It is similar to the SELECT statement in SQL. Genus names are used, instead of column and table names, to provide a model-centric view. Thus, to retrieve the names of all nutrients in the FEEDMIX model, the statement DISPLAY nutr is used. NUTR is assumed to be a genus of the current model and its default instance. SM/DB internally translates DISPLAY GENUS statements to SELECT statements. The STORE statement plays a similar role for insertion of values for a genus. It is translated to a SQL INSERT statement.

Other forms of the DISPLAY statement exist. DISPLAY MODEL displays general information about a model, including the names of its instances. DISPLAY DESCRIPTION lists the formulation of the model. DISPLAY INSTANCE lists model/data mappings.

## 4.5. Automatic generation of data for model instances

SM/DB provides the GENERATE GENUS statement to automatically generate data taking advantage of information in the model definition. It is useful in simulations and to avoid the typing of values that can be computed, as in the following examples:

(1) for a primitive entity YEARS to take the values 1983, 1984,... 1992, use: GENERATE GENUS years USING FORMULA 1983 $\langle =$ years $\rangle = 1992$ ;

(2) to generate all possible values for a compound entity such as LINKS in a transportation model, use: GENERATE GENUS links USING DISPLAY links FROM plants, markets;

(3) to randomly generate values for the genus SALES using a normal distribution with mean 2500 and a variance of 400, use: GENERATE GENUS sales USING FORMULA normal(2500, 400). As many values will be generated as there are values for the indexing genus.

## 4.6. Model solving and evaluation

DAMS provides two fundamental operations on models: Evaluation and solving. The EVALU-ATE commands provides a straight computation of functions and tests. The SOLVE statement invokes a 'solver' to manipulate a model instance. SOLVE is discussed in the next subsection.

The first form of EVALUATE deals with an entire model instance. When EVALUATE MODEL model-name or EVALUATE INSTANCE instance-name are used, all functions and tests in that instance are evaluated. The default instance is evaluated when EVALUATE MODEL is used. The statement EVALUATE MODEL feedmix would use the canonical instance defined in fig. 3 and compute values for NLEVEL, TNLEVEL, and TOTCOST. Note that Q must have been previously instantiated in order to compute NLEVEL.

The second form, EVALUATE GENUS, computes an individual function or test genus. It optionally computes values for all genera required as parameters. EVALUATE returns an error if any required genus is incorrectly instantiated; no tables are updated. Such an error occurs when the number of values for an attribute is less than the number of values in its index set. The form of the statement is

EVALUATE GENUS genus-name [FOR MODEL/INSTANCE name]
[INSTANTIATE PREVIOUS|WITHOUT INSTANTIATING PREVIOUS];

INSTANTIATE PREVIOUS, the default, has the effect of storing the values for all genera required to compute this genus. If EVALUATE GENUS tnlevel FOR feedmix is used, the values of TNLEVEL and NLEVEL are computed and stored in the database, replacing any existent values. If EVALUATE GENUS tnlevel FOR feedmix WITHOUT INSTANTIATING PREVIOUS is used, values for TNLEVEL are computed using whatever values already exist for NLEVEL.

## 4.7. The SOLVE statement

SOLVE is the most powerful statement in processing a model. It invokes a program (the solver) to manipulate a model instance. The format is the following.

SOLVE model-spec [USING solver-spec]

[MINIMIZING | MAXIMIZING genus name]

VARIABLES genus-name [,genus-name...]

OMIT genus-name [,genus-name...]

RESTRICT GENUS genus name TO INTEGER [BETWEEN min and max]

|BINARY

|POSITIVE

|BETWEEN min AND max

| REAL

model-spec may be the name of a model instance, a model (the default instance will be solved), or an executable model (defined later). Most clauses are optional, such as MINIMIZE/MAXIMIZE. The genus to be minimized or maximized must be a non-indexed function genus. OMIT indicates genera to be discarded. The RESTRICT clause provides additional information to the solver such as bounds for a variable. It may also relax a constraint, treating an attribute as real instead of integer. RESTRICT and OMIT do not have effect beyond the particular SOLVE execution. The following uses a linear programming solver on the FEEDMIX model.

SOLVE feedmix USING lpsolver
MINIMIZING totcost
VARIABLES q;

## 4.8. Solvers and executable models

DAMS considers two types of solvers: internal and external. An internal solver is a program written specifically to interface with DAMS. The mechanism is similar to GAMS. The above example uses “lpsolver” as an internal solver. A limited number of internal solvers is provided for the more common cases, such as linear programming. An external solver is an arbitrary computer program that can be automatically run and interfaced using files or the host database system. A solver representation defines the communication with the solver via its inputs and outputs. Model/solver mappings relate a model to an external solver. This architecture allows DAMS to be extended with arbitrary solvers without extensive recoding since only the mapping needs to be defined. It also allows the use of solvers that cannot be easily modified, either because of proprietary restrictions for commercial software, or because of technical reasons.

A realized model is formed by a model instance and a solver, i.e., it is the triple $\langle$ model, dataset, solver $\rangle$ . A realized model that is “ready to run” is called an executable model and includes model/data and model/solver mappings, as shown in fig. 5.

End users need not be aware of all these components. The model and the executable model can be prepared by an expert, while data preparation, model execution, and analysis of the model can be carried out by the end user. The distinction between executable models, internal and external solvers is transparent to the user. The SOLVE statement allows the name of an executable model to be used in the model-spec clause. This DAMS structure is not unlike that of a Fortran program using embedded SQL to access a database, where the user does not need to be aware that the application program and the DBMS are separate entities.

![](/api/attachments/3FCFVFWG/fulltext/images/48807c316f15bec4cc776242e335537fcd5ff95c0d00e0c3aa736059e29984d3.jpg)  
Fig. 5. The compositions of an executable model.

Each solver is given a representation that defines the types of models that can be manipulated. The representation includes a world view (entities manipulated by the solver), pre- and post-conditions that are true before and after execution of the solver, and a file interface. A discussion of world view and pre- and post-conditions is given in Eck et al. [5].

The file interface defines the files through which the solver receives its inputs and displays its outputs. Most solvers use a file structure that is more complex than a relational database and cannot be described in terms of just tables and columns. In DAMS, a file interface is as follows. Inputs and outputs are defined as separate collections of files. Files are not allowed to be used for both input and output. Files are 'logical' and may be assigned to a physical device such as keyboard, screen display, or disk. For each file, a file descriptor describes parameters such as name, device, type (sequential, host database table, ISAM), and record length (fixed, variable, number of bytes). The file header is an optional series of constant records that allows the inclusion of statements required by operating systems and solvers, such as the statement // EXEC MPSX for the MVS operating system. For SAS, the file header could include the OPTIONS statement to define the width of printer reports. The file footer is similar to the file header; also a series of constant records. Between header and footer, there are one or more segments. Records in a segment all have the same general format (or "scheme" in the relational terminology). A segment has descriptor, headers and footers similarly to the file. The segment descriptor defines the format of records in the segment. A record is composed of fields. All records in a segment have the same fields. Fields can be constants or variables. A constant field has a fixed value defined in the segment record descriptor. A variable field takes its value from an external file or is assigned a value by the solver.

The following example illustrates the use of external solvers and model/solver mappings. Consider a Fortran program that minimizes a linear program with $\geq$ constraints and produces only printed output. The program reads a file with array variables C (cost coefficients), B (available resources), and a matrix C (substitution coefficients). All records have a fixed format of 80 characters. Records containing values for C and B are identified by the constants ‘C’ and ‘RHS’ respectively. The program is run on the MVS system. This is a somewhat simplified situation but illustrates the major points of and limits the amount of code in the example. More complex situations such as equality and $\leq$ constraints can be handled though the mappings or additional clauses. The (partial) solver representation is

CREATE SOLVER REP lpfortran SYSTEM
MVS; BEGIN
WORLD VIEW BEGIN
PE i;
PE j;
ATT c(j);
ATT b(i);
ATT a(i, j);
ATT x(j);
END WORLD VIEW;
FILE DESCRIPTOR onlyfile INPUT RECORD SIZE 80 BEGIN
FILE HEADER '//DAMS JOB';
FILE HEADER '//EXEC LPSOLVER';
FILE HEADER '//SYSIN DD\*';
SEGMENT onlyfile BEGIN
RECORD costs BEGIN
CONSTANT 'C';
ARRAY c; END RECORD costs;
RECORD righthand BEGIN
CONSTANT 'RHS';
ARRAY b; END RECORD righthand;
RECORD coeffs BEGIN
MATRIX a; END RECORD coeffs;
END SEGMENT;
FILE FOOTER '//';
END FILE DESCRIPTOR;
END;

The world view defines the entities and attributes that the solver manipulates and that can be mapped to a model. The SYSTEM MVS clause specifies the computer on which the solver is run. Currently, DAMS allows solvers to reside on the VAX and on an IBM 3090 running MVS. VAX solvers are executed by 'escaping' to a shell, and MVS jobs are sent over a network to the IBM 3090. In the example, the file header contains the JCL statements to execute an MVS job. The filed interface has three segments, one for each record type.

File interfaces and solver representations cannot handle all possible cases. For example, it is not possible to specify the inputs for LINDO using the free-form algebraic style. It is possible, however, to specify a large subset of the MPSX format as a file interface. Solvers with multiple options are better (sometimes only) described through multiple solver representations, one for each related group of options.

To create a model/solver mapping for the FEEDMIX model and the LPFORTRAN solver representation, the following code can be used. Note that the mapping of Q to X is not necessary since this particular solver produces only printed output and does not store any results in the database.

CREATE SOLVER MAPPING feedsolvermap
FOR MODEL feedmix
AND SOLVER lpfortran
MAP nutr TO j:
MAP material TO i;
MAP ucost TO c;
MAP analysis (nutr, material) TO a (j, i);
MAP q TO x;

To create an executable model that solves the SAMPLE\_INSTANCE of the FEEDMIX model using LPSOLVER:

CREATE EXECUTABLE MODEL feedexec USING INSTANCE sample\_instance AND SOLVER MAPPING feedsolvermap;

The statement SOLVE feedexec is now all that is needed to solve the FEEDMIX model. In this particular case, DAMS will 'download' the dataset to a single VAX file with the format specified in the solver representation (lpfortran). The first records in the file would be the constants in the file headers and the last record would be as specified in the file footer. This file will then be sent over the network for execution on the IBM system. The output will be returned as a text file to the user.

## 5. SM/DB and SML

SM/DB shares with SML [8,11] the modeling concepts of structured modeling, and in fact the initial development of DAMS used SML as the model definition language. This section briefly describes the differences between the two languages.

First, SML is a model definition language. SM/DB adds facilities to manipulate models (SOLVE, EVALUATE, DISPLAY), datasets (DSL statements), model definitions (DROP and ALTER MODEL), and other modeling objects. SML allows implementors to define their own interfaces and commands. In FW/SM [12], the facilities of the Framework III system are used to provide user interface and database manipulation.

SML and SM/DB view models and databases in a different way. In SML, a model is composed of a model schema and a set of elemental detail tables (EDTs). A model schema corresponds to a 'model' in SM/DB. The EDTs store the data that instantiates the model schema. To create two model instances for the same model, in SML one must (at least conceptually) create two model schemas. EDTs differ from SM/DB tables in that EDTs obey a strict set of rules defining their format. EDTs are normalized to Boyce-Codd normal form [17] and are named after the genera they instantiate. EDT data is 'typed' (integer, real, etc.) according to the model schema. Moreover, data in an EDT is assumed to be in order. SM/DB tables are strictly relational (or nested relational); assume no order and impose no constraint on naming. SML assumes that every genus has a corresponding table and column in an EDT while SM/DB allows genera that are not mapped to a relational table.

Model definition also differs in some aspects. SM/DB allows single-instance attributes to be defined without an index set. This is useful for constants such as $\pi$ , or a fixed “rate of return”. For syntactical convenience, SM/DB allows initial values to be given in the model definition, although they are not considered part of the model definition.

Indexing and subscripting are treated differently in SM/DB. In SML, it is possible to indicate that, for example, a compound entity includes precisely the Cartesian product of two primitive entities. It is also possible to indicate the rules to form a subset of the Cartesian product. These two cases are treated identically in SM/DB and is left to the actual instance to define whether and which subset is used. In return for this reduced expressive power, SM/DB has simpler statements. In SM/DB the formulas for functions and tests are defined without subscripting, using set-oriented statements similar in concept to relational algebra.

## 6. Summary and conclusions

We have presented an overview of the DAMS data and model management system. DAMS attempts to support complex decision making in an organizational environment by providing the ability to share components among users, and to integrate simpler components to form larger, more complex systems. The framework for DAMS is based on model/data and model/solver independence, and for this reason, we have defined the conditions for model representations that make possible the reuse and combination of models, databases, and programs. These conditions were illustrated using algebraic notation and modeling languages. To support model independence in the DSS architecture, DAMS incorporates mappings and solver bases. Solver bases contain general purpose programs rather than just the small collection of specialized solvers found in most DSSs. Mappings relate the now independent components of a DSS, allowing them to be combined and reused as required by the decision situation at hand.

A prototype version of DAMS is implemented. DAMS is a collection of C programs making SQL calls to the multi-user INGRES database system. Interactive and API interfaces are operational. Model evaluation is done using INGRES: Function and test formulas are translated into SQL statements. An internal solver provides optimization for a restricted class of models by generating calls to SAS/OR. External solvers are also supported for a limited class of models. The current version is uneven on its support for features and user-friendliness and has the following restrictions. A genus is restricted to a maximum of four indexing genera. Tests values are stored as 0/1 values and formulas must be stated as arithmetic expressions instead of logical expressions. The processing of solver representations and model/solver mappings is not yet integrated into the SM/DB language processor; separate programs must be run or entered manually into the model and solver bases.

The development of DAMS has been a rewarding experience for us and our students and has provided us with multiple lessons. Using the host DBMS as both a data manager and an implementation vehicle has removed much of the drudgery, allowing us to test many ideas without writing code at all. For instance, we were able to test the model/data and model/solver mappings using only the SQL language, before writing the generalized versions in C. The multi-user environment facilitated group development of software.

The synergy of integration of model and data management in DAMS goes beyond the conceptual level. All the resources of the host database system are available and it is not necessary to switch from the DAMS to the host environment to access them. The host database system is a multi-user system widely used in industry on a range of computers. This allows DAMS to be used with existent databases that are simultaneously being used for conventional applications and supports a data-centric approach to modeling. It must be noted that DAMS is not dependent on any specific features of the current host. INGRES can be substituted by ORACLE, DB2, or any other DBMS that supports SQL without affecting the modeling language and functions.

An initial attempt was made to use SML as the modeling language. Our approach was the translation of SML to an intermediate form that could be easily compiled and executed. Our limited experience in compiler writing and the comprehensiveness of SML made the translator too difficult. The current CREATE MODEL statement is the result of our efforts to define a subset of SML that would be easier to implement and still retain most of the expressive power.

The concept of a workspace seems necessary to facilitate dynamic modification of models and datasets. Consider, for example, the addition of a function to compute the sum of Q in the FEED-MIX model. Currently this will cause modification of all canonical instances definitions and mappings, including the creation of a new tables. These are expensive operations that may be unnecessary for a one time computation. It seems preferable to use an interpretive approach during a session and only commit to the databases the results at the end of the session.

A second version of DAMS is planned using Microsoft Windows and ORACLE Version 6. Our intent is to have a better development environment and to provide modelers with 'live' links between applications. Windows provides these facilities and it is relatively easy to interface spreadsheet, database, and graphical packages. We decided against using a UNIX workstation environment because of the high cost of software and the more complicated procedures to obtain and install network versions of software.

## References

[1] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Mathematical Programming Within the Context of a Generalized Data Base Management System, R.A.I.R.O. Recherche Operationnelle/Operations Research 12, No. 2 (July 1978).

[2] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, The Evolving Roles of Models in Decision Support Systems, Decision Sciences 11 (1980) 337–356.

[3] G.H. Bradley and R.D. Clemence, A Type Calculus for Executable Modeling Languages, IMA Journal of Mathematics in Management 3 (1988).

[4] A. Brooke, D. Kendrick and A. Meeraus, GAMS: A user's Guide (The Scientific Press, 1988).

[5] R. Eck, A. Philippakis and R.G. Ramirez, Solver Representation using Structured Modeling, Proceedings of the IEEE International Hawaii Systems Conference (HICSS-23) January 1990.

[6] R. Fourer, Modeling Languages Versus Matrix Generators for Linear Programming, ACM Transactions on Mathematical Software 9, No. 2 (June 1983) 143–183.

[7] R. Fourer, Database Structures for a Class of Mathematical Programming Models, Proceedings of the Twenty-Fourth Annual Hawaii International Conference on System Sciences, Vol. III (January 1991) 306–316.

[8] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (May 1987).

[9] A.M. Geoffrion, Indexing In Mathematical Programming Languages, Working Paper No. 371, Western Management Science Institute, UCLA, 1989.

[10] A.M. Geoffrion, The Formal Aspects of Structured Modeling, Operations Research 37, No. 1 (January–February 1989) 30–51.

[11] A.M. Geoffrion, SML: A Model Definition Language for Structure Modeling, Working Paper No. 360, Western Management Science Institute, UCLA, August 1990.

[12] A.M. Geoffrion, S. Maturana, L. Neustadter, Y. Tsai and F. Vicuña, User Documentation for FW/SM, John E. Anderson Graduate School of Management, UCLA, June 1990.

[13] C.W. Holsapple and A.B. Whinston, Model Management Issues and Directions, Paper No. 7, 1988, Kentucky Institute for Knowledge Management.

[14] T.P. Liang, Integrating Model Management with Data Management in Decision Support Systems, Decision Support Systems 1 (1985) 221–232.

[15] K.A. Moser, R.G. Ramirez and R.D. St. Louis, Complex Object Databases for Model Management Systems, Proceedings of the 23rd International Hawaii Systems Science Conference (HICSS-23), Hawaii, January 3–7, 1990.

[16] W.A. Muhanna and R.A. Pick, Composite Models in SYMMS, Proceedings of the 21st Annual Hawaii International Conference on System Sciences (January 1988) 418–527.

[17] L. Neustadter, On The Structure of Data in SML Models, Research Paper, John E. Anderson Graduate School of Management, UCLA, March 1990.

[18] R.G. Ramirez, Architecture and Implementation of the DAMS System, ISUMMS Project Technical Report #4, Iowa State University, August 1991.

[19] R.G. Ramirez, The SM/DB Language: Reference Manual, ISUMMS Project Technical Report #3, Iowa State University, September 1991.

[20] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems, (Prentice-Hall International, Englewood Cliffs, NJ, 1982).
