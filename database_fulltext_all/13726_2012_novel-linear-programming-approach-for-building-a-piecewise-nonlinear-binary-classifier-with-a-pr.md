---
otero_id: 13726
otero_key: "2KHNHF6W"
title: "Novel linear programming approach for building a piecewise nonlinear binary classifier with a priori accuracy"
authors: "Ubaldo M. García-Palomares; Orestes Manzanilla-Salazar"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
We compare this algorithm with a new linear SVM that needs no pre tuning and has an excellent performance on standard and synthetic data. Highly encouraging numerical results are reported on synthetic examples, on the Japanese Bank dataset, and on medium and small datasets from the Irvine repository of machine learning databases.

# Novel linear programming approach for building a piecewise nonlinear binary classi<sup>fi</sup>er with a priori accuracy

Ubaldo M. García-Palomares <sup>a,b,</sup>⁎<sup>,1</sup>, Orestes Manzanilla-Salazar <sup>b,c</sup>

<sup>a</sup> Dep. Ingeniería Telemática, Universidad de Vigo, 36310 Vigo, Spain

<sup>b</sup> Dep. Ingeniería de Sistemas, Universidad Simón Bolívar, Caracas 89000, Venezuela

<sup>c</sup> CESMa, Universidad Simón Bolívar, Caracas 89000, Venezuela

## a r t i c l e i n f o

Article history: Received 19 October 2010 Received in revised form 22 September 2011 Accepted 3 November 2011 Available online 11 November 2011

Keywords: Binary classi<sup>fi</sup>cation Support vector machines Arti<sup>fi</sup>cial neural networks Classi<sup>fi</sup>cation trees Linear programming Piecewise discriminator

## a b s t r a c t

This paper describes a novel approach to build a piecewise (non)linear surface that separates individuals from two classes with an a priori classi<sup>fi</sup>cation accuracy. In particular, total classi<sup>fi</sup>cation with a good generalization level can be obtained, provided no individual belongs to both classes. The method is iterative: at each iteration a new piece of the surface is found via the solution of a Linear Programming model. Theoretically, the larger the number of iterations, the better the classi<sup>fi</sup>cation accuracy in the training set; numerically, we also found that the generalization ability does not deteriorate on the cases tested. Nonetheless, we have included a procedure that computes a lower bound to the number of errors that will be generated in any given validation set. If needed, an early stopping criterion is provided. We also showed that each piece of the discriminating surface is equivalent to a neuron of a feed forward neural network (FFNN); so as a byproduct we are providing a novel training scheme for FFNNs that avoids the minimization of non convex functions which, in general, present many local minima.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Let us <sup>fi</sup>rst mention minor peculiarities of our notation: $R ^ { n }$ denotes the n-th dimensional Euclidean space, lowercase Latin letters are vectors in $R ^ { n } ,$ , x<sup>k</sup> is the k-th component of $x _ { i } ,$ uppercase cursive letters ; , etc., denote sets in $R ^ { n } .$ . Given the sets $\mathcal { D } ,$ the difference set <sup>P N D H</sup>− consists of those members of that do not belong to . Lower-<sup>D H D H</sup>case Greek letters denote scalars. The rest of the notation is rather standard.

This paper is concerned with the binary classi<sup>fi</sup>cation problem (BCP) of determining a discriminating function $h ( \cdot ) { : } R ^ { n } \to R$ that separates individuals belonging to two different classes, say, class $\mathcal { P }$ and <sup>P</sup>class . This is a classical problem that still has vast applications in <sup>N</sup>several areas [4]. This work solves the BCP by successive linear programming (LP) models, which generate nodes of a decision tree. Each node classi<sup>fi</sup>es a group of individuals of one class.

