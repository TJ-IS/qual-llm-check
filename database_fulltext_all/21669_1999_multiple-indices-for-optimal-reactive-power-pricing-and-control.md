---
otero_id: 21669
otero_key: "4YF29FSM"
title: "Multiple indices for optimal reactive power pricing and control"
authors: "James A. Momoh; Jizhong Zhu"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00076-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multiple indices for optimal reactive power pricing and control

James A. Momoh <sup>)</sup>, Jizhong Zhu <sup>1</sup>

Electrical Engineering Department, Howard UniÕersity, 2300 Sixth Street, N.W., Washington, DC, 20059, USA

## Abstract

An integrated approach for reactive power price and control is developed. Reactive power price is divided into fixed and variable parts. The fixed part is the operational cost of reactive power service. The variable part of reactive power price is determined based on capability and contributions to the improvement of system performance such as security, reliability and economics. These contributions can be evaluated by computing sensitivity of objective function with respect to reactive power support. The optimal power flow OPF approach is used to carry out this purpose. For VAr planning or control Ž . Ž . purposes, three parallel indices are first presented to determine the sites of new VAr sources. They are benefit-to-cost ratio index, voltage reactive sensitivity index, and the bus voltage security index. The analytic hierarchical process is then used to comprehensively consider the effect of the three indices and the network topology for each candidate VAr source site. The proposed approach was tested on an IEEE 30-bus system with satisfactory results. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Reactive power pricing; VAr pricing; VAr control; Competitive environment; Optimal power flow; Cost–benefit analysis; Voltage reactive sensitivity; Bus voltage security; Analytic hierarchical process

## 1. Introduction

A great deal of research on optimal allocation and sizing of VAr sources to improve the system voltage profile and reduce losses has been conducted during the last decade 1–3,9,10,15 . Traditionally, trans-<sup>w</sup> <sup>x</sup> mission customers are charged for reactive power support service based only on the costs of transmission equipment or power factor penalties. In an open-access environment, the transmission system operator will continue to be responsible for coordinating the generation and transmission systems for the reactive power service and control based on a new price mechanism which can reflect the embedded costs incurred by the utilities for wholesale transactions 6,11,12 . Therefore, real-time reactive<sup>w</sup> <sup>x</sup> power pricing addresses the important issue of providing information to both the utility and consumers about the true burden on the system. Real-time reactive power pricing has been shown to perform better than the power factor penalty scheme in terms of providing incentives to all customers to reduce their reactive power consumption irrespective of their power factor 3–6,8 . Ref. 5 proposed an integrated<sup>w</sup> <sup>x</sup> <sup>w x</sup> framework for optimal reactive power planning and spot pricing, in which the selection of VAr source sites is based only on the real power generation operation benefit-to-cost ratio for a capacitor on load bus. However, this study neglects the effect of voltage improvement and system loss decrease in the selection of VAr source sites. In the new competitive environment, VAr pricing and control should be determined by considering voltage, security, transmission loss and economics.

This paper develops a price structure for providing reactive power service and control based on the cost–benefit analysis CBA and OPF approach. InŽ . OPF, the objective function is the minimization of system loss and the solution is the interior point approach. The cost of reactive power support service is determined based on capability and contribution to improvement of system performance including factors such as security, reliability and economics. Contribution or value of reactive support to the system can be evaluated by calculating sensitivity of objec tive function with respect to reactive power support. This sensitivity reflects dollar savings from applying VAr support service and control. The price will be determined based on this dollar-saving and operation cost of VAr service and control. The former is the variable part of VAr pricing, and the latter is the fixed part of VAr pricing.

For VAr planning purpose, costs and sites of reactive power sources must be determined. This paper first presents three parallel indices to determine the sites of new VAr sources. They are benefitto-cost ratio BCR , voltage reactive sensitivity indexŽ . Ž . Ž . VRSI and the bus voltage security index BVSI . Then, an analytic hierarchical process AHP modelŽ . is designed which comprehensively considers the effects of these three indices and the network topology for each candidate VAr support site. There is no question that each of three indices can reflect the improvement of the system’s operation state after the VAr support service is provided although the results from BCR, VRSI and BVSI may be different. Unfortunately, it is difficult to find a unified process for ranking these results. Moreover, all three indices have not included other qualitative relationships for considering relative importance of different VAr source sites. AHP, which is a simple and convenient method to analyze a complicated problem or a Ž complex system , can help to quantify the decision-. maker’s thinking 7,16 . Thus, it provides a useful<sup>w</sup> <sup>x</sup> means for considering myriad factors in the ranking and selection of VAr source locations.

The results of the developed approach are illustrated and discussed on an IEEE 30-bus system.

