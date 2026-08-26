---
otero_id: 17000
otero_key: "GTMVDFCX"
title: "A case study on decision support in a non-linear world"
authors: "G. van der Hoek; W. van Donselaar"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90012-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Case Study on Decision Support in a Non-Linear World

G. van der HOEK \*

and W. van DONSELAAR \*\*

\* Econometric Institute, Department of Operations Research, Erasmus University Rotterdam, 3000 DR Rouerdam and \*\* Royal Boskalis Westminster Dredging Company, The Netherlands

This paper deals with a practical decision situation in which a non-linear model had to be built describing the design and operation of a trailer suction dredger. The decision makers were faced with all kinds of stumbling blocks for the application of non-linear optimization techniques. This case study illustrates how a bottom-up decision support approach can stimulate improved decision making both on the operational and tactical level. Besides that the model improvements obtained in the prototyping phase led to remarkably reduced computing cost, a quantitative aspect that was highly appreciated too.

Keywords: Decision Support, Non-Linear Optimization, Design of Trailer Dredgers.

![](/api/attachments/GTMVDFCX/fulltext/images/eb74e7afc4cb66018f210348720de97df017b703b44923e294f70065a5551628.jpg)

Gerard van der Hoek received an M.Sc. from Leiden University (1968) and his Ph.D. from the Erasmus University in Rotterdam (1980). He has since published on Portfolio Selection Models and algorithms to evaluate those models; on the design, analysis and convergence of nonlinear programming algorithms and, more recently, on the embedding of such algorithms in Decision Support Systems for Engineering Design. His publications include Reduction Methods in Non-Linear Pro

gramming: Amsterdam, Mathematical Centre; Introduction in Linear and Non-Linear Programming (Dutch): Leiden, Stenfert Kroese and papers in Mathematical Programming and Management Science. He is currently Associate Professor in Operations Research at Erasmus University Rotterdam.

$^{1}$ The subject discussed in this paper is part of a large R&D project. To this project a number of people have contributed. Especially Ir. J.E. Stada for the Civil Engineering and Ir. J. Pinkster for Naval Architecture were stimulating forces in the project. A lot of numerical experiments with the GRG code were conducted by Drs. J. Vooijs, at that time a student of the Erasmus University. The authors would like to thank the referees for their suggestions to improve the paper.

1. The Need for Decision Support in Building Non-Linear Models

Usually the non-linear programming specialist is involved in solving well-structured optimization problems using his theory and algorithms.

In non-linear engineering design problems, solutions of intermediate models may lead to reformulations such as adding simple bounds on variables or even more deep-going reformulations of the model itself. The physical meaning of optimized variables and the corresponding interpretation of model outcomes stimulate a prototype-building process which non-linear software developers are not always aware of.

In the context of a design problem in shipbuilding engineering, the authors got involved in decision spirals in which down-to-earth optimization results stimulated both tactical decision discussions and research in neighboring disciplines.

This project was started when the application of Lasdon and Waren's GRG2 code for constrained non-linear optimization appeared to be too CPU expensive to solve an earlier version of the design problem. However, it appeared that CPU costs are not the only obstacle for applying non-linear optimization algorithms.

Other more or less mutually related stumbling blocks to be mentioned are:

(i) the identification of the non-linear nature of the problem considered,

(ii) The specification of the non-linear relationships,

![](/api/attachments/GTMVDFCX/fulltext/images/58bbde6ba63f41638f5aad9814402cc65ad9984c7d0da684701244429bbfd3e8.jpg)  
Wim van Donselaar obtained a degree in engineering from the Agricultural University at Wageningen in 1977 and a degree in economics from the University of Amsterdam in 1986. From 1978 until 1985 he worked for a Dutch contractor. First in the field of operations research, later as the companies EDP manager. He currently holds a management position with a Telecommunications company.

(iii) the lack of availability of non-linear programming software,

(iv) the lack of user-friendliness of software (as opposed to commercial linear programming packages),

(v) the lack of expertise in the problem environment,

(vi) the relatively restricted application area of non-linear programming,

(vii) the observation that sometimes straightforward linearizations yield acceptable, approximating solutions.

A remedy to overcome the problems sketched above is to embed the model building process in a decision support approach, which is by itself more suited to cope with the semi-structured decision situations encountered in real life model building. The resulting support system should be 'a coherent system of computer-based technology (hardware, software and supporting documentation) used by managers as an aid to their decision making in semi-structured tasks' (cited from Keen and Scott Morton [1978]).