$$
c (x) = \left\{ \begin{array}{r l} 1, & x \in \mathcal {P} \\ - 1, & x \in \mathcal {N}. \end{array} \right.
$$

We assume that an individual x is characterized by its n features $x ^ { 1 } , . . . , x ^ { n }$ and its class indicator c(x),

We extend this de<sup>fi</sup>nition to the class indicator of a set $s ,$

$$
c (\mathcal {S}) = \left\{ \begin{array}{l l} 1, & \mathcal {S} \subseteq \mathcal {P} \\ - 1, & \mathcal {S} \subseteq \mathcal {N} \\ 0, & \text { otherwise }. \end{array} \right.
$$

The discriminating function $h ( \cdot ) : \mathcal { D } \xrightarrow { } R ,$ , also called discriminating <sup>ð Þ D</sup>surface, decision rule or learning rule, satis<sup>fi</sup>es

$$
h (x) \bigg \{> 0, x \in \mathcal {P} <   0, x \in \mathcal {N}.
$$

Albeit a discriminating function always exists, provided $( \mathcal { P } \cap \mathcal { N } ) = \emptyset$ <sup>ð ÞP N ¼</sup>there are practical issues that prevent the practitioners from obtaining a solution. They rather search for the best separating function that minimizes a measure of the error set de<sup>fi</sup>ned as

$$
\mathcal {E} = \{x \in \mathcal {N}: h (x) \geq 0 \} \cup \{x \in \mathcal {P}: h (x) \leq 0 \}.\tag{1}
$$

On top of this, practitioners must formulate a model simple enough to generate an accurate solution within a reasonable time and allocated budget. Instead of striving for a discriminating function two less ambitious objectives are pursued. Given a class of functions $\mathcal { F }$ we want

O1 To <sup>fi</sup>nd the best separating function in for a training set $( \mathcal { T } \subseteq \mathcal { D } )$ O2 To accurately predict the class indicator of those individuals in − .

A variety of optimization models to minimize a measure of the error set have been suggested. Linear programming optimization <sup>E</sup>models (LPs) are mostly used, because they <sup>fi</sup>nd a solution in polynomial time, are robust and may deal with large problems. The simplest strategy is to obtain the best linear separating function. In the late sixties, [26] proposed the multisurface method (MSM), which <sup>fi</sup>nds a piecewise linear discriminating function for the training set . A clear description of MSM is given by [33] and a more updated version of MSM is given by [29].

Least square techniques and nonlinear constrained optimization models are used to train (FFNNs), which can generate a piecewise linear discriminating surface for any two disjoint sets with a suf<sup>fi</sup>ciently large but unknown number of neurons in the hidden layer [17]. MSM may also be used to train a feed forward neural network (FFNN) via LP models [27, Section 2].

Support vector machines (SVMs) developed at Bell Laboratories [41,42] solve quadratic programming optimization models (QPs), mainly with the intention of improving the prediction ability of the solution (objective O2). SVMs use kernels, which allow the search of the best linear separating function in a space bounded by the number of individuals. Primal and Dual $\mathrm { Q P }$ models have been tried for its solution. An account of going on research for an ef<sup>fi</sup>cient implementation of these QP models is given in [3, Section 5]. SVMs' objective is structural risk and does not attempt total separation, which can be obtained by our approach. Hence, our algorithm will render important when this feature is indispensable for the user.

Mixed integer linear programming models (MILPs) have recently been proposed whose solution gives rise to a piecewise separating surface [4,21,22], but there is no hint on the number of pieces necessary to obtain a required classi<sup>fi</sup>cation accuracy. A good account on different optimization models that have been proposed in the open literature to obtain the best separating function is given by Bennett and Parrado-Hernandez [3] and by Smaoui et al. [38].

We should keep in mind that the larger the set of functions ${ \mathcal F } ,$ <sup>F</sup>the better the separating function h∈ that minimizes the error set (1) on $\tau ;$ <sup>F</sup>but commonly the prediction ability on $( { \mathcal { D } } { - } T )$ worsens. <sup>T ð ÞD T</sup>This incident has been called over<sup>fi</sup>tting, and it causes a con<sup>fl</sup>ict between O1 and O2. A common approach is to impose a k-fold validation on any model that tries to satisfy the <sup>fi</sup>rst objective: the given sample is split in k subsamples; one of them is taken as a testing set and the separating function is sought on the training set made up by the remainder of the sample. This is done k times and the rates of success obtained on the testing sets give an estimate of the prediction ability.

This paper presents an iterative algorithm that solves LP models and is able to <sup>fi</sup>nd any explicit classi<sup>fi</sup>cation accuracy on a training set. It offers the following salient properties:

P1 The algorithm generates a piecewise (non)linear discriminating function.

P2 Within a <sup>fi</sup>nite number of iterations a complete or an a priori classi<sup>fi</sup>cation accuracy can always be obtained on the whole training set, or on either of the classi<sup>fi</sup>cation sets.

P3 The optimization model is linear, but may consider as many binary variables as predetermined by the computational resources.

P4 The size of the optimization model decreases with the iteration number; it is then plausible to solve MILPs at the <sup>fi</sup>nal stages of the method.

P5 The algorithm provides a lower bound on the number of errors that will occur in a given testing set.

P6 Large systems can be handled by way of parallelism and/or decomposition of the training set.

P7 An FFNN is easily adapted, which opens up the possibility of hardware implementations with the use of <sup>fi</sup>eld programmable gate arrays (FPGAs). See [39] and ([34], Chapters 1 and 10).

P8 Finally, only basic programming skills are needed for its implementation.

To summarize, our approach enjoys properties P2, P3, P4 which circumvent some of the de<sup>fi</sup>ciencies encountered in FFNNs, SVMs and MILPs mentioned earlier. It also exhibits other properties that enhance its usefulness.

Before proceeding any further, let us illustrate our approach with an easy example. Fig. 1 depicts a dot curve discriminating the sets and ${ \mathcal { N } } .$ <sup>P</sup>Generally this function is unknown to us, and it is in general <sup>N</sup>a dif<sup>fi</sup>cult task to <sup>fi</sup>nd out a nonlinear function that discriminates two classes (see [20], and references therein). Let us graphically exemplify how our algorithm obtains a piecewise linear discriminating function. The <sup>fi</sup>rst iteration of the algorithm <sup>fi</sup>nds a (hyper)plane that forces all individuals in $\mathcal { N }$ to be on one side, and all members <sup>N</sup>of located on the other side are considered well classi<sup>fi</sup>ed (Fig. 2a). The second iteration works on the reduced set of not yet classi<sup>fi</sup>ed individuals (Fig. 2b) and <sup>fi</sup>nds a new (hyper)plane. At this iteration, the hyperplane forces all individuals in $\mathcal { P }$ to be on the <sup>P</sup>same side (Fig. 2c). In this example total classi<sup>fi</sup>cation was obtained; otherwise, the iterations proceed until $\mathcal { P }$ or $\mathcal { N }$ is exhausted. A test is included that may stop the algorithm as soon as a possibility of over<sup>fi</sup>t is detected.

We now formally state the BCP. Let $\mathcal { D } \mathsf { C } \mathcal { R } ^ { n }$ be a bounded set, and <sup>D R</sup>let ; ⊂ . We assume that there exists a discriminating function $f ( \cdot ) : \mathcal { D } {  } R$ such that $f ( x ) > 0$ for all x∈ and $f ( x ) < 0$ for all x∈ . We <sup>ð Þ D P N</sup>also assume that sign(f(x)) is either at hand or easily computable for any x∈ p . In other words, we can easily deduce the class indi-<sup>T D</sup>cator c(x) in some subset of . Let us de<sup>fi</sup>ne the hard-margin $\rho ( f )$ as:

$$
\rho (f) = \min (| | x - z | |), x \in (\mathcal {P} \cup \mathcal {N}), z \in \mathcal {Z} = \{x \in \mathcal {D}: f (x) = 0 \},\tag{2}
$$

where ||⋅|| is any norm in R<sup>n</sup>. Geometrically, we might assume there is a gray zone $\mathcal { Z } _ { \epsilon } = \{ x \in \mathcal { D } : | f ( x ) | \le \epsilon \} \mathbb { F }$ , where sign(f) is uncertain, <sup>Z ¼ f jD ð Þj g</sup>either because of noise or by probabilistic estimation. In any event, the bigger the hard-margin, the better the predictive accuracy of an algorithm [33,37].

Our ultimate objective is to elaborate on linear programming optimization models that with the sign information $c ( x ) = \mathrm { s i g n } ( f ( x ) )$ for x∈ will <sup>fi</sup>nd a discriminating function h : →R with a high $\rho ( h )$ . In <sup>T D</sup>other words, we want the sign functions of h( ) and $f ( \cdot )$ to coincide on $( \mathcal { T } \subseteq \mathcal { D } ) ;$ at the same time we want to preserve an acceptable generalization capability.

![](/api/attachments/2KHNHF6W/fulltext/images/c0957d74890f80202fdca3a4d4117df71dda89f8501bb973e5c53a2cb086a265.jpg)  
Fig. 1. The unknown dot curve strictly discriminates sets and .

![](/api/attachments/2KHNHF6W/fulltext/images/1aa06d51169011f205f8b060e6c12d282f38b135e616b972fd04934ab2e8b735.jpg)  
Fig. 2. Discriminating function made up by 2 planes. The second plane discriminates the reduced set.

To simplify the notation we denote $c ^ { k } = ^ { \mathsf { d e f } } \ c ( x _ { k } )$ , and in order to <sup>¼ ð Þ</sup>have an implementable algorithm we assume that is a <sup>fi</sup>nite set, <sup>T</sup>which is a common strategy to deal with the binary classi<sup>fi</sup>cation problem:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Binary classification problem (BCP):
Given a sample of p points  $(x_{1},c^{1}),\ldots,(x_{p},c^{p})$  with
 $T=\{x_{k}\in\mathcal{D}\},\quad c^{k}=\left\{\begin{array}{ll}1&amp;when x_{k}\in\mathcal{P},\\-1&amp;when x_{k}\in\mathcal{N},\end{array}\right.\quad k=1,\ldots,p,$ 
(3)
find a function  $h(x)$  with high hard-margin  $\rho(h)$  and such that  $c(x)h(x)&gt;0$ , for  $x\in T$ .
</div>

We recall the reader that we focus the BCP within the objectives O1 and O2.

The remainder of the paper is organized as follows: the next section describes the shortcomings and advantages of LP optimization models that have been used for solving BCP and may look as predecessors of our algorithm. Section 3 describes the algorithm and also highlights an equivalent FFNN, which opens up the possibility of a hardware realization of the algorithm. Section 4 addresses some implementation issues that may enhance the algorithm performance and sketches a possible way to adapt the algorithm to a multiprocessing environment. In Section 5 synthetic and standard datasets are run with the algorithm suggested in this paper. Competitive results are reported. Finally, Section 6 concludes the paper with additional comments and <sup>fi</sup>nal remarks.

## 2. Background material

This section is a brief account on LP optimization models that gradually evolve to our model. On occasions we refer to related QP and MILP models. From the onset we specify the basis functions $g ^ { 1 } ( \cdot ) , . . . , g ^ { q } ( \cdot )$ $R ^ { n } { \to } R$ and hereafter denote its shifted linear combination $h ( x ) =$ $w ^ { T } g ( x ) - \theta$ as a hyperplane (in the q dimensional g( ) space). We hope not to offend the reader with this minor deviation. This connotation is however of common use with kernels in SVMs and was also adopted in [22]. It is an easy matter to adapt this $g ( \cdot )$ space into many standard methods that generate the hyperplane $h ( x ) = w ^ { T } x - \theta .$

Given $\tau \in [ 0 \ 1 ] ,$ , a non decreasing function $\phi ( \cdot ) { : } R \to R ,$ a monotone norm $| | \cdot | |$ and a large enough positive α we start with this nonlinear model:

$$
\begin{array}{l} \min _ {w \in R ^ {q}, \theta \in R, y \in R ^ {p}} \tau   \phi (\| w \|) + (1 - \tau) \sum_ {k = 1} ^ {p} y ^ {k} \\ c ^ {k} \Big (w ^ {T} g (x _ {k}) - \theta \Big) + \alpha   y ^ {k} \geq 1, k = 1,..., p \\ y ^ {k} \in \{0, 1 \}. \end{array}\tag{4}
$$

If we denote by $\left( \hat W , \hat \theta , \hat y \right)$ the optimal solution of model (4), the separating function is given by $h ( x ) = \bar { w } ^ { T } g ( x ) - \bar { \theta }$ . Note that for $\tau = 0 ,$ <sup>ð Þ ¼ ð</sup>, and large enough α, the binary variable $\bar { y } ^ { k } = 1$ if and only if $c ^ { k } h ( x _ { k } ) \leq 0 ,$ <sup>¼</sup>that is, a mismatch of the sign functions occurs; ideally we look for $\bar { y } ^ { k } = 0 , k = 1 , . . . , p .$ Therefore, when τ =0 model (4) provides the minimum of the empirical risk with the loss function commonly used in classi<sup>fi</sup>cation problems, which is a good estimate of the expected value of the misclassi<sup>fi</sup>cations [1,41]. Nonetheless, it has been asserted that the term $\boldsymbol { \phi } ( \cdot ) = \boldsymbol { w } ^ { T }$ w in the objective function improves the margin of the solution, which is closely related to the generalization ability of the model [24,41].

Model (4) has a serious shortcoming: there are p binary variables $y ^ { k } , k = 1 , . . . , p$ which may cause computational dif<sup>fi</sup>culties in large databases; however for moderate values of p it is highly recommended even without the normalization term $w ^ { T } w .$ Model (5) relaxes the binary constraints and becomes a variant of the well known support vector machine (SVM), which is probably the actual choice as a binary classi<sup>fi</sup>er in modern applications. The list of references on SVM is still growing at a sustained pace. Recent work is mainly devoted to <sup>fi</sup>nd ef<sup>fi</sup>cient ways for solving (5). See the list of references in [35].

$$
\begin{array}{l} \min _ {w \in R ^ {q}, \theta \in R, y \in R ^ {p}} \tau w ^ {T} w + (1 - \tau) \sum_ {k = 1} ^ {p} y ^ {k} \\ c ^ {k} \Big (w ^ {T} g (x _ {k}) - \theta \Big) + y ^ {k} \geq 1, k = 1,..., p \\ y ^ {k} \geq 0 \end{array}\tag{5}
$$

To make use of the powerful algorithms developed for solving LPs, Bradley and Mangasarian [6] proposed polyhedral norms that can be expressed with linear terms in the objective function. Wu and Zhou [44] have shown that LPs are more ef<sup>fi</sup>cient for large datasets. It has also been stated that norm-1 SVMs tend to generate sparse solutions on w, which is useful to <sup>fi</sup>nd relevant features, as commented in [5, Section 2]. It has also been observed empirically that model (5) with $\tau = 0$ is less sensitive to outliers than other models (Glen [14] cites Freed and Glover [10]).

Bi et al. [5] proposed the split of w in its positive and negative values $w = w _ { + } - w _ { - } , w _ { + } \geq 0 , w _ { - } \geq 0$ and they minimize a weighted combination of ||w||<sub>1</sub> and y. With no loss of generality we omit the weights and model (5) becomes

$$
\begin{array}{l} \underset { \begin{array}{c} w _ {+} \in R ^ {q}, w _ {-} \in R ^ {q} \\ \theta \in R, y \in R ^ {p} \end{array} } {\text {min}} \tau \sum_ {k = 1} ^ {q} \left(w _ {+} ^ {k} + w _ {-} ^ {k}\right) + (1 - \tau) \sum_ {k = 1} ^ {p} y ^ {k} \\ c ^ {k} \Big (\big (w _ {+} - w _ {-} \big) ^ {T} g (x _ {k}) - \theta \Big) + y ^ {k} \geq 1, k = 1,..., p \\ w _ {+}, w _ {-}, y \geq 0. \end{array}\tag{6}
$$

Bi et al. [5] also proposed the asymmetric LP model (7) as a means to identify lung nodules with a subset of cheap features in the <sup>fi</sup>rst stage of their cascade algorithm. For the subsequent stages they always resort to model (6).

$$
\begin{array}{l} \underset { \begin{array}{c} w _ {+} \in R ^ {q}, w _ {-} \in R ^ {q} \\ \theta \in R, y \in R ^ {| \mathcal {P} |} \end{array} } {\text {min}} \tau \sum_ {k = 1} ^ {q} \left(w _ {+} ^ {k} + w _ {-} ^ {k}\right) + (1 - \tau) \sum_ {k = 1} ^ {| \mathcal {P} |} y ^ {k} \\ c ^ {k} \Big ((w _ {+} - w _ {-}) ^ {T} g (x _ {k}) - \theta \Big) + y ^ {k} \geq 1, \quad x _ {k} \in \mathcal {P} \\ c ^ {k} \Big ((w _ {+} - w _ {-}) ^ {T} g (x _ {k}) - \theta \Big) \geq 1, \quad x _ {k} \in \mathcal {N} \\ w _ {+}, w _ {-}, y \geq 0. \end{array}\tag{7}
$$

A drawback of these optimization models is that the quality of their solutions strongly depends on the parameter τ, and tuning experiments must be carried out beforehand [5,7,12,18,35]. We should point out that if for some basis functions $g ^ { 1 } ( \cdot ) , . . . , g ^ { q } ( \cdot )$ there exist w^ ; <sup>^</sup>θ<sup> </sup> such that

$$
x \in \mathcal {P} \Rightarrow \hat {w} ^ {T} g (x) - \hat {\theta} > 0, \text {   and   } x \in \mathcal {N} \Rightarrow \hat {w} ^ {T} g (x) - \hat {\theta} <   0,\tag{8}
$$

then the discriminant $\hat { w } ^ { T } g ( x ) - \hat { \theta }$ solves the optimization models (5, $6 , 7 )$ when $\tau = 0 .$ <sup>ð Þ</sup>Nonetheless, these basis functions are in general unknown and dif<sup>fi</sup>cult to obtain [20, and references therein].

A matter of concern in all aforementioned models is the possibility of the optimal trivial solution $w = 0$ and several normalization procedures have been suggested. Mangasarian et al. [28] proposed the constraint $| | \boldsymbol { w } | | _ { \infty } = 1$ , which involves the formulation of 2q linear programming problems. This simple arti<sup>fi</sup>ce has a nice geometric interpretation and has given good results in practical problems; however, it may become a computational burden when solving large data sets with the use of Gaussian Kernels or when q, the number of basis functions, is large. Glover et al. [16] proposed to choose the better solution of two models: a model with the constraint $\sum _ { k } w ^ { k } \ge 1$ , and the other model with the constraint $\scriptstyle \sum _ { k } w ^ { k } \leq - 1$ This scheme was criticized by [23] because it left out some interesting points that satisfy $\textstyle \sum _ { k } w ^ { k } = 0$ . Nonetheless, Better et al. [4] report good results with the constraint $\textstyle \sum _ { k } w ^ { k } = 1$ in a MILP model.

Recent research has focused on models that generate at once multiple pieces of a separating function. A MILP with a large number of binary variables is proposed. This model has no polynomial solution time, but it renders excellent results for small data sets [22]. We should mention that the number of hyperplanes is a <sup>fi</sup>xed model parameter, but in general, the number of hyperplanes necessary to achieve an a priori classi<sup>fi</sup>cation accuracy is not known. For additional details on the use of MILPs we refer the reader to [4,15,21,22].

The LP optimization model that we propose in the next section may be formulated with a number of variables and constraints significantly lower than those required by the aforementioned algorithms. It is solved iteratively and at each iteration generates a non linear piece of the discriminating surface. The method ends when a classi<sup>fi</sup>- cation accuracy, predetermined by the practitioner, is obtained.

## 3. Optimization model and algorithm

The structure of our model resembles model (7); but ours is formulated with fewer constraints and variables. On one hand, we do not split w in its positive and negative part, although we will reconsider this option to implement an SVM in subsection 5.7. On the other hand, our model does not require as many constraints and variables as individuals in the training set. Let be a set of individuals <sup>S</sup>of the same class, that is, either p , in which case $\begin{array} { r } { c ( { \mathcal { S } } ) = 1 , 0 \Gamma { \mathcal { S } } \subseteq { \mathcal { N } } ; } \end{array}$ in which case, $c ( S ) = - 1$ . Let $\mathcal { X } = \{ x \in \mathcal { T } : c ( x ) = - c ( \mathcal { S } ) \}$ <sup>¼ S N</sup>. Given a parameter $\tau { \geq } 0 ,$ <sup>ð ÞS ¼ X ¼ f T ð Þ ¼</sup>, we formulate the LP model (9a) with $q + 1 + | S |$ variables, $| S | + | \mathcal { X } | + 1$ constraints and the bounds on the variables $| | w | | _ { \infty } \leq 1 0 , | \theta | \leq 1 0 0 , y \geq 0$ . Model (9b) considers binary variables and may be useful and convenient if our computational resources allow us to deal with MILPs. Our analysis however, will focus on the continuous model.

In order to deal with LP models, 9a and 9b should be solved by 3 optimization problems, with the constraint $w \neq 0$ replaced respectively by

$$
i) \sum_ {k = 1} ^ {q} w ^ {k} \geq 1, i i) \sum_ {k = 1} ^ {q} w ^ {k} \leq - 1, \text {   and   } i i i) - 1 \leq \sum_ {k = 1} ^ {q} w ^ {k} \leq 1.
$$

These are LP models bounded from below and therefore solvable. In case of infeasibility we can adjust the bound on θ, but this never occurred in our tests. We can select the best solution according to some criterion like fewer number of misclassi<sup>fi</sup>cations, minimum objective function, or any other criterion more suitable to the application at hand.

We should mention that our algorithm is iterative; at each iteration well classi<sup>fi</sup>ed individuals will not be considered again in further iterations, as it was proposed in MSM. This implies that the size of the model gets smaller and eventually binary variables can be taken into account.

$$
\begin{array}{c} \underset {w \in R ^ {q}, y \in R ^ {| S |}, \theta \in R} {\text {min}} \sum_ {x _ {k} \in \mathcal {S}} y ^ {k} \\ c (\mathcal {S}) \left(w ^ {T} g (x _ {k}) - \theta\right) + y ^ {k} \geq 1, x _ {k} \in \mathcal {S} \\ - c (\mathcal {S}) \left(w ^ {T} g (x _ {k}) - \theta\right) \geq 1, x _ {k} \in \mathcal {X} \\ w \neq 0 \\ \| w \| _ {\infty} \leq 1 0, | \theta | \leq 1 0 0, y \geq 0 \end{array}\tag{9a}
$$

$$
\begin{array}{c c} \underset {w \in R ^ {q}, y \in R ^ {| S |}, \theta \in R} {\text {min}} \sum_ {x _ {k} \in \mathcal {S}} y ^ {k} \\ c (\mathcal {S}) \Big (w ^ {T} g (x _ {k}) - \theta \Big) + \alpha y ^ {k} \geq 1, & x _ {k} \in \mathcal {S} \\ - c (\mathcal {S}) \Big (w ^ {T} g (x _ {k}) - \theta \Big) \geq 1, & x _ {k} \in \mathcal {X} \\ w \neq 0 \\ \| w \| _ {\infty} \leq 1 0, | \theta | \leq 1 0 0, y \in \{0, 1 \} \end{array}\tag{9b}
$$

Fig. 3 displays a signi<sup>fi</sup>cant difference between previous models and ours: Fig. 3a shows the training set, Fig. 3b shows the best separating hyperplane generated by SVMs, with 6 classi<sup>fi</sup>cation errors. It allows errors on both and . The <sup>fi</sup>rst iteration of MSM generates <sup>P N</sup>2 parallel hyperplanes to the SVM hyperplane and correctly classi<sup>fi</sup>es 6 individuals in its <sup>fi</sup>rst iteration (Fig. 3c). This number is always a lower bound to our algorithm. At each iteration, models (9a) and (9b) force all members of one class to be on the same side of the hyperplane and correctly classify as many members of the other class as possible (Fig. 3d). After two iterations (2 hyperplanes) our algorithm has already classi<sup>fi</sup>ed 14 individuals (Fig. 3e). After an unde<sup>fi</sup>ned number of iterations it will correctly classify the whole training set . Recent work [30,31] describes an earlier version of this algorithm <sup>T</sup>with encouraging results on synthetic and real datasets.

To apply models (9a) and (9b) a set is selected, which must be <sup>S</sup>either a subset of or a subset of . The initial iteration may only <sup>P N</sup>consider those individuals with trust values for $c ( x ) , \operatorname { s a y } , c ( x ) = c ( S )$

![](/api/attachments/2KHNHF6W/fulltext/images/5d55c02a53c1657126a09aaf11ef8eb357a96b2fd12b553539dd80df53f1f8a9.jpg)  
Fig. 3. Training set (a), SVM plane (b), one iteration of MSM (c), and two iterations of our algorithm (d,e).

with a high probability. We may also solve models (9a) and (9b) for $\begin{array} { r } { { \cal S } _ { k } { \cal C } { \cal S } , k = 1 , . . . , m , } \end{array}$ for some m, either sequentially or in parallel. It <sup>S S ¼</sup>is worth mentioning that we could solve (9b) for small values of $| S _ { k } | , k = 1 , . . . , m$ : The extreme case when $| S _ { k } | = 1 , k = 1 , . . . , m$ , albeit <sup>Sj j ¼ Sj</sup>probably inef<sup>fi</sup>cient, is theoretically possible.

Given any feasible, but not necessarily an optimum solution w\~ ; <sup>\~</sup>θ; y\~ <sup> </sup> to models (9a) and (9b), let us de<sup>fi</sup>ne $h ( x ) = \tilde { w } ^ { t } g ( x ) - \tilde { \theta } ,$ the hyperplane $\partial \mathcal { H } = \{ x \in \mathcal { D } : c ( S ) h ( x ) = - 1 \}$ , and the half space $\mathcal { H } = \{ x \in \mathcal { D } : c ( \mathcal { S } ) h ( x ) \leq - 1 \}$ <sup>gD ð ÞS ð Þ ¼</sup>, which contains all individuals yet to be classi<sup>fi</sup>ed. We claim that p because of the constraint $- c ( \mathcal { S } ) ( w ^ { T } g ( x _ { k } ) - \theta ) \geq 1 , x _ { k } \in \mathcal { X } .$ Also $\{ x _ { k } { \in } S : y ^ { k } > 2 \} { \subset } \mathcal { H } ,$ in model (9a) <sup>ð</sup>and $\{ x _ { k } { \in } S : y ^ { k } = 1 \} { \subset } \mathcal { H }$ <sup>X S H</sup>in model (9b) because they have not been clas-<sup>S ¼ H</sup>si<sup>fi</sup>ed. The algorithm interprets that all individuals in $\mathcal { Q } = \left( \mathcal { D } - \mathcal { H } \right)$ <sup>Q ¼ Dð ÞH</sup>are well classi<sup>fi</sup>ed, including those that do not belong to the training set. Note that individuals in the set $\{ x { \in } \mathcal { Q } : c ( x ) = - c ( \mathcal { S } ) \}$ will be misclassi<sup>fi</sup>ed.

![](/api/attachments/2KHNHF6W/fulltext/images/9f09147d29284b538ff0e2bacfbd9ebd6647f9d1c1cd0423dbe83cc2c8bf8a79.jpg)  
Fig. 4. Training algorithm. Each plane $\partial \mathcal { H } _ { \mathrm { i } }$ is a decision node. $c ( S _ { i } )$ is needed to check the testing set. Individuals in $\mathcal { Q } _ { i }$ are assigned the class $c ( S _ { i } ) .$ , Remaining individuals go to the next decision node.

The classi<sup>fi</sup>cation tree and a description of the basic training algorithm is given in Fig. 4. Its input is a training set of individuals with <sup>T</sup>known features and class indicator. Its outputs are t separating hyperplanes ∂ H and t class indicators $c ( S _ { i } ) , i = 1 , . . . , t ,$ where t is <sup>fi</sup>nite, <sup>S ¼</sup>although unknown beforehand. At all iterations either $S _ { i } \subseteq ( \mathcal { P } \cap \mathcal { R } _ { i } )$ or $S _ { i } \subseteq ( \mathcal { N } \cap \mathcal { R } _ { i } )$ , where $\mathcal { R } _ { i }$ <sup>S ð ÞP R</sup>stands for the reduced set of individuals that <sup>S ð ÞN R R</sup>have not as yet been classi<sup>fi</sup>ed $( \mathcal { R } _ { 1 } = \mathcal { T } )$ . This set is updated at each iteration; $\mathcal { R } _ { i + 1 } = \mathcal { R } _ { i } - Q _ { i } ,$ , where $\mathcal { Q } _ { i } = \mathcal { D } \mathrm { - } \mathcal { H } _ { i }$ is the set of quali<sup>fi</sup>ed in-<sup>R þ ¼ R</sup>dividuals; we label $c ( \mathcal { Q } _ { i } ) = c ( \mathcal { S } _ { i } )$ . The algorithm stops when either $( \mathcal { R } _ { i } \cap \mathcal { P } ) = \emptyset , \mathrm { o r } \left( \mathcal { R } _ { i } \cap \mathcal { N } \right) = \emptyset$ <sup>ð ÞS</sup>, that is, when there is no individual be-<sup>ð Þ ¼R P ð Þ ¼R N</sup>longing to either one of the classes. Other stopping conditions will be considered in Section 4.

At any iteration, say the j-th one, we can label the class indicator for all x∈ as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
for  $x \in D$ $\zeta_{0}(x) = -c(S_{j})$ 
for  $i = 1, \ldots, j$ 
    if  $x \notin H_{i}$ $\zeta_{0}(x) = c(S_{i})$ 
    break
    endif
    endfor
endfor
</div>

10

When the algorithm terminates, that is, when $j = t$ we have that $\boldsymbol { x } { \in } \mathcal { T } { \Rightarrow } ( \zeta _ { 0 } ( \boldsymbol { x } ) = c ( \boldsymbol { x } ) )$ . This equality does not necessarily hold when $\scriptstyle x \in ( { \mathcal { D } } - T ) .$

Glen [14] proposes a MILP to re<sup>fi</sup>ne the separating surface and claims that the performance of the classi<sup>fi</sup>er improves. We could merely slide the hyperplane $\partial \mathcal { H } _ { i }$ until maximum margin is obtained, that is, de<sup>fi</sup>ne $\begin{array} { r } { f ( \pmb { x } ) = c ( \mathcal { S } _ { i } ) \pmb { w } _ { i } ^ { T } \pmb { g } ( \pmb { x } ) - \pmb { \theta } , } \end{array}$ , and <sup>fi</sup>nd θ such that min $f ( x )$ $\scriptstyle x \in ( S _ { i } \cap \mathcal { Q } _ { i } ) = \operatorname* { m i n } | f ( x ) | , x \in \mathcal { X } _ { i }$ . A more elaborate LP model will be dis-<sup>ð Þ ¼S Q j ð</sup>cussed in Section 4.

## 3.1. Basis functions

This subsection refers to the basis function $g ( \cdot )$ . After a brief introduction we suggest a particular simple basis function that theoretically ensure that the algorithm will stop with total classi<sup>fi</sup>cation provided $( \mathcal { P } \cap \mathcal { N } ) = \emptyset$

<sup>ð Þ ¼P N</sup>The simplest basis is $g ^ { j } ( x ) = \mu _ { j } x ^ { j } , j = 1 , . . . , n ,$ which allows scaling or transformation of the variables, and piecewise linear separating surfaces. An extremely useful technique with SVMs has been the use of kernels. We can follow Kim and Ryoo [22], Section 3.5 and easily adopt kernels as basis functions in our approach; we could as well randomly select a <sup>fi</sup>nite set of individuals in $\mathcal { D } , \mathcal { Z } = \{ z _ { 1 } , . . . , z _ { m } \}$ and use $\overset { \cdot } { g ^ { k } } ( x ) = K ( z _ { k } , x ) , k = 1 , . . . , m ,$ , as suggested by Fung et al. [13]. We could also <sup>fi</sup>nd incrementally as suggested by Keerthi et al. <sup>Z</sup>[20]. Good numerical results for SVMs have been found with these strategies, and its use as basis functions should yield good results. Kernels in general work on higher dimensional subspaces and consequently demand more computational resources.

Quadratic separability has also been recently suggested. Liu and Potra [25] use semide<sup>fi</sup>nite programming to determine an ellipsoid capable of separating individuals of the same class from the rest. We now turn our attention to more manageable basis, which have the desirable property to allow <sup>fi</sup>nite termination for models (9a) and (9b) with total classi<sup>fi</sup>cation, provided $( \mathcal { P } \cap \mathcal { N } ) = \emptyset$

Proposition 1. Let $z { \in } { \tau }$ be any individual, let $S = \{ z \} , ~ \mathcal { X } =$ $\{ x { \in } T : c ( x ) = - c ( z ) \}$ <sup>T</sup>, and let $g ( x )$ <sup>S ¼ f g X ¼</sup>be either one of the following basis <sup>f T ð</sup>functions:

$$
g (x) = \left(x ^ {1},..., x ^ {n}, x ^ {T} x\right), \text { or }\tag{11a}
$$

$$
g (x) = \left(x ^ {1}, \dots , x ^ {n}, \left(x ^ {1}\right) ^ {2}, \dots , \left(x ^ {n}\right) ^ {2}\right),\tag{11b}
$$

If z∉ there always exists a linear combination of the basis function g( ) in (11a) and (11b) that strictly separates z from .

Proof. Let $\begin{array} { r } { \delta = m i n _ { x \in \mathcal { X } } | | x { - } z | | _ { 2 } , } \end{array}$ , and de<sup>fi</sup>ne $\nu = z .$

We have $\delta ^ { 2 } > 0 = ( z - \nu ) ^ { T } ( z - \nu ) = z ^ { T } z - 2 \nu ^ { T } z + \nu ^ { T } \nu ;$ hence $z ^ { T } z -$ $2 \nu ^ { T } z < \delta ^ { 2 } - \nu ^ { T } \nu .$

On the other hand, for any x∈ we have that $\delta ^ { 2 } \leq ( x - \nu ) ^ { T } ( x - \nu ) =$ $\boldsymbol { x } ^ { T } \boldsymbol { x } - 2 \boldsymbol { \nu } ^ { T } \boldsymbol { x } + \boldsymbol { \nu } ^ { T } \boldsymbol { \nu } ;$ hence $x ^ { T } x - 2 \nu ^ { T } x \geq \delta ^ { 2 } - \nu ^ { T } \nu$ . De<sup>fi</sup>ne the weights $w ^ { k } =$ $- 2 \nu ^ { k } , k = 1 , . . . , n$ , and $\theta = \delta ^ { 2 } - z ^ { T } z$

To end the proof we only need to specify $\boldsymbol { w } ^ { n + 1 } = 1$ if we use (11a), or $w ^ { k } = 1 , k = n + 1 , . . . , 2 n$ if we use (11b).

Basis (11a) and (11b) guarantee that the algorithm theoretically possesses total classi<sup>fi</sup>cation. We may simply separate a single individual z at every iteration. To ensure feasibility of models (9a) and (9b) we may adjust the bounds $\| w \| _ { \infty } \leq \lvert | 2 z \rvert | _ { \infty } , \lvert \theta \rvert \leq | \delta ^ { 2 } - z ^ { T } z | .$ A useful application of these basis will be given in the implementation section. Another feature that should not be overlooked is the capacity of the algorithm to use spheres as separating surfaces with the basis (11a) and (11b) (see Fig. 5).

## 3.2. Neural network interpretation

This subsection shows that our approach can be considered as a training method via LP models for the feed forward neural network (FFNN) depicted in Fig. 6. The MSM approach can also train FFNNs via LP techniques [27, Section 2] and it has the same drawbacks aforementioned for the BCP. In particular, MSM cannot <sup>fi</sup>nd two hyperplanes that correctly classi<sup>fi</sup>es individuals of different classes for the training set depicted in Fig. 5.

![](/api/attachments/2KHNHF6W/fulltext/images/4c2275605976c56b746f5e5d9a2ab9b804e1d1a5cd17a53e57635cd6cd64fb61.jpg)  
Fig. 5. Using (11a) to separate individuals with a sphere

Network 6 is composed of hard limiter neurons. The outputs of neurons in the hidden layer are given by $b ^ { j } = 1 { \mathrm { ~ i f ~ } } \nu _ { j } ^ { T } g > \xi ; b ^ { j } = 0$ otherwise, $\mathrm { f o r } j = 1 , \ldots , t .$ The output of the <sup>fi</sup>nal neuron is slightly different: $\zeta = \mathrm { s i g n } \left( u ^ { T } b - \xi _ { t + 1 } \right)$ . FFNNs were popular classi<sup>fi</sup>ers until the advent of the SVM. It is known that there exists a <sup>fi</sup>nite t and values $( \nu , \xi , u )$ that will discriminate any two sets and provided $\mathcal { P } \cap \mathcal { N } =$ $\emptyset \ [ 1 9 ]$ , but the conventional training of FFNN of minimizing the square errors of the outputs usually leads to <sup>fl</sup>at non convex optimization problems with many local minima and a deterioration of the generalization ability may occur [43]. On the other hand, modern technology allows hardware implementations of FFNNs with the use of <sup>fi</sup>eld programmable gate arrays (FPGAs), which opens up the possibility of real time response. See Szabó and Horváth [39] and Omondi and Rajapakse [34, Chapters 1 and 10].

Fig. 7 is the neural network equivalent to our approach with

$$
\begin{array}{l} v _ {j} = c \Big (\mathcal {S} _ {j} \Big) w _ {j} \\ \xi_ {j} = c \Big (\mathcal {S} _ {j} \Big) \theta_ {j} - 1 \\ u ^ {j} = c \Big (\mathcal {S} _ {j} \Big) / 2 ^ {j} \\ \xi_ {t + 1} = c (\mathcal {S} _ {t}) / 2 ^ {t + 1} \end{array} \quad j = 1,..., t,\tag{12}
$$

and consequently

$$
\zeta (x) = \operatorname{sign} \left[ \sum_ {k = 1} ^ {t} b ^ {k} c \left(\mathcal {S} _ {k}\right) / 2 ^ {k} - c \left(\mathcal {S} _ {t}\right) / 2 ^ {t + 1} \right].\tag{13}
$$

![](/api/attachments/2KHNHF6W/fulltext/images/3bce760fdc18fc410e13b37e575e43810c4d578cad5d413e4e82892d90044b86.jpg)  
Fig. 6. A feedforward neural network with hard limiter neurons: $b ^ { j } = 1 \mathrm { ~ i f ~ } \nu _ { j } ^ { T } g > \xi _ { j } , b ^ { j } = 0$ otherwise $j = 1 , . . . , t ; \zeta = \mathrm { s i g n } ( u ^ { T } b - \xi _ { t + 1 } ) .$

![](/api/attachments/2KHNHF6W/fulltext/images/5bc3a09b17c9fdf1644953ca4b7c6a86171bb52086f46bc00260dc099efe9f03.jpg)  
Fig. 7. Equivalent feed forward neural network with t neurons in the hidden layer.

Geometrically, each neuron in the hidden layer corresponds to the hyperplane ∂ de<sup>fi</sup>ned by our algorithm. We now prove that for any $x { \in } T , \zeta ( x )$ , the output of the network (Fig. 7) equals $\zeta _ { 0 } ( x )$ , the value given by (10). Consequently, as a byproduct, our algorithm gives an alternative way to train the FFNN (Fig. 6). It <sup>fi</sup>nds the values $( \nu , \xi , u )$ with LPs, instead of solving a more demanding non convex optimization problem.

## Remark 1.

$$
x \in \mathcal {H} _ {i} \Longleftrightarrow b ^ {i} = 0
$$

Proposition 2. $\zeta _ { 0 } ( x ) = \zeta ( x )$ for all x∈ .

Proof. Assume $\textstyle x \in { \mathcal { H } }$ foralli≤t. By $( 1 0 ) \ \zeta _ { 0 } ( x ) = - c ( S _ { t } )$ . By Remark 1, $b ^ { i } = 0$ <sup>H</sup> for all i ≤ t. Hence, by $\widehat { ( 1 3 ) } \zeta ( x ) = \mathrm { s i g n } \Big ( - c ( S _ { t } ) / 2 ^ { t + 1 } \Big ) = - c ( S _ { t } )$

Now assume that x∈ for all jbt and x∉ . By $( 1 0 ) \zeta _ { 0 } ( x ) = c ( S _ { t } )$ By the previous remark, this happens if and only if $b ^ { j } = 0 , j < t ,$ <sup>ð ÞS</sup><sub>and</sub> $b ^ { t } = 1 . \mathrm { ~ B y ~ } ( 1 3 ) \ \zeta ( x ) = \mathrm { s i g n } \big ( c ( S _ { t } ) \big ( 1 / 2 ^ { t } { - } 1 / 2 ^ { t + 1 } \big ) \big ) = c ( S _ { t } ) .$

<sup>ð Þ ¼ ð ÞS ¼ ð</sup>Finally, let us assume that there exists i b t such that $\boldsymbol { x } { \in } \mathcal { H } _ { j }$ for all j b i andx∉ $\because \mathcal { H } _ { i } .$ We obtain $\begin{array} { r } { _ { 1 } \zeta _ { 0 } ( x ) = c ( S _ { i } ) , \zeta ( x ) = \mathrm { s i g n } \Big ( c ( S _ { i } ) / 2 ^ { i } + \frac { j = i + 1 t } { \Sigma } \ b ^ { j } c ( S _ { j } ) / } \end{array}$ $2 ^ { j } - c ( S _ { t } ) / 2 ^ { t + 1 } \Big )$ . By observing that $\begin{array} { r } { \left| \sum _ { j = i + 1 } ^ { t } b ^ { j } c ( S _ { j } ) / 2 ^ { j } - c ( S _ { t } ) / 2 ^ { t + 1 } \right| < 1 / 2 ^ { i } } \end{array}$ we can assert that $\zeta ( x ) = c ( S _ { i } )$ , which completes the proof.

## 4. Implementation issues

We have coded our programs in MATLAB version 7.5 on a laptop with Windows XP equipped with a 1.8 GHz Intel with 1 GB of RAM and use the COIN-OR clp LP code for solving (9a) as recommended by [40]. We now address several interesting issues on the pseudo code described in Fig. 4.

## 4.1. Stopping criteria

The algorithm just explained and shown in Fig. 4 stops after it <sup>fi</sup>nds a quadratic discriminating function, with either (11a) or (11b), that fully separates $\mathcal { P }$ from ${ \mathcal { N } } ,$ though it is an easy matter to <sup>P N</sup>use (10) to stop the training when some classi<sup>fi</sup>cation level for either class, or for the whole training set, is reached. We just remark that at each iteration, say the j-th one,

$$
p = \sum_ {i \leq j, c (\mathcal {S} _ {i}) = 1} | \mathcal {Q} _ {i} | \text {   and   } q = \sum_ {i \leq j, c (\mathcal {S} _ {i}) = - 1} | \mathcal {Q} _ {i} |,
$$

represents respectively, the number of individuals from and that are correctly classi<sup>fi</sup>ed; hence, $p + q$ <sup>P N</sup>is a lower bound to the classi<sup>fi</sup>cation accuracy. We must emphasize that at the j-th iteration the classi-<sup>fi</sup>cation error on the training set is exactly $\left| { { S _ { j } } \cap { \mathcal { H } } _ { j } } \right|$ , which might be of utmost interest to the practitioner, who can stop the algorithm when he feels that a certain accuracy is acceptable for the particular problem at hand.

Instead of classi<sup>fi</sup>cation accuracy, the practitioner might be more concerned with generalization and may use a validation set $\nu$ to cope with over<sup>fi</sup>tting. At the j-th iteration, the cardinality $\left| \mathcal { E } _ { j } \right|$ of the set

$$
\mathcal {E} _ {j} = \left\{x \in \left(\mathcal {V} - \mathcal {H} _ {j}\right): c (x) \neq \zeta_ {0} (x) \right\}
$$

provides a lower bound to misclassi<sup>fi</sup>cation errors in and the algorithm may stop when $\left| \mathcal { E } _ { j } \right| / \left| \mathcal { V } \right|$ <sup>V</sup>surpasses an a priori given value. <sup>E  j jV</sup>Early stopping was proposed long ago [36] and it has been stated that ideally the training accuracy should only be slightly better than the accuracy on the validation set [2].

## 4.2. Regularization constraint on w

In our implementation models (9a) and (9b) are <sup>fi</sup>rst solved with the constraint $\textstyle \sum _ { j = 1 } ^ { q } w ^ { j } \geq 1$ and then with the constraint $\textstyle \sum _ { j = 1 } ^ { q } w ^ { j } \leq - 1$ <sup>¼ ¼</sup>We choose the solution hyperplane with the larger number of classi-<sup>fi</sup>ed individuals. If in both cases $\mathcal { Q } = \mathcal { Q }$ we declare that $\begin{array} { r } { \mathcal { Q } _ { i } = \mathcal { O } . } \end{array}$ . In other words, we do not attempt the third LP with the constraints $\scriptstyle - 1 \leq \sum _ { i = 1 } ^ { q } w ^ { j } \leq 1$

<sup>¼</sup>We also declare a LP failure if no solution exists in the <sup>fi</sup>rst two LP models.

![](/api/attachments/2KHNHF6W/fulltext/images/6b69c7c2d0787241bb11532b2974f6657d2d18f89c64184436c6f64251df404d.jpg)  
(a) Original dataset

![](/api/attachments/2KHNHF6W/fulltext/images/ac159c3310114725c9468ccfb5f6553e768b31e0a61453689ddfec9f67adc580.jpg)  
(b) Reduced set  
Fig. 8. Spiral dataset. On the right: $( S = { \mathcal { P } } ) { \Rightarrow } ( \mathcal { Q } = \emptyset ) .$

## 4.3. Convergence tolerances

Little attention has been paid to the roundoff errors arising from the solution of any optimization package. We relinquished an LP software that on several iterations reported infeasible solutions to model (9a). Besides, we introduced a tolerance in the de<sup>fi</sup>nition of $\mathcal { H } _ { i }$ in Fig. 4. Speci<sup>fi</sup>cally, $\mathcal { H } _ { i } = \{ x { \in } \mathcal { R } _ { i } : c ( S _ { i } ) h _ { i } ( x ) { \leq } \mathrm { - } ( 1 + \epsilon ) \}$ , with $= 1 0 ^ { - 7 } .$

## 4.4. Abnormal solution

Accumulation of roundoff errors that occur in any computer package may induce faulty statements. Other than the LP failure just mentioned, there exists the possibility that the algorithm speci<sup>fi</sup>es $\begin{array} { r } { \mathcal { Q } _ { i } = \mathcal { O } ; } \end{array}$ which may occur either by roundoff errors or by situations like that one depicted in Fig. 8(b). We recall that by Proposition 1 we may use (11a) or (11b) to encircle single individuals and therefore avoid $\mathcal { Q } _ { i } = \mathcal { O } . \mathsf { W h e n }$ $\mathcal { Q } _ { i - 1 } \neq \mathcal { O }$ we choose $\boldsymbol { S } _ { i }$ <sup>Q ¼</sup>as described in Fig. 4; otherwise, we use the basis (11a) or the basis (11b) and force $0 { < } | S _ { i } | { \le } | S _ { i - 1 } | / 4$ . The algorithm stops with an abnormal exit when $\mathcal { Q } = \mathcal { Q }$ <sup>Sj j</sup><sub>and</sub> $( S ) = 1$ . Theoretically this can only happen when $( \mathcal { P } \cap \mathcal { N } ) \neq \emptyset$

## 4.5. Choice of and large data sets

The pseudo code in Fig. 4 requires all members of $\boldsymbol { S _ { i } }$ to belong to the same class; either $S _ { i } \subseteq ( \mathcal { P } \cap \mathcal { R } _ { i } )$ OR $S _ { i } \subseteq ( \mathcal { N } \cap \mathcal { R } _ { i } )$ <sup>S</sup>. Apart from this <sup>S ð ÞP R S ð ÞN R</sup>minor condition, there is complete freedom to choose $\boldsymbol { S _ { i } }$ when $\mathcal { Q } _ { i - 1 } \neq \mathcal { O }$ . Any of the following strategies is valid:

$$
\begin{array}{l} * \mathcal {S} _ {i} \subseteq (\mathcal {P} \cap \mathcal {R} _ {i}) Z \text {when} | \mathcal {P} \cap \mathcal {R} _ {i} | \geq | \mathcal {N} \cap \mathcal {R} _ {i} |; \text {else} \mathcal {S} _ {i} \subseteq (\mathcal {N} \cap \mathcal {R} _ {i}) \\ * c (\mathcal {S} _ {i + 1}) = c (\mathcal {S} _ {i}) Z \\ * c (\mathcal {S} _ {i + 1}) = - c (\mathcal {S} _ {i}) Z \\ * c (\mathcal {S} _ {i + 1}) Z \text {is randomly chosen.} \end{array}
$$

We switch c at every iteration, except when dealing with large datasets. In this case, we force $\lvert \mathcal { X } _ { i } \rvert { \le } 4 0 0 0$ for all i, which enables us to <sup>Xj j</sup>solve the letter dataset from the Irvine repository with 20,000 samples [9]. It is theoretically possible to split $\mathcal { S } _ { i } = \cup _ { k = 1 } ^ { p } \mathcal { S } _ { i k }$ and run the <sup>S ¼ ¼ S</sup>pseudo code in Fig. 4 on each of these subsets, either sequentially or in parallel. We may de<sup>fi</sup>ne $\mathcal { Q } _ { i } = \cup _ { k = 1 } ^ { p } \mathcal { Q } _ { i k }$ and end the i-th iteration <sup>Q ¼ ¼</sup> <sup>Q</sup>after all subsets have been run. We might as well end the i-th iteration as soon as we <sup>fi</sup>nd $k \in \{ 1 , . . . , p \}$ such that $\mathcal { Q } _ { i k } \neq \mathcal { O } ;$ in this case, we de<sup>fi</sup>ne $\mathcal { Q } _ { i } = \mathcal { Q } _ { i k }$ . Total classi<sup>fi</sup>cation and the equivalent ANN are still valid.

Decomposition will be specially useful for large data sets.

## 4.6. Refinement of ∂

In the previous section we provide a way to improve the generalization ability of the classi<sup>fi</sup>er. We could also try to solve the LP model

$$
\begin{array}{c} \underset {w \in R ^ {d}, \theta , \alpha \in R} {\text { maximum }} \\ c (\mathcal {S} _ {i}) \Big (w ^ {T} g (x _ {k}) - \theta \Big) - \alpha \geq 0, \quad x _ {k} \in (\mathcal {S} _ {i} \cap \mathcal {Q} _ {i}) \\ c (\mathcal {S} _ {i}) \Big (w ^ {T} g (x _ {k}) - \theta \Big) + \alpha \leq 0, \quad x _ {k} \in \mathcal {X} _ {i} \\ \text { sign } \Big (w _ {i} ^ {j} \Big) w ^ {j} \geq 0, \quad j = 1,..., q \\ \sum_ {j = 1} ^ {q} \text { sign } \Big (w _ {i} ^ {j} \Big) w ^ {j} = 1, \end{array}\tag{14}
$$

which <sup>fi</sup>nds a unitary $w , \lvert \lvert w \rvert \rvert _ { 1 } = 1$ , with the same sign structure of $w _ { i }$ that best separates $( \boldsymbol { S } _ { i } \cap \mathcal { Q } _ { i } )$ from $\mathcal { X } _ { i } .$ We have not yet tried this model in our tests.

## 4.7. Model variant

Weights may be useful when the practitioner considers there are signi<sup>fi</sup>cant cost differences in the deviations y. Let 0ba∈ $\bar { \iota } R ^ { ( S ) }$ be a given vector of weights; the objective function becomes $\sum x _ { k } \in { \mathcal { S } } ~ a ^ { k } y ^ { k } .$ . Zou and Yuan [45] claim that for certain applications it could be advantageous to group some deviations in one factor before solving model 5 (or model 6). This is easily adapted to our model. Another possibility that could be introduced in the model is the effect of different basis functions for each hyperplane; that is, $h _ { i } ( \boldsymbol { x } ) = w _ { i } ^ { T } g _ { i } ( \boldsymbol { x } ) - \theta _ { i } , i = 1 , . . . , t .$

Finally we should point out that different objective functions can be used in our model (9a), as long as the constraints push all members of one class to the same side of the hyperplane. The objective function must somehow maximize the cardinality of or some <sup>Q</sup>other merit that in the long run improves the performance of the algorithm. To <sup>fi</sup>nd the best objective function does not seem to be an easy task.

## 5. Numerical tests

We conducted a series of experiments on a code written in MATLAB version 2007, which was tested on some synthetic examples and on small to medium size datasets from the Irvine repository [9]. As LP solver we used the clp-MatLab interphase suggested by Trotscher [40]. We should mention that the MatLab linprog code consistently failed.

As it has been stated, our algorithm theoretically obtains any a priori classi<sup>fi</sup>cation accuracy, including 100%, whereas most previous algorithms report the accuracy they are able to achieve. Hence, straightforward comparison on training accuracy is not evident; however, we report numerical results on prediction ability that show that our algorithm competes favorably.

## 5.1. Algorithm performance

In order to estimate the performance of our model, we carried out total classi<sup>fi</sup>cation tests on several well known datasets and report our <sup>fi</sup>ndings in Table 1, which shows the cpu time, the number of planes and the prediction error on a randomly generated testing set consisted of about 20% of the dataset. We used both the linear and the quadratic separating surface provided by the basis functions (11a) and (11b). We observed that this quadratic basis has a signi<sup>fi</sup>- cant impact on the medium size datasets and on the spiral dataset. Nonetheless, no conclusive statements should be drawn from these preliminary results.

(One run) performance. Errors in testing set, (hyper)planes and timing for total classi<sup>fi</sup>cation.

<table><tr><td rowspan="2">Dataset</td><td colspan="2">Size of</td><td rowspan="2">Separation</td><td rowspan="2">Errors %</td><td rowspan="2">Planes</td><td rowspan="2">Time sec.</td></tr><tr><td>Training</td><td>Testing</td></tr><tr><td rowspan="2">Abalone (0-8 rings)</td><td>3342</td><td>835</td><td>Linear</td><td>20.96</td><td>171</td><td>187.04</td></tr><tr><td></td><td></td><td>Quadratic</td><td>15.69</td><td>82</td><td>114.10</td></tr><tr><td rowspan="2">Bank</td><td>80</td><td>20</td><td>Linear</td><td>35.00</td><td>3</td><td>0.05</td></tr><tr><td></td><td></td><td>Quadratic</td><td>40.00</td><td>1</td><td>0.04</td></tr><tr><td rowspan="2">Cancer</td><td>548</td><td>135</td><td>Linear</td><td>8.89</td><td>5</td><td>0.43</td></tr><tr><td></td><td></td><td>Quadratic</td><td>11.11</td><td>2</td><td>0.38</td></tr><tr><td rowspan="2">Contraceptive</td><td>1180</td><td>293</td><td>Linear</td><td>0.68</td><td>3</td><td>0.75</td></tr><tr><td></td><td></td><td>Quadratic</td><td>1.71</td><td>4</td><td>1.44</td></tr><tr><td rowspan="2">Credit</td><td>527</td><td>131</td><td>Linear</td><td>35.12</td><td>8</td><td>0.90</td></tr><tr><td></td><td></td><td>Quadratic</td><td>35.12</td><td>7</td><td>1.63</td></tr><tr><td rowspan="2">Diabetes</td><td>314</td><td>78</td><td>Linear</td><td>0.00</td><td>1</td><td>0.20</td></tr><tr><td></td><td></td><td> $Quadratic^a$ </td><td>23.08</td><td>6</td><td>0.88</td></tr><tr><td rowspan="2">Heart</td><td>238</td><td>59</td><td>Linear</td><td>16.95</td><td>4</td><td>0.23</td></tr><tr><td></td><td></td><td>Quadratic</td><td>25.42</td><td>3</td><td>0.40</td></tr><tr><td rowspan="2">Housing (21)</td><td>405</td><td>101</td><td>Linear</td><td>12.87</td><td>7</td><td>0.50</td></tr><tr><td></td><td></td><td>Quadratic</td><td>13.86</td><td>4</td><td>0.94</td></tr><tr><td rowspan="2">Ionosphere</td><td>281</td><td>70</td><td>Linear</td><td>17.14</td><td>3</td><td>0.60</td></tr><tr><td></td><td></td><td>Quadratic</td><td>21.43</td><td>1</td><td>0.81</td></tr><tr><td rowspan="2">Letter (G)</td><td>4159</td><td>1039</td><td>Linear</td><td>2.60</td><td>14</td><td>58.65</td></tr><tr><td></td><td></td><td>Quadratic</td><td>2.79</td><td>6</td><td>30.77</td></tr><tr><td rowspan="2"> $Sonar^b$ </td><td>166</td><td>41</td><td>Linear</td><td>53.66</td><td>1</td><td>12.20</td></tr><tr><td></td><td></td><td>Quadratic</td><td>58.54</td><td>1</td><td>6.62</td></tr><tr><td rowspan="2">Spiral</td><td>308</td><td>76</td><td>Linear</td><td>72.37</td><td>83</td><td>4.62</td></tr><tr><td></td><td></td><td>Quadratic</td><td>71.05</td><td>11</td><td>0.47</td></tr><tr><td rowspan="2">Wine (≥7)</td><td>3919</td><td>979</td><td>Linear</td><td>21.55</td><td>131</td><td>285.44</td></tr><tr><td></td><td></td><td>Quadratic</td><td>20.12</td><td>76</td><td>284.51</td></tr></table>

<sup>a</sup> This result can only be explained by roundoff errors.  
<sup>b</sup> clp failed with quadratic separation. We used MatLab linprog.

## 5.2. The double spiral

The <sup>fi</sup>rst illustrative example is the spiral dataset (Fig. 8(a)). It consists of 192 members of and 192 members of . Fung and <sup>P N</sup>Mangasarian [11, Section 4] assert that this dataset gives FFNNs severe problems and it is not straightforward to specify the number of hyperplanes (neurons) necessary for complete classi<sup>fi</sup>cation, which is obtained by our algorithm with 108 linear hyperplanes. We should mention that at some iterations it was not possible to obtain a plane classifying individuals on one side of the plane, while forcing all individuals to stay on the other side (see Fig. 8(b)).

When we use the basis functions (11a) and (11b) the algorithm's performance improved notably. No empty was detected at any iteration and complete classi<sup>fi</sup>cation was obtained with only 13 (nonlinear) hyperplanes.

## 5.3. Bank dataset

As a second example we picked the Japanese Bank dataset provided by Glen [15, Table 1]. It has 50 individuals in each class and 7 features. Some multivariate statistics are provided by the same researcher [15, Tables 2–3]. Better et al. [4, Section 4] assert that only 3 linear hyperplanes are required for total classi<sup>fi</sup>cation. Our algorithm needed from 3 to 5 linear hyperplanes in 5 runs, while the MILP models given in [4,15] gave the expected theoretical number of hyperplanes.

It must be mentioned that the MILP models include the number of hyperplanes as a known parameter within its formulation. Our approach generates sequentially the hyperplanes and needs no previous information about the exact number of hyperplanes to obtain total classi<sup>fi</sup>cation.

Performance with 5 runs on random testing set. Errors on testing set and total number of hyperplanes at a given accuracy.

<table><tr><td rowspan="2">Dataset</td><td colspan="2">Size of</td><td rowspan="2">Accuracy %</td><td rowspan="2">Separation</td><td colspan="2">Range of</td></tr><tr><td>Train</td><td>Test</td><td>Errors %</td><td>Hyperplanes</td></tr><tr><td rowspan="10">Abalone (0-8 rings)</td><td>3342</td><td>835</td><td>60</td><td>Linear</td><td>25.63-29.10</td><td>4-5</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>24.07-27.90</td><td>6-7</td></tr><tr><td></td><td></td><td>70</td><td>Linear</td><td>25.63-27.66</td><td>4-5</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>23.95-27.42</td><td>6-9</td></tr><tr><td></td><td></td><td>80</td><td>Linear</td><td>23.23-25.87</td><td>31-48</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>21.32-23.23</td><td>11-24</td></tr><tr><td></td><td></td><td>90</td><td>Linear</td><td>21.20-23.71</td><td>81-100</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>18.80-23.59</td><td>53-76</td></tr><tr><td></td><td></td><td>100</td><td>Linear</td><td>19.16-21.80</td><td>156-172</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>19.28-23.71</td><td>82-105</td></tr><tr><td rowspan="10">Letter (letter G)</td><td>4159</td><td>1039</td><td>60</td><td>Linear</td><td>22.81-30.41</td><td>1-1</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>11.07-12.42</td><td>1-1</td></tr><tr><td></td><td></td><td>70</td><td>Linear</td><td>25.70-27.72</td><td>1-1</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>10.97-15.01</td><td>1-1</td></tr><tr><td></td><td></td><td>80</td><td>Linear</td><td>15.98-18.29</td><td>2-2</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>10.01-15.11</td><td>1-1</td></tr><tr><td></td><td></td><td>90</td><td>Linear</td><td>7.41-9.91</td><td>3-4</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>6.35-8.37</td><td>2-2</td></tr><tr><td></td><td></td><td>100</td><td>Linear</td><td>2.31-3.56</td><td>11-15</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>2.60-3.37</td><td>6-7</td></tr><tr><td rowspan="10">Wine (≥7)</td><td>3919</td><td>979</td><td>60</td><td>Linear</td><td>21.25-22.17</td><td>4-6</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>21.45-41.68</td><td>10-22</td></tr><tr><td></td><td></td><td>70</td><td>Linear</td><td>21.04-22.06</td><td>4-6</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>21.35-22.17</td><td>14-24</td></tr><tr><td></td><td></td><td>80</td><td>Linear</td><td>21.04-21.96</td><td>9-14</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>20.38-23.49</td><td>14-21</td></tr><tr><td></td><td></td><td>90</td><td>Linear</td><td>18.28-21.53</td><td>66-77</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>20.23-21.45</td><td>53-75</td></tr><tr><td></td><td></td><td>100</td><td>Linear</td><td>16.85-19.92</td><td>129-148</td></tr><tr><td></td><td></td><td></td><td>Quad</td><td>14.91-17.67</td><td>72-93</td></tr></table>

We also tried the prediction ability of our algorithm by randomly selecting 20 individuals for the testing set. In 5 runs, total classi<sup>fi</sup>cation of the training set was obtained with 3 to 5 hyperplanes with a range from 2 to 9 individuals misclassi<sup>fi</sup>ed with an average around 4.0. With basis (1) the algorithm needed 2 to 3 quadratics with 3 to 7 misclassi<sup>fi</sup>ed individuals.

## 5.4. Letter dataset

This dataset has 20,000 samples with 17 features. We arbitrarily de<sup>fi</sup>ne as the set of all samples that represented the G letter, and de-<sup>fi</sup>ne as the rest of the samples. The clp code gave us an out of memory message when the solution of model (9a) was attempted with more than 4000 constraints. We took the <sup>fi</sup>rst 4200 samples of the “letter” dataset and Tables 1 and 2 report the results obtained. We decided to repeat the experiment for the whole dataset with 16,000 elements for the training set and 4000 elements for the testing set. We impose the additional condition ≤4000 to avoid the annoying out <sup>j jX</sup>of memory message. The algorithm runs smoothly and in 151.57 s obtained total classi<sup>fi</sup>cation on the training set with 63 linear hyperplanes and 3.23% errors on the testing set.

## 5.5. Synthetic data sets

To con<sup>fi</sup>rm the importance of Proposition 1 we randomly generate 40 points for the set $\bar { \mathcal { P } } = \left\{ ( \xi , v ) : \left( \xi - 1 \right) ^ { 2 } + \left( v \overset { - } { \underset { - } { - } } 1 \right) ^ { 2 } \leq 4 \right\}$ and 35 points for the set $\mathcal { N } = \left\{ ( \xi , v ) : { ( \xi ^ { \downarrow } - 1 ) } ^ { 2 } + { ( v - 1 ) } ^ { 2 } > 4 \right\}$ <sup>Þ</sup>. We run the algorithm <sup>N ¼ ð Þ ð Þ þ ð Þ</sup>with the basis (11a) and show the result in Fig. 5. It is worth pointing out that the algorithm can generate disjoint spheres.

To study the effect of noise, we also test our algorithm with a synthetic data that was randomly perturbed. We used the separating surface suggested by [8]

$$
f (x) = 1 0 \sin \left(\pi x ^ {1} x ^ {2}\right) + 2 0 \left(x ^ {3} - 0. 5\right) ^ {2} + 1 0 x ^ {4} + 5 x ^ {5} - 1 3,\tag{15}
$$

and generate 1024 random points in ${ \mathsf { C } } = [ 0 1 ] ^ { 5 }$ . We assign c(x) = 1 if $f ( x ) > 0 ;$ otherwise $c ( x ) = - 1$ . Table 3 shows the results of our algorithm with this data, and also includes the test on a corrupted data

$$
y _ {i} ^ {k} = x _ {i} ^ {k} + 0. 1 r _ {i} ^ {k}, i = 1, \dots , 1 0 2 4; k = 1, \dots , 5,
$$

5-fold validation on synthetic data with known separating function (15) (pure and corrupted by Gaussian noise). % errors in training set (820), % testing set (204), (hyper) planes and timing.

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">Separation</td><td colspan="4">Range of</td></tr><tr><td>Train errors</td><td>Test errors</td><td>Planes</td><td>Time</td></tr><tr><td colspan="6">Our algorithm</td></tr><tr><td rowspan="3">Pure</td><td>Linear</td><td></td><td>9.31-17.15</td><td>26-35</td><td>1.10-2.00</td></tr><tr><td>Basis (11a)</td><td></td><td>10.3-14.70</td><td>16-24</td><td>0.97-1.30</td></tr><tr><td>Basis (11b)</td><td></td><td>2.45-6.86</td><td>4-6</td><td>0.68-0.80</td></tr><tr><td rowspan="3">Corrupted (σ=0.1)</td><td>Linear</td><td></td><td>17.18-27.61</td><td>33-38</td><td>1.25-1.43</td></tr><tr><td>Basis (11a)</td><td></td><td>28.46-31.05</td><td>26-32</td><td>1.10-1.35</td></tr><tr><td>Basis (11b)</td><td></td><td>13.50-20.86</td><td>16-19</td><td>0.81-0.93</td></tr><tr><td colspan="6">Our SVM (16)</td></tr><tr><td rowspan="3">Pure</td><td>Linear</td><td>12.68-14.02</td><td>10.29-16.67</td><td></td><td>0.43-0.85</td></tr><tr><td>Basis (11a)</td><td>12.93-14.15</td><td>11.77-17.16</td><td></td><td>0.43-0.62</td></tr><tr><td>Basis (11b)</td><td>3.42-4.39</td><td>3.92-6.37</td><td></td><td>1.45-2.75</td></tr><tr><td rowspan="3">Corrupted (σ=0.1)</td><td>Linear</td><td>15.37-18.11</td><td>13.50-22.01</td><td></td><td>0.28-0.47</td></tr><tr><td>Basis (11a)</td><td>15.22-17.96</td><td>13.50-22.70</td><td></td><td>0.31-0.38</td></tr><tr><td>Basis (11b)</td><td>10.50-13.24</td><td>10.43-19.02</td><td></td><td>0.87-1.02</td></tr></table>

where r<sup>k</sup> are random numbers with a normal distribution of 0 mean and variance $\sigma = 1$

The results were compared with the SVM (16) for both data sets. This particular test favors basis (11a) and (11b) over the linear separability. The predicting ability for both machines is alike, but ours does not generate any training errors. We observe from this example that our algorithm was sensitive to unbounded noise, because it makes harder to enclose all members of the set , as required by our algorithm. Better results are obtained with small amplitude noise.

## 5.6. Accuracy and generalization

Table 2 shows the testing errors on a sample of 20% of a dataset, and the number of hyperplanes needed to reach a given training accuracy on medium size datasets. We selected well known datasets from the Irvine repository and report our results on abalone (0–8 rings), letter (G), and wine $( \geq 7 )$ . The trend is to obtain a better training accuracy as we increase the number of hyperplanes, for both linear and quadratic separation. Fig. 9b shows that this is a non monotone behavior. Note that at the end of any iteration, only those individuals in ∩ are misclassi<sup>fi</sup>ed, while all individuals in are well classi<sup>fi</sup>ed.

The algorithm performance is rather remarkable: the number of errors detected on the testing set (20% of the dataset) always stays within tolerable values. In many cases, the prediction ability improved as the accuracy in the training set improved (Fig. 9). It is not obvious how to explain this behavior; but we noticed that a signi<sup>fi</sup>cant number of prediction errors is detected at early algorithm's iterations. We also show that – on some rare occasions – the algorithm does not report 100% accuracy with total classi<sup>fi</sup>cation. Fig. 9b shows a 9.26% training error on the wine dataset with quadratic separation; however, no misclassi<sup>fi</sup>ed elements are reported $\mathrm { { \bar { f } o r } } = 1 0 ^ { - 6 }$ in the de<sup>fi</sup>nition of in Fig. 4. With these results we did not consider early stopping.

## 5.7. Comparison with SVM on real data sets

We carried out some tests on small and medium size datasets from the Irvine repository [9], and compare the algorithm's performance with the version of SVM modeled by (16). This SVM is essentially model (6), with $w = v - z , \nu , z \geq 0$ and the additional constraint $| \nu ^ { T } e - $ $z ^ { T } e | \geq 1$ , where e is a vector of ones. This constraint is equivalent to $| w ^ { T } e | \geq 1$ and rules out the trivial solution $w = ~ 0 .$ . It may be implemented with 2 LP models as suggested for model (9a). With this model the value of τ was not signi<sup>fi</sup>cant for the SVM performance.

$$
\begin{array}{ll}\underset { \begin{array}{c}v\in R^{q},z\in R^{q}\\ \theta \in R,y\in R^{\mathcal{T}} \end{array} }{min} & \tau \sum_{k = 1}^{q}\Big(v^{k} + z^{k}\Big) + (1 - \tau)\sum_{x_{k}\in \mathcal{T}}y^{k}\\ & c^{k}\Big((v - z)^{T}g(x_{k}) - \theta \Big) + y^{k}\geq 1,x_{k}\in \mathcal{T}\\ & \left|v^{T}e - z^{T}e\right|\geq 1,(v,z,y)\geq 0 \end{array}\tag{16}
$$

We compare SVM (16) with one iteration of our algorithm – generating only one plane – and with the full version of the algorithm – total classi<sup>fi</sup>cation of the training set. We performed a 5-fold validation experiment. The dataset was split in 5 samples of equal size. One of the samples was taken as the testing set, while the rest was used as the training set. Table 4 shows the results for 5 different runs with linear separation. The <sup>fi</sup>rst row represents the average on 5 runs, and the min-max in the second row represent, respectively, the minimum and the maximum value obtained for each instance.

In average our algorithm gives a lower testing error in 8 of the 13 datasets used in our experiment. Moreover, as our algorithm has no training error, the results for the other 5 datasets are highly competitive. We also point out that the one plane version of our algorithm was better than the SVM on 4 datasets.

![](/api/attachments/2KHNHF6W/fulltext/images/d5749954baea98098550a5000cbb4793fe5615d2c9b8f661676173150744568d.jpg)

![](/api/attachments/2KHNHF6W/fulltext/images/d5d3f9925c53f9f6cf74d7efa40c60e6326680b38e46cca1311c4cde88561465.jpg)

![](/api/attachments/2KHNHF6W/fulltext/images/6599d66f43a7e28e0a9bfb7aca25eb6ec3de51f9aabe91ac94ea2e65d839c470.jpg)  
a) Algorithm precision on medium datasets. Testing set = 20% of dataset.