<table><tr><td colspan="2">The glossary of symbols used in this paper is as follows.</td></tr><tr><td> $\lambda_{\text{max}}$ </td><td>Maximal eigenvalue of the judgment matrix</td></tr><tr><td>nn</td><td>Dimension of the judgment matrix</td></tr><tr><td> $P_{\text{L}}$ </td><td>System power loss</td></tr><tr><td> $P_{\text{gslack}}$ </td><td>Real power of the slack generator</td></tr><tr><td> $P_{\text{dk}}$ </td><td>Real power load at load bus k</td></tr><tr><td> $Q_{\text{di}}$ </td><td>Reactive power load at load bus i</td></tr><tr><td> $V_{\text{gi}}$ </td><td>Voltage magnitude at generator bus i</td></tr><tr><td> $V_{\text{di}}$ </td><td>Voltage magnitude at load bus i</td></tr><tr><td> $Q_{\text{gi}}$ </td><td>VAr generation of generator i</td></tr><tr><td> $Z_{\text{L}}$ </td><td>Impedance of transmission line L</td></tr><tr><td> $I_{\text{Lmax}}$ </td><td>Maximal current limit through transmission line L</td></tr><tr><td> $q_{\text{ci}}$ </td><td>Reactive power of capacitor at bus i</td></tr><tr><td>T</td><td>Transformer tap position</td></tr><tr><td> $\theta$ </td><td>Voltage angle at bus i</td></tr><tr><td> $P_{\text{L}}$ </td><td>System real power loss</td></tr><tr><td>NG</td><td>Set of generation buses</td></tr><tr><td>NT</td><td>Set of transformer branches</td></tr><tr><td>ND</td><td>Set of load buses</td></tr><tr><td> $N_{\text{bus}}$ </td><td>Set of total network buses</td></tr><tr><td>NI</td><td>Set of the outage line (l=0 means no line outage)</td></tr><tr><td> $C_{\text{f(i)}}$ </td><td>Fixed part of reactive power pricing at VAr source bus i</td></tr><tr><td> $C_{\text{ci}}$ </td><td>Unit investment cost due to allocation of capacitors at load bus i (US$ MVAr-1)</td></tr><tr><td> $C_{\text{V(i)}}(t)$ </td><td>Variable part of reactive power pricing at VAr source bus i at time t</td></tr><tr><td> $q_{\text{ci}}$ </td><td>Reactive power of capacitor at bus i at time t</td></tr><tr><td> $\lambda$ </td><td>Pricing of electricity (US$ (MWh)-1)</td></tr><tr><td> $\partial P_{\text{L}}/\partial Q_i$ </td><td>Sensitivity of system-power-loss objective function with respect to reactive power support (capacitor)</td></tr><tr><td> $\alpha$ </td><td>Capital recovery factor (CRF)</td></tr><tr><td> $C_{\text{f(i)}}(t)$ </td><td>Hourly-based fixed cost of VAr pricing</td></tr><tr><td>r</td><td>Interest rate</td></tr></table>

$$
\begin{array}{l} n \\ P _ {\mathrm{L}} ^ {t} (0) \end{array}
$$

<sup>t</sup> P Ž . 0<sub>L</sub> System real power loss at time t before capacitor at bus i is installed

$F _ { \mathrm { L } } ^ { t } ( q _ { \mathrm { c } i } )$ System real power loss at time t after capacitor at bus i is installed $C ( q _ { \mathrm { c } i } )$ Equivalent daily investment cost of capacitor at load bus i ŽUS\$ $\mathrm { d a y ^ { - 1 } } )$

BCR<sup>t</sup> Hourly-based benefit-to-cost ratio index

<sup>t</sup> V Ž . 0<sub>j</sub> Voltage magnitude at bus j at time t before reactive injection at bus i is changed

$V _ { j } ^ { t } ( \varDelta Q _ { i } )$ Voltage magnitude at bus j at time t after a new reactive injection is added at bus i

$\varDelta Q _ { i } ^ { t }$ Increased reactive power injection at load bus i at time t

$\mathrm { \Delta V R S I } ^ { t }$ Hourly-based sensitivity index

$$
V _ {i} ^ {t} (0)
$$

$V _ { i } ^ { t } ( l )$ Voltage magnitude at bus i at time t in the case of line l outage $V _ { i \mathrm { m i n } }$ Lower limit of voltage at bus i $\mathbf { B V S I } ^ { t }$ Hourly-based voltage security margin index

## 2. OPF formulation

The aim of reactive power planning is to obtain the optimal VAr placement scheme location andŽ sizing of capacitors on the load buses under the . some load level and constraints. In this paper, an OPF formulation in which the objective function is the minimization of system power loss is used for this purpose. The OPF formulation can be expressed as follows.

Ž . 1 Objective function

min $P _ { \mathrm { { L } } } = F { \left( { P _ { \mathrm { { g s l a c k } } } } \right) } .$

1Ž .

Ž . 2 Constraints

$$
\sum_ {i = 1} ^ {\mathrm{NG}} P _ {\mathrm{g} i} = \sum_ {k = 1} ^ {\mathrm{ND}} P _ {\mathrm{d} k} + P _ {\mathrm{L}}\tag{2}
$$

$$
P _ {\mathrm{g} i} - P _ {\mathrm{d} i} - F _ {i} (V, \theta , T) = 0
$$

$$
i = 1, 2, \dots , N _ {\text { bus }}, \quad i \neq \text { slack }\tag{3}
$$

$$
Q _ {\mathrm{g} i} - Q _ {\mathrm{d} i} + q _ {\mathrm{c} i} - G _ {i} (V, \theta , T) = 0\tag{4}
$$

$$
i = 1, 2, \dots , N _ {\text { bus }}, \quad i \neq \text { slack }
$$

$$
P _ {\mathrm{slack}} - F _ {i} (V, \theta , T) = 0\tag{5}
$$

$$
\left[ V _ {i} ^ {2} + V _ {j} ^ {2} - 2 V _ {i} V _ {j} \cos \left(\theta_ {i} - \theta_ {j}\right) \right]
$$

$$
/ Z _ {L} (l) ^ {2} - I _ {L \max} ^ {2} (l) \leq 0 \quad l = 0, 1, 2, \dots , N 1\tag{6}
$$

$$
Q _ {\mathrm{g} i \min} \leq Q _ {\mathrm{g} i} \leq Q _ {\mathrm{g} i \max}, \quad i \in \mathrm{NG}\tag{7}
$$

$$
V _ {\mathrm{g} i \min} \leq V _ {\mathrm{g} i} \leq V _ {\mathrm{g} i \max}, \quad i \in \mathrm{NG}\tag{8}
$$

$$
V _ {\mathrm{d} i \min} \leq V _ {\mathrm{d} i} \leq V _ {\mathrm{d} i \max}, \quad i \in \mathrm{ND}\tag{9}
$$

$$
T _ {i \min} \leq T _ {i} \leq T _ {i \max}, \quad i \in \mathrm{NT}\tag{10}
$$

