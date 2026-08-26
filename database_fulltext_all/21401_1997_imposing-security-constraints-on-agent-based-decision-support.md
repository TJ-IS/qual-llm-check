---
otero_id: 21401
otero_key: "4R5MBHDA"
title: "Imposing security constraints on agent-based decision support"
authors: "Love Ekenberg; Mats Danielson; Magnus Boman"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00072-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Imposing security constraints on agent-based decision support

Love Ekenberg \*, Mats Danielson, Magnus Boman

The DECIDE Research Group, Department of Computer and Systems Sciences, Stockholm University and Royal Institute of Technology. Electrum 230, S-164 40 Kista, Sweden

## Abstract

The principle of maximising the expected utility has had a large influence on agent-based decision support. Even though this principle is often useful when evaluating a decision situation, it is not always the most rational decision rule and other candidates are worth considering. A decision making agent may want, for example, to exclude particular strategies which, in some sense, are too risky with respect to specific thresholds. A theory is presented for situations where a decision making agent, human or machine, has to choose between a finite set of strategies having access to a finite set of autonomous agents reporting their opinions on the strategies. The approach considers a decision problem with respect to the contents and the credibilities of the reports, and the main emphasis is on how to perform analyses in decision situations where the available information is vague or numerically imprecise. © 1997 Elsevier Science B.V.

Keywords: Decision analysis; Multi-agent systems; Utility theory; Uncertain reasoning; Security constraints

## 1. Introduction

Methods for decision support systems (DSSs) are of prime concern to any enterprise. All kinds of organisations must continuously make decisions of the most varied nature in order to survive and attain their objectives. A large part of the time spent in any organisation, not least at management levels, is spent gathering, processing, and compiling information for the purpose of making decisions supported by that information. Theories of intelligent agents offer means for dealing with the inherent complexity of developing distributed systems for organisational decision support and the advances in distributed agent intelligence (DAI) over the last five years has affected the design methods of DSSs in several ways. The field of DAI is often partitioned into a distributed problem solving (DPS) part and a multi-agent systems (MASs) part [5], and over the last ten years, decision theory has become increasingly more important, especially to the latter. Papers on game theory [44,42], rational meta-reasoning [45], autonomous agent co-operation [3], formal decision analysis [11,9], and even a return to classical decision methods [50] have appeared.

Rational decision making is weakly defined in [48] as the process of choosing among a finite number of acts by a series of steps that (i) lists the acts, (ii) determines all their consequences, and (iii) makes a comparative evaluation. Although the definition is of little use as such, its weaknesses make it suitable for use as a proviso for some points we wish to make in this paper. Note that the term act is loosely used.

A more detailed discussion can be found in [28]. Henceforth, we will instead use the concept of strategy. A classical problem concerning (iii) is that there exists no absolute notion of rational decision making. For instance, in MASs, in contrast to DPSs, there is no global notion of utility (cf. [43]). Rather, rationality is usually interpreted as meaning that any agent behaviour being sub-optimal with respect to the goal is either accidental or unavoidable. To explicate this interpretation, one may turn to the first presidential address of AAAI [37] which has been influential in spreading the agent metaphor. Drawing upon ideas put forward by McCarthy in the late 1950's, Newell suggested his principle of rationality ([37], pp. 8–14):

"If an agent has knowledge that one of its actions will lead to one of its goals, then the agent will select that action [...] The principle of rationality provides, in effect, a general functional equation for knowledge. The problem for agents is to find systems at the symbol level that are solutions to this functional equation, and hence can serve as representations of knowledge [...] The principle of rationality corresponds at the symbol level to the processes (and associated data structures) that attempt to carry out problem solving to attain the agent's goals".

More pragmatically, the concept of rationality was initially treated in the MASs area as merely another property that agents could have, along with, e.g., autonomy, mobility, and benevolence (cf. Chapter 2 of [15]). This development undoubtedly came about as a reaction to the view proposed earlier by traditional AI that cognitive capabilities are more important than an agent's means to communicate, react, or adapt. In the most extreme MAS frameworks (e.g., [6]), rationality is treated as an emergent feature of an agent system.

In the last few years, several researchers have equated rationality with the use of the principle of maximising the expected utility (PMEU) as a decision rule (see, e.g., [16]). This equality was inspired by earlier research that grew from efforts of Ramsey, von Neumann, and others. Ramsey was the first to suggest a theory that integrated the ideas on subjective probability and utility, in presenting (informally) a general set of axioms for preference comparisons between strategies with uncertain outcomes. From this set, he could justify a procedure to measure a person's degree of belief from his preferences between strategies of certain forms [41]. Von Neumann and Morgenstern [36] established the foundations for a modern theory of utility. They proposed a set of axioms that they deemed reasonable for a rational decision maker, and demonstrated that the act with the highest expected utility should be preferred, given that the decision maker acted in accordance with the axioms.

There are many reasons not to identify rationality with the PMEU (cf. [4]), some of them well-known to game theorists. The unrealistic assumption that the perfectly rational (or even hyperrational, see [40], p. 107) players of the game have full knowledge of the game structure, and of the rationality of their opponents, is necessary to attain the desired equilibria (cf. [2]). Even if one accepts that game-theoretical decision rules cannot always provide useful advice to agents in non-ideal games, a view now seemingly assumed in computer science [43], there remain difficult problems to face (cf. [34]). A widespread standpoint is that a formal foundation for the PMEU is laid by the large number of axiomatic theories provided for justification of the principle (cf. [14]). A common counter-reaction to this is that the independence axioms of utility theory are fallacious, and therefore cannot be used in the core of any decision theory. For instance, the French economist Allais [1] has shown that people do not act in accordance with certain independence axioms in the system of Savage [47] (which has been the most influential system following [41]). Savage's sure-thing principle is stated as follows ([47], p. 21):

"If the person would not prefer $f$ to $g$ , either knowing that the event $B$ obtained, or knowing that the event $-B$ obtained, then he does not prefer $f$ to $g$ . Moreover (provided he does not regard $B$ as virtually impossible) if he would definitely prefer $g$ to $f$ , knowing that $B$ obtained, and, if he would not prefer $f$ to $g$ , knowing that $B$ did not obtain, then he definitely prefers $g$ to $f$ ".

This principle is formalised by two axioms. The first axiom states that the relation between the acts f and $f'$ is independent of states when the two acts have identical consequences. The other axiom postulates that no preference between two consequences can be discarded by the knowledge of an event. Another line of criticism of the PMEU is that, even if we accept the axioms in the various axiom systems, the principle does not follow. For instance, [31] shows this for the systems in [21], [38], and [47]. A fuller account of a wide variety of systems is given in [30].

