---
otero_id: 21672
otero_key: "PFP8N4WN"
title: "The stability of electric energy markets"
authors: "Fernando L. Alvarado"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00077-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The stability of electric energy markets

Fernando L. Alvarado )

ECE Department, The UniÕersity of Wisconsin-Madison, Madison, WI 53706-1691, USA

## Abstract

Power system markets represented by dynamic equations provide insights into the market behavior which are not available from static models. In particular: 1 markets that are required to balance supply and demand precisely at all timesŽ . may be unstable if one supplier exhibits economies of scale and will be unstable if two suppliers exhibit this behavior. The instability is characterized by one or more positive eigenvalues. 2 Markets where some energy imbalance is allowed toŽ . accumulate can exhibit an instability, depending on the exact values of time constants and delays in the system. 3Ž . Congestion can be helpful from the perspective of stability: a market can become unstable in the eigenvalue sense if congestion is removed. 4 A power system with stable electromechanical dynamic behavior when considered by itself andŽ . Ž . market by itself stable can, when analyzed jointly, exhibit unstable behavior. Some of the instabilities alluded here areŽ . nothing more than fluctuations in demands and prices. However, fluctuations are likely to require larger security margins, thus greater costs to operate the system. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Market dynamics; Power system dynamics; Eigenvalues; Energy policy; ISO; System operation; Network congestion

## 1. Introduction

The response of markets to changes in prices is not instantaneous. Neither is the response of a power system to an order to increase the power output of a particular unit or units. These delays in the ability to respond to changing conditions can give rise to instabilities, where periods of excess supply at cheap prices are followed by periods of insufficient supply. This paper studies the dynamics of markets by themselves as well as their possible interaction with the other dynamic effects of an electromechanical power system.

The paper is useful for the design of power exchange rules, and also for the establishment of policies and procedures for Independent System Operators for Electric Power Systems. It is necessary in both cases to consider to some degree whether the markets that underlie this mode of operation lead to well-behaved stableŽ . equilibrium conditions. The potential instability of markets was recognized as a problem in the economics literature in the 1930s, where the use of static analysis techniques ‘cobweb diagrams’ was used to study theŽ . stability of markets 9 . Differential equation analysis of the stability of markets is described in Refs.<sup>w</sup> <sup>x</sup> 8,10,12,13 and in many other economics references. This paper uses differential<sup>r</sup>algebraic equations and eigenvalue techniques to study power system markets.

The present work is an extension and consolidation of a number of recent works in this direction 1–4 . Less<sup>w</sup> <sup>x</sup> direct treatments of similar problems in other contexts include Refs. 7,11 .<sup>w</sup> <sup>x</sup>

This paper is based on several assumptions. a Marginal production costsŽ . $\lambda _ { \mathrm { g } }$ are linear functions of the power generation order $P _ { \mathrm { g } }$ . b Marginal benefit functionsŽ . $\lambda _ { \mathrm { d } }$ are negatively-sloping linear functions of power consumption $P _ { \mathrm { d } } .$ . c Response of suppliers and consumers to observed prices is not instantaneous. It is governedŽ . by first order single time constant differential equations. d If power is not balanced precisely at all times, an Ž . energy imbalance results. An energy imbalance leads to the need to control such imbalance to prevent system damage or unwanted relay action. e The synchronous generators can be represented by differential equationŽ . models. Some of these models include the effect of voltage regulator and power system stabilizing signals Ž . Ž . PSSS . f The action of the governor<sup>r</sup>turbine system is also representable by a differential equation model. gŽ . Production is a function of marginal cost and price. Consumption is a function of marginal benefit, price, and system voltage. h The network is represented either as a set of linear algebraic equations, or just by a simpleŽ . power balance condition.

The paper considers several cases of increasing complexity:

<sup>Ø</sup> first, the dynamics of a pure market are formulated and analyzed, starting from a single supplier and a single consumer and generalizing it to the case of m providers and n consumers,

<sup>Ø</sup> second, the possibility of energy imbalance is taken into consideration,

<sup>Ø</sup> next, the effect of congestion is analyzed,

<sup>Ø</sup> finally, an integrated market-plus-network is developed and analyzed.

The paper concludes by reporting on a number of results obtained by the author from using the models developed.

## 2. Market-only dynamics

