---
otero_id: 25184
otero_key: "YGFYVHKV"
title: "A Method for Generation of Alternatives by Decision Support Systems"
authors: ""
year: "2001"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2001.11045683"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Method for Generation of Alternatives by Decision Support Systems

Bijan Fazlollahi, Rustam Vahidov

To cite this article: Bijan Fazlollahi, Rustam Vahidov (2001) A Method for Generation of Alternatives by Decision Support Systems, Journal of Management Information Systems, 18:2, 229-250. DOI: 10.1080/07421222,2001.11045683

To link to this article: https://doi.org/10.1080/07421222.2001.11045683

![](/api/attachments/YGFYVHKV/fulltext/images/00c4b4acafd77a6db6466a1f14f965b8bcfa777ee4b0f9d007d825d044fc4b08.jpg)

Published online: 09 Jan 2015.

![](/api/attachments/YGFYVHKV/fulltext/images/f1d7695d145d8e1ce90d7d78aaa22192276dbe27dc41f89c6b2b9bab365cba24.jpg)

Submit your article to this journal

![](/api/attachments/YGFYVHKV/fulltext/images/746bd3b65493d3bd9b7e3afc3013b10cf975709092a0188428a68db20fde8e5e.jpg)

Article views: 37

![](/api/attachments/YGFYVHKV/fulltext/images/3b74d5da068931ef656f82d985f673883f66828ea161722049c4d69afd2e8dfd.jpg)

View related articles

![](/api/attachments/YGFYVHKV/fulltext/images/25e34b9bf18fa89c0725cd6d15892bb4719fb9cc78c65dd7e8cb7e8c28a740f6.jpg)

Citing articles: 10 View citing articles

# A Method for Generation of Alternatives by Decision Support Systems

BIJAN FAZLOLLAHI AND RUSTAM VAHIDOV

BIJAN FAZLOLLAHI is an associate professor in the Department of Computer Information Systems and Institute of International Business in the Robinson College of Business at Georgia State University, Atlanta, Georgia. He received his Ph.D. in Management Information Systems from Syracuse University. His current research interest includes Decision Support Systems and Application of Emerging Technologies for Decision Support. He has published in Information Systems Research, Journal of Decision Support Systems, Interfaces, Fuzzy Sets and Systems, and International Journal of Intelligent Systems. His experience includes serving as a consultant in the area of Decision Support Systems for large public organizations. He serves on the editorial board of the Journal of Data Base Management.

RUSTAM VAHIDOV is an Assistant Professor of Management Information Systems at the Department of Decision Sciences and MIS at Concordia University, Montreal, Quebec, Canada. He earned his Ph.D. from Georgia State University, Atlanta, Georgia. Dr. Vahidov’s research interests include decision support systems, multi-agent systems, genetic algorithms, fuzzy logic, neural networks, and electronic commerce. He has published in the Journal of Decision Support Systems, International Journal of Intelligent Systems, Fuzzy Sets and Systems, and other journals and conference proceedings.

ABSTRACT: An essential feature of active Decision Support Systems (DSS) is the ability to take the initiative in performing decision-related tasks. One possibility for providing active high cognitive level decision support is through facilitating alternative generation in DSS. The method proposed in this work enables the generation of several diverse alternatives in a single run. The method relies on the principles of effective problem-solving/decision-making and facilitates divergent processes, the separation of alternative generation from evaluation, as well as the diminishing of human cognitive biases. A hybrid DSS based on genetic algorithms (GA) and fuzzy sets is used to operationalize the approach. The paper outlines the design requirements for alternative generation in DSS and discusses the inadequacies of the “whatif” simulation and traditional optimization methods in light of these requirements. The paper further elaborates on the appropriateness of GA as a tool for alternative generation in DSS for solving complex ill-structured problems. The method is illustrated using marketing mix problem in a simulated business environment. The results suggest that the GA-based alternative generation leads to promising diverse alterna tives. An active DSS incorporating the proposed method reduces the time-consuming manual search for promising alternatives and provides a higher degree of man–machine collaboration.

KEY WORDS AND PHRASES: alternative generation, decision support systems, genetic algorithms, marketing mix problem.

DECISION SUPPORT SYSTEMS (DSS) are information systems aimed at directly supporting decision-making processes. The main objective of DSS is to enhance the effectiveness of decision-making in less structured decision tasks [29]. Traditional DSS incorporate models and data used for informing decision-making process [1, 50].

Conventional DSS offer a weak form of support, where the potential power of human-computer collaboration is significantly underutilized. The process is user-directed, where the user must take the initiative to perform all necessary operations having full knowledge on where and how to use DSS tools. Researchers have recommended increasing effective utilization of DSS through a more active participation in decision-making [2, 7, 35, 44, 46], active support of high level cognitive processes [43], and stressing divergent processes [44].

One way to address the above concerns is to facilitate alternative generation in a DSS. In a conventional model-based DSS, the human performs alternative generation and the machine evaluates each alternative with simple calculations of the relevant criteria. This ignores the human yearning for more alternatives from which to choose. Thus, a conventional DSS supports primarily the choice phase of Simon’s decisionmaking model [49]. It does not provide adequate support for the design phase, particularly for alternative generation. The drawbacks of a human-only alternative generation include:

 A search for promising alternatives may be very time-consuming, especially if the number of decision variables is large,

 Human biases, such as “anchor and adjust” [24], may lead to accepting inferior solutions,

 Because of the above drawbacks and the nature of “what-if” analysis, the generated alternatives may lack true diversity, and

 Since in traditional DSS alternative generation is usually immediately followed by evaluation, the well-known problem-solving principles of deferred judgment and divergence-convergence [40, 42] are inevitably violated.

The purpose of this paper is to propose a method for alternative generation in DSS. The method facilitates generation of several diverse alternatives in a single run. The paper proposes use of genetic algorithms (GA) and fuzzy sets as a basis for alternative generation.

The subsequent sections cover the review of related work; a formal description of the problem; a description of genetic algorithms and their use for alternative generation; a description of the example application; and a discussion of simulations and simulation results. The paper concludes with brief summary of its findings and conclusions.

## Related Work

DSS AIM TO IMPROVE THE EFFECTIVENESS rather than the efficiency of the decisionmaking process for less-structured problems. In less-structured problems, the conditions indicating the existence of problems are not defined. There is no best methodology to approach solving these problems, and the criteria for choosing the best decisions are not clear [29]. A problem is unstructured if any of the three stages of decision-making (intelligence, design, choice) is unstructured. According to another definition, if either the initial or desired state, or the set of transformations to cover the gap between the two, is not precisely known, the problem is less structured [34].

