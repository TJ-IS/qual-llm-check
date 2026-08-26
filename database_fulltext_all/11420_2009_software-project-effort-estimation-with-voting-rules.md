---
otero_id: 11420
otero_key: "MJY6WNH3"
title: "Software project effort estimation with voting rules"
authors: "Stefan Koch; Johann Mitlöhner"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.12.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Software project effort estimation with voting rules

Stefan Koch <sup>a,</sup>⁎, Johann Mitlöhner

<sup>a</sup> Bogazici University, Istanbul, Turkey

<sup>b</sup> Vienna University of Economics and Business Administration, Vienna, Austria

## a r t i c l e i n f o

Article history: Received 4 June 2008 Received in revised form 27 November 2008 Accepted 12 December 2008 Available online 24 December 2008

Index terms: Cost estimation Product metrics Evolutionary computing Genetic algorithms Social choice

## a b s t r a c t

Social choice deals with aggregating the preferences of a number of voters into a collective preference. We will use this idea for software project effort estimation, substituting the voters by project attributes. Therefore, instead of supplying numeric values for various project attributes that are then used in regression or similar methods, a new project only needs to be placed into one ranking per attribute, necessitating only ordinal values. Using the resulting aggregate ranking the new project is again placed between other projects whose actual expended effort can be used to derive an estimation. In this paper we will present this method and extensions using weightings derived from genetic algorithms. We detail a validation based on several well-known data sets and show that estimation accuracy similar to classic methods can be achieved with considerably lower demands on input data.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

The estimation of effort, duration and costs for developing information systems has been a topic of research for a long time [16]. This has led to the development of several methods for effort estimation [5], including the well-known COCOMO [3], its update COCOMO II [4], approaches based on the function point metric [1,21], and models based on machine-learning concepts [35].

Nevertheless, the predictive quality and usage [14] has still been limited, as exempli<sup>fi</sup>ed by many software projects running over budget or allotted time frame [34]. The reasons for these problems are manifold, including the inherent uncertainty of software development, and the huge diversity in projects and adopted processes, which necessitate careful adaptation and calibration of models. Another problem especially of algorithmic models is the speci<sup>fi</sup>cation of the necessary input parameters like size, which is dif<sup>fi</sup>cult to determine at project start [12]. Also, algorithmic models are mostly limited to one major cost driver, most often size for example using lines-of-code, complemented with a small number of other in<sup>fl</sup>uence factors.

Advantages of machine-learning approaches are among others that a wide range of metrics can be employed to characterize a software project. Also Kitchenham and Mendes [17] have argued that multidimensional output metrics are necessary to capture the full richness of software development. Problems of some of these approaches are on the one hand the necessary data base of appropriate projects, and that the exact computation is sometimes dif<sup>fi</sup>cult to grasp, which might lead to a decrease in acceptance, especially at the management level.

In this paper we will argue to adopt techniques from the area of social choice for effort estimation. The advantage is that while arbitrary metrics can be used in arriving at an estimation, the process is fully transparent and easily understood. In addition, ranking projects by attributes is much easier than providing numeric values for project attributes, a task that is often daunting for project managers and experts. The approach described here is most akin to analogy-based estimation, with some differences as will be described here. We will also provide a discussion of the paired comparisons proposed by Miranda [22] for estimation, inspired by the analytic hierarchy process [28].

The structure of the paper is as follows: in the next section, an overview of related work will be given, followed by an introduction to the topic and the techniques of social choice. Next, we will apply the concepts of social choice to effort estimation, discussing both the basic approach proposed and some re<sup>fi</sup>nements. We will then describe the data sets used for validating the effort estimation procedure and provide an analysis of the results. The paper will end with conclusions and directions for future research.

## 2. Related work

Many models have been proposed to estimate the effort in software development. Maybe the best known is COCOMO [3] which uses a micture of algorithmic formulae and expert judgment. One drawback was that the quanti<sup>fi</sup>cation of size in lines-of-code (kilo delivered source instructions, KDSI) was necessary as an input parameter. Over the years, function points [1] and its many variants like most recently class points [8] have emerged as a way of quantifying this size, and have been adopted for the update COCOMO II [4]. Other models proposed include Putnam's model [24], and also proprietary versions like SLIM or ESTIMACS. In addition, a class of models has been developed based on machine-learning concepts [35]. The proposed methods have used, among others, neural nets [20,35], regression trees [30] or case-based reasoning, respectively analogybased estimation [32,31,23]. These models have the advantage of allowing for a much wider selection of possible project characteristics to include, which seems especially important for some kinds of development less focused on source code development like ERP (enterprise resource planning), web applications or similar. Nevertheless, in almost all approaches some input parameters need to be speci<sup>fi</sup>ed numerically on a rational scale, which can pose a major problem in a real-world setting. In the approach we present here a new project only needs to be placed into one ranking of old projects per attribute, necessitating only ordinally scaled values.

The approaches in effort estimation showing the most semblance to the method presented here are analogy-based estimation [32,31,23] and paired comparisons [22]. Both social choice and analogy-based approaches can deal with any number of variables, and search for the most similar projects. On the other hand, analogy-based estimation necessitates that the values of the different variables are expressed for the project to be estimated on a rational scale, and similarity is computed based on the Euclidean distance in the resulting ndimensional space. In the social choice approach, projects only need to be ranked according to each attribute, then the different rankings are aggregated to determine similar projects.

