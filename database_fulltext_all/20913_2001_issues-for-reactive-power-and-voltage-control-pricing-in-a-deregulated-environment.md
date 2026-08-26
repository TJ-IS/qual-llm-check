---
otero_id: 20913
otero_key: "A6C5NVMT"
title: "Issues for reactive power and voltage control pricing in a deregulated environment"
authors: "A.P Sakis Meliopoulos; G.J Cokkinides; Murad A Asa'd"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00107-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Issues for reactive power and voltage control pricing in a deregulated environment

A.P. Sakis Meliopoulos <sup>a,)</sup>, G.J. Cokkinides <sup>b</sup>, Murad A. Asa’d <sup>a</sup>

School of Electrical and Computer Engineering, Georgia Institute of Technology Atlanta, GA 30332-0250, USA UniÕersity of South Carolina Columbia, SC 29209, USA

## Abstract

Issues related to reactive power, voltage support and transmission losses as dictated from a certain class of electric loads are addressed. Specifically, the impact of predominantly induction motor loads on voltage support, reactive power requirements, and transmission losses is examined. These issues are examined with a model, which explicitly models the induction motor mechanical load. Simulation results on a simplified electric power system are presented. Based on these results, a pricing structure for voltage and reactive power support is proposed. The basic assumption of the paper is that, in a deregulated environment, the expense of the incremental requirements for voltage control should be charged to the member causing the additional requirements. The results of this work can also be used to justify long-term pricing agreements between suppliers and customers. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Reactive power; Induction motor loads; Voltage support; Reactive power pricing

## 1. Introduction

Voltage control in an electric power system is important for many reasons: a all end-use equip- Ž . ment need near-nominal voltage for their proper operation, b near-nominal voltage results in near- Ž . minimum transmission losses, and c near-nominal Ž .

voltages increase the ability of the system to withstand disturbances security . A reasonable voltageŽ . profile throughout an electric power system is associated with the ability of the system to transfer power from one location to another. When the voltage sags to low values, this ability of the system is compromised. The onset of power transfer inability can be detected with sensitivity analysis of reactive power requirements vs. real power load increases. This sensitivity is dependent on the characteristics of the electric load. Such sensitivity analyses have been performed using various electric load models, i.e. constant power load, constant impedance load, or combination of the two voltage-dependent load .Ž . The majority of electric loads are induction motors.

These loads do not fit into any of the load model categories mentioned 9 . Yet, they drastically affect<sup>w</sup> <sup>x</sup> the stability of the electric power system 2 . In this<sup>w</sup> <sup>x</sup> paper, we assert the need to model induction motor loads within the power flow formulation and directly evaluate the effects of such loads on reactive power requirements. It is shown that the power flow formulation can be augmented to include the specific induction motor loads. Interesting nonlinear phenom ena occur when the voltage at induction motor loads sags to low values. These phenomena affect the performance of the transmission system. In a deregulated environment, it makes sense to examine these phenomena and design a pricing model based on the economic impact of these phenomena 11 .<sup>w</sup> <sup>x</sup>

The paper is organized as follows: first, a formulation is proposed, which explicitly models the induction motors. This formulation is introduced as an extension to the usual power flow problem. Then, a sensitivity analysis procedure is introduced. This sensitivity is based on an extension of the co-state method. The proposed methods are applied to a simplified system comprising induction motor loads. The results of this system are discussed. A pricing approach for voltage support and reactive power requirements is presented.

## 2. Voltage control of induction motors

Many electric loads are primarily induction motors. These loads have their own characteristics. In general, the characteristics of induction motors are nonlinear and drastically impact the ability of the system to control the voltage. In this section, we describe these characteristics and we introduce a model, which is suitable for studying the impact of induction motors on voltage control.

Large-scale systems with induction motor loads can be modeled and analyzed by a simple extension of the power flow problem 1,3,6 . Specifically, the<sup>w</sup> <sup>x</sup> power flow equations must be augmented with the equations describing the operation of the induction motors. Consider a bus of a large electric power system, as it is illustrated in Fig. 1. In general, the bus may have generation and load, which may comprise induction motors. In this case, the power flow problem can be formulated as follows:

The power balance equation at bus k will be:

$$
\begin{array}{l} S _ {\mathrm{g} k} - S _ {\mathrm{d} k} = V _ {k} ^ {2} \sum_ {m \in K (k)} \left(g _ {k m} + g _ {\mathrm{s} k m}\right) \\ \qquad + V _ {k} ^ {2} g _ {k} - V _ {k} \sum_ {m \in K (k)} \left(V _ {m} \alpha_ {k m}\right) \\ \qquad + j \biggl (- V _ {k} ^ {2} \sum_ {m \in K (k)} \left(b _ {k m} + b _ {\mathrm{s} k m}\right) \\ \qquad - V _ {k} ^ {2} b _ {k} - V _ {k} \sum_ {m \in K (k)} \left(V _ {m} \beta_ {k m}\right) \biggr), \end{array}
$$

where $\alpha _ { k m } = g _ { k m } \mathrm { c o s } ( \delta _ { k } - \delta _ { m } ) + b _ { k m } \mathrm { s i n } ( \delta _ { k } - \delta _ { m } ) ,$ $\beta _ { k m } = g _ { k m } \sin ( \delta _ { k } - \delta _ { m } ) - b _ { k m } \cos ( \delta _ { K } - \delta _ { m } ) , ~ S _ { g k }$ is the complex power generated at bus k, $S _ { \mathrm { d } k }$ is the complex power absorbed by the load, including induction motors, $V _ { k }$ is the magnitude of the bus voltage at bus $k , \delta _ { k }$ is the phase angle of the voltage phasor at bus k.

It is important to observe that the contribution of induction motors to the term $S _ { \mathrm { d } k }$ is a function of the motor terminal voltage and the slip, $s _ { k }$ , of the motor. The above equation expresses power conservation at bus k. Specifically, the injected electric power $( S _ { \mathrm { g } k }$ $- S _ { \mathrm { d } k } )$ equals the electric power flowing into the circuits connected to bus k.

The induction motor contributes one more equation, which describes the power balance between the electric power delivered by the motor and the power absorbed by the mechanical load. For simplicity, we consider that all induction motor loads connected to a bus can be represented with an equivalent induction motor model. Then, the power balance between the electromagnetic power of the induction motor and the mechanical load is expressed in terms of the motor’s slip, the applied voltage, and the known mechanical torque:

![](/api/attachments/A6C5NVMT/fulltext/images/d4e658fbdbbb5b5f2bfdafeed5fcf145aa9cc9e7f25a4fd183453d9703ffdfae.jpg)  
Fig. 1. Illustration of a power system bus with generation and load.

$$
r _ {2 k} V _ {k} ^ {2} \left(\frac {1 - s _ {k}}{s _ {k}}\right) \Bigg | r _ {1 k} + r _ {2 k} + r _ {2 k} \left(\frac {1 - s _ {k}}{s _ {k}}\right)
$$

$$
- j \left(x _ {1 k} + x _ {2 k}\right) \Bigg | ^ {- 2} - \left(\frac {2}{P}\right) \omega_ {\mathrm{s}} \left(1 - s _ {k}\right) T _ {\mathrm{m}} = 0,
$$

where $r _ { 1 k }$ is the equivalent induction motor stator resistance, $r _ { 2 k }$ is the equivalent induction motor rotor resistance, $x _ { 1 k }$ is the equivalent induction motor stator reactance, $x _ { 2 k }$ is the equivalent induction motor rotor reactance, $s _ { k }$ is the equivalent induction motor slip, P is the induction motor number of poles, $\omega _ { \mathrm { s } }$ is the induction motor synchronous speed, $T _ { \mathrm { m } }$ is the torque of the mechanical load.

Collecting all equations for all buses, the power flow equations for the entire system can be written in the following compact form:

$$
g (\boldsymbol {x}) = 0
$$

where x is the state vector comprising phase angles and voltage magnitudes as in the usual power flow Ž . plus the induction motor slips for all buses with induction motors. These equations are a set of nonlinear equations. The standard solution method is by Newton’s method:

$$
\boldsymbol {x} ^ {v + 1} = \boldsymbol {x} ^ {v} - \mathbf {J} (\boldsymbol {x} ^ {v}) ^ {- 1} g (\boldsymbol {x} ^ {v})
$$

where $\boldsymbol { x } ^ { v + 1 }$ is the state vector iterate at the $( v + 1 ) ^ { \mathrm { s t } }$ iteration, $\pmb { x } ^ { v }$ is the state vector iterate at the Õth iteration, $\mathbf { J } ( \pmb { x } ^ { v } )$ is the Jacobian matrix of the functions $g ( \pmb { x } ) , g ( \pmb { x } ^ { v } )$ is an nx1 vector of real functions computed at $\pmb { x } ^ { v }$

The algorithm is terminated when the norm of $g ( \pmb { x } ^ { v } )$ becomes very small.

## 3. Sensitivity analysis

The sensitivity of system performance with respect to induction motor load can be defined with a number of sensitivity indices. Specifically, the following sensitivities are important:

$$
s _ {1} = \frac {\mathrm{d} Q _ {\mathrm{g} k}}{\mathrm{d} P _ {\mathrm{d} m}}
$$

$$
s _ {2} = \frac {\mathrm{d} V _ {k}}{\mathrm{d} P _ {\mathrm{d} m}}
$$

$$
s _ {3} = \frac {\mathrm{d} P _ {\text { loss }}}{\mathrm{d} P _ {\mathrm{dm}}}
$$

where $Q _ { \mathrm { g } k }$ is the generated reactive power at bus $k ,$ $V _ { k }$ is the bus voltage magnitude at bus $k , P _ { \mathrm { l o s s } }$ is the transmission losses, and $P _ { \mathrm { d } m }$ is the induction motor real power at bus m.