If a supplier observes a market price  above his<sup>r</sup>her production cost $\lambda _ { \mathrm { g } i } ,$ , the supplier will expand production until the marginal cost of production equals the price. The rate of expansion is proportional to the difference between the observed price and the actual production cost. The speed with which the generation power output $P _ { \mathrm { g } i }$ of supplier i can respond is supplier dependent. It is denoted by a time constant $\tau _ { \mathrm { g } i }$ for supplier i. Let the price at any given time be . The above yields the following differential equation:

$$
\tau_ {\mathrm{g} i} \dot {P} _ {\mathrm{g} i} = \lambda - b _ {\mathrm{g} i} - c _ {\mathrm{g} i} P _ {\mathrm{g} i}\tag{1}
$$

where $b _ { \mathrm { g } i } + c _ { \mathrm { g } i } P _ { \mathrm { g } i }$ is the marginal cost $\lambda _ { \mathrm { g } i }$ of supplier i.

A consumer demand $P _ { \mathrm { d } i }$ with a marginal benefit function $\lambda _ { \mathrm { d } i }$ above the marginal price will expand consumption until parity is attained. The speed of expansion is consumer dependent, and it is characterized by a time constant $\tau _ { \mathrm { d } i }$ . The equation describing the behavior of a consumer is:

$$
\tau_ {\mathrm{d} i} \dot {P} _ {\mathrm{d} i} = b _ {\mathrm{d} i} + c _ {\mathrm{d} i} P _ {\mathrm{d} i} - \lambda\tag{2}
$$

where $b _ { \mathrm { d } i } + c _ { \mathrm { d } i } P _ { \mathrm { d } i }$ is the marginal consumer benefit.

The final condition required to characterize the marketplace is balance between supply and demand. If there is no energy storage, such a condition for the case of m suppliers and n consumers is characterized by:

$$
\sum_ {i = 1} ^ {m} P _ {\mathrm{g} i} = \sum_ {i = 1} ^ {n} P _ {\mathrm{d} i}.\tag{3}
$$

Differential equations under the assumption that the state variable of interest are the quantities are known as the ‘Marshallian’ formulation. The price is a consequence of the quantity 12 . This model is appropriate when the quantities supplied and consumed are adjusted comparatively slowly relative to price. The dynamics of the model presented here include the further requirement that supply and demand be in precise balance at all times. An alternative dynamic model is based on the use of prices rather than quantities as state variables theŽ ‘Walrasian’ formulation ..

For a one supplier one demand case, these equations become:

$$
\tau_ {\mathrm{g}} \dot {P} _ {\mathrm{g}} = \lambda - b _ {\mathrm{g}} - c _ {\mathrm{g}} P _ {\mathrm{g}}\tag{4}
$$

$$
\tau_ {\mathrm{d}} \dot {P} _ {\mathrm{d}} = b _ {\mathrm{d}} + c _ {\mathrm{d}} P _ {\mathrm{d}} - \lambda\tag{5}
$$

$$
P _ {\mathrm{g}} = P _ {\mathrm{d}}\tag{6}
$$

which, in matrix form, can be expressed as:

$$
\left[ \begin{array}{c c c} \tau_ {\mathrm{g}} & 0 & 0 \\ 0 & \tau_ {\mathrm{d}} & 0 \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \dot {P} _ {\mathrm{g}} \\ \dot {P} _ {\mathrm{d}} \\ \dot {\lambda} \end{array} \right] = \left[ \begin{array}{c c c} - c _ {\mathrm{g}} & 0 & 1 \\ 0 & + c _ {\mathrm{d}} & - 1 \\ 1 & - 1 & 0 \end{array} \right] \left[ \begin{array}{c} P _ {\mathrm{g}} \\ P _ {\mathrm{d}} \\ \lambda \end{array} \right] + \left[ \begin{array}{c} - b _ {\mathrm{g}} \\ b _ {\mathrm{d}} \\ 0 \end{array} \right].\tag{7}
$$

The equilibrium for these equations is obtained by setting the derivative terms to zero:

$$
\left[ \begin{array}{c c c} - c _ {\mathrm{g}} & 0 & 1 \\ 0 & + c _ {\mathrm{d}} & - 1 \\ 1 & - 1 & 0 \end{array} \right] \left[ \begin{array}{c} P _ {\mathrm{g}} \\ P _ {\mathrm{d}} \\ \lambda \end{array} \right] = \left[ \begin{array}{c} b _ {\mathrm{g}} \\ - b _ {\mathrm{d}} \\ 0 \end{array} \right].\tag{8}
$$

