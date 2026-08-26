---
otero_id: 21744
otero_key: "ZG9FW9SA"
title: "Supporting decision making in combinatorially explosive multicriteria situations"
authors: "Sandeep Purao; Hemant K Jain; Derek L Nazareth"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00029-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting decision making in combinatorially explosive multicriteria situations

Sandeep Purao <sup>a,)</sup>, Hemant K. Jain <sup>b,1</sup>, Derek L. Nazareth <sup>b,2</sup>

a College of Business Administration, Georgia State UniÕersity, Atlanta, GA 30303, USA <sup>b</sup> School of Business Administration, UniÕersity of Wisconsin-Milwaukee, Milwaukee, WI 53201, USA

Accepted 21 June 1999

## Abstract

Several real-world problems, including distributed system design and product design among others, are characterized by combinatorially explosive solution spaces as well as multiple, conflicting criteria. Strategies for finding near-optimal solutions, developed for combinatorial problems, are not applicable in such situations, which require a balance between extensive computation and continual interaction. This makes support or automation of these decisions a difficult task. Current approaches to solve these problems fall in three categories: analytical, genetic algorithm-based approaches and local generators. They frequently assume well-behaved functions and clear understanding of interdependencies among criteria. Many such problems, however, present noisy and discontinuous evaluation functions and contain holistic interdependencies among these functions, rendering these solution approaches inadequate for these problems. We propose a theoretically grounded approach for decision support for this class of problems. The approach combines broad and deep searches with decision-maker feedback that allows the decision-maker to guide and<sup>r</sup>or stop the search. Specifically, it provides the decision-maker information about a the search spaces exploredŽ . Ž . Ž <sup>r</sup>probed so far, and b the search space not yet explored or may never be explored . We operationalize the approach in a two-phase solution procedure. The first phase — broad. characterization of search spaces — requires choices about randomization, sampling and decision space estimation techniques. The second phase — iterative local probes — requires choices about local search heuristics, and fuzzy interpretations based on which the decision-maker can evaluate alternatives and<sup>r</sup>or stop the search. We demonstrate a specific instantiation of the approach for a multicriteria object assignment problem to verify the feasibility of our approach. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Combinatorial optimization; Multiple criteria decision making; Decision support systems; Satisficing

## 1. Introduction

This paper develops a general approach for support in decision situations that involve combinatorially explosive alternatives and multiple, conflicting decision criteria. Traditionally, these two fields have dealt with different sets of concerns. Research in combinatorial problems has focused on techniques that yield increasingly near-optimal solutions 62 .<sup>w</sup> <sup>x</sup> Multiple criteria decision making research, on the other hand, has been concerned with designing approaches that facilitate trade-offs and assist the decision-maker in identifying a pareto-optimal solution <sup>w</sup> <sup>x</sup> 36 . Many real-world decision situations, though, require a combination of the two. The combination negates direct application of techniques from either domain. This paper combines the multiple theoretical bases from both research streams to develop an approach to enhance decision-making support in combinatorially explosive multicriteria situations.

Combinatorially explosive problems involve the selection or arrangement of discrete choices. For these problems, alternatives can be represented as a binary vector 0,1,1,0,1,0,1,1, . . . , representing prop- <sup>w</sup> <sup>x</sup> erties of the solution. Thus, for a product design problem, the bits represent the inclusion of specific characteristics in the product; for an assignment problem, they represent the allocation of a task to an individual, etc. The consequences of choosing a solution costs and payoffs are computed by differ- Ž . ent evaluation functions, which represent transformations of the solution vector. Since many such problems are NP-complete 18 , exact optimization<sup>w</sup> <sup>x</sup> algorithms are either too expensive or simply do not exist Ref. 8 , p. 508 . Heuristic techniques are,Ž <sup>w</sup> <sup>x</sup> . thus, often employed to arrive at near-optimal solutions 62 . The rich stream of research 51 on multi-<sup>w x</sup> <sup>w x</sup> ple criteria in decision making see Appendix A for aŽ compilation of important definitions is not tradition-. ally directed at combinatorially explosive problems. The existence of multiple criteria for combinatorially explosive problems introduces a new element of uncertainty — optimality depends on the decisionmaker’s preferences. In this case, the optimal solution is one that is ‘most preferred’ by the deci sion-maker and requires trade-offs among criteria. Arriving at this solution requires understanding and interpreting the underlying n-dimensional search space — a complex task in many real-world situations. Even satisficing strategies 49 are difficult to<sup>w</sup> <sup>x</sup> operationalize for these problems since they must balance extensive computation requirements against continual interaction with the decision-maker. This makes automation and support of these decisions a difficult task.

The objective of this paper is to develop a general approach to enhance decision support for such problems. To ensure generality and broad applicability, the class of problems considered in this research relaxes three assumptions that are often adopted in tackling such problems. These relaxations, which make for more real-world decision situations are: iŽ . complex evaluation functions that are generally not amenable to algebraic manipulation 60 , ii holistic <sup>w</sup> <sup>x</sup> Ž . interdependencies among criteria 15,38 , and iii <sup>w</sup> <sup>x</sup> Ž . unarticulated preferences among the decision criteria <sup>w</sup> <sup>x</sup> 25 see Appendix B . Fig. 1 defines the class ofŽ . problems addressed in this research.

![](/api/attachments/ZG9FW9SA/fulltext/images/02e7b131b69912c2822079eaed925f5ba5c23b5ee043e6ac6195b788d3cad969.jpg)  
Fig. 1. Class of problems under consideration.

The remainder of the paper is organized in the following sections. Section 2 discusses the unique issues posed by this class of problems, examines current solution approaches, and suggests an alternative that is motivated by recognized problems from previous research. Section 3 describes our approach, and discusses the theoretical bases used in its development. Section 4 demonstrates a specific instantiation of the approach to a real-world situation. Section 5 concludes the paper with a brief discussion of the applicability of our approach and directions for future research.

## 2. Optimization of combinatorial problems with multiple criteria

Due to their NP-completeness 18 , combinatorial<sup>w</sup> <sup>x</sup> problems are often tackled using a bounded approach <sup>w</sup> <sup>x</sup> <sup>w x</sup> 49 to locating optimal solutions 1 . Many such approaches often explicitly account for the possibility of error and uncertainty, espousing a more bounded interpretation of the notion of optimality. On the other hand, for problems involving multiple criteria, the general approach involves elicitation of the decision-maker’s preference structure, which is then applied to the alternatives at hand to arrive at the optimal solution. Quite often though, the preference structure can shift and adjust during the decision process 56 , and sometimes is not amenable to <sup>w</sup> <sup>x</sup> articulation. Decision-maker judgment is, then, essential in determining the most preferred solution. However, in combinatorially explosive situations, this approach to identifying the optimal most preferredŽ . quickly becomes infeasible. To deal with the combination of concerns presented by combinatorially explosive multiple criteria problems, traditional approaches in either research stream fall short.

## 2.1. Existing approaches

A few approaches have been proposed over the years to deal with ‘well-formulated’ problems in this class — that is, simplified along one<sup>r</sup>multiple dimensions to allow tractable solution procedures. They fall in three categories: analytical approaches, genetic algorithm-based approaches and heuristic approaches. Table 1 below shows some selected proposals from the first category.

One of the important results in MCDM theory, namely efficient solutions 19 , does not apply to <sup>w</sup> <sup>x</sup> 0–1 MCDM problems. This negates the use of parametric analysis of convex combinatorial problems in the search for efficient solutions where the decision variables are binary 44 , requiring compromises on<sup>w</sup> <sup>x</sup> the forms of objective functions or preference structures, or settling for possibly dominated solutions. Another set of approaches to solving 0–1 multiple criteria problems involves use of distance functions Žsee Ref. 51 for a discussion . These approaches<sup>w</sup> <sup>x</sup> . also require a priori information about the preference structure. Bowman 7 has proposed another ap- <sup>w</sup> <sup>x</sup> proach to the use of distance measures — the Tchebycheff norm — for finding efficient solutions Žsee Ref. 7 for an extended discussion . Various<sup>w</sup> <sup>x</sup> . forms of the Tchebycheff norm include optimization of a positive linear combination of the criteria, and minimization of weighted distances to a point that ‘‘slightly dominates’’ the ideal point Ref. 58 , p.Ž <sup>w</sup> <sup>x</sup> 35 . One disadvantage of the method is that the. solutions found are not necessarily efficient 52 . In<sup>w</sup> <sup>x</sup> summary, many of the analytical approaches require simplifying assumptions about problem structure, and add complexity to the solution procedure — without guaranteeing efficient solutions.

The second stream of research aimed at multicriteria optimization of large problems is referred to as multiobjective genetic optimization MOGA . ThisŽ . stream is characterized by approaches such as vector-evaluated genetic algorithms 45,46 , and itera-<sup>w</sup> <sup>x</sup> tive, rank-based methods 9,14 . These approaches <sup>w</sup> <sup>x</sup> represent application of the meta-heuristic of genetic algorithms in the specific context of MCDM problems. They are representative of the soft computing approach to multicriteria optimization 6 . Vectorevaluated genetic algorithm represents an extension of the genetic algorithm principles to accommodate vector-valued fitness measures. Schafer 46 proposes partitioning the population at each generation, thus creating sub-populations for each criteria; which are then merged to create the population at the next generation. This approach, however, implicitly assigns weights to the different criteria, which are determined by the previous generation of the population 45 . In some cases, the approach can lead to <sup>w</sup> <sup>x</sup> sub-populations species , each strong in one crite- Ž . rion to the detriment of others. Such speciation can conflict with the aim of finding a good compromise solution 14,46 .<sup>w</sup> <sup>x</sup>

Analytical solution approaches to multicriteria optimization

<table><tr><td>Researcher</td><td>Brief description of the technique</td></tr><tr><td>Pasternak and Passy [40]</td><td>Linear Objectives. Bicriterion. Systematically assign values of 0 or 1 to some components of x, examine feasibility with all other components at 1</td></tr><tr><td>Shapiro [47]</td><td>Convex Combination. Use of duality</td></tr><tr><td>Bitran [3,4]</td><td>Linear Objectives. First extension of implicit enumeration to MO problems</td></tr><tr><td>Lee and Morris [39]</td><td>Linear Objectives. Implicit enumeration. All objective functions must be non-decreasing in each component of x</td></tr><tr><td>Gabbani and Magazine [16]</td><td>Linear Objectives. Heuristics</td></tr><tr><td>Villareal and Karwan [57]</td><td>Non-linear Objectives. Preference Order Required. Branch and bound within dynamic programming. Reward function replaced by the preference order</td></tr><tr><td>Klein and Hannan [34]</td><td>Linear Objectives. Preference information obtained between Problems. Successive solution to single objective problems</td></tr><tr><td>Deckro and Winkofsky [12]</td><td>Implicit enumeration with bounding and preference directions</td></tr><tr><td>Kiziltan and Yucaoglu [33]</td><td>Linear Objectives. Extension of implicit enumeration. Each node in the tree represents partial solution</td></tr><tr><td>White [60]</td><td>Linear Objectives. Conversion to a Lagrangean problem</td></tr></table>

