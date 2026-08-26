---
otero_id: 17384
otero_key: "GY6FZA95"
title: "A decision support system for stochastic cost-volume-profit analysis"
authors: "Ramarathnam Ravichandran"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90069-f"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for stochastic cost-volume-profit analysis

Ramarathnam Ravichandran

Ball State University, Muncie, IN, USA

A decision support system for applying cost-volume-profit analysis in an uncertain environment is presented. Product mix programming problem is considered when the contributions of the products are stochastic in nature. Previous studies in this area have assumed that the product contributions are normally distributed and are independent of each other. These assumptions are relaxed in this paper by using four moments of the contributions. A decision support framework for CVP analysis with four moments is presented. The goal is to assist the decision maker in using multiple models and data sources for achieving different objectives. Various models needed for a flexible formulation of the decision problem are discussed. Components of the database and features of the dialog interface are presented along with a prototypical implementation.

Keywords: Decision support systems; Cost-volume-profit analysis; Uncertainty; Product mix programming; Four moments

![](/api/attachments/GY6FZA95/fulltext/images/20fbe878e9de3b367c57a8085bddca9601a188de97995945209cebe2d7f76155.jpg)

Ramarathnam Ravichandran ('Ravi') is an Assistant Professor of Information Systems at Ball State University, Muncie. He received his Ph.D. in Management Information Systems from Indiana University, Bloomington, IN. His articles have appeared in Decision Sciences and other journals. He is a member of Association for Computing Machinery, Decision Sciences Institute, The Institute of Management Sciences, and American Association of Artificial Intelligence. His current research interests include decision making, decision support system, database design, expert systems and systems development.

## 1. Introduction

Cost-volume-profit analysis is one of the widely used models for studying the relationships between the firm and the environment $[13,58,70]$ . Stochastic versions of the Cost-Volume-Profit (CVP) model are oriented toward supporting management in the decision-making process by providing pertinent information on the probability distribution of profit, including the expected profit, the variance of profit, the probability that profit exceeds a certain level, breakeven probabilities, sales volumes under different objectives, etc. This information is a function of the structure of the CVP relationships and the key variables chosen to describe these relationships $[21]$ . Hence the assumptions made about the variables selected and about the nature of the model must resemble the environment as closely as possible to provide relevant and correct information to the decision-maker (DM).

There has been a growing body of literature on the stochastic CVP model which examines the various assumptions about the model and the variables it represents under different scenarios $[1,6,13,14,15,19,34,43,45,46,47,50,60,73,77]$ . The primary emphasis has been, however, on the accuracy or appropriateness of the model in a particular situation with scant attention paid to the required interaction of the DM with the model to obtain a realistic overview of the whole situation. The decision-maker will have to specify the nature of the model and the relationships between the variables to derive a pragmatic representation of the situation.

In this paper we consider the case of a firm with multiple products operating under resource constraints. Previous studies in this area have assumed that product contributions are normally distributed and are independent of each other. The first objective of this paper is to relax these assumptions by using four moments of the contribution distribution. The second objective of this paper is to present a decision support framework for CVP analysis, which will assist the DM in effectively using multiple models and data sources for achieving different goals $[10,69,72]$ .

The plan of the paper is as follows. In the following section CVP analysis is discussed. Four moments are incorporated into the CVP analysis in the next section. Practical difficulties arising in the implementation of four moments approach are discussed in the following section. In the next section the decision support process is delineated and the components of the DSS are outlined. The next three sections deal with the model base, the data base and the dialog interface components of the DSS. A prototypical implementation is then presented.

## 2. CVP analysis

In this section, we discuss the CVP analysis in the context of product mix programming problem. The term product is used here in the generic sense, and thus includes both products and services, e.g., automobiles, financial portfolios. The objective is to arrive at a product mix that achieves a set of goals while obeying certain constraints. We start off with a simple version of the problem and gradually introduce more general formulations.

1. First, we start with a deterministic version of the problem. Contribution of each product is assumed to be fixed. The goal in this problem is to maximize the total contribution from all the products.

2. Next we let the contributions be stochastic. It is assumed that that contributions are normally distributed. The goal is to maximize the total contribution, while minimizing variations in the total contribution.

3. The DM may desire a certain probability of achieving a target profit level. The problem formulation is modified to take into account such goals.

4. Finally, we relax two assumptions that have been made by prior research in the product mix programming area. We relax the assumption that the contributions are normally distributed. The assumption of independence of product contributions is also relaxed.

## 2.1. Deterministic CVP analysis

Assume that a firm has fixed costs $\Pi_{m}$ and a target profit level $\Pi_{T}$ . Consider the firm with a single product. Let the variable cost associated with each unit be V, the selling price be P, with its contribution P-V or C. If the firm sells X units of the product, the total contribution is CX, and the total profit is $CX - \Pi_{m}$ . Using this relationship in the single product case, the DM knows how many units are to be sold in order to break even $(X = \Pi_{m}/C)$ and how many units in order to reach the target profit level $(X = (\Pi_{m} + \Pi_{T})/C)$ . In order to maximize profits, the firm will maximize its total contribution (CX).

Consider the case of n products. For the ith product, let the contribution be $c_{i}$ . If $x_{i}$ units of product i are produced and sold, then the contribution from product i will be $c_{i}x_{i}$ . The firm's goal is to maximize the sum of the contributions from all the products. The problem is to determine the number of units $x_{i}$ for each product i that will maximize the total contribution. Thus the goal is

$$
\operatorname{Max} \sum_ {i = 1} ^ {n} c _ {i} x _ {i}.\tag{1}
$$

If we let c be the contribution vector and x be the unit vector we can restate the objective function above as:

$$
\text { Max } c ^ {\prime} x.\tag{2}
$$

While deciding on x, the firm is usually faced with constraints. The constraints may relate to labor hours, raw materials, machine capacity, demand for the product, restrictions due to tax laws affecting a financial portfolio, etc. The decision problem in this case is

$$
\text { Max } c ^ {\prime} x\tag{3}
$$

such that

$$
A x \leq b,
$$

$$
x \geq 0,\tag{4}
$$

(5)

where c = contribution vector, x = unit vector (number of units for each product), A = constraint coefficient matrix, and b = vector of right hand side coefficients for the constraints.

## 2.2. Stochastic CVP analysis

In the above discussion, we have assumed that product contributions are fixed. However, the contribution of a product can be stochastic in nature. Let the product contributions be normally distributed. The firm's goal is to maximize the total contribution while reducing the fluctuations in the total contribution. The Mean–Variance (MV) framework [62,75] widely used in the financial portfolio management can be applied in this context. The MV framework seeks to maximize return while minimizing risk. Contribution of a product can be viewed as return from an investment. Let $\hat{c}$ be the mean vector for product contributions (the return component) and G be the dispersion matrix for contributions (the risk component). Thus the decision problem is

$$
\text { Max } \hat {c} ^ {\prime} x - x ^ {\prime} G x\tag{6}
$$

$$
\mathrm{suchthat}
$$

$$
A x \leq b,\tag{7}
$$

$$
x \geq 0,\tag{8}
$$

where $\hat{c} =$ mean contribution vector, and $G =$ dispersion matrix of the contribution.

Most often high return investments suffer from high risk, while low return investments enjoy low risk. Assuming that the DMs prefer lower risk levels to higher ones, a tradeoff is to be made between the level of return and the level of risk. A speculative DM may prefer 'high return-high risk' products to 'low return-low risk' products while a conservative DM may opt for 'low return-low risk' products. Under the MV framework, an efficient frontier is generated from which the DM selects points which satisfy the individual preferences for risk and return. A parametric programming approach can be used here. The objective function in Equation 6 is modified as

