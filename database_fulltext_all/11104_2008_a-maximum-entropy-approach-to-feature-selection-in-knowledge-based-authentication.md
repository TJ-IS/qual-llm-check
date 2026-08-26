---
otero_id: 11104
otero_key: "S4P2U832"
title: "A maximum entropy approach to feature selection in knowledge-based authentication"
authors: "Ye Chen; Divakaran Liginlal"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.07.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A maximum entropy approach to feature selection in knowledge-based authentication

Ye Chen <sup>a,</sup>⁎, Divakaran Liginlal <sup>b</sup>

<sup>a</sup> Data Mining and Research, Yahoo! Inc., 701 First Avenue, Sunnyvale, CA 94089, USA

<sup>b</sup> Operations and Information Management, University of Wisconsin-Madison, 975 University Avenue, Madison, WI 53706, USA

## a r t i c l e i n f o

Article history: Received 16 December 2006 Received in revised form 26 May 2008 Accepted 16 July 2008 Available online 23 July 2008

Keywords: Feature selection Maximum entropy Probabilistic model Metrics Security Knowledge-based authentication

## a b s t r a c t

Feature selection is critical to knowledge-based authentication. In this paper, we adopt a wrapper method in which the learning machine is a generative probabilistic model, and the objective is to maximize the Kullback–Leibler divergence between the true empirical distribution de<sup>fi</sup>ned by the legitimate knowledge and the approximating distribution representing an attacking strategy, both in the same feature space. The closed-form solutions to this optimization problem lead to three adaptive algorithms, uni<sup>fi</sup>ed under the principle of maximum entropy. Our experimental results show that the proposed adaptive methods are superior to the commonly used random selection method

© 2008 Elsevier B.V. All rights reserved

## 1. Introduction

Knowledge-based authentication (KBA) refers to the method of verifying a user's identity by matching one or more pieces of information (also called factoids) provided by an individual (claimant) against information sources associated with the claimant [14,30]. KBA has several advantages over other conventional methods of authentication for both claimants and veri<sup>fi</sup>ers [25]. First, no prior relationship needs to be established between the claimant and the veri<sup>fi</sup>er speci<sup>fi</sup>cally for the sake of authentication, since the knowledge required for user authentication is available from previous transactions or from public data sources such as Social Security Administration (SSA) and Consumer Reporting Agency (CRA). Second, the factoids are relatively easy to remember, compared with strong passwords [17]. KBA has consequently found wide use in e-commerce and egovernment applications, both as a primary method of authentication as in consumer credit check and as a secondary method to augment strong authentication methods such as one-time passcode and security token. KBA is usually implemented as a challenge–response system, a practical example of which is VeriSign's Consumer Authentication Service (CAS) deployed by eBay [35]. A comprehensive review of the KBA literature is available in [8].

The major challenges that exist in the discipline of KBA research and practice are: (1) the de<sup>fi</sup>nitions of key metrics such as guessability and memorability; (2) the estimation of the parameters; and (3) a uni<sup>fi</sup>ed framework which also captures the dependency relationships among factoids. Chen and Liginlal [8] proposed entropy-based metrics and a Bayesian network model of KBA, as an attempt to solve the model selection problem. Their underlying intuition is appealing. In the context of KBA, Shannon entropy [32] can be interpreted as a measure of the security strength of a single factoid or that of a KBA system consisting of a selected subset of factoids. From the methodological perspective, their primary contribution is a sound probabilistic approach to the information security problem of practical signi<sup>fi</sup>cance. The guessability metric is de<sup>fi</sup>ned as a probability and estimated by maximum likelihood estimation (MLE) and a gametheoretical derivation in a probabilistically rational setup. Based on the same probabilistic modeling approach proposed in [8], the problem of selecting secure KBA factoids yields a principled measure of factoid relevance, that is, Kullback–Leibler (KL) divergence between the true distribution underlying the legitimate knowledge and the conceived distribution possessed by attackers.

The purpose of this paper is to address the other fundamental problem in KBA modeling, namely that of feature selection. In the language of KBA, feature selection is the task of selecting a relevant subset of factoids, such that the resulting KBA system can best distinguish attackers from legitimate users. At a conceptual level, this mirrors the general twofold goal of feature selection as it is widely applied to machine learning, that is, to gain a better understanding of the underlying statistical regularity and thereby improve the predicative performance. In this regard, we shall formally de<sup>fi</sup>ne the relevance of the selected feature subset in terms of the assurance level guaranteed by the resulting KBA system and represented by the guessability metric. At a practical level, feature selection is necessary both to keep the computation tractable when hundreds of thousands of variables are present, and to cure the so called “curse of dimensionality” problem when the size of the training set is relatively small in a highdimensional feature space. Although the practical concern is not as severe in the KBA domain since it is uncommon to have hundreds of factoids in knowledge sources, the issue of computational ef<sup>fi</sup>ciency has implications for the response time of a KBA system, especially in online e-commerce applications. Besides, from a usability standpoint, it is necessary to focus on a small but relevant subset of factoids in KBA applications. In general, most users are considered unwilling to tolerate more than about <sup>fi</sup>ve questions [26].

However, an important distinction should be made between the KBA problem in particular or security tasks in general, and the traditional statistical classi<sup>fi</sup>cation problem. From the model learning point of view, we can neither readily obtain the training data from real attackers, nor shall we theoretically assume that the inherently unpredictable future attacking behaviors can be extrapolated from the past fraudulent data. This challenge precludes us from directly employing the state-of-the-art classi<sup>fi</sup>cation techniques such as Support Vector Machines (SVMs), which are discriminative models and are known to be sensitive to unseen data [5]. Instead, we take the generative view to <sup>fi</sup>rst model our opponent, i.e., potential attackers, and then model the KBA domain to deliver strong authentication systems. We do not have the training data about how those attackers will go about discharging their malicious behaviors, but we do know exactly what they are targeting; therefore, it is natural to use a gametheoretic analysis to speculate on their attacking strategies, based on some rationality assumptions. This leads to a maximum entropy approach to the feature selection problem in KBA. Our method is well grounded in probabilistic modeling and information theory. In fact, the principle of maximum entropy, with proper underlying probabilistic semantics for user authentication, provides us a uni<sup>fi</sup>ed framework for measurement, feature selection, and modeling tasks to design a secure and adaptive KBA system.

The rest of the paper is structured as follows. In Section 2, we formulate the feature selection problem in the KBA context, followed by a literature review of the major approaches to feature selection in general. In Section 3, we deliberate upon the generative model and the rational attacker assumptions. Section 4 presents three algorithms for feature selection, based on the principle of maximum entropy and characterized by increasing levels of adaptivity. In Section 5, we report the results of a computational evaluation that demonstrate the better authentication performance of the three adaptive algorithms over the random feature selection method commonly used in practical KBA deployments. We conclude in Section 6 by identifying several areas for future research.

## 2. Feature selection in KBA

## 2.1. Notation and terminology

We approach the KBA feature selection problem from a statistical modeling perspective, in which the knowledge with respect to authentication is embedded in a collection of discrete data. The data sources can be characterized at three hierarchical levels: factoid. identity, and domain. Formally:

1. A factoid describes one speci<sup>fi</sup>c characteristic of a legitimate user for the purpose of authentication, and is denoted by a pair of random variables (f, x). Here f is the name and x is the value of the factoid, e.g., (mother's maiden name, Alice).

2. An identity, denoted by id, corresponds to a legitimate user. It can be uniquely identi<sup>fi</sup>ed by such <sup>fi</sup>elds as user name and account number.

3. A domain denoted by K, consisting of a set of U identities $I = \{ \mathrm { i d } _ { \mathrm { u } } \} _ { u = 1 } U$ and a set of V factoids $F = \{ f _ { \nu } \} _ { \nu = 1 } ^ { V } ,$ is de<sup>fi</sup>ned by a $U \times V$ matrix $\mathbf { K } = \left( x _ { u v } \right) _ { U \times V } ,$ , where $x _ { u v }$ is the value of the vth factoid associated with the uth identity.

4. The feature selection problem involves selecting a subset of n factoids from the V candidates, where $n \leq V .$ . We represent the names of the selected factoids as a random vector $\pmb { f } \imath ( f _ { 1 } , . . . , f _ { i } , . . . , f _ { n } ) ,$ where $f _ { i } \in F ,$ and the factoid values associated with an id of the selected subset as a random vector $\pmb { x } \mathrm { = } ( x _ { 1 } , . . . , x _ { i } , . . . , x _ { n } )$ . Thus f ranges over all possible n-combinations within F, while x ranges over all realizations of f in K. Also note that x is fully functionally dependent on id, but not vice versa.

## 2.2. An information-theoretic formulation

From an information-theoretic view, the underlying knowledge is considered a source of information $\mathcal { \kappa } ,$ which generates factoid values <sup>K</sup>for all identities to form a domain K or the knowledge source against which to match claimants' responses. With respect to a KBA session involving challenges against a selected subset of factoids f, K de<sup>fi</sup>nes an empirical joint distribution p(x) over x, which is the random vector of factoid values with a certain entropy $H ( p ( { \pmb x } ) )$ ). Assuming the generative process to be stationary and ergodic, p(x) and $H ( p ( { \pmb x } ) )$ re<sup>fl</sup>ect the underlying statistical structure of the information source . <sup>K</sup>On the other hand, an attacker tries to guess the factoid values of f based on the knowledge and strategy at his disposal. We can regard a rational attacker as another source of information or a stochastic guessing machine ${ \mathcal { G } } ,$ which emits responses to factoids f following <sup>G</sup>another joint distribution q(x) with entropy $H ( q ( { \pmb x } ) )$ . For a single factoid $f ,$ the true empirical distribution p(x) and the guessing distribution $q ( x )$ of x are marginal distributions. At one extreme, if an attacker had full knowledge about the domain K, the guessing distribution $q ( { \pmb x } )$ would be identical to the true distribution p(x), given any identity under attack. Typically, an attacker only has zero or partial knowledge, thus $q ( { \pmb x } )$ is different from $p ( { \pmb x } )$ . The security strength of a KBA system, speci<sup>fi</sup>cally the relevance or optimality of the selected subset of factoids $\mathbf { \sigma } _ { f } ,$ can thus be quanti<sup>fi</sup>ed in terms of the cross entropy of the guessing distribution q(x) with respect to the true distribution p(x) over the same selected feature space, given an identity under attack. Thus the feature selection problem in the context of KBA can be formulated as the following optimization problem:

$$
\begin{array}{l} \boldsymbol {f} ^ {*} = \underset {\boldsymbol {f} \subseteq F} {\arg \max} H (p (\boldsymbol {x}), q (\boldsymbol {x}) | \boldsymbol {f}) \\ \qquad = \underset {\boldsymbol {f} \subseteq F} {\arg \max} - \sum_ {x} p (\boldsymbol {x}) \log q (\boldsymbol {x}) \\ \qquad = \underset {\boldsymbol {f} \subseteq F} {\arg \max} - \sum_ {x} p (\boldsymbol {x}) \log p (\boldsymbol {x}) + \sum_ {x} p (\boldsymbol {x}) \log \frac {p (\boldsymbol {x})}{q (\boldsymbol {x})} \\ \qquad = \underset {\boldsymbol {f} \subseteq F} {\arg \max} H (p (\boldsymbol {x})) + D _ {K L} (p (\boldsymbol {x}) | | q (\boldsymbol {x})). \end{array}\tag{1}
$$

In Eq. (1), the cross entropy $H ( p ( { \pmb x } ) , q ( { \pmb x } ) )$ measures the average amount of information in bits needed to identify a realization from the true but unknown distribution p(x), given that the arbitrary approximating distribution is $q ( { \pmb x } )$ instead. The cross entropy $H ( p ( { \pmb x } ) ,$ q(x)) is conceptually equivalent to the Kullback–Leibler (KL) divergence $D _ { K L } ( p ( { \pmb x } ) q ( { \pmb x } ) )$ or simply $D _ { K L } ( p q )$ , a probabilistic distance measure from the true distribution $p ( { \pmb x } )$ to the approximating distribution q(x) [23]. The only difference H(p(x)) is a constant given a selected subset of factoids f F. Both the cross entropy and the KL divergence hold their minima when the attacker has perfect information about the domain, i.e., min $H ( p ( { \pmb x } ) , q ( { \pmb x } ) ) = H ( p ( { \pmb x } ) )$ and min $D _ { K L } ( p ( { \pmb x } ) q ( { \pmb x } ) ) = 0 \mathrm { i f f } p = q .$

Let us reinterpret these information-theoretic concepts in the context of KBA. In general, the entropy H(K) of the entire discrete factoid space F is the average amount of information embodied in each row vector in the matrix K, or a measure of uncertainty one encounters to pinpoint all factoid values of an id. H(K) is an inherent property of the domain K over the entire feature space F. A selected subset of factoids de<sup>fi</sup>nes a subspace f with entropy $H ( p ( { \pmb x } ) )$ . From an attacker's perspective, the cross entropy $H ( p ( { \pmb x } ) , q ( { \pmb x } ) )$ is interpreted as the average amount of knowledge he needs to acquire in order to correctly guess the factoid values x of f associated with an id, and the KL divergence $D _ { K L } ( p ( { \pmb x } ) q ( { \pmb x } ) )$ is the extra effort in bits required since he erroneously conjectures $\pmb { x } { \sim } q ( \pmb { x } )$ instead of the true distribution $\pmb { x } \sim p$ (x). In other application areas holding the same information-theoretic view, q typically refers to a theory or a model to approximate a true distribution p. Thus the goal in that case is to minimize the cross entropy in order to asymptotically approximate the underlying process. For example, statistical language modeling adopts this view and develops a performance measure called perplexity which is closely related to cross entropy [16,31].

With regard to the KBA problem, the goal is the opposite: to maximize the cross entropy; since the approximating distribution $q ( { \pmb x } )$ is at the attacker's disposal. An optimal KBA design should select the factoids such that the attacker's cost is maximized. The two terms on the right-hand side of Eq. (1) imply two possible ways to increase the cross entropy: (1) to raise $H ( p ( { \pmb x } ) )$ with respect to the feature subspace f by feature selection; and (2) to enhance $D _ { K L } ( p ( { \pmb x } ) q ( { \pmb x } ) )$ so that the true distribution p(x) over f would look, to an attacker, as divergent as possible from the guessing distribution $q ( { \pmb x } ) ,$ , depending both on feature selection and the attacking strategy q(x). It is important to note, however, that an authentication session or experiment is always conducted in the context of a certain identity under attack. Thus, to calculate the entropy-based relevance measure $H ( p ( { \pmb x } ) , \ q ( { \pmb x } ) )$ , the probability distribution functions p(x) and q(x) should be considered as conditioned on the identity under attack, $\mathrm { i } . \mathrm { e } . , p ( { \pmb x } | \mathrm { i d } )$ and $q ( \pmb { x } | \mathrm { i d } ) ;$ and the cross entropy H(p(x), q(x)) of a domain K is the expected value of the cross entropy given an identity, i.e., $E _ { \mathrm { i d e } I } ( H ( p ( { \pmb x } | \mathrm { i d } )$ ; q x id , <sup>ð Þð Þð Þj ð Þj</sup>de<sup>fi</sup>ned on the probability space (I, P) where the distribution P of identity is assumed to be discretely uniform. Further, since x is fully functionally dependent on id, the true conditional distribution p(x|id) is deterministic, and hence $H ( p ( { \pmb x } | \mathrm { i d } ) ) = 0$ , ∀id. Therefore, it is suf<sup>fi</sup>cient to focus only on $E _ { \mathrm { i d e } I } ( D _ { K L } ( p ( { \pmb x } | \mathrm { i d } ) \parallel q ( { \pmb x } | \mathrm { i d } ) ) _ { } )$ , which involves two <sup>ð Þð Þð Þj ð Þj</sup>sources of a more stochastic nature: (1) an attacker's knowledge and guessing strategy represented as $q ( { \pmb x } )$ , and (2) the selected features f. More importantly, as illustrated later in Section 4, maximizing $E _ { \mathrm { i d e } I } ( D _ { K L } ( p ( { \pmb x } | \mathrm { i d } ) \parallel q ( { \pmb x } | \mathrm { i d } ) ) )$ is equivalent to maximizing the entropy <sup>ð Þð Þð Þj ð Þj</sup>of the true unconditional joint distribution marginalized over the eliminated factoids, i.e., $H ( p ( { \pmb x } ) )$ . Thus our approach to the optimization problem that focuses on $D _ { K L } ( p q )$ is essentially an application of the principle of maximum entropy. Finally, by applying the maximum entropy concept at different hierarchical levels, namely from domain, identity, to factoid, we obtain enhanced levels of assurance.

## 2.3. Literature review

The problem of feature selection has enjoyed signi<sup>fi</sup>cant attention in the areas where datasets with an overwhelming number of features are available, including machine learning, pattern recognition, and statistics. We refer the reader to [4,22] for a systematic survey and to [13] for a more timely treatment of the major approaches to feature selection in machine learning. In the case of supervised learning, the goal of feature selection is to <sup>fi</sup>nd an optimal subset of features such that the accuracy of the classi<sup>fi</sup>er is maximized, given an induction algorithm and a labeled training set. Thus feature selection can be formulated as an informed search problem, i.e., to search a best subset in the entire hypothesis space of all possible combinations of features. This problem is known to be

NP-hard for two reasons: (1) the underlying distribution over the entire feature space is unknown; and (2) an exhaustive search is intractable. Most feature selection algorithms resort instead to an approximate solution to <sup>fi</sup>nd a satisfactory subset instead. For example, decision tree algorithms [28,29] use mutual information as the heuristic metric to evaluate candidate features and greedy best-<sup>fi</sup>rst search as the organization of the search. However, decision trees suffer from the over<sup>fi</sup>tting problem when many features are irrelevant. Other feature selection algorithms may either use different evaluation heuristics, $\mathrm { e . g . }$ , correlation and classi<sup>fi</sup>cation accuracy, or apply different search strategies, e.g., hill-climbing and simulated annealing.

Based on their relationships with the associated induction algorithms, feature selection algorithms can be characterized as embedded, <sup>fi</sup>lter, or wrapper methods. The embedded methods incorporate feature selection as a built-in mechanism into the induction algorithm. Decision trees and neural networks fall into the embedded category. The <sup>fi</sup>lter approaches select features as a preprocessing step before induction, usually by exploiting some general characteristics of the training data and ignoring their effects on the induction algorithm. Examples of <sup>fi</sup>lter methods include the FOCUS algorithm [3] and the RELIEF algorithm [20]. The wrapper algorithms call the induction methods to assess alternative subsets and use the estimated accuracy of the induced classi<sup>fi</sup>er as the heuristic metric. The OBLIVION algorithm [24] is an example of the wrapper method; and many decision support problems tend to adopt wrapper methods [18,19]. Our proposed approach to feature selection in KBA adopts the wrapper idea and directly optimizes the objective function as in Eq. (1).

The same information-theoretic concepts has been adopted in a closely related area called privacy-preserving data mining [2,36], where the goal is to develop algorithms for disguising the original data in such a way that valuable patterns remain while private data is protected. Although the objective is quite different from that of security research and authentication in particular [34], the concept of entropy becomes the common fundamental measure. Speci<sup>fi</sup>cally, Agrawal and Aggarwal [1] proposed $2 ^ { H ( p ( x ) ) }$ as a measure of privacy of a random variable x; and used mutual information $I ( f , f )$ to quantify how faithfully the original density f can be reconstructed from the distorted data as the estimate $f .$ Sweeney [34] addressed the privacy-preserving problem from the perspective of anonymity. Essentially, anonymity is measured by $H ( p ( \mathrm { i d } | x _ { \mathrm { i d } } ^ { \prime } ) )$ where $\chi _ { \mathrm { i d } } ^ { \prime }$ is a modi<sup>fi</sup>ed feature value associated with id; and the proposed kanonymity protection can be achieved through generalization and suppression.

## 3. KBA model and metrics

Having formulated the feature selection problem, we now turn our attention to the KBA problem as a whole. We adopt a generative view [27], particularly Bayesian classi<sup>fi</sup>ers [11] as the underlying inductive paradigm for the KBA problem. To relax the naïve Bayes assumption, we model factoid dependency as a high-order Markov chain. Next, we brie<sup>fl</sup>y present the KBA model for the sake of readability and completeness of this work. For a detailed treatment, we refer the reader to [8].

## 3.1. A generative probabilistic model of KBA

## De<sup>fi</sup>nition 1. (Bayesian network model of KBA)

A Bayesian network model of KBA (BN-KBA) is de<sup>fi</sup>ned by a threetuple:

$$
\mathrm{BN-KBA} \stackrel {\text { def }} {=} (y, x, \theta).\tag{2}
$$

1. y is the class variable denoting the authenticity of a claimed identity, with possible outcomes {true, false} or a short notation $\{ 1 , - 1 \} ;$

2. $\pmb { x } { = } ( x _ { 1 } , . . . . , x _ { i } { , . . . } , x _ { n } )$ is the random vector of n selected factoids, with each variable x denoting the correctness {correct, wrong}, or the same short notation {1, −1}, of a claimant's response to the ith selected factoid; and

3. θ is the parameter set encoding the dependency relationships; speci<sup>fi</sup>cally,

$$
\theta = \left(p (y), \{p (x _ {i} | \pi (x _ {i})) \} _ {i = 1} ^ {n}\right),\tag{3}
$$

where π(x ) is the set of variables on which x is dependent, satisfying ${ \pmb y } \in { \pmb \pi } ( x _ { i } ) , \forall i .$

Thus a BN-KBA models a joint probability distribution:

$$
p (y, \pmb {x}) = p (y) \prod_ {i = 1} ^ {n} p (x _ {i} | \pi (x _ {i})).\tag{4}
$$

Note that we use the same notation of x as in Section 2.1, where x denotes the randomvector of factoid values; and the context will make it clear which space of x we are referring to. A BN-KBA adopts a graphical structure more general than the naïve Bayes, as illustrated in Fig. 2.

BN-KBA assumes the following generative process for the authentication data from a KBA session with a claimant, either legitimate or fraudulent, given the claimed identity id:

1. Generate y\~Bernoulli (p(y)).

2. If y= 1, for i =1 to n:

(a) Generate x \~Bernoulli (p(x |y=1, π(x )\y, id)).

3. Else, for i = 1 to n:

(a) Generate x \~Bernoulli (p(x |y=−1, π(x )\y, id)).

According to the generative process of BN-KBA, we need to estimate three types of model parameters: (1) the class prior $p ( y ) ,$ (2) the likelihood $p ( x _ { i } | y = 1 , \pi ( x _ { i } ) \backslash y )$ or named as memorability m(x | $\pi ( x _ { i } ) \backslash y ) .$ , and (3) the likelihood $p ( x _ { i } | y = - 1 , \pi ( x _ { i } ) \backslash y )$ or named as guessability g(x | π(x )\y). Since a rational attacker tries to guess all factoids in the selected vector x as a whole, we need to <sup>fi</sup>rst estimate the guessability of x denoted as g(x), and then derive $g ( x _ { i } | \cdot )$ from g(x). Let us assume that an attacker employs a brute force attacking strategy that always shoots the highest frequent realization(s) of the feature vector x, the guessability of x or of the KBA system is:

$$
g (\boldsymbol {x}) = \max _ {\boldsymbol {x} \in \mathcal {A}} p (\boldsymbol {x}),\tag{5}
$$

where denotes the set of all possible realizations of x.

<sup>A</sup>The task of deriving g(x |·) from g(x) is essentially to model the dependency relationships between x and $\pi ( x _ { i } ) \backslash y .$ The goal is that the learned model parameterized with g(x |·) captures the guessability of x a rational attacker can obtain. Assuming that g(x) is the estimated optimal guessability, the idea is to apply the chain rule of conditional probability to factorize the joint guessability g(x) as a product of conditional guessabilities g(x |·):

$$
g (\pmb {x}) = \prod_ {i = 1} ^ {d} p (x _ {i} = 1 | \pmb {h} _ {i} = 1, y = - 1),\tag{6}
$$

where $\pmb { x } \mathrm { = } ( x _ { 1 } , . . . , x _ { d } )$ is a vector of d interdependent factoids, $\mathbf { h } _ { i } \mathbf { = } ( x _ { 1 } , . . . , x _ { i - 1 } )$ denotes the history of x or the factoids challenged before x , and $\mathbf { h } _ { i } = 1$ means the responses to all the factoid components of h are correct.

With a learned BN-KBA model which compactly encodes a joint distribution as in Eq. (4), we can compute the class posterior by Bayes rule, and then compare the class posterior with a prede<sup>fi</sup>ned acceptance threshold to make the authentication decision [8].

## 3.2. Rational attacker assumption

Without loss of generality, we make three assumptions regarding a rational attacker: (1) an attacker does not have prior knowledge about any particular identity, but may know something about the identity population in K; (2) an attacker consistently applies a certain attacking strategy such as a brute force attack to guessing the selected subset of factoids x associated with all targeted identities; and (3) a KBA system only permits one trial of in-band attack and blocks further attempts [6]. Formally, an attacking strategy is de<sup>fi</sup>ned as a multivariate multinomial: q(x)≡Multinomial (β), where $\beta \mathrm { = } ( \beta _ { 1 } , . . . , \ \beta _ { j } , . . . , \ \beta _ { k } )$ is the multinomial parameter, $\begin{array} { r } { \sum _ { j = 1 } ^ { k } \beta _ { j } = 1 } \end{array}$ , and β is the probability that the attacker guesses x with the jth guessing vector realization. Likewise, the true joint distribution of x is: p(x)≡Multinomial (α). Let denote the set of all guessing realizations. We conservatively assume that $B \subseteq A .$ Further, we de<sup>fi</sup>ne three brute force strategies with respect to x <sup>B A</sup>as follows,

1. A generic brute force strategy: $\beta = \left( \frac { 1 } { | \mathcal { A } | } , \cdot \cdot \cdot \frac { 1 } { | \mathcal { A } | } \right)$

<sup>jAj</sup>2. A sophisticated brute force strategy: β=α.

3. A deterministic brute force strategy: $\beta = ( q ( \pmb { x } \in \mathcal { B } ) = 1 , q ( \pmb { x } \notin \mathcal { B } ) = 0 )$ where $B = \left\{ \pmb { a } _ { i } : p ( \pmb { x } = \pmb { a } _ { i } ) = m a x _ { \pmb { x } \in \mathcal { A } } p ( \pmb { x } ) \right\} \subseteq A .$

Indeed, from a game-theoretic view, a KBA problem can be formulated as a two-player zero-sum deterministic game with incomplete information [37] between a KBA system and an attacker. We have shown in [8] that all three strategies can be rational in different situations with regard to knowledge shared between both players. The generic brute force strategy is the equilibrium strategy if the attacker does not know the true distribution $p ( { \pmb x } )$ other than all possible realizations ; the deterministic brute force strategy is the equilibrium strategy and the best among the three given that an attacker knows $p ( { \pmb x } )$ at the domain level; and the sophisticated brute force strategy is a rational choice under circumstances lying between the above two extremes.

![](/api/attachments/S4P2U832/fulltext/images/900aa09c1be98e8edc828aa6fafe1b0dff3a6dbed33f9f8111ae76e10d8790ea.jpg)

![](/api/attachments/S4P2U832/fulltext/images/85bf2016c7432df44963b3871e0c18466c75d8a5a39dc1c236ae752f1ec8a4b4.jpg)

![](/api/attachments/S4P2U832/fulltext/images/b863c2aa47f7cd4c85029a86dcb4f26357dc03beaed680e02a447e6c2b3b9b00.jpg)  
Fig. 1. Graphical model representations of adaptive feature selections. The rectangles or plates represent replicates. The outer plate represents KBA domains K; the middle plate represents identities id within a domain; and the inner plate represents selected factoids f for an identity. (a) Domain-adaptive feature selection, (b) identity-adaptive feature selection, and (c) response-adaptive feature selection

## 4. Adaptive feature selection

In this section, we present three feature selection algorithms of increasing adaptivity based on the principle of maximum entropy, namely, domain-adaptive, identity-adaptive, and response-adaptive methods. To understand their differences, we show the graphical model representations in Fig. 1. All three feature selection schemes shown in Fig. $1 ( \mathsf { a } ) , ( \mathsf { b } ) ,$ , and (c), are three-level hierarchical models; K, F, and I are domain-level variables; id and x are identity-level variables; and $f _ { i }$ and $x _ { i }$ are factoid- or response-level variables. As the <sup>fi</sup>gure makes clear, the difference lies in the level at which one introduces the factoid subset variable f. As formulated in Section 2.2, the objective is to maximize the KL divergence $D _ { K L } ( p q )$ between the true distribution p (x) and the guessing distribution q(x) with respect to f.

## 4.1. Domain-adaptive feature selection (DomFS)

As the name suggests, domain-adaptive feature selection aims to <sup>fi</sup>nd the optimal subset of factoids for an entire domain K. Thus the selected factoid vector f is a domain-level variable, as shown in Fig. 1 (a). The feature selection algorithm is executed once for each domain, and the selected optimal factoid vector is used for all subsequent authentication sessions regardless of the claimed identity. As suggested in Section 3.2, we consider two attacking strategies: the deterministic and the sophisticated brute force strategies. To formalize the domain-adaptive feature selection method, we provide the following theorems.

Theorem 1. (DomFS under deterministic brute force attacking strategy)

If a rational impostor employs a deterministic brute force strategy, the optimal subset of factoids at the domain level is:

$$
\boldsymbol {f} ^ {*} = \arg \min _ {\boldsymbol {f} \subseteq F} \max _ {\boldsymbol {x} \in \mathcal {A}} p (\boldsymbol {x} | \boldsymbol {f}).\tag{7}
$$

Proof. Since the deterministic brute force strategy, along with the resulting guessability in Eq. (5), is the optimal among all multinomial attacking strategies, we want to select a subset of factoids such that the maximum guessability an impostor can obtain is minimized. □

Theorem 2. (DomFS under sophisticated brute force attacking strategy)

If a rational impostor employs a sophisticated brute force strategy characterized by β = α at the domain level, the optimal subset of factoid at the domain level is:

$$
\boldsymbol {f} ^ {*} = \arg \max _ {\boldsymbol {f} \subseteq F} H (p (\boldsymbol {x} | \boldsymbol {f})).\tag{8}
$$

Proof. $p ( { \pmb x } | { \pmb f } )$ is the conditional probability distribution of a factoid vector x given f, which we compactly note as p(x), and in a similar manner we get $q ( { \pmb x } )$ and $H ( p ( { \pmb x } ) )$ . Under the sophisticated brute force strategy, the guessing multinomial is $\beta = q ( { \pmb x } ) = p ( { \pmb x } )$ at the domain level. By the rationality assumptions made in Section 3.2, we have,

$$
q (\boldsymbol {x}) = q (\boldsymbol {x} | \mathrm{id}), \forall \mathrm{id}.\tag{9}
$$

However, the true distribution of x given a targeted identity differs substantially from that at the domain level. Speci<sup>fi</sup>cally,

$$
p (\boldsymbol {x} | \mathrm{id}) = \left\{ \begin{array}{l l} 1 & \text { if } \boldsymbol {x} = \boldsymbol {x} _ {i d}, \\ 0 & \text { otherwise }, \end{array} \right.\tag{10}
$$

Table 1 A KBA domain example

<table><tr><td>id</td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td></tr><tr><td>User1</td><td> $a_{11}$ </td><td> $a_{21}$ </td><td> $a_{31}$ </td><td> $a_{41}$ </td></tr><tr><td>User2</td><td> $a_{11}$ </td><td> $a_{21}$ </td><td> $a_{31}$ </td><td> $a_{42}$ </td></tr><tr><td>User3</td><td> $a_{11}$ </td><td> $a_{22}$ </td><td> $a_{31}$ </td><td> $a_{42}$ </td></tr><tr><td>User4</td><td> $a_{11}$ </td><td> $a_{22}$ </td><td> $a_{32}$ </td><td> $a_{42}$ </td></tr><tr><td>User5</td><td> $a_{11}$ </td><td> $a_{22}$ </td><td> $a_{32}$ </td><td> $a_{42}$ </td></tr><tr><td>User6</td><td> $a_{12}$ </td><td> $a_{21}$ </td><td> $a_{31}$ </td><td> $a_{41}$ </td></tr><tr><td>User7</td><td> $a_{12}$ </td><td> $a_{22}$ </td><td> $a_{31}$ </td><td> $a_{41}$ </td></tr><tr><td>User8</td><td> $a_{12}$ </td><td> $a_{22}$ </td><td> $a_{32}$ </td><td> $a_{42}$ </td></tr></table>

where $\pmb { x } _ { \mathrm { i d } }$ denotes id's realization of $\pmb { x } .$ In other words, p(x|id) is deterministic. According to the objective in Eq. (1), and assuming the impostor attacks each identity id with equal likelihood, the expected KL divergence between p and q, given an identity id under attack, reads:

$$
\begin{array}{r l} & {\mathbb {E} _ {\mathrm{id} \in I} (D _ {K L} (p | | q)) = \sum_ {\mathrm{id} \in I} p (\mathrm{id}) \sum_ {\boldsymbol {x} \in \mathcal {A}} p (\boldsymbol {x} | \mathrm{id}) l o g \frac {p (\boldsymbol {x} | \mathrm{id})}{q (\boldsymbol {x} | \mathrm{id})}} \\ & {\quad = - \sum_ {\mathrm{id} \in I} p (\mathrm{id}) l o g q (\boldsymbol {x} = \boldsymbol {x} _ {\mathrm{id}} | \mathrm{id})} \\ & {\quad = - \sum_ {\mathrm{id} \in I} p (\mathrm{id}) l o g q (\boldsymbol {x} = \boldsymbol {x} _ {\mathrm{id}})} \\ & {\quad = - \sum_ {\boldsymbol {x} \in \mathcal {A}} p (\boldsymbol {x}) l o g p (\boldsymbol {x}) = H (p (\boldsymbol {x})).} \end{array}\tag{11}
$$

Eq. (11) shows that maximizing the expected KL divergence between p and q at the identity level is equivalent to maximizing the entropy of x at the domain level. Hence Eq. (8) holds. □

Theorems 1 and 2 de<sup>fi</sup>ne the optimal domain-adaptive feature selection methods under two different rational attacking strategies. But both approaches are closely related to each other. Indeed, the two feature selection schemes are uni<sup>fi</sup>ed by the principle of maximum entropy. By Theorem 1, as in Eq. (7), we select the optimal feature vector that minimizes the probability of the most frequent vector realization; this has a direct effect of raising the joint entropy of x. By Theorem 2, as in Eq. (8), because the guessing distribution β of the sophisticated brute force attacking strategy is more stochastic than that of the deterministic brute force strategy, we directly maximize its entropy, or equivalently, the entropy of the true empirical distribution α at the domain level with respect to f. The common intuition is that the higher the entropy of the selected factoid vector, the more secure the resulting KBA system. Having formalized the domain-adaptive feature selection approaches, the algorithm is straightforward. We present the algorithm based on Theorem 1 in Algorithm 1. For Theorem 2, a similar algorithm can be readily developed.

## Algorithm 1. BN-KBA domain-adaptive feature selection

```txt
Input: n the number of selected factoids; F the set of all factoids; K the factoid values of all true identities.
Output: f* the optimal subset of factoids; x* the most frequent vector realization given f*.
/* Initialization */  
1 f* = 0;  
2 x* = 0;  
3 min_max_p = +∞;  
/* Minimize the maximum probability of the vector realization */  
4 foreach combination of n factoids f ⊆ F do  
5 max_p = max_x ∈ A p(x | f, K);  
6 max_x = arg max_x ∈ A p(x | f, K);  
7 if max_p < min_max_p then  
8 f* = f;  
9 min_max_p = max_p;  
10 x* = max_x;  
11 end  
12 end  
13 return(f*, x*);
```

![](/api/attachments/S4P2U832/fulltext/images/164cb8034b8d34194100e35dc9eb18ada65e1d2baa8e06c66bd6f97eb8dac3aa.jpg)  
Fig. 2. Adaptive feature selection methods. (a)–(f) correspond to 6 candidate factoid subsets, where each is a 2-vector. The upper part of each sub<sup>fi</sup>gure is the scatter plot of the two selected factoids, where each circle denotes an identity and the dark circles represent the claimed identity, i.e., User6. The lower part of each sub<sup>fi</sup>gure indicates their dependency directions in the BN. Results of adaptive feature selections: 1) Domain-adaptive: (a). (b) (d) or (f): 2) Identity-adaptive: (a): 3) Response-adaptive $\left( \mathbf { a } \right) \mathrm { i f } \ r _ { 1 } = a _ { 1 2 } , \left( \mathbf { c } \right) \mathrm { i f } \ r _ { 1 } = a _ { 1 1 } .$

Example 1. To further elucidate our idea, we consider a toy problem. Table 1 gives an example of a KBA domain that contains eight identities and four factoids, along with their true factoid values. Out of $F { = } \{ f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 } \} ,$ , suppose we want to select a 2-vector of factoids f. As shown in Fig. 2, we have ${ \binom { 4 } { 2 } } _ { c } = 6$ candidate subsets. By the domainadaptive feature selection as formalized in Algorithm 1, we should select the factoid vectors in Fig. 2(a), (b), (d), or (f), since their most frequent 2-vector realizations have probability <sup>3</sup>, which is the minimum in this domain.