Fonseca and Fleming 14 propose a rank-based <sup>w</sup> <sup>x</sup> fitness assignment approach to overcome this problem. They propose an iterative approach that relies on a ranking obtained at each generation from the decision-maker to evolve a uniformly distributed representation of the global trade-off surface. Their proposals, thus, engage in progressive articulation of preferences from the decision-maker. They concede that this demands a significantly higher effort from the decision-maker and cite it as the main disadvantage of their approach. The assumption they make is that through the process of communication with the GA, the decision-maker gradually ‘‘refines preferences’’, until a suitable solution is found 14 . To<sup>w</sup> <sup>x</sup> address the concerns posed by a higher level of interaction, they find that an automated decisionmaker — such as an expert system — may be a useful addition to their proposals.

While this research stream see Fig. 2 belowŽ . addresses some of the concerns of the so-called ‘analytical’ approaches, it does not relax the assumption of non-availability of preferences. The class of problems we address in this paper relaxes this assumption fully to non-articulation of preferences, following Tversky and Simonson 56 see Appendix <sup>w</sup> <sup>x</sup> Ž B . The approaches described above use either an. implicit preference structure 46 or engage in pro- <sup>w</sup> <sup>x</sup> gressive articulation of preferences 14 . This, cou-<sup>w</sup> <sup>x</sup> pled with the significant amount of interaction required for these approaches Fonseca and Fleming Ž <sup>w</sup> <sup>x</sup> 14 indicate the need for an automated decisionmaker , make these approaches difficult to apply in. many situations. Moreover, the efficiency and performance of genetic algorithms is often dependent upon the coding mechanisms adopted 20 , making<sup>w</sup> <sup>x</sup> the generality of these approaches suspect.

![](/api/attachments/ZG9FW9SA/fulltext/images/4a4e1f171475002dfd5f2c6df95dcf62b3532f28f3e2f3a684eb18555b5b33d5.jpg)  
Fig. 2. MOGA approaches.

Yet another research stream that has attempted to address large scale multicriteria optimization is characterized by heuristic approaches. In contrast to the MOGA approaches, which represent application of the ‘meta’-heuristic of genetic algorithms, these ‘heuristic’ techniques act as essentially generators of ad hoc non-dominated alternatives within local regions, allowing the decision-maker to steer the solution in the required direction. Jain and Dutta 26 ,<sup>w</sup> <sup>x</sup> and Lee and Sheng 38 , for instance, have proposed <sup>w</sup> <sup>x</sup> techniques for local searches similar to Ref. 50Ž <sup>w</sup> <sup>x</sup>. based on user-specified tolerances. These techniques have been applied to solve problems in information system design 27 , and despite their simplicity, such<sup>w</sup> <sup>x</sup> approaches provide a powerful tool for analyzing large scale multiple criteria problems 59 . Fig. 3<sup>w</sup> <sup>x</sup> shows a prototypical representation of this approach.

White 59 points out that such techniques provide <sup>w</sup> <sup>x</sup> little confidence to the decision-maker:

In many methods the decision maker is asked to make statements about satisficing levels, or about which relaxations he is prepared to make for the various objective functions. How can the decision maker make such judgments if he does not know the implications of his statements in this matter in terms of the exclusion of better solutions?

White’s 59 comments can be interpreted to find<sup>w</sup> <sup>x</sup> another direction where further improvements will be helpful, namely including the decision-maker as an integral part of the decision process in multiple criteria situations. Over the years, other researchers have recognized similar problems. Keen 31 , for <sup>w</sup> <sup>x</sup> instance, argues for a ‘behaviorally grounded’ optimality. Torn 54,55 suggests that optimality for ¨ <sup>w</sup> <sup>x</sup> multiple criteria problems should be tied to the decision-maker’s ‘confidence.’ Ramesh et al. 43 argue<sup>w</sup> <sup>x</sup> that ‘‘the effectiveness of interactive methods to solve multicriteria decision problems depends on . . . confidence in the final solution’’. Korhonen <sup>w</sup> <sup>x</sup> 36 also acknowledges that though there are many mathematically challenging and important unresolved problems in the MCDM area, the emphasis has clearly shifted to ‘decision support.’ Dyer et al. <sup>w</sup> <sup>x</sup> 13 argue that ‘behavioral convergence’ is more important than mathematical convergence.

![](/api/attachments/ZG9FW9SA/fulltext/images/fe6e27f59efd4c042bd0ad77f98dc388ece960b758e64f6e5afb76f1d45e9bc3.jpg)  
Fig. 3. Heuristic approaches.

In sum, the three current sets of techniques — analytical, genetic algorithms-based, and as generators of non-dominated solutions — may be considered as widely varying approaches to solve large MCDM problems. They demonstrate varying adherence to the basic search philosophy of broad explorations followed by deep probes. The MOGA approach comes closest to this philosophy. While other approaches following this philosophy may be identified, the above three represent techniques that have been specifically adapted for application to large MCDM problems, and are appropriate precursors for our proposals.

## 2.2. OÕercoming problems with current approaches

The review reveals a number of concerns. The analytic approaches 60 require simplifying assump- <sup>w</sup> <sup>x</sup> tions about problem structure, and add complexity to the solution procedure, without guaranteeing efficient solutions. The genetic algorithms-based approaches 14 come closer to the class of problems<sup>w</sup> <sup>x</sup> considered in this research, but fail to effectively consider the non- availability of preferences. In- Ž . stead, they engage in implicit or progressive articulation of preferences, placing a significant burden on the decision-maker. The generator approaches 26<sup>w</sup> <sup>x</sup> provide the decision-maker with non-dominated solutions, but provide little additional knowledge about the quality of these solutions and<sup>r</sup>or implications of his<sup>r</sup>her choices. The key, we believe, lies in interpreting the solution space, including the areas that are not yet explored. Fonseca and Fleming 14 , for<sup>w</sup> <sup>x</sup> example, indicate that knowledge of areas that end up being discarded is of doubtful utility. We, on the other hand, contend that knowledge about areas probed as well as those that cannot be probed can be interpreted in a profitable manner in the decision process. We, thus, propose to interpret the information afforded by global and local searches andŽ . make it available to the decision-maker and allow him<sup>r</sup>her to direct the decision process, allowing the preferences to remain unarticulated 25 . Fig. 4 shows<sup>w</sup> <sup>x</sup> an outline of the proposed approach.

Juxtaposed against the genetic algorithm-based approaches Fig. 2 and the heuristic approaches Ž . Ž . Fig. 3 , Fig. 4 shows the enhancements proposed in our approach. First, a decision space is made available for each criterion, indicated by the arcs next to the respective axes. Second, interpretations of possible solutions guide the decision-maker in the decision process. A combination of these two provides the decision-maker the context to make effective decisions. Information about portions of the search spaces that are not yet explored or may never beŽ explored is useful since it allows the decision-maker. to evaluate the currently available alternatives. With this interpretation, the decision-maker can address issues such as — are time-consuming searches for better alternatives likely to pay off? and how do the current solutions compare to the as yet undiscovered solutions? Information about search spaces that are explored so far allows the decision-maker to address issues such as — how does the current solution perform compared to others close by? and will perturbations to the solution result in major changes to the criteria values? In other words, this intelligence helps the decision-maker in deciding the direction for further probes, or in making the decision to stop the search.

![](/api/attachments/ZG9FW9SA/fulltext/images/a003370d19653fb3318d02f0e9b6d27478d16ef8c5d84e639a6928e8e3f33696.jpg)  
Fig. 4. Proposed approach

These ideas sound deceptively simple. Operationalizing these, however, is not an easy task. It requires consideration of a number of interrelated procedural concerns, statistical problems and cognitive load issues. A judicious selection and combination of techniques is, therefore, necessary to operationalize the approach in a manner that is theoretically sound, logically consistent and efficient. We propose a multi-phase approach to operationalize these ideas. Though researchers have proposed multi-phase or iterative approaches, linkages between them have not been exploited in the manner we propose. Neither has knowledge acquired from the different phases been interpreted for the decision-maker, allowing him<sup>r</sup>her to make more informed decisions. Section 3 identifies various subtasks necessary to effectively operationalize our approach, investigates alternate theoretical bases for these tasks, and suggests preferred choices for developing the approach.

## 3. Proposed approach

The solution we propose is a general approach that addresses many of the concerns outlined and discussed in Section 2.2. Our solution approach builds on, adapts and refines ideas proposed by many researchers. Specifically, it extends the notion of decision spaces proposed by Gardiner 17 . Gardiner<sup>w</sup> <sup>x</sup> proposed use of the concept of a decision space to denote an approximation of the distribution values representing a weighted aggregation of multiple criteria. We, instead, propose to use the notion separately for each decision criterion. To construct these decision spaces, we adapt the BTM better thanŽ most notion of Baum et al. 1 , which in turn draws. <sup>w</sup> <sup>x</sup> on randomization approaches for combinatorial problems 29,30 . Our approach corresponds to the pro- <sup>w</sup> <sup>x</sup> posal by Torn 55 to tie the notion of optimality to¨ <sup>w</sup> <sup>x</sup> decision-maker confidence that such a solution has been obtained. We enhance this notion by providing the decision-maker intelligence that allows an informed judgment about whether such a solution has been obtained. Finally, we respond to the notion of behavioral convergence, which Dyer et al. 13 argue as more important than mathematical convergence <sup>w</sup> <sup>x</sup> 63 .

More specifically, we suggest an augmented multi-phase approach by enhancing the information provided to the decision-maker. This includes: aŽ . information about the likelihood of finding a solution that dominates the currently attractive solution, and Ž . b information about the likelihood of finding other non-dominated solutions. Operationally, the proposed approach provides the decision-maker knowledge about the totality of the search space, affords ample opportunities for exploration and probes of search spaces while maintaining the sense of place to find a reasonable solution, and feels that the chances of having any unexplored solutions that significantly dominate the current solution are low. In other words, it provides the decision-maker the ability to guide the search and make educated guesses for evaluating the solutions and for stopping or continuing the search.

To operationalize the ideas outlined above, we propose a two-stage procedure: broad exploration of the search space, and deep probes in promising regions of the search space see Fig. 5 . TheŽ . broad exploration phase involves characterization of decision spaces to create a context in which the decision-maker can make judgments, and answer the types of questions mentioned above. The deep probes represent a capability for systematic search of the multi-dimensional space surrounding a given alternative.

## 3.1. Broad exploration

The broad exploration phase seeks to provide the decision-maker an appreciation of the limits of the search space and its behavior in different regions or at different intervals. Since the number of alternatives can be extremely large, realistic estimates for this purpose can only be obtained by a systematic sampling of the search space. This needs careful consideration of a number of important sub-tasks such as: sampling strategy, feasibility checking, and decision space estimation.

## 3.1.1. Sampling strategy

