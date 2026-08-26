---
otero_id: 20861
otero_key: "QY3VAJYN"
title: "The cost-minimizing inverse classification problem: a genetic algorithm approach"
authors: "Michael V. Mannino; Murlidhar V. Koushik"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00077-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The cost-minimizing inverse classification problem: a genetic algorithm approach

Michael V. Mannino <sup>a,)</sup>, Murlidhar V. Koushik <sup>b</sup>

<sup>a</sup> Graduate School of Business Administration, Campus Box 165, P.O. Box 173364, UniÕersity of Colorado at DenÕer, DenÕer, CO 80217-3364, USA

Microsoft Corporation, 11<sup>r</sup>2134, One Microsoft Way, Redmond, WA 98052-6399, USA

Accepted 27 April 2000

## Abstract

We consider the inverse problem in classification systems described as follows. Given a set of prototype cases representing a set of categories, a similarity function, and a new case classified in some category, we find the cost-minimizing changes to the attribute values such that the case is reclassified as a member of a different preferredŽ . category. The problem is AinverseB because the usual mapping is from a case to its unknown category. The increased application of classification systems in business suggests that this inverse problem can be of significant benefit to decision makers as a form of sensitivity analysis

Analytic approaches to this inverse problem are difficult to formulate as the constraints are either not available or difficult to determine. To investigate this inverse problem, we develop several genetic algorithms and study their performance as problem difficulty increases. We develop a real genetic algorithm with feasibility control, a traditional binary genetic algorithm, and a steepest ascent hill climbing algorithm. In a series of simulation experiments, we compare the performance of these algorithms to the optimal solution as the problem difficulty increases more attributes and classes . InŽ . addition, we analyze certain algorithm effects level of feasibility control, operator design, and fitness function to determineŽ . the best approach. Our results indicate the viability of the real genetic algorithm and the importance of feasibility control as the problem difficulty increases. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Inverse classification; Genetic algorithms; Classification systems; Sensitivity analysis

## 1. Introduction

Classification systems have become important tools used in the support of organizational decision making. When presented with a new case, a classification system returns the category that best describes the case. Examples of classification in business decision making include fault diagnosis in semiconductor manufacturing 28 , bank failure prediction 43 , and<sup>w x</sup> <sup>w x</sup> industry and occupation code prediction 16 . The <sup>w</sup> <sup>x</sup> primary goal of a classification system is to perform at the same level of human experts. Classification systems can provide many benefits to an organization such as reducing decision making time, improving the consistency of decisions, and reducing dependence on scarce human experts.

Notably absent in most classification systems is the ability to systematically conduct sensitivity analysis. Sensitivity analysis, which has been widely studied in many areas of mathematical programming, provides insight to decision makers by focusing on the impact of changes to one or more input variables on the values of the decision variables and objective function. In this paper, we study a sensitivity problem that we refer to as the cost-minimizing inÕerse classification problem. This problem deals with the question: What is the minimum required change to a case in order to reclassify it as a member of a Ž . different preferred class? This is an inverse problem because the normal mapping in a classification system is from a case to its predicted class.

An efficient solution to this inverse classification problem can be of significant value to decision makers in situations where attribute values can be manipulated. For example, municipal bond ratings by the two major rating agencies, Moody’s Investor Service, and Standard and Poor’s, are well-known determinants of the credit worthiness and hence, theŽ borrowing costs and financial integrity of a commu-. nity’s debt obligations. A number of factors belonging to four categories — economic base, financial analysis, administrative structure and debt — are used by these agencies in arriving at the bond rating. Several factors, such as population size and geographic location, can be difficult to manipulate. However, other factors such as housing variables Že.g., the percentage of owner-occupied dwellings and percentage of single-family housing units, which are both significant in their influence on the rating <sup>w</sup> <sup>x</sup> 15 are far more directly controllable. The cost-. minimizing solution to the problem of moving to an improved rating might clearly be of interest to the municipality’s administrators.

As a first attempt to study the cost-minimizing inverse classification problem, we study a heuristic approach using genetic algorithms for similaritybased classification systems. The most distinctive feature of similarity-based classification systems is that concept boundaries are not explicitly represented. The classifier, when presented with a new case, returns the predicted class as well as a goodness of fit measure such as the distance from other similar cases. Because concept boundaries are not explicitly represented, it is difficult to develop an analytic model of the cost-minimizing inverse problem. A genetic approach is interesting here because it can be efficient, can incorporate problem-specific knowledge, yet operate without explicit knowledge of concept boundaries.

Similarity-based classification systems are widely studied and used 17,42 . The simplest approach, <sup>w</sup> <sup>x</sup> known as the k nearest neighbors approach, does not require analysis of training data. However, because it may require retrieval of a large number of cases, other approaches have been devised that reduce the retrieval effort but require analysis of training data <sup>w</sup> <sup>x</sup> 10,25,45 . We focus on similarity-based techniques that reduce the search effort by saving only the prototype or most representative instances of each class 1 . Similarity-based classification has been<sup>w</sup> <sup>x</sup> applied to industrial problems 2 including industry <sup>w</sup> <sup>x</sup> and occupation classification 16 , clinical audiology<sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> 39 , customer technical support 41 , and message classification 22 . In the bond rating example dis- <sup>w</sup> <sup>x</sup> cussed previously, similarity-based classification would be a good approach because the municipality does not know the explicit concept boundaries as they are a closely guarded secret of the credit rating agency.

To study this problem, we develop several genetic algorithms and study their performance. To facilitate the comparison of the genetic algorithms with the optimal solution, we restrict our study to classification systems with real attributes. We present a real genetic algorithm with feasibility control, a traditional binary genetic algorithm, and a steepest ascent hill climbing algorithm. The real genetic algorithm uses feasibility preserving operators, a feasibility control parameter, and fitness functions for evaluation of infeasible solutions. In a series of simulation experiments, we compare the performance of these algorithms to the optimal solution as the problem difficulty increases more attributes and classes . InŽ . addition, we analyze certain algorithm effects levelŽ of feasibility control, operator design, and fitness function design to determine the best approach. Our . results provide insight into the capabilities of a genetic algorithm, when precise constraint boundaries are not known, the importance of feasibility control, and the effect of other design issues.

The rest of this paper is organized as follows. Section 2 reviews research on nearest point problems and sensitivity analysis for classification systems. Section 3 defines the cost-minimizing inverse classification problem and lists some simplifying assumptions. Section 4 describes the genetic algorithms used in our study. Section 5 reports on experiments comparing the genetic algorithms. Section 6 summarizes the paper and discusses future research directions.

## 2. Related work

The work most closely related to the model presented in Section 3 is the nearest point problem. In the nearest point problem, the goal is to find the nearest point by Euclidean distance in a convex polyhedral space. There are many applications of nearest point problems in robotics, geophysical data analysis, and optimization algorithms 3 . The near- <sup>w</sup> <sup>x</sup> est point problem can be solved by algorithms that utilize its underlying linear complementarity structure 37 , interior point methods 4 , and exterior <sup>w</sup> <sup>x</sup> <sup>w x</sup> point methods 6 . However, none of the work on<sup>w</sup> <sup>x</sup> nearest point problems addresses imprecisely known constraints.

Clustering is another related area. The objective in clustering problems is to assign objects to groups so that the members of each group are as similar as possible. Clustering can be hard in which each object is assigned to only one cluster or fuzzy in which objects are assigned with a degree of association. Clustering is similar to the inverse classification problem as the constraint boundaries are not known and heuristic solutions such as Tabu search 5,19<sup>w</sup> <sup>x</sup> and simulated annealing 7,31,40 have been used.<sup>w</sup> <sup>x</sup> Clustering is dissimilar in that a nearest point is not sought.

Several related studies deal with sensitivity analysis of classification. The sensitivity of efficiency classifications in the additive model of data envelopment analysis is studied in Ref. 14 . The authors<sup>w</sup> <sup>x</sup> formulate a model in which an organization’s classification as efficient or inefficient remains unchanged in a region of stability. Their model requires two classifications efficient or inefficient and the ex-Ž . plicit representation of resource production and usage in the data envelopment analysis model.

Sensitivity analysis in neural net models is studied in Ref. 32 . The authors develop a technique to <sup>w</sup> <sup>x</sup> show the relative importance of input variables and elements in the hidden layer of a neural network for product entry decisions. Although their technique does not require explicit modeling of concept boundaries, they do not compute a cost-minimizing point as described in this paper. Construction of prototype instances in a neural network framework is presented in Ref. 26 . This work describes a backward mode<sup>w</sup> <sup>x</sup> of classification in which a neural network for classification and a training set are known, but good representatives or prototypes of a class are un- Ž . known. However, the authors do not address the problem of finding cost-minimizing points.

There has been active research on using genetic algorithms for constrained optimization problems <sup>w</sup> <sup>x</sup> 33,35 . These efforts use techniques such as penalty functions, specialized operators, co-evolution, and repair algorithms. In addition, hybrid methods combining evolution with traditional optimization techniques have been used 29 . Some of these tech- <sup>w</sup> <sup>x</sup> niques penalty functions and specialized operators Ž . are adapted in this work. None of these approaches has been reported for the problem described here. All of the techniques require explicit enumeration of the constraints.