The case study discussed in this paper is also intended to advocate a bottom-up approach for developing decision support systems. It is the experience of the authors that this approach stimulates a high level of involvement of contributing disciplines and departments, with as a clear spin-off to reconsider model modules on the basis of intermediate results of the prototyping phase. The communication with the different disciplines was smoothed by the interactive shell which was built around the optimization package GRG2.

## 2. Case Description

A trailer suction dredger is a vessel equipped for maintenance work of ports and harbours as well as for capital dredging work. It is a free floating dredger that can easily manoeuvre between tankers and other ships. Fig. 1 shows a schematic lay-out of a trailer suction dredger.

The vessel is equipped with a suction tube that reaches to the bottom of the harbour, through which tube the mud and sand is pumped up and loaded into the cargo hold of the dredger. During dredging the vessel slowly sails the dredging area. When the cargo hold (hopper) is fully loaded the suction tube(s) is (are) hoisted on board and the dredger then sails to the dumping area, where the cargo is discharged. The vessel then returns to the dredging site and in doing so completes the cycle. From this very short description it can be anticipated that the design of such a dredger is a complicated business. Apart from the normal constraints that every naval architect deals with in the design of a dredger, the fundamental production process imposes a number of additional non-linear constraints. Lasdon's GRG code was successfully applied in fulfilling the imposed constraints on a set of simplified relations that govern the design of a trailer dredger at minimal costs. This optimization model yields a starting point in the design spiral dealt within a bigger computer program for computer aided design (CAD) of trailer dredgers. (EMOTRA: Economic MOdel TRAilers). This paper focuses on the problems, failures and difficulties met during the development of the set of initial model relations.

![](/api/attachments/GTMVDFCX/fulltext/images/82c3eb152797a13cb6781f51fc63ff67bc4e1a38fcbcdf6227496f72e5084217.jpg)  
Fig. 1. Schematic Lay-out of a Trailer Suction Dredger.

The design of a new trailer is a complex process not only technically but also organizationally. Although it is a tactical decision, there are strong relations to expertise and knowledge on the operational level. Various disciplines are involved, i.e. marketing, naval architecture, dredging, finance, mechanical engineering, electrical engineering and soil mechanics. As each discipline is involved in the initial design process, this stage can often result in many discussions where individuals attempt to include their personal requirements. This fragmented approach gives difficulties in arriving at a properly integrated and balanced design. The computer program is designed to come to an integrated approach of the various disciplines and to enable a quick settlement of differences giving quantitative instead of subjective answers.

At the beginning of a design procedure a Mission Profile for the dredger is specified, this means the specification of relevant data describing the tasks of the vessel. A number of rules of thumb can be used to produce an initial estimate of the main dimensions of the dredger. The problem dealt with in this study is to reduce these rules of thumb to a number of model relations and constraints and thereafter to solve the model.

## 3. Model Formulation

The model formulation starts with the Mission Profile. The Mission Profile specifies data that fall into three categories.

(1) Working conditions, e.g., sailing distance, suction depth, weather conditions, etc.

(2) Soil data.

(3) Financial data (limit fuel price, interest, etc.).

Added to this Mission Profile are a number of preset choices such as the number of suction-tubes to be used. This is one of the consequences of the structured analysis and design approach followed which advises a balanced partition of the system, see e.g. Page-Jones [1980]. From practice the choice for the number of suction-tubes can also be seen as fixing a certain scenario in which higher management is interested because of not modeled and/or structured considerations.

The resulting optimization model basically consists of a number of simplified relations stating design and performance requirements. In order to be able to develop a model it needs to be clear what is to be optimized. In this model the objective is to minimize the cost per $m^{3}$ dredged spoil. The costs can be roughly split into variable and fixed costs. Variable costs are:

\- Energy,

\- Food and travelling,

\- Maintenance and repairs.

Fixed costs are:

\- Depreciation,

\- Insurance,

\- Personnel.

Although some of the fixed costs contain variable elements and some of the variable costs contain fixed elements the above stated subdivision will be used throughout this paper. The dredging production is closely related to the loading diagram given in Fig. 2.

From Fig. 2 it can be seen that the optimally designed dredger lies somewhere between two extremes: the suction pump on a pontoon with sailing distance zero in the Mission Profile and a cargo vessel with sailing distance infinity in the Mission Profile. This illustrates the importance of the choice of the Mission Profile parameters, hence the dependence of the design of the dredging projects aimed at.

