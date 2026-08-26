---
otero_id: 14864
otero_key: "KGD9DRDA"
title: "Scalable learning of probabilistic latent models for collaborative filtering"
authors: "Helge Langseth; Thomas D. Nielsen"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2015.03.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Helge Langseth <sup>a,</sup>⁎, Thomas D. Nielsen <sup>b</sup>

<sup>a</sup> Department of Computer and Information Science, The Norwegian University of Science and Technology, Trondheim, Norway

<sup>b</sup> Department of Computer Science, Aalborg University, Aalborg, Denmark

## a r t i c l e i n f o

Article history: Received 29 April 2014 Received in revised form 6 February 2015 Accepted 19 March 2015 Available online 31 March 2015

Keywords: Collaborative <sup>fi</sup>ltering Scalable learning Probabilistic model Latent variables Variational Bayes

## a b s t r a c t

Collaborative <sup>fi</sup>ltering has emerged as a popular way of making user recommendations, but with the increasing sizes of the underlying databases scalability is becoming a crucial issue. In this paper we focus on a recently proposed probabilistic collaborative <sup>fi</sup>ltering model that explicitly represents all users and items simultaneously in the model. This model class has several desirable properties, including high recommendation accuracy and principled support for group recommendations. Unfortunately, it also suffers from poor scalability. We address this issue by proposing a scalable variational Bayes learning and inference algorithm for these types of models. Empirical results show that the proposed algorithm achieves signi<sup>fi</sup>cantly better accuracy results than other straw-men models evaluated on a collection of well-known data sets. We also demonstrate that the algorithm has a highly favorable behavior in relation to cold-start situations

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Recommender systems have become a well-established technology to help users cope with vast amounts of information. This is achieved by only presenting to the users the information which is deemed most relevant. Over the last years the diversity of the domains in which recommender systems have been successfully applied has increased significantly and includes movies, books, news, and products in general.

Recommender systems are typically grouped into two categories: content-based systems make item recommendations by combining content descriptions of the items in questions with a preference model of the user (e.g. inferred using previously rated items). On the other hand, collaborative filtering systems provide recommendations based on the ratings of other users with similar preferences. The two types of systems exhibit different characteristics; collaborative <sup>fi</sup>ltering systems typically enjoy a greater <sup>fl</sup>exibility in terms of the types of items that can be recommended whereas content-based systems are usually less susceptible to cold-start problems.

Collaborative <sup>fi</sup>ltering systems are often further sub-divided into model-based and memory-based [4] methods, although combinations of the two have also been proposed [29]. Memory-based systems rely on a distance measure to estimate user similarity, whereas model-based approaches learn a model of the user's preferences, which is subsequently used for making predictions. The earliest model-based approaches used a multinomial mixture model [10] for either grouping the users into user groups or items into item-categories. More recently, uniform models have been proposed that treat users and items equivalently and represent them jointly in the same model. An example of such a model is the probabilistic latent variable model proposed by Langseth and Nielsen [20].

The model described in [20] bears some resemblances with relational probabilistic models [13] in that it explicitly combines all users and items directly in the model [34,33,12]. More speci<sup>fi</sup>cally, the model is a special type of conditional linear Gaussian model [21], where each item and user is represented by a collection of abstract latent variables encoding intrinsic properties about the user/item in question. The rating assigned to item i by user p is in turn modeled as a linear Gaussian distribution conditioned on the corresponding latent user/item representations. This joint representation of users and items allows the model to take advantage of all the user/item information available when making recommendations. Not only does this result in high-quality recommendations, as documented in [20], but it also supports a well-founded and principled way of making group recommendations [7,25].

In order to learn the probabilistic latent variable models, Langseth and Nielsen [20] proposed an Expectation–Maximization (EM) algorithm tailored to the speci<sup>fi</sup>c model class. Unfortunately, the algorithm requires the calculation of the full covariance matrix for all the latent variables representing the users and items. Consequently, the algorithm does not scale to larger data sets.

In this paper we address the scalability problem by proposing approximate learning and inference algorithms based on a variational Bayes approach [1,3]. The algorithms employ a (generalized) mean-<sup>fi</sup>eld approximation of the variational distribution, which ensures that the complexity of the learning algorithm grows linearly in the number of data points/ratings. Furthermore, we show that the model <sup>fi</sup>ts within the general class of statistical query models that in turn supports an ef<sup>fi</sup>cient use of the MapReduce framework [8,6]; hence the algorithms are easily parallelizable and can exploit distributed architectures. We empirically evaluate the proposed algorithms using several wellknown data sets and demonstrate that the algorithm obtains results that are signi<sup>fi</sup>cantly better than what is obtained by a collection of straw-men methods. Finally, we analyze the performance of the method under cold-start conditions [19].

The remainder of the paper is structured as follows: In Section 2 we provide background information and describe the probabilistic latent variable model by Langseth and Nielsen [20]. Section 3 describes the variational Bayes based learning algorithm (with detailed derivations included in the Appendix A) and in Section 4 we present the empirical results. We conclude the paper in Section 5 and outline directions for future research.

## 2. A latent model for collaborative <sup>fi</sup>ltering

## 2.1. Bayesian network

A Bayesian network (BN) is a probabilistic graphical model that de-<sup>fi</sup>nes a compact representation of a joint probability distribution by exploiting and explicitly encoding conditional independence properties among the variables. The speci<sup>fi</sup>cation of a BN over a collection of variables $\{ X _ { 1 } , . . . , X _ { n } \}$ consists of two parts: a qualitative part and a quantitative part. The qualitative part corresponds to an acyclic directed graph $G = ( \nu , \mathcal { E } )$ , where the nodes represent the variables $\left\{ X _ { 1 } , . . . , X _ { n } \right\}$ <sup>¼ Vð ÞE V</sup>through a one-to-one mapping, and the edges specify the direct dependencies between the variables. For ease of exposition, we shall refer to nodes and variables interchangeably.

We shall describe the relations between the variables in a Bayesian network using graph terminology. Thus, the nodes whose outgoing edges intersect a node/variable $X _ { i }$ are called the parents of $\dot { X } _ { i } ,$ denoted $\pmb { \pi } _ { X _ { i } }$ , and the nodes to which there exists an edge emanating from $X _ { i }$ are called the children of $X _ { i \cdot }$ If there is a directed path from a node $X _ { i }$ to a node $X _ { j } ,$ then $X _ { j }$ is said to be a descendant of $X _ { i \cdot }$ Together the edges in the graph encode the conditional independence assumptions in the Bayesian network. Speci<sup>fi</sup>cally, a node $X _ { i }$ is conditionally independent of its non-descendants given its parents.

The quantitative part is de<sup>fi</sup>ned by a collection of conditional probability distributions or density functions s.t. each node is assigned exactly one probability distribution conditioned on its parents. In the remainder of this paper we shall assume that all variables are continuous. In particular, a variable X with parents $\pmb { \pi } _ { X _ { i } }$ is assumed to follow a conditional linear Gaussian distribution

$$
f \left(x _ {i} | \boldsymbol {\pi} _ {x _ {i}}\right) = \mathcal {N} \left(\boldsymbol {\mu} _ {i} + \boldsymbol {w} _ {i} ^ {\mathrm{T}} \boldsymbol {\pi} _ {x _ {i}}, \sigma_ {i}\right),
$$

i.e., the mean value is given as a weighted linear combination of the values of the parent variables whereas the variance is <sup>fi</sup>xed. The underlying conditional independence assumptions encoded in the BN allow us to calculate the joint probability function using the chain rule:

$$
f (x _ {1}, \dots , x _ {n}) = \prod_ {i = 1} ^ {n} f \left(x _ {i} | \boldsymbol {\pi} _ {x _ {i}}\right).
$$

With linear Gaussian distributions assigned to all the variables it follows that the joint distribution is a multivariate Gaussian distribution. The inverse of the covariance matrix (also called the precision matrix) for this multivariate distribution directly re<sup>fl</sup>ects the independencies de<sup>fi</sup>ned by the BN; the entry de<sup>fi</sup>ned by a pair of variables is zero if and only if the two variables are conditionally independent given the other variables in the network.

## 2.2. A latent variable model

The collaborative <sup>fi</sup>ltering method proposed in [20] relies on a Bayesian network representation that provides a joint model of all items, users, and their ratings. Before presenting the details of the model, we shall <sup>fi</sup>rst introduce some notation.

We will denote the matrix of ratings by R, which is of size # U × # M. Here # U is the number of users and # M is the number of items that are rated. R is a sparse matrix, meaning that it contains a considerable amount of missing values (more than 99% missing observations is quite common). The observed ratings are either realizations of ordinal variables (discrete variables with ordered states, $\mathrm { e . g . , ^ { \mathrm { 4 } } D i s l i k e ^ { \mathrm { " } } , ^ { \mathrm { 4 } } N e u t r a l ^ { \mathrm { " } } }$ ${ } ^ { \mathfrak { u } } \mathrm { L i k e } ^ { \mathfrak { v } } )$ or real numbers. In the following we will consider only continuous ratings encoded by real numbers, and assume that ratings given as ordinal variables have been translated into a numeric scale.

We use p as the index of an arbitrary person using the system, and i is the index of an item that can be rated. Consequently, $\pmb { \mathrm { R } } ( p , i )$ is the rating that person p gives item i. Next, we will use $\delta ( p , i )$ as an indicator function to show whether or not person p has rated item i. Speci<sup>fi</sup>cally, $\delta ( p , i ) = 1$ if the rating exists and $\delta ( p , i ) = 0$ otherwise. Furthermore, $\mathcal { T } ( p )$ is the set of items that person p has rated, i.e., $\mathcal { T } ( p ) = \cup _ { i : \delta ( p , i ) \neq 0 } \{ i \} ,$ and similarly $\mathcal { P } ( i ) = \cup _ { p : \delta ( p , i ) \neq 0 } \{ p \}$ <sup>Ið Þ</sup>is the set of persons that have rated item i. Lowercase letters are used to signify that a random variable is observed, so $\boldsymbol { r } ( p , i )$ is the rating that $p$ has given item i (that is, $\delta ( p , i ) = 1$ in this case). Finally, we let r denote all observed ratings (the part of R that is not missing).

When doing model-based collaborative <sup>fi</sup>ltering from a general perspective we look for a probabilistic model that for any item i and user p de<sup>fi</sup>nes a probability distribution over R(p, i) given model parameters ρ and observed ratings r. Given such a probability distribution, we can make recommendations based on the expected rating or the median rating for that distribution.

The probabilistic model that is proposed in [20] de<sup>fi</sup>nes a joint distribution over all ratings by introducing abstract latent variable representations of both the items and the users. Speci<sup>fi</sup>cally, each item i is represented by the random variables M and each user p is represented by the random variables $\mathbf { U } _ { p } .$ In a movie context one may for example interpret the different dimensions of m as representing different features of movie i such as to what extend the movie uses a well-known cast and the amount of explicit violence in the movie. Similarly, the dimensions of ${ \pmb u } _ { p }$ can be interpreted as corresponding to different user characteristics. Hence, since the variables are continuous, the value $\pmb { u } _ { p , j }$ of the jth variable $\mathbf { U } _ { p , j }$ can be interpreted as representing to what extent user p has the characteristics modeled by variable j. This also means that rather than assigning a user to a single “user group”, the continuous variables $\mathbf { U } _ { p , j }$ encode to what extent a user belongs to a certain group.<sup>1</sup> A priori we assume that $\mathbf { U } _ { p } { \sim } \mathcal { N } ( \mathbf { 0 } , \mathbf { I } )$ , for $1 \leq p \leq \# U _ { \cdot }$ , and $\mathbf { M } _ { i } { \sim } \mathcal { N } ( \mathbf { 0 } , \mathbf { I } )$ , for $1 \leq i \leq \# M .$

The rating assigned to item i by user p is modeled by assuming the existence of a linear mapping from the space describing users and items to the numerical rating scale:

$$
\mathbf {R} (p, i) | \left\{\mathbf {M} _ {i} = \boldsymbol {m} _ {i}, \mathbf {U} _ {p} = \boldsymbol {u} _ {p} \right\} = \boldsymbol {v} _ {p} ^ {\mathrm{T}} \boldsymbol {m} _ {i} + \boldsymbol {w} _ {i} ^ {\mathrm{T}} \boldsymbol {u} _ {p} + \phi_ {p} + \psi_ {i} + \epsilon .\tag{1}
$$

