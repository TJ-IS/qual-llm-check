---
otero_id: 15052
otero_key: "8H38SYCR"
title: "Optimal input/output reduction in production processes"
authors: "Alireza Amirteimoori; Ali Emrouznejad"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.020"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal input/output reduction in production processes

Alireza Amirteimoori <sup>a,</sup>⁎, Ali Emrouznejad <sup>b</sup>

<sup>a</sup> Department of Applied Mathematics, Islamic Azad University, Rasht-Iran

<sup>b</sup> Operations & Information Management Group, Aston Business School, Aston University, Birmingham B4 7ET, UK

## a r t i c l e i n f o

Article history: Received 17 June 2010 Received in revised form 25 September 2011 Accepted 18 November 2011 Available online 1 December 2011

Keywords: Data envelopment analysis Input/output reduction Ef<sup>fi</sup>ciency Multi-objective linear programming

## a b s t r a c t

While conventional Data Envelopment Analysis (DEA) models set targets for each operational unit, this paper considers the problem of input/output reduction in a centralized decision making environment. The purpose of this paper is to develop an approach to input/output reduction problem that typically occurs in organizations with a centralized decision-making environment. This paper shows that DEA can make an important contribution to this problem and discusses how DEA-based model can be used to determine an optimal input/output reduction plan. An application in banking sector with limitation in IT investment shows the usefulness of the proposed method.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

The measurement of technical ef<sup>fi</sup>ciency started with the research of Debreu [9]. In 1957, Farrell showed how to measure the technical and economic ef<sup>fi</sup>ciency of a sample of decision making units (DMUs). Farrell's measure was implemented in the LP problem which gave rise to the <sup>fi</sup>rst DEA model of Charnes et al. [4]. A variety of DEA applications and a growing body of research have led to many new developments in concepts and methodologies related to the DEA-ef<sup>fi</sup>ciency analysis. Extensive surveys provided by Cooper et al. and Emrouznejad et al. [8,10] corroborate this view. Since DEA was <sup>fi</sup>rst put forward by Charnes et al. in 1978, it has been widely used by organizations to evaluate the relative ef<sup>fi</sup>ciency of DMUs, allocating <sup>fi</sup>xed costs, resource allocation and target setting. Recently, many researchers have studied the issue of allocating <sup>fi</sup>xed costs, resource allocation and target setting (see for instances Refs. [1,2,5,7,14,15]). Cook and Kress [5] made the <sup>fi</sup>rst attempt to address the problem of <sup>fi</sup>xed cost allocation. They proposed a DEA approach to allocating <sup>fi</sup>xed cost which was based on two principles: invariance and Pareto-minimality. Beasly [2] developed an alternative DEAbased cost allocation approach by maximizing the average ef<sup>fi</sup>ciency across all DMUs and adding additional constraints and models to obtain a unique cost allocation. Cook and Zhu [6] have examined the issue of output deterioration often encountered in applying data envelopment analysis. They suggested some modi<sup>fi</sup>cations to the conventional DEA model so that the consequences captured on the output which can occur when inputs are reduced according to the computed performance measures. Korhonen and Syrjnen [13] developed an interactive formal approach based on DEA and multiobjective linear program (MOLP) to <sup>fi</sup>nd the most preferred allocation plan. Li et al. [14] argued that in the <sup>fi</sup>xed cost allocation problem the <sup>fi</sup>xed cost is a complement of other cost input, not an independent factor. Amirteimoori and Tabar [1] showed how output targets can be set at the same time as decisions are made about allocating input resources. Lin [15] proposed an ef<sup>fi</sup>ciency-driven approach for setting revenue targets.

As the foregoing attempts show, all of current studies have addressed the problems of allocating <sup>fi</sup>xed costs, resource allocation and target setting. In many real applications of DEA, the decision makers have to reduce the levels of some inputs and outputs. This could be because of the shortage of available funds. This is potentially useful in many applications, both in manufacturing and service industries. In manufacturing, the manufacturer has to reduce a number of employees. In lieu of ousting employees, he needs to reduce a speci<sup>fi</sup>c product. Normally, the manufacturer needs this resource/product reduction be fair and equitable.

As far as we know, no DEA-based work has been published focusing on input/output reduction. The current paper shows that just as DEA has made an important contribution to the problems of allocating <sup>fi</sup>xed costs, resource allocation and target setting, so too it can make an important contribution to the problem of input/output reduction. The paper discusses how DEA-based model can be used to address this problem. A procedure to determine an optimal reduction in inputs and outputs of DMUs while improving the total ef<sup>fi</sup>ciency of the central decision maker has been adopted.

The paper proceeds as follows. Section 2 introduces basic DEA models. The problem of input/output reduction is introduced in

Section 3. This is followed by a numerical example in Section 4 and an application in banking in Section 5. Conclusions and future research are given in Section 6.

## 2. Preliminaries

DEA is a powerful technique in productivity management. It is a linear programming-based methodology for measuring the relative ef<sup>fi</sup>ciency of decision making units (DMUs). Technical ef<sup>fi</sup>ciency of a DMU in DEA is determined relative to other similar units and can focus on either resource conservation or output augmentation. Suppose we have n DMUs $\{ D M U _ { j } { : } j = 1 , 2 , . . . , n \} ,$ , which produce s outputs, $y _ { r j } ; r { = } 1 , . . . , s$ by utilizing m inputs, $x _ { i j } ; i = 1 , . . . , m$ Many technical ef<sup>fi</sup>ciency models have been based on ratios of the form

$$
\text { Max } e _ {o} = \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r o}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i o}}
$$

where the weights $u _ { r }$ and $\nu _ { i }$ are non-negative. It is assumed that $x _ { i j } \geq 0$ and $y _ { r j } \ge 0$ for all $i , r$ and j. For example, if $p { = } 1 , . . . , n$ denotes a particular choice of unit, the CCR-ratio model of Charnes et al. [4] for the technical ef<sup>fi</sup>ciency score of unit $p$ is given by:

$$
\begin{array}{l} \text {Max} e _ {o} = \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r o}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i o}} \\ \text {s.t.} \\ \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r j}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i j}} \leq 1, j = 1,..., n, \\ u _ {r} \geq \epsilon , r = 1,..., s, \\ v _ {i} \geq \epsilon , i = 1,..., m. \end{array}\tag{1}
$$

where $e _ { o }$ is the ef<sup>fi</sup>ciency score of the o-th unit and $\epsilon > 0$ is a non-Archimedean in<sup>fi</sup>nitesimal quantity to enforce strict positivity of the weights. The above model is a fractional programming which can easily be transformed to the following linear programming using the Charnes and Cooper [3] transformation.

$$
\begin{array}{l} \text { Max } e _ {o} = \sum_ {r = 1} ^ {s} u _ {r} y _ {r o} \\ \text { s.t. } \\ \sum_ {i = 1} ^ {m} v _ {i} x _ {i o} = 1, \sum_ {r = 1} ^ {s} u _ {r} y _ {r j} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i j} \leq 0, j = 1,..., n, \\ u _ {r} \geq \epsilon , r = 1,..., s, \\ v _ {i} \geq \epsilon , i = 1,..., m. \end{array}\tag{2}
$$

