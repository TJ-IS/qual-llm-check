---
otero_id: 6664
otero_key: "KK6XEVAA"
title: "Three-stage reject inference learning framework for credit scoring using unsupervised transfer learning and three-way decision theory"
authors: "Feng Shen; Xingchao Zhao; Gang Kou"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113366"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Three-stage reject inference learning framework for credit scoring using unsupervised transfer learning and three-way decision theory

![](/api/attachments/KK6XEVAA/fulltext/images/7243988f105d57294ce1e3690c5b83d597e8946bc6890b6513dd9f70363eebf5.jpg)

Feng Shen<sup>a,b,⁎</sup>, Xingchao Zhao<sup>a</sup>, Gang Kou<sup>c,⁎⁎</sup>

<sup>a</sup> School of Finance, Southwestern University of Finance and Economics, Chengdu 611130, PR China

<sup>b</sup> Fintech Innovation Center, Southwestern University of Finance and Economics, Chengdu 611130, PR China

<sup>c</sup> School of Business Administration, Southwestern University of Finance and Economics, Chengdu 611130, PR China

## A R T I C L E I N F O

Keywords: Reject inference Unsupervised transfer learning Three-way decision theory Credit scoring

## A B S T R A C T

There has been significant research into reject inference, with several statistical methods and machine learning techniques having been employed to infer the possible repayment behavior of rejected credit applicants. This study proposes a novel three-stage reject inference learning framework using unsupervised transfer learning and three-way decision theory that integrates: (1) the rejected credit sample selection using three-way decision theory, (2) higher-level representations to transfer learning from both accepted and selected rejected credit samples; and (3) credit scoring using the reconstructed accepted credit samples. This method was found to both perform well for reject inference and handle negative transfer learning problems. The numerical results were validated on Chinese credit data, the results from which demonstrated the superiority of the proposed reject inference method for credit risk management applications.

## 1. Introduction

The 2008 subprime mortgage crisis demonstrated that the loan applicant credit risks needed to be better evaluated and that credit risk management needed to be a key focus for the banking industry. The Basel III Accord recommended that advanced internal credit scoring models be developed to properly manage financial institution credit risks. In this age of big data and Fintech, eficient and accurate credit scoring models are vital for banks and financial institutions because: 1) accurate credit scoring systems manage the measured credit risk based on the probability of default (PD), the loss given default (LGD), and the exposure at default (EAD); and 2) advanced credit scoring models allow for faster loan decisions and better mitigate risks, which reduces costs.

As a core decision support tool. credit scoring is being used extensively in financial institutions to predict borrower repayment behavior and provide accurate credit risk estimations [1]. Over the past decade, many credit scoring models based on statistical methods and machine learning techniques have been developed and optimized (see the review in [2]). As most current credit scoring models are based solely on accepted credit samples, the rejected credit samples, which are greater in number, are excluded because they lack repayment behavior information [3]. This means that as these models waste information resources and have biased parameter estimations (i.e., sample bias), the credit scoring system may not accurately or com pletely reflect the entire sample [4,5].

Reject inference [6,7] refers to a process that infers the possible loan repayment outcomes for rejected samples, with the associated credit scoring model being established based on both the accepted and rejected inferred repayment behavior observations, that is, the credit scoring model is representative of the entire loan applicant pool [8]. As reject inference has been seen to be theoretically necessary for credit scoring, it has been the focus of significant recent research. However, because of the limitations associated with the underlying assumptions and the disappointing performance of previous reject inference methods, this study proposes a three-stage reject inference learning framework based on an unsupervised transfer learning technique and three-way decision theory (3WD) [9]. Therefore, the main contributions of this work are as follows.

First, a novel learning approach for handling reject inference without “inferring” the outcomes of the rejected samples is provided. The proposed method utilizes a special unsupervised transfer learning algorithm that employs self-taught learning (STL) [10] for the “higherlevel” representation learning of the inputs for the accepted/labeled samples. The STL framework superiority in handling the reject inference problem is because: (1) the STL does not assume that the rejected/unlabeled samples share the same generative distribution as the accepted/labeled data [10], which difers significantly from statistical based and semi-supervised learning methods; (2) the STL algorithm, as a special type of unsupervised learning method, does not have to infer the possible labels for the rejected instances; and (3) as STL places significantly fewer restrictions on the type of unlabeled data, the unsupervised learning method is easier to apply than typical semi-su pervised learning or traditional transfer learning.

Second, an efective approach is proposed to address the negative transfer problems [11,12] that commonly occur in transfer learning tasks [13]. Based on Wang et al. [11], to avoid negative transfer problems, 3WD [9] is applied to select the “relevant” rejected samples for the transfer learning. Then, the proposed unsupervised transfer learning framework when trained is explored using diferent rejected sample selection strategies, with the empirical results suggesting that using the 3WD to select the relevant instances could efectively avoid negative transfer in the transfer learning.

Third, the STL approach provides a more general and flexible learning framework for reject inference as it learns the underlying representations for the accepted sample inputs. The learned accepted sample inputs can then be further utilized and classified using supervised classification models, such as individual classifiers and ensemble methods. The STL algorithm is also able to efectively address the massive big data credit scoring information.

The remainder of paper is structured as follows. Section 2 gives a systematic literature review. Section 3 briefly introduces the background to the unsupervised transfer learning method and 3WD. Section 4 formulates the proposed reject inference learning framework. Section 5 details the empirical study: dataset information, hyper-parameter tuning, performance measurements, and the experimental design. The numerical results and analysis are given in Section 6. Section 7 gives a further discussion of the proposed method, and concluding remarks and future research directions are provided in Section 8.

## 2. Literature review

Credit scoring models are essential tools for banks to distinguish high-risk loan applications from low-risk applications and manage the credit limits of existing customers. However, as most credit scoring models have been built based solely on accepted credit applicants, there are often sample selection bias problems. Previous studies have tended to treat these sample selection biases as missing data problems, with the missing mechanisms being further divided into missing at random (MAR) and missing not at random (MNAR) [6]. Consequently, various reject inference techniques have been developed based on the under lying assumptions for these missing mechanisms.

Based on an underlying MAR assumption, Feelders [3] used an expectation-maximization (EM) algorithm to handle the reject inference, which was a substantial improvement over an artificial dataset. However, as argued by Banasik and Crook [6], the underlying MAR assumption for the missing mechanism in Feelders [3] could have been untrue, and the evaluation results achieved by the EM algorithm using the artificial dataset lacked credibility. Sophisticated statistical techniques such as augmentation and exploration have been applied to reject inference in MNAR cases. Even though Crook and Banasik [7,14] empirically explored augmentation and exploration methods for reject inference, there were few notable improvements in their research, with a further study revealing that the augmentation only rarely benefited the credit scoring model [6]. Bücker et al. [15] modified the reweighting reject inference method, the classification results of their method outperformed the original model without reject inference.

