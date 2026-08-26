---
otero_id: 17352
otero_key: "X5ZSZBB6"
title: "Supporting preference elicitation"
authors: "Thomas Kämpke; Franz Josef Radermacher; Peter Wolf"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90048-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting preference elicitation The FAW preference elicitation tool \*

Thomas Kämpfe,
Franz Josef Radermacher
and Peter Wolf

University of Ulm, Ulm, Germany

The integration of decision analysis and expert system technology has not yet been sufficiently accomplished. For instance, knowledge-based systems often lack sophisticated abilities with respect to explicitly formulating needs of users, e.g. preference modelling. The approach presented has a broad range of applications but is aimed particularly at those in which the user's objective is not easily identified. Applications for machine scheduling and environmental risk assessment are outlined. We describe how identifying and continuously updating user preferences can be formally established.

Keywords: Linear programming, Human-machine interaction, Multi criteria decision making, User-modelling.

## 1. Introduction

Facilitating and guiding decision making is a potential often requested for knowledge-based systems. However, the (decision-theoretical) basis and framework for this target is often quite poor. In particular, almost no effort has been made to systematically elicit preference structures over different objectives from users as part of human-machine interaction. Thus, incorporation of the specific interests of a particular user is often possible only via user rejection of system proposals.

The aim is to model the user's decision problem, using the normatively sound framework of multi-attribute decision theory. The applications intended are problems for which the solution spaces to be screened are too large to be ex-

![](/api/attachments/X5ZSZBB6/fulltext/images/daba9a76dd1671d20f092ee014ef1dc37cdbe71667fc2461e6790bf059c84fe7.jpg)

Thomas Kämpfe is on the staff of the Forschungsinstitut für anwendungsorientierte Wissensverarbeitung (FAW) at the University of Ulm, Germany. He held positions at the Technical University of Aachen and at the University of Passau, both Germany, and visited the University of California, Berkeley, CA. His research interests include mathematical optimization, stochastic modelling, scheduling, algorithms for computer science, and decision analysis. He is currently involved in the development of an environmental information system with special emphasis on risk assessment.

![](/api/attachments/X5ZSZBB6/fulltext/images/4140611e89305ae6822c418db6973ac93af79baa643d36a0bcb56694784904bc.jpg)

dermacher holds Doctorates in Mathematics from the Technical University of Aachen and in Economics from the University of Karlsruhe. 1987–1991 he was President of the Society for Mathematics, Economics and Operations Research (GMOOR) and 1990 he was chairman of the Council of the German Research Institutes for Artificial Intelligence.

![](/api/attachments/X5ZSZBB6/fulltext/images/54eb269fb7a4440a0db554a8b034977cc4478adbae60cce4900ab0b2e47110e9.jpg)

Peter Wolf is on the staff of the FAW Ulm. He received his Diploma degree in Applied Mathematics from the University of Ulm and his Master's degree in Mathematics from Syracuse University, New York. His research interests include decision theory, optimization, object oriented technology and software engineering. He recently finished his Ph.D. at FAW Ulm on the topic of decision theory.

explicitly examined. In many of these cases, the objective of the user is not known and difficult to obtain. However, only a partial and hopefully rather complete knowledge about the objective will allow a system to concentrate its search processes on areas in the solution domain where solutions generally have high user preference.

The present paper focuses on a declarative representation of knowledge under the assumption of attributes and scales being precoded by or established together with domain experts. We try to mimic a decision analyst who intends to assess the user's preference function. Knowledge about how to do this is the basis of the system's process. Applications in the fields of machine scheduling and environmental risk assessment are given. Further work on the connection with uncertainty handling in expert systems is performed at the FAW and will be addressed elsewhere.

## 2. Artificial intelligence versus decision analysis

The ability to make consistent decisions given imprecise information within a changing environment is a basic human ability which is not completely appreciated as such by artificial intelligence. Current AI systems aim at supporting decision making, but this is usually done without any direct reference to any user preferences for certain goals. At best, preferences are addressed via constraints or local decision rules within search strategies.

On the other hand, decision analysis has dealt with the problem of decision making for the last 50 years, and this work has yielded deep scientific insight. Important work in this area was pioneered by von Neumann and Morgenstern [12] and even Cantor [1] and has close ties with utility theory and theories of psychological measurement. The basis of the decision-analysis approach to decision making is in the formulation of the proper framing of the problem. To create the proper frame, the relevant objectives (user aims) and the appropriate attributes must be identified. Attributes operationalize the degree to which objectives are satisfied by solutions. Solution alternatives have different values with regard to certain attributes, where tradeoffs (between Pareto optimal solutions) must be made explicit.

Based on this normatively sound theoretical background, decision analysts have been involved in major decision making all over the world, often in situations in which hundreds of millions of dollars were at stake. In such situations, typically only a small set of relevant alternatives were available, all of which had to be addressed completely and in detail. Note, however, that from an optimization point of view, optimal value functions that integrate the degree to which several goals are reached simultaneously fall naturally into this framework. Here, decision analysts are usually not involved. From the authors' point of view, this may be one reason why methods from applied mathematics and operations research have often failed to gain acceptance in practical applications. That is, optimization aims that were used (often because they offered good algorithms) did not really address the user's problem.

Given this background, this paper focuses on showing how objective functions, viewed as preference functions, can be elicited automatically and used effectively. Recent work in building expert systems for intricate applications $[2]$ has shown that the elicitation of user preferences can be prohibitively difficult and time-consuming, so that in certain cases the less powerful method of adding constraints and using, for example, an assumption-based truth maintenance system may be a reasonable alternative approach. Nevertheless, in the majority of cases, the most appropriate method will be (direct or indirect) preference elicitation. This results in our major thesis:

For decision making, preference modelling is as important as the modelling of the logical structure of the problem.

## 3. What are preferences good for?

Important application areas for which preference modelling is essential include scheduling, aiming, for instance, at early completion of several subtasks and the project as a whole; VLSI layout, where tradeoffs between goals such as packing density, length of wiring paths, and number of crossings over certain lines must be made, [11]; and factory production planning, where a number of aims like high throughput, early completion of certain important jobs, and the continuous use of available machinery must be balanced. For such problems the existence of (usually exponential) many solutions (schedules, layouts, strategies) is characteristic. Therefore, only a guided search that takes user aims into account offers a high likelihood for finding solutions that satisfy the user. The crucial task that is here very carefully to be addressed is defining the appropriate optimization aim, i.e. priority lists concerning objectives will generally not suffice. It is well known that many operations research projects have failed precisely because the optimization framework was poorly defined; instead, the problems were forced into a framework where an objective with good algorithmic tools was available. This kind of approach is futile.

At present, the typical situation envisioned is that domain experts and decision analysts together will tailor the elicitation tool to a particular application domain by setting up a large structured set of attributes and corresponding scales. Examples for what might be expected from future automatization in this direction can be obtained by looking into the use of tools such as HIVIEW [6] and TREEVAL [10]. An example of a good tool for representing standard preference functions is TREEVAL.

Suppose a system is in the process of solving some problem which has a variety of (feasible) solutions but an optimal solution – if there is any – has not been found. With respect to inference processes, an expert system always can generate not just one, but many solutions and can compare them globally using the preference function. After many solutions have been generated, the best is presented to the user who can compare this solution to others found earlier. The user may either accept or restart the whole process. If a new solution compares unsatisfactorily to one found earlier, the implication is that the user-preference function was not correctly chosen. He or she might also have modified the preference structure, thereby implicitly reviewing previous inputs. A local use of preference information would, of course, be even more valuable than the global comparison described. For example, one would like the global preference function to be of use for making better local decisions in search processes. This is, however, very unlikely in a general manner, as the NP-completeness of many problems is intuitively due to the impossibility of breaking a global problem efficiently down into local ones. For instance, given a partial solution, such as a partial schedule, a partial VLSI layout $[11]$ or a partial production plan, it is often unclear how this will turn out when globally extended. Also, an over-emphasis on a local greedy-type fulfillment of values will often mean that towards the end of some design, there is a sudden decrease in performance. Glover and Laguna $[4]$ address some of these problems and argue that in many applications local search decisions are essential for generating acceptable solutions. “Tabu search” and “target analysis” may be valuable instruments in this respect, in addition to other local decision rules such as a neighbourhood relation employed by simulated annealing. The precise degree to which the ideas presented here can be integrated into such frameworks has to be investigated in the future.

## 4. Mathematical approach

## 4.1. General considerations

The aim of the approach taken here is to find the “true” preference function of a particular decision maker. In decision theory literature (cf. [3]), different types of preference functions are discussed, mainly so-called value, measurable value and utility functions. A value function is an ordinal scale that rank orders alternatives whereas both measurable value and utility function are cardinal scales, i.e. differences have a specific interpretation. However, from a theoretical point of view, measurable value and utility functions are different concepts, whereas many decision analysts do not take the difference seriously in practice [5].

In order to assess a decision maker's preference function, different types of information given by him will be taken into account. This user information is classified into so-called “ordinal” and “cardinal” information. Ordinal information (e.g. ranks for alternatives) is unique up to isotone transformations and therefore can be represented by a value function. Cardinal information has the property that it needs to be represented either by a measurable value or by a utility function. This paper is mostly concerned with ordinal information which are e.g. holistic preferences or tradeoffs (details to this will be explained later).

The approach taken here is as follows: the preference function f of a particular decision maker is modelled as dependent on parameters which have to be found. Preference information from the user will be transformed into linear restrictions for the parameters of f. This paradigm is based on the so-called UTA-method by Jacquet-Lagrèze and Siskos [7]. However, differences to the UTA-method are made and many additional features are added.

Whenever preference information is given by the decision maker, one of the important tasks to be performed by a decision analyst, is to maintain consistency. Inconsistencies in decision making can be due to e.g. violations of transitivity, but also to not well defined parameters of the preference model. The first kind of inconsistency will be detected immediately in this approach. The second type leads to an empty restriction system and can be handled here, too. If the restriction system, in turn, is non-empty, it corresponds to the set of preference functions of a particular class that are consistent with all the information given by a decision maker so far. It is then possible to determine a particular function out of this set and to apply it. Interesting types of analysis, based on this set, can also be made, which yield further information on the decision maker's preference structure.

In this paper only additive preference models are treated whereby the one-dimensional components are approximated by piecewise linear functions. This, in turn, makes it possible to determine the scaling constants and the one-dimensional preference functions in parallel.

The approach can be applied to more general models also (e.g. the multilinear form) but then a proper parameter choice has to be done which may restrict the type of preference information usable. The approach can to some extent be employed in a group decision making context, too.

## 4.2. Choice of parameters

We start with n attributes $i=1,\ldots,n$ given and associated scales $X_{1},\ldots,X_{n}$ which are assumed to be finite intervals or finite sets. Thereby $X=X_{1}\times\ldots\times X_{n}$ denotes the n-dimensional consequence space, the attribute set $\{1,\ldots,n\}$ will be denoted by N. In the following we assume that the conditions for an additive value model have been verified and show how ordinal information can help to construct this function. The worst and best levels w.r.t. each attribute i are denoted by $W_{i}$ and $B_{i}$ , the worst and best conceivable consequences in X by $W=(W_{1},\ldots,W_{n})$ and $B=(B_{1},\ldots,B_{n})$ . The additive value function f can be modelled in the form

