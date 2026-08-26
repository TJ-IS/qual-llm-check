---
otero_id: 13828
otero_key: "34CRZX4F"
title: "Mechanism design for software agents with complete information"
authors: "Thomas C. O'Connell; Richard E. Stearns"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.10.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Mechanism design for software agents with complete information \$

Thomas C. O’Connell<sup>a,</sup>\*<sup>,1</sup>, Richard E. Stearns

<sup>a</sup> Department of Mathematics and Computer Science, Skidmore College, Saratoga Springs, NY 12866,USA <sup>b</sup> Department of Computer Science, University at Albany, SUNY, Albany, NY 12222,USA

Available online 29 November 2003

## Abstract

We investigate the mechanism design problem when the agents and the mechanism have computational restrictions. In particular, we examine how results in the mechanism design literature are affected when the social choice rule requires the mechanism to solve a computationally difficult optimization problem. Both dominant strategy and Nash implementation are considered for a multiagent version of the maximum satisfiability problem. We show that the best a mechanism can guarantee is that at least half of the maximum number of simultaneously satisfiable agents will be satisfied by the outcome. Our analysis highlights some of the difficulties that arise in applying results from mechanism design to computational problems. In particular, our results show that using approximation in multiagent settings can be much less successful than in traditional computational settings because of the game theoretic guarantees required of the outcomes. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Algorithmic mechanism design; Approximation algorithms; Game theory; Implementation theory

## 1. Introduction

With the advent of Internet computing and electronic commerce, there has been increasing interest in computational systems, referred to as multiagent systems, that involve the interaction of many different computer programs. These programs, or software agents, may be written by different people or companies with different goals in mind. In other words, the programs can be viewed as self-interested. Not surprisingly, the design and analysis of multiagent systems involves the tools of game theory and mechanism design (see Refs. [12,18,33,35] for examples). Developing a clear understanding of the computational issues involved in mechanism design should facilitate its use in multiagent system design. Therefore, in this paper, we consider how placing computational limitations on the agents and the mechanism affects classic results in the mechanism design literature. In particular, we investigate the effect of restricting the agents and the mechanism to polynomial time computation. (Section 3 provides details on exactly how this is done.) To focus our investigation, we consider a particular problem which we call Multiagent MAXSAT and restrict ourselves to complete information environments. In Multiagent MAXSAT, each agent’s preferences over the set of possible outcomes can be described by a disjunction over negated and unnegated Boolean variables.

For example, consider a warehouse inhabited by several robots that have different and possibly conflicting goals. (This example is based on an example from Ref. [33].) Each robot is concerned only with satisfying its own goal and does not care whether any of the other robots satisfy their goals. Rather than spending time negotiating with one another when a conflict arises, the robots rely on an outside arbitrator to resolve the conflict quickly and equitably. The arbitrator is referred to as a mechanism. The mechanism’s only goal is to have the outcome of its decisions satisfy some measure of social desirability called a social choice rule. If the mechanism is successful, it is said to implement the social choice rule. In this case, let the mechanism’s goal be to satisfy as many of the robots as possible. In other words, from the point of view of the mechanism, any outcome that satisfies the maximum number of simultaneously satisfiable robots is a good outcome and any other outcome is a bad outcome. Suppose in this warehouse there are n blocks $B _ { 1 }$ through $B _ { n }$ and one table. We can describe the state of the world using Boolean variables. Let $x _ { i } =$ true represent $B _ { i }$ being on the table and let $x _ { i } =$ false represent $B _ { i }$ being on the floor for $i = 1 , . . . , n .$ . If the robots’ goals are restricted to those that can be represented by a disjunction over the Boolean variables and their negations, this is an instance of a multiagent MAXSAT problem.

The problem of assigning truth values to a set of variables so that the number of satisfied disjunctions is maximized is known to be a computationally difficult problem (see Ref. [6]). According to the widely held belief of computer scientists and logicians, namely that P p NP, it would be impossible for the mechanism to maximize the number of satisfied agents in every instance if the agents and the mechanism are limited to polynomial time computation. Therefore, any polynomial time mechanism must settle for outcomes that are approximately optimal. (Readers unfamiliar with the P vs. NP question should refer to the Appendix A for an explanation.)

The main results of this paper are as follows:

(1) The revelation principle states that, if there is a mechanism that implements a social choice rule, then there is a truthful revelation mechanism that implements the social choice rule, i.e., there is a mechanism that asks the agents to declare their preferences and for which truthful declaration is an equilibrium strategy (see Section 4). The revelation principle allows the discussion to be restricted to social choice rules that are implementable by truthful revelation mechanisms. We show that the revelation principle applies when the mechanism and the agents are restricted to polynomial time but does not apply when the mechanism is restricted and the agents are not. This implies that, in the latter situation, we cannot restrict our attention to truthfully implementable social choice rules.

(2) We provide a mechanism with a non-dictatorial outcome function that implements MAXSAT in dominant strategies. The mechanism runs in polynomial time but the agents require nonpolynomial time to compute their dominant strategies. (Throughout this paper, we assume that P p NP.) This result is of interest because a classic theorem known as the Gibbard –Sattherwaite theorem states that in many situations, dominant strategy implementation with nondictatorial outcome functions is impossible. Gibbard –Sattherwaite does not apply to Multiagent MAXSAT.

(3) We provide a mechanism such that all dominant strategy equilibrium outcomes satisfy at least half of the agents. In this case, the mechanism and the agents use only polynomial time.

(4) We provide a polynomial time mechanism that guarantees that each Nash equilibrium outcome satisfies at least half of the agents. This mechanism is in many ways superior to the mechanism we developed for dominant strategy implementation.

(5) We show that in the case of strong implementation in dominant strategy, Nash, undominated Nash or subgame perfect equilibrium, it is impossible to guarantee that the equilibrium outcomes will satisfy more than half of the maximum number of simultaneously satisfiable agents. In contrast, there are approximation algorithms for the nonmultiagent version of MAXSAT that guarantee that 3/4 of the maximum number of simultaneously satisfiable agents will be satisfied (see Refs. [1,8,40]). This result suggests that we will be much less successful using approximation to overcome computational complexity in self-interested multiagent environments than in traditional computational environments.

The Multiagent MAXSAT problem is simplistic in that each agent is limited to preferences defined by simple unweighted disjunctions. However, since most of our results demonstrate the difficulty of designing mechanisms for such a restricted version of the problem, these difficulties will carry over to more realistic models. The environment we study is also somewhat unrealistic since we assume the agents have complete information, i.e., we assume each agent knows every other agent’s goal. However, understanding the problems that arise in the complete information environment should help to provide a foundation for future work in incomplete information environments (see Refs. [16,29] for surveys of mechanism design in incomplete information environments).

## 1.1. Related work

A computational formulation of the mechanism design problem is presented by Nisan and Ronen in Ref. [23] (see also Ref. [25]). They studied dominant strategy implementation for a task scheduling problem in which there is a set of tasks to be distributed among a group of agents in such a way that the time at which the last task is completed is minimized. The agents, who prefer to do no work at all, have different times in which they can perform each task. These times are unknown to the mechanism. The task scheduling problem is a computationally difficult problem. Therefore, even if the agents truthfully reveal their times to the mechanism, a mechanism restricted to polynomial time computation cannot always find an optimal task distribution. The best the mechanism can hope for is to find an approximately optimal task distribution. An ‘‘approximation’’ mechanism is provided in Ref. [23] such that each agent’s unique dominant strategy is to truthfully inform the mechanism of their times. In Ref. [24], it is shown that, under rather mild assumptions of what constitutes a reasonable social rule, dominant strategy implementation of reasonable social choice rules that approximately maximize the sum of the agents’ utilities is impossible. Restricted conditions under which such an approximation mechanism can be found are provided in Ref. [38]. Approximation in the context of combinatorial auctions is studied in Ref. [13].

All of the papers mentioned above consider only dominant strategy implementation. A dominant strategy is a strategy that gives the agent his best outcome regardless of what the other agents do. This makes dominant strategy implementation desirable since we can be very confident that agents will play dominant strategies when they can. However, because of the Gibbard –Sattherwaite theorem, dominant strategy implementation in general environments is often impossible (see Section 5). Therefore, the papers above, like much of the work in dominant strategy implementation, restrict the environment to be quasilinear. A quasilinear environment is one in which there is money (or another good) that can be transferred among the agents. An agent’s utility function in such an environment is simply the value he places on the outcome plus the amount of money he receives in transfer.

Since there may be problems of interests for which the environments are not quasilinear, understanding the implications of computational limitations for mechanism design in non-quasilinear environments is important. Without the quasilinear assumption, dominant strategy implementation often must be abandoned in favor of other forms of implementation. For complete information environments, the most widely studied of these is Nash implementation. We consider both dominant strategy and Nash implementation for Multiagent MAXSAT. We also briefly consider undominated Nash and subgame perfect implementation.

Another difference between our work and the work cited above is that the latter studies only truthful revelation mechanisms. For these mechanisms, the agents have no computation to perform. They simply pass their preferences unchanged to the mechanism. In our work, the agents’ computation time plays a significant role in the results. (In Ref. [24], the agents computational abilities are considered in trying to overcome their impossibility results.)

This paper can also be considered a contribution to the mechanism design literature on bounded rationality. In Ref. [19], it is pointed out that bounded rationality has received little attention in the mechanism design community. We believe that computer science provides a rich set of tools for modeling bounded rationality. Ideas from computer science have been used previously by game theorists and computer scientists studying bounded rationality in repeated games, see Refs. [3,21,22,27,31,37].

## 1.2. Outline

Section 2 provides a short review of mechanism design and formally defines the Multiagent MAXSAT problem as a computational problem. Section 3 formalizes the idea of a polynomial time mechanism. Section 4 discusses polynomial time revelation mechanisms. Sections 5 and 6 look at designing polynomial time mechanisms using dominant strategy and Nash equilibrium, respectively, for Multiagent MAXSAT. Section 7 provides a proof that the best a mechanism can guarantee is that half of the maximum number of simultaneously satisfiable agents will be satisfied. Since some readers may not be familiar with the relevant complexity concepts from computer science, we have included an appendix that briefly explains these concepts.

## 2. Motivation and definitions

The mechanism design problem is intended to model situations in which a set of self-interested agents must come to a collective decision. The designer of the decision making process would like the decision to be good for the society as a whole as defined by a social choice rule. The way the collective decision is made is that each agent sends a message to a decision making procedure. This decision making procedure then selects an outcome based on the messages sent by the agents. The intent of the decision making procedure is to produce a socially desirable outcome. Each agent, being self-interested, may prefer outcomes that are not socially desirable. Therefore, each agent will try to manipulate the decision making procedure into choosing outcomes that are better for the agent at the expense of the other agents. The ‘‘mechanism design problem’’ is the problem of designing the message sets and the selection rules so that, if the agents choose their messages rationally, the selected outcome is one of the outcomes defined by the social choice rule to be a good outcome. ‘‘Selecting rationally’’ means that the selected messages satisfy some equilibrium condition. The design problem is complicated by the fact that the agents are expected to select a message based on their own selfinterest rather than a message most useful for computing an outcome best for society. For surveys on this subject, see Refs. [14–16,19]. Here we deal with the additional complication that, even if the agents’ messages perfectly reflected their true preferences, the best outcome may be difficult to compute. In other words, even if the decision making procedure knew exactly what each agent wanted, it would be difficult to compute a good outcome.

The mechanism design problem is defined formally as follows.

Definition 2.1 . A mechanism design problem consists of

(1) a finite set of outcomes;

(2) a finite set of agents;