Besides these statistical methods, other solutions based on machine learning reject inference techniques have been developed and significant improvements achieved. Under a MAR assumption, Li et al. [4] and Tian et al. [5] employed semi-supervised SVM $( S ^ { 3 } \mathrm { V M } )$ models for reject inference. The $s ^ { 3 } \mathrm { V M }$ model was trained with both labeled/accepted samples and unlabeled/rejected samples to determine the supporting hyperplane, with the results being superior to traditional supervised credit scoring models. More recently, deep generative models have been proposed for credit scoring reject inference. Manci sidor et al. [16] coupled Bayesian methods and Gaussian mixtures in a semi-supervised framework using generative models, with the proposed methods inferring the unknown labels of the rejected samples based on an approximation of the posterior distribution and on an exact enumeration of two possible loan outcomes. When compared to the stateof-the-art credit scoring models, these deep generative models were found to have superior performance.

In general, statistical-based methods such as augmentation and exploration are more often built based on the underlying assumption that rejected samples share the same repayment behavior patterns as the accepted samples. However, as the actual repayment performances for the rejected samples are not accessed or are dificult to obtain, this assumption may be far from reality and cannot be easily theoretically verified. Nonetheless, while semi-supervised learning methods such as the $s ^ { 3 } \mathrm { V M }$ technique typically assume that the rejected sample repayment performances can be inferred using the accepted sample information, this type of label assignment for the rejected samples is not convincing as the decision boundary for the ${ \mathsf { S } } ^ { 3 } { \mathsf { V M } }$ can be misled by inappropriate pseudo label assignments [17,18]. Further, the current application for ${ \mathsf { S } } ^ { 3 } { \mathsf { V M } }$ in reject inference is limited to small-sized data problems, which prevents any big data applications. Lastly, while the deep generative models proposed in [16] were found to be able to handle the missing data problems well for the reject inference, it has been argued that generative methods only benefit classification tasks when the underlying assumptions are consistent with the ground truth of the data distributions; however, the performance of the generative models that incorporate unlabeled data degrades when the underlying assumptions are violated in reality [19].

This research proposes a novel three-stage learning framework for reject inference that uses three-way decision theory for the rejected data selection and unsupervised transfer learning for the higher-level representation learning. The proposed method originally learns the intrinsic structures of the accepted and the selected rejected sample credit variables and places significantly fewer restrictions on the rejected samples to increase the reject inference flexibility. In addition, the proposed method eficiently handles the common negative transfer problems in the transfer learning domain.

## 3. Background

This section briefly introduces the unsupervised transfer learning algorithm and the 3WD formulations.

## 3.1. Unsupervised transfer learning technique via self-taught learning

In this study, to improve the credit scoring performance, a special unsupervised transfer learning technique, the STL [10], was employed to utilize the information in the rejected data. STL places few restric tions on both the prior source and target data distributions, and the “higher-level” representations for the inputs detected by STL require no additional source domain data label information. Therefore, the flexibility of the STL method makes it ideal for handling reject inferences using big credit sample data.

Assume that input $x _ { u }$ and x are vectors for the rejected (unlabeled) and accepted (labeled) credit samples. The STL method uses $x _ { u }$ to detect the inherent elements that comprise the credit sample; for example, it may discover certain strong correlations between the credit variables, and therefore learn that most samples have many latent correlations. From this, it then learns to represent the credit samples in terms of the variable correlations that appear rather than the raw credit variable values, with the credit sample representations from the latent correlations being a higher more abstract representation of the input. When this learned representation is applied to the accepted credit data $x _ { l s }$ a higher-level representation of the accepted credit samples is also attained, making it an easier supervised learning task. The detailed mathematical formulations for the STL method can be found in [10].

## 3.2. Three-way decision theory

In this study, 3WD is utilized for the rejected data selection to avoid negative transfer. As an extension of traditional two-way decision theory, 3WD has an extra delayed determination decision choice because of the incomplete information.

Given a complementary state set Ω, for an object $x \in \Omega ,$ , suppose f(x) is the evaluation function, the value for which is the decision status value for x. In practice, this function can be defined in several ways; for example, as probability functions [9]. Let $( \alpha , \beta )$ denote a pair of thresholds that satisfy $\beta < \alpha .$ . Then, based on Bayesian decision theory risk minimization $[ 9 , 2 0 ]$ , 3WD divides Ω into three disjointed regions: positive (POS), boundary (BND), and negative (NEG): each of which respectively relates to three decisions: acceptance, rejection, and non committed. The three pair-wise regions are defined as follows:

$$
\begin{array}{r l} & {P O S = \{x \in \Omega \mid f (x) \geq \alpha \}} \\ & {B N D = \{x \in \Omega \mid \beta <   f (x) <   \alpha \},} \\ & {N E G = \{x \in \Omega \mid f (x) \leq \beta \}} \end{array}\tag{1}
$$

As shown in Eq. (1), the evaluation function design and the threshold determinations are two key issues that need further investigation. 3WD has been widely applied in many research fields: classification [21], clustering [22], attribute reduction [23], and granular computation [24].

## 4. Methodology

In this study, a three-stage reject inference learning framework is proposed, which requires no prior data distribution assumptions or any additional inference for the rejects. The three main procedures involved in the proposed learning framework are summarized in Fig. 1: rejected data selection with 3WD, “higher-level” learning representations for the accepted samples, and a binary classification with reconstructed features for the credit scoring.

As shown in Fig. 1, given the rejected credit data and the accepted credit data, in the first learning stage, the proposed learning framework measures the similarities between each rejected sample and the ac cepted training subset. Then three-way decision theory is applied to divide the rejected samples into positive, boundary, and negative regions. In the second stage of the proposed framework, the rejected samples in positive region and the accepted training data are combined to train the STL model. Note that the STL method only utilizes the credit data variables, that is, the training data label information is not used; therefore, the STL model is basically an unsupervised learning method. When the base vectors and the activations are derived, the higher-level accepted sample training and test subsets are transformed. Finally, in the third binary classification stage, the supervised learning algorithms are trained using the reconstructed training data features, with the trained classifiers being validated with the test samples.

## 4.1. Rejected data selection using three-way decision theory

As mentioned in Section 3.2, an evaluation function and threshold are required to obtain the disjointed regions divided by the 3WD. The evaluation function is defined as the similarity between each rejected applicant and the accepted dataset, and is an efective method for ensuring that the thresholds are obtained.

## 4.1.1. Evaluation function for resolving the rejected data

Typically, a traditional evaluation function, which is defined as the probability that object x belongs to Ω, is calculated using a supervised learning algorithm. However, as the real rejected data repayment information is unobservable in reject inference problems, it is not appropriate to train a supervised classification model using the accepted data to predict the probability of the rejected samples. Therefore, the similarity between each rejected applicant and the accepted dataset is taken as an evaluation function substitute in the 3WD. Diferent from [5,25], which simply used Euclidean distance to measure the simila rities between credit samples, the Mahalanobis distance (MD [26]) is used to calculate the similarities. First, unlike the Euclidean distance, as the MD attaches importance to the linear correlations between the random variables, the covariance structure of the data distribution is considered. Second, the distance measured using the MD is not afected by any correlation disturbances between the variables. Third, as the MD is scale-invariant, it is particularly flexible in handling credit data. In practice, the credit variable values can difer significantly, with the loan values, for example, being many thousand times greater than the loan interest rate. However, as the MD is invariant under afine variable transformations [27], it has been found to be superior when measuring the similarities between rejected and accepted samples.

