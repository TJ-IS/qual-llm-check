---
otero_id: 21661
otero_key: "YXS3ZANA"
title: "Modeling the consumer benefit in the optimal power flow"
authors: "James D. Weber; Thomas J. Overbye; Christopher L. DeMarco"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00071-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modeling the consumer benefit in the optimal power flow <sup>1</sup>

James D. Weber <sup>a,)</sup>, Thomas J. Overbye <sup>b,2</sup>, Christopher L. DeMarco <sup>c,3</sup>

<sup>a</sup> Department of ECE, UniÕersity of Illinois, EÕeritt Lab 338, 1406 W. Green, Urbana, IL 61801, USA

<sup>b</sup> Department of ECE, UniÕersity of Illinois, EÕeritt Lab 343, 1406 W. Green, Urbana, IL 61801, USA

Department of ECE, UniÕersity of Wisconsin-Madison, 1415 Engineering DriÕe, Madison, WI 53706, USA

## Abstract

The addition of a model of the consumer into the traditional optimal power flow OPF algorithm that minimizes supplierŽ . costs is investigated. The development of such a model is based on the solution of the OPF using an objective function for maximization of social welfare. A traditional OPF algorithm can be modified to solve the social welfare maximization problem by including price-dependent load models. This modification to the traditional OPF is intuitive and very simple. This modified OPF formulation facilitates simulation of spot markets for both real and reactive power. The algorithm is effective on systems of hundreds of buses, but small examples to compare the results to the traditional OPF are also insightful. The impact of price-dependent loads on systems with transmission congestion, increased fuel costs, and voltage problems can be studied. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Optimal power flow OPF ; Real-time pricing; Price-dependent loads; Reactive power; Load models; Electricity demand;Ž . Electricity supply; Consumer benefit

## 1. Introduction

Over the last 30 years or so, the optimal power flow OPF algorithm has been an active area of research.Ž . The OPF is defined as a static, nonlinear optimization problem in which certain control variables are adjusted to minimize an objective function, while satisfying physical and operational constraints. Typically, the objective function has been to either minimize the cost of generation, or to minimize system losses. Available controls have usually been power system devices, such as generator real and reactive power outputs, real power transactions between operating areas, transformer tap or phase positions, and switched shunt devices. Customer load has not been usually an explicit control device, except in the extreme case of ‘load shedding’ in which the load is involuntarily disconnected.

For the most part, the absence of load as a control in the OPF has been due to the inability of the operating utility to directly or indirectly control the load. The present-day flat and time-of-use rate structures have provided no opportunity for price-based control of most loads, with interruptible contracts and direct load management begin two possible exceptions.

However, over the last 10 to 15 years, there has been a growing movement towards providing customers with more price feedback through an electricity spot market. Much of the theory for such a market is described in Ref. 9 , with the definition of a spot price given as one in which customers are charged the marginal cost of<sup>w</sup> <sup>x</sup> providing electricity to their point of service that is, their node or bus . Other papers have addressed the issues Ž . of power system spot markets as well 2,8 . A key advantage of nodal spot prices is they provide a more <sup>w</sup> <sup>x</sup> economic approach to pricing with a result of improved transmission efficiency. In such a market, customer load is assumed to vary in response to changing prices according to its demand curve. That is, load becomes price-dependent and hence, a potential OPF control.

In this paper, we investigate the inclusion of such price-dependent loads in the OPF. While the inclusion of such price-dependent loads has been done 1 , here we provide a more formal argument for their inclusion and<sup>w</sup> <sup>x</sup> show how they can easily be added to a traditional OPF. By traditional OPF, we mean an OPF that minimizes the supplier fuel costs.

The OPF problem has been solved using a variety of different techniques. Here, we employ the Newton’s method approach 10 .<sup>w</sup> <sup>x</sup>

## 2. Notation

## 2.1. General conÕentions on notation for this paper

<sup>Ø</sup> All vector and matrix variables are in bold.

<sup>Ø</sup> All vectors are column vectors.

<sup>Ø</sup> Subscript p and subscript q signify a relation to real and reactive power, respectively.

## 2.2. Variable definitions

$$
\mathbf {s} = [ \mathbf {s} _ {\mathrm{p}} ^ {T} \mathbf {s} _ {\mathrm{q}} ^ {T} ] ^ {T}
$$

State variables and other controls e.g., tap ratiosŽ .

$$
\mathbf {d} = [ \mathbf {\tilde {d}} _ {\mathrm{p}} ^ {T} \mathbf {\tilde {d}} _ {\mathrm{q}} ^ {T} ] ^ {T}
$$

Supply vector

$$
\hat {\mathbf {s}} = [ \hat {\mathbf {s}} _ {\mathrm{p}} ^ {T} \hat {\mathbf {s}} _ {\mathrm{q}} ^ {T} ] ^ {T}
$$

Demand vector

$$
\hat {\mathbf {d}} = [ \hat {\mathbf {d}} _ {\mathrm{p}} ^ {T} \hat {\mathbf {d}} _ {\mathrm{q}} ^ {T} ] ^ {T}
$$

Augmented supply vector including zeros where no suppliers exists

$$
C (\mathbf {s}) = C \left(\mathbf {s} _ {\mathrm{p}}, \mathbf {s} _ {\mathrm{q}}\right) = \sum_ {\text { all   supplies }} C _ {\mathrm{k}} \left(\mathbf {s} _ {\mathrm{p}}, \mathbf {s} _ {\mathrm{q}}\right)
$$

$$
B (\mathbf {d}) = B \left(\mathbf {d} _ {\mathrm{p}}, \mathbf {d} _ {\mathrm{q}}\right) = \sum_ {\text { all   consumers }} B _ {\mathrm{k}} \left(\mathbf {d} _ {\mathrm{p}}, \mathbf {d} _ {\mathrm{q}}\right)
$$

Augmented demand vector including zeros where no loads exist Suppliers’ cost

$$
\mathbf {h} (\mathbf {x}, \mathbf {s}, \mathbf {d}) = \left[ \begin{array}{c} \hat {\mathbf {h}} (\mathbf {x}) - \hat {\mathbf {s}} + \hat {\mathbf {d}} \\ \overline {{\mathbf {h}}} (\mathbf {x}) \end{array} \right] = \left[ \begin{array}{c} \mathbf {h} _ {\mathrm{p}} (\mathbf {x}, \mathbf {s} _ {\mathrm{p}}, \mathbf {d} _ {\mathrm{p}}) \\ \mathbf {h} _ {\mathrm{q}} (\mathbf {x}, \mathbf {s} _ {\mathrm{q}}, \mathbf {d} _ {\mathrm{q}}) \\ \overline {{\mathbf {h}}} (\mathbf {x}) \end{array} \right]
$$

Consumers’ benefit

Equality constraints

$$
\mathbf {h} _ {\mathrm{p}} (\mathbf {x}, \mathbf {s} _ {\mathrm{p}}, \mathbf {d} _ {\mathrm{p}}) = \hat {\mathbf {h}} _ {\mathrm{p}} (\mathbf {x}) - \hat {\mathbf {s}} _ {\mathrm{p}} + \hat {\mathbf {d}} _ {\mathrm{p}}
$$

Real power flow equations

