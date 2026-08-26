---
otero_id: 20917
otero_key: "FTKDDAVH"
title: "Reactive power considerations in ATC computation"
authors: "Santiago Grijalva; Peter W Sauer"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00109-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Reactive power considerations in ATC computation

Santiago Grijalva, Peter W. Sauer

Department of Electrical and Computer Engineering, UniÕersity of Illinois at Urbana-Champaign, 1406 W. Green St., Urbana, IL 61801, USA

## Abstract

Reactive power impacts are considered in linear methods for computing Available Transfer Capability ATC . A newŽ . approach that first determines the reactive power flows using the exact circle equation for the transmission line complex flow, and then determines ATC using active power distribution factors is given. The ideas are demonstrated on 3-bus and 7-bus systems, and the results are discussed and compared with those obtained without reactive power considerations, and full nonlinear solutions. The following text includes the text and results from the conference paper: AReactive Power Considerations in Linear ATC ComputationB, presented at the 1999 Hawaii International Conference on System Sciences, Maui, Hawaii, January 5–8, 1999. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Linear ATC; Distribution factors; Reactive power

## 1. Introduction

It is known that given a specific condition of a power system, its ability to accommodate additional transactions is effectively determined if one is able to perform the following for the base case and a set of contingencies:

Ž .a Full AC power flow,

Ž . b Steady-state stability analysis,

Ž .c Voltage stability analysis, and

Ž . d Transient stability analysis.

For most real systems, this would require an extraordinary amount of computation time and for this reason, simplified methods needed to be developed.

The computation of Available Transfer Capability Ž . ATC has been performed using an active power linear model, which totally neglects the voltage-reactive power phenomena, as well as other operational issues and security constraints. It has been shown that neglecting the reactive power influence in ATC may generate errors that in certain conditions could drive the computation to wrong or at least inaccurate results 12,13 . This drawback in current ATC computations has motivated the definition of the Transmission Reliability Margin TRM , as a way to takeŽ . into consideration all uncertainties about the network and all possible computational errors due to model simplifications or wrong data. As this error could be as large as 8% of the transaction to be committed, there exists an interest in characterizing the components of this error, and identifying efficient ways to reduce it.

Throughout the paper, the central issue is the inclusion of reactive power as a way to decrease the errors of linear methods for ATC computation. This is motivated by the fact that:

Ž .a In highly loaded transmission systems, the reactive power can be a significant component of changes in flows.

Ž . b Thermal limits of transmission lines are MVA quantities instead of approximate active power Ž . MW limits.

Ž .c The consideration of reactive power flow provides insight in the behavior of the voltage and other security constraints of the system.

In the following, an efficient approach to include reactive power is proposed as a way to considerably decrease the error in ATC, with a small addition in computation requirements.

The rest of the paper is organized in the following manner. In Section 2 we present the modeling back ground, which explains the relation between active and reactive power in the transmission line, and the concept of active power distribution factors. In Section 3 we describe the equations required to include reactive power in a linear ATC calculation, namely, Reactive Power Linear ATC. In Section 4 we present and discuss 3-bus and 7-bus case systems and compare the results with the purely active power approach and full nonlinear solutions. In Section 5 we discuss additional considerations for Reactive Power Linear ATC as well as other potential applications to ATC-related problems. Finally, in Section 6 we present some conclusions.

Refs. 1–11,14–21 provide additional informa-<sup>w</sup> <sup>x</sup> tion on ATC computation.

## 2. Background

## 2.1. Transmission-line P–Q circle relation

Consider the short model of a transmission line i.e., only the series reactance is included, as shown in Fig. 1.

![](/api/attachments/FTKDDAVH/fulltext/images/7bd25c0f6acd7233b8fa12af8cd3e6cc9b7f194197c90b0afb71552e59fb7386.jpg)  
Fig. 1. Transmission line: short model.

The equation for the complex power flowing from node j to node k Ž . at j is:

$$
\begin{array}{r l} P _ {j k} + j Q _ {j k} & = V _ {j} V _ {k} Y _ {j k} \sin (\delta_ {j} - \delta_ {k}) \\ & + j \left[ V _ {j} ^ {2} Y _ {j k} - V _ {j} V _ {k} Y _ {j k} \cos (\delta_ {j} - \delta_ {k}) \right] \end{array}\tag{1}
$$

where the voltage magnitude $V _ { j }$ and $V _ { k }$ are state variables that depend on the overall operating condition of the power system.

We are interested in the $P { - } Q$ relation in a transmission line as a transaction in the power system occurs. Here, a power transaction is defined as the increase in active power at one or more buses, and the corresponding decrease at one or more other buses.

From Eq. 1 we have: Ž .

$$
P _ {j k} ^ {2} = \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2} \sin^ {2} \left(\delta_ {j} - \delta_ {k}\right)\tag{2}
$$

$$
\left(V _ {j} ^ {2} Y _ {j k} - Q _ {j k}\right) ^ {2} = \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2} \cos^ {2} \left(\delta_ {j} - \delta_ {k}\right)\tag{3}
$$

Adding these two equations, we get:

$$
P _ {j k} ^ {2} + \left(V _ {j} ^ {2} Y _ {j k} - Q _ {j k}\right) ^ {2} = \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2}\tag{4}
$$

Suppose now that voltages $V _ { j }$ and $V _ { k }$ remain approximately constant during the transaction. Then, Eq. Ž . 4 becomes the equation of a circle in the $P _ { j k } { - } Q _ { j k }$ plane which is centered at:

$$
\left(P _ {j k 0}, Q _ {j k 0}\right) = \left(0, V _ {j} ^ {2} Y _ {j k}\right)\tag{5}
$$

and has a radius:

$$
S _ {j k 0} = V _ {j} V _ {k} Y _ {j k}\tag{6}
$$

Here , denotes coordinates in aŽ . v v $P { - } Q$ plane.

Consequently, if the magnitude of the voltages at the two ends of the transmission line do not change too much during a transaction, then the active and reactive power flows are approximately related by a circle equation.

This approximation is well known in the power system literature and is used intensively here. Note that as in general $S _ { j k } \ne - S _ { k j } ,$ , the circles describing the two ends of the transmission line are different. The k-end circle is given by the equation:

$$
P _ {k j} ^ {2} + \left(V _ {k} ^ {2} Y _ {k j} - Q _ {k j}\right) ^ {2} = \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2}\tag{7}
$$

Note also that the radii of the two end circles have the same value.

Now consider the -model of the transmission line as shown in Fig. 2.

We have:

$$
\begin{array}{r l} P _ {j k} + j Q _ {j k} & = V _ {j} ^ {2} G _ {j k} - V _ {j} V _ {k} Y _ {j k} \cos \left(\delta_ {j} - \delta_ {k} + \theta_ {j k}\right) \\ & + j \left[ - V _ {j} ^ {2} B _ {j j} - V _ {j} ^ {2} B _ {j k} - V _ {j} V _ {k} Y _ {j k} \right. \\ & \times \sin \left(\delta_ {j} - \delta_ {k} + \theta_ {j k}\right) \Big ] \end{array}\tag{8}
$$

where

$$
G _ {j k} + j B _ {j k} = 1 / \left[ R _ {j k} + j X _ {j k} \right]\tag{9}
$$

