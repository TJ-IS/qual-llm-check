---
otero_id: 4368
otero_key: "X45PFA9K"
title: "Wastewater treatment: New insight provided by interactive multiobjective optimization"
authors: "Jussi Hakanen; Kaisa Miettinen; Kristian Sahlstedt"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.026"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Wastewater treatment: New insight provided by interactive multiobjective optimization

Jussi Hakanen ⁎, Kaisa Miettinen <sup>1</sup>, Kristian Sahlstedt <sup>2</sup>

Dept. of Mathematical Information Technology, P.O. Box 35 (Agora), FI-40014 University of Jyväskylä, Finland Pöyry Environment Ltd, P.O. Box 50, FI-01621 Vantaa, Finland

## a r t i c l e i n f o

Available online 25 November 2010

Keywords: Wastewater treatment planning Interactive methods Multicriteria optimization Decision support IND-NIMBUS Simulation-based optimization

## a b s t r a c t

In this paper, we describe a new interactive tool developed for wastewater treatment plant design. The tool is aimed at supporting the designer in designing new wastewater treatment plants as well as optimizing the performance of already available plants. The idea is to utilize interactive multiobjective optimization which enables the designer to consider the design with respect to several con<sup>fl</sup>icting evaluation criteria simultaneously. This is more important than ever because the requirements for wastewater treatment plants are getting tighter and tighter from both environmental and economical reasons. By combining a process simulator to simulate wastewater treatment and an interactive multiobjective optimization software to aid the designer during the design process, we obtain a practically useful tool for decision support. The applicability of our tool is illustrated with a case study related to municipal wastewater treatment where three con<sup>fl</sup>icting evaluation criteria are considered.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Operational requirements of wastewater treatment plants (WWTPs), notably the ef<sup>fl</sup>uent limits of nitrogen and phosphorus, are getting tighter and tighter because of increased emphasis on environmental values. Consequently, more complex wastewater treatment processes are gaining ground. At the same time, the needs for economical ef<sup>fi</sup>ciency (for example, minimizing plant footprint and the consumption of chemicals and energy) as well as for operational reliability are also emphasized. This makes the design of a WWTP a complex process involving trade-offs between a number of con<sup>fl</sup>icting economical and operational criteria. Therefore, a simpli<sup>fi</sup>ed approach where all the aspects are gathered together, usually as estimated total costs, and optimized is not adequate anymore. Instead, there is a need for decision support tools that can take simultaneously into account these different criteria and help the designer in analyzing their interdependencies. This kind of an approach enables getting a much more realistic idea on how the WWTP plant should be designed while balancing between con<sup>fl</sup>icting criteria.

Handling with problems involving multiple con<sup>fl</sup>icting criteria (or objectives) is called multiobjective optimization and many methods have been developed for such problems (see, e.g., [3,4,16,18,29]). Assuming the problem has been correctly speci<sup>fi</sup>ed, the methods usually concentrate on Pareto optimal solutions, also known as compromise solutions, where none of the objective values can be improved without impairing at least one of the others. Solving multiobjective optimization problems can be understood as <sup>fi</sup>nding the Pareto optimal solution that best satis<sup>fi</sup>es the needs of a decision maker (DM). This person can be, e.g., a designer when we are talking about practical applications like WWTP design. Thus, the <sup>fi</sup>nal solution of a multiobjective optimization method is often referred to as the most preferred solution.

The class of interactive multiobjective optimization methods (see, e.g., [18,25] and references therein) is a widely used one consisting of different approaches that iteratively proceed towards the most preferred solution and the DM can learn about the interdependencies among the objectives during the solution process and adjust one's preferences accordingly. An alternative approach is to compute a representative set of Pareto optimal solutions (note that there can be in<sup>fi</sup>nitely many Pareto optimal solutions) and let the DM choose the most preferred solution afterwards. A bene<sup>fi</sup>t of using interactive methods for decision support is that they generate Pareto optimal solutions based on the DM's preferences and when the DM changes one's preferences, a new or some new Pareto optimal solutions are obtained and the DM does not need to consider uninteresting solutions.

To guarantee a <sup>fi</sup>nal design which takes into account all the relevant criteria related to wastewater treatment, we propose an interactive design strategy that utilizes numerical simulation of wastewater treatment processes combined with an ef<sup>fi</sup>cient interactive multiobjective optimization method, NIMBUS [24]. Complex characteristics of wastewater treatment processes can be quanti<sup>fi</sup>ed by using numerical simulation techniques. The resulting WWTP design problem is thus simulation-based which means that the values of the objective and constraint functions consist of outputs of a process simulator. The approach combining numerical simulation with interactive multiobjective optimization enables the designer to simultaneously consider the process from different perspectives and optimally balance the <sup>fi</sup>nal design between different con<sup>fl</sup>icting design criteria.

The WWTP design problem has been previously considered by optimizing only one objective function, that in one way or another describes the costs of the process to be minimized (see, for example, [5,13,15,28]). So far, very little attention has been given to approaches utilizing multiobjective optimization. Actually, we have found only two papers in this <sup>fi</sup>eld that deal with multiple objectives. In [2], the idea is to produce a representative set of Pareto optimal solutions to the multiobjective optimization problem considering WWTP design. Let us also point out that the approach in [2] is not of simulation-based optimization as is the case in our study but considers the problem in a more general level without using numerical simulation. In [6], multiple objective functions are considered in conceptual design of activated sludge systems. A multiobjective methodology is used to evaluate and compare a small number of alternatives resulting from conceptual design. However, none of these approaches consider interactive methods that enable the designer to actively participate in the design process.

In this paper, we concentrate on utilizing modern optimization techniques to provide a decision support tool for the designer which helps him/her to locate the best trade-offs between different competing design alternatives in WWTP design. By utilizing interactive multiobjective optimization in the design process, the designer is able to learn about the problem and about the interdependences between the con<sup>fl</sup>icting design criteria. As mentioned, (s)he can concentrate only on those solutions that are of interest to him/her. When compared to the approach in [2], our interactive approach is more computationally ef<sup>fi</sup>cient, that is, the required number of Pareto optimal solutions computed is smaller because we do not try to approximate all the Pareto optimal solutions of which many can be uninteresting to the designer.

Our interactive design tool proposed consists of combining numerical simulation of wastewater treatment processes by the GPS-X process simulator with the interactive multiobjective optimization capabilities of the IND-NIMBUS optimization tool [21]. As already discussed, this kind of an interactive design tool is an entirely novel approach in WWTP design (the <sup>fi</sup>rst ideas of the tool were presented in [10]), although such tools are successfully utilized in other application <sup>fi</sup>elds. The possibilities of this interactive design tool are here illustrated by reporting results from a case study which deals with the optimization of a WWTP operation in terms of energy and chemical consumption, operational safety and ef<sup>fl</sup>uent quality.