The subscripts ‘min’ and ‘max’ stand for the lower and upper bounds of a constraint, respectively.

The OPF problem is computed using robust interior point optimal power flow RIOPF programŽ . <sup>w</sup> <sup>x</sup> 13,14 for every hour of the load curve.

## 3. Reactive power pricing

The reactive power pricing of each VAr source bus is divided into two parts in this paper. One is the fixed part, and another is the variable part. The OPF solution will give the amount of reactive power support needed at each load bus. It is necessary to use cost–benefit analysis CBA to analyze whetherŽ . the new VAr sources would be cost-effective when they are actually installed. The corresponding investment cost including installing cost of the VAr Ž . source is the fixed part of VAr pricing at this VAR source bus, i.e.,

$$
C _ {f (i)} = C _ {\mathrm{c} i} q _ {\mathrm{c} i}\tag{11}
$$

The variable cost of reactive power support service is determined based on capability and contribution to improvement of system performance including factors such as security, reliability and economics. Contribution or value of reactive support to the system can be evaluated by calculating sensitivity of objective function with respect to reactive power support. This sensitivity reflects dollar savings from applying VAr support service and control. Therefore, the variable part of reactive power pricing at this VAr source bus can be obtained through computing the power-loss-cost saving from applying reactive power support service.

$$
C _ {V (i)} (t) = - \lambda \frac {\partial P _ {\mathrm{L}}}{\partial Q _ {i}} \Bigg | _ {t} \times q _ {\mathrm{c} i} (t)\tag{12}
$$

The negative symbol in Eq. 14 means that sys-Ž . tem real power loss will reduce as the capacity of the capacitor increases. It is obvious that the variable part of VAr pricing at the same bus might be different during the operation period, i.e., VAr pricing is time-dependent.

Thus, the reactive power pricing on VAr source bus at time t can be obtained as follows:

$$
C _ {P (i)} (t) = C _ {f (i)} (t) + C _ {V (i)} (t)\tag{13}
$$

where

$$
C _ {f (i)} (t) = \frac {\alpha C _ {f (i)}}{8 7 6 0}\tag{14}
$$

$$
\alpha = \frac {r (1 + r) ^ {n}}{(1 + r) ^ {n} - 1}\tag{15}
$$

It was supposed that 1 year<sup>s</sup>8760 h in Eq. 14 .Ž .

## 4. Multiple indices for VAR planning

For VAr planning purposes, costs and sites of reactive power sources must be determined. The selection of new VAr source sites should be conducted according to capability and contribution to improvement of system performance including factors such as economics, sensitivity and security when they are actually installed. Consequently, multiple indices should be used in the selection of VAr source sites. Three parallel indices to select new VAr source sites are defined. They are benefit-to-cost ratio Ž . Ž . BCR , voltage reactive sensitivity index VRSI and bus voltage security index BVSI .Ž .

## 4.1. Benefit-to-cost ratio BCR( )

Cost–benefit analysis CBA is used to computeŽ . the economy index in the selection of VAr source sites. Since only those load buses with cost-effectiveness are possible to be selected as new VAr source sites, it is necessary to use CBA to analyze whether the new VAr sources would be cost-effective when they are actually installed. The following benefit-tocost ratio BCR index will be used for the selection Ž . of new VAr source sites.

$$
\mathrm{BCR} = \frac {\sum_ {t = 1} ^ {2 4} \lambda \left(P _ {\mathrm{L}} ^ {t} (0) - P _ {\mathrm{L}} ^ {t} \left(q _ {\mathrm{c} i}\right)\right)}{C \left(q _ {\mathrm{c} i}\right)}\tag{16}
$$

or

$$
\mathrm{BCR} ^ {t} = \frac {P _ {\mathrm{L}} ^ {t} (0) - P _ {\mathrm{L}} ^ {t} \left(q _ {\mathrm{c} i}\right)}{C \left(q _ {\mathrm{c} i}\right) / 2 4}\tag{17}
$$

$$
C (q _ {\mathrm{c} i}) = \frac {\alpha C _ {\mathrm{c} i} q _ {\mathrm{c} i}}{3 6 5}\tag{18}
$$

It was supposed that 1 year<sup>s</sup>365 days in Eq. Ž . 18 .

## 4.2. Voltage reactiÕe sensitiÕity index VRSI( )

Voltage reactive sensitivity index VRSI is used Ž . to calculate VAr<sup>r</sup>voltage sensitivity index with respect to bus reactive injection change in the selection of VAr source sites. The magnitude of the bus VAr<sup>r</sup>voltage sensitivity can be expressed by the total system incremental bus voltage $\Sigma \varDelta V _ { i } ,$ which is obtained by increasing a small reactive power injection at a given load bus. The bigger the value of $\Sigma \varDelta V _ { i } .$ , the more sensitive the voltage will be at a given bus to a change of reactive injection. It means that a load bus with the large value of $\Sigma \varDelta V _ { i }$ is a good candidate to be selected as a VAr source site. The following sensitivity index for each load bus is used in the paper.

$$
\mathrm{VRSI} _ {i} ^ {t} = \frac {\sum_ {j \in N} \Delta V _ {j} ^ {t}}{\Delta Q _ {i} ^ {t}} = \frac {\sum_ {j \in N} \left(V _ {j} ^ {t} (\Delta Q _ {i}) - V _ {j} ^ {t} (0)\right)}{\Delta Q _ {i} ^ {t}}\tag{19}
$$

## 4.3. Bus Õoltage security index BVSI( )

The indices BCR<sup>t</sup> and VRSI<sup>t</sup> reflect the economy and sensitivity in the selection of VAr source sites in the normal case. But they cannot reflect the voltage security or stability under the contingency cases. A bus voltage security index BVSI is presented to Ž . calculate the bus voltage security margin index in the selection of VAr source sites.

