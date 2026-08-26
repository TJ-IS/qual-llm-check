---
otero_id: 21716
otero_key: "5KUD7EMD"
title: "A probabilistic model for interactive decision-making"
authors: "Pierfrancesco Reverberi; Maurizio Talamo"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00013-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A probabilistic model for interactive decision-making

Pierfrancesco Reverberi <sup>a,)</sup>, Maurizio Talamo <sup>b,1</sup>

<sup>a</sup> Dipartimento di Informatica Sistemi e Produzione, UniÕersita degli Studi di Roma ‘Tor Vergata’, Via di Tor Vergata 110, 00133 Rome, \` Italy

Dipartimento di Informatica e Sistemistica, UniÕersita degli Studi di Roma ‘La Sapienza’, Via Salaria 113, 00198 Rome, Italy \`

Accepted 20 January 1999

## Abstract

A probabilistic reasoning model is defined where the decision maker d.m. is engaged in a sequential information-gather-Ž . ing process facing the trade-off between the reliability of the achieved solution and the associated observation cost. The d.m. is directly involved in the proposed flexible control strategy, which is based on information-theoretic principles. The devised strategy works on a Bayesian belief network that allows the efficient representation and manipulation of the knowledge base relevant to the problem domain. It is shown that this strategy guarantees a constant factor approximate solution with respect to the optimum of the decision problem. Some application examples are also discussed. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Decision-making under uncertainty; Information-gathering strategy; Myopic policy; Interactive solution procedure; Bayesian belief networks

## 1. Introduction

Many decision-making problems are characterized by a large number of interrelated variables on which only incomplete and noisy data are available. In this framework, the a priori specification of goals and preferences by the decision maker d.m. can result in a dominated solution, since he has to make his choices on the basis of aŽ . limited amount of information 8,21 . According to information economics, the most valuable antidote to<sup>w</sup> <sup>x</sup> uncertainty is the acquisition of information 1 . Actually, information-gathering actions produce a two-fold<sup>w</sup> <sup>x</sup> effect. On the one hand, the probability of any feasible event and<sup>r</sup>or combination of events are suitably updated. On the other hand, the d.m.’s beliefs and requirements are reconsidered and possibly changed.

A number of relevant contributions have been produced in diverse research areas such as artificial intelligence, information theory, decision theory, operations research and game theory. In particular, Moore and Whinston 11,12 developed a formal model of decision-making under uncertainty in which sequential <sup>w</sup> <sup>x</sup> information acquisition plays a crucial role. However, a fairly complete solution of the model is defined only in special cases where there are up to three possible outcomes for each information-gathering action. Later on, Jacob et al. 5 recognized the potential for embedding interactive reasoning processes within the model. Given<sup>w</sup> <sup>x</sup> the inherent capabilities of the human such as expertise, versatility and creativity and the computer such asŽ . Ž accuracy, memory capacity and processing speed , an integrated human. <sup>r</sup>computer information processor is shown to be able to merge their skills in order to solve decision problems more efficiently and effectively. Recently, Sarkar and Ghosh 17 presented a theoretical framework for a probabilistic reasoning model that uses<sup>w</sup> <sup>x</sup> the well-known Bayes rule to update beliefs about events according to new pieces of information. However, independence relationships among variables are not endogenously derived in their model. Moreover, although the model shows a good deal of flexibility, it is not fully interactive in nature, since the d.m. is not allowed to play an active role in the decision process.

The purpose of this paper is to develop a probabilistic decision-making model that allows the d.m. to make reliable inferences at a reasonable cost, in terms of both time and budget. The proposed model addresses the following issues. First, the model explicitly considers the opportunity to gather information in order to reduce the uncertainty associated with the final decision at the expense of additional costs. Actually, the d.m. is supposed to be engaged in a sequential reasoning process facing the trade-off between the reliability of the achieved solution and the associated observation cost. Second, the model formalizes human<sup>r</sup>computer interactions; namely, the model allows for a flexible control strategy in which the human is directly involved. Third, the model adopts a Bayesian belief network to structure and manage the decision problem, that is, to organize the knowledge base and perform the inference process. The compact representation provided by such a network gives a probabilistic description of the problem, where the involved variables may take any finite number of values. Moreover, the network is a natural device for both encoding and deriving complex conditional independence relations in the problem domain.

The main results achieved in this paper can be listed as follows. First, we define an information-gathering strategy that sequentially selects the most predictive source about the final outcome relative to its cost, namely, the source that gives the most probable system configuration that is consistent with the currently available information. It is implicitly assumed that either any assignment of monetary values to all benefits and losses associated with making a decision is arbitrary or the d.m. is unable to derive precise and reliable payoff estimates, as does happen in various applications 7 . Since the proposed selection rule is based on information theoretic principles, such a rule carries the advantage of not depending on the aforementioned inherently subjective estimates.

Second, we introduce an algorithm to implement the devised strategy in an efficient way. This algorithm makes it easy to formulate and evaluate sensitivity questions, such as the value of information or control. Furthermore, it allows the d.m. to be directly involved in the solution process by influencing the evaluation phase. Since it works on a Bayesian network, it can result in considerable gains in efficiency with respect to the usual decision tree evaluation procedures. In fact, it can take advantage of the displayed conditional independence relationships among problem variables which determine significant reductions in processing time and memory requirements. In particular, when the network is singly connected, polynomial time is required in order to reach the final solution 14,18 .

Third, we show that the strategy guarantees a constant factor approximate solution with respect to the optimum of the decision problem. Recall that the information-gathering process is ruled that is, both guided andŽ halted primarily on the basis of the d.m.’s preferences. In addition, the d.m.’s preferences may be revised as the. process itself is developed. In this framework, a myopic policy that is greedy in nature i.e., looks only one step Ž ahead by evaluating information sources one at a time is the best strategy the d.m. can follow in order to. control observation costs. On the other hand, non-interactive optimization models carry out an off-line search for the final solution. Hence, they may result either in a significant waste of both computational and financial resources or even in an infeasible solution. Note that the optimal solution could be achieved only by an ideal model that is available to an oracle who knows a priori the d.m.’s a posteriori requirements so that these can be explicitly taken into account.

This paper is organized as follows. Section 2 presents the decision-making model. In Section 3, the decision problem is formulated through a pair of alternative optimization programs that in turn are interpreted in terms of two-player games. An interactive myopic policy is devised in Section 4. Some application examples are illustrated in Section 5. Section 6 includes concluding remarks and directions for future work. Appendix A reports a listing of the mathematical notation, while Appendix B contains the formal proofs of the theoretical results achieved throughout the paper.

## 2. The decision model

The proposed decision-making model $M \equiv \langle X , f , C ( \cdot ) , \mathrm { { P r } ( \cdot ) , } D ( \cdot ) \rangle$ consists of the following five-tuple of elements.

<sup>.</sup> X is a finite set of variables, taking a finite number of values in the domain $R _ { ( X ) } .$

<sup>.</sup> f is the input data vector, including the values taken by variables in $F \subset X$ , that is the subset of variables that are observed by the d.m. at no cost e.g., some symptoms complained of by a patient to his physician .Ž . $C ( \cdot ) { : ( X \setminus F )  Z ^ { + } }$ is an upper-bounded linear and separable function, computing the total cost of observing variables not included in F Žnote that the upper-bound is simply determined by summing together the observation costs of all such variables ..

$\operatorname* { P r } ( . ) { : } \langle f , a , R _ { ( X ) } \rangle  [ 0 , 1 ]$ is a function that computes the probability of each possible combination of values for variables in X, where a is the vector of values taken by variables selected for observation, that is, included in $A \subset X$

$D ( \cdot ) \colon \langle f , a , C ( \cdot ) , \operatorname* { P r } ( \cdot ) \rangle  \{ 0 , 1 \}$ is a mapping that assesses the feasibility of any decision d about variables to be included in subset A, where d is feasible infeasible if and only ifŽ . $D ( \cdot ) = 1 \ \left( D ( \cdot ) = 0 \right)$

Let us now introduce the following definitions.

Definition 1. An explanation x is an assignment of values to all variables in X that is consistent with the values taken by those variables included in the whole evidence set $E = \left( F \cup A \right) \subset X$ . The best explanation $x ^ { * }$ is the most probable of such assignments.I

Thus, an explanation can be seen as a composite vector which includes the fixed subvector of values takenŽ . by observed variables and one of the possible subvectors of values taken by all remaining variables in $X \setminus E .$ It follows that the best explanation is the most probable combination of values for variables in $X \setminus E$ given the evidence at hand such a combination is determined according to the algorithm explained in SectionŽ $4 ;$ see also the examples given in Section 5 ..

Definition 2. The $\mathrm { { d . m . } \gamma _ { s } }$ a priori a posteriori minimum required confidence level about a certain event,Ž . denoted by Ž . Ž . , represents the prior posterior probability threshold level beyond which the d.m. is trustful enough about the occurrence of that event.I

Definition 3. A feasible set of decisions includes any decision d such that, given $f ,$ observing a produces $D ( \cdot ) = 1 .$ Ž . . This happens when the following conditions are satisfied: i the observation cost of A does not exceed $\overline { B }$ Ž . Ž . the d.m.’s available budget ; ii the probability of the best explanation of e is at least ${ \overline { { \alpha } } } ,$ , where e is the vector of values taken by variables in E.I

The d.m. searches for an optimal decision among those included in the feasible set, as defined by functional DŽ .<sup>P</sup> . It is worth noting that the set of feasible decisions is defined according to the actual values taken by the observed variables and their observation costs as well as the d.m.’s available budget and minimum required confidence level about the solution. All these elements characterize model M. It is possible to state the decision problem in the following terms.

Decision Problem DP( ). Given X and f , find a subset $A \subset X$ such that the d.m.’s a posteriori confidence level about the best explanation derived from $e = f \cup a$ is at least , while C AŽ . is the lowest possible.I

It is assumed that information-gathering actions can be performed only by incurring positive costs. The aim of the d.m. is to determine a low-cost subset of evidence variables that allow deriving an explanation which meets the specified reliability requirement. Keeping this subset of variables under control makes the d.m. feel confident about the state of the whole system. This approach is particularly suitable for diagnostic problems, where the focus is on relating the observed manifestations to the most probable underlying causes, whatever the nature of the investigated system. In this framework, it is assumed that the simplest explanation is the one which requires the minimal-cost evidence set while satisfying the reliability requirement . This recalls the well-knownŽ . Principle of Parsimony or Ockham’s Razor, stating that the simplest explanation is the preferable one see, e.g., Ž Ref. 15 . However, a cost-effectiveness approach has sometimes also been adopted in order to deal with<sup>w</sup> <sup>x</sup>. competitive environments. According to the transaction costs theory, the optimal entry strategy of a firm into a foreign market is determined by the cost minimization criterion, that reduces the risks of making decisions on the basis of a limited amount of both experience and information about market characteristics see, e.g., Ref.Ž <sup>w</sup> <sup>x</sup> 3 . It directly follows that information-gathering activities are closely linked with a firm’s investment decision. <sup>w</sup> <sup>x</sup> <sup>2</sup> in a new market 2,9 .

It is worth noting the following issues. First, the costs of collecting different pieces of information can be assessed even in the case when benefits and losses associated with possible decisions cannot be reliably evaluated in monetary terms. Second, different information sources may require significantly different observation costs. For instance, as remarked by Sarkar and Ghosh 17 , ‘‘performing a site visit to ensure that a vendor<sup>w</sup> <sup>x</sup> has adequate production facilities is much more time consuming and expensive than obtaining references by phone from prior customers of the vendor’’. Third, it may be the case that not all variables in X are observable in practice. According to model M, this can be formalized simply by associating to such variables an observation cost that exceeds the available budget ${ \overline { { B } } } .$

At this point, it is essential to remark that the d.m.’s a posteriori minimum required confidence level  about the best explanation cannot be known in advance to anyone but an omniscient oracle. Hence, off-line decision models necessarily use a proxy, given by an a priori value which depends on the initial d.m.’s viewpoint. Nevertheless, the d.m. can revise his judgements during the course of the solution process because he may feel more or less confident about the currently achieved explanation according to observed data. The significant implications of this fact will be discussed in detail in the following sections. In what follows, it is assumed that when E coincides with X, the d.m.’s a priori and a posteriori confidence levels about the best explanation are both equal to unity. In other words, the d.m. trusts that the system is able to produce a correct explanation of the evidence set in the deterministic case when all problem variables are observed.

## 3. Problem formulation

Depending on the context, the decision problem can be formulated by a pair of alternative optimization models, that can in turn be interpreted in terms of corresponding two-player games. On the one hand, probabilistic reasoning is performed by the d.m. e.g., identified as the first player with reference to anŽ . adversary that is the second player who is allowed to take an active part in the inference process for instance,Ž . Ž think of a potential entrant firm that aims at evaluating the profitability of a given market depending on the unknown nature of an established firm that currently enjoys a dominant position: see Ref. 2,10 . In this<sup>w</sup> <sup>x</sup>.

framework, a bilevel programming BP model can be used to express the conflicting goals of the two oppositeŽ . players within the competitive structure of a Leader–Follower Stackelberg game Ž Ž . . Case a below . On the other hand, the decision process is carried out with respect to an investigated system that is ruled solely by the case Ž . as in the usual circuit fault analysis or medical diagnosis . Thus, the adversary of the d.m. is supposed to be neutral, so that a simple integer programming IP model is suitable to build the structure of a game againstŽ . nature Ž Ž . .Case b below .

## 3.1. Case a : bile ( ) Õel programminglStackelberg game

When the d.m. faces a hostile adversary, it is necessary to solve the decision problem by a bilevel programming BP optimization model. In this framework, Leader that is, the first player, or the d.m. makesŽ . Ž . his decisions first while taking into account the reactions of his opponent, Follower the second player , who is Ž . allowed to act for his best only in light of the decisions made by the former. Formally, this can be expressed as follows:

$$
\underset {X} {\operatorname{MIN}} C (E) = \sum_ {i = 1} ^ {n} C \left(X _ {i}\right) e _ {i}\tag{1}
$$

$$
\operatorname * {P r} (x ^ {*} | e) \geq \alpha\tag{2}
$$

$$
\underset {e} {\text { MIN }} \left[ \operatorname * {P r} (x ^ {*} | E) \right]\tag{3}
$$

$$
C (E) = \sum_ {i = 1} ^ {n} C (X _ {i}) e _ {i} \geq \overline {{B}}\tag{4}
$$

$$
| F | <   | E | <   | X |\tag{5}
$$

$$
e _ {i} = \left\{ \begin{array}{l l} 0 & \quad \text { if } X _ {i} \text { is   not   observed } \\ 1 & \quad \text { if } X _ {i} \text { is   observed } \end{array} \right.\tag{6}
$$

Upper-level function 1 Leader’s problem requires that the cost of the evidence set be minimized. NoteŽ . Ž . that minimizing the observation cost of E is the same as minimizing the observation cost of A, since $E = F \cup A$ and F is available at no cost. Lower-level function 3 Follower’s problem aims at minimizing the probabilityŽ . Ž . of the best explanation of the values taken by observed variables. It is worth specifying that E denotes the set of variables selected for observation by Leader, while e denotes the vector of their actual values as replied by Follower. Constraint 2 restricts the feasible range of Follower’s problem objective function, since theŽ . probability of the best explanation $x ^ { * }$ of observed values e cannot fall below a fixed threshold. In other words, Leader carries on his information-gathering process until his a priori minimum required confidence level is reached provided that he has budget available . Thus, Leader pursues the minimization of observation costs toŽ . the extent that he is confident enough about the true nature of his adversary. Constraint 4 restricts the range ofŽ . feasible choices that are available to Leader, due to the role played by his adversary in the inference process. In fact, the uncertainty related to Follower’s nature and<sup>r</sup>or strategy is such that Leader has to spend at least a certain amount of money B in his search for a satisfactory solution. In the worst case, Leader has to spend all his budget B. Note, however, that Leader cannot spend more than $\overline { B }$ since such a solution would be infeasible. The purpose of constraint 5 is to exclude the borderline situations in which either no variable is acquired asŽ . evidence so thatŽ $\left| E \right| = \left| F \right| )$ or, in the opposite case, every variable in the domain is included in the evidence set Žso that $| E | = | X | )$ . In such cases, the decision problem is not worth analysing because of the absence of the trade-off between observation cost and confidence level that characterizes Leader’s strategy. Thus, the attention is focused on the interesting cases where Leader has to observe at least one variable but, at the same time, cannot observe all variables in order to reach his a priori minimum required confidence level about

Follower’s nature. Constraint 6 definesŽ . $e _ { i }$ as a binary variable that takes value 1 when $X _ { i } \in X$ is selected for observation and 0 otherwise $( \mathrm { i . e . , ~ } e _ { i } = 0$ when $X _ { i }$ .is not included in the evidence set .

## 3.2. Case b : integer programming ( ) lgame against nature

When it is assumed that the adversary of the d.m. is neutral, it follows that:

Ž .i the decision problem can be formulated in terms of a simple integer programming IP model, defined by Ž . function 1 and constraints 2 , 5 and 6 ;Ž . Ž . Ž . Ž .

Ž . ii the actual values taken by those variables selected for observation depend only on the probability distributions over the discrete and finite set of their possible values;

Ž . Ž . iii a kind of expectation–maximization exp–max solution procedure can replace the common minimization–maximization min–max Ž . strategy used in competitive games;

Ž . iv the d.m. can find the final solution by spending only a fraction of his budget.

Actually, stating that the d.m.’s adversary is neutral is the same as stating that the decision process is carried out with respect to an investigated system that is ruled solely by the case as in the usual circuit fault analysis or Ž medical diagnosis . Since no particular goal can be attributed to such a system, point i highlights that the. Ž . decision problem can be formulated while ignoring those conditions in the Case a model which are related toŽ . Follower—namely, function 3 and constraint 4 . This means that Follower cannot take an active part in theŽ . Ž . inference process, that is, he cannot force an investigated variable to take some specific value. Thus, the actual value taken by any variable is ruled only by the probability distribution defined over its domain point ii .Ž . Hence, Leader chooses variables to be observed according to the expected amount of information they can provide point iii: note that the proposed solution procedure will be explained in detail in Section 4 . The aboveŽ . considerations also imply that the d.m. is provided the opportunity to achieve the final solution and still save part of his budget point iv .Ž .

Despite the apparent simplicity of the above formulations, off-line optimization models suffer from some major flaws. First, within the assumed framework the very feasibility of the final solution to DP strictly depends on the d.m.’s requirements. However, when using off-line optimization, the d.m. can only wait during the solution process since he is not provided with any possibility to cooperate with the problem-solving system and tune it according to the real problem instance and the behaviour of the solution algorithm. This may cause incongruences or waste of resources, since the d.m.’s a posteriori minimum required confidence level about the final solution cannot be explicitly taken into account a priori, that is, when off-line optimization models are set on the basis of level . In fact, such a level may be revised depending on observed data. When these are controversial and do not precisely depict the reference environment, the d.m. is still uncertain about the best action to make even when level has been reached. Otherwise, at level the situation can be so clearly represented that some information becomes redundant and the corresponding observation cost could have been saved by the d.m.

Second, the computational complexity of off-line optimization approaches may be prohibitive, particularly for bilevel programming problems 4 . Things get even worse when the investigated system is non-deterministic. Actually, deterministic systems can be analysed using set covering or other similar techniques 15 . In this<sup>w</sup> <sup>x</sup> framework, the notion of minimality helps limit the search to explanations that are not subsumed by others. As remarked in Ref. 14 , when the system is non-deterministic the minimality criterion is no longer helpful because it is often possible to improve the accuracy of the best explanation by acquiring a larger evidence set, the reliability of the solution being a matter of degree. Models taking into account probabilistic information and uncertainty about system behavior require hard computations to find the most likely solution. In fact, such models commonly use a branch and bound algorithm which often runs in exponential time and overlooks structural properties of the investigated system that could make the solution search significantly faster see, e.g.,Ž Ref. 15 . In Section 4, a flexible heuristic algorithm is developed that achieves an acceptable solution at a <sup>w</sup> <sup>x</sup>. reasonable cost, not necessarily pursuing optimality. One of the most striking features of this algorithm is the inclusion of the human d.m. in the inference process.

## 4. The interactive solution search strategy

Generally speaking, a solution search strategy for DP has to produce an acceptable explanation at a reasonable cost for the d.m. In this paper, it is shown that the efficiency of the problem-solving system is improved by incorporating the human in the solution procedure. In fact, an interactive approach allows the d.m. to follow a learning process about the investigated environment and takes into account the progressive definition of his preferences along with the exploration of the solution space. Based on his expertise, the d.m. can guide the solution procedure through the direct manipulation and calibration of a small set of basic parameters. Moreover, he can revise previous responses based on currently available information.

Given the inherent capabilities of the human such as expertise, versatility and creativity and the computerŽ . Ž . such as accuracy, memory capacity and processing speed , an integrated human<sup>r</sup>computer information processor is often able to merge their skills in order to solve decision problems more efficiently and effectively <sup>w</sup> <sup>x</sup> 5 . Actually, it is shown by the following propositions that these features imply that in our case the d.m. reduces the cost of DP-solving by interacting with the problem-solving system.

Proposition 1. One of the following cases is satisfied for the evidence set $E ^ { * }$ , identified as the optimal solution Ž . of model IP: i $E ^ { * }$ Ž . is infeasible for the decision problem DP; ii $E ^ { * }$ is feasible, but its cost is arbitrarily larger than the cost of a DP optimal solution.

## Proof: See Appendix B.I

## Proposition 2. The same as Proposition 1, with BP replacing IP.I

The proposed interactive solution strategy is relatively easy to use, requires little response from the d.m. and still relies on the d.m. for the search procedure and the choice of a satisfactory solution. Such a strategy consists in scheduling the selection of variables according to a sequential myopic policy that incrementally builds the evidence set. Based on the available budget, at a given iteration the d.m. selects the most promising feasible variable, observes its value, evaluates its impact over the related variables and modifies his own beliefs and requirements. Then, the d.m. chooses whether to perform another information-gathering action and observe the most promising variable in $X \setminus E$ or else make a final decision $d ,$ on the basis of the currently available information. In the former case, he obtains a more accurate prediction of the true explanation at the expense of additional costs, while in the latter case he stops his search.

When reliable payoff estimates are not available or cannot even be obtained, arbitrariness and subjectiveness are inherent in decision theoretic models for selecting information sources. Then, it is suitable to follow information theoretic principles. In this framework, one of the most commonly used selection rules is based on the entropy function HŽ . <sup>P w</sup> <sup>x</sup> 19 . According to this function, the uncertainty regarding any target variable T that is characterized by the probability distribution PrŽ .t can be represented by the expression $\begin{array} { r } { H ( T ) = - \sum _ { t } \mathbf { P r } ( t ) \times } \end{array}$ log PrŽ . Ž t for discrete variables, the entropy function is the highest when all values are equally likely and zero when one value is known to be true with certainty . It follows that the residual uncertainty about the true value. of the target variable T, given that a variable $X _ { i }$ that is somewhat related to $T$ is instantiated to $x _ { i } .$ , can be written as $\begin{array} { r } { H ( T | x _ { i } ) = - \sum _ { t } \mathrm { P r } ( t | x _ { i } ) \times \log \mathrm { P r } ( t | x _ { i } ) } \end{array}$ . Then, the average residual uncertainty about $T _ { \ast }$ , summed over all possible values $x _ { i }$ of $X _ { i } ,$ is given by $\begin{array} { r } { H ( T | \dot { X } _ { i } ) = \sum _ { x _ { i } } H ( T | x _ { i } ) \times \operatorname* { P r } ( x _ { i } ) = - \sum _ { x _ { i } } \Sigma _ { t } \operatorname* { P r } ( t , x _ { i } ) \times \log \operatorname* { P r } ( t | x _ { i } ) } \end{array}$ . If we subtract $H ( T | X _ { i } )$ from the level of uncertainty about T prior to observing $X _ { i } ,$ Ž . , namely H T , we obtain the uncertainty-reducing potential of $X _ { i }$

This potential is called mutual information and is given by $\begin{array} { r } { I ( T , X _ { i } ) = H ( T ) - H ( T | X _ { i } ) = - \sum _ { x , \Sigma _ { t } } \mathrm { P r } ( t , x _ { i } ) \times } \end{array}$ $\mathrm { l o g } [ \mathrm { P r } ( t , x _ { i } ) / ( \mathrm { P r } ( t ) \mathrm { P r } ( x _ { i } ) ) ]$ . Note that $I ( T , X _ { i } )$ Ž .is a non-negative quantity that is bounded above by H T and is equal to zero if and only if $T$ and $X _ { i }$ are mutually independent, that is, $X _ { i }$ does not convey any information about T. Based on the foregoing statements, the variable to be selected for observation is the one that results, on average, in the greatest decrease in the entropy function, namely, in the highest value of the mutual information.

Although the entropy function shows desirable properties, it is not free from some weaknesses see Ref.Ž <sup>w</sup> <sup>x</sup> 14 . In particular, an entropy-based selection rule does not reflect ordering or scale information relative to the. values that any variable may take. As a result, scheduling the information acquisition activities based on the mutual information measure may occasionally require spending precious resources to perform irrelevant tests, while neglecting more informative ones. Thus, the mutual information selection rule is inappropriate for practical decision-making, on the ground that it does not indicate which questions will provide the most relevant information. Furthermore, the practical use of such a rule has been limited to reducing the uncertainty associated with a single target variable 6 .<sup>w</sup> <sup>x</sup>

In this paper, we propose an alternative probabilistic rule that reflects more closely the risks of acting under incomplete information by assuming a system-oriented perspective. Actually, this rule requires the d.m. to choose the most discriminating information source among the set of possible overall system configurations given the currently available information. In order to economize on data collection, at each iteration the d.m. would like to observe the feasible variable which maximizes the probability of the best explanation of the updated evidence set, relative to the observation cost of the variable at issue. Nevertheless, the actual values of the candidate variables for observation and thus their real contribution to the probability of the bestŽ explanation are not known in advance to the d.m. Thus, he has to select the most promising variable in terms of. the highest average ratio between the probability of the best explanation computed for all possible values ofŽ each variable relative to the observation cost of the variable. If more than one variable satisfy the above. criterion, the d.m. can select any of them.

The solution strategy has to be practically implemented by means of a computational tool which allows to evaluate function PrŽ . Ž .<sup>P</sup> in model M see Section 2 . In this work, a Bayesian belief network $G = \left( X , L \right)$ is used to structure and manage the decision problem at hand by specifying through the elements in L a set of mutual relationships between the variables in X. Now, it is worth introducing the following definitions.

Definition 4. A directed graph G<sup>s</sup>Ž . X, L is a structure which consists of a finite non-empty set of nodes X and a finite non-empty set of arcs L. Each arc is incident to the elements of an ordered pair of distinct nodes which are called its endpoints Žin particular, the first endpoint is said to be the start-node of the arc and the second is said to be its end-node..I

Definition 5. A directed path is a sequence of arcs such that the end node of any arc in the sequence is the start node of its consecutive arc in the sequence. A directed path is a directed cycle if the start node of the path is the same as its end node. A directed graph is acyclic if it does not contain any directed cycle.I

Definition 6. A Bayesian belief network is a directed acyclic graph in which the nodes represent discrete random variables that take on a finite number of possible values and the arcs signify the existence of direct causal influences between the linked variables.I

In a Bayesian belief network, the strengths of direct causal influences between subsets of variables are quantified by conditional probability matrices which report judgmental estimates relative to the occurrence of the different values of any node, given any value combination of their parents. The conjunction of such local estimates forms a complete and consistent global model associated with a joint distribution function over the variables, which allows any probabilistic query in the domain to be answered.

These features are particularly important when dealing with the problem of assembling the most probable explanation of the evidence set the so-calledŽ .belief reÕision procedure . In pure form, this optimization task is intractable, because enumerating and rating all possible explanations is prohibitive. However, the independence relationships among variables embodied in a Bayesian network make it possible to carry out local inference mechanisms and exploit a distributed computation paradigm which gains a considerable reduction in complexity through subtask decomposition. Similar mechanisms also allow updating the probability distribution of each variable every time a new piece of information is added to the evidence set at a constant cost Ž . belief updating . It has been shown that both belief reÕision and belief updating procedures run in polynomial time O nŽ .—that is, linear in the number of variables—in singly connected networks, where no more than one path exists between any two nodes see Ref. 14 , where the theoretical and computational features of Bayesian beliefŽ <sup>w</sup> <sup>x</sup> networks are discussed exhaustively ..

On the basis of the foregoing statements, a pair of heuristic algorithms can be devised for DP-solving, corresponding to the alternative problem formulations given in Section 3. Both algorithms possess the same structure, but they differ for some working rules such as node selection and stopping criterion . LetŽ . $\begin{array} { r } { \overline { { \operatorname* { P r } } } _ { i } ( x ^ { * } | e \cup X _ { i } ) = \sum _ { x , [ \operatorname* { P r } } ( x ^ { * } | e \cup x _ { i } ) \operatorname* { P r } ( x _ { i } ) ] . } \end{array}$ . In the game-against-nature case, the proposed algorithm consists of the following steps.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm I
(0) Initialize  $G = (X, L)$ , E = F,  $A = \varnothing$ ,  $C(X_i) \forall X_i \in X$ ,  $B = \text{MAX}_X C(X_i)$ ,  $\overline{B}$ ,  $\overline{\alpha}$ , k &gt; 1 ( $k \in R$ )
While  $(\Pr(\boldsymbol{x}^*|\boldsymbol{e}) &lt; \overline{\alpha})$  AND  $(B &lt; \overline{B})$  AND  $(E \subset X)$  do
(1) Select  $X_i \in X$  such that  $\overline{\Pr}_{i}(\boldsymbol{x}^*|\boldsymbol{e} \cup X_i)/C(X_i)$  is maximized
While  $(C(E \cup X_i) &gt; B)$  do
Set  $X = X \setminus X_i$ 
End While
(2) If  $(C(E \cup X_i) \leq B)$  Then do
Set  $E = X_i \cup E$ 
Compute  $\Pr(\boldsymbol{x}^*|\boldsymbol{e})$ 
Revise  $\overline{\alpha}$ 
Update  $\Pr(X_i = x_i)$ ,  $\forall x_i \in R_{X_i}$ ,  $\forall X_i \in X$ 
(3) Else do
Set  $(B = kB)$  AND E = F
End While
</div>

In short, Algorithm I can be interpreted as a policy intended primarily to control observation costs. The main goal of the algorithm is to achieve the minimum required probability of the best explanation while limiting the evidence set cost by imposing a certain upper bound B. Such a bound is successively relaxed by a given Ž constant $k )$ so long as the d.m. is not satisfied and the total available budget amount $\overline { B }$ is not overcome. The rationale for Algorithm I can be derived from Propositions 1 and 2, stating that an arbitrarily small increase in the minimum required confidence level may result in an arbitrarily large increase in the total observation cost. These propositions also imply that the algorithm is particularly effective when the observation cost of a single variable is low with respect to the whole evidence set. Algorithm I makes use of Pearl’s probability propagation methods on Bayesian networks 14 to arrange the nodes in a sorted list according to the information they <sup>w</sup> <sup>x</sup> provide to discriminate among competing explanations of the evidence set. Therefore, the d.m. can benefit from an effective support in making the choices that characterize his sequential information-gathering process. 3

Let us now analyse in detail each step of the procedure. Step 0 initializes the algorithm. Since E coincides with the possibly empty set of free evidence nodesŽ . F and A is the empty set of acquired evidence nodes, no observation costs are imposed on the d.m. In this step, the observation cost of each single node $C ( X _ { i } )$ is specified, together with the d.m.’s total available budget amount B and threshold confidence level $\overline { { \alpha } } .$ . Note that a current budget constraint B is also fixed so that the most promising node of the network is invariably selected.

Step 1 includes the key-point of the procedure, that is the choice of the candidate node for observation. This choice is made by the d.m. based on the node selection rule that has been discussed previously.

Once the d.m. has selected a candidate node for observation, he has to check if the total incurred cost overcomes the current budget constraint. In such a case, the node is discarded and less informative nodes are successively considered. If no node can be observed, then the current budget constraint is multiplied by a given constant $k > 1$ and the solution procedure restarts Ž . step 3 . Otherwise, step 2 requires first observing $X _ { i }$ and then updating the probability of the best explanation according to the value of the selected node. Then, the d.m. is allowed to revise his preferences. Thus, the reliability level required for the final solution is no longer fixed a priori, but may change a posteriori depending on the state and evolution of the solution process. This step also requires propagating the impact of the new piece of evidence to the probability distributions of all network variables.

Steps 1, 2 and 3 are reiterated so long as the following three conditions hold:

Ž .a the probability of the best explanation lies below the current d.m.’s a posteriori minimum required confidence level;

Ž . b the current budget constraint is compatible with the total available budget amount;

Ž .c there is at least one observable variable left.

These conditions act as alternative stopping rules. Thus, when any of them is no longer satisfied the algorithm stops and the achieved solution may not or cannot be improved. Ž .

Let us now consider the computational complexity of the proposed solution procedure. Algorithm I requires that all pending information sources be compared at each iteration on the basis of the probability of the best explanation associated with each of their possible values. At iteration $r + 1$ , there are $( n - r )$ Ž . pending nonfree sources left. If V is the maximum discrete and finite number of values that any variable of the network mayŽ . take, then the probability of the best explanation must be determined $V ( n - r )$ times. It has been noted previously that each computation of this kind requires $O ( n )$ time. In addition, when a new piece of evidence is collected that is, the most promising variable has been selected and its value observed , the probabilityŽ . distributions of all variables must be modified according to the belief updating procedure. It has been noted previously that this procedure also requires $O ( n )$ time. As a consequence, a single iteration of the algorithm requires $\left[ V ( n - r ) O ( n ) + O ( n ) \right]$ time, that can be stated as $O ( V n ^ { 2 } )$ . Now, recall that at the first iteration of Algorithm I the available budget for variable observation is fixed at level B. In the next steps of the algorithm, this level is successively multiplied by a given constant k. This is possible until the total available budget amount $\overline { B }$ is reached. It follows that the maximum possible number of algorithm iterations is given by <sup>w</sup>log $_ k ( { \overline { { B } } } / B ) + 1 ]$ for simplicity, it is assumed here thatŽ k, B and B are fixed so that such an expression gives an integer number . Then, the worst case overall complexity of Algorithm I is equal to. $O ( V n ^ { 2 } ) [ \log _ { k } ( \overline { { B } } / B ) + 1 ]$

Let $C _ { \mathrm { I } }$ be the cost of the solution given by Algorithm I and $C ^ { * }$ the cost of the optimal solution of $D P ;$ , for a given problem instance.

Proposition 3. For any given problem instance, if there exists an integer h, $0 \leq h \leq \left[ \log _ { k } ( \overline { { B } } / B ) + 1 \right]$ such that Algorithm I stops at iteration h, the following condition holds:

$$
C _ {\mathrm{I}} / C ^ {*} \leq \frac {k ^ {2}}{k - 1}.
$$

Proof: See Appendix B.I

Recall that $C ^ { * }$ can be obtained only by an oracle who anticipates a priori the correct $\overline { { \alpha } } .$ . Thus, it should not be mistaken for the observation cost given by any off-line optimization model. In fact, Propositions 1 to 3 imply that such models cannot even guarantee as good an approximation factor as Algorithm I.

## 5. Application examples

In this section, we illustrate a pair of application examples which show how Algorithm I works in practice: the first example addresses a simple circuit fault diagnosis problem, while the second one concerns market entry decision.

## 5.1. Circuit analysis

Let us consider the Bayesian belief network shown in Fig. 1b, representing the simple logic circuit in Fig. 1a. This consists of three AND-gates in tandem that relate binary input variables $X _ { i } ~ ( i = 1 , 2 , 3 )$ to intermediate unobserved variables $Y _ { i } = Y _ { i - 1 } \wedge X _ { i } \ ( i = 1 , 2 )$ as well as the circuit’s input $Y _ { 0 }$ and output $Y _ { 3 }$ . The circuit is assumed to be operational that is,Ž $Y _ { 0 } = 1 )$ . Moreover, node $Y _ { 3 }$ is permanently observed at zero cost. If $Y _ { 3 } = X _ { 1 } \wedge X _ { 2 } \wedge X _ { 3 } = 1$ , the overall state of the circuit is automatically determined, since all components must be functioning normal operation state . Otherwise, if a failure occurs that is,Ž . Ž $Y _ { 3 } = 0 )$ , any subset of inputs might be faulty. Let $Y _ { 3 } = 0$ . The problem is to identify the set of faulty components, given that input variables’ failures are assumed to be independent events with prior probabilities $q _ { i } = 1 - p _ { i } = \operatorname* { P r } ( X _ { i } = 0 ) , i = 1 , 2 , 3$ , and the conditional probability matrices that characterize child–parent relationships are $\operatorname* { P r } \left( \left. y _ { i } \right| y _ { i - 1 } , \boldsymbol { x } _ { i } \right) =$ $\begin{array} { r l r } { \int 1 } & { { } } & { \mathrm { i f } ~ y _ { i } = y _ { i - 1 } \wedge x _ { i } } \end{array}$ .Thus, the output of each component $( \mathrm { i . e . }$ , a child node is functionally determined by  . ½ <sub>0</sub> otherwise the state of its two inputs i.e., the parent nodes .Ž .

This example is taken from Ref. 14 . However, it is worth noting that in Pearl’s work circuit analysis is<sup>w</sup> <sup>x</sup> introduced in order to illustrate the nature and the mechanisms of the probability propagation schemes in Bayesian networks, given a fixed evidence set. On the other hand, in this paper the same example is extended in order to include the information acquisition issue, that is, to show how a d.m. can use the proposed information gathering strategy in order to build an evidence set that is convenient to his aims. In particular, we adopt Algorithm I to limit as much as possible the evidence set cost, while assessing the most probable state of all components so that the $\mathrm { { d . m . } } \ ' _ { s }$ minimum required confidence level about the overall state of the circuit is reached. Note that the only relevant case for the analysis occurs when $Y _ { 3 } = 0$ , while the candidate nodes for observation are $\left\{ X _ { i } \colon i = 1 , 2 , 3 \right\}$ , since they automatically determine the values of the others.

Algorithm I is initialized by setting $E = F = \{ Y _ { 0 } = 1 , Y _ { 3 } = 0 \} , A = \emptyset , C ( X _ { i } ) = 1 0 0 \forall i , B = 1 0 0 , \overline { { B } } = 2 0 0 ,$ $\overline { { \alpha } } = 0 . 9 , k = 2$ . In order to select the most informative variable, it is essential to compute the probability of the best explanation associated with each possible value of every candidate variable for observation. The problem size is small enough to allow the global computation of such probabilities, based on the network structure and the well-known Bayes’ formula $\operatorname* { P r } ( x ^ { * } | e ) = [ \operatorname* { P r } ( e | x ^ { * } ) \operatorname* { P r } ( x ^ { * } ) ] / \operatorname* { P r } ( e )$ . Note that larger size problems would Ž <sup>w</sup> <sup>x</sup>. <sup>4</sup> require using the distributed computation scheme outlined in Section 4 see Ref. 14 . It is assumed for simplicity that $1 / 2 > q _ { 1 } > q _ { 2 } > q _ { 3 }$ . Then, the explanations corresponding to the bold-face typed probabilities in Tables 1–3 are the best ones with respect to the considered values of the candidate evidence nodes. In particular, if the prior probabilities are set at $( p _ { 1 } = 0 . 8 ; q _ { 1 } = 0 . 2 ) , ( p _ { 2 } = 0 . 8 5 ; q _ { 2 } = 0 . 1 5 ) , ( p _ { 3 } = 0 . 9 ; q _ { 3 } = 0 . 1 )$ then the probabilities of the best explanations of $\{ ( X _ { i } \colon i = 1 , 2 , 3 ) \cup ( Y _ { 0 } = 1 , Y _ { 3 } = 0 ) \}$ , averaged over the possible values of $X _ { i } ,$ can be expressed as:

$$
\overline {{{{\operatorname * {P r}}}}} \left(X _ {1}\right) = 0. 7 6 5 \times 0. 2 0 0 + 0. 5 7 4 \times 0. 8 0 0 = 0. 6 1 2
$$

$$
\overline {{{\operatorname * {P r}}}} \left(X _ {2}\right) = 0. 7 2 0 \times 0. 1 5 0 + 0. 6 4 3 \times 0. 8 5 0 = \mathbf {0}. \mathbf {6 5 5}
$$

$$
\overline {{{{\operatorname * {P r}}}}} \left(X _ {3}\right) = 0. 6 8 0 \times 0. 1 0 0 + 0. 5 3 1 \times 0. 9 0 0 = 0. 5 4 6
$$

(a)  
![](/api/attachments/5KUD7EMD/fulltext/images/445fed1f374ab07f8c2c375919d5cb5e68b59b40a59a8236bc8963bd67b6ae97.jpg)

(b)  
![](/api/attachments/5KUD7EMD/fulltext/images/255d478c30ac1c1f46c6f07545a9ffeab008f230dbcf25d1b48cdac6296c65ba.jpg)  
Fig. 1. a A simple logic circuit. b The Bayesian belief network representation of the circuit. Ž . Ž .

Information content of variable $X _ { 1 }$ given the current evidence set

<table><tr><td colspan="5">Explanations</td></tr><tr><td>Observed values</td><td> $\boldsymbol{x}_{1}:\{X_{2}=X_{3}=0\}$ </td><td> $\boldsymbol{x}_{2}:\{X_{2}=1,X_{3}=0\}$ </td><td> $\boldsymbol{x}_{3}:\{X_{2}=0,X_{3}=1\}$ </td><td> $\boldsymbol{x}_{4}:\{X_{2}=X_{3}=1\}$ </td></tr><tr><td> $\boldsymbol{e}_{1}: X_{1}=0, Y_{0}=1, Y_{3}=0$ </td><td> $\Pr(\boldsymbol{x}_{1}|\boldsymbol{e}_{1})=q_{2}q_{3}$ </td><td> $\Pr(\boldsymbol{x}_{2}|\boldsymbol{e}_{1})=p_{2}q_{3}$ </td><td> $\Pr(\boldsymbol{x}_{3}|\boldsymbol{e}_{1})=q_{2}p_{3}$ </td><td> $\Pr(\boldsymbol{x}_{4}|\boldsymbol{e}_{1})=\boldsymbol{p}_{2}\boldsymbol{p}_{3}$ </td></tr><tr><td> $\boldsymbol{e}_{2}: X_{1}=1, Y_{0}=1, Y_{3}=0$ </td><td> $\Pr(\boldsymbol{x}_{1}|\boldsymbol{e}_{2})=q_{2}q_{3}/(1-p_{2}p_{3})$ </td><td> $\Pr(\boldsymbol{x}_{2}|\boldsymbol{e}_{2})=p_{2}q_{3}/(1-p_{2}p_{3})$ </td><td> $\Pr(\boldsymbol{x}_{3}|\boldsymbol{e}_{2})=\boldsymbol{q}_{2}\boldsymbol{p}_{3}/(\boldsymbol{1}-\boldsymbol{p}_{2}\boldsymbol{p}_{3})$ </td><td> $\Pr(\boldsymbol{x}_{4}|\boldsymbol{e}_{2})=0$ </td></tr></table>

Hence, node $X _ { 2 }$ is the candidate for observation note that observation costs can be neglected because theyŽ are the same for all nodes . Since. $C ( X _ { \gamma } ) = B = 1 0 0$ , node $X _ { 2 }$ is actually observed. Suppose $X _ { 2 } = 1$ . Then, it can be derived from Table 2 that $\{ X _ { 1 } = 0 , \ X _ { 2 } = 1 , \ X _ { 3 } = 1 ; Y _ { 0 } = 1 , Y _ { 1 } = 0 , Y _ { 2 } = 0 , Y _ { 3 } = 0 \}$ is the most probable overall state of the circuit, at a probability level equal to 0.643. Moreover, the probability distributions of other candidate nodes for observation are updated according to $X _ { 2 } = 1$ , so that: PrŽ $X _ { 1 } = 0 | e ) = { \pmb q } _ { 1 } / ( { \bf 1 } - { p } _ { 1 } { p } _ { 3 } )$ $\operatorname* { P r } ( X _ { 1 } = 1 | e ) = 1 - [ q _ { 1 } / ( 1 - p _ { 1 } p _ { 3 } ) ] ;$ PrŽ $X _ { 3 } = 0 | e \rangle = ( q _ { 3 } p _ { 1 } + q _ { 3 } q _ { 1 } ) / ( q _ { 3 } p _ { 1 } + q _ { 3 } q _ { 1 } + p _ { 3 } q _ { 1 } ) = q _ { 3 } / ( 1 -$ $p _ { 1 } p _ { 3 } ) , \operatorname* { P r } ( X _ { 3 } = 1 | e ) = 1 - [ q _ { 3 } / ( 1 - p _ { 1 } p _ { 3 } ) ] .$ . At this point, the d.m. does not seem to have any plausible reason to revise his prior requirements. Since the d.m. is not satisfied with the accuracy of the current solution becauseŽ $\operatorname* { P r } ( \pmb { x } ^ { * } | \pmb { e } ) = 0 . 6 4 3 < \overline { { \alpha } } = 0 . 9 )$ , he decides to make another information-gathering action.

Tables 4 and 5 report the probabilities of the best explanations associated with all possible values for the remaining candidate evidence nodes. Then, the average probabilities of the best explanations are:

$$
\overline {{{\operatorname * {P r}}}} \left(X _ {1}\right) = 0. 6 4 3 \times 0. 7 1 4 + 1 \times 0. 2 8 6 = 0. 7 4 5
$$

$$
\overline {{{{\operatorname * {P r}}}}} \left(X _ {3}\right) = 0. 7 1 4 \times 0. 3 5 7 + 1 \times 0. 6 4 3 = \mathbf {0 . 8 9 8}
$$

Hence, node $X _ { 3 }$ is the candidate for observation. Since $C ( X _ { 2 } \cup X _ { 3 } ) = 2 0 0 > B = 1 0 0$ , node $X _ { 3 }$ is discarded and so is for $X _ { 1 } ,$ , that has the same observation cost. Given that it is not possible to observe any further node, the current tentative solution is rejected, while the budget constraint is updated according to $B = k B ,$ , so that $B = 2 0 0$ this is allowed by the total available budget amount Ž . B<sup>s</sup>200 . Clearly, node $X _ { 2 }$ can be saved as part of the final solution.

Although the probability level reached by the best explanation is very near to the threshold $\overline { { \alpha } } = 0 . 9 .$ , the d.m. would need to observe at least node $X _ { 3 }$ in order to accept the solution. However, he notes that the best explanation will set node $X _ { 1 }$ at value $0 ,$ whatever the observed value for $X _ { 3 }$ . Hence, observing $X _ { 3 }$ does not provide significant further information to the d.m., who now feels more confident about the achieved solution. As a consequence, he fixes a lower a posteriori minimum required confidence level ${ \overline { { \alpha } } } ,$ say, equal to 0.625. Now, the stopping criterion is met and neither node $X _ { 3 }$ nor $X _ { 1 }$ need to be observed, so that $\{ X _ { 1 } = 0 , X _ { 2 } = 1$ $X _ { 3 } = 1 ; Y _ { 0 } = 1 , Y _ { 1 } = 0 , Y _ { 2 } = 0 , Y _ { 3 } = 0 \}$ is the final accepted solution. Thus, the d.m. can save a fraction of his budget, since $C ( X _ { 2 } ) = 1 0 0$ while $\overline { { B } } = 2 0 0$ . Note that an off-line optimization approach would result in an infeasible solution. As a matter of fact, a budget amount of $B = 3 0 0 > \overline { { B } } = 2 0 0$ would be necessary to reach $\overline { { \alpha } } = 0 . 9$ . Note also that the solution cost achieved by Algorithm I is optimal. In fact, it is the same as the cost incurred by an oracle who a priori is able to anticipate correctly that the $\mathrm { { d . m . } \gamma _ { s } }$ a posteriori minimum required confidence level will be equal to 0.625 since he makes his best choice by selecting nodeŽ $X _ { 2 }$ . for observation .

Information content of variable $X _ { 2 }$ given the current evidence set

<table><tr><td colspan="5">Explanations</td></tr><tr><td>Observed values</td><td> $\boldsymbol{x}_{5}:\{X_{1}=X_{3}=0\}$ </td><td> $\boldsymbol{x}_{6}:\{X_{1}=1,X_{3}=0\}$ </td><td> $\boldsymbol{x}_{7}:\{X_{1}=0,X_{3}=1\}$ </td><td> $\boldsymbol{x}_{8}:\{X_{1}=X_{3}=1\}$ </td></tr><tr><td> $\boldsymbol{e}_{3}:X_{2}=0,Y_{0}=1,Y_{3}=0$ </td><td> $\Pr(\boldsymbol{x}_{5}|\boldsymbol{e}_{3})=q_{1}q_{3}$ </td><td> $\Pr(\boldsymbol{x}_{6}|\boldsymbol{e}_{3})=p_{1}q_{3}$ </td><td> $\Pr(\boldsymbol{x}_{7}|\boldsymbol{e}_{3})=q_{1}p_{3}$ </td><td> $\Pr(\boldsymbol{x}_{8}|\boldsymbol{e}_{3})=\boldsymbol{p}_{1}\boldsymbol{p}_{3}$ </td></tr><tr><td> $\boldsymbol{e}_{4}:X_{2}=1,Y_{0}=1,Y_{3}=0$ </td><td> $\Pr(\boldsymbol{x}_{5}|\boldsymbol{e}_{4})=q_{1}q_{3}/(1-p_{1}p_{3})$ </td><td> $\Pr(\boldsymbol{x}_{6}|\boldsymbol{e}_{4})=\boldsymbol{p}_{1}\boldsymbol{q}_{3}/(1-\boldsymbol{p}_{1}\boldsymbol{p}_{3})$ </td><td> $\Pr(\boldsymbol{x}_{7}|\boldsymbol{e}_{4})=q_{1}p_{3}/(1-p_{1}p_{3})$ </td><td> $\Pr(\boldsymbol{x}_{8}|\boldsymbol{e}_{4})=0$ </td></tr></table>

Table 3  
Information content of variable $X _ { 3 }$ given the current evidence set

<table><tr><td colspan="5">Explanations</td></tr><tr><td>Observed values</td><td> $\boldsymbol{x}_{9}:\{X_{1}=X_{2}=0\}$ </td><td> $\boldsymbol{x}_{10}:\{X_{1}=1,X_{2}=0\}$ </td><td> $\boldsymbol{x}_{11}:\{X_{1}=0,X_{2}=1\}$ </td><td> $\boldsymbol{x}_{12}:\{X_{1}=X_{2}=1\}$ </td></tr><tr><td> $\boldsymbol{e}_{5}:X_{3}=0,Y_{0}=1,Y_{3}=0$ </td><td> $\Pr(\boldsymbol{x}_{9}|\boldsymbol{e}_{5})=q_{1}q_{2}$ </td><td> $\Pr(\boldsymbol{x}_{10}|\boldsymbol{e}_{5})=p_{1}q_{2}$ </td><td> $\Pr(\boldsymbol{x}_{11}|\boldsymbol{e}_{5})=q_{1}p_{2}$ </td><td> $\Pr(\boldsymbol{x}_{12}|\boldsymbol{e}_{5})=\boldsymbol{p}_{1}\boldsymbol{p}_{2}$ </td></tr><tr><td> $\boldsymbol{e}_{6}:X_{3}=1,Y_{0}=1,Y_{3}=0$ </td><td> $\Pr(\boldsymbol{x}_{9}|\boldsymbol{e}_{6})=q_{1}q_{2}/(1-p_{1}p_{2})$ </td><td> $\Pr(\boldsymbol{x}_{10}|\boldsymbol{e}_{6})=\boldsymbol{p}_{1}\boldsymbol{q}_{2}/(\boldsymbol{1}-\boldsymbol{p}_{1}\boldsymbol{p}_{2})$ </td><td> $\Pr(\boldsymbol{x}_{11}|\boldsymbol{e}_{6})=q_{1}p_{2}/(1-p_{1}p_{2})$ </td><td> $\Pr(\boldsymbol{x}_{12}|\boldsymbol{e}_{6})=0$ </td></tr></table>

## 5.2. Market entry decision

Let us consider a stylized situation where the sale-price of a good produced by an incumbent firm I which operates in a monopolistic market depends on her unit production cost which in turn is influenced primarily by the quality level of the good. Let P denote the variable that identifies the sale-price, AC the unit production cost and Q the quality level of the good produced by firm I, where all variables are binary and can take value high Ž . Ž . h or low l . The relation between these variables can be graphically represented by the chain of nodes $Q \to \mathbf { A C } \to P$ . Variable P is directly observable by a potential competitor firm Ž . E , while the values taken by Q and AC can only be inferred from that of P. The potential entrant has to evaluate the profitability of the market by assessing the most probable incumbent’s type at a reasonable cost, given his satisfactory confidence level $\overline { { \alpha } } = 0 . 8 0$ and available budget $\overline { { B } } = 1 0 0$ . Entry is assumed to be profitable only when the entrant correctly infers that the incumbent is a ‘weak’ competitor because she has a high unit production cost. By firm $E " s$ viewpoint, Q generates expectations about AC and AC expectations about P. These expectations are expressed by firm E through the specification of the following conditional probability matrices:

Ž .a $M _ { \mathrm { A C | Q } } = \mathrm { P r } ( \mathrm { A C | Q } )$

$$
\begin{array}{c c c} & \text {AC} \\ \text {Q} & \text {high} & \text {low} \\ \text {high} & 0. 8 0 & 0. 2 0 \\ \text {low} & 0. 2 5 & 0. 7 5 \end{array}
$$

$$
\mathrm{(b)} M _ {\mathrm{P} | \mathrm{AC}} = \operatorname * {P r} (\mathrm{P} | \mathrm{AC})
$$

$$
\begin{array}{c c c} & \text {P} \\ \text {AC} & \text {high} & \text {low} \\ \text {high} & 0. 7 0 & 0. 3 0 \\ \text {low} & 0. 1 0 & 0. 9 0 \end{array}
$$

Matrix a states that high unit production cost is essentially a feature of high quality for the good produced Ž . by firm I, since $\operatorname* { P r } ( \mathrm { A C } = h | \mathrm { Q } = h ) = 0 . 8 0$ , but there is also a not negligible chance that it can be associated with a low quality, since $\operatorname* { P r } ( \mathrm { A C } = h | \mathrm { Q } = l ) = 0 . 2 5$ Ž . . Matrix b states that price per se does not reflect clearly the incumbent’s cost structure that is, market profitability : in fact, given that unit production cost is high, price canŽ . be also high with probability 0.70 but even low with probability 0.30.

Table 4  
Information content of variable $X _ { 1 }$ given the updated evidence set

<table><tr><td colspan="3">Explanations</td></tr><tr><td>Observed values</td><td> $\boldsymbol{x}_{13}:\{X_3=0\}$ </td><td> $\boldsymbol{x}_{14}:\{X_3=1\}$ </td></tr><tr><td> $\boldsymbol{e}_7: X_1=0, X_2=1, Y_0=1, Y_3=0$ </td><td> $\Pr(\boldsymbol{x}_{13}|\boldsymbol{e}_7)=q_3/(1-p_1p_3)$ </td><td> $\Pr(\boldsymbol{x}_{14}|\boldsymbol{e}_7)=1-[q_3/(1-p_1p_3)]$ </td></tr><tr><td> $\boldsymbol{e}_8: X_1=1, X_2=1, Y_0=1, Y_3=0$ </td><td> $\Pr(\boldsymbol{x}_{13}|\boldsymbol{e}_8)=1$ </td><td> $\Pr(\boldsymbol{x}_{14}|\boldsymbol{e}_8)=0$ </td></tr></table>

Table 5  
Information content of variable $X _ { 3 }$ given the updated evidence set

<table><tr><td colspan="3">Explanations</td></tr><tr><td>Observed values</td><td> $x_{15}:\{X_1=0\}$ </td><td> $x_{16}:\{X_1=1\}$ </td></tr><tr><td> $e_9: X_3=0, X_2=1, Y_0=1, Y_3=0$ </td><td> $\Pr(x_{15}|e_9)=q_1/(1-p_1p_3)$ </td><td> $\Pr(x_{16}|e_9)=1-[q_1/(1-p_1p_3)]$ </td></tr><tr><td> $e_{10}: X_3=1, X_2=1, Y_0=1, Y_3=0$ </td><td> $\Pr(x_{15}|e_{10})=1$ </td><td> $\Pr(x_{16}|e_{10})=0$ </td></tr></table>

Let us now briefly recall from Ref. 14 that the probability distribution of a generic variable<sup>w</sup> <sup>x</sup> $X _ { i }$ can be computed when, in addition to the fixed conditional probability matrix which relates the variable to its parent node, two types of parameters are made available. These are the so-called $\pi$ and measuring the current strengths of the predictive and retrospective supports contributed by the parent and child nodes ofŽ $X _ { i } ,$ respectively to each possible value of the variable. Given that predictive and retrospective supports change their. values every time a new piece of evidence is collected, the probability distribution of $X _ { i }$ has to be modified accordingly. The separation between the two kinds of supports allows local updating of beliefs at each node and prevents feedback effects, circular reasoning or indefinite relaxations. Formally, the total evidence e obtained at any given moment can be decomposed into $e ^ { - }$ , representing the evidence connected to $X _ { i }$ through its child and $e ^ { + }$ , representing the evidence connected to $X _ { i }$ through its parent, in such a way that $\operatorname* { P r } ( X _ { i } = x _ { i } ) =$ $\gamma \operatorname* { P r } ( e ^ { - } | x _ { i } ) \operatorname* { P r } ( x _ { i } | e ^ { + } ) = \gamma \lambda ^ { ( } x _ { i } ) \pi ( x _ { i } )$ , where $\gamma$ is a normalizing constant such that $\textstyle \sum _ { x _ { i } } \operatorname* { P r } ( X _ { i } = x _ { i } ) = 1$ . Then, node $X _ { i }$ computes new messages to be sent to its child and parent nodes, respectively, on the basis of the updated  and  messages just received. This process takes place until, at peripheral nodes, the impact of a new piece of evidence is absorbed without reflection.

In our market entry decision example, let $e ^ { + }$ denote the evidence vector that is available a priori to the potential entrant. Such a vector consists of parameters and variables other than those explicitly included in the chain which are still relevant to characterize the considered market e.g., industrial sector, market structure, size,Ž growth rate and so on . Thus,. $\pi ( q ) = \operatorname* { P r } ( q | e ^ { + } )$ stands for the entrant’s prior certainty that quality level $q$ $( q = h , l )$ is achieved by firm $r { \mathrm { s } }$ good, while $\pi ( \mathrm { a c } ) = \operatorname* { P r } ( \mathrm { a c } | e ^ { + } )$ measures the entrant’s prior certainty that firm I’s unit production cost is at level ac $\mathrm { ( a c = } h , \ l \mathrm { ) }$ . Taking $\pi ( q ) = ( \pi ( q = h ) , \pi ( q = l ) ) = ( 0 . 8 0 , 0 . 2 0 )$ , we get:

$$
\pi (\mathrm{ac}) = (0. 8 0, 0. 2 0) \times \left[ \begin{array}{c c} 0. 8 0 & 0. 2 0 \\ 0. 2 5 & 0. 7 5 \end{array} \right] = (0. 6 9, 0. 3 1).
$$

As regards variable P, we have:

$$
\pi (p) = (0. 6 9, 0. 3 1) \times \left[ \begin{array}{c c} 0. 7 0 & 0. 3 0 \\ 0. 1 0 & 0. 9 0 \end{array} \right] = (0. 5 1, 0. 4 9).
$$

Before observing variable P, there is no particular evidential support for any specific value of variables AC and Q, so that all are unit vectors and the probability distributions for the nodes coincide with the given prior certainties.

At first, $\lambda ^ { * } ( \ l _ { p } ) = \lambda ( \ l _ { p } ) = ( 1 , 1 )$ and $\pi ^ { * } ( q ) = \pi ( q ) = ( 0 . 8 0 , 0 . 2 0 )$ . As a consequence, for node AC we get:

$$
\begin{array}{r l} \pi^ {*} (a c) & = \left[ \operatorname{MAX} \{(0. 8 0 \times 0. 8 0), (0. 2 0 \times 0. 2 5) \}, \operatorname{MAX} \{(0. 8 0 \times 0. 2 0), (0. 2 0 \times 0. 7 5) \} \right] \\ & = \left[ \operatorname{MAX} \{(0. 6 4, 0. 0 5) \}, \operatorname{MAX} \{(0. 1 6, 0. 1 5) \} \right] = (0. 6 4, 0. 1 6). \end{array}
$$

In a similar way, for node P we compute:

$$
\begin{array}{c} \pi^ {*} (p) = \left[ \operatorname{MAX} \bigl \{(0. 6 4 \times 0. 7 0), (0. 1 6 \times 0. 1 0) \bigr \}, \operatorname{MAX} \bigl \{(0. 6 4 \times 0. 3 0), (0. 1 6 \times 0. 9 0) \bigr \} \right] \\ = \left[ \operatorname{MAX} \bigl \{(0. 4 5, 0. 0 2) \bigr \}, \operatorname{MAX} \bigl \{(0. 1 9, 0. 1 4) \bigr \} \right] = (0. 4 5, 0. 1 9). \end{array}
$$

Now assume that firm $E ^ { * } s$ available budget is such that he can observe the price selected by firm I Žthis does happen if the observation cost of variable $P$ is lower than 100 . Let. $e ^ { - } = \{ P = l \}$ . Thus, firm E observes that price is low. The Ž .ac vector corresponding to node AC can be updated as follows:

$$
\lambda (\mathrm{ac}) = \operatorname * {P r} (e ^ {-} | \mathrm{ac}) = (0, 1) \times \left[ \begin{array}{l l} 0. 7 0 & 0. 3 0 \\ 0. 1 0 & 0. 9 0 \end{array} \right] = (0. 1 0, 0. 9 0).
$$

Then, node AC updates its probability distribution in the following way:

$$
\operatorname * {P r} (\mathrm{ac}) = \gamma \lambda (\mathrm{ac}) \pi (\mathrm{ac}) = \gamma (0. 1 0, 0. 9 0) (0. 6 9, 0. 3 1) = \gamma (0. 0 7, 0. 2 8) = (0. 2 0, 0. 8 0).
$$

The new $\lambda ( q )$ vector for node $Q$ can be computed according to the following rule:

$$
\lambda (q) = M _ {\mathrm{ac} | q} \lambda (\mathrm{ac}) = \gamma \left[ \begin{array}{c c} 0. 8 0 & 0. 2 0 \\ 0. 2 5 & 0. 7 5 \end{array} \right] \left[ \begin{array}{c} 0. 1 0 \\ 0. 9 0 \end{array} \right] = \gamma \left[ \begin{array}{c} 0. 2 6 \\ 0. 7 0 \end{array} \right]
$$

Then, node Q updates its probability distribution as follows:

$$
\operatorname * {P r} (q) = \gamma \lambda (q) \pi (q) = \gamma (0. 2 6, 0. 7 0) (0. 8 0, 0. 2 0) = \gamma (0. 2 1, 0. 1 4) = (0. 6 0, 0. 4 0).
$$

Let us now turn to the task of computing the most probable explanation of available evidence see Ref. 14 .Ž <sup>w</sup> <sup>x</sup>. Formally, finding the best explanation requires that the vector $x ^ { * }$ be determined such that $x ^ { * }$ is the most probable assignment of values to all variables that is consistent with e, representing observed evidence. Therefore, $x ^ { * }$ is the solution vector if $\mathrm { P r } ( \mathbf { \boldsymbol { x } } ^ { * } | \boldsymbol { e } ) = \mathrm { M A X } _ { \boldsymbol { x } } \mathrm { P r } ( \boldsymbol { x } | \boldsymbol { e } )$ . This vector can be obtained through local inference mechanisms that enable us to select and assemble together the most probable values of each variable. In order to illustrate these mechanisms, let us assume for simplicity that node $X _ { i }$ has a parent node $\mathrm { P A } _ { i }$ and a child node $\mathrm { C H } _ { i } .$ Then, it is possible to assess the most probable explanation associated with each of its possible values $x _ { i }$ on the basis of the degree of support contributed by its parent, denoted by $\pi ^ { * } ( \mathfrak { p a } _ { i } )$ , and the degree of support contributed by its children, denoted by $\lambda ^ { * } ( x _ { i } )$ , where:

$$
\pi^ {*} (\mathrm{pa} _ {i}) = \underset {\boldsymbol {e} ^ {+}} {\text { MAX }} \Pr (\mathrm{pa} _ {i}, \boldsymbol {e} ^ {+})\tag{7}
$$

$$
\lambda^ {*} (x _ {i}) = \underset {\boldsymbol {e} ^ {-}} {\text { MAX }} \operatorname * {P r} (\boldsymbol {e} ^ {-} | x _ {i})\tag{8}
$$

Message 7 stands for the probability of the most probable tail-extension of a possible observationŽ . $\mathrm { P A } _ { i } = \mathrm { p a } _ { i }$ relative to link $\mathrm { P A } _ { i } \to X _ { i } ,$ , while message 8 stands for the probability of the most probable head-extension ofŽ . observation $X _ { i } = x _ { i }$ relative to link $X _ { i } \to \mathbf { C H } _ { i }$ . Using these messages, together with the fixed probability matrix $\mathrm { P r } ( x _ { i } | \mathbf { p } \mathbf { a } _ { i } )$ for all i, one can find $X _ { i } ^ { \mathrm { ~ , ~ } } \mathrm { s }$ most probable value according to the rule: $\operatorname* { P r } ^ { * } ( x _ { i } ) = \beta \times \mathbf { M A X }$ $\lambda ^ { * } ( \dot { x _ { i } } ) \times \mathrm { { P r } } ( x _ { i } | \mathrm { { p a } } _ { i } ) \times \pi ^ { * } ( \mathrm { { p a } } _ { i } ) .$ , where $\bar { \boldsymbol { \beta } } = [ \mathrm { P r } ( e ^ { + } , e ^ { - } ) ] ^ { - 1 }$ is a normalizing constant. Note that the described messages carry a summarized description of the whole network which is enough to guarantee that locally optimal choices can be assembled in a globally optimal explanation. <sup>5</sup> Note also that the information carried by messages $\pi ^ { * }$ and $\lambda ^ { * }$ has a different meaning with respect to their counterparts $\pi$ and . While the propagation dynamics are the same in the two message-passing procedures, the former Ž . belief reÕision involves maximization whereas in the latter Ž . belief updating summation is performed.

In our market entry example, the best explanation identifies the most probable incumbent’s type since it gives the most probable combination of values for unobservable firm $I ^ { \prime } s$ characteristics i.e.,Ž . Q and AC given the value taken by the observed variable i.e.,Ž . P <sup>s</sup> l . First, note that predictive supports do not vary after observing $P = l$ since evidence is collected at the leaf of the considered chain. As regards diagnostic supports, given that $\{ P = l \}$ is observed we have $\lambda ^ { * } ( \mathbf { \Sigma } _ { p } ) = ( 0 , 1 ) ( 1 , 1 ) = ( 0 , 1 )$ . Then, for node AC we get:

$$
\lambda^ {*} (a c) = \left[ \operatorname{MAX} \{(0. 7 0 \times 0), (0. 3 0 \times 1) \}, \operatorname{MAX} \{(0. 1 0 \times 0), (0. 9 0 \times 1) \} \right] = (0. 3 0, 0. 9 0).
$$

Finally, for node Q we have:

$$
\begin{array}{r l} \lambda^ {*} (q) & = \left[ \operatorname{MAX} \{(0. 8 0 \times 0. 3 0), (0. 2 0 \times 0. 9 0) \}, \operatorname{MAX} \{(0. 2 5 \times 0. 3 0), (0. 7 5 \times 0. 9 0) \} \right] \\ & = \left[ \operatorname{MAX} \{(0. 2 4, 0. 1 8) \}, \operatorname{MAX} \{(0. 0 7, 0. 6 7) \} \right] = (0. 2 4, 0. 6 7). \end{array}
$$

Now, we can compute the probability level reached by the best explanation and simultaneously derive the associated most plausible values for each one of the variables:

$$
\begin{array}{r l} \operatorname * {P r} (x ^ {*} | P = l) & = \underset {x} {\text {MAX}} \operatorname * {P r} (x | P = l) = \underset {x} {\text {MAX}} (\lambda^ {*} \pi^ {*} | P = l) = \frac {\underset {x} {\text {MAX}} (\lambda^ {*} \pi^ {*})}{\operatorname * {P r} (P = l)} \\ & = \frac {\operatorname{MAX} \left\{\left[ (0 . 8 0 \times 0 . 2 4) , (0 . 2 0 \times 0 . 6 7) \right] , \left[ (0 . 6 4 \times 0 . 3 0) , (0 . 1 6 \times 0 . 9 0) \right] , \left[ (0 . 4 5 \times 0) , (0 . 1 9 \times 1) \right] \right\}}{0 . 4 9} \\ & = \frac {0 . 1 9}{0 . 4 9} = 0. 3 9 \end{array}
$$

which is obtained for $\scriptstyle ( Q = h , \ A C = h , \ P = l )$ . Since firm E is not confident enough about firm $I ^ { \prime } s$ type Žbecause $\operatorname* { P r } ( x ^ { * } | P = l ) = 0 . 3 9 < \overline { { \alpha } } = 0 . 8 0 )$ and no more observable variables are left, he decides not to enter the market.

## 6. Discussion

A probabilistic reasoning model has been defined where the d.m. is engaged in a sequential informationgathering process facing the trade-off between the reliability of the achieved solution and the associated observation cost. It is assumed that payoff information is not available or cannot be directly estimated. Then, a cost-effectiveness analysis framework has been adopted that uses information-theoretic principles to identify the most informative variable relative to its observation cost at any given stage of the process. The proposed model allows defining a flexible control strategy in which the human is directly involved. This strategy works on a Bayesian belief network that allows the efficient representation and manipulation of the knowledge base relevant to the problem domain. It has been shown that the devised strategy guarantees a constant factor approximate solution with respect to the optimum of the decision problem. On the other hand, non-interactive optimization approaches may result either in a significant waste of both computational and financial resources or even in an infeasible solution. Note that the optimal solution could be achieved only by an oracle who knows a priori the $\mathrm { { d . m . } \gamma _ { s } }$ a posteriori requirements. Finally, the discussed strategy has been applied to circuit fault analysis and market entry decision.

The proposed approach is particularly suitable for diagnostic problems, where the focus is on relating the observed manifestations to the most probable underlying causes whatever the nature of the investigated system Žsee Ref. 16 . In recent years, there have been important developments in commercial tools and programs<sup>w</sup> <sup>x</sup>. available for research that use Bayesian belief networks in such distinct application fields as circuit analysis, medical diagnosis, manufacturing quality control and risk management. These programs have proved useful for dealing with complex problems defined over large domains: for instance, the INTELLIPATH system for lymph node pathology is based on the specification of over 75,000 subjective probabilities and concerns over 60 diseases 20 . Note that the interactive solution strategy discussed in this paper can be suitably integrated into <sup>w</sup> <sup>x</sup> these models since a key point of any probabilistic decision-making model involves selecting the most informative questions in order to make an accurate final decision at a reasonable cost.

It is worth noting that each information-gathering action takes time to be performed so that there exists a certain time gap between deciding to make an action and getting the relevant information. It follows that the information sources sequential selection process takes time to complete. It is implicitly assumed that the investigated variables do not change their values as revealed by the information-gathering actions during theŽ . whole period of the decision process. Therefore, a suitable time constraint should be imposed on such a process within which it is reasonable to suppose that this assumption holds 11 .<sup>w</sup> <sup>x</sup>

The demand for information has been proved to depend not only on the specific decision setting, but also on the d.m.’s attitude toward risk as well as conditions and methods of payment for acquiring information sources <sup>w</sup> <sup>x</sup> 13 . We have not been primarily concerned with these issues here. We have only assumed that the d.m. has to make an ex ante payment, that is, to pay a given amount for observing any variable before learning its actual value. It follows that the d.m.’s budget amount is reduced of the corresponding information-gathering cost. This is usually the case when the d.m. resorts to external sources, such as consultants, market research firms and information services organizations. However, this method of payment may also apply to an end user department that is charged for the services provided by the information system department of the same firm that is anŽ internal information source ..

Future work will develop along the following directions. First, we intend to investigate the trade-off between solution accuracy and procedure complexity. Actually, the reliability of the solution can be improved at the expense of a higher complexity. This can be obtained both by identifying the ‘best’ value of parameter k and by recursively partitioning the interval width between the optimal and the achieved budget amount at the last iteration of Algorithm I, so long as the d.m. is satisfied. Second, we intend to assess the performance of alternative computational tools, given that some troubles affect Bayesian networks when their structure gets too complex and, in particular, when loops are present. Note that the computational complexity of belief propagation schemes depends far more on the network structure than either the number of variables or probability parameters per se.

## Acknowledgements

We are grateful to the Area Editor and an anonymous referee whose comments and suggestions led to major improvements in the paper.

## Appendix A. List of symbols

<table><tr><td>M</td><td>Decision-making model</td></tr><tr><td>DP</td><td>Decision problem</td></tr><tr><td>BP</td><td>Bilevel programming model</td></tr><tr><td>IP</td><td>Integer programming model</td></tr><tr><td>G=(X,L)</td><td>Bayesian belief network</td></tr><tr><td>X</td><td>Set of variables (of size n)</td></tr><tr><td>Xi</td><td>Any variable in X</td></tr><tr><td>xi</td><td>Any value of variable Xi</td></tr><tr><td>RX</td><td>Domain of variables in X</td></tr><tr><td>RXi</td><td>Domain of variable Xi</td></tr><tr><td>V</td><td>Maximum number of values for any network variable</td></tr><tr><td>F⊂X</td><td>Subset of no-cost variables</td></tr></table>

f Values of variables in F $A \subset X$ Subset of acquired variables a Values of variables in A $E = \left( F \cup A \right) \subset X$ Evidence set $E ^ { * }$ Optimal evidence set $e$ Values of variables in E $\boldsymbol { x }$ Explanation $x ^ { * }$ Best explanation $C ( \cdot )$ Observation cost function $C ^ { * }$ Optimal observation cost $Z ^ { + }$ Positive integer numbers $\operatorname* { P r } ( \cdot )$ Probability function ${ \overline { { \operatorname* { P r } } } } _ { i } ( x ^ { * } | e \cup X _ { i } )$ Average probability of $x ^ { * }$ after observing $X _ { i }$ given e $D ( \cdot )$ Decision map $d$ Any single decision α Minimum required confidence level a prioriŽ . $\overline { { \alpha } }$ Minimum required confidence level a posteriori Ž . $\overline { B }$ Total budget amount $B$ Current budget constraint $r$ Any Algorithm I iteration

## Appendix B. Proofs

## B.1. Proof of Proposition 1

Statement i follows from the fact that parametersŽ . and $\overline { B }$ Ž . Ž . in model 1 – 6 are set a priori in a once-for-all fashion. If $C ( E ^ { * } ) > \overline { { B } }$ , then IP does not admit a feasible solution for DP, since the observation cost of the optimal evidence set exceeds the d.m.’s available budget. As for statement ii , assume thatŽ . $\overline { { \alpha } } = \alpha - \varepsilon$ $\varepsilon > 0$ Ž . <sup>w</sup> . Then, simple examples such as those given in Section 5 show that C ${ \cal E } _ { ( \alpha - \varepsilon ) } ^ { * } ] - C [ E _ { ( \alpha ) } ^ { * } ] < 0$ , since the a posteriori threshold is met by observing $E _ { ( \alpha - \varepsilon ) } ^ { * } \subset E _ { ( \alpha ) } ^ { * } ,$ , that is, a subset of the variables which have to be observed given the a priori -threshold.

## B.2. Proof of Proposition 3

Assume that, for any given problem instance, there exists an integer h, $0 \leq h \leq [ \log _ { k } ( { \overline { { B } } } / B ) + 1 ] .$ , such that Algorithm I stops at iteration h. Let $B _ { ( h ) } ^ { * }$ be the optimal budget amount to be spent in order to reach $\overline { { \alpha } } _ { ( h ) }$ , that is the d.m.’s a posteriori minimum required confidence level in the final solution. Then:

$$
\operatorname * {P r} \Big (\boldsymbol {x} _ {(h - 1)} ^ {*} | \boldsymbol {e} _ {(h - 1)} \Big) <   \overline {{\alpha}} _ {(h)} \leq \operatorname * {P r} \Big (\boldsymbol {x} _ {(h)} ^ {*} | \boldsymbol {e} _ {(h)} \Big); B _ {(h - 1)} <   B _ {(h)} ^ {*} \leq B _ {(h)} = k B _ {(h - 1)}.
$$

In fact, $B _ { ( h ) } ^ { * }$ and $\overline { { \alpha } } _ { ( h ) }$ fall within the ranges identified by the last two steps of Algorithm I, since at the last iteration the d.m. is satisfied of the current solution, while at the last but one he does not feel confident enough. In the worst possible case $B _ { ( h - 1 ) } = C ^ { * }$ , so that at the last iteration the d.m. spends at most $B _ { ( h ) } = k C ^ { * }$

However, the evidence set may change completely but for the first selected node when passing from any given Ž . iteration to the next one. Therefore, at worst Algorithm I requires the following costs:

$$
\begin{array}{l} C _ {\mathrm{I}} = k C ^ {*} + C ^ {*} \sum_ {i = 0} ^ {[ \log (C ^ {*} / B) ]} \frac {1}{k ^ {i}} <   k C ^ {*} + C ^ {*} \sum_ {i = 0} ^ {\infty} \frac {1}{k ^ {i}} = k C ^ {*} + C ^ {*} \sum_ {i = 0} ^ {\infty} \left(\frac {1}{k}\right) ^ {i} \\ = k C ^ {*} + \frac {k}{k - 1} C ^ {*} = \frac {k ^ {2}}{k - 1} C ^ {*}, \text {i.e.d.} \end{array}
$$

## References

<sup>w</sup> <sup>x</sup> 1 K.J. Arrow, The value of and demand for information, in: C.B. McGuire, R. Radner Eds. , Decision and Organization, North-Holland, Ž . Amsterdam, 1972.

<sup>w</sup> <sup>x</sup>2 D. Campisi, A. Nastasi, P. Reverberi, Reducing information asymmetries in market entry decisions, Int. J. Systems Sci. 28 1997Ž . 657–667.

<sup>w</sup> <sup>x</sup> 3 J.H. Dunning, Multinational Enterprises and The Global Economy, Addison-Wesley, Reading, UK, 1993.

<sup>w</sup> <sup>x</sup> 4 P. Hansen, B. Jaumard, G. Savard, New branch-and-bound rules for linear bilevel programming, SIAM J. SSC 5 1992 1194–1217.Ž .

<sup>w</sup> <sup>x</sup> 5 V.S. Jacob, J.C. Moore, A.B. Whinston, An analysis of human and computer decision-making capabilities, Information and Management 16 1989 247–255.Ž .

<sup>w</sup> <sup>x</sup> 6 S.L. Lauritzen, D.J. Spiegelhalter, Local computations with probabilities on graphical structures and their applications to expert systems, J. R. Statistical Soc. 50 1988 157–224, Series B.Ž .

<sup>w</sup> <sup>x</sup> 7 M. Machina, Decision-making in the presence of risk, Science 1987 537–543. Ž .

<sup>w</sup> <sup>x</sup> 8 A.S. Masud, C.L. Hwang, Interactive sequential goal programming, J. Operational Res. Soc. 32 1981 391–400. Ž .

<sup>w</sup> <sup>x</sup> 9 A.M. McGahan, The effect of incomplete information about demand on preemption, Int. J. Industrial Organization 11 1993 327–346.Ž .

<sup>w</sup> <sup>x</sup> 10 P. Milgrom, J. Roberts, Limit pricing and entry under incomplete information: a general equilibrium analysis, Econometrica 50 1982Ž . 863–894.

<sup>w</sup> <sup>x</sup> 11 J.C. Moore, A.B. Whinston, A model of decision-making with sequential information acquisition, Decision Support Systems 2 1986 Ž . 285–307, Part 1 .Ž .

<sup>w x</sup>12 J.C. Moore, A.B. Whinston, A model of decision-making with sequential information acquisition, Decision Support Systems 3 1987Ž . 47–72, Part 2 .Ž .

<sup>w</sup> <sup>x</sup> 13 R. Nadiminti, T. Mukhopadhyay, C.H. Kriebel, Risk aversion and the value of information, Decision Support Systems 16 1996Ž . 241–254.

<sup>w</sup> <sup>x</sup> 14 J. Pearl, Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference, Morgan Kaufmann Publishers, San Mateo, CA, 1992.

<sup>w</sup> <sup>x</sup> 15 Y. Peng, J.A. Reggia, Abductive Inference Models for Diagnostic Problem-solving, Springer-Verlag, New York, 1990.

<sup>w</sup> <sup>x</sup>16 P. Reverberi, M. Talamo, A theoretical approach to diagnostic problem-solving in Bayesian belief networks, Proc. UNICOM Int. Conf. ‘Applied Decision Technologies’, London, 1995, pp. 185–207.

<sup>w</sup> <sup>x</sup> 17 S. Sarkar, D. Ghosh, A probabilistic reasoning model: formulation and control strategy, Decision Support Systems 17 1996 365–386. Ž .

<sup>w</sup> <sup>x</sup> 18 R.D. Shachter, Evaluating influence diagrams, Operations Res. 34 1986 871–882.Ž .

<sup>w</sup> <sup>x</sup>19 C.E. Shannon, A mathematical theory of communication, The Bell System Technical Journal 27 1948 379–423 and 623–656.Ž .

<sup>w</sup> <sup>x</sup> 20 D.J. Spiegelhalter, A.P. Dawid, S.L. Lauritzen, R.G. Cowell, Bayesian analysis in expert systems, Statistical Sci. 8 1993 219–247.Ž .

<sup>w</sup> <sup>x</sup> 21 M. Zeleny, J.L. Cochrane, A priori and a posteriori goals in macro-economic policy-making, in: M. Zeleny, J.L. Cochrane Eds. ,Ž . Multiple Criteria Decision-Making, University of South Carolina Press, Columbia, 1973, pp. 373–391.