The populations of interest to the decision-maker are criteria values. Since they represent transformations of the search space binary vectors , it is neces-Ž . sary to apply sampling to the underlying vector space. An implicit prerequisite for effective random sampling is the ability to select an element with uniform probability from the space under consideration 22 . Numerous techniques are available for<sup>w</sup> <sup>x</sup> random sampling from univariate distributions, using random number transformations 37 . No such ‘gen-<sup>w</sup> <sup>x</sup> eral’ methodology exists for random sampling from standard multivariate distributions Ref. 10 , p. 155 .Ž <sup>w</sup> <sup>x</sup> . The composition of the solution vector can, however, be exploited to devise an appropriate sampling procedure. Since each alternative can be represented as a binary vector, each element can be considered the outcome of a Bernoulli trial. A repeated random sampling from a Bernoulli distribution withŽ $p = 0 . 5 )$ followed by a concatenation, yields a random vector from the underlying vector space 23 , i.e., a specifi-<sup>w</sup> <sup>x</sup> cation of one alternative. Properties of vectors comprised of Bernoulli elements can be treated as analogous to a binomial distribution. Further, since we would like to ensure that the generated solution vectors represent extremes of value ranges, we can define such generation as ‘success,’ allowing us to treat the number of successful alternatives as a Poisson distribution. Then, using standard notation, a high probability of generating at least one solution in the upper p percent is given by: $1 - ( ( n p ) ^ { x } e ^ { - n p } ) /$ 0! . By selecting an appropriate confidence factor, an. appropriate sample size, n, can thus be computed. For instance, a sample of only 300 alternatives can yield solutions that exceed the 90th percentile both,Ž at the top and bottom , with a confidence of 95%. A. sample size of 1200 provides values in the top and bottom 95th percentile with the same level of confidence 53 . Selecting an appropriate sample size,<sup>w</sup> <sup>x</sup> then, requires choice of confidence levels and extreme value percentiles desired.

![](/api/attachments/ZG9FW9SA/fulltext/images/db35b4eb313bd0b65ecd018cd1a61fc987267d0f603707ed7c8edcf15c8bca23.jpg)  
Fig. 5. Operationalizing the approach.

## 3.1.2. Ensuring feasibility

It is important to check each sampled alternative for feasibility. This is relatively easily verified — by checking each generated vector to ensure that specified problem-specific constraints are met. For instance, for the object assignment problem we instantiated the approach for, ensuring feasibility meant that the sum of every five consecutive binary elements was at least equal to one that is, each objectŽ unit was assigned to at least one platform assuming five different computing platforms . If the problem . permits, and the search space is teeming with elements possessing the desired property, one can even dispense with checking feasibility 22 . An important<sup>w</sup> <sup>x</sup> assumption at work here is the existence of a large number of ‘feasible’ solutions to sample from. Studies 1 have shown that for effective sampling, it is<sup>w</sup> <sup>x</sup> necessary that feasible solutions constitute at least a modest fraction, say 1%, of the total random solutions generated — a condition quite easily met. For the object assignment problem considered, if there are M components to be allocated to N platforms, then the fraction of infeasible assignments is given by $[ ( 2 ^ { N } - 1 ) / 2 ^ { N } ] ^ { M }$ . For small M values, this may be a problem. However, for most common assignment problems Ž . M <sup>)</sup> 5 , this is clearly not an issue.

## 3.1.3. Decision space estimation

Based on the sample, an estimate of the decision space for each criterion can be computed. Ideally, a probability density function should be computed for each criterion. For the complex criteria formulations required by many real-world problems see Ap-Ž pendix B density estimation can, however, be diffi-. cult due to constraints on time and efforts and inadequate guarantees of correctness. A more feasible alternative is estimation of order statistics. Since combinatorial problems are characterized by a finite Ž . however large number of solutions, the distribution of solution values is bounded. For such distributions, the extreme values are equivalent to the points of truncation. An unbiased estimate of the extreme values can be found by computing extreme value statistics from repeated samples of size n, and applying the Weibull distribution 21 . Another technique,<sup>w</sup> <sup>x</sup> proposed by Dannenbring 11 , can also be employed <sup>w</sup> <sup>x</sup> due to its simplicity and flexibility. Using this technique, estimates of the extremes are computed as: $\theta _ { \operatorname* { m i n } } = 2 X _ { 1 } - X _ { 2 }$ and $\theta _ { \mathrm { m a x } } = 2 X _ { n } - X _ { n - 1 }$ where represents parameter estimates and $X _ { i }$ represents the ith order statistic derived from the sample. Finally, another issue to consider during decision space estimation is that of ‘scale.’ Since the criteria may have widely different value ranges e.g., response time Ž and cost , it is advisable to compute normalized. versions of values to ensure meaningful comparisons across criteria.

Fig. 6 shows a schematic outline of the tasks performed in this phase. The outcome of the ‘Broad

![](/api/attachments/ZG9FW9SA/fulltext/images/f9eff745093fbaae31c590d985daf127288b35aac311fa3deb8d351fab8e86c8.jpg)  
Fig. 6. Characterizing decision spaces.

Exploration’ phase is an approximate characterization of the decision space for each criterion. This phase may also involve tracking and compiling a pool of non-dominated solutions, which can be used as seed solutions for the next phase.

## 3.2. Deep probes

The second phase involves detailed probes of promising neighborhoods in the search space. The objective of this phase is to allow a guided and systematic exploration of alternatives in selected promising regions of the search space. It is facilitated by feedback and interpretation of the results obtained from each probe with the help of the decisionŽ spaces generated in phase one . This allows the. decision-maker to investigate if incremental improvements are possible around a current alternative; guide the search in the desired direction by specifying appropriate tolerances; ensure that no significantly better solutions exist in the vicinity; and assess the risk of overlooking other possibly attractive candidates by stopping the search. The sub-tasks of importance in this phase include: selection of seed solutions, local searches, interpretation of probe results and guided iteration.

## 3.2.1. Seed solutions

Conducting effective local searches requires identification of good starting points for new regions. Ideally, the initial seed solutions should represent non-dominated solutions from distinct and dissimilar regions of the search space. The pool of nondominated alternatives generated through randomŽ sampling in the previous phase provides an excel- . lent set of seed points. Since the solutions are nondominated, they also ensure that unnecessary efforts are not wasted in analyzing clearly inferior solutions. Other techniques such as multistart methods 5 ,<sup>w</sup> <sup>x</sup> simulated annealing 32 and <sup>w</sup> <sup>x</sup> <sup>r</sup>or computing measures of similarity across regions 50 may also be <sup>w</sup> <sup>x</sup> used for this purpose. The decision-maker can choose any of these as seed points to launch deep local probes, that is, fully search the region around the seed point by using a local search heuristic.

## 3.2.2. Local search heuristics

The local search heuristic conducts a systematic search around the indicated seed solution to identify non-dominated alternatives in the region. A commonly used local search technique for vector spaces is exchange search 26,38 . The heuristic exchanges<sup>w</sup> <sup>x</sup> the values of one or more variables with value 1 with one or more variables with value 0. For some problems, this technique may not be entirely appropriate, and a different heuristic may be applied. For instance, in an assignment problem, exchanging the third element in the vector with value 1 against the Ž . eleventh element with value 0 may translate to Ž . removing task ‘i’ from the responsibility list of person A and adding task ‘j’ to the responsibility list of person B. Such exchanges may not indicate meaningful local search. In such cases, a local search technique based on mutation may be used. Mutation is a widely accepted technique in the field of genetic algorithms 20 that is being adapted by other re- <sup>w</sup> <sup>x</sup> searchers 35 for performing local searches in com-<sup>w</sup> <sup>x</sup> binatorial optimization. In this technique, instead of exchanging elements within a vector, the values of vector elements are mutated in turn. This search technique has a much wider applicability. It can also reduce the real-time computational burden significantly, which may be a consideration in some cases. For instance, for a vector of size 300, a complete 1–1 exchange can easily result in generating upwards of 45,000 vectors. On the other hand, a 1-mutation would result in only 300 vectors. Though the probe results will depend on the topology of the n-dimensional space around the seed point; in general, generation of more vectors will lead to a higher number of non-dominated solutions. Thus, the cognitive load on the decision-maker must also be a factor in the choice of local search heuristic. To further ensure that the cognitive load on the decision-maker is reasonable, and to allow the decision-maker to guide the search in the desired direction, user-specified tolerances can be used to conduct the probes. For instance, the decision-maker may specify desired Ž . minimum improvements in certain criteria at the expense of maximum sacrifices in others. The probeŽ . can then retain only those non-dominated solutions that meet the specified tolerances. If the number of non-dominated solutions within tolerances is large Ž . or small , the decision-maker may choose to conduct the probe again while tightening or relaxing Ž . the tolerances.

## 3.2.3. Interpreting probe results

The results can be used to characterize the region around the seed solution and compare it to regions identified through other probes. Each alternative generated by the probe can also be interpreted using the decision spaces estimated in the first phase. For instance, consider a problem with three criteria, say, flexibility, dependability and performance. Using the decision spaces, a given alternative may be interpreted as: the possibility of improving flexibility is 30%, that of improving dependability is 25%, and that of improving performance is 35%. This information can be restated in two additional ways by treating the criteria evaluation functions as generators of elements in fuzzy sets 61 . First, the upper bound on<sup>w</sup> <sup>x</sup> possibility of generating a non-dominated solution in relation to the current solution can be stated as 35%. Second, a lower bound on the possibility of generating a solution that dominates the current solution can be stated as 25%.

As another example, consider a problem with three criteria, for which we have a solution X, with the following values: criterion C1 74 , criterion C2Ž . Ž . Ž . 92 , and criterion C3 83 . Since the scores are normalized, the values: 74, 92 and 83 represent the current level of achievement on each criteria. This immediately tells the decision-maker how good a solution is. In addition, the following information is available from the decision spaces computed in phase 1. For criterion C1, the probability of achieving a value <sup>)</sup>74 is 19%, for criterion C2, the probability of achieving a value <sup>)</sup>92 is 7%, and for criterion C3, the probability of achieving a value <sup>)</sup>83 is 23%. This provides the basis for computing fuzzy probabilities. The probability of finding another non-dominated solution with respect to X is simply 23% note that this actually represents the upperŽ limit ; whereas the probability of finding a solution. that dominates the current solution X is 7% again,Ž this represents the upper limit . Though the. decision-maker does not directly get the information about ‘‘distance’’ between the current values of the objective function in each criteria and the values of the criteria in a dominating solution. the maximum distance between the current solution and another that dominates it is bound by the scoring scheme. The probability of finding such a solution provided by our approach, in the limit, is 7%. In the absence of specific information regarding joint or conditional probability distributions, this estimation can provide useful bounds for assessing the relative worth of the current alternative. Incorporating the tolerances indi cated by the decision-maker can further refine both measures. In the absence of well-behaved criteria that lend themselves to algebraic manipulation of the n-dimensional search space — the fuzzy interpretations described above can perform adequately. Due to their simplicity, they can also entail negligible computational burden, that is, extremely quick response time.

## 3.2.4. Guided iteration

Using this additional information, and different seed points, the decision-maker can probe other promising regions of the search space. A solution obtained from a probe can also serve as the seed point for further probes — allowing the decisionmaker to steer the search in the desired direction. During this process, the decision-maker can make choices such as: probing a region multiple times by specifying different tolerances, discarding generated alternatives, or discarding complete regions. For this, the decision-maker can draw on information gathered earlier in the search process. During these tasks it is necessary to ensure non-dominance among alternatives generated from different probes, and keep track of additional statistics including: the number of regions probed; the number of alternatives on hand, etc. Fig. 7 shows a schematic outline of the operations necessary for this phase and their interrelationships to one another.

The ‘Deep Probes’ phase ends, at the discretion of the decision-maker, with generation of the final list of non-dominated solutions that the decisionmaker has retained. Based on the interpretations provided, the decision-maker may choose to stop the search and select one of the available solutions as the preferred solution. If, on the other hand, none of the current solutions provide the decision-maker with this sense of confidence, say, if the probability of finding a solution that dominates the current solution is above 15%, the decision-maker may conduct additional probes.

