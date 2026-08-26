---
otero_id: 1460
otero_key: "F64TG7UK"
title: "Inverse matrix-free incremental proximal support vector machine"
authors: "Zhenfeng Zhu; Xingquan Zhu; Yuefei Guo; Yangdong Ye; Xiangyang Xue"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.02.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Inverse matrix-free incremental proximal support vector machine

Zhenfeng Zhu <sup>a,</sup>⁎, Xingquan Zhu <sup>b</sup>, Yuefei Guo <sup>c</sup>, Yangdong Ye <sup>a</sup>, Xiangyang Xue <sup>c</sup>

<sup>a</sup> School of Information Engineering, Zhengzhou University, 100 Kexue Road, Zhengzhou 450001, PR China

<sup>b</sup> QCIS Center, Faculty of Engineering & Information Technology, University of Technology, Sydney, NSW 2007, Australia

<sup>c</sup> School of Computer Science, Fudan University, 220 Handan Road, Shanghai 200433, PR China

## a r t i c l e i n f o

Article history: Received 16 February 2011 Received in revised form 8 February 2012 Accepted 14 February 2012 Available online 21 February 2012

Keywords: Incremental learning Incremental proximal support vector machine High dimensionality Large scale

## a b s t r a c t

Traditional Support Vector Machines (SVMs) based learners are commonly regarded as strong classi<sup>fi</sup>ers for many learning tasks. Their ef<sup>fi</sup>ciency for large-scale high dimensional data, however, has shown to be unsatisfactory. Consequently, many alternative SVM solutions exist for large-scale and/or high dimensional data. Among them, proximal support vector machine (PSVM) is a simple but effective SVM classi<sup>fi</sup>er. Its incremental version (ISVM) is also available for large-scale data. Nevertheless, the computational ef<sup>fi</sup>ciency of the ISVM for high dimensional data still needs to be improved, mainly because it requires explicit matrix inversion for updating the decision model. To solve this problem, we propose, in this paper, an inverse matrix-free incremental PSVM (IMISVM) with the following two characteristics. Firstly, IMISVM avoids explicit matrix inversion and hence derives simple formulas for updating model parameters. Secondly, IMISVM achieves faster convergence speed than ISVM. Experimental results on synthetic and real-world data sets con<sup>fi</sup>rm that the proposed incremental classi<sup>fi</sup>er outperforms ISVM.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Traditional Support Vector Machines (SVMs) have been commonly regarded as strong classi<sup>fi</sup>ers for many learning tasks [13,33]. As our data-gathering ability continuously grows, in many applications, large-scale or continuous stream data make the standard SVMs inef<sup>fi</sup>- cient (or even inapplicable) for decision making [35]. To solve these problems, a number of variations are proposed [8,16,18,20, 21,24,27,28]. Among them, the proximal SVM (PSVM) and least squares SVM (LS-SVM) are simple yet effective algorithms [8,27], due to the essence of regularized least squares problems which merely need to solve linear equations [31]. In comparison, LS-SVM needs to calculate about n variables or parameters whereas PSVM has d variables for the corresponding linear equations, where n and d are the numbers of samples and dimensions, respectively.

To solve the problem and capture the dynamic decision logics from large-scale high dimensional data, the SVM based incremental learning mechanisms are developed, such as [2,4–7,9,12,25,26, 29,30,32], in which the representative methods employ a nice property of the SVM: the decision function resulting from the whole data set is the same as the one from the support vectors alone [29,30]. Accordingly, after new data are obtained, SVM classi<sup>fi</sup>ers can be trained from the new data plus the support vectors from the old ones [2,25,29,30]. Thus, these methods are able to scale up to large-scale data. Cauwenberghs and Poggio [4] claim that the methods like [29,30] only get approximate (or distorted) solutions which are different from the ones trained from the whole data set. Further, to build incremental SVM classi<sup>fi</sup>er with exact solutions, the paper [4] proposes a support vector classi<sup>fi</sup>cation machine (SVCM). Another strategy for designing incremental SVMs is to select informative training samples [5]. To achieve this, Cheng and Shih [5] employ k-means algorithm and active query. At the same time, the incremental versions of PSVM and LS-SVM also exist, in which the incremental PSVM (referred to as ISVM in this paper) has identical solution to PSVM [9]. A variation of ISVM has similar accuracy in handling concept drift data [14] with about a half runtime saving [32], whereas the complexity of the revised ISVM is still the same asymptotic complexity as ISVM. Similarly, the incremental versions of LS-SVM also have identical solution to LS-SVM [6,12]. Nevertheless, when new samples are attained, the solution in [6,12] has to explicitly invert the matrices with larger sizes which are decided by the number of samples. In contrast to LS-SVM, the sizes of inverse matrices of PSVM lie on the dimensionality. As is well known, for the incremental versions of PSVM and LS-SVM, sooner or later, the number of samples n will become much larger than the dimensionality d. Therefore, the incremental variations of PSVM are more ef<sup>fi</sup>cient than those of LS-SVM.

The analyses discussed above indicate that, one general assumption for incremental SVM methods is that the number of support vectors is much smaller than the size of the whole data set. In the extreme situation, all data points are support vectors, such as the two-spiral classi<sup>fi</sup>cation problem [27]. Consequently, the sizes of the decision model of the incremental SVM methods such as [29,30] may continuously grow with the data sizes, which makes the incremental learning ineffective or failed. On the other hand, the PSVM method, with the model size decided by the dimensionality, has similar results to the genuine SVM models [8]. The incremental method of PSVM (ISVM) is also a practical method for large-scale data. Once new data are added, ISVM has to explicitly invert modi<sup>fi</sup>ed matrices [9], which makes ISVM ineffective to scale up to high dimensional data.

In this study, we focus on ISVM and intend to address the problem of devising an incremental learning algorithm called inverse matrixfree incremental PSVM (IMISVM). The IMISVM is able to generate the same solution as ISVM but has one order of magnitude less time complexity than ISVM, the corresponding improvement is especially evident for high-dimensional and large-scale data. The proposed method derives simple formulas to update the inverse of the modi<sup>fi</sup>ed matrix. As a result, the model parameters are directly updated without explicitly solving the matrix inverse. Besides, it is well known that the solutions of PSVM and ISVM are regularized [8,9]. The corresponding regularization term is useful for insuf<sup>fi</sup>cient samples to solve the ill-posed problem [31]. However, this regularization term may result in some errors or model distortion. In this research, once the number of samples in incremental learning becomes large enough to avoid the ill-posed problem, this term is eliminated, which can retain (or improve) the prediction accuracy and speed up the convergence. Experimental results on real world UCI data set, USPS images, biological data and high dimensional synthetic data verify the effectiveness of our method.

Compared with ISVM, IMISVM also has constant model size which is independent of the data sizes. Besides, the main contributions of this study are threefold:

• Ef<sup>fi</sup>ciency for high dimensional data: Instead of calculating the matrix inversion to <sup>fi</sup>nd the solutions, simple but ef<sup>fi</sup>cient formulas are derived to update model parameters. As a result, IMISVM is very suitable for high dimensional data, and our experimental results show that its performance on the 4800 dimensional synthetic data is about 51 times faster than ISVM.

• Ef<sup>fi</sup>ciency for large scale data: The time complexity of IMISVM is linear to the number of samples. So, IMISVM can effectively deal with the large sample data.

• Fast convergence speed: The theoretical analysis and experimental results reveal that IMISVM has identical or better solutions than PSVM and ISVM. More importantly, the elimination of the regularization term is capable of accelerating the convergence speed of IMISVM.

The remainder of this paper is structured as follows. Section 2 describes PSVM and its incremental version (ISVM). The proposed incremental learning method IMISVM and its improvement are discussed in Section 3 which also compares IMISVM with ISVM. The details of IMISVM algorithm are given in Section 4, followed by the experimental results in Section 5. Conclusion and remarks are reported in Section 6.

## 2. Proximal support vector machine (PSVM)

This section brie<sup>fl</sup>y reviews the proximal SVM, and its incremental version.

## 2.1. Batch version of PSVM

