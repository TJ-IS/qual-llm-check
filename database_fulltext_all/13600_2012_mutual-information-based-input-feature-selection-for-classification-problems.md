---
otero_id: 13600
otero_key: "RMCGNTYE"
title: "Mutual information based input feature selection for classification problems"
authors: "Shuang Cang; Hongnian Yu"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.08.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mutual information based input feature selection for classi<sup>fi</sup>cation problems

Shuang Cang <sup>a,</sup>⁎, Hongnian Yu <sup>b,1</sup>

<sup>a</sup> School of Tourism, Bournemouth University, Poole, Dorset, BH12 5BB, UK

<sup>b</sup> Faculty of Computing, Engineering and Technology, Staffordshire University, Staffordshire, ST18 0AD, UK

## a r t i c l e i n f o

Article history: Received 12 December 2011 Received in revised form 26 June 2012 Accepted 17 August 2012 Available online 25 August 2012

Keywords: Feature ranking Optimal feature set Mutual information Classi<sup>fi</sup>cation

## a b s t r a c t

The elimination process aims to reduce the size of the input feature set and at the same time to retain the class discriminatory information for classi<sup>fi</sup>cation problems. This paper investigates the approaches to solve classi<sup>fi</sup>cation problems of the feature selection and proposes a new feature selection algorithm using the mutual information (MI) concept in information theory for the classi<sup>fi</sup>cation problems. The proposed algorithm calculates the MI between the combinations of input features and the class instead of the MI between a single input feature and the class for both continuous-valued and discrete-valued features. Three experimental tests are conducted to evaluate the proposed algorithm. Comparison studies of the proposed algorithm with the previously published classi<sup>fi</sup>cation algorithms indicate that the proposed algorithm is robust, stable and ef<sup>fi</sup>cient.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The search for ef<sup>fi</sup>cient and effective algorithms of input feature selection about classi<sup>fi</sup>cation problems [7] has a long history within the <sup>fi</sup>eld of pattern recognition. Reduction of the input features set can be desirable, or essential for a number of reasons, such as reducing the complexity of building and operating a classi<sup>fi</sup>er. In addition to the computational-cost saving, feature-space reduction can also reduce the actual cost of feature collection and pre-processing, and even lead to an improvement in classi<sup>fi</sup>er accuracy.

Mutual information (MI) which is a measure of the amount of information between two random variables is symmetric and non-negative, and is zero if and only if the variables are independent. Several earlier attempts have been made to construct an ef<sup>fi</sup>cient and effective feature selection procedure based on the MI concept [2,9,12]. This paper proposes a powerful feature selection algorithm based on the MI concept to offer signi<sup>fi</sup>cant improvement over these earlier attempts. The improvements are in terms of wider applicability, as good or better performance on the example classi<sup>fi</sup>cation tasks, a reduction in computational complexity and more information produced on the speci<sup>fi</sup>c feature– feature interaction presented in a classi<sup>fi</sup>cation problem.

A number of algorithms [1,3,4,14,15,17,18,19] have been proposed for feature ranking and selecting the optimal feature space. The clamping method in [18] uses trained multi-layer perceptrons [5,10,16] to rank the relative importance, or salience, of input features. The underlying idea is that if each input feature to a pre-trained network is in turn rendered information-less (e.g., all values reset to mean) then the resulting change in classi<sup>fi</sup>cation performance (with respect to accuracy when all features take their natural values) is a measure of feature salience. The advantage of the method is that it delivers a reliable result ef<sup>fi</sup>ciently even on the noisy data. The disadvantages are that it lacks a theoretical analysis and does not expose any detail of feature interaction.

The technique developed in [17] uses the repeated partial retraining each time and a space of input features is assessed. Different feature selection techniques are proposed using distance measures in [3,15], using dependency measures in [19] and using consistency measures in [8,13]. A variety of feature-ranking techniques are reviewed in [18], and feature selection using the MI concept is discussed in [9]. As described earlier, a fundamental weakness of the above techniques is that no single best ranking may exist for a given problem.

The algorithms ‘mutual information based feature selection’ (MIFS) studied in [2] and MIFS-U (U: uniform information distribution) studied in [12] involve the redundancy parameter β which is used to account for the redundancy among input features. If $\beta = 0 ,$ the MI among input features is not taken into consideration and the algorithms select features in the order of the MI between the individual input features and the class. However, if β is chosen too large, the algorithms only include the relation among the input features, and does not include the relation between the individual input features and the class [12], thus it is a dif<sup>fi</sup>cult task to adjust the parameter β.

The Taguchi method, MIFS-U, described by Kwak and Choi [12], provides a solution to the problem of identifying important features with as few experiments as possible. Success with this method, however, relies on certain assumptions about the feature set, e.g., that in-<sup>fl</sup>uences between variables are almost equal. As we wish to tackle the feature-selection problem in general, such restricted assumptions cannot be adopted and the Taguchi method will not be considered in detail.

The ‘minimal redundancy maximal relevance’ (mRMR) method [14] is a special case of the MIFS algorithm when $\beta = 1 / | S |$ , and it has more advantages than the MIFS and MIFS-U algorithms, because no parameter β is required. This is helpful in practice because there is no clear guidance on how to determine the parameter $\beta$ for a real problem.

The ‘normalized mutual information feature selection’ (NMIFS) algorithm [9] uses the normalized MI by the minimum entropy of both features, and uses the average normalized MI as a measure of redundancy of the individual feature and the subset of selected feature. Authors [9] claimed that the NMIFS algorithm is an enhancement over the MIFS, MIFS-U and mRMR algorithms. The NMIFS also eliminates the need of a user-de<sup>fi</sup>ned parameter $\beta$ required in the MIFS and MIFS-U.

In this paper, an MI algorithm between the combinations of input features and the class, instead of the MI between pairs of features, is proposed. The parameter $\beta$ is not required in the algorithm. The mutual information feature space forward selection is applied to the proposed algorithm, certainly the mutual information feature space backwards selection algorithm can also be applied, but it is not presented here due to the limitation of space.

The previous work only uses the MI computation between single (one) feature and the target class. The major enhancement of this paper is to extend this to the MI computation between a set of features and the target class. This paper also presents a general algorithm to address the change from the continuous feature to the discrete feature for the MI computation, it is the same as in Kwak and Choi's paper [12] which is just giving the bin number $( \boldsymbol { \mathrm { e . g . 5 , } } 6 , \ldots , 1 0 )$ for continuous features.

## 2. Related works

## 2.1. Mutual information

The MI which is a measure of the dependence between the random variables is always symmetric and non-negative. It is zero if and only if the variables are independent. The mutual information [10] between two discrete random variables $U { = } ( u _ { 1 } , u _ { 2 } { , } . . . , u _ { \mathrm { k } } )$ and $V { = } \left( \nu _ { 1 } , \nu _ { 2 } { , } . . . , \nu _ { \mathrm { d } } \right)$ is de<sup>fi</sup>ned as

$$
I (U, V) = \sum_ {u} \sum_ {v} p (u, v) \log \frac {p (u , v)}{p (u) p (v)}\tag{1}
$$

where $\left( u _ { 1 } , u _ { 2 } , . . . , u _ { \mathrm { k } } \right)$ and $\left( \nu _ { 1 } , \nu _ { 2 } , . . . . , \nu _ { \mathrm { d } } \right)$ are the values of the discrete variables U and $V ,$ respectively. p(u,v) is a joint density function and p(u) and $p ( \nu )$ are the marginal density functions.

The MI between class $C = ( c _ { 1 } , c _ { 2 } , . . . , c _ { k } )$ and feature $V { = } ( \nu _ { 1 } , \nu _ { 2 } { , } { \ldots } , \nu _ { d } )$ de<sup>fi</sup>ned in Eq. (1) can be written as

$$
\begin{array}{c} I (C, V) = \sum_ {c} p (c) \sum_ {v} p (v / c) \log \frac {p (v / c)}{p (v)} \\ = \sum_ {c} p (c) \sum_ {v} p (v / c) \log p (v / c) - \sum_ {v} p (v) \log p (v) \end{array}\tag{2}
$$

For simplicity, all continuous variables are transformed into the discrete features in order to use Eq. (2) which is easy to work out.

## 2.2. MIFS, MIFS-U, mRMR and NMIFS algorithms

## 2.2.1. MIFS algorithm