Max $\hat{c}'x - \beta x'Gx$

(9)

where $\beta$ is varied from 0 to $\infty$ . If $x'Gx$ is positive definite, an optimal solution for each value of positive $\beta$ exists. This set of solutions forms the efficient frontier. Points along the efficient frontier that will satisfy the DM's specified goals are then selected.

## 2.3. Incorporation of safety-first goals

The DM, while seeking to maximize returns, may want to be assured that losses are avoided

Also the DM may want to be assured that a certain target profit will be attained with a given probability. Such assurances on lower bounds on contribution levels may reduce the chances of achieving higher profits. In these situations, wherein certain goals geared toward safety take precedence over maximization of contribution, 'safety-first criteria' [51,74] are useful. Three safety-first goals have been put forth in the context of CVP analysis [19]. The following terms need to be defined for further discussion of these criteria.

$$
\alpha_ {(i)} = \text { Probability   of   breaking   even };
$$

$$
\begin{array}{r l} \alpha_ {1} & = \text { Probability   of   achieving   the   target } \\ & \text { profit }; \end{array}
$$

$q_{0}, q_{1} = \alpha_{0}, \alpha_{1}$ fractiles of the distribution of total contribution;

E = Solution matrix containing decision vectors along the efficient frontier.

The goals are:

1. Maximize the probability of success of achieving a target profit level (Max $\alpha_{1}$ ).

2. Maximize the target profit level with a given probability of success (Max $\Pi_{T}$ given $\alpha_{1}$ ).

3. Maximize the total contribution, given target profit level and probability of success (Max $\hat{c}'x$ given $II_{T}$ and $\alpha_{1}$ ).

Our objective is to select feasible solution points from the efficient frontier which will satisfy these goals. The above goals can be achieved through the following procedures [19]:

1. Maximize $\alpha_{1}$ :

$$
\text { Find } x _ {i} ^ {*} = \max _ {E} \left[ \frac {\hat {c} ^ {\prime} x - (\Pi_ {m} + \Pi_ {T})}{(x ^ {\prime} G x) ^ {1 / 2}} \right].\tag{10}
$$

2. Maximize $\Pi_{T}$ given $\alpha_{1}$ :

$$
\text { Find } x _ {2} ^ {*} = \max _ {E} \left[ \hat {c} ^ {\prime} x - q _ {1} (x ^ {\prime} G x) ^ {1 / 2} \right].\tag{11}
$$

3. Maximize $\hat{c}'x$ given $\alpha_{1}$ and $\Pi_T$ :

$$
\text {   Find   } x _ {3} ^ {*} = \max _ {E} \left[ \frac {\hat {c} ^ {\prime} x - (\Pi_ {m} + \Pi_ {T})}{(x ^ {\prime} G x) ^ {1 / 2}} \geq q _ {1} \right].\tag{12}
$$

It should be noted that a feasible solution may not exist if the aspiration levels of the DM are unrealistically high. The above solutions $x_{1}^{*}$ , $x_{2}^{*}$ , $x_{3}^{*}$ , are optimal if the following condition is satisfied [19]:

$$
\hat {c} ^ {\prime} x - q _ {1} \left(x ^ {\prime} G x\right) ^ {1 / 2} \geq \Pi_ {m}.\tag{13}
$$

2.4. Relaxing normality and independence assumptions

Prior studies in the stochastic CVP analysis area have shown the need for product contribution distributions. Prior studies have considered the cases of (a) single product firm (e.g., [57]) and (b) multiple product firm (e.g., [56]). But the results have not been extended for the case of the firm faced with constraints. Also the product contributions have been assumed to be independent of each other. By using four moments of the contribution distributions, we can relax both of these assumptions.

Each contribution distribution can be considered as a random variable. The four most 'observable' characteristics of a random variable are its location, its dispersion, its skewness and its kurtosis. In prior stochastic CVP programming literature, two assumptions have been made: (a) product contributions are normally distributed, and (b) product contributions are independent of each other. The normality assumption states that contribution distributions have no skewness and kurtosis. Such an assumption has been questioned in prior literature for both financial and non-financial products [5,20,56,57,61,68]. The independence assumption implies that products are independent of each other. However, such an assumption may not hold true [27,57]. For example, contribution of a by-product depends on the contribution of a primary product. Eckel and Hartley [27] discuss the independence assumption in stochastic CVP analysis and present its impact on the results through a simulation. Next we consider how these two assumptions can be relaxed in the stochastic CVP programming problem formulation by using four moments.

The four characteristics of location, dispersion, skewness, and kurtosis of a random variable are usually represented by its first four moments [57]. By using four moments of product contributions, normality assumption is immediately relaxed since non-normal distributions can be specified using four moments. Consider the independence assumption which states that product contributions are not related to each other. Note that the we are interested in the total contribution of all products as our objective variable. Products which are related to each other will affect total contribution distribution differently from unrelated products. The effect of related products on total contribution can be taken into account by using crossmoments. The details of four moments approach to relaxing normality and independence assumptions are presented in the next section.

## 3. Four moments approach to stochastic CVP analysis

It is better to recall that our objective variable, total contribution, is the sum of all the individual contributions. We have to obtain the distribution of total contribution by adding all individual contributions. Each contribution distribution can be considered as a random variable. Next we present formulae to compute four moments of the sum of two random variables. Using these formulae we can compute four moments of the total contribution, given individual contribution distributions and product interdependencies.

## 3.1. Definitions

$$
\begin{array}{l} \mu_ {x} = E (x) = \text { expected   value   of } x; \\ x _ {0} = x - \mu_ {x}; \\ \mu_ {n} (x) = E (x - \mu_ {x}) ^ {n} = E (x _ {0} ^ {n}) = n \text { th } \quad \text { central } \quad \text { moment   of } x; \end{array}
$$

$$
m n (x) = \text { sample   estimate   of } \mu_ {n} (x);
$$

$$
\begin{array}{l} \mu_ {0} (x) = 1; \\ \alpha_ {1} (x) = \frac {\mu_ {3} (x)}{\mu_ {2} (x) ^ {1 . 5}} = \text { measure   of   skewness }; \\ \beta_ {1} (x) = [ \alpha_ {1} (x) ] ^ {2} = \text { measure   of   skewness }; \\ \beta_ {2} (x) = \frac {\mu_ {4} (x)}{\mu_ {2} (x) ^ {2}} = \text { measure   of   kurtosis }; \end{array}
$$

For dependent random variables $x$ and $y$ we define

$$
\begin{array}{l} \mu_ {m n} (x, y) = E (x _ {0} ^ {m} y _ {0} ^ {n}); \\ \mu_ {m 0} (x, y) = \mu_ {m} (x) \text { and } \mu_ {0 m} (x, y) = \mu_ {n} (y). \end{array}
$$

When no confusion can arise, the random variable designations can be dropped. For example, $\mu_{n}(x)$ becomes $\mu_{n}$ and $\mu_{mn}(x, y)$ becomes $\mu_{mn}$ .

Also let

$$
{ } _ { n } C _ { i } = n ! / \left[ i ! ( n - i ) ! \right] ,\tag{14}
$$

$$
{ } _ { n } C _ { i j } = n ! / \left[ i ! j ! ( n - i - j ) ! \right] ,\tag{15}
$$

$$
{ } _ { n } C _ { i j k } = n ! / \left[ i ! j ! k ! ( n - i - j - k ) ! \right] .\tag{16}
$$

Let the dependency between two random variables be denoted by following functional relationships.

$$
y = f (x) + \epsilon ,\tag{17}
$$

$$
E (\epsilon \mid x) = 0,\tag{18}
$$

$$
E (\epsilon \mid x) ^ {n} = \mu_ {n} (\epsilon \mid x) = g _ {n} (x),\tag{19}
$$

where $\epsilon$ is the error term, $f(x)$ is the regression curve of y on x, $g_{2}(x)$ is the scedastic curve of y on x, $g_{3}(x)/[g_{2}(x)]^{1.5}$ is the clitic function, and $[g_{4}(x)/[g_{2}(x)]^{2}]-3$ is the kurtic function [65].

## 3.2. Computation of four moments

The formula for computing sum of two random variables is given below [56]. For $w = p + q$ ,

$$
\mu_ {n} (w) = E \left[ (p + q) - \left(\mu_ {p} + \mu_ {q}\right) \right] ^ {n}\tag{20}
$$

$$
= E \left(p _ {0} + q _ {0}\right) ^ {n}\tag{21}
$$

$$
= \sum_ {i = 0} ^ {n} \left\{\left(_ {n} C _ {i}\right) \left[ \left(\mu_ {i, n - i} (p, q)\right) \right] \right\}.\tag{22}
$$

In applying this equation the primary task lies in the determination of cross moments. The computation of cross moments may require the values of the central moments of the primary variables, p and q, beyond the fourth order. Given four moments of a primary variable, central moments up to any order can be rapidly generated by using the formulae given by Kendall and Stuart [54]. Next we present the formulae to compute moments for two cases: (a) independent products, and (b) dependent products. In the case of dependent products, we consider only those relationships characterized by a combination of linear or quadratic regression functions with constant, linear or quadratic scedastic functions. These relationships are well suited for relationships found between various variables in real world situations [65]. These relationships are illustrated in Fig. 1. More complicated dependencies such as higher order regression and scedastic functions or non-constant clitic and kurtic functions are not very meaningful here since the required parameters for these functions cannot be reliably estimated [56].

![](/api/attachments/GY6FZA95/fulltext/images/00b113904f23741c189602ad580a8b1fcac8149f9c8004856588eb560aeb90bd.jpg)  
Fig. 1. Types of relationships between products.

## 3.3. Formulae for moments and cross-moments

1. $x$ and $y$ independent

$$
\mu_ {w} = \mu_ {x} + \mu_ {y},\tag{23}
$$

$$
\mu_ {2} (w) = \mu_ {2} (x) + \mu_ {2} (y),\tag{24}
$$

$$
\mu_ {3} (w) = \mu_ {3} (x) + \mu_ {3} (y),\tag{25}
$$

$$
\mu_ {4} (w) = \mu_ {4} (x) + 6 \mu_ {2} (x) \mu_ {2} (y) + \mu_ {4} (y)\tag{26}
$$

Note that cross moments are not needed.

2. $x$ and $y$ dependent

(a) Linear Regression of $y$ on $x$ : $y = a + bx + \epsilon$ . Homoscedastic error term:

$$
\begin{array}{r l} \mu_ {m n} (x, y) & = \sum_ {i = 0} ^ {n} \left[ _ {n} C _ {i} \cdot b ^ {i} \cdot \mu_ {m + i} (x) \right. \\ & \quad \left. \cdot \mu_ {n - i} (\epsilon) \right]. \end{array}\tag{27}
$$

In this case, the error term can be distributed in any form. Eilon and Fowles [30] have investigated such error terms for investment projects.

ii. Linear scedasticity: $y = a + bx + \epsilon, \mu_{2} - (\epsilon | x) = p + qx_0$

$$
\mu_ {m n} (x, y) = \sum_ {i = 0} ^ {n} \left[ _ {n} C _ {i} \cdot b ^ {i} \cdot \mu_ {n + i, n - i} (x, \epsilon) \right],\tag{28}
$$

where

$$
\mu_ {m, 2 n - 1} (x, \epsilon) = 0,\tag{29}
$$

$$
c _ {2 n} = \mu_ {2 n} (\epsilon | x) / [ \mu_ {2 n} (\epsilon | x) ] ^ {n},\tag{30}
$$

$$
\mu_ {m, 2 n} (x, \epsilon)
$$

$$
= c _ {2 n} \sum_ {i = 0} ^ {n} \left[ _ {n} C _ {i} \cdot p ^ {i} \cdot q ^ {n - i} \cdot \mu_ {n + n - i (x)}\right) \bigg ].\tag{31}
$$

