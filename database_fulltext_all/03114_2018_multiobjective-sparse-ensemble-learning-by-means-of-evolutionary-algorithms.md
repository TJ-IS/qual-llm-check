---
otero_id: 3114
otero_key: "5Y5VYQQU"
title: "Multiobjective sparse ensemble learning by means of evolutionary algorithms"
authors: "Jiaqi Zhao; Licheng Jiao; Shixiong Xia; Vitor Basto Fernandes; Iryna Yevseyeva; Yong Zhou; Michael T.M. Emmerich"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.05.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multiobjective sparse ensemble learning by means of evolutionary algorithms

Jiaqi Zhao<sup>a</sup>, Licheng Jiao<sup>b</sup>, Shixiong Xia<sup>a,\*</sup>, Vitor Basto Fernandes<sup>c,d</sup>, Iryna Yevseyeva<sup>e</sup>, Yong Zhou<sup>a</sup>, Michael T.M. Emmerich<sup>f</sup>

<sup>a</sup> School of Computer Science and Technology, China University of Mining and Technology, No. 1, Daxue Road, Xuzhou, Jiangsu 221116, China

<sup>b</sup> Key Laboratory of Intelligent Perception and Image Understanding of the Ministry of Education, International Research Center for Intelligent Perception and Computation,

Joint International Research Laboratory of Intelligent Perception and Computation, Xidian University, Xi’an, Shaanxi 710071, China

<sup>c</sup> Instituto Universitário de Lisboa (ISCTE-IUL), ISTAR-IUL, University Institute of Lisbon, Av. das Forças Armadas, Lisboa 1649-026, Portugal

<sup>d</sup> School of Technology and Management, Computer Science and Communications Research Centre, Polytechnic Institute of Leiria, Leiria 2411-901, Portugal

<sup>e</sup> Faculty of Technology, De Montfort University, Gateway House 5.33, The Gateway, Leicester LE1 9BH, UK

<sup>f</sup> Multicriteria Optimization, Design, and Analytics Group, LIACS, Leiden University, Niels Bohrweg 1, Leiden 2333-CA, The Netherlands

## A R T I C L E I N F O

Keywords: Ensemble learning Sparse representation Classi<sup>fi</sup>cation Multiobjective optimization Change detection

## A B S T R A C T

Ensemble learning can improve the performance of individual classi<sup>fi</sup>ers by combining their decisions. The sparseness of ensemble learning has attracted much attention in recent years. In this paper, a novel multiobjective sparse ensemble learning (MOSEL) model is proposed. Firstly, to describe the ensemble classi<sup>fi</sup>ers more precisely the detection error trade-o<sup>f</sup> (DET) curve is taken into consideration. The sparsity ratio (sr) is treated as the third objective to be minimized, in addition to false positive rate (fpr) and false negative rate (fnr) minimization. The MOSEL turns out to be augmented DET (ADET) convex hull maximization problem. Secondly, several evolutionary multiobjective algorithms are exploited to <sup>fi</sup>nd sparse ensemble classi<sup>fi</sup>ers with strong performance. The relationship between the sparsity and the performance of ensemble classi<sup>fi</sup>ers on the ADET space is explained. Thirdly, an adaptive MOSEL classi<sup>fi</sup>ers selection method is designed to select the most suitable ensemble classi<sup>fi</sup>ers for a given dataset. The proposed MOSEL method is applied to well-known MNIST datasets and a real-world remote sensing image change detection problem, and several datasets are used to test the performance of the method on this problem. Experimental results based on both MNIST datasets and remote sensing image change detection show that MOSEL performs signi<sup>fi</sup>cantly better than conventional ensemble learning methods.

## 1. Introduction

The idea of ensemble learning methods [1] is to construct a set of classi<sup>fi</sup>ers with base learning algorithms and then classify new data points by taking a (weighted) vote of their predictions. Generally, ensemble methods combine the prediction of individual methods and can obtain better predictive performance than any individual method alone. Ensemble learning methods have attracted much attention in recent years. Not only have many ensemble algorithms been proposed [2,3], but also ensemble learning methods have been applied to many areas [4,5], such as medical information processing [1] and satellite image classi<sup>fi</sup>cation [6].

In general, an ensemble learning algorithm is constructed in two steps, i.e., training a number of component classi<sup>fi</sup>ers and then combining the predictions of the components. The most prevailing approaches for training component classi<sup>fi</sup>ers are bagging [7], boosting [8], random subspace [9], and rotation forest [10]. Recently, research has drawn attention to multiobjective optimization of ensemble learning [11,12] and several evolutionary multiobjective algorithms (EMOAs) have been used to deal with it. Generally, most of thi work is trying to obtain a set of classi<sup>fi</sup>ers with good performance on both diversity and accuracy by using multiobjective optimization algorithms with di<sup>f</sup>erent objectives. The multiobjective deep belief networks (DBNs) ensemble method was proposed in [13], in which an MOEA was applied to evolve multiple DBNs by considering accuracy and diversity as two con<sup>fl</sup>icting objectives. A divide-and-conquer based optimization framework for ensemble classi<sup>fi</sup>ers generation was proposed in [12], in which the accuracy of each class was treated as the objectives to describe the performance of classi<sup>fi</sup>ers. Besides, maximizing the ensemble size is also taken as an additional objective. The

Pareto image features were applied for candidate classi<sup>fi</sup>ers generation in [14] by using a multiobjective evolutionary trace transform algo rithm. These methods do not consider the redundancy between classi-<sup>fi</sup>ers and the e<sup>fi</sup>ciency of ensemble learning, as it requires a signi<sup>fi</sup>cant amount of memory to store the candidates of classi<sup>fi</sup>ers and lots of computation time is also needed to predict the label of each new input instance.

In this paper, we focus on combining the predictions of component classi<sup>fi</sup>ers by <sup>fi</sup>nding several appropriate sparse weight vectors for them. Many works have addressed the complexity of ensemble classi <sup>fi</sup>ers by reducing the number of classi<sup>fi</sup>ers in the component candidate set. The relationship between the ensemble learning and its component classi<sup>fi</sup>ers is analyzed in [15], which reveals that a better performance can be obtained by ensembling many instead of all the available classi<sup>fi</sup>ers. A genetic algorithm is adopted to evolve the weights of the component classi<sup>fi</sup>ers, showing that it can generate ensemble classi<sup>fi</sup>ers with small sizes but good generalization ability. The theoretical and empirical evidence in [16] suggests that a smaller ensemble size can often obtain better performance than a larger ensemble. It is, therefore, possible to obtain an ensemble which minimizes the number of individual classi<sup>fi</sup>ers and preserves or improves the performance of attributes, such as accuracy and cost of misclassi<sup>fi</sup>cation. However, only the accuracy is considered in this method, the result contains redundant classi<sup>fi</sup>ers, as the sparsity of ensemble classi<sup>fi</sup>ers is not considered. Several pruning strategies are analyzed in [17], including reduction error (RE), Kappa pruning (KP), complementarity measure (CM) and margin distance (MD). Matching pursuit (MP) is used to prune the ensemble classi<sup>fi</sup>ers in [18] by balancing the diversity and the in dividual accuracy. In these methods, the greedy strategy is used to search for the optimal classi<sup>fi</sup>ers set and it is easy to fall into the local extremum.

Sparse ensembles were proposed in [19]. The outputs of multiple classi<sup>fi</sup>ers were combined by using a sparse weight vector. The hinge loss and the 1-norm regularization were exploited to calculate the sparse weight vector, formulated as a linear programming problem. However, the 1-norm metric cannot describe the sparseness of ensemble classi<sup>fi</sup>ers precisely. This is because a weight vector with a group of small values can improve the performance of 1-norm measurement but cannot improve the performance of sparseness. The 0-norm metric can describe the sparseness more precisely [20]. The sparse ensemble learning is applied for synthetic aperture radar (SAR) image classi<sup>fi</sup>cation in [6] and for Youtube videos classi<sup>fi</sup>cation in [21]. The 0-norm learning can be regarded as an NP-hard problem, it is still an open problem to search the global optimum.

Compressed sensing (CS) [22] was brought to ensemble learning in [23]. It explores the globally optimal subset of classi<sup>fi</sup>ers for a given ensemble. To solve the compressed sensing problem, a sparse weighting vector which contains many zeros should be generated <sup>fi</sup>rst, and then appropriate weights should be provided for the remaining classi<sup>fi</sup>ers according to their relative importance. Several popular methods such as SpaRAS [24], OMP [25], FISTA [26], and PFP [27] are used to tune the weight vector of ensemble classi<sup>fi</sup>ers. In [23] it is shown that compressed sensing ensembles are often as accurate as, or more accurate than, conventional ensembles, although they use only small subsets of the total set of classi<sup>fi</sup>ers. However, the sparseness should be set in advance when using the compressed sensing methods. Meanwhile, the characteristics of the unbalanced data classi<sup>fi</sup>cation were not taken into consideration.

The contributions and drawbacks of the most related works of literature are listed in Table 1. Above all, the drawbacks of these methods are listed in the following: 1) The optimization algorithms used were easily trapped into local extremum; 2) only accuracy metric cannot describe ensemble performance precisely; and 3) the relationship between sparsity ensemble weights and ensemble performance was not analyzed in depth.

In this paper, we propose the novel concept of a multiobjective sparse ensemble learning (MOSEL) method, in which the relationship between the sparsity and the classi<sup>fi</sup>cation performance is explained. To accurately describe the performance of ensemble classi<sup>fi</sup>ers, the detection error trade-o<sup>f</sup> (DET) [28] performance is taken into consideration by adopting the false positive rate (fpr) and the false negative rate (fnr) simultaneously. Besides, the sparsity ratio (sr) of ensemble classi<sup>fi</sup>ers is treated as the third objective to be minimized. The DET can describe the classi<sup>fi</sup>ers more precisely than the accuracy metric especially for unbalance data classi<sup>fi</sup>cation problems [28]. Besides, the evolutionary multiobjective algorithm (EMOA) [29] technique is <sup>fi</sup>rst applied to evolve the combining weights of ensemble component classi<sup>fi</sup>ers. With the technique of tri-objective ensemble learning, we can obtain a set of ensemble classi<sup>fi</sup>ers with di<sup>f</sup>erent sparseness, rather than an ensemble classi<sup>fi</sup>er with a certain sparseness that is previously set. The sparsity and the error rates of ensemble classi<sup>fi</sup>ers are explainable, and their trade-o<sup>f</sup>s are quanti<sup>fi</sup>able in the augmented DET (ADET) space.

We analyze the properties of the ADET for sparse ensemble learning and several state-of-the-art many-objective optimization algorithms are applied to solve multiobjective ADCH maximization problems, including the two-archive algorithm (Two\_Arch2) [30], which focuses on convergence and diversity separately, the decomposition based algorithms, such as NSGA-III [31], the evolutionary algorithms based on both dominance and decomposition (MOEA/DD) [32], the reference vector guided evolutionary algorithm (RVEA) [33], an indicator based evolutionary algorithm with a reference point adaptation (AR-MOEA) [34], and 3D convex-hull-based evolutionary multiobjective optimization algorithm (3DFCH-EMOA) [35,36]. By using EMOAs, we can obtain a set of potentially optimal ensemble classi<sup>fi</sup>ers with different sr-fpr-fnr trade-o<sup>f</sup>s.

The remaining paper is organized as follows. Section 2 gives a brief introduction to multiobjective optimization of a sparse ensemble method. Section 3 presents the results of several classi<sup>fi</sup>cation problems with MNIST [37] and remote sensing change detection datasets, and Section 4 provides concluding remarks.

## 2. Multiobjective sparse ensemble learning

## 2.1. Ensemble learning

The idea of a sparse ensemble of classi<sup>fi</sup>ers is to combine the predictions of all classi<sup>fi</sup>ers in the candidate set using a sparse weight vector. The sparse vector has many elements with the value of zero and only classi<sup>fi</sup>ers corresponding to nonzero weights are selected for the ensemble. To improve the performance of the ensemble classi<sup>fi</sup>er and to reduce the memory demand for the components, it is required to select an optimal subset of classi<sup>fi</sup>ers and the corresponding weights vector for this subset. The problem of seeking sparse weights vectors can be modeled as a combinatorial optimization problem, which can be solved by evolutionary algorithms [30].

In this paper, we only consider binary supervised ensemble classi-<sup>fi</sup>cation problems. With a set of training samples $X _ { t r } = \{ ( x _ { j } , y _ { j } ) | x _ { j } \in R ^ { d } , y _ { j }$ $\in \{ - 1 , + 1 \} , j = 1 , 2 , . . . , M _ { t r } \}$ , where y is the class label corresponding to a given input $x _ { j } ,$ d is the dimensionality of sample of features, and $M _ { t r }$ is the number of instances. Note that in this work we only consider binary classi<sup>fi</sup>cation problems and we set the labels as {−1,1}, where 1 represents positive category and − 1 represents negative category, given a set of classi<sup>fi</sup>ers $\{ C _ { 1 } ( x ) , C _ { 2 } ( x ) , . . . , C _ { N } ( x ) \}$ , where C (x) is the i-th classi<sup>fi</sup>er in the candidate ensemble set. Usually, the classi<sup>fi</sup>er C (x) is obtained by using the training dataset $X _ { t r }$ with the strategy of random selection of the features or the instances.

A classi<sup>fi</sup>er can be obtained by using a training dataset with a machine learning algorithm, which can be described as an estimate of the unknown function $y = f ( x )$ . The classi<sup>fi</sup>er C (x) is a hypothesis f (x) about the true function f(x), which can predict the class label y for a new input vector x from a testing dataset $X _ { t s }$ or a validation dataset $X _ { \nu a l } .$

Table 1  
Contributions of several important literatures.

<table><tr><td>Literature</td><td>Contributions</td><td>Drawbacks</td></tr><tr><td>Zhou et al. [15]</td><td>The relationship between the ensemble learning and its component classifiers is analyzed.</td><td>The sparsity of ensemble was not taken into consideration.</td></tr><tr><td>Martínez-Munōz et al. [17]</td><td>Several pruning strategies were proposed.</td><td>The strategy is easy to fall into the local extremum.</td></tr><tr><td>Chen et al. [16]</td><td>Theoretical suggests that a smaller ensemble size can often obtain better performance than a larger ensemble.</td><td>The strategy is easy to fall into the local extremum.</td></tr><tr><td>Mao et al. [18]</td><td>Matching pursuit (MP) is used to prune the ensemble classifiers by balancing the diversity and the individual accuracy.</td><td>The strategy is easy to fall into the local extremum.</td></tr><tr><td>Zhang and Zhou [19]</td><td>The hinge loss and the 1-norm regularization was exploited.</td><td>The 1-norm metric cannot describe the sparseness of ensemble classifiers precisely.</td></tr><tr><td>Li et al. [23]</td><td>A compressed sensing approach for efficient ensemble learning.</td><td>The sparseness should be set in advance.</td></tr></table>

Usually, the training dataset is used for base classi<sup>fi</sup>ers learning, the validation dataset is used for ensemble pruning, and the test dataset is used for ensemble classi<sup>fi</sup>cation performance evaluation. Denote by $f _ { j i }$ the prediction of the ith learner C (x) for the jth sampling of the vali dation sample $x _ { j } ,$ that is described by Eq. (1).

$$
f _ {j i} = C _ {i} (x _ {j}).\tag{1}
$$

The prediction output label vector $\mathbf { f _ { i } }$ can be obtained by implementing the classi<sup>fi</sup>er C for the validation dataset $X _ { \nu a l }$ with size $M _ { \nu a l } ,$ which is denoted as in Eq. (2).