The MIFS [2] algorithm is a greedy selection algorithm that uses the MI between only two variables — the MI between one single variable and another single variable. Also a parameter $\beta$ involved in the algorithm is the redundancy parameter and is used to approximate the redundancy among input features and is to be determined. The algorithm MIFS is described as follows:

1) (Initialization): set F ← initial set of n features, $F { = } \{ f _ { 1 } , f _ { 2 } , { \ldots } f _ { n } \}$ , initial select feature set $S {  } \{ \}$

2) Compute I(C,f ) in Eq. (2) for the output class C and each input feature $\forall f _ { i } \in F .$ (It is noted that f = V in Eq. (2).)

3) (Selection of the <sup>fi</sup>rst feature): <sup>fi</sup>nd the feature $f _ { i }$ that maximizes $I ( C ; f _ { i } )$ , and set $F  F \backslash \{ f _ { i } \} , S  \{ f _ { i } \}$ , where $F \backslash \{ f _ { i } \}$ means that delete feature $f _ { i }$ from F.

4) (Greedy selection) repeat until the desired number of features are selected.

a) (Computation of the MI between features):

For all pairs of features $\left( f _ { i } f _ { s } \right)$ where $f _ { i } \in F f _ { s } \in S ,$ compute $I ( f _ { i } f _ { s } )$

b) (Selection of the next feature): Choose the feature f ∈F that maximizes $\begin{array} { r } { G = I ( \boldsymbol { C } ; f _ { i } ) - \beta \sum _ { f _ { s } \in S } I ( f _ { i } ; f _ { s } ) } \end{array}$ Set $F  F \backslash \{ f _ { i } \} , S  S \cup \{ f _ { i } \}$

## 2.2.2. MIFS-U algorithm

The MIFS-U [12] algorithm is a modi<sup>fi</sup>cation of the MIFS algorithm. The algorithm only changes b) in step 4) as follows:

b): Choose the feature $f _ { i } \in F$ that maximizes $G = I ( C ; f _ { i } ) - \beta$ $\textstyle \sum _ { f _ { \mathfrak { c } } \in S } I ( f C ; f _ { s } ) / H ( f _ { s } ) I ( f _ { i } ; f _ { s } ) ;$ <sup>ð Þ ð Þ ð Þ</sup>where H(f ) is the entropy of f . Set $F  F \backslash \{ f _ { i } \} , S  S \cup \{ f _ { i } \} .$

## 2.2.3. mRMR algorithm

The mRMR [14] algorithm is a modi<sup>fi</sup>cation of the MIFS-U algorithm. The algorithm only changes b) in step 4) as follows:

b): Choose the feature $f _ { i } \in F$ that maximizes $\begin{array} { r } { G = I ( C ; f _ { i } ) - \bigg ( \frac { 1 } { | S | } \bigg ) } \end{array}$ $\textstyle \sum _ { f _ { s } \in S } I ( f _ { i } ; f _ { s } )$ <sup>ð Þ</sup>Set F ← F \ {f }, S ← S ∪ {f }.

## 2.2.4. NMIFS algorithm

The NMIFS [9] algorithm is a modi<sup>fi</sup>cation of the mRMR algorithm. The algorithm only changes b) in step 4) as follows:

b): Choose the feature $f _ { i } \in F$ that maximizes $\begin{array} { r } { G = I ( C ; f _ { i } ) - \bigg ( \frac { 1 } { | S | } \bigg ) } \end{array}$ $\begin{array} { r l } & { \sum _ { f _ { s } \in S } I ( f _ { i } ; f _ { s } ) / \operatorname* { m i n } \{ H ( f _ { i } ) , H ( f _ { s } ) \} } \\ & { \mathrm { S e t } \ F \gets F \backslash \{ f _ { i } \} , S \gets S \cup \{ f _ { i } \} . } \end{array}$

3. The proposed algorithm — ‘normalized mutual information feature selection-feature space 2’ (NMIFS-FS2)

The proposed algorithm normalizes the mutual information feature selection using the feature space that contains 2 features, and is called ‘normalized mutual information feature selection-feature space 2’ (NMIFS-FS2). The NMIFS-FS2 algorithm is a modi<sup>fi</sup>cation of the NMIFS algorithm. However it uses the MI between the combinations of input features and the class instead of MI between the pairs of features used in the NMIFS. It does not require a parameter $\beta$ to be <sup>fi</sup>xed in the algorithm.

The NMIFS-FS2 algorithm changes b) in step 4) as follows:

b): Choose the feature $f _ { i } \in F$ that maximizes

$$
G = I (C; f _ {i}) - \left(\frac {1}{\left| S _ {s _ {m} s _ {n}} \right|}\right) \sum_ {f _ {s _ {m}} f _ {s _ {n}} \in S} I \left(f _ {i}; f _ {s _ {m}} f _ {s _ {n}}\right) / \min \left\{H \left(f _ {i}\right), H \left(f _ {s _ {m}}\right), H \left(f _ {s _ {n}}\right) \right\}.
$$

$$
\text { Set } F \leftarrow F \backslash \{f _ {i} \}, S \leftarrow S \cup \{f _ {i} \}.\tag{3}
$$

In Eq. $( 3 ) , S _ { s _ { m } s _ { n } }$ is the cardinality of all pairs of S set, and $I ( f _ { i } ; f _ { s _ { m } } f _ { s _ { n } } )$ is the MI between the feature space $I ( f _ { s _ { m } } f _ { s _ { n } } )$ and the individual feature $f _ { i \cdot }$

Next, the process of working out the information probability space for the feature space F is presented. Suppose that there are $n _ { i }$ discrete values $\left( \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { n _ { i } } \right)$ for each individual feature $f _ { i }$ and the probability corresponding to each discrete value $\nu _ { j } \mathrm { i } s p _ { v _ { j } }$ . The information probability space for each individual feature $f _ { i }$ is

$$
I P _ {f _ {i}} = \left[ \begin{array}{c c c c c} v _ {1} & \dots & v _ {j} & \dots & v _ {n _ {i}} \\ p _ {v _ {1}} ^ {(i)} & \dots & p _ {v _ {j}} ^ {(i)} & \dots & p _ {v _ {n _ {i}}} ^ {(i)} \end{array} \right].\tag{4}
$$

The values corresponding to the feature space F are all combinations of the discrete values chosen from all individual features. The information probability space for the feature space F can be written as $I P _ { F } = \left| \tilde { \nu } _ { 1 } \cdots \tilde { \nu } _ { j } \cdots \tilde { \nu } _ { m } \ \tilde { p } _ { \nu _ { 1 } } \cdots \tilde { p } _ { \nu _ { i } } \cdots \tilde { p } _ { \nu _ { m } } \right|$ , where $( \tilde { \nu } _ { 1 } , \tilde { \nu } _ { 2 } , . . . , \tilde { \nu } _ { j } , . . . , \tilde { \nu } _ { m } )$ indi-<sup>¼</sup>cates the values for the feature space $F ,$ and $\tilde { P } _ { \nu _ { i } } ( 1 \leq j \leq m )$ are the probabilities corresponding to the values ${ \tilde { \nu } } _ { j } .$ For example, the data set A contains the two features $f _ { 1 }$ and $f _ { 2 }$ with values $( \nu _ { 1 } , \nu _ { 2 } ) = ( 0 , 1 )$ respectively, and the data set A is $\begin{array}{c} \begin{array} { c c c c c c c c c } { f _ { 1 } } \\ { f _ { 2 } } \end{array} \left[ \begin{array} { c c c c c c c c c c } { 0 } & { 0 } & { 0 } & { 1 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \end{array} \right]  \end{array}$ . Thus the information probability space for the feature $f _ { 1 }$ is $I P _ { f _ { 1 } } = \left[ { \begin{array} { c c } { 0 } & { 1 } \\ { 6 } & { 4 } \\ { 1 0 } & { 1 0 } \end{array} } \right]$ , and the information probability space for the feature $f _ { 2 }$ is $\bar { I } P _ { f _ { 2 } } = \left[ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { 7 } } & { { 3 } } \\ { { 0 } } & { { \frac { 1 } { 1 0 } } } \end{array} \right]$ : We can work out that the information probability space is $I P _ { f _ { 1 } \cup f _ { 2 } } =$ $\left[ { \begin{array} { c c c c } { 0 0 } & { 0 1 } & { 1 0 } & { 1 1 } \\ { { \frac { 4 } { 1 0 } } } & { { \frac { 2 } { 1 0 } } } & { { \frac { 3 } { 1 0 } } } & { { \frac { 1 } { 1 0 } } } \end{array} } \right]$ for the feature space $F = f _ { 1 } \cup f _ { 2 } = \{ f _ { 1 } , f _ { 2 } \}$ , where 00 indicates that the feature $f _ { 1 }$ has a value of 0 and the $f _ { 2 }$ has a value of $0 ,$ and 01 indicates that the feature $f _ { 1 }$ has a value of 0 and the $f _ { 2 }$ has a value of 1 and so on. We can prove that the information probability space $I P _ { f _ { 1 } \cup f _ { 2 } }$ doesn't require that all features in the feature space $F = \{ f _ { 1 } , \dot { f } _ { 2 } \}$ are independent. For example, $P _ { \{ f _ { 1 } = 0 \cup f _ { 2 } = 0 \} } = P _ { \{ f _ { 1 } = 0 \} } + P _ { \{ f _ { 2 } = 0 \} } - P _ { \{ f _ { 1 } = 0 \cap f _ { 2 } = 0 \} }$ , where $\begin{array} { r } { P _ { \{ f _ { 1 } = 0 \cup f _ { 2 } = 0 \} } = \frac { 9 } { 1 0 } } \end{array}$ $\begin{array} { r } { P _ { \{ f _ { 1 } = 0 \} } = \frac { 6 } { 1 0 } , P _ { \{ f _ { 2 } = 0 \} } = \frac { 7 } { 1 0 } , P _ { \{ f _ { 1 } = 0 \cap f _ { 2 } = 0 \} } = \frac { 4 } { 1 0 } } \end{array}$ <sup>g¼</sup>and $P _ { \{ f _ { 1 } = 0 \cap f _ { 2 } = 0 \} } \varkappa 0$