## 4.2. Identity-adaptive feature selection (IdtFS)

Since the domain-adaptive feature selection uses a same subset of factoids for all claimants or KBA sessions, it actually aims to protect all identities in the domain as a whole or on average. In other words, for a speci<sup>fi</sup>c identity, this approach is not necessarily the optimal one. To address this issue, we propose the second method, called identityadaptive feature selection, which takes advantage of the fact that we can always recognize which identity an intruder is attacking before challenging him. In terms of adaptivity, we move from the domain level to the identity level. Given the claimed identity id the objective is to <sup>fi</sup>nd the optimal subset of factoids such that their values for id are the most dif<sup>fi</sup>cult to guess. Thus the selected factoid vector f is an identity-level variable, as shown in Fig. 1(b). The identity-adaptive algorithm is performed once for each identity, thus the resulting factoid subsets may be different for different identities. The motivation is that, by adapting the KBA system to distinct identities, the overall assurance level can be improved. At the identity level, it is suf<sup>fi</sup>cient to assume an impostor adopts the sophisticated brute force attacking strategy, since the deterministic brute force strategy entails zero guessability for those identities with less frequent vector realizations. Thus, the selection criteria turns out to be intuitive as follows.

## Theorem 3. (IdtFS under sophisticated brute force attacking strategy)

