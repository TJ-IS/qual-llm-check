---
otero_id: 13668
otero_key: "ND6GD7KB"
title: "Answering queries in hybrid Bayesian networks using importance sampling"
authors: "Antonio Fernández; Rafael Rumí; Antonio Salmerón"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.03.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Answering queries in hybrid Bayesian networks using importance sampling

Antonio Fernández ⁎, Rafael Rumí, Antonio Salmerón

Dept. Statistics and Applied Mathematics, University of Almería, La Cañada de San Urbano s/n, 04120 Almería, Spain

## a r t i c l e i n f o

Article history: Received 25 February 2011 Received in revised form 1 February 2012 Accepted 24 March 2012 Available online 3 April 2012

2000 MSC: 6505 68T37

## a b s t r a c t

In this paper we propose an algorithm for answering queries in hybrid Bayesian networks where the underlying probability distribution is of class MTE (mixture of truncated exponentials). The algorithm is based on importance sampling simulation. We show how, like existing importance sampling algorithms for discrete networks, it is able to provide answers to multiple queries simultaneously using a single sample. The behaviour of the new algorithm is experimentally tested and compared with previous methods existing in the literature. © 2012 Elsevier B.V. All rights reserved.

Keywords: Bayesian networks Probabilistic reasoning Importance sampling Mixtures of truncated exponentials

## 1. Introduction

Bayesian networks [17,36] have become a popular tool for representing uncertainty in decision support systems. A review of recent literature shows the variety of applications in which they have been successfully used [1,10,24,35,45]. One of the main reasons for using them as the inference engine in a decision support system is that ef<sup>fi</sup>cient reasoning algorithms can be designed, taking advantage of their structure [2,3,16,44,43,30,29].

Most of the methodological development around Bayesian networks has concentrated on the case in which all the variables involved are qualitative or discrete. However, decision support systems usually have to operate in domains described in terms of both discrete and continuous variables simultaneously. In such scenarios, there is always the possibility of discretising the continuous variables [20,34], in order to be able to use methods designed for discrete variables. But such a solution in general conveys a loss of information.

Continuous and discrete variables can be handled simultaneously, with no need to discretise, in the so-called hybrid Bayesian networks. The <sup>fi</sup>rst advances in this <sup>fi</sup>eld came along with the de<sup>fi</sup>nition of the Conditional Gaussian (CG) model [25,26,28]. The limitations of this approach are the assumption of normality over the continuous variables, and also the fact that dependencies of discrete variables conditional on continuous ones, are not allowed. This structural restriction is overcome in the augmented Conditional Linear Gaussian (CLG) networks, where discrete nodes are allowed to have continuous parents, by representing their conditional distributions as softmax functions [27]. However this model also relies on the normality assumption. Furthermore, exact inference is not possible in augmented CLG networks, and the solution proposed in [27] is based on a Gaussian approximation of the product of the Gaussian and softmax functions, which provides exact marginals for the discrete variables and also is able to obtain exact values only for the <sup>fi</sup>rst and second order moments of the distribution of the continuous variables.

A more general proposal is based on the use of mixtures of truncated exponentials (MTEs), which do not impose any restriction and also do not rely on the normality assumption [31]. This model has been successfully applied to decision problems [6]. An important feature of MTEs is that they are compatible with ef<sup>fi</sup>cient exact inference algorithms like, for instance, the Shenoy–Shafer architecture [44] and the variable elimination scheme [49]. As MTEs are able to approximate a wide variety of probability distributions [7], they can be used as a general framework for carrying out inference in hybrid Bayesian networks, just by approximating each conditional distribution in the network by an MTE and then using an exact inference algorithm. This approach has been analysed in [22], by solving a network involving Logistic and Gaussian distributions using MTEs, variational approximations [18], discretisation [33] and Markov Chain Monte Carlo [12].

A recent approach, similar in essence to MTEs, is based on representing the distribution in a hybrid Bayesian network as a Mixture of Polynomials (MOPs) [42]. Both MTEs and MOPs have been generalised in a global framework for representing hybrid Bayesian networks, called Mixtures of Truncated Basis Functions (MoTBFs) [23]. However, even though MOPs have some advantages over MTEs, specially the ability of dealing with a wider class of deterministic relationships, so far they lack of an algorithm for learning the models from data, while this issue has been solved for MTEs [38]. Hence, MTEs can be used as an exact model and not only as an approximation of other distributions. In that sense, MTEs behave as a nonparametric model, where no assumption is made about the underlying distribution.

Even though Bayesian networks allow ef<sup>fi</sup>cient inference algorithms to operate over them, it is known that exact probabilistic inference is an NP-hard problem [8]. Furthermore, approximate probabilistic inference is also an NP-hard problem if a given precision is required [9]. For that reason, approximate algorithms that tradeoff complexity for accuracy have been developed for discrete Bayesian networks. An important class of such approximate algorithms is based on the importance sampling technique, that provides a <sup>fl</sup>exible approach to construct anytime reasoning algorithms [4,13,32,46–48].

Inference in hybrid Bayesian networks with MTEs does not escape from the above mentioned complexity. If the model is learnt from a database using the algorithm in [38], it can be too complex if the number of variables is high. But even using the approximations in [7], inference may become unfeasible if the model is complex enough.

With this motivation, in this paper we propose an approximate algorithm for computing fast and accurate answers to precise queries in hybrid Bayesian networks with MTEs. The algorithm is based on importance sampling, and therefore it is an anytime algorithm [37] in the sense that the accuracy of its results is proportional to the time it is allowed to use for computing the answer. We show how our proposal outperforms the previous state-of-the-art method for approximate inference with MTEs, introduced in [40].

The rest of the paper is organised as follows. We establish the notation and de<sup>fi</sup>ne some preliminary concepts in Section 2. The problem addressed here is formally posted in Section 3. The core of the methodological contributions is in Section 4, and the details of the algorithm can be found in Section 5. The experimental analysis carried out to test the performance of the algorithm is reported in Section 6. The concluding remarks are given in Section 7.

## 2. Notation and preliminaries

Formally, a Bayesian network is a directed acyclic graph where each node represents a random variable, and the topology of the graph encodes the independence relations among the variables, according to the d-separation criterion [36]. Given the independences attached to the graph, the joint distribution is determined giving a probability distribution for each node conditioned on its parents, so that for a Bayesian network with variables $X _ { 1 } , . . . , X _ { n }$ the joint distribution factorises as

$$
p (x _ {1}, \dots , x _ {n}) = \prod_ {i = 1} ^ {n} p (x _ {i} | p a (x _ {i})),\tag{1}
$$

where pa(x ) denotes the parents of variable $X _ { i }$ in the network.

We will use uppercase letters to denote random variables, and boldfaced uppercase letters to denote random vectors, ${ \mathrm { e . g . } } { \mathbf { X } } = \{ X _ { 1 } , . . . ,$ $X _ { n } \}$ , and its domain will be written as $\Omega _ { \mathbf { X } } .$ By lowercase letters x (or x) we denote some element of $\varOmega _ { X } \left( 0 \mathrm { r } \varOmega _ { \mathbf { X } } \right)$

We are interested in hybrid Bayesian networks, which are de<sup>fi</sup>ned for a set of variables X that contains discrete and continuous variables. Throughout this paper we will assume that X=Y∪Z, being Y and Z sets containing only discrete and only continuous variables respectively. We will follow the approach based on mixtures of truncated exponentials [31], in which all the conditional distributions in Eq. (1) are represented as MTE potentials, which are formally de<sup>fi</sup>ned as follows.

## De<sup>fi</sup>nition 1. MTE potential

Let X be a mixed n-dimensional random vector. Let $\mathbf { Y } = ( Y _ { 1 } , . . . , Y _ { d } ) ^ { T }$ and $\mathbf { Z } = ( Z _ { 1 } , . . . , Z _ { c } ) ^ { T }$ be the discrete and continuous parts of $\mathbf { X } ,$ respectively, with $c + d = n .$ . We say that a function $f : \varOmega \mathbf { x } ^ { \mapsto } \mathbb { R } _ { 0 } ^ { + }$ is a mixture of truncated exponentials (MTE) potential if for each <sup>fi</sup>xed value $\mathbf { y } \in \varOmega _ { \mathbf { Y } }$ of the discrete variables Y, the potential over the continuous variables Z is de<sup>fi</sup>ned as:

$$
f (\mathbf {z}) = a _ {0} + \sum_ {i = 1} ^ {m} a _ {i} e x p \left\{\mathbf {b} _ {i} ^ {T} \mathbf {z} \right\},\tag{2}
$$

