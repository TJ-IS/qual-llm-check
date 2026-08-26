---
otero_id: 19920
otero_key: "84VRUNG4"
title: "Multiple objective metaheuristics for feature selection based on stakeholder requirements in credit scoring"
authors: "Naomi Simumba; Suguru Okami; Akira Kodaka; Naohiko Kohtake"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113714"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multiple objective metaheuristics for feature selection based on stakeholder requirements in credit scoring

![](/api/attachments/84VRUNG4/fulltext/images/81f67df706bed534dd4bedeb1354c2552f9457c8a691f1246d41e8d67361c155.jpg)

Naomi Simumba <sup>\*</sup>, Suguru Okami, Akira Kodaka, Naohiko Kohtake

Graduate School of System Design and Management, Keio University, 4-1-1, Hiyoshi, Kohoku-ku, Yokohama 223-8526, Japan

## A R T I C L E I N F O

Keywords: Profit scoring Alternative data Many objective optimization Non-dominated sorting Stakeholder requirements

## A B S T R A C T

Alternative data is increasingly utilized for credit evaluation of financially excluded persons. However, re quirements, such as reliability, which gain new importance when alternative data is employed for credit eval uation, have not been considered as part of the credit scoring process. This research proposes an approach for incorporating context-specific stakeholder requirements in the credit scoring process. Two hybrid heuristics are proposed for a feature selection process that simultaneously optimizes all requirements. The first is a multiple objective, non-dominated sorting, binary Grasshopper Optimization Algorithm. The second incorporates the selection. crossover, and mutation techniques of genetic algorithms for greater diversity. Both algorithms are fitted with objective functions obtained from stakeholder requirements for multiple objective feature selection. Empirical evaluation is conducted with stakeholder requirements and alternative data features collected from mobile, public geospatial, and satellite data sources. Their performance is compared against several existing algorithms, and they offer improved performance on specific metrics. The first algorithm outperforms the existing many-objective non dominated sorting genetic algorithm, NSGA-III, in terms of computational time, convergence, and spacing. Meanwhile, the second method results in greater spread for the same population size but has a lengthy computational time. Thus, stakeholder requirements are successfully incorporated into the feature selection process. This results in a better balance between objectives. These findings extend the research on hybrid metaheuristics for feature selection, as well as alternative data for credit scoring.

## 1. Introduction

Credit scoring is a necessary step in the lending process, allowing financial institutions to distinguish creditworthy borrowers and manage their exposure to risk [1]. Although traditional credit scoring requires financial data such as bank account records, this data is often unavai lable for financially excluded people [2]. Financial exclusion affects a large portion of society with 31% percent of adults globally being unbanked [3]. To overcome the lack of financial data and enable credit scoring of financially excluded people, the use of alternative data (or non-financial data) has been proposed [4]. Several researchers have examined credit scoring with alternative data. For instance. mobile. social media, and utilities data [5,6]. Furthermore, lenders in various parts of the globe currently offer loans assessed based on alternative data [7]. However, practical use of alternative data for credit scoring raises new concerns from stakeholders [2]. For instance, as alternative data is often not fully reported, completeness of variables may be an issue.

There is a higher risk of unintended disproportional impact on certain groups with the use of alternative data, making fairness in selection of variables crucial. Additionally, with new methods of data collection being employed, reliability must be considered [8]. These requirements are context specific and rely on the data sources and diverse stake holders involved, such as financial institutions, borrowers, and governments.

Certain requirements have been addressed in existing research. For instance, profit evaluations are a valuable tool in assessing the expected profit, and thus enhance business decision making for lenders [9]. Feature selection is another key consideration, with the goal typically being to minimize the number of features. Doing so reduces data acquisition costs, computation time, and model complexity [10], which affect the application of the model obtained. Much of the literature conducts feature selection as a preliminary step before training the credit scoring model, and aims to improve a statistical measure, for example area under the receiver operating curve (AUC) [6].

Multicriteria optimization methods have also been employed to simul taneously consider feature selection and a single training objective, for instance profit [11]. However, research exploring cases with more than two objectives or requirements for credit scoring is limited. Addition ally, the assumption is often made that all features have the same data acquisition cost [12]. Yet credit scoring gains new complexity where data acquisition costs vary for different variables [13]. This may be the case when alternative data from multiple sources is combined.

In addition, while incorporating business concerns in feature selec tion is not new, it is typically done through a priori decision making [1]. Analysts eliminate less desirable features according to needs (for example collection cost and ease of collection) prior to feature selection based on a single statistical measure (e.g. accuracy and AUC) or a business metric (e.g. profit). Therefore, the true impact of these features on all requirements is not known beforehand. Several requirements are not explicitly stated nor are they simultaneously assessed as part of the feature selection process. This could result in acceptable features being eliminated before analysis. Furthermore, to our knowledge, feature se lection conducted in the existing literature focused on concerns such as profit and exposure at default. These are inherently concerns from one stakeholder, the lender. The needs of some groups of stakeholders may be overlooked, which may affect the acceptance and success of the credit scoring system. For instance, lenders may be more concerned with profit, while borrowers may focus on fairness and explainability. To address these issues, an approach for handling stakeholder requirements surrounding alternative data use in credit evaluations is needed.

This research aims to fill the gap in existing literature by proposing an approach that simultaneously factors in profit, feature selection, and other context specific stakeholder data requirements. This methodology emphasises inclusion of requirements from different stakeholders. It also allows for clearer decision making as all the objectives are compared explicitly and simultaneously. As there will be three or more objectives to optimize, this becomes a many objective optimization problem [14]. The concept of requirement values is introduced to quantify data re quirements obtained through the stakeholder requirements definition process [15]. To perform simultaneous optimization, the continuous Grasshopper Optimization Algorithm (GOA) [16] is adapted for feature selection. GOA is a newly developed, nature-inspired metaheuristic selected due to its high exploration and fast convergence. It has also performed well in comparison to other existing algorithms on test problems. The algorithm is modified by introducing binarization through a transfer function and non-dominated sorting, thereby pro ducing a many objective non-dominated sorting, binary Grasshopper Optimization Algorithm (NSBGOA). Additionally, a second hybrid algorithm, SelCrossMut NSBGOA, is proposed by introducing the selec tion, crossover, and mutation strategies from genetic algorithms [17]. While existing literature has applied a binary GOA for feature selection [18,19], this research goes further by integrating non-dominated sorting and evolution strategies from genetic algorithms. The new algorithms are fitted with obiective functions from stakeholders' data requirements to conduct feature selection, thus balancing the considerations arising due to the nature and collection methods of alternative data The following are the key points of this research: incorporating stakeholder data requirements, evaluating more than two objective functions for credit scoring, requirement values to quantify the stakeholder re quirements, and development of two hybrid metaheuristics. Section 2 reviews related work while the proposed approach is detailed in Section 3. In Section $^ { 4 , }$ an empirical evaluation is conducted with data collected from farmers in rural Cambodia. Section 5 presents the results of the evaluations, which are then discussed in section 6. Limitations are given in section 7. Finally, a conclusion is reached in Section 8 where future research paths are also suggested.

## 2. Related work

## 2.1. Alternative data

Data applied for credit scoring can be broadly classified as traditional and alternative [2]. Traditionally, financial and demographic informa tion consisting of loan inquiries, payments, and defaults is applied. As this information is often lacking or sparse for financially excluded in dividuals, alternative data usage in credit scoring has seen a rise [20]. Incorporating email usage and psychometric variables has been shown to enhance predictive accuracy in default prediction [6]. Addition of call network information to debit and credit account information for credit scoring was proven to improve profit measures [21]. Public geospatial data has also found applications in this domain, with macroeconomic indicators proving useful in credit scoring [22]. Integration of satellite, public geospatial, and mobile data improved performance of credit scoring models [5].

## 2.2. Profit based credit scoring

Credit scoring is the set of decision models and techniques that aid lenders in granting consumer credit [1]. Analytically, credit scoring is a classification problem employing a wide range of algorithms of varying complexity, with logistic regression often being used a benchmark. Other commonly applied methods include support vector machines, artificial neural networks, and ensemble classifiers [12]. Recently, profit based measures have been introduced to enhance the business decision making process for lenders. Maldonado et al. in [9] proposed a profit measure consisting of the benefits of correctly classifying good bor rowers minus the losses from incorrectly classifying bad borrowers and the variable acquisition costs. Verbraken et al. proposed the Expected Maximum Profit (EMP) comprised of the benefits of correct classifica tion and costs of misclassification, and adapted it to consumer credit scoring [23].

EMP is the maximum amount a company can obtain by applying the classifier. There is no cost associated with correctly classifying a defaulter. Where a good borrower is incorrectly classified as bad, the cost is return on investment (ROI). Finally, where a defaulter is correctly classified, the benefit $b \in [ 0 , 1 ]$ is expressed by eq. 1. LGD is the loss given default, EAD is the exposure at default, and A is the principal amount of the loan. With $H _ { O }$ and $H _ { I }$ being the predicted cumulative density func tion, and π and $\pi _ { 1 }$ as the prior probabilities of default and non-default respectively, assuming a constant ROI, the EMP can be expressed by eq. 2 below.

