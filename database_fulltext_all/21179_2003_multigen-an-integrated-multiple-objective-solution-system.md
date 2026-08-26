---
otero_id: 21179
otero_key: "6DR73WTR"
title: "MultiGen: an integrated multiple-objective solution system"
authors: "S.K. Mirrazavi; D.F. Jones; M. Tamiz"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00135-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# MultiGen: an integrated multiple-objective solution system

S.K. Mirrazavi <sup>a</sup>, D.F. Jones <sup>b,</sup>\*, M. Tamiz <sup>b</sup>

<sup>a</sup>Temposoft UK, Albany House, Market Street, Maidenhead S16 8BE, UK

<sup>b</sup>School of Computer Science and Mathematics, University of Portsmouth, Mercantile House, Hampshire Terrace, Portsmouth PO1 2EG, UK

Accepted 3 July 2002

## Abstract

This paper presents an overview of a global multiple-objective system capable of rigourously handling a wide variety of multiple-objective and goal programming (GP) models. The system has two efficient solution engines that complement one another. These are an intelligent conventional optimisation system and a genetically driven heuristic search-based solver. The development of a linear and nonlinear sparse storage system capable of handling additional multiple-objective factors such as priority levels, goals, objectives, and upper and lower bounds is described. An appropriate input/output style for multipleobjective programmes is given. The resulting package provides an efficient and user-friendly environment for the interactive solution and analysis of a wide variety of multiple-objective programming (MOP) models <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Goal programming; Multiple-objective programming; Genetic algorithms

## 1. Introduction

A multiple-objective programming (MOP) technique can be described as one that aims to provide good solutions to decision problems characterised by the presence of multiple, often conflicting objectives. MOP models are used in many fields of application, examples of which include the areas of agriculture, engineering, and finance. Research on the theory and development of multiple-objective optimisation is extensive [13,23]. Ignizio [6], Hwang and Masud [5], Osyczka [16], and Yu [28] in particular have made considerable contributions in this field. Methods and software exist for the standard cases of a variety of MOP techniques such as compromise programming [29], composite programming, and efficient set generation [23]. Goal programming (GP) is a well-known MOP technique [18] that is based around the Simonian idea of satisficing a number of criteria. Good efficient revised simplex-based algorithms [8] are available and analysis techniques for all the main branches of GP have been well developed [7,18,25] and incorporated into computer packages such as GPSYS [11]. Additionally, methods such as simulation [17] and parametric linear programming can be used to examine multi-goal tradeoffs.

By adding one or more complicating factors, multiple-objective programmes become harder to solve. Such complicating factors may include nonlinearity, large numbers of integer variables, nonstandard underlying utility functions, or multi-modal objectives. The theoretical underpinning for the first two cases (nonlinear and integer) exists but such models can be in practice very hard to solve.

As well as development of conventional optimisation techniques, there has been a recent growth in heuristic search-based techniques for the solution of difficult models in the field of optimisation. Amongst the most popular of these is the technique of genetic algorithms (GA) that has been successfully used to solve many difficult problems in the fields of operational research and engineering [3]. GA is a novel and an evolutionary approach introduced by Holland [4]. It is one of the most appropriate techniques for providing solutions to difficult models. It can be considered as an alternative to the exact and traditional optimisation methods where solution of problems with complicating factors such as nonlinearity or a large number of integer variables is computationally very expensive. Selection, crossover, and mutation are the main operators of GA. The repeated use of these operators results in a series of populations of individuals with successively higher levels of fitness until some level of convergence around a single optimum or multiple optima is achieved. A detailed and comprehensive discussion of GA is given in Ref. [3].

GA has also been used for the solution of operational research problems including those with multiple objectives. As a result of their positive performance, many researchers have developed specific algorithms for the solution of such problems [22]. Schaffer [21] first introduced the concept of a multiple-objective GA, with his VEGA algorithm for the approximation of the efficient set. This idea was extended to include rank-based fitness and more efficient niching methods, and there is also a hint at the potential for interactive multi-objective GA [2]. Sakawa et al. [20] present a specialised modified GA for the case of 0– 1 fuzzy multi-objective programming [20]. The COMOGA method, which combines constraint satisfaction method with a type of multiple-objective GA, is introduced by Surry and Radcliffe [24]. A multiple-objective GA algorithm is also applied to the specific problem of airfoil design by Vicini and Quagliarella [26]. A recent review of multi-objective meta-heuristic theory and application is given by Jones et al. [12].

Many researchers and practitioners have employed GA for the solution of MOP models in recent years. The algorithms and techniques developed are all worthwhile and effective but largely specialised for the specific MOP applications.

This paper presents the design and development of a global multiple-objective system capable of rigourously handling all types of multiple-objective and GP models. The system is equipped with two engines based on conventional optimisation and a heuristic search technique.