If a rational impostor employs a sophisticated brute force strategy and claims the identity id, the optimal subset of factoids for id is:

$$
\boldsymbol {f} ^ {*} = \arg \max _ {\boldsymbol {f} \in F} h (\boldsymbol {x} _ {\mathrm{id}} | \boldsymbol {f}),\tag{12}
$$

where $h ( \mathbf { x } _ { i d } )$ is the Shannon information content or the entropy of the outcome ${ \bf x } _ { i d } o f { \bf x } ,$ and defined $b y - l o g p ( \mathbf { x } \mathrm { = } \mathbf { x } _ { i d } ) .$

Proof. Given the claimed identity id and under the sophisticated brute force strategy, the KL divergence between p and q reads:

$$
\begin{array}{c} D _ {K L} (p | | q) = \sum_ {\boldsymbol {x} \in \mathcal {A}} p (\boldsymbol {x} | \mathrm{id}) l o g \frac {p (\boldsymbol {x} | \mathrm{id})}{q (\boldsymbol {x} | \mathrm{id})} \\ = - l o g q (\boldsymbol {x} = \boldsymbol {x} _ {\mathrm{id}} | \mathrm{id}) \\ = - l o g   q (\boldsymbol {x} = \boldsymbol {x} _ {\mathrm{id}}) = - l o g   p (\boldsymbol {x} = \boldsymbol {x} _ {\mathrm{id}}). \end{array}\tag{13}
$$