Definition 1. As rejected sample data contain k instances $\mathcal { R } = \{ x _ { u } ^ { 1 } , x _ { u } ^ { 2 } , . . . , x _ { u } ^ { k } \} ;$ , where u indicates it is an unlabeled instance, and as an accepted dataset contains m instances $\mathcal { A } = \{ ( \boldsymbol { x } _ { l } ^ { 1 } , \boldsymbol { y } _ { l } ^ { 1 } ) , ( \boldsymbol { x } _ { l } ^ { 2 } , \boldsymbol { y } _ { l } ^ { 2 } ) , . . . , ( \boldsymbol { x } _ { l } ^ { m } , \boldsymbol { y } _ { l } ^ { m } ) \}$ where the l subscript indicates it is a labeled instance, the similarity between each rejected instance and the accepted dataset is calculated as:

$$
D _ {M} (x _ {u} ^ {i}) = \sqrt {(x _ {u} ^ {i} - \mu) ^ {T} S ^ {- 1} (x _ {u} ^ {i} - \mu)}\tag{2}
$$

where $\mu$ and S represent the mean vector and covariance matrix for the accepted data.

Definition 2. Based on Definition 1, the evaluation function for 3WD is further defined as:

$$
f (x _ {u} ^ {i}) = 1 - \frac {D _ {M} (x _ {u} ^ {i}) - \min \{D _ {m} (x _ {u}) \}}{\max \{D _ {m} (x _ {u}) \} - \min \{D _ {m} (x _ {u}) \}}\tag{3}
$$

where $f ( x _ { u } ^ { ~ i } )$ denotes the probability that object ${ x _ { u } } ^ { i }$ belongs to ${ \mathcal { A } } .$ Therefore, evaluation function $f ( x _ { u } ^ { ~ i } )$ is an interval $[ 0 , 1 ] _ { : }$ , where a rejected applicant with a larger $f ( x _ { u } ^ { ~ i } )$ indicates a more relevant relationship with the accepted data.

## 4.1.2. Threshold determination for the rejected sample selection

Another key issue is the determination of the thresholds for α and β under the 3WD. Here, a novel method for determining thresholds α and β is explored, for which the following three definitions regarding transfer learning are proposed.

Definition 3. [11] Assume a source domain data ${ \mathcal R } ,$ a target domain data ${ \mathcal { A } } ,$ and a specific supervised classification model ℏ. The classification score for $\hbar ,$ which is determined using the proposed learning framework, is $\hbar ( \mathcal { R } , \mathcal { A } )$ and similarly, the classification score for ℏ that is achieved solely from the labeled data $\mathcal { A }$ is $\hbar ( \emptyset , { \mathcal { A } } ) .$ Therefore, the transfer learning gap (TLG) is defined as:

$$
T L G (\mathcal {R}) = \hbar (\mathcal {R}, \mathcal {A}) - \hbar (\emptyset , \mathcal {A})\tag{4}
$$

Definition 4. Based on definitions 2 and 3, given a rejected credit dataset with its corresponding evaluation function values set $\{ f ( x _ { u } ^ { \ 1 } ) , f$ $( { x _ { u } } ^ { 2 } ) , . . . , f ( x _ { u } ^ { \ k } ) \}$ and a predefined threshold ${ \mathfrak { a } } ,$ the positive transfer threshold (PTT) is defined as:

$$
\begin{array}{r} P T T (\alpha) = T L G ((\mathcal {R} | f (x _ {u} ^ {i}) \geq \alpha)) \\ = \hbar (\mathcal {S}, \mathcal {A}) - \hbar (\emptyset , \mathcal {A}) \end{array}\tag{5}
$$

where $\mathcal { S }$ denotes the set of selected rejected samples, where each rejected applicant is satisfied with $f ( x _ { u } ^ { \ i } ) \ge \alpha .$

Definition 5. Similarly, the negative transfer threshold (NTT) β is defined as:

![](/api/attachments/KK6XEVAA/fulltext/images/8a7b2ed0ffbe7db790a6992a476e616027a22dde59d7ffb2b2b5c9411e344bdf.jpg)  
Fig. 1. Three-stage reject inference learning framework.

$$
\begin{array}{c} N T T (\beta) = T L G ((\mathcal {R} | f (x _ {u} ^ {i}) \leq \beta)) \\ = \hbar (\mathcal {S} ^ {\prime}, \mathcal {A}) - \hbar (\emptyset , \mathcal {A}) \end{array}\tag{6}
$$

where ${ \mathcal { S } } ^ { \prime }$ denotes the set of selected rejected samples and each rejected applicant is satisfied with $f ( x _ { u } ^ { \ i } ) \leq \beta .$

Based on the above definitions, thresholds $( \beta , \alpha )$ for the 3WD are determined as follows. First, all rejected samples are divided into m groups according to their evaluation function, $f ( x _ { u } ^ { ~ i } )$ , with each group containing an identical number of rejected samples; then, a grid search method is employed to search for the $( \beta , \alpha )$ thresholds that satisfy the following conditions:

$$
\alpha = \operatorname{argmax} \left\{P T T \left(\alpha_ {1}\right), P T T \left(\alpha_ {2}\right), \dots \right\}\tag{7}
$$

$$
\begin{array}{c} \beta = \operatorname{argmin} \{N T T (\beta_ {1}), N T T (\beta_ {2}),... \} \\ s. t. 0 \leq \beta <   \alpha \leq 1 \end{array}\tag{8}
$$

When threshold α with a maximum PTT score and threshold $\beta$ with a minimum NTT score are determined, the rejected dataset is divided into three disjointed regions as shown in Eq. (1). Finally, the rejected samples that belong to positive region are selected and utilized in the second stage of the proposed framework, as detailed in the next section.

4.2. Learning higher-level representations from the accepted and rejected credit samples

In this study, a special unsupervised transfer learning technique, STL, is employed to learn the higher-level representations for the accepted credit samples. However, as theoretically proved by Francesco et al. [28], the unsupervised learning of disentangled representations is fundamentally impossible without there being inductive biases in the models or data.

In this context, STL is modified to construct “higher-level” representations of the input features for the accepted samples. Two learning steps are performed in the proposed learning framework: in the first step, a sparse coding algorithm is applied to learn the “higherlevel” basis vectors {b} and activations {α}, and in the second step, the features for the accepted samples are reconstructed with the learned basis vectors and activations. The basic procedures are as follows.

Given an accepted credit dataset of m instances $\{ ( \boldsymbol { x _ { l } } ^ { 1 } , \boldsymbol { y _ { l } } ^ { 1 } ) , ( \boldsymbol { x _ { l } } ^ { 2 } , \boldsymbol { y _ { l } } ^ { 2 } ) .$ $\quad . . . , ( x _ { l } ^ { m } , y _ { l } ^ { m } ) \}$ , each $x _ { l } ^ { i } \in \mathcal { R } ^ { n }$ is the feature vector of an accepted credit instance i with $y _ { l } ^ { i }$ representing the corresponding loan status. For the credit scoring problem, one class is discriminated from the background data, $y _ { l } ^ { i } \in \{ 0 , 1 \}$ , and a set of k unlabeled examples is given,