The estimation approach presented by Miranda [22] based on AHP [28] is detailed for the case of size estimations. Using comparisons between each of the entities with a given limited verbal scale (‘equal,’ ‘slightly/much/extremely,’ ‘smaller/bigger’) results in a vector of weights which can be used to arrive at estimates for the size of all entities, if at least one reference point out of them is known. The semblance to social choice lies mostly in the fact that no quanti<sup>fi</sup>cation is needed from the user, only comparisons. In fact, the resulting vector is a form of ranking. The difference lies mostly in the fact that this approach is geared towards estimating a single attribute for several entities based on a single reference point, while social choice as described uses an arbitrary list of variables and aggregates the resulting ranking, thus leading to an overall picture and an effort estimate, but only for a single new project at a time; and since there are only weak preference assertions there is no need for a translation of verbal scales into numeric values as in AHP and similar methods.

Also some semblance in the usage of categorical variables can be identi<sup>fi</sup>ed with COBRA (Cost Estimation Benchmarking and Risk Analysis), which is a hybrid cost estimation method combining algorithmic and experiential approaches [6]. For producing cost overhead estimates, a causal model is built with experts to identify cost drivers, the effects of which are then modeled as triangular distributions. Combined with a relationship between cost overhead and productivity, an estimation is produced using parameters for the triangular distributions and employing Monte Carlo simulation. This approach was also adapted and used for web applications [26,25]. This approach has some similarities in that no exact quanti<sup>fi</sup>cations are necessary, and might be more usable in environments with only a small number of completed projects.

## 3. Social choice

In social choice voters express preferences over a set of candidates, and some aggregation algorithm (a voting rule) is used to <sup>fi</sup>nd a corresponding aggregate ranking and a winner, or a set of winners [27,9,33]. The notation x≻y is used to indicate that x is preferred to y, while x⪰y indicates that y is not preferred to x, and x∼y indicates indifference. A social choice problem is usually de<sup>fi</sup>ned by a set of n voters providing rankings for m alternatives, resulting in a “pro<sup>fi</sup>le,” e.g., for alternatives a, b, c and rankings a≻b≻c, b≻c≻a, c≻a≻b, $b { \succ } c { \succ } a .$ , the problem of rank aggregation consists of <sup>fi</sup>nding an aggregate ranking x⪰y⪰z such that the preferences stated by the voters are expressed in the aggregate ranking; e. g., a suitable aggregation from the example above is b≻c≻a, where alternative b is the only element in the winner set. An aggregation resulting from the application of a voting rule may contain indifferences, and the winner set may contain more than one alternative.

Pro<sup>fi</sup>les are often assumed to consist of strict orderings only; however, in this work we allow for indifferences in the input rankings, such as $x \succ ( y \sim z )$ which means that in this ranking the alternatives y and z are considered equal, while x is better than both y and z. As will be shown, allowing for indifferences is a practical precondition for applying social choice methods in project effort estimation.

There are several demands that are usually placed on voting rules. One of the most important demands is the Condorcet criterion: if an alternative x exists that beats all other alternatives in pairwise comparisons then x is a Condorcet winner [11], and an obvious demand on an aggregation rule is that it select x as the winner. Another demand on aggregation rules is that the aggregate relation should not contain any cycles and represent a complete (possibly weak) order of the alternatives. Voting rules ful<sup>fi</sup>ll these demands to differing degrees.

Not all social choice voting rules support weak rankings, as we will employ in this application. The following description gives a short overview of some voting rules from social choice theory that are based on margins; these rules allow for resolving indifferences in an easy and intuitive way. The margin of alternative x versus y is M(x,y)= $| x > y | - | y succ x | ,$ , where |x≻y| is the number of rankings where x is preferred to y. Rankings with indifference x∼ y do not contribute to the margins.

Simple Majority (SM): the simple majority rule is probably the most well-known procedure based on margins: a positive margin means that x wins against y in pairwise comparison and results in x≻y in the aggregate relation, a negative margins leads to y≻x, and a zero margin means indifference x∼y. Unfortunately, this rule can result in cycles in the aggregate preference relation, such as x≻y, y≻z, z≻x (drop the fourth voter from the example given above to arrive at a cycle). This limits the use of the simple majority rule in practical applications, and it will not be used in this work.

Copeland (CO): the Copeland rule scores the alternatives with the sum over the signs of the margins they achieve and ranks them according to those scores.

Maximin (MM): the Maximin rule scores the alternatives with the worst margin they each achieve and ranks them according to those scores.

Borda (BO): the Borda rule assigns linearly decreasing points to consecutive positions, e.g., for three alternatives the points would be 2 for <sup>fi</sup>rst place, 1 for second place, and 0 for third place. The alternatives are then ranked according to their total sums of scores over all voters. The Borda relation can also be computed from the margins alone; see, e.g., [18].

Since the aggregate relations of the Maximin, Copeland, and Borda rules are based on numeric scores they can always be expressed as complete weak preference orders, i.e. they can contain indifferences, but not cycles or intransitivities.

The rules described above will generally produce similar results for identical pro<sup>fi</sup>les; however, e.g., for the pro<sup>fi</sup>le ((a ≻ d ≻ c ≻ b), $( b \succ a \succ d / c ) , ( b \succ a \succ c \succ d ) )$ the margins are ((0,−1,3,3), (1,0,1,1), (−3, $- 1 , 0 , - 1 ) , ( - 3 , - 1 , 1 , 0 ) )$ , and the aggregate rankings are $( b { \succ } a { \succ } d { \succ } c )$ for CO, $( b { > } a { > } ( c { \sim } d ) )$ for MM, and $( a { > } b { > } d { > } c )$ for BO, i.e. the Maximin rule selects the same winner as the Copeland rule but introduces an indifference in c and d, while the Borda rule selects candidate a instead of b as the winner. More details on these and other commonly used voting rules and their properties can be found, e.g., in [11] and [27]. Some observations on the proximity of the results which the rules mentioned deliver can be found in [10].