Solution of this algebraic linear problem leads to:

$$
P _ {\mathrm{g}} = \frac {b _ {\mathrm{d}} - b _ {\mathrm{g}}}{c _ {\mathrm{g}} - c _ {\mathrm{d}}}\tag{9}
$$

$$
P _ {\mathrm{d}} = P _ {\mathrm{g}}\tag{10}
$$

$$
\lambda = \frac {- b _ {\mathrm{g}} c _ {\mathrm{d}} + c _ {\mathrm{g}} b _ {\mathrm{d}}}{c _ {\mathrm{g}} - c _ {\mathrm{d}}}\tag{11}
$$

Generally, the following is true:

$c _ { \mathrm { d } } < 0 \colon$ this means that marginal consumer benefit decreases with consumption;

$b _ { \mathrm { d } } > b _ { \mathrm { g } }$ : this means that initial consumer marginal benefit is greater than initial producer marginal cost;

$b _ { \mathrm { g } } > 0$ it takes some effort to produce the first unit ;Ž .

<sup>Ø</sup> while normally $c _ { \mathrm { g } } > 0$ , the case of $c _ { \mathrm { g } } \leq 0$ cannot be ruled out economies of scale .Ž .

The price  can be eliminated from the original dynamic equations by adding Eqs. 4 and 5 . Substitution Ž . Ž . from Eq. 6 , re-arrangement, and retention of the homogeneous portion of the result leads to: Ž .

$$
\left(\tau_ {\mathrm{g}} + \tau_ {\mathrm{d}}\right) \dot {P} _ {\mathrm{g}} = - \left(c _ {\mathrm{g}} - c _ {\mathrm{d}}\right) P _ {\mathrm{g}}.\tag{12}
$$

This is a linear first-order system. The condition for the stability of this system is that all eigenvalue one inŽ this case be negative:.

$$
\frac {c _ {\mathrm{d}} - c _ {\mathrm{g}}}{\tau_ {\mathrm{g}} + \tau_ {\mathrm{d}}} <   0\tag{13}
$$

or simply $c _ { \mathrm { g } } > c _ { \mathrm { d } } ,$ since $\tau _ { \mathrm { g } } > 0$ and $\tau _ { \mathrm { d } } > 0$ . Satisfying this condition is virtually assured, since $c _ { \mathrm { d } } < 0$ quite Ž often $c _ { \mathrm { d } } \ll \bar { 0 } )$ . Thus, this type of market is stable, and static analysis is sufficient to ascertain the economic behavior of such a market.

The above can be generalized to the case of m suppliers and n consumers. Furthermore, the possibility of a constant price-insensitive demand component can be considered. The resulting equations are:Ž .

$$
\begin{array}{r l} & {\left[ \begin{array}{c c c c c c c c} \tau_ {\mathrm{g} 1} & & & & & & & \\ & \ddots & & & & & \\ & & \tau_ {\mathrm{g} m} & & & & \\ & & & \tau_ {\mathrm{d} 1} & & & \\ & & & & \ddots & & \\ & & & & & \tau_ {\mathrm{d} n} & \\ & & & & & & 0 \end{array} \right] \left[ \begin{array}{c} \dot {P} _ {\mathrm{g} 1} \\ \vdots \\ \dot {P} _ {\mathrm{g} m} \\ \dot {P} _ {\mathrm{d} 1} \\ \vdots \\ \dot {P} _ {\mathrm{d} n} \\ \dot {\lambda} \end{array} \right]} \\ & {= \left[ \begin{array}{c} - b _ {\mathrm{g} 1} \\ \vdots \\ - b _ {\mathrm{g} m} \\ + b _ {\mathrm{d} 1} \\ \vdots \\ + b _ {\mathrm{d} n} \\ 0 \end{array} \right] + \left[ \begin{array}{c c c c c c c c c} - c _ {\mathrm{g} 1} & & & & & & & 1 \\ & \ddots & & & & & & \vdots \\ & & - c _ {\mathrm{g} m} & & & & & 1 \\ & & & + c _ {\mathrm{d} 1} & & & & - 1 \\ & & & & \ddots & & & \vdots \\ & & & & & + c _ {\mathrm{d} n} & - 1 \\ 1 & \dots & 1 & - 1 & \dots & - 1 & 0 \end{array} \right] \left[ \begin{array}{c} P _ {\mathrm{g} 1} \\ \vdots \\ P _ {\mathrm{g} m} \\ P _ {\mathrm{d} 1} \\ \vdots \\ P _ {\mathrm{d} n} \\ \lambda \end{array} \right]} \end{array}
$$

