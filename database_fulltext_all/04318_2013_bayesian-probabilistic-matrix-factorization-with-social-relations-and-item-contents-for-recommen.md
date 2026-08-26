---
otero_id: 4318
otero_key: "UZ25P3YV"
title: "Bayesian Probabilistic Matrix Factorization with Social Relations and Item Contents for recommendation"
authors: "Juntao Liu; Caihua Wu; Wenyu Liu"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.04.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bayesian Probabilistic Matrix Factorization with Social Relations and Item Contents for recommendation

Juntao Liu <sup>a,b</sup>, Caihua Wu <sup>c</sup>, Wenyu Liu <sup>a,</sup>⁎

<sup>a</sup> Department of Electronics and Information Engineering, Huazhong University of Science and Technology, Wuhan 430074, China

<sup>b</sup> Department of Computer Engineering, Mechanical Engineering Institute, Shijiazhuang 050003, China

<sup>c</sup> Information Combat Commanding Teaching and Research Section, Information Countermeasure Department, Air Force Radar Academy, Wuhan 430010, China

## a r t i c l e i n f o

Article history: Received 3 September 2012 Received in revised form 27 March 2013 Accepted 4 April 2013 Available online 15 April 2013

Keywords: Recommendation system Collaborative <sup>fi</sup>ltering Social network Item contents Matrix factorization Tags

## a b s t r a c t

Recommendation systems have received great attention for their commercial value in today's online business world. However, most recommendation systems encounter the data sparsity problem and the cold-start problem. To improve recommendation accuracy in this circumstance, additional sources of information about the users and items should be incorporated in recommendation systems. In this paper, we modify the model in Bayesian Probabilistic Matrix Factorization, and propose two recommendation approaches fusing social relations and item contents with user ratings in a novel way. The proposed approach is computationally ef<sup>fi</sup>cient and can be applied to trust-aware or content-aware recommendation systems with very large dataset. Experimental results on three real world datasets show that our method gets more accurate recommendation results with faster converging speed than other matrix factorization based methods. We also verify our method in cold-start settings, and our method gets more accurate recommendation results than the compared approaches.

Crown Copyright © 2013 Published by Elsevier B.V. All rights reserved.

## 1. Introduction

Recommendation systems have become an important research area in the past decade. Recommendation systems typically try to predict the interests of a user by collecting rating information of other users or items. Recommendation methods are generally divided into collaborative <sup>fi</sup>ltering (CF) methods and content-based (CB) methods [19]. In content-based recommendation methods, the rating of an item for a user is estimated based on the ratings of similar items for this user. Collaborative <sup>fi</sup>ltering methods try to predict the rating of an item for a particular user based on the previous ratings of this item rated by other similar users. The underlying assumption of collaborative <sup>fi</sup>ltering is that similar users have similar tastes. Collaborative <sup>fi</sup>ltering methods are widely used in large commercial systems, such as Amazon and Net<sup>fl</sup>ix.

Matrix factorization is one of the most popular collaborative <sup>fi</sup>ltering methods in recent years. It is assumed that the preference of a user can be represented by a small number of unobserved features. Formally, supposing that there are M users and N items, M × N matrix R is the observed rating matrix. Matrix factorization based methods <sup>fi</sup>nd M × D user latent feature matrix U and N × D item latent feature matrix V to minimize the loss function $f _ { l o s s } \left( R , \hat { R } \right)$ , which measures the difference between the observed rating matrix R and the predicted rating matrix $\hat { R } = U V ^ { T }$ . Here D is the dimension of user feature vector and item feature vector. D is much less than M and N.

A number of algorithms have been proposed to solve matrix factorization for recommendation, such as Variational Bayesian Matrix Factorization (VBMF) [10], Probabilistic Matrix Factorization (PMF) [22], Bayesian Probabilistic Matrix Factorization (BPMF) [23], General Probabilistic Matrix Factorization (GPMF) [25] and so on. Same as other collaborative <sup>fi</sup>ltering methods, these methods encounter the data sparsity problem [2]. For a particular recommendation system, the density of the observed rating matrix is usually less than 1% [24]. In this case, it is dif<sup>fi</sup>cult to <sup>fi</sup>nd similar users or similar items. Another well-known problem in recommendation system is the cold-start problem, that is, how to provide recommendation to new users who have expressed very few ratings. It is believed that social relations among users can alleviate these problems. For example, in our daily life, we often turn to our friends for recommendations. We share interests with close friends. Our tastes are also often affected by our friends. Cooperating with social relations in recommendation systems can improve recommendation accuracy [15]. In recent years, some recommendation methods fusing social relations by regularization [6,9,16,28] or factorization [13,15] were proposed. On the other hand, item contents, such as tags, categories and item pro<sup>fi</sup>le, also provide huge opportunity to improve the accuracy of recommendation. For example, we may like movies performed by a same actor.

In this paper, to alleviate the data sparsity problem and the cold-start problem and to improve recommendation accuracy further, we integrate social relations and item contents into the framework of Bayesian Probabilistic Matrix Factorization (BPMF) [23] in a novel way which is different from regularization-based methods and factorization-based methods, and propose two novel recommendation methods cooperating with social relations and item contents. In BPMF, the hyperparameters of user feature vectors are the same for all users. But in practice, users' preferences vary greatly, so the hyperparameters of different users should be different. Generating user feature vectors by uniform user hyperparameters in BPMF may lead to some recommendation errors. In this paper we modify the model in BPMF, and suggest that the hyperparameters of different user vectors are different. We then propose the Bayesian Probabilistic Matrix Factorization with Social Relations (BPMFSR) recommendation method. To alleviate data sparsity problem and cold-start problem we fuse social relations in this method. We argue that the posterior distribution of user hyperparameters should be conditioned on the feature vectors of trusted users. The underlying assumption is that the users' preference may be in<sup>fl</sup>uenced by their friends. On the other hand, similar to the uniform user hyperparameters, uniform item hyperparameters in BPMF also lead to some recommendation errors. To address this problem, we extend our BPMFSR method by fusing item contents information and propose an improved algorithm, Bayesian Probabilistic Matrix Factorization with Social Relations and Item Contents (BPMFSRIC). In BPMFSRIC, we assume that the hyperparameters of different item vectors are different, and the posterior distribution of item feature vector parameters is conditioned on the feature vectors of linked items. The links among items can be extracted by item contents information, such as tags, categories and properties. The BPMFSR can be applied to trust-aware recommender systems. If item contents are known additionally, BPMFSRIC can improve recommendation accuracy further. The proposed method is computationally ef<sup>fi</sup>cient, and can be applied to large-scale real life datasets. Experimental results on Douban dataset [16], Epinions dataset [17] and Last.fm dataset [4] show that the accuracy of our method outperforms other methods based on matrix factorization. We also verify our method in cold-start settings, and our method gets better results than other methods.

The rest of this paper is organized as follows. In Section 2, a survey of major recommendation methods based on matrix factorization is provided. Section 3 introduces PMF and BPMF brie<sup>fl</sup>y. The proposed method is described in Section 4. The experimental results are presented and analyzed in Section 5 followed by the conclusions and further work in Section 6.

## 2. Related work

Rating-based recommendation methods are generally divided into collaborative <sup>fi</sup>ltering (CF) methods and content-based (CB) methods [19]. Matrix factorization based methods are one kind of collaborative <sup>fi</sup>ltering methods. In this section we review several recommendation methods based on matrix factorization.

Lim and Teh [10] proposed Variational Bayesian based Matrix Factorization (VBMF) for movie recommendation. Nakajima and Sugiyama [18] analyzed VBMF theoretically. Probabilistic Matrix Factorization (PMF) proposed by Salakhutdinov and Mnih [22] models the predictive error of matrix factorization as Gaussian distribution. Gradient descent algorithm is used to <sup>fi</sup>nd the local maximal of the posterior probability over user and item latent matrices with parameters. PMF gets accurate results on Net<sup>fl</sup>ix dataset. The main shortcoming of PMF is that careful parameter tuning is needed to avoid over <sup>fi</sup>tting. This leads to high computational complexity on large datasets. Bayesian Probabilistic Matrix Factorization (BPMF) [23] overcomes this drawback by using Markov Chain Monte Carlo (MCMC) method that gets more accurate predictive results. As far as we know, BPMF method outperforms most of the recommendation methods based on matrix factorization. Shan and Banerjee [5] extended PMF and BPMF and proposed a series of general PMF (GPMF) methods. Porteous et al. [20] fused side information into BPMF model. In their model, the ratings are estimated by the product of the user latent matrix and the item matrix and the regression of user and item side information. Adams et al. [1] modi<sup>fi</sup>ed the BPMF model. The observed rating matrix, the user latent matrix and the item latent matrix are represented by time-varying functions. The variation processes of user latent matrix and item matrix are represented by Gaussian processes. Lu et al. [11] proposed a matrix factorization based recommendation method to predict the variation of ratings with time. Two regularization terms, spatial term and temporal term, are added into the objective function. Gemulla et al. [5] proposed a strati<sup>fi</sup>ed stochastic gradient descent (SSGD) algorithm to solve the general matrix factorization problem, and gave suf<sup>fi</sup>cient conditions for convergence. Luo et al. [12] proposed an incremental collaborative <sup>fi</sup>ltering recommendation method based on the regularized matrix factorization.

Generally, the main challenges for recommendation systems are the data sparsity problem and the cold-start problem [2]. To address these problems, in recent years, researchers proposed some matrix factorization based recommendation methods fusing social relations among users with rating data, which can help to improve the performance of recommender systems. These methods can be divided into two types: regularization-based methods and factorization-based methods.

Regularization-based methods typically add regularization term to the loss function and minimize it. For examples, recommendation method proposed by Hao Ma et al. [16] adds social regularization term to the loss function, which measures the difference between the latent feature vector of a user and those of his (or her) friends. Local minimum of the loss function is found by gradient-based method. Jamali and Ester [6] proposed a probability model similar to the model 1 in [16]. Relation regularized matrix factorization (RRMF) [9] method proposed by Li and Yeung adds the graph Laplacian regularization term of social relations into the loss function and minimizes the loss function by alternative projection algorithm. Zhu et al. [28] used the same model in [9] and built graph Laplacian of social relations using three kinds of kernel functions. The minimization problem is formulated as low-rank semide<sup>fi</sup>nite program (LRSDP) and is solved by the method proposed in [3]. Regularization-based methods always minimize the difference between the latent feature vector of a user and those of his (or her) friends and give weights to the regularization terms to tradeoff between factorization error and regularization terms. The weights should be tuned manually to avoid over <sup>fi</sup>tting. So the drawback of this kind of methods is the same as that of PMF.