## 4. Effort estimation based on social choice

For using social choice in effort estimation we will employ a basic analogy: voting rules can be used for effort estimation by replacing voters with project attributes. This means that each attribute considered provides a ranking of all projects available in the data base. Since indifferences are allowed it is straightforward to obtain a weak ranking from numeric project attributes; this is the method we will apply in our ex-post study. However, note that an ordinal scale is suf<sup>fi</sup>cient for the application of these methods: experts need only supply rankings for past projects in terms of the various attributes, which simpli<sup>fi</sup>es the gathering of input data. Each ranking therefore gives the impression of “size” or “complexity” of the projects according to one attribute. The aggregated ranking of all attributes will then represent an overall picture of the projects' “complexity,” and thus a ranking of the efforts necessary to implement them.

For estimating a new project the process is straightforward: according to each attribute, the project is put into the respective ranking of all old projects. Therefore, no quanti<sup>fi</sup>cation is necessary, the project is simply ranked among the existing projects. After this has been accomplished for all attributes, an aggregation rule is employed to arrive at an aggregate ranking. In this aggregate ranking the new project again is ranked with other projects whose actual efforts are known; therefore we have a ranking that indicates the effort of the new project, such as an upper and lower bound given by the old projects it has as neighbours, and we can compute the mean to arrive at a single value.

Naturally, this approach is dependent on the availability of a data set which covers the respective population of projects to be considered. Similar to machine-learning approaches, predictive quality is heavily in<sup>fl</sup>uenced by the similarity of the new project to be estimated to the projects in the data set. If the new project is an outlier, the prediction will be off target.

We will discuss this with a small example <sup>fi</sup>rst (see Fig. 1) before moving to the validation using large data sets. In this example, we know 3 projects (A, B and C) with their actual effort, their size in function points [1] and their required reliability. Project A has 1500 function points, medium required reliability and actual effort of 150 person-months, B has 1200 function points, low required reliability and 80 person-months, and C 900 function points, high required reliability and 72 person-months. This results in the ranking A≻B≻C for the “voter” function points, and C≻A≻B for reliability. If we want to derive an effort estimation for a new project D we need to place it into these rankings. First we determine that the function point count will be smaller than A, but larger than B, resulting in the new ranking $A { > } D { > } B { > } C .$ The reliability is equivalent to A, resulting in the second ranking $C \succ ( A \sim D ) \succ B$ . Using a social choice voting rule, for example the Borda rule, results in an aggregate ranking of $A { > } D { > } C { > } B .$ We see that D is ranked between A and C, so the effort is estimated to be between their values of 150 and 72, or the mean 111 if a single value is needed. If D were to be ranked <sup>fi</sup>rst or last in the aggregate ranking, the effort of the only neighbour would be used for estimation.

## 4.1. Binary model

When we apply this method of simply using all available characteristics to a data set we achieve very unsatisfactory accuracies; like linear regression and similar methods we need some way of weighting to account for the fact that the available project attributes are not equally important for effort estimation. Therefore we allow for some project attributes to be deleted from the set used, which means that they are not included in the aggregation. There are several ways of determining the attributes to delete, with the <sup>fi</sup>rst one being an inspection of the respective correlation coef<sup>fi</sup>cients of attributes with the expended effort. Those attributes with lower or no correlation can be excluded. The other approach is to select the set of attributes that, based on the available data set, gives the best predictive quality. This could even be determined by enumeration, if the number of attributes is reasonably small, or other approaches like genetic programming.

## 4.2. Weighted model

To further improve the proposed method each attribute is assigned a weight, e.g., between 0 (resulting in exclusion) and 99, as some attributes clearly have a stronger relationship to resulting effort than others. This translates into having more voters than attributes, with several voters giving their ranking according to a single attribute. For example, we might include <sup>fi</sup>ve voters using a ranking based on function points, while only two use the programmer capability. This corresponds to different weights assigned to the attributes. Using the ranking of known projects according to their actual expended efforts as “target” aggregate ranking, these weights, i.e. the number of voters, can be optimized using appropriate techniques. We want to select the weights in a way that minimizes overall estimation error.

We use a genetic algorithm to arrive at a near-optimal solution [13]. Genetic algorithms have already been applied in software project effort estimation in [7] showing promising results, and in [15] in connection with grey relational analysis. The population of solutions consists of integer vectors denoting the weights of each of the project attributes. Starting with a population of random weight vectors we assign <sup>fi</sup>tness values to each solution by calculating the estimation

Data base: 3 projects A, B, C with size in function points, required reliability, and actual effort

<table><tr><td></td><td>Project A</td><td>Project B</td><td>Project C</td><td>Ranking</td></tr><tr><td>Function Points</td><td>1500</td><td>1200</td><td>900</td><td> $A \succ B \succ C$ </td></tr><tr><td>Reliability</td><td>medium</td><td>low</td><td>high</td><td> $C \succ A \succ B$ </td></tr><tr><td>Effort</td><td>150</td><td>80</td><td>72</td><td></td></tr></table>