These equations can be reduced to a set of purely differential equations by algebraic elimination of one state variable $( P _ { \mathrm { g 1 } } )$ Ž . and elimination of one now redundant differential equations the first . The homogeneous portion of the reduced equations is in matrix form :Ž .

$$
\tilde {\mathbf {T}} \dot {\tilde {\boldsymbol {P}}} = - \tilde {\mathbf {C}} \tilde {\mathbf {P}}\tag{14}
$$

where:

$$
\begin{array}{l} \tilde {\mathbf {T}} = \left[ \begin{array}{c c c c c c} \tau_ {\mathrm{g} 1} + \tau_ {\mathrm{g} 2} & \dots & \tau_ {\mathrm{g} 1} & - \tau_ {\mathrm{g} 1} & \dots & - \tau_ {\mathrm{g} 1} \\ \vdots & \ddots & \vdots & \vdots & & \vdots \\ \tau_ {\mathrm{g} 1} & & \tau_ {\mathrm{g} 1} + \tau_ {\mathrm{g} m} & - \tau_ {\mathrm{g} 1} & \dots & - \tau_ {\mathrm{g} 1} \\ - \tau_ {\mathrm{g} 1} & \dots & - \tau_ {\mathrm{g} 1} & \tau_ {\mathrm{g} 1} + \tau_ {\mathrm{d} 1} & \dots & \tau_ {\mathrm{g} 1} \\ \vdots & & \vdots & \vdots & \ddots & \vdots \\ - \tau_ {\mathrm{g} 1} & \dots & - \tau_ {\mathrm{g} 1} & \tau_ {\mathrm{g} 1} & \dots & \tau_ {\mathrm{g} 1} + \tau_ {\mathrm{d} n} \end{array} \right] \\ \tilde {\mathbf {C}} = \left[ \begin{array}{c c c c c c} - c _ {\mathrm{g} 1} - c _ {\mathrm{g} 2} & \dots & - c _ {\mathrm{g} 1} & c _ {\mathrm{g} 1} & \dots & c _ {\mathrm{g} 1} \\ \vdots & \ddots & \vdots & \vdots & & \vdots \\ - c _ {\mathrm{g} 1} & \dots & - c _ {\mathrm{g} 1} - c _ {\mathrm{g} m} & c _ {\mathrm{g} 1} & \dots & c _ {\mathrm{g} 1} \\ c _ {\mathrm{g} 1} & \dots & c _ {\mathrm{g} 1} & - c _ {\mathrm{g} 1} + c _ {\mathrm{d} 1} & \dots & - c _ {\mathrm{g} 1} \\ \vdots & & \vdots & \vdots & \ddots & \vdots \\ c _ {\mathrm{g} 1} & \dots & c _ {\mathrm{g} 1} & - c _ {\mathrm{g} 1} & \dots & - c _ {\mathrm{g} 1} + c _ {\mathrm{d} n} \end{array} \right]. \end{array}
$$

The dynamic characteristics of the market are dictated by the eigenvalues of this generalized eigenvalue problem. The following additional general observations can be made from the diagonal-dominance characteristics of these matrices.

<sup>Ø</sup> If $c _ { \mathrm { g } i } > 0$ for all $i ,$ the result is a stable market all eigenvalues are negative .Ž .

<sup>Ø</sup> If ${ \dot { c _ { \mathrm { g } } _ { i } } } \leq 0$ for two or more values of i, the result is necessarily an unstable market.

<sup>Ø</sup> Because $\tilde { \mathbf { T } }$ is a diagonal-dominant positive matrix, it is sufficient to ascertain the stability properties of $\tilde { \mathbf { C } }$ to establish the stability properties of $\mathbf { \widetilde { T } } ^ { - 1 } \mathbf { \widetilde { C } }$

The practical consequence of the above is that markets can tolerate one supplier that exhibits economies of scale $\left( c _ { i } < 0 \right)$ , provided the economies are not too significant. In particular, if $c _ { i } < 0$ , then it is required that $\textstyle 1 / | c _ { i } | < \sum _ { j \mathop { = } 1 , j \not = i } ^ { m } 1 / | c _ { j } | .$