This model is a constant return to scale program and it assumes that the status of all input/output variables is known prior to solving the model. The ef<sup>fi</sup>ciency ratio ranges between zero and one, with $D M U _ { o }$ being considered relatively ef<sup>fi</sup>cient if it receives a score of one. This means that all the DMUs on the frontier (ef<sup>fi</sup>cient DMUs) have $e _ { o } = 1$ . From a managerial perspective, this model delivers assessments and targets with an output maximization orientation.

## 3. Optimal input/output reduction

Consider a decision-making environment in which a set of units fall under the umbrella of a central decision maker with power to control its inputs and outputs. Suppose there are n independent DMUs, where each $D M U _ { j } { : } j = 1 , . . . , n$ consumes m inputs $x _ { i j } { : } i = 1 , . . . , m$ to generate s outputs $y _ { r j } \colon r = 1 , . . . , s .$ . Because of some limitations, the central unit needs to reduce the inputs $i _ { 1 } ,$ $i _ { 2 } , \ldots , i _ { k } .$ In lieu of these input-reductions, some reductions in outputs $r _ { 1 } , r _ { 2 } , . . . , r _ { t }$ are expected. Let $I = \{ i _ { 1 } , i _ { 2 } , . . . , i _ { k } \}$ be the set of indices corresponding to the inputs that should be reduced and $I ^ { \prime } { = } \{ 1 , 2 , . . . , m \} { - } I .$ Also, let $O = \{ r _ { 1 } , r _ { 2 } , . . . , r _ { t } \}$ be the set of indices corresponding to the outputs that should be reduced and $O ^ { \prime } =$ $\{ 1 , 2 , . . . , s \} - O .$ . The total reduction in i-th input is denoted by $C _ { i } \colon$ i ∈ I. Moreover, the total reduction in r-th output is denoted by $\boldsymbol { F } _ { r } : \boldsymbol { r } { \in } { \boldsymbol { O } }$ . For each $D M U _ { p } : p = 1 , . . . , n$ the levels of reductions in ith input and r-th output are denoted by $c _ { i p }$ and $f _ { r p } ,$ respectively, with $\sum { } _ { p = 1 } ^ { n } c _ { i p } = C _ { i }$ and $\sum { _ { p } ^ { n } } = 1 f _ { r p } = F _ { r }$

In our study, we simply assume that the total ef<sup>fi</sup>ciency of the central decision maker is sum of the ef<sup>fi</sup>ciencies of the DMUs in centralized environment, in other word, $\begin{array} { r } { e ^ { C D M } = \sum _ { p = 1 } ^ { n } e _ { p } , } \end{array}$ in which $e ^ { C D M }$ is the total ef<sup>fi</sup>ciency of central decision maker. In the proposed approach, the aim of central decision maker is to reduce the levels of inputs and outputs in such a way that (i) the level of ef<sup>fi</sup>ciency in each DMU would not decrease as far as possible, (ii) the total ef<sup>fi</sup>ciency of the central decision maker would be improved with respect to its current performance. The approach takes the input usage and output production of each DMU into consideration and rationally, it has been assumed that the input/output reductions are attainable and feasible in the next season. Let $e _ { p }$ be the technical ef<sup>fi</sup>ciency of $D M U _ { p }$ obtained from CCR-model $( 2 )$ . Base on the above comments, we must have:

$$
\begin{array}{l} e _ {p} \leq \frac {\sum_ {r \in O ^ {\prime}} u _ {r} y _ {r p} + \sum_ {r \in O} u _ {r} (y _ {r p} - f _ {r p})}{\sum_ {i \in I ^ {\prime}} v _ {i} x _ {i p} + \sum_ {i \in I} v _ {i} (x _ {i p} - c _ {i p})} \leq 1, p = 1,..., n, \\ \sum_ {p = 1} ^ {n} c _ {i p} = C _ {i}, i \in I, p = 1,..., n, \\ \sum_ {p = 1} ^ {n} f _ {r p} = F _ {r}, r \in O, p = 1,..., n, \\ \sum_ {p = 1} ^ {n} e _ {p} \leq \sum_ {p = 1} ^ {n} \left[ \sum_ {r \in O ^ {\prime}} u _ {r} y _ {r p} + \sum_ {r \in O} u _ {r} (y _ {r p} - f _ {r p}) \right], \\ \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r p}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i p}} \leq 1, p \in E, \\ c _ {i p} \leq x _ {i p}, i \in I, p = 1,..., n, \\ f _ {r p} \leq y _ {r p}, r \in O, p = 1,..., n, \\ u _ {r}, v _ {i} \geq \epsilon , f o r a l l i, r, \\ c _ {i p}, f _ {r p} \geq 0, f o r a l l i, r, p \end{array}\tag{3}
$$

in which E is the set of all CCR-ef<sup>fi</sup>cient DMUs. The <sup>fi</sup>rst n fractions in Eq. (3) de<sup>fi</sup>ne ef<sup>fi</sup>ciency for each $D M U _ { p } { : } p = 1 , . . . , n .$ . The second and third equations ensure that the reduced inputs and outputs sum to precisely $C _ { i }$ and $F _ { r }$ respectively. The fourth and <sup>fi</sup>fth constraints guarantee that the total ef<sup>fi</sup>ciency of the central decision maker should be improved with respect to its current performance. >0 is a non-Archimedean in<sup>fi</sup>nitesimal quantity to enforce strict positivity of the weights u and $\nu _ { i \cdot }$ Since $u _ { r } , v _ { i } , f _ { r p }$ and $c _ { i p }$ are decision variables, the system of Eq. (3) is clearly nonlinear. If we make the change of variables $u _ { r } f _ { r p } =$ $\bar { f } _ { r p }$ and $v _ { i } c _ { i p } = \bar { c } _ { i p }$ , then, the system (3) reduces to the following form:

$$
\begin{array}{l} e _ {p} \leq \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {r \in O} \bar {f} _ {r p}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i p} - \sum_ {i \in I} \bar {c} _ {i p}} \leq 1, p = 1,..., n, \\ \sum_ {p = 1} ^ {n} \bar {c} _ {i p} = v _ {i} C _ {i}, i \in I, p = 1,..., n, \\ \sum_ {p = 1} ^ {n} \bar {f} _ {r p} = u _ {r} F _ {r}, r \in O, p = 1,..., n, \\ \sum_ {p = 1} ^ {n} e _ {p} \leq \sum_ {p = 1} ^ {n} \left[ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} + \sum_ {r \in O} \bar {f} _ {r p} \right], \\ \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r p}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i p}} \leq 1, p \in E, \\ \bar {c} _ {i p} \leq v _ {i} x _ {i p}, i \in I, p = 1,..., n, \\ \bar {f} _ {r p} \leq u _ {r} y _ {r p}, r \in O, p = 1,..., n, \\ u _ {r}, v _ {i} \geq \epsilon , f o r a l l i, r, \\ \bar {f} _ {r p}, \bar {c} _ {i p} \geq 0, f o r a l l i, r, p. \end{array}\tag{4}
$$

