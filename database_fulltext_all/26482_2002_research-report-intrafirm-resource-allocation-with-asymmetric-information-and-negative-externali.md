---
otero_id: 26482
otero_key: "BKVX5EDK"
title: "Research Report: Intrafirm Resource Allocation with Asymmetric Information and Negative Externalities"
authors: "Raja Nadiminti; Tridas Mukhopadhyay; Charles H. Kriebel"
year: "2002"
journal: "Information Systems Research"
doi: "10.1287/isre.13.4.428.70"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/BKVX5EDK/fulltext/images/86148f1c9b13fc6c7bda6213f4b0ea063c06b7e528400cc74a3fdd756bbed0c2.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Report: Intrafirm Resource Allocation with Asymmetric Information and Negative Externalities

Raja Nadiminti, Tridas Mukhopadhyay, Charles H. Kriebel,

## To cite this article:

Raja Nadiminti, Tridas Mukhopadhyay, Charles H. Kriebel, (2002) Research Report: Intrafirm Resource Allocation with Asymmetric Information and Negative Externalities. Information Systems Research 13(4):428-434. http://dx.doi.org/10.1287/ isre.13.4.428.70

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2002 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/BKVX5EDK/fulltext/images/9e6aabe2d63425e0af5b1f31ec33c672bd19a2517c2567cfdf809f99cc6054c5.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Report: Intrafirm Resource Allocation with Asymmetric Information and Negative Externalities

Raja Nadiminti • Tridas Mukhopadhyay • Charles H. Kriebel Graduate School of Industrial Administration, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213-3890 tridas@andrew.cmu.edu • ck04@andrew.cmu.edu

W <sup>e</sup> <sup>examine</sup> <sup>the</sup> <sup>intrafirm</sup> <sup>resource</sup> <sup>allocation</sup> <sup>problem</sup> <sup>with</sup> <sup>the</sup> <sup>following</sup> <sup>characteristics.</sup> The resource exhibits negative externalities, and the benefit of using the resource is known only to the user department and not to top management or other user departments. In addition, the consumption of the resource depends upon the choice of the mechanism for allocating the resource. For this problem, we derive a two-stage mechanism, and show that this proposed mechanism leads to optimal allocation.

(Resource Allocation; Asymmetric Information; Negative Externalities)

## 1. Introduction

Our goal is to analyze various schemes for the intrafirm allocation of resources with negative externalities, and then to develop an efficient mechanism for this allocation problem. This study is important for several reasons. From a practical point of view, a wide range of organizational resources exhibits negative externalities. Service departments with large waiting lines, congestion-prone electronic networks, machinery with output quality linked to production quantity are all examples of such resources. In addition, some intuitive and well-established results, such as marginal cost pricing for optimal allocation of resources, do not hold for resources exhibiting negative externalities. Also, this problem involves a conflict between the objectives of individual departments and the objectives of the organization. This conflict arises due to the externality cost created by the consumption of the resource, and the contribution of the resource to the departmental output that is known to the user, but not to the top management. Top management can observe only the departmental output and the amount of the resource consumed. If department managers have some private information about the use of this resource, they may not truthfully reveal that information.

We note the following characteristics of our resource allocation problem. This problem involves asymmetric information. The benefit function for using the resource is known only to the user department, not to top management or other users. Also, it has often been assumed in earlier work that user benefit functions are common knowledge. This could be true in an environment where the user benefit functions remain stable. Based on previous experience, top management may know the user types and the associated benefit functions, but may not know the benefit function of a specific user. However, in a changing environment, such as in computer services, where the user benefit functions change with time due to learning, user types may not be common knowledge. Another characteristic of the problem is that the user’s consumption quantity depends on the allocation mechanism and is not exogenous. If there were a price for the resource, users would consume certain quantities, and if the resource were free, the consumption quantity would be different. Including these features allows this paper to present new results on resource allocation with negative externalities.

We briefly compare our work with past research. Mendelson (1985) considered the benefit function of the organization as a whole but did not consider the benefit functions of individual users or the issue of asymmetric information. He showed that a free access policy leads to more than desirable congestion and derived the price for the resource that leads to an optimal allocation. Dewan and Mendelson (1990) extended the original analysis by considering a more general cost function. However, they also modeled the benefit function of the organization as a whole. Whang (1990) showed that Mendelson’s (1985) pricing mechanism is optimal for a large economy where each user has an infinitesimal consumption relative to the system as a whole. Giridharan and Mendelson (1994) derived an optimal pricing scheme for internal networks exhibiting both positive and negative externalities, but did not consider asymmetric information in their scheme.

