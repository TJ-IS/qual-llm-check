---
otero_id: 16386
otero_key: "RKDG4YPS"
title: "Feature assessment and ranking for classification with nonlinear sparse representation and approximate dependence analysis"
authors: "Yishi Zhang; Qi Zhang; Zhijun Chen; Jennifer Shang; Haiying Wei"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.05.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Feature assessment and ranking for classification with nonlinear sparse representation and approximate dependence analysis

![](/api/attachments/RKDG4YPS/fulltext/images/ff2ff9c5d1e390cde7cd3fc56152799f6c2fb72097af9571a57dd7cdd0382d4d.jpg)

Yishi Zhang<sup>a,d</sup>, Qi Zhang<sup>b,\*</sup>, Zhijun Chen<sup>c,\*</sup>, Jennifer Shang<sup>d</sup>, Haiying Wei<sup>a</sup>

<sup>a</sup> School of Management, Jinan University, Guangzhou 510632, China

<sup>b</sup> School of Economics and Management, China University of Geosciences (Wuhan), Wuhan 430074, China

<sup>c</sup> Intelligent Transport Systems Research Center, Wuhan University of Technology, Wuhan 430063, China

<sup>d</sup> Joseph M. Katz Graduate School of Business, University of Pittsburgh, Pittsburgh, PA 15260, USA

## A R T I C L E I N F O

Keywords: Feature selection Dimensionality reduction Classification Sparse representation Dependence analysis

## A B S T R A C T

Feature selection has received significant attention in knowledge management and decision support systems in the past decades. In this study, kernel-based sparse representation and feature dependence analysis are integrated into a feature assessment and ranking framework. The proposed method utilizes the advantages of the kernel-based sparse representation technique and of the information theoretic metric to iteratively obtain the salient feature cluster. Then, a novel approximate dependence analysis is applied to further maintain complementarity while eliminating redundancy among the features selected by nonlinear orthogonal matching pursuit (NOMP). This can efectively prevent the significant bias caused by the pairwise correlation analysis for a large-scale feature set. To illustrate the effectiveness of the proposed method. classification experiments are conducted with three representative classifiers, on nine well-known datasets. The experimental results show the superiority of the proposed method compared with the representative information theoretic and model-based methods in classification for data-driven decision support systems.

## 1. Introduction

Selecting salient features that preserve or promote the performance of data mining and decision-making is a problem of growing significance because of the increasing size, high-dimensionality, and complexity of real-world datasets in numerous domains, e.g., financial decision-making and credit scoring [e.g., Refs. 1, 2], image processing [e.g., Refs. 3-5], and cancer diagnosis [e.g., Refs. 6, 7]. Taking the credit scoring in peer-to-peer lending as an example, automatically detecting which customers are possible to default on loan repayment using machine learning methods has been a hot issue for years, as it can help financial experts to make profitable decisions while fulfilling regulatory requirements. However, tremendous financial features known as the curse-of-dimensionality will not only increase the computational cost but also impair the performance of the machine learning methods, owing to the inclusion of redundant and noisy information. Feature selection is thus applied to reduce the dimensionality of feature space and to boost the performance of the machine learning methods. Efective feature selection methods have been widely recognized for their capabilities in facilitating data acquisition, increasing learning eficiency, removing noise, and reducing overfitting.

Feature selection methods can be broadly classified into three distinct types: filter methods [e.g., Ref. 8], wrapper methods [e.g., Ref. 9], and embedded methods [e.g., Ref. 2]. Filter methods apply classifierirrelevant metrics such as information theoretic metrics [10] and $\ell _ { p ^ { - } }$ norm $( 0 < p \leq 2 ) [ 1 1 ]$ to evaluate and select features; therefore, they generally incur relatively low computational cost compared with the following two types. Wrapper methods evaluate and select feature subsets based on specific classification accuracies. Thus, their performances are generally sensitive to the classifiers they use [12]. In addition, the computational costs of wrapper methods are relatively high because each candidate of the feature subsets would be utilized to train the classifier. Embedded methods are classifiers where feature selection is integrated into the learning process [2]. They are also classifierspecific, which limits their applications to other classifiers. Ordinarily, Filter is preferable to other types because of its superiority in numerous respects, e.g., remarkable generalization performance among diferent classifiers and high computational eficiency [13].

Filter methods developed in the early stage, such as mutual information maximization (MIM) [14], evaluate and rank features in terms of only the relationship between the feature and the class $( \mathrm { i . e . , }$ class-relevance). Such simplicity renders them highly eficient even in present day applications. However, they have a severe drawback: Features are evaluated individually, and the potential correlations among them that may severely influence the classification performance are not considered. Since it has been indicated that simply combining class-relevant features together cannot guarantee the reasonable performance of the learning method, a natural improvement is to ad ditionally consider dependencies among features [10, 15, 16]. Because the combination of multiple correlations should be taken into account and the corresponding formulated problems are often nonconvex, it appears infeasible to obtain a globally optimal feature subset within polynomial time unless $\mathbf { P } = \mathbf { N P } ,$ . Moreover, a reliable estimation of the joint distribution among features requires a large amount of samples, whereas in most of the real-world cases, samples are insuficient fo even a medium-scale joint estimation. Therefore, a number of existing feature selection methods decompose the objective of feature selection into multiple sub-objectives, including maximizing class-relevance and minimizing feature inner-correlations $( \mathbf { e . g . }$ , redundancy) [17], and apply heuristic searching strategies and approximate dependence ana lysis $( \mathbf { e . g . }$ , pairwise correlation analysis) for each sub-objective to fi nally obtain satisfactory solutions, i.e., to determine well-qualified fea ture subsets [e.g., Refs. 8, 18] or feature sequences of which the top ranked features are salient for data representation [e.g., Refs. 10, 19, 20]. Besides, explicit decomposing the objective of feature selection into multiple sub-objectives can improve the interpretability of the results for real-world applications, e.g., practitioners and empirical re searchers can find potential collinearity by conducting redundancy analysis. However, most of the heuristic strategies employed in these methods seem to be intuitive and unsound. In addition, approximate strategies like pairwise correlation analysis may lead to significant bias in measuring feature dependencies. All these deficiencies result in an unstable performance of such methods.

Recently, sparse representation techniques have attracted increasing attention in numerous domains because they aim to obtain a small group of patterns to optimally recover the target, which can be formulated using a $\ell _ { 0 } -$ norm objective or regularization term [21]. In the context of feature selection, the aim of sparse representation is to determine a small number of features to preserve the classification accuracy [22-24]. The most significant advantage of sparse representation-based feature selection is that, it provides a unifying and analytically solvable optimization framework for feature selection. Recent feature selection methods with sparse representation techniques utilize a variety of sparse models, such as the models with $\ell _ { 1 } \cdot$ norm [25], ℓ -norm [24], and $\ell _ { 2 , p } { \mathrm { - n o r m } }$ $( 0 < p \leq 1 )$ [26], to select representative features. However, minimizing an $\ell _ { p } .$ -norm $( 0 \leq p < 1 )$ regularized objective is proved to be strongly NP-hard [21]. Although there are several relaxations, e.g., $\ell _ { 1 } \cdot$ or $\ell _ { 2 } .$ -norm as convex approximations, matrix computation incurs excessive execution time and space cost, and thus hinders the implementation of such methods on large-scale datasets. In addition, extant feature selection methods with sparse representation techniques do not explicitly handle feature inner-correlations, i.e., redundancy and complementarity [27], which is likely to severely influence the performance of the classification. This makes it similar to a black box, wherein it is infeasible to exactly determine whether or not suficient eforts have been undertaken to handle feature inner-correlations.

Considering these, in this study, we propose a novel feature ranking method wherein sparse representation and information theoretic metrics are integrated to discriminate salient features, taking advantage of both sparse representation and feature inner-correlation analysis. More specifically, the proposed method not only utilizes the optimization framework of sparse representation, but also conducts dependence analysis to explicitly handle feature inner-correlations like redundancy and complementarity, in such a way as to obtain a salient and interpretable results for classification modeling. To our knowledge, this work is the first attempt to select features by combining sparse representation technique and information theoretic dependence analysis.

The main contributions of this work that distinguishes it from extant literature are threefold:

• A nonlinear sparse representation method is applied to identify representative feature clusters,

conditional mutual information is used to identify the initial point for kernel orthogonal matching pursuit (OMP) in order to take into account the feature dependence, and

• a novel approximate dependence analysis strategy that can efectively prevent the significant bias caused by pairwise correlation analysis for large-scale feature set is proposed to eliminate redundancy and to keep complementarity.

The remainder of the paper is organized as follows: Section 2 introduces related work. Section 3 briefly describes feature inner-correlations in the context of information theory, the principle of sparse representation, and the overarching framework of the proposed method. Section 4 proposes a feature ranking approach based on kernel OMP. Then, Section 5 proposes a novel approximate redundancy-complementarity analysis. The proposed method is presented in Section 6. Section 7 presents the experimental results and discussions to evaluate the efectiveness of the proposed method in comparison with the representative feature selection methods on nine well-known datasets. Finally, Section 8 summarizes the concluding remark and indicates the future work.

## 2. Related work

## 2.1. Feature selection with dependence analysis

The main objective of the present feature evaluation criteria considering feature dependencies is to identify a set of class-relevant and complementary features, wherein the redundancy among them is minimal. In general, feature dependencies comprise feature redundancy and feature complementarity [20. 28] wherein redundancy has attracted significantly more attention than complementarity due to its detriment to classification performance. In order to identify class-relevance and redundancy, a number of novel feature-evaluation criteria have been developed [8. 17. 19. 29]. For example, Zhang et al. [8] propose a novel improvement of the firefly al gorithm [FA, see e.g., Ref. 30] to efectively eliminate redundancy among the features. The near-optimal feature subsets obtained by their methods significantly outperform those obtained by the typical FA-based feature selection methods in classification and regression modeling. For informa tion theoretic methods, the representative redundancy evaluation criterion is called minimum redundancy and maximum relevance (mRMR) [17]. It applies mutual information (MI) to analyze the class-relevance for each feature and the correlation between any two features. Another example is available in Yu and Liu [15] and Song et al. [31], wherein fast correlation based feature (FCBF) selection algorithms are developed to separately handle class-relevance and redundancy using normalized mutual informa tion. The conditional mutual information maximization (CMIMD) criterior for feature selection is proposed by Fleuret [19]; here, conditional mutual information (CMI) is applied as the metric of feature dependencies. Because CMI and its equivalent variant joint mutual information (JMI) [29, 32] can jointly identify class-relevance and redundancy, they have been widely applied for feature assessment and selection in literature [10, 20, 33, 34]. For example, Meyer and Bontempi [16] and Brown et al. [10] both expand JMI into three dimensions, including class-relevance, redundancy, and in teraction (in Meyer and Bontempi [16], these three dimensions are multi plied by normalization coeficients to penalize inputs with large entropies), to explicitly handle redundancy and complementarity. Zhang et al. [28] regard redundancy and complementarity as two poles of a comprehensive correlation which is called conditional redundancy, and then utilize CMI as the evaluation metric: Wang et al. [34] expand CMI into three terms cor: responding to class-relevance, redundancy, and complementarity, respec tively, and assign diferent weights to the terms to heuristically select fea tures with high class-relevance, high complementarity, and low redundancy. Despite the relatively high eficiency, most of the abovementioned methods conduct dependence analysis by means of pairwise approximation (i.e., only measuring dependence between any two features), and lack reliable double-checking strategies trying to reduce the bias caused by pairwise approximation.

## 2.2. Feature selection with sparse representation techniques

Most extant feature selection works with sparse representation techniques are largely based on the formulations of least square regression (LSR) [35], linear discriminative analysis (LDA) [26], and support vector machines (SVM) [24, 36]. The most popular sparse regularization is $\scriptstyle { \ell _ { 1 } - \mathrm { n o r m } }$ (namely Lasso) [37]. Although feature selection based on ℓ -norm can select sparse features for its computational convenience, the results are often not suficiently sparse. This implies that potential irrelevant and redundant features continue to be present in the selected feature subset. To date, there are two lines of research on sparse representation. One mainly focuses on improving the eficiency of sparse representation on high-dimensional data, where the typical method is called least angle regression (LARS) [22]. The other aims to obtain sparser solutions. For example, a series of works [21, 38, 39] extend $\ell _ { 1 }$ -norm to $\ell _ { p }$ -norm $( 0 < p < 1 )$ , and investigate its properties and possible applications. Xu et al. [40] analyze $\ell _ { 1 / 2 } { \cdot } \mathrm { n o r m }$ regularization and indicate that it exhibits the highest performance among all the $\ell _ { p } { \ - } { \ - } { \mathrm { n o r m } }$ regularizations with $p \in ( 0 , 1 )$ . Then they use $\ell _ { 1 / 2 } { \mathrm { - n o r m ~ r e g } } .$ ularization for robust face recognition [39]. However, the relaxation from $\ell _ { 0 } -$ to ℓ -norm $( 0 < p < 1 )$ cannot theoretically reduce the complexity of the original problem. Furthermore, Chen et al. [41] show that $\ell _ { p } .$ norm $( 0 < p < 1 )$ minimization is also strongly NP-hard; this restricts its application in various fields, particularly where execution time plays an essential role. From the perspective of a trade-of, the strong relaxations such as using $\ell _ { 1 } \cdot$ or $\ell _ { 2 } \cdot$ -norms continue to be widely used in the fields where machine learning and data mining play important roles [23, 24].

Regardless of the convex relaxations, matrix operations still require large execution time and space and thus are nearly intractable on largescale datasets. For example, algorithms based on LSR and LDA with $\ell _ { 2 , p ^ { - } }$ norm $( 0 < p \ \le \ 2 )$ regularization [11, 26, 35, 42] all required the construction of a transformation matrix $\textbf { D } \in \mathbb { R } ^ { m \times m }$ (m denotes the number of features in the feature space), resulting in large time and space overhead and thus hindering the use of such methods to address high-dimensionality.

## 3. Preliminaries and the framework

