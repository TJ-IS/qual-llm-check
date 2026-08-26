---
otero_id: 7410
otero_key: "AY5R9TTG"
title: "A multi-objective approach for profit-driven feature selection in credit scoring"
authors: "Nikita Kozodoi; Stefan Lessmann; Konstantinos Papakonstantinou; Yiannis Gatsoulis; Bart Baesens"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.03.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A multi-objective approach for profit-driven feature selection in credit scoring

![](/api/attachments/AY5R9TTG/fulltext/images/71b08ea85c75d2d96e7e6d9573e48ef2a1d4f081fbc60945cfdc521346218402.jpg)

Nikita Kozodoi<sup>a,b</sup>, Stefan Lessmann<sup>a</sup>, Konstantinos Papakonstantinou<sup>b</sup>, Yiannis Gatsoulis<sup>b</sup>, Bart Baesens<sup>c,</sup>

<sup>a</sup> Humboldt University of Berlin, Berlin, Germany

<sup>b</sup> Kreditech, Hamburg, Germany

<sup>c</sup> Catholic University of Leuven, Leuven, Belgium

## A R T I C L E I N F O

Keywords: Feature selection Multi-objective optimization Credit scoring Profit maximization Genetic algorithm

## A B S T R A C T

In credit scoring, feature selection aims at removing irrelevant data to improve the performance of the scorecard and its interpretability. Standard techniques treat feature selection as a single-objective task and rely on statistical criteria such as correlation. Recent studies suggest that using profit-based indicators may improve the quality of scoring models for businesses. We extend the use of profit measures to feature selection and develop a multi-objective wrapper framework based on the NSGA-II genetic algorithm with two fitness functions: the Expected Maximum Profit (EMP) and the number of features. Experiments on multiple credit scoring data sets demonstrate that the proposed approach develops scorecards that can yield a higher expected profit using fewer features than conventional feature selection strategies.

## 1. Introduction

Credit scoring refers to the use of statistical models that guide managerial decisions in the retail credit sector [12]. This sector has gained a considerable economic value: in 2017, consumer credit outstandings reached €1195 billion in EU.<sup>1</sup> In the US, the total outstanding consumer credit amount exceeded \$3831 billion.<sup>2</sup> At the same time, the delinquency rate on consumer loans by commercial banks experienced a growth of more than 11% since 2015.<sup>3</sup> The rise of default rates emphasizes the importance of accurately deciding upon loan provisioning, which is a task of credit scoring. To distinguish defaulters and nondefaulters, financial institutions deploy binary scoring models (i.e., scorecards) that predict the probability of default (PD) – an applicant's willingness and ability to repay debt [39].

Data-driven models, which are used to score applicants, require fi nancial institutions to face costs of gathering and storing large amounts of data on customer behavior. At the same time, companies are required to comply with regulations (i.e., the Basel Accords and IFRS 9) that enforce comprehensible scoring models. By removing irrelevant and redundant features, feature selection can reduce costs and improve the model performance and its comprehensibility (interpretability).

Feature selection can be considered as a multi-objective problem with conflicting goals. In credit scoring, these goals are: increasing the model profitability, reducing the data acquisition costs and improving the interpretability of the model. Yet, most existing approaches in machine learning literature treat feature selection as a single-objective task [5,11,45].

Standard feature selection techniques use statistical criteria to identify the optimal subset of features. Recent credit scoring literature criticized a widespread practice of using standard performance measures such as area under the receiver operating characteristic curve (AUC) for evaluating scoring models [20] and call for profit-based performance indicators [15,40]. This finding stresses the importance of using value-oriented feature selection strategies that identify the optimal subset of features in a profit-maximizing manner.

The goal of this paper is to design a feature selection framework for credit scoring that overcomes some of the drawbacks of traditional feature selection techniques. The proposed method selects features in a profit-maximizing manner rather than relying on statistical measures and addresses both profitability and comprehensibility with multi-cri teria optimization. We use the recently developed Expected Maximum Profit (EMP) measure to evaluate the model profitability [40]. Previous research has applied EMP for model selection but did not consider profit maximization at the feature selection stage. We also use the number of features as an indicator of model comprehensibility and data-related costs: minimizing the number of features reduces costs on data acquisition and storage and makes the model more comprehen sible [32]. To simultaneously address both objectives, we employ a multi-objective feature selection framework based on the non-dominated sorting-based genetic algorithm (NSGA-II) [13] with two fitness functions: EMP and the number of features. The proposed method generates a frontier of non-dominated solutions, which represents a trade-of between two objectives and can, therefore, aid decision-makers in selecting a suitable solution. To validate the efectiveness of our approach, we conduct empirical experiments on ten real-world credit scoring data sets.

The contribution of this paper is three-fold. First, we introduce a profit-centric feature selection framework by using the EMP measure as a fitness function, thereby extending the use of EMP to feature selection. Second, we employ a multi-objective feature selection framework based on the NSGA-II algorithm. To the best of our knowledge, the specific combination of multi-objective feature selection based on scorecard profitability and parsimony using NSGA-II is originally proposed here and extends previous work in the credit scoring literature. Third, we provide empirical evidence that the proposed multi-objective feature selection technique identifies feature subsets that deliver the same or higher expected profit using fewer features than conventional feature selection strategies.

The remainder of this paper is organized as follows. Section 2 reviews related literature on feature selection methods and describes previous work on profit-driven credit scoring. In Section 3, we present and explain the proposed multi-objective feature selection framework. Section 4 describes our experimental setup and presents the empirical results. In Section 5, we discuss the main conclusions of our study.

## 2. Theoretical background

## 2.1. Feature selection

Feature selection is a dimensionality reduction technique that aims at selecting a subset of features from the input data by removing irrelevant, redundant or noisy features while maintaining the model performance [16]. Feature selection methods split into three groups: filters, wrappers and embedded methods [17].

Filters perform feature selection based on some general data char acteristics before training the model. On the first stage, all features are ranked according to a certain criterion that describes the relevance of a particular feature. Popular measures include feature-to-target correlation [5], mutual information [11], Fisher score [8] and others. In the second stage, a certain percentage of the top-ranked features is selected, whereas features with lower importance are dropped from the model. Compared to other feature selection strategies, filters are fast and efi cient. However, they were shown to perform poorly in benchmark studies [17].

Wrappers are algorithms that iteratively process diferent feature subsets and select the optimal subset based on the model performance. Since evaluating all possible feature combinations is computationally expensive, research has suggested multiple heuristic search strategies. Popular approaches are sequential forward selection (SFS) and sequential backward selection (SBS) [17]. SFS starts with an empty model and iteratively adds features, selecting the one which brings the largest performance gain, whereas SBS starts with a full set of features and eliminates those contributing the least to the model performance. The search is continued until there is no further improvement. Another strategy relies on evolutionary algorithms such as genetic algorithms (GA), particle swarm optimization (PSO) and others [46]. GAs operate on a population of individuals, where each individual represents a model with binary genes indicating the inclusion of specific features. At each generation, a new population is created by selecting individuals according to their fitness (model performance), recombining them together and undergoing mutation. The model with the highest fitness is selected after running the algorithm for multiple generations.

Embedded methods conduct feature selection simultaneously with the model training. One of the popular approaches is L1-regularized regression that performs feature selection by assigning zero coeficients to irrelevant features in the process of the model development [42]. The main drawback of embedded methods is that they can only be applied within a specific model class.

Most existing feature selection techniques consider feature selection as a single-objective task. However, conflicting goals of feature selection (optimizing the model performance and minimizing the number of selected features) suggest that it can be treated as a multi-objective optimization problem. The literature on multi-objective feature selection is limited compared to the research on conventional single-objective techniques. Nevertheless, there exist a number of attempts to employ the multi-criteria optimization frameworks.

