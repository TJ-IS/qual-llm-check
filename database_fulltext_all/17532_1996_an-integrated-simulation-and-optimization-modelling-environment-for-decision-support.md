---
otero_id: 17532
otero_key: "ZDKWY952"
title: "An integrated simulation and optimization modelling environment for decision support"
authors: "Giorgio Guariso; Martin Hitz; Hannes Werthner"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00058-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An integrated simulation and optimization modelling environment for decision support

Giorgio Guariso $^{a,*}$ , Martin Hitz $^{b}$ , Hannes Werthner $^{c}$

$^{a}$ Dip. di Elettronica e Informazione, Politecnico di Milano Piazza Leonardo da Vinci 32, 20133 Milano, Italy $^{b}$ Institut für Angevandte Informatik und Informationssysteme, Universität Wien Liebiggasse 4 / 3-4, A-1010 Vienna, Austria $^{c}$ Institut für Statistik, Operations Research und Computerverfahren, Universität Wien Universitätsstraße 5, A-1010 Vienna, Austria

## Abstract

A general framework and a specific implementation of a software environment for model prototyping, simulation and optimization are presented. The integration of simulation and optimization, and the possibility of comparing experimental results under complete user control represent the central parts of the proposed approach. Optimization is performed by repetitive simulation runs under the control of an optimization method. The integration of simulation and optimization as well as the post processing facilities offer an effective support to the classical phases of the decision process: intelligence, design, and choice. The software is based on an object-oriented structure and encourages the user to develop his own hierarchy of model classes and experiments.

Keywords: Modelling and simulation; Integrated simulation environments; Optimization; Decision support systems

## 1. Introduction

Solving complex problems, such as those encountered in environmental planning and management, requires a set of human activities that can only partially be supported by a computer system. In fact the literature on decision support systems has recognized for a long time that most complex problems are inherently unstructured or poorly structured so that a satisfactory solution may be found only by a continuous interaction between the computer and the human operator. Many authors $[1,15,16,29,32]$ have tried to define the necessary steps that lead to the solution of such problems. Whatever scheme is taken, there is a certain number of functions that can only be performed by the operator (typically all the aspects concerned with the formalization or, at least, the description of the problem), while other functions (such as selection of a suitable model, running a simulation, optimization of a choice) can be mainly committed to the computer. However, it is well known that the path from an unstructured problem description to a formal problem statement is a continuum where a definite subdivision of tasks is impossible.

In the following, it is assumed that one of the key activities necessary to solve a complex problem is modelling. A computer environment is presented for supporting various phases of this activity, from model building, to simulation, optimization and comparison of different alternatives. This approach is intended for general use and thus does not include any facility for model or parameter choice related to a specific application domain. Such knowledge can, at least in part, be represented and used in a computerized modelling environment for instance by an expert system component (see $[25]$ for examples in the area of environmental modelling), but it must rely on the availability of a specific domain expertise, and thus strongly narrows the applicability of an integrated modelling environment.

The computer environment presented in the following is thus intended to be used by people in different domains who are able to describe a problem by means of equations, including the formalization of the effects of a decision, and who want to understand if such a decision is acceptable or to select the most convenient one within a limited class of alternatives.

Indeed, the facilities for the comparative evaluation of different alternatives and for their optimal selection are the most innovative ones and discriminate the modelling environment presented herein from many other commercial or research packages developed in the recent years (for instance, $MATRIX_{x}$ [28], STELLA [22], TESS [30], or [6] and [1]).

Model development requires these facilities at different stages. Parameter estimation is normally performed by optimizing, with respect to model parameters, a measure of the distance between real data and simulation results. Sensitivity analyses can be automatically performed by repeating a simulation with a set of different values of a certain parameter. Optimal control problems can sometimes be solved by assigning a given functional form to the controller and optimizing its parameters. The choice of the preferred model for a specific real system must be performed according to various indicators such as mean error, maximum error, and so on. A number of different control policies is usually judged according to several attributes, since it is very rare that a complex problem can be formulated as a single objective mathematical programming problem. Finally, in a complex and possibly poorly structured problem, it is almost impossible to define, prior to simulation, the significant results and the form of their presentation. It is normally the analysis of the first results which poses new questions and clarifies which additional output must be provided. Post-processing of simulation results is thus essential for supporting a really interactive output definition and enhancing the understanding of the problem under analysis.

Two roots form the basis of the proposed approach: The first stems from Simulation and Software Engineering. An object-oriented approach is used both in software design to allow a strong integration of the various modules and in model definition, where the user is encouraged to define his own hierarchy of model classes. The second basis is Operations Research that provided the theoretical framework for embedding simulation and optimization. The software environment can in fact solve traditional static optimization problems or run dynamic simulation models or integrate the two approaches to deal with the type of more complex problems mentioned above.

The authors' research activities of the last years in the area of Simulation and Decision Support Systems have lead to the development of various packages in different software and hardware environments [12-14]. They focus on the following tasks:

\- fast prototyping of simulation models;

\- storage, retrieval and editing of models developed;

\- storage, retrieval and editing of data for performing simulation experiments;

\- parameter estimation;

\- optimization by repeated simulation runs;

\- testing of optimal control policies;

\- evaluation and comparison of the outcomes of different decision alternatives.