Include new project D with function points between 1200 and 1500 and medium reliability in individual rankings and aggregate:

<table><tr><td></td><td>New Ranking</td></tr><tr><td>Function Points</td><td>A $\succ$ D $\succ$ B $\succ$ C</td></tr><tr><td>Reliability</td><td>C $\succ$ (A $\sim$ D) $\succ$ B</td></tr><tr><td>Aggregate Borda Ranking</td><td>A $\succ$ D $\succ$ C $\succ$ B</td></tr></table>

Estimate effort: state the interval, i.e. between A and C i.e. 150 and 72, or use the mean value 111

Fig. 1. Effort estimation with voting rules.

accuracies. These values are normalized by dividing by the sum of all <sup>fi</sup>tnesses, and the resulting values are used as sampling probabilities for putting solutions into the gene pool. The next generation of solutions is constructed by recombining parent solutions from the gene pool in a way similar to genetic crossover, i.e. taking the <sup>fi</sup>rst part up to a random crossover point from the <sup>fi</sup>rst parent and the remaining vector elements from the second parent, and adding a low probability random mutation. In addition, the current optimum solution is retained. Finally this new generation becomes the current one, and we continue with <sup>fi</sup>tness calculation. After a prede<sup>fi</sup>ned number of generations the algorithm stops, and the current best solution is used for estimation. This approach will not generally <sup>fi</sup>nd the optimal weight vector; however, it usually delivers a near-optimal solution fairly quickly.

## 5. Validation

## 5.1. COCOMO data set

The COCOMO Project Data Base contains project attributes and actual effort data for 63 software projects; since its publication in the classic volume by Boehm [3] it has been used as a data base for many software project effort estimation methods because of its ready availability and the possibility of comparison with other approaches. For the same reasons the COCOMO data set is used in this work.

The 15 attributes used in this work are RELY (required software reliability), DATA (data base size), CPLX (process complexity), TIME (time constraint for cpu), STOR (main memory constraint), VIRT (machine volatility), TURN (turnaround time), ACAP (analysts capability), AEXP (application experience), PCAP (programmers capability), VEXP (virtual machine experience), LEXP (language experience), MODP (modern programming practices), TOOL (use of software tools), and SCED (schedule constraint). We explicitly do not include the linesof-code, respectively KDSI (kilo delivered source instructions) of the projects, as this metric is dif<sup>fi</sup>cult to estimate at the beginning of a project.

In validation we use a jackkni<sup>fi</sup>ng approach. We use this method to arrive at estimates for each of the 63 projects in the COCOMO 81 data set, effectively treating each project as if it were not part of the data set and its actual effort were to be estimated from its attributes and the remaining 62 projects.

In order to study the performance of effort estimation we chose to use several measures. First, we report the standard measure mean magnitude of relative error (MMRE), which is most widely used. The problem is that a few widely inaccurate estimates in<sup>fl</sup>uence the overall measure in a way that is not representative of the quality of the whole approach. The median magnitude of relative error (MdMRE) is more robust than MMRE, but is normally not reported in other studies we use for comparison. Also commonly used is the pred(l), which more closely capture the perceived estimation quality. In this type of measure the percentage of estimates that lie within a certain range of the actual values is stated, such as the number of estimates that lie within 25% of the actual values. In our work we use the pred(25)

measure to evaluate the accurateness of the estimation, which is widely used.

In order to apply the social choice aggregation rules to the COCOMO data set the transition from rational values to ordinal values has to be made. This results in 15 rankings for the 63 projects, corresponding to the 15 project attributes. The project attributes in the data set are available in numeric format with values ranging from 0.70 to 1.66; however, in the evaluation of the projects there are only a limited number of different values actually used, e.g., only 5 levels for RELY are attributed to the projects. Therefore, many indifferences are contained in the project rankings that form the base for the aggregation by the social choice rules. Fortunately, the use of margin-based aggregation rules allows for easy treatment of these indifferences, since indifferent voters simply do not contribute to the corresponding margins. The transformation from the COCOMO project attribute values to rankings is therefore straightforward: for attributes positively correlated with effort translate numeric “N” to “≻” in the ranking; for negative correlation with effort reverse the ranking, and numeric identity “=” translates to indifference “\~.”

The voting rules are applied with the individual attribute rankings as input; the corresponding aggregate project rankings regularly contain indifferences, i.e. some ranks are shared by several projects; therefore, to derive an estimate for a project X whose actual effort is not known we distinguish the following cases: (1) Project X shares its rank with other projects; in this case we use the mean of the other projects' efforts as the estimate. (2) Project X is the only occupant of rank r with ranks r−1 and r+1 occupied by other projects; in this case we use the mean of the minimum effort at rank r−1 and the maximum effort at rank r+1 as the estimate (aggregate ranking is by descending effort). (3) Project X is ranked as new top or bottom; in this case we use the current maximum or minimum effort as an estimate. Using this methodology, we have then estimated, as described, every project in the data set using the data from the other projects following a jackkni<sup>fi</sup>ng approach.

## 5.1.1. Accuracy in the binary model

Aggregating the rankings derived from the COCOMO project attributes in a straightforward manner results in rather poor performance; however, by eliminating some project attributes from the rank aggregation using the binary model a pred(25) value of 0.27 can be reached with the Copeland and Borda rule, i.e. about 27% of the projects were estimated within a 25% range of their actual efforts; cf. Table 1. The Maximin rule fares a little worse with pred(25) value of 0.238.