Negatively-sloping marginal costs can be the result of:

<sup>Ø</sup> ‘valve points’ situations when a partially open steam valve in a unit leads to inefficient operation and otherŽ . such conditions dictated by the efficiencies of various technologies;

<sup>Ø</sup> requirements for minimum production levels;

<sup>Ø</sup> startup and shutdown costs;

<sup>Ø</sup> inherent economies of scale of certain technologies.

## 3. Energy imbalance

Energy imbalance means that the requirement for exact equality between supply and demand 17 is not metŽ . at all times. This leads to either an excess or a shortage of energy in the system. In a real power system, energy imbalance cannot be sustained indefinitely 5 . It must be reduced or driven to zero. In a traditional utility environment, such an objective is attained by automatic generation control. In a market-driven environment, it can be assumed that prices will reflect the degree of energy imbalance. That is, an excess of the quantity supplied the power generation order Ž $P _ { \mathrm { g } } )$ in the grid will slightly depress the value of the power, and thus will decrease the price of power. Such a situation can be represented by adjusting prices depending on the degree of energy imbalance. The changing of price depending on excess or shortfall of real time energy is referred as frequency regulation pricing or ACE area control error pricing. The equations representing the dynamics ofŽ . ACE pricing for m suppliers and n consumers are:

$$
\tau_ {\mathrm{g} j} \dot {P} _ {\mathrm{g} j} = - b _ {\mathrm{g} j} - c _ {\mathrm{g} j} P _ {\mathrm{g} j} + \lambda - K _ {j} E, \qquad j = 1, \ldots , m\tag{15}
$$

$$
\tau_ {\mathrm{d} i} \dot {P} _ {\mathrm{d} i} = b _ {\mathrm{d} i} + c _ {\mathrm{d} i} P _ {\mathrm{d} i} - \lambda , \qquad i = 1, \ldots , n\tag{16}
$$

$$
\dot {E} = \sum_ {j = 1} ^ {m} P _ {\mathrm{g} j} - \sum_ {i = 1} ^ {n} P _ {\mathrm{d} i}\tag{17}
$$

$$
\tau_ {\lambda} \dot {\lambda} = - E\tag{18}
$$

where: $b _ { \mathrm { g } j } + c _ { \mathrm { g } j } P _ { \mathrm { g } j }$ is the marginal cost of supplier j; $b _ { \mathrm { d } i } + c _ { \mathrm { d } i } P _ { \mathrm { d } i }$ is the marginal benefit of consumer i; $\tau _ { \mathrm { g } j }$ is the power generation order time constant of supplier $j ; \tau _ { \mathrm { d } i }$ is the demand time constant of consumer $i ; \lambda$ is the market price; $\tau _ { \lambda }$ is the market price time constant; E is the power system stored energy; $K _ { j }$ is a market stabilizer gain sent to supplier j.

The interpretation of these equations is as follows: generators act in a way that tends to increase production when prices exceed production marginal costs. Consumers act in a way that tends to increase consumption when marginal benefits exceed price. Since it may be impossible to perfectly balance supply and consumption at all times, any discrepancy accumulates as an energy error. In practical system, this results in either an increase in frequency or an increase in the ACE. The result of an excess of energy is a reduction in the system value of electric energy. The consequence of this is a probable reduction in price, which takes place according to some time constant $\tau _ { \lambda } .$ This reduction in system price increases consumption and decreases production, thereby leading to a decrease in the excess energy. Stability requirements also necessitate the presence of a supplementary stabilizing price signal to be sent to either the suppliers or the consumers 5 . Here, the signal is sent to the<sup>w</sup> <sup>x</sup> suppliers. The stabilizing signal is a constant gain times the accumulated energy error. This can be interpreted as a ‘bias’ that is added to prices whenever the energy error is non-zero. This supplementary signal is essential to asymptotic stable market behavior.

## 4. Network congestion

Congestion means that the flow in one or more lines must be regulated to avoid exceeding a rating and damaging the component, or other such reason. Introducing conditions for congestion avoidance within the previous dynamic formulation including energy imbalance presents several challenges, since congestion can Ž . result in a functional decoupling of the system.

Congestion can be expressed in terms of the network injections both generation and load . ForŽ . $n _ { \mathrm { s } } - 1$ congestion conditions:

$$
\left[ \begin{array}{c c c c c c} 1 & \ldots & 1 & - 1 & \ldots & - 1 \\ S _ {\mathrm{g} 2 1} & \ldots & S _ {\mathrm{g} 2 m} & S _ {\mathrm{d} 2 1} & \ldots & S _ {\mathrm{d} 2 n} \\ \vdots & & \vdots & \vdots & & \vdots \\ S _ {\mathrm{g} n _ {\mathrm{s}} 1} & \ldots & S _ {\mathrm{g} n _ {\mathrm{s}} m} & S _ {\mathrm{d} n _ {\mathrm{s}} 1} & \ldots & S _ {\mathrm{g} n _ {\mathrm{s}} n} \end{array} \right] \left[ \begin{array}{c} P _ {\mathrm{g} 1} \\ \vdots \\ P _ {\mathrm{g} m} \\ P _ {\mathrm{d} 1} \\ \vdots \\ P _ {\mathrm{d} n} \end{array} \right] = \left[ \begin{array}{c} P _ {\mathrm{D}} \\ s _ {2} \\ \vdots \\ s _ {n _ {\mathrm{s}}} \end{array} \right].\tag{19}
$$

The complete dynamic equations for the congested m-supplier n-consumer case with $n _ { \mathrm { s } }$ active algebraic congestion conditions in matrix notation are:

$$
\left[ \begin{array}{c c} \mathbf {T} & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} \dot {\boldsymbol {P}} \\ \dot {\boldsymbol {\Lambda}} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {C} & \mathbf {S} ^ {\mathrm{t}} \\ \mathbf {S} & 0 \end{array} \right] \left[ \begin{array}{c} \boldsymbol {P} \\ \boldsymbol {\Lambda} \end{array} \right] + \left[ \begin{array}{c} \boldsymbol {b} \\ s \end{array} \right]
$$

where T is an unreduced diagonal matrix with the time constants for power generation as well as demand; P is a vector of all power Ž . m generation powers and n demand powers ;  is a vector with all Lagrange multipliers Ž . the price  is the first of these ; C is the diagonal matrix of all quadratic cost coefficients $c _ { \mathrm { g } i }$ as well as $c _ { \mathrm { d } i } ,$ S is a matrix of sensitivity of constraints to injections its first row is the power balance condition ;Ž . s is a vector with $P _ { \mathrm { ~ D ~ } }$ Ž . the price-insensitive demand in its first position and the values of the right hand sides in the constraint equations in the remaining positions.

Because of these $n _ { \mathrm { s } }$ algebraic conditions introduced by congestion, the dynamic equations for this problem are of reduced order. Reduction of the dynamic algebraic equation problem to a purely differential equation can be done by first eliminating the $n _ { \mathrm { s } }$ redundant state variables in terms of a reduced set of $n + m - n _ { \mathrm { s } }$ of non-redundant variables, obtaining in the end a set of $n + m - n _ { \mathrm { s } }$ purely differential equations, organized as follows:

$$
\left[ \begin{array}{c c c} \mathbf {T} _ {1} & 0 & \mathbf {S} _ {1} ^ {\mathrm{t}} \\ 0 & \mathbf {T} _ {2} & \mathbf {S} _ {2} ^ {\mathrm{t}} \\ \mathbf {S} _ {1} & \mathbf {S} _ {2} & 0 \end{array} \right] \left[ \begin{array}{l} \dot {\boldsymbol {P}} _ {1} \\ \dot {\boldsymbol {P}} _ {2} \\ \dot {\boldsymbol {\Lambda}} \end{array} \right] = \left[ \begin{array}{c c c} \mathbf {C} _ {1} & 0 & \mathbf {S} _ {1} ^ {\mathrm{t}} \\ 0 & \mathbf {C} _ {2} & \mathbf {S} _ {2} ^ {\mathrm{t}} \\ \mathbf {S} _ {1} & \mathbf {S} _ {2} & 0 \end{array} \right] \left[ \begin{array}{l} \boldsymbol {P} _ {1} \\ \boldsymbol {P} _ {2} \\ \boldsymbol {\Lambda} \end{array} \right]
$$

where $\mathbf { S } _ { 1 }$ corresponds to an arbitrary but non-singular subset of $n _ { \mathrm { s } }$ by $n _ { \mathrm { s } }$ of S, and $P _ { 1 }$ corresponds to a subset $n _ { \mathrm { s } }$ of $P$ denoting the redundant power variables. Reduction and elimination of  and $P _ { 1 }$ yields the following reduced purely differential equations.