In factorization-based methods, social relations are represented as social relation matrix, which is factored as well as the rating matrix. The loss function is the weighted sum of the social relation matrix factorization error and the rating matrix factorization error. For example, SoRec [13] factorizes social relation matrix and rating matrix simultaneously. Social relation matrix is approximated as the product of the user latent feature matrix and the factor feature matrix. SoRec can also be extended to fuse social tags and item tags with rating information [15]. Yuan et al. [27] argued that factorization-based methods outperform regularizationbased methods for fusing membership information, and proposed a method fusing membership and friendship by factorization and regularization, respectively. Factorization-based methods encounter the same problem as regularization-based methods: the weight of the social relation matrix factorization error and the weight of the rating matrix factorization error should be tuned to avoid over <sup>fi</sup>tting, which is computationally expensive especially on large-scale datasets. To avoid parameter tuning, Singh and Gordon proposed Hierarchical Bayesian Collective Matrix Factorization (HBCMF) [26], in which two relation matrices are factored. The model of HBCMF is very similar to that of BPMF, and a block Metropolis–Hastings algorithm is used to sample from this model.

In this paper, we propose two novel recommendation methods cooperating with social relations and item contents. Our methods are different from previous methods because the way we use social relations and item contents is not factorization-based and regularizationbased. To fuse social relations and item contents, we modify the model in BPMF. The differences between our methods and PMF, and BPMF are shown in Fig. 1. Our methods not only avoid parameter tuning just as BPMF, but also improve recommendation accuracy and converge speed.

## 3. Preliminaries

In this section, we <sup>fi</sup>rst introduce preliminaries for matrix factorization based recommendation method. And then, we introduce the frameworks of PMF and BPMF brie<sup>fl</sup>y.

## 3.1. Matrix factorization for recommendation

Suppose there are M users and N items. Let matrix R denote the rating matrix, where $R _ { i j }$ represents the rating of user i for item j. In most online systems, $R _ { i j }$ is the K-point integer. For example, in Douban website (http://www.douban.com), rating values are 5-point integers, 1-point means ‘very bad’ and 5-point means ‘excellent’. Let $\breve { U } { \in } { \mathbb R } ^ { M \times \bar { D } }$ and $V { \in } \mathbb { R } ^ { N \times D }$ be the user and item latent feature matrices, where row vectors $U _ { i }$ and $V _ { j }$ represent user-speci<sup>fi</sup>c and item-speci<sup>fi</sup>c latent feature vectors. D is the dimension of user feature vector and item feature vector, which is much less than M and N. In Probabilistic Matrix Factorization (PMF) [22] method, the conditional probability of observed ratings matrix R is modeled as:

a  
![](/api/attachments/UZ25P3YV/fulltext/images/ef776d03a6a6c68a64361c57335a5655e5beb8585bbe2e31e06764a9819da49e.jpg)  
b

c  
![](/api/attachments/UZ25P3YV/fulltext/images/4532d1d260ca0692008d102afcaa2b030f6279e94d600b69d5f88b264bb88c04.jpg)  
d

$$
p \left(R | U, V, \sigma^ {2}\right) = \prod_ {i = 1} ^ {M} \prod_ {j = 1} ^ {N} \left[ N \left(R _ {i j} \mid U _ {i} V _ {j} ^ {T}, \sigma^ {2}\right) \right] ^ {I _ {i j}}\tag{1}
$$

where $N ( x | \mu , \sigma ^ { 2 } )$ is the probability density function of the Gaussian distribution with mean $\mu$ and variance $\sigma ^ { 2 } .$ . I is the indicator matrix. $I _ { i j }$ is equal to 1 if user i rated item j and 0 otherwise. The prior distributions of latent matrices U and V are modeled as:

$$
p \Big (U | \sigma_ {U} ^ {2} \Big) = \prod_ {i = 1} ^ {M} N \Big (U _ {i} | 0, \sigma_ {U} ^ {2} \Big)\tag{2}
$$

$$
p \Big (V | \sigma_ {V} ^ {2} \Big) = \prod_ {i = 1} ^ {N} N \Big (V _ {j} | 0, \sigma_ {V} ^ {2} \Big).\tag{3}
$$

The graphical model for PMF is shown in Fig. 1(a). This model is learned by maximizing posterior probability of latent matrices U and

![](/api/attachments/UZ25P3YV/fulltext/images/bb6192d9231bb3d5c87ab1f6cd6bfc3203ddd45391912b7f358bdb16463a594b.jpg)

![](/api/attachments/UZ25P3YV/fulltext/images/f714ef7042996a3ab04737f203e2b1ebd84a6731383f2a829db2b93c9d0d7c0a.jpg)  
Fig. 1. Graphical models for PMF $( \mathsf { a } ) ,$ BPMF (b), BPMFSR (c) and BPMFSRIC (d). The main difference between BPMF and BPMFSR is that BPMFSR generates user hyperparameters separately for every user vectors, while BPMF uses uniform user hyperparameters. BPMFSRIC not only generates user hyperparameters separately but also generate item hyperparameters separately.

V, which is equivalent to minimizing sum-of-squares of factorization error with quadratic regularization terms [22]:

$$
E = \frac {1}{2} \sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {N} I _ {i j} \left(R _ {i j} - U _ {i} V _ {j} ^ {T}\right) ^ {2} + \frac {\lambda_ {U}}{2} \| U \| _ {F r o} ^ {2} + \frac {\lambda_ {V}}{2} \| V \| _ {F r o} ^ {2}\tag{4}
$$

where $\lambda _ { U } = \sigma ^ { 2 } / \sigma _ { U } ^ { 2 } , \lambda _ { V } = \sigma ^ { 2 } / \sigma _ { V } ^ { 2 }$ and $| | \cdot | | _ { F r o } ^ { 2 }$ denote Frobenius norm. Local minimum of Eq. (4) is found through gradient descent method in PMF [22].

Although PMF is maybe the most popular method for collaborative <sup>fi</sup>ltering and it is very successful in the Net<sup>fl</sup>ix Prize contest, the drawbacks of this method are two-fold. Firstly, it requires careful tuning of parameters to avoid over <sup>fi</sup>tting. This process is computationally expensive on large datasets. Secondly, PMF assumes that user vectors and item vectors are independent and identically distributed and ignores the social relations among users. It is believed that social relations can alleviate the data sparsity problem, and improve recommendation accuracy. For this reason, Hao Ma et al. [16] add social regularization term to the loss function in Eq. (4). The social regularization term measures the difference between the feature vector of a user and those of his (or her) friends. Hao Ma's method gets more accurate recommendation results than NMF [8], PMF [22], RSTE [14] and other state-of-art on large real life datasets. In this paper, we compare our methods with Hao Ma's method.

## 3.2. Bayesian Probabilistic Matrix Factorization

To avoid parameter tuning, Salakhutdinov and Mnih [23] proposed a Bayesian model of Probabilistic Matrix Factorization (BPMF). The prior distributions of latent matrices U and V are given by:

$$
p \Big (U | \mu_ {U}, \Lambda_ {U} \Big) = \prod_ {i = 1} ^ {M} N \Big (U _ {i} | \mu_ {U}, \Lambda_ {U} ^ {- 1} \Big)\tag{5}
$$

$$
p \Big (V | \mu_ {V}, \Lambda_ {V} \Big) = \prod_ {i = 1} ^ {N} N \Big (V _ {j} | \mu_ {V}, \Lambda_ {V} ^ {- 1} \Big).\tag{6}
$$

BPMF assumes that user hyperparameters $\Theta _ { U } = \{ \mu _ { U } , \Lambda _ { U } \}$ and item hyperparameters $\Theta _ { V } = \{ \mu _ { V } , \Lambda _ { V } \}$ follow Gaussian-Wishart distribution. The prior distributions of user hyperparameters and item hyperparameters are given by:

$$
p \left(\Theta_ {U} \mid \Theta_ {0}\right) = p \left(\mu_ {U} \mid \Lambda_ {U}\right) p \left(\Lambda_ {U}\right) = N \left(\mu_ {U} \mid \mu_ {0}, \left(\beta_ {0} \Lambda_ {U}\right) ^ {- 1}\right) W \left(\Lambda_ {U} \mid W _ {0}, v _ {0}\right)\tag{7}
$$

$$
p \left(\Theta_ {V} \mid \Theta_ {0}\right) = p \left(\mu_ {V} \mid \Lambda_ {V}\right) p \left(\Lambda_ {V}\right) = N \left(\mu_ {V} \mid \mu_ {0}, \left(\beta_ {0} \Lambda_ {V}\right) ^ {- 1}\right) W \left(\Lambda_ {V} \mid W _ {0}, v _ {0}\right)\tag{8}
$$

where $W ( w | W _ { 0 } , \nu _ { 0 } )$ is the Wishart distribution with v degrees of freedom and $\mathsf { a } D \times D$ scale matrix $W _ { 0 } . \ \Theta _ { 0 } = \{ \mu _ { 0 } , \nu _ { 0 } , W _ { 0 } \}$ . The graphical model for BPMF is shown in Fig. 1(b). BPMF uses Gibbs algorithm to sample user and item feature vectors. It is assumed that the posterior distribution over user feature vector $U _ { i } ,$ which is conditioned on item feature matrix V, observed rating matrix R and hyperparameters, is Gaussian:

$$
\begin{array}{l} p (U _ {i} | R, V, \Theta_ {U}, \alpha) = N (U _ {i} | \mu_ {i} ^ {*}, (\Lambda_ {i} ^ {*}) ^ {- 1}) \\ \sim \prod_ {j = 1} ^ {N} \left[ N (R _ {i j} | U _ {i} ^ {T} V _ {j}, \alpha^ {- 1}) \right] ^ {I _ {i j}} p (U _ {i} | \mu_ {U}, \Lambda_ {U}) \end{array}\tag{9}
$$

where $\begin{array} { r } { \Lambda _ { i } ^ { * } = \Lambda _ { U } + \alpha \sum _ { j } ^ { N } = \ d _ { 1 } V _ { j } ^ { T } V _ { j } ) } \end{array}$ and $\begin{array} { r } { \mu _ { i } ^ { * } = ( \Lambda _ { i } ^ { * } ) ^ { - 1 } \mathopen { } \mathclose \bgroup \left( \alpha \sum _ { j = 1 } ^ { N } \big ( V _ { j } R _ { i j } \aftergroup \egroup \right) ^ { I _ { i j } } + } \end{array}$ $\mu _ { U } \Lambda _ { U } )$