To recap, the enhancements we have suggested in the form of the two-phase solution procedure outlined above enhance the decision support in combinatorially explosive multiple criteria situations by allowing the decision-maker to make more informed decisions. The information can be classified in many different ways. In our opinion, the most relevant is the following classification: a information aboutŽ . decision spaces probed so far, and b informationŽ . about decision spaces not yet explored or thoseŽ which may never be explored . The information is. interpreted to allow the decision-maker to make informed decisions. Table 2 below summarizes the interpretations provided, and the corresponding decisions.

## 4. Application

To demonstrate feasibility of the approach, it was instantiated and implemented for a specific problem — effective distribution of object-oriented applications over a client<sup>r</sup>server architecture 42 . The spe-<sup>w</sup> <sup>x</sup> cific case used for testing the prototype required assignment of 119 application components object Ž fragments over five processor types — based on. four criteria: Match, Concurrency, Flow and Replication. The multiple criteria optimization problem formulation is shown in Fig. 8 below. Appendix C presents a representative session with the prototype.

![](/api/attachments/ZG9FW9SA/fulltext/images/7c57976c9e129abbb980fa6771fd325dcd17008af8b2330b438a2dc1e655cb6a.jpg)  
Fig. 7. Systematic local probes.

Table 2  
Proposed enhancements to the multi-phase approach

<table><tr><td>Interpretation</td><td>Decision aspect supported</td></tr><tr><td>Probability of finding non-dominated solutions in relation to the current solution</td><td>Assessing whether additional search is worth the effort</td></tr><tr><td>Probability of finding a solution that dominates the current solution</td><td>Assessing the risk associated with stopping the search</td></tr><tr><td>Range of values of other solutions in the neighborhood around the current solution</td><td>Deciding on the direction of search from the current solution</td></tr><tr><td>Number of alternatives within user-specified tolerances around the current solution</td><td>Assessing the robustness of the current solution within user-specified tolerances</td></tr></table>

The prototype was implemented on a desktop PC <sup>w</sup> <sup>x</sup> 41 . Numerical computations for evaluation functions, vector manipulations, dominance checks and search processes were implemented in C; data management was delegated to a relational database created in Paradoxe user interfaces were developed in ObjectPALe. Table 3 shows the decisions made to instantiate the approach while developing the prototype.

Fig. 9 shows decision spaces for the four criteria. The shape of the profile indicates the nature of distribution of generated values. Replication costs, with a linear evaluation function indicate a quasiregular distribution. Other criteria have a more skewed distribution, with Flow being the most skewed. The averages shown indicate deviation from a symmetrical distribution. Once again, Flow illustrates this effectively. The prototype, as implemented, does not contain a ‘zoom-in’ capability, since our primary focus was to test the feasibility of our proposals. Enhancing the prototype with this capability will reveal the differences more sharply and could afford better information to the designer.

The user interface for the deep probe process is captured in Fig. 10. Criteria values for the current alternative are displayed in the lower left portion of the window. These are presented in normalized form Ž . percentiles , to provide the decision-maker with a measure of the room for improvement on each criterion. The decision to retain the alternative invokes another window that indicates to the decision-maker two additional pieces of information: probability of generating a non-dominated solution compared to