$$
f (x _ {1}, \dots , x _ {n}) = c _ {1} f _ {1} (x _ {1}) + \dots + c _ {n} f _ {n} (x _ {n}),\tag{1}
$$

where the functions $f_{i}(x_{i})$ for $i \in N$ are normalized by $f_{i}(W_{i}) = 0$ and $f_{i}(B_{i}) = 1$ , the function f by $f(W) = 0$ , $f(B) = 1$ and $(c_{1} + \ldots + c_{n}) = 1$ , $c_{i} > 0$ holds. An alternative representation of (1) is to use non-normalized functions $F_{i}(x_{i}) := c_{i} f_{i}(x_{i})$ such that

$$
f (x _ {1}, \dots , x _ {n}) = F _ {1} (x _ {1}) + \dots + F _ {n} (x _ {n}) \quad \text { with }\tag{2}
$$

$$
\begin{array}{l} F _ {i} (x _ {i}) = f (W _ {1}, \ldots , W _ {i - 1}, x _ {i}, W _ {i + 1}, \ldots , W _ {n}), \\ F _ {i} (B _ {i}) = c _ {i} f _ {i} (B _ {i}) = c _ {i}. \end{array}
$$

We take the latter form because it allows to neglect explicitly considering the scaling constants $c_{i}$ , which are the evaluations of the $F_{i}$ 's at their best levels. In order to approximate the conditional functions $F_{i}$ , a number of grid points $x_{i}^{j}, j=0,\ldots,m_{i}$ on the scale for each attribute $i\in N$ are chosen to define $F_{i}$ as a piecewise linear function whose shape closely resembles the real conditional function.

The number $m_{i}$ for $i=1,\ldots,n$ corresponds to the number of linear segments to approximate each conditional function $F_{i}$ . The set

$$
S _ {i} = \left(x _ {i} ^ {j}\right) _ {j = 0} ^ {m _ {i}}
$$

will be called the “grid” for attribute $i\ (S_{i} \subset X_{i})$ . It is assumed that the grid always contains the worst and best levels of each attribute. The use of small linear pieces allows to represent each value $F_{i}(x_{i}), x_{i} \in X_{i}$ by a linear combination of the support points $F_{i}(x_{i}^{j})$ and $F_{i}(x_{i}^{j+1})$ where $[x_{i}^{j}, x_{i}^{j+1}]$ is the interval that contains $x_{i}$ . Therefore $f(x)$ for $x \in X$ can be represented as a linear combination of at most 2n parameters. The values

$$
\theta_ {i} ^ {j} := F _ {i} \left(x _ {i} ^ {j}\right), \quad i = 1, \dots , n, j = 0, \dots , m _ {i}
$$

are the parameters of the model.

## 4.3. Transformation of ordinal information

Different ordinal information obtained from the decision maker will be translated into linear inequalities for these parameters, as described in the following. Since a linear programming approach will be used to determine the parameters, strict inequalities of the form $f(a) > f(b)$ for modelling “a is better than b” cannot be used as a restriction. Instead, a small threshold value $\delta > 0$ is introduced in order to avoid equal values for $f(a)$ and $f(b)$ when a strict inequality is wanted, and preference of a over b is expressed by $f(a) - f(b) \geq \delta (> 0)$ .

First we assume that $\delta$ has a lower bound $\delta^{min}$ (e.g. $\delta^{min}=0.01$ ), i.e. $\delta\geq\delta^{min}$ , is an additional restriction for the restriction system to be set up. An upper bound for $\delta$ can be deduced automatically which will be shown later. The use of such a lower bound makes sense, otherwise preferences between any two alternatives could have an arbitrary small difference in value which practically means that the alternatives considered are indifferent. The bound $\delta^{min}$ has to be determined in advance. Weak preferences ( $a\succ b$ ) and indifferences are transformed in the usual way, i.e.

$$
\begin{array}{l} a \succcurlyeq b \Leftrightarrow f (a) - f (b) \geq 0 \\ a \sim b \Leftrightarrow f (a) - f (b) = 0. \end{array}
$$

In the following it is shown how different types of ordinal information can be transformed into linear inequalities in the parameters $\theta_{i}^{j}$ and $\delta$ .

Monotonicity statements for all attributes $i \in N$ are necessary, otherwise the values $W_{i}$ and $B_{i}$ cannot be determined (cf. [9]). For example, if preferences in attribute i are strictly monotonically increasing, $x_{i}^{0} = W_{i}$ and $x_{i}^{m_{i}} = B_{i}$ holds, and the restrictions

$$
\theta_ {i} ^ {j + 1} - \theta_ {i} ^ {j} \geq \delta \quad \forall j = 0, \dots , m _ {i} - 1\tag{3}
$$

have to be fulfilled ( $\delta > 0$ ). If the function $F_{i}$ is only monotonically increasing,

$$
\theta_ {i} ^ {j + 1} - \theta_ {i} ^ {j} \geq 0 \quad \forall j = 0, \dots , m _ {i} - 1
$$

is sufficient. Of course, strictly monotonically decreasing functions must fulfill

$$
\theta_ {i} ^ {j - 1} - \theta_ {i} ^ {j} \geq \delta \quad \forall j = 1, \dots , m _ {i}.\tag{4}
$$

Non-monotonic functions can be modelled, too. For example, if $V_{i}$ is first strictly increasing up to $B_{i} \in X_{i}$ and then strictly decreasing, and $B_{i} = x_{i}^{k}$ for some $k \in \{0, \ldots, m_i\}$ , the corresponding inequalities will be

