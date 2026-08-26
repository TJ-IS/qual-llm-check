---
otero_id: 15644
otero_key: "43P4HWH9"
title: "Average-case analysis of VCG with approximate resource allocation algorithms"
authors: "Yevgeniy Vorobeychik; Yagil Engel"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.03.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Average-case analysis of VCG with approximate resource allocation algorithms 16

Yevgeniy Vorobeychik <sup>a,</sup>⁎, Yagil Engel <sup>b</sup>

<sup>a</sup> Sandia National Laboratories, P.O. Box 969, Mailstop 9159, Livermore, CA 94551-0969, United States <sup>b</sup> IBM Research, Haifa, Israel

## a r t i c l e i n f o

Article history: Received 29 September 2010 Received in revised form 16 January 2011 Accepted 17 March 2011 Available online 23 March 2011

Keywords: Algorithmic mechanism design Game theory VCG Average-case analysis

## a b s t r a c t

The Vickrey–Clarke–Groves (VCG) mechanism offers a general technique for resource allocation with payments, ensuring allocative ef<sup>fi</sup>ciency while eliciting truthful information about preferences. However, VCG relies on exact computation of an optimal allocation of resources, a problem which is often computationally intractable, and VCG that uses an approximate allocation algorithm no longer guarantees truthful revelation of preferences. We present a series of results for computing or approximating an upper bound on agent incentives to misreport their preferences. Our <sup>fi</sup>rst key result is an incentive bound that uses information about average (not worst-case) performance of an algorithm, which we illustrate using combinatorial auction data. Our second result offers a simple sampling technique for amplifying the dif<sup>fi</sup>culty of computing a utilityimproving lie. An important consequence of our analysis is an argument that using state-of-the-art algorithms for solving combinatorial allocation problems essentially eliminates agent incentives to lie.

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

Mechanism design provides a useful practical paradigm for competitive resource allocation when agent preferences are uncertain. Perhaps of greatest practical signi<sup>fi</sup>cance has been the <sup>fi</sup>eld of auction theory [9], and, in particular, the design of combinatorial auctions [2]. In a combinatorial auction, bidders are allowed to submit bids on all subsets of a given set of items.<sup>1</sup> The auctioneer must then solve the winner determination problem (WDP), computing which subsets of the goods will be allocated to which bidders, with the objective of maximizing allocative ef<sup>fi</sup>ciency.

Historically, the focus of mechanism design has been on engineering the incentives for participants to reveal their preferences truthfully, with computational aspects largely ignored. To this end, VCG has been advanced as one of the central schemes [15]. Computer Scientists have observed, however, that VCG coupled with approximate algorithms for WDP in combinatorial auctions fails to incentivize truthful revelation of preferences in most reasonable settings [17]. Since WDP is well known to be NP-Hard [11], and even hard to approximate [18], using VCG in practical combinatorial auction settings seems hopeless.

We argue that these hardness results may at times be unnecessarily pessimistic, and while the worst-case incentives to lie may exist in VCGbased mechanisms, effective incentives to lie may be negligible if the approximation algorithms used are very good in practice. Speci<sup>fi</sup>cally, we present a series of results, both theoretical and experimental, which allow the designer to measure – and in some cases address – the severity of the incentive problem with VCG-based mechanisms. First, we offer general techniques to empirically assess incentive effects of speci<sup>fi</sup>c algorithms based on average-case bounds. For example, if an algorithm can solve the allocation problem exactly in almost every instance, there are no incentives to deviate from truthfulness in the Bayes-Nash sense. We operationalize this bound in combinatorial auctions, illustrating how the use of a simulation-based model of bidder valuation distribution allows the designer to obtain precise probabilistic con<sup>fi</sup>- dence bounds on agent incentives to lie. Our results provide some evidence that, at least in the VCG-based combinatorial auction setting, incentives of players to lie about their preferences are rather small. Furthermore, we show that the designer can use sampling to reduce the likelihood that any player will compute an improving deviation. Signi<sup>fi</sup>cantly, this is a typical-case, and not a worst-case result. Finally, we offer a simulation-based technique to obtain relatively tight, albeit approximate, bounds on incentives of agents to misreport their preference. We use this approach to offer some qualitative evidence that the incentives to lie in some combinatorial auction settings decrease with increasing problem size.

## 2. Related work and motivation

There has been considerable literature attempting to address the incentives to misreport preferences that emerge when approximate allocation algorithms are used together with the VCG price scheme, particularly in the context of combinatorial auctions. Here we give several representative examples. Sanghvi and Parkes [20] demonstrate that computing an improving deviation in VCG-based combinatorial auctions is NP-Hard, although this worst-case result is dif<sup>fi</sup>cult to rely on in practice. Lavi and Swamy [10] present a truthful (in expectation) mechanism when the approximation algorithm bounds the integrality gap of LP relaxation, while Lehmann, O'Callaghan, and Shoham [12] and Mu'alem and Nisan [16] obtain general truthful mechanisms for combinatorial auctions when bidders are “single-minded” (i.e., each has a positive value for exactly one bundle of items). Dobzinski, Nisan, and Shapira [5] present a framework for designing truthful approximation algorithms, and demonstrate instances with an asymptotically optimal worst-case bound for the general WDP. Nisan and Ronen [17] develop a mechanism called second-chance, in which players are not capable of computing a bene<sup>fi</sup>cial lie.

The extensive literature addressing the incentive problems of approximate WDP implicitly suggests that such problems are critical. Field practitioners of combinatorial auctions, however, seem to rarely, if ever, have come up against the worst-case complexity issues [3,4]. Furthermore, the majority of combinatorial auction problems that have been studied in simulation can be solved very fast using modern algorithms [14,18,19], and, indeed, the general-purpose CPLEX integer programming tool is usually very effective [19].

There thus appears to be a gap between theory, which views the incentive problem of VCG-based mechanisms as severe, and practice, which ignores it almost entirely. We believe that one important reason for this gap is that mechanisms that have been developed to be both truthful and to provide suitable approximation guarantees tend to be somewhat complicated to implement and dif<sup>fi</sup>cult to communicate. Frequently, they randomize allocation, something that is dif<sup>fi</sup>cult to operationalize because of fairness considerations (for example, Dobzinsky, Nisan, and Shapira [5] suggest withholding a random sample of bidders from consideration, an idea which some bidders may <sup>fi</sup>nd disagreeable). Furthermore, worst-case guarantees provided tend to be so poor as to be of little practical consolation. Another important reason is that whereas literature to date has been motivated by the desire to prevent the worst-case performance, state-of-the-art algorithms (e.g., CPLEX) solve most realistic allocation problems (such as WDP) to optimality, and the worst case is rarely encountered in practice. Consequently, one may expect that in reality incentives to misreport preferences are often quite low. While practitioners appear to grasp this, they have, to date, no principled means to verify it. Our goal is to offer mechanism designers techniques to quantify (and, sometimes, to reduce) the incentives of bidders to lie, while capturing information about the distribution of the performance of their algorithm, rather than merely its worst-case performance.

A downside to our approach is that it is no longer distribution-free. Distribution-free mechanism design has clear advantages. First, we rarely truly know the distribution of agent preferences in practice, and attempts to glean information about it are likely to be gamed if the stakes are high enough. We also prefer not to assume that agents have common knowledge of such information either. Furthermore, economists have long been striving to reduce the common knowledge requirements in mechanism design [23]. Ultimately, a distribution-free guarantee is certainly most satisfying, as it relies on minimal assumptions. Many situations, however, to not lend themselves easily to simple, natural distribution-free mechanisms. Additionally, at times information about the distribution is available in some form. For example, combinatorial auctions are often run in high-stakes settings (such as wireless spectrum auctions), where there is considerable public information about the participants. Furthermore, a test suite has been developed for combinatorial auctions precisely with the goal of generating realistic problem instances [14]. Finally, there has already been much experience running large-scale combinatorial auctions, with state-of-the-art algorithms proving thus far quite capable [3]. All of this suggests that there may be many auction settings where much distributional information is available, and which therefore lend themselves well to the approaches we propose.