for all $\mathbf { z } \in \varOmega _ { \mathbf { Z } } ,$ where $a _ { i } \in \mathbb { R }$ and $\mathbf { b } _ { i } { \in } \mathbb { R } ^ { c } , i { = } 1 , . . . , m$ . We also say that f is an MTE potential if there is a partition $D _ { 1 } , . . . , D _ { k }$ of $\Omega _ { \mathbf { Z } }$ into hypercubes and in each one of them, f is de<sup>fi</sup>ned as in Eq. (2). An MTE potential is an MTE density if it integrates to 1.

A conditional MTE density can be speci<sup>fi</sup>ed by dividing the domain of the conditioning variables and specifying an MTE density for the conditioned variable for each con<sup>fi</sup>guration of splits of the conditioning variables. The next is an example of a conditional MTE density.

$$
f (y | x) = \left\{ \begin{array}{l l} 1. 2 6 - 1. 1 5 e ^ {0. 0 0 6 y} & \text { if } 0. 4 \leq x <   5,   0 \leq y <   1 3, \\ 1. 1 8 - 1. 1 6 e ^ {0. 0 0 0 2 y} & \text { if } 0. 4 \leq x <   5,   1 3 \leq y <   4 3, \\ 0. 0 7 - 0. 0 3 e ^ {- 0. 4 y} + 0. 0 0 0 1 e ^ {0. 0 0 0 4 y} & \text { if } 5 \leq x <   1 9,   0 \leq y <   5, \\ - 0. 9 9 + 1. 0 3 e ^ {0. 0 0 1 y} & \text { if } 5 \leq x <   1 9,   5 \leq y <   4 3. \end{array} \right.
$$

Since MTEs are de<sup>fi</sup>ned into hypercubes, they admit a treestructured representation in a natural way. Each entire branch in the tree determines one hypercube where the potential is de<sup>fi</sup>ned, and the function stored in the leaf of a branch is the de<sup>fi</sup>nition of the potential on it. An example of a tree-structured representation of an MTE potential is shown in Fig. 1.

We use the term mixed tree [31] to refer to a tree-structure representation of an MTE potential. A tree is a mixed tree if: (i) every <sup>T</sup>internal node represents a random variable, (ii) every arc outgoing from a continuous variable Z is labelled with an interval of values of Z, so that the domain of Z is the union of the intervals corresponding to the arcs Z-outgoing, (iii) every discrete variable has a number of outgoing arcs equal to its number of states and (iv) each leaf node contains an MTE potential de<sup>fi</sup>ned on variables in the path from the root to that leaf.

## 3. Problem formulation

The goal of this paper is to introduce a method for answering queries in hybrid Bayesian networks with MTEs. We consider a hybrid Bayesian network de<sup>fi</sup>ned for a set of variables X. A query is a question about a probability value for a target variable W X given that the values of some variables E⊂X are known. Thus, if we write $\mathbf { X } = ( W , \mathbf { Y } ^ { T } , \mathbf { Z } ^ { T } , \mathbf { E } ^ { T } ) ^ { T }$ where $\mathbf { Y } = ( Y _ { 1 } , . . . , Y _ { d } ) ^ { T }$ represents the non-observed discrete variables and $\mathbf { Z } = ( Z _ { 1 } , . . . , Z _ { c } ) ^ { T }$ represents the non-observed continuous variables and $\mathbf { E } { = } ( E _ { 1 } , . . . , E _ { k } ) ^ { T }$ , then a query about W given that E=e is

$$
P (a <   W <   b | \mathbf {E} = \mathbf {e}) = \frac {\int_ {a} ^ {b} \left(\sum_ {\mathbf {y} \in \mathbf {Y}} \int_ {\Omega_ {\mathbf {Z}}} \phi (w , \mathbf {y} , \mathbf {z} , \mathbf {e}) d \mathbf {z}\right) d w}{\phi_ {\mathbf {E}} (\mathbf {e})}\tag{3}
$$

if W is a continuous variable. The function ϕ in Eq. (3) is the joint distribution in the network and $\phi _ { \mathbf { E } }$ is its marginal over variablesE. Let ϕ denote the conditional distribution of any variable X in the network. Then, the joint distribution is de<sup>fi</sup>ned as

$$
\begin{array}{l} \phi (w, \mathbf {y}, \mathbf {z}, \mathbf {e}) = \\ \phi_ {W} (w | p a (w)) \prod_ {i = 1} ^ {d} \phi_ {Y _ {i}} (y _ {i} | p a (y _ {i})) \prod_ {j = 1} ^ {c} \phi_ {Z _ {j}} \Big (z _ {j} | p a \Big (z _ {j} \Big) \Big) \prod_ {l = 1} ^ {k} \phi_ {E _ {l}} (e _ {l} | p a (e _ {l})). \end{array}\tag{4}
$$

Since our goal is to answer a query given a <sup>fi</sup>xed value e of variables E, we will rather be interested in the restriction of the joint distribution to the knowledge that E e. We will replace any symbol ϕ in Eq. (4) by ψ, where the new symbols mean the former function restricted to e. With this notation, the joint distribution restricted to e can be written as

![](/api/attachments/ND6GD7KB/fulltext/images/524648788358ad5a70d910c4fd79dfb3cf831d93f782bf1b1fdae39ca1e3f36a.jpg)  
Fig. 1. A mixed tree representing an MTE potential.

$$
\begin{array}{l} \psi (w, \mathbf {y}, \mathbf {z}) = \\ \psi_ {W} (w | p a (w)) \prod_ {i = 1} ^ {d} \psi_ {Y _ {i}} (y _ {i} | p a (y _ {i})) \prod_ {j = 1} ^ {c} \psi_ {Z _ {j}} \Big (z _ {j} | p a \Big (z _ {j} \Big) \Big) \prod_ {l = 1} ^ {k} \psi_ {E _ {l}} (e _ {l} | p a (e _ {l})). \end{array}\tag{5}
$$

So, the numerator in Eq. (3) can be obtained as

$$
\begin{array}{c} \int_ {a} ^ {b} \bigg (\sum_ {\mathbf {y} \in \mathbf {Y}} \int_ {\Omega_ {\mathbf {z}}} \phi (w, \mathbf {y}, \mathbf {z}, \mathbf {e}) d \mathbf {z} \bigg) d w = \int_ {a} ^ {b} \Big (\sum_ {\mathbf {y} \in \mathbf {Y}} \int_ {\Omega_ {\mathbf {z}}} \psi (w, \mathbf {y}, \mathbf {z}) d \mathbf {z} \Big) d w \\ = \int_ {a} ^ {b} h (w) d w, \end{array}\tag{6}
$$

where $\begin{array} { r } { h ( w ) = \sum _ { \mathbf { y } \in \mathbf { Y } } \displaystyle \int _ { \Omega _ { \mathbf { z } } } \psi ( w , \mathbf { y } , \mathbf { z } ) d \mathbf { z } . } \end{array}$ To <sup>fi</sup>nally answer the query expressed in Eq. (3), we still have to compute $\phi _ { \mathbf { E } } ( \mathbf { e } )$ . This is obtained as

$$
\phi_ {\mathbf {E}} (\mathbf {e}) = \int_ {\Omega_ {W}} \left(\sum_ {\mathbf {y} \in \mathbf {Y}} \int_ {\Omega_ {\mathbf {z}}} \psi (w, \mathbf {y}, \mathbf {z}) d \mathbf {z}\right) d w = \int_ {\Omega_ {W}} h (w) d w.\tag{7}
$$

On the other hand, if W is discrete, a query is formulated as

$$
P (W = w | \mathbf {E} = \mathbf {e}) = \frac {\sum_ {\mathbf {y} \in \mathbf {Y}} \int_ {\Omega_ {\mathbf {z}}} \phi (w , \mathbf {y} , \mathbf {z} , \mathbf {e}) d \mathbf {z}}{\phi_ {\mathbf {E}} (\mathbf {e})},\tag{8}
$$

where $w \in \varOmega _ { W } .$ The numerator of Eq. (8) can be expressed as

$$
\sum_ {\mathbf {y} \in \mathbf {Y}} \int_ {\Omega_ {\mathbf {z}}} \phi (w, \mathbf {y}, \mathbf {z}, \mathbf {e}) d \mathbf {z} = \sum_ {\mathbf {y} \in \mathbf {Y}} \int_ {\Omega_ {\mathbf {z}}} \psi (w, \mathbf {y}, \mathbf {z}) d \mathbf {z} = h (w).\tag{9}
$$

A similar procedure is carried out to compute the denominator of Eq. (8):

$$
\phi_ {\mathbf {E}} (\mathbf {e}) = \sum_ {w \in \Omega_ {W}} \sum_ {\mathbf {y} \in \mathbf {Y}} \int_ {\Omega_ {\mathbf {Z}}} \psi (w, \mathbf {y}, \mathbf {z}) d \mathbf {z} = \sum_ {w \in \Omega_ {W}} h (w).\tag{10}
$$

Hence, answering the queries formulated in Eqs. (3) and (8), requires the computation of the expressions in Eqs. (6), (7), (9) and (10). The problem is that in all the cases, the calculations are carried out over the joint distribution, which size is exponential in the number of variables in the network. Therefore, if the number of variables is high, it can be dif<sup>fi</sup>cult or even impossible to represent such a joint distribution in a decision support system, specially if memory resources are limited. In the next section we propose a solution for approximating the quantities required to answer the queries, keeping the complexity bounded. The solution is based on the use of the importance sampling technique [39].

## 4. Answering queries using importance sampling

## 4.1. Continuous target variable

We will start off by considering the case in which the target variable, W, is continuous. Let us denote by θ the numerator of Eq. (3). We can write θ as

$$
\theta = \int_ {a} ^ {b} h (w) d w = \int_ {a} ^ {b} \frac {h (w)}{f ^ {*} (w)} f ^ {*} (w) d w = E _ {f ^ {*}} \left[ \frac {h (W ^ {*})}{f ^ {*} (W ^ {*})} \right],\tag{11}
$$

where $f ^ { * }$ is a probability density function on $( a , b )$ called sampling distribution, and $W ^ { * }$ is a random variable with density f \*. Let $W _ { 1 } ^ { * } , . . . , W _ { m } ^ { * }$ be a sample drawn from f <sup>∗</sup>. Then it is easy to prove that

$$
\hat {\theta} _ {1} = \frac {1}{m} \sum_ {i = 1} ^ {m} \frac {h (W _ {i} ^ {*})}{f ^ {*} (W _ {i} ^ {*})}\tag{12}
$$

is an unbiased estimator of θ. This procedure is called importance sampling.

As $\hat { \theta } _ { 1 }$ is unbiased, the error of the estimation is determined by its variance, which i

$$
\operatorname{Var} \left(\hat {\theta} _ {1}\right) = \operatorname{Var} \left(\frac {1}{m} \sum_ {i = 1} ^ {m} \frac {h \left(W _ {i} ^ {*}\right)}{f ^ {*} \left(W _ {i} ^ {*}\right)}\right) = \frac {1}{m} \operatorname{Var} \left(\frac {h \left(W ^ {*}\right)}{f ^ {*} \left(W ^ {*}\right)}\right).\tag{13}
$$

In order to minimise the variance in the expression above $, f ^ { * }$ must be selected in such a way that the ratio between h and f \*∗ be as constant as possible within interval (a,b). Actually, the minimum variance is reached when $f ^ { * }$ is proportional to h in that interval, but that is of no practical value, as we are assuming that h, which is equivalent to the joint distribution, is dif<sup>fi</sup>cult to handle. Later on we will show in detail a way to obtain an approximation to h, but keeping the complexity bounded. Let h\* be such an approximation. Then it holds that

$$
f ^ {*} (w) = \frac {h ^ {*} (w)}{\int_ {a} ^ {b} h ^ {*} (w) d w}, \quad a <   w <   b,\tag{14}
$$

is a probability density function within interval (a,b). Therefore, in order to apply importance sampling to answer our target query, we have to <sup>fi</sup>nd an approximation, h\*, of h and then obtain a sampling distribution from it, according to Eq. (14). Finally, we can estimate θ using Eq. (12).

On the other hand, $\phi _ { \mathbf { E } } ( \mathbf { e } )$ can be estimated using importance <sup>ð Þ</sup>sampling as well. In principle, a new sample should be generated, since the integral range in this case is the entire domain of W, and not only interval (a,b). To avoid generating two different samples, we can consider the following density:

$$
f _ {2} ^ {*} (w) = \frac {h ^ {*} (w)}{\int_ {\Omega_ {W}} h ^ {*} (w) d w},\tag{15}
$$

which is a density for $\Omega _ { W } .$ From this, we can generate a sample $W _ { 1 } ^ { * } , . . . ,$ $W _ { m } ^ { * } .$ . Then, it holds that

$$
\hat {\delta} = \frac {1}{m} \sum_ {i = 1} ^ {m} \frac {h (W _ {i} ^ {*})}{f _ {2} ^ {*} (W _ {i} ^ {*})}\tag{16}
$$

is an unbiased estimator of $\phi _ { \mathbf { E } } ( \mathbf { e } )$

Now, if we write $W _ { ( 1 ) } ^ { * } , . . . , W _ { ( k ) } ^ { * }$ for the elements from sample $W _ { 1 } ^ { * } , . . . ,$ $W _ { m } ^ { * }$ that fall inside interval (a,b), then it can be shown that

$$
\hat {\theta} _ {2} = \frac {1}{k} \sum_ {i = 1} ^ {k} \frac {h \left(W _ {(i)} ^ {*}\right)}{f _ {2} ^ {*} \left(W _ {(i)} ^ {*}\right)}\tag{17}
$$

is an unbiased estimator of θ. Next proposition establishes the impact of using the same sample on the accuracy of the estimation.

Proposition 1. Let m, $k , \hat { \theta } _ { 2 }$ and $\hat { \delta }$ be as in Eqs. (16) and (17). Then,

$$
\operatorname{Var} \left(\hat {\theta} _ {2}\right) \leq \frac {m}{k} \operatorname{Var} \left(\hat {\delta}\right) + \frac {\phi_ {\mathbf {E}} (e) ^ {2}}{2 k}.\tag{18}
$$

Proof. Let functions h and $f _ { 2 } ^ { * }$ be as in Eqs. (16) and (17). We define $\xi , \xi _ { 1 }$ and $\xi _ { 2 }$ as $\xi ( w ) = \frac { h ( w ) } { f _ { 2 } ^ { * } ( w ) } , \ \xi _ { 1 } ( w ) = \frac { h ( w ) I _ { ( a , b ) } ( w ) } { f _ { 2 } ^ { * } ( w ) }$ and $\xi _ { 2 } ( w ) =$ $\frac { h ( w ) I _ { \mathbb { R } \backslash ( a , b ) } ( w ) } { f _ { 2 } ^ { * } ( w ) } ,$ w∈R, where $a , b { \in } \mathbb { R } , I _ { ( a , b ) } ( w ) { = } 1 { \mathrm { i f } } w { \in } ( a , b )$ and 0 otherwise, and $I _ { \mathbb { R } \backslash ( a , b ) } ( w ) = 0$ if $w \in ( a , b )$ and 1 otherwise.

It is clear that $\xi = \xi _ { 1 } + \xi _ { 2 }$ and $\xi _ { 1 } \times \xi _ { 2 } = 0$ . Also, notice that the expected values of $\xi _ { 1 }$ and $\xi _ { 2 }$ can be written, respectively, as $E [ \xi _ { 1 } ] =$ $P ( a { < } W { < } b | \mathbf { E } = \mathbf { e } ) \phi _ { \mathbf { E } } ( e )$ and $E [ \xi _ { 2 } ] = P ( W \not \in ( a , b ) | \mathbf { E } = \mathbf { e } ) \phi _ { \mathbf { E } } ( e )$

Then,

$$
\begin{array}{r l} \operatorname{Var} (\xi) & = \operatorname{Var} (\xi_ {1} + \xi_ {2}) = \operatorname{Var} (\xi_ {1}) + \operatorname{Var} (\xi_ {2}) + 2 \operatorname{Cov} (\xi_ {1}, \xi_ {2}) \\ & = \operatorname{Var} (\xi_ {1}) + \operatorname{Var} (\xi_ {2}) + 2 (E [ \xi_ {1} \xi_ {2} ] - E [ \xi_ {1} ] E [ \xi_ {2} ]) \\ & = \operatorname{Var} (\xi_ {1}) + \operatorname{Var} (\xi_ {2}) - 2 P (a <   W <   b | \mathbf {E} = \mathbf {e}) \phi_ {\mathbf {E}} (e) P (W \notin (a, b) | \mathbf {E} = \mathbf {e}) \phi_ {\mathbf {E}} (e) \\ & = \operatorname{Var} (\xi_ {1}) + \operatorname{Var} (\xi_ {2}) - 2 \phi_ {\mathbf {E}} (e) ^ {2} P (a <   W <   b | \mathbf {E} = \mathbf {e}) (1 - P (a <   W <   b | \mathbf {E} = \mathbf {e})) \end{array}
$$

Hence,

$$
\begin{array}{l} \operatorname{Var} (\xi_ {1}) = \operatorname{Var} (\xi) - \operatorname{Var} (\xi_ {2}) \\ \qquad + 2 \phi_ {\mathbf {E}} (e) ^ {2} P (a <   W <   b | \mathbf {E} = \mathbf {e}) (1 - P (a <   W <   b | \mathbf {E} = \mathbf {e})) \\ \qquad \leq \operatorname{Var} (\xi) + \frac {1}{2} \phi_ {\mathbf {E}} (e) ^ {2}, \end{array}
$$

since $\mathrm { V a r } ( \xi _ { 2 } ) \geq 0$ and $P ( a < W < b | \mathbf { E } = \mathbf { e } ) ( 1 - P ( a < W < b | \mathbf { E } = \mathbf { e } ) ) \leq \frac { 1 } { 4 } .$ . Thus,

$$
\begin{array}{l} \frac {1}{m} \operatorname{Var} (\xi_ {1}) \leq \frac {1}{m} \operatorname{Var} (\xi) + \frac {\phi_ {\mathbf {E}} (e) ^ {2}}{2 m} \Rightarrow \frac {k}{m} \frac {1}{k} \operatorname{Var} (\xi_ {1}) \leq \frac {1}{m} \operatorname{Var} (\xi) + \frac {\phi_ {\mathbf {E}} (e) ^ {2}}{2 m} \Rightarrow \\ \frac {k}{m} \operatorname{Var} \Big (\hat {\theta} _ {2} \Big) \leq \operatorname{Var} \Big (\hat {\delta} \Big) + \frac {\phi_ {\mathbf {E}} (e) ^ {2}}{2 m} \Rightarrow \operatorname{Var} \Big (\hat {\theta} _ {2} \Big) \leq \frac {m}{k} \operatorname{Var} \Big (\hat {\delta} \Big) + \frac {\phi_ {\mathbf {E}} (e) ^ {2}}{2 k}. \end{array}
$$

Proposition 1 establishes that the variance of $\hat { \theta } _ { 2 }$ is related to the variance of <sup>^</sup>δ by the inverse of the proportion of elements in the sample that fall within interval $( a , b )$ . It means that using a single sample does not increase the error of the estimation dramatically. Actually, if all the elements in the sample are inside the target interval, then the variance of both estimators is asymptotically the same, as the term $\phi _ { \mathrm { E } } ( e ) ^ { 2 } / 2 k$ tends to 0 as k increases. Therefore, for large samples, the ratio between

the variances of both estimators veri<sup>fi</sup>es that ${ \frac { \operatorname { V a r } \left( { \hat { \theta } } _ { 2 } \right) } { \operatorname { V a r } \left( { \hat { \delta } } \right) } } \leq { \frac { m } { k } } .$

Notice that, if we used two samples instead of one (i.e., we used $\hat { \theta } _ { 1 }$ instead of $\hat { \theta } _ { 2 } )$ , of size m for <sup>^</sup>δ and size k for $\hat { \theta } _ { 1 }$ , the ratio would be

$$
\frac {\operatorname{Var} \left(\hat {\theta} _ {1}\right)}{\operatorname{Var} \left(\hat {\delta}\right)} = \frac {\frac {1}{k} \operatorname{Var} \left(\frac {h (W ^ {*})}{f ^ {*} (W ^ {*})}\right)}{\frac {1}{m} \operatorname{Var} \left(\frac {h (W ^ {*})}{f _ {2} ^ {*} (W ^ {*})}\right)},
$$

and according to Eqs. (14) and (15), it follows that

$$
\frac {\operatorname{Var} \left(\hat {\theta} _ {1}\right)}{\operatorname{Var} \left(\hat {\delta}\right)} = \frac {\frac {\left(\int_ {a} ^ {b} h ^ {*} (w) d w\right) ^ {2}}{k} \operatorname{Var} \left(\frac {h (W ^ {*})}{h ^ {*} (W ^ {*})}\right)}{\frac {\left(\int_ {\Omega_ {W}} h ^ {*} (w) d w\right) ^ {2}}{m} \operatorname{Var} \left(\frac {h (W ^ {*})}{h ^ {*} (W ^ {*})}\right)} = \frac {m}{k} \frac {\left(\int_ {a} ^ {b} h ^ {*} (w) d w\right) ^ {2}}{\left(\int_ {\Omega_ {W}} h ^ {*} (w) d w\right) ^ {2}} \leq \frac {m}{k}.
$$

The conclusion is that for large sample sizes, the variances of $\hat { \theta } _ { 1 }$ and $\hat { \theta } _ { 2 }$ are equally related to the variance of <sup>^</sup>δ. Therefore, for large samples, the use of a single sample is worth it.

## 4.2. Discrete target variable

If the target variable is discrete, the procedure is analogous. More precisely, if W is discrete then from Eq. (9) it follows that

$$
\begin{array}{l} \sum_ {\mathbf {y} \in \mathbf {Y}} \int_ {\Omega_ {\mathbf {z}}} \phi (w, \mathbf {y}, \mathbf {z}, \mathbf {e}) d \mathbf {z} = \sum_ {w ^ {\prime} \in \Omega_ {w}} h (w ^ {\prime}) I _ {w} (w ^ {\prime}) = \sum_ {w ^ {\prime} \in \Omega_ {w}} \frac {h (w ^ {\prime}) I _ {w} (w ^ {\prime})}{p ^ {*} (w ^ {\prime})} p ^ {*} (w ^ {\prime}) \\ = E _ {p ^ {*}} \left[ \frac {h (W ^ {*}) I _ {w} (W ^ {*})}{p ^ {*} (W ^ {*})} \right], \end{array}
$$

where $p ^ { * }$ is any probability mass function de<sup>fi</sup>ned on $\Omega _ { W } , W ^ { * }$ is a discrete random variable with distribution $p ^ { * } ,$ , and $I _ { w } ( x ) = 1 { \mathrm { i f } } w = x$ and 0 otherwise.

The rest of the procedure is analogous to the continuous case, that is, a sample $W _ { 1 } ^ { * } , . . . , W _ { m } ^ { * }$ is generated from $p ^ { * }$ and $\begin{array} { r } { \theta _ { d } = \sum _ { \mathbf { y } \in \mathbf { Y } } \int _ { \varOmega _ { \mathbf { Z } } } \phi ( w , \mathbf { y } , \mathbf { z } , \mathbf { e } ) d \mathbf { z } } \end{array}$ is estimated as

$$
\hat {\theta} _ {d} = \frac {1}{m} \sum_ {i = 1} ^ {m} \frac {h (W _ {i} ^ {*}) I _ {w} (W _ {i} ^ {*})}{p ^ {*} (W _ {i} ^ {*})},\tag{19}
$$

where subscript d indicates that this estimator is for the discrete case.

## 4.3. Obtaining a sampling distribution

The error in the estimation procedure above described, depends on the variance of the ratio $h / f$ . Therefore the best behaviour is obtained if the sampling distribution is close to h, as we mentioned before. In [41] a method for computing an accurate sampling distribution for discrete Bayesian networks was developed. It is based on computing the sampling distribution for a given variable through a process of eliminating the other variables from the set of all the conditional distributions in the network, $H = \{ p ( \mathbf { x } _ { i } | p a ( \mathbf { x } _ { i } ) ) , i = 1 , . . . , n \}$ . The procedure can be adapted <sup>¼ ð Þf ð j Þ ¼ g</sup>to the case of a hybrid Bayesian network as follows. Let $\{ X _ { 1 } , . . . , X _ { l } \}$ be the set of all the variables in the network, except the target W and the observations E. An elimination order σ is considered and variables are deleted according to such order: $X _ { \sigma ( 1 ) } , . . . , X _ { \sigma ( l ) }$

The deletion of a variable $X _ { \sigma ( i ) }$ consists of marginalising it out from the combination of all the functions in H which are de<sup>fi</sup>ned for that variable. More precisely, the steps are as follows:

• Let dom(f) denote the set of variables for which function f is de<sup>fi</sup>ned.

• Let $H _ { \sigma ( i ) } = \{ f { \in } H | X _ { \sigma ( i ) } { \in } \mathsf { d o m } ( f ) \}$

• Calculate

$$
f _ {\sigma (i)} = \prod_ {f \in H _ {\sigma (i)}} f\tag{20}
$$

and $f _ { \sigma ( i ) } ^ { \prime }$ de<sup>fi</sup>ned on dom $( f _ { \sigma ( i ) } ) \backslash \{ X _ { \sigma ( i ) } \} ,$ , by

$$
f _ {\sigma (i)} ^ {\prime} (\mathbf {y}) = \int_ {x _ {\sigma (i)} \in \Omega_ {x _ {\sigma (i)}}} f _ {\sigma (i)} \left(\mathbf {y}, x _ {\sigma (i)}\right) d x _ {\sigma (i)}   \forall \mathbf {y} \in \Omega_ {\operatorname{dom} \left(f _ {\sigma (i)}\right) \backslash \left\{X _ {\sigma (i)} \right\}}.\tag{21}
$$

• Transform H into $H \backslash H _ { \sigma ( i ) } \cup \left\{ f _ { \sigma ( i ) } ^ { \prime } \right\}$

Note that the integral in Eq. (21) would be a summatory if W were discrete. After deleting all the variables $X _ { \sigma ( 1 ) } , . . . , X _ { \sigma ( l ) }$ from the set of distributions $H = \{ p ( \mathbf { x } _ { i } | p a ( \mathbf { x } _ { i } ) ) , i = 1 , . . . , n \}$ , the remaining functions will depend only on W. If all the computations are exact, it was proved in [14] that the remaining function is actually the optimal sampling distribution.

However, the result of the products (see Eq. (20)) in the process of obtaining the sampling distribution may require a large amount of space to be stored, and therefore the algorithm in [41] approximates the result of the combinations by pruning the probability trees (in our case, mixed trees) used to represent the potentials. The price to pay is that the sampling distribution is not the optimal one and the accuracy of the estimations will depend on the quality of the approximations. Here we propose a strategy for approximating the MTE potentials resulting from the products in Eq. (20). We will explain the idea by considering an MTE potential de<sup>fi</sup>ned for a set of continuous variables $\mathbf { Z } = ( Z _ { 1 } , . . . , Z _ { t } ) ^ { T }$ as $\begin{array} { r } { \mathbf { \bar { \phi } } ( \mathbf { z } ) = a _ { 0 } + \sum _ { i = 1 } ^ { t } a _ { i } e ^ { \mathbf { b } _ { i } ^ { T } \mathbf { z } } } \end{array}$

<sup>¼</sup>The goal is to detect those exponential terms in ϕ z that are almost constant and remove them. The rationale behind this strategy is that, from the point of view of simulation, a <sup>fl</sup>at or constant term does not provide any useful information to the entire density, as there is already a constant term, namely $a _ { 0 } .$

Thus, we consider a threshold $\alpha \in ( 0 , 1 )$ and then, for each term $\begin{array} { r } { g _ { j } ( \mathbf { z } ) = a _ { j } e ^ { \mathbf { b } _ { j } ^ { T } \mathbf { z } } , j = 1 , . . . , t , } \end{array}$ in the mixture, if the condition $\frac { \operatorname* { m i n } \Bigl ( g _ { j } ( \mathbf { z } ) \Bigr ) } { \operatorname* { m a x } \Bigl ( g _ { j } ( \mathbf { z } ) \Bigr ) } > \alpha$ is satis<sup>fi</sup>ed, then $g _ { j } ( { \pmb z } )$ is replaced by $k _ { j } = \int _ { \mathbf { z } } g _ { j } ( \mathbf { z } ) d \mathbf { z } .$

The closer to 1 α is, the more accurate the approximation. Note that the previous statements can be made taking into account that the exponential function by nature is strictly increasing or decreasing on its whole domain, and therefore its maximum and minimum are always located at the borders of the domain. In this way, the shape of the function can be controlled.

Summing up, if the j-th term of the mixture is replaced by constant $k _ { j } ,$ except in the cases where the resulting density could have negative values. To avoid the presence of negative values, we correct the value of $k _ { j }$ by making $k _ { j } = \mathrm { m a x } \bigg \{ \mathrm { m i n } _ { \mathbf { z } } \Big \{ g _ { j } ( \mathbf { z } ) \Big \} , \int _ { \mathbf { z } } g _ { j } ( \mathbf { z } ) d \mathbf { z } \bigg \}$ . Thus, the resulting potential is

$$
\hat{\phi} (\mathbf{z}) = k + k_{j} + \sum_{\substack{i\in \{1,\ldots ,t\} \\ i\neq j}}a_{i}e^{\mathbf{b}_{i}^{T}\mathbf{z}}.
$$

But in fact, MTE potentials are de<sup>fi</sup>ned into hypercubes. Therefore, rather than approximating a single potential, after each product the whole mixed tree representing the resulting potential should be approximated following this strategy. The detailed procedure can be found in Alg. 1.

Algorithm 1. Prune MTE potential $( T , \alpha )$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: PruneMTEPotential(T,α)

Input: An mixed tree T and a threshold α for pruning terms.

Output: Tree T with terms pruned according to α.

1 Let Z be the set of continuous variables of tree T.

2 foreach leaf in T do

3 Let φ(z) = k + ∑i=1t ai e b$^{T}$z be the MTE stored in the current leaf.

4 for j := 1 to t do

5 Let a$_{j}$e b$^{T}$z be the j-term of φ(z).

6 if min(a$_{j}$e b$^{T}$z) / max(a$_{j}$e b$^{T}$z) &gt; α then

7 k$_{j}$ := max{min$_{z}$ {a$_{j}$e b$^{T}$z}, ∫$_{z}$ a$_{j}$e b$^{T}$z dZ).

8 Remove a$_{j}$e b$^{T}$z from φ(z)

9 Update the independent term k of φ(z) to k + k$_{j}$.

10 return T.
</div>

## 4.4. Answering multiple queries simultaneously

The procedure described so far is designed to answer queries concerning a single variable at a time. We will show in this section that it can be extended to allow the possibility of answering multiple queries about different variables at the same time. The idea is based on the elimination procedure described in Section 4.3.

It is possible to carry out a simulation in an order contrary to the one in which variables are deleted. To obtain a value for $X _ { \sigma ( i ) } ,$ the function $f _ { \sigma ( i ) }$ obtained in the deletion of this variable is used. This function is de<sup>fi</sup>ned for the values of variable $X _ { \sigma ( i ) }$ and other variables already sampled. Function $f _ { \sigma ( i ) }$ is restricted to the already obtained values of variables in dom $\mathcal { f } _ { \sigma ( i ) } ) \backslash \{ X _ { \sigma ( i ) } \}$ , giving rise to a density function which depends only on $X _ { \sigma ( i ) } .$ . Finally, a value for this variable is drawn from this density. If all the computations are exact, it was proved in [14] that the simulation is actually carried out using the optimal density, and we obtain a sample from the joint distribution of $X _ { \sigma ( 1 ) } , . . . , X _ { \sigma ( l ) }$