The rest of this paper is organized as follows. First, in Section 2, we brie<sup>fl</sup>y introduce wastewater treatment and describe the case study problem we are considering. Section 3 is devoted to introducing the interactive multiobjective optimization method we are using, namely NIMBUS and its implementation IND-NIMBUS. In addition, we describe the structure of the proposed interactive design tool and show how to use its graphical user-interface. In Section 4, we report the results of applying the new design tool to the case study described in Section 2 along with some discussion of the results obtained. Finally, we make some concluding remarks about the study and summarize topics for future research in Section 5.

## 2. On modelling wastewater treatment

## 2.1. Background

Mathematical modelling of WWTPs began gaining ground in the 1990s when experience on modelling techniques and computing power increased simultaneously. In the literature, the overwhelming majority of modelling considers the activated sludge process (ASP), globally the most common method of wastewater treatment. In this process, biomass (which is called activated sludge) suspended in the wastewater to be treated is cultivated and maintained in an aerated bioreactor. The wastewater is puri<sup>fi</sup>ed, i.e. organic carbon, nitrogen and phosphorus are removed, during its retention in the bioreactor. The bioreactor is followed by a clari<sup>fi</sup>er basin, in which the biomass is separated by gravitational settling and returned to the bioreactor, and the treated wastewater is directed as over<sup>fl</sup>ow to further treatment or to discharge. Excess activated sludge is removed from the process and treated separately. A schematical <sup>fl</sup>ow sheet of the process is presented in Fig. 1.

The activated sludge model (ASM) family developed by the Task Group of International Water Association has been established as a standard for ASP modelling [12]. These are mechanistic models, in which the various phenomena occurring in the bioculture are described by <sup>fi</sup>rst to third order differential equations. The reaction rates of different substances, e.g., fractions of organic carbon and nitrogen, are obtained by integrating the differential equations over time and factoring them with substance-speci<sup>fi</sup>c stoichiometric coef<sup>fi</sup>cients. These coef<sup>fi</sup>cients are based on continuity of key parameters (including total chemical oxygen demand, total nitrogen, total phosphorus and charge), which ensures model integrity. The models are nonlinear, re<sup>fl</sup>ecting the nonlinear nature of microbial growth and solids separation.

## 2.2. Optimization in WWTP design

As new treatment requirements prompt the use of more complex processes, the number of independent (and dependent) variables in the design task increases, and selection of their optimal values becomes more dif<sup>fi</sup>cult without appropriate support. Considering different objectives (treatment results, investment costs and operational costs) and different environmental conditions in which the plant has to operate (wastewater quality, <sup>fl</sup>ow and temperature <sup>fl</sup>uctuations) signi<sup>fi</sup>cantly increases the complexity of the problem. The optimal design and operation of a wastewater treatment plant involves, e.g., selecting appropriate volumes and functions for process units and determining optimal setpoints for dissolved oxygen concentrations, sludge circulation <sup>fl</sup>ows and chemical dosing rates such that they optimize the behaviour of the plant, according to some pre-de<sup>fi</sup>ned criteria, in given conditions [1]. Mathematical models are a powerful tool for this kind of optimization problems.

Optimization of WWTP design and operation by modelling and simulation has been applied since the 1990s. The studies usually involve comparisons of different process schemes or control strategies. The behaviour of the considered solutions is simulated, and the results are then compared to each other, usually in terms of investment or operational costs. The comparison can be done either by engineering judgement, as is usually the case (see e.g. [7,17]) or using a single objective optimization algorithm (see e.g. [5,28]). However, formulating the problem so that all relevant criteria are combined as a single criterion and using only this objective function instead of individual objective functions for each criterion hides the interdependencies between different criteria and, thus, makes it dif<sup>fi</sup>cult for the DM, who might be, e.g., a designer or a plant operator, to assess the true optimality of the solution. The DM may also have non-quanti<sup>fi</sup>able priorities, such as operational stability and ease of operation, which may depend on many decision variables to be optimized. For example, minimizing the concentration of activated sludge to avoid settler overload may be more important than minimizing certain residual pollutant concentrations in the ef<sup>fl</sup>uent. Therefore, for a truly optimal design, the procedure must present the DM with solutions based on a multiobjective optimization approach, out of which (s)he can choose the best ones to be elaborated further.

Because dealing with a pre-speci<sup>fi</sup>ed single function to be optimized is not appropriate in the presence of con<sup>fl</sup>icting criteria, one may ask, how should the optimization problem with multiple con<sup>fl</sup>icting objective functions be solved? In the next section, we describe some suitable approaches for solving such problems, utilizing concepts and methods of multiobjective optimization. We also describe the new interactive design tool proposed for WWTP design and operation and demonstrate its usage with a case study related to municipal wastewater treatment. Let us next brie<sup>fl</sup>y describe the case study problem considered before we continue with multiobjective optimization.

![](/api/attachments/X45PFA9K/fulltext/images/78ad4094b79a06596f91c7e25ca7ed16e50980c9a8a87501930614adc35d4df2.jpg)  
Fig. 1. A <sup>fl</sup>ow sheet of the activated sludge process.

## 2.3. Description of wastewater treatment process considered

The process considered in the case study of this paper is based on ASP and performs nitri<sup>fi</sup>cation, i.e., oxidation of ammonium nitrogen to nitrate nitrogen by autotrophic, slow-growing micro-organisms. The biochemical reactions involved consume a lot of oxygen and alkalinity. Oxygen is supplied by aeration compressors and alkalinity partly by in<sup>fl</sup>uent wastewater, partly by adding chemicals, e.g. $\mathrm { N a } _ { 2 } C O _ { 3 } .$ Aeration consumes energy and chemicals cost money, so minimizing the need for aeration and alkalinity addition is important for the operational economy of the plant. Another important control parameter is biomass concentration $\left( C _ { M L S S } \right)$ in the bioreactor, which should be kept as low as possible so that the secondary settler would not be overloaded in case of peak <sup>fl</sup>ows. The amount of $C _ { M L S S }$ is controlled by the removal rate of excess sludge, which is inversely proportional to the theoretical retention time of one biomass cell in the process, i.e. sludge retention time (SRT). The nitrifying biomass requires a relatively long SRT because of its low growth rate. The higher the SRT, the higher the concentration of biomass and thus the bigger the risk of clari<sup>fi</sup>er overload.

