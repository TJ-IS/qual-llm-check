---
otero_id: 26684
otero_key: "N5TF662C"
title: "Controlling Information System Departments in the Presence of Cost Information Asymmetry"
authors: "Eric T. G. Wang; Terry Barron"
year: "1995"
journal: "Information Systems Research"
doi: "10.1287/isre.6.1.24"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/N5TF662C/fulltext/images/4ea5c114e98cce07c3e867f0b9abc6e6e366872246c679fbc69aa0f6dc190438.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Controlling Information System Departments in the Presence of Cost Information Asymmetry

Eric T. G. Wang, Terry Barron,

## To cite this article:

Eric T. G. Wang, Terry Barron, (1995) Controlling Information System Departments in the Presence of Cost Information Asymmetry. Information Systems Research 6(1):24-50. http://dx.doi.org/10.1287/isre.6.1.24

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1995 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/N5TF662C/fulltext/images/627046e2e8a04e063b08338610b4b3459c28116cce2034a6f86f350ebf6fc30a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Controlling Information System Departments in the Presence of Cost Information Asymmetry

Eric T. G. Wang Department of Information Management

School of Management

Nattonal Central University

Chung-Li, Tarwan 32054

Republic of Chuna

Terry Barron

William E Sumon Graduate School of Busıness Adminıstration

U niversity of Rochester

Rochester, New York 14627

The control of an information systems (IS) department is studied when its manager has private information about the department's cost and has objectives which may differ from those of the organization. The computing resource is represented by a queueing model, and it is assumed there is no access to external information processing markets by either users or the IS department. A mechanism design approach is used. We derive conditions that the optimal mechanism must satisfy; the first-order conditions of the full-information problem generalize in a clear way with the virtual marginal cost replacing the full information marginal capacity cost. The consequences of the information asymmetry include reduced capacity, arrival rate and utilization rate, and higher prices and mean waiting time compared to the full-information solution. Thus the organization suffers losses due not only to the IS manager's informational rent, but also to the opportunity cost of jobs not served. The revelation principle guarantees that the resulting mechanism is at least as good as a profit center, as well as outperforming any other centralized method of control. The mechanism design approach is also shown to be robust with respect to uncertainty on the part of the central management about the degree of incentive conflict with the IS manager. An example and numerical results give some feeling for the magnitudes of the effects, and managerial implications are also discussed. The paper also serves to illustrate the application of mechanism design to an IS problem; we briefly discuss other promising IS applications of this important methodology.

Management of intormation systems-—Information asymmetry—Mechanism design—-Capacity—C ost center—Profit center

## 1. Introduction

management due to its rigorous modeling of delay costs, the most important short-run IS costs. That work has been generalized in a number of subsequent papers, such as Dewan and Mendelson (1990) and Whang (1990). However, to date in such research the IS manager is cither assumed to behave as a team member with the central management or is simply ignored, even though it is well-recognized that IS professionals are often strongly motivated to behave otherwise. This paper complements previous research in an important way by formally modeling, using a mechanism design approach, the information asymmetry and objective conflicts that can be expected to exist between the IS manager and the central management. Specifically, we assume the IS manager is motivated by “professionalism" (see below) and has private information about the cost of operating her department. By combining mechanism design with a queueing model of an information system to capture congestion costs, we are able to characterize the mechanism as a generalization of Mendelson's (1985) solution, show the superiority of a cost center over a profit center in this setting, derive a number of managerial implications, and provide a foundation for rigorously addressing other IS management problems. Ihe paper also serves to illustrate the application of mechanism design to an important IS problem. We briefly discuss other promising IS applications of this important methodology in §5.

Professionalism refers to the desire of IS professionals to learn state-of-the-art information technologies to a greater extent than is organizationally beneficial, since such knowledge is often a major factor determining their job market value (Mendelson (1994) discusses this and other types of IS management problems; also see Kaplan and Atkinson (1989), p. 531). Professionalism may therefore motivate IS staff to acquire software and hardware that are not justified by organizational net-value maximization if such decisions are left to them, putting them in conflict with central management. Furthermore, the IS staff, especially the IS manager, are usually the delegated experts specializing in acquiring information about computer technologies and the system operating environment, and are therefore much better informed on these issues than anyone else in the organization. As a result of this informational decentralization and asymmetry, the IS manager might misrepresent her private information if doing so will support her professionalism tendencies. Given these incentive and informational problems, the central management will seek to design a set of performance criteria and decision rules which restructure the IS manager's objective function, and thereby reduce or eliminate the informational rent that she can command. The approach to the problem used here is to design a mechanism to induce the manager to reveal her private information truthfully by self-selecting actions that maximize her utility (Fudenberg and Tirole 1991, ch. 7).

The plan of the paper is as follows. Section 2.1 briefly reviews the basic queueing model introduced by Mendelson (1985), and some basic concepts of mechanism design are discussed in §2.2. In §3, we study the possibility of achieving net value maximization (full information) by designing an incentive compatible mechanism when only the IS manager possesses private (perfect) information about a “technological" parameter of the cost function of operating an information system. The distortion of the central management's decision is fully explored through a specific example in §4. Section 5 contains the concluding remarks and future research directions. Some results for the case where the central management is uncertain about the IS manager's utility function are given in Appendix B.

## 2. Preliminaries

## 2.1. The Queueing Model

We begin with the queueing model of an information system introduced by Mendelson (1985).' Let λ be the average arrival rate of transactions (jobs) to the computer system, where the arrival process is assumed to be Poisson. V(λ) is a bounded real-valued function which denotes the expected gross value (per unit of time) of the computer service when the job arrival rate is λ. $V ( \lambda )$ is assumed to be twice continuously differentiable, strictly concave over $\mathcal { R } _ { + } , \mu$ denotes the capacity (the average service rate) of the computer system; the distribution of service times is not restricted. For $( \lambda , \mu ) \in \mathcal { R } _ { + } ^ { 2 }$ , the mean waiting time for a job to be completed is denoted by $W ( \lambda$ $\mu )$ which is twice continuously differentiable in both arguments with partials of constant signs: $W _ { \lambda } > 0 , W _ { \lambda \lambda } > 0 . W _ { \mu } < 0 , W _ { \mu \mu } > 0 .$ , and ${ \cal W } _ { \lambda \mu } ^ { \prime } = { \cal W } _ { \mu \lambda } < 0 .$ . These behavioral properties of the mean job waiting time are satisfied by a variety of single server queueing systems such as $M / M / \mathrm { ~ l ~ }$ and $M / G / 1$ . We further assume that the users delay cost per unit of time for all jobs, v, is constant.

The IS department's cost to operate a system with “effective" capacity $\mu$ is denoted by $C ( \mu , \theta )$ . This cost is assumed to depend on the quality of the staff and the ability of the manager of the IS department, which are summarized by the cost parameter, θ. $C ( \mu , \theta )$ is assumed increasing in both $\pmb { \mu }$ and θ and twice continuously differentiable A higher θ represents a lower quality of department, so it will cost the organization more to operate a given capacity. Depending on the problem that we are interested in, this cost can have either of two interpretations: (1) the cost of achieving a particular level of effective capacity of a new system, or (2) the cost of maintaining or improving the effective capacity of the current system.

The users and the central management are assumed to have the same valuation for the expected gross value and delay cost, so the central management's objective is to maximize the aggregate net value provided by the information system. With perfect information, their problem is:

$$
\max _ {\lambda , \mu} V (\lambda) - v \lambda W ^ {\prime} (\lambda , \mu) - C (\mu , \theta).\tag{2.1}
$$

We call (2.1 ) the full-information program, and its solution the full-information solution. We assume that the Hessian matrix of(2.1) is negative definite for $( \lambda , \mu ) \in \mathcal { R } _ { + } ^ { 2 }$ and thereby (2.1) has a unique maximum from the following first-order conditions (Mendelson 1985):

$$
0 = V ^ {\prime} (\lambda) - v W ^ {\prime} (\lambda , \mu) - v \lambda W _ {\lambda} ^ {\prime} (\lambda , \mu),\tag{2.2}
$$

$$
0 = - v \lambda W _ {\mu} ^ {\prime} (\lambda , \mu) - C _ {\mu} (\mu , \theta),\tag{2.3}
$$

where the prime and subscript denote the first and partial derivatives, respectively Let $\lambda ^ { \prime }$ and $\mu ^ { \ i }$ be the solutions of (2.2) and (2.3). The optimal price is:

$$
p ^ {i} = V ^ {\prime} (\lambda^ {i}) - v W (\lambda^ {i}, \mu^ {i})\tag{2.4}
$$

$$
= v \lambda^ {t} W _ {\lambda} ^ {r} (\lambda^ {t}, \mu^ {t})\tag{2.5}
$$

where (2.4) gives the marginal user's (job's) inverse demand function for the computer service. The optimal subsidy or surplus that the IS department should show is

$$
T ^ {t} = C (\mu^ {t}, \theta) - p ^ {t} \lambda^ {t}.\tag{2.6}
$$

In general, $T ^ { \iota }$ does not equal zero and therefore will not be useful in evaluating the IS department since a balanced budget will almost never correspond to the organizational net value maximizing performance. (See Dewan and Mendelson (1990), Wang (1991) for detailed discussions.)

## 2.2. Mechanism Design

A game-theoretic approach is required to investigate the central management's design of decision rules to induce the $\mathrm { I S }$ manager's truth-revelation and at the same time eliminate or reduce the informational rents that the IS manager can command. Here we briefly review some essentials of mechanism design; sce Fudenberg and Tirole (1991) for more detail

Let $D _ { 1 }$ be the feasible set of the IS manager's decisions, which in mechanism design is the message space of the IS manager's report of the cost parameter θ, whose value is uncertain for the central management. Thus, given the space of' the cost parameter and $D _ { 1 }$ , the IS manager's reporting strategy is a mapping: ${ \boldsymbol { \sigma } } _ { 1 } : \Theta \to D _ { 1 }$ Let $D _ { 2 }$ be the feasible set of decisions available to the central management concerning the IS operations and budget allocation: $\lambda , \mu ,$ and T. Thus, $I ) _ { 2 } = { \mathrm { \Omega } } ^ { * } { \mathrm { \Omega } } ^ { 2 } \times { \mathrm { \Omega } } ^ { * } { \mathrm { \Omega } }$ . A mechanısm is a process of generating decisions and budgeting allocation $\{ \lambda , \mu , T \}$ through a Bayesian game withn which the central management and the IS manager act and interact as follows:

1. The IS manager observes the realized θ.

2. The central management commits to a set of decision rules. $( \lambda ( \cdot ) , \mu ( \cdot ) , T ( \cdot ) )$

$$
\theta = \sigma_ {1} (\theta)
$$

$$
\sigma_ {1}: \Theta \rightarrow D _ {1}
$$

4. The center makes the decisions $( \lambda ( { \hat { \theta } } ) , \mu ( { \hat { \theta } } ) , T ( { \hat { \theta } } ) ) = \sigma _ { 2 } ( { \hat { \theta } } )$ based on the message received and the strategy $\sigma _ { 2 } : D _ { 1 }  D _ { 2 }$

5. The IS manager implements the decisions.

A Bayesian equilibrium of this game is a strategy pair $\big ( \sigma _ { 1 } ^ { * } , \sigma _ { 2 } ^ { * } \big )$ which are the best responses to each other's strategy. An arbitrary pair of strategies $\left( \sigma _ { 1 } , \sigma _ { 2 } \right)$ induces three outcome functions

$$
\lambda : \Theta \rightarrow \mathcal {R} _ {+}, \quad \mu : \Theta \rightarrow \mathcal {R} _ {+}, \quad T: \Theta \rightarrow \mathcal {R}.
$$

which define a mechanism $\Gamma ( \cdot ) \equiv ( \lambda ( \cdot ) , \mu ( \cdot ) , T ( \cdot ) )$ . A mechanism therefore is a procedure giving the decisions to the central management, which commits itself to a decision rule relating the choice of $\Gamma$ to messages sent by the IS manager. Thus a mechanism has the dual purposes of extracting information and making decisions.