![](/api/attachments/GTMVDFCX/fulltext/images/da335d2fbbc10b59bf5fe57cbcebb2bb7d817a0fd6a30ed194ab97ae239481bb.jpg)  
Fig. 2. Loading Diagram During a Complete Dredging Cycle.

## 3.1. Shipbuilding

The design of a dredger involves the following two working conditions:

(1) Free sailing either loaded or unloaded.

(2) Dredging with the suction tube lowered to the sea bottom.

In the model there are a few elementary variables that govern the design of a trailer dredger. These variables in turn are used to calculate all other variables necessary for the design.

The main variables mentioned above are:

(1) LPP Length between perpendiculars (m)

(2) DRAFT Average draft of the vessel (m)

(3) VLOREL Relative speed of the vessel in loaded condition (m/s)

(4) VTRREL Relative speed of the vessel in dredging condition (m/s)

In the free sailing condition the required propulsion thrust is calculated as a function of length, breadth, draft and sailing speed. The same calculation is done for the dredging condition, here the propulsion thrust is calculated as a function of length, breadth, draft, sailing speed during dredging, resistance of the suction tube and resistance of the draghead against the soil. Here the model ensures that the draghead remains in contact with the soil. The model assumes that the propulsion power installed is the maximum of the above.

Now it is possible to calculate as a derivative the hopper design. In this part of the model it is ensured that the cargo capacity will allow the level of the dredged material in the vessel to be above the surrounding water level.

In absence of a more sophisticated relation, the number of crewmembers is linearly related to the length of the dredger and depending on the type of design. This linear relation can only be so simple because of the definition of the scenarios considered.

The remaining specifications are derived through regression and/or empirical relations. These are the weights of accommodation, propulsion installation, dredging installation, steel, spare parts, electrical installation and various others.

In this part of the model a loop is introduced to check these weights against the calculated water displacement of the vessel.

Next a power balance is calculated for the various powered functions on board. These balance relations are represented by non-linear equality restrictions.

To finalize the shipbuilding design a stability check is performed resulting in a restriction in the model for the so-called metacentric height.

## 3.2. Dredging Production

The dredging production capacity is calculated in $m^{3}/week$ . The variables that govern the dredging production are:

(1) DHDRAG The pressure over the draghead (kPa)

(2) DSUCTU The diameter of the suction tube (m)

(3) FHKNIFE Cutting force of the draghead (kN)

(4) FILTIM The time needed to load the hopper (sec)

A strong relation exists also to the variable VTRREL, the relative speed in dredging condition.

In the draghead a very complicated process takes place in establishing an equilibrium between the mixture quantity and the density of the mixture flow. Internal research established a relation giving the mixture density and the mixture quantity in $m^{3}/sec$ as a result of soil conditions, draghead geometry and hydraulic pressure over the draghead. When these values are known it is relatively simple to calculate the pump power needed.

Next item in the calculation of the production are the overflow losses. When the dredging process starts, a mixture of water and sand is pumped into the hopper. In the hopper the sand starts settling, which results in a layer of water above the sand in the hopper.

It is possible, using a specially designed opening, to return the water collected in the hopper to the sea. In the shipbuilding part of the model it is ensured that it is possible to get rid of the water in this way. It will be clear that when returning the water to the sea, as mentioned above, some sand also leaves the hopper, thus explaining the curved loading diagram in Fig. 2 when the overflow becomes active.

## 3.3. Cycletime Calculation

Referring to Fig. 2 in this chapter the cycletime calculation is described. Let us assume that we start out with an empty hopper. Until the overflow is reached we have a linear relationship between the cargo loaded and time. When the overflow is reached also sand leaves the hopper causing the curve in the loading diagram.

Then the sailing time fully loaded needs to be calculated. This appears simpler than it actually is in practice because acceleration and deceleration effects have to be taken into account too. As a result of these effects it is easily understood that for certain sailing distances the dredger never reaches its specified service speed. When the dredger arrives at the dumping place the cargo is dumped. The time needed for dumping depends on the geometry of the unloading system, the degree to which the hopper is filled, the length of time the spoil stays in the hopper and the spoil characteristics.

Next the dredger sails back to the dredging area in the meantime pumping the water that is left out of the hopper. At a number of places in the described cycle delays are possible that are not discussed here.

## 3.4. Cost Calculation

The costs are all expressed in weekly costs. Fixed costs:

(1) Weekly hire rate: is calculated as a weekly annuity from the acquisition value minus the salvage value.

The acquisition value is the sum of the ten separate amounts of the classes in which the dredger is subdivided. Each group of specifications is represented by an empirical relation.

(2) Insurances: is a percentage of the acquisition price.

(3) Personnel: derived from the number of crew members times the average weekly salaries.

## Variable costs:

(1) Energy is derived from the power requirements during the whole cycle. It is a straightforward calculation to find the fuel consumption per kWh for the various lay-outs of engines and gearboxes.

(2) Food and travelling: depending on the location where the dredger is working the food and travelling cost will vary.

The calculation is based on average food and average travelling costs per crew member.

(3) Maintenance and repairs: calculated from an empirical relation encompassing the elements of the cycle time and power usage.

Adding the variable and fixed costs the weekly costs are known. These can be divided by the weekly production thus giving the costs per $m^{3}$ dredged material which is the objective function for the model.

## 3.5. Constraints and Objective Function

The model consists of 21 inequality constraints and 1 objective function. For reasons of confidentiality, in this chapter a discussion of only some of the constraint functions is given.

(1) G(1) > SUDEPT - DRAFT
It is an upper bound on the draft stating that the maximum draft should always be less than the suction depth.

## (2) $\mathbf{G}(2) > \mathbf{LPP} - \mathbf{VLOREL}^{**}2$

Equation 2 and 3 state the upper and lower bounds on the so-called Froude figure. The method on which the hull resistance is calculated, is only valid within these boundaries.

(3) $\mathbf{G}(3) > \mathbf{VLOREL}^{**}2 - \mathbf{LPP}.45^{**}2$

(4) G(4) > 1.5 - VTRAIL
Specifying the maximum speed of the dredger during trailing.

## (5) $\mathbf{G}(5) > 10000$ . - VOLHOP

It is an upper bound on the hopper capacity and can also be used to impose other maximum hopper capacities on the design.

## (6) $\mathbf{G}(6) > \mathbf{PRESIN} + 80$ .

The incoming pressure in the dredgepump PRESIN is a negative variable, it should never fall below -80. kPa because then the dredgepump starts cavitating which would completely destroy the pump. Apart from that the theory used does not include cavitation effects.

## (7) G(7) > 0.9\* VOLHOP - M3HHCY

This is another constraint due to the validity of the theory, in this specific case the overflow losses. It states that the hopper will not be loaded for more than 90% with settled material.

(8) G(8) > NBVMAX - NBV
Inequality 8 states that a dredger should be designed costing not more than NBVMAX.

## (9) G(9) > M3HSWK - M3WKMI

This constraint specifies that a dredger should be designed capable of a minimum weekly production of M3WKMI.

## (10) G(10) = COSTM3

This is the objective function composed of the weekly production costs divided by the weekly production in m3.

## 4. Practical and Theoretical Problems in the Model Formulation

## 4.1. Practical Problems in the Model Formulation

The major practical problem in the model formulation is the validity of the physical theory.

Since dredgers are expensive capital assets they are not readily available for research experiments necessary to provide comprehensive data.

In practice this means that measurements can be done only in actual working conditions if they do not interfere with the operations. The consequence is that extremes are never properly researched in operational conditions.

As a result the theory derived is only valid for a specific part of the real world. For production predictions this is fully acceptable since dredgers will not normally operate in extreme conditions.

The optimization procedure tends to investigate specifically that part of the physical world for which the theory is not validated. In order to control the optimizer, every possible lead to the part of the physical world had to be cut. The effect is an extensive number of functions that are not differentiable throughout. A particular salient example in this respect is the following one that shows that a starting point should be chosen very carefully.

In the dredging process obviously one should not load more spoil into the hopper than the dredger can carry, since otherwise it would sink.

However, in the formulation of a non-linear programming model, this means that only one constraint is not satisfied, this is usually corrected in the next iteration.

If the starting point in relation to FILTIM is chosen wrongly, unfortunately, the design process will start with a submarine, a situation that is not coped with in the model formulation.

The above stated constraint causes no problems in the other iterations, because a dredger is designed according to specific international standards. The rules state for instance a minimal required free board. The Newton steps in the line search of the optimization routine never caused unsolvable infeasibilities.

This problem is actually solved by starting with FILTIM being a sufficiently small number.