<sup>g¼ ¼ f g¼ ¼ ¼f g¼ ¼ ¼f g¼</sup>Here we only consider the feature space that contains 2 features in the proposed NMIFS-FS2 algorithm which can be extended to the feature space that contains more than 2 features, but needs a reasonable large data size. The more features are contained in the feature space; the larger data set is required in general.

We can see that the <sup>fi</sup>rst three features selected using formulas (2) and (4) are different with the rest of the features selected using formula (3), so using these two formulas does not produce the same scales of G values.

## 4. Neural networks (NN) for validation of feature selection algorithms

In order to test and compare these feature selection algorithms, a single-layer NN [5] is applied in this study. The NN is based on a linear combination of the input variables which is transformed by a nonlinear activation function, thus a linear combination of the outputs of these activation functions is constructed for the <sup>fi</sup>nal predicted outputs $\hat { y } _ { i }$ for the ith pattern. For the input dimension M vector with H hidden units of the neural networks, the output $\hat { y } _ { i }$ of the neural networks can be written as

$$
\hat {y} _ {i} = \sum_ {k = 1} ^ {H} w _ {k} ^ {(2)} g \left(\sum_ {j = 1} ^ {M} w _ {k j} ^ {(1)} f _ {i} ^ {(j)}\right)\tag{5}
$$

where $( f _ { i } ^ { ( 1 ) } , f _ { i } ^ { ( 2 ) } , . . . , f _ { i } ^ { ( M ) } )$ is the input features for the ith pattern, and $g$ is a nonlinear activation function. The common logistic sigmoid activation function $\displaystyle { g ( x ) = 1 / ( 1 + \exp ( - x ) ) }$ is used in this study. The parameters H and the weights $w _ { k j } ^ { ( 1 ) }$ , and $w _ { k } ^ { ( 2 ) }$ need to be determined by minimizing the error of output of $\dot { y } _ { i }$ in Eq. (5) and the actual true target output $y _ { i }$ using the training data set. The error function is presented in Eq. (6).

$$
E (W) = \frac {1}{2} \sum_ {i = 1} ^ {N} \left\{\hat {y} _ {i} - y _ {i} \right\} ^ {2} = \frac {1}{2} \sum_ {i = 1} ^ {N} \left\{\sum_ {k = 1} ^ {H} w _ {k} ^ {(2)} g \left(\sum_ {j = 1} ^ {M} w _ {k j} ^ {(1)} f _ {i} ^ {(j)}\right) - y _ {i} \right\} ^ {2}\tag{6}
$$

Minimizing the error function E(W) by the initial W (which might for instance be chosen at random) and then updating the weight vector by moving a small distance $\eta$ (learning rate parameter) in the W-space in the direction in which E(W) decreases most rapidly (the direction of $- \nabla _ { W } E )$ . By iterating this process as Eq. (7), eventually the weight W vector will converge to a point at which E is minimized. This point of the W value is used in Eq. (5). The training data is used to construct model (5), the validation data is used to determine the weights and the number of hidden units in Eq. (5). The test data is used to test the performance of model (5).

$$
W ^ {\mathrm{new}} = W ^ {\mathrm{old}} - \eta \frac {\partial E}{\partial W}\tag{7}
$$

The architecture of the multiple outputs NN is described in Fig. 1.

## 5. Experiment results

Three experimental tests (examples) are presented in this section to evaluate the proposed algorithm. The <sup>fi</sup>rst experimental example is well de<sup>fi</sup>ned and a similar problem is studied in [18] by using the clamping technique. The second example is studied in [9] and the last example is the heart data set from a real problem studied in [6].

For the <sup>fi</sup>rst two examples, β is chosen between 0.3 and 1 which is in the range of β value as Battiti [2] suggested (β is in the range of 0.5 and 1), and $\beta$ is chosen as 1 which is the same as the paper in [12] in the MIFS and MIFS-U algorithms for the last example. The purpose of using the different $\beta$ is to see all possibilities of the feature rankings since the best $\beta$ value is unknown for a given problem. The MIFS and MIFS-U algorithms show that more weights are added on the redundant features $\operatorname { i f } \beta$ is close to 1, which means that the algorithms consider more on the relationships between the features, and considers less on the relationships between features and outputs, vice versa.

## 5.1. Example 1: LIC1—a well defined problem

The LIC1 problem is de<sup>fi</sup>ned as

$$
\text { LIC1 } = \left\{ \begin{array}{l l} 2 & \sqrt {(x _ {1} - x _ {2}) ^ {2} + (y _ {1} - y _ {2}) ^ {2}} > l e n g t h \\ 1 & \text { otherwise } \end{array} \right..\tag{8}
$$

The input feature space is $F ^ { ( 9 ) } = [ f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 } , f _ { 5 } , f _ { 6 } , f _ { 7 } , f _ { 8 } , f _ { 9 } ] = [ x _ { 1 } , x _ { 2 } ,$ $y _ { 1 } , y _ { 2 } ,$ length, $i n _ { 6 } , i n _ { 7 } , i n _ { 8 } ,$ , in ], in is set as a dummy or irrelevant feature, and $i n _ { 7 }$ is set as $i n _ { 7 } { = } x _ { 1 } - x _ { 2 }$ which overlaps the features of $x _ { 1 }$ and $x _ { 2 }$ . Thus, the redundant feature is either $x _ { 1 }$ and x or the feature $i n _ { 7 } ,$ , because $i n _ { 7 }$ is a combination of $x _ { 1 }$ and $x _ { 2 } .$ Therefore, it is better to select $i n _ { 7 }$ and treat $x _ { 1 }$ and $x _ { 2 }$ as the redundant features. Thus $i n _ { 8 } = x _ { 1 } \times x _ { 2 }$ and $i n _ { 9 } { = } y _ { 1 } { \times } y _ { 2 }$ are the redundant features. Although the features $i n _ { 8 }$ and $i n _ { 9 }$ have relationships with the features $x _ { 1 } , x _ { 2 } ,$ $y _ { 1 }$ and $y _ { 2 } ,$ , they do not have any relationship with the class at all, consequently, the best/optimal feature space for this classi<sup>fi</sup>cation problem is $[ y _ { 1 } , y _ { 2 } ,$ length, in ] or $[ x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } ,$ length]. The feature space $[ y _ { 1 } , y _ { 2 } ,$ length, $i n _ { 7 } ]$ is better than the feature space $\left[ x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } , \right.$ length] because the aim is to determine the optimal feature space which contains as few features as possible and maintains the maximum information at the same time.

The set of 500 data samples that constructs the input features $F ^ { ( 9 ) }$ was generated randomly, with each input feature uniformly distributed on [0,1]; each set of input values was then paired with the correct classi<sup>fi</sup>cation, 2 or 1 according to the function de<sup>fi</sup>ned in Eq. (8). Each continuous input feature of training and test data sets is transformed into discrete feature with equal bin size. Here the bin size is chosen as $6 .$ Feature ranking according to the algorithms described in Section 2.2 and the algorithm proposed in Section 3 on this data are presented in Table 1. The maximum MI G values of each algorithm are illustrated in Table 2.