$$
x _ {u} ^ {1}, x _ {u} ^ {2}, \dots , x _ {u} ^ {k} \in \mathscr {R} ^ {n}.
$$

Both the accepted and selected rejected samples are included to learn the higher-level structural representations to account for the data inductive biases:

$$
\begin{array}{l} m i n _ {\beta , \partial} \sum_ {i = 1} ^ {k + m} \left\| x _ {a l l} ^ {i} - \sum_ {j = 1} ^ {s} \partial_ {j} ^ {i} \beta_ {j} \right\| _ {2} ^ {2} + \gamma | | \partial^ {i} | | _ {1} \\ s. t. | | \beta_ {j} | | _ {2} \leq 1, \forall j \in 1,..., s \end{array}\tag{9}
$$

where $x _ { a l l } = \{ \boldsymbol { x _ { u } } ^ { 1 } , \boldsymbol { x _ { u } } ^ { 2 } , . . . , \boldsymbol { x _ { u } } ^ { k } , \boldsymbol { x _ { l } } ^ { 1 } , \boldsymbol { x _ { l } } ^ { 2 } , . . . , \boldsymbol { x _ { l } } ^ { m } \}$ represents all training data, $x _ { u } ^ { \ k }$ is the input vector for the k-th unlabeled instance $( \mathrm { t h e } ^ { \ast } u ^ { \prime \prime }$ subscript indicates that it is an unlabeled instance), $x _ { l } ^ { m }$ is the input vector for the m-th labeled instance (the $\mathbf { \mu } ^ { \mathfrak { s } } l ^ { \mathfrak { n } }$ subscript indicates that it is a labeled instance), $\mathbf { \nabla } \cdot \beta$ is a base vector describing the training samples, $\beta _ { j }$ is the j-th component of $\beta ,$ ∂ is the activation of $\beta , \partial _ { j } ^ { i }$ is the activation of basis $\beta _ { j } ,$ and $\gamma$ is the sparse coeficient controlling ∂. Sparse coding approxi mately expresses the input $\boldsymbol { x _ { a l l } } ^ { i }$ as a sparse linear combination of the base $\beta _ { j } ,$ and the sparse vector $\partial ^ { i }$ is a new feature representation for $x _ { a l l } ^ { \textit { i } } .$ $\operatorname { E q . } \left( 9 \right)$ encourages activations $\partial _ { j }$ to be sparse with a low $L _ { 1 }$ norm. Each learning input $\boldsymbol { x _ { a l l } } ^ { i }$ is a weighted linear combination of $\beta _ { j }$ and $\partial _ { j } .$ . Note that $\operatorname { E q . }$ (9) can be iteratively solved over ∂ and $\beta$ while holding the other set of variables fixed [29,30].

For the unsupervised feature construction, once the activations set ∂ and the basis vectors $\beta$ are obtained in Step 1, “higher-level” representations are reconstructed for the labeled data and the newly-built features incorporated into the underlying structural information of all credit samples:

$$
\widehat {\partial} (x _ {l} ^ {i}) = \underset {\partial^ {i}} {\mathrm{argmin}} \left\| x _ {l} ^ {i} - \sum_ {j = 1} ^ {s} \beta_ {j} \partial_ {j} ^ {i} \right\| _ {2} ^ {2} + \gamma \sum_ {j = 1} ^ {s} | | \partial^ {i} | | _ {1}\tag{10}
$$

Note that Eq. (10) encourages feature set $\widehat { \partial }$ to be sparse, that is, most of its elements are zero. Subsequently, supervised learning is used to model the pattern events for the credit scoring.

## 4.3. Binary classification for credit scoring

The accepted samples now have new feature representations learned from both the accepted samples and the selected rejects. Supervised learning methods, such as individual classifiers and ensemble approaches, are now applied to deal with the reject inference problem taking advantage of the proposed learning framework.

To verify the efectiveness and superiority of the proposed learning framework, state-of-the-art classification methods logistic regression (LR), artificial neural network (ANN), random forest (RF), and XGBoost: are applied for credit scoring [31].

## 5. Empirical study

## 5.1. Dataset

A Chinese personal credit dataset was used to verify the applicability and generality of the proposed learning framework for reject inference. The dataset was provided by a Chinese financial institution that ofers consumer loans to individuals in China. All loan data from Mar 2010 to June 2019 were extracted, including both the accepted and rejected loan listings. After excluding records with obvious errors or missing values, the sample contained 606,658 loan requests (578,150 rejected loans and 28,508 accepted loans), the acceptance ratio of the dataset was 4.7%. There were 24,112 non-default loans and 4396 default records for the accepted loans, and the raw credit data has 20 features for the borrowers' base loan, certification, employment, and assets information. The definitions and brief statistics for the variables are given in Table 1.

## 5.2. Experimental design

To comprehensively demonstrate the superiority of the proposed learning framework, three main experiments were systematically designed.

Experiment I: This experiment sought to verify whether the proposed three-stage learning framework could benefit reject inference if all rejected samples were simply transferred to learn the higher-level representations. A traditional credit scoring method (Model 1) developed based on the labeled data only was estimated for the accepted samples and set as the benchmark. As per Section 4.3, four widely-used models (LR, ANN, RF, and XGBoost) were employed as the base classifiers in this work. Then, all rejected data were selected to learn the higher-level representations (Model 2), that ${ \mathrm { i } } s ,$ all the rejected samples belonging to the positive, boundary, and negative regions were selected for the proposed learning framework. These two learning methods were then comprehensively analyzed.

Experiment II: This experiment explored whether the proposed learning method was able to efectively address the negative transfer problem and benefit the reject inference. The 3WD method was employed to select the rejected samples, which were divided into a posi tive region, and then used the proposed three-stage learning framework to learn the latent representations from both the accepted samples and the selected rejected samples (Model 3). Considering the Experiment I results, the results from Model 3, and Models 1 and 2 were investigated.

Experiment III: This experiment sought to clarify the superiority of the proposed learning method, for which state-of-the-art reject inference techniques (augmentation, parceling, and $\mathsf { { S } ^ { 3 } V M } )$ were applied. Consequently, the classification scores for these classic reject inference methods were compared to the results of Model $^ { 3 , }$ the details for which are reported in Section 6.

## 5.3. Model implementation and hyper-parameter optimization

To ensure the efectiveness and comparability of the experiment, the hyper-parameters for each method needed to be carefully set. To ensure fair classifier comparisons, all the credit scoring methods used were validated over the same training and test samples. Because a repeated stratified random sampling method was used for the data splitting, the default rates in the selected training and test subsets were the same as in the original data. As shown in Fig. 2, following $[ 5 , 1 6 ]$ , 70% of the accepted credit samples were randomly sampled as the training set (default rate. 15.42%) and 30% were randomly selected as the test set (default rate, 15.42%). To construct the validation set, 30% of the training set were randomly selected with the default ratio being the same. Therefore, the ratios for the defaulters/non-defaulters in the training subset, the test subset, and the validation set were the same as in the original accepted data. The number of reject applications were also randomly selected so that together with the training samples they had the same acceptance ratio (4.7%) as the original data.

