---
otero_id: 19808
otero_key: "CN9Z46CH"
title: "Bayesian Stackelberg games for cyber-security decision support"
authors: "Yunxiao Zhang; Pasquale Malacaria"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113599"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Decision Support Systems

Bayesian Stackelberg games for cyber-security decision support

Yunxiao Zhang, Pasquale Malacaria

![](/api/attachments/CN9Z46CH/fulltext/images/4fb1ab97063fdb67ac4ddc5e26f6f8b3b14b4ca6d5379fbe9568360c40ac6bc6.jpg)

PII: S0167-9236(21)00109-3

DOI: https://doi.org/10.1016/j.dss.2021.113599

Reference: DECSUP 113599

To appear in: Decision Support Systems

Received date: 7 January 2021

Revised date: 12 May 2021

Accepted date: 12 May 2021

Please cite this article as: Y. Zhang and P. Malacaria, Bayesian Stackelberg games for cyber-security decision support, Decision Support Systems (2021), https://doi.org/10.1016/ j.dss.2021.113599

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2021 Published by Elsevier B.V.

# Bayesian Stackelberg games for cyber-security decision support

Yunxiao Zhang , Pasquale Malacaria

Queen Mary University of London, United Kingdom

## Abstract

A decision support system for cyber-security is here presented. The system aims to select an optimal portfolio of security controls to counteract multi-stage attacks. The system has several components: a preventive optimisation to select controls for an initial defensive portfolio, a learning mechanism to estimate possible ongoing attacks, and an online optimisation selecting an optimal portfolio to counteract ongoing attacks. The system relies on efficient solutions of bi-level optimisations, in particular, the online optimisation is shown to be a Bayesian Stackelberg game solution. The proposed solution is shown to be more efficient than both classical solutions like Harsanyi transformation and more recent efficient solvers. Moreover, the proposed solution provides significant security improvements on mitigating ongoing attacks compared to previous approaches. The novel techniques here introduced rely on recent advances in Mixed-Integer Conic Programming (MICP), strong duality and totally unimodular matrices.

Keywords: Attack graphs, Bayesian Stackelberg games, Cyber-security, Security games, Security investment

## 1. Introduction

Cyber-security is a concerning challenge to any organisation that uses IT devices to conduct daily business and activities. Digital assets like customer information and confidential product data are high-profile targets to those financially motivated cyber-attackers. Recent research [1, 2, 3, 4] addresses the question of how to select an optimal portfolio of security controls to counteract potential cyber-attacks. Other studies like [5, 6, 7] focus on the learning mechanism to detect and estimate ongoing attacks for an organisation.

In this work, we present a decision support system for an organisation to determine optimal security portfolios to counteract multi-stage (potential and ongoing) attacks. The system consists of a preventive optimisation to select an optimal preventive security portfolio to counteract potential attacks, a learning mechanism to estimate possible ongoing attacks, and an online optimisation to determine an optimal corrective security portfolio in response to the detected ongoing attacks. The preventive optimisation helps the organisation determine an optimal preventive security portfolio prior to attacks. In the later phases of normal operations, the learning mechanism will trigger alerts once an attack is detected. After being triggered, the online optimisation helps the organisation determine an optimal corrective security portfolio to mitigate ongoing attacks.

We use a probabilistic attack graph [1, 2, 4, 8, 9, 10, 11] to represent real-world multi-step attacks: nodes represent “privilege states” of the attacker, and each edge represents a vulnerability through which the attacker can transit between states as a result of successful exploitation. The attacker penetrates the organisation by choosing a sequence of exploitation actions, forming a path from source nodes to the target nodes. The security risk associated with a path is the probability of that attack path successfully reaching the target.

Specifically, we focus on the preventive and the online optimisation problems to efficiently determine optimal security portfolios for the organisation. In the initial security investment, the preventive optimisation is formulated as a standard Stackelberg game: the defender is the leader who selects a preventive security portfolio to minimise the potential security risk, and the attacker is the follower who maximises the potential security risk by choosing the most critical path from the source to the target. In particular [1] provides an efficient approach that can precisely solve this optimisation problem.

In the online $\mathrm { o g } ^ { * }$ misation, the defender has incomplete information about the attacker state: the defender cannot directly observe the attacker state but only estimate it through a sequence of alerts (i.e. observations). The attacker state is hence represented by a probability distribution – a belief vector. Each state in the vector corresponds to one type of the attacker who can mount specific multi-step attacks starting from that node. The online optimisation is thus a Bayesian Stackelberg game [12, 13]. The Harsanyi transformation is a classic technique to solve Bayesian Stackelberg games by transforming Bayesian games into a normal-form matrix game. Unfortunately, such a technique is not suitable for cyber-security problems with a large attack space since the transformation may result in an exponentially large intractable payoff matrix.

Thus, we propose an efficient approach to precisely solve these Bayesian Stackelberg games.

## 1.1. Contributions

This work’s main technical contribution is a new solution algorithm for the organisation solving the online optimisations (i.e. Bayesian Stackelberg games) over probabilistic attack graphs to select optimal corrective security portfolios. Several significant computational improvements to the classical Harsanyi transformation for Bayesian Stackelberg games have been proposed in the literature [13, 14, 15]. The approach in this paper provides a further dramatic computational improvement, over these works, for the precise solution of such $\mathbf { \hat { \Pi } } ^ { \mathbf { \Pi } ^ { - } \mathbf { \hat { \Pi } } ^ { \mathbf { \hat { \Pi } } } \mathbf { \hat { \Pi } } ^ { \mathbf { \hat { \Pi } } ^ { \mathbf { \hat { \Pi } } } } }$ . We use the property of totally unimodular matrices and strong duality to convert the online optimisation into a MICP conic structures in the mixed-integer optimisation [16, 17], we can efficiently solve a MICP by existing solvers (e.g. MOSEK version 9.2): an online optimisation problem over a complete attack graph with 50 nodes $( 2 . 8 1 \times 1 0 ^ { 1 4 }$ paths for an attacker to select) and 50 attacker types needs only an average of 179 seconds to solve.

The solution algorithm is part of the novel decision support system to provide optimal security portfolios for an organisation when facing both potential and ongoing attacks.

## 1.2. Related work

Several game-theoretical approaches have been used to model the interaction between the defender and the attacker, a particularly successful approach being based on Stackelberg games and Bayesian Stackelberg games [1, 13, 14, 15, 18]. In [18] the authors prove several results about the interchangeability of Nash and Stackelberg equilibrium in security games and the restriction on real attacking scenarios. The closest work to this paper is [1] where the cyber-security defence problem is formulated as a Stackelberg game with a probabilistic attack graph modelling all possible attack scenarios. We use [1] for our first stage preventive optimisation. Compared to [1] we distinguish types of controls from the perspective of the time when they become effective [19, 20]. Thus, we can split our budgets into different kinds of security portfolios that mitigate potential and ongoing attacks, respectively. The models in [3, 4] are also similar to our first stage optimisation in terms of the security risk, and the direct and indirect costs in the objective functions, but they only consider single-step attacks instead of multi-step attack scenarios. Other well known “single-step” approaches include: [2] that uses financial engineering tools like value-at-risk and conditional value-at-risk, and [21] that proposes a risk assessment and optimisation model to study the trade-off between financial costs and risk. The optimisation in [22] uses the strongest preventive measure of security to minimise the maximum reward for an optimal attacker.

Our second stage online optimisation is formulated as a Bayesian Stackelberg game. The Harsanyi transformation [12] is a classic technique to solve this kind of game. An efficient and exact method to solve Bayesian Stackelberg games, known as the Decomposed Optimal Bayesian Stackelberg Solver (DOBSS), has been developed in [13]: here a game is decomposed in multiple smaller problems. Further works, e.g. Hierarchical Bayesian solver for General Stackelberg games (HBGS) [14] and Handling Uncertainty Efficiently using Relaxation (HUNTER) [15], significantly improves the scalability over previous approaches. However, they are still not efficient enough for cyber-security games over large attack graphs. Our work also decomposes the game into multiple small problems; in addition, we apply the properties of totally unimodular matrices and strong duality to convert the cyber-security game into a tractable MICP. A recent study [23] considers how to use LP (linear programming) relaxations but it only focuses on general normal-form Stackelberg games. Unlike [23] and other previous approaches, our optimisation does not need a normal-form matrix to represent all possible values of security risk. More detailed reviews on Stackelberg security games can be found in [24, 25].

The general problem of cyber-security investment has been studied in a number of papers. One of the initial works is [26]: their model considers both the costs and benefits when determining the optimal level of investment. Recent work [27] linearises the classic exponential function of breach probability in [26] to select optimal security safeguards for Industry 4.0 supply chains. Similarly, the latest study [28] develops a multivariate model to quantify the costs of cyber-attacks and security. The cyber risk propagation problem is investigated in [29] with a two-echelon supply chain, and in [30] where the influence of insurance policies is taken into account. The recent work in [31] develops an efficient linear optimisation to simultaneously mitigate direct and indirect propagated cyber risk in a multi-tier supply chain.

There are several approaches to detect a complex multi-step attack, such as decision trees, neural nets and hidden Markov models (HMMs). In a direct comparison, [6] has shown HMMs generally perform better than two other approaches. We here directly apply well developed HMM approaches, such as [5, 7, 6], to the learning and inference module in our decision support system.

## 2. Mathematical modelling

A high-level description of the decision support system presented in this work is illustrated in Figure 1. It consists of two optimisation modules: the selection of an optimal preventive security portfolio in the initial investment and optimal corrective portfolios in the online defence (the online optimisation). Moreover, in order to learn the attacker behaviours from past data, an HMM-based learning module is added. Next, the inference module estimates the current attack state based on the sequence of alerts, given the system parameters for the learning module, and returns a belief to the online defence.

Figure 1: The framework of the decision support system.

In the initial investment, the defender focuses on minimising the potential security risk prior to attacks within limited budgets. The problem is formulated as a standard Stackelberg game: the defender selects an optimal preventive security portfolio to mitigate an optimal attacker who finds the most critical path to the target. In addition, the fraction of available budgets reserved for the online defence problem is also determined by solving the Pareto front.