Over the years, a number of other decision rules have been suggested. For example, regarding decisions under strict uncertainty, Milnor showed in his seminal article [35] that the decision rules of Laplace [26], Wald [51], Hurwicz [24], and Savage [46] were all inconsistent with a set of seemingly reasonable axioms, as well as with each other. For decisions with risk, a similar web of negative results has been developed. For instance, [19] points out that the approach in [27] has some counter-intuitive implications. Malmnäs [32] makes a similar point about the Gärdenfors–Sahlin approach. Also, different kinds of generalisations of the PMEU have been proposed, e.g., [18], [20], [29], [39], and [52], while [33] proposes a set of reasonable requirements and shows that none of these are compatible with the set.

We do not reject the use of the PMEU, but since there exists no absolute rational decision rule, a decision support system should provide possibilities to evaluate decision situations in several respects, and the purpose of this paper is to propose how this can be done in situations where the available information is vague or imprecise. First we briefly introduce a general method for decision making using autonomous agents. In the main part, we discuss a class of complementary decision rules by introducing security constraints. While a certain evaluation of a strategy may result in an acceptable expected utility, the consequences of adopting it might be so dire that it should nevertheless be avoided. It might, for example, endanger the entire purpose of the system, and in that case even a report with a low credibility is too risky to neglect. In order to attain a high level of security when allowing the reporting agents their autonomy and to be able to trust evaluations based on their reports, we suggest that security constraints should be imposed on them.

## 2. Decision support in numerically imprecise domains

Consider a scenario where a decision making agent (DMA), which may be a human decision maker as well as another agent process, faces a situation involving a choice between a finite set of strategies $\{S_{i}\}$ having access to a finite set of autonomous agents $\{A_{i}\}$ reporting their opinions on the strategies to the DMA; see Fig. 1.

In a situation modelled as above, some agents may be more reliable than others when assessing the strategies involved, since different agents may have different capabilities to determine the respective utilities. The DMA may also have access to assessments expressing the credibility of the different agents.

From this information, the DMA is set on evaluating the strategies given the agents' individual reports and their relative credibilities. However, for the DMA to carry out its tasks and to acquire sufficient and reliable knowledge, it is fundamental that it is able to evaluate information gathered from different sources, some unreliable and some noisy. The dynamic adaptation taking place over time as the DMA interacts with its environment, and with the other agents, is affected by the means available to assess and evaluate imprecise information. The DMA may rank the credibilities of the different autonomous agents as well as quantify them in imprecise terms. The autonomous agents have a similar expressibility regarding their respective reports about the strategies under consideration.

![](/api/attachments/4R5MBHDA/fulltext/images/4ff57cbb11a5f011b323932b7b9f6fb6a9ced414bd6ef3432c9732f9f4ca5bed.jpg)  
Fig. 1. A multi-agent decision model.

Example. A set of agents $(A_{1}, A_{2}, \text{and } A_{3})$ are to report to a DMA on their respective assessments concerning the strategies for an insurance policy of a company. The DMA has to decide whether to buy an essential insurance covering potential losses that would threaten the survival of the company, also to buy a desirable insurance covering potential losses that would be serious but not threaten the survival of the company, or not to buy an insurance at all. Label these strategies $S_{1}, S_{2}$ , and $S_{3}$ , respectively. Moreover, assume that the agents $A_{1}$ through $A_{3}$ have reported to the DMA the following utility statements. The utilities involved could, for example, be monetary values. In that case, they are linearly transformed to real values in the interval [0, 1].

Statements according to agent $A_{1}$ :

\- The utility of strategy $S_{1}$ is between 0.50 and 0.70.

\- The utility of strategy $S_{2}$ is between 0.10 and 0.70.

\- The utility of strategy $S_{3}$ is between 0.10 and 0.30.

\- The utility of strategy $S_{2}$ is at least 0.20 better than that of $S_{1}$ .

Statements according to agent $A_{2}$ :

\- The utility of strategy $S_{1}$ is between 0.40 and 0.60.

\- The utility of strategy $S_{2}$ is between 0.20 and 0.70.

\- The utility of strategy $S_{3}$ is at most 0.40.

\- The utility of strategy $S_{2}$ is at least 0.10 better than that of $S_{1}$ .

Statements according to agent $A_{3}$ :

\- The utility of strategy $S_{1}$ is at least equal to that of $S_{2}$ .

\- The utility of strategy $S_{2}$ is at least 0.20.

\- The utility of strategy $S_{3}$ is between 0.20 and 0.50.

Note that we only discuss the evaluation of the insurance situation from a global point of view. The individual agents may have used different kinds of risk evaluation methods to determine their utilities with respect to different criteria such as survival, economy, satisfaction, uninterrupted services, etc. (cf. [13]).

Moreover, the DMA has estimated the credibility of $A_{1}$ through $A_{3}$ as numbers in the interval [0, 1]. The number 0 denotes the lowest credibility, and 1 the highest:

\- The credibility of agent $A_{1}$ is between 0.10 and 0.80.

\- The credibility of agent $A_{2}$ is between 0.20 and 0.70.

\- The credibility of agent $A_{3}$ is at most 0.50.

One further reason for allowing comparative as well as interval assessments is that the agents' information may have different sources. For instance, intervals naturally occur from aggregated quantitative information while qualitative analyses often result in comparisons. Since the sources may be different, the assessments are not necessarily consistent with each other. Investigations into relaxing the pointwise quantitative nature of estimates were made quite early in the modern history of probability (see, e.g., [7], [8], [17], [22], [23], and [49]), and some aspects on the relation between our work and earlier approaches to represent estimates are treated in [10]. The method we propose allows for vague and numerically imprecise statements, expressing the different credibilities and utilities involved in a decision situation.

The two sets of statements in the example are transformed into linear systems of equations that are checked for consistency. The credibility statements and the set of reports constitute the credibility base $K(c)$ and the strategy base $S(u)$ respectively. A credibility base with k agents is expressed in the credibility variables $\{c_{1},\ldots,c_{k}\}$ stating the relative credibilities of the different agents. The term $c_{j}$ denotes the credibility of agent $A_{j}$ . A strategy base with k agents and m strategies is expressed in strategy variables $\{u_{11},\ldots,u_{1k},\ldots,u_{m1},\ldots,u_{mk}\}$ stating the utility of the strategies according to the different agents. The term $u_{ij}$ denotes the utility of strategy $S_{i}$ in the report of agent $A_{j}$ . It is assumed that the variables' respective ranges are real numbers in the interval [0,1]. A strategy base together with a credibility base constitute an information frame. Below, we will refer to an information frame as the structure $\langle K(c), S(u) \rangle$ .

Example (continued). The reports provided by the autonomous agents are translated to the following expressions:

$$
u _ {1 1} \in [ 0. 5 0, 0. 7 0 ]; \quad u _ {2 3} \in [ 0. 2 0, 1. 0 0 ];
$$

