---
otero_id: 17483
otero_key: "HU68GUM2"
title: "Qualitative and quantitative simulation of interacting markets"
authors: "G.J Wyatt; R.R Leitch; A.D Steele"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00030-v"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Qualitative and quantitative simulation of interacting markets $^{*}$

G.J. Wyatt $^{a,*}$ , R.R. Leitch $^{b}$ , A.D. Steele $^{b}$

$^{a}$ Department of Economics, Heriot-Watt University, P.O. Box 805, Riccarton, Edinburgh EH14 4AT UK

$^{b}$ Department of Computing and Electrical Engineering, Heriot-Watt University, P.O. Box 805, Riccarton, Edinburgh EH14 4AT UK

## Abstract

Traditional quantitative methods of analysis and simulation are compared with recently developed techniques in qualitative simulation by using as a case-study a simple dynamic model of the interacting markets for housing and mortgages. Analysis by the different techniques shows that while the qualitative simulation requires less detailed models, of the precision normally available in practice, it results in ambiguous descriptions of behaviour that for certain initial conditions can obscure the true behaviour. By contrast, quantitative simulation produces a unique precise behaviour, but in requiring excessively specific information of the modeller it may produce an inaccurate if precise outcome.

Keywords: Qualitative simulation; QSim; Housing market; Mortgage market; Flowgraph; Envisionment

## 1. Qualitative reasoning with economic models

The objectives of qualitative reasoning are to accurately represent our limited understanding of the system, and to reason within that limited understanding, so that correct but abstract inferences can be drawn, which are not based on assumptions introduced for such reasons as tractability, simplicity, convenience or elegance.

Qualitative reasoning has a long tradition in economics. Methods of comparative statics, which use verbal, diagrammatic and algebraic qualitative methods, are the common currency of discourse in the subject. Comparative statics enables quite powerful inferences to be made about the equilibrium states of simple systems when they are subjected to small perturbations. The system is assumed to be stable and the transition between equilibria is ignored. In fact, assumptions about stability are often useful in deriving comparative static implications via the ‘correspondence principle’ [7]. However, a local linear approximation in the neighbourhood of an equilibrium is often used to derive these implications, and this could be precarious since nonlinear dynamic systems have the potential for chaotic response to minor perturbations.

Chaotic behaviour presents severe problems for model-based explanation of the system. But even if chaos can be ruled out, there are still formidable difficulties in reasoning about dynamic systems. Economists using qualitative methods are usually anxious to preserve an agnostic stance about the transient behaviour of a system, limiting themselves to statements about the ‘short-run’ and the ‘long-run’, i.e. the impact and steady state responses respectively. Although such statements can be fairly robust, they avoid the very detail that is necessary for useful prediction. By contrast, such detail is provided in quantitative forecasts based on econometric estimates of dynamic economic models, but these often have a misleading precision which belies their common inaccuracy and unreliability.

The first problem with imprecise knowledge is to acknowledge it and describe it. This is the unavoidable task of an honest analyst. Then, reasoning with this imprecise knowledge is a major problem because it is inherently ambiguous. Whereas a precise dynamic system defined in terms of the real numbers has a unique evolution in response to some external perturbation, a system with a qualitative representation of the system states can show a bewildering variety of evolutions. That is to say, there may be several logically valid possibilities for transitions in the state of the system at any ‘moment’. The point of computer assistance in this setting is to keep track of these logical possibilities, retaining the complete set of possible behaviours for analysis. Faced with modelling uncertainty, the fundamental question to ask when considering quantitative or qualitative descriptions of behaviour is: is it better to have a precise (i.e. quantitative) prediction from an inaccurately described model or an imprecise (i.e. qualitative) prediction from an accurately described model?

During the last decade techniques for deriving the qualitative behaviour of a dynamic system have been explored $[5,9]$ . The most popular technique is Qualitative Simulation, 'QSim', developed by Ben Kuipers and coworkers $[6]$ . This can be considered as the qualitative counterpart to numerical simulation in that a set of equations (qualitative constraints) are described, and initial conditions for the state variables chosen. The simulation will then generate a qualitative description of the behaviour of the system until an equilibrium state is reached, or not. The qualitative description consists of a set of alternating real values, called 'landmarks', and open intervals between them, which give rise to corresponding time points associated with the landmarks, and durations associated with the open intervals. Qualitative simulation has been shown to be sound, in that it generates the correct qualitative solution to the system. However, because of the inherent ambiguity of (any) qualitative calculus, the algorithm also generates many 'spurious' behaviours that do not correspond to any actual qualitative solution to the equations. Much of the development of qualitative simulation has been aimed at minimising the spurious behaviours while retaining the soundness property [9]. More recently, less abstract (more precise) descriptions of behaviour have been proposed [8] that result in less spurious behaviours through the utilisation of semi-quantitative information when this is available. The trend is, therefore, to represent the model at the level of precision consistent with the knowledge about the system in such a way that meaningful inferences can be made, and to construct inference procedures to handle such information. This paper contributes to the small but growing literature on this topic [4].