## 3. Preliminaries

In our setting, each player $i \in I$ submits to a central designer his utility function, as indexed by his type $t _ { i } \in T _ { i } .$ Let O be the set of outcomes (e.g., feasible allocations), I be a set of n players, and let $T = T _ { 1 } \times \cdots \times T _ { n }$ be the joint type set. Assume that O and T for all i ∈ I are non-empty and compact. Let $F ( \cdot )$ be a probability distribution over joint player types and let $u _ { i } \big ( t _ { i } , o , p _ { i } \big )$ be player utility functions where $o \in O$ typically depends on joint player report t and $p _ { i }$ is the payment received by the agent (which is negative when the agent is paying the designer). While we may hope that all players submit their types honestly, they may choose to lie, submitting some $t ^ { \prime } { } _ { i }$ instead of $t _ { i } ,$ and these lies could, in general, be a function of true type $t _ { i \cdot }$

We assume that agent utility functions are quasi-linear in payments $p _ { i } ,$ that is u<sub>i</sub>(t<sub>i</sub>, $o , p _ { i } ) = \nu _ { i } ( t _ { i } , o ) + p _ { i } ,$ where $\nu _ { i } ( t _ { i } , ~ o )$ is the underlying value that player i with type $t _ { i }$ has for outcome $^ { 0 ; }$ we assume it to be continuous in both arguments. A mechanism is a function that chooses an outcome o and assigns the payments p for all players i given a joint report of types $t \in T .$ Thus, we use $o ( t )$ and $p _ { i } ( t )$ to indicate such choices as made by some speci<sup>fi</sup>ed mechanism.

A central aspect of mechanism design is the prediction of agent play for a given choice of a mechanism. Typically the role of such predictions is played by equilibrium concepts. We appeal to two such concepts below (de<sup>fi</sup>ned with respect to direct revelation mechanisms, that is, mechanisms which attempt to truthfully elicit player preferences). Under a dominant strategy equilibrium each player is (weakly) best off reporting his true type no matter what other players do. Under a Bayes-Nash equilibrium, on the other hand, each player maximizes his expected utility by reporting his true type $t _ { i } ,$ assuming that all other players are honest. Both equilibrium concepts admit natural notions of approximation: in an -dominant strategy equilibrium, a player can gain no more than  by deviating, no matter what the opponents do, whereas an -Bayes-Nash equilibrium guarantees that the expected gain to any player from deviation is at most $\epsilon ,$ with expectation taken with respect to the joint type distribution.

A useful measure of strategic stability is that of game-theoretic regret. While in general this measure can be de<sup>fi</sup>ned for any joint strategy pro<sup>fi</sup>le, we use it only to gauge the regret of truthful reporting. Hence, we use a simpler de<sup>fi</sup>nition, with $\tilde { \epsilon } = E _ { F } [ \epsilon ( t ) ] = E _ { F } [ \operatorname* { m a x } _ { i } \epsilon _ { i } ( t _ { i } ) ]$ where

$$
\epsilon_ {i} (t _ {i}) = \max _ {t _ {i} ^ {\prime} \in T _ {i}} E _ {F} \left[ u _ {i} \left(t _ {i}, o \left(t _ {i} ^ {\prime}, t _ {- i}\right), p _ {i} \left(t _ {i} ^ {\prime}, t _ {- i}\right)\right) - u _ {i} \left(t _ {i}, o (t), p (t)\right) | t _ {i} \right].
$$

In words, it is the maximum expected bene<sup>fi</sup>t any player can obtain from reporting untruthfully.

A widely studied goal of mechanism design, and one we focus on here, is that of maximizing social welfare, or the sum of player valuations. Formally, de<sup>fi</sup>ne social welfare to be

$$
V (t, o) = \sum_ {i \in I} v _ {i} (t _ {i}, o),
$$

where o is an outcome and t is a joint type pro<sup>fi</sup>le. Let $o ^ { * } : T  O$ denote the welfare optimal (ef<sup>fi</sup>cient) outcome (allocation) and let

$$
V ^ {*} (t) = \sum_ {i \in I} v _ {i} \big (t _ {i}, o ^ {*} (t) \big) = \max _ {o \in O} \sum_ {i \in I} v _ {i} (t _ {i}, o)
$$

be the maximum welfare achieved for a type pro<sup>fi</sup>le t. Let $V ^ { * } =$ $\scriptstyle \operatorname* { m a x } _ { t \in T } V ^ { * } ( t )$ . It is well known that optimal allocation can be achieved as a truthful dominant strategy equilibrium by using Groves payments [15], with $\begin{array} { r } { p _ { i } ( t ) = \sum _ { j \neq i } { \nu } _ { j } ( t _ { j } , o ^ { * } ( t ) ) + h _ { i } ( t _ { - i } ) } \end{array}$ . Here $h _ { i }$ is any real-valued function of the types reported by other players; for simplicity of exposition, we set it to $0 . ^ { 2 }$

Let $g : T  { \cal O }$ be an algorithm for computing an approximately ef<sup>fi</sup>cient allocation.<sup>3</sup> We say that $g ( \cdot )$ is an α-approximation if $V ^ { * }$ $( t ) \leq \alpha V _ { g } ( t )$ for any $t \in T .$ Since $g$ <sup>g</sup>may compute only a suboptimal <sup>g</sup>allocation, we let $V _ { g } ( t )$ be welfare at the allocation $g ( t )$ , that is $V _ { g } ( t ) =$ $\sum { _ { i \in I } { \nu _ { i } } } ( t _ { i } , g ( t ) )$ <sup>g</sup>. De<sup>fi</sup>ne VCG-based payments by $\begin{array} { r } { p _ { i } ^ { g } ( t ) = \sum _ { j \neq i } \bar { \nu _ { j } } ( t _ { j } , \ g } \end{array}$ $( t ) ) + h _ { i } ( t _ { - i } )$ . Hence, the VCG-based mechanism selects an outcome according to g, and the players receive payments $p _ { i } ^ { g } ( t )$

## 4. Connecting approximation and incentives

We begin our endeavor by exhibiting a simple bound that connects the approximation quality of an algorithm to the players' incentives to misreport preferences (both in the worst-case sense), due to Kothari, et al. [8].

Theorem 1. Suppose that $g$ is an α-approximation algorithm. Then truthful reporting is an -dominant strategy equilibrium $f o r \epsilon = \frac { \alpha - 1 } { \alpha } V ^ { * }$

While this bound is intuitive and easy to use in principle, in many interesting settings it is much too crude due to its worst-case nature. For example, the best known approximation ratio in combinatorial auctions is 2 (speci<sup>fi</sup>cally, a greedy algorithm is a 2-approximation when player valuations are submodular [13]). From a practical perspective, the resulting bound of $\frac { V ^ { * } } { 2 }$ is hardly encouraging: if the incentives to lie are as high as 50% of welfare, then we can safely say that honesty would be remarkably altruistic.

Given this state of affairs in combinatorial auctions, one may expect practitioners to worry about incentives. Many real problems, however, are “easy” in that the optimal or nearly optimal allocation can be found extremely fast in practice. Thus, while an algorithm may prove very bad in the worst case, it may be quite effective in a typical case. Our goal now is to incorporate this “empirical” <sup>fl</sup>avor into the analysis of incentives to lie.

To begin, suppose that, somehow, we have an approximation bound for $_ g$ that is a known function of α(t) for all $t \in T .$ In the most trivial case, it could be just a <sup>fi</sup>xed α, reducing the setup to the worstcase analysis above. Alternatively, we may be able to split the set of type pro<sup>fi</sup>les into subsets $T ^ { 1 } , T ^ { 2 } , \dots$ , and obtain much better uniform bounds on some of these subsets than the worst case analysis would allow. For example, perhaps we know that for some large subset of combinatorial auction problems we can compute exact or nearly exact optimal allocation quickly. In any case, presently we will see that we need not even construct $\alpha ( t )$ for all possible type pro<sup>fi</sup>les, but can obtain probabilistic bounds based on a sample of a <sup>fi</sup>nite subset of these.