$$
u _ {2 1} \in [ 0. 1 0, 0. 7 0 ]; \quad u _ {3 3} \in [ 0. 2 0, 0. 5 0 ];
$$

$$
u _ {3 1} \in [ 0. 1 0, 0. 3 0 ];
$$

$$
u _ {1 2} \in [ 0. 4 0, 0. 6 0 ]; \quad u _ {2 1} \geq u _ {1 1} + 0. 2 0;
$$

$$
u _ {2 2} \in [ 0. 2 0, 0. 7 0 ]; u _ {2 2} \geq u _ {1 2} + 0. 1 0;
$$

$$
u _ {3 2} \in [ 0. 0 0, 0. 4 0 ]; \quad u _ {1 3} \geq u _ {2 3}.
$$

The DMA has estimated the credibility of $A_{1}-A_{3}$ as numbers in the interval [0, 1]. Thus the translation of the statements into a credibility base results in the following expressions:

$$
c _ {1} \in [ 0. 1 0, 0. 8 0 ];
$$

$$
c _ {2} \in [ 0. 2 0, 0. 7 0 ];
$$

$$
c _ {3} \in [ 0. 0 0, 0. 5 0 ].
$$

The DMA typically wants the evaluation to result in an ordering of the strategies, complete with measures indicating how desirable they are. An approach using the PMEU is taken in $[12]$ , but as we argue above, the use of it as the sole evaluation principle is not satisfactory and a framework for agent-based decision support should also include qualitative methods. In the following section, some complementary decision rules are discussed.

## 3. Security constraints

In many decision contexts, the DMA may want to exclude particular strategies that, in some way, are too risky. If a DMA would receive only numerically precise information, such exclusions can be dealt with by specifying security constraints using two thresholds – one for the credibility and one for the utility. Then a strategy would be undesirable if it violates both of these thresholds. For instance, a strategy could be considered undesirable if an agent with a credibility above 0.75 reports that the utility of the strategy is below 0.1. However, when the information is numerically imprecise it is not obvious what the meaning of such settings are.

## 3.1. Basic security constraints

The intuition behind security constraints is that they provide thresholds beyond which a strategy is undesirable. Thus, a DMA might regard a strategy as undesirable if it has access to a report in which a credible agent assigns a low utility to the strategy. The first step is to formalise this. We can regard a situation structured in an information frame as a set of objects $\Sigma_{1},\ldots,\Sigma_{m}$ corresponding to the strategies $S_{1},\ldots,S_{m}$ , where each $\Sigma_{i}$ contains k elements $R_{ij}$ . These elements can be thought of as corresponding to reports from the different agents. In this representation $c_{j}$ and $u_{ij}$ correspond to the credibility and utility of the j-th element $R_{ij}$ in $\Sigma_{i}$ respectively. This notation will be used to simplify the presentation below. We also assume an information frame $\langle K(c),S(u)\rangle$ underlying all the definitions in the sequel. Since the agents are not necessarily consistent in their estimates, the first step is to determine the solution sets to $K(c)$ and $S(u)$ .

Definition. A list of numbers $[n_{1},\ldots,n_{s}]$ is a solution vector to a base X containing variables $x_{i}$ , where $i=1,\ldots,s$ , if $n_{i}$ can be consistently substituted for $x_{i}$ in X. The set of solution vectors to a base constitutes the solution set. This set is a convex polytope, i.e. an intersection of a finite number of closed half spaces.

Definition. The function Utility $_{2}$ : $\Sigma_{i}\times[0,1]\rightarrow\{true,false\}$ is defined as follows:

$Utility_{2}(R_{ij},a) = true iff S(u)\cup\{u_{ij}<a\} has a non-empty solution set.$

Otherwise Utility $_{2}(R_{ij},a)=$ false.

Definition. The function Credibility $_{2}$ : $[0,1]\times\Sigma_{i}\rightarrow\{true,false\}$ is defined as follows:

Credibility $_{2}(d,R_{ij})$ = true iff $K(c)\cup\{c_{j}>d\}$ has a non-empty solution set.
Otherwise Credibility $_{2}(d,R_{ij})$ = false.

Definition. The function Undesirable: $\Sigma_{i} \times [0,1] \times [0,1] \to \{\text{true, false}\}$ is now defined as follows:

Undesirable $_{3}(\Sigma_{i},a,d)=$ true iff Utility $_{2}(R_{ij},a)=$ true and Credibility $_{2}(d,R_{ij})=$ true, for some $R_{ij}\in\Sigma_{i}$ .

Otherwise Undesirable $_3(\Sigma_i, a, d) =$ false.

Example (continued). Suppose that the DMA has stipulated that a strategy $S_{i}$ is undesirable iff:

\- the element $R_{ij}$ belongs to $\Sigma_i$ ,

\- the utility of $R_{ij}$ is less than 0.45, and

\- the credibility of $R_{ij}$ is greater than 0.65.

Assume that $R_{12}$ belongs to $\Sigma_{1}$ , that $u_{12}$ is in the interval [0.40, 0.60], and that $c_{2}$ is in the interval [0.20, 0.70]. The value of Undesirable $_{3}(\Sigma_{1}, 0.45, 0.65)$ would now be true.

## 3.2. Reductions

In the example, the security constraints are violated near the boundaries of the credibility and utility intervals respectively. Since the agents are encouraged to be deliberately imprecise, values close to the boundaries seem to be the least reliable ones. Consequently, a problem is that the function Undesirable $_{3}$ is too sensitive to the different interval boundaries in $K(c)$ and $S(u)$ . One way of analysing the intervals is by contracting the information frame to locate critical variables and investigate the stability of the result. Another approach to analysing the result is by using Monte Carlo methods to study the parts of the solution sets of $K(c)$ and $S(u)$ where the strategies are undesirable. Unfortunately, Monte Carlo methods are inefficient and not well-suited for interactive analyses of the information frame, and thus we suggest the use of reductions as the primary method.

The concept of reduction indicates how much the different intervals in the information frame can be reduced before strategies cease to be undesirable. Some emphasis has to be put on the investigation of the effects of decreasing the intervals, since without such an option the set of undesirable strategies is often relatively large. Below, we propose a contraction principle that is reasonable but not the only one possible. For example, a DMA can stipulate that if, for a certain strategy, Utility $_{2}$ is still true when performing an 80% reduction of the strategy base and Credibility $_{2}$ is true when performing a 90% reduction of the strategy base, then the strategy is undesirable.

Example (continued). We investigate how much the different intervals can be decreased while the security constraints are still violated. In this manner we can study the stability of the result. For example, it can be seen that the strategy $S_{1}$ ceases to be undesirable when the left end-point of the interval of $u_{12}$ is increased by 0.05. Consequently, the result above is quite unstable.