A mechanism is said to be direct if and only if $\smash { l ) _ { \mathrm { : } } = 6 }$ , so that the IS manager's strategy is a reporting strategy which is a mapping $\sigma _ { 1 } : \Theta \to \Theta$ . In order for a mechanism to be truthfully implementable (truthful revelation is a dominant strategy for the IS manager). it must be incentive compatible. Let $\ell ^ { \prime } ( \hat { \theta } ; \beta )$ be the IS manager's utility wher the true cost parameter is θ and she reports ${ \hat { \boldsymbol { \ H } } } = \sigma _ { 1 } ( { \boldsymbol { \theta } } )$ . A direct mechanism is incentive compatible (a direct revelation mechanısm) if and only if

$$
U (\theta ; \theta) \geq U (\hat {\theta}; \theta), \quad \forall \theta , \hat {\theta} \in \Theta .
$$

Thus a direct revelation mechanism induces the IS manager's reporting strategy to be an identity function $\beta \ / \in _ { \sigma _ { 1 } } ( \beta )$ , for all θ in θ.

Letting the strategy pair $\left( \mathfrak { r } _ { 1 } , \sigma _ { 2 } \right)$ be a Bayesian equilibrium, the revelation princıple (Dasgupta et al. 1979; Myerson 1979; Myerson 1991, Chapter 6), implies that there exists another Bayesian equilibrium $\left( \tilde { \sigma } _ { \mathfrak { i } } , \sigma _ { \mathfrak { 2 } } \right)$ of a direct mechanism where $\tilde { \sigma } _ { 1 } ( \theta ) = \theta .$ for all θ in θ such that the induced outcomes coincide. Thus we can restrict our attention to the outcomes induced by direct, incentive compatible mechanisms without loss of generality. To limit analytical complexity, we consider only cases where the private information, θ, of the IS manager has only one dimension. We impose some additional assumptions on the information structure of the environment that we study:

Assumprion 1. The IS manager knows the realized θ exactly, while the central management only has some common knowledge prior beliefs about the distribution of $\theta , F ( { \tilde { \theta } } )$ , which is twice continuously differentiable and has probability density func-$t i o n f ( { \tilde { \theta } } ) > 0$ if and only if $\widetilde { \boldsymbol { \theta } } \in \mathbf { { \Theta } } \mathbf { { \Theta } } \equiv [ \underline { { \boldsymbol { \theta } } } , \overline { { \boldsymbol { \theta } } } ]$

Assumption 2 gives the properties of the capacity cost function that we assume in this paper.

ASSUMPTION 2. For all $\theta \in \mathbf { \Theta } _ { \mathbf { 0 } }$ and $\mu \in { \mathcal { R } } _ { + } , C ( \mu , \theta )$ is assumed to be twice continuously differentiable with respect to both arguments, and $C _ { \mu } > 0 , C _ { \theta } > 0 , C _ { \mu \theta }$ $> 0$ , and $C _ { \mu \mu } \geq 0$

This assumption says that the cost function is increasing in both arguments and weakly convex in μ. $C _ { \mu \theta } > 0$ , commonly called the “sorting condition," merely requires the marginal capacity cost to be monotone in θ.

AssumPTioN 3. The effective capacity can be observed and verifed by the centrat management ex post.

In general, this is a reasonable assumption since the central management can verify the effective capacity by historical data on average job turnaround time and system availability. Therefore the central management is assumed to be able to direct the IS manager to achieve a specified level of effective capacity.

AssumpTion 4. The central management and the users have the same gross value function and delay cost, which are the same as in the full information case in the previous section, and are common knowledge for both the central management and the IS manager.

## 3. Organization of IS Departments

There are two much-studied forms of organizing and evaluating information service units: the cost center and the profit center. In the absence of a competitive external market, Mendelson (1985) and Dewan and Mendelson (1990) have shown that it is never optimal to organize an IS department as a profit center due to the monopolistic pricing problem. However, this conclusion is derived from models having neither information asymmetry nor objective conflicts between the central management and the IS department. As it turns out, the same conclusion results in a simple way from our model as well, since the revelation principle implies that a suitably designed revelation mechanism can replicate the performance of any decentralized mechanism such as a profit center, and an optimally designed revelation mechanism is undominated by any other method of control. Consequently, we will derive the optimal revelation mechanism first

## 3.1. The Cost Center under Revelation Mechanisins

When the IS department is organized as a cost center, we assume that it is governed by a centralized mechanism under which, based on the IS manager's report, θ, the central management determines the budget allocation and all the operating variables such as prices and capacity. Cost centers are effective when the output can be deined and measured well, and the required inputs per unit of output can be specified (Kaplan and Atkinson 1989). Some outputs of an information system are not particularly difficult to measure, e.g., the average number of jobs processed per unit of time and the average response time. However, information systems are a very complex bundle of hardware, software, operating personnel, and users, making the required inputs to achieve a specific level of performance hard to measure. The relationship between inputs and outputs is further blurred by such qualitative requirements such as the degree of user friendliness, etc. Without detailed information about computer technologies and the local operating environment, it is difficult for the central management to set the standard costs appropriate to attaining a specific level of system performance. Thus the central management will want to induce the IS manager to report her private cost information. However, in the presence of information asymmetry and objective conflicts between the central management and the departmental manager, incurring “organizational slack"² is inevitable in general when the departmental manager is assigned the responsibility to perform certain tasks (see, e.g.. Antle and Eppen 1985, Antle and Fellingham 1990, Kirby et al. 1991). If the IS manager derives utility from consuming the organizational slack by, say, overinvesting in advanced technologies and staffers, then she has an incentive to overreport the IS department's costs. Notice that regardless of whether she intends to maximize her reward from cost savings or her utility from consuming the organizational slack, her optimal strategy is always to exaggerate the costs in order to influence the central management to provide as large a budget allocation as possible. Thus if the central management is aware of the IS manager's incentive problems, it would not simply accept whatever standard cost or budget allocation she proposes; some form of bargaining game should be expected during the budgeting process. Within an organization it is natural to assume that the central management possesses all the bargaining power and thereby can prescribe any decision rule that it sees fit.

Mechanism design requires the central management to first credibly commit to a mechanism, Γ(·). We first derive the required (incentive compatible) amount of excess budget allocation for each $\theta \in { \Theta }$ . Define the excess budget allocation when the IS manager reports  and the true cost parameter is θ:

$$
S (\hat {\theta}; \theta) \equiv R (\lambda (\hat {\theta}), \mu (\hat {\theta})) - C (\mu (\hat {\theta}), \theta) + T (\hat {\theta})
$$

where $R ( \cdot )$ is the IS department's revenue generated from its computing services and the transfer, $T ( \cdot )$ , depending on whether the IS department's revenue can cover its costs, can be positive (subsidy) or negative (taxation). To induce the IS manager's honest reporting requires:

$$
S (\theta ; \theta) \geq S (\hat {\theta}; \theta), \quad \forall \hat {\theta}, \theta \in \Theta .\tag{3.1}
$$

That is, truthfully revealing the cost information is the dominant strategy for the IS manager.

Of course, if the transfer rule (2.6) induces the IS manager's truthful reporting, then the full-information solution can always be obtained and the private information of the IS manager imposes no informational constraint on the central management. However, when the IS manager's objective is to maximize the excess budget allocation, the transfer rule (2.6) fails to be incentive compatible as shown by the following proposition.

PROPOSITION 1 $H C ( \mu , \theta )$ is increasing in θ for all $\theta \in \Theta$ , then the subsidy rule (2.6) is not incentive compatible and therefore it is impossible to achieve the full-information solution since the IS manager will overreport the IS department's costs.

Given the mechanism committed to by the central management and the realized cost parameter θ, the IS manager maximizes the excess budget allocation by solving:

$$
\max _ {\hat {\theta}} S (\hat {\theta}; \theta).
$$

Since the IS manager is perfectly informed, the revenue plus the transfer must at least fully cover the costs in order for her to agree to the terms of the budget allocation:

$$
S (\theta ; \theta) \geq 0, \quad \forall \theta \in \Theta .\tag{3.2}
$$

We call this the budget constraint, which is similar to the individual rationality constraint in the incentive literature. However, the budget constraint simply serves as a yardstick for the central management to calculate the appropriate taxation of or subsidy to the IS department so that it can at least balance its budget after taxation or subsidy for all $\theta \in \Theta$ . Thus, (3.1) and (3.2) form a set of constraints for the optimal mechanism design problem faced by the central management, and we say the set of mechanisms satisfying (3.1) and (3.2) is feasible. We now can characterize as Lemma 1 the set of feasible mechanisms. Similar lemmas are well known in the incentive literature, so we omit the proof (see, e.g., Baron and Myerson 1982, Guesnerie and Laffont 1984, Mirrlees 1986).

LEMMA 1. A direct, differentiable mechanism $\Gamma ( \cdot )$ is incentive compatible if and only if

$$
S (\theta) = S (\bar {\theta}) + \int_ {\theta} ^ {\bar {\theta}} C _ {\theta} (\mu (\tilde {\theta}), \tilde {\theta}) d \tilde {\theta}, S (\bar {\theta}) \geq 0,\tag{3.3}
$$

and $\mu ( \theta )$ is nonincreasing for all θ in θ.

From a technical point of view, this lemma can be used to replace the constraints (3.2) by a single constraint (Baron 1989). Notice that since $C _ { \theta } > 0 , S ( \theta )$ is decreasing in θ. Since the central management finds the excess budget allocation undesirable, it is optimal for it to set $S ( \overline { { { \theta } } } ) = 0$ , so that (3.2) is automatically satisfied for every θ in θ without disrupting the incentive compatibility constraints. Thus the central management's problem reduces to finding the expected net value maximizing capacity function $\mu ( \cdot )$ within the set of nonincreasing functions.

Without rewarding the IS manager on cost savings, the central management will incur an extra cost equal to S(θ). Although the IS manager derives utility from consuming $S ( \theta )$ , she might prefer an explicit reward (e.g., cash) since there will be some restrictions on how $S ( \theta )$ can be spent. As a result, the organization may be better of if truthful reporting can be induced by rewarding cost savings rather than having the IS manager consume all of $S ( \theta )$ . With general functional forms for the IS manager's utility generated by consuming organizational slack and pecuniary rewards, the problem becomes intractable. Thus we make the following assumption.

AssumPTioN 5. The IS manager has preferences linear in both pecuniary rewards and consumption of organızational slack: $B ( \phi , { \hat { \theta } } ) + \xi ( S - \phi )$ , where $B \{ \phi , \hat { \theta } )$ : the pecuniary reward to the IS manager if she shows a cost savings φ and reports ; φ: the amount excess budget allocation that the IS manager chooses to be shown as cost savings; and ξ: the index of the strength of the IS manager's professionalism tendency, $\xi \in [ 0 , 1 ]$

The IS manager's utility function is then:

$$
\begin{array}{c} U (\hat {\theta}; \theta) \equiv \max _ {0 \leq \phi \leq S} \left\{B (\phi , \hat {\theta}) + \xi (S - \phi) \right\}, \\ U (\theta) \equiv U (\theta ; \theta). \end{array}
$$

To clarify the presentation, we suppress $\xi$ from the IS manager's utility function

The linear structure we assume for the IS manager's utility function is restrictive, but it can be viewed as a first-order approximation of a more general utility function reflecting the IS manager's substitution between consuming organizational slack and pecuniary rewards. We believe that most of the qualitative results derived from this simple model will hold with a more general utility function. We restrict ξ to be within [0, 1] since for $\xi > 1$ , it is never worth the central management's while to lure the IS manager away from consuming organizational slack. Note that given Assumption 5, if the IS manager is not rewarded on cost savings, then $B ( \phi , { \hat { \theta } } ) \ = \ 0 , \ \forall \phi .$ , and if consuming organizational slack does not generate any positive utility for the IS manager, ξ = (. We assume that when the IS manager is indifferent between the pecuniary reward and the consumption of organizational slack, she chooses the pecuniary reward.