At a rational sight, an equitable reduction is to reduce $c _ { i p } { = } \rho _ { i p } C _ { i }$ and $f _ { r p } { = } \mu _ { r p } F _ { r }$ from $D M U _ { p }$ for each $p { = } 1 , 2 , . . . , n$ . Let us assume $\rho _ { i p } \stackrel { \cdot } { = } \frac { x _ { i p } } { \sum _ { l = 1 } ^ { n } x _ { i l } }$ and $\begin{array} { r } { \mu _ { r p } = \frac { y _ { r p } } { \sum _ { l = 1 } ^ { n } y _ { r l } } } \end{array}$ for each $p { = } 1 , 2 , . . . , n$ with $\begin{array} { r } { \sum _ { p = 1 } ^ { n } \mu _ { r p } = 1 } \end{array}$ <sup>¼</sup>  and $\begin{array} { r } { \sum _ { p = 1 } ^ { n } \rho _ { i p } = 1 } \end{array}$

With these proportions, we take the input usage and output production of all DMUs into consideration. So, it is rational to claim that the input/output reductions are attainable and feasible in the next season. The dif<sup>fi</sup>culty with these values to $c _ { i p }$ and $f _ { r p }$ is that there is no guarantee that they satisfy Eq. (4). In the absence of such reduction, we introduce goals achievement variables for ef<sup>fi</sup>ciency, inputs and outputs levels. Let

$$
\begin{array}{l} \left[ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {r \in O} \bar {f} _ {r p} \right] - e _ {p} \left[ \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} - \sum_ {i \in I} \bar {c} _ {i p} \right] = T _ {p} ^ {+} - T _ {p} ^ {-}, p = 1,..., n, \\ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {r \in O} \bar {f} _ {r p} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} + \sum_ {i \in I} \bar {c} _ {i p} = s _ {p} ^ {+} - s _ {p} ^ {-}, p = 1,..., n, \\ \bar {f} _ {r p} - \mu_ {r p} u _ {r} F _ {r} = \theta_ {r p} ^ {+} - \theta_ {r p} ^ {-}, r \in O, p = 1,..., n, \\ \bar {c} _ {i p} - \rho_ {i p} v _ {i} C _ {i} = \varphi_ {i p} ^ {+} - \varphi_ {i p} ^ {-}, i \in I, p = 1,..., n. \end{array}
$$

The nonnegative variables $T _ { p } { } ^ { + } , T _ { p } { } ^ { - } , s _ { p } { } ^ { + } , s _ { p } { } ^ { - } , \theta _ { r p } { } ^ { + } , \theta _ { r p } { } ^ { - } , \varphi _ { i p } { } ^ { + }$ and ${ { \varphi } _ { i p } } ^ { - }$ are called deviational variables and they represent the deviations above and below of the goals. To guarantee the feasibility and to ensure that each DMU can improve its ef<sup>fi</sup>ciency level, we consider the following:

$$
\begin{array}{l} \left[ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {r \in O} \bar {f} _ {r p} \right] - e _ {p} \left[ \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} - \sum_ {i \in I} \bar {c} _ {i p} \right] = T _ {p} ^ {+} - T _ {p} ^ {-}, p = 1, \dots , n, \\ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {r \in O} \bar {f} _ {r p} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} + \sum_ {i \in I} \bar {c} _ {i p} = s _ {p} ^ {+} - s _ {p} ^ {-}, p = 1, \dots , n, \\ \bar {f} _ {r p} - \mu_ {r p} u _ {r} F _ {r} = \theta_ {r p} ^ {+} - \theta_ {r p} ^ {-}, r \in O, p = 1, \dots , n, \\ \bar {c} _ {i p} - \rho_ {i p} v _ {i} C _ {i} = \varphi_ {i p} ^ {+} - \varphi_ {i p} ^ {-}, i \in I, p = 1, \dots , n, \\ \sum_ {p = 1} ^ {n} e _ {p} \leq \sum_ {p = 1} ^ {n} \left[ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} + \sum_ {r \in O} \bar {f} _ {r p} \right], \\ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} \leq 0, p \in E, \\ \sum_ {p = 1} ^ {n} \bar {c} _ {i p} = v _ {i} C _ {i}, i \in I, p = 1, \dots , n, \\ \sum_ {p = 1} ^ {n} \bar {f} _ {r p} = u _ {r} F _ {r}, r \in O, p = 1, \dots , n, \\ \bar {c} _ {i p} \leq v _ {i} x _ {i p}, i \in I, p = 1, \dots , n, \\ \bar {f} _ {r p} \leq u _ {r} y _ {r p}, r \in O, p = 1, \dots , n, \\ u _ {r}, v _ {i} \geq \epsilon , f o r a l l i, r, \\ \bar {f} _ {r p}, \bar {c} _ {i p} \geq 0, f o r a l l i, r, p. \end{array}\tag{5}
$$

We need to minimize $T _ { p } { } ^ { + } , s _ { p } { } ^ { + } + s _ { p } { } ^ { - } , \theta _ { r p } { } ^ { + } + \theta _ { r p } { } ^ { - }$ and ${ \varphi _ { i p } } ^ { + } + { \varphi _ { i p } } ^ { - } .$ Now, a multi-objective linear programming (MOLP) model is developed to determine an optimal input/output reduction. To this end, we solve the following MOLP problem:

$$
\operatorname{Min} \sum_ {p} ^ {n} T _ {p} ^ {+}
$$

$$
\operatorname{Min} \sum_ {p = 1} ^ {n} \left[ S p ^ {+} + S p ^ {-} \right]
$$

$$
\operatorname{Min} \sum_ {p = 1} ^ {n} \sum_ {r \in O} \left[ \theta_ {r p} ^ {+} + \theta_ {r p} ^ {-} \right]
$$

$$
M i n \sum_ {p = 1} ^ {n} \sum_ {r \in O} \left[ \varphi_ {i p} ^ {+} + \varphi_ {i p} ^ {-} \right]
$$

subject to :

$$
\left[ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {r \in O} \bar {f} _ {r p} \right] - e _ {p} \left[ \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} - \sum_ {i \in I} \bar {c} _ {i p} \right] = T _ {p} ^ {+} - T _ {p} ^ {-}, p = 1, \dots , n,
$$

$$
\sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {r \in O} \bar {f} _ {r p} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} + \sum_ {i \in I} \bar {c} _ {i p} = s _ {p} ^ {+} - s _ {p} ^ {-} p = 1, \dots , n,
$$

$$
\bar {f} _ {r p} - \mu_ {r p} u _ {r} F _ {r} = \theta_ {r p} ^ {+} - \theta_ {r p} ^ {-}, r \in O, p = 1, \dots , n,
$$

$$
\bar {c} _ {i p} - \rho_ {i p} v _ {i} C _ {i} = \varphi_ {i p} ^ {+} - \varphi_ {i p} ^ {-}, i \in I, p = 1, \dots , n,
$$

$$
\sum_ {p = 1} ^ {n} e _ {p} \leq \sum_ {p = 1} ^ {n} \left[ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} + \sum_ {r \in O} \bar {f} _ {r p} \right],
$$

$$
\sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} \leq 0, p \in E,\tag{6}
$$

$$
\sum_ {p = 1} ^ {n} \bar {c} _ {i p} = v _ {i} C _ {i}, i \in I, p = 1, \dots , n,
$$