![](/api/attachments/4YF29FSM/fulltext/images/6fe7c9eaf7e838be776563724683ee575fffcc29ab14b69ad4df4e0ee860df26.jpg)  
Fig. 1. Hierarchical model of VAr source-site ranking.

Let $V _ { i } ( 0 )$ be the voltage at bus i under the normal operational state. Generally, $V _ { i } ( 0 )$ is within voltage limits, i.e., safe if no system parameters loads orŽ lines change. The value of. $( V _ { i } ( 0 ) - V _ { i \operatorname* { m i n } } )$ is called voltage security margin VSM at bus Ž . i. In the contingency case such as transmission line outage, the voltage magnitude of buses may be reduced. It means that the voltage security margin of each bus in the contingency case may be smaller than that in normal case. Especially, the value of VSM at some buses may be negative under the serious contingency case. In this case, the corresponding bus voltage is not safe. Obviously, the bus with negative or very small VSM will be a good candidate to be selected as a new VAr source site. Since the values of VSM may be different for the same bus under the different contingency case, the minimal VSM will be used for each bus. This paper defined the following bus voltage security index for the selection of new VAr source sites.

Judgment matrix A-PI

<table><tr><td>A</td><td> $PI_{BCR}$ </td><td> $PI_{VRS}$ </td><td> $PI_{BVS}$ </td><td> $PI_C$ </td></tr><tr><td> $PI_{BCR}$ </td><td>1</td><td>1</td><td>2</td><td>5</td></tr><tr><td> $PI_{VRS}$ </td><td>1</td><td>1</td><td>1/2</td><td>2</td></tr><tr><td> $PI_{BVS}$ </td><td>1/2</td><td>2</td><td>1</td><td>3</td></tr><tr><td> $PI_C$ </td><td>1/5</td><td>1/2</td><td>1/3</td><td>1</td></tr></table>

$$
\mathrm{BVSI} _ {i} ^ {t} = \frac {V _ {i} ^ {t} (0) - \min \left[ V _ {i} ^ {t} (l) \right]}{V _ {i} ^ {t} (0) - V _ {i \min}} \quad l \in \mathrm{Nl}
$$

Ž . It can be shown from Eq. 20 that if $\mathbf { B } \mathbf { V } \mathbf { S } \mathbf { I } _ { i } ^ { t } = 1$ the voltage security margin is zero, i.e., the voltage at bus i has reached its lower limit. If $\mathrm { B V S I } _ { i } ^ { t } < 1$ the voltage at bus i is safe. The smaller the $\mathrm { B V S I } _ { i } ^ { t } ,$ the bigger the voltage security margin under the

20 Ž .

![](/api/attachments/4YF29FSM/fulltext/images/e9f0838d6f7be0a578c8de876f5f423018ba9520f6fc3efde66435b59970f028.jpg)  
Fig. 2. Real-time VAr pricing and VAr placement.

Table 2  
Real and reactive load of IEEE 30 bus system LSF Ž . <sup>s</sup>1.4

<table><tr><td>Bus no.</td><td>Real load (p.u.)</td><td>Reactive load (p.u.)</td><td>Bus no.</td><td>Real load (p.u.)</td><td>Reactive load (p.u.)</td></tr><tr><td>2</td><td>0.3038</td><td>0.1778</td><td>17</td><td>0.1260</td><td>0.0812</td></tr><tr><td>3</td><td>0.0336</td><td>0.0168</td><td>18</td><td>0.0448</td><td>0.0210</td></tr><tr><td>4</td><td>0.1064</td><td>0.0504</td><td>19</td><td>0.1330</td><td>0.0630</td></tr><tr><td>5</td><td>1.3188</td><td>0.4200</td><td>20</td><td>0.0308</td><td>0.0140</td></tr><tr><td>7</td><td>0.3192</td><td>0.1526</td><td>21</td><td>0.2450</td><td>0.1568</td></tr><tr><td>8</td><td>0.4200</td><td>0.4200</td><td>23</td><td>0.0448</td><td>0.0224</td></tr><tr><td>10</td><td>0.0812</td><td>0.0350</td><td>24</td><td>0.1218</td><td>0.0938</td></tr><tr><td>12</td><td>0.1568</td><td>0.1050</td><td>26</td><td>0.0490</td><td>0.0322</td></tr><tr><td>14</td><td>0.0868</td><td>0.0420</td><td>29</td><td>0.0336</td><td>0.0154</td></tr><tr><td>15</td><td>0.1148</td><td>0.0560</td><td>30</td><td>0.1484</td><td>0.0700</td></tr><tr><td>16</td><td>0.0490</td><td>0.0252</td><td></td><td></td><td></td></tr></table>

contingency case. If $\mathrm { B V S I } _ { i } ^ { t } > 1$ , the voltage at bus i is not safe, i.e., violates its lower limit.

Ž <sup>t</sup> <sup>t</sup> Obviously, all three indices BCR , VRSI and <sup>t</sup> BVSI reflect the improvement of the system’s op- . erational state after the VAr support service is provided. But the ranking results from these three methods may not be the same due to their independent nature. The problem is how to find a unified process for ranking these results. A simple method dealing with multiple indices is one that sums all indices, i.e.,

$$
\mathrm{PI} = \mathrm{PI} _ {\mathrm{BCR}} + \mathrm{PI} _ {\mathrm{VRS}} + \mathrm{PI} _ {\mathrm{BVS}}\tag{21}
$$

where

$$
\mathrm{PI} _ {\mathrm{BCR}} = \mathrm{BCR} ^ {t}\tag{22}
$$

$$
\mathrm{PI} _ {\mathrm{VRS}} = \mathrm{VRSI} ^ {t}\tag{23}
$$