$$
\mathbf {f _ {i}} = \left[ f _ {1 i}, f _ {2 i},..., f _ {M _ {v a l} i} \right] ^ {T}.\tag{2}
$$

The matrix F of prediction labels for all instances obtained by all of the classi<sup>fi</sup>ers can be denoted by Eq. (3),

$$
\mathbf {F} = [ \mathbf {f _ {1}}, \mathbf {f _ {2}}, \dots , \mathbf {f _ {N}} ]\tag{3}
$$

$$
\text { where } \mathbf {f} _ {\mathbf {i}} = [ f _ {1 i}, f _ {2 i}, \dots , f _ {M i} ] ^ {T}, i = 1, 2, \dots , N, \text { and } \mathbf {F} \in R ^ {M _ {v a l} \times N}.
$$

The ensemble learning can improve the performance of classi<sup>fi</sup>ers by combining the decisions of each classi<sup>fi</sup>er and assigning weight w to each of the classi<sup>fi</sup>er $C _ { i } ( x )$ , and the vector of weights w is denoted by Eq. (4).

$$
\mathbf {w} = [ w _ {1}, w _ {2}, \dots , w _ {N} ] ^ {T}.\tag{4}
$$

The predicted label vector $\mathbf { y } _ { p r e d i c t }$ obtained by ensemble learning for the input dataset X can be described as in Eq. (5).

$$
\mathbf {y} _ {\text { predict }} = \mathbf {F w}.\tag{5}
$$

The perfect ensemble classi<sup>fi</sup>er can be obtained by solving an equation ${ \bf y } _ { \nu a l } = { \bf y } _ { p r e d i c t } .$ Usually, the number of equations is larger than that of the weighting variables in the equation system. In this case, there are typically no exact solutions for equations. In this case, the equation system can be approximately solved by using optimization algorithms to <sup>fi</sup>nd solutions, which can minimize the di<sup>f</sup>erence between the training labels and predicting labels.

## 2.2. Multiobjective optimization of ensemble learning

The DET curve [28] is taken into consideration to describe the performance of ensemble classi<sup>fi</sup>ers, which has been proved to be a good measurement to evaluate the performance of classi<sup>fi</sup>ers [38]. The de<sup>fi</sup>nition of the DET curve is closely related to the two-by-two confusion matrix, which describes the relationship between the ground truth and the predicted class for a binary classi<sup>fi</sup>er. A confusion matrix is shown in Table 2, which includes four possible outcomes. An outcome is a true positive if a positive instance is correctly classi<sup>fi</sup>ed and it is a true negative if a negative instance is correctly classi<sup>fi</sup>ed. Whenever a negative instance is classi<sup>fi</sup>ed as positive, we call it a false positive. Finally, whenever a positive instance is classi<sup>fi</sup>ed as negative, we call it a false negative.

Let TN denote the number of true negatives, FP the number of false positives, TP the number of true positives, and FN the number of false negatives. Then the false positive rate (fpr) is de<sup>fi</sup>ned as $f p r = \mathrm { F P } / \quad$ (TN + FP), and the false negative rate (fnr) is de<sup>fi</sup>ned as $f n r = \mathrm { F N } / $ (TP + FN). To minimize the di<sup>f</sup>erence between true labels and predicted labels, both fpr and fnr should be minimized.

Table 2  
A two-by-two confusion matrix of binary classi<sup>fi</sup>ers

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">True class</td></tr><tr><td> $P^{+}$ </td><td> $N^{-}$ </td></tr><tr><td rowspan="2">Predicted class</td><td> $P^{+}$ </td><td>True positives (TP)</td><td>False positives (FP)</td></tr><tr><td> $N^{-}$ </td><td>False negatives (FN)</td><td>True negatives (TN)</td></tr></table>

To obtain sparse ensemble classi<sup>fi</sup>ers with good performance, not only should the di<sup>f</sup>erence between true label vector ${ \bf y } _ { \nu a l }$ and predicted label vector $\mathbf { y } _ { p r e d i c t }$ be minimized, but also the number of nonzero elements in the weight vector w should be minimized. In Eq. (6) we de<sup>fi</sup>ne the sparsity ratio (sr) to describe the sparseness of ensemble,

$$
s r = \frac {\| \mathbf {w} \| _ {0}}{N}.\tag{6}
$$

Here, N is the number of classi<sup>fi</sup>ers in the candidate ensemble set and ∥w∥ represents the number of nonzero entities in the weight vector. The weight vector w is constrained to non-negative values, as negative weightings are neither intuitively meaningful nor reliable [23]. We try to <sup>fi</sup>nd ensemble classi<sup>fi</sup>ers with a low value of sr in order to reduce classi<sup>fi</sup>cation e<sup>f</sup>ort and to counteract over<sup>fi</sup>tting of the ensemble classi<sup>fi</sup>er.

The computational cost of an ensemble classi<sup>fi</sup>er with high sr is considered to be higher than that of an ensemble classi<sup>fi</sup>er with lower sr. We prefer an ensemble classi<sup>fi</sup>er with lower sr when given two ensemble classi<sup>fi</sup>ers with the same performance criteria (fpr, fnr). So sr, fpr and fnr are con<sup>fl</sup>icting with each other. A low value of sr means that a small number of classi<sup>fi</sup>ers are selected for the ensemble, i.e., the ensemble classi<sup>fi</sup>er has a low value of sr, which would result in a poor performance of fpr and fnr. By treating the sparse term sr as the third objective, the sparse ensemble turns out to be a multiobjective problem. We denote it as multiobjective sparse ensemble learning (MOSEL) which is described in Eq. (7),

$$
\begin{array}{l l} \min \operatorname{MOSEL} (\mathbf {w}) & := (f p r, f n r, s r) (\mathbf {w}), \\ & \text { subject   to } \quad \mathbf {w} \in \Omega , \end{array}\tag{7}
$$

where is the set of all possible weight vectors and w refers to the weightings with good performance of sparse ensemble classi<sup>fi</sup>ers.

## 2.3. Sparse real encoding

The sparse real encoding strategy is designed to represent the weight vector for the evolutionary algorithms, which is an improved version of the real encoding method. The sparse real encoding is constituted by an array of real values in the interval [0, 0.1]. The length of the chromosome is determined by the number of candidate classi<sup>fi</sup>ers for ensembles. Two strategies are used to modify the real encoding approach for multiobjective sparse ensembles. One is called hard threshold sparse the other is called inequality constraint. Details will be discussed below.

The classi<sup>fi</sup>er with a small value of weight in the ensemble learning system does not contribute much to the <sup>fi</sup>nal decision. In this paper, we ignore the classi<sup>fi</sup>ers with small values by adopting a hard threshold strategy. The value of weights smaller than the threshold is set to zero, as described in $\mathtt { E q . }$ (8)

$$
\mathbf {w} _ {\text { update }} (i) = \left\{ \begin{array}{l l} 0, & \text { if } \quad \mathbf {w} (i) <   \sigma \\ \mathbf {w} (i), & \text { else }, \end{array} \right.\tag{8}
$$

where σ is the hard threshold. In Section 3, the value is set to $0 . 0 5 ,$ where N is the number of candidate classi<sup>fi</sup>ers. The sparse real encoding can model the solution of sparse ensemble learning, and then several EMOAs can be applied to evolve the individuals in the population set.

## 2.4. Adaptive MOSEL classifiers selection

The proposed MOSEL can deliver a set of ensemble classi<sup>fi</sup>ers, in this

The most suitable ensemble classi<sup>fi</sup>er can be selected by minimizing the risk R. The adaptive MOSEL classi<sup>fi</sup>ers selection algorithm is described in Algorithm 1. Firstly, randomly select an ensemble classi<sup>fi</sup>er from the mosel set, and then evaluate the distributions of the given dataset. Under the evaluated distributions we can select the most suitable ensemble classi<sup>fi</sup>er by minimizing Eq. (10). If the selected classi<sup>fi</sup>er is the same as the preselected one it can be returned as the most suitable classi<sup>fi</sup>er, else go back to Step 2.

## 2.5. Framework of MOSEL

The description of the framework of MOSEL is given in Algorithm 2. Firstly, we train a set of candidate classi<sup>fi</sup>ers with $X _ { t r }$ by adopting bagging or random subspace strategies. Secondly, optimize the sparse vector w by using EMOAs with $X _ { \nu a l s }$ which is used to evaluate the performance of each individual of the EMOAs. Thirdly, the most suitable ensemble classi<sup>fi</sup>ers for $X _ { t s }$ can be obtained by adopting adaptive MOSEL classi<sup>fi</sup>ers selection algorithm.

Algorithm 2. Learning procedure for MOSEL

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 Learning Procedure for MOSEL
1: Training a set of candidate of classifiers with  $X_{tr}$ 
2: Optimizing the sparse vector w by using EMOAs with  $X_{val}$ 
3: Obtain the most suitable ensemble classifier for  $X_{ts}$  by using adaptive MOSEL classifiers selection algorithm
</div>

part we designed an adaptive selection method to choose the most suitable classi<sup>fi</sup>er for a given dataset [39]. Let $p ( P ^ { + } )$ signify the frequency of positive samples and $p ( N ^ { - } )$ denote that of negative samples for a dataset. With an ensemble classi<sup>fi</sup>er, the risk (R) can be denoted as Eq. (9),

$$
R = \lambda (F N, P ^ {+}) \cdot p (P ^ {+}) \cdot f n r + \lambda (F P, N ^ {-}) \cdot p (N ^ {-}) \cdot f p r,\tag{9}
$$

where $\lambda ( F N , P ^ { + } )$ is the loss incurred for deciding Negative when the true label is Positive and so is $\lambda ( F P , N ^ { - } )$ . In many real-world problems we can not obtain the label of each sample, however, we can estimate the distributions of a dataset with a prede<sup>fi</sup>ned classi<sup>fi</sup>er, and we denote them as $\widehat { p } \left( P ^ { + } \right)$ and $\widehat { p } \left( N ^ { - } \right)$ . Speci<sup>fi</sup>cally, we do not consider cost-sensitive classi<sup>fi</sup>cation problem in this paper, Eq. (9) can be simpli<sup>fi</sup>ed as Eq. (10):

$$
R = \widehat {p} (P ^ {+}) \cdot f n r + \widehat {p} (N ^ {-}) \cdot f p r.\tag{10}
$$

Algorithm 1. Adaptive MOSEL classi<sup>fi</sup>ers selection (mosel, $X _ { t s } )$

## 3. Experimental studie

## 3.1. Algorithms involved

In this section, we present the experimental results of the proposed multiobjective sparse ensemble learning methods and then compare the results with the results obtained by two compressed sensing (CS) ensemble methods and two pruning ensemble methods. The sparse ensemble methods in our comparison include SpaRAS [24], OMP [25], which are the most popular methods for solving sparse reconstruction problems [23]. The compared pruning methods are Kappa pruning (KP) [17] and ensemble based on matching pursuit (MP) [18]. Several state-of-the-art EMOAs are used to search the solutions of MOSEL, in cluding Two\_Arch2 [30], NSGA-III [31], MOEA/DD [32], RVEA [33], AR-MOEA [34] and 3DFCH-EMOA [36]. The MNIST [37] and remote sensing change detection datasets are selected to evaluate the performance of the above methods. The strategy of random subspaces [9] is adopted as the dataset manipulation and the classi<sup>fi</sup>cation and regression tree (CART) [40] is used as the base learner. For each mentioned algorithm, 10 independent trials are conducted.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Adaptive MOSEL classifiers selection (mosel, $X_{ts}$)
Require: mosel is the ensemble classifiers set, the performance of each classifier in ADET space with $X_{val}$ can be obtained
Ensure: the most suitable ensemble classifier for $X_{ts}$
1: Set $t \leftarrow 0$ and select a classifier $i_t$ from the solution set mosel randomly
2: Predict the labels for $X_{ts}$ by $EnC_{wi_t}$ and evaluate the dataset distributions $\hat{p}_t(P^+)$ and $\hat{p}_t(N^-)$
3: $t \leftarrow t + 1$
4: $i_t \leftarrow \arg \min_{j=1}^{n} \hat{p}_{t-1}(P^+) \cdot fnr_j + \hat{p}_{t-1}(N^-) \cdot fpr_j$
5: if $i_t = i_{t-1}$ then
6: return $EnC_{i_t}$
7: else
8: Go to step 2
9: end if
</div>

## 3.2. Parameter setting

The experiment stopping criteria of the six EMOAs are set with a maximum of 30,000 function evaluations. The simulated binary crossover (SBX) and polynomial bit-<sup>fl</sup>ip mutation operators are applied in the experiments with crossover probability of $p _ { c } = 0 . 9$ and the mutation probability of $p _ { m } = 0 . 1$ . The population size is set to 100 for all EMOAs. All of the experiments were implemented using Matlab code running on an IBM X3650 server with Xeon E5-2600 2.9 GHz processors and 32 GB memory under Ubuntu 16.04. The details of experiments are described in the following sections.

## 3.3. Metrics

Six metrics are chosen to evaluate the performance of studied algorithms in the comparative experiment on these datasets, including Accuracy, Precision, Recall, F-measure, Kappa coe<sup>fi</sup>cient (Kappa) [41] and number of non-zero ensemble weight. Generally, Accuracy, Precision, Recall and F-measure are popular in the area of binary classi<sup>fi</sup>cation problem. The de<sup>fi</sup>nition of them is denoted in Eq. (11). The larger the value of them the better is the classi<sup>fi</sup>cation performance.

$$
\begin{array}{r l} {A c c u r a c y} & {= \frac {T P + T N}{T P + T N + F P + F N},} \\ {P r e c i s i o n} & {= \frac {T P}{T P + F P},} \\ {R e c a l l} & {= \frac {T P}{T P + F N},} \\ {F \text {-measure}} & {= \frac {2 \times P r e c i s i o n \times R e c a l l}{P r e c i s i o n + R e c a l l}} \end{array}\tag{11}
$$

Kappa is a statistic indicator which measures inter-rater agreement for categorical items. It is generally thought to be a more robust measure than simple percent agreement calculation, as Kappa takes into account the possibility of the agreement occurring by chance. The de-<sup>fi</sup>nition of Kappa is denoted in Eq. (12).

$$
\begin{array}{r l} {K a p p a} & {= \frac {A c c u r a c y - p _ {e}}{1 - p _ {e}},} \\ {p _ {e}} & {= \frac {T P \times (T P + F N) + T N \times (T N + F P)}{T P + T N + F P + F N}.} \end{array}\tag{12}
$$

Generally, the larger the value of the Kappa, the better performance of the algorithm. The number of non-zero ensemble weight is selected to describe the sparse ratio of ensemble weight. We prefer a low value of this metric. The statistical results of these metrics are listed in Tables 4–9 and 12–17. In these tables the best results obtained are marked in light grey and the second best results are marked in dark grey. Furthermore, the Wilcoxon sum-rank test [36], which is a statistical test, is selected to evaluate whether the di<sup>f</sup>erences between 3DFCH-EMOA (one of MOSEL methods) and other methods are sig ni<sup>fi</sup>cant or not.

## 3.4. Experimental results on MNIST datasets

## 3.4.1. Dataset description

The MNIST dataset [37] is widely used for machine learning and pattern recognition methods on real-world data. It contains a training set with 60,000 examples and a testing set with 10,000 examples. Some samples from MNIST dataset are shown in Fig. 1. The handwritten digits have been size-normalized and centered in a <sup>fi</sup>xed-size image (i.e., 28 × 28). The intensity of each pixel in an image is treated as its features, so the dimensionality of features set for each sample is 784. In this part, we use a small amount of examples for training and validation, and the remains for testing.

The MNIST dataset we used in this part is described in the left part of Table 3. As we only consider binary classi<sup>fi</sup>cation problems in this paper, we select several sub-datasets from the whole dataset, including ds1–ds9 (details are listed in the right part of Table 3). All of the subdatasets contain two classes, for instance, the positive class in ds2 includes ‘1’, and the negative class includes ‘0’ and ‘2’. Both balanced and unbalanced datasets are created; for instance, in the ds9 dataset, the ratio of positive instances to negative instances is about 1:9. For each of the datasets, 1/2 of training instances are randomly selected for candidate classi<sup>fi</sup>ers generation, and the rest is used for ensemble performance evaluation.

## 3.4.2. Experimental results and discussion

Firstly, the reference Pareto front is shown to illustrate the properties of solutions of tested EMOAs, which is calculated as the best set of solutions of several algorithms achieved in the <sup>fi</sup>rst experimental run. Without loss of generality, we only discuss the result of the ds3 dataset in Table 3.

The obtained reference Pareto front is shown in Fig. 2 (a). We can see that the reference Pareto front includes a set of discrete points on the ADET surface. To illustrate the reference Pareto front clearly, two

![](/api/attachments/5Y5VYQQU/fulltext/images/95c5d65561a09f1c6d68ab3f8e817b14a9fa3f901ecbedd644664a032a1365b6.jpg)  
Fig. 1. Samples from MNIST dataset.

Table 3  
The details of MNIST dataset used in the experiments.

<table><tr><td>class</td><td>No. all set</td><td>No. of testing</td><td>No. of training</td><td>ds1</td><td>ds2</td><td>ds3</td><td>ds4</td><td>d5</td><td>ds6</td><td>ds7</td><td>d8</td><td>ds9</td></tr><tr><td>0</td><td>6903</td><td>5923</td><td>980</td><td>+</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1</td><td>7877</td><td>6742</td><td>1135</td><td>-</td><td>+</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2</td><td>6990</td><td>5958</td><td>1032</td><td></td><td>-</td><td>+</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>3</td><td>7141</td><td>6131</td><td>1010</td><td></td><td></td><td>-</td><td>+</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>4</td><td>6824</td><td>5842</td><td>985</td><td></td><td></td><td></td><td>-</td><td>+</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>5</td><td>6313</td><td>5421</td><td>892</td><td></td><td></td><td></td><td></td><td>-</td><td>+</td><td>-</td><td>-</td><td>-</td></tr><tr><td>6</td><td>6876</td><td>5918</td><td>958</td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>+</td><td>-</td><td>-</td></tr><tr><td>7</td><td>7293</td><td>6265</td><td>1028</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>+</td><td>-</td></tr><tr><td>8</td><td>6825</td><td>5851</td><td>974</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>+</td></tr><tr><td>9</td><td>6958</td><td>5949</td><td>1009</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-</td></tr></table>

![](/api/attachments/5Y5VYQQU/fulltext/images/29aeeac9f868c823187e2bb37ddbeafd25562f1ccb1634bd54c76c73a4bb2efc.jpg)  
(a) The reference Pareto front in 3D

![](/api/attachments/5Y5VYQQU/fulltext/images/3498255eaa80ee76bf246c2ebf20e4db36a4f80f754708270969384ae30d28f2.jpg)  
(b) (fpr × sr) projection

![](/api/attachments/5Y5VYQQU/fulltext/images/2e4fabc7dc50f5eb2311b8669285bfe49f8c543ebf99769d5e123f5632421703.jpg)  
Fig. 2. The reference Pareto front for ds3 dataset.  
(c) (fnr × sr) projection

dimensional projections are shown in Fig. 2 (b) and (c), corresponding to fpr × sr projection and fnr × sr projection, respectively. From Fig. 2 (b) we conclude that 1) the fpr could not be reduced to zero, even with all of the classi<sup>fi</sup>ers active, but it got very close to it; 2) the best result of fpr can be obtained with the value of sr in the range of [0.3,0.75] and in the range of [0.75,1.0], which is almost exactly zero; and 3) there are no points (solutions) in the objective space region with the value of sr below 0.3, as the performance of the fpr is too bad. From Fig. 2 (c) we conclude that 1) the performance of fnr decreases with the decreasing of sr, when sr is above 0.8; 2) the best result of fnr is obtained with the value of sr in the range of [0.3,0.5]; and 3) the performance of fnr is suppressed when the value of sr is below 0.3. Taking the conclusions of Fig. 2 together, some more conclusions can be made: 1) The fpr, fnr and sr are con<sup>fl</sup>icting with each other, as they cannot reach the best result simultaneously; 2) the highest value of sr can not guarantee the best performance of fpr and fnr; and 3) very few classi<sup>fi</sup>ers can reduce the performance of ensemble learning, as the performance of both fpr and fnr degrades when the value of sr is lower than 0.3. The solutions of