The process model used here describes a nitrifying activated sludge process. The biological process is a plug-<sup>fl</sup>ow reactor with <sup>fi</sup>ve sections. All sections are equipped with bottom <sup>fi</sup>ne bubble aerators. The biochemical reactions are modelled with ASM3 [12]. Sodium carbonate is dosed as a 5% solution to compensate for alkalinity consumed by nitri<sup>fi</sup>cation. The wastewater treated by the process corresponds to typical Finnish mechanically and chemically pretreated municipal wastewater. The secondary clari<sup>fi</sup>er is modelled as a 10-layer one-dimensional settler. Solids separation is modelled with the Takacs double-exponential model [30]; no biological reactions are assumed to take place in the clari<sup>fi</sup>er. Default values are used for all kinetic and stoichiometric model parameters of ASM3 and the Takacs model. The oxygen concentration in the biological process is PIcontrolled, with a default setpoint of $2 . 0 \ : g / m ^ { 3 }$ in all sections. Mixed liquor suspended solids concentration $\left( C _ { M L S S } \right)$ is PI-controlled by regulating the excess sludge <sup>fl</sup>owrate. The default setpoint for $C _ { M L S S } \mathrm { i } s 3 . 0 k g / m ^ { 3 }$ . Excess sludge is removed from the aeration basin. In addition, the wastewater temperature, in<sup>fl</sup>uent <sup>fl</sup>owrate and the maximum volume of the reactor were <sup>fi</sup>xed to $1 2 ^ { o } C ,$ 60 000 $m ^ { 3 } / d$ and $1 7 0 0 0 m ^ { 3 }$ , respectively.

## 3. Decision support tool for WWTP design

Practical real-world optimization problems, like the ones in wastewater treatment, often have to be considered from many different perspectives. This gives rise to several con<sup>fl</sup>icting evaluation criteria as described in Section 2. In this section, we <sup>fi</sup>rst brie<sup>fl</sup>y discuss multiobjective optimization and, then, we introduce the interactive NIMBUS method along with its implementation IND-NIMBUS. Finally, we present the interactive design tool for WWTP design we have developed and describe how it could be used in solving WWTP design problems.

## 3.1. Multiobjective optimization

When the optimization problem in question needs to be solved with respect to several con<sup>fl</sup>icting criteria simultaneously, the concept of optimality needs to be rede<sup>fi</sup>ned. The solution in single objective optimization can be regarded as optimal when the objective function achieves the smallest or largest value (for minimization or maximization problems, respectively). Instead, when dealing with multiple con<sup>fl</sup>icting objective functions, the solution can be seen as optimal when no objective function value can be improved without impairing some other objective. These optimal solutions are called Pareto optimal solutions [18]. Typical to these optimal solutions is that there usually are (in<sup>fi</sup>nitely) many of them and they all are mathematically equivalent.

The multiobjective optimization problem can be formulated as

$$
\begin{array}{l l} \text { minimize } & \{f _ {1} (x),..., f _ {k} (x) \} \\ \text { subject   to } & x \in S, \end{array}\tag{1}
$$

where the real-valued objective functions $f _ { 1 } , . . . , f _ { k }$ are to be simultaneously optimized with respect to the feasible region $S { \subset } R ^ { n } .$ . In this paper, we consider only minimization problems because if some objective function $f _ { i }$ is to be maximized, it is equivalent to minimize $- f _ { i }$ The feasible region identi<sup>fi</sup>es the acceptable values for the decision variable vectors $\boldsymbol { x } = ( x _ { 1 } , . . . , x _ { n } ) ^ { T }$ and, in this paper, it is characterized by inequality constraint functions $g _ { 1 } , . . . , g _ { m }$ as well as lower and upper bounds (x<sup>l</sup> and $x _ { i } ^ { u } ,$ respectively) for each decision variable $x _ { i } , i = 1 , . . . , n .$ . Therefore, the feasible region can be de<sup>fi</sup>ned by

$$
S = \{x \in R ^ {n} | g _ {j} (x) \leq 0, j = 1,..., m, \text { and } x _ {i} ^ {l} \leq x _ {i} \leq x _ {i} ^ {u}, i = 1,..., n \}.\tag{2}
$$

In WWTP design problems, the decision variables are typically some operational parameters that affect the behaviour of the process with respect to the objectives chosen. The constraints speci<sup>fi</sup>ed restrict the feasible values of the decision variables as well as the performance of the process to satisfy, e.g., environmental regulations. In our case, the objective and the constraint function values are determined based on outputs of a process simulator used to simulate wastewater treatment when a given decision variable vector is used as an input for the simulator.

Solving problem (1) requires using the methods of multiobjective optimization (see, for example, [18] and references therein as well as [27] for such problems in chemical engineering) in order to <sup>fi</sup>nd the most preferred solution. Usually, the aim of solving practical multiobjective optimization problems is to <sup>fi</sup>nd the best compromise between the con<sup>fl</sup>icting objective functions that is to be further tested before it is being implemented in practice. To select the most preferred Pareto optimal solution, we must have some additional information and, in multiobjective optimization, the person who has that information is called a decision maker. The DM needs to be able to compare Pareto optimal solutions with the help of one's experience in the <sup>fi</sup>eld of the application area considered. The task of the DM is, also, to express preferences on what kind of solutions are desirable. In this way, the DM can direct the solution process and balance between con<sup>fl</sup>icting objectives.

Methods of multiobjective optimization can be categorized, for example, by the role of the DM [16,18]. The DM can express preferences before or after the method produces Pareto optimal solution(s) or the solution process can be iterative, that is, the steps of expressing preferences and generating Pareto optimal solutions can alternate until the best Pareto optimal solution has been identi<sup>fi</sup>ed. In this paper, we concentrate on the last type, that is, interactive multiobjective optimization methods [18,25]. Interactive methods are chosen because they are computationally ef<sup>fi</sup>cient (i.e., they generate only those Pareto optimal solutions that are of interest to the DM as mentioned before) and they enable the DM to learn about the interrelationships between con<sup>fl</sup>icting objective functions. These are important properties when dealing with practical multiobjective optimization problems.

## 3.2. NIMBUS and IND-NIMBUS