The area of problem-solving is very closely related to decision-making. In fact, some authors make no distinction between problem-solving and decision-making [34]. Researchers have made many prescriptions for improving problem-solving and decision-making effectiveness [57] including divergent/convergent thinking, deferred judgment, and control of human biases. Alex Osborn, the father of brainstorming, suggested that problem-solving consists of three stages: fact-finding, idea-finding, and solution-finding [40]. Osborn’s model was further expanded by Parnes, who suggested two additional stages and stressed the importance of divergent and convergent activities [41]. Divergent thinking is a creative input to problem-solving, while the convergent thinking deals with choice [18]. The divergence–convergence principle implies separation of evaluation and judgment from idea generation. This principle referred to as deferred judgment [40, 41], or ideation-evaluation [5] lies in the basis of creative problem-solving. It is also necessary to generate alternatives that are truly diverse, and not “clones” of one another. Otherwise this would lead to “myopic” alternative generation [6]. Generation of diverse promising alternatives may be hindered by human biases, such as “anchoring and adjusting” [24]. Therefore, one has to reduce the impact of such biases in a problem-solving process.

In a less structured problem there are normally several conflicting objectives that need to be achieved [29, 51]. One aspect of the lack of structure in such problems is the uncertainty about the desired states. Therefore, a desired characteristic of a DSS is support for the generation of diverse alternatives to achieve objectives.

Past research has focused on the evaluation of alternatives in terms of multiple objectives. Hogarth [24] distinguishes compensatory and non-compensatory models as strategies for choice. Compensatory models include linear, additive difference, and ideal point models, while non-compensatory models include conjunctive, disjunctive, lexicographic, and elimination-by-aspects models. One widely used Operations Research approach to multi-objective problems is goal programming [27], which is a generalization of linear programming to the case of multiple objectives. Traditional use of optimization methods assumes that these techniques will generate the “best” solution. These methods are not well suited for ill-structured problems, where the desired objectives are not known in advance. They do not produce multiple alternatives in a single run. They do not consider the divergence—convergence principles for effective problem-solving discussed previously. A possible use of optimization methods in DSS is to incorporate them as part of the human-directed tool.

Ironically, traditional model-based DSS are not characterized with the above principles of problem-solving/decision-making. For example, “what-if” DSS ignores the guideline for the separation of alternative generation from evaluation as well as the divergence–convergence principle. However, research findings have recommended the inclusion of these principles in guidelines for building DSS. Evans [17] argues that a computer algorithm for supporting problem-solving should generate “spread” [59] of alternatives preferably in a single run.

Recently, researchers have advocated a more proactive role for DSS in the man– machine collaboration. This may enable the DSS to support the user in abiding by the principles of problem-solving/decision-making. Manheim introduced a notion of active DSS and proposed an architecture for constructing such DSS, where certain tasks can be performed by the system in an autonomous fashion [35]. Chuang and Yadav [7] argued in favor of active support and proposed a framework for adaptive DSS. Dolk and Kridel proposed an active DSS for econometric analysis [12]. Raghavan also stressed the necessity to build more active DSS that would take the initiative in performing certain tasks, stress divergent processes, and engage in insightful conver sations. He proposed an architecture for active DSS and a prototype called JANUS [44]. Rao proposed an architecture for active DSS based on intelligent agents [46].

Developments in active DSS may contribute positively to the problem of alternative generation. Sharda and Steiger [48] and Steiger [52] argued that little attention had been paid in the past to the model analysis stage in model-based DSS. They proposed a system called INSIGHT for supporting model analysis based on multiple model instantiations. Through such analysis the decision-maker can get a better un derstanding into the situation by exploring the impact of different model parameter values on the solutions. In effect, this analysis facilitates alternative generation, since different parameters lead to different solutions. The work on the support for model building facilitates an easy construction of models, as well as an incorporation of the changes in those models to test different assumptions and generate alternatives [38]. There is also literature on interactive methods for alternative generation in decision support to elicit user preferences [28, 53]. The above methods, however, are sequential in manner. They do not aim at generating truly diverse alternatives with respect to the achievement of different objectives, and they are prone to human biases (e.g., anchoring and adjusting).

Advances in man–machine systems, where more activities can be delegated to machines necessitate development of advanced features/functions. Radermacher pointed out that decision support has been mainly restricted to the low cognitive level support [43]. Typical functionality of a DSS included such tasks as data storage, retrieval, manipulation, consistency checking, and small calculation. In an attempt to support higher level tasks, the researchers advocated the use of artificial intelligence techniques [43], as well as hybrid methods [32, 33, 53], that combine various techniques (e.g., fuzzy logic, neural nets, etc.) in one DSS. The major rationale for employing the latter includes combining the strengths of the individual techniques for more effective decision support. One such relatively novel technique that can be used in DSS [3] is GA [9]. GA can deal with problems that incorporate nonlinearity, discontinuity, uncertainty, complexity, and other demanding features. These features make the application of traditional search and optimization methods inappropriate.

The developments in active and adaptive DSS could lead to building a DSS, which follows the principles of decision-making and problem-solving. For example, an active “what-if” DSS would suggest promising and diverse alternatives giving the user more options from which to choose. However, currently there is no conceptual basis for building such systems. There is a pressing need to develop the design methods for active DSS that would support high level cognitive functions, such as alternative generation to solve-less structured problems.

The alternative generation problem considered here suggests diverse alternatives, which promise different potential desired states for the DSS user. The major difference from the traditional multi-objective optimization methods is that in our approach, DSS also support the decision-maker’s value judgment [24]. For example, in the case of marketing mix decisions, one alternative would lead to higher profits, while the other would promise higher market share. The user can then exercise judgment in making the final choice.

The alternative generation capability would benefit DSS in the following ways:

 It would facilitate divergent processes by offering a spread of alternatives,

 It would facilitate the separation of alternative evaluation from alternative generation,

 It would make DSS more active by enabling the exercise of initiative in searching for promising solutions and thus alleviate the user from a time-consuming manual search,

 It would reduce natural human biases, such as “anchor and adjust,” for the above reasons,

 It would provide cognitively “higher” support. It goes beyond simple calculations and data retrieval/manipulation capabilities to create a higher degree of man-machine collaboration.

The next section introduces the description of the problem of alternative generation.

## Problem of Alternative Generation

AS WE HAVE STRESSED, TRADITIONAL OPTIMIZATION METHODS of operations research (OR), including multi-criteria optimization methods (e.g., goal programming), strive for finding a single “best” solution to a problem at hand. These techniques require specification of the objective function and the set of constraints. Then, the optimization procedure identifies the solution that best fits the given specifications. However, for less structured problems with the presence of complexities and uncertainties, the notion of optimality may be fuzzy at best. For these problems, there is often some degree of uncertainty about the desired state. Hence, the objectives are not clear. The OR methods are inappropriate for making decisions in such situations. Human judgment is necessary for making a choice.

A more appropriate strategy for solving less structured problems is to use the methods that help generate promising candidate alternatives. These “good” candidates can then be passed to the decision-maker for selection, or, if necessary, modification. This relieves the decision-maker from the time-consuming task of locating promising candidates. Here, the computer-based procedure attempts to solve the alternative generation part of the original problem. Therefore, the procedure does not produce the solution, but a set of solutions. Each of these should be a “good” or viable alternative. The general formulation of the problem is given below.