![](/api/attachments/5Y5VYQQU/fulltext/images/511f0eb35601763fd489bcace929dc43aa0b88b3eec7dd0ba3c5c527e9603d77.jpg)  
(a) Result of Two\_Arch2

![](/api/attachments/5Y5VYQQU/fulltext/images/c4bb9ca40acbddb91b6a726b5b5028d1608eac01eef6a035a11d805bcab885c2.jpg)  
(b) Result of NSGA-III

![](/api/attachments/5Y5VYQQU/fulltext/images/6551c34e9b3cc46ad4c44266fb1a9e106f54431c7f569994da5176706235dca3.jpg)  
(c) Result of MOEA/DD

![](/api/attachments/5Y5VYQQU/fulltext/images/5d3201ae01024a5e6e9d7099313689b533a0143699c4daac59ca91c7dfa176e8.jpg)  
(d) Result of RVEA

![](/api/attachments/5Y5VYQQU/fulltext/images/55ca3e96f48ddaed4189ddf2f638d9e38abbac96d1b6b1d850356c0fb138eefe.jpg)  
(e) Result of AR-MOEA

![](/api/attachments/5Y5VYQQU/fulltext/images/8752c8a5cc2e29b3ed65a482a66c72ed1f27eec56d13c66f94fae1dcaeba61ef.jpg)  
(f) Result of 3DFCH-EMOA  
Fig. 3. The Pareto front for ds3 dataset (three axis projection) obtained by six EMOAs.

Table 4  
Mean and standard deviation of Accuracy of ensemble methods on MNIST datasets.

<table><tr><td>Datasets Methods</td><td>ds1</td><td>ds2</td><td>ds3</td><td>ds4</td><td>ds5</td></tr><tr><td>MP</td><td>0.9889 ± 0.0028</td><td>0.9766 ± 0.0023</td><td>0.9355 ± 0.0051</td><td>0.9419 ± 0.0046</td><td>0.9570 ± 0.0035</td></tr><tr><td>KP</td><td>0.9829 ± 0.0038</td><td>0.9695 ± 0.0043</td><td>0.9204 ± 0.0046</td><td>0.9232 ± 0.0076</td><td>0.9503 ± 0.0051</td></tr><tr><td>SpaRSA</td><td>0.9921 ± 0.0054</td><td>0.9836 ± 0.0082</td><td>0.9583 ± 0.0201</td><td>0.9506 ± 0.0187</td><td>0.9741 ± 0.0132</td></tr><tr><td>OMP</td><td>0.9885 ± 0.0032</td><td>0.9765 ± 0.0024</td><td>0.9347 ± 0.0043</td><td>0.9418 ± 0.0046</td><td>0.9561 ± 0.0035</td></tr><tr><td>Two_Arch2</td><td>0.9957 ± 0.0006</td><td>0.9891 ± 0.0007</td><td>0.9704 ± 0.0016</td><td>0.9641 ± 0.0014</td><td>0.9787 ± 0.0016</td></tr><tr><td>NSGA-III</td><td>0.9952 ± 0.0007</td><td>0.9893 ± 0.0005</td><td>0.9696 ± 0.0021</td><td>0.9651 ± 0.0011</td><td>0.9798 ± 0.0012</td></tr><tr><td>MOEA/DD</td><td>0.9952 ± 0.0012</td><td>0.9893 ± 0.0009</td><td>0.9698 ± 0.0022</td><td>0.9644 ± 0.0018</td><td>0.9797 ± 0.0010</td></tr><tr><td>RVEA</td><td>0.9959 ± 0.0008</td><td>0.9886 ± 0.0007</td><td>0.9696 ± 0.0016</td><td>0.9639 ± 0.0015</td><td>0.9778 ± 0.0018</td></tr><tr><td>AR-MOEA</td><td>0.9959 ± 0.0009</td><td>0.9897 ± 0.0004</td><td>0.9702 ± 0.0015</td><td>0.9648 ± 0.0018</td><td>0.9795 ± 0.0009</td></tr><tr><td>3DFCH-EMOA</td><td>0.9962 ± 0.0005</td><td>0.9894 ± 0.0005</td><td>0.9707 ± 0.0018</td><td>0.9654 ± 0.0012</td><td>0.9802 ± 0.0013</td></tr><tr><td>Datasets Methods</td><td>ds6</td><td>ds7</td><td>ds8</td><td>ds9</td><td>Average</td></tr><tr><td>MP</td><td>0.9484 ± 0.0041</td><td>0.9714 ± 0.0023</td><td>0.9724 ± 0.0018</td><td>0.9472 ± 0.0024</td><td>0.9599</td></tr><tr><td>KP</td><td>0.9345 ± 0.0062</td><td>0.9622 ± 0.0048</td><td>0.9650 ± 0.0048</td><td>0.9416 ± 0.0036</td><td>0.9500</td></tr><tr><td>SpaRSA</td><td>0.9624 ± 0.0102</td><td>0.9748 ± 0.0123</td><td>0.9796 ± 0.0066</td><td>0.9578 ± 0.0052</td><td>0.9704</td></tr><tr><td>OMP</td><td>0.9488 ± 0.0043</td><td>0.9714 ± 0.0022</td><td>0.9726 ± 0.0016</td><td>0.9472 ± 0.0024</td><td>0.9597</td></tr><tr><td>Two_Arch2</td><td>0.9614 ± 0.0034</td><td>0.9830 ± 0.0008</td><td>0.9823 ± 0.0006</td><td>0.9569 ± 0.0016</td><td>0.9757</td></tr><tr><td>NSGA-III</td><td>0.9638 ± 0.0025</td><td>0.9828 ± 0.0006</td><td>0.9827 ± 0.0006</td><td>0.9579 ± 0.0015</td><td>0.9762</td></tr><tr><td>MOEA/DD</td><td>0.9630 ± 0.0022</td><td>0.9829 ± 0.0003</td><td>0.9823 ± 0.0007</td><td>0.9568 ± 0.0013</td><td>0.9759</td></tr><tr><td>RVEA</td><td>0.9604 ± 0.0020</td><td>0.9825 ± 0.0006</td><td>0.9820 ± 0.0005</td><td>0.9556 ± 0.0013</td><td>0.9751</td></tr><tr><td>AR-MOEA</td><td>0.9619 ± 0.0026</td><td>0.9828 ± 0.0006</td><td>0.9822 ± 0.0005</td><td>0.9569 ± 0.0013</td><td>0.9760</td></tr><tr><td>3DFCH-EMOA</td><td>0.9630 ± 0.0021</td><td>0.9832 ± 0.0006</td><td>0.9827 ± 0.0004</td><td>0.9569 ± 0.0016</td><td>0.9764</td></tr></table>

The Pareto front and reference Pareto front by six EMOAs are shown in Fig. 3, in which the points of the Pareto front are marked in red and the points of reference Pareto front are marked in blue. By Comparing all Pareto front in Fig. 3, we can see that 1) the solutions of Two\_Arch2, NSGA-III, MOEA/DD, and AR-MOEA convergence to the local area; 2) the solutions of RVEA and 3DFCH-EMOA are distributed in a wider space; 3) RVEA can <sup>fi</sup>nd solutions with low value of sr; and 4) 3DFCH EMOA can obtain solutions with a high and low value of sr.

each EMOA are discussed next.

Kappa. SpaRSA performs better than other CS and pruning ensemble methods.

As most of the datasets used in this part are large and the distributions of them are unbalanced, a small improvement of the accuracy and Kappa can cause many samples to be correctly classi<sup>fi</sup>ed and reduce misclassi<sup>fi</sup>cation costs greatly. To show the classi<sup>fi</sup>cation performance in more detail, the Precision, Recall and F-measure are compared in the following discussion.

Table 4 shows the mean and standard deviation of Accuracy. The average classi<sup>fi</sup>cation accuracy for each method is listed in the last column of the table. By comparing all the results, we can conclude that the methods of MOSEL outperform CS and pruning ensemble methods. 3DFCH-EMOA and NSGA-III outperform other methods for most of the datasets.

The comparison of Precision is shown in Table 6. From the table we can see that 1) the new proposed MOSEL can obtain a higher value of Precision than CS and pruning ensemble methods; 2) 3DFCH-EMOA algorithm performs the best on most of the compared datasets. 3) 3DFCH-EMOA and NSGA-III obtain the best and the second best result on the average Precision, respectively. 4) SpaRSA performs better than other CS and pruning algorithms.

The statistical results of Kappa are shown in Table 5. By comparing the results on the table, we can see that MOSEL methods outperform CS and pruning methods for most of the MNIST datasets. NSGA-III and 3DFCH-EMOA outperform other methods on most of these datasets. NSGA-III plays slightly better than 3DFCH-EMOA in the metric of

The statistical results of Recall are listed in Table 7. From the table, we can see that EMOAs methods (i.e., the new proposed MOSEL model) outperform other compared methods on Recall. Since in the most of MNIST datasets that we used in this paper, there are far more negative instances than positive samples, the increasing of Recall can largely decrease the number of misclassi<sup>fi</sup>ed samples. When comparing results for the Recall metric, we can also conclude that the proposed MOSEL methods have clear advantages in the MNIST datasets. While comparing the metric of Recall, NSGA-III can obtain the highest value of the average of Recall on all the compared datasets, and 3DFCH-EMOA performs better than other methods except NSGA-III.

Table 5  
Mean and standard deviation of Kappa of ensemble methods on MNIST datasets.

