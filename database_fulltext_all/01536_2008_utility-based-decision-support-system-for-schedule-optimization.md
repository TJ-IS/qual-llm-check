---
otero_id: 1536
otero_key: "9V89NNE8"
title: "Utility-based decision support system for schedule optimization"
authors: "I-Tung Yang"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.08.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Utility-based decision support system for schedule optimization

I-Tung Yang

Department of Construction Engineering, National Taiwan University of Science and Technology, No. 43, Section 4, Keelung Road, Taipei 106, Taiwan

Received 26 December 2005; received in revised form 22 July 2007; accepted 5 August 2007 Available online 24 August 2007

## Abstract

The present study quantifies the impact of individual preferences of decision makers on schedule optimization and proposes a decision support system (DSS) to account for the diversity in the time–cost tradeoff analysis. The proposed DSS defines the multiattribute utility function based on subjective assessment of one-dimensional utility functions and scaling factors of time and cost. The multiattribute utility function is subsequently optimized by aid of a new particle swarm optimization algorithm. The application of the proposed DSS is demonstrated through case studies. It has been verified, both statistically and subjectively, that the proposed DSS is effective, efficient, and robust. It has also been shown that the proposed DSS outperforms genetic algorithms. The formulation of the proposed DSS is of practical value because it considers, in addition to direct and indirect costs, the amount of liquidated damages and bonus for early completion. Moreover, the formulation has no restriction on the forms of activity time– cost functions and therefore provides the most flexibility. © 2007 Elsevier B.V. All rights reserved.

Keywords: Decision support system; Utility; Optimization; Particle swarm optimization; Computational intelligence

## 1. Introduction

Much research effort on schedule optimization has been devoted to the time–cost tradeoff analysis of projects. It is generally realized that accelerating the progress of a project would require more labor and better equipment, thus involving higher costs. Accordingly, a tradeoff exists between project duration and cost. The decision of choosing a combination of time and cost to suit specific needs is relevant and important. In the time–cost tradeoff analysis, there are three common objectives: to minimize the direct (or total) cost while meeting a specified deadline, to minimize the project duration within a prescribed budget, or to obtain the Pareto front by optimizing both time and cost simultaneously.

To solve the time–cost tradeoff problem, numerous attempts have been made to a wide variety of models that can be categorized in two main groups: heuristic approaches and mathematical programming techniques. A popular heuristic approach begins with a list of activities on the critical path ranked in accordance with the unit change in cost for a reduction in duration. The heuristic then proceeds by crashing activities in the order of their lowest impact on costs [11]. Another kind of heuristics is the local search method, which is inspired by the advancement of computational intelligence, such as genetic algorithms (GA), to perform optimization on time and cost [10,16,17]. Mathematical programming models, depends on the type of the time– cost relationships, can be further divided into several well-developed kinds: linear programming, mixed integer programming, dynamic programming, and chance-constrained programming [8,18,21,27].

![](/api/attachments/9V89NNE8/fulltext/images/bfefa083546e77e2ffff814c4dded110c088001f7459246a83f3d7c92f3f5416.jpg)  
Fig. 1. Common utility shapes.

As a decision problem, the time–cost tradeoff analysis is embodied by subjective judgments in determining the optimality of a time–cost option. For example, whether it is preferred to have the project complete in 100 days, costing 10 million dollars or in 120 days, costing 9.5 million? Since both options cannot dominate each other, the question then becomes: “Can the decrease of 20 days offset the extra cost of 0.5 million?” The answer depends upon the perceived weights of 20 days and 0.5 million. The subjective judgments are often hard to measure and can vary from person to person and even time to time according to decision makers' individual preferences, implicitly influenced by environmental and personal factors, such as project immediacy, owner's financial condition, and consequences of late delivery.

The diversity in preferences can be addressed by individual's utility function, which measures satisfaction gained from the consequences of a project: total cost and project duration. In time–cost optimization, the utility functions are monotonically decreasing within the range of (0,1). Fig. 1 graphically depicts three common utility shapes: concave, convex, and combination. The shapes of the utility functions reflect the decision maker's nonlinear preference on time and cost, e.g., a 20 day reduction from 120 to 100 days would be preferred than that from 130 to 110 days in the case of a convex utility function. The absolute value of the curvature of the function indicates the strength of preferences. The higher the absolute value, the stronger the preference is. It is also possible that the decision maker switches his/her preference according to the magnitude of the variables. For example, the utility may be concave for a higher cost and convex when the cost is low.

Since preferences may vary and have a profound impact on schedule optimization, the diversity shall be accommodated to capture the true decision-making mechanisms. To address this need, the goal of the present study is three-fold: (1) to elicit decision makers preference (utility) toward time and cost; (2) to quantify the impact of the utility function on time–cost optimization; and (3) to develop a decision support system (DSS) to help determine the optimal time–cost solution by maximizing the utility function.

The proposed DSS assesses decision makers' preference by measuring their utility functions for time and cost separately. The two one-dimensional utility functions are then combined into a multiattribute function, which is optimized (maximized) within the search space of feasible activity durations and costs. Note that the activity durations and costs handled in this paper are deterministic. The proposed DSS focuses on finding subjectively optimal solution based on nonlinear utility functions.

