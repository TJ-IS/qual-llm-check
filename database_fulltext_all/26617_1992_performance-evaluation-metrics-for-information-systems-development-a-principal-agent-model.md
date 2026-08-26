---
otero_id: 26617
otero_key: "E755SFGS"
title: "Performance Evaluation Metrics for Information Systems Development: A Principal-Agent Model"
authors: "Rajiv D. Banker; Chris F. Kemerer"
year: "1992"
journal: "Information Systems Research"
doi: "10.1287/isre.3.4.379"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/E755SFGS/fulltext/images/1b0780a3e894bd2a2016961ca533d297203bf80b72500747fa3e25ef88c47096.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Performance Evaluation Metrics for Information Systems Development: A Principal-Agent Model

Rajiv D. Banker, Chris F. Kemerer,

## To cite this article:

Rajiv D. Banker, Chris F. Kemerer, (1992) Performance Evaluation Metrics for Information Systems Development: A Principal Agent Model. Information Systems Research 3(4):379-400. http://dx.doi.org/10.1287/isre.3.4.379

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1992 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/E755SFGS/fulltext/images/75240dd0e1c96d767f486cf3bef8518690f37449b155b3dad04335af6c4cc2ed.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Performance Evaluation Metrics for Information Systems Development: A Principal-Agent Model

Rajiv D. Banker

Chris F. Kemerer

Carlson School of Management

Universuty of Mınnesota

Mınneapolıs, Mınnesota 55455

Sloan School of Management

Massachusetts Instutute of Technology

50 Memorial Drive, E53-315

Cambridge, Massachusetts 02142-1347

The information systems (IS) development activity in large organizations is a source of increasing cost and concern to management. IS development projects are often over-budget, late, costly to maintain, and not done to the satisfaction of the requesting user. These problems exist, in part, due to the organization of the IS development process, where information systems development is typically assigned by the user (principal) to a systems developer (agent). These two parties do not have perfectly congruent goals, and therefore a contract is developed to specify their relationship. An inability to directly monitor the agent requires the use of performance measures, or metrics, to represent the agent's actions to the principal. The use of multiple measures is necessary given the multi-dimensional nature of successful systems development. In practice such contracts are difficult to develop satisfactorily, due in part to an inability to specify appropriate metrics. This paper develops a principal-agent model that provides a set of decision criteria for the principal 1o use to develop an incentive compatible contract for the agent. These criteria include the precision and the sensitivity of the performance metric. After presenting the formal model, some current software development metrics are discussed to illustrate how the model can be used to provide a theoretical foundation and a formal vocabulary for performance metric analysis. The model is also used in a positive (descriptive) manner to explain why current practice emphasizes metrics that possess relatively high levels of sensitivity and precision. Finally, some suggestions are made for the improvement of current metrics based upon these criteria.

Software engineering—Management of computing and information systems

## 1. Introduction

nformation systems (IS) development in large organizations is a source of increas-Ling cost and concern to management.¹ IS development projects are often over budget, late, costly to maintain, and not done to the satisfaction of the requesting user.² It has been suggested that these problems exist, in part, due to the organization of the IS development process, where information systems development is typically assigned by the user (principal) to a developer (agent) (Gurbaxani and Kemerer 1989, 1990; Beath and Straub 1989; Klepper 1990; Whang 1992; Richmond et al. 1992). These two parties do not have perfectly congruent goals, and therefore a contract is developed to specify their relationship. An inability to monitor the agent directly requires the use of performance measures, or metrics, to represent the agent's actions to the principal. The use of multiple measures is necessary given the multidimensional nature of successful systems development. In practice such contracts are difficult to develop satisfactorily, due in part to an inability to specify appropriate metrics.

There is much current interest in industry in general related to performance contracting, and specific issues related to software development contracting are growing in currency with the increased awareness and interest in outsourcing of the systems development and delivery functions.3 In order for organizations to enter into such arrangements with vendors formal contracts are required, and such contracts require valid performance evaluation metrics in order for both parties to reach agreement.

The difficulties that principals have in specifying performance metrics can be illustrated easily with a few examples from current practice. It is well documented that over an information system's useful life the maintenance costs typically exceed the development cost (Swanson and Beath 1990). Yet, in practice, software developers are typically evaluated by criteria such as on-time and on-budget delivery of the initial system, and rarely, if ever, on the likely maintainability of the system that they have just delivered (Gode et al. 1990). Izzo notes that, “Maintenance, long considered one of the most important product support services a business provides, is considered a secondary responsibility in information systems" (1987, p. 25). Therefore, the question remains, since developers understand this relationship, why don't their contractual arrangements reflect it?

Another example comes from a recent study of 11 large federal government systems integration projects.⁴ The most frequent definition of success was “user satisfaction," yet the report notes that “Agencies such as the US GAO . . . ignore long-term user satisfaction and focus instead on cost and budget issues because they are easy to measure." Even interpreting this statement in a relative manner, i.e., “. . . are easier to measure," it is not obvious why this should be the case. Tracking cost and schedule data tópically requires the implementation and use of a project management system devoted to the task. Developers need to record their time spent, and such actual data must be matched against previously budgeted milestones in order to generate the appropriate management information. Therefore, “easier to measure" must refer to conceptual rather than practical concerns. What is it that makes “user satisfaction"a desirable but underused performance metric?

In order to understand these apparent paradoxes of user and developer behavior this paper develops a principal-agent model that is analyzed to identify a set of decision criteria for the principal to use to specify the contract. This model results in two criteria, the precision and the sensittvty' of the performance metric which influence the emphasis on various metrics. In particular, the model suggests that metrics that are relatively more precise and more sensitive will be preferred in the long term by both the principal and the agent in establishing the contract. These general results are then applied to two mini-case studies, one an internal IS group and one an external provider, to illustrate the application of these concepts in an IS development context.

The model provides a theoretical foundation and a formal vocabulary for performance metric evaluation in the general context of a multidimensional performance contract. The results of the model are applied to two organizations to illustrate the model's use in a positive (descriptive) manner to suggest explanations for the current relative emphasis in practice on cost and schedule. Additional discussion of the results shows how these results could be used in a normative manner to improve current rnetrics and develop new metrics that are more likely to be adopted.

This paper is organized as follows. The formal model is developed and shown in §2. Section 3 first develops a simple framework of IS development project performance metrics, and then applies the model results to two mini-case studies. Section 4 presents a broader discussion of both the ramifications and limitations of the model outside the context of the two organizations studied. Finally, some concluding remarks are presented in §5.

## 2. General Model

Information systems (IS) development is modeled as a principal-agent problem, with the client (the principal) desiring information systems to be developed to meet her goals. She contracts with an IS project manager (the agent) to perform this work, due to specialized expertise on the part of the agent. The normal principal-agent model assumptions are made; (i) the goals of the agent are only imperfectly aligned with those of the principal (goal incongruence) and (ii) the agent's actions can only be imperfectly observed by the principal (information asymmetries). The principal is assumed to be risk-neutral and the agent is assumed to be risk and effort averse. Considerable prior work exists in this area, including Ross ( 1973), Jensen and Meckling (1976), Holmstrom (1979) and Harris and Ravıv (1979). The current work builds directly on prior work by Banker and Datar (1989).

The principal is assumed to be interested in the outcome along n dimensions, which are represented by the vector $\mathbf { x } \equiv ( \mathfrak { x } _ { 1 } , \ldots , \mathfrak { x } _ { i } , \ldots , \mathfrak { x } _ { n } )$ . The agent can increase the likelihood of obtaining a better outcome $x _ { t }$ by devoting more effort $a _ { \iota }$ towards that outcome. More formally, let

$$
\partial m _ {i} / \partial a _ {i} > 0, \quad \partial m _ {i} / \partial a _ {j} = 0, \quad i, j = 1, 2, \dots , n, j \neq i
$$

where $m _ { \iota } = E ( x , | a _ { \iota } )$ is the expected value of outcome $x _ { t }$

The outcomes cannot be observed jointly by the principal and the agent with perfect accuracy. The agent's efforts $\mathbf { a } = ( a _ { 1 } , \ldots , a _ { i } , \ldots , a _ { n } )$ cannot be perfectly observed by the principal without incurring prohibitive monitoring costs. For performance evaluation purposes, therefore, appropriate metrics $\mathbf { y } \equiv ( \mathbb { y } _ { 1 } , \dots , \mathbb { y } _ { \iota } , \dots , \mathbb { y } _ { n } )$ are developed to provide (imperfect) signals about the true outcomes.