## 3.1. Redundancy and complementarity from information theoretic perspective

As mentioned previously, the objective of feature selection can be factorized into interpretable sub-objectives that are necessary for dependence analysis using information theoretic metrics. In this section, we introduce certain necessary albeit fundamental information theo retic metrics that will be employed by the proposed method in the following context. Entropy, an essential quantitative description of information, is used to measure the extent of uncertainty for the dis tribution of a random variable X. It has the following formulation:

$$
H (X) = - \int_ {X} p (x) \mathrm{log} p (x) \mathrm{d} x,\tag{1}
$$

where x is the possible value assignment of $X , p ( \cdot )$ is the probability density function (for convenience, we hereafter use the notation log to denote logarithm to the base two). According to information theory, conditional entropy could be used to quantify the uncertainty of a variable conditioned on another. The conditional entropy of X given Y is defined as

$$
H (X | Y) = - \iint_ {X Y} p (x y) \log p (x | y) d x d y,\tag{2}
$$

Then, we can formulate the mutual information (MI) between two random variables X and Y:

$$
\begin{array}{r l} {I (X; Y) =} & {\iint_ {X Y} p (x y) \mathrm{log} \frac {p (x y)}{p (x) p (y)} \mathrm{d} x \mathrm{d} y} \\ {=} & {H (X) - H (X | Y),} \end{array}\tag{3}
$$

where x and $y$ are the possible value assignments of X and $\boldsymbol { Y } ,$ respectively. MI can be considered as the amount of information shared by two variables. In the context of feature selection, MI is one of the most widely used metrics for measuring the correlation intensity of two features. Note that MI is symmetrical, i.e., $I ( X ; Y ) = I ( Y ; X ) . \ I ( X ; Y ) = 0$ implies that X and Y are statistically independent.

Estimating MI between two random variables given the third can be achieved by CMI, which is widely used in information theoretic learning methods. CMI is defined as

$$
\begin{array}{r l} {I (X; Y | Z) =} & {\iiint_ {X Y Z} p (x y z) \log \frac {p (x y | z)}{p (x | z) p (y | z)} \mathrm{d} x \mathrm{d} y \mathrm{d} z} \\ {=} & {H (X | Z) - H (X | Y, Z).} \end{array}\tag{4}
$$

I(X;Y |Z) can be interpreted as the information shared by X and Y given the value of a third variable Z. CMI is also symmetrical for X and Y. A remarkable property of CMI in feature evaluation is that it can efectively distinguish useful features from useless ones. A large value of I(X;Y |Z) implies a strong relevance between X and Y when the distribution of $z$ is known, whereas a small I(X;Y |Z) implies negligible relevance when the distribution of Z is known, regardless of the original correlation between X and Y. For feature selection, the latter advantage prevents unnecessary eforts for further identifying whether X and Y are originally irrelevant or redundant when Z is given.

According to Brown et al. [10] and Chen et al. [27], CMI can simultaneously capture three essential feature correlations: class-relevance, redundancy, and complementarity among features. This can be demonstrated by expanding CMI as

$$
I (F _ {1}; C | F _ {2}) = I (F _ {1}; C) - I (F _ {1}; F _ {2}) + I (F _ {1}; F _ {2} | C).\tag{5}
$$

Herein, the first term on the right-hand side of Eq. (5) captures the class-relevance of $F _ { 1 } ,$ the second captures the redundancy between $F _ { 1 }$ and $F _ { 2 } ,$ and the final term captures the complementary correlation between $F _ { 1 }$ and $F _ { 2 } .$ This renders CMI a highly efective metric that can simultaneously give attention to the three feature correlations that play crucial roles in feature selection.

## 3.2. Sparse representation and orthogonal matching pursuit

In this section, we briefly introduce the fundamental formula of sparse representation and an efective solver named orthogonal matching pursuit (OMP) that will be applied in the proposed method. Recently, sparse representation has been playing increasingly important roles in feature selection and sparse reconstruction [21, 38, 41]. In general, sparse representation can be formalized as the determination of an optimal solution of a minimization programming wherein the objective function is the sum of a data-fitting term in ℓ -norm and a regularization term in ℓ -norm. As ℓ -norm minimization is strongly NPhard, its convex relaxation using $\ell _ { p } .$ norm $( p \geq 1 )$ is often applied in literature [41]. With a slight abuse of notation, let $\mathbf { F } = ( F _ { 1 } , . . . , F _ { k } )$ (where k is the number of features) and the i-th feature $F _ { i } = ( f _ { i , i } , . . . , f _ { n , i } ) ^ { T }$ (where $f _ { j , i }$ is the value of $F _ { i }$ in the j-th sample and n is the number of samples). Then, a linear sparse representation of the class C can be ideally described by all the features as

$$
C = \beta_ {1} \cdot \left( \begin{array}{c} f _ {1, 1} \\ \dots \\ f _ {n, 1} \end{array} \right) + \beta_ {2} \cdot \left( \begin{array}{c} f _ {1, 2} \\ \dots \\ f _ {n, 2} \end{array} \right) + \ldots + \beta_ {k} \cdot \left( \begin{array}{c} f _ {1, k} \\ \dots \\ f _ {n, k} \end{array} \right).\tag{6}
$$

Herein, $\pmb { \beta } = ( \beta _ { 1 } , \beta _ { 2 } , . . . , \beta _ { k } ) ^ { T } \in \mathbb { R } ^ { k }$ is a coeficient vector where most of the entries are expected to be zero. This can be obtained by solving the following minimization programming

$$
\min _ {\boldsymbol {\beta} \in \mathbb {R} ^ {k}} \| \boldsymbol {\beta} \| _ {0}, \quad \text { s.t. } \quad \mathbf {F} \cdot \boldsymbol {\beta} = C,\tag{7}
$$

where $\lVert \cdot \rVert _ { 0 }$ denotes the number of nonzero entries in the norm. However, model (7) is strongly NP-hard, rendering it infeasible to be exactly solved even within pseudo-polynomial time unless $\mathbf { P } = \mathrm { N P }$ . Recent development in compressed sensing indicates that if the exact solution is suficiently sparse, it can be obtained by solving the following relaxed programming with $p = 1 \ [ 4 3 ] ;$

$$
\min _ {\boldsymbol {\beta} \in \mathbb {R} ^ {k}} \| | \boldsymbol {\beta} \| _ {p} = \left(\sum_ {i = 1} ^ {k} | \beta_ {i} | ^ {p}\right) ^ {1 / p}, \quad \text {s.t.} \quad \mathbf {F} \cdot \boldsymbol {\beta} = C.\tag{8}
$$

The objective of model (8) is convex when $p = 1 _ { : }$ , and thus, optimal $\beta ^ { * }$ can be achieved within polynomial time. Because real-world datasets ordinarily have redundancy among the samples (i.e., sample matrices are not fully ranked), the equivalent relationship in the constraint of model (8) cannot strictly hold. A dense noise ψ is hence introduced and the equation becomes $C = \mathbf { F } \cdot \pmb { \beta } + \psi .$ Now, the problem is transformed to

$$
\min _ {\boldsymbol {\beta} \in \mathbb {R} ^ {k}} \| \boldsymbol {\beta} \| _ {p} = \left(\sum_ {i = 1} ^ {k} | \boldsymbol {\beta} _ {i} | ^ {p}\right) ^ {1 / p}, \quad \text {s.t.} \quad \| \mathbf {F} \cdot \boldsymbol {\beta} - C \| _ {2} \leq \epsilon\tag{9}
$$

where ϵ is the upper bound of $\| \psi \| _ { 2 }$ . The Lagrangian form of model (9) is represented as

$$
\min _ {\boldsymbol {\beta} \in \mathbb {R} ^ {k}} \| \mathbf {F} \cdot \boldsymbol {\beta} - C \| _ {2} ^ {2} + \lambda \cdot \| \boldsymbol {\beta} \| _ {p} ^ {p},\tag{10}
$$

where λ is the regularized coeficient. Model (10) is the style of the popular Lasso when $p = 1$ . As a trade-of between runtime and accuracy, a greedy algorithm called orthogonal matching pursuit (OMP) that performs reasonably in sparse representation in various fields [44] can be utilized to solve $\mathbf { E q . } \left( 1 0 \right)$ . Before we describe the process of OMP, we denote Ω as the index vector comprising the indices of the current selected features from F and $\mathbf { F } _ { \Omega }$ as the feature subset (the submatrix of F) where the entries (columns) are the selected features from F indexed by Ω, with a marginal abuse of notation. We use the superscript to denote the iteration step and the subscript to denote the index of the entry (column) in the set (matrix).

Algorithm 1. Orthogonal matching pursuit

OMP is a stepwise forward selection algorithm and is simple to implement. However, model (10) can only capture linear correlation in real-world tasks. Because the efectiveness of the linear sparsity model largely depends on the structure of the data, it may not enable suficiently accurate dimension reduction to be reliable if the data is not suficiently linearly-separable. Kernel-based algorithms [45] implicitly exploit the nonlinear structure of the data. Kernel methods can be applied to transform the data into a higher dimensional space via a transformation $\phi ( \cdot )$ such that the resulting transformed data becomes more separable and comply with the linear sparsity model. In this work, kernel operators are embedded in model (10) and thus render the model more robust in real-world feature selection tasks.

Given the transformed vectors $\mathbf { x } { \mapsto } \phi ( \mathbf { x } )$ and $\mathbf { y } { \mapsto } \phi ( \mathbf { y } )$ , the kernel function $\kappa : \mathbb { R } ^ { n } \times \mathbb { R } ^ { n } \mapsto \mathbb { R }$ , can be defined as the inner product of the transformed vectors: $\kappa ( \mathbf { x } , \mathbf { y } ) = \boldsymbol { \phi } ( \mathbf { x } ) ^ { T } \cdot \boldsymbol { \phi } ( \mathbf { y } )$ . The linear sparsity model (10) can be transformed as

$$
\min _ {\boldsymbol {\beta} \in \mathbb {R} ^ {k}} \| \mathbf {F} _ {\phi} \cdot \boldsymbol {\beta} - \phi (C) \| _ {2} ^ {2} + \lambda \cdot \| \boldsymbol {\beta} \| _ {p} ^ {p},\tag{11}
$$

where $\mathbf { F } _ { \phi } = ( \phi ( F _ { 1 } ) , . . . , \phi ( F _ { k } ) )$ ). Gaussian radial basis function (RBF) with the form

$$
\kappa (\mathbf {x}, \mathbf {y}) = \exp \left(- \frac {\| \mathbf {x} - \mathbf {y} \| _ {2}}{2 \sigma^ {2}}\right)\tag{12}
$$

is mostly applied, and it performs efectively in real-world applications [45]. In the following section, Gaussian RBF will be applied as the kernel function and Algorithm 1 will be modified to solve model (11) for the feature clustering task.

## 3.3. The proposed framework

Efective data-driven decision support systems require the raw data from multiple sources to be eficiently gathered and pre-processed for redundancy and noise elimination to facilitate classification modeling and enhance the performance for undertaking data-driven decisionmaking processes. Fig. 1 provides the diagram of the decision support process that integrates the framework of our proposed feature assessment and ranking method.

The framework of the proposed method shown in Fig. 1 consists of two main submodules. The first submodule (shown in left-hand side of Fig. 1) focuses on feature clustering. That is, it utilizes sparse representation techniques to categorize features into representative and

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: F /* feature set */, C /* class */
Output: S /* selected feature subset */, Ω /* Indices of selected features in F */
1 Initialize S ← ∅, Ω⁰ ← ∅, residual r⁰ = C, i ← 1 /* iteration counter */
2 repeat
3    Greedy search: Find the feature  $\widetilde{F}_{j}$  satisfying  $\max_{F \in F} \{F^{T} \cdot r^{i-1}\}$ 
4    Ωⁱ = Ωⁱ⁻¹ ∪ {j}
5    Projection: Pᵢ ← FΩⁱ · (FΩⁱᵀ · FΩⁱ)⁻¹ · FΩⁱᵀ /* Pᵢ denotes the projection onto the linear space spanned by the elements of FΩⁱ */
6    Update current residual: rⁱ ← (I - Pᵢ) · C /* I denotes the identity matrix. */
7    i ← i + 1
8 until the stopping criterion is satisfied, i.e.,  $\frac{||r^i||_2}{||r^i-1||_2} \geq 0.95;$ 
9 S ← FΩⁱ
10 return S
</div>

![](/api/attachments/RKDG4YPS/fulltext/images/6d45683319e6df13fa46defc6ba7145003c05f3d05ff8ab451321b1b0a1e66a4.jpg)  
Fig. 1. The process diagram for data-driven decision support processes.

non-representative groups according to a certain task. The representative features are candidates for final-selected features with high importance weights, while the non-representative features are weighted relatively lighter but still possible to be identified as representative in the next iterations. The second submodule (shown in right-hand side of Fig. 1) conducts dependence analysis for the representative features obtained from the first submodule for redundancy elimination and complementarity identification using information theoretic metrics. The features identified as redundant in this stage will be finally eliminated, because they may impair the discriminative power of other representative features with higher importance weights. Those identified as relevant or complementary will be assessed as salient features and finally top-ranked among the selected features.

Next, we introduce in detail the sparse representation technique and the information theoretic dependence analysis applied in the proposed method, and the collaborative feature selection process of the two

submodules.

## 4. Feature clustering by sparse representation