By integrating reductions with the procedures in Section 3.1 for handling security constraints, we propose a process taking into account the consistent instances of credibility and utility variables where the security constraints are violated. An algorithm for determining the solution set of a linear system is given in the definition below. We use the set union operation to denote list concatenation and the set difference operation to denote deletion of elements in a list.

Definition. Given a base $X$ containing a list $Z$ of all interval statements $[(c_1 \geq a_1, b_1 \geq c_1), \ldots, (c_n \geq a_n, b_n \geq c_n)]$ in $X$ , $\Omega(X)$ is generated by the following procedure:

(a) Let $X_0 = X$ and $Z_0 = Z$ .

(b) For all interval statements $(c_{i} \geq a_{i}, b_{i} \geq c_{i})$ in the list Z:

Substitute the statement $(c_{i} \geq \inf(\{n_{i}: n_{i}$ is at the $i$ -th position in a solution vector to $X_{i-1}\})$ , $\sup(\{n_{i}: n_{i}$ is at the $i$ -th position in a solution vector to $X_{i-1}\}) \geq c_{i})$ for the interval statement $(c_{i} \geq a_{i}, b_{i} \geq c_{i})$ in the list $Z_{i-1}$ , and call the result $Z_{i}$ . Let $X_{i} = (X_{i-1} - Z_{i-1}) \cup Z_{i}$ .

(c) Let $\Omega(X) = X_{n}$ .

Informally, $\Omega(X)$ is as X, but contains the (in some sense) maximal intervals, where each value in the intervals is a solution relative to X.

Example (continued). The strategy base $S(u)$ contains a number of strategy assessments, e.g., $u_{11} \in [0.50, 0.70]$ , $u_{21} \in [0.10, 0.70]$ , and $u_{21} \geq u_{11} + 0.20$ . Consequently, the greatest value that can consistently be assigned to $u_{11}$ is 0.50, since it is affected by the maximum value of $u_{21}$ (which is 0.70). Similarly, the least value that can consistently be assigned to $u_{21}$ is 0.70. Therefore, a representation $\Omega(S(u))$ of the solution set to this base would include $u_{11} \in [0.50, 0.50]$ , $u_{21} \in [0.70, 0.70]$ , and $u_{21} \geq u_{11} + 0.20$ . Prior to making any calculations at all, we reduce the base so that each value in each interval is a component in a solution vector to the base.

The contraction principle is defined in three parts. First we define a procedure for decreasing the widths of all the intervals in a base while maintaining consistency. The size of the reduction steps could for instance be proportional to the widths of the original intervals.

Definition. X is a system of linear equations, inequalities, and interval statements containing variables $\{x_{1},\ldots,x_{n}\}$ and $D=[d_{i}]$ is a list of n numbers. A reduction of X to $X^{*}$ is performed as follows:

(a) Let $X' = X$ .

(b) For all $x_{i} \in \{x_{1}, \ldots, x_{n}\}$ :

Replace the interval statements $(x_{i}-a_{i}\geq0,-x_{i}+b_{i}\geq0)$ in $X'$ by $(x_{i}-a_{i}-d_{i}\geq0,-x_{i}+b_{i}-d_{i}\geq0)$ , where $d_{i}\in D$ .

(c) Check whether the solution set to $X'$ is non-empty. If this is the case, let $X^{*} = X'$ . Otherwise, let $X^{*} = X$ .

Hence, given a list of $d_{i}$ 's, a reduction decreases the sizes of all the intervals that can possibly be decreased while maintaining a non-empty solution set. This procedure may now be iterated as far as possible. The number $\delta$ in the procedure below should be suitable for the given decision situation.

Definition. X is a system of linear equations, inequalities, and interval statements, and $\delta$ is a number in the interval [0, 0.5]. $[(x_{i}-a_{i}\geq0,-x_{i}+b_{i}\geq0)]$ is the list of interval statements in $\Omega(X)$ , and $D=[d_{i}]$ is a list where $d_{i}=\delta(b_{i}-a_{i})$ .

(a) A $\delta_0$ -reduction of $X$ to $Y_0$ is to let $Y_0 = \Omega(X)$ .

(b) Given a $\delta_{i-1}$ -reduction of $X$ to $Y_{i-1}$ . A $\delta_i$ -reduction of $X$ to $Y_i$ is the reduction of $Y_{i-1}$ to $Y_i$ , where $Y_{i-1} \neq Y_i$ .

Definition. Let X be a system of linear equalities, linear inequalities and interval statements, and let Y be a conjunction of linear inequalities. The function $\text{Contraction}^{\delta}(X,Y)$ is the number $k = \sup(\{s: \text{there is a } \delta_{s} \text{-reduction of } X \cup Y\})$ .

The function determines how far the base can be reduced while maintaining the consistency of the system.

## 3.3. Generalised security constraints

The procedures for handling security constraints can now be generalised by incorporating reductions of the information frame and investigate where the security constraints are violated. If the information frame can be reduced too far according to the DMA, the strategy is undesirable. As before, $\Sigma_{i}$ is the set corresponding to strategy $S_{i}$ . The number a is the threshold for the utility of the $R_{ij}$ :s with respect to the strategy base. The number b is the threshold for the reductions with respect to the strategy base. $^{1}$

Definition: The function SingletonUtility $_{3}$ : $\Sigma_{i}\times[0,1]\times N\to\{true,false\}$ is defined as follows:

SingletonUtility $_3$ ( $R_{ij}, a, b$ ) = true iff

Contraction $^{\delta}\left(S(u),\{u_{ij}<a\}\right)>b.$

Otherwise SingletonUtility $_3$ ( $R_{ij}, a, b$ ) = false.

Similarly, the number d is the threshold for the credibilities of the $R_{ij}$ 's, while e is the threshold for the reductions with respect to the credibility base.

Definition. The function SingletonCredibility $_{3}$ : [0,1] × N × $\Sigma_{i}$ → {true, false} is defined as follows:

SingletonCredibility $_3(d,e,R_{ij})$ = true iff

Contraction $^{\delta}\left(K(c),\{c_{j}>d\}\right)>e.$

Otherwise SingletonCredibility $_3(d, e, R_{ij})$ = false.

These definitions can now be combined into one that uses the four security thresholds together with $K(c)$ and $S(u)$ . This is accomplished by a function that checks whether there is an element $R_{ij}$ in a set $\Sigma_{i}$ which simultaneously fulfils the criteria in the two definitions above.

Definition. The function SingletonUndesirable: $\{\Sigma_{i}\} \times [0,1] \times N \times [0,1] \times N \to \{\text{true, false}\}$ is now defined as follows:

SingletonUndesirable $_{5}$ ( $\Sigma_{i},a,b,d,e$ ) = true iff
SingletonUtility $_{3}$ ( $R_{ij},a,b$ ) = true and
SingletonCredibility $_{3}$ ( $d,e,R_{ij}$ ) = true, for some $R_{ij} \in \Sigma_{i}$ .

Otherwise SingletonUndesirable $_{5}(\Sigma_{i},a,b,d,e)=$ false.

The definitions above generalise the function Undesirable $_{3}$ by incorporating reductions into the procedures in Section 3.1. Nevertheless, the definitions are still unsatisfying because they consider only singletons, i.e. they do not take into account how subsets of $\Sigma_{i}$ 's can make a strategy undesirable. This means that if several agents report that a strategy is too risky (with respect to a certain utility threshold), their total credibility should be considered even if their individual credibilities are too low to make the strategy undesirable. This is handled by the function Undesirable $_{5}$ below. The intuition behind it is that all subsets $\{R_{if},\ldots,R_{ig}\}$ of $\Sigma_{i}$ are considered. Each subset is checked for consistency with the expressions in the strategy base in order to see if the utility of each element in the subset is less than a for a certain reduction threshold b. If this is the case, the credibility of this subset is checked, i.e. it is checked whether the sum of the credibilities for all elements is greater than d for a certain threshold e.

Definition. The function Utility $_{3}$ : $2^{\Sigma_{i}} \times [0,1] \times N \rightarrow \{true, false\}$ is defined as follows:

Utility $_3(\{R_{if}, \ldots, R_{ig}\}, a, b) =$ true iff

$$
\mathrm{I} ^ {\delta} (S (u), \left\{u _ {i f} <   a \right\} \cup \dots \cup \left\{u _ {i g} <   a \right\})
$$

Thus, the function Utility $_{3}$ checks if $u_{ij}<a$ for all of the elements in the set $\{R_{if},\ldots,R_{ig}\}$ can be simultaneously satisfied given the thresholds $a$ and $b$ and the expressions in $S(u)$ .

Definition. The function Credibility $_3$ : $[0,1] \times N \times 2^{\Sigma_i} \to \{true, false\}$ is defined as follows:

Credibility $_{3}(d,e,\{R_{if},\ldots,R_{ig}\})$ = true iff

$$
\text { Contraction } ^ {\delta} \left(K (c), \left\{\left(c _ {f} + \dots + c _ {g}\right) > d \right\}\right) > e.
$$

$$
\text { Credibility } _ {3} (d, e, \{R _ {i f}, \dots , R _ {i g} \}) =
$$

The function checks if the sum $\sum c_{j} > d$ , where the credibilities of all of the elements in the set $\{R_{if}, \ldots, R_{ig}\}$ are summarised, is consistent with the threshold e and with the expressions in $K(c)$ .

Definition. The function Undesirable $_{5}$ : $\{\Sigma_{i}\} \times [0,1] \times N \times [0,1] \times N \to \{\text{true, false}\}$ is now defined as follows:

Undesirable $_{5}$ ( $\Sigma_{i},a,b,d,e$ ) = true iff Utility $_{3}$ ( $\{R_{if},\ldots,R_{ig}\},a,b$ ) = true and Credibility $_{3}$ ( $d,e,\{R_{if},\ldots,R_{ig}\}$ ) = true, for some set $\{R_{if},\ldots,R_{ig}\} \subseteq \Sigma_{i}$ . Otherwise Undesirable $_{5}$ ( $\Sigma_{i},a,b,d,e$ ) = false.

Example (continued). Using the definitions above, we may now investigate to what extent the different strategies are undesirable. Fig. 2 shows, for each strategy and a utility threshold of 0.10, the worst possible credibility assignments consistent with the information frame at different degrees of reduction. In the figure, $K(c)$ and $S(u)$ are reduced by the same degree, i.e. $b = e$ in Undesirable $_{5}$ , but as can be seen from its definition, this is not necessary.

![](/api/attachments/4R5MBHDA/fulltext/images/26276116dcf534403a36f4991d2ca686be9079afae3e0e3d95fb0412a2705551.jpg)  
Fig. 2. Utility threshold 0.10.

![](/api/attachments/4R5MBHDA/fulltext/images/b492f0a5b68e21764c5fef2f556dcc2db9af8451facd6dc5c17aa76db629af98.jpg)  
Fig. 3. Utility threshold 0.20.

From Fig. 2 it can be seen that the strategies $S_{1}$ and $S_{2}$ are not undesirable in any part of the information frame. Strategy $S_{3}$ is undesirable in the original frame and remains so until it is reduced by more than 60%. For instance, when the information frame is reduced by 40%, the greatest joint credibility for this strategy is 0.58.

Figs. 3 and 4 show the evaluations for the utility thresholds 0.20 and 0.50 respectively. As can be seen in Fig. 3, the strategies $S_{1}$ and $S_{2}$ are now undesirable in some parts of the information frame. However, they cease to be undesirable at reductions of at least 20%. Fig. 4 shows that for higher utility thresholds, $S_{3}$ is undesirable regardless of the degree of reduction. Thus, we can see that the result of the evaluation is strongly dependent on boundary values, and consequently they should be further investigated in an sensitivity analysis.

## 3.4. Some extensions

It is also possible to modify the function Utility $_{3}$ above to take care of other criteria and we will briefly discuss some of them. Following that, some classical criteria are considered within the framework.

![](/api/attachments/4R5MBHDA/fulltext/images/ffca6f0868b1ac4a389269800f127e757cb6915285eb08042c57525d173edabf.jpg)  
Fig. 4. Utility threshold 0.50.

1. In analogy to the definition of Undesirable $_{5}$ , a function can be defined which decides that a strategy is undesirable if the elements in $\Sigma_{i}$ are worse than a set $\{R_{ij}\}$ of elements (or a specific $R_{ts}$ ). This definition is especially useful when a DMA is going to evaluate a certain strategy and has access to information concerning a status quo state. ( $\Sigma$ below denotes an arbitrary set of elements $R_{ij}$ .)

The function $U - U_3 \colon 2^{\Sigma} \times 2^{\Sigma_i} \times [0,1] \to \{\text{true, false}\}$ is defined as follows:

$$
\mathrm{U} - \mathrm{U} _ {3} (\{R _ {t _ {1} S _ {1}}, \dots , R _ {t _ {n} S _ {n}} \}, \{R _ {i 1}, \dots , R _ {i k} \}, b) = \text { true }
$$

iff for all $R_{t_jS_j}$ in the set $\{R_{t_1S_1},\ldots ,R_{t_nS_n}\}$ ,

Contraction $^{\delta}\left(S(u),\left\{u_{i1}<u_{t_{i}S_{j}}\right\}\right.$

$$
\cup \dots \cup \left\{u _ {i k} <   u _ {t _ {j} S _ {j}} \right\}) > b.
$$