In the model also a number of empirical formulae derived from curve fits have been used. Either quadratic fits or linear regression equations are advisable in these situations. The limited validity of these approximating formulae forced the application of step size limitations in the optimization routine.

## 4.2. Theoretical Problems in the Model Formulation

The model developed requires the solution of a non-linear optimization problem with several pitfalls.

The problem functions, both the objective function and the constraint functions, allow the existence of local optima; the functions are not differentiable everywhere. This means that preferably an algorithm should be developed for the optimization of a non convex objective function on a non convex feasible region in the presence of points where the problem functions are not differentiable. These requirements cannot be met within the deadlines imposed on such a practical project. Hence, use must be made of available, well documented, thoroughly tested software for differentiable, local, constrained optimization. Lasdon and Waren's GRG2 code satisfies these requirements.

Furthermore, it is a known fact that there is no algorithm for NLP which solves every NLP problem most efficiently, even given an implementation of an algorithm, there is no unique choice of parameters within the code which yields most efficiently the solution for every problem. Hence, once the choice for a code has been made, the user is faced with the problem of “tuning” the parameters with respect to his problem and with the problem of tailoring his problem to avoid numerical instabilities. While the ‘tuning’ of the parameters will usually be accomplished during the experiments, a great deal of computational and numerical complications can be avoided by properly defining the objective function and the constraint functions of the problem.

In absence of a unique ‘best’ model, which approximates best reality in some specified sense, the designer has some freedom in formulating his objective function and his constraint functions. Besides that, a proper scaling of the problem functions and of the variables is necessary for non trivial models. Well known scaling devices are: scaling of the problem function such that all relevant function values will be of a similar magnitude; a similar scaling of the variables together with a corresponding adjustment of the dimension of the variables or, finally, some form of automatic scaling, used in algorithms such as the Self Scaling Variable Metric algorithms cf. Oren and Luenberger [1974] or the so-called collinear scaling, cf. Sorensen [1980].

4.3. GRG Imposed Restrictions on the Model Implementation

The main reasons for choosing Lasdon and Waren's GRG2 reduced gradient code to solve the optimization model are the fact that linear equality constraints are treated very well by this kind of algorithms and the availability of this thoroughly tested and well documented code (for an up-to-date overview of currently available codes, their efficiency and their effectiveness the experiments reported in Schittkowski [1980] supply an abundance of information).

Apart from the general points discussed above, the design of the GRG code imposes some further restrictions on the model implementation. We shall focus on I/O requirements and facilities and flexibility of the code to adapt small changes in the model in this chapter. A concise description of the code will precede this discussion. We shall restrict ourselves to those aspects relevant for our purpose. For a complete description of GRG we refer to Lasdon and Waren [1980].

## 4.3.1. A Concise Description of GRG2

Lasdon and Waren's GRG2 code is a FORTRAN IV program which uses Generalised Reduced Gradients to solve the general non-linear optimization problem

$$
\min F (X)\tag{1}
$$

s.t.

$$
C _ {i} (X) = 0, \quad i = 1, \dots , m,\tag{2}
$$

$$
L _ {j} \leq X _ {j} \leq U _ {j}, \quad j = 1, \dots , n,\tag{3}
$$

where

$$
\begin{array}{l l} X & \text { the } (n \times 1) \text {-vector of variables } (X _ {1}, \dots X _ {n}) \\ & \text {(slacks are included),} \end{array}
$$

$F(X)$ the (non)-linear objective function,

$C_i(X)$ the $i$ th (non)-linear constraint function, $L_j$ , $U_j$ lower- and upper bound of $X_j$ , $j = 1, \ldots, n$ .

Starting from a feasible point $X^{0}$ , which can be generated by the algorithm itself, suitable sets of m basic variables $X_{b}$ and $(n - m)$ non-basic variables are selected. Then equation (2) becomes

$$
C _ {i} \left(X _ {b} \left(X _ {n b}\right), X _ {n b}\right) = 0,\tag{4}
$$

in which $X_{b}$ occurs as a function of $X_{nb}$ . The calculation of $X_{b}$ requires the solution of a set of non-linear equations. In this way the problem is reduced to an unconstrained optimization problem in $(n - m)$ non-basic variables.

