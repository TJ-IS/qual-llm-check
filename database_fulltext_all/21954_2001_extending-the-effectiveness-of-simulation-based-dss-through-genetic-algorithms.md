---
otero_id: 21954
otero_key: "8Y8AHABY"
title: "Extending the effectiveness of simulation-based DSS through genetic algorithms"
authors: "Bijan Fazlollahi; Rustam Vahidov"
year: "2001"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00079-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Extending the effectiveness of simulation-based DSS through genetic algorithms

Bijan Fazlollahi $^{a,*}$ , Rustam Vahidov $^{b}$

$^{a}$ Department of Decision Sciences, College of Business Administration, Georgia State University, University Plaza, Atlanta, GA 30303, USA

$^{b}$ Department of Decision Sciences and MIS, John Molson School of Business, Concordia University, Montreal, Que., Canada H3G 1 M8

Received 1 March 2000; accepted 21 January 2001

## Abstract

Many real life ill-structured problems involve high uncertainty and complexity preventing application of analytical optimization techniques in building effective decision support systems (DSS). These systems may employ simulation method and search for a “good” solution through “what-if” analysis. However, this method is very time consuming and often overlooks the consideration of many promising alternative solutions. A genetic algorithm (GA) automates the search for “good” solutions by finding near-optimal solutions and increases effectiveness of DSS. This paper introduces a hybrid method based on the combination of Monte-Carlo simulation and genetic algorithms. The combined method is illustrated through application to the marketing mix problem to improve the process for searching and evaluating alternatives for decisional support. The paper compares two methods: MC and MC + GA. It also discusses ways for dealing with crisp and soft constraints contained in the example problem. A business game environment is chosen for experiments. The results of the experiments show that the GA-based approach outperforms human “what-if” method in terms of effectiveness and efficiency. © 2001 Elsevier Science B.V. All rights reserved.

Keywords: Decision support systems; Simulation; Genetic algorithms; Fuzzy sets; Marketing mix management

## 1. Introduction

Many real-life problems involve complexity, uncertainty, hard and soft constraints, as well as multiple and often conflicting objectives. Simulation models (e.g., Monte-Carlo simulation) may be the only legitimate choice for a decision maker to approach these problems [40]. In simulation models, the decision maker decides which promising alternatives to evaluate and performs “what-if” analysis $[27]$ . Decision support systems (DSS) often provide only the means for mechanical calculation for evaluating alternative solutions for these problems in terms of feasibility and achievement of objectives. Little or no support is provided on which “what-ifs” to try in search for promising solutions and when to stop the search, or how to ensure the feasibility of trial solutions. Generally, as the problem complexities and uncertainties increase it becomes even more difficult for the decision maker to generate feasible promising alternatives that allow for uncertainties and do not violate the constraints. Consequently, the decision makers is likely to “satisfice” and thus avoid an exhaustive, time consuming, and occasionally futile search to discover and evaluate the optimal choice.

An effective DSS with increased participation in the decision process is needed to avoid the above shortcomings. The objective of such DSS is to help search for feasible “good” solutions, stop the search when benefits becomes negligible, and reduce the effect of user cognitive biases.

One way to improve simulation-based DSS is through the use of genetic algorithms. Genetic algorithms (GA) $[8,13,16,17,28]$ apply the principles of biological evolution to the process of generating and improving a set of candidate solutions to a problem. Such search incorporates direction and randomness via the use of genetic operators for determining a set of “good” potential solutions. Monte-Carlo simulations allow modeling of complex uncertain response functions with little need for unrealistic simplifying assumptions. GA, on the other hand, are capable of finding near-optimal solutions of such functions. Combination of GA and simulations allows us to search for acceptable solutions without unnecessary simplifications required by traditional optimization models.

The purpose of this paper is to introduce the use of Monte-Carlo + GA-based hybrid method in a DSS framework for complex and uncertain problems and show how GA offsets the shortcomings of Monte-Carlo simulations alone. The method is illustrated through the application to the problem of managing marketing mix in an uncertain environment with both crisp and soft constraints. Furthermore, the effectiveness of the hybrid method is shown through experiments in a simulated business environment, where the problem is to find the values for price, advertising expenditures, and production volumes for multiple products that maximize an objective function (the expected marketing profit and the future value of inventory). There are both “crisp” and “soft” constraints in this problem.

## 2. Related work

DSS has been one of the most popular research topics in Information Systems Research [6,23].

Presently, there are no strong theory-based methods for relating DSS features and their effectiveness, and the issues of DSS design have not been adequately addressed $[36]$ . Nevertheless, there are several research results that may help in pointing the way on how to increase the effectiveness of simulation model-based DSS. More effective DSS are implied through features that enable increased DSS participation in the decision process, active participation $[1,26,30,32]$ , and balanced restrictiveness.

Alter [2] developed a taxonomy that distinguishes between the DSS on the basis of level of participation in the decision, i.e., the degree to which the system determines the decision. Alter's taxonomy, although over 25 years old, is still the only taxonomy that systematically distinguishes between DSS. In his classification representational models, optimization models, and suggestion systems are in the order from a low to high degree of system participation in the decision. Moving from the representational model type of DSS to an optimization type DSS is equivalent to climbing Alter's taxonomy ladder towards higher DSS participation in determining the decision.

Optimization models establish enough structure to use models as analysis tools. Here the model is in control of the search process and it determines which feasible candidate decisions to evaluate on the way to obtaining optimal solutions (assuming it utilizes an iterative optimization procedure). Elevation from the representational models to the optimization models may result from discovering additional structure in the decision task and assigning more activities to DSS. All DSS require some human judgment in performing the decision task $[20,25]$ . Increasing task structure implies less need for human judgment. Here the increased task structure is achieved through coupling of Monte-Carlo simulations with GA.