A few researchers incorporated asymmetric information in their models. Dolan (1978) analyzed the issue of pricing resources in the presence of asymmetric information and congestion costs, and Whang (1989) showed that cost allocation leads to a Pareto-optimal allocation in the presence of asymmetric information and negative externalities. However, in both of these models, the consumption of individual users is exogenously given. The consumption decision in our model is endogenous. Mendelson and Whang (1990) considered the pricing of resources with negative externalities for the M/M/1 queue. In their model, the job classes and their values are common knowledge; however, individual job characteristics are known only to the user.

We develop the proposed mechanism in a step-bystep manner. We begin by determining the first-best allocation with symmetric information. Then, we derive the optimal allocation for the case where top management knows the user benefit functions. We use the results of this case to develop the two-stage mechanism for the more realistic case where top management does not know the user benefit functions.

The organization of this paper is as follows. In $\ S 2 ,$ we describe our model and determine the optimal allocation with symmetric information. We also examine two common policies for the resource allocation.

## 2. Background

In this section, we describe the resource allocation problem and derive the conditions for optimal allocation with symmetric information. We also examine two common policies for the resource allocation.

## 2.1. The Resource Allocation Problem

A firm owns a service center (e.g., a computer system) that caters to n users (e.g., departments). We examine a discrete economy with a finite number of users. We assume that the users need a firm-specific unique service, not available outside. In other words, users’ participation is a given condition. The value or gross payoff (e.g., profit contribution to the firm) derived by department i from using the resource at a rate $q _ { i }$ is given by $v _ { i } ( q _ { i } ) . \ v _ { i } ( . )$ is a continuous, nondecreasing, twice differentiable concave function of the following type: $v _ { i } ^ { \prime } ( q _ { i } )  0 \mathrm { \ a s \ q _ { i }  \infty . }$ A constant variable cost is accrued by using the resource and is normalized at zero and incorporated in $v _ { i } ( q _ { i } )$ . Note that top management can observe only the output of the department, and as a result, cannot infer anything about the benefit function of the department. So the benefit function is known only to the department consuming the resource, not to either top management or other departments.

Consuming the resource at the rate $q _ { i }$ imposes an externality cost of q C(Q) to user i, where $Q = \Sigma q _ { i } .$ , and C(.) is a continuous, monotonically increasing, twice differentiable convex function representing the externality cost. Each user contributes to the externality cost experienced by all users. Thus, the externality cost for any user depends on its own, as well as the overall consumption. This cost can arise from considerations such as waiting time, service interruptions, degradation in the resource quality consumed, etc. Davis and Whinston (1962) categorize externalities as separable and nonseparable. As they point out, the case of a nonseparable externality is considerably more complex. We have chosen the nonseparable form of externality because it is appropriate for situations where the externality cost to any user depends on the total system usage. The externality cost function C(.) is assumed to be known to all users and the resource allocator. It is reasonable to make this assumption because both the users and the planner would know how the waiting time is linked to the overall consumption. Our treatment of the externality cost is consistent with prior work in this area, such as Mendelson (1985) and Whang (1990).

To mitigate the effect of the negative externality, top management may charge user i a price of $f ( q _ { i } , Q )$ for a consumption of $q _ { i }$ when the overall consumption is $Q .$ Thus, the net payoff for user i of consuming the resource at the rate $q _ { i }$ is

$$
B _ {i} = v _ {i} (q _ {i}) - q _ {i} C (Q) - f (q _ {i}, Q).
$$

The net value of the resource to the organization is defined as the total of the net payoffs of the n users plus the total price collected from the users. Whang (1990) examined three mechanisms (the private bargaining approach, the Clark-Groves tax mechanism and a Nash equilibrium-based mechanism) for a similar scenario; he also discussed the similarity between the three mechanisms and their limitations. We study various other mechanisms, each with a different set of rules. However, there are some common aspects that are summarized below.

The players in each game are the n-user departments and the planner or top management. Top management wants to maximize the net value to the organization and this objective is common knowledge. Each user i has private information about his benefit function, and it is common knowledge that the benefit function is concave. But a user may not truthfully reveal his benefit function; he may exploit his private information to obtain a higher allocation of the resource. Because each user consuming the resource has no disutility for the externality cost faced by other users, he may use more resource than what is optimal for the organization. As stated before, the cost function C(.) is assumed to be known to all users and the resource allocator. Users do not collude; each user is assumed to maximize the net payoff $B _ { i }$ for his department independently.