PSVM is a simple and effective SVM classi<sup>fi</sup>er [8]. This classi<sup>fi</sup>er is described as follows. Assume that $\boldsymbol { x } \in R ^ { d \times 1 }$ represents an example in d dimensional spaces and $X = [ x _ { 1 } , x _ { 2 } , . . . , x _ { n } ] ^ { T } { \in } \mathbf { \hat { \boldsymbol { R } } } ^ { n \times d }$ is the sample matrix consisting of n samples. Diagonal matrix $D \in { \cal R } ^ { n \times n }$ is used to assign the labels +1 and −1 for the positive and negative samples, respectively. The column vector of ones in n dimensional spaces is denoted by e. The objective function formulates an unconstrained optimization problem [8,9],

$$
\begin{array}{l} f (\vartheta , \gamma) = \min \biggl (\frac {1}{2} \left(\vartheta^ {T} \vartheta + \gamma^ {2}\right) + \frac {1}{2 \lambda} | | y | | ^ {2} \biggr), \\ s. t. \quad D (X \vartheta - e \gamma) + y = e \end{array}\tag{1}
$$

where $\vartheta \in R ^ { d \times 1 }$ is the parameter vector, γ is a scalar, λ is a positive tuning parameter, and y is the error variable. Setting the gradient with respect to $[ \vartheta ^ { T } , \gamma ] ^ { T }$ and solving the equations of ϑ and γ [8,9], we have,

$$
\left[ \begin{array}{c} \vartheta \\ \gamma \end{array} \right] = \left(\lambda I + Z ^ {T} Z\right) ^ {- 1} Z ^ {T} D e,\tag{2}
$$

where I is an identity matrix, the symbo $Z = [ X , - e ]$ can be viewed as an extended sample matrix. The parameters ϑ and γ form the optimal separating hyperplane [8,9,33], which is shown in Fig. 1. The hyperplanes $x ^ { T } \vartheta - \gamma = \pm 1$ determine the width of margin, and the positive and negative samples are pushed apart by optimizing the objective function (1). Conveniently, Eq. (2) is further simpli<sup>fi</sup>ed,

$$
\boldsymbol {\omega} = (\lambda I + A) ^ {- 1} Z ^ {T} L = \hat {A} ^ {- 1} Z ^ {T} L,\tag{3}
$$

where $\boldsymbol { \omega } = [ \vartheta ^ { T } , \gamma ] ^ { T } ,$ , the matrix $A = Z ^ { T } Z$ is called the cross-product matrix of $Z , { \hat { A } } = \lambda I + A$ and $L = D e$

From the perturbation theory point of view, the parameter λI in Eq. (3) is actually a perturbation or regularization term for producing computationally stable solution to the ill-posed problem [31]. In other words, the solution in Eq. (3) is regularized.

To classify the test instance $\boldsymbol { x } \in \bar { \boldsymbol { R } } ^ { d \times 1 }$ , the sign function is,

