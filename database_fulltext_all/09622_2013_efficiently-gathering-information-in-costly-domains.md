---
otero_id: 9622
otero_key: "F8DYWR6B"
title: "Efficiently gathering information in costly domains"
authors: "Shulamit Reches; Ya'akov (Kobi) Gal; Sarit Kraus"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.021"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ef<sup>fi</sup>ciently gathering information in costly domains

Shulamit Reches <sup>a</sup>, Ya'akov (Kobi) Gal <sup>b,</sup>⁎, Sarit Kraus <sup>c</sup>

<sup>a</sup> Department of Applied Mathematics, Jerusalem College of Technology, Israel

<sup>b</sup> Department of Information Systems Engineering, Ben-Gurion University of the Negev, Israel

<sup>c</sup> Computer Science Department, Bar Ilan University, Israel

## a r t i c l e i n f o

Article history: Received 17 March 2012 Received in revised form 20 December 2012 Accepted 25 January 2013 Available online 15 February 2013

Keywords: Incomplete information Arti<sup>fi</sup>cial intelligence Empirical analysis Value of information

## a b s t r a c t

This paper proposes a novel technique for allocating information gathering actions in settings where agents need to choose among several alternatives, each of which provides a stochastic outcome to the agent. Samples of these outcomes are available to agents prior to making decisions and obtaining further samples is associated with a cost. The paper formalizes the task of choosing the optimal sequence of information gathering actions in such settings and establishes it to be NP-Hard. It suggests a novel estimation technique for the optimal number of samples to obtain for each of the alternatives. The approach takes into account the trade-offs associated with using prior samples to choose the best alternative and paying to obtain additional samples. This technique is evaluated empirically in several different settings using real data. Results show that our approach was able to signi<sup>fi</sup>cantly outperform alternative algorithms from the literature for allocating information gathering actions in similar types of settings. These results demonstrate the ef<sup>fi</sup>cacy of our approach as an ef<sup>fi</sup>cient, tractable technique for deciding how to acquire information when agents make decisions under uncertain conditions.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In many settings characterized by uncertainty, agents can engage in information gathering actions before making decisions. For example, consider an e-commerce application in which a buyer needs to choose between several suppliers of a product or service (in the absence of a built-in reputation system). The buyer does not know the quality of each of the suppliers in advance, but can spend time and resources to collect information about them. This information provides a “noisy signal” about the quality of the suppliers. An example of another setting—which comprises part of our empirical methodology—involves choosing one of several heuristic algorithms for solving an optimization problem. Each algorithm yields a solution that varies in computation time when applied to the problem. The agent needs to decide in advance which algorithm to choose in order to minimize the amount of expected computation time.

The focus of this paper is on settings where an agent needs to choose an alternative among a set of candidates with unknown outcomes. The agent can obtain samples of information about the different alternative candidates at a cost, prior to choosing one of them.

A key facet of the settings we consider is that the agent needs to decide in advance about the amount of information to acquire about each alternative and cannot change this decision once it has chosen one of the candidates. This constraint occurs in many real-world scenarios, such as choosing the number of credit ratings to purchase about a customer before approving a requested loan, or the amount of time to spend obtaining information from referees about a potential job candidate. To succeed in such settings, it is necessary to reason about the trade-off between paying to acquire additional information about the alternative candidates and choosing the candidate that is deemed optimal based on the current available information.

The paper formalizes the task of information gathering under uncertainty as a stochastic optimization problem termed Optimal Allocation of Relevant Information (OARI) with the following characteristics: An agent must choose in advance how much information to obtain about each of a set of possible candidates prior to choosing one of them. Each of these candidates is associated with a reward sampled from a distribution that is not known to the agent. The agent is given a number of prior samples about each candidate that are drawn from its respective distribution. Obtaining additional information about each candidate provides an additional sample of its reward but is associated with a cost. The goal of the agent is to <sup>fi</sup>nd the allocation of information gathering actions among the different alternatives that maximize the agent's total reward while taking into account the cost of obtaining the additional information and the expected reward that is associated with the chosen alternative.

The paper establishes OARI to be an NP-Hard problem and presents a novel estimation technique for solving it called EURIKA (Estimating the Utility of Restricted Information among K Alternatives). EURIKA estimates the agent's utility function by approximating the probability that it will prefer each of the candidates to all other candidates given the acquired information. It derives the optimal number of information gathering actions in polynomial time. EUREKA assumes the existence of a probability distribution over the possible alternatives, but makes no other assumptions about the domain.

The applicability of EURIKA was shown empirically by using it to make decisions on real-world data. Speci<sup>fi</sup>cally, we evaluated EURIKA on a variety of settings that varied the type of task to optimize, the data obtained from the information gathering actions, and agents' utility functions. One of the settings required the agent to choose between various heuristic algorithms for solving 3-SAT problems while optimizing the number of problems solved and the amount of computation time. The candidate algorithms included existing 3-SAT approaches from the literature as well as the best-performing entries submitted by researchers to a SAT solver competition. Another setting involved choosing the best lecturer in order to maximize students' enrollment in a course, given that students' evaluations about lecturers can be obtained at a cost. The data for this domain was taken from real course enrollment data and evaluations submitted by college students.

In all of these domains, the performance of an agent using EURIKA was compared to alternative solutions from the literature as well as a baseline approach that never purchased any additional information. The results show that the agent using EURIKA was able to outperform both of these approaches in all of the domains. In particular, it was able to <sup>fi</sup>nd the best alternative more often than the alternative approaches, and more ef<sup>fi</sup>ciently, in that it acquired less or equal amounts of information to <sup>fi</sup>nd the best alternative.

This paper revises and extends earlier work [17] and makes the following contributions. First, it formally de<sup>fi</sup>nes the problem of optimal allocation of information gathering actions (OARI) and establishes it to be an NP-Hard problem.

Second, it presents a novel heuristic for solving the OARI problem analytically by computing the estimated bene<sup>fi</sup>t for different information gathering actions while taking into account their associated costs. Third, it proves the ef<sup>fi</sup>cacy of the technique empirically by applying it to several domains that include real-world data.

## 2. Related work

The OARI problem is related to several approaches for repeated decision-making under imperfect information. Azoulay-Schwartz and Kraus [1] suggested a theoretical approach for optimizing the amount of information that is required in order to decide between two alternatives. A naive application of this model for multiple alternatives requires the examination of all possible alternative pairs, which is infeasible for large settings, such as the ones considered in this paper. Our work extends their model to choosing the best out of multiple (more than two) alternatives using a tractable, analytical approach, and evaluates the model using real data. Talman et al. [19] presented a model which decides the amount of information the agent should obtain based on a set of prior samples of each alternative. This technique used a <sup>fi</sup>xed number of samples to distribute among the various alternatives in a way that is proportional to the quality of the prior samples. Our empirical work shows that EURIKA signi<sup>fi</sup>cantly outperforms the FNE model in all domains we considered.

In the Max K-Armed Bandit problem, an agent allocates trials to slot machines, each yielding a payoff from a <sup>fi</sup>xed (but unknown) distribution [5,18]. The objective is to allocate trials among the K arms to maximize the expected best single sample reward.<sup>1</sup> This problem is analogous to the OARI problem in that each trial provides an information sample about one of the alternatives. However, we do not assume that the number of trials is determined in advance, but optimize this number given the uncertainty over the different alternatives.

Second, in contrast to the K-Armed Bandit problem, we allow the agent to have prior knowledge about each alternative. As we show in the empirical section, this knowledge may lead the agent to decide not to allocate additional trials because they are not expected to change its choice.

Our work relates to the value of information problem which has received much attention in the arti<sup>fi</sup>cial intelligence literature [4,10,16]. Within this body of work, there are several approaches that are relevant to our study. Guestrin and Krause [9,11,12] suggest several models for selecting which variables to sample in a Bayesian network to minimize uncertainty in the network. Bilgic and Getoor [3] use graphical models to minimize the cost of the acquisition of information for the purpose of making predictions about variables of interest to the agent.

Heckerman et al. [10] provide an approximation algorithm for computing the next piece of evidence to choose to observe given the results of all possible samples of the variables. They provide an approximate algorithm that is limited to speci<sup>fi</sup>c classes of dependencies between variables, and the agent makes a binary decision whether to sample each variable. In contrast, this paper is concerned with cases in which alternatives are independent of each other and an agent can decide how may information samples to purchase about each alternative, rather than once. Such settings characterize many real world information gathering problems, as we demonstrate in the Empirical Methodology section.

Our work differs from sequential models that choose which information source to query after each decision based on the information that was observed so far. Notable examples of these works include Grass and Zilberstein [8], who proposed a decision theoretic approach for planning and executing information-gathering actions over time, and Madani et al. [13], who presented a model in which a learner has to identify which of a given set of possible classi<sup>fi</sup>ers has the highest expected accuracy. In contrast to our work, both of these works assume that obtaining the value of the various alternatives is not associated with a cost. Thus, they don't consider the trade-off that arises when deciding to acquire new information or to make a choice based on the available information. Tseng and Gmytrasiewicz [21] developed an information-gathering system that suggests to a user how to best retrieve information related to the user's decisions. Madigan and Almond [14] propose a myopic model of value of information that samples variables iteratively. All of these techniques do not reason about the effect of choosing one information source over another on an agent's utility. In our setting, the agent chooses the amount of information to acquire in advance, and cannot choose a different candidate once it has made its decisions.

Our work is further distinct in that we evaluate our approach empirically, showing that it generalizes to several domains.

Lastly, Conitzer and Sandholm [6] formalized several “metareasoning” problems in which agents collect information prior to making decisions. One of these problems involves an agent that optimizes which set of anytime algorithms to use for different problem instances. The OARI problem is distinct from this problem in that the allocation of information is measured in integer numbers (i.e., units of information) rather than real values (i.e., time). We show that the OARI problem is at least as hard as this problem. In addition, we provide a tractable solution algorithm for solving the OARI problem in practice and demonstrate the ef<sup>fi</sup>cacy of the algorithm on real data.

## 3. An optimal allocation of information problem

