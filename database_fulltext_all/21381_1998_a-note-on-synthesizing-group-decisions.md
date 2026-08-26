---
otero_id: 21381
otero_key: "4Z3HNYCE"
title: "A note on synthesizing group decisions"
authors: "S.I. Gass; T. Rapcsák"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00061-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A note on synthesizing group decisions

S.I. Gass <sup>a</sup>, T. Rapcsak <sup>b,)</sup> ´

<sup>a</sup> College of Business and Management, UniÕersity of Maryland, College Park, Maryland, MD 20742, USA <sup>b</sup> Laboratory of Operations Research and Decision Systems, Computer and Automation Institute, Hungarian Academy of Sciences, P.O. Box 63, Budapest, Hungary

## Abstract

An approach is discussed to expert group aggregation based on the Singular Value Decomposition SVD of Analytic Ž . Hierarchy Process AHP pairwise comparison matrices. The group decision phase should consist of the aggregation of theŽ . individual expert weight vectors determined by SVD, taking the voting powers of the experts and sensitivity analysis into account based on Bridgman’s principle. q 1998 Elsevier Science B.V.

Keywords: Group decision systems; AHP; Singular value decomposition

## 1. Introduction

In this note, we consider the multicriteria decision problem in which experts individually and independently evaluate a finite number of competing alternatives, with the objective of determining either the best alternative or a ranking of the alternatives. How this final determination is made is often a function of the multicriteria decision process that is used. However, some basic guidelines have been discussed in the literature.

Let $x _ { i } , j = 1 , \dotsc , n .$ be the judgement of the jth expert and denote the synthesizing aggregatingŽ . function of the n judgements by $f ( x _ { 1 } , \ldots , x _ { n } ) .$ Mirkin 10 , under the assumption that the judges do <sup>w</sup> <sup>x</sup> not have the same expertise, describes a process that uses competence weights for each expert. Here, each expert evaluates the alternatives against the criteria, with the final value of an alternative being a simple additive-multiplicative function of the competency weights and the evaluations. Mirkin notes that the resulting average scores are rather stable with respect to changes in groups of experts, but that such averages do not necessarily express the consistent opinion of a group. The paper by Temesi and Stahl 12<sup>w</sup> <sup>x</sup> describes an application that illustrates this approach to aggregating expert opinions. Aczel 1 states prop-´ <sup>w</sup> <sup>x</sup> erties e.g., symmetry, homogeneity of possible syn-Ž . thesizing functions, along with propositions and theorems that apply to such functions. He concludes that the geometric mean ‘may be’ the appropriate aggregating function in many situations. Prior work by Aczel and Saaty 2 showed that under the as- ´ <sup>w</sup> <sup>x</sup> sumptions of reciprocity $( f ( 1 / x _ { 1 } , \ldots , 1 / x _ { n } ) =$ $1 / f ( x _ { 1 } , \ldots , x _ { n } ) )$ and homogeneity $( f ( s x _ { 1 } , \ldots , s x _ { n } )$ $= s f ( x _ { 1 } , \ldots , x _ { n } ) )$ , the only solution for the synthesizing function is the geometric mean, i.e., $f ( x _ { 1 } , \dots , x _ { n } ) = \prod _ { i = 1 } ^ { n } x _ { i } ^ { 1 / n }$ , when $n \geq 2$ . The reciprocity assumption is also a requirement for the pairwise judgements that are made when applying the Analytic Hierarchy Process AHP for multicrite-Ž . ria analysis 11 . This note discusses an approach to<sup>w</sup> <sup>x</sup> expert group aggregation based on the Singular Value Decomposition SVD of AHP pairwise comparisonŽ . matrices.

## 2. Singular value decomposition

Singular value decomposition is an important tool of matrix algebra that has been applied to a number of areas, for example, principal component analysis and canonical correlation in statistics, the determination of Moore–Penrose generalized inverse, and low rank approximation of matrices 7,4,6 . The matrix<sup>w</sup> <sup>x</sup> algebra and computational aspects of SVD are discussed in 7 , furthermore in 5 , and statistical appli- <sup>w x</sup> <sup>w x</sup> cations are described in 6 .<sup>w</sup> <sup>x</sup>

The SVD of a general matrix A is a transformation into a product of three matrices, each of which has a simple special form and geometric interpretation. This SVD representation is given by the following theorem.

Theorem 2.1. Any real $\left( m \times n \right)$ matrix A with rank $k , \left( k \leq \operatorname* { m i n } ( m , n ) \right)$ , can be expressed in the form of $\boldsymbol { A } = \boldsymbol { U } \boldsymbol { D } \boldsymbol { V } ^ { \mathrm { T } } ,$ 2.1 Ž .