$$
b = \frac {L G D ^ {*} E A D}{A}\tag{1}
$$

$$
E M P = \int_ {0} ^ {1} (b ^ {*} \pi_ {0} H _ {0} - R O I ^ {*} \pi_ {1} H _ {1}) ^ {*} g (b) d b\tag{2}
$$

## 2.3. Optimizing multiple objectives

Multi Criteria Decision Making (MCDM) allows designers to balance several, often conflicting, objectives. MCDM with a continuous decision space is termed Multi Objective Decision Making (MODM) and utilizes Multi-Objective Optimization (MOO) methods [24]. MOO problems attempt to optimize more than one objective. For multi-objective problems, this may be defined by eqs. 3 and 4 below:

$$
\text { minimize } F (x) = \left(f _ {1} (x), f _ {2} (x), \dots , f _ {m} (x)\right) ^ {T}\tag{3}
$$

$$
\text { where   vector }, X = (x _ {1}, x _ {2}, \dots , x _ {n})\tag{4}
$$

Where X is the decision vector, Ω is the decision space, and $X { \in } S$ . F(x) is a vector of objective functions with F: $\Omega \to \Lambda .$ . The class of problems where m $\geq 3$ are referred to as many objective optimization problems (MaOP). The aim is to approximate the Pareto optimal set in the objective space, ꓥ, so that no single criterion can be improved without making at least one other criterion worse. This is a non-dominated set of solutions allowing the trade-off of one objective against the others [25].

Multi-objective optimization (MOO) methods guide the search for solutions towards the pareto optimal set while maintaining diversity. They are a valuable tool where feature selection must simultaneously accommodate several objectives. Evolutionary algorithms, based on the concept of random variation and subsequent selection, are commonly used for MOO problems [26]. Examples include Strength Pareto Evolutionary Algorithm (SEPA-II) and non-dominated sorting genetic algorithm (NSGA-II) which work on two-objective problems [14]. Var iations of other optimization methods incorporating non-dominated sorting (NS) have been proposed in the existing literature. Swarm in telligence optimization methods have been adapted for multiple objec tives by incorporating non-dominated sorting of solutions to select candidates for the next iteration. For example non-dominated sorting with the Artificial Bee Colony (ABC) [27]. Other research improved existing multi-objective algorithms. For instance, Siddiqi and Sait [28] proposed the use of Tabu Search to speed up the convergence of NSGA II.

Multi-objective evolutionary algorithms (MOEAs), for instance bi nary nondominated sorting genetic algorithm II (NSGA-II), are popular tools for solving multi-objective problems [14]. However, they deal poorly with many objective optimizations (MaOP), because the increasing number of objectives leads to deterioration. Several tech niques have been applied to extend multi-objective optimization to many objective problems, including indicator, aggregation, and refer ence methods [29]. Indicator-based methods such as the S-metric se lection evolutionary multi-objective algorithm (SMS-EMOA) do not rely on pareto dominance. However, the high computational cost of its hypervolume indicator with increasing objectives limits its application. Reference-based methods also exist. For example, an extension of NSGA-II to deal with MaOP called NSGA-III. NSGA-III generates a reference set from virtual points of the objective space to measure the quality of so lutions [30]. Examples of its adaptations include converting Cuckoo Optimization Algorithm (COA) for MaOP with the reference-based nondominated sorting strategy of NSGA-III [31].

## 2.4. Feature selection

Feature selection plays an important role in credit risk evaluation. Typically, the goal is to maximize the model performance while keeping the number of features to a minimum. This reduces noise, data acqui sition costs, and the risk of overfitting. Broadly, feature selection methods are divided into filter, wrapper, and embedded methods [10]. Filter methods select features based on inherent properties such as variance or mutual information [32]. These methods are blind to in teractions or correlations between features. An example would be analysis of variance (ANOVA). Wrapper methods, such as backward and forward selection, fit a model with subsets of the features and evaluate feature importance. They aim to find the best performing subset. How ever, these methods tend to have a high computational cost on datasets with a large feature set. Finally, embedded method simultaneously perform feature selection and model fitting. LASSO [33] and ridge regression are popular examples.

## 2.5. Multiple objectives in feature selection

Other examples of feature selection include Maldonado et al. [9] using Holdout Support Vector Machine (HOSVM) along with a profitbased measure to remove features which had the least impact on prof itability. Alternatively, mixed-integer linear programming models with varying acquisition costs as constraints have been used for feature se lection [13]. Multi-objective methods have been employed where mul tiple objectives are optimized during feature selection. Feature selection methods based on optimization of two criteria are readily available in existing literature. Feature selection was implemented by fitting a nondominated sorting genetic algorithm-II (NSGA-II) to maximize the ex pected maximum profit (EMP) and minimize the number of features [11]. Filter-based feature selection was conducted using a nondominated sorting binary Particle Swarm Optimization (NSBPSO) method with mutual information and entropy as the criteria to be optimized [34]. Continuous GOA algorithms were adapted for binary numbers and used in filter-based feature selection based on error rate and number of features [18,19].

Concretely, this research differs from existing literature by incorpo rating stakeholder requirements concerning alternative data into the feature selection process through modelling several fitness functions based on requirements values. Further, it employs two new metaheuristics, NSBGOA and SelCrossMut NSBGOA, for feature selection in credit scoring.

## 3. Proposed approach

This proposed approach is targeted towards credit evaluation of unbanked and thin file individuals where financial data of borrowers is unavailable and distance poses a challenge in data collection. Pre liminary work to be done before applying this method is described below.

## 3.1. Stakeholder requirement definition process

The stakeholder requirement definition process in the domain of Systems Engineering defines “… the requirements for a system that can provide the services needed by users and other stakeholders in the defined environment” [15]. The goal of the Systems Engineering process is to build a system that meets the requirements and needs of its stakeholders. Therefore, stakeholders who hold an interest in the system must first be identified. In the case of credit scoring for financially excluded persons, these may include financial institutions, borrowers, governments, and data collection companies. From the stakeholder requirement definition process, requirements may be obtained as follows:

• Core requirement: Functional requirements express “what” the system should do. In developing a credit evaluation system, it is important to note that the key requirement of any such system is to assess risk of lending to a target group of borrowers. Thus, we set this as the core functional requirement of the credit evaluation system.

• Additional Requirements (related to data): Non-functional re quirements express “how” the system should carry out its functions. Beyond the core functional requirement, other requirements may be determined through discussion with stakeholders. Specifically, this research focuses on addressing those requirements related to alter native credit scoring data.

## 3.2. Data identification and collection

This involves identifying available sources for collection of data related to the borrowers and their income earning activities. It is carried out through business analysis and research. This is followed by collec tion of data variables. Based on the data variables and the source from which they are collected, stakeholder data requirements values may be estimated.

## 3.3. Problem formulation

Definition 1. Available features, $Z = ( \mathbf { z } _ { 1 } , \mathbf { z } _ { 2 } , \mathbf { z } _ { 3 } , . . . , \mathbf { z } _ { \mathrm { h } } )$ is a vector of h data variables related to the borrowers and their income earning ac tivities that could be used to evaluate credit worthiness.

Definition 2. Stakeholder data requirements, $\mathbf { R } = ( \mathbf { r } _ { 1 } , \mathbf { r } _ { 2 } , \mathbf { r } _ { 3 } , . . . , \mathbf { r } _ { \mathrm { k } } )$ is a vector of k objective functions representing the stakeholder re quirements associated with the data. Each outlines a condition that data used in the profit scoring process must fulfil.

Definition 3. Expected Maximum Profit, (EMP) a general profit based measure.

Definition 4. Requirement values, V, (eq. 5) is a matrix with di mensions ${ \mathrm { ~  ~ h ~ } } ^ { * } { \mathrm {  ~ k ~ } } ,$ containing the values of the objective functions in R for each feature in Z. All requirement values are assigned to through esti mation during the data identification and estimation phase.

Definition 5. Default status, $D = ( { \mathrm { d } } _ { 1 } , { \mathrm { d } } _ { 2 } , { \mathrm { d } } _ { 3 } , . . . , { \mathrm { d } } _ { \mathrm { v } } )$ is a vector of length v with binary values representing repayment status of loans extended to the target group of borrowers.

Definition 6. Borrower information, B, (eq. 6) is a matrix with di mensions ${ \textbf { v } } ^ { * } { \textbf { h } } ,$ , containing the values of the features in Z for each borrower.

Requirements Values,

$$
V = \left[ \begin{array}{c c c c} \mathrm{rv} _ {1 1} & \mathrm{rv} _ {1 2} & \dots & \mathrm{rv} _ {1 k} \\ \mathrm{rv} _ {2 1} & \mathrm{rv} _ {2 2} & \dots & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \mathrm{rv} _ {h 1} & \dots & \dots & \ddots \end{array} \right]\tag{5}
$$

Borrower Information,

$$
B = \left[ \begin{array}{c c c c} \mathsf {b} _ {1 1} & \mathsf {b} _ {1 2} & \dots & \mathsf {b} _ {1 h} \\ \mathsf {b} _ {2 1} & \mathsf {b} _ {2 2} & \dots & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \mathsf {b} _ {\nu 1} & \dots & \dots & \ddots \end{array} \right]\tag{6}
$$