<table><tr><td>Datasets Methods</td><td>ds1</td><td>ds2</td><td>ds3</td><td>ds4</td><td>ds5</td></tr><tr><td>MP</td><td>0.9776 ± 0.0056</td><td>0.9493 ± 0.0050</td><td>0.8214 ± 0.0129</td><td>0.8089 ± 0.0159</td><td>0.8377 ± 0.0145</td></tr><tr><td>KP</td><td>0.9657 ± 0.0077</td><td>0.9338 ± 0.0092</td><td>0.7765 ± 0.0147</td><td>0.7474 ± 0.0233</td><td>0.8123 ± 0.0184</td></tr><tr><td>SpaRSA</td><td>0.9841 ± 0.0108</td><td>0.9644 ± 0.0177</td><td>0.8844 ± 0.0550</td><td>0.8395 ± 0.0588</td><td>0.9022 ± 0.0491</td></tr><tr><td>OMP</td><td>0.9769 ± 0.0064</td><td>0.9492 ± 0.0051</td><td>0.8193 ± 0.0109</td><td>0.8088 ± 0.0158</td><td>0.8342 ± 0.0136</td></tr><tr><td>Two_Arch2</td><td>0.9914 ± 0.0012</td><td>0.9763 ± 0.0016</td><td>0.9174 ± 0.0045</td><td>0.8805 ± 0.0050</td><td>0.9183 ± 0.0065</td></tr><tr><td>NSGA-III</td><td>0.9903 ± 0.0015</td><td>0.9767 ± 0.0012</td><td>0.9151 ± 0.0061</td><td>0.8844 ± 0.0037</td><td>0.9228 ± 0.0047</td></tr><tr><td>MOEA/DD</td><td>0.9904 ± 0.0024</td><td>0.9767 ± 0.0020</td><td>0.9159 ± 0.0063</td><td>0.8818 ± 0.0062</td><td>0.9222 ± 0.0042</td></tr><tr><td>RVEA</td><td>0.9917 ± 0.0016</td><td>0.9751 ± 0.0015</td><td>0.9150 ± 0.0046</td><td>0.8798 ± 0.0055</td><td>0.9147 ± 0.0074</td></tr><tr><td>AR-MOEA</td><td>0.9917 ± 0.0017</td><td>0.9775 ± 0.0009</td><td>0.9168 ± 0.0043</td><td>0.8832 ± 0.0062</td><td>0.9215 ± 0.0035</td></tr><tr><td>3DFCH-EMOA</td><td>0.9924 ± 0.0011</td><td>0.9769 ± 0.0012</td><td>0.9182 ± 0.0052</td><td>0.8852 ± 0.0043</td><td>0.9244 ± 0.0053</td></tr><tr><td>Datasets Methods</td><td>ds6</td><td>ds7</td><td>ds8</td><td>ds9</td><td>Average</td></tr><tr><td>MP</td><td>0.7539 ± 0.0216</td><td>0.8643 ± 0.0104</td><td>0.8601 ± 0.0096</td><td>0.6601 ± 0.0156</td><td>0.8370</td></tr><tr><td>KP</td><td>0.6718 ± 0.0441</td><td>0.8168 ± 0.0256</td><td>0.8213 ± 0.0256</td><td>0.6243 ± 0.0219</td><td>0.7967</td></tr><tr><td>SpaRSA</td><td>0.8183 ± 0.0453</td><td>0.8788 ± 0.0594</td><td>0.8965 ± 0.0330</td><td>0.7181 ± 0.0269</td><td>0.8762</td></tr><tr><td>OMP</td><td>0.7549 ± 0.0221</td><td>0.8645 ± 0.0101</td><td>0.8615 ± 0.0083</td><td>0.6601 ± 0.0156</td><td>0.8366</td></tr><tr><td>Two_Arch2</td><td>0.8060 ± 0.0200</td><td>0.9179 ± 0.0038</td><td>0.9091 ± 0.0034</td><td>0.6993 ± 0.0144</td><td>0.8907</td></tr><tr><td>NSGA-III</td><td>0.8200 ± 0.0144</td><td>0.9169 ± 0.0031</td><td>0.9112 ± 0.0032</td><td>0.7092 ± 0.0134</td><td>0.8941</td></tr><tr><td>MOEA/DD</td><td>0.8155 ± 0.0134</td><td>0.9175 ± 0.0018</td><td>0.9088 ± 0.0040</td><td>0.6989 ± 0.0117</td><td>0.8920</td></tr><tr><td>RVEA</td><td>0.8002 ± 0.0119</td><td>0.9156 ± 0.0033</td><td>0.9072 ± 0.0029</td><td>0.6881 ± 0.0120</td><td>0.8875</td></tr><tr><td>AR-MOEA</td><td>0.8091 ± 0.0156</td><td>0.9170 ± 0.0029</td><td>0.9087 ± 0.0027</td><td>0.7002 ± 0.0114</td><td>0.8917</td></tr><tr><td>3DFCH-EMOA</td><td>0.8149 ± 0.0126</td><td>0.9191 ± 0.0032</td><td>0.9110 ± 0.0023</td><td>0.6991 ± 0.0143</td><td>0.8935</td></tr></table>

Table 6  
Mean and standard deviation of Precision of ensemble methods on MNIST datasets.

<table><tr><td>Datasets Methods</td><td>ds1</td><td>ds2</td><td>ds3</td><td>ds4</td><td>ds5</td></tr><tr><td>MP</td><td>0.9902 ± 0.0026</td><td>0.9680 ± 0.0071</td><td>0.8805 ± 0.0219</td><td>0.9106 ± 0.0161</td><td>0.8917 ± 0.0176</td></tr><tr><td>KP</td><td>0.9848 ± 0.0069</td><td>0.9604 ± 0.0084</td><td>0.8620 ± 0.0202</td><td>0.8590 ± 0.0358</td><td>0.8707 ± 0.0275</td></tr><tr><td>SpaRSA</td><td>0.9928 ± 0.0056</td><td>0.9823 ± 0.0143</td><td>0.9334 ± 0.0482</td><td>0.9270 ± 0.0662</td><td>0.9520 ± 0.0500</td></tr><tr><td>OMP</td><td>0.9904 ± 0.0025</td><td>0.9679 ± 0.0093</td><td>0.8780 ± 0.0198</td><td>0.9106 ± 0.0161</td><td>0.8903 ± 0.0192</td></tr><tr><td>Two_Arch2</td><td>0.9949 ± 0.0010</td><td>0.9950 ± 0.0010</td><td>0.9649 ± 0.0048</td><td>0.9915 ± 0.0018</td><td>0.9840 ± 0.0023</td></tr><tr><td>NSGA-III</td><td>0.9951 ± 0.0010</td><td>0.9942 ± 0.0016</td><td>0.9631 ± 0.0049</td><td>0.9891 ± 0.0027</td><td>0.9846 ± 0.0023</td></tr><tr><td>MOEA/DD</td><td>0.9950 ± 0.0016</td><td>0.9942 ± 0.0013</td><td>0.9617 ± 0.0044</td><td>0.9911 ± 0.0020</td><td>0.9830 ± 0.0033</td></tr><tr><td>RVEA</td><td>0.9947 ± 0.0010</td><td>0.9941 ± 0.0017</td><td>0.9639 ± 0.0052</td><td>0.9919 ± 0.0021</td><td>0.9833 ± 0.0028</td></tr><tr><td>AR-MOEA</td><td>0.9954 ± 0.0010</td><td>0.9950 ± 0.0008</td><td>0.9639 ± 0.0043</td><td>0.9904 ± 0.0018</td><td>0.9838 ± 0.0032</td></tr><tr><td>3DFCH-EMOA</td><td>0.9952 ± 0.0009</td><td>0.9952 ± 0.0012</td><td>0.9656 ± 0.0047</td><td>0.9917 ± 0.0019</td><td>0.9849 ± 0.0023</td></tr><tr><td>Datasets Methods</td><td>ds6</td><td>ds7</td><td>ds8</td><td>ds9</td><td>Average</td></tr><tr><td>MP</td><td>0.8586 ± 0.0243</td><td>0.9026 ± 0.0142</td><td>0.9174 ± 0.0117</td><td>0.8113 ± 0.0276</td><td>0.9034</td></tr><tr><td>KP</td><td>0.8340 ± 0.0338</td><td>0.8823 ± 0.0169</td><td>0.8888 ± 0.0249</td><td>0.7744 ± 0.0393</td><td>0.8796</td></tr><tr><td>SpaRSA</td><td>0.9457 ± 0.0678</td><td>0.9306 ± 0.0528</td><td>0.9552 ± 0.0376</td><td>0.9343 ± 0.0684</td><td>0.9504</td></tr><tr><td>OMP</td><td>0.8628 ± 0.0255</td><td>0.9028 ± 0.0138</td><td>0.9171 ± 0.0118</td><td>0.8113 ± 0.0276</td><td>0.9035</td></tr><tr><td>Two_Arch2</td><td>0.9804 ± 0.0044</td><td>0.9730 ± 0.0042</td><td>0.9812 ± 0.0023</td><td>0.9773 ± 0.0038</td><td>0.9825</td></tr><tr><td>NSGA-III</td><td>0.9806 ± 0.0031</td><td>0.9731 ± 0.0025</td><td>0.9795 ± 0.0026</td><td>0.9725 ± 0.0064</td><td>0.9813</td></tr><tr><td>MOEA/DD</td><td>0.9796 ± 0.0053</td><td>0.9709 ± 0.0035</td><td>0.9803 ± 0.0032</td><td>0.9747 ± 0.0040</td><td>0.9812</td></tr><tr><td>RVEA</td><td>0.9806 ± 0.0037</td><td>0.9720 ± 0.0040</td><td>0.9805 ± 0.0021</td><td>0.9764 ± 0.0063</td><td>0.9819</td></tr><tr><td>AR-MOEA</td><td>0.9787 ± 0.0041</td><td>0.9726 ± 0.0043</td><td>0.9794 ± 0.0019</td><td>0.9740 ± 0.0056</td><td>0.9815</td></tr><tr><td>3DFCH-EMOA</td><td>0.9826 ± 0.0039</td><td>0.9740 ± 0.0023</td><td>0.9816 ± 0.0022</td><td>0.9769 ± 0.0056</td><td>0.9831</td></tr></table>

performance are con<sup>fl</sup>icting with each other, a good ensemble method should <sup>fi</sup>nd the best trade-o<sup>f</sup>s between them. From the performed experiments we demonstrate that EMOAs are suitable optimization techniques to tackle sparse ensemble problems.

The F-measure is compared in Table 8. From the table we can make some conclusions: 1) The proposed MOSEL outperforms other methods on most of the datasets; 2) NSGA-III and 3DFCH-EMOA can obtain better results than other MOSEL methods; 3) NSGA-III can obtain the best result on the average F-measure of all these datasets.

As 3DFCH-EMOA has good performance on most of these datasets, a more comprehensive comparison between 3DFCH-EMOA and other ensemble methods is presented in Table 10, which shows the corresponding Wilcoxon sum-rank test [36] results. By comparing the results we can <sup>fi</sup>nd that 3DFCH-EMOA outperforms CS and pruning ensemble methods signi<sup>fi</sup>cantly on most of the metrics except the non-zero metric on most of the datasets.

Table 9 shows the mean value and standard deviation of non-zero classi<sup>fi</sup>ers of the ensemble. By comparing the results we can conclude that KP and OMP have good performance on sparsity. However, they perform poorly on other metrics. If all values in the table are considered, we can conclude that KP has the best sparseness performance. However, the classi<sup>fi</sup>cation accuracy values of OMP and KP are lower than those of MOSEL methods, as these two algorithms do not <sup>fi</sup>nd good solutions that balance the performance between classi<sup>fi</sup>cation accuracy and ensemble sparsity. As the performance of sparsity and classi<sup>fi</sup>cation

## 3.5. Experimental results of image change detection

Remote sensing image change detection is a real-world problem that aims to <sup>fi</sup>nd out the change information that has occurred between two images of the same area taken at di<sup>f</sup>erent times [42]. It has been applied in many areas, including disaster monitoring, changed target detection and supervision of country resources [43]. Supervised methods have been widely used for remote sensing image change detection [44], as a small amount of labelled data can be used for model training and then the built model can be applied for large-scale image change detection. The change detection problem is an unbalanced classi<sup>fi</sup>cation problem as the proportion of the change area when compared to the total observed area is small. In this part, both synthetic aperture radar (SAR) [45] and optical images are used for the proposed methods evaluation.

Mean and standard deviation of Recall of ensemble methods on MNIST datasets.

<table><tr><td>Datasets Methods</td><td>ds1</td><td>ds2</td><td>ds3</td><td>ds4</td><td>ds5</td></tr><tr><td>MP</td><td>0.9859 ± 0.0054</td><td>0.9674 ± 0.0068</td><td>0.8479 ± 0.0149</td><td>0.7874 ± 0.0195</td><td>0.8371 ± 0.0277</td></tr><tr><td>KP</td><td>0.9787 ± 0.0052</td><td>0.9551 ± 0.0094</td><td>0.7980 ± 0.0296</td><td>0.7395 ± 0.0212</td><td>0.8153 ± 0.0212</td></tr><tr><td>SpaRSA</td><td>0.9902 ± 0.0061</td><td>0.9722 ± 0.0090</td><td>0.8910 ± 0.0363</td><td>0.8198 ± 0.0321</td><td>0.8858 ± 0.0356</td></tr><tr><td>OMP</td><td>0.9849 ± 0.0066</td><td>0.9674 ± 0.0080</td><td>0.8471 ± 0.0149</td><td>0.7873 ± 0.0194</td><td>0.8326 ± 0.0232</td></tr><tr><td>Two_Arch2</td><td>0.9960 ± 0.0011</td><td>0.9747 ± 0.0018</td><td>0.9101 ± 0.0056</td><td>0.8278 ± 0.0069</td><td>0.8832 ± 0.0102</td></tr><tr><td>NSGA-III</td><td>0.9945 ± 0.0010</td><td>0.9761 ± 0.0009</td><td>0.9085 ± 0.0073</td><td>0.8352 ± 0.0049</td><td>0.8896 ± 0.0079</td></tr><tr><td>MOEA/DD</td><td>0.9948 ± 0.0023</td><td>0.9761 ± 0.0020</td><td>0.9108 ± 0.0080</td><td>0.8300 ± 0.0082</td><td>0.8900 ± 0.0069</td></tr><tr><td>RVEA</td><td>0.9965 ± 0.0014</td><td>0.9743 ± 0.0014</td><td>0.9075 ± 0.0061</td><td>0.8265 ± 0.0084</td><td>0.8782 ± 0.0112</td></tr><tr><td>AR-MOEA</td><td>0.9957 ± 0.0013</td><td>0.9763 ± 0.0011</td><td>0.9102 ± 0.0061</td><td>0.8325 ± 0.0080</td><td>0.8884 ± 0.0070</td></tr><tr><td>3DFCH-EMOA</td><td>0.9968 ± 0.0010</td><td>0.9754 ± 0.0009</td><td>0.9106 ± 0.0056</td><td>0.8343 ± 0.0061</td><td>0.8918 ± 0.0084</td></tr><tr><td>Datasets Methods</td><td>ds6</td><td>ds7</td><td>ds8</td><td>ds9</td><td>Average</td></tr><tr><td>MP</td><td>0.7204 ± 0.0328</td><td>0.8597 ± 0.0104</td><td>0.8375 ± 0.0138</td><td>0.5984 ± 0.0225</td><td>0.8269</td></tr><tr><td>KP</td><td>0.6185 ± 0.0636</td><td>0.7989 ± 0.0380</td><td>0.7985 ± 0.0309</td><td>0.5692 ± 0.0262</td><td>0.7857</td></tr><tr><td>SpaRSA</td><td>0.7555 ± 0.0260</td><td>0.8585 ± 0.0526</td><td>0.8652 ± 0.0235</td><td>0.6143 ± 0.0195</td><td>0.8503</td></tr><tr><td>OMP</td><td>0.7189 ± 0.0324</td><td>0.8597 ± 0.0104</td><td>0.8400 ± 0.0116</td><td>0.5984 ± 0.0225</td><td>0.8263</td></tr><tr><td>Two_Arch2</td><td>0.7158 ± 0.0290</td><td>0.8860 ± 0.0068</td><td>0.8642 ± 0.0053</td><td>0.5714 ± 0.0182</td><td>0.8477</td></tr><tr><td>NSGA-III</td><td>0.7348 ± 0.0208</td><td>0.8843 ± 0.0052</td><td>0.8689 ± 0.0058</td><td>0.5851 ± 0.0173</td><td>0.8530</td></tr><tr><td>MOEA/DD</td><td>0.7291 ± 0.0201</td><td>0.8873 ± 0.0052</td><td>0.8644 ± 0.0058</td><td>0.5717 ± 0.0148</td><td>0.8505</td></tr><tr><td>RVEA</td><td>0.7075 ± 0.0176</td><td>0.8832 ± 0.0058</td><td>0.8617 ± 0.0050</td><td>0.5583 ± 0.0158</td><td>0.8437</td></tr><tr><td>AR-MOEA</td><td>0.7208 ± 0.0221</td><td>0.8849 ± 0.0069</td><td>0.8649 ± 0.0035</td><td>0.5736 ± 0.0140</td><td>0.8497</td></tr><tr><td>3DFCH-EMOA</td><td>0.7265 ± 0.0185</td><td>0.8873 ± 0.0054</td><td>0.8668 ± 0.0041</td><td>0.5712 ± 0.0185</td><td>0.8512</td></tr></table>