Our <sup>fi</sup>rst key result echoes Theorem 1, although we must weaken the approximate equilibrium notion to Bayes-Nash.<sup>4</sup>

Theorem 2. Suppose that the algorithm $g$ is an α(t)-approximation. Then a player i can gain at most $\epsilon _ { i } \big ( t _ { i } \big )$ <sup>g</sup>when others are playing truthfully, where

$$
\epsilon_ {i} (t _ {i}) = E _ {t _ {- i}} \biggl [ \frac {\alpha (t) - 1}{\alpha (t)} V ^ {*} (t) | t _ {i} \biggr ].
$$

The proofs of this and other results are in the Appendix $\mathtt { B } . ^ { 5 }$

Corollary 3. Suppose that the algorithm $g$ is an α(t)-approximation Then truthful reporting constitutes an -Bayes-Nash equilibrium for

$$
\epsilon = n E _ {t} \biggl [ \frac {\alpha (t) - 1}{\alpha (t)} V ^ {*} (t) \biggr ].
$$

Proof. Here we measure the expected bene<sup>fi</sup>t to deviation using the corresponding game-theoretic regret.

$$
\begin{array}{c} E _ {t} [ \epsilon (t) ] = E _ {t} [ \max _ {i} \epsilon_ {i} (t _ {i}) ] \leq E _ {t} [ \sum_ {i} \epsilon_ {i} (t _ {i}) ] = \sum_ {i} E _ {t _ {i}} [ \epsilon_ {i} (t _ {i}) ] \\ = \sum_ {i} E _ {t} \bigg [ \frac {\alpha (t) - 1}{\alpha (t)} V ^ {*} (t) \bigg ] = n E _ {t} \bigg [ \frac {\alpha (t) - 1}{\alpha (t)} V ^ {*} (t) \bigg ]. \end{array}\tag{□}
$$

Corollary 3 gives us a bound on the incentives of any player to lie that can incorporate full information about the distribution of algorithmic performance $\alpha ( t )$ induced by the distribution of instances (player preferences) F. Our use of the sum bound for the maximum, however, loses considerable tightness as compared to Theorem 1. Below we investigate, <sup>fi</sup>rst theoretically (Section 5) and later empirically (Section 6), the situations in which our average-case bound has bite.

## 5. Illustration of the non-uniform incentive bound

To illustrate an application of the non-uniform bound on the incentives to lie (i.e., Corollary 3), suppose that the space of joint types T can be partitioned into “easy” and “hard” type pro<sup>fi</sup>les, that is, $T = T \cup { \overline { { T } } }$ . Let $\mathbf { \alpha } \propto s u p _ { t \in \underline { { T } } } \mathbf { \alpha } \alpha ( t )$ and $\overline { { \alpha } } = s u p _ { t \in \overline { { T } } } \alpha ( t )$ and assume that <sup>  </sup>α≤α. For example, T can be the set of combinatorial auction <sup> </sup>problem instances for which solutions are relatively easy to compute given state-of-the-art optimization tools (perhaps very good approximations, i.e., small α, can be obtained very fast for these instances). <sup></sup>T, on the other hand, can be the set of those instances for which the worst-case performance of an algorithm is realized. Then, after some algebraic manipulation we obtain

$$
\begin{array}{l} \mathrm{E} _ {t} \left[ \frac {\alpha (t) - 1}{\alpha (t)} V ^ {*} (t) \right] = \int_ {\underline {{T}}} \frac {\alpha (t) - 1}{\alpha (t)} V ^ {*} (t) d F (t) + \int_ {\overline {{T}}} \frac {\alpha (t) - 1}{\alpha (t)} V ^ {*} (t) d F (t) \\ \leq \frac {\underline {{\alpha}} - 1}{\underline {{\alpha}}} \int_ {\underline {{T}}} V ^ {*} (t) d F (t) + \frac {\overline {{\alpha}} - 1}{\overline {{\alpha}}} \int_ {\overline {{T}}} V ^ {*} (t) d F (t) \\ = \frac {\underline {{\alpha}} - 1}{\underline {{\alpha}}} E _ {t} [ V ^ {*} (t) ] - \frac {\underline {{\alpha}} - 1}{\underline {{\alpha}}} \int_ {\overline {{T}}} V ^ {*} (t) d F (t) \\ \quad + \frac {\overline {{\alpha}} - 1}{\overline {{\alpha}}} \int_ {\overline {{T}}} V ^ {*} (t) d F (t) \\ \leq \frac {\underline {{\alpha}} - 1}{\underline {{\alpha}}} E _ {t \sim F | \underline {{T}}} [ V ^ {*} (t) ] \\ \quad + \left(\frac {1}{\underline {{\alpha}}} - \frac {1}{\overline {{\alpha}}}\right) V _ {\overline {{T}}} ^ {*} F (\overline {{T}}). \end{array}
$$

Note that since $\left( \frac { 1 } { \underline { { \alpha } } } { - } \frac { 1 } { \overline { { \alpha } } } \right) V ^ { * }$ is just a constant, as the probability measure of “hard” instances becomes small, the incentives for players to deviate approach $\frac { \alpha - 1 } { \alpha } E _ { t \sim F | L } \left[ V ^ { * } ( t ) \right]$ . Hence the following corollary.

Corollary 4. Suppose that $F ( { \overline { { T } } } ) = 0 .$ . Then truthful reporting constitutes an -Bayes-Nash equilibrium $f o r \epsilon = n \frac { \alpha - 1 } { \alpha } E _ { t \sim F | T } \left[ V ^ { * } ( t ) \right]$

In the special case when $\alpha = 1$ (that is, easy instances can be solved exactly in a relatively short time) as is the case in many combinatorial auction settings, and when $F ( { \overline { { T } } } ) = 0 ,$ , that is, when the probability of drawing a hard problem is ${ \dot { 0 } } ,$ truthful reporting is a Bayes-Nash equilibrium. Hence the following direct corollary.

Corollary 5. Suppose that $\alpha = 1$ and $F ( { \overline { { T } } } ) = 0 .$ . Then the strategy $s _ { i }$ $\left( t _ { i } \right) = t _ { i } -$ <sub>that is, truthfully reporting actual preferences – is a Bayes-Nash</sub> equilibrium under the allocation algorithm $g .$

$$
E _ {t} [ \epsilon (t) ] = n E _ {t} \left[ \frac {\alpha (t) - 1}{\alpha (t)} V ^ {*} (t) \right] = n \frac {\underline {{\alpha}} - 1}{\underline {{\alpha}}} E _ {t} [ V ^ {*} (t) ] = 0\tag{□}
$$

Corollaries 4 and 5 are mainly conceptual observations. In practice, we can rarely know that, for example, $F ( { \overline { { T } } } ) = 0$ . Nevertheless, as we demonstrate below, we can obtain practical probabilistic bounds based on Corollary 3.

## 6. Applying the non-uniform incentive bound

A key question that stems from the above analysis is how a mechanism designer would determine an incentive bound for his algorithm in practice. We would not, for example, want to require the designer to obtain a non-trivial α(t) for every $t \in T .$ Rather, we offer the following empirical approach:

1. Obtain or construct a simulator that allows one to sample joint player types $t \in T$ according to $F ;$

2. Collect a set of K joint type samples $t ^ { 1 } , . . . , t ^ { K } ;$