(3) for each agent, a preference set, which is a set of possible preference relations on the set of outcomes (a vector of preference relations, one from each agent’s set of preferences, is called a preference profile);

(4) a social choice rule which specifies, for each preference profile, a nonempty set of outcomes which are considered desirable from a social standpoint.

Intuitively, a preference set represents the set of preference relations that an agent might have. A preference profile represents the preference relations that the agents actually do have. The social choice rule says which outcomes are good from society’s viewpoint given a profile of the agents’ true preferences. The concept of a ‘‘mechanism for a mechanism design problem’’ is defined separately.

Definition 2.2. A mechanism for a mechanism design problem consists of

(1) a message set for each agent;

(2) an outcome function which is a mapping from the set of message vectors (one component for each agent) to the set of outcomes.

When a mechanism is imposed on a mechanism design problem, the result is a kind of a ‘‘game’’. At the start of the game, each agent is given a preference relation from his preference set. In the complete information case studied here, the agents are also informed about the preferences of the other agents. The agents each send a message to the mechanism which computes an outcome using the specified outcome function. The objective of the design problem is to design the mechanism so that (if agents play rationally) the computed outcome is an outcome preferred by the social choice rule.

We next define a MAXSAT mechanism design problem instance for which the outcomes are truth assignments to a set of Boolean variables and the agents’ preferences are determined by clauses. A clause is a disjunction of negated and unnegated Boolean variables. For a given clause, an agent prefers assignments which satisfy the clause to assignments which do not. The agent is indifferent among assignments which satisfy the clause and indifferent among assignments which do not. For example, if an agent’s preference relation is determined by the clause (x\_y\_z¯), the agent prefers assignments which assign x or y the value true or which assign z the value false.

Definition 2.3. A MAXSAT mechanism design problem instance consists of the following:

(1) the set of outcomes is the set of assignments to some specified finite set of Boolean variables;

(2) the agent set is some specified finite set;

(3) for each agent, the preference set is the set of clauses on the Boolean variables (and a preference profile is therefore specified by a vector of clauses);

(4) the social choice rule specifies that, for each preference profile h, any outcome that maximizes the number of satisfied clauses in h is socially desirable.

Notice that, to specify a MAXSAT mechanism design problem instance, one needs only to specify a list of variables and the number of agents. The preference sets and social choice rule are then implied by the definition. The outcome function defined by a mechanism for a MAXSAT problem instance is a mapping of message vectors (a finite set) into a set of variable assignments (also a finite set). From the perspective of computer science, this function can be computed in constant time where the constant is the maximum time taken over the finite set of possible inputs. We are not interested in such one-instance mechanisms. Instead we are interested in mechanisms which apply to a set of problem instances. The outcome function for such a mechanism must have as input both a description of a problem instance and a message vector for that instance. When these multiinstance mechanisms handle an infinite set of instances, one can sensibly ask how the outcome function’s computation time behaves as a function of input size. Therefore, we also define a mechanism for a set of mechanism design problem instances below. Although most of the mechanism design literature is in fact about mechanisms for sets of mechanism design problem instances, it has usually been unnecessary for these papers to make such a careful distinction between mechanisms for a particular mechanism design problem instance and mechanisms for a set of mechanism design problem instances. It is critical for us to do so here.

Definition 2.4 . A mechanism for a set S of mechanism design problem instances consists of the following:

(1) for each mechanism design problem instance in S, a message set for each agent;

(2) an outcome function which maps a problem instance p<sup>a</sup>S and a message vector for p (one component for each agent) to the an outcome from the set of outcomes.

Note that the outcome function of a ‘‘mechanism for a set of mechanism design problem instances’’ has two kinds of parameters: parameters describing an instance of the mechanism design problem and parameters for describing a message vector. The main topic of this paper is designing mechanisms for the set of MAXSAT mechanism design problem instances. We refer to this as the Multiagent MAXSAT problem. In this case, the description of the mechanism design problem instance supplied to the output function consists of a list of Boolean variables and the number of agents. The number of agents is actually redundant information since the procedure for computing outcomes can infer this number from the number of components in the message vector. This is not the case for the Boolean variables, however, since there is nothing that requires the message sets to refer to the Boolean variables at all.

Throughout the remainder of this paper, we use the term mechanism to refer to a mechanism for a set of mechanism design problems. This requires us to modify many of the standard definitions and results from the mechanism design literature so that they take into account the problem instance. In particular, we generalize the definition of a social choice rule to be a mapping of a problem instance and a preference profile for that problem instance to a set of socially desirable outcomes. For example, for Multiagent MAXSAT, we define the social choice rule as follows.

Definition 2.5. For any problem instance $p$ in the set of MAXSAT mechanism design problem instances and any preference profile $\theta$ for $p ,$

$$
\begin{array}{l} \text { MAXSAT } (p, \theta) \\ = \{t: t \text {   is   a   truth   assignment   to   the   variables } \\ \text { listed   in   } p \text {   that   satisfies   } N ^ {*} (\theta) \text {   clauses } \} \end{array}
$$

where $N ^ { * } ( \theta )$ is the maximum number of simultaneously satisfiable clauses in h.

There are different degrees to which a mechanism can succeed in satisfying a social choice rule. These are defined as follows.

Definition 2.6. Let F be a social choice rule for a set of mechanism design problem instances. Given a mechanism $T ,$ let $E ( p , \ \theta )$ be the set of equilibrium outcomes for a problem instance $p$ and a preference profile h. We say:

(1) C implements F if $E ( p , \theta ) \cap F ( p , \theta ) \neq \emptyset$ for all $p$ and h.

(2) C strongly implements F if $\emptyset \neq \operatorname { E } ( p , \theta ) \subseteq F ( p , \theta )$ for all $p$ and h.

(3) C fully implements F if $E ( p , \theta ) = F ( p , \theta )$ for all $p$ and h.

If multiple equilibria exist, it might be difficult to argue that one equilibrium will be played while another will not since all equilibria are equally rational according to any particular equilibrium criterion. The definition of implementation does not exclude the possibility of undesirable equilibrium outcomes.

Strong implementation eliminates mechanisms that do not guarantee that every equilibrium outcome is socially desirable. Full implementation ensures that not only are all equilibrium outcomes socially desirable but all socially desirable outcomes are achievable as equilibrium outcomes as well. Most of the economics literature on Nash implementation is concerned with full implementation. One reason for this, according to Maskin and Sjo¨stro¨m (Ref. [16], p. 4), is that the theory of strong implementation is ‘‘subsumed by the theory of full implementation since [strong]<sup>2</sup> implementation of $F$ is equivalent to full implementation of some sub-correspondence of $F _ { \cdot } ^ { \prime \prime }$ For our purposes, maintaining a distinction seems more appropriate. In line with the philosophy of approximation algorithms, we want to guarantee that all outcomes reach some threshold of acceptability. We are not necessarily concerned with making all acceptable outcomes possible. Therefore, in designing mechanisms to control the interactions of a group of software agents, we consider the mechanism successful if it achieves strong implementation. However, we return to this discussion in Section 6 where we provide some justification for trying to achieve full implementation.

## 3. Polynomial time mechanisms

An algorithm is said to run in polynomial time if there is a polynomial $q$ such that, for every possible input, the algorithm produces an output in no more than q(n) primitive computational steps where n is the size of the input. (For more details on this concept, see Refs. [5,6,9].) There are two computational processes to consider for Multiagent MAXSAT.

(1) The mechanism must compute the outcome function which, as described in the previous section, takes the description of the problem instance and the message vector passed by the agents as input.

(2) The agents must compute strategy functions which take a description of the problem instance and a description of the preference profile as input.

In the case of outcome functions and strategy functions for Multiagent MAXSAT, ‘‘polynomial in the input $\mathrm { s i z e } ^ { \mathbf { , } \mathbf { , } }$ is equivalent to ‘‘polynomial in the number of Boolean variables and the number of agents.’’ The number of literals in each clause is bounded by twice the number of variables so the size of the input to the strategy functions is polynomial in the number of variables and the number of agents. Under the reasonable assumption that the message lengths are polynomial in the number of variables and the number of agents, the entire input to the outcome function is so bounded. This assumption about message lengths must hold if the messages were produced by strategy functions in polynomial time.

We consider implementation in dominant strategy and Nash equilibrium which are defined below. In these definitions and in the remainder of this paper, $\nu _ { i }$ denotes the i-th component of a vector v while $\nu _ { - i }$ denotes the vector v with the i-th component removed. We use $( \nu _ { i } ^ { \prime } , \nu _ { - i } )$ to represent the vector v with the i-th component replaced by $\nu _ { i } ^ { \prime } .$

Let $g ( p ,$ m) denote the outcome of a mechanism C given the problem instance $p$ and message profile m. Let $t \succeq { i } ^ { \prime }$ denote that agent i prefers outcome t to outcome $t ^ { \prime }$ V.

Definition 3.1 . A vector of strategy functions $s ^ { * }$ (referred to as a strategy profile) is a dominant strategy equilibrium of a mechanism C if, for each agent $i ,$ all problem instances $p ,$ and all preference profiles $\theta ,$

$$
g (p, \left(s _ {i} ^ {*} (p, \theta), m _ {- 1}\right)) \succeq_ {i} g (p, \left(m _ {i} ^ {\prime}, m _ {- i}\right))
$$

for all messages $m _ { i } ^ { \prime }$ and all message profiles $m _ { - i }$

In other words, a strategy profile is a dominant strategy equilibrium if, no matter what the other agents do, no agent i can benefit by sending a message different from the one prescribed by $s _ { i } ^ { * }$

Definition 3.2 . A strategy profile $s ^ { * }$ is a Nash equilibrium of a mechanism C if, for each agent $i ,$ all problem instances $p ,$ and all preference profiles $\theta ,$

$$
g (p, (s _ {i} ^ {*} (p, \theta), s _ {- i} ^ {*} (p, \theta))) \succeq_ {i} g (p, (m _ {i} ^ {\prime}, s _ {- i} ^ {*} (p, \theta)))
$$

for all messages $m _ { i } ^ { \prime }$ V.

In other words, a strategy profile is a Nash equilibrium if no agent can benefit by unilaterally deviating from the prescribed message.

Definition 3.3. An outcome x is a polynomial time equilibrium outcome of a mechanism C if there is a equilibrium strategy profile $s ^ { * }$ , a problem instance $p ,$ and a preference profile h such that C outputs x when the message profile is $s ^ { * } ( p , \theta )$ and, for each agent $i , s _ { i } ^ { * }$ is a polynomial time strategy function.

We now define what it means for a mechanism to implement a social choice rule in polynomial time.

Definition 3.4. Let F be a social choice rule. Let $\varGamma$ be a polynomial time mechanism. Let $\mathrm { P E } ( p , \theta )$ be the set of polynomial time equilibrium outcomes of C for problem instance $p$ and preference profile h. We say that, in polynomial time for polynomial time bounded agents,

(1) C implements F if $\mathrm { P E } ( p , \theta ) \cap { \cal F } ( p , \theta ) \neq \emptyset$ for all $p$ and h.

(2) $\varGamma$ strongly implements F if $\emptyset \neq \operatorname { P E } ( p , \theta ) \subseteq F ( p , \theta )$ for all $p$ and h.

(3) C fully implements F if $\mathrm { P E } ( p , \theta ) = F ( p , \theta )$ for all $p$ and h.

The restriction to polynomial time equilibrium outcomes requires some discussion. As the following lemma shows, if there is at least one polynomial time equilibrium strategy profile, then every equilibrium outcome is a polynomial time equilibrium outcome.