$$
s i g n \Big (x ^ {T} \vartheta - \gamma \Big) = \left\{ \begin{array}{l l} + 1 & \text { if } x ^ {T} \vartheta - \gamma \geq 0, \\ - 1 & \text { else }. \end{array} \right.\tag{4}
$$

## 2.2. Incremental version of PSVM (ISVM)

According to Eq. (3), the weight ω of ISVM is updated by

$$
\tilde {\omega} = \left(\hat {A} + z z ^ {T}\right) ^ {- 1} \left(Z ^ {T} L + z l\right),\tag{5}
$$

where z is a column vector denoting the new (extended) instance, and l is a degraded matrix, a scalar here, representing the label of z. On the basis of Eq. (5), ISVM incrementally adds new samples and updates the weight. It is obvious that ISVM is equivalent to PSVM.

![](/api/attachments/F64TG7UK/fulltext/images/5373a463aeb004274973f3b2e6a09219ec948e366eed74d7873ef90193bedd17.jpg)  
Fig. 1. The illustration of proximal SVM classi<sup>fi</sup>er. The hyperplanes $x ^ { T } \vartheta - \gamma = \pm 1$ of positive and negative sample sets $X +$ and X− determine the width of margin. Then, the samples belonging to different categories are pushed apart by optimizing the objective function (1).

Note that, when computing the parameter ω\~ , ISVM directly inverts the matrix $\tilde { \boldsymbol { A } } = \hat { \boldsymbol { A } } + z \boldsymbol { z } ^ { T }$ [9]. To improve the ef<sup>fi</sup>ciency of ISVM, the backslash operation (in Matlab software) can be used, but the magni tude of the computational complexity is not changed. If the size of the matrix Ã is small, the direct calculation is feasible, however, when its size is large, the high computational cost of matrix inverse makes it worthwhile to pursue other solutions.

## 3. ISVM with inverse matrix-free

## 3.1. Basic method

In the original ISVM problems, if the number of dimensions is large, ISVM has to solve a large matrix inverse problem which requires high time complexity. This problem can be solved by the IMISVM. We know that the Sherman–Morrison formula is ef<sup>fi</sup>cient for solving modi<sup>fi</sup>ed problems when the modi<sup>fi</sup>ed entries in a matrix lie in a row or a column [1,11]. In fact, even if all the entries are changed, it is also possible for us to employ this formula. To be speci<sup>fi</sup>c, this formula is useful if the update is a rank-one modi<sup>fi</sup>cation. For our problem, this change comes from the continuous addition of samples in the form of $z z ^ { T }$ . When the <sup>fi</sup>rst example $z \in R ^ { ( d + 1 ) \times 1 }$ is gained, IMISVM uses the Sherman–Morrison formula to calculate the initial matrix inversion,

$$
\hat {A} ^ {- 1} = \left(\lambda I + z z ^ {T}\right) ^ {- 1} = \frac {I}{\lambda} - \frac {z}{\lambda^ {2} + \lambda z ^ {T} z} z ^ {T},\tag{6}
$$

Consequently, the initial weight vector ω^ equals $\hat { A } ^ { - 1 } z$ l by Eq. (3) where l is the label of z.

After initializing the parameters $\hat { A } ^ { - 1 }$ and ω^ by Eqs. (6) and (3) respectively, the two parameters are updated by using new instance as follows. Consider the foregoing samples form the sample matrix $Z ,$ when getting a new instance z, the sample matrix becomes $\tilde { Z } =$ $\left[ Z ^ { T } , z \right] ^ { T }$ , and

$$
\begin{array}{l} \tilde {A} = \tilde {Z} ^ {T} \tilde {Z} + \lambda I \\ = \left[ \frac {Z}{z ^ {T}} \right] ^ {T} \left[ \frac {Z}{z ^ {T}} \right] + \lambda I \\ = \left[ Z ^ {T}, z \right] \left[ \frac {Z}{z ^ {T}} \right] + \lambda I \\ = Z ^ {T} Z + \lambda I + z z ^ {T} \\ = \hat {A} + z z ^ {T}. \end{array}\tag{7}
$$

To update the weight vector, $\tilde { A } ^ { - 1 }$ should be calculated. Based on the Sherman–Morrison formula, the $\hat { A } ^ { - 1 }$ is updated as follows,

$$
\begin{array}{l} \tilde {A} ^ {- 1} = \left(\hat {A} + z z ^ {T}\right) ^ {- 1} \\ \quad = \hat {A} ^ {- 1} - \hat {A} ^ {- 1} z \Big (1 + z ^ {T} \hat {A} ^ {- 1} z \Big) ^ {- 1} z ^ {T} \hat {A} ^ {- 1} \\ \quad = \hat {A} ^ {- 1} - \frac {\hat {A} ^ {- 1} z}{\left(1 + z ^ {T} \hat {A} ^ {- 1} z\right)} z ^ {T} \hat {A} ^ {- 1} \\ \quad = \hat {A} ^ {- 1} - \frac {\beta}{1 + z ^ {T} \beta} z ^ {T} \hat {A} ^ {- 1} \\ \quad = \hat {A} ^ {- 1} - \mu z ^ {T} \hat {A} ^ {- 1} \\ \quad = \hat {A} ^ {- 1} - \mu \beta^ {T} \\ \quad = \Big (I - \mu z ^ {T} \Big) \hat {A} ^ {- 1} \\ \quad = \alpha \hat {A} ^ {- 1}, \end{array}\tag{8}
$$

where $\beta = \hat { A } ^ { - 1 } z , \mu = \beta / ( 1 + z ^ { T } \beta )$ and $\begin{array} { r } { \alpha { = } I { - } \mu z ^ { T } . } \end{array}$ We observe that the parameters β, μ, and α are all functions of the instance z. Besides, each parameter only has a single instance z. It embodies the decomposition course of $z z ^ { T }$ from the <sup>fi</sup>rst line to the last one in Eq. (8). The derivation in the sixth line indicates that the update of $\hat { \boldsymbol A } ^ { - 1 }$ is a simple rank-one modi<sup>fi</sup>cation.

According to PSVM, the update of ω^ is derived as follows,

$$
\begin{array}{l} \tilde {\omega} = \tilde {A} ^ {- 1} \tilde {Z} ^ {T} \tilde {L} \\ \qquad = \alpha \hat {A} ^ {- 1} \left[ Z ^ {T}, z \right] \left[ \begin{array}{c} L \\ l \end{array} \right] \\ \qquad = \alpha \Big [ \hat {A} ^ {- 1} Z ^ {T}, \hat {A} ^ {- 1} z \Big ] \left[ \begin{array}{c} L \\ l \end{array} \right] \\ \qquad = \alpha \Big (\hat {A} ^ {- 1} Z ^ {T} L + \hat {A} ^ {- 1} z l \Big) \\ \qquad = \alpha (\hat {\omega} + \beta l) \\ \qquad = \Big (I - \mu z ^ {T} \Big) (\hat {\omega} + \beta l) \\ \qquad = (\hat {\omega} + \beta l) - \mu z ^ {T} (\hat {\omega} + \beta l) \\ \qquad = (\hat {\omega} + \beta l) - z ^ {T} (\hat {\omega} + \beta l) \mu \\ \qquad = v - z ^ {T} v \mu , \end{array}\tag{9}
$$

where $\begin{array} { r } { { \pmb v } = \hat { \pmb { \omega } } + \beta l . } \end{array}$ Note that the parameters $z ^ { T } \hat { \omega } , z ^ { T } \beta$ and l are all scalars.

Fig. 2 illustrates the adjustment course of IMISVM. For ease of understanding, this <sup>fi</sup>gure only depicts the separating hyperplane. The initial samples (in red $\cdot _ { \times } \cdot$ and blue ‘|’) produce the gray decision hyperplane. When the samples (in red $\cdot _ { + } \cdot$ and blue $\cdot _ { - \ ' }$ increase, the gray hyperplane is changed to the black one. Namely, the hyperplane $x ^ { T } \hat { \vartheta } - \hat { \gamma } = 0 ,$ , by translating −γ^ and rotating ϑ<sup>^</sup>, can effectively separate positive samples from negative ones.

Lemma 1. The basic IMISVM has the same solution as PSVM.

Proof. For the <sup>fi</sup>rst instance $z _ { 1 }$ and its label l , Eqs. (6) and (3) mean that $\tilde { A } _ { 1 } ^ { - 1 } = ( \lambda I + z _ { 1 } z _ { 1 } ^ { T } ) ^ { - 1 }$ and $\tilde { \omega } _ { 1 } = \tilde { A } _ { 1 } ^ { - 1 } z _ { 1 } l _ { 1 }$ where $\tilde { \omega } _ { 1 }$ is the initial weight vector.

Furthermore, we set the sample matrix $Z _ { i } = [ z _ { 1 } ; z _ { 2 } ; \cdots ; z _ { i } ]$ and its label vector $L _ { i } = [ l _ { 1 } , l _ { 2 } , \cdots , l _ { i } ] ^ { T }$ where $2 \leq i \leq n .$ For the IMISVM, Eq. (7) indicates that

$$
\begin{array}{r l} & {\tilde {A} _ {i} = \tilde {A} _ {i - 1} + z _ {i} z _ {i} ^ {T}} \\ & {\quad = \lambda I + z _ {1} z _ {1} ^ {T} + z _ {2} z _ {2} ^ {T} + \dots + z _ {i} z _ {i} ^ {T}} \\ & {\quad = \lambda I + Z _ {i} ^ {T} Z _ {i},} \end{array}\tag{10}
$$

![](/api/attachments/F64TG7UK/fulltext/images/5c851b69dd2be81f3bfd42812401cba61b195b321e12a6a9c589243da851ed64.jpg)  
Fig. 2. The illustration of IMISVM classi<sup>fi</sup>er. The initial samples (in red $\because$ and blue ‘|’) determine the gray (dashed) decision hyperplane. As the samples (in red $\because$ and blue ‘ ’) increase, the initial hyperplane is adjusted to the black (solid) one.

and Eq. (8) implies that

$$
\begin{array}{r l} \tilde {A} _ {i} ^ {- 1} & = \left(\tilde {A} _ {i - 1} + z _ {i} z _ {i} ^ {T}\right) ^ {- 1} \\ & = \tilde {A} _ {i - 1} ^ {- 1} - \mu_ {i} \beta_ {i} ^ {T} \\ & = \tilde {A} _ {1} ^ {- 1} - \mu_ {2} \beta_ {2} ^ {T} - \mu_ {3} \beta_ {3} ^ {T} - \dots - \mu_ {i} \beta_ {i} ^ {T}, \end{array}\tag{11}
$$

or,

$$
\begin{array}{l} \tilde {A} _ {i} ^ {- 1} = \Big (\tilde {A} _ {i - 1} + z _ {i} z _ {i} ^ {T} \Big) ^ {- 1} \\ \qquad = \alpha_ {i} \tilde {A} _ {i - 1} ^ {- 1} \\ \qquad = \alpha_ {i} \Big (\alpha_ {i - 1} \Big (\dots \Big (\alpha_ {2} \tilde {A} _ {1} ^ {- 1} \Big) \Big) \Big), \end{array}\tag{12}
$$

where $\beta _ { i } = \tilde { A } _ { i - 1 } ^ { - 1 } z _ { i } , \mu _ { i } = \beta _ { i } / ( 1 + z _ { i } ^ { T } \beta _ { i } )$ and $\alpha _ { i } { = } I { - } \mu _ { i } z _ { i } ^ { T }$ In addition, Eq. (9) derives that

$$
\begin{array}{r l} & {\tilde {\omega} _ {i} = \alpha_ {i} (\dots (\alpha_ {3} (\alpha_ {2} (\tilde {\omega} _ {1} + \beta_ {2} l _ {2}) + \beta_ {3} l _ {3}) + \dots) + \beta_ {i} l _ {i})} \\ & {\qquad = \alpha_ {i} (\tilde {\omega} _ {i - 1} + \beta_ {i} l _ {i})} \\ & {\qquad = \tilde {A} _ {i} ^ {- 1} Z _ {i} ^ {T} L _ {i}.} \end{array}\tag{13}
$$

For the batch method PSVM,

$$
\hat {A} _ {n} = \lambda I + Z _ {n} ^ {T} Z _ {n}\tag{14}
$$

and Eq. (3) means that

$$
\hat {\omega} _ {n} = \hat {A} _ {n} ^ {- 1} Z _ {n} ^ {T} L _ {n}.\tag{15}
$$

The derivations in Eqs. (10), (11), (12) and (14) reveal that, when $i = n , \tilde { A } _ { n } = \tilde { A } _ { n }$ and $\tilde { A } _ { n } ^ { - 1 } = \hat { A } _ { n } ^ { - }$ −1

Finally, Eqs. (13) and (15) prove that IMISVM and PSVM have the same solution, namely,

$$
\begin{array}{r} \tilde {\omega} _ {n} = \tilde {A} _ {n} ^ {- 1} Z _ {n} ^ {T} L _ {n} \\ = \hat {A} _ {n} ^ {- 1} Z _ {n} ^ {T} L _ {n} \\ = \hat {\omega} _ {n}. \end{array}\tag{16}
$$

## 3.2. Improvement of IMISVM

Section 1 shows that the regularization term λI is a perturbation term for producing computationally stable solution to the ill-posed problem [31]. If the problem becomes well-posed, it seems unreasonable for us to still preserve the parameter λI. Namely, for well-posed problems, λI may result in some errors, such as unsatisfactory prediction accuracy. For incremental learning, this term is unnecessary once the number of samples becomes suf<sup>fi</sup>ciently large. In other words, the cross-product matrix $A { = } Z ^ { T } Z$ becomes nonsingular. Then, the exact inverse of A can be obtained by employing the Woodbury formula [11,34],

$$
A ^ {- 1} = (\hat {A} - \lambda I) ^ {- 1} = (I + \lambda \hat {A} ^ {- 1} (I - \lambda \hat {A} ^ {- 1}) ^ {- 1}) \hat {A} ^ {- 1}.\tag{17}
$$

On the basis of Eq. (17), the time complexity for correcting $A ^ { - 1 }$ is about $O ( 3 ( d + 1 ) ^ { 3 } )$ that is too expensive. We also know that <sup>^</sup>A equals $A + \ M ,$ which means the equation $A = \hat { A } - \lambda I$ can eliminate the regularization term. Thus, the exact model parameter ω is computed by using backslash operation. Although Eq. (17) does not transform the inverse of a larger matrix into that of a smaller one like its original intention, we observe that the nonsingularity of term $I { - } { \lambda } \hat { A } ^ { - 1 }$ is crucial to get the exact inverse, so this term is useful to judge if the number of samples becomes large enough to correct $A ^ { - 1 }$ . Once this inversion is corrected, IMISVM algorithm updates ω continuously and achieves faster convergence speed than ISVM.

Note that, to solve over-<sup>fi</sup>tting problems, we often add regularization term into some models. In fact, the regularization is used to train models on data sets of limited size for avoiding severe over-<sup>fi</sup>tting ([3], p. 145). For the incremental learning, the number of samples can become larger and larger, which will, in turn, provide enough information for training models without the regularization term. In this situation, this term can be dropped.

## 3.3. Comparisons between ISVM and IMISVM

The above analysis shows that both ISVM and the basic IMISVM are equivalent to PSVM. Therefore, the basic IMISVM is also equivalent to ISVM. This equivalence implies that the two incremental classi<sup>fi</sup>ers have the same prediction accuracy.

For convenience, $\hat { A } ^ { - 1 }$ and ω are also for representing $\hat { \boldsymbol A } ^ { - 1 } \left( \tilde { \boldsymbol A } ^ { - 1 } \right)$ and ω^ (ω\~ ), respectively. To update A<sup>−1</sup> and ω, IMISVM circumvents the explicit inverse which is necessary for ISVM, and gets the simple updating formulas described in Eqs. (8) and (9). Further, we analyze the time complexity of IMISVM. The computations of $A ^ { - 1 }$ and ω include two parts:

1) The initializations by Eqs. (6) and (3), and

2) the updates by Eqs. (8) and (9).

The time complexities of the two parts are about $O ( 2 ( d + 1 ) ^ { 2 } )$ each, and the total complexity for all n samples is about $O ( 2 ( d +$ $1 ) ^ { 2 } n )$ .

By contrast, the computational cost of ISVM is about $O ( ( d + 1 ) ^ { 3 } +$ $( d + \dot { 1 } ) ^ { 2 } ) n )$ which can be simpli<sup>fi</sup>ed as $O ( ( d + 1 ) ^ { 3 } n )$ . When the backslash operation is utilized, the complexity is reduced to $O ( ( d + 1 ) ^ { 3 } n /$ 3), but the magnitude of the complexity remains the same. So, IMISVM is more ef<sup>fi</sup>cient than ISVM. When IMISVM eliminates the term λI, the additional computational cost is $O ( ( d + 1 ) ^ { 3 } / 3 )$ . Thereby, for a number of samples, this operation hardly changes the time complexity of IMISVM.