$$
\sum_ {p = 1} ^ {n} \bar {f} _ {r p} = u _ {r} F _ {r}, r \in O, p = 1, \dots , n,
$$

$$
\bar {c} _ {i p} \leq v _ {i} x _ {i p}, i \in I, p = 1, \dots , n,
$$

$$
\bar {f} _ {r p} \leq u _ {r} y _ {r p}, r \in O, p = 1, \dots , n,
$$

$$
u _ {r}, v _ {i} \geq \epsilon , f o r a l l i, r,
$$

$$
\bar {f} _ {r p}, \bar {c} _ {i p} \geq 0, f o r a l l i, r, p.
$$

In Eq. (6) we have $\ [ 3 ( k + t ) + 2 ] n + l + 1$ inequality constraints with $[ 5 ( k + t ) + 2 ] n + m + s$ variables and so the feasibility of the system is guaranteed (note that k,l and t are respectively the cardinalities of I, E and O). If $\bar { f } _ { r p } , \bar { c } _ { i p } , u _ { r } , \nu _ { i } , \varphi _ { i p } { ^ { + } } , \varphi _ { i p } { ^ { - } } , \theta _ { r p } { ^ { + } } , \theta _ { r p } { ^ { - } } , s _ { p } { ^ { + } } , s _ { p } { ^ { - } } , T _ { p } { ^ { + } }$ and $T _ { p } { } ^ { - }$ be an optimal solution to Eq. (6), it would be easy to show that $\dot { f _ { r p } } = \frac { f _ { r p } } { u _ { r } }$ and $c _ { i p } = { \frac { { \bar { c } } _ { i p } } { v _ { i } } }$ satisfy in Eq. (3).

So far, the input/output reduction problem is formulated as a MOLP problem that usually has no unique solution. Considering priorities on the objectives in MOLP model (6), we solve the following linear programming problem:

$$
\begin{array}{c} M i n \psi = \beta_ {1} \sum_ {p = 1} ^ {n} T _ {p} ^ {+} + \beta_ {2} \sum_ {p = 1} ^ {n} \left[ s _ {p} ^ {+} + s _ {p} ^ {-} \right] + \\ \beta_ {3} \sum_ {p = 1} ^ {n} \sum_ {r \in O} \left[ \theta_ {r p} ^ {+} + \theta_ {r p} ^ {-} \right] + \beta_ {4} \sum_ {p = 1} ^ {n} \sum_ {i \in I} \left[ \varphi_ {i p} ^ {+} + \varphi_ {i p} ^ {-} \right] \end{array}
$$

Table 1

Subject to:

$$
\begin{array}{l} \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {r \in O} \bar {f} _ {r p} - e _ {p} \left[ \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} - \sum_ {i \in I} \bar {c} _ {i p} \right] = T _ {p} ^ {+} - T _ {p} ^ {-}, p = 1, \dots , n, \\ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {r \in O} \bar {f} _ {r p} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} + \sum_ {i \in I} \bar {c} _ {i p} = s _ {p} ^ {+} - s _ {p} ^ {-} p = 1, \dots , n, \\ \bar {f} _ {r p} - \mu_ {r p} u _ {r} F _ {r} = \theta_ {r p} ^ {+} - \theta_ {r p} ^ {-}, r \in O, p = 1, \dots , n, \\ \bar {c} _ {i p} - \rho_ {i p} v _ {i} C _ {i} = \varphi_ {i p} ^ {+} - \varphi_ {i p} ^ {-}, i \in I, p = 1, \dots , n, \\ \sum_ {p = 1} ^ {n} e _ {p} \leq \sum_ {p = 1} ^ {n} \left[ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} + \sum_ {r \in O} \bar {f} _ {r p} \right], \\ \sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i p} \leq 0, p \in E, \\ \sum_ {p = 1} ^ {n} \bar {c} _ {i p} = v _ {i} C _ {i}, i \in I, p = 1, \dots , n, \\ \sum_ {p = 1} ^ {n} \bar {f} _ {r p} = u _ {r} F _ {r}, r \in O, p = 1, \dots , n, \\ \bar {c} _ {i p} \leq v _ {i} x _ {i p}, i \in I, p = 1, \dots , n, \\ \bar {f} _ {r p} \leq u _ {r} y _ {r p}, r \in O, p = 1, \dots , n, \\ u _ {r}, v _ {i} \geq \epsilon , f o r a l l i, r, \\ \bar {f} _ {r p}, \bar {c} _ {i p} \geq 0, f o r a l l i, r, p \end{array}\tag{7}
$$

where $\beta _ { 1 } , \beta _ { 2 } , \beta _ { 3 }$ and $\beta _ { 4 }$ are user-de<sup>fi</sup>ned values that re<sup>fl</sup>ect the importance of the objectives and represent positive values with $\beta _ { 1 } + \beta _ { 2 } + \beta _ { 3 } + \beta _ { 4 } = 1$

In model (7), minimizing ψ guarantees to minimize the deviation from ef<sup>fi</sup>ciency level, after reducing inputs and outputs. By minimizing ψ, each DMU proposes a reduction plan. When $\psi = 0$ , the obtained reduction plan yields to an ef<sup>fi</sup>ciency score one for each DMU and each DMU reduces the inputs and outputs proportionate to its inputs consumptions and outputs productions. Moreover, in this case, the total ef<sup>fi</sup>ciency of the central decision maker will increase with respect to its current performance.

An important point to be noted is that this input/output reduction plan may not lead to the highest possible reduction. However, in case we had chosen the highest possible input/output reduction, we would not have taken the ability of DMUs in to consideration and hence this reduction plan might not have been possible and attainable in practice.

Another point in our approach is that in spite of the fact that the ef<sup>fi</sup>- ciency scores of some DMUs may be increased and this score may be decreased for some other DMUs, however, the total ef<sup>fi</sup>ciency of the central decision maker will be improved in the next production season. This means that there is a total progress from the current season to the next one. The following theorem shows that the total ef<sup>fi</sup>ciency of the central decision maker will be improved with respect to its current performance.

Theorem 1. Suppose ${ \cal D } { \cal M } U _ { p } : ( x _ { 1 p } - c _ { 1 p } , . . . , x _ { m p } - c _ { m p } ) , y _ { 1 p } - f _ { 1 p } , . . . , y _ { s p } -$ $y _ { s p } )$ is new input/output plan for $\bar { D M U _ { p } }$ in the next production season and consider the following linear programming problem:

$$
\bar {e} _ {p} = M a x \sum_ {r = 1} ^ {s} u _ {r} \left(y _ {r p} - f _ {r p}\right)
$$

subject to :

$$
\sum_ {i = 1} ^ {m} v _ {i} \left(x _ {i p} - c _ {i p}\right) = 1,\tag{8}
$$

$$
\sum_ {r = 1} ^ {s} u _ {r} y _ {r j} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i j} \leq 0, j \in E,
$$

u ; v ; ≥0; f or all $i , r ,$

Then, we must have $\begin{array} { r } { \sum _ { p = 1 } ^ { n } e _ { p } { \le } \sum _ { p = 1 } ^ { n } \bar { e } _ { p } . } \end{array}$