A general and powerful method for computing the above sensitivities has been developed. This method is an extension of the co-state method, initially developed for balanced three-phase networks $[ 4 , 5 , 7 , -$ 8,10 . A brief description of the extension of this<sup>x</sup> method to accommodate the computation of the above-defined sensitivities is presented.

The co-state method provides an elegant method for the computation of the derivative of any function with respect to any control variable. In our case, we would like to compute the derivatives of certain functions with respect to a dependent variable, i.e. $P _ { \mathrm { d } m }$ , the total induction motor load at bus m. Since $P _ { \mathrm { d } m }$ is a dependent variable, the co-state method cannot be directly applied. Introducing an independent control variable circumvents this limitation. Specifically, a control variable, u, representing real power injection at bus m is introduced. Next, four functions are introduced, $F _ { 1 } , F _ { 2 } , F _ { 3 }$ , and $F _ { 4 }$ , which represent the quantities $\mathcal { Q } _ { \mathrm { g } k } , \ V _ { k } , \ P _ { \mathrm { l o s s } }$ and $P _ { \mathrm { d } m }$ . In general, these quantities can be expressed as functions of the state vector x and the control variable u. Thus, any of the four functions is expressed as a function of x and u, i.e. $F ( \boldsymbol { x } , \boldsymbol { u } )$ . On the other hand, the states, x, and the control variable, u, must satisfy the power flow equations.

$$
g (\boldsymbol {x}, u) = 0\tag{1}
$$

where x is the system states, and u is the control variable.

![](/api/attachments/A6C5NVMT/fulltext/images/18294ec8fd677e63ee034d6b1f0b6c00435e9512974238a2de6c02a2498b5255.jpg)  
Fig. 2. A simplified electric power system — conventional induction motor loads.

Differentiation of the function $F ( \boldsymbol { x } , \boldsymbol { u } )$ and the power flow equations Eq. 1 yields:Ž Ž ..

$$
{\frac {\operatorname{d} F (\textbf {x} , u)}{\operatorname{d} u}} = {\frac {\partial F}{\partial u}} + {\frac {\partial F}{\partial \textbf {x}}} {\frac {\partial \textbf {x}}{\partial u}} {\frac {\partial g}{\partial u}} + {\frac {\partial g}{\partial \textbf {x}}} {\frac {\partial \textbf {x}}{\partial u}} = 0\tag{2}
$$

Upon elimination of the derivatives $( \partial \pmb { x } / \partial u )$ , one obtains:

$$
\frac {\mathrm{d} F (\boldsymbol {x} , u)}{\mathrm{d} u} = \frac {\partial F}{\partial u} - \frac {\partial F}{\partial \boldsymbol {x}} \left(\frac {\partial g}{\partial \boldsymbol {x}}\right) ^ {- 1} \frac {\partial g}{\partial u},\tag{3}
$$

where $( \partial g / \partial x ) ^ { - 1 }$ is the inverse of the system Jacobian matrix.

Define the co-state vector $\hat { x }$ as follows:

$$
\hat {\boldsymbol {x}} ^ {T} = \frac {\partial F}{\partial \boldsymbol {x}} \left(\frac {\partial g}{\partial \boldsymbol {x}}\right) ^ {- 1}
$$

In terms of the co-state vector $\hat { x } ^ { T } ,$ , Eq. 3 be- Ž . comes:

$$
\frac {\mathrm{d} F (\boldsymbol {x} , u)}{\mathrm{d} u} = \frac {\partial F}{\partial u} - \hat {\boldsymbol {x}} ^ {T} \frac {\partial g}{\partial u}.
$$

The above procedure is applied to the four functions $F _ { 1 } , F _ { 2 } , F _ { 3 }$ and $F _ { 3 }$ , yielding the derivatives:

$$
\frac {\mathrm{d} Q _ {\mathrm{g} k}}{\mathrm{d} u}, \quad \frac {\mathrm{d} V _ {k}}{\mathrm{d} u}, \quad \frac {\mathrm{d} P _ {\text { loss }}}{\mathrm{d} u}, \quad \text { and } \quad \frac {\mathrm{d} P _ {\mathrm{d} m}}{\mathrm{d} u}.
$$

The sensitivities $s _ { 1 } , \ s _ { 2 }$ and $s _ { 3 }$ are computed by the following equations:

$$
s _ {1} = \frac {\mathrm{d} Q _ {\mathrm{g} k} / \mathrm{d} u}{\mathrm{d} P _ {\mathrm{d} m} / \mathrm{d} u},
$$

$$
s _ {2} = \frac {\mathrm{d} V _ {\mathrm{k}} / \mathrm{d} u}{\mathrm{d} P _ {\mathrm{d} m} / \mathrm{d} u},
$$

$$
s _ {3} = \frac {\mathrm{d} P _ {\text { loss }} / \mathrm{d} u}{\mathrm{d} P _ {\mathrm{d} m} / \mathrm{d} u}.
$$

Note that the method is exact and quite efficient. It requires the computation of the co-state vector, which is done with a dual forward and back substitution 4,5,7,10 and a number of minor operations. <sup>w</sup> <sup>x</sup> Thus, the computation of the sensitivities requires operations comparable to two dual forward and back substitutions.

## 4. Example results

The application of the model presented in this paper is demonstrated on a simple electric power system, consisting of a generating substation, step-up transformer, a transmission line, step-down transformer and several induction motors. The system is illustrated in Fig. 2. The parameters of the system have been selected to represent typical systems and they are shown in Table 1. It is important to realize that the motors may or may not be controlled by variable voltage-variable frequency drives. For this system, we performed parametric studies of the voltage level, the reactive power requirement, and the transmission losses. The variable parameter is the total induction motor load. This parameter is denoted with the variable y in Table 1. Also note that the model requires the mechanical load torque, $T _ { \mathrm { m } } .$ . The assumed mechanical torque is listed in Table 1.

Table 1  
Example test system parameters

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Generator voltage</td><td>1.0 p.u.</td></tr><tr><td>Generator rated power</td><td>50 MV A</td></tr><tr><td>Step-up transformer impedance</td><td> $x = j0.1$  p.u.</td></tr><tr><td>Transmission line impedance</td><td> $Z = 0.01 + j0.1$  p.u.</td></tr><tr><td>Step-down transformer impedance</td><td> $x = j0.1$  p.u.</td></tr><tr><td>Induction motor rated voltage</td><td>13.8 kV</td></tr><tr><td>Induction motor rated power</td><td>Variable = 50 y MV A</td></tr><tr><td>Motor stator resistance</td><td>0.01 p.u.</td></tr><tr><td>Motor rotor resistance</td><td>0.015 p.u.</td></tr><tr><td>Motor stator reactance</td><td>0.1 p.u.</td></tr><tr><td>Motor rotor reactance</td><td>0.15 p.u.</td></tr><tr><td>Mechanical load torque</td><td> $T_{\text{m}} = (0.20 + 0.8(1 - s)^{2})$  y p.u.</td></tr></table>

![](/api/attachments/A6C5NVMT/fulltext/images/2793c58a1e75c924f15e674cd8e46bbbb25fd28d94322f831d9a504e7a870eb8.jpg)  
Fig. 3. Variation of the voltage magnitude at the load and of the generated reactive power vs. load rated power.

Fig. 3 illustrates the variation of the voltage magnitude and the generating unit reactive power output as the total induction motor load increases. Note that, when the induction motor load increases beyond the value of 0.90 p.u., the reactive power requirement increase and the voltage magnitude decreases below 0.9 p.u. When the load increases beyond the value of 1.2 p.u., the voltage collapses. What happens in this case is that the induction motor moves to an operating point of very high slip, in this case, s <sup>s</sup> 0.27, absorbs higher reactive power and causes the terminal voltage to dip voltage collapse . Note that the Ž . voltage collapse is abrupt and unexpected. It is important to observe that this behavior of the proposed model is realistic and quite different from simplified models such as constant power or constant impedance load models.

![](/api/attachments/A6C5NVMT/fulltext/images/e31bf0d304b15900cca2ddf5b8965f569bb0aeacd5e9e07d7fa13a745642f334.jpg)  
Fig. 4. Sensitivity of the voltage magnitude at the load vs. load rated power.

![](/api/attachments/A6C5NVMT/fulltext/images/00cd9f17968720a0501f837b56f7f10342465919e8a226820713f09cf9500885.jpg)  
Fig. 5. Sensitivity of generated reactive power vs. load rated power.

The performance of the system in the presence of induction motor loads can be better understood by studying the sensitivity of voltage magnitude, reactive power requirements and transmission losses vs. induction motor load. Figs. 4–6 illustrate these sensitivities as functions of total induction motor rated load. In Fig. 4, it is apparent that the sensitivity of the voltage magnitude becomes very high as the electric motor load approaches 1.2 p.u. It would be expedient to impose operating limits using the sensitivity of voltage magnitude. For example, if one is to apply limits to this sensitivity, i.e. 20%, then it is apparent that for this system, the induction motor load should not be more than 0.8 p.u. of the system rated power. Similarly, one can observe in Figs. 5 and 6 that the sensitivity of reactive power requirements and transmission losses increase drastically as the induction motor load increases. It is important to note that when the induction motor load is 0.8 p.u., the sensitivity of reactive power to rated load is 1.0, i.e. any additional 1 MW of load will require 1 MVA of generated reactive power. When the induction motor load becomes 1.0 p.u., the sensitivity becomes 1.58 MVA <sup>r</sup>MW. Similarly, the transmission loss sensitivity with respect to load increases drastically as the induction motor load reaches 1.0 p.u. For example, when the load is 1.0 p.u., the incremental losses become 4%, a relatively high value.

![](/api/attachments/A6C5NVMT/fulltext/images/6a880315ca1651b393c3b1ccc34a6a566d87d771c024c4733f9eff9178b07bf0.jpg)  
Fig. 6. Sensitivity of transmission loss vs. load rated power.

Figs. 4–6 illustrate that at the point before the voltage collapse, the sensitivities become very high. Specifically, the voltage sensitivity is <sup>y</sup>1.0, the reactive power sensitivity is 3.8 MVA <sup>r</sup>MW and the transmission loss sensitivity is 0.094. This data can be used in two ways. First, application of limits on system sensitivities will ensure that the system never operates near the point of voltage collapse. Second, the sensitivities can provide the basis for setting tariffs for voltage support and reactive power of predominantly induction motor loads. The basis of the tariff structure and its implementation is discussed in Section 5. One can argue that these tariffs may be applied to all loads for simplicity.

The results in Figs. 3–6 were obtained for a specific system. The same information can be obtained for any system using the proposed model. Then this information can be utilized to impose tariffs for loads that are predominantly induction motors.

## 5. Tariff structure

The basis of the tariff structure is the cost of providing voltage and reactive power support subject to acceptable system performance. Acceptable system performance can be established by imposing limits to the sensitivities of voltage magnitude and reactive power requirements. These limits are system dependent and should be decided upon extensive studies of the system. The same studies will provide the range of sensitivities of voltage magnitude, reactive power requirements and transmission losses. A direct cost can be associated with the transmission losses. An investment cost can also be associated with reactive power requirements. Let x be the average transmission loss sensitivity and z be the maximum reactive power sensitivity. Then the cost of providing these services is:

$$
C = p _ {1} x + p _ {2} z,
$$

where $p _ { 1 }$ is the price of electric energy, and $p _ { 2 }$ is the investment cost of reactive power sources.

Note that the investment cost must be computed on the basis of the maximum requirements throughout the study period. The cost C provides the basis for establishing the actual tariffs. It is also important to note that, today, technology exists to monitor the impact of a specific load on the system resources. Using this technology, one can monitor the voltage magnitude, reactive power and most importantly the sensitivities of voltage magnitude, reactive power requirements, and transmission losses. It is conceivable that pricing can be performed in real time on a use-of-resources basis.

## 6. Summary and conclusions

This paper has addressed the impact of predominantly induction motor loads on voltage magnitudes, reactive power requirements, and transmission losses. A model has been proposed to evaluate this impact on large-scale power systems. The proposed model incorporates the physical model of induction motors into the power flow formulation. As such, it is a realistic model and captures the true behavior of these loads.

Example calculations were carried out on a simplified power system. For this system, the voltage level, the active and reactive power requirements, and the transmission losses were computed vs. the total induction motor load. The model provides sensitivities of these quantities with respect to the induction motor loads and can be used to predict the total amount of load, which can be supported by the system voltage stability limit .Ž .

It was shown that there is a critical value of the load and when the load increased beyond this value, the reactive power requirements and the transmission losses increase in a highly nonlinear fashion. The onset of this condition is system dependent and can be determined with a series of simulations. A practical approach will be to use probabilistic simulation techniques, similar to those described in Ref. 11 , to<sup>w</sup> <sup>x</sup> obtain a statistical distribution of the critical induction motor loads.

The results provide the basis for deriving aggregate electric load models and the designing of a pricing schedule for voltage support and reactive power requirements. Specifically, the pricing is based on the cost function of the actual incremental losses and the cost of reactive power source requirements. Incremental loss cost is computed from the price of electric energy. The cost of reactive power sources is computed from the maximum required reactive power over a specified period of operation.

## Acknowledgements

The work reported in this paper has been partially supported by the ONR Grant No. N00014-96-1-0926. This support is gratefully acknowledged.

## References

<sup>w</sup> <sup>x</sup> 1 A.R. Bergen, V. Vittal, Power System Analysis, Prentice-Hall, Upper Saddle River, NJ.

<sup>w</sup> <sup>x</sup> 2 P. Kundur, Power System Stability and Control, McGraw-Hill, New York, 1994.

<sup>w</sup> <sup>x</sup> 3 F.C. Lu, Y.Y. Hsu, Reactive power<sup>r</sup>voltage control in a distribution substation using dynamical programming, IEE Proceedings, Generation Transmission Distribution 142 6Ž . Ž .1995 November.

<sup>w</sup> <sup>x</sup> 4 A.P. Meliopoulos, A.G. Bakirtizis, R.R. Kovacs, R.J. Beck, Bulk power system reliability assessment experience with the RECS program, IEEE Transactions on Power Systems PWRS-1 3 1986 235–243, August.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 A.P. Meliopoulos, G.J. Cokkinides, X.Y. Chao, A new probabilistic power flow analysis method, IEEE Transactions on Power Systems 6 1 1990 182–190, February.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 J.A. Momoh, R.J. Koessler, M.S. Bond, B. Stott, D. Sun, A. Papalexopoulos, P. Ristanovic, Challenges to optimal power flow, IEEE Transactions on Power Systems 12 1 1997Ž . Ž . February.

<sup>w</sup> <sup>x</sup> 7 A.P. Sakis Meliopoulos, F. Xia, Simultaneous transfer capability analysis: a probabilistic approach, Proceedings of the 11th Power System Computation Conference, Avignon, France, August 30–September 3, vol. 1, 1993, pp. 569–576.

<sup>w</sup> <sup>x</sup> 8 A.P. Sakis Meliopoulos, F. Xia, L. Luo, Monte Carlo simulation for evaluating power wheeling effects,Proceedings of the Twelfth Power Systems Computation Conference, Dresden, Germany, August 19–23, 1996, pp. 793–801.

<sup>w</sup> <sup>x</sup> 9 M.S. Sarma, Electric Machines, Steady-State Theory And Dynamical Performance, PWS Publishing Co., Boston, MA, 1996.

<sup>w</sup> <sup>x</sup> 10 F. Xia, A.P. Meliopoulos, A methodology for probabilistic simultaneous transfer capability analysis, IEEE Transactions on Power Systems 11 3 1996 1269–1278, August.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 C.W. Yu, A.K. David, Transmission pricing services in the context of industry deregulation, IEEE Transactions on Power Systems 12 1 1997 February. Ž . Ž .

![](/api/attachments/A6C5NVMT/fulltext/images/fea04a3ae691b298f3af7d756eea50ec0816ec28dec877c1698b1ce984ab9f62.jpg)

A.P. Sakis Meliopoulos ŽM 1976, SM 1983, F 1993 was born in Katerini,. Greece in 1949. He received the ME and EE diploma from the National Technical University of Athens, Greece in 1972 and his MSEE and PhD degrees from the Georgia Institute of Technology in 1974 and 1976, respectively. In 1971, he worked for Western Electric in Atlanta, GA. In 1976, he joined the Faculty of Electrical Engineering, Georgia Institute of Technology, where he is

presently a professor. He is active in teaching and research in the general areas of modeling, analysis, and control of power systems. He has made significant contributions to power system grounding, harmonics, and reliability assessment of power systems. He is the author of Power Systems Grounding and Transients, Marcel Dekker, June 1988, Lightning and Overvoltage Protection, Section 27, Standard Handbook for Electrical Engineers, McGraw-Hill, 1993, and the monograph, Numerical Solution Methods of Algebraic Equations, EPRI monograph series. Dr. Meliopoulos is a member of the Hellenic Society of Professional Engineering and Sigma Xi.

![](/api/attachments/A6C5NVMT/fulltext/images/a3c7fa2cff2cb96bb99109497606a6692758041f2b10b85b326261db478b220a.jpg)

George Cokkinides Ž .M 1985 was born in Athens, Greece in 1955. He obtained his BS, MS, and PhD degrees from the Georgia Institute of Technology in 1978, 1980, and 1985, respectively. From 1983 to 1985, he was a research engineer at the Georgia Tech Research Institute. Since 1985, he has been with the University of South Carolina where he is presently an Associate Professor of Electrical Engineering. His research interests include power system modeling

and simulation, power electronics applications, power system harmonics, and measurement instrumentation. Dr. Cokkinides is a member of the IEEE<sup>r</sup>PES.

![](/api/attachments/A6C5NVMT/fulltext/images/9826cc0caffbdfc42ab3838a0e031673674c1d8737deb415659f80fa498ecde8.jpg)

Murad Asa’d Ž . M 1998 is a graduate student at Georgia Institute of Technology in Atlanta, GA. He received his Diploma in Technology Engineering from Bradford College, UK in 1978, his BSEE from the University of Wales, Cardiff, UK in 1982 and his MSEE degree from Georgia Institute of Technology in 1995. His research interest lies in the general area of power systems in a deregulated environment.
