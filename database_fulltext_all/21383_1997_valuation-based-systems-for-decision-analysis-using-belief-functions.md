---
otero_id: 21383
otero_key: "D6RQFFXH"
title: "Valuation-based systems for decision analysis using belief functions"
authors: "Hong Xu"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00062-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Valuation-based systems for decision analysis using belief functions

Hong Xu

IRIDIA and Service d'Automatique, Université libre de Bruxelles, 50 Ave. F. Roosevelt, CP194/6, 1050 Brussels, Belgium

## Abstract

Valuation-based systems (VBS) provide a general framework for representing knowledge and drawing inferences under uncertainty. Recent studies have shown that the VBS can also represent and solve Bayesian decision problems. This paper proposes a decision calculus for belief function theory in the VBS. The proposed calculus uses a parameter whose role is the probabilistic interpretation of an assumption that disambiguates decision problems represented with belief functions. We show that the decision problems can be solved by using local computations with the presented calculus if they are represented in the VBS properly. We also show that the presented calculus can be reduced to the one for Bayesian decision problems when probabilities, instead of belief functions, are given. © 1997 Elsevier Science B.V.

Keywords: Decision analysis; Bayesian probability theory; Theory of belief functions; Valuation-based systems; Uncertain reasoning

## 1. Introduction

Decision making under uncertainty is a common problem in the real world. Decision analysis provides a method for decision making. The main objective of this method is to help the decision maker to select an appropriate decision alternative in the face of uncertain environment. Traditional Bayesian decision analysis is based on Bayesian probability theory and on utility theory. The uncertain states of nature are represented by probabilities, and the optimal decision is the one that optimizes its expected utility where the expectation is taken by using the probabilities. Methods for decision analysis based on other uncertain calculi have also been proposed: Jaffray [1], Smets [2], Strat [3] and Yager [4] use belief functions, and Dubois and Prade [5] use possibilities to represent the uncertainty. Some popular frameworks for representing and solving decision problems are decision trees and influence diagrams [6–8].

Recently, a new framework for uncertainty representation and reasoning, called a valuation-based system (VBS), has been proposed by Shenoy [9,10]. In the framework of VBS, knowledge is represented by objects consisting of a set of variables and a set of valuations defined on the subsets of variables, and influence is drawn by using two operators called combination and marginalization. By using these objects and operators, VBS can represent different types of uncertain knowledge in different domains including probability theory, Dempster

Shafer theory and Smets' transferable belief model, both based on belief functions, Zadeh-Dubois-Prade's possibility theory, etc. More recent studies have shown that VBS can also represent and solve Bayesian decision problems [11,12]. In VBS, the graphical representation is called a valuation network, and the method for solving problems is called the fusion algorithm. Initially the VBS was only concerned with uncertainty, and only later did Shenoy show its ability to solve decision problems. Shenoy [13] has also shown that the solution method of VBS for decision problems is more efficient than that of decision trees and of influence diagrams.

Belief functions [14-16] aim to model a decision maker's degree of belief about which state of affairs will prevail. Some methods have been suggested for decision analysis using belief functions when the probabilistic information is incomplete [1,3,4] or irrelevant [2]. In this paper, we propose a method for decision analysis using belief functions in the VBS and an extended framework of VBS adopted for decision analysis. This method, inspired by Strat [3], uses a parameter whose role is similar to the probabilistic interpretation of an assumption that disambiguates decision problems represented with belief functions. We will show that, with the proposed calculus, the fusion algorithm can be used for solving VBS when the problems are represented properly. We will also show that the proposed decision calculus is a kind of generalization for Bayesian decision problems.

The remainder of the paper is as follows. In Section 2, we review the basic concepts of belief functions and discuss the idea of decision analysis using belief functions by a simple example. In Section 3, we present a decision problem needing a belief function representation. In Section 4, we describe the VBS representation for decision problems. In Section 5, we present the decision calculus for belief functions and show how it benefits from the fusion algorithm for solving problems efficiently. Finally, in Section 6, we give our conclusions.

## 2. Decision analysis using belief functions

The classical Bayesian decision model assumes that a decision maker chooses an action (strategy) among a set of relevant actions D (decision variable) in such a way that the expected utility is maximized. Under the environment of uncertainty, the selected action must operate under one of a set of mutually exclusive and exhaustive states of nature. We denote such a set of possible states of nature by a random variable R. Then a utility function $u: D \times R \to \Re$ is specified, where $u(d_i, r_j)$ is the ‘payoff’ of action $d_i$ given state of nature $r_j$ and $\Re$ is the set of real numbers. In the Bayesian framework, the knowledge about R is described by a probability function P on R (or on $D \times R$ ). The expected value of the utility function is used to make decision. Let $E(d_i)$ denote the expected utility of action $d_i$ , computed by:

$$
E (d _ {i}) = \sum_ {r j \in R} P (r _ {j}) u (d _ {i}, r _ {j})
$$

Then, the ‘optimal’ action is the one that maximizes such expected utility. That is, $d^{*}$ is optimal if and only if $E(d^{*}) \geq E(d_{i})$ for all $d_{i} \in D$ . The process for computing $E(d^{*})$ can be seen by first deleting R from function $f(d_{i}, r_{j}) = P(r_{j})u(d_{i})$ by summation and then deleting D by maximization. The deleting sequence in the process is R, D where R is deleted before D. The above is only a canonical decision problem which includes only one decision variable and one random variable. Solving more complex decision problems can also be regarded as a process of deleting variables in sequence by summation or maximization correspondingly.

From the above analysis, we can see that the criteria of maximizing expected value can only be used when the probabilistic information about the states of nature is available. However, in the real world, this is not always the case. New models, such as those based on belief functions, have been proposed to represent quantified beliefs. The theory of belief functions $[14–16]$ allows the expression of all forms of partial beliefs up to total ignorance. It provides a facility to express one's belief only to the degree to which the information is available, and results in a more flexible description of uncertainty that is obtained by the decision maker. In this section, after reviewing the basic concepts of belief functions, we will describe a method for decision making where the uncertainty is represented by belief functions through a simple example.

## 2.1. Belief functions

Definition 1: Let $\Omega$ be a non-empty finite set called the frame of discernment (hereafter referred to as the frame). The mapping $bel\colon 2^{\Omega}\to [0,1]$ is an (unnormalized) belief function if and only if there exists a basic belief assignment (bba) $m\colon 2^{\Omega}\to [0,1]$ such that [16]: 1.

$$
\sum_ {A \subseteq \Omega} m (A) = 1
$$

2.

$$
b e l (A) = \sum_ {B \subseteq A, B \neq \emptyset} m (B)
$$

3.

$$
b e l (\emptyset) = 0
$$

Those subsets $A$ such that $m(A) > 0$ are called focal elements. A belief function is normalized if $m(\emptyset) = 0$ , in which case $bel(\Omega) = 1$ . In this paper, we will use normalized belief functions. A vacuous belief function is a belief function such that $m(\Omega) = 1$ and $m(A) = 0$ for all $A \neq \Omega$ , and it represents total ignorance.

The value $bel(A)$ quantifies the strength of the belief that event A occurs. It measures the same concept as $P(A)$ does in classical probability theory, but bel is not an additive measure. The value $m(A)$ represents the part of belief that supports the fact that A occurs and cannot support any more specific event (due to a lack of information). Note that m is not the counterpart of a probability distribution function p [17]. Both bel and P are defined on $2^{\Omega}$ , but m is defined on $2^{\Omega}$ whereas p is defined on $\Omega$ .

Given a belief function, we can define a plausibility function $pl: 2^{\Omega} \to [0,1]$ as follows: for $A \subseteq \Omega$

$$
p l (A) = b e l (\Omega) - b e l (\bar {A})
$$

where $\overline{A}$ is the complement of $A$ relative to $\Omega$ .

In fact, m, bel, and pl are in one-to-one correspondence with each other. The plausibility function is just another way of presenting the same information as a belief function. It can be regarded as a measure of the degree to which we do not doubt A. It can also be computed directly from the basic belief assignment:

$$
p l (A) = \sum_ {B \cap A \neq \emptyset} m (B)
$$

Comparing this formula with the one for the belief function, we say that $bel(A)$ quantifies the total amount of justified specific support given to A, and $pl(A)$ quantifies the maximum amount of potential specific support that could be given to A.

If further information such that $A \subseteq \Omega$ is false' becomes available, then the mass $m(B)$ initially allocated to $B$ is transferred to $A \cap B$ . This transfer of belief is called the conditioning process.

Definition 2: Let $bel$ be the belief function representing our belief about the frame $\Omega$ . Suppose we learn that $\overline{A} \subseteq \Omega$ is false. The resulting conditional belief function $bel(\cdot | A)$ ( $bel(B|A)$ can be read as the belief of $B$ given $A$ ) is obtained through the unnormalized rule of conditioning. For $B \subseteq \Omega$