![](/api/attachments/RMCGNTYE/fulltext/images/aeae63401c3790ecb7ce465a2ae309288747a3f0840fd2cf04f49107ce300373.jpg)  
Fig. 1. Architecture of NN in this study

From Tables 1 and 2, we can see that the <sup>fi</sup>rst 2 best features which are $f _ { 5 }$ (length) and $f _ { 7 } \ ( i n _ { 7 } )$ are correctly selected by all algorithms listed in Table 1a. However only the proposed algorithm NMIFS-FS2 produces the correct selection of the third and fourth features which are $f _ { 3 } = y _ { 1 }$ and $f _ { 4 } = y _ { 2 }$ . The feature ranking order is determined by the feature selection algorithm and the size of the optimal feature space is determined by the maximum MI G value, the stop point of feature selection for the optimal feature space is either reaching the negative value apart from the NMIFS-FS2 algorithm or no signi<sup>fi</sup>cant improvement on the maximum MI G value. According to Table 1b, the optimal feature space is $[ f _ { 5 } , f _ { 7 } ]$ for the MIFS with $\beta = 0 . 4 , \ 0 . 5 ,$ 0.6, 0.7, 0.8, 0.9, 1 and the mRMR algorithms, the optimal feature space is $[ f _ { 5 } , f _ { 7 } , f _ { 9 } ]$ for the MIFS with $\beta = 0 . 3$ , the MIFS-U with $\beta = 0 . 5 ,$ 0.6, 0.7, 0.8, 0.9, 1 and the NMIFS algorithms, the optimal feature space is $[ f _ { 5 } , f _ { 7 } , f _ { 1 } ]$ for the MIFS-U with $\beta = 0 . 3 , 0 . 4 .$ The optimal feature space is $[ f _ { 5 } , f _ { 7 } , f _ { 3 } , f _ { 4 } ]$ when applying the proposed NMIFS-FS2 which is the only algorithm that can correctly identify the optimal feature space among all the algorithms.

## 5.2. Example 2: nonlinear AND

This example studied in [9] provides a direct comparison of the existing algorithms with the proposed NMIFS-FS2. The nonlinear AND is a synthetic problem devised to show a situation where all existing algorithms will fail, while the proposed NMIFS-FS2 still produces the correctly optimal feature space. There are 14 features in total and the <sup>fi</sup>rst 5 features from $f _ { 1 }$ to $f _ { 5 }$ are the irrelevant features which were generated randomly from an exponential distribution with mean 10. The next 6 features from $f _ { 6 } \mathrm { t o } f _ { 1 1 }$ are the relevant features which were generated from a uniform distribution on [ 1 1].

Table 1  
Feature ranking based on the different mutual information algorithms

<table><tr><td>Algorithm</td><td colspan="9">Feature ranking</td></tr><tr><td>MIFS ( $\beta=0.3:0.1:1$ )</td><td> $f_5$ </td><td> $f_7$ </td><td> $f_9$ </td><td> $f_6$ </td><td> $f_8$ </td><td> $f_4$ </td><td> $f_3$ </td><td> $f_1$ </td><td> $f_2$ </td></tr><tr><td>MIFS-U ( $\beta=0.3,0.4$ )</td><td> $f_5$ </td><td> $f_7$ </td><td> $f_1$ </td><td> $f_9$ </td><td> $f_8$ </td><td> $f_4$ </td><td> $f_3$ </td><td> $f_6$ </td><td> $f_2$ </td></tr><tr><td>MIFS-U ( $\beta=0.5,0.6$ )</td><td> $f_5$ </td><td> $f_7$ </td><td> $f_9$ </td><td> $f_1$ </td><td> $f_8$ </td><td> $f_4$ </td><td> $f_3$ </td><td> $f_6$ </td><td> $f_2$ </td></tr><tr><td>MIFS-U ( $\beta=0.7,0.8$ )</td><td> $f_5$ </td><td> $f_7$ </td><td> $f_9$ </td><td> $f_8$ </td><td> $f_4$ </td><td> $f_1$ </td><td> $f_3$ </td><td> $f_6$ </td><td> $f_2$ </td></tr><tr><td>MIFS-U ( $\beta=0.9,1$ )</td><td> $f_5$ </td><td> $f_7$ </td><td> $f_9$ </td><td> $f_8$ </td><td> $f_4$ </td><td> $f_6$ </td><td> $f_3$ </td><td> $f_1$ </td><td> $f_2$ </td></tr><tr><td>mRMR, NMIFS</td><td> $f_5$ </td><td> $f_7$ </td><td> $f_9$ </td><td> $f_6$ </td><td> $f_8$ </td><td> $f_4$ </td><td> $f_3$ </td><td> $f_1$ </td><td> $f_2$ </td></tr><tr><td rowspan="2">NMIFS-FS2 (proposed)Features</td><td> $f_5$ </td><td> $f_7$ </td><td> $f_3$ </td><td> $f_4$ </td><td> $f_6$ </td><td> $f_8$ </td><td> $f_1$ </td><td> $f_9$ </td><td> $f_2$ </td></tr><tr><td> $f_1:x_1$ </td><td> $f_2:x_2$ </td><td> $f_3:y_1$ </td><td> $f_4:y_2$ </td><td> $f_5:length$ </td><td colspan="2"> $f_6:in_6(dummy)$ </td><td colspan="2"> $f_7:in_7=$  $x_1-x_2$   $f_8:in_8=x_1\times x_2$   $f_9:in_9=y_1\times y_2$ </td></tr></table>

The last 3 features from $f _ { 1 2 }$ to $f _ { 1 4 }$ are identical with the features $f _ { 9 }$ to $f _ { 1 1 } .$ . The class label is determined by Eq. (9).

$$
\begin{array}{l l} \text { If } f _ {6}. f _ {7}. f _ {8} > 0 \text { AND } f _ {9} + f _ {1 0} + f _ {1 1} > 0 & \text { then } X \in C _ {1} \\ \text { If } f _ {6}. f _ {7}. f _ {8} <   0 \text { AND } f _ {9} + f _ {1 0} + f _ {1 1} <   0 & \text { then } X \in C _ {2} \end{array}\tag{9}
$$

Clearly the features $f _ { 6 } , f _ { 7 }$ and $f _ { 8 }$ are included in the optimal feature space. One of the remaining three features is selected from each of the pairs $[ f _ { 9 } , f _ { 1 2 } ] , [ f _ { 1 0 } , f _ { 1 3 } ]$ and $[ f _ { 1 1 } , f _ { 1 4 } ]$ , which means that either $f _ { 9 } \mathrm { o r } f _ { 1 2 }$ is selected from the pair $[ f _ { 9 } , f _ { 1 2 } ] ,$ either $f _ { 1 0 } \mathrm { o r } f _ { 1 3 }$ is selected from the pair $\left[ f _ { 1 0 } , f _ { 1 3 } \right]$ and either $f _ { 1 1 }$ or $f _ { 1 4 }$ is selected from the pair $[ f _ { 1 1 } , f _ { 1 4 } ] .$ Sizes of the training data set are the same as example 1 which randomly generates 500 samples as the data set. When a sample is randomly generated, if it satis<sup>fi</sup>es $\operatorname { E q . }$ (9), then it is kept for the data set, otherwise it is removed. This process repeats until reaching 500 samples for the data set. The input feature space is $F ^ { ( 1 4 ) } = [ f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 } , f _ { 5 } , f _ { 6 } ,$ $f _ { 7 } , f _ { 8 } , f _ { 9 } , f _ { 1 0 } , f _ { 1 1 } , f _ { 1 2 } , f _ { 1 3 } , f _ { 1 4 } ] .$ . Feature ranking and the MI G value of each feature selection algorithm for this nonlinear AND problem are presented in Table 3 and Table A.1 (Table A.1 in Appendix $\mathsf { A } ) .$ respectively.

