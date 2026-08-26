---
otero_id: 26741
otero_key: "GZJAEZRA"
title: "Pricing Computer Services Under Alternative Control Structures: Tradeoffs and Trends"
authors: "Sanjeev Dewan"
year: "1996"
journal: "Information Systems Research"
doi: "10.1287/isre.7.3.301"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR Information Systems Research

![](/api/attachments/GZJAEZRA/fulltext/images/87f66e4bb1bba7e4eea784f60d16cc5ec56b2307743b1b5dcc60fbb254fa378c.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Pricing Computer Services Under Alternative Control Structures: Tradeoffs and Trends

Sanjeev Dewan,

To cite this article:

Sanjeev Dewan, (1996) Pricing Computer Services Under Alternative Control Structures: Tradeoffs and Trends. Information Systems Research 7(3):301-307. http://dx.doi.org/10.1287/isre.7.3.301

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1996 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/GZJAEZRA/fulltext/images/99ffb3e7ee097cf599b6b4c9c597ddc4a13f7c7b14e72515dd5e0a702e52cc90.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Pricing Computer Services Under Alternative Control Structures: Tradeoffs and Trends

Sanjeev Dewan

School of Business Administration, George Mason University, Fairfax, Virginia 22030 and Graduate School of Management, University of California, Irvine California 92697 sdewan@uci.edu

This paper extends the analysis of the long-run pricing and capacity decision problem for shared computer services by Dewan and Mendelson (1990) and makes two further contributions. First, we show that simple marginal capacity cost pricing is often optimal in the absence of private user information, and it outperforms cost recovery and profit center pricing methods. Second, we provide insights into the implications of declining computing costs on the tradeoff between capacity costs and user time. In equilibrium, expected user delay costs are bounded by capacity costs due to the substitution of cheaper information processing capacity for valuable user time.

(Pricing; Computer Services; Marginal Cost)

## 1. Introduction

IS resource managers often use internal pricing for the allocation of shared computer services (see McGee 1988) such as mainframe, client/server systems, and local area network resources. Alternative pricing schemes range from marginal cost pricing to cost recovery pricing and budget-based pricing to profit center pricing. These schemes can be centralized, as in the case of cost recovery pricing, or decentralized in the form of profit center pricing. The specific control structure used depends on the financial responsibility assigned to the IS resource manager by the top management of the firm. This paper compares alternative control structures in terms of price and capacity levels, and net value. It also examines the implications of declining computing costs on the tradeoff between capacity cost and user time.

We formulate the long-run pricing and capacity problem under an arbitrary control structure, which specifies the price function that will be used to allocate the available capacity. For example, under cost recovery pricing a control structure constraint ensures that the price must be equal to the average cost (so that the budget is balanced). Dewan and Mendelson (1990) show that for the M/M/1 queue and linear capacity cost function, the optimal price is equal to the (constant) marginal capacity cost. Under the same modeling choices, our analysis here shows that cost recovery pricing charges the marginal capacity cost plus the average delay cost per job. Thus, users incur their delay cost twice: once as a self-incurred opportunity cost and then again as part of the service charge. The higher price translates into lower capacity and lower arrival rate, relative to optimal. The price structure of the profit center, in equilibrium, adds the average reported profit on top of the average cost recovery price, further exacerbating the problem of under-investment and underutilization of service capacity. We numerically analyze the robustness of these results under a variety of service time distributions.

We also examine the impact of the prevailing cost trends on internal pricing and the tradeoff between computing capacity and user time. As computing capacity costs decline at a faster rate relative to the cost of user time, the IS resource manager has the opportunity to increase net-value by substituting computer capacity for user time. Our results suggest that due to this substitution, in equilibrium, capacity costs would be less than total user costs, contrary to some predictions (see e.g. Thadhani 1981).

It is important to clarify that the analysis in this paper focuses on the role of the price system in allocating service capacity, rather than on its role of eliciting private user information. Accordingly, we assume that there is no information asymmetry between the resource manager and users with respect to either demand or costs. Thus, this research is related to Mendelson (1985), Banker, Datar and Kekre (1988), Balachandran and Srinidhi (1987, 1990), Dewan and Mendelson (1990) and Westland (1992). Our results can serve as a useful starting point for further positive research on why certain types of firms adopt specific control structures (see e.g. Whang 1989). Our analysis can be readily extended to the case of multiple user classes, as in Balachandran and Schaefer (1980) and Mendelson and Whang (1990).

## 2. Alternative Price Structures

We adopt the basic analytical framework of Mendelson (1985) and Dewan and Mendelson (1990), modeling the computing facility as a queueing system. We interpret the arrival rate $\lambda$ to the queueing system as the quantity of services demanded per unit time, and the service rate $\mu$ as the total service capacity. Our analysis assumes the M/G/1 queue, though some of the analytical results are derived for the important special case of the M/M/1 queue.

The (gross) value from computing services to the organization per unit time is represented by the value function $V(\lambda)$ , which we assume is increasing, twice continuously differentiable and strictly concave. Capacity costs are specified by the function $C(\mu)$ , which we assume to be linear: $C(\mu) = b\mu$ . This assumption is supported by empirical evidence on computing capacity costs (Mendelson 1985), which suggest constant returns to scale. For delay costs, we adopt the linear delay cost structure of Dewan and Mendelson (1990); i.e., a service delay of time $\tau$ is associated with a delay cost $v\tau$ . Then, the expected delay cost per service request is $G(\lambda, \mu) = vW$ , where W is the expected waiting time in the queueing system. The aggregate delay cost per unit time is $H = \lambda vW$ .

Scale and allocation decisions are represented in our model by the choice of $\mu$ and $\lambda$ , respectively. While the system manager directly chooses the capacity $\mu$ , the arrival rate $\lambda$ is determined by the aggregate usage decisions of individual users. The system manager can influence these usage decisions, however, through his choice of price function $P(\lambda, \mu)$ , which in turn is driven by the underlying control structure. In the absence of pricing, Mendelson (1985) and Balachandran and Srinidhi (1987) have shown that the system is overcongested. Assuming that internal pricing is used to allocate computing resources, scale and capacity decisions under price function $P(\lambda, \mu)$ may be formulated as:

$$
\max _ {(\lambda , \mu) 0 \leq \lambda <   \mu} f (\lambda , \mu) = V (\lambda) - \lambda G (\lambda , \mu) - b \mu ,\tag{2.1}
$$

$$
\text { subject   to: } \quad V ^ {\prime} (\lambda) - G (\lambda , \mu) = P (\lambda , \mu).\tag{2.2}
$$

Equation (2.2) is the control structure constraint, which specifies the price function that must be used to allocate capacity. This equation also represents the demand relationship: the value of the marginal service request, $V'(\lambda)$ , is equal to the total user cost $G(\lambda, \mu) + P(\lambda, \mu)$ . Next, we specify the price function under alternative control structures:

(i) Net-Value Maximization. This case serves as the theoretical benchmark, and corresponds to the unconstrained problem of Eq. (2.1). Alternatively, this case is equivalent to the constrained problem with price function equal to the externality component of the marginal delay cost: $P(\lambda, \mu) = \lambda G_{\lambda}$ .¹ This follows from the optimality of charging the opportunity cost of meeting the service request (Dewan and Mendelson 1990). Denote the net-value maximizing solution by $(\lambda^{*}, \mu^{*})$ .

(ii) Marginal Capacity Cost Pricing. Here, the price charged is equal to the marginal capacity cost: $P(\lambda, \mu) \equiv b$ . Let $(\lambda^{b}, \mu^{b})$ represent the solution under marginal capacity cost pricing.

(iii) Cost Recovery Pricing. Under cost recovery pricing the objective is to recover the entire cost of capacity through user pricing. In effect, the full cost of capacity, used and idle, is charged to the users. Accordingly, $P(\lambda, \mu) = b\mu/\lambda$ , in order to balance the budget. Let $(\lambda^{a}, \mu^{a})$ denote the solution under cost recovery pricing. It is worth pointing out that other “budget-based” schemes, that do not necessarily balance the budget, can also be easily accommodated by setting $P(\lambda, \mu) = (b\mu + \pi)/\lambda$ , where $\pi$ is the budgeted tax or subsidy for the IS facility.

(iv) Profit Center Pricing. The decision problem of the IS manager under profit center pricing is to find $(\lambda^{m}, \mu^{m})$ that maximizes profit, given by $\lambda[V'(\lambda) - G(\lambda, \mu)] - b\mu$ . To cast profit center pricing into the common constrained optimization framework, we can set $P(\lambda, \mu) = (b\mu + \Pi^{m})/\lambda$ , where $\Pi^{m}$ is the maximal profit level corresponding to $(\lambda^{m}, \mu^{m})$ .

Associating the Lagrange multiplier $\delta$ with the constraint (2.2), the Lagrangian is given by

$$
L (\lambda , \mu , \delta) = f (\lambda , \mu) + \delta [ V ^ {\prime} (\lambda) - G - P (\lambda , \mu) ].
$$

Then, the first-order necessary conditions for an interior solution to the constrained optimization problem are:

$$
V ^ {\prime} (\lambda) = G + \lambda \frac {\partial G}{\partial \lambda} + b \left(\frac {\partial G}{\partial \lambda} + \frac {\partial P}{\partial \lambda} - V ^ {\prime \prime} (\lambda)\right),\tag{2.3}
$$

$$
b = - \lambda \frac {\partial G}{\partial \mu} - \delta \left(\frac {\partial G}{\partial \mu} + \frac {\partial P}{\partial \mu}\right),\tag{2.4}
$$

$$
V ^ {\prime} (\lambda) - G (\lambda , \mu) = P (\lambda , \mu).\tag{2.5}
$$

In Eqs. (2.3)-(2.4), the terms involving the Lagrange multiplier $\delta$ represent the distortion in the scale and allocation decisions due to the control structure constraint. The decisions deviate from the optimal, whenever the Lagrange multiplier is nonzero. The following theorem sheds light on alternative price structures.

THEOREM 1. For the M/M/1 queue: $^{2}$

$$
\begin{array}{r l} & {\mathrm{(i)} p ^ {*} = b,} \\ & {\mathrm{(ii)} p ^ {a} = b + G (\lambda^ {a}, \mu^ {a}),} \\ & {\mathrm{(iii)} p ^ {m} = b + G (\lambda^ {m}, \mu^ {m}) + \Pi^ {m} / \lambda^ {m}.} \end{array}
$$

PROOF. The first-order optimality conditions for the case of net-value maximization are given by Eqs. (2.3)-(2.4), setting $\delta = 0$ . Subtracting Eq. (2.4) from (2.3), we have $V'(\lambda) - G = p^{*} = b + \lambda (G_{\lambda} + G_{\mu})$ . The Pollaczek-Khinchin formula (Kleinrock 1975) for the waiting time in an $M / G / 1$ queue is given by

$$
W = \frac {1}{\mu} + \frac {\lambda (1 + c ^ {2})}{2 \mu (\mu - \lambda)},\tag{2.6}
$$

where $c$ is the coefficient of variation of the service time distribution. It follows from Eq. (2.6) that $G_{\lambda} + G_{\mu} = v(c^2 - 1) / (2\mu^2)$ . Thus, the optimal price is given by

$$
p ^ {*} = b + (c ^ {2} - 1) \cdot \frac {v \lambda}{2 \mu^ {2}}.\tag{2.7}
$$

Then, (i) follows from the fact that $c = 1$ for the $M / M / 1$ queue. For (ii) and (iii), let the price function be $P(\lambda, \mu) = (b\mu + \pi) / \lambda$ , where $\pi = 0$ in case (ii) and $\pi = \Pi^m$ in case (iii). For the $M / M / 1$ queue ( $c = 1$ ), it follows from Eq. (2.6) that $G_{\lambda} + G_{\mu} = 0$ . Also, since $G$ is homogeneous of degree -1, by Euler's law, $\lambda G_{\lambda} + \mu G_{\mu} = -G$ . Further, $\lambda P_{\lambda} + \mu P_{\mu} = -\pi / \lambda$ . Substituting these relations into Eqs. (2.3)-(2.5), we can solve for the Lagrange multiplier:

$$
\delta = \frac {- \lambda G - \pi}{\lambda V ^ {\prime \prime} (\lambda) + G + \pi / \lambda}.
$$

Substituting into Eq. (2.3), we have that

$$
p ^ {a} = G + \lambda \frac {\partial G}{\partial \lambda}, \quad \text { and }\tag{2.8}
$$

$$
p ^ {m} = G + \lambda \frac {\partial G}{\partial \lambda} + \Pi^ {m} / \lambda ,\tag{2.9}
$$

evaluated at their respective equilibria. Then, (ii) and (iii) are proved by combining the above price equations with the first-order condition (2.4). □

For c = 1, it is optimal to charge the marginal capacity cost, and the pricing rule is simple and easily implemented. Users are charged the constant marginal capacity cost b, independent of utilization. Then, only the fraction $\rho$ (relative utilization) of the capacity costs are recovered through pricing, while the remaining fraction $1 - \rho$ constitutes a budget deficit. While this pricing rule may be viewed as a fixed cost allocation, it is not a full cost allocation, as only the fraction $\rho$ of capacity costs are recovered through user pricing.

To fully recover capacity costs the IS resource manager must charge price $p^{u}$ above. Then, we see from Eq. (2.8) that users are charged both the externality cost (equal to b for c = 1) and the self-inflicted delay cost G. Thus, in order to balance the budget, users pay twice for the delay cost of their service request: once implicitly as a self-incurred opportunity cost, and then explicitly as part of the service fee.

Somewhat different analytical models find that cost recovery pricing is sometimes optimal. Balachandran and Srinidhi (1990) found that allocation of fixed capacity cost is optimal in the short-run (fixed capacity) problem with a linear value function and exponential capacity cost function. Whang (1989) demonstrated the optimality of a full cost allocation in a game-theoretic model of private demand information. The full cost allocation accounting rule leads to honest reporting of demand by users and also yields an efficient allocation of capacity. Interestingly, in Whang (1989), while the pricing formula is consistent with a full cost allocation, the actual value of the price charged is equal to marginal cost.

Under profit center pricing, Eq. (2.9) suggests that users incur the following costs: the externality cost (equal to b for c = 1); twice their own delay cost, as in cost recovery pricing; and, on top of all that, the average profit $\Pi^{m}/\lambda^{m}$ . The following theorem examines the impact of alternative control structures on the arrival rate and capacity.

THEOREM 2. For the M/M/1 queue:

(i) $\lambda^{*} = \lambda^{b} > \lambda^{a} > \lambda^{m},$

(ii) $\mu^{*} = \mu^{b} > \mu^{a} > \mu^{m}$ ,

(iii) $p^m > p^a > p^* = b$ .

PROOF. For $i = *, a, m$ the capacity is given by

$$
\mu^ {\prime} = \lambda^ {\prime} + \sqrt {\lambda^ {\prime} v / b},\tag{2.10}
$$

as shown in the proof of Theorem 1. Thus, the expected delay cost per job is

$$
G = \sqrt {b v / \lambda^ {i}}.\tag{2.11}
$$

Now, the equalities in the statement of the theorem are due to the fact that marginal cost pricing is optimal for the $M/M/1$ queue. It follows from the price structures derived in Theorem 1 and Eq. (2.10) that $V'(\lambda') = b + h'(\lambda)$ , for $i = *, a, m$ , where $h^*(\lambda) = \sqrt{bv/\lambda}$ , $h^a(\lambda) = 2h^*(\lambda)$ , and $h^m(\lambda) = h^a(\lambda) + \Pi^m/\lambda$ . Then, (i) is proved by noting that $V'(\lambda)$ is monotonically decreasing and $h^*(\lambda) < h^a(\lambda) < h^m(\lambda)$ for all $\lambda$ . (ii) follows from the fact that $\mu$ is increasing in $\lambda$ , as per Equation (2.10). Finally, (iii) follows from the price structures in Theorem 1 and the fact that the equilibrium delay cost, given by Eq. (2.11), is higher for lower values of the arrival rate.

Note that the equilibrium job delay cost is higher for lower values of equilibrium arrival rate (Eq. 2.11). Thus, the user experiences higher delay cost under cost recovery pricing, relative to marginal capacity cost pricing, while the delay cost under profit center pricing is higher still. These results are opposite from what one might expect in the short-run problem with fixed capacity. In sum, from Theorems 1 and 2, we have shown that: for the M/M/1 queue, the optimal price is equal to the marginal capacity cost; cost recovery pricing and profit center pricing charge successively higher prices which leads to successively greater under-investment and under-utilization of service capacity.

Next, we numerically analyze a class of more general service time distributions. We change the value of the coefficient of variation c, and study the impact on optimal arrival rate, capacity and price. Balachandran and Srinidhi (1987) also perform a similar analysis for the short-run problem. The range 0 < c < 1 corresponds to distributions whose variability is less than that of the exponential distribution. This includes the Erlang family of distributions, which is bounded by the deterministic $c = 0$ and the exponential $c = 1$ distributions. c > 1 corresponds to distributions that have variability higher than that of the exponential distribution. An example of this class of distributions is the hyperexponential family. Our numerical analysis assumes the isoelastic demand function, $V'(\lambda) = 2A\sqrt{\lambda}$ .

Figure 1 depicts price as a function of the squared coefficient of variation for the cases of net-value maximization $(p^{*})$ , marginal cost pricing $(p^{b})$ , cost recovery pricing $(p^{a})$ , and profit center pricing $(p^{m})$ . $c^{2}$ was varied between 0.02 and 3.00, while the other exogenous parameters were kept fixed at A = 15, v = 10, b = 1. Consistent with Theorem 1, the optimal price is lower (greater, respectively) than marginal capacity cost b for c < 1 (c > 1, respectively); $p^{*} = b$ when c = 1. The cost recovery price is higher than $p^{*}$ throughout, while the monopoly price is higher still. Note that the optimal price does not substantially deviate from the marginal capacity cost. Does the same pattern hold for net-values?

In Figure 2, we graph the net-value obtained under the various pricing schemes of Figure 1. Note that the curve for $NV^{b}$ , the net-value under marginal capacity cost pricing, is virtually indistinguishable from the corresponding curve for net-value maximization, $NV^{*}$ . Also note that $NV^{b} > NV^{a} > NV^{m}$ throughout. The net-value loss due to cost recovery pricing ranges between 6 and 12 percent, while the net-value loss under profit center pricing is much higher, ranging between 37 and 50 percent. Marginal capacity cost pricing is simple and roughly optimal.

Figure 1 Price as a Function of the Squared Coefficient of Variation $c^2$ , Under Alternative Price Structures  
![](/api/attachments/GZJAEZRA/fulltext/images/244e75bcbcf4c97986d3546c8065344efd75667e2285dd903a6764e6a10eb2ae.jpg)

Figure 3 depicts arrival rate and service capacity as a function of $c^{2}$ . The ratio of arrival rate to capacity represents the relative utilization of capacity. Note that arrival rate, capacity, as well as utilization are decreasing in the coefficient of variation c. At higher values of c, the expected user delay cost is higher, which tends to depress arrival rate, capacity and utilization. These results concur with similar findings of Balachandran and Srinidhi (1987). Again, the solution under marginal capacity cost pricing is not very different from optimal. The cost recovery price being higher than optimal throughout, leads to lower capacity and arrival rate. The problem of under-investment and under-utilization is further exacerbated under profit center pricing.

Thus, in the case of no private user information, marginal capacity cost pricing is optimal for the M/M/1 queue, and uniformly superior to other pricing methods under more general conditions. In the following section, we consider the effect of declining computing costs on marginal cost pricing over time.

Net-value as a Function of the Squared Coefficient of Variation $c^{2}$ , Under Alternative Price Structures. The Graphs Corresponding to Net-value Maximization and Marginal Cost Pricing, Respectively, Are Virtually Indistinguishable from Each Other  
![](/api/attachments/GZJAEZRA/fulltext/images/11695b7deeaddf21ca92296933a400092a1cb7e59023c323b0d8c6c2b91f6387.jpg)

## 3. Implications of Cost Trends

The prevailing cost trends are such that the unit computing capacity cost is declining at a relatively faster rate than the unit cost of users' time. In particular, the average cost of computing capacity is declining by roughly 20% per year, while the unit cost of user time (reflected, for example, in the average programmer wage rate) has remained constant in real terms (Gurbaxani and Mendelson 1992). It has been predicted (by Doherty and Kelisky 1979 and Thadhani 1981, among others) that the aggregate costs at a computing facility would follow the same pattern as the trends in unit costs: user-related costs would increase over time, constituting an increasingly larger proportion of the total costs of an IS facility.

Figure 3 Arrival Rate and Capacity as a Function of the Squared Coefficient of Variation $c^2$ , Under the Various Price Structures  
![](/api/attachments/GZJAEZRA/fulltext/images/42012d093a0eada2995845845ebe658ffb8dc1457f4c0c0cd3596c00def159a5.jpg)

Gurbaxani and Mendelson's (1992) empirical analysis of data-processing spending data reject related conjectures of increasing software budget shares, finding that the proportions of software and hardware remain roughly constant over time. They report that hardware constitutes 38% while software comprises 29% of the data processing budget. Further, hardware as a percentage of hardware and software is 57%, while software as a percentage of hardware and software is 43%. These proportions stay roughly constant over time, due to the substitution of increasingly cheaper hardware (analogous to computing capacity here) for relatively more expensive software development effort (user cost here).

One way in which hardware can be substituted for user time is by investing in “excess” capacity to improve system turnaround time. Indeed, increments to service capacity translate into more than proportionate improvements in system turnaround time, as shown in the following lemma. We define “capacity elasticity of turnaround time” $\eta$ as the percent reduction in average system turnaround time W due to a percent increase in service capacity $\mu$ :

$$
\eta = \frac {d W (\sigma \mu)}{d \sigma} \left. \frac {\sigma}{W (\mu)} \right| _ {\sigma = 1}.\tag{3.12}
$$

We then have the following result.

LEMMA 1. There are increasing returns to scale in system turnaround time.

PROOF. Substituting for W from Eq. (2.6) into the formula for elasticity in Eq. (3.12), we have

$$
\eta = \frac {2 (\mu - \lambda) ^ {2} + \lambda \mu (1 + c ^ {2})}{2 (\mu - \lambda) ^ {2} + \lambda (\mu - \lambda) (1 + c ^ {2})},
$$

where we assume that $\mu$ is a scale parameter of the service time distribution, as in Dewan and Mendelson (1990). Clearly $\eta$ is larger than 1, proving our result. ☐

For the special case of the M/M/1 queue the elasticity is given by $\eta = 1/(1 - \rho)$ , where $\rho$ is the relative capacity utilization. Thus, at 50% utilization a 10% increase in capacity enables a 20% improvement in system turnaround time. As computing costs decline, IS resource managers have the opportunity to expand computing capacity in order to keep turnaround time, and user costs, low. What are the implications of this substitution for the tradeoff between computing capacity and user time? We investigate this question next, studying the behavior of the ratio of user delay costs to capacity costs, $H_{i}^{*}/C_{i}^{*}$ . We have the following result.

THEOREM 3. For the M/M/1 queue, the cost ratio $H_{i}^{*}/C_{i}^{*}$ is less than unity for all t, and it is constant over time if, and only if, the demand function has unit elasticity.

PROOF. The first-order optimality conditions are:

$$
V ^ {\prime} (\lambda) - \sqrt {\frac {b v}{\lambda^ {*}}} - b = 0,\tag{3.13}
$$

$$
b - \frac {v \lambda^ {*}}{(\mu^ {*} - \lambda^ {*}) ^ {2}} = 0.\tag{3.14}
$$

Analyzing Eqs. (3.13)-(3.14), we obtain for the cost ratio:

$$
\frac {H ^ {*}}{C ^ {*}} = \frac {1}{1 + \sqrt {b \lambda^ {*} / v}},\tag{3.15}
$$

which is clearly less than one. For the "if" part, we substitute the unit-elasticity demand function $V'(\lambda) = A / \lambda$ into the first-order optimality conditions and solve to get

$$
\frac {H _ {i} ^ {*}}{C _ {i} ^ {*}} = \frac {2 \sqrt {v}}{\sqrt {v} + \sqrt {4 A + v}},\tag{3.16}
$$

which is clearly constant over time. For the "only if" part, note from Eq. (3.15) that $H_{i}^{*} / C_{i}^{*}$ is a constant (i.e., independent of $b$ ) if, and only if, $b\lambda^{*} = C$ , for some constant $C$ . Substituting $b = C / \lambda^{*}$ into Eq. (3.14), it follows from Eq. (3.13) that: $V'(\lambda^{*}) = (C + \sqrt{Cv}) / \lambda^{*}$ . Now, as $b$ is varied in the range $(0, \infty)$ , $\lambda^{*}$ also varies in the same range. We conclude that the demand function must have the form:

$$
V ^ {\prime} (\lambda) = \frac {C + \sqrt {C v}}{\lambda} \quad \text { for } \lambda \in (0, \infty),
$$

which clearly has unit elasticity. $\square$

According to the above theorem the aggregate cost of users' time, in equilibrium, is less than the total capacity cost. This result negates the conjectures predicting ever-increasing user costs. In sum, our analysis tends to reject the general notion that user costs would increase over time and tend to dominate capacity costs. The basic reason for the divergence between our predictions and those of Doherty and Kelisky (1979) and Thadhani (1981) is that our model endogenizes the substitution of computing capacity for interactive users' time, while the others ignored such substitution opportunities.

## 4. Concluding Remarks

The optimality of allocating resources inside the firm by pricing them at their marginal cost is a standard result (Hirshleifer 1982). This paper finds that this simple pricing concept also holds good for the allocation of shared information services in the presence of user delay costs. Using a common framework for analyzing alternative control structures, we show that the objectives of cost recovery and profit maximization lead to successively higher under-investment and under-utilization of service resources.

We derive closed-form results for alternative price structures in the case of the M/M/1 queue. In this case, marginal capacity cost pricing is optimal; cost recovery pricing charges users twice for their own delay cost, while the price is higher still under profit center pricing. Higher prices lead to under-investment and underutilization of service capacity. Numerical analysis suggests that these qualitative results are robust to the distribution of service requirements. We also examined the impact of the prevailing cost trends on marginal capacity cost pricing. Our results suggest that, in equilibrium, user delay costs will be less than computer capacity costs due to the substitution of service capacity for user time. $^{3}$

$^{1}$ The author thanks the associate editor and three anonymous referees for many helpful comments and suggestions

## References

Balachandran, K. R and M E Schaefer, "Public and Private Optimization at a Service Facility With Approximate Information on Congestion," European J Oper Res., 4 (1980), 195–202

—— and B. N. Srinidhu, "A Rationale for Fixed Charge Application," J Accounting, Auditing and Finance, Spring (1987), 151–169

— and —, "A Note on Cost Allocation, Opportunity Costs and Optimal Utilization," J. Business Finance and Accounting, 17, 4 (Autumn 1990), 579–584

Dewan, S and H Mendelson, "User Delay Costs and Internal Pricing for a Service Facility," Management Sci, 36, 12 (1990), 1502–1517.

Doherty, W J and R P. Kelisky, "Managing VM/CMS Systems For User Effectiveness," IBM Systems J, 18, 1 (1979), 143–163

Gurbaxani, V and H Mendelson, "An Empirical Analysis of Software and Hardware Spending," Decision Support Systems, 8 (1992), 1–16

Kleinrock, L., Queuing Systems, Vol I, Wiley, New York, 1975.

McGee, R W., Accounting for Data Processing Costs, Quorum Books, New York. 1988

Mendelson, H., "Pricing Computer Services: Queueing Effects," Comm. ACM, 28, 3 (1985), 312–321

— and S. Whang, "Optimal Incentive-Compatible Priority Pricing for the M/M/1 Queue," Oper Res., 38, 5 (1990), 870–883

Thadhani, A J, "Interactive User Productivity," IBM Systems J, 20, 4 (1981), 407-423

Whang, S., "Cost Allocation Revisited An Optimality Result," Management Sci., 35, 10 (October 1989), 1264–1273