3. For each $t ^ { k } ,$ compute $V _ { q } ( t ^ { k } )$ and $V ^ { * } ( t ^ { k } )$ (or an upper bound $\overline { { V } } ^ { * } ( t ^ { k } )$ on $V ^ { * } ( t ^ { k } )$ <sup>g</sup>, which could be obtained, for example, using LP relaxation instead of solving the mixed integer program for this instance); instance);

4. Compute $\alpha ( t ^ { k } ) = { \frac { V ^ { * } ( t ^ { k } ) } { V _ { g } ( t ^ { k } ) } } , \operatorname { l e t } { \hat { Z } } ( t ^ { k } ) = { \frac { \alpha ( t ^ { k } ) - 1 } { \alpha ( t ^ { k } ) } } V ^ { * } \big ( t ^ { k } \big )$ , and de<sup>fi</sup>ne $\hat { Z } = \frac { 1 } { K } \sum _ { k } ^ { K } \hat { Z } \Big ( t ^ { k } \Big )$ ;

5. Compute a probabilistic bound based on ${ \hat { Z } } .$

The <sup>fi</sup>rst step requires a designer to either obtain or construct a simulator. This seems rather demanding, but may be necessary to do for a high-stakes problem anyway. Moreover, in the case of combinatorial auctions, a state-of-the-art simulator to generate realistic problem instances is already publicly available [14].

For the last step, we have a few options. A most general option would be to use a distribution-free bound $( \mathbf { e . g . }$ , Hoeffding inequality), but these tend to be very loose. Instead, we assume that Z<sup>ˆ</sup> is normally distributed (an assumption that is justi<sup>fi</sup>ed by the Central Limit Theorem when K is large; Central Limit Theorem applies here since $\hat { Z } ( t ^ { k } )$ are i.i.d. and our assumptions of continuity of $\nu _ { i } ( \cdot )$ and compactness of T imply that the variance of $\hat { Z } ( t ^ { k } )$ is <sup>fi</sup>nite). Suppose we use $s ^ { 2 } \left( \hat { Z } ( t ^ { k } ) \right) / \bar { K }$ (where $s ^ { 2 } ( \cdot )$ is the sample variance) as an estimate of the variance o $: { \hat { Z } } .$ Then,

$$
E _ {t} \left[ \frac {\alpha (t) - 1}{\alpha (t)} V ^ {*} (t) \right] \leq \hat {Z} + z _ {\delta} \sqrt {\frac {s ^ {2} (\hat {Z} (t ^ {k}))}{K}}\tag{1}
$$

with probability at least $1 - \delta ,$ where $z _ { \delta }$ is the value of Normal distribution at $1 - \delta .$

## 6.1. Example: combinatorial auctions