where D is a $\left( k \times k \right)$ diagonal matrix with positiÕe diagonal elements $\alpha _ { 1 } , \ldots , \alpha _ { k }$ , U is an $\left( m \times k \right)$ matrix and V is an $\left( n \times k \right)$ matrix such that $U ^ { \mathrm { T } } U = I ,$ $V ^ { \mathrm { T } } V = I ,$ , i.e., the columns of U and V are orthonormal in the Euclidean sense <sup>w</sup> <sup>x</sup> 6 .

An equivalent formulation of Eq. 2.1 in terms of Ž . diads is

$$
A = \sum_ {i = 1} ^ {k} \alpha_ {i} u _ {i} v _ {i} ^ {\mathrm{T}},\tag{2.2}
$$

where $u _ { 1 } , \ldots , u _ { k }$ , and $v _ { 1 } , \ldots , v _ { k }$ , are the columns of $U$ and V, respectively. The diagonal numbers $\alpha _ { i }$ of D are called singular values, while the vectors $u _ { i }$ and $v _ { i } , \ i = 1 , \ldots , k .$ , are termed the left and right singular vectors, respectively. The left and right singular vectors form an orthonormal basis for the columns and rows of A in m-dimensional and n-dimensional spaces, respectively.

We can assume that SVD 2.2 ofŽ . A is such that the singular values $\alpha _ { i }$ of D are arranged so that $\alpha _ { 1 } \geq \alpha _ { 2 } \geq ~ \cdot ~ \cdot ~ \cdot ~ \geq \alpha _ { k }$ . If strict inequalities order the singular values, then there is no multiplicity of singular values and the SVD is uniquely determined up to reflections in corresponding singular vectors. If two singular values are identical, then the corresponding pairs of singular vectors are determined only up to rotations in their respective 2-dimensional subspace. This case leads to the instability of the associated singular vectors with respect to small changes in the elements of the matrix. It is rare, however, that singular values are equal in practice 6 .

If the singular values $\alpha _ { k ^ { * } + 1 } , \ldots , \alpha _ { k }$ are small compared to $\alpha _ { 1 } , \ldots , \alpha _ { k }$ ) for some $k ^ { * } < k$ , then by dropping the last $k - k ^ { * }$ terms of the right-hand side of Eq. 2.2 , a good approximation of Ž . A is obtained with a $k ^ { * }$ -dimensional matrix. The theorem of low rank approximation first stated and proved by Eckart and Young 4 is as follows 6 :<sup>w x</sup> <sup>w x</sup>

## Theorem 2.2. Let

$$
A _ {[ k ^ {*} ]} = \sum_ {i = 1} ^ {k ^ {*}} \alpha_ {i} u _ {i} v _ {i} ^ {\mathrm{T}},\tag{2.3}
$$

be the $\left( m \times n \right)$ matrix of rank $k ^ { * }$ formed from the largest $k ^ { * }$ singular Õalues and the corresponding singular Õectors of A. Then, $A _ { [ k ^ { * } ] }$ is the rank $k ^ { * }$ least squares approximation of A in that it minimizes the function

$$
\sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} \left(a _ {i j} - x _ {i j}\right) ^ {2} = t r a c e \left(\left(A - X\right) \left(A - X\right) ^ {\mathrm{T}}\right)\tag{2.4}
$$

for all matrices X of rank $k ^ { * }$ or less where the trace of a matrix means the sum of the diagonal elements.

## 3. Singular value decomposition of pairwise comparison matrices

Central to the Analytic Hierarchy Process 11 is<sup>w</sup> <sup>x</sup> the determination of pairwise comparison matrices for criteria with respect to one another, or for alternatives with respect to each criterion. An element $a _ { i j }$ of such a matrix represents the ratio of how criterion i Ž . Ž alternative i compares to criterion j alternative $j ) ,$ with $a _ { i j } = 1$ for $i = j$ and all $a _ { i j } > 0$ . Also, $a _ { j i } = 1 / a _ { i j }$ . Such positive matrices are called reciprocal. In this section, we describe the SVD of a pairwise reciprocal matrix that also has the property of consistency.

Definition 3.1. A real $\left( n \times n \right)$ positive matrix A is consistent if

$$
a _ {i k} = a _ {i j} a _ {j k}
$$

$$
\text {   for   all   } i, j, k = 1, \dots , n.
$$