$$
\left[ \mathbf {T} _ {2} + \mathbf {S} _ {2} ^ {\mathrm{t}} \mathbf {S} _ {1} ^ {- \mathrm{t}} \mathbf {T} _ {1} \mathbf {S} _ {1} ^ {- 1} \mathbf {S} _ {2} \right] \dot {\boldsymbol {P}} _ {2} = \left[ \mathbf {C} _ {2} + \mathbf {S} _ {2} ^ {\mathrm{t}} \mathbf {S} _ {1} ^ {- \mathrm{t}} \mathbf {C} _ {1} \mathbf {S} _ {1} ^ {- 1} \mathbf {S} _ {2} \right] \boldsymbol {P} _ {2}\tag{20}
$$

Thus, the model for a congested power system is of lower order than the model for the uncongested system. It is perfectly possible, however, to take into consideration delays and dynamics associated with congestion itself. For example, the assumption that operation of the system above congestion conditions is permitted for some time, provided incentives are created that eventually eliminate the congestion. However, it can be assumed that some delay is inherent in this process. The representation of this situation would amount to little more than replacing some or all of the algebraic equations from 19 with differential equations.Ž .

## 5. Electromechanical dynamics

It is also possible to model in detail the electromechanical dynamics of a system. For example, the detailed generation and transmission electromechanical dynamic models from Ref. 6 or any other such reference<sup>w</sup> <sup>x</sup> dealing with system electromechanical dynamics can be implemented.

For example, the turbine<sup>r</sup>governor can be modelled according to the block diagram Fig. 1, where $P _ { \mathrm { g } }$ corresponds to the power generation order associated with the market model, is the machine velocity, Y is the valve position, and $P _ { \mathrm { { m } } }$ the mechanical power output.

Likewise, the automatic voltage regulator can be modelled according a block diagram representation, such as illustrated in Fig. 2. It is important in any of these models to include the dynamics of any PSSS, which can be derived either from the machine velocity or machine terminal power is also selected by appropriate choice of parameters.

In fact, it is possible to continue in this fashion and represent every aspect of every machine and the entire network if desired, adding detailed models of the system at any time scale of interest. Of course, only those models that have time constants of the same order of magnitude as the market time constants are of interest. The approach extends traditional engineering analysis to help understand how the operation of a system might be affected by ‘signals’ coming from a market.

![](/api/attachments/PFP8N4WN/fulltext/images/ccde869d5bd6849dfb829ea7bb38f1453ceb20d1d3f8c1fcb76ae6ebb645d474.jpg)  
Fig. 1. Governor turbine block diagram.

![](/api/attachments/PFP8N4WN/fulltext/images/b37c491df09e07330f1d0b45c58c9c7af879a877c59d8ba8c78f4d52de33c3b2.jpg)  
Fig. 2. AVR model block diagram.

## 6. Results and experiments

The above models have been used by the author and his colleagues particularly Wellington Santos Mota inŽ . a variety of detailed simulations. The following general results have been obtained from observations of these numerical results for a large range of parameters and time constants.

<sup>Ø</sup> Markets that must balance supply and demand precisely at all times may be unstable if one supplier exhibits economies of scale and will be unstable if two suppliers exhibit this behavior 1 .<sup>w</sup> <sup>x</sup>

<sup>Ø</sup> Markets where some energy imbalance is allowed to accumulate can exhibit an instability, depending on the exact values of time constants and delays in the system 4 . This instability is necessarily an oscillatory<sup>w</sup> <sup>x</sup> instability.

<sup>Ø</sup> Congestion can indeed be helpful from the perspective of stability 1 . That is, congestion can make an<sup>w</sup> <sup>x</sup> otherwise unstable situation stable. This is not to mean that congestion is desirable. Quite the contrary, congestion generally leads to higher prices. However, not all effects of congestion are negative.

<sup>Ø</sup> A power system with stable electromechanical dynamic behavior when considered by itself and market byŽ . Ž itself stable can, when analyzed jointly, exhibit unstable behavior 3 .. <sup>w</sup> <sup>x</sup>

In all these results, only certain ranges of values lead to troublesome operation. In general, the problems are more severe when markets are able to respond quickly such as systems using price signals to balance energyŽ .