Lemma 3.1. Given a mechanism C, let PE(p, h) be the set of polynomial time equilibrium outcomes for problem instance p and preference profile h. Let $E ( p ,$ $\theta )$ be the set of all equilibrium outcomes for problem instance p and preference profile h. If there is at least one polynomial time equilibrium strategy profile for $T ,$ then $P E ( p , \ \theta ) = E ( p , \ \theta )$ for all p and h.

Proof . If suffices to show that $E ( p , \theta ) \subseteq \mathrm { P E } ( p , \theta ) .$ for all $p$ and $\theta .$ Let $\hat { p }$ be any problem instance and $\hat { \theta }$ be any preference profile consistent with ${ \hat { p } } .$ . Let t be any member of $E ( \hat { p } , \hat { \theta } )$ . Let $\hat { s }$ be an equilibrium strategy profile such that t is the outcome generated by C when given $\hat { s } ( \hat { p } , \ \hat { \theta } )$ . Let $s ^ { * }$ be any polynomial time equilibrium strategy profile for C. Define a new strategy profile $s ^ { \prime }$ Vsuch that for all $i ,$

$$
s _ {i} ^ {\prime} (p, \theta) = \left\{ \begin{array}{l} \hat {s} _ {i} (\hat {p}, \hat {\theta}) \text {   if   } p = \hat {p} \text {   and   } \theta = \hat {\theta} \\ s _ {i} ^ {*} (p, \theta) \text {   otherwise } \end{array} \right.
$$

For each $i , s _ { i } ^ { \prime }$ is polynomial time computable since $\hat { s } _ { i } ( \hat { p } , \hat { \theta } )$ is fixed and $s _ { i } ^ { * }$ is polynomial time computable. Furthermore, $s ^ { \prime }$ is an equilibrium strategy profile since both $s ^ { * }$ and $\hat { s }$ are. Since t is the outcome generated by C when given $\hat { s } ( \hat { p } , \hat { \theta } ) { = } s ^ { \prime } ( p , \theta )$ and $s ^ { \prime }$ is a polynomial time strategy profile, $t { \in } \mathrm { P E } ( \hat { p } , \ \hat { \theta } )$ . Therefore, $E ( \hat { p } , \hat { \theta } )$ $\underline { { \underline { { \mathbf { \Pi } } } } } \mathrm { P E } ( \hat { p } , \ \hat { \theta } )$ 5

As a result, we have the following proposition.

Proposition 3.1 . If C strongly [fully] implements a social choice rule F in polynomial time for polynomial time bounded agents then C strongly [fully] implements F.

Proof. Since C strongly implements F in polynomial time for polynomial time bounded agents, C has some polynomial time equilibrium strategy profile. The result then follows from Lemma 3.1. 5

This result is extremely useful because it implies that any property of a social choice rule that is necessary for strong or full implementation is also necessary for strong or full implementation in polynomial time for polynomial time bounded agents.

In Section 4, we show that MAXSAT is not implementable in polynomial time for polynomial time bounded agents. Therefore, the best one can hope for is to find some approximation to MAXSAT that is implementable in polynomial time for polynomial time bounded agents. An approximation to MAXSAT is defined as a social choice rule of the form:

$$
\begin{array}{l} c - \text { MAXSAT } (p, \theta) \\ = \{t: t \text {   satisfies   at   least   } c N ^ {*} (\theta) \text {   clauses } \} \end{array}
$$

where $c { \in } ( 0 , 1 )$ and $N ^ { * } ( \theta )$ is the maximum number of simultaneously satisfiable clauses in h. We say that MAXSAT is approximately implementable if there is some constant $c { \in } ( 0 , \ 1 )$ such that $c { \mathrm { - } } { \mathrm { M A X S A T } }$ is implementable. In Sections 5 and 6, we show that (1/2)-MAXSAT is strongly implementable in dominant strategy and Nash equilibrium, respectively. In Section 7, we show that c = 1/2 is the largest value for which c-MAXSAT is strongly implementable.

## 4. Revelation mechanisms

Mechanisms which require the agents to declare their preferences (truthfully or falsely) form an important class of mechanisms known as revelation mechanisms. A social choice rule F is said to be truthfully implementable if there is a revelation mechanism for which truthful preference declarations by all the agents constitutes an equilibrium with outcome in $F ( p , \theta )$ for all problem instances $p$ and all preference profiles h. The following result is known as the Revelation Principle. This principle applies to many equilibrium concepts including dominant strategy and Nash equilibrium so we state it without specifying a particular equilibrium concept (see the discussion in Ref. [15], pp. 182 –183):

Proposition 4.1 (The Revelation Principle). Suppose there exists a mechanism C that implements social choice rule F. Then F is truthfully implementable.

Proof . See, for example, Ref. [14].

Because of the Revelation Principle, the discussion can be restricted to social choice rules that are truthfully implementable. If we can show that there is no revelation mechanism to truthfully implement a social choice rule, then the social choice rule is not implementable by any mechanism. The Revelation Principle has a polynomial time analog if the agents are restricted to polynomial time strategies. This result holds for any equilibrium concept for which the standard Revelation Principle applies. The Polynomial Time Revelation Principle is important since proving a social choice rule is not truthfully implementable in polynomial time for polynomial time bounded agents amounts to little more than showing the non-multiagent version of the problem cannot be solved in polynomial time (see the Proof of Proposition 4.2 for example). In this section, we also show that the revelation mechanism does not apply when the mechanism is restricted to polynomial time but the agents are not. In essence, the mechanism can be designed in such a way that the agents have incentive to perform computation on behalf of the mechanism.

Theorem 4.1 (The Polynomial Time Revelation Principle). If a social choice rule F is implementable in polynomial time for polynomial time bounded agents then F is truthfully implementable in polynomial time for polynomial time bounded agents.

Proof . In the standard proof of the revelation principle (see Ref. [14] for example), we let C be a mechanism that implements $F$ and $s ^ { * }$ be any equilibrium strategy profile that results in an outcome in $F ( p , \ \theta )$ for all $p$ and $\theta .$ . Then a direct revelation mechanism $\varGamma ^ { \ast }$ is created which, given a problem instance and a declared preference profile $\hat { \theta } ,$ simulates $\varGamma$ on $s ^ { * } ( p , ~ \ r _ { \ r } \ r _ { \ r } )$ . It is straightforward to show that truthtelling is an equilibrium strategy for $\varGamma ^ { \ast }$

The proof of the Polynomial Time Revelation Principle follows immediately from the standard proof since, if $\varGamma$ and $s ^ { * }$ are computable in polynomial time, so is $\varGamma ^ { \ast }$ 5

As the following proposition shows, MAXSAT is not truthfully implementable by a polynomial time revelation mechanism. Combined with Theorem 4.1, this implies that MAXSAT is not polynomial time implementable for polynomial time bounded agents.

## Proposition 4.2. MAXSAT is not truthfully implementable by a polynomial time revelation mechanism.

Proof. Assuming P p NP, there is no algorithm to find a member of $\mathrm { M A X S A T } ( p , \ \theta )$ in polynomial time for all $p$ and h. Suppose MAXSAT is truthfully implemented by a mechanism C. Then the polynomial time algorithm that computes C finds a member of $\mathrm { M A X S A T } ( p , \ \theta )$ in polynomial time for all $p$ and h contradicting our assumption that $\mathrm { P } \neq \mathrm { N P } .$ 5

## Corollary 4.1. MAXSAT is not polynomial time implementable for polynomial time bounded agents.

## Proof. Immediate from Proposition 4.2 and Theorem 4.1. 5

Proposition 4.3 below shows that, if the agents are not restricted to polynomial time, MAXSAT is Nash implementable by a polynomial time mechanism. This implies that the revelation principle does not apply when the mechanism is restricted to polynomial time but the agents are unrestricted. In other words, if we are dealing with an asymmetrical environment where the agents have exponentially more computation time than the mechanism, we cannot necessarily rely solely on revelation mechanisms.

## Proposition 4.3. If the agents are unrestricted then MAXSAT is Nash implementable by a polynomial time mechanism.

Proof. We need to show that there is a polynomial time mechanism that Nash implements MAXSAT when the agents have no computational restrictions. In this mechanism, each agent i will declare a clause $\theta _ { i }$ and propose an outcome $t _ { i } .$ The mechanism will select as the outcome the proposed outcome that satisfies the most declared clauses. If there is a tie, the mechanism will take the proposed outcome of the least numbered agent involved in the tie. We claim that the strategy profile where each agent i declares its true clause and proposes any outcome that satisfies itself and the maximum number of other agents is a Nash equilibrium. Note that the agents’ strategies are not computable in polynomial time since they require each agent to solve the (non-multiagent) MAXSAT problem.

We need to show that no agent has incentive to deviate from this strategy. For any t and ${ \widehat { \theta } } ,$ let $N ( { \widehat { \theta } } , t )$ be the number of clauses in h that are satisfied by outcome t. First note that agent i would have no reason to deviate if it is satisfied by the selected outcome. Let $\theta$ be the preference profile. Let $t _ { j }$ be the outcome selected when each agent follows the strategy described above. Assume agent i is not satisfied by $t _ { j } .$ The number of agents satisfied by agent $i \mathrm { { ^ { \circ } s } }$ proposed outcome, $t _ { i } ,$ is either less than the number satisfied by $t _ { j }$ or $t _ { i }$ and $t _ { j }$ satisfy the same number of agents and $j < i .$ In other words, $N ( \theta , t _ { i } ) \le N ( \theta , t _ { j } )$ with strict inequality $\mathrm { i f } j > i .$ Since $t _ { i }$ satisfies agent i and the maximum number of other agents, $N ( ( \theta _ { i } ^ { \prime } , \ \theta _ { - } \ : _ { i } ) , \ t ) \leq N ( \theta , \ t _ { i } )$ for all $\theta _ { i } ^ { \prime }$ and all t such that t satisfies $\theta _ { i }$ . Furthermore, since $t _ { j }$ does not satisfy $\theta _ { i } , \ N ( \theta , \ t _ { j } ) \le N ( ( \theta _ { i } ^ { \prime } , \ \theta _ { - i } ) , \ t _ { j } )$ for all $\theta _ { i } ^ { \prime }$ . Combining these three inequalities, we have $N ( ( \theta _ { i } ^ { \prime } , \theta _ { - i } ) , t ) { \le } N ( ( \theta _ { i } ^ { \prime } , \theta _ { - i } ) , t _ { j } )$ for all $\theta _ { i } ^ { \prime }$ and all t such that t satisfies $\theta _ { i }$ with strict inequality if $j { > } i .$ Hence, agent i cannot change the selected outcome from an outcome that he is not satisfied with to an outcome that he is satisfied with by choosing a different message. Therefore, agent i cannot benefit by deviating from the strategy. In other words, the strategy profile is a Nash equilibrium.

Notice that with this strategy profile, at least one of the agents proposes an outcome that is in $\mathrm { M A X S A T } ( p , \theta )$ . Therefore, the outcome selected by the mechanism will be in MAXSAT $\left( p , \ \theta \right)$ which implies the mechanism implements MAXSAT. Furthermore, the computation performed by the mechanism is trivial. It simply needs to calculate and compare the number of clauses satisfied by each proposed outcome. This can clearly be done in polynomial time. 5

In the Proof of Proposition 4.3, we see that, if the mechanism is computationally restricted but the agents are not, then the mechanism can be designed in such a way that the agents perform computation and provide the results of that computation to the mechanism. In particular, the agents are given incentive to solve a version of the maximum satisfiability problem. The proof would also work in an incomplete information environment if the mechanism included two stages. In the first stage, the agents would declare their preferences to each other and the mechanism. In the second stage, the agents would propose an outcome. By lying in the first stage, an agent could affect the outcomes proposed by the other agents but a similar argument to the one above shows that the agents cannot affect the proposed outcomes in a beneficial way.

## 5. Dominant strategy implementation

When dealing with dominant strategy implementation, one must contend with an impossibility result known as the Gibbard –Satterthwaite Theorem [7,36] which restricts the set of implementable social choice functions to those that are dictatorial. (A social choice function maps a problem instance and a preference profile to a single outcome.)

Definition 5.1 . A social choice function f is dictatorial for problem instance $p$ if there is a single agent $i$ such that, for all preference profiles $\theta , f ( p , \theta )$ is agent i’s most preferred outcome.

We say a social choice function is truthfully implementable at $p$ if there is a revelation mechanism that implements f and for which there is an equilibrium strategy profile $s ^ { * }$ with $s ^ { * } ( p , \theta ) = \theta$

## Proposition 5.1 (The Gibbard –Satterthwaite

Theorem). Let f be any social choice function. Suppose, for problem instance p, the set of possible outcomes X is finite and contains at least three elements and that the range of f restricted to p is $X .$ Further suppose that the set of possible preference relations over X contains the set of strict preferences over X. Then f is truthfully implementable at p in dominant strategies if and only if f is dictatorial for problem instance $p .$