## 2.2. Optimal Allocation with Symmetric Information

The conditions for optimal allocation with symmetric information provide a useful benchmark for our model. If top management knew the benefit functions of users, there would be no need for a pricing mechanism. The planner would use the true benefit functions to determine the optimal amount of capacity for each user. So the planner will maximize the net value

$$
\sum B _ {i} = \sum [ v _ {i} (q _ {i}) - q _ {i} C (Q) ].
$$

The planner must find the $q _ { i }$ for each user i, such that the above sum is maximized. Thus, the optimal allocation problem for the planner is

$$
\max _ {q _ {i}} \sum \left[ v _ {i} (q _ {i}) - q _ {i} C (Q) \right] \text {   s.t.   } q _ {i} \geq 0.\tag{1}
$$

Because $v _ { i } ( . )$ is concave and C(.) is convex, the above expression is concave. Hence, Kuhn-Tucker conditions give the maximum. The solution to the above problem (1) is

$$
\begin{array}{l} v _ {i} ^ {\prime} (q _ {i}) = C (Q) + Q C ^ {\prime} (Q) \text {for} q _ {i} > 0 \\ v _ {i} ^ {\prime} (q _ {i}) \leq C (Q) + Q C ^ {\prime} (Q) \text {for} q _ {i} = 0 \end{array} .\tag{2}
$$

Thus, all users who use the system must have the same marginal benefits. If the marginal benefits of different users were not equal, then transferring the resource from a user with a lower marginal benefit to a user with a higher marginal benefit would increase the net value to the organization.

As we consider different mechanisms in the following sections, we keep in mind that each user is concerned about the other users’ decisions only because they affect Q. Once Q is specified, users are no longer concerned about the other users’ decisions because each user can calculate the optimal used amount, irrespective of how that Q is achieved. Once we find the optimal consumption for each user, we check if it satisfies (2). If it does not, then the consumption levels are not optimal.

## 2.3. Analysis of Two Common Policies

We analyze two allocation policies that have been studied under more specific conditions. We show the suboptimality of these two schemes. We do not discuss how Q is made known to the users; no matter how Q is made known, the following schemes are suboptimal.

Free Access. Under this policy, each user is given as much resource as he requests; no price is charged to combat the externality cost.

Proposition 1. The allocation under a free access policy does not maximize the net value to the organization.

Proof. Under the free access policy, each user maximizes

$$
\max _ {q _ {i}} \left\lfloor v _ {i} (q _ {i}) - q _ {i} C (Q) \right\rfloor \text {   s.t.   } q _ {i} \geq 0.
$$

The solution of this problem is

$$
\begin{array}{l} v _ {i} ^ {\prime} (q _ {i}) = C (Q) + q _ {i} C ^ {\prime} (Q) \text {   for   } q _ {i} > 0 \\ v _ {i} ^ {\prime} (q _ {i}) \leq C (Q) + q _ {i} C ^ {\prime} (Q) \text {   for   } q _ {i} = 0. \end{array}
$$

Clearly, the solution of this problem is not the same as the solution of the overall optimal allocation (2). ▫

Note the implications of the free access policy. With optimality (2), all users have the same marginal benefit. Under a free access policy, the users who consume the resource at a higher rate have a higher marginal benefit. Therefore, individually rational consumption does not maximize the net value to the organization. Mendelson’s finding (1985) that free access policy is suboptimal holds in the more general setting as well.

Uniform Pricing. Mendelson (1985) derived a pricing mechanism whereby each user is charged a constant unit price of $Q C ^ { \prime } ( Q )$ . Mendelson assumed that the users are homogeneous. Whang (1990) extended this analysis to a large economy where each user has an infinitesimal consumption relative to the whole system. For our purposes, we drop these two considerations and evaluate the uniform pricing mechanism. Our results show that no uniform pricing mechanism can lead to optimal allocation when users consume the resource at different rates.

Proposition 2. No uniform pricing mechanism can lead to optimal allocation when users consume the resource at different rates.