Moreover, IMISVM can also discard old data by using $A - z z ^ { T }$ to update A like that in [9]. This operation is able to dynamically remove some outdated samples, the relative derivation is described as follows.

Based on the current $A ^ { - 1 }$ , when deleting an old instance z,

$$
\begin{array}{l} \tilde {A} ^ {- 1} = \left(\hat {A} - z z ^ {T}\right) ^ {- 1} \\ \quad = \hat {A} ^ {- 1} + \hat {A} ^ {- 1} z \Big (1 - z ^ {T} \hat {A} ^ {- 1} z \Big) ^ {- 1} z ^ {T} \hat {A} ^ {- 1} \\ \quad = \hat {A} ^ {- 1} + \frac {\hat {A} ^ {- 1} z}{\left(1 - z ^ {T} \hat {A} ^ {- 1} z\right)} z ^ {T} \hat {A} ^ {- 1} \\ \quad = \hat {A} ^ {- 1} + \frac {\beta}{1 - z ^ {T} \beta} z ^ {T} \hat {A} ^ {- 1} \\ \quad = \hat {A} ^ {- 1} + \mu^ {\prime} z ^ {T} \hat {A} ^ {- 1} \\ \quad = \hat {A} ^ {- 1} + \mu^ {\prime} \beta^ {T} \\ \quad = \Big (I + \mu^ {\prime} z ^ {T} \Big) \hat {A} ^ {- 1} \\ \quad = \alpha^ {\prime} \hat {A} ^ {- 1}, \end{array}\tag{18}
$$

where $\beta = \hat { A } ^ { - 1 } z , \mu ^ { \prime } = \beta / ( 1 - z ^ { T } \beta )$ and $\alpha ^ { \prime } { = } I { + } \mu ^ { \prime } z ^ { T }$ . We observe that the parameters β, μ′, and α′ are also the functions of the instance z. Besides, each parameter also has a single z. The decomposition course in Eq. (18) is very similar to Eq. (8).

Then, comparing with the derivation in Eq. (9), if the current sample matrix Z includes an outdated instance z, we can obtain the update of ω^ for deleting z as below,

$$
\begin{array}{r l} \tilde {\boldsymbol {\omega}} & = \alpha^ {\prime} \Big (\hat {A} ^ {- 1} Z ^ {T} L - \hat {A} ^ {- 1} z l \Big) \\ & = \alpha^ {\prime} (\hat {\boldsymbol {\omega}} - \beta l) \\ & = \Big (I + \mu^ {\prime} z ^ {T} \Big) (\hat {\boldsymbol {\omega}} - \beta l) \\ & = (\hat {\boldsymbol {\omega}} - \beta l) + \mu^ {\prime} z ^ {T} (\hat {\boldsymbol {\omega}} - \beta l) \\ & = (\hat {\boldsymbol {\omega}} - \beta l) + z ^ {T} (\hat {\boldsymbol {\omega}} - \beta l) \mu^ {\prime} \\ & = v ^ {\prime} + z ^ {T} v ^ {\prime} \mu^ {\prime}, \end{array}\tag{19}
$$

where $\mathbf { \Delta } \mathbf { v } ^ { \prime } = { \hat { \omega } } - \beta l .$ . Note that the parameters $z ^ { T } \hat { \omega } , z ^ { T } \beta$ and l are all scalars.

Obviously, Eq. (19) is also similar to Eq. (9). So, Eqs. (18) and (19) show that the proposed IMISVM method can be modi<sup>fi</sup>ed for deleting outdated samples without matrix inversion. To achieve this aim, we only need to interchange the operators + and − in the corresponding formulas. Since this paper intends to solve the problems of incremental learning, we will omit detailed procedures for decremental learning.

## 4. Description of IMISVM algorithm

The detailed pseudocode of IMISVM is described in the Algorithm 1. This algorithm mainly calculates and updates two parameters $A ^ { - 1 }$ and ω, which correspond to steps 6 and 7, and steps 9 to 11. The main process of IMISVM works as follows. Given a sample matrix X which contains n samples in d dimensional spaces, and the label vector $L \in { \cal R } ^ { n \times 1 }$ , IMISVM algorithm incrementally fetches the instance-label pair bz,l> and updates the weight vector ω.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Pseudocode of IMISVM algorithm
Input:
Training set &lt;X,L&gt;.
Output:
Weight vector ω.
1 [n,d]=size(X);/* Get the size of the sample matrix X. */
2 Z=[X,-e];
3 for i=1 to n do
4 z=Z$_{i}^{T}$ and l=L$_{i}$;/* Get $i^{th}$ instance from $i^{th}$ row of Z and its label from L. */
5 if i==1 then
6 Calculate A$^{-1}$ by Eq. (6);
7 ω=A$^{-1}$zl;
8 else
9 β=A$^{-1}$z, μ=β/(1+z$^{T}$β) and v=ω+βl;
10 Update A$^{-1}$ by A$^{-1}$-μβ$^{T}$;
11 Update ω by v-z$^{T}$vμ;
12 end if
13 end for
</div>