This unconstrained problem in turn is further simplified by distinguishing amongst the non-basic variables between bounded variables (at their lower of upper bound) and super-basic variables (between their bounds). The unconstrained optimization is performed now with respect to these super-basic variables; during this optimization it is checked regularly if the set of super-basic variables has to be changed, if the bounded variables must be kept on their bounds and if the constraints are still satisfied. Here a pseudo Newton algorithm is used repeatedly to check feasibility of intermediately generated points. The algorithm stops if the second order conditions are satisfied or if no significant objective improvement is achieved in M (a user supplied number) consecutive iterations.

## 4.3.2. Input Requirements

The user has to supply the GRG subroutine with data defining the current optimization problem such as: problem functions, bounds on variables, initial guess and several parameters governing the line search precision, overall precision, a parameter to select one of the available algorithms for unconstrained optimization (conjugate directions, DFP, BFGS).

The input file requirements make the code less attractive for applications in which the user wants to solve a number of only slightly differing problems. For instance the addition of one constraint (e.g. a maximum new building value for the vessel) or other small changes in the problem formulation cannot easily be done.

The user also has to define a subroutine GCOMP in which all model relations are given. In this case GCOMP has the structure as in Fig. 3.

The different blocks of GCOMP have different backgrounds: accounting, civil engineering, naval architecture, ship building engineering. The departments concerned within Boskalis each supplied us with their block of GCOMP, using dimensions and ranges of variables usual for them. In order to keep their input in GCOMP, recognizable scaling and descaling devices had to be inserted into the optimization program.

## 4.3.3. Adding options to GRG2

The GRG2 code itself is a big set of sub-routines which cannot easily be modified. The complexity of the code, the many relations between the modules prevent the user from trying to incorporate additional options which seem to be simple at first glance. However, we expect the following options to be fruitful: A (Self) Scaling Variable Metric update for the unconstrained optimization, or the use of some initial scaling device. We expect those two options to be advantageous since it is known that (initially) scaled BFGS and its variants allow for the use of an inexact line search whereas Davidon–Fletcher–Powell requires an exact line search. Because each check on feasibility during the line search requires the solution of a set of non-linear equations, the line search will be costly. We may expect a reduction in costs when incorporating such alternatives, at the same time maintaining or even improving the efficiency and the robustness of the algorithm.

![](/api/attachments/GTMVDFCX/fulltext/images/de0f9a4f4adef515e90da6db5ae233f2a650e2a7d5abfa3e4fd71d2ca184b099.jpg)  
Fig. 3. Schematic Subdivision of the NLP Model in GCOMP.

## 4.3.4. Output Facilities for GRG2 and EMOTRA

The application of a sophisticated code like GRG in a modeling environment requires user friendly output facilities for the model as a whole. The designer of the trailer dredger will primarily be interested in optimal values of his decision variables and of his objective function. The dimensions of the vessel will be more appealing to him than intermediate messages of the optimization routine. That is why GRG2 should be incorporated as a reliable black box in the frame work of the whole EMOTRA model. Ideally the EMOTRA project should lead to an interactive computer program to be used as a learning tool for designers and for suppliers of modules and constraints of the model. The insight would be extended even more if a sensitivity analysis could be made available.

## 5. The Modeling Process

Basically two problems played an important role in the model formulation.

(1) Numerical difficulties due to the restricted validity of the theory.

(2) Understanding the influences of the various constraints on each other and the model performance.

The model very quickly became so complicated that it was not possible to see through the logic and to understand what happened anymore. Of course, this causes difficulties in validating the logic. To this end specially developed test programs were used to show in a step by step method and graphically what was happening.

The problem formulation turned out to be a continuous process of extending the model by adding and reformulating constraints and reducing it again by deleting others with the primary objective of finding solutions in the feasible area and not directly to finding an optimum. The process was governed through comparison of numerous measurements in operational conditions.

The model formulation itself also required a review of the existing theories related to the prediction of the production. It is very important to use meaningful constraint functions, that means meaningful to the discipline involved. In this respect it can be stated that an additional constraint is certainly acceptable if it enhances the clarity of the model. One example shows that in mathematical modeling care should always be taken in the straightforward usage of the same expressions as the relevant discipline does.

In naval architecture the usage of ratios describing the vessel's dimensions is quite common. These ratios involve length, breadth and draft. In one special case during the model formulation it turned out that all three ratios could be negative without violating any constraint. However, the calculated required propulsion power became negative, which had a positive effect on the cost per $m^{3}$ in the sense that the energy costs were reduced. This caused to totally illogical design for which the model is not intended.

## 6. Results and Experience with the Model