The rating in Eq. (1) is thus determined as an additive combination of user $p ^ { \prime } s$ preferences $\pmb { \nu } _ { p }$ for (or attitude towards) the features describing item i and item i's disposition w towards the different user groups.<sup>2</sup> The constants $\phi _ { p }$ and ψ in Eq. (1) can be interpreted as representing the average rating of user $p$ and the average rating of item i (after compensating for the user average), respectively. Furthermore, ε represents “sensor noise”, i.e., the variation in the ratings the model cannot explain.

For mathematical convenience, we assume that $\epsilon \sim \mathcal { N } ( 0 , \theta )$ . It follows that the marginal distribution for $\pmb { \mathrm { R } } ( p , i )$ can be written as

$$
\mathbf {R} (p, i) \sim \mathcal {N} \left(\phi_ {p} + \psi_ {i}, \boldsymbol {\nu} _ {p} ^ {\mathrm{T}} \boldsymbol {\nu} _ {p} + \boldsymbol {\mathbf {w}} _ {i} ^ {\mathrm{T}} \boldsymbol {\mathbf {w}} _ {i} + \theta\right).
$$

Finally it should be emphasized that we have the same number of latent variables for all users $( \mathrm { i } . \mathbf { e } . , | \mathbf { U } _ { o } | = | \mathbf { U } _ { p } | )$ and for all movies $( \mathrm { i } . \mathsf { e } . , |$ $\mathbf { M } _ { r } | = | \mathbf { M } _ { i } | )$ . Note, however, that |M<sub>i</sub>| and $| \mathbf { U } _ { p } |$ may differ. Fig. 1 (taken from [20]) shows a BN representation of the proposed model for a domain with two users and three items.

As described in [20] this model has several desirable properties. It allows for a semantic interpretation of the features/variables characterizing users and items, and it naturally provides support for making group recommendation. Furthermore, the model provides a generative perspective encompassing all ratings, users, and items simultaneously by entertaining a global view of the recommendation task. To see this, let us follow a chain of reasoning in the model depicted in Fig. 1: Assume User 1 has already rated Item 1, so that r(1, 1) has been observed by the system. When he also rates Item 2 (that is, $\mathbf { R } ( 1 , 2 ) = \pmb { r } ( 1 , 2 )$ is observed), one immediate effect is that the posterior distributions over $\mathbf { U } _ { 1 }$ and $\mathbf { M } _ { 2 }$ are updated to take the new information into account. Note that changing $\mathbf { U } _ { 1 }$ gives the model a new perspective towards all ratings User 1 has given, in particular r(1, 1): $\operatorname { I f } \mathbf { U } _ { 1 }$ is changed, we get a new understanding of how that particular rating came to be, and this may in turn shed new light on Item 1. Thus, the encoding of Item 1, represented by the distribution over $\mathbf { M } _ { 1 }$ , should be altered. Next, the new posterior over $\mathbf { M } _ { 1 }$ makes the model reconsider its representation of all users who have already rated Item 1, and thus the internal representation of those users must also be updated. This will again change the model's interpretation of all ratings that these users have given, and so on, quickly resulting in correlations between all ratings of all users. In general, the global perspective is both a desired property of the model as well as the source of a problem: From a predictive point of view, the model ef<sup>fi</sup>ciently leverages information from all observed ratings when generating new recommendations. This results in high quality recommendations, as demonstrated in [20], where the recommendation accuracy of the model signi<sup>fi</sup>cantly outperform other collaborative <sup>fi</sup>ltering systems when evaluated using the MovieLens 100k data set [15]. On the other hand, since all latent variables in the model quickly become entangled, this leads to computational challenges that must be further addressed to ensure that the model scales to reasonably sized data sets. This is the main topic of the next section.

![](/api/attachments/KGD9DRDA/fulltext/images/fcb6b8f31775dbda2bc414bdef9c541a92de051f0f16754db985d3af0595426f.jpg)  
Fig. 1. The full statistical model for collaborative <sup>fi</sup>ltering; this model has # $M = 3$ and #U = 2. The <sup>fi</sup>gure is from [20].

## 3. Learning the model from data

The learning algorithm described in [20] is based on the EMalgorithm [9]. Unfortunately, the computational complexity of that approach makes learning prohibitive for many real-world sized data sets. To see the problem, consider the rule for learning the weight $\pmb { \nu } _ { p } ,$ where the M-step [20] amounts to calculating

$$
\begin{array}{l} \boldsymbol {v} _ {p} \leftarrow \left[ \tau / \theta \cdot \mathbf {I} + \sum_ {i \in \mathcal {I} (p)} \mathbb {E} \left[ \mathbf {M} _ {i} \mathbf {M} _ {i} ^ {\mathrm{T}} \right] \right] ^ {- 1} \\ \times \left[ \sum_ {i \in \mathcal {I} (p)} \left(\boldsymbol {r} (p, i) \mathbb {E} [ \mathbf {M} _ {i} ] - \mathbb {E} \left[ \mathbf {M} _ {i} \mathbf {U} _ {p} ^ {\mathrm{T}} \right] \boldsymbol {w} _ {i} - \mathbb {E} [ \mathbf {M} _ {i} ] (\psi_ {i} + \phi_ {p})\right) \right], \end{array}\tag{2}
$$

where τ is a parameter introduced by Tikhonov regularization of the learned weights. Notice that the terms E M M<sup>Th i</sup> and E $\left[ \mathbf { M } _ { i } \mathbf { U } _ { p } ^ { \mathrm { T } } \right]$ are required. They are established during the algorithm's E-step, where the covariance matrix over all latent variables must be calculated. To <sup>fi</sup>nd the correlation between two latent vectors we must <sup>fi</sup>rst determine the full covariance matrix of all latent variables before the nonrelevant variables can be marginalized out. The size of the full covariance matrix quickly becomes problematic; a modest data set containing $\# U = 1 0 . 0 0 0 \mathrm { u s e r s }$ and $\# M = 1 . 0 0 0$ items results in a covariance matrix with more than $1 0 ^ { 8 }$ entries that need to be calculated. The source for this computational problem is the model's global perspective (discussed in Section 2.2), which generally introduces a posteriori correlations among all the latent variables.

In what follows we propose two approaches for speeding up the learning of the parameters. Firstly, an alternative learning algorithm based on a variational Bayes method is developed. As we shall see, by relying on this learning algorithm, the complexity problem mentioned above is mitigated (in fact, each iteration of the algorithm is linear in the number of ratings, users, and items). Secondly, we position the proposed learning algorithm within a MapReduce context, thereby also achieving a framework that can exploit distributed architectures and is scalable with the size of the data.

## 3.1. Variational Bayes approximations

Our starting-point for the subsequent developments is the de<sup>fi</sup>nition of the variational Bayes [2,32] framework. An introduction to the variational Bayes procedure can be found in [16]. In its general form, one considers the random variables $( X , Z ) ,$ , where $\pmb { X } = \pmb { x }$ is observed and we want to approximate f(z|x). We call the approximation q(z), where we for simplicity of notation suppress that $q ( z )$ depends on the observation x. We measure the quality of the approximation by the KL distance from $q \mathrm { t o } f ,$ and obtain

$$
D (q \| f) = \int_ {\mathbf {z}} q (\mathbf {z}) \log \left(\frac {q (\mathbf {z})}{f (\mathbf {z} | \mathbf {x})}\right) d \mathbf {z} = \int_ {\mathbf {z}} q (\mathbf {z}) \log \left(\frac {q (\mathbf {z})}{f (\mathbf {z} , \mathbf {x})}\right) d \mathbf {z} + \log (f (\mathbf {x})).
$$

By simple rearrangement, de<sup>fi</sup>ning $\mathcal { F } ( q ) = - \int _ { z } q ( z ) l o g \bigg ( \frac { q ( z ) } { f ( z , \pmb { x } ) } \bigg )$ dz and noting that $D ( q | | f ) \geq 0$ , we get that

$$
\log (f (\boldsymbol {x})) \geq \mathcal {F} (q).
$$

It follows that <sup>fi</sup>nding the $q ( \pmb { z } )$ that minimizes $D ( q \parallel f )$ is equivalent to maximizing ${ \mathcal { F } } ( q ) ,$ , under the constraints that $q ( \pmb { z } )$ is to be a probability density. Note that $\mathcal { F } ( q ) = - \int _ { z } q ( z ) l o g \left( \frac { q ( z ) } { f ( z , \pmb { x } ) } \right) d z = \mathbb { E } _ { q } \left[ l o g \left( \frac { f ( z , \pmb { x } ) } { q ( z ) } \right) \right] =$ $\mathcal { H } ( q ) + \mathbb { E } _ { q } [ l o g f ( \pmb { z } , \pmb { x } ) ] ,$ , where $\mathcal { H } ( q ) = - \mathbb { E } _ { q } [ l o g ( q ( \pmb { z } ) ) ]$ <sup>ð Þ</sup>is the entropy of $q ( \cdot ) .$

It turns out that we can maximize ${ \mathcal { F } } ( q )$ in a tractable way if we make structural assumptions about $q ( \cdot )$ <sup>Fð Þ</sup>. One popular strategy is to assume that $q ( z )$ factorizes into smaller factors, like for instance its separate variables, $\begin{array} { r } { q ( \pmb { z } ) = \prod _ { i } q _ { i } \left( z _ { i } \right) } \end{array}$ . This approach is commonly known as the mean-field approximation. In this case, through calculus of variations, we <sup>fi</sup>nd that $\mathcal { F } ( q )$ is maximized by setting

$$
\log q _ {i} (z _ {i}) = \mathbb {E} [ \log (f (\boldsymbol {z}, \boldsymbol {x})) ] + c,\tag{3}
$$

where c is a constant and the expectation is wrt. al $Z _ { j } \sim q _ { j } \thinspace s . t . j \neq i \thinspace [ 3 2 ]$ In principle, this allows us to calculate the distribution for Z if we assume that the distribution for each $Z _ { j } , j \neq i ,$ , is known.

However, an iterative procedure will have to be followed in practice. When utilizing Eq. (3) to <sup>fi</sup>nd the optimal approximation for $q _ { 1 } \left( z _ { 1 } \right)$ , say, the right-hand side of the equation will include expected values of (functions of) the other variables, that are calculated according to their respective approximate distributions. Thus, if, say, q<sub>2</sub> (z<sub>2</sub>) is wrongly assessed, the error will in turn affect the estimate of $q _ { 1 } \left( z _ { 1 } \right)$ and so on. Fortunately, the contraction theorem applies, ensuring an eventual convergence to a local optimum [32]. To this end, $\mathcal { F } ( q )$ is mon-<sup>Fð</sup>itored and used to determine the termination of the iterations.

## 3.2. Variational Bayes in our model

The speci<sup>fi</sup>cation of the full generative model over (R, U, M) given the parameters $\pmb { \rho } = ( \pmb { \phi } , \pmb { \psi } , \pmb { \nu } , \pmb { w } , \ \theta )$ can be expressed as

$$
f (\boldsymbol {r}, \boldsymbol {u}, \boldsymbol {m} | \rho) = f (\boldsymbol {r} | \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) f (\boldsymbol {m} | \rho) f (\boldsymbol {u} | \boldsymbol {\rho}),
$$

where