Sparse representation techniques can efectively select a small part of the features to represent the class. That is, features are separated into two groups: one group contains the selected relevant features for class representation, and the other contains the rest. Thus, sparse representation techniques are preeminent choices as clustering methods for class-relevance analysis. This task can be efectively formulated using model (11). Regarding the nonlinearity of the feature space, the kernel operator is a better choice to be applied in our method. Accordingly, OMP is required to be modified to nonlinear orthogonal matching pursuit (NOMP) to efectively capture the nonlinear correlations among the features. Recall that the inner product computation is conducted three times in Algorithm 1, namely, greedy search (line 3 in

Algorithm 1), projection (line 5), and residual updating (line 6). The kernel operator thus replaces the inner product and is integrated into each of them as follows. For convenience, certain notations in the Matlab syntax will be used in the following context. Let $\Gamma _ { \phi } \in \mathbb { R } ^ { k }$ be the kernel vector of which the j-th entry $\Gamma _ { \phi } ( j ) = \kappa ( F _ { j } , C )$ , and $\dot { \mathbf { A } } _ { \phi } \in \mathbb { R } ^ { k \times k }$ be the kernel matrix of which the $( j , l ) \ – \mathrm { t h }$ entry $\Lambda _ { \phi } ( j , l ) = \kappa ( F _ { j } , F _ { l } ) . \ \Gamma _ { \phi } ( \Omega )$ denotes the vector of which the entries are the corresponding ones in $\Gamma _ { \phi }$ indexed by the entries of Ω. $\Lambda _ { \phi } ( \Omega , \Omega )$ denotes the matrix of which the columns and rows are the corresponding ones in $\Lambda _ { \phi }$ indexed by the entries of $\Omega ,$ respectively. Then, the projection matrix P can be formulated as

