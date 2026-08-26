---
otero_id: 13682
otero_key: "G795T2YX"
title: "An evolutionary real options framework for the design and management of projects and systems with complex real options and exercising conditions"
authors: "Stephen X. Zhang; Vladan Babovic"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.12.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An evolutionary real options framework for the design and management of projects and systems with complex real options and exercising conditions

Stephen X. Zhang <sup>a,</sup>⁎, Vladan Babovic <sup>b,1</sup>

<sup>a</sup> Dept of Industrial & System Engineering, Pontificia Universidad Catolica de Chile, Avenida Vicuna Mackenna 4860, Macul, Santiago, Chile <sup>b</sup> Engineering Workshop 1 #02-05, 2 Engineering Drive 2, S117576, Singapore

## a r t i c l e i n f o

Article history: Received 3 April 2009 Received in revised form 26 October 2010 Accepted 1 December 2010 Available online 10 December 2010

Keywords: Uncertainty Decision support Evolutionary algorithms Dynamic strategic planning Flexible design

## a b s t r a c t

To address the issue of decision support for designing and managing <sup>fl</sup>exible projects and systems in the face of uncertainties, this paper integrates real options valuation, decision analysis techniques, Monte Carlo simulations and evolutionary algorithms in an evolutionary real options framework. The proposed evolutionary real options framework searches for an optimized portfolio of real options and makes adaptive plans to cope with uncertainties as the future unfolds. Exempli<sup>fi</sup>ed through a test case, the evolutionary framework not only compares favorably with traditional <sup>fi</sup>xed design approaches but also delivers considerable improvements over prevailing real options practices.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Managers tend to adopt a single scenario for the future, come up with a <sup>fi</sup>xed design, and compute a single performance measure for a project, thus ignoring the importance of embedding multiple real options in projects [2]. Nevertheless, embedding multiple real options and exercising them based on how the future unfolds is a very important means to deal with uncertainties in the design and management of projects and systems [43]. Decision making that involves the planning and exercising of multiple options under uncertainty is complex, and, due to the complexity, organizations often fail in practice to follow a well-structured, accountable and reproducible decision-making process for assessing and selecting a dynamic strategy to formulate a <sup>fl</sup>exible design solution [24].

The dif<sup>fi</sup>culties to design and value a portfolio of real options under uncertainty are fundamentally caused by the complex structure of project pay-offs generated from the many possible paths of uncertainty and the interaction effects among the option portfolio, where each option may alter the boundary conditions of other options [30]. The value of a combination of real options is not the combined value of each option in isolation [44]. To value a portfolio of real options, Anand [1] analyzed the determinants to explain the portfolio effects, and Baldwin and Clark [4] calculated the option value of modules in a modular architecture theoretically. However, it remains unclear how to quantitatively assess a portfolio of real options when the number of interacting real options becomes large and the design space becomes non-convex. No conventional real options methodologies are able to systematically and holistically value and select multiple interdependent real options and their exercising conditions in complex projects and systems.

To deal with the issue, this paper proposes to use Evolutionary Algorithms (EA) as a part of an evolutionary framework, which values and selects portfolios of real options and formulates an overall dynamic option exercising plan.

EA has been widely applied to solve dif<sup>fi</sup>cult optimization problems. It is a generic multi-objective population-based metaheuristic optimization method, inspired by biological evolution [51]. One of the most popular techniques in the <sup>fi</sup>eld of EA is Genetic Algorithm (GA). GA is suitable to solve very large, path dependent and non-convex problems [23]. GA relaxes the conventional requirements that variables be independent and identically distributed. Instead, only the objectives and the environment of a problem need to be formulated, and GA applies the genetic principles of selection, crossover and mutation repeatedly to a set (i.e. population) of solutions, until a satisfying set of solutions is found.

An important advantage of using evolutionary algorithms for complex problems is that they overcome some signi<sup>fi</sup>cant challenges that are dif<sup>fi</sup>cult to study analytically or by conventional techniques. Dias [20] and Lazo et al. [27] proposed using GA to <sup>fi</sup>nd the exercise regions (price and time) of real options in oil <sup>fi</sup>eld developments, and recently Hassan et al. [24] have used it in aircraft design. This paper develops a decision support framework that uses evolutionary algorithms to select portfolios of real options in systems and projects and formulate <sup>fl</sup>exible design solutions.

The proposed framework has the potential to take into account a larger pool of real options, a wide variety of exercising conditions, and an increased degree of interactions. We illustrate the proposed framework by an example of Maritime Domain Protection (MDP) system, created at the Naval Postgraduate School (NPS) [11].

## 2. Evolutionary real options framework

## 2.1. Real options analysis

Multiple sources of <sup>fl</sup>exibility exist in the design and management of systems and projects. Such <sup>fl</sup>exibilities are speci<sup>fi</sup>cally known as “real options”. The term real options was coined by Myers [33] to describe the choices embedded in physical systems and projects, much like the choices made available to investors by <sup>fi</sup>nancial options. Formally, the de<sup>fi</sup>nition of both <sup>fi</sup>nancial and real options is a right but not an obligation to take certain actions at or within a speci<sup>fi</sup>c time<sup>2</sup>. The actions can be an opportunity to invest (for a call option) or to exit a bad situation (for a put option). To act on the option is to “exercise” the option. By exercising an option under certain favorable realizations of uncertainties, people gain value, and therefore the option has a time premium or holding value.

A classic example of a “real option” is the sizing of the foundation of a parking garage so that extra <sup>fl</sup>oors can be added later if a large demand materializes [50]. The value of the parking garage with the extra sizing therefore includes not only its present value, but also the value associated with the option to add the extra <sup>fl</sup>oors. Other real options include the option to temporarily shut-down [10], the option to adjust capacity [13], the option to implement in stages [25], the option to grow [16], the option to develop knowledge [48], the options to internationalize [28,42], and the option to continue or discontinue a series of investments in stages [5,15]. Real life projects often involve a combination of various options.

Knowing the value of real options permits system designers and managers to decide which options or <sup>fl</sup>exible design elements that allow their systems to evolve effectively over time are worth their costs. The valuation of real options started by borrowing valuation from modern <sup>fi</sup>nancial options theory [45]. However, the valuation formulas suitable for <sup>fi</sup>nancial options are often inapplicable for real options due to their complexity and uniqueness [8], which require new frameworks [18,21,35]. To deal with those issues, we propose an evolutionary real options framework by consolidating the best practices from the state-ofthe-art real options approaches and extending them with an extra step of optimization by evolutionary algorithms.