Because of the Gibbard–Satterthwaite Theorem, dominant strategy implementation is generally studied in restricted environments. The most widely studied is the quasilinear environment. In a quasilinear environment, the agents’ have some sort of transferrable good, i.e., money, and the outcomes include the transfer of money to or from individual agents. An agent’s utility of an outcome is then defined to be the value the agent assigns to the non-monetary part of the outcome plus the actual amount of money transferred to the agent.

Fortunately, the Gibbard–Satterthwaite Theorem does not apply to Multiagent MAXSAT because the set of preference relations for Multiagent MAXSAT does not include the set of strict preference relations. Strict preferences are not possible because, if an agent’s clause does not include a variable $x _ { i } ,$ the agent is indifferent between truth assignments that are identical except in their assignment to $x _ { i } .$ . Furthermore, if the agent’s clause includes more than one literal, then the agent is indifferent between truth assignments that satisfy at least one of the literals. Since the Gibbard –Satterthwaite Theorem does not apply to MAXSAT, we are free to consider environments that are not quasilinear.

As the following proposition shows, if there are no computational restrictions on the mechanism, MAX-SAT is truthfully implementable in dominant strategies using an outcome function that is not dictatorial for any problem instance.

Proposition 5.2. MAXSAT is truthfully implementable in dominant strategies by a revelation mechanism with an outcome function that is not dictatorial for any problem instance $p .$

Proof. Order the truth assignments lexicographically where $x _ { i } = \mathrm { t r u e }$ comes before $x _ { i } = \mathrm { f a l s e }$ for $1 \leq i \leq n$ Define a revelation mechanism C that chooses the first truth assignment in the lexicographic ordering that satisfies the maximum number of simultaneously satisfiable clauses in the declared preference profile. For any truth assignment ˆt and any preference profile $\hat { \theta } ,$ define $N ( { \hat { \theta } } , { \hat { t } } )$ to be the number of clauses in $\hat { \theta }$ that $\hat { t }$ satisfies.

Let $p$ be any problem instance. Fix i and let $\theta _ { i }$ be agent $i \mathrm { { ^ { \circ } s } }$ true clause. To prove that truth telling is a dominant strategy for agent i, we need to show that no matter what preferences the other agents declare, agent i can do no better than to declare its true preference $\theta _ { i } .$

Let $\widehat { \theta } _ { - i }$ be any preference profile declared by the other agents. Let t be the outcome when the message profile is $( \theta _ { i } , \hat { \theta } _ { - i } )$ . Suppose agent i is not satisfied by $t .$ Let $t ^ { \prime }$ be any truth assignment that does satisfy $\theta _ { i } .$ . Let $\widehat { \theta } _ { i }$ be any clause that agent i can declare.

Since $t ^ { \prime }$ satisfies $\bar { \theta } _ { i } , N ( ( \hat { \theta } _ { i } , \hat { \theta } _ { - i } ) , t ^ { \prime } ) { \leq } N ( ( \theta _ { i } , \hat { \theta } _ { - i } ) , t ^ { \prime } )$ Since t does not satisfy $\theta _ { i } , N ( ( \theta _ { i } , \hat { \theta } _ { - i } ) , t ) \leq N ( ( \hat { \theta } _ { i } , \hat { \theta } _ { - i } ) ,$ $t ) .$ However, since t is chosen over $t ^ { \prime }$ when the agents declare $( \theta _ { i } , \hat { \theta } _ { - i } )$ , it must be the case that $N ( \theta _ { i } , \hat { \theta } _ { - i } ) ,$ $t ^ { \prime } ) \leq N ( ( \theta _ { i } , \hat { \theta } _ { - i } ) , t )$ . Combining these inequalities, we have, $N ( ( \hat { \theta } _ { i } , \hat { \theta } _ { - i } ) , t ^ { \prime } ) \leq N ( ( \hat { \theta } _ { i } , \hat { \theta } _ { - i } ) , t )$ . Furthermore, if $N ( ( \hat { { \boldsymbol { \theta } } } _ { \mathrm { i } } , \hat { { \boldsymbol { \theta } } } _ { - i } ) , t ^ { \prime } ) { = } N ( ( \hat { { \boldsymbol { \theta } } } _ { \mathrm { i } } , \hat { { \boldsymbol { \theta } } } _ { - i } ) , t ) ,$ , we must have $N ( \theta _ { i } ,$ $\hat { \theta } _ { - i } ) , t ^ { \prime } ) = N ( ( \theta _ { i } , \hat { \theta } _ { - i } ) , i$ t) and, therefore, the tie breaking rules must favor $t ,$ i.e., t comes before $t ^ { \prime }$ in the ordering. Thus, regardless of what clause agent i declares, $t ^ { \prime }$ will not be the outcome chosen by the mechanism. Since this is true for any $t ^ { \prime }$ that satisfies agent i and any $\hat { \theta } _ { - i } ,$ agent i cannot improve the outcome for himself by lying. Hence, truth telling is a dominant strategy.

To see that the outcome function is not dictatorial for $p ,$ suppose the preference profile is $( \bar { x } _ { 1 } , x _ { 1 } , . . . , x _ { 1 } )$ i.e., agent 1 is satisfied only when x = false and the other agents are satisfied only when $x _ { 1 } = \mathrm { t r u e }$ . The mechanism sets $x _ { 1 }$ to true so the outcome is not agent 1’s most preferred outcome. The same argument can be applied to the other agents which implies that the outcome chosen by the mechanism is not the same agent’s most preferred outcome for every h. 5

## 5.1. Approximation mechanisms for dominant strategy implementation

We know from Corollary 4.1 that MAXSAT cannot be implemented in polynomial time so we are interested in determining whether there is some constant c such that c-MAXSAT can be implemented in polynomial time. The question is can we convert one of the many existing approximation algorithms for nonmultiagent version of MAXSAT into a mechanism that truthfully implements c-MAXSAT? For example, suppose the mechanism were to use Johnson’s first approximation algorithm (see Refs. [2,11]) to determine the outcome. This is a greedy algorithm that takes the literal that appears in the most clauses and sets it to true. It then repeatedly chooses the unassigned literal that appears most in the remaining unsatisfied clauses and sets that to true. Let ties be broken by choosing the least numbered variable first and assigning true before false. If there are five agents with goals defined by the vector $\scriptstyle \theta = ( x _ { 1 } , \bar { x } _ { 1 } \lor \bar { x } _ { 2 } , \bar { x } _ { 1 } \lor \bar { x } _ { 2 } .$ $x _ { 2 } , x _ { 2 } )$ then the mechanism chooses $t = \bar { x } _ { 1 } x _ { 2 } , \mathrm { i . e . }$ , it sets $x _ { 1 }$ to false and $x _ { 2 }$ to true. Agent 1 is not satisfied by this outcome. However, if agent 1 declared its type to be $x _ { 1 } \vee \bar { x } _ { 2 } .$ the outcome would be $t = x _ { 1 } \bar { x } _ { 2 }$ which does satisfy agent 1. Therefore, in this instance, it is better for agent 1 to lie about his goal. In Ref. [28], we also show that a (2/3)-approximation algorithm from Ref. [11] does not result in a truthful mechanism. It is possible to strongly implement (1/2)-MAXSAT in polynomial time, however, using an mechanism based on the following property of MAXSAT.

Lemma 5.1. For any truth assignment t, let t¯ denote the truth assignment such that for every variable v, ¯t(v) = true if and only if t(v) = false. For all truth assignments t, either t or t¯ satisfies at least half of the maximum number of simultaneously satisfiable clauses.

Proof. Let $\theta _ { i }$ be any clause that t does not satisfy. Let $l _ { i }$ be a literal in $\theta _ { i } .$ Then $t ( l _ { i } ) = \mathrm { f a l s e }$ which implies $\bar { t } ( l _ { i } ) { = } \mathrm { t r u e }$ . Therefore, $\bar { t }$ satisfies $\theta _ { i } .$ Hence, for every clause $\theta _ { i } ,$ either t or $\bar { t }$ must satisfy $\theta _ { i }$ which implies that one of them must satisfy at least half the total number of clauses. 5

We can use this property to develop a polynomial time mechanism that strongly implements (1/2)- MAXSAT. For each problem instance $p ,$ fix a truth assignment $t _ { p }$ and define a social choice function f as follows:

$$
f (p, \theta) = \left\{ \begin{array}{l} \bar {t} _ {p} \text {   if   } \bar {t} _ {p} \text {   satisfies   more   clauses   in   } \theta \text {   than   } t _ {p} \\ t _ {p} \text {   otherwise } \end{array} \right.\tag{1}
$$

This social choice function is not dictatorial since, for any problem instance $p$ and for any agent $i ,$ we can define $\theta$ such that:

(1) $t _ { p }$ does not satisfy $\theta _ { i } ;$

(2) $t _ { p }$ does satisfy every clause in $\theta _ { - i } ;$

(3) $\bar { t } _ { p }$ does not satisfy any clause in $\theta _ { - i }$

For example, let $t _ { p } = \bar { x } _ { 1 } x _ { 2 } x _ { 3 }$ and $\scriptstyle \theta = ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ . We have $f ( p , \theta ) = t _ { p }$ which is not agent $1 \mathrm { { } ^ { \circ } s }$ most preferred outcome. A similar argument applies to the other two agents which implies that $f ( p , \ \theta )$ is not the same agent’s most preferred outcome for every h. Lemma 5.1 implies that $f ( p , \theta ) \varepsilon ( 1 / 2 ) \ – \mathrm { M A X S A T } ( p , \theta )$ for all $p$ and h. Therefore, any mechanism that truthfully implements $f ,$ also truthfully implements (1/2)-MAXSAT.

Define a revelation mechanism which we call the Complement Mechanism as follows. Given a problem instance $p ,$ let $t _ { p }$ be the fixed truth assignment from the definition of f in Eq. (1). If $t _ { p }$ satisfies at least as many of the declared clauses as ${ \bar { t } _ { p } } ,$ then choose $t _ { p }$ as the outcome; otherwise, choose $\bar { t } _ { p }$

Lemma 5.2. The Complement Mechanism truthfully implements f in dominant strategies in polynomial time for polynomial time bounded agents.

Proof. The Complement Mechanism is polynomial time since, to compute the outcome, it need only compare the number of clauses in h that are satisfied by two fixed truth assignments. Truth telling is certainly a polynomial time strategy so it suffices to show that truth telling constitutes a dominant strategy equilibrium.

Let $\theta _ { i }$ be the clause representing agent i’s true preference relation.

Case 1: $t _ { p }$ satisfies $\theta _ { i }$ and $\bar { t } _ { p }$ does not.

Agent i cannot change the number of clauses declared by the other agents that are satisfied by $t _ { p }$ or $\bar { t } _ { p }$ . Therefore, by lying, agent i can decrease (or leave unchanged) the number of clauses satisfied by $t _ { p }$ and increase (or leave unchanged) the number of clauses satisfied by $\bar { t } _ { p } .$ . Thus, if lying has any effect at all, it is to change the outcome from $t _ { p }$ to $\bar { t } _ { p }$ which is worse for agent i.

Case 2: $\bar { t } _ { p }$ satisfies $\theta _ { i }$ and $t _ { p }$ does not. A symmetric argument applies to this case.

Case 3: Both $t _ { p }$ and $\bar { t } _ { p }$ satisfy $\theta _ { i } .$ In this case, agent i does not care which of the two truth assignments is chosen so lying cannot be beneficial or harmful.

Since lying is never beneficial, truth telling is a dominant strategy. 5

Although we have shown that truth-telling is a dominant strategy equilibrium for the Complement Mechanism that results in an outcome in (1/2)-MAX-SAT, it is possible that there may be other dominant strategy equilibria and the corresponding outcomes may not belong to (1/2)-MAXSAT. Although, it could certainly be argued that truth-telling is such a simple strategy that it is the most likely dominant strategy to be played, we would be more confident in the mechanism if we could show that all dominant strategy equilibrium outcomes belonged to (1/2)-MAXSAT. In fact, as the following theorem shows, this is the case.

Theorem 5.1. (1/2)-MAXSAT is strongly implementable in dominant strategies in polynomial time for polynomial time bounded agents.

Proof. In the Proof of Lemma 5.2, Case 3 is the only case in which lying can affect the outcome and not be harmful to the agent. Therefore, if the agents all play dominant strategies then the only agents that lie are indifferent to the outcome. We claim that if any group of agents that are indifferent between $t _ { p }$ and $\bar { t } _ { p }$ affect the outcome by lying then the new outcome is still in (1/2)-MAXSAT.

Let p be the problem instance and h be the true preference profile. Suppose that a number of agents who are indifferent lie about their preference. Let $\theta ^ { \prime }$ be the declared preference profile. Assume without loss of generality that the mechanism outputs $\bar { t } _ { p }$ when the agents declare the true preference profile $\theta ,$ and $t _ { p }$ when the agents declare a preference profile hVwhich may include a number of lies. We know from Lemma 5.1 that, for any preference profile, at least one of $t _ { p }$ or $\bar { t } _ { p }$ satisfies at least half of the clauses. Therefore, $t _ { p }$ must satisfy at least half of the clauses in $\theta ^ { \prime }$ . Let $b$ be the number agents that strictly prefer $t _ { p }$ to $\bar { t } _ { p }$ and let $d$ be the number of agents who are indifferent between $t _ { p }$ and $\bar { t } _ { p } .$ . Since only indifferent agents lie, the number of clauses satisfied by $t _ { p }$ in $\theta ^ { \prime }$ and in $\theta$ is $b + d .$ . Since the mechanism outputs $t _ { p }$ when the message profile is $\theta ^ { \prime } { } _ { \mathrm { i } }$ $b + d$ must be at least I/2 where I is the total number or agents. However, this implies $t _ { p } { \in } ( 1 / 2 )$ $\mathrm { M A X S A T } ( p , \ \theta )$ . Therefore, every dominant strategy equilibrium outcome is in (1/2)-MAXSAT( p, h) for every p and h. 5

In Ref. [24], Nisan and Ronen showed that in quasilinear environments, dominant strategy implementation is impossible for many problems where approximation mechanisms must be used. The result above shows that, because of the characteristics of the multiagent MAXSAT problem, it is possible to achieve dominant strategy implementation using an approximation mechanism albeit one with a rather poor approximation ratio. Whether this indicates that there is hope for dominant strategy implementation in computational mechanism design problems in general is uncertain. In particular, it is not clear that a 1/2- approximation should be considered much of a success since it is achievable with a somewhat trivial mechanism. Our hope for dominant strategy implementation is further diminished by the results of Section 7 which show that 1/2 is the best approximation possible.

On a more positive note, the nature of the MAXSAT problem has allowed us to escape from the Gibbard– Sattherwaite theorem without resorting to the quasilinear assumption. Similar combinatorial problems may be able to escape as well and this should be considered before abandoning dominant strategy implementation altogether. When dominant strategy implementation must be abandoned in complete information environments, Nash implementation needs to be considered. We investigate Nash implementation for multiagent MAXSAT in the next section.

## 6. Nash implementation

We have seen that (1/2)-MAXSAT is strongly implementable in dominant strategies using the Complement Mechanism. However, the Complement Mechanism is not a particularly attractive mechanism since, for a problem instance $p ,$ the outcome is always either $t _ { p } \mathrm { o r } \bar { t } _ { p }$ for a fixed $t _ { p } .$ An unfortunate choice of ${ \bf \dot { \boldsymbol { t } } } _ { p }$ eliminates many outcomes that would be more desirable from a social viewpoint. For example, consider a problem instance with four agents and two variables $x _ { 1 }$ and $x _ { 2 } .$ . Let $t _ { p } = x _ { 1 } x _ { 2 }$ , i.e., $t _ { p }$ sets $x _ { 1 }$ and $x _ { 2 }$ to true. Let the true preference profile $\scriptstyle \theta = ( x _ { 1 } , x _ { 1 } , { \bar { x } } _ { 2 } , { \bar { x } } _ { 2 } )$ . The number of clauses in h that are satisfied by $t _ { p }$ and $\bar { t } _ { p }$ is 2. However, it is possible to satisfy all of the agents by choosing $t ^ { \prime } = x _ { 1 } \bar { x } _ { 2 }$ as the outcome. It would be better to implement a social choice rule that included any truth assignment that satisfied as least as many clauses as both $t _ { p }$ and $\bar { t } _ { p }$ . It could be argued that full Nash implementation of this social choice rule would be better than strong dominant strategy implementation using the Complement Mechanism. Unfortunately, this social choice rule is not fully Nash implementable (see Ref. [28]). In this section, we define an alternative social choice rule that is fully Nash implementable in polynomial time and does not eliminate optimal outcomes from consideration. Under this social choice rule, each desirable outcome is guaranteed to satisfy half of the maximum number of agents, which implies that (1/2)-MAXSAT is strongly Nash implementable in polynomial time. (Note: even though every dominant strategy equilibrium is also a Nash equilibrium, a mechanism that strongly implements a social choice rule in dominant strategies does not necessarily strongly Nash implement that same social choice rule. This is so because there may be undesirable Nash equilibrium outcomes that are not dominant strategy equilibrium outcomes.)

There are two properties of social choice rules that are extremely important for Nash implementation— no-veto power and monotonicity.

Definition 6.1 . A social choice rule F satisfies no-veto power if, when all but at most one of the agents ranks an outcome t as their weakly most preferred choice under a problem instance $p$ and preference profile $\theta ,$ $t { \in } F ( p , \theta )$ .

Definition 6.2. For each agent i, outcome t, and preference relation $\theta _ { i } ,$ define agent $i \mathrm { { ^ { \circ } s } }$ lower contour set for t and $\theta _ { i }$ to be the set:

$$
\begin{array}{c} L _ {i} (t, \theta_ {i}) = \{t ^ {\prime}: t \text {   is   preferred   to   } t ^ {\prime} \text {   under } \\ \text { preference   relation   } \theta_ {i} \} \end{array}
$$

Definition 6.3. A social choice rule F is said to be monotonic if, for all problem instances p, preference profiles h and $\theta ^ { \prime }$ , and all outcomes t such that

(1) $t { \in } F ( p , \theta )$ and

(2) $L _ { i } ( t , \theta _ { i } ) \subseteq L _ { i } ( t , \theta _ { i } ^ { \prime } )$ for all i,

we have $t { \in } F ( p , \theta ^ { \prime } )$

Condition 1 in Definition 6.3 states that t is socially desirable under h. Condition 2 states that no agent prefers an outcome to t under hVthat he does not prefer to t under h. Monotonicity says that when these two conditions are satisfied, t must be socially desirable under hVas well.

As the following result known as Maskin’s Theorem (see Ref. [15]) shows, monotonicity is a necessary and almost sufficient condition for full Nash implementation. Because of Proposition 3.1, this implies that monotonicity is also necessary for full Nash implementation in polynomial time for polynomial time bounded agents.

Proposition 6.1 (Maskin’s Theorem). If a social choice rule is fully Nash implementable then it is monotonic. If there are at least three agents then a social choice rule that is monotonic and satisfies noveto power is fully Nash implementable.

Corollary 6.1 . If a social choice rule F is fully Nash implementable in polynomial time for polynomial time bounded agents then it is monotonic.

Proof. The result follows from Propositions 3.1 and 6.1. 5

Given Maskin’s theorem, we can show that MAX-SAT is not fully implementable.

Proposition 6.2. The social choice rule for MAXSAT is not monotonic.

Proof. Consider the problem instance $p$ in which there are two agents and two variables $x _ { 1 }$ and $x _ { 2 }$ . Let $\scriptstyle \theta = ( x _ { 1 } , \bar { x } _ { 1 } )$ . The maximum number of simultaneously satisfiable clauses in $\theta$ is 1. Let $t = x _ { 1 } x _ { 2 }$ which is in $\mathrm { M A X S A T } ( p , \theta )$ . Let $\scriptstyle \theta ^ { \prime = } ( x _ { 2 } , { \bar { x } } _ { 1 } )$ . Since t satisfies agent 1 when the preference profile is either $\theta$ or $\theta ^ { \prime } { , }$ , agent 1 weakly prefers t to any other outcome under both $\theta _ { 1 }$ and $\theta _ { 1 } ^ { \prime } .$ Therefore, $L _ { 1 } ( t , \theta _ { 1 } ) { = } L _ { 1 } ( t , \theta _ { 1 } ^ { \prime } )$ . Since agent ${ 2 \mathrm { { } s } }$ preference is the same in either case, $L _ { 2 } ( t , \theta _ { 2 } ) { = } L _ { 2 } ( t ,$ $\theta _ { 2 } ^ { \prime } )$ . However, $t \not \in \mathbf { M A X S A T } ( p , \theta ^ { \prime } )$ which implies that MAXSAT is not monotonic. 5

The argument in the above proof can easily be generalized to instances in which the numbers of variables and agents are larger so there is no hope for achieving monotonicity on a (non-trivial) restricted set of problem instances.

## 6.1. Approximation mechanism for Nash implementation

Corollary 4.1 and Proposition 6.2 present two different obstacles to implementing MAXSAT in polynomial time for polynomial time bounded agents. Corollary 4.1 says that polynomial time implementation is impossible because of the computational constraints. Proposition 6.2 says that full implementation cannot be achieved even without the computational constraints. Given these obstacles, we would like to find a constant $c$ such that c-MAXSAT is strongly implementable in polynomial time for polynomial time bounded agents. If we were to find a c such that $c -$

MAXSAT is monotonic and satisfies no-veto power then, by Maskin’s Theorem, we would know that $c -$ MAXSAT is fully implementable. This, however, would not guarantee that c-MAXSAT is fully implementable by a polynomial time mechanism. In fact, Theorem 6.1 below shows that the standard mechanisms used to prove Maskin’s are not polynomial time when the social choice rule is c-MAXSAT.

There are several different mechanisms used to prove Maskin’s theorem. (see Refs. [15,17,32,34]) For example, in Ref. [32], Repullo defines a mechanism that fully implements a monotonic social choice rule satisfying no-veto power as follows. Each agent i declares a preference profile $\theta _ { i } ,$ a proposed outcome $x ^ { i } ,$ and a number $k ^ { i } .$ . Let $p$ be the problem instance and let $m { = } [ ( \theta _ { i } , x _ { i } , k _ { i } ) ] _ { i { = } 1 } ^ { I }$ be the message profile. Let the outcome function $g$ be defined by the following three rules:

(1) If every agent picks the same message $( \theta , x , k )$ and $x { \in } F ( p , \theta )$ then $g ( p , m ) = x .$

(2) If every agent but agent i picks the same message $( \theta , x , k )$ and $x { \in } F ( p , \theta )$ then

$$
g (p, m) = \left\{ \begin{array}{c} x _ {i} \text {   if   } x _ {i} \in L (x, \theta_ {i}) \\ x \text {   otherwise } \end{array} \right.
$$

If neither Rule 1 nor Rule 2 applies then set $g$ $( p , m ) = x _ { j }$ where $j$ is the agent with the highest $k _ { j }$ and ties are broken by choosing the least such $j .$

The idea behind Repullo’s mechanism is that if everyone declares the true preference profile $\theta ,$ the same socially desirable outcome x, and the same number $k ,$ Rule 1 will select x as the outcome. Rule 2 ensures that no single agent can profitably deviate from this strategy profile, establishing x as a Nash equilibrium outcome. Rule 3 has the effect that, if neither Rule 1 nor Rule 2 applies, then any agent can deviate from the strategy profile and change the outcome to anything he wants. This eliminates undesirable equilibrium outcomes (see Ref. [32] for details).

The only computationally non-trivial part of this mechanism is checking to see if $x { \in } F ( p , \ \theta )$ . This check, which also appears in the mechanisms used in Refs. [15,34], corresponds to the following decision problem when $F = c { \mathrm { - } } \mathbf { M } \mathbf { A } \mathbf { X } \mathbf { S } \mathbf { A } \mathbf { T }$ for some constant $c .$

Definition 6.4. Let $c , \ 0 < c < 1$ be fixed. The $c -$ MAXSAT Membership Problem is defined as follows: Given a set of Boolean variables $V { = } \{ \nu _ { 1 } , . . . . , \nu _ { n } \}$ , a set of clauses h over $V$ and a truth assignment $t ,$ does t satisfy at least $c$ times the maximum number of simultaneously satisfiable clauses in h?

Lemma 6.1 below shows that for fixed $^ { c , }$ this problem is NP-hard which implies that Repullo’s mechanism with $F { = } c { \mathrm { - } } \mathbf { M A X S A T }$ is not a polynomial time mechanism.

Lemma 6.1. Let c, $\theta < c < I$ be such that there is a polynomial time approximation algorithm for MAX-SAT that guarantees the number of satisfied clauses is at least c times the maximum number of simultaneously satisfiable clauses. The c-MAXSAT Membership problem is NP-hard.

Proof. Suppose we are given a set of clauses $\theta$ and we want to determine whether there is a truth assignment that satisfies all the clauses in h. Let $m ( \theta )$ be the maximum number of clauses in h that can be simultaneously satisfied. The set of clauses $\theta$ is satisfiable if and only if $\cdot _ { m } ( \theta ) = I$ where I is the number of clauses in $\theta .$

Consider the following algorithm for finding $m ( \theta ) { \mathrm { : } }$

(1) Use the polynomial time approximation algorithm we assumed we have for MAXSAT to choose a truth assignment t that satisfies at least $c m ( \theta )$ clauses.

(2) Let b be the number of clauses in $\theta$ that t satisfies.

(3) Let $k = 1$

(4) Extend the set of variables to the set $V ^ { k }$ by adding variable $\nu _ { n + k }$

(5) Extend the set of clauses to $\theta ^ { k }$ by adding a clause with a single literal $\nu _ { n + k }$

(6) Extend t to $V ^ { k }$ by setting $t ( \nu _ { n + k } )$ to FALSE.

(7) If t extended to $V ^ { k }$ does not satisfy $c m ( { \theta } ^ { k } )$ clauses, increment k and repeat from Step 4.

(8) Otherwise return $\lfloor ( 1 / c ) b \rfloor - k + 1$

We need to show that this algorithm returns the correct value of $m ( \theta )$ . Any truth assignment for $V ^ { k - 1 }$ can be extended to satisfy $\nu _ { n + k }$ without affecting the number of clauses it satisfied in $\theta ^ { k - 1 }$ since, for each $k , \ \nu _ { n + k }$ does not appear in any clause in $\theta ^ { k - 1 }$ Therefore, $m ( \theta ^ { k } ) { = } m ( \theta ) + k .$ . Since t does not satisfy $\nu _ { n + k }$ for any $k \geq 1$ , t satisfies b of the clauses in each of the $\theta ^ { k } .$ . The repetition is guaranteed to terminate by the time $k { = } \mathsf { I } ( ( 1 - c ) / ( c ) ) m ( \theta ) \mathsf { I } { + } 1$ since t satisfies at most m(h) clauses in $\theta ^ { k }$ and $m ( \theta ^ { k } ) { = } m ( \theta ) { + } \mathsf { I } ( ( 1 - c ) /$ $( c ) ) m ( \theta ) ] + 1 \geq ( m ( \theta ) / c ) + 1$ when $k { = } \operatorname { I } ( ( 1 - c ) /$ $( c ) ) m ( \theta ) ] + 1$ . Since the algorithm begins with a truth assignment that satisfies $b \geq c m ( \theta )$ clauses, it stops extending the set of clauses when k is the smallest integer such that $b < c ( m ( \theta ) + k )$ . This implies ${ \cal m } ( \theta ) { = } [ ( 1 / c ) b ] { -  k + 1 }$