The conditional distribution over user hyperparameters conditioned on the user feature matrix U is given as:

$$
p \left(\mu_ {U}, \Lambda_ {U} | U, \Theta_ {0}\right) = N \left(\mu_ {U} \mid \mu_ {0} ^ {*}, \left(\beta_ {0} ^ {*} \Lambda_ {U}\right) ^ {- 1}\right) W \left(\Lambda_ {U} \mid W _ {0} ^ {*}, v _ {0} ^ {*}\right)\tag{10}
$$

where

$$
\begin{array}{l} \mu_ {0} ^ {*} = \frac {\beta_ {0} \mu_ {0} + M \overline {{U}}}{\beta_ {0} + M}, \beta_ {0} ^ {*} = \beta_ {0} + M, v _ {0} ^ {*} = v _ {0} + M, \overline {{S}} = \frac {1}{M} \sum_ {i = 1} ^ {M} (U _ {i} - \overline {{U}}) ^ {T} (U _ {i} - \overline {{U}}) \\ \overline {{U}} = \frac {1}{M} \sum_ {i = 1} ^ {M} U _ {i} \text {and} W _ {0} ^ {*} = \left(W _ {0} ^ {- 1} + M \overline {{S}} + \frac {\beta_ {0} M}{\beta_ {0} + M} (\mu_ {0} - \overline {{U}}) ^ {T} (\mu_ {0} - \overline {{U}})\right) ^ {- 1}. \end{array}
$$

BPMF gets more accurate recommendation results than PMF, and avoids parameter tuning. But BPMF also ignores social relations among users. The distribution parameters of user feature vectors are estimated by all of the user feature vectors. It is observed that people with social relations are more likely to share same preferences. If we estimate distribution parameters of a particular user feature vector by the vectors of his (or her) friends, the recommendation accuracy will be improved further. By this idea, we propose our recommendation methods.

## 4. Proposed method

In BPMF framework, hyperparameters for all users are the same (see Eq. (5)). This is unreasonable because users' preferences are different, and the hyperparameters should be different too. We assume that user hyperparameters are different for different users, and propose Bayesian Probabilistic Matrix Factorization with Social Relations (BPMFSR), in which user hyperparameters are sampled according to the social relations. Our method uses the social relations in a novel way, which is not regularization-based and factorization-based, and can improve recommendation accuracy.

In BPMF, uniform item hyperparameters encounter the same problem. To improve the performance further, we fuse item contents as well as social relations, and propose Bayesian Probabilistic Matrix Factorization with Social Relations and Item Contents (BPMFSRIC), in which item hyperparameters are sampled according to the item contents.

In this section, we introduce BPMFSR and BPMFSRIC in details

## 4.1. Bayesian Probabilistic Matrix Factorization with Social Relation

It is unreasonable that hyperparameters $\Theta _ { U }$ are the same for different users in BPMF, which may cause some recommendation errors. To address this problem, we assume every user has its own hyperparameters. By this assumption, Eq. (5) should be modi<sup>fi</sup>ed as:

$$
p (U) = \prod_ {i = 1} ^ {M} N \Bigl (U _ {i} | \mu_ {U, i}, \Lambda_ {U, i} ^ {- 1} \Bigr)\tag{11}
$$

where $\Theta _ { U , i } = \{ \mu _ { U , i } , \Lambda _ { U , i } \}$ } are the hyperparameters for user feature vector U .

The posterior distribution over user feature vector $U _ { i }$ described in Eq. (9) should also be modi<sup>fi</sup>ed. In fact, the posterior distribution over user feature vector $U _ { i }$ is conditioned on the item feature matrix V, the observed rating matrix R and its own hyperparameters $\Theta _ { U , i } =$ $\{ \mu _ { U , i } , \Lambda _ { U , i } \}$ under our assumption. The posterior distribution over $U _ { i }$ is given as:

$$
\begin{array}{l} p \Big (U _ {i} | R, V, \Theta_ {U, i}, \alpha \Big) = N \Big (U _ {i} | \mu_ {U, i} ^ {*}, \left(\Lambda_ {U, i} ^ {*}\right) ^ {- 1} \Big) \\ \sim \prod_ {j = 1} ^ {N} \Big [ N \Big (R _ {i j} | U _ {i} ^ {T} V _ {j}, \alpha^ {- 1} \Big) \Big ] ^ {I _ {i j}} p \Big (U _ {i} | \mu_ {U, i}, \Lambda_ {U, i} \Big) \end{array}\tag{12}
$$

where $\begin{array} { r } { \Lambda _ { U , i } ^ { * } = \Lambda _ { U , i } + \alpha \sum _ { j = 1 } ^ { N } \Bigl ( V _ { j } ^ { T } V _ { j } \Bigr ) ^ { I _ { i j } } } \end{array}$ and $\begin{array} { r } { \mu _ { U , i } ^ { * } = ( \Lambda _ { i } ^ { * } ) ^ { - 1 } \big ( \alpha \sum _ { j = 1 } ^ { N } ( V _ { j } R _ { i j } ) ^ { I _ { i j } } + } \end{array}$ $\mu _ { U , i } \Lambda _ { U , i } )$

Because a user's preference is in<sup>fl</sup>uenced by his (or her) friends, we suppose that the conditional distribution over user hyperparameters is conditioned on feature vectors of user's friends. By this assumption, Eq. (10) should be modi<sup>fi</sup>ed as:

$$
\begin{array}{c} p \Big (\Theta_ {U, i} | U, \Theta_ {0} \Big) = p \Big (\Theta_ {U, i} | U _ {F, i}, \Theta_ {0} \Big) = p \Big (\mu_ {U, i}, \Lambda_ {U, i} | U _ {F, i}, \Theta_ {0} \Big) \\ = N \Big (\mu_ {U, i} | \mu_ {U, i} ^ {*}, \Big (\beta_ {U, i} ^ {*} \Lambda_ {U, i} \Big) ^ {- 1} \Big) W \Big (\Lambda_ {U, i} | W _ {U, i} ^ {*}, v _ {U, i} ^ {*} \Big) \end{array}\tag{13}
$$

$$
\begin{array}{r l} & {\mu_ {U, i} ^ {*} = \frac {\beta_ {0} \mu_ {0} + M _ {i} \overline {{U}} _ {(i)}}{\beta_ {0} + M _ {i}}, \beta_ {U, i} ^ {*} = \beta_ {0} + M _ {i}, v _ {U, i} ^ {*} = v _ {0} + M _ {i},} \\ & {W _ {U, i} ^ {*} = \left(W _ {0} ^ {- 1} + M _ {i} \overline {{S}} _ {U, i} + \frac {\beta_ {0} M _ {i}}{\beta_ {0} + M _ {i}} \left(\mu_ {0} - \overline {{U}} _ {(i)}\right) ^ {T} \left(\mu_ {0} - \overline {{U}} _ {(i)}\right)\right) ^ {- 1},} \\ & {\overline {{U}} _ {(i)} = \frac {1}{M _ {i}} \sum_ {j \in F _ {i}} U _ {j}, \overline {{S}} _ {U, i} = \frac {1}{M _ {i}} \sum_ {j \in F _ {i}} \left(U _ {j} - \overline {{U}} _ {(i)}\right) ^ {T} \left(U _ {j} - \overline {{U}} _ {i}\right), M _ {i} = | F _ {i} |} \end{array}
$$

where $U _ { F , i }$ is the matrix composed by feature vector of user i and feature vectors of user i's friends, $F _ { i }$ is the friend set of user i and himself and |⋅| denotes the size of a set.

The method described above is called Bayesian Probabilistic Matrix Factorization with Social Relations (BPMFSR), and the graph model is shown in Fig. 1(c). In this model, user feature vector $U _ { i }$ is generated according to its own hyperparameters $\Theta _ { U , i }$ for each user. We also use Gibbs sampling algorithm to sample user feature vectors and item feature vectors, which is given in Algorithm 1. In this algorithm, we <sup>fi</sup>rst generate user hyperparameters $\Theta _ { U , i }$ for each user by Eq. (13) and then generate user feature vector $U _ { i }$ with user hyperparameters $\Theta _ { U , i \cdot }$ If a user has very few friends, for an example, less than $D ,$ the hyperparameter estimation according to the feature vectors of his (or her) friends is meaningless. So in Algorithm 1, if user i has suf<sup>fi</sup>cient friends, hyperparameters are sampled according to the feature vectors of user i's friends, otherwise, hyperparameters are sampled according to the feature vectors of all users. Item hyperparameters and item feature vectors are generated by the same way in BPMF.

Algorithm 1. Gibbs sampling for Bayesian Probabilistic Matrix Factorization with Social Relationship (BPMFSR)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
01 Initialize model parameters  $U_{i}^{(1)}, V_{j}^{(1)}$ ;
02 for t = 1...T
03 sample the hyperparameters(Eq.10):
04  $\Theta_{U}^{(t)} \sim p(\Theta_{U}|U^{(t)}, \Theta_{0})$ 
05  $\Theta_{V}^{(t)} \sim p(\Theta_{V}|V^{(t)}, \Theta_{0})$ 
06 for i = 1...M,
07 if  $M_{i} &lt; D$  then
08 sample user features vector (Eq.9):  $U_{i}^{(t+1)} \sim p(U_{i}|R, V^{(t)}, \Theta_{U}^{(t)})$ 
09 else
10 sample hyperparameters for user i (Eq.13):  $\Theta_{U,i}^{(t)} \sim p(\Theta_{U,i}|U^{(t)}, \Theta_{0})$ 
11 sample user feature vector (Eq.12):  $U_{i}^{(t+1)} \sim p(U_{i}|R, V^{(t)}, \Theta_{U,i}^{(t)})$ 
12 end if
13 end for
14 for j = 1...N,
15 sample item features vector:  $V_{j}^{(t+1)} \sim p(V_{j}|R, U^{(t+1)}, \Theta_{V}^{(t)})$ 
16 end for
17 end for
</div>

Because different user hyperparameters are applied to different users, BPMFSR can get rid of the prediction errors caused by uniform user hyperparameters in BPMF. Furthermore, social relations are integrated in the model, which can improve prediction accuracy and alleviate the data sparsity problem and the cold-start problem.

4.2. Bayesian Probabilistic Matrix Factorization with Social Relation and Item Contents

Using uniform hyperparameters for all of the items in BPMF encounters the same problem caused by uniform user hyperparameters. To avoid the prediction error caused by uniform item hyperparameters and to further improve the recommendation accuracy, we assume that every item has its own hyperparameters. So Eq. (6) should be modi<sup>fi</sup>ed as:

$$
p (V) = \prod_ {j = 1} ^ {N} N \Bigl (V _ {j} | \mu_ {V. j}, \Lambda_ {V. j} ^ {- 1} \Bigr)\tag{14}
$$

where $\Theta _ { V , j } = \{ \mu _ { V , j } , \Lambda _ { V , j } \}$ are the hyperparameters for item feature vector $V _ { j } .$ By this assumption, the posterior distribution over item feature vector $V _ { j }$ is conditioned on the user feature matrix U, the observed rating matrix R and its own hyperparameters $\Theta _ { V , j } = \{ \mu _ { V , j } , \Lambda _ { V , j } \}$ . It is given as:

$$
\begin{array}{l} p \Big (V _ {j} | R, U, \Theta_ {V, j}, \alpha \Big) = N \Big (V _ {j} | \mu_ {V, j} ^ {*}, \left(\Lambda_ {V, j} ^ {*}\right) ^ {- 1} \Big) \\ \sim \prod_ {i = 1} ^ {M} \Big [ N \Big (R _ {i j} | U _ {i} ^ {T} V _ {j}, \alpha^ {- 1} \Big) \Big ] ^ {I _ {i j}} p \Big (V _ {j} | \mu_ {V, j}, \Lambda_ {V, j} \Big) \end{array}\tag{15}
$$

where $\begin{array} { r } { \Lambda _ { V , j } ^ { * } = \Lambda _ { V , j } + \alpha \sum _ { i = 1 } ^ { M } ( U _ { j } ^ { T } U _ { j } ) ^ { I _ { i j } } } \end{array}$ and $\mu _ { V , j } ^ { * } = ( \Lambda _ { V , j } ^ { * } ) ^ { - 1 } \big ( \alpha \textstyle { \sum _ { i = 1 } ^ { M } } ( U _ { i } R _ { i j } ) ^ { I _ { i j } } +$ $\mu _ { V , j } \Lambda _ { V , j } )$

Let $C _ { j }$ denote the item set in which every item links to item $j .$ The links between items can be constructed according to contents, such as item tags, categories and properties. For example, if two items are attached with a same tag, there is a link between them. We can also link the similar items by measuring item properties similarity.

To fuse item contents, we assume that the conditional distribution over item hyperparameters $\Theta _ { V , j } = \{ \mu _ { V , j } , \Lambda _ { V , j } \}$ is only conditioned on the feature vectors of items in $C _ { j } .$ The underlying assumption is that the items with links should receive similar ratings. The conditional distribution over hyperparameters of item j, $\Theta _ { V , j } = \{ \mu _ { V , j } , \Lambda _ { V , j } \}$ is given by:

$$
\begin{array}{c} p \Big (\Theta_ {V, j} | V, \Theta_ {0} \Big) = p \Big (\Theta_ {V, j} | V _ {C, j}, \Theta_ {0} \Big) = p \Big (\mu_ {V, j}, \Lambda_ {V, j} | V _ {C, j}, \Theta_ {0} \Big) \\ = N \Big (\mu_ {V, j} | \mu_ {V, j} ^ {*}, \left(\beta_ {V, j} ^ {*} \Lambda_ {V, j}\right) \Big) W \Big (\Lambda_ {V, j} | W _ {V, j} ^ {*}, v _ {V, j} ^ {*} \Big) \end{array}\tag{16}
$$

$$
\begin{array}{l} \mu_ {V, j} ^ {*} = \frac {\beta_ {0} \mu_ {0} + N _ {j} \overline {{V}} _ {(j)}}{\beta_ {0} + N _ {j}}, \beta_ {V, j} ^ {*} = \beta_ {0} + N _ {j}, v _ {V, j} ^ {*} = v _ {0} + N _ {j}, \\ W _ {V, j} ^ {*} = \left(W _ {0} ^ {- 1} + N _ {j} \overline {{S}} _ {V, j} + \frac {\beta_ {0} N _ {j}}{\beta_ {0} + N _ {j}} \left(\mu_ {0} - \overline {{V}} _ {(j)}\right) ^ {T} \left(\mu_ {0} - \overline {{V}} _ {(j)}\right)\right) ^ {- 1}, \\ \overline {{V}} _ {(j)} = \frac {1}{N j} \sum_ {k \in C _ {j}} V _ {k}, \overline {{S}} _ {V, j} = \frac {1}{N _ {j}} \sum_ {k \in C _ {j}} \left(V _ {k} - \overline {{V}} _ {(j)}\right) ^ {T} \left(V _ {k} - \overline {{V}} _ {(j)}\right), N _ {j} = \left| C _ {j} \right| \end{array}
$$

where $V _ { C , j }$ is the matrix composed by feature vectors of items in $C _ { j } ,$ and $C _ { j }$ is the item set in which items are linked to item j.

Table 1 Statistics of datasets.

<table><tr><td>Dataset</td><td>Douban</td><td>Epinions</td><td>Last.fm</td></tr><tr><td>Num. of users</td><td>129,490</td><td>49,290</td><td>1892</td></tr><tr><td>Num. of items</td><td>58,541</td><td>139,783</td><td>17,632</td></tr><tr><td>Num. of ratings</td><td>16,830,839</td><td>664,824</td><td>92,834</td></tr><tr><td>Rating matrix density</td><td> $2.220 \times 10^{-3}$ </td><td> $9.649 \times 10^{-5}$ </td><td> $2.783 \times 10^{-3}$ </td></tr><tr><td>Num. of friend links</td><td>1,692,952</td><td>487,181</td><td>12,717</td></tr><tr><td>Num. of tag statements</td><td>0</td><td>0</td><td>186,479</td></tr></table>

This method is called Bayesian Probabilistic Matrix Factorization with Social Relations and Item Contents (BPMFSRIC). Graphical model for BPMFSRIC is shown in Fig. 1(d). In this model, item hyperparameters are generated for each item, as well as user hyperparameters. We also use Gibbs sampler to sample user feature vectors and item feature vectors, which is given in Algorithm 2. Similar to Algorithm 1, Algorithm 2 samples item hyperparameters for each item if there are more than D items linking to it.

Algorithm 2. Gibbs sampling for Bayesian Probabilistic Matrix Factorization with Social Relationship and Item Contents (BPMFSRIC)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
01 Initialize model parameters  $U_{i}^{(1)}, V_{j}^{(1)}$ ;
02 for t = 1...T
03 sample the hyperparameters(Eq.10):
04  $\Theta_{U}^{(t)} \sim p(\Theta_{U}|U^{(t)}, \Theta_{0})$ 
05  $\Theta_{V}^{(t)} \sim p(\Theta_{V}|V^{(t)}, \Theta_{0})$ 
06 for i = 1...M,
07 if  $M_{i} &lt; D$  then
09 sample user feature vector (Eq.9):  $U_{i}^{(t+1)} \sim p(U_{i}|R, V^{(t)}, \Theta_{U}^{(t)})$ 
10 else
11 sample hyperparameters for user i (Eq.13):  $\Theta_{U,i}^{(t)} \sim p(\Theta_{U,i}|U^{(t)}, \Theta_{0})$ 
12 sample user feature vector (Eq.12):  $U_{i}^{(t+1)} \sim p(U_{i}|R, V^{(t)}, \Theta_{U,i}^{(t)})$ 
13 end if
14 end for
15 for j = 1...N,
16 if  $N_{j} &lt; D$  then
17 sample item feature vector:  $V_{j}^{(t+1)} \sim p(V_{j}|R, U^{(t+1)}, \Theta_{V}^{(t)})$ 
18 else
19 sample hyperparameters for item j (Eq.16):  $\Theta_{V,j}^{(t)} \sim p(\Theta_{V,j}|V^{(t)}, \Theta_{0})$ 
20 sample item feature vector (Eq.15):  $V_{j}^{(t+1)} \sim p(V_{j}|R, U^{(t+1)}, \Theta_{V,j}^{(t)})$ 
21 end if
22 end for
23 end for
</div>

vectors and sampling all item feature vectors is $O ( K )$ , where K is the number of nonzero entries in rating matrix R. So the computational complexity of one iteration in Algorithms 1 and 2 is O(K), which indicates that the computational complexity of our method is linear with respect to the number of observed ratings. This complexity analysis shows that our methods are very ef<sup>fi</sup>cient and can scale up with respect to very large datasets.

Compared with BPMF, the computational complexity of our methods is slightly higher in one iteration, because Algorithms 1 and 2 sample user hyperparameters and item hyperparameters using Eqs. (13) and (16) additionally. However, the computational complexity of sampling all user hyperparameters and sampling all item hyperparameters is much less than that of sampling user feature vectors and sampling item feature vectors. Furthermore, the experiments in Section 5 show that our methods converge faster than BPMF. Considering both computational complexity in one iteration and converge speed, our methods can achieve the same recommendation accuracy in few iterations and in less time.

## 4.4. Convergence analysis

Because we infer our model through Gibbs sampling, the convergence of the proposed method is guaranteed by that of Gibbs sampler. It has been proved that under positivity conditions, the Markov chain generated by Gibbs sampler will converge to its invariant distribution.

## De<sup>fi</sup>nition 1. Positivity condition [21]

A density function $f ( x _ { 1 } , x _ { 2 } , . . . . , x _ { n } )$ and marginal density functions $f _ { i } ( x _ { i } )$ are said to satisfy the positivity condition i $\dot { \ f } _ { i } ( x _ { i } ) > 0$ for all $x _ { 1 } , x _ { 2 } , . . . . , x _ { n }$ implies that $f ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) > 0 .$

The main computation of Algorithms 1 and 2 is sampling user feature vectors using Eq. (12) and sampling item feature vectors using Eq. (15). The computational complexity of sampling all user feature

Lemma 1. [21] If the joint distribution $f ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$ satisfies the positivity condition, the Gibbs sampler yields an irreducible and recurrent Markov chain.

The distribution in our model satis<sup>fi</sup>es the positivity condition, so our methods converge as the number of iteration approaches to ∞. Convergence of the proposed method is also con<sup>fi</sup>rmed by the experiments in Section 5.

## 4.3. Complexity analysis

## 5. Experiments

In this section, we present the experimental results on three large scale datasets to compare our method with other recommendation methods based on matrix factorization. We also verify our methods in cold-start settings.

Predictive accuracy comparison on Douban Dataset (the values in brackets are the results reported in [16]).