## 2.2. Consolidating the prevailing real options best practices:

Contrary to the traditional system engineering approach<sup>3</sup>, which optimizes a <sup>fi</sup>xed design based on a set of <sup>fi</sup>xed speci<sup>fi</sup>cations once the system and its objectives are de<sup>fi</sup>ned, the real options approach recognizes changes are inevitable over time and purposefully uses <sup>fl</sup>exibility to address them. Though varying from each other in terminologies and details, current real options best practices follow a stepwise process and consist of a few essential tasks [12,31,32,39,47]. Those tasks are consolidated (as circled by the smaller rounded rectangular in Fig. 1) and described as follows.

## A. Identify risk drivers and system states

All real options approaches start by the identi<sup>fi</sup>cation of key risk drivers. We want to identify useful risk drivers that will always affect the objectives of the systems or projects. In a quantitative decision support framework, the risk drivers need to be described by quanti<sup>fi</sup>able information that can be reviewed or updated regularly. When the risk changes, the system may still work reasonably well (i.e. the system still works in its current “state” where no major decisions or real options are exercised) or may only work if its “state” is changed. The number of system states depends on how many modes the system needs to work under.

## B. Identify options to change the state of systems over time

Designers can generate options to alter the system from one state to another state. On paper, decision makers can use real options to change a system at any time, but in practice physical projects and systems do not change continuously and instantaneously as <sup>fi</sup>nancial assets do in real-time markets. For this reason, real options related to systems are usually modeled in a discrete manner. A system has a large yet <sup>fi</sup>nite number of states and real options.

The number of system states and the number of options among the states determine the number of paths by which the system might be altered. The number of feasible paths available to a <sup>fl</sup>exible system is referred to as “outdegree” [37], which could be considered as a measure of the <sup>fl</sup>exibility of the system.

To structure the states and options of a system, a decision tree or an in<sup>fl</sup>uence diagram may be very helpful. Decision trees and in<sup>fl</sup>uence diagrams visually represent options and their exercising conditions [19]. The exercising conditions are usually estimated based on expert opinions and are often suboptimal, as it is beyond the limit of human cognition to search or identify optimal exercising conditions under vast uncertainty paths in a large and complex design space [29].

## C. Value real options using Monte Carlo simulations

Next, Monte Carlo simulations, capable of handling the non-linearity and discontinuity that are present in real options [7,17], can be employed to value the designs with and without real options. The difference in value between the design with and without real options is the value of the real options based on the Mutual Asset Disclaimer (MAD) method [9,14]. The number of designs without real options is limited, but the number of <sup>fl</sup>exible designs is overwhelmingly large due to the composition of different portfolios of real options and their exercising conditions. Valuing and comparing each of them one by one to select the optimal one is often not possible.

The design space with real options is combinatorial, and combinatorial space grows large easily<sup>4</sup>. “Combinatorics is the very heart of creation, hence of design… and design is inherently computational” [40]. Because the possible number of combinations is too large to be explored by the bounded rationality of human, designers cannot foretell which design solution is the best without devising a proper selection procedure — a design process. The essence of a design process therefore is to facilitate the exploration, analysis, optimization and selection of solutions in a combinatorial space.

In the problem of designing systems or projects with complex real options, the issues become:

• To explore and value real options while being able to account for

o Different option exercising conditions

o Interacting option portfolios

• To select and optimize portfolio(s) of real options and exercising conditions in a large <sup>fl</sup>exible design space

• To specify how the <sup>fl</sup>exible system with the selected portfolio of real options can and should evolve over time under uncertainty

![](/api/attachments/G795T2YX/fulltext/images/909dd9a3c311f34550a06618a4a67f48e79c4b6c5a3f6fb7630f20b1026e39f6.jpg)  
Fig. 1. Traditional <sup>fi</sup>xed design process, prevailing real options approach, and evolutionary real options approach (EA optimizes the options and the exercising conditions).

2.3. Extending the current real options practices to an evolutionary real options framework

To deal with the above issues, this study proposes an evolutionary real options framework (circled by the bigger rounded rectangular in Fig. 1). The evolutionary real options framework utilizes metaheuristic techniques, here, evolutionary algorithms, to optimize and select real options portfolios from the almost inde<sup>fi</sup>nite number of such portfolios without valuing them exhaustively. It also integrates with decision trees and simulation-based valuation methods.

Fig. 2 illustrates how the proposed framework extends current real options analysis (in the shaded areas). The framework starts with representing design solutions (portfolios of real options and exercising conditions) by a population of genetic strings. The initial population is often generated randomly by a computer in order to cover a diverse range of the search space, but it could also be “seeded”

![](/api/attachments/G795T2YX/fulltext/images/5db89482eaa525bd74239602ff7227d9593fdb6c0cf59d3384a1b2104e93007f.jpg)  
Fig. 2. A <sup>fl</sup>owchart of the proposed real options framework.

in areas where optimal solutions are likely to be found based on expert judgment. The size of the population is problem dependent, typically ranging from hundreds to tens of thousands.

The value of each option portfolio in the population is determined through Monte Carlo simulations. Monte Carlo simulations value a system by randomly generating the uncertain variables based on their stochastic distributions to imitate possible future paths. All the simulated paths are partitioned into branches at various decision nodes based on the exercising conditions of the real options. This means that different real options are exercised along different branches. The costs and bene<sup>fi</sup>ts related to each scenario in the branches can be computed. Aggregating them, we can get the values of a particular system design with an option portfolio. The values can be used to indicate the <sup>fi</sup>tness of the option portfolios in the population. As <sup>fi</sup>tness is usually problem-dependent, a variety of other <sup>fi</sup>tness measures can be devised to indicate the quality of the design solutions.

If the <sup>fi</sup>tness measure of the solutions is not yet good enough, the “survival of the <sup>fi</sup>ttest” principle that the <sup>fi</sup>tter individuals in a population will more likely produce a <sup>fi</sup>tter offspring is then implemented to produce the next population of solutions. Most of the selections of <sup>fi</sup>tter individuals are designed stochastically so that not all of the less-<sup>fi</sup>t solutions are eliminated. This maintains some diversity of the population so as to prevent the premature convergence of solutions. The selected individuals are chosen for reproduction (or crossover) at each generation, plus a mutation factor to randomly change the individuals, to develop a new population. The consequent new generation of population is based on, yet different from, the original population. As generations pass by, the <sup>fi</sup>tness increases until the algorithm terminates — often when either a satisfactory <sup>fi</sup>tness or a maximum number of generations is reached<sup>5</sup>.