## 2. A specific problem area: dynamic, interacting markets

The study reported here is part of an EC-funded working group on AI and economic modelling, in which various artificial intelligence methods are applied to a common problem area, namely the housing and mortgage markets in the Netherlands. Housing and mortgage markets are obviously rather closely coupled. It is difficult to understand developments in one of them without referring to the other. Moreover, it is clear that static analysis would provide an inadequate framework for addressing many of the key questions that arise, such as those concerning house price inflation, mortgage rationing and so on. Thus, these markets provide a suitable setting for the application of computer-based qualitative simulation. In this section we set out a conceptual model of these markets. The model is ‘conceptual’ in the sense that it aims only to capture some typically salient features of these markets; it would not necessarily be appropriate for any particular real world pair of housing and mortgage markets without suitable adaptation to incorporate the relevant institutional features. For present purposes, the model merely needs to be sufficiently plausible in some potential context for its implications to be worth serious consideration.

The model describes the interacting markets for housing and mortgages. However, it ignores the impact of these markets on the rest of the economy, such as those that might occur as changes in house prices and mortgage debt affect real wealth or inflation. In principle such effects would feed back into the housing and mortgage markets, but we have to draw the boundary somewhere! Accordingly, these variables are considered to be exogenous.

The model's dynamics arise on the one hand from a slower than instantaneous adjustment of house prices to changes occurring in the housing market, which might be due, for example, to adjustment costs, or menu costs. On the other hand, there is also a dynamic process of stock adjustment in the mortgage market. The model is set out in equation form below.

$$
\dot {P} = \phi \binom{E ^ {H}}{+}\tag{1}
$$

$$
E ^ {H} = H ^ {d} - \overline {{{{H}}}} ^ {s}\tag{2}
$$

$$
H ^ {d} = \eta (\underline {{{P}}})\tag{3}
$$

$$
D = \frac {M}{V}\tag{4}
$$

$$
V = P \cdot \overline {{H}} ^ {s}\tag{5}
$$

$$
\dot {M} = \psi \left( \begin{array}{c} E ^ {M} \\ + \end{array} \right)\tag{6}
$$

$$
E ^ {M} = M ^ {d} - M\tag{7}
$$

$$
M ^ {d} = \overline {{{D}}} ^ {d} \cdot V\tag{8}
$$

In this model the variables are represented by uppercase Roman letters. $\overline{H}^{s}$ represents the exogenous supply of housing, $H^{d}$ the demand for housing, $E^{H}$ the excess demand for housing and P the level of house prices. M is the stock of mortgage debt, $M^{d}$ the desired stock of mortgage debt and $E^{M}$ the excess demand for mortgage debt. V is the value of the housing stock and D the ratio of housing debt to house value. It is assumed that there is a desired ratio of mortgage debt to housing value, which is represented by $\overline{D}^{d}$ The Greek letters represent functions, all of which are assumed to be monotonic in their variables. The model assumes that financial gearing (D) is neutral, i.e. does not affect the demand for housing. As a result, there is no feedback from the mortgage market to the housing market. If such feedback is allowed, for example because more highly geared agents face larger transaction costs in the housing market, there would be a richer set of dynamic outcomes. We choose to ignore such complexity in order to focus on the methods of analysis. For the same reason, the model is kept as simple as possible by assuming income, wealth and interest rates to be exogenous and constant. Note also that the price of housing has been expressed as an asset price rather than the rental price for housing services. Although these simplifications certainly affect the realism of the model, the purpose here is to illustrate the state of the art regarding qualitative simulation, and this is best done with a model that has been pared down as much as possible.