We de<sup>fi</sup>ne the problem of optimally allocating information gathering actions as follows: A risk neutral agent has to choose an alternative from a set of K independent alternatives denoted $A = \{ a _ { 1 } , . . . , a _ { K } \}$ The reward for each alternative $a _ { i } ,$ denoted $R _ { i } ,$ is normally distributed $R _ { i } { \sim } N ( \mu _ { i } , \sigma _ { i } ^ { 2 } )$ ), with an unknown mean $\mu _ { i }$ and variance $\sigma _ { i } ^ { 2 }$ . The mean of the reward $\mu _ { i }$ is normally distributed $\mu _ { i } { \sim } N ( \zeta , \tau )$ for each $i { \in } \{ 1 , . . . . , K \}$ with known mean $\zeta$ and standard deviation τ. A sample $r _ { i }$ is a set of n ≥0 draws of the reward $R _ { i \cdot }$ The average of each sample $r _ { i }$ is denoted as ${ \overline { { r } } } _ { i \cdot }$

We assume that an agent has collected prior information about the alternatives consisting of samples $D = \{ ( \boldsymbol { r } _ { 1 } , \boldsymbol { n } _ { 1 } ) , . . . , ( \boldsymbol { r } _ { k } , \boldsymbol { n } _ { k } ) \}$ . The agent can decide to obtain an additional sample $r _ { i } ^ { \prime }$ consisting of $n _ { i } ^ { \prime }$ draws of the reward associated with alternative $a _ { i \cdot }$ The additional samples are denoted as $\boldsymbol { D } ^ { \prime } = \{ ( \boldsymbol { r } _ { 1 } ^ { \prime } , \boldsymbol { n } _ { 1 } ^ { \prime } ) , . . . , ( \boldsymbol { r } _ { k } ^ { \prime } , \boldsymbol { n } _ { k } ^ { \prime } ) \}$

<sup>¼</sup>Obtaining this information is associated with a cost and the number of possible samples that the agent can obtain is bounded by an integer $M { > } 0 ,$ , such that $\textstyle \cdot \sum _ { i = 1 } ^ { K } n _ { i } ^ { \prime } \leq M .$ . The goal of the agent is to <sup>fi</sup>nd the optimal <sup>¼</sup>allocation of samples for maximizing its reward given its chosen alternative and the information cost. Table 1 presents the notations we use for the description of the model.

The benefit to the agent is the difference between its utility from acquiring additional samples $D ^ { \prime } ,$ , and solely using its prior information $D . ^ { 2 }$

We denote the bene<sup>fi</sup>t as a function $B ( A , D , n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } , \zeta , \tau , \sigma _ { 1 } , . . . , \sigma _ { K } )$ that inputs a set of alternatives A, the distribution parameters $\zeta , \tau , \sigma _ { i }$ for $1 \leq i \leq K ,$ the prior information D about each alternative and the allocation $n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime }$ of the additional information units about each alternative $a _ { i } \in A .$ The function returns the bene<sup>fi</sup>t from this allocation. For the remainder of this paper, we will use an abbreviated notation, $B ( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } )$

The function Cost $: A \to R$ denotes the cost of obtaining one unit of information about alternative $a _ { i } \in A .$ . The total profit to the agent is the difference between the bene<sup>fi</sup>t from obtaining the additional information and its cost.

This pro<sup>fi</sup>t is a function $T ( A , D , n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } , \zeta , \tau , \sigma _ { 1 } , . . . , \sigma _ { K } , C o s t )$ which receives a set of alternatives A, the prior information D about each alternative, the distribution parameters $\zeta , \tau , \sigma _ { i }$ for $1 \leq i \leq K ,$ the Cost function and an allocation $n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime }$ of the additional information units about each alternative $a _ { i } \in A .$ It computes the total pro<sup>fi</sup>t to the agent from obtaining $\left( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } \right)$ additional information units, while taking the costs into consideration. For the remainder of this paper we will use the abbreviated notation $T ( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } )$ to denote this function.

$$
T \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = B \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \cdot \operatorname{Cost} \left(a _ {i}\right)\tag{1}
$$

We can now formally de<sup>fi</sup>ne the Optimal Allocation of Request Information (OARI) problem as follows:

## De<sup>fi</sup>nition 1. Optimal Allocation of Request Information (OARI).

Given a set of alternatives A, prior information D, the parameters $\zeta ,$ $\tau , \sigma _ { i }$ for each alternative $1 \leq i \leq K ,$ the bound on the number of information units $M ,$ and the Cost function. The OARI problem requires the <sup>fi</sup>nding of a vector $( n _ { 1 } ^ { * } , . . . , n _ { K } ^ { * } ) \in N ^ { K } , \ \sum _ { i = 1 } ^ { K } n _ { i } ^ { * } \le \bar { M }$ that maximizes the total pro<sup>fi</sup>t $T ( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } )$ of the agent.

This problem can be formulated as a decision problem as follows: Given a set of alternatives A, prior information $D ,$ the parameters $\zeta , \tau ,$ $\sigma _ { i }$ for each alternative $1 \leq i \leq K ,$ a bound on the number of information units M, and a threshold L as follows: Answer “yes” if there exists a vector $( n _ { 1 } ^ { * } . . . , n _ { K } ^ { * } ) , \sum _ { i = 1 } ^ { K } n _ { K } ^ { * } { \le } M$ such that $T ( n _ { 1 } ^ { * } , . . . , n _ { K } ^ { * } ) { \geq } L$

## Theorem 1. OARI is an NP-hard problem.

The proof of this theorem, via a reduction from the Knapsack problem [7], is given in Appendix A.

## 3.1. The EURIKA model

This section presents a model for solving the OARI problem, termed EURIKA (Estimating Utility of Restricted Information among K Alternatives). The model reasons about the trade-off between exploration and exploitation when choosing among multiple alternatives. It outputs the allocation of information gathering actions among the different alternatives, taking into account the prior sample of the rewards, the additional information that is obtained, and the cost of obtaining this information.

Summary of notations used in the paper.

<table><tr><td>Parameter</td><td>Description</td></tr><tr><td> $A = \{a_1, ..., a_K\}$ </td><td>Set  $A$  is a set of the  $K$  alternatives</td></tr><tr><td> $n_i$ </td><td>The number of prior units of information about alternative  $a_i$ </td></tr><tr><td> $R_i$ </td><td>Unknown reward of alternative  $a_i$ </td></tr><tr><td> $\overline{r}_i$ </td><td>The mean reward of  $n_i$  prior information units about alternative  $a_i$ </td></tr><tr><td> $n'_i$ </td><td>The number of units of information acquired about alternative  $a_i$ </td></tr><tr><td> $\overline{r'_i}$ </td><td>The mean reward of  $n'_i$  information units about  $a_i$ </td></tr><tr><td> $\mu_i$ </td><td>The mean of the reward of alternative  $a_i$ </td></tr><tr><td> $\sigma_i$ </td><td>The standard deviation of the reward of alternative  $a_i$ </td></tr><tr><td> $\zeta$ </td><td>The mean of the random variable  $\mu_i$ </td></tr><tr><td> $\tau$ </td><td>The variance of the random variable  $\mu_i$ </td></tr><tr><td> $Cost(a_i)$ </td><td>The cost of one unit of information about alternative  $a_i$ </td></tr><tr><td> $D = \{(\overline{r}_1, n_1), ..., (\overline{r}_k, n_K)\}$ </td><td>Prior information about alternatives in  $A$ </td></tr><tr><td> $D' = \left\{(\overline{r'_i}, n'_1), ..., (\overline{r'_k}, n'_K)\right\}$ </td><td>Additional information that is acquired about alternatives in  $A$ </td></tr></table>

The agent chooses its default alternative based solely on its prior information. Acquiring additional information about any of the alternatives is worthwhile to the agent only if it leads the agent to change its choice. Suppose the agent has already collected $n _ { i } ^ { \prime }$ units of information about a and that the mean reward associated with this sample, denoted as $\overline { { r } } _ { i } ,$ is known (we will drop this assumption later). Now, how should the agent make a decision about whether it prefers alternative $a _ { i }$ to $a _ { j } ?$ If the agent only considers the available information, its decision solely depends on the probability that the weighted mean reward of the information obtained about $a _ { i }$ is greater than that of the information obtained about $a _ { j } .$ In addition, the agent may also consider prior information about the distribution of these rewards. The following de<sup>fi</sup>nes the probability that the agent will prefer alternative a over any alternative $a _ { j }$ after obtaining $n _ { j } ^ { ' }$ information units about $a _ { j } .$

De<sup>fi</sup>nition 2. The term $P C _ { i } \Big ( n _ { j } ^ { \prime } \Big | { n _ { i } ^ { \prime } , \bar { r } _ { i } ^ { \prime } } \Big )$ is the probability that the agent will prefer alternative $a _ { i }$ <sup></sup>to alternative a as a result of $n _ { i } ^ { \prime }$ and n<sup>′</sup> additional information units about $a _ { i }$ and $a _ { j } ,$ given the sample $r _ { i \cdot } ^ { \prime \ 3 }$

Next, we will de<sup>fi</sup>ne the probability that a is the best alternative, that is, the agent chooses alternative a over all other alternatives as a result of obtaining additional information units on the other alternatives.

De<sup>fi</sup>nition 3. The term $P B _ { i } \Big ( n _ { 1 } ^ { \prime } , . . . , n _ { i - 1 } ^ { \prime } , n _ { i + 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } \Big | n _ { i } ^ { \prime } , \overline { { { r _ { i } ^ { \prime } } } } \Big )$ is the proba-<sup>þ </sup>bility that the agent will prefer alternative a to all other alternatives as a result of obtaining $\left( n _ { 1 } ^ { \prime } , . . . , n _ { i - 1 } ^ { \prime } , n _ { i + 1 } ^ { \prime } , . . . , n _ { K } ^ { ' } \right)$ additional information $\mathrm { \ u n i t s . } ^ { 4 }$

The following proposition states that the probability $P B _ { i } ( n _ { 1 } ^ { ' } , . . . , n _ { i - 1 } ^ { ' }$ $n _ { i + 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } \vert n _ { i } ^ { \prime } , \overline { { r _ { i } ^ { \prime } } } )$ can be computed as the product of the probabilities that the agent prefers $a _ { i }$ to each other alternative a given the sample $r _ { i \cdot } ^ { \prime }$

## Proposition 1.

$$
P B _ {i} \left(n _ {1} ^ {\prime}, \dots , n _ {i - 1} ^ {\prime}, n _ {i + 1} ^ {\prime}, \dots , n _ {K} ^ {\prime} \mid n _ {i} ^ {\prime}, \overline {{r}} _ {i} ^ {\prime}\right) = \prod_ {j \neq i} P C _ {i} \left(n _ {j} ^ {\prime} \mid n _ {i} ^ {\prime}, \overline {{r}} _ {i} ^ {\prime}\right).\tag{2}
$$

The proof is immediate, as the probability that the agent prefers $a _ { i }$ to any alternative $a _ { j }$ is independent of $a _ { i }$ when the sample mean $\overline { { a _ { i } } }$ is known. Now, because the true mean sample reward $\overline { { r _ { i } ^ { \prime } } }$ is unknown, we sum over each of its possible values, and obtain the term $P B _ { i } \left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ , which is the probability that the alternative $a _ { i }$ is preferred to all other alternatives.

$$
\begin{array}{l} P B _ {i} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \\ = \int_ {\overline {{r}} _ {i}} \prod_ {j \neq i} P B _ {i} \left(n _ {1} ^ {\prime}, \dots , n _ {i - 1} ^ {\prime}, n _ {i + 1} ^ {\prime}, \dots , n _ {K} ^ {\prime} \mid n _ {i} ^ {\prime}, \overline {{r}} _ {i} ^ {\prime}\right) \cdot P \left(\overline {{r}} _ {i} ^ {\prime}\right) d \overline {{r}} _ {i} ^ {\prime} \end{array}\tag{3}
$$

Here, the term $P \Big ( \overline { { r _ { i } ^ { \prime } } } \Big )$ is the probability that the mean reward from obtaining $n _ { \mathrm { ~ i ~ } } ^ { ' }$ units of information of alternative $a _ { i }$ is $\overline { { r } } _ { i }$ .

## 3.2. Computing the expected benefit of acquiring information

In this section, we show how to compute the bene<sup>fi</sup>t $B ( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } )$ from obtaining the sample $\left( \boldsymbol { n } _ { 1 } ^ { \prime } , . . . , \boldsymbol { n } _ { K } ^ { \prime } \right)$ . Without loss of generality, suppose alternative $a _ { 1 }$ is currently the best alternative given the prior information D.

We distinguish between the following two cases:

1. The agent does not obtain additional information. The expected reward in this case is the mean reward $\mu _ { 1 }$ of the current best alternative $a _ { 1 } .$

2. The agent decides to obtain $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ additional information units about alternatives $a _ { 1 } , \ldots , a _ { k } .$ In this case there are two possibilities:

• The agent decides not to change its initial decision $a _ { 1 }$ based on the $\left( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } \right)$ additional information. The expected reward in this case is $P B _ { 1 } ( n _ {   1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } ) { \cdot } \mu _ { 1 }$

• The agent prefers some alternative $a _ { i } ,$ i 1 to $a _ { 1 }$ based on the $\left( \boldsymbol { n } _ { 1 } ^ { \prime } , . . . , \boldsymbol { n } _ { K } ^ { \prime } \right)$ additional information. The expected reward in this case is $\begin{array} { r } { \sum _ { i = 2 } ^ { K } P B _ { i } \big ( \boldsymbol n ^ { ' } _ { 1 } , . . . , \boldsymbol n ^ { ' } _ { K } \big ) { \cdot } \boldsymbol \mu _ { i } . } \end{array}$

We can now compute the bene<sup>fi</sup>t from obtaining $\left( \boldsymbol { n } _ { 1 } ^ { \prime } , . . . , \boldsymbol { n } _ { K } ^ { \prime } \right)$ additional samples as the difference between the expected reward from obtaining and not obtaining this information. This bene<sup>fi</sup>t is denoted as $B ( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } | \mu _ { 1 } , . . . , \mu _ { K } )$ and computed as

$$
B \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime} \mid \mu_ {1}, \dots , \mu_ {K}\right) = P B _ {1} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \mu_ {1} + \sum_ {i = 2} ^ {K} P B _ {i} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \mu_ {i} - \mu_ {1}.\tag{4}
$$

Because we have that

$$
P B _ {1} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = 1 - \sum_ {i = 2} ^ {k} P B _ {i} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right)\tag{5}
$$