Hence, Eq. (12) follows from the objective function in Eq. (1). In fact, Theorem 2 considers the expected $D _ { K L } ( p | | q )$ over all identities. □

Identity-adaptive feature selection is intuitive in the sense that, through this method, we want to select the factoids such that id's values are as surprising or uncommon to an attacker as possible. In the language of probability, the optimal factoid subset $f ^ { * }$ minimizes p $\scriptstyle ( \pmb { x } = \pmb { x } _ { \mathrm { i d } } )$ , or equivalently, maximizes $h ( \pmb { x } _ { \mathrm { i d } } )$ . Therefore, the identityadaptive approach complies with the principle of maximum entropy at the identity level. According to Theorem 3, Algorithm 2 outlines the procedure of identity-adaptive feature selection.

Example 2. Let us revisit the KBA domain speci<sup>fi</sup>ed in Table 1, and further assume that the claimed identity id=User6, represented by the dark circles in Fig. 2. The true values of id are $( a _ { 1 2 } , \ a _ { 2 1 } , \ a _ { 3 1 } , \ a _ { 4 1 } ) .$ According to Algorithm 2, the optimal factoid subset is in $\mathrm { F i g . } 2 ( \mathsf { a } ) ,$ , i.e., $f ^ { * } { = } \left( x _ { 1 } , x _ { 2 } \right)$ , which has the minimum probability $\begin{array} { r } { p ( { \pmb x } = { \pmb x } _ { \mathrm { i d } } ) = \frac { 1 } { 8 } } \end{array}$ and the maximum outcome entropy $h ( \pmb { x } _ { \mathrm { i d } } ) = 3$

## Algorithm 2. BN-KBA identity-adaptive feature selection

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: id the claimed identity; n the number of selected factoids; F the set of all factoids; K the factoid values of all true identities.
Output: f* the optimal subset of factoids;  $x_{id}$  the factoid vector realization of id.
/* Initialization */  
1  $f^{*} = \emptyset$ ;
2 min_p = +∞;
/* Get id's factoid values from K */  
3  $X_{id} = \text{getIDVal}(id)$ ;
/* Minimize the probability of id's vector realization w.r.t. f */  
4 foreach combination of n factoids  $f \subseteq F$  do
5    p_id = p(x =  $x_{id} \mid f, K$ );
6    if p_id &lt; min_p then
7    f* = f;
8    min_p = p_id;
9    end
10 end
11 return( $f^{*}, x_{id}$ );
</div>

## 4.3. Response-adaptive feature selection (ResFS)

It is natural to extend the adaptive feature selection to the factoid or response level. In this method, the selection of the next optimal factoid is conditioned on the claimant's responses to the previous factoids. This method will always choose the next question such that the guessability of the vector consisting of the remaining factoids to be challenged as a whole, given the claimed identity id, is the lowest or the outcome entropy is the maximum. As shown in Fig. 1(c), the selected factoid vector f now becomes a factoid-level variable. By the response-adaptive method, feature selection is carried out on-the-<sup>fl</sup>y and is not complete until the challenge–response session ends. The response-adaptive approach can be motivated by the following observation. An impostor applying a sophisticated brute force attacking strategy may get correct responses to a signi<sup>fi</sup>cant part of the factoid vector, thus obtaining a suf<sup>fi</sup>cient class posterior or authentication score. For instance, consider that an impostor claims the identity User6 to a KBA modeled as Fig. 2(a), and adopts the sophisticated brute force strategy characterized by $\beta = \alpha \mathbf { = } p ( \pmb { x } )$ . Based on the analysis in the identity-adaptive selection, the impostor only has $\frac 1 8$ chance to hack both challenges. However, since the impostor also guesses $( a _ { 1 1 } , a _ { 2 1 } )$ and $( a _ { 1 2 } , a _ { 2 2 } )$ with a probability <sup>2</sup> for each, he still has 50% chance to guess exactly one question correctly, given User6's realization $( a _ { 1 2 } , a _ { 2 1 } ) .$ . The response-adaptive feature selection aims to address this issue. Formally, we have the following theorem.

## Theorem 4. (ResFS under sophisticated brute force attacking strategy)

Suppose a rational impostor employs a sophisticated brute force strategy; claims the identity id; and has responded to the previous factoid challenges ${ \pmb x } _ { p r e v }$ with ${ \bf r } _ { p r e \nu }$ . The optimal remaining subset of factoids for id is:

$$
\boldsymbol {f} ^ {*} = \underset {\boldsymbol {f} ^ {\prime} \subseteq F ^ {\prime}} {\arg \max} h \left(\boldsymbol {x} _ {\mathrm{id}} ^ {\prime} | \boldsymbol {x} _ {\text { prev }} = \boldsymbol {r} _ {\text { prev }}, \boldsymbol {f} ^ {\prime}\right),\tag{14}
$$

where the superscript ‘′’ stands for the vector of the remaining factoids to be selected, the subscript ‘prev’ denotes the previous factoids having been challenged against, and $h ( \pmb { x } _ { i d } ^ { \prime } )$ is calculated within the scope of $\mathbf { \dot { x } } _ { p r e v } = \mathbf { r } _ { p r e v }$ To select the next single factoid, we can apply the same heuristic to choosing one from $\pmb { f } ^ { * }$