$$
\theta_ {i} ^ {j + 1} - \theta_ {i} ^ {j} \geq \delta \quad \forall j = 0, \dots , k - 1.\tag{5}
$$

$$
\theta_ {i} ^ {j - 1} - \theta_ {i} ^ {j} \geq \delta \quad \forall j = k + 1, \dots , m _ {i}.\tag{6}
$$

The intuitive notion of “attribute importance” is often not captured correctly by decision makers when they give direct estimates for the scaling constants. The reason is that the ranges of attribute values are not taken into account accordingly (cf. [9, p. 271ff]). Therefore, it is always necessary to refer explicitly to the worst and best levels of each attribute. Starting from the worst conceivable alternative W the user is asked to imagine that he can change one attribute to its best level. He is then asked for a rank order of the attributes, i.e. which attribute he would like to improve first, which one next, and so on. For instance, if there are three attributes starting from $(W_{1}, W_{2}, W_{3})$ the decision maker might state that attribute 2 should be improved first, then attributes 3 and 1, which implies

$$
\left(W _ {1}, B _ {2}, W _ {3}\right) \succ \left(W _ {1}, W _ {2}, B _ {3}\right) \succ \left(B _ {1}, W _ {2}, W _ {3}\right).
$$

These preferences yield the restrictions

$$
\begin{array}{l} F _ {2} (B _ {2}) - F _ {3} (B _ {3}) \geq \delta \\ F _ {3} (B _ {3}) - F _ {1} (B _ {1}) \geq \delta . \end{array}
$$

Other restrictions can be gained by improving more than one attribute at the same time. For example, when comparing the alternatives $(W_{1}, B_{2}, W_{3})$ and $(B_{1}, W_{2}, B_{3})$ the decision maker might have the preference

$$
\left(B _ {1}, W _ {2}, B _ {3}\right) \succ \left(W _ {1}, B _ {2}, W _ {3}\right),
$$

which would be translated into

$$
F _ {1} (B _ {1}) + F _ {3} (B _ {3}) - F _ {2} (B _ {2}) \geq \delta
$$

and thus lead to an additional restriction for the scaling constants. From these examples it should be clear, that ordinal evaluations of reference alternatives that are composed of the worst and best levels of each attribute lead to restrictions for the “weights” of an additive model. These reference alternatives, however, can be built from other reference levels $W_{i}^{\prime}$ and $B_{i}^{\prime}$ for $i \in N$ ( $W_{i} \prec W_{i}^{\prime} \prec B_{i}^{\prime} \prec B_{i}$ ) also. This increases the acceptance of the questions mentioned above since the levels $W_{i}^{\prime}$ and $B_{i}^{\prime}$ can be freely chosen and the resulting alternatives could be more reasonable because they are less extreme. If the decision maker is asked in which sequence he would improve $W' = (W_{1}', \ldots, W_{n}')$ in one attribute to a better level $B_{i}'$ , the rank order could be completely different when using the levels $W_{i}$ and $B_{i}$ . The received information is again ordinal, e.g.

$$
\left(B _ {1} ^ {\prime}, W _ {2} ^ {\prime}, W _ {3} ^ {\prime}\right) \succ \left(W _ {1} ^ {\prime}, W _ {2} ^ {\prime}, B _ {3} ^ {\prime}\right) \succ \left(W _ {1} ^ {\prime}, B _ {2} ^ {\prime}, W _ {3} ^ {\prime}\right),
$$

which can be transformed into new linear restriction on the parameters of the additive model (see also the treatment of holistic preferences later on).

Tradeoffs are indifference judgements concerning two attributes (in the following denoted by Y and Z) with the other attributes held fixed. Since it is assumed that all conditions of an additive value model are fulfilled it is not necessary to mention the attributes apart from Y and Z explicitly. For instance, if y and $y'$ are levels of one attribute Y with $y \succ y'$ and z a level of the other attribute Z, the decision maker is asked to state a level $z' \succ z$ such that he is indifferent between $(y, z)$ and $(y', z')$ . The user-specified level $z'$ can thus be considered as a gain in z to account for the loss in y and is therefore called a “tradeoff”. This tradeoff would be translated into the restriction

$$
F _ {Y} (y) + F _ {Z} (z) = F _ {Y} (y ^ {\prime}) + F _ {Z} (z ^ {\prime}).
$$

If the user does not feel comfortable with indifferences, he may also specify preferences in order to establish at least certain bounds for tradeoffs. To give an example, let $B_{Y}$ and $B_{Z}$ be the best and $W_{Y}$ and $W_{Z}$ be the worst levels for the attributes $Y$ and $Z$ , respectively, and let $(B_{Y}, W_{Z})$ be preferred to $(W_{Y}, B_{Z})$ . Instead of asking now for an exact level $B_{Y} > y > W_{Y}$ such that $(y, B_{Z}) \sim (W_{Y}, B_{Z})$ holds, lower and upper bounds $y'$ and $y''$ in the sense

$$
\left(y ^ {\prime}, W _ {Z}\right) \prec \left(W _ {Y}, B _ {Z}\right) \prec \left(y ^ {\prime \prime}, W _ {Z}\right)
$$

could be given and would be translated into

$$
F _ {Y} (y ^ {\prime \prime}) - F _ {Z} (B _ {Z}) \geq \delta \quad \text { and }\tag{7}
$$

$$
F _ {Z} (B _ {Z}) - F _ {Y} (y ^ {\prime}) \geq \delta .\tag{8}
$$

The most general case regarding ordinal preference information is to consider alternatives that can differ in all attribute levels. These can be already given alternatives $a \in A \subset X$ or randomly generated alternatives $h \in X \setminus A$ . In any case, the decision maker may give holistic judgements for any two (pareto-efficient) alternatives $a, b \in X$ , e.g. $a > b$ . This preference would be translated into