![](/api/attachments/9V89NNE8/fulltext/images/0a044495db6e306ca1037f1a2edc6866a857baa6cba96259e2dd0319764932e6.jpg)  
Fig. 2. Proposed DSS.

Because the search space is often of high complexity (nonlinear, discontinuous, and nonsmooth), the optimization model is solved by a new computational intelligence technique: particle swarm optimization (PSO). Given that genetic algorithms are readily available, the reasons to develop a new PSO algorithm are multi-fold. PSO has been shown competitive to GA [1], or even superior to GA in continuous optimization problems [25]. Furthermore, PSO is particularly attractive in its algorithmic simplicity since it demands no coding and decoding operation [15].

Finally, the optimization results are directly linked to a full-scale schedule to facilitate further planning. Fig. 2 outlines the procedural steps, whose theoretical foundation will be introduced in the remainder of this paper.

## 2. Assessment of utility: lottery equivalent

To measure one's utility function, the best and worst extremes of the range of possible outcomes are assigned utilities of 1 and 0, respectively. Intermediate points of the utility function can be determined by either of the following two methods: certainty equivalent and lottery equivalent. Due to limited space, details of these two methods can be found in [4].

The proposed DSS adopts the lottery equivalent method, not the certainty equivalent method. This is to prevent the problem of error propagation, which may arise when calculating a utility requires utilities determined previously [19].

Specifically, the present study elicits the utility function of decision makers in the following steps:

1. Define the ranges of possible consequences of project duration and total cost by calculating the best (minimum) and worst (maximum) values. Assign the utilities of the former and the latter to be 1 and 0, respectively.

2. Assess the intermediate points of the utility functions by the lottery equivalent method.

3. Approximate the utility functions. Common forms include the power function $U ( X ) { = } a + b X ^ { c }$ and the exponential function $U ( X ) { = } a + b \mathrm { e } ^ { - c X }$ where $a , \ b ,$ and c are fitting parameters.

## 3. Multiattribute utility

The time–cost tradeoff analysis involves two criteria: project duration and total cost. To incorporate the preference of decision makers toward these two criteria simultaneously, the proposed DSS combines the two one-dimensional utility functions into a multiattribute utility function following the procedure suggested by Keeney and Raiffa [14].

The procedure, however, relies on two important assumptions: preferential independence and utility independence. Preferential independence is the condition that preferences for specific outcomes of one attribute do not depend on the value of another attribute. In the present study, the interviewed project managers are asked if their ranking of different times (costs) would be changed by variation in the levels of costs (times). The answer is no and thereby verifies the assumption of preferential independence.

Utility independence requires that preferences for uncertain choices involving different outcomes of one attribute are independent of the value of another attribute. This assumption is concerned with consistent preferences under uncertainty; it does not demand statistical independence between attributes. Here, the project managers do not change their preferences involving uncertain outcomes of times (costs) upon variation of costs (times). We believe this is because the range of possible times (costs) is not that wide to have an impact as the lowest estimate is typically 60–80% of the highest estimate, e.g., [10,17,29]. Of course, the finding is empirical and the assumption should always be checked.

After verification of preferential and utility independence, the procedure continues by estimating the scaling factors of both attributes. The scaling factor of an attribute against the other can be found by obtaining the indifference statement of the following form

$$
\left(X _ {1} ^ {*}, X _ {2 ^ {*}}\right) \sim (\mathbf {X} ^ {*}, p; \mathbf {X} _ {*})\tag{1}
$$

The question addressed to the project manager can be expressed as

“Consider two situations. The first one is that the project ends with the shortest duration and highest cost. The second situation is that you will have a probability $p$ to achieve the shortest duration and lowest cost while a probability $1 - p$ to have the longest duration and highest cost. Will you prefer the first situation if $p$ is 90%, 10%, and so on?”

By gradually bracketing the probability, the individuals would provide their specific scaling factor for time. For instance, if the individual is indifferent between two situations when the probability is $6 0 \% ,$ the scaling factor of time would be 0.60. The same procedure can be repeated to find the scaling factor for cost. Generally, a higher scaling factor reflects greater importance of the specific attribute.

With the one-dimensional utility function $U ( X _ { i } )$ and scaling factors $k _ { i } ,$ the multiattribute utility function U (X) is defined by

$$
K U (\mathbf {X}) + 1 = \prod_ {i = 1, 2} (K k _ {i} U (X _ {i}) + 1)\tag{2}
$$

where the normalizing parameter K can be derived by assuming the utilities of both attributes are 1:

$$
K + 1 = \prod_ {i = 1, 2} (K k _ {i} + 1)\tag{3}
$$

The parameter K is used to normalize the multiattribute utility value, i.e., to make the value lie between 0 and 1. All the scaling factors do not necessarily sum to 1. If they do, Eq. (3) will be degenerated to an additive case

$$
U (\mathbf {X}) = \sum_ {i = 1, 2} k _ {i} U (X _ {i})\tag{4}
$$

The procedure above needs 2(N − 1) evaluations to define N points in two dimensions because each dimension would need N − 2 estimates (exclude the best and worst) and 1 scaling factor. In contrast, without using the multiattribute utility function, pair-wise evaluation would require $N ^ { 2 } { - } 2$ points to define N discrete points for both time and cost (exclude the best and worst). Thus the procedure can reduce computational complexity considerably from exponential to linear.

## 4. Optimization model