For each of the models used, a grid search method was employed for the hyper-parameter optimization. Given a pre-specified hyper-parameter space, the grid search exhaustively explored all possible parameter combinations over the training subset, after which the classification abilities of the diferent parameter combinations were evaluated on the same validation dataset. Finally, the optimal hyper-parameters were determined based on the classification scores on the validation set. Note that to eliminate any sample difference influences. the same labeled training subset and rejected samples were used to optimize all the classification techniques. The hyper-parameter search spaces for all the classification techniques used in this study are listed in Table. 2.

To ensure fair comparisons, all models had identical training and test subsets and each experiment was run 30 times to guarantee robust results. All computational tests were conducted using Python<sup>1</sup> (version 3.7.4) on a PC equipped with Intel Core i5–8400 CPU and 16 GB usable RAM.

Table 1  
Definitions and statistical information of the variables for the used Chinese credit data.

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Type</td><td rowspan="2">Definition</td><td>Accepted</td><td>Rejected</td></tr><tr><td>Mean ± Std</td><td>Mean ± Std</td></tr><tr><td>Gender</td><td>Binary</td><td>Sex of applicant</td><td>0.87 ± 0.34</td><td>0.86 ± 0.35</td></tr><tr><td>Age</td><td>Discrete</td><td>Age of the applicant</td><td>31.60 ± 6.63</td><td>29.15 ± 6.42</td></tr><tr><td>Marriage</td><td>Categorical</td><td>Marital status</td><td>0.40 ± 0.56</td><td>0.74 ± 0.81</td></tr><tr><td>OfficeDomain</td><td>Categorical</td><td>Firm sector classification</td><td>7.16 ± 4.61</td><td>9.33 ± 4.91</td></tr><tr><td>OfficeScale</td><td>Categorical</td><td>Firm scale classification</td><td>1.54 ± 1.19</td><td>2.37 ± 1.40</td></tr><tr><td>OfficeType</td><td>Categorical</td><td>Firm nature classification</td><td>4.28 ± 2.65</td><td>5.89 ± 2.47</td></tr><tr><td>Salary</td><td>Categorical</td><td>Borrower&#x27;s income level</td><td>2.66 ± 1.35</td><td>4.10 ± 1.97</td></tr><tr><td>WorkYears</td><td>Categorical</td><td>Length of employment</td><td>1.17 ± 0.99</td><td>2.39 ± 1.36</td></tr><tr><td>Graduation</td><td>Categorical</td><td>Educational background</td><td>1.85 ± 0.82</td><td>2.41 ± 0.95</td></tr><tr><td>HasHouse</td><td>Binary</td><td>Whether the borrower is a homeowner</td><td>0.56 ± 0.50</td><td>0.30 ± 0.46</td></tr><tr><td>HouseLoan</td><td>Binary</td><td>Whether the borrower has a mortgage</td><td>0.23 ± 0.42</td><td>0.09 ± 0.29</td></tr><tr><td>HasCar</td><td>Binary</td><td>Whether the borrower is a car owner</td><td>0.40 ± 0.49</td><td>0.17 ± 0.37</td></tr><tr><td>CarLoan</td><td>Binary</td><td>Whether the borrower has a car loan</td><td>0.08 ± 0.28</td><td>0.04 ± 0.19</td></tr><tr><td>Credit</td><td>Binary</td><td>Verification of credit report</td><td>0.94 ± 0.24</td><td>0.21 ± 0.41</td></tr><tr><td>Work</td><td>Binary</td><td>Verification of work status</td><td>0.83 ± 0.37</td><td>0.05 ± 0.21</td></tr><tr><td>IncomeDuty</td><td>Binary</td><td>Verification of income</td><td>0.80 ± 0.40</td><td>0.05 ± 0.21</td></tr><tr><td>LoanPurpose</td><td>Categorical</td><td>Purpose for the loan</td><td>4.76 ± 2.15</td><td>4.74 ± 2.06</td></tr><tr><td>Amount</td><td>Continuous</td><td>Listed amount of loan</td><td>24,833 ± 44,003</td><td>60,944 ± 94,724</td></tr><tr><td>Interest</td><td>Continuous</td><td>Interest Rate on the loan</td><td>12.62 ± 2.31</td><td>13.39 ± 2.87</td></tr><tr><td>Month</td><td>Discrete</td><td>Number of installments</td><td>11.95 ± 7.92</td><td>15.90 ± 9.20</td></tr></table>

![](/api/attachments/KK6XEVAA/fulltext/images/b6a6e831886447937dc944e0850da4aa35354f2cd4d979ecdd9a79f4cd0c0542.jpg)  
Fig. 2. Data partition used in the experiments.

Table 2  
Search space of the hyper-parameters for the used algorithms in experimental study

<table><tr><td>Algorithm</td><td>Search space</td></tr><tr><td>LR</td><td>C∈ [0.01,1.0]; penalty∈{‘L1’,‘L2’}</td></tr><tr><td>ANN</td><td>hidden layer sizes∈[5, 100]; learning rate∈{‘constant’, ‘adaptive’}; activation∈ {‘relu’, ‘logistic’, ‘tanh’}</td></tr><tr><td>RF</td><td>number of estimators∈[10,100]; criterion∈{‘gini’, ‘entropy’}; max depth∈[3, 10]</td></tr><tr><td>XGBoost</td><td>number of estimators∈[10,100]; learning rate∈[0.1, 0.5]; max depth∈[3, 10]</td></tr><tr><td> $S^3VM^*$ </td><td>C∈[1, 5, 10, 13, 15, 17]; Gamma∈[0.5, 1, 1.5, 2, 2.5]; kernel∈{‘rbf’, ‘linear’}; r∈ [0.1, 1.0]</td></tr><tr><td>STL</td><td>number of bases∈[10,100]; sparse coefficient∈[0, 1]</td></tr></table>

<sup>⁎</sup> The $\mathsf { S } ^ { 3 } \mathrm { V M }$ was implemented using the open source code in [32].

## 5.4. Evaluation measures

It is important to choose appropriate measurement metrics in credit scoring problems to ensure a comprehensive evaluation of model effectiveness and to guide the classifier learning. Therefore, three widely used metrics for credit scoring problems were employed: brief score (BS), the Kolmogorov-Smirnov statistic (KS), and the area under the curve (AUC). As a mean-squared error (MSE) application for classification problems, BS measures the mean squared diference between the predicted probability and the actual credit sample response [31], with the score ranging from 0 (perfect probabilistic prediction) to 1 (poor prediction). The KS is a commonly used discrimination evaluation credit scoring indicator [33] that is equal to the maximum value of the diference between the false positive rate curve and the true positive rate curve, with the larger the KS value, the stronger the model's ability to distinguish between default borrowers and on-time repayment borrowers. Finally, the AUC is an extensively used discrimination cap ability measurement based on the ROC curve [33,34], with its value being equal to the area under the ROC curve, and ranging from ${ } ^ { \mathfrak { a } } 0 ^ { \mathfrak { n } }$ (indiscernibility) to “1” (perfect discernibility).