iii. Quadratic scedasticity: $y = a + bx + \epsilon, \mu_2(\epsilon | x) = p + qx_0 + rx_0^2$

The set of formulae include Equations 28, 29, 30 and the following equation.

$$
\begin{array}{r l} \mu_ {m, 2 n} (x, \epsilon) & = c _ {2 n} \sum_ {i = 0} ^ {n} \sum_ {j = 0} ^ {n - 1} \left[ _ {n} C _ {i j} \cdot p ^ {i} \cdot q ^ {j} \cdot r ^ {n - i - j} \right. \\ & \quad \left. \cdot \mu_ {2 n - 2 i - j + m} (x)\right). \end{array} \tag {32}
$$

(b) Quadratic Regression of $y$ on $x$ i. Homoscedastic error term: $y = a + bx + cx^2 + \epsilon$ . Let $g = b + 2c\mu_x$ and $h = -c\mu 2(x)$ . Then

$$
\mu_ {m n} (x, y) = \sum_ {i = 0} ^ {n} \sum_ {j = 0} ^ {n - i} \sum_ {k = 0} ^ {n - i - k} \left[ _ {n} C _ {i j k} \cdot g ^ {i} \cdot c ^ {j} \right.
$$

$$
\left. \cdot h ^ {n - i - j - k} \cdot \left(\mu_ {m + i + 2 j} (x) \mu_ {k} (\epsilon)\right) \right].\tag{33}
$$

ii. Linear Scedasticity: Similar to Linear Regression case above [54].

iii. Quadratic Scedasticity: Similar to Linear Regression case above [54].

## 4. Issues in the usage of four moments model

Several questions arise in the application of four moments model. Under what circumstances can it be used? What types of products are suitable for its application? Can a DM easily understand the implication of four moments? Are intuitive judgments about four moments difficult to make? Each of these issues is addressed next, along with suggestions for enhancing applicability and usage of the four moments model. The need for a DSS is also presented in this section.

One question that arises here is whether the DMs need the four moments approach. Kottas and Lau [57] discuss some examples wherein the DMs need and use skewness and kurtosis measures for the product contributions. Also in the financial literature, the need to handle higher moments is well established. An empirical study by Arditti [4] and a theoretical paper by Levy [59] found exceptions to the practice of using the two parameters of mean and variance. There has been an increased interest in considering higher moments in stochastic analysis (e.g., [61]). Recent empirical studies in the area of capital asset pricing model have supported the need for incorporating skewness in the models [5,20,68]. The four moments model can thus be applied to financial products. It also can be applied to other non-financial products such as agricultural products, oil, automobiles, and airline tickets where there is significant variation in contribution margins. The variation in contribution margin can arise from variations in (a) the sale price of the final product and/or (b) the sub-parts used in the final product. For instance, the contribution margin of a ton of grain can be highly stochastic depending on the prices quoted on the commodities market. The sale price of an automobiles varies depending on the different types of rebates used at different periods of time. In terms of airline tickets, price of one of the component namely the fuel varies significantly.