The interactive multiobjective optimization method used in this paper is the NIMBUS method [18,22–24], to be more speci<sup>fi</sup>c its latest, so-called synchronous version [24] and, especially, its implementation IND-NIMBUS [21] developed for solving industrial multiobjective optimization problems (http://www.ind-nimbus.it.jyu.<sup>fi</sup>). NIMBUS and IND-NIMBUS were chosen because they have been successfully applied in other areas, for example, in chemical process design [8,9], paper machine headbox design [14] and designing of ultrasonic transducers [11].

The NIMBUS method is based on the idea that the DM is asked at every iteration of the interactive solution process to classify the objective functions into up to <sup>fi</sup>ve classes at the current Pareto optimal solution. The classes re<sup>fl</sup>ect the preferences of the DM and how (s)he would like the current Pareto optimal solution to change to become more preferred. The classes are

• the functions whose values should be improved as much as possible,

• the functions whose values should be improved until a given aspiration level,

• the functions whose values are satisfactory at the moment,

• the functions whose values are allowed to impair up to a given bound and

• the functions whose values can change freely.

If the DM wants to change consideration from the current Pareto optimal solution to another Pareto optimal solution, (s)he needs to classify at least one objective function into the <sup>fi</sup>rst two classes and at least one objective function into the last two classes. This is due to the de<sup>fi</sup>nition of Pareto optimality (improvement cannot be obtained without trading off). Based on the classi<sup>fi</sup>cation information given by the DM, a new optimization problem is formed and solved. The resulting solution will be a Pareto optimal solution (see [18,24] for the proof) that satis<sup>fi</sup>es the preferences of the DM as well as possible. In the synchronous NIMBUS method [24], several optimization problems can be formed resulting in different Pareto optimal solutions (corresponding to the preference information speci<sup>fi</sup>ed). The DM may decide how many new solutions (s)he wants to see after each classi<sup>fi</sup>cation (between one and four) and it is then up to him/her to choose the one that best follows his/her preferences. The method has also a possibility to generate a desired number of intermediate Pareto optimal solutions between any two Pareto optimal solutions already computed to observe intermediate behaviour. More information about the NIMBUS method can be found in [24].

To apply the NIMBUS method in practice, an implementation called IND-NIMBUS [21] was developed. As already mentioned, IND-NIMBUS is devoted especially to solving industrial multiobjective optimization problems like, for example, the WWTP design. IND-NIMBUS provides the DM with a graphical user-interface (GUI) to aid in directing the interactive solution process of the NIMBUS method. In addition, IND-NIMBUS offers some single objective optimizers to be used in solving the single objective optimization problems formulated by the NIMBUS method (see [21] for details). The GUI of IND-NIMBUS consists of several tabs for different actions, for example, classi<sup>fi</sup>cation, generating intermediate solutions, visualization of the Pareto optimal solutions computed, numerical values for solutions obtained and adjusting method parameters. Next, we describe the interactive design tool for WWTP design and its features and, later, we show how it can be used in WWTP design through the GUI of IND-NIMBUS.

## 3.3. Construction of the interactive design tool

To solve WWTP design problems (discussed in Section 2) with respect to multiple objective functions, we have combined the IND-NIMBUS software with the commercial process simulator GPS-X (http://www.hydromantis.com/GPS-X.html). The GPS-X simulator is especially developed for numerical simulation of wastewater treatment processes. (Note that other appropriate process simulators could also have been used.) When connected successfully, this combination provides us a new interactive tool to support in designing new WWTPs that can consider the plant at the same time from many different aspects implying con<sup>fl</sup>icting evaluation criteria. The tool can also be used to optimize the performance of already operating plants. With the new tool, the DM obtains a more realistic overall picture of the problem and can make decisions based on versatile information including simultaneous consideration of several con<sup>fl</sup>icting criteria. In addition, with the help of this interactive tool, (s)he is able to learn about the behaviour of the problem and, if necessary, can change his/her mind and opinions as new information is gained. The learning aspect is a novel possibility when compared to previously used methods in WWTP design where usually only total costs have been minimized. Converting all evaluation criteria to money can lead to unnecessary simpli<sup>fi</sup>cations because it is not easy to estimate all costs and this may result in loss of information and understanding about the problem.

To begin with, both the simulator and the optimization tool were separate programs, so the <sup>fi</sup>rst step in developing the new design tool was to enable communication and data transfer between them. Fig. 2 shows a diagram of the communication between GPS-X and IND-NIMBUS as well as the communication between the DM and IND-NIMBUS. Communication between GPS-X and IND-NIMBUS is related to solving optimization problems producing new Pareto optimal solutions. There the inputs for GPS-X are the values of the decision variables and the outputs are the resulting objective and constraint function values. On the other hand, communication between IND-NIMBUS and the DM consists of decision making when the DM evaluates the Pareto optimal solutions computed by IND-NIMBUS and expresses preferences on producing new Pareto optimal solutions. Note that both of the communication phases are iterative and repeated as long as necessary. Whenever a new Pareto optimal solution is needed, the optimization phase is initiated.

Next, we shortly describe how the combination between IND-NIMBUS and GPS-X was realized. The basic idea behind the communication between these two programs is the following. First, the multiobjective optimization problem needs to be formulated. This includes speci<sup>fi</sup>cation of the decision variables, the objective functions and the (inequality) constraint functions limiting the feasible values of decision variables. Both objective and constraint functions are functions of the decision (or design) variables. One must also indicate whether the objective functions are to be minimized or maximized. Once the optimization problem has been formulated, the optimizer provides decision variable values to the simulator which is run with these input values. After the simulation run, the simulator returns the corresponding values of the objective and constraint functions to the optimizer (outputs of the simulator). This is repeated as often as objective and constraint function values are needed.

We decided to formulate the optimization problem in IND-NIMBUS because there is no readily available interface in the commercial GPS-X simulator for all the necessary components of the multiobjective optimization problem. First of all, the wastewater treatment process considered needs to be modelled with the GPS-X process simulator. Once we have a working process model available, we can start formulating the multiobjective WWTP design problem in IND-NIMBUS (as described above). After the IND-NIMBUS application has been started, a new problem can be added with a form through the GUI shown in Fig. 3. The form consists of four different tabs for different information about the optimization problem. There are tabs for some general information (e.g. a written problem description and the location of the GPS-X process executable used to simulate the process), entering data for objective and constraint functions as well as for decision variables.

The biggest challenge in combining two pieces of software that have been developed for different purposes is to establish required and reliable communication between them. GPS-X is a commercial simulator which made this task even more dif<sup>fi</sup>cult because there exist no interfaces to it that provide a structure suitable for multiobjective optimization as already mentioned and, naturally, we are not able to de<sup>fi</sup>ne new interfaces to it. In spite of this, the communication could be implemented by utilizing the general structure of how GPS-X works.

The basic operating principle of GPS-X is that for any simulation problem, it generates an executable program that GPS-X uses to simulate the process considered. The simulation parameters of this executable can be controlled by a command <sup>fi</sup>le and there exists also a way to extract output from the simulation. Based on this, the communication between GPS-X and IND-NIMBUS is the following. When an optimizer used to solve single objective subproblems formulated in IND-NIMBUS needs to evaluate the objective and constraint functions for some decision variable vector, an input <sup>fi</sup>le containing the variable names (as de<sup>fi</sup>ned in GPS-X) and their values is created and the executable is started by a system command. Then, before the executable performs simulation, it reads the values of the decision variables from the input <sup>fi</sup>le, runs the simulation and writes the output, that is, the values of the objective and constraint functions, into an output <sup>fi</sup>le. Finally after the simulation run has ended, IND-NIMBUS reads the values from the output <sup>fi</sup>le.

## 3.4. Using the interactive design tool through IND-NIMBUS

The interface of the design tool visible for the DM is the GUI of IND-NIMBUS and, next, we describe how it can be used. After the optimization problem has been formulated in IND-NIMBUS, as described in Section 3.3, the interactive solution process can be started. The process is started by computing the ideal values for each objective, that is, their best values when optimized individually with respect to the constraints. In other words, as many single objective optimization problems need to be solved as there are objectives. These ideal values give the best values that each objective function can obtain in the set of all Pareto optimal solutions. In addition, the worst values of the objective functions in the set of all Pareto optimal solutions can be approximated by using, for example, the payoff table [18]. The best and worst values of the objectives are used by the NIMBUS method for scaling purposes and they are also shown to the DM in order to give an idea about the attainable ranges of the objectives. The calculation of the ranges can be skipped if a reliable enough estimate of the best and worst objective function values is available.

Before the actual interactive solution process can start, the <sup>fi</sup>rst Pareto optimal solution must be computed and it is then shown to the DM. This solution is typically a neutral compromise solution (NCS) that is approximately in the middle of the ranges of the objectives in the set of Pareto optimal solutions [31]. Alternatively, a solution speci<sup>fi</sup>ed by the DM can be used as a starting point once it has been projected into the set of Pareto optimal solutions. From here on, the DM is involved in the solution procedure.

The DM can indicate how the current Pareto optimal solution should be improved. (S)he can classify the objective values in this solution with the help of the classi<sup>fi</sup>cation tab of IND-NIMBUS shown in Fig. 4. This tab consists of three parts: the current Pareto optimal solution, in which the classi<sup>fi</sup>cation is to be made, is presented on the left side of the tab, the solutions obtained during the solution process so far are shown in the upper right corner of the tab and the best candidates for the <sup>fi</sup>nal solution (selected by the DM) are presented in the lower right corner. Each objective function is represented by a colored bar. The general idea is that the shorter the colored bar, the better is the corresponding objective function value. Note, that the bars for the objective functions to be minimized start from left while the bars for the objective functions to be maximized (if there are any) start from right. The values at the left and right ends of each bar represent the ranges in the set of Pareto optimal solutions computed before the interactive solution process, as already described.

The DM can select the solution which (s)he wants to improve from the set of already obtained solutions. Then (s)he can perform the classi<sup>fi</sup>cation by clicking the bars representing the objective function values of the current solution on the left side of the tab. The numerical <sup>fi</sup>elds next to the bars can be used to give aspiration levels and bounds (the values speci<sup>fi</sup>ed by clicking with the mouse can also be edited).

![](/api/attachments/X45PFA9K/fulltext/images/4c3114e86a032801402bd991f2044e121cedb61811e5e280f4362934f5ee9b53.jpg)  
Fig. 2. A diagram of the data <sup>fl</sup>ow when using the new design tool.

![](/api/attachments/X45PFA9K/fulltext/images/cdc6a0564e3ba3122a8f2d821f0d64f7ae9f487cd89ad303e825a2365591a7ad.jpg)  
Fig. 3. A screenshot of the problem input dialog and its tab for objective functions.

Clicking different parts of the bars corresponds to the classi<sup>fi</sup>cation presented in Section 3.2. Thus, this is an implementation of the classi<sup>fi</sup>cation step in NIMBUS.

In the classi<sup>fi</sup>cation, the DM can ask for improvement in the objective functions that (s)he believes are not satisfactory. After the DM has <sup>fi</sup>nished the classi<sup>fi</sup>cation, new Pareto optimal solutions are calculated and they will appear into the set of solutions obtained. The DM can select the solutions that seem promising at the moment and place them in the set of best candidates with drag and drop. This set is used for helping the

DM to keep track of the best solutions obtained so far. The number of new Pareto optimal solutions generated as well as the optimizer used can be adjusted from the toolbar (if the DM wants to alter the default values).

Note that the classi<sup>fi</sup>cation information given by the DM is always suggestive and it is used for steering the solution process. However, there does not necessarily exist any Pareto optimal solution that could satisfy the classi<sup>fi</sup>cation exactly. Because both classi<sup>fi</sup>cation and new solutions obtained consist of objective function values (i.e., no arti<sup>fi</sup>cial information is used), it is easy for the DM to see how realistic his/her expectations were. From the new solutions generated the DM can see what kind of solutions are available and can learn about the possibilities and limitations of the problem in question.

![](/api/attachments/X45PFA9K/fulltext/images/fd606f6bdabec29e6ea93cf6e743f5620bc5d21399c1d7f36832850228c4a5ad.jpg)  
Fig. 4. A screenshot of the classi<sup>fi</sup>cation tab.

Besides classifying, the DM can direct the solution process by asking for a given number of intermediate Pareto optimal solutions to be generated. To generate intermediate solutions [24], the DM needs to select two solutions (end points), choose the number of new solutions to be produced and start the calculation. When the alternative solutions are computed, they will appear to the pool of the alternative solutions (output).

Because new Pareto optimal solutions are generated according to the DM's preferences during the solution process, it is important to be able to compare them whenever the DM so desires. The tab for visualizing the Pareto optimal solutions obtained is shown in Fig. 5. The aim of visualization is to give support for the DM in comparing different Pareto optimal solutions and to help him/her obtain more information on interrelationships of the objective functions. Again, this tab is divided into three parts: the left side of the tab is reserved for the visualization of the objective function values of the selected solutions while all the solutions and the best candidates are shown on the right side of the tab, respectively.

There are several types of visualizations available and the DM can choose the one (s)he <sup>fi</sup>nds most suitable. The DM must also select the solutions to be visualized (e.g., all of them, best candidates or selected ones). The solutions can be visualized with absolute or relative values of the objective functions. Fig. 6 shows examples of different types of visualizations that IND-NIMBUS can offer. The visualizations shown in the <sup>fi</sup>gure are 3D bars, value paths, whisker plot and petal diagrams, respectively. Other visualizations offered by IND-NIMBUS are bar chart, multiway dot plot and spider web chart. More information about visualizations in IND-NIMBUS can be found in [18], [19] and [20]. The numerical values of the Pareto optimal solutions obtained can also be exported to some other inspection tool more familiar to the DM, e.g. Microsoft Excel.

## 4. Case study

To illustrate the applicability of the new design tool and the interactive solution strategy in it (presented in Section 3), we report the results of solving a case study related to municipal wastewater treatment described in Section 2.

## 4.1. Case description

As said, in our case study, we need to balance between the amount of residual ammonium nitrogen in the treated wastewater, the usage of alkalinity chemical and the power consumption of the process. In other words, the DM operates on three con<sup>fl</sup>icting objective functions to be minimized, namely the residual ammonium nitrogen concentration $\{ g N / m ^ { 3 } \}$ , the dose of alkalinity chemical $[ m ^ { 3 } / d ]$ and the consumption of energy by aeration [kW]. In what follows, we will denote them by N, A and E, respectively. The primary objective N should be kept at a suf<sup>fi</sup>ciently low level while the other two objectives should be minimized as well.

The decision variables in our optimization problem are $C _ { M L S S } [ k g / m ^ { 3 } ] ,$ alkalinity chemical dosign rate $[ \bar { m } ^ { 3 } / d ]$ and the O -concentration in the last section of the reactor [g/m<sup>3</sup>]. The upper bounds used for the decision variables are 6.0, 500 and 2.5, respectively, while the lower bound for each is zero. Note that all the decision variables are continuous. The decision variables are coded into the process simulator and are automatically adjusted during the multiple simulation runs; the DM only adjusts the desired values of the objectives. As constraints of the optimization problem, we set restrictions for alkalinity of treated wastewater, that is, we require that the alkalinity remains between 1.5 and 2.0 mol/m<sup>3</sup>.

In our design tool, the optimization problems (produced by the NIMBUS method) were solved by using the controlled random search algorithm [26] (available in the IND-NIMBUS software). The DM involved in the solution process was an expert in WWTP design. In what follows, we describe the solution process.

## 4.2. Interactive solution process

At the beginning of the interactive solution process with the NIMBUS method, approximations of the ranges for the values of the objective functions in the set of Pareto optimal solutions were computed. These bounds help the DM in classi<sup>fi</sup>cation because (s)he gets some idea of what kind of objective function values are possible to achieve. The approximations of the lower (best) and upper (worst)

![](/api/attachments/X45PFA9K/fulltext/images/a56f7b65f9559789be9bf88f7cb049ee6da10572bac35fef2077f31167b578c1.jpg)  
Fig. 5. A screenshot of the visualization tab.

![](/api/attachments/X45PFA9K/fulltext/images/54179f1ac9dfd957036840cbc2c2bdfa85e5412261fbb5921e97d190ca6e2683.jpg)  
Fig. 6. Examples of different visualizations.

bounds for the objective functions in our case were (0.03,0.45,308) and (31.5,354,599), respectively.

The interactive solution process was started from a neutral compromise solution, which had the objective function values (8.05,218,460). For the DM, the value of N was not tolerable and indicated that, with these settings, the process would not work. Therefore, the DM made the <sup>fi</sup>rst classi<sup>fi</sup>cation to improve the value of N until 1, and allowed the value of A to increase up to 330. The value of E was satisfactory at the moment. In addition, the DM wanted to see three new Pareto optimal solutions. The resulting Pareto optimal solutions were (3.52,286,490), (1.69,326,506) and (4.90,298,477). As can be seen, it was not possible to fully satisfy the classi<sup>fi</sup>cation speci<sup>fi</sup>ed.

Of the new solutions found, the second one seemed to be the most promising. However, the value of N was still a bit too high. Therefore, the DM made the next classi<sup>fi</sup>cation to minimize N further until 0.5. In addition, he was willing to let the value of E increase up to 510 and allowed A to change freely. This time, he wanted to see two new Pareto optimal solutions. The following solutions were obtained: (1.11,336,515) and (0.55,347,528).

The latter solution obtained had the value of N below 1 and that was chosen as the basis for the next classi<sup>fi</sup>cation. After some consideration, the value 0.55 was regarded so low that the DM was willing to let it increase up to 1. Then, the DM wanted to study if the value of E could be minimized while letting the value of A change freely. He wanted to see three new solutions and the following ones were obtained: (9.36,246,448), (30.2,7.23,308) and (0.90,333,519). As can be seen from the solutions obtained, the <sup>fi</sup>rst two were not acceptable (as it turned out that it was not possible to minimize E without increasing N) but the third one seemed to be pretty good.

At this stage, the DM was almost satis<sup>fi</sup>ed. Finally, he wanted to generate intermediate solutions between the solutions (1.11,336,515) and (0.55,347,528) obtained after the second classi<sup>fi</sup>cation. By doing this, he wanted to see how the solutions would change when the value of N goes from 1.11 to 0.55. The number of intermediate solutions was set to two resulting in Pareto optimal solutions (0.92,336,519) and (0.72,332,524). Now the DM was happy with the solution process and did not want to continue. A list of the objective function values in the Pareto optimal solutions computed (numbered from the neutral compromise solution to 11) is shown in Table 1. To select the best

Pareto optimal solution the DM wanted to further analyze the solutions obtained, which we consider in the following.

## 4.3. Discussion

As the desired level of the main criterion, concentration of ammonium nitrogen in the ef<sup>fl</sup>uent, is ful<sup>fi</sup>lled completely or almost completely in solutions 5, 6, 9, 10 and 11, only these were studied further. In other words, those solutions were considered as best candidates. The values of the decision variables in the Pareto optimal solutions are shown in Table 2.

Solution 6 had the lowest ammonium concentration, which is re<sup>fl</sup>ected as the highest aerator wire power and alkalinity consumption (see Table 1). Moreover, also the C was the highest of all solutions. It can be deemed that in solution 6 there is an unnecessary high consumption of aeration and chemicals and an unnecessary high sludge concentration without substantial increase of nitri<sup>fi</sup>cation capacity or ef<sup>fl</sup>uent quality.

The remaining solutions were practically equal in terms of energy and chemical consumption and any one of them could have been selected as the <sup>fi</sup>nal solution. Because the DM needed to have only one <sup>fi</sup>nal solution (to be implemented), he made the decision based on the values of C (smaller values are better for implementation). For solutions 5 and 10, $C _ { M L S S }$ is about 3.7 while for solutions 9 and 11 it is between 3.8 and 3.9. The <sup>fi</sup>nal choice was thus made between solutions 5 and 10. Finally, solution 10 was chosen because:

Objective function values for the Pareto optimal solutions computed during the interactive solution process.

<table><tr><td rowspan="2"></td><td>N: residual ammonium nitrogen concentration</td><td>A: alkalinity chemical dosing rate</td><td>E: aeration energy consumption</td></tr><tr><td> $[gN/m^3]$ </td><td> $[m^3/d]$ </td><td>[kW]</td></tr><tr><td>Lower</td><td>0.03</td><td>0.45</td><td>308</td></tr><tr><td>Upper</td><td>31.5</td><td>354</td><td>599</td></tr><tr><td>NCS</td><td>8.05</td><td>218</td><td>460</td></tr><tr><td>2</td><td>3.52</td><td>286</td><td>490</td></tr><tr><td>3</td><td>1.69</td><td>326</td><td>506</td></tr><tr><td>4</td><td>4.90</td><td>298</td><td>477</td></tr><tr><td>5</td><td>1.11</td><td>336</td><td>515</td></tr><tr><td>6</td><td>0.55</td><td>347</td><td>528</td></tr><tr><td>7</td><td>9.36</td><td>246</td><td>448</td></tr><tr><td>8</td><td>30.2</td><td>7.23</td><td>308</td></tr><tr><td>9</td><td>0.90</td><td>333</td><td>519</td></tr><tr><td>10</td><td>0.92</td><td>336</td><td>519</td></tr><tr><td>11</td><td>0.72</td><td>332</td><td>524</td></tr></table>

Table 2  
Decision variable values for the Pareto optimal solutions computed during the interactive solution process.

<table><tr><td></td><td> $C_{MLSS}$  $[kg/m^3]$ </td><td>alkalinity chemical dosing rate  $[m^3/d]$ </td><td> $O_2$ -concentration in last section of the reactor  $[g/m^3]$ </td></tr><tr><td>NCS</td><td>3.68</td><td>218</td><td>0.19</td></tr><tr><td>2</td><td>3.30</td><td>286</td><td>1.13</td></tr><tr><td>3</td><td>3.56</td><td>326</td><td>0.66</td></tr><tr><td>4</td><td>3.16</td><td>298</td><td>1.17</td></tr><tr><td>5</td><td>3.68</td><td>336</td><td>0.71</td></tr><tr><td>6</td><td>3.96</td><td>347</td><td>0.72</td></tr><tr><td>7</td><td>3.02</td><td>246</td><td>1.59</td></tr><tr><td>8</td><td>3.09</td><td>7.23</td><td>0.68</td></tr><tr><td>9</td><td>3.84</td><td>333</td><td>0.56</td></tr><tr><td>10</td><td>3.69</td><td>336</td><td>0.99</td></tr><tr><td>11</td><td>3.85</td><td>332</td><td>0.84</td></tr></table>

• It gives a lower ammonium concentration with practically the same $C _ { M L S S }$ and only a slightly higher energy consumption than solution 5 and

• A lower ammonium concentration means more nitrifying biomass, which is important for operational safety in case of a sudden drop of temperature and/or increase of <sup>fl</sup>ow.

Let us add that the visualizations of IND-NIMBUS could be used to support the <sup>fi</sup>nal analysis between the best candidates.

Overall, the simultaneous consideration of con<sup>fl</sup>icting objectives and their interdependencies provided the DM with valuable information and new perspectives and insight into the problem. He could <sup>fi</sup>nd a very satisfactory solution and because of the interactive approach his understanding of the problem increased and he could be convinced of the usefulness of the <sup>fi</sup>nal solution. Further, the design tool was <sup>fl</sup>exible providing a possibility for further analysis of the most potential solutions instead of traditionally providing only one solution for the DM. The design tool was regarded easy and convenient to use and did not set too much cognitive load on the DM. In all, the experiences were very positive and encouraging and this case study demonstrates the need, potential and applicability of interactive decision support tools in WWTP design.

## 5. Conclusions

In this study, we have introduced a new interactive design tool for WWTP design. In addition, with a case study related to municipal wastewater treatment we have demonstrated the applicability of the tool (combining a simulator and an interactive multiobjective optimization system) in solving multiobjective optimization problems in the <sup>fi</sup>eld. Actually, the idea of formulating WWTP design problems as multiobjective optimization ones is very new and our tool is the <sup>fi</sup>rst interactive decision support system in this problem area.

To be more speci<sup>fi</sup>c, by combining the interactive multiobjective optimization tool IND-NIMBUS and the GPS-X simulator, we obtained an interactive design tool for WWTPs and could verify their operability together. With this tool, the designer is able to inspect the problematics related to WWTP design more realistically than before because (s)he can simultaneously take into account various evaluation criteria without a need to convert all the criteria e.g. into expressions of cost. Therefore, we avoid losing valuable information as unnecessary simpli<sup>fi</sup>cations in the model considered are not needed. Typically, nowadays such a simpli<sup>fi</sup>cation is made just for the sake of enabling optimization but we have here demonstrated that a more advanced and realistic approach is possible and has a lot of potential.

The results obtained from the case study of the WWTP design were very promising and provide a good basis for further research. The logical route to proceed now is as follows:

• a more complex process including multiple sludge circulations, aerated and unaerated reactor zones etc. may be addressed (e.g. nitrogen removal by predenitri<sup>fi</sup>cation or biological nitrogen and phosphorus removal by UCT-process),

• reactor volumes and areas can be used as decision variables, to include factors affecting investment costs and

• more operational variables can be included in the optimization, such as sludge circulation rates, DO concentrations in all aerated reactors, other chemical doses and sizes of functional reactor zones.

In all, the <sup>fi</sup>eld of the WWTP design can bene<sup>fi</sup>t a lot when utilizing tools of interactive multiobjective optimization in decision support. Our interactive design tool introduced is a pioneering software in the <sup>fi</sup>eld and the encouraging experiences point the way to more demanding applications.

## Acknowledgements

This research was a part of the project PROSIM, Optimization of Wastewater Treatment with Process Modelling and Simulation supported by Tekes, the Finnish Funding Agency for Technology and Innovation and the MASI technology program. The authors want to warmly thank Mr. Vesa Ojalehto for his valuable contribution with the software development.

## References

[1] E. Ayesa, B. Goya, A. Larrea, L. Larrea, A. Rivas, Selection of operational strategies in activated sludge processes based on optimization algorithms Water Science and Technology 37 (12) (1998) 327-334.

[2] P. Biswas, P. Bose, V. Tare, Optimal choice of wastewater treatment train by multiobjective optimization, Eng Optimiz 39 (2) (2007) 125–145.

[3] J. Branke, K. Deb, K. Miettinen, R. Slowinski (Eds.), Multiobjective Optimization: Interactive and Evolutionary Approaches, Springer-Verlag, Berlin, 2008

[4] V. Chankong, Y.Y. Haimes, Multiobjective Decision Making: Theory and Methodology, Science Publishing Co., Inc., New York, 1983

[5] I.A.C.P. Espirito-Santo, E.M.G.P. Fernandes, M.M. Araújo, E.C. Ferreira, NEOS server usage in wastewater treatment cost minimization, in: O. Gervasi, et al., (Eds.), Computational Science and Its Applications - ICCSA 2005, Lecture Notes in Computer Science, 3483, Springer–Verlag, Berlin, Heidelberg, 2005, pp. 632–641

[6] X. Flores, A. Bonmati, M. Poch, I.R. Roda, L. Jimenez, R. Banares-Alcantara Multicriteria evaluation tools to support the conceptual design of activated sludg systems, Water Science and Technology 56 (6) (2007) 85–94.

[7] S. Gillot, B. De Clercq, D. Defour, F. Simoens, K. Gernaey, P.A. Vanrolleghem, Optimization of wastewater treatment plant design and operation using simulation and cost analysis, Proceedings of WEFTEC '99, the 72nd Water Environment Federation Conference and Exposition, New Orleans, USA, 19998 CD-ROM.

[8] J. Hakanen, J. Hakala, J. Manninen, An integrated multiobjective design tool for process design, Applied Thermal Engineering 26 (2006) 1393–1399.

[9] J. Hakanen, Y. Kawajiri, K. Miettinen, L.T. Biegler, Interactive multi-objective optimization for simulated moving bed processes, Control Cybern 36 (2007) 283–302.

[10] HakanenJ. , SahlstedtK. , MiettinenK. , Simulation-based interactive multiobjective optimization in wastewater treatment, Proceedings of ENGOPT 2008, International Conference on Engineering Optimization Rio de Janeiro Brazil 20o8 CD-ROM.

[11] E. Heikkola, K. Miettinen, P. Nieminen, Multiobjective optimization of an ultrasonic transducer using NIMBUS, Ultrasonics 44 (4) (2006) 368–380.

[12] M. Henze, W. Gujer, T. Mino, M. van Loosdrecht, Activated Sludge Models ASM1, ASM2, ASM2d and ASM3 IWA Publishing London 2000

[13] R. Hernández-Suárez, J. Castellanos-Fernández, J.M. Zamora, Superstructure decomposition and parametric optimization approach for the synthesis of distributed wastewater treatment networks, Industrial and Engineering Chemistry Research 43 (2004) 2175–2191.

[14] J.P. Hämäläinen, K. Miettinen, P. Tarvainen, J. Toivanen, Interactive solution approach to a multiobjective optimization problem in a paper machine headbox design Journal of Optimization Theory and Applications 116 (2) (2003) 265–281.

[15] B. Holenda, E. Domokos, Á. Redey, J. Fazakas, Aeration optimization of a wastewater treatment plant using genetic algorithm, Optim Control App Methods 28 (2007) 191–208.

[16] C.-L. Hwang, A.S.M. Masud, Multiple Objective Decision Making – Methods and Applications: A State-of-the-Art Survey, Springer–Verlag, Berlin, Heidelberg, 1979.

[17] U. Jeppson, M.-N. Pons, I. Nopens, J. Alex, J.B. Cobb, K.V. Gernaey, C. Rosen, J.-P. Steyer, P. Vanrolleghem, Benchmark simulation model no 2: General protocol and exploratory case studies, Water Science and Technology 56 (2007) 67–78.

[18] K. Miettinen, Nonlinear Multiobjective Optimization, Kluwer Academic Publish ers, Boston, 1999.

[19] K. Miettinen, Graphical illustration of Pareto optimal solutions, in: T. Tanino, T. Tanaka, InuiguchiM. (Eds.), Multi-objective programming and goal programming: theory and applications, Springer–Verlag, Berlin, Heidelberg, 2003, pp. 197–202.

[20] K. Miettinen, Supporting comparison of alternatives in multiple criteria decision making with the help of visualizations Reports of the Department of Mathematical Information Technology, Series B, Scienti<sup>fi</sup>c Computing B 1/2003, University of Jyväskylä, Jyväskylä, 2003.

[21] IND-NIMBUS for demanding interactive multiobjective optimization, in: TrzaskalikT. (Ed.), Multiple criteria decision making '05, The Karol Adamiecki University of Economics in Katowice, 2006, pp. 137–1508, Katowice.

[22] K. Miettinen, M.M. Mäkelä, Interactive bundle-based method for nondifferentiable multiobjective optimization: NIMBUS, Optimization 34 (1995) 231–246.

[23] K. Miettinen, M.M. Mäkelä, Comparative evaluation of some interactive reference point-based methods for multi-objective optimisation, The Journal of the Operational Research Society 50 (1999) 949–959.

[24] K. Miettinen, M.M. Mäkelä, Synchronous approach in interactive multiobjective optimization, European Journal of Operational Research 170 (2006) 909–922.

[25] K. Miettinen, F. Ruiz, A.P. Wierzbicki, Introduction to multiobjective optimization: interactive approaches, in: J. Branke, K. Deb, K. Miettinen, R. Slowinski (Eds.), Multiobjective optimization: interactive and evolutionary approaches, Springer-Verlag, Berlin, 2008, pp. 27–57.

[26] W.L. Price, Global optimization by controlled random search, Journal of Optimization Theory and Applications 40 (1983) 333–348.

[27] G.P. Rangaiah (Ed.), Multi-objective optimization: techniques and applications in chemical engineering, World Scientic Publishing Co., Singapore, 2009.

[28] A. Rivas, I. Irizar, E. Ayesa, Model-based optimisation of wastewater treatment plants design, Environ Modell Soft 23 (2008) 435–450.

[29] Y. Sawaragi, H. Nakayama, T. Tanino, Theory of Multiobjective Optimization, Academic Press, Inc., Orlando, Florida, 1985.

[30] I. Takacs, G.G. Patry, D. Nolasco, A dynamic model of the clari<sup>fi</sup>cation-thickening process, Water Research 25 (1991) 1263–1271.

[31] A.P. Wierzbicki, Reference point approaches, in: T. Gal, T.J. Stewart, T. Hanne (Eds.), Multicriteria Decision Making: Advances in MCDM Models, Algorithms, Theory, and Applications, pages 9–1–9–39, Kluwer Academic Publishers, Boston, 1999.

Jussi Hakanen is a senior assistant of industrial optimization with the Department of Mathematical Information Technology, University of Jyväskylä, Finland. He received his PhD in mathematical information technology and his MSc in mathematics from the University of Jyväskylä, Finland. His research interests include theory, methods and applications of multiobjective optimization. Especially, he has applied (interactive) multiobjective optimization techniques to applications in chemical engineering.

Kaisa Miettinen is a Professor of industrial optimization with the Department of Mathematical Information Technology, University of Jyväskylä, Finland, where she heads the Research Group on Industrial Optimization. She received the MSc in mathematics and the PhD in mathematical information technology, both from the University of Jyväskylä, Finland. She has written the monograph Nonlinear Multiobjective Optimization (Kluwer/Springer, 1999) and over 50 peer-reviewed journal articles. Her research interests include multiobjective optimization (theory, methods, and software), multiple criteria decision making, nonlinear programming, evolutionary algorithms, hybrid approaches, as well as various applications of optimization.

Lic.Tech. Kristian Sahlstedt has worked as a consulting engineer and process specialist for wastewater treatment at Pöyry Finland Ltd since 2004. Previously he worked as a researcher in the Laboratory of Water and Wastewater Engineering of the Helsinki University of Technology, Finland. He has specialised in dynamic modelling of wastewater treatment throughout his career.