$$
\begin{array}{l l} \text {Optimize} & Z = \left\{ \begin{array}{l l} f _ {\text {Match}} (x, y), \\ f _ {\text {Concur}} (x, y), \\ f _ {\text {Flow}} (x, y), \\ f _ {\text {Repl}} (x, y) \end{array} \right. \\ \text {subject to} & \sum_ {\mathbf {p} \in \mathbf {P}} X _ {\mathrm{ip}} \geq 1 \quad \forall i \in J, \end{array} \qquad \begin{array}{l l} & \text {non - linear evaluation function} \\ & \text {procedural evaluation function} \\ & \text {procedural evaluation function} \\ & \text {linear evaluation function} \end{array}
$$

where P: set of processor types, J: set of object fragments, M: set of methods

$\Chi _ { \mathsf { i p } } \ = 1$ if object fragment i is assigned to processor type p, 0 otherwise

$\mathrm { Y } _ { \mathrm { m p } } = 1$ if method m is assigned to processor type p, 0 otherwise

Fig. 8. Example application Purao et al. 42 . Ž <sup>w</sup> <sup>x</sup>.

Table 3  
Choices made for implementing the approach in the prototype

<table><tr><td colspan="2">Broad exploration</td></tr><tr><td>Sampling strategy</td><td>Repeated Samples, Percentiles 95%, Confidence Factor 95%</td></tr><tr><td>Ensuring feasibility</td><td>Application of Problem-specific Constraints</td></tr><tr><td>Decision space estimation</td><td>Order Statistics Estimators, Normalized Values</td></tr><tr><td colspan="2">Deep probes</td></tr><tr><td>Seed solutions</td><td>Initial seed solutions generated in Phase One</td></tr><tr><td>Local search heuristics</td><td>Mutation search with user-specified tolerances</td></tr><tr><td>Interpretations</td><td>Fuzzy sets</td></tr><tr><td>Iterations</td><td>User-specified</td></tr></table>

this solution, and probability of generating a solution that dominates this solution. Controls provided to the decision-maker in the form of buttons include theŽ . ability to retain promising solutions <sup>w</sup> <sup>x</sup> Save , eliminate less desirable ones  Discard , and search the neighborhood around the current solution by providing tolerances <sup>w</sup> <sup>x</sup> Probe . Information about alternatives generated in the current probe is summarized as a description of the current region, and is displayed in the upper left segment of the window. The average and high scores for each criterion provides the decision-maker with a set of reference points for assessing the desirability of the current solution. Aggregated information about the regions and overall set of alternatives examined so far is presented in the right panes of the window. The operations available to the decision-maker here include the capability to restart the session <sup>w</sup> <sup>x</sup> Restart Žif the decision-maker feels that the search has been relatively fruitless ,. save it for later continuation <sup>w</sup> <sup>x</sup> Save or to reexamine the saved search spaces <sup>w</sup> <sup>x</sup> Spaces .

The prototype was operated by one of the researchers to solve the complex object assignment problem in multiple sessions. However, since the user interface is graphical see Figs. 9 and 10 , and Ž . on-line help can be provided, use of the prototype by a typical decision-maker would be straightforward. Experience with the prototype to date indicates that the solution approach is practical in achieving its professed goals. It provides the decision-maker a sense of the totality of the search space as well as the capability to conduct deep local probes. For the test application described above, several sessions were conducted with the prototype. On average, about 11.3 regions were explored, including repeat probes in some regions, retaining, on average, 10.6 solutions in the final set of alternatives. A complete session conducted using the prototype is shown in Appendix C. A representative session began with a pool of 11 initial seed points generated in phase one. Probes were conducted in 10 regions, and repeated in two regions. Twenty-two additional non-dominated alternatives were generated, by specifying tolerances that ranged from <sup>y</sup>10% to <sup>q</sup>10%. The final shortlist contained seven alternatives, from which the decision-maker selected one final alternative. Fig. 11 below shows the final selection.

![](/api/attachments/ZG9FW9SA/fulltext/images/ab83aead9eb952765899bfd6d8570cff177c4865f760af56f820e837ab43a205.jpg)  
Fig. 9. User interface component — decision spaces.

![](/api/attachments/ZG9FW9SA/fulltext/images/8d1d36fa8a510816bc1c72f2c43136179674d283214a509ef4523fe714e7c47c.jpg)  
Fig. 10. User interface component — deep probes.

The alternative finally selected yielded achievement levels of 69, 91, 74 and 76, respectively, for match, concurrency, flow and replication. The probability of finding a non-dominated solution in relation to this solution was computed at 23% and finding a solution that dominates this solution was computed at 7%. Repeated local probes, with varying tolerances, ensured that the solution was robust, and would withstand minor local perturbations.

## 5. Conclusions

In all combinatorial problems, searching for optimal solutions is fraught with much risk and uncertainty. This is a problem endemic to search: with a world that is much larger than can be fully explored, one may have to resort to some guesswork, which may not lead to an optimal solution. Arguably, there are advantages to reducing the search, and yet occasionally, doing so may throw out the baby with the bathwater 24 . A good approach can recognize this<sup>w</sup> <sup>x</sup> and provide specific strategies that allow the decision-maker to gauge the impact of selecting an alternative or making the decision to stop the search. For multiple criteria problems, this is especially true, since the portion of the decision space that can be searched effectively is often a small fraction of the total search space.

![](/api/attachments/ZG9FW9SA/fulltext/images/db5fdbe0bd71db02d4c380e9900636e494d69ff58616e9c69290dbd2e4e8428a.jpg)  
Fig. 11. Characteristics of the final preferred solution see Appendix C . Ž .

Over the years, the multiple criteria decision making research stream has focused on techniques that facilitate tradeoffs to identify a compromise solution from a limited set of available candidates. If however, the problem being considered has an extremely large number of alternatives, results from this research stream cannot be directly applied. Related research streams such as application of genetic algorithms for multiobjective optimization have attempted to address this concern. However, these approaches are fraught with significant demands on decision-maker interaction. In this paper, we have presented a theoretically grounded approach for enhancing decision support in combinatorial problems involving multiple criteria. The central enhancement proposed in our approach is the interpretation and presentation of additional information, using fuzzy logic techniques, which the decision-maker can exploit to make better informed decisions. This is the primary contribution of our research.

The two-phase procedure we suggest for operationalizing the notion of increased decision-maker confidence uses a combination of broad exploration and deep probes — polar-opposite strategies for searching in huge spaces 24 . A judicious combina- <sup>w</sup> <sup>x</sup> tion of these two is necessary to effectively address the class of problems discussed in this research. The research identifies specific ways for linking these two strategies, specifies sub-tasks for effective implementation of each strategy, and suggests several alternatives for each sub-task drawing on and demonstrating ways of combining a number of different theoretical bases. This represents an additional contribution of our research. It is possible to instantiate the approach in several different ways by keeping in mind the issues we have discussed and<sup>r</sup>or by combining some of the techniques we have suggested. The approach is general enough that it can be applied in situations as diverse as decision making under time pressure, strategic decision making and planning problems. Due to its modest demands on decision-maker interaction, and its quantification of the risk associated with stopping the search, the approach can be adapted to a multitude of situations.

While operationalizing our approach, we have not relied upon any specific properties of the problem domain. In fact, the problem we have attempted to address is prototypical of the class of problems specified in Fig. 1, which includes: a criteria for-Ž . mulations that defy algebraic manipulations, bŽ . holistic interdependencies among decision criteria, and c unarticulated preferences among decision Ž . criteria. If any of these generalizing criteria are not required, a specific implementation can be easily tailored to a problem domain, further increasing its effectiveness. However, as a base case, we would expect the approach we have suggested to perform equally well in situations which generally exhibit multiple criteria and a combinatorially explosive search space.

Finally, the feasibility of the approach is demonstrated by a specific implementation of the approach and its application to a problem involving object distribution in a client<sup>r</sup>server environment. While an application of the approach cannot provide definitive validation, it provides an important start in demonstrating feasibility and utility. Additional applications of the approach are necessary to further confirm the effectiveness of the proposals in diverse problem domains. Our current research focuses on implementing some additional mechanisms that can be employed to improve the process, integration of data visualization tools and further empirical investigations of the prototype.

## Acknowledgements

We would like to thank Veda Storey for her comments on an earlier draft. This research was supported, in part, by a research grant from the College of Business Administration of Georgia State University. We would also like to thank the anonymous reviewers whose comments have helped in better focusing the paper. Specifically, we appreciate one reviewer’s suggestions about robustness and generalizability of this research. We are grateful to another reviewer for suggesting to us a comparison of this research against other similar approaches.

## Appendix A. Multiple criteria decision making: key definitions

Multiple criteria decision making involves the explicit recognition of a plurality of objectives in decision-making situations. An MCDM situation, by definition, consists of multiple criteria that cannot be optimized simultaneously — that is, it is either not feasible or not desirable to redefine the criteria into a single measurable criterion. A multiple criteria problem is generally represented as:

$$
\text { Optimize } \quad f (x) = \left\{f _ {1} (x), f _ {2} (x), \dots , f _ {k} (x) \right\},
$$

subject to $x \in X$

where x represents an n-dimensional vector of decision variables, X the search space, and $f ( x )$ a vector of k real-valued functions.

The formulation gives rise to the following definitions see Fig. 12 .Ž .

Definition 1: A solution $\pmb { \alpha } = \{ \alpha _ { 1 } , \alpha _ { 2 } , \dots , \alpha _ { n } \}$ is a feasible solution if $\pmb { \alpha } \in X$

Definition 2: A feasible solution  is dominated by another feasible solution iff ' $i \in { \bf K } | f _ { i } ( \pmb { \beta } ) >$ $f _ { i } ( { \pmb \alpha } )$ , and $\forall j \in k , j \neq i f _ { j } ( \pmb { \beta } ) \geq f _ { j } ( \pmb { \alpha } )$

Definition 3: A feasible solution  is efficient or non-dominated Ž .pareto-optimal iff no other feasible solution dominates it, that is, for any $x \in X , f _ { i } ( x ) >$ $f _ { i } ( { \pmb \alpha } )$ requires that $\exists j \in k , j \neq i | f _ { j } ( x ) < f _ { j } ( \pmb { \alpha } )$

Definition 4: The vector $\pmb { \beta } = \{ \beta _ { 1 } , \beta _ { 2 } , \dots , \beta _ { k } \}$ where $\beta _ { i } = \operatorname* { m a x } _ { x \in X } f _ { i } ( x )$ Ž is the ideal solution also known as the ideal alternative, superior solution, or bench-.mark , and is often denoted as $f ^ { * } ( x ) = \left\{ f _ { 1 } ^ { * } ( x ) \right.$ $f _ { 2 } ^ { * } ( x ) , \ldots , f _ { k } ^ { * } ( x ) \}$ . It is not a feasible solution, since the vector x that can generate $\pmb { \beta }$ does not exist in the search space.

Definition 5: A function Õ represents the decisionmaker’s preference structure iff: $f ( \alpha ) \sim f ( \beta )$ iff $v ( f ( \alpha ) ) = v ( f ( \beta ) ) \forall \alpha , \beta \in X$ , and $f ( \pmb { \alpha } ) _ { \gg } f ( \pmb { \beta } )$ iff $v ( f ( \alpha ) ) > v ( f ( \beta ) ) \forall \alpha , \beta \in X$ , where <sup>;</sup> represents indifference and » represents preference. A preference function requires assumptions of global preorder and regularity.

![](/api/attachments/ZG9FW9SA/fulltext/images/e60b4558bd647b146bab2be7cbd3667d8fa899d6722ccb9db3414ccc4ec3a354.jpg)  
Fig. 12. Multiple criteria optimization

Definition 6: The efficient solution ‘most preferred by the decision-maker is the optimal solution. It minimizes a given measure of distance from the ideal.

Appendix B. Ensuring generalizability of the class of problems addressed

To allow development of a general approach, we allow three additional properties to define the class of problems considered in this research. They are as follows.

## B.1. Complexity of eÕaluation functions

The evaluation function defines a mapping f on X that associates with every $x \in X$ a cost or utility. Since the x values are discrete, f may be a a Ž . simple linear transformation, or b a non-linearŽ . function approximated by a well-behaved continuous function. In both, f remains algebraically manipulatable. In many situations, however, f requires a procedural evaluation, especially when the criterion value results depend upon multiple elements in the solution vector. A procedural evaluation function is often not amenable to direct algebraic manipulation. If some of the multiple evaluation functions require procedural evaluation, a characterization of the n-dimensional search space cannot be derived without significant distortion.

## B.2. Nature of interactions among criteria

Furquhar 15 discusses different kinds of interac-<sup>w</sup> <sup>x</sup> tions: a artificial — induced by the particularŽ . analytic procedure and lacking substantive meaning, Ž . b ordinal — indicated by a disproportionate increase or decrease in preference without rank Ž switching for some criteria when conditioned on. different levels of other criteria, c configural —Ž . indicated by a switching of ranks for some criteria conditioned on levels of another criterion, and dŽ . holistic — apparent from a configural interaction among every subset of criteria. The last category presents the most difficult set of problems. It represents a situation where the evaluation criteria are not decomposable over the solution vector. The presence of such dependencies makes inter-criteria characterizations such as additive, multiplicative or even sup-Ž porting vs. conflicting impractical, since they can . vary widely over different ranges and at different points.

## B.3. Nature of the preference function

The preference function specifies how the decision-maker performs trade-offs among the different criteria. The literature 28,48 classifies preference <sup>w</sup> <sup>x</sup> elicitation techniques in three broad categories: a a Ž . priori articulation — articulation of preferences before commencing the decision process, b a posteri-Ž . ori articulation — articulation after identification of non-dominated solutions, and c progressive articu-Ž . lation — construction of the preference function based on the decision-maker’s choices. Some researchers such as Ref. 25 , suggest a fourth cate-Ž <sup>w</sup> <sup>x</sup>. gory: d no articulation of preference information Ž . the decision process simply aids the decisionmaker in minimizing an implicit, unarticulated distance from the ideal, without any attempt at quantification or characterization of the preference function. This category allows violations of regularity and global preorder 56 and recognition of the fact that<sup>w</sup> <sup>x</sup> the preference function may mutate over different value ranges of a criterion, and may not be well-behaved even within small ranges 2 . It does not force<sup>w</sup> <sup>x</sup> any preconceived preferences on the search process, and allows maximum freedom to the decision-maker.

## Appendix C. A sample session with the prototype

The following represents a sample session with the prototype, which includes the progression from early promising solutions to the eventual preferred solution. The pool of non-dominated solutions found in the first phase in shown in the table below. The solution numbers refer to the number from the sample generated to create the decision spaces Table 4 .Ž .

The table shows that solutions 4 and 7 sampleŽ numbers 381 and 961 have low values for objec- .

Table 4

<table><tr><td></td><td>Solution #</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td></tr><tr><td>1</td><td>30</td><td>69</td><td>59</td><td>29</td><td>59</td></tr><tr><td>2</td><td>121</td><td>26</td><td>79</td><td>79</td><td>65</td></tr><tr><td>3</td><td>351</td><td>73</td><td>61</td><td>28</td><td>73</td></tr><tr><td>4</td><td>381</td><td>08</td><td>20</td><td>72</td><td>73</td></tr><tr><td>5</td><td>775</td><td>66</td><td>56</td><td>58</td><td>32</td></tr><tr><td>6</td><td>937</td><td>50</td><td>33</td><td>72</td><td>59</td></tr><tr><td>7</td><td>961</td><td>78</td><td>14</td><td>32</td><td>42</td></tr><tr><td>8</td><td>973</td><td>77</td><td>37</td><td>48</td><td>43</td></tr><tr><td>9</td><td>983</td><td>53</td><td>43</td><td>58</td><td>47</td></tr><tr><td>10</td><td>986</td><td>55</td><td>40</td><td>68</td><td>47</td></tr><tr><td>11</td><td>973</td><td>64</td><td>31</td><td>57</td><td>35</td></tr></table>

tives 1 and 2, respectively, and may not prove to be good starting solutions. We, thus, elect to use solution 3 sample number 351 as the starting point forŽ . the search. The session is shown below with comments added.

The first probe, with starting solution 3 73, 61,Ž 28, 73 and tolerances . Ž . <sup>y</sup>05, <sup>y</sup>05, <sup>q</sup>10, <sup>y</sup>05 resulted in nine solutions. Of these, six are nondominated Table 5 .Ž .

As discussed in the paper, the probabilities P1 and P2 indicate the following. P1 is the upper limit on the Probability of finding a solution that dominates this solution, whereas P2 is the upper limit on the Probability of finding another non-dominated solution with respect to this solution. Two solutions Ž . N1P2 and N1P4 from this probe were retained for further consideration. Based on an examination of the solutions, the solution N1P4 is selected as the starting solution for the next probe. The probability of finding a solution that dominates this solution is lower 43.2% compared to the others, however,Ž . there is still up to a 20.5% probability of finding other non-dominated solutions with respect to this solution. The solution also represents the best improvement on the criterion Flow, which had a low value 28 in the initial solution. The next probe was,Ž . thus, conducted with this starting solution and revised tolerances Table 6 .Ž .

Table 5

<table><tr><td>Probe 1</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td><td></td><td></td></tr><tr><td>Base values</td><td>73</td><td>61</td><td>28</td><td>73</td><td></td><td></td></tr><tr><td>Tolerances</td><td>-05</td><td>-05</td><td>+10</td><td>-05</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="3">Within tolerance</td><td>9</td><td></td><td></td></tr><tr><td colspan="3">Non-dominated</td><td>6</td><td>P1</td><td>P2</td></tr><tr><td>N1P1</td><td>71</td><td>63</td><td>43</td><td>69</td><td>57.9%</td><td>31.5%</td></tr><tr><td>N1P2</td><td>72</td><td>61</td><td>46</td><td>69</td><td>54.9%</td><td>29.5%</td></tr><tr><td>N1P3</td><td>69</td><td>63</td><td>47</td><td>80</td><td>54.2%</td><td>20.5%</td></tr><tr><td>N1P4</td><td>70</td><td>61</td><td>59</td><td>80</td><td>43.2%</td><td>20.5%</td></tr><tr><td>N1P5</td><td>72</td><td>61</td><td>44</td><td>80</td><td>56.9%</td><td>20.5%</td></tr><tr><td>N1P6</td><td>73</td><td>61</td><td>40</td><td>78</td><td>60.9%</td><td>21.3%</td></tr><tr><td colspan="7">Current Pool Solution*</td></tr><tr><td>N0P3</td><td>73</td><td>61</td><td>28</td><td>73</td><td></td><td></td></tr><tr><td>N0P8</td><td>77</td><td>37</td><td>48</td><td>43</td><td></td><td></td></tr><tr><td>N1P2</td><td>72</td><td>61</td><td>46</td><td>69</td><td></td><td></td></tr><tr><td>N1P4</td><td>70</td><td>61</td><td>40</td><td>78</td><td></td><td></td></tr></table>

<sup>U</sup> Two solutions N0P3 and N0P8 were generated in the last Ž . phase, and two N1P2, N1P4 are from the first probe. Ž .

The direction of improvement on Flow was even greater on this probe, and this solution was retained in the pool. It was decided to use this solution as the starting solution in the next probe to gain an improved score in the second criterion, Concurrency. The tolerances for the next probe were, thus, specified as Ž . <sup>y</sup>00, <sup>q</sup>02, <sup>y</sup>02, <sup>y</sup>02 . The probe yielded two solutions and considerable improvement on the second criterion Table 7 .Ž .

Since solution N3P1 indicated a low P1 and a reasonable P2, it was used as the starting point for the next probe. Two probes, with varying tolerances were conducted see Table 8 below . Neither resultedŽ . in any solutions within tolerances.

Table 6

<table><tr><td>Probe 2</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td><td></td><td></td></tr><tr><td>Base values</td><td>70</td><td>61</td><td>59</td><td>80</td><td></td><td></td></tr><tr><td>Tolerances</td><td>-02</td><td>+02</td><td>+02</td><td>-05</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="3">Within tolerance</td><td>1</td><td></td><td></td></tr><tr><td colspan="3">Non-dominated</td><td>1</td><td>P1</td><td>P2</td></tr><tr><td>N2P1</td><td>68</td><td>63</td><td>74</td><td>76</td><td>23.5%</td><td>36.1%</td></tr><tr><td colspan="7">Current pool Solution</td></tr><tr><td>N0P3</td><td>73</td><td>61</td><td>28</td><td>73</td><td></td><td></td></tr><tr><td>N0P8</td><td>77</td><td>37</td><td>48</td><td>43</td><td></td><td></td></tr><tr><td>N1P2</td><td>72</td><td>61</td><td>46</td><td>69</td><td></td><td></td></tr><tr><td>N1P4</td><td>70</td><td>61</td><td>40</td><td>78</td><td></td><td></td></tr><tr><td>N2P1</td><td>68</td><td>63</td><td>74</td><td>76</td><td></td><td></td></tr></table>

Table 7

<table><tr><td>Probe 3</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td><td></td><td></td></tr><tr><td>Base values</td><td>68</td><td>63</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>Tolerances</td><td>-00</td><td>+02</td><td>-02</td><td>-02</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="3">Within tolerance</td><td>2</td><td></td><td></td></tr><tr><td colspan="3">Non-dominated</td><td>2</td><td>P1</td><td>P2</td></tr><tr><td>N3P1</td><td>69</td><td>91</td><td>74</td><td>76</td><td>6.8%</td><td>32.4%</td></tr><tr><td>N3P2</td><td>69</td><td>70</td><td>74</td><td>82</td><td>17.1%</td><td>32.4%</td></tr><tr><td colspan="7">Current pool Solution</td></tr><tr><td>N0P3</td><td>73</td><td>61</td><td>28</td><td>73</td><td></td><td></td></tr><tr><td>N0P8</td><td>77</td><td>37</td><td>48</td><td>43</td><td></td><td></td></tr><tr><td>N1P2</td><td>72</td><td>61</td><td>46</td><td>69</td><td></td><td></td></tr><tr><td>N1P4</td><td>70</td><td>61</td><td>40</td><td>78</td><td></td><td></td></tr><tr><td>N2P1*</td><td>68</td><td>63</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>N3P1</td><td>69</td><td>91</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>N3P2</td><td>69</td><td>70</td><td>74</td><td>76</td><td></td><td></td></tr></table>

<sup>U</sup> N2P1 is dominated by N3P1 and is discarded by the tool.  
Table 9

It was decided to use solution N3P2 as the starting solution for the next probe. Once again no new solutions were found. It was decided to relax the tolerances. The new probe yielded two nondominated solutions, within tolerances Table 9 .Ž .

Two additional probes were conducted, with N5P1 and N5P2 as seed solutions. The tolerances specified for each probe were Ž . <sup>q</sup>03, <sup>q</sup>03, <sup>y</sup>00, <sup>y</sup>02 and $( + 0 2 , + 0 2 , - 0 0 , - 0 1 )$ , respectively. Neither probe resulted in any solutions within tolerances. These probes, along with probes 4 and 5 above gave an impression of reaching a plateau in the search. It was decided to use the other starting solution from the pool solution 8, N0P8 to explore a different region Ž . of the search space.

Table 8

<table><tr><td>Probe 4.1</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td><td></td><td></td></tr><tr><td>Base values</td><td>69</td><td>91</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>Tolerances</td><td>+02</td><td>-05</td><td>+02</td><td>+02</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="2">Within tolerance</td><td></td><td>0</td><td></td><td></td></tr><tr><td colspan="2">Non-dominated</td><td></td><td>0</td><td>P1</td><td>P2</td></tr><tr><td colspan="7">Probe 4.2</td></tr><tr><td>Base values</td><td>69</td><td>91</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>Tolerances</td><td>+03</td><td>-10</td><td>+03</td><td>+03</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="2">Within tolerance</td><td></td><td>0</td><td></td><td></td></tr><tr><td colspan="2">Non-dominated</td><td></td><td>0</td><td>P1</td><td>P2</td></tr></table>

<table><tr><td>Probe 5.1</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td><td></td><td></td></tr><tr><td>Base values</td><td>69</td><td>70</td><td>74</td><td>82</td><td></td><td></td></tr><tr><td>Tolerances</td><td>+02</td><td>-00</td><td>-00</td><td>+02</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="2">Within tolerance</td><td colspan="2">0</td><td></td><td></td></tr><tr><td colspan="2">Non-dominated</td><td colspan="2">0</td><td>P1</td><td>P2</td></tr><tr><td colspan="7">Probe 5.2</td></tr><tr><td>Base values</td><td>69</td><td>91</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>Tolerances</td><td>+02</td><td>-02</td><td>-02</td><td>-02</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="2">Within tolerance</td><td colspan="2">0</td><td></td><td></td></tr><tr><td colspan="2">Non-dominated</td><td colspan="2">0</td><td>P1</td><td>P2</td></tr><tr><td>N5P1</td><td>71</td><td>70</td><td>74</td><td>83</td><td>16.2%</td><td>30.5%</td></tr><tr><td>N5P2</td><td>73</td><td>70</td><td>74</td><td>82</td><td>17.1%</td><td>30.4%</td></tr><tr><td colspan="7">Current pool Solution</td></tr><tr><td>N0P3*</td><td>73</td><td>61</td><td>28</td><td>73</td><td></td><td></td></tr><tr><td>N0P8</td><td>77</td><td>37</td><td>48</td><td>43</td><td></td><td></td></tr><tr><td>N1P2*</td><td>72</td><td>61</td><td>46</td><td>69</td><td></td><td></td></tr><tr><td>N1P4*</td><td>70</td><td>61</td><td>40</td><td>78</td><td></td><td></td></tr><tr><td>N3P1</td><td>69</td><td>91</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>N3P2*</td><td>69</td><td>70</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>N5P1</td><td>71</td><td>70</td><td>74</td><td>83</td><td></td><td></td></tr><tr><td>N5P2</td><td>73</td><td>70</td><td>74</td><td>82</td><td></td><td></td></tr></table>

The dominated solutions are discarded by the tool.

The first probe with this solution 77, 37, 48, 43 ,Ž . with tolerances Ž .<sup>y</sup>02, <sup>q</sup>10, <sup>y</sup>05, <sup>y</sup>05 did not yield any new solutions within tolerances. However, another probe, with different tolerances Ž<sup>y</sup>05, <sup>q</sup>02, <sup>q</sup>03, <sup>q</sup>02 resulted in two solutions Table 10 .. Ž .

It was decided to use solution N6P1 for the next probe. With the tolerances specified at Ž<sup>y</sup>02, <sup>q</sup>03, <sup>y</sup>10, <sup>q</sup>03 , two new non-dominated solutions were . found in this region Table 11 .Ž .

Solution N7P1 was used for the next probe, yielding no new solutions. Next, solution N7P2 was used for another probe, with tolerances $( - 0 2 , + 0 3 , - 1 0 ,$ <sup>q</sup>03 . This probe resulted in one new solution Ta- . Ž ble 12 ..

The new solution, N8P1 71, 56, 85, 64 was thenŽ . used to probe another region, with progressively relaxed tolerances. When repeated probes failed to produce any new solutions, it was decided to move to the final choice stage Table 13 .Ž .

Table 10

<table><tr><td>Probe 6.1</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td><td></td><td></td></tr><tr><td>Base values</td><td>77</td><td>37</td><td>48</td><td>43</td><td></td><td></td></tr><tr><td>Tolerances</td><td>-02</td><td>+10</td><td>-05</td><td>-05</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="2">Within tolerance</td><td colspan="2">0</td><td></td><td></td></tr><tr><td colspan="2">Non-dominated</td><td colspan="2">0</td><td>P1</td><td>P2</td></tr><tr><td colspan="7">Probe 6.2</td></tr><tr><td>Base values</td><td>77</td><td>37</td><td>48</td><td>43</td><td></td><td></td></tr><tr><td>Tolerances</td><td>-05</td><td>+02</td><td>+03</td><td>+02</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="2">Within tolerance</td><td colspan="2">2</td><td></td><td></td></tr><tr><td colspan="2">Non-dominated</td><td colspan="2">2</td><td>P1</td><td>P2</td></tr><tr><td>N6P1</td><td>73</td><td>39</td><td>85</td><td>49</td><td>15.9%</td><td>53.0%</td></tr><tr><td>N6P2</td><td>76</td><td>40</td><td>51</td><td>45</td><td>25.0%</td><td>60.3%</td></tr><tr><td colspan="7">Current Pool Solution</td></tr><tr><td>N0P8</td><td>77</td><td>37</td><td>48</td><td>43</td><td></td><td></td></tr><tr><td>N3P1</td><td>69</td><td>91</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>N5P1</td><td>71</td><td>70</td><td>74</td><td>83</td><td></td><td></td></tr><tr><td>N5P2</td><td>73</td><td>70</td><td>74</td><td>82</td><td></td><td></td></tr><tr><td>N6P1</td><td>73</td><td>39</td><td>85</td><td>49</td><td></td><td></td></tr><tr><td>N6P2</td><td>76</td><td>40</td><td>51</td><td>45</td><td></td><td></td></tr></table>

Like probes 4 and 5, this region of the search space gave the impression of having leveled off at this point. There were nine non-dominated solutions in the final pool. The available pool was characterized with simple measures of range Table 14 .Ž .

Table 11

<table><tr><td>Probe 7</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td><td></td><td></td></tr><tr><td>Base values</td><td>73</td><td>39</td><td>85</td><td>49</td><td></td><td></td></tr><tr><td>Tolerances</td><td>-02</td><td>+03</td><td>-10</td><td>+03</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="3">Within tolerance</td><td>3</td><td></td><td></td></tr><tr><td colspan="3">Non-dominated</td><td>2</td><td>P1</td><td>P2</td></tr><tr><td>N3P1</td><td>73</td><td>43</td><td>85</td><td>55</td><td>15.9%</td><td>56.9%</td></tr><tr><td>N3P2</td><td>72</td><td>46</td><td>85</td><td>56</td><td>15.9%</td><td>53.9%</td></tr><tr><td colspan="7">Current pool Solution</td></tr><tr><td>N0P8</td><td>77</td><td>37</td><td>48</td><td>43</td><td></td><td></td></tr><tr><td>N3P1</td><td>69</td><td>91</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>N5P1</td><td>71</td><td>70</td><td>74</td><td>83</td><td></td><td></td></tr><tr><td>N5P2</td><td>73</td><td>70</td><td>74</td><td>82</td><td></td><td></td></tr><tr><td>N6P1</td><td>73</td><td>39</td><td>85</td><td>49</td><td></td><td></td></tr><tr><td>N6P2</td><td>76</td><td>40</td><td>51</td><td>45</td><td></td><td></td></tr><tr><td>N7P1</td><td>73</td><td>43</td><td>85</td><td>55</td><td></td><td></td></tr><tr><td>N7P2</td><td>72</td><td>46</td><td>85</td><td>56</td><td></td><td></td></tr></table>

Table 12

<table><tr><td>Probe 8</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td><td></td><td></td></tr><tr><td>Base values</td><td>72</td><td>46</td><td>85</td><td>56</td><td></td><td></td></tr><tr><td>Tolerances</td><td>-02</td><td>+03</td><td>-10</td><td>+03</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="3">Within tolerance</td><td>3</td><td></td><td></td></tr><tr><td colspan="3">Non-dominated</td><td>2</td><td>P1</td><td>P2</td></tr><tr><td>N8P1</td><td>71</td><td>56</td><td>85</td><td>64</td><td>15.9%</td><td>42.6%</td></tr><tr><td colspan="7">Current pool Solution</td></tr><tr><td>N0P8</td><td>77</td><td>37</td><td>48</td><td>43</td><td></td><td></td></tr><tr><td>N3P1</td><td>69</td><td>91</td><td>74</td><td>76</td><td></td><td></td></tr><tr><td>N5P1</td><td>71</td><td>70</td><td>74</td><td>83</td><td></td><td></td></tr><tr><td>N5P2</td><td>73</td><td>70</td><td>74</td><td>82</td><td></td><td></td></tr><tr><td>N6P1</td><td>73</td><td>39</td><td>85</td><td>49</td><td></td><td></td></tr><tr><td>N6P2</td><td>76</td><td>40</td><td>51</td><td>45</td><td></td><td></td></tr><tr><td>N7P1</td><td>73</td><td>43</td><td>85</td><td>55</td><td></td><td></td></tr><tr><td>N7P2</td><td>72</td><td>46</td><td>85</td><td>56</td><td></td><td></td></tr><tr><td>N8P1</td><td>71</td><td>56</td><td>85</td><td>64</td><td></td><td></td></tr></table>

Of the solutions in the final pool, some had less than half the possible achievable score less than 50Ž . on the second criteria concurrency . These wereŽ . considered inadmissible and discarded from consideration. Of the remaining alternatives, solution N3P1 indicates that

Ž .a the probability of finding a solution that dominates this solution is 6.8%, and

Ž . b the probability of finding a non-dominated solution with reference to this solution is 32.4%.

Table 13

<table><tr><td>Probe 9.1</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td><td></td><td></td></tr><tr><td>Base values</td><td>71</td><td>56</td><td>85</td><td>64</td><td></td><td></td></tr><tr><td>Tolerances</td><td>-02</td><td>+03</td><td>-10</td><td>+03</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="2">Within tolerance</td><td></td><td>0</td><td></td><td></td></tr><tr><td colspan="2">Non-dominated</td><td></td><td>0</td><td>P1</td><td>P2</td></tr><tr><td colspan="7">Probe 9.2</td></tr><tr><td>Tolerances</td><td>-02</td><td>+02</td><td>-10</td><td>+02</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="2">Within tolerance</td><td></td><td>0</td><td></td><td></td></tr><tr><td colspan="2">Non-dominated</td><td></td><td>0</td><td>P1</td><td>P2</td></tr><tr><td colspan="7">Probe 9.3</td></tr><tr><td>Tolerances</td><td>-04</td><td>+04</td><td>-10</td><td>+02</td><td></td><td></td></tr><tr><td rowspan="2">Found</td><td colspan="2">Within tolerance</td><td></td><td>0</td><td></td><td></td></tr><tr><td colspan="2">Non-dominated</td><td></td><td>0</td><td>P1</td><td>P2</td></tr></table>

Table 14

<table><tr><td colspan="5">Solution pool</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td></td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td></tr><tr><td>Low</td><td>69</td><td>37</td><td>48</td><td>43</td><td></td><td></td><td></td></tr><tr><td>High</td><td>77</td><td>91</td><td>85</td><td>83</td><td></td><td></td><td></td></tr><tr><td>Average</td><td>72.8</td><td>54.7</td><td>73.4</td><td>61.4</td><td></td><td></td><td></td></tr><tr><td>Current pool Solution</td><td></td><td></td><td></td><td></td><td></td><td>Prob1</td><td>Prob2</td></tr><tr><td>N0P8</td><td>77</td><td>37</td><td>48</td><td>43</td><td>discarded</td><td></td><td></td></tr><tr><td>N3P1</td><td>69</td><td>91</td><td>74</td><td>76</td><td></td><td>6.8%</td><td>32.4%</td></tr><tr><td>N5P1</td><td>71</td><td>70</td><td>74</td><td>83</td><td></td><td>16.3%</td><td>30.5%</td></tr><tr><td>N5P2</td><td>73</td><td>70</td><td>74</td><td>82</td><td></td><td>17.1%</td><td>30.1%</td></tr><tr><td>N6P1</td><td>73</td><td>39</td><td>85</td><td>49</td><td>discarded</td><td></td><td></td></tr><tr><td>N6P2</td><td>76</td><td>40</td><td>51</td><td>45</td><td>discarded</td><td></td><td></td></tr><tr><td>N7P1</td><td>73</td><td>43</td><td>85</td><td>55</td><td>discarded</td><td></td><td></td></tr><tr><td>N7P2</td><td>72</td><td>46</td><td>85</td><td>56</td><td>discarded</td><td></td><td></td></tr><tr><td>N8P1</td><td>71</td><td>56</td><td>85</td><td>64</td><td></td><td>15.9%</td><td>42.6%</td></tr></table>

It was decided that the risks associated with stopping the search a less than 6.8% possibility that aŽ solution that is better on all criteria is reasonable. considering the complexity of the problem. The probability of overlooking other non-dominated solutions a less than 32.4% possibility that such solu-Ž tions may exist ..

## References

<sup>w</sup> <sup>x</sup> 1 S. Baum, W.R. Terry, U.N. Parekh, Random sampling approach to MCDM, in: J.N. Morse Ed. , Organizations: Mul-Ž . tiple Agents with Multiple Criteria, Springer-Verlag, Berlin, 1980, pp. 10–27.

<sup>w</sup> <sup>x</sup> 2 D.E. Bell, Explaining utility theory paradoxes by decision regrets, in: J.N. Morse Ed. , Organizations: Multiple AgentsŽ . with Multiple Criteria, Springer-Verlag, Berlin, 1980, pp. 28–39.

<sup>w</sup> <sup>x</sup> 3 G.B. Bitran, Linear multiple objective programs with zero– one variables, Mathematical Programming 13 1977 121–Ž . 139.

<sup>w</sup> <sup>x</sup> 4 G.B. Bitran, Theory and algorithms for linear multiple objective programs with zero–one variables, Mathematical Programming 17 1979 362–390.Ž .

<sup>w</sup> <sup>x</sup> 5 C.G.E. Boender, A.H.G. Rinooy Kan, Bayesian stopping rules for multistart global optimization methods, Mathematical Programming 37 1987 59–80.Ž .

<sup>w</sup> <sup>x</sup> 6 C. Bonissone, Soft computing: the convergence of emerging reasoning technologies, Soft Computing April 1997 , 6–18.Ž .

<sup>w</sup> <sup>x</sup> 7 V.J. Bowman, Jr., On the relationship of the Tchebyecheff norm and the efficient frontier to multiple criteria objectives, in: H. Thiriex, S. Zionts Eds. , Multiple Criteria DecisionŽ . Making, Springer-Verlag, Berlin, 1980, pp. 76–85.

<sup>w</sup> <sup>x</sup> 8 J.D. Camm, J. Evans, Management Science: Modeling, Analysis and Interpretation, South-Western College Publishing, Cincinnati, OH, 1996.

<sup>w</sup> <sup>x</sup> 9 A.J. Chipperfield, C.M. Fonseca, P.J. Fleming, Development of genetic optimization tools for multiobjective optimization problems in CACSD, IEE Colloquium on Genetic Algorithms for Control Systems Engineering, The Institute of Electrical Engineers Digest No. 1992<sup>r</sup>106, 1992, pp. 3<sup>r</sup>1– 3<sup>r</sup>6.

<sup>w</sup> <sup>x</sup> 10 J. Dagpunar, Principles of Random Variate Generation, Oxford Science Publications, 1988.

<sup>w</sup> <sup>x</sup> 11 D.G. Dannenbring, Procedures for estimating optimal solution values for large combinatorial problems, Management Science 23 1977 1273–1283.Ž .

<sup>w</sup> <sup>x</sup> 12 R. Deckro, E. Winkofsky, Solving zero–one multiple objective programs through implicit enumeration, European Journal of Operational Research 12 4 1983 362–374.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 J. Dyer, P. Fishburn, R. Steuer, J. Wallenius, S. Zionts, Multiple criteria decision making, multiattribute utility theory: the next ten years, Management Science 38 5 1992Ž . Ž . 645–654.

<sup>w</sup> <sup>x</sup> 14 C. Fonseca, P.J. Fleming, Genetic algorithms for multiobjective optimization: formulation, discussion and generalization, in: S. Forrest Ed. , Genetic Algorithms: Proceedings of the Ž . Fifth International Conference, Morgan Kaufmann, San Mateo, CA, July 1993.

<sup>w</sup> <sup>x</sup> 15 P.H., Furquhar, Interdependent criteria in utility analysis, in: S. Zionts Ed. , Multiple Criteria Problem Solving, Ž . Springer-Verlag, Berlin, 1977, pp. 131–180.

<sup>w</sup> <sup>x</sup> 16 D. Gabbani, M. Magazine, An Interactive Heuristic Ap-

proach for Multi-Objective Integer Programming Problems, Working paper, Department of Management Science, University of Waterloo, Canada, 1985.

<sup>w</sup> <sup>x</sup> 17 P.C. Gardiner, Decision spaces, IEEE Transactions on Systems, Man, and Cybernetics SMC-7 5 1977 340–349.Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 M.R. Garey, D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, Freeman, San Francisco, 1979.

<sup>w</sup> <sup>x</sup> 19 A.M. Geoffrion, Proper efficiency and the theory of vector maximization, Journal of Mathematical Analysis and Applications 22 1968 307–322.Ž .

<sup>w</sup> <sup>x</sup> 20 D.E. Goldberg, Zen and the art of genetic algorithms, Proceedings of the Third International Conference of Genetic Algorithms, Morgan Kaufmann, CA, 1989, pp. 80–85.

<sup>w</sup> <sup>x</sup> 21 E.J. Gumbel, Statistics of Extremes, Columbia Univ. Press, New York, 1958.

<sup>w</sup> <sup>x</sup> 22 R. Gupta, S.A. Smolka, S. Bhaskar, On randomization in sequential and distributed algorithms, ACM Computing Surveys 26 1 1994 7–86.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 T. Haas, Personal Communication, University of Wisconsin-Milwaukee, Milwaukee, WI, 1994.

<sup>w</sup> <sup>x</sup> 24 D. Hofstadter, Fluid Concepts and Creative Analogies: Computer Models of the Fundamental Mechanisms of Thought, Basic Books, NY, 1996.

<sup>w</sup> <sup>x</sup> 25 C. Hwang, L. Young-Jou, L. Ting-Yun, A new approach for multiple objective decision making, Computers and Operations Research 20 8 1993 889–899.Ž . Ž .

<sup>w</sup> <sup>x</sup> 26 H.K. Jain, A. Dutta, Distributed computer system design: a multicriteria decision-making methodology, Decision Sciences 17 4 1986 437–453.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 H. Jain, M.R. Tanniru, B. Fazlollahi, MCDM approach to generating and evaluating alternatives in requirements analysis, Information Systems Research 2 3 1991 223–239.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 R. Javalgi, H. Jain, Integrating multiple criteria decision making models into the decision support system framework for marketing decisions, Naval Research Logistics Quarterly 35 1988 575–596.Ž .

<sup>w</sup> <sup>x</sup> 29 R.M. Karp, On the complexity of combinatorial problems, Networks 5 1975 44–68.Ž .

<sup>w</sup> <sup>x</sup> 30 R.M. Karp, An Introduction to Randomized Algorithms, Technical Report TR-90-024, Computer Science Division, University of California, Berkeley, 1990.

<sup>w</sup> <sup>x</sup> 31 P.G.W. Keen, The evolving concept of optimality, in: M.K. Starr, M. Zeleny Eds. , TIMS Studies in the ManagementŽ . Sciences 6 1977 31–57.Ž .

<sup>w</sup> <sup>x</sup> 32 S. Kirkpatrick, C.D. Gelat Jr., M.P. Vecchi, Optimization by simulated annealing, Science 220 1983 671–680.Ž .

<sup>w</sup> <sup>x</sup> 33 G. Kiziltan, E. Yucaoglu, An algorithm for multiobjective zero–one linear programming, Management Science 29 12 Ž . Ž .1983 1444–1453.

<sup>w</sup> <sup>x</sup> 34 D. Klein, E. Hannan, An algorithm for the multiple objective integer linear programming problem, European Journal of Operational Research 9 4 1982 378–385.Ž . Ž .

<sup>w</sup> <sup>x</sup> 35 A. Kolen, E. Pesch, Genetic local search in combinatoria optimization, Discrete Applied Mathematics 48 1994 273– Ž . 284.

<sup>w</sup> <sup>x</sup> 36 P. Korhonen, Multiple criteria decision support: the state of

research and future directions, Computers and Operations Research 19 7 1992 549–551. Ž . Ž .

<sup>w</sup> <sup>x</sup> 37 A. Law, W. Kelton, Simulation Modeling and Analysis, 2nd edn., McGraw-Hill, CA, 1991.

<sup>w</sup> <sup>x</sup> 38 H. Lee, O. Sheng, A multiple criteria model for the allocation of data files in a distributed information system, Computers and Operations Research 19 1 1992 21–33.Ž . Ž .

<sup>w</sup> <sup>x</sup> 39 S. Lee, R. Morris, Integer goal programming methods, in: M.K. Starr, M. Zeleny Eds. , Multiple Criteria DecisionŽ . Making, North-Holland, New York, 1977, pp. 273–289.

<sup>w</sup> <sup>x</sup> 40 H. Pasternak, U. Passy, Bicriterion mathematical programs with Boolean variables, in: M.K. Starr, M. Zeleny Eds. ,Ž . Multiple Criteria Decision Making, University of South Carolina Press, 1975, pp. 327–348.

<sup>w</sup> <sup>x</sup> 41 S. Purao, A Methodology for Distribution of Object-oriented Applications, Unpublished PhD Dissertation, University of Wisconsin-Milwaukee, Milwaukee, WI, 1995.

<sup>w</sup> <sup>x</sup> 42 S. Purao, H.K. Jain, D.L. Nazareth, Effective Object Distribution in a Client<sup>r</sup>Server Setting, Georgia State University Working Paper, 1997.

<sup>w</sup> <sup>x</sup> 43 R. Ramesh, S. Zionts, M. Karwan, A class of practical interactive branch and bound algorithms for multicriteria integer programming, European Journal of Operational Research 26 1986 161–172.Ž .

<sup>w</sup> <sup>x</sup> 44 L.M. Rasmussen, Zero–one programming with multiple criteria, European Journal of Operational Research 26 1986Ž . 83–95.

<sup>w</sup> <sup>x</sup> 45 J.T. Richardson, M.R. Palmer, G. Liepins, M. Hilliard, Some Guidelines for genetic algorithms with penalty functions, in: J.D. Schaffer Ed. , Proceedings of Third International Con-Ž . ference on Genetic Algorithms, Morgan Kaufmann, San Mateo, CA, 1989.

<sup>w</sup> <sup>x</sup> 46 J.D. Schaffer, Multiple objective optimization with vector evaluated genetic algorithms, in: J.J. Grefenstette Ed. , Pro-Ž . ceedings of the First International Conference on Genetic Algorithms, Lawrence Erlbaum, 1985, pp. 93–100.

<sup>w</sup> <sup>x</sup> 47 J.F. Shapiro, Multiple criteria public investment decision making by mixed integer programming, in: H. Thiriez, S. Zionts, Eds. , Multiple Criteria Decision Making, Springer-Ž . Verlag, Berlin, 1976, pp. 170–181.

<sup>w</sup> <sup>x</sup> 48 W.S. Shin, A. Ravindran, A comparative study of interactive tradeoff cutting plane methods for MOMP, European Journal of Operational Research 56 3 1992 380–393.Ž . Ž .

<sup>w</sup> <sup>x</sup> 49 H.A. Simon, Models of Bounded Rationality, The MIT Press, Cambridge, MA, 1982.

<sup>w</sup> <sup>x</sup>50 M.K. Starr, L. Greenwood, Normative generation of alternatives with multiple criteria evaluation, in: M.K. Starr, M. Zeleny Eds. , Multiple Criteria Decision Making, TIMSŽ . Studies in Management Sciences, Vol. 6, North-Holland Publishing, Amsterdam, 1977, pp. 111–127.

<sup>w</sup> <sup>x</sup> 51 R.E. Steuer, Multiple Criteria Optimization: Theory, Computation and Application, Wiley, New York, 1986.

<sup>w</sup> <sup>x</sup>52 R.E. Steuer, E. Choo, An interactive weighted Tchebycheff procedure for multiple objective programming, Mathematical Programming 26 3 1983 326–344.Ž . Ž .

<sup>w</sup> <sup>x</sup> 53 E. Tanis, Statistics, Harcourt Brace & Co., New York, 1987.

<sup>w</sup> <sup>x</sup> 54 A.A. Torn, Optimality by Means of Confidence, FEI Work- ¨

<sub>ing</sub> <sub>Paper</sub> <sub>No.</sub> <sub>25,</sub> <sub>Abo</sub> <sub>Swedish</sub> <sub>University</sub> <sub>School</sub> <sub>of</sub> <sub>Eco-</sub> ˚ nomics, 1978, pp. 1–8.

<sup>w</sup> <sup>x</sup> 55 A.A. Torn, A sampling-search-clustering approach for ex- ¨ ploring the feasible<sup>r</sup>efficient solutions of MCDM problems, Computers and Operations Research 7 1980 67–79.Ž .

56 A. Tversky, I. Simonson, Context-dependent preferences, Management Science 39 10 1993 1179–1189.Ž . Ž .

<sup>w</sup> <sup>x</sup> 57 B. Villareal, M. Karwan, Multicriteria integer programming: a hybrid dynamic programming recursive approach, Mathe-Ž . matical Programming 21 1981 204–223.Ž .

<sup>w</sup> <sup>x</sup> 58 P. Vincke, Multicriteria Decision-Aid, Wiley, NY, 1992.

<sup>w</sup> <sup>x</sup> 59 D.J. White, 1982, The foundations of multi-objective interactive programming — some questions, in: P. Hansen Ed. ,Ž . Essays and Surveys on Multiple Criteria Decision Making, Springer-Verlag, pp. 406–415.

<sup>w</sup> <sup>x</sup> 60 J.P. White, A multiple objective interactive Lagrangean relaxation approach, European Journal of Operational Research 19 1 1985 82–90.Ž . Ž .

<sup>w</sup> <sup>x</sup> 61 L.A. Zadeh, Fuzzy sets, Information and Control 8 1965Ž . 338–353.

<sup>w</sup> <sup>x</sup> 62 S.H. Zanakis, J.R. Evans, A.A. Vazacopoulos, Heuristic methods and applications: a categorized survey, European Journal of Operational Research 43 1989 88–110.Ž .

<sup>w</sup> <sup>x</sup> 63 M. Zeleny, An essay into a philosophy of MCDM: a way of thinking or another algorithm?, Computers and Operations Research 19 7 1992 563–566.Ž . Ž .

![](/api/attachments/ZG9FW9SA/fulltext/images/6ae33e98cfb2d10d719123d4f845f83f1d73e8feca88f7dc7b39cf34f8385b25.jpg)  
Sandeep Purao holds a PhD in MIS from the University of Wisconsin-Milwaukee. His research focuses on various aspects of information system design, with particular emphasis on object-oriented systems. His work has appeared in several journals such as Communications of the ACM, DataBase, Information and Management and Journal of Education for MIS. His current research interests include reusebased design with analysis patterns,

knowledge management for IS design and studies of complex design tasks. He is an Assistant Professor of Computer Information Systems at the J. Mack Robinson School of Business at Georgia State University, Atlanta, GA.

![](/api/attachments/ZG9FW9SA/fulltext/images/4bd1a2682ecb98de93689801727bde214d9940da26e47d8f67f4c748e4498f5e.jpg)

Hemant Jain is Lawrence G. Regner Research Professor of Management Information System in the School of Business Administration at the University of Wisconsin-Milwaukee. Professor Jain is also a director of UWM MIS Consortium, a partnership between the University and MIS community. Prof. Jain received his PhD in information system from Lehigh University in 1981, a M. Tech in Industrial Engineering from I.I.T. Kharagpur India and BS in Me-Ž .

chanical Engineering from University of Indore India . Prof.Ž . Jain’s interests are in the area of electronic commerce, system development using reusable components, multi-criteria decision making, distributed and co-operative computing systems, architecture design, database management and data warehousing. Data mining and visualization. He has published large number of articles in Information Systems Research, MIS Quarterly, IEEE transactions on Software Engineering, NaÕal Research Quarterly, Decision Sciences, Decision Support Systems, Information and Management, etc. Prof. Jain is on the editorial board of the Journal of Database Management, Information Technology and Management and is book review editor for Journal of Information Technology Cases and Applications.

![](/api/attachments/ZG9FW9SA/fulltext/images/b7d4264e80c7008d91f5e65732946b24d936f771e0c767dafe14e316dcea5d8c.jpg)

Derek L. Nazareth is Associate Professor of Management Information Systems at the University of Wisconsin-Milwaukee. He holds a Ph.D. in Management from Case Western Reserve University. He has published in Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Knowledge Acquisition, OMEGA, among others. His current research interests include data warehousing, distributed object systems, and knowledge

base verification. He is a member of AIS, AAAI, IEEE Computer Society, and INFORMS, and is the program chair for the AMCIS 1999 Conference.