$$
\begin{array}{l} f (\boldsymbol {r} | \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) = \prod_ {p = 1} ^ {\# U} \prod_ {i \in \mathcal {I} (p)} \sqrt {\frac {\theta}{2 \pi}} e x p \left(- \frac {\theta}{2} \Big (\boldsymbol {r} (p, i) - \Big (\boldsymbol {v} _ {p} ^ {\mathrm{T}} \boldsymbol {m} _ {i} + \boldsymbol {w} _ {i} ^ {\mathrm{T}} \boldsymbol {u} _ {p} + \phi_ {p} + \psi_ {i} \Big) \Big) ^ {2}\right); \\ f (\boldsymbol {m} _ {i} | \boldsymbol {\rho}) = \mathcal {N} (\boldsymbol {0} _ {s}, \boldsymbol {I} _ {s \times s}); \\ f \Big (\boldsymbol {u} _ {p} | \boldsymbol {\rho} \Big) = \mathcal {N} (\boldsymbol {0} _ {t}, \boldsymbol {I} _ {t \times t}). \end{array}
$$

Further, in a Bayesian formulation of the problem, we give the following prior distributions to our parameters

$$
\begin{array}{l} f (\theta) = \text { Gamma } (a, b), \quad f (\psi_ {i}) = \mathcal {N} \Big (\mu_ {\psi}, 1 / \kappa_ {\psi} \Big), \quad f \Big (\phi_ {p} \Big) = N \Big (\mu_ {\phi}, 1 / \kappa_ {\phi} \Big) \\ f (\boldsymbol {w} _ {i}) = \mathcal {N} (\boldsymbol {0} _ {s}, 1 / \tau \cdot \mathbf {I} _ {s \times s}), \quad f \Big (\boldsymbol {v} _ {p} \Big) = \mathcal {N} (\boldsymbol {0} _ {t}, 1 / \tau \cdot \mathbf {I} _ {t \times t}). \end{array}
$$

This allows us to, in principle, calculate $f ( \pmb { u } , \pmb { m } , \pmb { \rho } | \pmb { r } )$ . Note that we have kept $\mu _ { \phi } = 0$ <sup>fi</sup>xed in the experiments reported in this paper, and for each experiment we have de<sup>fi</sup>ned $\scriptstyle { \mu _ { \psi } \ a s }$ the mid-point of the relevant rating-scale. Furthermore, we have found the behavior of the model to be rather robust wrt. the values of $\kappa _ { \psi } , \kappa _ { \phi } ,$ a and b, and have for simplicity set each of them equal to one.

To cast the present problem into the formulation of $\operatorname { E q . } \left( 3 \right)$ , we let Z denote all the latent variables and model parameters $z =$ $( \mathbf { M } , \mathbf { U } , \phi , \psi , \nu , \mathbf { \boldsymbol { w } } , \theta )$ and X be the part of R that is observed (the other ratings are barren, and can be disregarded during parameter learning).

Two <sup>fl</sup>avors of the variational Bayes framework will be examined. The <sup>fi</sup>rst one, which we will name generalized mean-field (GMF), takes as its starting point that the variational approximation of the full joint factorizes according to

$$
q (\boldsymbol {u}, \boldsymbol {m}, \boldsymbol {\rho}) = q (\theta) \prod_ {p = 1} ^ {\# U} q \left(\phi_ {p}\right) q \left(\boldsymbol {u} _ {p}\right) q \left(\boldsymbol {v} _ {p}\right) \prod_ {i = 1} ^ {\# M} q \left(\psi_ {i}\right) q \left(\boldsymbol {m} _ {i}\right) q \left(\boldsymbol {w} _ {i}\right).
$$

Thus, the posterior distribution over the variables of interest given the ratings is approximated by assuming independence between vectors of latent variables. For instance, the generalized mean-<sup>fi</sup>eld approximation prescribes that $\mathbf { M } _ { i } \perp \perp \mathbf { U } _ { p } | \{ \mathbf { R } = r \}$ , and $\mathbf { M } _ { i } \perp \mathbf { M } _ { j } | \{ \mathbf { R } = r \}$ . On the other hand, note that the dimensions of each random vector are seen as correlated in the posterior, $\mathbf { e . g . } , \mathbf { M } _ { i , k } \mathbf { \mathcal { M } M } _ { i , l } \mathbf { \lvert \{ R = } \it { r \} }$ for a speci<sup>fi</sup>c item i.

The second formulation, which is the standard mean-<sup>fi</sup>eld (later to be referred to by MF), assumes that the posterior factorizes over all variables, giving us

$$
\begin{array}{l} q (\boldsymbol {u}, \boldsymbol {m}, \boldsymbol {\rho}) = q (\theta) \prod_ {p = 1} ^ {\# U} \left(q \Big (\phi_ {p} \Big) \prod_ {j = 1} ^ {| \mathbf {u} _ {p} |} q \Big (\boldsymbol {u} _ {p, j} \Big) q \Big (\boldsymbol {v} _ {p, j} \Big)\right) \\ \qquad \times \prod_ {i = 1} ^ {\# M} \left(q (\psi_ {i}) \prod_ {j = 1} ^ {| \mathbf {M} _ {i} |} q \Big (\boldsymbol {m} _ {i, j} \Big) q \Big (\boldsymbol {w} _ {i, j} \Big)\right), \end{array}
$$

which introduces the additional set of assumptions that $\mathbf { M } _ { i , k } \perp \perp \mathbf { M } _ { i , l } \vert \{ \mathbf { R } =$ r} and $\mathbf { U } _ { p , k } \perp \perp \mathbf { U } _ { p , l } \vert \{ \mathbf { R } = \pmb { r } \}$ further to those previously discussed. The details of the developments are given in Appendix $\mathsf { A } ,$ so here we will only show one example and comment on the relevant time complexity of the calculations, namely the weight $\pmb { \nu } _ { p } ,$ used to model user $p ^ { \prime } s$ preferences towards the items' latent representations.

Using the (generalized) variational Bayes machinery, $\mathbf { V } _ { p }$ is now modeled as a random variable with posterior distribution $q ( \pmb { \nu } _ { p } )$ which has the form of a multivariate Gaussian distribution, $q ( { \pmb v } _ { p } ) =$ $\mathcal { N } \left( \boldsymbol { \mu } _ { \boldsymbol { v } _ { p } } , \mathbf { Q } _ { \boldsymbol { v } _ { p } } ^ { - 1 } \right)$ , where

$$
\begin{array}{l} \mathbf {Q} _ {\boldsymbol {v} _ {p}} \leftarrow \tau \mathbf {I} + \mathbb {E} [ \Theta ] \sum_ {i \in \mathcal {I} (p)} \mathbb {E} \Big [ \mathbf {M} _ {i} \mathbf {M} _ {i} ^ {\mathrm{T}} \Big ] \\ \mu_ {\boldsymbol {v} _ {p}} \leftarrow \mathbf {Q} _ {\boldsymbol {v} _ {p}} ^ {- 1} \mathbb {E} [ \Theta ] \sum_ {i \in \mathcal {I} (p)} \mathbb {E} [ \mathbf {M} _ {i} ] \Big (\boldsymbol {r} (p, i) - \mathbb {E} \Big [ \mathbf {U} _ {p} \Big ] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] - \mathbb {E} [ \Psi_ {i} ] - \mathbb {E} \Big [ \Phi_ {p} \Big ] \Big). \end{array}\tag{4}
$$

As can be seen, the calculation of $\dot { \mu } _ { v _ { p } }$ strongly resembles the calculation of the point-estimate when using the EM algorithm $\left( \operatorname { E q . } \left( 2 \right) \right)$ ), but slightly simpli<sup>fi</sup>ed by utilizing that M is constrained to be independent of the other random variables in the posterior $q ( \pmb { u } , \pmb { m } , \pmb { \rho } )$ . The real bene<sup>fi</sup>t from a calculation point of view, though, is due to the simpli<sup>fi</sup>cations of the expectations coming into the calculations. Where the EMalgorithm using exact inference demanded that the covariance matrix over all latent variables was calculated to <sup>fi</sup>nd $\left\lceil \mathbf { M } _ { i } \mathbf { M } _ { i } ^ { \mathrm { T } } \right\rceil$ and $\vdots \left[ \mathbf { M } _ { i } \mathbf { U } _ { p } ^ { \mathrm { T } } \right]$ it is in the generalized mean-<sup>fi</sup>eld model suf<sup>fi</sup>cient to look at each latent vector at a time (as they are assumed to be independent a posteriori); $\mathbb { E } \left\lceil \mathbf { M } _ { i } \mathbf { M } _ { i } ^ { \mathrm { T } } \right\rceil$ can be found directly from the posterior variational distribution for $\mathbf { M } _ { i \cdot }$

Finally, the standard MF approach results in $\displaystyle \boldsymbol { l } \big ( \boldsymbol { \nu } _ { p , k } \big ) = \mathcal { N } \Big ( \boldsymbol { \mu } _ { \boldsymbol { \nu } _ { p , k } } , \boldsymbol { Q } _ { \boldsymbol { \nu } _ { p , k } } ^ { - 1 } \Big )$ where

$$
\begin{array}{l} Q _ {\boldsymbol {v} _ {p, k}} \leftarrow \tau + \mathbb {E} [ \Theta ] \sum_ {i \in \mathcal {I} (p)} \mathbb {E} \Big [ \mathsf {M} _ {i, k} ^ {2} \Big ] \\ \mu_ {\boldsymbol {v} _ {p, k}} \leftarrow Q _ {\boldsymbol {v} _ {p, k}} ^ {- 1} \mathbb {E} [ \Theta ] \sum_ {i \in \mathcal {I} (p)} \mathbb {E} \Big [ \mathbf {M} _ {i, k} \Big ] \Bigg (\boldsymbol {r} (p, i) - \mathbb {E} \Big [ \mathbf {U} _ {p} \Big ] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] - \mathbb {E} [ \Psi_ {i} ] - \mathbb {E} \Big [ \Phi_ {p} \Big ] \\ \qquad - \sum_ {\ell \neq k} \mathbb {E} \Big [ \mathbf {M} _ {i, \ell} \Big ] \mathbb {E} \Big [ \mathbf {V} _ {p, \ell} \Big ] \Bigg). \end{array}\tag{5}
$$

The logic behind the updating-rule remains the same, but the calculations are further simpli<sup>fi</sup>ed completely removing the need to invert matrices during the calculations. A Matlab implementation of the algorithm can be downloaded from http://people.cs.aau.dk/tdn/VB-CF/.

## 3.3. Parallelization

MapReduce [8,6] is a paradigm and framework to ef<sup>fi</sup>ciently distribute data-intensive calculations in parallel over multiple computational cores/CPUs. This parallelization is most ef<sup>fi</sup>cient when calculations are done concurrently and require no or little communication between the different calculation units. It has been shown [6] that Statistical

Query Models (SQMs) [17] <sup>fi</sup>t the MapReduce framework well. The mean-<sup>fi</sup>eld approximation described above lead to calculation steps as in Eq. (5), where – for a <sup>fi</sup>xed p – the calculations amount to calculations of (weighted) sums over subsets of the data. Parallelization is immediate with subsets of data being summarized at each computational core. This comes as no surprise as the mean-<sup>fi</sup>eld model is indeed an SQM. We have run our experiments on a con<sup>fi</sup>guration with relatively simple computational nodes (separate memory, shared disk). Here, data transfer and memory usage can be kept low by loading a separate subset of the data at each node, letting the mappers calculate the relevant statistics from that subset of the data, and having the reducer summarize the partial sums and <sup>fi</sup>nalize the calculations.

To see how this works in detail, assume that the rating data is separated into #Γ parts. Each part of the data is de<sup>fi</sup>ned as a sparse matrix over the same domain as the full data set would occupy, but holding only a subset of the ratings. For simplicity of notation, assume that the calculations are done on a cluster with #Γ cores, and that each core is able to hold its dedicated subset of the data in memory. When calculating $\mu _ { { \pmb v } _ { p , k } }$ in Eq. (5), we let each core γ calculate

$$
\begin{array}{l} \text { partial } (\gamma) \leftarrow \sum_ {i \in \mathcal {I} (p | \gamma)} \mathbb {E} \Big [ \mathbf {M} _ {i, k} \Big ] \Bigg (\boldsymbol {r} (p, i) \overline {{,}} - \mathbb {E} \Big [ \mathbf {U} _ {p} \Big ] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] - \mathbb {E} [ \Psi_ {i} ] - \mathbb {E} \Big [ \Phi_ {p} \Big ] \\ \quad - \sum_ {\ell \neq k} \mathbb {E} \Big [ \mathbf {M} _ {i, \ell} \Big ] \mathbb {E} \Big [ \mathbf {V} _ {p, \ell} \Big ] \Bigg) \end{array}
$$

where we use $\mathcal { T } ( p | \gamma )$ to signify the set of items that person p has rated in the data set held by core γ. Then, the reducer simply calculates