![](/api/attachments/2KHNHF6W/fulltext/images/5b1d27bff2e15f4b129f037e761d72868f255d670ca32644fc7d78f74fef2e5f.jpg)  
b) Non monotone behavior of prediction. Wine dataset with quadratic separation.  
Fig. 9. Algorithm behavior.

Table 4  
(5-Fold) error analysis for the SVM (16) and for our algorithm.

<table><tr><td rowspan="6">Dataset</td><td colspan="5">Error percentage with linear separation</td></tr><tr><td colspan="5">Average</td></tr><tr><td colspan="5">Min-max</td></tr><tr><td>SVM (16)</td><td></td><td colspan="2">Our algorithm</td><td>0% train</td></tr><tr><td></td><td></td><td colspan="2">One plane</td><td></td></tr><tr><td>Train</td><td>Test</td><td>Train</td><td>Test</td><td>Test</td></tr><tr><td rowspan="2">Abalone(0-8 rings)</td><td>15.85</td><td>16.12</td><td>55.65</td><td>55.38</td><td>22.20</td></tr><tr><td>15.44-16.25</td><td>14.13-18.44</td><td>54.43-58.05</td><td>53.17-57.73</td><td>20.96-23.11</td></tr><tr><td rowspan="2">Bank</td><td>11.25</td><td>25.00</td><td>10.75</td><td>22.00</td><td>23.00</td></tr><tr><td>8.75-13.75</td><td>15.00-35.00</td><td>5.00-15.00</td><td>5.00-35.00</td><td>5.00-35.00</td></tr><tr><td rowspan="2">Cancer</td><td>2.56</td><td>3.26</td><td>2.01</td><td>3.11</td><td>4.30</td></tr><tr><td>1.46-3.10</td><td>1.48-5.19</td><td>1.46-2.37</td><td>1.48-5.92</td><td>1.48-8.89</td></tr><tr><td rowspan="2">Contracep.</td><td>31.36</td><td>32.29</td><td>2.37</td><td>2.39</td><td>0.89</td></tr><tr><td>30.73-32.03</td><td>29.69-36.52</td><td>2.20-2.63</td><td>1.37-3.07</td><td>0.00-2.05</td></tr><tr><td rowspan="2">Credit</td><td>13.44</td><td>13.28</td><td>9.03</td><td>14.81</td><td>9.31</td></tr><tr><td>7.78-16.51</td><td>0.76-35.88</td><td>0.00-24.29</td><td>0.00-42.75</td><td>0.00-35.11</td></tr><tr><td rowspan="2">Diabetes</td><td>20.38</td><td>21.54</td><td>No errors</td><td></td><td></td></tr><tr><td>18.47-21.34</td><td>15.39-24.36</td><td></td><td></td><td></td></tr><tr><td rowspan="2">Heart</td><td>13.87</td><td>22.71</td><td>19.66</td><td>31.53</td><td>19.32</td></tr><tr><td>11.77-15.97</td><td>11.86-40.68</td><td>13.03-23.95</td><td>22.03-49.15</td><td>5.09-33.90</td></tr><tr><td rowspan="2">Housing(21K)</td><td>11.75</td><td>15.05</td><td>10.57</td><td>15.45</td><td>14.06</td></tr><tr><td>8.40-15.56</td><td>0.99-24.75</td><td>7.65-13.58</td><td>1.98-31.68</td><td>1.98-26.73</td></tr><tr><td rowspan="2">Ionosphere</td><td>3.56</td><td>14.00</td><td>3.84</td><td>17.14</td><td>16.57</td></tr><tr><td>2.14-6.05</td><td>8.57-22.86</td><td>1.07-7.47</td><td>10.00-27.14</td><td>10.00-27.14</td></tr><tr><td rowspan="2">Letter(G)</td><td>3.84</td><td>3.79</td><td>25.73</td><td>26.30</td><td>2.95</td></tr><tr><td>3.82-3.87</td><td>3.75-3.85</td><td>23.92-27.36</td><td>23.87-28.39</td><td>2.60-3.66</td></tr><tr><td rowspan="2">Sonar</td><td>1.08</td><td>33.17</td><td>0.72</td><td>36.59</td><td>36.59</td></tr><tr><td>0.00-3.61</td><td>21.95-51.22</td><td>0.00-2.41</td><td>24.39-53.66</td><td>24.39-53.66</td></tr><tr><td rowspan="2">Spiral</td><td>42.34</td><td>81.05</td><td>45.00</td><td>56.84</td><td>64.47</td></tr><tr><td>41.56-43.51</td><td>76.32-84.21</td><td>39.61-47.08</td><td>50.00-67.11</td><td>47.37-75.00</td></tr><tr><td rowspan="2">Wine(≥0.7)</td><td>21.64</td><td>21.66</td><td>67.11</td><td>67.01</td><td>25.54</td></tr><tr><td>21.64-21.64</td><td>21.66-21.66</td><td>65.25-69.07</td><td>53.73-73.85</td><td>21.55-30.34</td></tr></table>