Proof. Note that $\bar { e } _ { p }$ is the new ef<sup>fi</sup>ciency of DMU with respect to E. The ef<sup>fi</sup>ciency score $e _ { p } ^ { \dot { n } e w }$ of $D M U _ { p }$ is evaluated by solving the following program:

$$
e _ {p} ^ {\text { new }} = \operatorname{Max} \frac {\sum_ {r \in O ^ {\prime}} u _ {r} y _ {r p} + \sum_ {r \in O} u _ {r} \left(y _ {r p} - f _ {r p}\right)}{\sum_ {i \in I ^ {\prime}} v _ {i} x _ {i p} + \sum_ {i \in I} v _ {i} \left(x _ {i p} - c _ {i p}\right)}
$$

subject to :

$$
\left(\sum_ {r \in 0 ^ {\prime}} u _ {r} y _ {r j} + \sum_ {r \in 0} u _ {r} \left(y _ {r j} - f _ {r j}\right)\right) - \left(\sum_ {i \in I ^ {\prime}} v _ {i} x _ {i j} + \sum_ {i \in I} v _ {i} \left(x _ {i j} - c _ {i j}\right)\right) \leq 0, j = 1, 2, \dots , n,\tag{9}
$$

$u _ { r } , v _ { i } , 2 0 .$ ; f or all $i , r ,$

or equivalently

$$
\begin{array}{l} e _ {p} ^ {\text { new }} = \text { Max } \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r p} - \sum_ {r \in O} u _ {r} f _ {r p}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i p} - \sum_ {i \in I} v _ {i} c _ {i p}} \\ \text { subject   to: } \\ \left(\sum_ {r = 1} ^ {s} u _ {r} y _ {r j} - \sum_ {r \in O} u _ {r} f _ {r j}\right) - \left(\sum_ {i = 1} ^ {m} v _ {i} x _ {i j} - \sum_ {i \in I} v _ {i} c _ {i j}\right) \leq 0, j = 1, 2,..., n, \\ u _ {r}, v _ {i}, \geq 0, \text { for   all   } i, r. \end{array}\tag{10}
$$

Taking in to consideration the <sup>fi</sup>fth and sixth constraints in Eq. (7), the proof is evident.

## 4. Illustration with a numerical example

We illustrate the general approach to input/output reduction using a simple example involving 10 DMUs of an organization with two inputs and two outputs. The data are summarized in Table 1. Suppose that the organization has to reduce the <sup>fi</sup>rst input and second output and the amount of these reductions are respectively $C _ { 1 } = 7 5$ and $F _ { 2 } = 1 5 0$ . The problem is “how these inputs and outputs should be reduced from various DMUs in an equitable way without reducing their ef<sup>fi</sup>ciency $I ? "$ Running the CCR model (2) on these data, results in four ef<sup>fi</sup>cient units: $3 , 4 ,$ 6 and 8. Column 8 of Table 1 reports the CCR ef<sup>fi</sup>ciency score for each DMU. We applied model (7) to the data and derived an optimal reduction plan (note that $\beta _ { 1 } = \beta _ { 2 } = \beta _ { 3 } = \beta _ { 4 } = { \frac { 1 } { 4 } } . )$ . Columns 6 and 7 exhibit the amounts of input and output reductions, respectively. We <sup>fi</sup>nally calculated the new ef<sup>fi</sup>ciency scores for all DMUs after reductions and the results are listed in the last column of Table 1. It is interesting that by this reduction plan, all DMUs have an ef<sup>fi</sup>ciency score 1. The optimal values to the deviation variables phi $, \varphi _ { j } ^ { + } , \theta _ { j } ^ { - } , \theta _ { j } ^ { + } , s _ { j } ^ { - }$ and $s _ { j } ^ { + }$ are listed in Table 2. The optimal weights from model (7) are $u _ { 1 } { } ^ { * } = 0 . 0 1 2 2 , u _ { 2 } { } ^ { * } =$ 0:0003; ${ \nu _ { 1 } } ^ { * } = 0 . 0 0 5 3$ and ${ \nu _ { 2 } } ^ { * } = 0 . 0 0 1 0$ with $\psi ^ { * } = 5 6 . 8 4 5 8$

Note that the total ef<sup>fi</sup>ciency of the central decision maker in the current season is $\textstyle \sum _ { p = 1 } ^ { 1 0 } e _ { j } = 8 . 6 6 1 9$ , while, $\begin{array} { r } { \sum _ { p = 1 } ^ { 1 0 } \bar { e } _ { j } = 9 . 2 6 0 4 . } \end{array}$ This means that there is a total progress for central decision maker from current season to the next one.

The data and results for simple example

<table><tr><td> $DMU_j$ </td><td> $x_1$ </td><td> $x_2$ </td><td> $y_1$ </td><td> $y_2$ </td><td> $c_{1j}$ </td><td> $f_{2j}$ </td><td> $e_j$ </td><td> $e_j^{new}$ </td><td> $e_j$ </td></tr><tr><td>1</td><td>185</td><td>235</td><td>57</td><td>59</td><td>0</td><td>0</td><td>0.5855</td><td>0.6198</td><td>0.5855</td></tr><tr><td>2</td><td>173</td><td>224</td><td>65</td><td>91</td><td>6.0924</td><td>0</td><td>0.9384</td><td>0.8123</td><td>0.9757</td></tr><tr><td>3</td><td>159</td><td>145</td><td>79</td><td>84</td><td>4.8436</td><td>83.9726</td><td>1.0000</td><td>1.0000</td><td>1.0261</td></tr><tr><td>4</td><td>158</td><td>199</td><td>83</td><td>88</td><td>3.8030</td><td>65.9316</td><td>1.0000</td><td>1.0000</td><td>1.0142</td></tr><tr><td>5</td><td>175</td><td>221</td><td>74</td><td>73</td><td>0</td><td>0</td><td>0.8031</td><td>0.8450</td><td>0.8031</td></tr><tr><td>6</td><td>159</td><td>212</td><td>85</td><td>69</td><td>0</td><td>0</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>7</td><td>199</td><td>201</td><td>48</td><td>70</td><td>0</td><td>0</td><td>0.6416</td><td>0.6740</td><td>0.6421</td></tr><tr><td>8</td><td>177</td><td>189</td><td>64</td><td>99</td><td>60.2614</td><td>0</td><td>1.0000</td><td>1.0000</td><td>1.5162</td></tr><tr><td>9</td><td>176</td><td>149</td><td>59</td><td>74</td><td>0</td><td>0</td><td>0.8552</td><td>1.0000</td><td>0.8573</td></tr><tr><td>10</td><td>191</td><td>191</td><td>81</td><td>61</td><td>0</td><td>0</td><td>0.8381</td><td>0.9758</td><td>0.8402</td></tr></table>

Table 2  
The deviation variables in illustrative example.