The proposed framework has a number of important bene<sup>fi</sup>ts:

• The solutions containing portfolios of options and their exercising conditions are optimized and selected in an integrated manner simultaneously. This is very different from prevailing real options practices, which predetermine real options and exercising conditions in the phase of option identi<sup>fi</sup>cation, making it impossible to optimize them later on. Our proposed framework uses EAs to optimize them gradually and simultaneously based on the Darwinian process.

• EAs may discover new options and exercising conditions that humans may not perceive. Meanwhile, some real options may be deleted if they are deemed not to be useful in any scenarios (the costs of owning the options outweigh the bene<sup>fi</sup>ts in any circumstance). Thus, the real options representation is rede<sup>fi</sup>ned. The new real options representation (especially its feasibility and validity in the design and business environment) needs to be veri<sup>fi</sup>ed by system designers, policy makers, and managers. In this iterative re<sup>fi</sup>nement process, the real options framework undertakes the task of evaluating and optimizing option portfolios and allows system designers to concentrate more on the creative process of generating design alternatives and options.

• Our framework also facilitates the involvement of decision makers in the design process. Decision makers may conceive of or remove some real options based on their own judgment and information that designers do not possess. What-if analysis can be easily supported by the proposed framework, which can serve as a platform to carry out design experiments — substituting, rearranging, and reconnecting options, all backed up by associated values. Thus the proposed framework not only opens up the design space, valuing and selecting portfolios of real options beyond the bounded rationality of human, but also provides quantitative information to support the analysis of interest to decision makers and to supplement their managerial intuition and judgment.

## 2.4. Comparisons of the frameworks

The design space of a more <sup>fl</sup>exible design approach is expanded from (and contains) the design space of a less <sup>fl</sup>exible design approach, so the optimal design from a more <sup>fl</sup>exible design approach is better or at least equal to the optimal design from a less <sup>fl</sup>exible design approach. In that sense, a <sup>fi</sup>xed design is really a special case of (<sup>fl</sup>exible) designs where the bene<sup>fi</sup>t of every combination of real options is smaller than its cost. This could be due to either the future being the same as the forecasted or the cost of <sup>fl</sup>exibility is just too high to be incorporated. Likewise, the prevalent real option practices restricting to one or few real options are special cases of a general multiple real options design approach as in the proposed framework. A more <sup>fl</sup>exible design approach has the opportunity to yield more optimal designs under uncertainty. Nevertheless, designing with a more <sup>fl</sup>exible design approach does not mean that a large number of real options have to be used. It does permit a higher degree of freedom to use real options to further improve design solutions.

## 3. A numerical example applicaton

Terrorism threats in the Strait of Malacca, one of the world's most important shipping lanes, require an appropriate Maritime Domain Protection (MDP) system. The Naval Postgraduate School (NPS), Monterrey, CA, developed an MDP system based on which we will illustrate our proposed framework. NPS applied a widely adopted classical system engineering approach and architected a modular MDP system [34]. The MDP system consists of <sup>fi</sup>ve different subsystems (sensors, C3I, force, land and sea inspection), each of which consists of two or three alternative designs, which can be combined to result in various overarching MDP system. 109 such combinations are considered to be feasible system con<sup>fi</sup>gurations. For each of these system con<sup>fi</sup>gurations, the performance and costs are determined under a forecasted degree of maritime terrorism. Con<sup>fi</sup>gurations with better performance (resulting in lower successful rates of terrorism attacks) and lower costs were considered to be better designs. The best of them is selected as the optimal <sup>fi</sup>xed design.

The MDP system was used to introduce the idea of real options to the terrorism risk community in [11], which detailed the application of real options to an anti-terrorism system. Unfortunately, aiming to initiate real options to a new area of application, that paper did not develop a real options framework and did not highlight suf<sup>fi</sup>ciently its methodological contributions to real options analysis. This paper, aiming to propose and evaluate an evolutionary real options framework, utilizes the well documented MDP example to illustrate the application of the proposed framework.

This study uses the same modular system architectural principles and technical modules as well as the set of objective hierarchy as the NPS study [34]. The difference is this study does not believe the level of terrorism is certain. Terrorism attacks do not occur regularly and have little predictability. The architecting and design of the MDP system, especially to prevent a Weapons of Mass Destruction (WMD) attack, “comprises so many unknown variables that traditional cost– bene<sup>fi</sup>t analysis is rendered nearly impossible” [36]. Often risk is de<sup>fi</sup>ned using the frequency of occurrence and the impact or consequences of a terrorist attack as follows:

$$
\begin{array}{c} \text { Risk } = \text { probability   (statistical   frequency) } \\ \times \text { consequences   (monetary   terms) } \end{array}\tag{1}
$$

The probabilities and the consequences of occurrences are both highly uncertain and unpredictable in the coming years. As the risk of terrorism evolves, an optimal <sup>fi</sup>xed design conceived and designed today may be sub-optimal, yet decisions on the system must be made now to prevent terrorism in the decades to come. This study aims to design a <sup>fl</sup>exible MDP system with multiple real options and their subsequent exercising strategies, using the proposed evolutionary real options framework. The design solutions from the proposed framework, the prevailing real options practices and the <sup>fi</sup>xed design approach are compared. In this comparative fashion, the paper examines the added value of the evolutionary real options framework — speci<sup>fi</sup>cally its effectiveness in both <sup>fi</sup>nding suitable portfolios of real options and their exercising conditions to formulate a dynamic plan.

## 3.1. Applying the evolutionary real options framework

The key uncertainty in an MDP system is the degree of terrorism risk. While the evolution of terrorism risk is (near) continuous, the recon<sup>fi</sup>guration of a large-scale system mid-stream, even with prior embedded real options capabilities, has a long lead time. Therefore, the MDP system is modeled using discrete states. The design alternatives for all the system states are taken from the NPS study. Since the MDP system architected by NPS is modular, real options are readily available to alter the subsystem [3,38] as well as the overall con<sup>fi</sup>guration of the MDP system. The alteration requires an extra investment associated with acquiring and switching to the new subsystem alternative(s).

The overall MDP system design problem can be formulated as in Table 1.

Monte Carlo simulations are utilized to generate various paths to imitate the evolution of terrorism level by a modi<sup>fi</sup>ed lognormal stochastic process [6]. As time passes, the risk of terrorism changes, and real options can be exercised to recon<sup>fi</sup>gure the MDP system. As the recon<sup>fi</sup>guration of a large scale system can only be performed over discrete states, our study assumes that the real options to recon<sup>fi</sup>gure the system can be exercised in two stages at the third and sixth year in the ten-year lifespan of the MDP system.