We assume that ξ is known exactly by the central management. (Appendix B shows that the case of the central management being uncertain about ξ can be handled without much change.) Regardless of whether ξ is known to the central management, our mechanisms will not require the IS manager to reveal her actual $\xi .$ Since mechanism design problems with more than one informational parameter are extremely d:fficult to solve, even with very simple utility functions (see Baron (1989) for a discussion), requiring both θ and ξ to be revealed makes the problem intractable. Since the job of central management is to be expert in managing people rather than information systems, they are more likely to be able to form a reasonable opinion about ξ's value than $\theta ^ { \bullet } s$

LEmmA 2. Given the excess budget allocation S, it is always optimal for the central management to induce the IS manager to choose $\phi ^ { * } ( S ) = S$ , and the optimal rewards on cost savings $B ^ { * } ( S , { \hat { \boldsymbol { \theta } } } ) = \xi S$

From Lemma 2, we can write the IS manager's utility function as:

$$
U (\hat {\theta}; \theta) = \xi S (\hat {\theta}; \theta).
$$

Since the central management seeks to maximize the organizational expected net value generated by the information services, their mechanism design problem $\mathrm { i s } ^ { 4 } \mathrm { i s }$

$$
\max _ {\lambda (\cdot), \mu (\cdot), S (\cdot)} \int_ {\Theta} \left\{V (\lambda (\theta)) - v \lambda (\theta) W (\lambda (\theta), \mu (\theta)) - C (\mu (\theta), \theta) - \xi S (\theta) \right\} d F (\theta)\tag{3.4}
$$

subject to

$$
U (\theta) \geq U (\hat {\theta}; \theta), \quad \forall \theta , \hat {\theta} \in \Theta ,\tag{3.5}
$$

$$
U (\theta) \geq 0, \quad \forall \theta \in \Theta .\tag{3.6}
$$

Substituting $\xi S ( \theta )$ for $S ( \theta )$ in Lemma 1, implies (3.5) and (3.6) are satisfied if $U ( { \bar { \theta } } ) \geq 0$ and

$$
U (\theta) = U (\bar {\theta}) + \xi \int_ {\theta} ^ {\bar {\theta}} C _ {\theta} (\mu (\tilde {\theta}), \tilde {\theta}) d \tilde {\theta},
$$

provided $\mu ( \theta )$ is nonincreasing in θ. Since it is always optimal for the central management to set $U ( { \overline { { \theta } } } ) = 0$ , the organizational loss is:

$$
U (\theta) = \xi S (\theta) = \xi \int_ {\theta} ^ {\tilde {\theta}} C _ {\theta} (\mu (\tilde {\theta}), \tilde {\theta}) d \tilde {\theta}.\tag{3.7}
$$

When $\xi > 1 , \xi S > S$ , so the central management will never provide the IS manager any pecuniary rewards on the cost savings. This is equivalent to setting $\xi = 1$ . Using (3.7) in (3.4) and integrating by parts, the central management's problem becomes:

$$
\begin{array}{r l} \max _ {\lambda (\cdot), \mu (\cdot)} \int_ {\Theta} \left\{V (\lambda (\theta)) - v \lambda (\theta) W (\lambda (\theta), \mu (\theta)) \right. & \\ & \left. - C (\mu (\theta), \theta) - \xi \beta (\theta) C _ {\theta} (\mu (\theta), \theta) \right\} d F (\theta) \end{array}\tag{3.8}
$$

subject to

$$
\mu (\theta) \text {   is   nonincreasing   in   } \theta , \quad \forall \theta \in \Theta ,\tag{3.9}
$$

where $\beta ( \theta ) \equiv F ( \theta ) / f ( \theta )$ is the inverse hazard rate. The usual solution approach is to solve the unconstrained problem (3.8) first, and then to check whether (3.9) is satisfied for all θ. If it is not satisfied for all θ (i.e., when bunching or pooling occurs), then convexification techniques must be used (Baron and Myerson 1982, Guesnerie and Laffont 1984). Since this greatly complicates the mathematics while providing little insight into this problem, in the following proposition we impose some assumptions on (3.8) so that (3.9) will be satisfied for every θ.

PROPOsITION 2. If (1) the Hessian matrix of

$$
H \equiv V (\lambda) - v \lambda W (\lambda , \mu) - C (\mu , \theta) - \xi \beta (\theta) C _ {\theta} (\mu , \theta)
$$

with respect to λ and $\pmb { \mu }$ is negative definite; and (2) $C _ { \mu } ( \mu , \theta ) + \xi \beta ( \theta ) C _ { \theta \mu } ( \mu , \theta )$ is nondecreasing in θ for all $\theta \in \Theta$ , the optimal solution $\hat { o f ( 3 . 8 ) - ( 3 . 9 ) }$ is the solution $o f$ the following equations:

$$
0 = V ^ {\prime} (\lambda) - v W (\lambda , \mu) - v \lambda W _ {\lambda} (\lambda , \mu),\tag{3.10}
$$

$$
0 = - v \lambda W _ {\mu} (\lambda , \mu) - C _ {\mu} (\mu , \theta) - \xi \beta (\theta) C _ {\theta \mu} (\mu , \theta),\tag{3.11}
$$

and the optimal solution is globally incentive compatible . Moreover, letting $\lambda ^ { * } ( \theta )$ and $\mu ^ { * } ( \theta )$ be the solution of (3.10) and (3.11), the optimal price

$$
p ^ {*} (\theta) = v \lambda^ {*} (\theta) W _ {\lambda} (\lambda^ {*} (\theta), \mu^ {*} (\theta)),
$$

and the optimal incentive compatible transfer function $t . \mathrm { { s } ; }$

$$
\begin{array}{c} T ^ {*} (\theta) = - p ^ {*} (\theta) \lambda^ {*} (\theta) + C (\mu^ {*} (\theta), \theta) + S ^ {*} (\theta), \quad w h e r e \\ S ^ {*} (\theta) = \int_ {\theta} ^ {\tilde {\theta}} C _ {\theta} (\mu^ {*} (\tilde {\theta}), \tilde {\theta}) d \tilde {\theta}. \end{array}
$$

Discussion. The way the optimal mechanism works can be visualized as follows: the central management first displays a menu of values determined from the mechanism. $\{ \Gamma ^ { * } ( \theta ) : \theta \in \Theta \}$ , to the IS manager; then the central management asks the IS manager to pick a particular entry from the menu; after the IS manager picks the entry, the decisions and actions are implemented accordingly without any ex post adjustments. If the central management can credibly commit itself to a mechanism characterized by $\Gamma ^ { * } ( \theta )$ , we know that it is optimal for the IS manager to report θ truthfully. If the central management fails to convince the IS manager that it will not use the additional information revealed by her choice against her ex post, she would not reveal her private information truthfully, and each party would face a game similar to the original one.

Since only $\mu ^ { * } ( \theta )$ enters $S ^ { \ast } ( \theta )$ , it is the central management's choice of capacity (and thereby the corresponding budget allocation) that dictates the IS manager's reporting strategy. Without loss of generality, we can view the mechanism as taxing away all the IS department's revenue and then allocating it a lump-sum budget equal to $C ( \mu ^ { * } ( \theta ) , \theta ) + S ^ { * } ( \theta )$ , making the IS manager's informational rent;

$$
U (\hat {\theta}; \theta) = \xi \left\{C \left(\mu^ {*} (\hat {\theta}), \hat {\theta}\right) + \int_ {\hat {\theta}} ^ {\bar {\theta}} C _ {\theta} \left(\mu^ {*} (\tilde {\theta}), \tilde {\theta}\right) d \hat {\theta} - C \left(\mu^ {*} (\hat {\theta}), \theta\right) \right\}
$$

if the IS manager reports $\hat { \pmb \theta } .$ The incentive compatibility of the optimal budget allocation rule can then be easily checked by observing that

$$
\left. \frac {\partial U (\hat {\theta} ; \theta)}{\partial \hat {\theta}} \right| _ {\hat {\theta} = \theta} \equiv 0.
$$

$\mathbf { S o } ,$ as long as the central management and the IS manager have the same amount of information concerning the user's demand, the IS manager's incentive for truth-reporting will not be altered even when the realized revenue differs from $p ^ { * } ( \theta ) \lambda ^ { * } ( \theta )$ 1

Also note that the outcomes of this mechanism are equivalent to the outcomes of a bargaining game when the central management has all the bargaining power, and the outcomes of the optimal mechanism correspond to the central management's neutral bargaining solution (see Myerson 1985a, Spulber 1989). Thus, even when the central management has superior information about the user's demand or has its own objective as to what the scale of the IS operations should be, the optimal mechanism remains optimal with some appropriate modifications in response to a different value function.

The sources of the distortions due to both the incentive conflicts and the information asymmetry are clearly visible in Equations (3.10) and (3.11). First, comparing (3.10) and its full-information counterpart, Equation (2.2), shows that there is no direct distortion in the short-run problem since, given a particular capacity, (2.2) and (3.10) yield the same solution. However, comparing (2.3) and (3.11) it is clear that the full-information first-order condition is distorted by the extra term $\xi \beta ( \theta ) C _ { \theta \mu } ( \mu , \theta )$ $\geq 0 .$ . This has the effect of reducing the optimal capacity from that of the full-information solution, which in turn will reduce the arrival rate via (3.10).

The intuition behind the restriction in capacity can be seen from the fact that the IS manager's ex post informational rent is

$$
\xi S (\theta) = \xi \int_ {\theta} ^ {\hat {\theta}} C _ {\theta} (\mu (\tilde {\theta}), \tilde {\theta}) d \tilde {\theta}.
$$

Since $C _ { \theta \mu } > 0$ , distorting $\pmb { \mu }$ downward will reduce the integrand in $\xi S ( \theta )$ , reducing her informational rent and her incentive to overstate cost. The ex post informational rent is calculated based upon the mechanism (note $\mu ( \theta )$ in the integrand), and as can be seen from the limits of integration, it is zero at $\bar { \theta }$ and at its maximum at θ. This occurs since it is impossible for the IS manager to misrepresent the least efficient department $( \ i . \mathsf { e } _ { \cdot } , \ \tilde { \theta } )$ as anything else, and thus she has no power to extract any reward for her information. On the other hand, she has the greatest latitude for misrepresentation when the department is most efficient (i.e., θ), and thus must be rewarded most to induce truthful reporting.

It is also interesting to compare the ex post informational rent to the virtual informational rent, $\xi \beta ( \theta ) C _ { \theta } ( \mu , \theta )$ in H. Intuitively, the role of the virtual informational rent is to cause the mechanism to be designed to guard against reports of large values ofθ. When $\theta = \theta$ , there is no other state in θ that the IS manager can overstate it to be since $F ( { \underline { { \theta } } } ) = 0$ . Consequently, from the central management's standpoint, distorting $\mu ( \underline { { \theta } } )$ ex ante will affect the IS manager's incentive for misrepresentation with probability zero, and therefore the virtual informational rent should cause no penalty to be placed on such a report; this is called “no distortion at the bottom." However, when θ $> \underline { { \theta } } .$ , a distortion of $\dot { \mu } ( \theta )$ will reduce the IS manager's incentive for misrepresentation for all $\hat { \boldsymbol { \theta } } \in [ \underline { { \boldsymbol { \theta } } } , \boldsymbol { \theta } ]$ , and distorting $\mu (  { \bar { \theta } } )$ can reduce the IS manager's informational rent for all possible realizations of θ. As a result, the central management wants the mechanism to place the highest penalty on the IS manager's reporting ē.

Thus it can be seen that there are two sources of efficiency loss from the organization's viewpoint. The first is the reward $\xi S ( \theta )$ to the IS manager, and the second is the opportunity cost of the jobs not served due to the reduction in arrival rate caused by restricting capacity. Hence capacity must be set to balance the reduction in informational rent against the loss due to fewer jobs served; this is accomplished through the term $\xi \beta ( \theta ) C _ { \theta \mu } ( \mu , \theta )$ in (3.11), the contribution of the virtual informational rent to the virtual marginal capacity cost.

The effects of the incentive conflicts are captured by $\xi$ in (3.11). Note that $\xi = 0$ can be interpreted as meaning the organization's objectives and those of the IS manager coincide, so that (3.11) reduces to the full information first-order condition, (2.3). As ¿ grows, so does the impact of $\xi \beta ( \theta ) C _ { \theta \mu } ( \mu , \theta )$ , up to the point $\xi = 1$ , and the IS manager consumes all of the slack for $\xi \ge 1$ . Thus as ξ grows, the central management will find it optimal to distort the capacity downward progressively more, and the optimal arrival rate with it.