More formally, let

$$
y _ {i} = x _ {i} + \epsilon_ {i}, \quad i = 1, 2, \dots , n
$$

where $\epsilon _ { i }$ represents random variations (noise) for each of the n outcomes of interest. In order to provide incentives for the agent to exert greater effort to produce higher levels of the outcomes of interest to the principal, the principal bases the agent's compensation on the jointly observable metrics $s = s ( \mathbf { y } )$ where s represents the agent's compensation. The monetary value of the outcomes to the principal is represented by w, where w is a function of x, and therefore the risk-neutral principal seeks to maximize the expected value of $w ( \mathbf { x } ) - s ( \mathbf { y } )$ . The agent, due to his risk and effort aversion, must be compensated at the end of the contractual time period (Lambert 1983). The principal understands the agent to be economically rational, and knows that a compensation contract based on y’ will influence the agent's actions a. The agent seeks to maximize the expected value of $u ( s ) - v ( \mathbf { a } )$ where $u ( \cdot )$ represents his utility for compensation, s(·), and $v ( \cdot )$ represents his disutility for effort, with $u ^ { \prime } ( \cdot ) > 0 , u ^ { \prime \prime } ( \cdot ) < 0$ , and $v ^ { \prime } ( \cdot ) > 0$ . The principal's problem can now be formulated as follows:

$$
\max _ {s (\cdot), \mathbf {a}} E [ w (\mathbf {x}) - s (\mathbf {y}) ]\tag{1}
$$

subject to

$$
E [ u (s (\mathbf {y})) - v (\mathbf {a}) ] \geq u _ {0},\tag{2a}
$$

$$
\partial E [ u (s (\mathbf {y})) - v (\mathbf {a}) ] / \partial a _ {i} = 0 \quad \text { for } \quad i = 1, \dots , n,\tag{2b}
$$

$$
s \in [ s _ {L}, s _ {H} ], \quad \mathbf {a} \in [ \mathbf {a} _ {L}, \mathbf {a} _ {H} ].\tag{2c}
$$

The objective function simply maximizes the expected benefit $w ( \mathbf { x } )$ to the principal of the information systems outcomes x net of compensation s paid to the agent. The first constraint (“individual rationality") ensures that the contract guarantees the agent a minimum expected utility level, $u _ { \theta }$ , equaling at least his best alternative employment possibility. The next set of n constraints (“self-selection") ensures that the agent's effort level choices $a _ { \iota } , i = 1 , 2 , \ldots , n$ , maximize his own expected utility level, and thus provide incentive compatibility with the second best actions. This set of first order optimization conditions is assumed to characterize the optimal action choices for the agent (Rogerson 1985). The final constraints specify a bounded feasible space to ensure the existence of an optimal solution to the principal's constrained maximization problem (Holmstrom 1979).

This program, solved repeatedly for different values of $u _ { 0 }$ , will generate the Pareto efficient frontier of possible contracts whereby neither the principal nor the agent can be made better off without the other being made worse off. The principal seeks to design the compensation contract that will maximize her own utility. The model can be solved by setting the agent's expected utility at the level $u _ { 0 } .$ . This amount is assumed to be determined by the market for the agent's skills. Therefore, in terms of the model, improved metrics (metrics which more closely approximate the actual outcomes) in the short term only benefit the principal, since solving the model involves selecting a fixed expected utility for the agent. However, in the long term improved metrics will lead to more effective monitoring, which will lead to actions by the agent that will improve his marginal product, which will move the entire Pareto efficient frontier outward, which will result in both parties being better off, under the assumption that the market will prevent the principal from capturing all of the marginal rents resulting from such a shift. Therefore, better metrics ultimately will be preferred by both the principal and the agent.

The Euler-Lagrange optimization conditions for the mathematical program above are given by the following:

$$
\frac {1}{u ^ {\prime} (s)} - \lambda + \sum_ {i = 1} ^ {n} \mu_ {i} \frac {\int [ \partial f (\mathbf {x} , \mathbf {y} ; \mathbf {a}) / \partial a _ {i} ] d \mathbf {x}}{\int f (\mathbf {x} , \mathbf {y} ; \mathbf {a}) d \mathbf {x}},\tag{3}
$$

$$
\frac {\partial^ {2}}{\partial a _ {i} ^ {2}} E [ w (\mathbf {x}) - s (\mathbf {y}) ] + \sum_ {j = 1} ^ {n} \mu_ {j} \frac {\partial^ {2}}{\partial a _ {i} ^ {2}} E [ u (s) - v (\mathbf {a}) ] = 0
$$

for each $\iota = 1 , \ldots n .$

(4)

Here, λ and $\mu _ { t } , \iota = 1 , \dots , n$ , are Lagrange multipliers for the $( n + 1 )$ constraints. The joint probability density function of the outcomes x and the metrics y is embodied in $f ( \cdot )$ , and $\partial f ( \cdot ) / \partial a _ { \iota }$ denotes its partial derivative with respect to effort dimension $a _ { \iota }$ . The condition in (3) reflects pointwise optimization for each observable value of the metric vector y. Since the actual outcomes x are not jointly observable, the incentive contract cannot be based on it, and therefore integration is performed over all possible values of x in condition (3). Let

$$
f (\mathbf {x}, \mathbf {y}; \mathbf {a}) = g (\mathbf {x} | \mathbf {y}; \mathbf {a}) h (\mathbf {y}; \mathbf {a})\tag{5}
$$

where $g ( \cdot )$ is the probability density function of x conditional on the observed value of $\mathbf { \dot { y } } .$ , and $h ( \cdot )$ is the marginal probability density function of $\mathbf { y }$ . Now

$$
\int [ \partial f (\cdot) / \partial a _ {i} ] d \mathbf {x} = \int [ \partial g (\cdot) / \partial a _ {i} ] h (\cdot) d \mathbf {x} + \int g (\cdot) [ \partial h (\cdot) / \partial a _ {i} ] d \mathbf {x}.\tag{6}
$$

But, $\int \{ \boldsymbol { \mathbf { \mathit { x } } } \} ( \ \cdot \ ) d \mathbf { \mathbf { \mathbf { x } } } = \mathrm { ~ 1 ~ }$ because $g ( \cdot )$ is a probability density function, and therefore

$$
\int [ \partial g (\cdot) / \partial a _ {i} ] h (\cdot) d \mathbf {x} = h (\cdot) \frac {\partial}{\partial a _ {i}} \int g (\cdot) d \mathbf {x} = 0.\tag{7}
$$

It follows from (5), (6) and (7) that

$$
\frac {\int [ \partial f (\mathbf {x} , \mathbf {y} ; \mathbf {a}) / \partial a _ {i} ] d \mathbf {x}}{\int f (\mathbf {x} , \mathbf {y} ; \mathbf {a}) d \mathbf {x}} = \frac {[ \partial h (\mathbf {y} ; \mathbf {a}) / \partial a _ {i} ]}{h (\mathbf {y} ; \mathbf {a})}.\tag{8}
$$

Returning to the condition in (3)

$$
\frac {1}{u ^ {\prime} (s)} = \lambda + \sum_ {i = 1} ^ {n} \mu_ {i} \frac {[ \partial h (\mathbf {y} ; \mathbf {a}) / \partial a _ {i} ]}{h (\mathbf {y} ; \mathbf {a})}.\tag{9}
$$

Differentiating (9) with respect to a particular $\nu _ { \prime } . \textit { J } ^ { = } 1 , \dots \dots n$ , yields

$$
\left[ - \frac {u ^ {\prime \prime} (s)}{\left(u ^ {\prime} (s)\right) ^ {2}} \right] \left[ \frac {\partial s ^ {*} (\mathbf {y})}{\partial y _ {j}} \right] = \sum_ {i = 1} ^ {n} \mu_ {i} \frac {\partial}{\partial y _ {j}} \frac {[ \partial h (\cdot) / \partial a _ {i} ]}{h (\cdot)}.\tag{10}
$$