A final study to note involves the use of genetic algorithms for sensitivity analysis 30 . The authors<sup>w</sup> <sup>x</sup> describe a method whereby the output of a genetic algorithm is consulted to provide sensitivity information. The authors’ method may also apply to the genetic algorithms described here to provide additional information.

## 3. Problem definition and solution approaches

In this section, we define the particular inverse classification problem studied in this paper. We make several simplifying assumptions about the inverse classification problem so that we can compare the performance of approximate solution approaches to the optimal solution.

## 3.1. General problem definition

The cost-minimizing inverse classification problem determines the minimum cost alternative by which a reference instance $r = \{ r _ { 1 } , \ r _ { 2 } , \ldots , \ r _ { n } \}$ , currently categorized in class $C _ { i }$ , can have its attribute values modified so that it is recategorized in a Ž . different preferred class $C _ { \lambda , \ i } \ne \lambda \in \{ 1 , 2 , \ \cdot \cdot \cdot , m \}$ The process of classifying an instance k is a mapping from the set of attribute values $\{ k _ { 1 } , ~ k _ { 2 } , ~ \cdots $ $\boldsymbol { k } _ { n } \}$ and prototype instances R to exactly one of m classes: classify $( k , R )  C _ { i } , i \in \{ 1 , 2 , \ \cdot \ \cdot \ , m \}$ . Let $q = \{ q _ { 1 } , q _ { 2 } , \dotsb , q _ { n } \}$ denote a modified instance of r after one or more attribute values have been manipulated and change\_cost $( r , \ q )$ denote the total cost of the modifications. The inverse classification problem CP1 can be formulated as:

$$
\begin{array}{c} \text {Problem CP1:} \min (  c h a n g e \_ c o s t (  r, q)) \\ q \\ \text {s.t.} \quad \text {classify} (  q, R) \to C _ {\lambda}. \end{array}\tag{1}
$$

## 3.2. Assumptions

We make the following assumptions that enable the cost-minimizing inverse classification problem to be formulated as an optimization problem.

Attribute domains are real-valued, i.e., Ždom $A _ { 1 } ) \times \ldots \times \operatorname { d o m } ( A _ { n } ) = E ^ { n }$ , where $E ^ { n }$ represents n-dimensional Euclidean space. Further, we assume that attribute values are mapped to the range Ž . LB, UB where LB and UB represent the lower and upper bounds, respectively.

<sup>Ø</sup> Each attribute can be independently changed. Independence allows an attribute to be modified without inducing changes in other attributes. The case where only some attributes can be modified is clearly of practical interest. Our approach allows this to be modeled by associating such attributes with significantly higher change costs.

<sup>Ø</sup> Attribute change costs are non-uniform, linear functions. Non-uniformity implies that change costs can differ among attributes. Linearity implies that change costs are stationary over the domain.

<sup>Ø</sup> Concepts defining class boundaries represent linear constraints. Linear class boundaries imply that the region describing any individual class is a convex space.

With these assumptions, the inverse classification problem can be formulated as Problem CP2. Let $h _ { j }$ denote the change cost associated with attribute $A _ { j } .$ Since $h _ { j }$ is stationary, the objective function is the weighted Euclidean distance between the original and modified instances. In the formulation, we have chosen to minimize the square of the weighted Euclidean distance:

$$
\text { Problem   CP2: } \min _ {q} \sum_ {j = 1} ^ {n} h _ {j} ^ {2} (r _ {j} - q _ {j}) ^ {2}.\tag{2}
$$

Appendix A describes a mathematical programming formulation of Problem CP2. The formulation requires the construction of a Voronoi diagram, a fundamental data structure in computational geometry 9 . A Voronoi diagram is a partition that reflects <sup>w</sup> <sup>x</sup> proximity relationships among a collection of points or sites. Each point is associated with the region closest to it. Voronoi diagrams have been applied in a wide variety of areas such as cluster analysis, disk optimization, collision detection in robotics, and crystallography. Appendix B describes the technique used to construct a Voronoi diagram. The mathematical programming formulation in Appendix A uses the constraints generated from the Voronoi diagram.

The mathematical programming formulation in Appendix A is impractical for many classification systems because of the complexity to construct the underlying Voronoi diagram. First, to support queries on all classes, the entire Voronoi diagram must be constructed. Vertex enumeration algorithms used to construct the Voronoi diagram are exponentially complex in the worst case. Second, the number of sites can increase because more than one site exists in many classification systems. Techniques to identify prototypes from a training set of cases such as the IB3 algorithm 1 usually permit multiple proto- <sup>w</sup> <sup>x</sup> types per class to support disjunctive concept spaces. Third, there are environments in which the prototypes change as new cases are acquired. Recomputing the Voronoi diagram in changing environments may not be cost-effective.

In Section 4, we describe approximate techniques that can be used in situations where the math programming solution is not appropriate. We use the math programming formulation to gauge the quality of solutions generated by the heuristic methods.

## 4. Genetic algorithm design

In this section we, present the genetic algorithms used to find solutions to the inverse classification Problem CP2. We first present the features of the real genetic algorithm including the mutation and crossover operators, the feasibility control parameter, and the fitness functions for non-feasible solutions. In Sections 4.2 and 4.3, we briefly present the two comparison algorithms, the traditional binary genetic algorithm and the steepest ascent hill climbing algorithm.

## 4.1. Real genetic algorithm

Genetic algorithms are probabilistic search algorithms based on the principles of natural selection, evolution, and heredity. Historically, genetic algorithms have used the binary alphabet for internal representation of chromosomes. This practice was largely inspired by early work in genetic algorithms that exploited the simplicity of this approach. In addition, a number of theoretical results, such as the well-known Schema Theorem and the Implicit Parallelism Property 24 , were derived on the basis of<sup>w</sup> <sup>x</sup> this representation. However, recent work suggests that the implicit parallelism result does not depend on the use of a binary alphabet and that it may be worthwhile to experiment with larger alphabets, floating point representations, and new operators <sup>w</sup> <sup>x</sup> 8,44 . In addition, experiments using genetic algorithms on floating point representations using modified genetic operators show that overall performance, as measured by efficiency and standard deviation, improves substantially especially in the presence of non-trivial constraints 34 . In this study, we adopt a <sup>w</sup> <sup>x</sup> floating point representation for feature values since this is the most natural way of modeling the data. Each chromosome is therefore represented as a vector with a fixed number of floating point values, one value per attribute.

An important advantage of real encoding for constrained optimization problems is the ability to control the feasibility of chromosomes. A chromosome is infeasible when it is not classified in the preferred class. We exploit this advantage by designing feasibility preserving mutation and crossover operators. The operators are adapted from Ref. 34 where they are used with known linear constraints. In contrast, the problem studied here has unknown linear constraints.

In the remainder of this section, the details of the real genetic algorithm are described. The mutation and crossover operators presented in Sections 4.1.1 and 4.1.2 followed by the feasibility control parameter and fitness function in Sections 4.1.3 and 4.1.4.

## 4.1.1. Mutation operator

Because class boundaries are not precisely known, mutation cannot take advantage of explicit constraint information to transform a chromosome to a feasible state. Instead, the feasible mutation operator uses a binary search to find a feasible state change. If no feasible transformation is found, no mutation occurs. Pseudo code for the mutation operator known as FeasibleMutationSearch appears below. In the pseudo code, CalcNonUniformMutation is the nonuniform mutation operator described in Ref. 34 . A<sup>w</sup> <sup>x</sup> non-uniform mutation operator is designed so that the extent of change induced by the operator varies with the age of the population. The extent of change becomes very small when the population’s age approaches the designated maximal number of generations.

procedure FeasibleMutationSearch Input: Chromosome, MutPoint, SearchDepth, Age Output: new value for the mutated gene Ž Mut-Point. of Chromosome TempChromosome Chromosome Adjust <sup>¤</sup> CalcNonUniformMutation ChroŽ - mosome, MutPoint, Age. TempChromosome MutPoint<sup>w</sup> <sup>x¤</sup>Adjust if ImproÕes TempChromosome Ž . , Chromosome Chromosome MutPoint<sup>w</sup> <sup>x</sup> Adjust exit procedure Upper<sup>¤<</sup>Chromosome MutPoint<sup>w</sup> <sup>xy</sup>Adjust<sup><</sup> Lower 0 BestMutation <sup>¤</sup> BinSearch LowerŽ , Upper, SearchDepth, MutPoint, Chromosome. Chromosome MutPoint<sup>w x¤</sup>BestMutation end procedure