## Algorithm 2. Sampling distributions $( B , \mathsf { e } )$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2: SamplingDistributions(B,e)

Input: A hybrid BN, B, and an observation e.

Output: A sampling distribution for each variable in the network.

1 Let  $H := \{\psi_{X_1}, \ldots, \psi_{X_l}\}$  be all the potentials in B restricted to the evidence e, represented as mixed trees.

2 S := ∅.

3 for i := 1 to l do

4 Select the next variable to remove,  $X_i$ .

5  $H_{X_i} := \{\psi \in H | X_i \in \text{dom}(\psi)\}$ .

6  $f_{X_i} := \prod_{\psi \in H_{X_i}} \psi$ .

7  $f_{X_i}^* := \text{PruneMTEPotential}(f_{X_i}, \alpha)$ .

8  $S := S \cup \{f_{X_i}^*\} ; H := H \setminus H_{X_i}$ .

9 if  $X_i$  is continuous then

10  $H := H \cup \{\int_{X_i} f_{X_i}^* dx_i\}$ .

11 else

12  $H := H \cup \{\sum_{X_i} f_{X_i}^*\}$ .

13 return S.
</div>

The details of this procedure are given in Alg. 2, which computes a sampling distribution for each unobserved variable in a hybrid Bayesian network. Later on we will study how to determine the order of the variables in Step. 4. Now let us denote by $W _ { 1 } , . . . , W _ { n }$ the unobserved variables in the network, and by $E _ { 1 } , . . . , E _ { k }$ the observed ones. Note that after applying Alg. 2, if we set $\alpha = 1$ in Step. 4, then it holds that the true joint probability function is $\begin{array} { r } { f ( w _ { 1 } , . . . , w _ { n } , e _ { 1 } , . . . , e _ { k } ) = \prod _ { i = 1 } ^ { l } f _ { X _ { i } } ^ { * } } \end{array}$ . That is, if we simulate each variable $X _ { i }$ using $f _ { X _ { i } } { } ^ { * } .$ <sup>¼</sup>, we would actually be obtaining a sample of random vectors $\mathbf { w } _ { 1 } , . . . , \mathbf { w } _ { n } , \mathbf { e } _ { 1 } , . . . , \mathbf { e } _ { k }$ from the true distribution.