To evaluate the asymptotic running time of the algorithm, first note that, given our assumptions, we know that each of the steps of this algorithm other than checking the condition in Step $7$ takes polynomial time. Furthermore, the maximum number of iterations is $\lceil ( ( 1 - c ) / ( c ) ) \bar { I } \rceil + 1 \ \mathrm { s o }$ , since $c$ is fixed, there are a polynomial number of iterations. Hence, if Step $7$ takes polynomial time, the entire algorithm is polynomial time. Since Step 7 is equivalent to checking whether $t { \in } c { \mathrm { - } } \mathrm { M A X S A T } ( p , \ \theta ^ { k } )$ , the entire algorithm is polynomial time if and only if the $c -$ MAXSAT Membership problem can be solved in polynomial time.

We can use this algorithm to decide SAT by comparing the output to the number of clauses in $\theta .$ The Boolean formula h is satisfiable if and only if the value for $m ( \theta )$ returned in Step 8 is I. Therefore, given an algorithm that solves the c-MAXSAT Membership problem in polynomial time, we can create an algorithm that solves SAT in polynomial time. Hence, the c-MAXSAT Membership problem is NP-hard. 5

Theorem 6.1. Let c, $\theta < _ { \bf { \mathscr { c } } } < _ { \bf { \mathscr { I } } , }$ be such that there is a polynomial time approximation algorithm for c-MAXSAT. When F = c-MAXSAT, Repullo’s mechanism is not a polynomial time mechanism.

Proof. For the mechanism to check whether $\scriptstyle x \in F ( \theta )$ in Rules 1 and 2, it requires a solution to the $c -$ MAXSAT Membership problem. Lemma 6.1 shows this cannot be done in polynomial time. 5

For Repullo’s mechanism to implement c-MAX-$\mathrm { S A T } ,$ for every problem instance $p$ and preference profile h, at least one of the agents must choose an outcome that is in $c { \mathrm { - } } { \mathrm { M A X S A T } } ( p , \ \theta )$ . Theorem 6.1 implies that if c is such that Repullo’s mechanism with $F { = } c { \mathbf { - } } { \mathbf { M A X S A T } }$ is polynomial time then the agents cannot find an alternative in $c { \mathrm { - } } { \mathrm { M A X S A T } }$ in polynomial time. Therefore, either the mechanism is not polynomial time or there is no polynomial time equilibrium strategy profile. However, as discussed in Section 2, we are willing to settle for strong implementation as opposed to full implementation of c-MAXSAT. Thus, it is sufficient for our purposes to find a social choice rule F such that:

(1) $F$ is monotonic and satisfies no-veto power; (2) $F ( p , \theta ) { \subseteq } c { \mathrm { - } } \mathrm { M A X S A T } ( p , \theta )$ for all $p$ and $\theta ;$ (3) checking membership in $F$ is easy.

These conditions are met with $c = 1 / 2$ by the social choice rule that defines an outcome to be desirable if it satisfies at least half the total number of agents as opposed to half the maximum number of simultaneously satisfiable agents.

Lemma 6.2. Let $F ( p , \theta ) { = } \{ t { : }$ t satisfies at least half the clauses in $\theta \} .$ If the set of problem instances is restricted to those in which there are at least three agents, F is fully Nash implementable using Repullo’s mechanism.

Proof . F satisfies no-veto power since, if all but one agent ranks an outcome t as their (weakly) most preferred outcome, t satisfies at least half of the agents.<sup>3</sup> Let p, h, hVand t be such that $t { \in } F ( p , \theta )$ and $L _ { i } ( t , \ \theta _ { i } ) \subseteq L _ { i } ( t , \ \theta _ { i } ^ { \prime } )$ for all i. Suppose, t satisfies $\theta _ { j }$ for some agent j. Then $L _ { j } ( t , \ \theta _ { j } )$ contains every possible outcome and, since $L _ { j } ( t , \ \theta _ { j } ) \subseteq L _ { j } ( t , \ \theta _ { j } ^ { \prime } ) , L _ { j } ( t , \ \theta _ { j } ^ { \prime } )$ contains every possible outcome. Since every clause has a satisfying truth assignment, this implies that t satisfies $\theta _ { j } ^ { \prime }$ . Since this is true for each j such that t satisfies $\theta _ { j }$ and since $t { \in } F ( p , \theta )$ , t satisfies at least half of the clauses in hV. This implies $t { \in } F ( p , \theta ^ { \prime } )$ . Therefore, F is monotonic. Since F is monotonic and satisfies no-veto power, Repullo’s mechanism fully Nash implements F. 5

Theorem 6.2. When restricted to problem instances p in which there are at least three agents, the social choice rule (1/2)-MAXSAT is strongly Nash implementable in polynomial time for polynomial time bounded agents.

Proof. Let F be the social choice rule defined in Lemma 6.2. It is easy to check whether a truth assignment satisfies at least half of the total number of clauses so Repullo’s mechanism is polynomial time computable. Let $\theta$ be the agents’ true preference profile. Let t be any truth assignment in $F ( p , \theta )$ . The strategy profile in which each agent sends the message $( \theta , t , 1 )$ is a Nash equilibrium (see Ref. [32]). Such a strategy can be computed in polynomial time since the agents could, for example, all use the complement algorithm to find a t that satisfies at least half of the total number of clauses. Hence, F is fully Nash implementable in polynomial time for polynomial time bounded agents. Since $F ( p , \ \theta ) { \subseteq } ( 1 / 2 ) – \mathrm { M A X - }$ $\operatorname { S A T } ( p , \theta )$ for all $p$ and $\theta , ( 1 / 2 ) – \mathrm { M A X S A T }$ is strongly Nash implementable in polynomial time for polynomial time bounded agents. 5