$$
\begin{array}{r l} \mathbf {P} = & [ \phi (F _ {\Omega_ {1}}),..., \phi (F _ {\Omega_ {| \Omega |}}) ] \cdot ([ \phi (F _ {\Omega_ {1}}),..., \phi (F _ {\Omega_ {| \Omega |}}) ] ^ {T} \cdot [ \phi (F _ {\Omega_ {1}}),..., \phi (F _ {\Omega_ {| \Omega |}}) ]) ^ {- 1} \\ & \cdot [ \phi (F _ {\Omega_ {1}}),..., \phi (F _ {\Omega_ {| \Omega |}}) ] ^ {T} \\ = & [ \phi (F _ {\Omega_ {1}},..., \phi (F _ {\Omega_ {| \Omega |}}) ] \cdot \boldsymbol {\Lambda} _ {\phi} ^ {- 1} (\Omega , \Omega) \cdot [ \phi (F _ {\Omega_ {1}}),..., \phi (F _ {\Omega_ {| \Omega |}}) ] ^ {T} \end{array}\tag{13}
$$

The residual updating process can be formulated as

$$
\begin{array}{r l} \phi (\mathbf {r}) = & (\mathbf {I} - \mathbf {P}) \cdot \phi (C) \\ = & \phi (C) - [ \phi (F _ {\Omega_ {1}}),..., \phi (F _ {\Omega_ {| \Omega |}}) ] \cdot \boldsymbol {\Lambda} _ {\phi} ^ {- 1} (\Omega , \Omega) \cdot [ \phi (F _ {\Omega_ {1}}),..., \phi (F _ {\Omega_ {| \Omega |}}) ] ^ {T} \\ & \cdot \phi (C). \end{array}
$$

Since $\mathbf { P } ^ { 2 } = \mathbf { P } ,$ we can get

$$
\begin{array}{r l} \kappa (F _ {j} ^ {T}, \mathbf {r} ^ {i}) = & \phi (F _ {j}) ^ {T} \cdot \phi (\mathbf {r} ^ {i}) \\ = & \phi (F _ {j}) ^ {T} \cdot \phi (C) - \phi (F _ {j}) ^ {T} \cdot [ \phi (F _ {\Omega_ {1} ^ {i}}),..., \phi (F _ {\Omega_ {| \Omega^ {i} |} ^ {i}}) ] \cdot \boldsymbol {\Lambda} _ {\phi} ^ {- 1} (\Omega^ {i}, \Omega^ {i}) \\ & \cdot [ \phi (F _ {\Omega_ {1} ^ {i}}),..., \phi (F _ {\Omega_ {| \Omega^ {i} |} ^ {i}}) ] ^ {T} \cdot \phi (C) \\ = & \kappa (F _ {j}, C) - [ \kappa (F _ {j}, F _ {\Omega_ {1} ^ {i}}),..., \kappa (F _ {j}, F _ {\Omega_ {| \Omega^ {i} |} ^ {i}}) ] \cdot \boldsymbol {\Lambda} _ {\phi} ^ {- 1} (\Omega^ {i}, \Omega^ {i}) \\ & \underset {\Gamma_ {\phi} (j)} {\widetilde {\Gamma_ {\phi} (j)}} - \underset {\boldsymbol {\Lambda} _ {\phi} (j, \Omega^ {i})} {\widetilde {\Gamma_ {\phi} (j , \Omega^ {i})}} \\ & \cdot [ \kappa (F _ {\Omega_ {1} ^ {i}}, C),..., \kappa (F _ {\Omega_ {| \Omega^ {i} |} ^ {i}}, C) ] ^ {T} \\ = & \Gamma_ {\phi} (j) - \boldsymbol {\Lambda} _ {\phi} (j, \Omega^ {i}) \cdot \boldsymbol {\Lambda} _ {\phi} ^ {- 1} (\Omega^ {i}, \Omega^ {i}) \cdot \boldsymbol {\Gamma} _ {\phi} (\Omega^ {i}), \end{array}\tag{16}
$$

(14)

Eq. (16) illustrates a straightforward implementation of kernelbased OMP: It renders the greedy search executable without the knowledge of the values of $\phi ( F _ { j } )$ and $\phi ( \mathbf { r } ^ { i } )$ . It should be also noted that the distance captured by $| | \boldsymbol { F } - \dot { \boldsymbol { C } } | | _ { 2 } ^ { 2 }$ is likely to be excessively large for F ∈F because of dimensional inconsistency between the features and the class. This may result in accuracy loss or even invalid computational results when it is implemented using computing platforms such as Matlab. To achieve this, we apply $\| \mathbf F \| _ { F }$ as the modified factor and use $\parallel F - C \parallel _ { 2 } ^ { 2 }$ <sup>2</sup> rather than $\| \boldsymbol { F } - \boldsymbol { C } \| _ { 2 } ^ { 2 }$ in the proposed method. We give the $\overline { { | | \textbf { F } | | _ { F } } }$ pseudo code of NOMP in Algorithm 2.

Algorithm 2. Nonlinear orthogonal matching pursuit.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: F /* feature set */, C /* class */
Output: S /*selected feature subset*/, Ω /* Indices of selected features in F */
1 Initialize: Calculate  $\Gamma_{\phi}$  and  $\Lambda_{\phi}$ ,  $r^{0} \leftarrow C$ ,  $S \leftarrow \varnothing$ ,  $\Omega^{0} \leftarrow \varnothing$ ,  $i \leftarrow 1$ 
2 Calculate  $||\phi(\mathbf{r}^{0})||_{2} = \sqrt{\kappa(C,C)}$ 
3  $\Omega^{1} \leftarrow \Omega^{0} \cup \{j | \arg\max_{j} \Gamma_{\phi}(j)\}$ 
4 repeat
5 Find the feature  $\widetilde{F}_{j}$  satisfying the maximization problem:
6  $\max_{F \in \mathbf{F}} \{\Gamma_{\phi}(j) - \Lambda_{\phi}(j, \Omega^{i}) \cdot (\Lambda_{\phi}(\Omega^{i}, \Omega^{i}) + \lambda \cdot \mathbf{I})^{-1} \cdot \Gamma_{\phi}^{T}(\Omega^{i})\}$ 
7  $\Omega^{i+1} = \Omega^{i} \cup \{j\}$ 
8 Calculate  $||\phi(\mathbf{r}^{i})||_{2} = \sqrt{\kappa(\mathbf{r}^{i}, \mathbf{r}^{i})}$  in terms of Eq.(15)
9  $i \leftarrow i + 1$ 
10 until the stopping criterion is satisfied, i.e.,  $\frac{||\phi(\mathbf{r}^{i})||_{2}}{||\phi(\mathbf{r}^{i-1})||_{2}} \geq 0.95;$ 
11  $S \leftarrow F_{\Omega^{i+1}}$ 
12 return S
</div>

$$
\begin{array}{r l} \kappa (\mathbf {r}, \mathbf {r}) = & \phi (\mathbf {r}) ^ {T} \cdot \phi (\mathbf {r}) \\ = & \kappa (C, C) + \phi (C) ^ {T} \cdot (\mathbf {P} ^ {2} - 2 \mathbf {P}) \cdot \phi (C) \\ = & \kappa (C, C) - \phi (C) ^ {T} \cdot [ \phi (F _ {\Omega_ {1}}),..., \phi (F _ {\Omega_ {| \Omega |}}) ] \cdot \boldsymbol {\Lambda} _ {\phi} ^ {- 1} (\Omega , \Omega) \\ & \quad \cdot [ \phi (F _ {\Omega_ {1}}),..., \phi (F _ {\Omega_ {| \Omega |}}) ] ^ {T} \cdot \phi (C) \\ = & \kappa (C, C) - [ \kappa (C, F _ {\Omega_ {1}}),..., \kappa (C, F _ {\Omega_ {| \Omega |}}) ] \cdot \boldsymbol {\Lambda} _ {\phi} ^ {- 1} (\Omega , \Omega) \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {and} \\ & = & \kappa (C, C) - \Gamma_ {\phi} ^ {T} (\Omega) \cdot \boldsymbol {\Lambda} _ {\phi} ^ {- 1} (\Omega ,   \Omega) \cdot \boldsymbol {\Gamma} _ {\phi} (\Omega). \\ & = & \kappa (C, C) - \Gamma_ {\phi} ^ {T} (\Omega) \cdot \boldsymbol {\Lambda} _ {\phi} ^ {- 1} (\Omega ,   \Omega) \cdot \boldsymbol {\Gamma} _ {\phi} (\Omega). \\ & = & \kappa (C, C) - [ F _ {\Omega_ {1}} ] ^ {T} [ F _ {\Omega_ {1}} ] ^ {T} [ F _ {\Omega_ {1}} ] ^ {T} [ F _ {\Omega_ {1}} ] ^ {T} [ F _ {\Omega_ {1}} ] ^ {T} [ F _ {\Omega_ {1}} ] ^ {T} [ F _ {\Omega_ {1}} ] ^ {T} [ F _ {\Omega_ {1}} ] ^ {T} [ G _ {\Omega_ {1}} ] ^ {T} [ G _ {\Omega_ {1}} ] ^ {T} [ G _ {\Omega_ {1}} ] ^ {T} [ G _ {\Omega_ {1}} ] ^ {T} [ G _ {\Omega_ {1}} ] ^ {T} [ G _ {\Omega_ {1}} ] ^ {T} [ G _ {\Omega_ {1}} ] ^ {T} [ G _{\Omega_ {1}} ] ^ {T} [ G _{\Omega_ {1}} ] ^ {T} [ G _{\Omega_ {1}} ] ^ {T} [ G _{\Omega_ {1}} ] ^ {T} [ G _{\Omega_ {1}} ] ^ {T} [ G _{\Omega_ {1}} ] ^ {T} [ G _{\Omega_ {1}} ] ^ {T} [ G _{\Omega_{1}} ] ^ {T} [ G _{\Omega_{1}} ] ^ {T} [ G _{\Omega_{1}} ] ^ {T} [ G _{\Omega_{1}} ] ^ {T} [ G _{\Omega_{1}} ] ^ {T} [ G _{\Omega_{1}} ] ^ {T} [ G _{\Omega_{1}} ] ^ {T} [ G _{\Omega_{1}} ] ^ {T} [G _{\Omega_{1}} ] ^{T} [G _{\Omega_{1}} ] ^{T} [G _{\Omega_{1}} ] ^{T} [G _{\Omega_{1}} ] ^{T} [G _{\Omega_{1}} ] ^{T} [G _{\Omega_{1}} ] ^{T} [G _{\Omega_{1}} ] ^{T} [G _{\Omega_{1}} ] ^{T} [G _{\Omega_{2}} ] ^{T} [G _{\Omega_{2}} ] ^{T} [G _{\Omega_{2}} ] ^{T} [G _{\Omega_{2}} ] ^{T} [G _{\Omega_{2}} ] ^{T} [G _{\Omega_{2}} ] ^{T} [G _{\Omega_{2}} ] ^{T} [G _{\Omega_{2}} ] ^{T} [G_{\Omega_{2}}] ^{T} [G_{\Omega_{2}}] ^{T} [G_{\Omega_{2}}] ^{T} [G_{\Omega_{2}}] ^{T} [G_{\Omega_{2}}] ^{T} [G_{\Omega_{2}}] ^{T} [G_{\Omega_{2}}] ^{T} [G_{\Omega_{2}}] ^{T} [G_\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\partial_{\partial}\\ & = & K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathbf {r}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {R}) = K(\mathcal {S}). \\ & = & K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathbb {E}), \\ & = & K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathcal {R}) = K (\mathbb {E}), \\ & = & K (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathbb {E}), \\ & = & k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathbb {E}), \\ & = & k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = <   k (\mathcal {R}), \\ & = & k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) = k (\mathcal {R}) <   k (\mathcal {R}), \\ & = & k (\mathcal {R}) = k (\mathcal {R}) > 0. \\ & = & k (\mathcal {R}) > 0. \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). <   k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & k (\mathcal {\Sigma}). \\ & = & <   k (\mathcal {\Sigma}). \\ & = & <   k (\mathcal {\Sigma}). \\ & = & <   k (\mathcal {\Sigma}). \\ & = & <   k (\mathcal {\Sigma}). \\ & = & <   k (\mathcal {\Sigma}). \\ & = & <   k (\mathcal {\Sigma}). \\ & = & <   k (\mathcal {\Sigma}). \\ & = & <   k (\mathcal {\Sigma}). \\ *\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^ {\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*^{+}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{+}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^{\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\>\\*{}^ {\prime}\\> \\*\end{array}
$$

For the greedy search process, suppose it is in the i-th step; then, we obtain

(15)

The stop rule of NOMP applied in Algorithm 2 depends on the noise structure of the data [44]. In the noiseless case, the rule should be $\mathbf { r } = 0 .$ . In this work, the convergence of NOMP is measured as the change in the residual r, and we heuristically set the stop rule as $\frac { \parallel \phi ( \mathbf { r } ^ { i } ) \parallel _ { 2 } } { \parallel \phi ( \mathbf { r } ^ { i - 1 } ) \parallel _ { 2 } } \geq 0 . 9 5 .$ . In addition, it should be noted that $\Delta _ { \phi } ( \Omega ^ { i } , \Omega ^ { i } )$ cannot be guaranteed to be nonsingular in many cases. Since a valid inversion can be conducted only on nonsingular matrices, a regularization term is introduced by adding a constant value to the diagonal elements of $\Lambda _ { \phi } ( \Omega ^ { i } , \Omega ^ { i } )$ , i.e., $\Lambda _ { \phi } ( \Omega ^ { i } , \Omega ^ { i } ) + \lambda \ { \cdot } { \bf I } ( \lambda > 0 ) .$ λ is generally a small number and is set as 0.0005 in the proposed method.

## 5. Approximate dependence analysis

As mentioned previously, feature selection methods with sparse representation do not explicitly handle redundancy and complementarity. It seems hard to know exactly whether or not those methods undertake suficient eforts to handle feature inner-correlations. On the contrary, information theoretic feature evaluation strategies generally achieve remarkable performances in redundancy and complementarity analysis and thus are included in this work to cover the deficiency of sparse representation techniques with respect to these aspects.

![](/api/attachments/RKDG4YPS/fulltext/images/d0f8b38c2106c0d3a7ef9dd45d05fcbd7c5a04d090a08bbed72c0a78fed1fd47.jpg)  
Fig. 2. Process diagram of dependence analysis in the proposed method.

Because highly correlated features are likely to exhibit similar dis criminative power, taking into account only the relevance between the features and the class is likely to result in two neglects, which possibly impair the quality of the selected features for classification [27]: One is the neglect of redundancy among the selected features, caused by the assumption of individual independence of features (e.g. MIM). The other is the neglect of group capacity of features, caused by only measuring pairwise redundancy among features (e.g. mRMR). For example, features with low individual capacity are identified as either irrelevant or redundant by measuring their pairwise correlation. However, it is also likely that some of those features contribute largely to the discriminative power of the whole feature subset if they are selected. Thus, feature complementarity becomes a conspicuous correlation among features that should be applied to partially prevent the bias caused by pairwise redundancy analysis [27, 46]. However, such a complementarity analysis in literature still focuses on pairwise correlation of features, whereas k-wise (k ≥ 3) complementary correlation among features are omitted; this is likely to also result in bias in feature evaluation, particularly when the size of the selected feature subset is large.

In this section, we focus on dependence analysis for the features generated within each execution of NOMP. The highlight of this strategy is that it can efectively prevent bias caused by the pairwise correlation analysis, because the feature subset (cluster) selected from each iteration is almost constrained in a small scale (owing to the ef fective sparse representation of the features). We start our analysis from the perspective of redundancy–complementarity dimension because redundancy and complementarity can be measured comprehensively as two dimensions of feature dependence [27]. The detailed procedure of the redundancy–complementarity analysis in the proposed method is depicted in Fig. 2. Specifically, the procedure first identifies the dependence of the features from the perspective of the redundancy–complementarity dimension: If complementarity arises, the features are selected; otherwise, the dominance of the features (i.e., which feature contributes more to the discriminative capability) is further analyzed to determine which one is redundant. In addition, to partially overcome the estimation bias arising from the finite samples, a significance rule is finally introduced to eliminate redundancy.

## 5.1. Redundancy–complementarity identification

To illustrate the dependence identification process in detail, we first propose certain equivalent transformations of MI and CMI in the following theorem.

Theorem 1. For ∀F ,F ∈F (F ≠F ) and the class $C ,$ we have

$$
I (F _ {i} F _ {j}; C) \geq I (F _ {i}; C) + I (F _ {j}; C)\tag{17}
$$

$$
\longleftrightarrow I (F _ {i}; C) \leq I (F _ {i}; C | F _ {j})\tag{18}
$$

$$
\longleftrightarrow I (F _ {j}; C) \leq I (F _ {j}; C | F _ {i}).\tag{19}
$$

Proof. Without loss of generality, we only need to prove

$$
I (F _ {i} F _ {j}; C) \geq I (F _ {i}; C) + I (F _ {j}; C) \longleftrightarrow I (F _ {i}; C) \leq I (F _ {i}; C | F _ {j}).
$$

$$
\begin{array}{l} I (F _ {i}; F _ {j}, C) \geq I (F _ {i}, C) + I (F _ {j}, C) \leq I (F _ {i}, C) \geq I (F _ {i}, C, F _ {j}) \\ \text {Since} \\ I (F _ {i}; F _ {j}) - I (F _ {i}; F _ {j} | C) \\ = \iint_ {F _ {i} F _ {j}} p (f _ {i} f _ {j}) \log \frac {p (f _ {i} f _ {j})}{p (f _ {i}) p (f _ {j})} d f _ {i} d f _ {j} \\ - \iiint_ {F _ {i} F _ {j} C} p (f _ {i} f _ {j} c) \log \frac {p (f _ {i} f _ {j} | c)}{p (f _ {i} | c) p (f _ {j} | c)} d f _ {i} d f _ {j} d c \end{array}\tag{20}
$$

(21)

and with the fact

$$
p (f _ {i} f _ {j}) = \int_ {C} p (f _ {i} f _ {j} c) \mathrm{d} c,
$$

Eq. (20) can be rewritten as

$$
= \iiint_ {F _ {i} F _ {j} C} p (f _ {i} f _ {j} c) \log \frac {p (f _ {i} f _ {j})}{p (f _ {i}) p (f _ {j})} \mathrm{d} f _ {i} \mathrm{d} f _ {j} \mathrm{d} c
$$

With Eqs. (21) and (22), we have

$$
\begin{array}{l} I (F _ {i}; F _ {j}) - I (F _ {i}; F _ {j} | C) \\ = \iiint_ {F _ {i} F _ {j} C} p (f _ {i} f _ {j} c) \log \left(\frac {p (f _ {i} f _ {j})}{p (f _ {i}) p (f _ {j})} \cdot \frac {p (f _ {i} | c) p (f _ {j} | c)}{p (f _ {i} f _ {j} | c)}\right) \mathrm{d} f _ {i} \mathrm{d} f _ {j} \mathrm{d} c \\ = \iiint_ {F _ {i} F _ {j} C} p (f _ {i} f _ {j} c) \log \frac {p (f _ {i} f _ {j}) p (f _ {i} c) p (f _ {j} c)}{p (f _ {i}) p (f _ {j}) p (c) p (f _ {i} f _ {j} c)} \mathrm{d} f _ {i} \mathrm{d} f _ {j} \mathrm{d} c \\ = \iiint_ {F _ {i} F _ {j} C} p (f _ {i} f _ {j} c) \log \left(\frac {p (f _ {i} c)}{p (f _ {i}) p (c)} \cdot \frac {p (f _ {i} f _ {j}) p (f _ {j} c)}{p (f _ {i} f _ {j} c) p (f _ {j})}\right) \mathrm{d} f _ {i} \mathrm{d} f _ {j} \mathrm{d} c \\ = \iint_ {F _ {i} C} p (f _ {i} c) \log \frac {p (f _ {i} c)}{p (f _ {i}) p (c)} \mathrm{d} f _ {i} \mathrm{d} c \\ - \iiint_ {F _ {i} F _ {j} C} p (f _ {i} f _ {j} c) \log \frac {p (f _ {i} c | f _ {j})}{p (f _ {i} | f _ {j}) p (c | f _ {j})} \mathrm{d} f _ {i} \mathrm{d} f _ {j} \mathrm{d} c \\ = I (F _ {i}; C) - I (F _ {i}; C | F _ {j}), \end{array}\tag{22}
$$

i.e.

$$
I (F _ {i}; F _ {j}) - I (F _ {i}; F _ {j} | C) = I (F _ {i}; C) - I (F _ {i}; C | F _ {j}),\tag{23}
$$

we have

$$
I (F _ {i}; C | F _ {j}) = I (F _ {i}; C) - I (F _ {i}; F _ {j}) + I (F _ {i}; F _ {j} | C).\tag{24}
$$

According to the chain rule of CMI [47], we have

$$
I (F _ {i} F _ {j}; C) = I (F _ {j}; C) + I (F _ {i}; C | F _ {j}).\tag{25}
$$

With Eqs. (24) and (25), we obtain

$$
I (F _ {i} F _ {j}; C) = I (F _ {i}; C) + I (F _ {j}; C) - I (F _ {i}; F _ {j}) + I (F _ {i}; F _ {j} | C).\tag{26}
$$

Therefore,

$$
\begin{array}{c} I (F _ {i} F _ {j}; C) \geq I (F _ {i}; C) + I (F _ {j}; C) \\ \longleftrightarrow \\ I (F _ {i}; F _ {j}) \leq I (F _ {i}; F _ {j} | C). \end{array}\tag{27}
$$

With Eq. (23), we finally obtain

$$
\begin{array}{c} I (F _ {i} F _ {j}; C) \geq I (F _ {i}; C) + I (F _ {j}; C) \\ \longleftrightarrow \\ I (F _ {i}; C) \leq I (F _ {i}; C | F _ {j}). \end{array}
$$

The proof is complete.

In Theorem $1 , I ( F _ { i } F _ { j } ; C )$ captures the correlation between the feature group $\{ F _ { i } , F _ { j } \}$ and the class C. From the perspective of the redundancy–complementarity dimension, $I ( F _ { i } F _ { j } ; C ) > I ( F _ { i } ; C ) + I ( F _ { j } ; C )$ reveals that the joint discriminative capability of $\{ F _ { i } , F _ { j } \}$ is enhanced when they are drawn together; this implies complementarity between $F _ { i }$ and $F _ { j } .$ On the contrary, $I ( F _ { i } F _ { j } ; C ) < I ( F _ { i } ; C ) + I ( F _ { j } ; C )$ reveals that the joint discriminative capability of $\{ F _ { i } , F _ { j } \}$ is impaired when they are drawn together; this implies redundancy between $F _ { i }$ and $F _ { j } .$ Theorem 1 provides an alternative perspective to identify complementarity and redundancy: If the appearance of $F _ { i }$ increases the relevance between $F _ { j }$ and the class, $F _ { i }$ and $F _ { j }$ are complementary to each other. Otherwise, redundancy is present and needs to be further analyzed. Thus, we can only compare $I ( F _ { i } ; C )$ and $I ( F _ { i } ; C | F _ { j } )$ (or $I ( F _ { j } ; C )$ and $I ( F _ { j } ; C | F _ { i } ) )$ for redundancy–complementarity analysis rather than compare the joint mutual information and the summation of the individual mutual information.

## 5.2. Dominance identification

This step focuses on identifying the dominant feature from the pair of features. That is, it would label one feature as redundant, which may finally be eliminated. According to Theorem 1, redundancy implies I $( F _ { i } ; C ) > I ( F _ { i } ; C | F _ { j } )$ and $I ( F _ { j } ; C ) > I ( F _ { j } ; C | F _ { i } )$ . Thus, the diference between I $\left( F _ { i } ; C \right)$ and $I ( F _ { i } ; C | F _ { j } )$ (and that between $I ( F _ { j } ; C )$ and $I ( F _ { j } ; C | F _ { i } ) )$ can be applied to measure the magnitude of redundancy. We define the redundancy rate of $F _ { i }$ given $F _ { j }$ as

$$
\Delta (F _ {i} | F _ {j}) = \frac {I (F _ {i} ; C) - I (F _ {i} ; C | F _ {j})}{I (F _ {i} ; C)},\tag{28}
$$

then, the dominant feature can be identified by comparing $\Delta ( F _ { i } | F _ { j } )$ and $\Delta ( F _ { j } | F _ { i } )$ since $\Delta ( \cdot )$ could measure the extent to which the discriminative capability of a feature can be substituted by that of another. To conduct this more eficiently, we propose the following theorem:

Theorem 2. For $\forall { \cal F } _ { i } , { \cal F } _ { j }$ ∈F $( F _ { i } { \neq } F _ { j } )$ and the class ${ \cal C } , ~ i f ~ I ( F _ { i } F _ { j } ; C ) ~ \geq ~ I$ $( F _ { i } ; C ) + I ( F _ { j } ; C ) ,$ , we obtain

$$
\frac {\Delta (F _ {i} | F _ {j})}{\Delta (F _ {j} | F _ {i})} = \frac {I (F _ {j} ; C)}{I (F _ {i} ; C)}.
$$

The proof of Theorem 2 is omitted as it is straightforward with Eq. (23). Theorem 2 reveals that the redundancy rate of a feature is proportional to its class-relevance. It provides a surprisingly eficient means to identify dominance, i.e., a straightforward comparison of I $( F _ { i } ; C )$ and $I ( F _ { j } ; C )$ enables the determination of the feature that is potentially redundant and should be further analyzed. We note here that Theorem 2 is also the theoretical base for the methods such as FCBF [15] and Fast-FCBF [31], which apply the approximate Markov blanket to identify redundancy.

## 5.3. Redundancy elimination

The feature remaining after the above two steps is a redundant candidate, which needs to be tested for significant redundancy. However, it is challenging to set a pervasive statistical test for redundancy analysis because the data distribution and the sample size vary depending on the conditions. Conventionally, the thresholding approach is widely applied to address this issue because of convenience. In this work, we apply a top-down approach for more reliable redundancy analysis. That $\mathbf { i } s ,$ we first sort the features selected by NOMP in the descending order of their class-relevance; then, we compare the pairwise correlations between features within a top-down order: According to Theorem 2, the features sorted in the top (i.e., with higher values of I(F;C)) are dominant compared with their followers. From the reliability perspective, the features sorted below are more likely to be significantly redundant. Therefore, we only need to test the redundancy for the features $( F _ { j } )$ , which are sorted below the current one (F ) and simultaneously satisfy the non-complementarity rule:

![](/api/attachments/RKDG4YPS/fulltext/images/d82749384c595c6184ebea29248f49929dc552854333edbf158618df738d764c.jpg)  
Fig. 3. A toy example of one iteration of the proposed method.

$$
I (F _ {j}; C) > I (F _ {j}; C | F _ {i}).\tag{29}
$$

Then, if the correlation between $F _ { i }$ and $F _ { j }$ is larger than the class-relevance of the non-dominant feature $F _ { i } , F _ { j }$ is identified as redundant and finally removed from the feature subset. Thus, we apply the following redundancy rule

$$
I (F _ {j}; C) <   I (F _ {i}; F _ {j})\tag{30}
$$

to finally indicate that $F _ { j }$ is significantly redundant in the proposed method.

## 6. Proposed method

The proposed method given in Algorithm 3, called feature selection with sparse representation and dependence analysis (SRDA), dynamically combines NOMP and dependence analysis. We also provide a toy example of an iteration of the proposed method on a dataset with 16 features, which is shown in Fig. 3.

In order to further utilize the high capability of MI in identifying relevant features, we marginally modify the NOMP shown in Algorithm 2 by using

$$
\widetilde {F} = \arg \max _ {F \in \mathbf {F} \setminus \mathbf {S}} I (F; C | \mathbf {S})\tag{31}
$$

to determine the initial feature for NOMP. However, the estimation of the joint distribution of the selected features in S is impeded by sample insuficiency. Thus, we apply the following approximation of Eq. (31):

$$
\tilde {F} = \arg \max _ {F \in \mathbf {F} \setminus \mathbf {S}} \{\min _ {F ^ {\prime} \in \mathbf {S}} I (F; C | F ^ {\prime}) \}\tag{32}
$$

to determine the initial feature. Herein, min ${ } _ { F ^ { \prime } \in \mathbf { S } } I ( F ; C | F ^ { \prime } )$ is the pairwise pessimistic approximation of I(F;C|S) [48].

Algorithm 3. Feature selection with Sparse Representation and Dependence Analysis (SRDA)

```txt
Input: F /*feature set*/, C /*class*/, δ /*expected # features to be selected*/
Output: S /*selected feature subset*/, Ω /*Indices of selected features in F*/
1 Initialize: Calculate Γφ and Λφ, r0 ← C, S ← ∅, Ω0 ← ∅, i ← 1 /*iteration counter for NOMP*/
2 repeat
3    SNOMP ← ∅, Ω0 ← ∅, i ← 1
4    Ω1 ← Ω0 ∪ {j|Fj = arg maxF∈F\S {minF'∈S I(F;C|F')}}
5    repeat
6    Find the feature F̃j satisfying the maximization problem:
7    maxF∈F{Γφ(j) - Λφ(j, Ωi) · (Λφ(Ωi, Ωi) + λ · I)-1 · ΓφT(Ωi)}
8    Ωi+1 = Ωi ∪ {j}
9    Calculate ||φ(ri)||2 = √κ(ri,ri) in terms of Eq.(15)
10    i ← i + 1
11    until |φ(ri)||2 / ||φ(ri-1)||2 ≥ 0.95;
12    S ← S ∪ FΩi+1
13    /* Dependence analysis step */
14    Sorder ← Sort(S,'descend')    /* sort the features in S in the descending order of I(Fi;C)**/
15    Fi ← getFirstElement(Sorder)
16    repeat
17    Fj ← getNextElement(Sorder,Fi)
18    repeat
19    if I(Fj;C) > I(Fj;C|Fi) and I(Fj;C) < I(Fi;Fj) then
20    Remove Fj from Sorder
21    end
22    Fj ← getNextElement(Sorder,Fj)
23    until Fj == NULL;
24    Fi ← getNextElement(Sorder,Fi)
25    until Fi == NULL;
26    S ← Sorder
27 until |S| ≥ δ;
28 return S
```

The next section describes the extensive classification experiments conducted to empirically illustrate the efectiveness of the proposed method compared with the representative feature selection methods.

Table 1  
Description of datasets.

<table><tr><td>#</td><td>Name</td><td># samples</td><td># features</td><td># classes</td></tr><tr><td>1</td><td>isolet5</td><td>1559</td><td>617</td><td>26</td></tr><tr><td>2</td><td>DNA</td><td>3186</td><td>180</td><td>3</td></tr><tr><td>3</td><td>mfeat-factors</td><td>2000</td><td>216</td><td>10</td></tr><tr><td>4</td><td>mfeat-pixel</td><td>2000</td><td>240</td><td>10</td></tr><tr><td>5</td><td>mfeat-zernike</td><td>2000</td><td>47</td><td>10</td></tr><tr><td>6</td><td>optdigits</td><td>5620</td><td>63</td><td>10</td></tr><tr><td>7</td><td>spambase</td><td>4601</td><td>57</td><td>2</td></tr><tr><td>8</td><td>musk2</td><td>6598</td><td>166</td><td>2</td></tr><tr><td>9</td><td>14_Tumors</td><td>308</td><td>15,009</td><td>26</td></tr></table>

## 7. Experiments and discussion

Four representative information theoretic feature selection methods, namely, MIM [14], mRMR [17], FOU [10], and JMI [29], and an $\ell _ { 2 , p } { \mathrm { - n o r m } }$ regularized discriminative feature selection method [DFS, 26] are used to compare with the proposed SRDA. Three representative classifiers, namely, k-nearest neighbor [kNN, 49], naïve Bayes classifier [NBC, 50], and random forest [51], are selected to generate the classification error rate on the datasets represented with the selected features, because of their proven efectiveness in real-world applications.

Weka [Waikato environment for knowledge analysis, 50] is selected as the classification platform. Because MIM has already been integrated in Weka, we directly use it in Weka to generate datasets with its selected features prior to classification. mRMR, FOU, and JMI are implemented in Java and with Weka interfaces. DFS and the proposed SRDA are implemented in Matlab. Following Liang and Hu [33] and Wang et al. [34], we set k = 1 for kNN. For random forest, we use the default parameter setting in Weka. For DFS, we set $p = 1$ as suggested by Tao et al. [26].

![](/api/attachments/RKDG4YPS/fulltext/images/b6037c3522d12cbc4db1663bf5f52f32d9ffb9a20441431257678efc25e3cd01.jpg)  
(a)

![](/api/attachments/RKDG4YPS/fulltext/images/42f8d712bc6b99530a31b60660720e0567c068fe312027c223437e9ee645d7da.jpg)  
(b)

![](/api/attachments/RKDG4YPS/fulltext/images/b5a741d386b75286d2a54552d69152220815e400508f121268953e24693d6975.jpg)  
(c)

![](/api/attachments/RKDG4YPS/fulltext/images/4e55744da67c563d2f143f38bf09585b305342646fd51a59dd8dd6b059421d8a.jpg)  
(d)

![](/api/attachments/RKDG4YPS/fulltext/images/2473c67cd37e61f303429a060d71d169a2379a49a8b602e6a513c4e6bafe4d9a.jpg)  
(e)

![](/api/attachments/RKDG4YPS/fulltext/images/28347b2e96d65426f602cdba1d615ea9cde8f8967f3270edeb49eb9099ee6329.jpg)  
(f)

![](/api/attachments/RKDG4YPS/fulltext/images/43604e8f4dc948e660170c60d5630f5f4532bbe7a1e2e29ec77a64b3a3304d19.jpg)  
(g)

![](/api/attachments/RKDG4YPS/fulltext/images/b2f649737582da60adc3646c1500c951360d65e26a4a4c01b16105548ecdb58c.jpg)  
(h)

![](/api/attachments/RKDG4YPS/fulltext/images/99546e9b0663914c96902f6d12732c5e76efcec77cc60aebc22a5712c7e9a8f2.jpg)  
(i)  
Fig. 4. Accuracy comparison using kNN with diferent number of selected features on the selected datasets.

## 7.1. Datasets

Nine frequently-used datasets from diferent fields (such as industrial engineering, bioinformatics, and image processing) are applied in the experiments, wherein eight of them are randomly selected from the UCI Machine Learning Repository<sup>1</sup>. Since we want to verify the eficiency and efectiveness of the proposed method on high-dimensional data, we also select a well-known microarray dataset, 14\_Tumors [52], as the benchmark dataset. General information about these datasets is summarized in Table 1.

Isolet5 is a dataset for the prediction task of speech recognition. It contains 617 voice-related features and a total of 1559 samples. The class labels are the 26 letters in the alphabet. DNA dataset consisting of 3186 samples and 180 indicator binary features is created for re cognition the boundaries between exons and introns given a sequence of DNA. The dataset applied in our experiments is slightly diferent from the original one in the UCI Machine Learning Repository (the original 60 symbolic attributes were changed into 180 binary attribute and four samples with ambiguities were removed)<sup>2</sup>. Multiple Features (mfeat) is a set of datasets that consist of features of handwritten numerals extracted from a collection of Dutch utility maps. In our experiments, three kinds of them, namely, mfeat-factors, mfeat-pixel, and mfeat-zernike, are selected as the benchmark datasets. Optical Recognition of Handwritten Digits (optdigits) dataset contains 5620 samples and 64 integer features in the range of [0,16]. The first feature of this dataset is removed in our experiments for its value never changes. Spambase contains a total of 4601 spam and non-spam email samples and 57 features indicating the length of sequences of consecutive capital letters and whether a particular word or character frequently occurs in the email. Musk2 dataset describes a set of 102 molecules of which 39 are judged by human experts to be musks and the remaining 63 molecules are judged to be non-musks. It contains 6598 samples and 166 features. 14\_Tumors consists of 308 samples with a total of 26 classes including 14 various human tumor types (leukemia, prostate, lung, colorectal, lymphoma, bladder, melanoma, uterus, breast, renal, pancreas, ovary, mesothelioma, and CNS) and 12 normal tissues (breast, prostate, lung, colon, germinal center, bladder, uterus, peripheral blood, kidney, pancreas, ovary, and brain). Each sample has 15,009 genes (features).

![](/api/attachments/RKDG4YPS/fulltext/images/6c2c4553c658073703995a752fc2e30d0facb3c485f39fc2f33e1a67df2f777d.jpg)  
(a)

![](/api/attachments/RKDG4YPS/fulltext/images/cbb37213ed9c1e19b5ad93366f4602e29a3ae60336ee8235ccaccb47bcc79ae1.jpg)  
(b)

![](/api/attachments/RKDG4YPS/fulltext/images/89b17ea92ef8536ff947e1d7ca089780e5fdc23db5a469c1cb744b95ea8876a9.jpg)  
(c)

![](/api/attachments/RKDG4YPS/fulltext/images/1af82423b03c6cf7322464374a24bd549724e40c289c84a432d2aad8cb3bde9f.jpg)  
(d)

![](/api/attachments/RKDG4YPS/fulltext/images/bc2c812ac2b19796586eb18f6c6c7709ff41409e97140d0acfffca87fa8edb92.jpg)  
(e)

![](/api/attachments/RKDG4YPS/fulltext/images/86f2ea6870bbd9ab4eb35c0d246114ff840960ec42e0cfcfed9d7008ef1fd5f9.jpg)  
(f)

![](/api/attachments/RKDG4YPS/fulltext/images/40f6253df34219696c18bdcd41b0793915611ab9b4806446ba79cfd3b3f4cf3d.jpg)  
(g)

![](/api/attachments/RKDG4YPS/fulltext/images/43309d9e87fdb6c821e7a0b94d433cf06629eb06d6e0e24866a4c031f06639fd.jpg)  
(h)

![](/api/attachments/RKDG4YPS/fulltext/images/53f194b09596d320f7ae92dbb727ec5b3a89b4310cbda180bcea50fafc2efeec.jpg)  
(i)  
Fig. 5. Accuracy comparison using NBC with diferent numbers of selected features on the selected datasets.

## 7.2. Experimental settings

First. we illustrate the classification results of the three classifiers on the top δ selected features for each feature selection method; here, δ is the desired number of selected features, specified as $\delta = [ 1 , 2 , . . . , t ]$ . The maximal acceptable size t is set as min {100, | |}F . The 5-fold crossvalidation is performed to obtain the average classification error and the corresponding standard deviation. That is, each dataset is randomly partitioned into five complementary folds, wherein each fold as well as the other four folds will be represented using the features selected by feature selection methods working on the other four folds. The current fold (test set) will be then applied to validate the classification models trained on the other four folds (training set). After five rounds of the procedure mentioned above, the average classification result will be finally obtained and reported.

To further verify the superiority of the proposed method, we sta tistically compare the classification results on the datasets with an identical number of selected features for all the compared methods. Specifically, the top 20 and 40 features, respectively, are applied to obtain the classification results. Because suficient samples are required for the statistical test to obtain reliable results, the 5-fold cross-vali dation is repeated 20 times with diferent random seeds to generate 100 classification error samples. The average of these samples is reported, and the Wilcoxon rank-sum test with a significance level of 0.05 is applied to determine the statistical significance of the diferences of such results.

## 7.3. Experimental results and discussion

Figs. 4 (a)–(i) and 5(a)–(i) show the error rates and the corresponding standard deviations of kNN and NBC, respectively, w.r.t. the number of selected features on the nine datasets via 5-fold cross-validation.

According to the results shown in Fig. 4 (a)–(i), the superiority of SRDA can be verified in the majority of cases, particularly, on six datasets: isolet5 $( \mathrm { F i g . ~ 4 ~ ( a ) } )$ , mfeat-factors (Fig. 4 (c)), mfeat-pixel (Fig. 4 (d)), mfeat-zernike (Fig. 4 (e)), musk2 (Fig. 4 (h)), and 14\_Tumors (Fig. 4 (i)). It should be noted that although DFS is claimed by Tao et al. [26] to be capable of addressing redundancy, our experimental results demonstrate that DFS performs marginally inferiorly on the whole, among the selected methods. This is possibly because DFS does not suficiently consider redundancy and complementarity. Moreover, DFS is computationally intractable on 14\_Tumors, which contains 15,009 features. This empirically implies the limitations of the feature selection methods based on linear discriminative analysis.

![](/api/attachments/RKDG4YPS/fulltext/images/891a3f438aafb29b4ea2167004605c72e3666bd6c422eb052d5ddb6d50d196f1.jpg)  
(a)

![](/api/attachments/RKDG4YPS/fulltext/images/71a760fc7774e5df83305e0826896d3ebed9a7bc8978b4d5a5ef8382bda9c03a.jpg)  
(b)

![](/api/attachments/RKDG4YPS/fulltext/images/9ec9b23730117f881e2c9466203f49764b9bb0c7a5145261f902af18f32a8354.jpg)  
(c)

![](/api/attachments/RKDG4YPS/fulltext/images/675269a473451a51fdcd85843ccbe1f5f2f158373962a4113c3085991154b800.jpg)  
(d)

![](/api/attachments/RKDG4YPS/fulltext/images/5435d5b085c0176682f109f8b04fe598329d4cc21c60e9b0b382e360b1dd0302.jpg)

![](/api/attachments/RKDG4YPS/fulltext/images/0fc720b8be174c16fdd7d009f8b2fb6dd72b728c5468f44dfc41134ceb713fed.jpg)  
(f)

(e)  
![](/api/attachments/RKDG4YPS/fulltext/images/2d66ad34c8877768d331497c0a1027ae13ab1ce22979839f8be8a2836fe4c1c2.jpg)  
(g)

![](/api/attachments/RKDG4YPS/fulltext/images/bcef1104d76a310d6a453d788f3261f92a0acaa9536f350cb122e4f444310a08.jpg)  
(h)

![](/api/attachments/RKDG4YPS/fulltext/images/67306a23089f4fbbfd31a24696deaf1b52e100842f0edcb027aa3c5403633def.jpg)  
(i)  
Fig. 6. Accuracy comparison using random forest with diferent numbers of selected features on the selected datasets.

However, for the rest datasets (i.e., DNA, optdigits, and spambase), all the selected methods except DFS (which performs inferiorly) exhibit similar performance, indicating the similar utilities of their selected features in data representation. It is also observed that the proposed SRDA performs relatively inferiorly at the top of the selected features $( \boldsymbol { \mathrm { e . g . } }$ , top 1–10 features of isolet5 and mfeat-pixel and top 1–30 features of mfeat-factors and 14\_Tumors, respectively); this implies that redundancy is not fully eliminated among the top selected features. This phenomenon could be owing to the fact that SRDA conducts dependence analysis only locally $( \mathrm { i . e . , }$ only considers redundancy and com plementarity within the feature group generated by NOMP). On the whole, the proposed SRDA achieves no significantly inferior results on any of the selected datasets. The comparison results of NBC and random forest shown in Figs. 5 (a)–6(i) are similar to those of kNN, which also verify the efectiveness of SRDA.

Tables 2–4 present the classification error rate of kNN, NBC, and random forest over the 20 × 5-fold cross-validation on the top 20 and 40 selected features, respectively. For each dataset, the Wilcoxon test is conducted to evaluate the statistical significance of the diference between two sequences of the classification results, i.e., the sequence of the 20 × 5-fold cross-validation results corresponding to SRDA and that corresponding to any other feature selection method. The Err column records the average error rate of the $2 0 \times 5 – \mathrm { f o l d }$ cross-validation. The p-val column records the p-value associated with the Wilcoxon test, where a p-value less than 0.05 indicates statistical significance. The notations •/∘ are used to illustrate that the average error rate corresponding to the current feature selection method is significantly lower/ higher than that of SRDA. The bold value in each row represents the best classification result (i.e., the lowest error rate). The average error rate for all the datasets is reported in the last two rows. In addition, Table 5 reports the numbers of the significant losses/significant wins/ ∘ denotes statistical degradation at significance level of 0.05, and • denotes statistical improvement at significance level of 0.05. \* Calculated only on eight datasets.

∘ denotes statistical degradation at significance level of 0.05, and • denotes statistical improvement at significance level of 0.05. \* Calculated only on eight datasets.

Table 2  
Results of classification error rate of kNN and Wilcoxon test for top 20 and 40 selected features.

<table><tr><td>#</td><td>#</td><td>SRDA</td><td colspan="2">MIM</td><td colspan="2">mRMR</td><td colspan="2">FOU</td><td colspan="2">JMI</td><td colspan="2">DFS</td></tr><tr><td>datasets</td><td>features</td><td>Err</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td></tr><tr><td rowspan="2">1</td><td>20</td><td>34.63</td><td>56.12</td><td>0.000°</td><td>39.35</td><td>0.000°</td><td>40.14</td><td>0.000°</td><td>43.04</td><td>0.000°</td><td>56.74</td><td>0.000°</td></tr><tr><td>40</td><td>29.20</td><td>44.90</td><td>0.000°</td><td>32.55</td><td>0.000°</td><td>33.39</td><td>0.000°</td><td>38.08</td><td>0.000°</td><td>37.62</td><td>0.000°</td></tr><tr><td rowspan="2">2</td><td>20</td><td>9.30</td><td>9.62</td><td>0.123</td><td>9.42</td><td>0.658</td><td>10.31</td><td>0.000°</td><td>9.72</td><td>0.012°</td><td>19.10</td><td>0.000°</td></tr><tr><td>40</td><td>14.68</td><td>14.77</td><td>0.581</td><td>14.93</td><td>0.158</td><td>17.01</td><td>0.000°</td><td>14.58</td><td>0.808</td><td>19.44</td><td>0.000°</td></tr><tr><td rowspan="2">3</td><td>20</td><td>8.61</td><td>14.22</td><td>0.000°</td><td>9.70</td><td>0.000°</td><td>9.89</td><td>0.000°</td><td>11.66</td><td>0.000°</td><td>12.52</td><td>0.000°</td></tr><tr><td>40</td><td>6.25</td><td>12.15</td><td>0.000°</td><td>7.45</td><td>0.000°</td><td>7.22</td><td>0.000°</td><td>9.37</td><td>0.000°</td><td>7.31</td><td>0.000°</td></tr><tr><td rowspan="2">4</td><td>20</td><td>12.06</td><td>35.39</td><td>0.000°</td><td>15.09</td><td>0.000°</td><td>26.78</td><td>0.000°</td><td>19.61</td><td>0.000°</td><td>29.50</td><td>0.000°</td></tr><tr><td>40</td><td>8.75</td><td>20.02</td><td>0.000°</td><td>11.35</td><td>0.000°</td><td>17.97</td><td>0.000°</td><td>12.62</td><td>0.000°</td><td>19.66</td><td>0.000°</td></tr><tr><td rowspan="2">5</td><td>20</td><td>28.74</td><td>35.88</td><td>0.000°</td><td>31.23</td><td>0.000°</td><td>34.48</td><td>0.000°</td><td>34.80</td><td>0.000°</td><td>31.13</td><td>0.000°</td></tr><tr><td>40</td><td>27.40</td><td>28.59</td><td>0.000°</td><td>28.69</td><td>0.000°</td><td>29.33</td><td>0.000°</td><td>28.61</td><td>0.000°</td><td>28.05</td><td>0.000°</td></tr><tr><td rowspan="2">6</td><td>20</td><td>9.04</td><td>10.11</td><td>0.000°</td><td>8.95</td><td>0.532</td><td>10.62</td><td>0.000°</td><td>9.93</td><td>0.000°</td><td>13.08</td><td>0.000°</td></tr><tr><td>40</td><td>5.78</td><td>6.11</td><td>0.000°</td><td>6.11</td><td>0.001°</td><td>6.32</td><td>0.000°</td><td>6.11</td><td>0.000°</td><td>6.00</td><td>0.010°</td></tr><tr><td rowspan="2">7</td><td>20</td><td>6.96</td><td>7.89</td><td>0.000°</td><td>7.45</td><td>0.000°</td><td>9.53</td><td>0.000°</td><td>7.56</td><td>0.000°</td><td>9.95</td><td>0.000°</td></tr><tr><td>40</td><td>7.01</td><td>6.96</td><td>0.861</td><td>7.18</td><td>0.048°</td><td>8.96</td><td>0.000°</td><td>7.01</td><td>0.740</td><td>8.28</td><td>0.000°</td></tr><tr><td rowspan="2">8</td><td>20</td><td>4.08</td><td>4.32</td><td>0.001°</td><td>4.98</td><td>0.000°</td><td>4.95</td><td>0.000°</td><td>4.36</td><td>0.000°</td><td>5.12</td><td>0.000°</td></tr><tr><td>40</td><td>4.05</td><td>4.22</td><td>0.014°</td><td>5.09</td><td>0.000°</td><td>5.15</td><td>0.000°</td><td>4.45</td><td>0.000°</td><td>5.45</td><td>0.000°</td></tr><tr><td rowspan="2">9</td><td>20</td><td>49.68</td><td>59.50</td><td>0.000°</td><td>53.87</td><td>0.005°</td><td>45.10</td><td>0.000°</td><td>53.53</td><td>0.008°</td><td>N/A</td><td>N/A°</td></tr><tr><td>40</td><td>37.34</td><td>51.65</td><td>0.000°</td><td>45.00</td><td>0.000°</td><td>38.13</td><td>0.442</td><td>46.02</td><td>0.000°</td><td>N/A</td><td>N/A°</td></tr><tr><td rowspan="2">Avg.</td><td>20</td><td>18.12</td><td>25.89</td><td></td><td>20.00</td><td></td><td>21.31</td><td></td><td>21.58</td><td></td><td>22.14*</td><td></td></tr><tr><td>40</td><td>15.61</td><td>21.04</td><td></td><td>17.59</td><td></td><td>18.16</td><td></td><td>18.54</td><td></td><td>16.48*</td><td></td></tr></table>

Table 3  
Results of classification error rate of NBC and Wilcoxon test for top 20 and 40 selected features.

<table><tr><td>#</td><td>#</td><td>SRDA</td><td colspan="2">MIM</td><td colspan="2">mRMR</td><td colspan="2">FOU</td><td colspan="2">JMI</td><td colspan="2">DFS</td></tr><tr><td>datasets</td><td>features</td><td>Err</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td></tr><tr><td rowspan="2">1</td><td>20</td><td>27.75</td><td>58.73</td><td>0.000°</td><td>34.31</td><td>0.000°</td><td>26.11</td><td>0.000°</td><td>39.33</td><td>0.000°</td><td>41.46</td><td>0.000°</td></tr><tr><td>40</td><td>23.22</td><td>46.52</td><td>0.000°</td><td>28.28</td><td>0.000°</td><td>20.15</td><td>0.000°</td><td>34.55</td><td>0.000°</td><td>22.98</td><td>0.723</td></tr><tr><td rowspan="2">2</td><td>20</td><td>5.54</td><td>6.80</td><td>0.000°</td><td>6.79</td><td>0.000°</td><td>4.96</td><td>0.000°</td><td>6.72</td><td>0.000°</td><td>16.48</td><td>0.000°</td></tr><tr><td>40</td><td>4.20</td><td>5.27</td><td>0.000°</td><td>5.19</td><td>0.000°</td><td>4.84</td><td>0.000°</td><td>5.26</td><td>0.000°</td><td>8.75</td><td>0.000°</td></tr><tr><td rowspan="2">3</td><td>20</td><td>8.02</td><td>13.48</td><td>0.000°</td><td>8.10</td><td>0.485</td><td>9.56</td><td>0.000°</td><td>10.12</td><td>0.000°</td><td>10.75</td><td>0.000°</td></tr><tr><td>40</td><td>7.06</td><td>12.28</td><td>0.000°</td><td>6.77</td><td>0.098</td><td>8.35</td><td>0.000°</td><td>9.27</td><td>0.000°</td><td>7.18</td><td>0.899</td></tr><tr><td rowspan="2">4</td><td>20</td><td>13.19</td><td>36.88</td><td>0.000°</td><td>18.38</td><td>0.000°</td><td>29.21</td><td>0.000°</td><td>21.19</td><td>0.000°</td><td>26.12</td><td>0.000°</td></tr><tr><td>40</td><td>11.55</td><td>22.44</td><td>0.000°</td><td>14.11</td><td>0.000°</td><td>19.44</td><td>0.000°</td><td>15.40</td><td>0.000°</td><td>18.01</td><td>0.000°</td></tr><tr><td rowspan="2">5</td><td>20</td><td>25.75</td><td>34.07</td><td>0.000°</td><td>29.95</td><td>0.000°</td><td>30.89</td><td>0.000°</td><td>33.45</td><td>0.000°</td><td>28.21</td><td>0.000°</td></tr><tr><td>40</td><td>25.71</td><td>27.00</td><td>0.000°</td><td>27.05</td><td>0.000°</td><td>27.33</td><td>0.000°</td><td>27.07</td><td>0.000°</td><td>26.21</td><td>0.111</td></tr><tr><td rowspan="2">6</td><td>20</td><td>9.01</td><td>11.11</td><td>0.000°</td><td>9.25</td><td>0.029°</td><td>11.43</td><td>0.000°</td><td>10.80</td><td>0.000°</td><td>12.10</td><td>0.000°</td></tr><tr><td>40</td><td>7.74</td><td>7.83</td><td>0.438</td><td>7.75</td><td>0.961</td><td>8.04</td><td>0.011°</td><td>7.78</td><td>0.737</td><td>8.28</td><td>0.000°</td></tr><tr><td rowspan="2">7</td><td>20</td><td>9.35</td><td>10.08</td><td>0.000°</td><td>8.76</td><td>0.000°</td><td>10.76</td><td>0.000°</td><td>9.42</td><td>0.842</td><td>10.98</td><td>0.000°</td></tr><tr><td>40</td><td>9.79</td><td>10.26</td><td>0.001°</td><td>9.16</td><td>0.000°</td><td>10.89</td><td>0.000°</td><td>10.06</td><td>0.033°</td><td>10.41</td><td>0.000°</td></tr><tr><td rowspan="2">8</td><td>20</td><td>7.36</td><td>8.36</td><td>0.000°</td><td>8.20</td><td>0.000°</td><td>11.03</td><td>0.000°</td><td>10.64</td><td>0.000°</td><td>9.90</td><td>0.000°</td></tr><tr><td>40</td><td>7.71</td><td>7.97</td><td>0.004°</td><td>8.73</td><td>0.000°</td><td>10.65</td><td>0.000°</td><td>10.69</td><td>0.000°</td><td>10.18</td><td>0.000°</td></tr><tr><td rowspan="2">9</td><td>20</td><td>43.83</td><td>57.34</td><td>0.000°</td><td>50.42</td><td>0.000°</td><td>44.08</td><td>0.224</td><td>49.92</td><td>0.003°</td><td>N/A</td><td>N/A°</td></tr><tr><td>40</td><td>42.58</td><td>52.05</td><td>0.000°</td><td>45.24</td><td>0.002°</td><td>39.29</td><td>0.000°</td><td>46.97</td><td>0.000°</td><td>N/A</td><td>N/A°</td></tr><tr><td rowspan="2">Avg.</td><td>20</td><td>16.64</td><td>26.32</td><td></td><td>19.35</td><td></td><td>19.78</td><td></td><td>21.29</td><td></td><td>19.50*</td><td></td></tr><tr><td>40</td><td>15.51</td><td>21.29</td><td></td><td>16.92</td><td></td><td>16.55</td><td></td><td>18.56</td><td></td><td>14.00*</td><td></td></tr></table>

ties of the selected methods compared with SRDA.

The results shown in Tables 2–4 illustrate that, SRDA achieves the best classification results in most of the cases. The average error rates for SRDA (18.12 (20 features)/15.61 (40 features) for kNN, 16.64 (20 features)/15.51 (40 features) for NBC, and 15.81 (20 features)/12.92 (40 features) for random forest) are the lowest among all the feature selection methods with the three classifiers. In addition, the results of loss/win/tie shown in Table 5 also verify that SRDA significantly outperforms all the other methods. It can be also seen that MIM performs inferiorly to most of the selected methods especially on high-dimensional data, indicating the importance of feature inner-correlations for classification modeling. FOU, JMI, and mRMR explicitly conduct de pendence analysis, so they perform significantly better than MIM and DFS.

We take an example on spambase dataset using MIM and DFS as the compared methods to further illustrate the characteristics of SRDA for supporting decision-making processes. The top five features selected by MIM and SRDA are “char\_freq\_!” (frequency of “!” in the email), “char\_freq\_\$” (frequency of “\$”), “capital\_run\_length\_longest” (length of longest uninterrupted sequence of capital letters), “word\_freq\_remove” (frequency of “remove”), and “word\_freq\_your” (frequency of “your”). The results are interpretable in decision making processes because these words and items do frequently appear in junk emails like some advertisements for products/websites. However, the sixth selected feature of SRDA is “word\_freq\_free” (frequency of “free”) while that of MIM is “capital\_run\_length\_average” (average length of uninterrupted sequence of capital letters), where the former corresponds to better classification results for all the selected classifiers. From our experience, word “free”

Table 4  
Results of classification error rate of random forest and Wilcoxon test for top 20 and 40 selected features.

<table><tr><td>#</td><td>#</td><td>SRDA</td><td colspan="2">MIM</td><td colspan="2">mRMR</td><td colspan="2">FOU</td><td colspan="2">JMI</td><td colspan="2">DFS</td></tr><tr><td>datasets</td><td>features</td><td>Err</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td><td>Err</td><td>p-val</td></tr><tr><td rowspan="2">1</td><td>20</td><td>28.33</td><td>51.01</td><td>0.000°</td><td>32.21</td><td>0.000°</td><td>29.00</td><td>0.040°</td><td>35.70</td><td>0.000°</td><td>47.79</td><td>0.000°</td></tr><tr><td>40</td><td>22.04</td><td>37.21</td><td>0.000°</td><td>25.19</td><td>0.000°</td><td>22.89</td><td>0.007°</td><td>30.57</td><td>0.000°</td><td>27.74</td><td>0.000°</td></tr><tr><td rowspan="2">2</td><td>20</td><td>5.63</td><td>5.97</td><td>0.004°</td><td>5.80</td><td>0.049°</td><td>5.56</td><td>0.866</td><td>6.03</td><td>0.008°</td><td>14.40</td><td>0.000°</td></tr><tr><td>40</td><td>4.18</td><td>4.64</td><td>0.000°</td><td>4.63</td><td>0.000°</td><td>4.81</td><td>0.000°</td><td>4.63</td><td>0.000°</td><td>7.05</td><td>0.000°</td></tr><tr><td rowspan="2">3</td><td>20</td><td>7.12</td><td>9.86</td><td>0.000°</td><td>7.80</td><td>0.000°</td><td>8.51</td><td>0.000°</td><td>8.74</td><td>0.000°</td><td>10.73</td><td>0.000°</td></tr><tr><td>40</td><td>5.88</td><td>7.76</td><td>0.000°</td><td>5.60</td><td>0.098</td><td>6.92</td><td>0.000°</td><td>6.59</td><td>0.000°</td><td>6.98</td><td>0.826</td></tr><tr><td rowspan="2">4</td><td>20</td><td>11.91</td><td>32.37</td><td>0.000°</td><td>14.63</td><td>0.000°</td><td>18.50</td><td>0.000°</td><td>17.50</td><td>0.000°</td><td>23.18</td><td>0.000°</td></tr><tr><td>40</td><td>8.56</td><td>16.77</td><td>0.000°</td><td>10.39</td><td>0.000°</td><td>11.15</td><td>0.000°</td><td>11.67</td><td>0.000°</td><td>14.57</td><td>0.000°</td></tr><tr><td rowspan="2">5</td><td>20</td><td>27.13</td><td>30.88</td><td>0.000°</td><td>28.19</td><td>0.000°</td><td>28.75</td><td>0.000°</td><td>30.49</td><td>0.000°</td><td>27.35</td><td>0.536</td></tr><tr><td>40</td><td>25.38</td><td>25.45</td><td>0.929</td><td>25.52</td><td>0.623</td><td>26.34</td><td>0.000°</td><td>25.48</td><td>0.656</td><td>25.31</td><td>0.816</td></tr><tr><td rowspan="2">6</td><td>20</td><td>6.09</td><td>6.89</td><td>0.000°</td><td>6.32</td><td>0.000°</td><td>7.72</td><td>0.000°</td><td>6.77</td><td>0.000°</td><td>8.30</td><td>0.000°</td></tr><tr><td>40</td><td>4.63</td><td>4.72</td><td>0.244</td><td>4.62</td><td>0.831</td><td>4.60</td><td>0.638</td><td>4.70</td><td>0.458</td><td>4.72</td><td>0.591</td></tr><tr><td rowspan="2">7</td><td>20</td><td>6.46</td><td>6.83</td><td>0.001°</td><td>6.63</td><td>0.142</td><td>8.86</td><td>0.000°</td><td>6.69</td><td>0.034°</td><td>8.49</td><td>0.000°</td></tr><tr><td>40</td><td>5.60</td><td>5.57</td><td>0.792</td><td>5.99</td><td>0.000°</td><td>7.36</td><td>0.000°</td><td>5.64</td><td>0.406</td><td>6.68</td><td>0.000°</td></tr><tr><td rowspan="2">8</td><td>20</td><td>3.83</td><td>3.97</td><td>0.100</td><td>4.58</td><td>0.000°</td><td>4.58</td><td>0.000°</td><td>4.04</td><td>0.008°</td><td>4.36</td><td>0.000°</td></tr><tr><td>40</td><td>3.34</td><td>3.43</td><td>0.195</td><td>3.47</td><td>0.067</td><td>3.98</td><td>0.000°</td><td>3.70</td><td>0.000°</td><td>3.86</td><td>0.000°</td></tr><tr><td rowspan="2">9</td><td>20</td><td>45.77</td><td>59.82</td><td>0.000°</td><td>52.60</td><td>0.000°</td><td>45.81</td><td>0.866</td><td>53.05</td><td>0.000°</td><td>N/A</td><td>N/A°</td></tr><tr><td>40</td><td>36.69</td><td>51.37</td><td>0.000°</td><td>44.79</td><td>0.000°</td><td>39.11</td><td>0.044°</td><td>46.24</td><td>0.000°</td><td>N/A</td><td>N/A°</td></tr><tr><td rowspan="2">Avg.</td><td>20</td><td>15.81</td><td>23.07</td><td></td><td>17.64</td><td></td><td>17.48</td><td></td><td>18.78</td><td></td><td>18.08*</td><td></td></tr><tr><td>40</td><td>12.92</td><td>17.44</td><td></td><td>14.47</td><td></td><td>14.13</td><td></td><td>15.47</td><td></td><td>12.11*</td><td></td></tr></table>

∘ denotes statistical degradation at significance level of 0.05, and • denotes statistical improvement at significance level of 0.05. \* Calculated only on eight datasets.

Table 5  
Results of loss/win/tie.

<table><tr><td></td><td># features</td><td>MIM</td><td>mRMR</td><td>FOU</td><td>JMI</td><td>DFS</td></tr><tr><td rowspan="2">kNN</td><td>20</td><td>8/0/1</td><td>7/0/2</td><td>8/1/0</td><td>9/0/0</td><td>9/0/0</td></tr><tr><td>40</td><td>7/0/2</td><td>8/0/1</td><td>8/0/1</td><td>7/0/2</td><td>9/0/0</td></tr><tr><td rowspan="2">NBC</td><td>20</td><td>9/0/0</td><td>7/1/1</td><td>6/2/1</td><td>8/0/1</td><td>9/0/0</td></tr><tr><td>40</td><td>8/0/1</td><td>6/1/2</td><td>7/2/0</td><td>8/0/1</td><td>6/0/3</td></tr><tr><td rowspan="2">Random forest</td><td>20</td><td>8/0/1</td><td>8/0/1</td><td>7/0/2</td><td>9/0/0</td><td>8/0/1</td></tr><tr><td>40</td><td>5/0/4</td><td>5/0/4</td><td>8/0/1</td><td>6/0/3</td><td>6/0/3</td></tr></table>

The results are collected according to the p-val of the Wilcoxon test presented in Tables 2 and 4.

![](/api/attachments/RKDG4YPS/fulltext/images/4f289716d59144a0fcfc7873f226105f2638e6c7847d4a5bf242ef2922a07fec.jpg)  
Fig. 7. Execution time for DFS and SRDA on the selected datasets. The results for 14\_Tumors are omitted because DFS is computationally intractable within reasonable time frame on 14\_Tumors.

is more likely to co-occur with dollar sign “\$” and word “your” in junk mails. In addition, “capital\_run\_length\_average” seems redundant when “capital\_run\_length\_longest” has been already selected, although both of them seem relevant to spam detection. This indicates the superiority of SRDA in redundancy and complementarity analysis. As for DFS, the top-ranked features performs significantly inferiorly in spam detection, indicating that redundancy is not fully removed. Worse still, the features selected by DFS, e.g., “char\_freq\_(” (frequency of char “(”) in the top-ranked features, are less interpretable for spam analysis and de tection.

## 7.4. Runtime comparison for DFS and SRDA

In order to show the relative eficiency of SRDA, we compare the runtime of SRDA and DFS on DNA, isolet5, mfeat-factors, mfeat-pixel, mfeat-zernike, musk2, optdigits, and spambase datasets, respectively. The results are given in Fig. 7. For each dataset, we report the runtime of the methods when they select 100 features. Because DFS is computationally intractable on 14\_Tumors within reasonable time frame, we do not show the results of either methods on 14\_Tumors.

As can be seen from Fig. 7, SRDA runs significantly faster than DFS on all the selected datasets, particularly on isolet5 (containing 1559 samples and 617 features), mfeat-factors (containing 2000 samples and 216 features), and mfeat-pixel (containing 2000 samples and 240 features), verifying the eficiency of the proposed method. In addition, the results also show that DFS is much more sensitive to the number of features and requires a significantly longer runtime when the feature size increases. This as well as the computational intractability on 14\_Tumors both imply a dilemma that DFS and similar sparse representation-based feature selection methods will face when dealing with large-scale datasets.

## 8. Conclusions

In this paper, a novel feature selection method is proposed to discriminate the salient features for classification utilizing both sparse representation and information theoretic dependence analysis. Specifically, each iteration of the proposed method first applies a nonlinear sparse representation approach to determine the representative feature cluster and then conducts approximate dependence analysis to eliminate redundancy in such a manner as to obtain the final selected features. This searching strategy can efectively prevent the significant bias caused by pairwise correlation analysis of large-scale feature set because the size of the selected feature cluster from each iteration is generally small owing to the efective sparse representation of features. For dependence analysis, the complementary correlation of features is first examined, and then, dominance analysis is conducted on the features with non-complementarity. Finally, redundancy analysis is conducted on the non-dominant features, which are finally eliminated if the redundancy rule is satisfied. The proposed method not only utilizes the optimization framework of sparse representation to select features, but also conducts dependence analysis to explicitly handle redundancy and complementarity. In addition, explicit redundancy and complementarity analysis can improve interpretability in decision support processes. Extensive classification experiments are conducted for the proposed method and five representative feature selection methods, including four representative information theoretic feature selection methods and an $\ell _ { 2 , p } { \mathrm { - n o r m } }$ regularized discriminative feature selection method. The experimental results on nine popular datasets verify the efectiveness and superiority of the proposed method.

However, our method exhibits certain evident limitations. For example, classes are always discrete whereas features are sometimes continuous, and we do not consider an efective approach toward measuring the correlation among diferent types of variables. Another limitation of this study is that our method still applies pairwise analysis as an approximation for the analysis of higher-order correlations, although the pairwise analysis of a not-so-large feature cluster can partially prevent estimation bias in the proposed method. Extending our method along such lines would require modeling a complex k-wise analytical framework that attempts to prevent estimation bias caused by the sample insuficiency — an analytically challenging task. Future research could profitably consider these and other extensions such as applying $\ell _ { p } { \ - } { \mathrm { n o r m } }$ $( 0 < p < 1 )$ which exhibits more desirable characteristics in sparse representation. In addition, the idea of this paper can be applied to an unsupervised feature selection scheme: Unsupervised dimensionality reduction approaches like principal components analysis (PCA) and information theoretic dependence analysis can be possibly integrated into a transfer learning method, yielding another promising future research direction.

## Acknowledgments

We would like to thank the associate editor and three anonymous reviewers for their constructive comments and suggestions. This study was supported in part by the National Natural Science Foundation of China under Grants71702066,71802192,61703319, and71772077, in part by China Postdoctoral Science Foundation under Grant2017M612856, in part by Humanity and Social Science Youth foundation of Ministry of Education of China under Grant18YJC630137, and in part by National Key R&D Program of China under Grant2017YFB0102500

## References

[1] Y.O. Serrano-Silva, Y. Villuendas-Rey, C. Yáñez-Márquez, Automatic feature weighting for improving financial Decision Support Systems, Decision Support Systems 107 (2018) 78–87.

[2] S. Maldonado. C. Bravo, J. López, J. Pérez, Integrated framework for profit-based feature selection and SVM classification in credit scoring, Decision Support Systems 104 (2017) 113–121.

[3] L. Zhang, K. Mistry, M. Jiang, S. Chin Neoh, M.A. Hossain, Adaptive facial point detection and emotion recognition for a humanoid robot, Computer Vision and Image Understanding 140 (2015) 93–114. https://doi,org/10.1016/i.cviu,2015.07 007 https://linkinghub.elsevier.com/retrieve/pii/S1077314215001605.

[4] S.C. Neoh, L. Zhang, K. Mistry, M.A. Hossain, C.P. Lim, N. Aslam, P. Kinghorn, Intelligent facial emotion recognition using a lavered encoding cascade optimization model, Applied Soft Computing 34 (2015) 72–93, https://doi.org/10.1016/j. asoc.2015.05.006 https://linkinghub.elsevier.com/retrieve/pii/ S1568494615003063

[5] L. Zhang, K. Mistry, S.C. Neoh, C.P. Lim, Intelligent facial emotion recognition using moth-firefly optimization, Knowledge-Based Systems 111 (2016) 248–267, https: doi.org/10.1016/j.knosys.2016.08.018 https://linkinghub.elsevier.com/retrieve/ pji/S0950705116302799

[6] T.Y. Tan, L. Zhang, S.C. Neoh, C.P. Lim, Intelligent skin cancer detection using enhanced particle swarm optimization, Knowledge-Based Systems 158 (2018) 118–135, https://doi.org/10.1016/j.knosys.2018.05.042 https://linkinghub.

elsevier.com/retrieve/pii/S0950705118302879.

[7] W. Srisukkham, L. Zhang, S.C. Neoh, S. Todryk, C.P. Lim, Intelligent leukaemia diagnosis with bare-bones PSO based feature optimization, Applied Soft Computing 56 (2017) 405–419, https://doi.org/10.1016/j.asoc.2017.03.024 https:/ linkinghub.elsevier.com/retrieve/pii/S1568494617301485

[8] L. Zhang, K. Mistry, C.P. Lim, S.C. Neoh, Feature selection using firefly optimization for classification and regression models, Decision Support Systems 106 (2018) 64–85.

[9] R. Kohavi, G.H. John, Wrappers for feature subset selection, Artificial Intelligence 97 (1997) 273–324.

[10] G. Brown, A. Pocock, M.-J. Zhao, M. Luján, Conditional likelihood maximisation: a unifying framework for information theoretic feature selection, Journal of Machin Learning Research 13 (2012) 27–66

[11] L. Wang, S. Chen, Y. Wang, A unified algorithm for mixed $\ell _ { 2 , p }$ -minimizations and its application in feature selection, Advances in Neural Information Processing Systems 23 (2010) 1813–1821.

[12] I. Rodriguez-Lujan, R. Huerta, C. Elkan, C.S. Cruz, Quadratic programming feature selection. Journal of Machine Learning Research 11 (2010) 1491–1516.

[13] I. Guyon, A. Elisseef, An introduction to variable and features election, Journal of Machine Learning Research 3 (2003) 1157–1182

[14] D.D. Lewis, Feature selection and feature extraction for text categorization, Proceedings of the Workshop on Speech and Natural Language, Association for Computational Linguistics Morristown, NJ, USA, 1992, pp. 212–217.

[15] L. Yu, H. Liu, Eficient feature selection via analysis of relevance and redundancy, Journal of Machine Learning Research 5 (2004) 1205–1224.

[16] P. Meyer, G. Bontempi, On the use of variable complementarity for feature selection in cancer classification, Evolutionary Computation and Machine Learning in Bioinformatics 3907 (2006) 91–102.

[17] H. Peng, F. Long, C. Ding, Feature selection based on mutual information: criteria of max-dependency, max-relevance, and min-redundancy, IEEE Transactions on Pattern Analysis and Machine Intelligence 27 (8) (2005) 1226–1238.

[18] D. Pandit, L. Zhang, S. Chattopadhyay, C.P. Lim, C. Liu, A scattering and repulsive swarm intelligence algorithm for solving global optimization problems, Knowledge-Based Systems 156 (2018) 12–42.

[19] F. Fleuret, Fast binary feature selection with conditional mutual information, Journal of Machine Learning Research 5 (2004) 1531–1555.

[20] Y. Zhang, C. Yang, A. Yang, C. Xiong, X. Zhou, Z. Zhang, Feature selection for classification with class-separability strategy and data envelopment analysis Neurocomputing 166 (2015).172–184 http://www.sciencedirect.com/science/ article/pji/S0925231215004609

[21] X. Chen, F. Xu, Y. Ye, Lower bound theory of nonzero entries in solutions of $\ell _ { 2 } - \ell _ { p }$ minimization. SIAM Journal on Scientific Computing 32 (5) (2010) 2832–2852

[22] B. Efron, T. Hastie, I. Johnstone, R. Tibshirani, Least angle regression, Annals of Statistics 32 (2) (2004) 407–499.

[23] K. Wang, R. He, L. Wang, W. Wang, T. Tan, Joint feature selection and subspace learning for cross-modal retrieval. JEEE Transactions on Pattern Analysis and Machine Intelligence 38 (10) (2016) 2010–2023

[24] B. Peng, L. Wang, Y. Wu, An error bound for ℓ -norm support vector machine coeficients in ultra-high dimension, The Journal of Machine Learning Research 17 (1) (2016) 8279–8304.

[25] M. Liu, D. Zhang, Pairwise constraint-guided sparse learning for feature selection, JEEE Transactions on Cybernetics 46 (1) (2016) 298–310.

[26] H. Tao, C. Hou, F. Nie, Y. Jiao, D. Yi, Efective Discriminative Feature Selection With Nontrivial Solution, JEEE Transactions on Neural Networks & Learning Systems 27 (4) (2016) 796–808

[27] Z. Chen, C. Wu, Y. Zhang, Z. Huang, B. Ran, M. Zhong, N. Lyu, Feature selection with redundancy-complementariness dispersion, Knowledge-Based Systems 89 (2015) 203–217

[28] Y. Zhang, A. Yang, C. Xiong, Z. Zhang, Feature selection using data envelopmen analysis, Knowledge-Based Systems 64 (2014) 70–80

[29] P.E. Mever, C. Schretter, G. Bontempi, Information-theoretic feature selection in microarray data using variable complementarity, JEEE Journal of Selected Topics in Signal Processing 2 (3) (2008) 261–274

[30] L. Zhang, W. Srisukkham, S.C. Neoh, C.P. Lim, D. Pandit, Classifier ensemble re duction using a modified firefly algorithm: an empirical evaluation, Expert Systems with Applications 93 (2018) 395–422 https://linkinghub.elsevier.com/retrieve pji/S0957417417306759

[31] O. Song, J. Ni, G. Wang, A fast clustering-based feature subset selection algorithm for high-dimensional data, IEEE Transactions on Knowledge and Data Engineering 25 (1) (2013) 1–14.

[32] H.H. Yang, J. Moody, Feature selection based on joint mutual information, Proceedings of International ICSC Symposium on Advances in Intelligent Data Analysis, 1999, pp. 22–25.

[33] M. Liang, X. Hu, An eficient semi-supervised representatives feature selection algorithm based on information theory, Pattern Recognition 61 (2017) 511–523.

[34] J. Wang, J.-M. Wei, Z. Yang, S.-Q. Wang, Feature selection by maximizing independent classification information, JEEE Transactions on Knowledge and Data Engineering 29 (4) (2017) 828–841.

[35] F. Nie, H. Huang, X. Cai, C.H. Ding, Eficient and robust feature selection via joint ℓ -norms minimization, Advances in Neural Information Processing Systems 23 (2010) 1813–1821.

[36] H.A.L, Thi, T.P. Dinh. H.M. Le. X.T. Vo. DC approximation approaches for sparse optimization, European Journal of Operational Research 244 (1) (2015) 26–46.

[37] S. Luo, Z. Chen, Sequential lasso cum EBIC for feature selection with ultra-high dimensional feature space. Journal of the American Statistical Association 109 (2014) 1229–1240.

[38] S. Foucart, M.-J. Lai, Sparsest solutions of underdetermined linear systems via ℓ - minimization for 0 < q < 1, Applied and Computational Harmonic Analysis 26 (3) (2009).395–407

[39] Z. Xu, X. Chang, F. Xu, H. Zhang, L regularization: a thresholding representation theory and a fast solver, IEEE Transactions on Neural Networks and Learning Systems 23 (7) (2012) 1013–1027.

[40] Z. Xu, H. Zhang, Y. Wang, X. Chang, Y. Liang, L regularization, Science China 53 (6) (2010) 1159–1169.

[41] X. Chen, D. Ge, Z. Wang, Y. Ye, Complexity of unconstrained ℓ − ℓ minimization, Mathematical Programming 143 (1-2) (2014) 371–383.

[42] M. Masaeli, G. Fung, J.G. Dy, From Transformation-based Dimensionalit Reduction to Feature Selection, Proceedings of the 27th International Conference on International Conference on Machine Learning, ICML’10, Omnipress, USA, 2010, pp. 751–758 http://dl.acm.org/citation.cfm?id=3104322.3104418.

[43] E.J. Candes, T. Tao, Decoding by linear programming, IEEE Transactions on Information Theory 51 (2005) 4203–4215.

[44] T.T. Cai, L. Wang, Orthogonal matching pursuit for sparse signal recovery with noise, IEEE Transactions on Information Theory 57 (7) (2011) 4680–4688.

[45] X. Mo, V. Monga, R. Bala, Z.G. Fan, Adaptive sparse representations for video anomaly detection. JEEE Transactions on Circuits and Systems for Video Technology 24 (4) (2014) 631–645.

[46] X. Sun, Y. Liu, M. Xu, H. Chen, J. Han, K. Wang, Feature selection using dynamic weights for classification, Knowledge-Based Systems 37 (2013) 541–549.

[47] D. Huang, T.W.S. Chow, Efective feature selection scheme using mutual informa tion, Neurocomputing 63 (2005) 325–343

[48] G. Wang, F.H. Lochoysky, O. Yang, Feature selection with conditional mutual information maximin in text categorization. Proceedings of the 19th ACM International Conference on Information and Knowledge Management, CIKM’04, ACM Press, New York, NY, USA. 2004, pp. 342–349.

[49] D. Aha, D. Kibler, Instance-based learning algorithms, Machine Learning 6 (1991) 37–66.

[50] H.I. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques with Java Implementations, Morgan Kaufmann, San Francisco, CA, USA, 2000.

[51] L. Breiman, Random forests, Machine Learning 45 (1) (2001) 5–32.

[52] S. Ramaswamy, P. Tamayo, R. Rifkin, S. Mukherjee, C.H. Yeang, M. Angelo, C. Ladd, M. Reich, E. Latulippe, J.P. Mesirov, T. Poggio, W. Gerald, M. Loda, E.S. Lander, T.R. Golub. Multiclass cancer diagnosis using tumor gene expression signatures, Proceedings of the National Academy of Sciences of the United States of America 98 (26) (2001).15149–15154

Yishi Zhang received a Bachelor Degree in Computer Science from University of Electronic Science and Technology of China in 2009, and a Master Degree and his Ph.D. in Software Architecture and Management Science and Engineering from Huazhong University of Science and Technology in 2011 and 2016, respectively. He is now a research fellow in School of Management at Jinan University, and a postdoc in Joseph M. Katz Graduate School of Business at University of Pittsburgh. His research interests in volve dimensionality reduction, topic modeling, and business intelligence.

Qi Zhang received a Bachelor Degree in Mechanical and Electrical Integration, a Master Degree in Technological Economics and Management, and her Ph.D. in Management Science and Engineering from Wuhan University of Technology, respectively. She is now an associate professor in School of Economics and Management, China University of Geosciences (Wuhan). Her research interests involve business intelligence and big data analytics in the field of digital business.

Zhijun Chen received a Bachelor Degree in Mechanical Engineering and Automation from Wuhan University of Technology in 2009, and a Master Degree and his Ph.D. in Transportation Engineering and Automotive Engineering from Wuhan University of Technology, in 2012 and 2016, respectively. He is now an associate professor in Intelligent Transport Systems Research Center, Wuhan University of Technology. His research interests involve trafic safety, vehicle behavior recognition, machine learning, and big data analytics in intelligent transportation systems.

Jennifer Shang is a Full professor in the area of Business Analytics in Joseph M. Katz Graduate School of Business at University of Pittsburgh. She received her Ph.D. in Operations Management from University of Texas at Austin. She has published in various journals, including Management Science, Information Systems Research, Marketing Science, European Journal of Operational Research, among others. She has won the EMBA Distinguished Teaching Award and several Excellence-in-Teaching Awards from th MBA/EMBA programs at Katz Business School.

Haiying Wei received a Bachelor Degree in Statistics from Renmin University of China in 1986, a Master Degree in Finance from Jinan University in 1997, and her Ph.D. in Management Science and Engineering from Huazhong University of Science and Technology in 2006. At present. she is a professor in School of Management at Jinan University, and serves as an executive member of China Institutions for Higher Learning. Her research interests involve statistical analysis and its application in marketing.