The model is built to support decision making. This means that the decision maker should have confidence in the results produced by the model. Such a confidence can only be gained through extensive usage, providing insight in weaknesses and strength of the model. Two specific experiments which were performed will be described shortly now. They both concern optimization aspects which turned out to be of great importance for the interpretation of the model results and for the computing costs.

Both the experiments concern the following mission profile parameters:

Density water,

Suction depth,

Distance dredging-discharge area,

Percentage of ship-on-duty time lost to delays,

Percentage dredgetime needed for manoeuvring,

Grain size distribution,

Sharpness sand,

Water temperature,

Fuel price.

Restrictions imposed in the model formulation:

Maximum allowed new building value of the vessel,

Maximum draft,

Minimum production.

Variations in the design to be selected by the decision maker:

Number of suction tubes,

Position of the dredge pump.

Split hopper or bottom doors.

Action radius (storage capacity for fuel and water).

The starting point $X^{0}$ used for chapter 6.1 is given by the following choice for the variables defined in section 3.1. and 3.2:

1. LPP (length): 90.0 m

2. DRAFT: 5.0 m

<table><tr><td>3. VLOREL:</td><td>5.0 m/s</td></tr><tr><td>4. DHDRAG:</td><td>75.0 kPa</td></tr><tr><td>5. DSUCTU:</td><td>0.90 m</td></tr><tr><td>6. VTRREL:</td><td>1.5 m/s</td></tr><tr><td>7. FHNIFE:</td><td>50.0 KN</td></tr><tr><td>8. FILTIM:</td><td>2400.0 sec</td></tr></table>

The stopping criterion of the GRG code is: either the Kuhn–Tucker optimality conditions are satisfied to within $10^{-3}$ or the total fractional change of the objective function is less than $10^{-3}$ in 3 (or sometimes 4 or 5, if the user wants to impose this) consecutive iterations.

## 6.1. Efficiency and Robustness of the Variable Metric Option in the GRG code

The optimization of the reduced problem is carried out using the DFP or the complementary DFP (:BGFS) variable metric algorithm by setting the parameter CG4 or CG5 respectively. When a variable metric method is used, the user has the option to allocate memory space for storing and updating the concerning Hessian matrices. If the dimension of the reduced problem (the number of superbasics) exceeds the user supplied bounds, the algorithm switches automatically to a conjugate gradient minimization of the reduced problem. Varying this storage space from 0 (no space) to 8 (the maximal number of superbasic variables) the following is observed;

\- if DFP is used and the so-called CG-option becomes active (which means that the routine switches automatically to a conjugate gradient algorithm to solve unconstrained non-linear subproblems), the costs for optimization increase always and sometimes the routine failed to converge;

\- if the CG-option becomes active when using the BFGS update strategy, the solution is always reached, though at higher costs.

The conclusion is that it is always advisable to use the (default) BFGS variable metric algorithm to solve the unconstrained reduced problem. The user should be aware of the fact that he has to declare sufficient memory space for storing and updating the Hessian matrix.

The next point of interest is the required exactness of the line search. The user supplied parameter ITLIM governs the precision with which the line search determines the line minimum. ITLIM is the maximum number of Newton calls in one line search. Table 1 shows the influence of ITLIM on the optimization, where F\* stands for the cost per m³ dredged material.

Table 1.  
Influence of line search precision.

<table><tr><td>ITLIM</td><td>4</td><td>6</td><td>8</td><td>10</td></tr><tr><td>function evaluations</td><td>142</td><td>208</td><td>192</td><td>345</td></tr><tr><td>iterations</td><td>22</td><td>30</td><td>25</td><td>37</td></tr><tr><td>Newton calls</td><td>67</td><td>89</td><td>84</td><td>133</td></tr><tr><td>F*</td><td>1.61</td><td>1.48</td><td>1.45</td><td>1.48</td></tr></table>

From these results we decided to use ITLIM = 8 as the preferable value for the further experiments. This results in a so-called inexact line search and prevents spending too much time in solving systems of non-linear equations to investigate points during the line search.

## 6.2. Non Convexity in the Problem Formulation

The mathematical model defined in chapter 3.5 contains non convexities. In the experiments to be reported in this chapter, we varied initial points for the optimization, to verify the existence of different local optima.

However, we limited ourselves to starting points which were both physically and technically realistic. These additional constraints have a clear impact on the conclusions which can be drawn from table 2 below: starting from different, physically and technically realistic starting points, the routine always located the same optimum.