The next step of the proposed DSS is to maximize the utility function within the search space of feasible activity times and costs, which ultimately determine the optimal pair of project duration and cost. This section gives the formulation of the optimization model. The project duration is

$$
D = \max _ {\forall i} \left\{E S _ {i} + t _ {i} \right\}\tag{5}
$$

where D denotes the project duration, which is the maximum early finish time among all the activities i.

The early start time $E S _ { i }$ is computed recursively by satisfying the precedence constraints between activity i and all the activities in its successor set S

$$
\begin{array}{l} E S _ {i} + t _ {i} \leq E S _ {j}, \forall j \in S _ {i} \\ E S _ {i}, t _ {i} \geq 0 \end{array}\tag{6}
$$

where $t _ { i }$ is the duration for activity i.

The total cost encompasses three elements: direct cost, indirect cost, and the amount of liquidated damages or bonus for early completion. The direct cost is simply the sum of all the activity costs, each of which is a function of the activity duration.

$$
C _ {\mathrm{dir}} = \sum_ {\forall i} c _ {i} = \sum_ {\forall i} f (t _ {i})\tag{7}
$$

Eq. (7) has no assumption on the form of the activity time–cost function, i.e., it can be of any type: piecewise linear, nonlinear, discrete, or discontinuous.

The indirect cost, such as daily overhead, is expressed as a linear increasing function of time

$$
C _ {\mathrm{ind}} = D \times \alpha\tag{8}
$$

where α = daily indirect cost that is measured in \$/day.

The amount of liquidated damages or bonus is regulated in the clauses of the contract to prevent late completion and encourage early delivery. The amount is usually imposed as a fixed number or as an increasing function of time. For the latter, the amount may, on some occasions, be capped at an upper bound, which is a portion of the expense (the sum of direct and indirect costs). For example, the amount of liquidated damages may be expressed as: “If there is a delay in completing the work over 100 days, the liquidated damages is assessed to be \$1,000 per day or 10% of the expense whichever is smaller.” In mathematical form, the amount of liquidated damages is

$$
C _ {\mathrm{liq}} = \min \left\{\gamma^ {+} \times \max [ 0, (D - D ^ {+}) ], \left(C _ {\mathrm{dir}} + C _ {\mathrm{ind}}\right) \times \beta^ {+} \right\}\tag{9}
$$

where $\gamma ^ { + } { = } \mathrm { d a i l y }$ liquidated damage payment rate, measured in \$/day; D<sup>+</sup> = targeted project duration (for damages); D = actual project duration; β<sup>+</sup> = percentage of the expense.

Similarly, the amount of bonus can be illustrated as “If the project is completed within 80 days, the bonus for early completion is \$800 per day or 8% of the expense whichever is smaller.” The bonus can be expressed as

$$
C _ {\text { bon }} = \min \{\gamma^ {-} \times \max [ 0, (D ^ {-} - D) ], (C _ {\text { dir }} + C _ {\text { ind }}) \times \beta^ {-} \}\tag{10}
$$

where γ<sup>−</sup> = daily bonus rate measured in \$/day; D<sup>−</sup> = targeted project duration (for bonus); $\beta ^ { - } = \mathsf { p e r - }$ centage of the expense.

Overall, the total cost is the sum of all the elements in Eqs. (7)–(10). The bonus for early completion would essentially decrease the total cost.

$$
C = C _ {\mathrm{dir}} + C _ {\mathrm{ind}} + C _ {\mathrm{liq}} - C _ {\mathrm{bon}}\tag{11}
$$

The project duration and total cost can be directly mapped to a utility value according to the multivariate utility function. The utility value then becomes the objective being optimized subject to constraints in Eqs. (5)–(11):

Maximum $\mathrm { U } ( C , D )$

<sub>ð</sub><sup>12</sup><sub>Þ</sub>

## 5. Particle swarm optimization algorithm

The complexity of the present optimization model is primarily determined by Eq. (7) as the function between activity time and cost may take several forms: piecewise linear [11], nonlinear [5], discontinuous [18], discrete [3,10], and any mix of the above [28]. Furthermore, the MAX and MIN functions in Eqs. (9) and (10) would make the problem nonsmooth and nonconvex, presumably causing the appearance of multiple local optimal solutions. This level of complexity makes traditional optimization techniques of limited help.

To optimize the multiattribute utility function in such an intractable search space, the proposed DSS is equipped with a new particle swarm optimization (PSO) algorithm. The original PSO concept was pioneered by Eberhart and Kennedy [6] by mimicking the social adaptation of a biological creature in a swarm, such as fishes, insects, or birds [15]. This computational intelligence technique has been since applied to a wide spectrum of domains [13,22– 24,26]. Application results confirm the general performance of PSO algorithms.

A standard PSO algorithm is initialized with a swarm of random candidate solutions (particles). Each particle is iteratively moved across the search space and is attracted to the position of the best fitness historically achieved by the particle itself (local best, pBest) and by the best among the neighbors (global best, gBest). In essence, each particle continuously focuses and refocuses the effort of its search according to both local and global bests until converging to the optima.

The PSO concept is easy to implement because it involves only two equations, illustrated in Fig. 3. The first equation moves a particle by adding a change velocity $\overrightarrow { \nu _ { i } } ( t + 1 )$ to the current position $\overrightarrow { x _ { i } } ( t )$ at time step t + 1:

$$
\overrightarrow {x _ {i}} (t + 1) = \overrightarrow {x _ {i}} (t) + \overrightarrow {v _ {i}} (t + 1)\tag{13}
$$

The second determines the velocity as a combination of three contributing factors: (1) previous velocity $\overrightarrow { \nu _ { i } } ( t )$ , (2) movement in the direction of the local best $\dot { \overrightarrow { x _ { \mathrm { L } } } }$ <sup>ð Þ</sup>, and (3) movement in the direction of the global best $\overrightarrow { x _ { \mathrm { G } } }$ Formally, the velocity is given by

$$
\begin{array}{c} \overrightarrow {v _ {i}} (t + 1) = w \times \overrightarrow {v _ {i}} (t) + r _ {1} c _ {1} \big (\overrightarrow {x _ {\mathrm{L}}} - \overrightarrow {x _ {i}} (t) \big) \\ + r _ {2} c _ {2} \big (\overrightarrow {x _ {\mathrm{G}}} - \overrightarrow {x _ {i}} (t) \big) \end{array}\tag{14}
$$

![](/api/attachments/9V89NNE8/fulltext/images/679634aa367a63f058d175bc48b836a3ec29d9029f6182a58b0f30461b751861.jpg)  
Fig. 3. Illustration of PSO concept.

where w is an inertia weight to control the influence of the previous velocity; $r _ { 1 }$ and $r _ { 2 }$ are two random numbers uniformly distributed in the range of $( 0 , 1 ) ; c _ { 1 }$ and $c _ { 2 }$ are two acceleration constants. The inertia weight has been suggested to decrease as the progress of the evolution to encourage exploration at the beginning and gradually shift the focus to exploitation. Furthermore, to prevent oscillation, the velocity is constrained within a feasible range $( - V _ { \mathrm { m a x } } , V _ { \mathrm { m a x } } )$

The parameters above, along with the swarm size and the number of iterations, are adjustable and have been extensively studied in the literature [2,7,9]. The default setup of the proposed DSS includes the following parameters: w starts at 1.2 and gradually decreases to $0 . 4 ; c _ { 1 }$ and $c _ { 2 }$ are equal to 2; the swarm consists of 20 particles. To prevent superfluous searching, the proposed algorithm places more emphasis on the critical activities because crashing non-critical activities is less likely to increase the total utility. To do so, the acceleration constants for the critical activities are doubled, so as to increase the probability of being crashed.

The pseudocode of the proposed PSO algorithm is shown in Fig. 4. Particles (candidate solutions) are flown in an N-dimensional space where each dimension corresponds to an activity. Each position vector (the time and cost of activities) leads to specific project duration and total cost, which subsequently determine the multiattribute utility value, i.e., the fitness. Note that because PSO requires only direct evaluation of the fitness, it has no restriction on the forms of activity time–cost functions.

![](/api/attachments/9V89NNE8/fulltext/images/6f55bf2afb0932c70eefd7d8b3b0d6df3e5736eb04f4f38463ba7cf936abed4b.jpg)  
Fig. 4. Pseudocode of PSO algorithm.

The proposed algorithm terminates when one of the three termination criteria is met. The simplest one keeps track of the number of iterations and stops the search after certain iterations. The second criterion measures the difference between the best and worst particle in the current iteration. When this difference becomes smaller than a specified percentage of that same difference of the initial swarm, the algorithm is terminated. The third compares the improvement made in the past iterations and terminates the search when the improvement is less than a specified threshold. In comparison, the first criterion is intuitive and guaranteed to stop the algorithm while the second and third criteria ensure convergence.

## 6. Illustrative application: concrete bridge

The proposed DSS was implemented and applied to a concrete bridge project described in [18]. Table 1 tabulates the descriptions of eight activities, their immediate predecessors, and discrete options of times and costs. The indirect cost of this project is \$500/day. If the project is completed later than 100 days, the amount of liquidated damages is \$400 per day up to 10% of the expense. If the project is completed before 80 days, the bonus is \$200 per day up to 5% of the expense.

A group of seasoned project managers are placed in different scenarios to test the proposed DSS. The project managers, with basic understanding of decision-making theory, are first introduced to project information. During interviews, we elicit individual project managers' utility functions and scaling factors of time and cost by interactively asking them to make choice between different lotteries, according to the aforementioned lottery equivalent method. Subsequently, the proposed DSS defines the multiattribute utility function and begins the optimization process.

Three scenarios are studied. The first scenario is a normal situation where no other information is given. The second scenario adds an external condition as the project is classified urgent by the local government. The third scenario is when the budget is tight and the project can be delayed without much adverse effect.

Fig. 5 illustrates the elicited utility functions of a manager. Dotted lines represent the approximated curves for time D and cost C: U(D) = 1.3097 − 0.1060exp(0.0185D) and U(C) = 1.3351 − 0.1099exp (0.0112C). The concavity of the functions, i.e., the second derivatives are negative, reflects the individual preference of the manager. The estimated scaling factors of time and cost are (0.6, 0.6) for the first scenario, (0.8, 0.3) for the second, and (0.1, 0.8) for the third. The multiattribute utility function defined by the proposed DSS is displayed as a concave surface in Fig. 6.