$$
\mathrm{PI} _ {\mathrm{BVS}} = \mathrm{BVSI} ^ {t}\tag{24}
$$

But Eq. 21 cannot distinguish the different con-Ž . tributions of three indices to the improvement of the system performance when the VAr support sites are actually installed. Moreover, it is also very difficult to treat other qualitative relationships in ranking, such as relative importance of different VAr source sites. This paper uses the AHP approach to solve these problems.

## 5. AHP for ranking VAr sources

In order to obtain a unified VAr source location ranking, an analytic hierarchical process AHP isŽ . used for this purpose.

## 5.1. Principle of AHP

In the analytic hierarchical process, a structural model of the analytic hierarchy is first established through analysis of the complex system. Then the complex problem is transformed into the problem of ranking calculation within the hierarchical structure. In the ranking calculation, the ranking in each hierarchy can also be converted into the judgment and comparison of a series of pairs of factors. This implies that a judgment matrix is needed to reflect these judgments and comparisons. The judgment matrix can be formed according to the quantified judgment of pairs of factors using some ratio scale method 7,16 . Consequently, the value of the <sup>w</sup> <sup>x</sup> weighting coefficient of all factors can be obtained through calculating the maximal eigenvalue and the corresponding eigenvector of the judgment matrix. Obviously, the purpose of ranking the elements of the eigenvector corresponding to the maximal eigenvalue is simply to obtain the weighting of each factor among the different kinds of factors. The steps of the AHP algorithm may be written as follows 16 .<sup>w</sup> <sup>x</sup>

Step 1: Set up a hierarchy model.

Step 2: Form a judgment matrix. The value of elements in the judgment matrix reflects the user’s knowledge about the relative importance between every pair of factors.

Step 3: Calculate the maximal eigenvalue and the corresponding eigenvector of the judgment matrix.

Step 4: Check hierarchical rank and consistency of results.

Table 3  
System loss reduction from VAr support of each load bus

<table><tr><td>Load bus</td><td>Loss reduction (MW h-1)</td><td>Load bus</td><td>Loss reduction (MW h-1)</td></tr><tr><td>2</td><td>0.00000</td><td>17</td><td>0.02874</td></tr><tr><td>3</td><td>0.01549</td><td>18</td><td>0.04893</td></tr><tr><td>4</td><td>0.01495</td><td>19</td><td>0.05157</td></tr><tr><td>5</td><td>0.00000</td><td>20</td><td>0.09304</td></tr><tr><td>7</td><td>0.01792</td><td>21</td><td>0.09128</td></tr><tr><td>8</td><td>0.00000</td><td>23</td><td>0.10174</td></tr><tr><td>10</td><td>0.02255</td><td>24</td><td>0.11150</td></tr><tr><td>12</td><td>0.00792</td><td>26</td><td>0.11849</td></tr><tr><td>14</td><td>0.02790</td><td>29</td><td>0.10555</td></tr><tr><td>15</td><td>0.03692</td><td>30</td><td>0.12966</td></tr><tr><td>16</td><td>0.02225</td><td></td><td></td></tr></table>

Table 4  
Variable cost of VAr pricing for each load bus

<table><tr><td>Load node</td><td>VAr pricing [US$ (p.u. MVAr) $^{-1}$  day $^{-1}$ ]</td><td>Load node</td><td>VAr pricing [US$ (p.u. MVAr) $^{-1}$  day $^{-1}$ ]</td></tr><tr><td>2</td><td>0.0000</td><td>17</td><td>985.3710</td></tr><tr><td>3</td><td>531.0854</td><td>18</td><td>1677.5993</td></tr><tr><td>4</td><td>512.5712</td><td>19</td><td>1768.1135</td></tr><tr><td>5</td><td>0.0000</td><td>20</td><td>3189.9415</td></tr><tr><td>7</td><td>614.3997</td><td>21</td><td>3129.5987</td></tr><tr><td>8</td><td>0.0000</td><td>23</td><td>3488.2271</td></tr><tr><td>10</td><td>773.1425</td><td>24</td><td>3822.8555</td></tr><tr><td>12</td><td>271.5427</td><td>26</td><td>4062.5126</td></tr><tr><td>14</td><td>956.5710</td><td>29</td><td>3618.8556</td></tr><tr><td>15</td><td>1265.8280</td><td>30</td><td>4445.4839</td></tr><tr><td>16</td><td>762.8568</td><td></td><td></td></tr></table>

We can perform the hierarchical rank according to the value of elements in the eigenvector, which represents the relative importance of the corresponding factor. The consistency index of a hierarchy ranking CI is defined as

$$
\mathrm{CI} = \left(\lambda_ {\max} - n n\right) / (n n - 1)\tag{25}
$$

The stochastic consistency ratio is defined as:

$$
\mathrm{CR} = \mathrm{CI} / \mathrm{RI}\tag{26}
$$

where RI is a set of given average stochastic consistency indices and CR is the stochastic consistency ratio.

It is possible to precisely calculate the eigenvalue and the corresponding eigenvector of a matrix, however, this would be time-consuming. Moreover, it is not necessary to precisely compute the eigenvalue and the corresponding eigenvector of the judgment matrix. The reason being that the judgment matrix, which is formed by the subjective judgment of the user, itself has some range of error. Therefore, the approximate approaches, which were presented in the Ref. 16 , are adopted in the paper to compute the maximal eigenvalue and the corresponding eigenvector.

## 5.2. Hierarchy model for ranking VAr sources

A hierarchy model is devised as in Fig. 1, according to the AHP principle.

The hierarchical model of VAr source-site ranking consists of three sections: 1 the unified ranking Ž . of VAr source sites, 2 the performance indices, inŽ . which the $\mathrm { P I } _ { \mathrm { C } }$ reflects the relative importance of load nodes, and 3 load busesŽ . $C _ { 1 } , \ldots , C _ { m }$ which identify the candidate VAr source sites.

