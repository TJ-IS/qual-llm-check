---
otero_id: 26260
otero_key: "F5DPXKPV"
title: "Alternative Mechanisms of Allocating Computer Resources Under Queueing Delays"
authors: "Seungjin Whang"
year: "1990"
journal: "Information Systems Research"
doi: "10.1287/isre.1.1.71"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Information Systems Research

## H4R

![](/api/attachments/F5DPXKPV/fulltext/images/737dc5d06fd75614bdb7523ba5dd09d4b7185fc259367f88d7da57f7145be1cf.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Alternative Mechanisms of Allocating Computer Resources Under Queueing Delays

Seungjin Whang,

To cite this article:

Seungjin Whang, (1990) Alternative Mechanisms of Allocating Computer Resources Under Queueing Delays. Information Systems Research 1(1):71-88. http://dx.doi.org/10.1287/isre.1.1.71

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1990 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/F5DPXKPV/fulltext/images/99830e1166de35d3712a682a923baf810ffd22a439f9bbbb11a3744a815f516c.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Alternative Mechanisms of Allocating Computer Resources Under Queueing Delays

Seungjin Whang

Graduate School of Business

Stanford University

Stanford, California 94305

A theoretical framework is developed in which alternative mechanisms of allocating congestion-prone computer rescurces are studied and compared. Two—discrete and continuum-models of economies are presented to depict a small and a large economy respectively. Alternative allocation mechanisms are discussed in these two models: (1) the private bargaining approach, (2) allocations attainable through Nash equilibria and (3) the Clarke-Groves tax mechanism in the discrete economy model, and (4) Mendelson's (1985) job-by-job pricing and (5) the exchange-market-based allocation in the continuum economy model. We find equivalence among the bribes and prices associated with these mechanisms. The theory is related to practical implications pertaining to the design of computer chargeback systems and the role of the system manager.

Control of computer resources—-Queueing detays-Allocation methods

## 1. Introduction

system dates back to the mid-sixties wher Kleinrock (1964) applied queueing theory to communication networks. Ever since there has been a considerable body of work along this line of research (see Kleinrock 1975, Sauer and Chandy 1981 Tanenbaum 1981, Lazowska, Zahorjan, Graham and Sevcik 1984, for example). This research has recently led to a variety of software products supporting computer performance evaluation and capacity planning (CPE/CP). Most of the past research is, however, focused on the performance analysis of a computer system, with little regard to its control and management issues. One of the prominent exceptions to this trend is the work of Mendelson (1985), who provides a microeconomic analysis incorporating queueing effects and incentive issues in a computer center. One of his important results is that a free access policy in a computer system leads to more congestion than socially optimal, so that some kind of control mechanism (e.g., pricing) is required to maximize the net value of the system.

The main concern of this paper is to explore Mendelson's point from a broader perspective, and compare alternative mechanisms to achieve optimal allocations of congestion-prone computer resources—optimal in the sense that it maximizes the net value of the system defined as the sum of individual users' net benefits. We develop a simple framework similar to Mendelson's (1985) to discuss different mechanisms on the same footing. Two—discrete and continuum—models of economies are presented to depict a small and a large economy respectively. Alternative allocation mechanisms are discussed in these two models: (1) the private bargaining approach, (2) allocations attainable through Nash equilibria and (3) the Clarke-Groves tax mechanism in the discrete economy model, and (4) the job-by-job pricing mechanism and (5) the market-based allocation in the continuum economy model.

These mechanisms have been independently developed under different settings in the theory of externalities, ever since Pigou (1920) first brought externalities under economics analysis. Pigou seemed to believe (without analytic support) that there exists a determinate (meaning that all the parameters of the price schedule are predetermined other than the user's decision) tax system that induces selfinterested agents to reach a socially optimal equilibrium. Following the Pigouvian tradition, Mendelson (1985) formalizes the job-by-job pricing mechanism in computer center environments. One of the crucial assumptions underlying the Pigouvian tradition is that the economy should comprise a large number of agents. In case there are a small number of agents involved in the externality, the availability of such a determinate tax schedule is not guaranteed.

As a resolution to this situation Meade (1952) proposes a nondeterminate tax schedule that aligns the incentives of agents with the social objective in the presence of entangled externality relations. This allocation is attainable through a Nash equilibrium under a strong assumption that the central planner has all relevant agent-specific information available. Davis and Whinston (1962) raise questions regarding conceptual and operational difficulties when the allocation is implemented through non-dominant strategy equilibria.

Meanwhile, an entirely different approach had been proposed by Coase (1960) Coase claims that a socially optimal allocation can be achieved with minimal state intervention through an initial assignment of rights followed by voluntary exchange of rights, if there is no transaction cost. Further, the optimal allocation takes place independent of the initial allocation of the rights. The Coase theorem, however, has been under attack in several aspects, one main criticism (due originally to Wellisz 1964) being that the private bargaining approach is exposed to game-theoretic dissembling when a transaction involves many agents. More recent scrutiny of the theory reveals that complete information among agents is a crucial assumption to be added to the theorem. It has been suggested by Arrow (1979) and Samuelson (1985) that the rights assignment would not suffice to achieve the social optimum in the presence of imperfect information.

A breakthrough to handle the case of informational asymmetry was provided by Vickrey (1961), Clarke (1971) and Groves and Loeb (1975). The central planner would like to allocate scarce resources to maximize a social welfare function. Each agent is oriented toward his own interest rather than achievement of the social welfare, and possesses private information about his preference. The problem is how to optimally allocate the resources under the incentive and asymmetric information problems. To resolve this, consider the following class of mechanisms: first ask each agent to report his private information to the central planner. Based on the reports, the central planner makes an allocation decision and the tax charged to each agent is determined. Since there is no way to enforce each agent to report his true parameter, the tax is designed such that each agent finds it to his best interest to report his true parameters. The Clarke-Groves tax mechanism is one of such self-enforcing mechanisms.

In the present paper these alternative mechanisms are grafted to a computer system environment. Each mechanism is addressed in one of the two (small and large) economic models which are seemingly developed in isolation, but there is enough linkage between the two economic settings to allow comparisons of all these alternatives in a consistent manner. This approach guides us to practical implications pertaining to the design of computer chargeback systems and the role of the system manager in a computer center. Another contribution of this paper that is of theoretical character is to demonstrate striking equivalence among the bribes/prices associated with all these mechanisms.

The plan of this paper is as follows. §2 develops a small-economy model in which a finite number of significantly large agents (e.g., departments in a firm, or colleges in a university) are competing over the use of the system. Three allocation mechanisms—(1) the private bargaining approach, (2) allocations attainable through Nash equilibria and (3) the Clarke-Groves tax mechanism—are discussed in this model. An alternative economy with a continuum of agents (e.g., individual users of a mainframe) is introduced in §3, in which we study the remaining two mechanisms—(4) the job-by-job pricing mechanism and (5) the exchange-marketbased allocation. The last section provides an overview of the results, discusses several related issues, and suggests further research.

## 2. A Discrete Economy

An organization owns a computer system which is shared among N agents $( \mathbf { e . g . }$ departments). When agent i uses the system at the rate of $\lambda , \geq 0$ per unit of time for $i = 1 , 2 \dots N ,$ the gross benefit (or profit contribution to the organization) accruing to agent i per unit time is denoted by $V _ { \mathfrak { r } } ( \lambda _ { \mathfrak { r } } )$ , where $V , ( \cdot )$ is assumed to be nondecreasing, concave and continuously twice differentiable for $i = 1 , 2 \dots N .$ C(λ) denotes the congestion cost inflicted on € ach job in the system where λ is the total usage rate, i.e., $\lambda \stackrel { \mathrm { d e f } } { = } \textstyle \sum _ { k = 1 } ^ { N } \lambda _ { , }$ ; hence, the term $\lambda , C ( \lambda )$ represents the congestion cost incurred by agent i per unit time. C(·) is strictly increasing, convex and continuously twice differentiable. This congestion cost captures queueing delays (i.e., slow response times) and other quality degradation (e.g., frequent breakdowns or poor quality of a laser printer) due to systems congestion. There is a constant variable cost of using the system, which is normalized at zero and incorporated into the (gross) benefit function. The net benefit (per unit time) to agent i is defined as $\begin{array} { r } { N \bar { V } _ { \iota } ( \mathtt { A } ) = V _ { \iota } ( \lambda _ { \iota } ) - \lambda _ { \iota } C ( \lambda ) } \end{array}$

The net value of the system is defined as the aggregation of the net benefits of those who participate in the system. The decision to be made by the organization is how to allocate the system to N agents such that the net value of the system per unit time is maximized. Formally, the problem can be formulated as

$$
\max _ {\lambda} \sum_ {k = 1} ^ {N} \left[ V _ {k} \left(\lambda_ {k}\right) - \lambda_ {k} C \left(\sum_ {j = 1} ^ {N} \lambda_ {j}\right) \right],\tag{2.1}
$$

where $\lambda _ { \iota } \in [ 0 , \infty )$ A solution to the program is called socially optimal. To simplify the analysis we assume the program has a unique solution $\lambda ^ { * }$ . The following proposition reveals the simple structure of $\pmb { \lambda } ^ { * }$

PROPOSITION 1. Let $\bigstar ^ { * }$ be the solution to the problem (2.1). Then $\bigstar ^ { * }$ satisies

$$
\left\{ \begin{array}{l l} V _ {k} ^ {\prime} (\lambda_ {k} ^ {*}) = C (\lambda^ {*}) + \sum_ {j = 1} ^ {N} \lambda_ {j} ^ {*} C ^ {\prime} (\lambda^ {*}) & \text {if} \lambda_ {k} ^ {*} \geq 0; \\ V _ {k} ^ {\prime} (0) \leq C (\lambda^ {*}) + \sum_ {j = 1} ^ {N} \lambda_ {j} ^ {*} C ^ {\prime} (\lambda^ {*}) & \text {if} \lambda_ {k} ^ {*} = 0. \end{array} \right.
$$

PRooF. Straightforward from the Kuhn-Tucker Theorem

The socially optimal rule is, therefore, to allocate the system such that the marginal value of the last use is identical, say ${ \mathfrak { F } } ,$ across all participating agents. Those agents who do not have any system applications worth more than $\breve { \bar { V } }$ should abstain from the system. We assume throughout this paper that each agent is oriented towards maximizing his own performance measure, which is given by the net benefit minus transfer price payment. The key issue to be addressed is the design of goal-congruent mechanisms to achieve the socially optimal allocation We discuss three such mechanisms which operate under different logistics: the private bargaining approach, the Clarke-Groves tax mechanism and a mechanism built on Nash equilibrium.

## 2.1. Private Bargaining Approach

According to this decentralized approach, the system manager initially assigns the usage rights of the system to agents to yield an allocation $\lambda ^ { \bar { \circ } }$ with $\begin{array} { r } { \sum _ { k = 1 } ^ { N } \lambda _ { k } ^ { \circ } < \infty , } \end{array}$ which may not necessarily be socially optimal. Then, agents trade the usage rights through private bargaining and a series of re-allocations of rights result. According to Coase (1960), this bargaining process will achieve a Pareto optimum (which corresponds to the social optimum in our economy of agents with quasi-linear utility) even under the existence of externalities. A required condition for the Coase economy is that the bargaining market is frictionless in the sense that there are no transaction costs and all gains from transactions are exhausted. Possible transactions in our framework consist of the following three types: (1) usage rights are newly issued, (2) usage rights are retired from the system, and (3) usage rights are exchanged between two agents. Every transaction must be based on unanimous agreements by the agents affected. For example, if an agent applies for an increase of his rate by a certain amount, he must get permission for the increase from each incumbent user. This process involves payment of a bribe by the one to the other. Likewise, an agent may choose to retire his usage rights by receiving compensation from the incumbent users

PRoposıTioN 2. Suppose the initial allocation of the system is given by λ° satisfying $\begin{array} { r } { \sum _ { l = 1 } ^ { N } \lambda _ { l } ^ { \circ } < \infty } \end{array}$ . The three types of transactions described above achieve a Pareto optimum, hence the social optimum, independent of the initial allocation

ProoF. We show that there is room for a Pareto-improving transaction of some type if and only if the optimality conditions of Proposition 1 are not met.

Consider first the case of allocation λ in which, for some $i , V _ { \iota } ^ { \prime } ( \lambda _ { \iota } ) > C ( \lambda ) +$ $\Sigma _ { k } \lambda _ { k } C ^ { \prime } ( \lambda )$ , violating an optimality of Proposition 1. We now show that i can find a Pareto-improving transaction of type 1. Leting $f _ { \iota } ( \lambda _ { \iota } ) = V _ { \iota } { } ^ { \prime } ( \lambda _ { \iota } ) - C ( \Sigma _ { \iota = 1 } ^ { \cal N } \lambda _ { \iota } ) -$ $\begin{array} { r } { \sum _ { k } \lambda _ { k } C ^ { \prime } ( \sum _ { l = 1 } ^ { \mathrm { \tilde { N } } } \lambda _ { \mathrm { \ell } } ) , } \end{array}$ , we find $f _ { \iota } ^ { \prime } ( \cdot ) < 0$ from concavity of $V ( \cdot )$ , and monotonity and strict convexity of $\overrightarrow { C } ( \cdot )$ .We can find $\epsilon > \vartheta$ such that $f _ { \iota } ( \lambda _ { \iota } + \iota ) > 0$ for any $x \in [ 0 , \epsilon ]$ . It follows that

$$
\int_ {\lambda_ {i}} ^ {\lambda_ {i} + \epsilon} f _ {i} (x) d x > 0,
$$

which can be shown (after some algebra) equivalent to

$$
\left[ V _ {i} \left(\lambda_ {i} + \epsilon\right) - \left(\lambda_ {i} + \epsilon\right) C (\lambda + \epsilon) \right] - \left| V _ {i} \left(\lambda_ {i}\right) - \lambda_ {i} C (\lambda) \right]
$$

$$
> - \sum_ {k \neq i} \left[ V _ {k} (\lambda_ {k}) - \lambda_ {k} C (\lambda + \epsilon) \right] + \sum_ {k \neq i} \left[ V _ {k} (\lambda_ {k}) - \lambda_ {k} C (\lambda) \right].
$$

Using the notation $\begin{array} { r } { N V _ { k } ( \mathbf { \lambda } ) = V _ { k } ( \lambda _ { k } ) - \sum _ { \jmath = 1 } ^ { N } \mathcal { A } _ { \jmath } C ( \boldsymbol { \lambda } ) } \end{array}$ , the last expression is rewritten as

$$
N V _ {i} (\boldsymbol {\lambda} + \epsilon \mathbf {e} _ {i}) - N V _ {i} (\boldsymbol {\lambda}) > - \sum_ {k \neq i} \left[ N V _ {k} (\boldsymbol {\lambda} + \epsilon \mathbf {e} _ {i}) - N V _ {k} (\boldsymbol {\lambda}) \right],
$$

where $\mathbf { e } _ { \iota }$ denotes an N-vector with 1 in its i-th element and zeroes elsewhere. This result implies that when i's usage rate $\lambda _ { \iota }$ increases by e, the gain to i exceeds the loss to the rest of the incumbent. Hence, there is a pressure towards issuing more rights with a bribe arrangement.

Similarly, when $\begin{array} { r } { V _ { \cdot } ^ { \prime } ( \lambda _ { \cdot } ) < C ( \lambda ) + \sum \lambda _ { k } C ^ { \prime } ( \lambda } \end{array}$ for some i, it can be shown that retiring some of i's rights (type-2 transaction) after some sidepayment proves beneficial both to i and the rest of the users

Further, similar arguments may be employed to show that if the current allocation λ satisfies $V _ { \iota } { ' } ( \lambda _ { \iota } ) > V _ { \iota } { ' } ( \lambda _ { \iota } )$ for $i \neq j ,$ there exists a mutual interest on both sides to negotiate towards a new allocation $( \boldsymbol { \lambda } _ { t } ^ { \dagger } , \boldsymbol { \lambda } _ { t } ^ { \dagger } )$ satisfying $\lambda _ { \iota } ^ { \dagger } > \lambda _ { \iota } , \lambda _ { \iota } ^ { \dagger } + \lambda _ { \iota } ^ { \dagger }$ $= \lambda , + \lambda$ and $\bar { V _ { \scriptscriptstyle 1 } ^ { \prime } } ( \lambda _ { \scriptscriptstyle 1 } ^ { \dagger } ) \geq V _ { \scriptscriptstyle 1 } ^ { \prime } ( \lambda _ { \scriptscriptstyle 1 } ^ { \dagger } )$ . By switching the roles of i and j we conclude that the system will evolve itself until it satisfies $\mathrm { \large { \cdot } } V _ { \mathrm { \scriptsize { \cdot } } } ^ { \prime } ( \lambda _ { \iota } ) = V _ { \iota } ^ { \prime } ( \lambda _ { \iota } )$ for all $i \neq j$

## Whang

Next, we must show that no coalition formed by a subset of the whole can improve upon the socially optimal allocation. If such a coalition exists, the $c o r e ^ { 1 }$ would be empty and the desired allocation would not be attained. To prove this, suppose that a proper subset $A \subset \{ 1 , 2 , \cdots , N \}$ of the user population can improve upon the socially optimal allocation $\bigstar ^ { * }$ . Let the new allocation be denoted by $\lambda ^ { A }$ Note that $\begin{array} { r } { \lambda _ { t } ^ { A } > \bar { 0 } ; } \end{array}$ , if and only if $i \in { \cal A } .$ . To achieve the allocation the coalition must buy up all the outstanding usage rights held by those outside the coalition. The reservation price of these rights is given by $\begin{array} { r } { \sum _ { \iota \not \in \mathcal { A } } [ V _ { \iota } ( \lambda _ { \iota } ^ { * } ) - \lambda _ { \iota } ^ { * } C ( \lambda ^ { * } ) ] } \end{array}$ . For this project to be profitable, it must hold that the increase in the net value accruing to the coalition should exceed the bribe payment. That is,

$$
\sum_ {t \in A} \left[ V _ {t} \left(\lambda_ {t} ^ {A}\right) - \lambda_ {t} ^ {A} C \left(\lambda^ {A}\right) \right] - \sum_ {t \in A} \left[ V _ {t} \left(\lambda_ {t} ^ {*}\right) - \lambda_ {t} ^ {*} C \left(\lambda^ {*}\right) \right] \geq \sum_ {i \notin A} \left[ V _ {t} \left(\lambda_ {t} ^ {*}\right) - \lambda_ {t} ^ {*} C \left(\lambda^ {*}\right) \right].
$$

Equivalently,

$$
\begin{array}{l} \sum_ {t \in A} \left[ V _ {t} \big (\lambda_ {t} ^ {A} \big) - \lambda_ {t} ^ {A} C (\lambda^ {A}) \right] \geq \sum_ {t \in A} \left[ V _ {t} \big (\lambda_ {t} ^ {*} \big) - \lambda_ {t} ^ {*} C (\lambda^ {*}) \right] + \sum_ {t \notin A} \left[ V _ {t} \big (\lambda_ {t} ^ {*} \big) - \lambda_ {t} ^ {*} C (\lambda^ {*}) \right] \\ = \max _ {\lambda} \sum_ {t = 1} ^ {N} \left[ V _ {t} \big (\lambda_ {t} \big) - \lambda_ {t} C (\lambda) \right], \end{array}
$$

which contradicts the unique optimality of $\bigstar ^ { * }$ . Hence, there is no coalition that can improve upon the socially optimal allocation.

Lastly, to complete the proof, we must show that no coalition can profitably bribe other user coalitions to reduce their use. Suppose a new coalition $A ^ { \prime } \subset$ $\{ 1 , 2 , \cdots , N \}$ proposes a new allocation $\pmb { \lambda } ^ { \prime } ,$ , where there exists some nonmember i with $\lambda _ { \iota } ^ { \prime } > 0 .$ . Let $\tau _ { \iota }$ denote the bribe paid to nonmember i. Voluntary acceptance entails that $\tau _ { \prime } \geq \dot { N V } _ { \mathrm { \ell } } ( \mathtt { A } ^ { * } ) - N V ( \mathtt { A } ^ { \prime } )$ , for all $i \not \in { \cal A } ^ { \prime } .$ . Coalition $A ^ { \prime }$ strictly prefers $\mathbf { \lambda } ^ { \star }$ iff $\Sigma _ { \iota \in \boldsymbol { A } } [ N V _ { \iota } ( \lambda ^ { \cdot } ) - N \dot { V } _ { \iota } ( \lambda ^ { * } ) ] > \Sigma _ { \iota \not \in \boldsymbol { A } ^ { \prime } } \tau _ { \iota }$ . These two inequalities yield $\begin{array} { r } { \dot { \sum } _ { \iota = 1 } ^ { \tilde { N } } N V _ { \iota } ( \mathsf { A } ^ { \prime } ) > } \end{array}$ $\begin{array} { r } { \sum _ { \iota = 1 } ^ { \tilde { N } } { N V } _ { \iota } ( \lambda ^ { * } ) , } \end{array}$ , which contradicts the Pareto optimality of $\bigstar$ . This completes the proof of the theorem.

The types of transactions sufficient to achieve optimality can further be reduced to the first two $( \mathrm { i . } \mathbf { e . }$ , issuance and retirement of rights), since an exchange transaction can be emulated by a serial application of type-1 and type-2 transactions.

Suppose now that the system has reached the social optimum $\bigstar$ through the bargaining process. Let's consider agent i with $\lambda _ { t } ^ { * } > 0$ , His own valuation of the usage rate $\lambda _ { \iota } ^ { * }$ is given by $N V _ { \iota } ( \mathsf { { A } } ^ { * } ) \bar { \mathbf { \Psi } } = V _ { \iota } ( \lambda _ { \iota } ^ { * } ) - \lambda _ { \iota } ^ { * } C ( \lambda ^ { * } )$ , while the other users maximum bribe² offer to the retirement of $\lambda _ { \iota } ^ { * }$ is given by

$$
\begin{array}{l} B _ {t} \stackrel {{\text { def }}} {{=}} \sum_ {k \neq t} \left[ N V _ {k} (\boldsymbol {\lambda} _ {- t} ^ {\dagger}) - N V _ {k} (\boldsymbol {\lambda} ^ {*}) \right] \\ = \sum_ {k \neq t} \left\{\left[ V _ {k} (\lambda_ {k} ^ {\tau}) - \lambda_ {k} ^ {\dagger} C (\lambda^ {\dagger}) \right] - \left[ V _ {k} (\lambda_ {k} ^ {*}) - \lambda_ {k} ^ {*} C (\lambda^ {*}) \right] \right\}, \end{array}\tag{2.2}
$$

where ${ \sf A } _ { - \imath } ^ { \dagger } = ( { \sf A } _ { 1 } ^ { \dagger } , \cdot \mathrm {  ~ \cdot ~ } , { \sf A } _ { \imath - 1 } ^ { \dagger } , { \sf A } _ { \imath + 1 } ^ { \dagger } , \cdot \cdot \cdot , { \sf A } _ { N } ^ { \dagger } )$ solves max $\smash { _ { \lambda _ { k - 1 } } \sum _ { k \neq 1 } [ V _ { k } ( \lambda _ { k } ) - \lambda _ { k } C }$ $\textstyle ( \sum _ { j \neq i } \lambda _ { j } ) ]$ . Faced with this offer, however, agent i will find it to his interest to reject it; otherwise there is a possibility of further Pareto improvement, which contradicts the assumed optimality of $\mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } \mathbf \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda \lambda } \mathbf \mathbf { \lambda } \mathbf { \lambda } \mathbf \mathbf { \lambda } \mathbf \lambda \mathbf { \lambda } \mathbf \mathbf { \lambda \lambda } \mathbf \mathbf { \lambda \lambda } \mathbf \mathbf  \lambda \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \mathbf { } \lambda \mathbf \lambda \lambda \mathbf \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \lambda \mathbf \lambda \mathbf \lambda \lambda \mathbf \lambda \mathbf \lambda \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \mathbf \lambda \lambda \lambda \mathbf \lambda \lambda \lambda \lambda \mathbf $

Set in a real environment, the Coase markct is exposed to a variety of problems: (1) The bargaining costs may be substantial (Cheung (1978)).

(2) Free-rider or hold-out problems exist especially when the number of agents is large (Wellisz 1968),

(3) Agents in many cases do not have complete information of each other's preference, hence the bargaining process may not ensure an optimal allocation (Arrow 1979, Samuelson 1985).

(4) In the absence of a proper procedure to make an initial right assignment, the bargaining market may be infested with arbitrageurs and bargaining cost increases.³

(5) When the condition $\Sigma _ { \iota \cdot } ^ { N } \ : _ { 1 } \lambda _ { \iota } < \infty$ of Proposition 1 is not met (i.e., in a system where cach agent is given unlimíted, nontransterable usage rights), the system will stop at an overcongested state.

For these reasons, the mechanism in its pure form may find its applications where the number of agents is small and inforimation gap among agents is narrow. For example, a firm with a small number of departments sharing a mainframe computer may adopt this mechanism. A possible scenario goes as follows: The Accounting/Payroll department of a firm acquires a mini-computer to automate routine payroll processes. After the installation of the system, other departments may wish to share the system. Under these circumstances, things can be negotiated such that several departments have access to the system at some nominal fee which may marginally contribute to the fixed cost of the system. Note in this case the system is operated without any intervention of the firm-wide central planner.⁴

## 2.2. The Clarke-Groves Tax Mechanism

Several authors (Zerbe 1976, Arrow 1979 and Samuelson 1981) have recently indicated that the Coase theorem is based on an unstated assumption that al agents have perfect information about each other's preference. Absent this assumption, agents in our small economy are exposed to incentives to manipulate the

## Whang

economic system to their best advantages by distorting their preferences (the benefit function, in our context) or by controlling the externality structure. The Clarke-Groves tax mechanism is a proposal to coordinate decisions overcoming the informational asymmetry and incentive problems. The mechanism operates in the following way: first the system manager announces a charging schedule. All agents who would participate in the system report their gross benefit functions to the system manager. Based on the reports, the system manager determines the usage rate for each agent so as to maximize the net value of the system. Finally, the charge is computed according to the announced schedule.

However, since there is no way to ensure or verify that agents report truthfully, the Clarke-Groves tax is designed to induce each user to reveal his true value as a dominant strategy. Under the current setting, the tax is given by

$$
\begin{array}{l} Q _ {t} \stackrel {{\text { def }}} {{=}} \sum_ {k \neq t} \left[ N V _ {k} (\boldsymbol {\lambda} _ {- t} ^ {\dagger}) - N V _ {k} (\boldsymbol {\lambda} ^ {*}) \right] \\ = \sum_ {k \neq t} \left\{\left[ \tilde {V} _ {k} (\boldsymbol {\lambda} _ {k} ^ {\dagger}) - \boldsymbol {\lambda} _ {k} ^ {\dagger} C (\boldsymbol {\lambda} ^ {\dagger}) \right] - \left[ \tilde {V} _ {k} (\boldsymbol {\lambda} _ {k} ^ {*}) - \boldsymbol {\lambda} _ {k} ^ {*} C (\boldsymbol {\lambda} ^ {*}) \right] \right\}, \end{array}\tag{2.3}
$$

where $\bigstar$ denotes the optimal value of λ computed on the basis of the reported benefits $\tilde { \mathbf { v } } ,$ and ${ \pmb { \lambda } } _ { - } ^ { \dagger }$ , denotes the optimal value of $\mathtt { \lambda } _ { \mathtt { k } _ { - \iota } } = ( \lambda _ { 1 } , \cdot \cdot \cdot , \lambda _ { \iota - 1 } , \lambda _ { \iota + 1 } , \cdot \cdot \cdot , \lambda _ { \scriptscriptstyle N } )$ computed on the basis of the reports disregarding the report by agent i. Agent i is assigned to the usage rate $\lambda _ { \iota } ^ { * }$ and charged the amount $Q _ { \iota }$ . Note that $Q , \ b = 0$ if $\lambda _ { \prime } ^ { * } = 0 ,$

This price scheme is well known to induce the agents to report their true parameters.

Proposrrion 3. Faced with the pricing schedule Q, each agent finds it to his best interest to reveal his true beneft function.

The proof is similar to the one in Groves (1976) and omitted here.

The property that reporting one's true preference is a dominant strategy does not necessarily imply that agents will voluntarily participate in the assignment process and comply with the outcome. While an addition of a large constant to $Q _ { \imath } ,$ for example, preserves truthful reporting as the dominant strategy for each agent, no agent would voluntarily participate if the constant is made large enough. (We assume here that an agent not participating in the system gets zero payoff.) However, the proposed price scheme $\mathbf { Q }$ as it is solves the participation problem as well, which is the content of the next proposition.

PROPOsITION 4. Under the price scheme $\mathbf { Q } ,$ each agent will voluntarily participate in the system $i f$ and only if his participation helps increase the net value of the system.

PRooF. Agent i will decide to participate in the use of the system if and only if the charge does not exceed the net benefit of the system to him, or if and only if

$$
Q _ {t} = \sum_ {k \neq t} \left\{\left[ V _ {k} \left(\lambda_ {k} ^ {\dagger}\right) - \lambda_ {k} ^ {\dagger} C \left(\lambda^ {\dagger}\right) \right] - \left[ V _ {k} \left(\lambda_ {k} ^ {*}\right) - \lambda_ {k} ^ {*} C \left(\lambda^ {*}\right) \right] \right\} \leq V _ {t} \left(\lambda_ {t} ^ {*}\right) - \lambda_ {t} ^ {*} C \left(\lambda^ {*}\right).\tag{2.4}
$$

But the system wants him to participate if and only if the net value of the system with his participation is at least as large as that without him, i.e., if and only if

$$
\sum_ {k = 1} ^ {N} \left[ V _ {k} \left(\lambda_ {k} ^ {*}\right) - \lambda_ {k} ^ {*} C \left(\lambda^ {*}\right) \right] \geq \sum_ {k \neq t} \left[ V _ {k} \left(\lambda_ {k} ^ {\dagger}\right) - \lambda_ {k} ^ {\mathrm{r}} C \left(\lambda^ {\dagger}\right) \right],
$$

which is identical to (2.4). This completes the proof.

An interesting point is that the Clarke-Groves tax $Q _ { \iota }$ given by (2.3) coincides with the maximum bribe $B _ { \iota }$ (given by (2.2)) offered to agent i under the private bargaining approach. The main difference is the way :axes change hands. In the latter approach, taxes are collected from one group and given to the other, while in the Clarke-Groves mechanism, taxes are collecttd by the system manager. In the private bargaining approach, agent i currently using the system has to choose one of the two alternatives: collect $B _ { \iota }$ and quit. or stay with the system. Hence he chooses to stay if and only if the benefit of using the system equals or exceeds the bribe $B _ { \imath } .$ On the other hand, the Clarke-Groves mechanism offers two possible options for agent i to choose from: quit the system, or pay $Q _ { t } ( = B _ { t } )$ to the system and stay. Under this scheme, too, agent i decides to stay if and only if the net benefit of the system to the agent equals or exceeds the charge $B _ { \iota }$ . Therefore, agent i makes the same decision under either mechanism.

This equivalence of the Coase bribe and the Clarke-Groves tax provides an insight to the demand revealing property of the Clarke-Groves mechanism. In the Coase regime, agent / who is characterized by his value function $V _ { \iota }$ tries (through bargaining) to reach the best position available to him, which is the Pareto optimum point $\bigstar ^ { * }$ . Note that this allocation $\bigstar$ maximizes the net value of the system $\begin{array} { r } { \sum _ { k = 1 } ^ { \tilde { N } } N V _ { k } ( \mathbf { \lambda } ) } \end{array}$ , and also $\Sigma _ { k - 1 } ^ { N } [ N V _ { k } ( { \bf \vec { n } } ) - N V _ { k } ( \pmb { \lambda } _ { - , } ^ { \dag } ) ] = N V _ { \iota } ( \pmb { \lambda } ) - B _ { \iota } ( \pmb { \lambda } )$ which is the differential between his net benefit and the maximum bribe tendered to him. This also implies that $\bigstar ^ { * }$ maximizes $N V _ { \iota } ( \lambda ) \ \textrm { - } \mathscr { Q } _ { \iota } ( \lambda )$ . By guaranteeing to return the best bargaining outcome, therefore, the Clarke-Groves tax mechanism places agent i in a position to prefer the allocation $\bigstar ^ { * }$ , which is attainable by revealing his true preference. In the sense, the Clarke-Groves mechanism under the current setting is an outcome of the Revelation Principle (Myerson (1979)) applied to the Coase market.

Note that the after-tax net value $\nu _ { t } ^ { C G }$ to agent i under the Clarke-Groves tax mechanism is given by

$$
v _ {i} ^ {C G} \stackrel {\text { def }} {=} N V _ {i} \left(\lambda_ {i} ^ {*}\right) - Q _ {i} \left(\boldsymbol {\lambda} ^ {*}\right) = N V \left(\{1, 2, \dots , N \}\right) - N V \left(\{1, 2, \dots , N \} - \{i \}\right),
$$

where $N V ( S ) { \overset { \underset { \mathrm { d e f } } { } } { = } } \operatorname* { m a x } _ { { \boldsymbol { \lambda } } } \Sigma _ { k \in S } [ V _ { k } ( \lambda _ { k } ) - \lambda _ { k } C ( { \boldsymbol { \lambda } } ) ] .$ for $S \subset \{ 1 , 2 , \ldots , N \}$ . This can be interpreted as agent $i \mathbf { \ ' } _ { \mathbf { S } }$ dividend associated with the cooperative game of system sharing. Interestingly, the expression is an instance of probabilistic value (Loehman and Whinston $1 9 7 6 ,$ and Weber 1988) that is a weighted sum of marginal contributions to different coalitions, $\begin{array} { r } { \mathrm { i . e . , } \ \nu _ { \iota } = \sum _ { S \subset \{ 1 , \ ^ { \prime } , \quad \nu \} } p _ { S } [ N V ( S ) - N V ( S - i ) ] } \end{array}$ with $\begin{array} { r l } { \sum _ { S \subset \{ 1 , 2 , \} } } & { { } , N \} p _ { \mathord { \Game } } = 1 . \mathrm { ~ A ~ } } \end{array}$ specific choice of the probability function $p _ { S }$ leads to a different dividend sharing scheme: the current mechanism is derived by having $p _ { \{ 1 , 2 , . . . \ , N \} } = 1$ , while the choice of $p _ { S } = ( | S | - 1 ) ! ( N - | S | ) ! / N !$ and $p _ { S } = 1 / 2 ^ { N - 1 }$ respectively lead to the Shapley value and the Banzhaf value.

In an organization each department is asked to report its future demand of computer resources. This report forms a basis for making systems acquisition decisions and allocating resources to departments in the form of computer budget. Costs associated with acquisition and operation of the system are fully or partially absorbed by user departments following a predetermined taxing scheme. This process can be viewed as following the essence of the Clarke-Groves tax mechanism.

Superior as it is in its capabilities of aligning individual incentives under informational asymmetry, this demand revealing process has several shortcomings: (1) The reporting processes will incur significant communication costs

(2) There is no guarantee that the budget will be balanced (Groves and Ledyard 1977), so that this approach is unacceptable in an environment (e.g., a systemsharing cooperative) where the budget must be balanced.

(3) It is vulnerable to coalitions (Groves and Ledyard 1977, Green and Laffont 1976).

(4) The charging scheme is not intuitively clear or user-friendly (Bohm 1984).

(5) Agents are undermotivated to gather information (Tideman and Tullock 1977).

(6) It is a one-shot allocation process and implicitly assumes that each agent has full information about his future demand of the system at the time of the allocation. Typically, this is not the case in practice, hence some additional provision of adjustment processes is required.

(7) When there exist budget constraints (unlike our model), some user departments may go bankrupt when the tax is assessed.

(8) When the proposal is to change the existing system to a new one, the Clarke-Groves allocation is not necessarily a Pareto improvement from the statusquo. (Note that Proposition 4 shows that the allocation is a Pareto improvement from the null system. Hence, the proposition holds only for a newly installed system.)

## 2.3 Allocation Attainable through Nash Equilibria

This alternative way of implementing the optimal allocation is based on a Nash equilibrium concept. The system manager announces a charging schedule S. Next, agents choose their usage rates in a Nash equilibrium strategy. The system manager charges each agent based on the announced charging schedule and the usage-rate vector λ' observed, i.e., $S = S ( { \pmb \lambda } ^ { \prime } )$ ). An allocation λ' is an (Nash) equilibrium if, for each $i = 1 , 2 , \ldots , N ,$

$$
N V _ {i} \left(\lambda^ {\prime}\right) - S _ {i} \left(\lambda^ {\prime}\right) \geq N V _ {i} \left(\lambda_ {- t} ^ {\prime}, \lambda_ {t}\right) - S _ {i} \left(\lambda_ {- t} ^ {\prime}, \lambda_ {i}\right), \quad \text { for   all } \quad \lambda_ {t} \in [ 0, \infty),
$$

where $\mathtt { \mathtt { A } _ { - \iota } } = ( \mathtt { \lambda } _ { 1 } , \mathtt { \ldots } , \mathtt { \lambda } _ { \iota - 1 } , \mathtt { \lambda } _ { i + 1 } , \mathtt { \ldots } , \mathtt { \lambda } _ { \Lambda } ) .$ . That is, each agent chooses his usage rate to maximize his payoff, taking other agents' usage decisions as given. A charging schedule is efficient if it yields the socially optimal allocation as an equilibrium. Note that nonparticipation $( \lambda _ { \iota } = 0 )$ is one of the competing strategies available to each agent in the definition of the equilibrium, hence efficiency requires that each agent not only produce the socially optimal usage rate, but voluntarily participate if and only if it makes a nonnegative contribution to the net value of the system, (Recall that Propositions 3 and 4 demonstrate analogous properties of the Clarke-Groves tax Q.)

The next proposition introduces an efficient charging schedule in this setting

PROPOSITION 5. Let

$$
S _ {i} (\boldsymbol {\lambda}) = \sum_ {j \neq i} \lambda_ {j} \left[ C \left(\sum_ {k = 1} ^ {N} \lambda_ {k}\right) - C \left(\sum_ {k \neq i} \lambda_ {k}\right) \right],\tag{2.5}
$$

where λ denotes the observed arrival rates at equilibrium. Then, S is efficient

ProoF. Straightforward by comparing the first-order conditions of the social and agent $i \ ' \mathbf { s }$ objectives. To show that the schedule resolves the participation problem, we use the fact that $S _ { \iota }$ is right-continuous at $\lambda _ { \iota } = 0$ for each i.

Interestingly, the charging schedule S can be terived from the Clarke-Groves tax $Q$ when the impact of agent $i ^ { \prime } s$ usage decision or. others' usage rates is ignored $( \mathrm { i . e . }$ $\pmb { \lambda } _ { - 1 } ^ { \dag } = \pmb { \lambda } _ { - i } ^ { * }$ in (2.2)'s notation).

Note that the optimal price schedule depends on the joint decisions made by the agents. In building a strategy, therefore, each agent is required to predict what decisions others will make. While various modlels of Nash equilibrium have been studied in the literature (e.g., Meade 1952, Wellisz 1964, and Whitcomb 1972), Davis and Whinston (1962) point out several (oncerns about using the (nondomi nant) Nash equilibrium criterion:

(1) Equilibrium may not exist under certain settings,

(2) Equilibrium may exist in multiplicity, so tnat it is not clear which of them wil be chosen by the agents

(3) Computation of the equilibrium and its corresponding charges may be a nontrivial task.

Further drawbacks of this approach are:

(4) This approach requires that each agent, but not necessarily the manager have complete information on the other agents' benefit functions.5 This is an unrealistic assumption; each agent typically possesses some private information on his unique business setting. Further, it is unlikely that only the system manager is isolated from the public information. If, instead, the system manager has also full information, why bother to use pricing at all instead of allocating the resources administratively?

(5) The price schedule is left indeterminate until all the decisions by agents are made and observed. This uncertainty in price schedule reduces its appeal to the users of the system.

A variety of cost sharing schemes of the computer expenditures commonly observed in practice are strongly reminiscent of this mechanism, even if the price schedule actually used does not exactly follow its theoretical counterpart.

## 3. A Continuum Economy

This section develops a large-scale version of the model discussed in the previous section. Consider a large economy with a continuum of risk-neutral agents (i.e., individual users) indexed by $\lambda \in \bar { R } ^ { + }$ . Agent λ extracts the gross benefit of $\nu _ { \lambda }$ each time he uses the system.6 The value $\nu _ { \lambda }$ is only known to agent λ, and not to the system manager. The latter, however, has access to the aggregate distribution of gross benefit $\nu _ { \lambda } .$ . The distribution of $\nu _ { \lambda }$ is represented by a downward sloping marginal value function MV(λ). This continuum model is an abstraction of an economy in which there are a large number of agents using the system at a small rate. The net value of the system, when the system is used by agents in [0, λ] at an infinitesimal rate each, is given by $\begin{array} { r } { \int _ { 0 } ^ { \lambda } \left[ M \dot { V } ( x ) - C ( \lambda ) \right] d \dot { x } . } \end{array}$ Hence, the net-value-maximizing λ must satisfy the following first-order condition (assuming it is an interior solution)

$$
M V (\lambda) - C (\lambda) - \lambda \frac {d C}{d \lambda} = 0.\tag{3.1}
$$

Again our concern is how the system manager in lack of full information can implement the optimal allocation. We discuss two approaches to this problem: (1) job-by-job pricing, which charges a determinate price for each use of the system, and (2) an allocation scheme based on an exchange market

## 3.1. Job-by-Job Pricing

According to this scheme, the system manager posts a price and each agent pays the price for each use. Agent λ derives from each use of the system the net payoff of $\left[ M V ( \lambda ) - C ( \lambda ) - p \right]$ , where p is the price charged for each use of the system. For a marginal user (λ) of the system, it holds that

$$
M V (\lambda) - C (\lambda) - p = 0.\tag{3.2}
$$

This is a demand relationship that depicts the relationship between the price p and its resulting usage rate λ. The optimal price $p ^ { * }$ that maximizes the net value of the system is obtained by comparing (3.1) and (3.2) to give the following result.

PRoposiTiON 6. (Mendelson 1985) The price that achieves the optimal allocation of the system in the current regime is given by

$$
p ^ {*} = \lambda^ {*} \frac {d C}{d \lambda} \Bigg | _ {\lambda = \lambda^ {*}},\tag{3.3}
$$

where $\lambda ^ { * }$ solves (3.1).

Note that this optimal price $p ^ { * }$ is determinate—meaning that all the parameters of the price schedule are predetermined other than the user's usage decision. This determinate price scheme seems closest to the remedy Pigou proposed for resolving the divergence of individual interests from the social optimum in the presence of externalities.

In the previous section it was demonstrated that the maximum bribe, $B _ { \imath } ,$ , to agent i under the Coase mechanism, the Clarke-Groves tax $Q _ { \imath } ,$ and the Nash equilibrium charge $S _ { \ell }$ are counterparts of each other. We now investigate the relationship of the price $p ^ { * }$ to those of the preceding mechanisms.

Going back to the Nash price scheme S of the preceding section, let's suppose that agent i requires a small usage rate $\Delta \lambda _ { \iota ^ { \prime } }$ Then we have

$$
\lim _ {\Delta \lambda_ {t} \rightarrow 0 ^ {+}} \frac {S _ {t}}{\Delta \lambda_ {t}} \Bigg | _ {\lambda = \lambda^ {*}} = \lim _ {\Delta \lambda_ {t} \rightarrow 0 ^ {+}} \sum_ {j \neq t} \lambda_ {j} ^ {*} \frac {C \left(\Sigma_ {k = 1} ^ {N} \lambda_ {k}\right) - C \left(\Sigma_ {k \neq t} \lambda_ {k}\right)}{\Delta \lambda_ {t}} \Bigg | _ {\lambda = \lambda^ {*}} = \lambda^ {*} \frac {d C}{d \lambda_ {t}} \Bigg | _ {\lambda = \lambda^ {*}},\tag{3.4}
$$

which coincides with Mendelson's job-by-job price $\boldsymbol { p } ^ { * }$ . That is, the Nash equilibrium charge rate (per use) to user i approaches Mendelson's price $p ^ { * }$ as i's usage rate tends to zero.

The relationship between Mendelson's job-by-job price and the Clarke-Groves tax (or the Coase bribe) can also be understood through the relationship between the Nash equilibrium charge and the Clarke-Groves tax (see §2.3): Mendelson's price is derivable from the Clarke-Groves tax by letting i's rate converge to zero while keeping the total usage rate constant, $. \mathrm { e } . , \ \Delta \lambda _ { i } \to 0$ and $\Sigma _ { k } \Delta \lambda _ { k } = \lambda ^ { * }$ . In summary, Mendelson's job-by-job price is a limit ng version of the Clarke-Groves tax, the Coase bribe or the Nash equulibrium charge.

The determinate Pigouvian tax can be found to optimally allocate the system when the following conditions are met: (1) the system manager has access to aggregate-level information about the economv (.e., the demand function of the system and congestion cost) in order to compute the optimal tax; and (2) the economy is large and each agent is a small player in the system without any power to manipulate the system. Examples of the Pigouvian tax applied to public goods include various tolls (e.g., bridges, tunnels, highways, parks and parking lots) and license fees (e.g., fishing or hunting). Perhaps this mechanism is the most popular type of computer chargeback system in an organization. According to this policy, fixed rates are charged for use of CPU, main memoiy, disk space, communication line, file servers, and laser printers. Charging rates may be a function of intensity of use, time of the day, or job priorities. The manager must keep track of the demand patterns to compute the optimal price

## 3.2. Allocation through Exchange Markets

This approach is basically a continuum-economy version of the Coase mechanism. The system manager makes an initial allocation of usage rights, which may not be optimal. A maiket is formed in which the rights are traded among agents. With an infinite number of agents in this continuum economy, those types of transactions (type-1 and -2 transactions in §2.1) requiring approvals by the whole incumbent users cannot be processed in the market. This implies that the system manager has to determine the optimal number (λ\*) of rights to be issued and the

## Whang

market is expected to process only exchange (type-3) transactions. At equilibrium the right to use the system for a unit of time is traded at a single price $q ^ { \dagger } .$ . To agent λ who is faced with the price $\boldsymbol { q } ^ { \dagger } ,$ , the optimal strategy is: use the system if and only if $M V ( \lambda ) \geq q ^ { \dagger } + C ( \lambda ^ { * } )$ . Hence agents’ decision rule $D ( \boldsymbol { \lambda } )$ can be written as $D ;$ $R ^ { + } \to \{ 0 , 1 \} - { \mathbf a }$ mapping from an agent index to a binary value (1 for participation and 0 otherwise). Since $D ( \cdot )$ is nonincreasing and there is a total of $\lambda ^ { * }$ usage rate outstanding, agent $\lambda ^ { * }$ is the marginal user of the system satisfying

$$
M V (\lambda^ {*}) = q ^ {\dagger} + C (\lambda^ {*}).\tag{3.5}
$$

Comparing this with equation (3.1) and noting the optimality of $\lambda ^ { * } ,$ , we find

$$
q ^ {\dagger} = \lambda^ {*} \frac {d C}{d \lambda} \Bigg | _ {\lambda = \lambda^ {*}} = p ^ {*},
$$

which is Mendelson's job-by-job price. This gives the following proposition.

PRoposiTioN 7. Suppose the system manager in this regime makes an initial allocation of the system such that the total usage rate is socially optimal. Then the system is optimally allocated through the exchange process and the market price of the usage right equals Mendelson's job-by-job price.

An organization with a large number of users may use this policy by issuing marketable “computer dollars"such that the total utilization of the system is kept less than, say, 60%. Every student in a college, for example, is given a certain amount of computer money. When a student runs out of the budget, he may purchase computer dollars at the going rate from another student who has an excess of it, or directly from the computer center.

This principle was, or is currently, adopted in the United States for the allocations of electromagnetic spectrums (Nelson and Noll 1985), airport time slots (Regulation 1982) and pollution rights (Yandle 1978). In each of these cases the system manager (the Federal Communications Commission, the Federal Aviation Administration and the Environmental Protection Agency, respectively) determínes the maximum number of usage rights which are assigned to users in one way or another. Then these rights are traded in a market (typically under certain constraints).

The determination of the optimal number of outstanding rights may be a problem. However, at least in principle the system manager can adjust her decision over a period by reissuing or buying back rights in the market. For this reason, the manager is, and should be, sensitive to a large transaction: For example, the center reserves the right to change its ongoing exchange rate of computer dollars if the purchasing volume is more than a certain amount. This active role of the system manager differentiates this mechanism from the pure Coase's approach. This simple policy change relaxes most of the difficulties faced by the Coase market. On the other hand, the transaction costs involved in matching sellers and buyers are usually higher than in the job-by-job pricing mechanism where users are directly charged for using the system.

## 4. Conclusion

We have studied five alternative mechanisms under two different models that would achieve socially optimal allocations of congestion-prone computer resources. An important implication of the results is that optimality of a certain mechanism is ensured only in one of the two——small or large---economies. Many debates over the validity of the Pigouvian tradition or the private bargaining approach stem from employing a wrong model in discussions of a specific mechanism. Coase (1960), for example, criticizes the Pigouvian tradition in its roots? by suggesting a series of cases each depicting a small economy (in which the Pigouvian tax is not doing well). The Coase's invariance proposition in turn has been challenged by several authors8 who apply the principle to a large economy: e.g., Will drivers on highways negotiate to reach an optimal traffic level? Will drivers and pedestrians seek bribe arrangements to minimize car accidents? Our alternative models suggest a set of conditions under which one is superior to the other.

A key result of this paper is the equivalence of bribes and prices associated with various mechanisms. Mendelson's job-by-job price $p ^ { * }$ which is identical to the exchange market price $q ^ { \dagger }$ is a limiting version of the Nash equilibrium charge $\mathbf { s } ,$ which in its turn can be derived from the Clarke-Groves tax Q by ignoring the effect of one's usage rate decision on those of others. Moreover, the Clarke-Groves tax Q matches with the maximum bribe bid B from the rest of the users in the Coase cconomy, which implies that the Clarke-Groves mechanism is in fact a visible-hand version of the bargaining approach-—thereby mitigating chronic problems of the private bargaining approach such .ts free-rider or hold-out problems.

The main differences among these alternative schemes, therefore, lie with the logistics in which each one of them is operated. This means that the economic structure, informational feasibility and transaction costs involved in its implementation play a key role in the design of the system allocation.º These factors clearly vary from situation to situation and are extremely hard to quantify. It is perhaps on this account that problems of systems design are regarded as not theoretical but empirical ones (Calabresi 1968). Nonetheless, we have benefitted from the theoretical framework we developed by seeking a positive basis for understanding various system allocations commonly found in practice.

We have excluded from our discussions some feasible mechanisms. One is to administratively allocate the resources without using any pricing or sidepayment arrangements. This may achieve the social optimum if the system manager has complete information of the agents' benefit functions. In small organizations, we find, the system manager has a wide latitude of deciding how much resource to allocate to which job in which priority order. While this approach is economically efficient and saves the (nontrivial) cost of operating an accounting system, some undesirable non-economical issues (such as fairness, power and politics) may be raised.

Another allocation method which we have excluded from our discussion is a bidding mechanism. In a static setting where blocks of CPU time are allocated, this mechanism has characteristics similar to the Clarke-Groves mechanism, as is shown by Loeb (1977). A bidding mechanism may also be employed in a dynamic setting where computer resources are traded at run time among multiple tasks According to Walspurger et al.'s (1989) experiment with the second-price sealed-bid auction system called Spawn, the market price remains relatively steady in equilibrium. A question that arises is: is there any advantage of such a dynamic bidding system over job-by-job pricing? Its answer depends on the system manager's capability of acquiring demand information. When the manager is able to keep track of the information, the job-by-job pricing system will attain the same efficiency as the dynamic bidding system. Otherwise, the latter is superior since it polls private information and reflects it into the allocation process. Yet, the resource consumption incurred by operating a bidding process must be traded off with its advantage. Accordingly, the bidding mechanism may be preferred when the environment is changing fast in a nonrepetitive way (since the information gap between the users and the system manager can be reduced by letting users reveal their demands) and expensive resources are involved (since inefficiency is costly)

It is often argued that with the drop in CPU costs, transfer pricing of computer services has become less important and will ultimately be phased out in favor of allocation to overhead. In response to this argument, consider Mendelson's job-byjob price in the large economy, which is given by $p ^ { * } = \lambda ^ { * } ( d C / d \lambda ) \vert _ { \lambda = \lambda ^ { * } }$ . It is noted that both the optimal price $p ^ { * }$ and the optimal arrival rate $\lambda ^ { * }$ are dependent on the capacity of the system which we have so far taken as given; the optimal arrival rate $\lambda ^ { * }$ increases and the optimal price $p ^ { * }$ decreases in capacity. That $\mathbf { i s } ,$ a system with large capacity should encourage more jobs to be processed by lowering the unit price. A crucial observation here is that even if the unit price may become small, the total charge $\lambda ^ { * } p ^ { * }$ may remain significant. Further, we should note that the system demand is also on the rise over time, by the introduction of new domains of applications such as simulations, DBMSs, LANs, graphics, point-of-sale systems, and expert systems. The above arguments suggest the following scenario: As the capacity cost drops, the system manager will purchase a larger system to run more applications which become cost-justifiable. The per-MIPS charge of the system will go down, but the pool of applications running on the system will grow larger. To protect the system from overcongestion and discourage low-valued tasks from the system, some way of allocating the computer resources may still be required. From this perspective, therefore, it is not immediate to predict the phase-out of chargeback systems as the future trend.

In designing an allocation system for an organization, the system designer should assess the costs and advantages of each mechanism, and develop a system that minimizes the transaction costs under informational and other environmental constraints. Often, a mixture of mechanisms is employed in an organization to complement the weaknesses of each other. In a university, for example, a certain amount of computer money may be allocated to each college following the spirit of the Clarke-Groves mechanism. Since no college can accurately forecast its yearly demand, an internal market is opened where the computer dollars are traded among the colleges with updated information. On the other hand, each college may use job-by-job pricing in allocating the budgeted computer resources to its students.

There are several research issues that are closely related to the present work. One is to analyze the long-run problem in which capacity as well as allocation must be determined. Of particular interest is the problem when the system manager does not have complete knowledge of the users’ demand functions (see Whang 1989). How can the manager control the users incentives to exaggerate their demands in order to enjoy a congestion-free system? Another interesting line of research is to survey actual implementations ot allocation systems and try to gain further insights to alternative allocation mechanisms.

Acknowledgements. This paper is based on a chapter of my Ph.D. thesis completed at the University of Rochester. I wish to thank my thesis advisor, Haim Mendelson, for many helpful comments and encouragement. Also I am most grateful to anonymous referees and the Associate Editor, Andrew Whinston, who were intrumental in fixing the incomplete proof of Proposition 2, enriching the content of discussions. and refining the presentation of the earlier version. Any remaining errors are mine.\*

\*Andrew B Whinston, Associate Editor This paper was received on July 20, 1988 and has been with the author 1½2 months for 1 revision

## References

Alchian. A. A. and W. A Allen, Exchange and Prodution, 3rd Edition, Wadsworth Publishing Company, Belmont, CA, 1983.

Arrow, K, “The Property Rights Doctrine and Demand Revelation under Incomplete Information," in: M. J Boskin, (Ed), Economics and Human Welfare, Academic Press, New York, 1979

Bohm, P., “Revealing Demund for an Actual Public Good " J. Public Economucs, 24 (1984), 135–151.

Calabresi, G., “Transaction Costs, Resources Allocation and Liability Rules—A Comment," J. Law and Economucs, 11 (1968), 67–73.

Cheung, S. N. S., The Myth of Social Cost, The Institute of Economic Affairs, 1978.

Clarke, E. H., “Multipart Pricing of Public Goods," Publıc Chorce, 11 (1971), 17–33.

, Demand Revelation and the Provision of Pubic Goods, Ballinger Publishing Company, Cambrıdge, MA, 1980

Coase, R., “The Problem ot Social Cost," J. Law and Ecoromıcs, 3 (1960), 1–44.

d'Aspremont, C. and L. A. Gerard-Varet, “"On Bayesian Incentive Compatible Mechanisms," in Aggregatton and Revelatton of Preferences, J-J Laffont (Ed ), North-Holland Publishing Company, Amsterdam, 1979.

Davis, O. A. and A. B. Whinston, "Externalities, Welfare, and the Theory of Games," J. Political Economy, 70 (1962), 241- 262.

Green, J. and J-J Laffont, “On Coalition Incentive Compatıbilty," Discussion Paper, No. 497, Harvard Institute of Economic Research, 1976

Grether, D., M. Isaac and C. Plott, "The Allocation of Landing Rights by Unanimity among Competitors," Amer. Economuc Rev , 71 (1981), 166–17

Groves, T., “Information, Incentives and the Internalization of Production Externalities," in Theory and Measurement of Economt Externalttes, S. A. Y. Lin (I:d.), Academıc Press, New York, 1976.

and J. Ledyard,  Some Limitation of Demand Revealing Processes," Publc Choice, 29, 2 (1977), 107–124

and M. Loeb, “Incentives and Public Inputs," J Publu Economucs, 4 (1975), 211–226.

Holderness, C. G., "A Legal Foundation for Exchange," J. Legal Studıes, 14 (1985), 321–344.

Roberts, Kevin, “The Characterization of Implementable Choice Rules," in Aggregation and Revelation of Preferences, J-J Laffont (Ed.), North-Holland Publishing Company, Amsterdam, 1979.

## Whang

Holderness, C. G., “The Assignment of Rights, Income Effects, and the Allocation of Resources," Working Paper, W. E. Simon School of Business Administration, University of Rochester, 1987.

Hurwicz, L., “Optimality and Informational Efficiency in Resource Allocation Processes," in Mathematical Methods in the Social Sciences, K. Arrow, S. Karlin and P. Suppe (Eds.), Stanford University; Stanford, CA, 1959.

“Outcome Functions Yielding Walrasian and Lindahl Allocations at Nash Equilibrium Points," Rev. Economic Studies, (1976), 217–225.

Kleinrock, L., Communication Nets, Dover, New York, 1964

, Queueing Systems: Vol. II Computer Applications, John Wiley and Sons, New York, 1976.

Lazowska, E., J. Zahorjan, G. S. Graham, and K. C. Sevcik, Quantitatıve System Performance: Computer System Analysis Using Queueing Network Models, Prentice-Hall, Englewood Cliffs, NJ, 1984

Libecap, G. D. and S. N. Wiggins, “Contractual Responses to the Common Pool: Prorationing of Crude Oil Production," Amer. Economıc Rev. (1984), 87–98.

Lin, S. A. Y., "Introduction," Theory and Measurement of Economic Externalties, Academic Press, New York, 1976.

Loeb, M., "Alternative Versions of the Demand-Revealing Process," Publc Choice, 14, (1977), 15–26

Loehman, E. T. and A. B. Whinston, "A Generalized Cost Allocation Scheme," Theory and Measurement of Economic Externalties, Academic Press, New York, 1976, 87–101

Meade, J. E., “External Economies and Diseconomies in a Competitive Situation," Economic J., 62 (1952), 312–321.

Mendelson, H., “Pricing Computer Services: Queueing Effects," Comm. ACM, 28, 3(1985), 312–321

and S. Whang, “Optimal Incentive-Compatible Priority Pricing for the M/M/1 Queue," Oper. Res., (1989) forthcoming.

Morrison, S. A., “The Equity and Efficiency of Runway Pricing," J. Public Economıcs, 34 (1987), 45–60

Myerson, R., “Incentive-Compatibility and the Bargaining Problem,"Econometrica, 47 (1979), 61–74

Naor, P., "On the Regulation of Queue Size by Levying Tolles," Econometrica, 37, (1969), 15–24.

Nelson, F. and R. Noll, “Policymakers' Preferences for Alternative Allocations of the Broadcast Spectrum," in Antitrust and Regulation, F. M. Fısher (Ed.), 1985.

Pigou, A. C., The Economics of Welfare, First Edition, Macmillan, London, 1920.

Regulation, Sept.-Oct., Airline Competition and the Slot Market, (September-October 1982), 8–10

Samuelson W., “A Comment on the Coase Theorem," in Game-theoretic Models of Bargaining, A. Roth (Ed.), Cambridge University Press, London, 1985.

Sauer, C. H. and K. M. Chandy, Computer Systems Performance Modeling, Prentice-Hall, Englewood Cliffs, NJ, 1981.

Tanenbaum, A. S., Computer Networks, Prentice-Hall, Englewood Cliffs, NJ, 1981.

Tideman, T. N. and G. Tullock, “Some Limits of Demand Revealing Processes: Comment," Public Choice, 29, 2 (1977), 125–128.

Vickrey, W., “Counterspeculation, Auction and Competitive Sealed Tenders," J. Finance, 16 (1961) 8-37.

Waldspurger, C., T. Hogg, B. Huberman, J. Kephart, and S. Stornetta, “Dynamics of Computation Group," Working paper, Xerox Palo Alto Center, 1989.

Weber, R. J., “Probabilistic Values for Games," The Shapley Value, A. Roth (Ed.), Cambridge University Press, London, 1988, 101–120.

Wellisz, S., “On the External Diseconomies and the Government-Assisted Invisible Hand," Economuca, (1964), 345–362.

Whang, S., "Pricing Computer Services. Incentive, Information and Queueing Effects," unpublished dissertation, W. E. Simon Graduate School of Business Administration, University of Rochester, 1988.

"Cost Allocation Revisited: An Optimality Result," Management Sct., 35, 10 (1989), 1264-1273

Whitcomb, D. F., Externalities and Welfare, Columbia University Press, New York, 1972.

Yandle, B., “The Emerging Market in Air Pollution Rights, Regulation," (1978), 21–29.

Zerbe, R. O., “The Problem of Social Cost: Fifteen Years Later," in Theory and Measurement of Economic Externalities, S. A. Y. Lin (Ed.), Academic Press, New York, 1976.