By contrast, Fig. 7 plots the convex multiattribute utility function of another manager on a different estimate of scaling factors: (0.8, 0.6) for the first scenario. The approximated utility functions of time and cost are U(D) = −0.9206 + 3.3183exp(−0.0094D) and U(C)=−0.8230+3.4620exp(−0.0064C), respectively.

The PSO algorithm, at the core of the proposed DSS, automatically optimizes the multiattribute utility function. Table 2 indicates the optimal activity durations and costs as well as the resulting project durations and total cost in three scenarios. It appears that the scaling factors is effective in locating the optimal project duration and total cost, taking into account project managers' individual preferences.

To investigate the impact of the diversity in individual's preferences, we further focus on the first scenario while testing three different utility functions: (1) convex on both time and cost, (2) concave on time but convex on cost, (3) convex on cost but concave on time. It is shown in Table 3 that diverse preferences strongly affect the optimal results by as much as 25% in time (58 to 73 days) and 18% in cost (\$152,600 to \$180,100).

<table><tr><td colspan="4">Activity information</td></tr><tr><td>Act. ID</td><td>Act. description</td><td>I.P.</td><td>(Time in days, cost in 1,000)</td></tr><tr><td>1</td><td>Site preparation</td><td>-</td><td>(14, $23),(20, $18),(24, $12),(28, $8),(32, $4)</td></tr><tr><td>2</td><td>Forms and rebars</td><td>1</td><td>(15, $3),(18, $2.4),(20, $1.8),(23, $1.5),(25, $1)</td></tr><tr><td>3</td><td>Excavation</td><td>1</td><td>(15, $4.5),(22, $4),(33, $3),(42, $2.2),(48, $1.9)</td></tr><tr><td>4</td><td>Precast concrete (PC)girders</td><td>1</td><td>(12, $45),(16, $35),(20, $30),(25, $27),(33, $25)</td></tr><tr><td>5</td><td>Pour foundation and piers</td><td>2, 3</td><td>(20, $20),(24, $17.5),(28, $15),(30, $10),(32, $8)</td></tr><tr><td>6</td><td>Deliver PC girders</td><td>4</td><td>(14, $36),(15, $33),(17, $28),(18, $24),(19, $23),(20, $21),(22, $18),(24, $16),(25, $14)</td></tr><tr><td>7</td><td>Erect girders</td><td>5, 6</td><td>(7, $40),(9, $32),(10, $30),(11, $28),(12, $26),(14, $25),(16, $23),(18, $21)</td></tr><tr><td>8</td><td>Finish up</td><td>7</td><td>(2, $7),(3, $6.5),(4, $6),(5, $5.5),(6, $5)</td></tr></table>

![](/api/attachments/9V89NNE8/fulltext/images/1314f2dfefbff21f3c8608a33f116d29b56dfdb5fcdab71339ed8a1f63a650dc.jpg)  
Fig. 5. Elicited utility functions.

![](/api/attachments/9V89NNE8/fulltext/images/cd4c82da824bc95a93c8c168782256b32a0b782aa6cab6e42e5d267522e5ee83.jpg)

Statistically, the proposed DSS is verified with respect to its effectiveness, efficiency, and robustness. For the solutions in Table 2, an exhaustive search concludes that there is no better solution, i.e., with a higher utility value. This proves that the proposed DSS is effective in finding the unique optimal solution. In terms of efficiency, the proposed DSS takes only 20,000 trials (20 particles for 1000 iterations), which is only 1.78% of the entire search space consisting of 1,125,000 feasible solutions. In terms of robustness, we repeat the test 5 times and the proposed DSS never miss the optimal solution.

![](/api/attachments/9V89NNE8/fulltext/images/7f4ad995c22d786459e8a9923c73da3fcb8027c39451260e58b6a1dd4cc2803d.jpg)  
Fig. 6. Concave multiattribute utility function.

Subjectively, the managers comment that the proposed DSS can capture the true decision-making mechanism behind schedule optimization. They agree that the elicitation approach in the proposed DSS is more relevant than asking them to assign arbitrary weights of time and cost. They are satisfied with the convenience of the proposed DSS in automatically defining and optimizing the multiattribute utility function.

## 7. Data set with five cases

A data set is used to demonstrate the general performance of the proposed DSS against GA. The data set includes five cases from the literature [12,17,18,20,28]. We believe the data set is adequate because it includes all types of activity time–cost functions, as listed in Table 4: linear, nonlinear (quadratic, logarithmic, and exponential), discrete, and discontinuous.

![](/api/attachments/9V89NNE8/fulltext/images/db12ba75b23422bc67e205e8dd90b0dfae0d0987b7f8bf4bf3b282a529bb2ce8.jpg)  
0.00-0.200.20-0.400.40-0.600.60-0.800.80 -1.00  
Fig. 7. Convex multiattribute utility function.

Table 2  
Optimization results varying scaling factors