From Tables 3 and A.1, we can see that the algorithms listed in Table 3, apart from the algorithms NMIFS and NMIFS-FS2, can only identify up to the <sup>fi</sup>rst two $( f _ { 9 }$ and $f _ { 1 0 } )$ , or the <sup>fi</sup>rst three $( f _ { 9 } , f _ { 1 0 } \mathrm { a n d } f _ { 1 1 } )$ relevant features, whereas the <sup>fi</sup>rst four $( f _ { 9 } , \ f _ { 1 0 } , \ f _ { 1 1 }$ and $f _ { 7 } )$ relevant features are identi<sup>fi</sup>ed by the algorithm MIFS-U $( \beta = 1 )$ . The next two relevant features $f _ { 7 }$ and $f _ { 8 }$ are identi<sup>fi</sup>ed only by the NMIFS and the NMIFS-FS2 algorithms, and the last relevant feature $f _ { 6 }$ is correctly identi<sup>fi</sup>ed only by the NMIFS-FS2 algorithm. The optimal feature space can only be identi<sup>fi</sup>ed by the NMIFS-FS2 algorithm for this problem.

5.3. Example 3: single proton emission computed tomography (SPECT) heart data

This data is adopted from the UC Irvine Machine Learning Repository (http://archive.ics.uci.edu/), and is studied in [6,11]. This 267 SPECT patients' image data set describes diagnosing of cardiac (SPECT) images and it was processed to extract the features that summarize the original SPECT images. The pattern was further processed to obtain 22 binary feature patterns and this format is used in this experiment. Each of the patients is classi<sup>fi</sup>ed into two categories: normal and abnormal, but this data set is unbalanced because it only contains 55 normal cases and 212 abnormal cases. The balanced test and validation data sets with the same size of normal and abnormal cases are used in this experiment in order to reduce the biases. The balanced 30 and 30 cases are randomly selected as the test and validation data set, respectively, and the rest of the data (207) is used as the training data. The training data is used to select the optimal feature set by a feature selection algorithm, and is also used to train the NN model. The validation data is used to determine the weights in the NN model (NN trained from the training data). For simplicity, <sup>fi</sup>xed three multiple numbers of inputs are used as hidden units in the NN model and the test data which is unseen data is used to validate the feature selection algorithms.

Table 4  
Table 2  
Maximum MI G values of each feature selection.

<table><tr><td>Algorithm</td><td colspan="9">Maximum MI G values of each feature selection</td></tr><tr><td>MIFS (β=0.3)</td><td>0.421</td><td>0.102</td><td>0.001</td><td>-0.023</td><td>-0.066</td><td>-0.202</td><td>-0.222</td><td>-0.351</td><td>-0.385</td></tr><tr><td>MIFS (β=0.4)</td><td>0.421</td><td>0.100</td><td>-0.005</td><td>-0.032</td><td>-0.094</td><td>-0.274</td><td>-0.298</td><td>-0.478</td><td>-0.515</td></tr><tr><td>MIFS (β=0.5)</td><td>0.421</td><td>0.098</td><td>-0.011</td><td>-0.041</td><td>-0.123</td><td>-0.346</td><td>-0.375</td><td>-0.605</td><td>-0.644</td></tr><tr><td>MIFS (β=0.6)</td><td>0.421</td><td>0.096</td><td>-0.017</td><td>-0.050</td><td>-0.151</td><td>-0.418</td><td>-0.452</td><td>-0.732</td><td>-0.774</td></tr><tr><td>MIFS (β=0.7)</td><td>0.421</td><td>0.094</td><td>-0.022</td><td>-0.059</td><td>-0.179</td><td>-0.490</td><td>-0.528</td><td>-0.859</td><td>-0.904</td></tr><tr><td>MIFS (β=0.8)</td><td>0.421</td><td>0.092</td><td>-0.028</td><td>-0.068</td><td>-0.207</td><td>-0.562</td><td>-0.605</td><td>-0.986</td><td>-1.034</td></tr><tr><td>MIFS (β=0.9)</td><td>0.421</td><td>0.090</td><td>-0.034</td><td>-0.077</td><td>-0.235</td><td>-0.634</td><td>-0.682</td><td>-1.113</td><td>-1.164</td></tr><tr><td>MIFS (β=1)</td><td>0.421</td><td>0.088</td><td>-0.039</td><td>-0.086</td><td>-0.263</td><td>-0.706</td><td>-0.758</td><td>-1.240</td><td>-1.293</td></tr><tr><td>MIFS-U (β=0.3)</td><td>0.421</td><td>0.107</td><td>0.020</td><td>0.016</td><td>0.012</td><td>0.010</td><td>0.005</td><td>0.001</td><td>-0.006</td></tr><tr><td>MIFS-U (β=0.4)</td><td>0.421</td><td>0.106</td><td>0.017</td><td>0.015</td><td>0.010</td><td>0.009</td><td>0.003</td><td>0.000</td><td>-0.010</td></tr><tr><td>MIFS-U (β=0.5)</td><td>0.421</td><td>0.106</td><td>0.015</td><td>0.013</td><td>0.008</td><td>0.007</td><td>0.002</td><td>0.000</td><td>-0.013</td></tr><tr><td>MIFS-U (β=0.6)</td><td>0.421</td><td>0.106</td><td>0.014</td><td>0.010</td><td>0.006</td><td>0.006</td><td>0.001</td><td>-0.001</td><td>-0.017</td></tr><tr><td>MIFS-U (β=0.7)</td><td>0.421</td><td>0.105</td><td>0.013</td><td>0.009</td><td>0.005</td><td>0.003</td><td>-0.001</td><td>-0.002</td><td>-0.020</td></tr><tr><td>MIFS-U (β=0.8)</td><td>0.421</td><td>0.105</td><td>0.013</td><td>0.007</td><td>0.003</td><td>-0.001</td><td>-0.002</td><td>-0.003</td><td>-0.024</td></tr><tr><td>MIFS-U (β=0.9)</td><td>0.421</td><td>0.105</td><td>0.012</td><td>0.006</td><td>0.002</td><td>-0.003</td><td>-0.003</td><td>-0.005</td><td>-0.027</td></tr><tr><td>MIFS-U (β=1)</td><td>0.421</td><td>0.104</td><td>0.012</td><td>0.004</td><td>0.001</td><td>-0.003</td><td>-0.004</td><td>-0.009</td><td>-0.031</td></tr><tr><td>mRMR</td><td>0.421</td><td>0.088</td><td>-0.011</td><td>-0.026</td><td>-0.052</td><td>-0.130</td><td>-0.119</td><td>-0.151</td><td>-0.158</td></tr><tr><td>NMIFS</td><td>0.421</td><td>0.099</td><td>0.004</td><td>-0.009</td><td>-0.015</td><td>-0.052</td><td>-0.049</td><td>-0.048</td><td>-0.067</td></tr><tr><td>NMIFS-FS2</td><td>0.421</td><td>0.621</td><td>0.768</td><td>-0.111</td><td>-0.114</td><td>-0.116</td><td>-0.231</td><td>-0.234</td><td>-0.238</td></tr><tr><td>Features</td><td colspan="9"> $f_1:x_1$   $f_2:x_2$   $f_3:y_1$   $f_4:y_2$   $f_5:length$   $f_6:in_6$   $f_7:in_7$   $f_8:in_8$   $f_9:in_9$ </td></tr></table>

Note: Bold number indicates that the corresponding feature belongs to the optimal subset.

The various feature selection algorithms are applied to this SPECT data, and the parameter β is chosen as value 1 which is the same as used in the papers [2,12]. 20 experiments are performed for each feature selection algorithm using the randomly selected training data, the <sup>fi</sup>nal feature selection ranking is determined by the mode (majority vote) of these 20 experiments and the results are illustrated in Table 4.

## Table 4 shows that

a) The most important feature is the 13th feature (f ) which is selected by all <sup>fi</sup>ve feature selection algorithms.

b) The feature f is selected as the second most important feature by MIFS-U (β=1) and the proposed NMIFS-FS2 algorithms, however, f is selected as the least important feature and f is selected as the second most important feature by MIFS (β=1), mRMR and NMIFS.

c) The feature $f _ { 2 2 }$ is selected as the third most important feature by NMIFS-FS2, while it is selected as the almost least important feature by the rest of the feature selection algorithms.

In order to validate each feature selection algorithm and obtain the optimal feature subset, the same data sets of the training, validation and test data that are used in the feature selection of 20 experiments

Feature ranking based on the different mutual information algorithms.

