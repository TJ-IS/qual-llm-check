---
otero_id: 17467
otero_key: "VFBWC8HE"
title: "Application of Markov decision processes to search problems"
authors: "Leo B. Hartman; Kees M. van Hee"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00021-j"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Application of Markov decision processes to search problems

Leo B. Hartman, Kees M. van Hee $^{1}$

Department of Computer Science, University of Waterloo, Ontario, Canada

## Abstract

Many decision problems contain, in some form, a NP-hard combinatorial problem. Therefore decision support systems have to solve such combinatorial problems in a reasonable time. Many combinatorial problems can be solved by a search method. The search methods used in decision support systems have to be robust in the sense that they can handle a large variety of (user defined) constraints and that they allow user interaction, i.e. they allow a decision maker to control the search process manually. In this paper we show how Markov decision processes can be used to guide a random search process. We first formulate search problems as a special class of Markov decision processes such that the search space of a search problem is the state space of the Markov decision process. In general it is not possible to compute an optimal control procedure for these Markov decision processes in a reasonable time. We therefore, define several simplifications of the original problem that have much smaller state spaces. For these simplifications, decompositions and abstractions, we find optimal strategies and use the exact solutions of these simplified problems to guide a randomized search process. The search process selects states for further search at random with probabilities based on the optimal strategies of the simplified problems. This randomization is a substitute for explicit backtracking and avoids problems with local extrema. These randomized search procedures are repeated as long as we have time to solve the problem. The best solution of those generated during that time is accepted. We illustrate the approach with two examples: the N-puzzle and a job shop scheduling problem.

Keywords: Markov decision processes; Guided random search; State space approximation

## 1. Introduction

Many decision problems contain a NP-hard combinatorial problem. A decision support system (dss) that assists a decision maker, needs a solver for the underlying combinatorial problem, that computes an approximation of a solution, because in most cases there is not enough time to compute an exact solution. There are two good reasons to solve a combinatorial problem by a search method: search methods are robust, i.e. they can be adapted easily if the problem is changing a bit, and they allow user interaction, i.e. they enable a decision maker to do search steps manually. Search problems are studied both in the field of combinatorial optimization and in artificial intelligence and have many different formulations. Normally the solution of a search problem is an element in a finite set, called the search space, that satisfies some criterion. The elements of the search space are called search states. Often the search space is specified in an implicit form, i.e., is specified by a method to compute the neighbourhood of a search state, i.e., the set of search states adjacent in the search space. A neighbourhood is usually small compared to the total search space. The neighbours of a search state are determined in two steps: first an action is chosen and secondly a transition function computes the neighbour, based on the action and the current search state. Sometimes there is a one-one relation between actions and neighbours, in that case the selection of an action is identified with the selection of a neighbour.

Searching is the process of starting at some element, selecting an action, making a transition to the corresponding neighbour and repeating these steps until a solution, i.e. a search state that satisfies some criterion, is found. The criterion is often membership in a particular set and is tested by an algorithm implementing the characteristic function for the set. In other cases the criterion is expressed in terms of a (real-valued) function, called the criterion function and a solution is a search state such that the value of the criterion function has a minimal or maximal value. This formulation is usually called an optimization problem. In general a method for controlling the search process is called a search method. Strategies for optimization problems that may stop at a local optimum of the criterion function are called local search methods.

Most interesting search problems are NP-hard so it is unlikely that there is an efficient algorithm to solve them. We are, therefore, interested in good approximations that involve a reasonable amount of computation.

There are specific algorithms for specific classes of search problems, e.g., the traveling salesman problem and the graph colouring problem. We use the term problem type for these classes. (See for instance [13] for a survey of optimization problem types.) While many researchers try to exploit all the knowledge they have about the structure of problem type to obtain an efficient algorithm, other researchers focus on what we call robust methods that work on a large variety of problem types. For example, branch-and-bound methods and heuristic search methods like the A\* algorithm are robust in this sense. (See, for instance, [14].) An interesting class of robust methods is based on analogies with physical or biological processes, for instance, simulated annealing [2] and genetic algorithms [4]. In both cases the search method randomizes its choices to simulate a natural process. In [1] a general search method is presented that subsumes, for instance, genetic algorithms and simulating annealing. It is shown that the search processes of this method behave like Markov chains and this property is used to prove convergence of the search method. In these randomized search methods the neighbourhood is searched at random according to some distribution over its elements. In simulated annealing, for example, the neighbours are selected with probabilities depending on the difference of the criterion value of the neighbour and the starting search state. A nice feature of random search methods is that no explicit backtracking is necessary since there is always some chance of returning to search states already visited.

A feature that is usually not considered in search problems is the cost of computation in relation with the quality of the solution. (See [5], [6], [11], [16].) In many practical cases, however, it is not worthwhile to carry out a long search for the best solution; instead we would accept a suboptimal solution found at a reasonable cost. In the case of a criterion function, we always get a value if we stop searching. In case we are looking for a search state in a given set there is, in fact, also a criterion function, namely the characteristic function of the given set. If however, we stop without obtaining a search state of this set, we fail to solve the problem even though we might be very “close” to a solution. We therefore, concentrate on problem types where there is a criterion function that expresses the quality of each of the search states in the search space. For instance, in scheduling problems the search space is the set of partial schedules and there might not be a schedule that meets all our constraints. In practice, however, it is usually possible to give a criterion value to partial schedules as well.

We concentrate on robust search problems where we apply random search and where we consider the search cost relative to the solution criterion value.

A second approach to decision making is based on Markov decision processes. A Markov decision process is characterized by a state space, an action set for each state and a transition probability. In each state some utility (cost or reward) is obtained and the goal is to control the process in such a way that the expected total utility is maximized. Markov decision processes deal explicitly with actions whose outcome is probabilistic and so have wider application than do search problems. In practice, however, Markov decision processes have a serious drawback because the known algorithms to determine an optimal control procedure algorithms, value iteration and policy iteration, iterate over the whole state space and are limited to “small” problems (cf. [3], [15]). An advantage of Markov decision processes is that they offer a useful framework for the specification of decision problems.

We discuss how the theory of Markov decision processes applies to search problems. The similarity with a search problem is evident: the state space is the search space, the transition probability describes the random probes over the neighbourhood of a search state, given an action. Further, the utility is the cost of choosing a neighbour if we continue the search and is the criterion value when we stop searching. In fact the Markov decision process that is equivalent to a search problem is a controlled stopping problem (cf. [7]).

Our approach is to solve the search problem by guided random search, which means that we simulate one or more random search processes and we use the best of them as our solution. A solution is a search path. If it contains cycles we may of course cut these cycles out to obtain a better search path. The actions in each step of the random search process are selected from distributions that are determined by a Markov decision process. We say that the search is guided by the Markov decision process. We call the Markov decision process that is equivalent with the search process the equivalent process. There are three ways of guidance.

\- In each step we compute an optimal action for the equivalent process to the search problem; the computation of this action does not require iteration over the whole state space, but only computations over a part that can be reached from the current state in a limited number of steps. We call this the exact method.

\- We define one or more abstractions of the equivalent process to the search problem. An abstraction has a much smaller state space than the equivalent process and actions for the abstracted process must be translated to the equivalent process. We use the actions of the abstractions for the search process. We call this the abstraction method.

\- We decompose the state space of the equivalent process into several subsets of a “manageable” size and we define for each of these subsets a Markov decision process that has the same structure, except for the fact that we stop as soon as we leave the (sub) state space. We call these smaller systems decompositions. For these decompositions we compute the optimal strategy as soon as we reach one of their states and we use this strategy until we leave the state space of the decomposition. We call this the decomposition method.

Note that in the exact method we solve (a part of a) Markov decision process in every step of the search process, in the abstraction method we only solve some Markov decision processes before the search process starts and in the decomposition method we solve Markov decision processes only when we enter the state space of a decomposition.