One of the approaches to perform multi-criteria feature selection is to convert a problem into a single-objective task by aggregating the weighted objectives into a single fitness function. For instance, Bolón-Canedo and colleagues propose adding a new term to the evaluation function of well-known filter methods such as correlation-based feature selection, Minimal-Redundancy-Maximal-Relevance and RelieF [6,7]. The new term represents a number of features or their cost, which ensures that two objectives are included in the fitness function. A major downside of this approach is the requirement to explicitly assign weights to objectives, which is a challenging task given uncertainty and diferent scales of the objectives.

Another approach to account for multiple objectives is to consider a single-objective optimization problem with a budget constraint. In some studies, researchers suggest minimizing the number of features given that a certain level of performance is achieved [3,33], whereas others optimize predictive performance under the budget constraint for the cost of included features [29]. Both these directions require setting a specific threshold to introduce a budget constraint, either for the model performance or for the number of used features. Therefore, the application of this approach is problematic in cases with no hard budget constraints.

A more promising strategy is to consider objectives separately and look for a set of non-dominated solutions that are optimal in terms of multiple objectives instead of focusing on a single solution. The set of non-dominated points is also known as the Pareto eficient frontier and represents points, for which one cannot improve on one objective without decreasing the other. Literature proposed multi-objective modifications of the well-known evolutionary algorithms such as GA and PSO that rely on multiple fitness functions to perform a search of the non-dominated solutions. Emmanouilidis et al. used a two-objective genetic algorithm to perform feature selection that minimizes the number of features and optimizes the error rate or RMSE for classification and regression on diferent data sets [14]. More recent studies use modified versions of multi-objective genetic algorithms including the Strength Pareto Evolutionary Algorithm (SEPA-II) and the Non-Dominated Sorting Genetic Algorithm(NSGA-II) [18,36] to perform feature selection with the same objectives. Research has also suggested using other evolutionary algorithms such as PSO [44] and Artificial Bee Colony (ABC) [19].

The first attempt to perform profit-driven feature selection has been applied in customer churn [25] within the embedded framework for holdout support vector machines (HOSVM), where the authors use multiple metrics for customer churn to select features. The authors also extended their approach to credit scoring [27] by introducing the L infinity norm as a group penalty function to perform cost-based feature selection while training the SVM classifier. In [26], they also use the EMP measure to tune SVM parameters in a profit-maximizing manner. The studies conclude that the developed framework outperforms con ventional feature selection techniques in terms of profit.

The approach proposed in this paper difers from the framework suggested in [26,27] in two important dimensions. First, the latter balance three objectives: Euclidean norm minimization, group penalization for feature selection and hinge loss minimization. This way, the techniques in [26,27] do not provide a Pareto frontier with non dominated solutions in terms of the considered objectives. Producing a corresponding frontier of non-dominated solutions with respect to the trade-of between scorecard profitability and parsimony is a goal of this study. Insights into this trade-of will help risk analysts to make informed decisions how many variables to use for a scorecard, which, fo example in the case where variables are purchased from external entities such as credit bureaus, has wider reaching benefits related to the costs of data acquisition. Second, the approaches proposed in [26,27] qualify as embedded feature selection frameworks that can only be applied within an SVM classifier. Recent benchmarking studies in credit scoring suggest that alternative classifiers and tree-based ensemble methods in particular might perform better than SVMs in consumer credit scoring [23]. Given these results, developing a model-agnostic feature selection approach that can be used with any classifier and that facilitates optimizing both profitability and model comprehensibility contributes to the literature.

## 2.2. Profit-oriented credit scoring

The credit scoring task is commonly expressed as a classification problem, where a predictive model learns to diferentiate between bad risks (defaulters) and good risks (repayers). Traditional machine learning algorithms are designed to optimize statistical measures such as mean squared error. In recent years, credit scoring literature proposed diferent strategies to introduce the profit maximization to the scorecard development. One approach is to modify the target variable to reflect profitability. For instance, Serrano-Cinca et al. suggest using the internal rate of return based on the loan interest [34]. Finlay proposes estimating a contribution of each applicant to the profit of the financial institution [15]. Both these measures imply replacing a binary default indicator by a continuous target variable and therefore transform a classification problem into a regression task.

Another approach toward profit scoring is based on using profit related performance measures for model selection. Recently, Verbraken and colleagues suggested the Expected Maximum Profit (EMP) measure [40]. The calculation of EMP is based on costs and benefits that arise as a result of the actions the company undertakes. To illustrate the calculation process, we follow their notation and label defaulters as class 0 and non-defaulters as class 1. The scorecard assigns a score to each applicant that expresses the probability of default. Applicants are then considered as bad risks and rejected if the estimated credit score ex ceeds a cutoff value t. Table 1 provides a confusion matrix with the corresponding class probabilities, where π are prior probabilities of good and bad loans, and F (t) are predicted cumulative density functions of the scores of class i.

Confusion matrix with costs.

<table><tr><td rowspan="2">Actual label</td><td colspan="2">Predicted label</td></tr><tr><td>Bad risk</td><td>Good risk</td></tr><tr><td>Bad risk</td><td> $\pi_0F_0(t)$ benefit: B</td><td> $\pi_0(1 - F_0(t))$ cost: 0</td></tr><tr><td>Good risk</td><td> $\pi_1F_1(t)$ cost: C</td><td> $\pi_1(1 - F_1(t))$ cost: 0</td></tr></table>

The EMP measure assumes that in the basic scenario no scoring mechanism is implemented and therefore all loans are granted. Hence, if an applicant is predicted as a good risk, no additional costs or benefit are observed. In contrast, if an applicant is predicted to be a defaulter, the company faces cost C in case of an incorrect prediction and gets benefit B from an accurate prediction. The methodology to calculate parameters B and C was developed by [9].

Parameter B is the benefit from correctly identifying a bad risk. By not providing a loan to a defaulter, the company saves money that would be lost in case of issuing the loan. This amount is the expected loss in case of default:

$$
B = \frac {L G D \cdot E A D}{A},\tag{1}
$$

where LGD refers to the loss given default, EAD is the exposure at default, and A is the principal of the loan [28]. Since recovery rates for defaulted loans vary heavily [35], B is considered as a random variable, which can take values between 0 and 1. The following probability distribution is assumed:

• B = 0 with probability p (a customer repays the entire loan)

• B = 1 with probability p (a customer defaults on the entire loan)

• B follows a uniform distribution in (0, 1) with $F ( B ) = 1 - p _ { 0 } - p _ { 1 }$

Parameter C is the cost of the incorrect classification of good risks. By rejecting a good customer, the company loses money that could be earned as return on investment:

$$
C = \mathrm{ROI} = \frac {I}{A},\tag{2}
$$

where I is the total interest. Verbraken et al. [40] treat parameter C as constant and that we follow their approach in this paper. Given these parameters, the EMP measure can be computed as:

$$
\mathrm{EMP} = \int_ {0} ^ {1} [ B \cdot \pi_ {0} F _ {0} (t) - C \cdot \pi_ {1} F _ {1} (t) ] f (B) d (B)\tag{3}
$$

EMP can be interpreted as the incremental profit from deciding on credit applications using a scorecard compared to a baseline scenario where credits are granted without screening. In this paper, we use EMP to measure the profitability of the scorecard. Furthermore, we rely on the EMP measure as one of the optimization objectives to enable profitdriven feature selection.

The literature on profit-oriented credit scoring focuses on model selection and parameter estimation but does not pay suficient attention to the feature selection stage. Current research on profit-driven feature selection in credit scoring is limited to the embedded regularization framework for SVMs [26,27] described above. This paper proposes a model-agnostic profit-driven feature selection approach that optimizes both profitability and model comprehensibility.

## 3. Proposed profit-driven feature selection approach

We treat feature selection as a multi-objective problem with two goals: a) maximizing the performance of the scorecard; b) minimizing the number of used features used by the model. We propose a wrapper method based on the binary multi-objective nondominated sorting based genetic algorithm (NSGA-II) with two fitness functions: EMP and number of features. The suggested approach addresses two issues with traditional feature selection techniques in credit scoring: it relies on a profit-driven indicator rather than statistical performance measures and addresses both profitability and model comprehensibility by employing multi-objective optimization.