Once the <sup>fi</sup>rst instance z is acquired, step 6 adds the regularization term λI in Eq. (6) to produce nonsingular A and calculate $A ^ { - 1 }$ by a rank-one modi<sup>fi</sup>cation. In step 7, IMISVM initializes the weight vector ω. When more samples are obtained, IMISVM updates $A ^ { - 1 }$ and ω according to the formulas listed from steps 9 to 11.

It is obvious that the IMISVM algorithm does not invert any matrix. This strategy, on the one hand, can update $A ^ { - 1 }$ and ω in a fast way. On the other hand, for nearly singular matrices, it is more numerically stable than explicitly calculating the matrix inversion. Moreover, by avoiding the inversion operation, IMISVM becomes competent to solve the problems with large sizes. Besides, IMISVM algorithm can estimate the initial parameter values based on the <sup>fi</sup>rst instance, which means that, at the beginning of incremental learning, IMISVM has no rigorous constraint on the number of samples: one is enough. As the samples increase, IMISVM is capable of getting better prediction accuracy. When the samples are enough to produce nonsingular matrix $I - \lambda A ^ { - 1 }$ <sup>1</sup>, the term λI is eliminated to speed up the convergence. To reduce the times for estimating the singularity of $I - \mathsf { M } ^ { - 1 }$ , we introduce a control parameter κ such that the current number of samples n must not be smaller than $\kappa ( d + 1 ) ( \kappa \geq 1 )$ . In the following experiments, this parameter is used together with the matrix $I { - } \lambda \hat { A } ^ { - 1 }$ to judge the suf<sup>fi</sup>ciency of samples.

## 5. Experiments

PSVM has similar performance (w.r.t. the prediction accuracy) to the standard SVM classi<sup>fi</sup>ers, but it is more ef<sup>fi</sup>cient than other SVMs such as $S V M ^ { l i g h t } [ 1 3 ] ,$ SSVM [16], LSVM [21], and SMO [8,24]. Since IMISVM is an incremental version of PSVM, this paper mainly compares IMISVM with ISVM. Besides, IMISVM is also compared with SVCM. The experimental results on synthetic data, real world UCI data set, USPS and biological data demonstrate the performance of IMISVM.

## 5.1. Benchmark data set

Four types of data sets (one synthetic and three real-world data sets) for binary classi<sup>fi</sup>cation problems are employed in our experiments. The descriptions of these data sets are as follows.

NDC data set is produced by using the normally distributed clustered generator (NDC) [23]. This generator can control the mean and covariance matrix of produced samples and hence get the adjustable dimensions as well as linear separability.

Mushroom data set. The Mushroom data set is collected from UCI Machine Learning Repository [22]. These data record 22 attributes of mushrooms, such as shapes, colors, odors and habitats. Each attribute includes at least two and at most twelve values. Binary codes are used to depict whether the values of attributes exist or not. Then, these attributes are extended to 117 dimensions. This data set consists of 4 208 positive (or edible) samples (51.8%) and 3 916 negative (or poisonous) samples (48.2%). So, the learning task is to predict if one kind of mushroom is edible or not (i.e., it is a binary class problem). Furthermore, in order to compare the algorithm performance with respect to different data dimensions, these feature vectors are reduced to $d = 1 0$ by NNMF (non-negative matrix factorization) method [17].

USPS Digit data sets. The Digit data sets are collected from the US Postal Service (USPS) database which includes the images of handwritten digits $1 , 2 , . . . , 9$ and 0, with about 7000 samples for type of digits [15]. The digits are translated and scaled so that each one has a <sup>fi</sup>xed size $2 8 \times 2 8 .$ . The corresponding pixel vectors, with the length of 784, are directly used as features here. For the same purpose as that on Mushroom data set, these feature vectors are reduced to $d = 1 0$ and 100 by NNMF. The images of three pairs: 4 and 9, 2 and 7, 3 and 8 are visually similar, respectively. So, these pairs are chosen to compare the classi<sup>fi</sup>cation performance between IMISVM and ISVM. Another reason for selecting these pairs is that each pair of digits has the similar numbers of samples in both training and test sets, $\mathrm { i . e . , }$ , the data sets are relatively balanced. Otherwise, the weighting method of samples can be adopted [10]. Table 1 speci<sup>fi</sup>es the three pairs of digits, where the positive and negative samples are abbreviated as PS and NS, respectively.

TIS data set. The TIS data set consists of 13375 samples each of which has 927 dimensions [19]. The learning task of this data set is to discover the gene Translation Initiation Site (TIS) from the DNA sequence. In other words, to discover the site where RNA polymerase binds to the DNA sequence and generates a copy of the DNA (in the form of messenger RNA, mRNA) which contains the protein coding information. Finding TIS is a major step in gene discovery and gene function analysis. The 927 dimensions of the TIS data set include following features: (1) the positions of the nucleotides adenine (denoted by A), thymine (denoted by T), and guanine (denoted by G) (although a DNA sequence contains four types of nucleotides, a TIS only contains A, T, and $G ) ; ( 2 )$ the amino acids, which are translated version of every three nucleotides; and (3) the pair of amino acids.

Detailed information of digit images.

<table><tr><td>Positive samples (PS)</td><td>Negative samples (NS)</td><td colspan="2">Training sets</td><td colspan="2">Test sets</td></tr><tr><td></td><td></td><td>No. of PS</td><td>No. of NS</td><td>No. of PS</td><td>No. of NS</td></tr><tr><td>4</td><td>9</td><td>5842</td><td>5949</td><td>0982</td><td>1009</td></tr><tr><td>2</td><td>7</td><td>5958</td><td>6265</td><td>1032</td><td>1028</td></tr><tr><td>3</td><td>8</td><td>6131</td><td>5851</td><td>1010</td><td>0974</td></tr></table>

The class label of the TIS data set is to indicate whether one example is true transcription initiation site or not (i.e., it is also a binary class problem). To demonstrate the algorithm performance with respect to the increasing data dimensions, we also reduce the dimensions by NNMF.

## 5.2. Experimental results

When training the ISVM and IMISVM classi<sup>fi</sup>ers, the NDC, Mushroom and TIS data sets are partitioned into two parts: 80% of them are randomly selected for training and the rest 20% are used for test.

a) Runtime about dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/4d046b688a277436a3d2df581605d46b694b02cd1d3b4a513da2fc7b55dbd51c.jpg)

b) Runtime about samples  
![](/api/attachments/F64TG7UK/fulltext/images/f266da5a0e8116d9869e60549f5cf700840a30815ce12e88a6cd2957c78adc72.jpg)

c) A local enlargement of (b)  
![](/api/attachments/F64TG7UK/fulltext/images/7896f8b255afec4874695a9ddf509344e31a20b7a6d4bc4a003350daee12f9b3.jpg)  
Fig. 3. Comparisons of average runtime of ten experiments on NDC data set.

The average experimental results of ten times are reported in the following <sup>fi</sup>gures. Additionally, all experiments are performed in Matlab 6.5 software, on a PC with 2.80 GHz CPU and 2 GB memory.

## 5.2.1. Comparisons w.r.t. efficiency