Our goal in this section is to answer a set of queries about the unobserved variables expressed as $P ( W _ { i } = w _ { i } | \mathbf { E } = \mathbf { e } ) ~ { \mathrm { o r } } ~ P ( a _ { i } < W _ { i } <$ $b _ { i } | \mathbf { E } = \mathbf { e } ) , i = 1 , . . . , n ,$ <sup>ð ¼ j Þ¼ ð</sup>if W is discrete or continuous, respectively. It can be shown that we can use the joint sample to estimate the different probabilities separately, since each individual sample is itself a suf<sup>fi</sup>cient statistic for the probability of a precise variable.

Let $W _ { 1 } ^ { ( j ) } , . . . , \bar { W } _ { n } ^ { ( j ) } , j { = } \bar { 1 } , . . . , m$ be a sample of size m drawn from the sampling distribution in the set S returned by Alg. 2. Then

$$
\hat {\delta} _ {2} = \frac {1}{m} \sum_ {j = 1} ^ {m} \frac {\psi \left(W _ {1} ^ {(j)} , \dots , W _ {n} ^ {(j)}\right)}{\prod_ {i = 1} ^ {n} f _ {W _ {i}} ^ {*} \left(W _ {i} ^ {(j)}\right)}\tag{22}
$$

is an unbiased estimator of $\phi _ { \mathbf { E } } ( \mathbf { e } )$