NSGA-II is a multi-objective evolutionary algorithm developed by [13] to address disadvantages of the previous version of NSGA [37]. NSGA-II is designed to solve multi-objective optimization problems by finding a set of non-dominated solutions which form the eficient Pareto frontier. Experiments on diferent test problems have shown that NSGA-II is able to maintain a better spread of solutions and convergence compared to some other multi-objective optimizers [13].

NSGA-II consists of three main stages: fast non-dominated sorting, diversity preservation and population update. First, the initial popula tion of n individuals is generated with random gene values. In the case of feature selection, each individual represents a set of features included in the predictive model. We code a population of individuals with a set of binary genes with each gene representing the inclusion of a certain feature in the scorecard.

Second, we compute fitness values for the considered objective functions. For each individual in the current population, we construct a scoring model with a diferent set of features, which is defined by the gene values of these individuals. We evaluate the performance of the scorecard in terms of EMP and store EMP and the number of selected features as two fitness values.

On the next stage, the population goes through the usual genetic operators: selection, crossover and mutation. The selection is performed with a binary tournament method based on the crowded comparison operator. First, we sort the population by a non-domination rank – the number of individuals dominated by a given solution in terms of the considered objective functions. Next, individuals with the same nondomination ranks are sorted by their crowding distance – the average distance of two solutions on either side of this individual along each of the objectives. Next, one-point crossover is applied to the remaining population. Gene values of the child are computed as a weighted average of the gene values of the parents. In a binary NSGA-II, which is the focus of this paper, a one-point crossover operator simply copies parents' genes if they are the same and randomly chooses a binary value for the conflicting genes. Finally, each gene of the child is flipped with a mutation probability m. These operations are performed until the size of the ofspring population reaches n.

After applying all genetic operations, both parents and children are merged into the new population of size 2n to ensure elitism. The population is again sorted according to the non-domination and crowding distance. After the sorting is complete, only the top n individuals are selected to proceed to the next stage. This approach helps the algorithm to construct a uniformly spread-out Pareto-optimal frontier by elim inating solutions that are either dominated or located in the crowded regions of the frontier.

The NSGA-II algorithm was previously used for feature selection in fields not related to credit risk. The fitness functions considered in the literature are the number of features and statistical performance measures such as error rate or mean squared error [18,31,36]. In credit risk, NSGA-II has only been applied to a bank-loan portfolio selection problem [30], where the algorithm is used to optimize portfolio return and risk. In this paper, we rely on the NSGA-II algorithm to perform multi objective feature selection for credit scoring. The central novelty of our approach is the use of a profit measure as one of the fitness functions within a multi-objective feature selection framework.

## 4. Experimental results

## 4.1. Data description

The empirical evaluations are based on ten retail credit scoring data sets coming from diferent sources. Data sets australian and german stem from the UCI Repository [24]. The data sets pakdd, lending club and gmsc were provided by diferent companies for the data mining competitions on PAKDD and Kaggle platforms. Data sets bene1, bene2 and uk were collected from financial institutions in the Benelux and UK [1]. The thomas data set is provided by [38]. Finally, hmeq is a data set on home equity loans collected by [2].

Each of the data sets has a unique set of features describing the loan applicant (e.g., gender, income) and loan characteristics (e.g., amount, duration). Some data sets also include information on previous loans of the applicant. The target variable is a binary indicator of whether the customer has repaid the loan or not. Table 2 summarizes the main characteristics of the data sets.

Table 2  
Credit scoring data sets.

<table><tr><td>Data label</td><td>Sample size</td><td>No.  $features^*$ </td><td>Default rate</td></tr><tr><td>australian</td><td>690</td><td>42</td><td>0.4449</td></tr><tr><td>german</td><td>1000</td><td>61</td><td>0.3000</td></tr><tr><td>thomas</td><td>1225</td><td>28</td><td>0.2637</td></tr><tr><td>bene1</td><td>3123</td><td>83</td><td>0.3333</td></tr><tr><td>hmeq</td><td>5960</td><td>20</td><td>0.1995</td></tr><tr><td>bene2</td><td>7190</td><td>28</td><td>0.3000</td></tr><tr><td>uk</td><td>30,000</td><td>51</td><td>0.0400</td></tr><tr><td>lending club</td><td>43,344</td><td>206</td><td>0.1351</td></tr><tr><td>pakdd</td><td>50,000</td><td>373</td><td>0.2608</td></tr><tr><td>gmsc</td><td>150,000</td><td>68</td><td>0.0668</td></tr></table>

\*Number of features after data preprocessing (see Section 4.2).

As suggested by Table 2, most of the data sets are imbalanced: default rate fluctuates between 4% and 44%. The sample size and number of features varies significantly across the data sets, which suggests that we use a heterogeneous data library for further analysis.

## 4.2. Experimental setup

Our modeling pipeline consists of several stages. First, each data set is pre-processed in the same way. We impute missing values with means for continuous features and with most frequent values for categorical features. Next, we encode all categorical features with k-1 dummies, where k is the number of unique categories.

After preprocessing, the data sets are randomly partitioned into two subsets: training sample (70% cases) and holdout sample (30%). On the training set, we use 4-fold cross-validation to perform feature selection. Next, we use the whole training set to train scorecards with the identified feature subsets and evaluate their performance on the holdout data.

We use three base classifiers: extreme gradient boosting, logistic regression and L1-regularized logistic regression. This allows us to check the robustness of feature selection techniques across diferent predictive algorithms and see whether internal feature selection in models such as L1 regression diminishes the value of the proposed wrapper approach.

Before performing feature selection, we use a subset of the training data to tune meta-parameters of the base classifiers. For each of the considered classification algorithms, we perform a learning curve analysis to select a suitable sample size by gradually increasing the percentage of the training sample until the model performance in terms of EMP stops improving. Next, we use the corresponding subset to perform parameter tuning using grid search [4]. The full parameter grid is presented in Table 3.

The parameters of NSGA-II (number of generations and population size) were selected based on the experiments on the subsets of training data, where we compared performance of three specifications (50 × 50, $1 0 0 \times 1 0 0$ and 200 × 200) in terms of maximal EMP. Based on these results, number of generations and population size were set to 200. After identifying suitable meta-parameter values, we perform feature selection with the suggested multi-objective framework.

Table 3 Parameter grid.

<table><tr><td>Method*</td><td>Parameter</td><td>Candidate values</td></tr><tr><td>LR</td><td>-</td><td>-</td></tr><tr><td>L1</td><td>cost</td><td> $2^{-10}$ ,  $2^{-9.5}$ ,  $2^{-9}$ , ...,  $2^{10}$ </td></tr><tr><td rowspan="3">XG</td><td>nrounds</td><td>10, 25, 50, 100, 250, 500, 1000, 2500</td></tr><tr><td>eta</td><td>0.01, 0.03, 0.05</td></tr><tr><td>max. depth</td><td>1, 3, 5</td></tr></table>

<sup>⁎</sup>Abbreviations: LR = logistic regression, L1 = L1-regularized LR, XG = extreme gradient boosting.

As described in Section $^ { 3 , }$ the EMP measure depends on two para meters, which need to be specified in order to calculate EMP on a scorecard level. These parameters are the expected loss in case of default and return on investment. For data sets where this information is not available or cannot be deprived from available meta-data, we follow the empirical findings of [40] and assume that the loss given default follows a bimodal distribution with point masses $p _ { 0 } = 0 . 5 5$ for no loss and $p _ { 1 } = 0 . 1$ for full loss; we also follow [40] in assuming a constant return on investment of 0.2664. The selected values correspond to the default values provided in the R package for EMP estimation available at CRAN [10].