DSS effectiveness may be increased through active participation of DSS in the decision-making process. Traditional DSS offer a weak form of support, where the DSS user is assumed to have full knowledge of a system's capabilities and take the initiative in human-computer interaction. In this setup, the potential power of human-computer collaboration is significantly underutilized. Using GA, the DSS may participate more actively in the decision-making process by taking the initiative in search for promising solutions. Mirchandani and Pakath discuss a GA-driven adaptive

DSS as an example of making decision support more active.

The concept of “restrictiveness” may also guide how to increase the effectiveness of simulation model-based DSS through improved DSS features. System restrictiveness is the degree to which, and manner in which, a DSS limits its users’ decision-making processes to a subset of all possible processes. It is a quality but it is not measurable. A DSS with just the right amount of restrictiveness may lead to better decisions. A DSS that limits the available processes to potentially superior prescriptive and normative techniques is more restrictive and may provide more effective support. However, a DSS which reduces the need for simplifying heuristics and the effects of their “systematic cognitive biases”, expands a decision maker’s information processing capabilities and therefore is less restrictive and may also provide more effective support.

The conceptual model of restrictiveness does not specify the methodology for increasing restrictiveness. In particular, how would one go about manipulating restrictiveness in simulation-based DSS? One practical way to achieve this is to build effective simulation-based DSS through increasing restrictiveness via genetic algorithms that can perform the search for promising alternatives, thus eliminating the necessity for manual search and restricting the user to the analysis rather than the search. The GA also reduces the cognitive bias for “satisficing” and the strategy of “anchor and adjust” which tend to settle for local optima. Also, hard and soft constraints may be incorporated in the GA component to further restrict the system and ensure the generation of feasible solutions.

There have been several attempts to incorporate GA into DSS. Wang and Leu $[41,42]$ used GA for adaptive selection of rules for the DSS for trading at Taiwan stock market. They compared the performance of this adaptive design to that of the stationary rules to show that the former is better. Balakrishnan and Jacob $[4]$ incorporate different techniques, including complete enumeration, heuristic dynamic programming and GA in their DSS for product design. The approach increases the confidence in the quality of decisions thus promising more effective decisions. These applications are encouraging contributions to the field of DSS. However, further investigation into the use of GA in DSS for problems with uncertainty and various types of constraints was needed.

Several research results report the application of the hybrid method to searching for near-optimal solutions. An example of finance application of Monte-Carlo in combination with GA includes finding optimal hedging strategies for trading options, where simulations were used to model the uncertain market factors $[39]$ . In this application, the GA — generated hedging strategies were better than those generated by the traditional delta rule. However, this application did not incorporate constraints. Examples of applications of Monte-Carlo in combination with GA for engineering problems include optimal scheduling for flexible manufacturing systems $[31]$ , optimal scheduling of hot parts operating $[34]$ , and optimal tolerance allotment $[22]$ . Some of these problems incorporated hard or crisp constraints; none considered the soft type of constraints.

## 3. The general model of the problem

Gatignon [14] defines the general model for marketing mix as follows:

$$
y = f (X, Z, \beta , \gamma , \varepsilon),\tag{1}
$$

where y is a measure of market response (i.e., sales, market share, profit), X a set of marketing variables, Z a set of environmental variables, $\beta$ the response parameters of marketing variables; $\gamma$ the response parameters of environmental variables, and $\varepsilon$ the disturbance term. In general, the functional form of the model is non-linear, and linearizing the model would make it inappropriate in most marketing contexts because of simplifying assumptions [15].

Different techniques for making marketing mix decisions that will optimize the response function have been proposed. However, the inherent simplifying assumptions of these techniques limit their usefulness in real situations. The Dorfman–Steiner theorem specifies the conditions for the optimality of marketing mix, which includes values of elasticities $[7]$ . Similar conditions are specified by Lambin $[21]$ . The use of these results, however, is hampered by the difficulty in estimating the exact values of elasticities. Moreover, the techniques require specifications of quantities of products sold and these cannot be accurately estimated.

A number of marketing and joint marketing–production decision-making models emerged from the OR/MS area. In particular, the mathematical programming models were reviewed by Rangaswamy $[33]$ , and Eliashberg and Steinberg $[9]$ . These models represent marketing problems in terms of objective function and a number of constraints. However, the use of mathematical programming tools becomes more difficult as the complexity of the objective function increases (e.g., it becomes non-linear, non-differentiable, and uncertain). Moreover, these tools are inappropriate for objective functions that have local minima.

The marketing mix problem belongs to a class of problems that, due to inherent complexity and uncertainty, cannot be adequately solved by traditional optimization techniques. In highly competitive and uncertain dynamic environments, external factors, such as the state of the economy, consumer preferences, as well as strategies and tactics of competing firms determine the dynamics of the market. In making marketing mix decisions on price, advertising expenses, quantity and other variables for multiple products, the firm must consider various constraints and uncertain environmental and competitive factors. In general, the objective function may be complex, non-differentiable, and uncertain. The uncertainty may arise from ignorance about competitor actions and other environmental factors. Constraints may include both crisp and “soft”, or “fuzzy” ones. These characteristics of the problem prohibit the use of the traditional calculus-based and mathematical programming techniques.

Both Gatignon and Rangaswamy stress the use of simulation models as more appropriate for complex market response, than are traditional optimization tools. For complex market response patterns, the simulation models seem to be the best tools to analyze different alternatives. These models allow the decision maker to do “what-if” analysis and see how the key criteria change in response to changes in the input variables.

Simulation method overcomes the problems associated with most optimization methods: unrealistic assumptions, failure to deal with local optima, uncertainties, and non-differentiability of the objective function. The drawback of the simulation-based approach is that the user may spend significant time and effort in manually optimizing the solution and fail to consider many promising alternatives. This disadvantage grows exponentially as the number of decision variables increase, since each new variable leads to a considerably larger space of possible combinations.