The size of the state spaces of abstractions or decompositions should be such that the necessary computations can be carried out in internal memory. Since we have to maintain some functions over the states, a reasonable size is $10^{5}$ states. The number of steps in a random search process should be large enough to be able to reach goal states (if they are defined) and the number of runs, i.e. the number of simulations of the search process, should be determined by the amount of computing time we may spend to solve the problem. We illustrate the results of some methods with numerical examples. The examples we have chosen are simple and well-known: the N-puzzle and a jobshop scheduling problem. The method is however intended for more complex problems for which no efficient algorithms are known. Note that in the guided random search process all kinds of constraints may be added while the guides are computed with models that might not be able to deal with these constraints.

The idea of approximating a Markov decision process with a very large state space by one with a much smaller state space is not new at all (see for instance $[12]$ ). However the use of these exact solutions for controlling a random search process for the original problem seems to be new. So we still solve the original problem and not another problem that “looks” similar.

## 2. Search problems

In this section we formalize the notion of a search problem. A search problem is characterized by a 5-tuple

$$
(S, A, T, c, r)
$$

in which

\- $S$ is a finite set, called the search space

\- A is a set-valued function, such that $\operatorname{dom}(A) = S$ and for all $s \in S$ the set $A(s)$ is finite and is called the set of allowable actions in state $s$ . There is one special action, called stop such that $\forall s \in S: stop \in A(s)$

\- $T$ is a function, called the transition function $\operatorname{dom}(T) = \{(s, a) | s \in S \land a \in A(s) \setminus \{stop\}\}$ with

$$
\forall s \in S, a \in A (s) \setminus \{s t o p \}: T (s, a) \in S
$$

T is such that if we are in state s and we choose action $a \in A(s) (a \neq stop)$ then we move to state $T(s, a)$ . If we take the action stop, the search stops.

\- $c$ is a function with $c \in S \to \mathbb{R}^{+}$ , called the cost function. If we are in state $s$ and we choose action $a \in A(s)$ and $a \neq stop$ we incur a cost $c(s)$ . It is assumed that

$$
\exists \epsilon \in \mathbb {R} ^ {+}: \forall s \in S \setminus \{s t o p \}: c (s) \geq \epsilon
$$

\- $r$ is a function with $r \in S \to R^{+}$ , called the terminal reward function. If we choose action stop in some state $s$ , we receive a final reward $r(s)$ .

A search path is a (finite) sequence of the following form:

$$
\left\langle \left(s _ {0}, a _ {0}\right), \dots , \left(s _ {n - 1}, a _ {n - 1}\right), \left(s _ {n}, s t o p\right) \right\rangle
$$

where $a_{i} \neq stop$ for $0 \leq i \leq n - 1$ and

$$
\forall i \in \{0, \dots , n - 1 \}: T (s _ {i}, a _ {i}) = s _ {i + 1}
$$

The objective is to find a search path with a maximal total return:

$$
r (s _ {n}) - \sum_ {j = 0} ^ {n - 1} c (s _ {j}),
$$

if the search is started in some given initial state $s_{0} \in S$ . We call such a path a solution of the search problem. A search method chooses the next action in a state given a partial search path. This concept will be formalized in the next section. Note that our formulation differs from the more standard formulation of a search problem in the sense that we have not defined goal states that have to be reached. In fact our formulation is a generalization of the standard formulation. To verify this let $S'$ be the subset of S that contains the goal states. To enforce that we are looking for search paths that stop if and only if a goal state is reached, we define the terminal reward function as:

$$
r (s) = \text { `large'   if   } s \in S ^ {\prime}
$$

= 0 otherwise.

Here the value ‘large’ denotes a value that is larger than (an upper bound for) the total cost of the set $S'$ .

We have chosen this generalization because in many search problems it is impossible to find a search path to the goal set in a reasonable time or there might be no search path to the goal set at all. In these cases the decision maker is satisfied with a partial solution, i.e. a search state with some good quality measure. This quality measure is expressed by the terminal reward function. So we forget the concept of a goal and we just look for a path from the initial state to a final state such that the reward of the final state minus the cost of the visits to other states is maximal.

We next consider another generalization of the standard search problems: we introduce random search actions. A random search action is a probability distribution over the set of actions in a state. We exclude the stop action from this distribution. Formally: for all $s \in S$ we define a finite set $Q(s)$ of probability distributions over $A(s) \setminus \{stop\}$ . Hence $q \in Q(s)$ is a function:

$$
q \colon A (s) \setminus \{s t o p \} \rightarrow [ 0, 1 ]
$$

such that

$$
\sum_ {a \in A (s) \setminus \{s t o p \}} q (a) = 1
$$

If we choose $Q(s)$ such that all of its members are degenerate distributions, i.e. all distributions that give one action probability one, then the set of all randomized search procedures enclosed the set of all deterministic search procedures. We conclude this section with the definition of a randomized search problem which is characterized by a 6-tuple:

$$
(S, A, Q, T, c, r)
$$

where $(S, A, T, c, r)$ is a search problem as defined above and, for $s \in S$ , $Q(S)$ is a finite set of randomized actions over $A(s)$ .

## 3. Markov decision processes

We now define one version of a Markov decision process and we summarize some old and well-known properties of these processes. Our discussion will be restricted to the class of Markov decision processes called negative dynamic programs. These processes have been extensively studied in $[17]$ (see also $[3]$ and $[15]$ ).

A Markov decision process is defined by a 4-tuple

$$
(X, D, P, u)
$$

in which

\- $X$ is a finite (or countable) set called the state space

\- $D$ is a set-valued function, with $\operatorname{dom}(D) = X$ and for $s \in X$ the set $D(s)$ is finite and it denotes the set of allowable actions in state $s$

\- $P$ is a transition probability, i.e. $P$ is a function with $\operatorname{dom}(P) = \{(s, a) | s \in X \land a \in D(s)\}$ and

$$
\begin{array}{l} \forall s \in X, a \in D (s): \forall s ^ {\prime} \in X: P (s ^ {\prime} | s, a) \in [ 0, 1 ] \\ \wedge \sum_ {s ^ {\prime} \in X} P (s ^ {\prime} | s, a) = 1 \end{array}
$$

\- $u$ is a real-valued function, such that $\text{dom}(u) = \text{dom}(P)$ , called the utility function

The next concept we define is a strategy. Let a Markov decision process be given. A strategy is an infinite sequence $\pi_{0}, \pi_{1}, \pi_{2}, \ldots$ such that

$$
\forall n \in N a t: \pi_ {n} \in (X \times \overline {{D}}) ^ {n} \times X \rightarrow \overline {{D}}
$$

where $\overline{D}=\bigcup_{s\in X}D(s)$ and Nat is the set of natural numbers including 0. The meaning of a strategy is that it determines for each path of the form $\langle(s_{0},a_{0}),\ldots,(s_{n-1},a_{n-1}),s_{n}\rangle$ what the next action has to be, namely $\pi_{n}(s_{0},a_{0},\ldots,s_{n-1},a_{n-1},s_{n})$ . The set of all strategies is denoted by $\Pi$ .

It can be proven that given a strategy $\pi$ and a starting state s, a stochastic process is determined. We denote the probability distribution over the paths of this process by $P_{s}^{\pi}$ and the expectation operator by $E_{s}^{\pi}$ . Let $X_{n}$ denote the state of the system after the n-th transition and $A_{n}$ the action chosen in that state for a (stochastic) process starting in s with strategy $\pi$ . Then $X_{n}$ and $A_{n}$ are random variables with joint distribution $P_{s}^{\pi}$ and $\langle X_{0}, A_{0}, X_{1}, A_{1}, \ldots \rangle$ is a stochastic process. The expected total return, denoted by $v(s, \pi)$ is defined by:

$$
v (s, \pi) = \mathbb {E} _ {s} ^ {\pi} \left[ \sum_ {n = 0} ^ {\infty} u (X _ {n}, A _ {n}) \right]
$$

We are interested in a strategy $\pi^{*}$ that satisfies:

$$
v (s, \pi^ {*}) = \sup _ {\pi \in \Pi} v (s, \pi)
$$

Such a strategy is called optimal. A strategy $\pi$ with the property that for all $n \pi_{n}$ depends only on the last visited state is called a stationary strategy and if $\pi_{n}$ depends only on n and the last visited state it is called memoryless. (Note that a stationary strategy is also memoryless.)

We define $v(s) = \sup_{\pi \in \Pi} v(s, \pi)$ and we call it the value function. Further we introduce similar functions for finite processes:

$$
v _ {k} (s, \pi) = \mathbb {E} _ {s} ^ {\pi} \left[ \sum_ {n = 0} ^ {k} u (X _ {n}, A _ {n}) \right]
$$

and

$$
v _ {k} (s) = \sup _ {\pi \in \Pi} v _ {k} (s, \pi).
$$

The following condition makes the Markov decision process a negative dynamic program:

$$
\forall s \in X, a \in D (s): u (s, a) \leq 0.
$$

For negative dynamic programs with finite sets of allowable actions the following properties hold: 1. the value function v satisfies, for all $s \in X$ :

$$
v (s) =
$$

$$
\max _ {a \in D (s)} \left\{u (s, a) + \sum_ {s ^ {\prime} \in X} P \left(s ^ {\prime} \mid s, a\right) \cdot v \left(s ^ {\prime}\right) \right\}
$$

2. there exists a stationary strategy that is optimal for all initial states, and the strategy that always takes an action that maximizes the right hand side in the equation above is such a strategy.

3. the sequence of functions $w_{n}$ on $X$ , defined, for $s \in X$ , by: $w_{0}(s) = 0$ and

$$
w _ {n + 1} (s) =
$$

$$
\max _ {a \in D (s)} \left\{u (s, a) + \sum_ {s ^ {\prime} \in X} P \left(s ^ {\prime} \mid s, a\right) \cdot w _ {n} \left(s ^ {\prime}\right) \right\}
$$

satisfies:

$$
\forall n \in N a t, s \in X: w _ {n} (s) \geq w _ {n + 1} (s)
$$

$\forall s \in X: v(s) = \lim_{n \to \infty} w_n(s)$

$\forall s \in X, k \in Nat : v_k(s) = w_{k+1}(s)$

4. for every initial state $s \in X$ and every $k \in Nat$ there is a memoryless strategy $\pi$ such that

$$
v _ {k} (s, \pi) = v _ {k} (s)
$$

and this strategy selects in state $s'$ at stage $n = k, k - 1, \ldots, 1$ an action that maximizes

$$
\max _ {a \in D (s)} \left\{u (s, a) + \sum_ {s ^ {\prime} \in X} P \left(s ^ {\prime} \mid s, a\right) \cdot w _ {n - 1} \left(s ^ {\prime}\right) \right\}
$$

Note that the “stage” means the number of steps to go. It is an immediate consequence of these properties that

$$
\forall s \in X, n \in N a t: w _ {n} (s) \geq v (s)
$$

so with $w_{n}$ we compute an upperbound for the value function. Approximating v by the sequence $\{w_{n}, n \in Nat\}$ is called value iteration.

## 4. Search problems as Markov decision processes

We are now ready to verify that a search problem is, in fact, a Markov decision process. We will consider only randomized search problems because the deterministic search problems are a special case of this class.

Let a randomized search problem $(S, A, Q, T, c, r)$ be given. It defines the Markov decision process $(X, D, P, u)$ in the following way:

\- $X = S \cup \{end\}$ , where end is a new state that denotes the situation after the search process has been stopped

$\forall_{s}\in S:D(s) = Q(s)\cup \{stop\}$

\- $D(end) = \{stop\}$

\- $\forall s, s' \in S, q \in Q: P(s' \mid s, q)$

$$
= \sum_ {\{a \in A (s) | T (s, a) = s ^ {\prime} \}} q (a)
$$

\- $\forall s \in X: P(end \mid s, stop) = 1$

\- $\forall s \in S, d \in D(s): (d \neq stop \Rightarrow u(s, d))$

$$
= - c (s)) \wedge u (s, s t o p) = r (s)
$$

\- $u(end, stop) = 0$

There is only one action, stop, that is possible in state end and it keeps the system in state end. The reward r is obtained if and only if stop is chosen in a state different from end.

Note that we cannot apply the properties of negative dynamic programs because the utility u is not non-positive. However we will see later that it is straightforward to modify the reward function a bit, such that we obtain a negative dynamic program. From now on we only consider Markov decision processes that represent randomized search problems.

First we introduce the concept of a stopping time. Each strategy determines a stopping time $\tau$ which is a random variable like the $X_{n}$ and $A_{n}$ , and that satisfies:

$$
\begin{array}{r l} & (\tau = 0 \Rightarrow A _ {0} = s t o p) \land \forall k \in N a t \setminus \{0 \}: \\ & \tau = k \Leftrightarrow (A _ {k} = s t o p \land A _ {k - 1} \neq s t o p) \end{array}
$$

In case all $A_{n} \neq stop$ then $\tau = \infty$ . Note that if $A_{n-1} \neq stop$ then all former actions differ from stop also. For $\tau \neq \infty$ we observe that $X_{\tau}$ is the state where action stop is chosen and so $r(X_{\tau})$ is the terminal reward if the search is stopped. For $\tau = \infty$ we define $r(X_{\tau}) = 0$ . Now we are able to give a more convenient expression for the expected total return of a search problem, let $s \in S$ and $\pi \in \Pi$ :

$$
v (s, \pi) = \mathbb {E} _ {s} ^ {\pi} \left[ r (X _ {\tau}) - \sum_ {n = 0} ^ {\tau - 1} c (X _ {n}) \right]
$$

First we show how to transform this Markov decision process into a negative dynamic program.

Lemma 1. Let $M = \max_{s \in S} r(s)$ and let $\tilde{r}$ be defined by

$$
\forall s \in S: \bar {r} (s) = r (s) - M
$$

Then we have $\forall s\in S,\pi \in \Pi$

$$
\begin{array}{r l} & {\mathbb {E} _ {s} ^ {\pi} \left[ r (X _ {\tau}) - \sum_ {n = 0} ^ {\tau - 1} c (X _ {n}) \right]} \\ & {\qquad = \mathbb {E} _ {s} ^ {\pi} \left[ \tilde {r} (X _ {\tau}) - \sum_ {n = 0} ^ {\tau - 1} c (X _ {n}) \right] + M} \end{array}
$$

This lemma allows us to use $\tilde{r}$ instead of r, and with $\tilde{r}$ we have a negative dynamic program. It is easy to transform the results of the case with $\tilde{r}$ to the case with r by adding M. From now on we assume r is not positive. We call a Markov decision process having these properties a search process and a strategy is now called a search method.

So we may apply the results for negative dynamic programs. Properties 1 and 3 of the former section can be reformulated.

Lemma 2. The functional equations for a search process have the following form:

\- the value function of a search process satisfies for all $s \in S$ :

$$
\begin{array}{l} v (s) = \max \left\{r (s), \max _ {q \in Q (s)} \left\{- c (s) + \sum_ {a \in A (s)} q (a) \right. \right. \\ \left. \cdot v (T (s, a)) \right\} \Bigg \} \end{array}
$$

\- the sequence of functions $w_{n}$ on $S$ satisfy, for $s \in S$ : $w_{0}(s) = 0$ and

$$
\begin{array}{l} w _ {n + 1} (s) = \max \left\{r (s), \max _ {q \in Q (s)} \left\{- c (s) \right. \right. \\ \left. + \sum_ {a \in A (s)} q (a) \cdot w _ {n} (T (s, a)) \right\} \Bigg \} \end{array}
$$

Remember that $\forall s\in X, n\in Nat: w_{n}(s)\geq v(s)$ , so we have an upperbound on $v$ . The next lemmas will be used to derive a lowerbound. First we introduce subsets of $\Pi$ , the set of all strategies. With $\Pi_{n}$ we denote the set of all strategies that stop before the $n+1$ -th transition and

$$
\tilde {\Pi} = \bigcup_ {n = 0} ^ {\infty} \Pi_ {n}
$$

the set of all strategies that stop. For these strategies we define a sequence of functions on $X$ by: $\forall s \in X, n \in \text{Nat}: z_n(s) = \sup_{\pi \in H_n} v_n(s, \pi)$

The next lemma gives some intuitive clear properties for the functions $z_{n}$ .

Lemma 3. The functions $z_{n}$ satisfy the following properties:

$\bullet z_0(s) = r(s)$

\- for $n \in Nat: z_{n+1}(s) = \max\{r(s), \max_{q \in Q(s)}\{-c(s) + \sum_{a \in A(s)} q(a) \cdot z_n(T(s, a))\}\}$ - for a given initial state and a given search time limit $k$ there is a memoryless strategy $\pi$ that chooses in search state $s$ at stage $n = k$ , $k - 1, \ldots, 1$ a (randomized) action that maximizes:

$$
\begin{array}{l} \max \left\{r (s), \max _ {q \in Q (s)} \left\{- c (s) + \sum_ {a \in A (s)} q (a) \right. \right. \\ \left. \cdot z _ {n - 1} (T (s, a)) \right\} \\ w h i c h s a t i s f i e s v _ {k} (s, \pi) = z _ {k} (s). \end{array}
$$

The proof of this lemma is not trivial, but uses standard arguments of the field of Markov decision processes. The next lemma gives the desired bounding properties.

Lemma 4. The following properties hold for all $s \in S$ :

$$
\begin{array}{l}\bullet \lim _ {n \rightarrow \infty} z _ {n} (s) = v (s)\\\bullet \forall m, n \in N a t: z _ {m} (s) \leq v (s) \leq v _ {n} (s) = w _ {n + 1} (s)\end{array}
$$

We are now able to approximate v as precisely as we want. Suppose we have computed lower and upper bounds $z_{m}$ and $v_{n}$ . The next lemma tells us how to determine an optimal strategy; however for every state we have to perform this computation.

Lemma 5. Let $s \in S$ be given, as well as $z_{m}$ and $v_{n}$ . If

$$
\begin{array}{c} r (s) \geq \max _ {q \in Q (s)} \left\{- c (s) + \sum_ {a \in A (s)} q (a) \right. \\ \cdot v _ {n} (T (s, a)) \Bigg \} \end{array}
$$

then choose stop and if;

$$
\begin{array}{c} r (s) \leq \max _ {q \in Q (s)} \left\{- c (s) + \sum_ {a \in A (s)} q (a) \right. \\ \cdot z _ {m} (T (s, a)) \Bigg \} \end{array}
$$

then continue the search. In the second case choose random search action $\tilde{q}$ if:

$$
\begin{array}{l} \sum_ {a \in A (s)} q (a) \cdot z _ {m} (T (s, a) \\ \geq \max _ {q \in Q (s)} \sum_ {a \in A (s)} q (a) \cdot v _ {n} (T (s, a) \end{array}
$$

If there is a case that is not covered by one of the conditions above we have to improve our the bounds by further iteration.

Note that it is not necessary to compute $z_{m}$ and $v_{n}$ for all $s \in S$ in order to determine the optimal randomized action in some state s because to compute for instance $v_{n}(s)$ we need for $k \in \{1, \ldots, n-1\}$ the values $v_{k}(s')$ for those $s'$ that can be reached by T in n-k steps. So this gives us an exact method to determine an optimal action for each search state.

Since, for all search methods, $\pi \in \tilde{\Pi}$ and all $s \in S$ we have:

$$
- M \leq v (s, \pi) \leq - \mathbb {E} _ {s} ^ {\pi} [ \tau ] \cdot \epsilon
$$

we may conclude

$$
\mathbb {E} _ {s} ^ {\pi} [ \tau ] \leq M / \epsilon
$$

which gives an estimate for the required number of steps to find that $v_{n}$ and $z_{n}$ are very close.

## 5. Simplification and guided random search

Although the exact method is elegant it can be very (computing) time consuming because the functions $v_{n}$ and $z_{m}$ have to be computed (as far as we need them) in every step of the random search process. The standard method for Markov decision processes, value iteration, is not applicable because it requires iteration over the whole state space.

We, therefore consider simplified Markov decision processes, translate their solutions to the equivalent process and use them in a guided random search, which is an approximation of the equivalent process.

Our main concern is the size of the search space; the simplified problems should have smaller search spaces. These smaller search spaces may be obtained by either decomposition or abstraction.

Decomposition splits the search space into subsets and for each of these subsets a search problem, a decomposition, is solved. Decompositions have almost the same structure as in the equivalent process, except that it stops when the boundary (defined below) of the state space is reached. Let $S_{1}^{\prime},\ldots,S_{n}^{\prime}$ be a partitioning of the search space S in non-empty sets. We then define the search space $S_{i}$ of decomposition i by:

$$
\begin{array}{c} S _ {i} = \left\{s \in S \mid s \in S _ {i} ^ {\prime} \vee \exists x \in S _ {i} ^ {\prime}, a \in A (x): \right. \\ s = T (x, a) \} \end{array}
$$

Here $S_{i} \setminus S_{i}'$ is called the boundary of the state space of decomposition $i$ and $S_{i}'$ the internal state space of $i$ . Further $A_{i}(s) = A(s)$ , if $s \in S_{i}'$ and $A_{i}(s)=\{stop\}$ , if s is in the boundary. The cost and reward functions are the same as in the equivalent process.

The guided search process uses the optimal actions of a decomposition as long as the system is in the internal state space of the decomposition. If the process enters the boundary an optimal search method for the entered decomposition is computed and that one is used until again a boundary is hit. Note that if the search process leaves an internal state space it enters an internal state space of exactly one other decomposition. Further note that the search process is only stopped in internal states.

Abstraction is a more general technique. Often we consider several abstractions simultaneously.

Let $(S, A, T, Q, c, r)$ be a randomized search problem, then the randomized search problems $(S_{i}, A_{i}, Q_{i}, T_{i}, c_{i}, r_{i})$ $(i \in \{1, \ldots, n\})$ are called abstractions if and only if there exist functions $\alpha_{i}$ and $\beta_{i}$ and $\gamma$ such that (for $(i \in \{1, \ldots, n\})$ ):

\- $\alpha_{i} \in S \to S_{i}$ and $\operatorname{dom}(\alpha_{i})$ is much larger than $\operatorname{rng}(\alpha_{i})$ .

$$
\beta \in \overrightarrow {A} \rightarrow \overline {{A}} _ {i}
$$

$$
\begin{array}{r l} \beta_ {i} (a) & \in A _ {i} (\alpha_ {i} (s)) \wedge T _ {i} (\alpha_ {i} (s), \beta_ {i} (a)) \\ & = \alpha_ {i} (T (s, a)) \end{array}
$$

where

$$
\bar {A} = \bigcup_ {s \in S} A (s) \quad \text { and } \quad \bar {A} _ {i} = \bigcup_ {s \in S _ {i}} A _ {i} (s)
$$

\- $\gamma \in \overline{A}_1 \times \ldots \times \overline{A}_n \to \overline{D}$ such that $\forall s \in S$ :

$$
\begin{array}{l} \bigwedge_ {i \in \{1, \dots , n \}} a _ {i} \in A _ {i} \big (\alpha_ {i} (s) \big) \\ \Rightarrow \gamma (a _ {i}, \dots , a _ {n}) \in D (s) \end{array}
$$

So $\alpha_{i}$ and $\beta_{i}$ form a morphism from the original problem to the abstraction i. Note that $\alpha_{i}$ and $\beta_{i}$ map the states and actions of the equivalent process to the state and actions of the decompositions, and that $\gamma$ combines the actions of the decompositions into an action for the equivalent process. Note that $\gamma$ produces either the stop action or a distribution over $A(s)$ , which may be degenerate. The functions $\beta_{i}$ do not play a role in the search method, they just guarantee consistency between the equivalent process and the abstractions. The function $\gamma$ can be constructed in many ways. Sometimes the actions of abstractions can be executed simultaneously (as in the job shop example) and in other cases they are actions for the equivalent process themselves and so only one of them can be executed (as in the N-puzzle example). A reasonable requirement for $\gamma$ is: $\gamma(stop, \ldots, stop) = stop$ .

We did not specify any requirement for the terminal reward and the cost function of the abstractions. A natural requirement is that for all $s \in S$ : $c_{i}(\alpha_{i}(s))$ is “close” to $c(s)$ and $r_{i}(\alpha_{i}(s))$ is “close” to $r(s)$ . An obvious choice for $c_{i}$ is:

$$
c _ {i} (s _ {i}) = \frac {\sum_ {\{s \in S \mid \alpha_ {i} (s) = s _ {i} \}} c (s)}{\# \{s \in S \mid \alpha_ {i} (s) = s _ {i} \}}
$$

where $\# A$ is the cardinality of set $A$ . A similar choice is possible for $r_i$ .

Before we can start the guided random search we have to compute stationary search methods for all abstractions. Let us call these search methods $\pi_{i}$ , such that $\pi_{i}$ is a function that assigns to each state $s_{i} \in S_{i}$ either the value stop or a distribution over $A_{i}(s_{i})$ .

The guided random search procedure is the following algorithm:

$$
\begin{array}{l} s \leftarrow s _ {0}; \\ a \leftarrow a _ {0}; \left\{a _ {0} \in A (s _ {0}) \setminus \{s t o p \} \right\} \\ l i s t \leftarrow \langle \rangle ; \\ \text { while } a \neq s t o p d o \\ \quad s \leftarrow T (s, a); \\ \quad l i s t \leftarrow l i s t \circ (s, a, c (s)); \\ \text { for all } i \in \{i, \dots , n \} d o \\ \quad \text { if } \pi_ {i} (\alpha_ {i} (s)) = s t o p \text { then } \\ \quad a _ {i} \leftarrow s t o p \\ \quad \text { else } a _ {i} \text { is   a   random   drawing } \\ \quad f r o m \pi_ {i} (\alpha_ {i} (s)) \text { fi }; \\ \quad \text { if } \gamma (a _ {1}, \dots , a _ {n}) = s t o p \text { then } a \leftarrow s t o p \\ \quad \text { else } a \text { is   a   random   drawing   from } \\ \quad \gamma (a _ {i}, \dots , a _ {n}) \text { fi } \\ l i s t \leftarrow l i s t \circ (s, s t o p, r (s)). \end{array}
$$

(Here $\circ$ denotes concatenation of an element to a list.) The variable list contains a solution of the problem. To determine the total return we simply have to add the third components of the elements of the list. The search path is obtained from this list by deleting the last component from each element of the list.

It is possible that the search is recurrent with the search returning to a previously visited state. In that case cycles can be eliminated from a search path to obtain a better solution.

We may apply this random search procedure repeatedly and return the best path found when the available computing time is exhausted.

## 6. Example: the $N$ -puzzle

The N-puzzle is a generalization of the 15-puzzle, a child's toy in which tiles numbered 1 to 15 are arranged in a 4 by 4 grid. An empty grid position allows tile in adjacent grid positions to be moved into that space, thus allowing the configuration of the puzzle to change, i.e., allows the puzzle to occupy different states. Solving the puzzle involves returning the puzzle to its goal state (Table 1).

The experiments discussed in this section actually involve the 8-puzzle rather than the 15-puzzle version previously described. The value of N = 8 was chosen because of the convenient size of the search space. There are $9! = 362880$ distinct configurations of the 8-puzzle only half of which are reachable from the goal state, thus resulting in a state space with 181440 states. A search space of this size is large enough to be interesting but small enough to analyze and manipulate in explicit form. For a similar reason the 8-puzzle was chosen for other empirical studies [5], [16].

For $N = k^2 - 1$ for some $k$ the state space $S_N$ is such that

$$
S _ {N} = \left\{s \mid s \in \{1, \dots , k \} ^ {2} + \{0, 1, \dots , N \} \right.
$$

Table 1
Goal state.

<table><tr><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>12</td><td>13</td><td>14</td><td>15</td></tr></table>

Table 2
Example state.

<table><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td></td></tr><tr><td>7</td><td>8</td><td>6</td></tr></table>

where $A \rightarrow B$ is the set of one-one mappings from set A into set B and 0 is the position without a tile. That is, members of $S_{N}$ are permutations of $\{0, \ldots, N\}$ . For N = 8, states have the form

$$
\begin{array}{c} \{(((1, 1), 1), ((1, 2), 2), ((1, 3), 3), \\ ((2, 1), 4), ((2, 2), 5), ((2, 3), 0), \\ ((3, 1), 7), ((3, 2), 8), ((3, 3), 6) \} \end{array}
$$

or more graphically as in Table 2.

The actions involve moving one of the tiles adjacent to the blank position into that position thus leaving the original position of the tile blank. We refer to these moves by the direction in which the blank moves and the set of possible moves is therefore {up, right, down, left}.

If we use $\text{row}(s)$ and $\text{col}(s)$ to refer to the first and second indices of the blank element in state s then

left $\in A(s)$ if $\operatorname{col}(s) > 1$

$$
\mathrm{up} \in A (s) \text {   if   } \operatorname{row} (s) > 1
$$

$$
\operatorname{right} \in A (s) \text {   if   } \operatorname{col} (s) <   k
$$

$$
\operatorname{down} \in A (s) \text {   if   } \operatorname{row} (s) <   k
$$

We distinguish a goal state such that $\text{row}(s)=1$ and $\text{col}(s)=1$ and $s(i,j)=(i-1)*k+j-1$ and refer to it by the term $g_{N}$ . That is, $g_{N}$ is the state as in Table 3. The transition function T is defined as follows:

$$
T (s, \text { left }) = s ^ {\prime}
$$

Table 3
Generic goal state.

<table><tr><td></td><td>1</td><td>...</td><td>k-1</td></tr><tr><td>k</td><td>k+1</td><td>...</td><td>2k-1</td></tr><tr><td colspan="4">...</td></tr><tr><td>N-k+1</td><td>N-k</td><td>...</td><td>N</td></tr></table>

such that

$$
\begin{array}{l} \forall (i, j) \in \{1, \dots , k \} ^ {2}: \\ \quad \left(\left((i, j) \neq (\operatorname{row} (s), \operatorname{col} (s))\right) \right. \\ \quad \wedge (i, j) \neq (\operatorname{row} (s), \operatorname{col} (s) - 1) \\ \Rightarrow s (i, j) = s ^ {\prime} (i, j)) \\ \quad \wedge s ^ {\prime} (\operatorname{row} (s), \operatorname{col} (s)) = s (\operatorname{row} (s), \operatorname{col} (s) - 1) \\ \quad \wedge s ^ {\prime} (\operatorname{row} (s), \operatorname{col} (s) - 1) = s (\operatorname{row} (s), \operatorname{col} (s)). \end{array}
$$

In short, the blank and the tile to its left exchange position. $T(s, m)$ for $m \in \{up, right, down\}$ is defined in a similar way. The state space $S_{N}$ then is the set $\{g\}$ closed under application of the actions defined by A.

The cost of visiting a state is the same for all states:

$$
\forall s \in S _ {N}: c (s) = 1
$$

The reward function is zero except for the distinguished goal state:

$$
\begin{array}{r l} r (s) = \rho & \text { if } s = g \\ = 0 & \text { otherwise } \end{array}
$$

where $\rho > 0$ .

We define $q_{i}(a)$ for $i \in \{\text{up, right, down, left}\}$ . For $\xi \in [0, 1]$

$$
\begin{array}{r l} q _ {i} (a) = \xi & \text { if } a = i \text { and } a \in A (s) \\ & = (1 - \xi) / (\# A (s) - 1) \\ & \text { if } a \neq i \text { and } a \in A (s) \end{array}
$$

where $\#A(s)$ is the cardinality of $A(s)$ . Then the set of randomized moves from state s is

$$
Q (s) \subset \left\{q _ {\mathrm{up}}, q _ {\text {right}}, q _ {\text {down}}, q _ {\text {left}} \right\}
$$

with $q_{i} \in Q(s)$ iff $i \in A(s)$ . For example, if $s_1$ is as in Table 4, then for $q_{\mathrm{up}} \in Q(s_1)$ :

$$
\begin{array}{l} q _ {\mathrm{up}} (\mathrm{up}) = \xi \\ q _ {\mathrm{up}} (\text {right}) = 0 \\ q _ {\mathrm{up}} (\text {down}) = (1 - \xi) / 2 \\ q _ {\mathrm{up}} (\text {left}) = (1 - \xi) / 2 \end{array}
$$

We see that $G_{N}=(S_{N}, A, Q, T, c, r)$ is a randomized search problem. To obtain an abstraction we use proper subsets of the N tiles to specify equivalence classes of states in $S_{N}$ . If we have $\delta\subset\{1,\ldots,N\}$ then the equivalence class of $s$ with respect to $\delta$ is

Table 4  
Example of initial state.

<table><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td></td></tr><tr><td>7</td><td>8</td><td>6</td></tr></table>

$$
[ s ] _ {\delta} = \left\{s ^ {\prime} \in S _ {N} \mid s (i, j) \notin \delta \Rightarrow s ^ {\prime} (i, j) = s (i, j) \right\}
$$

The tiles in $\delta$ are permuted among themselves. Equivalent states are only required to agree on the position of tiles not in $\delta$ . $\delta$ names positions in $s$ that are 'don't cares or wildcards and that match any member of $\delta$ . Let $S_{\delta}$ be the set of equivalence classes induced by $\delta$ of states in $S$ . This is the search space of the abstract problem. The goal in such an abstract search space is just $[g]_{\delta}$ where $g$ is the goal state in $S$ . The function $\alpha$ for this abstraction as

$$
\alpha (s) = [ s ] _ {\delta}
$$

Since there are the same set of allowable moves for each abstract state as for the corresponding state in the original search problem $G_{N}$ , we have simply for $a \in A(s)$ : $\beta(a) = a$ . In the experiments we only consider combinations of at most two abstractions. For the case of only one abstraction $\delta$ we have

$$
\gamma_ {\delta} (a) = a
$$

and we call the randomized search problem $G_{N,\xi,\delta}$ . For the case of two abstractions we define

$$
\gamma \in \overline {{{A}}} \times \overline {{{A}}} \rightarrow [ 0, 1 ]
$$

as

$$
\gamma_ {\delta , \epsilon} (a _ {\delta}, a _ {\epsilon}) = \left\{(a _ {\delta}, 1 / 2), (a _ {\epsilon}, 1 / 2) \right\}
$$

where $a_{\delta}$ and $a_{\epsilon}$ are the actions obtained from the abstractions induced by $\delta$ and $\epsilon$ . Thus we obtain a randomized search problem $G_{N,\xi,\delta\epsilon}$ that combines two abstractions defined by $\delta$ and $\epsilon$ .

## 6.1. Experiments

In order to measure the quantitative effect of abstraction we carried out a number of experi-

Table 6

ments with the 8-puzzle, varying the degree of abstraction, i.e., the number of wildcards, and the parameter $\xi$ of the probability distributions that determine the outcome of a move. Each of the experiments consisted of applying an abstract strategy to 1000 games. Given an initial state, the strategy generated actions until either the goal state was reached or the limit of 4000 steps was exceeded. For each game an initial state was selected by following a sequence of 21 randomly chosen steps. Doubling back was prohibited so a move could not be undone by the immediately following move. It was possible, however, for a loop to occur and for steps to be retraced thereafter. (Note that, by empirical verification, there are no states in the concrete space more than 31 steps from the goal.) The random steps need not all be on paths away from the goal node and, therefore, it is possible for an optimal solution for an initial state generated in this way to be less than 21 steps long.

We carried out experiments with the following strategies:

\- $G_{8,\xi,\delta_i}$ for $i = 3, \ldots, 7$ and for $\xi = \{.6, .7, .8, .9\}$ - $G_{8,\xi,\delta_i\epsilon_i}$ for $i = 3, \ldots, 7$ and for $\xi = \{.6, .7, .8, .9\}$ for $\delta_i = \{8 - i, 8 - i + 1, \ldots, 8\}$ and $\epsilon_i = \{1, 2, \ldots, i\}$ . For clarity the subscripts for $\delta$ and $\epsilon$ are omitted below. No confusion should arise. We refer to $G_{N,i,\delta}$ and $G_{N,\xi,\delta\epsilon}$ as simple and combined strategies, respectively. Thus, the experiments involved from 3 to 7 wildcards and a range of values for $\xi$ for both the simple and combined abstract strategies.

Table 5 shows the relative size of the concrete and abstract state spaces as a function of the number of wildcards. An abstract state defines an equivalence class of concrete states. The size of this equivalence class represents the factor by which the concrete search space is compressed by the abstraction mapping. As the size of equivalence classes grow, the optimal action of the abstract state matches fewer of the optimal actions for concrete states in its equivalence class. This property, of course, reduces performance of guided random search.

Table 5  
The size of equivalence classes of abstract states as a function of the number of wildcards.

<table><tr><td>Number of wildcards</td><td>Size of equivalence classes</td></tr><tr><td>3</td><td>6</td></tr><tr><td>4</td><td>12</td></tr><tr><td>5</td><td>60</td></tr><tr><td>6</td><td>360</td></tr><tr><td>7</td><td>2520</td></tr></table>

Percentage of successes as a function of the number of wild cards i and the randomization parameter $\xi$ for the simple and combined strategies.

<table><tr><td rowspan="2">i</td><td colspan="4">ξ</td></tr><tr><td>.6</td><td>.7</td><td>.8</td><td>.9</td></tr><tr><td>3</td><td>87/100</td><td>87/100</td><td>88/100</td><td>88/100</td></tr><tr><td>4</td><td>77/100</td><td>76/100</td><td>80/100</td><td>81/100</td></tr><tr><td>5</td><td>81/100</td><td>75/100</td><td>62/100</td><td>50/100</td></tr><tr><td>6</td><td>51/71</td><td>50/65</td><td>40/59</td><td>35/60</td></tr><tr><td>7</td><td>11/20</td><td>11/20</td><td>11/20</td><td>11/20</td></tr></table>

Tables 6 and 7 summarize experiments for both simple and combined strategies. The data suggest that, for the conditions of the 8-puzzle, the guided randomized search performs significantly better than pure random search and the combined strategy, $G_{8,\xi,\delta\epsilon}$ , performs better than the corresponding simple strategy, $G_{8,\xi,\delta}$ .

Table 6 shows the rate at which the guided random searches succeed in find the goal state. As a point of comparison the pure random search under the same conditions succeeds only 1.5% of the time. Even if the random search is allowed to continue for 100,000 steps, the success rate remains less than 17%. Thus from table 6 both the simple and combined guided searches perform much better.

The percentage of successes is the percentage of the total number of games for which a solution was found within 4000 steps. The value $\xi$ is the probability of taking the optimal move at each step and $i$ is the number of wild cards. Each entry gives the percentage for the simple strategy $G_{8,\xi,\delta}$ and the combined strategy $G_{8,\xi,\delta\epsilon}$ .

It is also clear that the combined strategy performs better than the simple strategy. The $\epsilon$ abstraction provides additional information about the direction of the goal even though moves provided the $\delta$ and $\epsilon$ abstractions are selected with equal probability.

Number of steps within which 50% of the games are solved by the simple and combined strategies and the combined strategy $G_{8,\xi,\delta\epsilon}$

<table><tr><td rowspan="2">i</td><td colspan="4">ξ</td></tr><tr><td>.6</td><td>.7</td><td>.8</td><td>.9</td></tr><tr><td>3</td><td>21/20</td><td>17/17</td><td>15/15</td><td>13/13</td></tr><tr><td>4</td><td>35/27</td><td>35/21</td><td>27/17</td><td>37/15</td></tr><tr><td>5</td><td>677/43</td><td>669/37</td><td>1111/27</td><td>3015/23</td></tr><tr><td>6</td><td>3697/393</td><td>-/97</td><td>-/85</td><td>-/55</td></tr><tr><td>7</td><td>-/-</td><td>-/-</td><td>-/-</td><td>-/-</td></tr></table>

Table 7 summarizes how quickly the combined strategy discovers solutions relative to the simple strategy.

Each entry shows the number of steps for the simple and combined strategy respectively. A “-” indicates that for the data collected not enough games were solved. The value $\xi$ is the probability of taking the optimal move at each step and i is the number of wild cards. Each entry gives the percentage for the simple strategy $G_{8,\xi,\delta}$ . We also did some experiments with decomposition. It turned out that the greater the state spaces of the decompositions are the better the guide works.

## 7. Example: job shop scheduling

The problem is defined by a 4-tuple $(M, K, D, J)$ :

1. $M$ is a finite set of machine types

2. $K$ is a function such that $K \in M \to N$ and $K(m)$ is the number of machines of type $m$ .

3. $D$ is a finite set of job identities

4. J is a set of jobs, in fact it is a function: $J \in D \to M^{*}$ , so a job is a pair consisting of a job identity and a sequence of machine type, required for the subsequent operations for the job.

We introduce some notation. For sequences, head gives the head, tail gives the tail and size the size. Further we need:

rest(0, p) = p

$$
\operatorname{rest} (k, p) = \operatorname{tail} (\operatorname{rest} (k - 1, p))
$$

From these objects we derive a search problem $(S, A, T, c, g)$ :

1. $S \subset D \to M^{*}$ such that $s \in S$ if and only if $\forall n \in D$ : $\exists k \in N$ : $s(n) = \text{rest}(k, J(n))$ The search state is, therefore, the amount of work still to be done.

2. $A(s)\subset D\to M$ such that

$$
\begin{array}{l} \forall a \in A (s): \forall n \in \operatorname{dom} (a): \\ a (n) = h e a d (s (n)) \wedge \forall m \in M: \\ \# \{n \in D | a (n) = m \} \leq k (n) \end{array}
$$

An action is, therefore, an assignment of tasks to machine types such that the machine is appropriate for the task (i.e., $a(n) = \text{head}(s(n))$ ) and we do not exceed the number of available machines.

3. $\forall s\in S,a\in A(s)$ $\forall n\in D:(n\notin \operatorname {dom}(a)\Rightarrow T(s,a)(n) = s(n))\wedge$ $(n\in \operatorname {dom}(a)\Rightarrow T(s,a)(n) = tail(s(n)))$

4. $c(s) = 1$ for all $s \in S$

5. $r(s) = -max_{n\in D}size(s(n))$

The “reward” is, in fact, a penalty for unfinished work. In the initial state it is $r(s) = -max_{n \in D} size(J(n))$ and in the ‘goal’ state it is just 0. Note that, since the reward function is already negative, it does not require a transformation.

An optimal search method corresponds to a schedule with a minimal make span. Finding such a schedule for this problem type is an NP-hard problem (see [8] or [10]) and it is reasonable to adopt an approximation to the problem type.

## 7.1. Experiments

We give the results for some very small problems in order to be enable the reader to calculate the optimal policies by hand.

We consider three strategies:

1. Decomposition by restricted look-ahead

2. Abstraction with “wildcard” machines

3. Abstraction by splitting in job sets

For the first strategy we consider the following jobshop problem. In Table 8 A, B and C represent machine types and each row represents a job. For each machine type the number of available machines is one. It is easy to verify that the optimal schedule takes 9 time units.

Table 8  
Example of jobshop.

<table><tr><td>A</td><td>B</td><td>C</td><td>B</td><td>A</td><td>C</td></tr><tr><td>A</td><td>C</td><td>A</td><td>B</td><td>A</td><td>B</td></tr><tr><td>B</td><td>C</td><td>B</td><td>A</td><td>C</td><td>B</td></tr><tr><td>B</td><td>A</td><td>C</td><td>A</td><td>B</td><td>C</td></tr><tr><td>C</td><td>B</td><td>A</td><td>B</td><td>C</td><td>A</td></tr></table>

Table 9  
Comparison random and two decompositions.

<table><tr><td>Schedule time</td><td>Random</td><td>3 ahead</td><td>5 ahead</td></tr><tr><td>9</td><td>18.8</td><td>71.2</td><td>77.4</td></tr><tr><td>10</td><td>56.4</td><td>93.2</td><td>96.6</td></tr><tr><td>11</td><td>88.4</td><td>99.2</td><td>100</td></tr></table>

In Table 9 we compare purely random search with two decomposition strategies with three and five steps look-ahead. The entries in the table are the percentages of runs for different completion times.

For the second strategy we consider only the first four jobs. Further the problem is the same. Each abstraction has only two machine types with one machine and “enough” of the third machine type. The three abstractions are combined. In Table 10 we display the percentages of runs for different completion times.

For the last strategy we added one job (Table 11). Further the problem is the same. For this problem the minimal makespan is 13. The abstractions are obtained by considering two groups of three jobs each: one group with the first three and the second group with the last three (including the extra job). The results are displayed in Table 12.

Table 10  
Comparison random and an abstraction.

<table><tr><td>Schedule time</td><td>Random</td><td>Abstraction</td></tr><tr><td>9</td><td>19</td><td>44.0</td></tr><tr><td>10</td><td>55.4</td><td>90.0</td></tr><tr><td>11</td><td>87.4</td><td>98.8</td></tr><tr><td>12</td><td>99.8</td><td>100</td></tr></table>

Table 11  
New job.

<table><tr><td>C</td><td>A</td><td>C</td><td>B</td><td>A</td><td>B</td></tr></table>

Table 12  
Another comparison random and abstraction.

<table><tr><td>Schedule time</td><td>Random</td><td>Abstraction</td></tr><tr><td>13</td><td>35.0</td><td>41.4</td></tr><tr><td>14</td><td>77.4</td><td>85.5</td></tr><tr><td>15</td><td>93.8</td><td>98.6</td></tr><tr><td>16</td><td>99.4</td><td>99.8</td></tr></table>

## 8. Conclusions

Applying techniques of Markov decision processes to implicitly defined search problems is a challenge. We have shown that the application of such techniques to large implicitly defined search spaces is feasible. The process of abstracting or decomposing the search and “translating” the actions of the resulting Markov decision back to the original search problem provides guidance for a randomized search. In addition experiments show that randomization accomplishes the same effect as explicit backtracking. Randomization sufficiently perturbs the search process so that the process does not get stranded at local optima. The same effect can be obtained by repeating the randomized search in the case of search problems involving actions that are irreversible.

We considered two techniques, decomposition and abstraction. The first one requires the solution of many Markov decision problems during the search process while the second one only requires the solution of some Markov decision problems before the search process starts. The choice of good abstractions is far from trivial, while the decompositions can be obtained easily.

While the experiments presented here allow us to claim interesting properties of the approach regarding two specific problems, the 8-puzzle and simple jobshop scheduling problem, additional experiments are required before more general statements can be made. Future directions include both experimenting with more realistic decision problems and comparing our approach with more traditional heuristic methods such as $A^{*}$ . Such directions will extend our understanding of the empirical properties of abstraction and decomposition. It would also be useful to measure the frequency with which the optimal actions for the concrete states of an equivalence class coincide with optimal action of the corresponding abstract state. The 8-puzzle is small enough that such measurements are feasible. We would also like to obtain methods for automatically generating abstractions and decompositions. For decompositions this seems to be quite simple while we have no idea to do this for abstractions. Finally we are interested in analytical results, such as bounds on the expected value of guided search.

The main point of this paper is that the guided randomized search performs much better than pure random search. That is, an exact solution for an abstracted problem captures useful information about the original concrete problem.

## Acknowledgement

The authors wish to thank Arno van Haastert, student from Eindhoven University of Technology, for performing some of the experiments and the Institute for Robotics and Intelligent Systems at the University of Waterloo for supporting this research.

## 9. Appendix

In this section the proofs of the lemma's of section 4 are presented.

## Proof of Lemma 1

Remember that S is finite, so M is defined properly. Using some well-known property of conditional probabilities, for the case

$$
\mathbb {P} _ {s} ^ {\pi} [ \tau = \infty ] \neq 0 \wedge \mathbb {P} _ {s} ^ {\pi} [ \tau <   \infty ] \neq 0
$$

we obtain:

$$
\begin{array}{l} \mathbb {E} _ {s} ^ {\pi} \left[ \tilde {r} (X _ {\tau}) - \sum_ {n = 0} ^ {\tau - 1} c (X _ {n}) \right] \\ = \mathbb {E} _ {s} ^ {\pi} \left[ \tilde {r} (X _ {\tau}) - \sum_ {n = 0} ^ {\tau - 1} c (X _ {n}) | \tau <   \infty \right] \mathbb {P} _ {s} ^ {\pi} [ \tau <   \infty ] \\ + \mathbb {E} _ {s} ^ {\pi} \left[ \tilde {r} (X _ {\tau}) - \sum_ {n = 0} ^ {\tau - 1} c (X _ {n}) | \tau = \infty \right] \mathbb {P} _ {s} ^ {\pi} [ \tau = \infty ] \end{array}
$$

Since $\forall s\in S\colon c(s) > \epsilon >0$ we have that

$$
\mathbb {E} _ {s} ^ {\pi} \left[ \sum_ {n = 0} ^ {\infty} c (X _ {n}) \mid \tau = \infty \right] = \infty
$$

So, if $P_{s}^{\pi}[\tau = \infty ] > 0$ then

$$
\mathbb {E} _ {s} ^ {\pi} \left[ \tilde {r} (X _ {\tau}) - \sum_ {n = 0} ^ {\tau - 1} c (X _ {n}) \right] = - \infty
$$

which is also the case if $\tilde{r}$ is replaced by $r$ . On the other hand, if $P_{s}^{\pi}[\tau = \infty] = 0$ we have:

$$
\begin{array}{r l} & {\mathbb {E} _ {s} ^ {\pi} \Bigg [ \tilde {r} (X _ {r}) - \sum_ {n = 0} ^ {r - 1} c (X _ {n}) \Bigg ]} \\ & {\quad = \mathbb {E} _ {s} ^ {\pi} \Bigg [ \tilde {r} (X _ {\tau}) - \sum_ {n = 0} ^ {\tau - 1} c (X _ {n}) | \tau <   \infty \Bigg ] \mathbb {P} _ {s} ^ {\pi} [ \tau <   \infty ]} \\ & {\quad = E _ {s} ^ {\pi} \Bigg [ r (X _ {\tau}) - M - \sum_ {n = 0} ^ {\tau - 1} c (X _ {n}) \Bigg ]} \end{array}
$$

which gives the desired result. □

## Proof of Lemma 2

We only proof the first functional equation, the second one proceeds along the same lines. First note that $v(end) = 0$ . So we may rewrite the functional equation for v as:

$$
\begin{array}{l} v (s) = \max \left\{r (s), \max _ {q \in Q (s)} \left\{- c (s) \right. \right. \\ \left. + \sum_ {s ^ {\prime} \in X} P \left(s ^ {\prime} \mid s, a\right) \cdot v \left(s ^ {\prime}\right) \right\} \Bigg \} \end{array}
$$

If we substitute the definition of $P$ , we only have to check that

$$
\begin{array}{l} \sum_ {s ^ {\prime} \in X} \bigg (\sum_ {\{a \in A (s) | T (s, a) = s ^ {\prime} \}} q (a) \bigg) \cdot v (s ^ {\prime}) \\ = \sum_ {a \in A (s)} q (a) \cdot v (T (s, a)) \end{array}
$$

To verify this we rewrite the left hand side into:

$$
\sum_ {s ^ {\prime} \in X} \sum_ {\{a \in A (s) | T (s, a) = s ^ {\prime} \}} q (a) \cdot v (T (s, a))
$$

Note that every $a \in A(s)$ appears only once in this double summation so we may rewrite this formula into

$$
\sum_ {a \in A (s)} q (a) \cdot v (T (s, a))
$$

which gives the desired result. □

## Proof of Lemma 3

The proof proceeds along the same lines as the proof of the similar properties for the functions $w_{n}$ and v. See [15] or [17]. ☐

## Proof of Lemma 4

Fix some $s \in S$ . First note that for $\pi \in \Pi_n$ : $v_n(s, \pi) = v(s, \pi)$ because after stopping the utility is 0 forever. Since, for all $n \in Nat$ : $\Pi_n \subset \Pi_{n+1}$ we have $z_n(s) \leq z_{n+1} \leq 0$ . Therefore $\lim_{n \to \infty} z_n(s)$ exists. Let us call this limit $z(s)$ . Note that:

$$
\lim _ {n \rightarrow \infty} \sup _ {\pi \in \Pi_ {n}} v (s, \pi) = \sup _ {\pi \in \tilde {\Pi}} v (s, \pi)
$$

Hence $z(s) = \sup_{\pi \in \tilde{H}} v(s, \pi)$ . To prove the first property we have only to show that the limit over $\tilde{H}$ equals the limit over $\Pi$ . To verify this, note that all strategies $\pi$ for which $P_s^\pi[\tau = \infty] > 0$ , have $v(s, \pi) = -\infty$ , as we have seen in the lemma (1). Since there is at least one strategy that does better, namely the strategy that stops immediately, we may delete the strategies in $\Pi \setminus \tilde{H}$ if we have compute the supremum. Hence $z(s) = v(s)$ .

To prove the second property note that

$$
z _ {n} (s) = \sup _ {\pi \in \Pi_ {n}} v (s, \pi , n) \leq \sup _ {\pi \in \Pi} v _ {n} (s, \pi) = v _ {n} (s).
$$

## Proof of Lemma 5

To prove this replace $z_{m}$ and $v_{n}$ by v in the formulas. Then we obtain exactly property (2) of negative dynamic programs as given in the section 3. ☐

## References

[1] E.J.L. Aarts and J. Korst. Simulated Annealing and Boltzman Machines: A Stochastic Approach to Combinatorial Optimization and Neural Computing. Wiley, 1989.

[2] E.J.L. Aarts, A.E. Eiben, and K.M. van Hee. Global convergence of genetic algorithms: a Markov chain analysis. In H.P. Schwefel and R. Maenner (eds.), editors, Parallel problem solving from nature, Lecture Notes in Computer Science. Springer Verlag, 1991.

[3] E.V. Denardo. Dynamic programming: Models and Applications. Prentice Hall, 1982.

[4] D.E. Goldberg. Genetic algorithms in search, optimization, and machine learning. Addison-Wesley, 1989.

[5] O. Hansson and A. Mayer. Probabilistic heuristic estimates. In Proceedings of the Fifth Workshop on Uncertainty in Artificial Intelligence, 1989.

[6] L.B. Hartman. Decision theory and the cost of planning. Technical Report 355, Department of Computer Science, University of Rochester, Rochester, NY, March 1989.

[7] A. Hordijk. Markov decision processes and potential theory. MC Tracts, 1986.

[8] D.S. Johnson J.R. Garey. Computers and Intractability: A Guide to the Theory of NP-completeness. Freeman, 1979.

[9] Richard E. Korf. Macro-operators: A weak method for learning. AI, 26:35–77, 1985.

[10] J.K. Lenstra and Rinooy Kan. Complexity of scheduling under precedence constraints. Operations Research, 26:22–35, 1978.

[11] Steven Minton. Qualitative results concerning the utility of explanation-based learning. In AAAI-88, pages 564–569, 1988.

[12] J.M. Norman. Heuristic procedures in dynamic programming. Manchester University Press, 1972.

[13] C.H. Papadimitrion and K. Steiglitz. Combinatorial Optimization: Algorithms and Complexity. Prentice Hall, 1982.

[14] J. Pearl. Heuristics: Intelligent Search Strategies for Computer Problem Solving. Addison-Wesley, 1984.

[15] S.M. Ross. Introduction to stochastic dynamic programming, Academic Press, 1983.

[16] S. Russell and E. Wefald. Do the Right Thing. 1991.

[17] R.E. Strauch. Negative dynamic programming. Annals of Mathematical Statistics, pages 871-890, 1966.

Kees M. van Hee is professor of computing science at the Eindhoven University of Technology (since 1984) and part-time consultant of Bakkenist Management Consultants, in Amsterdam. He received a masters degree in mathematics (1971) from the University of Leiden and a Ph.D in mathematics from Eindhoven (1978). His dissertation was on adaptive control of Markov decision processes. From 1978 till 1984 he worked for a consultancy company in Rotterdam where he developed several decision support systems. His research interests are: formal specifications, in particular executable specifications and heuristic search methods for operational planning problems.

Leo B. Hartman received a Ph.D in Computer Science from the University of Rochester (1990). He is currently working in the Computing and Intelligent Systems group of the Canadian Space Agency. His research interests include artificial intelligence, symbolic computing, the representation of uncertainty and the control of inference.