Another question concerns the ability of the DM to easily understand the implication of four moments. The concepts of skewness and kurtosis are as easy to understand as the concepts of mean and variance. Many people with little or no mathematical training have found skewness and kurtosis useful and significant in describing frequency distributions. [66]. The first two moments capture the location (mean) and dispersion (variation) of the contribution. The third and fourth moments capture the level of skewness and the height of contribution distribution. Skewness captures the symmetry of observations around mean and kurtois the relative number of observations in the vicinity of the mean. Most decision makers prefer high returns (mean) with lower variability (variance). Most decision makers will prefer positive skewness and higher level of kurtosis in their product contributions.

The ability of the DM to obtain intuitive judgments about four moments is yet another concern in the application of four moments model. It may be difficult for even for the mathematically inclined DM to obtain intuitive judgments about the four moments as such. This is a disadvantage of the four moments approach as experienced in assembly line balancing problems [16]. However, this problem can be solved by using several approaches. One way is to use known guidelines for eliciting four moment information from the DM [61]. Another way to obviate this problem is to allow the use of different types of inputs for describing the product distribution. Using such inputs, four moments are computed. Such an approach would obviate the need for direct elicitation of four moments from the decision maker. Possible inputs for computing four moments include (a) frequency distribution, (b) optimistic – most likely – pessimistic values, (c) values at any three percentiles, and (d) functional form. It is this second approach which will be used in the DSS.

## 4.1. Need for a DSS

The incorporation of the four moments in the product mix programming approach increases the complexity of the problem formulation. As a result it needs to be handled by the use of multiple models and data sources. The following factors make the need for a DSS critical:

\- Interactive modeling and analysis: For successful analysis, feedback from the decision maker about intermediate results from the analysis is needed. The decision maker needs to be satisfied about situation modeling at three intermediate points during the analysis: (a) fitting distributions for the product contributions, (b) encountering infeasible quadratic programming solution vectors, and (c) computing attainable goal levels. The decision maker should be able to alter the problem formulation. For instance, in case the best attainable goal levels fall short of expected goal levels, the DM can either reduce the desired goal levels or increase resource capacities. Sensitivity analysis will be useful in this context. The decision maker should have the opportunity to pose 'what if' questions and examine the impact of various resource constraints on the solution. Such an interactive analysis is best supported through a computerized DSS. Several studies have investigated DSS effectiveness in supporting complex decision making processes in different settings [69]. The studies include individual DSS cases [7,33,44,71], field studies [3,23,36,38,53,76], field tests [29,35,39], and laboratory studies [2,8,9,17,18,24,25,26,28,42,48,55,63,69]. Results from these studies indicate that DSSs can improve performance, although results have been mixed. For instance, among field test studies Fudge and Lodish reported higher sales for DSS users than non-DSS users [35]. In a laboratory experiment involving financial planning models groups with access to a DSS made significantly more effective decisions than their non-DSS counterparts [69].

\- Multiple models: For effective decisions, which will be accepted and implemented by the decision maker, appropriate models have to be employed. Specialized decision models have to be employed for modeling (a) stochastic product contributions, (b) relationships among products, (c) successive quadratic programming, and (d) goal seeking. If one model is unsatisfactory to the decision maker, another model needs to be selected and employed. The model base and model base-management features available in a DSS are perfectly suited for such an approach [10].

\- Multiple data items and formats: While the proposed stochastic CVP analysis uses specific data items and formats, requiring that all the inputs be in the appropriate format may make the analysis a tedious process. The decision maker should not, for instance, be required to provide the four moments of product contributions. Rather equivalent forms of information from which data required for the analysis can be derived should be allowed in input and output operations. As an example, the decision maker should be allowed to specify the stochastic characteristics of product contributions in any of the following forms: (a) frequency distribution, (b) triangular distribution (optimistic – most likely – pessimistic), (c) values at any three percentiles (e.g. 15%, 50%, 90%), (d) four moments, and (e) functional form. The data can be based on the DM's judgments and/or historical data. Specialized cases of products having deterministic contributions should be automatically handled. Such a flexibility will facilitate enhanced acceptance and usage of the proposed approach. A DSS is ideally suited for providing such flexibility [10].

![](/api/attachments/GY6FZA95/fulltext/images/c32a2c966c5b0c4ad16980b56301ee8e9c2e9da3e1bd3596703c61135d88371b.jpg)  
Fig. 2. Data flow diagram for DSS.

Comprehensive reviews of decision support applications research [31,32] indicate that for complex decision modeling situations DSSs are useful. Such modeling situations include diverse topics such as computer integrated manufacturing [22] and career planning decisions [17].

## 5. Decision support system

In this section various steps involved in the decision process are discussed. An overview of the components of the DSS is presented.

## 5.1. Decision process

An outline of the various steps involved in the decision process is delineated in a data flow diagram in Fig. 2. This data flow diagram is drawn using the conventions of Gane and Sarson [37]. Processes are shown inside squares and data utilized are shown in rectangles with open ends on the right hand side. Regular lines show data flows, while dashed lines show control flows.

![](/api/attachments/GY6FZA95/fulltext/images/8ef40b698db5d62687f16586cbc8f72fca10fc1471060b861894fcd48ee7f129.jpg)  
Fig. 3. Components of the DSS.

First, the four moments of the product contributions are computed using available data on product contributions. Second, cross moments are computed using information on four moments and on product relationships. Third, a quadratic programming problem is formulated and solved using the stochastic characteristics of the contribution (i.e., moments and cross moments which enter into the objective function) subject to the resource constraints. If there are no feasible solutions, the decision maker is required to revise the problem formulation. In case of feasible solutions, a set of possible solution vectors on the efficient frontier is generated. Fourth, using the solution vectors and information on desired goals, best possible goal attainment levels are sought. In case the goals cannot be achieved, the decision maker is requested to revise the goals (i.e., reduce the aspiration levels). In case the goals are achievable but the decision maker is not satisfied with the attained levels (e.g., probability of success is too low), the decision maker can revise the goals until a satisfactory solution is achieved.

It should be noted that the data flow diagram in Fig. 2 is a high level diagram showing a bird's-eye view of the entire process. For instance, the data store labeled 'Product contributions' (shown in the top left corner) may contain information on the stochastic characteristics of the contributions in various types ranging from historical cost accounting data to a functional form of the contribution. Similarly the process labeled 'Compute four moments' can invoke several models to compute the four moments of contributions given different types of contribution data. Additional details on the data stores and the data processes will be presented in the next three sections. Various steps in the problem formulation and the problem solving phases are illustrated later on with a sample interactive DSS session.

## 5.2. Components of the DSS

The components of a decision support system for implementing the above approach is presented in Fig. 3. The various components in data base, model base and dialog interface subsystems interact with each other. The model base has four models, which deal with (a) derivation of moments of product contributions, (b) derivation of cross moments from product relationship information, (c) quadratic programming, and (d) seeking to satisfy decision maker goals. The database subsystem stores several types of basic and derived data. The dialog interface subsystem has three subsystems: (a) command processor, (b) results processor, and (c) database processor dealing with data input and output.

## 6. Model base

Previous work in stochastic programming has assumed correct input data and the proper delivery of the output to the user. Preoccupation with a single-model structure can inhibit the adoption of the stochastic CVP approach by decision makers. Models must be embedded in a decision support system with the data base functioning as the integration and communication mechanism between them [72]. To facilitate the discussion of the various models, a summary of the various steps involved in the analysis is presented first.

## 6.1. Summary of various steps in the analysis

1. Obtain the following data from the decision maker and other sources: (a) product contribution data, (b) product relationship data, (c) resource constraints data, and (d) desired goal levels.

2. Compute the four moments of product contributions, as necessary.

3. Compute the cross moments of related products.

4. Formulate quadratic programming problem.

5. Solve quadratic programming problem. If infeasible, go back to step 1 for reformulating the problem.

6. Generate solution vectors on efficient frontier.