In order to derive the distribution of the performance metrics y, some additional structure is imposed. In particular, it is assumed that the stochastic variables $x _ { \iota }$ , given the agent's choice of efforts $a _ { \iota }$ , are statistically independent⁶ and are normally distributed with means $m _ { \iota }$ and variances $\eta _ { \iota } ^ { 2 }$ . The measurement error $\epsilon _ { \iota }$ in the metric $y _ { \iota }$ is also assumed to be distributed normally with mean zero and variance $\boldsymbol { \sigma } _ { \iota } ^ { 2 }$ . The errors $\epsilon _ { t }$ are assumed to be distributed independent of $x _ { i } , x _ { j }$ and $\epsilon _ { \ j } , j \neq i .$ , It follows, therefore, that the metrics $y _ { \imath } = x _ { \imath } + \epsilon _ { \imath }$ are distributed independent of the other stochastic variables descrıbed above.

The conditional distribution of each $y _ { t }$ given $a _ { \iota }$ , being a convolution of two random variables following a bivariate normal distribution, is itself normal with mean

$$
E (y _ {i} | a _ {i}) = E (x _ {i} | a _ {i}) + E (\epsilon_ {i}) = m _ {i} + 0 = m _ {i}
$$

and variance

$$
V (y _ {i} | a _ {i}) = V (x _ {i} | a _ {i}) + V (\epsilon_ {i}) = \left(\eta_ {i} ^ {2} + \sigma_ {i} ^ {2}\right).
$$

(In the analysis presented here, it is assumed that only the mean $m , ( a , )$ is affected by the agent's actions. However, this approach could be extended to address the case where the variance of $x _ { \iota }$ can be influenced by the agent's actions.) The probability density function $h , ( \operatorname { J } _ { t } ^ { \prime } \mid a _ { t } )$ is then given by

$$
h _ {i} \left(y _ {i} \mid a _ {i}\right) = \exp \left\{\frac {- 1}{2} \ln 2 \pi V \left(y _ {i} \mid a _ {i}\right) - \left[ y _ {i} - m _ {i} \left(a _ {i}\right) \right] ^ {2} / 2 V \left(y _ {i} \mid a _ {i}\right) \right\}.
$$

Further, since the $y _ { \iota }$ are independently distributed,

$$
h (\mathbf {y} | \mathbf {a}) = \prod_ {i = 1} ^ {n} h _ {i} (y _ {i} | a _ {i}) \quad \text { and }
$$

$$
\begin{array}{r l} \frac {\partial h (\mathbf {y} | \mathbf {a}) / \partial a _ {i}}{h (\mathbf {y} | \mathbf {a})} & = \frac {\partial \ln h (\mathbf {y} | \mathbf {a})}{\partial a _ {i}} = \frac {\partial \ln h _ {i} (y _ {i} | a _ {i})}{\partial a _ {i}} \\ & = [ y _ {i} - m _ {i} (a _ {i}) ] [ \partial m _ {i} (a _ {i}) / \partial a _ {i} ] / V (y _ {i} | a _ {i}) \\ & = [ y _ {i} - m _ {i} (a _ {i}) ] [ \partial m _ {i} (a _ {i}) / \partial a _ {i} ] / [ \eta_ {i} ^ {2} + \sigma_ {i} ^ {2} ]. \end{array}
$$

Therefore,

$$
\begin{array}{r l} \frac {\partial}{\partial y _ {j}} \frac {[ \partial h (\mathbf {y} | \mathbf {a}) / \partial a _ {i} ]}{h (\mathbf {y} | \mathbf {a})} & = 0 \\ & = [ \partial m _ {i} (a _ {i}) / \partial a _ {i} ] / [ \eta_ {i} ^ {2} + \sigma_ {i} ^ {2} ] \quad \text { for } \quad j \neq i, \quad \text { and } \end{array}
$$

It follows from equation (10) that

$$
\frac {\partial s ^ {*} (\mathbf {y})}{\partial y _ {i}} = \frac {- (u ^ {\prime} (\cdot)) ^ {2}}{u ^ {\prime \prime} (\cdot)} \cdot \frac {\mu_ {i} [ \partial m _ {i} (a _ {i}) / \partial a _ {i}) ]}{[ \eta_ {i} ^ {2} + \sigma_ {i} ^ {2} ]}.\tag{11}
$$

Recall that the goal is to characterize the optimal compensation contract, determined as a function of the available metrics. The principal's problem can be decomposed into two steps, one being the aggregation of the multiple performance metrics (the primary interest of the current analysis), and the other being the transformation of this aggregated signal into the ultimate compensation paid to the agent, the unidimensional $s ^ { * } ( \mathbf { y } )$ . Since the right-hand side of equation (11) is independent of $\mathbf { y } .$ , it follows that the optimal compensation contract $s ^ { * } ( \mathbf { y } )$ can be written as $\mathrm {  ~ s } ^ { * } ( \mathrm { \bf ~ y } ) = \mathrm {  ~ s } ^ { * } ( s _ { 2 } ^ { * } ( \mathrm { \bf ~ y } ) )$ ) where $s _ { 2 } ^ { * } ( \mathbf { y } )$ is linear in y and can be interpreted as the aggregated performance evaluation metric, and $s _ { 1 }$ is the mapping of the aggregate into compensation. It follows from equation (11) that

$$
s _ {2} ^ {*} (\mathbf {y}) = \sum_ {i = 1} ^ {n} \rho_ {i} \xi_ {i} y _ {i}\tag{12}
$$