The degree of the central management's uncertainty about the IS department's efficiency is similarly captured by $\beta ( \theta )$ , albeit in a somewhat less obvious way. This is most easily seen by using a uniform distribution defined on the interval $[ \underline { { \theta } } , \overline { { \theta } } ]$ , which gives $\beta ( \theta ) = \theta - \underline { { \theta } }$ , where $\theta \leq \theta \leq \overline { { \theta } } .$ . The central management's degree of uncertainty is then reflected by the length of $[ \underline { { \theta } } , \bar { \theta } ]$ . Clearly, when the central management is perfectly informed about $\theta , S ( \theta ) = 0$ , so that (3.11) coincides with (2.3) as we would expect.

The expression $\beta ( \theta ) ~ = ~ \theta ~ - ~ \underline { { \theta } }$ emphasizes the rather paradoxical nature of the central management's problem due to its uncertainty about θ. When there is a possibility that the IS operation is highly efficient (i.e., θ is very low), this enhances the ability of the IS manager to generate large amounts of informational rent when reporting a given θ, and therefore (3.11) says that the lower θ is, the larger is the required downward distortion of the capacity since $\beta ( \theta )$ is larger.

## 3.2. The Profit Center

In McGee's study (1988, p. 59), a little over 8% of the companies in his sample use a profit center to manage their computing resources. A profit center is one form of decentralized mechanism where the capacity and pricing decisions are delegated to the IS department, and its performance is evaluated based on the profit it generates. As in the cost center case, if the IS department is not rewarded for its profit, it is optimal for the IS manager to consume it all and report zero profit. Thus whether she consumes profit via overinvestment or receives an explicit reward based on reported profit, she will set the capacity and price in order to maximize her department's profit. However, the IS manager's decision on consuming organizational slack (the profit) will be altered by the nature of the reward. Therefore, the IS manager sets the capacity and price to maximize her department's profit

$$
\pi (\theta) \equiv \pi (\lambda^ {p} (\theta), \mu^ {p} (\theta)) = \max _ {\lambda , \mu} p \lambda - C (\mu , \theta).\tag{3.12}
$$

where $p = \mathrm { \Delta } { \mathrm { \Delta } } { \mathrm { \Delta } } { \mathrm { \Delta } } p = \mathrm { \Delta } { \mathrm { \Delta } } { \mathrm { \Delta } }$ . Note that even though the user's dela costs are not directly borne by the IS department, the IS department has to take full account of them in its profit maximization since (3.12) is equivalent to:

$$
\max _ {\lambda , \mu} \lambda V ^ {\prime} (\lambda) - v \lambda W (\lambda , \mu) - C (\mu , \theta).
$$

For a given λ, the IS-related costs borne by the organization when the IS department is organized as a profit center are exactly the same as when the central management is fully informed. However, the IS department's profit maximizıng price does not maximize the organizational net value. In contrast with the revelation mechanism, the distortion of decisions here stems from the distortion of the users' gross value, not the cost, since when maximizing the organizational net value, the users gross value should be evaluated as $V ( \lambda )$ instead of $\lambda V ^ { \prime } ( \lambda )$ . Also by assumption $V ( \lambda )$ is concave, so $V ( \lambda ) > \lambda V ^ { \prime } ( \lambda )$ for all $\lambda > 0$ . Thus, as long as the IS department is able to earn a positive profit, the resulting organizational net value will be positive. Because $V ( \lambda ) = \lambda V ^ { \prime } ( \lambda )$ for all λ if and onlv if $V ( \lambda )$ is linear, the net value maximizing decisions coincide with the IS department's profit maximizing decisions if and only if $V ( \lambda )$ is linear.

As mentioned above, in order to induce the IS manager not to consume the organizational slack, the central management still has to provide appropriate rewards on profit. Given the linearity of the IS manager's utility, the optimal rewards take the same form as for the cost center, $\xi \pi ( \theta )$ . Thus, when the IS department is organized as a profit center, it is easy to show that the expected organizational net value is:

$$
E \left\{N V ^ {p} (\theta) \right\} = \int_ {\Theta} \left\{V \left(\lambda^ {p} (\theta)\right) - \lambda^ {p} (\theta) V ^ {\prime} \left(\lambda^ {p} (\theta)\right) + (1 - \xi) \pi (\theta) \right\} d F (\theta).
$$

Thus, providing appropriate rewards on profit gives the organization a strictly posi tive expected net gain

$$
(1 - \xi) \int_ {\Theta} \pi (\theta) d F (\theta),
$$

provided that $\xi < 1$ .When $\xi \ge 1$ , the expected organizational net value is simply the expected difference between the users' and the IS department's valuations.

In addition, the expected organizational net value when the IS department is organized as a profit center cannot be greater than that attained by a cost center governed by the optimal revelation mechanism. When communication between the central management and the IS department is unlimited and costless, the performance of the profit center can be replicated by the centralized mechanism $\left\{ \lambda ^ { p } ( \theta ) , \mu ^ { p } ( \theta ) : \theta \in \Theta \right\}$ with the IS manager being compensated by the amount $\xi \pi ( \theta )$ . This mechanism is incentive compatible since the decisions made under it by the central management are the same as those the IS manager would make if the decisions were left to her. The revelation principle then implies that a cost center under the optimal mechanism provides performance at least as good as the profit center.

## 3.3. Comparative Statics

Here we present some comparative static analysis by varying the support of the central management's prior beliefs about the IS department's cost parameter, θ, and the index of the IS manager's preference concerning the excess budget allocation, $\xi .$ Also we parametrize the users' aggregate value function $V ( \lambda , k )$ by a parameter k such that $V _ { \boldsymbol { k } } ( \lambda , k ) > 0$ and study the effect of varying k. Let $H ^ { * } ( \theta )$ be $H ( \theta )$ evaluated at $\lambda = \lambda ^ { * } ( \theta )$ and $\mu = \mu ^ { * } ( \theta )$ , and therefore $E \{ N V ^ { * } ( \theta ) \} = E \{ H ^ { * } ( \theta ) \}$ . We further assume that $F ( \theta )$ is uniform and examine the effects of mean-preserving spreads using the parameter $\delta , \mathrm { i . e . , } \Theta = [ \underline { { { \theta } } } - \delta , \overline { { { \theta } } } + \delta ]$ . The results of the comparative statics for the optimal mechanism and profit center are summarized in Table 1.

From Table 1, it is clear that, except for δ, an increase in the value of parameters has an unambiguous effect on the expected organizational net value. The effect of an increase in k or ξ should be clear. A stronger demand for information processing should generate a higher organizational net value regardless of how the IS department is organized. On the other hand, the expected organizational net value should decrease if the organization's IS manager is subject to a more severe incentive problem.

TABLE 1  
The Effect of an Increase in k, ξ, θ, θ, δ

<table><tr><td></td><td>k</td><td> $\xi$ </td><td> $\underline{\theta}$ </td><td> $\bar{\theta}$ </td><td> $\delta$ </td></tr><tr><td> $E\{NV^{*}\}$ </td><td>+</td><td>-</td><td>-</td><td>-</td><td>+/-</td></tr><tr><td> $E\{NV^{p}\}$ </td><td>+</td><td>-</td><td>-</td><td></td><td>+</td></tr></table>

Here δ parametrizes the spread of the mean-preserving spread of the distrıbution, i e , $\mathbf { \theta } \mathbf { \theta } \mathbf { \theta } \mathbf { \Theta } \Theta = [ \theta \mathrm { ~ - ~ } \delta \mathrm { ~ , ~ } \tilde { \theta } \mathrm { ~ + ~ } \delta ] .$

Also, we should expect IS departments which are provided explicit rewards to perform better than those not so rewarded. This hypothesis may be a topic for empirical investigation.

Since for each $\theta , N V ^ { p } ( \theta )$ will not be affected by variations in θ and ${ \overline { { \theta } } } ,$ it is readily verified that $E \{ N V ^ { p } ( \theta ) \}$ is decreasing in both θ and ē. We also can show that $E \{ N V ^ { p } ( \theta ) \}$ is increasing in δ provided that $N V ^ { p } ( \theta )$ is convex in θ. This result is obvious, since a mean-preserving spread increases the support of θ by an equal amount at the upper and lower ends. So if $N V ^ { p } ( \theta )$ is decreasing and convex, the effect of a decrease in $\underline { { \theta } }$ will be stronger than that of an increase in $\overline { { \theta } } .$ The effect of varying the support of the central management's prior beliefs, θ, is less obvious under the optimal revelation mechanism. For example, it can be shown that when $F ( \theta )$ is uniform, the expected organizational net value is decreasing in both θ and ${ \overline { { \theta } } } .$ Consequently, a mean-preserving spread of the support θ can cause the expected organizational net value to increase or decrease. An interesting implication of this is that in general it will be unclear whether the central management will be willing to pay for information which reduces its uncertainty about θ, especially since both the expected value and the spread are likely to be affected. Carlyle (1990) reports that firms which offer independent assessments of IS department costs have considerable difficulty attracting new clients, and their fees seem surprisingly low (\$20,000 to \$150,000 cepending on the size of the department). Since in general such information may both reduce uncertainty and alter the expected value, the information's expected value is quite difficult to assess, and likely to be quite low, causing few firms to use the services, and those that do use them to be willing to pay relatively little.

## 4. Example

The analytical work presented thus far offers little direct insight into the magnitudes of the distortions and performance differences involved. Thus we present a specific example to make the implications more concrete. We make the following assumptions for this example:

1. The organization's information system can be characterized as an $M / M / 1$ queueing system with First-Come First-Served discipline.

2. The aggregate gross value function is $V { \underline { { ( \lambda ) } } } = 2 k \big | \lambda$ , where $k > 0$ , so that the gross inverse demand curve is $V ^ { \prime } ( \lambda ) = k / \sqrt \lambda$ . This is an isoelastic demand curve having price elasticity of demand $\epsilon = - 2$ , which is quite elastic, meaning the user population has some freedom in how they acquire computing.

3. The “true” capacity cost function is $C ^ { \prime } ( \mu , \theta ) = \theta \mu$ , so the marginal capacity cost is θ. Since recent empirical work (e.g., Barron 1992, Mendelson 1987) implies that constant marginal capacity cost for hardware is reasonable, a lower bound for θ is given by the hardware component of $C ,$ , which can be estimated from market data.

(In Barron (1992), for 1988 data, this was about $\$ 70,000$ per MIPS, or about \$0.002 per million instructions assuming a five year system lifetime.)

4. The cost parameter $\theta \in { \bf \Theta } \Theta = [ \underline { { { \theta } } } , { \bf \Xi } \overline { { { \theta } } } ]$ is uniformly distributed. (The uniform distribution satisfies the monotonicity constraint.)

5. As has been assumed throughout, $\xi \in [ 0 , 1 ]$

6. The users' delay cost, v, is assumed to be 1. This entails no loss of generality, but it implies that k and θ are correspondingly scaled by v.