A trinomial decision tree (Fig. 3) is used to represent the real options to recon<sup>fi</sup>gure in three stages. The three stages in the trinomial path-dependent tree result in nine paths. Along the 9 paths, there are in total 13 decision nodes of real options: one decision node in stage one (year 2007), three in stage two (2010), and nine in stage three (2013). At each decision node, system managers have the <sup>fl</sup>exibilities or real options to recon<sup>fi</sup>gure the MDP system. Each recon<sup>fi</sup>guration involves the substitution of one system con<sup>fi</sup>guration for another, i.e., a real option is exercised with an associated exercising cost. In a trinomial tree, there are three mutually exclusive and exhaustive real options at each of the decision nodes. The determination of which option is to be applied depends on the degree of terrorism risk and the exercising conditions of the real options. These conditions are initially set using expert opinions.

For example, Fig. 3 illustrates a case where experts handpick the exercising conditions of the three real options in a decision node. 1) A (lesser and cheaper) option is used if the risk in the decision node is lower than 0.58 times of its previous level (corresponding to the lower 25th percentile of the terrorism risk pro<sup>fi</sup>le); 2) a (better and more costly) option is used if the risk in the decision node is higher than 1.72 times of its previous level (corresponding to the upper 25 percentile of the terrorism risk pro<sup>fi</sup>le); and 3) another option is used then the risk is between 0.58 and 1.72 times of its previous level (corresponding to the risk level between 25th and 75th percentiles).

This partition scheme makes sense, because if the terrorism risk rises, it is justi<sup>fi</sup>able to apply an option to augment the MDP capability, and if the terrorism falls, it is better to apply an option to use a more compact MDP system to reduce cost. However, it is left out whether or not partitioning decision space by the upper 25%, lower 25% and middle 50% of the terrorism risk pro<sup>fi</sup>le is optimal.

Optimizing the option exercising conditions poses a practical challenge. Even if option exercising conditions are not considered as decision variables, the MDP problem already constitutes a very large design space. The design space is at the scale of 10 to the power of 26 as a consequence of its 13 decision nodes, each of which involves 109 real options. To estimate the design space with exercising conditions as decision variables, the exercising conditions, which are contingent upon and de<sup>fi</sup>ned based on the degree of terrorism, need to be discretized. If they are discretized by a step of 0.01 (again normalized based on the degree of terrorism in year 2007), the design space, with options and option exercising conditions both as decision variables, is at the scale of 10 to the power of 58.

## 3.1.1. Optimization by evolutionary algorithms

Because the number of real options is large, the exercising conditions of real options are intricate, and the design space is complex, it is unrealistic to expect human cognition to identify the most optimal set of real options and exercising conditions under uncertainty. This study uses GA as the search engine to optimize the set of system con<sup>fi</sup>gurations in 13 decision nodes (“Config” in Fig. 3) and their exercising conditions under uncertainties based on multiple objectives.

GA is capable of optimizing from multiple objectives. In this case, two metrics, based on the system value, are chosen. The value of the MDP system is the difference between the system performance and its cost. The value of the MDP system depends on the following decision variables.

$$
\text { Value\_of\_a\_system } = \sum_ {i, j} f _ {i, j} \left(\text { threshold } _ {i, j}, \text { config } _ {i, j}\right)\tag{2}
$$

where,

threshol $d _ { i , j }$ is the exercising conditions to get into branch j at stage i $c o n f i g _ { i , j }$ is the con<sup>fi</sup>guration to be used in branch j at stage i

The value of the MDP system is derived by aggregating the values of the system along all the paths of <sup>fl</sup>uctuating terrorism risk, which are generated by 5000 Monte Carlo simulations. The value of system along each path is computed by calculating the costs and bene<sup>fi</sup>ts of both the design and the options exercised along that path. Whether options should be exercised and which options to exercise for a given path, depends on the branch that path takes at various decision nodes. The branching of the paths at a decision node in a decision tree is de<sup>fi</sup>ned by the option exercising conditions.

Table 1 Formulation of the MDP system design problem by different design approaches.

<table><tr><td></td><td>Problem constructions</td><td>Traditional fixed design approach</td><td>Prevailing real options practices</td><td>Proposed real options framework</td></tr><tr><td>Objective</td><td>Maximize System Performance = Risk Saved = (Attack Damage without the protection system - Attack Damage with the system in place)</td><td>defined in the NPS study</td><td>same as in NPS</td><td>same as in NPS</td></tr><tr><td>Constraints</td><td>Technical availability of alternative designs</td><td>defined in the NPS study</td><td>same as in NPS</td><td>same as in NPS</td></tr><tr><td rowspan="3">Decisions</td><td>The system in initial stage</td><td>a fixed system</td><td>a flexible system with options</td><td>a flexible system with options</td></tr><tr><td>Subsequent real options to change the system</td><td>N.A.</td><td>one or few</td><td>many</td></tr><tr><td>The exercising conditions to activate the real options</td><td>N.A.</td><td>predetermined</td><td>optimized</td></tr><tr><td rowspan="3">Given Input</td><td>Performance and cost of each alternative design</td><td>defined in the NPS study</td><td>same as in NPS</td><td>same as in NPS</td></tr><tr><td>Cost of exercising real options</td><td>defined in the NPS study</td><td>cost of the alternative design plus 5% switching cost</td><td>cost of the alternative design plus 5% switching cost</td></tr><tr><td>Description of terrorism prevention requirement</td><td>a single forecast</td><td>a distribution</td><td>a distribution</td></tr></table>

![](/api/attachments/G795T2YX/fulltext/images/2862e31b23c7a6362026fb6dae55b1b1d58efc2a602cd74182b886dd2b14c9b3.jpg)  
Fig. 3. A handpicked real options solution represented in a trinomial scenario tree of 3 stages (r<sub>1</sub>, r<sub>2</sub> and r<sub>3</sub> denote the degree of terrorism risk in the three stages respectively).

Therefore, both real options and their exercising conditions affect system value and have to be optimized and selected simultaneously in order to maximize the system value under uncertainty. In addition, the exercising conditions have to exhaustively and exclusively cover all the scenarios in a stage. Fig. 4 illustrates this concept. The study assumes that the evolution of terrorism risks follows a modi<sup>fi</sup>ed lognormal distribution in stages (Fig. 4a) with a standard deviation of 35%. Fig. 4b shows how genetic algorithm simultaneously selects three different real options (con<sup>fi</sup>gurations) and de<sup>fi</sup>nes three option exercising conditions (illustrated by the percentiles of risk).