<table><tr><td>Algorithm</td><td colspan="14">Feature ranking</td></tr><tr><td>MIFS (β=0.3)</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_3$ </td><td> $f_1$ </td><td> $f_7$ </td><td> $f_4$ </td><td> $f_2$ </td><td> $f_5$ </td><td> $f_8$ </td><td> $f_6$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td></tr><tr><td>MIFS (β=0.4:0.1:0.8)</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_3$ </td><td> $f_1$ </td><td> $f_4$ </td><td> $f_2$ </td><td> $f_7$ </td><td> $f_8$ </td><td> $f_5$ </td><td> $f_6$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td></tr><tr><td>MIFS (β=0.9)</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $f_1$ </td><td> $f_4$ </td><td> $f_7$ </td><td> $f_8$ </td><td> $f_5$ </td><td> $f_6$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td></tr><tr><td>MIFS (β=1)</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $f_1$ </td><td> $f_4$ </td><td> $f_7$ </td><td> $f_8$ </td><td> $f_6$ </td><td> $f_5$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td></tr><tr><td>MIFS-U (β=0.3)</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{12}$ </td><td> $f_{11}$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td><td> $f_7$ </td><td> $f_3$ </td><td> $f_5$ </td><td> $f_1$ </td><td> $f_4$ </td><td> $f_8$ </td><td> $f_2$ </td><td> $f_6$ </td></tr><tr><td>MIFS-U (β=0.4)</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td><td> $f_7$ </td><td> $f_3$ </td><td> $f_5$ </td><td> $f_1$ </td><td> $f_4$ </td><td> $f_8$ </td><td> $f_2$ </td><td> $f_6$ </td></tr><tr><td>MIFS-U (β=0.5)</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td><td> $f_7$ </td><td> $f_3$ </td><td> $f_5$ </td><td> $f_1$ </td><td> $f_4$ </td><td> $f_2$ </td><td> $f_8$ </td><td> $f_6$ </td></tr><tr><td>MIFS-U (β=0.6:0.1:0.8)</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td><td> $f_7$ </td><td> $f_3$ </td><td> $f_1$ </td><td> $f_5$ </td><td> $f_4$ </td><td> $f_2$ </td><td> $f_8$ </td><td> $f_6$ </td></tr><tr><td>MIFS-U (β=0.9)</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td> $f_7$ </td><td> $f_{14}$ </td><td> $f_3$ </td><td> $f_1$ </td><td> $f_5$ </td><td> $f_2$ </td><td> $f_4$ </td><td> $f_8$ </td><td> $f_6$ </td></tr><tr><td>MIFS-U (β=1)</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_7$ </td><td> $f_3$ </td><td> $f_5$ </td><td> $f_1$ </td><td> $f_4$ </td><td> $f_2$ </td><td> $f_8$ </td><td> $f_6$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td></tr><tr><td>mRMR</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_3$ </td><td> $f_1$ </td><td> $f_7$ </td><td> $f_4$ </td><td> $f_2$ </td><td> $f_5$ </td><td> $f_8$ </td><td> $f_6$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td></td></tr><tr><td>NMIFS</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_7$ </td><td> $f_8$ </td><td> $f_{12}$ </td><td> $f_6$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td><td> $f_4$ </td><td> $f_1$ </td><td> $f_5$ </td><td> $f_2$ </td><td> $f_3$ </td></tr><tr><td>NMIFS-FS2</td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{11}$ </td><td> $f_7$ </td><td> $f_8$ </td><td> $f_6$ </td><td> $f_1$ </td><td> $f_5$ </td><td> $f_2$ </td><td> $f_4$ </td><td> $f_3$ </td><td> $f_{12}$ </td><td> $f_{13}$ </td><td> $f_{14}$ </td></tr></table>

SPECT heart data: mode of feature rankings based on the different mutual information algorithms.

<table><tr><td>Algorithm</td><td colspan="23">Feature ranking</td></tr><tr><td>MIFS (β=1)</td><td> $f_{13}$ </td><td> $f_{18}$ </td><td> $f_{17}$ </td><td> $f_{15}$ </td><td> $f_6$ </td><td> $f_{19}$ </td><td> $f_2$ </td><td> $f_{11}$ </td><td> $f_7$ </td><td> $f_4$ </td><td> $f_{12}$ </td><td> $f_{16}$ </td><td> $f_{14}$ </td><td> $f_{20}$ </td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{21}$ </td><td> $f_5$ </td><td> $f_3$ </td><td> $f_{22}$ </td><td> $f_8$ </td><td> $f_1$ </td><td></td></tr><tr><td>MIFS-U(β=1)</td><td> $f_{13}$ </td><td> $f_1$ </td><td> $f_{14}$ </td><td> $f_{15}$ </td><td> $f_{18}$ </td><td> $f_{17}$ </td><td> $f_{19}$ </td><td> $f_6$ </td><td> $f_2$ </td><td> $f_{11}$ </td><td> $f_7$ </td><td> $f_4$ </td><td> $f_{12}$ </td><td> $f_{16}$ </td><td> $f_9$ </td><td> $f_{20}$ </td><td> $f_{10}$ </td><td> $f_{21}$ </td><td> $f_3$ </td><td> $f_{22}$ </td><td> $f_5$ </td><td> $f_8$ </td><td></td></tr><tr><td>mRMR</td><td> $f_{13}$ </td><td> $f_{18}$ </td><td> $f_{17}$ </td><td> $f_{15}$ </td><td> $f_{19}$ </td><td> $f_6$ </td><td> $f_2$ </td><td> $f_{11}$ </td><td> $f_7$ </td><td> $f_4$ </td><td> $f_{16}$ </td><td> $f_{12}$ </td><td> $f_{14}$ </td><td> $f_{20}$ </td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{21}$ </td><td> $f_5$ </td><td> $f_3$ </td><td> $f_{22}$ </td><td> $f_8$ </td><td> $f_1$ </td><td></td></tr><tr><td>NMIFS</td><td> $f_{13}$ </td><td> $f_{18}$ </td><td> $f_{17}$ </td><td> $f_{15}$ </td><td> $f_6$ </td><td> $f_{19}$ </td><td> $f_2$ </td><td> $f_{11}$ </td><td> $f_7$ </td><td> $f_4$ </td><td> $f_{12}$ </td><td> $f_{16}$ )</td><td> $f_{14}$ </td><td> $f_{20}$ </td><td> $f_9$ </td><td> $f_{10}$ </td><td> $f_{21}$ </td><td> $f_5$ </td><td> $f_3$ </td><td> $f_{22}$ </td><td> $f_8$ </td><td> $f_1$ </td><td></td></tr><tr><td>NMIFS-FS2</td><td> $f_{13}$ </td><td> $f_1$ </td><td> $f_{22}$ </td><td> $f_8$ </td><td> $f_5$ </td><td> $f_3$ </td><td> $f_{21}$ </td><td> $f_{10}$ </td><td> $f_{20}$ </td><td> $f_9$ </td><td> $f_{16}$ </td><td> $f_{14}$ </td><td> $f_{12}$ </td><td> $f_4$ </td><td> $f_7$ </td><td> $f_{11}$ </td><td> $f_2$ </td><td> $f_6$ </td><td> $f_{19}$ </td><td> $f_{15}$ </td><td> $f_{17}$ </td><td> $f_{18}$ </td><td></td></tr></table>

Table 5  
Classi<sup>fi</sup>cation rates (%) of the different feature selection algorithms on the test data set.

<table><tr><td></td><td>MIFS (β=1)</td><td>MIFS-U (β=1)</td><td>mRMR</td><td>NMIFS</td><td>NMIFS-FS2</td></tr><tr><td>First 1 feature</td><td>50%</td><td>50%</td><td>50%</td><td>50%</td><td>50%</td></tr><tr><td>First 3 features</td><td>50%</td><td>49.83%</td><td>50%</td><td>50%</td><td>50%</td></tr><tr><td>First 5 features</td><td>50%</td><td>50%</td><td>50%</td><td>50%</td><td>50.83%</td></tr><tr><td>First 7 features</td><td>49.83%</td><td>51%</td><td>49.5%</td><td>49.5%</td><td>54.83%</td></tr><tr><td>First 9 features</td><td>49.17%</td><td>50.67%</td><td>49.33%</td><td>49.17%</td><td>57.33%</td></tr><tr><td>First 11 features</td><td>51.33%</td><td>55.17%</td><td>51.17%</td><td>51.17%</td><td>65.17%</td></tr><tr><td>First 13 features</td><td>53.17%</td><td>57.33%</td><td>53.67%</td><td>53.5%</td><td>66%</td></tr><tr><td>First 15 features</td><td>63.17%</td><td>59%</td><td>63.17%</td><td>62.5%</td><td>68%</td></tr><tr><td>First 17 features</td><td>68.83%</td><td>65.5%</td><td>67.33%</td><td>67.17%</td><td>67.67%</td></tr><tr><td>First 19 features</td><td>66.67%</td><td>66.5%</td><td>67.83%</td><td>68.5%</td><td>67%</td></tr><tr><td>First 21 features</td><td>67.67%</td><td>67.17%</td><td>67.17%</td><td>67.17%</td><td>66.5%</td></tr><tr><td>All 22 features</td><td>66.83%</td><td>66.83%</td><td>66.83%</td><td>66.83%</td><td>66.83%</td></tr></table>