To illustrate the techniques introduced above, we now offer an incentive analysis of combinatorial auctions based on auction instances (in our notation, $t ^ { k } )$ generated by CATS [14]. Since the absolute values of the bounds are not very meaningful, we give them as fractions of $V ^ { * }$ While $V ^ { * }$ is actually unknown, note that $\hat { Z } / V ^ { * } { \le } \hat { Z } / \operatorname* { m a x } _ { k } V ^ { * } ( t ^ { k } )$ , so below we report $\hat { Z } ^ { ' } = \hat { Z } / \operatorname* { m a x } _ { k } V ^ { * } \big ( t ^ { k } \big )$ : Additionally, CATS generates a set of bids, but does not specify the number of players (which could therefore be arbitrary). Consequently, we ultimately report bounds as multiples of $n V ^ { * }$

The data set we used is composed of (a) a set of samples with 1000 bids on 144 goods (1K-144), (b) a set with 1000 bids on 256 goods (1K-256), (c) a set with 2000 bids on 64 goods (2K-64), and (d) a set with varying problem sizes (varsize). Each set contains 5000 samples, 500 for each of 10 different distributions. The data include the result obtained by CPLEX which ran to optimality, the results obtained by CASS [6] after about 7500 s for 1K-144 and 1K-256, or 44,000 s for the other datasets, and, for the dataset 1K-256, the result obtained by the Gonen–Lehmann (GL) algorithm [7].<sup>6</sup>

We computed the bound on the incentives of agents to lie for each dataset, as well as for the union set. For each one we include the data for all CATS distributions except “arbitrary”. For $g ( t )$ we used the following combination: we used the result returned by CPLEX for a sampled pro<sup>fi</sup>le $t ^ { k }$ if it was obtained in at most S seconds; otherwise the result returned by CASS was used. We varied the time limit S between 500 and 60,000 s (about 16.6 h). The longer time limits are reasonable for high volume auctions in which a lot of money is at stake.<sup>7</sup>

In Fig. 1 (left), we show the resulting bound for each dataset as a function of the time limit, which allows us to quantify the tradeoff between the amount of time given to the algorithm and regret (incentives for players to lie).<sup>8</sup> The bounds are computed as explained above, with con<sup>fi</sup>dence level $1 - \delta = 0 . 9 5$ . The chart for the dataset of 1K-144 is omitted because the $\hat { Z }$ is zero (all instances were quickly solved to optimality). In this case, we can obtain an upper bound of 0.0006 on the proportion of suboptimally solved instances (giving a regret bound of 0.0006nV ) with 0.95 con<sup>fi</sup>dence using the Clopper– Pearson bound [1].

The results for the union data set are shown in Fig. 1, right. Observe that for all our results, with the possible exception of 2K-64, the bound on incentives to lie is quite low, far lower than $\frac { V ^ { * } } { 2 }$ suggested by the uniform (worst-case) analysis. Thus, if the number of players is not too large, there do not appear to be signi<sup>fi</sup>cant incentives for bidders to lie.<sup>9</sup>

## 7. Computing a better response

Our average-case analysis of incentives to deviate assumes that mechanism participants have unlimited computational power. However, if we <sup>fi</sup>nd the allocation problem fundamentally hard to solve for the designer, it is likely that it is no less dif<sup>fi</sup>cult for players to pro<sup>fi</sup>tably deviate. Indeed, Sanghvi and Parkes [20] show that computing a better response is NP-Hard for a combinatorial allocation problem under certain assumptions on $g .$ This worst-case result, <sup>g</sup>however, is unsatisfying in our setting, since as long as the players can often (that is, on many actual problem instances) compute a better response, they will try to do so. Insofar as we can bound their gains tightly, this would not be a concern. But for the case that our bounds leave enough room for gains, we wish to have a general purpose technique to make deviations relatively challenging to compute.

![](/api/attachments/43P4HWH9/fulltext/images/0b572eda3bcae3f8dfd7cea71614a2e1b16d45c593dbe4fda2d2984cef27fafb.jpg)

![](/api/attachments/43P4HWH9/fulltext/images/5372ecc222529d5644534fa3218ff04dfabf82317c39f4aeaa904e70479f076e.jpg)  
Fig. 1. Upper bound on regret, as a fraction of $n V ^ { * }$ , left: for several data set sizes, and right: for the union of all data.

In this section we suggest a very simple sampling technique which allows us to amplify complexity of the deviation problem on average, under some assumptions on the algorithmic capabilities of the mechanism participants.

Our <sup>fi</sup>rst result re<sup>fl</sup>ects an assumption that the designer can construct a belief (prior) distribution over the algorithms which would be used (independently) by each player. Our results below are then with respect to the randomized “pseudo-algorithm” induced by this distribution. In its simplest form, it may be that the problem is well-enough understood that state-of-the-art algorithms for computing improving deviations are readily available, so both the designer and the players would simply utilize the best of these. Under this assumption, consider the following sampling algorithm:

1. For each player i, draw L samples t′ from the belief distribution over the players' algorithms (we can think of these as sample deviations); let ${ { T } _ { i } ^ { \prime } } \mathrm { { = } } \{ { t _ { i } , t _ { i } ^ { \prime } } ^ { 1 } , . . . . , t _ { i } ^ { \prime } { } ^ { L } \}$ , where $t _ { i }$ is the actual reported type of $i ;$

2. De<sup>fi</sup>ne $\begin{array} { r } { g _ { i } ^ { \prime } ( t ) \in \arg \operatorname* { m a x } _ { o = g ( t _ { i } ^ { \prime } , ~ t - i ) | t _ { i } ^ { \prime } \in T _ { i } ^ { \prime } } \sum _ { j \in I } \nu _ { j } \big ( t _ { j } , g ( t _ { i } ^ { \prime } , t _ { - i } ) \big ) } \end{array}$ for each i; 3. De<sup>fi</sup>ne $\begin{array} { r } { g ^ { \prime } ( t ) { \in } \mathrm { a r g ~ m a x } _ { o = g _ { i } ^ { \prime } ( t ) \mid i \in I } \sum _ { j \in I } { \nu } _ { j } ( t _ { j } , g _ { i } ( t ) ) } \end{array}$

Observe that this enhanced algorithm can only improve social welfare.

Theorem 6. Given $g ^ { \prime } ( t )$ as the allocation mechanism, the probability (with respect to the belief distribution) that some player can compute an improving deviation is at most ${ \frac { n } { L + 1 } } . ^ { 1 { \dot { 0 } } }$

A direct consequence of Theorem 6 is that incentives of any player to lie can be made arbitrarily small as long as there is some non-zero cost to performing better-response computations.<sup>11</sup>

While the assumption that algorithmic capabilities of players are predictable is often reasonable, we may wish to make a stronger statement. For example, perhaps sampling deviations using some very simple heuristic (e.g., uniform random search), while entirely different from what players may in fact do, nevertheless makes pro<sup>fi</sup>table deviations increasingly dif<sup>fi</sup>cult for them to compute. As the following theorem suggests, the above result does, indeed, generalize (in a somewhat weaker form) to a very large class of sampling distributions and player deviation algorithms.

Formally, let $G ( u )$ be the distribution function of player utilities induced by the designer's search process (e.g., uniform sampling from the type space), whereas $H ( u )$ is the distribution function of player i's utilities induced by the player's search.

Theorem 7. Let $U _ { 1 } = \{ u | G ( u ) = 1 \}$ and suppose that $H ( U _ { 1 } ) = 0 .$ . Then $l i m _ { L  \infty } \int _ { \mathbb { R } } G ( u ) ^ { L } d H ( u ) = 0 .$

The interpretation is that as long as the players do not have a positive probability of reaching a utility that is better than any that the designer can possibly attain, the designer can use random sampling to effectively eliminate incentives to lie. In essence, in order to gain from lying the players need to know signi<sup>fi</sup>cantly more about the problem than the designer.

## 8. Simulation-based analysis of incentives to lie

The theoretical bounds above are in an important sense rather crude. Speci<sup>fi</sup>cally, recall that we arrived at Corollary 3 by bounding $E _ { t }$ [max  (t )] with $\textstyle \sum _ { i } E _ { t _ { i } } [ \epsilon _ { i } ( t _ { i } ) ]$ . That the sum can be a very loose upper bound is easy to see with a simple illustration. Consider a collection of i.i.d. random variables distributed uniformly on a unit interval. Clearly, the expectation of the maximum of these cannot exceed 1. On the other hand, if we have n such variables, the sum of expectations gives us an upper bound of n/2, or a factor of $O ( n )$ larger than the quantity it bounds! While the incentives to lie may often be small enough for the loose upper bound of Corollary 3 to nevertheless give meaningful results, a negative conclusion based on it need not imply that all hope is lost. Rather, we present in this section a simulation-based scheme that bounds more tightly, albeit approximately, the incentives of agents to lie for any given approximation algorithm combined with a VCG-based scheme. A further bene<sup>fi</sup>t of a fully simulation-based approach is that it allows us to combine very naturally the upper bound on regret with a prior distribution on the algorithms that agents may use to compute a utility-improving lie. We illustrate our simulation-based technique in the context of combinatorial auctions using a greedy approximation algorithm [13]. Since the greedy algorithm, while highly effective when valuation distribution is submodular, can be quite poor when complementarities are signi<sup>fi</sup>cant, we should not draw conclusions based on absolute regret values presented; rather, we offer some qualitative insights that are suggestive of a broader pattern.

![](/api/attachments/43P4HWH9/fulltext/images/1ab2818f29ef8fc2cb6551674776c18d7b83e325d17b1ee3d544482e14eaf3b0.jpg)

![](/api/attachments/43P4HWH9/fulltext/images/26bbf6f6e4b73e757a48380c8269dbd99366e797c6d6bd7dca0d4481e0207bf5.jpg)  
Fig. 2. Average game-theoretic regret when greedy algorithm is used to approximate WDP of a combinatorial auction with submodular valuations. Left: as a function of the number of players; the number of items is <sup>fi</sup>xed at 20. Right: as a function of the number of items; the number of players is <sup>fi</sup>xed at 5.

Consider the following algorithm for simulation-based regret approximation.

1. Generate M random type pro<sup>fi</sup>le t according to F;

2. For each sampled type pro<sup>fi</sup>le t, generate L random deviations t′ for each player i, drawn according to a randomized distribution ${ \sf G } ; ^ { 1 2 }$

3. Compute approximate regret for each player i,

$$
\hat {\epsilon} _ {i} (t _ {i}) = \max _ {l = 1, \dots , L} u _ {i} \left(t _ {i} ^ {\prime l}, g (t)\right) - u _ {i} (t _ {i}, g (t));
$$

4. Compute approximate regret $\hat { \epsilon } ( t ) = \mathrm { m a x } _ { i } \hat { \epsilon } _ { i } ;$

5. Compute average regret $\hat { \epsilon } = \textstyle \frac { 1 } { M } \hat { \epsilon } ( t ^ { m } )$

For the results reported below, we chose M to be 40–100 and let $\mathrm { L } = 1 0 0 . ^ { 1 }$ 3

The results that we report are actually (approximate) upper bounds on the incentives to deviate because (a) we consider maximum gain for every type pro<sup>fi</sup>le sampled, rather than for each player given the distribution of other player types, and (b) we report the fraction of utility relative to the greedy, rather than optimal, allocation (i.e., we report $\hat { \epsilon } / \operatorname* { m a x } _ { m = 1 , \dots , M } V _ { g } ( t ^ { m } ) )$

<sup>gð Þ</sup>Our <sup>fi</sup>rst set of simulations considers two kinds of valuations: randomly generated submodular valuations and valuations in which marginal values of items are generated uniformly randomly on the unit interval. We present these results in Fig. 2, where we separately vary the number of players and items in the auction. As we can observe, in spite of the rather weak worst-case guarantees on the performance of the greedy algorithm in the case of submodular valuations, the average regret tends to be low. Additionally, regret tends to decrease with increasing complexity of the allocation problem. In order to assess the robustness of the latter phenomenon to different distributions of valuations, we use the CATS tool [14].

The results for several CATS distributions are shown in Fig. 3.<sup>14</sup> While incentives to lie can be relatively large, in all but one case the incentives to deviate from truthful reporting decrease with increasing problem complexity, suggesting that this observation is rather robust.

## 9. Conclusion

We presented a series of results that allow construction of average-case bounds on agent incentives to lie about their preferences for VCG-based mechanisms. Conceptually, this deviates from the more traditional worst-case analysis which often fails to provide meaningful bounds. Practically, we introduce a simple method for assessing incentive properties of speci<sup>fi</sup>c approximation algorithms, and even heuristics that lack formal approximation guarantees, in the context of economic resource allocation problems. We illustrate the resulting empirical incentive analysis for a speci<sup>fi</sup>c approximation algorithm in the context of several combinatorial auction problems. Our results here suggest that using state-of-the-art algorithms for solving combinatorial allocation problems essentially eliminates agent incentives to misreport their preferences. In addition, we show that even if incentives to lie about true player types are signi<sup>fi</sup>cant, the designer can use sampling to make it unlikely that any player will compute a utility-improving lie. This provides a typical-case complement to an already known worst-case hardness result. Our <sup>fi</sup>nal contribution is a fully simulation-based method for approximating tighter bounds on incentives of agents to misreport their preferences. As an illustration of the power of this method, we demonstrate that incentives to lie decrease with increasing problem size when the designer uses a greedy approximation algorithm.

## Appendix A. Welfare properties of VCG-based mechanisms

It is generally assumed that incentives to lie are undesirable, in part because they result in greater uncertainty about outcomes. However, such incentives would pose a substantially lesser problem if they are aligned with social utility. Note that under VCG-based payments any unilateral deviation that improves player i's utility is also welfare improving. Speci<sup>fi</sup>cally, observe that

$$
\begin{array}{r l} & u _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i}), p _ {i} (t _ {i} ^ {\prime}, t _ {- i})) = \sum_ {j} v _ {j} \Big (t _ {j}, g (t _ {i, t - i} ^ {\prime}) \Big) > u _ {i} (t _ {i}, g (t), p _ {i} (t _ {i}, t _ {- i})) \\ & \qquad = \sum_ {j} v _ {j} \Big (t _ {j}, g (t) \Big). \end{array}
$$