The computational costs of IMISVM and ISVM are related to two factors: the numbers of the dimensions and samples. The results with one <sup>fi</sup>xed factor are illustrated in Fig. 3 which also shows the results of SVCM. These experiments are conducted on the synthetic data generated from NDC [23]. When the training set contains 160 positive and 160 negative samples as well as the dimension increases from 10 to 100 with the step size of 10, Fig. 3 (a) reports the computational costs of IMISVM and ISVM which are actually quadratic and cubic functions of the data dimension, respectively. The time complexity of SVCM is an approximately increasing function of the number of dimensions, but the runtime of SVCM is much larger than that of ISVM and IMISVM. When d equals 10 and the training set increases one instance at a time from 1 to 320, Fig. 3 (b) shows that the computational costs of IMISVM and ISVM are two approximately linear functions with different slopes (Please refer to Fig. 3 (c) for clear view). The curve from SVCM is also an approximate line with much bigger slope than those of ISVM and IMISVM. In the three sub<sup>fi</sup>gures, the curves of IMISVM are under those of ISVM, which re<sup>fl</sup>ects that IMISVM is more ef<sup>fi</sup>cient than ISVM when the dimensions or the samples increase. Besides, the test accuracies are controlled by the input parameters of NDC [23]. When the NDC data set has 200 dimensions, for one class, its mean and covariance matrix are zero and I respectively, for the other class, the two statistics are $1 / \sqrt { 1 0 }$ and $2 ^ { 2 } I$ respectively, the average accuracy of ISVM is equal to that of the basic

a) Runtime for 10 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/b3ef5fc51d2a6018fca20ca67daa400dea05463630ea6b166dfa487db2949732.jpg)

b) Runtime for 117 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/c7b4054d95bef0522adfd9d4dc93466d73910f836c4a64de3b331c2794dc3636.jpg)  
Fig. 4. Comparisons of average runtime of ten experiments on UCI Mushroom data set.

IMISVM and it is 80.25%, it is 82.5% for SVCM. These results show that SVCM has the similar prediction accuracies to those of ISVM and IMISVM. However, on this small-scale data set, SVCM has much higher computational cost than ISVM and IMISVM. Accordingly, we only compare ISVM with IMISVM on middle-scale Mushroom, Digit and TIS and large-scale synthetic data sets further.

Fig. 4 reports the runtime performance comparisons on Mushroom data set. Fig. 4 (a) and (b) shows the results of d=10 and d=117, respectively. Each sub<sup>fi</sup>gure indicates that when the samples increase, IMISVM is more ef<sup>fi</sup>cient than ISVM. Moreover, when the dimensions increase, the increment of runtime of IMISVM is much smaller than that of ISVM.

a) Runtime for 10 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/890b7c63805d8ce0f36af30b6a66297837d84d27121af49f2011c468aa896230.jpg)

b) Runtime for 100 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/849cbe0906b5efb697c0146f32b38ffccd436ae171f4c4b617fbbd21c8cf63c6.jpg)

c) Runtime for 784 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/38e43bb5c817ba06798d7a0ac55a26d1bba4f8e5e4af272858d558610ceee0cb.jpg)  
Fig. 5. Comparisons of average runtime of ten experiments on USPS Digit data sets 4 and 9.

Fig. 5 further reports the results on digit pair 4 and 9 which have 11791 training samples. Fig. 5 (a), (b) and (c) shows the results of d=10, d=100 and $d = 7 8 4$ (without dimensionality reduction), respectively. Compared with Fig. 4, Fig. 5 demonstrates the similar results. This similarity indicates that IMISVM is more practical for incremental learning than ISVM. Because the computational costs of 2 and 7, and 3 and 8 are similar to those of 4 and 9, it is unnecessary to display their results again. Additionally, the average prediction accuracies of the three pairs of digit images are 92.43% (d=10), 95.82% $( d = 1 0 0 )$ and 96.67% $( d = 7 8 4 )$ , which implies that when the dimensions increase, the basic IMISVM and ISVM can obtain better accuracies.

a) Runtime for 10 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/5a78590793345254429210aa079fc220110730e99a5eae8ec6a8b9b32cd9af43.jpg)

b) Runtime for 100 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/73e1e8cce152831b5d2646bd77aafc7772971eb82d336d55106f6665b5eb2c51.jpg)

c) Runtime for 927 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/6df069dce1e17ee8a8bb03be4d7b1af12f7d8d60bacf9e10129e9b9005717274.jpg)  
Fig. 6. Comparisons of average runtime of ten experiments on TIS data set.

Table 2  
Detailed information of data blocks.

<table><tr><td>Data sets</td><td>Dimension (d)</td><td>No. of each instance block (n&#x27;)</td><td>No. of block</td><td>No. of total instance (n)</td></tr><tr><td>DS_1</td><td>0150</td><td>200000</td><td>005</td><td>1000000</td></tr><tr><td>DS_2</td><td>0300</td><td>100000</td><td>010</td><td>1000000</td></tr><tr><td>DS_3</td><td>0600</td><td>050000</td><td>020</td><td>1000000</td></tr><tr><td>DS_4</td><td>1200</td><td>020000</td><td>050</td><td>1000000</td></tr><tr><td>DS_5</td><td>2400</td><td>010000</td><td>100</td><td>1000000</td></tr><tr><td>DS_6</td><td>4800</td><td>005000</td><td>200</td><td>1000000</td></tr></table>

More experiments are conducted on TIS data set and the results are illustrated in Fig. 6 which also shows the similar results to those in Figs. 5 and 4. Fig. 6 (c) is for the runtime without dimensionality reduction, which reveals that, although TIS data set contains a smaller number of samples, it needs more runtime because of the higher dimensions than the digit pair 4 and 9. In addition, the basic IMISVM

## a) Runtime for 150 dimensions

![](/api/attachments/F64TG7UK/fulltext/images/9a9c2d2ea51eff7841e6cce368ff7f4db68ad742818673cd1f7af658f149c355.jpg)  
(c) Runtime for 600 dimensions

b) Runtime for 300 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/f6909f19239a234eb9071146273cad2627a458c8992924b3bf13969ef1c9caa1.jpg)

![](/api/attachments/F64TG7UK/fulltext/images/3ac8323275bb790067e73c322443160a371eecb2b35730a26c2ab6c0ed0fa8ed.jpg)

d) Runtime for 1 200 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/51e0cbe8e84dc5c38d96506b501d3c3f5f48b97640cc4b686548fcb5fcffbc8e.jpg)

e) Runtime for 2 400 dimensions  
![](/api/attachments/F64TG7UK/fulltext/images/905da09038b0a2bf1e4c97d1fadfe7412ccbe47a635ed55e9b883b6c503d1d46.jpg)  
Fig. 7. Comparisons of runtime of on DS\_ 1 to DS\_ 5 data sets

and ISVM have the same prediction accuracies, when the dimensions increase, they are 71.56%, 75.22% and 76.92%, respectively.

To show the performance of IMISVM for much higher dimensional and larger data sets than those used above, again, we use NDC [23] to produce the synthetic data. Due to the limit of the memory of our computer, in the extreme case, IMISVM method can deal with the samples with the dimension $d = 1 0 ^ { 8 }$ , and the samples can be put in the memory one by one. By contrast, to solve this kind of data problem, ISVM must invert the regularized cross-product matrix ${ \lambda } I { + } Z ^ { T } Z$ with the size of $1 0 ^ { 8 } \times 1 0 ^ { 8 }$ . For the limited memory, it is impossible for ISVM to make it. By special trial, the allowable maximal size of the invertible matrix here is about d×d where $d = 5 \times 1 0 ^ { 3 }$ . To compare IMISVM with ISVM, we set the dimension set {150,300, 600,1200,2400,4800} and use NDC [23] to produce a million samples for each dimension. Also, for the positive samples, the mean and covariance matrix are zero and I respectively, for the negative ones, the two statistics are $1 / \sqrt { 1 0 }$ and 2<sup>2</sup>I respectively. In fact, even though the dimension number m equals 150, the NDC program can not produce the total data set in one time. So, we have to produce several “data blocks” for each data set and Table 2 shows the size of each block in detail. We can use the data blocks to simulate the frequent I/O operation and record the corresponding time. In other words, the runtime here includes two parts: the time for reading the samples (I/O) and the time for computing without I/O.