are used for the NN models. The NN models are trained using the training data sets which contain the <sup>fi</sup>rst 1 important feature, the <sup>fi</sup>rst 3 important features until all the 22 features. The feature rankings are selected by the different feature selection algorithms and experiments. The validation data sets are used to determine the weights of the trained NN models for a <sup>fi</sup>xed number of hidden units of these 20 experiments, run 15 times for each input due to the different initial weights of each run for the same inputs, and the trained NN model (weights as parameters) with the best performance of these 15 runs on the validation data set is selected as the <sup>fi</sup>nal trained NN model. Applying the trained NN model to the test data sets, the means of these classi<sup>fi</sup>cation rates for the different inputs and the different feature selection algorithms are presented in Table 5 and illustrated in Fig. 2 for the training, validation and test data sets.

![](/api/attachments/RMCGNTYE/fulltext/images/501e97e43b6aec7dfe2068b64116c50689b6676fb477f802fcb47d5a07419ac7.jpg)

![](/api/attachments/RMCGNTYE/fulltext/images/7041383c2e21fbaa97f970c2a52a3a4e67f98dfcd93c6d97d03d61d481fcaa84.jpg)

Fig. 2 shows that the performance of the proposed NMIFS-FS2 algorithm is signi<sup>fi</sup>cantly better than that of the other feature selection algorithms for this data set. The test data set is used to validate the feature selection algorithms; the performances of using the <sup>fi</sup>rst 3 features as inputs are almost the same for all <sup>fi</sup>ve feature selection algorithms. The performance of the NMIFS-FS2 algorithm is signi<sup>fi</sup>cantly better than that of the other four algorithms from using the <sup>fi</sup>rst 4 features to the <sup>fi</sup>rst 15 features as inputs. The performance after using the <sup>fi</sup>rst 15 features as inputs becomes stable for all <sup>fi</sup>ve algorithms. The best optimal subset that contains the <sup>fi</sup>rst 15 features $[ f _ { 1 3 } , f _ { 1 } , f _ { 2 2 } ,$ f<sub>8,</sub> $f _ { 5 } , f _ { 3 } , f _ { 2 1 } , f _ { 1 0 } , f _ { 2 0 } , f _ { 9 } , f _ { 1 6 } , f _ { 1 4 } , f _ { 1 2 } , f _ { 4 } , f _ { 7 } \ ]$ is selected by the NMIFS-FS2 algorithm. The performance of the MIFS-U (β=1) algorithm is better than that of the MIFS $( \beta = 1 )$ , mRMR and NMIFS algorithms from using the <sup>fi</sup>rst 5 features to the <sup>fi</sup>rst 13 features as inputs, then the MIFS-U (β=1) algorithm becomes worse than the MIFS $( \beta = 1 )$ mRMR and NMIFS algorithms from using the <sup>fi</sup>rst 14 features as inputs. This best optimal subset gives us the implication of the importance features on normal/abnormal SPECT patients [6,11].

![](/api/attachments/RMCGNTYE/fulltext/images/fa1536abdab6360834d065e0deb4fdfa9c5631b98434fbe6499a90723c5c42e6.jpg)  
Fig. 2. Means of classi<sup>fi</sup>cation rates of 20 runs for the different feature selection algorithms.

## 6. Conclusions and future research works

This paper has investigated the approaches to solve the important classi<sup>fi</sup>cation problem of the feature selection. The main contribution of this paper is that the MI formula (NMIFS-FS2) has been proposed to calculate the MI between a combination of features, or a set of features, and the class. The mutual information theory for the feature selection algorithms MIFS, MIFS-U, mRMR and NMIFS uses only the pair wise MI, that is the MI between an individual feature to another individual feature, and between an individual feature and the class. Thus they require the redundancy parameter β to approximate the interaction between the features, but it is dif<sup>fi</sup>cult to select the value of parameter β. There are no procedures and suggestions on selecting the value of β [12]. Experiment results have demonstrated that the proposed algorithm NMIFS-FS2 is more robust, widely applicable, informative and accurate than the MIFS, MIFS-U, mRMR and NMIFS algorithms. The stability of the performance and the agreement of ranking for the NMIFS-FS2 algorithm show encouraging results.

In summary, the proposed composite algorithm, NMIFS-FS2, appears to represent further improvement in the procedures available for computationally tractable and effective identi<sup>fi</sup>cation of the optimal feature space of the input features for classi<sup>fi</sup>cation problems.

In order to transform the continued-valued features into the discrete-valued features, we need to pack almost equally the number of bins from the range of the number for each continuous variable.

Future work will apply the proposed algorithm to a wide range of data sets with the different split training, validation and test data sets to test if the NMIFS-FS2 algorithm still outperforms the other feature selection algorithms such as MIFS, MIFS-U, mRMR and NMIFS.

## Appendix A

Table A.1  
Maximum MI G value of each feature selection.