$$
f (a) - f (b) = \sum_ {i = 1} ^ {n} \left(F _ {i} (a _ {i}) - F _ {i} (b _ {i})\right) \geq \delta
$$

for each such pair thus producing additional restrictions. Of course, the rank order of reference alternatives was just an example for that though the way to obtain that information was different. Generally the three relations $a \succ b$ , $a \succ b$ and $a \sim b$ are allowed for any two holistic alternatives $a, b \in X$ .

The problem of maintaining consistency within the given evaluations from a normative point of view is not trivial. For example, after entering $a \succ b$ and $b \succ c$ the entering of $a \preccurlyeq c$ violates transitivity, thus only the entering of $a \succ c$ should be possible (which at this point, of course, is redundant). Pragmatic and methodological aspects in handling problems of this kind are addressed in [13] and cannot be explained here in detail.

## The restriction system

Let I denote the set of preference information received by the decision maker. The set I contains monotonicity statements, evaluation of reference alternatives, tradeoffs and arbitrary holistic judgements as described. Since judgements on reference alternatives are specific holistic preferences they do not have to be considered explicitly. The entire restriction system is denoted by $\Theta(I)$ and may consist of the following parts:

$$
\Theta (I) \left\{ \begin{array}{l l} f (a) - f (b) \geq \delta & \forall a, b \in A \text { with } a > b \\ f (a) - f (b) = 0 & \forall a, b \in A \text { with } a \sim b \\ f (a) - f (b) \geq 0 & \forall a, b \in A \text { with } a \succcurlyeq b \\ \text { restrictions   from   tradeoffs   (cf.   7,   8) } \\ \text { monotonicity   restrictions   for   all } \\ n \text { attributes   (cf.   3,   4) } \\ \delta \geq \delta^ {\min} \end{array} \right.
$$

The linear restriction system $\Theta(I)$ is either empty or non-empty. Feasibility can be checked by performing the phase 1 of a linear program. If $\Theta(I)$ is feasible, one suitable preference function, i.e. one point out of $\Theta(I)$ has to be determined. In this approach this is done by using the objective function

max $\delta$

(9)

i.e. the preference function chosen has the property that it maximizes the differences $f(a) - f(b)$ for any two alternatives or consequences with $a > b$ . If $\delta^{max}$ is the optimal value of the linear program

max $\delta$

subject to $\Theta(I)$

then one also has an upper bound for $\delta$ . If $\Theta(I)$ is empty, the information captured by $I$ is inconsistent. This situation has to be handled in detail. The inconsistency could be due to the fact that $\delta^{\min}$ was chosen too large. This can be easily checked if one substitutes the restriction $\delta \geq \delta^{\min}$ by $\delta \geq 0$ . If there is a feasible solution for this modified linear program and $\delta^{\max}$ is very small ( $\delta^{\max} \approx 0$ ), this would be equivalent to an inconsistency since strict preferences cannot be modelled properly. Otherwise the decision maker could adjust $\delta^{\min}$ to $\delta^{\min'}$ such that $\delta^{\min'} \leq \delta^{\max}$ holds.

## 4.4. Transformation of cardinal information

Cardinal information includes the evaluation of lotteries and strength of preferences. A von Neumann-Morgenstern utility function reflects the decision maker's preference structure for lotteries whereas a measurable value function ranks strength of preferences.

The assumption for a utility function to be additively decomposable are well known [9, pp. 295] and have to be fulfilled if the approach described here is to be applied. In this case, many types of information regarding the decision maker's risk behaviour can be taken into account. For example, if the decision maker is risk avers with respect to attribute $i$ , his utility function $F_{i}$ must be concave. This can be achieved by adding the restrictions

$$
\frac {\theta_ {i} ^ {j} - \theta_ {i} ^ {j - 1}}{x _ {i} ^ {j} - x _ {i} ^ {j - 1}} - \frac {\theta_ {i} ^ {j + 1} - \theta_ {i} ^ {j}}{x _ {i} ^ {j + 1} - x _ {i} ^ {j}} \geq 0 \quad \forall j = 1, \dots , m - 1.
$$

A certainty equivalent $x_{i}$ for a lottery $l$ (i.e. $x_{i} \sim l$ ) where $l = \langle (p, 1 - p); (x_{i}', x_{i}'')\rangle$ denotes the risky alternative that yields $x_{i}'$ with probability $p$ and $x_{i}''$ with probability $1 - p$ , has to fulfill $F_{i}(x_{i}) = pF_{i}(x_{i}') + (1 - p)F_{i}(x_{i}'').$ (10) In the equation (10) the terms $F_{i}(x_{i}), F_{i}(x_{i}')$ and $F_{i}(x_{i}'' )$ are convex combinations of parameters $\theta_{i}^{j}, j \in \{0, \dots, m_{i}\}$ and therefore (10) gives an additional restriction for the system $\Theta(I)$ . Of course, the same argument can be made, if $p$ is determined as probability equivalent for $x_{i}, x_{i}^{\prime}$ and $x_{i}^{\prime\prime}$ given.

Bounds for certainty and probability restrictions can analogously be transformed into proper inequalities (compare the transformation of bounds for tradeoffs).

Using this parameter approach for assessing one-dimensional utility functions is very helpful since thus many different types of information can be exploited, even if the decision maker is not able to state exact indifferences.

It would be even possible to rank order several lotteries with two or more outcomes, if the decision maker is willing to do that, and to use that information in the described construction process of the utility function $F_{i}$ .

The decision maker may give information on his strength of preferences, too, e.g. he may say that for three alternatives $x, y, z \in X$ with $x > y > z$ , he prefers $x$ more over $y$ than $y$ over $z$ . This would add the restriction

$$
\begin{array}{l} f (x) - f (y) > f (y) - f (z) \quad \text { or } \\ f (x) - 2 f (y) - f (z) \geq \delta (> 0). \end{array}
$$

This is one example for representing preference strength. Direct rating techniques are also usable, e.g. if $x \in X$ is rated between 0.4 and 0.6 this information would be translated into

$$
0. 4 \leq f (x) \leq 0. 6.
$$

## 4.5. Differences to PREFCALC

The system PREFCALC and its underlying theory known as the “UTA-method” by [7] are the basis for this approach. However, there are many differences and extensions that were not realized in PREFCALC.

To begin with, the use of error variables $\sigma_{a}$ , $\sigma_{b} \geq 0$ for modelling the preference $a \succ b$ by

$$
\left(f (a) + \sigma_ {a}\right) - \left(f (b) + \sigma_ {b}\right) \geq \delta
$$

is not made here. If the preference information given is consistent with an additive preference model, these terms vanish anyway.

This enables one to consider only the restrictions that are really necessary for the underlying preference function. If the restriction set is not empty, the entire set of consistent preference functions is obtainable and can be analyzed. In contrast, PREFCALC uses the linear program

$$
\min \sum_ {a \in B} \sigma_ {a} - \delta\tag{11}
$$

which collapses the function set to exactly one function. In PREFCALC the set $B \subset A$ used is a subset of the given alternative set A, for which a complete order has to be specified. Using PREFCALC it is not possible to specify only a partial order on B. In this approach, this can be done, since alternatives are compared only pairwise.

In PREFCALC the interacting is very static. Based on a complete order on B, a preference function consistent with it is computed by a linear program. This function is then applied to the entire alternative set.

If the user then wants to add additional preferences that are not in B he cannot do so unless he enlarges B. He then has to re-enter information given before which can make the use of PREFCALC somewhat inefficient.

In this approach, re-entering of information is not necessary since all the evaluations given are stored and can be taken into account automatically. It is also possible to delete parts of former preferences which cannot be done in PREFCALC unless B is modified and evaluated again. Thus the interaction with the system provides more flexibility, especially the decision maker can work on his decision problem in different sessions.

A main difference to PREFCALC is also the extension to more types of information. All three relations $\succ, \succ$ and $\sim$ can be used whereas PREFCALC only allows $\succ$ .

The performing of tradeoffs or the evaluation of improvements of reference levels is not possible in PREFCALC unless one constructs specific hypothetical alternatives. But then again, B needs to be enlarged by these alternatives to a new set $B'$ and a complete preference order for $B'$ is necessary, i.e. the hypothetical alternatives have to be compared with all alternatives $b \in B$ , too.

## 5. Preference functions as performance measures

Preference functions arise as measures of performance in queueing theory, as cost functions in (machine) scheduling, and in an abundance of other application areas. Assessing preference functions in such an area can benefit from that area's particular structure. We demonstrate this in scheduling. Thus, we shortly repeat the underlying (standard) scheduling model of which numerous relaxations are known.

A set of jobs $\{1,\ldots,n\}$ is to be processed on machines $1,\ldots,m$ , m<n in general, where all machines are identical meaning that they can all perform the same tasks at the same speed. Jobs are available at time 0 and they require some known amount $x_{1},\ldots,x_{n}\in(0,\infty)$ of processing time. A schedule S assigns each job a starting time on a free machine. Once started, job i will be processed without interruption (non-preemptive scheduling) until its completion time $C_{i}=C_{i}(S)$ . Various schedules are feasible and they are to be ranked by a so-called regular measure of performance (cost function) $f:\mathbb{R}_{\geq}^{n}\to\mathbb{R}_{\geq}$ depending on $C_{1},\ldots,C_{n}$ ; $f(C_{1},\ldots,C_{n})$ . Regularity of f means isotonicity with respect to the point-wise order $\leq_{R^{n}}$ of two vectors $x=(x_{1},\ldots,x_{n})^{T}$ , $y=(y_{1},\ldots,y_{n})^{T}\in\mathbb{R}^{n}$ : $x\leq_{R^{n}}y$ iff $\forall i=1,\ldots,n$ $x_{i}\leq y_{i}$ . $x\leq_{R^{n}}y$ must imply $f(x)\leq f(y)$ . Common measures of performance are:

$f(C_{1},\ldots ,C_{n}) = \max \{C_{1},\ldots ,C_{n}\} = :C_{\max}$ make- span,

$f(C_{1},\ldots ,C_{n}) = \sum_{i = 1}^{n}w_{i}C_{i}$ weighted flowtime with fixed $w_{i}\in (0,\infty)$ and special case

$f(C_{1},\ldots ,C_{n}) = \sum_{i = 1}^{n}C_{i}$ flowtime, $f(C_1,\dots ,C_n) = \sum_{i = 1}^{n}w_i(C_i - d_i)^+$ weighted tardiness where $d_{i}\in (0,\infty)$ is the due date of job $i$

The first three functions belong to the class of Markovian cost functions, these are functions of the form

$$
\begin{array}{r l} & f (C _ {1}, \dots , C _ {n}) \\ & = g (\{1, \dots , n \}) C _ {i _ {1}} + g (\{1, \dots , n \} - \{i _ {1} \}) \\ & \times (C _ {i _ {2}} - C _ {i _ {1}}) + \dots \\ & + g (\{i _ {n} \}) (C _ {i _ {n}} - C _ {i _ {n - 1}}) \end{array}
$$

for $C_{i_1} \leq \ldots \leq C_{i_n}$ . The function $g: \mathcal{P}(\{1, \ldots, n\}) \to \mathbb{R}_{\geq}$ with $g(\emptyset) = 0$ is called cost rate of $f$ ; $\mathcal{P}(\{1, \ldots, n\})$ is the power set of $\{1, \ldots, n\}$ . Setting for $U \neq \emptyset g(U) = 1$ , $g(U) = \sum_{i \in U} w_i$ , and $g(U) = |U|$ results in makespan, weighted flowtime, and flowtime, respectively. A Markovian cost function is generally not an additive preference function since it cannot be written as a sum of $n$ functions $f_1, \ldots, f_n: f(C_1, \ldots, C_n) \neq f_1(C_1) + \ldots + f_n(C_n) (\neq \text{denoting that functions are not identical})$ . A Markovian cost function generally is not even a multilinear preference function.

Simple schedules or scheduling strategies are given by static priority rules: $1 \prec_{pri} \ldots \prec_{pri} n$ means that jobs are considered in the sequence $(1, \ldots, n)$ . If job 1 is available at time 0 (it may not be due to a later release time or precedence constraints), it is assigned to a processor and removed from the priority list. Then the next job on the list is considered and so on. At any decision moment the current list is scanned and the procedure is repeated until the list of unassigned jobs is empty. Time 0 and job completions are decision moments.

We do not focus on algorithms for scheduling problems but on assessing cost functions, for example by determining the coefficients in case of the weighted flowtime criterion. Weighted flowtime is an additive preference function. Determining the $w_{i}$ 's is done by an analog to the LP formulation of the previous section. However, it is important to note that in order to exploit special structure and to be efficient, subsequent linear programs are not straightforward special cases of those given before. In fact they are neither more nor less general. This is due to at least two reasons:

1. The intricate relationship between scheduling (model) and preference functions.

2. The nonexistence of a best or worst alternative (since schedules (alternatives) are considered for fixed but otherwise arbitrary processing times).

Suppose information is given about a schedule $S_{k}$ being preferred to some other schedule $S_{j}$ for schedules $S_{j}$ , $S_{k}$ in some set B. Further, there may be given explicit information on indifferences of alternatives in some set S; S = 0 admitted. This information can be transformed into the linear program denoted by LPwC (linear program for weighted completions):

LPwC max $\delta -\epsilon$

subject to $\sum_{i=1}^{n} w_i C_i (S_k) + \delta \leq \sum_{i=1}^{n} w_i C_i (S_j)$

for $S_{j}\prec S_{k},S_{j},S_{k}\in \mathcal{B}$

$$
- \epsilon \leq \sum_ {i = 1} ^ {n} w _ {i} C _ {i} (S _ {k}) - \sum_ {i = 1} ^ {n} w _ {i} C _ {i} (S _ {j}) \leq \epsilon
$$

$$
\begin{array}{l} \text { for } S _ {j} \sim S _ {k}, S _ {j}, S _ {k} \in \mathcal {I} \\ \sum_ {i = 1} ^ {n} w _ {i} = 1 \\ w _ {1}, \ldots , w _ {n}, \delta , \epsilon \geq 0. \end{array}
$$

For $\mathcal{I} = \emptyset$ the second set of constraints and $\epsilon$ vanish. Subsequent statements about $LPwC$ are to be understood respectively. A preference over schedules is representable by $\sum_{i=1}^{n} w_i C_i$ iff $LPwC$ has a solution with $\epsilon = 0 < \delta$ . The norming condition $\sum_{i=1}^{n} w_i = 1$ may not be dropped since $LPwC$ without this condition has an objective unbounded from above.

Schedules appearing in pairwise relations $\prec$ or $\sim$ must be considered for the same processing times. Otherwise preferences over schedules and preferences over processing times may become confused.

Example. Let n = 3 jobs and m = 2 machines. Consider two schedules:

$S_{1}$ is given by the static priority $1 \prec_{\mathrm{pri}} 2 \prec_{\mathrm{pri}} 3$ and $S_{2}$ is given by the static priority $1 \prec_{\mathrm{pri}} 3 \prec_{\mathrm{pri}} 2$ .

$i(x_{i})$ : job i needs processing time $x_{i}$ .

<table><tr><td>machine 1</td><td>1(5)</td><td>3(4)</td></tr><tr><td>machine 2</td><td>2(6)</td><td></td></tr></table>

Condition $S_{2} \prec S_{1}$ is transformed into $5w_{1} + 10w_{2} + 4w_{3} + \delta_{2} \geq 5w_{1} + 6w_{2} + 9w_{3} + \delta_{1} + \delta$ ( $\Leftrightarrow 4w_{2} + \delta_{2} \geq 5w_{3} + \delta_{1} + \delta$ ). LPwC is thus solvable with $\delta_{1} = \delta_{2} = 0 < \delta$ .

The linear program to assess an arbitrary Markovian cost function is an immediate generalization of LPwC. Its number of variables is exponential in n. However, there are preferences which cannot be represented even by an arbitrary Markovian cost function.

Example. Let n = 4 jobs and m = 1 machine. Consider the schedules:

$S_{1}$ is given by the static priority

$$
1 \prec_ {\mathrm{pri}} 2 \prec_ {\mathrm{pri}} 3 \prec_ {\mathrm{pri}} 4,
$$

$S_{2}$ is given by the static priority

$$
2 \prec_ {\mathrm{pri}} 1 \prec_ {\mathrm{pri}} 3 \prec_ {\mathrm{pri}} 4,
$$

$S_{3}$ is given by the static priority

$$
\begin{array}{l} 2 \prec_ {\text {pri}} 1 \prec_ {\text {pri}} 4 \prec_ {\text {pri}} 3, \\ \text {and} \end{array}
$$

$S_{4}$ is given by the static priority

$$
1 \prec_ {\mathrm{pri}} 2 \prec_ {\mathrm{pri}} 4 \prec_ {\mathrm{pri}} 3.
$$

If all processing times are equal (say 1), then elementary calculations show that the strict preference $S_{1} \prec S_{2} \prec S_{3} \prec S_{4}$ cannot be represented by a Markovian cost function.

Non-Markovian cost functions like weighted tardiness can also be assessed by linear programs if the due dates $d_{i}$ are known. For unknown weights and due dates the linear framework is left. The variety of arising nonlinear problems is subject to further investigations.

## 6. Implementational issues and an application to environmental modelling

A prototype system that is able to handle all the ordinal information as described in section 4 and partially cardinal information was developed at the FAW. It is implemented in the language 'Objective-C', a superset of C which incorporates object-oriented programming concepts. The implementation is on a SUN 3/80. In order to be able to use specific procedures of the tool in other systems, too, it is planned, to write a C-interface for the objects in question. An interface in X-Windows is also planned which would be especially useful for displaying the piecewise linear functions.

In the current system, user information is obtained using a command language. This enables a decision maker to effectively enter and view his preference information. Since many commands have been implemented, it is impossible to describe all of them in detail here. For example, the command ordinal a b allows to select two alternatives a and b and evaluate them ordinally. The command display ordinals shows all the evaluations stated so far (including dominance relations), and display preference function shows the current preference function chosen from the set of functions consistent with the information given.

If inconsistent information is given, the system detects it automatically and shows the user preference information reasonably to be modified in order to achieve consistency again.

Moreover, a specific preference elicitation system to handle a practical problem of environmental risk assessment was developed [8]. The latter system ranks a large number (200–5000) of “point sources” of potential hazard to groundwater according to expert judgement. Such point sources comprise production facilities dealing with hazardous liquids, gasoline stations, and even laundries. Expert judgement was chosen as a proxy measure for unavailable statistical information about the potential environmental damage depending on a set of criteria. Such statistical information like regression does not depend on personal preferences, and it is the true measure of risk here. However, unobtainability of this past information had to be substituted by anticipative abilities and experience of domain experts. The set of criteria, which were agreed upon by a board of responsible individuals, consists of:

• Volume of stored hazardous liquid.

\- Hazard class of stored liquid.

\- Importance of endangered water supply well.

\- Technical safety of storage tank.

\- Location relative to water protection zones or well catchments.

Suppose monitoring wells are to be built close to the point sources in their groundwater downstream area. Risk ranking allows N monitoring wells – the number N given for example by some budget constraint – to be assigned to the N most risky point sources. Multicriteria decision analysis is a well-suited tool to deal with such a problem in principle. In this case however, MCDA becomes applicable only if implemented in a software system, one reason being the large number of alternatives which humans have difficulties to handle. In the given application the FAW preference elicitation tool was applied to deduce a preference function approximation on the base of an ordinal ranking of about 10 “extreme” point sources. Using the obtained preference function to order all point sources resulted in a ranking that after some minor re-ordering gained approval by the group of responsible experts.

## Acknowledgements

The authors would like to thank all participants of the FAW workshop Decision Analysis and Knowledge Based Reasoning which took place at the FAW, September 11–15, 1989, and which helped formulate the approach presented here.

## References

[1] G. Cantor, Beiträge zur Begründung der transfiniten Mengenlehre, Mathematische Annalen 46 (1895) 481-512.

[2] V. Dhar and N. Ranganathan, Experiments with an Integer Programming Formulation of an Expert System, MCC Technical Report No. ACA-AI-022-89 (1989).

[3] J. Dyer and R. Sarin, Measurable Multi-Attribute Value Functions, Operations Research 27, No. 4 (1979) 810–822.

[4] F. Glover and M. Laguna, Target Analysis to Improve a Tabu Search Method for Machine Scheduling, Working Papers on Artificial Intelligence in Management Science 1 (1989) 56–74.

[5] W. Edwards and D. Von Winterfeldt, Decision Analysis and Behavioural Research (Cambridge University Press, Cambridge, 1986).

[6] P.C. Humphreys and A. Wisudha, Techniques and Tools Providing Strategic Decision Support: A Framework, Review and Guidelines, Technical Report No. 89-1 (Decision Analysis Unit Publications, London, 1989).

[7] E. Jacquet-Lagrèze and J. Siskos, Assessing a Set of Additive Utility Functions for Multicriteria Decision-Making, the UTA Method, European Journal of Operational Research 10, No. 2 (1982) 48–58.

[8] T. Kämpfe, W. Kress, K.-P. Schulz and P. Wolf, Multiattributive Bewertungen mit Anwendungen auf Umweltprobleme, FAW-Bericht TR-91009 (Ulm, 1991).

[9] R.L. Keeney and H. Raiffa, Decisions with Multiple Objectives – Preferences and Value Tradeoffs (Wiley, New York, 1976).

[10] D.B. Lee, Enhanced Decision Analysis Support System, Unpublished Masters Thesis (School of Engineering, Air Force Institute of Technology, Wright Patterson Air Force Base, 1981).

[11] T. Lengauer, Combinatorial Algorithms for Integrated Circuit Layout (Wiley, New York, 1990).

[12] J. von Neumann and O. Morgenstern, Theory of Games and Economic Behaviour (Princeton University Press, Princeton, NJ, 1947).

[13] P. Wolf, Rechnerunterstützte Elizitierung mehrattributiver Präferenzstrukturen, Dissertation (University of Ulm, 1992).
