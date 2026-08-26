---
otero_id: 26771
otero_key: "QWMFA8P7"
title: "Information Acquisition Policies for Resource Allocation Among Multiple Agents"
authors: "J. C. Moore; H. R. Rao; A. Whinston; K. Nam; T. S. Raghu"
year: "1997"
journal: "Information Systems Research"
doi: "10.1287/isre.8.2.151"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR Information Systems Research

![](/api/attachments/QWMFA8P7/fulltext/images/1686f3b9f0b9d1fcfd49634b6f4e92100fc6514a9f75561e490df9bef4450618.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Information Acquisition Policies for Resource Allocation Among Multiple Agents

J. C. Moore, H. R. Rao, A. Whinston, K. Nam, T. S. Raghu,

To cite this article:

J. C. Moore, H. R. Rao, A. Whinston, K. Nam, T. S. Raghu, (1997) Information Acquisition Policies for Resource Allocation Among Multiple Agents. Information Systems Research 8(2):151-170. http://dx.doi.org/10.1287/isre.8.2.151

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1997 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/QWMFA8P7/fulltext/images/65c97e7c8033daf7641da5aea9685801deb5dbd0d4a841cce429a3a892462650.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Information Acquisition Policies for Resource Allocation Among Multiple Agents

J. C. Moore • H. R. Rao • A. Whinston • K. Nam • T. S. Raghu

Krannert Graduate School of Management, Purdue University, W. Lafayette, Indiana 47907
duke@mgmt.purdue.edu

School of Management, State University of New York at Buffalo, Buffalo, New York 14260 mgmtrao@acsu.buffalo.edu

MSIS, College of Business Administration, University of Texas at Austin, Austin, Texas 78712 abw@uts.cc.utexas.edu

School of Management, State University of New York at Buffalo, Buffalo, New York 14260 knam@cakra.dongguk.ac.kr

School of Management, State University of New York at Buffalo, Buffalo, New York 14260
raghu@acsu.buffalo.edu

This paper investigates a problem of resource allocation, where a manager allocates discrete resources among multiple agents in a team in a socially optimal manner. In making this allocation, the manager needs to understand the preference orders of the agents for the discrete resources. The manager does this by adopting an information acquisition policy. Three different information acquisition policies are investigated here. The trade off between the amount of information elicited and the costs involved are studied for each of the policies.
(Information Acquisition Policies; Discrete Resource Allocation; Team Problem Solving)

## 1. Introduction

Managers often encounter a ubiquitous problem: how to decide on the allocation of scarce resources (e.g., a limited amount of mainframe computer time) to their subordinates based on the subordinates' individual capabilities or objectives. Since managers typically do not have complete information about their subordinates preferences and capabilities, they have to acquire such knowledge by interacting with them. In the process of interaction and knowledge elicitation, managers encounter costs, in terms of space and time constraints. As they acquire more information about their subordinates' preferences and capabilities, they can utilize this information to arrive at an allocation of the resources among the various agents in such a way that the organizational or team objectives are fulfilled. Clearly, managerial decision making needs to be closely linked with information systems for good decisions to be generated.

While this problem of allocating scarce resources to a team of individual agents in such a way as to optimize a performance measure has long been studied in management, the traditional approaches taken in addressing such a problem have involved developing optimization models, which are then often solved through standard linear programming techniques (Mathur and Solow 1994). However these approaches have typically ignored the issue of incomplete information or have not allowed for the opportunity to acquire additional information from additional information sources (Preckel et al. 1993). In fact, the idea of studying such problems in terms of the design and functioning of abstract resource allocation mechanisms and of viewing informational exchange as a critical factor in such design is relatively new (Hurwicz 1986, Hurwicz and Marschak 1985, Marschak 1986, Moore et al. 1994). Recent studies by the present authors (Moore et al. 1994, 1996) have provided an information-theoretic basis for the optimal assignment of discrete resources to two or more agents.

This paper examines problem solving in a multiple-agent environment of incomplete information, as applied to the discrete resource allocation problem (RAP) (Marschak and Radner 1972, Moore and Whinston 1986, Balakrishnan and Whinston 1991, De et al. 1993, Mookerjee and DosSantos 1993). It allows alternative IS structures to be investigated since it can concretely identify the nature of information flows and various communication patterns (Barros 1988).

This paper examines the problem solving process for the resource allocation problem (RAP) from the perspective of a manager who is a benevolent dictator, in the sense that the manager is interested in maximizing an objective function which is determined by a well-defined function of the individual agents' preferences. The manager, who typically has only partial information, carries out actions to acquire additional information about the preference profile of each agent in the context of various resource allocation choices, prior to making the allocation. After obtaining this additional information, the manager allocates resources among the members of the team in a socially optimal manner. The manager's overall problem is, then, one of balancing the contribution of additional information in increasing the team social welfare (payoff) of the allocation against the cost of the experimentation necessary to obtain the additional information.

The social welfare function is chosen to be an additive utilitarian social welfare function of the Bergson-Samuelson type (Samuelson $^{1}$ 1983). There are several advantages to this choice: first it allows the characterization of team performance in terms of a single dimension; second it allows the interaction of the agents in the team through sharing of the common resource; third it offers opportunities for decentralization as well as division of labor, since it is a separable function.

The objective of this research is to incorporate the information system within the decision-making environment. The contributions of this paper are twofold:

\- From a decision making perspective, it demonstrates how a manager can make an optimal decision with respect to allocating resources amongst subordinates, even with incomplete information.

\- From an information system perspective, it examines different information acquisition strategies in terms of the cost structures, not only for information gathering, but also for information processing. The incorporation of computational costs, communication and switching costs in the analysis allows consideration of the process of acquiring information, deliberating and then acting for the effective management of resources.

## 2. The Resource Allocation Problem

## 2.1. A Formal Model

The starting point of this study is a “decision model with sequential information acquisition” (Moore and Whinston 1986). The model is utilized to examine the problem-solving process for the resource allocation problem (RAP) from the perspective of a manager who is, in effect, a benevolent dictator. The decision problem is defined in terms of a set of mutually exclusive (discrete) states (the state space X), a set of available decisions (the decision space D), a payoff function ( $\omega^{*}$ ), and a set of information gathering actions (A). The manager carries out actions ( $a \in A$ ) to acquire information about each agent’s preference profile over resource bundles prior to making the allocation. This information-gathering action results in a partition of the state space and, when implemented, results in a determination of which element of the partition contains the actual state ( $x \in X$ ). Performing a sequence of such actions (defined as a strategy) thus results in a sequence of the state space, X, each of which is a refinement of the previous partitions in the sequence; and thus, when implemented, such a strategy determines a decreasing sequence of sets containing the actual state. The information-acquisition process allows the manager to eliminate a set of inferior allocations from the set of admissible allocations (note: not all allocations may be admissible, for example, the manager would not allocate the least preferred choices to all the agents), and thereby also eliminate a set of admissible experiments that are associated with inferior allocations (note that the experiments that are admissible are for those bundles for which the manager has no a priori information). The final partition (which is not necessarily the finest partition) leads to a final decision $(d \in D)$ (about the resources to be allocated to the agents).

The goal of the decision problem is, therefore, to use an efficient information acquisition strategy to gain enough information about subordinates' preferences and capabilities as to enable the manager to choose a particular allocation from the set of feasible allocations in such a way as to maximize the expected net payoff (the welfare less the aggregate costs of all actions $[c(a)]$ leading to the final partition).

## 2.2. Preference Profiles

In the following discussion, we will let $z$ denote a commodity bundle, while $\overline{z}$ denotes the resource constraint, and $Z$ the commodity space of all bundles under consideration. The set $Z$ is assumed to be of the form $\{0, 1, 2, \ldots, m\} \times \{0, 1, 2, \ldots, n\}$ . (The simulations carried out later are specific to the case where $n = 1$ .) We shall denote the $i$ th agent's preferences by $\geq_i$ , strict preference by $>_i$ , and indifference by $\sim_i$ .

We denote the collection of all strictly increasing preference profiles over allocations by W, that is, W consists of all (complete, reflexive, and transitive) preference profiles over $Z, \geq$ , which satisfy (for the case under study):

$$
\text { if } (a, b) \geq (c, d) \text { and } (a, b) \neq (c, d), \text { then } (a, b) > (c, d).
$$

We suppose that each agent's preference profile (or preference relation), $\geq_{i}$ , is an element of $W$ ; but that this is the only a priori information which the manager has about the agent's preferences. In order to learn more about the agent's preference relations, the manager must undertake information-acquisition actions. In this context, we can define $\mathcal{Q}(z)$ to be the initial noncomparable set for $z \in Z$ . The noncomparable set, for any specified bundle $z$ , is the set of commodity bundles about which no prior preference information (in relation to $z$ ) is known to the manager, i.e.,

$$
\mathcal {Q} (z) = \{z ^ {\prime} \in Z | z ^ {\prime} \neq z \text {   and   } z \neq z ^ {\prime} \}.\tag{1}
$$

In obtaining more information about the agents' preferences, the manager reduces the size of the noncomparable set, for each agent and each bundle, z.

## 2.3. Ranking of Resource Bundles.

We now restate the above problem of determining preference relations in the following manner: given the set of resource bundles, Z, we determine the ranking of each element $z \in Z$ for agent i as the number of elements in the set Z which the manager knows agent i considers to be no better than (not preferred to) z. Note that even at the outset the element z itself is counted while determining the ranking. Therefore, the resource bundle $(0, 0)$ always has a ranking of 1, since it is considered equally preferred to itself, and there are no resource bundles in the set Z, over which $(0, 0)$ is preferred. This method of ranking the elements in Z is always consistent with the agent's true underlying preferences. The transitivity of each agent's preferences implies that the rank of a resource bundle $(a, b)$ is greater than or equal to the rank of a bundle $(c, d)$ if $(a, b)$ is weakly preferred to $(c, d)$ .

If the manager acquires complete information about agent i's preferences, then the ranking method just described will yield a well-defined function which represents agent i's true preferences (that is, the method will generate a utility function for agent i). Consequently, we can think of the manager's objective as being that of finding sufficient information about each agent's true utility function as to result in the maximization of some function of the agents' utility functions. Moreover, we can view the state space for each agent as consisting of the collection of all strictly increasing integer-valued functions defined on the commodity space and satisfying, for each $z \in Z$ : $1 \leq f(z) \leq \#Z$ , where $\#Z$ denotes the number of elements of Z.

We now use an example to illustrate the above discussion on the RAP. Let there be two goods with a resource constraint of $\bar{z} = (2, 1)$ , so that there are two units of one good and one unit of a second good (see Figure 1).

The state space W can then be thought of as being given by the following set of $f^{h}s$ , $\{f^{1},\ldots,f^{11}\}$ :

<table><tr><td>z/f</td><td> $f^{1}$ </td><td> $f^{2}$ </td><td> $f^{3}$ </td><td> $f^{4}$ </td><td> $f^{5}$ </td><td> $f^{6}$ </td><td> $f^{7}$ </td><td> $f^{8}$ </td><td> $f^{9}$ </td><td> $f^{10}$ </td><td> $f^{11}$ </td></tr><tr><td>(0,0)</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>(0,1)</td><td>2</td><td>3</td><td>3</td><td>4</td><td>4</td><td>2</td><td>3</td><td>3</td><td>2</td><td>3</td><td>3</td></tr><tr><td>(1,0)</td><td>3</td><td>2</td><td>3</td><td>2</td><td>2</td><td>3</td><td>2</td><td>3</td><td>3</td><td>2</td><td>3</td></tr><tr><td>(1,1)</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>(2,0)</td><td>5</td><td>5</td><td>5</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td></tr><tr><td>(2,1)</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td></tr></table>

(A general method for enumerating this complete family of functions involves mapping the resource space to lattice space and enumerating the number of

Figure 1 Commodity Space

![](/api/attachments/QWMFA8P7/fulltext/images/291cae4a3ab42bafeba9fa2d059b2d0ea12e91a59d6da630f176254ce047de63.jpg)

subdiagonal paths from the origin to a coordinate point in lattice space (Kaparthi and Rao 1991). Details of the combinatorics are available in Rao (1987).)

## 2.4. Assigning Utility Values to the Resource Bundles

The initial information the manager has about the agents' preferences (namely, that $\geq_{i} \in W$ ) can be used to calculate initial lower $[\mathbf{u}(z)]$ and upper $[\overline{u}(z)]$ for agent $i$ 's utility function, $u_{i}$ , at each bundle, $z$ . For example, the lower and upper bounds on the utility value of resource bundle $(0, 0)$ are 1 and 1 respectively. Similarly the lower and upper bounds on the utility value of the resource bundle $(2, 1)$ in the previous example are 6 and 6 respectively. The lower and upper bounds for other resource bundles in the example could similarly be determined. Also note that the difference between the upper and lower bounds is always greater than or equal to 0. The following diagram gives the lower and upper bounds on the utility value of resource bundles for the $(2 \times 1)$ resource allocation problem discussed before:

<table><tr><td>z</td><td>(0,0)</td><td>(1,0)</td><td>(0,1)</td><td>(1,1)</td><td>(2,0)</td><td>(2,1)</td></tr><tr><td>{u(z),... u(z)}</td><td>{1}</td><td>{2,3}</td><td>{2,3,4}</td><td>{4,5}</td><td>{3,4,5}</td><td>{6}</td></tr></table>

The utility values can also be conceptualized using the definitions of “upper wedge” (U(z)) and “lower wedge” (L(z)), where

$$
\begin{array}{l} U (z) = \{z ^ {\prime} \in Z   |   z ^ {\prime} \geq z \} \quad \text { and } \\ L (z) = \{z ^ {\prime} \in Z   |   z \geq z ^ {\prime} \}. \end{array}\tag{2}
$$

Now, the lower and upper bounds of z are simply a function of the number of elements in $U(z)$ and $L(z)$ , i.e.,

$$
\mathbf {u} (z) = \# L (z), \quad \overline {{{{u}}}} (z) = \# Z - \# U (z) + 1.\tag{3}
$$

The existence of a priori information about the comparability of certain bundles (from the viewpoint of the manager) implies that the range of values associated with that bundle will also be small. The lack of a priori information implies a larger range, i.e., a large number of alternate utility values associated with the bundle. For example, in the case of either bundle $(0, 0)$ or bundle $(2, 1)$ , the lower bound equals the upper bound. On the other hand, the bundles $(0, 1)$ and $(2, 0)$ have the greatest number of alternate utility values associated with them since the difference between the upper and lower bounds are the largest among all the bundles.

In the information gathering process, a manager has to operate in several successive stages to be able to infer each individual agent's preference ordering over commodity bundles. Each action allows the identification of a subset of utility functions. In other words, each information gathering action $a \in A$ results in a signal that partitions the original state space (F) into subsets of the state space or (ultimately) into a singleton element $f^{h}, h = 1, \ldots, \#F$ .

At each stage in the information acquisition process, all nontrivial experiments would deal only with the (a priori) noncomparable bundles (note: $\mathcal{C}(z)$ is updated at each stage). The experimental set for this example is $A = \{a_{1}, a_{2}, a_{3}\}$ , where the nontrivial pairwise comparison experiments are

$$
\begin{array}{c} a _ {1} = \langle (1, 0): (0, 1) \rangle , \quad a _ {2} = \langle (2, 0): (0, 1) \rangle , \\ a _ {3} = \langle (2, 0): (1, 1) \rangle . \end{array}
$$

When two bundles about which there is no a priori comparative preference information are compared, the results of the comparison can be used to make further inferences (that are consistent with the axioms of rationality) about other bundles and about other experiments. In essence the axiom of transitivity is used to build a transitive closure of the preference relationships at each step. Thus, the deductive process is used to update and extend the preference ordering for each individual agent, and to draw implications that have an effect on the choice of future experiments.

The specific scheme that we use for intra-agent polling is detailed by the following algorithm. In prior research (Rao 1987, Moore et al. 1994) we have shown that the algorithm detailed below results in the most efficient strategy for total information acquisition for a single agent. Note that the algorithm results in partitioning the state space into unique and single elements.

## 2.5. Algorithm for Information Acquisition and Utility Value Assignment

Step 1. Label the commodity bundles Z, with the maximal element denoted by $z_{p}$ (in our example this corresponds to (2, 1) in Figure 1), where Z is the commodity space with a strictly increasing weak order defined on it. The maximal element $z_{p}$ is labeled p (p = #Z).

Step 2. Form a set S consisting of all elements of Z except $z_{p}$ (which has been labeled as p). Therefore, Set S consists of #Z - 1 elements.

Step 3. While Set S is not empty or S is not singleton do the following steps:

(a) Select two bundles $h$ and $g$ whose preference relationship is not known a priori and each bundle ( $h$ and $g$ ) is preferred to all other bundles in its comparable set.

(b) Compare the bundles $h$ and $g$ .

(c) if $h > g$ ,

label h as #S. Remove h from the Set S.

else if $h \sim g$ , label both $h$ and $g$ as $\# S$ . Remove $h$ and $g$ from Set $S$ .

else if $h \prec g$ , label $g$ as $\# S$ . Remove $g$ from Set $S$ .

In the above algorithm after each labeling, the maximal element in the updated set of bundles is discarded from the Set S. The process continues till the maximal element of the updated set coincides with the minimal element of Z (corresponding to $(0, 0)$ in Figure 1).

The most efficient strategy for intra-agent polling for the above example, following the above algorithm is to start with experiment $a_{3}$ and then based on the signal received, carry out experiment $a_{2}$ or alternately $a_{1}$ (Moore et al. 1994).

## 3. Multiple Agent Problem

## 3.1. The Multiple Agent Extension to the Single Agent Problem

In the previous section a brief description of the Model as it pertained to the single agent decision making problem was offered.

In this section, we discuss extensions necessary for application to multiple agent problem solving. We shall first embed this problem in the decision model discussed so far.

This problem is essentially looked at from the perspective of team theory. The manager initiates actions by sending requests for experiments to be performed, and the individual agents send messages to the manager communicating the results of those experiments.

The actions thus conducted correspond to an m triple of experiments (one for each of the m agents). (As mentioned earlier, for our resource allocation study, we assume that the manager initially has access to the same collection of experiments for each agent. In future studies we can extend our research to include the case where each agent has access to nonsymmetric experimental strategies.)

The state space of the multiple agent problem, X, can be expressed as a Cartesian product of the individual state spaces, $X_{i}$ , of each agent, where $i = 1, \ldots, m$ . Each independent action/experiment $a_{i}$ can generate a number of different information signals. Each information signal partitions the state space $X_{i}$ for each agent ( $i = 1, \ldots, m$ ), thus creating an associated information structure.

Further we can equivalently express the state space, $X_{i}$ , in terms of the preference structure $W_{i}$ of each agent over the set of commodity bundles (see discussion in §2). Thus, any team problem with a single joint payoff function can be defined on the tuple

$$
\begin{array}{l} m \\ (\Pi W _ {i}, d). \\ i = 1 \end{array}
$$

Hence any team problem, in which messages are sent from the manager to agents, and where the final decision is made by the manager is a special case of the model in §2, with one decision maker. Since the team problem reduces to a special case of the Model, the same treatment of refinement of information structures can be applied (Moore and Whinston 1986, Balakrishnan and Whinston 1991).

## 3.2. Social Welfare Function, Pruning, and the Adjacency Matrix

The goal of the manager is to choose an allocation d from the set of allocations D, such that the expected net social welfare is maximized. Using the concept of pruning, dominated allocations can be found at each step in the information gathering process. Hence an efficient process of eliminating dominated allocations from the decision space, will also have the minimum average number of experiments.

The manager's utilitarian social welfare function is chosen to be an additively decomposable function of the form of the Bergson-Samuelson welfare function (Samuelson 1983). This form of a function allows the characterization of team performance in terms of a single dimension; allows the interaction of the agents in the team through sharing of the common resource; and offers opportunities for decentralization as well as division of labor since it is a separable function. The manager can poll the agents for information independently of each other if he so wishes, ignoring interactions that arise because of the sharing of the common resources. This can be done if the manager is more interested in the actual resource allocation rather than the process (Simon and Ando 1961).

3.2.1. The Welfare Function. We define the welfare function over the agents $i = 1, \ldots, m$ to be of the additively decomposable form:

$$
\begin{array}{l} \omega (f, d) = \omega [ (f ^ {h (1)}, \dots , f ^ {h (m)}), (z ^ {1}, \dots , z ^ {m}) ] \\ = \sum_ {i = 1} ^ {m} f ^ {h (i)} (z ^ {i}), \quad \text { where } h \in (1, \dots \# F), \end{array}\tag{4}
$$

$d = (z^{1}, \ldots, z^{m}) \in Z$ , and $f^{h(t)}$ is agent $i$ 's utility function (as revealed by the responses to the manager's queries).

The goal of this decision problem is to choose an allocation for each agent subject to the following allocation restriction: If one bundle $z^{i}$ is allocated to one agent, the remainder has to be allocated to the other agents ( $z^{i}$ is the bundle allocated to agent i).

The allocation among the members of the team is done in a way that maximizes the expected net welfare, which is a function of the expected gross welfare and the expected experimental costs for the manager. For any element of the state space $f^{h(t)}$ that is in some partition $B_{i} \subseteq X_{i}$ , at any given stage in the information gathering process, we have the following:

For a given allocation d belonging to the set of all possible allocations D,

(i) the lower bound on the gross welfare (payoff) is given by

$$
\underline {{\omega}} (d, B) = \sum_ {i = 1} ^ {m} \underline {{u}} _ {i} (z ^ {i}, B _ {i}).\tag{5}
$$

(ii) The upper bound on the gross welfare (payoff) is given by

$$
\overline {{{{\omega}}}} (d, B) = \sum_ {i = 1} ^ {m} \overline {{{{u}}}} _ {i} (z ^ {i}, B _ {i}).\tag{6}
$$

Thus we can define an admissible allocation $d'$ as one where the upper bound of the allocation $d'$ is greater than or equal to the lower bound of any alternate allocation. Similarly, we can define a dominant allocation $d'$ as one where the lower bound on the gross social welfare for an allocation is greater than or equal to the upper bound on the gross social welfare for alternate allocations, i.e.,

$$
\begin{array}{r l} & {\forall (d ^ {\prime}, d) \in D \colon \underline {{{{\omega}}}} (d ^ {\prime}, B)} \\ & {\qquad = \sum_ {i = 1} ^ {m} \underline {{{{u}}}} _ {i} (z ^ {i}, B _ {i}) \geq \sum_ {i = 1} ^ {m} \overline {{{{u}}}} _ {i} (z ^ {i}, B _ {i}) = \underline {{{{\omega}}}} (d, B)} \end{array}\tag{7}
$$

(for any alternative allocation d). It immediately follows from the above definitions that the set of dominant allocations belongs to the set of admissible allocations which in turn belongs to the set of all possible allocations.

3.2.2. Pruning Computation. This subsection discusses the computational method of reducing the size of the decision space.

An allocation d can be pruned whenever the upper bound of its payoff $\overline{\omega}(d, B)$ is less than or equal to the lower bound of the payoff of some alternate allocation $\underline{\omega}(d', B)$ . In this case, the precise payoff of the pruned allocation is guaranteed to be less than or equal to the gross social welfare of the alternate allocations.

The approach of using bounds to prune an allocation is used extensively in branch and bound literature. For example, graph algorithms such as $AO^{*}$ (Martelli and Montanari 1973, Nilsson 1980) maintain estimated cost of a solution in each path of the graph and compare it to a reference value, which could be considered as a threshold value beyond which the solution is too expensive to be considered. Thus whenever a graph path exceeds a threshold value the path would not be considered further in the search process. Our pruning algorithm employs a similar (but distinct) algorithm where the threshold value is generated within the search process and it may change in the course of searching the solution space. Hence, it is necessary to first find the threshold value and then compare the potential bounds of each path with this threshold value. This is done as follows. The information acquisition process eliminates the set of inferior allocations from the set of admissible allocations, and hence a set of admissible experiments from the manager's consideration. Thus, the choice of information gathering experiments would have a critical impact on an efficient strategy for finding a socially optimal resource allocation.

The pruning computation method admits a termination criterion for the information gathering process. The process of information acquisition ultimately terminates whenever the lower bound of the payoff of one allocation is greater than or equal to the upper bound of all the remaining allocations that have not been eliminated so far. Hence, it is not necessary for the manager to exhaustively evaluate the agent's utility functions. The process of narrowing the bounds of the payoff results in the narrowing of the choice set, and consequent narrowing of the set of decision alternatives. The implication is that it is not necessary to acquire total information, a dominant allocation can be found on the basis of partial information.

A strategy to achieve the termination criterion is as follows: the information gathering (pairwise comparison) process has to be conducted so as to partition the state space in a way that achieves/obtains tighter intervals for ranges of utility values. This would:

(i) raise the lower bound of one allocation such that it is greater than or equal to the upper bounds of the remaining allocations,

(ii) lower the upper bounds of all but one of the alternate allocations until the termination condition is met.

Thus the manager can successively reduce the size of the nondominated set of alternatives.

Each information gathering action results in an increase in $\underline{\omega}(\cdot)$ and/or a decrease in $\overline{\omega}(\cdot)$ , such that the bounds of the ranges progressively move towards convergence. Ultimately, with total information, i.e., the finest information partition, the aggregate social welfare of the resource allocation would be a single value, rather than a range of values. However, in most cases, the total information is not necessary, it is enough to gather partial information about the preference profiles that would allow pruning out all dominated allocations, resulting in a single dominant allocation, or a set of dominant allocations.

3.2.3. Adjacency Matrices. The strictly increasing weak order W on Z, is a reflexive, transitive relation on Z. The strictly increasing weak order property over bundles in Z space can now be represented by an adjacency matrix W, which gives information about the preference orders of each agent. Note that initially, the adjacency matrix is tentative since it gets updated as additional information gets available. To further refine the preference orders, it is necessary to conduct experiments, and thereby determine the appropriate order for the commodity bundles in question.

This is done by expanding the relationship W at each step of the information gathering process by considering the transitive closure of the relation.

An element in the ith row and jth column is '1' if the manager knows that allocation i is weakly preferred to allocation j and '0' otherwise.

Suppose at some step $(t)$ , we have the following matrix:

$$
W = W (t) = [ w (t) _ {i j} ], \quad \text { where }\tag{8}
$$

$$
w (t) _ {i j} = \left\{ \begin{array}{l l} 1 & \text { if } i W (t) j, \\ 0 & \text { otherwise. } \end{array} \right.\tag{9}
$$

Given a response for a pairwise comparison, say for pairs h and g in an adjacency matrix W, the inferencing steps would be conducted as given in the following algorithm.

## 3.2.4. Algorithm for Inferencing.

Assume $h\geq g$

Step 1: Construct two sets SetH and SetG. SetH contains all resource bundles (including h) that are in the "upper wedge" of the resource bundle h (for a definition of upper wedge see Equation 2). SetG contains all resource bundles that are in the "lower wedge" of g. Therefore, all resource bundles in SetH dominate the elements in SetG.

Step 2: If $h \sim g$ then we need to construct two more sets as follows.

Construct two sets SetG' and SetH'. SetG' contains all resource bundles (including g) that are in the upper wedge of the resource bundle g. SetH' contains all resource bundles that are in the lower wedge of h. Therefore all resource bundles in SetG' dominate the elements in SetH'.

Step 3: For each element $i \in \operatorname{Set} H$ do

for each element $j \in \operatorname{Set} G$ do

(a) Set $W(i,j)$ to 1

(b) Set $W(j, i)$ to -1

(c) Increment the lowerbound on resource bundle $i$ by 1

(d) Decrement the upperbound on resource bundle $j$ by 1

Step 4: If $h \sim g$ then repeat Step 3 for Sets SetH' and SetG'

The above algorithm updates the adjacency matrix based on the response obtained for the pairwise comparison. In Steps 3a and 3b, the entries in the adjacency matrix are updated for the agent from whom the response was obtained. Steps 3c and 3d update the lower and upper bounds for rows i and j. This lower and upper bound information is utilized in pruning computation. We see from the algorithm that the computational complexity of inferencing is in the worst case proportional to the number of cells in the adjacency matrix.

Note that the pruning computation has to examine only the upper and lower bounds of each row in the adjacency matrix. Since the upper and lower bounds are updated for each row in the inferencing stage, while pruning we need not examine the individual entries in the adjacency matrix. This approach considerably lowers the computational complexity of pruning (being proportional to the number of rows of the matrix).

Using the initial adjacency matrix, and the results of any experimental sequence, we can construct a sequence of updated W matrices, which can then be used to choose a dominant allocation. In the two-agent resource allocation problem, $D = \{(z^{1}, z^{2}) | z^{1} \in Z \text{ and } z^{2} = (\overline{z} - z^{1})\}$ where the agents are indexed by 1 and 2 respectively. The set of all (a priori) admissible allocations (the decision space) is given by the set of two-tuple pairs. The first 2-tuple consists of the allocation of the two goods to the first agent and the second 2-tuple, the complement allocations to the second agent.

For $\bar{z}=(2,1)$ the set of possible allocations, D, for the two good problem is $\{[(0,0),(2,1)],[(1,0),(1,1)],\ldots,[(2,1),(0,0)]\}$ . Say the manager conducts an experiment $\langle(2,0):(0,1)\rangle$ for both agents 1 and 2. Suppose that for

Agent 1 the manager gets the signal $(2,0) > (0,1)$ and for Agent 2 the manager receives the signal $(2,0) < (0,1)$ . Then the updated W matrix, $W_{1}$ would be constructed using the above algorithm for inferencing to give the updated bounds on the payoffs for each possible allocation. Figures 2 and 3 show how the updating is done on the matrices. The dominant allocation is shown in Figure 3(c).

An observation of the $\underline{\omega}_{1}(d)$ and $\overline{\omega}_{1}(d)$ values shows that $d(5)$ is clearly the dominant allocation. We see that it is not necessary to conduct any more experiments on Agent A or Agent B's preference profiles, even though neither agents' preference profiles are completely known. In other words, carrying out any more experiments would have no information value for the manager for the purposes of resource allocation. In summary, a manager would almost never have to take recourse to requesting that all experiments in his repertoire be conducted since:

(i) A dominant allocation emerges long before all experiments are conducted.

(ii) The marginal value of information decreases as the process of information gathering unfolds thus giving rise to a cost benefit tradeoff.

Figure 2(a) Initial Adjacency Matrix Entries for Both the Agents

<table><tr><td></td><td>(0,0)</td><td>(0,1)</td><td>(1,0)</td><td>(1,1)</td><td>(2,0)</td><td>(2,1)</td></tr><tr><td>(0,0)</td><td>*</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td></tr><tr><td>(0,1)</td><td>1</td><td>*</td><td>0</td><td>-1</td><td>0</td><td>-1</td></tr><tr><td>(1,0)</td><td>1</td><td>0</td><td>*</td><td>-1</td><td>-1</td><td>-1</td></tr><tr><td>(1,1)</td><td>1</td><td>1</td><td>1</td><td>*</td><td>0</td><td>-1</td></tr><tr><td>(2,0)</td><td>1</td><td>0</td><td>1</td><td>0</td><td>*</td><td>-1</td></tr><tr><td>(2,1)</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>*</td></tr></table>

\* Tie.

Figure 2(b) Initial Lower and Upper Bounds for the Welfare Function

<table><tr><td></td><td>Lower Bound ω(d)</td><td>Upper Bound ω̅1(d)</td></tr><tr><td>d(1) = [(0,0), (2,1)]</td><td>7</td><td>7</td></tr><tr><td>d(2) = [(0,1), (2,0)]</td><td>5</td><td>9</td></tr><tr><td>d(3) = [(1,0), (1,1)]</td><td>6</td><td>8</td></tr><tr><td>d(4) = [(1,1), (1,0)]</td><td>6</td><td>8</td></tr><tr><td>d(5) = [(2,0), (0,1)]</td><td>5</td><td>9</td></tr><tr><td>d(6) = [(2,1), (0,0)]</td><td>7</td><td>7</td></tr></table>

Figure 3(a) Adjacency Matrix for Agent A After the Response (2, 0)
(0, 1)

<table><tr><td></td><td>(0,0)</td><td>(0,1)</td><td>(1,0)</td><td>(1,1)</td><td>(2,0)</td><td>(2,1)</td></tr><tr><td>(0,0)</td><td>*</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td></tr><tr><td>(0,1)</td><td>1</td><td>*</td><td>0</td><td>-1</td><td>-1</td><td>-1</td></tr><tr><td>(1,0)</td><td>1</td><td>0</td><td>*</td><td>-1</td><td>-1</td><td>-1</td></tr><tr><td>(1,1)</td><td>1</td><td>1</td><td>1</td><td>*</td><td>0</td><td>-1</td></tr><tr><td>(2,0)</td><td>1</td><td>1</td><td>1</td><td>0</td><td>*</td><td>-1</td></tr><tr><td>(2,1)</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>*</td></tr></table>

Figure 3(b) Adjacency Matrix for Agent B After the Response (2, 0)
(0, 1)

<table><tr><td></td><td>(0,0)</td><td>(0,1)</td><td>(1,0)</td><td>(1,1)</td><td>(2,0)</td><td>(2,1)</td></tr><tr><td>(0,0)</td><td>*</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td></tr><tr><td>(0,1)</td><td>1</td><td>*</td><td>1</td><td>-1</td><td>1</td><td>-1</td></tr><tr><td>(1,0)</td><td>1</td><td>-1</td><td>*</td><td>-1</td><td>-1</td><td>-1</td></tr><tr><td>(1,1)</td><td>1</td><td>1</td><td>1</td><td>*</td><td>1</td><td>-1</td></tr><tr><td>(2,0)</td><td>1</td><td>-1</td><td>1</td><td>-1</td><td>*</td><td>-1</td></tr><tr><td>(2,1)</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>*</td></tr></table>

Figure 3(c) Lower and Upper Bounds on the Welfare Functions

<table><tr><td></td><td>Lower Bound ω(d)</td><td>Upper Bound ω̄1(d)</td></tr><tr><td>d(1) = [(0,0), (2,1)]</td><td>7</td><td>7</td></tr><tr><td>d(2) = [(0,1), (2,0)]</td><td>5</td><td>6</td></tr><tr><td>d(3) = [(1,0), (1,1)]</td><td>7</td><td>8</td></tr><tr><td>d(4) = [(1,1), (1,0)]</td><td>6</td><td>7</td></tr><tr><td>d(5) = [(2,0), (0,1)]</td><td>8</td><td>9**</td></tr><tr><td>d(6) = [(2,1), (0,0)]</td><td>7</td><td>7</td></tr></table>

\*\* Dominant allocation.

The properties discussed above help to eliminate inadmissible allocations. One can then devise prescriptions for efficient policies to be followed by the policy maker so that an optimal allocation of resources can be found.

## 4. Different Information Gathering Policies for Two Agents

Three different information gathering policies for interagent preference polling are simulated and investigated. Applications of these three policies can be found in the network environment (Fitzgerald 1993, Srinivasan and Gupta 1996). Consider the previous example of two agents. We assume the agents are denoted as Agent A and Agent B. (For the intra-agent polling scheme we utilize the Algorithm detailed in §2.)

Policy CPP (Concurrent polling with pruning computation at the end of each round): The manager polls the agents concurrently. The information structure is updated for each agent after each interrogation and after all agents respond in one round, the pruning mechanism is utilized. The manager then reviews the solutions obtained. If the dominant allocation cannot be obtained, this process of concurrent polling is continued until the final optimal solution is obtained.

This policy is geared towards single node broadcast communication (Bertsekas and Tsitsiklis 1989), the motivation here is to reduce the broadcast time.

Policy RPP (Round robin roll call polling with pruning computation after each roll call): The manager polls agents alternatively. The manager interrogates agent A and carries out the pruning computation to see if the current information is enough to guarantee dominance. If more information is required, this polling process and computation process is continued with agent B and then back to A and so on until the final optimal solution can be obtained. Therefore, the information structure for each agent is updated and the pruning algorithm utilized whenever each agent responds to a question.

Policy RPP reflects maximum flexibility on the part of the manager to switch between agents. The motivation here is to make use of the current available information to the fullest extent possible. This situation is indicative of a communication environment where switching between agents is not constrained.

Policy SPP (Sequential dedicated polling with pruning computation after each poll): The manager starts the polling process with an arbitrary agent (say, Agent A). This agent is repeatedly and exclusively polled for information. That is, the manager investigates only agent A's preference structure, carries out the pruning computation based only on agent A's information structure. Only if the final optimal allocation cannot be obtained based on agent A's final preference structure, does the policy maker investigate / poll the second agent, agent B.

This is analogous to the polling policy being dictated by the communication protocol available between the agents and the manager. The above policy reflects the availability of a dedicated link to any agent throughout the communication process.

Each policy incurs different cost structures not only for information gathering (Balakrishnan and Whinston 1991) but also for information processing (Conlisk 1988). The information gain resulting from the process of information gathering is represented by the amount of updated preference information for the agents in terms of the cumulative number of zero cells that are updated in the W matrix (see previous section for a discussion of the W matrix) for each question asked. Therefore, the higher the information gain resulting from a certain policy the more efficient the policy is.

We shall consider three types of costs incurred during information gathering and processing: communication, computation and switching costs.

Communication cost: The communication costs, $C_{k}$ , are incurred primarily for information gathering when the manager sends a question to a certain agent and when the agent responds with a signal about his preference to the manager. The more the questions that are asked, the higher the communication costs that are incurred.

Computation cost: On receiving a signal from the agent, the manager utilizes inference mechanisms to update the state space, specifically the information structure. The computation cost associated with inferencing is denoted by $C_{i}$ . The pruning computation costs, $C_{p}$ , are associated with the processing that determines (a) the dominance of a resource allocation and (b) the next experiment that is to be conducted. Therefore, the pruning computation costs increase with the number of agents because the manager has to consider all possible allocations to each agent. (Note: Also, the computation costs may change as a result of the questions asked, because as the state space is updated, different numbers of inferior allocations may be eliminated by the pruning algorithm.)

Switching cost: The switching costs, $C_{s}$ , are incurred when the manager switches the order of the questions either from Agent A to Agent B or Agent B to Agent A. Included in switching costs (Fitzgerald 1993) are setup costs, and delay costs (Balakrishnan and Whinston 1991). The more frequent the switching, the more the cost incurred because of setup or delay time (Kurose and Simha 1989, Weinrib and Gopal 1987). Clearly, information gathering Policy SPP incurs switching costs infrequently while Policies CPP and RPP incur switching costs consistently since the polling is carried out in a round robin mode. Also, the switching costs increase with the number of agents.

Therefore, the total search costs, TSC, are the weighted sum of the communication costs $C_{k}$ , the pruning computation costs $C_{p}$ , the inferencing costs $C_{i}$ , and the switching costs $C_{s}$ :

$$
\mathrm{TSC} = \alpha C _ {k} + \beta C _ {p} + \gamma C _ {i} + \delta C _ {s}.\tag{10}
$$

The choice of information gathering policy depends on the total search costs and the penalties $(\alpha, \beta, \gamma, \delta)$ for each cost, i.e., computation, communication, and switching (Stone and Bokhari 1978). The costs could be monetary or could be some other measure such as the delays involved. In the simulation experiments that we conduct we use delay as a cost measure. The problem addressed here is to minimize the total search cost (TSC) in Equation (10) subject to the constraint that the agents are allocated resources in such a way that optimal welfare is achieved.

## 5. Simulation

Two thousand simulations were conducted for each of the policies for various problem sizes. Each of the simulations was conducted for two probability scenarios, (a) with the actual probabilities for each signal (see Rao (1987) and Kaparthi and Rao (1991) for details of generating the probabilities from the lattice space enumerations), and (b) with an approximation that utilized uniform probabilities (equal probabilities for each signal).

Interestingly the same pattern of results were seen with respect to the performance of the different policies for actual and uniform probabilities (the relative performance of the policies remained the same). However, the cost figures obtained using uniform probabilities are consistently less than the corresponding costs obtained using actual probabilities. The reason for this is evident from the nature of actual probabilities, where a signal which can give the greatest amount of information is the least likely to occur at any stage of questioning, whereas with uniform probabilities the signal which yields the greatest amount of information is as likely to occur as other signals. The relative performance of the policies remains the same due to the following reason.

When uniform distribution is used in lieu of actual probability distribution for both the agents, it means that the agents' preferences are biased in the same manner. Therefore the relative performance of the different policies would remain the same.

The fact that the same patterns of results are seen for both actual and uniform probabilities would have an important implication, that it is not necessary to compute exact probability values in order to compare the different information acquisition policies. It should be noted that computation of exact probabilities involves the use of a recursion equation, a process that becomes quite complicated for large problem sizes (see Rao (1987) for a detailed discussion). The probabilities generated from a uniform distribution may be used in lieu of the actual probabilities. However, the bias introduced through the use of uniform probability distribution will have an effect on the optimal allocation of resources, i.e., the final allocation may not maximize welfare. This issue is discussed in detail in Rao et al. (1997).

## 5.1. Pruning Computations

The amount of pruning of the solution space at any stage depends on the information gathered till that stage. We note that the aggregate information gathered in the initial stages of questioning would not be sufficient to derive substantial benefits from pruning the solution space in the initial stages. In fact, it may be inefficient in terms of the computation efforts to prune the solution space in the initial stages in any of the three policies. However, it may also be inefficient to begin pruning at a very late stage in the information acquisition process as it would lead to acquisition of signals which could have been avoided had the state space been pruned earlier. Clearly, there exists an optimal point to start the pruning computations in the information acquisition process.

To verify this, we tested the policies by deferring the pruning computation till a certain amount of information had been gathered. The number of zeroes filled in the adjacency matrix is used as a measure of information gathered. To determine the optimal point at which to start pruning, we ran simulations that delayed pruning till at least 75%, 66%, 50%, 33% and 0% of the initial number of zeroes were filled in. The results of these simulations are shown in Table 1, and as charts in Figure 4. We measure the total computation delay in a policy as follows:

Total Computation Delay

## = No. of Inferences\*Delay per Inference

## + No. of Pruning\*Delay per Pruning.

The Delay per Inferencing and the Delay per Pruning are obtained by measuring the actual CPU time taken by the program to perform one inferencing and one pruning. The actual CPU times are shown in Table 6.

We observe from Figure 4 that interestingly, the computation effort is minimal when pruning starts at the half way stage. Though we have illustrated the results for a single policy (i.e., policy SPP) similar results were obtained for other policies as well.

Table 1 Computation Costs for Different Pruning Delays

<table><tr><td>Resource Space</td><td>Pruning Delay @</td><td>0.75</td><td>0.66</td><td>0.5</td><td>0.33</td><td>0</td></tr><tr><td rowspan="3">5*1</td><td>No. Of Inferences</td><td>9.757</td><td>9.757</td><td>9.7945</td><td>10.141</td><td>9.7555</td></tr><tr><td>No. of Prunes</td><td>3.788</td><td>3.621</td><td>2.68825</td><td>1.776</td><td>5.242</td></tr><tr><td>Total Computation Cost</td><td>0.092193</td><td>0.091781</td><td>0.089795</td><td>0.090484</td><td>0.095772</td></tr><tr><td rowspan="3">6*1</td><td>No. Of Inferences</td><td>11.794</td><td>11.794</td><td>11.8208</td><td>12.211</td><td>11.7893</td></tr><tr><td>No. of Prunes</td><td>4.637</td><td>4.137</td><td>3.1465</td><td>2.016</td><td>6.29025</td></tr><tr><td>Total Computation Cost</td><td>0.111584</td><td>0.110349</td><td>0.10813</td><td>0.108651</td><td>0.115628</td></tr><tr><td rowspan="3">7*1</td><td>No. Of Inferences</td><td>13.775</td><td>13.775</td><td>13.7925</td><td>14.33</td><td>13.7715</td></tr><tr><td>No. of Prunes</td><td>5.525</td><td>4.781</td><td>3.5575</td><td>2.24</td><td>7.29125</td></tr><tr><td>Total Computation Cost</td><td>0.130597</td><td>0.128759</td><td>0.125885</td><td>0.127195</td><td>0.134929</td></tr><tr><td rowspan="3">8*1</td><td>No. Of Inferences</td><td>15.864</td><td>15.864</td><td>15.863</td><td>16.366</td><td>15.8573</td></tr><tr><td>No. of Prunes</td><td>6.163</td><td>5.607</td><td>4.146</td><td>3.291</td><td>8.385</td></tr><tr><td>Total Computation Cost</td><td>0.149908</td><td>0.148535</td><td>0.144917</td><td>0.147076</td><td>0.155339</td></tr></table>

Figure 4 Computation Delays Under Delayed Pruning

<table><tr><td>Computation DelayFor 5*1</td><td>Computation DelayFor 6*1</td></tr><tr><td>Computation DelayFor 7*1</td><td>Computation DelayFor 8*1</td></tr></table>

We further conjectured that it may still not be efficient to prune after each round of polling. It may be more efficient to prune at various intervals. For this, we decided to prune at the following intervals: after the first half number of zeroes are filled, and then we prune at each stage where the number of zeroes fall to half the number at the previous pruning stage, i.e., if we do the first pruning computation when the number of zeroes are 30, we prune next when the number of zeroes fall to 15, 7, 3, and 1, where the number of zeroes are checked after each polling. Based on the above discussion on pruning computations we can derive new policies from the three main policies proposed earlier. We list the various policies tested in our simulations below.

Policy CPP.0. This is the same as policy CPP discussed earlier (concurrent polling with the pruning computation at the end of each round).

Policy CPP.1. This is derived from policy CPP.0 and works as follows: The agents are polled as in policy CPP.0, however, the pruning of state space begins when at least half the initial number of zeroes have been filled in, i.e., at least half the information required initially has been acquired. The subsequent stages are similar to that of policy CPP.0.

Policy CPP.2. This is again derived from Policy CPP.0, and works as follows: The agents are polled as in policy CPP.0 and the pruning of state space begins when at least half the initial number of zeroes have been filled in, i.e., at least half the information required initially have been acquired. Subsequent pruning computations are conducted when the number of zeroes in the adjacency matrices of the agents falls to half the number at the previous pruning computation stage.

Policy RPP.0. This is Policy RPP explained in the earlier section (round robin roll call polling with pruning computation after each roll call).

Policy RPP.1. This policy is derived from policy RPP.0 and proceeds as follows: Till half the original number of zeroes have been filled in, no pruning is done (and the agents are polled as in Policy RPP.0), after which pruning computations are conducted as in policy RPP.0.

Policy SPP.0. This is policy SPP described in the previous section (sequential dedicated polling with pruning computation after each poll).

Policy SPP.1. This policy follows the polling pattern outlined in policy SPP.0, however, as in the other derived policies, pruning is delayed till the half way stage of information acquisition. Subsequently, both polling and pruning patterns follow the pattern of policy SPP.0.

Policy SPP.2. This policy follows the polling pattern of policy SPP.0, and the pruning pattern of policy SPP.1 until the first pruning. After the first pruning computation is conducted, the next pruning computation is delayed till half the amount of information required at the end of the first pruning stage have been acquired, and so on.

Policy CP.0. This is a benchmark policy that does no pruning, and polls the agents as in policy CPP.0.

Policies CPP.X and Policies RPP.X follow a democratic policy as far as polling is concerned, whereas policies SPP.X follow a "preferential" polling policy by polling one agent exclusively followed by the other agent.

We have listed the different policies in Table 2. In Table 2, I denotes an Inferencing Stage, and P denotes a pruning stage, $I_{A}$ indicates that the inferencing is done after questioning Agent A, and $I_{B}$ indicates that the inferencing is done after questioning agent B.

## 5.2. Conjectures

Based on the individual characteristics of the policies we make the following conjectures on performance characteristics of these policies as follows.

Conjecture 1. We conjecture that policies CPP.X and policies RPP.X would require lesser number of questions than policies SPP.X since they use information from both the agents in their inferencing from the beginning and thus may be able to more efficiently conduct the polling process.

Conjecture 2. Policies that delay pruning computations till the half way point are more efficient computationally than corresponding policies that prune from the beginning. Hence, we expect that policies CPP.1 and CPP.2 would be computationally efficient compared to policy CPP.0, similarly, policy RPP.1 would be computationally efficient compared to RPP.0, and policies SPP.1 and SPP.2 would be computationally efficient compared to policy SPP.0.

Conjecture 3. Among policies CPP.0, CPP.2 and RPP.1, policy CPP.2 should be computationally more efficient, since it minimizes the number of pruning computations.

Conjecture 4. Not performing any pruning computations would result in the maximum number of questions. We expect this to happen since pruning allows further reduction of state-space.

## 5.3. Results

Based on the simulation results, we observe the following in terms of our conjectures:

Conjecture 1. As predicted in Conjecture 1, policies CPP.X and RPP.X indeed need lesser number of questions when compared to policies SPP.X (Refer to Tables

3(a) and (b)). Policy RPP.1 requires the least number of questions. Since communication costs are proportional to the number of questions, Policy RPP.1 would incur the least communication cost, while Policy SPP.2 would require the maximum communication cost. The fact that Policy RPP.1 (or Policy RPP.0) entails less questions than Policy SPP.2 (or Policy SPP.0), suggests that a “democratic” polling policy than a “preferential” polling policy like Policy SPP.2 (or Policy SPP.0) is more effective. This result is interesting and a probable explanation for this phenomenon could be that Policy RPP.1 (also Policy RPP.0) always makes use of the updated information structure and helps ask appropriate questions to the agent as opposed to Policy CPP.2 and Policy CPP.0. For the CPP policies, the results of refining agent A’s (or agent B’s) information structure are not available when asking a question to agent B (or agent A) until the next polling session, since agents are polled simultaneously. Policy RPP.0 on the other hand always makes use of the updated information structure and helps ask more appropriate questions to the agents.

Conjecture 2. We observe from Tables 4(a), (b) and 5(a), (b) that while delaying the pruning computations has resulted in the reduction of the number of pruning computation stages, in general, it also results in a slight increase in the number of questions asked (except for Policy SPP.1 that reduces both the number of questions and pruning computation stages as compared to Policy SPP.0). However, to test whether these policies reduce the total computation costs we need to take into account both unit computation and pruning costs. We explore this further in the later part of this section.

Conjecture 3. We observe from Tables 4 and 5 that policies RPP.1 and CPP.2 do reduce the number of pruning computation stages, however, this is accompanied by an increase in the number of questions, thus it is unclear as yet if they do minimize the computation costs. We explore this interesting aspect of pruning v/s inferencing tradeoff further in a later part of this section.

Table 2 Different Policies Tested in Simulation

<table><tr><td>Policy →</td><td>Policy CPP.0</td><td>Policy RPP.0</td><td>Policy SPP 0</td><td>Policy CPP.1</td><td>Policy CPP.2</td><td>Policy RPP.1</td><td>Policy SPP 1</td><td>Policy SPP.2</td><td>Policy CP.0</td></tr><tr><td>Explanation</td><td>IIPIIP..</td><td>IPIPIP..</td><td>IaPlaP. IbPlbP</td><td>III. .(half life-HL)IIPIIP</td><td>III. .(halflife)PIII(HL)P. .</td><td>III(HL)PIPIPIPla</td><td>(HL)PlaP ibPlbP..</td><td>Iala (HL)Pla.(HL)P.. Ib. (HL)P</td><td>IIIIIIIIII . .</td></tr></table>

Table 3a No. of Switches in Each Policy (Actual Probabilities)

<table><tr><td>Problem Size</td><td>Policy CPP.0</td><td>Policy RPP.0</td><td>Policy SPP.0</td><td>Policy CPP.1</td><td>Policy CPP.2</td><td>Policy RPP.1</td><td>Policy SPP.1</td><td>Policy SPP.2</td><td>Policy CP.0</td></tr><tr><td>5 × 1</td><td>11.3215</td><td>10.609</td><td>2</td><td>11.3625</td><td>11.1868</td><td>10.65</td><td>2</td><td>2</td><td>12.101</td></tr><tr><td>6 × 1</td><td>13.369</td><td>12.637</td><td>2</td><td>13.4082</td><td>13.437</td><td>12.6337</td><td>2</td><td>2</td><td>15.6842</td></tr><tr><td>7 × 1</td><td>15.3647</td><td>14.596</td><td>2</td><td>15.392</td><td>15.7603</td><td>14.613</td><td>2</td><td>2</td><td>17.362</td></tr><tr><td>8 × 1</td><td>17.471</td><td>16.5615</td><td>2</td><td>17.4827</td><td>17.995</td><td>16.5737</td><td>2</td><td>2</td><td>20.0825</td></tr></table>

Table 3b No. of Switches in Each Policy (Uniform Probabilities)

<table><tr><td>Problem Size</td><td>Policy CPP.0</td><td>Policy RPP.0</td><td>Policy SPP.0</td><td>Policy CPP.1</td><td>Policy CPP.2</td><td>Policy RPP.1</td><td>Policy SPP.1</td><td>Policy SPP.2</td><td>Policy CP.0</td></tr><tr><td>5 × 1</td><td>10.448</td><td>9.822</td><td>2</td><td>10.468</td><td>10.235</td><td>9.824</td><td>2</td><td>2</td><td>10.976</td></tr><tr><td>6 × 1</td><td>12.308</td><td>11.58</td><td>2</td><td>12.332</td><td>12.184</td><td>11.574</td><td>2</td><td>2</td><td>13.266</td></tr><tr><td>7 × 1</td><td>14.068</td><td>13.3</td><td>2</td><td>14.083</td><td>14.184</td><td>13.311</td><td>2</td><td>2</td><td>15.506</td></tr><tr><td>8 × 1</td><td>15.851</td><td>15.052</td><td>2</td><td>15.859</td><td>16.153</td><td>15.063</td><td>2</td><td>2</td><td>17.921</td></tr></table>

Conjecture 4. We observe from Table 4 that Policy CP.0 which does not perform any pruning requires the maximum number of questions as predicted in Conjecture 4.

Thus we can summarize our observations from Tables 3 to 5 as follows:

(1) Policy CP.0 requires the largest number of questions, while

(2) Policy SPP.0 (and policies derived from it) incurs the least switching costs because there is only one switch between agents. Switching costs for Policy RPP.0 (and policies derived from it) are smaller than those of Policy CPP.0 (and policies derived from it). We might garner that the more efficient policy (like Policy RPP.0) would require less questions and hence less switching.

Table 4a No. of Questions in Each Policy (Actual Probabilities)

<table><tr><td>Problem Size</td><td>Policy CPP.0</td><td>Policy RPP.0</td><td>Policy SPP.0</td><td>Policy CPP.1</td><td>Policy CPP.2</td><td>Policy RPP.1</td><td>Policy SPP.1</td><td>Policy SPP.2</td><td>Policy CP.0</td></tr><tr><td>5 × 1</td><td>9.7555</td><td>9.2855</td><td>10.0935</td><td>9.7945</td><td>9.9602</td><td>9.321</td><td>10.0772</td><td>10.3728</td><td>10.9493</td></tr><tr><td>6 × 1</td><td>11.7893</td><td>11.2568</td><td>12.257</td><td>11.8208</td><td>12.1652</td><td>11.2635</td><td>12.2373</td><td>12.7948</td><td>13.5422</td></tr><tr><td>7 × 1</td><td>13.7715</td><td>13.1792</td><td>14.4522</td><td>13.7925</td><td>14.4395</td><td>13.207</td><td>14.4327</td><td>15.2952</td><td>16.2292</td></tr><tr><td>8 × 1</td><td>15.8573</td><td>15.1365</td><td>16.661</td><td>15.863</td><td>16.6478</td><td>15.1475</td><td>16.6437</td><td>17.9083</td><td>18.96</td></tr></table>

Table 4b No. of Questions in Each Policy (Uniform Probabilities)

<table><tr><td>Problem Size</td><td>Policy CPP.0</td><td>Policy RPP.0</td><td>Policy SPP.0</td><td>Policy CPP.1</td><td>Policy CPP.2</td><td>Policy RPP.1</td><td>Policy SPP.1</td><td>Policy SPP.2</td><td>Policy CP.0</td></tr><tr><td>5 × 1</td><td>8.872</td><td>8.497</td><td>8.737</td><td>8.892</td><td>9.025</td><td>8.488</td><td>8.737</td><td>8.975</td><td>9.864</td></tr><tr><td>6 × 1</td><td>10.756</td><td>10.201</td><td>10.529</td><td>10.751</td><td>10.885</td><td>10.171</td><td>10.532</td><td>10.934</td><td>12.129</td></tr><tr><td>7 × 1</td><td>12.444</td><td>11.899</td><td>12.307</td><td>12.449</td><td>12.875</td><td>11.899</td><td>12.313</td><td>12.906</td><td>14.379</td></tr><tr><td>8 × 1</td><td>14.221</td><td>13.603</td><td>14.09</td><td>14.221</td><td>14.773</td><td>13.605</td><td>14.102</td><td>14.923</td><td>16.783</td></tr></table>

INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 2, June 1997

Table 5a No. of Pruning Computations in Each Policy (Actual Probabilities)

<table><tr><td>Problem Size</td><td>Policy CPP.0</td><td>Policy RPP.0</td><td>Policy SPP.0</td><td>Policy CPP.1</td><td>Policy CPP.2</td><td>Policy RPP.1</td><td>Policy SPP.1</td><td>Policy SPP.2</td><td>Policy CP.0</td></tr><tr><td>5 × 1</td><td>5.242</td><td>9.2855</td><td>10.0935</td><td>2.6883</td><td>2.1673</td><td>3.7415</td><td>3.3618</td><td>2.059</td><td>0</td></tr><tr><td>6 × 1</td><td>6.2903</td><td>11.2568</td><td>12.257</td><td>3.1465</td><td>2.3433</td><td>4.4933</td><td>3.9298</td><td>2.3510</td><td>0</td></tr><tr><td>7 × 1</td><td>7.2913</td><td>13.1792</td><td>14.4522</td><td>3.5575</td><td>2.581</td><td>5.2353</td><td>4.542</td><td>2.5173</td><td>0</td></tr><tr><td>8 × 1</td><td>8.385</td><td>15.1365</td><td>16.661</td><td>4.146</td><td>2.7195</td><td>6.1703</td><td>5.0945</td><td>2.7045</td><td>0</td></tr></table>

Table 5b No. of Pruning Computations in Each Policy (Uniform Probabilities)

<table><tr><td>Problem Size</td><td>Policy CPP.0</td><td>Policy RPP.0</td><td>Policy SPP.0</td><td>Policy CPP.1</td><td>Policy CPP.2</td><td>Policy RPP.1</td><td>Policy SPP.1</td><td>Policy SPP.2</td><td>Policy CP.0</td></tr><tr><td>5 × 1</td><td>4.787</td><td>8.497</td><td>8.737</td><td>2.576</td><td>2.263</td><td>3.709</td><td>3.009</td><td>2.047</td><td>0</td></tr><tr><td>6 × 1</td><td>5.75</td><td>10.201</td><td>10.529</td><td>3.162</td><td>2.442</td><td>4.536</td><td>3.542</td><td>2.258</td><td>0</td></tr><tr><td>7 × 1</td><td>6.662</td><td>11.899</td><td>12.307</td><td>3.556</td><td>2.669</td><td>5.219</td><td>4.054</td><td>2.474</td><td>0</td></tr><tr><td>8 × 1</td><td>7.583</td><td>13.603</td><td>14.09</td><td>4.184</td><td>2.887</td><td>6.305</td><td>4.558</td><td>2.648</td><td>0</td></tr></table>

(3) Policy SPP.0 incurs the largest number of pruning computation stages. Pruning computation stages for policies Policy CPP.1 and Policy SPP.2 are the least. However, as a tradeoff these policies require higher communication costs. A “preferential” polling policy like Policy SPP.0 is observed to incur the largest pruning costs. This suggests that inferior allocations are not eliminated here as much as in other policies. In this regard, such a policy is unattractive. A possible explanation for such a shortcoming could be the fact that the lack of consideration of the second agent’s preferences until later in the polling process does not help identify inferior allocations quickly. Observation 3 reiterates the benefits of a more “democratic” polling policy.

(4) With equal weights associated to the three different costs of communication costs, switching costs, and pruning computation costs, the total search cost (TSC) for the undemocratic polling policies (like Policy SPP.0 and policies derived from it) remains the lowest, although simulation indicates that these policies are not generally as effective as other policies in terms of communication costs and pruning computation costs. The low total cost for Policy SPP.0 may be attributed mainly to the low, constant switching costs incurred for this policy.

## 5.4. Discussion

While the above observations describe the general characteristics of the different policies, the particular policy to be chosen for a specific problem depends on the over all cost function of that problem. While it is possible that some managers may need to minimize only one of the above categories of costs, for example, only the communication cost may be relevant, it may not generally be the case. In general, the overall cost structure could be a function consisting of the above three cost categories as in Equation (10). Below, we consider three different cost functions and analyze the policies in each case.

Case 1. Cost Function Consisting of Only Computation Delay. In this case we consider a situation where computation delays have to be kept to a minimum. The cost function could then be written as follows:

Computation Delay

= Time per Inference\*No. of Inferences

\+ Time per Pruning\*No. of Pruning Computations

The computation time required by the algorithm in terms of the time per inferencing and pruning that we obtained are given in Table 6 (actual CPU time).

Table 6 Computation Delays in Terms of Actual CPU Time

<table><tr><td>Resource Space</td><td>Time per Inference (Secs.)</td><td>Time per Pruning (Secs.)</td></tr><tr><td>5 × 1</td><td>8.49 E-3</td><td>0.247 E-3</td></tr><tr><td>6 × 1</td><td>1.116 E-2</td><td>0.052 E-2</td></tr><tr><td>7 × 1</td><td>1.4114 E-2</td><td>0.1836 E-2</td></tr><tr><td>8 × 1</td><td>1.725 E-2</td><td>0.2554 E-2</td></tr></table>

Using Tables 4, 5, and 6, we can compute the value of the cost functions for the policies. Table 7 shows the comparisons among the policies for this objective. We see that Policy RPP.1 incurs a minimum amount of computation delay when compared to other policies. Hence, Policy RPP.1 is computationally the most efficient among all the policies. In general, we observe that policies which poll both agents alternatingly fare better in terms of computation as compared to policies that poll one agent repeatedly before polling the other agent. In addition, not pruning the solution space in the initial stages is found to be more efficient in terms of computation. The reason for this could be that the information available in the initial stages may be too little to prune the solution space, and hence any attempt to prune would incur computation costs without any associated benefit in terms of reducing the number of admissible orderings.

Case 2. Polling over a computer network using TCP/IP. In this case we assume that the polling is automated, that is polling is carried out by an automated manager (e.g., a computer program) that communicates with the agents over a computer network. When the manager has to poll the agents over a TCP/IP network, the manager will have to establish connection over the communication network with the agents. A nontrivial amount of time would be spent in setting up this connection. In addition, the actual communication itself would again incur time delays. Let us assume that the manager can establish a connection and communicate with only a single agent at a time. This means that there will be a switching delay when the questioning is switched between the agents. For illustrative purposes we use representative time figures for communication and switching delays from Stevens (1994). Further assuming that the automated manager is a program similar to the one used in the simulation experiments, we can use the computation delays from Table 6. Every communication with a node involves the establishment of a connection, communicating the question, getting the appropriate response. After obtaining the response the manager does the inferencing and pruning (based on which policy is being used). Also, the manager has to break a connection if it has to switch from one agent to another, if the next question is to the same agent, no switching delay is incurred as there is no need to establish a new connection. Switching delay is the sum of the time required for setting up a connection and then terminating it. The switching and computation delays used in our analysis are (Stevens 1994)

$$
\text { Switching   Delay } = 4 \text {   Secs., }
$$

$$
\text { Communication   Delay } = 8 \text {   Secs.   }
$$

As mentioned before these figures are for illustrative purposes to show how a policy can be chosen for a particular scenario. The delay numbers could change depending on the network configuration, distance between the server and the agents and the type of computer system being used. Table 8 shows the costs incurred under each category as well as the total cost incurred by each policy.

Table 7 Computation Delays for Case 1

<table><tr><td>Resource Space</td><td>Policy CPP.0</td><td>Policy RPP.0</td><td>Policy SPP.0</td><td>Policy CPP.1</td><td>Policy CPP.2</td><td>Policy RPP.1</td><td>Policy SPP.1</td><td>Policy SPP.2</td><td>Policy CP.0</td></tr><tr><td> $5 \times 1$ </td><td>0.095772</td><td>0.101769</td><td>0.110625</td><td>0.089795</td><td>0.089915</td><td>0.088377</td><td>0.093859</td><td>0.093151</td><td>0.09296</td></tr><tr><td> $6 \times 1$ </td><td>0.13484</td><td>0.131479</td><td>0.143162</td><td>0.133556</td><td>0.136982</td><td>0.128037</td><td>0.138612</td><td>0.144012</td><td>0.151131</td></tr><tr><td> $7 \times 1$ </td><td>0.207758</td><td>0.210208</td><td>0.230513</td><td>0.201199</td><td>0.208538</td><td>0.196016</td><td>0.212042</td><td>0.220498</td><td>0.229059</td></tr><tr><td> $8 \times 1$ </td><td>0.294954</td><td>0.299763</td><td>0.329954</td><td>0.284226</td><td>0.29412</td><td>0.277053</td><td>0.300115</td><td>0.315825</td><td>0.32706</td></tr></table>

Table 8 Delay Numbers for the Policies in Case 2

<table><tr><td>Resource Space</td><td>Total Delays</td><td>Policy CPP.0</td><td>Policy RPP.0</td><td>Policy SPP.0</td><td>Policy CPP.1</td><td>Policy CPP.2</td><td>Policy RPP.1</td><td>Policy SPP.1</td><td>Policy SPP.2</td><td>Policy CP.0</td></tr><tr><td rowspan="4">5 × 1</td><td>Comm. Delay</td><td>78.044</td><td>74.284</td><td>80.748</td><td>78.356</td><td>79.6816</td><td>74.568</td><td>80.6176</td><td>82.9824</td><td>87.5944</td></tr><tr><td>Switching Delay</td><td>45.286</td><td>42.436</td><td>8</td><td>45.45</td><td>44.7472</td><td>42.6</td><td>8</td><td>8</td><td>48.404</td></tr><tr><td>Comp. Delay</td><td>0.095772</td><td>0.101769</td><td>0.110625</td><td>0.089795</td><td>0.089915</td><td>0.088377</td><td>0.093859</td><td>0.093151</td><td>0.09296</td></tr><tr><td>Total</td><td>123.4258</td><td>116.8218</td><td>88.85862</td><td>123.8958</td><td>124.5187</td><td>117.2564</td><td>88.71146</td><td>91.07555</td><td>136.0914</td></tr><tr><td rowspan="4">6 × 1</td><td>Comm. Delay</td><td>94.3144</td><td>90.0544</td><td>98.056</td><td>94.5664</td><td>97.3216</td><td>90.108</td><td>97.8984</td><td>102.3584</td><td>108.3376</td></tr><tr><td>Switching Delay</td><td>53.476</td><td>50.548</td><td>8</td><td>53.6328</td><td>53.748</td><td>50.5348</td><td>8</td><td>8</td><td>62.7368</td></tr><tr><td>Comp. Delay</td><td>0.13484</td><td>0.131479</td><td>0.143162</td><td>0.133556</td><td>0.136982</td><td>0.128037</td><td>0.138612</td><td>0.144012</td><td>0.151131</td></tr><tr><td>Total</td><td>147.9252</td><td>140.7339</td><td>106.1992</td><td>148.3328</td><td>151.2066</td><td>140.7708</td><td>106.037</td><td>110.5024</td><td>171.2255</td></tr><tr><td rowspan="4">7 × 1</td><td>Comm. Delay</td><td>110.172</td><td>105.4336</td><td>115.6176</td><td>110.34</td><td>115.516</td><td>105.656</td><td>115.4616</td><td>122.3616</td><td>129.8336</td></tr><tr><td>Switching Delay</td><td>61.4588</td><td>58.384</td><td>8</td><td>61.568</td><td>63.0412</td><td>58.452</td><td>8</td><td>8</td><td>69.448</td></tr><tr><td>Comp. Delay</td><td>0.207758</td><td>0.210208</td><td>0.230513</td><td>0.201199</td><td>0.208538</td><td>0.196016</td><td>0.212042</td><td>0.220498</td><td>0.229059</td></tr><tr><td>Total</td><td>171.8386</td><td>164.0278</td><td>123.8481</td><td>172.1092</td><td>178.7657</td><td>164.304</td><td>123.6736</td><td>130.5821</td><td>199.5107</td></tr><tr><td rowspan="4">8 × 1</td><td>Comm. Delay</td><td>126.8584</td><td>121.092</td><td>133.288</td><td>126.904</td><td>133.1824</td><td>121.18</td><td>133.1496</td><td>143.2664</td><td>151.68</td></tr><tr><td>Switching Delay</td><td>69.884</td><td>66.246</td><td>8</td><td>69.9308</td><td>71.98</td><td>66.2948</td><td>8</td><td>8</td><td>80.33</td></tr><tr><td>Comp. Delay</td><td>0.294954</td><td>0.299763</td><td>0.329954</td><td>0.284226</td><td>0.29412</td><td>0.277053</td><td>0.300115</td><td>0.315825</td><td>0.32706</td></tr><tr><td>Total</td><td>197.0374</td><td>187.6378</td><td>141.618</td><td>197.119</td><td>205.4565</td><td>187.7519</td><td>141.4497</td><td>151.5822</td><td>232.3371</td></tr></table>

We observe from Table 8 that policies Policy SPP.0, Policy SPP.1, and Policy SPP.2 perform the best in this case, with Policy SPP.1 having the minimum delay. These policies fare better because they minimize the number of switches (which is a constant number equal to 2). Since these policies have to establish a connection with an agent only once they are able to minimize the switching delays, and since switching and communication delays are of the same order (secs) of magnitude and the other policies have almost the same number of switches as the number of questions, they do not perform as well as these policies. However, when we consider the individual delays, we observe that Policy RPP.1 incurs the least amount of computation and communication delays. Thus, one may expect that Policy RPP.1 would be a better option when switching delays are insignificant compared to computation and communication delays. For example, assume that the manager can accommodate multiple connections, i.e., he can maintain a connection between the two agents simultaneously. Now the manager need not have to close a connection every time he has to switch between agents. Therefore, a connection is established and broken only once for each agent, and hence the switching delay for each policy would be the same. Under this scenario, Policy RPP.1 would incur the minimum delay.

Case 3. Communication Through E-Mail/Telephone/Fax. When the manager has to communicate over e-mail, telephone or fax media, the cost structures would be significantly different as compared to the previous case; for example, one significant difference would be the absence of switching delays. The manager would incur the same amount of delay for communicating a response whether he switches from one agent to another or not. In addition, use of this media implies that computation delays are larger as the process would normally require human mediation, unlike the previous example where the coordination activity was essentially handled by a computer over a computer network. The following numbers are used as delay factors for this case:

$$
\text { Communication   Delay } = 3 6 0 \text {   Secs. },
$$

$$
\text { Switching   Delay } = 0 \text {   Secs. }
$$

It is assumed that switching delay is embedded in the communication delay, as the time required to ask a question is the same, whether there is a switch from one agent to another or not. Assuming manual inferencing and pruning, we approximate the processing times required of the manager as follows, which are indicative of the time required to carry out the computations. Since the effort needed to infer from a question would be dependent on the size of the matrix (no. of cells), we compute the time required to complete an inferencing stage as follows:

Inferencing Time in Secs. = Size of the Matrix.

The pruning computation effort would be dependent on the number of rows in the matrix. Therefore, we compute the pruning time as follows:

Pruning Time = No. of Rows in the Matrix\*4 Secs.

However, the numbers used above are arbitrary estimates, the actual time taken by a particular manager could vary. The inferencing and pruning times for different resource spaces are given in Table 9. The performance of the policies in Case 3 are given in Table 10. We observe now that Policy RPP.1 outperforms all other policies. Since, Policy RPP.1 minimizes both the number of questions and the number of pruning computations it performs better than the other policies in this scenario. Since switching cost is zero in this case, policies targeted at minimizing switching costs do not perform well.

Another interesting possibility is the case in which the questioning is manually done as in Case 3, but computation is done using a computer program as in Case 2. In such a case, the manager would manually enter the response to the program, which then does the inferencing and pruning. In this case, both computation and switching delays would not be very important, since computation time is very small (in milliseconds) compared to the communication time. Thus Policy RPP.0 which minimizes the number of questions and hence the total communication delay would be a better choice under this case, with Policy RPP.1 coming in as a close second.

In this study, we have tested several different information gathering policies in order to investigate which policy is the most efficient one. These policies are motivated by communication link restrictions found in the network environment. The paper has shown the following:

Table 9 Computation Times for Case 3

<table><tr><td>Resource Space</td><td>No. Of Rows</td><td>No. Of Cells</td><td>Time per Inference (Secs)</td><td>Time per Pruning (Secs)</td></tr><tr><td>5 × 1</td><td>12</td><td>144</td><td>144</td><td>48</td></tr><tr><td>6 × 1</td><td>14</td><td>196</td><td>196</td><td>56</td></tr><tr><td>7 × 1</td><td>16</td><td>256</td><td>256</td><td>64</td></tr><tr><td>8 × 1</td><td>18</td><td>324</td><td>324</td><td>72</td></tr></table>

\- The importance of using a correct polling policy with a dual objective of minimizing costs and acquiring information quickly is illustrated by the simulation.

\- The tradeoff between the different policies with respect to communication, computation and switching costs provides a valuable insight into what constitutes an effective information gathering policy. Depending on the penalties incurred for the costs in any particular situation, any of the policies could emerge as the winner. The paper illustrates the case when equal penalties are assigned to the cost components, as well as three different scenarios.

\- The study reveals the characteristic of a policy (Policy RPP.0 in the paper) that acquires information quickly (in terms of communication delays). This confirms the benefits of having information assimilated in the decision making process as and when it is available. However, the study also reveals that there are economies of scale as far as information processing is concerned. For example, the study reveals that pruning at initial stages of information acquisition may not be efficient in terms of computation and it may be beneficial to delay the pruning of the solution space until an appropriate stage in the information acquisition process. We further have shown empirically that starting pruning at the midway stage of information gathering is most efficient in terms of computation.

\- The use of uniform probability distributions is found to be a good approximation to the actual probability distribution in simulating the responses of agents (in accordance with their preferences). A decision making policy with minimum dependence on probability distributions and utility functions is most accessible (Weber 1987). To this extent, the decision making policies discussed here are shown to be accessible.

Table 10 Delay Numbers for the Policies in Case 3

<table><tr><td>Resource Space</td><td>Total Delays</td><td>Policy CPP.0</td><td>Policy RPP.0</td><td>Policy SPP.0</td><td>Policy CPP.1</td><td>Policy CPP.2</td><td>Policy RPP.1</td><td>Policy SPP.1</td><td>Policy SPP.2</td><td>Policy CP.0</td></tr><tr><td rowspan="4">5 × 1</td><td>Comm. Delay</td><td>3511.98</td><td>3342.78</td><td>3633.66</td><td>3526.02</td><td>3585.672</td><td>3355.56</td><td>3627.792</td><td>3734.208</td><td>3941.748</td></tr><tr><td>Switching Delay</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Comp. Delay</td><td>1656.41</td><td>1782.816</td><td>1937.952</td><td>1539.444</td><td>1538.297</td><td>1521.816</td><td>1612.481</td><td>1592.515</td><td>1576.699</td></tr><tr><td>Total</td><td>5168.39</td><td>5125.596</td><td>5571.612</td><td>5065.464</td><td>5123.969</td><td>4877.376</td><td>5240.273</td><td>5326.723</td><td>5518.447</td></tr><tr><td rowspan="4">6 × 1</td><td>Comm. Delay</td><td>4244.15</td><td>4052.448</td><td>4412.52</td><td>4255.488</td><td>4379.472</td><td>4054.86</td><td>4405.428</td><td>4606.128</td><td>4875.192</td></tr><tr><td>Switching Delay</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Comp. Delay</td><td>2662.96</td><td>2836.714</td><td>3088.764</td><td>2493.081</td><td>2515.601</td><td>2459.268</td><td>2618.58</td><td>2639.437</td><td>2654.271</td></tr><tr><td>Total</td><td>6907.11</td><td>6889.162</td><td>7501.284</td><td>6748.569</td><td>6895.073</td><td>6514.128</td><td>7024.008</td><td>7245.565</td><td>7529.463</td></tr><tr><td rowspan="4">7 × 1</td><td>Comm. Delay</td><td>4957.74</td><td>4744.512</td><td>5202.792</td><td>4965.3</td><td>5198.22</td><td>4754.52</td><td>5195.772</td><td>5506.272</td><td>5842.512</td></tr><tr><td>Switching Delay</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Comp. Delay</td><td>3992.14</td><td>4217.344</td><td>4624.704</td><td>3758.56</td><td>3861.696</td><td>3716.048</td><td>3985.459</td><td>4076.678</td><td>4154.675</td></tr><tr><td>Total</td><td>8949.88</td><td>8961.856</td><td>9827.496</td><td>8723.86</td><td>9059.916</td><td>8470.568</td><td>9181.231</td><td>9582.95</td><td>9997.187</td></tr><tr><td rowspan="4">8 × 1</td><td>Comm. Delay</td><td>5708.63</td><td>5449.14</td><td>5997.96</td><td>5710.68</td><td>5993.208</td><td>5453.1</td><td>5991.732</td><td>6446.988</td><td>6825.6</td></tr><tr><td>Switching Delay</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Comp. Delay</td><td>6375.78</td><td>6599.514</td><td>7264.196</td><td>6072.644</td><td>6255.603</td><td>5957.948</td><td>6425.111</td><td>6713.345</td><td>6901.44</td></tr><tr><td>Total</td><td>12084.4</td><td>12048.65</td><td>13262.16</td><td>11783.32</td><td>12248.81</td><td>11411.05</td><td>12416.84</td><td>13160.33</td><td>13727.04</td></tr></table>

## 6. Conclusion

Allocation of scarce resources to competing agents by a manager is a ubiquitous decision problem. In making this allocation, the manager has to consider the partial preference profiles of the agents by polling them for information so that he can make a socially optimal allocation. The type of polling policy employed for information acquisition is crucial in determining how effectively and economically this information can be acquired and an optimal decision can be made.

Resource allocation methods have been studied in prior literature (Mathur and Solw 1994), but have typically ignored the process and costs of information acquisition and the existence of incomplete information. In contrast, this paper has contributed as follows: It has developed a method to incorporate information systems in the decision making process thus allowing the study of alternative IS structures and the nature of information flows. It has evaluated different policies of information acquisition, in terms of costs of both information acquisition and information processing. Depending on the cost structure, it has shown how a manager can efficiently make optimal allocations with incomplete information.

The empirical evidence that the use of uniform probability distributions results in the same patterns as the actual probability distributions would have an impact on managerial decision making. It would allow managers to evaluate and utilize decision making and information acquisition policies even without knowledge of actual probability distributions. $^{2}$

$^{2}$ The author would like to thank the Editor and AE for their encouragement, the referees for their critical comments, and the participants at the ICOQM conference, Jaipur, India. This paper has been funded by NSF under grant #IRI 955790.

## References

Arrow, K. and L. Hurwicz (Eds.), Studies in Resource Allocation Processes, Cambridge University Press, New York, 1977.

Balakrishnan, A. and A. B Whinston, "Information Issues in Model Specification," Information Systems Res., 2, 4 (1991), 263–286.

Barros, O., "Modeling and Evaluation of Alternative Information Systems Structures," Proc. 9th International Conf. on Information Systems, ICIS, Minneapolis, MN, 1988.

Bertsekas, D. P. and J. N. Isitsiklis, Parallel and Distributed Computation: Numerical Methods, Prentice Hall, Englewood Cliffs, NJ, 1989.

Conlisk, J., "Optimization Cost," J. Economics Behavior and Organization, 9 (1988), 213–228.

De, P., V. S. Jacob, and R. Pakath, "A Formal Approach for Designing Distributed Expert Problem Solving Systems," Information Systems Res., 4, 2 (1993).

Fitzgerald, J., Business Data Communications: Basic Concepts, Security, and Design, 4th ed., John Wiley & Sons, New York, 1993.

Hurwicz, L., "Incentive Aspects of Decentralization," in K. A. Arrow and M. D. Intrilligator (Eds.), Handbook of Mathematical Economics, Vol. III, Elsevier Science Publishers, North-Holland, Amsterdam, 1986.

— and T. Marschak, "Discrete Allocation Mechanisms: Dimensional Requirements When Desired Outcomes are Unbounded," J. Complexity, 1 (1985), 264–303.

Kaparthi, S. and H. R. Rao, "Higher Dimensional Restricted Lattice Paths with Diagonal Steps," Discrete Appl. Math., 31 (1991), 279-289.

Kurose, J. F. and R. Simha, "A Microeconomic Approach to Optimal Resource Allocation in Distributed Computer Systems," IEEE Trans. on Computers, 38, 5 (1989).

Marschak, J., and R. Radner, Economic Theory of Teams, Yale University Press, New Haven, CT, 1972.

Marschak, T., "Organizational Design," in K. A. Arrow and M. D. Intrilligator (Eds.), Handbook of Mathematical Economics, Vol. III, Elsevier Science Publishers, North-Holland, Amsterdam, 1986.

Martelli, A. and U. Montanari, "Additive And/Or Graphs," Proc. JCAI-73, Somerset, NJ, 1973.

Mathur, K. and D. Solow, Management Science: The Art of Decision Making, Prentice Hall, Englewood Cliffs, NJ, 1994.

Mookerjee, V. S. and B. L. DosSantos, "Inductive Expert System Design: Maximizing System Value," Information Systems Res., 4, 2 (1993).

Moore, J. C., H. Raghav Rao, and A. B. Whinston, "Information Processing for a Finite Resource Allocation Mechanism," forthcoming in Economic Theory.

—, —, and —, "Multi-agent Resource Allocation: An Incomplete Information Perspective," IEEE Trans. on Systems, Man and Cybernetics, 24, 8 (August 1994).

— and A. B. Whinston, "A Model of Decision-Making with Sequential Information Acquisition," Decision Support Systems, (1986).

Nilsson, N. J., Principles of Artificial Intelligence, Morgan Kaufmann, Palo Alto, CA, 1980.

Preckel, P. V., A. Yang, and H. Moskowitz, "Decision Analysis with Incomplete Utility and Probability Information," Oper. Res., 41, 5 (1993), 864–879.

Rao, H. R., "A Decision Theoretic Perspective of Multiple Agent Problem Solving: Application to a Resource Allocation Problem," Ph.D. Thesis, Purdue University, West Lafayette, IN, 1987.

——, J. C. Moore, K. Nam, T. S. Raghu, and A. B. Whinston, "A Comparison of Three Information Gathering Strategies in DAI Systems Under Noisy Conditions," Expert Systems with Applications, forthcoming.

Russel, S. J. and E. Wefald, Do the Right Thing: Studies in Limited Rationality, MIT Press, Cambridge, MA, 1991.

Samuelson, P., The Foundations of Economic Analysis, Harvard University Press, Cambridge, MA, 1983.

Srinivasan, M. M. and D. Gupta, "When Should a Roving Server Be Patient," Management Sci., 42, 3 (1996), 437–451.

Stevens, W. R., TCP/IP Illustrated Vol. 1: The Protocols, Addison-Wesley, Reading, MA, 1994.

Stone, H. S. and S. H. Bokhari, "Control of Distributed Processes," IEEE Computer, July (1978), 97–106.

Traub, J. F., G. W. Wasilkowski, and H. Wozniakowski, Information, Uncertainty, Complexity, Addison-Wesley, Reading, MA, 1983.

Weber, M., "Decision Making with Incomplete Information," European J. Oper. Res., 28 (1987), 44–57.

Weinrib, A. and G. Gopal, "Decentralized Resource Allocation for Distributed Systems," Proc. IEEE Infocom, 1987, 328–336.

Michael J. Shaw, Associate Editor. This paper was received on July 6, 1995, and has been with the authors 6 months for 1 revision.