FeasibleMutationSearch uses two alternative criteria to control the search. The diÕersity criterion selects the largest feasible adjustment to the chromosome. Using the diversity criterion, the ImproÕes function returns true if the original adjustment results in a feasible solution. If ImproÕes returns false, the binary search is executed. Inside the binary search, the best mutation value is updated whenever a mutation results in a feasible solution and the mutation amount is larger than the previous best mutation. In contrast, the fitness criterion selects the mutation value with the largest fitness. Using the fitness criterion, the ImproÕes function returns true if the original adjustment is feasible and the resulting chromosome has a larger fitness value than the original chromosome. Inside the binary search, the best mutation value is updated whenever a mutation results in a feasible chromosome and the chromosome’s fitness is larger than the fitness associated with the previous best mutation.

## 4.1.2. CrossoÕer operator

We adapt the partial vector crossover operator from Ref. 34 as a feasibility preserving crossover<sup>w</sup> <sup>x</sup> operator. Let $\pmb q ^ { t } = \{ q _ { 1 } , \ q _ { 2 } , \ \cdot \ \cdot \ , \ q _ { n } \}$ and ${ \pmb s } ^ { t } = \{ s _ { 1 }$ $s _ { 2 } , ~ \cdots , ~ s _ { n } \}$ represent two feasible solution vectors at time t and assume that the crossover point falls between attributes indexed by j and j<sup>q</sup>1. Since the search space F is convex cf. Section 3 , there existsŽ . $a \in [ 0 , 1 ]$ such that:

$$
\begin{array}{c} \boldsymbol {q} ^ {t + 1} = \left\{q _ {1}, \dots , q _ {j}, a s _ {j + 1} + (1 - a) q _ {j + 1}, \dots , a s _ {n} \right. \\ \quad \left. + (1 - a) q _ {n} \right\} \in F, \\ \boldsymbol {s} ^ {t + 1} = \left\{s _ {1}, \dots , s _ {j}, a q _ {j + 1} + (1 - a) s _ {j + 1}, \dots , a q _ {n} \right. \\ \quad \left. + (1 - a) s _ {n} \right\} \in F. \end{array}
$$

Similar to the feasible mutation operator, we use a binary search with two criteria to find the best a value. The diÕersity criterion finds the largest a value that is consistent with the feasibility constraint. The fitness criterion finds the fitness-maximizing a value that is consistent with the feasibility constraint. If no consistent value of a is found, then it is set to 0, implying no swapping of genetic material. Note that a <sup>s</sup> 1 results in a simple swapping of values between the two chromosomes.

## 4.1.3. Feasibility control parameter

To control the application of the feasibility preserving operators, we use a feasibility control parameter. The feasibility control parameter is defined as the minimal fraction of feasible solutions required in each generation. A value of 0 indicates that all members of a generation can be infeasible no feasi-Ž bility requirement , while a value of 1 indicates that. all members must be feasible. The feasibility control parameter restricts the application of the feasibility preserving mutation and crossover operators previously defined. When the feasibility level is exceeded in a generation, subsequent chromosomes in the generation are created using non-closed versions of the operators. The non-closed operators involve a single application of the underlying formula non- Ž uniform mutation or partial vector crossover without. the binary search to ensure feasibility.

## 4.1.4. Fitness function

The fitness function for feasible chromosomes is derived directly from the objective function Problem CP2. The only change is due to the maximizing nature of genetic algorithms. Since the objective function is a minimization problem, a simple transformation makes it into a maximization problem. The fitness of a feasible solution q is given by:

$$
\text { fitness } (q) = C _ {\max} - \left[ \sum_ {j = 1} ^ {n} h _ {j} ^ {2} \left(r _ {j} - q _ {j}\right) ^ {2} \right] ^ {1 / 2},\tag{3}
$$

where $C _ { \mathrm { m a x } }$ is a value larger than the worst objective function value.

When infeasible solutions can be generated, the fitness function is typically augmented with a penalty function. Both the binary genetic algorithm and the real genetic algorithm with a feasibility control lessŽ than 1 can generate infeasible solutions. The aug-. mented fitness function should have several properties: 1 the amount of penalty depends on the extentŽ . of infeasibility; 2 infeasible solutions should re- Ž . ceive lower fitness values than feasible solutions; and 3 transition between the fitness values of feasi-Ž . ble and infeasible solutions should be smooth. The second and third properties may conflict. If all feasible solutions have a larger fitness value than infeasible solutions, the fitness function may have a large discontinuity that causes poor feasible solutions to dominate. To make the transition smoother, it may be beneficial to allow some infeasible solutions Ž . especially those close to the optimal solution to have better fitness values than poor feasible solutions.

We designed two fitness functions for infeasible solutions to test the sensitivity of the genetic algorithm to the second and third properties. In both infeasible fitness functions, the fitness is the sum of a penalty amount measuring the amount of infeasibility and an objectiÕe amount measuring the quality of some feasible solution. The penalty amount is the distance between the infeasible point and the closest feasible point. The objective amount differs in the two fitness functions. In the AFitness function, the fitness of each infeasible solution is guaranteed to be worse than all feasible solutions. In the SFitness function, the fitness of each infeasible solution is guaranteed to be worse than some feasible solution Ž . in practice, it is worse than most feasible solutions . The AFitness function ensures that the second property is satisfied, while the SFitness function ensures that the third property is satisfied.

Fig. 1, containing a two-dimensional Voronoi diagram with five sites, illustrates the two fitness functions for infeasible solutions. In Fig. 1, Site3 is the preferred site, r is the reference point, and i is an infeasible point generated by the genetic algorithm.

![](/api/attachments/QY3VAJYN/fulltext/images/315450f52a301d019dc10df1b0cc7104ab40f224310ffadc2940c94c95d66ca2.jpg)  
Fig. 1. Voronoi diagram depicting the infeasible fitness functions.

The labeled points interior to Site3 $( q I$ through $q 6 )$ are feasible solutions previously generated by the genetic algorithm. Assume that $q 3$ is the closest to i among the interior points $( q l$ through $q 6 )$ , while $q 6$ is the worst point among the interior points. Then, the distance from $i$ to $q 3 ,$ , denoted by the dark line connecting them, is the penalty amount. The objective amount in AFitness is the distance from r to $q 6$ Ž .the worst known feasible point . The objective amount in SFitness is the distance from r to $q 3 .$

The precise definition of the two fitness functions for infeasible chromosomes is given below. Let i be an n-dimensional infeasible point, $q ^ { \prime }$ be the point in $F$ closest to $i ,$ and $q ^ { \prime \prime }$ be the point in F farthest from $r .$ Then the AFitness and SFitness functions are defined as:

$$
\begin{array}{l} A F i t n e s s (i) = C _ {\max} - \left\{\left[ \sum_ {j = 1} ^ {n} h _ {j} ^ {2} \left(q _ {j} ^ {\prime} - i _ {j}\right) ^ {2} \right] ^ {1 / 2} + \left[ \sum_ {j = 1} ^ {n} h _ {j} ^ {2} \left(q _ {j} ^ {\prime \prime} - r _ {j}\right) ^ {2} \right] ^ {1 / 2} \right\} \end{array}\tag{4}
$$

$$
\begin{array}{l} S F i t n e s s (i) = C _ {\max} - \left\{\left[ \sum_ {j = 1} ^ {n} h _ {j} ^ {2} \big (q _ {j} ^ {\prime} - i _ {j} \big) ^ {2} \right] ^ {1 / 2} \right. \\ \left. + \left[ \sum_ {j = 1} ^ {n} h _ {j} ^ {2} \big (q _ {j} ^ {\prime} - r _ {j} \big) ^ {2} \right] ^ {1 / 2} \right\}. \end{array}\tag{5}
$$

## 4.2. Binary genetic algorithm

Even though the published literature contains a large number of algorithms, the traditional binary algorithm 21 is still widely used and a good bench-<sup>w</sup> <sup>x</sup> mark for a more specialized algorithm. Thus, the experiments in Section 5 use the traditional binary genetic algorithm as one of the algorithms. The traditional binary genetic algorithm uses the singlepoint crossover and mutation operators. The fitness function is described Section 4.1.4. The only modification to the traditional binary algorithm is the use of the modGA <sup>w</sup> <sup>x</sup> 34 reproduction algorithm instead of roulette wheel selection. The modGA algorithm uses an elitist strategy in which some members of the previous generation are copied to the next generation.

## 4.3. Steepest ascent hill climber

The steepest ascent hill climber is a greedy heuristic algorithm as it always moves in the direction of largest gain. On certain optimization problems 34 ,<sup>w</sup> <sup>x</sup> hill climbing algorithms will eventually find the optimal solution. In our problem, a hill climber seems like a good heuristic because the constraints are linear and only one optimal value exists.

We designed a steepest ascent hill climber so that its search effort is similar to the genetic algorithms. In the outer loop, the steepest ascent hill climber conducts NumGens local searches where NumGens is the number of generations used by the genetic algorithms. In each outer iteration, the hill climber uses the best solution from the previous iteration. In the first iteration, the best solution in the original feasible population is used. In the inner loop, the hill climber performs PopSize mutations of a starting solution where PopSize is the population size used by the genetic algorithms. Mutation is performed using the diversity control version of the Feasible-MutationSearch procedure Section 4.1.1 where theŽ . age and mutation point are randomly generated each time. In effect, the hill climber works like a superelite, real genetic algorithm using only mutation. The pseudo-code for the hill climber is given below.