The voting rules deliver estimates e for each project i, and by comparing with the corresponding actual project efforts a<sub>i</sub> the deviations d =|e −a |/a are calculated. By counting the number of d b0.25 we arrive at the pred(25) value as tabulated in Table 1. To indicate the size of the deviations the mean value of the d (MMRE) is tabulated in Table 1, although it is not robust to large outliers. Therefore we also report the median value (MdMRE).

The accuracy of the resulting estimates is similar to the initial Basic COCOMO model estimates of 0.29 but using pred(30) [3], but it should be noted that lines-of-code (KDSI) is not used in our approach, although it constitutes the main cost driver in COCOMO.

Table 1  
Estimation accuracy and weights for the COCOMO data set

<table><tr><td></td><td>Pred(25)</td><td>MMRE</td><td>MdMRE</td><td>Rely</td><td>Data</td><td>Cplx</td><td>Time</td><td>Stor</td><td>Virt</td><td>Turn</td><td>Acap</td><td>Aexp</td><td>Pcap</td><td>Vexp</td><td>Lexp</td><td>Modp</td><td>Tool</td><td>Sced</td></tr><tr><td colspan="19">Binary</td></tr><tr><td>CO</td><td>0.270</td><td>3.046</td><td>0.754</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>MM</td><td>0.238</td><td>13.843</td><td>1.226</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>BO</td><td>0.270</td><td>4.416</td><td>0.663</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td colspan="19">Weighted</td></tr><tr><td>CO</td><td>0.460</td><td>10.418</td><td>0.472</td><td>94</td><td>82</td><td>29</td><td>98</td><td>48</td><td>10</td><td>4</td><td>0</td><td>9</td><td>27</td><td>50</td><td>21</td><td>4</td><td>37</td><td>47</td></tr><tr><td>MM</td><td>0.444</td><td>8.406</td><td>0.472</td><td>83</td><td>64</td><td>49</td><td>60</td><td>98</td><td>68</td><td>52</td><td>82</td><td>71</td><td>34</td><td>97</td><td>27</td><td>3</td><td>0</td><td>13</td></tr><tr><td>BO</td><td>0.381</td><td>8.367</td><td>0.500</td><td>95</td><td>95</td><td>3</td><td>70</td><td>27</td><td>92</td><td>35</td><td>0</td><td>19</td><td>7</td><td>22</td><td>40</td><td>10</td><td>7</td><td>84</td></tr></table>

Table 2  
Estimation accuracy and weights for the Albrecht data set

<table><tr><td></td><td>Pred(25)</td><td>MMRE</td><td>MdMRE</td><td>In</td><td>Out</td><td>File</td><td>INQ</td><td>FP</td></tr><tr><td colspan="9">Binary</td></tr><tr><td>CO</td><td>0.458</td><td>2.022</td><td>0.417</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>MM</td><td>0.417</td><td>1.677</td><td>0.389</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>BO</td><td>0.542</td><td>0.887</td><td>0.250</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="9">Weighted</td></tr><tr><td>CO</td><td>0.625</td><td>1.082</td><td>0.222</td><td>24</td><td>25</td><td>96</td><td>80</td><td>37</td></tr><tr><td>MM</td><td>0.458</td><td>1.472</td><td>0.382</td><td>55</td><td>56</td><td>9</td><td>85</td><td>91</td></tr><tr><td>BO</td><td>0.708</td><td>0.976</td><td>0.175</td><td>25</td><td>39</td><td>91</td><td>52</td><td>9</td></tr></table>

## 5.1.2. Accuracy in the weighted model

With the genetic algorithm approach described above a signi<sup>fi</sup>cant increase in accuracy is possible. Using a population size of 2000 solutions and 1000 generations<sup>2</sup> we arrive at weight vectors such as those shown in Table 1. The maximum value for weights was set at 99, which means that with 15 project attributes there are 100<sup>15</sup> possible solutions. The mutation probability during a crossover was set at 0.01, which means that one in a hundred solutions generated by crossover will contain a mutation i.e. a single random weight.

For each voting rule the best weight vector found is given in Table 1. The weighted model achieves a signi<sup>fi</sup>cant improvement over the binary model with estimation accuracies up to pred(25)=0.46 for the Copeland rule, i.e. nearly half of the estimates are within ±25% of the actual efforts, with a moderate mean deviation of 0.472; cf. Table 1. This clearly outperforms the initial Basic COCOMO model with a pred (30) of 0.29 [3]. However, MMRE is quite high with values up to 10.418 for the Copeland rule. In [29], linear regression using this data set results in a MMRE of 5.2 and a neural network approach reaches 4.28, both of which are considerably below the results presented here. In [15], this data set is used intensively for validation, with grey relational analysis outperfoming other approaches with a pred(25) of 0.38, with approaches considered being case-based-reasoning with 0.12, classi-<sup>fi</sup>cation and regression trees with 0.25, neural networks with 0.11, regression results with 0.17 and genetic programming with 0.15. We therefore are able to clearly outperform all of these approaches considering the pred(25), although lines-of-code are not employed, which nearly all other methods use.<sup>3</sup> This change when using different quality measures will be discussed in the conclusions.

Any comparison of estimation accurateness has to take into account the fact that the estimation approach described in this work does not rely on rational scale values for the project attributes; rankings i.e. ordinal scale are suf<sup>fi</sup>cient. In practical applications this translates into a signi<sup>fi</sup>cant advantage for this approach since experts do not have to provide numeric values for the project attributes; it is suf<sup>fi</sup>cient to provide rankings, which are usually much easier to derive from past experience and expertise.