<table><tr><td>Algorithm</td><td colspan="14">Maximum MI G value of each feature selection</td></tr><tr><td>MIFS (β=0.3)</td><td>0.217</td><td>0.151</td><td>0.121</td><td>-0.019</td><td>-0.029</td><td>-0.041</td><td>-0.051</td><td>-0.062</td><td>-0.085</td><td>-0.104</td><td>-0.122</td><td>-0.645</td><td>-0.740</td><td>-0.778</td></tr><tr><td>MIFS (β=0.4)</td><td>0.217</td><td>0.148</td><td>0.114</td><td>-0.029</td><td>-0.042</td><td>-0.058</td><td>-0.073</td><td>-0.085</td><td>-0.117</td><td>-0.141</td><td>-0.165</td><td>-0.932</td><td>-1.040</td><td>-1.085</td></tr><tr><td>MIFS (β=0.5)</td><td>0.217</td><td>0.145</td><td>0.106</td><td>-0.039</td><td>-0.054</td><td>-0.075</td><td>-0.092</td><td>-0.110</td><td>-0.147</td><td>-0.179</td><td>-0.207</td><td>-1.220</td><td>-1.340</td><td>-1.392</td></tr><tr><td>MIFS (β=0.6)</td><td>0.217</td><td>0.142</td><td>0.099</td><td>-0.049</td><td>-0.067</td><td>-0.091</td><td>-0.111</td><td>-0.136</td><td>-0.178</td><td>-0.217</td><td>-0.249</td><td>-1.507</td><td>-1.640</td><td>-1.700</td></tr><tr><td>MIFS (β=0.7)</td><td>0.217</td><td>0.139</td><td>0.091</td><td>-0.059</td><td>-0.080</td><td>-0.107</td><td>-0.131</td><td>-0.162</td><td>-0.209</td><td>-0.254</td><td>-0.291</td><td>-1.794</td><td>-1.939</td><td>-2.007</td></tr><tr><td>MIFS (β=0.8)</td><td>0.217</td><td>0.136</td><td>0.083</td><td>-0.070</td><td>-0.093</td><td>-0.123</td><td>-0.150</td><td>-0.187</td><td>-0.240</td><td>-0.292</td><td>-0.334</td><td>-2.081</td><td>-2.239</td><td>-2.314</td></tr><tr><td>MIFS (β=0.9)</td><td>0.217</td><td>0.133</td><td>0.076</td><td>-0.079</td><td>-0.105</td><td>-0.140</td><td>-0.169</td><td>-0.213</td><td>-0.271</td><td>-0.330</td><td>-0.376</td><td>-2.369</td><td>-2.539</td><td>-2.622</td></tr><tr><td>MIFS (β=1)</td><td>0.217</td><td>0.130</td><td>0.068</td><td>-0.088</td><td>-0.118</td><td>-0.157</td><td>-0.189</td><td>-0.238</td><td>-0.301</td><td>-0.367</td><td>-0.419</td><td>-2.656</td><td>-2.839</td><td>-2.929</td></tr><tr><td>MIFS-U (β=0.3)</td><td>0.217</td><td>0.159</td><td>0.151</td><td>0.142</td><td>0.110</td><td>0.098</td><td>0.013</td><td>0.007</td><td>0.005</td><td>0.005</td><td>0.002</td><td>0.001</td><td>0.001</td><td>-0.001</td></tr><tr><td>MIFS-U (β=0.4)</td><td>0.217</td><td>0.159</td><td>0.142</td><td>0.129</td><td>0.093</td><td>0.082</td><td>0.011</td><td>0.006</td><td>0.004</td><td>0.003</td><td>0.000</td><td>-0.001</td><td>-0.001</td><td>-0.002</td></tr><tr><td>MIFS-U (β=0.5)</td><td>0.217</td><td>0.158</td><td>0.141</td><td>0.106</td><td>0.076</td><td>0.066</td><td>0.009</td><td>0.005</td><td>0.002</td><td>0.002</td><td>-0.001</td><td>-0.002</td><td>-0.002</td><td>-0.004</td></tr><tr><td>MIFS-U (β=0.6)</td><td>0.217</td><td>0.158</td><td>0.141</td><td>0.084</td><td>0.060</td><td>0.051</td><td>0.008</td><td>0.003</td><td>0.000</td><td>0.000</td><td>-0.003</td><td>-0.003</td><td>-0.004</td><td>-0.005</td></tr><tr><td>MIFS-U (β=0.7)</td><td>0.217</td><td>0.158</td><td>0.140</td><td>0.062</td><td>0.043</td><td>0.035</td><td>0.006</td><td>0.002</td><td>-0.001</td><td>-0.001</td><td>-0.004</td><td>-0.005</td><td>-0.006</td><td>-0.007</td></tr><tr><td>MIFS-U (β=0.8)</td><td>0.217</td><td>0.158</td><td>0.140</td><td>0.040</td><td>0.027</td><td>0.020</td><td>0.004</td><td>0.001</td><td>-0.003</td><td>-0.003</td><td>-0.006</td><td>-0.006</td><td>-0.008</td><td>-0.008</td></tr><tr><td>MIFS-U (β=0.9)</td><td>0.217</td><td>0.158</td><td>0.139</td><td>0.018</td><td>0.010</td><td>0.005</td><td>0.004</td><td>-0.001</td><td>-0.004</td><td>-0.005</td><td>-0.007</td><td>-0.007</td><td>-0.010</td><td>-0.010</td></tr><tr><td>MIFS-U (β=1)</td><td>0.217</td><td>0.157</td><td>0.139</td><td>0.009</td><td>0.005</td><td>0.002</td><td>0.001</td><td>-0.002</td><td>-0.003</td><td>-0.003</td><td>-0.005</td><td>-0.006</td><td>-0.008</td><td>-0.013</td></tr><tr><td>mRMR</td><td>0.217</td><td>0.130</td><td>0.106</td><td>-0.022</td><td>-0.023</td><td>-0.022</td><td>-0.026</td><td>-0.027</td><td>-0.029</td><td>-0.034</td><td>-0.038</td><td>-0.044</td><td>-0.090</td><td>-0.092</td></tr><tr><td>NMIFS</td><td>0.217</td><td>0.148</td><td>0.130</td><td>0.001</td><td>-0.009</td><td>0.007</td><td>-0.011</td><td>0.004</td><td>0.005</td><td>-0.017</td><td>-0.017</td><td>-0.018</td><td>-0.023</td><td>-0.024</td></tr><tr><td>NMIFS-FS2</td><td>0.217</td><td>0.487</td><td>0.907</td><td>-0.098</td><td>-0.108</td><td>-0.113</td><td>-0.129</td><td>-0.122</td><td>-0.118</td><td>-0.119</td><td>-0.118</td><td>-0.159</td><td>-0.193</td><td>-0.188</td></tr></table>

## References

[1] U. Alper, M. Alper, A discrete particle swarm optimization method for feature selection in binary classi<sup>fi</sup>cation problems, European Journal of Operational Research 206 (2010) 528–539.

[2] R. Battiti, Using mutual information for selecting features in supervised neutral net learning, IEEE Transactions Neural Networks 5 (1994) 537–550.

[3] J. Bins, B. Draper, Feature selection from huge feature sets, in: Proc. of Eighth International Conference on Computer Vision, Vancouver, BC, Canada, 2001, pp. 159–165.

[4] Y. Chen, D. Liginlal, A maximum entropy approach to feature selection in knowledge-based authentication, Decision Support Systems 46 (2008) 388–398

[5] M.B. Christopher, Neural Networks for Pattern Recognition, Oxford University Press, 1995.

[6] K.J. Cios, L. Kurgan, Hybrid inductive machine learning: an overview of CLIP algorithms, in: L.C. Jain, J. Kacprzyk (Eds.), New Learning Paradigms in Soft Computing, Physica-Verlag (Springer), 2001.

[7] P. Cortez, A. Cerdeira, F. Almeida, T. Matos, J. Reis, Modeling wine preferences by data mining from physicochemical properties, Decision Support Systems 47 (2009) 547-533.

[8] M. Dash, H. Liu, Consistency-based search in feature selection, Journal of Arti<sup>fi</sup>cial Intelligence 151 (2003) 155–176.

[9] P.A. Estévez, M. Tesmer, C.A. Perez, J.M. Zurada, Normalized mutual information feature selection, IEEE Transactions on Neural Networks 20 (2) (2009) 189–201.

[10] S. Haykin, Neural Networks: A Comprehensive Foundation, Prentice Hall, 1999.

[11] L.A. Kurgan, K.J. Cios, R. Tadeusiewicz, M. Ogiela, L.S. Goodenday, Knowledge discovery approach to automated cardiac SPECT diagnosis, Artificial Intelligence in Medicine 23 (2) (2001) 149–169

[12] N. Kwak, C.H. Choi, Input feature selection for classification problems. IEEE Transactions Neural Networks 13 (2002).143-159

[13] G. Lashkia, L. Anthony, Relevant, irredundant feature selection and noisy example elimination, IEEE Transactions on Systems, Man, and Cybernetics — Part B: Cybernetics 34 (2) (2004) 888–897.

[14] H. Peng, F. Long, C. Ding, Feature selection based on mutual information: criteria of max-dependency, max-relevance and min-redundancy, IEEE Transactions on Pattern Analysis and Machine Intelligence 27 (8) (2005) 1226–1238.

[15] M. Sebban, R. Nock, A hybrid <sup>fi</sup>lter/wrapper approach of feature selection using information theory, Pattern Recognition 35 (4) (2002) 835–846.

[16] S. Theodoridis, K. Koutroumbas, Pattern Recognition, Academic Press, San Diego, 1999.

[17] P. van de Laar, T.M. Heskes, C.C.A.M. Gielen, Partial retraining: a new approach to input relevance determination, International Journal of Neural Systems 9 (1999) 75–85.

[18] W.J. Wang, P. Jones, D. Partridge, A comparative study of feature-salience ranking techniques, Neural Computation 13 (2001) 1603-1623

[19] L. Yu, H. Liu, Ef<sup>fi</sup>cient feature selection via analysis of relevance and redundancy, Journal of Machine Learning Research 5 (2004) 1205–1224.

Dr Shuang Cang is a Senior Lecturer in the School of Tourism, Bournemouth University, UK. She gained BSc (Hons) with <sup>fi</sup>rst class honors, MSc with distinction and a PhD degree in Mathematics/Applied Mathematics. She worked in a UK leading Software Company for about two and half years. Then she worked in the Department of Computer Sciences at Exeter University and University of Wales (Aberystwyth). She spent over two vears as Senior Statistician/Senior Analyst in the UK Government Research Laboratory and UK Government Department, where she applied statistical and pattern recognition techniques to solve real and complex problems. Her research interests cover data mining, arti<sup>fi</sup>cial intelligence, pattern recognition, multivariance statistics, forecasting and segmentations.

Hongnian Yu is currently a Professor of Faculty of Computing, Engineering and Technology at Staffordshire University. He has extensive research experience in modeling and control of robots and mechatronic devices and neural networks, mobile computing, modeling, scheduling, planning and simulations of large discrete event dynamic systems, RFID with applications to manufacturing systems, supply chains, transportation networks and computer networks. He has published over 200 research papers and held several grants from EPSRC, the Royal Society, and other funding bodies. He is a member of the EPSRC Peer Review College and serves on various conferences and academic societies.