In other words: all these starting points are lying in the region of attraction of one optimum. Clearly the added restrictions cut off mathematically existing local optima, which are not relevant for our design.

The different starting points reported in Table 2 were obtained from the starting point given above by varying initial values of the variable DSUCTU (we chose 50–100 cm) and LPP (we chose 50–100 m). Note that the existing differences in F\* and in the values of the variables do not lead to a differently designed trailer.

## 6.3. Gains Obtained by the Application of the DSS Approach

The formulation of the mathematical model for the design of trailer dredgers has clearly been improved by the DSS approach in conducting the experiments. Managers were assisted in their decisionmaking and the effectiveness of decision-making was clearly improved. In so far, well known criteria (cf. Keen and Scott Morton [1978]) were satisfied. The project also shows the great difficulties arising in modeling a complex technical situation and to understand the internal logic and implications even in a relatively small model.

Table 2.  
Objective function values $F^{*}$ reached for varying values of DSUCTU and LPP.

<table><tr><td colspan="2">Case 1</td><td colspan="2">Case 2</td></tr><tr><td>DSUCTU</td><td>F*</td><td>LPP</td><td>F*</td></tr><tr><td>50 cm</td><td>Failure</td><td>100 m</td><td>1.45</td></tr><tr><td>60</td><td>1.45</td><td>90</td><td>1.45</td></tr><tr><td>70</td><td>1.46</td><td>80</td><td>1.57</td></tr><tr><td>80</td><td>1.48</td><td>70</td><td>1.45</td></tr><tr><td>90</td><td>1.45</td><td>60</td><td>1.45</td></tr><tr><td>100</td><td>1.45</td><td>50</td><td>1.53</td></tr></table>

Furthermore, to be more concrete, compared with the original model, 8 out of 21 constraints were removed from the model, two variables were replaced by other, more appropriately chosen variables and two nonlinear equality constraints (extremely hard to handle numerically) could be replaced by apparently binding inequalities. Also, some other constraints were reformulated and a draft restriction was added. This always active restriction clearly accelerated the optimization process. The GRG2 routine always stopped because of neglectable objective function improvement in consecutive iterations. The CPU time required on a HP 3000 for solving the optimization model was reduced to 30% of the time needed in experiments with the original model. This made it possible to run the program in daytime instead of overnight, hence the response time improved significantly and supporting decision making meetings can now be done more efficiently. Qualitatively, the insight in the formulation and the impact of modules supplied by engineering and naval architecture was deepened profoundly.

With respect to the evaluation of the DSS approach in the project, it can be said that several goals were met. In the prototyping phase several differently and more or less independently operating departments got involved in a joint project. The benefits obtained not only concerned the design process as a whole but also the contributing disciplines themselves. An improved, controlled design process was achieved in which different organisational levels of the company were strongly involved.

For the non-linear optimization specialists, the DSS approach broadened their scope and view on both the applicability of their tools and the way in which the really non-linear world can benefit of them.

## References

Bus, J.C.P. (1980), Numerical solution of systems of non-linear equations, M.C. Tract 122, Amsterdam.

Hoek, G. van der (1980), Reduction methods in non-linear programming, M.C. Tract 126, Amsterdam.

Keen, P.G.W. and M.S. Scott Morton (1978), Decision Support Systems, an organizational perspective, Addison-Wesley, Reading, MA.

Lasdon, L.S. and A.D. Waren (1980), Generalised reduced gradient software for linearly and non-linearly constrained problems, Operations Research Department of Computer and Information Science, Cleveland, Ohio.

Oren, S.S. and D.G. Luenberger (1974), Self scaling variable metric algorithms, part 1, criteria and sufficient conditions for scaling a class of algorithms. Management Science, 20(5).

Page-Jones, M. (1980), The practical guide to structured systems design, Yourdon Press, A Prentice-Hall Company, Englewood Cliffs.

Schittkowski, K. (1980), Nonlinear Programming Codes, Information, Tests, Performance, Lecture Notes in Economics and Mathematical Systems no. 183, Springer-Verlag, Berlin.

Sorensen, D.C. (1980), The Q-superlinear convergence of a collinear scaling algorithm for unconstrained optimization, SIAM J. Numer. Anal, 17, 014–114.

Stada, J.E. (1980), Produktieberekening sleepzuigers in zand (in Dutch; 'Production calculations cutter suction dredgers for sand'), Confidential, Internal Research Project, Royal Boskalis Dredging Company, Papendrecht).