$$
\begin{array}{l} \mathbf {h} _ {\mathrm{q}} (\mathbf {x}, \mathbf {s} _ {\mathrm{q}}, \mathbf {d} _ {\mathrm{q}}) = \hat {\mathbf {h}} _ {\mathrm{q}} (\mathbf {x}) - \hat {\mathbf {s}} _ {\mathrm{q}} + \hat {\mathbf {d}} _ {\mathrm{q}} \\ \mathbf {g} (\mathbf {x}, \mathbf {s}, \mathbf {d}) = \left[ \begin{array}{c} \mathbf {s} _ {\min} - \mathbf {s} \\ \mathbf {s} - \mathbf {s} _ {\max} \\ \mathbf {d} _ {\min} - \mathbf {d} \\ \mathbf {d} - \mathbf {d} _ {\max} \\ \overline {{\mathbf {g}}} (\mathbf {x}) \end{array} \right] \\ \mathbf {f} (\mathbf {d}, \mathbf {p} _ {\mathrm{d}}) \\ L, \overline {{L}} \\ \boldsymbol {\lambda} = \left[ \begin{array}{c c c} \boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} & \boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} & \boldsymbol {\lambda} _ {\mathrm{f}} ^ {T} \end{array} \right] ^ {T} \\ \boldsymbol {\lambda} _ {\mathrm{h}} = \left[ \begin{array}{c c c} \boldsymbol {\lambda} _ {\hat {\mathrm{h}}} ^ {T} & \boldsymbol {\lambda} _ {\hat {\mathrm{h}}} ^ {T} \end{array} \right] ^ {T} = \left[ \begin{array}{c c c} \boldsymbol {\lambda} _ {\hat {\mathrm{hp}}} ^ {T} & \boldsymbol {\lambda} _ {\hat {\mathrm{hq}}} ^ {T} & \boldsymbol {\lambda} _ {\hat {\mathrm{h}}} ^ {T} \end{array} \right] ^ {T} \\ \boldsymbol {\lambda} _ {\mathrm{g}} = \left[ \begin{array}{c c c} \boldsymbol {\lambda} _ {\mathrm{gsmin}} ^ {T} & \boldsymbol {\lambda} _ {\mathrm{gsmax}} ^ {T} & \boldsymbol {\lambda} _ {\mathrm{gdmin}} ^ {T} & \boldsymbol {\lambda} _ {\mathrm{gdmax}} ^ {T} & \boldsymbol {\lambda} _ {\overline {{\mathrm{g}}}} ^ {T} \end{array} \right] ^ {T} \\ \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hs}}} = \left[ \begin{array}{c c c} \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hsp}}} ^ {T} & \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hsq}}} ^ {T} \end{array} \right] ^ {T} \\ \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} = \left[ \begin{array}{c c c} \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hdp}}} ^ {T} & \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hdq}}} ^ {T} \end{array} \right] ^ {T} \\ \tilde {\boldsymbol {\lambda}} _ {\mathrm{f}} = \left[ \begin{array}{c c c} \tilde {\boldsymbol {\lambda}} _ {\mathrm{fp}} ^ {T} & \tilde {\boldsymbol {\lambda}} _ {\mathrm{fq}} ^ {T} \end{array} \right] ^ {T} \\ p = [ p _ {\mathrm{s}} ^ {T}: p _ {\mathrm{d}} ^ {T} ] ^ {T} = [ p _ {\mathrm{sp}} ^ {T}: p _ {\mathrm{sq}} ^ {T}: p _ {\mathrm{dp}} ^ {T}: p _ {\mathrm{dq}} ^ {T} ] ^ {T} \\ D (p) \\ S (p) \end{array}
$$

Reactive power flow equations

Inequality constraints

Additional equation for consumer demand Lagrange functions Lagrange multiplier vector

Lagrange multiplier vector for power flow equations and other equality constraints

Lagrange multiplier vector for inequality constraints

Reduced Lagrange multiplier vector including only entries for power flow equations which include a supply of real or reactive power

Reduced Lagrange multiplier vector including only entries for power flow equations which include a demand of real or reactive power

Lagrange multiplier vector for additional constraints

Price vector for variable suppliers and variable consumers Ž . includes real and reactive prices

## 3. Traditional OPF formulation

For background, the traditional OPF with the objective of minimizing generation costs is described in this section of the paper. As mentioned in the introduction, the consumer demand is not typically a variable in this problem. In order for this development to match later equations, we will maximize the negative of the costs instead of minimizing the costs.

$$
\begin{array}{l} \max _ {\mathbf {s}, \mathbf {x}} - C (\mathbf {s}) \\ \mathbf {h} (\mathbf {x}, \mathbf {s}, \mathbf {d}) = \left[ \begin{array}{c} \hat {\mathbf {h}} (\mathbf {x}) - \hat {\mathbf {s}} + \hat {\mathbf {d}} \\ \overline {{\mathbf {h}}} (\mathbf {x}) \end{array} \right] = 0 \end{array}
$$

s.t .

$$
\mathbf {g} (\mathbf {x}, \mathbf {s}, \mathbf {d}) = \left[ \begin{array}{c} \mathbf {s} _ {\min} - \mathbf {s} \\ \mathbf {s} - \mathbf {s} _ {\max} \\ \mathbf {d} _ {\min} - \mathbf {d} \\ \mathbf {d} - \mathbf {d} _ {\max} \\ \overline {{\mathbf {g}}} (\mathbf {x}) \end{array} \right] \leq 0.\tag{3.1}
$$

To solve this nonlinear program, form the Lagrange function for it.

$$
\begin{array}{l} \overline {{L}} = - C (\mathbf {s}) + \boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} \mathbf {h} (\mathbf {x}, \mathbf {s}, \mathbf {d}) + \boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \mathbf {g} (\mathbf {x}, \mathbf {s}, \mathbf {d}) \\ \overline {{L}} = \left( \begin{array}{l} - C (\mathbf {s}) + \boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} \big [ \hat {\mathbf {h}} (\mathbf {x}) - \hat {\mathbf {s}} + \hat {\mathbf {d}} \big ] + \boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} \big [ \overline {{\mathbf {h}}} (\mathbf {x}) \big ] \\ + \boldsymbol {\lambda} _ {\mathrm{gsmin}} ^ {T} [ \mathbf {s} _ {\mathrm{min}} - \mathbf {s} ] + \boldsymbol {\lambda} _ {\mathrm{gsmax}} ^ {T} [ \mathbf {s} - \mathbf {s} _ {\mathrm{max}} ] \\ + \boldsymbol {\lambda} _ {\mathrm{gdmin}} ^ {T} [ \mathbf {d} _ {\mathrm{min}} - \mathbf {d} ] + \boldsymbol {\lambda} _ {\mathrm{gdmax}} ^ {T} [ \mathbf {d} - \mathbf {d} _ {\mathrm{max}} ] + \boldsymbol {\lambda} _ {\overline {{\mathbf {g}}}} ^ {T} \overline {{\mathbf {g}}} (\mathbf {x}) \end{array} \right). \end{array}\tag{3.2}
$$

The problem can then be determined by solving for the necessary Kuhn–Tucker conditions 6 : <sup>w</sup> <sup>x</sup>

Stationarity conditions:

$$
\begin{array}{l} \frac {\partial \overline {{L}}}{\partial \mathbf {x}} = \boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} \frac {\partial \mathbf {h} (\mathbf {x} , \mathbf {s} , \mathbf {d})}{\partial \mathbf {x}} + \boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \frac {\partial \mathbf {g} (\mathbf {x} , \mathbf {s} , \mathbf {d})}{\partial \mathbf {x}} = \mathbf {0} \\ \frac {\partial \overline {{L}}}{\partial \mathbf {s}} = - \frac {\partial C (\mathbf {s})}{\partial \mathbf {s}} - \tilde {\boldsymbol {\lambda}} _ {\mathrm{hs}} - \boldsymbol {\lambda} _ {\mathrm{gsmin}} + \boldsymbol {\lambda} _ {\mathrm{gsmax}} = 0 \\ \frac {\partial \overline {{L}}}{\partial \boldsymbol {\lambda} _ {\mathrm{h}}} = \mathbf {h} (\mathbf {x}, \mathbf {s}, \mathbf {d}) = 0 \end{array}\tag{3.3}
$$

Complimentary slackness conditions:

$$
\boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \mathbf {g} (\mathbf {x}, \mathbf {s}, \mathbf {d}) = 0; \quad \boldsymbol {\lambda} _ {\mathrm{g}} \geq 0.
$$

## 4. Maximizing social welfare

In order to maximize social welfare within a power system, the objective function for the OPF described in Section 3 need only be modified to include a consumer benefit function B dŽ .. This function models the benefit which the consumer gains by using the power and reactive power which they receive.

$$
\begin{array}{l} \max _ {\mathbf {x}, \mathbf {s}, \mathbf {d}} B (\mathbf {d}) - C (\mathbf {s}) \\ \mathbf {h} (\mathbf {x}, \mathbf {s}, \mathbf {d}) = \left[ \begin{array}{c} \hat {\mathbf {h}} (\mathbf {x}) - \hat {\mathbf {s}} + \hat {\mathbf {d}} \\ \overline {{\mathbf {h}}} (\mathbf {x}) \end{array} \right] = 0 \end{array}
$$

s.t .

$$
\mathbf {g} (\mathbf {x}, \mathbf {s}, \mathbf {d}) = \left[ \begin{array}{c} \mathbf {s} _ {\min} - \mathbf {s} \\ \mathbf {s} - \mathbf {s} _ {\max} \\ \mathbf {d} _ {\min} - \mathbf {d} \\ \mathbf {d} - \mathbf {d} _ {\max} \\ \overline {{\mathbf {g}}} (\mathbf {x}) \end{array} \right] \leq 0.\tag{4.1}
$$

Again, to solve this, form a Lagrange function as follows:

$$
\begin{array}{l} L = B (\mathbf {d}) - C (\mathbf {s}) + \boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} \mathbf {h} (\mathbf {x}, \mathbf {s}, \mathbf {d}) + \boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \mathbf {g} (\mathbf {x}, \mathbf {s}, \mathbf {d}) \\ L = \left( \begin{array}{l} B (\mathbf {d}) - C (\mathbf {s}) + \boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} \big [ \hat {\mathbf {h}} (\mathbf {x}) - \hat {\mathbf {s}} + \hat {\mathbf {d}} \big ] + \boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} \big [ \overline {{\mathbf {h}}} (\mathbf {x}) \big ] \\ + \boldsymbol {\lambda} _ {\mathrm{gsmin}} ^ {T} [ \mathbf {s} _ {\mathrm{min}} - \mathbf {s} ] + \boldsymbol {\lambda} _ {\mathrm{gsmax}} ^ {T} [ \mathbf {s} - \mathbf {s} _ {\mathrm{max}} ] \\ + \boldsymbol {\lambda} _ {\mathrm{gdmin}} ^ {T} [ \mathbf {d} _ {\mathrm{min}} - \mathbf {d} ] + \boldsymbol {\lambda} _ {\mathrm{gdmax}} ^ {T} [ \mathbf {d} - \mathbf {d} _ {\mathrm{max}} ] + \boldsymbol {\lambda} _ {\overline {{\mathrm{g}}}} ^ {T} \overline {{\mathbf {g}}} (\mathbf {x}) \end{array} \right). \end{array}\tag{4.2}
$$

The maximization problem can then be determined by solving for the necessary Kuhn–Tucker conditions:

$$
\begin{array}{l} \frac {\partial L}{\partial \mathbf {x}} = \boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} \frac {\partial \mathbf {h} (\mathbf {x} , \mathbf {s} , \mathbf {d})}{\partial \mathbf {x}} + \boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \frac {\partial \mathbf {g} (\mathbf {x} , \mathbf {s} , \mathbf {d})}{\partial \mathbf {x}} = 0 \\ \frac {\partial L}{\partial \mathbf {s}} = - \frac {\partial C (\mathbf {s})}{\partial \mathbf {s}} - \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hs}}} - \boldsymbol {\lambda} _ {\mathrm{gsmin}} + \boldsymbol {\lambda} _ {\mathrm{gsmax}} = 0 \\ \frac {\partial L}{\partial \mathbf {d}} = \frac {\partial B (\mathbf {d})}{\partial \mathbf {d}} + \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} - \boldsymbol {\lambda} _ {\mathrm{gdmin}} + \boldsymbol {\lambda} _ {\mathrm{gdmax}} = 0 \\ \frac {\partial L}{\partial \boldsymbol {\lambda} _ {\mathrm{h}}} = \mathbf {h} (\mathbf {x}, \mathbf {s}, \mathbf {d}) = 0 \\ \boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \mathbf {g} (\mathbf {x}, \mathbf {s}, \mathbf {d}) = 0; \quad \boldsymbol {\lambda} _ {\mathrm{g}} \geq 0. \end{array}\tag{4.3}
$$

The solution to Eq. 4.3 would then constitute a maximization of the social welfare for a power market.Ž .

## 5. Alternative approach—price-dependent load models

Because many people already have an OPF algorithm with the objective of minimizing generation costs in the system, it is of interest to incorporate the maximization of social welfare into this OPF in the simplest manner possible. To do this, consider the difference between the necessary conditions described in Eq. 3.3Ž . with those of Eq. 4.3 . The only difference is the condition:Ž .

$$
\frac {\partial B (\mathbf {d})}{\partial \mathbf {d}} = - \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} + \boldsymbol {\lambda} _ {\mathrm{gdmin}} - \boldsymbol {\lambda} _ {\mathrm{gdmax}} = 0.\tag{5.1}
$$

Instead of enforcing this condition, consider defining the function $\mathbf { D } ( \mathbf { p } _ { \mathrm { d } } )$ as the functional inverse of $( \partial B ( { \bf d } ) ) / ( \partial { \bf d } )$ , meaning that for all $\mathbf { p _ { \mathrm { d } } }$ and d the following hold:

$$
\frac {\partial B (\mathbf {D} (\mathbf {p} _ {\mathrm{d}}))}{\partial \mathbf {d}} = \mathbf {p} _ {\mathrm{d}} \text {   and   } \mathbf {D} \left(\frac {\partial B (\mathbf {d})}{\partial \mathbf {d}}\right) = \mathbf {d}.\tag{5.2}
$$

After studying Eq. 5.2 , one realizes that enforcing the condition of Eq. 5.1 is equivalent to enforcing the Ž . Ž . condition of Eq. 5.3 :Ž .

$$
\mathbf {d} = \left(\frac {\partial B (\mathbf {d})}{\partial \mathbf {d}}\right) ^ {- 1} = \mathbf {D} \left(- \tilde {\lambda} _ {\hat {\mathrm{hd}}} + \boldsymbol {\lambda} _ {\mathrm{gdmin}} - \boldsymbol {\lambda} _ {\mathrm{gdmax}}\right).\tag{5.3}
$$

Eq. 5.3 is what we call the price-dependent load model.Ž .

Therefore, in order to solve the maximization of social welfare, simply take the traditional OPF which enforces the conditions of minimizing costs of Eq. 3.3 and add to it the condition of Eq. 5.3 . In order to Ž . Ž .

simplify this more, simply substitute Eq. 5.3 back into Eq. 3.3 anywhere Ž . Ž . d appears. This results in the necessary conditions of Eq. 5.4 : Ž .

$$
\begin{array}{l} \left( \begin{array}{c} \boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} \frac {\partial \mathbf {h} \big (\mathbf {x} , \mathbf {s} , \mathbf {D} \big (- \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} + \boldsymbol {\lambda} _ {\mathrm{gdmin}} - \boldsymbol {\lambda} _ {\mathrm{gdmax}} \big) \big)}{\partial \mathbf {x}} \\ + \boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \frac {\partial \mathbf {g} \big (\mathbf {x} , \mathbf {s} , \mathbf {D} \big (- \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} + \boldsymbol {\lambda} _ {\mathrm{gdmin}} - \boldsymbol {\lambda} _ {\mathrm{gdmax}} \big) \big)}{\partial \mathbf {x}} \end{array} \right) = 0 \\ - \frac {\partial C (\mathbf {s})}{\partial \mathbf {s}} - \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hs}}} - \boldsymbol {\lambda} _ {\mathrm{gsmin}} + \boldsymbol {\lambda} _ {\mathrm{gsmax}} = 0 \\ \mathbf {h} \Big (\mathbf {x}, \mathbf {s}, \mathbf {D} \Big (- \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} + \boldsymbol {\lambda} _ {\mathrm{gdmin}} - \boldsymbol {\lambda} _ {\mathrm{gdmax}} \Big) \Big) = 0 \\ \boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \mathbf {g} \Big (\mathbf {x}, \mathbf {s}, \mathbf {D} \Big (- \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} + \boldsymbol {\lambda} _ {\mathrm{gdmin}} - \boldsymbol {\lambda} _ {\mathrm{gdmax}} \Big) \Big) = 0 \\ \boldsymbol {\lambda} _ {\mathrm{g}} \geq 0. \end{array}\tag{5.4}
$$

## 6. Consumer demand function

## 6.1. Real power benefit function

As shown in Section 5, the price-dependent load model is based on the existence of a consumer benefit Ž . function, B d , where d includes both the real and reactive power demand: $\mathbf { d } = [ \mathbf { d } _ { \mathrm { p } } ^ { T } \ \mathbf { d } _ { \mathrm { q } } ^ { T } ] ^ { T }$

The consumer demand in our development is a function of the price paid at the node: $\mathbf { d } = \mathbf { D } ( \mathbf { p } )$ . This demand function is the inverse of Ž Ž .. Ž . B d <sup>r</sup> d . For a more intuitive feel of what this means, consider the sample plots of consumer benefit for real power shown in Fig. 1.

It is important to assume that the consumer benefit function, B, be concave and increasing in order to help insure only one social welfare maximum exists ignoring the convexity of the constraints . These are goodŽ . assumptions however. Presumably, the consumer always gains some benefit from more consumption therefore the benefit increases. Even if the consumer does not gain more benefit, he will be able to resell the power on the market. The concavity assumption is valid because an intelligent consumer will always give energy to her most beneficial processes first thereby making the marginal benefit for lower consumption larger.

At the optimal solution from the social welfare perspective, $( \partial B ( { \bf d } ) ) / ( \partial { \bf d } )$ will be the price for each consumer. Thus by taking the inverse of the, the consumer demand function for only real power will be as shown in Fig. 2.

This consumer demand function is what must be substituted as part of Eq. 5.3 in order to produce the socialŽ . welfare maximum.

![](/api/attachments/YXS3ZANA/fulltext/images/c94935ee6e29cccaf970ab70c5c71779f862c56a70655aace4341af9ea583bc5.jpg)  
Fig. 1. Consumer benefit and derivative of benefit.