Generally, given a possible solution $\boldsymbol { \cdot } \boldsymbol { s } = \{ \mathbf { z } _ { 1 } , \mathbf { z } _ { 2 } , \mathbf { z } _ { 3 } , . . . , \mathbf { z } _ { \mathrm { p } } \}$ containing $p$ features where ${ \mathfrak { s c z } } ,$ then the value of the uth data requirement for this solution, ${ \bf r _ { u } } ,$ is given by eq. 7.

$$
\mathrm{r} _ {u} = \frac {\sum_ {i = 1} ^ {p} \mathrm{rv} _ {q u}}{\text { value   with   all   features }}\tag{7}
$$

Goal: Identify the set of non-dominated solutions, $S = \{ s _ { 1 } , s _ { 2 } , s _ { 3 } , . . . \}$ where each member, $s ,$ is a unique subset of the available features, Z. These subsets should result in non-dominated values of the data requirements, R, so that one objective cannot be improved without harming another. To achieve this, two algorithms are proposed based on GOA: NSBGOA and SelCrossMut NSBGOA.

## 3.4. Grasshopper optimization algorithm (GOA)

Grasshopper Optimization Algorithm (GOA) is a nature-inspired metaheuristic. Metaheuristics aim to select the best solutions to lead to the optimal solution while also employing randomization to avoid any local optima. GOA has proven to be a powerful optimization algo rithm with high exploration and fast convergence, outperforming several existing techniques on test problems. Its adaptive behaviour also balances exploration and exploitation. These features motivate the choice of GOA for this research. Classed as a Swarm Intelligence (SI) algorithm, GOA was proposed Saremi et al. [16]. It mathematically models the behaviour of grasshoppers which tend to form swarms, with the position of the grasshoppers in the swarm representing a potential solution. $\mathrm { X _ { i } , }$ the position of the ith grasshopper is expressed by eq. 8 as a function of the social interaction (S ), gravity force (G ), and wind advection (A ).

$$
X _ {i} = S _ {i} + G _ {i} + A _ {i}\tag{8}
$$

With the gravity component ignored, and the wind direction assumed to point towards the target, the equation adapted for optimi zation of N grasshoppers is expressed by eq. 9:

$$
X_{i}^{d} = c\left(\sum_{\substack{j = 1\\ j\neq i}}^{N}c\frac{ub_{d} - lb_{d}}{2}s\Big(\Big|x_{j}^{d} - x_{i}^{d}\Big|\Big)\frac{x_{j} - x_{i}}{d_{ij}}\right) + \widehat{T_{d}}\tag{9}
$$

$d _ { i j }$ (eq. 10) is the distance between the ith and jth grasshopper and the function, s, of eq. 11 represents the strength of the social forces, where l is the attractive range scale and f is the intensity of attraction.

$$
d _ {i j} = \left| d _ {j} - d _ {i} \right|\tag{10}
$$

$$
s (r) = f e ^ {\frac {- r}{l}} - e ^ {- r}\tag{11}
$$

The adjustment of l and f makes it possible to model different social behaviours in the grasshoppers by altering the comfort, attraction, and repulsion zones of the swarm. As suggested by the authors in [16], we select l = 1.5 and $\cdot f { = } 0 . 5$ . Since the function s returns values close to zero for distances greater than 10, the distance is mapped to the interval $[ 1 , 4 ]$ . In eq. 9, ub and $i b _ { d }$ are the upper bound and lower bound in the Dth dimension $s ( r ) = f e ^ { \frac { - r } { l } } - e ^ { - r } .$ . <sup>̂</sup>T is the value of the Dth dimension in the target.The parameter c (eq. 12) is the decreasing coefficient to shrink the comfort zone, repulsion zone, and attraction zone. The parameter c decreases the comfort zone with each iteration as follows, where L is the maximum number of iterations, l is the current value, and cmax and cmin are the maximum and minimum values respectively:

$$
c = c m a x - l \frac {c m a x - c m i n}{L}\tag{12}
$$

Thus, the grasshoppers, which are initialized at random positions, are brought together into a unified, regulated swarm. Eventually, the grasshoppers reach a comfort zone and stop moving. Each grasshopper's next position is a function of its current position, the target position, and the position of other grasshoppers in the swarm. This algorithm is given in Table 1.

## 3.5. NSBGOA

Prior to explaining the NSBGOA algorithm, the need for binarization must be discussed. Given j as the number of features, a grasshopper's position is a j bit binary number with each bit denoting whether the corresponding feature is selected. Since the traditional GOA optimizer is continuous in nature, and feature selection requires binary numbers, conversion is required. Several techniques have been proposed for conversion [19]. One technique uses transfer functions, including the sigmoidal and hyperbolic tan transfer functions, allowing the conversion from real to binary without changing the structure of the algorithm. The output of the transfer function then denotes the probability of updating the binary bit from 0 to 1, and vice versa. Probability of changing values is given by the step vector values. From eq. 9, the velocity of the grasshopper at each iteration, ΔX, is adapted to eq. 13 below. A random number, $^ { r , }$ in the range [0,1] and the sigmoidal transfer function (eq. 14) are used to obtain the dth dimension of a grasshopper in the next iter ation, $X _ { t + 1 } { } ^ { d } ( \mathrm { e q . ~ } 1 5 )$ .

$$
\Delta X = c_{1}\left(\sum_{\substack{j = 1\\ j\neq i}}^{N}c_{2}\frac{ub_{d} - lb_{d}}{2}s\Big(\big|x_{j}^{d} - x_{i}^{d}\big|\Big)\frac{x_{j} - x_{i}}{d_{ij}}\right)\tag{13}
$$

$$
T (\Delta X _ {t}) = \frac {1}{1 + e ^ {- \Delta X _ {t}}}
$$

(14)