<table><tr><td>D (dimension)</td><td>Training</td><td>Metrics</td><td>Hao Ma&#x27;s method</td><td>BPMF</td><td>BPMFSR</td></tr><tr><td rowspan="6">10</td><td rowspan="2">40%</td><td>MAE</td><td> $0.5845 \pm 0.0008(0.5685)$ </td><td> $0.5583 \pm 0.0001$ </td><td> $0.5577 \pm 0.0001$ </td></tr><tr><td>RMSE</td><td> $0.7411 \pm 0.0005(0.7125)$ </td><td> $0.7045 \pm 0.0002$ </td><td> $0.7045 \pm 0.0001$ </td></tr><tr><td rowspan="2">60%</td><td>MAE</td><td> $0.5665 \pm 0.0005(0.5593)$ </td><td> $0.5512 \pm 0.0001$ </td><td> $0.5510 \pm 0.0001$ </td></tr><tr><td>RMSE</td><td> $0.7221 \pm 0.0005(0.7042)$ </td><td> $0.6971 \pm 0.0001$ </td><td> $0.6973 \pm 0.0001$ </td></tr><tr><td rowspan="2">80%</td><td>MAE</td><td> $0.5562 \pm 0.0003(0.5543)$ </td><td> $0.5472 \pm 0.0002$ </td><td> $0.5467 \pm 0.0002$ </td></tr><tr><td>RMSE</td><td> $0.7099 \pm 0.0004(0.6988)$ </td><td> $0.6930 \pm 0.0002$ </td><td> $0.6934 \pm 0.0003$ </td></tr><tr><td rowspan="6">30</td><td rowspan="2">40%</td><td>MAE</td><td> $0.5950 \pm 0.0004$ </td><td> $0.5588 \pm 0.0001$ </td><td> $0.5570 \pm 0.0001$ </td></tr><tr><td>RMSE</td><td> $0.7524 \pm 0.0005$ </td><td> $0.7051 \pm 0.0001$ </td><td> $0.7039 \pm 0.0001$ </td></tr><tr><td rowspan="2">60%</td><td>MAE</td><td> $0.5789 \pm 0.0002$ </td><td> $0.5509 \pm 0.0001$ </td><td> $0.5486 \pm 0.0001$ </td></tr><tr><td>RMSE</td><td> $0.7336 \pm 0.0007$ </td><td> $0.6963 \pm 0.0001$ </td><td> $0.6948 \pm 0.0001$ </td></tr><tr><td rowspan="2">80%</td><td>MAE</td><td> $0.5674 \pm 0.0001$ </td><td> $0.5448 \pm 0.0001$ </td><td> $0.5427 \pm 0.0001$ </td></tr><tr><td>RMSE</td><td> $0.7204 \pm 0.0001$ </td><td> $0.6896 \pm 0.0001$ </td><td> $0.6884 \pm 0.0001$ </td></tr></table>

Predictive accuracy comparison on Epinions dataset.

<table><tr><td>D (dimension)</td><td>Training</td><td>Metrics</td><td>Hao Ma&#x27;s method</td><td>BPMF</td><td>BPMFSR</td></tr><tr><td rowspan="8">10</td><td rowspan="2">40%</td><td>MAE</td><td> $0.9261 \pm 0.0034$ </td><td> $0.8535 \pm 0.0018$ </td><td> $0.8411 \pm 0.0006$ </td></tr><tr><td>RMSE</td><td> $1.2046 \pm 0.0050$ </td><td> $1.0858 \pm 0.0026$ </td><td> $1.0695 \pm 0.0008$ </td></tr><tr><td rowspan="2">60%</td><td>MAE</td><td> $0.9313 \pm 0.0023$ </td><td> $0.8383 \pm 0.0018$ </td><td> $0.8359 \pm 0.0006$ </td></tr><tr><td>RMSE</td><td> $1.2003 \pm 0.0047$ </td><td> $1.0704 \pm 0.0027$ </td><td> $1.0655 \pm 0.0009$ </td></tr><tr><td rowspan="2">80%</td><td>MAE</td><td> $0.9018 \pm 0.0026$ </td><td> $0.8144 \pm 0.0020$ </td><td> $0.8114 \pm 0.0022$ </td></tr><tr><td>RMSE</td><td> $1.1630 \pm 0.0027$ </td><td> $1.0498 \pm 0.0023$ </td><td> $1.0435 \pm 0.0025$ </td></tr><tr><td rowspan="2">90%</td><td>MAE</td><td> $0.8915 \pm 0.0036$ </td><td> $0.8081 \pm 0.0020$ </td><td> $0.8056 \pm 0.0020$ </td></tr><tr><td>RMSE</td><td> $1.1510 \pm 0.0055$ </td><td> $1.0435 \pm 0.0035$ </td><td> $1.0334 \pm 0.0040$ </td></tr><tr><td rowspan="8">30</td><td rowspan="2">40%</td><td>MAE</td><td> $0.9341 \pm 0.0040$ </td><td> $0.8446 \pm 0.0073$ </td><td> $0.8381 \pm 0.0010$ </td></tr><tr><td>RMSE</td><td> $1.2043 \pm 0.0021$ </td><td> $1.0785 \pm 0.0069$ </td><td> $1.0666 \pm 0.0012$ </td></tr><tr><td rowspan="2">60%</td><td>MAE</td><td> $0.9332 \pm 0.0031$ </td><td> $0.8423 \pm 0.0057$ </td><td> $0.8348 \pm 0.0017$ </td></tr><tr><td>RMSE</td><td> $1.2015 \pm 0.0039$ </td><td> $1.0741 \pm 0.0056$ </td><td> $1.0640 \pm 0.0025$ </td></tr><tr><td rowspan="2">80%</td><td>MAE</td><td> $0.9135 \pm 0.0019$ </td><td> $0.8156 \pm 0.0018$ </td><td> $0.8124 \pm 0.0016$ </td></tr><tr><td>RMSE</td><td> $1.1736 \pm 0.0025$ </td><td> $1.0496 \pm 0.0026$ </td><td> $1.0403 \pm 0.0024$ </td></tr><tr><td rowspan="2">90%</td><td>MAE</td><td> $0.9078 \pm 0.0039$ </td><td> $0.8087 \pm 0.0025$ </td><td> $0.8078 \pm 0.0024$ </td></tr><tr><td>RMSE</td><td> $1.1661 \pm 0.0051$ </td><td> $1.0434 \pm 0.0034$ </td><td> $1.0352 \pm 0.0030$ </td></tr></table>

## 5.1. Datasets

We evaluate our method on Douban dataset [16], Epinions dataset [17] and Last.fm dataset [4]. Douban (http://www.douban.com) dataset, crawled by Hao Ma et al. [16], contains 16,830,839 ratings of 129,490 users on 58,541 movies and 1,692,952 friend links between these users. For more details, please see [16].

Epinions (http://www.epinions.com) dataset [17] contains 49,290 users and 139,783 items. These users issued 664,824 ratings and 487,181 trust statements. Note that the Epinions dataset collected by Massa and Avesani [17] used in this paper is different from that used in [16]. Epinions dataset collected by Massa and Avesani [17] contains more items, ratings, friend links and fewer users.

Last.fm (http://www.lastfm.com) dataset is released in the framework of the 2nd International Workshop on Information Heterogeneity and Fusion in Recommender Systems (HetRec 2011) [4]. It contains 1892 users, 17,632 artists and 11,946 tags. Different from Douban dataset and Epinions dataset, Last.fm dataset only records listening count that each user listened to artists. Listening count ranges from 1 to 352,698. To test our methods on Last.fm, we map listening counts into integer values of 1 to 5 to represent the extent of favor of artists by the similar way in [7]. The mapping formula is given as:

$$
r = \left\{ \begin{array}{l} \left\lfloor \log_ {1 0} l \right\rfloor + 1, \text { if } \left\lfloor \log_ {1 0} l \right\rfloor + 1 \leq 5 \\ 5, \text { otherwise } \end{array} \right.\tag{17}
$$

a) 40% training data, $D = 1 0$ where l is the listening count, r is the mapped value, and ⌊⋅⌋ is the operator of rounding towards zero. To test BPMFSRIC method, we build the links according to tags. If two artists received a same tag more than 5 times, we link these two artists. Last.fm contains 12,717 friend links, 92,834 listening counts and 186,479 tag statements.

![](/api/attachments/UZ25P3YV/fulltext/images/5ab2f7ce09765a8790b03e71f00075f14e5c32c7e5be11ec9f077b770d9b8e67.jpg)  
d) 40% training data, $D = 3 0$

b) 60% training data, $D = 1 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/76a624c38d721d65c77a2d88c280edbdcd2953fd34c994b8f141c82bfddbd045.jpg)  
e) 60% training data, $D = 3 0$

c) 80% training data, $D = 1 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/2841ddf2ef536f4ebda8351684942e063c9ee9efd2d200e57c1b21defdf8852d.jpg)

![](/api/attachments/UZ25P3YV/fulltext/images/094170d9f7519ce833e283efe95cc9b4788095464fc38a46c35f94679097a3e9.jpg)

f) 80% training data, $D = 3 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/3eb369f24c29ec856a0ab9e6387bc66c41981db526cab583370e51420005ba5d.jpg)

![](/api/attachments/UZ25P3YV/fulltext/images/696daefd8255d4e309a3298ce0ce4dab6c3a54df52be41c3fb2483646573c0e7.jpg)  
Fig. 2. Testing RMSE of all methods on Douban dataset, the x-axis shows the number of epoch and y-axis shows testing RMSE.

a) 60% training data, D = 10  
![](/api/attachments/UZ25P3YV/fulltext/images/b5d4246b38c95f39f60accaff376202e87ce0c1f830497551251e17b7ba9e2f3.jpg)  
d) 60% training data, $D = 3 0$

b) 80% training data, D = 10  
![](/api/attachments/UZ25P3YV/fulltext/images/180e484037c1eef6bd9073f4d594a07c44eeda3f5b49a14ad738f734e74f781b.jpg)

c) 90% training data, D =10  
![](/api/attachments/UZ25P3YV/fulltext/images/6a0ae027e88d81f8dcf98b6f0107814717528b5bcd519d80823186b52f47dff9.jpg)

e) 80% training data, $D = 3 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/08ac08478091f7c3e031d5843c4729e1b6f7b145c1c5b5b659dc50cfd0d90290.jpg)

f) 90% training data, $D = 3 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/70303105010ccf83d0abb26fe4bc86db204369f5947f46f40a7dd974a3e1919b.jpg)

![](/api/attachments/UZ25P3YV/fulltext/images/2b3005634328985c5c33e118a435f75a25abac92b2a0ffb2a7a991356372c119.jpg)  
Fig. 3. Testing RMSE of all methods on Epinions dataset, the x-axis shows the number of epoch and y-axis shows testing RMSE

The statistics of these datasets are summarized in Table 1.