![](/api/attachments/YXS3ZANA/fulltext/images/6c80893786b79ca2f8fc59718245fa9bd6e1e964c4a461d95276dc289acf0971.jpg)  
Fig. 2. Consumer demand for real power.

The point $( p _ { \mathrm { b a s e } } , d _ { \mathrm { b a s e } } )$ and the slope $m _ { \mathrm { p r i c e } }$ will specify the line. Therefore the consumer demand function will be:

$$
\mathbf {D} _ {\mathrm{p}} \left(\mathbf {p} _ {\mathrm{p}}\right) = \left(\mathbf {d} _ {\text { p   b   a   s   e }} + \mathbf {M} _ {\text { p   r   i   c   e }} \mathbf {p} _ {\text { p   b   a   s   e }}\right) - \mathbf {M} _ {\text { p   r   i   c   e }} \mathbf {p} _ {\mathrm{p}},\tag{6.1}
$$

where $\mathbf { M } _ { \mathrm { { p r i c e } } }$ is a diagonal matrix with entries $m _ { \mathrm { p r i c e } } .$ Ignoring reactive power consumption completely, this demand function corresponds to a quadratic consumer benefit function for real power as shown in Eq. 6.2 : Ž .

$$
B _ {\mathrm{p}} \left(\mathbf {d} _ {\mathrm{p}}\right) = \mathbf {d} _ {\mathrm{p}} ^ {T} \left(\mathbf {M} _ {\text { p   r   i   c   e }} ^ {- 1} \mathbf {d} _ {\text { p   b   a   s   e }} + \mathbf {p} _ {\text { p   b   a   s   e }}\right) - \frac {1}{2} \mathbf {d} _ {\mathrm{p}} ^ {T} \mathbf {M} _ {\text { p   r   i   c   e }} ^ {- 1} \mathbf {d} _ {\mathrm{p}}.\tag{6.2}
$$

## 6.2. ReactiÕe power benefit function

While many are comfortable with the idea of a spot market for real power, the viability of a spot market for reactive power remains cloudy. In Ref. 5 , the creation of a full spot market for reactive power is put forth. While this does help create an efficient market for allocating the operational costs of the reactive power supply, it does not overcome two large issues in the reactive power market: the capital costs of reactive power equipment such as capacitor banks andŽ $\mathrm { L T C } ^ { \prime } \mathrm { s } )$ are large compared to operational costs and reactive power spot prices are extremely volatile. For example, in Refs. 3,11 , reactive power spot prices are shown to vary by<sup>w</sup> <sup>x</sup> orders of magnitude when voltage limits are encountered in the power system.

In order to overcome these issues, Refs. 3,4 propose the development of pricing schemes which take into<sup>w</sup> <sup>x</sup> account the capital investment required to install reactive power equipment along with alternatives which try to overcome some of the price volatility in reactive power spot prices.

Although there is still some debate regarding the viability of reactive power spot prices, a portion of any pricing scheme will likely be based on the spot pricing approach. The section investigates how to incorporate this idea into the price-dependent load model.

In order to incorporate the simulation of a reactive power market through price-dependent reactive loads, it is necessary to determine a benefit function that befits the benefits gained by reactive power consumption. This reactive benefit function should not follow the same mold as the real power benefit equation because reactive power really acts more as a service which enables the consumption of real power.

Using this point of view, consider the benefit of the reactive power as the avoidance of moving the reactive power from some desired level for a given power consumption. Define a desired reactive power demand as a function of the real power demand: $d _ { \mathrm { q d e s i r e d } } = f ( d _ { \mathrm { p } } )$ . This desired reactive demand will be the demand which the load will naturally require at the given load level. Also assume that the magnitude of the function increases with $d _ { \mathfrak { p } } .$ . Now consider a concave function, $k ( x )$ , which has a maximum value of zero at zero such as in Fig. 3.

![](/api/attachments/YXS3ZANA/fulltext/images/974fdecab88df4cfbb66b14d9d92fa2390bc2f688d5623c405f73621d9a8fd68.jpg)  
Fig. 3. Concave k xŽ ..

Then using $d _ { \mathrm { q d e s i r e d } } = f ( d _ { \mathrm { p } } )$ Ž . along with the function k x , construct the reactive power benefit function for an individual load is as in Eq. 6.3 :Ž .

$$
B _ {\mathrm{q}} \big (d _ {\mathrm{p}}, d _ {\mathrm{q}} \big) = B _ {\mathrm{q0}} k \big (d _ {\mathrm{q}} - f \big (d _ {\mathrm{p}} \big) \big).\tag{6.3}
$$

Due to the properties specified for k xŽ ., this benefit has a maximum value of zero which is achieved when the reactive power demand is equal to the desired reactive demand, $f ( d _ { \mathfrak { p } } )$ . The benefit decreases on both sides of this value because the consumer must provide their own reactive power support using power electronics, capacitive<sup>r</sup>inductor support, etc. One can envision a system load with a filtering device such as that seen in Fig. 4.

The model here assumes that the cost of operating this filtering device is equal to zero when it is performing no filtering, i.e., when $d _ { \mathrm { q } } = f ( d _ { \mathrm { p } } )$ Ž . and increases, according to k x , as it moves away from that point.

Incorporating Eq. 6.3 into the total consumer benefit results in a function of both the real and reactiveŽ . demand:

$$
B \big (\mathbf {d} _ {\mathrm{p}}, \mathbf {d} _ {\mathrm{q}} \big) = \sum_ {\text { all   consumers }} \Big (B _ {\mathrm{p}} \big (d _ {\mathrm{p}} \big) + B _ {\mathrm{q}} \big (d _ {\mathrm{p}}, d _ {\mathrm{q}} \big) \Big).\tag{6.4}
$$

The consumer demand function can then be calculated from Eq. 6.4 by determining the functional inverse ofŽ . the derivative of this consumer benefit function.

![](/api/attachments/YXS3ZANA/fulltext/images/83e1dd20e94e59e43e1e5324fb770ba43ac63e6fd9639fb26a18e29dfcb21828.jpg)  
Fig. 4. The load model with reactive control.

## 7. Example demand function for real and reactive power

As an example, consider using the quadratic real power benefit function for each consumer of the form $B _ { \mathrm { p } } ( d _ { \mathrm { p } } ) = a d _ { \mathrm { p } } - b d _ { \mathrm { p } } ^ { 2 }$ . This is the same form as Eq. 6.2 . For the reactive power benefit function, useŽ . $\dot { d _ { \mathrm { q d e s i r e d } } } = f ( \dot { d } _ { \mathrm { p } } ) = \dot { \gamma } d _ { \mathrm { p } }$ and $k ( x ) = - x ^ { 2 }$ . This corresponds to a constant power factor load where $= \surd 1 - \mathrm { p f } ^ { 2 } / \mathrm { p f }$ and the cost of compensating for reactive power by the consumer increases quadratically as it moves away from constant power factor. Thus, the consumer benefit function is Eq. 7.1 :Ž .

$$
B \left(d _ {\mathrm{p}}, d _ {\mathrm{q}}\right) = a d _ {\mathrm{p}} - b d _ {\mathrm{p}} ^ {2} - B _ {\mathrm{qo}} \left[ d _ {\mathrm{q}} - \gamma d _ {\mathrm{p}} \right] ^ {2} = a d _ {\mathrm{p}} + \left(- b - B _ {\mathrm{qo}} \gamma^ {2}\right) d _ {\mathrm{p}} ^ {2} - B _ {\mathrm{qo}} d _ {\mathrm{q}} ^ {2} + 2 B _ {\mathrm{qo}} \gamma d _ {\mathrm{p}} d _ {\mathrm{q}}.\tag{7.1}
$$

It should be noted that Eq. 7.1 is simply the summation of two concave functions and is therefore itself Ž . concave.

Now it is of interest to determine the consumer demand functions that result by calculating the functional inverse of the derivative of the consumer demand function. The derivative with respect to the real power demand is shown in Eq. 7.2 :Ž .

$$
\frac {\partial B \left(d _ {\mathrm{p}} , d _ {\mathrm{q}}\right)}{\partial d _ {\mathrm{p}}} = \frac {\partial B _ {\mathrm{p}} \left(d _ {\mathrm{p}}\right)}{\partial d _ {\mathrm{p}}} + \frac {\partial B _ {\mathrm{q}} \left(d _ {\mathrm{p}} , d _ {\mathrm{q}}\right)}{\partial d _ {\mathrm{p}}} = [ a - 2 b d _ {\mathrm{p}} ] + [ 2 B _ {\mathrm{qo}} \gamma (- \gamma d _ {\mathrm{p}} + d _ {\mathrm{q}}) ].\tag{7.2}
$$