In the following three sections, we will analyze how these functions can support the decision-making process by making reference to its classical subdivision in three phases: intelligence, design, and choice, respectively. Phase I can be interpreted as the formalization of the problem, when the user defines a set of equations which are thought to be representative of the original situation. Phase II corresponds to a more detailed definition that includes the selection of all the required numerical values, within the general functional description already defined. Phase III compares the results of alternative problem formalizations and/or alternative numerical values in order to support a final selection.

Although we believe that this view indeed reflects very well the mainstream activities during the decision making process, it should be noted that we do by no means advocate a pure “waterfall” approach. On the contrary, it is clear that the process is in fact inherently iterative (if not recursive), especially when the problem is a priori not (yet) well defined, as each of the steps in itself involves some decision making that may in turn require problem (re-)formulation, experimentation and analysis, leading to the widely acknowledged cyclic process model (for a recent discussion, see [31]).

Throughout the following sections, the problem of deciding a policy for the management of a natural population of wild animals, precisely an ungulate population in an Alpine environment, will be used to demonstrate the capabilities of the software environment. The example uses one of the available software environments, MoBase [13] running in LISP on a LISP machine. Obviously, the complexity of these kinds of problems (see for instance [5]), prevents the possibility of a detail account of all the development (e.g., the selection and calibration of the models of the systems involved) and thus it will be illustrated as if the three phases could be followed in a simple, sequential way.

Section 5 will finally describe the overall design and architecture of the software environment, highlighting the integration of the different component modules. Such an architecture summarizes all the characteristics of the prototypes already developed.

## 2. Problem formulation (Intelligence)

The intelligence phase can be supported by allowing the user to search in a problem context space, i.e., to look for or to enter data and models that define the original situation in an acceptable way. This means that his activity should not be limited to the development or the selection of a model representing the physical system under consideration. Most probably, the problem formulation process will start from retrieving and analyzing (e.g., performing some statistics or even simply plotting) the data available for the problem at hand, then will go through the selection of a model (or a set of suitable models) of a physical system, and will be completed by the choice of the information-decision structure within which such a system will be operated. Each time the user goes through this phase, he will thus define not only the classical simulation model, but also a set of data to be used and the type of management actions to be evaluated.

It is fairly obvious that data can be suitably managed, analyzed and presented using a data base management system, however, the organization of model definition, storage and retrieval is more complex.

A model base can serve as a repository for model classes, i.e., for structural definitions of different types of models. The variety of possible models, considered in the following, is restricted to the classical definition $[33]$ based on input, state and output variables related by a set of ordinary differential or difference equations. They can be partitioned into three main classes: basic, static and compound models. Basic models are simply standard dynamic models, while static (memoryless) models are represented by non-dynamic relationships. Compound models are aggregations of models of any type obtained by connecting the input and output variables of the components. Note that optimization models are not present in this classification since they will be considered, as explained later, as particular procedures for the use of the models in the base.

A model class stored in the model base must be defined by the following set of fixed attributes which the user can modify, but not cancel:

\- A class name, which should be as explanatory as possible of the class main features.

\- An extensive textual description of the relevant characteristics of the model class (both these items support to different extents the user selection within a specified application domain).

![](/api/attachments/ZDKWY952/fulltext/images/7da879c5dabf46d4c51438147f6f9eceb4edb66107e2e60af5b654ef320ae912.jpg)  
Fig. 1. Class lattice of the proposed modelling environment.

\- A (possibly empty) set of input variables. In the context of modelling and simulation, the term variable will always denote a conceptual place holder for time dependent values $^{1}$ . Each variable is described by a name, unit of measurement, range of permissible values, and a textual comment.

\- A set of output variables (each defined by name, equation, textual description, unit of measurement, and value range).

\- A (possibly empty) set of model parameters. In contrast to variables, parameters stand for time independent scalar quantities used within a model. Each parameter is described by name, textual information, and default value.

\- A time unit.

\- A time step for discretization of differential equations (this is, in a certain sense, a characteristic of the model since its correct value depends on both the parameters and the equations of the model).

Basic and compound model classes must contain in addition:

\- A set of state variables (each described by name, textual information, equation of the transition function, value range and default initial value)

\- A default simulation method, i.e., a numerical procedure for solving recursive algebraic equations in case of discrete time systems or differential equations in case of continuous time systems.

While basic and compound models look similar within this framework, they differ in so far as the above attributes are given explicitly for basic models, whereas for compound models they are deduced from attributes of their components at the time of creation (see below).

The operations defined on the model base must be:

\- definition of a new class,

\- deletion of a class,

\- editing of a class definition, and

\- instantiation of a class.

These operations allow the user to define and manage his own lattice of model classes. In fact, he can specify new classes by progressively specializing existing ones (both instantiating a set of class attributes or adding new ones) or by generalizing them, deleting some attributes of the class from which it is derived (see, for instance, [27]). Though each class has a unique “parent” class, in the sense that the user derives it from a single existing class, he must be allowed to arbitrarily modify them during the editing process. The overall class lattice created in this way may be represented as in Fig. 1. There exists a limited number of reserved abstract classes that the user can only specialize (solid connections in Fig. 1 represent inheritance) and a much larger number of user classes connected by a more general “is-like” relation (dotted lines in Fig. 1) empirically established by the user at the time of creation (for a detailed discussion of this issue, see [18]).