Since the ongoing attacks are hidden, and only the alerts triggered by the attacker are observable, an HMM is embedded into the learning and inference module to return the best belief. Many learning algorithms and inference algorithms for HMMs have been developed for detecting real-time multi-step attacks. We refer interested readers to the previous works in [5, 7, 6, 32], and we will not repeat them here.

Within the remaining budgets after the initial investment, the online defence focuses on minimising the ongoing security risk when an attack is occurring. Because of the hidden attacker state, the problem is a Bayesian Stackelberg game where the defender only has a belief vector representing a probability distribution over the nodes where the attacker could be. Thus, we consider the expected security risk as the expectation over the security risks corresponding to each attacker type. Every attacker type aims to find the path with the highest probability of success given the security portfolio selected by the defender. Thus, we treat the inner problem as multiple smaller attacker’s maximisation problems. With a series of conversions, the original Bayesian Stackelberg game is reformulated as a standard MICP that can be efficiently solved by existing solvers.

## 2.1. Attack graph model

We use a probabilistic attack graph to model the security risk of an organisation. The nodes in the attack graph represent the “privilege states” of the attacker, and the edges are the exploitation of a vulnerability that allows the attacker to change its privilege state. Each edge is associated with the success probability of the exploitation attempts $\mathrm { c o r r e s p o } ^ { r \bullet \bullet } \mathfrak { u } _ { \varpi }$ o that edge. The success probability of the exploitation attempts is determined by t $\mathrm { ~ \ ' ~ e ~ } _ { \mathrm { { L a s c } - l i n e } }$ probability of success $\pi _ { e }$ and the effectiveness of controls, $p _ { e c l }$ , applied on edge. In each privilege state, the attacker can take one of the available attack steps, corresponding to a directed edge out of that node. All of such edges share the same head but may have different tails. Such a probabilistic attack graph $G = ( \mathcal V , \mathcal E , \overline { { h } } , t , p , s , T )$ is defined as a directed multi-graph where node and edge sets are noted $\nu , \varepsilon$ tates of an attacker in an organisation, and an edge e can hence represent a possible attack step between two privilege states. $\overline { { h } } , t$ are functions returning head and tail of an $\mathrm { e d } \mathfrak { g } \doteq ; \mathbf { \xi } _ { r } \mathfrak { r }$ is a function returning the attacker’s probability of success of an edge; s T, represent the initial node in the graph and the target node in the graph respectively. These are the same notations as [1] (in Section 3.1). As outlined in the same work, this structure is general enough to model attacks over several targets with different impacts and losses. The security risk of an attack graph is defined as the highest success probability of attacks across all possible paths. Different impacts and losses for different targets can be described by adding a new target node and create edges to this new target node from all real target nodes, then use the $\pi$ on these edges to model differences in losses, e.g. if target $t _ { 1 }$ has double loss than target $t _ { 2 }$ then add target node $t _ { 3 }$ , add edges $t _ { 1 }  t _ { 3 }$ with $\pi _ { t _ { 1 } t _ { 3 } } = 1$ and $t _ { 2 }  t _ { 3 }$ with $\pi _ { t _ { 2 } t _ { 3 } } = 0 . 5$

## 3. Initial investment: a preventive optimisation

In the initial investment, we are interested in preventive controls that are implemented prior to an attack. The set of all available preventive controls is denoted by $\mathcal { C } _ { p }$ and a preventive security portfolio can be expressed using binary indicators $x _ { c l }$ satisfying:

$$
x _ {c l} \in \{0, 1 \}, \forall c \in \mathcal {C} _ {p}, \forall l \in \mathcal {L} (c); \sum_ {l \in \mathcal {L} (c)} x _ {c l} \leq 1, \forall c \in \mathcal {C} _ {p}.\tag{1}
$$

A control c can be potentially implemented at different intensity levels. We thus let $\mathcal L ( c )$ denote the set of intensity levels for control c . The interpretation of the binary decision variables x is as follows: if control c at intensity level l is selected, then $x _ { c l } = 1$ ; otherwise, $x _ { c l } = 0$ sum of binary indicators of all levels of control c is less than or equal to one.

A control can be effective on multiple edges, and an edge may be affected by multiple controls. Thus, we denote the subset of preventive controls that is effective on edge e by $\mathcal { C } _ { p } ( e )$ Even in the case that no control is implemented on $\operatorname { c i } _ { \theta } ~ e$ , the base-line probability $\pi _ { e }$ may not be one as it relates to the difficulty of exploiting underlying vulnerabilities. Implementation of security controls will reduce the probability of the successful attack step associated with that edge. The attacker must “break” every implemented control to finally succeed (this assumption of independence of controls is justified in [1]). Thus the overall probability of the successful exploitation of edge e is denoted by:

$$
p _ {e} (r) = \pi_ {e} \prod_ {c \in \mathcal {C} _ {p} (e), l \in \mathcal {L} (c)} \left(p _ {e c l} x _ {c l} + \left(1 - x _ {c l}\right)\right).\tag{2}
$$

If $x _ { c l } = 1$ , the corresponding effectiveness is $p _ { e c l }$ ; otherwise, for $x _ { c l } = 0$ it is 1.

Since the implementation of security controls is not cost-free, the selection of controls must be subject to budget constraints. Moreover, exhausting all available budgets in the initial investment is not a wise decision because the online defence will have no budget left for corrective controls responding to ongoing attacks. Thus, the organisation has to find the most profitable security portfolio that can significantly reduce the potential security risk while still keeping sufficient budgets for the online defence. Two kinds of costs must be considered by the organisation. They are the direct cost and the indirect cost defined as:

$$
D (x) = \sum_ {c \in \mathcal {C} _ {p} (e), l \in \mathcal {L} (c)} x _ {c l} \text {Cost} _ {\text {cl}},\tag{3}
$$

$$
I (x) = \sum_ {c \in \mathcal {C} _ {p} (e), l \in \mathcal {L} (c)} x _ {c l} \text {IndirectCost} _ {\mathrm{cl}}.\tag{4}
$$

The direct costs usually refer to monetary investment, and the indirect cost are the side-effects on normal operations, e.g. a service slowdown, a strict access control, etc. Suppose the total budgets for the direct costs and the indirect costs are $B _ { D }$ and $B _ { I }$ , respectively. The fractions of the direct budget and the indirect budget to be used in the initial investment are denoted by $p _ { D }$ and $p _ { I }$ . In other words, the available direct budget and the available indirect budget in the initial investment are $p _ { D } \times B _ { D }$ and $p _ { I } \times B _ { I }$ <sub>I</sub> . We have hence the following constraints:

$$
D (x) \leq p _ {D} \times B _ {D}, I (x) \leq p _ {I} \times B _ {I}.\tag{5}
$$

Note that they are equivalent to $\sum _ { c \in \mathcal { C } _ { p } ( e ) , l \in \mathcal { L } ( c ) } x _ { c l } \mathsf { C o s t } _ { \mathrm { c l } } \le p _ { { P } } \ : B _ { D }$ and

$\sum _ { c \in { \mathcal { C } } _ { p } ( e ) , l \in { \mathcal { L } } ( c ) } x _ { c l } \mathrm { I n d i r e c t C o s t } _ { \mathrm { c l } } \leq p _ { I } \times B _ { I }$ Both variables $p _ { D }$ and $p _ { I }$ should be decided in a manner that balances the potential security risk and the remaining budgets $B _ { D } - D ( x )$ and $B _ { I } - I ( x )$ reserved for the online defen $p _ { D }$ and $p _ { I }$ would be to run the Pareto front and find the values that provide the best return over investment.

This leads to the following optimisation problem to find an optimal preventive security portfolio:

$$
\begin{array}{c} \min _ {x} r _ {s} (x), \\ \text { s.t.:(1),(15) } \end{array}\tag{6}
$$

$$
r (c) = \max _ {\omega_ {s \rightarrow T}} \prod_ {e \in \omega_ {s \rightarrow T}, c \in \mathcal {C} _ {p} (e), l \in \mathcal {L} (c)} \pi_ {e} \left(p _ {e c l} x _ {c l} + \left(1 - x _ {c l}\right)\right).\tag{7}
$$

where $\omega _ { s  T }$ is a path from the source (node 0) to the target, and $r _ { s }$ is the security risk: the highest probability that attacker successfully reaches the target from the source.

Here we give a high-level summary of how this optimisation is solved in [1]. First the optimisation variable $\omega _ { s  T }$ is translated into new binary variables $\tau _ { e } , e \in \mathcal { E }$ : for each edge e , $\tau _ { e }$ represents whether the attacker selects that edge as a part of his attack path. Equation (7) can be equivalently expressed as $r _ { s } = \mathrm { m a x } _ { \{ \tau _ { e } , e \in \mathcal { E } \} } \prod _ { e \in \mathcal { E } } ( \tau _ { e } p _ { e } + 1 - \tau _ { e } )$ subject to the linear flow conversion constraints and the binary constraints. Refer to Lemma 1 in [1].

Since a logarithm function, log( )x , is strictly monotone for $x > 0$ , we can convert the product to a sum: $\log ( r _ { s } ) = \operatorname* { m a x } _ { \{ \tau _ { e } , e \in \mathcal { E } \} } \sum _ { e \in \mathcal { E } } \log ( \tau _ { e } p _ { e } + 1 - \tau _ { e } )$ . Noting $\tau _ { e }$ is a binary variable: if $\tau _ { e } = 0$ , then log $( \tau _ { e } p _ { e } + 1 - \tau _ { e } ) = 0$ ; else if $\tau _ { e } = 1$ , then $\log ( \tau _ { e } p _ { e } + 1 - \tau _ { e } ) = \log ( p _ { e } )$ . Hence, this can be further simplified to a linear form $\log ( r _ { s } ) = \operatorname* { m a x } _ { \{ \tau _ { e } , e \in \mathcal { E } \} } \sum _ { e \in \mathcal { E } } \tau _ { e } \log ( p _ { e } )$ . So far, the original nonlinear maximization problem (7) has been relaxed to an integer linear programming (ILP) subject to the same constraints. Thanks to Lemma 2 (totally unimodular matrices) in [1], such an ILP can be further exactly relaxed to a linear programming (LP): the binary constraints (i.e. ${ \tau _ { e } } \in \{ 0 , 1 \} ,$ ) are equivalent to $\tau _ { e } \geq 0 , \ \forall e \in \mathcal { E }$

Thanks to the exact relaxation and strong duality in LP, we can dualize the original maximization problem. The resulting minimisation LP is:

$$
\min _ {x, \rho} \rho_ {s} - \rho_ {T},\tag{8}
$$

s.t.:(1), (15),

$$
\rho_ {\underline {{t}} (e)} - \rho_ {\overline {{h}} (e)} \geq \sum_ {c \in \mathcal {C} _ {p} (e), l \in \mathcal {L} (e)} x _ {e l} \log (p _ {e c l}) + \log (\pi_ {e}), \forall e \in \mathcal {E}.\tag{9}
$$

where the $\rho$ is a vector of dual variables for the inner maximization. The detailed conversions ${ \boldsymbol { \prime } } _ { \mathcal { A } } \colon$ discuss how to determine $p _ { D }$ and $\boldsymbol { p } _ { \boldsymbol { I } }$ using the Pareto front.

Example: Let’s consider the example illustrated in Figure 2. We assume the base-line probability of the successful attack step associated with all unprotected edges to be one, i.e. $\pi _ { e } = 1$ for all $e \in { \mathcal { E } }$ . Suppose the set of preventive control is $\mathcal { C } _ { p } = \{ c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } , c _ { 6 } , c _ { 7 } \}$ , and the set of $\mathcal { C } _ { c } = \{ c _ { 5 } , c _ { 6 } , c _ { 7 } , c _ { 8 } , c _ { 9 } , c _ { 1 0 } \}$ . These corrective controls are to be selected in the online defence, and we will clarify this point in the next toy example. Note control $c _ { 5 } , \ : \ : c _ { 6 }$ and $c _ { 7 }$ are both preventive and corrective, hence can be selected both in the initial investment and the online defence. The effectiveness of controls is as follows:

$$
\begin{array}{l} c _ {1} = 0. 5, c _ {2} = 0. 2, c _ {3} = 0. 1, c _ {4} = 0. 2, c _ {5} = 0. 5, \\ c _ {6} = 0. 6, c _ {7} = 0. 5, c _ {8} = 0. 2, c _ {9} = 0. 6, c _ {1 0} = 0. 3. \end{array}
$$

Figure 2: An example of an attack graph

Suppose each control has direct and indirect costs one, and both budgets are 7, i.e. $B _ { D } = 7$ and $B _ { \scriptscriptstyle I } = 7$ . We examine the solutions of Pareto front with $p _ { D }$ and $p _ { I }$ equal to (1/ 7, 2 / 7, ,1) , respectively. We present the solutions of the Pareto front in Table 1.

Table 1: Pareto front of the toy example

<table><tr><td> $(p_{D}, p_{I})$ </td><td>controls</td><td>budget used</td><td>security risk</td></tr><tr><td>(1/7, 1/7)</td><td> $[c_{2}]$ </td><td>1</td><td>1</td></tr><tr><td>(2/7, 2/7)</td><td> $[c_{2}, c_{3}]$ </td><td>2</td><td>0.200</td></tr><tr><td>(3/7, 3/7)</td><td> $[c_{1}, c_{2}, c_{3}]$ </td><td>3</td><td>0.100</td></tr><tr><td>(4/7, 4/7)</td><td> $[c_{2}, c_{3}, c_{6}, c_{7}]$ </td><td>4</td><td>0.072</td></tr><tr><td>(5/7, 5/7)</td><td> $[c_{1}, c_{2}, c_{3}, c_{6}, c_{7}]$ </td><td>5</td><td>0.050</td></tr><tr><td>(6/7, 6/7)</td><td> $[c_{1}, c_{2}, c_{3}, c_{5}, c_{6}, c_{7}]$ </td><td>6</td><td>0.036</td></tr><tr><td>(1, 1)</td><td> $[c_{1}, c_{2}, c_{3}, c_{4}, c_{5}, c_{6}, c_{7}]$ </td><td>7</td><td>0.030</td></tr></table>

Figure 3: Pareto front of the toy example w.r.t. $( p _ { p } , p _ { I } )$

Selection of $p _ { D }$ and <sub>I</sub>p $\gamma _ { I }$ : In the toy example, the most profitable $p _ { D }$ and $p _ { I }$ are of 0.2 (dropped by 0.8, i.e. from 1 to 0.2) and (3 / 7,3 / 7) with security risk of 0.1 ( further dropped by 0.1, i.e. from 0.2 to 0.1). The remaining budgets are 5 and 4, respectively. In this case, we select controls $\left[ c _ { _ 2 } , \ c _ { _ 3 } \right]$ as the preventive security portfolio because it remains sufficient budgets for the online algorithm and also significantly reduces the security risk. In addition, $c _ { 1 }$ is a less effective control (with the effectiveness of 0.5). Instead of implementing control $c _ { 1 }$ , we prefer to reserve budgets for the online defence. The preference of a control over another is determined by the reduction in security risk and the costs, which depends on the effectiveness of a control, the edges where the control is available and the costs.

## 4. Online Defensive Algorithm

Let x be the portfolio consisting of the set of all active controls selected by previous optimisations. The current security risk is then denoted by $r _ { i } ( y ; x )$ . The corrective security portfolio can be expressed by binary indicators $y _ { c l }$ satisfying:

$$
y _ {c l} \in \{0, 1 \}, \forall c \in \mathcal {C} _ {c}, \forall l \in \overline {{\mathcal {L}}} (c); \quad \sum_ {l \in \overline {{\mathcal {L}}} (c)} y _ {c l} \leq 1, \forall c \in \mathcal {C} _ {c}.\tag{10}
$$

The online optimisation will select controls and their levels based on both the effectiveness in reducing the overall expected security risk and the costs to obtain an optimal portfolio. If such a control is in the previously implemented portfolio, a higher intensity level can be selected in the online defence. We denote the set of higher intensity levels of control c by $\overline { { \mathcal { L } } } ( c )$

For example, let c be a control with three intensity levels: $L _ { 1 } , \ L _ { 2 }$ and $L _ { 3 }$ . Suppose control $c$ with $L _ { \mathrm { 1 } }$ has been selected in the previously implemented portfolio. The higher intensity level set, $\overline { { \mathcal { L } } } ( c ) = \{ L _ { 2 } , L _ { 3 } \}$ , has two corresponding binary indicators $y _ { c , L _ { 2 } }$ and $y _ { c , L _ { 3 } }$ . If $\sum { } _ { l \in \overline { { \mathcal { L } } } ( c ) } y _ { c l } = 0$ , control c remains uncha ge at level $L _ { \mathrm { 1 } }$ ; otherwise, a higher intensity level of control c is selected (i.e. either $y _ { c , r } \mathrm { ~ \ - ~ } 1$ o $y _ { c , L _ { 3 } } = 1 )$ ). On the other hand, if the previous optimisation has not selected $\smash { \mathbf { C } \mathbf { C } _ { \alpha , \mathrm { ~ } } ^ { \prime } \mathbf { \Psi } _ { 0 , \mathrm { ~ } } c }$ control c with a zero intensity level “ $L _ { 0 }$ ” is set is $\overline { { \mathcal { L } } } ( c ) = \{ L _ { 1 } , L _ { 2 } , L _ { 3 } \}$ , so any of three levels of control c can be selected in this corrective security portfolio. Similarly, the direct and indirect budget constraints for the online defence are:

$$
\overline {{\mathcal {P}}} (y; x) = \sum_ {c \in \mathcal {C} _ {c}, l \in \overline {{\mathcal {L}}} (c)} y _ {c l} \overline {{\operatorname{Cost}}} _ {c l} \leq \mathrm{dir} _ {t} (B _ {D} - D (x))\tag{11}
$$

$$
\overline {{I}} (y; x) = \sum_ {c \in \mathcal {C} _ {c}, l \in \overline {{\mathcal {L}}} (c)} y _ {c l} \overline {{\text {IndirectCost}}} _ {c l} \leq \operatorname{ind} _ {t} (B _ {I} - I (x)),\tag{12}
$$

where and di $\mathtt { r } _ { t } , \mathtt { i n d } _ { t } \le 1$ are the fractions of the remaining budget to be spent for one corrective optimisation at time $t : \ \mathrm { d i } \mathtt { r } _ { t } , \mathrm { i n d } _ { t } \leq 1$ depends on the length of the attack, which can be estimated but not precisely determined a priori. One principled way to find reasonable ${ \mathrm { d i } } \mathtt { r } _ { t }$ and ind would be to run the Pareto front and find the values of ${ \mathrm { d i } } \ttSigma _ { t }$ and ind that provide the best return over investment.

To reduce the expected security risk, we formulate the online defence as a min-max optimisation: the defender finds an optimal corrective security portfolio to mitigate an optimal attacker who is in one of multiple nodes. Suppose the inference module at time t returns a belief vector $B ( X _ { t } ) = ( b _ { 0 } , . . . , b _ { n } )$ , where each $b _ { i }$ denotes the likelihood that the attacker is in node i at time t . The optimisation problem is as follows:

$$
\min _ {y} \sum_ {i \in \mathcal {S} _ {0}} b _ {i} r _ {i} (y; x),\tag{13}
$$

$$
\begin{array}{l} \text {s.t.: (10),(1011),(101112),} \end{array}
$$

$$
r _ {i} (y; x) = \max _ {\omega_ {i \rightarrow T}} \prod_ {e \in \omega_ {i \rightarrow T}} p _ {e} (y; x), \forall i \in \mathcal {S} _ {0},\tag{14}
$$

where $ { \boldsymbol { S } } _ { 0 }$ is the set of nodes with non-zero belief, $\omega _ { i  T }$ is a path from the node i to the target, and $p _ { e } ( y ; x )$ denotes the overall probability of the successful exploitation of edge e given the previously implemented portfolio x :

$$
p _ {e} (y; x) = \pi_ {e} (x) \prod_ {c \in \mathcal {C} _ {c} ^ {(e)}, l \in \mathcal {C} _ {c} ^ {(e)}} (\rho_ {e}, y _ {c l} + (1 - y _ {c l})).\tag{15}
$$

## 4.1. Solving the online defence optimisation

The constraint (14) can be replaced by an inequality constraint, that is