Genetic algorithms (GA) may be used to identify a set of “good” alternatives for the marketing mix problem. They are new optimization tools that search for solutions based on the principles of evolution $[12]$ . The technique is applicable to a wide class of problems, and GA are capable of dealing with more complex response functions than traditional optimization approaches. The potential applications of GA to marketing optimization problems are consumer behavior; segmentation, targeting and positioning, managing the marketing mix; and strategic marketing. Hurley et al. $[19]$ discussed applications to site location analysis and segmentation (product–market structure) in detail. Terano and Ishino $[37,38]$ used GA for extracting marketing decision rules from questionnaire.

A number of applications of GA to economic problems are reported in the literature including those reported by Holland and Miller $[18]$ . Arifovic $[3]$ reported application of GA to setting the quantities of a product in an environment where multiple firms competed in a market for a single product. The firms were price-takers, and the production decisions were made before observing the market price. Also, Midgley et al. $[29]$ reported an application of GA to the pricing problem. They used GA to determine optimal pricing for three major coffee brands in a regional US coffee market. The GA considered only four levels for price of coffee.

## 4. Genetic algorithms

Holland and coworkers have developed GA as a principally new approach in optimization theory. The idea behind it is borrowed from the evolution of living organisms. GA use selection, crossover, and mutation operators to breed good solutions. “Goodness” of the solutions is measured by so-called “fitness function”. This is based on the objective function of the problem and must be non-negative. GA is less demanding than “strong” optimization methods, as there is no need for calculating derivatives or performing complex mathematical transformations. Moreover, the probability of being trapped by local optima is comparatively low (though it still not zero). Local optima are the “curse” of local search methods (e.g., gradient ascent), because these methods lead to the nearest local optimal point, which might not be the best globally. Since GA evolve the population of solutions, this reduces the chance of being trapped in local minima.

There are a number of ways to deal with constraints using GA. The most widely used include penalty functions, repair algorithms, and special design of genetic operators. In our opinion, a good way to handle crisp constraints is to avoid generation of invalid solutions, wherever possible, through the careful design of genetic operators. In case of soft constraints, where small violations do not lead to invalid solutions in a strict sense, penalty functions can be utilized.

## 5. Monte-Carlo plus GA-based hybrid DSS

The overall architecture of the marketing DSS based on Monte-Carlo simulations plus GA is shown in Fig. 1. The GA module overcomes the problem of manual search for promising alternatives. It generates sets of candidate solutions, which are entered into the simulation module for evaluation. The simulation module then produces the outputs based on the known facts, estimates, and candidate solutions. The output of the model is finally used to evaluate the submitted candidate solutions.

![](/api/attachments/8Y8AHABY/fulltext/images/27d8592af39d6190ef2739e5374a9951e1e2bbee742c4b02e19b155e1ee8d1f5.jpg)  
Fig. 1. Structure of the GA-based marketing DSS.

A number of Monte-Carlo simulations are performed at each evolution step for each chromosome in the population to evaluate their fitness. The simulation module uses statistical models to calculate the outputs and returns average results of simulations. The database module holds the historical facts, estimates, and parameters of the models, as well as the parameters of GA. The database also keeps track of the evolution history, last updated genetic pool, the values of the best chromosome, and other useful information.

The algorithm proceeds as follows:

1. The system updates the database with the relevant information (e.g., past facts, existing constraints, etc.) in interaction with the user.

2. The user specifies his/her estimates concerning uncertain factors (e.g., future actions of competitors).

3. The GA starts its work in interaction with the Monte-Carlo simulation module as follows:

3.1. An initial population of candidate solutions is randomly generated.

3.2. The fitness value is calculated for each chromosome (potential solution) in the population:

\- Each is entered as a candidate solution to the simulation module.

\- The module performs a number of Monte-Carlo simulations and returns the results to the GA module.

\- The GA module computes the fitness value for a chromosome based on the output of the simulations.

3.3. The selection operator generates a new population from the old one based on the fitness values of its chromosomes.

3.4. A crossover operator is applied to the population.

3.5. A mutation operator is applied to the population.

3.6. The fitness value is calculated for each chromosome in the population (as in step (3.2)).

3.7. If the stopping criteria are met, then the process ends; otherwise it returns to step (3.3).

4. The results of GA, including the last generated pool of candidate solutions, the history of evolution of solutions, and other information is written to the database. The best generated solution is presented to the user.

The user can request other solutions from the database. He or she can then modify the proposed solution and directly interact with the Monte-Carlo simulation module to perform refining “what-if” analysis. The user can also change his/her estimates and re-run the GA to do sensitivity analysis and see how sensitive the solution is to the estimates of uncertain factors.

## 6. The experiments

For our experiments we used the SIMQ game, which is a system that simulates a hypothetical business environment; in this, a number of firms compete for three products $(x, y, \text{and } z)$ in an olygopolistic market [5,35]. A team of students who generally decide to pursue profitability and market share goals, manages each firm. The teams make marketing, production, and financial decisions each quarter using DSS incorporating accounting and representational models. The decisions include the mix and amounts of goods to produce, pricing, advertising expenses, and production capacity. The DSS for marketing decisions incorporates a Monte-Carlo simulation model.

We formulate the general marketing mix problem as follows:

Optimize:

$$
y = f (X, Z, \beta , \gamma).\tag{2}
$$

Subject to constraints:

$$
g _ {i} (X, Z) \in \Omega_ {i},\tag{3}
$$

where the parameters and variables in (2) and (3) were described previously, $g_{i}$ and $\Omega_{i}$ describe the ith constraint on the values of marketing variables in general form.

In the context of SIMQ game, the objective is to maximize the overall marketing value, which is aggregation of the individual marketing values for the three products:

$$
\mathrm{MV} = \sum_ {i \in \{x, y, z \}} \mathrm{MV} _ {i}.\tag{4}
$$

Subject to:

$$
\sum_ {i \in \{x, y, z \}} Q _ {i} \leq \text { Capacity },\tag{5}
$$