<table><tr><td rowspan="2">Act. ID</td><td colspan="2">Equal emphasis (0.6, 0.6)</td><td colspan="2">Emphasis on time (0.8, 0.3)</td><td colspan="2">Emphasis on cost (0.1, 0.8)</td></tr><tr><td>Act. duration</td><td>Act. cost</td><td>Act. duration</td><td>Act. cost</td><td>Act. duration</td><td>Act. cost</td></tr><tr><td>1</td><td>14</td><td>23</td><td>14</td><td>23</td><td>32</td><td>4</td></tr><tr><td>2</td><td>15</td><td>3</td><td>15</td><td>3</td><td>18</td><td>2.4</td></tr><tr><td>3</td><td>15</td><td>4.5</td><td>15</td><td>4.5</td><td>15</td><td>4.5</td></tr><tr><td>4</td><td>20</td><td>30</td><td>16</td><td>35</td><td>25</td><td>27</td></tr><tr><td>5</td><td>30</td><td>10</td><td>20</td><td>20</td><td>32</td><td>8</td></tr><tr><td>6</td><td>25</td><td>14</td><td>19</td><td>23</td><td>25</td><td>14</td></tr><tr><td>7</td><td>12</td><td>26</td><td>9</td><td>32</td><td>12</td><td>26</td></tr><tr><td>8</td><td>2</td><td>7</td><td>2</td><td>7</td><td>2</td><td>7</td></tr><tr><td>Project duration (days)</td><td>73</td><td></td><td>60</td><td></td><td>96</td><td></td></tr><tr><td>Total cost ($1,000)</td><td>152.6</td><td></td><td>173.5</td><td></td><td>140.9</td><td></td></tr><tr><td>Direct cost</td><td>117.5</td><td></td><td>147.5</td><td></td><td>92.9</td><td></td></tr><tr><td>Indirect cost</td><td>36.5</td><td></td><td>30</td><td></td><td>48</td><td></td></tr><tr><td>Damage/bonus</td><td>-1.4</td><td></td><td>-4</td><td></td><td>0</td><td></td></tr></table>

The proposed DSS and GA are compared on the same ground: both with 40 candidate solutions evaluated for 10,000 iterations. Other parameters remain the same as in the highway maintenance project. Table 4 compares the optimized utility values and the differences in percentage. The proposed DSS outperforms GA in the first four cases (by as much as 6.04%) while both are equal in the last case. The results, again, verify the performance of the proposed DSS.

Table 3  
Optimization results varying preferences

<table><tr><td rowspan="2">Act. ID</td><td colspan="2">Convex on both time and cost</td><td colspan="2">Concave on time but convex on cost</td><td colspan="2">Convex on time but concave on cost</td></tr><tr><td>Act. duration</td><td>Act. cost</td><td>Act. duration</td><td>Act. cost</td><td>Act. duration</td><td>Act. cost</td></tr><tr><td>1</td><td>14</td><td>23</td><td>14</td><td>23</td><td>14</td><td>23</td></tr><tr><td>2</td><td>15</td><td>3</td><td>15</td><td>3</td><td>15</td><td>3</td></tr><tr><td>3</td><td>15</td><td>4.5</td><td>15</td><td>4.5</td><td>15</td><td>4.5</td></tr><tr><td>4</td><td>16</td><td>35</td><td>20</td><td>30</td><td>16</td><td>35</td></tr><tr><td>5</td><td>20</td><td>20</td><td>30</td><td>10</td><td>20</td><td>20</td></tr><tr><td>6</td><td>19</td><td>23</td><td>25</td><td>14</td><td>19</td><td>23</td></tr><tr><td>7</td><td>7</td><td>40</td><td>12</td><td>26</td><td>9</td><td>32</td></tr><tr><td>8</td><td>2</td><td>7</td><td>2</td><td>7</td><td>2</td><td>7</td></tr><tr><td>Project duration (days)</td><td>58</td><td></td><td>73</td><td></td><td>60</td><td></td></tr><tr><td>Total cost ($1,000)</td><td>180.1</td><td></td><td>152.6</td><td></td><td>173.5</td><td></td></tr><tr><td>Direct cost</td><td>155.5</td><td></td><td>117.5</td><td></td><td>147.5</td><td></td></tr><tr><td>Indirect cost</td><td>29</td><td></td><td>36.5</td><td></td><td>30</td><td></td></tr><tr><td>Damage/ bonus</td><td>-4.4</td><td></td><td>-1.4</td><td></td><td>-4</td><td></td></tr></table>

Table 4  
Comparison between the proposed DSS and GA in five cases

<table><tr><td rowspan="2">Case</td><td rowspan="2">Type of time–cost function</td><td colspan="3">Optimized utility value</td></tr><tr><td>Proposed DSS</td><td>GA</td><td>Difference in percentage</td></tr><tr><td>Moussourakis and Haksever</td><td>Discrete/piecewise linear/discontinuous</td><td>0.6413</td><td>0.6048</td><td>6.04%</td></tr><tr><td>Harris</td><td>Linear</td><td>0.6832</td><td>0.6698</td><td>2.00%</td></tr><tr><td>Yang</td><td>Nonlinear (quadratic, logarithmic, and exponential)</td><td>0.7551</td><td>0.7517</td><td>0.45%</td></tr><tr><td>Li and Love</td><td>Linear</td><td>0.9309</td><td>0.9288</td><td>0.23%</td></tr><tr><td>Liu et al.</td><td>Discrete/piecewise linear/discontinuous</td><td>0.6534</td><td>0.6534</td><td>0.00%</td></tr></table>

## 8. Real-life application: highway maintenance