However, group deviations may in general lead to welfare loss. A key question, then, is whether there necessarily exists a welfare improving Bayes-Nash equilibrium strategy pro<sup>fi</sup>le. We now show that the answer is, in general, negative.

Example 1. Consider the following combinatorial auction setting. We have two players (1 and 2) and two items (1 and 2). As is standard, assume that $\mathtt { v } _ { 1 } ( \varnothing ) = \mathtt { v } _ { 2 } ( \varnothing ) = 0$ and consider the following value functions:

![](/api/attachments/43P4HWH9/fulltext/images/bd366b09023492dcf8ceac7bcfb68d7bf1d518d7a414cac93a41750a9b712b45.jpg)

![](/api/attachments/43P4HWH9/fulltext/images/024da32ea3dbe41cc2d718d1f85b5668a2dd062a6fc9454ffe9ba7be18950a37.jpg)  
Fig. 3. Average game-theoretic regret in combinatorial auctions with submodular and random valuations. Left: as a function of the number of players; the number of bids is 20. Right: as a function of the number of submitted bids; the number of players is 15.

$$
v _ {1} (\{1, 2 \}) = 1 0, v _ {1} (\{1 \}) = v _ {1} (\{2 \}) = 4
$$

$$
v _ {2} (\{1, 2 \}) = 5, v _ {2} (\{1 \}) = v _ {2} (\{2 \}) = 2.
$$

De<sup>fi</sup>ne $\mathbf { V } _ { 1 } ^ { \prime }$ and $\mathbf { V } _ { 2 } ^ { \prime }$ to be:

$$
v _ {1} ^ {\prime} (\{1, 2 \}) = 2, v _ {1} ^ {\prime} (\{1 \}) = v _ {1} ^ {\prime} (\{2 \}) = 0
$$

$$
v _ {2} ^ {\prime} (\{1, 2 \}) = 2, v _ {2} ^ {\prime} (\{1 \}) = v _ {2} ^ {\prime} (\{2 \}) = 0
$$

and suppose that the algorithm g allocates the items as follows:

$g ( v _ { 1 } , v _ { 2 } )$ assigns good 1 to player 1 and good 2 to player 2 (for a total <sup>g</sup>welfare of 6)

$g ( v _ { 1 } ^ { \prime } , v _ { 2 } )$ assigns both goods to player 1 (to yield the optimal welfare <sup>g</sup>of ${ \bf \dot { \rho } } _ { 1 0 } )$

$g ( v _ { 1 } ^ { \prime } , v _ { 2 } ^ { \prime } )$ assigns both goods to player 2 (to yield a total welfare of 5)

$g ( v _ { 1 } ^ { \prime \prime } , v _ { 2 } ^ { \prime } )$ assigns both goods to player 2 for any v″

$g ( v _ { 1 } ^ { \prime } , v _ { 2 } ^ { \prime \prime } )$ assigns both goods to player 1 for all $\nu _ { 2 } ^ { \prime \prime }$ except $\nu _ { 2 } ^ { \prime \prime } = \nu _ { 2 } ^ { \prime } .$

$g ( v _ { 1 } ^ { \prime \prime } , v _ { 2 } ^ { \prime \prime } )$ assigns both goods to player 2 for all v″ and $\nu _ { 2 } ^ { \prime \prime }$ , with the exception of the cases outlined above.

Now, for the computation of player utilities below, ignore the $\mathrm { h } _ { \mathrm { i } }$ payment term as it does not affect the players' incentives. Observe that in this example, $\left( \mathsf { v } _ { 1 } , \mathsf { v } _ { 2 } \right)$ is not an equilibrium, since the utility to each players is 6, whereas player 1 could obtain 10 by deviating to v′ , which would yield the utility of 2 for the second player. Furthermore, $( \mathsf { v } _ { 1 } ^ { \prime } , \mathsf { v } _ { 2 } )$ is not an equilibrium either, since player 2 could now gain by deviating to $\mathbf { V } _ { 2 } ^ { \prime } ,$ , obtaining the utility of $5 ,$ which would give player 1 the utility of 2. The pro<sup>fi</sup>le $\left( \mathbf { V } _ { 1 } ^ { \prime } , \mathbf { V } _ { 2 } ^ { \prime } \right)$ is, however, an equilibrium, and yields lower welfare than the truthful pro<sup>fi</sup>le. Additionally, any pure or mixed strategy pro<sup>fi</sup>le with support on v″ and $\mathrm { v } _ { 2 } ^ { \prime \prime }$ that are not the special cases described above will yield the same welfare as $\left( \mathsf { v } _ { 1 } ^ { \prime } , \mathsf { v } _ { 2 } ^ { \prime } \right)$

To see that no mixed strategy equilibrium with any support will do the job, note that we can only increase welfare by having player 2 play $\boldsymbol { \nabla } 2$ as a part of the support. Without loss of generality, let's look at the restricted game with player 1 choosing between actions $\mathsf { v } _ { 1 }$ and $\mathbf { V } _ { 1 } ^ { \prime }$ and player 2 choosing between $\mathrm { v } _ { 2 }$ and $\mathbf { V } _ { 2 } ^ { \prime }$ . Suppose that player 2 plays v2 with probability and $\mathbf { V } _ { 2 } ^ { \prime }$ with probability $_ { 1 - \alpha }$ . Then the utility of player 1 from playing $\mathsf { v } _ { 1 }$ is 4α+2, while his utility from playing $\mathbf { V } _ { 1 } ^ { \prime }$ is 8α+2, and the two are only equal when $\alpha = 0 ,$ , that is, when player 2 always selects $\mathbf { V } _ { 2 } ^ { \prime }$ . In this case, all pro<sup>fi</sup>les yield welfare of 5.

We now formally state the negative result demonstrated by the above example.

Proposition 8. Let P be a combinatorial allocation problem. Then there exists an allocation algorithm g and player valuation functions $\nu _ { i }$ with $\nu _ { i }$ $( \infty ) { = } 0 f o r$ all players i such that every Bayes-Nash equilibrium yields strictly lower welfare than the strategy profile in which all players report their valuations truthfully.

For the purposes of the above example, we had to construct a rather bizarre outcome function g(t). An open question is whether some typical approximation algorithms have properties which do ensure that at least one equilibrium (or, ideally, all equilibria) is (are) welfare improving as compared to truthful reporting.

## Appendix B. Proofs

## B.1. Proof of Theorem 2

Let $t _ { i } ^ { * } { = } \arg \operatorname* { m a x } _ { t _ { i } } u _ { i } ( t _ { i } , t _ { - i } )$ . The most that the player can gain from deviating to $t _ { i } ^ { * }$ is