![](/api/attachments/ZDKWY952/fulltext/images/8e23dbcd9b4c18251c435c01c557709ef8dfe30b8eff3d310e174fcd8be7f1f9.jpg)  
Fig. 2. A compound model consisting of three submodels.

This structure allows the maximum flexibility to the user so that he can create the structure of classes that best reflects his “problem space understanding” as recommended in [7].

To specify the topological information of compound models, the user first selects component model classes from the model base and then must define, for instance in graphical form, the connections between input and output variables of the components. For compound models of deeper structure (i.e., having compound models as components), both, the bottom-up and the top-down approach must be supported. While the bottom-up approach is straightforward – connecting existing models to yield a new (compound) model – the top-down definition process may start off with dummy models (black boxes with a specified number of input and output variables, but without internal structure) in order to specify high-level relationships between the components before going into any detail. The definition of such a dummy model may be completed at any time prior to simulation. An example of a compound model defined in this way is presented in Fig. 2, where submodels are considered black boxes and therefore only input and output variables are shown (input and output variables are represented by arrows entering the boxes from the left and leaving them on the right side, respectively):

Seen from the top level, the system consists of three components: An ungulate population, the grass they consume (Food), and a hunting policy (Manager). The links between Food and Population represent the natural mutual feedback between these models, while the feedback loop through Manager represents the control mechanism to be decided upon. Food is a basic model, Manager a static one and Population is in turn a compound model composed by two age classes, namely reproductive animals (variable “Adults”) and non reproductive ones (variable “Young”).

Both classes are supposed to feed with different metabolic rates (these parameters are not shown in Fig. 2) on a common resource (variable "Grass") and be depleted by hunting; their growth rate can be assumed to follow the Michaelis-Menten dynamics so that it reaches a limit value when the food is abundant. Grass dynamic is represented (see, for instance, [10]), by a logistic growth perturbed by a random noise representing variable environmental conditions.

The hunting model is a static one and may represent two different policies: a constant number of hunting licenses (policy class A) or a variable number computed every year as a linear function of the adult population in the preceding year (policy class B). Thus, under policy class B more licenses are issued when more animals are available. The two policy classes are defined by the equation of the Manager model which describes the dependence of its output variable “HuntingEffort”, from the input variable Adults and the model parameter P (the variable t represents time measured in years):

Policy A: HuntingEffort(t) = P

$$
\text { Policy   B: } \text { HuntingEffort(t) } = \text { P } ^ {*} \text { Adults(t - 1) }
$$

The problem is thus to select the most effective policy for determining the hunting effort.

In practice, during construction of a compound model, the model base manager must supervise the coupling of input variables to output variables in order to ensure unit-compatibility, thereby supplying conversion functions on the links where necessary, and completes the user's specification by inferring the compound model's attributes from its components. In this aggregation process, the possibly different time units and time steps of the components are taken into account and the time step of the compound model is computed as the greatest common divisor of all the components' time steps. However, the simulation itself should proceed for each component with its own time step, thus allowing the required precision (discretization can be coarser for blocks with a slower dynamic) with a minimum of computation.

## 3. Defining and conducting experiments (Design)

The use of models for simulation implies the definition of what is called an experiment [33]. This means that all the items that are not relative to the model structure have to be fixed. An experiment E is defined as a tuple

$$
\mathrm{E} = \left(\mathrm{M}, \mathrm{t} _ {\mathrm{o}}, \mathrm{t}, \mathrm{X} _ {\mathrm{o}}, \mathrm{U}, \mathrm{P}, \mathrm{m}, \mathrm{k}\right)
$$

which contains the model M, the values of the initial and final time $t_{o}$ and t, the initial values of the state variables $X_{o}$ , the input functions U for the total interval, a set of values P for the parameters, and a method m to perform the simulation. The schedule k is necessary in the case of multiple experiments (see below).

Experiment planning is in itself a nontrivial task. The selection of input, parameter and initial state values is almost always entirely relying upon the user's knowledge of the real problem. Only few theoretical results (mainly for linear systems)

are available to understand in advance if a given input sequence is significant or how the output will depend on some parameter value. Even the user is not always well aware, at the beginning of the study, of the kind of results he is interested in and which features of the model will be more significant for the solution of a specific problem. Thus, a number of simulations will usually be performed, each one corresponding to a different experiment.

This repetitive use of simulation is also typical of many other problems, such as those quoted in the Introduction. For instance, to plan the size of a system it may be useful to simulate how it will be managed, and to optimally control a plant may imply to simulate its future conditions. It is thus of relevance to find a common framework for integrating both optimization and simulation models. Only few attempts in this direction have been reported in the literature and they were mainly aimed at constructing simulation software packages, including some parameter estimation facilities [2,9,24].

![](/api/attachments/ZDKWY952/fulltext/images/51d3e15b106e3e21ea8da107f4cbea866ea1828ca6ced8b97a4886224f238bff.jpg)  
Fig. 3. Defining an experiment with an optimization method.

For the purpose mentioned above, it is useful to introduce a multiple experiment as an extension of the (elementary) experiment previously defined. A multiple experiment is defined as a set $\{E_{1}, E_{2}, ..., E_{N}\}$ of experiments controlled by a schedule k. A schedule may include, for instance, a procedure to access the database several times to get different values of the input functions. A slightly more complex schedule might be an algorithm to subdivide a range of possible parameter values into evenly spaced intervals and to simulate the system in correspondence with those parameter values. A third, even more complex schedule, could plan new experiments on the basis of the results of preceding ones, for instance, aiming at optimizing a suitable performance indicator by parameter variation. The latter allows to define a traditional optimization problem as a multiple experiment performed on a simulation model (sometimes this is called “goal-oriented simulation”). One may also imagine the case in which the performance indicator is not dependent upon time and thus there is no simulation model to run: this is the classical problem dealt with by the majority of Operation Research techniques.