we can write the expected pro<sup>fi</sup>t as

$$
B (n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime} | \mu_ {1}, \dots , \mu_ {K}) = \sum_ {i = 2} ^ {K} P B _ {i} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot (\mu_ {i} - \mu_ {1}).\tag{6}
$$

The above equation depends on the reward means $\{ \mu _ { 1 } , . . . , \mu _ { K } \}$ which are unknown. Therefore we need to integrate over their possible values. We use the posterior distribution $P ( \mu _ { i } | D , D ^ { \prime } )$ to combine the prior information D, the acquired samples $D ^ { \prime } ,$ , and the parameters $\zeta , \tau , \sigma _ { 1 } , . . . , \sigma _ { K }$ . The posterior distribution over μ can be computed in closed form. Because μ is a conjugate prior to the normal distribution, its posterior is a normal distribution with mean $\frac { \sigma _ { i } ^ { 2 } \zeta + n _ { i } \tau ^ { 2 } \overline { { r } } _ { i } } { \sigma _ { i } ^ { 2 } + n _ { i } \tau ^ { 2 } }$ and variance $\frac { \sigma _ { i } ^ { 2 } \tau ^ { 2 } } { \sigma _ { i } ^ { 2 } + n _ { i } \tau ^ { 2 } } .$ Considering all possible values of $\mu _ { i } ,$ we attain the

Proposition 2.