In looking at the derivative of the consumer benefit function with respect to real power demand, it is normally expected that this derivative always be positive because some marginal benefit is expected from increased consumption. However, because of the model that is being proposed, this will not always be true.

One possibility is that $( \partial B _ { \mathrm { p } } ( d _ { \mathrm { p } } ) ) / ( \partial d _ { \mathrm { p } } )$ is negative. This is an artifact of using the model outside the range intended. The benefit model for real power should be concave and increasing. The quadratic function is concave, but will begin decreasing once the maximum point is reaching. It is therefore important that the real power load for a consumer be limited to the range in which the function $a - 2 b d _ { \mathrm { p } }$ is positive. Otherwise, the consumer gets more benefit by decreasing power consumption regardless of any other costs. This would not make sense as the consumer could always resell the power and thereby get some use.

The other possibility is that $( \partial B _ { \mathrm { q } } ( d _ { \mathrm { p } } , d _ { \mathrm { q } } ) ) / ( \partial d _ { \mathrm { p } } )$ be negative and begin to dominate the first term. This is not unrealistic. It would merely mean that further increases in real power would result in large costs for reactive power consumption and therefore reduce the consumer benefit.

Now consider taking the derivative with respect to reactive power demand:

$$
\frac {\partial B \left(d _ {\mathrm{p}} , d _ {\mathrm{q}}\right)}{\partial d _ {\mathrm{q}}} = 2 B _ {\mathrm{q0}} \left(- d _ {\mathrm{q}} + \gamma d _ {\mathrm{p}}\right).\tag{7.3}
$$

Eq. 7.3 shows that in order to increase benefit, the reactive power demand is always pushed toward the Ž . desired level $\gamma d _ { \mathrm { p } }$

In order to determine the consumer demand function, equate Eqs. 7.2 and 7.3 to the price of real andŽ . Ž . reactive power, respectively:

$$
\frac {\partial B \big (d _ {\mathrm{p}} , d _ {\mathrm{q}} \big)}{\partial \mathbf {d}} = \left[ \begin{array}{c} a \\ 0 \end{array} \right] + \left[ \begin{array}{c c} - 2 b - 2 B _ {\mathrm{qo}} \gamma^ {2} & 2 B _ {\mathrm{qo}} \gamma \\ 2 B _ {\mathrm{qo}} \gamma & - 2 B _ {\mathrm{qo}} \end{array} \right] \left[ \begin{array}{c} d _ {\mathrm{p}} \\ d _ {\mathrm{q}} \end{array} \right] = \left[ \begin{array}{c} p _ {\mathrm{p}} \\ p _ {\mathrm{q}} \end{array} \right].\tag{7.4}
$$

Then solve for real and reactive demand in terms of these prices, i.e. determine the functional inverse.

$$
\mathbf {D} (\mathbf {p}) = \left[ \begin{array}{c} - \frac {1}{2 b} \left(p _ {\mathrm{p}} + \gamma p _ {\mathrm{q}}\right) + \frac {a}{2 b} \\ \gamma \left(- \frac {1}{2 b} \left(p _ {\mathrm{p}} + \gamma p _ {\mathrm{q}}\right) + \frac {a}{2 b}\right) - \frac {1}{2 B _ {\mathrm{q0}}} p _ {\mathrm{q}} \end{array} \right].\tag{7.5}
$$

Note:

$$
d _ {\mathrm{q}} = \gamma d _ {\mathrm{p}} - \frac {1}{2 B _ {\mathrm{q0}}} p _ {\mathrm{q}}
$$

It is helpful to rewrite this additional equation in a more meaningful way. Eq. 7.5 can be rewritten asŽ . follows:

$$
\mathbf {D} (\mathbf {p}) = \left[ \begin{array}{l} d _ {\text {pbase}} + m _ {\mathrm{p}} p _ {\text {pbase}} \\ d _ {\text {qbase}} + \gamma m _ {\mathrm{p}} p _ {\text {pbase}} \end{array} \right] - \left[ \begin{array}{c c} m _ {\mathrm{p}} & \gamma m _ {\mathrm{p}} \\ \gamma m _ {\mathrm{p}} & \left(\gamma^ {2} m _ {\mathrm{p}} + \frac {d _ {\text {qbase}}}{2 \overline {{B _ {\mathrm{qo}}}}}\right) \end{array} \right] \left[ \begin{array}{l} p _ {\mathrm{p}} \\ p _ {\mathrm{q}} \end{array} \right]\tag{7.6}
$$

with the following definitions:

$$
m _ {\mathrm{p}} = \frac {1}{2 b} \quad \gamma = \frac {d _ {\mathrm{qbase}}}{d _ {\mathrm{pbase}}} \quad B _ {\mathrm{qo}} = \frac {\overline {{B _ {\mathrm{qo}}}}}{d _ {\mathrm{qbase}}}
$$

and one demand point of $d _ { \mathrm { p } } = d _ { \mathrm { p b a s e } }$ and $d _ { \mathrm { q } } = d _ { \mathrm { q b a s e } }$ at prices $p _ { \mathrm { p } } = p _ { \mathrm { p b a s e } }$ and $p _ { \mathrm { q } } = 0$ given.Eq. 7.6 can also beŽ . written in the form:

$$
\begin{array}{l} d _ {\mathrm{p}} = \left(d _ {\mathrm{pbase}} + m _ {\mathrm{p}} p _ {\mathrm{pbase}}\right) - m _ {\mathrm{p}} (p _ {\mathrm{p}} + \gamma p _ {\mathrm{q}}) \\ d _ {\mathrm{q}} = \gamma d _ {\mathrm{p}} - \frac {d _ {\mathrm{qbase}}}{2 \overline {{B _ {\mathrm{q0}}}}} p _ {\mathrm{q}}. \end{array}\tag{7.7}
$$

Now, at each demand bus specify a value of $m _ { \mathrm { p } } , p _ { \mathrm { p b a s e } } , \overline { { B _ { \mathrm { q o } } } } , d _ { \mathrm { p h a s e } }$ , and $d _ { \mathrm { q b a s e } }$ and substitute:

$$
\mathbf {D} _ {\text {busk}} \left(\left[ \begin{array}{l} \boldsymbol {\lambda} _ {\hat {\mathrm{hdp}}} + \boldsymbol {\lambda} _ {\mathrm{gdpmin}} - \boldsymbol {\lambda} _ {\mathrm{gdpmax}} \\ \boldsymbol {\lambda} _ {\hat {\mathrm{hdq}}} + \boldsymbol {\lambda} _ {\mathrm{gdqmin}} - \boldsymbol {\lambda} _ {\mathrm{gdqmax}} \end{array} \right]\right) = \left[ \begin{array}{l} d _ {\text {pbase}} + m _ {\mathrm{p}} p _ {\text {pbase}} \\ d _ {\text {qbase}} + \gamma m _ {\mathrm{p}} p _ {\text {pbase}} \end{array} \right] - \left[ \begin{array}{c c} m _ {\mathrm{p}} & \gamma m _ {\mathrm{p}} \\ \gamma m _ {\mathrm{p}} & \left(\gamma^ {2} m _ {\mathrm{p}} + \frac {d _ {\text {qbase}}}{2 B _ {\mathrm{qo}}}\right) \end{array} \right]
$$

$$
\times \left[ \begin{array}{c} \boldsymbol {\lambda} _ {\hat {\mathrm{hdp}}} + \boldsymbol {\lambda} _ {\mathrm{gdpmin}} - \boldsymbol {\lambda} _ {\mathrm{gdpmax}} \\ \boldsymbol {\lambda} _ {\hat {\mathrm{hdq}}} + \boldsymbol {\lambda} _ {\mathrm{gdqmin}} - \boldsymbol {\lambda} _ {\mathrm{gdqmax}} \end{array} \right]\tag{7.8}
$$

into the OPF necessary conditions shown in Eq. 5.4 . This will result in the social welfare maximum for theŽ . economic load model that has been described.

If you are interested in simulating only a real power market without the reactive power market, then you may simply ignore the price dependence of reactive power demand and assume that the load always maintains constant power factor. This results in the following load model:

$$
\begin{array}{l} d _ {\mathrm{p}} = \left(d _ {\mathrm{pbase}} + m _ {\mathrm{p}} p _ {\mathrm{pbase}}\right) - m _ {\mathrm{p}} p _ {\mathrm{p}} \\ d _ {\mathrm{q}} = \gamma d _ {\mathrm{p}} \end{array} .\tag{7.9}
$$

## 8. Implementation of real and reactive price-dependent loads into the OPF

This section will study how the consumer demand function of Eq. 5.4 effects the calculations of theŽ . Newton’s method algorithm.