## 6. Final remarks

We propose a classi<sup>fi</sup>cation algorithm that uses LP models to generate a non linear piecewise discriminating function that completely separates members of two different classes. It can achieve any a priori accuracy stated by the practitioner and seems more practical than previous approaches with the same goal: standard ANN training with an unknown large number of neurons, SVMs with – a proper – kernel, AdaBoost and Boosting algorithms with heuristic strategies [32], MSM with two hyperplanes per iteration and classi<sup>fi</sup>cation trees linked to MSMs. As a byproduct we found that the outcome of the algorithm is equivalent to a FFNN; so we can assert that we have developed a new training algorithm for FFNNs that does not involve the optimization of non convex functions. The training is obtained by an iterative solution of linear programming models, the most conspicuous tool in operations research.

Our algorithm is iterative and the training accuracy improves up to any level imposed by the user, provided there are no individuals belonging to both classes. Numerical examples show a remarkable property of the algorithm: in most experiments carried out, the number of errors measured on a randomly chosen testing set did not deteriorate. A numerical comparison was carried out with a version of SVM suggested in this paper. The results show that the total classi<sup>fi</sup>cation algorithm is highly competitive.

This paper hints on algorithm variants that have not been implemented; mainly the decomposition scheme and parallelism for classifying large datasets. This is a road open to research. Also, it seems plausible to generalize the algorithm to multi classi<sup>fi</sup>cation and we have started efforts in this direction.