where $\rho _ { \iota } \ = \ \big [ \eta _ { \iota } ^ { 2 } + \sigma _ { \iota } ^ { 2 } \big ] ^ { - 1 }$ is the precision of the metric y, which is inversely related to $V ( x _ { \iota } \mid a _ { \iota } )$ and $V ( \epsilon _ { t } )$ , and $\xi _ { \iota } ^ { \mathrm { ~ ~ } } = \mu _ { \iota } \partial m _ { \iota } ( a _ { \iota } ) / \partial a _ { \iota }$ , is the sensttivit y of the outcome $\cdot \bar { \cdot } _ { \iota }$ (and the metric $\mathbf { \boldsymbol { { \mathbf { \mathit { \mathbf { \mathbf { \mathbf { \Lambda } } } } } } } } _ { \mathbf { \boldsymbol { \mathbf { \Lambda } } } } ^ { \prime } ( \mathbf { \Lambda } )$ to the agent's action $a _ { \iota }$

Precision is a measure of the degree to which the value of the metric can be predicted, given a set of actions. The lack of precision, or increase in the variance, can be seen as being due to two sources. The first is that the relationship between an outcome $X _ { t }$ and corresponding action $a _ { t }$ may contain a great deal of uncertainty' due to the effect of factors outside the purview of the agent. A second source may be a lack $o f$ accuracy, or “noise" in measuring $\boldsymbol { \cdot } \boldsymbol { \cdot } \boldsymbol { \cdot } \boldsymbol { \cdot }$ , i.e., large variations in the values of $\epsilon _ { i }$ . More formally, the inverse of the precision measure can be decomposed into its two constituent components, as follows:

$$
\operatorname{var} \left(y _ {i} | \mathbf {a}\right) = \operatorname{var} \left(x _ {i} | \mathbf {a}\right) + \operatorname{var} \left(\epsilon_ {i}\right)
$$

where the first term on the RHS corresponds to the uncertainty component (the amount of variance in the outcome given a set of agent's actions) and the second term corresponds to the inaccuracy component (the variance of the noise in measuring the outcome).7 Less formally, precision is a measure of the degree to which random factors may augment or countervail the agent's efforis to bring about the outcomes valued by the princıpal. All else being equal, an agent will be better monitored by metrics with higher precision since the same incentives can be provided to the agent while imposing a reduced level of risk. Therefore, a metric with higher precision will be preferred by the principal since it will be more informative about the agent's action choice. This is true whether the greater precision results from greater certainty, greater accuracy, or some combination.

In equation (12), $\xi _ { \iota } = \mu _ { \iota } \partial / \eta _ { \iota } ( a _ { \iota } ) / \partial a _ { \iota }$ is the sensıtrv  of the outcome $x _ { i }$ (and the metric $\cdot ^ { \cdot } { } _ { i }$ to the agent's action $a _ { \iota }$ . Using standard sensitivity analysis in optimization theory (Ioffe and Tihomirov 1979, pp. 292–298) the ξ, is seen to correspond to the change in the principal's expected utility relative to the change in the agent's expected utility when, at the optimal solution, the agent's incentive compatibility constraint for the choice of $\textstyle \dot { \boldsymbol { a } } _ { \iota }$ is perturbed marginally. In other words. $\xi _ { \iota }$ is the marginal value to the principal of providing the incentive to the agent to increase his effort $a _ { i }$ by a marginal unit. Less formally, the degree of sensitivity of a metric (or outcome) can be seen as a measure of the impact that a unit of the agent's effort has on outcomes of tmportance to the principal. The principal will want to encourage the agent's actions that most increase the final payoff to her, and therefore metrics that correspond to these “high payoff”activities that are most sensitive to the agent's actions will be preferred by her relative to those with less impact.8 For a metric to exhibit high sensitivity it must exhibit significant changes during the evaluation period in response to the agent's actions. A very sensitive metric would show a large change in the value to the principal, on average, for even a small additional amount of disutility to the agent resulting from an increase in effort. In terms of the optimal contract, more weight will be placed on metrics with high sensitivity relative to those with low sensitivity. Specifically, in the optimal performance evaluation measure the relative weight on each metric is directly proportional to its sensitivity times its precision.

It is relatively easy to see that precision and sensitivity are independent concepts. Recall that $y _ { \iota } = x _ { \iota } + \epsilon _ { \iota } , i = 1 , 2 , . . . , n$ where the $\epsilon _ { t }$ represent random variations (noise) for each of the n outcomes of interest. Suppose the vector of outcomes x is $\mathbf { x } = k \mathbf { a } + E$ , where k reflects the agent's ability to influence the outcome, and E represents the effect of external factors, assumed to be a normally-distributed stochastic variable. Combining these two cquations results in $\mathbf { y } = k \mathbf { a } + E + \epsilon .$ The ka term represents the degree of sensitivity of the metric, and the second and third terms represent the two components of precision, certainty and accuracy.

Sensitivity and precision need not move together, i.e., metrics may score relatively high on one dimension and relatively low on the other. A simple two-metric example may help to illustrate this point. Imagine a compensation contract between the owner of a high technology corporation (the principal) and the firm's CEO (the agent). The owner may be ultimately interested in the total cash flow stemming from her investment in the firm's stock but, given the difficulty in observing this during the time period of a typical performance contract, may elect to use the level of short-term and/or long-term profits as the metrics $ { \left( { \boldsymbol { \mathbf { \mathit { y } } } _ { t } ^ { \cdot } } \right) }$ , for purposes of the contract. The question then is how much weight to place on either metric. Short-term profits are a relatively more precise metric since the variance surrounding the effects of the agent's actions are relatively smaller than in the case of longer term profits, when many external factors (e.g., general economic conditions; actions of successor managers) may have unaccounted for effects. However, short-term profits may exhibit less sensitivity than long-term profits in that decisions that the agent may take today, e.g., technology selection, may have influence only in the longer run. That is, however hard the agent works he cannot do much to increase short-term profits. In other words, even in a world where no other forces countervailed (making the metric very precise), the sensitivity of the short-term profits metric to the agent's action may still be low. Therefore, the choice of weights for the two metrics would involve balancing these competing effects.

Of course, an actual contract may be based on several (>2) metrics. In particular, in the case of software development it will be argued below that this is the appropriate form for contracts to take. Since the true levels of the agent's efforts a are unobserved, for incentive contracting purposes the principal and the agent agree on a set of performance evaluation metrics y that can be observed. This multidimensionality poses a dilemma for the principal: how to establish a contract that maximizes the agent's efforts appropriately across dimensions; in particular, which metrics to emphasize or weight in the agent's performance evaluation.

In order to effect the appropriate behaviors, the principal will base the agent's compensation in part upon the value of the performance metrics y.1º Since the y are likely to be imperfect surrogates for the x and underlying effort choices a, some uncertainty is present. Therefore, an extreme form of compensation contract involving total reliance on performance evaluation metrics and assurance of certain utility for the principal is unlikely, since this places extreme risk on the agent, who is assumed to be risk averse. Conversely, however, the opposite extreme of zero reliance on the performance evaluation metrics is also unlikely, as this does not allow the principal to offer any incentives for appropriate behavior. These notions are, of course, predicated on the idea that the information costs related to gathering and reporting the y do not swamp the benefits to be gained from superior contracts.

It should further be noted that these results for use of the metrics for performance evaluation purposes are not dependent upon the customary assumption of risk neutrality of the principal.' In a case where both the principal and the agent are risk averse the central results for performance evaluation are unchanged. To evaluate the performance of the agent, the metrics y will be aggregated with weights reflecting sensitivity and precision as described above. In addition, the metrics will also be used for optimal risk sharing when both the principal and the agent are risk averse, where the exact weights for this purpose will depend on their relative risk tolerances.

However, within the range of likely contract forms, there is still room for considerable variation in terms of the choice of individual metrics (the 1,s) and the weight that is to be assigned each metric in the compensation scheme. A metric that is more precise will receive more weight when all of the metrics are aggregated to determine the final performance evaluation than an otherwise identical metric. Similarly for a metric that is more sensitive. A potential issue is the mapping of the weighted performance evaluation metrics to the actual rewards. However, as shown above in equation (12), this third step is straightforward in this analysis, as the rewards will depend directly upon the weighted aggregate of the individual y',s. Therefore, the critical decision problem for the principal is the selection and use of appropriate metrics

## 3. Application of the Model to IS Development

In this three-part section the model developed in §2 is applied to the domain of Information Systems (IS) development. Section A describes the broad overall dimensions of performance evaluation in IS development and gives illustrative examples of the typical metric used in each category. Section B presents specific metric operationalizations of these dimensions gleaned from two mini-case studies. Section C interprets the case study data in light of the model results.

## A. Performance Evaluation in IS Development

The principal seeks to motivate the agent to take actions that increase gross benefits and decrease costs.'² It is assumed that higher effort on the part of the agent increases the expected value of the gross benefits to the principal. In an IS development context the costs and benefits have both long-term and short-term components. In the short term the emphasis is on initial systems development costs, most prominently labor costs. However, there are also longer term matntenance costs associated with each system. Numerous studies have shown that over half of all systems moneys are spent on maintenance (Lientz and Swanson 1981, Boehm 1987) and, most recently, that for every dollar spent on development, nine will be spent on maintenance (Corbi 1989). While many factors (including exogenous factors such as future changes in the business environment) may affect maintenance costs, for information systems development contracting purposes the principal can only attempt to ensure that the system developed by the agent can be maintained at the least possible foreseeable cost.

Benefits have traditionally been much more difficult to quantify, but can also be seen as having both a short- and long-term component. The principal requesting the system can begin to benefit only when the system is completed. Further, the business use of the new system may have to be coordinated with several other business activities, and considerable other resources may have to be committed at the anticipated implementation time for the system. particularly for larger systems. Therefore, if the system is delivered on time, the principal is likely to be better off, ceteris paribus, than if it were delivered late. This corresponds to the notion of timeliness, the ability to deliver the system on or before the deadline. However, in the long term. the ultimate value of the system may be due to the provision of user-desirable functionality which improves organizational performance. This is the notion of effectiveness, and it can only be interpreted in a longer term context.

Therefore, for model illustration purposes, the focus is on four outcomes for the principal to apply the efforts of the agent, represented as $x _ { 1 }$ (initial developmen cost), $x _ { 2 }$ (maintainabılity), $x _ { 3 }$ (timeliness), and $\cdot \bar { \cdot } _ { 4 }$ (effectiveness).13 These are perhaps best presented by means of ${ \mathrm { ~ a ~ } 2 \times 2 }$ matrix.

Table 1 presents four outcomes (x) of interest to the principal requesting the information system.14(It will be useful to bear in mind that “initial development cost" will be an outcome to be reduced, in contrast to the other outcomes which are to be increased.) The princıpal and the agent must jointly agree on a set of performance evaluation metrics y for the compensation contract, If the x are observable by both the principal and the agent in the contractual period, then these may serve as the y. However, if that is not the case, then the principal and the agent must determine surrogate metrics that are jointly observable.

TABL上 1  
Classification Matrix of IS Development Proje  Outcomes

<table><tr><td></td><td>Short Term</td><td>Long Term</td></tr><tr><td>Cost</td><td>Initial Development Cost</td><td>Maintainability</td></tr><tr><td>Benefit</td><td>Timeliness</td><td>Effectiveness</td></tr></table>

## B. Performance Evaluation Metric Operationalizations

In order to determine the type and extent of project measurement used, two sites were seleced as mini-case studies, one an internal development organızation and the other an external firm. They are believed to be representative of typical current practice in information systems development.'⁵

The internal organization is located within a large commercial bank. The information systems development group consists of approximately 450 professional staff members who work at developing and maintaining financial application software for the bank's internal use. The applications are largely on-line transaction processing systems, cperating almost exclusively in an IBM mainframe COBOL environment. The bank's systems contain over 10,000 programs, totalıng over 20 million lines of code. The programs are organized into application systems (e.g., Demand Deposits) of typically 100–300 programs each. Some of the bank's major application systems were written in the mid-1970s and are generally acknowledged to be more poorly designed and harder to maintain than more recently written software. The bank has made some attempts to upgrade its systems development capability. These steps include the introduction of a commercial structured analysis and design methodology, the institution of a formal software reuse library, and the use of some CASE tools on a few pilot projects.

The external organization is a major systems consulting and integration firm that operates nationally. Their staff consists of over 2,000 systems development professionals who are recruited from leading colleges and universities. They develop custom applications and sell customizable packages to a variety of public and private clients. Their various divisions are organized around a small number of specific industries, such as financial services. These divisions tend to focus on software and hardware platforms that are widespread in their respective market segments, although there is some firmwide commonality across divisions via a standardized development methodology and toolset. An emphasis is placed on very large systems integration projects that are often multiyear engagements. A state of the art development environment is maintained, with the firm being an early adopter of most software engineering innovations

B.1 Initial Development Cost—Empirical Observations. At the bank, development cost is tracked through a project accounting system that is used to chargeback systems developer hours to the requesting user department. Hours are charged on a departmental average basis, with no allowance for the skill or experience level of the developer being incorporated into the accounting system. Mainframe computer usage is also charged back to the user, at a “price" designed to fully allocate the annual cost of operating the data center to the users. However, labor costs are generally believed to constitute 80% of the cost at this organization (Kemerer 1987).

At the consulting firm, development costs are tracked through a sophisticated project accounting and billing system, with the main entry being the biweekly timesheets of the professional staff, who may be simultaneously working on multiple projects for different clients. Time and materials contracts typically have multiple hourly rates whereby more project team members are billed at higher rates. Other direct project charges are also administered through this system, especially travel. Development is typically done at the client's site, and therefore hardware chargeback is typically unnecessary.

B.2 Maıntainabılity—Empirical Observations. Long term maintenance costs are, in part, a function of the maintainability of a system (Banker et al. 1991a, 1992). While there are many factors outside the control of both the principal and the agent that can affect maintenance costs (e.g., changes in external business conditions such as regulatory changes), the principal desires that the agent deliver a system that can be maintained at the least possible cost. Therefore, the outcome that is desired is a high level of maintainability. Unfortunately, even the growing recognition of the significant magnitude of maintenance efforts has not yet produced a well-accepted metric for maintainability. The closest approximation to such a notion are the class of software metrics known as complexity metrics (McCabe 1976, Halstead 1977, Banker et al. 1991b). The general notion is that, as systems become more complex they become more difficult to maintain. The various complexity metrics provide a means of measuring this complexity, and therefore can be used both to predict maintenance costs, and as an input to the repair/rewrite decision (Gill and Kemerer 1991, Banker et al. 199la, 1992).

At the bank, while maintenance projects are recognized as the primary information systems development activity, no attempt was made to measure and manage the maintainability of the applications, although most recently interest has been expressed in using the McCabe cyclomatic complexity metrics to aid management in this area. Similarly, at the consulting firm no maintainability measures are tracked, even though the ongoing maintenance of the developed system by the firm is a requirement of many projects.

B.3 Timeliness—Empirical Observations On the benefit row of Table 1, the short run benefit is provided by delivering the system on schedule, what is referred to as system timeliness. Of course, the appropriate duration of a systems development project is very much dependent upon such factors as the size of the system and the productivity of the development staff. Therefore, the timeliness metric is generally stated in relative terms, rather than absolute terms, most typically in relation to a deadline. Thus, a system is delivered “on time" or “two months late." Of course, this metric is really a difference result, and therefore an agent seeking to minimize the difference can direct effort both towards maximizing the time period (deadline) allowed during the project planning stage, as well as towards actually developing the system in such a way as to minimize the delay from the delivery date. However, a tendency on the part of developers to estimate or propose excessively long development times will be mitigated by other controls, i.e., an external developer is unlikely to be awarded such a contract, and an in-house developer may find that the principal chooses not to do the system at all. Therefore, a timeliness metric can be assumed to provide at least partial motivation to develop the system promptly.

At the bank, project schedules are published and the larger projects are tracked via a regular status meeting chaired by the most senior vice president in charge of the information systems function. Project adherence to intermediate milestones is checked, and late projects are flagged for discussion. At the consulting firm, adherence to schedule is monitored through use of a development methodology with standardized milestones. Deliverable deadlines are an important part of many contracts, with clients’ desire to implement systems by certain fixed dates a key contributor to their decision to use an external developer. Some contracts contain penalty clauses for late delivery.

B.4 Effectiveness—Empirical Observations. The fourth and final cell in Table 1 is a long-term benefit, or effectiveness. Effectiveness metrics are much sought, but little or no general agreement has been reached on such metrics. Crowston and Treacy note that:

Implicit in most of what we do in MIS is the belief that information technology (I T), has an impact on the bottom line of the business. Surprisingly, we rarely know if thıs is true (1986, p. 299)

They go on to review the existing literature in this area for the previous ten years and conclude that until more progress is made in identifving performance variables, the best current metrics can only test whether systems engender user satisfaction. This finding was recently reaffirmed by a study of large federal government systems integration projects, where a survey of the program managers revealed that user satisfaction was the most frequently cited measure of success [ADAPSO 1991]. Therefore, commonly accepted effectiveness metrics tend to take the form of surveys of user satisfaction that could be administered at the end of the project.16

At the bank, no formal mechanisms are in place to measure user satisfaction, although occasional efforts are made to interview key users about their needs. At the consulting firm, while user satisfaction is deemed to be highly relevant in terms of its linkage to follow-on contracts, until very recently, no standardized mechanism existed to capture this information. Of course, contractual provisions typically guarantee some minimum level of performance. Beyond this. a small number of newer projects are experimenting with a user satisfaction survey.

## C. Application of Model Results

The results of the previous sections are now combined by applying the measurement criteria from the model to the commonly used operationalizations of IS performance evaluation metrics. From this application some observations are made with regard to the model criteria about the relative emphasis on the current operationalizations in practice.

TABLE 2  
Metric Operationalızations of IS Development Project Outcomes

<table><tr><td></td><td>Short Term</td><td>Long Term</td></tr><tr><td>Cost</td><td>Budget</td><td>Complexity metrics</td></tr><tr><td>Benefit</td><td>Schedule</td><td>User satisfaction</td></tr></table>

Table 2 summarizes the empirically observed operationalizations of the project outcome dimensions from Table 1.

C.1 Precision. The first criterion is the precision of the performance evaluation metrics. The two principal components of precision, lack of certainty, as defined by $\mathrm { V a r } ( x _ { \iota } \mid \mathbf { a } )$ , and lack of accuracy, as defined by $\mathrm { V a r } ( \epsilon _ { \iota } )$ , are considered in turn. Certainty, as defined above, is directly related to the outcome, while accuracy is related to outcome through a specific metric.

There are relatively few factors external to the agent's actions that influence development cost and timeliness, as compared to the long-term outcomes, in that the agent can propose a budget and schedule and then staff the project in such a way as to attempt to meet those goals. Of course, the influence of external factors is not absent. In particular, the interface with other projects can be a source of disruption for the agent. A parallel project may not complete its portion in time for the agent's project to keep to its critical path and therefore its schedule. Changes in project scope are also an important influence, unless the agent carefully manages the changes by ensuring that the schedule and budgets are revised accordingly.

Interruptions to the project are likely to have greater effects on schedule than on the budget. This is because if work on the project is delayed it is often possible to temporarily reassign staff to work that does not have them charging time to the project, thus avoiding a budget overrun. On the other hand, “time marches on" as far as the deadline goes, with any delay in the critical path making the project late. Therefore, the certainty component of the precision of the budget metric will be higher than that for schedule.

Maintainability as operationalized by complexity metrics would rate a relatively middle score on a certainty scale. The agent's actions can clearly improve complexity metric scores, but he may be constrained by outside limitations, such as the need to reuse portions of existing systems that are relatively complex. Also, there are many dimensions to software complexity, and a metric like cyclomatic complexity measures only one aspect. In fact, it may be argued that overly strict reliance on one complexity metric can merely transfer the complexity to other, unmeasured dimensions, e.g., data complexity. Therefore, complexity metrics are relatively less certain than budget metrics.

Finally, least certain of all is the system's effectiveness. The system may have been poorly conceived initially by the requester, and therefore, the delivered system, while perhaps meeting the agreed upon technical specifications, may not prove to be valuable. Or, the principal may have done an inadequate job of making the organizational changes necessary for the success of the new system, e.g., reassignment of tasks, retraining, and adjustment of compensation systems. In support of these notions there is a growing body of descriptive work that suggests that many completed systems are never used (Rothfeder 1988, Kemerer and Sosa 1991)

In the accuracy component, the short-term measures clearly allow for more accuracy than the long-term measures. Project management systems routinely track project expenditures and deadlines, and these provide metrics that are relatively objective and accurate versus either maintainability (subject to limitations in measurement and the impact of the unknown nature of future change requests) or effectiveness (subject to the lack of reliability of the measurement instrument and the unknown impact of future changes in the business). For example, if user satisfaction metrics are used, it may be in the interests of the user to not report satisfaction as high, in order to extract additional effort or attention from the developer. These problems with maintainability and effectiveness reduce the precision of metrics for those performance evaluation variables.

Summing these two components of precision, certainty and accuracy, it can be seen that, at these two sites, development cost scores relatively the best on both componenis, while effectiveness scores relatively the worst. Timeliness and maintainability rate in the middle of these two extremes in terms of their precision

C.2 Sensitivity. If sensitivity is high, then for a small amount of disutility the agent can significantly increase the utility of the principal. Development cost, operationalized at both sites primarily as labor work months, is a sensitıve metric, that is, it possesses a relatively high value for $\mu _ { 1 } \partial m _ { 1 } ( a _ { 1 } ) / \partial a _ { 1 }$ . A project manager can change the expected development cost by deciding which staff members are to be assigned and how they are to be deployed, and by providing leadership and supervision during the development process. In addition, a manager may also influence project cost by under-reporting his own hours, as a means of adding value to a project without exceeding the budget. However, project managers at the consulting firm can typically exert more leverage than can their counterparts at the bank since at least some differential labor rate structures exist. The consulting firm agent can exploit different mixes of high and low cost staff in an attempt to keep within the budget. At the bank all staff are charged to projects at the bank's average labor cost, and therefore a bank project manager has somewhat less flexibility.

One concern with this analysis might be the notion that a project manager at the bank could essentially “game" meeting a particular budget by assigning a staff of say, for example, more productive than average people to a project with a tight budget since everyone is charged at the same \$40/hour rate. However, this scenario does not ultimately change the sensitivity rating, due to the following logic. If the project manager is assumed to be at a low level where he has only one project in whose outcome he is interested, then he might attempt such an optimization. However, at the bank there are multiple projects and hence multiple project managers, all of whom would like to game the situation this way, and therefore. through competition for resources, this strategy is not likely to obtain. Alternatively, one might posit a “super project manager," responsible for all the current projects. In this case this individual is presumably interested in the outcomes of all the projects and cannot staff them all with “above average" personnel.

The other short-term measure, timeliness, as operationalized by the degree to which the deadline is met, is also a sensitive metric. However, timeliness is not very highly sensitive, since while assigning less or more expensive personnel can directly affect the project cost, the influence on timeliness is less direct. An example of this is Brooks's research which has been summarized into the aphorism that “adding staff to a late project makes it later," denying the ability of the agent to move the timeliness metric in the desired direction in a substantial way (Brooks 1975, p. 25). The less sensitive nature of schedule performance depends in part upon the project specification being sufficiently concrete as to disallow the possibility of significant “gaming,' i.e., undocumented reductions in scope that allow the appearance of on time delivery of what in reality is significantly reduced functionality. This is the situation at both of the case study sites, particularly the external consulting firm where formal contracts are the norm. However, where this is not the case it might be expected that timeliness would be the most sensitive metric.

In terms of the longer-term metrics, the cost side is reflected by maintainability, possibly operationalized by complexity metrics (although not done at either site), and the benefit side is referred to as effectiveness, possibly operationalized by user satisfaction (although not done regularly at either site). Maintenance, despite its growing economic importance, is a relatively unstudied and therefore poorly understood phenomenon. Since the relationships among agents' efforts and their impact on maintainability are not well understood, and since metrics for measuring maintainability are immature, it follows that the relationship among agent's efforts and complexity metrics are even less well understood. The project manager's ability to influence maintainability is limited, and thus the sensitivity of maintenance metrics can only be described as relatively low.

Conversely, the user satisfaction metrics used to indicate effectiveness should show relatively high sensitivity. Often, the inclusion of a seemingly small feature can greatly improve the user's perceived or even actual value for the application. If the IS development agent is aware of user needs and preferences, particularly regarding user interface issues, he is often able to greatly influence user satisfaction. Since the literature notes the strong influence played by expectations in user satisfaction, a talented agent may be able to greatly control expectations, and therefore the value of the metric at the end of the project.

In summary, for these two sites, the relative sensitivity of the commonly used metrics are as follows. If used, user satisfaction exhibits relatively high sensitivity. Timeliness and development cost may also be relatively sensitive, with the consulting firm agents often having a greater ability to influence this than bank project managers. Finally, maintainability, with the current poor understanding of the relationship between complexity and maintenance, is relativelv the least sensitive of the four.

C.3 Summary. In examining all of the performance evaluation metrics relative to the criteria defined by the model, it is proposed that at these two sites development cost and timeliness rate well in terms of both sensitivity and precision. User satisfaction seems sensitive, but fares poorly in terms ofits precision, while maintainability is only moderately sensitive and moderately precise.

Recall equation (12):

$$
s _ {2} ^ {*} (\mathbf {y}) = \sum_ {i = 1} ^ {n} \rho_ {i} \xi_ {i} y _ {i}.\tag{12}
$$

This result shows that a linear aggregation of the scores will produce the correct ranking of performance evaluation metrics. In other words, metrics with relatively higher levels of precision and sensitivity will receive more weight in the final aggregated evaluation. As shown in Table 3, an ordinal ranking of the metrics discussed in the mini-case studies would find budget and schedule performance at the top, followed by user satisfaction and then followed by maintainability

TABLE 3

<table><tr><td colspan="5">Relative Metric Values</td></tr><tr><td rowspan="2">Metric</td><td colspan="3">Precision</td><td rowspan="2">Ordinal Score</td></tr><tr><td>Certainty</td><td>Accuracy</td><td>Sensitivity</td></tr><tr><td>Budget Performance</td><td>High</td><td>High</td><td>Medium to High (bank) (consultants)</td><td>1</td></tr><tr><td>Schedule Performance</td><td>Medium</td><td>High</td><td>High</td><td>1</td></tr><tr><td>User Satisfaction</td><td>Low</td><td>Medium</td><td>High</td><td>2</td></tr><tr><td>Maintenance complexity</td><td>Medium</td><td>Medium</td><td>Low</td><td>3</td></tr></table>

To summarize, this ranking is based on observations at the two sites. In practice, both sites emphasize measurement on two dimensions, cost and timeliness, that are seen to possess relatively the most precision and sensitivity, as predicted by the model. How these dimensions might fare at other sites, or at these same sites in the future, are discussed in the following section.

## 4. Discussion

In this section the generalizability and implications of the results shown in §3 are discussed. Limitations of the model and possible extensions to it are also presented

## A. Generalizability and Implications of the Results

In examining the results presented above, one possible concern might be with the representativeness of the two mini-case studies. While their measurement practices are as predicted by the model, to what degree are they believed to be representative of current practice?

Three other sources of data on the current state of measurement suggest that the two mini-cases may be quite typical of current practice. The first source is a survey of over 140 medium to large IS departments conducted in 1988. in which managers were asked what measures they currently used (Howard 1988). By far the leading measures were work-hours per project, a measure of development cost (78% of managers surveyed), and adherence to delivery dates, a measure of timeliness (72%). The third most used measure was computer resource usage, which was only mentioned by 27% of the respondents. All other measures were less frequently reported, and, in particular, “module size," a potential measure of maintainability, was reported by only 8% of the respondents.

A second independent source is some descriptive data from the text by Jones (1991). His reports about the status of software measurement in various industries are worth quoting at length:

Companies such as Exxon and Amoco were early students of software productivity measurement, and have been moving into . . . user satısfaction as well. . The leading insurance companies such as Hartford Insurance, UNUM. USF&G, John Hancock, and Sun Life Insurance tend to measure productivity, and are now stepping up to. user satisfaction measures as well.. In the manufacturing, energy, and wholesale/retail segments the use of software productivity measurement appears to be proportional to the size of the enterprise: the larger companies with more than a thousand software professionals such as Sears Roebuck and J C Penney measure productivity, but the smaller ones do not. . . user satisfaction measurement are just beginning to heat up within these industry segments. Companies such as Consolıdated Edıson, Florida Power and Light, and Cincınnatı Gas and Electrıc are becoming fairly advanced in software productivity measure. Here too,. user satisfaction measures have tended to lag behınd. (pp. 16–18)

Jones's use of“productivity” here is in a broad sense that receiving more output for the work hours input to the project will result in better performance on both budget and schedule relative to less productive projects. Note that maintainability metrics are conspicuous by their absence from this list, and that user satisfaction metrics tend to lag schedule and budget metrics.

A third source is the work of Humphrey on software process maturity (Humphrey 1988, p. 74). He notes that the first measures adopted by organizations are cost and schedule metrics, and it is not until stage four of the five-stage model that more comprehensive measures are expected to be implemented. It should be noted that the vast majority of software development organizations in the United States are currently at stages one or two.

These independent observations corroborate what was observed at the two minicase studies. Budget and schedule metrics are in wide use, while effectiveness measures in the form of user satisfaction metrics are less widely adopted. Measures of maintainability are completely absent from these discussions, which is consistent with the results in Table 3 which suggest that they are the least likely of the four to be adopted.

The implications for this choice of adoption are worthy of managerial concern. The emphasis on short-term results may produce decisions on project planning, staffing, and technology adoption that are suboptimal for the organization in the long term. For example, the almost total lack of measurement of the maintainability impacts of project decisions implies that only minimal effort will be devoted towards, for example, useful design and code documentation or adherence to structured coding precepts, to the extent that these activities are viewed as costly or otherwise compete for resources with different activities that are measured. Similarly, an emphasis on schedule and budget measurements in preference to effectiveness measures implies an emphasis on delivering any product on-time, rather than a better product later, where this latter option might be the preferred alternative for the organization.

Another application of these results could be on the part of external IS development firms. As agents typically bidding on competitive contracts, one method of increasing the desirability of their services to the principal is by incurring so-called bonding costs (Jensen and Meckling 1976). These bonding costs are actions by the agent to provide assurances to the principal that possible goal incongruencies on the part of the agent will be offset by such costs. One way for IS development agents to do this would be to develop performance “guarantee" metrics that have relatively high levels of precision and sensitivity upon which a contract can be based. For example, the external consulting firm portrayed in this mini-case study could provide suggested maintainability and effectiveness measures that it was willing to adhere to as part of its proposal. Such a proposal would be viewed more favorably by the principal than one without, all other things being equal.

Most importantly, while some of these conclusions may have been made by other observers, the current research provides a theoretically grounded formal model which provides concepts that predict the choice of performance metrics in information systems organizations. These concepts conceivably can be used then to diagnose and improve current metrics and support the development of new metrics. With an informed urderstanding of why it is that budget and schedule metrics are preferred in practice, managers who wish to provide more balanced project outcomes by, for example, seeking to incorporate measures of maintainability into the development contract, should seek to discover and/or develop maintainability metrics that possess high levels of precision and sensitivity. For example, if code complexity metrics such as McCabe's cyclomatic complexity are shown to be good predictors of future maintenance costs, and if the agent can be given sufficient control over the code. perhaps through automated restructurers, such that he can influence these metrics in the appropriate direction, then inclusion of such measures in performance evaluation contracts can be expected to increase (Gill and Kemerer 1991).

## B. Limitations and Possible Extensions to the Results

The discussion so far has been limited to application of the results of the model to examples in traditional information systems development that are currently observed. Two obvious extensions to this analysis would be to (a) apply the model to different development environments, and (b) speculate as to future trends that may have some impact on these results.

Different environments may have available metric operationalizations that exhibit higher precision or sensitivity or both versus their counterparts in traditional information systems. For example, the effectiveness dimension is traditionally perceived as difficult to quantify. However, in another environment this may not be the case. For example, in a safety critical application, such as real-time control of a nuclear power plant, software reliability may be the overwhelming criterion, and therefore the degree to which the software has been tested and can be “proven" correct may swamp all other possible effectiveness considerations. To the degree that metrics for reliability exhibit higher precision relative to the equivalent user satisfaction metric of traditional :nformation systems, and to the degree that reliability is a highly valued outcome dimension, it will be weighted more heavily. Another example might be the effectiveness of a real-time military fire control system which may depend almost solely on its operational performance (speed). This may lend itself to easily definable metrics that possess desirable properties.

One change that may occur over time within the commercial information systems environment is greater recognition of the abilitv to measure and improve software maintainability (Swanson and Beath 1989, Chapter 8). While the importance of the maintenance activity has been recognized for over a decade (Lientz and Swanson 1981) it is only recently that research has linked measures of complexity to maintainability (Gibson and Senn 1989, Gill and Kemerer 1991, Banker et al. 1991a, 1992). This realization has been accompanied by the commercial availability of automated tools that deliver the metric values. To the degree to which these static analysis tools are delivered within CASE environments, rather than having to be justified and purchased as stand-alone tools, their use can be expected to increase. Therefore, over time a greater understanding and refinements of software complexity metrics as operationalizations of the maintainability dimension may improve the precision of this metric. The sensitivity of maintenance metrics may also improve as research in this field provides clearer direction to managers to best apply their efforts in reducing maintenance requirements.

A further interpretation of the results from the model would be to move beyond the positive or descriptive aspects and use the results to argue for greater emphasis on development and improvement of metrics for both effectiveness and maintainability, as these are the two dimensions least well represented by current metrics. For example the effectiveness dimension would be emphasized more if there were a more precise metric than the current user satisfaction metric. It should be noted that this result for effectiveness, derived from the agency theory perspective, matches well with some current calls from practitioners for better measures of the “business value" of IS development (Banker and Kauffman 1988) and with movements toward user-centered design within the human-computer interaction research community (Grudin 1991)..

## 5. Concluding Remarks

This paper has developed a principal-agent model that provides a common conceptual framework to illuminate current and future practice with regard to performance evaluation metrics for information system development. Given the principalagent nature of most significant scale IS development, insights that will allow for greater alignment of the agent's goals with those of the principal through incentive contracts will serve to make IS development both more efficient and more effective. An important first step in this process is gaining a better understanding of the behav-

The current research provides a theoretically grounded formal model which defines criteria that predict the choice of performance metrics in information systems organizations. The insights available from the model both suggest explanations as to the current weighting of the dimensions of IS development performance, and provide insights into where better metrics are needed if the current largely unsatisfactory situation is to be remedied. These concepts can conceivably be used to diagnose and improve current metrics and support the development of new metrics.

In terms of future research, a natural follow-on would be to perform a formal empirical validation of the proposed relative weightings given a set of performance evaluation metrics. This will require the development of an instrument to measure the model's sensitivity and precision constructs. The ultimate value of such research will be in an increased understanding of how best to evaluate current systems development performance, so as to provide guidance to managers on how best to improve that performance. Given the key role played by systems development in enabling strategic uses of information technology, such improvement is of critical importance to the management of organizations.\*

Acknowledgements. This research was made possible, in part, by support from NSF Grant SES-8709044 (Carnegie Mellon University). the Center for Information Systems Research (MIT) and the International Financial Services Research Center (MIT). Helpful comments on earlier drafts were received from C. Beath, E. Brynjolfsson, G. Kaufman, S. Kekre, R. Klepper, T. Malone, T. Mukhopadhyay, W. Orlikowski, and J. Whang. Helpful comments from three anonymous referees and the Associate Editor are gratefully acknowledged.

Goodhue, D. “IS Attitudes: Toward Theoretical and Definition Clarity," Proceedings of the Seventh Internauonal Conterence on Informauon Systems. San Diego, California, December 1986, 181-194.

## Bibliography

ADAPSO, “Observations on Successful Federal Systems Integration Programs. An ADAPSO Survey of Industry and Federal Agency Program Managers," ADAPSO Federal Information Systems Integration Committee Technical Report, June 1991.

Anthes, G. H., “Oversight Agencies Neglect Role of User Satisfaction," Computerworld, 81 (July 22 1991).

Banker, R. D. and S. M. Datar, “Sensıtivity, Precision and Linear Aggregation of Sıgnals for Performance Evaluation," Journal of Accounting Research, 27, 1 (Spring 1989), 21–39

, C. F. Kemerer and D. Zweig, “Software Complexity and Software Maintenance Costs,"MIT Sloan School Working Paper #3155-90, Jaunary 1992

Banker, R. D , S. M. Dater and D. Zweıg, “Complexity, Structuredness, and the Rate of Errors in Application Programs," University of Minnesota Working Paper, 1991a,

and -. “Software Complexity Metrics: An Empırical Study," University of Minnesota Working Paper, 1991b

and R. Kauffman, “Strategıc Contributions of Information Technology: An Empırical Study of ATM Networks," Proceedings of the Ninth International Conference on Informaton Systems, Minneapolis, Minnesota, 1988, 141–150.

Beath, C. M. and D. Straub, "Managing Informaton Resources at the Department Level: An Agency Perspective," Proceedıngs of the 22nd Hawaii Internattonal Conterence on Systems Sciences, Kailua-Kona, Hawaii, January 1989, 151-159.

Bennett, A., “Payıng Workers to Meet Goals Spreads, but Gauging Performance Proves Tough," W’all Street Journal, B1 (September 10, 1991).

Berger, P., “Selecting Enterprise-Level Measures of IT Value," in Measuring Business V’alue of Informatton Techno'ogtes, P. Berger, J. G. Koielus and D. E. Sutherland (eds.), ICIT Press, Washington DC, 1988, 59–92.

Boehm, B., “Improving Software Productivity," Computtr, 20. 9 (September 1987), 43–57.

Brooks, F., The Mythical Man-Month, Addison-Wesley, 1975.

Chismar, W., C. H. Kriebel and N P. Melone, “A Criticism of Information Systems Research Employing User Satisfaction,' " Graduate School of Industrial Adminıstration, Carnegie Mellon University Work-1ng Paper 24-85-86, 1986.

Cooper, R. and T. Mukhopadhyay, "Toward the Formulation and Validation of a Microeconomic Production Approach for Management Information System Effectiveness,"Carnegie Mellon University Working Paper, November 1990

Corbi, T. A., “Program Understanding: Challenge for the 1990s," 1BM Svstems Journal. 28, 2 (1989). 294-306.

Gibson, V. R. and J. A. Senn, “System Structure and Software Maintenance Performance " (ommunicatons of the 1CM, 32. 3 (March 1989), 347–358

Gill, G. K. and C. F. Kemerer, “Cyclomatic Complexity Density and Software Maintenance Productivity," IEEE Transaction on Software Engineering, 17, 12 (December 1991). 1284–1288.

Gode, D. K., A. Barua and T. Mukhopadhyay, "On the Economics of the Software Replacement Problem," Proce?dings of the Ith Internattonal Conference on Informatton Systems Copenhagen, Denmark, pp. 159–170, December 1990

- , “I/S Satisfactoriness: An Outeomes Measure for MIS Research," University of Minnesota MISRC Working Paper MISRC-WP-89-05, October 1988

Grudın, J.. “Interactive Systems: Bridging the Gaps between Developers and Users," 1EEl: Computer, 24, 4 (Aprl 1991), 59–69.

Gurbaxanı. V and C F Kemerer, “An Agent-theoretic Perspective on the Management of Information Systems," Proceedıngs of the 22nd Hawau Internattonal Conference on System Sciences. Kailua-Kona, Hawan, 1989, 141–150

and , “An Agency Theory View of the Management of End User Computing," Proceedings of the 11th International Conference on Information Svstems. Copenhagen, Denmark, 279–290, December 1990.

Halstead, M., Elements of Software Suence, Elsevier North-Holland, New York, NY, 1977.

Harrıs, M and A. Raviv, “Optımal Incentive Contracts with Imperfect Information," Journal of Eco nomic Theory, 20. (1979), 231–259.

Holmstrom, B . “Moral Hazard and Observability," Bell Journal of Economıcs, 10, 1 (Spring 1979), 74-91.

and P. Milgrom, “Multi-task Princıpal-Agent Analyses: Incentive Contracts, Asset Ownershıp and Job Design." Yale Universıty Workıng Paper 45, May 1990

Howard. P. C., “Trends in Applcation Development Productivity." System Development, 8, I1 (November 1988), 1–5

Humphrey, W. S., "Characterizing the Software Process: A Maturity Framework," IEEE Software, 5, 3 (March 1988), 73–79.

Ioffe, A D and V. M. Tihomirov, Theorr of Extremal Problems, North-Holland, New York. NY, 1979

Izzo, J., The Embauled Fortress Strategies for Restoring Information Systems Productivity. Jossey-Bass San Francisco, CA, 1987.

Jensen, M. and W. Mecklıng, “Theory of the Firm: Managerial Behaviour, Agency Costs, and Ownership Structure," Journal of Financial Economics, 3, 305–360, 1976

Jones, C., 1pphed Software Measurement, McGraw-Hill, New York, NY, 1991.

Kemerer, C F., Measurement of Software Development Productvity, Unpublshed Carnegie Mellon University Ph.D. Thesis, 1987.

- and G. L Sosa, “Systems Development Risks in Strategic Information Systems." Informatton and Software Technology, 33, 3 (April 1991), 212–223

Kirkpatrick D , "Why Not Farm Out Your Computıng?," Fortune (September 23, 1991). 103–112.

Klepper, R , “An Agency Theory Perspective on Information Centers," Proceedtngs of the T'wentγ-Third Annual Hawau International Conference on System Sciences, Kailua-Kona, Hawaii, January 1990., 251-259

Lambert, R. A . “Long-term Contracts and Moral Hazard," Bell Journal of Economıc s, (1983), 441–452

Lientz, B P and E. B. Swanson, “Problems in Application Software Maintenance." Communications of the /1CM1, 24, 11 (November 1981), 31–37.

McCabe. T J, “A Complexity Measure." IEEF. I ransacttons on Sofiware Engineering, SE-2, 4 (1976). 308-320

Mehler, M., “Reining in Runaway Systems," Informatton W'eek, 351 (December 16, 1991), 20–24.

Melone, N. P., “Theoretical Assessment of User-Satisfaction Construct in Information Systems Research," Management S(tence, 36, 1 (January 1990), 76–91.

Miller, J., "Information Systems Effectiveness. The Fit Between Business Needs and System Capabilities," Proceedıngs of Tenth International Conference on Information Systems, Boston, MA, December 1989 273-288

Mukhopadhyay, T and R. B. Cooper, “Impact of Management Information Systems on Decisions," Omega 20, 1 (1992), 37–49

Richmond, W. B., A. Seidmann and A. B. Whinston, “Incomplete Contracting Issues in Information Systems Development Outsourcing." Dectston Support Systems, in press, 1992.

Rogerson, W., “The First-Order Approach to Princıpal-Agent Problems," Econometrica, 1985.

Ross, S , “The Economic Theory of Agency The Principal's Problem," 1merican Economic Revten, (1973),134-139

Rothfeder, J., “lt's Late, Costly, and Incompetent-But Try Firing a Computer System,"Bustness W’eek (November 7, 1988), 164–165.

Swanson, E. B and C M. Beath, Maintaıntng Inforinatton Systens in Organtzattons, John Wiley & Sons. New York, 1989.

and - , "Departmentalization in Software Development and Maintenance," (ommunicattons of the 1CM1 33, 6 (June 1990). 658–667

Ware, R., “Gong-Ho Projects." Journal of Systems Management, 41, 12 (December 1990), 18.

Whang, S., “Contracting for Software Development," Management Sctence 38, 3 (March 1992). 307– 324.