Suppose that this set of equations represents our stylised understanding of the housing and mortgage markets. There are now several ways to investigate the behaviour of this system. First we could assume that the system is stable, eliminate the dynamics, and conduct comparative static analysis of the effect of exogenous changes on the equilibrium. Secondly, we could make a linear approximation to the system, and derive analytical solutions for its dynamic evolution. Thirdly, we could allow the system to be non-linear, and depict its qualitative behaviour by means of a phase diagram. Fourthly, retaining the nonlinearity but with numerically specified functions and initial values, we could simulate instances of its evolution. Fifthly, and what concerns us here, we could try to retain the qualitative specification, without linearizing or assuming specific nonlinear functions, and simulate its qualitative evolution. Each of these possibilities has advantages and disadvantages which are best clarified by their application.

## 3. Traditional modes of analysis

## 3.1. Comparative statics

Equilibrium is synonymous with ‘steady state’, and is obtained by setting $\dot{P}=0$ and $\dot{M}=0$ . Then by totally differentiating the system we can derive the effects of changes in the exogenous variable $H^{s}$ on the equilibrium values of the endogenous variables. Thus, for example, we find the following results:

$$
d P = \frac {d \overline {{H}} ^ {s}}{\eta_ {P}}
$$

$$
d M = \left(\frac {\overline {{{H}}} ^ {s}}{\eta_ {P}} + P\right) \overline {{{D}}} ^ {d} \cdot d \overline {{{H}}} ^ {s}
$$

where the variables are measured at equilibrium and the differentials represent shifts in the equilibrium. Subscripts indicate partial derivatives of the relevant functions. This implies that an increase in the housing stock reduces the equilibrium house price since $\eta_{P}<0$ but the sign of the effect on the stock of mortgage debt is ambiguous.

## 3.2. Linear approximation of a real-valued dynamic system

For the purpose of linearisation we now measure all the variables apart from $E^{H}$ and $E^{M}$ on a logarithmic scale. This converts the division of equation (4) into subtraction and the multiplications of equations (5) and (8) into additions. The time derivatives now represent proportional rates of change. Furthermore we stipulate that the Greek letters now represent positive parameters instead of functions, thus $\eta$ is interpreted as the price elasticity of housing demand, so equation (3) becomes $H^{d} = -\eta \cdot P$ . The most convenient way to handle the system thus linearised is to represent it as a flowgraph, displaying causal connections, in complex frequency space using the Laplace transform [2]. Such a flowgraph is displayed in Fig. 1.

The system determinant is $\Delta(s)=s^{2}+(\Psi+\phi\eta)s+\Psi\phi\eta$ . The composite coefficients in this quadratic in s (the dummy Laplace transform variable) are all positive, which implies that the real parts of its roots are negative, and the system is stable. The response of house prices and the stock of mortgages to the exogenous variable is given by:

![](/api/attachments/HU68GUM2/fulltext/images/6ec36c32b86ba33485b1fb38a03df73c3dc412b381db92d597c385b77cb71596.jpg)  
Fig. 1. Flowgraph representation of the model.

$$
\begin{array}{l} P (s) = \big (- \phi (\Psi + s) H ^ {S} (s) \big) / \Delta (s) \\ M (s) = \big (\Psi s + \phi \Psi (\eta - 1) \big) H ^ {s} (s) \big) / \Delta (s). \end{array}
$$

The inverse Laplace transform of these equations gives the complete analytical time path of house prices and mortgages once the time path of the exogenous housing stock is given. This enables investigation of the effects of changing the parameter values on qualitative aspects of the detailed time path, such as overshooting, oscillation and damping. However, the eventual steady state can be evaluated without taking the inverse transform, by using the fact that it is given by the limits of $sP(s)$ and $sM(s)$ as s goes to infinity. If we assume a step increase in the exogenous variables, for which the Laplace transforms are

$$
H ^ {s} (s) = d H ^ {s} / s
$$

and

$$
D ^ {d} (s) = d D ^ {s} / s,
$$

the implied change in the steady state can be seen to be qualitatively equivalent with the comparative statics implications outlined in 3.1 above.

## 3.3. Phase diagram

A phase diagram can be an effective representation of the behaviour of a nonlinear system that can be reduced to two state variables. The housing and mortgage model yields the phase diagram shown in Fig. 2. The shape of the curve depicting equilibrium in the housing market, $\dot{P}=0$ is horizontal while that depicting equilibrium in the mortgage market, M = 0 slopes upwards.

![](/api/attachments/HU68GUM2/fulltext/images/13b555e9c15c27fd90c457be600c09282270b56e4fc4434fd2a4d3b23425f88d.jpg)  
Fig. 2. Phase diagram.