There are several issues that are still unresolved: Actually, it is not clear how to compensate for the roundoff errors that cause anomalous results, like failure of LP software, less than 100% accuracy at termination, and no qualifying individuals at some iterations, which is an undesirable situation. A quadratic separating surface theoretically overcomes the latter incident and made the algorithm run until <sup>fi</sup>nal classi<sup>fi</sup>cation on all reported datasets. However, we do not know the real effect that this arti<sup>fi</sup>ce will have on large data sets.

## Acknowledgments

The authors are indebted to anonymous referees, who offered advices that improved the quality of this paper.

## References

[1] M. Anthony, P. Barlett, Neural Network Learning, Cambridge University Press, 1999.

[2] K.P. Bennett, E.J. Bredensteiner, Geometry in learning, in: C.A. Gorini (Ed.), Geometry at work: a collection of papers showing applications of geometry, Mathemat ical Association of America, 2000, pp. 132–145.

[3] K.P. Bennett, E. Parrado-Hernández, The interplay of optimization and machine learning research, Journal of Machine Learning Research 7 (2006) 1265–1281.

[4] M. Better, F. Glover, M. Samorani, Classi<sup>fi</sup>cation by vertical cand cutting multihyperplane decision tree induction, Decision Support Systems 48 (2010) 430–436.