Because IMISVM has the same prediction accuracy as that of ISVM, we mainly compare their ef<sup>fi</sup>ciencies in the following experiments. When one block data is input, the corresponding time for reading is about 0.35 s. Compared with the computation time, the reading time is too small and cannot obviously shown in Figs. 7 and 8. Note that, the runtime here is only for one experiment. Even so, the total runtime for 150 to 2400 dimensions is about 1.3 and 31.1 days for IMISVM and ISVM, respectively. To observe the results of 4800 dimensions, <sup>fi</sup>rstly, we record the runtime for 5000 samples and show it in Fig. 8(a). Fig. 8(a) indicates that, for 5000 samples, the runtime of IMISVM and ISVM is 27.47 min and 23.15 h, respectively. From their time complexities and the experimental results shown above, we know that their runtime is directly proportional to the numbers of samples. Then, Fig. 8(b), depicting the predicted results for 1000000 samples, implies that the predicted runtime for IMISVM and ISVM is about 3.82 days and 192.90 days, respectively. Further, on all 1000000 samples, we use quadratic and cubic curves to <sup>fi</sup>t the runtime of different dimensions for IMISVM and ISVM respectively and describe the results in Fig. 8(c). Fig. 8(c) shows that the proposed method IMISVM has much smaller runtime than ISVM. The corresponding curve of IMISVM is visibly distinct from that of ISVM for high dimensional data. In a word, Figs. 7 and 8 demonstrate that IMISVM has much higher ef<sup>fi</sup>ciency than ISVM, especially for higher dimensions and larger scale samples.

## 5.2.2. Comparisons w.r.t. convergence speed

The analysis in Section 2 means that, only when the samples are not enough to produce nonsingular cross-product matrix, the regularization term is necessary.

Once this situation is reversed, this term can be safely eliminated. Furthermore, the elimination can speed up the convergence of IMISVM. In the following experiments, the control parameter κ is set to 4. This parameter is used together with the matrix $I { - } { \lambda } \hat { A } ^ { - 1 }$ to judge the suf<sup>fi</sup>ciency of samples. These experiments are conducted on Mushroom, Digit and TIS data sets to show the effectiveness of eliminating the regularization term λI. Since the basic IMISVM and ISVM have identical accuracy and the runtime is similar to that shown in Figs. 4, 5 and 6, we focus on the comparison of accuracy on IMISVM (after eliminating λI) and ISVM, the <sup>fi</sup>nal results are illustrated in Fig. 9. All the sub<sup>fi</sup>gures in Fig. 9 re<sup>fl</sup>ect that this elimination can retain (or improve) the prediction accuracy and speed up the convergence of IMISVM, which is most obvious in Fig. 9 (e). Moreover, this trend is retained as the samples increase.

a) Runtime for 5 000 samples  
![](/api/attachments/F64TG7UK/fulltext/images/bc0c530047465b5c95028bdbdca974e2380fb0ea502669fca301bd83639422dc.jpg)

b) Runtime for 1 000 000 samples  
![](/api/attachments/F64TG7UK/fulltext/images/bd7244f6b9f0acfd329f21e306882d763c3c2324a6af95c6cf4f9c83af6e52d6.jpg)

(c) Runtime of di erent dimensions for 1 000 000 samples  
![](/api/attachments/F64TG7UK/fulltext/images/6cf23f3d5157f2467e00b297cf77d42191b0f5a69fa46350823277b91568009c.jpg)  
Fig. 8. Comparisons of runtime of on DS\_ 6 data set.

The experiments above verify that ISVM and IMISVM are more ef<sup>fi</sup>cient than SVCM. Furthermore, IMISVM is more ef<sup>fi</sup>cient than ISVM, especially when the dimensions or samples increase. Besides, the IMISVM has the same or better prediction accuracies than ISVM. In addition, the elimination of regularization term accelerates the convergence of IMISVM. These results imply that IMISVM is a competitive choice to acquire satisfactory ef<sup>fi</sup>ciency in high dimensional spaces or for large-scale data.

a) Comparison on Mushroom  
![](/api/attachments/F64TG7UK/fulltext/images/a608a9386f251da97f58477885e86f75d67fd3904911a1a0d7efe29d80ff7c1b.jpg)

b) Comparison on Digits 4 and 9  
![](/api/attachments/F64TG7UK/fulltext/images/9f65fccff3deb0c208c78b429611e81f15e8f7fc13b42b11f4116c8ba86f2b19.jpg)

c) Comparison on Digits 2 and 7  
![](/api/attachments/F64TG7UK/fulltext/images/508fcfa1e6e7fb4fc7bed8581f2abbff03276cd16c57b94fc1831fdffb03bc04.jpg)

d) Comparison on Digits 3 and 8  
![](/api/attachments/F64TG7UK/fulltext/images/fa48bd6fa8e3d479d891c309955612312b9ae8c612bd75bfa1daa1965f423205.jpg)

![](/api/attachments/F64TG7UK/fulltext/images/97a706178a8f2dcc0feeb63e018283c22a5dfc18d584f39533d10aba761d389c.jpg)  
Fig. 9. Comparisons of average prediction accuracies of ten experiments on UCI Mushroom, USPS Digit and biological TIS data (with the elimination of regularization term λI for IMISVM, d=10).

## 6. Conclusion

In this paper, we proposed a fast inverse matrix-free incremental classi<sup>fi</sup>er (IMISVM) with the following four properties for effective learning for large-scale high-dimensional data: 1) the model size of IMISVM is a constant which is independent of the data sizes; 2) IMISVM employs the Sherman–Morrison formula in the regularized least squares learning and obtains a linear function for model updating, thus, IMISVM has one order of magnitude less time complexity, with respect to the data dimensionality, than ISVM; 3) compared to ISVM classi<sup>fi</sup>er, IMISVM has the same or better prediction accuracy; and 4) the elimination of regularization term speeds up the convergence of IMISVM. All the above properties make IMISVM more ef<sup>fi</sup>cient for dealing with high-dimensional and large-scale data. Experimental results on synthetic and real-world data (including high dimensional biological data and synthetic data) demonstrate the advantages of the IMISVM in comparison with its peer incremental SVMs.

This paper mainly focuses on two-class classi<sup>fi</sup>cation problems. Extending the IMISVM to handle multi-class classi<sup>fi</sup>cation problems is an important research topic, we intend to address it in the future.

## Acknowledgments

We thank anonymous reviewers for their very useful comments and suggestions. This work was partially supported under Australian Research Council's Future Fellowship funding scheme (No. FT100100971), and by National 973 Program (No. 2010CB327906), the National Science Foundation of China (NSFC) Grants (No. 61170223, and No. 60875003), the China Postdoctoral Science Foundation (CPSF) Grant (No. 2011M501189), the State Key Laboratory Program Grant (No. RCS2009K003), the National High Technology Research and Development Program of China (No. 2009AA01A346).

## References

[1] M.S. Bartlett, An inverse matric adjustment arising in discriminant analysis, Annals of Mathematical Statistics 22 (1) (1951) 107–111.

[2] H. Bentounsi, M. Batouche, Incremental support vector machines for handwritten arabic character recognition, Proceedings of the 1st International Conference on Information and Communication Technologies: From Theory to Applications 2004, pp. 477–478.

[3] C.M. Bishop, Pattern Recognition and Machine Learning, Springer, New York, 2006. [4] G. Cauwenberghs, T. Poggio, Incremental and decremental support vector machines learning, Advances in Neural Information Processing Systems, 2001, pp. 409–415.

[5] S. Cheng, F.Y. Shih, An improved incremental training algorithm for support vector machines using active query, Pattern Recognition 40 (2007) 964–971.

[6] T.N. Do, J.D. Fekete, Large scale classi<sup>fi</sup>cation with support vector machine algo rithms, Procedings of the 6th International Conference on Machine Learning and Applications, 2007, pp. 7–12.

[7] P. Domingos, G. Hulten, Mining high-speed data streams, Proceedings of the 6th ACM International Conference on Knowledge Discovery and Data Mining, 2000, pp. 71–80

[8] G. Fung, O.L. Mangasarian, Proximal support vector machine classi<sup>fi</sup>ers, Proceeding of the 7th ACM International Conference on Knowledge Discovery and Data Mining 2001, pp. 77–86.

[9] G. Fung, O.L. Mangasarian, Incremental support vector machine classi<sup>fi</sup>cation, Proceedings of the 2nd SIAM International Conference on Data Mining, 2002, pp. 247–260.