Proof. Given the claimed identity id, the previous responses $\pmb { r } _ { p r e { \nu } }$ and under the sophisticated brute force strategy, the KL divergence between p and q over the space of the remaining selected factoids is:

$$
\begin{array}{r l} D _ {K L} (p | | q) & = \sum_ {\boldsymbol {x} ^ {\prime}} p \big (\boldsymbol {x} ^ {\prime} | \boldsymbol {x} _ {\text {prev}} = \boldsymbol {r} _ {\text {prev}}, \text {id} \big) \log \frac {p \big (\boldsymbol {x} ^ {\prime} | \boldsymbol {x} _ {\text {prev}} = \boldsymbol {r} _ {\text {prev}} , \text {id} \big)}{q \big (\boldsymbol {x} ^ {\prime} | \boldsymbol {x} _ {\text {prev}} = \boldsymbol {r} _ {\text {prev}} , \text {id} \big)} \\ & = - \log q \big (\boldsymbol {x} ^ {\prime} = \boldsymbol {x} _ {\text {id}} ^ {\prime} | \boldsymbol {x} _ {\text {prev}} = \boldsymbol {r} _ {\text {prev}}, \text {id} \big) \\ & = - \log q \big (\boldsymbol {x} ^ {\prime} = \boldsymbol {x} _ {\text {id}} ^ {\prime} | \boldsymbol {x} _ {\text {prev}} = \boldsymbol {r} _ {\text {prev}} \big) \\ & = - \log p \big (\boldsymbol {x} ^ {\prime} = \boldsymbol {x} _ {\text {id}} ^ {\prime} | \boldsymbol {x} _ {\text {prev}} = \boldsymbol {r} _ {\text {prev}} \big). \end{array}\tag{15}
$$

Hence, by the objective function in Eq. (1), Eq. (14) holds. Further, the next single factoid is selected by scanning the individual factoids in $\pmb { f } ^ { \ast }$ and choosing the one that maximizes the same objective in Eq. (15). □

It is worth mentioning that the selection of the next factoid will be restricted within the optimal vector of the remaining factoids, which is essentially identity-adaptive selection conditioned on the previous responses. The idea is to avoid local optima. In fact, if an impostor answers all previous questions correctly, the resulting whole optimal factoid subset is identical to the one selected by the identity-adaptive approach. The detailed algorithm is shown in Algorithm 3.

Example 3. Again, consider the scenario in Table 1, given id=User6 and $n = 2 .$ . We <sup>fi</sup>rst select $( x _ { 1 } , x _ { 2 } )$ before issuing any challenge, which is equivalent to the identity-adaptive method. We then select $x _ { 1 }$ <sup>fi</sup>rst by a natural tie-breaking since $h ( x _ { 1 } = a _ { 1 2 } ) = h ( x _ { 2 } = a _ { 2 1 } ) = 1 . 4 2$ . Suppose we get a response $\scriptstyle { \mathsf { a } } _ { 1 2 } ,$ , which is correct, we should choose x as the second factoid since $h ( x _ { 2 } = a _ { 2 1 } | x _ { 1 } = a _ { 2 1 } ) = 1 . 5 8$ is the maximum among $\{ x _ { 2 } , x _ { 3 } ,$ $x _ { 4 } \} _ { \cdot }$ If the response to x is wrong, $\mathrm { i } . \mathrm { e } . , a _ { 1 1 }$ , the optimal second factoid is $x _ { 4 }$ since $h ( x _ { 4 } = a _ { 4 1 } | x _ { 1 } = a _ { 1 1 } ) = 2 . 3 2$ is the largest. Recall the aforementioned motivating example, given the <sup>fi</sup>rst response $a _ { 1 1 } ,$ we select $x _ { 4 }$ instead of $x _ { 2 }$ as the second factoid to minimize the probability that an impostor guesses the second challenge correctly. A gametheoretic interpretation follows. Given the <sup>fi</sup>rst response $a _ { 1 1 } ,$ we can infer that the rational attacker is using a guessing realization $( a _ { 1 1 } , \cdot ) .$ . Under the sophisticated brute force strategy, we can use this knowledge to more precisely predict his guess of the second factoid, assuming that the impostor knows the true joint distribution or the dependency relationship at the domain level. Therefore, in the response-adaptive method, even for the same targeted identity, the factoid vector selected can be different depending on the claimant's responses.

From domain-adaptive, identity-adaptive, to response-adaptive feature selections, the gained adaptivity, however, is at the expense of more computational cost. This re<sup>fl</sup>ects the trade-off between security and other criteria such as usability, cost, and ef<sup>fi</sup>ciency. Fortunately, our experiments show that the increase in computing time is not only acceptable but also justi<sup>fi</sup>able.

## 5. Experiments

To empirically validate the contributions of our proposed approach to adaptive feature selection in KBA, we consider two hypotheses:

## Algorithm 3. BN-KBA response-adaptive feature selection

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: id the claimed identity; n the number of selected factoids; F the set of all factoids; K the factoid values of all true identities.

Output: f* the optimal n-vector of factoids; r the responses to the optimal factoids w.r.t. id;  $x_{id}$  id's factoid vector realization.

/* Declaration and Initialization */

1  $f^{*} = (f[1],...,f[n])$ ;

2  $r = (r[1],...,r[n])$ 

3  $F' = F$ ;

4  $f^{*} = 0$ ;

5  $r_{prev} = 0$ ;

/* Get id's realization from K */ 

6  $X_{id} = \text{getIDVal}(id)$ ;

/* Stepwise choose fractoids */ 

7 for i = to n do

/* Num left to be selected */ 

8  $n' = n - i + 1$ ;

/* Select the optimal remaining  $n'$ -vector */ 

9  $min\_p = +\infty$ ;

10 foreach  $n'$ -vector  $f' \subseteq F'$  do