Since F is implementable and includes every optimal outcome, it follows from Lemma 3.1 that every optimal outcome is a polynomial time equilibrium outcome. Thus, while strong dominant strategy implementation using the Complement Mechanism can eliminate optimal outcomes from occurring, full Nash implementation of F using Repullo’s mechanism would not preclude the possibility of any optimal outcome. The problem we face is that of defining mechanisms so that the suboptimal equilibrium outcomes are not too bad. As we show in the next section, our ability to eliminate suboptimal outcomes is severely limited.

## 7. Upper bounds on approximability

Existing work in mechanism design shows that it is possible to implement a wider range of social choice rules in undominated Nash equilibrium<sup>4</sup> [10,30] and subgame perfect equilibrium<sup>5</sup> [20] than in Nash equilibrium. In Ref. [30], it is observed that for a social choice rule to be fully implementable in Nash, undominated Nash, or subgame perfect equilibrium, it must satisfy Property Q defined below. Property Q must also be satisfied for full implementation in dominant strategies. Therefore, by Proposition 3.1, Property Q must be satisfied for full implementation in polynomial time for polynomial time bounded agents for each of these four equilibrium concepts.

Definition 7.1 . (from Ref. [30]) A social choice rule satisfies Property Q if, for any problem instance $p ,$ whenever $\theta , \theta ^ { \prime }$ and t are such that $t { \in } F ( p , \ \theta )$ and $t \notin F ( p , \theta ^ { \prime } )$ , there is an agent i such that $\theta _ { i } \neq \theta _ { i } ^ { \prime }$ and agent i is not completely indifferent under $\theta _ { i } ^ { \prime }$

Property Q says that, if an outcome goes from being socially desirably under a one preference profile to socially undesirable under a new preference profile, at least one of the agents whose preferences have changed is not completely indifferent under the new preference profile. To see why this property is necessary for full Nash implementation, consider an equilibrium strategy profile $s ^ { * }$ . Fix a preference profile. The equilibrium outcome corresponding to $s ^ { * }$ must be socially desirable if full Nash implementation is achieved. Now suppose agent 1’s preference changes to that of indifference while the other agents’ preferences remain the same. Since agent 1 is indifferent, he cannot deviate from $s ^ { * }$ and improve his utility. Furthermore, none of the other agents can improve their utilities by deviating from $s ^ { * }$ since $s ^ { * }$ is an equilibrium strategy profile under the original preference profile. Therefore, $s ^ { * }$ must remain an equilibrium strategy profile under the new preference profile.

The following lemma shows that the only approximate social choice rules for MAXSAT that can be fully implemented are those that guarantee the number of clauses satisfied is a constant times the total number of clauses rather than a constant times the maximum number of simultaneously satisfiable clauses. This severely limits the social choice rules for MAXSAT that are fully implementable. In particular, consider a social choice rule in which each outcome satisfies c times the total number of agents for some constant c. Since the set of desirable outcomes must be non-empty for each preference profile and since it may be impossible to satisfy more than half of the agents for some profiles, c cannot be larger than 1/2. The Proof of Theorem 7.1 below formalizes this argument.

Lemma 7.1. Let F be a social choice rule such that, for some constant c, $O < c \leq I , \ F ( p , \ \theta ) \subseteq c { - } M A X S A T$ $\mathit ( p , \ \theta )$ for all p and h. Suppose, for some problem instance p and preference profile h, there exists a truth assignment $t { \in } F ( p , \ \theta )$ that satisfies strictly less than cI clauses where I is the number of agents. Then F does not satisfy Property Q.

Proof. Let $F , p , \theta , c ,$ and t be as defined above. For each i such that t satisfies $\theta _ { i } ,$ let $l _ { i }$ be any literal in $\theta _ { i }$ such that $t ( l _ { i } ) { = } \operatorname { T r u e } .$ . Create $\theta ^ { \prime }$ from h by adding $\bar { l } _ { i }$ to every $\theta _ { i }$ that t satisfies. For each $i ,$ either $\theta _ { i } ^ { \prime } = \theta _ { i }$ or agent i is completely indifferent under $\theta _ { i } ^ { \prime }$ . Hence, for $F$ to satisfy Property Q, it must be the case that $t { \in } F ( p , \theta ^ { \prime } )$

Let $N ^ { * } ( \theta ^ { \prime } )$ be the maximum number of simultaneously satisfiable clauses in $\theta ^ { \prime }$ . Since ¯t must satisfy every clause in $\theta ^ { \prime }$ that t does not satisfy and since ¯t must satisfy $\theta _ { i } ^ { \prime }$ V if t satisfies $\theta _ { i } , N ^ { * } ( \theta ^ { \prime } ) { = } I .$ Since the clauses in $\theta$ that t does not satisfy also appear in $\theta ^ { \prime } ,$ , the number of clauses in $\theta ^ { \prime }$ that t satisfies is strictly less than $c I { = } c N ^ { * } ( \theta ^ { \prime } )$ . Therefore, $t \not \in c \mathrm { - } \mathrm { M A X S A T } ( p , \theta ^ { \prime } )$ and, since $c \mathrm { - M A X S A T } ( p , \theta ^ { \prime } ) \supseteq F ( p , \theta ^ { \prime } )$ , tgF( p, hV). Thus, $F$ does not satisfy Property Q. 5

The following theorem shows that it is impossible to strongly implement c-MAXSAT if $c { > } 1 / 2 \mathrm { : }$

Theorem 7.1. Let c be a constant such that $I /$ $2 < c \leq I .$ . Then c-MAXSAT cannot be strongly implemented in dominant strategy, Nash, undominated Nash or subgame perfect equilibrium.

Proof . Let C be any mechanism that strongly implements c-MAXSAT. Let $E ( p , \ \theta )$ be the set of equilibrium outcomes of C for problem instance $p$ and preference profile h. By definition, C fully implements E. Since C strongly implements $\begin{array} { r } { c \mathbf { - M A X S A T } , } \end{array}$ $E ( p , \theta ) \subseteq c \mathbf { - M A X S A T } ( p , \theta )$ for all $p$ and h.

Let $p$ be a problem instance such that the number of agents I is even. Let $\theta _ { i } ^ { \prime } { = } x _ { 1 }$ for $1 \leq i \leq I / 2$ . Let ${ \theta } _ { i } ^ { \prime } \mathrm { { = } } \bar { x } _ { 1 }$ for $I / 2 + 1 \leq i \leq I .$ . Since the maximum number of simultaneously satisfiable clauses is $I / 2$ , no truth assignment can satisfy more than $I / 2$ clauses. Therefore, any $t { \in } E ( p , \theta ^ { \prime } )$ satisfies less than cI clauses in hV. According to Lemma 7.1, this implies that E does not satisfy Property Q. But then E is not fully implementable which is a contradiction since C fully implements $E .$ 5

By Proposition 3.1, Theorem 7.1 also holds for strong implementation in polynomial time for polynomial time bounded agents. Our inability to strongly implement c-MAXSAT for c>1/2 is perhaps not surprising since Theorem 7.1 also implies that the exact social choice rule (take c = 1) is not strongly implementable even when there are no computational restrictions. In other words, we are attempting to use approximation not only to overcome the computational constraints of the problem but also to overcome the game theoretic constraints.

## 8. Conclusion

Using a multiagent version of MAXSAT, we have investigated the difficulties that arise in applying classic results from the mechanism design literature to computationally complex optimization problems. Table 1 summarizes the results presented in this paper.

We have demonstrated that, despite the impossibility results regarding dominant strategy implementation, it is possible to implement an approximate social choice rule for Multiagent MAXSAT in dominant strategy equilibrium. Our results suggest the following general approach to designing mechanisms for computational problems in non-quasilinear environments.

(1) Determine whether the Gibbard –Sattherthwaite Theorem applies. If it does, then dominant strategy implementation is not an option. If it does not apply and the agents are restricted to polynomial time, look for a revelation mechanism to truthfully implement an approximate social choice rule. If the agents are not restricted then non-revelation mechanisms should be considered.

A summary of results on the implementability of MAXSAT and c-MAXSAT<sup>a</sup>

<table><tr><td>Rule</td><td>Dominant strategy</td><td>Nash</td></tr><tr><td>MAXSAT</td><td>TruthfullyNot Truthfully in Poly TimeNot Strongly</td><td>Not Strongly</td></tr><tr><td>(1/2)-MAXSAT</td><td>Truthfully in Poly TimeStrongly in Poly Time</td><td>Strongly in Poly Time</td></tr><tr><td>(&gt;1/2)-MAXSAT)</td><td>Not Strongly</td><td>Not Strongly</td></tr></table>

<sup>a</sup> The negative results regarding strong implementation of MAXSAT and c-MAXSAT for c>1/2 apply to undominated Nash and subgame perfect equilibrium as well. By Proposition 3.1, ‘‘Not Strongly’’ implies ‘‘Not Strongly in Poly Time’’.

(2) If dominant strategy implementation is not possible then find an approximate social choice rule F such that:

(a) F satisfies Property Q.

(b) F is monotonic.

(c) F satisfies the no-veto property.

(d) The problem of checking membership in F is easy.

If such an approximate social choice rule can be found then use Repullo’s mechanism to achieve Nash implementation. (A similar mechanism from Ref. [34] may be more appropriate in some cases.)

We also showed that (1/2)-MAXSAT is the best approximate social choice rule for Multiagent MAX-SAT that can be strongly implemented in dominant strategy, Nash, undominated Nash or subgame perfect equilibrium in spite of the fact that there are many approximation algorithms for the non-multiagent version of this problem that achieve better lower bounds than 1/2. Several authors [1,8,40] provide algorithms for the non-multiagent version of MAXSAT that achieve lower bounds <sub>z</sub> 3/4. Our results, therefore, indicate that it can be much more difficult to design good approximation mechanisms than to design good approximation algorithms. Previously, work by Nisan and Ronen [25] provided conditions under which it is impossible to achieve dominant strategy implementation using approximation mechanisms in quasilinear environments. Our work confirms that the problems of approximation in mechanism design are not confined to dominant strategies or to quasilinear environments.

While the purpose of this paper is not to study quasilinear environments, it should be pointed out that our positive results that a 1/2-approximation is achievable carry over to the quasilinear environment by simply viewing our mechanism as one in which all transfers are 0. The result indicating that 1/2 is the best possible approximation does not necessarily carry over, however. The reason for this is that when the outcome includes transfers of money, it is impossible for an agent to be completely indifferent. The result would also not carry over to any problem in which complete indifference on the part of the agents is impossible.

Future work should consider multiagent versions of other computational problems. Furthermore, in this paper, we consider only complete information environments, i.e., environments in which the agents know each other’s preferences. This is certainly not the case in most real situations. However, developing an understanding of the complete information environment should provide the foundation for further work in understanding the incomplete information problem.

## Acknowledgements

We would like to thank Larry Kranich for the many helpful comments and suggestions.

## Appendix A. P, NP and approximation algorithms

Viewed abstractly, programs take finite length strings as input and produce outputs. The input is thought of as a question and the output the answer. A ‘‘computational problem’’ can be thought of as a mapping of questions into answers. A program is said to solve a computational problem if it gives a correct answer to each question. A program which solves a problem is referred to as an algorithm for the problem and particular input sequences are referred to as problem instances. The complexity of an algorithm is measured by a time function. Time functions bound the ‘‘worst case’’ time, namely the largest number of steps taken by any input of a given length. The ‘‘number of steps used’’ is referred to as the computation time.

Polynomial time is defined as follows:

Definition A.1. An algorithm is said to be polynomial time if its computation time (as a function of input length) is bounded by a polynomial function.