Let $X = ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$ be a vector of decision variables and $C = ( c _ { 1 } , c _ { 2 } , . . . , c _ { m } )$ be a vector of relevant criteria. Let $F = f _ { 1 } ( ) , f _ { 2 } ( ) , . . . , f _ { m } ( ) )$ be a vector of functions mapping the decision variables into the set of criteria F : X ®C. Let $C _ { j } ^ { * } = ( c _ { j 1 } ^ { * } , c _ { j 2 } ^ { * } , . . . , c _ { j m } ^ { * } )$ be a vector containing desirable values for criteria $c _ { i } , i = 1 , m$ . We will call this vector the alternative goal (not to be confused with the term “alternative,” which here means a potential solution). In traditional multi-objective optimization problems, one would attempt to find such values of X that would achieve $C _ { j } ^ { * }$ best. In general, however, there are a number of different combinations of desired values for $C _ { j } ^ { * } j = 1 , r$ , that is, r alternative goals. Since all values for criteria should be reached in order to achieve a given alternative goal, we can write:

$$
\begin{array}{c} G _ {j} = \Big [ f _ {1} \left(x _ {1}, x _ {2},..., x _ {n}\right) \to c _ {j 1} ^ {*} \Big ] \wedge \Big [ f _ {2} \left(x _ {1}, x _ {2},..., x _ {n}\right) \to c _ {j 2} ^ {*} \Big ] \\ \wedge \ldots \wedge \Big [ f _ {m} \left(x _ {1}, x _ {2},..., x _ {n}\right) \to c _ {j m} ^ {*} \Big ] \end{array}
$$

or

$$
G _ {j} = \underset {i = 1} {\overset {m} {\wedge}} \bigg [ f _ {i} \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \to c _ {j i} ^ {*} \bigg ].\tag{1}
$$

As mentioned previously, the automated procedure for alternative generation should find a set of viable “solutions” where these solutions lead to multiple alternative goals. Therefore, we apply “OR” (disjunction) operation to the alternative goals in Equation (1) to obtain the global goal:

$$
G = \underset {j = 1} {\overset {r} {\vee}} G _ {j} = \underset {j = 1} {\overset {r} {\vee}} \underset {i = 1} {\overset {m} {\wedge}} \left[ f _ {i} \left(x _ {1}, x _ {2}, \dots , x _ {n}\right)\rightarrow c _ {j i} ^ {*} \right].\tag{2}
$$

Adding constraints in a very general form:

$$
\Phi (\mathrm{X}) \subset \Omega ,\tag{3}
$$

where Frestricts the values of criteria associated with solution X to a feasible region W, we complete the formulation of the problem. The solutions to the problem (Equations 2 and 3) can be represented as a matrix $r \times n$ with r rows being alternative solutions, and n columns being values of different decision variables:

$$
X ^ {*} = \left[ \begin{array}{c c c c} x _ {1 1} ^ {*} & x _ {1 2} ^ {*} & \ldots & x _ {1 n} ^ {*} \\ x _ {2 1} ^ {*} & x _ {2 2} ^ {*} & \ldots & x _ {2 n} ^ {*} \\ \vdots & \vdots & & \vdots \\ x _ {r 1} ^ {*} & x _ {r 2} ^ {*} & \ldots & x _ {r n} ^ {*} \end{array} \right],\tag{4}
$$

such that

$$
X _ {k} ^ {*} \neq X _ {1} ^ {*}, k, 1 = \overline {{1 , r}}; k \neq 1.\tag{5}
$$

Here, $\boldsymbol { x } _ { \ i j } ^ { * }$ is ith alternative value of jth decision variable, and $X _ { k } ^ { * }$ is kth row of matrix (Equation 4), that is, kth alternative. The requirement Equation (5) specifies that no two alternatives should be the same.

Note two important aspects of the above formulation. First, as we already mentioned, the global solution is not a vector, but a matrix. This feature distinguishes the current approach from traditional approaches, where solutions are typically vectors. Second, the disjunction connective in the global goal will most likely introduce multiple optima. Although traditionally multiple optima are considered detrimental, in this problem formulation we intentionally introduce nondominated multiple optima and seek multiple candidate solutions. We try to avoid dominated local optima that may be present due to the complexities of the functions included in $F .$

We further advocate use of fuzzy sets in constructing the goal Equation (2). There are several reasons for doing this:

 Human decision-makers prefer linguistic, or “soft” information [37], and fuzzyset theory allows representing such information.

 Preferences are formulated in fuzzy terms in DSS, and the use of fuzzy preferences makes DSS more robust [20].

 Since the membership function of fuzzy sets has a range [0, 1] (see Appendix), it provides a standard scale for measuring the degree of achievement of different objectives.

 It makes it easy to incorporate possible “soft” constraints in the problem (e.g., “avoid large inventory build-ups”) into the overall objective.

With a little modification, we can rewrite Equation (2) as

$$
\tilde {G} = \underset {j = 1} {\overset {r} {\vee}} \underset {i = 1} {\overset {m} {\wedge}} \bigg [ f _ {i} \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \to \tilde {c} _ {j i} ^ {*} \bigg ],\tag{6}
$$

where $\tilde { c } _ { j i } ^ { * }$ is jth fuzzy desired value for the ith criterion. One way of aggregating the components of the above goal is through use of min and max operations for Ùand $\vee ,$ respectively [14]:

$$
\mu_ {\ddot {G}} (X) = \max _ {j} \min _ {i} \left\{\mu_ {\dot {c} _ {j i} ^ {*}} \left[ f _ {i} \left(x _ {1}, x _ {2}, \dots , x _ {n}\right)\right]\right\}\rightarrow \max, i = \overline {{1 , m}}; j = \overline {{1 , r}},\tag{7}
$$

where ${ \mu } _ { \ddot { G } } ( X )$ is the membership function indicating the degree to which the fuzzy goal $\tilde { G }$ is achieved, and $\mu _ { \vec { c } _ { j i } } ( \boldsymbol { \mathbf { \rho } } )$ is that indicating the degree to which the fuzzy desired value $\tilde { c } _ { j i } ^ { * }$ is achieved.

Equation (7) is of a general form. The alternative goals, including the fuzzy sets for the desired values, should be specified in accordance with the problem at hand. The most important guideline in specifying the alternative objectives is to try to set the diverse alternative goals. For example, in a strategic planning case the diverse alternatives could be “low cost leader,” “differentiated approach,” and “best value.” Each of these translates into a different set of objectives.

Consider, for example, a simplified case of a marketing mix problem where two alternatives are described as achieving (1) high profit and moderate sales, or (2) moderate profit and high sales. Assume a candidate solution S achieves the objective “high profit” to degree 80 percent, the objective “moderate sales” to 70 percent, the objective “moderate profit” to 100 percent, and the objective “high sales” to degree 90 percent. Then, the alternative goal (1) would be achieved to 70 percent (min(80%, 70%)), and alternative goal (2) would be achieved to 90 percent (min(100%, 90%)). The total goal would be then achieved to 90 percent (max(70%, 90%)).

The next section briefly discusses genetic algorithms and their applicability to the problem of alternative generation. For a detailed discussion of GA, please see, for example [23, 36].