Let $W _ { 1 } ^ { ( j ) } { } ^ { * } , . . . , W _ { n } ^ { ( j ) } { } ^ { * } , j = 1 , . . . , \tilde { r }$ be the elements from the sample above that fall into interval $( a _ { i } , b _ { i } )$ (or for which $W _ { i } ^ { ( j ) } { = } w _ { i }$ in the discrete case), $i = 1 , . . . , n .$ . Then

$$
\hat {\theta} _ {W _ {i}} = \frac {1}{r} \sum_ {j = 1} ^ {r} \frac {\psi \left(W _ {1} ^ {(j) *} , \dots , W _ {n} ^ {(j) *}\right)}{\prod_ {i = 1} ^ {n} f _ {W _ {i}} ^ {*} \left(W _ {i} ^ {(j) *}\right)}\tag{23}
$$

is an unbiased estimator of $\int _ { a } ^ { b } \biggl ( \sum _ { \mathbf { y } \in \mathbf { Y } } \int _ { \Omega _ { \mathbf { z } } } \phi ( w _ { i } , \mathbf { y } , \mathbf { z } , \mathbf { e } ) d \mathbf { z } \biggr ) d w _ { i } , i = 1 , . . . , n$ (see Eq. (3)). A similar result can be derived immediately in the case that W is discrete, and therefore the quantity to estimate is $\begin{array} { r } { \sum _ { \mathbf { y } \in \mathbf { Y } } \displaystyle \int _ { \Omega _ { \mathbf { z } } } \phi ( w _ { i } , \mathbf { y } , \mathbf { z } , \mathbf { e } , } \end{array}$ dz (see $\operatorname { E q . } \left( 8 \right) )$ . In Eqs. (22) and (23), function ψ in the numerator is de<sup>fi</sup>ned in a similar way as in Eq. (5), i.e. the product of conditionals restricted to the observations.

## 5. The algorithm

In this section we give the details of the algorithm that implements our proposal for answering multiple queries in hybrid Bayesian networks with MTEs using importance sampling. First of all it should be emphasised that Alg. 2 makes a decision about which variable to remove in each iteration (see Step 4). The decision there in<sup>fl</sup>uences the complexity of the product in Step 6, since it determines the set of potentials that will be multiplied. We propose to use a one-step look-ahead heuristic based on selecting the variable that results in a potential of lowest size<sup>1</sup> after the product in Step 6.

Though it is not possible to know beforehand the exact size of a potential resulting from a product, an upper bound is given in [40]. This is the bound actually used for deciding the elimination order in Alg. 2. In this point, we have all the tools necessary for establishing our proposal for answering multiple queries, which is described in Alg. 3.

Algorithm 3. Answer queries $( B , \mathbf { e } , \mathbf { Q } )$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 3: AnswerQueries(B,e,Q)

Input: A hybrid BN B with variables X. An observation e about a set of variables E. A list of queries Q of the form
 $P(a_{i} &lt; W_{i} &lt; b_{i} \mid \mathbf{e})$  if  $W_{i}$  is continuous and  $P(W_{i} = w_{i} \mid \mathbf{e})$  otherwise.

Output: Estimations  $\hat{P}(a_{i} &lt; W_{i} &lt; b_{i} \mid \mathbf{e})$  or  $\hat{P}(W_{i} = w_{i} \mid \mathbf{e})$ .

1 Let  $W_{1}, \ldots, W_{n}$  be the variables in X \ E.

2 S := SamplingDistributions(B,e)

3 Initialise  $r_{i} := 0$  and  $\hat{P}_{i} := 0, i = 1, \ldots, n$ , and  $\hat{\phi}(\mathbf{e}) := 0$ .

4 for j := 1 to m do

5 Generate a sample  $w_{1}^{*}, \ldots, w_{n}^{*}$  for variables  $W_{1}^{(j)}, \ldots, W_{n}^{(j)}$  by simulating in reverse order to the one used in Alg. 2, using the sampling distributions in S (see [40]).

6 for i := 1 to n do

7 if  $W_{i}$  is continuous then

8 if  $w_{i}^{*} \in (a_{i}, b_{i})$  then

9  $\hat{P}_{i} := \hat{P}_{i} + \frac{\psi(w_{1}^{*}, \ldots, w_{n}^{*})}{\prod_{k=1}^{n} f_{W_{k}}^{*}(w_{k}^{*})}.$ 

10  $r_{i} := r_{i} + 1.$ 

11 else

12 if  $w_{i}^{*} = w_{i}$  then

13  $\hat{P}_{i} := \hat{P}_{i} + \frac{\psi(w_{1}^{*}, \ldots, w_{n}^{*})}{\prod_{k=1}^{n} f_{W_{k}}^{*}(w_{k}^{*})}.$ 

14  $r_{i} := r_{i} + 1.$ 

15  $\hat{\phi}(\mathbf{e}) := \hat{\phi}(\mathbf{e}) + \frac{\psi(w_{1}^{*}, \ldots, w_{n}^{*})}{\prod_{k=1}^{n} f_{W_{k}}^{*}(w_{k}^{*})}.$ 

16  $\hat{\phi}(\mathbf{e}) := \frac{\hat{\phi}(\mathbf{e})}{m}.$ 

17  $\hat{P}_{i} := \frac{\hat{P}_{i}}{r_{i} \times \hat{\phi}(\mathbf{e})}, i = 1, \ldots, n.$ 

18 return  $\hat{P}_{1}, \ldots, \hat{P}_{n}.$
</div>

## 6. Experimental evaluation

A series of experiments was carried out with the aim of analysing the performance of the proposed methodology. We have used two hybrid Bayesian networks. The <sup>fi</sup>rst one, denoted as arti<sup>fi</sup>cial, is an arti<sup>fi</sup>cial network with 97 variables, whose structure and parameters were generated at random, in the same way as the networks used in [40].

The second one has been created taking the structure from the barley network [21], which is originally fully discrete, and making some assumptions about the kind of the variables. Out of the 48 variables in the network, 10 of them were considered as discrete with two states, and the remaining were considered continuous with support in the interval [0,1]. The domain of each continuous variable was split into two pieces. The MTE densities associated with each split were de<sup>fi</sup>ned using 2 exponential terms, with parameters generated at random as in [40]. For each network, 20% of the variables were observed at random, considering as goal variables the remaining 80%. For each network, we considered 10 different observations. The queries were also selected at random, with uniform probability for each value of the discrete variables, and considering an interval of width of a 10% of its support for each continuous target variable.

## 6.1. Experiment 1

In this experiment we compared the performance of the importance sampling (IS) algorithm versus the other two approximate propagation methods existing in the literature for MTE networks: Markov Chain Monte Carlo (MCMC) and Penniless Propagation (PP) [40]. The version of the MCMC algorithm used in this paper is the adaptation for MTEs described in [40].

For each set of observations, the execution time and the error in the estimations were computed. The error was calculated using the $\chi ^ { 2 }$ divergence, which is de<sup>fi</sup>ned as

$$
\chi^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {(p _ {i} - p _ {i}) ^ {2}}{p _ {i}},
$$

where $p _ { i } , i { = } 1 , . . . , n$ are the true probabilities for each query, and $\hat { p } _ { i } ,$ $i = 1 , . . . , n$ are their estimations. The true probabilities have been computed using the variable elimination algorithm [49]. Notice that, using that algorithm it is possible to obtain the exact probabilities, but the time required is too long compared with the three approximate methods analysed here.

Fig. 2 shows the results of the experiment for networks arti<sup>fi</sup>cial and barley, respectively, represented as beanplots [19], which are extended versions of the well known box-plots where the empirical distribution of the data is also shown. The three beanplots correspond to the $\chi ^ { 2 }$ error, execution time and the rate error×time obtained for a set of 10 observations. Each execution of the simulation algorithms (IS and MCMC) was repeated 10 times, using in both cases a sample of size 500. The results shown correspond to the average over the 10 executions. In order to simplify the potentials during the propagation, we have set a threshold $\alpha { = } 0 . 9 5$ for the mixed trees in the IS algorithm (see Section 4.3) and for algorithm PP we chose the following parameters, taken from [40]: $_ { J o i n } = 0 . 0 5 , \ _ { D i s c } = 0 . 0 5$ . We refer the readers to the original reference for a detailed explanation of the meaning of those parameters. We limited the maximum number of exponential terms in the PP algorithm to 2.

The experimental results show how the IS algorithm clearly outperforms the other two in terms of accuracy, speed and rate error×time for network arti<sup>fi</sup>cial. For network barley, the error is again lower for IS, but in exchange the running time is the worse. This is due to the higher complexity of the potentials involved in this network, which makes the algorithm invest much time on obtaining the sampling distributions. However, the time invested is worth it, as can be seen looking at the plot corresponding to the rate error×time, which is better for IS. Therefore, we conclude that this experiments suggest that IS offers the best way for dealing with the tradeoff between complexity and accuracy when answering multiple queries.

![](/api/attachments/ND6GD7KB/fulltext/images/26dd40a191020d4fdaceb067b2cf1ef21a689d9e70c4c20e26ad851d9763a2e4.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/588c8436ab761530367f02c759d73c09268d13af9a023e3ce7c994c87184a921.jpg)

## 6.2. Experiment 2

The second experiment is devoted to analyse the impact of the sample size as well as the execution time in the behaviour of the simulation algorithms, that is IS and MCMC. Fig. 3 shows the $\chi ^ { 2 }$ divergence as a function of sample size and time, for the two networks considered. It can be seen that IS converges more quickly than MCMC, and also converges to a more accurate solution. The results are consistent with the known tendency of MCMC in Bayesian networks, to fall in regions of the sample space conformed by con<sup>fi</sup>gurations of low probability [15].

## 6.3. Experiment 3

The third experiment was aimed at testing the impact of using the pruning method proposed in Section 4.3. More precisely, we performed a test consisting of running the algorithm with different α thresholds and measuring the $\chi ^ { 2 }$ error of the predictions. As in previous experiments, for each of the 10 observations, the algorithm was run 10 times. The results displayed in Fig. 4 show the average of the errors obtained. As expected, the error decreases as we increase the threshold, which means that we are being more strict with the pruning criterion.

## 6.4. Experiment 4

Finally, we replicated the three experiments described above including deterministic relations in the used networks. We only considered deterministic conditionals for discrete variables, as the MTE model does not support this kind of relations among continuous variables beyond linear dependencies involving a single variable [5].

![](/api/attachments/ND6GD7KB/fulltext/images/88517317469ac44f08a0fca93ff7cf95703cf695a49dc8fd2d7dfd30372b2938.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/780a12c75f049db371e9f7c019655de3b8a2bc35b2b9c7efd999ed8ee3d37861.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/63bf6c8807d3a912ac3c46c7bc4758e44153981e222cce82ffafd2ceb55c74e1.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/f6af0ea428a231c33d762436e365f5d06b6d1de853710da26e256c6303894187.jpg)  
Fig. 2. Beanplots of the $\chi ^ { 2 }$ error, execution time and the rate error×time for the queries in networks arti<sup>fi</sup>cial and barley

![](/api/attachments/ND6GD7KB/fulltext/images/3a4c7c06348e235f31126ff3aae9ed01f434f9a6a42a16e9aaa83d7c244c7af7.jpg)  
Fig. 3. $\chi ^ { 2 }$ error for methods IS and MCMC as a function of the sample size and execution time. Results for networks arti<sup>fi</sup>cial and barley.

In order to include deterministic conditionals, we selected at random 80% of the discrete variables and then set to 1 the probability of one of its possible values, and to 0 the remaining probabilities. The results are displayed in Figs. 5–7. It can be seen that the performance of the algorithm in the presence of deterministic relations is similar to the general case.

![](/api/attachments/ND6GD7KB/fulltext/images/f5fb422ee17c681deddcc59fb12d053b1ee4740b127bc8c40d3d3a5c2e65c63b.jpg)

## 7. Conclusions

We have introduced a method for solving multiple queries in hybrid Bayesian networks with MTEs. The method is based on importance sampling, which makes it an anytime algorithm. The algorithm is able to compute answers to multiple questions using a unique sample. We have shown that the variance remains bounded if the same sample is also used to compute the numerator and denominator in each query.

![](/api/attachments/ND6GD7KB/fulltext/images/0a023e87e03ccdd55f0ac6a7de236dc44b8e10127e108d739d4f43a2a9f30fa5.jpg)  
Fig. 4. $\chi ^ { 2 }$ error for different levels of pruning. The higher the α threshold, the less pruning is actually carried out. Results for networks barley and arti<sup>fi</sup>cial.

![](/api/attachments/ND6GD7KB/fulltext/images/0eb76ffd8e8e75d888963738efb32a91bcc6f9b94ca373f203bac733fb18a89e.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/6cc72ec3b50a7323c4564552b59d1fae71cefa64cae1d26bc4a4b71f103796e7.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/024193e705bc06b5e4d2018fa3dc6c8640b4840b70b99dbbceb33d23be046512.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/bcf5a6b8e99d535b166cf019021da80e7a4e800ee2fcb79c46afb84e6d6977fe.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/89e1a203b59e9a339c68cac80d7429a9e4b5ab02e1383e9bb4d63a12d1cdaa54.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/d0e2c87009c2db22dfe8cbac143c056ae172b4150effe7455b00a59e36b3825b.jpg)  
Fig. 5. Beanplots of the $\chi ^ { 2 }$ error, execution time and the rate error×time for the queries in networks arti<sup>fi</sup>cial and barley with deterministic relations.

![](/api/attachments/ND6GD7KB/fulltext/images/572df6ffc67f288cc7eb5d572e9f7166a24f88069aa915eb6a56c7bd2e53f04f.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/6645c40e87a8030c9ac01e1f88380b4dd6898fc59e87c658b6f4dfedd646b0a8.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/41759e5d5034780c7978e92d9935583507b2233ea3d18b4aeee2844f5d08dd81.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/bf0af19aed8e60ac441c4c6092ce345751162d50013dd352105129626c60b05c.jpg)  
Fig. 6. $\chi ^ { 2 }$ error for methods IS and MCMC as a function of the sample size and execution time, Results for networks artificial and barley with deterministic relations

![](/api/attachments/ND6GD7KB/fulltext/images/6c219e21fdcd30660281ca7dcbcc0b59988519073db17ee81935a2295c33ff4b.jpg)

![](/api/attachments/ND6GD7KB/fulltext/images/a2f9d026a62a943f6d7a2283e12c5044eb26977398397031ccb48c06aa08fc7e.jpg)  
Fig. $7 . \ \chi ^ { 2 }$ error for different levels of pruning. The higher the α threshold, the less pruning is actually carried out. Results for networks barley and arti<sup>fi</sup>cial with deterministic relations.

The experiments conducted illustrate the behaviour of the proposed algorithm, and they support the idea that the IS algorithm outperforms the two algorithms previously used for carrying out probabilistic reasoning in hybrid Bayesian networks with MTEs. Therefore, the methodology introduced here expands the class of problems that can be handled using hybrid Bayesian networks, and more precisely, it provides versatility to the MTE model, by increasing the ef<sup>fi</sup>ciency in solving probabilistic inference tasks.

We expect to continue this research line by developing methods for answering more complex queries. For instance, a query consisting on <sup>fi</sup>nding the most probable explanation to an observed fact in terms of a set of target variables, which is called abductive inference [11]. We also plan to study the application of the proposed algorithm to MOPs [42]. The main difference would be in Alg. 1, as in the case of MOPs, each term may oscillate within an interval, while MTEs are smoother.

## Acknowledgements

Work supported by the Spanish Ministry of Science and Innovation, projects TIN2007-67418-C03-02, TIN2010-20900-C04-02 and ERDF funds.

## References

[1] X. Bai, Predicting consumer sentiments from online text, Decision Support Systems 50 (2011) 732–742.

[2] C. Butz, S. Hua, K. Konkel, H. Yao, Join tree propagation with prioritized messages, Networks 55 (2010) 350–359.

[3] C. Butz, K. Konkel, P. Lingras, Join tree propagation utilizing both arc reversal and variable elimination, International Journal of Approximate Reasoning 52 (2010) 948-959.

[4] J. Cheng, M.J. Druzdzel, AIS-BN: an adaptive importance sampling algorithm for evidential reasoning in large Bayesian networks, Journal of Arti<sup>fi</sup>cial Intelligence Research 13 (2000) 155–188.

[5] E. Cinicioglu, P. Shenoy, Arc reversals in hybrid Bayesian networks with deterministic variables, International Journal of Approximate Reasoning 50 (2009) 763–777.

[6] B.R. Cobb, Ef<sup>fi</sup>ciency of in<sup>fl</sup>uence diagram models with continuous decision variables, Decision Support Systems 48 (2009) 257–266.

[7] B.R. Cobb, P.P. Shenoy, R. Rumí, Approximating probability density functions with mixtures of truncated exponentials, Statistics and Computing 16 (2006) 293–308

[8] G.F. Cooper, The computational complexity of probabilistic inference using Bayesian belief networks, Arti<sup>fi</sup>cial Intelligence 42 (1990) 393–405.

[9] P. Dagum, M. Luby, Approximating probabilistic inference in Bayesian belief networks is NP-hard, Arti<sup>fi</sup>cial Intelligence 60 (1993) 141–153.

[10] A. Fernández, M. Morales, C. Rodríguez, A. Salmerón, A system for relevance analysis of performance indicators in higher education using Bayesian networks, Knowledge and Information Systems 27 (2011) 327–344.

[11] J. Gámez, Abductive inference in Bayesian networks: a review, in: J. Gámez, S. Moral, A. Salmerón (Eds.), Advances in Bayesian Networks, Springer Verlag, 2004, pp. 101–120.

[12] W.R. Gilks, S. Richardson, D.J. Spiegelhalter, Markov Chain Monte Carlo in Practice, Chapman and Hall, London, UK, 1996.

[13] V. Gogate, R. Dechter, SampleSearch: importance sampling in presence of determinism, Arti<sup>fi</sup>cial Intelligence 175 (2011) 694–729.

[14] L.D. Hernández, S. Moral, A. Salmerón, A Monte Carlo algorithm for probabilistic propagation in belief networks based on importance sampling and strati<sup>fi</sup>ed simulation techniques, International Journal of Approximate Reasoning 18 (1998) 53–91.

[15] C.S. Jensen, A. Kong, U. Kjærulff, Blocking Gibbs sampling in very large probabilistic expert systems, International Journal of Human Computer Studies 42 (1995) 647–666.

[16] F.V. Jensen, S.L. Lauritzen, K.G. Olesen, Bayesian updating in causal probabilistic networks by local computation, Computational Statistics Quarterly 4 (1990) 269–282.

[17] F.V. Jensen, T.D. Nielsen, Bayesian Networks and Decision Graphs, Springer, 2007.

[18] M. Jordan, An introduction to variational methods for graphical models, Machine Learning 37 (1999) 183–233

[19] P. Kampstra. Beanplot: a boxplot alternative for visual comparison of distributions. Journal of Statistical Software 28 (2008) 1–9.

[20] D. Kozlov, D. Koller, Nonuniform dynamic discretization in hybrid networks, in: D. Geiger, P.P. Shenoy (Eds.), Proceedings of the 13th Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, Morgan Kaufmann, 1997, pp. 302–313.

[21] K. Kristensen, I.A. Rasmussen, The use of a Bayesian network in the design of a decision support system for growing malting barley without use of pesticides, Computers and Electronics in Agriculture 33 (2002) 197–217.

[22] H. Langseth, T.D. Nielsen, R. Rumí, A. Salmerón, Inference in hybrid Bayesian networks, Reliability Engineering and System Safety 94 (2009) 1499–1509.

[23] H. Langseth, T.D. Nielsen, R. Rumí, A. Salmerón, Mixtures of truncated basis functions, International Journal of Approximate Reasoning 53 (2012) 212–227.

[24] P. Larrañaga, S. Moral, Probabilistic graphical models in arti<sup>fi</sup>cial intelligence, Applied Soft Computing 11 (2011) 1511–1528.

[25] S.L. Lauritzen, Propagation of probabilities, means and variances in mixed graphical association models, Journal of the American Statistical Association 87 (1992) 1098–1108.

[26] S.L. Lauritzen, F. Jensen, Stable local computation with conditional Gaussian distributions, Statistics and Computing 11 (2001) 191–203.

[27] U. Lerner, Exact inference in networks with discrete children of continuous parents, in: J. Breese, D. Koller (Eds.), Uncertainty in Arti<sup>fi</sup>cial Intelligence, Morgan Kaufmann, 2001, pp. 319–328.

[28] A. Madsen, Belief update in CLG Bayesian networks with lazy propagation International Journal of Approximate Reasoning 49 (2008) 503–521.

[29] A. Madsen, Improvements to message computation in lazy propagation, International Journal of Approximate Reasoning 51 (2010) 499–514.

[30] A. Madsen, F. Jensen, Lazy propagation: a junction tree inference algorithm based on lazy evaluation, Arti<sup>fi</sup>cial Intelligence 113 (1999) 203–245.

[31] S. Moral, R. Rumí, A. Salmerón, Mixtures of truncated exponentials in hybrid Bayesian networks, Lecture Notes in Arti<sup>fi</sup>cial Intelligence 2143 (2001) 135–143.

[32] S. Moral, A. Salmerón, Dynamic importance sampling in Bayesian networks based on probability trees, International Journal of Approximate Reasoning 38 (2005) 245–261.

[33] M. Neil, M. Tailor, D. Marquez, Inference in Bayesian networks using dynamic discretisation, Statistics and Computing 17 (1999) 219–233.

[34] M. Neil, M. Tailor, D. Marquez, N. Fenton, P. Hearty, Modelling dependable systems using hybrid Bayesian networks, Reliability Engineering and System Safety 93 (2008)933-939

[35] E. Ngai, Y. Hu, Y. Wong, Y. Chen, X. Sun, The application of data mining techniques in <sup>fi</sup>nancial fraud detection: a classi<sup>fi</sup>cation framework and an academic review of literature, Decision Support Systems 50 (2011) 559–569.

[36] J. Pearl, Probabilistic Reasoning in Intelligent Systems, Morgan Kaufmann, San Mateo, 1988.

[37] F. Ramos, F. Cozman, Anytime anyspace probabilistic inference, International Journal of Approximate Reasoning 38 (2005) 53–80.

[38] V. Romero, R. Rumí, A. Salmerón, Learning hybrid Bayesian networks using mixtures of truncated exponentials, International Journal of Approximate Reasoning 42 (2006) 54–68.

[39] R.Y. Rubinstein, Simulation and the Monte Carlo Method, Wiley, New York, 1981.

[40] R. Rumí, A. Salmerón, Approximate probability propagation with mixtures of truncated exponentials, International Journal of Approximate Reasoning 45 (2007) 191–210.

[41] A. Salmerón, A. Cano, S. Moral, Importance sampling in Bayesian networks using probability trees Computational Statistics and Data Analysis 34 (2000) 387–413

[42] P. Shenoy, J. West, Inference in hybrid Bayesian networks using mixtures of polynomials, International Journal of Approximate Reasoning 52 (2011) 641–657.

[44] P.P. Shenoy, G. Shafer, Axioms for probability and belief function propagation, in: R.D. Shachter, T.S. Levitt, J.F. Lemmer, L.N. Kanal (Eds.), Uncertainty in Arti<sup>fi</sup>cial Intelligence 4, North Holland, Amsterdam, 1990, pp. 169–198.

[43] P.P. Shenoy, Binary join trees for computing marginals in the Shenoy–Shafer architecture, International Journal of Approximate Reasoning 17 (1997) 239–263.

[45] K. Xu, S. Liao, J. Li, Y. Song, Mining comparative opinions from customer reviews for competitive intelligence, Decision Support Systems 50 (2011) 743–754

[46] H. Yu, R. van Engelen, Arc refractor methods for adaptive importance sampling on large Bayesian networks under evidential reasoning, International Journal of Approximate Reasoning 51 (2010) 800–819.

[47] C. Yuan, M. Druzdzel, Importance sampling algorithms for Bayesian networks: principles and performance, Mathematical and Computer Modelling 43 (2005) 1189–1207.

[48] C. Yuan, M. Druzdzel, Theoretical analysis and practical insights into importance sampling for Bayesian networks, International Journal of Approximate Reasoning 46 (2007) 320–333.

[49] N.L. Zhang, D. Poole, Exploiting causal independence in Bayesian network inference, Journal of Arti<sup>fi</sup>cial Intelligence Research 5 (1996) 301–328.

Antonio Fernández is currently a postdoc research assistant in the Department of Statistics and Applied Mathematics at the University of Almería, Spain. He obtained his PhD from the University of Almería in 2011. He is a member of the Data Analysis Group of the University of Almería and his research interests include data mining, probabilistic graphical models and their applications.

Rafael Rumí is currently Associate Professor in the Department of Statistics and Applied Mathematics at the University of Almería, Spain. He obtained his PhD in Mathematics from the University of Almería in 2003. Formerly, he has worked in the Andalusian Statistical Institute. His current research interests are mainly focused on hybrid Bayesian networks and their applications to <sup>fi</sup>nance and environmental science.

Antonio Salmerón is currently Professor in the Department of Statistics and Applied Mathematics at the University of Almería, Spain. He obtained his PhD in Arti<sup>fi</sup>cial Intelligence from the University of Granada in 1998, and received the José Cuena award from the Spanish Association for Arti<sup>fi</sup>cial Intelligence in 2001. Professor Salmerón has been Chairman of the doctoral programmes study board at the University of Almería from 2001 to 2007. He was co-Chairman of the First European Workshop on Probabilistic Graphical Models, held in 2002. His current research interests are mainly focused on probabilistic graphical models, specially hybrid Bayesian networks and probabilistic decision graphs.