It is unknown whether polynomial time algorithms exist for some problems. For example, no polynomial time algorithm has been found to determine whether an arbitrary CNF Boolean formula is satisfiable. This problem is known in the computer science literature as the Satisfiability Problem or simply SAT. Technically, SAT is not formally defined until one specifies the notation whereby lists of clauses are to be described and presented as input to a program for solving the problem. There are obviously many natural ways to do this and the actual number of input symbols needed to describe a particular set of clauses will vary somewhat with the notation. However, the effects of these variations on the time functions are too small to make a polynomial algorithm non-polynomial or vice versa. Thus, it makes sense to ask the question ‘‘can SAT be solved in polynomial time?’’ without being specific about the notation.

SAT is an example of a ‘‘YES/NO problem’’, namely a problem where the answer for any problem instance is YES or NO. YES/NO problems are called decision problems. Other problems require an answer describing a maximum or a minimum. These problems are referred to as optimization problems. One such problem is a variation on SAT known as MAXSAT.

Definition A.2. The problem MAXSAT is the following: given a list of clauses, what is the maximum number of clauses that can be simultaneously satisfied by an assignment to the variables?

MAXSAT is the problem upon which the results in this paper are based. It is not known whether MAX-SAT can be solved in polynomial time. However, it is obvious that MAXSAT cannot be easier than SAT, because an answer to MAXSAT gives an immediate answer to SAT. If the maximum number of clauses that can be satisfied is equal to the number of clauses, the answer to SAT is YES; and otherwise it is NO. Thus, any evidence that SAT is hard is also evidence that MAXSAT is hard.

If a set of clauses is satisfiable, there is an easy proof that the SAT answer to the problem instance is YES. The proof consists of a proposed assignment to the Boolean variables and verification that the assignment satisfies each clause. By ‘‘easy’’, we mean that the proof can be checked in time polynomial in the instance length. Be sure to notice the difference between checking a proof (easy) and finding a proof (believed to be hard).

The class of YES/NO problems with easy to check proofs is called NP. The NP stands for ‘‘nondeterministic polynomial’’ which means that, if you guess a proof (guessing is nondeterministic), you can verify the proof in polynomial time. A major question in computer science and mathematics is ‘‘can all problems in NP be solved in polynomial time?’’ Letting P be the set of YES/NO problems solvable in polynomial time, the question is expressed simply as ‘‘does P= NP?’’

In Ref. [4], it was proved that, if SAT is in P, then P = NP. In other words, if there are any problems in NP that are not in P, then SAT is one of these problems. Since it is hard to believe that all problems in NP can be solved in polynomial time, it is hard to believe that SAT can be solved in polynomial time. The key idea in Cook’s proof is that, given a solver for SAT, only a polynomial number of additional steps would be needed to solve any problem in NP. A problem with this property is called NP-hard. Because of Cook’s result, NP-hardness can be proven by showing that only a polynomial number of additional steps is needed to solve SAT (or any other known NPhard problem). MAXSAT is NP-hard because, given a solver for MAXSAT, the answer to SAT is obtained simply by comparing the maximum number of satisfiable clauses with the number of clauses.

## A.1. Approximation algorithms

When faced with an NP-hard optimization problem, we cannot hope to find a polynomial time algorithm assuming P p NP. However, it may be that we would be willing to settle for approximately optimal solutions. In that case, we would like to develop a polynomial time approximation algorithm. For example, Ref. [11] provides two polynomial time approximation algorithms for MAXSAT. Johnson’s first approximation algorithm for MAXSAT guarantees that at least 1/2 of the maximum number of simultaneously satisfiable clauses are satisfied while his second algorithm guarantees that the number of clauses satisfied will be within a factor of 2/3 of the optimal. Several authors [1,8,40] provide algorithms for MAXSAT that achieve lower bounds <sub>z</sub> 3/4 (see Ref. [2] for a survey of approximation algorithms for MAXSAT and Ref. [39] for an introduction to approximation algorithms).

When faced with the problem of designing mechanisms that must solve computationally difficult problems, we will no doubt have to resort to mechanisms that find approximately optimal solutions. For example, in Ref. [25], an existing approximation algorithm for the task scheduling problem was used to create a truthful mechanism for their multiagent version of the problem. In this paper, we showed that creating a good approximation mechanism is not always an easy thing to do even when we have several good approximation algorithms for the problem at hand.

## References

[1] T. Asano, Approximation algorithms for MAX SAT: Yannakakis vs. Goemans and Williamson, Proceedings of the 3rd Israel Symposium on Theory and Computing Systems, Ramat Gan, Israel, 1997, pp. 24 – 37.

[2] R. Battiti, Approximation algorithms and heuristics for MAX-SAT, in: D.-Z. Zhu, P.M. Pardalos (Eds.), Handbook of Combinatorial Optimization, vol. 1, Kluwer Academic Publishing, Norwell, MA, 1998, pp. 77– 148.

[3] E. Ben-Porath, Repeated games with finite automata, Journal of Economic Theory 59 (1993) 17 – 32.

[4] S. Cook, The complexity of theorem proving procedures, Proceedings of the 3rd ACM Symposium on the Theory of Computing, ACM, New York, NY, 1971, pp. 151– 158.

[5] T. Cormen, C. Leiserson, R. Rivest, C. Stein, Introduction to Algorithms, MIT Press, Cambridge, MA, 2001.

[6] M. Garey, D. Johnson, Computers and intractability: a guide to the theory of NP-completeness, W. H. Freeman, New York, NY, 1979.

[7] A. Gibbard, Manipulation of voting schemes: a general result, Econometrica 41 (1973) 587– 602.

[8] M. Goemans, D. Williamson, Improved approximation algorithms for maximum cut and satisfiability problems using semidefinite programming, Journal of the ACM 42 (1995) 1115– 1145.

[9] J. Hopcroft, J. Ullman, Introduction to Automata theory, languages, and computation, Addison-Wesley, Reading, MA, 1979.

[10] M. Jackson, T. Palfrey, S. Srivastava, Undominated Nash implementation in bounded mechanisms, Games and Economic Behavior 6 (1994) 474 – 501.

[11] D. Johnson, Approximation algorithms for combinatorial problems, Journal of Computer and System Sciences 9 (1974) 256– 278.

[12] S. Kraus, Strategic negotiation in multiagent environments, MIT Press, Cambridge, MA, 2001.

[13] D. Lehmann, L.I. O’Callaghan, Y. Shoham, Truth revelation in approximately efficient combinatorial auctions, Journal of the ACM 49 (5) (2002) 577 – 602.

[14] A. Mas-Colell, M. Whinston, J. Green, Microeconomic theory, Oxford Univ. Press, New York, NY, 1995.

[15] E. Maskin, The theory of implementation in Nash equilibrium: a survey, in: L. Hurwicz, D. Schmeidler, H. Sonnenschein (Eds.), Social Goals and Social Organization: Essays in Mem-

ory of Elisha Pazner, Cambridge Univ. Press, New York, NY, 1985, pp. 173–204.

[16] E. Maskin, T. Sjo¨ stro¨ m, Implementation theory, in: K. Arrow, A. Sen, K. Suzumura (Eds.), Handbook of Social Choice and Welfare, North-Holland, Amsterdam, 2002.

[17] R. McKelvey, Game forms for Nash implementation of general social choice correspondences, Social Choice and Welfare 6 (1989) 139– 156.

[18] D. Monderer, M. Tennenholtz, H. Varian, Special issue: economics and artificial intelligence, Games and Economic Behavior 35 (2001) 1 – 5.

[19] J. Moore, Implementation, contracts and renegotiation in environments with complete information, in: J.-J. Laffont (Ed.), Advances in Economic Theory: Sixth World Congress, Cambridge Univ. Press, Cambridge, UK, 1992, pp. 182 – 282.

[20] J. Moore, R. Repullo, Subgame perfect implementation, Econometrica 56 (1988) 1191 – 1220.

[21] A. Neyman, Cooperation, repetition and automata, in: S. Hart, A. Mas-Colell (Eds.), Cooperation: Game Theoretic Approaches, Volume NATO ASI-Series F vol. 155, Springer, New York, NY, 1997, pp. 233 – 255.

[22] A. Neyman, D. Okada, Two person repeated games with finite automata, International Journal of Game Theory 29 (3) (2000) 309 – 325.

[23] N. Nisan, A. Ronen, Algorithmic mechanism design, Proceedings of the 31st Annual ACM Symposium on Theory of Computing, ACM, New York, NY, 1999, pp. 129 – 140, Atlanta, GA.

[24] N. Nisan, A. Ronen, Computationally feasible VCG mechanisms, Proceedings of the Second ACM Conference on Electronic Commerce, 2000 October, pp. 242– 252.

[25] N. Nisan, A. Ronen, Algorithmic mechanism design, Games and Economic Behavior 35 (2001) 166 – 196.

[26] T.C. O’Connell, R.E. Stearns, Polynomial time mechanism design for collective decision making, in: S. Parsons, P. Gmytrasiewicz, M.J. Wooldridge (Eds.), Game Theory and Decision Theory in Agent-Based Systems, Kluwer, Boston, MA, 2002, pp. 197–216.

[27] T.C. O’Connell, R.E. Stearns, On finite strategy sets for finitely repeated zero-sum games, Games and Economic Behavior 43 (2003) 107– 136.

[28] T.C. O’Connell. Bounded Rationality in Repeated Games and Mechanism Design for Agents in Computational Settings. PhD thesis, Department of Computer Science, University at Albany, SUNY, Albany York, NY 12222, (2000).

[29] T. Palfrey, Implementation in Bayesian equilibrium: the multiple equilibrium problem in mechanism design, in: J.-J. Laffont (Ed.), Advances in Economic Theory: Sixth World Congress, Cambridge Univ. Press, Cambridge, UK, 1992, pp. 283–321.

[30] T. Palfrey, S. Srivastava, Nash implementation using undominated strategies, Econometrica 59 (1991) 479 – 501.

[31] C. Papadimitriou, On games with a bounded number of states, Games and Economic Behavior 4 (1992) 122– 131.

[32] R. Repullo, A simple proof of Maskin’s theorem on Nash implementation, Social Choice and Welfare 4 (1987) 39 – 41.

[33] J. Rosenschein, G. Zlotkin, Rules of encounter: designing conventions for automated negotiation among computers, MIT Press, Cambridge, MA, 1994.

[34] T. Saijo, Strategy space reductions in Maskin’s theorem: sufficient conditions for Nash implementation, Econometrica 56 (3) (1988) 693– 700.

[35] T. Sandholm, Distributed rational decision making, in: G. Weiss (Ed.), Mutiagent Systems: A Modern Approach to Distributed Artificial Intelligence, MIT Press, Cambridge, MA, 1999, pp. 201–258.

[36] M. Satterthwaite, Strategy-proofness and Arrow’s conditions: existence and correspondence theorems for voting procedures and social welfare functions, Journal of Economic Theory 10 1975, pp. 187– 217.

[37] R.E. Stearns, Memory bounded game playing automata. Technical Report 547, Institute for Mathematical Studies in the Social Sciences, Stanford University, (1989).

[38] M. Tenneholtz, N. Kfir-Dahav, D. Monderer, Mechanism design for resource bounded agents, Proceedings of the Fourth International Conference on Multiagent Systems, IEEE Computer Society, Los Alamitos, CA, 2000, pp. 309 – 316, Boston, MA.

[39] V.V. Vazirani, Approximation algorithms, Springer, New York, NY, 2001.

[40] M. Yannakakis, On the approximation of maximum satisfiability, Journal of Algorithms 17 (1994) 475 – 502.