## 5.2. Albrecht data set

In order to provide further validation for the proposed method we also used another freely available and commonly used data set. The

Table 3  
Estimation accuracy and weights for the ERP data set

<table><tr><td></td><td>Pred(25)</td><td>MMRE</td><td>MdMRE</td><td>BAAN</td><td>SAP</td><td>SSW</td><td>US</td><td>IF</td><td>SITES</td><td>MOD</td></tr><tr><td colspan="11">Binary</td></tr><tr><td>CO</td><td>0.452</td><td>12.972</td><td>0.480</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>MM</td><td>0.161</td><td>8.742</td><td>1.725</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>BO</td><td>0.258</td><td>9.417</td><td>0.725</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td colspan="11">Weighted</td></tr><tr><td>CO</td><td>0.452</td><td>1.394</td><td>0.375</td><td>23</td><td>18</td><td>39</td><td>91</td><td>39</td><td>3</td><td>38</td></tr><tr><td>MM</td><td>0.258</td><td>2.816</td><td>0.944</td><td>25</td><td>1</td><td>41</td><td>58</td><td>9</td><td>69</td><td>48</td></tr><tr><td>BO</td><td>0.452</td><td>17.774</td><td>0.500</td><td>79</td><td>13</td><td>5</td><td>83</td><td>61</td><td>80</td><td>72</td></tr></table>

Albrecht data set used in deriving the function point method [1] contains 24 projects; only 5 project attributes are used for estimation, therefore the solution space is much smaller than in the case of the COCOMO data set, with only 100<sup>5</sup> possible solutions. The pred(25) accuracy is quite high, with typical results around 0.6 and up to 0.7; see Table 2. In [31], analogy-based estimation and regression analysis are used (with regression models using the entire data set, not employing jackkni<sup>fi</sup>ng), resulting in pred(25)of 0.33 in all variants.

## 5.3. ERP data set

Estimating the effort for ERP implementation projects is a suitable area for validating the proposed methodology. The implementation of an ERP system is risky and complex for individual companies, but differs from the development and implementation of individual software solutions in some important points. It actually changes the enterprise and the business processes in many cases, and a majority of the necessary expenditure does not <sup>fl</sup>ow into the production of new program code, but into adjustment work (so-called customizing). Thus traditional metrics for the size of software products as for instance function points [1] or lines-of-code are not easily applicable. In addition, this constitutes a more up-to-date data set and development environment than the other examples.

The ERP data set we use here contains project attributes and efforts for the customisation of enterprise resource planning software (SAP, Oracle, Peoplesoft, BaaN and others). This is based on a questionnaire, which was after a pretest sent to Austrian companies which had already introduced an ERP system. Altogether 300 enterprises of different industries were addressed, using customer lists of several different suppliers including SAP and BaaN which had already been used in a preceding study on ERP system selection processes [2]. This set consists of 31 projects with the 7 attributes BAAN, SAP (zero or one indicating use of respective software), SSW (use of other standard software), US (number of users), IF (number of interfaces), SITES (number of installation sites) and MOD (number of modules implemented) describing the projects. This provides an alternative to the classic software development process, and the results show that the proposed approach is applicable for this type of project as well (see Table 3). The same data set was also used for validating an effort estimation method based on data envelopment analysis [19], with the best results giving an MMRE of 1.548 and 0.314 pred(25). Analogybased estimation on this data set gives a pred(25) of 0.286 with MMRE 0.482, classi<sup>fi</sup>cation trees reach 0.257 pred(25) and MMRE 0.596. Our results from social choice with pred(25)=0.452 and MMRE=1.394 for the Copeland rule (see Table 3) therefore seem encouraging.

Table 4  
Estimation accuracy for all data sets

<table><tr><td>Data set</td><td>Method</td><td>Pred(25)</td><td>MMRE</td><td>MdMRE</td><td>Source</td></tr><tr><td rowspan="10">COCOMO</td><td>Social choice (weighted, CO)</td><td>0.46</td><td>10.42</td><td>0.47</td><td></td></tr><tr><td>COCOMO Basic Model</td><td>&lt;0.29</td><td></td><td></td><td>[3]</td></tr><tr><td>Linear regression</td><td></td><td>5.20</td><td></td><td>[29]</td></tr><tr><td>Neural network</td><td></td><td>4.28</td><td></td><td>[29]</td></tr><tr><td>Grey relational analysis</td><td>0.38</td><td>0.69</td><td></td><td>[15]</td></tr><tr><td>Case-based reasoning</td><td>0.12</td><td>4.46</td><td></td><td>[15]</td></tr><tr><td>Classification and regression trees</td><td>0.25</td><td>2.44</td><td></td><td>[15]</td></tr><tr><td>Neural network</td><td>0.11</td><td>1.43</td><td></td><td>[15]</td></tr><tr><td>Regression analysis</td><td>0.17</td><td></td><td></td><td>[15]</td></tr><tr><td>Genetic programming</td><td>0.15</td><td></td><td></td><td>[15]</td></tr><tr><td rowspan="3">Albrecht</td><td>Social choice (weighted, BO)</td><td>0.71</td><td>0.98</td><td>0.18</td><td></td></tr><tr><td>Regression analysis</td><td>0.33</td><td>0.90</td><td></td><td>[31]</td></tr><tr><td>Analogy-based estimation</td><td>0.33</td><td>0.62</td><td></td><td>[31]</td></tr><tr><td rowspan="4">ERP</td><td>Social choice (weighted, CO)</td><td>0.45</td><td>1.39</td><td>0.38</td><td></td></tr><tr><td>DEA</td><td>0.31</td><td>1.55</td><td>0.48</td><td>[19]</td></tr><tr><td>Analogy-based estimation</td><td>0.29</td><td>0.48</td><td>0.41</td><td></td></tr><tr><td>Classification and regression trees</td><td>0.26</td><td>0.60</td><td>0.51</td><td></td></tr></table>