[5] J. Bi, S. Periaswamy, K. Okada, T. Kubota, G. Fung, M. Salganicoff, B. Rao, Computer aided detection via asymmetric cascade of sparse hyperplane classi<sup>fi</sup>ers, in: Proceedings of the 12th ACM SIGKDO international conference on knowledge discovery and data mining. DOI 10.1145/1150402.1150518, Philadelphia, PA, 2006, pp. 837–844.

[6] P. Bradley, O.L. Mangasarian, Feature selection via concave minimization and support vector machines, in: J. Shavlik (Ed.), Proc. of the Fifteenth International Conference (ICML 98), Morgan Kaufmann, 1998, pp. 82–90

[7] A. Cassioli, D. Di Lorenzo, M. Locatelli, F. Schoen, M. Sciandrone, Machine learning for global optimization, Technical Report, Optimization on Line, 2009.

[8] V. Cherkassky, Y. Ma, Practical selection of SVM parameters and noise estimation for SVM regression, Neural Networks 17 (2004) 113–126.

[9] A. Frank, A. Asuncion, UCI Machine Learning Repository, 2010 http://archive.ics. uci.edu/ml.

[10] N. Freed, F. Glover, Evaluating alternative linear programming models to solve the two-group discriminant problem, Decision Sciences 17 (1986) 151–162.