7. Compute best attainable goal levels in comparison with desired goal levels.

8. If attained goal levels satisfy the decision maker, STOP. If not, modify problem formulation or revise goal levels as indicated by decision maker, until decision maker is satisfied.

## 6.2. Models for deriving four moments

The various steps involved in deriving four moments of the product contribution are depicted in Fig. 4. The four moments of each product's contribution can be obtained either from historical data or from the decision-maker's intuitive judgments about the behavior of the primary variable. Historical data may be in any form residing in the data base which is being continually updated. In case the DM is only able to specify the modal values and tail-end values (for example at probability levels of 0.05, 0.55 and 0.95), then through an interaction with the model base, Schmeiser-Deutsch (S-D) Distribution [67] can be fitted to the stochastic characteristics. Four moments can be obtained from the S-D Distribution and stored in the data base.

The DM can specify the density function of the contribution of various products. This will automatically define the primary variable, mean and all the central moments. The DM may also specify the first four moments of a primary variable.

![](/api/attachments/GY6FZA95/fulltext/images/3061b98822737c355a2b64f4068cd32eee6023c75b850aa11c154b42ea0232af.jpg)  
Fig. 4. Deriving four moments of the product contributions.

The DM must be aware of the situations wherein the third moment does not efficiently represent skewness [49] and wherein the fourth moment does not sufficiently represent kurtosis [64]. Information in the form of explanatory 'HELP' paragraphs of these situations is available in the DSS. It must, however, be pointed out that these exceptions occur rarely in the real world and, hence, do not possess much significance in our context.

## 6.3. Model for quadratic programming

It is desirable that the quadratic programming (QP) algorithm used in the model base be able to handle iterative applications. From among the various QP algorithms, the algorithm of Goldfarb and Idani [41] was chosen. Their algorithm uses ‘active constraint set’ approach in a dual problem framework. It has been found to be superior to many of the existing successive quadratic programming codes and has performed well in degenerate and ill-framed problems [41]. It is thus suitable for solving the quadratic programming problem (QPP) in an iterative fashion in the broader parametric QPP problem in Equation 9. The model tries to find out many points to describe the efficient frontier. The number of points to be sampled along the efficient frontier may be specified by the decision-maker in the beginning. The parametric QPP obtains solutions at various values of $\beta$ . It seeks to achieve more changes in the basis solution. In case no feasible solutions are possible with the current constraint set, the decision maker is requested to revise the existing problem formulation. One possible course of action for the decision maker is to relax the resource constraints, which might be accomplished by expanding available resources.

![](/api/attachments/GY6FZA95/fulltext/images/b4d00b86f0397714fdc2acdb4980321c7600c504d08bc37bceb547933858d8bf.jpg)  
Fig. 5. Data flow diagram for computing goal attainment levels.

## 6.4. Models for goal seeking

There are three inbuilt models which evaluate a particular product mix in the light of the three goals (discussed earlier) given the probability levels of breakeven and of profit preferred by the DM. The results can be ranked or presented in descending order to the DM, who will then decide upon the final mix.

While evaluating the final results, the DM may desire that the outputs be presented in various ways. The various steps involved in providing desirable formats for goal levels are delineated in Fig. 5. The DM may want probabilistic information at fixed distribution intervals (e.g., 0.50, 0.75, 0.90, and 0.95) or at arbitrary distribution intervals (e.g., 0.21, 0.62). On the other hand, the DM may feel that the probabilistic results will be meaningful only when considered in terms of inequalities given the uncertain environment. The probability distribution function fitted and the final results, hence, may vary. Different models for dealing with various requirements are presented next.

1. Information at fixed intervals: In case the decision-maker desires probability levels only at fixed intervals, which is most likely, then Bowman and

Shenton's tables [11,12] are utilized to find the different fractiles of the distribution.

2. Information on non-fixed intervals: In case the decision-maker desires information at certain intervals which are not fixed (like 0.62 probability of success), then a versatile distribution is fitted by using the four moments. There are two alternatives here:

(a) Pearsonian Distribution: Here a Pearsonian distribution is fitted and then the percentage points are ascertained. This involves a certain amount of computational work. A separate model will perform this function.

(b) S.D Distribution: S-D Distribution [67] is fitted using the four moments. This involves a nonlinear minimization problem, but existence of an efficient algorithm for solving this special problem structure makes this computationally more attractive compared to the Pearsonian curve fitting. The fractile levels can be ascertained by a closed-form formula involving a single exponentiation operation as compared to the operations involving multiple exponentiation and gamma function evaluations in the Pearsonian curve fitting model.

The decision maker is provided information on the ‘closeness of fit of the fitted distribution’ (using S-D or Pearsonian distributions) to the four moments. Sometimes it is possible that one of the above distribution-fitting procedures may fail, though such occurrences will be very rare in the practical world. In such a circumstance the other distribution can be used to fit the distribution function to the objective variable (total contribution). Although S-D Distribution is a newcomer, it is computationally more attractive than Pearsonian Distribution. But Pearsonian Distribution enjoys the advantage of successful applications in empirical curve fitting in the real world. In the DSS, S-D distribution is the default choice and is hence used first before Pearsonian Distribution. However, the decision-maker is given the flexibility of changing the default to Pearsonian Distribution.

3. Inequality information: In case the decision maker deems probabilistic information in the form of inequalities to be appropriate, then Gauss-Camp-Meidall (GCM) Inequality [40] is used to determine the probability estimates. The GCM inequality is a generalization of Tchebycheff's

Inequality. The GCM Inequality has several functional forms, one of which is

$$
P (| X - \mu | > \lambda \sigma) \leq \frac {4 (1 + s ^ {2})}{9 (\lambda - s) ^ {2}} \text { if } \lambda > s, \quad \text { where }\tag{34}
$$

$$
s = | \mu - \mu_ {0} | / \sigma\tag{35}
$$

The modal point $\mu_{0}$ can be determined thus:

$$
\mu_ {0} = \mu - \frac {\sigma \sqrt {\beta_ {1}} (\beta_ {2} + 3)}{2 (5 \beta_ {2} - 6 \beta_ {2} - 9)}, \quad \text { where }\tag{36}
$$

$$
\beta_ {1} = \frac {\mu_ {3} ^ {2}}{\mu_ {2} ^ {3}}, \beta_ {2} = \frac {\mu_ {4}}{\mu_ {2} ^ {2}}\tag{37}
$$

## 7. Data base

The data for the product mix programming problem are provided by the decision maker. However, in case the data provided by the DM needs to be converted to some other form before the goals of the DM can be sought, the inputs are converted and stored in the data base. The database thus keeps track of (a) data directly provided by the DM, and (b) data derived from base data which are needed for computations, both of which can be used by the different models in the model base. Models also store intermediate results in the database, which are retrieved by other models when needed. Information on product contributions, product relationships, constraints and goals are generally elicited from the decision maker. Moments and cross moments of the contributions, efficient frontier, solutions, and results from 'what if' queries are usually computed by different models and stored in the database. Use of the database promotes the modularity of the various models and promotes data independence in the DSS. Thus new models and changes in database can easily be incorporated in the DSS.

## 8. Dialog interface

The dialog interface subsystem has three subsystems: (a) command processor, (b) results processor, and (c) database processor (dealing with data input and output). The command processor responds to various commands from the user. It invokes the various modules of the DSS, which in turn employs multiple models and data sources. There are six modules in the DSS, namely (a) tutorial, (b) constraints, (c) solutions, (d) products, (e) goals, and (f) output. The user can enter and exit various modules during the analysis. The commands are English-like in nature e.g., display, delete, save, what if, help, add, modify, solve, quit, enter. Given the narrow domain of analysis, many commands can be parsed through word-matches. Context sensitivity is also used in the processing of commands. For instance, add command denotes the addition of a new goal in the goals module and the addition of a new product in the products module. The DM can use extra qualifiers to declare more specific intentions, e.g., display constraints. Some redundancy is built into the system to provide the DM with flexibility in interacting with the DSS. For instance, the solve command can be used to view the solution(s) in modules other than the solution module.