$$
\begin{array}{c} B \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) = \int_ {\mu_ {1}}... \int_ {\mu_ {K}} \sum_ {i = 2} ^ {K} P B _ {i} \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) \cdot (\mu_ {i} - \mu_ {1}) \cdot \\ \prod_ {i = 1} ^ {K} P r \Big (\mu_ {i} \Big | D, D ^ {'} \Big) d \mu_ {1}... d \mu_ {K}. \end{array}\tag{7}
$$

The agent's expected bene<sup>fi</sup>t gained from obtaining $\left( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } \right)$ additional units of information, while considering the various costs involved in obtaining $\textstyle \sum _ { i = 1 } ^ { K } n _ { i } ^ { ' }$ units of information is described in <sup>¼</sup>Eq. (1), which we restate here for convenience.

$$
T \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = B \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \cdot \operatorname{Cost} \left(a _ {i}\right)
$$

The solution to the OARI problem is a vector $( n _ { 1 } ^ { * } , . . . , n _ { K } ^ { * } )$ that maximizes the above function, such that $\textstyle \sum _ { 1 } ^ { K } n _ { i } ^ { * } < M$ . This computation is exponential in the number of possible alternatives to consider.<sup>5</sup> An alternative approach is to maximize the function analytically, using several approximations which we describe in the next section.

We assume that the agent bases its decision solely on its observations. These include the prior information and the acquired samples about the various alternatives. This means that for any two alternatives $a _ { i }$ and $a _ { j }$ and samples $\boldsymbol { r } _ { i } ^ { \prime }$ and $r _ { j } ^ { \prime } ,$ the agent prefers $a _ { i }$ over a if the following holds:

$$
\frac {n _ {i} \overline {{r}} _ {i} + n _ {i} ^ {\prime} \overline {{r ^ {\prime}}} _ {i}}{n _ {i} + n _ {i} ^ {\prime}} > \frac {n _ {j} \overline {{r}} _ {j} + n _ {j} ^ {\prime} \overline {{r ^ {\prime}}} _ {j}}{n _ {j} + n _ {j} ^ {\prime}}.\tag{8}
$$

The following proposition states that the probability that the agent changes its alternative can be computed using the normal distribution.

Proposition 3. Given $n _ { i } , n _ { j } , \bar { r } _ { i } , \bar { r } _ { j } , n _ { i } ^ { \prime } , n _ { j } ^ { \prime } , \sigma _ { i } , \sigma _ { j }$ and $\overline { { { r ^ { \prime } } } } _ { i }$ the value of $P C _ { i } \Big ( n _ { i } ^ { ' } , n _ { j } ^ { ' } , \overline { { r _ { i } ^ { \prime } } } \Big )$ , is as follows:

$$
P C \left(n _ {i} ^ {\prime}, n _ {j} ^ {\prime}, \overline {{r}} _ {i} ^ {\prime}\right) = P r \left(Z <   Z _ {\alpha} \left(n _ {i} ^ {\prime}, n _ {j} ^ {\prime}, \overline {{r}} _ {i} ^ {\prime}\right)\right).\tag{9}
$$

Here, Z is a random variable, with a standard normal distribution, $P r ( Z { < } Z _ { \alpha } ( n ^ { ' } { _ i } , n ^ { ' } { _ j } , r ^ { ' } { _ i } ) )$ is the probability that the random variable Z will have a value less than $Z _ { \alpha } ( n _ { i } ^ { \prime } , n _ { j } ^ { \prime } , r _ { i } ^ { \prime } )$ , and

$$
Z _ {\alpha} \left(n _ {i} ^ {\prime}, n _ {j} ^ {\prime}, \overline {{r}} _ {i} ^ {\prime}\right) = \frac {\sqrt {n _ {j}} \left(\left(n _ {j} + n _ {j} ^ {\prime}\right) \left(n _ {i} \bar {r} _ {i} + n _ {i} ^ {\prime} , r _ {i} ^ {\prime}\right) - \left(n _ {i} + n _ {i} ^ {\prime}\right) \left(n _ {j} \bar {r} _ {i} - \mu_ {j} , n _ {j} ^ {\prime}\right)\right)}{n _ {j} ^ {\prime} \left(n _ {i} + n _ {i} ^ {\prime}\right) \sigma_ {j}}
$$

The proof is in the Appendix A. Thus we can write

$$
P C _ {i} \left(n _ {j} ^ {\prime} \mid n _ {i} ^ {\prime}, \overline {{r}} _ {i} ^ {\prime}\right) = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {Z _ {\alpha} \left(n _ {i} ^ {\prime}, n _ {j} ^ {\prime}, r _ {i} ^ {\prime}\right)} e ^ {- \frac {t ^ {2}}{2}} d t.\tag{10}
$$

## 3.3. Approximations

In order to compute PC $\mathbf { \widetilde { \Gamma } } ( n _ { j } ^ { \prime } | n _ { i } ^ { \prime } , \overline { { r _ { i } ^ { \prime } } } )$ as a function of the parameters $n _ { i } ^ { \prime } , n _ { j } ^ { \prime }$ <sup></sup>we use the following approximation. The following proposition uses a summation of polynomials to compute the integration in Eq. (10).

Proposition 4. The function

$$
P _ {a p p r o x} (x) = \left\{ \begin{array}{l l} 0. 5 - \frac {1}{\sqrt {2 \pi}} \sum_ {k = 0} ^ {n} \frac {x ^ {2 k + 1} (- 1) ^ {k}}{2 ^ {k} (2 k + 1) k !} & | x | <   d \\ 0 & x \geq d \\ 1 & x \leq - d \end{array} \right.
$$

is an approximation of the function $F ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } }  _ { x } ^ { \infty } e ^ { \frac { - t ^ { 2 } } { 2 } }$ dt. Here, d is a positive integer that binds the error $R _ { n } { = } | F ( x ) ^ { \vee \underline { { { 2 \pi } } } } { \dot { P } } _ { - }$ \_approx(x)| as follows. $I f \left| x \right| < d ,$ then $R _ { n } { \leq } \frac { d ^ { n + 1 } } { ( n + 1 ) ! } .$ Otherwise, $R _ { n } { \leq } 0 . 5 { - } \frac { 1 } { \sqrt { 2 \pi } } \int _ { 0 } ^ { | d | } e ^ { \frac { - t ^ { 2 } } { 2 } } \mathrm { d } t .$

The proof is in Appendix A. According to Proposition $^ { 4 , }$ we can use $P _ { - }$ approx to approximate the density of a standard normal probability function $F ( x )$ within the bounds of |d| as a piecewise integrable function. The size of the approximation error depends on d and n. By Eq. (10), we get that $1 - F \big ( Z _ { \boldsymbol { \alpha } } \big ( \bar { n ^ { \prime } } _ { i } , \bar { n ^ { \prime } } _ { j } \big ) \big ) = P C _ { i } \Big ( \bar { n ^ { \prime } } _ { j } \Big | \bar { n ^ { \prime } } _ { i } , \overline { { r ^ { \prime } } } _ { i } \Big )$ . We use Proposition $^ { 4 , }$ where ${ \pmb x } = Z _ { \alpha } ( { \pmb n } _ { i } ^ { \prime } , { \pmb n } _ { j } ^ { \prime } , { \pmb r } _ { i } ^ { \prime } )$ , to approximate $P C _ { i } \Big ( n _ { j } ^ { ' } \Big | { n _ { i } ^ { ' } } , { \overline { { r _ { i } ^ { ' } } } } \Big )$

We now place $P C _ { i } \Big ( \boldsymbol { n } _ { j } ^ { \prime } \Big | \boldsymbol { n } _ { i } ^ { \prime } , \overline { { \boldsymbol { r } _ { i } ^ { \prime } } } \Big )$ in Eq. (2) to compute $P B _ { i } ( n _ { 1 } ^ { ' } , . . . ,$ $n _ { i - 1 } ^ { \prime } , n _ { i + 1 } ^ { \prime } , . . . , n _ { K } ^ { ' } \left| n _ { i } ^ { \prime } , \overline { { r _ { i } ^ { ' } } } \right.$ (the probability that $a _ { i }$ is the best alternative); place $P B _ { i } \Big ( n _ { 1 } ^ { ' } , . . . , n _ { i - 1 } ^ { ' } , n _ { i + 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \Big | n _ { i } ^ { ' } , \overline { { { r _ { i } ^ { ' } } } } \Big )$ in $\operatorname { E q . } \left( 7 \right)$ to compute B (the expected pro<sup>fi</sup>t), and place B in Eq. (1) to compute T (the expected bene<sup>fi</sup>t). Finally, we can <sup>fi</sup>nd the vector $\left( n _ { 1 } ^ { * } , . . . , n _ { K } ^ { * } \right)$ that maximizes T numerically using the simplex algorithm [15].

## 4. Experimental design and analysis

In this section, we provide an extensive evaluation of the EURIKA model in settings that include synthetic as well as ecologically realistic data. These settings differ in the way the samples determine how agents incur utilities or costs. Therefore, we adapted separate B and T functions for each of the settings.

Two of the domains involve choosing algorithms for solving 3-SAT formulas. The candidate algorithms consisted of heuristic approaches from the SAT literature as well as algorithms submitted by researchers to a competition for solving SAT formulas. A third domain involves choosing lecturers for courses from among different student evaluations. We describe each of the domains, and show how to adapt the OARI model to the domain. We then show how we use the EURIKA model to <sup>fi</sup>nd the optimal number of samples to obtain for each alternative. We compare the performance of the EURIKA model to several candidate models. Although the OARI formalism assumes that populations are normally distributed, our empirical results show that our approach can also be applied towards populations that may not adhere to this assumption.

## 4.1. The SAT simulation domain

In the SAT simulation domain, an agent is given a set of 3-SAT formulas to satisfy. Each alternative $a _ { i }$ represents a heuristic algorithm for solving 3-SAT formulas. Changing the assignment of an attribute in a formula, referred to as a “<sup>fl</sup>ip” operation, costs one unit of computation time. Each candidate algorithm $a _ { i }$ solves a 3-SAT formula using an expected number of $\mu _ { i }$ <sup>fl</sup>ip operations. In this domain, we use μ to refer to costs rather than rewards as originally formalized. A sample of n<sup>′</sup> applications of a generates $n _ { i } ^ { \prime } \mu _ { i }$ expected <sup>fl</sup>ips and solves n<sup>′</sup> 3-SAT formulas. There are two possible con<sup>fi</sup>gurations in this domain: in the <sup>fi</sup>rst, the agent must minimize the amount of computation time to solve a given set of formulas. In the second, the agent must maximize the number of formulas it solves for a <sup>fi</sup>xed amount of computation time.

## 4.1.1. Minimal time (MT) configuration

In this con<sup>fi</sup>guration, the objective is to solve N formulas using the least amount of computation time. Suppose that, without loss of generality, algorithm $a _ { 1 }$ is the best alternative given the prior information D. If the agent chooses this algorithm, the expected number of <sup>fl</sup>ip operations for solving N formulas is $N ^ { \cdot } \mu _ { 1 } .$ . Now, obtaining $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ information units of the various algorithms solves $\textstyle \sum _ { i = 1 } ^ { K } { n _ { i } ^ { ' } }$ 3-SAT formulas at an expected cost of $\textstyle \sum _ { i = 1 } ^ { K } n _ { i } ^ { ' } \mu _ { i }$ <sup>¼fl</sup>ip operations. Suppose the <sup>¼</sup>agent decides to obtain additional information. In this case there are two possibilities:

• The agent will choose to continue to use algorithm $a _ { 1 }$ to solve the remaining $\begin{array} { r } { \left( N - \sum _ { i = 1 } ^ { K } n _ { i } ^ { ' } \right) } \end{array}$ <sup>fl</sup>ip operations. In this case, the expected <sup>¼</sup>number of <sup>fl</sup>ip operations is

$$
P B _ {1} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {1}.
$$

• The agent will choose alternative $a _ { j } , j \neq 1$ to solve the remaining $\scriptstyle \left( N - \sum _ { i = 1 } ^ { K } n _ { i } ^ { ' } \right)$ <sup>fl</sup>ip operations. In this case, the expected number of <sup>fl</sup>ip operations is

$$
\sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {j}.
$$

The expected number of <sup>fl</sup>ip operations for obtaining $\left( \boldsymbol { n } _ { 1 } ^ { \prime } , . . . , \boldsymbol { n } _ { K } ^ { \prime } \right)$ information units, denoted $E F ( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } )$ sums over these two cases

$$
E F \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = \sum_ {j = 1} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {j}.\tag{11}
$$

The expected bene<sup>fi</sup>t for obtaining $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ information units is the difference between the expected number of <sup>fl</sup>ips before and after obtaining the additional information.

$$
B \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = (N \cdot \mu_ {1}) - E F \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right)\tag{12}
$$

The cost function in this domain assigns one unit of computation time to each <sup>fl</sup>ip operation. Therefore, the expected pro<sup>fi</sup>t for obtaining $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ information units, de<sup>fi</sup>ned in Eq. (1), is computed as

$$
\begin{array}{l}T \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = B \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \cdot \mu_ {i}\\= (N \cdot \mu_ {1}) - E F \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \cdot \mu_ {i}\\= (N \cdot \mu_ {1}) - \sum_ {j = 1} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {j} - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \cdot \mu_ {i}\\= (N \cdot \mu_ {1}) - \left( \right.P B _ {1} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {1} + \sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {j} - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \cdot m.\end{array}\tag {13}
$$

Since $\begin{array} { r } { P B _ { 1 } \left( n ^ { ' } _ { 1 } , . . . , n ^ { ' } _ { K } \right) = 1 - \sum _ { j = 2 } ^ { K } P B _ { j } \left( n ^ { ' } _ { 1 } , . . . , n ^ { ' } _ { K } \right) } \end{array}$ the above equation can be written as

$$
\begin{array}{l} T \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) = (N \cdot \mu_ {1}) - \left(\left(1 - \sum_ {j = 2} ^ {K} P B _ {j} \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {'}\right) \cdot \mu_ {1} \right. \right. \\ \quad \left. + \sum_ {j = 2} ^ {K} P B _ {j} \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {'}\right) \cdot \mu_ {j}\right) - \sum_ {i = 1} ^ {K} n _ {i} ^ {'}: \mu_ {i} \\ = - \sum_ {i = 1} ^ {K} n _ {i} ^ {'} \cdot (\mu_ {i} - \mu_ {1}) + \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {'}\right) \cdot \sum_ {j = 2} ^ {K} P B _ {j} \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) \cdot \Big (\mu_ {1} - \mu_ {j} \Big). \end{array}\tag{14}
$$

The OARI problem in this con<sup>fi</sup>guration is to <sup>fi</sup>nd the optimal allocation of heuristic algorithms $( n _ { 1 } ^ { * } , . . . , n _ { K } ^ { * } )$ that maximizes Eq. (14).

## 4.1.2. Maximal number of formulas (MF) configuration

In this con<sup>fi</sup>guration, the objective is to solve as many formulas as possible using T <sup>fl</sup>ips. We formulate the EURIKA problem for this setting as follows. Suppose that, without loss of generality, algorithm $a _ { 1 }$ is the best alternative given the prior information D. If the agent chooses this algorithm without obtaining additional samples, the expected number of formulas it would solve $\mathrm { i } s \frac { T } { \mu _ { 1 } } .$ As before, obtaining $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ information units of the various algorithms solves $\textstyle \sum _ { i = 1 } ^ { K } n _ { i } ^ { ' }$ 3-SAT formulas and performs $\textstyle \sum _ { i = 1 } ^ { K } n _ { i } ^ { ' } { \boldsymbol { \mu } } _ { i }$ expected <sup>fl</sup>ip operations. At this point, there are $\begin{array} { r } { T - \sum _ { i = 1 } ^ { K } n _ { i } \mu _ { i } } \end{array}$ <sup>¼fl</sup>ips remaining. If the agent decides to obtain this information, then there are two possibilities:

• The agent will choose to continue to use algorithm $a _ { 1 }$ with a probability of $P B _ { 1 } \left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ . In this case, the expected number of formulas solved is

$$
P B _ {1} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \frac {T - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \mu_ {i}}{\mu_ {1}}.
$$

• The agent will choose alternative $a _ { j } , j \neq 1$ to use for the remaining $\begin{array} { r } { T - \sum _ { i = 1 } ^ { \overline { { K } } } n _ { i } ^ { ' } \mu _ { i } } \end{array}$ <sup>fl</sup>ip operations. In this case, the expected number of <sup>¼</sup>formulas solved is

$$
\sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \frac {T - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \mu_ {i}}{\mu_ {j}}.
$$

The expected number of <sup>fl</sup>ip operations for obtaining $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ information units, denoted as $E N ( n ^ { ' } { } _ { 1 } , . . . , n ^ { ' } { } _ { K } )$ is the sum of these two cases:

$$
E N \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = \sum_ {j = 1} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \frac {T - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \mu_ {i}}{\mu_ {j}}.\tag{15}
$$

The expected bene<sup>fi</sup>t to the agent from obtaining $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ information units is the difference between the expected number of formulas solved after and before obtaining the additional information.

$$
B \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = E N \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) - \frac {T}{\mu_ {1}}\tag{16}
$$

The expected pro<sup>fi</sup>t to this cost con<sup>fi</sup>guration, given in Eq. (1) is computed as

$$
\begin{array}{l} T \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = B \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) + \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \\ \quad = E N \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) - \frac {T}{\mu_ {1}} + \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \\ \quad = \sum_ {j = 1} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \frac {T - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \mu_ {i}}{\mu_ {j}} - \frac {T}{\mu_ {1}} + \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \\ \quad = P B _ {1} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \frac {T - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \mu_ {i}}{\mu_ {1}} + \\ \quad \sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \frac {T - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \mu_ {i}}{\mu_ {j}} - \frac {T}{\mu_ {1}} + \sum_ {i = 1}^{K} n _ {i} ^ {\prime}. \end{array}\tag{17}
$$

Since $P B _ { 1 } \left( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } \right) = 1 - \textstyle \sum _ { j = 2 } ^ { K } P B _ { j } \left( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } \right)$ , the above equation equals to

$$
\begin{array}{l} T \left(n _ {1} ^ {\prime},..., n _ {K} ^ {\prime}\right) = \left(1 - \sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime},..., n _ {K} ^ {\prime}\right)\right) \cdot \frac {T - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \mu_ {i}}{\mu_ {1}} \\ \quad + \sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime},..., n _ {K} ^ {\prime}\right) \cdot \frac {T - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \mu_ {i}}{\mu_ {j}} - \frac {T}{\mu_ {1}} + \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \\ = \sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime},..., n _ {K} ^ {\prime}\right) \cdot \left(T - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \mu_ {i}\right) \cdot \left(\frac {1}{\mu_ {j}} - \frac {1}{\mu_ {1}}\right) \\ \quad + \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime} \cdot \left(1 - \frac {\mu_ {i}}{\mu_ {1}}\right). \end{array}\tag{18}
$$

The OARI problem in this con<sup>fi</sup>guration is to <sup>fi</sup>nd the optimal allocation of heuristic algorithms $\left( n _ { 1 } ^ { * } , . . . , n _ { K } ^ { * } \right)$ that maximizes Eq. (18).

## 4.2. The SAT competition domain

This domain uses real automatic 3-SAT solvers submitted to the Ninth International Conference on Theory and Applications of Satis<sup>fi</sup>ability Testing Conference.<sup>6</sup> Performance in the competition was based on a score that takes into account two factors:

• the number of instances solved within a given run-time limit;

• the total time needed to solve all instances.

We detail how to tailor the OARI problem for this domain. We set N to equal the total number of formulas in the competition. As before, $a _ { i }$ is a possible solution algorithm, and $n _ { i } ^ { ' }$ is the number of 3-SAT equations that are solved using algorithm $a _ { i \cdot }$ The mean score in the competition associated with algorithm a is represented as μ . Thus, obtaining $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ samples of the various algorithms solves $\textstyle \sum _ { i = 1 } ^ { K } n ^ { ' }$ <sub>i</sub> 3-SAT formulas and provides an expected score of $\textstyle \sum _ { i = 1 } ^ { K } \mu _ { i } \cdot n _ { i } ^ { ' }$ <sup>¼</sup>points. There are two possibilities.

• The agent will choose to continue to use algorithm $a _ { 1 }$ to solve the remaining $\begin{array} { r } { \left( N - \sum _ { i = 1 } ^ { K } n _ { i } ^ { ' } \right) } \end{array}$ formulas. In this case, the expected score is

$$
P B _ {1} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {1} ^ {\prime}\right) \mu_ {1}.
$$

• The agent will choose alternative $a _ { j } , j \neq 1$ to use for the remaining $\left( N - \breve { \sum } _ { i = 1 } ^ { K } n _ { i } ^ { ^ { \prime } } \right)$ formulas. In this case, the expected score is

$$
\sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \mu_ {j}.
$$

The expected score for obtaining $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ information units, denoted as $E S ( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } )$ sums over these two cases

$$
E S \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = \sum_ {j = 1} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {j}.\tag{19}
$$

The expected bene<sup>fi</sup>t for obtaining the sample $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ is the difference in score from obtaining and not obtaining the additional information.

$$
B \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = E S \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) - (N \cdot \mu_ {1})\tag{20}
$$

The expected pro<sup>fi</sup>t to this cost con<sup>fi</sup>guration, given in $\operatorname { E q . } \left( 1 \right)$ , is computed as

$$
\begin{array}{l} T \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) = B \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) + \sum_ {j = 1} ^ {K} n _ {i} ^ {\prime} \cdot \mu_ {i} \\ = \sum_ {j = 1} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {j} - (N \cdot \mu_ {1}) + \sum_ {j = 1} ^ {K} n _ {i} ^ {\prime}; \mu_ {i} \\ = P B _ {1} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {1} \\ + \sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {j} - (N \cdot \mu_ {1}) \\ + \sum_ {j = 1} ^ {K} n _ {i} ^ {\prime} \cdot \mu_ {i} = \left(1 - \sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right)\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {1} \\ + \sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 2} ^ {K} n _ {i} ^ {\prime}\right) \cdot \mu_ {j} - (N \cdot \mu_ {1}) + \sum_ {j = 1} ^ {K} n _ {i} ^ {\prime}; \mu_ {i} \\ = \sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \left(N - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}\right) \cdot (\mu_ {j} - \mu_ {1}) - \sum_ {i = 1} ^ {K} n _ {i} ^ {\prime}. \end{array}\tag{21}
$$

## 4.3. The professor evaluation domain

In this domain, the objective is to choose the lecturer with the highest enrollment potential of K possible lecturers. Each alternative a represents a sample from a database of student satisfaction scores. This domain includes real data from a survey <sup>fi</sup>lled out by students at the Jerusalem College of Technology. The enrollment potential for courses depends on the satisfaction rating associated with the lecturer. The agent can query the database, for a cost, about professors' satisfaction ratings. The agent's objective is to choose the lecturer with the highest enrollment potential while taking into account the cost of obtaining information about students' ratings.

We formulate the OARI problem for this setting. Every lecturer a is associated with a mean satisfaction score that is represented by μ . The pro<sup>fi</sup>t to the college is $\mu _ { i } \cdot \nu ,$ where v is a positive constant, representing the fact that popular lecturers are more likely to draw higher course enrollments, leading to higher pro<sup>fi</sup>ts. Suppose that, without loss of generality, the agent chooses lecturer $a _ { 1 }$ based on the prior information D. In this case, the expected bene<sup>fi</sup>t is $\mu _ { 1 } \cdot \nu .$ . Suppose that the agent has obtained $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ samples of the various lecturers. As before, there are two possibilities.

• The agent will continue to choose lecturer $a _ { 1 } .$ . In this case, the expected bene<sup>fi</sup>t is $P B _ { 1 } ( n _ { 1 } ^ { \prime } , . . . , n _ { K } ^ { \prime } ) { \cdot } \mu _ { 1 } { \cdot } \nu .$

• The agent will choose a different lecturer $a _ { j } , j \neq i$ with probability $P B _ { j } ( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } )$ . In this case, the expected bene<sup>fi</sup>t is

$$
\sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime},..., n _ {K} ^ {\prime}\right) \cdot \mu_ {j} \cdot v.
$$

The expected reward of the sample $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ is the sum of these two cases:

$$
\left(P B _ {1} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \mu_ {1} \cdot v\right) + \left(\sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \mu_ {j} \cdot v\right).\tag{22}
$$

Because

$$
P B _ {1} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \mu_ {1} \cdot v = \left(1 - \sum_ {j = 2} ^ {K} P B _ {j} \left(n _ {1} ^ {\prime}, \dots , n _ {K} ^ {\prime}\right) \cdot \mu_ {j}\right) \cdot v
$$

the expected bene<sup>fi</sup>t to the agent from obtaining the sample $\left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ can be written as

$$
\begin{array}{l} B \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) = \left(1 - \sum_ {j = 2} ^ {K} P B _ {j} \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big)\right) \cdot \mu_ {1} \cdot v \\ \qquad + \sum_ {j = 2} ^ {K} P B _ {j} \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) \cdot \mu_ {j} \cdot v - \mu_ {1} \cdot v \\ \qquad = \sum_ {j = 2} ^ {K} P B _ {j} \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) \cdot (\mu_ {i} - \mu_ {1}) \cdot v. \end{array}\tag{23}
$$