The schedule k, which characterizes the multiple experiment with respect to the elementary one, may be defined by the following set (see Fig. 3):

$$
\mathrm{k} = (\mathrm{N}, \mathrm{R} (\mathrm{P}), \mathrm{S} (\mathrm{t}, \mathrm{P}, \mathrm{V}), \mathrm{C}, \mathrm{O})
$$

where

\- N is the maximum number of elementary experiments to perform;

\- R is the range of variation (or set of values) of P,

![](/api/attachments/ZDKWY952/fulltext/images/aa590272f2f819519ce277612348b3315f63081217999f3db839d1815a69fb81.jpg)  
Fig. 4. Results of the management policies: (a) Policy A (fixed number of licenses) (b) Policy B (number of licenses proportional to the adult population).

\- S is an (optional) score to be evaluated as a function of time, model parameters, and any set of model variables v (i.e., input-, state- or output variables for the total time interval), usually serving as an objective function for goal-oriented experimentation,

\- C is an (optional) set of constraints on state and output values;

\- O is an (optional) method to compute new values of P on the basis of preceding results of S.

Evidently this definition of multiple experiments comprises several different operations that are normally performed with models, such as parameter estimation and sensitivity analyses. k defines whether the experiment is simple or goal-oriented, in which case the method O, the score S and, optionally, the set of constraints C have to be set.

As for the simulation methods, also the optimization method must be chosen by the user. Such a choice may be guided by some rules which suggest a suitable procedure based on the number of variables to optimize, structural properties of the problem (linear, quadratic, etc.), and the maximum number of elementary experiments the user has decided to spend.

The information relative to each experiment may be stored and retrieved using an experiment base defined by a lattice of classes quite similar to that previously described for models.

In the population management study, two multiple experiments for optimizing the parameter P characterizing the policies A and B (see their mathematical definition above) must be planned. This allows the user to determine the best policy within each class. As in many natural resources management problems, the objective function for such an optimization was assumed to be the total discounted benefit from hunting over a long period (50 years) i.e.,