The results processor conveys messages from different modules (e.g., too ambitious goals). The database processor acts as a front-end to the database. It stores information in the database, retrieves current information from database (e.g., information on other products in the database, while adding a new product), and keeps the user informed about the new updates made by the models in the model base as necessary.

The dialog subsystem specifically provides flexibility in the following areas to select various choices available to the decision-maker.

\- Specifying stochastic characteristics of the contribution through historical data adjusted for future charges along with any subjective estimates for new products.

\- Flexibility in selecting the form of constraints and the nature of constraints. The user can view the existing constraints easily.

\- Flexibility in specifying the generation of efficient frontier and the capability to graphically portray the efficient frontier to the decision-maker.

\- Providing an idea of the fitted distribution through graphical display of both primary and objective variables. If the DM thinks that the fitted distribution is inappropriate the inputs can be changed.

\- Providing an idea of the goodness of fit of the final objective variables.

\- Flexibility in providing probabilistic information at fixed intervals or at nonfixed intervals and inequality information.

\- Ability to handle ‘what if’ questions.

\- Displaying the final information in a side by side fashion for three ‘safety-first criterion based’ goals so that the DM can choose the optimal combination according to the needs. For a given level of fixed costs and target profits, the feasibility of desired break-even probabilities and desired target profit probabilities are displayed. Also maximum target profit level for a given target profit probability level is presented.

\- The ability to inform the DM of the infeasible aspiration levels. If the desired probabilities are, for example, too high to be realized given the stochastic characteristics of the contribution margins, the dialog system indicates that the goal levels specified in terms of $(\alpha_0, \alpha_1)$ , $(\Pi_T, \Pi_m)$ are too ambitious and requests the DM to scale down the desired goal levels.

## 9. Illustration of the DSS

A prototype of the above DSS framework has been implemented on an Amadhal V6 mainframe under the IBM CMS operating system. The core of the DSS uses a set of FORTRAN and PASCAL subroutines and library functions.

A transcript of a session with the DSS is shown in the Appendix. A sample problem is solved by using the DSS in this session. The problems involves four products, two of which are interdependent. In this session, the DM examines the existing information in the database, adds a new product, modifies constraints and previously specified goals, takes a look at the solution, poses some ‘what if’ questions, adds a new goal, finds the impact of the goal on the solution, and is satisfied with the solution.

## 10. Conclusion

A framework for providing decision support for cost-volume-profit analysis under an uncertain environment is presented in this paper. Existing stochastic product mix programming problem formulation is extended using four moments of the product contributions to take into account potential dependency relationships between products. Models which are suitable for flexible formulation and solution of the decision problem are selected from existing literature. The need to accommodate various types of input data is illustrated. The database as a depository for both (a) input from the DM and (b) intermediate computational results promotes the modularity of the model base and data independence.

Validity of the DSS is an important issue. Validation is critical in expert system (ES) implementations since heuristics and rules in ES knowledge bases need to be verified. In a DSS, models embedded in the model base are normative models which have been analytically derived using certain assumptions and thus the DSS model base need not be validated. Validity in a DSS may be viewed in two contexts: (a) formulated model and (b) generated solutions. We need to ensure that the DSS is providing the kind of support for which it was designed. The system under consideration is designed to support stochastic CVP programming problems. Different models are provided to support a flexible problem formulation by the DM. No restrictive assumptions are forced upon the user. This will ensure that appropriate models are employed to arrive at a valid problem formulation. Another important factor in valid formulation is the ease with which appropriate models can be selected, since it can affect the actual model formulation process by the decision maker. The DM should not be forced to go through elaborate steps to select the right model. Provision of easy-to-use interface with English-like commands supports the DM. A tutorial module further helps the DM in learning to use the DSS. Another key factor in promoting the validity of the DSS is the provision of feedback to the DM which makes sure the results from the analysis reflect the reality as close as possible. By using well-known models the validity of solutions is enhanced. For instance, choosing the quadratic programming code from Goldfarb and Idani [41] which performs well in degenerate and ill-framed problems provides the best kind of support for semi-structured problems such as the CVP analysis problem at hand. Valid ity of the DSS is a necessary but not sufficient requirement for successful adoption and usage. Successful DSS adoption and usage are influenced by other organizational factors [3,23,36, 38,53,72,76]. Such factors need to be explored in the context of CVP analysis in the future by researchers in this area.

```txt
TUTORIAL CONSTRAINTS SOLUTIONS
PRODUCTS GOALS OUTPUT

The following commands are available to you for working in all the modules except in TUTORIAL module.

DISPLAY DELETE SAVE WHAT IF HELP ADD MODIFY SOLVE QUIT ENTER

Enter your commands on the command line (indicated by the `===>' prompt on the screen). Now enter your command.

The DM now enters the PRODUCTS module and takes a look at the product information existing in the database.

==> ENTER PRODUCTS
==> DISPLAY ALL

The products currently active in the system are 3.
Their characteristics follow.

Product Name : X1

Distribution of Contribution

Expected Value: 49.5 Moments about mean
Variation : 1.68 Second :
2.83
Skew : 0.71 Third :
3.38
Peakedness : 3.78 Fourth :
30.3

Influences Product(s): X2
Influenced by Product(s): None
Relation(s): X2 = A + 2 X1 + Error (relation number: 1)

Product name : X2

Distribution of Contribution

Expected Value: 4.0 Moments about mean
Variation : Second:
```

By providing the DM with flexible modeling capabilities, feedback mechanisms, and easy to use interfaces, we can enhance the acceptance and usage of complex decision models $[72]$ . The flexible, interactive approach is needed to improve the quality of the decisions made by the DMs who confront ever-increasing complexities and competitive pressures.

## Appendix: A sample DSS session

In this sample session, a problem involving four products, two of which are interrelated is formulated and solved by the DM. The DSS can be operated by English-like commands. Different options are provided to the DM and 'HELP' information is available. The numbers used are in units known to the DM or predefined by the DM, e.g., thousands of dollars. The following transcript is annotated with comments to improve the readability. Terminal input and output are displayed in 'this font', while the comments are shown in 'this regular text font'. Lines which start with the prompt symbol ‘===>’ show the inputs from the DM.

Initially some information on modules and commands is given briefly. There are six modules in the DSS including a TUTORIAL module. Some redundancy has been built into the system to provide the DM with flexibility in interacting with DSS. For example, the SOLVE command can be used to view the solution(s) in modules other than the SOLUTION module.

## Product Mix Decision Support System

The following modules are available under this system. You can enter modules and quit modules to operate on the various aspects of decision problem faced by you. The current module in which you are in will be displayed at the right hand top side of the screen.

```txt
Relation to other products
```

```txt
Influences Product(s): None
Influenced by Product(s): X1
Relation(s): X2 = A + 2 X1 + Error (relation number: 1)
```

```txt
Skew Third : Third :
Peakedness : Fourth:
```

```txt
Relation to other products: NONE
```

The DM examines the nature of dependence relation between products X1 and X2.

```txt
==> DISPLAY RELATION 1
Relation : X2 = A + 2 X1 + Error (relation number: 1)
The above relation can be described as follows
Nature of relation : Linear Regression
Error term nature : Homoscedasticity
Mean Square Error : 1.0
```

The DM starts adding a new product X4 to the DSS. Out of five input options for describing X4's contribution, the DM selects the percentile option, and supplies the subjective estimates.

```txt
===> ADD
Enter the name of the new product:
===> X4
```

You are now adding Product X4 to the existing product(s).

You can now give details about the distribution of the new product's contribution. You have the following options in giving the necessary details.

```txt
1. Frequency Distribution
2. Optimistic - most likely - pes - simistic
3. Values at three percentiles (e.g. 15%, 50%, 90%)
4. Four moments
5. Functional form
```

(For more information on the above options type 'HELP DISTRIBUTION INPUTS')

```txt
Now choose your option by entering number or obtain help on options.
```

```txt
===>3
```

You have chosen to describe the new product X4 by three percentile values the middle of which is the modal value of the contribution. Enter the low percentage point and value separated by blank(s):

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$= = = &gt; 5 34$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$= = = &gt; 40 37$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$= = = &gt; 85 42$
</div>

The DSS fits a S-D distribution to the percentile values provided, derives four moments of X4's contribution and asks the DM if she wishes to see a 'fitted curve' or the 'four moments' of the contribution. But the DM declines.

```txt
Goal Description FEASIBLE?
1 Desired Break-
even Probability : 90% YES
2 Desired Target
Profit Probability : 75% YES