$$
\mu_ {\boldsymbol {v} _ {p, k}} \leftarrow Q _ {\boldsymbol {v} _ {p, k}} ^ {- 1} \mathbb {E} [ \Theta ] \sum_ {\gamma = 1} ^ {\# \Gamma} \text { partial } (\gamma),
$$

and the result is identical to Eq. (5). Similar parallelization is readily available for all the remaining learning rules of the recommender model.

Note that the quantities entering into the calculations are either scalars $( \mathbb { E } \big [ \mathbf { M } _ { i , \ell } \big ] , \mathbb { E } \big [ \mathbf { V } _ { p , \ell } \big ] , \mathbb { E } [ \Psi _ { i } ] , \mathbb { E } \big [ \Phi _ { p } \big ] , Q _ { { \boldsymbol { v } } _ { p , k } } , \mathbb { E } [ \Theta ] \big )$ or modestly sized vectors $( \mathbb { E } \big [ \mathbf { U } _ { p } \big ] , \mathbb { E } [ \mathbf { W } _ { i } ] )$ , and that the reducer step is computationally simple. The overhead due to the parallelization is therefore negligible, and in practice one will observe that the computational time is close to inversely proportional to #Γ. This is in contrast to the maximumlikelihood learning [20]: In that case, the reducer would have to calculate E $\left[ \mathbf { M } _ { i } \mathbf { U } _ { p } ^ { \mathrm { T } } \right]$ (see Eq. (2)). These expectations are found by calculating the inverse of the precision matrix containing all latent variables, which is a computationally daunting task.

## 4. Empirical results

In this section we will report on the results of the proposed collaborative <sup>fi</sup>ltering algorithm when run on a number of standard data sets. For the smaller data sets, where more computationally expensive straw-men can be employed, we will also report on those results for comparison.

## 4.1. Empirical setup

When learning the parameters of our model with a <sup>fi</sup>xed model structure, we use the MF learning scheme described in Section 3. For the results reported in this section, we terminated the algorithm when the relative increase in the likelihood bound was less than $1 0 ^ { - 5 }$ from one iteration to the next, or when the algorithm had run for 100 iterations. As we have already discussed, the GMF method is computationally more expensive than the standard MF. When learning a model using the generalized mean-<sup>fi</sup>eld method we therefore initialize the learning algorithm by <sup>fi</sup>rst learning a model using the MF algorithm, and then using the learned model as the starting-point for the GMF algorithm. Following this approach, GMF learning typically terminated after only 10–25 iterations.

Table 1  
Summary statistics for the data sets included in our study.

<table><tr><td>Name</td><td>#Ratings</td><td>#Users</td><td>#Items</td><td>Sparsity</td><td>Range</td></tr><tr><td>MovieLens 100k [15]</td><td>100.000</td><td>943</td><td>1.682</td><td>93.7%</td><td>1★-5★</td></tr><tr><td>MovieLens 1M [15]</td><td>1.000.209</td><td>6.040</td><td>3.952</td><td>95.8%</td><td>1★-5★</td></tr><tr><td>MovieLens 10M [15]</td><td>10.000.054</td><td>71.567</td><td>10.681</td><td>98.7%</td><td>1★-5★</td></tr><tr><td>Last.fm</td><td>92.834</td><td>1.892</td><td>18.745</td><td>98.4%</td><td>1★-5★</td></tr><tr><td>Jester [14]</td><td>4.136.630</td><td>73.421</td><td>100</td><td>43.7%</td><td>[-10,+10]</td></tr><tr><td>BookCrossing</td><td>433.671</td><td>77.805</td><td>185.973</td><td>99.9%</td><td>1★-10★</td></tr><tr><td>Yahoo!</td><td>717.872.016</td><td>1.823.179</td><td>136.736</td><td>99.7%</td><td>1★-5★</td></tr></table>

Deciding upon the model structure amounts to determining the number of latent variables to describe both users and items as well as the value for τ. When doing so, we used the same greedy strategy as described in [20]: The idea is to start from the simplest model structure, i.e., setting $| \mathbf { U } _ { p } | = 1 , | \mathbf { M } _ { i } | = 1$ , for all i and p, and setting $\tau = 1 . ^ { 3 } \tau$ τ is then gradually increased until the results, calculated using the wrapper approach, show that this is harmful for the predictive performance; for the experiments reported in this section we used four folds. Next we iteratively considered the neighboring models $( | \mathbf { U } _ { p } | = 2 , | \mathbf { M } _ { i } | = 1 )$ and $( | \mathbf { U } _ { p } | = 1 , | \mathbf { M } _ { i } | = 2 )$ in the same fashion, and at each step select the best scoring model as the current candidate model. When learning using the GMF algorithm, we <sup>fi</sup>rst use the standard MF algorithm for structure learning, and then use the GMF algorithm only to calculate the posterior over the <sup>fi</sup>xed structure.

## 4.2. The data sets

Before presenting the experimental results we <sup>fi</sup>rst give some summary statistics for the data sets used in the experiments, see Table 1. For each data set we report its most commonly used name together with the number of ratings, users, and items. We also report the sparsity level, calculated as the fraction of item-user combination not having a rating, as well as the range of legal ratings. For the latter, numbers post<sup>fi</sup>xed by stars denote integer ratings, whereas the interval for the Jester data set indicates real-valued ratings.

The MovieLens data sets [15] contain user supplied ratings of movies. There are three versions of the MovieLens data sets, namely MovieLens 100k, MovieLens 1M, and MovieLens 10M. The MovieLens 100k data set is supplied with <sup>fi</sup>ve prede<sup>fi</sup>ned folds for crossvalidation, and these folds were also used during testing. For the two other MovieLens sets, we have randomly partitioned the data sets in a training set with 80% of the ratings and a test set with the remaining 20% of the ratings.<sup>4</sup>

The Last.fm data set<sup>5</sup> documents the number of times a user of the Last.fm service has listened to different music artists. In its original form, the data set contains information about the social networking activities, tagging, and music listening information of the users. In order to use the data within our framework, we have made a stripped down and re-coded version of the data set, focusing only on the amount of time that a user has listened to a particular artist: For each user, the 10% of the artists that the user has listened to the least are rated with “One star”. The artists that appear between the 10% and 30% percentiles of the listening time are coded as “Two stars”. The artists with a listening time between the 30% and 70% percentiles are recoded as “Three stars”, and the artists the user have listened to from the 70% percentile and up to (and including) the 90% percentile are given “Four stars”. The artists above the 90% percentile are given “Five stars”. The encoding scheme introduces some particularities in the data. Firstly, all users have the same average rating and the same observed variance; in fact they have identical empirical distributions for their ratings. Secondly, the empirical distributions are symmetric; there are equally many ratings of one and <sup>fi</sup>ve stars and similarly for two and four stars. We note that the simple structure of the ratings does not give the proposed model an unfair advantage over the straw-men models as it, e.g., still explicitly tries to capture potential differences in the average ratings between users through the user offset $\phi _ { p } . ^ { 6 }$

The Jester data [14] contains ratings of jokes. This data set is not as sparse as the other data sets; 19.2% of the users have rated all the jokes, approximately 17% of the items have been rated by more than 90% of the users, and in total the sparsity level is 43.7%.

The original BookCrossing data set contains 1.149.780 ratings from 278.858 users with demographic information regarding a total of 271.379 books. For the empirical results reported in this paper, we have disregarded the demographic information. Further, the data set contains both explicit and implicit ratings. We have only considered the explicit ratings, leaving us with a smaller data set (see Table 1).

Finally, the Yahoo! data set contains users' ratings of songs. The data set also includes information about artist, album, and genre attributes, but this information has been disregarded for the experiments in the present paper.

## 4.3. Accuracy results

In the following subsections we report on the accuracy results of the models learned by the proposed algorithms using the data sets described above. For comparison we also evaluate the accuracy using the following straw-men methods:

Pearson (k) denotes a memory-based approach, where the predicted rating of the active item is calculated as a weighted sum of the ratings given to the k items deemed most important (measured using Pearson correlation) wrt. the active item [15].

Euclidean (k) is the k-nearest neighbors algorithm, where the distance is calculated using the Euclidean norm [24].

SVD (λ) performs a singular value decomposition, where λ is the regularization weight. For each setting of λ we ran experiments with the number of dimensions ranging from one to twenty-<sup>fi</sup>ve, and we present the best of these results here. Note that when choosing the number of dimensions based on the obtained results on the test set, we slightly favor the SVD algorithm over the other algorithms. Two options were considered for λ: λ = 0, resulting in a non-regularized model, and λ = 0.01 (as done by [30]). The learning was implemented with an adaptive learning rate. It was terminated when the relative improvement in error was lower than 10<sup>5</sup> or when the algorithm had run for 10.000 iterations.

The quality of recommendations is measured using the Mean Absolute Error (MAE). For the calculation of the MAE results in this section we rounded off the predicted ratings to the nearest integer value between one and <sup>fi</sup>ve as this slightly improved the results.

## 4.3.1. The MovieLens data sets

In addition to the straw-men methods listed above, we also compared the accuracy results with the collaborative <sup>fi</sup>ltering model learned using the method described in [20], denoted EM in Table 2.

The results for MovieLens 10k are shown in Table 2, where we see that both the regular and generalized mean-<sup>fi</sup>eld models outperform the straw-men models. The results in the scienti<sup>fi</sup>c literature are not directly comparable to ours, mainly because the experimental settings are different. Many researchers using the MovieLens 100k data set have made their own training and test sets without further documentation. However, the reported MAE values are typically about 0.73–0.74 or poorer [15,31,26,23,27,18,5,28,22,35] although results as low as 0.690 have also recently been reported [12]. See [20] for further discussion of the performance of these straw-men models.

The table shows the MAE results for the data sets MovieLens 100k, MovieLens 1M, and MovieLens 10M. Note that the values can only be compared vertically and not horizontally.

<table><tr><td rowspan="2"></td><td colspan="3">MovieLens</td></tr><tr><td>100k</td><td>1M</td><td>10M</td></tr><tr><td>Pearson (10)</td><td>0.7295</td><td>0.7433</td><td>-</td></tr><tr><td>Euclidean (10)</td><td>0.7446</td><td>0.7809</td><td>-</td></tr><tr><td>Pearson (25)</td><td>0.7080</td><td>0.7161</td><td>-</td></tr><tr><td>Euclidean (25)</td><td>0.7244</td><td>0.7532</td><td>-</td></tr><tr><td>Pearson (50)</td><td>0.7110</td><td>0.7046</td><td>-</td></tr><tr><td>Euclidean (50)</td><td>0.7328</td><td>0.7389</td><td>-</td></tr><tr><td>Pearson (all)</td><td>0.7122</td><td>0.7081</td><td>-</td></tr><tr><td>Euclidean (all)</td><td>0.7220</td><td>0.7229</td><td>-</td></tr><tr><td>SVD ( $\lambda = 0$ )</td><td>0.6916</td><td>0.6829</td><td>0.6223</td></tr><tr><td>SVD ( $\lambda = 0.01$ )</td><td>0.6869</td><td>0.6563</td><td>0.6099</td></tr><tr><td>EM</td><td>0.6848</td><td>-</td><td>-</td></tr><tr><td>MF</td><td>0.6745</td><td>0.6412</td><td>0.5953</td></tr><tr><td>GMF</td><td>0.6736</td><td>0.6412</td><td>0.5953</td></tr></table>

The data sets MovieLens 1M and 10M do not come with prede<sup>fi</sup>ned cross-validation folds and were instead randomly divided into two sets each: 80% for training and 20% for testing. The results of the comparison can also be seen in Table 2. For the MovieLens 10M data set we have only made a comparison based on SVD; the size of the data set makes direct use of the other straw-men models intractable.

Based on the MovieLens 10M data set, the mean-<sup>fi</sup>eld learning algorithm produced a model with two latent variables representing the users and nineteen latent variables representing the items; the prior precision was set to 100. In comparison, the best SVD model uses C = 15 dimensions; the SVD model was selected from a set of candidate models with dimensions {1,2,3,4,5,6,7,8,9,10,12,14,15,16,18,20}. The mean-<sup>fi</sup>eld model learned for the MovieLens 1M data set contains two latent variables representing users and 10 latent variables representing items.

## 4.3.2. The Last.fm, Jester, and BookCrossing data sets

Due to the relatively small size of the modi<sup>fi</sup>ed Last.fm data set we have been able to compare the proposed method with all the strawmen methods. On the other hand, we were only able to compare the results of the proposed method with that of SVD for the Jester and BookCrossing data sets. The results can be found in Table 3.

## Table 3

The tables shows the MAE results for the Last.fm, Jester and BookCrossing data sets. Note that MAE is not normalized wrt. the range of the ratings. The MAE values for Jester, which contains ratings between −10 and +10, are therefore larger than those for Last.fm (ranging from one to <sup>fi</sup>ve) and BookCrossing (between one and ten).

<table><tr><td></td><td>Last.fm</td><td>Jester</td><td>BookCrossing</td></tr><tr><td>Pearson (10)</td><td>0.8915</td><td>-</td><td>-</td></tr><tr><td>Euclidean (10)</td><td>0.9485</td><td>-</td><td>-</td></tr><tr><td>Pearson (25)</td><td>0.8664</td><td>-</td><td>-</td></tr><tr><td>Euclidean (25)</td><td>0.9291</td><td>-</td><td>-</td></tr><tr><td>Pearson (50)</td><td>0.8601</td><td>-</td><td>-</td></tr><tr><td>Euclidean (50)</td><td>0.9209</td><td>-</td><td>-</td></tr><tr><td>Pearson (all)</td><td>0.8547</td><td>-</td><td>-</td></tr><tr><td>Euclidean (all)</td><td>0.9131</td><td>-</td><td>-</td></tr><tr><td>SVD ( $\lambda = 0$ )</td><td>0.8405</td><td>3.3669</td><td>1.8362</td></tr><tr><td>SVD ( $\lambda = 0.01$ )</td><td>0.8460</td><td>3.2545</td><td>1.7813</td></tr><tr><td>MF</td><td>0.8077</td><td>3.1335</td><td>1.1576</td></tr><tr><td>GMF</td><td>0.8077</td><td>3.1191</td><td>1.1576</td></tr></table>

![](/api/attachments/KGD9DRDA/fulltext/images/455c6ce7a45e154bfd6413567499e970d3faa651f3136ac8d20b8f84bc1eb6f0.jpg)  
Fig. 2. Log–log plot of the comparison of the runtime between the mean-<sup>fi</sup>eld approach and the learning scheme described in [20]. The numbers relate to the MovieLens 100k data set [15]

## 4.3.3. The Yahoo data set

The size of the Yahoo! 700M music data set prohibit a full structural learning using the equipment at our disposal. Instead we have, somewhat arbitrarily, chosen to learn a regular mean-<sup>fi</sup>eld model with four latent variables for both the users and the items; in total the learned model contains approximately 7.7 million latent variables. The learned model provides an MAE of 0.7942 based on the prede<sup>fi</sup>ned training/ test set division. In comparison, the best MAE result reported by MyMediaLite [11] is 0.81445 using a factorized matrix approach<sup>7</sup>; due to the size of the data set we have not been able to compare the method with the other straw-men methods listed above.

## 4.4. Run-time performance

In this section we compare the run-time performance of the regular mean-<sup>fi</sup>eld implementation (that does not exploit the MapReduce architecture) with the EM-algorithm described in [20] based on the MovieLens 100k data set. The results of the comparison can be seen in Fig. 2, which shows a log–log plot of the learning time for sixteen different collaborative <sup>fi</sup>ltering models using the mean-<sup>fi</sup>eld approach as well as the EM-algorithm described in [20]. The sixteen different models vary in the number of latent variables (ranging from one to four) used to descried the users and the items in the domain. As can be seen from the <sup>fi</sup>gure, the mean-<sup>fi</sup>eld approach achieves a substantial performance improvement compared to the EM-algorithm, and, as demonstrated in Table 2, this improvement is obtained without a loss in precision.

## 4.5. Cold-start

In this section we investigate how vulnerable our model is to coldstart problems. For the investigation, we have used the MovieLens 100k data set with the pre-de<sup>fi</sup>ned cross-validation folds, but with the following changes: For each cross-validation iteration, we modify the training set by randomly removing all but κ ratings from one <sup>fi</sup>fth of the users (called the cold-start users). A model is then learned from this modi<sup>fi</sup>ed training set, and evaluated using MAE on the associated prede<sup>fi</sup>ned test set (retaining only the cold-start users). We repeat the process <sup>fi</sup>ve times to minimize the stochasticity of the results due to the random selection of which ratings to retain for the chosen users. Next, the process is repeated, by choosing a new set of cold-start users, and calculating the MAE for the <sup>fi</sup>ve models learned when their ratings are partly removed. We continue in this way a total of <sup>fi</sup>ve times, making sure that each user has been selected as a cold-start user exactly once. The MAE results from these 25 repetitions are averaged, and stored as the MAE on the <sup>fi</sup>rst cross-validation fold. The same procedure is then repeated for the other four folds, thus in total requiring 125 runs of the learning algorithm.

For each cross-validation fold, we chose the structure $( | \mathbf { U } _ { p } | , | \mathbf { M } _ { i } | , \tau )$ by structural learning. For simplicity, the structure was kept <sup>fi</sup>xed for all 25 replications inside one cross-validation fold, and was chosen to <sup>fi</sup>t the original data set, i.e., the data set we had prior to the removal of any ratings. The results aggregated over all <sup>fi</sup>ve cross-validation folds are reported in Fig. 3. On the x-axis we show κ, the number of ratings left in the training set for the cold-start-users. On the y-axis we give the cold-start efficiency, which for a particular κ value is de<sup>fi</sup>ned as the MAE of the full data set divided by the MAE obtained as above when the cold-start users had only κ ratings. An ef<sup>fi</sup>ciency close to one thus means that the system has been able to learn almost all the information available about the cold-start users using only κ of these users' ratings. The <sup>fi</sup>gure shows the results for the mean-<sup>fi</sup>eld algorithm in solid line with circular markers and the results of the SVD algorithm (dashed line and crosses). We note that not only does the mean-<sup>fi</sup>eld algorithm obtain better results for the whole data set (as reported in Table 2), it is also better suited for cold-start, with an ef<sup>fi</sup>ciency above 0.8 for = 1. The results for the generalized mean-<sup>fi</sup>eld model was similar to the results of the mean-<sup>fi</sup>eld model, but are omitted for clarity of the <sup>fi</sup>gure.

## 4.6. Summary of results

The <sup>fi</sup>rst thing to notice from the results reported in this section is that the latent variable model described in Section 2.2 consistently and signi<sup>fi</sup>cantly outperforms the collection of straw-men methods on a wide range of data sets (see Tables 2 and 3). Furthermore, strong results were documented in cold-start situations (Fig. 3). Three different algorithms for learning the latent variable model have been evaluated:

• The EM algorithm relies on exact inference and is described in [20] for the latent variable model considered in this paper. The computational complexity of this algorithm is, however, problematic when considering realistically sized data sets. In this paper it thus serves as a point of reference for the two approximate algorithms (MF and GMF) being proposed.

• The MF algorithm is an approximate inference algorithm that assumes that every latent variable is independent of all the other latent variables a posteriori. This assumption, which improves the run-time performance with several orders of magnitude (Fig. 2), violates the inherent modeling premises of the model. Still, as reported in

![](/api/attachments/KGD9DRDA/fulltext/images/29b9adb74cbf11ee9576593d6eccba895ba284926ee82cc6835649a147a22968.jpg)  
Fig. 3. Ef<sup>fi</sup>ciency vs κ for MF and SVD.

Table 2, this apparent inconsistency does not lead to a loss in precision. In fact, a small improvement is observed. One possible explanation for this is the regularization effect produced by the prior distributions over the model parameters, thus reducing the risk/effect of over-<sup>fi</sup>tting.

• The GMF alternative is a natural intermediate solution, where only some of the latent variables (namely those representing different aspects of a single item or person) are correlated a posteriori. The application of the GMF algorithm had only a modest impact on the results when compared to the MF approach, thus indicating that the extra modeling <sup>fl</sup>exibility was not signi<sup>fi</sup>cant when evaluated on the data sets we considered. On the other hand, its computational complexity is higher than that of the MF algorithm, because it requires inversion of matrices that are in general non-diagonal whereas the MF algorithm works with scalers (compare Eqs. (4) to (5)).

We conclude that out of the three approaches examined, the MF algorithm appears to <sup>fi</sup>nd the best balance between computational complexity and predictive ability for the data sets we have considered in this study.

## 5. Conclusion and future work

In this paper we have proposed two scalable algorithms for learning probabilistic collaborative <sup>fi</sup>ltering models that explicitly represents all users and items simultaneously [20]. The algorithms are based on the variational Bayes framework and differ in terms of the complexity of the variational distributions being applied. The computational complexity of the algorithms is linear in the number of ratings. Furthermore, both algorithms support a seamless parallel implementation that can easily be exploited in a MapReduce architecture. This allows for the processing of extremely large data sets, which we have illustrated by evaluating and comparing the algorithm based on the Yahoo 700M data set. The algorithms have also been evaluated on a collection of other publicly available collaborative <sup>fi</sup>ltering data sets and compared with well-known straw-men methods. The empirical results demonstrate that not only do the algorithms signi<sup>fi</sup>cantly outperform the straw-men methods, but we also observe a very favorable performance in cold-start scenarios. We observe only minor differences between the two algorithms wrt. prediction quality, and therefore do not <sup>fi</sup>nd support for selecting the computationally more complex algorithm (GMF) over its simpli<sup>fi</sup>ed counterpart (MF) in our analysis. In particular, the simpler version is recommended for use in big data situations.

As part of our future work, we are currently exploring methods for extending the model and the learning algorithm to also include content information about users and items. We expect that this type of information will be encoded using discrete variables, thus producing a particu lar type of hybrid probabilistic collaborative <sup>fi</sup>ltering model.

## Appendix A. Developments of variational Bayes inference

## A.1. Model definition

In this appendix we will derive the updating rules for the variational Bayes learning and inference algorithms.

The speci<sup>fi</sup>cation of the full generative model over (R, U, M) given the parameters $\pmb { \rho } = ( \pmb { \phi } , \pmb { \psi } , \pmb { \nu } , \pmb { w } , \theta )$ can be expressed as

$$
f (\boldsymbol {r}, \boldsymbol {u}, \boldsymbol {m} | \boldsymbol {\rho}) = f (\boldsymbol {r} | \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) f (\boldsymbol {m} | \boldsymbol {\rho}) f (\boldsymbol {u} | \boldsymbol {\rho}),
$$

where

$$
\begin{array}{l} f (\boldsymbol {r} | \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) = \prod_ {p = 1} ^ {\# U} \prod_ {i \in \mathcal {I} (p)} \sqrt {\frac {\theta}{2 \pi}} e x p \bigg (- \frac {\theta}{2} \left(\boldsymbol {r} (p, i) - \left(\boldsymbol {v} _ {p} ^ {\mathrm{T}} \boldsymbol {m} _ {i} + \boldsymbol {w} _ {p} ^ {\mathrm{T}} \boldsymbol {u} _ {p} + \phi_ {p} + \psi_ {i}\right)\right) ^ {2} \bigg) \\ f (\boldsymbol {m} _ {i} | \boldsymbol {\rho}) = \mathcal {N} (\boldsymbol {0} _ {\boldsymbol {s}}, \boldsymbol {I} _ {\boldsymbol {s} \times \boldsymbol {s}}) \\ f (\boldsymbol {u} _ {p} | \boldsymbol {\rho}) = \mathcal {N} (\boldsymbol {0} _ {t}, \boldsymbol {I} _ {t \times t}). \end{array}
$$

Further, in a Bayesian formulation of the problem, we give the following prior distributions to our parameters

$$
\begin{array}{l} f (\theta) = \text {Gamma} (a, b), \quad f (\psi_ {i}) = \mathcal {N} \left(\mu_ {\psi}, 1 / \kappa_ {\psi}\right), \quad f \left(\phi_ {p}\right) = \mathcal {N} \left(\mu_ {\phi}, 1 / \kappa_ {\phi}\right) \\ f (\boldsymbol {w} _ {i}) = \mathcal {N} (\boldsymbol {0} _ {\boldsymbol {s}}, 1 / \tau \cdot \mathbf {I} _ {\boldsymbol {s} \times \boldsymbol {s}}), \quad f \left(\boldsymbol {v} _ {p}\right) = \mathcal {N} (\boldsymbol {0} _ {t}, 1 / \tau \cdot \mathbf {I} _ {t \times t}). \end{array}
$$

This allows us to, in principle, calculate $f ( \pmb { u } , \pmb { m } , \rho | \pmb { r } )$ . Note that we have kept $\mu _ { \phi } = 0$ <sup>fi</sup>xed in the experiments reported in this paper.

## A.2. The generalized mean-field model

We will <sup>fi</sup>rst assume a full variational joint distribution of the form

$$
q (\boldsymbol {u}, \boldsymbol {m}, \boldsymbol {\rho}) = q (\theta) \prod_ {p = 1} ^ {\# U} q \left(\phi_ {p}\right) q \left(\boldsymbol {u} _ {p}\right) q \left(\boldsymbol {v} _ {p}\right) \prod_ {i = 1} ^ {\# M} q \left(\psi_ {i}\right) q \left(\boldsymbol {m} _ {i}\right) q \left(\boldsymbol {w} _ {i}\right),
$$

i.e., the distribution factors into terms so that, e.g., $\mathbf { M } _ { i } \perp \perp \mathbf { U } _ { p } | \mathbf { R } .$ On the other hand, note that ${ \bf M } _ { i , k } \perp / { \bf M } _ { i , l } | { \bf R } , \mathrm { e t c } .$

Based on Eq. (3), we get the following for M , where $i \in \{ 1 , . . . , \# M \}$ is <sup>fi</sup>xed:

$$
\log q (\boldsymbol {m} _ {i}) = \int_ {\boldsymbol {u}, \boldsymbol {m} _ {- i}, \boldsymbol {\rho}} q (\boldsymbol {u}, \boldsymbol {m} _ {- i}, \boldsymbol {\rho}) \log f (\boldsymbol {r}, \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) d \boldsymbol {u} d \boldsymbol {m} _ {- i} d \boldsymbol {\rho} + \text { const. },\tag{A.1}
$$

where m is used as a shorthand for the collection of all m with $j \neq i$ and u denotes the collection of all $\begin{array} { r } { { \pmb u } _ { p } , p = 1 , . . . , \# U . } \end{array}$

The integral can be expanded as:

$$
\begin{array}{l} \int_ {\boldsymbol {u}, \boldsymbol {m} _ {- i}, \boldsymbol {\rho}} q (\boldsymbol {u}, \boldsymbol {m} _ {- i}, \boldsymbol {\rho}) \log f (\boldsymbol {r}, \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) d \boldsymbol {u} d \boldsymbol {m} _ {- i} d \boldsymbol {\rho} \\ = \int_ {\boldsymbol {u}, \boldsymbol {m} _ {- i}, \boldsymbol {\rho}} q (\boldsymbol {u}, \boldsymbol {m} _ {- i}, \boldsymbol {\rho}) \sum_ {j = 1} ^ {\# M} \sum_ {p \in \mathcal {P} (j)} \log f (\boldsymbol {r} (p, j) | \boldsymbol {m} _ {j}, \boldsymbol {v} _ {p}, \boldsymbol {u} _ {p}, \boldsymbol {w} _ {j}, \phi_ {p}, \psi_ {j}, \theta) d \boldsymbol {u} d \boldsymbol {m} _ {- i} d \boldsymbol {\rho} \\ + \log f (\boldsymbol {m} _ {i}) + \text { const. } \\ = \int_ {\boldsymbol {u}, \boldsymbol {m} _ {- i}, \boldsymbol {\rho}} q (\boldsymbol {u}, \boldsymbol {m} _ {- i}, \boldsymbol {\rho}) \sum_ {p \in \mathcal {P} (j)} \log f (\boldsymbol {r} (p, i) | \boldsymbol {m} _ {i}, \boldsymbol {v} _ {p}, \boldsymbol {u} _ {p}, \boldsymbol {w} _ {i}, \phi_ {p}, \psi_ {i}, \theta) d \boldsymbol {u} d \boldsymbol {m} _ {- i} d \boldsymbol {\rho} \\ + \log f (\boldsymbol {m} _ {i}) + \text { const. }, \end{array}
$$

where the constant is used to continuously collect all terms that do not depend on m . Next, log $f ( \boldsymbol { r } ( p , i ) | m _ { i } , \boldsymbol { \nu } _ { p } , \boldsymbol { u } _ { p } , \boldsymbol { w } _ { i } , \phi _ { p } , \psi _ { i } , \theta )$ can be written as follows (when all terms not involving m are continuously collected into the constant):

$$
\begin{array}{l} \log f \Big (\boldsymbol {r} (p, i) | \boldsymbol {m} _ {i}, \boldsymbol {v} _ {p}, \boldsymbol {u} _ {p}, \boldsymbol {w} _ {i}, \phi_ {p}, \psi_ {i}, \theta \Big) \\ = - \frac {\theta}{2} \left(\boldsymbol {r} (p, i) - \left(\boldsymbol {m} _ {i} ^ {\mathrm{T}} \boldsymbol {v} _ {p} + \boldsymbol {u} _ {p} ^ {\mathrm{T}} \boldsymbol {w} _ {i} + \phi_ {p} + \psi_ {i}\right)\right) ^ {2} + \text { const. } \\ = - \frac {\theta}{2} \boldsymbol {m} _ {i} ^ {\mathrm{T}} \boldsymbol {v} _ {p} \boldsymbol {v} _ {p} ^ {\mathrm{T}} \boldsymbol {m} _ {i} + \theta \cdot \boldsymbol {m} _ {i} ^ {\mathrm{T}} \boldsymbol {v} _ {p} \left(\boldsymbol {r} (p, i) - \boldsymbol {u} _ {p} ^ {\mathrm{T}} \boldsymbol {w} _ {i} - \phi_ {p} - \psi_ {i}\right) + \text { const. } \end{array}\tag{A.2}
$$

Consider now an r-dimensional Gaussian variable $\pmb { X } \sim \mathcal { N } \Big ( \pmb { \mu } , \pmb { 0 } ^ { - 1 } \Big )$ where μ is the expected value and Q is the inverse variance, or precision. By simple calculation, and letting all terms that are not depending on x continuously disappear into the constant, we <sup>fi</sup>nd that

$$
\begin{array}{l} \log f (\boldsymbol {x} | \boldsymbol {\mu}, \boldsymbol {Q}) = \log \bigg ((2 \pi) ^ {r / 2} | \boldsymbol {Q} | ^ {1 / 2} e x p \bigg (- \frac {1}{2} (\boldsymbol {x} - \boldsymbol {\mu}) ^ {\mathrm{T}} \boldsymbol {Q} (\boldsymbol {x} - \boldsymbol {\mu}) \bigg) \bigg) \\ = - \frac {1}{2} (\boldsymbol {x} - \boldsymbol {\mu}) ^ {\mathrm{T}} \boldsymbol {Q} (\boldsymbol {x} - \boldsymbol {\mu}) + \text { const. } \\ = - \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {x} + \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {\mu} + \text { const. } \end{array}\tag{A.3}
$$

Since $\mathbf { M } _ { i } \sim \mathcal { N } ( \mathbf { 0 } _ { s } , I _ { s \times s } )$ , it follows that log $\begin{array} { r } { f ( \pmb { m } _ { i } ) = - \frac { 1 } { 2 } \pmb { m } _ { i } ^ { T } \pmb { m } _ { i } + \mathrm { c o n s t } . } \end{array}$ Utilizing $\operatorname { E q . } ( \mathsf { A . 2 } )$ , the integral in Eq. (A.1) can therefore be written as

$$
\begin{array}{l} \log q (\boldsymbol {m} _ {i}) = - \frac {1}{2} \boldsymbol {m} _ {i} ^ {\mathrm{T}} \left(\mathbf {I} + \mathbb {E} [ \Theta ] \sum_ {p \in \mathcal {P} (i)} \mathbb {E} \left[ \mathbf {V} _ {p} \mathbf {V} _ {p} ^ {\mathrm{T}} \right]\right) \boldsymbol {m} _ {i} \\ \quad + \mathbb {E} [ \Theta ] \boldsymbol {m} _ {i} ^ {\mathrm{T}} \left(\sum_ {p \in \mathcal {P} (i)} \mathbb {E} \left[ \mathbf {V} _ {p} \right] \left(\boldsymbol {r} (p, i) - \mathbb {E} \left[ \mathbf {U} _ {p} \right] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] - \mathbb {E} \left[ \Phi_ {p} \right] - \mathbb {E} [ \Psi_ {i} ]\right)\right) \\ \quad + \text { const. } \end{array}
$$

Comparing the terms of Eq. (A.4) with those of Eq. (A.3), we <sup>fi</sup>nd that $q ( \pmb { m } _ { i } )$ must be a Gaussian with precision

$$
\mathbf {Q} _ {\boldsymbol {m} _ {i}} = \mathbf {I} + \mathbb {E} [ \boldsymbol {\Theta} ] \sum_ {p \in \mathcal {P} (i)} \mathbb {E} \left[ \mathbf {V} _ {p} \mathbf {V} _ {p} ^ {\mathrm{T}} \right]
$$

and expectation

$$
\mathbf {Q} _ {\boldsymbol {m} _ {i}} ^ {- 1} \mathbb {E} [ \Theta ] \sum_ {p \in \mathcal {P} (i)} \mathbf {V} _ {p} \Big (\boldsymbol {r} (p, i) - \mathbb {E} \Big [ \mathbf {U} _ {p} \Big ] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] - \mathbb {E} \Big [ \Phi_ {p} \Big ] - \mathbb {E} [ \Psi_ {i} ] \Big).
$$

Using the same procedure as above we <sup>fi</sup>nd that $q ( \pmb { \nu } _ { p } )$ also has the form of a multivariate Gaussian distribution, $q ( \pmb { \nu } _ { p } ) = \mathcal { N } \Big ( \mu _ { \pmb { \nu } _ { p } } , \mathbf { Q } _ { \pmb { \nu } _ { p } } ^ { - 1 } \Big )$ where

$$
\begin{array}{l} \mathbf {Q} _ {\mathbf {v} _ {p}} = \tau \mathbf {I} + \mathbb {E} [ \Theta ] \sum_ {i \in \mathcal {I} (p)} \mathbb {E} \left[ \mathbf {M} _ {i} \mathbf {M} _ {i} ^ {\mathrm{T}} \right]; \\ \mu_ {\mathbf {v} _ {p}} = \mathbf {Q} _ {\mathbf {v} _ {p}} ^ {- 1} \mathbb {E} [ \Theta ] \sum_ {i \in \mathcal {I} (p)} \mathbb {E} [ \mathbf {M} _ {i} ] \left(\boldsymbol {r} (p, i) - \mathbb {E} \left[ \mathbf {U} _ {p} \right] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] - \mathbb {E} \left[ \Phi_ {p} \right] - \mathbb {E} [ \Psi_ {i} ]\right). \end{array}
$$

Similar update rules are obtained for $q ( { \pmb u } _ { p } )$ and $q ( \mathbf { w } _ { i } )$

Next, we move on to $\Psi _ { i } ,$ which can be interpreted as the a priori rating for item i. In our Bayesian formulation, $\Psi _ { i } \sim \mathcal { N } \Big ( \mu _ { \psi } , \kappa _ { \psi } ^ { - 1 } \Big )$ , where $\mu _ { \psi }$ and $\kappa _ { \psi }$ are the hyper-parameters, denoting the expectation and precision, respectively. Starting again from Eq. (3) we have that

$$
\begin{array}{l} \log q (\psi_ {i}) = \int_ {\boldsymbol {u}, \boldsymbol {m}, \theta , \boldsymbol {\phi}, \boldsymbol {\psi} _ {- i}} q (\boldsymbol {u}, \boldsymbol {m}, \theta , \boldsymbol {\phi}, \boldsymbol {\psi} _ {- i}) \log f (\boldsymbol {r}, \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) d \boldsymbol {u} d \boldsymbol {m} d \theta d \boldsymbol {\phi} d \boldsymbol {\psi} _ {- i} \\ + \text { const. } \end{array}
$$

As before we expand the integral, and simplify by continuously moving all terms not depending on ψ<sub>i</sub> into the constant:

$$
\begin{array}{l} \int_ {\boldsymbol {u}, \boldsymbol {m}, \theta , \boldsymbol {\phi}, \boldsymbol {\psi} _ {- i}} q (\boldsymbol {u}, \boldsymbol {m}, \theta , \boldsymbol {\phi}, \boldsymbol {\psi} _ {- i}) l o g [ f (\boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) f (\boldsymbol {r} | \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) ] d \boldsymbol {u} d \boldsymbol {m} d \theta d \boldsymbol {\phi} d \boldsymbol {\psi} _ {- i} \\ = l o g f (\psi_ {i}) + \int_ {\boldsymbol {u}, \boldsymbol {m}, \theta , \boldsymbol {\phi}, \boldsymbol {\psi} _ {- i}} q (\boldsymbol {u}) q (\boldsymbol {m}) q (\theta) q (\boldsymbol {\phi}) q (\boldsymbol {\psi} _ {- i}) \cdot \\ \frac {\theta}{2} \sum_ {p \in \mathcal {P} (i)} \left(\mathbf {r} (p, i) - \left(\mathbf {m} _ {i} ^ {\mathrm{T}} \mathbf {v} _ {p} + \mathbf {u} _ {p} ^ {\mathrm{T}} \mathbf {w} _ {i} + \phi_ {p} + \psi_ {i}\right)\right) ^ {2} d \boldsymbol {u} d \boldsymbol {m} d \theta d \boldsymbol {\phi} d \boldsymbol {\psi} _ {- i} + c o n s t. \\ = l o g f (\psi_ {i}) - \frac {\mathbb {E} [ \Theta ]}{2} \sum_ {p \in \mathcal {P} (i)} \left[ 2 \psi_ {i}   \mathbb {E} [ \mathbf {M} _ {i} ] ^ {\mathrm{T}}   \mathbb {E} [ \mathbf {V} _ {p} ] + 2 \psi_ {i}   \mathbb {E} [ \mathbf {U} _ {p} ] ^ {\mathrm{T}}   \mathbb {E} [ \mathbf {W} _ {i} ] + 2 \psi_ {i}   \mathbb {E} [ \phi_ {p} ] + \psi_ {i} ^ {2} - 2 r (p, i)   \psi_ {i} \right] + c o n s t. \end{array}
$$

Thus, we get

$$
\begin{array}{l} \log q (\psi_ {i}) = - \frac {1}{2} \psi_ {i} ^ {2} \Big (\kappa_ {\psi} + | \mathcal {P} (i) | \mathbb {E} [ \Theta ] \Big) \\ \qquad + \psi_ {i}   \mathbb {E} [ \Theta ] \sum_ {p \in \mathcal {P} (i)} \Big (\boldsymbol {r} (p, i) - \mathbb {E} [ \mathbf {M} _ {i} ] ^ {\mathrm{T}} \mathbb {E} \Big [ \mathbf {V} _ {p} \Big ] - \mathbb {E} \Big [ \mathbf {U} _ {p} \Big ] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] - \mathbb {E} \Big [ \phi_ {p} \Big ] \Big) \\ \qquad + \psi_ {i}   \kappa_ {\psi} \mu_ {\psi} + \text { const. } \end{array}\tag{A.4}
$$

Comparing Eqs. (A.4) to (A.3), we recognize that $q \left( \psi _ { i } \right)$ is a Gaussian with mean $\mu _ { \psi _ { i } }$ and variance $\sigma _ { \psi _ { i } } ^ { 2 }$ , where:

$$
\begin{array}{l} \sigma_ {\psi_ {i}} ^ {2} = 1 / \Big (\kappa_ {\psi} + | \mathcal {P} (i) | \mathbb {E} [ \Theta ] \Big); \\ \mu_ {\psi_ {i}} = \sigma_ {\psi_ {i}} ^ {2} \left(\kappa_ {\psi} \mu_ {\psi} + \mathbb {E} [ \Theta ] \sum_ {p \in \mathcal {P} (i)} \left(\boldsymbol {r} (p, i) - \mathbb {E} [ \mathbf {M} _ {i} ] ^ {\mathrm{T}} \mathbb {E} \left[ \mathbf {V} _ {p} \right] - \mathbb {E} \left[ \mathbf {U} _ {p} \right] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] - \mathbb {E} \left[ \Phi_ {p} \right]\right)\right). \end{array}
$$

Using the same procedure, we also <sup>fi</sup>nd that $q \left( \phi _ { p } \right)$ is a Gaussian distribution. We utilize that $\phi _ { p }$ has a priori mean $\mu _ { \phi } = 0$ to simplify the results slightly, and obtain that

$$
\begin{array}{l} \sigma_ {\phi_ {p}} ^ {2} = 1 / \Big (\kappa_ {\phi} + | \mathcal {I} (p) | \mathbb {E} [ \Theta ] \Big); \\ \mu_ {\phi_ {p}} = \sigma_ {\phi_ {p}} ^ {2}   \mathbb {E} [ \Theta ] \sum_ {i \in \mathcal {I} (p)} \Big (\boldsymbol {r} (p, i) - \mathbb {E} [ \mathbf {M} _ {i} ] ^ {\mathrm{T}} \mathbb {E} \Big [ \mathbf {V} _ {p} \Big ] - \mathbb {E} \Big [ \mathbf {U} _ {p} \Big ] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] - \mathbb {E} [ \Psi_ {i} ] \Big). \end{array}
$$