In addition, GA is able to take account of path dependency — a key obstacle to real options analysis. For example, a con<sup>fi</sup>guration that gives the best performance for a speci<sup>fi</sup>c decision node may not be chosen because it may not embed suitable real options to cope with the uncertainties and, as a consequence, may not deliver the best overall system value over time. Each decision at a decision node affects future choices. Therefore, optimization needs to consider not only the impact of a con<sup>fi</sup>guration over the project value at a given stage, but also its impact at later stages i +n (n=1, 2, …). This pathdependency is dif<sup>fi</sup>cult for conventional analytical optimization techniques to solve but is much less an issue for GA.

![](/api/attachments/G795T2YX/fulltext/images/8c7b7cf2eea683e72131ebe31fbc1335864410ae620fabd36b5b0c9e85985df5.jpg)  
Fig. 4. a. A schematization of an uncertain variable over time (more uncertain in more distant future). b. Selecting options and their exercising conditions — both are contingent upon the uncertainty.

## 4. Results

Before comparing the resulting design solutions from different approaches (based on the agents that choose the options and exercising conditions), we <sup>fi</sup>rst take a look at their respective design spaces (Table 2). In the MDP case study, a <sup>fi</sup>xed design is chosen from the design space of 109 alternative system con<sup>fi</sup>gurations, and, as the design is <sup>fi</sup>xed, neither options nor exercising conditions are applicable. The conventional real options approach is called hand picking real options approach. It uses human cognition to <sup>fi</sup>nd the exercising conditions and select the suitable options from 109 con<sup>fi</sup>gurations at 13 decision nodes — a large search space. In the approach of EA selecting real options without exercising conditions, the exercising conditions are still predetermined by human experts, but the suitable options are picked and optimized by evolutionary algorithms. In the EA selecting real options with exercising conditions approach, both real options and their exercising conditions are selected by EAs. As the control of decision variables becomes less stringent, the design space grows and the computational complexity in selecting optimal solutions increases.

To evaluate and compare the resulting design solutions using those approaches, this study follows the established valuation method [9,14], in which the NPV of the traditional <sup>fi</sup>xed design is subtracted from that of the <sup>fl</sup>exible design to derive the added value of real options. Table 3 summarizes the NPV of the MDP system using different design approaches and valuation methods.

## 4.1. The conventional system engineering approach

The traditional design process develops a <sup>fi</sup>xed MDP design and values it based on a forecasted level of terrorism risk, resulting in a deterministic<sup>6</sup> project value at \$574M. Monte Carlo simulations of the key uncertainty driver reveal that the project value may <sup>fl</sup>uctuate widely. A lower realization of terrorism risk will lower the performance and therefore the value of the MDP system, and a higher realization of terrorism risk (while still under the working range of the system) will increase the value of the MDP system.

The impact of the uncertainty is not symmetric just as it would not be in most complex systems. A higher realization of terrorism risk in a MDP system has a larger impact on the system value than a lower realization would have. Consequently the average NPV valued based on nondeterministic Monte Carlo simulations is higher than the NPV of the same design valued deterministically based on averaged inputs. Monte Carlo simulations also point out some alarming <sup>fi</sup>ndings: the minimum and the 5 percentile system value of the <sup>fi</sup>xed design are deeply negative, a fact that is hidden in the deterministic valuation method.

## 4.2. The hand-picked real options approach

In the common practice of real options, the option exercising conditions are predetermined prior to the valuation and selection of the real options [22,47,50]. For instance, Fig. 3 shows that the decision makers have decided that three different real options will be used respectively for the 25th, 50th, and 75th percentiles of the pro<sup>fi</sup>le of the degree of terrorism (their exercising conditions) before they proceed to select the three real options.

Table 2  
A summary of design approaches.

<table><tr><td rowspan="2">Design Approach</td><td colspan="2">Design Decisions</td><td rowspan="2">Design Space Freedom</td></tr><tr><td>Choice of Option</td><td>Choice of Exercising Conditions</td></tr><tr><td>Fixed peak design</td><td>No option to change</td><td>Not applicable</td><td>109</td></tr><tr><td>Hand picking real options</td><td>Designer</td><td>Predetermined manually</td><td> $109^{13} = 10 \exp 26.5$ </td></tr><tr><td>EA selecting real options without exercising rules</td><td>EA</td><td>Predetermined manually</td><td> $109^{13} = 10 \exp 26.5$ </td></tr><tr><td>EA selecting real options together with exercising rules</td><td>EA</td><td>EA</td><td> $109^{13} * 10000^{6} = 10 \exp 58$ </td></tr></table>

The resulting real options design compares favorably with the optimal <sup>fi</sup>xed design. On one hand, the minimum project value and the 5th percentile project value are elevated (−\$2288M to −\$1267M and −\$1780M to −\$1083M), because con<sup>fi</sup>gurations that have lower costs and correspondingly less protective capabilities are utilized when the realization of terrorism is in the lower 25% branch. On the other hand, if the degree of terrorism is above the 75th percentile, more capable yet more expensive con<sup>fi</sup>gurations are utilized, which increase the top 5th percentile project value from \$16,160M to \$34,708M and the maximum project value from \$141,874M to \$579,905M. The average project value increases signi<sup>fi</sup>cantly to \$10,043M from \$3295M. This increment in the average project value commonly stands for the value of the real options in the literature.

## 4.3. EA selecting real options without exercising conditions

As proposed by the extended evolutionary real options framework, the issue of picking suitable real options can be tackled by GAs. GAs are used to search for suitable real options in all the 13 decision nodes to make an option portfolio based on the objectives of the design. The evaluation and selection of real options, if required, must be made from multiple perspectives [49]. In this case, the objectives are made customizable. Two objectives, the average and the 5th percentile project values from the Monte Carlo simulations, are used here to cover both the project value and its risk exposure.

To ensure a fair comparison with the hand-picking real options design approach, the same predetermined exercise regions (the 25th, 50th, and 75th percentile of risk pro<sup>fi</sup>le) are applied. While the predetermined exercising regions are kept unchanged, GA is able to select a different set of system con<sup>fi</sup>gurations (Fig. 5). The solution found by GA is better than the hand-picking real options design in the average project value (increased from \$10,043M to \$10,277M) and risk exposure (the 5th percentile project value increases from − \$1083M to −\$298M). The maximum and 95th percentile project values are almost identical to those from the hand-picking real options design.