## Genetic Algorithms and Their Applicability to Alternative Generation

GENETIC ALGORITHMS ARE APPLICABLE to a wide class of problems [36]. Evolutionary techniques have found successful applications in decision, negotiation, and search problems [15, 39]. A potential for application of GA to DSS has been recognized in the past (see for example [3]). Genetic algorithms have been developed as a principally new approach in optimization theory [19, 23, 25, 36]. The idea behind GA is borrowed from the evolution of living organisms. GA use selection, crossover, and mutation operators to breed good solutions. “Goodness” of the solutions is measured by so-called “fitness function.” The fitness function is based on the objective function of the problem and must be nonnegative. GA are less demanding than “strong” optimization methods as there is no need for calculating derivatives or performing complex mathematical transformations. Moreover, the probability of being trapped by local optima is comparatively low (though it still is not zero). Local optima are the “curse” of local search methods (e.g., gradient ascent), because these methods lead to the nearest local optimal point, which might not be the best globally. Since GA evolve the population of solutions this reduces the chance of being trapped in local minima.

There are a number of ways to deal with constraints using GA. Coello [10] categorizes them into the following categories: penalty functions; special representations; separation of objectives and constraints; hybrid methods; and novel approaches. A good approach to handle crisp constraints is to avoid generation of invalid solutions, wherever possible, through the careful design of genetic operators. In case of soft constraints, where small violations do not lead to invalid solutions in a strict sense, such constraints may be made a part of multi-objective functions [11, 56], which Coello categorizes under “separation of objectives and constraints” [10]. The details of handling constraints for our example problem will be discussed later in the paper.

One of the key characteristics of GA is that they are global optimization techniques operating on a population of potential solutions. The GA parameter “population size” (which can be either static or dynamic) refers to the number of candidate solutions in a population at each step of GA. Thus, GA inherently generate many alternative solutions (in a single run), which is one of the principles of successful problem solving. Furthermore, we can increase the diversity of these alternatives by specifying diverse alternative goals in the global goal and choosing GA parameters (e.g., mutation and crossover rate) to stress exploration, rather than exploitation of the search space.

The GA are characterized by their ability to deal with a wide class of problems [36]. This characteristic stems largely from the mild requirements GA places on the objective function to be optimized. In general, GA can deal with complex, nonlinear, and uncertain objective functions, as long as the degree of “goodness” of the chromosomes can be estimated in some way. Therefore, we can easily incorporate fuzzy terms, such as “high sales” or “large inventories,” into the fitness function without having to specify precise values.

We conclude that GA are applicable for the problem of alternative generation. In particular, the hybrid approach with the combination of GA as an alternative generation procedure and fuzzy sets for expressing diverse preferences for evaluating the alternatives, promises to make DSS a more active and advanced collaborator in a decision-making process. The subsequent sections illustrate an application of GA to generate alternatives for the marketing mix problem.

## Generating Alternatives for Marketing Mix Problem Using Genetic Algorithms

THE MARKETING MIX PROBLEM involves making decisions on price, promotion, and other important variables for various products. Traditionally, this problem was considered an optimization problem [21], and there have been attempts to optimize some specified objective function [13, 16, 31, 45]. However, the inherent simplifying assumptions of these approaches limit their usefulness [22, 45]. In highly competitive and uncertain dynamic environments, external factors, such as the state of the economy, consumer preferences, as well as strategies and tactics of competing firms determine the dynamics of the market. Gatignon [22] and Rangaswamy [45] stress the use of simulation models, rather than traditional optimization as an appropriate decision-support tool for these problems. These models allow the decision-maker to evaluate alternatives and see how the key criteria change in response to changes in the input variables.

The simulation method overcomes the problems associated with most optimization methods: unrealistic assumptions, failure to deal with local optima, uncertainties, nondifferentiability of the objective function, and the necessity to aggregate multiple criteria into a single objective function. Simulation may serve as a basis for “what-if” type of DSS. The drawbacks of the simulation-based approach include:

 the user may waste significant time and effort examining inferior (in a Pareto sense) solutions,

 the user is prone to different biases (e.g., “anchor and adjust”), generates “clone” alternatives (because of “anchoring,” or settling on one solution), and fails to consider many promising solutions,

 the generated alternatives are immediately evaluated, which may lead to premature termination of search.

Genetic algorithms identify a set of “good” alternatives for the marketing mix problem better than humans do. GA-directed search is automated and is not prone to human biases. Furthermore, the evaluation by the decision-maker is done after the set of alternatives has been generated.

The potential applications of GA to marketing optimization problems are: consumer behavior; segmentation, targeting and positioning, managing the marketing mix; and strategic marketing [26]. Hurley et al. [26] discuss applications to site location analysis, and segmentation (product-market structure) in detail. Terano and Ishino [55, 56] used GA for extracting marketing decision rules from a questionnaire. Balakrishnan and Jacob [3, 4] used GA to support the product design process. The above approaches treat marketing problems in a traditional optimization sense, assuming that there is a single “best” solution. Our approach employs GA as an alternative generation tool (rather than conventional optimization tool) for generating promising alternatives for ill-structured problems.

Let us reproduce Equation (2):

$$
G = \underset {j = 1} {\overset {r} {\vee}} \underset {i = 1} {\overset {m} {\wedge}} \bigg [ f _ {i} \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \to c _ {j i} ^ {*} \bigg ].
$$

With respect to the marketing mix problem, vector C consists of important marketing criteria, including profit, market share, sales volume, marketing expenditures, and other important indicators. As we stressed earlier, we will use fuzzy criteria in our formulation. This makes sense, since specifying precise target values for sales, market share, and other variables would not be adequate in complex and imprecise environments. Vector X consists of decision variables, such as price, advertising expenditures, quantity, and other controllable variables, for different products. Note, that some decision variables can also be part of criteria, for example, advertising expenditures. Function vector F maps the values of decision variables into the values of criteria. If there are intrinsic uncertainties in the problem formulation, the simulation model can be used to determine the expected values of criteria. Constraints (Equation 3) may contain both “hard” (crisp) and “soft” (fuzzy) constraints. We advocate the use of special methods to ensure that no invalid (in a sense of hard constraints) chromosomes are produced and the inclusion of soft constraints into the fitness function as a fuzzy objective. In the next section we will discuss handling constraints in more detail using an example.

In general, the values of decision variables will need to be translated into the chromosome representation. Genetic algorithm then proceeds as follows:

1. Initial population of candidate solutions is randomly generated.

2. Fitness value is calculated for each chromosome (potential solution) in the population (this may require running simulations and passing the results to the GA).

3. Selection operator generates new population from the old population based on fitness values of the chromosomes.

4. Crossover operator is applied to the population.

5. Mutation operator is applied to the population.

6. Fitness value is calculated for each chromosome in the population (similar to step 2).

7. If stopping criteria are met, then the process ends, otherwise it goes back to step 3. The stopping criteria may include the maximum number of generations, or some goal attainment based measure.

8. The set of the best generated alternative solutions for the alternative goals and the key criteria are presented to the user.

