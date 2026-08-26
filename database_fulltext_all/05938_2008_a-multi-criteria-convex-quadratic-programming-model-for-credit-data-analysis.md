---
otero_id: 5938
otero_key: "X5AS9MWJ"
title: "A Multi-criteria Convex Quadratic Programming model for credit data analysis"
authors: "Yi Peng; Gang Kou; Yong Shi; Zhengxin Chen"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.12.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# A Multi-criteria Convex Quadratic Programming model for credit data analysis

Yi Peng <sup>a,c,1</sup>, Gang Kou <sup>b,c,⁎,1</sup>, Yong Shi <sup>c,d</sup>, Zhengxin Chen <sup>c</sup>

<sup>a</sup> School of Management and Economy, University of Electronic Science and Technology of China, Chengdu, 610054, PR China <sup>b</sup> The Thomson Corporation, R&D, 610 Opperman Drive, Eagan, MN 55123, USA

<sup>c</sup> College of Information Science & Technology, University of Nebraska at Omaha, Omaha, NE 68182, USA <sup>d</sup> CAS Research Center on Fictitious Economy and Data Sciences, Beijing 100080, PR China

Received 13 April 2006; received in revised form 26 November 2007; accepted 2 December 2007 Available online 8 December 2007

## Abstract

Speed and scalability are two essential issues in data mining and knowledge discovery. This paper proposed a mathematical programming model that addresses these two issues and applied the model to Credit Classification Problems. The proposed Multicriteria Convex Quadric Programming (MCQP) model is highly efficient (computing time complexity $O ( n ^ { 1 . 5 - 2 } ) )$ and scalable to massive problems (size of $\hat { O } ( 1 0 ^ { 9 } ) )$ because it only needs to solve linear equations to find the global optimal solution. Kernel functions were introduced to the model to solve nonlinear problems. In addition, the theoretical relationship between the proposed MCQP model and SVM was discussed. © 2007 Elsevier B.V. All rights reserved.

Keywords: Data mining; Classification; Mathematical programming; Multiple criteria decision making; Multi-criteria Convex Quadric Programming (MCQP)

## 1. Introduction

Data mining and knowledge discovery (DMKD) [7,31] has made great progress during the last fifteen years. As one of the major tasks of data mining and an important problem in research and practice, classification has wide business and scientific applications. The classification models can be represented in various forms, such as classification rules, decision trees, mathematical formulae, or neural networks. Among a variety of proposed methods, mathematical programming based approaches have been proven to be excellent in terms of classification accuracy, robustness, and efficiency [2,6,22–28]. The most well-known mathematical programming based classification method is Support Vector Machine (SVM), which was originated from the statistical learning theory [46–51]. In SVM, the goal of a classification model is to find the maxima of the buffer area between decision regions [3]. Data from two classes are separated by two hyperplanes defined by some boundary instances called support vectors. The hyperplanes are either linear in the original input space or nonlinear in a higher dimensional feature space [9,12].

Compared with machine learning and statistic techniques, mathematic programming based approaches for

DMKD are still underdeveloped. Many issues remain unsolved in this area. Two of these issues are of particular interest of this study. The first issue is scalability. It is challenging to find optimal solution for largescale mathematical programming problems due to the computational complexity [37–40] constraint matrix is determined by the size of the training dataset, the computation time increases as the size of training data increases and performance is therefore degraded. The second issue is that many mathematical programming problems require specialized codes or programs such as CPLEX or LINGO.

The objective of this paper is to present an efficient and scalable mathematical programming based classification model, Multi-criteria Convex Quadric Programming model (MCQP). The model was stimulated by the idea of maximizing the external distance between groups and minimizing the internal distance within a certain group [10,11]. It is efficient because it only needs to solve linear equations to find the global optimal solution and obtain the classifier. Kernel functions are introduced to the model to solve nonlinear problems. The scalability issue was addressed by a new epsilonsupport vector approach. Since there are similarities between the MCQP model and SVM, we also discussed the theoretical relationship between the proposed model and SVM model. In fact, our model can be converted to a standard SVM classification model when different pnorm is selected in objective function.

The proposed classification model can be applied in a variety of applications, such as credit card portfolio management, marketing promotion, financial loan evaluation, insurance premium calculation, and medical clinic decision. In order to test the applicability of proposed model, it was applied to four financial-related datasets from four different countries and the classification results of MCQP were compared with four wellknown and frequently used classification benchmark tools: SPSS Linear Discriminant Analysis (LDA) [44], Decision Tree based See5 [34,35], SVMlight [15–17], and LibSVM [5].

This paper is organized as follows: Section 2 discussed the formulation of MCQP model; Section 3 presented an empirical study that compared the MCQP model with well-established classification tools; and Section 4 summarized the paper and discussed future research directions.

This paragraph lists some symbols and acronyms that are used in this paper. A vector $\mathbf { X } \in \Re ^ { r }$ is r-dimensional vector. e denotes a vector of ones and 0 denotes a vector of zeros. The transposed vector will be a vector by a prime superscript $\stackrel { \cdot } { \cdot } \forall p \in [ 1 , \infty )$ , the p-norm of vector is $\vert \vert X \vert \vert _ { p } ^ { p } = ( \sum ^ { r } \vert x _ { i } \vert ^ { p } ) ^ { \frac { 1 } { p } }$ and $\left| \left| X \right| \right| _ { \infty } ^ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq r } ( \left| x _ { i } \right| )$ . The ¼inner product of 2 vectors X and i 1 $\mathbf { Y } \in \Re ^ { r }$ is denoted by $X ^ { T } Y = \sum _ { i = 1 } ^ { r } \ x _ { i } y _ { i }$ . A matrix $M \in \Re ^ { n \times r }$ is a real $n \times r -$ <sup>¼</sup>dimensional matrix. $M _ { i }$ denotes the ith row of M and $M _ { j }$ denotes the jth column of M. $M ^ { T }$ is the transpose of M. The identity matrix is denoted by I. $\varPhi$ is the mapping from the input space to the feature space, Φ: $A \longrightarrow F . K ( \cdot , \cdot ) / \mathrm { K }$ ernel function is the inner/scalar product in feature space. Positive semidefinite matrix is a Hermitian matrix all of whose eigenvalues are nonnegative. Linear programming (LP) problems are optimization problems with linear objective function and linear constraints. Nonlinear programming problems are optimization problems with nonlinear function in the objective function/the constraints or both. TP (True Positive): The number of records in Bad class that is classified correctly. FP (False Positive, False Alarm): The number of records in Normal class that is classified as Bad class. TN (True Negative): The number of records in Normal class that is classified correctly. FN (False Negative): The number of records in Bad class that is classified as Normal class.

## 2. Multi-criteria Convex Quadratic Programming model

In this section, we present a Multi-criteria Convex Quadric Programming model (MCQP) classification model based on the idea of maximizing the external distance between groups and minimizing the internal distance within a certain group [10,13,17]. The proposed MCQP model is highly efficient because it only needs to solve linear equations to find the global optimal solution and obtain the classifier. Kernel functions are also introduced to our model to solve nonlinear problems. Furthermore, we demonstrate the theoretical relationship between our models and SVM. By selecting different p-norm in objective function, our model can be converted to a standard Support Vector Machine classification model.

## 2.1. MCQP model formulation

Suppose we want to classify data in r-dimensional real space $\Re ^ { r }$ into two distinct groups via a hyperplane defined by a kernel function and multiple criteria. The following models represent this concept mathematically:

Each row of a n × r matrix $\pmb { A } = ( A _ { 1 } , . . . , A _ { n } ) ^ { T }$ is a vector $\mathbf { \mathcal { A } } _ { i } { = } ( a _ { i 1 } , . . . , ~ a _ { i r } ) { \in } \Re ^ { r }$ that corresponds to one of the records in the training dataset of a binary classification problem, $i { = } 1 , . . . , n ;$ n is the total number of records in the dataset. Two groups, $G _ { 1 }$ and $G _ { 2 }$ , are pre-defined while $G _ { 1 } \cap G _ { 2 } { = } \varPhi$ and $A _ { i } \in \{ G _ { 1 } \cup G _ { 2 } \}$ . A boundary scalar b can be selected to separate $G _ { 1 }$ and $G _ { 2 }$ . Let $\mathbf { X } { = } ( x _ { 1 } , . . . , x _ { r } ) ^ { T } { \in } \Re ^ { r }$ be a vector of real number to be determined. Thus, we can establish the following linear inequations for a linear separable dataset [8]:

$$
\boldsymbol {A} _ {i} \mathbf {X} <   b, \quad \forall \boldsymbol {A} _ {i} \in G _ {1};\tag{1}
$$

$$
\boldsymbol {A} _ {i} \boldsymbol {X} \geq b, \quad \forall \boldsymbol {A} _ {i} \in G _ {2};\tag{2}
$$

To formulate the criteria and constraints for data separation, some variables need to be introduced. In the classification problem, $\mathbf { \Delta } A _ { i } \mathbf { X }$ is the score for the ith record. If an element $A _ { i }$ is correctly classified, then let $\beta _ { i }$ be the distance from $A _ { i }$ to $^ { b , }$ and consider the linear system, $A _ { i } \mathbf { X } { = } b { - } \beta _ { i } , \forall A _ { i } \in G _ { 1 }$ and $A _ { i } \mathbf { X } { = } b + \beta _ { i } , \forall A _ { i } { \in } G _ { 2 }$ . However, if we consider the case where the two groups are not linear separable because of mislabeled records, a “Soft Margin” and slack distance variable $\mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega }$ need to be introduced. Previous equations now transforms to ${ \bf \nabla } A _ { i } { \bf X } =$ $b + \alpha _ { i } - \beta _ { i } , \forall A _ { i } \in G _ { 1 }$ and $A _ { i } \mathbf { X } = \boldsymbol { b } - \alpha _ { i } + \beta _ { i } , \forall A _ { i } \in G _ { 2 }$ . To complete the definitions of $\beta _ { i }$ and $\alpha _ { i } ,$ let $\beta _ { i } { = } 0$ for all misclassified elements and $\boldsymbol { \alpha } _ { i } = 0$ for all correctly classified elements. By incorporating the definitions of $\beta _ { i }$ and $\alpha _ { i } , ( 1 )$ and (2) can be reformulated as three models: Medium, Strong and Weak.

$( M e d i u m ~ M o d e l ) ~ A _ { i } { \bf X } = b + \alpha _ { i } - \beta _ { i } , ~ \forall A _ { i } \in G _ { 1 }$ and $A _ { i } \mathbf { X } = \boldsymbol { b } - \alpha _ { i } + \beta _ { i } , \forall A _ { i } \in G _ { 2 } ,$ (Strong Model) $A _ { i } \mathbf { X } = b - { \boldsymbol { \delta } } + \alpha _ { i } - \beta _ { i } , \forall A _ { i } \in G _ { 1 }$ and $A _ { i } { \bf X } = b + \delta - \alpha + \beta _ { i } , \forall A _ { i } \in G _ { 2 } , \delta$ is a given scalar. $b - \delta$ and $b { + } \delta$ are two adjusted hyper planes for strong model. (Weak Model) $A _ { i } \mathbf { X } = b + \delta + \alpha _ { i } - \beta _ { i } , ~ \forall A _ { i } \in G _ { 1 }$ and $A _ { i } { \bf X } = b - \delta - \alpha _ { i } + \beta _ { i } , \ \forall A _ { i } \in G _ { 2 } ,$ , δ is a given scalar. $b { + } \delta$ and $b - \delta$ are two adjusted hyper planes for weak model. A loosing relationship of the Medium, Strong, and Weak models is given as:

## Theorem 1.

(i) A feasible solution of Strong Model is the feasible solution of Medium and Weak Model.

(ii) A feasible solution of Medium Model is the feasible solution of Weak Model.

(iii) If a data case $A _ { i }$ is classified as a given class $G _ { j }$ by Strong Model, then it may be in $G _ { j }$ by using Medium Model and Weak Model.

(iv) If a data case $A _ { i }$ is classified as a given class $G _ { j }$ by model Medium Model, then it may be in $G _ { j }$ by using Weak Model.

Proof. Let Feas = Feasible area of Strong $\mathrm { M o d e l } , \mathrm { F e a s } _ { 2 } { = }$ Feasible area of Medium Model, and ${ \mathrm { F e a s } } _ { 3 } { = } \mathrm { F }$ easible area of Weak Model.

$$
\forall X _ {s} ^ {*} \in \text { Feas } _ {1}, X _ {s} ^ {*} \in \text { Feas } _ {2} \text { and } X _ {s} ^ {*} \in \text { Feas } _ {3}.
$$

$$
\forall X _ {m} ^ {*} \in \text { Feas } _ {2}, X _ {m} ^ {*} \in F e a s _ {3}.
$$

Obviously, we will have Fea ${ \mathfrak { i } } _ { 1 } \subseteq \mathrm { F e a s } _ { 2 } \subseteq \mathrm { F e a s } _ { 3 } , { \mathrm { s o } }$ (i) and (ii) is true.

(iii) and (iv) are automatically true from the conclusion of (i) and (ii) for a certain value of $\delta { > } 0$ □

Redefine X as $\mathbf { X } / \delta , b$ as $b / \delta , \alpha _ { i }$ as $\alpha _ { i } / \delta , \beta _ { i }$ as $\beta _ { i } / \delta ,$ , and introduce

$$
\delta^ {\prime} = \left\{ \begin{array}{l} 1, \text { Strong   Model } \\ 0, \text { Medium   Model }, \\ - 1, \text { Weak   Model } \end{array} \right.
$$

Define a $n \times n$ diagonal matrix Y which only contains $^ { * * } + 1 ^ { * } \mathrm { o r } ^ { * * } - 1 ^ { * }$ indicates the class membership. $\mathrm { A } ^ {  } - 1 ^ { \ ' }$ in row i of matrix Y indicates the corresponding record $\mathbf { } A _ { i } { \in } G _ { 1 }$ and a $\cdot ^ { \left. } + 1 ^ { \right. }$ in row i of matrix Y indicates the corresponding record $\mathbf { } A _ { i } { \in } G _ { 2 }$ . The above three models can be rewritten as a single constraint:

$$
\boldsymbol {Y} (<   \boldsymbol {A} \cdot \boldsymbol {X} > e b) = \delta^ {\prime} + \alpha - \beta ,
$$

where $e { = } ( 1 , 1 , . . . , 1 ) ^ { T } , \alpha { = } ( \alpha _ { 1 } { , } . . . , \alpha _ { n } ) ^ { T }$ and $\beta { = } ( \beta _ { 1 } , . . . , \beta _ { n } ) ^ { T } .$

The proposed multi-criteria optimization problem contains three objective functions. The first mathematical function $f ( \alpha ) = | | \alpha | | _ { p } ^ { p } = \sum | \alpha _ { i } | ^ { p } \ ( 1 \leq p \leq \infty )$ dei=1 <sup>i</sup>¼<sup>1</sup>scribes the summation of total overlapping distance of misclassified records to b. The second function $g ( \beta ) =$ $\vert \vert \beta \vert \vert _ { q } ^ { q } = \sum _ { i = 1 } ^ { n } \vert \beta _ { i } \vert ^ { q } ( 1 \leq q \leq \infty )$ represents the aggregation <sup>¼</sup>of total distance of correctly separated records to b. The distance between the two adjusted bounding hyper planes is defined as $( \frac { 2 } { | | X | | _ { s } ^ { s } } )$ in geometric view. In order to <sup>jj jj</sup>maximize this distance, a third function $h ( X ) = { \frac { \| X \| _ { s } ^ { s } } { 2 } }$ <sup>ð Þ ¼</sup>should be minimized. The final accuracy of this classification problem depends on simultaneously minimize $f ( \alpha )$ , minimize $h ( X )$ and maximize $g ( \beta )$ . Thus, a multicriteria programming model for classification can be formulated as:

(Generalized Model) Minimize f (α), minimize $h ( X )$ and maximize $g ( \beta )$

Subject to:

$$
\boldsymbol {Y} (<   \boldsymbol {A} \cdot \boldsymbol {X} > - e b) = \delta^ {\prime} + \alpha - \beta ,
$$

$$
\alpha_ {i}, \beta_ {i} \geq 0, 1 \leq i \leq n
$$

where Y is a given n × n diagonal matrix, $e { = } ( 1 , 1 , . . . , 1 ) ^ { T } ,$ $\alpha = ( \alpha _ { 1 } , . . . , \alpha _ { n } ) ^ { T } , \beta { = } ( \beta _ { 1 } , . . . , \beta _ { n } ) ^ { T }$ , X and b are unrestricted. Fig. 1 shows the geometric view of our two-class model. Squares indicate group “+” and dots represent group $^ { 6 6 } - ^ { 5 9 }$ . In order to separate groups via the X vector by a hyperplane b, we set up two Max and one Min objectives. Max objectives maximize the sum of distance from the points to their boundary and the distance between the two adjusted boundaries. Min objective minimizes the total overlapping.

Furthermore, to transform the multi-criteria classification model into a single-criterion problem, a weight vector $( W _ { \alpha } , W _ { \beta } )$ , weights $W _ { \alpha } + W _ { \beta } { = } 1 , { > } 0$ and $W _ { \beta } { > } 0$ , is introduced for f(α) and $g ( \beta )$ , respectively. The values of $W _ { \alpha }$ and $W _ { \beta }$ can be arbitrary pre-defined and then optimized by cross-validation in the process of identifying the optimal solution to indicate the relative importance of the three objectives. We assume that $W _ { \beta } { < } W _ { \alpha }$ and consider minimizing misclassification rates has higher priority than maximizing distance of correctly separated records to the boundary in classification problems. The generalized model can then be converted into a single-criterion mathematical programming model:

(Model 1) Minimize $\begin{array} { r } { \frac 1 2 \| X \| _ { s } ^ { s } + W _ { \alpha } \| \alpha \| _ { p } ^ { p } - W _ { \beta } \| \beta \| _ { q } ^ { q } } \end{array}$ Subject to: $Y ( < A \cdot \bar { X ^ { > } } - e b ) { = } \delta ^ { \prime } e - \alpha + \bar { \beta }$

$$
\alpha_ {i}, \beta_ {i} \geq 0, 1 \leq i \leq n
$$

where Y is a given $n \times n$ diagonal matrix, $e { = } ( 1 , 1 , . . . , 1 ) ^ { T } ,$ $\alpha = ( \alpha _ { 1 } , . . . , \alpha _ { n } ) ^ { T } , \beta = ( \beta _ { 1 } , . . . , \beta _ { n } ) ^ { T } ,$ , X and b are unrestricted.

Note that the introduction of $\beta _ { i }$ is one of the major differences between the proposed model and existing Support Vectors approaches [44,47].

Different values of $s , p$ and q will lead to different forms of Model 1. If $s = p { = } q { = } 1$ , Model 1 becomes a linear programming problem. If any of $s , p$ or $p$ is greater than 1, Model 1 becomes a nonlinear problem.

![](/api/attachments/X5AS9MWJ/fulltext/images/a9e9cde31c6185ab523b8029bfbf2e264de4d61fc89e38e81db203bdd1f81490.jpg)  
Fig. 1. A two-class model.

Since it is much easier to find optimal solutions for convex programming form than any other forms of nonlinear programming, our study will focus on convex models. Without losing generality, let $s { = } 2 , p { = } 2$ and $q = 1$ and Model 1 is now a convex quadratic programming form. The constraints remain the same and the objective function becomes: bjective function becomes

(Model 2) Minimize $\frac { 1 } { 2 } \left| \left| X \right| \right| _ { 2 } ^ { 2 } + W _ { \alpha } \sum _ { i = 1 } ^ { n } \ \alpha _ { i } ^ { 2 } - W _ { \beta } \sum _ { i = 1 } ^ { n } \ \beta _ { i }$ Subject to: $Y \left( < A \cdot X > - e b \right) = \delta ^ { \prime } e ^ { - \frac { i = 1 } { \alpha } + } \beta$

In order to reduce the number of variables involved in the model and thus simplify the computing, let $\eta _ { i } =$ ${ \alpha _ { i } - \beta _ { i } }$ . According to our previous definitions, $\eta = \alpha _ { i }$ for all misclassified records and $\eta _ { i } = - \beta _ { i }$ for all correctly separated records.

To add strong convexity to the objection function, we add $\begin{array} { r } { \frac { W _ { b } } { 2 } b ^ { 2 } } \end{array}$ to the objective function of Model 2. The weight $W _ { b }$ is an arbitrary positive number. Previous computation results [9] show that this change will not affect the optimal solution if we let $W _ { b } \ll W _ { \beta } .$ Model 2 becomes: becomes:

(Model 3) Minimize ${ \frac { 1 } { 2 } } \left| \left| X \right| \right| _ { 2 } ^ { 2 } + { \frac { W _ { \alpha } } { 2 } } \sum _ { i = 1 } ^ { n } \ \eta _ { i } ^ { 2 } + W _ { \beta } \sum _ { i = 1 } ^ { n } \ \eta _ { i } +$ ${ \frac { W _ { b } } { 2 } } b ^ { 2 }$

Subject to: $Y ( < A \cdot X > - e b ) { = } \delta ^ { \prime } e - \eta$ where Y is a given $n \times n$ diagonal matrix, $e { = } ( 1 , 1 , . . . , 1 ) ^ { T } ,$ $\boldsymbol { \eta } { = } ( \eta _ { 1 } , . . . , \eta _ { n } ) ^ { T } , \eta , X$ and b are unrestricted, $1 \leq i \leq n$

$$
\begin{array}{l} L (X, b, \eta , \theta) = \frac {1}{2} | | X | | _ {2} ^ {2} + \frac {W _ {\alpha}}{2} \sum_ {i = 1} ^ {n} \eta_ {i} ^ {2} + W _ {\beta} \sum_ {i = 1} ^ {n} \eta_ {i} \\ \qquad + \frac {W _ {b}}{2} b ^ {2} - \theta^ {T} (Y (<   A \cdot X > - e b) - e \delta^ {\prime} + \eta) \end{array}
$$

where $\theta = ( \theta _ { 1 } , . . . , \theta _ { n } ) ^ { T } , \eta { = } ( \eta _ { 1 } , . . . , \eta _ { n } ) ^ { T } , \theta _ { i } , \eta _ { i } { \in } \Re$

According to Wolfe Dual Theorem [52], we have:

$$
\begin{array}{r l} & {\nabla_ {X} L (X, b, \eta , \theta) = X - A ^ {T} Y \theta = 0,} \\ & {\nabla_ {b} L (X, b, \eta , \theta) = W _ {b} b + e ^ {T} Y \theta = 0,} \\ & {\nabla_ {\eta} L (X, b, \eta , \theta) = W _ {\alpha} \eta + W _ {\beta} e - \theta = 0} \end{array}\tag{3}
$$

Introduce the above equations to the constraints of Model 3, we can get:

$$
\begin{array}{l} Y \bigg ((A \cdot A ^ {T}) Y \theta + \frac {1}{W _ {b}} e (e ^ {T} Y \theta) \bigg) + \frac {1}{W _ {\alpha}} (\theta - W _ {\beta} e) \\ = \delta^ {\prime} e \Rightarrow \theta = \frac {\left(\delta^ {\prime} + \frac {W _ {\beta}}{W _ {\alpha}}\right) e}{\frac {I}{W _ {\alpha}} + Y ((A \cdot A ^ {T}) + \frac {1}{W _ {b}} e e ^ {T}) Y} \end{array}\tag{4}
$$

Theorem 2. For some $\begin{array} { r } { W _ { \alpha } { > } 0 , \theta = \frac { \left( \delta ^ { \prime } + \frac { W _ { \beta } } { W _ { \alpha } } \right) e } { \frac { I } { W _ { \alpha } } + Y \left( ( A \cdot A ^ { T } ) + \frac { 1 } { W _ { b } } e e ^ { T } \right) Y } } \end{array}$ exists.

Proof. Let $\begin{array} { r } { H { = } Y \bigg [ A - \Big ( \frac { 1 } { W _ { b } } \Big ) ^ { \frac { 1 } { 2 } } e \bigg ] , } \end{array}$ , we thus see that:

$$
\theta = \frac {\left(\delta^ {\prime} + \frac {W _ {\beta}}{W _ {\alpha}}\right) e}{\left(\frac {I}{W _ {\alpha}} + H H ^ {T}\right)}\tag{4}
$$

∀H, $\exists W _ { \alpha } \geq \varepsilon > 0$ , and $\forall i , j \in [ 1$ , size of $( H H ^ { T } ) ]$

We may have $\begin{array} { r } { \left( \frac { I } { W _ { \alpha } } \right) _ { i , i } > \rvert ( H H ^ { T } ) _ { i , i } \rvert } \end{array}$ and the inversion of $\begin{array} { r } { ( \frac { I } { W _ { \alpha } } + H H ^ { T } ) } \end{array}$ i;i exists.

$$
\text { So   } \theta = \frac {\left(\delta^ {\prime} + \frac {W _ {\beta}}{W _ {\alpha}}\right) e}{\frac {I}{W _ {\alpha}} + Y \left((A \cdot A ^ {T}) + \frac {1}{W _ {b}} e e ^ {T}\right) Y} \text {   exists. }
$$

## 2.2. Epsilon-support vector

In existing SVM approaches [1], the sparsity of the optimal $\boldsymbol { \alpha } _ { i } ^ { * }$ (many of $\boldsymbol { \alpha } _ { i } ^ { * } { = } 0 )$ is the key in solving largescale SVM problem and the support vectors $( \alpha _ { i } ^ { * } { = } 0 )$ are the points at the hyperplane. Similarly, the support vector $A _ { i }$ of our models can be defined as $\alpha _ { i } ^ { * } { = } \beta _ { i } ^ { * } { = } 0$ . Due to the formulation of the model objectives, almost none of the data points $A _ { i }$ lie on two adjusted bounding hyper planes $b { \pm } 1$ . Thus most of the time $\boldsymbol { \alpha } _ { i } ^ { * }$ and $\beta _ { i } ^ { * }$ do not equal to zero simultaneously. A Karush–Kuhn–Tucker (KKT) condition that has been used in previous support vector approaches [6,37] cannot be held any more because of the introduction of distance variable $\beta _ { i }$ in our model. As a result, we need to establish another condition for those data points $A _ { i } ,$ whose corresponding $| \alpha _ { i } ^ { * } - \beta _ { i } ^ { * } | < \varepsilon ,$ , to define the epsilon-support vectors (eSVs) such that the computation complexity can be reduced for large-scale problems. ε is picked so that only a small part (e.g. 1%) of the records belongs to epsilon-support vectors. Generally, if $n { < } 1 , 0 0 0 { , } 0 0 0$ , Model 3 can use the whole dataset; otherwise, a sample training set (e.g. 1% of the population) can be randomly generated from the original data. Using the sample set, we can find an optimal solution and epsilon-support vectors for the original dataset. All epsilon-support vectors are used to re-train the model repeatedly until the classification results meet certain criteria or threshold. A stratified random sampling approach is incorporated into our algorithm for large-scale data mining problem $( > O ( 1 0 ^ { 9 } ) )$ ).

The following algorithm summarized the whole process:

Algorithm 1. Input: The training dataset A as the population, n is the number of observation in the population and is a huge number; m is the number of subpopulations that can be fitted into main memory; The testing dataset $A ^ { \prime } { ; }$ Algorithm Stop criteria.

Output: Average classification accuracies; decision score for every record; decision function.

Step 1: A is evenly partitioned into m subpopulations or strata by random selection.

Step 2: One random sample is drawn from each of m subpopulations and formulates the first training set Tr.

Step 3: Compute ${ \boldsymbol { \theta } } ^ { * } { = } ( \theta , . . . , \theta _ { n } ) ^ { T }$ using Tr as input. $W _ { \beta } , W _ { \alpha } , W _ { b }$ are chosen by cross-validation.

Step 4: Compute $\begin{array} { r } { \boldsymbol { X } ^ { * } = \boldsymbol { A } ^ { T } \boldsymbol { Y } \boldsymbol { \theta } ^ { * } , \boldsymbol { b } ^ { * } = \frac { - 1 } { W _ { h } } \boldsymbol { e } ^ { T } \boldsymbol { Y } \boldsymbol { \theta } ^ { * } } \end{array}$ . If the performance measures meet the preset criteria (accuracy, total computation time, etc.) and the iteration times ${ \scriptstyle \sum 1 0 }$ (<sup>⁎</sup>), stop; otherwise go to Step 5.

Step 5: Compute $| \alpha _ { i } ^ { * } - \beta _ { i } ^ { * } |$ for all observations in $A .$

Step 6: Suppose we have $n _ { I }$ observations (epsilon-support vectors (eSVs)) which $| \alpha _ { i } ^ { * } - \beta _ { i } ^ { * } | < \varepsilon$ and $n _ { 2 }$ observations (Non epsilon-support vectors) which $| \alpha _ { i } ^ { * } - \beta _ { i } ^ { * } | { > } \varepsilon$ . Formulate a new set with all $n _ { I } { \mathrm { e S V s } }$ and some $( n _ { 3 } , \ n _ { 3 } \leq n _ { 2 }$ and $n _ { 3 } \cong 1 0 \% ^ { * } n _ { I } )$ non-eSVs. If $( n _ { 3 } + n _ { I } ) \le m$ , the new set becomes the new training set; otherwise, randomly sample m observations from the new set to formulate a train set. Go back to Step 3.

END

<sup>⁎</sup>Iteration times must be greater than 10 to minimize the influence of the selection of initial training dataset.

Appendix B (epsilon-support vector and large-scale Data Mining Problem) summarized an experimental study that tested the applicability of Algorithm 1 on large synthetic classification problem $\scriptstyle \left( > \mathbf { O } ( 1 0 ^ { 9 } ) \right)$ ).