<table><tr><td> $DMU_{j}$ </td><td> $\varphi_{j}^{-}$ </td><td> $\varphi_{j}^{+}$ </td><td> $\theta_{j}^{-}$ </td><td> $\theta_{j}^{+}$ </td><td> $s_{j}^{-}$ </td><td> $s_{j}^{+}$ </td><td> $T_{j}^{-}$ </td><td> $T_{j}^{+}$ </td></tr><tr><td>1</td><td>7.9195</td><td>0.0000</td><td>11.5234</td><td>0.0000</td><td>0.5054</td><td>0.0000</td><td>0.0004</td><td>0.0000</td></tr><tr><td>2</td><td>7.3736</td><td>0.0000</td><td>17.7734</td><td>0.0000</td><td>0.2912</td><td>0.0000</td><td>0.2228</td><td>0.0000</td></tr><tr><td>3</td><td>6.7809</td><td>0.0000</td><td>16.3806</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>4</td><td>6.7436</td><td>0.0000</td><td>17.1674</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>5</td><td>7.4914</td><td>0.0000</td><td>14.2578</td><td>0.0000</td><td>0.2267</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>6</td><td>6.8065</td><td>0.0000</td><td>13.4766</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>7</td><td>8.5188</td><td>0.0000</td><td>13.6719</td><td>0.0000</td><td>0.6510</td><td>0.0000</td><td>0.2003</td><td>0.0000</td></tr><tr><td>8</td><td>7.2586</td><td>0.0000</td><td>19.3359</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>9</td><td>7.5342</td><td>0.0000</td><td>14.4531</td><td>0.0000</td><td>0.3408</td><td>0.0000</td><td>0.1841</td><td>0.0000</td></tr><tr><td>10</td><td>8.1764</td><td>0.0000</td><td>11.9141</td><td>0.0000</td><td>0.1988</td><td>0.0000</td><td>0.0038</td><td>0.0000</td></tr></table>

The deviation variables in bank branches.  
Table 4

## 5. An application in the banking sector

The approach proposed herein is developed for the purpose of assessing the impact of IT on bank performance. Kao and Hwang [11,12] investigated the impact of IT on <sup>fi</sup>rm performance. We used the same data to show the applicability of the proposed approach. Data on 27 <sup>fi</sup>rms are selected and are derived from operations during 1987–1989. We use <sup>fi</sup>ve variables from the data set as inputs and outputs. Three factors are selected as inputs: IT budget $\left( x _ { 1 } \right)$ , <sup>fi</sup>xed assets $\left( x _ { 2 } \right)$ , and the number of employees $\left( x _ { 3 } \right)$ , and two factors as outputs: the dollar value of deposits $( y _ { 1 } ) _ { \cdot }$ and pro<sup>fi</sup>t earned $\left( y _ { 2 } \right)$ . Table 3 shows a listing of the data set. The <sup>fi</sup>rst <sup>fi</sup>ve columns of the table exhibit the original data. We <sup>fi</sup>rst solved the standard DEA model (2) and get the technical ef<sup>fi</sup>ciency scores for each DMU as shown in the nine-th column of the table. As the column shows, four units are CCR ef<sup>fi</sup>cient.

<table><tr><td> $DMU_j$ </td><td> $\varphi_{j}^{-}$ </td><td> $\varphi_{j}^{+}$ </td><td> $\theta_{j}^{-}$ </td><td> $\theta_{j}^{+}$ </td><td> $s_{j}^{-}$ </td><td> $s_{j}^{+}$ </td><td> $T_{j}^{-}$ </td><td> $T_{j}^{+}$ </td></tr><tr><td>1</td><td>0.0000</td><td>0</td><td>0.0388</td><td>0.0000</td><td>0.2004</td><td>0.0000</td><td>0.0347</td><td>0</td></tr><tr><td>2</td><td>0.0000</td><td>0</td><td>0.0569</td><td>0.0000</td><td>0.2145</td><td>0.0000</td><td>0.0574</td><td>0</td></tr><tr><td>3</td><td>0.0000</td><td>0</td><td>0.0608</td><td>0.0000</td><td>0.4705</td><td>0.0000</td><td>0.0854</td><td>0</td></tr><tr><td>4</td><td>0.0000</td><td>0</td><td>0.0353</td><td>0.0000</td><td>0.3098</td><td>0.0000</td><td>0.0788</td><td>0</td></tr><tr><td>5</td><td>0.0000</td><td>0</td><td>0.0397</td><td>0.0000</td><td>0.3402</td><td>0.0000</td><td>0.0637</td><td>0</td></tr><tr><td>6</td><td>0.0000</td><td>0</td><td>0.0637</td><td>0.0000</td><td>0.6273</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>7</td><td>0.0000</td><td>0</td><td>0.1541</td><td>0.0000</td><td>0</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>8</td><td>0.0000</td><td>0</td><td>0.0172</td><td>0.0000</td><td>0.2425</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>9</td><td>0.0000</td><td>0</td><td>0.1784</td><td>0.0000</td><td>1.9207</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>10</td><td>0.0000</td><td>0</td><td>0.0201</td><td>0.0000</td><td>0.4382</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>11</td><td>0.0000</td><td>0</td><td>0.0214</td><td>0.0000</td><td>0.4432</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>12</td><td>0.0000</td><td>0</td><td>0.0271</td><td>0.0000</td><td>0.1821</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>13</td><td>0.0000</td><td>0</td><td>0.1085</td><td>0.0000</td><td>0.1452</td><td>0.0000</td><td>0.0898</td><td>0</td></tr><tr><td>14</td><td>0.0000</td><td>0</td><td>0.0417</td><td>0.0000</td><td>0.8184</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>15</td><td>0.0000</td><td>0</td><td>0.0521</td><td>0.0000</td><td>0.6517</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>16</td><td>0.0000</td><td>0</td><td>0.0177</td><td>0.0000</td><td>0.2104</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>17</td><td>0.0000</td><td>0</td><td>0.0112</td><td>0.0000</td><td>0.1012</td><td>0.0000</td><td>0.0089</td><td>0</td></tr><tr><td>18</td><td>0.0079</td><td>0</td><td>0.0000</td><td>0.0000</td><td>0</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>19</td><td>0.0000</td><td>0</td><td>0.0314</td><td>0.0000</td><td>0.0922</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>20</td><td>0.0000</td><td>0</td><td>0.0256</td><td>0.0000</td><td>0.0377</td><td>0.0000</td><td>0.0373</td><td>0</td></tr><tr><td>21</td><td>0.0000</td><td>0</td><td>0.0179</td><td>0.0000</td><td>0.0599</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>22</td><td>0.0000</td><td>0</td><td>0.0390</td><td>0.0000</td><td>0.1298</td><td>0.0000</td><td>0.0189</td><td>0</td></tr><tr><td>23</td><td>0.0000</td><td>0</td><td>0.0440</td><td>0.0000</td><td>0.133</td><td>0.0000</td><td>0.057</td><td>0</td></tr><tr><td>24</td><td>0.0000</td><td>0</td><td>0.0328</td><td>0.0000</td><td>0.0444</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>25</td><td>0.0000</td><td>0</td><td>0.0180</td><td>0.0000</td><td>0.1713</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>26</td><td>0.0000</td><td>0</td><td>0.0168</td><td>0.0000</td><td>0</td><td>0.0000</td><td>0</td><td>0</td></tr><tr><td>27</td><td>0.0000</td><td>0</td><td>0.0424</td><td>0.0000</td><td>0.0414</td><td>0.0000</td><td>0.0414</td><td>0</td></tr></table>