$$
\text { Supply } _ {i} \approx \text { Demand } _ {i}, \quad i \in \{x, y, z \}.\tag{6}
$$

The objective function (4) is the total marketing value of the mix. There are crisp and soft constraints in the problem. Crisp constraint (5) limits the total production volume for three products by the capacity of firm's facilities. Soft constraints (6) require the probabilities of stocking out for the three products to be away from 0 and 1 to avoid large inventory buildups as well as shortages in delivering the products. In other words, soft constraints require that the supply should meet the demand to some extent.

Individual marketing values are affected by the decisions of the firm as well as external (possibly uncertain) factors:

$$
\begin{array}{l} \mathrm{MV} _ {i} = \mathrm{MV} _ {i} (P _ {i}, A _ {i}, P _ {i} ^ {\mathrm{c}}, A _ {i} ^ {\mathrm{c}}, C _ {i}, Q _ {i}, V _ {i}, T _ {i}), \\ i \in \{x, y, z \}, \end{array}
$$

where P is the price of a product, A the advertising expenses, $P^{c}$ the average price charged by competitors, $A^{c}$ the average competitor advertising, C the cost of a product, Q the quantity produced, V the future value (estimated value of the product in the time frame beyond the current planning horizon) of a product, and T reflects the temporal pattern of dynamics of the demand for the product.

The expected marketing value (MV) represents the effectiveness of marketing decisions. It is based on the estimate of profit and future value of inventory for a given set of potential decisions.

The expected profit and inventory level depends on the estimate of sales, which, in turn depends on the estimate of demand. If demand is more than the quantity produced, then all the produced goods will be sold, otherwise, the level of demand will determine the sales volume $[24]$ :

$$
\begin{array}{c} \text {   If   } D _ {i} \geq Q _ {i}, \text {   Then   } S _ {i} = Q _ {i}, I _ {i} = 0, \\ \text {   Else   } S _ {i} = D _ {i}, I _ {i} = Q _ {i} - D _ {i}. \end{array}
$$

Here $D$ is demand, $S$ the sales, $I$ the inventory level, and $Q$ the quantity produced. The demand is influenced both by the firm's decisions and the decisions of competing firms. Uncertainty arises from the ignorance of competitor decisions on price and advertising, as well as the uncertainty inherent in demand forecasting.

Summarizing the above, the problem is defined as: find such a combination of decision variables $(P, A, Q)$ that improves the total MV (4), subject to constraints (5) and (6). Making effective decisions is difficult: one has to consider all of the three products jointly in order to manage them properly. Moreover, the situation is complicated by uncertainties involved in competitors' decisions on price and advertising.

## 7. Solving the marketing mix problem with Monte-Carlo simulation plus “what-if”

Monte-Carlo simulations are used to deal with the uncertainty in the described problem. The objective is to predict the level of the MV for a given set of decisions and environmental variables. Different sets of variables are involved in the simulations. The decision variables include: the quantities of products to produce, prices, and advertising expenses. The decision maker has control over the decision variables. The known environmental variables include historical industry and firm's prices, advertising expenses, R&D expenditures, and market share data. The uncertain variables include average industry price, advertising expenses, and R&D expenditures for the current quarter.

Basically, the uncertainty stems from lack of knowledge about competitors' future actions. Although the exact competitors' behavior can hardly be determined, judgment, as well as business intelligence information may be used $[10,11]$ to estimate the approximate intentions of competitors. Here, uncertainties are represented as triangular distributions with user-defined ranges and peak points for average industry price, advertising expenses, and R&D expenditures. During Monte-Carlo simulations the values for average industry price, advertising expenses, and R&D expenditures are generated from user-specified triangular distributions. The results from a number of runs, with different values for uncertain variables, are averaged. Also, the probability of stocking out is estimated as the ratio of cases when the demand exceeded the supply to the total number of cases.

In evaluating different decisions, the user avoids both the cases when the probability of stocking out is close to zero (zero inventory), or one (excessive inventory). In other words, the desired situation is where demand is met to some extent by supply. The good solutions would also generate higher levels of MV without violating the capacity constraint; i.e., the MV is the objective function. The general strategy for the user is to determine the quantities for the three products so that the probabilities of stockout are far from zero and one, and then perform local search for better prices and advertising expenditures until no further improvement is made. The user can then try other set of quantities.

## 8. Solving the marketing mix problem: integration of Monte-Carlo simulation with GA and fuzzy set concepts

Balakrishnan and Jacob point out that the ability to generate a set of alternative solutions from which a decision maker can make a choice is a strong advantage of GA. Here we use both Monte-Carlo and GA.

## 8.1. Solution representation

Each chromosome represents the set of decision variables. We included into consideration nine variables: quantities to produce, prices, and advertising expenses for three hypothetical products X, Y, and Z. We employed binary representation for chromosome encoding of our decision variables, 10 binary digits per variable, with the total length of the chromosomes being 90.

The structure of a chromosome is:

$$
(P _ {x} ^ {\mathrm{b}}, P _ {y} ^ {\mathrm{b}}, P _ {z} ^ {\mathrm{b}}, A _ {x} ^ {\mathrm{b}}, A _ {y} ^ {\mathrm{b}}, A _ {z} ^ {\mathrm{b}}, Q _ {x / y} ^ {\mathrm{b}}, Q _ {x / z} ^ {\mathrm{b}}, Q ^ {\mathrm{b}}).
$$

Here, $P_{x}^{b}, P_{y}^{b}, P_{z}^{b}$ are binary string representations of prices for products x, y, and z; $A_{x}^{b}, A_{y}^{b}, A_{z}^{b}$ are those for advertising expenditures; and $Q_{x/y}^{b}, Q_{x/z}^{b}, Q^{b}$ are those encoding the mix of the products and the total quantity of them. The conversion from the binary representation is made using the upper and lower limits for the variables shown in Table 1. For example, the following partial chromosome