and<sup>r</sup>or when the electromechanical system is slow in responding such as, for example, the situation of a set ofŽ power plants connected to a river system with delays between stations ..

## 7. Conclusions

A new approach to the analysis of integrated markets and power systems has been reviewed and mathematically described. The approach permits the characterization of stability of markets using some mild linearity assumptions and assuming that the response of markets can be characterized in terms of differential equations. Important results and conclusions derived using these models are reviewed in Section 6. The main conclusion from these results is that it is essential at some point to take a look at the integrated operation of systems with signals coming from a market, particularly if the markets are fast and the response of the systems is sluggish as it might be with large plants or with natural delays introduced by items such as, for example, Ž river systems . The validity of these models can be extended if one wishes to also take into account the discrete. nature of several of the pricing strategies by resorting to difference instead of differential equations , representŽ . the transmission grid losses and reactive power , and model any desired or agreed-upon operating policies in Ž . greater detail. In fact, it is recommended that no policy for system operation should be implemented without at least some attention paid to the possible dynamic implications of the policy.

## References

<sup>w</sup> <sup>x</sup> 1 The stability of power system markets, IEEE Transactions on Power Systems 1998 , to appear.Ž .

<sup>w</sup> <sup>x</sup> 2 F. Alvarado, The dynamics of power system markets, Technical Report PSERC-97-01, Power Systems Engineering Research Consortium PSERC , The University of Wisconsin, March 1997.Ž .

<sup>w</sup> <sup>x</sup> 3 F.L. Alvarado, W.S. Mota, Dynamic instabilities in energy markets, VI SEPOPE Conference, May 24–29, 1998.

<sup>w</sup> <sup>x</sup> 4 F.L. Alvarado, W.S. Mota, The role of energy imbalance management on power market stability, Proceedings of the 31st Annual Hawaii International Conference on System Sciences HICSS , IEEE Computer Society 3 1998 4–9.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 F.L. Alvarado, The dynamic of power system markets technical report PSERC-97-01, The University of Wisconsin-Madison, March 1997.

<sup>w</sup> <sup>x</sup> 6 P.M. Anderson, A.A. Fouad, Power System Control and Stability, The Iowa State Univ. Press, Ames, IA, 1977.

<sup>w</sup> <sup>x</sup> 7 R. Baldick, R.J. Kaye, F.F. Wu, Electricity tariffs under imperfect knowledge of participant benefits, IEEE Transactions on Power Systems 7 4 1992 1471–1482.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 B. Beavis, I.M. Dobbs, Optimization and Stability Theory for Economic Analysis, Cambridge Univ. Press, London, 1990.

<sup>w</sup> <sup>x</sup> 9 M. Ezekiel, The cobweb theorem, Quarterly Journal of Economics 52 2 1938 255–278. Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 D. Hawkins, Some conditions for macroeconomic stability, Econometrica, October 1948 310–322.Ž .

<sup>w</sup> <sup>x</sup> 11 J. Ruusunen, R.P. Hamalainen, M. Rasnen, Game theoretic modelling in the dynamic pricing of electricity, in: R.P. Hamalainen, H.K. Ehtamo Eds. , Lecture Notes in Control and Information, Vol. 157, Springer-Verlag, 1990.Ž .

<sup>w</sup> <sup>x</sup> 12 P.A. Samuelson, Foundations of Economic Analysis, Enlarged Edition, Harvard Univ. Press, 1983.

<sup>w</sup> <sup>x</sup> 13 G.L. Thompson, S.A.O. Thore, Computational economics, Annals of Operations Research, Vol. 68, Boltzer Science, 1997.

Fernando L. Alvarado was born in Lima, Peru. He did his undergraduate studies at the National Engineering University in Peru, and his MS studies at Clarkson University and he holds a PhD degree from the University of Michigan. He is a professor at the University of Wisconsin in Madison. He recently participated as a member of the Task Force on Energy Infrastructures, Presidential Commission on Critical Infrastructures, January–April 1998. He is a full professor of Electrical and Computer Engineering at the University of Wisconsin. University of Wisconsin is also a member of PSERC, a NSF and Industry Sponsored Consortium of Universities involved in Electrical Power Systems Research. He is a fellow of IEEE and a member of the IEEE Energy Policy Board. He has well over 200 technical publications in prestigious journals and conferences. He is a senior consultant with Christensen Associates.