Proof. Under the uniform pricing scheme, the individual user’s overall benefit is $[ v _ { i } ( q _ { i } ) - q _ { i } C ( Q ) - p q _ { i } ]$ where $p$ is the price charged per unit consumed. Thus, each user maximizes

$$
\max _ {q _ {i}} \left\lfloor v _ {i} (q _ {i}) - q _ {i} C (Q) - p q _ {i} \right\rfloor \text {   s.t.   } q _ {i} \geq 0.
$$

The solution to this problem is

$$
v _ {i} ^ {\prime} (q _ {i}) = C (Q) + q _ {i} C ^ {\prime} (Q) + p \text {   for   } q _ {i} > 0.
$$

If different users have different consumption rates from this condition, then it means that they have different marginal benefits at equilibrium. However, Condition (2) says that all users must have the same marginal benefit under optimality. Hence, when we observe different consumption rates by different users under the constant pricing scheme, we can conclude that it does not lead to the overall optimal allocation. ▫

A uniform pricing scheme can lead to an optimal allocation only when the users consume the resource at the same rate. For instance, when users have the same benefit functions, a uniform pricing mechanism can lead to optimal allocation. However, it is unrealistic to assume that all users have the same benefit function.

## 3. The Optimal Mechanism

We derive the optimal mechanism in two steps. First, we consider the case where top management knows the user benefit functions. We use the results of this case to develop the two-stage mechanism for the more realistic case where top management does not know the user benefit functions.

## 3.1. Known Benefit Functions

For this case, the planner knows the user benefit functions, but does not know the benefit function of a specific user. The planner may learn the user benefit function from prior experience if the value each user derives from consuming the resource remains stable over time. Because the planner knows the benefit functions, he can calculate the optimal $Q ^ { * }$ and announce that he will charge $f ( q , Q ^ { * } )$ for a consumption of $\mid q .$ The users know the function $f ( . )$ when they decide their consumption rates. Therefore, we derive the $f ( . )$ that allows the planner to achieve the optimal allocation through a pricing mechanism. The challenge for the planner is to charge a price so that the marginal benefit of each user is the same at $Q ^ { * } .$ . The solution calls for an allocation such that different users can be charged at different rates by the optimal mechanism.

Proposition 3. The planner achieves the optimal allocation by using a pricing mechanism in which the marginal price for a consumption rate of $q _ { i }$ is $( Q ^ { * } - q _ { i } ) C ^ { \prime } ( Q ^ { * } )$

Proof. With the given mechanism, an individual user’s net payoff at $Q$ is

$$
B _ {i} = v _ {i} (q _ {i}) - q _ {i} C (Q) - \int_ {o} ^ {q _ {i}} (Q - q) C ^ {\prime} (Q) d q.
$$

The net value to the organization is

$$
\begin{array}{l} = \sum \int_ {o} ^ {q _ {i}} (Q - q) C ^ {\prime} (Q) d q \\ \quad + \sum \left[ v _ {i} (q _ {i}) - q _ {i} C (Q) - \int_ {o} ^ {q _ {i}} (Q - q) C ^ {\prime} (Q) d q \right] \\ = \sum [ v _ {i} (q _ {i}) - q _ {i} C (Q) ]. \end{array}
$$

The maximization problem for the planner is

$$
\max _ {q _ {i}} \sum \left\lfloor v _ {i} (q _ {i}) - q _ {i} C (Q) \right\rfloor \text {   s.t.   } q _ {i} \geq 0.
$$

This expression is the same as in (1). Thus, the pricing mechanism maximizes the net value to the organization.

Does the pricing mechanism also maximize each individual user’s net payoff? The first-order condition for any user who participates in the system $( q _ { i } > 0 )$ is given by $\partial B _ { i } / \partial q _ { i } = 0 ;$

$$
\begin{array}{r l} \text {   thus,   } v _ {i} ^ {\prime} (q _ {i}) & = C (Q) + q _ {i} C ^ {\prime} (Q) + (Q - q _ {i}) C ^ {\prime} (Q) \\ & = Q C ^ {\prime} (Q) + C (Q). \end{array}
$$

Consequently, all users have the same marginal benefit, and this marginal benefit is the solution (2). Hence, this solution leads to the optimal allocation. ▫

## 3.2. Unknown Benefit Functions