In [23], the authors use a data set of ERP implementation projects for comparing analogy and regression models, with variables being available including users, sites, interfaces, modi<sup>fi</sup>cations, reports, and similar. They report an MdMRE of 0.43 for practitioners using a multiple regression model, of 0.51 for practitioners using the analogy tool, and for the tools alone of 0.35 for multiple regression respective 0.52 for the analogy tool. Sadly, their data set is not available for a comparison.

## 6. Conclusions and future research

Using several data sets we have demonstrated the accuracy and applicability of the social choice method. It has been shown that using social choice voting rules for rank aggregation a software project effort estimation method can be constructed that achieves an estimation accuracy similar and in general superior to traditional regressionbased or other approaches; the comparison with regression-based approaches is especially favorable when taking into account the fact that only ordinal values are needed in our approach. Table 4 gives an overview of the results. This shows that the proposed approach fares well in general, as given by good pred(25) values, but is problematic in extreme cases, i.e. those outliers being ranked at top or bottom. This can be seen in less than optimal MMRE values. In practice, these projects can easily be detected during application. Further and more systematic evaluation is needed to explore the characteristics of various social choice voting rules in software project effort estimation and their applicability in different types of settings.

While in this ex-post study rational values were used to derive project rankings for each attribute, the practical application of the approach only calls for ranking projects according to attributes, which is usually a much easier task than specifying rationally scaled values. This differentiates this approach from analogy-based estimation [32,31,23]. In only needing comparisons, this approach shows similarities to the work of Miranda [22]; however, while that approach is geared towards estimating a single attribute for several entities based on a single reference point, social choice uses an arbitrary list of variables and aggregates the resulting ranking for arriving at an effort estimation.

Overall, we think that this approach widens the method selection available in effort estimation, and especially offers some advantages. The main concept can be easily understood, and in estimating a new project no numeric values but only a ranking within an existing set of projects is necessary, which is more akin to expert estimation, but alleviating some of the problems associated with it. In future research more work should be invested in validating the accuracy and usability of this approach in other settings, especially other types of development like web applications or similar, or with larger data sets. It would also be interesting to gain feedback from actual users on how much value they place in the advantages of this method, i.e. only necessitating ordinal values via placement within rankings of <sup>fi</sup>nished projects. In addition, the weighting procedure presented here using genetic programming gives promising results, but other methods can also be considered and evaluated for arriving at a solution.

## References

[1] Allan J. Albrecht, John E. Gaffney, Software function, source lines of code, and development effort prediction: a software science validation, IEEE Transactions on Software Engineering 9 (6) (November 1983) 639–648.

[2] Edward Bernroider, Stefan Koch, ERP selection process in midsize and large organizations, Business Process Management Journal 7 (3) (2001) 251–257.

[3] Barry W. Boehm, Software Engineering Economics, Prentice-Hall, Englewood Cliffs, New Jersey, 1981.

[4] Barry W. Boehm, Chris Abts, A. Winsor Brown, Sunita Chulani, Bradford K. Clark, Ellis Horowitz, Ray Madachy, Donald J. Reifer, Bert Steece, Software Cost Estimation with COCOMO II, Prentice Hall PTR, Upper Saddle River, New Jersey, 2000.

[5] B.W. Boehm, C. Abts, S. Chulani, Software development cost estimation approaches a survey, Annals of Software Engineering 10 (2000) 177–205