A larger case is used to investigate the practicability of the proposed DSS. This real-life project is to maintain an existing highway. The work section, originally built as a dual, 7.3 meter wide, 22.8 cm thick reinforcedconcrete pavement, has developed severe step faulting at the transverse cracks in the outside lane. There are also many transverse cracks in the inside lane, but without faulting. The plan is to remove the old concrete for the first 6 km and build outside-lane concrete inlays with doweled contraction joints. Also, crews repair the inside lane with full-depth patches, dowel-bar retrofits, and diamond grinding. All the 28 activities and their original durations are shown in a Primavera bar chart in Fig. 8. The project is originally estimated to take 80 working days and cost \$1,328,650. Since each activity is associated with 3 to 5 time–cost options, the number of feasible solutions is more than $1 0 ^ { \dot { 1 } 1 }$ , which represents a large and practical search space.

The proposed DSS obtains the utility function for time D (in days) and cost C (in \$1000) as follows $U ( D ) =$ $1 . 6 2 3 2 - 0 . 2 2 8 7 \mathrm { e x p } ( 0 . 0 2 5 D )$ and $U ( C ) = 1 . 4 4 0 7 -$ $0 . 0 1 0 8 \mathrm { e x p } ( 0 . 0 0 2 8 C )$ . The owner is particularly concerned with traffic congestion caused by construction; thereby emphasis is on time: the scaling factors of time and cost are set to be (0.8, 0.6).

After 1,000 iterations, the optimal utility value converges to 0.9234, with project duration of 45 days and total cost of \$1,452,540. Note that convergence cannot guarantee global optimality; hence the solution may be near-optimal. Yet, to obtain a near-optimal solution in 73 s (in a Pentium-4 2.4 GHz machine) is a lot more practical to project managers, in a time-starved world, than spending days locating the global optimal solution. What is impressed is that the proposed DSS searches only a very small portion of the search space, in the order of 10<sup>−7</sup>, to reach the competitive solution.

![](/api/attachments/9V89NNE8/fulltext/images/c9756ac21095133680c46f93a171160e5b0cbb80f11f1ec8a8c4710e5c308890.jpg)  
Fig. 8. Bar chart of highway maintenance project.

The proposed DSS is run 11 times, of which the highest, medium, and lowest solutions are reported in Fig. 9. The proposed DSS is compared with GA that uses Palisade Evolver v4.0 with the following parameters: crossover rate = 0.8, mutation rate = 0.1, and population size =100. Both with the random generation of initial solutions, the proposed DSS is superior to GA in two perspectives. First, the proposed DSS takes only 1,000 iterations to find a much better solution than GA in 100,000 iterations. Second, the proposed DSS is more robust than GA because the range of possible solutions of the former is smaller than the latter (0.0099 versus 0.0549).

![](/api/attachments/9V89NNE8/fulltext/images/f8aaf0e773cf34f79b0ef12999078cd38c00c69ef4c26d65986a5b9db727c9f5.jpg)  
Fig. 9. Proposed DSS versus GA.

## 9. Conclusion

The present study develops a utility-based DSS to facilitate schedule optimization. The proposed DSS accounts for the diversity in preferences of decision makers and therefore can capture the true decisionmaking mechanisms. Specific steps of the proposed DSS and their theoretical grounds are presented in this paper. At the core of the proposed DSS is a new particle swarm optimization algorithm, which is used to obtain the optimal solution with respect to the maximal utility value. This study confirms that the individual's preference does indeed play an important role in decision-making of schedule optimization and therefore shall be accommodated in the analysis.

The proposed DSS has been tested in seven cases. Test results verify that the proposed DSS is effective, efficient, and robust. It has also been shown that the proposed DSS outperforms GA in a real-life project as well as examples from the literature.

Despite the focus on time and cost, the proposed DSS can be easily extended to incorporate other criteria into optimization, such as required quality and functionality or environmental influence. Quantitative measurement, however, has to be defined beforehand. In fact, the increased dimensions of attributes would make the PSO algorithm even more attractive in terms of computational efficiency, compared to traditional optimization techniques.

## Acknowledgment

The author is grateful to the financial support from National Science Council, Taiwan under Grant No. 95- 2221-E-032-052-MY3. This study has benefited from the participation of the project managers and Sun, Ying-Shyuan, who develops the Evolver model for the highway maintenance project. Appreciation also goes to the anonymous reviewers for suggesting emphasis on the critical activities during optimization, which turns out to be advantageous.

## References

[1] P.J. Angeline, Evolutionary optimization versus particle swarm optimization: philosophy and performance differences, Evolutionary Programming VII, Lecture Notes in Computer Science, Vol. 1447, Springer-Verlag, 1998, pp. 601–610.

[2] M. Clerc, J. Kennedy, The particle swarm explosion, stability, and convergence in a multidimensional complex space, IEEE Transaction on Evolutionary Computation 6 (2002) 58–73.

[3] P. De, E.J. Dunne, J.B. Ghosh, C.E. Welles, The discrete time– cost tradeoff problem revisited, European Journal of Operational Research 81 (1995) 225–238.

[4] R. de Neufville, Applied Systems Analysis: Engineering Planning and Technology Management, McGraw-Hill, New York, 1990.

[5] R.F. Deckro, J.E. Hebert, W.A. Verdini, P.H. Grimsrud, S. Venkateshwar, Nonlinear time/cost tradeoff models in project management, Computers and Industrial Engineering 28 (2) (1995) 219–229.

[6] R.C. Eberhart, J. Kennedy, A new optimizer using particle swarm theory, Proceedings of the Sixth International Symposium on Micro Machine and Human Science, Nagoya, Japan, 1995, pp. 39–43.