The cost function in this domain assigns c units to obtaining each satisfaction rating. Incorporating this cost, we obtain the following:

$$
\begin{array}{l} T \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) = B \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) - \sum_ {i = 1} ^ {K} n _ {i} ^ {'} \cdot c = \\ \sum_ {j = 2} ^ {K} P B _ {j} \Big (n _ {1} ^ {'},..., n _ {K} ^ {'} \Big) \cdot (\mu_ {i} - \mu_ {1}) \cdot v - \sum_ {i = 1} ^ {K} n _ {i} ^ {'} \cdot c. \end{array}\tag{24}
$$

## 5. Empirical methodology

To evaluate the performance of EURIKA, we conducted a number of experiments, using each of the domains described in the previous section. We compared the EURIKA approach to the FNE model [19], as well as a baseline that solely uses the agent's prior information to choose the best alternative. Our hypothesis was that using the EURIKA technique would increase the agent's overall gain as compared to the other methods. For each of the domains, the evaluation was performed over a number of rounds. Each round proceeded as follows:

• EURIKA was used to solve the OARI problem in each of the domains, and the optimal information gathering actions $( n _ { 1 } ^ { * } , . . . n _ { K } ^ { * } )$ were obtained.

• The alternative that is associated with the highest sample mean based on the obtained and prior information was chosen to solve the relevant problem instances in the domain.