## 4.4. EA selecting real options together with exercising conditions

Furthermore, genetic algorithms can be deployed to select a portfolio of real options as well as their exercising conditions simultaneously. Rather than predetermining the option exercising conditions at the 25th, 50th and 75th percentiles of the risk pro<sup>fi</sup>le as estimated by experts, the evolutionary real options framework combines the real options and exercising conditions in various ways to search for possible better <sup>fl</sup>exible designs.

Table 3  
The project values based on design approaches.

<table><tr><td rowspan="2">Design Approach</td><td colspan="2">Design Decisions</td><td rowspan="2">Valuation Approach</td><td colspan="5">NPV metrics</td></tr><tr><td>Selection of Option</td><td>Selection of exercising conditions</td><td>Mean</td><td>Max</td><td>P95</td><td>P5</td><td>Min</td></tr><tr><td rowspan="2">Fixed peak design</td><td rowspan="2">No</td><td rowspan="2">Not applicable</td><td>Deterministic valuation</td><td>574</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>By simulation</td><td>3295</td><td>141,874</td><td>16,160</td><td>-1780</td><td>-2288</td></tr><tr><td>Hand picking real options</td><td>Predetermined manually</td><td>Designers</td><td>By simulation</td><td>10,043</td><td>579,905</td><td>34,708</td><td>-1083</td><td>-1267</td></tr><tr><td>EA selecting real options without exercising rules</td><td>EA</td><td>Predetermined manually</td><td>By simulation</td><td>10,277</td><td>579,402</td><td>34,610</td><td>-298</td><td>-485</td></tr><tr><td>EA selecting real options together with exercising rules</td><td>EA</td><td>EA</td><td>By simulation</td><td>11,329</td><td>592,330</td><td>47,395</td><td>-304</td><td>-1625</td></tr></table>

The remainder of this section discusses the results in Table 3 greater depth.

An example of the solutions found by GAs is shown in Fig. 6. In the second stage (2010), the solution keeps using one con<sup>fi</sup>guration (index number 8) as long as the risk is within 4.88 times of its previous level in the <sup>fi</sup>rst stage in 2007 (i.e. the entire 98th percentile of the risk pro<sup>fi</sup>le). And a high-performing con<sup>fi</sup>guration (index number 84) is exercised for the 98–99th percentiles and for the 99– 100th percentiles for the scenarios of very high terrorism risk. The exercising conditions in stage 2 are highly asymmetrical, as are those in stage 3. This implies that it is more critical to make decisions to change in certain scenarios rather than in some other scenarios and it may not be optimal to partition the decision space simply in a symmetric manner.

Using GAs on both the options and their exercising conditions increases the average value of the project to \$11,329M. Because the exercising regions of real options in this plan are exclusively focused on the high terrorism risk side (to switch only when the risk escalates by about 5-fold, i.e. to switch at the 98th and 99th percentiles of the risk pro<sup>fi</sup>le), the design focuses on the capability of the system to protect from higher degrees of terrorism risk and thereby captures more value. This is demonstrated by the considerable increase of the 95th percentile of NPV to \$47,395 compared to \$34,610 using the approach in which GAs are only deployed to optimize the options but not the exercising conditions.

The system con<sup>fi</sup>gurations in the adjacent branches of a decision tree could be the same at times in the design solutions, as found in both the hand-picked solution in Fig. 3 and GA-based solution in Figs. 5 and 6. This implies that the decision tree representations could be improved, for instance, project managers can combine some branches or split them to form new branches in a decision tree. A decision tree represents a decision structure (at what conditions to use which options), and hence, optimizing the decision tree is a primary means to improve the project design.

## 4.5. Sensitivity of real options value to the level of the uncertainty

The sensitivity of the value of real options with respect to the level of uncertainty around the degree of terrorism is shown in Fig. 7. As the uncertainty around the degree of terrorism becomes larger, the MDP system requirement is less predictable, the likelihood to recon<sup>fi</sup>gure the system using real options increases, and as a result embedding real options in the project becomes more valuable.

![](/api/attachments/G795T2YX/fulltext/images/c5d13d080d5edce1af698265c3570bfb6586684570bc04a47d39b113f5774752.jpg)  
Fig. 5. A design solution that GA selects the real options (con<sup>fi</sup>g.) at the 13 decision nodes in the 3 stages (the decision variables that GA optimizes are in Italic)

![](/api/attachments/G795T2YX/fulltext/images/0c49fb50ba9c4d15d2b55d358feffb8215d1d80f417272458bc0da9d41bd4eac.jpg)  
Fig. 6. A design that GA selects both the real options and their exercising conditions — in this case the con<sup>fi</sup>gurations and the degree of risk to exercise these con<sup>fi</sup>gurations

## 4.6. Summary of result

The results from the test case con<sup>fi</sup>rm extant <sup>fi</sup>ndings [20,47,50] that embedding real options in design can provide huge bene<sup>fi</sup>ts (e.g. the mean value of the conventional hand-picking real options design is 3 times higher than that of the optimal <sup>fi</sup>xed design). Furthermore, the evolutionary framework extends the prevailing real options practices and the extension is found to be valuable (the mean project value further increases by 13%). The proposed framework is able to value multiple interdependent real options and their exercising conditions and provides an integrated approach to decision-making regarding the design, planning, and management of <sup>fl</sup>exible systems and projects.

![](/api/attachments/G795T2YX/fulltext/images/4d65552255d0374bd8d7f3ea8157b1266f3604eba9195ffb67369b669981345b.jpg)  
Fig. 7. Real options value versus the uncertainty associated with the level of terrorism

## 5. Discussions

This study con<sup>fi</sup>rms the important bene<sup>fi</sup>ts as well as the dif<sup>fi</sup>culties of using multiple real options [45,46]. As demonstrated in the MDP case study, the framework makes possible the task of evaluating and selecting portfolios of real options as well as their exercising conditions in a large design space. The resulting design solutions are better than those from the conventional real options approaches and the traditional system engineering approach. Evolutionary algorithms have also demonstrated the capability to search design solutions based on more than one objective and are suitable to support multi-objective decision-making involving real options.

The evolutionary real options framework facilitates the exploration, analysis, optimization and selection of solutions effectively in a combinatorial real options design space — the essence of a design process [40] and allows the decision process regarding to options portfolios to be within the bounds of reasonable effort of decision makers. In doing so, the proposed framework frees up the design space and permits human experts to focus on the more creative process of generating design alternatives to harness more from <sup>fl</sup>exibility. It fundamentally changes the design process by improving the designers’ understanding of <sup>fl</sup>exibility, systematizing the decision process regarding to <sup>fl</sup>exibility, and facilitating the leverage of <sup>fl</sup>exibility through the ex ante planning of downstream decisions.