We consider three cases in addition to the optimal mechanism. In order to have some benchmarks, we also provide results for the perfect information case, which of course is not in general attainable (however, see the “Discussion"section below), and two cases which are attainable, the profit center, and the “naive" mechanism. Under the naive mechanism the central management accepts whatever report the IS manager gives, and sets capacity and arrival rate accordingly. This corresponds to an extreme case of bounded rationality (Simon 1961, Williamson 1985) with the central management failing to realize there is any incentive problem. Of course the revelation principle guarantees that the expected net value of the optimal mechanism will exceed that of either the profit center or the naive mechanism, but this result is gross of any costs of computation and communiçation. Thus if either of these suboptimal alternatives is not too inferior to the optimal mechanism, they could in fact be superior once these additional costs are included.

The results for this example are summarized in Table 2, and numerical results for a particular case are shown in Table 3. More detailed discussion follows below.

Incomplete Information with Optimal Mechanism. Since $C _ { \theta \mu \theta } = 0$ and $\beta ^ { \prime } ( \theta ) > 0 $ the optimal mechanism given in Proposition 2 is feasible for this example. Also, if k $> \forall \gamma ( \theta )$ for all θ in θ, where $\gamma ( \theta ) = \theta + \xi \beta ( \theta ) = \theta + \xi ( \theta - \underline { { { \theta } } } )$ is the virtual marginal capacity cost, $\mu ^ { * } ( \theta )$ is strictly decreasing in θ, so the monotonicity constraint is satisfied.

The optimal lump-sum budget allocation to the IS department is

$$
T ^ {*} (\theta) = \theta \mu^ {*} (\theta) + \int_ {\theta} ^ {\bar {\theta}} \mu^ {*} (\tilde {\theta}) d \tilde {\theta}.
$$

Therefore the informational rent of the IS manager equals $\xi \int _ { \theta } ^ { \bar { \theta } } \mu ^ { * } ( \tilde { \theta } ) d \tilde { \theta }$ . Obviously, as asserted by Lemma 1, this informational rent is strictly decreasing in θ and equals zero when $\theta = { \overline { { \theta } } } .$

Note that the optimal utilization rate $\rho ^ { * } ( \theta ) \equiv \lambda ^ { * } ( \theta ) / \mu ^ { * } ( \theta )$ is decreasing in θ while the optimal waiting time $W ^ { * } ( \theta ) \equiv 1 / ( \mu ^ { * } ( \theta ) - \lambda ^ { * } ( \theta ) )$ is increasing in θ. So, when the IS department is more efficient, the system response time should be shorter even though the system is running with a heavier load. Nevertheless the aggregate users delay $\lambda ^ { * } ( \theta ) W ^ { * } ( \theta )$ is decreasing in $\vartheta . ^ { \ast }$

A Fully Informed Central Management: An Upper Benchmark. The optimal solution of the full-information case can be obtained by replacing $\gamma ( \theta )$ by θ. Thus, from Table 2, it is readily verified that when the central management is fully informed. the

TABLE 2

Summary of the Four Cases in the Example

$$
p ^ {*} (\theta) = \gamma (\theta) = \theta + \xi (\theta - \underline {{{{\theta}}}})\tag{p(θ}
$$

$$
p ^ {i} (\theta) = \theta
$$

$$
p ^ {p} (\theta) = \frac {2 \theta (k - \sqrt {\theta})}{k - 2 \sqrt {\theta}}
$$

$$
p ^ {n} (\theta) = \theta^ {n}\tag{\(\lambda (\theta)\}
$$

$$
\lambda^ {*} (\theta) = \left[ \frac {k - \sqrt {\gamma (\theta)}}{\gamma (\theta)} \right] ^ {2}
$$

$$
\lambda^ {\prime} (\theta) = \left[ \frac {k - \sqrt {\theta}}{\theta} \right] ^ {2}
$$

$$
\lambda^ {p} (\theta) = \left[ \frac {k - 2 \sqrt {\theta}}{2 \theta} \right] ^ {2}
$$

$$
\lambda^ {n} (\theta) = \left[ \frac {k - \sqrt {\theta^ {n}}}{\theta^ {n}} \right] ^ {2}\tag{\(\mu (\theta)\}
$$

$$
\mu^ {*} (\theta) = \frac {k (k - \sqrt {\gamma (\theta)})}{\gamma (\theta) ^ {2}}
$$

$$
\mu^ {i} (\theta) = \frac {k (k - \sqrt {\theta})}{\theta^ {2}}
$$

$$
\mu^ {p} (\theta) = \frac {k (k - \sqrt {2 \theta})}{4 \theta^ {2}}
$$

$$
\mu^ {n} (\theta) = \frac {\lambda (k - \sqrt {\theta^ {n}})}{\theta^ {n 2}}
$$

E{NV(θ)}

$$
E \{N V ^ {*} \} = \int_ {\Theta} \gamma (\theta) \lambda^ {*} (\theta) d F (\theta)
$$

$$
E \{N V ^ {\prime} \} = \int_ {\Theta} \theta \lambda^ {\prime} (\theta) d F (\theta)
$$

$$
E \{N V ^ {p} \} = \int_ {\Theta} \left\{k \sqrt {\lambda^ {p} (\theta)} + (1 - \xi) \theta \lambda^ {p} (\theta) \right\} d F (\theta)
$$

$$
E \{N V ^ {n} \} = \int_ {\Theta} \theta^ {n} \lambda^ {n} (\theta) d F (\theta)
$$

optimal subsidy to the IS department, $\theta ( \mu ^ { \prime } ( \theta ) - \lambda ^ { \prime } ( \theta ) )$ , equals the aggregate users delay cost, $\lambda ^ { \prime } ( \theta ) / ( \mu ^ { \prime } ( \theta ) - \lambda ^ { \prime } ( \theta ) )$ ). This conforms to the usual optimality condition for an $M / M / 1$ queueing system with linear users’ delay cost and capacıty cost (Dewan and Mendelson 1990).

Discussion. The effects of the information asymmetry can now be clearly seen. For every $\theta , N \Gamma ^ { \prime \prime } ( \theta ) > N \Gamma ^ { \prime \ast } ( \theta )$ and

$$
\begin{array}{r l} \lambda^ {*} (\theta) & \leq \lambda^ {t} (\theta); \quad \mu^ {*} (\theta) \leq \mu^ {t} (\theta); \quad p ^ {*} (\theta) \geq p ^ {t} (\theta); \\ \rho^ {*} (\theta) & \leq \rho^ {t} (\theta); \quad W ^ {*} (\theta) \geq W ^ {t} (\theta) \end{array}
$$

March 1995

<table><tr><td> $\theta$ </td><td> $λ^t$ </td><td> $λ^*$ </td><td> $λ^n$ </td><td> $λ^p$ </td><td> $μ^t$ </td><td> $μ^*$ </td><td> $μ^n$ </td><td> $μ^p$ </td><td> $p^t$ </td><td> $p^*$ </td><td> $p^n$ </td><td> $p^p$ </td></tr><tr><td>1.0</td><td>16.00</td><td>16.00</td><td>3.91</td><td>2.25</td><td>20.00</td><td>20.00</td><td>5.36</td><td>3.75</td><td>1.00</td><td>1.00</td><td>1.84</td><td>2.67</td></tr><tr><td>1.2</td><td>10.59</td><td>8.82</td><td>3.21</td><td>1.37</td><td>13.56</td><td>11.41</td><td>4.48</td><td>2.44</td><td>1.20</td><td>1.30</td><td>2.00</td><td>3.25</td></tr><tr><td>1.4</td><td>7.43</td><td>5.45</td><td>3.21</td><td>0.88</td><td>9.74</td><td>7.30</td><td>4.48</td><td>1.68</td><td>1.40</td><td>1.60</td><td>2.00</td><td>3.83</td></tr><tr><td>1.6</td><td>5.45</td><td>3.63</td><td>3.21</td><td>0.60</td><td>7.30</td><td>5.02</td><td>4.48</td><td>1.21</td><td>1.60</td><td>1.90</td><td>2.00</td><td>4.40</td></tr><tr><td>1.8</td><td>4.13</td><td>2.56</td><td>3.21</td><td>0.41</td><td>5.65</td><td>3.63</td><td>4.48</td><td>0.89</td><td>1.80</td><td>2.00</td><td>2.00</td><td>4.97</td></tr><tr><td>2.0</td><td>3.21</td><td>1.87</td><td>3.21</td><td>0.29</td><td>4.48</td><td>2.74</td><td>4.48</td><td>0.68</td><td>2.00</td><td>2.50</td><td>2.00</td><td>5.53</td></tr><tr><td> $θ$ </td><td> $W^t$ </td><td> $W^*$ </td><td> $W^n$ </td><td> $W^p$ </td><td> $ρ^t$ </td><td> $ρ^*$ </td><td> $ρ^n$ </td><td> $ρ^p$ </td><td> $S^t$ </td><td> $S^*$ </td><td> $S^n$ </td><td> $π^p$ </td></tr><tr><td>1.0</td><td>0.25</td><td>0.25</td><td>0.69</td><td>0.67</td><td>0.80</td><td>0.80</td><td>0.73</td><td>0.60</td><td>0.00</td><td>7.55</td><td>4.52</td><td>2.25</td></tr><tr><td>1.2</td><td>0.33</td><td>0.38</td><td>0.79</td><td>0.94</td><td>0.78</td><td>0.77</td><td>0.72</td><td>0.56</td><td>0.00</td><td>4.52</td><td>3.59</td><td>1.64</td></tr><tr><td>1.4</td><td>0.43</td><td>0.54</td><td>0.79</td><td>1.26</td><td>0.76</td><td>0.75</td><td>0.72</td><td>0.53</td><td>0.00</td><td>2.70</td><td>2.69</td><td>1.24</td></tr><tr><td>1.6</td><td>0.54</td><td>0.72</td><td>0.79</td><td>1.64</td><td>0.75</td><td>0.72</td><td>0.72</td><td>0.49</td><td>0.00</td><td>1.49</td><td>1.79</td><td>0.95</td></tr><tr><td>1.8</td><td>0.66</td><td>0.93</td><td>0.79</td><td>2.08</td><td>0.73</td><td>0.70</td><td>0.72</td><td>0.46</td><td>0.00</td><td>0.63</td><td>0.90</td><td>0.75</td></tr><tr><td>2.0</td><td>0.79</td><td>1.16</td><td>0.79</td><td>2.60</td><td>0.72</td><td>0.68</td><td>0.72</td><td>0.43</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.59</td></tr><tr><td> $θ$ </td><td> $U^t$ </td><td> $U^*$ </td><td> $U^n$ </td><td> $U^p$ </td><td> $NV^t$ </td><td> $NV^*$ </td><td> $NV^n$ </td><td> $NV^p$ </td><td> $TNV^t$ </td><td> $TNV^*$ </td><td> $TNV^n$ </td><td> $TNV^p$ </td></tr><tr><td>1.0</td><td>0.00</td><td>3.78</td><td>2.26</td><td>1.13</td><td>16.00</td><td>12.22</td><td>7.20</td><td>8.63</td><td>16.00</td><td>16.00</td><td>11.72</td><td>9.76</td></tr><tr><td>1.2</td><td>0.00</td><td>2.26</td><td>1.79</td><td>0.82</td><td>12.70</td><td>10.34</td><td>6.43</td><td>6.67</td><td>12.70</td><td>12.60</td><td>10.01</td><td>7.49</td></tr><tr><td>1.4</td><td>0.00</td><td>1.35</td><td>1.34</td><td>0.62</td><td>10.41</td><td>8.83</td><td>6.43</td><td>5.32</td><td>10.41</td><td>10.18</td><td>9.12</td><td>5.94</td></tr><tr><td>1.6</td><td>0.00</td><td>0.74</td><td>0.90</td><td>0.48</td><td>8.72</td><td>7.66</td><td>6.43</td><td>4.34</td><td>8.72</td><td>8.40</td><td>8.22</td><td>4.82</td></tr><tr><td>1.8</td><td>0.00</td><td>0.31</td><td>0.45</td><td>0.37</td><td>7.44</td><td>6.76</td><td>6.43</td><td>3.59</td><td>7.44</td><td>7.07</td><td>7.33</td><td>3.96</td></tr><tr><td>2.0</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.29</td><td>6.43</td><td>6.04</td><td>6.43</td><td>3.01</td><td>6.43</td><td>6.04</td><td>6.43</td><td>3.30</td></tr><tr><td colspan="13"> $E\{NV^t\} = 10.1 \text{(Full Information)}$   $E\{NV^*\} = 8.52 \text{(Optimal Mechanism)}$   $E\{NV^n\} = 6.45 \text{(Naive)}$   $E\{NV^p\} = 5.12 \text{(Profit Center)}$ </td></tr></table>

with equality holding at $\theta = \underline { { \theta } } .$ , the “no distortion at the bottom” property.

Thus, when $\theta = \underline { { \theta } }$ , the system is operating at its full efficiency; however, the ex post informational rent of the IS department is also the largest (also see Figure 2). On the other hand., when $\theta \ = \ { \overline { { \theta } } } ,$ the state of the system is set by taking full account of the virtual informational rent. $\xi ( \bar { \theta } - \underline { { { \theta } } } ) \mu ^ { * } ( \bar { \theta } )$ , but the IS manager's ex post informational rent equals zero. Intuitively, the central management attempts to distort the capacity decision so that the informational rent can be reduced when θ is low. Hence, even when the IS department has no way to overstate its cost $\displaystyle ( \operatorname { i } . \mathrm { e } . . \theta = \breve { \theta } )$ ), the capacity is set at a level as if the marginal cost $\gamma ( { \bar { \theta } } ) = { \bar { \theta } } + \xi ( { \bar { \theta } } - \underline { { { \theta } } } )$ . By distorting the capacity decision, the central management is able to make overstating the cost parameter relatively unattractive, reducing the IS department's incentive for misrepresentation.

Even in the presence of asymmetric information $\left( \lambda ^ { \prime } ( \theta ) , \mu ^ { \prime } ( \theta ) \right)$ is feasible since $\mu ^ { \prime } ( \theta )$ is decreasing in θ. However, the mechanism implementing the full information outcome is not optimal because of the excess budget required to induce truth revelation. In order to induce the IS manager's truth-revelation while implementing $( \lambda ^ { \prime } ( \theta )$ $\mu ^ { \iota } ( \theta ) )$ , the central management needs to set:

$$
S (\theta) = \int_ {\theta} ^ {\bar {\theta}} C _ {\theta} (\mu^ {t} (\tilde {\theta}), \tilde {\theta}) d \hat {\theta},
$$

which will give the IS manager too large an informational rent, leaving the organization worse off.

The Profit Center. From §3.2, the optimal incentive scheme is $\xi \pi .$ , so that $U ( \theta )$ $= \xi \pi ( \theta )$ , where

$$
\pi (\theta) = \max _ {\lambda , \mu} \lambda (V ^ {\prime} (\lambda) - W ^ {\prime} (\lambda , \mu)) - C (\mu , \theta)
$$

which, in this example, has a unique maximum $\mathrm { i f } k > 2 \sqrt { \theta }$ . Assuming this is the case, Table 2 shows that the monopolistic price, $p ^ { p } ( \theta )$ , is more than double the net value maximizing price, θ, even though $p ^ { p } ( \theta )$ is determined based on the true cost. Also, since the IS department's revenue is

$$
p ^ {p} (\theta) \lambda^ {p} (\theta) = \theta (\lambda^ {p} (\theta) + \mu^ {p} (\theta)).
$$

the IS department's profit is $\theta \lambda ^ { p } ( \theta )$

Furthermore, the utilization rate of the system under the profit center is $\rho ^ { p } ( \theta ) = ( k$ $- \ 2 \sqrt { \theta } ) / k$ . Since $\xi \in [ 0 , 1 ]$ , and thereby $\sqrt { \gamma ( \theta ) } < 2 \sqrt { \theta }$ , the profit center will have a lower utilization rate for all θ compared with the cost center. Whether the mean waiting time is larger or smaller under the profit center is less obvious, however. It can be shown that if θ is very wide and ξis close to one, the extent of the distortion in the case of the cost center will be substantial when θ is large, so the mean waiting time under the cost center can become larger than that under the profit center. In most other cases, users will suffer a longer delay when the IS department is organized as a profit center, as well as being charged a higher price. In any case, because $V ^ { \prime } ( \lambda ^ { p } ( \theta ) )$ $> V ^ { \prime } ( \lambda ^ { * } ( \theta ) )$ , the total cost per job incurred by the users under the profit center will be larger than that under the cost center. Consequently, we may expect the users to press the central rnanagement to reorganize the IS department as a cost center.

A Naive Central Management: A Lower Benchmark. Under mild conditions on the support of θ and the demand parameter, k, it can be shown that the IS manager's optimal reporting strategy leads to the equation:

$$
\begin{array}{l} \theta = \hat {\theta} \left[ 1 - \frac {2 k - 2 \sqrt {\bar {\theta}}}{4 k - 3 \sqrt {\bar {\theta}}} \right] \\ \equiv g (\hat {\theta}). \end{array}\tag{4.1}
$$

For $k > \sqrt { \hat { \theta } } , g ( \hat { \theta } )$ is increasing, and $g ( \theta ) < \theta$ . Thus, $g ( { \hat { \theta } } )$ is invertible, and for all $\theta > 0 ;$ (4.1) has a unique solution $\hat { \boldsymbol { \theta } } ( \boldsymbol { \theta } ) = \boldsymbol { g } ^ { - 1 } ( \boldsymbol { \theta } )$ . Consequently, $\mathrm { i f } \hat { \theta } ( \theta ) \geq \overline { { \theta } }$ for all $\theta \in { \mathbf { \Theta } } _ { \Theta }$ , the IS manager will always report $\hat { \theta } ( \theta ) = \bar { \theta } ;$ if there is a $\theta ^ { o } \in ( \underline { { \theta } } , \overline { { \theta } } )$ such that $\widehat { \theta } ( \theta ^ { o } ) = \overline { { { \theta } } } _ { ; }$ , the IS manager's optimal reporting strategy is

$$
\theta^ {n} (\theta) = \left\{ \begin{array}{l l} \bar {\theta} & \text {   if   } \quad \theta \geq \theta^ {o} \\ \hat {\theta} & \text {   where   } \quad g (\hat {\theta}) = \theta \quad \text {   for   } \quad \theta \in [ \underline {{\theta}}, \theta^ {o}). \end{array} \right.
$$

## 4.1. Numerical Results

We provide numerical results for the case where $k = 5 , \xi = 0 . 5$ and $\mathbf { \theta } \mathbf { \theta } = [ 1 , 2 ]$ in Table 3 and Figures 1 to 3. Since $\xi \in [ 0 , 1 ] , \xi = 0 . 5$ corresponds to a moderate level of incentive conflict. Since θ is the marginal capacity cost $( \mathsf { M C C } )$ here, and θ is measured in units of the users’ delay cost parameter, v, $\theta = 1$ implies that the central management's lower bound on the MCC equals v. This lower bound must be at least as large as the hardware component of MCC, so the value mentioned in Assumption 3 at the start of the example corresponds roughly to $\pmb { v } = \$ 7.50$ per hour, which we can take to be approximately equal to the average user's wage rate. Thus $\theta = 1$ is consistent with any wage rate of at least \$7.50 per hour. The value of k is also measured in units of v, but it is not quite as easy to interpret as θ since the marginal value of jobs depends on λ. The maximum λ in Table 3 implies that the gross value of computing is \$40v per period, so if $v = \$ 15$ per hour, this is about \$1.25 million per year, a fairly modest amount. As a result, the numerical values used model a modest computing facility.

Figure 1 shows the distortion in capacity caused by the information asymmetry. Figure 3 shows that in this example the ex post organizational net value is higher under the optimal mechanism than under the profit center for all values of θ. (The revelation principle implies that the expected net value under the optimal mechanism must be higher than for the profit center, but not necessarily that the ex post net value be higher for all values of θ.) Interestingly, Figure 2 shows that over most of $\mathbf { \nabla } \cdot \mathbf { \nabla } \theta ^ { * } \mathbf { s }$ range the IS manager's utility is also significantly higher under the optimal mechanism than it is under the profit center; the IS manager will prefer a profit center only when she runs a high-cost operation. Clearly the restriction in capacity (and output) under the profit center is severe enough to make her informational rent very low, and this restriction has a similarly bad effect on the organization as a whole. This is apparent in the TNV panel of Table 3, which shows that the profit center yields a much smaller total $\ " \mathrm { p i e } \ "$ which adversely affects all participants. Conversely, the optimal mechanism yields TNV's which are a very large fraction of the full-information case. Thus it is clear from the vastly inferior performance of the profit center versus the optimal mechanism that a smaller informational rent for the IS manager by itself is not necessarily organizationally beneficial. Also note from Figure 2 that the amounts paid to the IS manager under the optimal mechanism are not extreme, lying between zero and about \$117.000 per year if $v = \$ 15$ per hour, and amounting to about \$34,000 per year at the expected θ of 1.5.

![](/api/attachments/N5TF662C/fulltext/images/7c7052dea67cbcd886941d94711e6b1c2dcf5a94c8dae3246b4c3bae406d1426.jpg)  
FIGURE 1. μ(θ) with $k = 5 ; \xi = 0 . 5 ; \Theta = [ 1 , 2 ] ; \iota$ v = 1. The behavior of λ(θ) ın each case looks very sımilar to that of µ(θ).

The preceding discussion implies that a profit center will generally be disliked by all three major participants, namely the users, the central management, and the IS manager. lt is then perhaps not surprising to see the majority of firms organizing IS departments as cost centers (McGee 1988). There are, however, two important assumptions behind this conclusion: (1) no external market access, and (2) unlimited communication between the IS manager and the central management.

## 5. Implications and Future Research Directions

The maor technical contributions of the paper stem from Proposition 2, which shows that the first-order conditions of the full-information problem, first established by Mendelson (1985), generalize in a clear and elegant way to the case of cost information asymmetry and incentive conflict by replacing the “true" marginal capacity cost by its virtual counterpart. Furthermore, as was shown in Appendix B, the approach is robust to uncertainty about the degree of professionalism characterizing the IS manager. Also, Wang (1991) shows the approach is robust to relaxing the assumption of continuously variable capacity used in this paper to allow for discrete capacity choices. Although discreteness impairs the performance of the optimal mechanism, it can in fact improve the performance of a profit center, depending on the set of available systems (Wang 1991). Nevertheless, by the revelation principle, the discreteness of system capacity will not cause the profit center to outperform the cost center governed by the optimal mechanism. On the other hand, although under unlimited, costless communication, the optimal centralized mechanism gives the maximal net value that an IS department can generate under any organizational arrangement, the profit center can be preferable if communicating cost information is very costly or limited, as shown in Wang (1991).

![](/api/attachments/N5TF662C/fulltext/images/8666132669a4c31926d2770e941adda72c270ba80afe151d5b339b643db25829.jpg)  
FIGURE 2. U(θ) with k = 5: ξ = 0.5; θ = [1, 2], v = 1.

There are several managerial implications of the results. First, it was shown that these incentive problems lead to reduced capacity, arrival rate and utilization rate, and higher prices and mean waiting time compared to the full-information solution. Thus the organization suffers losses due not only to the IS manager's informational rent, but also to the opportunity cost of jobs not served. Furthermore, users suffer the costs of higher prices and more waiting time. Several factors are important in the central management's attempts to control these problems: (1) information on the possible range of capacity costs, especially a good upper bound, (2) an idea of the degree of incentive conflict between the IS manager and central management, (3) the ability of the central management to make credible commitments, and (4) information about the gross value of computing to the organization. It is worth noting that elevating the head of the IS group to a central management position such as CIO will be likely to have a beneficial effect on all of these. In particular, regarding point (2), this step can both help to align incentives, thereby reducing the degree of conflict in the first place, and also provide others in the central management with better information about the IS manager's preferences. Furthermore, since the magnitude of the loss is increasing in the scale of the IS resources, one would expect such arrangements to be most common in larger organizations.

![](/api/attachments/N5TF662C/fulltext/images/357ec7c1d7e0a4cdbde9f70884d0ae36920f873d7cfeda53ee3e377ed293a419.jpg)  
FIGURE 3. NV(θ) with k = 5; ξ = 0.5; θ = [1. 2], v = 1.

Second, the revelation principle guarantees that in the presence of cost information asymmetry and incentive conflicts, a cost center governed by the optimal mechanism will be superior to any other organizational alternative for IS services by the criterion of the expected net value of the resource. Interestingly, this result holds despite the fact that with a profit center the “true" rather than the virtual cost is used. The example and numerical results give evidence that the difference in performance between the optimal mechanism and two practical competitors, a profit center and a naively governed cost center, is indeed significant. This coincides with the observed (low) frequency of profit centers in organizations (McGee 1988).

Third, it is important for central management to recognize that organizational slack is the inevitable result of information asymmetry, and focusing solely on its reduction is not always desirable. It was seen in the example that the profit center is very effective in limiting the IS manager's informational rent, but it also yielded the least organizational net value. Under the optimal mechanism, all the parties (users, IS manager and the organization) will nearly always be better off than under a profit center. Also, our results suggest that organizational performance should on average be better with direct compensation for reported cost savings rather than allowing the IS manager to consume all of the slack. Thus we should expect organizations having such incentive schemes to have better-performing IS departments than those without them.

Methodologically, mechanism design allows a number of other IS management problems to be studied more rigorously than was previously possible. For example, Barron and Wang (1992) studies the effects of the presence of an external option on the expected organizational net value and on the IS manager's informational rent, and derives decision rules for outsourcing. When the profit center's pricing decision is bounded by the external price, changing the organization of the IS department from a cost center to a profit center is similar to changing a cost-plus contract to a fixed-price contract; the efficient usage of the organization's resource is encouraged and the organizational net value may improve ex post.

More generally, mechanism design is very useful in analyzing bargaining situations such as contracting for software development, and analyzing relationship-specific IS investments. The revelation principle not only generates the welfare upper-bound for the mechanism designer but can make complex problems more tractable as well. Mechanism design can also be extended to multiagent settings, so that it is possible to study IS resource allocation problems such as controlling networks and distributed computing, and issues in downsizing and system integration.\*

Acknowledgments. The authors thank the Associate Editor and the two referees for their many useful comments on earlier versions of the paper; it has been greatly improved as a result.

\*Rajiv Banker, Associate Editor. This paper was received on September 19, 1991, and has been with the authors 4 months for 2 revisions.

## Appendix A. Proofs

PROOF OF PROPOSITION I

We prove this proposition in its most general form. i.e., no differentiability is assumed for the functions. We show that (2.6) does not satisfy (3.1). Consider any two distınct possible realizations of θ: $\theta _ { 1 } , \theta _ { 2 } \in \Theta$ with $\theta _ { 2 } > \theta _ { 1 } . \operatorname { L e t } \lambda _ { i } = \lambda ( \theta _ { i } ) , \mu _ { i } \equiv \mu ( \theta _ { i } ) . R _ { t } \equiv R ( \lambda _ { i } , \mu _ { i } )$ , and $T _ { \cdot } \equiv T ( \boldsymbol { \theta } _ { \cdot } )$ for $l \ = \ 1 , 2 .$ Inducing the IS manager's truth-reporting requires

$$
S (\theta_ {1}; \theta_ {1}) \geq S (\theta_ {2}; \theta_ {1}), \quad S (\theta_ {2}; \theta_ {2}) \geq S (\theta_ {1}; \theta_ {2}),
$$

which by the definition of S(·), together with the subsıdy rule (2.6) which says $T _ { \iota } = C ( \mu _ { \iota } , \theta _ { \iota } ) - R _ { \iota }$ for 1 $\mathbf { \Omega } = \mathbf { \Omega } 1 , 2 .$ ımply

$$
0 \geq C (\mu_ {2}, \theta_ {2}) - C (\mu_ {2}, \theta_ {1}), \quad 0 \geq C (\mu_ {1}, \theta_ {1}) - C (\mu_ {1}, \theta_ {2}).
$$

But $C ( \mu , \theta )$ is increasing in θ and $\theta _ { 2 } > \theta _ { 1 }$ imply $C ( \mu _ { 2 } , \theta _ { 2 } ) > C ( \mu _ { 2 } , \theta _ { 1 } )$ ) and $C ( \mu _ { 1 } , \theta _ { 2 } ) > C ( \mu _ { 1 } , \theta _ { 1 } )$ . Hence, the first inequality is violated, and thereby if the central management follows the rule (2.6), the manager wilf overreport the realized θ.

PROOF OF IEMMA 2. From the linear structure of the IS manager's utılıty function, it is obvious that $\phi ( S ) = S 1 \mathbf { f } B ( S , { \hat { \theta } } ) \geq \xi S$ and that q $\gamma ( S ) = 0 1 \mathrm { f } B ( S , \hat { \theta } ) < \xi S$ . Then beçause the central management values S(θ) fullv and bv assumption $\xi \in [ 0 , 1 ] , 1 1$ is obvious that $B \big ( \psi \big ) \simeq \xi \phi$ , and the central management always unduces the IS manager to take the reward from cost saving: $( \mathrm { i . e . , } \phi ^ { * } ( S ) = S )$

PRoOF OF PRoPosrTiON 2. Maximızing (3 8) pointwise with respect to λ and μ gives the following first-order conditions:

$$
\partial H / \partial \lambda = V ^ {\prime} (\lambda) - v W ^ {\prime} (\lambda , \mu) - v \lambda W _ {\lambda} ^ {\prime} (\lambda , \mu) = 0,
$$

$$
\partial H / \partial \mu = - v \lambda W _ {\mu} ^ {\prime} (\lambda , \mu) - C _ {\mu} (\mu , \theta) - \xi \beta (\theta) C _ {\theta \mu} (\mu , \theta) = 0.
$$

Letting $\mu ^ { * } ( \theta )$ denote the optimal capacity, we now show that $\iota / \mu ^ { * } ( \beta ) / d \beta \leq 0$ provided the assumptions hold. Let  be the Hessian matrix of I, and bv the implicit function theorem (see, e.g., Mas-Colell 1985)

$$
\left[ \frac {d \lambda^ {*} (\theta)}{d \theta} \frac {d \mu^ {*} (\theta)}{d \theta} \right] ^ {T} = - \mathcal {H} ^ {- 1} [ H _ {\lambda \beta} H _ {\omega \theta} ] ^ {I}
$$

where the superscript T denotes transpose. Writing out the right-hand side of this equation, gives

$$
- \frac {1}{| \mathcal {H} |} \left[ \begin{array}{c c} H _ {\mu \mu} & - H _ {\mu \lambda} \\ - H _ {\lambda \mu} & H _ {\lambda \lambda} \end{array} \right] \left[ \begin{array}{l} H _ {\lambda \theta} \\ H _ {\mu \nu} \end{array} \right]
$$

where $\{ \mathcal { H } \}$ 1s the determinant of $\mathcal { H }$ . Since $\mathcal { H }$ is assumed to be negative definite, $\mid \mathcal { H } \mid$ is positive. Because only $\mu ^ { * } ( \theta )$ is required to be nonincreasing, the incentive constraint is satisfied $1 \mathbf { f } - I I _ { \lambda \mu } I I _ { \lambda \theta } + H _ { \lambda \lambda } H _ { \mu \theta }$ $\geq 0 .$ But ${ \cal { H } } _ { \lambda \theta } ~ = 0$ and $H _ { \lambda \lambda } < 0$ , and thereby $\mu ( \beta )$ is nonincreasing if ${ \cal { H } } _ { \mu \nu } \leq 0$ But

$$
I I _ {\mu \theta} = C _ {\theta \mu} (1 + \xi \beta^ {\prime} (\theta)) - \xi \beta (\theta) C _ {\theta \mu \theta}
$$

and thereby $\{ 3 9 \}$ is satisfied provided that the second assumption holds. Thus from Lemma 1, the optimal mechanism is globally incentive compatible $\hat { \Gamma } \mu ^ { * } ( \theta )$ is nonincreasing in $\theta _ { \star } ^ { \ 6 }$

Finally, the optimal price follows directly from (3.10) This compietes our proof. }

## Appendix B. Imperfect Information about ξ

When the central management is uncertain about $\xi .$ let the probabilty distribution $G ( \xi )$ be their prior beliefs about $\xi , G ( \xi )$ is assumed to be twice continuously differentiable and has a density function $g ( \xi ) > 0$ if and only $\mathfrak { t f } \xi \in [ 0 , \ 1 ]$ . Let

$$
\begin{array}{r l} H ^ {+} (\lambda , \mu , \theta , \eta) & =: V (\lambda) - v \lambda W (\lambda , \mu) - C (\mu , \theta) - \eta \beta (\theta) C _ {\theta} (\mu , \theta), \\ H ^ {-} (\lambda , \mu , \theta) & =: V (\lambda) - v \lambda W (\lambda , \mu) - C (\mu , \theta) - \beta (\theta) C _ {\theta} (\mu , \theta). \end{array}
$$

The linear structure of the IS manager's utility function implies that she will consume all the organızational slack if and only if $\eta < \xi ,$ so the virtual organizational net value equals $H ^ { + } ( \lambda , \mu . \ A , \eta ) { \mathfrak { s } } \mathfrak { s } \mathfrak { s } \mathfrak { s } \mathfrak { s } \mathfrak { s }$ and equals $H _ { \mathrm { ~ \tiny ~ \left( ~ \lambda , ~ \right)} \mu , \ \theta  }$ otherwise, making the central management's problem:

$$
\max _ {\lambda (\theta), \mu (\theta), \eta \in [ 0, 1 ]} \int_ {\Theta} \left\{G (\eta) H ^ {+} (\lambda , \mu , \theta , \eta) + [ 1 - G (\eta) ] H ^ {-} (\lambda , \mu , \theta) \right\} d F (\theta)\tag{B.1}
$$

Observe that, for any μ and θ, the virtual capacity cost is:

$$
C (\mu , \theta) + [ 1 - (1 - \eta) G (\eta) ] \beta (\theta) C _ {\theta} (\mu , \theta),
$$

so that the optimal η can be determined by mınimızing:

$$
1 - (1 - \eta) (\tilde {J} (\eta).\tag{B.2}
$$

Since $1 - ( 1 - \eta ) G ( \eta ) \in [ 0 , 1 ]$ and reaches its maximum of 1 at the boundaries of the support of $\eta .$ ımplying an interior solution for η. Differentiating (B.2) and equating the result to zero gives

$$
0 \equiv G (\eta) = (1 - \eta) g (\eta) | _ {\eta = \eta^ {*}} \Rightarrow \frac {g (\eta^ {*})}{G (\eta^ {*})} = \frac {1}{1 - \eta^ {*}}\tag{B.3}
$$

To ensure that $( \mathtt { B } . 2 )$ is convex and thereby (B.3) gives a global minimum, we need the second-order condition:7

6Note that given $C _ { \theta \mu \theta } \geq 0$ and the assumption that $C _ { \mu \theta } > 0 .$ , the sign of $H _ { \mu \theta }$ depends on the sign of $\beta ^ { \prime } ( \theta )$ $= ( f ( \theta ) ^ { 2 } - F ( \theta ) f ^ { \prime } ( \theta ) \big ) / f ( \theta ) ^ { 2 } . \mathrm { S o } , \beta ( \theta )$ is increasing if and only if for all θ: $F ( \theta ) / f ( \theta ) < f ( \theta ) / f ^ { \prime } ( \theta )$ . This condition, the monotone hazard rate condition, is implied by the monotone likelihood ratio property Thus, whenever the distribution function satisfies the monotone likelihood ratio property, we know that the hazard rate β(θ) is increasing, and thereby the monotonicity constraint (3.9) is satisfied for all θ This property is satisfied by many families of probability distrıbutions, e.g., the normal, the exponential, the Poisson, and the unıform, etc. For details, see Milgrom (1982).

7 We thank one of the referees for helpful suggestions in the following line of argument

$$
2 g (\eta) - (1 - \eta) g ^ {\prime} (\eta) > 0, \quad \forall \eta \in [ 0, 1 ] \quad \text { or }
$$

$$
\frac {g ^ {\prime} (\eta)}{g (\eta)} <   \frac {2}{1 - \eta}.\tag{B.4}
$$

Note that $g ( \eta ) / G ( \eta )$ is the inverse hazard rate, and it is decreasing if and only if

$$
\frac {g (\eta)}{G (\eta)} > \frac {g ^ {\prime} (\eta)}{g (\eta)}.
$$

Then (B.3) yields a global minimum if $g ( \eta ) / G ( \eta )$ is monotone decreasing, since

$$
\frac {2}{1 - \eta} > \frac {1}{1 - \eta} = \frac {g (\eta)}{G (\eta)} > \frac {g ^ {\prime} (\eta)}{g (\eta)}.
$$

Because

$$
\frac {d}{d \eta} \ln g (\eta)) = \frac {g ^ {\prime} (\eta)}{g (\eta)} \quad \text { and } \quad - 2 \frac {d}{d \eta} \ln (1 - \eta)) = \frac {2}{1 - \eta},
$$

the second-order condition is satisfied if and only if ln g( η) does not increase faster than -2 ln(1 – η) does This holds it $\dot { \boldsymbol g } ( \boldsymbol \eta )$ is decreasing or a constant, $\mathrm { i . e . , } G ( \eta )$ is (weakly) concave. On the other hand, if (B.4) does not hold globally, (B.2) can be concave over some range, so the first-order condition will yield a local maximum. Assuming that the second-order condition is satisfied, substituting (B.3) ınto (B.2) yields

$$
\alpha (\eta^ {*}) \equiv 1 - \frac {G (\eta^ {*}) ^ {2}}{g (\eta^ {*})}.
$$

To derive the optimal mechanism, maximizing (B.1) pointwise with respect to λ and $\pmb { \mu }$ yields the following first-order conditions

$$
0 = V ^ {\prime} (\lambda) - v W (\lambda , \mu) - v \lambda W _ {\lambda} (\lambda , \mu),\tag{B.6}
$$

$$
0 = - v \lambda W _ {\mu} (\lambda , \mu) - C _ {\mu} (\mu , \theta) - \alpha (\eta^ {*}) \beta (\theta) C _ {\theta \mu} (\mu , \theta).\tag{B.7}
$$

As shown in Propositior $2 , \mu ( \theta )$ is decreasing if

$$
[ 1 + \alpha (\eta^ {*}) \beta^ {\prime} (\theta) ] C _ {\theta \mu} + \alpha (\eta^ {*}) \beta (\theta) C _ {\theta \mu \theta} > 0,
$$

which is satisfied if both β(θ) and $C _ { \theta \mu } ( \mu , \theta )$ ) are nondecreasing in θ. Assume this is the case. We now can give the first-order condition (B.3) a more intuitive interpretation