===> WHAT IF

Enter desired goal number and new value separated by blank(s):
===> 2 85

Goal Description FEASIBLE?
2 Desired Target
Profit Probability : 85% YES
```

```txt
Now product 4 has been added to the products file.
Do you wish to see a fitted curve of the distribution or four moments of the distribution of the contribution as deduced from your inputs?
Answer 'YES' or 'NO'.
===> NO
Do you think that this product is related to other product(s) already in the system? Answer 'YES' or 'NO'.
===> NO
===> SAVE
===> QUIT
```

The DM enters the CONSTRAINTS module and enters a new set of constraints using the 'equalities/inequalities' option.

```perl
==> ENTER CONSTRAINTS
==> DELETE ALL
==> ADD ALL

You can enter your constraints using following options:

1. Mathematical equality / inequality form(s)
2. Constraints in the descriptive form(s)

(For more information on the above options type 'HELP INEQUALITIES INPUTS')

Now choose your option by entering number or obtain help on options.

==> 1
==> 5X1+8X2+12X3+6X4 <= 1721
==> 12X1+0.8X2+2.1X3+1X4 >= 255
==> 5X1+ X2+2X2+2X4=366
==> 40X1+20X2+10X3+50X4=6680
==> SAVE
==> QUIT
```

The DM invokes the GOALS module, takes a look at the goal parameters already defined in the DSS, and modifies one goal level.

```perl
==> ENTER GOALS
==> DISPLAY BRIEFLY

Goal Parameters Description
1 Fixed Costs : 5000
2 Target Profit : 700
3 Desired Break-
even Probability : 90%
4 Desired Target
Profit Probability : 60%

==> MODIFY

Enter desired goal number and new value separated by blank(s):