Lastly, the distribution for the precision, $q \left( \theta \right)$ is to be calculated. The prior distribution of Θ is assumed to be a Gamma distribution with hyper-parameters a and b:

$$
f (\theta) = \frac {b ^ {a}}{\Gamma (a)} \theta^ {a - 1} e x p (- b \theta).
$$

As usual, we start from $\operatorname { E q . } \left( 3 \right)$ and obtain that

$$
\begin{array}{l} \log q (\theta) \\ = \int_ {\boldsymbol {u}, \boldsymbol {m}, \boldsymbol {\phi}, \boldsymbol {\psi}} q (\boldsymbol {u}, \boldsymbol {m}, \boldsymbol {\phi}, \boldsymbol {\psi}, \theta) \log f (\boldsymbol {r}, \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\phi}, \boldsymbol {\psi}, \theta) d \boldsymbol {u} d \boldsymbol {m} d \boldsymbol {\phi} d \boldsymbol {\psi} + \text { const. } \\ = \log f (\theta) + \int_ {\boldsymbol {u}, \boldsymbol {m}, \boldsymbol {\phi}, \boldsymbol {\psi}} q (\boldsymbol {u}) q (\boldsymbol {m}) q (\phi) q (\psi). \\ \sum_ {i = 1} ^ {\# M} \sum_ {p \in \mathcal {P} (i)} \log f \Big (\boldsymbol {r} (p, i) | \boldsymbol {m} _ {i}, \boldsymbol {v} _ {p}, \boldsymbol {u} _ {p}, \boldsymbol {w} _ {i}, \phi_ {p}, \psi_ {i}, \theta \Big) d \boldsymbol {u} d \boldsymbol {m} d \boldsymbol {\phi} d \boldsymbol {\psi} + \text { const. } \end{array}
$$

Next, observe that when # Obs is de<sup>fi</sup>ned as the total number of observed ratings,

$$
\begin{array}{l} \log f (\mathbf {r} | \mathbf {m}, \mathbf {u}, \rho) \\ = \log \left(\prod_ {p = 1} ^ {\# U} \prod_ {i \in \mathcal {I} (p)} \sqrt {\frac {\theta}{2 \pi}} \exp \left(- \frac {\theta}{2} (\mathbf {r} (p, i) - (\mathbf {v} _ {p} ^ {T} \mathbf {m} _ {i} + \mathbf {w} _ {i} ^ {T} \mathbf {u} _ {p} + \phi_ {p} + \psi_ {i})) ^ {2}\right)\right) \\ = \frac {\# \text {Obs}}{2} \log (\theta) - \frac {\theta}{2} \left(\mathbf {r} (p, i) - \left(\mathbf {m} _ {i} ^ {T} \mathbf {v} _ {p} + \mathbf {u} _ {p} ^ {T} \mathbf {w} _ {i} + \phi_ {p} + \psi_ {i}\right)\right) ^ {2} + \text {const.}, \end{array}
$$

where the constant includes all terms not involving θ. Similarly, observe that

$$
\begin{array}{c} \log f (\theta) = a \log (b) - \log (\Gamma (a)) + (a - 1) \log (\theta) - b \theta \\ = (a - 1) \log (\theta) - b \theta + \text { const. } \end{array}\tag{A.5}
$$

It follows that

$$
\begin{array}{l} \log q (\theta) = \log (\theta) \left(a - 1 + \frac {\# \text { Obs }}{2}\right) \\ \quad - \theta \left(b + \frac {1}{2} \sum_ {p = 1} ^ {\# U} \sum_ {i \in \mathcal {I} (p)} \mathbb {E} \left(\boldsymbol {r} (p, i) - \mathbf {U} _ {p} ^ {\mathrm{T}} \mathbf {W} _ {i} - \mathbf {M} _ {i} ^ {\mathrm{T}} \mathbf {V} _ {p} - \Phi_ {p} - \Psi_ {i}\right) ^ {2}\right) + \text { const }., \end{array}
$$

and by comparing this expression with the Gamma distribution $\left( \operatorname { E q . } \left( \mathsf { A . 5 } \right) \right)$ we <sup>fi</sup>nd that q(θ) is a Gamma distribution with parameters:

$$
\begin{array}{l} a ^ {*} = a + \frac {\# \text {Obs}}{2} \\ b ^ {*} = b + \frac {1}{2} \sum_ {p = 1} ^ {\# U} \sum_ {i \in \mathcal {I} (p)} \mathbb {E} \bigg [ \Big (\boldsymbol {r} (p, i) - \mathbf {U} _ {p} ^ {\mathrm{T}} \mathbf {W} _ {i} - \mathbf {M} _ {i} ^ {\mathrm{T}} \mathbf {V} _ {p} - \Phi_ {p} - \Psi_ {i} \Big) ^ {2} \bigg ]. \end{array}
$$

The convergence of the iterative learning scheme is controlled by monitoring the lower-bound of the marginal likelihood of the data, de<sup>fi</sup>ned by ${ \mathcal { F } } ( q ) = { \mathcal { H } } ( q ) + \mathbb { E } _ { ( q ) } [ l o g f ( r , m , \pmb { u } , \pmb { \rho } )$ , where $\mathcal { H } ( q )$ is the entropy of the variational distribution. The calculation of this lower-bound is straightforward given the developments above.

## A.3. Standard mean-field

The developments of the previous subsection were based on the assumption that the variational approximation factorizes according to

$$
q (\boldsymbol {u}, \boldsymbol {m}, \boldsymbol {\rho}) = q (\theta) \prod_ {p = 1} ^ {\# U} q \left(\phi_ {p}\right) q \left(\boldsymbol {u} _ {p}\right) q \left(\boldsymbol {v} _ {p}\right) \prod_ {i = 1} ^ {\# M} q \left(\psi_ {i}\right) q \left(\boldsymbol {m} _ {i}\right) q \left(\boldsymbol {w} _ {i}\right).
$$

We now take this one step further, assuming that the full joint $q ( \pmb { u } , \pmb { m } , \pmb { \rho } )$ has the form

$$
\begin{array}{l} q (\boldsymbol {u}, \boldsymbol {m}, \boldsymbol {\rho}) = q (\theta) \prod_ {p = 1} ^ {\# U} \left(q \Big (\phi_ {p} \Big) \prod_ {j = 1} ^ {| U _ {p} |} q \Big (\boldsymbol {u} _ {p, j} \Big)   q \Big (\boldsymbol {v} _ {p, j} \Big)\right) \\ \qquad \times \prod_ {i = 1} ^ {\# M} \left(q (\psi_ {i}) \prod_ {j = 1} ^ {| M _ {i} |} q \Big (\boldsymbol {m} _ {i, j} \Big)   q \Big (\boldsymbol {w} _ {i, j} \Big)\right), \end{array}
$$

which introduces the set of additional assumptions that $\mathbf { M } _ { i , k } \perp \perp \mathbf { M } _ { i , l } \vert \mathbf { R }$ and $\mathbf { U } _ { p , k } \perp \perp \mathbf { U } _ { p , l } \vert \mathbf { R }$ in addition to those previously discussed. It turns out that these additional assumptions simplify the calculations of the approximate posteriors for $\mathbf { M } _ { i } , \mathbf { U } _ { p } , \mathbf { W } _ { i } ,$ , and $\mathbf { V } _ { p }$ even further, while the developments for $\Phi _ { p } , \Psi _ { i }$ , and Θ remain unchanged.

Let us consider how to calculate $q ( \pmb { m } _ { i , k } )$ , i.e., the distribution of the kth element of the latent vector describing item i. Starting from $\operatorname { E q . } \left( 3 \right)$ , we need to calculate the expectation of log f(r, u, m, ρ) wrt. all random variables except $\mathbf { M } _ { i , k } .$ Continuously collecting all terms that are independent of ${ \bf { m } } _ { i , k }$ into the constant, and using the shorthand ${ \pmb { m } } _ { - i k }$ for the collection of all m-variables except ${ \bf { m } } _ { i , k } ,$ , we obtain

$$
\begin{array}{l}\log q (\boldsymbol {m} _ {i, k})\\= \int_ {\boldsymbol {u}, \boldsymbol {m} _ {- i k}, \boldsymbol {\rho}} q (\boldsymbol {u}, \boldsymbol {m} _ {- i k}, \boldsymbol {\rho}) \log f (\boldsymbol {r}, \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) d \boldsymbol {u} d \boldsymbol {m} _ {- i k} d \boldsymbol {\rho} + \text {const.}\\= \int_ {\boldsymbol {u}, \boldsymbol {m} _ {- i k}, \boldsymbol {\rho}} q (\boldsymbol {u}, \boldsymbol {m} _ {- i k}, \boldsymbol {\rho}) \sum_ {p \in \mathcal {P} (i)} \log f (\boldsymbol {r} (p, i) | \boldsymbol {m}, \boldsymbol {u}, \boldsymbol {\rho}) d \boldsymbol {u} d \boldsymbol {m} _ {- i k} d \boldsymbol {\rho}\\+ \log f (\boldsymbol {m} _ {i, k}) + \text {const.}\\= - \frac {1}{2} \boldsymbol {m} _ {i, k} ^ {2} \left(1 + \mathbb {E} [ \Theta ] \sum_ {p \in \mathcal {P} (i)} \mathbb {E} [ \mathbf {V} _ {p, j} ^ {2} ]\right)\\+ \boldsymbol {m} _ {i, k} \mathbb {E} [ \Theta ] \sum_ {p \in \mathcal {P} (i)} \mathbb {E} [ \mathbf {V} _ {p, j} ] \left(\boldsymbol {r} (p, i) - \mathbb {E} [ \mathbf {U} _ {p} ] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] \right.\\- \sum_ {\ell \neq k} \mathbb {E} [ \mathbf {M} _ {i, \ell} ] \mathbb {E} [ \mathbf {V} _ {p, \ell} ] - \mathbb {E} [ \Phi_ {p} ] - \mathbb {E} [ \Psi_ {i} ]\left. \right)\\+ \text {const.}\end{array}
$$

Again, we <sup>fi</sup>nd that ${ q } ( { \pmb m } _ { i , k } )$ must be a Gaussian, this time with parameters

$$
\begin{array}{l} \sigma_ {\boldsymbol {m} _ {i, k}} ^ {2} = \left(1 + \mathbb {E} [ \Theta ] \sum_ {p \in \mathcal {P} (i)} \mathbb {E} \Big [ \mathbf {V} _ {p, k} ^ {2} \Big ]\right) ^ {- 1}; \\ \mu_ {\boldsymbol {m} _ {i, k}} = \sigma_ {\boldsymbol {m} _ {i, k}} ^ {2} \mathbb {E} [ \Theta ] \sum_ {p \in \mathcal {P} (i)} \mathbb {E} \Big [ \mathbf {V} _ {p, k} \Big ] \left(\boldsymbol {r} (p, i) - \mathbb {E} \Big [ \mathbf {U} _ {p} \Big ] ^ {\mathrm{T}} \mathbb {E} [ \mathbf {W} _ {i} ] \right. \\ \left. - \sum_ {\ell \neq k} \mathbb {E} \Big [ \mathbf {M} _ {i, \ell} \Big ] \mathbb {E} \Big [ \mathbf {V} _ {i, \ell} \Big ] - \mathbb {E} \Big [ \Phi_ {p} \Big ] - \mathbb {E} [ \Psi_ {i} ]\right). \end{array}
$$

In the previous sub-section we found that the variance of $q ( \pmb { m } _ { i } )$ was given by $\begin{array} { r } { \left( \mathbf { I } + \mathbb { E } [ \Theta ] \sum _ { p \in \mathcal { P } ( i ) } \mathbb { E } [ \mathbf { V } _ { p } ] \mathbb { E } \big [ \mathbf { V } _ { p } ^ { \mathrm { T } } \big ] \right) ^ { - 1 } } \end{array}$ , hence the inversion of one $s \times s$ matrix (per item) was required to calculate the variational approximation. The matrixes are not diagonal in general, so if #M is large, the computational savings of the present result can be noteworthy, even for small values of s.

Using the same procedure as above we <sup>fi</sup>nd that $q ( \pmb { \nu } _ { p , k } )$ also has the form of a multivariate Gaussian distribution, $q ( \pmb { \nu } _ { p , k } ) = \mathcal { N } \Big ( \mu _ { \pmb { \nu } _ { p , k } } , \mathbf { Q } _ { \pmb { \nu } _ { p , k } } ^ { - 1 } \Big )$ , where $\begin{array} { r } { Q _ { \pmb { \nu } _ { p , k } } = \tau + \mathbb { E } [ \Theta ] \sum _ { i \in \mathcal { I } ( p ) } \mathbb { E } \left[ \mathbf { M } _ { i , k } ^ { 2 } \right] } \end{array}$ and $\begin{array} { r } { \boldsymbol { \mu } _ { \pmb { \nu } _ { p , k } } = Q _ { \pmb { \nu } _ { p , k } } ^ { - 1 } \mathbb { E } [ \Theta ] \sum _ { i \in \mathcal { I } ( p ) } \mathbb { E } \big [ \mathbf { M } _ { i , k } \big ] } \end{array}$ $( \pmb { r } ( p , i ) - \mathbb { E } \big [ \pmb { \mathsf { U } } _ { p } \big ] ^ { \mathrm { T } } \mathbb { E } [ \pmb { \mathsf { W } } _ { i } ] - \sum _ { \ell \neq k } \mathbb { E } \big [ \pmb { \mathsf { M } } _ { i , \ell } \big ] \mathbb { E } \big [ \pmb { \mathsf { V } } _ { i , \ell } \big ] - \mathbb { E } \big [ \Phi _ { p } \big ] - \mathbb { E } [ \Psi _ { i } ] \big )$

$$
q (\boldsymbol {u} _ {p, k})
$$

$$
q (\boldsymbol {w} _ {i, k})
$$

## References

[1] H. Attias, A variational Bayesian framework for graphical models, Advances in Neural Information Processing Systems 12 (1–2) (2000) 209–215.

[2] M.J. Beal, Variational algorithms for approximate Bayesian inference(Ph.D. thesis) Gatsby Computational Neuroscience Unit, University College London, 2003.

[3] M.J. Beal, Z. Ghahramani, Variational Bayesian learning of directed graphical models with hidden variables, Bayesian Analysis 1 (4) (2006) 793–831.

[4] J.S. Breese, D. Heckerman, C. Kadie, Empirical analysis of predictive algorithms for collaborative <sup>fi</sup>ltering, Proceedings of the Fourteenth Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, Morgan Kaufmann Publishers 1998, pp. 43–52.

[5] J. Chen, J. Yin, Recommendation based on in<sup>fl</sup>uence sets, Proceedings of the Workshop on Web Mining and Web Usage Analysis, 2006.

[6] C.T. Chu, S.K. Kim, Y.A. Lin, Y. Yu, G.R. Bradski, A.Y. Ng, K. Olukotun, Map-Reduce for machine learning on multicore, in: B. Schölkopf LC. Platt T. Hoffman (Eds.). Advances in Neural Information Processing Systems, 19, MIT Press 2006, pp. 281–288.

[7] L.M. de Campos, J.M. Fernández-Luna, J.F. Huete, M.A. Rueda-Morales, Managing uncertainty in group recommending processes, User Modeling and User-Adapted Interaction 19 (2009) 207–242.

[8] J. Dean, S. Ghemawat, MapReduce: simpli<sup>fi</sup>ed data processing on large clusters, Proceedings of the 6th Conference on Symposium on Operating Systems Design & Implementation, vol. 6, USENIX Association 2004, pp. 137–150.

[9] A.P. Dempster, N.M. Laird, D.B. Rubin, Maximum likelihood from incomplete data via the EM algorithm, Journal of the Royal Statistical Society, Series B 39 (1977) 1-38

[10] R. Duda, P. Hart, D. Stork, Pattern classi<sup>fi</sup>cation, Wiley Interscience, 2001.

[11] Z. Gantner, S. Rendle, C. Freudenthaler, L. Schmidt-Thieme, MyMediaLite, Proceedings of the <sup>fi</sup>fth ACM conference on Recommender systems — RecSys '11, ACM Press, New York, New York, USA Oct. 2011, p. 305 (URL http://dl.acm.org/citation. cfm?id=2043932.2043989).

[12] K. Georgiev, P. Nakov, A non-IID framework for collaborative <sup>fi</sup>ltering with restricted Boltzmann machines, in: S. Dasgupta, D. Mcallester (Eds.),Proceedings of the 30th International Conference on Machine Learning (ICML-13), JMLR Workshop and Conference Proceedings, vol. 28 May 2013, pp. 1148–1156 (URL http://jmlr. org/proceedings/papers/v28/georgiev13.pdf).

[13] L. Getoor, B. Taskar, Introduction to statistical relational learning (adaptive computation and machine learning), The MIT Press, 2007.

[14] K. Goldberg, T. Roeder, D. Gupta, C. Perkins, Eigentaste: a constant time collaborative <sup>fi</sup>ltering algorithm, Information Retrieval 4 (2002) 133–151.

[15] J. Herlocker, J. Konstan, A. Borchers, J. Riedl, An algorithmic framework for performing collaborative <sup>fi</sup>ltering, Proceedings of the ACM 1999 Conference on Research and Development in Information Retrieval 1999, pp. 230–237.

[16] M.I. Jordan, Z. Ghahramani, T.S. Jaakkola, L.K. Saul, An introduction to variational methods for graphical models, Machine Learning 37 (1999) 183–233.

[17] M. Kearns, Ef<sup>fi</sup>cient noise-tolerant learning from statistical queries, Journal of the ACM 45 (6) (1998) 983–1006.

[18] D. Kim, B.-J. Yum, Collaborative <sup>fi</sup>ltering based on iterative principal component analysis, Expert Systems with Applications 28 (4) (2005) 823–830.

[19] H.-N. Kim, A. El-Saddik, G.-S. Jo, Collaborative error-re<sup>fl</sup>ected models for cold-start recommender systems, Decision Support Systems 51 (3) (Jun. 2011) 519–531.

[20] H. Langseth, T.D. Nielsen, A latent model for collaborative <sup>fi</sup>ltering, International Journal of Approximate Reasoning 53 (4) (June 2012) 447–466.

[21] S.L. Lauritzen, Propagation of probabilities, means and variances in mixed graphical association models, Journal of the American Statistical Association 87 (420) (1992) 1098–1108.

[22] G. Lekakos, P. Caravelas, A hybrid approach for movie recommendation, Multimedia Tools and Applications 36 (2008) 5570.

[23] Q. Li, B.M. Kim, Clustering approach for hybrid recommender system, WI '03: Proceedings of the 2003 IEEE/WIC International Conference on Web Intelligence, IEEE Computer Society, Washington, DC, USA 2003, pp. 33–38.

[24] B. Marlin, Collaborative <sup>fi</sup>ltering: a machine learning perspective(Master of Science Thesis) Graduate Department of Computer Science, University of Toronto, 2004.

[25] J. Masthoff, Group recommender systems: combining individual models, in: F. Ricci, L. Rokach, B. Shapira, P.B. Kantor (Eds.), Recommender Systems Handbook, Springer, US 2011 pp. 677–702.

[26] P. Melville, R. Mooney, R. Nagarajan, Content-boosted collaborative <sup>fi</sup>ltering for improved recommendations, Proceedings of the Eighteenth National Conference on Arti<sup>fi</sup>cial Intelligence, The AAAI Press 2002, pp. 178–192.

[27] B. Mobasher, X. Jin, Y. Zhou, Semantically enhanced collaborative <sup>fi</sup>ltering on the web, Web Mining: From Web to Semantic Web, First European Web Mining Forum, EMWF 2003, Lecture Notes in Computer Science, No. 3209 2003, pp. 57–76.

[28] S.-T. Park, D.O. Pennock, N.G. Madani, D. DeCoste, Nave <sup>fi</sup>lterbots for robust coldstart recommendations, KDD Õ06: Proceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2006, pp. 699–705.

[29] D.M. Pennock, E. Horvitz, S. Lawrence, C.L. Giles, Collaborative <sup>fi</sup>ltering by personality diagnosis: a hybrid memory- and model-based approach, Proceedings of the Sixteenth Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, Morgan Kaufmann Publishers 2000, pp. 473–480.

[30] R. Salakhutdinov, A. Mnih, G. Hinton, Restricted Boltzmann machines for collaborative <sup>fi</sup>ltering, Proceedings of the Twenty-fourth International Conference on Machine Learning, vol. 24 2007, pp. 791–798.

[31] A. Schein, A. Popescul, L. Ungar, D. Pennock, Generative models for cold-start recommendations, Proceedings of the 2001 SIGIR Workshop on Recommender Systems, 2001.

[32] V. Šmdl, A. Quinn, The variational Bayes method in signal processing, Springer-Verlag, 2006.

[33] T.T. Truyen, D.Q. Phung, S. Venkatesh, Ordinal Boltzmann machines for collaborative <sup>fi</sup>ltering, Proceedings of the Twenty-<sup>fi</sup>fth Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence 2009, pp. 548–556.

[34] Z. Xu, V. Tresp, K. Yu, H.-P. Kriegel, In<sup>fi</sup>nite hidden relational models, Proceedings of the Twenty-Second Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence 2006, pp. 544–551.

[35] K. Yoshii, M. Goto, K. Komatani, T. Ogata, H. Okuno, An ef<sup>fi</sup>cient hybrid music recommender system using an incrementally trainable probabilistic generative model, IEEE Transactions on Audio, Speech and Language Processing 16 (2008) 435–447.

Helge Langseth is a professor at the Department of Computer and Information Science at the Norwegian University of Science and Technology. His work has been published in several journals in the areas of machine learning and decision support systems. His current research interests center around learning from big data.

Thomas Dyhre Nielsen is an associate professor at at the Department of Computer Science, Aalborg University, Denmark. His main research interests concern learning of probabilistic graphical models from (hybrid) data and the use of these types of models for machine learning and decision analysis. He is currently member of two editorial boards and area editor for the International Journal of Approximate Reasoning.