Since the proposed framework employs metaheuristic evolutionary algorithms, whose goal is to <sup>fi</sup>nd a satisfying near-optimal rather than global optimal solution, the design solutions obtained are not guaranteed global optimums. However, a global optimal solution may just be an illusion since any system model is only a simpli<sup>fi</sup>ed approximate of the reality subjecting to our bounded rationality. All prescriptive decision analysis is boundedly rational — “there is no such thing as a <sup>fi</sup>nal or complete analysis; there is only an economic analysis given the resources available” [26]. The issue of concern for real options in design is not to identify a single global optimum but to make better design choices.

The proposed framework not only changes the actual design, but also the design and decision process. It exposes, evaluates, and systematizes the design process with complex real options and therefore permits reasonable effort on the part of decision makers [41].

## 6. Conclusions

Extant literature has long recognized both the importance and the dif<sup>fi</sup>culties of incorporating multiple interacting real options [45,46]. The proposed evolutionary real options framework, with evolutionary algorithms as the engine of its extended optimization step, is able to value and select <sup>fl</sup>exible solutions with portfolios of real options. It delivers a roadmap for deploying those options under uncertainty. Moreover, the proposed framework opens up the design space, frees the range of “what if” questions that designers can pose regarding the vast possibilities a system can evolve, and it allows human cognition to focus more on the creative process of generating design alternatives and options to enable option-rich designs. It compares favorably with the state-of-the-art real options approaches and can be a helpful supplement to managerial intuition and qualitative thinking in designing projects and systems with multiple complex real options.

## Acknowledgements

The authors gratefully acknowledge the support and contribution from Singapore-Delft Water Alliance (SDWA) — R-264-001-001-272. For more information, please visit http://www.sdwa.nus.edu.sg. The authors also thank Defense Science and Technology Agency of Singapore, who funded the case used in this paper. Finally, the authors acknowledge the support by Academic Research Fund under grant “Data Assimilation and Data-Driven Knowledge Discovery” R-264-000-199-133/112.

## References

[1] J. Anand, R. Oriani, R.S. Vassolo, Managing a portfolio of real options, in: J.J. Reuer, T.W. Tong (Eds.), Advances in Strategic Management, Emerald Group Publishing Limited, West Yorkshire, England, 2007, pp. 275–303

[2] B. Asrilhant, R.G. Dyson, M. Meadows, On the strategic project management process in the UK upstream oil and gas sector, Omega 35 (2007) 89–103.

[3] V. Babovic, Emergence, Evolution, Intelligence: Hydroinformatics, Taylor & Francis, London, 1996.

[4] C.Y. Baldwin, K.B. Clark, Design Rules: The Power of Modularity, The MIT Press, Cambridge, MA, 2000.

[5] M. Benaroch, Managing information technology investment risk: a real options perspective, Journal of Management Information Systems 19 (2002) 43–84.

[6] S. Bouriaux, W. Scott, Capital market solutions to terrorism risk coverage: a feasibility study, Journal of Risk Finance 5 (2004) 34–44.

[7] P.P. Boyle, Options: a Monte Carlo approach, Journal of Financial Economics 4 (1977) 323–338.

[8] M.A. Brach, Real Options in Practice, Wiley, Hoboken, New Jersey, 2003

[9] R. Brealey, S. Myers, Principles of corporate <sup>fi</sup>nance, McGraw-Hill, Boston, 2000.

[10] M.J. Brennan, E.S. Schwartz, Evaluating natural resource investments, Journal of Business 58 (1985) 135–157.

[11] J. Buurman, S. Zhang, V. Babovic, Reducing risk through real options in systems design: the case of architecting a maritime domain protection system, Risk Analysis 29 (2009) 366–379.

[12] M. Cardin, W. Nuttall, R. de Neufville, J. Dahlgren, Extracting value from uncertainty: a methodology for engineering systems design, 17th, Annual International Symposium of the International Council on Systems Engineering, INCOSE, San Diego. 2007.

[13] Y.-C. Chou, C.T. Cheng, F.-C. Yang, Y.-Y. Liang, Evaluating alternative capacity strategies in semiconductor manufacturing under uncertain demand and price scenarios, International Journal of Production Economics 105 (2007) 591–606.

[14] T. Copeland, V. Antikarov, Real Options: A Practitioner's Guide, Texere Publishing, New York, 2001.

[15] G. Cortazar, E.S. Schwartz, J. Casassus, Optimal exploration investments under price and geological-technical uncertainty: a real options model, R and D Management 31 (2001) 181–189.

[16] Q. Dai, R.J. Kauffman, S.T. March, Valuing information technology infrastructures: a growth options approach, Information Technology and Management 8 (2007) 1–17.

[17] R. de Neufville, Dynamic strategic planning for technology policy, International Journal of Technology Management 19 (2000) 225–245.

[18] R. de Neufville, Real options: dealing with uncertainty in systems planning and design, Integrated Assessment 4 (2003) 26–34.

[19] R. Demirer, J.M. Charnes, D. Kellogg, In<sup>fl</sup>uence diagrams for real options valuation, Journal of Finance Case Research 9 (2007) 43–70.

[20] M.A.G. Dias, Investment in Information for Oil Field Development Using Evolutionary Approach with Monte Carlo Simulation, 5th Annual International Conference on Real Options - Theory Meets Practice, UCLA, 2001.

[21] T.W. Faulkner, Applying ‘options thinking’ to R&D valuation, Research Technology Management 39 (1996) 50–56.

[22] D.N. Ford, D.M. Lander, J.J. Voyer, A real options approach to valuing strategic <sup>fl</sup>exibility in uncertain construction projects, Construction Management and Economics 20 (2002) 343–351.

[23] D. Goldberg, Genetic algorithms in search, optimization and machine learning, Addison-Wesley Professional, Boston, MA, USA, 1989.

[24] R. Hassan, R. De Neufville, D. McKinnon, Value-at-risk analysis for Real Options in complex engineered systems, Proceedings of IEEE International Conference on Systems, Man and Cybernetics, Waikoloa, HI, 2005, pp. 3697–3704.

[25] C. Hilhorst, P. Ribbers, E. van Heck, M. Smits, Using Dempster-Shafer theory and real options theory to assess competing strategies for implementing IT infrastructures: a case study, Decision Support Systems 46 (2008) 344–355.

