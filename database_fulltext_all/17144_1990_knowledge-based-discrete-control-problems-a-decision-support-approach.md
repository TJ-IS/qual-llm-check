---
otero_id: 17144
otero_key: "FUA46C6T"
title: "Knowledge based discrete control problems: A decision support approach"
authors: "Hans-Jürgen Sebastian"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90023-k"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge Based Discrete Control Problems: A Decision Support Approach

Hans-Jürgen SEBASTIAN

Technische Hochschule Leipzig, 7030 Leipzig, DDR

The aim of this paper is to applicate the theory and methods of Knowledge Based Systems (KBS) in combination with DSS concepts to develop more practical control models, to reach more efficient and user-friendly solution methods which determine closed optimal controls or control strategies, and to include learning and explanatory abilities into models and solution procedures. The paper deals with the description of discrete control problems (DCP) in case of incomplete information (control under uncertainty). The well known models of DCP will be generalized by introducing a structured knowledge base. An architecture for a Knowledge Based Discrete Control Problem (KBDCP) will be proposed. It contains three interactive Expert Systems which are connected to each other.

![](/api/attachments/FUA46C6T/fulltext/images/d1eb402639e0e7020effaead38d5d4699a3527181e6266c7b430a767991f1a51.jpg)

Hans-Jürgen Sebastian received the Dr.sc.nat. degree from Leipzig University of Technology in 1975. At the Department of Mathematics and Computer Sciences of this University he lectures mathematics, operations research and optimal control. He is author of some books for example of the monograph Discrete Dynamic Optimization (1981). Over the last 15 years he has published articles about optimization, discrete optimal control and knowledge based systems. His

current research work includes knowledge based decision support systems theory and applications.

## 1. Introduction

The aim of this paper is to use the theory and methods of Knowledge Based Systems (KBS) and to combine them with the basic concepts of DSS:

to develop more realistic discrete control models,

\- to make the solution methods which determine "good" controls or control strategies more efficient and user-friendly and,

\- to include learning and explanatory abilities into the models and into the solution procedures.

Therefore, the paper deals primarily with the description of discrete control problems (DCP) aspecially in the case of incomplete informations (control under uncertainty). The well known models of DCP will be generalized by introducing a structured knowledge base. Furthermore, we develop an architecture for a Knowledge Based Discrete Control Problem (KBDCP), which consists mainly of three interactive Expert Systems connected to each another.

The third topic of the paper is the modelling of the diagnosis and of the control subsystem. These theoretical approaches show that the subsystems proposed are not common expert systems, but more general Knowledge Based Decision Support Systems (KBDSS).

The paper does not deal with the problem of optimality. Nevertheless, there are interesting new questions of the optimality of the controls related to the diagnosis approach for system-state-sets we are using. For this optimization problem see [8].

Before we start with these topics, let's briefly give a short outline about Expert Systems and a more detailed description of the disadvantages of the models and methods of DCP known from the literature.

Expert Systems are Information Systems, which

represent sets of knowledge (in the form of facts, rules, frames, semantic networks, ...),

![](/api/attachments/FUA46C6T/fulltext/images/1d4647955f2c80ed69037c611526128a29104caa8d7fadacf536c8c5000d4de6.jpg)  
Fig. 1. The Architecture of an Expert System.

\- help to acquisite and to change some of this knowledge,

\- are able to find conclusions (new knowledge) using the stored knowledge by performing inferences and,

\- are able to explain their knowledge and the solution (inference) process.

Following this definition (see [1]), we come to an architecture of an Expert System obtained in fig. 1, which has to be combined with the model base, the data base and some other parts of a DSS to get a KBDCP.

In the following we discuss some of the disadvantages of the existing models and methods of discrete time control problems including uncertainties of a general type.

\- In many applications it is on principle impossible to know the actual system state exactly. All the well known approaches to handle this situation like the stochastic, the adaptive or the min-max approach lead to large numerical problems.

\- The forecasting of time dependent parameters is very difficult or even impossible to realize automatically.

\- The analytic or algorithmic description of the control domain of a discrete time control problem, is the common way to obtain feasibility. However, this description does not include the knowledge of “similar situations or decisions in the past", of "non- or suboptimality of subsets", more generally spoken it does not include the mathematical knowledge about the problem and the algorithms available.

\- The known discrete control models don't have learning abilities in the sense of machine learning, only parameter-learning is included. The models and consequently the computer implementations don't have explanatory facilities.