The performance indices $\mathrm { P I } _ { \mathrm { { B C R } } } , \mathrm { P I } _ { \mathrm { { V R S } } }$ , and $\mathrm { P I } _ { \mathrm { B V S } }$ are defined in Eqs. 22 – 24 . Obviously, eigenvec-Ž . Ž . tors of $\mathrm { P I } _ { \mathrm { B C R } } , \ \mathrm { P I } _ { \mathrm { V R S } }$ and $\mathrm { P I } _ { \mathrm { B V S } }$ can be obtained through normalization. However, it is very difficult to obtain exactly $\mathrm { P I } _ { \mathrm { C } }$ and the corresponding eigenvector. They can be obtained, however, through forming and computing the judgment matrix $\mathbf { P I } _ { \mathrm { C } } – \mathbf { C }$ according to the position of load buses in power network and, the experience of operators.

In addition, the judgment matrix A-PI, which is shown in Table 1, can also be obtained according to the nine-scale method 7,16 for practical operating<sup>w</sup> <sup>x</sup> cases in power systems. For example, the operator might think that the BCR index $\mathrm { P I } _ { \mathrm { B C R } }$ is very important compared with relative importance index $\mathrm { P I } _ { \mathrm { C } }$ , in which case, the corresponding element in judgment matrix should be ‘5’. If the BVSI index $\mathrm { P I } _ { \mathrm { B V S } }$ is slightly more important compared with VRSI index $\mathrm { P I } _ { \mathrm { V R S } }$ , then the corresponding element in the judgment matrix should be ‘2’. If both indices of BCR and VRSI are thought to be equally important, the corresponding element in the matrix should be ‘1’.

Table 5  
Single hierarchical ranking of VAR support buses

<table><tr><td>Bus no.</td><td>BCR</td><td>Rank no.</td><td>VRSI</td><td>Rank no.</td><td>BVSI</td><td>Rank no.</td></tr><tr><td>10</td><td>0.237</td><td>13</td><td>3.135</td><td>12</td><td>0.398</td><td>12</td></tr><tr><td>14</td><td>0.293</td><td>12</td><td>2.860</td><td>13</td><td>0.338</td><td>13</td></tr><tr><td>15</td><td>0.387</td><td>10</td><td>3.137</td><td>11</td><td>0.518</td><td>10</td></tr><tr><td>17</td><td>0.302</td><td>11</td><td>3.199</td><td>10</td><td>0.410</td><td>11</td></tr><tr><td>18</td><td>0.513</td><td>9</td><td>3.951</td><td>9</td><td>0.705</td><td>8</td></tr><tr><td>19</td><td>0.541</td><td>8</td><td>4.105</td><td>8</td><td>0.767</td><td>6</td></tr><tr><td>20</td><td>0.976</td><td>6</td><td>8.041</td><td>6</td><td>0.647</td><td>9</td></tr><tr><td>21</td><td>0.958</td><td>7</td><td>7.713</td><td>7</td><td>0.754</td><td>7</td></tr><tr><td>23</td><td>1.067</td><td>5</td><td>8.094</td><td>5</td><td>1.293</td><td>4</td></tr><tr><td>24</td><td>1.170</td><td>3</td><td>8.582</td><td>4</td><td>2.290</td><td>5</td></tr><tr><td>26</td><td>1.243</td><td>2</td><td>10.58</td><td>2</td><td>5.136</td><td>2</td></tr><tr><td>29</td><td>1.107</td><td>4</td><td>10.40</td><td>3</td><td>5.005</td><td>3</td></tr><tr><td>30</td><td>1.360</td><td>1</td><td>10.73</td><td>1</td><td>7.848</td><td>1</td></tr></table>

## 6. Numerical example

According to the scheme discussed in Sections 1–5, the real-time VAr pricing and VAr control scheme is summarized in Fig. 2.

The approach is examined using the IEEE 30-bus system. The main parameters of the system, such as generator output constraints and maximal current orŽ power constraints, are taken from Ref. 17 . The. <sup>w</sup> <sup>x</sup> basic system reactive demand at some nodes was increased during the study. Due to the limited space, only the results under peak load condition with loadŽ scaling factor $\mathrm { L S F } = 1 . 4 )$ are given in the paper. The real and reactive load of each load bus used in this study are listed on Table 2.

It is assumed that the pricing of electricity is Ž . <sup>1</sup> US\$20 MW h , and the investment cost of the capacitor is US\$100.0 $\mathrm { k V A r } ^ { - 1 }$ . Considering the interest rate $r = 0 . 0 6 ,$ , the capital recovery years $n = 1 2$ the capital recovery factor CRF can be computed, Ž . i.e., $\alpha = 0 . 1 1 9 3$ . Thus, the cost of the capacitor, i.e., the fixed cost of VAr pricing on each VAr support bus, is approximated as US\$32.68 MVAr<sup>y1</sup> day<sup>y1</sup>, Ž . <sup>1</sup> <sup>1</sup> or US\$3268 p.u. MVAr day base power is Ž 100 MVA . The upper and lower limits of bus. voltage are given as 1.05 and 0.95 p.u., respectively. The power loss minimization is selected as objective function. Table 3 is the result of loss reduction when each load bus is respectively installed with the same amount of VAr support, i.e., 1.4 MVAr. The variable cost of VAr pricing for each reactive power support node is computed and listed in Table 4.

Table 7  
Unified ranking of VAr support nodes for IEEE 30 bus system