## 3.4. Numerical simulation

In order to carry out a standard numerical simulation, it is necessary to specify: (i) the exact form of the functions in the model; (ii) the precise values of the parameters in those functions; and (iii) the numerical starting values of the variables. Given this information, the output of a numerical simulation can easily be visualised as the evolution of the variables over time as in Fig. 3. Alternatively, a trajectory through the state space could be shown. To produce Fig. 3, the following assumptions were made: equations (1) and (6) of the model were simple proportional functions with coefficients equal to 1 and 0.4 respectively, equation (3) was set to

$$
H _ {d} = 2 2 - 5 \sqrt {P},
$$

the exogenous variables were set at

$$
\overline {{{H}}} ^ {s} = 1 0
$$

and

$$
\overline {{{D}}} ^ {d} = 0. 8,
$$

and the integrating variables were initialized at $P_{0}=7$ and $M_{0}=M^{d}-10$ . Thus there is initially an excess supply of housing and excess demand for mortgages. Of course, all these ‘guesses’ are responsible for the unique solution.

## 4. Qualitative simulation

The objective of qualitative simulation is to produce all the possible qualitative behaviours of the system that are consistent with the qualitative understanding of the model. Thus, it uses the same qualitative information about the system as comparative statics, but it also aims to describe the transient paths and to determine the existence of unstable behaviour. It differs from the real-valued dynamic modes of analysis described above by only utilising the qualitative knowledge of the system; it does not require the modeller to 'guess' real values in order to solve the equations. In its current state of development, however, it too has various problems as a tool of analysis. First, it is not a trivial task to specify the qualitative model accurately and completely; secondly, the computer generation of the tree of possible evolutions can absorb a huge amount of computer memory, much of which represents spurious behaviour; and thirdly, there is a problem in designing an effective means of reporting the output when there are many possible evolutions of the system.

![](/api/attachments/HU68GUM2/fulltext/images/aa4218f0e8999b5bf45997b7643897f8e6f7be61ed19528c0bce9153b23564d1.jpg)  
Fig. 3. Numerical simulation.

The method of qualitative simulation that we report here is based on the QSim algorithm. We assume a ‘quantity space’ of three elements: positive, zero and negative. Within this quantity space there are qualitative ‘landmarks’ which are points of some significance, either because they mark a change in behaviour, such as a switch from positive to zero in the rate of change of some variable, or because the analyst has stipulated these points as being of interest in the setting up of the simulation.

The model represents a one-way coupling between the housing market and the mortgage market. Both markets individually contain first-order dynamic adjustment processes. A first step in simulating the whole system is to simulate these first-order components separately. For each separate market QSim generates just one qualitative path from any consistent initial state. This is to be expected. Coupling the two markets is however more problematical for the qualitative simulator. We now explore in some depth the qualitative simulation when the two markets are coupled in the one direction given by the full model: the state of the housing market affects the mortgage market, but not vice-versa. It is useful to recall the phase diagram displayed in Fig. 2 above.

The qualitative behaviour of the system depends on which region in the phase plane it starts from. The phase plane contains nine regions, defined in terms of the qualitative state of the pair of variables $\dot{P}$ and $\dot{M} (<0, =0, >0)$ . Thus also points on the curves $\dot{P}=0$ and $\dot{M}=0$ are considered as regions. The regions are labelled by numerals in Fig. 4.

![](/api/attachments/HU68GUM2/fulltext/images/8e569858b4340aabb2fecf646e4ab629561453f2af8b1b6d5e8a5563b4155a7b.jpg)  
Fig. 4. Qualitative states of the system.

We consider QSim analyses of a few of these regions in detail before summarizing the qualitative analysis of the model (simulations were performed both on a Sun Sparc station using QSim 2.0, written in LISP, and on a 486 pc running MS-DOS using SIMCC [1], written in Turbo C. The input syntax illustrated is that of QSim).

Region 1 is the equilibrium state of the system. Initializing QSim in this region confirms that no changes ensue. There is only one qualitative behaviour.

Region 2 implies equilibrium in the housing market, but excess demand in the mortgage market. Qualitative simulation from this starting point shows P to remain constant while M increases to an equilibrium. To ensure this sensible outcome, it was necessary to initialize M at a finite value.

Region 6 is similarly a state of equilibrium in the housing market, but with excess demand in the mortgage market. Again, starting in this state, QSim yields the expected unique behaviour.