In the following, we include some of the points mentioned above in a more general discrete control model by using a structured knowledge base and the Expert Systems technology. As a result we don't get just an Expert System like defined above, but a knowledge based decision support system (DSS) which consists of a combination of an interactive DSS with Expert System technology.

## 2. Knowledge Based Discrete Control Problems - Modelling

## 2.1. Notations, Definitions

We consider finite stage control problems. The stages are denoted by $i = 1, 2, \ldots, N$ . Stages i are time intervals $i := [t_{i-1}, t_i]$ , $i = 1, \ldots, N$ .

\- At each stage $i$ the system state is represented by a state vector $x_{i} \in X_{i} \subseteq R^{a}$ . The state set $X_{i}$ is a subset of an Euclidean space $R^{a}$ . $i = 1, 2, \ldots, N$ . As an initial state we introduce $x_{0} \in X_{0}$ , $x_{N}$ is called terminal state of the process.

\- With $m_i$ we denote the parameter vector of the system considered at stage $i + 1, i = 0, 1, \ldots, N - 1$ . The parameter vectors are assumed to be not controllable, they are belonging to a parameter set $M_i \subseteq R^c$ .

\- The control vector at stage $i+1$ is denoted by $u_i$ , $u_i \in U_i(x_i, m_i) \subseteq R^b$ for $i=0, 1, \ldots, N-1$ . The control domain $U_i(x_i, m_i)$ depends on the state vector of the stage $i$ and on the parameter vector of stage $i+1$ .

With this notations we can illustrate the discrete time control process like in fig. 2.

\- In many applications the states are not directly observable or measurable or in some sense only inexactly known. Therefore we still introduce an observation vector $y_i$ of stage $i$ , which belongs to an observation set $Y_{i}, y_{i} \in Y_{i}, i = 1, 2, \ldots, N$ .

![](/api/attachments/FUA46C6T/fulltext/images/1d635a04bcde57f872730a933feeb5dae6fd505890256a48b27ef7434fb023ef.jpg)  
Fig. 2. Discrete Time Control Process.

## 2.2. The model

Using these four kinds of vectors, we can formulate a discrete time control model like follows (see also fig. 2).

$$
\begin{array}{l} \text {(1) State Equations} \\ T _ {i} \colon X _ {i} \times U _ {i} \times M _ {i} \to X _ {i + 1} \\ (T _ {i} \text { unique mapping into } X _ {i + 1}), \\ x _ {i + 1} = T _ {i} (x _ {i}, u _ {i}, m _ {i}) \quad \text { for } \quad i = 0, 1, \dots , N - 1, \\ U _ {i} \supseteq \bigcup_ {x _ {i}, m _ {i}} U _ {i} (x _ {i}, m _ {i}). \end{array}
$$

(2) Objective Function

$$
\begin{array}{l} Z \big (x _ {0}, x _ {1}, \dots , x _ {N}; u _ {0}, u _ {1}, \dots , u _ {n - 1} \big) \\ = \sum_ {i = 0} ^ {N - 1} W _ {i} \big (x _ {i}, u _ {i} \big) + W _ {N} \big (x _ {N} \big) \Rightarrow \max \end{array}
$$

with

$$
W _ {i} \colon X _ {i} \times U _ {i} \rightarrow R ^ {1},
$$

$W_{N}: X_{N} \to R^{1}, 1 \geqslant 1$ , integer.

For $l \geqslant 2$ we have a multiobjective problem.

## (3) Information Spectrum

The most important part of the model is the so called information spectrum (fig. 3).

We introduce the following notations:

$$
\begin{array}{r l} _ {i} a & = \left(a _ {0}, a _ {1}, \dots , a _ {i}\right), \\ & \quad a _ {j}, j = 0, 1, \dots , i, \text {vector} \\ w _ {i} & = \left(m _ {i}, m _ {i + 1}, \dots , m _ {N - 1}\right), \text {complete parameter} \\ & \quad \text {forecast} \\ w _ {i, n} & = \left(m _ {i}, m _ {i + 1}, \dots , m _ {i + n - 1}\right), n \geqslant 1, \text {integer}, \end{array}
$$

parameter forecast with time horizon n.

The set $\zeta_{i}$ including all informations available to the decision maker at time point $t_{i}$ (it means to choose $u_{i}$ ) is called information-set at time point (stage), i.

