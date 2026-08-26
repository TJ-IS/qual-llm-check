---
otero_id: 2644
otero_key: "UWHCKS3J"
title: "Hybrid approaches for classification under information acquisition cost constraint"
authors: "Parag C. Pendharkar"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.07.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 41 (2005) 228 – 241

www.elsevier.com/locate/dsw

# Hybrid approaches for classification under information acquisition cost constraint

Parag C. Pendharkar<sup>\*</sup>

School of Business Administration Pennsylvania State University at Harrisburg, 777 West Harrisburg Pike Middletown, PA 17057, United States

Received 13 September 2003; received in revised form 5 July 2004; accepted 7 July 2004 Available online 14 August 2004

## Abstract

We address a problem of classification with information acquisition cost constraint (CIACC). The objective of the CIACC problem is to develop a classification function that maximizes correct classifications under the user defined information acquisition cost constraint. We propose hybrid simulated annealing and neural network (SA-ANN), and tabu search and neural network (TS-ANN) procedures to solve the CIACC problem. Using simulated and a real-world data set from medical domain, we show that the proposed hybrid procedures solve the CIACC problem. The results of our experiments indicate that the performance of hybrid approaches is sensitive to the data distribution, and memory-based hybrid tabu search approaches may perform as good as or better than probabilistic hybrid simulated annealing approach. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Economics of information; Computational complexity; Classification; Medical diagnosis; Heuristics; Artificial intelligence; Simulated annealing; Neural networks; Tabu Search; Knapsack optimization

## 1. Introduction

Classification systems play an important role in business decision-making. In financial decision-making, classification systems are used for consumer credit granting decisions and for assessing corporate financial health [29]. There are several classification systems available in the literature [1,29]. However, the practical use of classification systems may be limited because the current classification systems do not allow decision-makers to incorporate information acquisition cost constraint. For example, in several financial applications (loan approval, credit scoring, etc.), an applicant is asked to submit processing fee along with the application [20]. The processing fee may be used to validate the information entered in the application. It is important that the cost of validating the information should not exceed the processing fee. In other words, a classification system that requires the total cost of input variables (independent variables) exceed the cost of application processing fee may be of a little economic value to the organizations. Further, it may not be necessary to validate all the information entered in the application; validating a few attributes may be considered sufficient as long as the quality of decision is not impacted, and cost of validating the information is less than or equal to the processing fee. Traditional classification systems do not allow a decision-maker to incorporate information acquisition cost constraint. For example, in the aforementioned credit approval problem, it may be desirable to design a classification system that only uses those attributes such that the cost of validating information is less than or equal to the processing fee.

Using an information acquisition cost constraint may be useful in identifying cases that may have been difficult to classify within the given economic constraint. The difficult-to-classify cases may be the cases where more information is necessary, when compared to trivial cases, to classify them into an appropriate category. Such difficult-to-classify cases may need an organization to exceed the user-defined information acquisition cost constraint to acquire more information for their classification in an appropriate category.

The impact of information acquisition and search costs is studied widely in economics. For example, Brannon and Gorman [2] study the impact of price information costs on market performance and buyer and seller behavior. Rothschild [36,37] suggested three factors that have an influence on consumer behavior and market performance: the cost of search (information acquisition cost), the dispersion of prices, and the knowledge of price distribution. Since most consumers are on budget, Brannon and Gorman [2] write <sup>b</sup>First and foremost of the factors that determine the amount of search is the marginal cost of search. As the cost of search increases, the amount of search undertaken decreases, according to the laws of demand.<sup>Q</sup>

While most of the research related to information acquisition/search cost in economics is related to one product, multiple suppliers and one budget, information acquisition cost problem in classification is that of multiple products (attributes), multiple costs and one budget. Further, in classification problems a decision-maker need not consider all the attributes for making a decision. In the case of credit screening problem described above, a can validate only few attributes from an application. Trusted third-party information provider companies, such as USSearch (www.ussearch.com), offer different choice of products at different prices. Each product may have a different impact on decision-making. Thus, selection of right combination of attributes, in consideration of cost and decision-making, can help a select the right product to purchase. We define the problem of designing a classification system, where information acquisition costs are considered, as the problem of classification with information acquisition cost constraint (CIACC).

The contributions of the current research are as follows. First, we propose a classification problem with information acquisition cost constraint. Second, we show that the CIACC problem is NP-hard. And third, we propose a procedure based on hybrid heuristic neighborhood search simulated annealing (SA) and artificial neural network (ANN), and tabu search (TS) and ANN algorithms for solving the classification problem under information acquisition cost constraint.

The rest of the paper is organized as follows. In Section 2, we describe the problem of classification with information acquisition cost constraint and show that the problem is NP-hard. In Section 3, we review the related research on cost sensitive classification. In Section 4, we propose a hybrid SA-ANN, and TS-ANN greedy heuristic (GH) and ratio heuristic (RH) algorithms for solving CIACC problem. In Section 5, using simulated data and a real-world data set, we describe the results of our experiments using the proposed heuristic algorithms. In Section 6, we conclude the paper with summary and directions for future work.

## 2. Classification with information acquisition cost constraint

In this section, we present a formal definition of the classification problem with information acquisition cost constraint. We use the following notation:

$\pmb { \cal D } { = } \{ d _ { 1 } , \ d _ { 2 } , \ . . . , \ d _ { m } \}$ is a vector of set of m decisions/classes, where $d _ { i } \in \{ 0 , 1 \}$ . If the ith $( i \in \{ 1$ $\cdots , m \}$ decision is taken then $d _ { i } { = } 1 , d _ { i } { = } 0$ otherwise. The vector D satisfies the constraint $\textstyle \sum _ { i = 1 } ^ { m } d _ { i } = 1$

$X = \{ x _ { 1 } , \ x _ { 2 } , \ . . . , \ x _ { n } \}$ is the vector of n input variables or decision making attributes considered for decision making.

$C { = } \{ c _ { 1 } , c _ { 2 } , . . . , c _ { n } \}$ is the vector of n information acquisition/validation costs associated with the n input variables.

$\scriptstyle { \eta = \mathrm { T h e } }$ maximum information acquisition cost allowed.

$U { = } \{ u _ { 1 } , \ u _ { 2 } , \ . . . , \ u _ { n } \} , \ u _ { i } { \in } \{ 0 , 1 \} , \ \forall i { \in } \{ 1 , \ . . . , \ n \}$ which satisfies the ${ \pmb U } ^ { T } { \pmb C } \le { \pmb \eta }$ constraint.

Let $f ( Z ) { \longrightarrow } D$ is a classification function, which takes vector $\boldsymbol { Z }$ of input variables and maps it to its respective decision in D. For classification problem, without information acquisition constraint, $\boldsymbol { Z }$ is the same as $X .$ In case of classification problem with information acquisition constraint, the set of elements in $\boldsymbol { Z }$ can be obtained as

$$
\mathbf {Z} = \{x _ {i} | \forall_ {i}, u _ {i} \neq 0 \}.
$$

The cardinality of $\boldsymbol { Z }$ is variable and depends on the number of non-zero elements in $U .$ Thus, the classification problem with information acquisition cost constraint consists of finding a combination of a classification function $f ( )$ and a vector $\mathbf { \delta } _ { Z , \mathrm { ~ ~ } }$ such that $f ( Z )$ is optimized. Whether the problem of optimization of $f ( )$ is that of maximization or minimization depends on the objectives of the decision-maker. If it is desired to learn a classification function (with information acquisition cost constraint) that maximizes the total correct classifications then the problem is that of maximization. On the other hand, if it is desired to learn a classification function to minimize total misclassification costs then the problem is that of minimization.

The classification with information acquisition cost constraint (CIACC) is an NP-hard problem and is very difficult to solve optimally. The following theorem formally proves the factorial complexity of CIACC.

## Theorem 1. The solution search space for worst case CIACC has factorial complexity.

Proof. Assuming $\eta \sum _ { i = 1 } ^ { n } c _ { i }$ for worst-case search space complexity, it can be shown that the search space of all the unique solution vectors $U$ is given by $2 ^ { n }$ . Ignoring a vector of all zero elements, the search space of all the unique realistic solutions is given by $2 ^ { n } - 1$ . From binomial theorem, we have $\begin{array} { r } { \mathbf { \overline { { 2 } } ^ { n } } = \sum _ { g = 0 } ^ { \overline { { n } } } \binom { n } { g } } \end{array}$ . This means that the solution search space complexity is $O ( n ! )$ . This proves the theorem. 5

Corollary 1. The general case CIACC is a zero-one knapsack problem and is NP-hard. The zero-one knapsack problem with linear objective function is known to be NP-hard [17] by using the objective function f(Z) and the constraint $\bar { U } ^ { T } \bar { C } \le \eta$ changes the zero-one knapsack problem to the CIACC problem. The objective function $f ( \mathbf { Z } )$ is the discriminant function which maximizes the total number of correct classifications. The function f(Z) may be either a linear or a non-linear function.

Given that CIACC problem is NP-hard heuristic approaches, such as tabu search, simulated annealing and genetic algorithms can be used to compute approximate solutions for the CIACC problem in polynomial time.

## 3. Literature review related to cost sensitive learning

Interest in cost sensitive learning dates back to late 1980s and early 1990s [5,18]. The early work focused on developing cost sensitive inductive learning methods to bias robot learning in uncertain and noisy environments [39,8]. In the early 1990s, Mookerjee and Dos Santos [18] formally incorporated misclassification cost-based metrics into classification systems. They argued that most of the classification systems maximize solution accuracy (number of correctly classified cases) and very few maximize the system value. Mookerjee and Dos Santos [18] defined system value as the benefits (of correctly classifying objects less the costs of incorrect classification) obtained from the system’s solutions, and the costs incurred in using the system. The costs incurred include information acquisition, social and personal costs resulting from the use of the classification systems. Using Moore and Whinston’s [22,23] studies as a theoretical basis, Mookerjee and Dos Santos [18] proposed a valuebased induction algorithm that allowed information to be acquired only if its value exceeds its cost. In a series of simulation experiments, Mookerjee and Dos Santos [18] found that their proposed algorithm resulted in a greater system value than the ID3 algorithm [34], and the ID3 algorithm with pessimistic pruning [35]. Mookerjee and Mannino [20] categorized the cost-based classification systems into two broad categories: (1) cost minimization and (2) value maximization classification systems. In cost minimization classification systems, the objective was to minimize the misclassification costs while holding the decision quality constant. In value maximizationbased classification systems both decision quality and cost were allowed to change. Mookerjee and Mannino [20] argued that value maximization classification systems were less common because the value of correct and incorrect decisions was hard to estimate and it may be unacceptable to change an expert’s decision.

Research on cost minimization classification systems has focused mainly on incorporating misclassification cost matrices in inductive/decision tree-based classification systems. Several researchers [7,12,33] proposed different decision tree learning and pruning approaches that consider misclassification costs. Turney [40] proposed a hybrid genetic algorithmbased decision tree induction algorithm called Inexpensive Classification with Expensive Test (ICET) that minimized misclassification and clinical test costs. Domingos [6] used ensembles of C 4.5 classifiers and Breiman’s Bagging approach to estimate class probabilities of the training instances. Based on the class probability estimates and the loss function, the training data were relabeled and a single model was retrained on the training data. According to Domingos [6], MetaCost produced large cost reductions when compared to cost-insensitive C4.5 and two other stratification approaches.

Several other studies have focused on minimizing information acquisition costs for case retrieval and sequential expert systems [20,21]. In one study, Mookerjee and Mannino [21] developed two algorithms called case retrieval loss criterion $\mathrm { ( C R _ { \mathrm { l c } } ) }$ and cost-based variant ID3 (ID3<sub>c</sub>) that attempted to minimize information acquisition costs in case retrieval. The authors reported that both $\mathrm { C R _ { \mathrm { l c } } }$ and $\mathrm { I D } 3 _ { \mathrm { c } }$ significantly reduced information acquisition costs. In another study, Mannino and Mookerjee [16] developed heuristics and embedded the heuristic into an informed $A O ^ { * }$ search algorithm to design sequential expert systems that lowered the search effort and minimized the expected cost to operate the system.

Mookerjee and Mannino [19] studied mean-risk tradeoffs of inductive classification systems. According to the authors, the mean-risk tradeoffs are significant when there are asymmetries in misclassification costs and information acquisition costs. The authors developed a combined mean-risk measure and incorporated it into the risk-based induction algorithm. Simulation results reported in the study suggest that mean-based and risk-based algorithms show a significant performance difference.

Several other researchers have used cost-based metrics in classification systems. Mannino and Koushik [15] examined the inverse classification problem to identify cost minimization changes to different independent variables so that a case can be classified into a different preferred class. Park [28] incorporated Type I and Type II error cost estimates in a binary classification and regression tree (CART) approach to find a total cost minimizing classification system. Murphy and Benaroch [25] used classification cost for selecting attributes in a rulebased induction system. Nunez [27] used cost minimization and value maximization approaches for inductive expert systems. Zubek and Dietterich [44] illustrate how pruning can facilitate cost sensitive heuristic search. Nanda and Pendharkar [26] incorporated Type I and Type II error costs in genetic algorithm-based linear classifier.

Turney [40] classifies misclassification error and information acquisition costs into two categories—the constant cost category and the conditional cost category. Constant cost is a fixed parameter and does not depend on the circumstances. Conditional cost is dependent on the circumstances specific to a case. For example, the cost of a certain mistake in medical diagnosis may be different for different type of medical patients [40]. In our research, we focus on constant information acquisition costs.

While classification tree approaches, such as ID3, C4.5 and CART have been used for cost-sensitive classification, it is important to note the limitation of these approaches. First, classification tree approaches are suitable for sequential decision-making environment where not all information is available at the same time. In a non-sequential decision-making environment, classification tree approaches attempt to solve the problem in a sequential manner by developing a decision tree using one attribute at a time [35]. Further, all classification tree approaches implement some type of greedy local search algorithm which may be prone to overfitting the training data and eluding global optimum [3,35]. When CIACC is used in a non-sequential decision-making environment the problem has factorial complexity. Thus, a heuristic global search approach is preferable to a sequential local search approach. The approaches proposed in this research are suitable CIACC for non-sequential decision-making problems with constant information acquisition costs.

## 4. Hybrid heuristic algorithms for solving CIACC problem

The CIACC problem is an NP-hard problem. Complete and exact methods for solving the NPhard problem have a factorial time complexity, and solving time for these methods may become prohibitory for large size problems [9]. For solving NP-hard problems in practice, global search algorithms such as simulated annealing, tabu search and genetic algorithms are used [9]. Global search algorithms can be categorized into memory-based global search algorithms, and memory-less probabilistic algorithms. Tabu search is a memory-based algorithm that <sup>b</sup>remembers<sup>Q</sup> non-promising solutions visited in past. Simulated annealing and genetic algorithm are probabilistic memory-less global search algorithms that do not keep a memory of non-promising solutions visited in past. Due to the probabilistic nature of memory-less global search algorithms and the memory dependence of memorybased global search algorithm, global search algorithms do not guarantee the optimal solution. However, global search algorithms do not require factorial time complexity to solve large size NPhard problems and provide heuristic solutions in polynomial time.

The SA algorithm for optimization was first proposed by Kirkpatrick et al. [11]. In the SA algorithm, a random point is first selected and, beginning with this point in search space, a random move is made in the neighborhood of the initial point. If the move introduces a better point (positive move), it is accepted. If the move introduces a worse point (negative move), it is accepted with a decreasing probability over time. The SA algorithm avoids the local optimum by allowing a negative move from a potentially feasible solution (a) to an inferior solution (b) in its neighborhood with the following probability:

$$
P (a \rightarrow b) = \text { Minimum } \left\{1, e ^ {\left(- \frac {\Delta f}{t _ {i}}\right)} \right\}
$$

where $t _ { i }$ is the temperature, and $\Delta f$ (for maximization problems with objective function f()) is defined as follows:

$$
\Delta f = f (a) - f (b).
$$

Temperature $t _ { i }$ is gradually reduced from a large initial value to zero based on the annealing schedule. Typically, an SA algorithm stops when a fixed number of non-improving iterations is realized or when a limit of iterations is reached. If n is the number of variables and $q$ is the collection of value domains associated with the variables n then the worst case time complexity of SA algorithm is $O ( | n | ^ { * } | q | )$ [9].

For solving CIACC problem using SA, we first define our neighborhood function as:

$$
N (k) = \{Y \in \{0, 1 \} ^ {n}: \operatorname{norm} (K, Y) = 1 \}.
$$

In other words, the neighborhood of K consists of all binary n-tuples in which exactly one entry of K has been changed. The neighborhood $Y { = } [ y _ { 1 } , . . . . , y _ { n } ] { \in }$ $N ( K )$ can be obtained by generating a random integer j such that 1VjVn, and then defining

$$
y _ {j} = \left\{ \begin{array}{l l} k _ {i} & \text { if } i \neq j \\ 1 - k _ {i} & \text { if } i = j. \end{array} \right.
$$

The current cost of clinical tests can be obtained as follows:

$$
\operatorname{CurCost} (Y) = \left\{ \begin{array}{l l} \operatorname{CurCost} (K) + c _ {j} & \text { if } k _ {j} = 0 \\ \operatorname{CurCost} (K) - c _ {j} & \text { if } k _ {j} = 1. \end{array} \right.
$$

The values of f( Y) and f(K) are obtained by using a neural network classifier that uses the back-propagation algorithm. We call these values as Neural( Y) and Neural(K) for ease of understanding. The number of inputs in the neural networks is sum of non-zero values of Y and K plus one threshold (bias) input. The number of hidden nodes in the neural network is always equal to twice the size of inputs and one threshold (bias) node.

It can be shown that if K is feasible then Y is feasible whenever $k _ { j } { = } 1 . \operatorname { I f } k _ { i } { = } 0$ and $\operatorname { C u r C o s t } ( K ) { = } c _ { j } { \leq } { \eta }$ , then Y is feasible; else, it is not feasible and the heuristic fails. Assuming that $Y { = } h _ { \mathrm { N } } ( K )$ (where $h _ { \mathrm { N } }$ represents the neighborhood heuristic) is feasible and Neural ( Y)<sup>N</sup>Neural(K), K will be replaced by Y in an SA algorithm. If Neural( Y)<sup>b</sup>Neural(K), then K will be replaced by Y with probability of e<sup>(neural(Y)Neural(K))/T</sup>. It is sufficient to begin with the trivial feasible solution $[ 0 , 0 , . . . , 0 ]$ and then use the SA algorithm to evolve the best heuristic solution. The values $T _ { 0 } , z _ { \mathrm { m a x } } ,$ , and a are the initial temperature, maximum iterations and step values, respectively. These values are user defined and are constant. Fig. 1 illustrates the hybrid simulated annealing-artificial neural network (SA-ANN) procedure for solving CIACC problem. The Neural()

```txt
z←0
T←T₀
K←[kₚ…,kₙ]=[0,…,0]
CurCost←0
K_Best←K
while z≤z_max

do
    let j←Rand(l,n) // a random integer between l and n
    Y←K
    yj←1-xj
    if (yj=1) and (CurCost+cj>η)
    then Y←Fail
    if Y≠Fail

    then
    if (Neural(Y)≥Neural(K) and yj=1)
    then[K←Y
    CurCost←CurCost+cj
    if Neural(K)>Neural(K_best)
    then K_Best←K
    elseif (Neural(Y)<Neural(K) and yj=1)
    then[r←Random(0,1)
    if r<e(Neural(Y)-Neural(K))/T
    then[K←Y
    CurCost←CurCost+cj
    elseif (Neural(Y)≥Neural(K) and yj=0)
    then[K←Y
    CurCost←CurCost-cj
    if Neural(K)>Neural(K_best)
    then K_Best←K
    else[r←Random(0,1)
    if r<e(Neural(Y)-Neural(K))/T
    K←Y
    CurCost←CurCost-cj
    return (K_best)

    z←z+1
    T←αT
    return (K_best)
```  
Fig. 1. The SA-ANN procedure for solving knapsack classification problem.

procedure in Fig. 1 invokes a back-propagation neural network algorithm that uses the inputs from the feasible solution and the data related to the inputs to learn connection weights for a neural network classifier. Suppose we have N learning examples with each example having n inputs and l outputs.

The feasible solution has an impact on the number of inputs n. In particular, n is equal to sum of all $k _ { i }$ for all $i { = } \{ I , { \bf { \Gamma } } , { \bf { \Gamma } } { \bf { \Omega } } \quad { \bf { \Omega } } \quad$ . We use a three-layer neural network with number of hidden nodes always equal to twice the number of inputs. The input vector can be described as $S _ { j } { = } ( S _ { 1 j } , . . . , S _ { n j } )$ and, the output vector can be described as $A _ { j } = ( A _ { 1 j } , . . . , A _ { l j } ) , 1 { \leq } j { \leq } N .$ Learning using back-propagation algorithm takes place using the following two steps.

(1) Forward propagation: The input $S _ { j }$ is fed into the input layer and an output $\pmb { O } _ { j } { = } ( O _ { 1 j } , . . . , O _ { l j } )$ is generated on the basis of the current weights ${ \cal { W } } { = } ( W _ { 1 I } ,$ $\ldots , W _ { n l } )$ . The value of $\mathbf { \delta } _ { O _ { j } }$ is compared with the actual output $A _ { j }$ and output differences are summed to generate an error function E defined as:

$$
E = \frac {1}{2} \sum_ {l = 1} ^ {l} \sum_ {j = 1} ^ {N} (A _ {l j} - O _ {l j}) ^ {2}.\tag{4.1}
$$

(2) Error back propagation: In this step, the error from Eq. (4.1) is back propagated by performing weight updates using gradient descent as follows:

$$
\Delta W _ {n l} = - \frac {\partial E}{\partial W _ {n l}} \eta ,\tag{4.2}
$$

where 0<sup>b</sup>g<sup>b</sup>1 is a parameter controlling the convergence rate of the algorithm.

The process of forward propagation and error backpropagation continues until E converges. W can be updated in two different ways. The first approach, also called online updating, is to update W for each $( S _ { j } ,$ $A _ { j } )$ pair. In the second approach, also called batch updating, $\Delta W _ { n l }$ are accumulated and updated after a complete run of all the N examples. In unimodal functions, the optimal can be found by moving along the local gradients given by Eq. (4.2). We use batch updating for our research.

Tabu search (TS) approach is different from SA algorithm in that it implements memory-based search for solving CIACC problem. Unlike SA algorithm where previously visited solutions are not kept in memory, TS algorithm maintains explicit memory of solutions visited in the past. We implement a na<sup>R</sup>ve TS procedure where the explicit short-term memory of the solutions visited in the past is stored in Tabu List. Solutions that are in the Tabu List are not considered for some specified time (iterations) L, which is called Tabu Tenure. Fig. 2 illustrates the hybrid-na<sup>R</sup>ve TS-ANN search procedure that we use for solving CIACC problem. The neighborhood function used for TS is same as that of SA procedure.

We use two different heuristics for our TS approach. The first heuristic is called the greedy heuristic and the second heuristic is called ratio heuristic. The greedy heuristic (GH) $h _ { \mathrm { N } } ( K )$ is defined as,

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$h_{\mathrm{N}}(K) = Y$ , where $\left\{ \begin{array}{ll}Y\in N(K),\\ Y\text{is feasible,}\\ \mathrm{change}(X,Y)\notin \{\mathrm{TabuList}[d]:\\ c - L\leq d\leq c - 1\} ,\\ \text{and Neural (Y) is maximum}\\ \text{among all such}\\ \text{feasible solutions.} \end{array} \right.$
</div>

The variable c is the iteration number at which the change i was forbidden. The change (X,Y) is defined as follows,

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
change(X, Y) = i ⇔  $x_{i} \neq y_{i}$ .
</div>

The norm(X,Y)=1. Fig. 3 illustrates the procedure that was implemented for the greedy heuristic.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure TabuSearch (int $z_{max}$, int L)
external Neural ()
external Heuristic ()
z←l
Select a random feasible solution K=[k0, ..., k_{n-l}]∈{0,l}^n
CurCost←Σc_i k_i
OptCorrect←0
K_Best←K
while z≤Z_max
    if (Heuristic (z,L) ≠ Fail)
    then [if (Neural (K) &gt; Neural (K_best))
    then [K_Best←K
    OptCorrect←Neural (K_best)
    z ←z+l
    return (K_best))
</div>

Fig. 2. The TS-ANN Procedure.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure Greedy Heuristic (int z, int L)

$N \leftarrow \{0, \ldots, n\}$ $start \leftarrow \max \{0, z-L\}$
for $j \leftarrow$ start to $z-1$

do
    $N \leftarrow N \setminus \{TabuList[j]\}$
    for each $i \in N$
    do
    if ($x_i=1$)
    then
    $x_i \leftarrow 0$
    Correct$_i$ ← Neural (K)
    $x_i \leftarrow 1$
    else if ($x_i=0$ and CurCost+$c_i \leq \eta$)
    then
    $x_i \leftarrow 1$
    Correct$_i$ ← Neural (K)
    $x_i \leftarrow 0$ $j \leftarrow j+1$

    if ($j=0$) then FAIL
    OptCorrect ← Neural (K)
    index ← 0
    for each $i \in N$
    do
    if (Correct$_i$ &gt;OptCorrect)
    then
    $OptCorrect \leftarrow Correct_i$
    index ← i
    TabuList[z] ← index
    K[index] ← l-K[index]
    end
</div>

Fig. 3. The greedy heuristic procedure used in TS-ANN.

The ratio heuristic (RH) is similar to greedy-heuristic except that instead of selecting a move such that correct classification is maximized, ratio heuristic selects a move such that the ratio of correct classification divided by the information acquisition cost is maximized. Fig. 4 illustrates the pseudo-code for the ratio heuristic.

## 5. Experiments with simulated and real-world data

We test our proposed approaches for solving the CIACC problem. In order to test the performance and improve the internal validity of our experiments, we use both simulated and real-world data.

## 5.1. Simulated data

There are several studies in the literature that report the sensitivity of machine learning approaches to different data distributions [1,31,30,29]. The use of simulated data allows a researcher to test the robustness and performance of different classification approaches across different data distributions. In order to test the robustness of proposed hybrid approaches across different data distributions, we use simulated data for our experiments. Using the methodology described in Vale and Maurelli [42], we generated 20 random data samples for each of three different data distributions. The three data distributions that were considered for this research were exponential distribution, uniform distribution and normal distribution.

Procedure Ratio Heuristic (int z, int L)  
![](/api/attachments/UWHCKS3J/fulltext/images/863c5768b3cef412624064a505801ffbc15cf30c2977326727dae858b2bd5d3e.jpg)  
Fig. 4. The ratio heuristic procedure used in TS-ANN.

Each data sample consisted of 300 examples of 10 independent attributes (x<sub>1</sub>, x<sub>2</sub>, . . ., x<sub>10</sub>) equally split between two groups. The mean for group 1 was approximately set equal to zero, and the mean of group 2 was approximately set equal to 0.5. The standard deviation for all the attributes was approximately set equal to one, and skewness was set equal to zero. Tables 1–3 illustrate the actual means and standard deviations of generated data, for each of three distributions, averaged across 3000 examples.

The information acquisition costs were generated randomly for each attribute. We used a normal distribution with a mean of 10 and standard deviation of 5. Table 4 illustrates the random cost that was generated for each attribute. The actual mean and standard deviation of generated data was 10.84 and 4.81, respectively. The maximum allowable information acquisition cost was set equal to 70 (cost constraint).

Table 1  
Descriptive statistics for simulated data with exponential distribution

<table><tr><td rowspan="2">Variable</td><td colspan="3">Group 1</td><td colspan="3">Group 2</td></tr><tr><td>Mean (S.D.)</td><td>Minimum</td><td>Maximum</td><td>Mean (S.D.)</td><td>Minimum</td><td>Maximum</td></tr><tr><td> $x_{1}$ </td><td>0.01(1.02)</td><td>-0.99</td><td>9.22</td><td>0.50(1.00)</td><td>-0.49</td><td>10.14</td></tr><tr><td> $x_{2}$ </td><td>0.03(0.99)</td><td>-0.99</td><td>5.68</td><td>0.50(0.99)</td><td>-0.49</td><td>8.56</td></tr><tr><td> $x_{3}$ </td><td>0.00(1.02)</td><td>-0.99</td><td>8.50</td><td>0.52(1.03)</td><td>-0.49</td><td>7.87</td></tr><tr><td> $x_{4}$ </td><td>-0.01(0.96)</td><td>-0.99</td><td>6.20</td><td>0.46(1.00)</td><td>-0.49</td><td>10.83</td></tr><tr><td> $x_{5}$ </td><td>0.00(0.98)</td><td>-0.99</td><td>8.02</td><td>0.49(0.99)</td><td>-0.49</td><td>8.28</td></tr><tr><td> $x_{6}$ </td><td>-0.01(0.99)</td><td>-0.99</td><td>12.12</td><td>0.48(0.99)</td><td>-0.49</td><td>6.68</td></tr><tr><td> $x_{7}$ </td><td>-0.02(0.97)</td><td>-0.99</td><td>8.69</td><td>0.49(0.97)</td><td>-0.49</td><td>7.97</td></tr><tr><td> $x_{8}$ </td><td>0.01(0.98)</td><td>-0.99</td><td>8.00</td><td>0.50(1.02)</td><td>-0.49</td><td>9.26</td></tr><tr><td> $x_{9}$ </td><td>-0.01(0.95)</td><td>-0.99</td><td>7.11</td><td>0.51(1.03)</td><td>-0.49</td><td>8.57</td></tr><tr><td> $x_{10}$ </td><td>0.01(1.01)</td><td>-0.99</td><td>8.26</td><td>0.47(0.96)</td><td>-0.49</td><td>8.75</td></tr></table>

Table 2  
Descriptive statistics for simulated data with uniform distribution

<table><tr><td rowspan="2">Variable</td><td colspan="3">Group 1</td><td colspan="3">Group 2</td></tr><tr><td>Mean (S.D.)</td><td>Minimum</td><td>Maximum</td><td>Mean (S.D.)</td><td>Minimum</td><td>Maximum</td></tr><tr><td> $x_{1}$ </td><td>-0.02(1.01)</td><td>-1.75</td><td>1.75</td><td>0.49(1.00)</td><td>-1.25</td><td>2.25</td></tr><tr><td> $x_{2}$ </td><td>-0.02(1.01)</td><td>-1.75</td><td>1.75</td><td>0.51(1.00)</td><td>-1.25</td><td>2.25</td></tr><tr><td> $x_{3}$ </td><td>-0.01(1.01)</td><td>-1.75</td><td>1.75</td><td>0.46(1.02)</td><td>-1.25</td><td>2.25</td></tr><tr><td> $x_{4}$ </td><td>0.01(1.01)</td><td>-1.75</td><td>1.75</td><td>0.50(0.99)</td><td>-1.25</td><td>2.25</td></tr><tr><td> $x_{5}$ </td><td>0.02(1.00)</td><td>-1.75</td><td>1.75</td><td>0.53(1.01)</td><td>-1.25</td><td>2.25</td></tr><tr><td> $x_{6}$ </td><td>-0.01(1.00)</td><td>-1.75</td><td>1.75</td><td>0.47(1.01)</td><td>-1.25</td><td>2.25</td></tr><tr><td> $x_{7}$ </td><td>0.02(1.01)</td><td>-1.75</td><td>1.75</td><td>0.49(1.01)</td><td>-1.25</td><td>2.25</td></tr><tr><td> $x_{8}$ </td><td>0.02(1.01)</td><td>-1.75</td><td>1.75</td><td>0.50(1.00)</td><td>-1.25</td><td>2.25</td></tr><tr><td> $x_{9}$ </td><td>0.02(1.00)</td><td>-1.75</td><td>1.75</td><td>0.51(1.01)</td><td>-1.25</td><td>2.25</td></tr><tr><td> $x_{10}$ </td><td>0.00(1.00)</td><td>-1.75</td><td>1.75</td><td>0.49(1.02)</td><td>-1.25</td><td>2.25</td></tr></table>

Table 3  
Descriptive statistics for simulated data with normal distribution

<table><tr><td rowspan="2">Variable</td><td colspan="3">Group 1</td><td colspan="3">Group 2</td></tr><tr><td>Mean (S.D.)</td><td>Minimum</td><td>Maximum</td><td>Mean (S.D.)</td><td>Minimum</td><td>Maximum</td></tr><tr><td> $x_{1}$ </td><td>-0.00(1.01)</td><td>-3.82</td><td>3.61</td><td>0.50(0.99)</td><td>-2.62</td><td>3.99</td></tr><tr><td> $x_{2}$ </td><td>-0.01(0.98)</td><td>-3.44</td><td>3.32</td><td>0.51(1.00)</td><td>-2.98</td><td>4.49</td></tr><tr><td> $x_{3}$ </td><td>0.00(1.02)</td><td>-3.65</td><td>3.68</td><td>0.51(1.00)</td><td>-2.80</td><td>4.74</td></tr><tr><td> $x_{4}$ </td><td>0.01(0.99)</td><td>-3.36</td><td>3.94</td><td>0.49(1.00)</td><td>-2.98</td><td>4.27</td></tr><tr><td> $x_{5}$ </td><td>-0.01(0.99)</td><td>-3.14</td><td>3.99</td><td>0.50(0.99)</td><td>-2.91</td><td>3.75</td></tr><tr><td> $x_{6}$ </td><td>-0.00(1.00)</td><td>-3.65</td><td>3.23</td><td>0.50(1.01)</td><td>-3.59</td><td>4.20</td></tr><tr><td> $x_{7}$ </td><td>0.00(1.01)</td><td>-3.36</td><td>3.39</td><td>0.51(0.99)</td><td>-3.18</td><td>3.65</td></tr><tr><td> $x_{8}$ </td><td>0.00(0.98)</td><td>-3.66</td><td>3.63</td><td>0.49(1.00)</td><td>-3.21</td><td>3.95</td></tr><tr><td> $x_{9}$ </td><td>0.00(1.00)</td><td>-3.45</td><td>3.68</td><td>0.48(0.99)</td><td>-2.90</td><td>4.29</td></tr><tr><td> $x_{10}$ </td><td>0.00(1.03)</td><td>-3.33</td><td>4.48</td><td>0.49(0.99)</td><td>-3.01</td><td>3.66</td></tr></table>

After initial experimentation, we set the values of the different parameters for SA and ANN as: $T _ { 0 } \mathrm { = } 1 0 0 0 , ~ z _ { \mathrm { m a x } } \mathrm { = } 1 0 , ~ \mathrm { \it { \alpha } x = } 0 . 9 9 9$ , learning rate for ANN=0.1 and number of iterations (stopping criteria) for ANN=1000. For TS, the following parameters were used after initial experimentation: $z _ { \mathrm { m a x } } { = } 1 0 0 0$ and L=3. Tables 5 and 6 illustrate the descriptive and pairwise difference in means t-statistics for correct classification and information acquisition cost. The means and standard deviations are averaged across 20 experiments. The bold font entries in the table indicate that the technique listed in the row has a higher mean that the technique listed in the column, and the difference of means between the two techniques is statistically significant. The abbreviations GH and RH stand for greedy heuristic and ratio-heuristic for hybrid tabu search algorithm.

The results indicate that generally the performance, in terms of correct classification, is higher for nonparametric distributions (uniform and exponential). Also, probabilistic hybrid SA algorithm performs equal or worse than memory-based hybrid tabu search algorithms. Table 6 illustrates that memory-based GH and RH algorithms have non-significant difference in means (at 0.01 level of significance) as far as information acquisition cost is concerned. The results also indicate that the difference in means between probabilistic SA algorithm and memory-based tabu search (GH and RH), for correct classification, is significant. Memory-based tabu search algorithm tend to have higher information costs; although the cost is always less than or equal to the information acquisition cost constraint.

## 5.2. Real-world data

The real-world data for our experiments comes from health care industry. The health care industry has been changing continuously for last three decades [13]. Among the drivers for the change are:

(1) pressure from the general public to provide customized, high-quality care at lowest possible cost,

(2) pressure from the regulatory bodies, such as Joint Commission of Accreditation of Healthcare Organizations (JCAHO), to employ quality management techniques to obtain accreditation status [43], and

(3) pressure from federal Medicare/Medicaid administrators to minimize cost without sacrificing quality and efficiency of service.

The Medicare Act of the Reagan administration, and the prospective payment system (PPS) set forth in this act, required the classification of each patient into one of the 468 diagnosis related groups (DRGs) [14].

Table 4  
The simulated information acquisition costs for variables

<table><tr><td colspan="10">Information acquisition costs</td></tr><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td><td> $x_{6}$ </td><td> $x_{7}$ </td><td> $x_{8}$ </td><td> $x_{9}$ </td><td> $x_{10}$ </td></tr><tr><td>12.11</td><td>12.45</td><td>10.51</td><td>12.70</td><td>4.69</td><td>19.33</td><td>16.60</td><td>7.98</td><td>7.20</td><td>4.83</td></tr></table>

Table 5  
Results for correct classification for simulated data

<table><tr><td></td><td>SA (Normal)</td><td>GH (Normal)</td><td>RH (Normal)</td><td>SA (Uni.)</td><td>GH (Uni.)</td><td>RH (Uni.)</td><td>SA (Exp.)</td><td>GH (Exp.)</td><td>Mean</td><td>Std. dev.</td></tr><tr><td>SA (Normal)</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>225.15</td><td>5.07</td></tr><tr><td>GH (Normal)</td><td>5.66*</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td>230.55</td><td>4.77</td></tr><tr><td>RH (Normal)</td><td>3.94*</td><td>2.49**</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td>228.90</td><td>3.96</td></tr><tr><td>SA (Uni.)</td><td>1.13</td><td>0.21</td><td>0.21</td><td>0.00</td><td></td><td></td><td></td><td></td><td>229.70</td><td>16.63</td></tr><tr><td>GH(Uni.)</td><td>2.02**</td><td>0.30</td><td>1.01</td><td>1.11</td><td>0.00</td><td></td><td></td><td></td><td>232.20</td><td>15.48</td></tr><tr><td>RH(Uni.)</td><td>2.03**</td><td>0.35</td><td>0.89</td><td>0.91</td><td>0.93</td><td>0.00</td><td></td><td></td><td>231.60</td><td>15.22</td></tr><tr><td>SA (Exp.)</td><td>11.93*</td><td>7.82*</td><td>9.67*</td><td>3.31*</td><td>3.06*</td><td>3.51*</td><td>0.00</td><td></td><td>242.35</td><td>5.11</td></tr><tr><td>GH (Exp.)</td><td>15.23*</td><td>12.61*</td><td>16.09*</td><td>5.28*</td><td>5.01*</td><td>5.61*</td><td>5.12*</td><td>0.00</td><td>247.65</td><td>4.09</td></tr><tr><td>RH (Exp.)</td><td>15.64*</td><td>12.40*</td><td>18.86*</td><td>4.85*</td><td>4.60*</td><td>5.25*</td><td>4.09*</td><td>1.39</td><td>246.55</td><td>3.79</td></tr></table>

A t-test was employed to test the significance of difference of means.  
\*\* p<sup>b</sup>0.05.

Under the PPS mechanism, the major private carriers paid fixed fees based on the DRG classification [24].

Chilingerian and Sherman’s [4] study on benchmarking physician practice patterns notes the following:

(1) Physicians control 80% of the health care cost where changes in their practice can have substantial cost impact.

(2) There are a number of effective ways to treat similar patients, some of which may be less costly than the others.

(3) If efficient practice patterns are identified and adopted by physicians then the savings in health care costs are potentially substantial.

Kumar and Motwani [13] and Pendharkar et al. [32] argue that the knowledge-based expert systems (ES) and decision support systems (DSS) that assist physicians in diagnosis and treatment of patients play a vital role in medicine.

We believe that CIACC can be used for medical diagnosis for the following reasons:

(1) The variable g may be determined by the decision-maker in light of the prescribed fixed fees of a given DRG classification.

(2) The function f(x) may be determined by the decision-maker in light of the quality care objectives of the health care facility (maximize correct predictions, minimize misclassification costs or both).

The CIACC problem allows the decision-maker to incorporate the information acquisition cost constraint.

We apply the proposed hybrid SA and TS procedures to a real-world data set for prediction of the heart disease. The heart disease data set has been used in previous studies [10] and is publicly available. The data comes from the Cleveland Clinic Foundation, and it is available from the machine learning data repository at the University of California, Irvine. The data set used in this research consists of 270 total usable examples, with two group (presence and absence of heart disease) covariances being equal. The kurtosis value for this non-parametric data set is 3.6. There are 13 attributes, with eight attributes taking numerical continuous values and 5 taking categorical values. The list of 13 different values, their descriptions, and information acquisition costs (obtained from Turney [41]) are listed in Table 7.

Table 6  
Results for information acquisition cost for simulated data

<table><tr><td></td><td>SA (Normal)</td><td>GH (Normal)</td><td>RH (Normal)</td><td>SA (Uni.)</td><td>GH (Uni.)</td><td>RH (Uni.)</td><td>SA (Exp.)</td><td>GH (Exp.)</td><td>Mean</td><td>Std. dev.</td></tr><tr><td>SA (Normal)</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>59.79</td><td>7.51</td></tr><tr><td>GH (Normal)</td><td>2.82**</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td>65.04</td><td>4.01</td></tr><tr><td>RH (Normal)</td><td>2.43**</td><td>0.43</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td>64.51</td><td>4.31</td></tr><tr><td>SA (Uni.)</td><td>0.09</td><td>2.53**</td><td>1.94</td><td>0.00</td><td></td><td></td><td></td><td></td><td>59.58</td><td>9.05</td></tr><tr><td>GH (Uni.)</td><td>2.98**</td><td>0.11</td><td>0.54</td><td>3.30*</td><td>0.00</td><td></td><td></td><td></td><td>65.19</td><td>4.57</td></tr><tr><td>RH (Uni.)</td><td>1.12</td><td>2.01</td><td>1.58</td><td>1.56</td><td>2.65**</td><td>0.00</td><td></td><td></td><td>62.15</td><td>5.17</td></tr><tr><td>SA (Exp.)</td><td>0.62</td><td>3.06*</td><td>3.14*</td><td>0.49</td><td>3.97*</td><td>1.85</td><td>0.00</td><td></td><td>58.31</td><td>8.23</td></tr><tr><td>GH (Exp.)</td><td>2.07</td><td>0.30</td><td>0.03</td><td>2.02</td><td>0.44</td><td>1.45</td><td>3.13*</td><td>0.00</td><td>64.54</td><td>5.17</td></tr><tr><td>RH (Exp.)</td><td>1.41</td><td>1.93</td><td>1.85</td><td>1.07</td><td>2.03</td><td>0.04</td><td>1.73</td><td>1.61</td><td>62.23</td><td>4.93</td></tr></table>

A t-test was employed to test the significance of difference of means.  
\* Represents p<sup>b</sup>0.01.  
\*\* Represents p<sup>b</sup>0.05.

The total cost of using all the attributes is \$ 600.57. We create ten 200-example data sets from the original set of 270 examples. Although the ten 200-example data sets contain a lot of overlapping examples, no two data sets contained exactly the same cases. We arbitrarily set the value of g=\$300.29 (50% of total cost of all the attributes) for our experiments. We use the hybrid SA-ANN and the TS-ANN procedures to solve the CIACC problem for the 10 data sets. The values for different parameters for the algorithms were kept same as the values used in simulation experiments. Tables 8 and 9 illustrate the results of our experiments using the SA-ANN and TS-ANN procedures, respectively.

Table 7  
The description of the heart disease prediction attributes and their costs

<table><tr><td>Attribute number</td><td>Name</td><td>Description</td><td>Cost ($)</td></tr><tr><td>1</td><td>Age</td><td>Age in years</td><td>1.00</td></tr><tr><td>2</td><td>Sex</td><td>Patient&#x27;s gender</td><td>1.00</td></tr><tr><td>3</td><td>Cp</td><td>Chest pain type</td><td>1.00</td></tr><tr><td>4</td><td>Trestbps</td><td>Resting blood pressure</td><td>1.00</td></tr><tr><td>5</td><td>Chol</td><td>Serum cholesterol</td><td>7.27</td></tr><tr><td>6</td><td>Fbs</td><td>Fasting blood sugar</td><td>5.20</td></tr><tr><td>7</td><td>Restecg</td><td>Resting electrocardiograph</td><td>15.50</td></tr><tr><td>8</td><td>Thalach</td><td>Maximum heart rate achieved</td><td>102.90</td></tr><tr><td>9</td><td>Exang</td><td>Exercise induced angina</td><td>87.30</td></tr><tr><td>10</td><td>Oldpeak</td><td>ST depression induced by exercise relative to rest</td><td>87.30</td></tr><tr><td>11</td><td>Slope</td><td>Slope of peak exercise ST segment</td><td>87.30</td></tr><tr><td>12</td><td>Ca</td><td>Number of major vessels colored by fluoroscopy</td><td>100.90</td></tr><tr><td>13</td><td>Thal</td><td>3=normal; 6=fixed defect; 7=reversible defect</td><td>102.90</td></tr></table>

Table 8  
Pairwise comparisons for differences of means for three experiments (correct classification)

<table><tr><td>Comparison</td><td>SA mean (S.D.)</td><td>TS-GH mean (S.D.)</td><td>TS-RH mean (S.D.)</td><td>Two-tailed t-value</td><td>P</td></tr><tr><td>SA vs. TS-GH</td><td>126 (14.04)</td><td>127.5 (11.29)</td><td></td><td>-0.3011</td><td>0.7701</td></tr><tr><td>SA vs. TS-RH</td><td>126 (14.04)</td><td></td><td>129.8 (12.72)</td><td>-0.8337</td><td>0.4260</td></tr><tr><td>TS-GH vs. TS-RH</td><td></td><td>127.5 (11.29)</td><td>129.8 (12.72)</td><td>-1.3227</td><td>0.2185</td></tr></table>

\*p<sup>b</sup>0.01, \*\*p<sup>b</sup>0.05.

For correct classification, no difference of means was observed for any of the three techniques. For information acquisition cost, the mean of information acquisition cost for hybrid SA algorithm was lower than the means for hybrid TS approaches.

The hybrid SA is a probabilistic approach in which the probability to move away from local optimum decreases with time. Thus, the hybrid SA approach attempts to find higher quality solution early in its annealing schedule. The hybrid TS approach avoids the poor quality solutions stored in its memory and improves the probability to finding high quality solutions. Thus, the performance of hybrid TS approaches is likely to improve with increase in the value of tabu-tenure (memory). Increasing the value of tabu-tenure, while increasing the performance of the quality of the final solution, leads to longer run times for the hybrid TS approaches. Higher values of tabu-tenure lead to higher number of comparisons between a potential solution, and the existing poor quality solutions in the tabu-memory. In our experiments, we determined initial value for the hybrid SA and the hybrid TS algorithm so that the run times for both algorithms are somewhat similar. A decisionmaker, based on his/her resources, may choose different values for the TS and the SA algorithms and may obtain slightly different results.

Table 9  
Pairwise comparisons for differences of means for three experiments (cost)

<table><tr><td>Comparison</td><td>SA mean (S.D.)</td><td>TS-GH mean (SD)</td><td>TS-RH mean (S.D.)</td><td>Two-tailed t-value</td><td>P</td></tr><tr><td>SA vs. TS-GH</td><td>184.98 (76.27)</td><td>293.84 (5.36)</td><td></td><td>-4.5382</td><td>0.001*</td></tr><tr><td>SA vs. TS-RH</td><td>184.98 (76.27)</td><td></td><td>293.64 (5.73)</td><td>-4.6068</td><td>0.001*</td></tr><tr><td>TS-GH vs. TS-RH</td><td></td><td>293.84 (5.36)</td><td>293.64 (5.73)</td><td>0.1138</td><td>0.911</td></tr></table>

\*\*p<sup>b</sup>0.05.  
\*p<sup>b</sup>0.01.

It is likely that the information acquisition cost constraint may change either over time or for a different decision-maker. In case of a different information acquisition cost, say $\eta ^ { \mathrm { n e w } }$ , it may not be always necessary to develop a separate system. We provide two criteria where it may not be necessary to develop a separate system. First, we assume that S represents a set of input variables contained in the final solution vector for the CIACC problem. Also, assume that NS represents a set of input variables that are not included in the final solution vector for the CIACC problem. Thus, S\NS=f. Assume that Cost(S) represents the total cost of all the variables in set $S ,$ , and Max(NS) is the maximum individual cost of a variable in the set NS. The two criteria are as follows.

Criterion 1. If $\eta ^ { \mathrm { n e w } } { > } \eta$ and $( \eta - \mathrm { C o s t } ( S ) ) { \mathord { \operatorname - } } \mathrm { M a x } ( N S )$ then there is no need to develop a separate system.

The primary reason for proposing this criterion is that when original system was developed, it could have considered at least one additional variable from set NS, if such a variable could have improved the classification accuracy. Given that (gCost(S))<sup>N</sup>Max(NS), the addition of at least any one variable was feasible. Since the original system chose to exclude all the variables in NS, when it could have included at least one additional variable, a new value of constraint $\eta ^ { \mathrm { n e w } }$ may not be very promising.

Criterion 2. If $\eta ^ { \mathrm { n e w } } { < } \eta$ and if Cost(S)Vg<sup>new</sup>, then there is no need to develop a separate system.

Criterion 2 is a trivial result. For any value of $\mathrm { C o s t } ( S ) { \le } \eta ^ { \mathrm { n e w } } { < } \eta$ , the results of the original system are valid and are best in a heuristic sense.

## 6. Summary and possible extensions

We have proposed a problem of CIACC. Three hybrid SA and TS greedy heuristic and ratio heuristic approaches were developed to solve the CIACC problem. Using simulated data and a real-world heart disease data set, we have solved the CIACC problem using the proposed hybrid procedures. The results of our experiments indicate that memory-based TS approaches perform equal or better than memory-less hybrid SA approach.

While most classification systems are evaluated based on the output performance metrics (total classifications), CIACC evaluates the performance of a classification system by evaluating both output performance (total classifications) and economy of inputs. In our paper, we assumed that the management was indifferent to which inputs are selected in decision-making. However, in real-world, management may want to include certain input variables and may be indifferent to inclusion of other input variables. The current approach can be modified so that certain inputs can always be included in the final solution. The mandatory requirement of inclusion of certain variables in the final solution reduces the search space of the possible unique solutions, and improves the probability that the hybrid heuristic TS and SA algorithms may obtain optimal solution to the CIACC problem.

Our objective was to maximize the total number of classifications. In an event where it is desired to minimize misclassification cost, the error function defined in Eq. (4.1) can be changed as follows [38]:

$$
E = \frac {1}{2} \sum_ {l = 1} ^ {l} Z _ {l} \sum_ {j = 1} ^ {N} (A _ {l j} - O _ {l j}) ^ {2}.
$$

where $\begin{array} { r } { Z _ { l } = \sum _ { i = 1 } ^ { l } C _ { i l } \pi _ { l } } \end{array}$ : The term $C _ { i l }$ is the misclassification cost of classifying an example in group $i ,$ when it should be correctly classified in group l. The term $\pi _ { l }$ is the prior probability of group l. For correct classification, misclassification cost can be considered as zero. Future research is needed to evaluate the performance of the proposed hybrid procedures for minimizing misclassification costs.

## References

[1] S. Bhattacharyya, P.C. Pendharkar, Inductive evolutionary and neural techniques for discrimination: a comparative study, Decision Sciences 29 (4) (1998) 871 – 900.

[2] J.I. Brannon, M.F. Gorman, The effects of information costs on search and convergence in experimental markets, Journal of Economic Behavior and Organization 47 (2002) 375–390.

[3] L. Breiman, J.H. Friedman, R.A. Olshen, J. Stone, Classification and regression trees, Wadsworth International Group, Belmont, CA, 1984.

[4] J.A. Chilingerian, S.D. Sherman, Benchmarking physician practice patterns with DEA: a multi-stage approach for cost containment, Annals of Operation Research 67 (1996) 83– 116.

[5] G.R. Dattatreya, V.V.S. Sarma, Bayesian and decision tree approaches for pattern recognition including feature measurement costs, IEEE Transactions on Pattern Analysis and Machine Intelligence 3 (1981) 293 – 298.

[6] P. Domingos, MetaCost: a general method for making classifiers cost-sensitive, Proceedings of the Fifth International Conference on Knowledge Discovery and Data Mining (1999) 155– 164.

[7] B.A. Draper, C.E. Brodley, P.E. Utgoff, Goal-directed classification using linear machine decision trees, IEEE Transactions on Pattern Analysis and Machine Intelligence 16 (9) (1994) 888–893.

[8] D. Gordon, D. Perlis, Explicitly biased generalization computational intelligence, Computational Intelligence 5 (2) (1989) 67 – 81.

[9] J.K. Hao, J. Pannier, Simulated annealing and tabu search for constraint solving, Fifth International Symposium on Artificial Intelligence and Mathematics Fort Lauderdale, Florida, USA, 1998, pp. 1 – 15.

[10] R.D. King, R. Henry, C. Feng, A.A. Sutherland, Comparative study of classification algorithms: statistical, machine learning and neural network machine intelligence, in: K. Furukawa, D. Michie, S. Muggleton (Eds.), Machine Intelligence and Inductive Learning, Clarendon Press, Oxford, 1994.

[11] S. Kirkpatrick, C.D. Gelatt, M.P. Vecchi, Optimization by simulated annealing, Science 220 (4578) (1983) 671 – 679.

[12] U. Knoll, G. Nakhaeizadeh, B. Tausend, Cost-sensitive pruning of decision trees, Proceedings of the Eight European Conference on Machine Learning ECML-94, Springer-Verlag, Berlin, Germany, 1994, pp. 383 – 386.

[13] A. Kumar, J.G. Motwani, Management of health care technology literature (1979–1997): a multidimensional introspection, IEEE Transactions on Engineering Management 46 (3) (1999) 247– 264.

[14] D. Longo, M. Sohn, S. Shortell, The etiology and determinants of hospital closure, Journal of Health Care Finance 22 (3) (1996) 34 – 48.

[15] M.V. Mannino, M.V. Koushik, The cost minimizing inverse classification problem: a genetic algorithm approach, Decision Support Systems 29 (3) (2000) 283– 300.

[16] M.V. Mannino, V.S. Mookerjee, Optimizing expert systems: heuristics for efficiently generating low-cost information acquisition strategies, INFORMS Journal on Computing 3 (1999) 278– 291.

[17] S. Martello, D. Pisinger, P. Toth, Dynamic programming and strong bounds for the 0–1 knapsack problem, Management Science 45 (3) (1999) 414 – 424.

[18] V.S. Mookerjee, B. Dos Santos, Inductive expert system design maximizing system value, Information Systems Research 4 (1993) 111 – 140.

[19] V.S. Mookerjee, M.V. Mannino, Sequential decision models for expert system optimization, IEEE Transactions on Knowledge and Data Engineering 9 (1997) 675 – 687.

[20] V.S. Mookerjee, M.V. Mannino, Redesigning case retrieval to reduce information acquisition costs, Information Systems Research 8 (1997) 51 – 68.

[21] V.S. Mookerjee, M.V. Mannino, Mean-risk tradeoffs in inductive expert systems, Information Systems Research 11 (2) (2000) 137– 158.

[22] J.C. Moore, A.B. Whinston, A model of decision-making with sequential information acquisition—part I, Decision Support Systems 2 (1986) 285 – 307.

[23] J.C. Moore, A.B. Whinston, A model of decision-making with sequential information acquisition—part II, Decision Support Systems 3 (1986) 47– 72.

[24] R.C. Morey, D.A. Dittman, Cost pass-through reimbursement to hospitals and their impacts on operating efficiencies, Annals of Operation Research 67 (1996) 117– 139.

[25] C.K. Murphy, M. Benaroch, Adding value to induced decision trees for time sensitive data, INFORMS Journal of Computing 9 (1997) 385–396.

[26] S. Nanda, P.C. Pendharkar, Development and comparison of analytical techniques for predicting insolvency risk, International Journal of Intelligent Systems in Accounting, Finance & Management 10 (3) (2001) 35 – 56.

[27] M. Nunez, The use of background knowledge in decision tree induction, Machine Learning 6 (1991) 231– 250.

[28] J. Park, Classifier performance vs. data characteristics: binary tree case, Proceedings of 2nd INFORMS Conference of Information Systems and Technology, 1997, pp. 1 – 8.

[29] P.C. Pendharkar, An empirical study of design and testing of hybrid evolutionary–neural approach for classification, Omega: An International Journal of Management Science 29 (4) (2001) 361 – 374.

[30] P.C. Pendharkar, A computational study on the performance of ANNs under changing structural design and data distributions, European Journal of Operational Research 138 (2002) 155– 177.

[31] P.C. Pendharkar, J.A. Rodger, An empirical study of impact of crossover operators on the performance of nonbinary genetic algorithm based neural approaches for classification, Computers & Operations Research 31 (2004) 481– 498.

[32] P.C. Pendharkar, J.A. Rodger, G.J. Yaverbaum, N. Herman, M. Benner, Association, statistical, mathematical, and neural approaches for mining breast cancer patterns, Expert Systems with Applications 17 (1999) 223– 232.

[33] F.J. Provost, Goal-directed inductive learning: trading off accuracy for reduced error cost, AAAI Spring Symposium on Goal-Driven Learning, 1994.

[34] J.R. Quinlan, Induction of decision trees, Machine Learning 1 (1986) 81 – 106.

[35] J.R. Quinlan, C4.5 Programs for Machine Learning, Morgan Kaufmann, San Mateo, CA, 1993.

[36] M. Rothschild, Models of market organization with imperfect information, Journal of Political Economy (1973) 1283 – 1308.

[37] M. Rothschild, Searching for the lowest price when the distribution of prices is unknown, Journal of Political Economy (1974) 689– 711.

[38] K.Y. Tam, M.Y. Kiang, Managerial applications of neural networks: the case of bank failure predictions, Management Science 38 (1992) 926– 947.

[39] M. Tan, CSL: a cost sensitive learning system for sensing and grasping objects, IEEE International Conference on Robotics and Automation Cincinnati, Ohio, 1990, pp. 858 – 863.

[40] P.D. Turney, Cost-sensitive classification: empirical evaluation of a hybrid genetic decision tree induction algorithm, Journal of Artificial Intelligence Research 2 (1995) 369 – 409.

[41] P.D. Turney, Types of cost in inductive concept learning, International Conference on Machine Learning Workshop Notes on Cost-Sensitive Learning, 2000, pp. 15–21.

[42] C.D. Vale, V.A. Maurelli, Simulating multivariate non-normal distributions, Psychometrika 48 (1983) 465– 471.

[43] S. Woolhandler, D.U. Himmelstein, The deteriorating administrative efficiency of the U.S. health care system, New England Journal of Medicine 324 (1993) 1253– 1258.

[44] V.B. Zubek, T.G. Dietterich, Pruning improves heuristic search for cost-sensitive learning, Proceedings of the 2002 International Conference on Machine Learning, 2002, pp. 27– 34.

![](/api/attachments/UWHCKS3J/fulltext/images/8712eb6371f41265add44a2ca6903f97ed7e935fee2ee60daa1f77b0f7c05055.jpg)

Parag Pendharkar is an associate professor of information systems at Penn State Harrisburg. His work has appeared, or have been accepted, for publication in Annals of Operations Research, Communications of ACM, Computers and Operations Research, Decision Sciences, Decision Support Systems, European Journal of Operational Research, Expert Systems with Applications, Intelligent

actions on Professional Communication, Interfaces, Information and Management, Multiple Valued Logic, Omega, as well as several other journals. Currently, he is serving as an associate editor for the International Journal of Human–Computer Studies.