We now analyze the case where the user benefit functions change over time and, consequently, are not known to the planner. This version of the allocation problem is complicated for two reasons: (1) because the benefit functions are not known to the planner, he cannot calculate the optimal $Q ^ { * }$ and (2) because $Q ^ { * }$ is not known, the users do not know the externality cost and, as a result, cannot make their consumption decisions. With this much uncertainty involved, how could the planner decide on a pricing mechanism? For this problem, we propose the following two-stage mechanism.

Stage 1. Because the planner does not know the overall consumption $Q ,$ he announces a pricing scheme that is a function $f ( q , Q )$ of both the individual and the overall consumption.

Stage 2. Next, the users submit a consumption level for each amount of overall consumption, i.e., user i submits a function $q _ { i } ( Q )$

We show that a unique $Q ^ { * }$ exists that leads to the optimal allocation. Thus, after collecting the $q _ { i } ( Q ) s$ from the users, the planner announces the $Q ^ { * }$ . Then, the user department finds its share of the resource directly from $Q ^ { * }$

We use the concept of perfect equilibrium and proceed backwards. First, we examine the user decision to submit $q _ { i } ( Q )$ in Lemma 1 below. Next, we consider the pricing scheme for the planner in Proposition 4.

Lemma 1. If users are charged $f ( q _ { i } , ~ Q ) ~ = ~ \int _ { o } ^ { q _ { i } } ( Q ~ -$ $q ) C ^ { \prime } ( Q ) d q$ for an individual consumption of q<sub>i</sub> with the overall consumption being $Q ,$ then each user will submit the $q ( Q )$ that satisfies the relation $v _ { i } ^ { \prime } ( q _ { i } ) = Q C ^ { \prime } ( Q ) + C ( Q )$ for all i.

Proof. With the above pricing mechanism, the benefit to each user is $v _ { i } ( q _ { i } )$ and the cost is $q _ { i } ( Q ) + f ( q _ { i } , Q )$ At optimality, marginal benefit must be equal to marginal cost and, hence,

$$
v _ {i} ^ {\prime} (q _ {i}) = Q C ^ {\prime} (Q) + C (Q).
$$

Because this $q _ { i }$ is individually an optimal decision for each user, it is in the best interest of each user to submit $q ( Q )$

Alternatively, if each user i thinks that others make a net overall consumption of $Q ^ { \prime } , \mathbf { i . e . } , Q ^ { \prime } = \Sigma q ^ { \prime } { } _ { j }$ where $j \neq i ,$ then he would like to consume $q _ { i }$ such that

$$
v _ {i} ^ {\prime} (q _ {i}) = (Q ^ {\prime} + q _ {i}) C ^ {\prime} (Q ^ {\prime} + q _ {i}) + C (Q ^ {\prime} + q _ {i}).
$$

Because ${ \cal Q } ^ { \prime } + q _ { i } = Q ,$ no matter what $Q ^ { \prime }$ is, each user would like to submit a $q ( Q )$ that satisfies the relation $v _ { i } ^ { \prime } ( q _ { i } ) = Q C ^ { \prime } ( Q ) + C ( Q )$ . ▫

Proposition 4. The planner achieves optimal allocation in the following ways:

(1) He announces the pricing scheme for an individual consumption of $q _ { i }$ with the overall consumption being $Q$ : $\begin{array} { r } { f ( q _ { i } , Q ) = \int _ { o } ^ { q _ { i } } ( Q \mathrm { ~ - ~ } q ) C ^ { \prime } ( Q ) d q . } \end{array}$

(2) He asks users to submit their usage schedules $q _ { i } ( Q ) ,$ , i $= 1 , \ldots , n .$

Proof. This is apparent from Lemma 1 above and Lemma 2 below. From Lemma 1, the planner knows that the announced pricing scheme will induce the users to submit their usage schedules, $q _ { i } ( Q ) , i = 1 , . . , n .$ From Lemma 2, the planner knows that a unique $Q ^ { * }$ exists at which the net payoff of each user is maximized and $\Sigma q ^ { * } { } _ { i } = Q ^ { * }$ . In addition, this allocation is optimal because it satisfies (2). ▫

Lemma 2. For any collection of benefit functions $v _ { 1 } ( , ) , \ldots , v _ { n } ( . )$ and the convex cost function $C ( . ) ,$ there exists a unique $Q ^ { * }$ at which

$$
\begin{array}{l} v _ {i} ^ {\prime} (q _ {i} ^ {*}) = Q ^ {*} C ^ {\prime} (Q ^ {*}) \\ \qquad + C (Q ^ {*}) \text {   for   all   } i, \text {   and   } \sum q _ {i} ^ {*} = Q ^ {*}. \end{array}
$$