$\boldsymbol { \mathbf { B } } \mathbf { y }$ the envelope theorem, differentiating (B.1) with respect to η totally and equating it to zero gives:

$$
0 = g (\eta) \left\{\int_ {\Theta} \left[ H ^ {+} (\lambda , \mu , \theta , \eta) - H ^ {-} (\lambda , \mu , \theta) \right] d F (\theta) \right\} - G (\eta) \int_ {\Theta} \frac {\partial H ^ {+} (\lambda , \mu , \theta , \eta)}{\partial \eta} d F (\theta).\tag{B.8}
$$

From (B.8), we see that an increase in η increases the likelihood that the IS manager will get the pecuniary reward, and thereby the expected organizational net value is increased by

$$
g (\eta) \left\{\int_ {\Theta} \left[ H ^ {+} (\lambda , \mu , \theta , \eta) - H ^ {-} (\lambda , \mu , \theta) \right] d F (\theta) \right\} = g (\eta) (1 - \eta) \int_ {\Theta} \beta (\theta) C _ {\theta} (\mu , \theta) d F (\theta)
$$

However, by doing so, the expected informational rent of the IS manager is also increased by:

$$
G (\eta) \int_ {\Theta} \frac {\partial H ^ {+} (\lambda , \mu , \theta , \eta)}{\partial \eta} d F (\theta) = G (\eta) \int_ {\Theta} \beta (\theta) C _ {\theta} (\mu , \theta) d F (\theta).
$$