$$
m (B \mid A) = \left\{ \begin{array}{c c} \sum_ {X \subseteq \bar {A}} m (B \cup X) & \text { if } B \subseteq A \subseteq \Omega \\ 0 & \text { otherwise } \end{array} \right.
$$

Except for the lack of normalization, this rule corresponds to Dempster's rule of conditioning [18].

## 2.2. Decision analysis

In this subsection, we show how to generalize the computation of expected utility to accept belief function representation. The basic idea is inspired by Strat [3]. For a problem with a single decision, the presented method and Strat's [3] are exactly the same. Ours is different from Strat's in the case where there is a sequence of decisions to make. This will be discussed later in this subsection. First, let's look at the following example:

Example 1: A carnival wheel is divided into ten equal sectors, each having \$1, \$5, \$10 or \$20 printed out on it. Four sectors are for \$1, two for \$5, two for \$10, and one for \$20. However, one of the sectors is hidden from view, but we know it is one of these four values. How much are we willing to pay to play this game?

This problem cannot be solved directed by computing the expected utility as described at the beginning of this section since the probability information is not complete. The uncertain situation can be well represented using belief functions. The bba representation is as follows:

$$
m (\{1 \}) = 0. 4
$$

$$
m (\{5 \}) = 0. 2
$$

$$
m (\{1 0 \}) = 0. 2
$$

$$
m (\{2 0 \}) = 0. 1
$$

$$
m (\{1, 5, 1 0, 2 0 \}) = 0. 1
$$

Suppose that the utility function is defined as $u( play, \$x) = x$ . For computing the expected utility of this problem, i.e. the expected value we gain if we play the game, we need to know the value of the hidden sector. From the available information, we know that there is a 0.1 chance that the hidden sector is selected, and that the best value of this sector is \$20 and the worst is \$1. Thus we can obtain an interval of the expected value if we play the game:

$$
E (p l a y) = \left[ E _ {*} (p l a y), E ^ {*} (p l a y) \right] = [ 5. 5, 7. 4 ]
$$

where

$$
\begin{array}{l l} E _ {*} (p l a y) & = \sum_ {\theta \subseteq \Theta} m (\theta) \min _ {\theta_ {i} \in \theta} [ u (p l a y, \theta_ {i}) ] \\ & = 0. 4 (1) + 0. 2 (5) + 0. 2 (1 0) + 0. 1 (2 0) + 0. 1 (1) = 5. 5 \\ E ^ {*} (p l a y) & = \sum_ {\theta \subseteq \Theta} m (\theta) \max _ {\theta_ {i} \in \theta} [ u (p l a y, \theta_ {i}) ] \\ & = 0. 4 (1) + 0. 2 (5) + 0. 2 (1 0) + 0. 1 (2 0) + 0. 1 (2 0) = 7. 4. \end{array}
$$

It can be seen that sometimes the interval is not very satisfactory when we have to make a decision. In the example, if the cost of the game is \$5, then we should be willing to play the game regardless of the value of the hidden sector. However, if the game costs \$6, should we play? In this paper, we will use the idea proposed in [3]: let $\lambda$ be the probability that the value assigned to the hidden sector is the one that we would have assigned (i.e. \$20) if given the opportunity, so $(1 - \lambda)$ is the probability that the carnival hawker chooses the value of the hidden sector (i.e. \$1). Then the expected utility of example 1 can be computed as follows:

$$
E (p l a y) = 7. 4 \lambda + 5. 5 (1 - \lambda) = 5. 5 + 1. 9 \lambda
$$

To decide whether to play the game, we need only to assess the parameter $\lambda$ . For example 1, it would be wise to allow that the hawker has hidden the value from view. Thus, we might assume $\lambda = 0$ , and $E( play) = 5.5$ . Therefore, we should not be willing to pay more than \$5.50 to play the game.

Remark: The use of the parameter $\lambda$ to choose a value between two extremes is the same as Strat's method, which is, as discussed in [3], similar in spirit to the Hurwicz approach with a probability distribution [19]. If $\lambda = 0$ , we obtain the minimax criterion. If $\lambda = 1$ , we obtain the maximax criterion. Strat [3] has also explained the reasons for using the parameter $\lambda$ in detail. Recently, Schubert [20] gave an analysis of decision making based on a study of the relation between $\lambda$ and the derived optimal decision.

Table 1  
The result of an electronic test related to the well capacity of the oil

<table><tr><td>Prob.</td><td>Test results</td><td>Capacity</td></tr><tr><td>0.5</td><td>Red (re)</td><td>Dry</td></tr><tr><td>0.2</td><td>Yellow (ye)</td><td>Dry or wet</td></tr><tr><td>0.3</td><td>Green (gr)</td><td>Wet or soaking</td></tr></table>

In this paper, we inherit the basic idea of using $\lambda$ . However, for the case where there is a sequence of decisions to make, we will assume that each time when we meet a decision to be made, we use the parameter to compute the expected utility for that decision. Instead, in [3], the interval is kept until the end of the computation to derive the expected value for the whole problem, which is sufficient to compute the maximum expected utility, but not to find the optimal strategy for each step of decisions. More discussion about when and how $\lambda$ is used will be given later when the method is embedded in valuation-based systems.

## 3. Oil wildcatter problem

Before describing valuation-based systems, let's first look at a decision making problem abstracted from [3], in which some changes have been made in the original one from [7]—the oil wildcatter's problem—where the uncertainties are represented by belief functions.

An oil wildcatter must decide either to drill (d) or not to drill (d). He is uncertain whether the hole is dry (dr), wet (we) or soaking (so). Drilling a hole costs \$70k. The payoffs for hitting a soaking, a wet or a dry hole are \$270k, \$120k, and \$0, respectively. At a cost of \$10k, the wildcatter can make an electronic test that is related to the well capacity of the oil. The result of the application of the test is either red (re), yellow (ye) or green (gr). Due to some extra hidden variables, red indicates that the well is dry, yellow that it is either dry or wet, and green that it is either wet or soaking. Before running the test, there is an a priori probability associated with each of these test results: 0.5 with red, 0.3 with yellow and 0.2 with green (see Table 1).

From Table 1, we find that some of the probabilities are available only for the subsets of possible values of capacity instead of for every single element. Therefore, this problem cannot be directly solved by using Bayesian decision theory. However, we can use a belief measure on $\{dr, we, so\}$ . Next, we will present the decision calculus for belief functions and show how to represent and solve this problem.

## 4. Valuation-based system representation

In valuation-based systems (VBS), a decision problem is represented by variables and valuations. Precedence constraints are needed to represent the chronological constraints among the variables. Two operators, combination and marginalization, are used for the computation. A graphic description of VBS is called a valuation network.

## 4.1. Basic components

A VBS representation for a decision problem defined on a set of variables $\mathbf{U}\left(\mathbf{U}=\mathbf{U}_{D}\cup\mathbf{U}_{R}\right)$ is denoted by a 6-tuple $\Delta=\{\mathbf{U}_{D},\mathbf{U}_{R},\{\Theta_{X}\}_{X\in\mathbf{U}},\{v_{1},\ldots,v_{m}\},\{\beta_{1},\ldots,\beta_{n}\},\rightarrow\}$ , representing decision variables, belief variables $^{1}$ , frames of the variables, utility valuations, belief function valuations, and precedence constraints, respectively.

## 4.1.1. Variables, frames and configurations

The set of variables U consists of decision variables $U_{D}$ and belief variables $U_{R}$ . The possible values of a decision variable represent the acts available at that point. The possible values of a belief variable represent the states of nature. We call the set of all possible values of variable X the frame of X and denote it by $\Theta_{X}$ . Given a non-empty subset A of U, the frame for A, denoted by $\Theta_{A}$ , is the Cartesian product of the frames for the variables in A and the elements of $\Theta_{A}$ are the configurations of A. Graphically, decision variables are represented by rectangles, and belief variables by circles.

4.1.1.1. Notation. If $a_i$ is a configuration of $A(\subseteq \mathbf{U})$ , $b_j$ is a configuration for $B(\subseteq \mathbf{U})$ , and $A \cap B = \emptyset$ , then $(a_i, b_j)$ denotes a configuration for $A \cup B$ . For the empty set $\emptyset$ , let $\diamondsuit$ denote its only configuration. Thus, if $a_i$ is a configuration of $A$ , then $(a_i, \diamondsuit) = a_i$ . We use lowercase letters such as $a, b$ to represent subsets of a frame and lowercase letters with subscripts such as $a_i, b_j$ to represent the corresponding elements. For example, $a_i \in a, b_j \in b$ .

## 4.1.2. Utility valuations

A utility (or payoff) valuation v for $A(\subseteq\mathbf{U})$ is a function from $\Theta_{A}$ to the set of real numbers. The values of utility valuation are utilities. Graphically, utility valuations are represented by diamond-shaped nodes.

## 4.1.3. Belief function valuations

Suppose $A \subseteq \mathbf{U}$ and $A \cap \mathbf{U}_R \neq \emptyset$ . A belief function valuation $\beta$ for $A$ is a belief function defined over $\Theta_A$ . Suppose $R$ is belief variable in $A$ , a belief function valuation $\beta$ bearing on $A$ constructed from a family of conditional belief functions for $R$ given $A - \{R\}$ : $\{bel_R(\cdot | a_i): a_i \in \Theta_{A - \{R\}}\}$ is a non-informative belief function over $A - \{R\}$ . We will discuss the relation between conditional belief functions and non-informative belief functions in more detail after the definition of marginalization. Graphically, belief function valuations are represented by triangles connected to the variables they bear on. A non-informative belief function $\beta$ over $A - \{R\}$ is indicated by an arrow from $\beta$ to $R$ .

## 4.1.4. Precedence constraints

Another ingredient of the VBS representation in decision analysis is chronology or precedence constraints, denoted by $\rightarrow$ . Graphically, it is represented by a bold arrow from one variable to another. Intuitively, $D \rightarrow R$ means that the state of R can only be known after the decision for D has been made. $R \rightarrow D$ means that the decision maker expects to be informed of the true value of R before he makes decision D. Generally, four constraints are needed for the precedence relation:

(p1) the transitive closure of $\rightarrow$ , denoted by $\succ$ , is a partial order (irreflexive and transitive) on U;

(p2) for any $D \in \mathbf{U}_D$ and any $R \in \mathbf{U}_R$ , either $R \succ D$ or $D \succ R$ ;

(p3) if there is a non-informative belief function over $A - \{R\} (R \in \mathbf{U}_R \cap A)$ , and there is a decision variable $D \in A$ , then $D > R$ ;

(p4) if there is a belief function valuation for $A$ and a decision variable $D \in A$ , then $D > R$ for some belief variable $R \in A$ .

Let's look at the oil wildcatter's problem. The valuation network is illustrated in Fig. 1. It consists of two decision variables $D$ with frame $\{\mathrm{d}(\mathrm{drill}), \overline{\mathrm{d}}(\mathrm{not~drill})\}$ and $T$ with frame $\{\mathrm{t}(\mathrm{test}), \overline{\mathrm{t}}(\mathrm{not~test})\}$ , two belief variables $R$ (test results) with frame $\{\mathrm{re}, \mathrm{ye}, \mathrm{gr}, \mathrm{nr}\}$ , where $\mathrm{nr}(\mathrm{no~result})$ represents the state when no test is taken, and $O$ (the state of the oil) with frame $\{\mathrm{dr}, \mathrm{we}, \mathrm{so}\}$ . We also have the precedence relations: $T \to R$ , $R \to D$ , $D \to O$ . There are two utility valuations and two belief function valuations in the network. The utility valuations $v_1$ and $v_2$ stand respectively for the profit from testing and the profit from drilling (see Table 2). The belief function valuations $\beta_1$ and $\beta_2$ (shown in Table 3) are the non-informative belief functions constructed respectively from the conditional belief functions $bel(R|T)$ and $bel(O|R)$ .

Table 3  
![](/api/attachments/D6RQFFXH/fulltext/images/16b250fc8aa35d714556fde1fcd6655bb8539f3cba2e6a7da6db18adf3c1facd.jpg)  
Fig. 1. Graphical VBS representation for the oil wildcatter problem.

## 4.2. Combination and marginalization

Apart from the basic components of the representation, VBS has two operators called combination and marginalization for the computation. Before defining combination and marginalization, we introduce a new representation for both the belief function and the utility valuation as follows:

Table 2  
Utility valuations for the oil wildcatter's problem

<table><tr><td> $a \subseteq \Theta_{\{T\}}$ </td><td> $v_1$ </td><td colspan="2"> $a \subseteq \Theta_{\{D,O\}}$ </td><td> $v_2$ </td></tr><tr><td>t</td><td>-10</td><td>d</td><td>dr</td><td>-70</td></tr><tr><td> $\overline{t}$ </td><td>0</td><td>d</td><td>we</td><td>50</td></tr><tr><td></td><td></td><td>d</td><td>so</td><td>200</td></tr><tr><td></td><td></td><td> $\overline{d}$ </td><td>dr</td><td>0</td></tr><tr><td></td><td></td><td> $\overline{d}$ </td><td>we</td><td>0</td></tr><tr><td></td><td></td><td> $\overline{d}$ </td><td>so</td><td>0</td></tr></table>

Non-informative belief function $\beta_{1}$ over $\{T\}$ constructed from bel (Result|Test) and for $\beta_{2}$ over $\{D\}$ from bel (Oil|Result)

<table><tr><td colspan="2"> $a \subseteq \Theta_{\{T,R\}}$ </td><td> $\beta_1$ </td><td colspan="2"> $b \subseteq \Theta_{\{R,O\}}$ </td><td> $\beta_2$ </td></tr><tr><td>t</td><td>re</td><td>0.5</td><td>re</td><td>dr</td><td>0.5</td></tr><tr><td> $\bar{t}$ </td><td>nr</td><td></td><td>ye</td><td>dr</td><td></td></tr><tr><td>t</td><td>ye</td><td>0.2</td><td>ye</td><td>we</td><td></td></tr><tr><td> $\bar{t}$ </td><td>nr</td><td></td><td>gr</td><td>we</td><td></td></tr><tr><td>t</td><td>gr</td><td>0.3</td><td>gr</td><td>so</td><td></td></tr><tr><td> $\bar{t}$ </td><td>nr</td><td></td><td>nr</td><td>dr</td><td></td></tr><tr><td></td><td></td><td></td><td>re</td><td>dr</td><td>0.2</td></tr><tr><td></td><td></td><td></td><td>ye</td><td>dr</td><td></td></tr><tr><td></td><td></td><td></td><td>ye</td><td>we</td><td></td></tr><tr><td></td><td></td><td></td><td>gr</td><td>we</td><td></td></tr><tr><td></td><td></td><td></td><td>gr</td><td>so</td><td></td></tr><tr><td></td><td></td><td></td><td>nr</td><td>dr</td><td></td></tr><tr><td></td><td></td><td></td><td>nr</td><td>we</td><td></td></tr><tr><td></td><td></td><td></td><td>re</td><td>dr</td><td>0.3</td></tr><tr><td></td><td></td><td></td><td>ye</td><td>dr</td><td></td></tr><tr><td></td><td></td><td></td><td>ye</td><td>we</td><td></td></tr><tr><td></td><td></td><td></td><td>gr</td><td>we</td><td></td></tr><tr><td></td><td></td><td></td><td>gr</td><td>so</td><td></td></tr><tr><td></td><td></td><td></td><td>nr</td><td>we</td><td></td></tr><tr><td></td><td></td><td></td><td>nr</td><td>so</td><td></td></tr></table>

Suppose $\mu$ is a valuation for $A(\subseteq \mathbf{U})$ . $\mu$ can always be represented by a set of pair $(a, \mathcal{F}_{\mu,a})$ where $\mathcal{F}_{\mu,a}$ pairs is defined as $\{(a_i, f_{\mu,a}(a_i)): a_i \in a\}$ , $a$ is a non-empty subset of $\Theta_A$ and $f_{\mu,a}$ is a mapping from $a$ to the set of real numbers with respect to $\mu$ (for belief functions, the real numbers are in the interval [0, 1]). Then, both belief functions (or bba's) and utilities can be similarly represented as follows.

\- Suppose $v$ is a utility valuation for $A$ . Then $v$ can be represented by a set with one element $(a, \mathcal{F}_{v,a})$ where $\mathcal{F}_{v,a} = \{(a_i, f_{v,a}(a_i): a_i \in a\}$ , and $a = \Theta_A$ . For each $a_i \in \Theta_A$ , $f_{v,a}(a_i) = v(a_i)$ . For example, in the oil wildcatter problem, $v_2$ is a utility valuation for $\{D, O\}$ . It is represented as a set with one element $(\Theta_{\{D,O\}}), \mathcal{F}_{v_2,\Theta_{\{D,O\}}}$ . Table 2 shows $\mathcal{F}_{v_2,\Theta_{\{D,O\}}} = \{(a_i, f_{v_2,\Theta_{\{p,O\}}} (a_i))\}$ . For an element of $\Theta_{\{D,O\}}$ , say (d, dr), $f_{v_2,\Theta_{\{D,O\}}}((d,dr)) = v_2((d,dr)) = -70$ . $v_1$ is represented in a similar way.

\- Suppose $\beta$ is a belief function for $A$ . Then it can be represented by a set with elements like $(a, \mathcal{F}_{\beta,a})$ , where $a$ is a focal element of $\beta$ and $\mathcal{F}_{\beta,a} = \{(a_i, f_{\beta,a}(a_i)): a_i \in a\}$ . For every $a_i \in a$ , $f_{\beta,a}(a_i) = m(a)$ . Specifically, if $\beta$ is a probability for $A$ , then it is represented as a set of $(a, \{(a_i, f_{\beta,a}(a_i))\})$ , where $a$ is a singleton subset $\{a_i\}$ , and $f_{\beta,a}(a_i) = p(a_i)$ . For example, in the oil wildcatter problem, $\beta_1$ is a belief function valuation for $\{T, R\}$ . It is represented as a set of three elements like $(a, \mathcal{F}_{\beta_1,a})$ , $\mathcal{F}_{\beta_1,a} = \{(a_i, f_{\beta_1,a}(a_i))\}$ where $a \subseteq \Theta_{\{T,R\}}$ . Table 3 shows $\mathcal{F}_{\beta_1,a}$ . Let $a = \{(t, re), (t, nr)\}$ , for every $a_i$ of $a$ , e.g. $a_i = (t, re)$ , $f_{\beta_1,a}(a_i) = m(\{(t,re), (t,nr)\}) = 0.5$ . $\beta_2$ has a similar representation.

The concepts of projection and extension are needed for the definition of combination and marginalization. Definition 3: Projection of configurations simply means dropping the extra coordinates. If $X$ and $Y$ are sets of variables, $Y \subseteq X$ , and $x_i$ is an element of $\Theta_X$ , then let $x_i^{\downarrow Y}$ denote the projection of $x_i$ to $\Theta_Y$ . $x_i^{\downarrow Y}$ is an element of $\Theta_Y$ . If $x$ is a non-empty subset of $\Theta_X$ , then the projection of $x$ to $Y$ , denoted by $x^{\downarrow Y}$ , is obtained by $x^{\downarrow Y} = \{x_i^{\downarrow Y} | x_i \in x\}$ . If $y$ is a subset of $\Theta_Y$ , then the extension of $y$ to $X$ , denoted by $y^{\uparrow X}$ , is $y \times \Theta_{X-Y}$ (it is also called the cylindric extension of $y$ into $X$ ).

## 4.2.1. Combination

The definition of combination depends on the type of the valuations being combined. Let $A$ and $B$ be subsets of $\mathbf{U}$ .

\- Suppose $\beta_{A}$ and $\beta_{B}$ are belief function valuations for $A$ and $B$ , respectively. Then their combination, denoted by $\beta_{A} \otimes \beta_{B}$ , is a belief function valuation for $A \cup B$ , defined by Dempster's rule of combination. Since only belief functions are involved here, we can use $m_{A}(a)$ and $m_{B}(b)$ directly. Therefore, $\beta_{A} \otimes \beta_{B}$ is obtained by: for any $c \subseteq \Theta_{A \cup B}$

$$
(m _ {A} \otimes m _ {B}) (c) = K ^ {- 1} \sum_ {a ^ {\uparrow A \cup B} \cap b ^ {\uparrow A \cup B} = c} m _ {A} (a) m _ {B} (b)
$$

where

$$
K = 1 - \sum_ {a ^ {\uparrow A \cup B} \cap b ^ {\uparrow A \cup B} = \emptyset} m _ {A} (a) m _ {B} (b)
$$

\- Suppose $v_A$ and $v_B$ are utility valuations for $A$ and $B$ , respectively. Then their combination, denoted by $v_A \otimes v_B$ , is a utility valuation for $A \cup B$ . Since only utilities are involved here, we can use $v_A(a_i)$ and $v_B(b_j)$ directly. Then the computation is as follows: for any $c_k \in \Theta_{A \cup B}$

$$
\left(v _ {A} \otimes v _ {B}\right) \left(c _ {k}\right) = v _ {A} \left(c _ {k} ^ {\downarrow A}\right) + v _ {B} \left(c _ {k} ^ {\downarrow B}\right)
$$

\- Suppose $\beta_{A}$ is a belief function valuation for $A$ and $v_{B}$ is a utility valuation for $B$ . Let the combination be represented by a set of $(c, \{(c_{k}, f_{\beta_{A} \otimes v_{B}, c}(c_{k}))\})$ . It is obtained by: for any $c_{k} \in c$ , $c \in \{a^{\uparrow A \cup B} \cap b^{\uparrow A \cup B}\}$

$$
f _ {\beta_ {A} \otimes v _ {B}, c} (c _ {k}) = \sum_ {a ^ {\uparrow A \cup B} \cap b ^ {\uparrow A \cup B} = c} f _ {\beta_ {A}, a} \left(c _ {k} ^ {\downarrow A}\right) f _ {v _ {B}, b} \left(c _ {k} ^ {\downarrow B}\right)
$$

Note that the combination of a belief function and a utility valuation is not a belief function. The resulting valuation could be a utility valuation or a collection of subset-utility pairs. We call this kind of valuation and utility valuation a ‘non-belief function valuation’. From the definition, we find that the combination has the following properties:

1. the combination is commutative;

2. the combination for belief functions is associative, so is that for utility valuations;

3. the combination for a mixture of belief functions and utility valuations is not associative.

In case 3, if there is only one utility valuation, the combination is still associative. Therefore, in order to deal with the lack of associativity, we define the combination for a mixture of belief function valuation and utility valuations where they can be in any order as follows. First combine all the utility valuations, then combine the resulting valuation with the combination of belief functions. Formally, suppose $v_{1}, \ldots, v_{m}$ are utilities and $\beta_{1}, \ldots, \beta_{n}$ are belief functions. Then $(\otimes \{v_{1}, \ldots, v_{m}, \beta_{1}, \ldots, \beta_{n}\})$ denotes $(\otimes \{v_{1}, \ldots, v_{m}\}) \otimes (\otimes \{\beta_{1}, \ldots, \beta_{n}\})$ .

For the definition of marginalization, we propose to use the parameter $\lambda$ , as discussed in Section 2. It has been mentioned that, in [3], $\lambda$ is used only once at the end of computation of expected utility. For a decision problem with a sequence of decision to be made, this is not enough. In our paper, we will use $\lambda$ as follows. Recall the definition of precedence constraint. We have assumed that for any decision variable D and belief variable R, either $R \succ D$ or $D \succ R$ . Then we can partition the set of all belief variables $U_{R}$ into a set of disjoint sets $I_{0}, \ldots, I_{n}$ satisfying $I_{0} \succ D_{1} \succ \ldots \succ D_{m} \succ I_{n}$ where $U_{D} = \{D_{1}, \ldots, D_{m}\}$ . Therefore we assume that $\lambda$ is used once for each set $I_{i}$ . As the deletion sequence respects the precedence constraint, only the belief variable which is deleted just before a decision variable or the last variable to be deleted will use $\lambda$ in its deletion. For the sake of representation simplicity, we add constraint (p5) for the precedence relation so that $\lambda$ is used once each time when a belief variable is deleted.

(p5) For any two belief variables $R_{1}$ and $R_{2}$ (if there exist), there exists at least a decision variable $D$ such that $R_{1} \succ D \succ R_{2}$ or $R_{2} \succ D \succ R_{1}$ , or there does not exist any decision variables in the valuation network.

## 4.2.2. Marginalization

Suppose $A$ is a subset of $\mathbf{U}$ containing variable $X$ , and $\alpha$ is a valuation for $A$ , represented as a set of $(a, \mathcal{F}_{\alpha, a})$ , $\mathcal{F}_{\alpha, a} = \{(a_i, f_{\alpha, a}(a_i))\}, a_i \in a$ . The definition of marginalization depends on the type of variables being eliminated. Since the criterion of maximizing the expected utility is used, eliminating a decision variable is done by maximization, while computation for eliminating a belief variable depends on the uncertain formalism being used. The marginal of $\alpha$ for $A - \{X\}$ , denoted by $\alpha^{\downarrow (A - \{X\})}$ , is a valuation for $A - \{X\}$ , defined as follows: for $b \subseteq \Theta_{A - \{X\}}$

If $X$ is a decision variable, then $\forall b_{i} \in b$

$$
f _ {\alpha^ {\downarrow (A - \{X \})}, b} (b _ {i}) = \sum_ {a ^ {\downarrow (A - \{X \})} = b} \max \left[ f _ {\alpha , a} (a _ {j}) \mid a _ {j} ^ {\downarrow (A - \{X \})} = b _ {i} \right]\tag{1}
$$

If $X$ is a belief variable, then $\forall b_{i} \in b$

$$
f _ {\alpha^ {\downarrow (A - \{X \})}, b} (b _ {i}) = \sum_ {a ^ {\downarrow (A - \{X \})} = b} \left\{\lambda \max \left[ f _ {\alpha , a} (a _ {j}) \mid a _ {j} ^ {\downarrow (A - \{X \})} = b _ {i} \right] + (1 - \lambda) \min \left[ f _ {\alpha , a} (a _ {j}) \mid a _ {j} ^ {\downarrow (A - \{X \})} = b _ {i} \right] \right\}\tag{2}
$$

From the definition, we find that the marginalization has the following properties:

1. Suppose $A(\subseteq \mathbf{U})$ contains decision variables $D_{1}$ and $D_{2}$ , and $\alpha$ is a non-belief function valuation $^{2}$ for $A$ . Then we have

$$
\left(\alpha^ {\downarrow (A - \{D _ {1} \})}\right) ^ {\downarrow (A - \{D _ {1}, D _ {2} \})} = \left(\alpha^ {\downarrow (A - \{D _ {2} \})}\right) ^ {\downarrow (A - \{D _ {1}, D _ {2} \})}
$$

2. Suppose $A(\subseteq \mathbf{U})$ contains belief variable $R_{1}$ and $R_{2}$ , and $\alpha$ is a non-belief function valuation for $A$ . Then generally

$$
\left(\alpha^ {\downarrow (A - \{R _ {1} \})}\right) ^ {\downarrow (A - \{R _ {1}, R _ {2} \})} \neq \left(\alpha^ {\downarrow (A - \{R _ {2} \})}\right) ^ {\downarrow (A - \{R _ {1}, R _ {2} \})}\tag{3}
$$

But if $\alpha$ is a belief function, then

$$
\left(\alpha^ {\downarrow (A - \{R _ {1} \})}\right) ^ {\downarrow (A - \{R _ {1}, R _ {2} \})} = \left(\alpha^ {\downarrow (A - \{R _ {2} \})}\right) ^ {\downarrow (A - \{R _ {1}, R _ {2} \})}
$$

Note that constraint (p5) avoids the situation in which two belief variables $R_{1}$ and $R_{2}$ exist in the deletion sequence such that $X_{1} \succ R_{1} \succ X_{2}$ and $X_{1} \succ R_{2} \succ X_{2}$ , thus the situation of the inequality (Eq. (3)) is avoided. In practice, if two such belief variables do exist, the solution to this problem is to merge these two random variables as one variable before deleting them. For Bayesian decision problem, constraint (p5) is not needed since the value is always unique when a belief variable is deleted, thus $\lambda$ will never be used, i.e. $\max [f_{\alpha,a}(a_j)|a_j^{\downarrow (A - \{X\})} = b_i]$ is always equal to $\min [f_{\alpha,a}(a_j)|a_j^{\downarrow (A - \{X\})} = b_i]$ in Eq. (2).

If there are neither decision variables nor utility valuations in VBS, it is easy to prove that combination is then reduced to Dempster's rule of combination, and marginalization (Eq. (2)) is then reduced to the following:

$$
\alpha^ {\downarrow (A - \{X \})} (b) = \sum_ {a ^ {\downarrow (A - \{X \})} = b} \alpha (a)\tag{4}
$$

Thus, the VBS is reduced to an evidential system for propagating belief functions $[9,21]$ .

## 4.3. Non-informative belief functions

From the definition of combination, we can see that all the belief functions are processed in the form of joint belief on a product space. In this subsection, we will discuss so-called non-informative belief functions which represent the same information as conditional belief functions, but they are defined on a product space.

Definition 4: Suppose $A \subseteq \mathbf{U}$ , $R \in A \cap \mathbf{U}_R$ , and $\beta$ is a belief function valuation for $A$ . If $\beta^{\downarrow (A - \{R\})}$ is a vacuous belief function for $A - \{R\}$ , then $\beta$ is a non-informative belief function over $A - \{R\}$ .

Note that the non-informative belief function is on the joint space of all the variables involved, whereas a conditional belief function for $R$ given $A - \{R\}$ is a belief on $\Theta_R$ given each element of $A - \{R\}$ . The use of conditional belief functions parallels the use of conditional probabilities in a Bayesian network. It is more 'natural' and 'easy' for the user to provide and to understand the belief functions in conditional form [22]. For example, in Table 3, we cannot judge whether $\beta_1$ is non-informative or not over some variables if we do not use marginalization. However, the belief functions provided by the users in the form in Table 1 are more natural. Thus, we can assume that the users' knowledge is encoded in the conditional form and that the joint beliefs are constructed based on the known conditional form. Therefore, we can use conditional beliefs for the representation, and construct the joint belief from the conditional beliefs for the computation. However, the joint belief functions induced by a family of conditional beliefs are not always unique [22]. Smets [18] has shown that when the conditional belief functions are represented by $\{bel_B(\cdot |a_i):a_i\in \Theta_A\}$ where $A, B$ are two disjoint subsets of $\mathbf{U}$ , we can always construct a joint belief function from it, and when the Principle of Minimal Commitment is applied, the joint belief is unique by combining the so-called ballooning extension of the conditional beliefs.

The ballooning extension of a conditional belief function over B given $a \subseteq \Theta_{A}$ is the belief function over $\Theta_{A \cup B}$ such that $m(b|a) (b \subseteq \Theta_{B})$ is allocated to the set $b^{\uparrow A \cup B} \cup \overline{a}^{\uparrow A \cup B}$ , i.e. the largest subset of $\Theta_{A \cup B}$ such that its intersection with $b^{\uparrow A \cup B}$ is the extension of b to $A \cup B$ .

The belief function so built is the least committed belief function on $\Theta_{A\cup B}$ among all belief function on $\Theta_{A\cup B}$ whose conditioning on $a^{\uparrow A\cup B}$ is equal to $bel(\cdot |a)$ . Formally, the ballooning extension of $bel_B(b|a)$ ( $a\subseteq \Theta_A$ , $b\subseteq \Theta_B$ ) on $A\times B$ is computed as follows [18]:

$$
b e l _ {A \times B} (b ^ {\uparrow A \cup B} \cup \bar {a} ^ {\uparrow A \cup B}) = b e l _ {b} (b | a)
$$

Lemma 1: [18] Suppose $A$ and $B$ are two disjoint subsets of $\mathbf{U}$ . If all we know about the relation between $A$ and $B$ is given by a family of conditional belief functions: $\{bel_{B}(\cdot |a_{i}):a_{i}\in \Theta_{A}\}$ or represented by $m_B(\cdot |a_i)$ , then, by combining the ballooning extension of each $bel_{B}(\cdot |a_{i})$ on $\Theta_{A\cup B}$ , we can construct the belief function on $\Theta_{A\cup B}$ as follows [23,18]. Let $c\subseteq \Theta_{A\cup B}$ and $b^{i} = (c\cap \{a_{i}\}^{\uparrow A\cup B})^{\downarrow B}$ . We have

$$
m _ {A \cup B} (c) = \prod_ {a _ {i} \in \Theta_ {A}} m _ {B} \left(b ^ {i} \mid a _ {i}\right)\tag{5}
$$

It is easy to find that a belief function for $A$ constructed from $\{bel_R(\cdot |a_i):a_i\in \Theta_{A - \{R\}}\}$ or equally from $\{m_R(\cdot |a_i):a_i\in \Theta_{A - \{R\}}\}$ by using lemma 1 (combining the ballooning extensions) is a non-informative belief function over $A - \{R\}$ .

For the oil wildcatter problem, the two belief function valuations are defined in conditional form as follows (from Table 1):

$$
m (\{\mathrm{re} \} | t) = 0. 5, m (\{\mathrm{ye} \} | t) = 0. 2, m (\{\mathrm{gr} \} | t) = 0. 3;
$$

$$
m (\{\mathrm{nr} \} \mathbb {t}) = 1;
$$

$$
m (\{\mathrm{dr} \} | \mathrm{re}) = 1; m (\{\mathrm{dr}, \mathrm{we} \} | \mathrm{ye}) = 1; m (\{\mathrm{we}, \mathrm{so} \} | \mathrm{gr}) = 1;
$$

$$
m (\{\mathrm{dr} \} | \mathrm{nr}) = 0. 5, m (\{\mathrm{dr}, \mathrm{we} \} | \mathrm{nr}) = 0. 2, m (\{\mathrm{we}, \mathrm{so} \} | \mathrm{nr}) = 0. 3
$$

The corresponding valuations in joint form can be computed by lemma 1. For example, to compute $\beta_{1}$ for $\{T, R\}$ , we have

$$
m (\{\mathrm{t}, \mathrm{re}), (\bar {\mathrm{t}}, \mathrm{nr}) \} = m (\{\mathrm{re} \} | \mathrm{t}) \times m (\{\mathrm{nr} \} | \bar {\mathrm{t}}) = 0. 5 \times 1 = 0. 5
$$

$$
m (\{(t, \mathrm{ye}), (\bar {t}, \mathrm{nr}) \} = m (\{\mathrm{ye} \} | t) \times m (\{\mathrm{nr} \} | t) = 0. 2 \times 1 = 0. 2
$$

$$
m (\{\mathrm{(t,gr)}, (\mathrm{t,nr}) \} = m (\{\mathrm{gr} \} | \mathrm{t}) \times m (\{\mathrm{nr} \} [ \mathrm{t}) = 0. 3 \times 1 = 0. 3
$$

The masses on the other subsets are zeros. Similarly, we can compute $\beta_{2}$ for $\{R, O\}$ as well. The results are shown in Table 3.

For the non-informative belief functions, we have the following lemmas:

Lemma 2: Suppose $\beta_{1}$ is a belief function constructed from a family of conditional beliefs for $R$ given $A - \{R_{1}\}$ , $\beta_{2}$ is a belief function constructed from a family of conditional beliefs for $R$ given $B - \{R_{2}\}$ . Then $\beta_{1} \otimes \beta_{2}$ is a non-informative belief function over $(A \cup B) - \{R_{1}, R_{2}\}$ .

Proof: To prove the above conclusion, we need to prove: For any focal element $a$ in $\beta_{1}$ , any focal element $b$ in $\beta_{2}$ , $(a^{\uparrow A\cup B}\cap b^{\uparrow A\cup B})^{\downarrow (A\cup B - \{R_1,R_2\})} = \Theta_{A\cup B - \{R_1,R_2\}}$ . Since $\beta_{1}$ and $\beta_{2}$ are constructed from conditional belief functions, we have:

For any focal element $a$ of $\beta_{1}, a^{\downarrow A - \{R_{1}\}} = \Theta_{A - \{R_{1}\}}$

For any focal element $b$ of $\beta_{2}$ , $b^{\downarrow B - \{R_2\}} = \Theta_{B - \{R_2\}}$

Because $R_{1} \notin B$ , $R_{2} \notin A$ , according to the definition of extension, we have:

$$
\forall x _ {i} \in \Theta_ {A \cup B - \{R _ {1}, R _ {2} \}}, r _ {2} \in \Theta_ {R _ {2}}, \exists r _ {1} \in \Theta_ {R _ {1}}, ((x _ {i}, r _ {2}), r _ {1}) \in a ^ {\uparrow A \cup B}
$$

$$
\forall x _ {i} \in \Theta_ {A \cup B - \{R _ {1}, R _ {2} \}}, r _ {1} \in \Theta_ {R _ {1}}, \exists r _ {2} \in \Theta_ {R _ {2}}, ((x _ {i}, r _ {1}), r _ {2}) \in b ^ {\uparrow A \cup B}
$$

Thus, $\forall x_{i}\in\Theta_{(A\cup B-\{R_{1},R_{2}\})},\exists r_{1}\in\Theta_{R_{1}},r_{2}\in\Theta_{R_{2}}$ , such that $(x_{i},(r_{1},r_{2}))\in(a^{\uparrow A\cup B}\cap b^{\uparrow A\cup B})$ . In other words, $\forall x_{i}\in\Theta_{(A\cup B-\{R_{1},R_{2}\})},x_{i}\in(a^{\uparrow A\cup B}\cap b^{\uparrow A\cup B})^{\downarrow(A\cup B-\{R_{1},R_{2}\})}$ . Therefore, the lemma is proved.

Lemma 3: Suppose $X \in \mathbf{U}_R$ , $v$ is a utility valuation for $A$ bearing on $X$ , $\beta$ is a non-informative belief function over $B - \{X\}$ . $(v \otimes \beta)^{\downarrow (A \cup B - \{X\})}$ is a utility valuation for $A \cup B - \{X\}$ .

Proof: $v$ has only one element $(a, \mathcal{F}_{v,a})$ where $a = \Theta_A$ , and $\Theta_A^{\uparrow A \cup B} = \Theta_{A \cup B}$ . Let $b$ be a focal element of $\beta$ , then $a^{\uparrow A \cup B} \cap b^{\uparrow A \cup B} = b^{\uparrow A \cup B} = b \times \Theta_{A - B}$ . By the definition of non-informative belief functions, $b^{\downarrow (B - \{X\})}$ $= \Theta_{B - \{X\}}$ then $(b^{\uparrow A\cup B})^{\downarrow (A\cup B - \{X\})} = \Theta_{A\cup B - \{X\}}$ . Thus, $(v\otimes \beta)^{\downarrow (A\cup B - \{X\})}$ has only one element $(c,\mathcal{F}_{(v\otimes \beta)^{\downarrow (A\cup B - \{X\})},c})$ where $c = \Theta_{A\cup B - \{X\}}$ , i.e. it is a utility valuation for $A\cup B - \{X\}$

From lemma 2, we have that, if the problem is represented by non-informative belief functions, then all the belief functions will be non-informative belief functions during computation. Thus, the normalization factor K can be ignored for such a case.

## 5. VBS solution

The main objective in solving a decision problem is computing an optimal strategy. A strategy is a choice of an act for each decision variable D as a function of configurations of belief variables R such that $R \succeq D$ . Computing a strategy is a book-keeping matter. Each time we eliminate a decision variable from a valuation using maximization, we store a table of optimal values of the decision variable where the maxima are achieved. We can regard this table as a function, and call it ‘solution for that decision variable’. Formally, suppose $D \in A$ , we use $\Psi_{D}$ : $\Theta_{A-\{D\}} \to \Theta_{D}$ to denote the solution for D.

## 5.1. Solving a canonical decision problem

Consider a canonical decision problem $\Delta_c = \{\{D\}, \{R\}, \{\Theta_D, \Theta_R\}, \{v\}, \{\beta\}, \to\}$ as described at the beginning of Section 2. Its VBS representation is illustrated in Fig. 2.

Solving Bayesian decision problems in VBS is based on the criterion of maximizing expected payoff. The presented calculus is essentially based on the generalization for expectation operation for belief functions proposed by Strat [3]. As shown in Fig. 2, $\Delta_c = \{\{D\}, \{R\}, \{\Theta_D, \Theta_R\}, \{v\}, \{\beta\}, \to\}$ where $\beta$ is constructed from a family of conditional belief functions for $R$ given $\{D\}$ . Let $v \otimes \beta$ be represented as $\{(a, \mathcal{F}_{v \otimes \beta, a})\}$ where $\mathcal{F}_{v \otimes \beta, a} = \{(a_i, f_{v \otimes \beta, a}(a_i)) : a_i \in a\}$ . Based on the generalization for expectation operation for belief functions, the expected utility interval is computed by: for $d_i \in \Theta_D$

$$
\left[ \sum_ {a \subseteq \Theta_ {\{D, R \}}} \min _ {r _ {j} \in \Theta_ {R}} \left\{f _ {v \otimes \beta , a} \left(\left(d _ {i}, r _ {j}\right)\right) \right\}, \sum_ {a \subseteq \Theta \{D, R \}} \max _ {r _ {j} \in \Theta_ {R}} \left\{f _ {v \otimes \beta , a} \left(\left(d _ {i}, r _ {j}\right)\right) \right\} \right]
$$

But an interval of expected values is not very satisfactory when we have to make a decision. Thus, additional assumptions need to be made to compute a unique expected utility. To this end, the parameter $\lambda$ is proposed to resolve the ambiguity. Then the expected value (associated with an optimal act $d^{*}$ with respect to $\lambda$ ) is $((v \otimes \beta)^{\downarrow \{D\}})^{\downarrow \emptyset}(\diamond)$ , act $d^{*}$ is optimal if $(v \otimes \beta)^{\downarrow \{D\}}(d^{*}) = ((v \otimes \beta)^{\downarrow \{D\}})^{\downarrow \emptyset}(\diamond)$ . Note that $(v \otimes \beta)^{\downarrow \{D\}}$ is a utility valuation according to lemma 3.

Note that if $\beta$ is defined as a probability function, the computation of the expected utility interval is reduced to the computation of the unique expected utility, and the combination and the marginalization are reduced to those for probability theory.

![](/api/attachments/D6RQFFXH/fulltext/images/92a5292bcbad069a0dfe074d03d783e8d7e0c5691937798a524e375223f2e861.jpg)  
Fig. 2. A graphical representation of VBS for a decision problem.

## 5.2. VBS solution using fusion algorithm

For solving Bayesian decision problems, Shenoy [12] introduced a division operator; he also gave some restriction for VBS representation in order to avoid divisions during computation. Since division of two belief functions does not always result in a belief function, we will only discuss the decision calculus in the case where the division can be avoided. Therefore, we state the following assumption for the VBS representation.

Assumption 1: In the VBS representation, at least one of the following two conditions should be satisfied. (1) There is only one utility valuation. (2) For each belief variable, we only have a non-informative belief function constructed from a family of conditional belief functions for that variable such that the variables on which the belief function is conditioned always precede the belief variable.

In order to use the VBS solution method, the VBS representation of a decision problem needs to be well-defined for the case of belief functions. Formally, the VBS representation $\Delta = \{\mathbf{U}\}_{D}$ , $\mathbf{U}_R$ , $\{\Theta_X\}_{X \in \mathbf{U}}$ , $\{v_1, \ldots, v_m\}$ , $\{\beta_1, \ldots, \beta_n\}, \to$ is well-defined if

1. $\cup \mathbf{H}_D\supseteq \mathbf{U}_D$ , where $\mathbf{H}_D$ denotes the set of subsets of $\mathbf{U}$ for which payoff valuations exist in the VBS;

2. $\cup \mathbf{H}_R \supseteq \mathbf{U}_R$ , where $\mathbf{H}_R$ denotes the set of subsets of $\mathbf{U}$ for which probability valuations exist;

3. the five constraints (p1) to (p5) (cf. Section 4) for the precedence relation ‘→’ are satisfied;

4. suppose $Q$ is the subset of decision variables included in the domain of the joint belief function $\beta_1 \otimes \ldots \otimes \beta_n$ . Then $(\beta_1 \otimes \ldots \otimes \beta_n)^{\downarrow Q}$ is a vacuous belief function for $Q$ .

If the VBS representation of a decision problem is well-defined. Then it can be reduced to an equivalent canonical problem $\Delta_c$ [12]. Computing an optimal strategy can be achieved in two steps: first, we compute the maximum expected value of the utilities, obtained by $((\otimes \{v_1,\dots,v_m\})\otimes (\otimes \{\beta_1,\dots,\beta_n\}))^{\downarrow \emptyset}(\diamond)$ , or simply $(\otimes \{v_1,\dots,v_m,\beta_1,\dots,\beta_n\})^{\downarrow \emptyset}(\diamond)$ ; second, we compute an optimal strategy $\sigma^{*}$ that gives us the maximum expected value.

A strategy $\sigma^{*}$ of $\Delta$ is optimal if $(v\otimes \beta)^{\downarrow \{D\}}(d_{\sigma_{*}}) = (\otimes \{v_{1},\ldots ,v_{m},\beta_{1},\ldots ,\beta_{n}\})^{\downarrow \emptyset}(\diamond)$ where $v,\beta$ and $D$ refer to the equivalent canonical problem $\Delta_c$ of $\Delta$ .

However, when there are two many variables in the network, it is not computationally tractable to compute $(\otimes\{v_{1},\ldots,v_{m},\beta_{1},\ldots,\beta_{n}\})$ . Shenoy [11,12] has proposed a fusion algorithm, an application of local computational technique to the solution of VBS. The core of this algorithm is the fusion operation. Consider a set of valuations $\alpha_{1},\ldots,\alpha_{k}$ , suppose $\alpha_{i}$ is a valuation for $A_{i}$ . Let $Fus_{X}\{\alpha_{1},\ldots,\alpha_{k}\}$ denote the collection of valuations after deleting a variable X, then

$$
F u s _ {X} \left\{\alpha_ {1}, \dots , \alpha_ {k} \right\} = \alpha^ {\downarrow (A - \{X \})} \cup \left\{\alpha_ {i} | X \notin A _ {i} \right\}\tag{6}
$$

where $\alpha = \otimes \{\alpha_i | X \in A_i\}$ , and $A = \cup \{A_i | X \in A_j\}$ .

The solution method of VBS for decision problems is called the fusion algorithm [11]. The basic idea is to successively delete all the variables from the VBS. The sequence in which the variables are deleted must respect the precedence constraints, i.e. if $X \succ Y$ , then $Y$ must be deleted before $X$ . The following theorem shows that this fusion algorithm can also be used for the case of belief functions. The proof will be given in Appendix A.

Theorem 1: Suppose $\Delta = \{\mathbf{U}_D, \mathbf{U}_R, \{\Theta_X\}_{X \in (\mathbf{U})}, \{v_1, \ldots, v_m\}, \{\beta_1, \ldots, \beta_n\}, \to\}$ is a well-defined VBS representation for the case of belief functions, and satisfies Assumption 1. Using the decision calculus defined above, we can also use the fusion algorithm to solve such VBS.

It is easy to prove that the representation is well-defined. Then, conceptually, we can compute the expected value by $(((v_{1} \otimes v_{2}) \otimes (\beta_{1} \otimes \beta_{2}))^{\downarrow\{T,R,D\}})^{\downarrow\{T,R\}})^{\downarrow\{T\}})^{\downarrow\emptyset}$ . The maximal frame is $\Theta_{\{T,R,D,O\}}$ . By using the fusion algorithm, the expected utility is computed by $(((((\beta_{2} \otimes v_{2})^{\downarrow\{R,D\}})^{\downarrow\{R\}}) \otimes \beta_{1})^{\downarrow\{T\}}) \otimes v_{1})^{\downarrow\emptyset}$ where the maximal frame involved is $\Theta_{\{R,D,O\}}$ . Obviously, the latter is more efficient since the maximal frame involved in the computation is smaller. Tables 4–7 illustrate the computation in detail when $\lambda = 0.5$ . The result (when $\lambda = 0.5$ ) is: the maximal expected value is 27.5k. An optimal strategy can be constructed from the information in $\Psi_{T}$ and $\Psi_{D}$ . From $\Psi_{T}$ , it can be seen that the wildcatter should do the test. And from $\Psi_{D}$ , it can be seen that if the test result is red, the optimal decision is not to drill; if the result is yellow or green, the optimal decision is to drill. If $\lambda = 0$ , then the maximal expected utility is \$5k; the optimal strategy is to do the test first, and if the test result is green then to drill, otherwise, not to drill. If $\lambda = 1.0$ , then the maximal expected utility is \$60k; the optimal strategy is to do the test first, and if the test result is red then not to drill, otherwise, to drill. The maximum expected utility value and the optimal strategy change according to the value of $\lambda$ .

Computation of $\lambda \max +(1 - \lambda)\min$ part $(\beta_{2}\otimes v_{2})^{\downarrow \{R,D\}}$ (see Eq. (2)), summation will be done in Table 5). Here, $c = a^{\uparrow \{R,D,O\}}\cap b^{\uparrow \{R,D,O\}}$ , where $a,b$ are the extended focal elements of $v_{2}$ and $\beta_{2}$ , respectively. $\lambda = 0.5$ is used in marginalization

<table><tr><td colspan="3"> $c \subseteq \Theta_{\{R,D,O\}}$ </td><td> $\beta_2$ </td><td> $v_2$ </td><td> $\beta_2 \otimes v_2$ </td><td> $(\beta_2 \otimes v_2)^{\mathbf{1}\{R,D\}}$ </td></tr><tr><td>re</td><td>d</td><td>dr</td><td>0.5</td><td>-70</td><td>-35</td><td>-35</td></tr><tr><td>re</td><td> $\overline{d}$ </td><td>dr</td><td></td><td>0</td><td>0</td><td>0</td></tr><tr><td>ye</td><td>d</td><td>dr</td><td></td><td>-70</td><td>-35</td><td>0.5(-35)+0.5(25)=-5</td></tr><tr><td>ye</td><td>d</td><td>we</td><td></td><td>50</td><td>25</td><td></td></tr><tr><td>ye</td><td> $\overline{d}$ </td><td>dr</td><td></td><td>0</td><td>0</td><td>0.5(0)+0.5(0)=0</td></tr><tr><td>ye</td><td> $\overline{d}$ </td><td>we</td><td></td><td>0</td><td>0</td><td></td></tr><tr><td>gr</td><td>d</td><td>we</td><td></td><td>50</td><td>25</td><td>0.5(25)+0.5(100)=62.5</td></tr><tr><td>gr</td><td>d</td><td>so</td><td></td><td>200</td><td>100</td><td></td></tr><tr><td>gr</td><td> $\overline{d}$ </td><td>we</td><td></td><td>0</td><td>0</td><td>0.5(0)+0.5(0)=0</td></tr><tr><td>gr</td><td> $\overline{d}$ </td><td>so</td><td></td><td>0</td><td>0</td><td></td></tr><tr><td>nr</td><td>d</td><td>dr</td><td></td><td>-70</td><td>-35</td><td>-35</td></tr><tr><td>nr</td><td> $\overline{d}$ </td><td>dr</td><td></td><td>0</td><td>0</td><td>0</td></tr><tr><td>re</td><td>d</td><td>dr</td><td>0.2</td><td>-70</td><td>-14</td><td>-14</td></tr><tr><td>re</td><td> $\overline{d}$ </td><td>dr</td><td></td><td>0</td><td>0</td><td>0</td></tr><tr><td>ye</td><td>d</td><td>dr</td><td></td><td>-70</td><td>-14</td><td>0.5(-14)+0.5(10)=-2</td></tr><tr><td>ye</td><td>d</td><td>we</td><td></td><td>50</td><td>10</td><td></td></tr><tr><td>ye</td><td> $\overline{d}$ </td><td>dr</td><td></td><td>0</td><td>0</td><td>0.5(0)+0.5(0)=0</td></tr><tr><td>ye</td><td> $\overline{d}$ </td><td>we</td><td></td><td>0</td><td>0</td><td></td></tr><tr><td>gr</td><td>d</td><td>we</td><td></td><td>50</td><td>10</td><td>0.5(10)+0.5(40)=25</td></tr><tr><td>gr</td><td>d</td><td>so</td><td></td><td>200</td><td>40</td><td></td></tr><tr><td>gr</td><td> $\overline{d}$ </td><td>we</td><td></td><td>0</td><td>0</td><td>0.5(0)+0.5(0)=0</td></tr><tr><td>gr</td><td> $\overline{d}$ </td><td>so</td><td></td><td>0</td><td>0</td><td></td></tr><tr><td>nr</td><td>d</td><td>dr</td><td></td><td>-70</td><td>-14</td><td>0.5(-14)+0.5(10)=-2</td></tr><tr><td>nr</td><td>d</td><td>we</td><td></td><td>50</td><td>10</td><td></td></tr><tr><td>nr</td><td> $\overline{d}$ </td><td>dr</td><td></td><td>0</td><td>0</td><td>0.5(0)+0.5(0)=0</td></tr><tr><td>nr</td><td> $\overline{d}$ </td><td>we</td><td></td><td>0</td><td>0</td><td></td></tr><tr><td>re</td><td>d</td><td>dr</td><td>0.3</td><td>-70</td><td>-21</td><td>-21</td></tr><tr><td>re</td><td> $\overline{d}$ </td><td>dr</td><td></td><td>0</td><td>0</td><td>0</td></tr><tr><td>ye</td><td>d</td><td>dr</td><td></td><td>-70</td><td>-21</td><td>0.5(-21)+0.5(15)=-3</td></tr><tr><td>ye</td><td>d</td><td>we</td><td></td><td>50</td><td>15</td><td></td></tr><tr><td>ye</td><td> $\overline{d}$ </td><td>dr</td><td></td><td>0</td><td>0</td><td>0.5(0)+0.5(0)=0</td></tr><tr><td>ye</td><td> $\overline{d}$ </td><td>we</td><td></td><td>0</td><td>0</td><td></td></tr><tr><td>gr</td><td>d</td><td>we</td><td></td><td>50</td><td>15</td><td>0.5(15)+0.5(60)=37.5</td></tr><tr><td>gr</td><td>d</td><td>so</td><td></td><td>200</td><td>60</td><td></td></tr><tr><td>gr</td><td> $\overline{d}$ </td><td>we</td><td></td><td>0</td><td>0</td><td>0.5(0)+0.5(0)=0</td></tr><tr><td>gr</td><td> $\overline{d}$ </td><td>so</td><td></td><td>0</td><td>0</td><td></td></tr><tr><td>nr</td><td>d</td><td>we</td><td></td><td>50</td><td>15</td><td>0.5(15)+0.5(60)=37.5</td></tr><tr><td>nr</td><td>d</td><td>so</td><td></td><td>200</td><td>60</td><td></td></tr><tr><td>nr</td><td> $\overline{d}$ </td><td>we</td><td></td><td>0</td><td>0</td><td>0.5(0)+0.5(0)=0</td></tr><tr><td>nr</td><td> $\overline{d}$ </td><td>so</td><td></td><td>0</td><td>0</td><td></td></tr></table>

Computation of $\tau^{\downarrow (R)}$ where $\tau = (\beta_{2}\otimes v_{2})^{\downarrow (R,D)}$ . $\Psi_D$ is stored when $D$ is deleted

<table><tr><td> $c \subseteq \Theta_{\{R,D\}}$ </td><td></td><td> $\tau^{\downarrow\{R,D\}}$ </td><td> $\tau^{\downarrow\{R\}}$ </td><td> $\Psi_D$ </td></tr><tr><td>re</td><td>d</td><td>-70.0</td><td></td><td></td></tr><tr><td>re</td><td> $\overline{d}$ </td><td>0.0</td><td>0.0</td><td> $\overline{d}$ </td></tr><tr><td>ye</td><td>d</td><td>-10.0</td><td></td><td></td></tr><tr><td>ye</td><td> $\overline{d}$ </td><td>0.0</td><td>0.0</td><td> $\overline{d}$ </td></tr><tr><td>gr</td><td>d</td><td>125.0</td><td>125</td><td>d</td></tr><tr><td>gr</td><td> $\overline{d}$ </td><td>0.0</td><td></td><td></td></tr><tr><td>nr</td><td>d</td><td>0.5</td><td>0.5</td><td>d</td></tr><tr><td>nr</td><td> $\overline{d}$ </td><td>0.0</td><td></td><td></td></tr></table>

Computation of $(\tau^{\downarrow \{R\}}\otimes \beta_{1})^{\downarrow \{T\}}$ where $\tau = (\beta_{2}\otimes v_{2})^{\downarrow \{R,D\}}$ . Let $c = a^{\uparrow \{R,T\}}\cap b^{\uparrow \{R,T\}}$ , where $a,b$ are the extended focal elements of $\beta_{1}$ and $\tau^{\downarrow \{R\}}$ , respectively. $\lambda$ is not needed in marginalization because $\beta_{1}$ is a probability

<table><tr><td> $c \subseteq \Theta_{\{R,T\}}$ </td><td></td><td> $\beta_1$ </td><td> $\tau^{\downarrow \{R\}}$ </td><td> $\tau^{\downarrow \{R\}} \otimes \beta_1$ </td><td> $(\tau^{\downarrow \{R\}} \otimes \beta_1)^{\downarrow \{T\}}$ </td></tr><tr><td>re</td><td>t</td><td>0.5</td><td>0.0</td><td>0.00</td><td>0.00</td></tr><tr><td>nr</td><td> $\bar{t}$ </td><td></td><td>0.5</td><td>0.25</td><td>0.25</td></tr><tr><td>ye</td><td>t</td><td>0.2</td><td>0.0</td><td>0.00</td><td>0.00</td></tr><tr><td>nr</td><td> $\bar{t}$ </td><td></td><td>0.5</td><td>0.10</td><td>0.10</td></tr><tr><td>gr</td><td>t</td><td>0.3</td><td>125.0</td><td>37.50</td><td>37.50</td></tr><tr><td>nr</td><td> $\bar{t}$ </td><td></td><td>0.5</td><td>0.15</td><td>0.15</td></tr></table>

Computation of $(v\otimes v_{1})^{\downarrow \emptyset}$ where $v = (\tau^{\downarrow \{R\}}\otimes \beta_{1})^{\downarrow \{T\}}$ $\Psi_T$ is stored when $T$ is deleted

<table><tr><td> $c \subseteq \Theta_{\{T\}}$ </td><td> $v$ </td><td> $v_1$ </td><td> $v \otimes v_1$ </td><td> $\tau^{\downarrow \emptyset}(\diamondsuit)$ </td><td> $\Psi_T$ </td></tr><tr><td>t</td><td>37.5</td><td>-10</td><td>27.5</td><td>27.5</td><td>t</td></tr><tr><td> $\overline{t}$ </td><td>0.5</td><td>0</td><td>0.5</td><td></td><td></td></tr></table>

## 6. Conclusions

We have presented and discussed a decision calculus for belief function theory in VBS, which can be regarded as a generalization of the calculus for the Bayesian probability theory. If there are no belief variables in the problem, which is thus an optimization problem, the solution technique reduces to dynamic programming $[21,12]$ . If there are no decision variables, then our objective may become to find the marginal of some variables and the solution technique reduces to the one for belief function propagation in an evidential system. The presented calculus has some limitations due to the division of belief functions. For the case of probability theory, VBS representation can directly represent arbitrary probability, and the division operation is introduced to the solution method for such a case. Extension to this similar case for belief function theory remains a topic for future research.

We have also proposed a parameter $\lambda$ for marginalization in the presented calculus. This idea is inspired by Strat's method for making the additional assumption when sufficient information is not available for making the decision. Although this criteria may not be the best one for decision making, as Strat commented on his method, the objective in this paper is to develop a decision calculus for belief function theory which can benefit from the VBS representation and solution method for decision problems, especially from the fusion algorithm which can reduce the complexity of computation, and all those computations both for belief functions and for utilities are in one VBS framework. Xu et al. [24] have proposed a decision support system using belief functions which is an integration of an evidential system for belief function propagation and a valuation-based system for Bayesian decision analysis, based on the transferable belief model [16]. In this system, the maximum expected utility is always unique due to the pignistic transformation [2] from belief functions to probabilities when decision has to be made, which avoids the use of the parameter.

## Acknowledgements

I am very grateful to Yen-Teh Hsia, Prakash Shenoy, Philippe Smets and Alessandro Saffiotti for their careful reading and valuable suggestions on this paper. I would also express my appreciation to the anonymous referees for their careful reading of the paper and excellent suggestions and comments. This work has been supported by a grant of IRIDIA, Université libre de Bruxelles.

## Appendix A. Proof of Theorem 1

We first state and prove several lemmas related to the local computations. For the sake of simplicity, from now on, we use the same notation as in [12] if the valuation is a utility valuation, use bba to represent the belief function valuation if it is a belief function, and use the unified representation only when it is necessary.

Lemma 4: Suppose $X \in \mathbf{U}_D$ , $v$ is a utility valuation for $A$ bearing on $X$ , $\beta$ is a belief function for $B$ , $X \notin B$ . $X$ is the minimal variable of $A \cup B$ with respect to the precedence constraint. Then

$$
(v \otimes \beta) ^ {\downarrow (A \cup B - \{X \})} = \beta \otimes v ^ {\downarrow (A - \{X \})}
$$

Proof: $v$ has only one pair $(a, \mathcal{F}_{v,a})$ where $a = \Theta_A$ , $\Theta_A^{\uparrow A \cup B} = \Theta_{A \cup B}$ . Suppose $b$ is a focal element of $\beta$ , then $a^{\uparrow A \cup B} \cap b^{\uparrow A \cup B} = b^{\uparrow A \cup B} = b \times \Theta_{A - B}$ . Let $\{(c, \mathcal{F}_{(v \otimes \beta)^{\downarrow (A \cup B - \{X\}), c}})\}$ be the resulting valuation, then $c = (b^{\uparrow A \cup B})^{\downarrow (A \cup B - \{X\})}$ . Since $X \notin B$ , we have that, $(b^{\uparrow A \cup B})^{\downarrow (A \cup B - \{X\})} = b^{\uparrow (A \cup B - \{X\})}$ and $m(b^{\uparrow A \cup B}) = m((b^{\uparrow A \cup B})^{\downarrow (A \cup B - \{X\})})$ .

$$
\begin{array}{l} f _ {(v \otimes \beta) ^ {\downarrow (A \cup B - \{X \})}, c} (c _ {i}) = \sum_ {b ^ {\uparrow (A \cup B - \{X \})} = c} \max \left[ v \left(x _ {j}, c _ {i} ^ {\downarrow (A - \{X \})}\right) m \left(b ^ {\uparrow A \cup B}\right) | x _ {j} \in \Theta_ {X} \right] \\ = \sum_ {b ^ {\uparrow (A \cup B - \{X \})} = c} \max \left[ v \left(x _ {j}, c _ {i} ^ {\downarrow (A - \{X \})}\right) | x _ {j} \in \Theta_ {X} \right] m \left(b ^ {\uparrow A \cup B - \{X \}}\right) = f _ {v ^ {\downarrow (A - \{X \})} \otimes \beta , c} (c _ {i}) \end{array}
$$

which concludes the proof.

Lemma 5: Suppose $X \in \mathbf{U}_R$ , $\beta$ is a belief function for $A$ bearing on $X$ , $v$ is a utility valuation for $B$ , $X \notin B$ . $X$ is the minimal variable of $A \cup B$ with respect to the precedence constraint. Then

$$
\left(\nu \otimes \beta\right) ^ {\downarrow (A \cup B - \{X \})} = \nu \otimes \beta^ {\downarrow (A - \{X \})}
$$

Proof: Let $\{(c, \mathcal{F}_{(v \otimes \beta) \downarrow (A \cup B - \{X\}), c)\}$ be the resulting valuation, then $c = (a^{\uparrow A \cup B} \cap b^{\uparrow A \cup B})^{\downarrow (A \cup B - \{X\})} = (a^{\uparrow A \cup B})^{\downarrow (A \cup B - \{X\})}$ . Therefore

$$
\begin{array}{l} f _ {(v \otimes \beta) ^ {\downarrow (A \cup B - \{X \})}, c} (c _ {i}) = \sum_ {(a ^ {\uparrow A \cup B}) ^ {\downarrow (A \cup B - \{X \})} = c} \left\{\left(\lambda \max \left[ v (c _ {i} ^ {\downarrow B}) m (a ^ {\uparrow A \cup B}) | x _ {i} \in a ^ {\downarrow \{X \}} \right] \right. \right. \\ \left. + (1 - \lambda) \min \left[ v (c _ {i} ^ {\downarrow B}) m (a ^ {\uparrow A \cup B}) | x _ {i} \in a ^ {\downarrow \{X \}} \right] \right\} = v (c _ {i} ^ {\downarrow B}) \sum_ {(a ^ {\uparrow A \cup B}) ^ {\downarrow (A \cup B - \{X \})} = c} \\ \times \left\{\lambda \max \left[ m (a ^ {\uparrow A \cup B}) | x _ {i} \in a ^ {\downarrow \{X \}} \right] + (1 - \lambda) \min \left[ m (a ^ {\uparrow A \cup B}) | x _ {i} \in a ^ {\downarrow \{X \}} \right] \right\} \\ = v (c _ {i} ^ {\downarrow B}) \sum_ {a ^ {\downarrow (A - \{X \})}) ^ {\uparrow ((A - \{X \}) \cup B)} = c} \left\{\lambda \max \left[ m (a) | x _ {i} \in a ^ {\downarrow \{X \}} \right] \right. \\ + (1 - \lambda) \min \left[ m (a) | x _ {i} \in a ^ {\downarrow \{X \}} \right] \Bigg \} = f _ {v \otimes \beta^ {\downarrow (A - \{X \})}, c} (c _ {i}) \end{array}
$$

which concludes the proof.

Lemma 6: Suppose $X \in \mathbf{U}_R$ , $\beta_1$ is a belief function for $A$ bearing on $X$ , $v$ is a utility valuation for $B$ bearing on $X$ , $\beta_2$ is a belief function for $B'$ , $X \notin B'$ . $X$ is the minimal variable of $A \cup B \cup B'$ with respect to the precedence constraint. Then

$$
\left(v \otimes \beta_ {2} \otimes \beta_ {1}\right) ^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = \left(\beta_ {1} \otimes v\right) ^ {\downarrow (A \cup B - \{X \})} \otimes \beta_ {2}
$$

Proof: According to assumption 6.1, $\beta_{1}$ and $\beta_{2}$ are constructed from conditional belief functions. Thus, combination is associative, and $K = 1$ . Let $a$ and $b'$ be focal elements of $\beta_{1}$ and $\beta_{2}$ , respectively, and $\mu$ the resulting valuation. Let $d' = (a^{\uparrow A \cup B \cup B'} \cap b^{\uparrow A \cup B \cup B'} \cap b'^{\uparrow A \cup B \cup B'})^{\downarrow (A \cup B \cup B' - \{X\})}$ . Since $b = \Theta_{B}$ , $d' = (a^{\uparrow A \cup B \cup B'} \cap b'^{\uparrow A \cup B \cup B'})^{\downarrow (A \cup B \cup B' - \{X\})}$ . As $X \notin B'$ , we get $b'^{\uparrow (A \cup B \cup B' - \{X\})} = b'^{\uparrow B' \cup (A \cup B - \{X\})}$ . Therefore,

$$
\begin{array}{l} f _ {\mu , c} (c _ {i}) = \sum_ {d ^ {\prime} = c} \Big \{\lambda \max \Big [ m _ {1} (a ^ {\uparrow A \cup B \cup B ^ {\prime}}) m _ {2} (b ^ {\uparrow A \cup B \cup B ^ {\prime}}) v \big ((x _ {i}, c _ {i} ^ {\downarrow (A - \{X \})}) \big) | x _ {i} \in \Theta_ {X} \Big ] \\ \qquad + (1 - \lambda) \min \Big [ m _ {1} (a ^ {\uparrow A \cup B \cup B ^ {\prime}}) m _ {2} (b ^ {\uparrow A \cup B \cup B ^ {\prime}}) v \big ((x _ {i}, c _ {i} ^ {\downarrow (A - \{X \})}) \big) | x _ {i} \in \Theta_ {X} \Big ] \Big \} \\ = m _ {2} (b ^ {\uparrow A \cup B \cup B ^ {\prime}}) \sum_ {d ^ {\prime} = c} \Big \{\lambda \max \Big [ m _ {1} (a ^ {\uparrow A \cup B \cup B ^ {\prime}}) v \big ((x _ {i}, c _ {i} ^ {\downarrow (A - \{X \})}) \big) | x _ {i} \in \Theta_ {X} \Big ] \\ \qquad + (1 - \lambda) \min \Big [ m _ {1} (a ^ {\uparrow A \cup B \cup B ^ {\star}}) v \big ((x _ {i}, c _ {i} ^ {\downarrow (A - \{X \})}) \big) | x _ {i} \in \Theta_ {X} \Big ] \Big \} = m _ {2} (b ^ {\uparrow (A \cup B \cup B ^ {\prime} - \{X \})}) \\ \qquad + (1 - \lambda) \min \Big [ m _ {1} (a ^ {\uparrow A \cup B}) v (\big ((x _ {i}, c _ {i} ^ {\downarrow (A - \{X \})}) \big) | x _ {i} \in \Theta_ {X} \Big ] \\ \qquad + (1 - \lambda) \min \Big [ m _ {1} (a ^ {\uparrow A \cup B}) v (\big ((x _ {i}, c _ {i} ^ {\downarrow (A - \{X \})}) \big) | x _ {i} \in \Theta_ {X} \Big ] \Big \} = f _ {(\beta_ {1} \otimes v) ^ {\downarrow (A \cup B - \{X \})} \otimes \beta_ {2}, c} (c _ {i}) \end{array}
$$

which concludes the proof.

Lemma 7: Suppose $X \in \mathbf{U}_R$ , $\beta$ is constructed from a family of conditional belief functions for $X$ given $A - \{X\}$ , $v$ and $v'$ are utility valuations for $B$ and $B'$ , respectively, $X \in B$ , $X \notin B'$ . $X$ is the minimal variable of $A \cup B \cup B'$ with respect to the precedence constraint. Then

$$
\left(v \otimes v ^ {\prime} \otimes \beta\right) ^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = \left(\beta \otimes v\right) ^ {\downarrow (A \cup B - \{X \})} \otimes v ^ {\prime}
$$

Proof: Since $\beta$ is constructed from a family of conditional belief functions for $X$ given $A - \{X\}$ , $\beta^{\downarrow (A - \{X\})}$ is a vacuous belief function. Using lemma 3, we have that the resulting valuation of the left hand side is a utility valuation. Let $C' = A \cup B \cup B'$ , $C = C' - \{X\}$ . Then

$$
\begin{array}{l} \big (v \otimes v ^ {\prime} \otimes \beta \big) ^ {\downarrow (A \cup B \cup B \cup B ^ {\prime} - \{X \})} \big (c _ {i} \big) \\ = \sum_ {(x _ {i}, c _ {i}) \in a ^ {\uparrow C ^ {\prime}}} \Big \{\lambda \max \Big [ m (a ^ {\uparrow C ^ {\prime}}) \Big (v \Big (\big (x _ {i}, c _ {i} ^ {\downarrow (B - \{X \})} \big) \Big) + v ^ {\prime} \big (c _ {i} ^ {\downarrow B ^ {\prime}} \big) \Big) | x _ {i} \in \Theta_ {X} \Big ] \\ + (1 - \lambda) \min \Big [ m (a ^ {\uparrow C ^ {\prime}}) \Big (v \Big (\big (x _ {i}, c _ {i} ^ {\downarrow (B - \{X \})} \big) \Big) + v ^ {\prime} \big (c _ {i} ^ {\downarrow B ^ {\prime}} \big) \Big) | x _ {i} \in \Theta_ {X} \Big ], \\ = \sum_ {(x _ {i}, c _ {i}) \in a ^ {\uparrow C ^ {\prime}}} \Big \{m (a ^ {\uparrow C ^ {\prime}}) \Big (\lambda \max \Big [ v \Big (\big (x _ {i}, c _ {i} ^ {\downarrow (B - \{X \})} \big) \Big) + v ^ {\prime} \big (c _ {i} ^ {\downarrow B ^ {\prime}} \big) | x _ {i} \in \Theta_ {X} \Big ] \\ + (1 - \lambda) \min \Big [ v \Big (\big (x _ {i}, c _ {i} ^ {\downarrow (B - \{X \})} \big) \Big) + v ^ {\prime} \big (c _ {i} ^ {\downarrow B ^ {\prime}} \big) | x _ {i} \in \Theta_ {X} \Big ] \Big), \\ = \sum_ {(x _ {i}, c _ {i}) \in a ^ {\uparrow C ^ {\prime}}} \Big \{m (a ^ {\uparrow C ^ {\prime}}) \Big (\lambda \max \Big [ v \Big (\big (x _ {i}, c _ {i} ^ {\downarrow (B - \{X \})} \big) | x _ {i} \in \Theta_ {X} \Big ] \Big) \\ + (1 - \lambda) \min \Big [ v \Big (\big (x _ {i}, c _ {i} ^ {\downarrow (B - \{X \})} \big) | x _ {i} \in \Theta_ {X} \Big ] \Big), \\ = ((\beta \otimes v) ^ {\downarrow (A \cup B - \{X \})} \otimes (v ^ {\prime} \otimes \beta^ {\downarrow (A - \{X \})})) (c _ {i}) = ((\beta \otimes v) ^ {\downarrow A U B - \{X \})} \otimes v ^ {\prime}) (c _ {i}) \\ = ((\beta \otimes v) ^ {\downarrow (A U B - \{X \})} \otimes (v ^ {\prime} \otimes b ^ {\downarrow (A - \{X \})})) (c _ {i}) = ((\beta \otimes v) ^ {\downarrow A U B - \{X \})} \otimes v ^ {\prime}) (c _ {i}).   \end{array}
$$

which concludes the proof.

To prove theorem 1, we need to prove the following lemma.

Lemma 8: Suppose $\Delta = \{\mathbf{U}_D, \mathbf{U}_R, \{\Theta_X\}_{X \in \mathbf{U}}\}, \{v_1, \ldots, v_m\}, \{\beta_1, \ldots, \beta_n\}, \to\}$ for the case of belief functions is a well-defined VBS representation (including (p5) for precedence relation), and satisfies assumption 6.1. Suppose $X$ is a minimal variable in $\mathbf{U} = \mathbf{U}_D \cup \mathbf{U}_R$ , with respect to the partial order $\succ$ , where $\succ$ is the transitive closure of $\rightarrow$ . Then

$$
\left(\otimes \left\{v _ {1}, \dots , v _ {m}, \beta_ {1}, \dots , \beta_ {n} \right\}\right) ^ {\downarrow (\mathrm{U} - \{X \})} = \otimes F u s _ {X} \left\{v _ {1}, \dots , v _ {m}, \beta_ {1}, \dots , \beta_ {n} \right\}
$$

Proof: We prove this lemma in four mutually exclusive and exhaustive cases.

Case 1: Suppose $X \in \mathbf{U}_D$ , and none of the belief functions bear on $X$ . Without loss of generality, assume $v_1, \ldots, v_k$ are the utility valuations bearing on $X$ . Let $v = \otimes \{v_1, \ldots, v_k\}$ , $B = \cup \{B_1, \ldots, B_k\}$ , then

$$
\left(\otimes \left\{v _ {1}, \dots , v _ {m}, \beta_ {1}, \dots , \beta_ {n} \right\}\right) ^ {\downarrow (\mathbf {U} - \{X \})} = \otimes \left(\left\{v ^ {\downarrow (B - \{X \})} \right\} \cup \left\{v _ {i} | X \notin B _ {i} \right\} \cup \left\{\beta_ {1}, \dots , \beta_ {n} \right\}\right)\tag{7}
$$

Let $v' = \otimes \{v_{k+1}, \ldots, v_m\}$ , $B' = \cup \{B_{k+1}, \ldots, B_m\}$ , $\beta = \otimes \{\beta_1, \ldots, \beta_n\}$ , $A = \cup \{A_1, \ldots, A_n\}$ , then Eq. (7) can be simplified as

$$
\left(v \otimes v ^ {\prime} \otimes \beta\right) ^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = v ^ {\downarrow (B - \{X \})} \otimes v ^ {\prime} \otimes \beta
$$

By the definition and properties of combination, $v \otimes v'$ can be regarded as a utility valuation for $B \cup B'$ , and by lemma 4, we have

$$
\left(v \otimes v ^ {\prime} \otimes \beta\right) ^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = \left(\left(v \otimes v ^ {\prime}\right) \otimes \beta\right) ^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = \left(v \otimes v ^ {\prime}\right) ^ {\downarrow (B \cup B ^ {\prime} - \{X \})} \otimes \beta
$$

It has been proved in [12] that $(v\otimes v^{\prime})^{\downarrow (B\cup B^{\prime} - \{X\})} = v^{\downarrow (B - \{X\})}\otimes v^{\prime}$ , then

$$
\left(v \otimes v ^ {\prime} \otimes \beta^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = \left(v \otimes v ^ {\prime}\right) ^ {\downarrow (B ^ {\prime} \cup B - \{X \})} \otimes \beta = v ^ {\downarrow (B - \{X \})} \otimes v ^ {\prime} \otimes \beta \right.
$$

Case 2: Suppose $X \in \mathbf{U}_R$ , and none of the utility valuations bear on $X$ . Without loss of generality, assume that $\beta_1, \ldots, \beta_k$ are the belief functions bearing on $X$ . Let $\beta = \otimes \{\beta_1, \ldots, \beta_k\}$ , $B = \cup \{B_1, \ldots, B_k\}$ . Then

$$
\left(\otimes \left\{v _ {1}, \dots , v _ {m}, \beta_ {1}, \dots , \beta_ {n} \right\}\right) ^ {\downarrow (\mathrm{U} - \{X \})} = \left\{v _ {1}, \dots , v _ {m} \right\} \otimes \left\{\beta^ {\downarrow (B - \{X \})} \right\} \otimes \left\{\beta_ {i} | X \notin B _ {i} \right\}\tag{8}
$$

Let $\beta' = \otimes\{\beta_{k+1}, \ldots, \beta_n\}$ , $B \ldots = \cup\{B_{k+1}, \ldots, B_n\}$ , $v = \otimes\{v_1, \ldots, v_m\}$ , $A = \cup\{A_1, \ldots, A_m\}$ , then Eq. (8) can be simplified to

$$
\left(\beta \otimes \beta^ {\prime} \otimes v\right) ^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = v \otimes \beta^ {\prime} \otimes \beta^ {\downarrow (B - \{X \})}
$$

By lemma 5, we have

$$
\left(v \otimes \beta^ {\prime} \otimes \beta\right) ^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = \left(v \otimes \left(\beta \otimes \beta^ {\prime}\right)\right) ^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = v \otimes \left(\beta \otimes \beta^ {\prime}\right) ^ {\downarrow (B \cup B ^ {\prime} - \{X \})}
$$

It has been proved in [10] that

$$
\left(\beta^ {\prime} \otimes \beta\right) ^ {\downarrow (B \cup B ^ {\prime} - \{X \})} = \beta^ {\downarrow (B - \{X \})} \otimes \beta^ {\prime}
$$

therefore

$$
\left(v \otimes \beta^ {\prime} \otimes \beta\right) ^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = v \otimes \left(\beta \otimes \beta^ {\prime}\right) ^ {\downarrow (B \cup B ^ {\prime} - \{X \})} = v \otimes \beta^ {\prime} \otimes \beta^ {\downarrow (B - \{X \})}
$$

Case 3: Suppose $X \in \mathbf{U}_R$ , and all the utility valuations bear on $X$ . Without loss of generality, assume that $\beta_1, \ldots, \beta_k$ , $v_1, \ldots, v_j$ are the belief functions bearing on $X$ . Let $\beta = \otimes \{\beta_1, \ldots, \beta_k\}$ , $B = \cup \{B_1, \ldots, B_k\}$ , $v = \otimes \{v_1, \ldots, v_m\}$ , $A = \cup \{A_1, \ldots, A_m\}$ . Then

$$
\left(\otimes \left\{v _ {1}, \dots , v _ {m}, \beta_ {1}, \dots , \beta_ {n} \right\}\right) ^ {\downarrow (\mathrm{U} - \{X \})} = \left\{\left(v \otimes \beta\right) ^ {\downarrow (A \cup B - \{X \})} \otimes \left\{\beta_ {i} | X \notin B _ {i} \right\} \right.\tag{9}
$$

Let $\beta' = \otimes\{\beta_{k+1}, \ldots, \beta_n\}$ , $B' = \cup\{B_{k+1}, \ldots, B_n\}$ , then Eq. (9) can be simplified as follows

$$
\left(\beta \otimes \beta^ {\prime} \otimes v\right) ^ {\downarrow (A \cup B \cup B ^ {\prime} - \{X \})} = \left(v \otimes \beta\right) ^ {\downarrow (A \cup B - \{X \})} \otimes \beta^ {\prime}
$$

which is the result of lemma 6.

Case 4: Suppose $X \in \mathbf{U}_R$ , and there exist utility valuations bearing on $X$ and utility valuations not bearing on $X$ . Without loss of generality, assume that $\beta_1, \ldots, \beta_k, v_1, \ldots, v_j$ are the belief functions and utility valuations bearing on $X$ . Let $\beta = \otimes \{\beta_1, \ldots, \beta_k\}$ , $B = \cup \{B_1, \ldots, B_k\}$ , $v = \otimes \{v_1, \ldots, v_j\}$ , $A = \cup \{A_1, \ldots, A_j\}$ . Then

$$
\left(\otimes \left\{v _ {1}, \dots , v _ {m}, \beta_ {1}, \dots , \beta_ {n} \right\}\right) ^ {\downarrow (\mathrm{U} - \{X \})} = \left\{v _ {i} | X \notin A _ {i} \right\} \otimes \left\{\left(v \otimes \beta\right) ^ {\downarrow (A \cup B - \{X \})} \right\} \otimes \left\{\beta_ {i} | X \notin B _ {i} \right\}\tag{10}
$$

Let $\beta' = \otimes \{\beta_{k+1}, \ldots, \beta_n\}$ , $B' = \cup \{B_{k+1}, \ldots, B_n\}$ , $v' = \otimes \{v_{j+1}, \ldots, v_m\}$ , $A' = \cup \{A_{j+1}, \ldots, A_m\}$ . Then Eq. (10) can be simplified as follows

$$
\left(v \otimes v ^ {\prime} \otimes \beta \otimes \beta^ {\prime}\right) ^ {\downarrow (A \cup A ^ {\prime} \cup B \cup B ^ {\prime} - \{X \})} = v ^ {\prime} \otimes (v \otimes \beta) ^ {\downarrow (A \cup B - \{X \})} \otimes \beta^ {\prime}
$$

By the properties of combination, the left hand side of the above equation can also be written as: $((v \otimes v') \otimes \beta \otimes \beta')^{1(A \cup A' \cup B \cup B' - \{X\})}$ , where $v \otimes v'$ can be regarded as a utility valuation for $A \cup A'$ bearing on $X$ . Then, it becomes Case 3

$$
\left(\left(v \otimes v ^ {\prime}\right) \otimes \beta \otimes \beta^ {\prime}\right) ^ {\downarrow (A \cup A ^ {\prime} \cup B \cup B ^ {\prime} - \{X \})} = \left(\left(v \otimes v ^ {\prime}\right) \otimes \beta\right) ^ {\downarrow (A \cup A ^ {\prime} \cup B - \{X \})} \otimes \beta^ {\prime}
$$

By lemma 7, we have

$$
\left(\left(v \otimes v ^ {\prime}\right) \otimes \beta\right) ^ {\downarrow (A \cup A ^ {\prime} \cup B - \{X \})} = v ^ {\prime} \otimes \left(v \otimes \beta\right) ^ {\downarrow (A \cup B - \{X \})}
$$

therefore

$$
\left(\left(v \otimes v ^ {\prime}\right) \otimes \beta \otimes \beta^ {\prime}\right) ^ {\downarrow (A \cup A ^ {\prime} \cup B \cup B ^ {\prime} - \{X \})} = \left(\left(v \otimes v ^ {\prime}\right) \otimes \beta\right) ^ {\downarrow (A \cup A ^ {\prime} \cup B - \{X \})} \otimes \beta^ {\prime} = v ^ {\prime} \otimes (v \otimes \beta) ^ {\downarrow (A \cup B - \{X \})} \otimes \beta^ {\prime}
$$

which concludes the proof.

Proof of theorem 1: By definition, $(\otimes \{v_1, \ldots, v_m, \beta_1, \ldots, \beta_n\})^{\downarrow \emptyset}$ is obtained by deleting a variable sequentially with respect to the deletion sequence. By the definition of marginalization and lemma 2, we have that after deletion and fusion at each step, the resulting VBS is well-defined. Thus, we can apply the result of lemma 8 repeatedly until all the variables are deleted, and the resulting valuation will be $(\otimes \{v_1,\dots ,v_m,\beta_1,\dots ,\beta_n\})^{\downarrow \emptyset}$ by using lemma 8.

## References

[1] Jaffray J. Y., Linear utility theory for belief functions, Oper. Res. Lett. 8 (1989) 107–112.

[2] Smets Ph., Constructing the pignistic probability function in a context of uncertainty, in M. Henrion, R. D. Shachter, L. N. Kanal and J. Lemmer, eds. Uncertainty in Artificial Intelligence 5 (North-Holland, Amsterdam, 1990) 29–40.

[3] Strat T., Decision analysis using belief functions, Int. J. Approx. Reasoning 4 (1990) 391–417.

[4] Yager R. R., Decision making under Dempster-Shater uncertainties, Iona College Machine Intelligence Institute Tech. Rep. MII-915 (1989).

[5] Dubois D. and Prade H., Decision evaluation methods under uncertainty and imprecision, in J. Kacprzyk and M. Federizzi eds. Lecture Notes in Economics and Mathematical Systems: Combining Fuzzy Imprecision with Probabilistic Uncertainty in Decision Making 310 (Springer, Berlin, 1987) 48–65.

[6] Howard R. A. and Matheson J. E., Influence diagrams, in Readings on the Principles and Applications of Decision Analysis, II (Strategic Decision Group, Menlo Park, CA, 1981) 719–762.

[7] Raiffa H., Decision Analysis (Random House, New York, 1968).

[8] Shachter R. D., Evaluating influence diagrams, Oper. Res. 34 (1986) 871–882.

[9] Shenoy P. P., A valuation-based language for expert systems, Int. J. Approx. Reasoning 3 (1989) 383–411.

[10] Shenoy P. P., Valuation-based systems: A framework for managing uncertainty in expert systems, in L. A. Zadeh and J. Kacprzyk, eds. Fuzzy Logic for the Management of Uncertainty (John Wiley, New York, 1992) 83–104.

[11] Shenoy P. P., A fusion algorithm for solving Bayesian decision problems, in B. D. D'Ambrosio, Ph. Smets and P. P. Bonissone, eds. Proc. 7th Uncertainty in Artificial Intelligence (San Mateo, CA, Morgan Kaufmann, 1991) 323–331.

[12] Shenoy P. P., Valuation-based systems for Bayesian decision analysis, Oper. Res. 40 (1992) 463-484.

[13] Shenoy P. P., A comparison of graphical techniques for decision analysis, Eur. J. Oper. Res. (1994) in press.

[14] Shafer G., A Mathematical Theory of Evidence (Princeton University, 1976).

[15] Smets Ph., Belief functions, in Ph. Smets, A. Mamdani, D. Dubois and H. Prade, eds. Non Standard Logics for Automated Reasoning (Academic Press, London, 1988) 253–286.

[16] Smets Ph. and Kennes R., The transferable belief model, Artif. Intell. 66 (1994) 191–234.

[17] Smets Ph., The transferable belief model and random sets, Int. J. Intell. Syst. 7 (1992) 37–46.

[18] Smets Ph., Belief functions: the disjunctive rule of combination and the generalized Bayesian theorem, Int. J. Approx. Reasoning 9 (1993) 1–35.

[19] Hurwicz L., A criterion for decision-making under uncertainty, Tech. Rep. 355, Cowles Commission (1952).

[20] Schubert J., Cluster-based specification techniques in Dempster–Shafer theory for an evidential intelligence analysis of multiple target tracks, Ph.D. Dissertation, Department of Numerical Analysis and Computing Science, Royal Institute of Technology, Sweden, 1994.

[21] Shenoy P. P., Valuation-based systems for discrete optimization, in P. P. Bonissone, M. Henrion, L. N. Kanal and J. F. Lemmer, eds. Uncertainty in Artificial Intelligence 6 (North-Holland, Amsterdam, 1991).

[22] Xu H. and Smets Ph., Reasoning in evidential networks with conditional belief function, Int. J. Approx. Reasoning (1995).

[23] Smets Ph., Un modèle mathématico-statistique simulant le processus du diagnostic médical, Doctoral dissertation, Université libre de Bruxelles (1978).

[24] Xu H., Hsia Y-T. and Smets Ph., A belief-function based decision support system, in D. Heckerman and A. Mamdani, eds. Proc. 9th Uncertainty in Artificial Intelligence (San Mateo, CA, Morgan Kaufmann, 1993) 535–542.

![](/api/attachments/D6RQFFXH/fulltext/images/ede0fedc3a621a37cc88761130812a158bc7e0a6deb1701a7834c3941efda7ef.jpg)  
Hong Xu obtained her Bachelor degree of Engineering from Huazhong (University of Science and Technology, Wuhan, China, in 1988, her Master degree in Information Technology from Vrije Universiteit Brussel, Brussels, Belgium, in 1991, and Ph.D. degree in Applied Science from Université Libre de Bruxelles, Brussels, Belgium, in 1995.  
She is currently a research fellow at the IRIDIA, Institut de Recherches Interdisciplinaires et de Développement en Intelligence Artificielle, of Université Libre de Bruxelles. Her research interests include belief function theory and approximate reasoning and decision analysis under uncertainty.