Regions 3, 4, 5, 7, 8, 9 all displayed the expected behaviours when examined by QSim, but they also gave spurious output in the sense that the QSim algorithm identified multiple instances of these behaviours, and usually continued doing so until all available computing memory was exhausted.

To illustrate the QSIM input syntax, we reproduce part of the input for a simulation in which the system is initialised in region 7, with both house prices and the stock of mortgages falling -i.e. a situation of simultaneous excess supply in both markets. The simulator requires first that the quantity spaces be defined, i.e. the set of qualitative values or pre-set landmarks for each variable in the model. Thus, for the housing variables we set:

```lisp
(P (0 inf))    ;; house prices
(dP (minf 0 inf))    ;; change in
    house prices
(Hd (0 inf))    ;; demand for
    housing
(Hs (0 inf))    ;; supply of
    housing
(Eh (minf 0 inf))    ;; excess demand
    for housing.
```

The constraints (i.e. equations) are formulated thus:

```txt
((constant Hs)) ;; Hs is constant (exogenous)
((d/dt P dP)) ;; dP is the rate of change of P
((ADD Hs Eh Hd)) ;; n.b. no subtraction constraint in QSIM
((M+Eh dP)) ;; dP a monotonic increasing function of Eh
((M-P Hd)) ;; Hd a monotonic decreasing function of P.
```

Initial conditions are specified thus:

(P ((0 inf) dec)) ; House prices are falling
(dP ((minf 0) inc)) ; but the rate of change is increasing
(Hd ((0 inf) inc)) ; housing demand is increasing
(Hs ((0 inf) std)) ; housing supply is constant
(Eh ((minf 0) inc)) ; excess demand is negative but increasing.

The initialisation is checked for consistency with the constraints in the model.

A total of 39 behaviours resulted from this initialisation, with 31 of them being incomplete (i.e. not terminated at a steady state or at the limiting values of all variables) when the memory resource limit of the computer was exhausted. Although this appears to be an excessively large number of behaviours, it contains just three separate types of trajectory of the state variables P and M. The remaining behaviours are due to the other variables reaching landmark values during these three types of trajectory for P and M. The eight complete behaviours all involve the rates of change of the state variables P and M going to zero –i.e. the system reaching equilibrium. They only differ in that the equilibrium is reached at positive or zero values of the state variables. While the latter cases are unusual, they are nevertheless meaningful outcomes of the model since it is conceivable that housing demand falls so far short of supply that all housing wants are met at zero price; and of course the demand for mortgages vanishes if housing is so abundant that its price is zero.

In view of the fact that the QSim output appears indeterminate in many instances, it is useful to examine what behaviours we would wish to be revealed by a qualitative simulation. In essence, the qualitative state of a system is determined by the signs of the rates of change of the state variables. Thus Fig. 5 summarizes in a semi-pictorial manner all the relevant states and transitions to subsequent states. If the system can remain in a state for a finite time period, its possible presence in that state is represented by a small open circle. But if a state is essentially momentary only, the system's possible presence in that state is represented by a black dot. The arrows depict the possible transitions to neighbouring states. A minimal requirement of a qualitative simulation is that it should produce all the qualitative trajectories implied by Fig. 5, which is called an ‘envisionment’ of the system. However, it is not clear from our simulations that with typically finite computing resources such a requirement can be fulfilled for models of sufficient complexity to benefit from computer assistance.

<table><tr><td> $\dot{M}$ P</td><td>-</td><td>0</td><td>+</td></tr><tr><td>+</td><td></td><td></td><td></td></tr><tr><td>0</td><td></td><td></td><td></td></tr><tr><td>-</td><td></td><td></td><td></td></tr></table>

Fig. 5. Envisionment table of qualitative transitions.

## 5. Conclusions

The various modes of analysing the housing and mortgage model set out in sections 3 and 4 above have their advantages and disadvantages. Comparative statics retains the qualitative nature of the model, is normally the simplest to do, but only yields statements about changes in the equilibrium, assuming it to be stable. It ignores the path between equilibria. Linear approximation could be thought of as a generalisation of comparative statics to include dynamics. However, it makes more demands of the analyst, and the approximation may have doubtful validity as a representation of the possible transient behaviours of the underlying nonlinear model. Phase diagrams give powerful pictorial representations of the whole set of transient paths while retaining the nonlinear specification of the system. However, the precise partition of the phase space which a phase diagram employs can be misleading since the qualitative knowledge of the system may be consistent with very different partitions. The same difficulties occur with numerical simulation, and are indeed compounded by the misleading precision of the output generated by arbitrarily selected functions with numerically specific parameters. Nevertheless, numerical simulation is the natural way to explore an econometrically estimated model.