$$
r _ {i} (y; x) \geq \max _ {\omega_ {i \rightarrow T}} \prod_ {e \in \omega_ {i \rightarrow T}} p _ {e} (y; x), \forall i \in \mathcal {S} _ {0}.\tag{16}
$$

Since it is a minimisation, the optimisation will push all security risks (i.e. r ) down. Thus (14) and (16) are equivalent. Because of properties of totally unimodular matrices and strong duality of the maximization (refer to [1]), such an inequality constraint can be converted as follows:

$$
\begin{array}{l} \log (r _ {i} (y; x)) \geq \min _ {\rho^ {i}} \{\rho_ {i} ^ {i} - \rho_ {T} ^ {i}: \rho_ {\underline {{t}} (e)} ^ {i} - \rho_ {\overline {{h}} (e)} ^ {i} \geq \\ \sum_ {c \in \mathcal {C} _ {c} (e), l \in \overline {{\mathcal {L}}} (c)} y _ {c l} \log (p _ {e c l}) + \log (\pi_ {e} (x)), \forall e \in \mathcal {E} _ {i} \}, \end{array}\tag{17}
$$

where $\mathcal { E } _ { i }$ is the set of edges in the subgraph starting with node i . This can be further relaxed to

$$
\exists \rho^ {i}: \log (r _ {i} (y; x)) \geq \rho_ {i} ^ {i} - \rho_ {T} ^ {i}; \text { and }\tag{18}
$$

$$
\rho_ {\underline {{t}} (e)} ^ {i} - \rho_ {\overline {{h}} (e)} ^ {i} \geq \sum_ {c \in \mathcal {C} _ {c} (e), l \in \overline {{\mathcal {L}}} (c)} y _ {c l} \log (p _ {e c l}) + \log (\pi_ {e} (x)), \forall e \in \mathcal {E} _ {i}.\tag{19}
$$

Next, we convert the problem into a standard MICP. Let $R _ { i } = \log ( r _ { i } ( y ; x ) )$ . The objective function becomes a sum of exponential functions:

$$
\sum_ {i \in \mathcal {S} _ {0}} b _ {i} \exp (R _ {i}) = \sum_ {i \in \mathcal {S} _ {0}} \exp (z _ {i})\tag{20}
$$

where $z _ { i } = R _ { i } + \log ( b _ { i } )$

Definition 1. The exponential cone is a convex subset of $\mathbb { R } ^ { 3 }$ [33]:

$$
\mathcal {K} _ {\text { exp }} = \mathbf {c l} \left\{\left(m _ {1}, m _ {2}, m _ {3}\right): m _ {1} \geq m _ {2} \exp \left(m _ {3} / m _ {2}\right), m _ {2} > 0 \right\}.\tag{21}
$$

Let $u _ { i }$ , for $i \in S _ { 0 }$ , be optimisation variables. Then, the online problem converts to a MICP with exponential cones:

$$
\arg \min _ {y, \{\rho^ {i}, i \in \mathcal {S} _ {0} \}, R, u, z i \in \mathcal {S} _ {0}} \sum u _ {i},\tag{22}
$$

$$
\mathrm{s.t.}: ((u _ {i}, 1, z _ {i}) \in \mathcal {K} _ {e x p},\tag{23}
$$

$$
z _ {i} = R _ {i} + \log (b),
$$

$$
(1 8), (1 9)), \forall i \in \mathcal {S} _ {0}; (1 0), (1 1), (1 2).\tag{24}
$$

Proposition 1. The conic constraint (23) is equivalent to the inequality $u _ { i } \geq \exp ( z _ { i } )$ . Minimising $\sum _ { i \in S _ { 0 } } u _ { i }$ subject to the conic constraints is equivalent to minimise $\sum _ { i \in { \mathcal { S } } _ { 0 } } \exp ( z _ { i } )$

Proof. The inequality $u _ { i } \geq \exp ( z _ { i } ^ { \cdot } , \cdot \ )$ equivalent to $u _ { i } - \nu _ { i } = \exp ( z _ { i } )$ and $\nu _ { i } \ge 0$ where $\nu _ { i }$ is a min $\sum _ { i \in S _ { 0 } } u _ { i } = \operatorname* { m i n } \sum _ { i \in S _ { 0 } } \exp ( z _ { i } ) + \nu _ { i }$ . Since a minimisation solution must have $\nu _ { i } ^ { * } = f , \ldots \cdot \mathrm { e }$ have $u _ { i } ^ { * } = \exp ( z _ { i } ^ { * } )$ . Finally, since for all $i \in S _ { 0 } , \ u _ { i } \geq \exp ( z _ { i } )$ , we have min $\sum _ { i \in S _ { 0 } } u _ { i } = \operatorname* { m i n } _ { \angle _ { \bullet i \in S _ { 0 } } } \exp ( z _ { i } )$

Example: Let’s consider again the example in Figure 2. Suppose that the inference module estimates the attacker may be in node 1 or node 2. The updated belief vector is $B ( X _ { t } ) = ( 0 . 1 , 0 . 7 , 0 . 2 , 0 , . . . , 0 )$ . In the initial investment, the preventive security portfolio is $[ c _ { 2 }$ $c _ { 3 } \ ]$ with security risk of 0.2 and the remaining budgets 5. Now, available controls are $\mathcal { C } _ { c } = \{ c _ { 5 } , c _ { 6 } , c _ { 7 } , c _ { 8 } , c _ { 9 } , c _ { 1 0 } \}$ . Given the previously implemented security portfolio, the base-line effectiveness is:

$$
\begin{array}{l} \pi_ {0 \to 2} (x) = 0. 2, \pi_ {0 \to 3} (x) = 0. 2, \pi_ {0 \to 4} (x) = 0. 1, \\ \pi_ {1 \to 2} (x) = 0. 1, \pi_ {1 \to 4} (x) = 0. 2. \end{array}
$$

The base-line effectiveness of other edges remains unchanged (i.e. $\pi _ { e } ( x ) = 1 )$ . Since we cannot precisely determine the optimal value of ${ \mathrm { d i } } \ttSigma _ { t }$ and ind , we solve the solution of Pareto front that produces the best return over investment. The Pareto-front solution is

Table 2: Pareto front of the toy example at time t .

<table><tr><td> $(dir_t, ind_t)$ </td><td>controls</td><td>budget used</td><td>expected security risk</td><td>security risk  $(r_0, r_1, r_2)$ </td></tr><tr><td>(1/5,1/5)</td><td> $[c_8]$ </td><td>1</td><td>0.290</td><td>(0.2,0.1,1)</td></tr><tr><td>(2/5,2/5)</td><td> $[c_8, c_9]$ </td><td>2</td><td>0.107</td><td>(0.072,0.040,0.360)</td></tr><tr><td>(3/5,3/5)</td><td> $[c_6, c_8, c_9]$ </td><td>3</td><td>0.063</td><td>(0.026,0.024,0.216)</td></tr><tr><td>(4/5,4/5)</td><td> $[c_6, c_7, c_8, c_9]$ </td><td>4</td><td>0.061</td><td>(0.026,0.022,0.216)</td></tr><tr><td>(1,1)</td><td> $[c_6, c_7, c_8, c_9]$ </td><td>4</td><td>0.061</td><td>(0.026,0.022,0.216)</td></tr></table>

The most profitable $( \mathrm { d i r } _ { t } , \mathrm { i n d } _ { t } ) \ \mathrm { a r e } ( \cdot ^ { \prime } 5 , 2 / 5 )$ and (3 / 5,3 / 5) with optimal security portfolio $\left[ c _ { 8 } , \ c _ { 9 } \right]$ and $[ c _ { 6 } , \ c _ { 8 } , \ c _ { 9 } ]$ , respectively. Both of them have a significant reduction in the security risk. The portfolio $\left[ c _ { 8 } , c _ { 9 } \right]$ is recommended to the defender who wants to save budgets for future defence; whereas $[ c _ { 6 } , c _ { 8 } , c _ { 5 } ] \vdots$ for the defender who prefer focusing on the current defence.

## 4.2. Justifying the online defence

In the example in Figure 2, notice that the graphs starting from node 1 and node 2 are both sub-graphs of the graph starting from node 0. One may ask why we do not consider the optimisation of a whole graph starting from node 0 since both sub-graphs are included in the whole graph?

If we start from node 0, the problem reduces to find the security portfolio minimising the attacker’s probability of success through the most critical path from the source to the target. Thus, we may leave other critical paths (those not starting from the source) with less protection. Hence we would consider probabilities that are wrong, given the current beliefs. In extreme cases, there would be paths that, given current beliefs, should be impossible, yet would be considered very

likely.

Example: To illustrate this point, consider the example in Figure 4. Suppose each control costs one in direct and indirect costs, and the total budgets are three each. Assume the base-line probability of every edge to be one and the effectiveness of controls as follows:

$$
c _ {1} = 0. 2, c _ {2} = 0. 1, c _ {3} = 0. 1, c _ {4} = 0. 3, c _ {5} = 0. 5, c _ {6} = 0. 5.
$$

## Figure 4: A small toy example

There are four paths from the source (node 0) to the target (node 3). Let’s consider the belief vector $B ( X _ { t } ) = ( b _ { 0 } , . . . , b _ { 3 } ) = ( 0 . 1 , 0 . 7 , 0 . 2 , 0 )$ . With $\mathbf { t h e } \cdot \sin \theta ,$ belief, every edge has a different weight. For example, in the case of no security $\mathrm { c c } \mathrm { n t r } \mathrm { \dot { c } , \dot { \Omega } }$ the attacker may select any path starting from the node where he is with an equal probability . The probability that the attacker may exploit edge 0 to 3 is $0 . 0 3 3 { = } 1 / 3 { \times } 0 . 1$ ; whereas edge 1 to 3 has a probability of $0 . 3 5 0 { = } 1 / 2 { \times } 0 . 7$ to be exploited by the attacker, which is ten times h $\bullet \mathbf { { o } } ^ { \mathbf { { k } } }$ er than edge 0 to 3. To reduce the security risk, we should consider those edges that $\smash { \mathbf { \phi } _ { \mathbf { \phi } } \mathbf { \Lambda } _ { \mathbf { \Lambda } } } \mathcal { S } \textbf { \Lambda } _ { \mathbf { \Lambda } } \mathrm { ~ m ~ }$ ore likely to be exploited.