Table 3  
Classification results of Experiment I (%).

<table><tr><td></td><td>LR</td><td>ANN</td><td>RF</td><td>XGBoost</td></tr><tr><td colspan="5">Panel A. AUC</td></tr><tr><td>Model1</td><td> $74.74 \pm 0.34$ </td><td> $75.97 \pm 0.52$ </td><td> $75.99 \pm 0.15$ </td><td> $76.03 \pm 0.24$ </td></tr><tr><td>Model2</td><td> $74.93 \pm 0.09$ </td><td> $75.65 \pm 0.44$ </td><td> $75.81 \pm 0.58$ </td><td> $75.99 \pm 0.15$ </td></tr><tr><td colspan="5">Panel B. KS</td></tr><tr><td>Model1</td><td> $36.57 \pm 0.82$ </td><td> $38.95 \pm 1.07$ </td><td> $38.31 \pm 0.60$ </td><td> $38.75 \pm 0.96$ </td></tr><tr><td>Model2</td><td> $37.23 \pm 0.50$ </td><td> $37.94 \pm 0.96$ </td><td> $38.98 \pm 1.31$ </td><td> $38.48 \pm 0.75$ </td></tr><tr><td colspan="5">Panel C. BS</td></tr><tr><td>Model1</td><td> $11.56 \pm 0.07$ </td><td> $11.40 \pm 0.12$ </td><td> $11.37 \pm 0.05$ </td><td> $11.36 \pm 0.05$ </td></tr><tr><td>Model2</td><td> $11.51 \pm 0.03$ </td><td> $11.41 \pm 0.09$ </td><td> $11.50 \pm 0.07$ </td><td> $11.36 \pm 0.04$ </td></tr></table>

## 6. Experimental results

In this study, the three-stage learning framework was tested on a Chinese credit dataset, and three measurement metrics, a Friedman test and a post-hoc Nemenyi test [35] performed to test the ability of the proposed method in addressing the reject inference problem. All results for all methods used are reported in Tables 3-6. Several interesting conclusions were drawn from the empirical results.

## 6.1. Experiment I results

To explore whether reject inference could be improved, all the rejected Chinese credit data samples were transferred to learn the latent representations, after which Models 1 and 2 were separately estimated. Table 3 reports the average classification scores and standard devia tions for Models 1 and 2, with the results in bold indicating the best performances for each classifier over the three measurement indicators.

As shown in Table 3, Model 2 had a poorer performance than Model 1 over most classifiers, with the Model 2 classification scores for the ANN, RF, and XGBoost classifiers becoming more degraded in the overall evaluation metrics than in Model 1. Specifically, a maximum decrease of 1% was observed in the ANN model in terms of the KS indicator within the diferent learning frameworks. Interestingly, slight changes were observed using the BS indicator; however, when equipped with Model 2, the LR classifier performed slightly better than the conventional supervised learning framework.

In Model 2, the negative transfer problem was evident in the performance of the four state-of-the-art classifiers, indicating that when seeking to improve reject inference using an unsupervised transfer learning framework, this problem needs to be addressed.

## 6.2. Experiment II results

To deal with the negative transfer and address the reject inference problem, a data selection method based on three-way decision theory was proposed and the rejected samples divided into positive, boundary, and negative disjointed regions. Subsequently, based on the findings in

Table 4  
Classification results of Experiment II (Model 3) (%).

<table><tr><td></td><td>LR</td><td>ANN</td><td>RF</td><td>XGBoost</td></tr><tr><td>AUC</td><td>75.47 ± 0.41</td><td>76.40 ± 0.44</td><td>76.69 ± 0.53</td><td>77.35 ± 0.64</td></tr><tr><td>KS</td><td>38.00 ± 0.75</td><td>39.48 ± 0.95</td><td>40.55 ± 0.92</td><td>40.58 ± 1.17</td></tr><tr><td>BS</td><td>11.46 ± 0.07</td><td>11.31 ± 0.10</td><td>11.41 ± 0.07</td><td>11.21 ± 0.10</td></tr></table>

Table 5  
Classification results of Experiment III (%).

<table><tr><td></td><td>Parceling</td><td>Augmentation</td><td> $S^3VM$ </td></tr><tr><td>AUC</td><td>75.07 ± 0.26</td><td>74.28 ± 0.44</td><td>74.08 ± 0.46</td></tr><tr><td>KS</td><td>37.26 ± 0.77</td><td>35.89 ± 1.01</td><td>36.72 ± 0.88</td></tr><tr><td>BS</td><td>15.29 ± 0.36</td><td>11.97 ± 0.16</td><td>11.83 ± 0.11</td></tr></table>

Table 6

Average computation times for all the used learning methods (in seconds).  
Panel A. Base classifiers with diferent learning methods

<table><tr><td></td><td>LR</td><td>ANN</td><td>RF</td><td>XGBoost</td></tr><tr><td>Model 1</td><td>6.25</td><td>35.94</td><td>43.44</td><td>146.03</td></tr><tr><td>Model 2</td><td>288.06</td><td>370.75</td><td>335.31</td><td>1254.10</td></tr><tr><td>Model 3</td><td>456.97</td><td>576.22</td><td>1123.98</td><td>1828.44</td></tr></table>

Panel B. Classical reject inference models.

<table><tr><td>Parceling</td><td>Augmentation</td><td> $S^{3}VM$ </td></tr><tr><td>176.42</td><td>24.99</td><td>412.38</td></tr></table>

Section 6.1, the rejects from the negative and boundary regions were excluded and all remaining rejected data transferred to learn new representations for the accepted samples, that is, only the rejected samples from the positive regions were incorporated into the proposed learning method. The corresponding experimental results are shown in Table 4.

All the Model 3 classifiers significantly outperformed their corresponding classification performances in Model 1. Specifically, Model 3 greatly enhanced the LR, ANN and XGBoost classifiers over the BS, KS, and AUC indicators; however, there were few BS score improvements observed for the RF classifier. In general, the results in Table 4 suggested that the proposed learning framework would be suitable for practical reject inference applications.

Further, when Models 2 and Model 3 were compared, each of which had diferent rejected sample sets, Model 3 surprisingly outperformed Model 2 for all base classifiers over the three indicators, with the Model 3 AUC indicator achieving significantly better results than Model 2. In other words, the proposed data selection method based on 3WD was able to efectively avert the negative transfer problem.

## 6.3. Experiment III results

Some standard reject inference techniques parceling, augmentation, and S<sup>3</sup>VM method were also conducted and compared with the pro posed learning method, the results for which are shown in Table 5.