procedure HillClimb Input: Chromosome, NumGens, PopSize, Depth Output: BestChromosome the best chromoŽ - some generated. BestChromosome<sup>¤</sup>Chromosome for i<sup>s</sup>1 to NumGens InitChromosome BestChromosome for j <sup>s</sup> 1 to PopSize NewChromosome<sup>¤</sup>InitChromosome Randomly generate Age and MutPoint FeasibleM utationSearch Ž NewChromosome, MutPoint, Depth, Age. if fitness NewChromosome Ž . <sup>)</sup> fitness Ž . BestChromosome BestChromosome<sup>¤</sup>NewChromosome next j next i return BestChromosome end procedure

## 5. Experimental comparison

In this section, we describe simulation experiments to evaluate the performance of the genetic algorithms. We describe the research questions, experimental design, experimental procedures, and results.

## 5.1. Research questions

The objective of the experiments is to investigate genetic algorithm performance as related to algorithm issues and problem difficulty. For the algorithm issues, we are primarily interested in the effect of feasibility control and algorithm binary, real, and Ž hill climbing because these factors generalize to . other genetic algorithms. We are secondarily interested in issues specific to our algorithms including feasibility search criteria diversity vs. fitness in the Ž . mutation and crossover operators, and evaluation of infeasible solutions. For problem difficulty, we are interested in the effect of search effort and number of attributes.

We have several beliefs about the relationship between algorithm issues, problem difficulty, and performance. First, we believe that increasing feasibility control will improve performance and that increasing the number of classes will make feasibility control more important. Hypotheses 1 and 1.1 state these beliefs. Second, because of the importance of feasibility control, we believe that the real-1 algorithm real genetic algorithm with feasibilityŽ control parameter equal to 1 will dominate the other. algorithms as stated in Hypothesis 2. Because the other algorithm issues are rather specific to our problem, we do not state formal hypotheses for them. Third, we believe that performance will worsen as the number of attributes increases, as stated in Hypothesis 3. Additional search effort will improve performance but will not entirely compensate for increases in the number of attributes. The search effort is determined by the number of individuals sampled number of generations times the population Ž size ..

Hypothesis 1. As the feasibility control increases, the performance of the real genetic algorithm improÕes.

Hypothesis 1.1. As the number of classes changes from low to medium and medium to high, feasibility control becomes more important.

Hypothesis 2. The real-1 algorithm will dominate the binary, real-0, and hill climber algorithms.

Hypothesis 3. Performance becomes worse as the number of attributes increases. Increasing the number of indiÕiduals sampled will not entirely compensate for increases in the number of attributes.

We use two performance measures: i the per-Ž . centage cost difference PD between the geneticŽ . algorithm and optimal solution and ii the percent-Ž . age improvement PI of the genetic algorithm as Ž . compared to the best initial solution. BestGA is defined as the best in all generations in which the genetic algorithm executed. PI is an internal measure of performance as it uses the initial population to account for problem difficulty. Problem difficulty can arise from a number of sources such as how far the reference point is from the optimal solution, the quality of solutions in the initial population, and the shape of the preferred region:

$$
\mathrm{PD} = 1 0 0 \times \frac {\text { BestGA } - \text { Optimal }}{\text { Optimal }},\tag{6}
$$

$$
\mathrm{PI} = 1 0 0 \times \frac {\text { BestInitial } - \text { BestGA }}{\text { BestInitial } - \text { Optimal }}.\tag{7}
$$

## 5.2. Experimental design

We use several experiments to test the hypotheses discussed in Section 5.1. For Hypothesis 1, we use a linear regression model as shown in the response function Eq. 8 below:Ž Ž ..

$$
\begin{array}{r l} E (Y) & = \beta_ {0} + \beta_ {1} \mathrm{FC} + \beta_ {2} \mathrm{NC} _ {\mathrm{L}} + \beta_ {3} \mathrm{NC} _ {\mathrm{M}} \\ & + \beta_ {4} \mathrm{FCNC} _ {\mathrm{L}} + \beta_ {5} \mathrm{FCNC} _ {\mathrm{M}}. \end{array}\tag{8}
$$

Here, Y is the performance measure PD or PI , FCŽ . is the feasibility control parameter, and $\mathrm { N C } _ { \mathrm { L } }$ and $\mathrm { N C } _ { \mathrm { M } }$ are indicator variables defined as follows:

$$
\mathrm{NC} _ {\mathrm{L}} = \left\{ \begin{array}{l} 1 \text {   if   the   number   of   classes   is   low } \\ 0 \text {   otherwise } \end{array} \right.\tag{9}
$$

$$
\mathrm{NC} _ {\mathrm{M}} = \left\{ \begin{array}{l} 1 \text {   if   the   number   of   classes   is   moderate } \\ 0 \text {   otherwise } \end{array} \right.\tag{10}
$$

In this model, we vary the feasibility control from 0.0 to 1.0 in steps of 0.10. For the number of classes, <sup>1</sup> we use low, moderate 15 , and high 30 levels.Ž . Ž . Each observation is the average performance over 30 problems where a problem is a random combination of a preferred site and a reference point. Because we are not interested in the impact of the number of attributes, we use separate regressions for a variety of number of attributes. Each regression uses a sample of 160 randomly generated observations.

For Hypothesis 2, we use a single-factor, fixed effects model with equal treatment sample sizes 38 .<sup>w</sup> <sup>x</sup> This experiment has four treatments corresponding to the binary genetic algorithm, the real genetic algorithm with feasibility control of 0, the real genetic algorithm with feasibility control of 1, and the hill climbing algorithm. Each observation is the average over 30 randomly selected problems combina- Ž tion of number of classes, attributes, preferred site, and reference point . The number of classes is uni-. formly drawn from low, moderate, or high where the low, moderate, and high levels are defined as in experiment 1. For each treatment, the same set of 30 observations was used.

For Hypothesis 3, we generate data to plot graphs depicting the relationship between the number of generations, number of attributes, and performance. We generate data by varying the maximum number of generations and averaging the best performance across a set of 30 randomly selected problems com-Ž binations of preferred class and reference point ..

## 5.3. Experimental procedure

To conduct the experiments discussed in Section 5.2, we determined parameter values and devised a method to generate experimental observations. We determined parameter values through an examination of previous work and pilot studies. For the replacement ratio 0.9 , aging parameter 2 , and binaryŽ . Ž . search depth 3 of the real genetic algorithm, weŽ .

![](/api/attachments/QY3VAJYN/fulltext/images/c4ebc0630fb0576606340461503075580d6a51d3a33dfcd601027ef8ced856f1.jpg)  
Fig. 2. Infeasible fitness function results.

relied on values suggested in Ref. 34 . For the real<sup>w</sup> <sup>x</sup> crossover and mutation rates, we conducted a small simulation experiment at a number of levels. The simulations suggested that a crossover rate of 0.3 and mutation rate of 0.2 give excellent results. These rates are comparable to previous studies 34,36 . For <sup>w</sup> <sup>x</sup> the binary genetic algorithm, we used a crossover rate of 0.5 and mutation rate of 0.001 based on an examination of past studies discussed in Refs. 21,23 .<sup>w</sup> <sup>x</sup> For the population size, pilot studies suggested that small sizes 10 give slightly better results after 2500Ž . individuals as well as converge more rapidly than larger sizes. Our results with small population sizes are also consistent with previous studies discussed in Ref. 20 .<sup>w</sup> <sup>x</sup>

Each observation results from executing the appropriate algorithm real, binary, or hill climbing Ž . with specified parameter settings on randomly selected problems. A problem is a combination of reference point, preferred class, and change cost vector. The techniques described in Appendices A and B were used to generate the Voronoi diagram for a given set of sites and determine the optimal solution for the Voronoi diagram, reference point, change cost vector, and preferred class. The costs were uniformly drawn from a population with a moderate Ž . 0.3 coefficient of variation. There is one set of sites for each combination of attributes and number of classes.

![](/api/attachments/QY3VAJYN/fulltext/images/da78cf29d1e98c16de7bc82f95e13e57ada36bacddc054d4f8a2677a9a158c93.jpg)  
Fig. 3. Search criteria results for the mutation<sup>r</sup>crossover operators.

Table 1  
PD parameter estimates for 10 attributes<sup>a</sup>

<table><tr><td>Variable</td><td>df</td><td>Parameter estimate</td><td>Standard error</td><td>t-value</td><td>P-value</td></tr><tr><td>INTERCEPT</td><td>1</td><td>62.064340</td><td>2.57018713</td><td>24.148</td><td>0.0001</td></tr><tr><td>FC</td><td>1</td><td>-53.445617</td><td>3.83140876</td><td>-13.949</td><td>0.0001</td></tr><tr><td> $NC_L$ </td><td>1</td><td>6.432133</td><td>2.42319567</td><td>2.654</td><td>0.0087</td></tr><tr><td> $NC_M$ </td><td>1</td><td>18.872213</td><td>4.10872816</td><td>4.593</td><td>0.0001</td></tr><tr><td> $FC*NC_M$ </td><td>1</td><td>-12.680096</td><td>6.63619464</td><td>-1.911</td><td>0.0578</td></tr></table>

$^ \mathrm { a } R ^ { 2 }$ 0.6983; Adj. $R ^ { 2 }$ 0.6907.

## 5.4. Pilot study results

We first conducted informal studies about the issues specific to the real genetic algorithm. Fig. 2 displays results about the two infeasible fitness functions Ž . SFitness vs. AFitness . Each point in Fig. 2 is an average over a number of observations where each observation is the average of a number of runs with the same initial population. The results in Fig. 3 support the notion that genetic algorithms can be sensitive to the choice of fitness functions for infeasible solutions. The SFitness is the better choice as all genetic algorithms with feasibility control less than 1 have improved performance. It is interesting to note that the order of the real-0 and binary algorithms changes with the different infeasible fitness functions.

Fig. 3 depicts results about the four combinations of operator crossover and mutation and search cri-Ž . terion diversity and fitness . The fitness and diver-Ž .

Table 2  
PI parameter estimates for 10 attributes<sup>a</sup>

<table><tr><td>Variable</td><td>df</td><td>Parameter estimate</td><td>Standard error</td><td>t-value</td><td>P-value</td></tr><tr><td>INTERCEPT</td><td>1</td><td>68.962752</td><td>0.45239398</td><td>152.440</td><td>0.0001</td></tr><tr><td>FC</td><td>1</td><td>24.703983</td><td>0.61000792</td><td>40.498</td><td>0.0001</td></tr><tr><td> $NC_L$ </td><td>1</td><td>1.506254</td><td>0.47251011</td><td>3.188</td><td>0.0017</td></tr><tr><td> $NC_M$ </td><td>1</td><td>1.150204</td><td>0.47251011</td><td>2.434</td><td>0.0160</td></tr></table>

$^ \mathrm { a } R ^ { 2 }$ 0.9112; Adj. $R ^ { 2 }$ 0.9095.

Table 3  
PD parameter estimates for five attributes<sup>a</sup>

<table><tr><td>Variable</td><td>df</td><td>Parameter estimate</td><td>Standard error</td><td>t-value</td><td>P-value</td></tr><tr><td>INTERCEPT</td><td>1</td><td>9.760559</td><td>0.39049992</td><td>24.995</td><td>0.0001</td></tr><tr><td>FC</td><td>1</td><td>-9.769902</td><td>0.52654999</td><td>-18.555</td><td>0.0001</td></tr><tr><td> $NC_L$ </td><td>1</td><td>1.431880</td><td>0.40786387</td><td>3.511</td><td>0.0006</td></tr><tr><td> $NC_M$ </td><td>1</td><td>1.815742</td><td>0.40786387</td><td>4.452</td><td>0.0001</td></tr></table>

${ } ^ { \mathrm { a } } R ^ { 2 }$ 0.6947; Adj. $R ^ { 2 }$ 0.6890.

sity versions of the crossover operator ŽCrossFit and CrossDiÕ, respectively do not seem to affect the . results so we ignore them in our discussion. The mutation operator with the diversity criterion Ž . MutDiÕ provides slightly better results after 2500 individuals. It is interesting to note that the fitness criterion Ž . MutFit provides a very rapid improvement in the fitness function. However, the rapid improvement cannot be sustained, indicating that more search depth may be necessary. Even with the same binary search depth, the MutFit operator requires considerably longer run times up to twoŽ times as long than the. MutDiÕ operator because the MutDiÕ operator only performs the binary search if the initial mutation result is infeasible. Thus, we strongly prefer the MutDiÕ operator because it provides excellent results after 2500 individuals and uses little search effort.

## 5.5. Experiment results

For experiment 1, Tables 1–4 show the parameter estimates for the response functions PD and PI inŽ . Eq. 8 for five and 10 attributes. In these tables,Ž . only those variables that were found to be significant at a P-value of 0.06 or below are shown.

The results support Hypothesis 1 but offer only mild support for Hypothesis 1.1. For Hypothesis 1, feasibility control is significant in all response functions. To aid in understanding the results for Hypothesis 1.1, Table 5 decomposes the response function by number of classes. This table reveals that there is some support in the response function for percentage improvement. The percentage improvement functions for 10 attributes support Hypothesis 1.1. However, in the five attribute dimension cases, there is support for the feasibility control being more important to the low number of classes. In the percentage difference response functions, the slope of the response function is only affected by the number of classes in one case five attributes, medium .Ž .

Table 4  
PI parameter estimates for five attributes<sup>a</sup>

<table><tr><td>Variable</td><td>df</td><td>Parameter estimate</td><td>Standard error</td><td>t-value</td><td>P-value</td></tr><tr><td>INTERCEPT</td><td>1</td><td>86.850910</td><td>0.35075947</td><td>247.608</td><td>0.0001</td></tr><tr><td>FC</td><td>1</td><td>10.470872</td><td>0.63382790</td><td>16.520</td><td>0.0001</td></tr><tr><td> $FC \times NC_L$ </td><td>1</td><td>2.064426</td><td>0.67227601</td><td>3.071</td><td>0.0025</td></tr></table>

${ } ^ { \mathrm { a } } R ^ { 2 }$ 0.6918; Adj. $R ^ { 2 }$ 0.6880.

Table 5  
Response functions for experiment 1

<table><tr><td rowspan="2">Classes</td><td colspan="2">Dimensions</td></tr><tr><td>5</td><td>10</td></tr><tr><td rowspan="2">High</td><td> $E(PD) = 9.76-9.77 \text{ FC}$ </td><td> $E(PD) = 62.06-53.45 \text{ FC}$ </td></tr><tr><td> $E(\text{PI}) = 86.85 + 10.47 \text{ FC}$ </td><td> $E(\text{PI}) = 68.26 + 24.70 \text{ FC}$ </td></tr><tr><td rowspan="2">Medium</td><td> $E(PD) = 11.38-9.77 \text{ FC}$ </td><td> $E(PD) = 80.86-66.12 \text{ FC}$ </td></tr><tr><td> $E(\text{PI}) = 86.85 + 10.47 \text{ FC}$ </td><td> $E(\text{PI}) = 70.11 + 24.70 \text{ FC}$ </td></tr><tr><td rowspan="2">Low</td><td> $E(PD) = 11.38-9.77 \text{ FC}$ </td><td> $E(PD) = 68.69-53.45 \text{ FC}$ </td></tr><tr><td> $E(\text{PI}) = 86.85 + 12.54 \text{ FC}$ </td><td> $E(\text{PI}) = 70.46 + 24.70 \text{ FC}$ </td></tr></table>

There are a number of possible explanations for the weak support of Hypothesis 1.1. One explanation is that the increase in classes was not enough to make a difference. Another explanation is that competing forces are at work. For example, the fitness function exerts strong pressure to focus on feasible solutions and infeasible solutions close to the optimal. This increased selection pressure combined with the smaller feasible space may counteract the effect of increased constraints.

Table 6  
PD ANOVA results for experiment 2

<table><tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Algorithm</td><td>44008.256</td><td>3</td><td>14669.419</td><td>150.2</td><td>8.64E-40</td><td>2.683</td></tr><tr><td>Within</td><td>11329.226</td><td>116</td><td>97.666</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>55337.482</td><td>119</td><td></td><td></td><td></td><td></td></tr></table>

Table 7  
PI ANOVA results for experiment 2

<table><tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Algorithm</td><td>49173.759</td><td>3</td><td>16391.253</td><td>843.305</td><td>1.43E-78</td><td>2.683</td></tr><tr><td>Within</td><td>2254.682</td><td>116</td><td>19.437</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>51428.441</td><td>119</td><td></td><td></td><td></td><td></td></tr></table>

Table 8  
PD and PI summary results for experiment 2

<table><tr><td>ALG</td><td>PD Avg</td><td>PD Var</td><td>PI Avg</td><td>PI Var</td></tr><tr><td>Real-1</td><td>4.324</td><td>7.847</td><td>96.323</td><td>0.997</td></tr><tr><td>Real-0</td><td>16.601</td><td>38.987</td><td>86.051</td><td>6.345</td></tr><tr><td>HC</td><td>19.900</td><td>29.039</td><td>70.490</td><td>14.401</td></tr><tr><td>Binary</td><td>55.754</td><td>314.790</td><td>42.642</td><td>56.005</td></tr></table>

Tables 6–8 show the analysis of variance results for experiment 2. Because both analyses support the hypothesis that at least one of the means is different, t tests for equality of sample means were performed Ž . Tables 9 and 10 . The results support Hypothesis 2 in that real-1 is the best algorithm for both PD and PI measures. The results also support a ranking of the remaining algorithms as real-0, HC, and Binary. The reasonable performance of HC suggests that mutation is an important operator. The superiority of real-0 over HC suggests that reproduction and crossover play a significant, although not dominant, role in the search process. The poor performance of Binary suggests that the small role of mutation is not adequate in constrained optimization problems. Simple changes such as large increases in the mutation rate make Binary behave as a random search. A more fundamental change may be necessary.

For experiment 3, Fig. 4 shows results for various numbers of attributes when varying the maximum number of generations. These graphs support Hypothesis 3 in that performance deteriorates as the

Table 9  
PD sample mean results

<table><tr><td>Comparison</td><td>P-value</td><td>t-Value</td></tr><tr><td>Real-1, real-0</td><td>3.19412E-12</td><td>-9.82621685</td></tr><tr><td>Real-0, HC</td><td>0.032770655</td><td>-2.18817487</td></tr><tr><td>HC, Binary</td><td>2.62237E-12</td><td>10.59174601</td></tr></table>

Table 10  
PI sample mean results

<table><tr><td>Comparison</td><td>P-value</td><td>t-Value</td></tr><tr><td>Real-1, real-0</td><td>2.44412E-22</td><td>20.76336538</td></tr><tr><td>Real-0, HC</td><td>3.13435E-24</td><td>18.71289961</td></tr><tr><td>HC, Binary</td><td>8.40517E-22</td><td>-18.1783105</td></tr></table>

![](/api/attachments/QY3VAJYN/fulltext/images/c53bbebdf367663b7133677d77fdf2ebdedc8b1d24bac0a6151243b85e523e88.jpg)

![](/api/attachments/QY3VAJYN/fulltext/images/fc81bf4242a9985937fe955f7006e501b56ed0c1877fa1b6287ebbb6e14d3d0c.jpg)

![](/api/attachments/QY3VAJYN/fulltext/images/dfbe18443eee257895a9a6aa87bc06b39e081822de7f65f64d6c435a011e7b9c.jpg)

![](/api/attachments/QY3VAJYN/fulltext/images/ffb2edcb025a226d61de34537b87f05e4ba2fcad7c7c1a5e72d4a79a284b2912.jpg)  
Fig. 4. PD and PI search effort results.

number of attributes increases. The graphs for the high and low classes look similar, indicating that real-1 was robust with increasing the number of constraints in this range. However, the results do not seem to show that the search effort increases to reach the performance limit. In the PD graph, the performance limit is reached at about 4000 individuals for all four graphs even though there is some fluctuation after this point in the 10 attribute case. In another simulation, we increased the number of individuals of the 10A case from 10,000 to 19,000. Surprisingly, the 10A performance did not seem to improve much even with increasing individuals to 19,000.

## 5.6. Discussion

These results provide several lessons about genetic algorithm performance. First, these results provide additional evidence that constrained optimization problems are difficult for genetic algorithms. The poor performance of the traditional binary algorithm shows that specialized designs may be necessary. Second, these results provide additional evidence about the viability of real genetic algorithms. The real genetic algorithm is a good tool even when constraint boundaries are not known precisely. The reasonable performance of the real algorithm even without feasibility control shows that real encoding is responsible for some of the success. Third, these results show that genetic algorithm performance on constrained optimization problems is rather sensitive to the operators and fitness function. The importance of feasibility control shows the need for feasibility preserving operators. In addition, the results support fitness functions that do not overly penalize infeasible solutions and operators that emphasize diversity rather than fitness improvements.

A final lesson from this study involves the use of approximate solution techniques such as genetic algorithms vs. optimal solution techniques such as quadratic programming. As the results demonstrate, the best approximate results were only within 10% of the optimal solution for the largest size problems tested. There is ample reason to prefer the optimal solution if it can be generated efficiently. Because constructing a Voronoi diagram is computationally expensive, the real genetic algorithm may be preferred for moderate-size problems in dynamic environments and time-constrained environments. The real genetic algorithm provides a fast approximate solution for these environments. In addition, for large problems, the real genetic algorithm provides a solution approach when the Voronoi diagram cannot be constructed.

## 6. Summary and conclusion

We examined the cost-minimizing inverse classification problem with respect to similarity-based classification systems. As a form of sensitivity analysis, the importance of this problem seems likely to grow with the spread of classification systems in organizations. The use of similarity-based systems was motivated by their importance and their implicit representation of concept boundaries. A genetic algorithm is well suited to this problem because the concept boundaries can be implicitly encoded in the fitness function. We developed three genetic algorithms real, binary, hill climbing and comparedŽ . their performance to the optimal solution. The strong performance of the real genetic algorithm emphasized that genetic algorithms can perform well on constrained optimization problems even when the constraint boundaries are not explicitly represented. In addition, the empirical results replicated other studies in the need for feasibility control in operator design and the viability of real encoding.

We see this as an initial effort to study inverse classification problems. An obvious extension to this study is to relax the real attribute restriction. Many classification systems operate with attributes of mixed data types including real, integer, ordinal, and nominal. To study this relaxation, we will need to amend our genetic algorithms, use an actual classification system, and devise good heuristics with which to compare our approach. Because the performance of the binary genetic algorithm was poor here, a mapping between real and discrete representations may be necessary. Other possible extensions are studying other classification systems and searching for tradeoffs between the benefit of moving to a better class and the cost of changing attributes.

## Appendix A. Mathematical programming formulation

The assumptions given in Section 3.2 allow us to transform the inverse classification problem into an equivalent problem based on Voronoi diagrams. Formally, a Voronoi diagram is a cell complex that reflects proximity relationships as follows. Let $S =$ $\{ s _ { 1 } , s _ { 2 } , \ldots , s _ { m } \}$ be a set of m sites defined in $E ^ { n }$ Then the Voronoi diagram V SŽ . of S decomposes $E ^ { n }$ into m cells, one for each site in $S ,$ with the property that any point x lies in the cell corresponding to site $s _ { i }$ if and only if $\delta ( \boldsymbol { x } , s _ { i } ) < \delta ( \boldsymbol { x } , s _ { i } ) \forall j \in$ $S - \left\{ i \right\}$ , where $\delta ( { x } , \ { s } _ { i } )$ denotes the Euclidean distance between point x and site $s _ { i } \ [ 9 , 1 8 ]$

The relationships between the inverse classification problem and Voronoi diagrams can be described as follows. Prototypes in the classification system correspond to sites in the Voronoi diagram. Attributes of a prototype or an instance correspond to dimensions in the Voronoi diagram. Concepts defining a given class are represented in the Voronoi diagram as bisectors separating two adjacent regions.

Fig. A1 shows a Voronoi diagram in the plane for five sites in the range $\mathrm { L B } = 1 0 0 , \ \mathrm { U B } = 2 0 0$ . Note that not all pairs of sites have their bisecting surfaces present in the diagram. For example, there is no point common to sites 1 and 3. Consider point $p$ in region 2, and assume that region 3 is the preferred region. Then point $q ,$ shown on the bisector separating regions 2 and 3, is a solution to the inverse classification problem if attribute change costs are uniform.

One of the problems in using Voronoi diagrams is that it is difficult to generate such diagrams in arbitrary space. Commercially available software packages, such as Mathematica 13 , do not have the <sup>w</sup> <sup>x</sup> ability to construct Voronoi diagrams beyond two-dimensional space. As a result, our approach is based on the observation that Voronoi diagrams in n dimensions are related to arrangements of hyperplanes in $\left( n + 1 \right)$ dimensions 18 . In addition, we also use<sup>w</sup> <sup>x</sup> the reverse search algorithm 12 for enumeration of<sup>w</sup> <sup>x</sup> all vertices of a convex polyhedron, and its C implementation 11 . Details of the method used in the <sup>w</sup> <sup>x</sup> construction of Voronoi diagrams are given in $\mathsf { A p - }$ pendix B.

![](/api/attachments/QY3VAJYN/fulltext/images/a5e75b3740dead90fe25682eeb3fade789b64cea078621ebdde58dfc5370baca.jpg)  
Fig. A1. Voronoi diagram for two dimensions and five sites.

This method allows us to determine the set of bisectors that are present in the Voronoi diagram. Let $B ( l )$ denote the set of sites with which site $s _ { \lambda }$ has a bisector in the Voronoi diagram. Then $B ( l )$ can be partitioned into sets $B ^ { + } ( l )$ and $B ^ { - } ( l )$ defined as follows:<sup>2</sup>

$$
B ^ {+} (\lambda) = \left\{s _ {i} \left| \sum_ {j = 1} ^ {n} \left(s _ {\lambda , j} - s _ {i, j}\right) s _ {\lambda , j} - \frac {1}{2} \sum_ {j = 1} ^ {n} \left(s _ {\lambda , j} ^ {2} - s _ {i, j} ^ {2}\right) > 0 \right. \right\},\tag{A1}
$$

$$
B ^ {-} (\lambda) = \left\{s _ {i} \left| \sum_ {j = 1} ^ {n} \left(s _ {\lambda , j} - s _ {i, j}\right) s _ {\lambda , j} - \frac {1}{2} \sum_ {j = 1} ^ {n} \left(s _ {\lambda , j} ^ {2} - s _ {i, j} ^ {2}\right) <   0 \right. \right\}.\tag{A2}
$$

It follows that any other point $q = \{ q _ { 1 } , q _ { 2 } , . . . , q _ { n } \}$ is contained in the open region of site $s _ { \lambda }$ if it satisfies similar constraints with respect to the sites in $B ^ { + } ( l )$ and $B ^ { - } ( l )$

Using the constraints in Eqs. A1 and A2 , theŽ . Ž . inverse classification problem can be formulated as shown below in Problem CP2. Let $h _ { j }$ denote the change cost associated with attribute $A _ { j } .$ Since $h _ { j }$ is stationary, the objective function is the weighted Euclidean distance between the original and modified instances. In the formulation shown below, we have chosen to minimize the square of the weighted Euclidean distance:

Problem CP2: min $\sum _ { j = 1 } ^ { n } h _ { j } ^ { 2 } \big ( r _ { j } - q _ { j } \big ) ^ { 2 }$ q

$$
\begin{array}{l} \text {s.t.} \quad \sum_ {j = 1} ^ {n} \left(s _ {i, j} - s _ {k, j}\right) q _ {j} \\ \qquad - \frac {1}{2} \sum_ {j = 1} ^ {n} \left(s _ {i, j} ^ {2} - s _ {k, j} ^ {2}\right) \geq 0 \forall s _ {k} \in B ^ {+} (\lambda) \\ \qquad - \left(\sum_ {j = 1} ^ {n} \left(s _ {i, j} - s _ {k, j}\right) q _ {j} \right. \\ \qquad - \frac {1}{2} \sum_ {j = 1} ^ {n} \left(s _ {i, j} ^ {2} - s _ {k, j} ^ {2}\right) \Bigg) \geq 0 \forall s _ {k} \in B ^ {-} (\lambda) \\ q _ {j} \geq \mathrm{LBfor} j = 1, 2, \dots , n \\ - q _ {j} \geq - \mathrm{UBfor} j = 1, 2, \dots , n. \end{array}
$$

The objective function in Problem CP2 can be reduced to standard form as:

$$
\text { Problem   CP3: } \min _ {\boldsymbol {q}} \boldsymbol {g} ^ {\mathrm{T}} \boldsymbol {q} + \frac {1}{2} \boldsymbol {q} ^ {\mathrm{T}} \mathbf {H} \boldsymbol {q}
$$

where g is an $n \times 1$ column vector whose jth element is $- 2 p _ { j } h _ { j } ^ { 2 }$ and H is an $n \times n$ diagonal matrix whose jth diagonal element is $2 h _ { j } ^ { 2 } , \ q$ is an $n \times 1$ column vector representing the decision variable, and ${ \pmb g } ^ { \mathrm { T } } , \ { \pmb q } ^ { \mathrm { T } }$ denote transposes. Since H is positive definite, a unique solution to Problem CP3 exists provided the constraint set is consistent. In this research, we used the IMSL procedure QPROG 27<sup>w</sup> <sup>x</sup> to solve Problem CP3.

## Appendix B. Construction of Voronoi diagram

We describe here the steps used for constructing Voronoi diagrams.

Input: Coordinates of m sites in $E ^ { n } .$ . The ith site is denoted by $s _ { i } , i = 1 , 2 , \cdots , m .$

Output: Set of bisector surfaces hyperplanesŽ . defining the region of site $s _ { i } .$

B.1. Step 1: transform coordinates to hyperplane in $E ^ { n + \mathbf { \lambda } }$ 1

We use the property that Voronoi diagrams in $E ^ { n + 1 }$ . Let the coordinates of site $s _ { i }$ in $E ^ { n }$ be denoted by $\{ s _ { 1 } , s _ { 2 } , . . . , s _ { m } \}$ . We map each site $s _ { i } \in S$ in $E ^ { n }$ to the hyperplane of a unit paraboloid in $E ^ { n + 1 }$ by using the geometric transformation $\xi$ defined below. For this purpose, we identify any point $\{ y _ { i , 1 } , ~ y _ { i , 2 } \}$ $\cdots \ , \ y _ { i , n } \} \ E ^ { n }$ with the hyperplane $\{ y _ { i , 1 } , ~ y _ { i , 2 } , ~ . \ldots ,$ $y _ { i , n } , \ 0 \}$ in $E ^ { n + 1 }$ . Transform $\xi ( s _ { i } )$ maps the coordinates of site $s _ { i }$ to the hyperplane:

$$
\begin{array}{c} \xi (s _ {i}) = 2 (s _ {i, 1} x _ {1} + s _ {i, 2} x _ {2} + \ldots + s _ {i, n} x _ {n}) \\ - (s _ {i, 1} ^ {2} + s _ {i, 2} ^ {2} + \ldots + s _ {i, n} ^ {2}). \end{array}\tag{B1}
$$

It has been shown in Ref. 18 that<sup>w</sup> <sup>x</sup> $\xi ( s _ { i } )$ is the unique hyperplane that touches the unit paraboloid $U { : } s _ { i , n + 1 } = s _ { i , 1 } ^ { 2 } + s _ { i , 2 } ^ { 2 } + \ldots + s _ { i , n } ^ { 2 }$ in the vertical projection $U ( s _ { i } )$ of $s _ { i }$ on surface U. The transformations hence result in a convex polyhedron given by the set of m unique hyperplanes in $E ^ { n + 1 }$

B.2. Step 2: enumerate all Õertices of conÕex polyhedron

Enumeration of all vertices of the convex polyhedron is based on the property that vertices of the convex polyhedron in $E ^ { n + 1 }$ , when projected back to $E ^ { n }$ , are also vertices of the Voronoi diagram seeŽ Ref. 18 . The reverse search enumeration method<sup>w</sup> <sup>x</sup>. described in Ref. 12 was employed for this pur- <sup>w</sup> <sup>x</sup> pose. A C language implementation of the algorithm is given in Ref. 11 . This implementation was found<sup>w</sup> <sup>x</sup> to be suitable since it uses multiple precision rational arithmetic and is capable of handling problems of fairly large size. The vertices generated by the algorithm are transformed to $E ^ { n }$ by projection, i.e. simply dropping the Ž . n<sup>q</sup>1 th coordinate.

## B.3. Step 3: identify actiÕe bisecting surfaces of Voronoi diagram

Identification of the active bisector surfaces was done by using the following decision rule. Consider sites $s _ { i }$ and $s _ { k }$ . The bisecting surface, SepŽ . i, k , separating these two sites is the hyperplane:

$$
\begin{array}{l} \operatorname{Sep} (i, k) \colon \sum_ {j = 1} ^ {n} \left(s _ {i, j} - s _ {k, j}\right) x _ {j} \\ \qquad - \frac {1}{2} \sum_ {j = 1} ^ {n} \left(s _ {i, j} ^ {2} - s _ {k, j} ^ {2}\right) = 0. \end{array}\tag{B2}
$$

If SepŽ . i, k contains one or more of the vertices generated in step 2, then it is an active bisector surface and is present in the Voronoi diagram; otherwise, not. Identification of all the bisector surfaces Ž .<sup>n</sup> thus partitions the n-dimensional space LB, UB into m convex regions, one for each of the m sites.

## B.4. Step 4: testing

Testing of the Voronoi diagram is necessary since vertex coordinates are converted from rational to real values, which may cause some loss in precision. To test the algorithm, we generated several thousand points at random and ensured that the classification by considering the active bisector surfaces was identical to the classification using the nearest neighbor rule.

## References

<sup>w</sup> <sup>x</sup> 1 D. Aha, D. Kibler, M. Albert, Instance-based learning algorithms, Machine Learning 6 1991 37–66.Ž .

<sup>w</sup> <sup>x</sup> 2 B. Allen, Case-based reasoning: business applications, Communications of the ACM 37 3 1994 40–42, March.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 K. Al-Sultan, Nearest point problems: theory and algorithms, PhD Dissertation, The University of Michigan, Ann Arbor, 1990.

<sup>w</sup> <sup>x</sup> 4 K. Al-Sultan, A Newton-based radius reduction algorithm for nearest point problems in pos cones, ORSA Journal on Computing 6 3 1994 292–299, Summer. Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 K. Al-Sultan, A Tabu search approach to the clustering problem, Pattern Recognition 28 9 1995 1443–1451.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 K. Al-Sultan, K. Murty, Exterior point algorithms for nearest points and quadratic programs, Mathematical Programs 57 Ž . 1992 145–161.

<sup>w</sup> <sup>x</sup> 7 K. Al-Sultan, S. Selim, A global algorithm for the fuzzy clustering problem, Pattern Recognition 26 9 1993 1357–Ž . Ž . 1361.

<sup>w</sup> <sup>x</sup> 8 J. Antonisse, A new interpretation of schema notation that overturns the binary encoding constraint, in: J. Schaffer Ž .Ed. , Proceedings of the Third International Conference on Genetic Algorithms, Morgan Kaufman Publ., Los Altos, CA, 1989.

<sup>w</sup> <sup>x</sup>9 F. Aurenhammer, Voronoi diagrams — a survey of a fundamental geometric data structure, ACM Computing Surveys 23 3 1991 345–405, September.Ž . Ž .

<sup>w</sup> <sup>x</sup>10 P. Avesani, E. Blanzieri, F. Ricci, Advanced metrics for class-driven similarity search,Proceedings of the 10th International Workshop on Database and Expert System Applications,1998.

<sup>w</sup> <sup>x</sup> 11 D. Avis, A C implementation of the reverse search vertex enumeration algorithm, Technical Report SOCS-92.120, School of Computer Science, McGill University, Montreal, Quebec H3A 2A7, October 1992; revised June 1993.

<sup>w</sup> <sup>x</sup> 12 D. Avis, H. Fukuda, A pivoting algorithm for convex hulls and vertex enumeration of arrangements and polyhedra, Discrete and Computational Geometry 8 1992 295–313.Ž .

<sup>w</sup> <sup>x</sup> 13 P. Boyland, Guide to standard Mathematica packages, Technical Report, Wolfram Research, Champaign, IL, 1991.

<sup>w</sup> <sup>x</sup> 14 A. Charnes, S. Haag, P. Jaska, J. Semple, Sensitivity of efficiency classifications in the additive model of data envelopment analysis, International Journal of Systems Science 23 Ž . Ž .5 1992 789–798.

<sup>w</sup> <sup>x</sup> 15 G.S. Cluff, P.G. Farnham, Standard and Poor’s vs. Moody’s: which city characteristics influence municipal bond ratings?, Quarterly Review of Economics and Business 2 3 1984Ž . Ž . 72–94.

<sup>w</sup> <sup>x</sup> 16 R. Creecy, B. Masand, S. Smith, D. Waltz, Trading MIPS and memory for knowledge engineering, Communications of the ACM 35 8 1992 48–64, August.Ž . Ž .

<sup>w</sup> <sup>x</sup>17 B. Dasrathy Ed. , Nearest Neighbor NN Norms: NN Pat-Ž . Ž . tern Classification Techniques, IEEE Computer Society Press, Los Alamitos, CA, 1990.

<sup>w</sup> <sup>x</sup> 18 H. Edelsbrunner, Algorithms in Combinatorial Geometry, Springer-Verlag, Berlin, Germany, 1987.

<sup>w</sup> <sup>x</sup> 19 F. Glover, Tabu search — Part I, ORSA Journal on Computing 2 1 1989 190–206. Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 D. Goldberg, Sizing populations for serial and parallel genetic algorithms, in: J. Schaffer Ed. , Proceedings of the Ž . Third International Conference on Genetic Algorithms, Morgan Kaufman Publ., San Mateo, CA, 1989.

<sup>w</sup> <sup>x</sup> 21 D. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning, Addison-Wesley, Reading, MA, 1989.

22 M. Goodman, Prism: a case-based telex classifier,Proceedings of the 2nd Innovative Applications of Artificial Intelligence,1990.

<sup>w</sup> <sup>x</sup> 23 J. Grefenstette, Optimization of control parameters for genetic algorithms, IEEE Transactions on Systems, Man and Cybernetics 1 1986 122–128, JanuaryŽ . <sup>r</sup>February.

<sup>w</sup> <sup>x</sup> 24 J. Grefenstette, J. Baker, How genetic algorithms word: a critical look at implicit parallelism, in: J. Schaffer Ed. ,Ž . Proceedings of the Third International Conference on Genetic Algorithms, Morgan Kaufman Publ., San Mateo, CA, 1989, pp. 20–27.

<sup>w</sup> <sup>x</sup> 25 T. Hastie, R. Tibshirani, Discriminant adaptive nearest neighbor classification, IEEE Transactions on Pattern Analysis and Machine Intelligence 18 6 1996 607–616, June. Ž . Ž .

<sup>w</sup> <sup>x</sup> 26 K. Hirota, W. Pedrycz, Prototype construction and evaluation as inverse problems in pattern classification, Pattern Recognition 25 6 1992 601–608.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 IMSL Math<sup>r</sup>Library, User’s Manual — Fortran Subroutines for Mathematical Applications, Version 1.1, December 1989.

<sup>w</sup> <sup>x</sup> 28 K. Irani, J. Cheng, U. Fayyad, Z. Qian, Applying machine learning to semiconductor manufacturing, IEEE Expert 8 1Ž . Ž . 1993 41–47, February.

<sup>w</sup> <sup>x</sup> 29 J. Kim, H. Myung, Evolutionary programming techniques for constrained optimization problems, IEEE Transactions on Evolutionary Computation 1 2 1997 129–140, July. Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 S. Kimbrough, J. Oliver, On automating candle lighting analysis: insight from search with genetic algorithms and approximate models,Proceedings of the Twenty-Seventh Annual Hawaii International Conference on System Sciences, 1994, pp. 536–544.

<sup>w</sup> <sup>x</sup> 31 P. Laarhoven, E. Aarts, Simulated Annealing: Theory and Practice, Reidel, the Netherlands, 1987.

<sup>w</sup> <sup>x</sup> 32 B. Mak, R. Blanning, An empirical measure of element contribution in neural networks, IEEE Transactions on Systems, Man, and Cybernetics 28 4 1998 561–564, Novem-Ž . Ž . ber.

<sup>w</sup> <sup>x</sup> 33 Z. Michalewicz, A survey of constraint handling techniques in evolutionary computation methods, in: J. McDonnell, R. Reynolds, D. Fogel Eds. , Proceedings of the 4th AnnualŽ . Conference on Evolutionary Programming, MIT Press, Cambridge, MA, 1996, pp. 135–155.

<sup>w</sup> <sup>x</sup> 34 Z. Michalewicz, Genetic Algorithms<sup>q</sup>Data Structures<sup>s</sup> Evolution Programs, 3rd edn., Springer-Verlag, Berlin, Germany, 1996.

<sup>w</sup> <sup>x</sup> 35 Z. Michalewicz, M. Schoenauer, Evolutionary algorithms for constrained optimization problems, Evolutionary Computation 4 1 1996 1–32.Ž . Ž .

<sup>w</sup> <sup>x</sup> 36 Z. Michalewicz, G. Vignaux, M. Hobbs, A nonstandard genetic algorithm for the nonlinear transportation problem, ORSA Journal on Computing 3 4 1991 307–316, Fall.Ž . Ž .

37 K. Murty, Linear Complementarity, Linear and Non-Linear Programming, Springer-Verlag, Berlin, 1988.

<sup>w</sup> <sup>x</sup> 38 J. Neter, W. Wasserman, M. Kuttner, Applied Linear Statistical Models, Richard D. Irwin, Homewood, IL, 1985.

<sup>w</sup> <sup>x</sup> 39 B. Porter, R. Bareiss, R. Holte, Concept learning and heuristic classification in weak theory domains, Artificial Intelligence Journal 45 1 1990 229–264.Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 S. Selim, K. Alsultan, A simulated annealing algorithm for the clustering problem, Pattern Recognition 24 10 1991Ž . Ž . 1003–1008.

<sup>w</sup> <sup>x</sup> 41 E. Simoudis, Using case-based retrieval for customer technical support, IEEE Expert 7 5 1992 7–11, October.Ž . Ž .

<sup>w</sup> <sup>x</sup> 42 C. Stanfill, D. Waltz, Toward memory-based reasoning, Communications of the ACM 29 12 1986 1213–1228,Ž . Ž . December.

<sup>w</sup> <sup>x</sup> 43 K. Tam, M. Kiang, Predicting bank failures: a neural network approach, Applied Artificial Intelligence 4 1990 265– Ž . 282.

<sup>w</sup> <sup>x</sup> 44 A. Wright, Genetic algorithms for real parameter optimization, in: G. Rawlins Ed. , Foundations of Genetic Algo-Ž . rithms, Morgan Kaufman Publ., San Mateo, CA, 1991.

<sup>w</sup> <sup>x</sup>45 P. Zakarauskas, J. Ozard, Complexity analysis for partitioning nearest neighbor searching algorithms, IEEE Transactions on Pattern Analysis and Machine Intelligence 18 6Ž . Ž . 1996 663–668, June.

Michael V. Mannino is an Associate Professor of Informations Systems in the Graduate School of Business Administration, University of Colorado at Denver. Previously, he was a faculty member in the Computer and Information Sciences Department at the University of Florida, the Department of Management Science and Information System at the University of Texas at Austin, and the Management Science Department at the University of Washington. Dr. Mannino teaches and conducts research in database management, software engineering, and knowledge representation. His articles have appeared in journals affiliated with the ACM, IEEE, and TIMS. IBM and Unify have supported his research. He is also the author of Database Application DeÕelopment and Design, an introductory database management textbook to be published in fall 2000 by Irwin McGraw-Hill.

Murli Koushik was formerly Assistant Professor of Information Systems in the School of Business Administration at the University of Washington, Seattle, WA. He has published articles in Information Systems Research ISR and Information Systems. He Ž . is currently a Senior Database Administrator in the Information Technology Group at Microsoft, Redmond, WA.