$$
X _ {t + 1} ^ {d} = \left\{ \begin{array}{l} 1 \text {   if   } r <   T (\Delta X _ {t + 1} ^ {d}) \\ 0 \text {   if   } r \geq T (\Delta X _ {t + 1} ^ {d}) \end{array} \right.\tag{15}
$$

Table 1 Pseudo code for Grasshopper Optimization Algorithm.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm for GOA
Initialize the swarm  $X_{0}$ 
Initialize cmax, cmin, and maximum number of iterations
Calculate fitness of each search agent
T = the best search agent
while (i &gt; Max number of iterations)
    Update c using equation 12
    for each search agent
    normalize the distances between grasshoppers in [1,4]
    update the position of the current grasshopper
    bring the current grasshopper back if it goes outside the boundaries
    end for
    update T if there is a better solution
    i = i+1
end while
Return T
</div>

Necessary operations are given in Table 2. Finally, the NSBGOA al gorithm proceeds as follows. The NSBGOA algorithm is given in Table 3:

• Initialization(): The population is initialized by assigning grass hoppers to N random positions, where N is the size of population.

• Fitness\_evaluation(): For each grasshopper position, features denoted by 1 are selected and used to compute the value of the stakeholder data requirements, R. These values serve as the fitness of the associated grasshopper.

• Non\_dominated\_sorting(): The traditional GOA algorithm performs a simple comparison to update the best position during each

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
List of operations
Initialize()
    Initialize the grasshopper swarm  $G_{t}$  (i = 1,2,...,N)
    Initialize cmax, cmin, and maximum number of iterations, maxIter

SelCrossMut_Operator ()
    $Q_{t}$  = Recombine and mutate  $P_{t}$ $H_{t}$  =  $Q_{t} \cup P_{t}$ , where  $H_{t}$  is a population of size 2N

GOA_Operator()
    Update c
    for grasshopper in  $G_{t}$ 
    normalize the distances between grasshoppers in [1,4]
    compute and update new grasshopper positions

Select_Next()
    $Z_{t}$  = Sort  $H_{t}$  by position on fronts
    $G_{t+1}$  = ∅
    i = 1
    while i &lt;= N do:
    $G_{t+1}$  =  $G_{t+1} \cup ith$  member of  $Z_{t}$ 
    i = i + 1
    end while
    bestFront $_{t+1}$ , fitnessOfBestFront $_{t+1}$  = non_dominated_sorting( $G_{t+1}$ ,  $F_{t}$ )

non_dominated_sorting()
    based on fitness values, arrange population into fronts, with each front containing a set of non dominated solution
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 3
Proposed NSBGOA.

Proposed NSBGOA

Input:
• Available features, Z
• Requirements, R
• Requirements values, V
• Borrower information, B
• Default status, D
• Population size, N
• maxIter

Steps
t=0
$G_t$ = Initialize()
$P_t$ = $G_t$ $F_t$ = Fitness_Evaluation($P_t$, B, D, V)
bestFront$_t$, fitnessOfBestFront$_t$ = non-dominated_sorting($P_t$, $F_t$)
while t &lt; maxIter do:
    $G_t$ = GOA_Operator($P_t$, bestFront$_t$)
    $P_t$ = $G_t$ $F_t$ = Fitness_Evaluation($P_t$, B, D, V)
    bestFront$_t$, fitnessOfBestFront$_t$ = non-dominated_sorting($P_t$, $F_t$)
    $G_{t+1}$, bestFront$_{t+1}$, fitnessOfBestFront$_{t+1}$ = Select_Next($P_t$, N, bestFront$_t$, fitnessOfBestFront$_t$)
    t = t + 1

end while
S = bestFront

Output
• set of non-dominated solutions, S
</div>

iteration. This in turn becomes the target towards which all grass hoppers are guided. However, as there are multiple objectives being optimized. a simple comparison would be unsuitable. Therefore. non-dominated sorting is employed to organise the population of grasshoppers into fronts, so that each front contains a set of nondominated solutions and the first front contains the best set of so lutions. The first front is assigned as the bestFront.

From here, the algorithm performs the following until the maximum number of iterations is reached.

• GOA\_operator(): the distances between grasshoppers is normalized between in [1,4] and ΔX is computed by eq. 13. The new grasshopper positions are updated by eq. 15.

• Fitness\_evaluation()

• Non\_dominated\_sorting()

• Select\_next(): the grasshopper population is re-arranged according to position on the first front and the next generation is created by selecting the first N grasshoppers. The best front and fitness of the best front for this new generations are also obtained for the next iteration.

## 3.6. SelCrossMut NSBGOA

The second proposed algorithm, termed SelCrossMut NSBGOA, ex tends NSBGOA by incorporating the selection, crossover and mutation operations associated with genetic algorithms to increase the diversity at each step. Table 4 gives the overall SelCrossMut NSBGOA algorithm. Genetic algorithms are based on the concept of natural evolution wherein selection and recombination of chromosomes over time leads to fitter individuals. An initial population of candidate solutions, or in dividuals, is selected and evaluated for fitness using the provided fitness or objective functions. Selection and then crossover are used to come up with new individuals, and fitter individuals become part of the popu lation for the next iteration [17]. The SelCrossMut\_Operator performs recombination and mutation by first selecting two members of the population and crossing them to obtain two children. Mutation, where a bit is arbitrarily changed, may also occur with a given probability. The child and parent populations are then combined and evaluated before non-dominated sorting is performed. This selection, crossover and mu tation process increases the diversity of the population and allows the algorithm to consider solutions from a wider range.

## 3.7. Performance metrics

Hypervolume indicator (HV) measures the size of the space domi nated by the Pareto Front approximation, S, and delimited from above by the reference point $, y ,$ such that s $^ { \mathrm { ~ ~ } } { } _ { S , \ / }$ s dominates y. HV is given by eq. 16 where $\lambda _ { m }$ is the m-dimensional Lebesgue measure and m is the number of obiectives [35]. HV is a commonly applied measure to compare performance of different algorithms. It can be used as measure of convergence and distribution.

$$
H V (S, y) = \lambda_ {m} \left(\bigcup_ {s \in S} [ s; y ]\right)\tag{16}
$$

Generational Distance (GD), an indicator used to measure conver gence, is given by eq. 17 where P is a discrete representation of the Pareto front, |S| is the number of points in an approximation of the

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 4 Proposed SelCrossMut NSBGOA.

Proposed SelCrossMut NSBGOA

Input:
• Available features, Z
• Requirements, R
• Requirements values, V
• Borrower information, B
• Default status, D
• Population size, N
• maxIter

Steps
t=0
$G_t$ =Initialize()
$P_t$ = $G_t$ $H_t$ = SelCrossMut_Operator($P_t$)
$F_t$ = Fitness_Evaluation($H_t$, B, D, V)
bestFront$_t$, fitnessOfBestFront$_t$ = non-dominated_sorting($H_t$, $F_t$)
while t &lt; maxIter do:
    $G_t$ = GOA_Operator($H_t$, bestFront$_t$)
    $P_t$ = $G_t$ $H_t$ = SelCrossMut_Operator($P_t$)
    $F_t$ = Fitness_Evaluation($H_t$, B, D, V)
    bestFront$_t$, fitnessOfBestFront$_t$ = non-dominated_sorting($H_t$, $F_t$)
    $G_{t+1}$, bestFront$_{t+1}$, fitnessOfBestFront$_{t+1}$ = Select_Next($H_t$, N, bestFront$_t$, fitnessOfBestFront$_t$)
    t = t + 1

end while
S = bestFront

Output: set of non-dominated solutions, S
</div>

Pareto set, and p generally equals 2.

$$
G D (S, P) = \frac {1}{| S |} \left(\sum_ {s \in S} \min _ {q \in P} \| F (s) - F (q) \| ^ {p}\right) ^ {1 / p}\tag{17}
$$

Spacing (SP), given in eq. 18, measures distribution with S as the Pareto approximation and $d _ { i }$ as the $\boldsymbol { \mathrm { l } } _ { 1 }$ distance calculated by eq. 19.

$$
S P (S) = \sqrt {\frac {1}{| S | - 1} \sum_ {i = 1} ^ {| S |} (\bar {d} - d _ {i}) ^ {2}}\tag{18}
$$

$$
d _ {i} = \min _ {\left(s _ {i}, s _ {j}\right) \epsilon S, s _ {i} \neq s _ {j}} \left\| F (s _ {i}) - F (s _ {j}) \right\| _ {1}\tag{19}
$$

Overall Pareto Spread (OS) (eq. 20) denotes the extent of the front covered by the pareto front approximations with m objectives. S is the Pareto approximation, Q is the nadir point, U is the ideal point.

$$
O S (S) = \prod_ {i = 1} ^ {m} \frac {\left| \max _ {s \epsilon S} f _ {i} (s) - \min _ {s \epsilon S} f _ {i} (s) \right|}{\left| f _ {i} (Q) - f _ {i} (\mathrm{U}) \right|}\tag{20}
$$

## 3.8. Comparison to existing research

While two objective optimization of profit and number of features with the non-dominated sorting algorithm (NSGA-II) was considered [11], this research did not consider additional objectives due to alter native data. Further, data acquisition costs were assumed to uniform for all variables. In addition, performance of the NSGA-II algorithm de grades with a larger number of objectives, making it unsuitable for this application. Cost-based feature selection with varying costs was proposed in [13] by introducing constraints to a support vector machine (SVM) classifier. Enhancement of credit scoring with alternative data was researched [6]. However, additional requirements were not evaluated. In terms of the algorithm applied, [27,31] proposed the use of nondominated sorting methods inspired by NSGA-III and NSGA-II methods to adapt optimization methods for multiple objectives, while [28] employed Tabu search to speed up the convergence of NSGA-II. Continuous GOA was adapted for feature selection with several pro posed binary versions of GOA using hamming distance [18], as well as stochastic mutation and transfer functions [19]. However, these methods did not consider integrating non-dominated sorting or selec tion, crossover, and mutation strategies from genetic algorithms with GOA for increase diversity. The proposed approach evaluates all ob jectives on the same basis and does not require the decision maker to state preferences such as penalization weights or constraint values prior to analysis. Additionally, several solutions are offered, which allows decision makers to consider different trade-offs. Table A.1 shows this comparison.

## 4. Empirical evaluation

## 4.1. Study area

To evaluate the proposed approach, analysis is conducted of loans given to smallholder farmers in Cambodia. Cambodia, a developing country in Asia, has agriculture as a major economic activity. Access to financial services remains a challenge with less than 30% of adults using formal lending services [36]. Overall, the study area can be considered as a typical area where smallholder farmers have difficulties in accessing financial services.

## 4.2. Stakeholder requirement definition process

Stakeholders including lending institutions, smallholder farmers, agricultural businesses that work with smallholder farmers, and data collection companies were identified in Cambodia. Through a series of interviews and workshops conducted with these stakeholders from 2017 to 2020, several requirements were collected for a credit evaluation system using alternative data. Below is a non-exhaustive list of some of these requirements raised by stakeholders:

i. Profit: the data used for evaluation should result in maximized profits.

ii. Number of Features: a minimal amount of data shall be collected for evaluation.

iii. Affordability: the affordability of data collection should be maximized, thus keeping data collection costs to a minimum.

iv. Reliability: the data used in evaluation should be as reliable as possible.

v. Collectability (the ease with which data can be collected): data collection shall require minimal time and expert know-how.

actual implementation would require more detailed assignment of requirement values, for evaluation purposes, a simple assignment method with estimated rankings is utilized. Public geospatial data is the easiest to collect and the most affordable because it is free. However, it may be the least reliable with a lower update frequency. Satellite data, coming from independently verifiable measurements, may be the most reliable and expensive. Features from the three data sources are given an approximate ranking on their affordability, reliability, and collectability as shown in Table 5. To compute affordability, we consider that a group of variables may be purchased together, meaning that incorporating a single variable from a given source has the same acquisition cost as incorporating all variables from that source. Additionally, a per-variable cost of 0.01 is deducted to account for storage and processing costs. This value is kept small so as to not affect the trade-off between objectives. However, it allows the model to favor solutions with a smaller number of variables even when they are from the same source. For reliability and collectability, we consider that variables from the same source may have different values. For instance, self-reported information may be less reliable than meta-data collected from the user's behaviour on the mo bile application. It should be noted that assigned requirement values may change depending on the context, even for similar data sources., From the functions in Table 5, except for affordability, the objectives are scaled by division with maximum.

## 4.3. Data identification and collection

Profit scoring for smallholder farmers requires consideration of the data pertaining to repayment ability such as rainfall and temperature. Information about factors such as water availability, access to markets, and vegetation, can be obtained from satellite images and public geo spatial data. Moreover, information about behaviour and demographics can be collected through a mobile application. Broadly, the features may be grouped by their source.

• Credit Data: default information from loans extended to farmers in rural Cambodia from 2018 to 2019 was assessed. Loans had a oneyear term of maturity. “Paid” loans, encoded as binary 1, refer to loans that had been repaid in full at the time of loan maturity. “Default” loans, encoded as binary 0, refer to loans that were not paid in full at the time of loan maturity.

• Mobile Features: the collection of mobile data was done through an agribusiness' mobile application. The data were anonymized by the provider and used solely for research purposes. Application users collect farm activity information from farmers in their area on a regular basis. These farmers may not be able to use the application directly due to cost or illiteracy, et cetera. Additionally, information on the behaviour of users on the application was also collected. The data comprises behaviour of users on the mobile application, including the number of farms they cater to and whether they take recommended actions such as uploading photographs. Behavioural information was chosen as it can give insight into an individual's character. Importantly, the geographical location of each farm was collected as it is necessary for the combination of mobile data with the other data types.

• Public Geospatial Features: were obtained by integrating farm location and public geospatial data. These features gave the prox imity of the farm to roads, rivers, and canals. Proximity to these could affect the ability of the farmer to produce a high yield and access markets to sell their crops.

• Satellite features: were obtained from satellite data sources and included temperature, elevation, slope, as well as vegetation and water indices.

The data collected from these three sources was integrated with the spatio-temporal integration method proposed by Simumba et al. [5], resulting in a total of 66 available features listed in Table B.1. While

## 4.4. Data analysis

Pre-processing involved imputing data using mean values and rescaling using the max-min method for numeric variables. The 245:43 entries resulted in an imbalance ratio of 1 to 5.7 and the synthetic mi nority oversampling technique (SMOTE) was employed for class bal ance. All analysis was conducted in CRAN R. NSBGOA and SelCrossMut NSBGOA were evaluated as per Tables 3 and 4, respectively, using appropriately modified version of the “GOA” function (“metaheur isticOpt” package). To calculate the EMP for each subset of features in the population, a logistic regression classifier was trained with the “caret” package using three repeats of tenfold cross-validation and the best model was selected based on the EMP (“EMP” package). EMP pa rameters were set to $p _ { O } = 0 . 5 5 , p _ { I } = 0 . 1 , R O I = 0 . 2 6 4 4$ [23]. This was followed by evaluation of the remaining obiectives according to Table 5. The NSGA-III and NSGA-II algorithms were implemented with the same data and objective functions using the “nsga3” and “nsga2” functions (“rmoo” package) to compare their performance to the proposed algo rithms. Beyond this, a genetic algorithm (GA) [17] and a LASSO [33] regression model with alpha = 1 and lambda =0 were fitted on the data using three repeats of tenfold cross-validation with the best model selected based on the EMP. Lastly, a logistic regression model was also trained on all the original features. The initial population and maximum iterations were both set to 50 for SelCrossMut NSBGOA, NSBGOA, NSGA-III, NSGA-II, and GA. Algorithms were assessed by the same procedure on the Australian, Taiwan, and German credit datasets from the UCI Machine Learning repository [37], with results available in the supplementary data for initial population and maximum iterations both set to 25.

Table 5  
Estimated Ranking for Requirement Value Assignment.

<table><tr><td>Objective</td><td>Function</td><td>Mobile features</td><td>Public geospatial features</td><td>Satellite features</td></tr><tr><td>Expected maximum profit (EMP)</td><td> $EMP = \int_{0}^{1}(b * \pi_{0}H_{0} - ROI * \pi_{1} H_{1}) * g(b)$  db/ max profit</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Number of features (cardinality)</td><td>(1 - p)/ max number of features</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Affordability</td><td>affordability, \( r_{1} = \sum_{q=1}^{3} source_{q} - (0.01 * variables)_{q}/ value with all features</td><td>2</td><td>3</td><td>1</td></tr><tr><td>Reliability</td><td>reliability, \( r_{2} = \sum_{q=1}^{p} rv_{q2}/value with all features</td><td>2</td><td>1</td><td>3</td></tr><tr><td>Collectability</td><td>collectability, \( r_{3} = \sum_{q=1}^{p} rv_{q3}/value with all features</td><td>1</td><td>3</td><td>2</td></tr></table>

## 5. Results

The two new algorithms, SelCrossMut NSBGOA and NSBGOA, were evaluated in comparison to existing multiple objective optimization methods, NSGA-II and NSGA-III. Ten runs of each algorithm were completed, and the average performance metrics are given in Fig. 1. From Fig. 1(c), it is observed that NSGOA and SelCrossMut NSBGOA produce the smallest hypervolumes, outperforming the existing methods. They also show a slight improvement in generational distance according to Fig. 1(a). In terms of distribution and spread, NSBGOA gives the highest spacing with the smallest overall pareto spread, which implies well distributed solutions within a smaller area. Meanwhile, SelCrossMut NSBGOA provides solutions which cover a greater area but have reduced spacing between them. This may be due to the selection, crossover, and mutation operations introduced to increase diversity.

The results given in Table 6 are the top non-dominated solutions from each algorithm. Computational time was measured for all algo rithms on a workstation with 16GB RAM and an Intel(R) Xeon(R) Silver 4112 CPU 4 core 2.6GHz processor, while the number of features per solution was averaged across all 10 runs. The average objective values are also given. For the average number of features per solution, NSBGOA produced the smallest value, and SelCrossMut NSBGOA the largest. SelCrossMut NSBGOA and NSGA-III take longer to compute. Addition ally, a linear regression model was trained on the objective values of the solutions obtained from all 10 runs of each algorithm according to eq. 21. This was to determine the empirical weights of the objectives among the final solutions and examine the balance between requirements. The objective weights are dominated by affordability, although NSBGOA, NSGA-III. and NSGA-II achieve a better balance of obiectives.

$$
1 = \mathrm{w} _ {1} \mathrm{r} _ {1} + \mathrm{w} _ {2} \mathrm{r} _ {2} + \mathrm{w} _ {3} \mathrm{r} _ {3} + \mathrm{w} _ {4} \mathrm{r} _ {4} + \mathrm{w} _ {5} \mathrm{r} _ {5}\tag{21}
$$

Table 7 gives results from 10 runs of the algorithms optimizing a single objective (EMP). It is apparent that LASSO and logistic regression have significantly shorter computational times. Yet, failing to include all the objectives led to poorly balanced objectives for LASSO and logistic regression, which provided extremely low values for cardinality despite high values for the other objectives. Meanwhile, GA had the greatest reduction in features (higher cardinality). Radar plots (Supplementary figure 1 Objective values for solutions with maximum EMP) give the max EMP solution for each algorithm, showing the improved balance of objectives due to use of multiple objectives.

![](/api/attachments/84VRUNG4/fulltext/images/bc473b2bef5e1a722e2d0495b04d2fda2ff95fda474888320040b98d612dd41d.jpg)  
(a)

![](/api/attachments/84VRUNG4/fulltext/images/3551c81673533705eb97bf9aecbd666e6fdf2587f03353776053f8fd183f5a84.jpg)  
(c)

## 6. Discussion

This research proposed two new algorithms for optimization of multiple objectives, as well as the use of stakeholder requirements for feature selection where alternative data is required for credit scoring. Existing multiple and single objective methods were evaluated in com parison to the proposed algorithms.

## 6.1. Practical considerations

Of the single objective algorithms, GA produced the best balance between objectives. However, this method can only produce one solu tion, giving stakeholders limited options for decision making. The multiple objective algorithms were efficient in reducing the number of features. However, this led to lower values for some objectives. This demonstrates the ability of multi-objective methods to balance several factors. Such methods may be advantageous in cases where the decisionmaker is willing to make slight sacrifices in other objectives to reduce the number of features, which could result in reduced data-acquisition costs. Furthermore, it should be noted that the multiple objective methods produce several non-dominated solutions or feature sets with different objective values for each. From a business perspective, these methods give the benefit of a posteriori decision-making. To apply these results, the decision-maker would consider the objective values obtained from each subset of features and select the final solution based on these objectives and priorities. The relevance of the features dropped out could also be an important additional consideration for decision makers.

The performance metrics such as spacing, spread, and time can guide the choice of algorithm for a given application. Maximizing spread and spacing while minimizing time is desirable. Further, as all objectives are

![](/api/attachments/84VRUNG4/fulltext/images/b227a3339c11e79212802cb0e783b5140f50c549f05fc6d56d202999caa12e24.jpg)  
(b)

![](/api/attachments/84VRUNG4/fulltext/images/c552b17b4924827f18ce6fede4f1c7401b8533318c17709c9753e5e174f01f1c.jpg)  
(d)  
Fig. 1. Results of multiple objective algorithms in 10 runs (a) generational distance, (b) spacing, (c) hypervolume, (d) overall pareto spread.

Table 6  
Summary results of multiple objective optimization.

<table><tr><td rowspan="2">Algorithm</td><td rowspan="2">Number of feature sets/run</td><td># of features/ solution</td><td colspan="2">Computational time (minutes)</td><td>Objective</td><td rowspan="2">Objective weights</td><td colspan="3">Objective values</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td><td></td><td>Mean</td><td>Standard deviation</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Emp</td><td>0.207</td><td>0.784</td><td>0.027</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Cardinality</td><td>0.709</td><td>0.46</td><td>0.106</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Affordability</td><td>0.153</td><td>1.056</td><td>0.028</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Reliability</td><td>0.379</td><td>0.466</td><td>0.103</td></tr><tr><td>NSGA2</td><td>50</td><td>38.1</td><td>7.4</td><td>29.184</td><td>2.895</td><td>Collectability</td><td>0.392</td><td>0.44</td><td>0.1</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Emp</td><td>0.295</td><td>0.77</td><td>0.02</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Cardinality</td><td>0.837</td><td>0.5</td><td>0.088</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Affordability</td><td>0.014</td><td>1.034</td><td>0.121</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Reliability</td><td>0.387</td><td>0.413</td><td>0.088</td></tr><tr><td>NSGA3</td><td>50</td><td>38.9</td><td>4.533</td><td>279.477</td><td>30.245</td><td>Collectability</td><td>0.458</td><td>0.393</td><td>0.084</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Emp</td><td>0.254</td><td>0.818</td><td>0.019</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Cardinality</td><td>0.765</td><td>0.499</td><td>0.07</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Affordability</td><td>0.038</td><td>1.055</td><td>0.061</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Reliability</td><td>0.435</td><td>0.455</td><td>0.065</td></tr><tr><td>NSBGOA</td><td>33</td><td>35.5</td><td>3.629</td><td>89.928</td><td>2.489</td><td>Collectability</td><td>0.39 $-2.86 \times 10^{-15}$ </td><td>0.441</td><td>0.066</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Emp</td><td> $10^{-15}$ </td><td>0.792</td><td>0.031</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Cardinality</td><td>-0.124</td><td>0.494</td><td>0.105</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Affordability</td><td>1.00 $-2.24 \times 10^{-15}$ </td><td>1.061</td><td>0.013</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Reliability</td><td> $10^{-15}$ </td><td>0.45</td><td>0.102</td></tr><tr><td>SelCrossMut</td><td></td><td></td><td></td><td></td><td></td><td></td><td> $4.04 \times 10^{-16}$ </td><td></td><td></td></tr><tr><td>NSBGOA</td><td>50</td><td>39.1</td><td>3.843</td><td>283.366</td><td>19.102</td><td>Collectability</td><td></td><td>0.439</td><td>0.099</td></tr></table>

Table 7  
Summary results of single objective optimization

<table><tr><td rowspan="2">Algorithm</td><td colspan="2"># of features/solution</td><td colspan="2">Computational time (minutes)</td><td colspan="3">Objective values</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td><td>Objective</td><td>Mean</td><td>Standard deviation</td></tr><tr><td rowspan="6">LASSO</td><td rowspan="6">60.1</td><td rowspan="6">1.449</td><td rowspan="6">3.236</td><td rowspan="6">0.292</td><td>Emp</td><td>0.901</td><td>0.008</td></tr><tr><td>Cardinality</td><td>0.089</td><td>0.022</td></tr><tr><td>Affordability</td><td>1.011</td><td>0.003</td></tr><tr><td>Reliability</td><td>0.807</td><td>0.021</td></tr><tr><td>Collectability</td><td>0.795</td><td>0.017</td></tr><tr><td>Emp</td><td>0.736</td><td>0.007</td></tr><tr><td rowspan="5">Logistic regression with all features</td><td rowspan="5">66</td><td rowspan="5">0</td><td rowspan="5">3.695</td><td rowspan="5">0.129</td><td>Cardinality</td><td>0</td><td>0</td></tr><tr><td>Affordability</td><td>1</td><td>0</td></tr><tr><td>Reliability</td><td>0.9</td><td>0</td></tr><tr><td>Collectability</td><td>0.872</td><td>0</td></tr><tr><td>Emp</td><td>0.868</td><td>0.011</td></tr><tr><td rowspan="4">Genetic Algorithm</td><td rowspan="4">32.3</td><td rowspan="4">3.057</td><td rowspan="4">29.502</td><td rowspan="4">3.536</td><td>Cardinality</td><td>0.511</td><td>0.046</td></tr><tr><td>Affordability</td><td>1.063</td><td>0.006</td></tr><tr><td>Reliability</td><td>0.458</td><td>0.042</td></tr><tr><td>Collectability</td><td>0.436</td><td>0.043</td></tr></table>

being maximized, a lower hypervolume is preferred in this case. The two proposed algorithms outperformed existing methods with regards to hypervolume and gave a slight improvement in generational distance, displaying better convergence. While SelCrossMut NSBGOA gave the best hypervolume and its solutions covered a greater area, its signifi cantly lengthier computational time and poor spacing pose a disad vantage. Similarly, the lengthy computational time required by NSGA-III coupled with its poor spread, hypervolume, and generational distance are a drawback. Meanwhile, NSBGOA offers a good balance of conver gence, distribution, spacing, feature reduction, and computational time. Importantly, it performs better than the existing NSGA-III on these metrics, and better than the existing NSGA-II on all but computational time. However, it gave poor spread. In practice, NSBGOA should be the preferred option where fewer, well-converged, well-spaced solutions were desired and overall spread was less important. Alternatively, NSGA-II would be acceptable where reducing computational time and increasing spread were more important.

From Tables 6 and 7, it is clear that affordability dominates the other objectives. This can be explained by the manner in which the objectives were modelled (Table 5). Since many of the solutions included at least one variable from each source and the bulk of the affordability objective was determined by the source of the data, affordability values were higher than the other objectives. This raises an important question about the assignment of requirement values on a group level versus an indi vidual level, which should be considered carefully by decision makers.

## 6.2. General implementation

The proposed process can be implemented by lenders in partnership with data collection companies. General application would require the necessary steps outlined in the proposed approach: stakeholder identi fication and analysis, collection of requirements, data identification and collection, and many objective feature selection. The empirical evalua tion conducted here involved loans to small holder farmers, which made data such as vegetation indices relevant. However, a different context would change the stakeholders and relevant data. The non-financial data sources can be adapted to other contexts provided the data collected has a relation to the income earning potential and, thus, the creditworthiness of the borrowers under consideration. In other words, variables that have a relation to the income of borrowers can be collected. For instance, if the target borrowers were small shop owners, relevant features may be proximity to main market and size of clientele. Further, although only profit, number of features, affordability, reli ability, and collectability were considered for this empirical evaluation, a practical case may employ a different set of requirements. For example, a stakeholder may be concerned with completeness of avail able features. As such, collecting stakeholder requirements for each application is important.

With the proposed process, the feature selection process is more transparent. Stakeholders can be made aware of all the criteria used for selection, and of the criteria values for the final selection. All re quirements are evaluated simultaneously, allowing decision makers to fully grasp the impact of the selections. Further, requirements that are assigned on a group level, rather than individual level, appear to dominate the other objectives. Therefore, it is recommended that for practical implementation, a group penalty function be incorporated into the objective functions for requirements with group level assignment of requirement values.

## 6.3. Legal and ethical considerations

The selection of alternative data requires several considerations in practice [38]. Chiefly, transparency and fairness are essential to prevent discrimination. Justification must be provided for each feature's rela tionship to the borrower's income, repayment ability, and willingness, with special care being taken to avoid features that may introduce bias. Ethics committees should be used to ensure this. Furthermore, as data from different sources may be needed, collaboration between different data collection companies may be necessary. Authorization from po tential borrowers, as well as data privacy and security should be ensured. Although the empirical evaluation conducted here focused on farmers, the proposed method may be utilized with target groups engaged in other economic activities who lack access to financial services.

## 7. Limitations

Solutions from each iteration go through non-dominated sorting with the best front selected for the next iteration (solutions chosen from the top of the fronts). Thus, some solutions in the same non-dominated front may have been excluded to maintain the population size. Although this process does not guarantee that the optimal Pareto Frontier will be found, it continuously searches and ensures that the best solutions from the search are selected. Further, the proposed algorithms may be tested on other datasets.

## 8. Conclusion

This research proposed the incorporation of stakeholder re quirements, modelled as objectives, into the feature selection process when credit scoring with alternative data. Additionally, two new algo rithms, SelCrossMut NSBGOA and NSBGOA, were suggested to conduct this selection and produce a non-dominated set of solutions. Empirical evaluation fitted these methods with stakeholder requirements when lending to rural farmers. The two proposed algorithms show promising results, outperforming existing methods on specific metrics. Sel CrossMut NSBGOA produced solutions with good spread and hyper volume although its lengthy computational time and poor spacing would be disadvantageous. In comparison to NSGA-III, NSBGOA had better convergence, spacing and computational time, but poor spread. Through the proposed method, stakeholder requirements were suc cessfully included in feature selection, resulting in a better balance be tween objectives. However, as a small dataset was used for empirical evaluation, future work should include further validation on a larger data set.

Supplementary data to this article can be found online at https://doi. org/10.1016/j.dss.2021.113714.

## Author contributions

Conceptualization, N.S., S.O., and N.K.;

methodology, N.S. and S.O.;

formal analysis, validation, visualization, writing original draft, N.S.; review and editing, S.O., A.K., and N.K.;

supervision, N.K.;

project administration and funding acquisition, A.K. and N.K.

All authors have read and agreed to the published version of the manuscript.

## Acknowledgments

The authors would like to thank Agribuddy Ltd. (www.agribuddy. com) for their kind assistance in providing data. This work was sup ported by the JSPS KAKENHI Grant [Grant Number JP19H04100], whose role was the provision of funding. The authors have no declara tions of interest to make.

## Appendix A. Related research

Comparison with existing research.

<table><tr><td>Research</td><td>Data</td><td>Criteria</td><td>Method</td><td>Feature selection</td></tr><tr><td>Maldonado et al. [13]</td><td>Financial</td><td>Cost</td><td>Mixed-Integer SVMLP Mixed-Integer SVM</td><td>Features have different group acquisition costs</td></tr><tr><td>Maldonado et al. [9]</td><td>Financial</td><td>Profit measure incorporating variable acquisition costs</td><td>SVM with  $L_{\infty}$ -norm penalty function for grouped feature selection</td><td>Features have different group acquisition costs</td></tr><tr><td>Djeundje et al. [6]</td><td>Non-financial:DemographicPsychometricEmail data</td><td>AUC</td><td>Principle component analysisLASSO and Ridge regression</td><td>Feature acquisition costs assumed to be uniform</td></tr><tr><td>Kozodoi et al. [11]</td><td>Financial</td><td>EMPNumber of features</td><td>NSGA-II</td><td>All features assumed to cost the same</td></tr><tr><td>Usman et al. [31]</td><td>Assorted benchmark datasets</td><td>Mutual InformationEntropy</td><td>Cuckoo Optimization Algorithm using NSGA-II and NSGA-III non dominated soring methods to handle two</td><td>All features assumed to cost the same</td></tr><tr><td>Mafarja et al. [19]</td><td>Assorted benchmark datasets</td><td>Classification error rateNumber of features</td><td>Binary GOA-M (with stochastic mutation)Binary GOA-S (with sigmoid function)</td><td>All features assumed to cost the same</td></tr></table>

Table A.1 (continued )

<table><tr><td>Research</td><td>Data</td><td>Criteria</td><td>Method</td><td>Feature selection</td></tr><tr><td>This research</td><td>Non-financial:SatelliteMobilePublic geospatial</td><td>EMP,number of features,Stakeholder Requirements</td><td>Binary GOA-V (with hyperbolic tangent function)NSBGOA (with non-dominated sorting and sigmoid function)SelCrossMut NSBGOA (NSBGOA with selection, crossover, and mutation)</td><td>Features have different individual acquisition costs</td></tr></table>

## Appendix B. Input data

Table B.1  
Input data variables.

<table><tr><td>Source</td><td>Feature</td><td>Details</td><td>Feature</td><td>Details</td></tr><tr><td>Loan</td><td>Loan default</td><td>Default: 43,Non default: 245</td><td></td><td></td></tr><tr><td rowspan="9">Mobile</td><td>User has uploaded family photo</td><td>No: 230, yes: 58</td><td>Number of activity reports</td><td>Mean: 1.965</td></tr><tr><td>User has uploaded Land Document Photos</td><td>No: 268, yes: 20</td><td>Number of harvest reports</td><td>Mean: 0.049</td></tr><tr><td>User has uploaded ID Photos</td><td>No: 225, yes: 63</td><td>Number of seeding reports</td><td>Mean: 7.708</td></tr><tr><td>User has uploaded photo with house</td><td>No: 225, yes: 63</td><td>Number of tractor reports</td><td>Mean: 0.358</td></tr><tr><td>User gender</td><td>Male: 107, female: 181</td><td>Number of trouble reports</td><td>Mean: 0.309</td></tr><tr><td>Number of reports sent by user on app</td><td>Mean: 10.389</td><td>Period active in days</td><td>Mean: 44.333</td></tr><tr><td>Number of farms user reported from</td><td>Mean: 2.198</td><td>Mean time of day report sent</td><td>Mean: 06:21:39</td></tr><tr><td>Number of farms registered by user</td><td>Mean: 32.319</td><td>Earliest time of day report sent</td><td>Mean: 09:40:00</td></tr><tr><td>Number of days user has been active</td><td>Mean: 2.958</td><td>Latest time of day report sent</td><td>Mean: 14:00:30</td></tr><tr><td rowspan="5">Public geospatial</td><td>Farm is within 1 km of canal</td><td>No: 138, yes: 150</td><td>farm is within 5 km of road</td><td>No: 16, yes: 272</td></tr><tr><td>Farm is within 2 km of canal</td><td>No: 95, yes: 193</td><td>farm is within 1 km of river</td><td>No: 265, yes: 23</td></tr><tr><td>Farm is within 5 km of canal</td><td>No: 58, yes: 230</td><td>farm is within 2 km of river</td><td>No: 239, yes: 49</td></tr><tr><td>Farm is within 1 km of road</td><td>No: 150, yes: 138</td><td>farm is within 5 km of river</td><td>No: 148, yes: 140</td></tr><tr><td>Farm is within 2 km of road</td><td>No: 107, yes: 181</td><td></td><td></td></tr><tr><td rowspan="20">Satellite</td><td>3 year mean january temperature</td><td>Mean: 15114.982</td><td>3 year mean september ndvi</td><td>0.662</td></tr><tr><td>3 year mean february temperature</td><td>Mean: 15244.503</td><td>3 year mean october ndvi</td><td>0.637</td></tr><tr><td>3 year mean march temperature</td><td>Mean: 15451.226</td><td>3 year mean november ndvi</td><td>0.581</td></tr><tr><td>3 year mean april temperature</td><td>Mean: 15565.771</td><td>3 year mean december ndvi</td><td>0.591</td></tr><tr><td>3 year mean may temperature</td><td>Mean: 15396.334</td><td>3 year mean january ndwi</td><td>-0.042</td></tr><tr><td>3 year mean june temperature</td><td>Mean: 15305.008</td><td>3 year mean february ndwi</td><td>-0.089</td></tr><tr><td>3 year mean july temperature</td><td>Mean: 15224.351</td><td>3 year mean march ndwi</td><td>-0.093</td></tr><tr><td>3 year mean august temperature</td><td>Mean: 15184.259</td><td>3 year mean april ndwi</td><td>-0.071</td></tr><tr><td>3 year mean september temperature</td><td>Mean: 15140.049</td><td>3 year mean may ndwi</td><td>-0.034</td></tr><tr><td>3 year mean october temperature</td><td>Mean: 15093.496</td><td>3 year mean june ndwi</td><td>-0.001</td></tr><tr><td>3 year mean november temperature</td><td>Mean: 15065.239</td><td>3 year mean july ndwi</td><td>0.022</td></tr><tr><td>3 year mean december temperature</td><td>Mean: 15049.27</td><td>3 year mean august ndwi</td><td>0.024</td></tr><tr><td>3 year mean january ndvi</td><td>Mean: 0.555</td><td>3 year mean september ndwi</td><td>0.044</td></tr><tr><td>3 year mean february ndvi</td><td>Mean: 0.454</td><td>3 year mean october ndwi</td><td>0.053</td></tr><tr><td>3 year mean march ndvi</td><td>Mean: 0.390</td><td>3 year mean november ndwi</td><td>0.032</td></tr><tr><td>3 year mean april ndvi</td><td>Mean: 0.390</td><td>3 year mean december ndwi</td><td>-0.004</td></tr><tr><td>3 year mean may ndvi</td><td>Mean: 0.503</td><td>Mean night light radiance</td><td>0.015</td></tr><tr><td>3 year mean june ndvi</td><td>Mean: 0.581</td><td>Farm elevation</td><td>40.844</td></tr><tr><td>3 year mean july ndvi</td><td>Mean: 0.629</td><td>Farm slope</td><td>0.866</td></tr><tr><td>3 year mean august ndvi</td><td>Mean: 0.644</td><td></td><td></td></tr></table>

## References

[1] L.C. Thomas, D.B. Edelman, J.N. Crook, Credit Scoring and its Applications, Society for Applied and Industrial Mathematics, Philadelphia, 2002.

[2] Robinson+Yu, Knowing the Score: New Data, Underwriting, and Marketing in the Consumer Credit Marketplace [Online]. Available: https://www.upturn.org/stati c/files/Knowing the Score Oct 2014 v1 1.pdf, 2014.

[3] A. Demirgüç-Kunt, L. Klapper, D. Singer, S. Ansar, J. Hess, The Global Findex Database, Washington DC, USA, 2017.

[4] A. Costa, A. Deb, M. Kubzansky, Big data, small credit: the digital revolution and its impact on emerging market consumers, Innov. Technol. Governance, Glob. 10 (3–4) (2015) 49–80, https://doi.org/10.1162/inov\_a\_00240.

[5] N. Simumba, S. Okami, A. Kodaka, N. Kohtake, Spatiotemporal integration of mobile, satellite, and public geospatial data for enhanced credit scoring, SS Symmetry 13 (575) (2021).

[6] V.B. Djeundje, J. Crook, R. Calabrese, M. Hamid, Enhancing credit scoring with alternative data, Expert Syst. Appl. 163 (2021), 113766, https://doi.org/10.1016/ j.eswa.2020.113766.

[7] Hu Yue, T. Ziyi, In depth: want a loan? China's tech giants are at your service, Nikkei. https://asia.nikkei.com/Spotlight/Caixin/In-depth-Want-a-loan-China-s-te ch-giants-are-at-your-service.

[8] K. Kaul, Housing and Housing Finance, Urban Institute, 2021. https://www.urban. org/urban-wire/adopting-alternative-data-credit-scoring-would-allow-millions-co nsumers-access-credit (accessed Sep. 14, 2021).

[9] S. Maldonado, C. Bravo, J. Lopez, ´ J. P´erez, Integrated framework for profit-based feature selection and SVM classification in credit scoring, Decis. Support. Syst. 104 (2017) 113–121, https://doi.org/10.1016/j.dss.2017.10.007.

[10] I. Guyon, M. Nikravesh, S. Gunn, L.A. Zadeh (Eds.), Feature Extraction, Foundations and Applications, Springer Berlin Heidelberg, Berlin, 2006

[11] N. Kozodoi, S. Lessmann, K. Papakonstantinou, Y. Gatsoulis, B. Baesens, A multi objective approach for profit-driven feature selection in credit scoring, Decis. Support. Syst. 120 (January) (2019) 106–117, https://doi.org/10.1016/j. dss.2019.03.011.

[12] S. Lessmann, B. Baesens, H.V. Seow, L.C. Thomas, Benchmarking state-of-the-art classification algorithms for credit scoring: an update of research. Eur. J. Oper. Res 247 (1) (2015) 124–136., https://doi.org/10.1016/i.eior,2015.05.030.

[13] S. Maldonado, J. P´erez, C. Bravo, Cost-based feature selection for support vector machines: an application in credit scoring, Eur. J. Oper. Res. 261 (2) (2017) 656–665. https://doi,org/10.1016/i.eior,2017.02.037

[14] M.T.M.E. Andre, A tutorial on multiobjective optimization : fundamentals and evolutionary methods, Nat. Comput. (2018), https://doi.org/10.1007/s11047- 018-9685-y.

[15] SE Handbook Working Group, Systems Engineering Handbook, International Council on Systems Engineering, San Diego, California, USA, 2011.

[16] S. Saremi, S. Mirjalili, A. Lewis, Advances in engineering software grasshopper optimisation algorithm : theory and application, Adv. Eng. Softw. 105 (2017) 30–47, https://doi.org/10.1016/j.advengsoft.2017.01.004.

[17] S. Khan, M. Asjad, A. Ahmad, Review of modern optimization techniques, Int. J. Eng. Tech. Res. (April) (2015), https://doi.org/10.17577/IJERTV4IS041129.

[18] H. Hichem, M. Elkamel, M. Rafik, M.T. Mesaaoud, C. Ouahiba, A new binary grasshopper optimization algorithm for feature selection problem, J. King Saud Univ. - Comput. Inf. Sci (2019), https://doi.org/10.1016/j.jksuci.2019.11.007.

[19] M. Mafarja, I. Aljarah, H. Faris, A.I. Hammouri, A.M. Al-zoubi, S. Mirjalili, Binary grasshopper optimisation algorithm approaches for feature selection problems, Expert Syst. Appl. 117 (2019) 267–286, https://doi.org/10.1016/j. eswa.2018.09.015.

[20] International Bank for Reconstruction and Development, Mobile Technologies and Digitized Data to Promote Access to Finance for Women in Agriculture, Washington D.C, World Bank Group, 2017.

[21] M. Oskarsd<sup>´</sup> ottir, ´ C. Bravo, C. Sarraute, J. Vanthienen, B. Baesens, The value of big data for credit scoring: enhancing financial inclusion using mobile phone data and social network analytics, Appl. Soft Comput. J. 74 (October) (2019) 26–39, https:/ doi.org/10.1016/i.asoc.2018.10.004.

[22] A. Blanco, R. Pino-Mejías, J. Lara, S. Rayo, Credit scoring models for the microfinance industry using neural networks: evidence from Peru, Expert Syst Appl. 40 (1) (2013) 356–364, https://doi.org/10.1016/j.eswa.2012.07.051.

[23] T. Verbraken, C. Bravo, R. Weber, B. Baesens, Development and application of consumer credit scoring models using profit-based classification measures, Eur. J. Oper. Res. 238 (2) (2014) 505–513, https://doi.org/10.1016/j.ejor.2014.04.001.

[24] G.O. Odu, O.E. Charles-Owaba, Review of multi-criteria optimization methods – theory and applications, IOSR J. Eng. 3 (10) (2013) 01–14, https://doi.org 10.9790/3021-031020114.

[25] Y. Censor, Pareto optimality in multiobjective problems, Appl. Math. Optim. 4 (1) (1977) 41–59, https://doi.org/10.1007/BF01442131.

[26] A. Ghosh, Evolutionary algorithms for multi-criterion optimization: a survey, Int. J. Comput, Inform, Sci, 2 (1) (2004) 38–57

[27] A. Kishor, P.K. Singh, J. Prakash, Neurocomputing NSABC : non-dominated sorting based multi-objective arti fi cial bee colony algorithm and its application in data clustering, Neurocomputing 216 (2016) 514–533, https://doi.org/10.1016/j. neucom.2016.08.003.

[28] U.F. Siddiqi, S.M. Sait, An optimization heuristic based on non-dominated sorting and Tabu search for the fixed Spectrum frequency assignment problem, IEEE Access 6 (2018) 72635–72648, https://doi.org/10.1109/ACCESS.2018.2882595.

[29] T. Wagner, N. Beume, B. Naujoks, Pareto-, aggregation-, and indicator-based methods in many-objective optimization, Lect. Notes Comput. Sci. (including Subser. Lect. Notes Artif, Intell. Lect, Notes Bioinformatics) 4403 LNCS (2007) 742–756. https://doi.org/10.1007/978-3-540-70928-2 56.

[30] B. Li, J. Li, K. Tang, X. Yao, Many-objective evolutionary algorithms: a survey, ACM Comput. Sury. 48 (1) (2015). https://doi.org/10.1145/2792984.

[31] A.M. Usman, U.K. Yusof, S. Naim, Filter-Based Multi-Objective Feature Selection Using NSGA III and Cuckoo Optimization Algorithm, IEEE, 2020, https://doi.org 10.1109/ACCESS.2020.2987057 no. April.

[32] B. Bonev, F. Escolano, M. Cazorla, Feature selection, mutual information, and the classification of high-dimensional patterns, Pattern. Anal. Applic. 11 (309–319) (2008), https://doi.org/10.1007/s10044-008-0107-0.

[33] R. Tibshirani, Regression shrinkage and selection via the lasso: a retrospective, J. R. Stat. Soc. 73 (3) (2011) 273–282

[34] B. Xue, L. Cervante, L. Shang, M. Zhang, A particle swarm optimisation based multi-obiective filter approach to feature selection for classification. in: PRICAI 2012: Trends in Artificial Intelligence. PRICAI 2012. Lecture Notes in Computer Science, 2012, https://doi.org/10.1007/978-3-642-32695-0 no. 7458.

[35] C. Audet, J. Bigeon, D. Cartier, S. Le Digabel, L. Salomon, Performance indicators in multiobjective optimization, Eur. J. Oper. Res. 292 (2) (2021) 397–422.

[36] World Bank Group, “Financial inclusion,” Global Financial Development Report 2014, Washington DC, 2014.

[37] UCI Machine Learning Repository Datasets. https://archive.ics.uci.edu/ml/dataset s.php (accessed Oct. 01, 2021).

[38] M. Hurley, J. Adebayo, Credit scoring in the era of big data, Yale J. Law Technol. Artic 18 (1) (2017).

Naomi Simumba is PhD candidate at the Graduate School of System Design and Man agement at Keio University, where she is also employed as a research associate. She conducts research on the use of machine learning and geospatial analysis for a range of social issues. She holds a bachelors' degree in Electrical and Electronics Engineering and a masters' degree in Systems Engineering.

Dr. Suguru Okami is a graduate of the Graduate School of System Design and Manage ment at Keio University. He is currently the Group Manager of Evidence and Observational Research at an international firm.

Dr. Akira Kodaka currently works at the Graduate School of System Design and Man agement, Keio University as a Project Senior Assistant Professor. He conducts research on Disaster Risk Reduction of Area-BCM and Systems Engineering. He holds a PhD from the University of Tokyo.

Professor Naohiko Kohtake is a professor and current head of the Sensing and Design Laboratory and the Sports System Design and Management Laboratory at the Graduate School of System Design and Management at Keio University where he is responsible for space system engineering and intelligent systems. He has worked in research and devel opment on avionics systems for the H-II/H-IIA rocket at Japan Aerospace Exploration Agency (JAXA) and on-board software at European Space Agency. He is a steering com mittee member of Multi-GNSS Asia consortium and Sentinel Asia Project, and an adviser of Quasi-Zenith Satellite System Business Innovation Council. He is also adjunct associate professor, Asian Institute of Technology, Thailand.