The next section illustrates an example application of GA to marketing mix problem using simulation environment.

## Example Application

FOR OUR EXPERIMENTS WE USED SIMQ business simulation software, where a number of firms compete for three products $( x ^ { \prime } , y ^ { \prime } , \mathrm { a n d } z ^ { \prime } )$ in an oligopolistic market of a hypothetical business environment [8, 47]. A team of graduate students manages each firm. The teams make marketing, production, and financial decisions each quarter using DSS incorporating accounting and representational models. The decisions include a mix and quantity of goods to produce, pricing information, advertising expenses, as well as production capacity. The DSS for marketing decisions incorporates a Monte-Carlo simulation model. This model allows estimating the distributions of important output variables (e.g., sales, market share, profits, inventory levels) given the trial decisions and other input information. The decision-makers use these criteria as a guide to analyze different alternatives.

In searching for promising decisions, the decision-makers have to watch for hard and soft constraints in the problem. The hard constraint includes the requirement that the total production quantity of the three products should be limited by the capacity of the production facilities. The soft constraint is to avoid large inventory buildups, and still have some level of inventory. We call it “soft,” since there are no “crisp” boundaries for inventory levels. Even if such boundaries were to be specified, slight violation of them would not lead to infeasible solutions.

In our prototype, we tried to alleviate the user’s search process by delegating GA the task of generating a set of promising alternatives. We used the variables Volume Sales, Profit, and Advertising Expenditures as criteria to evaluate the alternatives. We generated the following set of situation descriptors to specify “good,” or “promising” alternatives.

1. High Volume Sales And Moderate Profit And Somewhat High Advertising (to capture market share and yet make substantial profit);

2. High Profit And Somewhat High Volume Sales And Moderate Advertising (to make high profit and have some inventory to avoid stockouts);

3. Moderate Volume Sales And Somewhat High Profit And Somewhat Low Advertising Expenditures;

4. Moderate Volume Sales And Some Profit And Low Advertising.

The above items form the basis for alternative goals. In reality, one could use multiple experts in a brainstorming session to specify a set of diverse specifications for desired goals. Note that the target values of the criteria are expressed in fuzzy linguistic terms, rather than precise values, which is more appropriate for human experts and decision-makers.

We used binary-coded chromosomes for encoding the prices, advertising expenditures, and quantities for the three products. Here GA interacts with Monte-Carlo simulation model to obtain the expected values for the above criteria, and then uses membership functions (discussed in the Appendix) to obtain the value of the fitness function. To calculate the fitness of a trial solution (chromosome), the conditions specified above are aggregated through the “OR” operation to form a single clause in accordance with Equation (2). Since we are using fuzzy terms, the actual fitness function is similar to Equation (7).

We handled the capacity constraint in the following way. Instead of explicitly generating the quantities for the three products, we encode the product mix by taking one product (in our case, the product x, which is one of the product quantity decision variables) as the base product and encoding the quantities of others through the ratio of the quantity of the base product to them. We encode these using $Q _ { x ^ { ' } / y ^ { ' } }$ and $Q _ { x ^ { ' } / z ^ { ' } }$ which are actually the angles representing the mix of products. The tangent of these angles gives the actual ratio of product $x ^ { \prime }$ to the products $y ^ { \prime }$ and $z ^ { \prime }$ . Use of angles instead of actual ratios is preferred since we can control the ranges for these angles easier than those for the ratios. The variable Q represents the total actual quantity of the three products and is limited by the capacity limit of 15,000. Symbolically,

$$
\frac {Q _ {x ^ {\prime}}}{Q _ {y ^ {\prime}}} = \tan Q _ {x ^ {\prime} / y ^ {\prime}}, \frac {Q _ {x ^ {\prime}}}{Q _ {z ^ {\prime}}} = \tan Q _ {x ^ {\prime} / z ^ {\prime}}, Q _ {x ^ {\prime}} + Q _ {y ^ {\prime}} + Q _ {z ^ {\prime}} = Q,
$$