![](/api/attachments/FUA46C6T/fulltext/images/909450865ae50f27070aedba794111a201b0232347f7235c5e67ee998d10a0ba.jpg)  
Fig. 3. Complete Information Structure.

Consequently, we have

$$
\zeta_ {i} \subseteq \left\{\underbrace {_ {i} y , _ {i} x , _ {i - 1} m , _ {i - 1} u} _ {\text { complete   history }}; \underbrace {w _ {i}} _ {\text { complete   future }} \right\}.
$$

For our model we consider the following special information set:

$$
\zeta_ {i} ^ {*} \subseteq \left\{_ {i} y, _ {i - 1} m, _ {i - 1} u; (w _ {i, n}, w _ {i + n}) = w _ {i} \right\}.
$$

The tuple $S_{\mathrm{inf}} = (\zeta_0^*, \zeta_1^*, \ldots, \zeta_{N-1}^*)$ we call information spectrum independent on the state history $_i x$ .

## (4) Knowledge Base

The real new part of the model is the knowledge base. We propose a knowledge base structured into 3 parts:

(a) Knowledge Base, KB (D), for the diagnosis of states on the base of observations,

(b) Knowledge Base, KB (M), for the determination of a control vector (knowledge about feasibility, about optimality, about methods and algorithms available to the problem).

(c) Knowledge Base, KB (F), for the generation of parameter-forecasting on the base of observations, estimations and from statistics.

In section 3 we will give some examples for such knowledge bases to illustrate the ideas of this approach, however it seems to be impossible to give a complete overview of the knowledge bases in detail in such a paper.

## 2.3. Architecture of the Knowledge Based Discrete Control Problem (KBDCP)

In fig. 4 we show the architecture of the proposed KBDCP. The notations used in this figure will be explained later. The idea is, to combine three interactive Expert Systems, each related to the corresponding knowledge base KB (D), or KB (M) or KB (F) respectively.

## (1) Diagnosis Expert System

The input data are observations, measurements and a set $X_{i}^{*}$ of states computed by applying the state transformation. This information is needed to have the actual fact-knowledge about the system. Applying the set of diagnose rules, the Expert System performs interactively the result $X_{i}^{\prime}$ , it means it determines a subset $X_{i}^{\prime} \subseteq X_{i}$ and concludes the unknown state $x_{i}$ belonging to $X_{i}^{\prime}$ , $x_{i} \in X_{i}^{\prime}$ .

## (2) Forecasting Expert System

To generate control actions, the system needs a complete, $w_{i}$ , or an incomplete, $w_{i,n}$ , parameter-forecasting, respectively. In reality peoples observe or measure some data or disturbances, estimate the future development. However, they are, in general, not able to find a real good forecasting for the time depending parameter vectors $m_{j}$ using the given factual knowledge, their own experiences with disturbances and the existing inexact rules. An interactive Expert System may therefore help to perform a reasonable parameter forecasting in form of a set $W_{i}^{\prime}$ of vectors $w_{i}$ . The modelling of this Expert System will be considered in another publication [7].

![](/api/attachments/FUA46C6T/fulltext/images/12a6ac2280447f846709ea5109e9b017a6828a53225e6f88fb70ce3d3145ac0d.jpg)  
Fig. 4. KBDCP - Proposed Architecture.

## (3) Control Expert System

On the base of the diagnose result $X_{i}^{\prime}$ and the result of the forecasting procedure $W_{i}^{\prime}$ an “Control” Expert System performs interactively a control vector $\hat{u}_{i}$ or a control set $\hat{U}_{i}$ respectively, which is recommended from the system to be a “good” control action at time point $t_{i}$ .

Furthermore, this Expert System uses the knowledge about feasibility and optimality in dependence on $X_{i}^{\prime}$ and the knowledge on available methods and algorithms for determination of $\hat{u}_{i}$ or $\hat{U}_{i}$ .

It means, the Control Expert System needs the results of the parallel working interactive Expert Systems for diagnosis and parameter forecasting. Because of the dynamic character of our system which has to be controlled, we have a “real time requirement”. The interactive decision support process starting at time point $t_{i}$ and using the three Expert Systems proposed needs a random time $\epsilon_{i}$ . So we have to assume, that our process is slow enough, with other words, that we have time enough to decide,