$$
\sum_ {t = 1} ^ {5 0} \left((1 + r) ^ {- t} (q \cdot \text { HuntingEffort } (t) \cdot \text { Adults } (t)\right)
$$

$$
- \mathrm{s} \cdot \text { HuntingEffort(t) }
$$

where r, q, and s represent respectively the discount rate, the catchability coefficient and the cost per unit effort and are supposed to be known and constant in time.

A bisection method was chosen from the optimization method bank and the discrete time simulator (the model is defined on a yearly basis) from the simulation method bank. The two multiple experiments were performed with the same initial conditions and no external addition of animals and/or food. Sample results of these two experiments are shown in Fig. 4. It appears that the overall system (grass and animals) tends to an equilibrium around which it oscillates due to the random variations of grass availability.

## 4. Comparing experiments (Choice)

The final phase of analyzing and comparing experiment results in order to perform a choice must be supported by a temporary and flexible output structure that the user can easily manipulate in order to enhance his understanding of the various aspects of the case at hand. Experience demonstrates that, when a decision problem is complex and has many relevant variables (as it is usually the case when it is poorly structure) it is almost impossible to plan in advance which kind of output would be convenient and effective in order to understand it and find a viable decision. It is thus unlikely that a user could be able to decide interactive changes of parameters by looking at one or few variables at run time. Therefore, despite this may appear as a limitation with respect to many other simulation packages, we have restricted the capability of the output analyzer to post processing. In any case, it is immediate to modify an experiment already performed to introduce, for instance, a parameter variation at a certain time or a smaller time step for better precision.

The analysis of results is even more difficult if one has to compare several models representing different views or formalizations of the original problem, different parameter values or different information structures (e.g., open loop vs. feedback control). The choice phase of the decision process is clearly the most critical and the one where subjective judgment of the user plays the most relevant part. Though in fact even during the preceding phases the user has an essential role in defining a structure for the original problem (i.e., he must select a model and define experiments), in this final phase his subjective judgment becomes more explicit. The software module that supports this phase is called the working sheet and can provide several features for the interpretation of the final results.

<table><tr><td colspan="5">0 to 50 years of experiment A of Pop-Control</td></tr><tr><td>t [years]</td><td>HuntingEff [numbers]</td><td>Young [kg]</td><td>Adults [kg]</td><td>Grass [kg]</td></tr><tr><td>0</td><td>.149</td><td>1.616</td><td>2.978</td><td>24.728</td></tr><tr><td>1</td><td>.149</td><td>1.517</td><td>2.805</td><td>26.949</td></tr><tr><td>2</td><td>.149</td><td>1.327</td><td>2.589</td><td>24.470</td></tr><tr><td>3</td><td>.149</td><td>1.140</td><td>2.411</td><td>18.935</td></tr><tr><td>4</td><td>.149</td><td>.936</td><td>2.189</td><td>21.454</td></tr><tr><td>5</td><td>.149</td><td>.907</td><td>1.965</td><td>27.660</td></tr><tr><td>6</td><td>.149</td><td>.912</td><td>1.805</td><td>30.800</td></tr><tr><td>7</td><td>.149</td><td>.876</td><td>1.693</td><td>27.573</td></tr><tr><td>8</td><td>.149</td><td>.785</td><td>1.587</td><td>28.236</td></tr><tr><td>9</td><td>.149</td><td>.743</td><td>1.477</td><td>42.491</td></tr><tr><td>10</td><td>.149</td><td>.803</td><td>1.401</td><td>59.049</td></tr><tr><td>11</td><td>.149</td><td>.837</td><td>1.378</td><td>65.747</td></tr><tr><td>12</td><td>.149</td><td>.846</td><td>1.377</td><td>67.029</td></tr><tr><td>13</td><td>.149</td><td>.848</td><td>1.379</td><td>65.061</td></tr><tr><td>14</td><td>.149</td><td>.844</td><td>1.381</td><td>66.303</td></tr><tr><td>15</td><td>.149</td><td>.849</td><td>1.381</td><td>66.313</td></tr><tr><td>16</td><td>.149</td><td>.849</td><td>1.383</td><td>61.013</td></tr><tr><td>17</td><td>.149</td><td>.833</td><td>1.381</td><td>75.035</td></tr><tr><td>18</td><td>.149</td><td>.872</td><td>1.388</td><td>71.380</td></tr><tr><td>19</td><td>.149</td><td>.884</td><td>1.396</td><td>73.815</td></tr><tr><td>20</td><td>.149</td><td>.879</td><td>1.405</td><td>68.892</td></tr><tr><td>21</td><td>.149</td><td>.871</td><td>1.414</td><td>72.690</td></tr><tr><td>22</td><td>.149</td><td>.887</td><td>1.420</td><td>68.223</td></tr><tr><td>23</td><td>.149</td><td>.879</td><td>1.428</td><td>67.133</td></tr><tr><td>24</td><td>.149</td><td>.880</td><td>1.431</td><td>63.273</td></tr><tr><td>25</td><td>.149</td><td>.870</td><td>1.432</td><td>70.780</td></tr><tr><td>26</td><td>.149</td><td>.893</td><td>1.433</td><td>65.931</td></tr><tr><td>27</td><td>.149</td><td>.880</td><td>1.439</td><td>77.262</td></tr><tr><td>28</td><td>.149</td><td>.915</td><td>1.446</td><td>77.674</td></tr><tr><td>29</td><td>.149</td><td>.920</td><td>1.464</td><td>79.592</td></tr><tr><td>30</td><td>.149</td><td>.936</td><td>1.481</td><td>86.118</td></tr><tr><td>31</td><td>.149</td><td>.961</td><td>1.503</td><td>76.717</td></tr><tr><td>32</td><td>.149</td><td>.954</td><td>1.525</td><td>67.891</td></tr><tr><td>33</td><td>.149</td><td>.942</td><td>1.534</td><td>68.553</td></tr><tr><td>34</td><td>.149</td><td>.950</td><td>1.537</td><td>62.211</td></tr><tr><td>35</td><td>.149</td><td>.931</td><td>1.538</td><td>56.382</td></tr><tr><td>36</td><td>.149</td><td>.908</td><td>1.528</td><td>57.961</td></tr><tr><td>37</td><td>.149</td><td>.909</td><td>1.513</td><td>67.941</td></tr><tr><td>38</td><td>.149</td><td>.935</td><td>1.509</td><td>76.728</td></tr><tr><td>39</td><td>.149</td><td>.958</td><td>1.521</td><td>79.675</td></tr><tr><td>40</td><td>.149</td><td>.972</td><td>1.539</td><td>79.596</td></tr><tr><td>41</td><td>.149</td><td>.984</td><td>1.559</td><td>84.508</td></tr><tr><td>42</td><td>.149</td><td>1.008</td><td>1.581</td><td>71.659</td></tr><tr><td>43</td><td>.149</td><td>.989</td><td>1.599</td><td>65.957</td></tr><tr><td>44</td><td>.149</td><td>.982</td><td>1.603</td><td>65.900</td></tr><tr><td>45</td><td>.149</td><td>.984</td><td>1.604</td><td>66.022</td></tr></table>

The working sheet can display or plot all the model variables one at a time or in any group, within windows of variable size, shape and position. It allows the generation of new model variables as combinations of computed ones without repeating the experiment. Using a simple algebraic notation, the user is able to define, for instance, the difference between two model variables or to multiply a variable by a constant. It is classical that the user starts to ask for new variable combinations after having seen the first simple results, as understanding is a continuous process.

As an additional support to this phase, the system offers the possibility of computing also scalar variables as functions of the time series generated in the experiment. These scalar variables may represent statistics (mean, maximum, minimum, variance, etc.) or any other performance index that appears significant to the user (Fig. 5).

A peculiar feature of the working sheet is the possibility of working on several experiments simultaneously in order to compare their results. This means that the user can select a certain number of indices and collect them in a table showing the performances of each experiment under those points of view. The resulting matrix is the basis for the choice phase. It is processed, in general, by standardizing its values, setting weights (or sometimes utilities) to each index, and then selecting the alternative which has the highest weighted sum of indices. The choice of the proper weights is a topic largely discussed by the literature on multi-criteria choice $[11,20,26]$ and implies the explicit quantification of the user's preferences. Programs implementing a series of suggestions for weight selection are already available $[8,19]$ and thus this point has been left to the user, who can implement various approaches through the facilities offered by the working sheet.

![](/api/attachments/ZDKWY952/fulltext/images/bfa65f0c758d4859d1dd09e8aa7839206c27787df0ff5a2ff63186e3e5a9b90e.jpg)  
Fig. 5. Postprocessing the results of a simulation run.

![](/api/attachments/ZDKWY952/fulltext/images/74de88f67cb225865d24c556964b82b3cebe948aac1b810f133ffad1601a5262.jpg)  
Fig. 6. Numerical comparison between the two policies A and B.

Using the working sheet for the population control problem, one can compare the performances of the two alternatives by analyzing graphically (see again Fig. 4) and numerically (Fig. 6) their results. With policy A the hunting effort is clearly constant, while with policy B it follows the variation in the population density. Policy B has a higher value of the discounted benefit, but also allows a higher mean value of available animals (see the aggregate “Mean-Animals” measured in unit biomass per unit area and computed thanks to the post processing capability of the system) and, obviously, a slightly less mean availability of grass. Policy B thus seems, under these aspects, to be superior to policy A. Clearly, this may not be true any more if the implementation costs of the two policies are take into account and, in any case, the final choice will always require a political judgment which cannot be attempted by an automatic system.

## 5. System architecture

The sequence of steps in the decision process and their necessary support outlined above suggest that the software environment can be implemented using the architecture sketched in Fig. 7. For instance, in our current attempt to integrate and re-implement previous prototypes on a uniform platform (Microsoft Windows), Borland C++ [4] is used as an implementation language and GUPTA as an SQL-based database layer [23] (this could certainly be improved in the future using a PC-based object-oriented database management system, however, encapsulating the database access by a set of interface classes rendered our design independent of the concrete data storage employed).

Three basic types of objects can be distinguished in the software environment: models, experiments and time series. They are stored in the respective bases, which allow the instantiation, storage, retrieval and editing operations. The user creates a simulation model by instantiating a predefined subclass in the model base. The definition of an experiment requires the specification of all input data, initial and parameter values, and of a simulation and (optionally) an optimization method. The input data in turn are maintained in the data base where the unique possible structure is a time-series. Algorithms (simulation and optimization methods) are stored in two separate banks. Simulation are compared and post-processed on the working sheet.

These modules can be differentiated with respect to their accessibility by the user and to the level of knowledge they represent:

![](/api/attachments/ZDKWY952/fulltext/images/b0749e58f4ebe064ff04f2f723fb04ce6368547ba1cb613195b5cbfa7e67995f.jpg)  
Fig. 7. General architecture of the software environment.

\- The two method banks provide the deep level of knowledge concerning simulation and optimization procedures. They are maintained by a system administrator and are accessible to the user in a read-only mode.

\- The three bases contain structural information on classes and distinct instances of the respective objects. Here, the user maintains information and knowledge of some importance, which is typical of the type of problems he is dealing with. The bases are thus maintained by both the administrator and the user.

\- The working sheet is a typical problem-oriented structure containing information only about the current working session and thus embeds the most short-term knowledge. It is completely under user control.

Communication between the user and the different software modules is based on forms, menus and the mouse. This user interface provides also the overall system control.

The modules mentioned above have been designed following the object-oriented paradigm and contain both the data structures and the respective operations. In such a way a distributed software control mechanism is obtained and changes in one module do not call for changes in others, thus implementing the principle of information hiding.

The model base has been implemented to support the intelligence phase in decision making according to the specifications in Section 2. The choice of maintaining only structured input/output models limits the applicability of this software environment and is closely related to the type of problems (mainly related to environmental management), which have generated this research. In some engineering problems in fact, it is unclear at the beginning of the analysis, which entity must be considered a “cause” (i.e., input) and which must be considered an “effect” (output). In environmental management, however, the distinction between the human actions to investigate and the response of the environment is usually clear. Equations can thus be written in the normal (declarative) form, where the dependent variables (or their derivative) are assigned a value computed on the basis of input variables.

The simulation method bank serves as a pool of available simulation procedures for discrete and continuous models. These procedures are encapsulated by C++ classes (an idiom that might be called a procedural object), with an abstract superclass defining the general protocol. For any concrete subclass, a specific simulation procedure redefines the abstract (pure virtual) simulation method. There is a default method (i.e., a default instance of the procedural object) for each model type, which can be selected when a new model class is defined by the user. While these default methods should be appropriate for many applications, the user may change them depending on the specific experimental conditions. Moreover, due to the dynamic binding mechanism of C++ that comes with virtual functions, the method bank can be extended without affecting stored models or model classes.

Message passing as a communication technique is particularly important to simplify the maintenance and the enlargement of the simulation method bank, because it hides all the details related to the model to the equation solution procedure. For instance, simulation methods initially issue requests for obtaining the set of input variables or, during the actual simulation process, for the value of a certain input variable at a certain time step. The experiment answers these requests by accessing different sources. For instance, input variables may be linked to a time series stored in the data base or to an output variable of another submodel of the current model; in both cases, a conversion method might need to be called to answer the simulator's request correctly.

The data base contains the set of persistent time-series. These usually represent data measured on some real system or significant results of some experiments, which the user wants to store for a certain period. This contrasts the short-lived data in the working sheet, which will be lost after a session. Together with these data, the base contains also the data access functions. Thus, the user or the rest of the system does not directly work on the data. They send messages to appropriate data access methods, which return specific values or set of values. If any conversion is necessary, for example in the case where some interpolation is needed because the data at a specific time point are not explicitly stored, this is performed automatically by the corresponding access method.

Every simulation run of a model is performed via an experiment. In general the data, model and experiments are independent from each other and can be accessed separately. In the case of a simulation, the model is activated from the experiment base and the experiment collects all the data necessary for a simulation run (a similar concept can be found in SIMAN [21] where also parameter distributions can be specified). The instantiated experiment frame becomes the center of the entire system and controls all the flows of information between the other components. The schedule k determines how the simulation has to be performed (N number of times or until the goal S is optimized) and recalculates the parameter set P with respect to the previous result for S computed on the basis of the model variables V as shown in Fig. 8. Note that the assumption that the decision variables are represented simply by the set of model parameters P is not a limitation since both, the initial conditions $X_{o}$ and the input values U may be expressed in terms of some model parameters.

manner as simulation methods. An abstract base class encapsulates an abstract routine with a message passing interface to the experiment to be conducted. This is specialized by a set of concrete subclasses (maintained by the system administrator), each responsible for the implementation of a certain optimization method (cf. [17]): Null (no optimization at all), bisection, gradient, Powell's search, simulated annealing, tabu search. When the user specifies an objective function to be optimized, he is also forced to select one of the optimization methods provided. Again, new procedures can easily be integrated by defining a new subclass and overriding the abstract optimization method; however, this task should only be performed by a system administrator.

The working sheet, supporting the final choice phase, represents an object-oriented version of a classical spreadsheet containing the results of different experiments. According to the specifications above, it provides complete freedom in the output format definition and incremental displaying of original data and variables as well as newly defined combinations of them. The user can also store data persistently in the data base, when they are felt to be of any importance.

Optimization methods are kept in a similar

## 6. Concluding remarks

An integrated environment for both simulation and optimization was presented. It supports the user during the whole decision process, from problem formulation until the evaluation of alternative solution strategies. The software modules constituting this environment can be immediately related to the classical phases in decision making, namely, intelligence, design, and choice.

![](/api/attachments/ZDKWY952/fulltext/images/f95a94fbf8941200e33b202973a19b3e144408d6c727a595c28dedf0c809e123.jpg)  
Fig. 8. Schedule k controls the experimentation process.

We stress again that such a system is dedicated to users that are able to understand equations and thus the advantages and approximations inherent in the mapping of a real world problem into a mathematical formulation. The system offers them a complete freedom from algorithm definition and programming and enables the prototyping of even a complex model in terms of minutes.

Further research efforts may be directed toward the development of facilities to expand potential users. For instance, the analysis of some structural properties of the problem at hand may be utilized to automatically choose the most suitable simulation or optimization methods. The support to the modelling phase may be enhanced by allowing a more rough and straightforward initial description of the problem in qualitative terms. A qualitative simulation can thus be produced to check if it is worthwhile to proceed to a better quantification of such a model or its structure must be completely modified. Finally, the possibility of integrating submodels described in quantitative and in qualitative terms would reflect in a more realistic way the present knowledge about many complex systems, several parts of which can be modelled only in very simplistic terms.

## References

[1] O. Balci, R. E. Nance, E. J. Derrick, E. H. Page, and J. L. Bishop. Model generation issues in a simulation support environment. Proc. 1990 Winter Simulation Conf., 257–263, 1991.

[2] L. G. Birta. Optimization in simulation studies. In: Ören, T.I., Zeigler, B.P., and Elzas, M.S. (Eds.) Simulation and Model-Based Methodologies: An Integrative View. NATO ASI Series Vol. 10. Springer Verlag, Berlin, 1984, 185–216.

[3] R. H. Bonczek, C. W. Holsapple, and A. B. Whinston,

A.B. Foundations of Decision Support Systems. Academic Press, Orlando, 1991.

[4] Borland International Inc., Borland C++, Version 4.0, 1993.

[5] G. Caughley. Analysis of Vertebrate Populations. Wiley, London, 1977.

[6] F. E. Cellier, Q. Wang, and B. P. Zeigler. A five level hierarchy for the management of simulation models. Proc. 1990 Winter Simulation Conf., 55–64, 1991.

[7] P. Coad and E. Yourdon. Object-oriented Analysis. Yourdon Press Computing Series, Prentice Hall, Englewood Cliffs, NJ, 1990.

[8] A Colorni, E. Laniado, and F. Rosace. VISPA: Valutazione Integrata per la Scelta tra Progetti Alternativi, CLUP, Milano, 1988 (in Italian).

[9] R. De Buyser and J. A. Spriet. OPTISIM: An optimization-simulation environment for model building. Proc. of the European Simulation Multiconference, Nice (June 1988), SCS, Ghent, 16–21.

[10] C. W. Fowler and T. D. Smith. Dynamics of Large Mammals Populations, John Wiley, New York, 1981.

[11] A. Goicoechea, D. R. Hansen, and L. Duckstein. Multi-objective Decision Analysis with Engineering and Business Applications. John Wiley, New York, 1982.

[12] G. Guariso, M. Hitz, M. Schauer, and H. Werthner. MoNet: Eine Simulationsumgebung für hierarchische Input/Output-Modelle. 5th Int. Symp. on Computer Science for Environmental Protection, Vienna (September 1990), Springer-Verlag, Berlin, 521–530 (in German).

[13] G. Guariso, M. Hitz, and H. Werthner. A knowledge based simulation environment for fast prototyping. Proc. of the European Simulation Multiconference, Nice, (June 1988) SCS, Ghent, 187–192.

[14] G. Guariso, M. Hitz, and H. Werthner. An intelligent simulation model generator. Simulation 53, 2 (August 1989), 57–66.

[15] G. Guariso, M. Hitz, and H. Werthner. Experience in the development of advanced modelling environments. In: F. Pichler, R. Moreno Diaz (Eds.): Lecture Notes in Computer Science 585, Springer Verlag, 1992, 476–491.

[16] G. Guariso and H. Werthner. Environmental Decision Support Systems. E. Horwood, Chichester, 1989.

[17] M. Hitz and M. Hudec. Employing the Object Oriented Paradigm in Statistical Computing. Proc. COMPSTAT 1994, August 22–26 1994, Vienna, Physica Verlag (to appear).

[18] M. Hitz, H. Werthner, and T. I. Ören. Employing Databases for Large Scale Reuse of Simulation Models. Proc. 1993 Winter Simulation Conference (G.W. Evans, M. Mollaghasemi, E.C. Russel, W.E. Biles, eds.), Los Angeles, CA, December 12–15, 1993, 544–551.

[19] R. Janssen. A system to support discrete choice problems. Proc. AIRO '90, Operation Research Soc. of Italy, (October 1990) 691–706.

[20] R. L. Keeney and H. Raiffa. Decision with Multiple Objectives: Preferences and Value Tradeoffs. John Wiley, New York, 1976.

[21] C. D. Pegden, R. E. Shannon, and R. P. Sadowski. Introduction to Simulation Using SIMAN. McGraw-Hill, New York, 1990.

[22] B. Richmond. An Academic User's Guide to STELLA. High Performance Systems Inc., Hanover, NH, 1987.

[23] B. Ring, R. Cummings, and S. Sambar. SQLBase C Application Programming Interface-Reference Manual. Gupta Technologies, Inc., 1991.

[24] R. Ruzicka. Simul-R - A simulation language with special features for model-switching and analysis. Proc. of the European Simulation Multiconference, Nice, (June 1988). SCS, Ghent, 28-32.

[25] E. J. Rykiel (ed.). Artificial Intelligence and Expert Systems in Ecology and Natural Resources Management. Ecological Modelling 46 (Special Issue). 1/2 (July 1989), 3–133.

[26] A. Schärlig. Décider sur Plusieurs Critères. Presses Polytechniques et Universitaires Romandes, Lausanne, 1985 (in French).

[27] B. Shriver and P. Wegner (eds.). Research Directions in Object-Oriented Programming. The MIT Press, Cambridge, Mass., 1987.

[28] S. C. Shah, M. A. Floyd, and L. L. Lehman. MATRIX $_{X}$ : Control Design and Model Building CAE Capability. Computer-Aided Control Systems Engineering (M. Jamshidi and C. J. Herget, eds.), Elsevier, Amsterdam, 1985.

[29] R. H. Sprague and E. D. Carlson. Building Effective Decision Support Support. Prentice-Hall, Englewood Cliffs, New Jersey, 1982.

[30] C. R. Standridge and A. A. B. Pristker. TESS: The Extended Simulation Support System. Halstead Press, New York, 1987.

[31] O. Tanir and S. Sevinc. Defining requirements for a standard simulation environment. IEEE Computer 27, 2 (February 1994), 28–34.

[32] E. Turban. Decision Support and Expert Systems. Macmillan Publishing Co., New York, 1988.

[33] B. P. Zeigler. Theory of Modelling and Simulation. John Wiley, New York, 1976.

![](/api/attachments/ZDKWY952/fulltext/images/3b78b579072f052456538721f15176c64ec9939c3872adf5762b71e2fc3a18b1.jpg)

Giorgio Guariso is professor of Systems Analysis at the Department of Electronics and Information, Politecnico di Milano, where he graduated in Electronic Engineering in 1976. He has been working with the Italian National Research Council, the Egyptian Academy for Research and Technology and the International Institute for Applied Systems Analysis. His research activities include modelling and simulation, optimization and AI

and their applications to environmental problems. He is chairman of the IFIP working group on “Computers and Environment”.

![](/api/attachments/ZDKWY952/fulltext/images/5fca2638aa18350a069a7f313f85d3962c234ffd33fe54ffb16bb0276483de31.jpg)

Martin Hitz is Assistant Professor at the Department of Applied Computer Science, University of Vienna holding a Master's degree and Ph.D. in Computer Science from the Technical University of Vienna. His interests include information systems design, object oriented software engineering, and reusability.

![](/api/attachments/ZDKWY952/fulltext/images/77d5190f0fb07dc8f03167c4d3a11c3f2289e1d9275ee52488c29710ba185152.jpg)

Hannes Werthner is Associate Professor at the Department of Statistics, Operations Research and Computer Science, University of Vienna. He received a Master's degree and Ph.D. in Computer Science both from the Technical University of Vienna. His main research interests include simulation environments, OO design, information systems and multimedia.