It is first noted that after taking derivatives of h and g with respect to x, no dependence on s or d is found asŽ long as s and d are not functions of x, which we have assumed in this paper . Note: in the future, it may make. sense to write the consumer benefit as a function of voltage, which would make d dependent on x. For now however, the choice of the consumer demand function has no effect on the first equation. The only influence comes in the third and fourth equations. The consumer demand function has only changed the demand function from a constant to one dependent on the Lagrange multipliers $\tilde { \lambda } _ { \mathrm { \hat { h } d } } , \ \lambda _ { \mathrm { g d m i n } }$ and $\pmb { \lambda } _ { \mathrm { g d m a x } }$ . This will not impede the OPF algorithm as it will only require a simple function evaluation.

In using Newton’s method to solve these nonlinear equations, derivatives of the equations must be determined in order to calculate a Hessian matrix. In order to evaluate how the consumer demand function will effect these equations take the derivatives of the third and fourth equations with respect to $\tilde { \lambda } _ { \mathrm { \hat { h } d } } , \ \lambda _ { \mathrm { g d m i n } }$ and $\pmb { \lambda } _ { \mathrm { g d } \operatorname* { m a x } }$

$$
\begin{array}{l} \frac {\partial \mathbf {h} (\mathbf {x} , \mathbf {s} , \mathbf {D})}{\partial \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}}} = \frac {\partial \left[ \begin{array}{c} \hat {\mathbf {h}} (\mathbf {x}) - \hat {\mathbf {s}} + \hat {\mathbf {d}} \\ \overline {{\mathbf {h}}} (\mathbf {x}) \end{array} \right]}{\partial \mathbf {d}} \frac {\partial \mathbf {D}}{\partial \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}}} = - \left[ \hat {\mathbf {I}} _ {\mathrm{PQ}} \right] \left[ - \hat {\mathbf {M}} _ {\mathrm{PQprice}} \right], \\ \frac {\partial \mathbf {h} (\mathbf {x} , \mathbf {s} , \mathbf {D})}{\partial \boldsymbol {\lambda} _ {\mathrm{gdmin}}} = \frac {\partial \left[ \begin{array}{c} \hat {\mathbf {h}} (\mathbf {x}) - \hat {\mathbf {s}} + \hat {\mathbf {d}} \\ \overline {{\mathbf {h}}} (\mathbf {x}) \end{array} \right]}{\partial \mathbf {d}} \frac {\partial \mathbf {D}}{\partial \boldsymbol {\lambda} _ {\mathrm{gdmin}}} = + \left[ \hat {\mathbf {I}} _ {\mathrm{PQ}} \right] \left[ - \tilde {\mathbf {M}} _ {\mathrm{PQprice}} \right], \\ \frac {\partial \mathbf {h} (\mathbf {x} , \mathbf {s} , \mathbf {D})}{\partial \boldsymbol {\lambda} _ {\mathrm{gdmax}}} = \frac {\partial \left[ \begin{array}{c} \hat {\mathbf {h}} (\mathbf {x}) - \hat {\mathbf {s}} + \hat {\mathbf {d}} \\ \overline {{\mathbf {h}}} (\mathbf {x}) \end{array} \right]}{\partial \mathbf {d}} \frac {\partial \mathbf {D}}{\partial \boldsymbol {\lambda} ^ {\mathrm{gdmax}}} = - \left[ \hat {\mathbf {I}} _ {\mathrm{PQ}} \right] \left[ - \overline {{\mathbf {M}}} _ {\mathrm{PQprice}} \right], \\ \frac {\partial \mathbf {g} (\mathbf {x} , \mathbf {s} , \mathbf {D})}{\partial \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}}} = \frac {\partial \left[ \begin{array}{c} s _ {\min} - s \\ s - s _ {\max} \\ d _ {\min} - d \\ d - d _ {\max} \\ g (x) \end{array} \right]}{\partial D} \frac {\partial D}{\partial \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}}} = + [ \tilde {\mathbf {I}} _ {\mathrm{PQ}} ] [ - \hat {\mathbf {M}} _ {\mathrm{PQprice}} ], \\ \frac {\partial g (\mathbf {x} , s , D)}{\partial \boldsymbol {\lambda} _ {\mathrm{gdmin}}} = + [ \tilde {\mathbf {I}} _ {\mathrm{PQ}} ] [ \tilde {\mathbf {M}} _ {\mathrm{PQprice}} ], \\ \frac {\partial g (\mathbf {x} , s , D)}{\partial \boldsymbol {\lambda} _ {\mathrm{gdmax}}} = + [ \tilde {\mathbf {I}} _ {\mathrm{PQ}} ] [ - \overline {{\mathbf {M}}} _ {\mathrm{PQprice}} ], \end{array}
$$

where the variables are defined as $\hat { \mathbf { I } } _ { \mathrm { P Q } } =$ matrix with diagonal entries of one corresponding to consumer demand variables d, $\hat { \mathbf { I } } _ { \mathrm { P Q } } =$ matrix with diagonal entries of one to consumer demands d which are at a limit, a block diagonal matrix with $2 \times 2$ entries of:

$$
\hat {\mathbf {M}} _ {\mathrm{PQprice}} = \left[ \begin{array}{c c} m _ {\mathrm{p}} & \gamma m _ {\mathrm{p}} \\ \gamma m _ {\mathrm{p}} & \left(\gamma^ {2} m _ {\mathrm{p}} + \frac {\mathbf {d} _ {\mathrm{qbase}}}{2 \overline {{B}} _ {\mathrm{qo}}}\right) \end{array} \right]
$$

corresponding to variables d, a block diagonal matrix with $2 \times 2$ entries of:

$$
\tilde {\mathbf {M}} _ {\mathrm{PQprice}} = \left[ \begin{array}{c c c} m _ {\mathrm{p}} & \gamma m _ {\mathrm{p}} \\ \gamma m _ {\mathrm{p}} & \left(\gamma^ {2} m _ {\mathrm{p}} + \frac {\mathbf {d} _ {\mathrm{qbase}}}{2 \overline {{B _ {\mathrm{qo}}}}}\right) \end{array} \right]
$$

corresponding to variables $\pmb { \lambda } _ { \mathrm { g d \ m i n } }$ related to d, a block diagonal matrix with $2 \times 2$ entries of:

$$
\overline {{\mathbf {M}}} _ {\mathrm{PQprice}} = \left[ \begin{array}{c c} m _ {\mathrm{p}} & \gamma m _ {\mathrm{p}} \\ \gamma m _ {\mathrm{p}} & \left(\gamma^ {2} m _ {\mathrm{p}} + \frac {\mathbf {d} _ {\mathrm{qbase}}}{2 \overline {{B _ {\mathrm{qo}}}}}\right) \end{array} \right]
$$

corresponding to variables $\pmb { \lambda } _ { \mathrm { g d \ m i n } }$ related to d.

The key point to recognize is that the effect of the additional price-dependent equations on the Hessian matrix is limited to small $2 \times 2$ block diagonal entries. From Eq. 7 of Ref. 10 , the Hessian matrix for the<sup>w</sup> <sup>x</sup> coupled OPF formulation is shown to have the structure in Eq. 8.1 :Ž .

$$
\mathbf {W} = \left[ \begin{array}{c c} \mathbf {H} & - \mathbf {J} ^ {T} \\ - \mathbf {J} & 0 \end{array} \right].\tag{8.1}
$$

The block diagonal entries which are added to the Hessian by the price-dependent loads will be in the zero matrix in the lower right partition. Because some entries are added on the off-diagonals in this zero matrix, it is possible that some degradation of sparsity may occur, however it will be minor. If one is only interested in simulating the real power market using the price-dependent load of Eq. 7.9 , theŽ . $2 \times 2$ block diagonals will be replaced by purely elements on the diagonal. This will ensure that no degradation of sparsity will occur.

Although some minor degradation of sparsity is possible, overall, it is expected that the price-dependent load will help with convergence of the OPF. This is because the loads in the system will tend to decrease if the system moves close to a limit due to the price increasing.

![](/api/attachments/YXS3ZANA/fulltext/images/1190cfaf50d2e42605f18cab3d062e6e8e7a526f588bb6fde48b6fabb5d8a293.jpg)  
Fig. 5. Hessian for minimizing costs.

![](/api/attachments/YXS3ZANA/fulltext/images/d43a1b6b95ca85be798fdf98cf941ef0485c53ff77c8fd9bf5b2a5f63c567818.jpg)  
Fig. 6. Hessian matrix for IEEE 118-bus system after adding price-dependent real power loads.