Proof. We first prove existence and then uniqueness.

Existence. Order the $v _ { i } ( . )$ functions such that $v _ { i } ^ { ' } ( 0 )$ is nondecreasing in i. Let $q _ { i } ^ { \prime }$ be such that $v _ { i } ^ { \prime } ( q _ { i } ^ { \prime } ) = v _ { 1 } ^ { \prime } ( 0 )$ for each i. This construction is possible because all $v _ { i } ( . )$ are concave and $v _ { i } ^ { \prime } ( q _ { i } )  0$ as $q _ { i } \to \infty .$ . Let $Q ^ { \prime } \ = \ \Sigma q _ { i } ^ { \prime }$ Then there are three possible cases.

Case $( i ) . v _ { 1 } ^ { \prime } ( 0 ) = C ( Q ^ { \prime } ) + Q ^ { \prime } C ^ { \prime } ( Q ^ { \prime } ) .$

Then $Q ^ { * } = Q ^ { \prime } ;$ we have the existence of $Q ^ { * } .$

$$
\text { Case   (ii). } v _ {1} ^ {\prime} (0) > C (Q ^ {\prime}) + Q ^ {\prime} C ^ {\prime} (Q ^ {\prime}).
$$

Then we can always find a $\Delta _ { i }$ for every i such that $Q _ { \Delta } ^ { \prime }$ $= \Sigma ( q _ { i } ^ { \prime } + \Delta _ { i } )$ and

$$
v _ {1} ^ {\prime} (\Delta_ {1}) = C (Q _ {\Delta} ^ {\prime}) + Q _ {\Delta} ^ {\prime} C ^ {\prime} (Q _ {\Delta} ^ {\prime}) = v _ {i} ^ {\prime} (q _ {i} ^ {\prime} + \Delta_ {1}).
$$

This is possible because the $v _ { i } ( . ) s$ are concave and C(.) is convex. Then $Q ^ { * } = Q _ { \Delta } ^ { \prime } ;$ we have the existence of $Q ^ { * } .$

Case (iii). $v _ { 1 } ^ { \prime } ( 0 ) < C ( Q ^ { \prime } ) + Q ^ { \prime } C ^ { \prime } ( Q ^ { \prime } ) .$ Select the smallest $v _ { j } ( 0 )$ for which $v _ { j } ^ { \prime } ~ \geq ~ C ( Q ^ { \prime \prime } ) ~ + ~$ $Q ^ { \prime \prime } C ^ { \prime } ( Q ^ { \prime \prime } )$ , where $Q ^ { \prime \prime } = \Sigma q _ { i } ^ { \prime \prime }$ summed over all $i > j$ and $v _ { i } ( q _ { i } ^ { \prime \prime } ) = v _ { j } ^ { \prime } ( 0 )$

We are assured of finding such $\textsf { a } j$ because $v _ { i } ^ { \prime } ( q ) > 0$ at $q = 0$ for all i and $C ( Q ) = 0 { \mathrm { ~ a t ~ } } Q = 0$ . Note that for $i < j , q _ { i } ^ { \prime \prime } = 0$ . That is, some users are not allowed to use the service center. Once we find such $\mathsf { a } \mathsf { j } ,$ we apply the reasoning in Case (1) or Case (2) and the existence is proved.

Uniqueness. We prove this by contradiction. Let there be another Q that satisfies the desired condition. Let the two Qs be $Q ^ { * }$ and $Q ^ { * * } ,$ , with $Q ^ { * * } > Q ^ { * } ,$ . Then, because C(.) is a monotonically increasing convex function,

$$
Q ^ {* *} C ^ {\prime} (Q ^ {* *}) + C (Q ^ {* *}) > Q ^ {*} C ^ {\prime} (Q ^ {*}) + C (Q ^ {*}).
$$

Because $v _ { i } ^ { \prime } ( Q _ { i } ) = Q C ^ { \prime } ( Q ) + C ( Q ) \mathrm { f o r ~ a l l } i \mathrm { a t } Q = Q ^ { * }$ and $Q ^ { * * } .$

$$
v _ {i} ^ {\prime} (q _ {i} ^ {* *}) > v ^ {\prime} (q _ {i} ^ {*}) \text {   for   all   } i.
$$

But if $Q ^ { * * } > Q ^ { * } ,$ there must be at least one $q _ { i } ^ { * * } > q _ { i } ^ { * } ,$ and because $v _ { i } ( . )$ is concave, it implies that a $v _ { i } ^ { \prime } ( q _ { i } ^ { * * } ) <$ $v _ { i } ^ { \prime } ( q _ { i } ^ { * } )$ . That contradicts (a) and, hence, we cannot have two Qs satisfying the desired condition. ▫

Note that the planner knows more than what is strictly required of him in Lemma 2. Lemma 2 requires that the value functions $v _ { 1 } ( . ) , \ldots , v _ { n } ( . )$ be concave and the externality cost be $C ( Q )$ convex. In our case, the planner also has the additional knowledge of the actual C(Q).

We now restate the mechanism. The planner announces the pricing scheme, and each user then submits q as a function of Q. Finally, the planner selects Q\*. Note the significant features of this mechanism. First, the above mechanism results in dominant strategy equilibrium. Second, it requires little processing on the part of the users as well as the planner because each user need not know the beliefs or the preferences of other users. The only information that the planner must know is the function C(.). Third, there is no attempt on the part of the planner to know v(.) for any user. Thus, the idea is not to make the asymmetric information symmetric. The planner extracts just enough information to implement the mechanism.

## 4. Conclusion

The two significant results of this paper are: (1) for a certain class of problem, there is a way to achieve the first-best allocation under asymmetric information, even if the planner does not know the user benefit functions and (2) for resource allocation with negative externalities, a volume discounted pricing mechanism leads to optimal allocation. These results apply to any firm-specific unique resource such that users’ participation is a given condition.

In the proposed mechanism, the only information that the planner needs to know is the relationship between the load on the service center and the externality cost. It appears reasonable to assume that this relationship would be known from previous experience.

In our model, the information available to the planner and the users is asymmetric. When the information is symmetric, there is no need for a pricing mechanism because the planner can allocate the optimal amount of capacity to each user. But this will not increase the net value over our mechanism because the two-stage mechanism leads to the maximum possible net value.

Our model does not consider that users may want more resource to reduce their efforts. Future work should consider effort averse users (Harris, Kriebel, and Raviv 1982). For a given capacity, we have shown how the optimal resource allocation can be attained. An extension of our model may examine the capacity decision of the planner (Mendleson 1985, Whang 1989). Another interesting line of future research concerns the solution to the optimal replacement problem (e.g., Kriebel and Mikhail 1975, Kriebel et al. 1977).

## Acknowledgments

This research was supported in part by the National Science Foundation under Grant No. IRI-9012740. The authors thank Professor Konduru Sivaramakrishnan for his helpful comments.

## References

Davis, A. O. and A. B. Whinston. 1962. Externalities, welfare, and the theory of games. J. Political Econom. 70(2) 241–262.

Dewan, S., H. Mendelson. 1990. User delay costs and internal pricing for a service facility. Management Sci. 36(12) 1502–1517.

Dolan, R. J. 1978. Incentive mechanisms for priority queuing problems. Bell J. Econom. 9(2) 421–436.

Giridharan, P. S., H. Mendelson. 1994. Free-access policy for internal networks. Inform. Systems Res. 5(1) 1–22.

Harris, M., C. H. Kriebel, A. Raviv. 1982. Asymmetric information incentives and intrafirm resource allocation. Management Sci. 28(6) 604–620.

Kriebel, C. H., O. Mikhail. 1975. Dynamic pricing of resources in computer networks. M. A. Geisler, ed. Logistics TIMS Studies in the Management Sci. North Holland, 105–121.

——, A. A. Atkinson, H. W. H. Zia. 1977. Optimal investment, pricing and replacement of computer resources. Naval Res. Logist. Quart. 4 537–547.

Mendelson, H. 1985. Pricing computer services: Queuing effects. Comm. ACM. 28(3) 312–321.

——, S. Whang. 1990. Optimal incentive-compatible priority pricing for the M/M/1 queue. Oper. Res. 38(5) 870–883.

Whang, S. 1989. Cost allocation revisited: An optimality result. Management Sci. 35(10) 1264–1273.

——. 1990. Alternative mechanisms of allocating computer resources under queuing delays. Inform. Systems Res. 1(1) 71–88.

Seungjin Whang, Associate Editor. This paper was received on February 1, 1995, and was with the authors 52 months for revision.