The remainder of this paper is divided into five sections. Section 2 overviews the system developed by the authors: MultiGen and its underlying solvers. Section 3 presents the theoretical underpinning of this research discussing issues such as the adaptation of basic genetic operators and calculation of fitness functions in a multiple-objective environment. Section 4 describes the storage system that caters for all types of mathematical programming and MOP models. An interactive graphics-based environment, which controls the specification control unit and the output format of the system, is presented in Section 5. Finally, Section 6 draws some conclusions.

## 2. Overview of MultiGen system

MultiGen has been designed and developed for the efficient solution of linear and nonlinear MOP models. It has two solution engines. These are GPSYS [11], a conventional and intelligent solution and analysis system and a heuristic search-based technique employing GA. This will result in a global multiple-objective system where GA [1] can be an alternative solution tool for GPSYS in attempting to finding good initial solutions in models where the conventional method is experiencing difficulty and vice versa. An explanation of solution and analysis methods of GPSYS is out of scope of this paper. These issues are discussed in Refs. [9,11,14].

## 3. Algorithmic issues in the genetically driven system design

This section deals with the algorithmic issues involved in the design of a system capable of solving difficult multiple-objective models by GA. The system is designed to handle the inclusion of multiple objectives in GA issues such as adaptation of the basic genetic operators (crossover, mutation, and in particular selection) into a multiple-objective environment and how best to model multiple-objective fitness functions.

## 3.1. Multiple-objective fitness function calculation

In order to successfully apply GA to multipleobjective models, a method must be found of transforming the normally single-dimensional fitness func tion into a multiple-objective measure of fitness. The generalised MOP model designed and developed in this study comprises a fitness function calculated from goals, constraints, and objectives. Goals, constraints, and objectives have the same mathematical structure but they represent different underlying philosophies leading to different requirements or restrictions in a model. The difference between goals and constraints lies in the meaning of the right-hand side values. The right-hand side value of a goal represents desires or aspirations of the decision-maker that may or may not be achieved, whereas in constraints, the right-hand side must be satisfied in order to avoid infeasible solutions. Objectives represent the maximisation or minimisation of mathematical functions, e.g. minimising risk or maximising profit.

The following is the representation of a generic MOP model designed and developed in this study:

Fitness function (Z)