Otherwise $U - U_3(\{R_{t_1S_1}, \ldots, R_{t_nS_n}\}, \{R_{i1}, \ldots, R_{ik}\}, b) = \text{false.}$

2. Positive criteria can also be introduced by substituting the expressions $u_{ij} < a$ with $u_{ij} > a$ in the procedure Utility $_{3}$ to receive the function Desirable $_{5}$ . This states that a strategy $S_{i}$ is desirable if the elements in $\Sigma_{i}$ are better than a certain utility threshold when $S(u)$ is reduced by a certain amount.

3. In analogy with 1, we may define a criterion which states that a strategy $S_{i}$ is desirable if the elements in $\Sigma_{i}$ are better than a set of $R_{ij}$ 's.

The function U-D\$\_{3}\$: \$2^{\Sigma} \times 2^{\Sigma\_{i}} \times [0,1]^{\nu} \rightarrow \{\text{true, false}\}\$ is defined as follows:

$$
\mathrm{U-D} _ {3} (\{R _ {t _ {1} S _ {i}}, \dots , R _ {t _ {n} S _ {n}} \}, \{R _ {i 1}, \dots , R _ {i k} \}, b) = \text { true }
$$

iff for all $R_{t_jS_j}$ in the set $\{R_{t_1S_1},\ldots ,R_{t_nS_n}\}$ ,

Contraction $\delta (S(u),\{u_{i1} > u_{t_jS_j}\})$

$$
\cup \dots \cup \left\{u _ {i k} > u _ {t _ {j} S _ {j}} \right\}) > b.
$$

Otherwise U-D $_3$ ( $\{R_{t_1S_1}, \ldots, R_{t_nS_n}\}, \{R_{i1}, \ldots, R_{ik}\}, b$ ) = false.

In a similar way the procedures can, with some modifications, be adapted to a number of approaches to decisions under strict uncertainty. Consider a traditional decision model in Fig. 5.

<table><tr><td></td><td> $\mathbf{s}_1$ </td><td> $\mathbf{s}_2$ </td><td>...</td><td> $\mathbf{s}_{\mathbf{n}}$ </td></tr><tr><td> $\mathbf{S}_1$ </td><td> $\mathbf{k}_{11}$ </td><td> $\mathbf{k}_{12}$ </td><td>...</td><td> $\mathbf{k}_{1n}$ </td></tr><tr><td> $\mathbf{S}_2$ </td><td> $\mathbf{k}_{21}$ </td><td> $\mathbf{k}_{22}$ </td><td>...</td><td> $\mathbf{k}_{2n}$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $\mathbf{S}_{\mathbf{m}}$ </td><td> $\mathbf{k}_{\mathbf{m}1}$ </td><td> $\mathbf{k}_{\mathbf{m}2}$ </td><td>...</td><td> $\mathbf{k}_{\mathbf{mn}}$ </td></tr></table>

Fig. 5. A state-consequence matrix.

The possible states $(s_{1},\ldots,s_{n})$ in the model describe a set of mutually exclusive and exhaustive descriptions of the world, not leaving any relevant state out. These states determine the consequences (such as $k_{ij}$ ) of the different strategies $(S_{1},\ldots,S_{m})$ . The true state is the state that does eventually obtain – the description of the actual world. Thus, if we adopt the strategy $S_{2}$ and if $s_{3}$ becomes the true state, consequence $k_{23}$ will occur. The preferences among the consequences are supposed to be expressed by some kind of value function. Below, we assume such a function and denote the value of consequence $k_{ij}$ by $v_{ij}$ . In our terminology, the criterion of [51] can be stated as follows:

1. Set a threshold by choosing an index $V_{i} = \min \{v_{ij} : j = 1, \ldots, n\}$ .

2. Choose $S_{k}$ such that its index $V_{k}$ is given by $V_{k} = \max \{V_{i}: i = 1, \ldots, m\}$ .

This is a very pessimistic criterion; the strategy that should be chosen is the one that gives the best result if the worst possible outcome will obtain for each strategy. The criterion is also known as the maximin utility criterion and originates from Wald's work within game theory.

We can now adapt the framework described above to also include this decision rule in the sense that the worst report(s) of each strategy are considered. First we make the following definitions.

Definition. U-Max $_1(\Sigma_i)$ is the set $\{R_{is} \in \Sigma_i: S(u) \cup \{u_{is} > u_{it}\}$ has a non-empty solution set for every $t \neq s\}$ .

Definition. U-Min $_1(\Sigma_i)$ is the set $\{R_{is} \in \Sigma_i: S(u) \cup \{u_{is} < u_{it}\}$ has a non-empty solution set for every $t \neq s\}$ .

Wald's maximin principle is now implemented by using the function U-Min $_1$ to determine the minimal element (if there is a unique one) in $\{R_{i1},\ldots,R_{ik}\}$ for each strategy $S_i$ (denote it by $R_{ik_i}$ ), and by using the function U-Max $_1$ to determine the maximal elements in $\{R_{1k_1},\ldots,R_{mk_m}\}$ .

The primary problem with this implementation is that the set of minimal elements in $\{R_{i1},\ldots,R_{ik}\}$ usually contains more than one element. One solution is to demand that for every i, $\Sigma_{i}$ must have a least element with respect to the utilities involved. If this requirement is not fulfilled, a procedure for decreasing the number of elements in the set of strategies can be defined by using reductions as before. The same applies to determining the maximal elements in $\{R_{1k_{1}},\ldots,R_{mk_{m}}\}$ . This is accomplished by the following definitions:

Definition. U-Min $_2$ ( $\Sigma, b$ ) is the set $\{R_{ij} \in \Sigma$ : for all $t \neq j$ , Contraction $^{\delta}(S(u), \{u_{ij} < u_{it}\}) > b\}$ .

Definition. U-Max $_{2}(\Sigma,b)$ is the set $\{R_{ij}\in\Sigma\colon$ for all $t\neq j$ , Contraction $^{\delta}(S(u),\{u_{ij}>u_{it}\})>b\}$ .

By using these definitions we can investigate which maximal or minimal elements in the respective sets can be eliminated with respect to a threshold b. A more optimistic approach is taken in [24]. It recommends a mixture of an optimistic and a pessimistic attitude:

1. Select a constant $\alpha \in [0,1]$ as the pessimism-optimism index.

2. Let $M_{i} = \max \{v_{ij}, j = 1, \ldots, n\}$ and $V_{i} = \min \{v_{ij}, j = 1, \ldots, n\}$ .

3. Choose $S_{k}$ such that

$$
\alpha V _ {k} + (1 - \alpha) M _ {k} = \max \left\{\alpha V _ {i} + (1 - \alpha) M _ {i} \right\}.
$$