$$
E _ {t - i} \Big [ \sum_ {j} v _ {j} \Big (t _ {j}, g (t _ {i} ^ {*}, t _ {- i}) \Big) - \sum_ {j} v _ {j} \Big (t _ {j}, g (t) \Big) | t _ {i} \Big ]
$$

$$
\leq E _ {t - i} \left[ \sum_ {j} v _ {j} \left(t _ {j}, o ^ {*} \left(t _ {i} ^ {*}, t _ {- i}\right)\right) - \sum_ {j} v _ {j} \left(t _ {j}, g (t)\right) \mid t _ {i} \right]
$$

$$
\leq E _ {t - i} \left[ \sum_ {j} v _ {j} \left(t _ {j}, o ^ {*} (t _ {i} ^ {*}, t _ {- i})\right) - \frac {1}{\alpha (t)} \sum_ {j} v _ {j} \left(t _ {j}, o ^ {*} (t)\right) | t _ {i} \right]
$$

$$
\leq E _ {t - i} \left[ \sum_ {j} v _ {j} (t _ {j}, o ^ {*} (t)) - \frac {1}{\alpha (t)} \sum_ {j} v _ {j} (t _ {j}, o ^ {*} (t)) | t _ {i} \right]
$$

$$
\leq E _ {t - i} \left[ \frac {\alpha (t) - 1}{\alpha (t)} V ^ {*} (t) \mid t _ {i} \right].
$$

## B.2. Proof of Theorem 6

To prove this theorem, we <sup>fi</sup>rst need the following lemma.

Lemma 9. Let $t _ { i }$ be the type of player i and $t _ { i } ^ { \prime } \neq t _ { i }$ be his deviation, and suppose that t ′ is sampled from T uniformly randomly. Then for any $q \geq 0$

$$
\operatorname * {P r} \left\{\sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t _ {i} ^ {\prime}, t _ {- i})) \geq q \right\} = \operatorname * {P r} \left\{\sum_ {i} v _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i})) \geq q \right\}.
$$

Proof. Observe, <sup>fi</sup>rst, that for any q, z and any $t _ { i } ^ { \prime } \neq t _ { i } ,$

$$
\begin{array}{c} \operatorname * {P r} \bigl \{v _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i})) \geq q | v _ {i} (t _ {i} ^ {\prime}, g (t _ {i, t - i} ^ {\prime})) \geq z \bigr \} \\ = \operatorname * {P r} \bigl \{v _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i})) \geq q \bigr \}, \end{array}
$$

since the value function itself is <sup>fi</sup>xed. Consequently, letting

$$
V _ {- i} (t _ {i} ^ {\prime}) = \sum_ {j \neq i} v _ {j} (t _ {j}, g (t _ {i} ^ {\prime}, t _ {- i}),
$$

we get

$$
\begin{array}{l} \operatorname * {P r} \Big \{v _ {i} (t _ {i}, g (t _ {i, t - i} ^ {\prime})) + V _ {- i} (t _ {i} ^ {\prime}) \geq q   | v _ {i} (t _ {i} ^ {\prime}, g (t _ {i} ^ {\prime}, t _ {- 1})) + V _ {- i} (t _ {i} ^ {\prime}) \geq z) \\ = E _ {V - i \big (t _ {i} ^ {\prime} \big) = w} \Big [ \operatorname * {P r} \Big \{v _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i})) \geq q - w   | v _ {i} (t _ {i} ^ {\prime}, g (t _ {i} ^ {\prime}, t _ {- i})) \geq z - w \Big \} \Big ] \\ = E _ {V - i \big (t _ {i} ^ {\prime} \big) = w} \big [ P r \big \{v _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i})) \geq q - w \big \} \big ] \\ = P r \big \{v _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i})) + V _ {- i} (t _ {i} ^ {\prime}) \geq q \big \}. \end{array}
$$

Now, observe that, given the de<sup>fi</sup>nition of $g ^ { \prime } ( \ u )$

$$
\begin{array}{l} \operatorname * {P r} \bigg \{\sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t _ {i, - i} ^ {\prime})) \geq q \bigg \} \\ = \operatorname * {P r} \bigg \{\sum_ {i} v _ {i} (t _ {i}, g (t _ {i} ^ {*}, t _ {- i})) \geq q   |   v _ {i} (t _ {i} ^ {\prime}, g (t _ {i} ^ {*}, t _ {- i})) + V _ {- i} (t _ {i} ^ {*}) \geq z, \end{array}
$$

and, consequently,

$$
\operatorname * {P r} \left\{\sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t _ {i} ^ {\prime}, t _ {- i})) \geq q \right\} = \operatorname * {P r} \left\{\sum_ {i} v _ {i} (t _ {i}, g (t _ {i} ^ {*}, t _ {- i})) \geq q \right\}.
$$

But, since both t′<sub>i</sub> and t<sub>i</sub>\* are drawn uniformly randomly,

$$
\operatorname * {P r} \Bigl \{\sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t _ {i} ^ {\prime}, t _ {- i})) \geq q \Bigr \} = \operatorname * {P r} \Bigl \{\sum_ {i} v _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i})) \geq q \Bigr \}.
$$

We are now ready to prove the theorem. First, consider a select player i.

$$
\begin{array}{l} \operatorname * {P r} \bigl \{u _ {i} (t _ {i}, g ^ {\prime} (t _ {i} ^ {\prime}, t _ {- i}), p _ {i} (t _ {i} ^ {\prime}, t _ {- i})) > u _ {i} (t _ {i} g ^ {\prime} (t), p (t)) \bigr \} \\ \leq \operatorname * {P r} \bigl \{u _ {i} (t _ {i} g ^ {\prime} (t _ {i} ^ {\prime}, t _ {- i}), p _ {i} (t _ {i} ^ {\prime}, t _ {- i})) \geq u _ {i} (t _ {i}, g ^ {\prime} (t), p (t)) \bigr \} \\ = \operatorname * {P r} \biggl \{\sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t _ {i} ^ {\prime}, t _ {- i})) \geq \sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t)) \biggr \}. \end{array}
$$

First, consider the quantity $\begin{array} { r } { \operatorname* { P r } \{ \sum _ { i } \nu _ { i } ( t _ { i } , \ g ^ { \prime } ( t _ { i } ^ { \prime } , \ t _ { - i } ) ) \ge q \} } \end{array}$ for some <sup>fi</sup>xed q. By Lemma 9,

$$
\operatorname * {P r} \biggl \{\sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t _ {i} ^ {\prime}, t _ {- i})) \geq q \biggr \} = \operatorname * {P r} \biggl \{\sum_ {i} v _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i})) \geq q \biggr \}.
$$

Hence,

$$
\begin{array}{l} \operatorname * {P r} \bigg \{\sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t _ {i} ^ {\prime}, t _ {- i})) \geq \sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t)) \bigg \} \\ = \operatorname * {P r} \bigg \{\sum_ {i} v _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i})) \geq \sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t)) \bigg \}. \end{array}
$$

Let $\begin{array} { r } { V ^ { \prime } ( t ) = \sum _ { i } \nu _ { i } ( t _ { i } , g ( t _ { i } ^ { \prime } , t _ { - i } ) ) } \end{array}$ ). By conditioning, we have

$$
\begin{array}{l} \operatorname * {P r} \Bigl \{\sum_ {i} v _ {i} (t _ {i}, g (t _ {i} ^ {\prime}, t _ {- i})) \geq \sum_ {i} v _ {i} (t _ {i}, g ^ {\prime} (t)) \Bigr \} \\ = E _ {V ^ {\prime} (t)} \left[ \operatorname * {P r} \Bigl \{\sum_ {i} v _ {i} (t _ {i} g ^ {\prime} (t)) \leq z | V ^ {\prime} (t) = z \Bigr \} \right] \\ \leq E _ {V ^ {\prime} (t)} \left[ \operatorname * {P r} \Bigl \{\max _ {t _ {i} ^ {\prime} \in T _ {i} \backslash t _ {i}} \sum_ {i} v _ {i} (t _ {i}, g (t _ {i} ^ {\prime \prime}, t _ {- i})) \leq z | V ^ {\prime} (t) = z \Bigr \} \right] \\ = E _ {V ^ {\prime} (t)} \left[ \operatorname * {P r} \Bigl \{\sum_ {i} v _ {i} (t _ {i}, g (t _ {i} ^ {\prime \prime}, t _ {- i})) \leq z | V ^ {\prime} (t) = z \Bigr \} ^ {L} \right]. \end{array}
$$