The following conclusions were made after Table 5 was compared to Tables 3 and 4. First, consider the ANN, RF, and XGBoost classifiers, the proposed learning framework that utilized the positive region rejected samples outperformed all three classical reject inference techniques over the three indicators, which proved the superior performance of the proposed method over traditional reject inference models. Second, compared to the traditional credit scoring models, the augmentation and ${ \mathsf { S } } ^ { 3 } { \mathsf { V M } }$ models had much poorer scores than the ANN, RF, and XGBoost classifiers, possibly because: (1) due to the large proportion of noisy data in the rejected dataset incorporated in the augmentation and ${ \mathsf { S } } ^ { 3 } { \mathsf { V M } } ,$ , the base classifiers discriminant capabilities were blocked, which was also shown in Section 7; and (2) the augmentation and $s ^ { 3 } \mathrm { V M }$ were developed based on logistic regression and support vector machines, the classification abilities of which are typically worse than advanced credit scoring models such as RF and XGBoost.

Finally, the computation eficiencies for the proposed learning framework were examined, with the summary average computation times (in seconds) shown in Table 6. The results showed that even though it had a relatively longer computational time, the proposed learning method, which utilized the positive region rejected samples for the transfer learning, was a much better choice than the traditional su pervised learning or the classical reject inference models. In summary, the proposed approach was shown to have significant potential for some real-world applications.

![](/api/attachments/KK6XEVAA/fulltext/images/a4ea962e3edfa9a375f524ef99963f993ff7874106f673b58ad5d88a057dcf43.jpg)  
(a) Nemenyi test of AUC indicator

![](/api/attachments/KK6XEVAA/fulltext/images/c07f19c7f6361375bba8c2356afffb75e66518a19454e41ff1ad5e5c150d2be1.jpg)

![](/api/attachments/KK6XEVAA/fulltext/images/6da130537724923a76baae4b1fa875155df3064372a0a8709f5ff69e913afd35.jpg)  
(c) Nemenyi test of BS indicator  
Fig. 3. Statistical significance tests for the learning methods involved in this study. Groups of classifiers that are not significantly diferent (at p = 0.10) are connected.

## 6.4. Significance tests for the experiments

To achieve convincing conclusions, statistical significance tests based on the Friedman and post-hoc Nemenyi tests were performed, with the result statistics for BS, the KS, and AUC shown in Fig. 3.

As shown in Fig. 3, Model 3 for most base learners generally and significantly outperformed Models 1 and Model 2. Specifically, in terms of the XGBoost classifier, the AUC and KS indicators in Model 3 were significantly superior to the other learning strategies for most classifiers, including the traditional supervised learning models and the standard reject inference techniques, it was concluded that the three stage learning framework significantly enhanced the reject inference. Model 3 was also significantly superior to Model 2 for ANN, RF, and XGBoost base classifiers over most indicators (two out of three), which further indicated the superiority of the proposed learning framework in addressing the negative transfer problem. Consider the XGBoost, RF, and ANN classifiers, there were no significant diferences under Model 3 over the three indicators; however, any small credit scoring improvements could result in significantly greater profits for financial institutions. Generally, this finding again proved that the proposed learning framework was a promising credit scoring research direction for reject inference.

## 7. Discussion

To comprehensively understand the superiority of the proposed learning method, this section further explored the underlying data structures for the accepted and rejected samples in the diferent regions.

Fig. 4 shows the data diferences between the accepted and rejected samples using a Q-Q plot. If the two sets came from a population with the same distribution, the points should fall approximately along the reference line, with the greater the departure from this reference line, the greater the evidence for the conclusion that the two datasets came from populations with diferent distributions. Here, the loan amount and interest continuous variables were verified.

Several interesting conclusions can be drawn from Fig. 4. First, the scatter plot for the accepted credit samples and all the rejected samples were far from the reference line, which indicated that the rejected sample distribution was significantly diferent from the accepted sample distribution. Based on the numerical results in Model 2, the negative transfer problem in Section 5.1 resulted from the transfer of “irrelevant” source data, which was consistent with Wang et al. [11]. Moreover, the scatterplot for the accepted and rejected samples in the positive region were much closer to the reference line than in the other two situations, that is, the rejected samples in the positive regions were more similar to the accepted samples in general, which further proved that the proposed three-stage learning framework is a promising approach for reject inference.

![](/api/attachments/KK6XEVAA/fulltext/images/a572fd93c98c89e2353d97590730bf4418cf5d71f0c1de64139713bd27de3061.jpg)  
(a)

![](/api/attachments/KK6XEVAA/fulltext/images/21b797af5a23b486bb43ad3e5c2ad7e0a712ab8386945883ae6ea2fa627577db.jpg)  
(b)  
Fig. 4. Q-Q plot for the accepted and rejected samples: (a) loan amount for the accepted samples versus the rejected samples in positive regions; (b) loan interest fo the accepted samples versus the rejected samples in positive regions.

## 8. Conclusions

In this study, a novel three-stage learning framework based on unsupervised transfer learning and three-way decision theory was proposed for reject inference, and an STL technique employed to learn “higher-level” representations for the credit risk classification task. The empirical results, as measured by three commonly used indicators and statistical significance tests, indicated that the proposed learning framework significantly outperformed the other learning methods, which implies that it has a broad prospective application for handling reject inference. The novel learning paradigm was also found to successfully deal with the negative transfer problems that normally occur in transfer learning. This study also explored the possible distributions between the accepted and rejected samples using a Q-Q plot, and found that the accepted and rejected samples had dissimilar distributions, which provided a comprehensive understanding of the inherent reject inference mechanism. Compared to other standard reject inference techniques, such as augmentation, parceling, and S<sup>3</sup>VM, the proposed learning method showed superior credit scoring task performances; therefore, it could be a prospective loan decision-making application for financial institutions. This method could assist in the development of an advanced internal credit scoring system for banks and other financial institutions, which could result in eficiency improvements and greater profits.

A Chinese credit data set was employed to verify the novel learning model, for which the rejected and accepted data shared identical classification variables. However, in more complex credit systems, there are normally fewer indicators in the rejected data than in the accepted data. Therefore, a major future research task is determining how to transfer the information contained in rejected samples to improve the credit scoring when fewer variables are available. The decision thresholds for the 3WD were explored using a grid search method, which required significant computation costs; therefore, more eficient methods for exploring the optimal thresholds for 3WD are needed.

## Acknowledgments

This research was supported by the Humanities and Social Sciences Foundation of the Ministry of Education of China (no. 17YJC630119) , National Natural Science Foundation of China (no. U1811462, no. 71910107002, no. 71725001), Chinese National Funding of Social Sciences (no. 19ZDA092) and Applied Basic Research Program of Sichuan Province (no. 2020YJ0042). It was also supported by the Fundamental Research Funds for the Central Universities (no. JBK2003020), the project of Research Center for System Sciences and Enterprise Development (no. Xq20B08), and the project of Fintech Innovation Center of Southwestern University of Finance and Economics.

## References

[1] R. Tsaih, Y.-J. Liu, W. Liu, Y.-L. Lien, Credit scoring system for small business loans, Decis, Support, Syst, 38 (1) (2004) 91–99.