[26] R.A. Howard, J.E. Matheson, Readings on the principles and applications of decision analysis, Decision Analysis Group, Stanford Research Institute, Menlo Park, Calif, 1976.

[27] J. Lazo, M. Pacheco, M. Vellasco, M. Dias, Real Option Decision Rules For Oil Field Development Under Market Uncertainty Using Genetic Algorithms And Monte Carlo Simulation, 7th Annual Real Options International Conference, DC Washington, 2003.

[28] S.H. Lee, M. Makhija, Flexibility in internationalization: is it valuable during an economic crisis? Strategic Management Journal 30 (2009) 537–555

[29] J. March, Bounded rationality, ambiguity, and the engineering of choice, The Bell Journal of Economics 9 (1978) 587–608.

[30] R.G. McGrath, A real options logic for initiating technology positioning investments, Academy of Management Review 22 (1997) 974–996.

[31] K.D. Miller, H.G. Waller, Scenarios, real options and integrated risk management, Long Range Planning 36 (2003) 93–107.

[32] J. Mun, Real options analysis: tools and techniques for valuing strategic investments and decisions, John Wiley & Sons, Hoboken, N.J., 2006

[33] S.C. Myers, Determinants of corporate borrowing, Journal of Financial Economics 5 (1977) 147–175.

[34] NPS, Maritime Domain Protection in the Straits of Malacca, Naval Postgraduate School, Monterry, California, 2005.

[35] E. Pennings, O. Lint, The option value of advanced R & D, European Journal of Operational Research 103 (1997) 83–94.

[36] C. Raymond (Ed.), Maritime Terrorism, A Risk Assessment: The Australian Example, World Scienti<sup>fi</sup>c, Institute of Defence and Strategic Studies, Singapore, 2005.

[37] A. Ross, D. Rhodes, D. Hastings, De<sup>fi</sup>ning changeability: reconciling <sup>fl</sup>exibility, adaptability, scalability, modi<sup>fi</sup>ability, and robustness for maintaining system lifecycle value, Systems Engineering 11 (2008) 246–262.

[38] R. Sanchez, J.T. Mahoney, Modularity, <sup>fl</sup>exibility, and knowledge management in product and organization design, Strategic Management Journal 17 (1996) 63–76.

[39] M. Schneider, M. Tejeda, G. Dondi, F. Herzog, S. Keel, H. Geering, Making real options work for practitioners: a generic model for valuing R&D projects, R and D Management 38 (2008) 85–106.

[40] H. Simon, Problem forming, problem <sup>fi</sup>nding, and problem solving in design, in: A. Collen, W. Gasparski (Eds.), Design and systems: general applications of methodology, Transaction Publishers, New Jersey, USA, 1995, pp. 245–257.

[41] P. Todd, I. Benbasat, The in<sup>fl</sup>uence of decision aids on choice strategies: an experimental analysis of the role of cognitive effort, Organizational Behavior and Human Decision Processes 60 (1994) 36–74.

[42] T.W. Tong, J.J. Reuer, M.W. Peng, International joint ventures and the value of growth options, Academy of Management Journal 51 (2008) 1014–1029.

[43] A. Triantis, A. Borison, Real options: state of the practice, Journal of Applied Corporate Finance 14 (2001) 8–24.

[44] L. Trigeorgis, The nature of option interactions and the valuation of investments with multiple real options, Journal of Financial and Quantitative Analysis 28 (1993) 1–20.

[45] L. Trigeorgis, Real Options: Managerial Flexibility and Strategy in Resource Allocation, The MIT Press, Cambridge, Mass, 1996.

[46] R.S. Vassolo, J. Anand, T.B. Folta, Non-additivity in portfolios of exploration activities: a real options-based analysis of equity alliances in biotechnology, Strategic Management Journal 25 (2004) 1045–1061.

[47] T. Wang, R. de Neufville, Real options "in" projects, 9th Annual International Conference on Real Options, Paris, 2005.

[48] L.C. Wu, C.S. Ong, Y.W. Hsu, Knowledge-based organization evaluation, Decision Support Systems 45 (2008) 541–549.

[49] S.X. Zhang, V. Babovic, A real options approach to design and architect water supply systems using Innovative water technologies under uncertainty, Journal of Hydroinformatics (in press)

[50] T. Zhao, C.L. Tseng, Valuing <sup>fl</sup>exibility in infrastructure expansion, Journal of Infrastructure Systems 9 (2003) 89–97.

[51] E. Zitzler, L. Thiele, Multiobjective evolutionary algorithms: a comparative case study and the strength Pareto approach, IEEE Transactions on Evolutionary Computation 3 (1999) 257–271.

![](/api/attachments/G795T2YX/fulltext/images/2b166386ba9e2c3117346b0db15a9d00e87f99562e7df5483fb5b3f18cbbddf2.jpg)

Stephen Zhang is an assistant professor in the Department of Industrial and System Engineering in the Ponti<sup>fi</sup>cal Catholic University of Chile (Ponti<sup>fi</sup>cia Universidad Católica de Chile). His PhD is in the area of using real options in new technological projects, from the Department of Engineering and Technology Management at National University of Singapore. Prior to become a professor, Stephen had engineering experiences in STMicroelectronics and Siemens AG, management consulting experiences in Titan Group and Mikinsey, and research experiences in Nationa University of Singapore and Singapore Delft Water Alliance (SDWA). Webpage: http://www.ing.puc.cl/ics/detalle html?pr=szhang.

![](/api/attachments/G795T2YX/fulltext/images/b5bb0678d2487704f802abb2ceb04af745cf62851000776870c3c69e1ed3077c.jpg)

Vladan Babovic is an associate professor at National University of Singapore and the founding Director of Singapore-Delft Water alliance, a multi-disciplinary research initiative involving NUS, PUB (Singapore) and Delft Hydraulics (The Netherlands).Dr Babovic obtained his PhD. degrees from both UNESCO-IHE and Delft University of Technology, The Netherlands in 1995. In 2001, he has obtained a business degree at IMD in Lausanne (Switzerland). Prior to joining NUS, he was Head of emerging Technologies at Danish Hydraulic Institute (1995–2002), Chief Technology Of<sup>fi</sup>cer at Tetrasys, Switzerland (2002–2004) and Senior Research Scientist at Delft Hydraulics (2003–2005). Webpage: http:// www.eng.nus.edu.sg/civil/people/cvebv/cvebv.html.