To evaluate the performance of the proposed algorithm, we compare it to five traditional feature selection strategies: SFS, SBS, LASSO, single-objective GA and single-objective binary PSO [43]. To ensure a fair comparison, we set the number of generations and number of in dividuals for the simple GA to the same values as for the NSGA-II, which results in the same total number of models trained within the algorithm. We also use a scorecard that relies on a full set of features as a benchmark. All five single-objective benchmarks use the EMP measure as a fitness function. We only consider wrapper methods as benchmarks because of their superior performance compared to other feature selection strategies [17].

Compared to other single-objective feature selection benchmarks considered in this paper, the advantage of SFS and SBS is that they can also provide a Pareto frontier based on their path to the final solution. On each iteration, we save the best-performing variable subset and evaluate its performance on the holdout sample, thereby obtaining a set of non-dominated solutions.

## 4.3. Empirical results

In this section, we start with the experimental results where logistic regression is used as a base model for all techniques and then focus on the aggregated results across diferent classifiers. Logistic regression is still widely used in practice [22,38] despite that other algorithms have been shown to predict credit risk more accurately [23]. Detailed results for the other base classifiers including extreme gradient boosting and L1-regularized regression are given in Figs. A1 and B1 in the Appendix A and B.

Before moving to the empirical results, consider the example Pareto frontier depicted in Fig. 1. Here, the task is to minimize objective I while maximizing objective II. The frontier is represented by points A to

![](/api/attachments/AY5R9TTG/fulltext/images/5378d1bb99febbc9499ab27edc63b1c1d60c952a38816b6b691df1954e8d186e.jpg)  
Fig. 1. Example multi-objective optimization. The task is to minimize objective I while maximizing objective II. Points A – E represent solutions on the eficient frontier, points $\mathbf { G } , ]$ F and H are external solutions. Compared to the frontier, H is dominated by points A to D, G is a non-dominated point, and F dominates solutions D and E on the frontier.

E, whereas points F, G and Hare external solutions (benchmarks). Point H is dominated by points A to D on the Pareto frontier because they perform better in two objectives. Points F and G demonstrate better performance in terms of objective II compared to the best solution from the Pareto frontier (point E). However, there is a crucial diference between these points. Solution G does not dominate any points on the frontier – it achieves better performance in objective II only by deteriorating on objective I. At the same time, point F achieves better performance in both objectives compared to points D and E on the frontier. Therefore, F dominates these solutions. It is important to distinguish domination (point F) and non-domination (point G) when comparing the performance of diferent feature selection techniques.

Fig. 2 presents the graph matrix with the performance of the considered feature selection methods on all ten data sets. The Pareto frontier identified by the NSGA-II algorithm is depicted with red markers, whereas other points represent the single-objective benchmarks. GA, PSO and LASSO provide single solutions, whereas for SBS and SFS we depict the Pareto frontiers obtained during the feature selection. The black cross marks the baseline solution which is based on a full model without feature selection.

Results indicate that the size of the NSGA-II Pareto frontier varie across the data library from having just two solutions (thomas and bene1) to 20 feature subsets (pakdd). The small size of the Pareto frontier can be explained by two reasons: first, no candidate solutions with a larger number of features demonstrate better performance during cross-validation; second, some solutions become dominated when evaluating their quality on the holdout data and are therefore dropped from the frontier. Hence, NSGA-II frontiers are likely to contain fewer solutions on data sets with lower dimensionality and stronger diferences in data distribution between the training and holdout samples.

Overall, the points on NSGA-II frontiers usually populate regions with a smaller number of features compared to benchmarks. Singleobjective methods optimize predictive performance but do not account for the number of features. This does not motivate the algorithm to select smaller feature subsets. Nevertheless, sequential forward selection chooses fewer features compared to sequential backward elimination on all ten data sets.

We also note that frontiers produced by SFS are more stable compared to SBS-based frontiers as they have more solutions that remain non-dominated after reevaluating performance on the holdout sample. According to Fig. 2, SFS frontiers contain more solutions than NSGA-II frontiers on 6 data sets. Nevertheless, most points on SFS frontiers are dominated by the results obtained by NSGA-II. Below, we extend the comparison by focusing on the best-performing solutions from the frontiers.

To evaluate the quality of the NSGA-II frontiers and compare them with the single objective benchmarks, we look at the performance of the considered feature selection methods in Table 4. To facilitate comparison, on each of the Pareto frontiers we select one solution that achieves the best performance in terms of EMP (the upper-right point). Then, we compare this solution with single-objective benchmarks in terms of EMP and the number of features.

As Table 4 suggests, the best-performing NSGA-II solution is based on fewer features compared to the solutions selected by single-objective techniques in 7 out of 10 cases and achieves the highest expected profit in 4 data sets. There is only one data set where one of the benchmarks identifies a solution which has both higher EMP and a lower complexity (SFS on gmsc). Tables with the performance of feature selection methods using other base classifiers produce similar results (see Appendix).

To further extend the comparison, we define three metrics based on the notions discussed in example in Fig. 1. Let S be a share of data sets where all single-objective benchmarks are weakly dominated by points on the Pareto frontier resulting from the NSGA-II algorithm (e.g., point H). If satisfied, this condition indicates a clear advantage of the multi-