If a matrix is consistent, then it is also reciprocal and $a _ { i i } = 1$ . Hence, a consistent matrix can be viewed as a pairwise comparison matrix. It has been proved that a positive, reciprocal matrix A is consistent iff the largest eigenvalue of A, $\lambda _ { \operatorname* { m a x } } = n \left[ 1 1 \right]$

Theorem 3.1. The SVD of a positiÕe, consistent matrix consists of only one diad where the right singular Õector is equal to the left eigenÕector multiplied by a normalizing constant, and the left singular Õector to the right eigenÕector multiplied by a second normalizing constant.

Proof. The rank of a positive, consistent matrix is equal to one, and the general form of the matrix is as follows:

$$
A = \left( \begin{array}{c c c c} w _ {1} / w _ {1} & w _ {1} / w _ {2} & \dots & w _ {1} / w _ {n} \\ w _ {2} / w _ {1} & w _ {2} / w _ {2} & \dots & w _ {2} / w _ {n} \\ \vdots & \ddots & \vdots \\ w _ {n} / w _ {1} & w _ {n} / w _ {2} & \dots & w _ {n} / w _ {n} \end{array} \right), \quad \mathbf {w} = (w _ {i}) \in R _ {+} ^ {n},\tag{3.1}
$$

where $R _ { + } ^ { n }$ is the positive orthant. The singular value decomposition for the matrix A can be obtained by the following diad:

$$
A = c _ {1} / c _ {2} \left( \begin{array}{c} c _ {2} w _ {1} \\ c _ {2} w _ {2} \\ \vdots \\ c _ {n} w _ {n} \end{array} \right) (1 / c _ {1} w _ {1}, 1 / c _ {1} w _ {2}, \ldots , 1 / c _ {1} w _ {n}), \quad \mathbf {w} \in R _ {+} ^ {n},\tag{3.2}
$$

where $c _ { 1 }$ and $c _ { 2 }$ are positive constants and $c _ { 2 } ^ { 2 } =$ $1 / \Sigma _ { i = 1 } ^ { n } w _ { i } ^ { 2 }$ and $\overline { { c } } _ { 1 } ^ { 2 } = \sum _ { i = 1 } ^ { n } 1 / w _ { i } ^ { 2 }$ . In formula 3.2 ,Ž . $c _ { 1 } / c _ { 2 }$ is the singular value. I

The singular value decomposition seems to be numerically stable and a generally satisfactory matrix algebra method 7 . Moreover, the value of<sup>w</sup> <sup>x</sup> function 2.4 may measure the inconsistency of aŽ . matrix. By Theorem 3.1, the measure of inconsistency is equal to zero in the case of a consistent matrix. The statement gives a new argument for the use of the right eigenvector left singular vector asŽ . weights in AHP for consistent pairwise comparison matrices.

## 4. Group decision based on pairwise comparison matrices

In this part, the question is how to synthesize group judgements given by a set of pairwise comparison matrices. In AHP, the pairwise comparison matrices are reciprocal and it is assumed that the synthesized aggregated judgement can also be stated Ž . as a reciprocal matrix. The geometric mean has been suggested for this purpose 11 . The theoretical back- <sup>w</sup> <sup>x</sup> ground was clarified by Aczel and Saaty 2 , where´ <sup>w</sup> <sup>x</sup> requirements related to synthesizing functions, in particular, separability, associativity, cancellativity, consensus, reciprocal and homogeneity properties, were investigated and all functions satisfying them were determined.

We present a different idea for the group decision phase that consists of the aggregation of the individual expert weight vectors. In this way, the voting powers of the experts can be taken into account based on Bridgman’s principle 3 and sensitivity analysis developed for decision models originated from this principle 9 can also be applied.

In our case, the decision problem is to aggregate the weight vectors obtained by singular value decomposition from the $n \times n$ pairwise comparison matrices of the m experts so that the voting powers of the decision makers given by the person respon- Ž sible for the decisions can be taken into account. Let. $w _ { i j } > 0 , i = 1 , \ldots , m , j = 1 , \ldots , n ,$ , denote the jth components of the ith weight vectors; $v _ { i } > 0 , \ i =$ $1 , \ldots , m$ , the ith expert’s voting power; and $x _ { j } ,$ $j = 1 , \dots , n$ , the unknown components of the synthesized weight vector. The data of this decision problem can be written in tabular form:

$$
\begin{array}{c c c} & x _ {1} & \dots & x _ {n} \\ & A _ {1} & \dots & A _ {n} \\ v _ {1} & E _ {1} & \left[ \begin{array}{c c c} w _ {1 1} & \dots & w _ {1 n} \\ \vdots & \ddots & \vdots \\ w _ {m 1} & \dots & w _ {m n} \end{array} \right], \end{array}\tag{4.1}
$$

where the columns for alternatives $A _ { 1 } , \ldots , A _ { n }$ , are the components of the weight vectors to be aggregated and $E _ { 1 } , \ldots , E _ { m }$ , denote the experts. Let $\mathbf { a } _ { i } =$ $( w _ { i 1 } , \ldots , w _ { i n } ) ^ { \mathrm { T } } , i = 1 , \ldots , m$

The decision principle is to minimize the weighted sum of one of the Holder–Young distances of the¨ given weight vectors and the unknown vector $\mathbf { x } =$ $( x _ { 1 } , \ldots , x _ { n } ) ^ { \mathrm { { T } } }$ . This kind of principles can be formulated by the following entropy optimization problems:

$$
\min \frac {\sum_ {i = 1} ^ {m} v _ {i} H _ {\alpha} (\mathbf {a} _ {i} \| \mathbf {x})}{\sum_ {i = 1} ^ {m} v _ {i}} x _ {j} \geq 0, j = 1, \dots , n,\tag{4.2}
$$

where the Holder–Young distances as a function of a¨ parameter are given in the form of

$$
H _ {\alpha} \left(\mathbf {a} _ {i} \| \mathbf {x}\right) = \frac {1}{\alpha (1 - \alpha)} \sum_ {j = 1} ^ {m} \alpha w _ {i j}
$$

$$
+ (1 - \alpha) x _ {j} - w _ {i j} ^ {\alpha} x _ {j} ^ {1 - \alpha}, \quad \alpha \in R,\tag{4.3}
$$

and $H _ { \alpha } ( \mathbf { a } _ { i } \parallel \mathbf { x } )$ is defined in the limit for $\alpha = 0$ and $\alpha = 1 \ [ 8 ]$ . This class of decision principles contains infinitely many elements. The generalized arithmetic and geometric mean values as functions of , given by

$$
x _ {j} = \left(\sum_ {i = 1} ^ {m} \frac {v _ {i}}{v} w _ {i j} ^ {\alpha}\right) ^ {1 / \alpha}, \quad j = 1, \ldots , n,\tag{4.4}
$$

can be explicitly obtained as the solution of the corresponding entropy optimization problems 4.2 , Ž . where $\Sigma _ { i = 1 } ^ { m } v _ { i } = v $ . In addition, functions 4.3 fulfilŽ . the properties of separability, homogeneity, convexity in x, a and , and the statistical property that the best approximation of the probability based on the observations is the relative frequency 8 .<sup>w</sup> <sup>x</sup>

The generalized Kullback’s I-divergence used as the objective function in decision models is defined in $R _ { + } ^ { n }$ Ž the positive orthant in $R ^ { n } )$ as

$$
D \left(\mathbf {x} \| \mathbf {a} _ {i}\right) = \sum_ {j = 1} ^ {n} x _ {j} \log \left(\frac {x _ {j}}{w _ {i j}}\right) - \sum_ {j = 1} ^ {n} x _ {j} + \sum_ {j = 1} ^ {n} w _ {i j}.\tag{4.5}
$$

If the objective function of problem 4.2 is replacedŽ . by 4.5 , then the optimal solution of 4.2 has an Ž . Ž . explicit form that yields the geometric mean for aggregating the weight vectors:

$$
x _ {j} = \prod_ {i = 1} ^ {m} w _ {i j} ^ {v _ {i} / v}, \quad j = 1, \ldots , n.\tag{4.6}
$$

We point out that the case of Kullback’s I-divergence can be obtained from 4.2 withŽ . $\alpha = 1$

The values of decision models are often subjective or uncertain. Thus, it is important to verify the final ranking of the alternatives using sensitivity analysis. Real-life applications of decision models based on Bridgman principle require the sensitivity analysis of many decision parameters. In previous work, Meszaros and Rapcsak 9 considered the fol-´ ´ ´ <sup>w</sup> <sup>x</sup> lowing sensitivity problems: What are the intervals of the final ranking of the alternatives with the restriction that the intervals of the weights are given? What are the intervals of the weights with the restriction that the final ranking of the alternatives does not change? Consider a subset of the alternatives in which the change of the alternative values is allowed in a given interval. In what intervals are the weights allowed to vary, and how will these modifications effect the values in the entire set of the alternatives? It was shown that these general sensitivity problems, related to decision models based on Bridgman’s principle, lead to the optimization of linear fractional functions over rectangles and a polynomial algorithm with a bound of O nŽ . log n .