[2] X. Dastile, T. Celik, M. Potsane, Statistical and machine learning models in credit scoring: a systematic literature survey, Appl. Soft Comput, 91 (2020) 106263.

[3] A. Feelders, Credit scoring and reject inference with mixture models, Int. J. Intell. Syst. Account Finance Manag. 9 (2000) 1–8.

[4] Z. Li, Y. Tian, K. Li, F. Zhou, W. Yang, Reject inference in credit scoring using semisupervised support vector machines, Expert Syst. Appl. 74 (2017) 105–114.

[5] Y. Tian, Z. Yong, J. Luo, A new approach for reject inference in credit scoring using kernel-free fuzzy quadratic surface support vector machines, Appl. Soft Comput. 73 (2018) 96–105.

[6] J. Banasik, J. Crook, Reject inference, augmentation, and sample selection, Eur. J. Oper. Res. 183 (3) (2007) 1582–1594.

[7] J. Crook, J. Banasik, Does reject inference really improve the performance of ap plication scoring models? J. Bank. Financ. 28 (4) (2004) 857–874.

[8] B. Anderson, Using bayesian networks to perform reject inference, Expert Syst. Appl, 137 (2019) 349–356

[9] Y. Yao, Three-way decisions with probabilistic rough sets, Inf. Sci. 180 (3) (2010) 341–353.

[10] Rajat Raina, Alexis Battle, Honglak Lee, Benjamin Packer, Y. Andrew, Self-taugh learning: transfer learning from unlabeled data, Proceedings of the 24th International Conference on Machine Learning. 2007, pp. 759–766

[11] Z. Wang, Z. Dai, B. Póczos, J. Carbonell, Characterizing and avoiding negative transfer. The JEEE Conference on Computer Vision and Pattern Recognition. 2019 pp. 11293–11302

[12] M.T. Rosenstein. Z. Marx. LP. Kaelbling, T.G. Dietterich. To transfer or not to transfer. NIPS 2005 Workshop on Transfer Learning, vol. 898. 2005, pp. 1–4.

[13] S.J. Pan, Q. Yang, A survey on transfer learning, IEEE Trans. Knowl. Data Eng. 22 (10) (2010) 1345–1359.

[14] J. Banasik, J. Crook, Credit scoring, augmentation and lean models, J. Oper. Res. Soc. 56 (9) (2005) 1072–1081.

[15] M. Bücker, M. van Kampen, W. Krämer, Reject inference in consumer credit scoring with nonignorable missing data, J. Bank. Financ. 37 (3) (2013) 1040–1045.

[16] R.A. Mancisidor, M. Kampfmeyer, K. Aas, R. Jenssen, Deep generative models for reject inference in credit scoring, Knowledge-Based Syst. 196 (2020) 105758.

[18] Y.-F. Li, Z.-H. Zhou, Towards making unlabeled data never hurt, Proceedings of the 28th International Conference on Machine Learning, vol. 37, 2011, pp. 1081–1088.

[19] F.G. Cozman, I. Cohen, Unlabeled data can degrade classification performance of generative classifiers, Proceedings of the 15th International Conference of the Florida Artificial Intelligence Research Society (FLAIRS). 2002, pp. 327–331.

[20] Y. Yao. Three-way decision: An interpretation of rules in rough set theory. In: Proceedings of Rough Sets and Knowledge Technology, 4th International Conference 2009; vol. 5589: 642–649.

[21] S. Maldonado, G. Peters, R. Weber, Credit scoring using three-way decisions with probabilistic rough sets, Inf. Sci. 507 (2020) 700–714.

[22] P. Wang, Y. Yao, Ce3: a three-way clustering method based on mathematical morphology, Knowledge-Based Syst. 155 (2018) 54–65.

[23] J. Qian, C. Dang, X. Yue, N. Zhang, Attribute reduction for sequential three-way decisions under dynamic granulation, Int. J. Approx. Reason. 85 (2017) 196–216

[24] Y. Yao, Three-way decision and granular computing, Int. J. Approx. Reason. 103 (2018) 107–123.

[25] M.K. Afridi, N. Azam, J. Yao, E. Alanazi, A three-way clustering approach for handling missing data using gtrs, Int. J. Approx. Reason. 98 (2018) 11–24.

[26] R. Maesschalck, D. Jouan-Rimbaud, D. Massart, The mahalanobis distance, Chemom. Intell. Lab. Syst. 50 (1) (2000) 1–18.

[27] Mvung Geun Kim, Multivariate outliers and decompositions of mahalanobis distance, Commun. Stat-Theor M 29 (7) (2000) 1511–1526.

[28] L. Francesco, B. Stefan, L. Mario, R. Gunnar, G. Sylvain, S. Bernhard, B. Olivier, Challenging common assumptions in the unsupervised learning of disentangled representations, Proceedings of the 36th International Conference on Machine Learning, vol. 97, 2019, pp. 4114–4124.

[29] H. Lee, A. Battle, R. Raina, A.Y. Ng, Efficient sparse coding algorithms, Ady. Neural

Inf. Proces. Syst. 19 (2007) 801–808.

[30] A.Y. Ng, Feature selection, L1vs. L2regularization, and rotational invariance, Proceedings of the 21st International Conference on Machine Learning, 2004, pp. 78-85.

[31] S. Lessmann, B. Baesens, H.-V. Seow, L.C. Thomas, Benchmarking state-of-the-art classify cation algorithms for credit scoring: an update of research, Eur. J. Oper. Res. 247 (2015) 124–136.

[32] F. Bagattini and P.Cappanera and F. Schoen, Lagrangean-based combinatorial optimization for large-scale S3VMS. In IEEE Transactions on Neural Networks and Learning Systems 2017: 1–10.

[33] D.J. Hand, Good practice in retail credit scorecard assessment, J. Oper. Res. Soc. 56 (9) (2005) 1109–1117.

[34] T. Fawcett, An introduction to ROC analysis, Pattern Recogn. Lett. 27 (8) (2006) 861–874.

[35] Janez Demšar, Statistical comparisons of classifiers over multiple data sets, J. Mach. Learn. Res. 7 (2006) 1–30.

Feng Shen is a professor at School of Finance, Southwestern University of Finance and Economics. He received his Ph.D. from School of Business, Sichuan University. His current research interests include financial risk management, credit scoring, fintech, ma chine learning, data mining, and quantitative trading.

Xingchao Zhao is currently pursuing the Ph.D. degree in Finance, School of Finance, Southwestern University of Finance and Economics. His current research interests includ credit risk management, fintech, machine learning, and data mining.

Gang Kou is a professor and executive dean of School of Business Administration, Southwestern University of Finance and Economics. He received his Ph.D. in Information Technology from the College of Information Science & Technology, University of Nebraska at Omaha; got his Master degree in Department of Computer Science, University of Nebraska at Omaha; and B.S. degree in Department of Physics, Tsinghua University, Beijing, China. His research interests are in Data mining, Multiple Criteria Decision Making and Credit management. He has published more than eighty papers in various peer-reviewed journals. Gang Kou is listed as the Highly Cited Researcher (Computer Science) by Clarivate Analytics (Web of Science).