The great attraction of qualitative simulation is that it properly incorporates the inexact knowledge about the system being modelled, so that its results are not the consequences of unfounded assumptions. In the present state of the art, however, it suffers from producing spurious behaviours and combinatorially intractable output for ‘interesting’ models. Nevertheless, our investigations demonstrate that it is already feasible to apply qualitative simulation to interesting economic models.

The problem of spurious behaviours in QSim is tackled in more recent approaches which utilise semi-qualitative information to capture more detailed descriptions of the functional relations. Q3 [3], applies numerical upper and lower bounds to variables, whereas FuSim [8] implements a fuzzy quantity space and uses fuzzy rules to represent the uncertain functions. This is an active area of research which holds out the prospect of significantly reducing the spurious behaviours whilst producing a dynamic simulation at a degree of precision consistent with the underlying knowledge and data. Its application to the modelling of economic systems is reported in [8].

## References

[1] J.J. Alba, J. Villar, J. and A. Muños, 1992, Constraint-based qualitative simulation and its application to diagnosis (Instituto de Investigacion Tecnologica, Universidad Pontificia Comillas, Madrid).

[2] D.K. Anand, 1984, Introduction to control systems (Pergamon Press Ltd., Oxford).

[3] D. Berleant and B. Kuipers, 1992, Qualitative-numeric simulation with Q3, in B. Faltings and P. Struss eds., Recent advances in qualitative physics (MIT Press, Mass).

[4] R. Berndsen R., 1992, Qualitative reasoning and knowledge representation in economic models (PhD thesis, Katholieke Universiteit Brabant, Tilburg, Netherlands).

[5] D.G. Bobrow, ed., 1984, Qualitative reasoning about physical systems (North-Holland, Amsterdam).

[6] B. Kuipers, 1986, Qualitative simulation. Artificial Intelligence, 29, pp. 289–338.

[7] P.A. Samuelson, 1947, Foundations of economic analysis (Harvard University Press, Cambridge, Mass.)

[8] J.A. Scott, R.R. Leitch and G.J. Wyatt, 1995, Reducing precision to achieve accurate economic models, Economic and Financial Computing, Summer Autumn.

[9] Q. Shen and R.R. Leitch, 1991, Fuzzy qualitative simulation, IEEE Transactions Systems, Man and Cybernetics, 23, 4, 1038–1061.

[10] D. Weld and J. de Kleer, eds., 1992, Readings in qualitative reasoning about physical systems (Morgan Kaufman, San Mateo, California).

![](/api/attachments/HU68GUM2/fulltext/images/b71dbdaf15777dde11bae5bd241e3979df4fb5d36c4be5acf385578409610974.jpg)

Geoffrey Wyatt, BA (Keele), DPhil (York) is Reader in Economics at Heriot-Watt University where he was recently Head of the Economics Department. He has been involved in model building and forecasting at the OECD in Paris. His main publications have been on the economics of research, invention and technical change, and on the industrial organisation of derivative asset exchanges. Current research interests centre on

the representation of economic models by causal graphs and the application of qualitative modelling to economics.

![](/api/attachments/HU68GUM2/fulltext/images/5c0dd588f3fbd7af79da664e194833849f22e91e59c88608988237e318424472.jpg)

Roy Leitch, BSc, PhD (Heriot-Watt) is Professor of Systems Engineering and Director of the Intelligent Systems Laboratory in the Department of Computing and Electrical Engineering at Heriot-Watt University. His research activities include the use of Knowledge Based System techniques for the control and diagnosis of industrial processes and the development of intelligent training and education systems based on Artificial

Intelligence methods. The current focus of the work is in the development of qualitative simulation techniques and their application to model-based reasoning for dynamic systems. He is a Fellow of the Institution of Electrical Engineers.

![](/api/attachments/HU68GUM2/fulltext/images/c631068f874f14eba7cf9c79f07e8e4c14c2102adbb9fd3820d10b817ef0c380.jpg)

Andrew Steele, received the MEng degree in electrical and electronic engineering in 1992 from Heriot-Watt University, and is currently working towards a PhD on time-constrained model-based diagnosis of dynamic systems.