If we consider the optimisation on the whole graph starting from node 0 the problem is similar to that in [1], with optimal port $\hat { \mathbf { \Omega } } ^ { \prime } \circ \bar { \mathbf { \Omega } } ^ { } [ c _ { 1 } ^ { \phantom { } } , \ c _ { 2 } ^ { \phantom { } } , \ c _ { 6 } ^ { \phantom { } } ]$ . The edges from node 0 to node 1, 2, 3 are well protected by the security $\mathbf { p o } \mathbf { \mathrm { 1 } 4 U c } ^ { \dagger } \mathbf { \dot { \mathbf { \xi } } } \mathbf { O }$ whereas edge 1 to 2, edge 1 to 3 and edge 2 to 3 are counter-measures. As a result, the expected security risk is $0 . 9 5 = 0 . 1 { \times } 0 . 5 + 0 . 7 { \times } 1 + 0 . 2 \ { \cdot } 1$ However, if we select the security portfolio using the belief vector (i.e. $\sum _ { i } b _ { i } r _ { i } )$ expected risk reduce to $0 . 4 6 = 0 . 1 { \times } 0 . 5 + 0 . 7 { \times } 0 . 5 + 0 . 2 { \times } 0 . 3$ with an optimal security portfolio $\{ c _ { 4 } , \ c _ { 5 } , \ c _ { 6 } \}$ . The protected edges are those more likely to be exploited by the attacker in the next step.

## 4.3. The online defence as a Bayesian Stackelberg game

The online defence problem closely relates to a special class of games: Bayesian Stackelberg games [12, 13]. In such games, the type k follower has an appearance probability of $b ^ { k }$ Similarly, in the online defence, the defender has a belief vector representing a probability distribution over the nodes where the attacker could be, i.e. a probability distribution over attacker’s types. The Harsanyi transformation [12], which converts a Bayesian Stackelberg game into a normal-form game, is the classical technique to find optimal strategies.

Optimality study on the online defence: The online defence optimisation problem presented in (13) can be reformulated as a game matrix with payoff matrices $R ^ { k } = \{ R _ { i j } ^ { k } \}$ for every attacker type:

$$
P ^ {D}: \min _ {\delta} \max _ {\alpha} \sum_ {k \in \mathcal {K}} b ^ {k} \sum_ {i \in \mathcal {D}, j \in \mathcal {A} ^ {k}} R _ {i j} ^ {k} \delta_ {i} \alpha_ {j} ^ {k},\tag{25}
$$

$$
\text { s.t.: } \delta_ {i} \in \{0, 1 \}, \forall i \in \mathcal {D}; \quad \sum_ {i \in \mathcal {D}} \delta_ {i} = 1;\tag{26}
$$