and $\theta _ { j k }$ is the angle of the series impedance.

We change this equation to be:

$$
P _ {j k} - V _ {j} ^ {2} G _ {j k} = - V _ {j} V _ {k} Y _ {j k} \cos (\delta_ {j} - \delta_ {k} + \theta_ {j k})\tag{10}
$$

$$
Q _ {j k} + V _ {j} ^ {2} B _ {j j} + V _ {j} ^ {2} B _ {j k} = - V _ {j} V _ {k} Y _ {j k} \sin \left(\delta_ {j} - \delta_ {k} + \theta_ {j k}\right)\tag{11}
$$

Taking the square of both equations and adding:

$$
\begin{array}{r l} & \left(P _ {j k} - V _ {j} ^ {2} G _ {j k}\right) ^ {2} + \left(Q _ {j k} + V _ {j} ^ {2} B _ {j j} + V _ {j} ^ {2} B _ {j k}\right) ^ {2} \\ & = \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2} \end{array}\tag{12}
$$

Which is similar to Eq. 4 . Again, if the voltagesŽ . $V _ { j }$ and $V _ { k }$ remain approximately constant during the transaction, Eq. 12 is the equation of a circle in the Ž . $P _ { j k } { - } Q _ { j k }$ plane which is centered at:

![](/api/attachments/FTKDDAVH/fulltext/images/eac5851c8e51bf6b49636cf958d34e53b55190f8d594eefd626ea9a002919fd8.jpg)  
Fig. 2. Transmission line: -model.

$$
\left(P _ {j k 0}, Q _ {j k 0}\right) = \left(V _ {j} ^ {2} G _ {j k}, - V _ {j} ^ {2} B _ {j j} - V _ {j} ^ {2} B _ {j k}\right)\tag{13}
$$

and has a radius $S _ { j k 0 } = V _ { j } V _ { k } Y _ { j k }$

14 Ž .

## 2.2. Line thermal limits and ATC

Probably the most relevant security constraint within the computation of ATC is given by the transmission line thermal limits MVA . Let us de- Ž . note by $\mid S _ { j k } \mid$ the magnitude of the complex power flowing through the line $j { - } k$ at bus j. The thermal limit of this line is then a specified scalar constant $S _ { j k } ^ { \mathrm { m a x } }$ . For a transaction of $\varDelta P$ megawatts between buses i and $s , \mid S _ { j k } \mid$ must be always less than $S _ { j k } ^ { \mathrm { m a x } }$ If this does not hold for a line j–k, then we say that this line is oÕerloaded, and that the line is limiting the transaction.

Therefore, the basic ATC problem regarding thermal security limits is: given an initial operating state of the power system, determine the maximum amount $+ \Delta P$ for a transaction between generator i Ž . seller Ž . and generator s buyer such that $\mid S _ { j k } \mid < S _ { j k } ^ { \mathrm { m a x } }$ for all $j { - } k$ lines sidesŽ . j and k in the system.

## 2.3. Distribution factors

Let us assume that a transaction P between buses i and s occurs in the power system. The active power injection at bus i and extraction at busŽ .s will result in a variation in the flows of power through the transmission lines. The variation of the active power flowing through a specific line $j - k \ ( \varDelta P _ { j k } )$ can be approximately related to the active power injection at bus $i \left( \varDelta P _ { i } \right)$ and a simultaneous reduction at bus s, by an active power distribution factor:

$$
\rho_ {i - s, j k} = \Delta P _ {j k} / \Delta P _ {i}\tag{15}
$$

## 2.4. Limiting and operating circles

In the $P _ { j k } { - } Q _ { j k }$ plane, the thermal limit of a transmission line is represented as a circle with center at the origin and radius equal to $S _ { j k } ^ { \mathrm { m a x } }$ . This is here referred to as the limiting circle. We also know that all feasible operating points in the $P _ { j k } { - } Q _ { j k }$ plane will lay approximately on the Ž . operating circle given by Eq. 4 if the transmission-line short modelŽ . is used. This is shown in Fig. 3.

![](/api/attachments/FTKDDAVH/fulltext/images/104454843b486200752da0475219fc7e046f8b568730d1c5089e89ff3c382755.jpg)  
Fig. 3. Operating and limiting circles transmission line short model.

When the -model of the transmission line is used, the operating circle is given by Eq. 12 . TheŽ . meaning of this equation is that the circle is displaced to be centered at the point defined by Eq. 13 Ž . while its radius remains the same, as shown in Fig. 4.

## 3. Reactive power consideration in linear ATC

## 3.1. Maximum line complex flow

Figs. 3 and 4 provide the following information.

Ž . Ž . a The operating circle is the approximate geometric locus of every complex power flow operating point for the line j–k at side j.

Ž . b The transmission line j–k allows power flow operating points that are restricted to the interior of the limiting circle.

Ž .c The maximum complex power flow allowed through the line $j { - } k$ corresponds to a point, which lies at the intersection of the limiting and the operating circles. This point is denoted by $( P _ { j k } ^ { * } , \ Q _ { j k } ^ { * } )$ and corresponds to the operating point at which the MVA rating of the line has been reached. Let us call this point the maximum complex flow for line $j { - } k .$

This point depends on the system operating conditions, the location and amount of the power transaction, and the MVA rating of the line.

Note that the intersection of the two circles involves two possible solutions. The solution must consider the point that is reached when the injection $\varDelta P$ is positive. Furthermore, note that as there is a sending and a receiving circle for one transmission line, we will have to identify the one that reaches the limit first.

For the short model of the transmission line, the maximum complex flow $( P _ { j k } ^ { * } , \ Q _ { j k } ^ { * } )$ is obtained by solving the system of equations:

$$
P _ {j k} ^ {2} + \left(V _ {j} ^ {2} Y _ {j k} - Q _ {j k}\right) ^ {2} = \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2}\tag{16}
$$

$$
P _ {j k} ^ {2} + Q _ {j k} ^ {2} = \left(S _ {j k} ^ {\max}\right) ^ {2}\tag{17}
$$

Expanding the first equation and subtracting from the second one,

$$
\left(V _ {j} ^ {2} Y _ {j k}\right) ^ {2} - 2 V _ {j} ^ {2} Y _ {j k} Q _ {j k} = \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2} - \left(S _ {j k} ^ {\max}\right) ^ {2}\tag{18}
$$

Therefore,

$$
\begin{array}{c} Q _ {j k} ^ {*} = \left(1 / 2 V _ {j} ^ {2} Y _ {j k}\right) \Big [ \left(S _ {j k} ^ {\max}\right) ^ {2} \\ + \left(V _ {j} ^ {2} Y _ {j k}\right) ^ {2} - \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2} \Big ] \end{array}\tag{19}
$$

and,

$$
P _ {j k} ^ {*} = \left[ \left(S _ {j k} ^ {\max}\right) ^ {2} - Q _ {j k} ^ {* 2} \right] ^ {1 / 2}\tag{20}
$$

![](/api/attachments/FTKDDAVH/fulltext/images/59957b25cb8cf68dfe4536a250c35d510f1ff162b5f962a9e6ce8b6bb75701d3.jpg)  
Fig. 4. Operating and limiting circles transmission line -model.