<table><tr><td>Bus number</td><td>Total weight</td><td>Rank number</td></tr><tr><td>10</td><td>0.0276</td><td>12</td></tr><tr><td>14</td><td>0.0268</td><td>13</td></tr><tr><td>15</td><td>0.0336</td><td>10</td></tr><tr><td>17</td><td>0.0298</td><td>11</td></tr><tr><td>18</td><td>0.0409</td><td>9</td></tr><tr><td>19</td><td>0.0438</td><td>8</td></tr><tr><td>20</td><td>0.0700</td><td>7</td></tr><tr><td>21</td><td>0.0724</td><td>6</td></tr><tr><td>23</td><td>0.0881</td><td>5</td></tr><tr><td>24</td><td>0.1020</td><td>4</td></tr><tr><td>26</td><td>0.1462</td><td>2</td></tr><tr><td>29</td><td>0.1353</td><td>3</td></tr><tr><td>30</td><td>0.1835</td><td>1</td></tr></table>

It can be seen from Table 4 that minimum benefit will be obtained if the VAr supports are located on load buses a2, a3, a4, a5, a7, a8, a12 and a16, so these buses will not appear in the ranking of VAr source sites. A single hierarchical ranking is defined based on the ranking obtained by using only one of the three indices BCR, VRSI and BVSI . The singleŽ . hierarchical ranking results of VAr source sites are listed in Table 5. It can be observed from Table 5 that the major candidate VAr support nodes selected by these three methods are the same, but different in ranking.

Table 6  
Judgment matrix $\mathbf { P I } _ { \mathbf { C } ^ { - } } \mathbf { C }$ for IEEE 30-bus system

<table><tr><td> $\mathbf{PI}_{\text{C}}$ </td><td> $C_{10}$ </td><td> $C_{14}$ </td><td> $C_{15}$ </td><td> $C_{17}$ </td><td> $C_{18}$ </td><td> $C_{19}$ </td><td> $C_{20}$ </td><td> $C_{21}$ </td><td> $C_{23}$ </td><td> $C_{24}$ </td><td> $C_{26}$ </td><td> $C_{29}$ </td><td> $C_{30}$ </td></tr><tr><td> $C_{10}$ </td><td>1</td><td>5</td><td>1</td><td>2</td><td>3</td><td>1</td><td>1</td><td>1/2</td><td>1/2</td><td>1/3</td><td>1/3</td><td>1/2</td><td>1/3</td></tr><tr><td> $C_{14}$ </td><td>1/5</td><td>1</td><td>1/3</td><td>1/3</td><td>1</td><td>1/2</td><td>1/2</td><td>1/3</td><td>1/3</td><td>1/3</td><td>1/4</td><td>1/3</td><td>1/4</td></tr><tr><td> $C_{15}$ </td><td>1</td><td>3</td><td>1</td><td>2</td><td>3</td><td>2</td><td>2</td><td>1/2</td><td>1/3</td><td>1/3</td><td>1/3</td><td>1/31</td><td>1/4</td></tr><tr><td> $C_{17}$ </td><td>1/2</td><td>3</td><td>1/2</td><td>1</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1/2</td><td>1/2</td><td>1/2</td><td>1/2</td><td>1/3</td></tr><tr><td> $C_{18}$ </td><td>1/3</td><td>1</td><td>1/3</td><td>1/3</td><td>1</td><td>1</td><td>1</td><td>1/3</td><td>1/3</td><td>1/3</td><td>1/4</td><td>1/3</td><td>1/4</td></tr><tr><td> $C_{19}$ </td><td>1</td><td>2</td><td>1/2</td><td>1/3</td><td>1</td><td>1</td><td>1</td><td>1/2</td><td>1/3</td><td>1/2</td><td>1/4</td><td>1/3</td><td>1/4</td></tr><tr><td> $C_{20}$ </td><td>1</td><td>2</td><td>1/2</td><td>1/3</td><td>1</td><td>1</td><td>1</td><td>1/2</td><td>1/3</td><td>1/2</td><td>1/3</td><td>1/3</td><td>1/4</td></tr><tr><td> $C_{21}$ </td><td>2</td><td>3</td><td>2</td><td>1</td><td>3</td><td>2</td><td>2</td><td>1</td><td>1/2</td><td>1/2</td><td>1/3</td><td>1/2</td><td>1/3</td></tr><tr><td> $C_{23}$ </td><td>2</td><td>3</td><td>3</td><td>2</td><td>3</td><td>3</td><td>3</td><td>2</td><td>1</td><td>2</td><td>1</td><td>2</td><td>1/2</td></tr><tr><td> $C_{24}$ </td><td>3</td><td>3</td><td>3</td><td>2</td><td>3</td><td>2</td><td>2</td><td>2</td><td>1/2</td><td>1</td><td>1/2</td><td>1/2</td><td>1/2</td></tr><tr><td> $C_{26}$ </td><td>3</td><td>4</td><td>3</td><td>2</td><td>4</td><td>4</td><td>3</td><td>3</td><td>1</td><td>2</td><td>1</td><td>2</td><td>1</td></tr><tr><td> $C_{29}$ </td><td>2</td><td>3</td><td>3</td><td>2</td><td>3</td><td>3</td><td>3</td><td>2</td><td>1/2</td><td>2</td><td>1/2</td><td>1</td><td>1/3</td></tr><tr><td> $C_{30}$ </td><td>3</td><td>4</td><td>4</td><td>3</td><td>4</td><td>4</td><td>4</td><td>3</td><td>2</td><td>1</td><td>3</td><td>1</td><td>1</td></tr></table>

In order to conduct the unified ranking of VAr source sites, it is necessary to comprehensively consider the results of three indices and the relative importance of VAr support buses by using the judgment matrix $\mathbf { P I } _ { \mathrm { C } } – \mathbf { C }$ for the IEEE 30-bus system given in Table 6. The values in Table 6 reflect the relative importance in the power system for every pair of VAr support nodes. These values have been selected according to the engineer’s knowledge and experience, using the nine-ratio-scale method 16 . <sup>w</sup> <sup>x</sup> Table 7 provides the unified ranking results of VAr support nodes which coordinates BCR, VRSI and BVSI methods by using AHP for the IEEE 30-bus system. The unified ranking results presented in Table 6 considered the relative importance of VAr support nodes in the power system.