Each round included four alternative solutions and a set of <sup>fi</sup>ve instances of prior information about each alternative. We varied the total number of rounds between 15 and 40 for each domain, such that all alternatives would be considered.

The parameters $\zeta$ and $\tau ^ { 2 }$ were assigned the average and the standard deviation of all of the rewards in each domain. The parameter $\sigma _ { i }$ was assigned the value of the standard deviation of the prior data obtained for each domain. In practice, when computing $P B _ { i } \left( n _ { 1 } ^ { ' } , . . . , n _ { K } ^ { ' } \right)$ , we assumed that the differences between sample means of different alternatives are independent.

For the SAT simulation domain, we used the same algorithms and settings used by Talman et al. [19] to facilitate comparison. These included a Greedy-SAT algorithm and variant GSAT algorithm with Random Walk probabilities of 40%, 60% and 80%. For the MF cost con<sup>fi</sup>guration, the number N of formulas to solve was set to 300. For the MT cost con<sup>fi</sup>gurations, the number of <sup>fl</sup>ip operations was set to 200,000 or 500,000 for each run. We executed all algorithms on the same 300 3-SAT formulas used by Talman et al. [19]. Each formula consisted of 100 different variables and 430 clauses. Each of the formulas was guaranteed to have a valid truth assignment. The prior data D for a given round consisted of the results of applying each of the four candidate algorithms on <sup>fi</sup>ve different 3-SAT formulas. Based on the average and standard deviation of the number of <sup>fl</sup>ip operations on all problems for all algorithms, we set $\zeta = 5 5$ , 200 and τ=22, 140.

In the SAT competition domain we used the 16 <sup>fi</sup>nalists of the SAT-Race 2006 competition. All algorithms were evaluated on the same 100 SAT formulas that were used in the <sup>fi</sup>nals. We followed the declared rules of the competition, in that solving each SAT problem earned the solver 1 point and additional “speed” points. The execution time was limited to 15 min per formula, otherwise the solver received 0 points for that instance. The number of speed points $p _ { s }$ for each successful solver s was computed by $p _ { s } = P _ { \mathrm { m a x } } { \cdot } ( 1 { - } \frac { t _ { s } } { T } )$ where t is the execution time solver s requires in order to solve the SAT instance, T is the execution time threshold, and $P _ { \mathrm { m a x } }$ is the maximal speed score a solver can receive for solving one SAT formula. Based on the average and standard deviation of the scores achieved by the different algorithms, we set $\zeta = 0 . 5 8 5$ and $\tau = 0 . 1 8 1$ . Other parameters were set to correspond to those in the actual tournament: $P _ { \mathrm { m a x } }$ was set at 1, N was set at 100, and T was set at 15 min. The candidate algorithms comprised the top-scoring entries in the competition.<sup>7</sup> The 3-SAT formulas in the competition were taken from several benchmark applications in industry, such as bounded model checking, and pipelined machines, as well as a set of formulas used in past competitions.

In the professor evaluation domain we used a student survey which was held at the Jerusalem College of Technology. Students were asked to rate lecturers' performance on their courses, using a scale ranging from 1 to 10. The 16 lecturers that received students' ratings were divided into four groups of four lecturers. Each round consisted of four lecturers and a prior sample of the ratings of <sup>fi</sup>ve students about each of the lecturers. We evaluated EURIKA over all lecturers for different values of v (250, 500, 750, 1000). We set the cost of obtaining each student rating for a particular lecturer at c=5 dollars. Using our database, we set $\zeta = 8 . 0 6$ and $\tau { = } 2 . 1 4 ,$ , which are respectively the average and the standard deviation of the grades that were given to 128 different lecturers.

The FNE model solely uses the prior information to decide on the number of samples to obtain. Alternatives with higher prior means are sampled more often than those with lower prior means. Again, we used the same procedure used by Talman et al. [19], in which the best alternative was sampled 6 times, the second-best was sampled 4 times, the third-best was sampled 3 times, and the worst alternative was sampled twice.

Fig. 1 presents the average number of <sup>fl</sup>ip operations per formula for the MF (left) and MT scenario (right) for the SAT simulation domain. The average number of <sup>fl</sup>ip operations per formula using the EURIKA model was 5825, while the average number according to the priorbest alternative model was 9273 (T-test pb0.002). Using EURIKA allowed one to save up to 47% <sup>fl</sup>ip operations per formula compared to the case in which additional information is not obtained. The EURIKA approach also used signi<sup>fi</sup>cant less <sup>fl</sup>ip operations per formula than the FNE model (5825 operations versus 6390 operations, T-test $\mathrm { P V } = 0 . 0 5 4 )$ ). The average number of samples recommended by EURIKA was 16.35, which was similar to the 15 samples used by the FNE, but EURIKA allocated these samples over different algorithms.

Fig. 1 also presents the average number of formulas solved in the MF scenario for the $T { = } 5 0 0 K$ and T=200K settings. For the $T =$ 200K setting, the EURIKA completed 34 formulas on average, versus 32 formulas solved by the FNE model, and 20 formulas solved by the prior-best alternative model. Although the difference between EURIKA and the FNE model was small, it was statistically signi<sup>fi</sup>cant. The difference in performance increased substantially for the $T =$ 500K setting. Here, EURIKA completed 86 formulas on average, versus 70 formulas using the FNE model, and 71 formulas using the prior-best alternative model (T-test pb0.001). The average number of samples recommended by EURIKA for this scenario was 8.15, almost half of the 15 samples used by the FNE. This shows that EURIKA was able to outperform the FNE model while acquiring less information that the FNE model.

![](/api/attachments/F8DYWR6B/fulltext/images/7a2d10742f6867b3f6d964f1bbaa1a22b0b2a5322e60ba710251537f7dc0cdaa.jpg)  
Fig. 1. (Left) Average # of formulas solved in the MF scenario (higher is better); (right) average # of <sup>fl</sup>ips per formula (divided by 10) in the MT scenario (lower is better).

Table 2 summarizes the extent to which each heuristic algorithm was chosen (in percentages) by the various models for the MT cost con-<sup>fi</sup>guration in the SAT simulation domain. A post-hoc analysis of this domain revealed that Random 80% was the best heuristic algorithm for solving the 3-SAT formulas in the simulation, followed by the Random 40%, Random 80%, and GSAT algorithms. As shown by the table, all algorithms chose the best heuristic more often than they chose other heuristics. However, EURIKA was able to choose the best heuristic 26% more often than the prior-best alternative model, and 8.8% more often than the FNE model (chi-square test, PVb0.001). In contrast to the other approaches, EURIKA did not use GSAT at all, which was the worst heuristic algorithm. Table 3 compares the performance of the various approaches in the SAT-competition domain.

As shown in the <sup>fi</sup>gure, the EURIKA model signi<sup>fi</sup>cantly outperformed all the other approaches. The average number of points using EURIKA (77 points) was signi<sup>fi</sup>cantly higher than the average number of points for the prior-best alternative (70 points) and the FNE model (73.5 points).

Fig. 2 compares the performance of the various models in the professor evaluation domain. We used several different values for v, and in all of these EURIKA signi<sup>fi</sup>cantly outperformed the prior-best method and the FNE model (T-test pb0.001).

On average, the EURIKA model achieved 54,638 points while the prior-best model achieved 52,136 points and the FNE model achieved 53,090 points (T-test, PVb0.001).

Table 4 concludes this section with two examples of the way EURIKA informed the information gathering actions in the 3-SAT simulation domain. Each example is drawn from one of the evaluation

## Table 2

Frequency (in percentages) of choosing each heuristic algorithm in the MT scenario according to the different approaches.

<table><tr><td>Model</td><td>GSAT</td><td>Random 60%</td><td>Random 80%</td><td>Random 40%</td></tr><tr><td>Prior-best</td><td>7.5%</td><td>22.5%</td><td>50.0%</td><td>20.0%</td></tr><tr><td>FNE model</td><td>0.7%</td><td>25.1%</td><td>67.2%</td><td>7.0%</td></tr><tr><td>EURIKA</td><td>0.0%</td><td>19.3%</td><td>76.0%</td><td>4.7%</td></tr></table>

Average performance for each approach in the SAT competition domain

<table><tr><td></td><td>Experiment 1</td><td>Experiment 2</td><td>Experiment 3</td></tr><tr><td>Prior-best</td><td>79.54</td><td>66.08</td><td>64.36</td></tr><tr><td>FNE model</td><td>80.77</td><td>69.1</td><td>70.54</td></tr><tr><td>EURIKA</td><td>81.42</td><td>73.5</td><td>75.9</td></tr></table>