Thus, at optimum, these two effects must be balanced. Furthermore. since $\begin{array} { r } { \int _ { \Theta } \beta ( \theta ) C _ { \vartheta } ( \mu , \theta ) d F ( \theta ) > 0 , } \end{array}$ (B.8) is equivalent to $0 = G ( \eta ) - ( 1 - \eta ) g ( \eta ) | _ { \eta = \eta ^ { * } } ,$ , as required in (B.3).

Finally, we present results for the example of §4. For the assumptions of the example, it is easy to verify that $( \mathbf { B . 6 } ) \mathbf { - } ( \mathbf { B } \ 8 )$ ) yield a global optımal solution. Thus, by setting $\gamma ( \theta ) = \theta + \alpha ( \eta ^ { \ast } ) ( \theta - \underline { { { \theta } } } )$ ), the expected organizational net value then equals:

$$
\begin{array}{r l} E \left\{N V (\theta) \right\} & = \int_ {\Theta} \gamma (\theta) \lambda^ {*} (\theta) d F (\theta) \\ & = \left[ \frac {\theta}{\bar {\theta} - \underline {{\theta}}} + \frac {k ^ {2} \ln \gamma (\theta)}{(\bar {\theta} - \underline {{\theta}}) (1 + \alpha (\eta^ {*}))} - \frac {4 k \sqrt {\gamma (\theta)}}{(\bar {\theta} - \underline {{\theta}}) (1 + \alpha (\eta^ {*}))} \right] _ {\theta} ^ {\theta} \end{array}
$$