The positive square root must be chosen to maintain consistency with the distribution factors. Similar relations are obtained for the receiving end:

$$
Q _ {k j} ^ {*} = \left(2 V _ {k} ^ {2} Y _ {j k}\right) ^ {- 1} \left[ \left(S _ {j k} ^ {\max}\right) ^ {2} + \left(V _ {k} ^ {2} Y _ {j k}\right) ^ {2} \right.
$$

$$
\left. - \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2} \right]\tag{21}
$$

$$
P _ {k j} ^ {*} = \left[ \left(S _ {j k} ^ {\max}\right) ^ {2} - Q _ {k j} ^ {* 2} \right] ^ {1 / 2}\tag{22}
$$

It is clear that Eqs. 19 – 22 can be applied directly Ž . Ž . if the values of the voltages are known.

In order to determine the $P _ { j k } ^ { * }$ and $\boldsymbol { Q } _ { j k } ^ { * }$ for the case of the transmission line -model, more complicated equations are required because the following system of equations must be solved:

$$
\left(P _ {j k} - V _ {j} ^ {2} G _ {j k}\right) ^ {2} + \left(Q _ {j k} + V _ {j} ^ {2} B _ {j j} + V _ {j} ^ {2} B _ {j k}\right) ^ {2}
$$

$$
= \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2}\tag{23}
$$

$$
P _ {j k} ^ {2} + Q _ {j k} ^ {2} = \left(S _ {j k} ^ {\max}\right) ^ {2}\tag{24}
$$

Rewriting these equations with the center coordinates and the radius defined by expressions 13 andŽ . Ž . 14 ,

$$
\left(P _ {j k} - P _ {j k 0}\right) ^ {2} + \left(Q _ {j k} - Q _ {j k 0}\right) ^ {2} = S _ {j k 0} ^ {2}\tag{25}
$$

$$
P _ {j k} ^ {2} + Q _ {j k} ^ {2} = \left(S _ {j k} ^ {\max}\right) ^ {2}\tag{26}
$$

Expanding the first equation and subtracting the second one, gives,

$$
\begin{array}{c} Q _ {j k} = \left(1 / 2 * Q _ {j k 0}\right) \Big [ - 2 P _ {j k} P _ {j k 0} + \left(S _ {j k} ^ {\max}\right) ^ {2} \\ + P _ {j k 0} ^ {2} + Q _ {j k 0} ^ {2} - S _ {j k 0} ^ {2} \Big ] \end{array}\tag{27}
$$

Defining

$$
- \mathrm{Mo} ^ {2} = P _ {j k 0} ^ {2} + Q _ {j k 0} ^ {2} - S _ {j k 0} ^ {2}\tag{28}
$$

we have,

$$
Q _ {j k} = \left(1 / 2 * Q _ {j k 0}\right) \left[ - 2 P _ {j k} P _ {j k 0} + \left(S _ {j k} ^ {\max}\right) ^ {2} - \mathrm{Mo} ^ {2} \right]\tag{29}
$$

Substituting this into Eq. 26 gives for the solutionŽ . of $P _ { j k } ^ { * }$

$$
\left(P _ {j k 0} ^ {2} + Q _ {j k 0} ^ {2}\right) P _ {j k} ^ {* 2} - P _ {j k 0} \left(\left(S _ {j k} ^ {\max}\right) ^ {2} - \mathrm{Mo} ^ {2}\right) P _ {j k} ^ {*}
$$

$$
+ \left[ \left(S _ {j k} ^ {\max}\right) ^ {2} - \mathrm{Mo} ^ {2} \right] ^ {2} / 4 - Q _ {j k 0} ^ {2} \left(S _ {j k} ^ {\max}\right) ^ {2} = 0\tag{30}
$$

This is a quadratic equation in $P _ { j k } ^ { * }$ . Defining:

$$
A = \left(P _ {j k 0} ^ {2} + Q _ {j k 0} ^ {2}\right)\tag{31}
$$

$$
B = - P _ {j k 0} \left(\left(S _ {j k} ^ {\max}\right) ^ {2} - \mathrm{Mo} ^ {2}\right)\tag{32}
$$

$$
C = \left[ \left(S _ {j k} ^ {\max}\right) ^ {2} - \mathrm{Mo} ^ {2} \right] ^ {2} / 4 - Q _ {j k 0} ^ {2} \left(S _ {j k} ^ {\max}\right) ^ {2}\tag{33}
$$

we obtain:

$$
P _ {j k} ^ {*} = \left[ - B \pm (B ^ {2} - 4 A C) ^ {1 / 2} \right] / 2 A\tag{34}
$$

and

$$
Q _ {j k} ^ {*} = \left[ \left(S _ {j k} ^ {\max}\right) ^ {2} - P _ {j k} ^ {* 2} \right] ^ {1 / 2}\tag{35}
$$