$$
0 <   t _ {i} + \epsilon_ {i} \ll t _ {i + 1} \sim \epsilon_ {i} \ll t _ {i + 1} - t _ {i} = \Delta .
$$

There are many examples of real processes for which this requirement is fulfilled, for instance in chemical process control and for some control processes in complex production, transportation and inventory systems.

## 3. Modelling of the Expert Systems - Theoretical Approach

## 3.1. The Diagnosis Expert System

Let us consider stage $i-1$ and let be “ $x_{i-1} \in X_{i-1}'$ ” the knowledge about the state vector at time point $t_{i-1}$ .

The consequences of this assumption are:

(a) The set $U_{i-1}(x_{i-1}, m_{i-1})$ is unknown at time point $t_{i-1}$ (because $x_{i-1}$ is unknown). Therefore it is impossible to choose $u_{i-1}$ .

(b) It is impossible to compute $x_{i}$ from $T_{i - 1}$ , $x_{i} = T_{i - 1}(x_{i - 1}, u_{i - 1}, m_{i - 1})$ since $x_{i - 1}$ and $u_{i - 1}$ are unknown.

There are some possible ways to overcome this difficulties:

\- The insurance (pessimistic) approach: Define $U_{i-1}^{*}(X_{i-1}', m_{i-1}) = \bigcap_{x_{i-1} \in X_{i-1}'} U_{i-1}(x_{i-1}, m_{i-1})$ (assumed to be not empty) and assume $u_{i-1} \in U_{i-1}^{*}(X_{i-1}', m_{i-1})$ . This approach decreases the control domain, but the control actions are feasible independent on the real value of $x_{i-1}$ .

\- Some stochastic approach: We interprete $x_{i-1}$ as a random vector with values in $X_{i-1}'$ and require some probability $P(\cdot)$ not smaller than a given safetyfactor

$$
P \left(u _ {i - 1} \in U _ {i - 1} (\bullet)\right) \geqslant \alpha .
$$

In the following, we consider the “insurance (pessimistic) approach”. Applying the reduced control domain $U_{i-1}^{*}(X_{i-1}^{\prime}, m_{i-1})$ we introduce the reachable subset $X_{i}^{*}$ of the state domain by

$X_{i}^{*}=\left\{x_{i}=T_{i-1}(x_{i-1},u_{i-1},m_{i-1})/x_{i-1}\in X_{i-1}^{\prime}\right\}$ with $u_{i-1}\in U_{i-1}^{*}(X_{i-1}^{\prime},m_{i-1}),m_{i-1}\in M_{i-1}$ chosen to be fixed. This set should be known and to be used for the diagnosis of the set $X_{i}^{\prime}$ (of the stage i). If we take into account, that the Expert System performs his diagnose result on the base of the observation vector $y_{i}$ , than we can conclude:

The Expert System realizes a diagnosis mapping $D_{i}$

$$
\begin{array}{l} D _ {i} \colon Y _ {i} \times P (X _ {i}) \to P (X _ {i}), \\ \left(P (X _ {i}) - \text { power   set   of } X _ {i}\right) \end{array}
$$

$(D_{i}$ maps from the Cartesian product $Y_{i} \times P(X_{i})$ into the power set $P(X_{i})$ of $X_{i}$ ,

$$
X _ {i} ^ {\prime} = D _ {i} \left(y _ {i}; X _ {i} ^ {*}\right),
$$

such, that (1) $X_{i}^{\prime}\subseteq X_{i}^{*}$ or (2) $X_{i}^{\prime}\cap X_{i}^{*}\neq$ $\emptyset$ , respectively.

Well known observation equations like $x_{i}=Dy_{i}+c$ with matrices D and c are special cases, but more general mappings $D_{i}$ needs not to be unique, in many cases there is no analytic description of $D_{i}$ .

The diagnosis mapping may be defined for instance, by a set of facts and rules like: (1) If $y_{i} = \mathring{y}_{i} \in Y_{i}$ , then $x_{i} \in X_{i}'(\mathring{y}_{i})$ . Rules (1) may be defined for a finite set of observations $\mathring{y}_{i}$ only.

For other cases we could have rules like (2) If $y_{i} \subseteq \mathring{Y}_{i}$ , then (p) $x_{i} = \mathring{x}_{i} \in X_{i}'(\mathring{Y}_{i})$ . For a finite set of subsets $\mathring{Y}_{i}$ of $Y_{i}$ these can be defined. This is a case of inexact reasoning, because the conclusion is valid only with a probability $p$ depending on $\mathring{Y}_{i}$ . (3) If $X_{i_1^*} = \mathring{X}_i^*$ and $y_{i} \subseteq Y_{i}$ , then (q) $x_{i} = \mathring{x}_{i} \in X_{i}'(\mathring{X}_{i}^{*}, Y_{i})$ . It means inexact reasoning with probability $q$ . The rules are defined for finite number of sets $\mathring{X}_{i}^{*}$ and observation subsets $\mathring{Y}_{i}$ . These rules are highly aggregated. In general, $D_{i}$ is given by sets of depending on each another rules.

We remark, that there are still other possibilities to model this diagnosis process. For instance, let us consider the following fuzzy approach. We denote with $\bar{x}_{i}$ the real (unknown) state vector. $X_{i}^{\prime}$ denotes a fuzzy set in $X_{i}$ . The membership function $\mu_{i}(x_{i})$ describes the “possibility” of “ $x_{i}=\bar{x}_{i}$ ” for each $x_{i}\in X_{i}$ . Let us consider the case

$$
\mu_ {i} \left(x _ {i}\right) = \left\{ \begin{array}{l l} 0 & \text { for } x _ {i} \in X _ {i} \setminus X _ {i} ^ {\prime} \\ \mu_ {i} ^ {+} \left(x _ {i}\right) > 0 & \text { for } x _ {i} \in X _ {i} ^ {\prime}. \end{array} \right.
$$

Then, the diagnosis problem is to determine the fuzzy set $X_{i}^{\prime}$ in $X_{i}$ characterized by the membership function $\mu_{i}^{+}(x_{i})$ .

## 3.2. The Control Expert System

For more simplicity in the notations, in the following, we assume the parameters $m_{i}$ considered to be fixed (given numerically). Therefore we will have no parameters $m_{i}$ in our notations.

Let us compare the classical control problem, with our generalization using different knowledge bases.

In the classical control problem the situation is characterized like follows:

\- The state vector $x_{i}$ is known (with some uncertainties),

\- The feasible control function $h_i$ is defined by

$$
h _ {i} \colon X _ {i} \to U _ {i}; u _ {i} = h _ {i} (x _ {i}) \in U _ {i} (x _ {i}),
$$

$$
\begin{array}{l} h ^ {i} = \left(h _ {i}, h _ {i + 1}, \dots , h _ {N - 1}\right) \\ \text { is   a   feasible   control   policy }, \end{array}
$$

$$
i = 0, 1, \dots , N - 1.
$$

\- At any stage $i$ , we have the (local) control problem! determine $u_{i} \in U_{i}(x_{i})$ or the (local) synthesis problem! determine $h_{i}$ .

Of course, it would be also possible to support the solution process of these local problems by knowledge based systems. We will do this, however, related to our control problem with unknown states:

\- The state vector $x_{i}$ is unknown. As a result of a diagnose mapping we get: $x_{i} \in X_{i}'$ with a known subset $X_{i}'$ of $X_{i}$ .

\- The feasible control function $h_i$ is defined by:

$h_i: P(X_i) \to U_i$ with

$$
u _ {i} = h _ {i} \left(X _ {i} ^ {\prime}\right) \in U _ {i} ^ {*} \left(X _ {i} ^ {\prime}\right) \subseteq U _ {i},
$$

$$
U _ {i} ^ {*} \left(X _ {i} ^ {\prime}\right) = \bigcap_ {x _ {i} \in X _ {i} ^ {\prime}} U _ {i} \left(x _ {i}\right),
$$

$$
h ^ {i} = \left(h _ {i}, h _ {i + 1}, \dots , h _ {N - 1}\right).
$$

\- At any stage $i$ , we have the (local) control problem! determine $u_{i} \in U_{i}^{*}(X_{i}^{\prime})$ or the (local) synthesis problem! determine $h_{i}(X_{i}^{\prime})$ ; Find for each subset $X_{i}^{\prime} \subseteq X_{i}$ a control vector $u_{i}$ , which belongs to $U_{i}^{*}(X_{i}^{\prime})$ .

For the solution of the local control problem it is necessary to formulate the Control Knowledge Base in three main parts.

(α) Knowledge Base of the stage i (including: feasibility description, property description (optimality, non-optimality, heuristics), method- and algorithm base),

(β) Knowledge Base of the control history, experiences from similar processes (learning),

(γ) Knowledge base of the whole discrete control problem.

We restrict our considerations to the part ( $\alpha$ ) and we introduce (in the sense of an example) an approximation to get a finite set of rules. (For this approach we choose a structured rule-based system to model the domain knowledge of the local control problem. Of course, there are alternative possibilities for this knowledge representation.)

Notations and assumptions: $u_{i}^{(j)}$ is a control-parameter $j = 1,2,\ldots ,b$ of the stage $i,i$ assumed to be fixed. $u_{i} = (u_{i}^{(1)},\dots,u_{i}^{(b)})$ is a control-vector. We assume, that there is a finite number $K$ of subsets $X_{i}(k)$ of $X_{i}, k = 1,2,\dots,K$ with the property: $\bigcup_{k}X_{i}(k) = X_{i}$ and $X_{i}(k_{1})\cap X_{i}(k_{2}) = \emptyset$ for each $k_{1}\neq k_{2}$ .

With these notations and the assumption that we can reduce our consideration on a finite set

$X_{i}(1),\ldots,X_{i}(K)$ of state-subsets (state classes) we can formulate the local Knowledge Base (stage i) as follows.

Primary constraints (feasibility): “If $x_{i} \in X_{i}(k)$ , then $u_{i} \in U_{i}(k)$ ” for each $k = 1, 2, \ldots, K$ (K production rules to describe feasibility; $U_{i}(k) := U_{i}(X_{i}(k))$ ).

Property based constraints (heuristics): Example 1: Not-optimal subsets. For each $k$ , a subset $U_i^{NO}(k)$ of $U_i(k)$ which does not include "optimal-control-vectors", is known ( $K$ facts: " $U_i^{NO}(k) \subseteq U_i(k)$ is a not-optimal-control-set"). Additionally, there may be known $R$ subsets $\overline{X}_i(r)$ of $X_i$ , $r = 1, 2, \ldots, R$ with $\overline{X}_i(r) = X_i(k)$ for some $k$ or $\overline{X}_i(r) = \bigcup_{k \in K'} X_i(k)$ , $K' \subseteq \{1, 2, \ldots, K\}$ ,

which generate the following R constraints “If $x_{i} \in \overline{X}_{i}(r)$ , then the set $\overline{U}_{i}(\overline{X}_{i}(r))$ does not include optimal-control-vectors” (R production rules, $\overline{U}_{i}(\overline{X}_{i}(r)) \subseteq U_{i}(\overline{X}_{i}(r))$ .) To apply this kind of rules, it's necessary to add the following rule to the set of primary constraints

$$
\text {   "   If   } x _ {i} \in \bigcup_ {k \in K ^ {\prime}} X _ {i} (k), \text {   then   } u _ {i} \in \bigcap_ {k \in K ^ {\prime}} U _ {i} (k) \text {. }
$$

Example 2: Good-control-vectors. For each k, a subset $U_{i}^{G}(k)$ of $U_{i}(k)$ , which includes only “good-control-vectors”, is known (K facts: “ $U_{i}^{G}(k) \subseteq U_{i}(k)$ is a good-control-set”; remark the connections with “properties, methods and algorithms”). Additionally, there may be known T subsets $X_{i}^{+}(t)$ (defined as $\overline{X}_{i}(r)$ ), which generate the T constraints: “If $x_{i} \in X_{i}^{+}(t)$ , then the set $U_{i}^{+}(X_{i}^{+}(t))$ includes only good-control-vectors” (T production rules, $U_{i}^{+}(X_{i}^{+}(t)) \subseteq U_{i}(X_{i}^{+}(t))$ . It is easy to see, that we could describe “good-control-vectors”, with fuzzy sets and introduce inexact reasoning.

Control-set depending on the diagnosis-result $X_i'$ : We determine the set $K'$ of all $k \in \{1, 2, \ldots, K\}$ with $X_i' \cap X_i(k) \neq \emptyset$ . We approximate $X_i'$ by $\bigcup_{k \in K'} X_i(k) = X_i''$ and use the rules formulated above to determine the control domain.

Properties, methods and algorithms: This part of the local knowledge base contains the mathematical knowledge about the problem and may have connections to the more heuristic “property based constraints”. We give here only examples of such kind of mathematical knowledge. For more simplicity we choose as example the well known classical dynamic programming. Let be, according to $(\gamma)$ , a kind of discrete dynamic programming available to our problem. Furthermore let be the dimension of $X_{i}$ low enough to solve the Bellmanean functional equations numerically. Then, the following rules could be available:

(R1) “If X is convex and $W(x, u)$ , $W_{N}(x)$ are concave functions and $T(x, u)$ is a linear transformation and $U(x)$ is a convex-set function, then the function $W_{i}(x, u) + f_{i+1}(T(x, u))$ which has to be maximized is a concave function in $X \times U''$ .

![](/api/attachments/FUA46C6T/fulltext/images/46576af1251ae56ba3cf40c55f5fa5d454d82924e7907cac365e4e82cbd173b7.jpg)  
Fig. 5. And–Or Graph.

(R2) “If $G_{i}(x, u) = W_{i}(x, u) + f_{i+1}(T(x, u))$ is a concave function in $X \times U$ , then $G_{i}(x, u)$ is for each $x \in X$ a concave function in $u \in U(x)$ (Property-Property-Rules).

(R3) “If $G_{i}(x, u)$ is for each $x \in X$ a concave function in $u \in U(x)$ and $U(x)$ is a convex set for each $x \in X$ , then compute $\operatorname{Max}_{u \in U(x)} G_{i}(x, u) =: f_{i}(x)$ for each $x \in X_{G} \subseteq X$ applying a concave maximization algorithm taken from $\{A_{1}, A_{2}, \ldots, A_{c}\}$ .

(R4) If the assumption of rule R3 holds and furthermore the are valid $U(x) = R^{b}$ and $G_{i}(x, u)$ is differentiable with respect to u, then use the free maximization gradient algorithm $A_{1}$ (Property-Action-Rules).

Using And-Or graphs we can represent such kind of knowledge in the following way (fig. 5). Of course these four rules show only in principle one possible way to make the mathematical knowledge available for the control expert system.

We remark that it is possible to translate such a structured local knowledge base consisting in the parts

\- primary constraints (feasibility),

– property-based constraints (heuristics),

\- control-set (depending on the diagnosis result), and

– properties, methods and algorithms,

into a PROLOG-programme or to use an Expert System Shell (rule based system) to make experiments with such a subsystem. The formulation of the parts ( $\beta$ ) and ( $\gamma$ ) of the control knowledge base and an optimization approach will be published in [8].

We have considered an example of our approach for the field of inventory control systems. It gives a combination of the well known dynamic inventory control problems with knowledge based and decision support methods. We consider as state variables the available stock level (at time point $t_{i}$ ) of a product or material p, which is stored at some places of a (large) storage. (Even if the stock level at the time point considered is known, it has to be diagnostized interactively, which part of this stock can really be used – is available – at this time point.)

As control variables we use variables for input and output (of products into or from the storage) and ordering-variables for all products (materials) which are considered. Furthermore, the time-dependent (partly unknown) parameters describe the future demand of each of the products to be stored. Our approach – in my opinion – helps to build more realistic dynamic DSS for such kind of inventory-control problems. For a detail description of this application see [7].

## References

[1] Appelrath, H.-J., Von Datenbanken zu Expertensystemen, in: Informatik-Fachberichte 102, Springer, 1985.

[2] Savory, S., Künstliche Intelligenz und Expertensysteme, Oldenburg Verlag München, Wien, 1985.

[3] Sebastian, H.-J., Sieber, N., Diskrete Dynamische Optimierung, Geest & Portig K.G. Leipzig, 1981.

[4] Sebastian, H.-J., Sieber, N., Optimale Steuerung von Prozessen und ihre Anwendungen Wissenschaftliche Zeitschrift der TH Leipzig, Heft 6, 1986.

[5] Sebastian, H.-J., Ehrenberg, D., Wissensbasierte Entscheidungsunterstützende Systeme (WES) in der Lagerhaltung. Wissenschaftliche Zeitschrift der TH Leipzig, Heft 1, 1987.

[6] Trippler, G., Sebastian, H.-J., On a Discrete Optimal Control Problem with Incomplete Information. Optimization 16 (1985) 1, 71–85.

[7] Sebastian, H.-J., Knowledge Based Discrete Control Problems - An Example from the Field of Inventory Control. Wissenschaftliche Zeitschrift der TH Leipzig, to appear.

[8] Sebastian, H.-J., Knowledge Based Discrete Control Problems - The Optimality Problem. Optimization, to appear.