(0000111110 0100000110 0100111010

$$
0 1 0 1 1 0 0 1 0 1 \quad 0 0 0 0 0 0 1 0 0 0 \quad 1 1 0 0 0 0 0 0 0 1 \quad \dots)
$$

Table 1
Ranges for variables

<table><tr><td rowspan="2"></td><td colspan="3">Product</td></tr><tr><td>X</td><td>Y</td><td>Z</td></tr><tr><td>Min price ($)</td><td>310</td><td>410</td><td>250</td></tr><tr><td>Max price $)</td><td>340</td><td>450</td><td>275</td></tr><tr><td>Min advertising ($)</td><td>70000</td><td>40000</td><td>20000</td></tr><tr><td>Max advertising ($)</td><td>120000</td><td>100000</td><td>80000</td></tr></table>

translates into the real-valued vector:

$$
(3 2 4. 5 5; 4 2 5. 0 9; 2 5 9. 0 4; 1 0 2, 5 5 1; 4 3, 7 5 4; 5 0, 2 0 5; \dots)
$$

representing the set of decisions that implies the price for product x be \$324.55; advertising expenditures of \$102,551, etc. In other words, the floating point chromosome explicitly represents the set of possible marketing decisions. The total quantity of products is restricted to 13,000.

## 8.2. Objective function

MV (5) is the objective function and the basis for constructing the fitness function for GA. A set of potential decisions is input to the Monte-Carlo simulation model along with the values of environmental variables. The Monte-Carlo simulation model calculates the average marketing value of the given set of decisions. In solving the marketing mix problem we are not concerned with mathematically exact location of the optimum, rather, we are trying to locate close-to-optimal solutions. GA can operate in noisy environments, therefore, use of stochastic models, such as Monte-Carlo simulation in combination with GA is appropriate.

## 8.3. Handling constraints

The capacity of firm's facilities limits the total quantity of products to be produced. The capacity requirement dictates the necessity of developing the way to handle constraints in GA. The crisp constraint is handled by careful implementation of the genetic operators. Instead of explicitly generating the quantities for the three products, we encode the product mix by taking one product (in our case the product $x$ ) as the base product and encoding the quantities of others through the ratio of the quantity of the base product to them. The numbers $Q_{x/y}^{b}$ and $Q_{x/z}^{b}$ are actually the angles representing the mix of products. The tangent of these angles gives the actual ratio of product x to the products y and z. Use of angles instead of actual ratios is preferred, since we can control the ranges for these angles easier than those for the ratios. The last substring $Q^{b}$ represents the total actual quantity of the three products and is limited by the capacity limit of 13,000. Symbolically,

$$
\begin{array}{l} \frac {Q _ {x}}{Q _ {y}} = \tan Q _ {x / y}, \quad \frac {Q _ {x}}{Q _ {z}} = \tan Q _ {x / z}, \\ Q _ {x} + Q _ {y} + Q _ {z} = Q, \end{array}
$$

where $Q_{x/y}$ , $Q_{x/z}$ , Q are the real-number translations of the binary $Q_{x/y}^{b}$ , $Q_{x/z}^{b}$ , $Q^{b}$ , and $Q_{x}$ , $Q_{y}$ , $Q_{z}$ are the quantities of products x, y, and z. From the above formulas we can derive the quantities of the products as follows:

$$
\begin{array}{l} Q _ {x} = \frac {Q}{1 + (1 / \tan Q _ {x / y}) + (1 / \tan Q _ {x / z})}, \\ Q _ {y} = \frac {Q _ {x}}{\tan Q _ {x / y}}, \quad Q _ {z} = \frac {Q _ {x}}{\tan Q _ {x / z}}. \end{array}
$$

This method guarantees that no invalid chromosomes (infeasible solutions) will be generated as a result of genetic operations.

The requirement that the supply to be close to the demand (7), translates into the “soft” or “fuzzy” constraint of probabilities of stocking out being away from zero and one. Here the term “fuzzy” implies that there is no strict constraint on the range of the probability of stocking out. Rather, it is transformed into a mathematical form from a linguistic definition, such as “the supply should be close to the estimated demand”. Trying to make supply exactly meet the demand does not make much sense, because the demand cannot be predicted with accuracy.

Fuzzy Sets Theory, introduced by Zadeh [43] helps to deal with situations similar to this. We used the membership function for the term “the supply is not close to demand”, defined as follows:

$$
\mu_ {i} = \left\{ \begin{array}{l l} \tan h (r _ {i} \cdot (| D _ {i} - Q _ {i} | - \vartheta_ {i})) & \text { if } | Q _ {i} - Q _ {i} | \geq \vartheta_ {i}, \\ 0, & \text { otherwise }. \end{array} \right.\tag{7}
$$

![](/api/attachments/8Y8AHABY/fulltext/images/c1519363da5b13eec73c18adac2ed17c2b9272e29419798f40f489bfb495cf20.jpg)

|D-Q|

Fig. 2. The shape of membership function.

Here, $\mu_{i}$ is the membership function for ith product, $D_{i}$ the demand for ith product, $Q_{i}$ the quantity produced, $\vartheta_{i}$ the allowance for a gap between the demand and supply, i.e., considered to be insignificant, and $r_{i}$ the coefficient that defines the steepness of the membership function beyond the range defined by the allowance. The shape of the membership function is represented graphically in Fig. 2.

One way of dealing with constraints in GA employs penalty functions. If a candidate solution violates a constraint, then “penalty” is applied to the fitness function by decreasing its value for the corresponding chromosome. We incorporated the soft constraint based on the membership function (7) with the adjusted steepness coefficient $r_{i}^{\prime}$ as a penalty in the following way:

$$
\text { fitness } = \sum_ {i \in \{x, y, z \}} \mathrm{MV} _ {i} - \sum_ {i \in \{x, y, z \}} l _ {i} \cdot \mu_ {i} ^ {\prime}.\tag{8}
$$

Here, $MV_{i}$ is the marketing value of the ith product, $\mu_{i}^{\prime}$ is derived from $\mu_{i}$ by using the adjusted coefficient of steepness $r_{i}^{\prime}$ instead of $r_{i}$ , and $l_{i}$ is the maximum penalty that can be subtracted from the solution's marketing value for violating the constraint on supply being close to demand. The reason for using the adjusted shape of the original membership function is to be able to control the convergence of the GA. If the gap between demand and supply is within a pre-set interval, no penalty is imposed. As the gap increases, the penalty starts rising according to the tangent curve. There is an upper limit for a penalty since the membership function cannot be higher than one. Setting the parameter $r_{i}^{\prime}$ at low level makes the curve close to linear. It is important to make the curve smooth enough, so, that the algorithm “feels” the direction in which the penalty is decreased. The values of the parameters $l_{i}$ , $r_{i}$ , $\vartheta_{i}$ were set to 20,000; 0.00001; and 20, respectively, for all three products. These values for parameters were found empirically.

Although, in many cases the penalty function approach does not produce good results, since it allows the presence of many invalid chromosomes in the population, in our case, because of the nature of soft constraint (6), such chromosomes are not invalid but are undesirable.

It may appear that the objective/fitness function is linear. However, the formulas only show the aggregation of different marketing values. The calculation of individual marketing values involves combined use of complex non-linear discontinuous functions (since there are decision rules involved to determine the sales level) and Monte-Carlo simulations. Hence, the relationship between the decision variables and the value of fitness function is complex and uncertain.

## 9. Results of empirical test of the hybrid DSS

We used a traditional DSS based on a Monte-Carlo simulation model and a hybrid DSS based on GA plus Monte-Carlo for our experiments.

We conducted experiments to test the performance of a Monte-Carlo + GA-based system as compared to that of a Monte-Carlo + human “what-if”. The subjects included 25 upper division business students taking a course in generalized modeling techniques. We feel that these subjects are appropriate for the experiment, because they were knowledgeable of the business environment and modeling techniques, and, in particular, they were exposed to the use of Monte-Carlo simulation models in the course they were taking. All the subjects used the Monte-Carlo-based simulation DSS. The subjects had been told how to perform simulations. Their goal was to maximize the total MV of their decisions, while observing the crisp and soft constraints.

We ran GA 25 times, for 100 and 1000 generations. In each run GA produced slightly different results, because it uses stochastic component in the search process. The parameters are summarized in Table 2. We experimented with different rates for genetic operators and finally chose those ones. Fig. 3 shows a typical example of the dynamics of the fitness function for 1000 generations of GA.

Table 2
Parameters of the GA

<table><tr><td>Representation</td><td>Binary</td></tr><tr><td>Chromosome length</td><td>90</td></tr><tr><td>Sampling</td><td>Elitist</td></tr><tr><td>Population size</td><td>50</td></tr><tr><td>Crossover rate</td><td>0.7</td></tr><tr><td>Mutation rate</td><td>0.007</td></tr><tr><td>Number of generations</td><td>100; 1000</td></tr></table>

The performance of the human “what-if” was compared with the performance of the GA-based system. We measured the performance of both approaches in terms of achieved MV, estimated probabilities of stocking out, and time elapsed. Table 3 compares the performance of the two approaches in terms of MV achieved.

The results indicate that Monte-Carlo + GA outperformed the Monte-Carlo + “what-if” approach after 100 and 1000 generations. The one-tail heteroskedastic (since the variances of MV are obviously unequal for the two methods) t-tests for the difference of the means between the Monte-Carlo + “what-if” and both 100 and 1000 generations GA combined with Monte-Carlo was significant (see Table 3).

Table 4 reports the probabilities of stocking out for the three products. The standard deviation of these probabilities is an important measure of the performance, because even if the averages of the reported probabilities are neither close to zero, nor to one, their spread across the experiments may be wide. Therefore, low standard deviation would be the desired characteristic of these probabilities. In general, the standard deviations of the probabilities of stocking out for each of the three products was significantly lower for the decisions produced by GA, as confirmed by the F-test (see the p-values in Table 4). An exception is the probability of stockout of x for 100-iterations GA, where the p-value for the difference in standard deviations between the GA and human “what-if” is 0.053, and is, hence not significant at 0.05 level, but significant at 0.1 level.

The average time spent by humans was 75 min. It took approximately 15 s for GA to evolve 100 generations and 2.5 min to run 1000 generations.

![](/api/attachments/8Y8AHABY/fulltext/images/12f2c345e1c619824a1c0141fd64232842f1c509ab3612885fbc3506351d3c56.jpg)  
Fig. 3. A typical example of dynamics of evolution of population of marketing mix decisions.

Comparison of marketing values produced by MC + GA vs. MC + human “what-if” (The figures in the table are based on simulations and hence do not reflect the accuracy of real world measures)

<table><tr><td>Method</td><td>Average</td><td>S.D.</td><td>Median</td><td>p-Value</td></tr><tr><td>MC + “what-if”</td><td>1117173</td><td>41650</td><td>1133910</td><td>N/A</td></tr><tr><td>MC + GA (100 iterations)</td><td>1156956</td><td>11675</td><td>1158122</td><td>0.000042</td></tr><tr><td>MC + GA (1000 iterations)</td><td>1164106</td><td>6614</td><td>1164944</td><td>0.000004</td></tr></table>

Comparison of probabilities of stocking out produced by MC + GA vs. MC + human “what-if”

<table><tr><td rowspan="2">Method</td><td colspan="3">Probability of stockout for x</td><td colspan="3">Probability of stockout for y</td><td colspan="3">Probability of stockout for z</td></tr><tr><td>Average</td><td>S.D.</td><td>p-Value</td><td>Average</td><td>S.D.</td><td>p-Value</td><td>Average</td><td>S.D.</td><td>p-Value</td></tr><tr><td>MC + “what-if”</td><td>0.361</td><td>0.304</td><td>N/A</td><td>0.300</td><td>0.247</td><td>N/A</td><td>0.386</td><td>0.264</td><td>N/A</td></tr><tr><td>MC + GA(100)</td><td>0.378</td><td>0.104</td><td>0.000</td><td>0.272</td><td>0.177</td><td>0.053</td><td>0.389</td><td>0.055</td><td>0.000</td></tr><tr><td>MC + GA(1000)</td><td>0.403</td><td>0.009</td><td>0.000</td><td>0.269</td><td>0.032</td><td>0.000</td><td>0.384</td><td>0.029</td><td>0.000</td></tr></table>

The most common comments reported by the subjects included the difficulty of making joint decisions on multiple products while watching not to violate the crisp and soft constraints, as well as little guidance concerning the direction of the search. The results suggest that the method that combines genetic algorithms with simulation models produces better decisions in terms of marketing value and the probabilities of stocking out for the products than human “what-if”. Furthermore, the time spent on search for “good” decisions is significantly reduced.

## 10. Summary and conclusion

Many real life problems require consideration of complexities and uncertainties in decision-making. Addressing the requirements led us to incorporate simulation models (e.g., Monte-Carlo) within representational model-based DSS. The objective was to improve the effectiveness of Monte-Carlo-based DSS. This was achieved by increasing restrictiveness, proactiveness, and task structure through employment of a hybrid simulation model and GA-based method.

We have defined the general architecture and principles for the GA + simulations-based DSS. A marketing mix problem was chosen for the illustration of the approach. A business game environment was used for the experimental comparison of the performance of our hybrid approach with the performance of a simulation-based approach. The experiments have shown the superiority of Monte-Carlo + GA over Monte-Carlo + human “what-if” search as indicated by:

\- higher performance criterion “MV” for the MC + GA approach;

\- ability to stay within feasible solutions region;

\- efficient search compared to human “what-if”; and

\- expanding the limit of “bounded rationality” overcoming human information processing limitations when facing complex situations. The subjects experienced difficulty in making joint decisions on multiple variables.

A limitation of this study is the use of students as subjects in the experiments. However, the advantage of using them was that they were knowledgeable about basic business administration concepts and modeling techniques. It would be difficult to have a sufficient number of practitioners with similar knowledge for experiments.

One implication of this work is the possibility of the use of genetic algorithms as a vehicle for conducting DSS research. Research in restrictiveness theory may be advanced using GA to manipulate system restrictiveness by limiting the user's activities in such a manner that increases the overall effectiveness and efficiency of the decisions. GA can also be used to make a DSS more active by enabling generation of promising alternatives. Finally, GA can serve as a vehicle to increase the task structure in the presence of uncertainty and complexity through employing global search for near-optimal solutions.

## References

[1] A.A. Ahgehrn, Computers that criticize you: stimulus-based decision support systems, Interfaces 23 (3), 1991, pp. 3–16.

[2] S.A. Alter, Taxonomy of decision support systems, Sloan Mgmt. Rev. 19 (1), (Fall 1977) 39–56.

[3] J. Arifovic, Genetic algorithm learning and the Cobweb model, Journal of Economic Dynamics and Control 18 (1), 1994, pp. 3–28.

[4] P.V. Balakrishnan, V.S. Jacob, Triangulation in decision support systems: algorithms for product design, Decision Support Systems 14 (4), 1995, pp. 313–327.

[5] G. Churchill, Applied Decision Sciences, Alphagraphics, Atlanta, 1992.

[6] E. Claver, R. Gonzales, J. Llopis, An analysis of research in information systems (1981–1997), Information and Management 37, 2000, pp. 181–195.

[7] R. Dorfman, P.O. Steiner, Optimal advertising and optimal quality, American Economic Review 44, 1954, pp. 826–836.

[8] R.E. Dorsey, W.J. Mayer, Genetic algorithms for estimation problems with multiple optima, non-differentiability and other irregular features, Journal of Business and Economic Statistics 13 (1), 1995, pp. 53–66.

[9] J. Eliashberg, R. Steinberg, Market–production joint decision-making, in: J. Eliashberg, G.L. Lilien (Eds.), Handbooks in Operations Research and Management Science, Marketing, Vol. 5, North-Holland, Amsterdam, 1993, pp. 827–880.

[10] B. Fazlollahi, R.M. Vahidov, Applicability of FRIL to business intelligence, in: Proceedings of the Third European Congress on Intelligent Techniques and Soft Computing, Aachen, Germany, 1995, pp. 121–125.

[11] B. Fazlollahi, R.M. Vahidov, Intelligent neural networks in business intelligence, in: Proceedings of the World Congress on Neural Networks, Vol. II, Washington, DC, July 17–21, 1995, pp. 721–724.

[12] L.J. Fogel, A.J. Owens, M.J. Walsh, Artificial Intelligence through Simulated Evolution, Wiley, New York, 1966.

[13] S. Forrest, Genetic algorithms: principles of natural selection applied to computation, Science 26, 1993, pp. 872–878.

[14] H. Gatignon, Marketing mix models, in: J. Eliashberg, G.L. Lilien (Eds.), Handbooks in Operations Research and Management Science, Marketing, Vol. 5, North-Holland, Amsterdam, 1993, pp. 697–731.

[15] H. Gatignon, D.M. Hanssens, Modeling marketing interactions with application to salesforce effectiveness, Journal of Marketing Research 24 (3), 1987, pp. 247–257.

[16] D.E. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning, Addison-Wesley, Reading, MA, 1989.

[17] J.H. Holland, Adaptation in Natural and Artificial Systems, University of Michigan, Ann Arbor, MI, 1975.

[18] J.H. Holland, J.H. Miller, Artificial adaptive agents in economic theory, American Economic Review, Papers of Proceedings of the 103rd Annual Meeting of the American Economic Association, 1991, pp. 365–370.

[19] S. Hurley, L. Moutinho, N.M. Stephens, Solving marketing optimization problems using genetic algorithms, European Journal of Marketing 29 (4), 1995, pp. 39–56.

[20] P.G.W. Keen, M.S. Scott-Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

[21] J.-J. Lambin, Optimal allocation of competitive marketing efforts: an empirical study, Journal of Business 43 (4), 1970, pp. 468–484.

[22] J. Lee, G.E. Johnson, Optimal tolerance allotment using a genetic algorithm and truncated Monte-Carlo simulation, Computer-Aided Design 25 (9), 1993, pp. 601–611.

[23] Z. Lee, S. Gosain, I. Im, Topics of interest in IS: evolution of themes and differences between research and practice, Information and Management 36, 1999, pp. 233–246.

[24] C.S. Maddala, F.D. Nelson, Maximum likelihood methods for models for markets in disequilibrium, Econometrica 42, 1974, pp. 1013–1030.

[25] E.G. Mallach, Understanding Decision Support Systems and Expert Systems, Richard D. Irwin, Inc., 1994.

[26] M. Manheim, An architecture for active DSS, in: Proceedings of the 21st Hawaiian International Conference on Systems Sciences, Vol. III, 1988, pp. 356–365.

[27] R. McHaney, T.P. Cronan, Toward an empirical understanding of computer simulation implementation success, Information and Management 37, 2000, pp. 135–151.

[28] Z. Michalewicz, Genetic Algorithms + Data Structures = Evolution Programs, Springer, Berlin, 1992.

[29] D.F. Midgley, R.E. Marks, L.G. Cooper, Breeding competitive strategies, Management Science 43 (3), 1997, pp. 257–275.

[30] D. Mirchandani, R. Pakath, Four models for a decision support system, Information and Management 35 (1), 1999, pp. 31–42.

[31] L. Rabelo, Y. Yih, A. Jones, J.-Sh. Tsai, Intelligent scheduling for flexible manufacturing systems, Proceedings of the IEEE International Conference on Robotics and Automation 3, 1993, pp. 810–815.

[32] S.A. Raghavan, JANUS: a paradigm for active decision support, Decision Support Systems 7, 1991, pp. 379–395.

[33] A. Rangaswamy, Marketing decision models: from linear programs to knowledge-based systems, in: J. Eliashberg, G.L. Lilien (Eds.), Handbooks in Operations Research and Management Science, Marketing, Vol. 5, North-Holland, Amsterdam, 1993, pp. 733–771.

[34] M. Sakawa, J. Utaka, M. Inuiguchi, I. Shiromaru, N. Suginohara, T. Inoue, Hot parts operating schedule of gas turbines by genetic algorithms, in: Proceedings of the International Joint Conference on Neural Networks and Fuzzy Satisficing Methods, Vol. I, Nagoya, 1993, pp. 746–749.

[35] B. Schott, T. Whalen, Fuzzy uncertainty in imperfect competition, Information Sciences 76, 1994, pp. 339–354.

[36] M. Silver, Systems that Support Decision Makers: Description and Analysis, Wiley, New York, 1991.

[37] T. Terano, Y. Ishino, Knowledge acquisition from questionnaire data using simulated breeding and inductive learning methods, Expert Systems with Applications 11 (4), 1996, pp. 507–518.

[38] T. Terano, Y. Ishino, Marketing data analysis using inductive learning and genetic algorithms with interactive and automated phases, in: Proceedings of the Fourth IEEE International Conference on Evolutional Computing, 1995, pp. 771–776.

[39] L. Vacca, Managing options risk with genetic algorithms, in: Proceedings of the IEEE/IAFE 1997 Computational Intelligence for Financial Engineering, March 24–25, New York, 1997, pp. 29–32.

[40] H.M. Wagner, Principles of Operations Research, Prentice-Hall, Englewood Cliffs, NJ, 1975.

[41] J.-H. Wang, J.-Y. Leu, Dynamic trading decision support system using rule selector based on genetic algorithms, in: Proceedings of the 1996 IEEE Signal Processing Society Workshop, 1996, pp. 119–128.

[42] J.-H. Wang, J.-Y. Leu, Stock trading decision support system using rule selector based on sliding window in: Proceedings of the 1997 IEEE International Conference on Systems, Man, and Cybernetics, Vol. 1, 1997, pp. 559–564.

[43] L. Zadeh, Fuzzy sets, Information and Control 8, 1965, pp. 338–353.

![](/api/attachments/8Y8AHABY/fulltext/images/125502fa0f11a361b8273fb2a47cacbd7ca937932b9e879ffab2db7ebf705d9a.jpg)

Bijan Fazlollahi is an educator and a consultant. He conducts research in the area of decision support systems. He has papers published in Journal of Decision Support Systems, Journal of Management Information Systems, Interfaces, Information Systems Research, Fuzzy Sets and Systems, International Journal of Intelligence Systems, Journal of Intelligence and Fuzzy Systems, Information and Management. His teaching area

is computer information systems, decision support systems, database management systems, and international business. He also teaches internationally in the Newly Independent States and

Eastern Europe. He was a Fulbright Lecturer in the Former USSR and received two honorary doctorate degrees from major universities there. He has consulted for large organizations such as airports and police departments in the area of computer information systems. He is a member of the Editorial Board of the Journal of Database Management Systems.

![](/api/attachments/8Y8AHABY/fulltext/images/3a5154afb2a82c0c25905bcb8d26fa805e62366123cc742752fc66db57a07b3b.jpg)

Rustam Vahidov is an Assistant Professor of Management Information Systems at Concordia University (Montreal, Que.). His research interests include decision support systems, multi-agent systems, genetic algorithms, fuzzy logic, neural networks and their application to decision support. He has papers published in Academic Journals including Decision Support Systems, Fuzzy Sets and Systems, International Journal of Intelligent Systems, and also in various conference proceedings.