Note that if $\alpha=1$ , this is again the maximin utility criterion, whereas if $\alpha=0$ , it is the so-called maximax utility criterion. Different ways of choosing appropriate pessimism–optimism indices have been presented, but we do not enlarge on that subject here.

By using the function U-Max $_{2}$ to determine $\max(u_{i1},\ldots,u_{ik})$ and then applying the function U-Max $_{2}$ to determine $\max(u_{1k_{1}},\ldots,u_{mk_{m}})$ , the maxi-max return criterion is achieved. This can be generalised to take account of Hurwicz's criteria by applying the functions U-Max $_{2}$ and U-Min $_{2}$ to evaluate all expressions:

$$
\begin{array}{l} \alpha \left(\min \left(u _ {1 1}, \dots , u _ {1 k}\right)\right) + (1 - \alpha) \left(\max \left(u _ {1 1}, \dots , u _ {1 k}\right)\right), \\ \vdots \end{array}
$$

$$
\alpha (\min (u _ {m 1}, \dots , u _ {m k})) + (1 - \alpha) (\max (u _ {m 1}, \dots , u _ {m k})).
$$

Savage's minimax regret criterion [46] can be implemented in the same manner as above, after modelling the problem as a state-consequence matrix [25]. The minimax regret criterion was first suggested as an improvement over Wald's maximin utility criterion. In Savage's own words ([47], p. 164):

“[...] the minimax rule recommends the choice of such an act that the greatest loss that can possibly accrue to it shall be as small as possible”.

This can be formalised as follows:

1. Let $r_{ij} = \max \{v_{sj}, s = 1, \dots, m\} - v_{ij}$ .

2. Let $V_{i} = \max \{r_{ij}, j = 1, \ldots, n\}$ .

3. Choose $S_{k}$ such that $V_{k} = \min \{V_{i}: i = 1, \dots, m\}$ .

This concludes our exposition of rules to integrate into a security constraint framework, but it does in no way exhaust the possibilities. By using suggestions such as those above, the decisions made by the DMA will be more reliable and predictable than if security constraints were not imposed on the reports. The trust the DMA can put in the results will increase considerably as it is able to set the constraints according to its appreciation of the particular decision problem.

## 4. Concluding remarks

We have shown how a decision making agent may analyze and evaluate informal and numerically imprecise reports made by different autonomous agents when determining which strategies to exclude because they are undesirable. The approach considers a decision problem with respect to the contents and the credibilities of the received reports. These two aspects are modelled in an information frame consisting of two systems of inequalities and interval statements. The strategies are evaluated relative to a set of security constraints considering how risky the strategies are. Moreover, it is investigated in which parts of the solution sets to the information frame those conditions are met. This is accomplished by introducing reductions as a complement to Monte Carlo methods. The contraction indicates how much the different intervals in the information frame can be reduced before strategies cease to be undesirable. In this manner it is possible to investigate critical variables and the stability of the result. Different suggestions of decision rules have been investigated, but we have also noted that these are not the only possible ones and the proposed constraint framework could use other decision criteria as well. When strategies violating the security constraints have been excluded, quantitative methods can be of importance.

We have also argued that there is no universal rule with which rationality could be equated. Instead, a successful agent must be good at analysing results from a set of reasonable decision rules. Such analyses should ideally exploit several decision rules shown appropriate for the particular domain of interest. By studying the properties of the solution space corresponding to different strategies as evaluated by different decision rules, and by conducting sensitivity analyses of the result, the decision making agent will be able to gain a good understanding of the decision situation and the merits of each strategy.

## References

[1] M. Allais, Fondements d'une Théorie Positive des Choix Comportant un Risque et Critique des Postulats et Axioms de L'Ecole Americaine, D. Reidel, Dordrecht, 1953.

[2] C. Bicchieri, M.L.D. Chiara, Preface, in: C. Bicchieri, M.L.D. Chiara (Eds.), Knowledge, Belief, and Strategic Interaction, Cambridge University Press, Cambridge, 1992, pp. vii–xii.

[3] M. Boman, L. Ekenberg, Eliminating paraconsistencies in 4-valued cooperative deductive multidatabase systems with classical negation, in: Proceedings of Cooperating Knowledge Based Systems, 1994, pp. 161–176.

[4] M. Boman, L. Ekenberg, Decision making agents with relatively unbounded rationality, Invited Paper in: Proceedings of DIMAS'95, 1995, pp. I/28–I/35.

[5] A.H. Bond, L. Gasser, Readings in Distributed Artificial Intelligence, Morgan Kaufmann, Los Altos, CA, 1988.

[6] R.A. Brooks, A robust, layered control system for a mobile robot, IEEE Journal on Robotics and Automation 2 (1986) 14–23.

[7] G. Choquet, Theory of capacities, Université de Grenoble. Annales de l'Institut Fourier 5 (1953–54) 131–295.

[8] A.P. Dempster, Upper and lower probabilities induced by a multivalued mapping, Annals of Mathematical Statistics 38 (1967) 325–339.

[9] L. Ekenberg, M. Boman, M. Danielson, A tool for coordinating autonomous agents with conflicting goals, in: Proceedings of ICMAS'95, AAAI/MIT Press, Cambridge, MA, 1995, pp. 89–93.

[10] L. Ekenberg, M. Danielson, A support system for real-life decisions in numerically imprecise domains, in: Proceedings of the International Conference on Operations Research '94, Springer, Berlin, 1994, pp. 500–505.

[11] L. Ekenberg, M. Danielson, A tool for handling uncertain information in multi-agent systems, in: Proceedings of MAA-MAW'94, Lecture Notes in Computer Science, Springer, Berlin, 1995.

[12] L. Ekenberg, M. Danielson, M. Boman, From local assessments to global rationality, to appear in International Journal of Intelligent and Cooperative Information Systems.

[13] L. Ekenberg, S. Oberoi, I. Orci, A cost model for managing information security hazards, Computers and Security 14 (1995) 707–717.

[14] P. Fishburn, Subjective expected utility: a review of normative theories, Theory and Decision 13 (1981) 139–199.

[15] J.R. Galliers, A theoretical framework for computer models of cooperative dialogue, acknowledging multi-agent conflict, Ph.D. thesis, Computer Laboratory, University of Cambridge, Cambridge, 1989.

[16] P.J. Gmytrasiewicz, E.H. Durfee, Elements of a utilitarian theory of knowledge and action, in: Proceedings of 13th IJCAI, 1993, pp. 396–402.

[17] I.J. Good, Subjective probability as the measure of a non-measurable set, in: P. Suppes, E. Nagel, A. Tarski (Eds.), Logic, Methodology, and the Philosophy of Science, Stanford University Press, Stanford, CA, 1962, pp. 319–329.