If $G ( \eta )$ is uniform and $F ( \theta )$ is uniform over [1, 2], then $E \left\{ N V ( \vartheta ) \right\}$ is approximately equal to 7.93. Compared with knowing ξ exactly, the expected organizational net value decreases about 0 6 when the central management is uncertain about ξ and the realization of ξ equals 0.5.

For the profit center, to determine the optimal incentive scheme, the central management solves

$$
\max _ {\nu \in [ 0, 1 ]} \int_ {\Theta} \left\{G (\eta) N V ^ {+} (\lambda (\theta), \mu (\theta), \theta , \eta) + [ 1 - G (\eta) ] N V ^ {-} (\lambda^ {p} (\theta), \mu^ {p} (\theta), \theta) \right\} d F (\theta),\tag{B.9}
$$

where $\lambda ^ { p } ( \theta )$ and $\mu ^ { p } ( \theta )$ are the IS department's profit maximizing solution and

$$
N V ^ {+} \left(\lambda^ {p} (\theta), \mu^ {p} (\theta), \theta , \eta\right) = V \left(\lambda^ {p} (\theta)\right) - v \lambda^ {p} (\theta) W \left(\lambda^ {p} (\theta), \mu^ {p} (\theta)\right) - C \left(\mu^ {p} (\theta), \theta\right) - \eta \pi (\theta).
$$

$$
N V ^ {-} \left(\lambda^ {p} (\theta), \mu^ {p} (\theta), \theta\right) = V \left(\lambda^ {p} (\theta)\right) - v \lambda^ {p} (\theta) W \left(\lambda^ {p} (\theta), \mu^ {p} (\theta)\right) - C \left(\mu^ {p} (\theta), \theta\right) - \pi (\theta).
$$

(B.9) yields the same first-order condition with respect to η as in the cost center case

$$
0 \equiv g (\eta) (1 - \eta) - G (\eta) | _ {\eta = \eta^ {*}}.
$$

Therefore for the profit center,

$$
E \left\{N V ^ {p} \right\} = \int_ {\Theta} \left\{k \sqrt {\lambda^ {p} (\theta)} + (1 - \alpha (\eta^ {*})) \theta \lambda^ {p} (\theta) \right\} d F (\theta).
$$

and when Gξ) is uniform, $E \{ N V ^ { p } \}$ is approxımately equal to 4.82 versus 5.12 when ξis known exactly.

## References

Antle, Rick and Gary Eppen, “Capital Rationing and Organızational Slack in Capital Budgeting," Management Scl, 31, 2, February (1985), 163–174.

- and John Fellingham, “Resource Rationıng and Organizational Slack ın a Two-Period Model," J Accounting Res, 28, 1, Spring (1990), 1–24.

Baron. David P.. “Design of Regulatory Mechanisms and Institutions," in Richard Schmalensee and Robert D. Willig, (Eds.), Handbook of Industrial Organızation, Elsevier Science Publishers, Amsterdam, The Netherlands. 1989

Baron, Davıd P. and Roger B. Myerson, “Regulatıng a Monopolist with Unknown Cost,"Econometrica, 50, 4, July (1982), 911–930

Barron, Terry, “Some New Results in Testing for Economies of Scale in Computing: 1985 and 1988 Data," Decision Support Systems, Special Issue on Information Systems and Economıcs, 8, 5 (1992), 405-429.

and Eric Wang, "IS Outsourcing Decisions with Information Asymmetry and Objective Conflicts." working paper, Simon School, University of Rochester, Rochester, NY, 1992.

Carlyle, R. E., “Getting a Grp on Costs," Datamatton, July 15 (1990), 20–23.

Cyert, R. and J. March, The Behavior Theory' of the Firm, Prentice-Hall, Englewood Cliffs, NJ, 1963.

Dasgupta, P. S., P. J. Hammond, and E S. Maskin, "The Implementation of Social Choice Rules: Some Results o7 Incentive Compatibılity," Review of Economic Studies. 46 (1979), 185-216.

Dewan, Sanjeev and Haim Mendelson, “User Delay Costs and Internal Pricing for a Service Facılity," Management Sct, 36, 12, December (1990), 1502-1517.

Fudenberg, Drew and Jean Tirole, Game Theory, MIT Press, Cambrıdge, MA, 1991.

Guesnerie, R. and Jean-Jacques Laffont, “A Complete Solution to a Class of Princıpal-Agent Problems with an Application to the Control of a Self-Managed Firm," J Publ Economics. 25 (1984), 329– 369.

Holmstrom, Bengt and Roger B. Myerson, “Efficient and Durable Decision Rules with Incomplete Information,"Econometrica, 51, 6 (1982), 1799–1819

Kaplan, Robert S. and Anthony A. Atkınson, Advanced Management Accountıng, 2nd ed., Prentice-Hall Inc., Englewood Cliffs, NJ, 1989

March 1995

, "Bayesian Equulibrium and Incentive Compatibılity: An Introduction," in L. Hurwicz, D. Schmeidler, and H. Sonnenschein (Eds ), Soctal Goals and Socta/ Organtzatton. Cambridge Unıversity Press, Cambrıdge, England, 1985b, 229–259

Kırby, Alison J., S. Reichelsteın, P. Sen and T.-Y Paık, “Partıcıpation, Slack, and Budget-Based Performance Evaluation," J 4ccounting Res , 29, 1, Spring (1991) 109–128

Mas-Colell, Andreu, The Theory of General Economuc Equultbrnum 1 Differenttal Approach, Cambridge Unıversity Press, Cambrıdge, Fngland, 1985

McGee, Robert W., Accounttng for Data Processtng Costs, Quorum Books, New York, 1988.

Mendelson, Haim, “Pricing Computer Services: Queueing Effects," Conmunicatons ofthe ACA1, 28, 3, March (1985), 312–321.

- , "Economies of Scale in Computing Grosch's Law Revisited," Communicatons of the 4C'M1. 30, 12 (1987), 1066–1072

- , The Economies of Information Svstems Management Prentice-Hall. Englewood Chiffs, NJ (forthcoming)

Milgrom. Paul R., "Good News and Bad News: Representation Theorems and Application," The Bell J Economtcs, 12, 2, Autumn (1982), 380–391

Mirrlees, J . “The Theory of Optımal Taxation," in Kenneth J. Arrow and Michael D Intrılligator (Eds.) Handbook of Mathematical Economı, Vol III, North-Holland, Amsterdam, The Netherlands, 1986.

Myerson, Roger B.. "Incentive Compatibilitv and the Bargaining Problem," Econometrica, 47 (1979). 61-73.

- , “Analysis of Two Bargaining Problems with Incomplete Information," In Alvin E. Roth (Ed.), Game-theorete M1odels of Bargatnıng. Cambrıdge University Press, Cambrıdge, England, 1985a, 115– 147.

, Game Theory Inalsts of C’onfltct, Harvard Business School Press, Cambridge, MA, 1991.

Simon, Herbert A, Admn/stratve Behavior, 2nd ed , Macmullan, New York, 1961

Spulber, Danıel F., Regulatton and Markets, MII Press, Cambridge, MA, 1989

Wang, Eric T. G., “Controlling Information System Departments in the Presence of Cost Information Asymmetry." working paper. Sımon School, University of Rochester Rochester, NY, 1991.

Whang, Seungjn, “Alternative Mechanısms of Allocatıng Computer Resources under Queueing Delays," Informatton Svstems Res , 1, 1, March (1990), 71–88

Williamson, Oltver E., The Econome Instttuttons of Caputaltsmn. The Free Press, New York, 1985.