[10] G. Fung, O.L. Mangasarian, Multicategory proximal support vector machine classi<sup>fi</sup>ers, Machine Learning 59 (1–2) (2005) 77–97.

[11] W.W. Hager, Updating the inverse of a matrix, SIAM Review Archive 31 (2) (1989) 221–239.

[12] K. Hyunsoo, P. Haesun, Incremental and decremental least squares support vector machine and its application to drug design, Proceedings of the 3rd IEEE International Conference on Computational Systems Bioinformatics, 2004, pp. 656–657.

[13] T. Joachims, Making large-scale support vector machine learning practical, Advances in Kernel Methods-Support Vector Learning (1999) 169–184.

[14] R. Klinkenberg, T. Joachims, Detecting concept drift with support vector machines, Proceedings of the 17th International Conference on Machine Learning, 2000, pp. 487–494.

[15] Y. LeCun, L. Bottou, Y. Bengio, P. Haffner, Gradient-based learning applied to document recognition, Proceedings of the IEEE 86 (11) (1998) 2278–2324 Available online: http://yann.lecun.com/exdb/mnist/.

[16] Y.J. Lee, O.L. Mangasarian, SSVM: a smooth support vector machine, Computational Optimization and Applications 20 (1) (2001) 5–22.

[17] D.D. Lee, H.S. Seung, Learning the parts of objects by non-negative matrix factorization, Nature 401 (6755) (1999) 788–791.

[18] Q. Li, L. Jiao, Y. Hao, Adaptive simpli<sup>fi</sup>cation of solution for support vector machine, Pattern Recognition 40 (2007) 972–980.

[19] H. Liu, L. Wong, Data mining tools for biological sequences, Journal of Bioinformatics and Computational Biology 1 (1) (2003) 139–167 Available online: http://leo.ugr.es/elvira/DBCRepository/SequenceData/TIS.html.

[20] Y. Lu, V.P. Roychowdhury, Parallel randomized sampling for support vector machine (SVM) and support vector regression (SVR), Journal of Knowledge and Information Systems 14 (2) (2008) 233–247.

[21] O.L. Mangasarian, D.R. Musicant, Lagrangian support vector machines, Journal of Machine Learning Research 1 (2000) 161–177.

[22] P.M. Murphy, D.W. Aha, UCI Repository of Machine Learning Databases. Available online: http://archive.ics.uci.edu/ml/datasets.html 1992

[23] D.R. Musicant, NDC: Normally Distributed Clustered DatasetsAvailable online: http://www.cs.wisc.edu/musicant/data/ndc/1998

[24] J. Platt, Sequential minimal optimization: a fast algorithm for training support vector machines, Adyances in Kernel Methods-Support Vector Learning (1999) 185-208.

[25] S. Rüping, Incremental learning with support vector machines, Proceedings of the 1st International Conference on Data Mining, 2001, pp. 641–642.

[26] J. Schlimmer, R. Granger, Incremental learning from noisy data, Machine Learning 1 (3) (1986) 317–354.

[27] J.A.K. Suykens, J. Vandewalle, Least squares support vector machine classi<sup>fi</sup>ers, Neural Processing Letters 9 (3) (1999) 293–300.

[28] J.A.K. Suykens, T.V. Gestel, J.D. Brabanter, B.D. Moor, J. Vandewalle, Least Squares Support Vector Machines, World Scienti<sup>fi</sup>c Publishing Company, Singapore, 2002

[29] N.A. Syed, H. Liu, K.K. Sung, Handling concept drifts in incremental learning with support vector machines, Proceedings of the 5th ACM International Conferene on Knowledge Discovery and Data Mining, 1999, pp. 317–321.

[30] N.A. Syed, H. Liu, K.K. Sung, Incremental learning with support vector machines, Workshop on Support Vector Machine at the 16th International Joint Conference on Articial Intelligence, 1999.

[31] A.N. Tikhonov, V.Y. Arsenin, Solutions of Ill-Posed Problems, John Wiley and Sons, New York, 1977.

[32] A. Tveit, M.L. Hetland, H. Engum, Incremental and decremental proximal support vector classi<sup>fi</sup>cation using decay coef<sup>fi</sup>cients, Proceedings of the 5th International Conference on Data Warehousing and Knowledge Discovery, 2003, pp. 422–429.

[33] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer, New York, 1996.

[34] M. Woodbury, Inverting Modi<sup>fi</sup>ed Matrices, Technical Report 42, Statistical Research Group, Princeton University, Princeton, NJ, 1950.

[35] P. Zhang, X. Zhu, Y. Shi, L. Guo, X. Wu, Robust ensemble learning for mining noisy data streams, Decision Support Systems 50 (2) (2011) 469–479.

![](/api/attachments/F64TG7UK/fulltext/images/b68fae5f62e2f874001a44f7f59fe7302d68d81f4cec1b17e76f1a8e75c97657.jpg)

Zhenfeng Zhu received the B.A. and M.A. degrees at the School of Information Engineering from Zhengzhou University, Zhengzhou, China, in 2003 and 2006, respectively. He received the Ph.D. degree at the School of Computer Science, Fudan University, in July 2010. Currently, he is an assistant professor at the School of Information Engineering, Zhengzhou University. His main research interests include machine learning, pattern recognition and computer vision.

![](/api/attachments/F64TG7UK/fulltext/images/959f7901a6de68d44516c77eff03b0af3617eb58ad166b7de9e389e14744e4a2.jpg)

Xingquan Zhu received his Ph.D. degree in Computer Science from Fudan University, Shanghai China, in 2001. He is a recipient of the Australia ARC Future Fellowship and a Professor of the Centre for Quantum Computation & Intelligent Systems, Faculty of Engineering and Information Technology, University of Technology, Sydney (UTS), Australia. Dr. Zhu's research mainly focuses on data mining, machine learning, and multimedia systems. Since 2000, he has published more than 120 referred journal and conference proceedings papers in these areas. Dr. Zhu is an Associate Editor of the IEEE Transactions on Knowledge and Data Engineering (2009 – present), and a Program Committee Co-Chair for the 23rd IEEE International Conference on Tools with Arti<sup>fi</sup>cial Intelligence (ICTAI 2011) and the 9th International Conference on Machine Learning and Applications (ICMLA 2010).

![](/api/attachments/F64TG7UK/fulltext/images/915ff58ebea39fc4617907e93d4ef1961c8c8d725e850a36c2239a0237c7b1e7.jpg)

Yuefei Guo received the B.S. degree from the Department of Mathematics, East China Normal University, Shanghai, China, in 1985, and the MS and Ph.D. degrees from the Department of Computer Science, Nanjing University of Science and Technology, Nanjing, China, in 1997 and 2000, respectively. He is now an Associate Professor in the School of Computer Science, Fudan University. His research interests include pattern recognition, feature selection, computer vision and image processing.

![](/api/attachments/F64TG7UK/fulltext/images/00bacd232ef22f45afe399f4e049e90da6fd3158089ebd78c1b1048f6b1dbaa1.jpg)

Yangdong Ye received the B.S. degree in computer science from Shenyang Institute of Technology, Shenyang, China, in 1983 and the Ph.D. degree in computer science from China Academy of Railway Science, Beijing, China, in 2002 Currently he is a Professor at the School of Information Engineering, Zhengzhou University, Zhengzhou, China. His main research interests are database system, machine learning, and intelligent system.

![](/api/attachments/F64TG7UK/fulltext/images/cdebb8bbd9496715c205ab89f47fb107e5a32488ac0a05efbfcf68a049e20512.jpg)

Xiangyang Xue received the B.S., M.S., and Ph.D. degrees in communication engineering from Xidian University, Xi'an, China, in 1989, 1992, and 1995, respectively. He joined the Department of Computer Science, Fudan University, Shanghai, in May 1995. Since 2000, he has been a Full Professor, He has published more than 1o0 research papers in journals or conference proceedings. His current research interests include multimedia information processing and retrieval, pattern recognition, and machine learning. Dr. Xue is an Associate Editor of the IEEE Transactions on Autonomous Mental Development and the Journal of Computer Research and Development.