The above line of research is planned to be continued by investigating the role of SVD in analyzing inconsistent comparison matrices and how the results can be used to measure inconsistency. Also, we plan to study the exact formulation of sensitivity analysis with respect to group decisions, especially the impact of uncertainty in the competency weights of the experts.

## Acknowledgements

This research was supported in part by the Hungarian National Research Foundation, Grant No. OTKA-T016413.

## References

<sup>w</sup> <sup>x</sup> 1 J. Aczel, Determining merged relative score, Journal of´ Mathematical Analysis and Applications 150 1990 20–40.Ž .

<sup>w</sup> <sup>x</sup> 2 J. Aczel, T.L. Saaty, Procedures for synthesizing ratio judge- ´ ments, Journal of Mathematical Psychology 27 1983 93–Ž . 102.

<sup>w</sup> <sup>x</sup> 3 P.W. Bridgman, Dimensional Analysis, Yale University Press, New Haven, 1931.

<sup>w</sup> <sup>x</sup> 4 C. Eckart, G. Young, The approximation of one matrix by another of lower rank, Psychometrika 1 1936 211–218.Ž .

<sup>w</sup> <sup>x</sup> 5 G.H. Golub, W. Kahan, Calculating the singular values and pseudoinverse of a matrix, SIAM Journal on Numerical Analysis 2 1965 205–224.Ž .

<sup>w</sup> <sup>x</sup> 6 M.J. Greenacre, Theory and Applications of Correspondence Analysis, Academic Press, London, Orlando, 1984.

<sup>w</sup> <sup>x</sup> 7 W.J. Kennedy, J.E. Gentle, Statistical Computing, Marcel Dekker, New York, Basel, 1980.

<sup>w</sup> <sup>x</sup> 8 E. Klafszky, Holder–Young Distance and its Application to ¨ Decision Problems, Prodinform, Budapest, 1992 in Hungar-Ž ian ..

<sup>w</sup> <sup>x</sup> 9 Cs. Meszaros, T. Rapcsak, On sensitivity analysis for a class´ ´ ´ of decision systems, Decision Support Systems 16 1996 Ž . 231–240.

<sup>w</sup> <sup>x</sup> 10 B.G. Mirkin, Group Choice, V.H. Winston and Sons, Washington, 1979.

<sup>w</sup> <sup>x</sup> 11 T.L. Saaty, The analytic hierarchy process, McGraw-Hill, New York, 1980.

<sup>w</sup> <sup>x</sup> 12 J. Temesi, J. Stahl, An application of group decision methods for tender evaluation, PU.M.A. 2 1991 15–22.Ž .

![](/api/attachments/4Z3HNYCE/fulltext/images/2f1a97c96191e7724883ca7e3ab6583db1b95e96cb1867227635616220de4a31.jpg)

Saul I. Gass received a B.S. degree in Education and M.A. degree in mathematics from Boston University and a P h .D . d eg ree in en g in eerin g science<sup>r</sup>operations research from University of California, Berkeley. Currently he is Professor of Management Science and Statistics at the College of Business and Management, University of Maryland. Associate or contributing editor for numerous publications including ORSA Journal on Computing, Op-

erations Research, Interfaces, NaÕal Research Logistics, Computers and Operations Research. He is the author of Linear Programming; now in 5th edition; an Illustrated Guide to Linear Programming; and Decision Making, Models and Algorithms. He was President of Operations Research Society of America and Omega Rho. He received the George E. Kimball Medal in 1991.

![](/api/attachments/4Z3HNYCE/fulltext/images/638315cd61e63dce4e9625cbea6f3de31c7fce9f6a564580d52d90fd045662ea.jpg)

Tamas Rapcsak graduated from Kossuth´ ´ Lajos University, Debrecen, Hungary, and received a Ph.D. degree in operations research. His current posts include Head of Department and Laboratory of Operations Research and Decision Systems at Computer and Automation Institute, Hungarian Academy of Sciences, Professor of Applied Mathematics, Technical University of Budapest, Head of Department of Economic Decision Žjoint department with Budapest Univer-

sity of Economic Sciences . His research interests include decision. systems, nonlinear optimization and generalized convexity. He was President of Hungarian Operational Research Society. Editor of Journal of Global Optimization and Central European Journal for Operations Research and Economics. He received the Gyula Farkas Prize in 1978.