[11] G. Fung, O.L. Mangasarian, Proximal support vector machine classi<sup>fi</sup>ers, in: F. Provost, R. Srikant (Eds.), Proc. Knowledge Discovery and Data Mining, MIT Press, 2001, pp. 77–86.

[12] G. Fung, O.L. Mangasarian, A.J. Smola, Minimal kernel classi<sup>fi</sup>ers, Journal of Machine Learning Research 3 (2002) 303–321.

[13] G. Fung, O.L. Mangasarian, J. Shavlik, Knowledge-based support vector machine classi<sup>fi</sup>ers, in: B., et al., (Eds.), Advances in Neural Information Processing Systems, MIT Press, 2003, pp. 521–528

[14] J.J. Glen, An iterative mixed integer programming method for classi<sup>fi</sup>cation accuracy maximizing discriminant analysis, Computers and Operations Research 30 (2003) 181–198.

[15] J.J. Glen, Mathematical programming models for piecewise-linear discriminant analysis, Journal of the Operational Research Society 56 (2005) 331–341.

[16] F. Glover, S. Keene, B. Duea, A new class of models for the discriminant problem, Decision Sciences 19 (1988) 269–280.

[17] M.H. Hassoun, Fundamentals of Arti<sup>fi</sup>cial Neural Networks, The MIT press, 1995.