Table 8  
Mean and standard deviation of F-measure of ensemble methods on MNIST datasets.

<table><tr><td>Datasets Methods</td><td>ds1</td><td>ds2</td><td>ds3</td><td>ds4</td><td>ds5</td></tr><tr><td>MP</td><td>0.9881 ± 0.0030</td><td>0.9677 ± 0.0032</td><td>0.8636 ± 0.0096</td><td>0.8444 ± 0.0132</td><td>0.8631 ± 0.0125</td></tr><tr><td>KP</td><td>0.9817 ± 0.0041</td><td>0.9577 ± 0.0059</td><td>0.8282 ± 0.0122</td><td>0.7943 ± 0.0186</td><td>0.8417 ± 0.0154</td></tr><tr><td>SpaRSA</td><td>0.9915 ± 0.0058</td><td>0.9772 ± 0.0113</td><td>0.9116 ± 0.0418</td><td>0.8699 ± 0.0471</td><td>0.9175 ± 0.0413</td></tr><tr><td>OMP</td><td>0.9876 ± 0.0035</td><td>0.9676 ± 0.0032</td><td>0.8620 ± 0.0081</td><td>0.8443 ± 0.0131</td><td>0.8602 ± 0.0116</td></tr><tr><td>Two_Arch2</td><td>0.9954 ± 0.0006</td><td>0.9848 ± 0.0010</td><td>0.9367 ± 0.0034</td><td>0.9023 ± 0.0041</td><td>0.9308 ± 0.0056</td></tr><tr><td>NSGA-III</td><td>0.9948 ± 0.0008</td><td>0.9851 ± 0.0007</td><td>0.9350 ± 0.0047</td><td>0.9056 ± 0.0031</td><td>0.9347 ± 0.0040</td></tr><tr><td>MOEA/DD</td><td>0.9949 ± 0.0013</td><td>0.9851 ± 0.0013</td><td>0.9356 ± 0.0049</td><td>0.9034 ± 0.0052</td><td>0.9342 ± 0.0036</td></tr><tr><td>RVEA</td><td>0.9956 ± 0.0009</td><td>0.9841 ± 0.0010</td><td>0.9348 ± 0.0036</td><td>0.9017 ± 0.0046</td><td>0.9278 ± 0.0063</td></tr><tr><td>AR-MOEA</td><td>0.9956 ± 0.0009</td><td>0.9856 ± 0.0006</td><td>0.9363 ± 0.0033</td><td>0.9046 ± 0.0052</td><td>0.9336 ± 0.0030</td></tr><tr><td>3DFCH-EMOA</td><td>0.9960 ± 0.0006</td><td>0.9852 ± 0.0008</td><td>0.9373 ± 0.0040</td><td>0.9062 ± 0.0036</td><td>0.9360 ± 0.0046</td></tr><tr><td>Datasets Methods</td><td>ds6</td><td>ds7</td><td>ds8</td><td>ds9</td><td>Average</td></tr><tr><td>MP</td><td>0.7829 ± 0.0195</td><td>0.8805 ± 0.0091</td><td>0.8756 ± 0.0086</td><td>0.6883 ± 0.0146</td><td>0.8616</td></tr><tr><td>KP</td><td>0.7076 ± 0.0422</td><td>0.8381 ± 0.0229</td><td>0.8409 ± 0.0230</td><td>0.6553 ± 0.0202</td><td>0.8273</td></tr><tr><td>SpaRSA</td><td>0.8393 ± 0.0394</td><td>0.8931 ± 0.0524</td><td>0.9079 ± 0.0293</td><td>0.7400 ± 0.0239</td><td>0.8942</td></tr><tr><td>OMP</td><td>0.7837 ± 0.0198</td><td>0.8807 ± 0.0089</td><td>0.8768 ± 0.0074</td><td>0.6882 ± 0.0146</td><td>0.8612</td></tr><tr><td>Two_Arch2</td><td>0.8271 ± 0.0184</td><td>0.9275 ± 0.0034</td><td>0.9190 ± 0.0030</td><td>0.7209 ± 0.0138</td><td>0.9049</td></tr><tr><td>NSGA-III</td><td>0.8400 ± 0.0132</td><td>0.9266 ± 0.0028</td><td>0.9209 ± 0.0029</td><td>0.7304 ± 0.0129</td><td>0.9081</td></tr><tr><td>MOEA/DD</td><td>0.8358 ± 0.0123</td><td>0.9272 ± 0.0016</td><td>0.9187 ± 0.0036</td><td>0.7206 ± 0.0113</td><td>0.9062</td></tr><tr><td>RVEA</td><td>0.8218 ± 0.0110</td><td>0.9255 ± 0.0029</td><td>0.9172 ± 0.0026</td><td>0.7102 ± 0.0116</td><td>0.9021</td></tr><tr><td>AR-MOEA</td><td>0.8300 ± 0.0143</td><td>0.9267 ± 0.0026</td><td>0.9186 ± 0.0024</td><td>0.7219 ± 0.0109</td><td>0.9059</td></tr><tr><td>3DFCH-EMOA</td><td>0.8353 ± 0.0115</td><td>0.9286 ± 0.0029</td><td>0.9206 ± 0.0021</td><td>0.7207 ± 0.0138</td><td>0.9073</td></tr></table>

## 3.5.1. Datasets description

The second dataset is the Bern dataset of two SAR images with a spatial resolution of 10 m × 10 m and a spatial size of 301 × 301. They were acquired over the city of Bern, Switzerland by the European Remote Sensing 2 satellite SAR sensor in April and May 1999, respec tively. Fig. 5 shows the two images, manually de<sup>fi</sup>ned reference map and training image patch with a spatial size 100 × 100 in the log ratio di<sup>f</sup>erence image.

Six pairs of remote sensing images are used for classi<sup>fi</sup>cation performance evaluation, details are described in the following. The <sup>fi</sup>rst dataset is the Ottawa dataset of two SAR images with a spatial resolution of 10 m × 10 m and a spatial size of $2 9 0 \times 3 5 0 ,$ acquired in July and August 1997, respectively. They were acquired over the city of Ottawa by the Radarsar SAR sensor and were provided by the Defence Research and Development Canada (DRDC)-Ottawa. Panels (a) and (b) in Fig. 4 present the <sup>fl</sup>ood-a<sup>fl</sup>icted areas and $\mathrm { F i g . ~ 4 }$ (c) shows the manually de<sup>fi</sup>ned reference map. The sample patch for model training and validation is marked in blue with a spatial size $1 0 0 \times 1 0 0$ in the log

The third dataset is the Mexico dataset of two optical images acquired by Landsat-7 (US satellite) in April 2000 and May 2002, respectively. These two images are extracted from Band 4 of the ETM+ images. The sizes of both images are 512 × 512 pixels. This dataset shows the vegetation damage after the forest <sup>fi</sup>re in urban Mexico. Panels (a)–(d) in Fig. 6 show the two images, reference map and example patch with a spatial size 100 × 100, respectively.

The 4–6th datasets are the selected from the Yellow River in eastern China of two SAR images captured by Radarsat-2 (Canadian satellite) with a spatial resolution $8 \mathrm { ~ m ~ } \times 8 \mathrm { m }$ in July 2008 and June 2009, respectively. Note that the two SAR images are single-look and four-look,

Table 9  
Mean and standard deviation of non-zero ensemble weight for each method on MNIST datasets.

<table><tr><td>Datasets Methods</td><td>ds1</td><td>ds2</td><td>ds3</td><td>ds4</td><td>ds5</td></tr><tr><td>MP</td><td> $26.00 \pm 0.00$ </td><td> $26.00 \pm 0.00$ </td><td> $26.00 \pm 0.00$ </td><td> $26.00 \pm 0.00$ </td><td> $26.00 \pm 0.00$ </td></tr><tr><td>KP</td><td> $1.00 \pm 0.00$ </td><td> $1.00 \pm 0.00$ </td><td> $1.00 \pm 0.00$ </td><td> $1.00 \pm 0.00$ </td><td> $1.00 \pm 0.00$ </td></tr><tr><td>SpaRSA</td><td> $19.70 \pm 16.79$ </td><td> $11.80 \pm 11.30$ </td><td> $20.20 \pm 15.99$ </td><td> $14.90 \pm 14.95$ </td><td> $24.40 \pm 17.25$ </td></tr><tr><td>OMP</td><td> $1.00 \pm 0.00$ </td><td> $1.00 \pm 0.00$ </td><td> $2.00 \pm 0.00$ </td><td> $1.60 \pm 0.52$ </td><td> $1.00 \pm 0.00$ </td></tr><tr><td>Two_Arch2</td><td> $41.30 \pm 5.68$ </td><td> $42.30 \pm 7.67$ </td><td> $44.20 \pm 4.83$ </td><td> $41.50 \pm 3.78$ </td><td> $39.20 \pm 5.22$ </td></tr><tr><td>NSGA-III</td><td> $15.10 \pm 3.41$ </td><td> $19.30 \pm 2.79$ </td><td> $27.10 \pm 3.90$ </td><td> $25.70 \pm 4.83$ </td><td> $28.40 \pm 2.41$ </td></tr><tr><td>MOEA/DD</td><td> $13.20 \pm 3.94$ </td><td> $25.00 \pm 5.58$ </td><td> $34.50 \pm 10.06$ </td><td> $50.70 \pm 15.56$ </td><td> $33.30 \pm 8.65$ </td></tr><tr><td>RVEA</td><td> $67.40 \pm 11.35$ </td><td> $53.30 \pm 10.98$ </td><td> $45.20 \pm 5.14$ </td><td> $49.70 \pm 8.12$ </td><td> $48.70 \pm 5.50$ </td></tr><tr><td>AR-MOEA</td><td> $24.90 \pm 4.48$ </td><td> $24.00 \pm 3.02$ </td><td> $31.70 \pm 4.81$ </td><td> $30.50 \pm 3.24$ </td><td> $34.30 \pm 4.92$ </td></tr><tr><td>3DFCH-EMOA</td><td> $83.70 \pm 20.23$ </td><td> $58.50 \pm 25.52$ </td><td> $72.40 \pm 24.09$ </td><td> $64.10 \pm 18.88$ </td><td> $45.20 \pm 8.61$ </td></tr><tr><td>Datasets Methods</td><td>ds6</td><td>ds7</td><td>ds8</td><td>ds9</td><td>Average</td></tr><tr><td>MP</td><td> $26.00 \pm 0.00$ </td><td> $26.00 \pm 0.00$ </td><td> $26.00 \pm 0.00$ </td><td> $26.00 \pm 0.00$ </td><td> $26.00$ </td></tr><tr><td>KP</td><td> $1.00 \pm 0.00$ </td><td> $1.00 \pm 0.00$ </td><td> $1.00 \pm 0.00$ </td><td> $1.00 \pm 0.00$ </td><td> $1.00$ </td></tr><tr><td>SpaRSA</td><td> $26.30 \pm 15.30$ </td><td> $21.30 \pm 16.60$ </td><td> $19.80 \pm 16.42$ </td><td> $28.30 \pm 16.81$ </td><td> $20.74$ </td></tr><tr><td>OMP</td><td> $2.00 \pm 0.00$ </td><td> $1.00 \pm 0.00$ </td><td> $1.00 \pm 0.00$ </td><td> $2.00 \pm 0.00$ </td><td> $1.40$ </td></tr><tr><td>Two_Arch2</td><td> $41.70 \pm 6.72$ </td><td> $41.50 \pm 2.76$ </td><td> $40.80 \pm 2.86$ </td><td> $38.80 \pm 4.69$ </td><td> $41.26$ </td></tr><tr><td>NSGA-III</td><td> $27.00 \pm 3.50$ </td><td> $26.80 \pm 3.79$ </td><td> $27.30 \pm 4.62$ </td><td> $28.10 \pm 3.28$ </td><td> $24.98$ </td></tr><tr><td>MOEA/DD</td><td> $34.00 \pm 4.74$ </td><td> $45.00 \pm 11.85$ </td><td> $41.00 \pm 16.25$ </td><td> $37.40 \pm 9.36$ </td><td> $34.90$ </td></tr><tr><td>RVEA</td><td> $47.60 \pm 6.22$ </td><td> $50.40 \pm 3.66$ </td><td> $52.40 \pm 7.32$ </td><td> $49.20 \pm 8.13$ </td><td> $51.54$ </td></tr><tr><td>AR-MOEA</td><td> $34.10 \pm 3.81$ </td><td> $31.70 \pm 2.63$ </td><td> $31.60 \pm 4.95$ </td><td> $32.80 \pm 4.21$ </td><td> $30.62$ </td></tr><tr><td>3DFCH-EMOA</td><td> $45.70 \pm 7.66$ </td><td> $58.50 \pm 25.10$ </td><td> $48.60 \pm 12.28$ </td><td> $50.00 \pm 9.09$ </td><td> $58.52$ </td></tr></table>

Table 10  
Wilcoxon sum-rank test on MNIST datasets: each x-y-z in following table means 3DFCH-EMOA wins x times, losses y times, draws z times.

<table><tr><td></td><td>MP</td><td>KP</td><td>SpaRSA</td><td>OMP</td><td>NSGA-III</td><td>Two_Arch2</td><td>MOEA/DD</td><td>RVEA</td><td>AR-MOEA</td></tr><tr><td>Accuracy</td><td>9-0-0</td><td>9-0-0</td><td>5-1-3</td><td>9-0-0</td><td>2-0-7</td><td>1-0-8</td><td>1-0-8</td><td>7-0-2</td><td>1-0-8</td></tr><tr><td>Kappa</td><td>9-0-0</td><td>9-0-0</td><td>5-1-3</td><td>9-0-0</td><td>2-0-7</td><td>1-0-8</td><td>1-0-8</td><td>6-0-3</td><td>1-0-8</td></tr><tr><td>Precision</td><td>9-0-0</td><td>9-0-0</td><td>7-0-2</td><td>9-0-0</td><td>0-0-9</td><td>1-0-8</td><td>1-0-8</td><td>2-0-7</td><td>1-0-8</td></tr><tr><td>Recall</td><td>7-1-1</td><td>8-0-1</td><td>1-3-5</td><td>7-1-1</td><td>0-0-9</td><td>1-0-8</td><td>1-0-8</td><td>4-0-5</td><td>0-0-9</td></tr><tr><td>F-measure</td><td>9-0-0</td><td>9-0-0</td><td>1-1-7</td><td>9-0-0</td><td>2-0-7</td><td>1-0-8</td><td>1-0-8</td><td>6-0-3</td><td>1-0-8</td></tr><tr><td>Non-zero</td><td>0-9-0</td><td>0-9-0</td><td>0-9-0</td><td>0-9-0</td><td>0-4-5</td><td>0-9-0</td><td>0-6-3</td><td>0-3-6</td><td>0-9-0</td></tr></table>

![](/api/attachments/5Y5VYQQU/fulltext/images/894907f84af437eae6b828978517f0e0aa7d5d598407a74c98b2fe2bfb916bf6.jpg)  
(a)

![](/api/attachments/5Y5VYQQU/fulltext/images/7507cf00d75dfc04562adcd44bd80432ae59d7c5e7b57c09006f1a81aa17db86.jpg)  
(b)  
(c)