## 2.3. Nonlinear classifier and Kernel function

In order to find ways to create nonlinear classifiers, we may transform the original input space to high dimension feature space by a nonlinear transformation. Thus, a nonlinear hyperplane in original space may be linear in the high-dimensional feature space. For example, every inner product $( A _ { i } \cdot A _ { j } )$ in Model 3 can be replaced by a nonlinear kernel function $\mathrm { K } ( A _ { i } , A _ { j } )$ , which will extend the applicability of the proposed model to linear inseparable datasets. However, it is difficult to directly introduce kernel function to Model 3. Let ${ \bf K } ( { \cal A } , { \cal A } ^ { T } ) { = } \varPhi ( { \cal A } ) \varPhi ( { \cal A } ^ { T } )$ be a kernel function. If we only replace $\boldsymbol { A } \boldsymbol { A } ^ { T }$ with $\mathbf { K } ( A \mathcal { A } ^ { T } )$ , we have to compute $\boldsymbol { X } ^ { * } \boldsymbol { = } \boldsymbol { \varPhi } ( \boldsymbol { \bar { A } } ^ { T } ) \boldsymbol { Y } \boldsymbol { \theta } ^ { * }$ to get the decision function. However, the computation of $\varPhi ( A )$ or $\boldsymbol { \varPhi } ( \boldsymbol { A } ^ { T } )$ is almost impossible. In order to get ride of this problem, we replace X by $A ^ { T } Y \theta$ and $A A ^ { T }$ with $\mathbf { K } ( A , A ^ { T } )$ and Model 3 now becomes Model $3 ^ { \prime }$ Since $W _ { \beta } , W _ { \alpha } , W _ { b }$ are changeable, the change in objective function in Model $3 ^ { \prime }$ will not affect the optimal solution.

(Model 3′) Minimize ${ \frac { 1 } { 2 } } \| \theta \| _ { 2 } ^ { 2 } + { \frac { W _ { \alpha } } { 2 } } \sum _ { i = 1 } ^ { n } \ \eta _ { i } ^ { 2 } + W _ { \beta } \sum _ { i = 1 } ^ { n } \ \eta _ { i } +$ $\begin{array} { r } { \frac { W _ { b } } { 2 } b ^ { 2 } } \end{array}$

Subject to: $Y ( { \bf K } ( { \cal A } , { \cal A } ^ { T } ) Y \theta - e b ) { = } { \mathrm { i s ~ } } \delta ^ { \prime } e - \eta$

The Lagrange function corresponding to Model $3 ^ { \prime }$ is

$$
\begin{array}{l} L (\theta , b, \eta , \rho) = \frac {1}{2} | | \theta | | _ {2} ^ {2} + \frac {W _ {\alpha}}{2} \sum_ {i = 1} ^ {n} \eta_ {i} ^ {2} + W _ {\beta} \sum_ {i = 1} ^ {n} \eta_ {i} \\ \qquad + \frac {W _ {b}}{2} b ^ {2} - \rho^ {T} \big (Y \big (K \big (A, A ^ {T} \big) Y \theta - e b \big) - e \delta^ {\prime} + \eta \big) \end{array}
$$