where $Q _ { x ^ { ' } } , Q _ { y ^ { ' } } , Q _ { z ^ { ' } }$ are the quantities of products $x ^ { \prime } , y ^ { \prime }$ , and $z ^ { \prime }$ . From the previous formulas we can derive the quantities of the products as follows:

$$
Q _ {x ^ {\prime}} = \frac {Q}{1 + \frac {1}{\tan Q _ {x ^ {\prime} / y ^ {\prime}}} + \frac {1}{\tan Q _ {x ^ {\prime} / z ^ {\prime}}}}, Q _ {y ^ {\prime}} = \frac {Q _ {x ^ {\prime}}}{\tan Q _ {x ^ {\prime} / y ^ {\prime}}}, Q _ {z ^ {\prime}} = \frac {Q _ {x ^ {\prime}}}{\tan Q _ {x ^ {\prime} / z ^ {\prime}}}.
$$

This method guarantees that no invalid chromosomes (infeasible solutions) will be generated as a result of genetic operations. This method seems ad hoc in our case. It can potentially be generalized to include more complex constraints. However, our interest here is in generating diverse alternatives and not in developing general constraint handling procedures.

The soft constraint concerning inventory buildups is directly incorporated into the multi-objective function as a fuzzy term. To this end, we added the term “Some Inventory” to our alternative goals specified earlier.

To complete the specification of the fitness function we specified the membership functions used for fuzzy terms. Membership functions reflect the degree to which an item can be described by a given fuzzy term. Fuzzy set theory provides the experts with the flexibility in specifying fuzzy terms they use in their respective fields [30]. Experts also use their judgment in specifying the parameters of the membership functions. For example, if market share is described by a fuzzy term “medium” and a triangular function is chosen for representation, the experts will have to specify what is the smallest and highest values for market share to be considered medium at all (membership 0), and what is the most representative value that describes “medium” market share (membership 1). With these parameters specified, the membership of any crisp value for market share to the fuzzy set “medium” can be calculated. The discussion on the membership functions we chose to represent fuzzy terms is given in the Appendix.

The chromosomes encoding candidate solutions are represented in GA as follows:

$$
\Big (P _ {x ^ {\prime}} ^ {b}, \mathrm{P} _ {y ^ {\prime}} ^ {b}, P _ {z ^ {\prime}} ^ {b}, A _ {x ^ {\prime}} ^ {b}, A _ {y ^ {\prime}} ^ {b}, A _ {z ^ {\prime}} ^ {b}, Q _ {x ^ {\prime} / y ^ {\prime}} ^ {b}, Q _ {x ^ {\prime} / z ^ {\prime}} ^ {b}, Q ^ {b} \Big).
$$

Here, $P _ { x ^ { \prime } } ^ { b } , P _ { v ^ { \prime } } ^ { b } , P _ { z ^ { \prime } } ^ { b }$ are binary string representations of prices for products $x ^ { \prime } , y ^ { \prime }$ , and $z ^ { \prime }$ ; $A _ { x ^ { \prime } } ^ { b } , A _ { y ^ { \prime } } ^ { b } , A _ { z ^ { \prime } } ^ { b }$ are those for advertising expenditures; and $Q _ { x ^ { \prime } / y ^ { \prime } } ^ { b } , Q _ { x ^ { \prime } / z ^ { \prime } } ^ { b } , Q ^ { \bar { b } }$ are those encoding the mix of the products and the total quantity of the products.

In our experiments GA used elitist selection in which the chromosomes best satisfying the described conditions are always preserved. The chromosome length was 90, the population size was set to 80, number of generations in a single run was 300, the probability of mutation was 0.008, and the probability of crossover was 0.7. The results of 50 runs are presented in Table 1.

## Results and Discussions

THE MARKETING MIX PROBLEM REQUIRES making decisions on price, promotion, and other variables in order to achieve “best” outcome in terms of key marketing criteria (e.g., profit and market share). However, because of the ill-structured nature of the problem, determination of what makes the outcome “best” is largely judgmental. The proposed method makes a thorough search of the solution space and presents several promising alternative solutions to the decision-maker. The proposed method avoids the drawbacks of “what $\mathrm { i f } ^ { \flat }$ -type simulation that often leads to waste of time and effort in examining inferior solutions (in Pareto sense), fails to consider many promising alternatives, and may terminate the search process prematurely.

In the previous section we illustrated an application of our method to the marketing mix problem. The tabulated results (Table 1) show that diverse alternative goals lead to diverse alternatives in terms of the key criteria. The first goal emphasizes high volume sales, whereas the second one stresses high profit and some inventory. The third and the fourth goals lead to the somewhat low to low advertising expenditures with moderate to high profit and some inventory.

<table><tr><td rowspan="2">Condition #</td><td colspan="2">Sales Volume, units</td><td colspan="2">Profit, $</td><td colspan="2">Advertising, $</td><td colspan="2">Inventory, units</td></tr><tr><td>Mean</td><td>St.D.</td><td>Mean</td><td>St.D.</td><td>Mean</td><td>St.D.</td><td>Mean</td><td>St.D.</td></tr><tr><td>1</td><td>13,720</td><td>313</td><td>844,127</td><td>23,691</td><td>215,235</td><td>24,240</td><td>80</td><td>49</td></tr><tr><td>2</td><td>12,562</td><td>474</td><td>1,097,802</td><td>32,927</td><td>149,525</td><td>33,310</td><td>27.6</td><td>25.7</td></tr><tr><td>3</td><td>11,897</td><td>699</td><td>942,212</td><td>21,377</td><td>108,121</td><td>6,039</td><td>82</td><td>40.4</td></tr><tr><td>4</td><td>8,867</td><td>321</td><td>762,757</td><td>14,320</td><td>38,575</td><td>3,730</td><td>109</td><td>116</td></tr></table>

<sub>1.ResultsoftheSi</sub>m<sup>ula</sup>

![](/api/attachments/YGFYVHKV/fulltext/images/aff11644ba65d7d0a1a3bbd5ebcfcfd0784e7b4f4241fb799c4ae3c0b2a89b25.jpg)  
Figure 1. Alternatives 1 Through 4 Mapped on Sales Volume and Profit Dimensions

Figure 1 plots the alternatives 1 through 4 along the Profit and Sales Volume dimensions. As shown in the figure, alternative 1 attempts to maximize sales volume, while alternative 2 strives to maximize profit. The alternatives 3 and 4 lead to decreased Sales Volume and Profit, but also imply lower Advertising Expenditures as one can see from Figures 2 and 3.

The divergence of alternatives was assessed using MANOVA. In MANOVA, only Profit, Sales Volume, and Advertising Expenditures were included, since the Inventory Level is not a criterion, but is used to impose a soft constraint. We used MANOVA since we were interested in detecting significant differences among the groups of observations measured by multiple criteria. The analysis of the results of the procedure rejected the hypothesis that the generated alternatives are the same with the pvalue of 0.000. This provides some evidence in favor of our expectation concerning the diversity of alternatives.

The results showed that:

 DSS can be built for a manageable number of promising diverse alternatives,

 The alternatives were diverse in terms of the achievement of objectives,  Each alternative informs the decision-making process on making trade-offs between conflicting objectives,

![](/api/attachments/YGFYVHKV/fulltext/images/fed1faeb87b799b69bae830d6d4c29ea01d2720187bffe713e54508c5863ddab.jpg)  
Figure 2. Alternatives 1 Through 4 Mapped on Sales Volume and Advertising Dimensions

 The alternative generation is completed before the evaluation of alternatives by the decision-maker.

In the context of the marketing mix problem, the method generates alternative deci sions tied to the key marketing criteria (e.g., profits, sales, etc.). This allows a decision-maker to examine diverse and promising scenarios in making marketing mix decisions. Furthermore, the decision-maker would also acquire a better insight into the problem as he analyzes the impact of different alternatives on the above criteria.

Possible difficulties related to the choice of various parameters required by the method can be addressed by: setting those parameters automatically (e.g., rate of crossover and mutation), or eliciting them from the user (if these relate directly to the marketing problem domain, e.g., parameters for fuzzy values of profits, inventories, etc.) in a user-friendly fashion. In the latter case, the user may be asked to define his perception of fuzzy terms using numeric input or interactive graphics.

## Conclusions

OUR WORK WAS BUILT UPON THE PREMISE that the principles of effective problem solving/decision-making should guide the development of active DSS. Our purpose has been to propose a method for alternative generation within active DSS based on genetic algorithms and fuzzy sets. We have specified the problem of alternative generation and contrasted it to the traditional view of optimization methods. We have further argued in favor of using genetic algorithms as an alternative generation procedure.

![](/api/attachments/YGFYVHKV/fulltext/images/fac2758c2dafeaea878c3e52a66015380a3e984dd50943fd6c5f9cc2d5ed8058.jpg)  
Figure 3. Alternatives 1 Through 4 Mapped on Profit and Advertising Dimensions

The outlined approach is best suited for the less structured problems. Specifically, it is most appropriate for the situations where the desired objectives are not clear. In many such cases the alternative goals can only be rationally specified in vague terms, thus, leading to the use of fuzzy sets. The GA-based DSS can recommend different promising alternatives for further analysis by the decision-maker who can then analyze/modify the alternatives and assess their implications and consequences for the final choice. Use of GA is preferred, not only because they operate on a population of solutions and produce multiple alternatives in a single run, but also because they can cope with complex problems and are less prone to inferior local minima as compared to local search methods.

One limitation of the current work is that it did not empirically investigate the link between generating diverse alternatives and the effectiveness of the final solutions. We implicitly relied on the principle of problem-solving stating that multiple diverse alternatives lead to improved problem-solving/decision-making. Another important limitation of the work is that it addresses primarily the divergence aspect of decisionmaking and largely ignores the convergence aspect. The latter involves systematic analysis and possible modification of the alternatives ultimately resulting in the choice of the final decision. In the proposed method, the user is expected to analyze and modify the alternatives and perform trade-offs. In this respect the work needs to be expanded further in order to address the convergent processes. The purpose of this paper was to introduce a method for alternative generation. Some possibilities for supporting convergent processes include: the design of the interactive methods with the dynamic formulation of alternative goals allowing the user to “zoom into” a particular region of solution space, and the use of critics to support the user’s judgment at the choice phase of decision-making [58].

The above possibilities are promising directions for future research. Other research opportunities include the design of supporting tools for eliciting parameters of fuzzy terms from the user, adaptive automatic tuning of these parameters, and the design of methods for the integration of the existing models in DSS with the alternative generation procedure. Further empirical investigation is needed to evaluate the effectiveness of the proposed DSS design as compared with the traditional DSS. Finally, application to other problems/areas is needed to demonstrate the generality of the approach. For example, alternative generation capability would greatly benefit e-commerce applications. Equipped with such DSS, online users could focus on good and diverse items of interest, thus avoiding a time-consuming manual search and information overload.

## REFERENCES

1. Alter, S. Transforming DSS jargon into principles for DSS success. In P. Gray (ed.), Decision Support and Executive Information Systems. Englewood Cliffs, NJ: Prentice Hall, 1994, pp. 3–26.

2. Angehrn, A.A. Computers that criticize you: Stimulus-based decision support systems. Interfaces, 23, 3 (1991), 3–16.

3. Balakrishnan, P.V., and Jacob, V.S. Triangulation in decision support systems: Algorithms for product design. Decision Support Systems, 14, 4 (1995), 313–327.

4. Balakrishnan, P.V., and Jacob, V.S. Generic algorithms for product design. Management Science, 42, 8 (August 1996), 1105–1117.

5. Basadur, M. Managing the creative process in organizations. In M.A. Runco (ed.), Problem Finding, Problem-Solving and Creativity. Norwood, NJ: Ablex Publishing, 1994, pp. 237– 268.

6. Brightman, H.J. Problem-Solving: A Logical and Creative Approach. Atlanta: Georgia State University, College of Business Administration, Business Publishing Division, 1980.

7. Chuang, T., and Yadav, S.B. The development of an adaptive decision support system. Decision Support Systems, 24, 2 (1998), 73–87.

8. Churchill, G. Applied Decision Sciences. Atlanta: Alphagraphics, 1992.

9. Coello, C.A.C. A comprehensive survey of evolutionary-basedmultiobjective optimization techniques. Knowledge & Information Systems, 1, 3, (1999), 269–308.

10. Coello, C.A.C. A survey of constraint handling techniques used with evolutionary algorithms. Technical Report Lania-RI-99-04, Laboratorio Nacional de Infomatica Avandoza, Xalapa, Varacruz, Mexico, 1999.

11. Coello, C.A.C. The use of multiobjective optimization technique to handle constraints. Proceedings of the Second International Symposium on Artificial Intelligence; Adaptive Systems. La Habana, Cuba: Institute of Cybernetics, Mathematics and Physics (CIMAF), March 1999, pp. 251–256.

12. Dolk, D.R., and Kridel, D.J. An active modeling system for econometric analysis. Decision Support Systems, 7, 4 (1991), 315–328.

13. Dorfman, R., and Steiner, P.O. Optimal advertising and optimal quality. American Economic Review, 44 (December 1954), 826–836.

14. Dubois, D., and Prade, H. Possibility Theory: An Approach to Computerized Processing of Uncertainty. New York: Plenum Press, 1988.

15. Dworman, G.; Kimbrough S.O., and Laing, J.D. On automated discovery of models using generic programming: bargaining in a three-agent coalitions game. Journal of Management Information Systems, 12, 3 (Winter 1995–1996), 97–125.

16. Eliashberg, J., and Steinberg, R. Market-production joint decision-making. In J. Eliashberg and G.L. Lilien (eds.), Handbooks in Operations Research and Management Science. Marketing. vol. 5. Amsterdam and New York: North-Holland, 1993, pp. 827–880.

17. Evans, J.R. Creative Thinking in the Decision and Management Sciences. Cincinnati, OH: South-Western Publishing Co., 1990.

18. Flood, R.L. Solving Problem-Solving: A Potent Force for Effective Management. New York: John Wiley & Sons, 1995.

19. Forrest, S. Genetic algorithms: principles of natural selection applied to computation. Science, 261 (August 1993), 872–878.

20. Garavelli, A.C.; Gorgoglione, M.; and Scozzi, B. Fuzzy logic to improve the robustness of decision support systems under uncertainty. Computer & Industrial Engineering, 37, 1–2 (1999), 477–480.

21. Gatignon, H. Marketing-mix models. In J. Eliashberg, and G.L. Lilien (eds.), Handbooks in Operations Research and Management Science. Marketing, vol. 5. Amsterdam and New York: North-Holland, 1993, pp. 697–731.

22. Gatignon, H., and Hanssens, D.M. Modeling marketing interactions with application to salesforce effectiveness. Journal of Marketing Research, 24, 3 (1987), 247–257.

23. Goldberg, D.E. Genetic Algorithms in Search, Optimization, and Machine Learning. Reading, MA: Addison-Wesley, 1989.

24. Hogarth, R. Judgement and Choice. New York: John Wiley & Sons, 1987.

25. Holland, J.H. Adaptation in Natural and Artificial Systems. Ann Arbor: University of Michigan Press, 1975.

26. Hurley, S.; Moutinho, L.; and Stephens, N.M. Solving marketing optimization problems using genetic algorithms. European Journal of Marketing, 29, 4 (1995), 39–56.

27. Ignizio, J.P. Goal Programming and Extensions. Lexington, MA: Lexington Books, 1976.

28. Kalu, T.C. An algorithm for systems welfare interactive goal programming modeling. European Journal of Operational Research, 116, 3 (1999), 508–529.

29. Keen, P.G.W., and Scott Morton, M.S. Decision Support Systems: An Organizational Perspective. Reading, MA: Addison-Wesley, 1978.

30. Klir, G.J.; Clair, U.S.; and Yoan, B. Fuzzy Set Theory. Upper Saddle River, NJ: Prentice Hall, 1997.

31. Lambin, J.-J. Optimal allocation of competitive marketing efforts: An empirical study. Journal of Business, 43, 4 (1970), 468–484.

32. Lenard, M.J.; Madey, G.R.; and Alam, P. The design and validation of a hybrid information system for the auditor’s going concern decision. Journal of Management Information Systems, 14, 4 (Spring 1998), 219–237.

33. Li, S. The development of a hybrid intelligent system for developing marketing strategy. Decision Support Systems, 27, 4 (2000), 395–409.

34. MacCrimmon, K.R., and Taylor, R.N. Decision-making and problem-solving. In M.D. Dunnette (ed.), Handbook of Individual and Organizational Psychology. Chicago: Rand-McNally, 1976, pp. 1397–1453.

35. Manheim, M. An architecture for active DSS. Proceedings of the 21st Hawaiian International Conference on Systems Sciences, vol. III. Los Alamitos, CA: IEEE, 1988, pp. 356–365.

36. Michalewicz, Z. Genetic Algorithms + Data Structures = Evolution Programs. Berlin: Springer-Verlag, 1992.

37. Mintzberg, H. The Nature of Managerial Work. New York: Harper and Row, 1973.

38. Murphy, F.H.; Stohr, E.A.; and Ma, P. Composition rules for building linear programming models from component models. Management Science, 38, 7 (1992), 948–963.

39. Oliver, J.R. A machine-learning approach to automated negotiation and prospects for elec-

tronic commerce. Journal of Management Information Systems, 13, 3 (Winter 1997), 83–112.

40. Osborn, A. Applied Imagination. New York: Charles Scribner’s Sons, 1963.

41. Parnes, S.J. Creative Behavior Guidebook. New York: Charles Scribner’s Sons, 1967.

42. Parnes, S.J.; Noller, R.B.; and Biondi, A.M. Guide to Creative Action. New York: Charles Scribner’s Sons, 1977.

43. Radermacher, F.J. Decision support systems: Scope and potential. Decision Support Systems, 7, 4–5 (1994), 315–328.

44. Raghavan, S.A. JANUS: A paradigm for active decision support. Decision Support Systems, 7, 4 (1991), 379–395.

45. Rangaswamy, A. Marketing decision models: From linear programs to knowledge-based systems. In J. Eliashberg and G.L. Lilien (eds.), Handbooks in Operations Research and Man-

agement Science. Marketing, vol. 5. Amsterdam and New York: North-Holland, 1993, pp. 733– 771.

46. Rao, H.; Raghav, Sridhar, R.; and Narain, S. An active intelligent decision support system. Decision Support Systems, 12, 1 (1994), 79–91.

47. Schott, B., and Whalen, T. Fuzzy uncertainty in imperfect competition. Information Sciences, 76, 3–4 (1994), 339–354.

48. Sharda, R., and Steiger, D.M. Inductive model analysis systems: Enhancing model analysis in decision support systems. Information Systems Research, 7, 3 (1996), 328–341.

49. Simon, H. The New Science of Management Decisions. New York: Harper, 1960.

50. Sprague, R.H. A framework for the development of decision support systems. MIS Quarterly, 4, 4 (1980), 1–26.

51. Stabell, C. Towards a theory of decision support. In P. Gray (ed.), Decision Support and Executive Information Systems. Englewood Cliffs, NJ: Prentice Hall, 1994, pp. 45–57.

52. Steiger, D.M. Enhancing user understanding in a decision support system: A theoretical basis and framework. Journal of Management Information Systems, 15, 2 (Fall 1998), 199– 220.

53. Sun, M.; Stam, A.; and Steuer, R.E. Interactive multiple objective programming using Tchebycheff programs and artificial neural networks. Computers & Operations Research, 27, 7–8 (2000), 601–620.

54. Surry, P.D.; Radcliffe, N.J.; and Boyd, I.D. A multi-objective approach to constrained optimization of gas supply networks: The COMOGA method. In T.C. Fogarty (ed.), Evolutionary Computing. Berlin: Springer-Verlag, 1995, pp. 166–180.

55. Terano, T., and Ishino, Y. Marketing data analysis using inductive learning and genetic algorithms with interactive and automated phases. Proceedings of Fourth IEEE International Conference on Evolutional Computing. Piscataway, NJ: IEEE, 1995, pp. 771–776.

56. Terano, T., and Ishino, Y. Knowledge acquisition from questionnaire data using simulated breeding and inductive learning methods. Expert Systems with Applications, 11, 4 (1996), 507–518.

57. Van Gundy, A.B. Creative Problem-Solving: A Guide for Trainers and Management. New York: Quorum Books, 1987.

58. Vahidov, R., and Elrod, R. Incorporating critique and argumentation in DSS. Decision Support Systems, 26, 3 (1999) 249–258.

59. Woolsey, G. Two essays on model motivation: With this sign optimize & the sheckels of silver solution. Interfaces, 9, 1 (1978), 13–17.

## Appendix

FUZZY SETS CAN BE USED FOR THE REPRESENTATION of imprecise concepts [30]. Membership functions are used to describe the degree to which a given object is perceived to belong to a fuzzy set. These functions have a range [0, 1], where zero indicates that an object does not belong to a set, and one indicates definite membership of an object to the set. The intermediate values indicate partial membership.

The shape and parameters of membership functions can be chosen by experts, either directly or indirectly, to reflect their perception of a given fuzzy term. For our simulations we used gaussian, sigmoidal, and reverse sigmoidal membership functions to represent the fuzzy linguistic terms “moderate/some,” “high,” and “low,” respectively, used in the specified conditions. The reason for using these “smooth” functions instead of, for example, trapezoidal or triangular membership functions is that the former ones indicate gradual change in memberships, and prevent form plateau-like formations:

Gaussian:

$$
\mu = e ^ {- \frac {(v - a) ^ {2}}{2 b ^ {2}}}.
$$

Sigmoidal:

$$
\mu = \frac {1}{1 + e ^ {- b (v - a)}}.\tag{12}
$$

Reverse sigmoidal:

$$
\mu = \frac {1}{1 + e ^ {- b (a - v)}}.\tag{13}
$$

Here, v is the numeric value of the variable, m is the membership, and a and b are parameters determining the shape of the membership functions. Table A1 lists the types and parameters a and b for membership functions defining the linguistic terms used in the conditions. We have chosen the values of these parameters based on our experience with the simulation model.

To accomplish “and” and “or” operations necessary for calculating the achievement of the goal we used minimum and maximum of the membership degrees of the operands, respectively.

For further discussion of fuzzy sets and operations on fuzzy sets, one can refer to the fuzzy sets literature, for example [14, 30].

Table A1. Parameters of Fuzzy Sets Used in the Conditions

<table><tr><td>Variable / Value</td><td>Membership Function</td><td>a</td><td>b</td></tr><tr><td>Profit: High</td><td>(12)</td><td>$1,000,000</td><td>0.00001</td></tr><tr><td>Profit: Somewhat high</td><td>(11)</td><td>$900,000</td><td>200,000</td></tr><tr><td>Profit: Moderate</td><td>(11)</td><td>$800,000</td><td>200,000</td></tr><tr><td>Profit: Some</td><td>(11)</td><td>$600,000</td><td>200,000</td></tr><tr><td>Volume sales: High</td><td>(12)</td><td>$13,000</td><td>0.005</td></tr><tr><td>Volume sales: Somewhat high</td><td>(11)</td><td>$13,000</td><td>5,000</td></tr><tr><td>Volume sales: Moderate</td><td>(11)</td><td>$9,000</td><td>5,000</td></tr><tr><td>Advertising: Somewhat high</td><td>(11)</td><td>$220,000</td><td>50,000</td></tr><tr><td>Advertising: Moderate</td><td>(11)</td><td>$160,000</td><td>50,000</td></tr><tr><td>Advertising: Somewhat low</td><td>(11)</td><td>$100,000</td><td>50,000</td></tr><tr><td>Advertising: Low</td><td>(13)</td><td>$50,000</td><td>0.0001</td></tr><tr><td>Inventory: Some</td><td>(11)</td><td>$100</td><td>200</td></tr></table>