![](/api/attachments/5Y5VYQQU/fulltext/images/bb28cc6bd21e70cf9c8a29d12e5ad332ad87a120f42fadbb9fa982939ab352b2.jpg)  
(d)

Fig. 4. Multitemporal images relating to Ottawa. (a) Image acquired in July 1997, during the summer <sup>fl</sup>ooding, (b) image acquired in August 1997, after the summer <sup>fl</sup>ooding, (c) ground truth, (d) initial di<sup>f</sup>erence image obtained via the log ratio operator and examples marked in blue extracted for model training and validation. (For interpretation of the references to color in this <sup>fi</sup>gure legend, the reader is referred to the web version of this article.)  
![](/api/attachments/5Y5VYQQU/fulltext/images/f31538d937af28713f0c6629533214c00e60cdf7f1ea95233058669b8044db7e.jpg)  
(a)

![](/api/attachments/5Y5VYQQU/fulltext/images/a884646f9cd7ca0db4a20ea58be6fcd950452eca70c1e07b93d8435d8fa74818.jpg)  
(b)

![](/api/attachments/5Y5VYQQU/fulltext/images/b181b18ea2935c2c86f06f33462271ed25da343172ee26257ec8ea42df1aa338.jpg)  
(c)

![](/api/attachments/5Y5VYQQU/fulltext/images/b85384c214e710ffcd03cd79637464726af562eba9a1dcd1c091f9a1db3b1dab.jpg)  
(d)

Fig. 5. Multitemporal images relating to the city of Bern. (a) Image acquired in April 1999, (b) image acquired in May 1999, (c) ground truth and (d) example extracted for model training and validation.  
![](/api/attachments/5Y5VYQQU/fulltext/images/39c17dea8c2665177366e7d2b5882fab83e4a1dcb7cf90e105188c034aac056f.jpg)  
(a)

![](/api/attachments/5Y5VYQQU/fulltext/images/97ed960a446dd3e85aae3d88dc0ea17f6e91a5ffc077253b3573730133eebc6d.jpg)  
(b)

![](/api/attachments/5Y5VYQQU/fulltext/images/25b50bafc3de229b23fedaf2d399bec52d6d76260627a9a2086463f4aacf4d3f.jpg)  
(c)

![](/api/attachments/5Y5VYQQU/fulltext/images/d70faab49a12aca3d5c42d1f011fc34c7f165e7a0085f087dbccd768a02c0493.jpg)  
(d)  
Fig. 6. Multitemporal images relating to the city of Mexico. (a) Optical image acquired in 2000, (b) optical image acquired in 2002, (c) ground truth and (d) example extracted for model training and validation.

respectively, which increases the di<sup>fi</sup>culty of change detection. These datasets include di<sup>f</sup>erent typical areas, including farmlands, coastline and inland water. Fig. 7 shows the changed areas that appear as newly reclaimed farmlands, with a spatial size 306 × 291. Fig. 8 shows the coastline where the changed areas are relatively small, with a spatial size 450 × 280. Inland water where the changed areas are concentrated on the borderline of the river is shown in Fig. 9. The spatial size of Inland water is 291. × 444

![](/api/attachments/5Y5VYQQU/fulltext/images/835af0319c637cb5c2b6fe3bd9a792cd0920ad5ae36b068831f63b1d5d259839.jpg)  
(a)

![](/api/attachments/5Y5VYQQU/fulltext/images/494a1cad1ca8fdabae765f9452e7fd7e9fb1fbe6af2bf2b43aaaf7be9dba934f.jpg)  
(b)

![](/api/attachments/5Y5VYQQU/fulltext/images/1458aa6c5c0b0d92ac908319af91ba5da84fca3bef4ac16b375177c22d8797bf.jpg)  
(c)

![](/api/attachments/5Y5VYQQU/fulltext/images/3b5009526a2ce5809cf9c48a80cb153939b2d111896c2131282616e4313bd5a9.jpg)  
(d)

Fig. 7. Multitemporal images relating to Farmland of Yellow River Estuary. (a) SAR image acquired in June 2008, (b) SAR image acquired in June 2009, (c) ground truth and (d) examples extracted for model training and validation.  
![](/api/attachments/5Y5VYQQU/fulltext/images/7317eaceaa839fd1f18104b3543e216891cdd852396d3d63a7eb6c8e99d09ceb.jpg)  
(a)

![](/api/attachments/5Y5VYQQU/fulltext/images/b46f7320b9563c98128f56bb5d671ea65ae68b5b75225bd2c0dbf2959666914a.jpg)  
(b)

![](/api/attachments/5Y5VYQQU/fulltext/images/876f7ad7b35b79bd4414dc1ca5b813280e5481484483240e95eaeff99cd92679.jpg)  
(c)

![](/api/attachments/5Y5VYQQU/fulltext/images/39c7589e13132297f27ed1ec7e5455dba22c3e0a49cd5a05d169168e7685b5cc.jpg)  
(d)

Fig. 8. Multitemporal images relating to Coastline of Yellow River Estuary. (a) SAR image acquired in June 2008, (b) SAR image acquired in June 2009, (c) ground truth and (d) examples extracted for model training and validation.  
![](/api/attachments/5Y5VYQQU/fulltext/images/6a420f2e427f2dcb1aadc5a5a71ab4c66559b215909f3967ad3affe71d68bc55.jpg)  
(a)

![](/api/attachments/5Y5VYQQU/fulltext/images/9b4c26ea3391c43ab5c49f72e90c0eaccd77b68d4e6919afbfd5c479c1ab68a2.jpg)  
(b)

![](/api/attachments/5Y5VYQQU/fulltext/images/014c3af0cdd74ad56fc156ea179e4db9d49a173a443f1b63dfff1064c85bc77d.jpg)  
(c)

![](/api/attachments/5Y5VYQQU/fulltext/images/e9215a10a5a8c6b0f6335d79ebac22fc5f32f00c6590ce4ab92b200dd3321402.jpg)  
(d)  
Fig. 9. Multitemporal images relating to Inland water of Yellow River Estuary. (a) SAR image acquired in June 2008, (b) SAR image acquired in June 2009, (c) ground truth and (d) examples extracted for model training and validation.

Table 11  
The details of remote sensing datasets.

<table><tr><td rowspan="2"></td><td colspan="6">Datasets</td></tr><tr><td>Ottawa</td><td>Bern</td><td>Mexico</td><td>Farmland</td><td>Coastline</td><td>Inland water</td></tr><tr><td>Image spatial size</td><td>290 × 350</td><td>301 × 301</td><td>512 × 512</td><td>306 × 291</td><td>450 × 280</td><td>291 × 444</td></tr><tr><td>Sample patch size</td><td>100 × 100</td><td>100 × 100</td><td>100 × 100</td><td>80 × 80</td><td>80 × 80</td><td>100 × 100</td></tr></table>

The spatial and sample patch sizes of these remote sensing dataset are listed in Table 11. In this part, discrete wavelet transform [46], grey-level co-occurrence matrix (CLCM) [47] and Gabor <sup>fi</sup>lter bank [6] are selected to extract features for each pixel of log di<sup>f</sup>erence images. The dimension of the feature is 38, i.e., each pixel of the log di<sup>f</sup>erence image is represented by a 38 dimension vector. For each dataset, 2/3 samples from the training patch are randomly selected for model training and the remaining 1/3 samples are selected for validation. The whole log di<sup>f</sup>erence images are used for testing.

## 3.5.2. Experimental results and discussion

The mean and standard deviation of the classi<sup>fi</sup>cation accuracy are shown in Table 12. By comparing all the results we can conclude that 1) OMP performs the best on Ottawa and Farmland datasets; 2) the methods of MOSEL outperform CS and pruning ensemble methods on most of the datasets except Ottawa and Farmland; and 3) 3DFCH-EMOA can obtain the highest accuracy except for the Farmland dataset.

Table 12  
Mean and standard deviation of Accuracy of ensemble methods on change detection datasets.

<table><tr><td>Datasets Methods</td><td>Ottawa</td><td>Bern</td><td>Mexico</td><td>Farmland</td><td>Coastline</td><td>Inland water</td><td>Average</td></tr><tr><td>MP</td><td>0.9190±0.0069</td><td>0.9880±0.0020</td><td>0.9665±0.0043</td><td>0.9145±0.0149</td><td>0.9855±0.0062</td><td>0.9693±0.0027</td><td>0.9571</td></tr><tr><td>KP</td><td>0.8882±0.0657</td><td>0.9898±0.0014</td><td>0.9670±0.0059</td><td>0.9204±0.0154</td><td>0.9866±0.0054</td><td>0.9659±0.0078</td><td>0.9530</td></tr><tr><td>SpaRSA</td><td>0.9123±0.0235</td><td>0.9909±0.0031</td><td>0.9636±0.0071</td><td>0.9186±0.0108</td><td>0.9831±0.0086</td><td>0.9677±0.0079</td><td>0.9560</td></tr><tr><td>OMP</td><td>0.9276±0.0023</td><td>0.9887±0.0018</td><td>0.9682±0.0038</td><td>0.9239±0.0050</td><td>0.9855±0.0061</td><td>0.9694±0.0029</td><td>0.9605</td></tr><tr><td>Two_Arch2</td><td>0.9263±0.0027</td><td>0.9931±0.0004</td><td>0.9725±0.0015</td><td>0.9205±0.0020</td><td>0.9908±0.0006</td><td>0.9731±0.0009</td><td>0.9627</td></tr><tr><td>NSGA-III</td><td>0.9267±0.0030</td><td>0.9930±0.0005</td><td>0.9723±0.0014</td><td>0.9227±0.0034</td><td>0.9907±0.0008</td><td>0.9735±0.0010</td><td>0.9632</td></tr><tr><td>MOEA/DD</td><td>0.9275±0.0018</td><td>0.9932±0.0004</td><td>0.9723±0.0014</td><td>0.9229±0.0030</td><td>0.9911±0.0006</td><td>0.9739±0.0010</td><td>0.9635</td></tr><tr><td>RVEA</td><td>0.9262±0.0012</td><td>0.9929±0.0004</td><td>0.9722±0.0013</td><td>0.9206±0.0028</td><td>0.9909±0.0006</td><td>0.9735±0.0009</td><td>0.9627</td></tr><tr><td>AR-MOEA</td><td>0.9268±0.0025</td><td>0.9929±0.0004</td><td>0.9716±0.0017</td><td>0.9214±0.0040</td><td>0.9906±0.0003</td><td>0.9734±0.0012</td><td>0.9628</td></tr><tr><td>3DFCH-EMOA</td><td>0.9276±0.0025</td><td>0.9934±0.0004</td><td>0.9729±0.0014</td><td>0.9227±0.0013</td><td>0.9911±0.0005</td><td>0.9741±0.0007</td><td>0.9637</td></tr></table>

Table 13  
Mean and standard deviation of Kappa of ensemble methods on change detection datasets.

<table><tr><td>Datasets Methods</td><td>Ottawa</td><td>Bern</td><td>Mexico</td><td>Farmland</td><td>Coastline</td><td>Inland water</td><td>Average</td></tr><tr><td>MP</td><td>0.6782±0.0224</td><td>0.5702±0.0442</td><td>0.7970±0.0315</td><td>0.4747±0.0530</td><td>0.3616±0.1256</td><td>0.5565±0.0216</td><td>0.5730</td></tr><tr><td>KP</td><td>0.6180±0.1322</td><td>0.5811±0.0584</td><td>0.8042±0.0383</td><td>0.4867±0.0651</td><td>0.3327±0.2237</td><td>0.5291±0.0736</td><td>0.5586</td></tr><tr><td>SpaRSA</td><td>0.6683±0.0700</td><td>0.6425±0.0694</td><td>0.7776±0.0448</td><td>0.5013±0.0498</td><td>0.3540±0.1189</td><td>0.5578±0.0632</td><td>0.5836</td></tr><tr><td>OMP</td><td>0.7170±0.0077</td><td>0.5858±0.0475</td><td>0.8072±0.0278</td><td>0.5239±0.0176</td><td>0.3464±0.0932</td><td>0.5620±0.0326</td><td>0.5904</td></tr><tr><td>Two_Arch2</td><td>0.7177±0.0078</td><td>0.6798±0.0386</td><td>0.8376±0.0105</td><td>0.5204±0.0088</td><td>0.3463±0.1073</td><td>0.5970±0.0111</td><td>0.6165</td></tr><tr><td>NSGA-III</td><td>0.7179±0.0080</td><td>0.6885±0.0335</td><td>0.8360±0.0098</td><td>0.5273±0.0124</td><td>0.3679±0.1192</td><td>0.6017±0.0118</td><td>0.6232</td></tr><tr><td>MOEA/DD</td><td>0.7209±0.0054</td><td>0.6913±0.0330</td><td>0.8364±0.0097</td><td>0.5310±0.0131</td><td>0.3887±0.0859</td><td>0.6023±0.0101</td><td>0.6284</td></tr><tr><td>RVEA</td><td>0.7186±0.0035</td><td>0.6725±0.0298</td><td>0.8354±0.0091</td><td>0.5234±0.0107</td><td>0.3511±0.1072</td><td>0.5985±0.0083</td><td>0.6166</td></tr><tr><td>AR-MOEA</td><td>0.7187±0.0077</td><td>0.6814±0.0335</td><td>0.8309±0.0118</td><td>0.5222±0.0159</td><td>0.3322±0.0518</td><td>0.5981±0.0132</td><td>0.6139</td></tr><tr><td>3DFCH-EMOA</td><td>0.7211±0.0064</td><td>0.7020±0.0271</td><td>0.8407±0.0095</td><td>0.5279±0.0072</td><td>0.3873±0.0947</td><td>0.6064±0.0092</td><td>0.6309</td></tr></table>

Table 14  
Mean and standard deviation of Precision of ensemble methods on change detection datasets.

<table><tr><td>Datasets Methods</td><td>Ottawa</td><td>Bern</td><td>Mexico</td><td>Farmland</td><td>Coastline</td><td>Inland water</td><td>Average</td></tr><tr><td>MP</td><td>0.7846±0.0436</td><td>0.5336±0.0727</td><td>0.8790±0.0128</td><td>0.3915±0.0467</td><td>0.3810±0.1346</td><td>0.6030±0.0502</td><td>0.5954</td></tr><tr><td>KP</td><td>0.6779±0.1477</td><td>0.6124±0.0675</td><td>0.8639±0.0271</td><td>0.4119±0.0658</td><td>0.3597±0.1247</td><td>0.5655±0.1097</td><td>0.5819</td></tr><tr><td>SpaRSA</td><td>0.7412±0.0904</td><td>0.6834±0.1484</td><td>0.8720±0.0435</td><td>0.4074±0.0396</td><td>0.4298±0.2348</td><td>0.5873±0.1053</td><td>0.6202</td></tr><tr><td>OMP</td><td>0.8005±0.0143</td><td>0.5548±0.0675</td><td>0.8896±0.0120</td><td>0.4265±0.0191</td><td>0.3776±0.1211</td><td>0.6021±0.0491</td><td>0.6085</td></tr><tr><td>Two_Arch2</td><td>0.7816±0.0169</td><td>0.8152±0.0310</td><td>0.8944±0.0038</td><td>0.4161±0.0074</td><td>0.7171±0.0551</td><td>0.6674±0.0188</td><td>0.7153</td></tr><tr><td>NSGA-III</td><td>0.7855±0.0208</td><td>0.7865±0.0353</td><td>0.8958±0.0038</td><td>0.4237±0.0125</td><td>0.6647±0.0532</td><td>0.6757±0.0234</td><td>0.7053</td></tr><tr><td>MOEA/DD</td><td>0.7886±0.0129</td><td>0.8052±0.0309</td><td>0.8919±0.0031</td><td>0.4251±0.0113</td><td>0.7310±0.0339</td><td>0.6875±0.0288</td><td>0.7216</td></tr><tr><td>RVEA</td><td>0.7768±0.0095</td><td>0.8151±0.0318</td><td>0.8922±0.0024</td><td>0.4171±0.0097</td><td>0.7455±0.0644</td><td>0.6782±0.0213</td><td>0.7208</td></tr><tr><td>AR-MOEA</td><td>0.7852±0.0182</td><td>0.7914±0.0307</td><td>0.8951±0.0027</td><td>0.4191±0.0146</td><td>0.7009±0.0700</td><td>0.6742±0.0262</td><td>0.7110</td></tr><tr><td>3DFCH-EMOA</td><td>0.7898±0.0186</td><td>0.8177±0.0235</td><td>0.8930±0.0025</td><td>0.4237±0.0053</td><td>0.7223±0.0275</td><td>0.6895±0.0160</td><td>0.7227</td></tr></table>