As a demonstration of how these models effect the Hessian matrix, study Figs. 5 and 6. They show Hessian matrices for the IEEE 118-bus system with cost data created following the premise that larger units are general cheaper units. Fig. 5 shows the Hessian matrix for the objective of minimizing total generation costs. Notice the large zero partition in the lower right. Fig. 6 shows the Hessian matrix with price-dependent real power loads included. Notice that new elements are only added along the diagonal of the zero partition. Also note that with both real and reactive price-dependent loads included, 2<sup>=</sup>2 blocks would appear along the diagonal of the Hessian matrix.

## 9. Application to a real power spot market

## 9.1. Showing general ideas

The OPF modifications as discussed in Section 8 were implemented into the PowerWorlde OPF that minimizes fuel costs 7 . As a case for comparison purposes, Fig. 7 shows a small six-bus system that has been <sup>w</sup> <sup>x</sup> optimized to minimize fuel costs.

![](/api/attachments/YXS3ZANA/fulltext/images/6eb667aec8e6171432f10e749255ce9d90c44925e17416473390a8199c5d453a.jpg)  
Fig. 7. Six-bus system with fuel costs minimized.

![](/api/attachments/YXS3ZANA/fulltext/images/e96b557f74b9ead58388ef8fbbb88592a0abde488c4917dbf8e09da2f013dd45.jpg)  
Fig. 8. Six-bus system maximizing social welfare.

The costs curves for the generators shown in Fig. 7 are:

$$
C \left(P _ {\mathrm{Gq}}\right) = \left(1 0 5 + 1 2 P _ {\mathrm{G} 1} + 0. 0 1 2 P _ {\mathrm{G} 1} ^ {2}\right) \times \text { FuelCost1 }
$$

$$
C \left(P _ {\mathrm{G} 2}\right) = \left(9 6 + 9. 6 P _ {\mathrm{G} 2} + 0. 0 0 9 6 P _ {\mathrm{G} 2} ^ {2}\right) \times \text { FuelCost2 }
$$

$$
C \left(P _ {\mathrm{G} 3}\right) = \left(1 0 5 + 1 3 P _ {\mathrm{G} 1} + 0. 0 1 3 P _ {\mathrm{G} 3} ^ {2}\right) \times \text { FuelCost3 }
$$

$$
C \left(P _ {\mathrm{Gq}}\right) = \left(9 4 + 9. 4 P _ {\mathrm{G} 1} + 0. 0 0 9 4 P _ {\mathrm{G} 4} ^ {2}\right) \times \text { FuelCost4 }
$$

with FuelCost X<sup>s</sup>US\$1.00<sup>r</sup>BTU for all generators.

Following Eq. 7.9 , the system was then optimized to maximize social welfare by implementing aŽ . price-dependent real power demand curve at each bus of:

$$
d _ {\mathrm{p}} \left(p _ {\mathrm{p}}\right) = d _ {\text { p   b   a   s   e }} \left(1 + \frac {m _ {\text { p   r   i   c   e }}}{d _ {\text { p   b   a   s   e }}} \left(p _ {\text { p   b   a   s   e }} - p _ {\mathrm{p}}\right)\right) = d _ {\text { p   b   a   s   e }} \left(1 + 1 0 \left(2 0 - p _ {\mathrm{p}}\right)\right)
$$

with $d _ { \mathrm { p b a s e } }$ equal to the base demand for the bus. In this example, $d _ { \mathrm { p b a s e } } = 1 0 0 \ \mathrm { M W }$ for each load as shown in Fig. 7. This price model means the loads will consume their $d _ { \mathrm { p b a s e } }$ if the spot price is $p _ { \mathrm { p } } = 2 0 ~ \mathrm { U S \Phi / M W H }$ . If the spot price falls below US\$20<sup>r</sup>MWH the loads will begin to consume more power, while if the spot price increases the loads will respond by consuming less. This sensitivity to price is encapsulated in the term $m _ { \mathrm { p r i c e } } / d _ { \mathrm { p b a s e } }$ that determines the slope of the demand function given in Fig. 2. This optimization yields the results shown in Fig. 8.

![](/api/attachments/YXS3ZANA/fulltext/images/7e09cef1b8a1e926598e260273271c90f9ecf056c82decd3c2de006d24c4d718.jpg)  
Fig. 9. Line limit has been decreased to 40 MVA.

![](/api/attachments/YXS3ZANA/fulltext/images/fc4ae8e4b7377bb81dbf93a77e39c55a6044b5a032bc8e643f167de4255128a6.jpg)  
Fig. 10. Fuel costs increased by 50%.

It should be noticed that in Fig. 8, the spot prices are all below US\$20<sup>r</sup>MWH causing the loads to converge more than their $d _ { \mathrm { p b a s e } }$ of 100 MW. It should also be noticed that while in Fig. 7 the load at every bus was 100 MW, the loads are varied in Fig. 8 with the smaller loads at buses with larger marginal costs. These differences are relatively small for this case, but now consider what happens as the system moves toward a transmission line limit. In Fig. 8, 66 MVA is flowing on the line from bus 4 to bus 5. If this limit were decreased to 40 MVA, then it would be expected that the marginal cost at bus 5 would tend to increase. The consumer would then decrease the demand. This is exactly what happens as is shown in Fig. 9.

The price increases at bus 5 causing the demand at bus 5 to decrease from 130 to 102 MW. It should also be noted that the price decreases at bus 4 causing the demand at bus 4 to increase from 140 to 163 MW. The price decreases at bus 4 because the line reaching a limit causes there to be a surplus of cheap power at bus 4.

Now consider another scenario where the cost of fuel increases throughout the entire power system. The line limit is increased back to 100 MVA, but the fuel costs throughout the system are increase by 50%. This should drive the marginal costs of the generators up thus increasing marginal costs throughout the system. Results of this simulation are shown in Fig. 10.

## 10. Application to a real and reactive power spot market

Now consider using the solution shown in Fig. 8, but with the addition of price-dependent reactive power loads. With this price-dependence it is expected that the reactive power load at buses 5 and 6 may be reduced, as their price is positive. The variable $\overline { { B _ { \mathrm { q o } } } }$ was chosen to be 0.5 and the OPF results are shown in Fig. 11.

![](/api/attachments/YXS3ZANA/fulltext/images/cbecc8d23e2d3fbd6930b1391dce587f545fc765a77f409cb3bdb93580e37e5e.jpg)  
Fig. 11. Reactive Power Price Dependance, $\overline { { B _ { \mathrm { q o } } } } = 0 . 5 .$

![](/api/attachments/YXS3ZANA/fulltext/images/0682517456494706f4d7e4234e76b9bc8d85fcc3882365df8e36ff62a8ae60f0.jpg)  
Fig. 12. Three-bus system with real power price dependence only.