11    p_id = p( $x = x_{id} | x_{prev} = r_{prev}, f', K$ );

12    if p_id &lt; min_p then

13    $f^{*} = f'$ ;

14    min_p = p_id;

15    end

16 end

/* Select the next facloid among  $f^{*}$ */

17  $min\_p = +\infty$ ;

18 foreach  $f \subseteq f^{*}$  do

19    p_id = p( $x = x_{id} | x_{prev} = r_{prev}, f, K$ );

20    if p_id &lt; min_p then

21    f[i] = f;

22    min_p = p_id;

23    end

24 end

/* Get response to the current factoid */ 

25 r[i] = getIdRes(f[i]);

/* Update round variables */ 

26  $F' = F'\setminus f[i]$ ;

27  $r_{prev} = r_{prev} \cup r[i]$ ;

28 end

29 return( $f^{*}, r, x_{id}$ );
</div>

Hypothesis 1. Adaptive feature selection methods are superior to random selection in terms of authentication accuracy and error rates.

Hypothesis 2. As the level of adaptivity increases, the corresponding feature selection methods improve signi<sup>fi</sup>cantly in terms of authentication accuracy and error rates.

## 5.1. Experimental setup

In security domain, the access to historical fraudulent or malicious data is typically restricted for con<sup>fi</sup>dentiality, privacy and expense concerns (the popularity of the Enron Email corpus is an interesting example [21]). Another caveat lies in using historical data to <sup>fi</sup>t a predictive model for the authentication purpose, given that the behaviors of impostors are by nature unpredictable. Thus we adopt a Markov Chain Monte Carlo (MCMC) method [12] to generate claimant samples. It is also suf<sup>fi</sup>cient to demonstrate our idea by constructing a dataset of legitimate users constituting a domain K. A unifying information-theoretic view of simulating the entire dataset is the generative model shown in Fig. 3.

The <sup>fi</sup>rst step is to generate a KBA domain from the “original” information source , which is characterized by a set of parameters or summary statistics: $\Theta = \{ \alpha _ { v } \} _ { v = 1 } ^ { V }$ , where $\alpha _ { v }$ de<sup>fi</sup>nes a multinomial distribution of a candidate factoid $x _ { \nu } .$ Given the source parameter Θ, the generative process for a KBA domain K of U genuine users is straightforward:

1. For each of the U genuine users:

(a) Generate a unique ${ \mathrm { i d } } _ { u } .$

(b) For each of the V candidate factoids $x _ { v } .$

i. Generate $\boldsymbol { x } _ { v ^ { \prime } }$ \~ Multinomial(α ).

Each factoid value is sampled independently, but the resulting empirical joint distribution $p ( { \pmb x } )$ will typically show some dependencies.

Having sampled a KBA domain K, we obtain a snapshot of the domain-level parameters: $\theta = ( p ( y ) , \{ m ( x _ { \nu } ) \} _ { \nu = 1 } ^ { V } , \{ g ( x _ { \nu } ) \} _ { \nu = 1 } ^ { V } \bar { ) }$ , where p(y) is the class prior, $m ( x _ { \nu } )$ is the memorability of the vth candidate factoid, and $g ( x _ { \nu } )$ is the guessability. Here we only keep the marginal distributions m(x ) and $g ( x _ { \nu } )$ for the sake of claimant generation. The estimation of these model parameters has been discussed in Section 3. From the KBA domain characterized by θ, the generative process for M claimants follows:

1. For each of the M claimants:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(a) Generate $y\sim$ Bernoulli $(p(y))$ (b) Generate the claimed id $\sim$ Uniform $(\{\mathrm{id}_u\}_1^U)$ (c) For each of the $V$ responses $r_v$ to $x_{v}$: i. If $y = 1$, generate the correctness $c_{v}\sim$ Bernoulli $(m(x_{v}))$ A. If $c_{v} = 1$, $r_v = x_v$ B. Else, $r_v =$ Uniform $(A_{v}\backslash x_{v})$ ii. Else, $r_v\sim$ Multinomial $(\alpha_{v})$
</div>

Here $A _ { v }$ denotes the set of all possible outcomes of $x _ { v }$ . By this generative process, we model an impostor who employs a sophisticated brute force strategy $\beta _ { v } = \alpha _ { v }$ for each factoid independently. In other words, we do not model a claimant to explicitly leverage the knowledge about the possible dependency relationship between factoids, which would involve real-time gaming with the KBA system, i.e., the next trying probability depends on the previous challenges and responses, and thus is infeasible for an ordered sampling. The stepwise guessing strategy exploiting dependency knowledge is what the response-adaptive model tries to protect against. Thus we cannot expect the response-adaptive approach to outperform the identityadaptive selection on this particular dataset. On the other hand, if the response-adaptive model performs comparably to the identityadaptive model, it will justify the potential of the response-adaptive model; because we have already analytically explained that the response-adaptive feature selection method can trap the attackers who want to exploit some dependency knowledge.

Table 2  
![](/api/attachments/S4P2U832/fulltext/images/5fc357706ea38d78e7a259a503f4a0fb8bce3aee4f7df63e1ec0e0abd725c59f.jpg)  
Fig. 3. The generative model for a synthetic dataset.

With the generated dataset of both the KBA domain and claimants, we can compare four feature selection methods. Other than the three proposed adaptive methods, we also implemented a random feature selection method (RanFS) as a baseline model as suggested by Chokhani [10]. Compared with our adaptive methods, the random feature selection method chooses and orders the factoids uniformly randomly for each KBA session.

We ran R=10 independent replications for each feature selection method, with each replication authenticating M=1000 claimant samples. The dataset of R×M claimants is consistent across four models. The KBA domain tested consists of V=5 candidate factoids and U=1000 identities, which are <sup>fi</sup>xed across replications and models. The performance measures are adopted from other conventional authentication methods such as biometrics [15]:

1. Accuracy = The percentage of claimants being correctly authenticated.

2. False Acceptance Rate (FAR) = The percentage of impostors being incorrectly accepted as genuine users.

3. False Rejection Rate (FRR) = The percentage of genuine users being incorrectly rejected.

4. Equal Error Rate (EER) = The rate at which FAR is equal to FRR.

FAR, also known as Type II error, measures the security strength of a KBA system. FRR, or more generally Type I error, indicates the usability or inconvenience to genuine users. Thus FAR is of more interest for authentication. However, FAR and FRR are inadvertently traded off against each other by adjusting the acceptance threshold. A more regularized measure is EER or cross-over error rate (CER). The smaller the EER, the better the KBA system in the sense of a better balance between Type I and II errors. We report replication means of these measures. Table 2 summarizes the con<sup>fi</sup>guration of the experimental parameters.

## 6. Results

The replication means of the performance measures under different thresholds are plotted in Fig. 4. In terms of accuracy, the three adaptive feature selection methods remarkably outperform random selection, as shown in Fig. 4(a), especially when thres ≥0.5. In terms of error rates, the three adaptive selection methods have signi<sup>fi</sup>cantly lower FRR than random selection, as shown in Fig. 4(b). And the adaptive methods also obtain comparably small FAR rates. By closely examining Fig. 4(b), we can see the EERs of the adaptive approaches are all substantially smaller than that of random selection. The EER reduction from random selection to the response-adaptive method is about 40%. When comparing the three adaptive selection methods themselves, we <sup>fi</sup>nd the response-adaptive selection is slightly superior in both accuracy and error rates to the identityadaptive method, followed by the domain-adaptive method.

Experimental parameters

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Num of genuine users</td><td>U=1000</td></tr><tr><td>Num of claimants/replication</td><td>M=1000</td></tr><tr><td>Num of replications</td><td>R=10</td></tr><tr><td>Num of candidate factoids</td><td>V=5</td></tr><tr><td>Num of selected factoids</td><td>n=3 etc.</td></tr><tr><td>Class prior</td><td>p(y)=0.5 etc.</td></tr><tr><td>Memorability</td><td>m(xv)=0.9 etc., v=1...5</td></tr><tr><td>Guessability</td><td>{g(xv)}=(0.5, 0.3, 0.1, 0.2, 0.4) etc.</td></tr><tr><td>Threshold</td><td>thres=[0, 1]</td></tr></table>

One observation from our experiments is that the choice of the acceptance threshold is nontrivial. It is dif<sup>fi</sup>cult to interpret and justify an optimal threshold, especially when comparing across different models. We argue that the con<sup>fi</sup>guration of the threshold should be domainspeci<sup>fi</sup>c and dependent on the objective of assurance level. To eliminate the effect of threshold, we take a Bayesian view and consider the KBA as a probabilistic classi<sup>fi</sup>cation problem. Speci<sup>fi</sup>cally, to compute the performance measures, we count the soft or probabilistic labels:

1 . B a y e s a c c u r a c y = ∑<sup>M</sup> p y = 1 r<sub>j</sub> sign 1 + y<sub>j</sub>  + p y = −1 r<sub>j</sub>   sign 1−y<sub>j</sub>  .

2. Bayes $\begin{array} { r } { \mathrm { F A R } = \left( \sum _ { j = 1 } ^ { M } p \big ( y = 1 | \pmb { r _ { j } } \big ) s i g n \big ( 1 - y _ { j } \big ) \right) \div \sum _ { j = 1 } ^ { M } s i g n \big ( 1 - y _ { j } \big ) . } \end{array}$

3. Bayes $\begin{array} { r } { \mathrm { F R R } = \ \left( \sum _ { j = 1 } ^ { M } p \big ( y = - 1 | r _ { j } \big ) s i g n \big ( 1 + y _ { j } \big ) \right) \div \sum _ { j = 1 } ^ { M } \mathrm { ~ s i g n } \big ( 1 + y _ { j } \big ) . } \end{array}$

Here j indexes a claimant, r<sub>j</sub> denotes the claimant's responses, and y is the known class label. sign(x) is the sign function, thus sign(1 +y )

a  
![](/api/attachments/S4P2U832/fulltext/images/73a02adb797b28bec5e0c07261a4d94491a59d9fc11aeb8a6ef63da93605c2fd.jpg)

b  
![](/api/attachments/S4P2U832/fulltext/images/1ce4b7fddcd5a85e7111f6679d742b43917b9491126bb8237e2447ebdd1c19ae.jpg)  
Fig. 4. Performance measures under different thresholds. (a) Accuracy, and (b) error rates

Table 3  
Comparison of feature selection methods

<table><tr><td>Model</td><td>Bayes accuracy</td><td>Bayes FAR</td><td>Bayes FRR</td><td>Time (ms/session)</td></tr><tr><td>Random selection</td><td>0.8892</td><td>0.0744</td><td>0.1469</td><td>223</td></tr><tr><td>Domain-adaptive</td><td>0.9253</td><td>0.0522</td><td>0.0971</td><td>17</td></tr><tr><td>Identity-adaptive</td><td>0.9357</td><td>0.0630</td><td>0.0655</td><td>267</td></tr><tr><td>Response-adaptive</td><td>0.9415</td><td>0.0601</td><td>0.0569</td><td>494</td></tr></table>

yields 1 if $y _ { j } = 1$ for a genuine user and 0 if $y _ { j } { = } { - } 1$ for an impostor. The performance measures under the Bayesian view is presented in Table 3. The results con<sup>fi</sup>rm both hypotheses. Because the Bayes measures eliminate the impact of threshold, the adaptive methods surpass random selection in accuracy, FRR, and FAR. Also, we report the average computational time for each KBA session under four feature selection schemes. As shown in the last column of Table 3, as the level of adaptivity increases, more computational time was committed. But the increase is moderate under a typical hardware environment. In terms of computational time, the domain-adaptive approach is especially appealing. Finally, we performed a sensitivity analysis by systematically changing the experimental parameters, including number of selected factoids $( n { = } 1 . . . 5 )$ , class prior $\scriptstyle ( p ( y = 1 )$ $= 0 . 5 . . . 0 . 9 )$ , memorability, and guessability. The results exhibited the same patterns and con<sup>fi</sup>rmed our earlier observations.

## 7. Conclusion

In this paper, we <sup>fi</sup>rst formally addressed the problem of feature selection in the context of KBA. Based on a Bayesian network model of KBA, the proposed feature selection methods <sup>fi</sup>nd their root in statistical modeling and information theory. Further, under some rationality assumptions about the attacker's behavior, feature selection can be formulated as an optimization problem to maximize the KL divergence between the guessing distribution and the true empirical distribution over the same space of a selected feature subset. Speci<sup>fi</sup>cally, the application of the principle of maximum entropy elegantly leads to a closed-form solution to the optimization problem, with a distinctive and intuitive interpretation in the security domain. We then presented three feature selection algorithms characterized by increasing levels of adaptivity. Finally, our empirical results demonstrate that the proposed methods signi<sup>fi</sup>cantly outperform the commonly used random selection method. From a broader decision support perspective, although arti<sup>fi</sup>cial intelligence and optimization techniques have been emphasized as principal enablers of decision making [33], their underlying potential has not been seriously exploited in security decision support problems. To the best of our knowledge, this work is among the <sup>fi</sup>rst attempts to formally model KBA and, in particular the <sup>fi</sup>rst to provide a mathematical framework for the KBA feature selection problem.

Our future work will consider more realistic rationality assumptions and more sophisticated attacking strategies. Empirical evaluations with human subjects are expected to yield better insights into user perception of assurance level and alternate attacking strategies. In fact, serious efforts have been undertaken along this direction. One study with human subjects [9], who take on both authentic user and attacker roles, shows that: (1) the proposed feature selection approach captures the principal components of the security strength of a KBA design, and (2) the underlying rational attacker assumption is a sensible approximation to the human attacker. Another interesting project [7] validates the signi<sup>fi</sup>cance of our probabilistic framework for KBA by using online social networking data. We have shown that if an attacker utilizes the personal knowledge statistically inferred from the publicly available social networking data, the attacking strategy will become more informed which leads to a much higher guessability.

## References

[1] D. Agrawal, C.C. Aggarwal, On the design and quanti<sup>fi</sup>cation of privacy preserving data mining algorithms, Proceedings of the 20th ACM SIGMOD-SIGACT-SIGART Symposium on Principles of Database Systems, ACM, New York, NY, 2001, pp. 247–255.

[2] R. Agrawal, R. Srikant, Privacy-preserving data mining, ACM SIGMOD Record 29 (2) (2000) 439–450.

[3] H. Almauallium, T.G. Dietterich, Learning with many irrelevant features, Proceedings of the 9th National Conference on Arti<sup>fi</sup>cial Intelligence (AAAI 91), vol. 2, 1991, pp. 547–552, Anaheim, CA.

[4] A.L. Blum, P. Langley, Selection of relevant features and examples in machine learning, Arti<sup>fi</sup>cial Intelligence 97 (1–2) (1997) 245–271.

[5] C.J.C. Burges, A tutorial on support vector machines for pattern recognition, Data Mining and Knowledge Discovery 2 (2) (1998) 121–167.

[6] W.E. Burr, D.F. Dodson, W.T. Polk, Electronic authentication guideline: recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63 Version 1.0.2, National Institute of Standards and Technology (NIST), 2006.

[7] Y. Chen, A Bayesian Network Model of Knowledge-Based Authentication, Ph.D. dissertation, University Wisconsin-Madison, Madison, WI, 2007.

[8] Y. Chen, D. Liginlal, Bayesian networks for knowledge-based authentication, IEEE Transactions on Knowledge and Data Engineering 19 (5) (2007) 695–710.

[9] Y. Chen, D. Liginlal, An empirical investigation of knowledge-based authentication, Proceedings of the 13th Americas Conference on Information Systems (AMCIS 2007), Keystone, CO, 2007.

[10] S. Chokhani, Knowledge based authentication (KBA) metrics, KBA Symposium-Knowledge Based Authentication: Is It Quanti<sup>fi</sup>able?, 2004.

[11] N. Friedman, D. Geiger, M. Goldszmidt, Bayesian network classi<sup>fi</sup>ers, Machine Learning 29 (2–3) (1997) 131–163.

[12] W.R. Gilks, Markov Chain Monte Carlo in Practice, Chapman & Hall/CRC, 1995.

[13] I. Guyon, A. Elisseeff, An introduction to variable and feature selection, Journal of Machine Learning Research 3 (2003) 1157–1182.

[14] N.E. Hastings, D.F. Dodson, Quantifying assurance of knowledge based authentication, ECIW 2004: The 3rd European Conference on Information Warfare and Security, 2004.

[15] A. Jain, S. Pankanti, R. Bolle, Biometrics: Personal Identi<sup>fi</sup>cation in Networked Society Kluwer Academic Publishers 1999.

[16] F. Jelinek, R.L. Mercer, L.R. Bahl, J.K. Baker, Perplexity—a measure of dif<sup>fi</sup>culty of speech recognition tasks, Proceedings of the 94th Meeting of the Acoustic Society of America, Miami Beach, FL, 1977.

[17] B. Kaliski, Protecting the knowledge, KBAKBA symposium-knowledge based authentication: is it quanti<sup>fi</sup>able?, 2004.

[18] B.-S. Kang, S.-C. Park, Integrated machine learning approaches for complementing statistical process control procedures, Decision Support Systems 29 (1) (2000) 59–72.

[19] Y. Kim, Toward a successful CRM: variable selection, sampling, and ensemble, Decision Support Systems 41 (2) (2006) 542–553.

[20] K. Kira, L.A. Rendell, A practical approach to feature selection, Proceedings of the 9th International Conference on Machine Learning (ICML 92), Morgan Kaufmann, Aberdeen, Scotland, 1992, pp. 249–256.

[21] B. Klimt, Y. Yang, Introducing the Enron Corpus, Proceedings of the First Conference on Email and Anti-Spam (CEAS 2004), Mountain View, CA, 2004.

[22] R. Kohavi, G.H. John, Wrappers for feature subset selection, Arti<sup>fi</sup>cial Intelligence 97 (1–2) (1997) 273–324.

[23] S. Kullback, R.A. Leibler, On information and suf<sup>fi</sup>ciency, The Annals of Mathematical Statistics 22 (1) (1951) 79–86.

[24] P. Langley, S. Sage, Oblivious decision trees and abstract cases, Working Notes of the AAAI-94 Workshop on Case-Based Reasoning, AAAI Press, 1994.

[25] B. Lawler, Models of knowledge based authentication (KBA), KBA Symposium-Knowledge Based Authentication: Is It Quanti<sup>fi</sup>able?, 2004.

[26] S. Lowry, Challenge & response within e-authentication framework, KBA Symposium-Knowledge Based Authentication: Is It Quanti<sup>fi</sup>able?, 2004.

[27] A.Y. Ng, M.I. Jordan, On discriminative vs. generative classi<sup>fi</sup>ers: a comparison of logistic regression and naive Bayes, Proceedings of the 16th Annual Conference on Neural Information Processing Systems (NIPS 02), vol. 14, 2002

[28] J.R. Quinlan, Induction of decision trees, Machine Learning 1 (1986) 81–106.

[29] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Francisco, CA, 1993.

[30] T. Regan, Information source metrics, KBA Symposium-Knowledge Based Authentication: Is It Ouantifiable? 2004

[31] R. Rosenfeld, A maximum entropy approach to adaptive statistical language modeling, Computer Speech and Language 10 (1996) 187–228.

[32] C. Shannon, A mathematical theory of communication, Bell System Technical Journal 27 (1948) 379–423.

[33] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002) 111–126