Table 15  
Mean and standard deviation of Recall of ensemble methods on change detection datasets.

<table><tr><td>Datasets Methods</td><td>Ottawa</td><td>Bern</td><td>Mexico</td><td>Farmland</td><td>Coastline</td><td>Inland water</td><td>Average</td></tr><tr><td>MP</td><td>0.6763±0.0268</td><td>0.6358±0.0577</td><td>0.7617±0.0512</td><td>0.7619±0.0442</td><td>0.3883±0.1587</td><td>0.5479±0.0284</td><td>0.6287</td></tr><tr><td>KP</td><td>0.7069±0.0341</td><td>0.5750±0.1011</td><td>0.7861±0.0539</td><td>0.7354±0.0508</td><td>0.5228±0.2162</td><td>0.5440±0.0831</td><td>0.6450</td></tr><tr><td>SpaRSA</td><td>0.7038±0.0309</td><td>0.6352±0.0564</td><td>0.7364±0.0533</td><td>0.8050±0.0543</td><td>0.4424±0.2395</td><td>0.5709±0.0315</td><td>0.6489</td></tr><tr><td>OMP</td><td>0.7227±0.0090</td><td>0.6404±0.0620</td><td>0.7696±0.0450</td><td>0.8206±0.0186</td><td>0.3553±0.1034</td><td>0.5585±0.0418</td><td>0.6445</td></tr><tr><td>Two_Arch2</td><td>0.7422±0.0115</td><td>0.5927±0.0667</td><td>0.8150±0.0203</td><td>0.8493±0.0102</td><td>0.2415±0.0954</td><td>0.5634±0.0117</td><td>0.6340</td></tr><tr><td>NSGA-III</td><td>0.7389±0.0131</td><td>0.6219±0.0605</td><td>0.8110±0.0189</td><td>0.8466±0.0088</td><td>0.2700±0.1220</td><td>0.5654±0.0174</td><td>0.6423</td></tr><tr><td>MOEA/DD</td><td>0.7405±0.0107</td><td>0.6149±0.0613</td><td>0.8151±0.0171</td><td>0.8563±0.0123</td><td>0.2740±0.0789</td><td>0.5584±0.0183</td><td>0.6432</td></tr><tr><td>RVEA</td><td>0.7484±0.0092</td><td>0.5804±0.0522</td><td>0.8131±0.0155</td><td>0.8588±0.0151</td><td>0.2438±0.1039</td><td>0.5582±0.0097</td><td>0.6338</td></tr><tr><td>AR-MOEA</td><td>0.7405±0.0154</td><td>0.6074±0.0565</td><td>0.8032±0.0200</td><td>0.8442±0.0088</td><td>0.2245±0.0492</td><td>0.5606±0.0144</td><td>0.6300</td></tr><tr><td>3DFCH-EMOA</td><td>0.7397±0.0115</td><td>0.6216±0.0431</td><td>0.8214±0.0173</td><td>0.8486±0.0117</td><td>0.2763±0.0923</td><td>0.5631±0.0146</td><td>0.6451</td></tr></table>

the datasets; 2) 3DFCH-EMOA obtained the best result and MOEA/DD obtained the second best result on the average Precision; 3) 3DFCH-EMOA obtained the best result and KP obtained the second best result on the average Recall; and 4) the two metrics, i.e., Precision and Recall are con<sup>fl</sup>icting with each other. Generally, a method which has a good performance on one objective will not necessarily have a good performance on another objective. 3DFCH-EMOA can <sup>fi</sup>nd a good trade-o<sup>f</sup> between these two metrics.

The statistical results of Kappa are shown in Table 13. By comparing the results on the table, we can conclude that 1) OMP outperforms other CS and pruning ensemble methods; 2) 3DFCH-EMOA and MOEA/DD perform better than other MOSEL methods on most of the datasets; and 3) 3DFCH-EMOA can obtain the best result on the average Kappa of the six remote sensing datasets.

The metrics of Precision and Recall are compared in Tables 14 and 15, respectively. By comparing the results we can <sup>fi</sup>nd out that 1) the new proposed MOSEL methods outperform other methods on most of

The statistical results of F-measure is listed in Table 16. F-measure is a comprehensive consideration of Precision and Recall. By comparing the results we can make conclusions: 1) The proposed MOSEL method performs better than other methods on most of the remote sensing datasets; 2) 3DFCH-EMOA outperforms others on most of the datasets; 3) MOEA/DD performs the second best on the average F-measure.

Table 16  
Mean and standard deviation of F-measure of ensemble methods on change detection datasets.

<table><tr><td>Datasets Methods</td><td>Ottawa</td><td>Bern</td><td>Mexico</td><td>Farmland</td><td>Coastline</td><td>Inland water</td><td>Average</td></tr><tr><td>MP</td><td>0.7254±0.0184</td><td>0.5762±0.0434</td><td>0.8153±0.0293</td><td>0.5160±0.0475</td><td>0.3684±0.1241</td><td>0.5724±0.0204</td><td>0.5956</td></tr><tr><td>KP</td><td>0.6829±0.0974</td><td>0.5862±0.0580</td><td>0.8223±0.0352</td><td>0.5259±0.0587</td><td>0.4015±0.1448</td><td>0.5465±0.0706</td><td>0.5942</td></tr><tr><td>SpaRSA</td><td>0.7200±0.0557</td><td>0.6470±0.0679</td><td>0.7975±0.0411</td><td>0.5405±0.0453</td><td>0.3611±0.1174</td><td>0.5744±0.0594</td><td>0.6068</td></tr><tr><td>OMP</td><td>0.7595±0.0063</td><td>0.5914±0.0467</td><td>0.8245±0.0259</td><td>0.5610±0.0157</td><td>0.3533±0.0918</td><td>0.5778±0.0313</td><td>0.6112</td></tr><tr><td>Two_Arch2</td><td>0.7612±0.0063</td><td>0.6832±0.0385</td><td>0.8527±0.0098</td><td>0.5585±0.0079</td><td>0.3496±0.1080</td><td>0.6108±0.0107</td><td>0.6360</td></tr><tr><td>NSGA-III</td><td>0.7612±0.0062</td><td>0.6920±0.0333</td><td>0.8512±0.0091</td><td>0.5646±0.0111</td><td>0.3715±0.1194</td><td>0.6152±0.0114</td><td>0.6426</td></tr><tr><td>MOEA/DD</td><td>0.7636±0.0045</td><td>0.6947±0.0328</td><td>0.8517±0.0089</td><td>0.5681±0.0118</td><td>0.3922±0.0863</td><td>0.6156±0.0097</td><td>0.6477</td></tr><tr><td>RVEA</td><td>0.7623±0.0030</td><td>0.6759±0.0297</td><td>0.8507±0.0084</td><td>0.5614±0.0097</td><td>0.3543±0.1078</td><td>0.6121±0.0078</td><td>0.6361</td></tr><tr><td>AR-MOEA</td><td>0.7619±0.0064</td><td>0.6849±0.0334</td><td>0.8465±0.0109</td><td>0.5600±0.0143</td><td>0.3357±0.0522</td><td>0.6118±0.0127</td><td>0.6335</td></tr><tr><td>3DFCH-EMOA</td><td>0.7637±0.0049</td><td>0.7053±0.0270</td><td>0.8556±0.0088</td><td>0.5652±0.0066</td><td>0.3908±0.0951</td><td>0.6197±0.0089</td><td>0.6500</td></tr></table>

Table 17  
Mean and standard deviation of non-zero ensemble weight for each method on change detection datasets.

<table><tr><td>Datasets Methods</td><td>Ottawa</td><td>Bern</td><td>Mexico</td><td>Farmland</td><td>Coastline</td><td>Inland water</td><td>Average</td></tr><tr><td>MP</td><td>26.00 ± 0.00</td><td>26.00 ± 0.00</td><td>26.00 ± 0.00</td><td>26.00 ± 0.00</td><td>26.00 ± 0.00</td><td>26.00 ± 0.00</td><td>26.00</td></tr><tr><td>KP</td><td>1.00 ± 0.00</td><td>1.00 ± 0.00</td><td>1.00 ± 0.00</td><td>1.00 ± 0.00</td><td>1.00 ± 0.00</td><td>1.00 ± 0.00</td><td>1.00</td></tr><tr><td>SpaRSA</td><td>19.10 ± 16.30</td><td>23.90 ± 17.11</td><td>14.60 ± 15.89</td><td>28.50 ± 15.79</td><td>12.10 ± 15.20</td><td>17.80 ± 16.84</td><td>19.33</td></tr><tr><td>OMP</td><td>21.80 ± 2.62</td><td>1.00 ± 0.00</td><td>2.70 ± 0.48</td><td>15.20 ± 9.37</td><td>1.00 ± 0.00</td><td>1.00 ± 0.00</td><td>7.12</td></tr><tr><td>Two_Arch2</td><td>49.80 ± 6.16</td><td>48.00 ± 5.37</td><td>45.90 ± 4.46</td><td>50.80 ± 4.96</td><td>49.00 ± 7.12</td><td>49.10 ± 4.36</td><td>48.77</td></tr><tr><td>NSGA-III</td><td>37.60 ± 3.98</td><td>33.40 ± 4.55</td><td>35.50 ± 3.14</td><td>38.00 ± 5.64</td><td>27.50 ± 4.84</td><td>34.90 ± 5.45</td><td>34.48</td></tr><tr><td>MOEA/DD</td><td>46.60 ± 11.94</td><td>53.20 ± 13.60</td><td>50.40 ± 17.69</td><td>42.30 ± 5.03</td><td>53.20 ± 11.59</td><td>42.30 ± 11.66</td><td>48.00</td></tr><tr><td>RVEA</td><td>49.90 ± 8.09</td><td>60.20 ± 5.92</td><td>55.00 ± 7.59</td><td>45.70 ± 4.81</td><td>67.70 ± 7.26</td><td>56.40 ± 6.24</td><td>55.82</td></tr><tr><td>AR-MOEA</td><td>43.90 ± 4.77</td><td>39.60 ± 5.25</td><td>41.90 ± 5.78</td><td>45.70 ± 4.47</td><td>37.60 ± 3.57</td><td>41.50 ± 5.52</td><td>41.70</td></tr><tr><td>3DFCH-EMOA</td><td>71.40 ± 17.49</td><td>62.30 ± 10.63</td><td>85.60 ± 21.82</td><td>70.20 ± 16.25</td><td>63.00 ± 24.81</td><td>74.40 ± 23.98</td><td>71.15</td></tr></table>

Table 18  
Wilcoxon sum-rank test on change detection datasets: each x-y-z in this table means that 3DFCH-EMOA wins x times, losses y times, draws z times.

<table><tr><td></td><td>MP</td><td>KP</td><td>SpaRSA</td><td>OMP</td><td>NSGA-III</td><td>Two_Arch2</td><td>MOEA/DD</td><td>RVEA</td><td>AR-MOEA</td></tr><tr><td>Accuracy</td><td>5-0-1</td><td>5-0-1</td><td>5-0-1</td><td>4-0-2</td><td>2-0-4</td><td>0-0-6</td><td>0-0-6</td><td>2-0-4</td><td>1-0-5</td></tr><tr><td>Kappa</td><td>5-0-1</td><td>5-0-1</td><td>4-0-2</td><td>3-0-3</td><td>0-0-6</td><td>0-0-6</td><td>0-0-6</td><td>1-0-5</td><td>0-0-6</td></tr><tr><td>Precision</td><td>5-0-1</td><td>5-0-1</td><td>3-0-3</td><td>3-0-3</td><td>2-0-4</td><td>2-0-4</td><td>0-0-6</td><td>0-0-6</td><td>1-0-5</td></tr><tr><td>Recall</td><td>3-0-3</td><td>2-1-3</td><td>3-0-3</td><td>3-0-3</td><td>0-0-6</td><td>0-0-6</td><td>0-0-6</td><td>0-0-6</td><td>1-0-5</td></tr><tr><td>F-measure</td><td>5-0-1</td><td>5-0-1</td><td>4-0-2</td><td>3-0-3</td><td>0-0-6</td><td>0-0-6</td><td>0-0-6</td><td>1-0-5</td><td>0-0-6</td></tr><tr><td>Non-zeros</td><td>0-6-0</td><td>0-6-0</td><td>0-6-0</td><td>0-6-0</td><td>0-5-1</td><td>0-6-0</td><td>0-4-2</td><td>0-2-4</td><td>0-6-0</td></tr></table>

Table 17 shows the mean value and standard deviation of non-zero classi<sup>fi</sup>ers of the ensemble weight. By comparing the results we can conclude that KP and OMP have good performance on sparsity. How ever, they perform poorly on Accuracy and Kappa metrics.

As 3DFCH-EMOA has good performance on most of the compared metrics, we make a more comprehensive comparison between 3DFCH-EMOA and other ensemble methods. The Wilcoxon sum-rank test results are listed in Table 18. By comparing the results we can <sup>fi</sup>nd out that 3DFCH-EMOA outperforms CS and pruning ensemble methods signi<sup>fi</sup>cantly on accuracy and Kappa metrics for most of the datasets.

EMOAs is not even. To <sup>fi</sup>nd evenly distributed solutions MOSEL must be studied further. Besides, the generation of candidate classi<sup>fi</sup>ers was not taken into consideration and the importance of each dimension of data not studied in depth. In the future, the generation of candidate classi-<sup>fi</sup>ers can be further studied, which can provide some useful rules related to the corresponding data mining tasks.

## Acknowledgments

## 4. Conclusions

In this paper, we proposed the multiobjective sparse ensemble learning model and analyzed its properties in the ADET space. Firstly, MOSEL is modeled as ADCH maximization problem, and the relationship between the sparsity and the performance of ensemble classi<sup>fi</sup>ers on the ADET space is explained. Secondly, sparse real encoding is designed as a bridge between MOSEL and EMOAs, and six EMOAs were used to <sup>fi</sup>nd a sparse ensemble classi<sup>fi</sup>er with good performance. Thirdly, an adaptive MOSEL classi<sup>fi</sup>er selection algorithm was proposed to select the most suitable ensemble classi<sup>fi</sup>er for a given dataset. Experimental results based on well-known MNIST and remote sensing change detection datasets show that the proposed MOSEL performs signi<sup>fi</sup>cantly better than conventional ensemble learning methods. However, the distribution of MOSEL solutions obtained by several

The authors would like to thank the editor and anonymous reviewers for their very competent comments and suggestions. This work was supported by the Fundamental Research Funds for the Central Universities (No. 2018XKQYMS27).

## References