[6] Lionel C. Briand, Khaled El Emam, Frank Bomarius, Cobra: a hybrid method for software cost estimation, benchmarking, and risk assessment, 20th International Conference on Software Engineering (ICSE '98), 1998, pp. 390–399.

[7] Colin J. Burgess, Martin Le<sup>fl</sup>ey, Can genetic programming improve software effort estimation? a comparative evaluation, Information and Software Technology 43 (2001) 863–873.

[8] G. Costagliola, F. Ferrucci, G. Tortora, G. Vitiello, Class point: an approach for the size estimation of object-oriented systems, IEEE Transactions on Software Engineering 31 (1) (2005) 52–74.

[9] Didier Dubois, Jean-Luc Koning, A decision engine based on rational aggregation of heuristic knowledge, Decision Support Systems 11 (4) (1994) 337–361.

[10] D. Eckert, C. Klamler, J. Mitlöhner, C. Schlötterer, A distance-based comparison of basic voting rules, Central European Journal of Operations Research 14 (4) (2006) 377–386.

[11] P.C. Fishburn, Condorcet social choice functions, SIAM Journal of Applied Mathematics 33 (1977) 469–489.

[12] María N. Moreno Garca, Luis A. Miguel Quintales, Francisco J. Garca Pealvo, M. Jos Polo Martn, Building knowledge discovery-driven models for decision support in project management, Decision Support Systems 38 (2) (2004) 305–317.

[13] David Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning, Kluwer Academic Publishers, Boston, MA, 1989.

[14] F.J. Heemstra, Software cost estimation, Information Software Technology 34 (10) (1992) 627–639.

[15] Sun-Jen Huang, Nan-Hsing Chiu, Li-Wei Chen, Integration of the grey relational analysis with genetic algorithm for software effort estimation, European Journal of Operational Research 188 (2008) 898–909.

[16] M. Jorgensen, M. Shepperd, A systematic review of software development cost estimation studies, IEEE Transactions on Software Engineering 33 (1) (2007) 33–53.

[17] B. Kitchenham, E. Mendes, Software productivity measurement using multiple size measures, IEEE Transactions on Software Engineering 30 (12) (2004) 1023–1035.

[18] C. Klamler, On the closeness aspect of three voting rules: Borda copeland maximin, Group Decision and Negotiation 14 (3) (2005) 233-240

[19] Stefan Koch, ERP implementation effort estimation using data envelopment analysis, in: W. Abramowicz, H.C. Mayr (Eds.), Technologies for Business Information Systems, Springer Verlag, Dordrecht, The Netherlands, 2007, pp. 121–132.

[20] Stephen G. MacDonnel, Andrew R. Gray, Alternatives to regression models for estimating software projects, Proceedings of the IFPUG Fall Conference, IFPUG (International Function Point User Group), Dallas. Texas, 1996, pp. 279.1–279.15.

[21] Jack E. Matson, Bruce E. Barrett, Joseph M. Mellichamp, Software development cost estimation using function points, IEEE Transactions on Software Engineering 20 (4) (April 1994) 275–287.

[22] Eduardo Miranda, Improving subjectice estimates using paired comparisons, IEEE Software 18 (1) (January/February 2001) 87–91.

[23] Ingunn Myrtveit, Erik Stensrud, A controlled experiment to assess the bene<sup>fi</sup>ts of estimating with analogy and regression models, IEEE Transactions on Software Engineering 25 (4) (July/August 1999) 510–525.

[24] L.H. Putnam, A general empirical solution to the macro software sizing and estimating problem, IEEE Transactions on Software Engineering 4 (4) (July 1978) 345–361.

[25] Melanie Ruhe, Ross Jeffery, Isabella Wieczorek, Cost estimation for web applications, 25th International Conference on Software Engineering, 2003, pp. 285–294.

[26] Melanie Ruhe, Ross Jeffery, Isabella Wieczorek, Using web objects for estimating software developing effort for web applications, Ninth International Software Metrics Symposium, 2003, pp. 30–37.

[27] D. Saari, Decisions and Elections Explaining the Unexpected, Cambridge University Press, 2001.

[28] T.L. Saaty, Multicriteria Decision Making: The Analytic Hierarchy Process, RWS Publications, 1990.

[29] Bill Samson, David Ellison, Pat Dugard, Software cost estimation using an albus perceptron (cmac), Information and Software Technology 39 (1997) 55–60.

[30] Richard W. Selby, Adam A. Porter, Learning from examples: generation and evaluation of decision trees for software resource analysis, IEEE Transactions on Software Engineering 14 (12) (December 1988) 1743–1756.

[31] Martin Shepperd, Chris Scho<sup>fi</sup>eld, Estimating software project effort using analogies, IEEE Transactions on Software Engineering 23 (12) (November 1997) 736-743.

[32] Martin Shepperd, Chris Scho<sup>fi</sup>eld, Barbara Kitchenham, Effort estimation using analogy, Proceedings of the 18th International Conference on Software Engineering (ICSE 1996), IEEE, Berlin, 1996, pp. 170–178.

[33] Bojan Srdjevic, Linking analytic hierarchy process and social choice next term methods to support group decision-making in water management, Decision Support Systems 42 (4) (2007) 2261–2273.

[34] Rajan Srikanth, Matthias Jarke, The design of knowledge-based systems for managing ill-structured software projects, Decision Support Systems 5 (4) (1989) 425–447.

[35] Krishnamoorthy Srinivasan, Douglas Fisher, Machine learning approaches to estimating software development effort, IEEE Transactions on Software Engineering 21 (2) (February 1995) 126–137.

![](/api/attachments/MJY6WNH3/fulltext/images/f440a938b904b14d3e1f7ef0cce3f4ebab330f4191dd8ef17dc3edce2f02fac4.jpg)

Stefan Koch is Associate Professor of Information Business at the Bogazici University, Istanbul. His research interests include user innovation, cost estimation for software projects, the open source development model, the evaluation of bene<sup>fi</sup>ts from information systems and ERP systems He has published over 10 papers in peer-reviewed journals, including Information Systems Journal, Information Economics and Policy, Electronic Markets, Journal of Database Management, Journal of Software Maintenance and Evolution and Wirtschaftsinformatik, and over 30 in international conference proceedings and book collections. He has also edited a book titled ‘Free/Open Source Software Development’ for an international publisher in 2004, and serves as

Editor-in-Chief of the International Journal on Open Source Software & Processes.

![](/api/attachments/MJY6WNH3/fulltext/images/93d1bdaa51f8a44a25d2cc1aaed66d445e399f7dfa405adab331bbe6df29a5e2.jpg)

Johann Mitlöhner is Assistant Professor at the Institute for Information Business of the Vienna University of Economics and Business Administration. His research interests include social choice methods, software development methods, and semantic web technologies. He has published 6 papers in peer-reviewed journals and over 20 in international conference proceedings and book collections.