We use Mean Absolute Error (MAE) and Root Mean Square Error (RMSE) to measure prediction accuracy of recommendation methods. MAE is de<sup>fi</sup>ned as:

$$
\mathrm{MAE} = \frac {1}{T} \sum_ {i, j} | R _ {i j} - \hat {R} _ {i j} |
$$

## 5.2. Comparisons

<sub>ð</sub><sup>18</sup><sub>Þ</sub>

We compare Hao Ma's method [16] and BPMF [23] with our methods. Hao Ma's method is implemented using model 2 with PCC similarity (see [16] for details). It is reported that this implementation gets the highest prediction accuracy and outperforms NMF [8], PMF [22], RSTE [14] and other state-of-art. The initial solutions of our methods are the same as those of BPMF. In our methods, $\mu _ { 0 } , \nu _ { 0 } ,$ and $W _ { 0 }$ are set to be the same values as those in BPMF. The experiments repeat 10 times. Mean and standard deviation of MAE and RMSE are calculated.

where $R _ { i j }$ is the rating given by user i for item j, and $\hat { R } _ { i j }$ is the prediction of $R _ { i j } .$ T is the total number of tested ratings. RMSE is de<sup>fi</sup>ned as:

$$
\mathrm{RMSE} = \sqrt {\frac {1}{T} \sum_ {i , j} \left(R _ {i j} - \hat {R} _ {i j}\right) ^ {2}}.\tag{19}
$$

For Douban dataset, we randomly select 40%, 60% and 80% ratings as training data, and use the rest of ratings to test the algorithms. For Epinions dataset, we use 40%, 60%, 80% and 90% ratings as training data. Because Douban dataset and Epinions dataset don't contain item contents information, which is needed by BPMFSRIC, we don't test BPMFSRIC on these two datasets. The experimental results are shown in Tables 2 and 3. We give the mean and standard deviation of RMSE and MAE for each experiment. The best results which are statistically signi<sup>fi</sup>cant (at the 5% signi<sup>fi</sup>cance level) are set to be bold. According to the results, it can be observed that our method outperforms Hao

Table 4 Predictive accuracy comparison on Last.fm dataset.

<table><tr><td>D (dimension)</td><td>Training</td><td>Metrics</td><td>Hao Ma&#x27;s method</td><td>BPMF</td><td>BPMFSR</td><td>BPMFSRIC</td></tr><tr><td rowspan="6">10</td><td rowspan="2">40%</td><td>MAE</td><td> $0.4806 \pm 0.0032$ </td><td> $0.3359 \pm 0.0018$ </td><td> $\mathbf{0.3338} \pm \mathbf{0.0012}$ </td><td> $0.3341 \pm 0.0007$ </td></tr><tr><td>RMSE</td><td> $0.6936 \pm 0.0047$ </td><td> $0.4655 \pm 0.0036$ </td><td> $0.4613 \pm 0.0028$ </td><td> $\mathbf{0.4604} \pm \mathbf{0.0026}$ </td></tr><tr><td rowspan="2">60%</td><td>MAE</td><td> $0.4539 \pm 0.0070$ </td><td> $0.3270 \pm 0.0014$ </td><td> $\mathbf{0.3261} \pm \mathbf{0.0015}$ </td><td> $0.3278 \pm 0.0012$ </td></tr><tr><td>RMSE</td><td> $0.6529 \pm 0.0104$ </td><td> $0.4502 \pm 0.0023$ </td><td> $\mathbf{0.4489} \pm \mathbf{0.0023}$ </td><td> $0.4502 \pm 0.0021$ </td></tr><tr><td rowspan="2">80%</td><td>MAE</td><td> $0.4310 \pm 0.0056$ </td><td> $0.3234 \pm 0.0012$ </td><td> $0.3222 \pm 0.0014$ </td><td> $0.3237 \pm 0.0016$ </td></tr><tr><td>RMSE</td><td> $0.6210 \pm 0.0080$ </td><td> $0.4465 \pm 0.0018$ </td><td> $0.4449 \pm 0.0021$ </td><td> $0.4461 \pm 0.0020$ </td></tr><tr><td rowspan="6">30</td><td rowspan="2">40%</td><td>MAE</td><td> $0.4849 \pm 0.0020$ </td><td> $0.3378 \pm 0.0006$ </td><td> $0.3354 \pm 0.0004$ </td><td> $0.3345 \pm 0.0005$ </td></tr><tr><td>RMSE</td><td> $0.6977 \pm 0.0019$ </td><td> $0.4686 \pm 0.0018$ </td><td> $0.4630 \pm 0.0017$ </td><td> $\mathbf{0.4596} \pm \mathbf{0.0013}$ </td></tr><tr><td rowspan="2">60%</td><td>MAE</td><td> $0.4691 \pm 0.0027$ </td><td> $0.3283 \pm 0.0016$ </td><td> $0.3277 \pm 0.0019$ </td><td> $0.3286 \pm 0.0017$ </td></tr><tr><td>RMSE</td><td> $0.6708 \pm 0.0038$ </td><td> $0.4529 \pm 0.0021$ </td><td> $0.4515 \pm 0.0022$ </td><td> $0.4508 \pm 0.0020$ </td></tr><tr><td rowspan="2">80%</td><td>MAE</td><td> $0.4492 \pm 0.0013$ </td><td> $0.3241 \pm 0.0012$ </td><td> $0.3235 \pm 0.0012$ </td><td> $0.3244 \pm 0.0014$ </td></tr><tr><td>RMSE</td><td> $0.6418 \pm 0.0026$ </td><td> $0.4467 \pm 0.0024$ </td><td> $0.4452 \pm 0.0024$ </td><td> $0.4451 \pm 0.0026$ </td></tr></table>

Table 6  
a) 40% training data, D = 10  
![](/api/attachments/UZ25P3YV/fulltext/images/bb791102eabc34632022df70eb9541fbb64b24accea6d2a67aab18f694006304.jpg)  
d) 40% training data, $D = 3 0$

b) 60% training data, D = 10  
![](/api/attachments/UZ25P3YV/fulltext/images/2fd6a6c0384edae63e5cadfd6eae9016baa1be5f97c94399fcf271eb046f0a91.jpg)

c) 80% training data, D = 10  
![](/api/attachments/UZ25P3YV/fulltext/images/ab65bec2a12256c26ddd85b59514b9d17f412f3be00e17b62903429f7d641aac.jpg)

e) 60% training data, $D = 3 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/42b7d2ff8cb4edb1e1b7d166a5bca77ffa08dd4b34e9a3398153d031aa6a9cac.jpg)

f) 80% training data, $D = 3 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/7847fa43ea71f61192b14964a0024643aad0c7a485e1fa75433b85b21aa55857.jpg)

![](/api/attachments/UZ25P3YV/fulltext/images/c59364d80a2b1aa770b4e21403e2b97fe74f2a2b509ed64d6598b9695e1ed0e6.jpg)  
Fig. 4. Testing RMSE of all methods on Last.fm dataset, the x-axis shows the number of epoch and y-axis shows testing RMSE.

Ma's method and BPMF on Epinions datasets in the term of improved RMSE and MAE. On Douban dataset, in the cases of 60% and 80% training data with $D = 1 0 .$ , BPMF get lower RMSE than BPMFSR. MAE and RMSE generated by BPMF and BPMFSR on Douban dataset are very close. The advantages of BPMFSR are more obvious on Epinions dataset. Epinions dataset is much sparser than Douban dataset, so we can say that

Predictive accuracy comparison in cold-start settings on Douban dataset.

<table><tr><td>D (dimension)</td><td>Cold-start users</td><td>Metrics</td><td>Hao Ma&#x27;s method</td><td>BPMF</td><td>BPMFSR</td></tr><tr><td rowspan="4">10</td><td rowspan="2">60%</td><td>MAE</td><td> $0.7321 \pm 0.0005$ </td><td> $0.6337 \pm 0.0004$ </td><td> $0.6335 \pm 0.0003$ </td></tr><tr><td>RMSE</td><td> $0.9067 \pm 0.0002$ </td><td> $0.7902 \pm 0.0004$ </td><td> $0.7885 \pm 0.0004$ </td></tr><tr><td rowspan="2">40%</td><td>MAE</td><td> $0.7319 \pm 0.0003$ </td><td> $0.6333 \pm 0.0004$ </td><td> $0.6327 \pm 0.0003$ </td></tr><tr><td>RMSE</td><td> $0.9071 \pm 0.0006$ </td><td> $0.7899 \pm 0.0004$ </td><td> $0.7877 \pm 0.0005$ </td></tr><tr><td rowspan="4">30</td><td rowspan="2">60%</td><td>MAE</td><td> $0.7320 \pm 0.0008$ </td><td> $0.6340 \pm 0.0007$ </td><td> $0.6336 \pm 0.0009$ </td></tr><tr><td>RMSE</td><td> $0.9077 \pm 0.0010$ </td><td> $0.7906 \pm 0.0010$ </td><td> $0.7895 \pm 0.0012$ </td></tr><tr><td rowspan="2">40%</td><td>MAE</td><td> $0.7324 \pm 0.0007$ </td><td> $0.6338 \pm 0.0006$ </td><td> $0.6334 \pm 0.0007$ </td></tr><tr><td>RMSE</td><td> $0.9080 \pm 0.0010$ </td><td> $0.7903 \pm 0.0011$ </td><td> $0.7891 \pm 0.0012$ </td></tr></table>

Predictive accuracy comparison in cold-start settings on Epinions dataset.