$$
\left(\alpha_ {j} ^ {k} \in \{0, 1 \}, \forall j \in \mathcal {A} ^ {k}; \quad \sum_ {i \in \mathcal {A} ^ {k}} \alpha_ {j} ^ {k} = 1, k \in \mathcal {K}. \right.\tag{27}
$$

where denotes the set of all feasible security portfolios subject to the budget constraints, and $\mathcal { A } ^ { k }$ denotes the set of feasible paths from the node here the k -th attacker is believed to be to the target. If the binary indicator $\delta _ { i } = 1$ , then se portfolio selected; otherwise, $\delta _ { i } = 0$ Moreover, the defender can only select one portfolio. Similarly, the attacker of type k selects the path j from the set $\mathcal { A } ^ { k }$ if $\alpha _ { j } ^ { k } = 1$ ; otherwis $\mathbf { \boldsymbol { \cdot } } ^ { k } = 0$ . Also, one type of attacker can only select one path. The payoff $R _ { i j } ^ { k }$ represents the security risk when the defender selects portfolio i and the type k attacker selects path $R ^ { k }$ will increase exponentially with respect to the number of controls and edges. Although it is not practical to form such large payoff matrices in real applications, we can theoretically investigate optimality for the online defence problem represented in this equivalent matrix game setting.

To solve a Bayesian Stackelberg game, the Harsanyi transformation determines the attacker’s type according to a given belief probability $b ^ { k }$ . For the defender, it is as if there is a single attacker type, whose path set $\overline { { A } }$ contains the cross product of the paths associated with every attacker type. In other words, the “path” ${ \overline { { j } } } \in { \overline { { \mathcal { A } } } }$ in the Harsanyi-transformed game corresponds to a vector $( j ^ { 1 } , . . . , \tilde { j } ^ { | \mathcal { K } | } ) \in \mathcal { A } ^ { 1 } \times . . . \times \mathcal { A } ^ { | \mathcal { K } | }$ in game $P ^ { D }$ . The security risk corresponding to these transformed “paths” is weighted by the appearance probabilities of every attacker type. Thus the normal-form payoff matrix of the Harsanyi-transformed game is constructed as in [12]:

$$
\overline {{{R}}} _ {i \bar {j}} = \sum_ {k \in \mathcal {K}} b ^ {k} R _ {i j} ^ {k}.\tag{28}
$$

Then the Harsanyi-transformed game $P ^ { H }$ can be formulated as:

$$
P ^ {H}: \min _ {\delta} \max _ {a} \sum_ {i \in \mathcal {D}, j \in \overline {{\mathcal {A}}}} \overline {{R}} _ {i j} \delta_ {i} a _ {j},\tag{29}
$$

s.t.:(26),

$$
a _ {j} \in \{0, 1 \}, \forall j \in \overline {{\mathcal {A}}}; \sum_ {i \in \overline {{\mathcal {A}}}} a _ {j} = 1.\tag{30}
$$

Here the attacker will select only one feasible “path” to maximize the weighted security risk after the defender’s decision.

Proposition 2. The online defence optimisation problem (13) has the same optimal security portfolio as the Harsanyi-transformed game $P ^ { H }$ with a normal-form payoff matrix in (28).

Proof. Since Problem $P ^ { D }$ is equivalent to the optimisation (13), $\mathbf { w } _ { \mathbf { \lambda } }$ only have to prove Problem $P ^ { D }$ has the same optimal solution as the game $P ^ { H }$

The defender is the leader who moves first. Suppose the defender selects the security portfolio i (i.e. $\delta _ { i } = 1$ and $\delta _ { n } = 0$ for all $n \neq i )$ ; the optimal action of the attacker is to find the most critical path <sup>\*</sup>j (i.e. $a _ { _ j ^ { * } } = 1$ and $a _ { j } = 0$ for ${ \bf { a } } { \bf { l } } ^ { \prime } { \bf { \Delta } } j \neq j ^ { * } { \bf { \Delta } } .$ ) resulting in the highest security risk $\overline { { R } } _ { i j } { } ^ { * }$ . Thus, the min-max game $P ^ { H }$ can be reduced to a single-level problem with an auxiliary constraint:

$$
\overline {{P}} ^ {F} \cdot \min _ {a, a, \lambda} \sum_ {i \in \mathcal {D}, j \in \overline {{\mathcal {A}}}} \overline {{R}} _ {i j} \delta_ {i} a _ {j},\tag{31}
$$

$$
\mathrm{s.t.}: (2 6), (2 6 3 0),
$$

$$
0 \leq \lambda - \sum_ {i \in \mathcal {D}} \overline {{R}} _ {i j} \delta_ {i} \leq M (1 - a _ {j}), \forall j \in \overline {{\mathcal {A}}}.\tag{32}
$$

where M is a large constant. For the security portfolio i , the auxiliary constraint becomes:

$$
0 \leq \lambda - \overline {{R}} _ {i j} \leq M (1 - a _ {j}), \forall j \in \overline {{\mathcal {A}}}.\tag{33}
$$

The leftmost inequality enforces that the variable is greater than or equal to the highest security risk, i.e. $\lambda \geq \overline { { R } } _ { i j } { ^ { * } }$ . The rightmost inequality enforces $\lambda \leq \overline { { R } } _ { i j } { ^ { * } }$ for the most critical path (i.e. $a _ { j } ^ { * } = 1 )$ , and $\lambda - \overline { { R } } _ { i j } \leq M$ for all other paths (i.e. $a _ { j } = 0$ for all $j \neq j ^ { * } )$ . In other words, the auxiliary constraint (32) enforces the attacker to select the most critical path given a security portfolio.

Next, we prove the proposition by contradiction. Suppose portfolio i is an optimal solution for the problem $P ^ { D }$ , whereas there exits another portfolio $i ^ { * } \neq i$ that is an optimal solution for the Harsanyi-transformed game $P ^ { H }$ . Thus, for the reduced game $\overline { { P } } ^ { H }$ , there must exist two real variables (we omit the corresponding constraints here):

$$
\lambda^ {i} = \max _ {a} \sum_ {j \in \mathcal {A}} \overline {{R}} _ {i j} a _ {j}, \text {   and   } \lambda^ {i ^ {*}} = \max _ {a} \sum_ {j \in \mathcal {A}} \overline {{R}} _ {i ^ {*} j} a _ {j},\tag{34}
$$

such that $\lambda ^ { i } > \lambda ^ { i ^ { * } }$ . Recall the normal-form matrix is constructed from the individual payoff matrices of each attacker type, i.e. $\begin{array} { r } { \overline { { \boldsymbol { R } } } _ { i \overline { { \boldsymbol { j } } } } = \sum _ { k \in \mathcal { K } } b ^ { k } \boldsymbol { R } _ { i j } ^ { k } } \end{array}$ , and every $a _ { j }$ corresponds to a particular cross product of paths of every attacker type. Thus, these two variables can be reformulated as Problem $P ^ { D }$ :

$$
\lambda^ {i} = \max _ {\alpha} \sum_ {k \in \mathcal {K}} b ^ {k} \sum_ {j \in \mathcal {A} ^ {k}} R _ {i j} ^ {k} \alpha_ {j}; \text { and } \lambda^ {i *} = \max _ {\alpha} \sum_ {k \in \mathcal {K}} b ^ {k} \sum_ {j \in \mathcal {A} ^ {k}} K _ {i j} ^ {k} \alpha_ {j}.\tag{35}
$$

Given i is the optimal security portfolio for problem $P _ { \mathrm { ~ \bf ~ \Lambda ~ } } ^ { D } \mathbf { \Lambda } _ { \bf { w } }$ e have $\lambda ^ { i } < \lambda ^ { i ^ { * } }$ which contradicts to $\lambda ^ { i } > \lambda ^ { i ^ { * } }$ . Thus, we must have $i = i ^ { * }$ , i.e. i is also $\therefore e$ optimal security portfolio for the Harsanyi-transformed game $P ^ { H }$ 

Example Let’s illustrate Proposition 2 with the example in Figure 4. Assume the belief vector $B ( X _ { t } ) = ( 0 , 0 . 6 , 0 . 4 , 0 )$ There are two types of attacker who could either be in node 1 or node 2. The type 1 attacker ha the target: $\omega _ { 1 } ^ { k = 1 } \colon 1  3$ and $\omega _ { 2 } ^ { k = 1 } \colon 1  2  3 .$ The type 2 attacker has only one path: ${ \mathcal { D } } _ { 1 } ^ { \cdot = 2 } \colon 2  3$ . Then we can construct a normal-form payoff matrix corresponding to th e probabiliti s of appearances of types for the Harsanyi-transformed game in Table 3.

Table 3: The payoff matrix

<table><tr><td>Portfolio</td><td> $(\omega_{1}^{k=1} \times \omega_{1}^{k=2})$ </td><td> $(\omega_{2}^{k=1} \times \omega_{1}^{k=2})$ </td><td>Portfolio</td><td> $(\omega_{1}^{k=1} \times \omega_{1}^{k=2})$ </td><td> $(\omega_{2}^{k=1} \times \omega_{1}^{k=2})$ </td></tr><tr><td> $[c_{1},c_{2},c_{3}]$ </td><td>1</td><td>0.46</td><td> $[c_{2},c_{3},c_{4}]$ </td><td>0.72</td><td>0.1254</td></tr><tr><td> $[c_{1},c_{2},c_{4}]$ </td><td>0.72</td><td>0.174</td><td> $[c_{2},c_{3},c_{5}]$ </td><td>0.70</td><td>0.46</td></tr><tr><td> $[c_{1},c_{2},c_{5}]$ </td><td>0.70</td><td>1</td><td> $[c_{2},c_{3},c_{6}]$ </td><td>1</td><td>0.46</td></tr><tr><td> $[c_{1},c_{2},c_{6}]$ </td><td>1</td><td>1</td><td> $[c_{2},c_{4},c_{5}]$ </td><td>0.42</td><td>0.174</td></tr><tr><td> $[c_{1},c_{3},c_{4}]$ </td><td>0.72</td><td>0.1254</td><td> $[c_{2},c_{4},c_{6}]$ </td><td>0.72</td><td>0.174</td></tr><tr><td> $[c_1,c_3,c_5]$ </td><td>0.70</td><td>0.46</td><td> $[c_2,c_5,c_6]$ </td><td>0.70</td><td>1</td></tr><tr><td> $[c_1,c_3,c_6]$ </td><td>1</td><td>0.46</td><td> $[c_3,c_4,c_5]$ </td><td>0.42</td><td>0.1254</td></tr><tr><td> $[c_1,c_4,c_5]$ </td><td>0.42</td><td>0.174</td><td> $[c_3,c_4,c_6]$ </td><td>0.72</td><td>0.1254</td></tr><tr><td> $[c_1,c_4,c_6]$ </td><td>0.72</td><td>0.174</td><td> $[c_3,c_5,c_6]$ </td><td>0.70</td><td>0.46</td></tr><tr><td> $[c_1,c_5,c_6]$ </td><td>0.70</td><td>1</td><td> $[c_4,c_5,c_6]$ </td><td>0.42</td><td>0.174</td></tr></table>

As the table would be too long to be presented if we consider all possible security portfolios for the toy example, here we consider a simplified scenario where every portfolio has exact three controls, i.e. the defender has to spend all direct and indirect budgets. Although it is unwise for the defender to exhaust all budgets in real applications, our purpose is to show (13) and $P ^ { H }$ have the same optimal portfolio. From Table 3, the $\mathrm { c e } \mathrm { \hookrightarrow } \mathrm { e }$ four optimal security portfolios for $P ^ { H } : [ c _ { 1 } , \ c _ { 4 } , \ c _ { 5 } ] , [ c _ { 2 } , \ c _ { 4 } , \ c _ { 5 } ] , [ c _ { 3 } , \ c _ { 4 } , \ c _ { 5 } ]$ , and $[ c _ { \scriptscriptstyle 4 } , c _ { \scriptscriptstyle 5 } , \dot { \mathbf { \xi } } _ { \scriptscriptstyle 5 } ]$ with the same security risk of 0.42 defender’s selection. Solving the online defence problem as a MICP, we obtain the optimal portfolio $[ c _ { 4 } , \ c _ { 5 } , \ c _ { 6 } ]$ which is the optimal solution for the Harsanyi-transformed game.

## 5. Evaluation

In this section, we first show that our approach for Bayesian Stackelberg games over attack graphs is very efficient. Our optimisation needs fewer optimisation variables, compared to DOBSS and the Harsanyi transformation. Then we provide numerical evaluations to illustrate that the online defence is efficient for realistic scenarios. Finally, we analyse an attack scenario using the decision support system to find optimal security portfolios.

## 5.1. Optimisation variables for complete attack graphs

For a complete direct graph with N nodes, the number of edges is $N ( N { - } 1 ) / 2$ , and the number of paths is $2 ^ { N - 2 }$ . Suppose we have A attacker types, and each of them corresponds to a complete directed sub-graph with $n _ { i }$ nodes, where $i = 1 , . . . , A$ . Let C be the number of controls for the defender, and each control has $l _ { j }$ levels for $j = 1 , . . . , C$ . Table 4 shows the number of optimisation variables needed for the security portfolios and the attacker’s actions, respectively: notice that the number of decision variables for the online defence increases linearly with respect to the number of controls and nodes, whereas DOBSS <sup>1</sup> and the Harsanyi Transformation have an exponential increase rate. For an attack graph with 50 nodes, 25 attacker types, 20 controls with 2 levels each, the online defence needs $2 0 \times 2 = 4 0$ defender’s variables, up to $5 0 \times 2 5 = 1 2 5 0$ attacker’s variables and 75 auxiliary variables. However, DOBSS needs up to $3 ^ { 2 0 }$ defender’s variables (if budgets are large), up to $2 ^ { 4 8 } \times 2 5 = 7 \times 1 0 ^ { 1 5 }$ attacker’s variables and $2 . 4 \times 1 0 ^ { 2 5 }$ auxiliary variables. No solver can neither efficiently generate such large matrices nor handle this number of variables, e.g. not enough memory. This is also the case for HBGS and HUNTER when dealing with an attack graph consisting of $2 . 8 \times 1 0 ^ { 1 4 }$

Table 4: number of optimisation variables

<table><tr><td>Opt. Variables</td><td>online defence</td><td>DOBSS</td><td>Warsanyi Trans.</td></tr><tr><td>Defender&#x27;s</td><td> $d_{O}=\sum_{j=1}^{C}l_{j}$ </td><td> $d_{D}=\prod_{j=1}^{C}(l_{j}-1)$ </td><td> $d_{H}=\prod_{j=1}^{C}(l_{j}+1)$ </td></tr><tr><td>Attacker&#x27;s</td><td> $a_{O}=\sum_{i=1}^{A}n_{i}$ </td><td> $a_{D}=\sum_{i=1}^{n-2}2^{n-2}$ </td><td> $a_{H}=2\sum_{i=1}^{A}n_{i}^{-2A}$ </td></tr><tr><td>Auxiliary</td><td>3A</td><td> $d_{D}\times a_{O}+A$ </td><td>N/A</td></tr><tr><td>Total Used</td><td> $3A+d_{O}+a_{O}$ </td><td> $d_{D}\times a_{D}+a_{D}+A$ </td><td> $d_{H}+a_{H}$ </td></tr></table>

## 5.2. Optimisation over complete attack graphs

Complete directed graphs are generated over an increasing number of N nodes, and 20 controls with two levels each. For each control, random effectiveness and random direct and indirect costs are generated. For each edge, the number of controls is a random number between 1 and 4. We consider two attackers’ types who could be in node 0 or node N / 2 , with a random belief. All computations were performed on a PC with a 2.8 gigahertz Intel Core i7 and 16 gigabytes RAM. The optimisation was programmed in Python using the MOSEK version 9.2 solver. The results are shown in Figure 5. For the complete graph with 200 nodes, it has 19,900 edges and $4 \times 1 0 ^ { 5 9 }$ paths. Our optimisation can find the optimal solution within an average of 1440 seconds.

Figure 5: Results for complete graphs. For each number of nodes, ten runs have been conducted to generate the boxplot.

Next, let us consider a complete attack graph with 50 nodes (1225 edges and $2 . 8 \times 1 0 ^ { 1 4 }$ paths), whereas the number of attacker types ranges from 10 to 50. The results are shown in Figure 6. Finally, we compare the computation time between the online defence, DOBSS, HBGS and HUNTER in Table 5. In the cyber-security domain, a multi-step cyber-security game may contain a large number of paths and actions to be selected. Since DOBSS, HBGS and HUNTER are developed for single-step matrix games, they can be inefficient for such security games with a huge action space. However, our optimisation can efficiently produce the optimal solution: in particular, it can find the optimal solution over a complete attack graph with N = 50 ( N = 70 resp.) for the defender facing 50 attacker types within an average of 179 seconds (709.4 seconds resp.). Note the computation time only increases by 4 times, while the number of paths increases by $1 0 ^ { 6 }$ times.

Figure 6: Results for a complete graph with 50 nodes. For each number of nodes, ten runs have been conducted. CO  
Table 5: Computation Time

<table><tr><td>Algorithms</td><td>Types</td><td>Actions (Paths)</td><td>Avg. Time (secs)</td></tr><tr><td>Online Defence ( $N = 50$ )</td><td>50</td><td> $2.81 \times 10^{14}$ </td><td>179.3</td></tr><tr><td>Online Defence ( $N = 70$ )</td><td>50</td><td> $2.95 \times 10^{20}$ </td><td>709.4</td></tr><tr><td>DOBSS [14]</td><td>6</td><td>30</td><td>12593.8</td></tr><tr><td>HBGS [14]</td><td>50</td><td>30</td><td>3321.7</td></tr><tr><td>HUNTER [15]</td><td>10</td><td>13</td><td>108.3</td></tr><tr><td>HUNTER-BFS [15]</td><td>200</td><td>5</td><td>1143.5</td></tr></table>

## 5.3. Case study: a network attack graph

To demonstrate our decision support system in a realistic scenario, we consider a university campus with two departments having a similar network structure. This scenario is based on [34] (see Example 3). We follow [1] to present the attack scenario as a probabilistic attack graph. In addition, we extend the case study by adding more possible controls based on the MITRE ATT&CK enterprise matrices [35].

The main steps and states of the attack scenarios are depicted in Figure 7.

Figure 7: The attack graph of the case study.

Node 0 is the source where the attacker initially located (i.e. the state prior to the attack), node $T _ { \scriptscriptstyle 0 }$ is the target node where the attacker has successfully exploited the database in either Department 1 or Department 2. Node 1 is a gateway that connects the two departments. For the department networks, we have left the same numbering for nodes as in [34]. For example, node 18-1 in Department 1 and node 18-2 in Department 2 represent the same node 18 in Example 3 [34]. In Department 1, node 10-1 is the state where a malicious input has been accessed by an employee browsing either a malicious or a compromised website (two edges leading to node 10-1). Node 18-1 represents the state where the attacker has gained net access to the webserver via http protocol. In node 22-1, the attacker can execute code on the webserver running apache. An example vulnerability is CVE-2006-3747 in Rewrite module in apache. In node 14-1, the attacker can execute code on a workstation. An example vulnerability is CVE-2009-1918 in Microsoft IE. Node 26-1 represents access to the database server via dbprotocol. Node 30-1 is the target where the attacker executes code on the database server as root. An example vulnerability on the database server is CVE-2009-2446 in dispatch\_command function in MySQL. Since Department 2 has the same network structure, we do not repeat the nodes in Department 2 again. Compared to Department 1, the workstations, the webserver, and the database server in Department 2 may suffer from similar vulnerabilities, for example, CVE-2016-7283 in the workstation, which allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption) via a crafted website; CVE-2005-1344 in the webserver, which allows attackers to execute arbitrary code via a long realm argument; and CVE-2009-4484 in the database, which allows remote attackers to execute arbitrary code or cause a denial of service. In the network, each edge represents a possible attack step. The authors in [34] have estimated the base-line success probability $\pi _ { e }$ of attack steps via various sources. The base-line probabilities are shown on edges, and edges without a number have $\pi _ { e } = 1$ . Our purpose here is to show how our decision support system works. The precise vulnerabilities on the organisation and the base-line success probabilities should be decided on specific instances of this scenario.