The IT budget currently is 5.8916 billion dollars. Assume now due to <sup>fi</sup>nancial crises the executive board of bank comes on the pressure to reduce IT budget from 5.8916 to 2.8916, that is saving of 3 billion dollars. Obviously the committee board expects some reduction in the pro<sup>fi</sup>t, however the maximum pro<sup>fi</sup>t reduction accepted by committee board is 2 billion dollars, that is reduction of the pro<sup>fi</sup>t from 11.948 billion dollars to no less than 9.948 billion dollars. We applied the model assuming $C _ { 1 } = 3$ and $F _ { 2 } = 2$ , the results are presented in columns 7 and 8 of Table 3. In this application, we assumed that the importance of ef<sup>fi</sup>ciency, inputs and outputs are same. So, we let $\beta _ { 1 } = \beta _ { 2 } = \beta _ { 3 } =$ $\begin{array} { r } { \beta _ { 4 } = \frac { 1 } { 3 } . } \end{array}$ . Column 10 shows the new ef<sup>fi</sup>ciency of the branches with new input/output plan. As can be seen the new ef<sup>fi</sup>ciencies are greater than the old one and the bank saved 1 billion dollars over all which shows the difference between saving in IT budget and losing in pro<sup>fi</sup>t. The last column of Table 3 shows the ef<sup>fi</sup>ciency scores $\bar { e } _ { p } s .$ One can <sup>fi</sup>nd that $\begin{array} { r } { \sum _ { i = 1 } ^ { 2 7 } e _ { j } = 2 0 . 5 3 0 1 { < } \sum _ { i = 1 } ^ { 2 7 } \bar { e } _ { j } = 2 3 . 8 3 7 7 . } \end{array}$

The optimal values to the deviation variables $T _ { j } ^ { - } , T _ { j } ^ { + } , \varphi _ { j } ^ { - } , \varphi _ { j } ^ { + } , \theta _ { j } ^ { - } , \theta _ { j } ^ { + }$ $S _ { j } ^ { - }$ and $S _ { j } ^ { + }$ are listed in Table 4.

Table 3  
Data and results for bank branches.

<table><tr><td>j</td><td> $x_1$ </td><td> $x_2$ </td><td> $x_3$ </td><td> $y_1$ </td><td> $y_2$ </td><td> $c_{1j}$ </td><td> $f_{2j}$ </td><td> $e_j$ </td><td> $e_j^{new}$ </td><td> $e_j$ </td></tr><tr><td>1</td><td>0.150</td><td>0.713</td><td>13.300</td><td>14.478</td><td>13.300</td><td>0.0734</td><td>0.232</td><td>0.722</td><td>0.764</td><td>0.722</td></tr><tr><td>2</td><td>0.170</td><td>1.071</td><td>16.900</td><td>19.502</td><td>16.900</td><td>0.0832</td><td>0.34</td><td>0.793</td><td>0.823</td><td>0.793</td></tr><tr><td>3</td><td>0.235</td><td>1.224</td><td>24.000</td><td>20.952</td><td>24.000</td><td>0.115</td><td>0.363</td><td>0.634</td><td>0.651</td><td>0.634</td></tr><tr><td>4</td><td>0.211</td><td>0.363</td><td>15.600</td><td>13.902</td><td>15.600</td><td>0.1033</td><td>0.211</td><td>0.663</td><td>0.703</td><td>0.663</td></tr><tr><td>5</td><td>0.133</td><td>0.409</td><td>18.485</td><td>15.206</td><td>18.485</td><td>0.0651</td><td>0.237</td><td>0.632</td><td>0.671</td><td>0.632</td></tr><tr><td>6</td><td>0.497</td><td>5.846</td><td>56.420</td><td>81.186</td><td>56.420</td><td>0.2432</td><td>0.7957</td><td>0.763</td><td>0.765</td><td>0.838</td></tr><tr><td>7</td><td>0.060</td><td>0.918</td><td>56.420</td><td>81.186</td><td>56.420</td><td>0.0293</td><td>1.0253</td><td>1.000</td><td>1.000</td><td>1.962</td></tr><tr><td>8</td><td>0.071</td><td>1.235</td><td>12.000</td><td>11.441</td><td>12.000</td><td>0.0347</td><td>0.1581</td><td>0.555</td><td>0.569</td><td>0.580</td></tr><tr><td>9</td><td>1.500</td><td>18.120</td><td>89.510</td><td>124.072</td><td>89.510</td><td>0.7342</td><td>1.521</td><td>0.625</td><td>0.643</td><td>0.698</td></tr><tr><td>10</td><td>0.120</td><td>1.821</td><td>19.800</td><td>17.425</td><td>19.800</td><td>0.0587</td><td>0.2087</td><td>0.505</td><td>0.507</td><td>0.536</td></tr><tr><td>11</td><td>0.120</td><td>1.915</td><td>19.800</td><td>17.425</td><td>19.800</td><td>0.0587</td><td>0.2118</td><td>0.503</td><td>0.506</td><td>0.534</td></tr><tr><td>12</td><td>0.050</td><td>0.874</td><td>13.100</td><td>14.342</td><td>13.100</td><td>0.0244</td><td>0.1704</td><td>0.669</td><td>0.675</td><td>0.704</td></tr><tr><td>13</td><td>0.370</td><td>6.918</td><td>12.500</td><td>32.491</td><td>12.500</td><td>0.1811</td><td>0.648</td><td>0.949</td><td>1.000</td><td>1.113</td></tr><tr><td>14</td><td>0.440</td><td>4.432</td><td>41.900</td><td>47.653</td><td>41.900</td><td>0.2154</td><td>0.4714</td><td>0.591</td><td>0.599</td><td>0.648</td></tr><tr><td>15</td><td>0.431</td><td>4.504</td><td>41.100</td><td>52.63</td><td>41.100</td><td>0.2109</td><td>0.5581</td><td>0.670</td><td>0.682</td><td>0.728</td></tr><tr><td>16</td><td>0.110</td><td>1.241</td><td>14.400</td><td>17.493</td><td>14.400</td><td>0.0539</td><td>0.1846</td><td>0.676</td><td>0.679</td><td>0.729</td></tr><tr><td>17</td><td>0.053</td><td>0.450</td><td>7.600</td><td>9.512</td><td>7.600</td><td>0.0259</td><td>0.067</td><td>0.718</td><td>0.718</td><td>0.778</td></tr><tr><td>18</td><td>0.345</td><td>5.892</td><td>15.500</td><td>42.469</td><td>15.500</td><td>0.1768</td><td>0.5758</td><td>1.000</td><td>1.000</td><td>1.259</td></tr><tr><td>19</td><td>0.128</td><td>0.973</td><td>12.600</td><td>18.987</td><td>12.600</td><td>0.0626</td><td>0.2194</td><td>0.840</td><td>0.881</td><td>0.885</td></tr><tr><td>20</td><td>0.055</td><td>0.444</td><td>5.600</td><td>7.546</td><td>5.600</td><td>0.0269</td><td>0.153</td><td>0.999</td><td>1.000</td><td>0.999</td></tr><tr><td>21</td><td>0.057</td><td>0.508</td><td>5.700</td><td>7.595</td><td>5.700</td><td>0.0279</td><td>0.1161</td><td>0.774</td><td>0.843</td><td>0.787</td></tr><tr><td>22</td><td>0.098</td><td>0.370</td><td>14.100</td><td>16.906</td><td>14.100</td><td>0.048</td><td>0.233</td><td>0.807</td><td>0.842</td><td>0.807</td></tr><tr><td>23</td><td>0.104</td><td>0.395</td><td>14.600</td><td>17.264</td><td>14.600</td><td>0.0509</td><td>0.263</td><td>0.863</td><td>0.911</td><td>0.863</td></tr><tr><td>24</td><td>0.206</td><td>2.680</td><td>19.600</td><td>36.43</td><td>19.600</td><td>0.1008</td><td>0.4286</td><td>0.955</td><td>0.963</td><td>1.038</td></tr><tr><td>25</td><td>0.067</td><td>0.781</td><td>10.500</td><td>11.581</td><td>10.500</td><td>0.0328</td><td>0.1147</td><td>0.627</td><td>0.630</td><td>0.681</td></tr><tr><td>26</td><td>0.100</td><td>0.872</td><td>12.100</td><td>22.207</td><td>12.100</td><td>0.049</td><td>0.1853</td><td>1.000</td><td>1.000</td><td>1.108</td></tr><tr><td>27</td><td>0.011</td><td>1.757</td><td>12.700</td><td>20.67</td><td>12.700</td><td>0.0052</td><td>0.253</td><td>1.000</td><td>1.000</td><td>2.121</td></tr></table>