<table><tr><td>D (dimension)</td><td>Cold-start users</td><td>Metrics</td><td>Hao Ma&#x27;s method</td><td>BPMF</td><td>BPMFSR</td></tr><tr><td rowspan="8">10</td><td rowspan="2">60%</td><td>MAE</td><td> $0.9236 \pm 0.0026$ </td><td> $0.8558 \pm 0.0021$ </td><td> $0.8558 \pm 0.0017$ </td></tr><tr><td>RMSE</td><td> $1.2092 \pm 0.0031$ </td><td> $1.0809 \pm 0.0034$ </td><td> $1.0806 \pm 0.0033$ </td></tr><tr><td rowspan="2">40%</td><td>MAE</td><td> $0.9250 \pm 0.0008$ </td><td> $0.8517 \pm 0.0012$ </td><td> $0.8517 \pm 0.0010$ </td></tr><tr><td>RMSE</td><td> $1.2105 \pm 0.0015$ </td><td> $1.0769 \pm 0.0018$ </td><td> $1.0759 \pm 0.0018$ </td></tr><tr><td rowspan="2">10%</td><td>MAE</td><td> $0.9229 \pm 0.0025$ </td><td> $0.8496 \pm 0.0040$ </td><td> $0.8469 \pm 0.0049$ </td></tr><tr><td>RMSE</td><td> $1.2104 \pm 0.0040$ </td><td> $1.0725 \pm 0.0053$ </td><td> $1.0717 \pm 0.0055$ </td></tr><tr><td rowspan="2">5%</td><td>MAE</td><td> $0.9192 \pm 0.0049$ </td><td> $0.8424 \pm 0.0050$ </td><td> $0.8389 \pm 0.0048$ </td></tr><tr><td>RMSE</td><td> $1.2071 \pm 0.0048$ </td><td> $1.0643 \pm 0.0055$ </td><td> $1.0625 \pm 0.0049$ </td></tr><tr><td rowspan="8">30</td><td rowspan="2">60%</td><td>MAE</td><td> $0.9287 \pm 0.0030$ </td><td> $0.8551 \pm 0.0025$ </td><td> $0.8516 \pm 0.0024$ </td></tr><tr><td>RMSE</td><td> $1.2093 \pm 0.0031$ </td><td> $1.0803 \pm 0.0030$ </td><td> $1.0794 \pm 0.0029$ </td></tr><tr><td rowspan="2">40%</td><td>MAE</td><td> $0.9264 \pm 0.0014$ </td><td> $0.8478 \pm 0.0013$ </td><td> $0.8469 \pm 0.0011$ </td></tr><tr><td>RMSE</td><td> $1.2064 \pm 0.0023$ </td><td> $1.0740 \pm 0.0012$ </td><td> $1.0742 \pm 0.0013$ </td></tr><tr><td rowspan="2">10%</td><td>MAE</td><td> $0.9282 \pm 0.0048$ </td><td> $0.8498 \pm 0.0040$ </td><td> $0.8449 \pm 0.0039$ </td></tr><tr><td>RMSE</td><td> $1.2113 \pm 0.0066$ </td><td> $1.0730 \pm 0.0054$ </td><td> $1.0702 \pm 0.0052$ </td></tr><tr><td rowspan="2">5%</td><td>MAE</td><td> $0.9243 \pm 0.0108$ </td><td> $0.8431 \pm 0.0063$ </td><td> $0.8388 \pm 0.0071$ </td></tr><tr><td>RMSE</td><td> $1.2082 \pm 0.0152$ </td><td> $1.0655 \pm 0.0090$ </td><td> $1.0623 \pm 0.0101$ </td></tr></table>

a) 60% cold-start user, $D = 1 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/306edd205c6f35264db287754758dacc8a069c6e4034ff22dd4a62aedf6f40dd.jpg)

b) 60% cold-start user, $D = 3 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/dbf8eda39e009f02b564daa22eff9869819231107745061e24f6c15d23219df2.jpg)

c) 40% cold-start user, $D = 1 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/0c9ddcee6049ffe471eea1cf50315115757a95de36716a3fef5796dc1e42d2e3.jpg)

d) 40% cold-start user, $D = 3 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/bf0f197da8cc9e12e7d2fcaab3f0feb201062104dd9aafbc7e3f44caf3bacfa1.jpg)  
Fig. 5. Testing RMSE of all methods on Douban dataset for cold-start user setting, the x-axis shows the number of iteration and v-axis shows testing RMSE

BPMFSR alleviates the data sparsity problem better than other methods. We also notice that the increasing of user and item feature vector dimension doesn't improve the predictive accuracy of Hao Ma's method and BPMF, while BPMFSR gets more accurate results with higher dimension. This indicates that Hao Ma's method and BPMF may over <sup>fi</sup>t in high dimension.

a) 10% cold-start user, $D = 1 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/d7c78e2d3d83409dd24045c181dc60b3cf438dbe0540f145c8c613528687ebb0.jpg)

b) 10% cold-start user, $D = 3 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/6e2269150353d510be058cc666d50494e129677da663f8e68fde556f6dd5992c.jpg)

c) 5% cold-start user, $D = 1 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/cc76e4a3ddfd0c0a4fa01f75c29f1541c2235ec4807d8dbee87c2332b0fd5793.jpg)

d) 5% cold-start user, $D = 3 0$  
![](/api/attachments/UZ25P3YV/fulltext/images/c0609d5195d8ef0c8c810edc8a35af82ae9d7d5277296f3d7411b39726a348aa.jpg)  
Fig, 6. Testing RMSE of all methods on Epinions dataset for cold-start user setting, the x-axis shows the pumber of epoch and v-axis shows testing RMSE

Table 7  
Predictive accuracy comparison in cold-start settings on Last.fm dataset.

<table><tr><td>D (dimension)</td><td>Cold-start users/items</td><td>Metrics</td><td>Hao Ma&#x27;s method</td><td>BPMF</td><td>BPMFSR</td><td>BPMFSRIC</td></tr><tr><td rowspan="4">10</td><td rowspan="2">10%/10%</td><td>MAE</td><td> $0.4973 \pm 0.0155$ </td><td> $0.4213 \pm 0.0183$ </td><td> $0.4209 \pm 0.0186$ </td><td> $0.4178 \pm 0.0169$ </td></tr><tr><td>RMSE</td><td> $0.7150 \pm 0.0180$ </td><td> $0.6039 \pm 0.0225$ </td><td> $0.6009 \pm 0.0239$ </td><td> $0.5960 \pm 0.0191$ </td></tr><tr><td rowspan="2">5%/5%</td><td>MAE</td><td> $0.4860 \pm 0.0187$ </td><td> $0.4127 \pm 0.0183$ </td><td> $0.4106 \pm 0.0183$ </td><td> $0.4082 \pm 0.0198$ </td></tr><tr><td>RMSE</td><td> $0.7027 \pm 0.0232$ </td><td> $0.5945 \pm 0.0260$ </td><td> $0.5885 \pm 0.0276$ </td><td> $0.5857 \pm 0.0271$ </td></tr><tr><td rowspan="4">30</td><td rowspan="2">10%/10%</td><td>MAE</td><td> $0.4883 \pm 0.0095$ </td><td> $0.4174 \pm 0.0105$ </td><td> $0.4143 \pm 0.0086$ </td><td> $\mathbf{0.4131} \pm \mathbf{0.0087}$ </td></tr><tr><td>RMSE</td><td> $0.7091 \pm 0.0101$ </td><td> $0.6017 \pm 0.0114$ </td><td> $0.5972 \pm 0.0100$ </td><td> $0.5954 \pm 0.0097$ </td></tr><tr><td rowspan="2">5%/5%</td><td>MAE</td><td> $0.4800 \pm 0.0183$ </td><td> $0.4093 \pm 0.0165$ </td><td> $0.4055 \pm 0.0159$ </td><td> $0.4033 \pm 0.0160$ </td></tr><tr><td>RMSE</td><td> $0.6970 \pm 0.0211$ </td><td> $0.5878 \pm 0.0212$ </td><td> $0.5831 \pm 0.0199$ </td><td> $0.5786 \pm 0.0203$ </td></tr></table>

Note that the results reported in [16], shown in the brackets in Table 2, are slightly lower than the results obtained by our implementation. Because we cannot get the code used in [16], we attribute the discrepancy to some implementation details unmentioned in [16]. Although the results reported in [16] and those obtained by us are slightly different, we can draw the same conclusion that our method outperforms Hao Ma's method on Douban dataset in the case of D = 10 even using the results reported in [16].

by Eq. (17). Tag statements are used to build links between items (artists). If two artists received a same tag more than 5 times, we link these two artists. We randomly select 40%, 60% and 80% ratings as training data, and use the rest of ratings as testing data. The experiments repeat 10 times, and mean and standard deviation of MAE and RMSE are calculated. The experimental results are shown in Table 4. It can be observed that our methods get lower mean of MAE and RMSE than Hao Ma's method and BPMF in all cases. When dimension is high, BPMFSRIC gets lower mean of MAE and RMSE than BPMFSR.

Figs. 2 and 3 show testing RMSE generated by all methods at every epoch on Douban dataset and Epinions dataset. It can be observed that Hao Ma's method over <sup>fi</sup>ts after several epochs, while BPMF and BPMFSR do not over <sup>fi</sup>t at all. RMSE values generated by BPMFSR are higher than those generated by BPMF at the beginning, but after about 10 epochs BPMFSR outperforms BPMF. This indicates that BPMFSR converges faster than BPMF.

We compare BPMFSR and BPMFSRIC with Hao Ma's method and BPMF on Last.fm dataset. Listening count is mapped into 5-point rating

Fig. 4 shows testing RMSE generated by all methods at every epoch on Last.fm dataset. Trends of convergence are similar to those in Figs. 2 and 3. Furthermore, BPMFSRIC and BPMFSR converge faster than BPMF especially in the cases of 40% training data.

## 5.3. Comparisons in cold-start settings

We test our methods in cold-start settings. For Douban dataset we randomly select 60% and 40% users as cold-start users. For Epinions dataset, we randomly select 60%, 40%, 10% and 5% users as cold-start users. All the ratings stated by cold-start users are treated as testing

a) 10% cold-start user and 10%  
![](/api/attachments/UZ25P3YV/fulltext/images/e4927e0a77d0c4eeef24fa36299736caed969b1e38a4df17c64de50ded3809c7.jpg)  
c) 5% cold-start user and 5%  
cold-start item, D =10

b) 10% cold-start user and 10%  
![](/api/attachments/UZ25P3YV/fulltext/images/4d04e0d97a98f11a5fefb88d28c7ccbdef61b83706039c3e9e015dd7c1513cd1.jpg)

![](/api/attachments/UZ25P3YV/fulltext/images/52d37a0dfb766aea0beadf8bf82f241ae6954550dbe728ab832677a437012f05.jpg)

d) 5% cold-start user and 5%  
cold-start item, D = 30  
![](/api/attachments/UZ25P3YV/fulltext/images/76b18b9ad221e68b0e0a1d7591a2fb1e19fc64668f7695e6d4d3d1f5d88d6e20.jpg)  
Fig. 7. Testing RMSE of all methods on Last.fm dataset for cold-start user setting, the x-axis shows the number of epoch and y-axis shows testing RMSE.

a  
![](/api/attachments/UZ25P3YV/fulltext/images/8e46f320611a598018b36b16e2c787e756581d66ec40c0589723bf78a205fba4.jpg)

b  
![](/api/attachments/UZ25P3YV/fulltext/images/04d6128bfa0f2b9d90edd31b9aa8db459832b668fbc9181f33474b087833437a.jpg)