[19] K. Hornik, M. Stinchcombe, H.H. White, Multilayer feedforward networks are universal approximations. Neural Networks 2 (1989) 359–366

[20] S. Keerthi, O. Chapelle, D. DeCoste, Building support vector machines with reduced classi<sup>fi</sup>er complexity, Journal of Machine Learning Research 7 (2006) 1493–1515.

[21] K. Kim, H.S. Ryoo, Data separation via a <sup>fi</sup>nite number of discriminant functions: a global optimization approach, Applied Mathematics and Computation 190 (2007) 476–489.

[22] K. Kim, H.S. Ryoo, Nonlinear separation of data via mixed 0–1 integer and linear programming, Applied Mathematics and Computation 193 (2007) 183–196.

[23] G. Koehler, Improper linear discriminant classi<sup>fi</sup>ers, European Journal of Operational Research 50 (1991) 188–198.

[24] Y. Lin, Support vector machines and the Bayes rule in classi<sup>fi</sup>cation, Data Mining and Knowledge Discovery 6 (2002) 259–275.

[25] X. Liu, F.A. Potra, Pattern separation and prediction via linear and semide<sup>fi</sup>nite programming, Studies in Informatics and Control 18 (2009) 71–82.

[26] O.L. Mangasarian, Multisurface method of pattern separation, IEEE Transactions on Information Theory IT 14 (1968) 801–807.

[27] O.L. Mangasarian, Mathematical programming in neural networks, Journal on Computing 5 (1993) 349–360.

[28] O.L. Mangasarian, W. Wild, Multisurface proximal support vector machine classi-<sup>fi</sup>cation via generalized eigenvalues, IEEE Transactions on Pattern Analysis and Machine Intelligence 28 (2006) 69–74.

[29] O.L. Mangasarian, R. Setiono, W. Wolberg, Pattern recognition via linear programming: Theory and applications in medical diagnosis, in: Proceedings of the Workshop on Large-Scale Numerical Optimization, pp. 22–31.

[30] O.G. Manzanilla Métodos multi-superficie para construir clasificadores binarios con optimización matemática Master's thesis, Universidad Simón Bolívar, 2005

[31] O.G. Manzanilla, U.M. García Palomares, Links between multisurface methods and arti<sup>fi</sup>cial neural networks for classi<sup>fi</sup>cation problems, Revista de la Facultad de Ingeniería, Universidad Central de Venezuela (submitted for publication).

[32] R. Meir, G. Ratsch, An introduction to boosting and leveraging, in: S. Mendelson, A. Smola (Eds.), Advanced Lectures on Machine Learning, Springer Verlag, 2003, pp. 118–183.

[33] H. Nakayama, Y.B. Yun, T. Asada, M. Yoon, Mop/gp models for machine learning, European Journal of Operational Research 166 (2005) 756–768.

[34] A.R. Omondi, J.C. Rajapakse (Eds.), FPGA Implementations of Neural Networks, Springer, 2006, 10 0-387-28485-0.

[35] C.J. Ong, S.Y. Shao, J.B. Yang, An improved algorithm for the solution of the entire regulation path of support vector machine, Technical Report, Optimization on line, Argonne, IL, 2009 http://www.optimization-online.org/DB\_HTML/2009/04 2284.html.

[36] W.S. Sarle, Stopped training and other remedies for over<sup>fi</sup>tting, in: Proceedings of the 27th Symposium on the Interface of Computing Science and Statistics pp. 352–360

[37] J. Shawe-Taylor, N. Cristianini, On the generalization of soft margin algorithms, IEEE Transactions on Information Theory 48 (2002) 2721–2735.

[38] S. Smaoui, H. Chabchoub, B. Aouni, Mathematical programming approaches to classi<sup>fi</sup>cation problems, Advances in Operations Research 34 (2009)

[39] T. Szabó, G. Horváth, An ef<sup>fi</sup>cient hardware implementation of feed-forward neural networks, Applied Intelligence 21 (2004) 143–158

[41] V.N. Vapnik, The Nature of Statistical Learning Theory, 2nd print edition Springer Verlag0-387-94559-8. 1998

[40] T. Tr tscher, Linear mixed integer program solver, , 2009.

[42] V.N. Vapnik, S. Golowich, A.J. Smola, Support vector method for function approximation, regression estimation, and signal processing, in: M. Mozer, M. Jordan, T. Petsche (Eds.), Advances in Neural Information Processing Systems, MIT press, Cambridge, MA, 1997, pp. 281–287.

[43] A.R. Waleed, A.A. Hamza, Cooperative neural network generalization model incorporating classi<sup>fi</sup>cation and association, European Journal of Scienti<sup>fi</sup>c Research 36 (2009) 639–648.

[44] Q. Wu, D. Zhou, SVM soft margin classi<sup>fi</sup>ers: linear programming versus quadratic programming, Neural Computation 17 (2005) 1160–1187.

[45] H. Zou, M. Yuan, The F -norm support vector machine, Statistica Sinica (2008) 379–398.

Prof. Ubaldo M. Garcia Palomares is an Electrical Engineer who graduated in 1968, with Ms.Sc. and Ph.D. from the University of Wisconsin, Madison. His area of interest is the design of algorithms for solving optimization models. He has written over 40 papers and actually works on derivative free methods and linear discriminant for classi<sup>fi</sup>cation problems.

Prof. Orestes Manzanilla Salazar is a Production Engineer from Universidad Simón Bolívar (2002) and Magister in System Engineering at the same University. His present line of research is the use of Operations Research tools in Data Mining and he teaches Linear Programming and Decision taking.