where $\boldsymbol { \theta } = ( \theta _ { 1 } , . . . , \ \theta _ { n } ) ^ { T } , \ \eta { = } ( \eta _ { 1 } , . . . , \ \eta _ { n } ) ^ { T } , \ \rho { = } ( \rho _ { 1 } , . . . , \ \rho _ { n } ) ^ { T } ,$ $\theta _ { i } , \eta _ { i } , \rho _ { i } \in \Re$

$$
\begin{array}{l} \nabla_ {\theta} L (\theta , b, \eta , \rho) = \theta - Y (\mathbf {K} \big (\boldsymbol {A}, \boldsymbol {A} ^ {T} \big) ^ {T} Y \rho = 0, \\ \nabla_ {b} L (\theta , b, \eta , \rho) = W _ {b} b + e ^ {T} Y \rho = 0, \\ \nabla_ {\eta} L (\theta , b, \eta , \rho) = W _ {\alpha} \eta + W _ {\beta} e - \rho = 0. \end{array}\tag{5}
$$

Introduce these 3 equations in (5) to the constraints of Model $3 ^ { \prime }$ , we can get:

$$
\begin{array}{l} Y \left(K (A, A ^ {T}) Y Y K (A, A ^ {T}) ^ {T} Y \rho + \frac {1}{W _ {b}} e (e ^ {T} Y \rho)\right) \\ = \delta^ {\prime} e - \frac {1}{W _ {\alpha}} (\rho - W _ {\beta} e) \Rightarrow \rho \\ = \frac {\left(\delta^ {\prime} + \frac {W _ {\beta}}{W _ {\alpha}}\right) e}{\frac {I}{W _ {\alpha}} + Y \left(K (A , A ^ {T}) K (A , A ^ {T}) ^ {T} + \frac {1}{W _ {b}} e e ^ {T}\right) Y} \end{array}\tag{6}
$$

Theorem 3. For some, $\begin{array} { r } { W _ { \alpha } > 0 , \rho = \frac { \left( \delta ^ { \prime } + \frac { W _ { \beta } } { W _ { x } } \right) e } { \frac { I } { W _ { x } } + Y \left( K \left( A , A ^ { T } \right) K \left( A , A ^ { T } \right) ^ { T } + \frac { 1 } { W _ { b } } e e ^ { T } \right) Y } } \end{array}$ exists.

Proof. Let $\begin{array} { r } { H = Y \bigg [ K ( A , A ^ { T } ) - \Big ( \frac { 1 } { W _ { b } } \Big ) ^ { \frac { 1 } { 2 } } e \bigg ] } \end{array}$ , we thus see that:

$$
\rho = \frac {\left(\delta^ {\prime} + \frac {W _ {\beta}}{W _ {\alpha}}\right) e}{\left(\frac {I}{W _ {\alpha}} + H H ^ {T}\right)}\tag{\( (6') \}
$$

$\forall H , \exists W _ { \alpha } \geq \varepsilon > 0 .$ , and $\forall i , j \in 1$ , size of $( H H ^ { T } )$

We may have $\left( \frac { I } { W _ { \alpha } } \right) _ { i , i } > \bar { | } ( H H ^ { T } ) _ { i , i } |$ and the inversion of $\begin{array} { r } { ( \frac { I } { W _ { \alpha } } + H H ^ { T } ) } \end{array}$ exists.

$$
\text { So } \rho = \frac {\left(\delta^ {\prime} + \frac {W _ {\beta}}{W _ {\alpha}}\right) e}{\frac {I}{W _ {\alpha}} + Y \left(K (A , A ^ {T}) K (A , A ^ {T}) ^ {T} + \frac {1}{W _ {b}} e e ^ {T}\right) Y} \text { exists. }
$$

Algorithm $1 ^ { \prime }$ describes how to use Model $3 ^ { \prime }$ in a classification problem.

Algorithm 1′. Input: A n × r matrix A as the training dataset, a $n \times n$ diagonal matrix Y labels the class of each record, a kernel function $\operatorname { K } ( A _ { i } , A _ { j } )$

Output: Classification accuracies for each group in the training dataset, score for every record, decision function.

Step 1: Compute $\rho ^ { * } \substack { = } ( \rho _ { 1 } , . . . , \rho _ { n } ) ^ { T } \mathfrak { b } \mathrm { y } \left( 6 \right) . \ W _ { \beta } , \ W _ { \alpha } , \ W _ { b }$ are chosen by cross-validation.

Step 2: Classify an incoming $A _ { i }$ by using decision function

$$
\left(\left(K \big (A _ {i}, A ^ {T} \big) K \big (A, A ^ {T} \big) ^ {T} + \frac {1}{W _ {b}} e ^ {T}\right) Y \rho^ {*}\right) \left\{ \begin{array}{l} > 0, \Rightarrow A _ {i} \in G _ {1} \\ \leq 0, \Rightarrow A _ {i} \in G _ {2} \end{array} \right..
$$

END

There are similarities and differences between the models presented in this section and Support Vector Machines. Appendix $\mathrm { C } ( \mathrm A$ comparison of our model with SVM) discussed and summarized these relationships.

## 3. Experiments in credit data analysis

In this section we applied our MCQP model to realworld credit datasets. The data used in our analysis come from four countries and represent four aspects of credit risk: consumer credit card application, credit card transaction, loan approval, and corporation bankruptcy. Credit risk analysis is an important task for financial institutions. It helps credit card issuers or banks to better manage their credit balances and establish appropriate policies for different categories of credit accounts. It is a challenge to classify and predict potential bankruptcies or defaulters in a reliable precision due to the dynamic nature of defaulters behaviors. Discriminant analysis is one of the most popular quantitative tools in credit risk analysis [36]. Integer programming, logistic regression, decision trees, association rule, expert systems, neural networks, genetic programming, and dynamic models are also widely used [54,36,45]. Relatively few mathematical programming tools [14,18,43] have been explored and applied to credit risk analysis.

Each record in these four datasets has a class label to indicate its' financial status: either Normal or Bad. Bad indicates a bankrupt credit or firm account and Normal indicates a current status account. The result of the MCQP model is compared with four well-known classification methods: Linear Discriminant Analysis (LDA) [44], Decision Tree based See5 [34,35], SVMlight [15–17] and LibSVM [5].

The basic idea of credit risk classification is to build classifiers based on known class labels and uses the established classifiers to predict class labels of unknown data. The common features of the four data are that they are related to credit risk analysis and are two-class datasets without missing values. The differences are that they concern about different credit aspects and have different number of records and variables. The first benchmark set is a German credit card application dataset from UCI Machine Learning databases [29]. The set contains 1000 records (700 Normal and 300 Bad) and 24 variables. The second set is an Australian credit approval dataset from See5 [35]. It has 690 records (383 Normal and 307 Bad) and 15 variables. The third set is a Japanese firm bankruptcy set [21], which collects 37 bankrupt (Bad) sample Japanese firms and 111 nonbankrupt (Normal) sample Japanese firms from 1989 to 1999. Each record has 13 variables. The last dataset is from a major US bank and contains 6000 credit card data (5040 Normal and 960 Bad) and 64 variables [19,20,32,33], which describe cardholders' behaviors. The experiment was carried out according to the Credit Classification Process:

## 3.1. Credit Classification Process

Input: The dataset $A = \{ A _ { 1 } , ~ A _ { 2 } , ~ A _ { 3 } , . . . , ~ A _ { n } \}$ , a $n \times n$ diagonal matrix $\pmb { Y } \bigg ( Y _ { i , i } \Big \{ = + 1 , \quad i { \in } \{  \mathrm { B a d } \}  \\ { = - 1 , i { \in } \{ } \mathrm { N o r m a l } \} \bigg )$

<sup>¼ - f g</sup>Output: Average classification accuracies of 10- fold cross-validation for Bad and Normal; decision score for every record; decision function.

Step 1: Apply classification methods: LDA, Decision Tree, SVM, MCQP (Model 3, Algorithm 1), to A using 10-fold cross-validation. The outputs are a set of decision functions, one for each classification method.

Step 2: Compute the classification accuracies using the decision functions from Step 1.

END

Because different performance metrics are appropriate in different settings [4], five evaluation criteria: accuracy, KS score, type I and II errors, and correlation coefficient, were used to evaluate the classification methods. Accuracy is one the most widely used classification performance metrics. It is the ratio of correctly predicted records to the entire records or records in a particular class.

$$
\text { Overall   Accuracy } = \frac {\mathrm{TN} + \mathrm{TP}}{\mathrm{TP} + \mathrm{FP} + \mathrm{FN} + \mathrm{TN}},
$$

$$
\text { Normal   Accuracy } = \frac {\mathrm{TN}}{\mathrm{FP} + \mathrm{TN}},
$$

$$
\text { Bad   Accuracy } = \frac {\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}}.
$$

Type I error is defined as the percentage of predicted Normal records that are actually Bad records and Type II error is defined as the percentage of predicted Bad records that are actually Normal records [41,42]. Since Type I error indicates the potential charge-off loss of credit issuers, it is considered more important than Type II error from credit issuers' point of view.

$$
\text { Type   I   error } = \frac {\mathrm{FN}}{\mathrm{FN} + \mathrm{TN}}, \text { Type   II   error } = \frac {\mathrm{FP}}{\mathrm{FP} + \mathrm{TP}}.
$$

A popular measurement in credit risk analysis, KS score, was also calculated. The higher the KS score, the better the classification methods. The KS (Kolmogorov–Smirnov) value is defined as:

KS value =Max |Cumulative distribution of Bad − Cumulative distribution of Normal|.

Another measurement— Correlation coefficient, which falls into the range of [−1, 1], was used to avoid the negative impacts of imbalanced classes. The correlation coefficient is −1 if the predictions are completely contrary to the real value, 1 if the predictions are 100% correct, and 0 if the predictions are randomly produced. The Correlation coefficient is calculated as follows:

Correlation coefficient

$$
= \frac {(\mathrm{TP} \times \mathrm{TN}) - (\mathrm{FP} \times \mathrm{FN})}{\sqrt {(\mathrm{TP} + \mathrm{FN}) (\mathrm{TP} + \mathrm{FP}) (\mathrm{TN} + \mathrm{FP}) (\mathrm{TN} + \mathrm{FN})}}.
$$

Tables 1, 2, 3 and 4 in Appendix A report the averages of 10-fold cross-validation results of the five classification methods for the German set, Australian set, Japanese set, and US set, respectively. Due to the space limitation, we only list the detailed 10-fold cross-validation results of MCQP for the US set (Table 5). Each table summarizes the five metrics for training and test sets. Training results indicate how well the classification model fits the training set while test results reflect the real predicting power of the model. Among the five methods, LibSVM achieved the best performance on all five metrics for the German set, but performs poorly on the Australian set (27.1% accuracy for Bad, 45.62% Type I error rate, 13.99 KS, 0.174 correlation coefficient), comparing to LDA, See5, and MCQP. SVMlight did not perform well for the German set neither (18.03% accuracy for Normal, 34.14% Type I error rate, 8.69 KS, 0.126 correlation coefficient). LDA yielded the best accuracy for Bad, Type I error rate, KS score, and correlation coefficient for the Australian set. It also has the best accuracy for Normal, Type II error rate, KS score, and correlation coefficient for the US set and exhibits comparative results on the other two sets. See5 has the best accuracies for Overall and Normal for the Australian and Japanese sets. SVMlight performs about average for the German and US sets, but poorly for the Japanese and Australian sets. MCQP has the best accuracy for Overall and Normal, Type I and II error rates, KS score, and correlation coefficient for the Japanese set and the best accuracy for Bad, Type I error rate for the US sets. It also has above average performance on the German and Australian sets.

The experimental study indicates that (1) MCQP achieves comparable results to some well-known classification techniques; (2) the performance of classification methods may vary when the datasets have different characteristics.

## 4. Conclusion

This study makes three major contributions. First, we presented a novel approach for classification problems based on multiple criteria mathematical programming [41]. The basic idea is to maximize the external distance between groups and minimize the internal distance within a certain group [9]. Kernel functions are also introduced to our model to solve nonlinear problems. Furthermore, we demonstrated the theoretical relationship between our models and SVM (Refer to Appendix C). Selecting different p-norm in objective function, our model can be converted to a standard Support Vector Machine classification model. We validated the proposed model using four credit risk datasets and compared with four well-known classification tools in terms of accuracy, type I and II errors, KS score, and correlation coefficient. The results indicate that the MCQP model has the most excellent performance in two datasets and competitive results in the other two datasets.

Furthermore, we conducted two experimental studies using computer generated large-scale data (size of $O ( 1 0 ^ { 9 } )$ ). The experimental studies were summarized in Appendix B and the results indicate that the epsilon-support vector approach is capable of solving very large-scale data mining problems and have good performance even when the dataset is highly noised (Refer to Appendix B: Tables 1 and 2). The efficiency of the proposed MCQP model was also validated in this synthetic large-scale classification problem: the average computing time for 100 million records with 20 variables is 711.3 s (Refer to Appendix B: Tables 1 and 2).

To summarize, this paper proposed and applied mathematical programming model to classification problems to address two aspects of data mining algorithm: speed and scalability. The proposed models achieved better or comparable classification accuracies to other classification models such as SVM and decision tree. They are highly efficient (computing time complexity $O ( n ^ { 1 . 5 - 2 } ) )$ and scalable to massive problems (size of $O ( 1 0 ^ { 9 } ) )$ ).

There are many unsolved questions and answers to these questions will further improve the performance of the mathematic model proposed. For example, in this study Gauss kernel was arbitrarily chosen. One direction is to build a theoretical guideline that helps the selection of appropriate kernel function and therefore optimizes the credit analysis result. Another direction is to apply the proposed MCQP in various real-life data mining problems, such as AIDS research [53] and the interaction of anti-body and anti-gene. The results of these ongoing researches will be reported in the near future.

## Acknowledgments

This research has been partially supported by grants from National Natural Science Foundation of China (#70621001, #70531040, #70472074), 973 Project #2004CB720103, Ministry of Science and Technology, China, and BHP Billiton Co., Australia. Part of the work is done while Gang Kou and Yi Peng are visiting students in Data Mining Research Group, Univ. of Illinois at Urbana-Champaign. The authors would like to thank Prof. Yinjie Tian, Prof. Yongyi Chen and the anomalous reviewers for their valuable comments.

## Appendix A. Classification results of 4 credit datasets

Appendix A1  
10-fold cross-validation result of German set

<table><tr><td rowspan="2"></td><td colspan="3">Classification accuracy</td><td colspan="2">Error rate</td><td rowspan="2">KS score</td><td rowspan="2">Corr coef</td></tr><tr><td>Overall</td><td>Normal</td><td>Bad</td><td>Type I</td><td>Type II</td></tr><tr><td colspan="8">Linear Discriminant Analysis</td></tr><tr><td>Training</td><td>73.80%</td><td>73.43%</td><td>74.67%</td><td>25.65%</td><td>26.25%</td><td>48.10</td><td>0.481</td></tr><tr><td>Test</td><td>72.20%</td><td>72.57%</td><td>71.33%</td><td>28.32%</td><td>27.77%</td><td>43.90</td><td>0.439</td></tr><tr><td colspan="8">See5</td></tr><tr><td>Training</td><td>89.10%</td><td>95.57%</td><td>74.00%</td><td>21.39%</td><td>5.65%</td><td>69.57</td><td>0.712</td></tr><tr><td>Test</td><td>72.20%</td><td>84.00%</td><td>44.67%</td><td>39.71%</td><td>26.37%</td><td>28.67</td><td>0.312</td></tr><tr><td colspan="8">SVMlight</td></tr><tr><td>Training</td><td>68.65%</td><td>79.00%</td><td>44.50%</td><td>41.26%</td><td>32.06%</td><td>23.50</td><td>0.250</td></tr><tr><td>Test</td><td>66.50%</td><td>77.00%</td><td>42.00%</td><td>42.96%</td><td>35.38%</td><td>19.00</td><td>0.203</td></tr><tr><td colspan="8">libSVM</td></tr><tr><td>Training</td><td>93.25%</td><td>100.00%</td><td>77.50%</td><td>18.37%</td><td>0.00%</td><td>77.50</td><td>0.795</td></tr><tr><td>Test</td><td>94.00%</td><td>100.00%</td><td>80.00%</td><td>16.67%</td><td>0.00%</td><td>80.00</td><td>0.816</td></tr><tr><td colspan="8">MCQP</td></tr><tr><td>Training</td><td>73.86%</td><td>74.91%</td><td>71.42%</td><td>27.62%</td><td>26.00%</td><td>46.33</td><td>0.464</td></tr><tr><td>Test</td><td>73.50%</td><td>74.38%</td><td>72.00%</td><td>27.35%</td><td>26.24%</td><td>46.38</td><td>0.464</td></tr></table>

## Appendix A2

10-fold cross-validation result of Australian set

<table><tr><td rowspan="2"></td><td colspan="3">Classification accuracy</td><td colspan="2">Error rate</td><td rowspan="2">KS score</td><td rowspan="2">Corr coef</td></tr><tr><td>Overall</td><td>Normal</td><td>Bad</td><td>Type I</td><td>Type II</td></tr><tr><td colspan="8">Linear Discriminant Analysis</td></tr><tr><td>Training</td><td>86.09%</td><td>80.94%</td><td>92.51%</td><td>8.47%</td><td>17.08%</td><td>73.45</td><td>0.739</td></tr><tr><td>Test</td><td>85.80%</td><td>80.68%</td><td>92.18%</td><td>8.83%</td><td>17.33%</td><td>72.86</td><td>0.733</td></tr><tr><td colspan="8">See5</td></tr><tr><td>Training</td><td>90.29%</td><td>91.64%</td><td>88.60%</td><td>11.06%</td><td>8.62%</td><td>80.24</td><td>0.803</td></tr><tr><td>Test</td><td>86.52%</td><td>87.99%</td><td>84.69%</td><td>14.82%</td><td>12.42%</td><td>72.68</td><td>0.727</td></tr><tr><td colspan="8">SVMlight</td></tr><tr><td>Training</td><td>55.22%</td><td>23.76%</td><td>94.46%</td><td>18.90%</td><td>44.66%</td><td>18.22</td><td>0.258</td></tr><tr><td>Test</td><td>44.83%</td><td>18.03%</td><td>90.65%</td><td>34.14%</td><td>47.48%</td><td>8.69</td><td>0.126</td></tr><tr><td colspan="8">libSVM</td></tr><tr><td>Training</td><td>99.71%</td><td>100.00%</td><td>99.35%</td><td>0.65%</td><td>0.00%</td><td>99.35</td><td>0.994</td></tr><tr><td>Test</td><td>44.83%</td><td>86.89%</td><td>27.10%</td><td>45.62%</td><td>32.61%</td><td>13.99</td><td>0.174</td></tr><tr><td colspan="8">MCQP</td></tr><tr><td>Training</td><td>87.25%</td><td>88.50%</td><td>86.38%</td><td>13.34%</td><td>11.75%</td><td>74.88</td><td>0.749</td></tr><tr><td>Test</td><td>86.38%</td><td>87.00%</td><td>85.52%</td><td>14.27%</td><td>13.20%</td><td>72.52</td><td>0.725</td></tr></table>

Appendix A3  
10-fold cross-validation result of Japanese set

<table><tr><td rowspan="2"></td><td colspan="3">Classification accuracy</td><td colspan="2">Error rate</td><td rowspan="2">KS score</td><td rowspan="2">Corr coef</td></tr><tr><td>Overall</td><td>Normal</td><td>Bad</td><td>Type I</td><td>Type II</td></tr><tr><td colspan="8">Linear Discriminant Analysis</td></tr><tr><td>Training</td><td>73.65%</td><td>72.07%</td><td>78.38%</td><td>23.08%</td><td>26.27%</td><td>50.45</td><td>0.506</td></tr><tr><td>Test</td><td>68.92%</td><td>68.47%</td><td>70.27%</td><td>30.28%</td><td>30.97%</td><td>38.74</td><td>0.387</td></tr><tr><td colspan="8">See5</td></tr><tr><td>Training</td><td>93.24%</td><td>96.40%</td><td>83.78%</td><td>14.40%</td><td>4.12%</td><td>80.18</td><td>0.808</td></tr><tr><td>Test</td><td>72.30%</td><td>84.68%</td><td>35.14%</td><td>43.37%</td><td>30.36%</td><td>19.82</td><td>0.228</td></tr><tr><td colspan="8">SVMlight</td></tr><tr><td>Training</td><td>100.00%</td><td>100.00%</td><td>100.00%</td><td>0.00%</td><td>0.00%</td><td>100.00</td><td>1.000</td></tr><tr><td>Test</td><td>48.15%</td><td>47.25%</td><td>52.94%</td><td>49.90%</td><td>49.91%</td><td>0.19</td><td>0.002</td></tr><tr><td colspan="8">libSVM</td></tr><tr><td>Training</td><td>100.00%</td><td>100.00%</td><td>100.00%</td><td>0.00%</td><td>0.00%</td><td>100.00</td><td>1.000</td></tr><tr><td>Test</td><td>50.46%</td><td>49.45%</td><td>55.88%</td><td>47.15%</td><td>47.49%</td><td>5.33</td><td>0.053</td></tr><tr><td colspan="8">MCQP</td></tr><tr><td>Training</td><td>73.65%</td><td>72.38%</td><td>77.98%</td><td>23.33%</td><td>26.16%</td><td>50.36</td><td>0.504</td></tr><tr><td>Test</td><td>72.30%</td><td>72.30%</td><td>72.47%</td><td>27.58%</td><td>27.65%</td><td>44.77</td><td>0.448</td></tr></table>

Appendix A4  
10-fold cross-validation result of the US set

<table><tr><td rowspan="2"></td><td colspan="3">Classification accuracy</td><td colspan="2">Error rate</td><td rowspan="2">KS score</td><td rowspan="2">Corr coef</td></tr><tr><td>Overall</td><td>Normal</td><td>Bad</td><td>Type I</td><td>Type II</td></tr><tr><td colspan="8">Linear Discriminant Analysis</td></tr><tr><td>Training</td><td>80.29%</td><td>75.43%</td><td>85.14%</td><td>16.46%</td><td>22.40%</td><td>60.57</td><td>0.609</td></tr><tr><td>Test</td><td>78.79%</td><td>74.00%</td><td>83.57%</td><td>18.17%</td><td>23.73%</td><td>57.57</td><td>0.578</td></tr><tr><td colspan="8">See5</td></tr><tr><td>Training</td><td>85.21%</td><td>78.00%</td><td>92.43%</td><td>8.85%</td><td>19.23%</td><td>70.43</td><td>0.712</td></tr><tr><td>Test</td><td>75.00%</td><td>72.14%</td><td>83.57%</td><td>18.55%</td><td>25.00%</td><td>55.71</td><td>0.561</td></tr><tr><td colspan="8">SVMlight</td></tr><tr><td>Training</td><td>75.57%</td><td>66.29%</td><td>84.86%</td><td>18.60%</td><td>28.43%</td><td>51.14</td><td>0.520</td></tr><tr><td>Test</td><td>74.00%</td><td>65.14%</td><td>82.86%</td><td>20.83%</td><td>29.61%</td><td>48.00</td><td>0.488</td></tr><tr><td colspan="8">libSVM</td></tr><tr><td>Training</td><td>79.93%</td><td>72.71%</td><td>87.14%</td><td>15.03%</td><td>23.85%</td><td>59.86</td><td>0.605</td></tr><tr><td>Test</td><td>77.57%</td><td>70.43%</td><td>84.71%</td><td>17.83%</td><td>25.88%</td><td>55.14</td><td>0.557</td></tr><tr><td colspan="8">MCQP</td></tr><tr><td>Training</td><td>78.84%</td><td>72.38%</td><td>85.36%</td><td>16.82%</td><td>24.45%</td><td>57.74</td><td>0.582</td></tr><tr><td>Test</td><td>78.50%</td><td>71.92%</td><td>85.22%</td><td>17.05%</td><td>24.78%</td><td>57.14</td><td>0.577</td></tr></table>

Appendix A5  
10-fold cross-validation results of US set by MCQP

<table><tr><td rowspan="2"></td><td colspan="3">Classification accuracy</td><td colspan="2">Error rate</td><td rowspan="2">KS score</td><td rowspan="2">Corr coef</td></tr><tr><td>Overall</td><td>Normal</td><td>Bad</td><td>Type I</td><td>Type II</td></tr><tr><td colspan="8">Training set</td></tr><tr><td>Fold 1</td><td>79.52%</td><td>73.68%</td><td>85.31%</td><td>16.62%</td><td>23.58%</td><td>58.99</td><td>0.594</td></tr><tr><td>Fold 2</td><td>78.65%</td><td>71.84%</td><td>85.35%</td><td>16.94%</td><td>24.81%</td><td>57.19</td><td>0.577</td></tr><tr><td>Fold 3</td><td>78.65%</td><td>72.18%</td><td>85.10%</td><td>17.11%</td><td>24.64%</td><td>57.28</td><td>0.578</td></tr><tr><td>Fold 4</td><td>78.73%</td><td>72.85%</td><td>84.81%</td><td>17.25%</td><td>24.25%</td><td>57.66</td><td>0.581</td></tr><tr><td>Fold 5</td><td>78.89%</td><td>72.42%</td><td>85.37%</td><td>16.81%</td><td>24.42%</td><td>57.79</td><td>0.583</td></tr><tr><td>Fold 6</td><td>78.89%</td><td>71.82%</td><td>85.92%</td><td>16.39%</td><td>24.70%</td><td>57.74</td><td>0.583</td></tr><tr><td>Fold 7</td><td>78.37%</td><td>72.61%</td><td>85.02%</td><td>17.10%</td><td>24.37%</td><td>57.63</td><td>0.581</td></tr><tr><td>Fold 8</td><td>79.05%</td><td>72.24%</td><td>85.94%</td><td>16.29%</td><td>24.42%</td><td>58.18</td><td>0.587</td></tr><tr><td>Fold 9</td><td>78.57%</td><td>71.38%</td><td>85.58%</td><td>16.81%</td><td>25.06%</td><td>56.96</td><td>0.575</td></tr><tr><td>Fold 10</td><td>79.05%</td><td>72.76%</td><td>85.22%</td><td>16.88%</td><td>24.22%</td><td>57.98</td><td>0.584</td></tr><tr><td>Average</td><td>78.84%</td><td>72.38%</td><td>85.36%</td><td>16.82%</td><td>24.45%</td><td>57.74</td><td>0.582</td></tr><tr><td colspan="8">Testing set</td></tr><tr><td>Fold 1</td><td>77.86%</td><td>68.49%</td><td>88.06%</td><td>14.85%</td><td>26.35%</td><td>56.55</td><td>0.577</td></tr><tr><td>Fold 2</td><td>80.00%</td><td>72.00%</td><td>89.23%</td><td>13.01%</td><td>23.88%</td><td>61.23</td><td>0.622</td></tr><tr><td>Fold 3</td><td>80.00%</td><td>76.06%</td><td>84.06%</td><td>17.33%</td><td>22.17%</td><td>60.12</td><td>0.603</td></tr><tr><td>Fold 4</td><td>77.14%</td><td>69.49%</td><td>82.72%</td><td>19.91%</td><td>26.95%</td><td>52.21</td><td>0.527</td></tr><tr><td>Fold 5</td><td>78.57%</td><td>71.01%</td><td>85.92%</td><td>16.55%</td><td>25.23%</td><td>56.93</td><td>0.576</td></tr><tr><td>Fold 6</td><td>75.00%</td><td>70.83%</td><td>79.41%</td><td>22.52%</td><td>26.86%</td><td>50.24</td><td>0.504</td></tr><tr><td>Fold 7</td><td>82.14%</td><td>77.05%</td><td>86.08%</td><td>15.30%</td><td>21.05%</td><td>63.13</td><td>0.634</td></tr><tr><td>Fold 8</td><td>78.57%</td><td>72.73%</td><td>83.78%</td><td>18.23%</td><td>24.56%</td><td>56.51</td><td>0.569</td></tr><tr><td>Fold 9</td><td>77.86%</td><td>71.79%</td><td>85.48%</td><td>16.82%</td><td>24.81%</td><td>57.27</td><td>0.578</td></tr><tr><td>Fold 10</td><td>77.86%</td><td>69.74%</td><td>87.50%</td><td>15.20%</td><td>25.70%</td><td>57.24</td><td>0.582</td></tr><tr><td>Average</td><td>78.50%</td><td>71.92%</td><td>85.22%</td><td>17.04%</td><td>24.78%</td><td>57.14</td><td>0.577</td></tr></table>

## Appendix B. Epsilon-support vector and large-scale data mining problem

In this section, we test the applicability of our algorithm in large-scale data mining problem $( > O ( 1 0 ^ { 9 } ) )$ , which is too large to be loaded into a typical PC memory (512MB-4Gb) but can be saved in hard disk (40Gb-1Tb). Because it is hard to find any real life data in such size, we use a Normally Distributed Clustered program (NDC) [30] to generate datasets. Normally distributed cluster is a data generator. NDC generates data points clustered to a series of random centers and all points are multivariate normal distributed. All variables are integers for simplicity. Then, NDC randomly generates a separating plane and assigns a class for each random center according to the random separating plane. NDC changes dataset separability by changing the variances of the distributions. The percentage of separability is calculated by counting how many points end up on the right and wrong side of the separating plane. NDC will provide the percentage of linear separability.

The experimental study has two parts. The first one is to test the capability of the proposed algorithm in massive problem with low noises. The second test is to evaluate the performance of the proposed algorithm for high noise, large dataset.

## Massive dataset

The first experiment dataset consists of 100 million records and each record has 20 variables. It is balanced with 50% of the data in the first group and 50% of the data in the second group. The dataset is 95% “linear separable” [30]. As we mentioned in the introduction, the proposed model is efficient because it only needs to solve linear equations to find the global optimal solution. To prove our argument, we summarized the computing time of the large dataset in Table 1. The average training time of 10-fold cross-validation for the 100 million records with 20 variables is only 711.3 s, which confirms that the MCQP model is highly efficient for massive datasets.

## Appendix B1

massive dataset computing results

<table><tr><td rowspan="2">10-fold</td><td colspan="2">Training</td><td rowspan="2">Time (s)</td><td colspan="2">Testing</td></tr><tr><td>Class 1</td><td>Class 2</td><td>Class 1</td><td>Class 2</td></tr><tr><td>Fold 1</td><td>94.93%</td><td>94.87%</td><td>631</td><td>94.91%</td><td>94.82%</td></tr><tr><td>Fold 2</td><td>94.96%</td><td>94.82%</td><td>933</td><td>94.93%</td><td>94.82%</td></tr><tr><td>Fold 3</td><td>94.85%</td><td>94.93%</td><td>378</td><td>94.87%</td><td>94.91%</td></tr><tr><td>Fold 4</td><td>94.88%</td><td>94.89%</td><td>785</td><td>94.87%</td><td>94.90%</td></tr><tr><td>Fold 5</td><td>94.84%</td><td>94.95%</td><td>655</td><td>94.82%</td><td>94.93%</td></tr><tr><td>Fold 6</td><td>94.95%</td><td>94.93%</td><td>1217</td><td>94.89%</td><td>94.91%</td></tr><tr><td>Fold 7</td><td>94.93%</td><td>94.93%</td><td>467</td><td>94.91%</td><td>94.86%</td></tr><tr><td>Fold 8</td><td>94.98%</td><td>94.85%</td><td>632</td><td>94.92%</td><td>94.84%</td></tr><tr><td>Fold 9</td><td>94.87%</td><td>94.94%</td><td>876</td><td>94.85%</td><td>94.83%</td></tr><tr><td>Fold 10</td><td>94.83%</td><td>94.88%</td><td>539</td><td>94.84%</td><td>94.86%</td></tr><tr><td>Average</td><td>94.90%</td><td>94.90%</td><td>711.3</td><td>94.88%</td><td>94.87%</td></tr></table>

## Large dataset with high noise

The dataset consists of 2 million records and each record has 10 variables. It is balanced with 50% of the data in the first group and 50% of the data in the second group. The dataset is 75% linear separable and the average computing time is 1466.1 s.

## Appendix B2

High noise dataset computing results

<table><tr><td rowspan="2">10-fold</td><td colspan="2">Training</td><td rowspan="2">Time (s)</td><td colspan="2">Testing</td></tr><tr><td>Class 1</td><td>Class 2</td><td>Class 1</td><td>Class 2</td></tr><tr><td>Fold 1</td><td>71.34%</td><td>74.33%</td><td>1279</td><td>70.25%</td><td>71.12%</td></tr><tr><td>Fold 2</td><td>72.77%</td><td>74.13%</td><td>849</td><td>72.85%</td><td>72.47%</td></tr><tr><td>Fold 3</td><td>74.79%</td><td>72.44%</td><td>1537</td><td>72.31%</td><td>71.23%</td></tr><tr><td>Fold 4</td><td>70.94%</td><td>73.58%</td><td>2574</td><td>70.32%</td><td>72.09%</td></tr><tr><td>Fold 5</td><td>74.11%</td><td>72.35%</td><td>742</td><td>72.57%</td><td>71.32%</td></tr><tr><td>Fold 6</td><td>73.56%</td><td>74.33%</td><td>1380</td><td>73.24%</td><td>72.67%</td></tr><tr><td>Fold 7</td><td>71.90%</td><td>70.38%</td><td>3546</td><td>70.39%</td><td>70.12%</td></tr><tr><td>Fold 8</td><td>73.89%</td><td>72.48%</td><td>836</td><td>72.37%</td><td>72.23%</td></tr><tr><td>Fold 9</td><td>72.37%</td><td>73.38%</td><td>711</td><td>71.56%</td><td>71.73%</td></tr><tr><td>Fold 10</td><td>73.56%</td><td>72.84%</td><td>1207</td><td>72.40%</td><td>72.19%</td></tr><tr><td>Average</td><td>72.92%</td><td>73.02%</td><td>1466.1</td><td>71.83%</td><td>71.72%</td></tr></table>

The experimental results indicate that the new approach is capable in solving large-scale data mining problems $( > O ( 1 0 ^ { 9 } ) )$ and has good performance when the dataset is highly noised (noises are larger than 25% of the whole data).

## Appendix C. A Comparison of our model with SVM

Let $s { = } 2 , q { = } 1$ and $p { = } 1$ in Model 1 in Section 2. The constraints remain the same and Model 1's objective function becomes: comes:

(SVM Model 1) Minimize ${ \frac { 1 } { 2 } } \left| \left| X \right| \right| _ { 2 } ^ { 2 } + W _ { \alpha } \sum _ { i = 1 } ^ { n } \ \alpha _ { i } - W _ { \beta } \sum _ { i = 1 } ^ { n } \ \beta _ { i }$

The Lagrange function $L ( X , b , \alpha , \beta , \xi , \psi , \zeta )$ corresponding to SVM Model 1 is

$$
\frac {1}{2} | | X | | _ {2} ^ {2} + W _ {\alpha} \sum_ {i = 1} ^ {n} \alpha_ {i} - W _ {\beta} \sum_ {i = 1} ^ {n} \beta_ {i} - \sum_ {i = 1} ^ {n} \xi_ {i} (y _ {i} (<   A \cdot X > - b) - \delta^ {\prime} + \alpha_ {i} - \beta_ {i}) - \sum_ {i = 1} ^ {n} \psi_ {i} \alpha_ {i} - \sum_ {i = 1} ^ {n} \zeta_ {i} \beta_ {i}
$$

where $\xi _ { i } , \psi _ { i } , \zeta _ { i } \in \Re , \psi _ { i } \geq 0 , \zeta _ { i } \geq 0$

Based on Wolfe Dual Theorem, $\begin{array} { r } { \nabla _ { X } L ( X , b , \alpha , \beta , \xi , \psi , \zeta ) = 0 , \nabla _ { b } L ( X , b , \alpha , \beta , \xi , \psi , \zeta ) = 0 , \nabla _ { \alpha } L ( X , b , \alpha , \beta , \xi , \psi , \zeta ) = 0 , \nabla _ { \beta } L ( X , b , \alpha , \beta , \psi , \zeta ) = 0 , } \end{array}$ $\beta , \xi , \psi , \zeta ) = 0$ . We can get:

$$
X = \sum_ {i = 1} ^ {n} \xi_ {i} y _ {i} A _ {i}, \sum_ {i = 1} ^ {n} \xi_ {i} y _ {i} = 0, W _ {\alpha} = \xi_ {i} + \psi_ {i}, W _ {\beta} = \xi_ {i} - \zeta_ {i}.\tag{7}
$$

Introduce (7) to the Lagrange function, the equivalent Wolfe Dual problem of SVM Model 1 is expressed as: (SVM Model 2) Maximize $- \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \ \xi _ { i } y _ { i } \xi _ { j } y _ { j } \big ( { \cal A } _ { i } \cdot { \cal A } _ { j } \big ) + \delta ^ { \prime } \sum _ { i = 1 } ^ { n } \ \xi _ { i }$ Subject to:

$$
\sum_ {i = 1} ^ {n} \xi_ {i} y _ {i} = 0,
$$

$$
W _ {\beta} \leq \xi_ {i} \leq W _ {\alpha}
$$

where $W _ { \beta } { < } W _ { \alpha }$ are given, $1 \leq i \leq n$

The global optimal solution of the primal problem SVM Model 1 can be obtained from the solution of the Wolfe Dual problem:

$$
X ^ {*} = \sum_ {i = 1} ^ {n} \xi_ {i} ^ {*} y _ {i} A _ {i}, b ^ {*} = y _ {j} - \sum_ {i = 1} ^ {n} \xi_ {i} ^ {*} y _ {i} (A _ {i} \cdot A _ {j}), \forall \xi_ {i} ^ {*} \in (W _ {\alpha}, W _ {\beta}).
$$

The classification decision function becomes sgn ${ \big ( } \left( X ^ { * } \cdot A _ { i } \right) - b ^ { * } { \big ) } { \left\{ \begin{array} { l l } { > 0 , \Rightarrow A _ { i } \in G _ { 1 } } \\ { \leq 0 , \Rightarrow A _ { i } \in G _ { 2 } } \end{array} \right. }$

A classification problem can be solved by SVM algorithm 1 using SVM model 2.

## SVM Algorithm 1

Input: A $n \times r$ matrix A as the training dataset, a n × diagonal matrix Y labels the class of each record.

Output: classification accuracies for each group in the training dataset, score for every record, decision function $\operatorname { s g n } \big ( \big ( \boldsymbol { X } ^ { * } \cdot \boldsymbol { A } _ { i } \big ) - \boldsymbol { b } ^ { * } \big ) \biggl \{ \begin{array} { l } { > 0 , \Rightarrow A _ { i } \in G _ { 1 } } \\ { \leq 0 , \Rightarrow A _ { i } \in G _ { 2 } } \end{array} $

Step 1: Construct quadratic programming problem as SVsM model 2 and find the optimal solution $\xi _ { i } ^ { * } , W _ { \beta } , W _ { \alpha }$ are chosen by cross-validation.

Step 2: Compute $\boldsymbol { X } ^ { * } = \sum _ { i = 1 } ^ { n } \ \boldsymbol { \xi } _ { i } ^ { * } \boldsymbol { y } _ { i } \boldsymbol { A } _ { i } , \boldsymbol { b } ^ { * } = \boldsymbol { y } _ { j } - \sum _ { i = 1 } ^ { n } \ \boldsymbol { \xi } _ { i } ^ { * } \boldsymbol { y } _ { i } \big ( \boldsymbol { A } _ { i } \boldsymbol { \cdot } \boldsymbol { A } _ { j } \big ) , \forall \boldsymbol { \xi } _ { i } ^ { * } \in \big ( \boldsymbol { W } _ { \alpha } , \boldsymbol { W } _ { \beta } \big ) .$

<sup>¼</sup>Step 3: Classify an incoming $A _ { i }$ <sup>¼</sup>by using decision function sgn $\left( \left( \boldsymbol { X } ^ { * } \cdot \boldsymbol { A } _ { i } \right) - \boldsymbol { b } ^ { * } \right) \left\{ \begin{array} { l l } { > 0 , \Rightarrow A _ { i } \in { \boldsymbol { G } } _ { 1 } } \\ { \leq 0 , \Rightarrow A _ { i } \in { \boldsymbol { G } } _ { 2 } } \end{array} \right.$

END

For nonlinear problems, $( A _ { i } , A _ { j } )$ in SVM Model 2 is inner product in the vector space and it can be substituted by a kernel K $( A _ { i } , A _ { j } )$ . Thus SVM Model 2 is easily transformed to a nonlinear model by replacing $( A _ { i } , A _ { j } )$ with any positive semidefinite kernel function $\operatorname { K } ( A _ { i } , A _ { j } )$

(SVM Model 2′) Maximize $- { \textstyle \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \ \xi _ { i } y _ { i } \xi _ { j } y _ { j } K { \big ( } A _ { i } \cdot A _ { j } { \big ) } + \delta ^ { \prime } \sum _ { i = 1 } ^ { n } \ \xi _ { i }$

Subject to:

$$
\sum_ {i = 1} ^ {n} \xi_ {i} y _ {i} = 0,
$$

$$
W _ {\beta} \leq \xi_ {i} \leq W _ {\alpha}
$$

where $W _ { \beta } { < } W _ { \alpha }$ are given, $1 \leq i \leq n$

The corresponding $\boldsymbol { X } ^ { * } , \boldsymbol { b } ^ { * }$ of SVM model $2 ^ { \prime }$ can be expressed as:

$$
X ^ {*} = \sum_ {i = 1} ^ {n} \xi_ {i} ^ {*} y _ {i} A _ {i}, b ^ {*} = y _ {j} - \sum_ {i = 1} ^ {n} \xi_ {i} ^ {*} y _ {i} K (A _ {i} \cdot A _ {j}), \forall \xi_ {i} ^ {*} \in (W _ {\alpha}, W _ {\beta}).
$$

A nonlinear classification problem can be solved by SVM algorithm 1′ using SVM model 2′.

SVM Algorithm $I ^ { \prime }$

Input: A $n \times r$ matrix A as the training dataset, a $n \times n$ diagonal matrix Y labels the class of each record, a kernel function $\operatorname { K } ( A _ { i } , A _ { j } )$

Output: classification accuracies for each group in the training dataset, score for every record, decision function.

Step 1: Construct quadratic programming problem as SVM model $2 ^ { \prime }$ and find the optimal solution $\xi _ { i } ^ { * } , W _ { \beta } , W _ { \alpha }$ are chosen by cross-validation.

Step 2: Compute $\boldsymbol { b } ^ { * } = y _ { j } - \sum _ { i = 1 } ^ { n } \ \boldsymbol { \xi } _ { i } ^ { * } y _ { i } K \big ( \boldsymbol { A } _ { i } \cdot \boldsymbol { A } _ { j } \big ) , \forall \boldsymbol { \xi } _ { i } ^ { * } \in \big ( W _ { \alpha } , W _ { \beta } \big ) .$

<sup>¼</sup>Step 3: Classify an incoming $A _ { j }$ using decision function sgn $\left( \sum _ { i = 1 } ^ { n } \ \xi _ { i } ^ { * } y _ { i } K \big ( A _ { j } \cdot A _ { i } \big ) - b ^ { * } \right) \left\{ \begin{array} { l l } { > 0 , \Rightarrow A _ { j } \in G _ { 1 } } \\ { \leq 0 , \Rightarrow A _ { j } \in G _ { 2 } } \end{array} \right.$

END

In this section, we demonstrated how Model 1 in Section 2 can be transformed to a standard SVM model. There are two differences between our model and other existing Support Vectors approaches: (1) our model is formulated by multiple criteria and different p-norm can be chosen to set up different models; (2) the introduction of $\beta _ { i }$ is one of the major differences between the proposed model and Support Vectors approaches.

## References

[1] B.E. Boser, I. Guyon, V.N. Vapnik, A training algorithm for optimal margin classifiers, Proceedings of the Fifth Annual Workshop on Computational Learning Theory, Pittsburgh, PA, USA, 1992, pp. 144–152.

[2] P.S. Bradley, U.M. Fayyad, O.L. Mangasarian, Mathematical programming for data mining: formulations and challenges, INFORMS Journal on Computing 11 (3) (1999) 217–238.

[3] C.J.C. Burges, A tutorial on support vector machines for pattern recognition, Knowledge Discovery and Data Mining 2 (2) (1998) 121–167.

[4] R. Caruana, A. Niculescu-Mizil, Data mining in metric space: an empirical analysis of supervised learning performance criteria, Proceedings of the Tenth International Conference on Knowledge Discovery and Data Mining (KDD'04), Seattle, Washington, USA, 2004, pp. 69–78.

[5] C.C. Chang, C.J. Lin, LIBSVM: a library for support vector machines, 2001, Software available at http://www.csie.ntu.edu. tw/\~cjlin/libsvm.

[6] N. Cristianini, J. Shawe-Taylor, An Introduction to Support Vector Machines, Cambridge University Press, Cambridge, UK, 2000.

[7] U.M. Fayyad, G. Piatetsky-Shapiro, P. Smith, From data mining to knowledge discovery: an overview, Advance in Knowledge Discovery and Data Mining, AAAI Press/The MIT Press, Cambridge, 1996.

[8] N. Freed, F. Glover, Simple but powerful goal programming models for discriminant problems, European Journal of Operational Research 7 (1981) 44–60.

[9] G. Fung, Machine learning and data mining via mathematical programming-based support vector machines, Ph.D thesis, The University of Wisconsin - Madison, 2003.

[10] G. Fung, O.L. Mangasarian, Data selection for support vector machine classification, in: R. Ramakrishnan, S. Stolfo (Eds.),

Proceedings KDD2000: Knowledge Discovery and Data Mining, Boston, MA, USA, 2000, pp. 64–70.

[11] G. Fung, O.L. Mangasarian, Multicategory proximal support vector machine classifiers, Machine Learning 59 (2005) 77–97.

[12] G. Fung, O.L. Mangasarian, A.J. Smola, Minimal kernel classifiers, Journal of Machine Learning Research 3 (2002) 303–321.

[13] G.H. Golub, C.F. Loan, Matrix Computations, Johns Hopkins University Press, Baltimore MD, 1989.

[14] D.J. Hand, Discrimination and Classification, Wiley, Chichester, 1981.

[15] T. Joachims, Making large-scale SVM learning practical, in: B. Schöl lkopf, C. Burges, A. Smola (Eds.), Advances in Kernel Methods— Support Vector Learning, MIT-Press, Cambridge, Massachusetts, USA, 1999.

[16] T. Joachims, Learning to classify text using support vector machines: methods, theory, and algorithms, Kluwer Academic Publishers, Netherlands, 2002.

[17] T. Joachims, SVM-light: Support Vector Machine, 2004, available at: http://svmlight.joachims.org/.

[18] P. Kolesar, J.L. Showers, A robust credit screening model using categorical data, Management Science 31 (2) (1985) 123–133.

[19] G. Kou, Y. Peng, Y. Shi, Z. Chen, A new multi-criteria convex quadratic programming model for credit analysis, in: V.N. Alexandrov, et al., (Eds.), ICCS 2006, LNCS 3994, Springer-Verlag, Berlin, 2006, pp. 476–484.

[20] G. Kou, Y. Peng, Y. Shi, M. Wise, W. Xu, Discovering credit cardholders' behavior by multiple criteria linear programming, Annals of Operations Research 135 (1) (2005) 261–274.

[21] W. Kwak, Y. Shi, S. Eldridge, G. Kou, Bankruptcy prediction for Japanese firms: using multiple criteria linear programming data mining approach, International Journal of Business Intelligence and Data Mining 1 (4) (2006) 401–416.

[22] O.L. Mangasarian, Generalized support vector machines, in: A.J. Smola, P. Bartlett, B. Schökopf, D. Schuurmans (Eds.), Advances in Large Margin Classifiers, MIT Press, 2000, pp. 135–146.

[23] O.L. Mangasarian, Generalized support vector machines, in: A. Smola, P. Bartlett, B. Scholkopf, D. Schuurmans (Eds.), Advances in Large Margin Classifiers, MIT Press, Cambridge, MA, 2000, pp. 135–146.

[24] O.L. Mangasarian, Support vector machine classification via parameterless robust linear programming, Optimization Methods and Software 20 (2005) 115–125.

[25] O.L. Mangasarian, Linear and nonlinear separation of patterns by linear programming, Operations Research 13 (1965) 444–452.

[26] O.L. Mangasarian, Multi-surface method of pattern separation, IEEE Transactions on Information Theory 14 (1968) 801–807.

[27] O.L. Mangasarian, D.R. Musicant, Successive overrelaxation for support vector machines, IEEE Transactions on Neural Networks 10 (1999) 1032–1037.

[28] O.L. Mangasarian, J.W. Shavlik, E.W. Wild, Knowledge-based kernel approximation, Journal of Machine Learning Research 5 (2004) 1127–1141.

[29] P.M. Murphy, D.W. Aha, UCI repository of machine learning databases, 1992, www.ics.uci.edu/\_mlearn/MLRepository.html.

[30] D.R. Musicant, NDC: normally distributed clustered datasets, 1998, www.cs.wisc.edu/\_musicant/data/ndc/.

[31] D.L. Olson, Y. Shi, Introduction to Business Data Mining, McGraw-Hill/Irwin, 2005.

[32] Y. Peng, G. Kou, Z. Chen, Y. Shi, Cross-validation and ensemble analyses on multiple-criteria linear programming classification for credit cardholder behavior, in: M. Bubak, et al., (Eds.), ICCS 2004, LNCS 3039, Springer-Verlag, Berlin, 2004, pp. 931–939.

[33] Y. Peng, G. Kou, Y. Shi, Z. Chen, Improving clustering analysis for credit card accounts classification, in: V.S. Sunderam, et al., (Eds.), ICCS 2005, LNCS 3516, Springer-Verlag, Berlin, 2005, pp. 548–553.

[34] J. Quinlan, Induction of decision trees, Machine Learning 1 (1986) 81–106.

[35] J. Quinlan, See5.0., 2004, available at:http://www.rulequest.com see5-info.html.

[36] E. Rosenberg, A. Gleit, Quantitative methods in credit management: a survey, Operations Research 42 (1994) 589–613.

[37] B. Schölkopf, A.J. Smola, Learning with Kernels, MIT Press, 2002.

[38] B. Schölkopf, C. Burges, A. Smola (Eds.), Advances in Kernel Methods— Support Vector Learning, MIT Press, Cambridge, MA, 1999.

[39] B. Schölkopf, C. Burges, V. Vapnik, Incorporating invariances in support vector learning machines, in: C. von der Malsburg, W. von Seelen, J.C. Vorbrüggen, B. Schölkopf (Eds.), Artificial Neural Networks— ICANN'96, Springer Lecture Notes in Computer Science, vol. 1112, 1996, pp. 47–52.

[40] B. Schölkopf, S. Mika, C.J.C. Burges, P. Knirsch, K.-R. Müller, G. Rätsch, A. Smola, Input space vs. feature space in kernelbased methods, IEEE Transactions on Neural Networks 10 (5) (1999) 1000–1017.

[41] Y. Shi, Multi-Criteria and Multi-Constraints linear programming, World Scientific Publish Co., 2001.

[42] Y. Shi, Y. Peng, G. Kou, Z. Chen, Classifying credit card accounts for business intelligence and decision making: a multiplecriteria quadratic programming approach, International Journal of Information Technology and Decision Making 4 (4) (2005) 1–19.

[43] J.L. Showers, L.M. Chakrin, Reducing uncollectable revenue from residential telephone customers, Interfaces 11 (1981) 21–31.

[44] SPSS Incorporation, SPSS for Windows, release 11.0.1 (15 Nov, 2001). Homepage: http://www.spss.com/.

[45] V.G. Tony, B. Bart, P. Van Dijcke, J. Garcia, J. Suykens, J. Vanthienen, A process model to develop an internal rating system: sovereign credit ratings, Decision Support Systems 42 (2) (2006) 1131–1151.

[46] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer, New York, USA, 1995.

[47] V.N. Vapnik, The Nature of Statistical Learning Theory, second edition. Springer, New York, 2000.

[48] V.N. Vapnik, Estimation of Dependences Based on Empirical Data [in Russian], Nauka, Moscow, 1979 (English translation: Springer Verlag, New York, 1982).

[49] V.N. Vapnik, O. Chapelle, Bounds on error expectation for support vector machines, Neural Computation 12 (9) (2000) 2013–2036.

[50] V. Vapnik, A. Chervonenkis, A note on one class of perceptrons, Automation and Remote Control 25 (1964) 821–837.

[51] V. Vapnik, A. Lerner, Pattern recognition using generalized portrait method, Automation and Remote Control 24 (1963) 774–780.

[52] P. Wolfe, A duality theorem for nonlinear programming, Quarterly of Applied Mathematics 19 (3) (1961) 239–244.

[53] J. Zheng, W. Zhuang, N. Yan, G. Kou, H. Peng, C. McNally, D. Erichsen, A. Cheloha, S. Herek, C. Shi, Y. Shi, Classification of HIV-1 mediated neuronal dendritic and synaptic damage using multiple criteria linear programming, Neuroinformatics 2 (3) (2004) 303–326.

[54] H. Zhao, A multi-objective genetic programming approach to developing Pareto optimal decision trees, Decision Support Systems 43 (3) (2007) 809–826.

Yi Peng is Associate Professor in the School of Management and Economy at University of Electronic Science and Technology of China. Her research interests include data mining foundations and theories, mathematical modeling, data mining techniques and applications.

Gang Kou is Research Scientist in R&D of the Thomson Corporation. His research interests include the development of theoretical concepts, algorithms and systems pertaining for Multi-Criteria Decision Making and applications of data mining techniques to real world data analysis problems.

Yong Shi is the director of Chinese Academy of Sciences Research Center on Fictitious Economy & Data Science. He is also Professor in the College of Information Science and Technology at the University of Nebraska at Omaha. Dr. Shi's research interests include multiple criteria decision making, data mining, information overload, and telecommunication management.

Zhengxin Chen is Professor in the College of Information Science and Technology at the University of Nebraska at Omaha. His primary research interests include various issues in AI, Database management systems, intelligent information retrieval, and data mining.