Comparing Figs. 8 and 11, one sees that the reactive power spot market has had some effect on the system, but it was not a large one. As a power system approaches a voltage limit, however, the reactive power marginal costs increase rapidly. At these points, the influence of reactive power price dependence will make a large difference in the OPF solutions. Fig. 12 shows a sample three-bus power system taken from Ref. 11 simulated<sup>w</sup> <sup>x</sup> using the real power price-dependent model $d _ { \mathrm { p } } ( p _ { \mathrm { p } } ) = d _ { \mathrm { p b a s e } } ( 1 + 1 0 ( 3 5 - p _ { \mathrm { p } } )$ and reactive power demand maintaining constant power factor.

Bus 2 in Fig. 12 is at the voltage limit specified of 0.96 pu and as a result the reactive power marginal cost at this bus is a very large US\$5.54<sup>r</sup>MVRH. Applying the reactive power price dependence model in this situation will not only decrease the reactive power demand, but may also enable the bus to increase its real power demand as the voltage limit is removed. The result of simulating this system with $\overline { { B _ { \mathrm { q o } } } }$ is shown in Fig. 13. The results shown in Fig. 13 verify that the real power demand is able to increase as expected.

## 11. A possible further restatement of the traditional OPF

Consider the necessary equations for our alternate approach shown in Eq. 5.4 . Consider the functionŽ . Ž . S p which is the functional inverse of $( \partial C ( \mathbf { s } ) ) / ( \partial \mathbf { s } )$ . In other words ${ \bf p } _ { \mathrm { s } } - \frac { \partial C } { \partial { \bf s } } ( { \bf S } ( { \bf p } _ { \mathrm { s } } ) ) = 0 \forall { \bf p } _ { \mathrm { s } }$ . Then enforcing the condition $\frac { - \partial C ( \mathbf { s } ) } { \partial \mathbf { s } } - \tilde { \lambda } _ { \mathrm { \hat { h } \mathrm { s } } } - \lambda _ { \mathrm { g s \operatorname* { m i n } } } + \lambda _ { \mathrm { g s \operatorname* { m a x } } } = 0$ is the same as enforcing the condition $\begin{array} { r } { \mathbf s = \mathbf S ( \tilde { \lambda } _ { \mathrm { \hat { h } s } } + \lambda _ { \mathrm { g s \operatorname* { m i n } } } - } \end{array}$ $\pmb { \lambda } _ { \mathrm { g s } \operatorname* { m a x } } )$

![](/api/attachments/YXS3ZANA/fulltext/images/ad7324f608f454f3576dce10095c19f374af918ff9d3524be39065fd86f3f0a5.jpg)  
Fig. 13. Reactive power price dependence, $\overline { { B _ { \mathrm { q o } } } } = 1 . 0 .$

Therefore, we may rewrite the necessary conditions as:

$$
\begin{array}{l} \left(\boldsymbol {\lambda} _ {\mathrm{h}} ^ {T} \frac {\partial \mathbf {h} \Big (\mathbf {x} , \mathbf {s} , \mathbf {D} \Big (\tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} + \boldsymbol {\lambda} _ {\mathrm{gdmin}} - \boldsymbol {\lambda} _ {\mathrm{gdmax}} \Big) \Big)}{\partial \mathbf {x}} \right. \\ \left. + \boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \frac {\partial \mathbf {g} \Big (\mathbf {x} , \mathbf {s} , \mathbf {D} \Big (\tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} + \boldsymbol {\lambda} _ {\mathrm{gdmin}} - \boldsymbol {\lambda} _ {\mathrm{gdmax}} \Big) \Big)}{\partial \mathbf {x}}\right) = 0 \\ \mathbf {s} - \mathbf {S} \Big (\tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hs}}} + \boldsymbol {\lambda} _ {\mathrm{gsmin}} - \boldsymbol {\lambda} _ {\mathrm{gsmax}} \Big) = 0 \\ \mathbf {h} \Big (\mathbf {x}, \mathbf {s}, \mathbf {D} \Big (- \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} + \boldsymbol {\lambda} _ {\mathrm{gdmin}} - \boldsymbol {\lambda} _ {\mathrm{gdmax}} \Big) \Big) = 0 \\ \boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \mathbf {g} \Big (\mathbf {x}, \mathbf {s}, \mathbf {D} \Big (- \tilde {\boldsymbol {\lambda}} _ {\hat {\mathrm{hd}}} + \boldsymbol {\lambda} _ {\mathrm{gdmin}} - \boldsymbol {\lambda} _ {\mathrm{gdmax}} \Big) \Big) = 0 \end{array}\tag{10.1}
$$

which can be simplified to:

$$
\begin{array}{l}\left( \right.\lambda_ {\mathrm{h}} ^ {T} \frac {\partial \mathbf {h} \left(\mathbf {x} , \mathbf {S} \left(\tilde {\lambda} _ {\hat {\mathrm{hs}}} + \lambda_ {\mathrm{gsmin}} - \lambda_ {\mathrm{gsmax}}\right) , \mathbf {D} \left(- \tilde {\lambda} _ {\hat {\mathrm{hd}}} + \lambda_ {\mathrm{gdmin}} - \lambda_ {\mathrm{gdmax}}\right)\right)}{\partial \mathbf {x}} + \lambda_ {\mathrm{g}} ^ {T} \frac {\partial \mathbf {g} \left(\mathbf {x} , \mathbf {S} \left(\tilde {\lambda} _ {\hat {\mathrm{hs}}} + \lambda_ {\mathrm{gsmin}} - \lambda_ {\mathrm{gsmax}}\right) , \mathbf {D} \left(- \tilde {\lambda} _ {\hat {\mathrm{hd}}} + \lambda_ {\mathrm{gdmin}} - \lambda_ {\mathrm{gdmax}})\right)\right)}{\partial \mathbf {x}} = 0\\\mathbf {h} \left(\mathbf {x}, \mathbf {S} \left(\tilde {\lambda} _ {\hat {\mathrm{hs}}} + \lambda_ {\mathrm{gsmin}} - \lambda_ {\mathrm{gsmax}}\right), \mathbf {D} \left(- \tilde {\lambda} _ {\hat {\mathrm{hd}}} + \lambda_ {\mathrm{gdmin}} - \lambda_ {\mathrm{gdmax}}\right)\right) = 0\\\boldsymbol {\lambda} _ {\mathrm{g}} ^ {T} \mathbf {g} \left(\mathbf {x}, \mathbf {S} \left(\tilde {\lambda} _ {\hat {\mathrm{hs}}} + \lambda_ {\mathrm{gsmin}} - \lambda_ {\mathrm{gsmax}}\right), \mathbf {D} \left(- \tilde {\lambda} _ {\hat {\mathrm{hd}}} + \lambda_ {\mathrm{gdmin}} - \lambda_ {\mathrm{gdmax}}\right) \right. = 0\end{array}\tag{10.2}
$$

In this formulation, consumer demand functions and supplier supply functions can be submitted and the optimum determined.

## 12. Conclusion

This paper shows that one can make simple modifications to an existing OPF algorithm that minimizes generation costs in order to solve the maximization of social welfare objective of the OPF. This modification is both simple and intuitive and leads to the possibility of simulating a real and reactive power market by asking participants to submit price-dependent demand curves. This idea further leads to the possible reformulation of the generation costs into price-dependent supply curves. Given a set of price-dependent supply curves along with a set of price-dependent demand curves, a two sided power market could be simulated.

## References

<sup>w</sup> <sup>x</sup> 1 M.L. Baughman, S.N. Siddiqi, Real-time pricing of reactive power: theory and case study results, IEEE Transactions on Power Systems 6 1 1991 23–29. Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 H. Chao, S. Peck, A market mechanism for electric power transmission, Journal of Regulatory Economics, July 1996, pp. 25–59.

<sup>w</sup> <sup>x</sup> 3 D. Chattopadhyyay, K. Bhattacharya, J. Parikh, Optimal reactive power planning and its spot pricing: an integrated approach, IEEE Transactions on Power Systems 10 4 1995 2014–2020.Ž . Ž .

4 S. Hao, A. Papalexopoulos, Reactive power pricing and management, IEEE Transactions on Power Systems 12 1 1997 95–104. Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 W.W. Hogan, Markets in real electric networks require reactive prices, The Energy Journal 14 3 1993 . Ž . Ž .

<sup>w x</sup>6 H.W. Kuhn, A.W. Tucker, Nonlinear programming, Proc. Second Berkeley Symposium on Mathematical Statistics and Probability, Univ. of California Press, 1961, pp. 481–492.

<sup>w</sup> <sup>x</sup> 7 T.J. Overbye, P.W. Sauer, G. Gross, M.J. Laufenberg, J.D. Weber, A simulation tool for analysis of alternative paradigms for the new electricity business, Proceedings of 30th Hawaii International Conference on System Sciences, Maui, HI, January 1997, pp. V634–V640.

8 I.J. Perez-Arriago, C. Meseguer, Wholesale marginal prices in competitive generation markets, IEEE Transactions on Power Systems 12 2 1997 710–717.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 F.C. Schweppe, M.C. Caramanis, R.D. Tabors, R.E. Bohn, Spot Pricing of Electricity, Kluwer Academic Publishers, Boston, 1988.

<sup>w</sup> <sup>x</sup> 10 D.I. Sun, B. Ashley, B. Brewer, A. Hughes, W.F. Tinney, Optimal power flow by Newton approach, IEEE Transactions on Power Apparatus and Systems 103 1994 2864–2880.Ž .

<sup>w</sup> <sup>x</sup> 11 J.D. Weber, M.J. Laufenberg, T.J. Overbye, P.W. Sauer, Assessing the Value of Reactive Power Services in Electric Power Systems, Conference on Unbundled Power Quality Services, Key West, Florida, November 17–19, 1996.

James D. Weber received his BS degree in Electrical Engineering from the University of Wisconsin, Platteville in 1995. He was a summer intern at Wisconsin Power and Light Company in 1994 and 1995. He is currently a graduate student in Electrical and Computer Engineering at the University of Illinois at Urbana-Champaign while working as a software developer for PowerWorld.

Thomas J. Overbye received his BS, MS, and PhD degrees in Electrical Engineering from the University of Wisconsin-Madison in 1983, 1988 and 1991, respectively. He was employed with Madison Gas and Electric Company from 1983 to 1991. Currently he is an Associate Professor of Electrical and Computer Engineering at the University of Illinois at Urbana-Champaign. In 1993, he was the recipient of the IEEE PES Walter Fee Outstanding Young Engineer Award.

Christopher L. DeMarco received his SB in Electrical Engineering from MIT in 1980 and his PhD in the same subject from the University of California, Berkeley in 1985. Since 1985, he has been a member of the faculty of the Department of Electrical and Computer Engineering, University of Wisconsin-Madison.