![](/api/attachments/F8DYWR6B/fulltext/images/788e633459f651b404204f270fb66f6c584b542a2cf39b86a1c3496167e7c63c.jpg)  
Fig. 2. Average performance (in hundreds of dollars) in the professor evaluation domain.

rounds, in which Algorithms 1, 2, 3, and 4 correspond to different candidate algorithms. In the <sup>fi</sup>rst example, Algorithm 4 had the lowest average cost when considering the prior information, but with high standard deviation. Therefore EURIKA recommended additional samples. The new information included 35 samples of Algorithm 1, zero samples of Algorithms 2 and 3, and four samples of Algorithm 4.

In this example, the prior cost of using Algorithm 2 and its standard deviation is considerably lower than using the other algorithms. In this clear-cut situation, EURIKA did not recommend the obtainment of any additional information about the various alternatives.

## 6. Conclusion and future work

This paper formalized the problem of obtaining information gathering actions about stochastic processes with unknown outcomes that affect agents' utilities. Agents can obtain information at a cost about the different alternative processes. The paper established this problem to be NP-Hard, and provided a tractable, analytical solution to the problem by approximating the expected bene<sup>fi</sup>t from obtaining information about each alternative, while taking into account the associated costs. The solution to the problem is based on estimating the agent's expected bene<sup>fi</sup>t from gaining additional units of information about the alternative processes using statistical measures. The robustness of our technique is demonstrated empirically by deploying it in settings that varied the type of task to optimize, the nature of information gathering actions, and the measure of performance. These settings included “ecologically realistic” data that was obtained from the real world. Although our theoretical model assumes that populations are normally distributed, our empirical results show that in practice, our approach can also be applied towards populations that may not adhere to this assumption. In future work, we will augment the domain for situations in which agents' rewards are biased as well as situations in which distributions over rewards are unknown. We will also consider situations which include other decision-makers, requiring agents to consider the effect of their information gathering actions on each other's utilities.

## Table 4

Examples of performance the 3-SAT simulation domain

<table><tr><td></td><td>Algorithm 1</td><td>Algorithm 2</td><td>Algorithm 3</td><td>Algorithm 4</td></tr><tr><td>Average cost</td><td>25,751.40</td><td>22,708.80</td><td>26,332.60</td><td>14,201.60</td></tr><tr><td>Standard deviation ( $\sigma_i$ )</td><td>42,039.39</td><td>30,161.97</td><td>13,926.25</td><td>21,474.92</td></tr><tr><td>Additional samples</td><td>35</td><td>0</td><td>0</td><td>4</td></tr><tr><td>Average cost</td><td>6747.40</td><td>1143.20</td><td>9273.60</td><td>8503.20</td></tr><tr><td>Standard deviation ( $\sigma_i$ )</td><td>10,034.72</td><td>273.99</td><td>13,879.72</td><td>9530.35</td></tr><tr><td>Additional samples</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

## Acknowledgement

This work was supported in part by the Google Inter-university center for Electronic Markets and Auctions and Marie Curie reintegration grant 268362.

## Appendix A

Proof of Theorem 1. We present a reduction from the Knapsack problem [7]. An instance of the Knapsack problem is given by a constraint $C > 0 ,$ , a target value $V { > } 0$ and a set of n items $\{ 1 , . . . , n \}$ when each item i has a positive integer value $\nu _ { i }$ and a positive integer weight $w _ { i } .$ . The aim is to answer $\ " \mathrm { y e s } \ "$ if a vector $( u _ { 1 } , . . . , u _ { n } ) \in N ^ { n }$ exists such that $\textstyle \sum _ { i = 1 } ^ { n } u _ { i } \cdot v _ { i } \geq V$ under the condition that $\sum { } _ { i = 1 } ^ { n } u _ { i } \cdot w _ { i } \leq C$ . We create an instance of OARI as follows.

• For each item i we create an alternative $a _ { i \cdot }$ . The number of alternatives K equals the number of items n.

• For each variable $u _ { i }$ we create a variable $n _ { \mathrm { ~ } i \cdot } ^ { \prime }$

• We set $M = C .$

• We set L=V.

• We de<sup>fi</sup>ne the function Cost as follows:

$$
C o s t (a _ {i}) = \left\{ \begin{array}{l l} 0 & \text { if } \sum_ {j = 1} ^ {n} n _ {j} ^ {'} \cdot w _ {j} \leq C \\ v _ {i} & \text { otherwise } \end{array} \right..
$$

Suppose we already know that the expected pro<sup>fi</sup>t from obtaining $n _ { i } ^ { ' }$ units of information about alternative $a _ { i }$ is equal to $n _ { i } ^ { \prime } \cdot \boldsymbol { v } _ { i } .$ As a result $\begin{array} { r } { B ( \boldsymbol n ^ { \prime } _ { 1 } , . . . , \boldsymbol n ^ { \prime } _ { n } ) = \sum _ { j = 1 } ^ { n } \boldsymbol n ^ { \prime } _ { j } \cdot \boldsymbol \nu _ { j } . } \end{array}$ . Since $T ( n _ { 1 } ^ { ' } , . . . , n _ { n } ^ { ' } ) = B ( n _ { 1 } ^ { ' } , . . . , n _ { n } ^ { ' } ) -$ $\textstyle \sum _ { i = 1 } ^ { n } \dot { n _ { \ i } } \cdot C o s t ( a _ { i } )$ <sup>¼ ¼</sup>we obtain:

$$
T \Big (n _ {1} ^ {'},..., n _ {n} ^ {'} \Big) = \left\{ \begin{array}{l l} \sum_ {i = 1} ^ {n} n _ {i} ^ {'} \cdot v _ {i} & \text { if } \sum_ {i = 1} ^ {n} n _ {i} ^ {'} \cdot w _ {i} \leq C \\ 0 & \text { otherwise } \end{array} \right..
$$

We now prove that a vector ${ \overline { { v } } } { \in } N ^ { n }$ solves the OARI if and only if it solves the Knapsack problem.

(⇒) Suppose there is a solution for the OARI instance, that is a vector $( n ^ { \prime } _ { 1 } , . . . , n ^ { \prime } _ { n } ) { \in } N ^ { n }$ such that $\textstyle \sum _ { i } ^ { n } n _ { i } ^ { ' } \leq C$ and $T ( n ^ { ' } _ { 1 } , . . . , n ^ { ' } _ { n } ) { \geq } V .$ Since $V > 0 ,$ we have the following:

$T ( n ^ { \prime } _ { 1 } , . . . , n ^ { \prime } _ { n } ) { \neq } 0$ and thus $\begin{array} { r } { \sum _ { i = 1 } ^ { n } n _ { i } ^ { ' } \cdot w _ { i } { \le } C } \end{array}$

$$
\bullet \quad T (n _ {1} ^ {\prime},..., n _ {n} ^ {\prime}) = \sum_ {i = 1} ^ {n} n _ {i} ^ {\prime} \cdot v _ {i}..
$$

As a result, $\scriptstyle \sum _ { i = 1 } ^ { n } n _ { i } ^ { ^ { \prime } } \cdot v _ { i } \geq V$ and thus the vector $\left( n _ { 1 } ^ { ' } , . . . , n _ { n } ^ { ' } \right)$ is a so-<sup>¼</sup>lution to the Knapsack instance.

(⇐) Suppose there is a solution to the Knapsack instance, that is, a vector $( u _ { 1 } , . . . , u _ { n } ) { \in } N ^ { n }$ , such that $\textstyle \sum _ { i = 1 } ^ { n } u _ { i } \cdot w _ { i } \leq C$ and $\begin{array} { r } { \sum _ { i = 1 } ^ { n } u _ { i } \cdot \nu _ { i } { \geq } V . } \end{array}$ Since $\textstyle \sum _ { i = 1 } ^ { n } u _ { i } \cdot w _ { i } \leq C ,$ $\begin{array} { r } { T ( u _ { 1 } , . . . , u _ { n } ) = \sum _ { i = 1 } ^ { n } u _ { i } \cdot \nu _ { i } } \end{array}$ then $T ( u _ { 1 } , . . . , u _ { n } ) { \geq } V .$ In addition, since w is a positive integer for 1≤i≤n, $\begin{array} { r } { \sum _ { i = 1 } ^ { n } u _ { i } \le \sum _ { i = 1 } ^ { n } u _ { i } \cdot } \end{array}$ $w _ { i } { \leq } C ,$ and thus $\left( u _ { 1 } , \ldots , u _ { n } \right)$ solves the OARI problem. Therefore, the OARI problem is NP-Hard.<sup>8</sup> □

Proof of Proposition 3. After obtaining the $\overline { { \boldsymbol { r } ^ { \prime } } } _ { i } , \overline { { \boldsymbol { r } ^ { \prime } } } _ { j }$ additional information about alternatives $a _ { i } , a _ { j } ,$ the agent will choose alternative a if: $\frac { n _ { i } \overline { { r } } _ { i } + n _ { i } ^ { \prime } \overline { { r ^ { \prime } } } _ { i } } { n _ { i } + n _ { i } ^ { \prime } } > \frac { n _ { j } \overline { { r } } _ { j } + n _ { j } ^ { \prime } \overline { { r } } _ { j } ^ { \prime } } { n _ { j } + n _ { j } ^ { \prime } } \mathrm { ~ i f ~ } \overline { { r ^ { \prime } } } _ { j } < \frac { ( n _ { j } + n _ { j } ^ { \prime } ) \left( n _ { i } \overline { { r } } _ { i } + n _ { i } ^ { \prime } \overline { { r ^ { \prime } } } _ { i } \right) } { n _ { j } ^ { \prime } ( n _ { i } + n _ { i } ^ { \prime } ) } - \frac { n _ { j } \overline { { r } } _ { j } } { n _ { j } ^ { \prime } } .$ Since $r _ { j } ^ { \prime } { \sim } N \Big ( \mu _ { j } , \sigma ^ { 2 } \Big )$ $\overline { { r ^ { \prime } } } _ { j } { \sim } N \Big ( \mu _ { j } , \frac { { \sigma } ^ { 2 } } { n } \Big )$ and thus $P r \left( \overline { { r ^ { \prime } } } _ { j } < \frac { ( n _ { j } + n _ { j } ^ { ' } ) \left( n _ { i } \overline { { r } } _ { i } + n _ { i } ^ { ' } \overline { { r ^ { \prime } } } _ { i } \right) } { n _ { j } ^ { \prime } ( n _ { i } + n _ { i } ^ { ' } ) } - \frac { n _ { j } \overline { { r } } _ { j } } { n _ { j } ^ { \prime } } \right)$ is equal to the probability $P r \Big ( Z { < } Z _ { \alpha } \Big ( n _ { \ i } ^ { ' } , n _ { \ j } ^ { ' } , \overline { { { r ^ { ' } } } } _ { i } \Big ) \Big )$ where $Z _ { \alpha } \Big ( n _ { i } ^ { ' } , n _ { j } ^ { ' } , \overline { { { r _ { i } ^ { \prime } } } } \Big ) =$ $\frac { \sqrt { n _ { j } } \Big ( \big ( n _ { j } + n _ { j } ^ { ' } \big ) \big ( n _ { i } \overline { { r } } _ { i } + n _ { i } ^ { ' } r _ { i } ^ { ' } \big ) - \big ( n _ { i } + n _ { i } ^ { ' } \big ) \Big ( n _ { j } \overline { { r } } _ { i } - \mu _ { j } n _ { j } ^ { ' } \Big ) \Big ) } { n _ { j } ^ { ' } ( n _ { i } + n _ { i } ^ { ' } ) \sigma _ { j } } ,$

Proof of Proposition 4. Using the Maclaurin series expansion of the function $e ^ { x } \left[ 2 0 \right]$ we obtain:

$$
e ^ {x} \approx \sum_ {k = 0} ^ {\infty} \frac {x ^ {k}}{k !}.\tag{25}
$$

Therefore:

$$
e ^ {\frac {- x ^ {2}}{2}} \approx \sum_ {k = 0} ^ {\infty} \frac {(- 1) ^ {k} x ^ {2 k}}{2 ^ {k} k !}.\tag{26}
$$

Since $\textstyle { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { 0 } ^ { \infty } e ^ { \frac { - t ^ { 2 } } { 2 } } \mathrm { d } t = 0 . 5$ , we attain:

$$
\frac {1}{\sqrt {2 \pi}} \int_ {x} ^ {\infty} e ^ {\frac {- t ^ {2}}{2}} d t = 0. 5 - \frac {1}{\sqrt {2 \pi}} \int_ {0} ^ {x} e ^ {\frac {- t ^ {2}}{2}} d t
$$

$$
= 0. 5 - \frac {1}{\sqrt {2 \pi}} \int_ {0} ^ {x} \sum_ {k = 0} ^ {\infty} \frac {(- 1) ^ {k} t ^ {2 k}}{k ! 2 ^ {k}} d t + R _ {n}
$$

$$
= 0. 5 - \frac {1}{2 \pi} \Sigma_ {k = 0} ^ {n} \frac {(- 1) ^ {k} x ^ {2 k + 1}}{2 ^ {k} (2 k + 1) k !} + R _ {n}.
$$

According to the Lagrange Reminder theorem (see [20]) we <sup>fi</sup>nd that when |x|bd:

$$
\left| R _ {n} \right| <   \left| \frac {x ^ {n + 1}}{(n + 1) !} \right| <   \frac {d ^ {n + 1}}{(n + 1) !}.\tag{27}
$$

As a result $R _ { n } {  } 0 { \mathrm { , w h e n ~ } } n  { \infty } ,$ , and thus $\begin{array} { r } { P _ { a p p r o x } ( x ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { x } ^ { \infty } e ^ { \frac { - t ^ { 2 } } { 2 } } } \end{array}$ dt when $n \longrightarrow \infty .$ In addition, since $F ( x )$ <sup>ð Þ ¼</sup> is the integration over a density function, $F ( x ) \to 1$ when $x \to - \infty ,$ and $F ( x ) \to 0$ when $x \to \infty .$ . Thus, the error when $| x | \geq d$ holds $R _ { n } { \leq } 0 . 5 { - } \frac { 1 } { \sqrt { 2 \pi } } \int _ { 0 } ^ { | d | } e ^ { \frac { - t ^ { 2 } } { 2 } } \mathsf { d } t$ □

## References

[1] R. Azoulay-Schwartz, S. Kraus, Acquiring an optimal amount of information for choosing from alternatives, Cooperative Information Agents VI, 2002, pp. 123–137.

[2] D.A. Berry, B. Fristedt, Bandit Problems: Sequential Allocation of Experiments, Chapman and Hall, London, 1985.

[3] M. Bilgic, L. Getoor, Voila: ef<sup>fi</sup>cient feature-value acquisition for classi<sup>fi</sup>cation, Proceedings of the National Conference on Artificial Intelligence (AAAI). 2007

[4] S.E. Chick, J. Branke, C. Schmidt, Sequential sampling to myopically maximize the expected value of information, INFORMS Journal on Computing 220 (1) (2010) 71–80.

[5] V. Cicirello, S.F. Smith, The max K-armed bandit: a new model of exploration applied to search heuristic selection, National Conference on Arti<sup>fi</sup>cial Intelligence (AAAI), 2005, pp. 1355–1361.

[6] V. Conitzer, T. Sandholm, De<sup>fi</sup>nition and complexity of some basic metareasoning problems, International Joint Conference of Arti<sup>fi</sup>cial Intelligence (IJCAI), 1998, pp. 208–213.

[7] R. Garey, D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, Freeman, San Francisco, CA, 1979.

[8] J. Grass, S. Zilberstein, A value-driven system for autonomous information gathering, Journal of Intelligent Information Systems 140 (1) (2000) 5–27, (ISSN 0925–9902).

[9] C. Guestrin, Krause, Optimal value of information in graphical models, Journal of Arti<sup>fi</sup>cial Intelligence Research 35 (2009) 557–591.

[10] D. Heckerman, E. Horvitz, B. Middleton, An approximate nonmyopic computation for value of information, IEEE Transactions on Pattern Analysis and Machine Intelligence 150 (3) (1993) 292–298.

[11] A. Krause, C. Guestrin, Optimal nonmyopic value of information in graphical models-ef<sup>fi</sup>cient algorithms and theoretical limits, International Joint Conference on Arti<sup>fi</sup>cial Intelligence (IJCAI), 2005.

[12] A. Krause, C. Guestrin, Near-optimal observation selection using submodular functions, Proceedings of the National Conference on Arti<sup>fi</sup>cial Intelligence (AAAI), 2007.

[13] O. Madani, D.J. Lizotte, R. Greiner, Active model selection, Proceedings of the 20th Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, 2004, pp. 357–365.

[14] D. Madigan, R.G. Almond, On test selection strategies for belief networks. chapter Learning from Data: AI and Statistics IV, Springer-Verlag, 1996, pp. 89–98.

[15] J.A. Nelder, R. Mead, A simplex method for function minimization, The Computer Journal 70 (4) (1965) 308–313.

[16] Y. Radovilsky, S.E. Shimony, Observation subset selection as local compilation of performance pro<sup>fi</sup>les, Proc. of the 24th Annual Conf. on Uncertainty in Arti<sup>fi</sup>cial Intelligence (UAI-08), 2008, pp. 460–467.

[17] S. Reches, S. Talman, S. Kraus, A statistical decision-making model for choosing among multiple alternatives, International Joint Conference on Autonomous Agents and Multi-agent Systems (AAMAS), 2007.

[18] J. Streeter, S. Smith, An asymptotically optimal algorithm for the max k-armed bandit problem, National Conference On Arti<sup>fi</sup>cial Intelligence (AAAI), 2006

[19] S. Talman, R. Toester, S. Kraus, Choosing between heuristics and strategies — an enhanced model, International Joint Conference of Arti<sup>fi</sup>cial Intelligence (IJCAI), 2005, pp. 324–330.

[20] B. Thomas, R.L. Finney, Calculus and Analytic Geometry, Addison Wesley, 1996.

[21] C.C. Tseng, P.J. Gmytrasiewicz, Time sensitive sequential myopic information gathering, Proceedings of the 35th Annual Hawaii International Conference on Systems Science, 2002, p. 7.

Shulamit Reches (PhD, Computer Science, Bar Ilan University, 2010) is a faculty member in the Department of Applied Mathematics at Jerusalem College of Technology. Her research focus and publication record focuses on decision-making in uncertain environments.

Kobi Gal (PhD, Harvard University, 2007) is a faculty member in the Department of Information Systems and Software Engineering at Ben-Gurion University and an associate of the School of Engineering and Applied Sciences at Harvard University. He has published over 30 papers in top conferences and journals focusing on human-computer decision-making in areas from negotiation to science education. Gal is the recipient of the EU's Marie Curie Reintegration Grant for 2010; a two-time recipient of Harvard University's Derek Bok award for excellence in teaching; and a recipient of the School of Engineering and Applied Science's outstanding teacher award. He has taught numerous courses on AI and cognitive science at Harvard and Ben-Gurion Universities.

Sarit Kraus (Ph.D. Computer Science, Hebrew University, 1989) is a Professor of Computer Science at Bar-Ilan University and Adjunct Professor at the Institute for Advanced Computer Studies, University of Maryland. Kraus' research has made highly in<sup>fl</sup>uential contributions to numerous sub<sup>fi</sup>elds of Arti<sup>fi</sup>cial Intelligence, most notably to multiagent systems and nonmonotonic reasoning, Her research interests focus on the development of automated agents that negotiate with people. In particular, she has developed Diplomat, the <sup>fi</sup>rst automated agent that negotiated pro<sup>fi</sup>ciently with people.

In 1995, Kraus was awarded the IJCAI Computers and Thought Award. In 2002, she was elected as an AAAI fellow. In 2007, she was awarded the ACM SIGART Agents Research award, and her paper with Prof. Barbara Grosz was a winner of the IFAAMAS in<sup>fl</sup>uential paper award (joint winner). In 2008, she was elected as an ECCAI fellow. She was awarded the EMET prize in 2010, and in 2011, she was awarded the advanced ERC grant.

Kraus has published over 300 papers in leading journals and major conferences. She is the author of the book Strategic Negotiation in Multi-agent Environments (2001) and a co-author of the book Heterogeneous Active Agents (2000); both were published by MIT Press. She has presented many invited talks and tutorials, including a recent invited tutorial at ECAI 2010 on automated negotiation.