As a matter of fact, $\beta _ { 1 } , \beta _ { 2 }$ and β<sub>3</sub> play important role in the LP model (7) and different values to these parameters are led to different reduction plans.

GAMS software on a machine with CPU: Intel Pentium 4 at 2 GHz, RAM: 512 MB is used to our calculation.

## 6. Conclusions and future research

In centralized decision making environment, increasing or decreasing in input consumption or output production involves the participation of all DMUs, each contributing in part to total consumption or production. The present study has focused on a decision-making environment in which a central decision maker controls the inputs and outputs of a set of units and there could be some limitations of the availability of resources, as results the central decision maker may want to reduce the levels of some inputs and outputs. The paper discussed how DEA-based model could be used to determine an optimal input/output reduction plan. The input/output reduction problem is formulated as a MOLP problem that usually has no unique solution. It depends on the priorities de<sup>fi</sup>ned by the central decision maker. The proposed approach seeks to improve the ef<sup>fi</sup>ciency score of each DMU, and the total ef<sup>fi</sup>ciencies of all DMUs will be increased after reduction of the concerned inputs/outputs. It should be pointed out that the approach proposed in this paper considered the proportionate reduction in inputs and outputs. An alternative input/output reduction strategy can be put forward by considering the production/consumption ability of units.

In the DEA model discussed in this paper an assumption of constant returns to scale is considered. The approach is also applicable to variable returns to scale environment. Moreover, <sup>fi</sup>nding a stability intervals for DMUs is an interesting future research.

## Acknowledgment

The authors would like to acknowledge the suggestions received from three anonymous referees that greatly improved the paper. Any errors and omissions are our own.

## References

[1] A. Amirteimoori, M.M. Tabar, Resource allocation and target setting in data envelopment analysis, Expert Systems with Applications 37 (2009) 3036–3039.

[2] J.E. Beasly, Allocating <sup>fi</sup>xed costs and resources via data envelopment analysis, European Journal of Operational Research 147 (2003) 197–216.

[3] A. Charnes, W.W. Cooper, Programming with linear fractional functions, Naval Research Logistics Quarterly 9 (1962) 181–186.

[4] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the ef<sup>fi</sup>ciency of decision making units, European Journal of Operational Research 2 (6) (1978) 429–444.

[5] W.D. Cook, M. Kress, Characterizing an equitable allocation of shared costs: a DEA approach, European Journal of Operational Research 119 (1999) 652–661.

[6] W.D. Cook, J. Zhu, Output deterioration with input reduction in data envelopment analysis, IIE Transactions 35 (2003) 309–320.

[7] W.D. Cook, J. Zhu, Allocation of shared costs among decision making units: a DEA approach, Computers and Operations Research 32 (2005) 2171–2178.

[8] W.W. Cooper, L.M. Seiford, J. Zhu, Handbook of Data Envelopment Analysis, Kluwer Academic Publishers Norwell MA 2004

[9] J. Debreu, The coef<sup>fi</sup>cient of resource utilization, Econometrica 19 (1951) 273–292.

[10] A. Emrouznejad, B.R. Parker, G. Tavares, Evaluation of research in ef<sup>fi</sup>ciency and productivity: a survey and analysis of the <sup>fi</sup>rst 30 years of scholarly literature in DEA, Socio-Economic Planning Sciences 42 (2008) 151–157.

[11] C. Kao, S.N. Hwang, Ef<sup>fi</sup>ciency measurement for network systems: IT impact on <sup>fi</sup>rm performance, Expert Systems with Applications 147 (2009) 197–216.

[12] C. Kao, S.N. Hwang, Ef<sup>fi</sup>ciency measurement for network systems: IT impact on <sup>fi</sup>rm performance, Decision Support Systems 48 (2010) 437–446.

[13] P. Korhonen, Syrjänen, Resource allocation based on ef<sup>fi</sup>ciency analysis, Management Science 50 (2004) 1134–1144

[14] Y. Li, F. Yang, L. Liang, Z. Hua, Allocating the <sup>fi</sup>xed cost as a complement of other cost inputs: a DEA approach, European Journal of Operational Research 197 (2009) 389–401.

[15] T.T. Lin, An ef<sup>fi</sup>ciency-driven approach for setting revenue target, Decision Support Systems 49 (2010) 311–317.

Alireza Amirteimoori is an associate professor in Applied Mathematics & Operations Research group in Islamic Azad University in Rasht, Iran. His research interests lie in the broad area of performance management with special emphasis on the quantitative methods of performance measurement, and especially those based on the broad set of methods known as Data Envelopment Analysis, (DEA). Amirteimoori's papers appear in journals such as International Journal of Mathematics in Operations Research, Applied Mathematics and Computation, Journal of the Operations Research Society of Japan, Journal of Applied Mathematics, Journal of Global Optimization, Optimization, Central European Journal of Operations Research, Expert Systems with Applications, International Journal of Advanced Manufacturing Technology, RAIRO-Operations Research, Applied Mathematical Letters, International Journal of Production Economics and etc.

Ali Emrouzneiad is a Reader in Management Science at the Aston Business School in Birmingham, UK. His areas of research interest include performance measurement and management, ef<sup>fi</sup>ciency and productivity analysis, and data mining. Dr Emrouznejad serves on the editorial board of several scienti<sup>fi</sup>c journals; he is senior editor and one of the founding members of the Data Envelopment Analysis Journal, associate editor of the IMA Journal of Management Mathematics and guest editor to several special issues of journals including Journal of Operational Research Society, Annals of Operations Research, Journal of Medical Systems, and International Journal of Energy Management Sector. He is co-founder of Performance Improvement Management Software (PIM-DEA).