The university has a firewall control N0. The two departments have similar controls: for example, ScW-1 represents a patch for the workstation vulnerabilities in Department 1, while $\mathsf { S C W } - 2$ is a patch for the workstation vulnerabilities in Department 2.

In the following the index of controls is omitted for the sake of simplicity. Controls ${ \mathrm { S C S } } ,$ and $\mathtt { S C D b }$ are the patches for the webserver and the database server vulnerabilities, respectively. N1 and N2 are external and internal firewalls for the departments. User education Ed has two levels: Level 1 is basic training to identify social engineering techniques and phishing emails, and Level 2 is a more advanced training. AnW, AnS, and $\mathtt { A n o }$ are antivirus software for the workstation, the webserver, and the database server respectively. ReW restricts web-based content, and $\mathrm { N e t } \mathrm { \bar { \Sigma } }$ scans and removes malicious email attachments or links for the workstation. ApS is application isolation and sandboxing for the webserve $\tt A p \bar { \sf W }$ is application micro-segmentation to mitigate the impact of client-side exploitation for the workstation. EpW is exploit protection – security applications to mitigate some exploitation behaviour. Controls $\mathtt { D r S }$ and DrD disable or remove unnecessary or unused shells $\mathbf { \rho } _ { \mathbf { C } , i }$ r interpreters for the webserver and the database server. Controls MaS and mise available services to only those that are necessary for the webserver and the Code signing controls for the webserver (CsS) and the database server (CsD) only permi execution of signed scripts where possible. $\mathbf { \mathbb { E } } \mathbf { \times } \mathbf { \in } \mathbf { S }$ and $\operatorname { E x e D }$ enable application controls where appropriate for the webserver and the database server.

User education $\varsigma ^ { \star }$ ntrol (Ed), patching controls $( \mathsf { S c W } , \mathsf { S c S }$ , and $\mathtt { S C D } )$ , firewalls (N1 and N2), and antivirus (AnW, AnS, and AnD) are only preventive. Other controls are both preventive and corrective. We estimate the effectiveness of controls into three levels: Very High $( \mathrm { V } ) =$ 0.0001, High (H) = 0.2, and Medium $( \mathbf { M } ) = 0 . 6$ . The costs and effectiveness of controls are shown in Table 6. The possible controls are based on the MITRE ATT&CK enterprise matrices [35], but practitioners can determine more precise controls and values based on a specific instance of this scenario.

Table 6: Values for controls in the case study.

<table><tr><td>Controls</td><td>ScW</td><td>ScS</td><td>ScD</td><td>N1</td><td>N2</td><td>Ed-L1</td><td>Ed-L2</td><td>AnW</td><td>AnS</td></tr><tr><td>Cost</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Indirect Cost</td><td>3</td><td>5</td><td>10</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Effectiveness</td><td>V</td><td>V</td><td>V</td><td>H</td><td>M</td><td>M</td><td>H</td><td>H</td><td>H</td></tr><tr><td>Controls</td><td>AnD</td><td>NetW</td><td>ReW</td><td>ApS</td><td>ApW</td><td>EpW</td><td>DrS</td><td>MaS</td><td>DrD</td></tr><tr><td>Cost</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Indirect Cost</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>2</td><td>2</td><td>3</td></tr><tr><td>Effectiveness</td><td>H</td><td>M</td><td>M</td><td>M</td><td>M</td><td>M</td><td>H</td><td>H</td><td>H</td></tr><tr><td>Controls</td><td>MaD</td><td>CsS</td><td>CsD</td><td>ExeS</td><td>ExeD</td><td>NO</td><td></td><td></td><td></td></tr><tr><td>Cost</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Indirect Cost</td><td>3</td><td>2</td><td>3</td><td>1</td><td>3</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Effectiveness</td><td>H</td><td>M</td><td>M</td><td>H</td><td>H</td><td>M</td><td></td><td></td><td></td></tr></table>

Initial investment: Suppose the direct and indirect budgets are 20, i.e. $B _ { D } = 2 0$ and $B _ { I } = 2 0$ . We examine the solutions of the $p _ { D }$ and $p _ { I }$ in the range of 0 and 1. The defender selects the most profitable initial investment via the solutions of the Pareto front. In this case, we select $( p _ { D } , p _ { I } ) = ( 1 0 / 7 , 0 \textsuperscript { 1 7 / 2 0 } )$ with an optimal preventive security portfolio [ ScW-1, AnD-1, E -2, , AnS-2] resulting in a security risk of 0.00480 . Patching the vulnerabilities are the most ffective controls. Due to a high indirect cost, the optimal preventive solution select $\therefore 1 y = \Delta W - 1$ and ScW-2 to patch the workstations in Department 1 and 2. Antivirus Controls AnD-1 and AnD-2 are applied for the database servers in Department 1 and 2. Application control ExeS-1 is applied for the webserver in Department 1, and antivirus control is applied for the webserver in Department 2. The remaining direct and indirect budgets for the online defence are 10 and 10.

Online Defence: We consider an ongoing attack scenario where the attacker may have access to the webserver and even execute code on the webserver in Department 1: suppose the inference module returns the belief vector $b _ { 1 8 - 1 } = 0 . 7$ and $b _ { 2 2 - 1 } = 0 . 3$ . We run the solutions of the Pareto front to find the optimal corrective security portfolio: [EpW-1, DrD-1, ExeD-1] (budget used = (5, 7)) with the expected security risk of $0 . 0 0 1 5 7 = 0 . 0 0 0 1 9 2 \times 0 . 7 + 0 . 0 0 4 8 0 \times 0 . 3$ . Since the attacker is in Department 1, no Department 2 control is selected in the Pareto front solutions.

Next we compare the online optimisation solution to the solution in [1]. First, we run the solution with the same budget (5, 7). The selected corrective portfolio is [ApS-1, DrS-1, DrS-2, ExeS-2] (budget used is (5,7)). Although attacker has accessed to Department 1, the solution select controls DrS-2, ExeS-2 in Department 2 that cannot mitigate the ongoing attack. Moreover, the solution has an expected security risk of $0 . 0 3 6 7 = 0 . 0 0 0 9 6 0 \times 0 . 7 + 0 . 1 2 \times 0 . 3$ which is about 23 times higher than the optimal online optimisation solution.

One may argue that we could isolate the Department 2 network when finding the corrective security portfolio to mitigate the ongoing attack in Department 1. Run the solution in [1] with the same budget (5, 7). The selected corrective portfolio is [ApS-1, DrS-1, ExeD-1] (budget used is (4,7)), resulting an expected security risk of $0 . 0 0 7 3 3 = { \cap } { _ { \bigcup } } 2 2 \times 0 . 7 + 0 . 0 2 4 0 \times 0 . 3$ . The

## 6. Conclusion

This work presented an optimal multi-stage cyber-defence mechanism against multi-step attacks. and an online optimization to counteract ongoing attacks. The latter optimization is cast as a Bayesian Stackelberg game in which the defender has incomplete information about the current attacker state. The proposed optimisation is solved by using properties of totally unimodular matrices, strong duality, and MICP (MILP (Mixed-Integer linear programming), respectively); the solution provides a dramatic computational improvement on previous solutions for these Bayesian Stackelberg games. $\mathrm { ~ \ r ~ { ~ T ~ } ~ } _ { \mathrm { ~ L ~ } } ^ { \mathrm { ~ o ~ } } , \mathrm { ~ \ r ~ { ~ r ~ } ~ \ r ~ { ~ o ~ s ~ e ~ d ~ } ~ }$ solution significantly reduces the security risk for ongoing attacks compared to previous approaches, and provides to cybersecurity experts a unified mathematical framework both for preventive investment and countermeasures for ongoing attacks.