[1] S. Piri, D. Delen, T. Liu, H.M. Zolbanin, A data analytics approach to building a clinical decision support system for diabetic retinopathy: developing and deploying a model ensemble, Decision Support Systems 101 (2017) 12–27.

[2] R. Gupta, K. Audhkhasi, S. Narayanan, Training ensemble of diverse classi<sup>fi</sup>ers on feature subsets, Acoustics, Speech and Signal Processing (ICASSP), 2014 IEEE International Conference on, 2014, pp. 2927–2931.

[3] A. Riccardi, F. Fernandez-Navarro, S. Carloni, Cost-sensitive AdaBoost algorithm for ordinal regression based on extreme learning machine. JEEE Trans. Cybernetics 44 (10) (2014) 1898 1909.

[4] Y. Liu, C. Jiang, H. Zhao, Using contextual features and multi-view ensemble learning in product defect identification from online discussion forums. Decision Support Systems 105 (2018) 1–12.

[5] P. du Jardin, Failure pattern-based ensembles applied to bankruptcy forecasting, Decision Support Systems 107 (2018) 64 77.

[6] Z. Zhao, L. Jiao, F. Liu, J. Zhao, Semisupervised discriminant feature learning for

SAR image category via sparse ensemble, IEEE Transactions on Geoscience and Remote Sensing 54 (6) (2016) 3532 3547.

[7] L. Breiman, Bagging predictors, Machine Learning 24 (1996) 123–140.

[8] J.H. Friedman, Greedy function approximation: a gradient boosting machine. Annals of Statistics 29 (5) (2001) 1189–1232

[9] T.K. Ho, The random subspace method for constructing decision forests, IEEE Transactions on Pattern Analysis and Machine Intelligence 20 (8) (1998) 832–844.

[10] J. Rodriguez, L. Kuncheva, C. Alonso, Rotation forest: a new classi<sup>fi</sup>er ensemble method, IEEE Transactions on Pattern Analysis and Machine Intelligence 28 (10) (2006) 1619–1630.

[11] A. Mukhopadhyay, U. Maulik, S. Bandyopadhyay, C. Coello, Survey of multiobjective evolutionary algorithms for data mining: part II, IEEE Transactions on Evolutionary Computation 18 (1) (2014) 20–35.

[12] M. Asafuddoula, B. Verma, M. Zhang, A divide-and-conquer based ensemble classi<sup>fi</sup>er learning by means of many-objective optimization, IEEE Transactions on Evolutionary Computation (2017), http://dx.doi.org/10.1109/TEVC.2017. 2782826 1-1.

[13] C. Zhang, P. Lim, A.K. Qin, K.C. Tan, Multiobjective deep belief networks en semble for remaining useful life estimation in prognostics, IEEE Transactions on Neural Networks and Learning Systems 28 (10) (2017) 2306–2318.

[14] W.A. Albukhanajer, Y. Jin, J.A. Bri<sup>f</sup>a, Classi<sup>fi</sup>er ensembles for image identi<sup>fi</sup>ca tion using multi-objective Pareto features, Neurocomputing 238 (2017) 316–327.

[15] Z.-h. Zhou, J. Wu, W. Tang, Ensembling neural networks: many could be better than all, Arti<sup>fi</sup>cial Intelligence 137 (2002) 239–263.

[16] H. Chen, P. Tiho, X. Yao, Predictive ensemble pruning by expectation propagation, IEEE Transactions on Knowledge and Data Engineering 21 (7) (2009) 999–1013.

[17] G. Martínez-Muñoz, D. Hernández-lobato, A. Suárez, An analysis of ensemble pruning techniques based on ordered aggregation, IEEE Transactions on Pattern Analysis and Machine Intelligence 31 (2009) 245–259.

[18] S. Mao, L. Jiao, L. Xiong, S. Gou, Greedy optimization classi<sup>fi</sup>ers ensemble based on diversity, Pattern Recognition 44 (6) (2011) 1245 1261.

[19] L. Zhang, W.-D. Zhou, Sparse ensembles using weighted combination methods based on linear programming, Pattern Recognition 44 (1) (2011) 97–106.

[20] L. Li, X. Yao, R. Stolkin, M. Gong, S. He, An evolutionary multiobjective approach to sparse reconstruction, IEEE Transactions on Evolutionary Computation 18 (6) (2014) 827–845.

[21] Y.-L. Chen, C.-L. Chang, C.-S. Yeh, Emotion classi<sup>fi</sup>cation of YouTube videos, Decision Support Systems 101 (Supplement C) (2017) 40–50.

[22] D. Donoho, Compressed sensing, IEEE Transactions on Information Theory 52 (4) (2006) 1289–1306.

[23] L. Li, R. Stolkin, L. Jiao, F. Liu, S. Wang, A compressed sensing approach for e<sup>fi</sup>cient ensemble learning, Pattern Recognition 47 (10) (2014) 3451–3465.

[24] S. Wright, R. Nowak, M. Figueiredo, Sparse reconstruction by separable approximation, IEEE Transactions on Signal Processing 57 (7) (2009) 2479–2493.

[25] G. Davis, S. Mallat, M. Avellaneda, Adaptive greedy approximations, Constructive Approximation 13 (1997) 57–98.

[26] K.-C. Toh, S. Yun, An accelerated proximal gradient algorithm for nuclear norm regularized linear least squares problems, Paci<sup>fi</sup>c Journal of Optimization 6 (3) (2010) 615–640.

[27] M.D. Plumbley, Recovery of sparse representations by polytope faces pursuit, International Conference on Independent Component Analysis and Signal Separation. 2006, pp. 206–213.

[28] A.F. Martin, G.R. Doddington, T. Kamm, M. Ordowski, M.A. Przybocki, The DET curve in assessment of decision task performance. European Conference on Speech Communication and Technology, Eurospeech 1997, Rhodes, Greece, September, 1997, pp. 1895–1898.

[29] A. Mattiussi, M. Rosano, P. Simeoni, A decision support system for sustainable energy supply combining multi-objective and multi-attribute analysis: an Australian case study, Decision Support Systems 57 (Supplement C) (2014) 150–159.

[30] H. Wang, L. Jiao, X. Yao, Two\_Arch2: An improved two-archive algorithm for many-objective optimization, IEEE Transactions on Evolutionary Computation 19 (4) (2015) 524 541.

[31] K. Deb, H. Jain, An evolutionary many-objective optimization algorithm using reference-point-based nondominated sorting approach, part I: solving problems with box constraints, IEEE Transactions on Evolutionary Computation 18 (4) (2014) 577 601.

[32] K. Li, K. Deb, Q. Zhang, S. Kwong, An evolutionary many-objective optimization algorithm based on dominance and decomposition, JEEE Transactions or Evolutionary Computation 19 (5) (2015) 694 716.

[33] R. Cheng, Y. Jin, M. Olhofer, B. Sendho<sup>f</sup>, A reference vector guided evolutionary algorithm for many-objective optimization, IEEE Transactions on Evolutionary Computation 20 (5) (2016) 773–791.

[34] Y. Tian, R. Cheng, X. Zhang, F. Cheng, Y. Jin, An indicator based multi-objective evolutionary algorithm with reference point adaptation for better versatility, IEEE Transactions on Evolutionary Computation (2017), http://dx.doi.org/10.1109/ TEVC,2017.2749619.1-1

[35] J. Zhao. V. Basto Fernandes. L. Jiao. L. Yeyseveva. A. Maulana. R. Li. T. Bäck, K Tang, M.T.M. Emmerich, Multiobjective optimization of classi<sup>fi</sup>ers by means of 3D convex-hull-based evolutionary algorithms, Information Sciences 367–368 (2016) 80–104.

[36] J. Zhao, L. Jiao, F. Liu, V.B. Fernandes, I. Yevseyeva, S. Xia, M.T. Emmerich, 3D fast convex-hull-based evolutionary multiobjective optimization algorithm, Applied Soft Computing 67 (2018) 322–336.

[37] Y. Lecun, L. Bottou, Y. Bengio, P. Ha<sup>f</sup>ner, Gradient-based learning applied to document recognition, IEEE, 1998, pp. 2278–2324.

[38] P. Wang, M. Emmerich, R. Li, K. Tang, T. Bäck, X. Yao, Convex hull-based multi

objective genetic programming for maximizing receiver operator characteristic performance, IEEE Transactions on Evolutionary Computation 19 (2) (2015) 188 200.

[39] I. Mendialdua, A. Arruti, E. Jauregi, E. Lazkano, B. Sierra, Classi<sup>fi</sup>er subset selection to construct multi-classifiers by means of estimation of distribution al gorithms, Neurocomputing 157 (2015) 46–60.

[40] X. Wu, V. Kumar, J.R. Quinlan, J. Ghosh, Q. Yang, H. Motoda, G.J. Mclachlan, A. Ng, B. Liu, P.S. Yu, Top 10 algorithms in data mining, Knowledge and Information Systems 14 (1) (2008) 1–37.

[41] G.H. Rosen<sup>fi</sup>eld, A coe<sup>fi</sup>cient of agreement as a measure of thematic classi<sup>fi</sup>cation accuracy, Photogrammetric Engineering & Remote Sensing 52 (2) (1986) 223–227.

[42] M. Gong, J. Zhao, J. Liu, Q. Miao, L. Jiao, Change detection in synthetic aperture radar images based on deep neural networks, IEEE Transactions on Neural Networks and Learning Systems 27 (1) (2016) 125–138.

[43] Y. Zheng, L. Jiao, H. Liu, X. Zhang, B. Hou, S. Wang, Unsupervised saliency guided SAR image change detection, Pattern Recognition 61 (2017) 309–326.

[44] R.J. Radke, S. Andra, O. Al-Kofahi, B. Roysam, Image change detection algorithms: a systematic survey, IEEE Transactions on Image Processing 14 (3) (2005) 294–307.

[45] J. Liu, M. Gong, K. Qin, P. Zhang, A deep convolutional coupling network for change detection based on heterogeneous optical and radar images, IEEE Transactions on Neural Networks and Learning Systems 29 (3) (2018) 545 559

[46] G. Akbarizadeh, A New Statistical-based kurtosis wavelet energy feature for texture recognition of SAR Images, IEEE Transactions on Geoscience & Remote Sensing 50 (11) (2012) 4358 4368.

[47] B. Hou, X. Zhang, N. Li, MPM SAR image segmentation using feature extraction and context model, IEEE Geoscience & Remote Sensing Letters 9 (6) (2012) 1041 1045.

Jiaqi Zhao received the B.Eng. degrees in intelligence science and technology in 2010, the Ph.D. degree in circuits and systems in 2017 from Xidian University, Xian, China. Between 2013 and 2014. he was an exchange Ph.D. student with the Leiden Institute for Advanced Computer Science (LIACS), University of Leiden, The Netherlands. He is currently with the School of Computer Science and Technology, China University of Mining and Technology, Xuzhou, China. His current research interests include multiobjective optimization, machine learning and image processing.

Licheng Jiao received the B.S. degree from Shanghai Jiao Tong University, Shanghai, China, in 1982 and the M.S. and Ph.D. degrees from Xian Jiaotong University, Xian, China, in 1984 and 1990, respectively. Since 1992, he has been a professor with th School of Electronic Engineering, Xidian University, Xian, where he is currently the Director of the Key Laboratory of Intelligent Perception and Image Understanding of the Ministry of Education of China, International Research Center of Intelligent Perception and Computation. His current research interests include intelligent information processing, image processing, machine learning, and pattern recognition. Prof. Jiao is a member of the IEEE Xian Section Execution Committee; the President of the Computational Intelligence Chapter, the IEEE Xian Section, and the IET Xian Network: the Chairman of the Awards and Recognition Committee; the Vice Board Chairperson of the Chinese Association of Arti<sup>fi</sup>cial Intelligence; a Councilor of the Chinese Institute of Electronics; a Committee Member of the Chinese Committee of Neural Networks: and an Expert of the Academic Degrees Committee of the State Council

Shixiong Xia is currently a professor with the China University of Mining and Technology, Xuzhou, China. His research interests include pattern recognition and in telligent information processing.

Vitor Basto Fernandes graduated from the University of Minho - Portugal in information systems in 1995, post-graduated in distributed systems and mobile computing in 1997 and 2005 respectively. In 2006 he got his PhD on multimedia transport protocols from the University of Minho - Portugal, where he has been lecturer on distributed systems and information systems planning and development. From 2005 he has been lecturing at the University of Tras-os-Montes e Alto Douro - Portugal, and invited assistant professor in the same university in 2007 and 2008, being responsible for computer networks, programming and information system integration courses. In 2008 he joined the Polytechnic Institute of Leiria - Portugal as assistant professor in the Informatics Engineering Department, where he has been teaching software engineering, information systems integration and cognitive networks. He is currently coordinator professor at Polytechni Institute of Leiria, has been involved in national and international research projects, published a number of conference and journal papers in his research interest area, computer networks. semantic web and optimization

Iryna Yevseyeva is a lecturer in Computer Science at the Faculty of Technology in the De Montfort University in Leicester. Before joining De Montfort University in 2016, she was a Leading Research Associate at the Choice Architecture for Information Security (ChAISe) project in the Newcastle University working on improving security decision making in organizations in 2013–2016. Previously she was a post-doctoral researcher at LIACS in the Leiden University in The Netherlands working on optimizing drug discovery in 2012–2013. She held several post-doctoral research posts in Portugal: at the Polytechnic Institute of Leiria in 2011–2012 on spam <sup>fi</sup>ltering; at INESC Porto with Ciencia 2008 grant in 2009–2011 on scheduling optimization; at the University of Algarve with grants from Academy of Finland and European Commission (Erasmus Mundus) on multiobiective evolutionary algorithms development in 2008–2009. Iryna received PhD degree in computer science and optimization from the University of Jyvaskyla in Finland in 2007 for the research on multicriteria classi<sup>fi</sup>cation with applications in healthcare. Before joining PhD program in 2004, she worked as a software developer at the Niilo Maki Institute of Neuropsychology, Finland, in 2001–2003. She has Master of Science degree in mobile computing from the University of Jyvaskyla, Finland (2001) and Master degree with honours in information technology from the Kharkov National University of Radio-Electronics, Ukraine (2000)

Yong Zhou is an associate professor in China University of Mining and Technology. His current interests include intelligent information processing and information fuse.

Michael T.M. Emmerich born in 1973 in Coesfeld, Germany, received his Diploma in Applied Informatics with Application Field Chemical Engineering in 1999 from the University Dortmund. After three years as a research consultant for nonlinear optimiza tion in the chemical industry (CASA/ICD e.V., Dortmund), he worked as a research assistant in the Chair of Systems Analysis, Faculty for Informatics, University of Dortmund. He received his Dr. rer,nat.degree in 2005 from the University Dortmund on the topic Single- and Multiobjective Evolutionary Design Optimization Assisted by Gaussian Random Fields (Promotors: Prof.H.P. Schwefel (1st), Prof. P. Buchholz (2nd)). Since 2005 he has been working as an Assistant Professor at the Leiden Institute for Advanced Computer Science, The Netherlands, where he leads the Multidisciplinary Optimization and Decision Analysis (MODA) research group. Since 2016 he is appointed as associate professor. Besides at Leiden University, he worked as a researcher for the Laboratory for Technical Turbomachinery, NTU Athens (gr), ACCESS e.V. (Material sci ence), RWTH Aachen, University of the Algarve, Faro, Instituto Superior T ecnico Lisbon, and FOM Institute, AMOLF Amsterdam. His main research interests are algorithm design for multicriteria optimization, spatial modeling, and complex systems analysis, with ap plications in engineering, chemistry, and the biomedical sciences.