[7] R.C. Eberhart, Y. Shi, Comparing inertia weights and constriction factors in particle swarm optimization, Proceedings of the 2000 Congress on Evolutionary Computation, 2000, pp. 84–88.

[8] S.E. Elmaghraby, Resource allocation via dynamic programming in activity networks, European Journal of Operational Research 64 (1993) 199–215.

[9] A.P. Engelbrecht, Computational Intelligence: An Introduction, John Wiley, New York, 2002.

[10] C.W. Feng, L.Y. Liu, S.A. Burns, Using genetic algorithms to solve construction time–cost trade-off problems, Journal of Computing in Civil Engineering 11 (3) (1997) 184–189.

[11] J.W. Fondahl, A non-computer approach to the critical path method for the construction industry, Technical Report, Vol. 9, The Construction Institute, Department of Civil Engineering, Stanford University, 1961.

[12] R.B. Harris, Precedence and Arrow Networking Techniques for Construction, Wiley, New York, 1978.

[13] N.B. Jin, Y. Rahmat-Samii, Parallel particle swarm optimization and finite difference time-domain (PSO/FDTD) algorithm for multiband and wide-band patch antenna designs, IEEE Transactions on Antennas and Propagation 53 (11) (2005) 3459–3468.

[14] R. Keeney, H. Raiffa, Decisions with Multiple Objectives, Wiley, New York, 1976.

[15] J. Kennedy, R.C. Eberhart, Y. Shi, Swarm Intelligence, Morgan Kaufmann, San Francisco, 2001.

[16] S.S. Leu, C.H. Yang, GA-based multicriteria optimal model for construction scheduling, Journal of Construction Engineering and Management 125 (6) (1999) 420–427.

[17] H. Li, P.E.D. Love, Improved genetic algorithms for time–cost optimization, Journal of Construction Engineering and Management 123 (3) (1997) 233–237.

[18] L.Y. Liu, S.A. Burns, C.W. Feng, Construction time–cost tradeoff analysis using LP/IP hybrid method, Journal of Construction Engineering and Management 121 (4) (1995) 446–454.

[19] M. McCord, R. de Neufville, Lottery equivalents: reduction of the certainty effect in utility assessment, Management Science 32 (1986) 56–60.

[20] J. Moussourakis, C. Haksever, Flexible model for time–cost tradeoff problem, Journal of Construction Engineering and Management 130 (3) (2004) 307–314.

[21] R.M. Reda, R.I. Carr, Time–cost tradeoffs among related activities, Journal of Construction Engineering and Management 115 (3) (1989) 475–486

[22] J. Robinson, Y. Rahmat-Samii, Particle swarm optimization in electromagnetics, IEEE Transactions on Antennas and Propagation 52 (2) (2004) 397–407.

[23] A. Salman, I. Ahmad, S. Al-Madani, Particle swarm optimization for task assignment problem, Microprocessors and Microsystems 26 (8) (2002) 363–371.

[24] W.H. Slade, H.W. Ressom, M.T. Musavi, R.L. Miller, Inversion of ocean observations using particle swarm optimization, IEEE Transactions on Geoscience and Remote Sensing 42 (9) (2004) 915–1923.

[25] K. Veeramachaneni, T. Peram, C. Mohan, L. Osadciw, Optimization using particle swarm with near neighbor iterations, Genetic and Evolutionary Computation Conference, GECCO 2003, Chicago, USA, Lecture Notes in Computer Science, Vol. 2723, Springer-Verlag, 2003.

[26] M.P. Wachowiak, R. Smolikova, Y. Zheng, J.M. Zurada, A.S. Elmaghraby, An approach to multimodal biomedical image registration utilizing particle swarm optimization, IEEE Transactions on Evolutionary Computation 8 (3) (2004) 289–301.

[27] I.T. Yang, Impact of budget uncertainty on project time–cost tradeoff, IEEE Transactions on Engineering Management 52 (2) (2005) 167–174.

[28] I.T. Yang, Chance-constrained time–cost tradeoff analysis considering funding variability, Journal of Construction Engineering and Management 131 (9) (2005) 1002–1012.

[29] D.X.M. Zheng, S.T. Ng, M.M. Kumaraswamy, Applying Pareto ranking and niche formation to genetic algorithm-based multiobjective time–cost optimization, Journal of Construction Engineering and Management 131 (1) (2005) 81–91.

![](/api/attachments/9V89NNE8/fulltext/images/b35c415905afbfc7ff713fe04a0da097ada2213a2288fe72ee1f246a27b34d4f.jpg)

I-Tung Yang is currently an Assistant Professor in the Department of Construction Engineering at National Taiwan University of Science and Technology. He earned his Ph.D. in Civil Engineering from the University of Michigan, Ann Arbor in 2002. He also holds two master’s degrees in Industrial and Operations Engineering and Construction Engineering and Management from the University of Michigan. He has research interests in stochastic optimization, computer simulation, and soft

computing. He has served as a reviewer for 9 reputable journals and several international conferences, and on the boards of professional organizations. His publications have appeared in ASCE Construction Engineering and Management, IEEE Transactions on Engineering Management, Computer-aided Civil and Infrastructure Engineering, Construction Management and Economics, and International Journal of Project Management.