[18] J. Green, B. Jullien, Ordinal independence in nonlinear utility theory, Journal of Risk and Uncertainty 1 (1988) 355–387.

[19] P. Gärdenfors, N.-E. Sahlin, Unreliable probabilities, risk taking, and decision making, Synthese 53 (1982) 361–386.

[20] O. Hagen, Separation of cardinal utility and specific utility of risk in theory of choices under uncertainty, Statsøkonomisk Tidsskrift 3 (1969) 81–107.

[21] I.N. Hernstein, J. Milnor, An axiomatic approach to measurable utility, Econometrica 21 (1953) 291–297.

[22] P.J. Huber, The case of Choquet capacities in statistics, Bulletin of the International Statistical Institute 45 (1973) 181–188.

[23] P.J. Huber, V. Strassen, Minimax tests and the Neyman-Pearsons lemma for capacities, Annals of Statistics 1 (1973) 251–263.

[24] L. Hurwicz, Optimality criteria for decision making under ignorance, Cowles Commission Discussion Paper 370, 1951.

[25] R. Jeffrey, The Logic of Decision, University of Chicago Press, Chicago, IL, 1983.

[26] P. Laplace, Essai Philosophique sur les Probabilités, 5th ed., 1825. Paris Translation published by Dover, New York, 1952.

[27] I. Levi, On indeterminate probabilities, The Journal of Philosophy 71 (1974) 391–418.

[28] I. Levi, Feasibility, in: C. Bicchieri, M.L.D. Chiara (Eds.), Knowledge, Belief, and Strategic Interaction, Cambridge University Press, Cambridge, 1992, pp. 1–20.

[29] G. Loomes, R. Sudgen, Regret theory: an alternative theory of rational choice under uncertainty, The Economic Journal 92 (1982) 805–824.

[30] P.-E. Malmnäs, Axiomatic justification of the utility principle, Research Report HSFR 677/87, 1990.

[31] P.-E. Malmnäs, Axiomatic justification of the utility principle, Synthese 99 (1994) 233–249.

[32] P.-E. Malmnäs, Towards a mechanization of real life decisions, in: D. Prawitz, D. Westerståhl (Eds.), Logic and Philosophy of Science in Uppsala, Kluwer Academic Publishers, Dordrecht, 1994.

[33] P.-E. Malmnäs, Evaluations, preferences, choice rules, Department of Philosophy, Stockholm University, 1996.

[34] E.F. McClennen, Rational choice in the context of ideal games, in: C. Bicchieri, M.L.D. Chiara (Eds.), Knowledge, Belief, and Strategic Interaction, Cambridge University Press, Cambridge, 1992, pp. 47–60.

[35] J. Milnor, Games against nature, in: R. Thrall, C. Coombs, R. Davis (Eds.), Decision Processes, Wiley, New York, 1954, pp. 49–59.

[36] J. von Neumann, O. Morgenstern, Theory of Games and Economic Behavior, 2nd ed., Princeton University Press, Princeton, NJ, 1947.

[37] A. Newell, The knowledge level, AI Magazine, Summer (1981) 1–20.

[38] G. Oddie, P. Milne, Act and Value, Theoria 57 (1990) 42–76.

[39] J. Quiggin, A theory of anticipated utility, Journal of Economic Behavior and Organization 3 (1982) 323–343.

[40] W. Rabinowicz, Tortuous labyrinth: noncooperative normal-form games between hyperrational players, in: C. Bicchieri, M.L.D. Chiara (Eds.), Knowledge, Belief, and Strategic Interaction, Cambridge University Press, Cambridge, 1992, pp. 107–126.

[41] F.P. Ramsey, Truth and probability, in: D.H. Mellor (Ed.), Foundations: Essays in Philosophy, Logic, Mathematics and Economics, Routledge & Kegan Paul, London, 1978, pp. 58–100.

[42] J.S. Rosenschein, The role of knowledge in logic-based rational interactions, in: Proceedings of Seventh Phoenix Conference on Computers and Communications, 1988, pp. 497–504.

[43] J.S. Rosenschein, Consenting agents: negotiation mechanisms for multi-agent systems, in: Proceedings of 13th IJ-CAI, 1993, pp. 792–799.

[44] J.S. Rosenschein, M.R. Genesereth, Deals among rational agents, in: Proceedings of 9th IJCAI, 1985, 91–99.

[45] S. Russell, E. Wefald, Principles of metareasoning, in: Proceedings of KR-89, 1989, pp. 400–411.

[46] L. Savage, The theory of statistical decision, Journal of the American Statistical Association 46 (1951) 55–67.

[47] L. Savage, The Foundations of Statistics, 2nd ed., Dover, New York, 1972.

[48] H.A. Simon, Administrative Behaviour, 3rd ed., Free Press, New York, 1976.

[49] C.A.B. Smith, Consistency in statistical inference and decision, Journal of the Royal Statistic Society. Series B 23 (1961) 1–25.

[50] W. Stirling, Multi agent coordinated decision-making using epistemic utility theory, in: Castelfranchi, Werner (Eds.), Artificial Social Systems, Lecture Notes in AI, vol. 830, Springer, Berlin, 1994, pp. 164–183.

[51] A. Wald, Statistical Decision Functions, Wiley, New York, 1950.

[52] M. Yaari, The dual theory of choice under risk, Econometrica 55 (1987) 95–115.

![](/api/attachments/4R5MBHDA/fulltext/images/b85638528c2b75e18b3928ea145b503a60ec1c0dfccf0c25535eb153244a0a1d.jpg)

![](/api/attachments/4R5MBHDA/fulltext/images/be8bf66a03f97dba8908e97ceb5a3946ea3177f8d706ee8a9d536c6ee985015c.jpg)

Magnus Boman is a senior researcher in the DECIDE group at the Department of Computer and Systems Sciences (DSV) at Stockholm University and the Royal Institute of Technology. He has recently co-written a textbook on conceptual modelling and will this year edit a special issue on multi-agent rationality for the journal Robotics and Autonomous Systems. Boman is also scientific co-chair for MAAMAW (Modelling Autonomous Agents in a Multi-Agent World).

![](/api/attachments/4R5MBHDA/fulltext/images/a645a229de6950ab1c9269736a6ae7036b5570803c68d15475794f0b99827127.jpg)

Mats Danielson will earn his Ph.D. in Computer Science at DSV in the spring of 1997. He has more than ten years experience as a computer consultant in industry, designing large systems. Danielson is a member of the DECIDE group at DSV.

Love Ekenberg is a senior researcher in the DECIDE group at DSV. He is currently a guest researcher at IIASA (International Institute for Applied Systems Analysis), Vienna. Ekenberg has several years experience as a consultant in formal methods and verification of safety critical systems.