## 7. Conclusions

An integrated approach to determine VAr price and selection of new VAr support sites is developed in the paper. The VAr pricing is divided into two parts: fixed and variable. The fixed pricing is the investment cost of VAr support service. The variable pricing, which is determined based on capability and contribution to improvement of system performance such as security, reliability and economics is the dollar savings from applying VAr support service and control. The optimal power flow approach is employed to carry out this purpose. In the selection and ranking of reactive power support nodes, three parallel indices have been proposed in the study. AHP is used to comprehensively consider the results of three indices and other quantitative relationships for considering the relative importance of different VAr source sites. Simulation and results show that the proposed approach is powerful.

## Acknowledgements

This work has been supported by a grant from the National Science Foundation Contract No. EEC-Ž 9726049 ..

## References

<sup>w</sup> <sup>x</sup> 1 O. Alsac, J. Bright, M. Prais, B. Stott, Further developments in LP-based optimal power flow, IEEE Trans. Power Syst. 2 Ž . 1990 697–711.

<sup>w</sup> <sup>x</sup> 2 O. Alsac, B. Sttot, Optimal power flow with steady-state security, IEEE Trans. PAS 93 1974 745–751.Ž .

<sup>w</sup> <sup>x</sup> 3 M.L. Baughman, S.N. Siddiqi, Real-time pricing of reactive power: theory and case study results, IEEE Trans. Power Syst. PWRS 6 1991 23–29.Ž .

<sup>w</sup> <sup>x</sup> 4 S.V. Berg, J. Adams, B. Nickum, Power factors and the efficient pricing and production of reactive power, The Energy J. 4 1994 93–102.Ž .

<sup>w</sup> <sup>x</sup> 5 D. Chattopadhyay, K. Bhattacharya, J. Parikh, Optimal reactive power planning and its spot-pricing: an integrated approach, IEEE PES Winter Meeting, WM 204-8 PWRS, 1995.

<sup>w</sup> <sup>x</sup> 6 N.H. Dandachi, M.J. Rawlins, O. Alsac, B. Stott, OPF for reactive pricing studies on the NGC system, IEEE Power Industry Computer Applications Conference, PICA ’95, UT, May 1995, pp. 11–17.

<sup>w</sup> <sup>x</sup> 7 T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

<sup>w</sup> <sup>x</sup> 8 F.C. Schweppe, M.C. Caramanis, R.D. Tabors, R.E. Bohn, Spot Pricing of Electricity, Kluwer Academic Publishers, 1988.

<sup>w</sup> <sup>x</sup> 9 K. Mamandur, R. Chenoweth, Optimal control of reactive power flow for improvements in voltage profiles and for real power loss minimization, IEEE Trans. PAS 100 1981 Ž . 3185–3194.

<sup>w</sup> <sup>x</sup> 10 M.O. Mansour, T.M. Abdel-Rahman, Non-linear VAR optimization using decomposition and coordination, IEEE Trans. PAS 103 1984 246–255.Ž .

<sup>w</sup> <sup>x</sup> 11 J.A. Momoh, J.Z. Zhu, A new approach to VAR pricing and control in the competitive environment, in: Proceedings of Thirty-First Hawaii International Conference on System Science, HI, Jan. 1998.

<sup>w</sup> <sup>x</sup> 12 J.A. Momoh, J.Z. Zhu, J.L. Dolce, A new method to congestion analysis for aerospace power system, Proceedings of the IEEE 1997 North American Power System Symposium Ž .NAPS , WY, October 1997.

<sup>w</sup> <sup>x</sup> 13 J.A. Momoh, G.F. Brown, R.A. Adapa, Evaluation of interior point methods and their application to power systems economic dispatch, Proceedings of the IEEE 1993 North American Power System Symposium NAPS , October 1993, pp. Ž . 116–123.

<sup>w</sup> <sup>x</sup> 14 J.A. Momoh, Robust interior point optimal power flow, EPRI Final Report TR-105081, May 1995.

<sup>w</sup> <sup>x</sup> 15 J.Z. Zhu, C.S. Chang, Power system optimal VAR planning with security and economic constraints, Proceedings of International Power Eng. Conference, IPEC ’97, Singapore, May 1997, pp. 42–46.

<sup>w</sup> <sup>x</sup> 16 J.Z. Zhu, M.R. Irving, Combined active and reactive dispatch with multiple objectives using analytic hierarchical process, IEEE Proceedings Part C 143 1996 344–352.Ž .

<sup>w</sup> <sup>x</sup> 17 J.Z. Zhu, G.Y. Xu, A unified model and automatic contingency selection algorithm for the P- and Q-subproblems, Electric Power Syst. Res. 32 1995 101–105.Ž .

James A. Momoh received the BSEE 1975 from Howard Uni-Ž . versity, the MSEE 1976 from Carnegie Mellon University, theŽ . MS 1980 in systems engineering from the University of Pennsyl- Ž . vania and the PhD 1983 in electrical engineering from HowardŽ . University. Professor Momoh is chair of the Electrical Engineering department at Howard University and also the Director of the Center for Energy System and Controls. His current research activities are concentrated in stability analysis, system security and expert systems design for utility firms and government agencies. In 1987, he received a National Science Foundation Presidential Young Investigator Award.

Jizhong Zhu received the BSEE 1985 , MS 1987 and PhD Ž . Ž . Ž . 1990 from Chongqing University, China. He is a professor at Chongqing University, China. He was a Royal Society fellow and visiting research fellow at Brunel University in the UK during 1995–1996. He was a postdoctoral fellow at National University of Singapore, and is currently a research fellow at Howard University. His research interest is in the analysis, operation, planning and control of power systems.