Letting $F ( z )$ be the distribution over t′ (it is identical for $t _ { i } ^ { \prime \prime }$ by construction), we have

$$
\begin{array}{l} E _ {V ^ {\prime} (t)} \left[ \operatorname * {P r} \left\{\sum_ {i} v _ {i} (t _ {i}, g (t _ {i} ^ {\prime \prime}, t _ {- i})) \leq z | V ^ {\prime} (t) = z \right\} ^ {L} \right] \\ = \int_ {\mathbb {R}} F (z) ^ {L} d F (z) = \frac {1}{L + 1}. \end{array}
$$

To conclude the proof, we only need to apply the union bound to obtain $\frac { n } { L + 1 }$ as the upper bound over all the players.

## B.3. Proof of Theorem 7

First, observe that by the Dominated Convergence Theorem,

$$
\lim _ {L \to \infty} \int_ {\mathbb {R}} G (u) ^ {L} d H (u) = \int_ {\mathbb {R}} \lim _ {L \to \infty} G (u) ^ {L} d H (u),
$$

since both G(u) and H(u) are probability densities. Now,

$$
\begin{array}{c} \int_ {\mathbb {R}} \lim _ {L \to \infty} G (u) ^ {L} d H (u) = \int_ {\overline {{U _ {1}}}} \lim _ {L \to \infty} G (u) ^ {L} d H (u) + \int_ {U _ {1}} \lim _ {L \to \infty} G (u) ^ {L} d H (u) \\ = \int_ {\overline {{U _ {1}}}} \lim _ {L \to \infty} G (u) ^ {L} d H (u). \end{array}
$$

Since for every u∈ $\overline { { \overline { { U } } _ { 1 } } }$ ; lim $_ { \infty } G ( u ) ^ { L } = 0$

$$
\int_ {\mathbb {R}} \lim _ {L \to \infty} G (u) ^ {L} d H (u) = \int_ {\overline {{U _ {1}}}} \lim _ {L \to \infty} G (u) ^ {L} d H (u) = 0.
$$

## References

[1] C. Clopper, E. Pearson, The use of con<sup>fi</sup>dence or <sup>fi</sup>ducial limits illustrated in the case of the binomial, Biometrika 26 (1934) 404–413.

[2] P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, 2006.

[3] R.W. Day, P. Cramton, The quadratic core-selecting payment rule for combinatorial auctions, Working paper, 2010.

[4] R.W. Day, S. Raghavan, Fair payments for ef<sup>fi</sup>cient allocations in public sector combinatorial auctions, Management Science 53 (2007) 1389–1406.

[5] S. Dobzinski, N. Nisan, M. Shapira, Truthful randomized mechanisms for combinatorial auctions, in: 38th ACM Symposium on Theory of Computing, 2006, pp. 644–652

[6] Y. Fujishjima, K. Leyton-Brown, Y. Shoham, Taming the computational complexity of combinatorial auctions: Optimal and approximate approaches, in: International Joint Conference on Artificial Intelligence. 1999 pp. 548–553

[7] R. Gonen, D. Lehmann, Linear programming helps solving large multi-unit combinatorial auctions, in: Electronic Market Design Workshop, 2001.

[8] A. Kothari, D.C. Parkes, S. Suri, Approximately-strategyproof and tractable multiunit auctions, Decision Support Systems 39 (2005) 105–121

[9] V. Krishna, Auction Theory, Academic Press, 2002.

[10] R. Lavi, C. Swamy, Truthful and near-optimal mechanism design via linear programming, in: 46th IEEE Symp. on Foundations of Comp. Sc., 2005, pp. 595–604.

[11] D. Lehmann, R. Müller, T. Sandholm, The winner determination problem, in: [2], 2006, pp. 297–318.

[12] D. Lehmann, L.I. O'Callaghan, Y. Shoham, Truth revelation in approximately efficient combinatorial auctions, Journal of the ACM 49 (2002) 1-26.

[13] B. Lehmann, D. Lehmann, N. Nisan, Combinatorial auctions with decreasing marginal utilities Games and Economic Behavior 55 (2006) 270–296.

[14] K. Leyton-Brown, Y. Shoham, A test suite for combinatorial auction, in: [2], 2006, pp. 451–478.

[15] A. Mas-Colell, M.D. Whinston, J.R. Green, Microeconomic Theory, Oxford Univ. Press, 1995.

[16] A. Mu'alem, N. Nisan, Truthful approximation mechanisms for restricted combinatorial auctions, in: AAAI, 2002, pp. 379–384.

[17] N. Nisan, A. Ronen, Computationally feasible VCG mechanisms, Journal of Arti<sup>fi</sup>cial Intelligence Research 29 (2007) 19–47.

[18] T. Sandholm, Algorithm for optimal winner determination in combinatorial auctions, Arti<sup>fi</sup>cial Intelligence 135 (2002) 1–54.

[19] T. Sandholm, S. Suri, A. Gilpin, D. Levine, CABOB: a fast optimal algorithm for winner determination in combinatorial auctions, Management Science 51 (2005) 374–390.

[20] S. Sanghvi, D.C. Parkes, Hard-to-manipulate combinatorial auctions, Technical Report, Harvard University, 2004

[21] Y. Vorobeychik, Y. Engel, Average-case analysis of incentives under approximate allocation algorithms, in: Sixth International Workshop on Internet and Network, Economics, 2010, pp. 251–258.

[22] Y. Vorobeychik, Y.Engel, Incentive analysis of approximately ef<sup>fi</sup>cient allocation algorithmsin: Ninth International Conference on Autonomous Agents and Multiagent Systems, 2010, pp. 1479–1480.

[23] R. Wilson, Game-theoretic analyses of trading processes, in: T. Bewley (Ed.), Advances in Economic Theory: Fifth World Congress, Cambridge University Press, Cambridge, U.K., 1987, pp. 33–70.

Yevgeniy Vorobeychik is a Senior Member of Technical Staff at Sandia National Laboratories. Between 2008 and 2010 he was a post-doctoral research associate at the University of Pennsylvania Computer and Information Science department. He received Ph.D. (2008) and M.S.E. (2004) degrees in Computer Science and Engineering from the University of Michigan, and a B.S. degree in Computer Engineering from Northwestern University. His work focuses on simulation-based game theory and mechanism design, algorithmic game theory, network economics, and machine learning. Dr. Vorobeychik was nominated for the 2008 ACM Doctoral Dissertation Award and received honorable mention for the 2008 IFAAMAS Distinguished Dissertation Award. He was also a recipient of a STIET doctoral fellowship at the University of Michigan, as well as a distinguished Computer Engineering undergraduate award at Northwestern University.

Yagil Engel joined the IBM research lab in Haifa in July 2010, after two years as a postdoc at the Technion, Faculty of Industrial Engineering and Management, where his research focused on game-theoretic aspects of AI planning, and where he also teaches a class on Electronic Commerce Algorithms. He completed his PhD at the University of Michigan in 2008, in the area of Arti<sup>fi</sup>cial Intelligence at the Computer Science division. His thesis focuses on multi-attribute utility theory and decision making in the context of business-to-business electronic commerce, and his publication record includes in addition works on procurement auctions and graphical models for decision making under uncertainty. Prior to graduate studies Yagil worked in the software industry on commercial state-of-the-art Business to Business auction systems.