Real work data validation of the framework is a challenging yet important future step for this research.

## ACKNOWLEDGMENTS

This work was supported by EPSRC [grant numbers EP/R004891/1].

Declarations of interest: none.

Yunxiao Zhang: Conceptualization, Methodology, Investigation, Software, Formal analysis, Writing - Original Draft

Pasquale Malacaria: Conceptualization, Methodology, Investigation, Formal analysis, Writing - Review & Editing, Supervision, Project administration, Funding acquisition

## References

[1] M. Khouzani, Z. Liu, P. Malacaria, Scalable min-max multi-objective cyber-security optimisation over probabilistic attack graphs, European Journal of Operational Research 278 (3) (2019) 894–903.

[2] T. Sawik, Selection of optimal countermeasure portfolio in it security planning, Decision Support Systems 55 (1) (2013) 156–164.

[3] A. Fielder, E. Panaousis, P. Malacaria, C. Hankin, F. Smeraldi, Decision support approaches for cyber security investment, Decision support systems 86 (2016) 13–23.

[4] M. Khouzani, P. Malacaria, C. Hankin, A. Fielder, F. Smeraldi, Efficient numerical frameworks for multi-objective cyber security planning, in: European Symposium on Research in Computer Security, Springer, Springer International Publishing, Cham, 2016, pp. 179–197.

[5] P. Holgado, V. A. Villagrá, L. Vazquez, Real-time multistep attack prediction based on hidden markov models, IEEE Transactions on Dependable and Secure Computing 17 (1) (2020) 134–147.

[6] D. Ourston, S. Matzner, W. Stump, B. Hopkins, Applications of hidden markov models to detecting multi-stage network attacks, in: 36th Annual Hawaii International Conference on System Sciences, 2003. Proceedings of the, IEEE, 2003, pp. 10–pp.

[7] T. Shawly, A. Elghariani, J. Kobes, A. Ghafoor, Architectures for detecting interleaved multi-stage network attacks using hidden markov models, IEEE Transactions on Dependable and Secure Computing (2019).

[8] T. Sommestad, M. Ekstedt, H. Holm, The cyber security modeling language: A tool for assessing the vulnerability of enterprise system architectures, IEEE Systems Journal 7 (3) (2012) 363–373.

[9] N. Poolsappasit, R. Dewri, I. Ray, Dynamic security risk management using bayesian

attack graphs, IEEE Transactions on Dependable and Secure Computing 9 (1) (2011) 61–74.

[10] L. Wang, T. Islam, T. Long, A. Singhal, S. Jajodia, An attack graph-based probabilistic security metric, in: IFIP Annual Conference on Data and Applications Security and Privacy, Springer, Springer Berlin Heidelberg, Berlin, Heidelberg, 2008, pp. 283–296.

[11] H. M. Almohri, L. T. Watson, D. Yao, X. Ou, Security optimization of dynamic networks with probabilistic graph modeling and linear programming, IEEE Transactions on Dependable and Secure Computing 13 (4) (2015) 474–487.

[12] J. C. Harsanyi, R. Selten, A generalized nash solution for two-person bargaining games with incomplete information, Management science 18 (5-part-2) (1972) 80–106.

[13] P. Paruchuri, J. P. Pearce, J. Marecki, M. Tambe, F. Ordonez, S. Kraus, Playing games for security: An efficient exact algorithm for solving bayesian stackelberg games, in: Proceedings of the 7th International Joint Conference on Autonomous Agents and Multiagent Systems - Volume 2, AAMAS ’08, International Foundation for Autonomous Agents and Multiagent Systems, Richland, SC, 2008, pp. 895–902.

[14] M. Jain, C. Kiekintveld, M. Tambe, Quality-bounded solutions for finite bayesian stackelberg games: Scaling up, in: The 10th International Conference on Autonomous Agents and Multiagent Systems - Volume 3, AAMAS ’11, International Foundation for Autonomous Agents and Multiagent Systems, Richland, SC, 2011, p. 997–1004.

[15] Z. Yin, M. Tambe, A unified method for handling discrete and continuous uncertainty in bayesian stackelberg games, in: Proceedings of the 11th International Conference on Autonomous Agents and Multiagent Systems - Volume 2, AAMAS ’12, International Foundation for Autonomous Agents and Multiagent Systems, Richland, SC, 2012, p. 855–862.

[16] D. A. Morán R, S. S. Dey, J. P. Vielma, A strong dual for conic mixed-integer programs, SIAM Journal on Optimization 22 (3) (2012) 1136–1150.

[17] M. Lubin, Mixed-integer convex optimization: outer approximation algorithms and modeling power, Ph.D. thesis, Massachusetts Institute of Technology (2017).

[18] D. Korzhyk, Z. Yin, C. Kiekintveld, V. Conitzer, M. Tambe, Stackelberg vs. nash in security games: An extended investigation of interchangeability, equivalence, and uniqueness, Journal of Artificial Intelligence Research 41 (2) (2011) 297–327.

[19] B. Stefan, CYBERSECURITY INVESTMENTS: Decision Support Under Economic Aspects, Springer International Publishing, 2018.

[20] C. Schiller, J. R. Binkley, Botnets: The killer web applications, Elsevier, 2011.

[21] V. Viduto, C. Maple, W. Huang, D. LóPez-PeréZ, A novel risk assessment and optimisation model for a multi-objective network security countermeasure selection problem, Decision Support Systems 53 (3) (2012) 599–610.

[22] S. Mukdasanit, S. Kantabutra, Attack and defense in the layered cyber-security model and their (1 )  -approximation schemes, Journal of Computer and System Sciences 115 (2021) 54–63.

[23] C. Casorrán, B. Fortz, M. Labbé, F. Ordóñez, A study of general and security stackelberg

applications in stackelberg security games, Handbook of Dynamic Game Theory (2018) 1223–1269.

beyond a decade of success, in: Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence, IJCAI-18, International Joint Conferences on Artificial Intelligence Organization, 2018, pp. 5494–5501.

[26] L. A. Gordon, M. P. Loeb, The economics of information security investment, ACM Transactions on Information and System Security (TISSEC) 5 (4) (2002) 438–457.

[27] T. Sawik, A linear model for optimal cybersecurity investment in industry 4.0 supply chains, International Journal of Production Research (2020) 1–18.

[28] M. Bentley, A. Stephenson, P. Toscas, Z. Zhu, A multivariate model to quantify and mitigate cybersecurity risk, Risks 8 (2) (2020).

[29] Y. Li, L. Xu, Cybersecurity investments in a two-echelon supply chain with third-party risk propagation, International Journal of Production Research (2020) 1–23.

[30] G.-H. Cui, Z. Wang, J.-L. Li, X. Jin, Z.-W. Zhang, Influence of precaution and dynamic post-indemnity based insurance policy on controlling the propagation of epidemic security risks in networks, Applied Mathematics and Computation 392 (2021) 125720.

[31] T. Sawik, Balancing cybersecurity in a supply chain under direct and indirect cyber risks, International Journal of Production Research (2021) 1–17.

[32] A. Ahmadian Ramaki, A. Rasoolzadegan, A. Javan Jafari, A systematic review on intrusion detection based on the hidden markov model, Statistical Analysis and Data Mining: The ASA Data Science Journal 11 (3) (2018) 111–134.

[33] MOSEK ApS, Modeling cookbook 3.2.2 (2020). URL https://docs.mosek.com/modeling-cookbook/expo.html

[34] A. Singhal, X. Ou, Security risk analysis of enterprise networks using probabilistic attack graphs, in: Network Security Metrics, Springer, 2017, pp. 53–73.

[35] The MITRE Corporation, Mitre att&ck matrix for enterprise (2020). URL

## Highlights

 A cyber-security decision support system for an organisation to select an optimal portfolio of security controls to counteract multi-stage cyber-attacks.

The system consists of a preventive optimisation for an initial defensive portfolio, a learning mechanism to estimate possible ongoing attacks, and an online optimisation to counteract ongoing attacks.

The online optimisation is formulated as a Bayesian Stackelberg games, and a proposed solution shows a dramatic computational improvement for the precise solution of such games.

## Biographical Notes:

Yunxiao Zhang received the BEng degree in Electrical and Electronic Engineering from Newcastle University, UK, and the MSc degree in Control Systems and the PhD degree from Imperial College London, UK. Currently, he is a Postdoctoral Research Assistant at the School of Electronic Engineering and Computer Science, Queen Mary University of London, UK, with Professor Pasquale Malacaria. His current research interests lie in cyber-security investment, optimization, game theory.

Pasquale Malacaria received his Laurea in Philosophy from “La Sapienza” University in Rome and his PhD from the University of Paris VII in France. His work focuses on information theory, optimization, game theory, verification and their applications to computer security. He is a Professor of Computer Science at Queen Mary University of London. He has been an EPSRC advanced research fellow, is a recipient of the Alonzo Church award 2017 and the Facebook Faculty awards 2015.

![](/api/attachments/CN9Z46CH/fulltext/images/1ed9a8b69efa601577e9683a18a2201f0ddfef55649cfaf2a02a8a3bf044ab96.jpg)  
Figure 1

![](/api/attachments/CN9Z46CH/fulltext/images/c5872b39189038399d22bcf17b5b729e08da344261f93f72b637b32ed68476cc.jpg)  
Figure 2

![](/api/attachments/CN9Z46CH/fulltext/images/1f1258e4e7e9fb165700816338e43ce77406dec71e9290e7b86d558b489c6335.jpg)  
Figure 3

![](/api/attachments/CN9Z46CH/fulltext/images/f9c7d5cc55fd12d899ddce57adb4b0d93a77ed6bd8af1c270771c137e78870c5.jpg)  
Figure 4

![](/api/attachments/CN9Z46CH/fulltext/images/2a5508bd6dfeec59f331bad6c91f246e0d8cfc61eaed2a9fec49f64fbf1844a8.jpg)  
Figure 5

![](/api/attachments/CN9Z46CH/fulltext/images/301321d21bd9044588163a26c51785437db1562dd8e574f4812a4cab7d8af5d0.jpg)  
Figure 6

![](/api/attachments/CN9Z46CH/fulltext/images/848d587ff6fc6335272ce17a0fcc3c91a16a9efd084e0aa9850bf425cba078a9.jpg)