![](/api/attachments/AY5R9TTG/fulltext/images/1043dafbc21683ed3c67f956b14e8d01013abb9bb273d7c098c60c97f8e65137.jpg)  
Fig. 2. Performance of feature selection methods. Each diagram in the graph matrix depicts results on a single data set. The Pareto frontier produced by the NSGA-II algorithm is depicted with red points. Green points represent non-dominated solutions from SFS and SBS; blue and yellow markers refer to other single-objective benchmarks. LR is used as a base classifier. (For the interpretation of the color references in this figure, the reader is kindly referred to the web version of this paper.

Number of selected features

Table 4  
Performance of feature selection methods: LR\*.  
Expected Maximum Profi

<table><tr><td>Data</td><td>NSGA-II**</td><td>GA</td><td>PSO</td><td>SBS**</td><td>SFS**</td><td>LASSO</td><td>Full model</td></tr><tr><td>australian</td><td>0.0990</td><td>0.0953</td><td>0.0999</td><td>0.0974</td><td>0.0989</td><td>0.0972</td><td>0.0974</td></tr><tr><td>german</td><td>0.0477</td><td>0.0465</td><td>0.0439</td><td>0.0433</td><td>0.0443</td><td>0.0436</td><td>0.0430</td></tr><tr><td>thomas</td><td>0.1730</td><td>0.1729</td><td>0.1728</td><td>0.1728</td><td>0.1728</td><td>0.1729</td><td>0.1728</td></tr><tr><td>bene1</td><td>0.1457</td><td>0.1458</td><td>0.1457</td><td>0.1458</td><td>0.1458</td><td>0.1457</td><td>0.1458</td></tr><tr><td>hmeq</td><td>0.0235</td><td>0.0231</td><td>0.0229</td><td>0.0232</td><td>0.0224</td><td>0.0111</td><td>0.0236</td></tr><tr><td>bene2</td><td>0.1587</td><td>0.1584</td><td>0.1583</td><td>0.1583</td><td>0.1584</td><td>0.1583</td><td>0.1583</td></tr><tr><td>uk</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td></tr><tr><td>lending club</td><td>0.0008</td><td>0.0009</td><td>0.0009</td><td>0.0009</td><td>0.0006</td><td>0.0007</td><td>0.0009</td></tr><tr><td>pakdd</td><td>0.0161</td><td>0.0165</td><td>0.0163</td><td>0.0127</td><td>0.0152</td><td>0.0158</td><td>0.0165</td></tr><tr><td>gmsc</td><td>0.0042</td><td>0.0042</td><td>0.0042</td><td>0.0043</td><td>0.0043</td><td>0.0040</td><td>0.0043</td></tr></table>

<table><tr><td>australian</td><td>6</td><td>18</td><td>19</td><td>40</td><td>11</td><td>12</td><td>42</td></tr><tr><td>german</td><td>12</td><td>24</td><td>31</td><td>57</td><td>17</td><td>22</td><td>61</td></tr><tr><td>thomas</td><td>1</td><td>14</td><td>14</td><td>24</td><td>13</td><td>7</td><td>28</td></tr><tr><td>bene1</td><td>1</td><td>40</td><td>42</td><td>78</td><td>9</td><td>18</td><td>83</td></tr><tr><td>hmeq</td><td>12</td><td>15</td><td>14</td><td>19</td><td>11</td><td>12</td><td>20</td></tr><tr><td>bene2</td><td>2</td><td>5</td><td>10</td><td>26</td><td>5</td><td>10</td><td>28</td></tr><tr><td>uk</td><td>2</td><td>17</td><td>21</td><td>50</td><td>15</td><td>8</td><td>51</td></tr><tr><td>lending club</td><td>13</td><td>77</td><td>105</td><td>205</td><td>42</td><td>65</td><td>206</td></tr><tr><td>pakdd</td><td>160</td><td>370</td><td>183</td><td>370</td><td>43</td><td>131</td><td>373</td></tr><tr><td>gmsc</td><td>21</td><td>39</td><td>39</td><td>56</td><td>13</td><td>25</td><td>68</td></tr></table>

\*Results in this table use logistic regression as a base classifier. Results for other models are given in the Appendix. EMP is rounded to four digits after the decimal point.  
\*\*Here, we consider a single solution on the Pareto frontier, which has the highest EMP and uses the maximal number of features.

Table 5  
Aggregated results.

<table><tr><td>Base classifier</td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td></tr><tr><td>Logistic regression</td><td>40%</td><td>90%</td><td>10%</td></tr><tr><td>L1-regularized LR</td><td>50%</td><td>100%</td><td>0%</td></tr><tr><td>Gradient boosting</td><td>50%</td><td>100%</td><td>0%</td></tr></table>

objective feature selection over the benchmarks, since they cannot achieve better performance in any of the objectives. Next, let $S _ { 2 }$ indicate a share of data sets with a weaker condition: none of the benchmarks dominates the solution on the Pareto front. Here, benchmarks may either be dominated by the solutions on the frontier $( \boldsymbol { \mathrm { e . g . } }$ point H) or achieve better EMP than solutions on the frontier, but only if they use more features (e.g., point G). Finally, let $S _ { 3 }$ be a share of data sets where one or more benchmarks dominate at least one solution on the frontier. This condition corresponds to point F from the aforemen tioned example and demonstrates an advantage of the single-objective benchmarks. We compute shares S $S _ { 2 }$ and $S _ { 3 }$ separately for each base classifier. The results are given in Table 5.

According to Table 5, all single-objective benchmarks are dominated by the best point on the NSGA-II frontier on 40% of the data sets for LR, 50% of the cases for L1 and XG. In other words, NSGA-II identifies a feature subset that simultaneously has a higher profitability and contains fewer features compared to the solutions identified by the conventional single-objective strategies on at least 40% of the data sets.

In most of the remaining cases, single-objective benchmarks can outperform the best multi-objective solution in terms of EMP only if they use more features. This is observed for five remaining data sets when using any of the considered base classifiers. In this case, solutions on the frontier identified by our method are still non-dominated by benchmarks and represent a trade-of between model comprehensibility and profitability in the regions where fewer features are used. Feature subsets selected by the single-objective benchmarks could serve as a possible extension of the frontier.

From the business perspective, solutions on the NSGA-II frontie may be more attractive for companies even if the scorecards are characterized by a lower profitability but based on a significantly smaller amount of data. For instance, NSGA-II achieves EMPof 0.0161 on pakdd data using 160 features, whereas single-objective GA identifies a subset of 370 features that obtains EMP of 0.0165. Here, relying on a multiobjective algorithm results in a 2% drop in EMP but also eliminates 57% of features. It is then the task of a risk analyst to decide whether a drop in profitability would be compensated by reducing the costs of collecting and storing the data on customer behavior.

Taking both objectives into account, solutions lying on the NSGA-II frontier are not dominated by any of the benchmarks in 90% to 100% cases depending on the base model. As we noted above, there is only one data set where one of the single-objective benchmarks identifies a feature subset that dominates some solutions on the NSGA-II based Pareto frontier. There is a single case (gmsc data with LR), where one of the single-objective methods dominates some solutions on the frontier. This indicates a good performance of the proposed multi-objective feature selection algorithm.

Another dimension of the algorithm comparison concerns the training times. In Table 6, we report the training times of all feature selection techniques considered in this study depending on the base classifier. The total training times are averaged across the ten credit scoring data sets. The experiments were performed on a machine with 4

Table 6  
Total training times.

<table><tr><td rowspan="2">Feature selection method</td><td colspan="3">Total training time* (minutes)</td></tr><tr><td>LR</td><td>L1</td><td>XG</td></tr><tr><td>NSGA-II</td><td>170.61</td><td>82.50</td><td>468.23</td></tr><tr><td>Single-objective GA</td><td>185.38</td><td>84.52</td><td>482.17</td></tr><tr><td>Single-objective PSO</td><td>107.98</td><td>57.94</td><td>270.63</td></tr><tr><td>SFS</td><td>65.42</td><td>61.69</td><td>115.96</td></tr><tr><td>SBS</td><td>295.06</td><td>14.02</td><td>425.62</td></tr><tr><td>LASSO</td><td>0.35</td><td>0.35</td><td>0.35</td></tr></table>

\*The total training times are averaged across 10 data sets.

cores at 3.4 GHz and 768 GB RAM.

As expected, training times of NSGA-II and single-objective GA are similar since they have the same total number of models trained within the algorithm. NSGA-II has slightly lower training times because it considers more feature subsets with lower cardinality while trying to minimize the number of features. PSO is characterized by a lower running time because of the faster convergence, whereas LASSO-based feature selection proves to be the fastest technique in our set as it only requires training a single L1 model to select features. Comparing SFS and SBS, we conclude that backward selection is preferable for L1- regularized regression due to a faster convergence but is substantially slower for LR and XG, which require more time to train models with many features. SFS is faster than NSGA-II for all base classifiers, while SBS performs significantly slower for LR-based feature selection.

Overall, we can note that the strong advantage of LASSO in the eficiency is compensated by its poor performance in terms of profitability and number of features, as detailed above. The use of NSGA-II does not involve substantially larger training times compared to the techniques such as SBS or single-objective GA. Comparing NSGA-II and PSO, one can conclude that faster convergence of PSO comes at the cost of lower profitability and comprehensibility of the final scoring model. The same holds for SFS that usually fails to find more preferable feature subsets identified by NSGA-II due to the limitations of its greedy framework.

## 5. Conclusion

This paper introduces a multi-objective profit-driven framework for feature selection in credit scoring. We use the recently developed EMP measure and the number of features as two fitness functions for the wrapper-based feature selection to address both profitability and comprehensibility. Multi-objective optimization is performed with the genetic algorithm NSGA-II. We evaluate the efectiveness of our approach by running empirical experiments on ten real-world retail credit scoring data sets.

Empirical results indicate that the proposed multi-objective feature selection framework performs highly competitive compared to the conventional feature selection strategies. The developed approach identifies feature subsets that yield the same or higher expected profit using fewer features than single-objective benchmarks on at least half of the data sets. Depending on a base classifier, solutions selected by the NSGA-II are not dominated by any of the single-objective benchmarks in 90% to 100% of cases. The results imply that previous work in ignoring the two objectives of feature selection in credit scoring has missed promising solutions that can be identified using the suggested framework.

In addition to demonstrating a superior performance, the suggested multi-objective method serves as a tool to find a trade-of in two conflicting objectives: comprehensibility and profitability of the model. By comparing the non-dominated solutions on the eficient frontier, risk managers can select a suitable subset of features depending on their business context.

Future research could pursue several directions. Recent literature suggested novel multi-criteria optimization methods that could replace the NSGA-II algorithm in the proposed profit-driven feature selection framework. Jimenez and colleagues proposed ENORA algorithm that demonstrates promising performance compared to NSGA-II [21]; Hancer and colleagues suggest multi-objective artificial bee colony optimization [19]; Zhang et al. apply multi-criteria particle swarm optimization to perform feature selection [47]. A systematic benchmark or corresponding solvers appears valuable to identify the most suitable multi-objective approach and clarify the degree to which alternative approaches display diferent performance in a value-based feature selection context.

Another promising avenue would be to use the suggested approach to optimize a diferent set of relevant objectives. In particular, minimizing risk while maximizing profitability is crucial in the wider scope of financial risk management and could be considered in a credit portfolio management context. More generally, future research could consider adjusting or extending the set of objectives for the feature selection algorithm, or apply the algorithm for other tasks in a predictive modeling process.

Finally, the use of the developed feature selection approach could be extended to other business applications. One of the possible domains is customer churn. Verbraken and colleagues developed a similar EMP measure for customer churn models [41], which could serve as one of the objectives for the feature selection algorithm.

## Appendix A. Empirical results using L1 model

Performance of feature selection methods: L1\*.

<table><tr><td colspan="8">Expected Maximum Profit</td></tr><tr><td>Data</td><td>NSGA-II**</td><td>GA</td><td>PSO</td><td>SBS**</td><td>SFS**</td><td>LASSO</td><td>Full model</td></tr><tr><td>australian</td><td>0.1057</td><td>0.1014</td><td>0.1029</td><td>0.1031</td><td>0.1029</td><td>0.0852</td><td>0.0712</td></tr><tr><td>german</td><td>0.0371</td><td>0.0373</td><td>0.0397</td><td>0.0401</td><td>0.0357</td><td>0.0353</td><td>0.0224</td></tr><tr><td>thomas</td><td>0.1729</td><td>0.1728</td><td>0.1728</td><td>0.1728</td><td>0.1728</td><td>0.1728</td><td>0.1728</td></tr><tr><td>bene1</td><td>0.1463</td><td>0.1459</td><td>0.1459</td><td>0.1459</td><td>0.1460</td><td>0.1458</td><td>0.1457</td></tr><tr><td>hmeq</td><td>0.0186</td><td>0.0183</td><td>0.0183</td><td>0.0183</td><td>0.0186</td><td>0.0077</td><td>0.0077</td></tr><tr><td>bene2</td><td>0.1591</td><td>0.1591</td><td>0.1583</td><td>0.1583</td><td>0.1588</td><td>0.1583</td><td>0.1583</td></tr><tr><td>uk</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td></tr><tr><td>lending club</td><td>0.0001</td><td>0.0002</td><td>0.0001</td><td>0.0002</td><td>0.0001</td><td>0.0000</td><td>0.0000</td></tr><tr><td>pakdd</td><td>0.0159</td><td>0.0158</td><td>0.0153</td><td>0.0159</td><td>0.0150</td><td>0.0121</td><td>0.0120</td></tr><tr><td>gmsc</td><td>0.0044</td><td>0.0045</td><td>0.0045</td><td>0.0045</td><td>0.0044</td><td>0.0000</td><td>0.0000</td></tr><tr><td colspan="8">Number of selected features</td></tr><tr><td>australian</td><td>21</td><td>25</td><td>20</td><td>31</td><td>9</td><td>13</td><td>42</td></tr><tr><td>german</td><td>6</td><td>27</td><td>27</td><td>42</td><td>21</td><td>21</td><td>61</td></tr><tr><td>thomas</td><td>3</td><td>13</td><td>17</td><td>23</td><td>4</td><td>7</td><td>28</td></tr><tr><td>bene1</td><td>3</td><td>36</td><td>44</td><td>77</td><td>11</td><td>20</td><td>83</td></tr><tr><td>hmeq</td><td>3</td><td>14</td><td>13</td><td>17</td><td>4</td><td>13</td><td>20</td></tr><tr><td>bene2</td><td>3</td><td>3</td><td>14</td><td>21</td><td>4</td><td>11</td><td>28</td></tr><tr><td>uk</td><td>8</td><td>25</td><td>29</td><td>45</td><td>7</td><td>11</td><td>51</td></tr></table>

(continued on next page)

![](/api/attachments/AY5R9TTG/fulltext/images/74f8a8a08468df7a5db968bc34fa35c9a38fce6a83c338015ee5ca998a39034a.jpg)  
Expected Maximum Profit  
(9) pakdd  
(7) uk  
(8) lendingclub  
(10) gmsc  
(5) hmeq

Table A1 (continued)

<table><tr><td>Data</td><td>NSGA-II**</td><td>GA</td><td>PSO</td><td>SBS**</td><td>SFS**</td><td>LASSO</td><td>Full model</td></tr><tr><td>lending club</td><td>6</td><td>105</td><td>109</td><td>182</td><td>56</td><td>81</td><td>206</td></tr><tr><td>pakdd</td><td>229</td><td>207</td><td>191</td><td>371</td><td>40</td><td>126</td><td>373</td></tr><tr><td>gmsc</td><td>17</td><td>31</td><td>36</td><td>64</td><td>22</td><td>31</td><td>68</td></tr></table>

\*L1 is used as a base classifier. EMP is rounded to four digits after the decimal point.  
\*\*Here, we consider a single solution on the Pareto frontier, which has the highest EMP and uses the maximal number of features.

![](/api/attachments/AY5R9TTG/fulltext/images/7fb631fe243a6ce30500386cbd5b63e884b47d7d8aad4d7b1cab64dffe8c64bc.jpg)

![](/api/attachments/AY5R9TTG/fulltext/images/f375d5a66f4ff3664ed5b69e8a109ed9730239b46f04ddb5364c30d80a49d8b4.jpg)

![](/api/attachments/AY5R9TTG/fulltext/images/6b83fc833688b0009b9320b8bfcdbdb90b804cb62e89b308f2723a54561d9ad8.jpg)

![](/api/attachments/AY5R9TTG/fulltext/images/63f4078acc8e18551dfb4827d8e8e909fc8b819f6145759496597709fd1a27be.jpg)

![](/api/attachments/AY5R9TTG/fulltext/images/85e88ada8a27ea7d215b95346ba7e3141ad94c998a5f5f8f2c10bd07cf0b2994.jpg)

![](/api/attachments/AY5R9TTG/fulltext/images/e20cc49e7f7345397209b0047aad6c9ee81f03ce429ed0a75e6959ffb9303307.jpg)

![](/api/attachments/AY5R9TTG/fulltext/images/70c07bf3b2350450af01d87251c614677625e96ef59aa4a794e884b2e00735e6.jpg)

![](/api/attachments/AY5R9TTG/fulltext/images/dd1f3a35b7027fae81cfb40bfb417e0d983ba31cf2ebea1618e5c009653c14c4.jpg)

![](/api/attachments/AY5R9TTG/fulltext/images/7cb6d23b12ff4b1029bfc73295d1b23bc8a448ae700938b0b215ad14d4b107b9.jpg)

![](/api/attachments/AY5R9TTG/fulltext/images/9d92b6864c7c073bcc37d47e939d0cfd05244e6e1383e3984a7aa10f8c8eaab2.jpg)  
Fig. A1. Performance of feature selection methods. Each diagram in the graph matrix depicts results on a single data set. The Pareto frontier produced by the NSGA-I algorithm is depicted with red points. Green points represent non-dominated solutions from SFS and SBS; blue and yellow markers refer to other single-objective benchmarks. L1 is used as a base classifier. (For the interpretation of the color references in this figure, the reader is kindly referred to the web version of this paper.)

Appendix B. Empirical results using XG model  
Performance of feature selection methods: XG\*. <sub>abl</sub>e<sup>B</sup>

<table><tr><td colspan="8">Expected Maximum Profit</td></tr><tr><td>Data</td><td>NSGA-II**</td><td>GA</td><td>PSO</td><td>SBS**</td><td>SFS**</td><td>LASSO</td><td>Full model</td></tr><tr><td>australian</td><td>0.1060</td><td>0.1065</td><td>0.1046</td><td>0.1056</td><td>0.1060</td><td>0.1054</td><td>0.1055</td></tr><tr><td>german</td><td>0.0393</td><td>0.0391</td><td>0.0407</td><td>0.0411</td><td>0.0330</td><td>0.0327</td><td>0.0392</td></tr><tr><td>thomas</td><td>0.1731</td><td>0.1728</td><td>0.1728</td><td>0.1728</td><td>0.1728</td><td>0.1728</td><td>0.1728</td></tr><tr><td>bene1</td><td>0.1457</td><td>0.1457</td><td>0.1457</td><td>0.1457</td><td>0.1459</td><td>0.1459</td><td>0.1457</td></tr><tr><td>hmeq</td><td>0.0422</td><td>0.0418</td><td>0.0402</td><td>0.0415</td><td>0.0399</td><td>0.55</td><td>0.0418</td></tr><tr><td>bene2</td><td>0.1583</td><td>0.1583</td><td>0.1283</td><td>0.1583</td><td>0.1583</td><td>0.1583</td><td>0.1583</td></tr><tr><td>uk</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td><td>0.2593</td></tr><tr><td>lending club</td><td>0.0008</td><td>0.0007</td><td>0.0007</td><td>0.0007</td><td>0.0008</td><td>0.0006</td><td>0.0009</td></tr><tr><td>pakdd</td><td>0.0168</td><td>0.0165</td><td>0.0163</td><td>0.0164</td><td>0.0157</td><td>0.0161</td><td>0.0166</td></tr><tr><td>gmsc</td><td>0.0046</td><td>0.0045</td><td>0.0045</td><td>0.0046</td><td>0.0044</td><td>0.0042</td><td>0.0045</td></tr><tr><td colspan="8">Number of selected features</td></tr><tr><td>australian</td><td>3</td><td>17</td><td>20</td><td>36</td><td>11</td><td>14</td><td>42</td></tr><tr><td>german</td><td>2</td><td>25</td><td>31</td><td>51</td><td>11</td><td>21</td><td>61</td></tr><tr><td>thomas</td><td>10</td><td>12</td><td>9</td><td>23</td><td>3</td><td>7</td><td>28</td></tr><tr><td>bene1</td><td>1</td><td>42</td><td>47</td><td>80</td><td>4</td><td>22</td><td>83</td></tr><tr><td>hmeq</td><td>19</td><td>15</td><td>13</td><td>19</td><td>12</td><td>12</td><td>20</td></tr><tr><td>bene2</td><td>1</td><td>10</td><td>28</td><td>28</td><td>3</td><td>11</td><td>28</td></tr><tr><td>uk</td><td>1</td><td>18</td><td>27</td><td>47</td><td>5</td><td>9</td><td>51</td></tr><tr><td>lending club</td><td>12</td><td>107</td><td>106</td><td>197</td><td>13</td><td>93</td><td>206</td></tr><tr><td>pakdd</td><td>203</td><td>180</td><td>195</td><td>366</td><td>14</td><td>124</td><td>373</td></tr><tr><td>gmsc</td><td>24</td><td>34</td><td>38</td><td>66</td><td>14</td><td>34</td><td>68</td></tr></table>

![](/api/attachments/AY5R9TTG/fulltext/images/c98293bfad3cef482986a2c4faba6db30fe6309b6daddf0b3c5f830638f53859.jpg)

Fig. B1. Performance of feature selection methods. Each diagram in the graph matrix depicts results on a single data set. The Pareto frontier produced by the NSGA-II algorithm is depicted with red points. Green points represent non-dominated solutions from SFS and SBS; blue and yellow markers refer to other single-objective benchmarks. XG is used as a base classifier. (For the interpretation of the color references in this figure, the reader is kindly referred to the web version of this paper.)

## References

[1] B. Baesens, T. Van Gestel, S. Viaene, M. Stepanova, J. Suykens, J. Vanthienen, Benchmarking state-of-the-art classification algorithms for credit scoring, Journal of the Operational Research Society 54 (6) (2003) 627–635

[2] B. Baesens, D. Roesch, H. Scheule, Credit Risk Analytics: Measurement Techniques,

[3] S. Benítez-Peña. R. Blanquero. E. Carrizosa. P. Ramírez-Cobo. Cost-sensitive feature

[4] J.S. Bergstra, R. Bardenet, Y. Bengio, B. Kégl, Algorithms for hyper-parameter optimization. Advances in Neural Information Processing Systems (2011) 2546–2554. timization. Advances in Neural Information Processing Systems (2011) 2546–2554

[5] V. Bolón-Canedo. N. Sánchez-Maroño. A. Alonso-Betanzos, A review of feature

selection methods on synthetic data. Knowledge and Information Systems 34 (3) (2013) 483–519.

[6] V. Bolón-Canedo, N. Sánchez-Maroño, A. Alonso-Betanzos, Recent advances and emerging challenges of feature selection in the context of big data, Knowledge-Based Systems 86 (2015) 33–45

[7] V. Bolón-Canedo. N. Sánchez-Maroño. A. Alonso-Betanzos, J.M. Benítez, F. Herrera Sciences 282 (2014) 111–135

[8] B. Boney, F. Escolano, M. Cazorla, Feature selection, mutual information, and the classification of high-dimensional patterns. Pattern Analysis and Applications 11 (3–4) (2008) 309–319

[9] C. Bravo, S. Maldonado, R. Weber, Granting and managing loans for micro-entrepreneurs: new developments and practical experiences, European Journal o

Operational Research 227 (2) (2013) 358–366.

[10] C. Bravo, T. Verbraken, EMP: expected maximum profit for credit scoring. R package version 1.0, http://CRAN.R-project.org/package=EMP, (2014) , Accessed date: 1 September 2018.

[11] S. Cang, H. Yu, Mutual information based input feature selection for classification problems, Decision Support Systems 54 (1) (2012) 691–698.

[12] J.N. Crook, D.B. Edelman, L.C. Thomas, Recent developments in consumer credit risk assessment, European Journal of Operational Research 183 (3) (2007) 1447–1465.

[13] K. Deb, A. Pratap, S. Agarwal, T.A.M.T. Meyarivan, A fast and elitist multiobjective genetic algorithm: NSGA-II, IEEE Transactions on Evolutionary Computation 6 (2) (2002) 182–197.

[14] C. Emmanouilidis, A. Hunter, J. MacIntyre, C. Cox, Selecting features in neurofuzzy modelling by multiobjective genetic algorithms, Proceedings of the 9th International Conference on Artificial Neural Networks, 1999, pp. 4387–4392 (Washington, D.C).

[15] S. Finlay, Credit scoring for profitability objectives, European Journal of Operational Research 202 (2) (2010) 528–537.

[16] I. Guyon, A. Elisseef, An introduction to feature and feature selection, Journal of Machine Learning Research 3 (2003) 1157–1182.

[17] I. Guyon, S. Gunn, M. Nikravesh, L.A. Zadeh, Feature Extraction: Foundations and Applications (Studies in Fuzziness and Soft Computing), Springer-Verlag, 2006.

[18] T.M. Hamdani, J.M. Won, A.M. Alimi, F. Karray, Multi-objective feature selection with NSGA II, International Conference on Adaptive and Natural Computing Algorithms, Springer, Berlin, Heidelberg, 2007, April, pp. 240–247.

[19] E. Hancer, B. Xue, M. Zhang, D. Karaboga, B. Akay, Pareto front feature selection based on artificial bee colony optimization. Information Sciences 422 (2018) 462-479.

[20] D.J. Hand, Good practice in retail credit scorecard assessment, Journal of the Operational Research Society 56 (9) (2005) 1109–1117.

[21] F. Jimenez, A.F. Gómez-Skarmeta, G. Sánchez, K. Deb, An evolutionary algorithm for constrained multi-objective optimization, Proceedings of the 2002 Congress on Evolutionary Computation, IEEE, 2002, pp. 1133–1138.

[22] K.M. Jung, L.C. Thomas, M.C. So, When to rebuild or when to adjust scorecards, Journal of the Operational Research Society 66 (10) (2015) 1656–1668.

[23] S. Lessmann, B. Baesens, H.V. Seow, L.C. Thomas, Benchmarking state-of-the-art classification algorithms for credit scoring: an update of research, European Journa of Operational Research 247 (1) (2015) 124–136.

[24] M. Lichman, UCI machine learning repository, School of Information and Computer Science, University of California, Irvine, CA, http://archive.ics.uci.edu/ml/, (2013) , Accessed date: 1 September 2018.

[25] S. Maldonado, Á. Flores, T. Verbraken, B. Baesens, R. Weber, Profit-based feature selection using support vector machines – general framework and an application for customer retention, Applied Soft Computing 35 (2015) 740–748.

[26] S. Maldonado, C. Bravo, J. Lopez, J. Pérez, Integrated framework for profit-based feature selection and SVM classification in credit scoring, Decision Support Systems 104 (2017) 113–121.

[27] S. Maldonado, J. Pérez, C. Bravo, Cost-based feature selection for support vector machines: an application in credit scoring, European Journal of Operational Research 261 (2) (2017) 656–665

[28] E. Mays, N. Lynas, Credit Scoring for Risk Managers: The Handbook for Lenders,

[29] F. Min. O. Hu. W. Zhu. Feature selection with test cost constraint. International Journal of Approximate Reasoning 55 (1) (2014) 167–179.

[30] A. Mukerjee, R. Biswas, K. Deb, A.P. Mathur, Multi objective evolutionary algo rithms for the risk return trade of in bank loan management, Internationa Transactions in Operational Research 9 (5) (2002) 583–597.

[31] L.S. Oliveira, R. Sabourin, F. Bortolozzi, C.Y. Suen, Feature selection using multiobjective genetic algorithms for handwritten digit recognition, Proceedings of the 16th International Conference on Pattern Recognition, IEEE, 2002, pp. 240–247.

[32] F. Poursabzi-Sangdeh, D.G. Goldstein, J.M. Hofman, J.W. Vaughan, H. Wallach Manipulating and measuring model interpretability. NIPS 2017 Transparent and Interpretable Machine Learning in Safety Critical Environments Workshop. 2017.

[33] R. Saeedi, B. Schimert, H. Ghasemzadeh. Cost-sensitive feature selection for onbody sensor localization, Proceedings of the 2014 ACM International Joint Conference on Pervasive and Ubiquitous Computing, ACM, 2014, pp. 833–842

[34] C. Serrano-Cinca, B. Gutiérrez-Nieto, The use of profit scoring as an alternative to credit scoring systems in peer-to-peer (P2P) lending, Decision Support Systems 89 (2016)113-122

[35] M. Somers, J. Whittaker, Quantile regression for modelling distributions of profit and loss, European Journal of Operational Research 183 (3) (2007) 1477–1487.

[36] A.J. Soto, R.L. Cecchini, G.E. Vazquez, I. Ponzoni, Multi objective feature selection in QSAR using a machine learning approach, QSAR & Combinatorial Science 28

(11–12) (2009) 1509–1523.

[37] N. Srinivas, K. Deb, Muiltiobjective optimization using nondominated sorting in genetic algorithms, Evolutionary Computation 2 (3) (1994) 221–248.

[38] L.C. Thomas, D.B. Edelman, J.N. Crook, Credit Scoring and its Applications, SIAM, Philadelphia, 2002.

[39] R. Tsaih, Y.J. Liu, W. Liu, Y.L. Lien, Credit scoring system for small business loans, Decision Support Systems 38 (1) (2004) 91–99.

[40] T. Verbraken, C. Bravo, R. Weber, B. Baesens, Development and application of consumer credit scoring models using profit-based classification measures, European Journal of Operational Research 238 (2) (2014) 505–513.

[41] T. Verbraken, W. Verbeke, B. Baesens, A novel profit maximizing metric for measuring classification performance of customer churn prediction models, IEEE Transactions on Knowledge and Data Engineering 25 (5) (2013) 961–973.

[42] D. Vidaurre, C. Bielza, P. Larrañaga, A survey of L1 regression, International Statistical Review 81 (3) (2013) 361–387

[43] S.M. Vieira, L.F. Mendonça, G.J. Farinha, J.M. Sousa, Modified binary PSO for feature selection using SVM applied to mortality prediction of septic patients Applied Soft Computing 13 (8) (2013) 3494–3504.

[44] B. Xue, M. Zhang, W.N. Browne, Particle swarm optimization for feature selection in classification: a multi-objective approach, IEEE Transactions on Cybernetics 43 (6) (2013)1656–1671

[45] B. Xue, M. Zhang, W.N. Browne, X. Yao, A survey on evolutionary computation approaches to feature selection, IEEE Transactions on Evolutionary Computation 20 (4) (2016) 606–626.

[46] J. Yang, V. Honavar, Feature subset selection using a genetic algorithm, Feature Extraction, Construction and Selection, Springer, Boston, MA, 1998, pp. 117–136

[47] Y. Zhang, D.W. Gong, J. Cheng, Multi-objective particle swarm optimization approach for cost-based feature selection in classification. IEEE/ACM Transactions or Computational Biology and Bioinformatics 14 (1) (2017) 64–75.

Nikita Kozodoi is a PhD candidate at the Chair of Information Systems at the Humboldt University of Berlin and research associate at Kreditech. Hamburg. He holds a M.Sc degree in Economics and Management Science. In the course of his Ph.D., Nikita researches applications for machine learning in credit risk analytics

Stefan Lessmann received a diploma in business administration and a PhD from the University of Hamburg in 2002 and 2007, respectively. Stefan worked as a lecturer and senior lecture in business informatics at the Institute of Information Systems of the University of Hamburg. Since 2008, Stefan is a guest lecturer at the School of Management of University of Southampton, where he teaches under- and postgraduate courses on quantitative methods, electronic business, and web application development. Stefan completed his habilitation in the area of predictive analytics in 2012. In 2014, Stefan joined the Humboldt-University of Berlin, where he heads the Chair of Information Systems at the School of Business and Economics. Stefan published several papers in leading international journals and conferences, including the European Journal of Operational Research, the IEEE Transactions of Software Engineering, and the International Conference on Information Systems. He actively participates in knowledge transfer and consulting proiects with industry partners: from small start-up companies to global players.

Konstantinos Papakonstantinou is the Chief Data Oficer at Kreditech. In his current role. he is overlooking research and development activities of machine-learning-based solutions for credit risk management, product personalization, customer acquisition and retention. Konstantinos holds a MSc in Electrical Engineering from the University of Southern California and a PhD in Statistical Signal Processing from Telecom ParisTech

Yiannis Gatsoulis is Head of Data Science at Kreditech, Hamburg. He holds a PhD in Robotics from the University of Leeds and an MSc in Artificial Intelligence from the University of Edinburgh. He has over 10 years of experience is solving a wide-spread of research problems in machine learning both in academic and industrial environments.

Bart Baesens is a professor of Big Data & Analytics at KU Leuven (Belgium), and a lec turer at the University of Southampton (United Kingdom). He has done extensive research on big data & analytics, credit risk modeling, fraud detection, and marketing analytics. He co-authored more than 250 scientific papers and 10 books some of which have been translated into Chinese, Kazakh and Korean, and sold more than 20,000 copies of these books world-wide. Bart received the OR Society's Goodeve medal for best JORS paper in 2016 and the EURO 2014 and EURO 2017 award for best EJOR paper. His research is summarized at www.dataminingapps.com. He also regularly tutors, advises and provides consulting support to international firms with respect to their analytics and credit risk management strategy.