The solution of the system of Eqs. 23 and 24 , Ž . Ž . given by Eqs. 34 and 35 is graphically interpreted Ž . Ž . in Fig. 5. Consider $( P _ { j k } ^ { 0 } , Q _ { j k } ^ { 0 } )$ as the initial operating point for the complex power flow through the line. Assume that the active power distribution factor relating $P _ { j k }$ and the injection $P _ { i } ,$ , given by $\rho _ { i - s , j k } =$ $\Delta P _ { j k } / \Delta P _ { i } ^ { ' }$ , is positive. Then the increase in injection $\varDelta P _ { i }$ will move the operating point to the right, following the shape of the operating circle. We are interested in estimating $\Delta P _ { j k } ^ { * }$ , i.e, the variation over the $P _ { j k }$ –coordinate that drives the operating point to $( P _ { j k } ^ { * } , \dot { Q } _ { j k } ^ { * } )$

![](/api/attachments/FTKDDAVH/fulltext/images/2c1f9b9f952e78f45201b394a13791bb2db0b9556d212b438d9b050496291c97.jpg)  
Fig. 5. Graphic interpretation of quadratic solutions.

The solution is characterized as follows:

Ž .a The intersection of the circles is located at two operating points.

Ž . b The solution of the quadratic system of equations results in four pairs of points $( P _ { j k } ^ { * } , Q _ { j k } ^ { * } )$ . Two of them the intersections represent real solutions.Ž . Ž .c We are interested in just one point, the one corresponding to the current direction of the distribution factor.

The required solution to the system of equations can be identified from the four values obtained by taking into account the direction of the distribution factor and the initial operating point over the operating circle.

## 3.2. ATC computation

Now, let the initial complex power flow through the line j–k Ž . at j be given by

$$
P _ {j k} ^ {0} + j Q _ {j k} ^ {0}\tag{36}
$$

as a result of a power flow for the given initial condition. These values represent the initial operating $P { - } Q$ point for the line $j { - } k .$ . The change in active power flow through the line necessary to reach the line MVA limit is then given by:

$$
\Delta P _ {j k} ^ {*} = P _ {j k} ^ {*} - P _ {j k} ^ {0}\tag{37}
$$

Where $P _ { j k } ^ { * }$ is calculated either by Eq. 20 for theŽ . short model of the line, or by Eq. 34 for theŽ . -model. Using Eq. 15 :Ž .

$$
\Delta P _ {i} ^ {* j k} = \Delta P _ {j k} ^ {*} / \rho_ {i - s, j k}\tag{38}
$$

This value represents the maximum transaction that can be allocated between bus i and s so that line $j { - } k$ does not become overloaded. As none of the lines in the system can operate overloaded, the computation must identify the minimum $\varDelta P _ { i } ^ { * j k }$ for all $j { - } k$ lines.

This is the maximum feasible allocation i.e., the ATC considering thermal limit constraints:

$$
\mathrm{ATC} _ {i - s} ^ {\text { thermal }} = \min \left\{\Delta P _ {i} ^ {* j k} \text {   among   all   } j - k \text {   lines } \right\}\tag{39}
$$

## 3.3. Determination of unfeasible cases

Now consider Fig. 6, which shows a typical operating circle and limiting circles for two different cases of line MVA ratings.

Suppose that the state of the system is such that the initial complex flow of line $j { - } k$ at side j is $( P _ { j k } ^ { 0 } ;$ $Q _ { j k } ^ { 0 } )$ , and corresponds to point A in the figure. Let the limit of the line flow be given by the limiting circle I. Now assume that due to a large transaction, the magnitude of the active power flowing through the line is increased. Therefore, the operating point is going to move along the operating circle until the line hits its limit at point B.

Now suppose that limiting circle II represents the line rating. Then, due to the transaction, the operating point is going to continue moving along the operating circle, until it reaches point C. There, no more active power can flow through the line regardless of the amount of reactive power assumingŽ voltages are held constant . At point C the system . collapses and therefore, the operating point cannot reach the intersection of the circles at point D.

Point C is the limit of steady state stability for the transfer of active power through line $j { - } k .$ , for voltages $V _ { j }$ and $V _ { k }$ constant. Using Eqs. 5 and 6 , theŽ . Ž . coordinates of point C are given by:

![](/api/attachments/FTKDDAVH/fulltext/images/2ff371ae04391d37e5778b5ea7ba5c9ce7bfa65ca457f0392246ad66f283c444.jpg)  
Fig. 6. Interpretation of unfeasible cases.

$$
\left(V _ {j} V _ {k} Y _ {j k}, V _ {j} ^ {2} Y _ {j k}\right)\tag{40}
$$

Note that point C will be reached before the thermal limit of the line if it is located inside the limiting circle. This condition is expressed in the following way:

$$
\left[ \left(V _ {j} V _ {k} Y _ {j k}\right) ^ {2} + \left(V _ {j} ^ {2} Y _ {j k}\right) ^ {2} \right] ^ {1 / 2} <   S _ {j k} ^ {\max}\tag{41}
$$

In order to include this consideration in the algorithm, suppose that the ATC for a transaction between bus i and bus s is to be evaluated. Then, Eq. Ž . 41 must be tested for each line j–k in order to determine if the power transfer limit could be reached before the thermal limit of a line.

Ž . If condition 41 is violated, we must set $P _ { j k } ^ { * }$ and $Q _ { j k } ^ { * }$ for line j–k as:

$$
P _ {j k} ^ {*} = V _ {j} V _ {k} Y _ {j k}\tag{42}
$$

$$
Q _ {j k} ^ {*} = V _ {j} ^ {2} Y _ {j k}\tag{43}
$$

And we compute the maximum complex flows $P _ { j k } ^ { * }$ and $Q _ { j k } ^ { * }$ for the rest of the lines as explained in Section 3.1 and ATC as explained in Section 3.2. However, as it could be very dangerous to operate the system near the power transfer limit, it is convenient to reduce $P _ { j k } ^ { * }$ by a security margin for those lines where condition 41 was violated.Ž .

Furthermore, it may be desirable to estimate the proximity to a stability limit in each line, even when other lines could be slightly overloaded. This would require the determination of $P _ { j k } ^ { * }$ and $Q _ { j k } ^ { * }$ as in Section 3.1 for every line, and then the test of the following condition:

$$
P _ {m n} ^ {*} \left(\rho_ {i - s, j k} / \rho_ {i - s, m n}\right) <   V _ {j} V _ {k} Y _ {j k}\tag{44}
$$

for every line m–n and every line j–k. In this equation, the value $P _ { m n } ^ { * } ( \rho _ { i - s , j k } / \rho _ { i - s , m n } )$ represents the actual power that will flow through line $j - k , \ : P _ { j k }$ when line m–n is at its thermal limit. This value is compared with the active power coordinate of the transfer limit of line j–k. If condition 44 is applica-Ž . ble to a pair of lines j–k and m–n, this means that the power transfer limit of line $j { - } k$ is reached before the thermal limit of line m–n.

These considerations must be taken into account in the computation of ATC. Note that this discussion has been derived for the short model of the transmission line. If the general model were to be used, then Eqs. 40 and 41 would be replaced by the follow- Ž . Ž . ing expression:

$$
\left(- V _ {j} ^ {2} G _ {j k} + V _ {j} V _ {k} Y _ {j k}, - V _ {j} ^ {2} B _ {j j} - V _ {j} ^ {2} B _ {j k}\right)\tag{45}
$$

$$
\left[ \left(- V _ {j} ^ {2} G _ {j k} + V _ {j} V _ {k} Y _ {j k}\right) ^ {2} + \left(- V _ {j} ^ {2} B _ {j j} - V _ {j} ^ {2} B _ {j k}\right) ^ {2} \right] ^ {1 / 2}\tag{46}
$$

In this case, as the origin of the operating circle is displaced from the Q-axis, each equation must be tested for two values.

## 4. Case examples

## 4.1. 3-bus reactiÕe system

The computation was tested in the 3-bus system shown in Fig. 7.

The case was set up as follows:

Ž .a Voltages are set at 1.0, 1.0 and 1.04 pu for buses 1, 2 and 3, respectively. During the transaction, voltages are regulated and the reactive support is unlimited.

Ž . b The reactances of the transmission lines are 0.9, 0.28 and 0.37 for lines 1–2, 2–3 and 1–3, respectively.

Ž .c The initial operating point is as shown in Fig. 7.

Ž . d All possible transactions were simulated, i.e., between areas 1 to 2, 1 to 3 and 2 to 3, as selling and buying areas.

ATC was computed by the following three methods.

Ž .a The Active Power Linear ATC is computed by the classical method. In this case the MVA limit is reached through the use of active power distribution factors computed experimentally as sensitivities . Ž .

![](/api/attachments/FTKDDAVH/fulltext/images/2416e067d3df02f1dd081f3cc3f6f5208ee9e2f8ab6ea2d161d0953b7c4cbfe8.jpg)  
Fig. 7. 3-bus system base case.

Reactive power<sup>r</sup>voltage considerations are neglected. For this case:

$$
\mathrm{ATC} _ {i - s} ^ {\text { thermal }} = \min \left\{\Delta P _ {i} ^ {* j k} \text {   among   all   } j k \text {   lines } \right\}\tag{47}
$$

where the necessary injection change is approximated as:

$$
\Delta P _ {i} ^ {* j k} \cong \left(S _ {j k} ^ {\max} - S _ {j k} ^ {\mathrm{o}}\right) / \rho_ {i - s, j k}\tag{48}
$$

Ž . b Reactive Power Linear ATC is computed as described in Section 3 of this paper.

Ž .c Finally, the actual ATC is calculated using full AC power flow. For each transaction, the generation is increased in each area until each of the lines atŽ each side reaches its MVA limit, and the necessary . injection is determined this point. These values are considered as the reference for the calculation of errors obtained with methods a and b .Ž . Ž .

## 4.1.1. Results

The results are shown in per unit $( S _ { \mathrm { b a s e } } = 1 0 0 $ MVA in Table 1. Corresponding errors are com- . puted for methods a and b with respect to theŽ . Ž . actual ATC values.

The results presented in Table 1 show the information corresponding to ATC values for transactions between areas 1–2, 1–3 and 2–3, respectively.

For each type of transaction, the results obtained by each method of computation for $P ^ { * }$ are presented. ATC is the minimum quantity among the values of $P ^ { * }$ for that transaction. ATC results are shown in bold. For example, for the transaction between areas 1 and 2 injection at 1 , the limiting Ž . line is identified as line 3-1 side 3 , which reachesŽ . its thermal limit with an injection of 2.03 p.u., or 203 MW at bus 1. This corresponds to the actual ATC value for that transaction.

Comparing the results obtained by different methods, ATC is determined by the linear method with an error of 5.85%, 5.22% and 6.04% for transactions between areas 1–2, 1–3 and 2–3, respectively. Including reactive power results in errors of 0.73%, 0.13% and 1.63%, correspondingly.

The magnitude of the errors for the values of $\Delta P ^ { * }$ is consistent in the two methods. It is noticed that for large values of $\Delta P ^ { * }$ , the errors tend to increase in both methods. The last column of the table demonstrates however how the error obtained with Active Power Linear ATC is consistently reduced using the reactive power approach.

Cells tagged as AUnst.B correspond to cases were a steady-state stability limit was reached before a thermal limit. For example, for a transaction between area 1 and 3, line 2–3 is never thermally limited, as the power transfer limit of 1–3 is reached first. In this computation, the combinatorial approach determined by Eq. 44 was used. As it can be seen, theŽ . reactive power approach correctly identifies these unfeasible cases. The linear approach does not consider this issue and the corresponding cell is tagged as non-available NŽ . <sup>r</sup>A .

Table 1 ATC results for the 3-bus system

<table><tr><td colspan="4">Transaction</td><td>Actual</td><td colspan="2">Linear</td><td colspan="2">Reactive</td></tr><tr><td>S/B</td><td>Line</td><td> $\rho_{i-s,jk}(-)$ </td><td>Rating (p.u.)</td><td> $\Delta P^{*}$ (p.u.)</td><td> $\Delta P^{*}$ (p.u.)</td><td>Error (%)</td><td> $\Delta P^{*}$ (p.u.)</td><td>Error (%)</td></tr><tr><td rowspan="6">1-2</td><td>1-2</td><td>0.395</td><td>1.00</td><td>2.330</td><td>2.53</td><td>8.65</td><td>2.261</td><td>-2.97</td></tr><tr><td>2-1</td><td>-0.395</td><td>1.00</td><td>2.330</td><td>2.53</td><td>8.65</td><td>2.261</td><td>-2.97</td></tr><tr><td>1-3</td><td>0.605</td><td>1.30</td><td>2.110</td><td>2.15</td><td>1.84</td><td>2.123</td><td>0.60</td></tr><tr><td>3-1</td><td>-0.605</td><td>1.30</td><td>2.030</td><td>2.15</td><td>5.85</td><td>2.045</td><td>0.73</td></tr><tr><td>2-3</td><td>-0.605</td><td>1.40</td><td>2.270</td><td>2.31</td><td>1.94</td><td>2.304</td><td>1.51</td></tr><tr><td>3-2</td><td>0.605</td><td>1.40</td><td>2.190</td><td>2.31</td><td>5.66</td><td>2.218</td><td>1.27</td></tr><tr><td rowspan="6">1-3</td><td>1-2</td><td>0.242</td><td>1.00</td><td>3.490</td><td>4.13</td><td>18.40</td><td>3.690</td><td>5.74</td></tr><tr><td>2-1</td><td>-0.242</td><td>1.00</td><td>3.490</td><td>4.13</td><td>18.40</td><td>3.690</td><td>5.74</td></tr><tr><td>1-3</td><td>0.758</td><td>1.30</td><td>1.690</td><td>1.72</td><td>1.48</td><td>1.694</td><td>0.24</td></tr><tr><td>3-1</td><td>-0.758</td><td>1.30</td><td>1.630</td><td>1.72</td><td>5.22</td><td>1.632</td><td>0.13</td></tr><tr><td>2-3</td><td>0.242</td><td>1.40</td><td>Unst</td><td>5.79</td><td>N/A</td><td>Unst.</td><td>-</td></tr><tr><td>3-2</td><td>-0.242</td><td>1.40</td><td>Unst</td><td>5.79</td><td>N/A</td><td>Unst.</td><td>-</td></tr><tr><td rowspan="6">2-3</td><td>1-2</td><td>-0.190</td><td>1.00</td><td>4.430</td><td>5.26</td><td>18.81</td><td>4.700</td><td>6.10</td></tr><tr><td>2-1</td><td>0.190</td><td>1.00</td><td>4.430</td><td>5.26</td><td>18.81</td><td>4.700</td><td>6.10</td></tr><tr><td>1-3</td><td>0.190</td><td>1.30</td><td>Unst</td><td>6.84</td><td>N/A</td><td>Unst.</td><td>-</td></tr><tr><td>3-1</td><td>-0.190</td><td>1.30</td><td>Unst</td><td>6.84</td><td>N/A</td><td>Unst.</td><td>-</td></tr><tr><td>2-3</td><td>0.810</td><td>1.40</td><td>1.700</td><td>1.73</td><td>1.67</td><td>1.721</td><td>1.24</td></tr><tr><td>3-2</td><td>-0.810</td><td>1.40</td><td>1.630</td><td>1.73</td><td>6.04</td><td>1.657</td><td>1.63</td></tr></table>

Note that in this case, the equations for the simple transmission line model were used. These are exact equations for the case system. Also, voltages are held constant and therefore the error introduced in the computation corresponds to considering constant active-power distribution factors. The computation error obtained using the reactive power approach is due only to this fact.

## 4.2. 7-Bus full system

The influence of voltage changes in PQ-buses, inclusion of the general transmission-line model and changes in the distribution factors was analyzed in the 7-bus system shown in Fig. 8.

The system to be simulated has three areas, A, B and C. A transaction between area B and area A was investigated. The selling point is bus 6 injectionŽ . and bus 4 is the buying point extraction . TheŽ .

computation was performed using the three methods previously explained.

The system has the following characteristics:

Ž .a Transmission line parameters are given in Table 2.

Ž . b Voltages are regulated; no reactive power generation limits are considered.

Ž .c Initial operating conditions are as shown in Fig. 8.

## 4.2.1. Results

The results for ATC evaluations are shown in Table 3 for the most limiting lines.

The actual value for ATC was determined as 0.7 p.u. 70 MW injection at bus 6. Line 4-2 side 4 is Ž . Ž . the most limiting line in this case. Whereas the Reactive Power Linear approach gives a very close result of 0.69 p.u., the Linear approach is unable to correctly identify the limiting side of the line and gives a considerable error in the computation. For other limiting lines, the errors are consistently reduced using the reactive power approach.

![](/api/attachments/FTKDDAVH/fulltext/images/edee741b68d73540695b0ffec7f660add088c7dad4bdfb35afeacbb535f4d682.jpg)  
Fig. 8. 7-bus system.

The errors obtained for line 2–6 with the linear method are due to the large change in reactive power derived from the change in the active power injection.

The final condition of the system is shown in Fig. 9 where the largest feasible transaction has been already committed.

## 5. Additional considerations

## 5.1. Implementation

The main objective of including reactive power in ATC is to enhance the identification and estimation of the maximum secure transaction that can be committed between nodes of a system. Reactive Power Linear ATC tends to reduce the error in the estimated values, but also increases the computational requirements.

Fig. 10 shows the algorithm for the computation with all the required equations.

It is very important to notice that given an initial operating condition of the system, the computation of the maximum complex flows step 1 to 4 is Ž . performed only once. Then in step 5, ATC could be performed for any transaction between any pair of buses i <sup>y</sup> s, by only applying the set of Eqs. 37 –Ž . Ž . 39 once. This is the same requirement used in Linear Active Power ATC, which also requires step 1. Therefore, the increase in computational time is given by applying steps 2, 3 and 4 only once.

Table 2  
Line parameters for the 7-bus system

<table><tr><td>Lines</td><td></td><td>R (p.u.)</td><td>X (p.u.)</td><td>C (p.u.)</td><td>MVA</td></tr><tr><td>From</td><td>To</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>2</td><td>0.020</td><td>0.060</td><td>0.010</td><td>170</td></tr><tr><td>1</td><td>3</td><td>0.060</td><td>0.240</td><td>0.020</td><td>130</td></tr><tr><td>2</td><td>3</td><td>0.040</td><td>0.180</td><td>0.020</td><td>130</td></tr><tr><td>2</td><td>4</td><td>0.060</td><td>0.180</td><td>0.030</td><td>100</td></tr><tr><td>2</td><td>5</td><td>0.040</td><td>0.120</td><td>0.020</td><td>100</td></tr><tr><td>2</td><td>6</td><td>0.030</td><td>0.060</td><td>0.020</td><td>160</td></tr><tr><td>3</td><td>4</td><td>0.010</td><td>0.030</td><td>0.010</td><td>200</td></tr><tr><td>4</td><td>5</td><td>0.080</td><td>0.240</td><td>0.060</td><td>100</td></tr><tr><td>7</td><td>5</td><td>0.020</td><td>0.060</td><td>0.020</td><td>120</td></tr><tr><td>6</td><td>7</td><td>0.080</td><td>0.240</td><td>0.040</td><td>80</td></tr><tr><td>6</td><td>7</td><td>0.080</td><td>0.240</td><td>0.040</td><td>80</td></tr></table>

Table 3  
Results for the 7-bus system. Transaction 6–4

<table><tr><td colspan="3">Transaction</td><td>Actual</td><td colspan="2">Linear</td><td colspan="2">Reactive</td></tr><tr><td>Line (-)</td><td> $\rho_{i-s,jk}(-)$ </td><td>Rating (p.u.)</td><td> $\Delta P^{*}$ (p.u.)</td><td> $\Delta P^{*}$ (p.u.)</td><td>Error (%)</td><td> $\Delta P^{*}$ (p.u.)</td><td>Error (%)</td></tr><tr><td>4-2</td><td>-0.294</td><td>1.00</td><td>0.70</td><td>0.77</td><td>9.82</td><td>0.690</td><td>1.38</td></tr><tr><td>2-4</td><td>0.326</td><td>1.00</td><td>0.72</td><td>0.70</td><td>-2.86</td><td>0.716</td><td>0.54</td></tr><tr><td>6-2</td><td>0.740</td><td>1.60</td><td>1.04</td><td>0.89</td><td>-14.76</td><td>1.043</td><td>-0.25</td></tr><tr><td>2-3</td><td>0.253</td><td>1.20</td><td>1.12</td><td>1.11</td><td>-1.19</td><td>1.118</td><td>0.17</td></tr><tr><td>2-6</td><td>-0.713</td><td>1.60</td><td>1.13</td><td>0.97</td><td>-14.24</td><td>1.128</td><td>0.20</td></tr><tr><td>3-2</td><td>-0.235</td><td>1.20</td><td>1.24</td><td>1.28</td><td>2.95</td><td>1.217</td><td>1.89</td></tr><tr><td>6-7</td><td>0.130</td><td>0.80</td><td>2.73</td><td>2.58</td><td>-5.33</td><td>2.694</td><td>1.32</td></tr><tr><td>7-5</td><td>0.252</td><td>1.20</td><td>2.31</td><td>2.14</td><td>-7.41</td><td>2.267</td><td>1.88</td></tr></table>

An important fact about this type of computations is that it determines the reactive power influence in the system by means of active power distribution factors and system parameter information. Therefore, the subroutine could be easily incorporated in any ATC program based on active power distribution factors.

## 5.2. Limitations of the reactiÕe power approach

Eq. 39 gives an estimation of the ATC for aŽ . transaction between buses i and s. However, there are a number of approximations of the real system that were made in the process:

Ž .a Even with unlimited reactive power supply, the magnitude of the voltages for PQ buses will change during the transaction. This will also happen in the PV buses if we consider the limits in the generation of reactive power.

Ž . b The active power distribution factors are good approximations to the power distribution, but are not constant even when voltages at the PV buses can be maintained. Their behavior is worst in

![](/api/attachments/FTKDDAVH/fulltext/images/3fd390f22f1c0a22b747bef1bf9c7e647ecfa9cccf47d05eac0da5a1e30eb5a4.jpg)  
Fig. 9. Final condition for the 7-bus system.

![](/api/attachments/FTKDDAVH/fulltext/images/310815d3060c6a520a52a9838c6fdf114514faacaf5a02fe5f8e923081f3644e.jpg)

(42)

(43)

## 4. COMPUTE MAXIMUM COMPLEX FLOWS

For all j-k feasible lines, sending & receiving ends:

$$
\left(\mathrm{P} _ {\mathrm{jk0}}, \mathrm{Q} _ {\mathrm{jk0}}\right) = \left(\mathrm{V} _ {\mathrm{j}} ^ {2} \mathrm{G} _ {\mathrm{jk}}, - \mathrm{V} _ {\mathrm{j}} ^ {2} \mathrm{B} _ {\mathrm{jj}} - \mathrm{V} _ {\mathrm{j}} ^ {2} \mathrm{B} _ {\mathrm{jk}}\right)\tag{13}
$$

$$
\mathrm{S} _ {\mathrm{jk0}} = \mathrm{V} _ {\mathrm{j}} \mathrm{V} _ {\mathrm{k}} \mathrm{Y} _ {\mathrm{jk}}.\tag{14}
$$

$$
- \mathrm{Mo} ^ {2} = \mathrm{P} _ {\mathrm{jk0}} ^ {2} + \mathrm{Q} _ {\mathrm{jk0}} ^ {2} - \mathrm{S} _ {\mathrm{jk0}} ^ {2}\tag{28}
$$

$$
\mathrm{A} = \left(\mathrm{P} _ {\mathrm{jk0}} ^ {2} + \mathrm{Q} _ {\mathrm{jk0}} ^ {2}\right)\tag{31}
$$

$$
\mathrm{B} = - \mathrm{P} _ {\mathrm{jk0}} \left(\left(\mathrm{S} _ {\mathrm{jk}} ^ {\max}\right) ^ {2} - \mathrm{Mo} ^ {2}\right)\tag{32}
$$

$$
\mathrm{C} = \left[ \left(\mathrm{S} _ {\mathrm{jk}} ^ {\max}\right) ^ {2} - \mathrm{Mo} ^ {2} \right] ^ {2} / 4 - \mathrm{Q} _ {\mathrm{jk0}} ^ {2} \left(\mathrm{S} _ {\mathrm{jk}} ^ {\max}\right) ^ {2}\tag{33}
$$

$$
\mathrm{P} _ {\mathrm{jk}} ^ {*} = \left[ - \mathrm{B} \pm \left(\mathrm{B} ^ {2} - 4 \mathrm{AC}\right) ^ {1 / 2} \right] / 2 \mathrm{A}\tag{34}
$$

$$
Q _ {j k} ^ {*} = \left[ \left(S _ {j k} ^ {\max}\right) ^ {2} - P _ {j k} ^ {* 2} \right] ^ {1 / 2}\tag{35}
$$

## 5. COMPUTE ATC

For all j-k lines and ends, for all i-s transactions

$$
\Delta \mathrm{P} _ {\mathrm{jk}} ^ {*} = \mathrm{P} _ {\mathrm{jk}} ^ {*} - \mathrm{P} _ {\mathrm{jk}} ^ {0}\tag{37}
$$

$$
\Delta \mathrm{P} _ {\mathrm{i}} ^ {* \mathrm{jk}} = \Delta \mathrm{P} _ {\mathrm{jk}} ^ {*} / \rho_ {\mathrm{i-s,jk}}\tag{38}
$$

$$
\mathrm{ATC} _ {\mathrm{i-s}} ^ {\text { thermal }} = \min \left\{\Delta \mathrm{P} _ {\mathrm{i}} ^ {* j k} \text { among   all   j - k.   lines } \right\}\tag{39}
$$

![](/api/attachments/FTKDDAVH/fulltext/images/6796c0ffe8706bbb1dfd9a5da8735c90c30cf7430e38c651687e9ea7091c0ac1.jpg)  
Fig. 10. Computation of reactive power linear ATC.

systems with large flows of reactive power through the transmission system.

Several enhancements to the described approach could be obtained, especially if there is some a priori knowledge about the behavior of the voltage during the transaction.

## 5.3. ReactiÕe power support

The transmission-line circle parameters and equations have additional information that could be exploited in an integrated simulation environment. From Eq. 25 , the reactive power flow through lineŽ . $j { - } k$ at side j, is given by:

$$
Q _ {j k} = Q _ {j k 0} + \left[ S _ {j k 0} ^ {2} - \left(P _ {j k} - P _ {j k 0}\right) ^ {2} \right\} ^ {1 / 2}\tag{49}
$$

This equation is valid for every line complex power flow if the voltages remain constant or approxi- Ž mately constant . In the same manner, for a variation. in power:

$$
\begin{array}{l} \Delta Q _ {j k} = Q _ {j k 0} - Q _ {j k} ^ {0} \\ \qquad + \left[ S _ {j k 0} ^ {2} - \left(\Delta P _ {j k} + \Delta P _ {j k} ^ {0} - P _ {j k 0}\right) ^ {2} \right] ^ {1 / 2} \end{array}\tag{50}
$$

Noting that $\varDelta P _ { j k } = \rho _ { i - s , j k } \ \varDelta P _ { i } ,$ , we have:

$$
\begin{array}{l} \Delta Q _ {j k} = Q _ {j k 0} - Q _ {j k} ^ {0} \\ \qquad + \left[ S _ {j k 0} ^ {2} - \left(\rho_ {i - s, j k} \Delta P _ {i} + \Delta P _ {j k} ^ {0} - P _ {j k 0}\right) ^ {2} \right] ^ {1 / 2} \end{array}\tag{51}
$$

And because the variation in the reactive power injection at a PV bus j equals the summation of the reactive power flows on the transmission lines andŽ static compensators connected to that bus, we have. that $\Delta Q _ { j } = \Sigma _ { k } \ \varDelta Q _ { j k }$ . Therefore,

$$
\begin{array}{l} Q _ {j} = Q _ {j} ^ {0} + \Sigma_ {k} \Big \{Q _ {j k 0} - Q _ {j k} ^ {0} \\ \qquad + \left[ S _ {j k 0} ^ {2} - \Big (\rho_ {i - s, j k} \Delta P _ {i} + \Delta P _ {j k} ^ {0} - P _ {j k 0} \Big) ^ {2} \right] ^ {1 / 2} \Big \} \end{array}\tag{52}
$$

where the summation is performed over all k lines connected to bus j.

Note that as a result of the ATC computation, all terms in Eq. 52 are known, except the variation in Ž . the active power injection $\varDelta P _ { i }$ , which is the independent variable.

Eq. 52 allows us to estimate the necessary reac- Ž . tive support requirements for a transaction between buses i and s, at any PV bus $j .$ Furthermore, under the assumption that voltages will remain approximately constant, this equation would be applicable to any amount of the transaction $\varDelta P _ { i }$ . It consequently represents an equation for the reactive power injection due to large variations in active power.

## 6. Conclusions

The results obtained in this paper show that the inclusion of reactive power in a linear ATC can reduce the errors in the estimation of the maximum transaction over a transmission system. It also provides a way to estimate the proximity to steady state stability limits due to a transaction.

The computation could be efficiently implemented in linear ATC programs, without a considerable increase in computer requirements.

Extensive test on large scale systems should be performed with the inclusion of reactive power in order to determine the convenience of using Reactive Power Linear ATC for operating purposes.

## Acknowledgements

This work was supported in part by funds from National Science Foundation Grant NSF EEC 96- 15792, the University of Illinois Power Affiliates Program, the Grainger endowments to the University of Illinois, Power Systems Engineering Research Center PSERC subcontracts from Cornell Univer-Ž . sity, and The Fulbright Commission.

## References

<sup>w</sup> <sup>x</sup> 1 P.M. Andersen, A. Bose, A probabilistic approach to power system stability analysis, IEEE Transactions on Power Apparatus and Systems 1983 2430–2439, August.Ž .

<sup>w</sup> <sup>x</sup> 2 S. Ahmed-Zaid, W. Sauer, Optimal system loadability, Proc. 1981 Midwest Power Symposium, University of Illinois at Urbana-Champaign, Urbana, IL, 1981, pp. 1–10, Sec. 3.1, October 15–16.

<sup>w</sup> <sup>x</sup> 3 H.D. Chiang, The BCU method for direct stability analysis of electric power systems: theory and applications, IMA Series, Systems and Control Theory for Power Systems, vol. 64, Springer Verlag, 1995, pp. 39–94.

<sup>w</sup> <sup>x</sup> 4 I. Dobson, L. Lu, Computing an optimum direction in control space to avoid saddle node bifurcation and voltage collapse in electric power systems, IEEE Transactions on Automatic Control 37 10 1992 1616–1620, October.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 R.D. Dunlop, R. Gutman, P. Marchenko, Analytical development of loadability characteristics for EHV and UHV transmission Lines, IEEE Transactions on Power Apparatus and Systems PAS-98 2 1979 606–617, MarchŽ . Ž . <sup>r</sup>April.

<sup>w</sup> <sup>x</sup> 6 L.L. Garver, P.R. Van Horne, K.A. Wirgau, Load supplying capability of generation–transmission networks, IEEE Transactions on Power Apparatus and Systems PAS-98 3 1979Ž . Ž . 957–962, May<sup>r</sup>June.

<sup>w</sup> <sup>x</sup> 7 G.T. Heydt, B.M. Katz, A stochastic model in simultaneous interchange capacity calculations, IEEE Transactions on Power Apparatus and Systems PAS-94 2 1975 350–359,Ž . Ž . March<sup>r</sup>April.

<sup>w</sup> <sup>x</sup> 8 T.W. Kay, P.W. Sauer, R.D. Shultz, R.A. Smith, EHV and UHV loadability dependence on VAR supply capability, IEEE Transactions on Power Apparatus and Systems PAS-101 9 1982 3568–3575, September.Ž . Ž .

<sup>w</sup> <sup>x</sup>9 G.L. Landgren, S.W. Anderson, Simultaneous power interchange capability analysis, IEEE Transactions on Power Apparatus and Systems PAS-92 6 1973 1973–1986,Ž . Ž . Nov<sup>r</sup>Dec.

<sup>w</sup> <sup>x</sup> 10 G.L. Landgren, H.L. Terhune, R.K. Angel, Transmission interchange capability — analysis by computer, IEEE Transactions on Power Apparatus and Systems PAS-91 6 1972Ž . Ž . 2405–2414, Nov<sup>r</sup>Dec.

<sup>w</sup> <sup>x</sup> 11 P.W. Sauer, On the formulation of power distribution factors for linear load flow methods, IEEE Transactions on Power Apparatus and Systems PAS-100 2 1981 764–770, Febru- Ž . Ž . ary.

<sup>w</sup> <sup>x</sup> 12 P.W. Sauer, Technical challenges of computing available transfer capability ATC in electric power systems, Proceed- Ž . ings of the Thirtieth Annual 1997 Hawaii InternationaŽ . Conference on System Sciences, Maui, Hawaii, January 7–10, vol. V, 1997, pp. 589–593.

<sup>w</sup> <sup>x</sup> 13 P.W. Sauer, Alternatives for calculating Transmission Reliability Margin TRM in Available Transfer Capability ATC ,Ž . Ž . Proceedings of the Thirty-First Annual 1998 Hawaii Inter-Ž . national Conference on System Sciences, Kona, Hawaii, January 6–9, vol. III, 1998, p. 89.

<sup>w</sup> <sup>x</sup> 14 P.W. Sauer, K.D. Demaree, M.A. Pai, Stability limited load supply and interchange capability, IEEE Transactions on Power Apparatus and Systems PAS-102 11 1983 3637–Ž . Ž . 3643, November.

<sup>w</sup> <sup>x</sup> 15 P.W. Sauer, R.J. Evans Jr., M.A. Pai, Maximum unconstrained loadability of power systems, Proceedings 1990 IEEE International Symposium on Circuits and Systems, 90 CH 2868-8, New Orleans, LA, May 1–3, 1990, pp. 1818– 1821.

<sup>w</sup> <sup>x</sup> 16 P.W. Sauer, B.C. Lesieutre, M.A. Pai, Maximum loadability and voltage stability in power systems, International Journal of Electrical Power and Energy Systems 15 3 1993 Ž . Ž . 145–154.

<sup>w</sup> <sup>x</sup> 17 H.P. St. Clair, Practical concepts in capability and performance of transmission lines, AIEE Transactions 72 1953Ž . 1152–1157, Part III, December.

<sup>w</sup> <sup>x</sup> 18 B. Stott, J.L. Marinho, Linear programming for power sys-

tem network security applications, IEEE Transactions on Power Apparatus and Systems PAS-98 3 1979 837–848, Ž . Ž . May<sup>r</sup>June.

<sup>w</sup> <sup>x</sup> 19 Transmission Transfer Capability Task Force, Transmission Transfer Capability, North American Electric Reliability Council, Princeton, New Jersey, May 1995.

<sup>w</sup> <sup>x</sup> 20 Transmission Transfer Capability Task Force, Available Transfer Capability Definitions and Determination, North American Electric Reliability Council, Princeton, New Jersey, June 1996.

<sup>w</sup> <sup>x</sup> 21 Union Electric, Simultaneous Transfer Capability: Direction for Software Development, EPRI Report EL-7351, Project 3140-1, Electric Power Research Institute, Palo Alto, CA, August 1991.

![](/api/attachments/FTKDDAVH/fulltext/images/3c0b124e3dc759be972cad2f646e13cc43bf6013b543fb2d2de6ba8d74408f01.jpg)

Peter W. Sauer obtained his Bachelor of Science degree in Electrical Engineering from the University of Missouri at Rolla in 1969, the Master of Science and PhD degrees in Electrical Engineering from Purdue University in 1974 and 1977, respectively. From 1969 to 1973, he was the electrical engineer on a design assistance team for the Tactical Air Command at Langley Air Force Base, Virginia, working on design and construction of airfield lighting and electrical

distribution systems. He has been on the faculty at Illinois since 1977 where he teaches courses and directs research on power systems and electric machines. His main interests are in modeling and simulation of power system dynamics with applications to steady-state and transient stability analysis. From August 1991 to August 1992 he served as the Program Director for Power Systems in the Electrical and Communication Systems Division of the National Science Foundation in Washington D.C. He is the Chairman of the IEEE Power Engineering Society PES WorkingŽ . Group on Dynamic Security Assessment, and Chairman of the IEEE Central Illinois Chapter of PES. He is a registered Professional Engineer in Virginia and Illinois and a Fellow of the IEEE.

![](/api/attachments/FTKDDAVH/fulltext/images/4886b7f26b0e78dacaa772aaf4a3a5ef95eeb7683c871eb0caacbc1ce96451b1.jpg)

Santiago Grijalva was born in Quito-Ecuador in November 1970. He received the Engineer Degree from the National Polytechnic University-Ecuador in 1994, and the MSc Diploma from the Army Polytechnic University-Ecuador in 1997, in Electrical Engineering and Information Systems, respectively. Since 1995 he worked as EMS Engineer and then as Head of the Software Department in the Ecuadorian National Center of Energy Control, on mainte-

nance and development of real-time SCADA-EMS systems. By means of a Fulbright Fellowship, he is currently a Graduate Student and a Research Assistant at the University of Illinois at Urbana-Champaign. His interests are concentrated in power system control and operation, real-time power applications, and information systems.