$$
\left\{ \begin{array}{l} \min Z = \{(p _ {i} \times \beta_ {i}) + (n _ {j} \times \beta_ {j}) + (n _ {k} + p _ {k}) \times \beta_ {k} \} + \\ \{(s _ {l} \times \xi_ {l}) + (s _ {m} \times \xi_ {m}) + (| f _ {n} - b _ {n} | \times \xi_ {n}) \} + \\ \{(z _ {p} \times \beta_ {p}) - (z _ {q} \times \beta_ {q}) \} \end{array} \right.
$$

Subject to Goals

$$
\left\{ \begin{array}{l l} f _ {i} (x) + n _ {i} - p _ {i} = b _ {i} & \text { minimising } p _ {i} \\ f _ {j} (x) + n _ {j} - p _ {j} = b _ {j} & \text { minimising } n _ {j} \\ f _ {k} (x) + n _ {k} - p _ {k} = b _ {k} & \text { minimising } n _ {k} \text { and } p _ {k} \end{array} \right.
$$

Constraints

$$
\left\{ \begin{array}{l l} f _ {l} (x) + s _ {l} = b _ {l} & (\leq) \text { constraint } \\ f _ {m} (x) - s _ {m} = b _ {m} & (\geq) \text { constraint } \\ f _ {n} (x) = b _ {n} & (=) \text { constraint } \end{array} \right.
$$

Objectives

$$
\left\{ \begin{array}{l l} z _ {p} = f _ {p} (x) & \text { minimisation } \\ z _ {q} = f _ {q} (x) & \text { maximisation } \end{array} \right.
$$

where $( \beta )$ is the weight of a goal or an objective. (n) is a fixed penalty associated with a hard constraint. In order for a solution to be feasible, all the fitness function coefficients associated with the $( \xi ) ^ { \cdot } \mathbf { s }$ must be zero. This is achieved by setting the $( \xi ) ^ { \cdot } { \mathbf { s } }$ to a suitably large value. $f ( x )$ is a linear or nonlinear function of x and x is the set of decision variables to be determined. b is the set of right-hand side values. $n _ { i }$ and $p _ { i }$ represent the negative and positive deviations from the target value of the i-th goal. $s _ { 1 }$ and $s _ { \mathrm { m } }$ represent slack and surplus variables of the corresponding constraints. The fitness function value (Z) of every string in a population is evaluated by placing the values of decision variables into the corresponding row, e.g. f<sub>i</sub>(x) a goal, f<sub>l</sub>(x) a constraint, or $f _ { p } ( x )$ an objective and calculating it in the above fashion.

Note that the system can handle any combination of the above formulation. Some of these combinations are represented in Table 1 where $r , s ,$ and t are defined as positive integer constants representing the number of objectives, goals, and constraints in the model, respectively. Model 1 has a single objective and a set of constraints and is hence a linear or nonlinear programming model (see footnote of Table 1). Model 3 is a goal programming model that uses the $L _ { \infty }$ metric to determine the distance from optimality [19]. The $L _ { \infty }$ metric seeks to minimise the maximum deviation from amongst the set of goals and hence provide a general balance between the achievement of the goals. This model also forms the basis for the development of $L _ { \infty }$ compromise programming. Model 5 is a constrained MOP that also provides the basis for the development of $L _ { 1 }$ compromise programming models. The $L _ { 1 }$ metric seeks to minimise a weighted sum of the unwanted deviations from the set of goals.

Table of MultiGen model formulations

<table><tr><td>No.</td><td>Model</td><td>Objectives ()</td><td>Goals ()</td><td>Constraints()</td></tr><tr><td>1</td><td>LP/NLP $^{a}$ </td><td>(1)</td><td>(0)</td><td>(t)</td></tr><tr><td>2</td><td>Constrained GP</td><td>(0)</td><td>(s)</td><td>(t)</td></tr><tr><td>3</td><td>Chebychev GP</td><td>(0)</td><td>(s)</td><td>(special set)</td></tr><tr><td>4</td><td>Unconstrained GP</td><td>(0)</td><td>(s)</td><td>(0)</td></tr><tr><td>5</td><td>Constrained MOP</td><td>(r)</td><td>(0)</td><td>(t)</td></tr><tr><td>6</td><td>Unconstrained MOP</td><td>(r)</td><td>(0)</td><td>(0)</td></tr><tr><td>7</td><td>Hybrid MOP/GP-Constrained</td><td>(r)</td><td>(s)</td><td>(t)</td></tr><tr><td>8</td><td>Hybrid MOP/GP-Unconstrained</td><td>(r)</td><td>(s)</td><td>(0)</td></tr></table>

<sup>a</sup> LP if all constraints and the objective function are linear, NLP otherwise.

## 3.2. Adaptation of genetic operators into multipleobjective environment

As mentioned in Section 1, the genetic algorithm is composed of three basic operators, selection, crossover, and mutation. Of these three operations, crossover and mutation require little alteration in moving from a single to a multiple-objective framework.

When solving certain types of multiple-objective models, such as lexicographic GP, a vector-valued fitness function must be used. The fact that the fitness function is vector-valued causes difficulties for the conventional roulette-wheel selection that is based around a single measure of fitness. For this reason, it is better to use the concept of tournament selection [3] for this type of model.

In this research, tournament selection is used to handle natural orderings or semi-orderings of the objectives that take place in a multiple-objective model. This technique is extended to conduct the lexicographic comparison between two or more vectors for the selection of the fittest individual. Assuming minimisation, the selection method for vectorvalued fitness functions is shown by the following fragment of pseudocode:

```txt
For each Priority Level, I=1 to L Do
.... Is the new gene better than the current best at priority level I ? ....
If New(I) < Best(I) Then
    For each priority level, J = 1 to L Do
    Best(J) = New(J)
    Continue For Loop(J)
    Exit
.... Is the new gene worse than the current best at priority level I ? ....
Else if Best(I) < New(I) Then
    Exit
End if
.... If the new and best gene are equal at priority level I Then ....
.... check the lower priority levels
Continue For Loop(I)
```

where New(I) and Best(I) are the fitness function values of the new and the best gene at priority level I of a population, respectively. Suppose that the following five individual genes with four priority levels have been selected from a population and the fittest is to be chosen for the next population: $g _ { 1 } = [ \alpha _ { 1 } , \alpha _ { 4 } , \alpha _ { 2 } , \alpha _ { 3 } ] , \ g _ { 2 } = [ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } , \alpha _ { 4 } ] , \ g _ { 3 } = [ \alpha _ { 4 } , \alpha _ { 2 } , \alpha _ { 1 } , \alpha _ { 3 } ] .$ 2 $g _ { 4 } { = } [ \alpha _ { 3 } , \alpha _ { 1 } , \alpha _ { 4 } , \alpha _ { 2 } ]$ , and $g _ { 5 } { = } [ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 4 } , \alpha _ { 3 } ]$ , where $\alpha _ { 1 } , \alpha _ { 1 }$ $\mathcal { \alpha } _ { 1 } , \mathcal { \alpha } _ { 2 } , \mathcal { \alpha } _ { 3 } ,$ and $\alpha _ { 4 }$ are fitness function values in priority levels 1 to 4, and,

$$
0 \leq \alpha_ {1} <   \alpha_ {2} <   \alpha_ {3} <   \alpha_ {4}.
$$

Assuming minimisation, $g _ { 3 }$ and $g _ { 4 }$ are not fit to be selected since their first priority level fitness values $( x _ { 4 }$ and $\alpha _ { 3 } ,$ respectively) are dominated by that of $g _ { 1 } ,$ $_ { g _ { 2 } , }$ and $g _ { 5 } \ ( \mathrm { i } . \mathrm { e } . \ \alpha _ { 1 } )$ . It is clear that $g _ { 2 }$ is the fittest gene since its fitness function value in priority levels 2 and 3 dominates the fitness function values of the same priority levels in $g _ { 1 }$ and $g _ { 5 } ,$ , respectively.

## 4. MultiGen input style

A sparse storage system (linear and nonlinear), which caters for linear programming, integer programming, goal programming, compromise programming, and multi-objective programming models, is designed.

This is a fundamental building block to the success of the system. The issue of effective representation and storage of a nonlinear coefficient matrix is a nontrivial one. An additional complicating factor is the existence of multiple objectives, with additional information such as priorities, rankings, deviational variables, and upper or lower bound.

Fig. 1 shows the general overview of the input data structure that is divided into the following sections:

Variable information: This section represents information regarding decision variables in a model. These include the variable’s name, granularity, and lower and upper bounds.

Row information: (a) Rigid part: The coefficient matrix is represented by this part of the input structure and is specified in row-wise format. This section deals with the left-hand side section of the goals, constraints, and objectives (linear and nonlinear). Decision variables and mathematical functions can be utilised in order to form the appropriate algebraic expressions. Specialised intrinsic functions, such as POW(), EXP(), LOG(), SIN(), etc., have been developed for the user-friendly representation of nonlinear mathematical functions. The function $\mathrm { P O W } ( X , y )$ raises a variable X to the power y. Immediate identification of these functions takes place in the case where calculation of the right-hand side values of the goals or constraints forms part of the fitness function evaluation. (b) Multiple-objective environment: This section deals with the multiple-objective environment of the data structure. It decides whether a row is a constraint (R), an objective (W), or a goal (D). A constraint is defined as any equality or inequality restriction that has to be met in order to make a solution feasible. An objective is defined as a desire by the decision-maker to maximise or minimise a function of the decision variables, without reference to any set level. A goal is defined as a desire by a decision-maker for a function of the decision variables to achieve a certain level. Reflections and linkages among the concepts of constraints, goals, and objectives in the context of multi-objective programming are given by Romero et al. [19]. Penalties $( P ) ,$ , deviational variable and objective weights (b), right-hand side values of constraints (TL), and target values of goals (TL) are all processed in this section and are stored in a compact structure.

<table><tr><td colspan="2">Variable Information</td></tr><tr><td rowspan="3">Row Information</td><td>Rigid Part</td></tr><tr><td>Multiple Objective Environment:</td></tr><tr><td>Goals Achievement/Fitness FunctionObjectives Deviational variablesConstraints Right hand side valuePriority Levels Target value, Penalty</td></tr></table>

Fig. 1. The general overview of MultiGen input storage structure.

Description of the multiple-objective environment of the input storage in MultiGen system

<table><tr><td>0(TL)γ</td><td>target value/right-hand side</td></tr><tr><td>α(-D)β</td><td>positive deviational variable</td></tr><tr><td>α(+D)β</td><td>negative deviational variable</td></tr><tr><td>α(+D)β and α(-D)β</td><td>positive and negative deviational variables</td></tr><tr><td>α(-R)β</td><td>(≥) constraint</td></tr><tr><td>α(+R)β</td><td>(≤) constraint</td></tr><tr><td>α(+R)β and α(-R)β</td><td>(=) constraint</td></tr><tr><td>α(-W)β</td><td>maximisation objective</td></tr><tr><td>α(+W)β</td><td>minimisation objective</td></tr><tr><td>α(-P)β</td><td>negative fixed-charge penalty</td></tr><tr><td>α(+P)β</td><td>positive fixed-charge penalty</td></tr><tr><td>0(EN)</td><td>end of row</td></tr></table>

## 4.1. An example

The following MOP example is given for the purpose of illustration:

$$
\min Z = 0. 2 5 p _ {1} + 2 0 S + 0. 0 5 p _ {2} + n _ {3} + n _ {4} + 5. 0 z _ {1}\tag{1}
$$

Subject to

$$
3 x _ {1} + x _ {2} ^ {- 0. 5} + \mathrm{e} ^ {x _ {1} ^ {- 0. 5}} + n _ {1} - p _ {1} = 1. 5 0\tag{2}
$$

$$
3 x _ {1} + x _ {2} ^ {- 0. 5} + \mathrm{e} ^ {x _ {1} ^ {0. 5}} + n _ {2} - p _ {2} = 4. 0 0\tag{3}
$$

$$
3 x _ {1} + x _ {2} ^ {- 0. 5} + \mathrm{e} ^ {x _ {1} ^ {- 0. 5}} - M \times S \leq 4. 0 0\tag{4}
$$

$$
x _ {2} ^ {0. 2 1} + \sin x _ {1} x _ {2} + n _ {3} - p _ {3} = 1. 7 5\tag{5}
$$

$$
\ln (x _ {3} + 1) + \cos x _ {1} ^ {5. 6} + n _ {4} - p _ {4} = 0. 0\tag{6}
$$

$$
x _ {1} + x _ {2} + x _ {3} + x _ {4} \leq 3. 0\tag{7}
$$

$$
z _ {1} = x _ {1} ^ {2} + x _ {2} ^ {2} + x _ {3} ^ {0. 5}\tag{8}
$$

$$
\begin{array}{l l} 0. 0 \leq x _ {1} \leq 1. 0, & 0. 0 \leq x _ {2} \leq 2. 0, \quad 1. 0 \leq x _ {3} \leq 3. 0, \\ - 1. 0 \leq x _ {4} \leq 1. 0 \end{array}\tag{9}
$$

Shown below is the input data file in MultiGen format. The granularity and the lower and upper bounds of the variables are defined in VARS section. The ROWS section caters for the rigid part of the goals, constraints, and objectives. The multiple-objective environment of MultiGen is represented in the TYPE section of the input data structure.

Table 2 details the multi-objective notation used. Any lexicographic priority level number is represented by c, $\beta$ is the corresponding goal, objective, or penalty weight, and a˜ is the right-hand side or target value for the corresponding row. Note that the decision-maker can easily convert a goal to a hard constraint or an objective by changing a $^ { \circ } \mathrm { D } ^ { \prime }$ to an $ { \mathrm { \Delta } } ^ {  { \ell } }  { \mathrm { R } } ^ {  { \ell } }$ or a ‘W’, respectively.

```csv
VARS 4
1 X1 1.0 0.0 1.0
2 X2 1.0 0.0 2.0
3 X3 1.0 1.0 3.0
4 X4 1.0 -1.0 1.0
ROWS 4
1 {X1}*(3.0) + POW(X2,-0.5) + EXP(POW(X1,-0.5));
2 POW(X2,0.21) + SIN(X1*X2);
3 LOG(X3+1) + COS(POW(X1,5.6));
4 X1 + X2 + X3 + X4;
5 POW(X1,2.0) + POW(X2,2.0) + POW(X3,0.5);
TYPE 4
1 OTL 1.5 1-D 0.25 OTL 4.0 1-D 0.05 1+P 20.0 OEN
2 OTL 1.75 1+D 1.0 OEN
3 OTL 0.0 1+D 1.0 OEN
4 OTL 3.0 1+R 10.0 OEN
5 OTL 0.0 1+W 5.0 OEN
END
```

The negative and positive fixed-charge penalties are used to formulate preference structures such as discontinuities and varying penalty levels dependent on the distance from the goals. This situation occurs when the left-hand side function goes beyond a level that requires further expense or inconvenience to take place, e.g. the renting of an extra warehouse in a stock control model or the construction of extra flood defences in a reservoir planning model. MultiGen can handle these discontinuities, which can be converted into a multiple-objective format by addition of a binary variable S and a sufficiently large constant M [10]. An example of this situation is given by Eqs. (2)–(4). These equations share the same rigid part but each represent different parts of the preference structure. The above mentioned equations are all represented by the first row in the TYPE section. The binary variable S is placed in the achievement function (Eq. (1)) with a weight whose size represents the inconvenience or cost incurred at the discontinuity.

Constraint violations are currently handled by the penalty method. In this method, the model is associated with a penalty or cost, i.e. b in a(R)b and a(+R)b that will be included in the fitness function evaluation, as shown in Table 2 and Section 3.1.

## 5. Interactive environment

MultiGen’s interactive mode consists of two main display screens for the solution of multiple-objective models. These are the MultiGen specification and result screens. The former details specific GA functions giving full control of the system to the decisionmaker whereas the latter displays a balanced output allowing the user to analyse and examine the solution.

## 5.1. MultiGen specifications unit

The specification screen details the GA solution parameters, i.e. operators, variables, and utility. It also displays the control buttons in order to process and solve multiple-objective models by the GA algorithm. The MultiGen specification control unit offers the decision-maker a complete environment to control the parameters before and during the course of solution. Fig. 2 displays the specification unit, which is divided into three GA specification areas plus a system control unit where all the command buttons are located. These include GA operators (top left), GAvariables (top right), GA utility (bottom right), and control (bottom left).

## 5.1.1. GA operators

. Mutation—This operation ensures that genetic diversity and a correct degree of randomness are maintained. It involves the modification of individual genetic string positions to their opposite value in a random fashion with the mutation probability of $p _ { \mathrm { m } } .$ For example, if the first bit in a string has the value 1 and ${ p } _ { \mathrm { m } } \mathrm { = } 0 . 0 2$ , then there is a 2% chance of that bit being mutated to its opposite value of 0 and a 98% chance of that bit remaining unchanged. The user also has a choice of selecting and setting a variant of mutation, i.e. creep mutation with probability of $p _ { \mathrm { c m } } .$ Creep mutation increases the probability of bits adjacent to a mutated bit being themselves mutated. As a decision variable is usually coded into the genetic string as a portion of adjacent bits along that string, creep mutation thus allows for a greater chance of substantial change to an individual decision variable.

. Crossover—This is a breeding operation with a probability of $p _ { \mathrm { c } }$ where selected parents swap parts of their genes in order to produce new offspring. The user has a choice between uniform or single-point crossover as explained by Goldberg [3].

## 5.1.2. GA variables

. Child Ratio—Number of new individuals created from selected parents.

. Population Size—Number of genes in the population.

. Generation Number—Maximum number of generations to perform the GA search (MaxGen).

. Initial Random Number—A large negative number that is used in the process of initialising the random number generator.

. Generations to Convergence—This number (Gnum) allows the decision-maker to specify the number of generations over which the measure of convergence is calculated. The measure of convergence is defined as 100 times the absolute value of the change in the best fitness function value over the last Gnum generations divided by the absolute value of the best fitness function value in the current generation.

![](/api/attachments/6DR73WTR/fulltext/images/f4063b532446d339c253597480ceeca67e0a5fce925bbf52c18d824e3149ab28.jpg)  
Fig. 2. MultiGen specification control unit.

## 5.1.3. GA utility

. Elitism—This mechanism is an amendment to the standard selection process that gives an automatic place in generation n+1 to the individual with the best fitness function value in population (n).

. Niching—This utility penalises individuals/genes with common characteristics in a population to maintain diversity according to a sharing function based at the decision variable level. Details of the niching algorithm used are given by Goldberg [3].

## 5.1.4. System control unit

Each button details a specific function and follows a natural order of use during the process of solution.

. Input—Default values for parameters in the GA operator, GA variable, and GA utility section are entered by pressing this button. This option helps practitioners who have less knowledge on how to set these values when solving different models for the first run. The decision-maker can access the system in order to change default values to his/her preference once he/ she is familiar with the behaviour of the model. The user can also enter all parameters manually.

. Process—Identification and process of GA parameters by the system takes place.

. Run—The model is solved by performing selection, crossover, and mutation operations for the chosen number of generations. A temporary output screen appears in the interactive environment giving the current best fitness function value of each generation instantly. The purpose of this screen is to report the convergency rate of the model. The decision-maker has the option to stop the solution procedure and reset the parameter/s in the specification screen and rerun the model if he/she is not satisfied with the behaviour of the model. The temporary screen disappears when the solution process is either completed or stopped.

The following algorithm gives a general overview of the multiple-objective genetic algorithm developed in this study:

## INITIALIZATION

1. An internal view of the model is created in a designed compact storage format. This accommodates the multiple objective requirements of the model as well as providing fast and easy access of the solution algorithm to data, as detailed in section 4.

2. Genetic string size and the value of parent individuals in the population are calculated and initialised respectively.

## FITNESS FUNCTION CALCULATIONS

3. The multi-objective fitness values of individual genes in the population and the multi-objective fitness function of the model are calculated for the corresponding generation, as detailed in section 3.1.

## OPERATORS

4. Selection, crossover and mutation operations are performed,as detailed in 3.2.

5. Steps 3 and 4 are repeated for the Maximum number of generations.

## OUTPUT

6. Appropriate results are displayed, as detailed in section 5.2.

Result—This button displays the result screen interactively where multiple-objective and GA properties of the model are reported, as shown in section outstyle.

Clear Form—This button clears all the parameters entered in the MultiGen specification unit in order to set new parameter values for the new GA runs.

Stop—The stop button halts the solution process.

GPSYS—This displays the GPSYS specifications file in order to run the model by conventional methods GPSYS.

## 5.2. MultiGen output style

The MultiGen output style is a results box that can be displayed interactively by pressing the ‘Result button on the system control unit of the specification screen. The results box provides a complete environment to display appropriate model information and suitable solution output. It consists of eight model specification objects, an information panel, and four control buttons;

. Model Info—This button displays model statistics in eight designated areas provided on the result screen. These include number of goals, constraints, objectives, priority levels, variables, and other information such as genetic string size of the model, convergence information, and solution time. It also displays detailed results on the information panel. These include the best, the worst, and the average fitness function values in a population and the number of crossovers and mutations performed at each iteration, as detailed in Fig. 3.

. Variable Info—This button provides the decisionmaker with the values of the decision variables at the current generation when pressed. It is useful for checking the progress of the genetic algorithm, and hence guiding any interactive changing of parameters as required.

. Constraint Info—This button provides the decision-maker with the difference between the target value/right-hand side value and the rigid part of a goal/constraint for all rows in the model. This information will let the decision-maker know about the state of goals and constraints, i.e. whether the goal is satisfied or not satisfied and the amount by which the goal is not satisfied in the latter case. The decisionmaker can then modify some of the parameters and parts of the model for the future GA calculations if he/ she wishes to do so.

![](/api/attachments/6DR73WTR/fulltext/images/3588fb6807c906c2f86f23b29be851d655312695e66a02bcaaca97cd9f65580a.jpg)  
Fig. 3. MultiGen result unit.

. New Input—This button shows the specification screen unit interactively where the decision-maker can change all or some of the GA parameters, rerun the model, and examine the new results.

Note that the information panel can be scrolled up and down where results (model, variables, and constraints) for every single generation can be examined.

## 6. Summary and conclusion

This paper has reported the design and development of a global multiple-objective system: MultiGen. A sparse storage system is designed to accommodate the multiple-objective requirements of MOP models in a GA platform. Unique intrinsic functions are developed for the efficient representation of nonlinear mathematical functions. Specialised data structure and algorithms are designed and implemented in order to handle the interface between MOP and GA in issues such as multiple-objective fitness function calculations and adaptation of genetic operators into multiple-objective environment.

MultiGen has an interactive environment that consists of two main screens. The specification screen details GA solution parameters giving full control of the solution process to the decision-maker. The result screen provides appropriate output for the decisionmaker to examine the outcome.

There are a number of solution parameters (e.g. crossover probability) to be set by the decision-maker when solving a model by GA. Therefore, this would not make the GA system user-friendly especially when used by less experienced practitioners. Furthermore, being a heuristic search method, difficult models often must be solved (more than once) with different values of GA parameters in order to find the optimal solution or converge around a reasonable local optimum.

The interactive environment of MultiGen system provides the decision-maker with easy and fast access to change the GA parameters, rerun the model, and examine the results interactively. The input button on specification screen helps the less experienced users by providing default values for the GA parameters for the first GA run. The default values will help the decision-maker to examine the behaviour of his/her model. He/she can then alter these values for better and more refined solutions. There exists the possibility of the combination of MultiGen with preference elicitation and interactive methods, as detailed by Vincke [27], in order to perform a more formal search for optimal solutions with regard to the decisionmaker’s underlying preferences.

A selection of difficult problems from different industrial contexts have been solved in order to evaluate the computational performance of MultiGen. The details of this experimentation are given in Ref. [15]. The capability of MultiGen as a heuristic searchbased system is demonstrated by its performance on this set of real life problems. In the same study, the performance of MultiGen is also compared with an intelligent integer goal programming (IGP) system by solving difficult IGP problems [15]. This study shows that the MultiGen system is capable of finding the optimal solution with regard to the decision-makers preferences for models with up to 100 constraints and 200 variables. With a model of over 200 constraints and 200 variables, MultiGen failed to find a good integer solution. These preliminary results give an idea of the scope of MultiGen to solve this particular variety of multi-objectives programmes.

The development of such a package as MultiGen allows good solutions to be produced when solving certain types of difficult, e.g. large integer or non-linear optimisation models. MultiGen may also be used as an alternative solution tool where conventional systems experience difficulties. The system should aid and encourage researchers and practitioners to use powerful evolutionary algorithms such as GA for the solution of operational research and engineering problems. The development of MultiGen is an ongoing process leading to a more robust and flexible MOP system.

## Acknowledgements

This research is supported by the British Engineering and Physical Sciences Research Council (EPSRC), UK (Grant No. GR/M27593).

## References

[1] D.L. Carroll, A single objective genetic algorithm in Fortran, University of Illinois. Public domain code available from http://www.cuaerospace.com/carroll/ga.html.

[2] C.M. Fonesca, P.J. Fleming, Genetic algorithms for multi-objective optimization: formulation discussion and generalization, Proceedings of the 5th Annual Conference on Genetic Algorithms, (1993) 416– 423.

[3] L.R. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning, Addison-Wesley, Reading, MA, 1989.

[4] J.H. Holland, Adaptation in Natural and Artificial Systems, University of Michigan Press, Ann Arbor, MI, 1975.

[5] C.L. Hwang, A.S.M. Masud, Multiple objective decision making-methods and applications: a state-of-the-art survey, Lecture Notes in Economics and Mathematical Systems, vol. 164, Springer-Verlag, Berlin, 1979.

[6] J.P. Ignizio, Linear Programming in Single and Multiple Objective Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[7] J.P. Ignizio, Generalized goal programming. An overview, Computers and Operations Research 10 (1983) 277 – 289.

[8] J.P. Ignizio, T.M. Cavalier, Linear Programming, Prentice-Hall, Englewood Cliffs, NJ, 1994.

[9] D.F. Jones, The Design and Development of an Intelligent Goal Programming System, PhD Thesis, University of Portsmouth, UK, 1995.

[10] D.F. Jones, M. Tamiz, Expanding the flexibility of goal programming via preference modelling techniques, OMEGA, International Journal of Management Science 23 (1995) 41 – 48.

[11] D.F. Jones, M. Tamiz, S.K. Mirrazavi, Intelligent solution and analysis of goal programmes: the GPSYS system, Decision Support Systems 23 (1998) 329 – 332.

[12] D.F. Jones, S.K. Mirrazavi, M. Tamiz, Multi-objective metaheuristics: an overview of the current state-of-the-art, European Journal of Operational Research 137 (2002) 1 – 9.

[13] K.M. Miettinen, Nonlinear Multi-Objective Optimization, Kluwer Academic Publishing, Boston, MA, 1999.

[14] S.K. Mirrazavi, Investigation and Development of Efficient Integer and Integer Goal Programming Systems, PhD Thesis, University of Portsmouth, UK, 1997.

[15] S.K. Mirrazavi, D.F. Jones, M. Tamiz, A comparison of genetic and conventional methods for the solution of integer goal programmes, European Journal of Operational Research 132 (2001) 594 – 602.

[16] A. Osyczka, Multicriterion Optimisation in Engineering with FORTRAN Programs, Ellis Horwood, Chichester, UK, 1984.

[17] M. Pidd, Computer Simulation in Management Science, Wiley, Chichester, 1998, 0471979317.

[18] C. Romero, Handbook of Critical Issues in Goal Programming, Pergamon, Oxford, 1991.

[19] C. Romero, D.F. Jones, M. Tamiz, Goal programming, compromise programming and reference point method formulations: linkages and utility interpretations, Journal of Operatio - nal Research Society 49 (1998) 986 – 991.

[20] M. Sakawa, K. Kato, H. Sunada, T. Shibano, Fuzzy programming for multiobjective 0 – 1 programming problems through revised genetic algorithms, European Journal of Operational Research, (1997) 149–158.

[21] J.D. Schaffer, Multiple objective optimisation with vector evaluated genetic algorithms, Proceedings of an International Conference on Genetic Algorithms and their Applications, (1985) 93– 100.

[22] N. Srinivas, K. Deb, Multiobjective optimisation using nondominated sorting in genetic algorithms, Evolutionary Computation 2 (3) (1994) 221 – 248.

[23] R. Steuer, Multiple Criteria Optimisation: Theory, Computation and Applications, Wiley, New York, NY, 1986.

[24] P.D. Surry, N.J. Radcliffe, The COMOGA method: constrained optimization by multi-objective genetic algorithms, Control and Cybernetics 26 (1997) 391– 412.

[25] M. Tamiz, S.K. Mirrazavi, D.F. Jones, Extensions of Pareto efficiency analysis to integer goal programming, OMEGA, International Journal of Management Science 27 (1999) 179– 188.

[26] A. Vicini, D. Quagliarella, Inverse and direct airfoil design using a multi-objective genetic algorithm, AIAA Journal 35 (1997) 1499–1505.

[27] P. Vincke, Multicriteria Decision Aid, Wiley, Chichester, 1992.

[28] P.L. Yu, Multiple-Criteria Decision Making Concepts, Techniques, and Extensions, Plenum, New York, 1985.

[29] M. Zeleny, Multi Criteria Decision Making, McGraw-Hill, New York, 1982.

![](/api/attachments/6DR73WTR/fulltext/images/a467d373730d86d8fb080193c7784e0cd3e2b01c5a54d617c3d7b7387d097fd4.jpg)  
S. Keyvan Mirrazavi has a PhD in operational research and is currently an IT consultant in London practicing optimisation and scheduling. His areas of interest include software development, optimisation, mathematical programming, and meta-heuristics.

![](/api/attachments/6DR73WTR/fulltext/images/1e03c6dbf05a6f19a0a70902dedaef75bd32911a15d1648fa2d9dd7731242609.jpg)

Dylan Francis Jones has a PhD in operational research and currently holds a senior lecturing post at the University of Portsmouth, UK. His research interests include multiple-objective optimisation and decision support, goal programming, mathematical programming, heuristic methods, and the design of intelligent software for the analysis and solution of the above mathematical methods. He is one of the founders of MOPGP and STAMDA.

![](/api/attachments/6DR73WTR/fulltext/images/4bd673d361d8bc6d62bd449757093c3039ad273f7c297779c93b9e24770542e9.jpg)

Mehrdad Tamiz is a professor and consultant in operational research. He is based in the School of Computer Science and Mathematics, University of Portsmouth, UK. His main research interests are in efficient modelling and solving linear, integer, multiobjective, and goal programming problems, portfolio selection and analysis, risk analysis, and volatility measurement of stocks and shares. He is actively involved with the organisation of the MOPGP conference

series and is the president of STAMDA.