[34] L. Sweeney, K-anonymity: a model for protecting privacy, International Journal on Uncertainty, Fuzziness and Knowledge-Based Systems 10 (5) (2002) 557–570.

[35] K. Trilli, B. Andrews, KBA challenge response system, KBA Symposium-Knowledge Based Authentication: Is It Quanti<sup>fi</sup>able?, 2004.

[36] V.S. Verykios, E. Bertino, I.N. Fovino, L.P. Provenza, Y. Saygin, Y. Theodoridis, Stateof-the-art in privacy preserving data mining, ACM SIGMOD Record 33 (1) (2004) 50-57.

[37] J. von Neumann, O. Morgenstern, Theory of Games and Economic Behavior, Princeton University Press, Princeton, NJ, 1944.

![](/api/attachments/S4P2U832/fulltext/images/7dfd7a62ea478b17df9ecceba8fe134faf8ef84989e91a77538c74b0d3bbabe1.jpg)

Ye Chen is a Sr. Scientist in the Data Mining and Research group at Yahoo! Inc. He received his Ph.D. degree in Information Systems from the Operations and Information Management department, University of Wisconsin-Madison. Dr. Chen's research interests lie in statistical machine learning, particularly Bayesian methods, to solve problems in data mining, exploratory data analysis, security in e-commerce and online social networking. His research. His teaching and research have received funding from organizations such as Microsoft Corporation, Hewlett Packard, CISCO, and the International Center for Automated Information Research at the University of Florida.

research work has been published in journals such as IEEE Transactions on Knowledge and Data Engineering and Journal of Database Management.

![](/api/attachments/S4P2U832/fulltext/images/1a4d4793a80946971e5ba375d559b168ceeadf53b3875dff9a1288c03fd5f94d.jpg)

Divakaran Liginlal is an Assistant Professor in the School of Business, University of Wisconsin, Madison. He received a B.S. in Telecommunication Engineering from the University of Kerala, M. S. in Computer Science from the Indian Institute of Science at Bangalore, India, and a Ph.D. in Management Information Systems from the University of Arizona. Prof. Liginlal's research interests are in computational and cognitive models of decision making and problem solving

and information security technologies and strategies. His research work has been published in journals such as Fuzzy Sets and Systems, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man, and Cybernetics, and the European Journal of Operational