==> 4 75
==> SAVE
==> QUIT
```

The DM next invokes the SOLUTIONS module, examines the attainability of goals and poses a 'what if' question.

The DM now adds one more goal and examines the resulting solution. Satisfied with the results, the DM notes down the production volume and ends the interactive session.

===> ADD
You can add one more goal
3 Maximum Target Profit for a given target profit probability level: (VALUE)
Enter your probability level (%)
===> 75

3 Maximum Target Profit for a given target profit probability level 75 %: (VALUE) 840

## ===> DISPLAY PRODUCT VOLUMES

## Product Name Volume (in units)

===> BYE

Hope you enjoyed this session and found it useful!

## References

[1] Z. Adar, A. Barnea, and B. Lev. A comprehensive cost-volume-profit analysis under uncertainty. Accounting Review, 52:137–149, 1977.

[2] R.J. Aldag and D.J. Power. An empirical assessment of computer-assisted decision analysis. Decision Sciences, 17:572–588, Fall 1986.

[3] S.L. Alter. Decision Support Systems: Current Practice and Continuing Challenges. Addison-Wesley, Reading, Massachusetts, 1980.

[4] F.D. Arditti. Risk and required rate of return. The Journal of Finance, 22:19–36, 1967.

[5] S.G. Badrinath and S. Chatterjee. On measuring skewness and elongation in common stock return distributions: the case of the market index. Journal of Business, 61(4):451–472, Oct. 1988.

[6] C.B. Barry, J.I. Velez-Arocho, and P.R. Welch. A Bayesian approach to CVP analysis under parameter uncertainty. Quarterly Review of Economics and Business, 24(2):71–90, Summer 1984.

[7] B.M. Bass. Organizational Decision Making. Richard D. Irwin, Inc., Homewood, Illinois, 1983.

[8] I. Benbasat and A.S. Dexter. Individual differences in the use of decision support aids. Journal of Accounting Research., 20:1–11, Spring 1982.

[9] I. Benbasat and R.G. Schroeder. An experimental investigation of some MIS design variables. MIS Quarterly, 1:37–50, March 1977.

[10] R.H. Bonczek, C.W. Holsapple, and A.B. Whinston. Foundations of Decision Support Systems. Academic Press, New York, 1981.

[11] K.O. Bowman and L.R. Shenton. Approximate percentage points for Pearson distributions. Biometrika, 66:147-52, 1979.

[12] K.O. Bowman and L.R. Shenton. Further approximate Pearson percentage points and Cornish-Fisher. Communications in Statistics, 88:147–152, 1978.

[13] P.L. Brockett, A. Charnes, W.H. Cooper, and H.C. Shin. Cost-volume-utility analysis with partial stochastic information. Quarterly Review of Economics and Business, 27(3):70–90, Autumn 1987.

[14] P.L. Brockett, A Charnes, W.W. Cooper, and H.C. Shin. A chance constrained programming approach to cost-volume-profit analysis. Accounting Review, 59(3):474-487, July 1984.

[15] R. Cantrell and L.P. Ramsay. Some statistical issues in the estimation of a simple cost-volume-profit model. Decision Sciences, 15(4):507–521, Fall 1984.

[16] R.L. Carraway. A dynamic programming approach to stochastic assembly line balancing. Management Science, 35:459–472, April 1989.

[17] W.I.. Cats-Baril and G.P. Huber. Decision support systems for ill-structured problems: an empirical study. Decision Sciences, 18:350–372, Summer 1987.

[18] D. Chakravarti, A.A. Mitchell, and R. Staelin. Judgment-based marketing decision models: an experimental investigation of the decision calculus approach. Management Science, 25:251–262, March 1979.

[19] J.T. Chen. Cost volume profit analysis in stochastic programming models. Decision Sciences, 11:632-647, 1980.

[20] T.E. Conine and M. Tamarkin. Implications of skewness in returns for utilities' cost of equity capital. Financial Management, 14(4):66–71, Winter 1985.

[21] G.M. Constantinides, Y. Ijiri, and R.A. Leitch. Stochastic cost-volume-profit analysis with a linear demand function. Decision Sciences, 12:417–427, 1981.

[22] S. De, S.Y. Nof, and A.B. Whinston. Decision support in computer integrated manufacturing. Decision Support Systems, 1(1):37–55, 1985.

[23] N.J. Dean. The computer comes of age. Harvard Business Review, 46:83–91, January–February 1968.

[24] N. Dickmeyer. Measuring the effects of a university planning decision aid. Management Science, 29:637–385, June 1983.

[25] G.W. Dickson, J.A. Senn, and N.L. Chervany. Research in management information systems: the Minnesota experiments. Management Science, 29:913–923, May 1983.

[26] B.L. Dos Santos and M.L. Bariff. A study of user interface aids for decision support systems. Management Science, 34, April 1988.

[27] N. Eckel and R.V. Hartley. Linear dependence in stochastic CVP analysis. The Mid-Atlantic Journal of Business, 23(1):45–53, Winter 1984/1985.

[28] N.L. Eckel. The impact of probabilistic information on decision behavior and performance in an experimental game. Decision Sciences, 14:483–502, Fall 1983.

[29] F. Edelman. Managers, computer systems and productivity. MIS Quarterly, 5:1–19, September 1981.

[30] S. Eilon and T.R. Fowkes. Sampling procedures for risk simulation. Operational Research Quarterly, 24:241–251, 1973.

[31] J.J. Elam, G.P. Huber, and M.E. Hurt. An examination of the DSS literature (1975–1985). In E.R. McLean and H.G. Sol, editors, Decision Support Systems: A Decade in Perspective, pages 1–16, Elsevier Science Publishers, New York, 1986.

[32] H.B. Eom and Sang M. Lee. Decision support systems applications research: a bibliography (1971–1988). European Journal of Operational Research, 46:333–342, 1990.

[33] R.L. Ferguson and O.H. Jones. A computer aided decision system. Management Science, 15:B550–561, June 1969.

[34] D.R. Finley and W.M. Liao. A general decision model for cost-volume-profit analysis under uncertainty: a comment. The Accounting Review, 56(2):400–403, Apr. 1981.

[35] W.K. Fudge and L.M. Lodish. Evaluation of the effectiveness of a salesman's planning system by field experimentation. Interfaces, 8, November 1977.

[36] C.A. Gallagher. Perceptions of a value of a MIS. Academy of Management Journal, 17:46–65, 1974.

[37] C. Gane and T. Sarson. Structured Systems Analysis: Tools and Techniques. McAuto, A division of McDonnell Douglas, Box 516, Saint Louis, Missouri, 63166, 1977.

[38] J. Garrity. Top management and computer profits. Harvard Business Review, 41:172–174, 206, July–August 1963.

[39] J.E. Gochenouer. An empirical study of the impact of a decision support language on knowledge workers. 1985. Unpublished doctoral dissertation.

[40] H.J. Godwin. On generalization of Tchebycheff's Inequality. Journal of American Statistical Association, 50:923–945, 1955.

[41] D. Goldfarb and A. Idnani. A numerically stable dual method for solving strictly convex quadratic programs. Mathematical Programming, 27:1-33, 1983.

[42] M.D. Goslar, G.I. Green, and T.H. Hughes. Decision support systems: an empirical assessment for decision making. Decision Sciences, 79–91, Winter 1986.

[43] J.E. Hilliard and R.A. Leitch. CVP analysis under uncertainty: a log normal approach. Accounting Review, 50:69–80, 1975.

[44] E. Horwitt. DSS: effective relief for frustrated management. Business Computer Systems, 44–59, July 1984.

[45] B.E. Ismail and J.G. Louderbeck. Optimizing and satisficing in stochastic cost-volume-profit-analysis. Decision Sciences, 10:205–217, 1979.

[46] R.K. Jaedicke and A.A. Robicheck. Cost-volume-profit analysis under conditions of uncertainty. Accounting Review, 39:917–926, 1964.

[47] J.E. Jarrett. Approach to cost-volume-profit analysis under uncertainty. Decision Sciences, 405–420, 1973.

[48] R. Joyner and K. Tunstall. Computer augmented organizational problem solving. Management Science, 17: B212–B225, February 1970.

[49] I. Kaplansky. A common error concerning kurtosis. Journal of American Statistical Association, 40:259, 1945.

[50] A. Karnani. Stochastic cost-volume-profit analysis in a competitive oligopoly. Decision Sciences, 14:187–193, 1983.

[51] S. Kataoka. A stochastic programming model. Econometrica, 31:181–196, 1963.

[52] P.G.W. Keen. Value analysis: justifying decision support systems. MIS Quarterly, 5:1–15, March 1981.

[53] P.G.W. Keen and S. Morton. Decision Support Systems: An Organizational Perspective. Addison-Wesley, Reading, Massachusetts, 1978.

[54] M.G. Kendall and A. Stuart. The Advanced Theory of Statistics. Volume I, Charles Griffin and Company, London, 1969.

[55] W.R. King and J.I. Rodriguez. Evaluating management information systems. MIS Quarterly, 2:43–51, September 1978.

[56] J.F. Kottas and H.S. Lau. A four-moments alternative to simulation for a class of stochastic management models. Management Science, 28:749–758, 1982.

[57] J.F. Kottas and H.S. Lau. Stochastic breakeven analysis. Journal of Operational Research Society, 29:251–257, 1978.

[58] J. Kriens, J.T. Vanliesh, J. Roemen, and P. Verheyen. Management accounting and operational research-review. European Journal of Operational Research, 13(4):339-352, 1983.

[59] H. Levy and M. Sarnat. Investment and Portfolio Analysis. John Wiley, New York, 1972.

[60] M. Liao. Model sampling: a stochastic CVP analysis. Accounting Review, 50:780–790, 1975.

[61] D.V. Lindely. Using expert advice on a skew judgmental distribution. Operations Research, 35(5):716–721, Sep-Oct. 1987.

[62] H.M. Markowitz. Portfolio Selection: Efficient Diversification of Investments. John Wiley and Sons, Inc., New York, 1959.

[63] S. McIntyre. An experimental study of the impact of judgment-based marketing models. Management Science, 28:17–23, January 1982.

[64] J.K. Ord. The discrete Student's t distribution. Annals of Mathematical Statistics, 39:1513-1516, 1968.

[65] S.J. Pretorius. Skew bivariate frequency surfaces, examined in the light of numerical illustrations. Biometrika, 50(22):109–223, 1930/31.

[66] H.L. Rietz. Mathematical Statistics. Mathematical Association of America, 1927.

[67] B.W. Schmeiser and S.J. Deutsch. A versatile four parameter family of probability distributions suitable for simulation. AIIE Transactions, 170–181, 1977.

[68] R.S. Sears and K.C.J. Wei. The structure of skewness preferences in asset pricing models with higher moments: an empirical test. Financial Review, 23(1):25–38, Feb. 1988.

[69] R. Sharda, S.H. Barr, and J.C. McDonnell. Decision support system effectiveness: a review and empirical test. Management Science, 34(2):139–159, 1988.

[70] Wei Shih. A general decision model for cost-volume-profit analysis under uncertainty. The Accounting Review, 687–706, Oct. 1979.

[71] H.A. Simon. The New Science of Management Decision. Prentice-Hall, Inc., Englewood Cliffs, N.J., 1977.

[72] R.H. Sprague and E.D. Carlson. Building Effective Decision Support Systems. Prentice-Hall, Inc., New Jersey, 1982.

[73] M.K. Starr and C.S. Tapiero. Linear breakeven analysis under risk. Operational Research Quarterly, 26:847–856, 1975.

[74] L.G. Telser. Safety first and hedging. The Review of Economic Studies, 23:1–16, 1955.

[75] J. Tobin. Liquidity preference as behavior toward risk. The Review of Economic Studies, 25:65–86, 1958.

[76] G.R. Wagner. Realizing DSS benefits with the IFPS planning language. January 1980. Paper presented at the Hawaii International Conference on System Science.

[77] J.A. Yunker and P.J. Yunker. Cost-volume-profit analysis under uncertainty: an integration of economic and accounting concepts. Journal of Business and Economics, 34:21–30, 1982.