c  
![](/api/attachments/UZ25P3YV/fulltext/images/84cd17a91f204f0369f365f67dbf365b9195db2525e037ab6a5e6863fa466e26.jpg)  
Fig. 8. Impact of feature dimension on all datasets (60% training data)

data and all the other ratings are treated as training data. We compare Hao Ma's method and BPMF with BPMFSR. The results are shown in Tables 5 and 6. It can be observed that BPMFSR outperforms the compared methods on Douban dataset in all cases. In Epinions dataset, BPMFSR obtains lower mean of RMSE and MAE.

Figs. 5 and 6 show testing RMSE generated by all methods at every epoch on Douban dataset and Epinions dataset in cold-start-user settings. We can <sup>fi</sup>nd Hao Ma's method over<sup>fi</sup>ts at the beginning in all cases. BPMFSR converges faster than BPMF and gets better results in fewer epochs.

For Last.fm dataset we randomly select 5% and 10% users and items as cold-start users and cold-start items. All the ratings for cold-start users and cold-start items are treated as testing data and all other ratings are treated as training data. We compare Hao Ma's method and BPMF with BPMFSR and BPMFSRIC. The results are shown in Table 7. It can be observed that BPMFSR and BPMFSRIC obtain lower mean of RMSE and MAE then the compared methods in all cases. Because item contents are used in BPMFSRIC, BPMFSRIC gets more accurate prediction results than BPMFSR in all cases.

Fig. 7 shows the testing RMSE generated by all methods at every epoch on Last.fm dataset in cold-start user and item settings. We can <sup>fi</sup>nd Hao Ma's method over<sup>fi</sup>ts at the beginning for all cases. Our methods converge faster than BPMF and get better results in fewer epochs.

## 5.4. Impact of the feature dimension

We investigate the impact of the feature dimension. Using 60% training data, we change the feature dimension and calculate RMSE on Douban dataset, Epinions dataset and Last.fm dataset. The results are presented in Fig. 8. We observe that the feature dimension impacts the recommendation results. As feature dimension increases, the prediction accuracy increases quickly at <sup>fi</sup>rst. But when feature dimension increases further, the prediction accuracy increases slowly and even decreases on Last.fm. This phenomenon indicates that very high feature dimension cannot help to improve the recommendation accuracy.

## 6. Conclusion and future work

To address the data sparsity problem and the cold-start problem, in this paper, we modify the model in BPMF. We assume that the user hyperparameters and item hyperparameters are different for each user vector and item vector. The proposed recommendation methods, BPMFSR and BPMFSRIC, sample user hyperparameters and item hyperparameters according to the social relations and item contents. By this novel way we fuse social relations and item contents with ratings, which is different from traditional regularization-based methods and factorization-based methods. BPMFSR can be applied to trust-aware recommendation systems, while if the item contents are available, BPMFSRIC can improve recommendation accuracy further. The proposed methods are computationally ef<sup>fi</sup>cient and can scale up with respect to very large datasets. Experimental results on three large real world datasets show that our methods get more accurate recommendation results with faster converging speed than the other state-of-the-art recommendation methods based on matrix factorization. Moreover, our methods outperform other methods in cold-start settings.

In our methods, we only use the trust information, while distrust statements are also provided in many online social networks. How to use distrust information is one of our further research directions. An important problem should be investigated: how the distrust relations affect the user preference.

Furthermore, we only use the direct trust relations between users and ignore the indirect trust relations. Trust relations can propagate among people in real life, so indirect trust relations can also affect the preference of a user. How to fuse indirect trust relations is another research direction.

## Acknowledgments

This work is supported by the National Natural Science Foundation of China (61173120). The authors would like to thank the reviewers and editor for their helpful comments.

## References

[1] R.P. Adams, G.E. Dahl, I. Murray, Incorporating Side Information in Probabilistic Matrix Factorization with Gaussian Processes, UAI, 2010, pp. 1–9.

[2] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[3] S. Burer, R. Monteiro, A nonlinear programming algorithm for solving semide<sup>fi</sup>nite programs via low-rank factorization, Mathematical Programming 95 (2) (2003) 329–357.

[4] I. Cantador, P. Brusilovsky, T. Ku<sup>fl</sup>ik, Second workshop on information heterogeneity and fusion in recommender systems (hetrec2011), Proceedings of the Fifth ACM Conference on Recommender systems, RecSys'11, ACM, New York, NY, USA, 2011, pp. 387–388.

[5] R. Gemulla, E. Nijkamp, P. Haas, Y. Sismanis, Large-scale matrix factorization with distributed stochastic gradient descent, Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2011 pp. 69–77.

[6] M. Jamali, M. Ester, A transitivity aware matrix factorization model for recommendation in social networks, Proceedings of the Twenty-Second International Joint Conference on Arti<sup>fi</sup>cial Intelligence, IJCAI'11, AAAI Press, 2011, pp. 2644–2649.

[7] O. Koyejo, J. Ghosh, A kernel-based approach to exploiting interaction-networks in heterogeneous information sources for improved recommender systems, Proceedings of the 2nd International Workshop on Information Heterogeneity and Fusion in Recommender Systems, ACM, 2011, pp. 9–16.

[8] D. Lee, H. Seung, et al., Learning the parts of objects by non-negative matrix factorization, Nature 401 (6755) (1999) 788–791.

[9] W. Li, D. Yeung, Relation regularized matrix factorization, Proceedings of the 21st International Joint Conference on, Arti<sup>fi</sup>cial Intelligence, 2009, pp. 1126–1131.

[10] Y. Lim, Y. Teh, Variational Bayesian approach to movie rating prediction, Proceedings of KDD Cup and Workshop, Citeseer, 2007, pp. 15–21.

[11] Z. Lu, D. Agarwal, I. Dhillon, A spatio-temporal approach to collaborative <sup>fi</sup>ltering, Proceedings of the Third ACM Conference on Recommender Systems, ACM, 2009, pp. 13–20.

[12] X. Luo, Y. Xia, Q. Zhu, Incremental collaborative <sup>fi</sup>ltering recommender based on regularized matrix factorization, Knowledge-Based Systems 27 (2012) 271–280.

[13] H. Ma, H. Yang, M. Lyu, I. King, SoRec: social recommendation using probabilistic matrix factorization, Proceedings of the 17th ACM Conference on Information and Knowledge Management, ACM, 2008, pp. 931–940.

[14] H. Ma, I. King, M. Lyu, Learning to recommend with social trust ensemble, Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2009, pp. 203–210.

[15] H. Ma, T. Zhou, M. Lyu, I. King, Improving recommender systems by incorporating social contextual information, ACM Transactions on Information Systems (TOIS) 29 (2) (2011) 9:1–9:23.

[16] H. Ma, D. Zhou, C. Liu, M. Lyu, I. King, Recommender systems with social regularization, Proceedings of the Fourth ACM International Conference on Web Search and Data Mining, ACM, 2011, pp. 287–296.

[17] P. Massa, P. Avesani, Trust-aware bootstrapping of recommender systems, ECAI 2006 Workshop on Recommender Systems, Citeseer, Riva del Garda, Italy, 2006, pp. 29–33.

[18] S. Nakajima, M. Sugiyama, Theoretical analysis of Bayesian matrix factorization, Journal of Machine Learning Research 12 (2011) 2583–2648.

[19] D.H. Park, H.K. Kim, I.Y. Choi, J.K. Kim, A literature review and classi<sup>fi</sup>cation of recommender systems research, Expert Systems with Applications 39 (11) (2012) 10059–10072.

[20] I. Porteous, A. Asuncion, M. Welling, Bayesian matrix factorization with side information and Dirichlet process mixtures, Proceedings of the 24th AAAI Conference on, Arti<sup>fi</sup>cial Intelligence, 2010, pp. 563–568.

[21] C. Robert, G. Casella, Monte Carlo Statistical Methods, Springer Texts in Statistics, Springer, 2004.

[22] R. Salakhutdinov, A. Mnih, Probabilistic Matrix Factorization, Advances in Neural Information Processing Systems, 20, 2008. 1257–1264.

[23] R. Salakhutdinov, A. Mnih, Bayesian probabilistic matrix factorization using Markov Chain Monte Carlo, Proceedings of the 25th International Conference on Machine Learning, ACM, 2008, pp. 880–887.

[24] B. Sarwar, G. Karypis, J. Konstan, J. Reidl, Item-based collaborative <sup>fi</sup>ltering recommendation algorithms, Proceedings of the 10th International Conference on World Wide Web, ACM, 2001, pp. 285–295.

[25] H. Shan, A. Banerjee, Generalized probabilistic matrix factorizations for collaborative <sup>fi</sup>ltering, Data Mining (ICDM), 2010 IEEE 10th International Conference on, IEEE, 2010, pp. 1025–1030.

[26] A. Singh, G. Gordon, A Bayesian matrix factorization model for relational data Proceedings of the Twenty-Sixth Conference Annual Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence (UAI-10), AUAI Press, Corvallis, Oregon, 2010, pp. 556–563.

[27] Q. Yuan, L. Chen, S. Zhao, Factorization vs. regularization: Fusing heterogeneous social relationships in top-n recommendation, Proceedings of the <sup>fi</sup>fth ACM conference on Recommender Systems, ACM, 2011, pp. 245–252.

[28] J. Zhu, H. Ma, C. Chen, J. Bu, Social Recommendation Using Low-rank Semide<sup>fi</sup>nite Program, AAAI, 2011, pp. 158–163

Juntao Liu received the BS and MS degrees in Computer Science from Ordnance Engineering College, Shijiazhuang, China, in 2002 and 2005, respectively. He is a lecturer in the Department of Computer Engineering, Ordnance Engineering College. He is currently pursuing the Ph.D. degree in the Department of Electronics and Information Engineering, Huazhong University of Science and Technology. His research interests include data mining, machine learning and computer vision.

Caihua Wu received the BS, MS and PhD degrees in Computer Science from Ordnance Engineering College, Shijiazhuang, China, in 2003, 2006 and 2009 respectively. Now she is a lecturer in the Department of Information Counterwork, Air Force Radar Academy. Her research interests include data mining, information counterwork and software engineering.

Wenyu Liu received the BS degree in Computer Science from Tsinghua University, Beijing, China, in 1986, and the MS and PhD degrees, both in Electronics and Information Engineering, from Huazhong University of Science and Technology (HUST), Wuhan, China, in 1991 and 2001, respectively. He is now a professor and associate dean of the Department of Electronics and Information Engineering, HUST. His current research areas include computer graphics, multimedia information processing, and computer vision. He is a member of IEEE System, Man and Cybernetics Society.
