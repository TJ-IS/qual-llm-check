---
otero_id: 17332
otero_key: "WCBNSWDY"
title: "The accuracy of concepts learned from induction"
authors: "Li-Hui Tsai; Gary J Koehler"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90036-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The accuracy of concepts learned from induction

Li-Hui Tsai and Gary J. Koehler
University of Florida, Gainesville FL, USA

Inductive learning methods identify a concept from a training sample consisting of positive and negative examples of a target concept. Several studies have shown how such methods could be used to determine rules for expert systems. The question addressed in this paper is: how accurate is the induced concept when used to classify the original domain or another close domain? We derive results that can be used to determine the accuracy of an induced concept. Two previously published applications of inductive learning are used to illustrate our results.

Keywords: Inductive learning; Expert systems; PAC-learning; Predictive accuracy.

![](/api/attachments/WCBNSWDY/fulltext/images/e07c8260514faf48d95392061b3df89d26be72cf06637acb30c581b5bda8fe18.jpg)

Li-Hui Tsai is an Assistant Professor in the Department of Decision and Information Sciences at the University of Florida. She received her Ph.D. at the University of California at Berkeley in 1987. She has published in SIAM Journal of Computing, Operations Research Letters, and Information Processing Letters.

![](/api/attachments/WCBNSWDY/fulltext/images/e683447508ad88e21bdd688675b012d3dbee90f730c1ddda44660f0c08d2e089.jpg)

Gary J. Koehler is Professor and Chairman of the Department of Decision and Information Sciences at the University of Florida. He received his Ph.D. at Purdue University in 1973. In 1979 he co-founded Micro Data Base Systems, Inc. and was its President and CEO until 1987. he has published in a number of journals including Management Science, Decision Sciences, Operations Research, the SIAM Journal of Control and Optimization, Discrete Applied Mathematics, Naval Research Logistics, European Journal of Operations Research, the Journal of Finance, and Managerial and Decision Economics.

Correspondence to: L.-H. Tsai, Department of Decision and Information Sciences, University of Florida, Gainesville, FL 32611, USA. Tel: (904) 392 5946. E-mail: tsai@nervm.

## 1. Introduction

A number of recent papers have presented applications of inductive algorithms for business problems $[5,13,22]$ . These methods were developed in machine learning areas to infer classification rules from examples $[14,17,20]$ . Classification rules may be used directly for predictive or descriptive purposes or may be used to build knowledge bases.

While these papers have been primarily expository and report excellent empirical results for inductive methods compared to more traditional categorical approaches, such as discriminant analysis [6], they leave the reader with the impression that inductive methods are superior to such traditional approaches.

In this paper we show that care must be taken in applying inductive methods. Unlike deductive inference methods that preserve truth, inductive methods are only logically guaranteed to preserve falsehood. To reduce the chance of a large error, very large samples may be required to infer a classification rule. In contrast, recent studies have used very small sample sizes to induce concepts.

Recent work in machine learning has focused on establishing a theoretical foundation for learnability $[4,7,9,23]$ . These include bounds on sample sizes to guarantee the discovery of a concept that is probably close to the true concept one is trying to learn. We extend these results by showing how to measure the accuracy of a concept already learned. These measures are then applied to several recent studies that are based on very small sample sizes. Our results cast doubts on the accuracy of the induced concepts found in these studies.

In section 2 we review notation and background material in machine learning. Our main results are given in section 3 where we give procedures to assess the accuracy of a learned concept. In section 4 we present a well-known inductive algorithm, ID3, and establish some properties that will be used in applying our results in section 5.

## 2. Induction

Inductive learning is used to infer rules of classification by analyzing examples from a domain. When the domain consists of two distinct groups of instances (called the negative and positive instances), the task is called binary classification. Several techniques have been developed to systematically induce rules of identification from a set of positive and negative examples $[14,17,20]$ . These techniques have been applied to solve different problems in several business areas $[5,13,22]$ .

Let the set X represent a domain of interest. The target concept, $h^{*}$ , is the subset of X that consists of all positive instances in X. To identify the target concept, a set of training examples are drawn randomly with replacement from X according to a fixed but arbitrary probability distribution $P_{x}$ . Let f be the inductive function derived from the training sample using some inductive algorithm. The function f classifies an instance as positive or negative, i.e.,

$$
f \colon X \to \{+, - \}.
$$

A learned concept, h, is a subset of X that consists of instances that will be classified as positive according to the inductive rule, i.e.,

$$
h = \{x \mid f (x) = +, x \in X \} = f ^ {- 1} (+).
$$

The error, $\epsilon$ of a learned concept is the probability of the symmetric difference between the learned concept and the target concept. We denote the error of a concept h as

$$
P _ {x} \left\{h \Delta h ^ {*} \right\} = P _ {x} \left\{\left(h - h ^ {*}\right) \cup \left(h ^ {*} - h\right) \right\}.
$$

The confidence parameter, $\delta$ , is an upper bound on the likelihood of an error. Using the terminology introduced in [3], an inductive function f is a $(\epsilon, \delta)$ -probably approximately correct identification (PAC-identification) of $h^{*}$ in domain X if

$$
\operatorname{Prob} \left\{P _ {\mathrm{x}} \left\{f ^ {- 1} (+) \Delta h ^ {*} \right\} \geqslant \epsilon \right\} \leqslant \delta ,
$$

which is equivalent to

$$
\operatorname{Prob} \left\{P _ {\mathrm{x}} \left\{f ^ {- 1} (+) \Delta h ^ {*} \right\} \leqslant \epsilon \right\} \geqslant 1 - \delta .
$$

Prob{ } means probability. Less formally, the rerequirement for a PAC-identification is that the probability of the difference between an induced classification and the true classification be small ( $\epsilon$ ) with high probability (1 - $\delta$ ). Accordingly, we name a concept h as a ( $\epsilon$ , $\delta$ )-probably approximately correct concept if

$\operatorname{Prob}\left\{P_{x}\{h\Delta h^{*}\} \geqslant \epsilon\right\} \leqslant \delta.$

Assuring that the induced concept is probably approximately correct requires that a sufficiently large sample size be taken. Blumer, et al. [4], Ehrenfeucht, et al. [7], and Haussler [9] developed several criteria to assure that a PAC-identification will be induced. These results which are summarized below are preceded by several principles and four definitions.

The class of all possible concepts based only on the attributes of the instances of X is $C = 2^{X}$ , where C contains the target concept $h^{*}$ . A hypothesis space, $H \subseteq C$ , consists of those concepts consistent with a concept description language used by the learning algorithm. The concept $h^{*}$ might not be in H. A finite sample of instances, Q, is used by the learning algorithm. A version space of Q with respect to H is the set of all concepts in H consistent with the examples in Q. A concept is consistent with Q if its positive and negative examples in Q are the positive and negative examples under $h^{*}$ , respectively.

Definition 1. The growth function of $H$ , $\pi_{\mathrm{H}}(m)$ , is the maximum number of ways the concepts in $H$ can label a set of $m$ instances.

Definition 2. The Vapnik–Chervonenkis dimension of H, VCdim(H), is the largest m such that $\pi_{\mathrm{H}}(m)=2^{m}$ .

Definition 3. The version space of Q (w.r.t. H) is $\epsilon$ -exhausted (w.r.t. $h^{*}$ ) if it does not contain any hypothesis h with $P_{x}(h\Delta h^{*}) > \epsilon$ .

Definition 4. Any algorithm that will $\epsilon$ -exhaust H with probability at least $1-\delta$ is denoted an $(\epsilon,\delta)$ -learning algorithm.

Upper and lower bounds for $\epsilon$ -exhaustion are summarized below. Bound (1) provides a sufficient upper bound on the sample size needed to guarantee an $(\epsilon, \delta)$ -PAC-identification. Bound (2) provides a necessary lower bound.

Theorem 1. Bounds [4, 9] (1) For any given $\epsilon$ and $\delta$ , with $0 \leqslant \epsilon$ , $\delta \leqslant 1$ , if the size of $Q$ is at least $\min \left\{(1 / \epsilon)\left[\ln(2 / \delta) + \ln|H|\right]\right\}$ .

$$
\begin{array}{l} (1 / \epsilon) \left[ 4 \log_ {2} (2 / \delta) \right. \\ \left. + 8 \mathrm{VCdim} (H) \log_ {2} (1 3 / \epsilon) \right] \}, \end{array}
$$

then the version space $Q$ (w.r.t. $H$ ) is $\epsilon$ -exhausted with probability at least $1 - \delta$ .

(2) For

$$
0 <   \epsilon <   1 / 2,
$$

and

$\operatorname{VCdim}(H) < \infty,$

then any $(\epsilon, \delta)$ -learning algorithm for $H$ must use a sample size of

$$
\max \left\{\left[ (1 - \epsilon) / \epsilon \right] \ln (1 / \delta), \right.
$$

$$
\operatorname{VCdim} (H) \left[ 1 - 2 (\epsilon (1 - \delta) + \delta) \right] \}.
$$

A tighter lower bound requiring slightly more restrictive conditions is given below.

## Theorem 2. Lower Bound [7] For

$$
0 <   \epsilon \leqslant 1 / 8,
$$

$$
0 <   \delta \leqslant 1 / 1 0 0,
$$

and

$$
2 \leqslant \mathrm{VCdim} (H) <   \infty ,
$$

then any $(\epsilon, \delta)$ -learning algorithm for $H$ must use a sample size of

$$
\max \left\{\left[ (1 - \epsilon) / \epsilon \right] \ln (1 / \delta), \right.
$$

$$
\left(\operatorname{VCdim} (H) - 1\right) / [ 3 2 \epsilon ] \}.
$$

These last two theorems are surprising in that they show that concepts can be learned by taking sample sizes that are logarithmic in the size of the hypothesis space, that are independent of the true concept, and that are independent of the sampling distribution. Although the sample size may be logarithmic in the size of the hypothesis space, it may still be a large number.

## 2.1. An illustration with $|H| < \infty$

Suppose we wish to characterize successful firms using the following list of attributes:

<table><tr><td>Attribute</td><td>Values</td></tr><tr><td>Type</td><td>ServiceManufacturingDistribution</td></tr><tr><td>Span</td><td>InternationalNationalRegional</td></tr><tr><td>Options</td><td>YesNo</td></tr><tr><td>Debt</td><td>YesNo</td></tr><tr><td>Positive retained Earnings</td><td>YesNo</td></tr><tr><td>Non-voting stock</td><td>YesNo</td></tr><tr><td>High-tech stock</td><td>YesNo</td></tr></table>

It is easy to see that $|X|=2^{5}3^{2}=288$ and that there are $2^{288}$ possible concepts. Suppose we are only interested in pure conjunctive concepts. A pure conjunctive concept consist of logically “ANDed” atoms of the form “attribute=value”. Since each attribute can either be a term of a conjunctive concept or not, the number of conjunctive concepts is $|H|=3^{5}4^{2}=3888$ . From Theorem 3.6 [9], the VCdim(H) for pure conjunctive hypotheses satisfies

$$
n \leqslant \mathrm{VCdim} (H) \leqslant 2 n,
$$

where $n$ is the number of attributes. Thus

$$
7 \leqslant \mathrm{VCdim} (H) \leqslant 1 4.
$$

For $\epsilon = 0.1$ and $\delta = 0.05$ , Theorem 1, part 1 shows that for a sample of size

$$
m = \min \{1 1 3, 8 0 7 8 \} = 1 1 3,
$$

then we are guaranteed to $\epsilon$ -exhaust H with probability of 0.95. Here we used $\mathrm{VCdim}(H)=14$ to be conservative. Theorem 1, part 2 shows that no learning function can guarantee (0.10, 0.05)-PAC identification with fewer than

$$
m = \max \{2 7, 1 0 \} = 2 7,
$$

samples.

## 2.2. An illustration with $|H| = \infty$

Suppose we wish to learn the range of debt-to-equity ratios within which successful growth companies operate. Let X be the interval $[0, 1]$ , which represents all possible values of debt-equity ratios.

The true concept $h^{*}$ is either the interval represented by $[L, U]$ for some values of $L \leqslant U$ or it is the empty set. The hypothesis space H consists of all intervals $[a, b]$ with $0 \leqslant a \leqslant b \leqslant 1$ plus the empty set. The empty set is added to allow for the possibility that the target concept may not be expressed by an interval. Since there are an infinite number of intervals in $[0, 1]$ , $|H| = \infty$ .

A training sample would be constructed using the debt-equity ratios of randomly selected firms and an assignment of each firm as either a positive example (a successful growth firm) or a negative example.

One possible learning algorithm is as follows:

(1) Let $P$ be the set of positive instances in the sample and

(2) If $l \leqslant x \leqslant \mu$ for any negative example, $x$ , then return $\emptyset$ , otherwise return $[l, \mu]$ .

The growth function for H is determined as follows. Consider the maximum number of ways some single-instance sample can be labelled by concepts in H. The instance $0 \in X$ can be labelled as + by the concept [0, 1] and - by the concept [0.5, 1]. The - label means that 0 is not in [0.5, 1]. Hence,

$$
\pi_ {\mathrm{H}} (1) = 2.
$$

Given any two instances $(x, y)$ in X with x < y, the possible classifications by concepts in H are $(+, -)$ , $(-, +)$ , $(+, +)$ , and $(-, -)$ . For example, for the two instances (0.3, 0.7), the following four concepts give the indicated labelling:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
[0.1, 0.4] gives $(+, -)$;  
[0.5, 0.9] gives $(-, +)$;  
[0.2, 0.8] gives $(+, +)$; and  
[0.8, 1.0] gives $(-, -)$.  
Thus  
$\pi_{\mathrm{H}}(2) = 4$.
</div>

Given any three instances, $(x, y, z)$ , x < y < z, no concept in H can classify $(x, y, z)$ as $(+, -, +)$ but all other classification combinations are possible. Hence,

$$
\pi_ {\mathrm{H}} (3) = 7.
$$

Let $\epsilon = 0.1$ and $\delta = 0.01$ . By part (1) of theorem 1, if a sample $Q$ has size at least

$$
\begin{array}{c} \min \left\{\infty , (1 / 0. 1) \left[ 4 \log_ {2} (2 / 0. 0 1) \right. \right. \\ \left. + 1 6 \log_ {2} (1 3 / 0. 1) \right\} = 1 4 2 9. 3, \end{array}
$$

then the probability is no greater than 0.01, of an error greater than 10%, for any learning algorithm that produces a concept consistent with Q.

Similarly, from theorem 2, if the size of $Q$ is less than

$$
\begin{array}{r l} & \max \left\{\left((1 - 0. 1) / 0. 1\right) \ln (1 / 0. 0 1), (2 - 1) / 3. 2 \right\} \\ & = \max \{4 1. 4, 0. 3 \} = 4 1. 4, \end{array}
$$

no learning function that induces a concept from Q can guarantee a $(0.1, 0.01)$ -PAC-identification.

## 2.3. Focus of research

Theorem 1 provides bounds on the training sample size to guarantee a PAC-identification of a concept. It is often the case that one cannot obtain a large enough sample. In such cases it is of value to obtain a posterior evaluation of the concept accuracy.

For this purpose, a set of examples, called the test set, is employed. Often a test set is a holdout sample randomly removed from original cases available for training.

In the next section we provide posterior measurements for the error and confidence parameters implicit in an inductive function. This measurement is especially useful when:

(1) $|H|$ and VCdim(H) can not be evaluated or are infinite. In such cases it is difficult to determine a training sample size for PAC-identification; or

(2) $|H|$ and VCdim(H) are large. When this happens the upper bound given by theorem 1 is very loose. In this case, it is likely that an inductive function, $f$ , derived from a training sample of size equal to the bound provided by (1) in theorem 1 is actually more accurate than a $(\epsilon, \delta)$ -PAC-identification, i.e., the probability that $P_{\mathrm{x}}\{f^{-1}(+) \Delta h^{*}\} \geqslant \epsilon$ is much smaller than $\delta$ . A posterior measurement is likely to provide a more precise evaluation.

In addition to the above two situations, there is an additional need for establishing estimates of the error and confidence parameters. Consider the case where a concept has been learned from examples in one domain but will be applied in another (related) domain. A common example is applying rules learned in the past to current of future situations where the environment may be ‘close’ but different.

For example, credit approval rules derived from past data may have been good predictors in the past but may not be valid today or tomorrow because of changing economic conditions. Estimating their reliability is an important consideration.

In the next section we establish a procedure for estimating the error and confidence parameters. These results are applied in later sections.

## 3. Error and confidence parameter estimation

Let N be a domain of interest. N may be equivalent to X or closely related. A sample $Q_{N}$ drawn from N according to a fixed but arbitrary probability distribution $P_{N}$ is called the test sample. N and $P_{N}$ can be the same or different from X and $P_{x}$ . Let f be the inductive function learned from the training sample from X. We assume that N is close enough in structure to X so that f can be meaningfully applied to N. Let $f_{N}$ be the function defined in N by f. That is

$$
f _ {N}: N \rightarrow \{+, - \}.
$$

Let $h_{N}^{*}$ be the target concept in N, i.e., $h_{N}^{*}$ is the subset of N that consists of all positive instance of the target concept. Let $h'$ be the concept in $2^{N}$ represented by $f_{N}$ . $h'$ is the subset of N that consists of instances identified as positive by $f_{N}$ , i.e.,

$$
h ^ {\prime} = \left\{t \mid f _ {N} (t) = +, t \in N \right\} = f _ {N} ^ {- 1} (+).
$$

The error of $f_{N}$ , $\theta$ , is the probability of the symmetric difference between $h'$ and $h_{N}^{*}$

$$
\theta = P _ {N} \left\{h ^ {\prime} \Delta h _ {N} ^ {*} \right\} = P _ {N} \left\{\left(h ^ {\prime} - h _ {N} ^ {*}\right) \cup \left(h _ {N} ^ {*} - h ^ {\prime}\right) \right\}.
$$

Let m be the number of samples in $Q_{N}$ and b be the number of misclassifications in $Q_{N}$ according to $f_{N}$ . b is the sum of the number of positive samples that are classified as negative and the number of negative samples that are classified as positive, according to $f_{N}$ .

The following result gives a posterior estimate of the concept error of $f_{N}$ determined using the test sample $Q_{N}$ assuming a uniform prior. This result can be found in [21,24].

Theorem 3. Posterior estimate of the confidence parameter Given b failures in a sample size of m, the posterior estimate of the binomial parameter, $\theta$ , using a uniform prior is

$\operatorname{Prob}\{\theta \geqslant \epsilon \mid b, m\}$

$$
= \sum_ {k = 0} ^ {b} C _ {k} ^ {m + 1} \epsilon^ {k} (1 - \epsilon) ^ {m + 1 - k} \quad \text { for } \epsilon \leqslant 0. 5,
$$

and

$$
\begin{array}{l} \text { Prob } \{\theta \geqslant \epsilon \mid b, m \} \\ = \sum_ {k = m + 1 - b} ^ {m + 1} C _ {k} ^ {m + 1} (1 - \epsilon) ^ {k} \epsilon^ {m + 1 - k} \text {   for   } \epsilon \geqslant 0. 5. \end{array}
$$

Here $C_{k}^{m}$ is the number of combinations of m things taken k at a time. The terms in Theorem 3 are easily computed using the Incomplete Beta distribution and methods given in [2] or approximated using methods given in [18]. The use of theorem 3 is questionable, however, since a uniform prior is almost always inappropriate.

In the next subsections we develop probabilistic estimates of the error that are based on the assumption of a Beta prior distribution.

## 3.1. Error estimation when $|H| < \infty$

In this section we present a method to test a concept that has been discovered during a training episode. We explicitly assume that the domain, X, is unchanged (ie., X = N), and that the use of information available during training is known and relevant during testing. In Section 3.3, we drop this assumption.

From theorem 1, part 1, after the initial training with a sample of size $m_{1}$ , we know that

$$
\operatorname{Prob} \{\theta \geqslant \epsilon \} \leqslant | H | (1 - \epsilon) ^ {m _ {1}}.
$$

Let $Z^{+}$ be the set of positive integers and let $F(H, m_{1})$ be the set $\{(a, b): a, b \in \mathbb{Z}^{+}\}$ where, for all $0 < \epsilon < 1$ , $I_{\epsilon}(a, b)$ is an Incomplete Beta distribution that is consistent with the above bound. $I_{\epsilon}(a, b)$ gives the probability of a value less than or equal to $\epsilon$ . Denote by $F(H, m_{1})$ the set of integer parameters for Incomplete Beta distributions that are consistent with the information of Theorem 1, part 1. In the following we develop a characterization of $F(H, m_1)$ .

First, Lemma 1 provides a necessary condition.

Lemma 1. Consistent beta priors For $|H| < \infty$ and $p, q \in \mathbb{Z}^+$ , then

$$
(p, q) \in F (H, m _ {1}),
$$

only if $q \geqslant m_1$ .

Proof. After training with $m_{1}$ examples, the probability of an error of $\epsilon$ is bounded from above by

$$
\mid H \mid (1 - \epsilon) ^ {m _ {1}}.
$$

Then any consistent Beta prior must satisfy

$$
1 - \mathrm{I} _ {\epsilon} (p, q) \leqslant | H | (1 - \epsilon) ^ {m _ {1}},
$$

for all $0 < \epsilon < 1$ where $I_{\epsilon}(p, q)$ is the Incomplete Beta which gives the probability of a value less than or equal to $\epsilon$ . This can be rewritten with a Binomial distribution as

$$
\sum_ {k = 0} ^ {p - 1} C _ {k} ^ {q + p - 1} \epsilon^ {k} (1 - \epsilon) ^ {p + q - 1 - k} \leqslant | H | (1 - \epsilon) ^ {m _ {1}}.
$$

Divide each side by

$$
(1 - \epsilon) ^ {m _ {1}}.
$$

The last term of the sum (where $k = p - 1$ ) contains

$$
\left(1 - \epsilon\right) ^ {q - m _ {1}}.
$$

By choosing $\epsilon$ close enough to 1, this term can be made larger than $|H|$ when $q < m_1$ .

A uniform Beta prior is consistent only if $m_{1}=1$ . So theorem 3 is seldom appropriate.

Next, Lemma 2 provides several combinatorial identities that can be found in [8]. These are used in Lemma 3.

Lemma 2. Combinatorial identities [8] The following hold:

(1) $C_n^{-x} = (-1)^n C_n^{x + n - 1};$

(2) $\sum_{k=0}^{n} C_k^{x+k} = C_n^{x+n+1}$ ;

(3) $\sum_{k=0}^{n} C_k^x C_{n-k}^y = C_n^{x+y}$ (Vandermonde convolution).

Lemma 3 provides a partial characterization of $F(H, m_1)$ .

Lemma 3. Partial Characterization For $|H| < \infty$ and any $p \in \mathbb{Z}^+$ and $q = m_1$ , then

$$
(p, q) \in F (H, m _ {1})
$$

if and only if

$$
C _ {p - 1} ^ {q + p - 1} \leqslant | H |.
$$

Proof. Assume $q = m_1$ and $p \in \mathbb{Z}^+$ . Using a binomial expansion we get

$$
\begin{array}{l} f (\epsilon) = \sum_ {k = 0} ^ {p - 1} C _ {k} ^ {q + p - 1} \epsilon^ {k} (1 - \epsilon) ^ {p - 1 - k} \\ = \sum_ {k = 0} ^ {p - 1} C _ {k} ^ {q + p - 1} \sum_ {h = 0} ^ {p - 1 - k} (- 1) ^ {h} C _ {h} ^ {p - 1 - k} \epsilon^ {h + k}. \end{array}
$$

This can be rewritten as

$$
f (\epsilon) = \sum_ {k = 0} ^ {p - 1} c _ {k} \epsilon^ {k},
$$

where

$$
c _ {k} \equiv \sum_ {h = 0} ^ {k} (- 1) ^ {h} C _ {k - h} ^ {q + p - 1} C _ {h} ^ {p - 1 - k + h}.
$$

From Lemma 2, part 1 we get that

$$
(- 1) ^ {h} C _ {h} ^ {p - 1 - k + h} = C _ {h} ^ {k - p}.
$$

Thus

$$
c _ {k} \equiv \sum_ {h = 0} ^ {k} C _ {h} ^ {k - p} C _ {k - h} ^ {q + p - 1}.
$$

From lemma 2, part 3 we get

$$
c _ {k} \equiv \sum_ {h = 0} ^ {k} C _ {h} ^ {k - p} C _ {k - h} ^ {p - 1 - k + h} = C _ {k} ^ {k + q - 1}.
$$

Hence

$$
f (\epsilon) = \sum_ {k = 0} ^ {p - 1} C _ {k} ^ {k + q - 1} \epsilon^ {k}.
$$

(Necessity) Since it is necessary that

$$
f (\epsilon) \leqslant | H |,
$$

then

$$
\sum_ {k = 0} ^ {p - 1} C _ {k} ^ {k + q - 1} \epsilon^ {k} \leqslant | H |,
$$

must hold for $\epsilon = 1$ . Substituting for $\epsilon$ gives

$$
\sum_ {k = 0} ^ {p - 1} C _ {k} ^ {k + q - 1} \leqslant | H |.
$$

From Lemma 2, part 2 we get

$$
\sum_ {k = 0} ^ {p - 1} C _ {k} ^ {k + q - 1} = C _ {p - 1} ^ {p + q - 1} \leqslant | H |.
$$

(Sufficiency) $(p, q) \in (F(H, m_1)$ if

$$
f (\epsilon) \leqslant | H |,
$$

for $0 \leqslant \epsilon \leqslant 1$ . Clearly, $f(0) = 0 \leqslant |H|$ . Consider the first derivative of $f(\epsilon)$ .

$$
f ^ {\prime} (\epsilon) = \sum_ {k = 0} ^ {p - 1} C _ {k} ^ {k + q - 1} k \epsilon^ {k - 1} \geqslant 0,
$$

for $0 \leqslant \epsilon \leqslant 1$ . Thus, $f(\epsilon)$ is increasing in $\epsilon$ . But, as shown above,

$$
f (1) = C _ {p - 1} ^ {p + q - 1}.
$$

Hence, $\mathrm{f}(\epsilon) \leqslant |H|$ if

$$
C _ {p - 1} ^ {p + q - 1} \leqslant | H |.
$$

With lemma 3 and 4 we will have our main result.

Lemma 4. Assume $|H| < \infty$ and $p, q \in \mathbb{Z}^+$ . If $(p, q) \in F(H, m_1)$

then

$$
(t, q) \in F (H, m _ {1}), \quad 1 \leqslant t \leqslant p,
$$

$$
(p, t) \in F (H, m _ {1}), t \geqslant q.
$$

Proof. From Abromowitz and Segun [2], formula 26.5.16 gives

$$
\mathrm{I} _ {\epsilon} (p - 1, q) \geqslant \mathrm{I} _ {\epsilon} (p, q),
$$

for all $0 \leqslant \epsilon \leqslant 1$ . Thus, since

$$
1 - \mathrm{I} _ {\epsilon} (p, q) \leqslant | H | (1 - \epsilon) ^ {m _ {1}},
$$

we get

$$
1 - \mathrm{I} _ {\epsilon} (p - 1, q) \leqslant | H | (1 - \epsilon) ^ {m _ {1}}.
$$

Likewise, formulas 26.5.10 and 26.5.16

$$
\mathrm{I} _ {\epsilon} (p, q + 1) \geqslant \mathrm{I} _ {\epsilon} (p, q),
$$

so

$$
1 - \mathrm{I} _ {\epsilon} (p, q + 1) \leqslant | H | (1 - \epsilon) ^ {m _ {1}}.
$$

We now give the main result of this subsection.

Theorem 4. For $|H| < \infty$ and $p, q \in \mathbb{Z}^{+}$ , then $(p, q) \in F(H, m_{1})$ ,

only if $q \geqslant m_1$ and $1 \leqslant p \leqslant p^*$ where $p^*$ is the largest $p$ satisfying

$$
C _ {p - 1} ^ {m _ {1} + p - 1} \leqslant | H |.
$$

After a test sample of size $m_{2}$ is evaluated, giving b misclassifications, the posterior distribution will have parameters $(p + b, q + m_{2} - b)$ . Assuming $p, q \in Z^{+}$ , the worst possible confidence factor is

$$
\begin{array}{l l} \delta \equiv \sup & \left[ 1 - \mathrm{I} _ {\epsilon} (p + b, q + m _ {2} - b) \right], \\ \text {st.} & (p, q) \in F (H, m _ {1}). \end{array}
$$

This can be rewritten and bounded using theorem 4 as

$$
\begin{array}{l l} \delta \equiv \sup & \left[ 1 - \mathrm{I} _ {\epsilon} (p + b, q + m _ {2} - b) \right], \\ \text {st.} & 1 \leqslant p \leqslant p ^ {*}, \\ & q \geqslant m _ {1}, \\ & p, q \in \mathbb {Z} ^ {+}. \end{array}
$$

In the proof of lemma 4, the term

$$
\mathrm{I} _ {\epsilon} (p + b, q + m _ {2} - b),
$$

is decreasing with increases in its first argument and decreases in its second argument. Hence, the supremum is attained and is

$$
\delta = 1 - \mathrm{I} _ {\epsilon} (p ^ {*} + b, m _ {1} + m _ {2} - b).
$$

Theorem 5. Suppose $|H| < \infty$ and $p^*$ is the largest positive integer, $p$ , satisfying

$$
C _ {p - 1} ^ {m _ {1} + p - 1} \leqslant | H |.
$$

After training with $m_{1}$ samples and testing with $m_{2}$ samples obtaining b misclassifications, then

$$
\operatorname{Prob} \left\{\theta \geqslant \epsilon \right\} \leqslant \delta \leqslant 1 - I _ {\epsilon} (p ^ {*} + b, m _ {1} + m _ {2} - b).
$$

Theorem 5 gives a bound on the probability of an error of size $\epsilon$ that is independent of the Beta prior.

When $|H|$ is large, the Incomplete Beta can be approximated using a normal distribution as shown in [18].

## 3.2. An illustration

Suppose in the example of section 2.1 that the sample size was $m_{1}=113$ . Further suppose that we now take a sample of size $m_{2}=10$ and get two $(b=2)$ misclassifications using the learned concept.

To apply Theorem 5, we must first find $p^*$ using

$$
C _ {p - 1} ^ {p + q - 1} \leqslant | H |,
$$

with $q = m_{1}$ . For $p = 2$ , we get 114 for the Binomial coefficient. For $p = 3$ we get 6555. Since $|H| = 3888$ , $p^{*} = 2$ . Hence

$$
\begin{array}{r l} \operatorname{Prob} \{\theta \geqslant 0. 1 \} & \leqslant \delta \leqslant 1 - \mathrm{I} _ {\epsilon} (p ^ {*} + b, m _ {1} + m _ {2} - b) \\ & = 1 - \mathrm{I} _ {\epsilon} (4, 1 2 1). \end{array}
$$

Evaluating the last term gives

$$
\operatorname{Prob} \{\theta \geqslant 0. 1 \} \leqslant \delta \leqslant 1 - 0. 9 9 8 8 7 = 0. 0 0 1 1 3.
$$

So the probability that the error of the learned concept is greater than 0.1 is less than 0.00113. The apparent increase in confidence is deceiving. This bound results from the worst posterior Beta. Using the Beta prior that corresponds to this posterior before seeing the test results would have given

$$
\begin{array}{r l} \operatorname{Prob} \{\theta \geqslant 0. 1 \} & \leqslant \delta = 1 - I _ {\epsilon} (p ^ {*}, m _ {1}) \\ & = 1 - I _ {\epsilon} (2, 1 1 3) = 0. 0 0 0 0 8 3. \end{array}
$$

3.3. A general error bound independent of $|H|$ and X.

In this section we develop a bound on $\operatorname{Prob}\{\theta \geqslant \epsilon\}$

that requires no assumptions on the prior distribution or on H. This bound also ignores any information that may have been obtained during training. This is appropriate especially when the training domain is different from the testing domain. For ease of presentation, let $m = m_{2}$ .

Theorem 6. Bound on the posterior estimate of the confidence parameter For any $b / m \leqslant \epsilon$ then

$$
\operatorname{Prob} \{\theta \geqslant \epsilon \} \leqslant e ^ {- 2 (\epsilon - b / m) ^ {2} m}.
$$

To prove theorem 6 we will need the following.

Lemma 5. Hoeffding inequalities [10] Let $x_{1}, x_{2}, \ldots, x_{n}$ be independent random variables with $0 \leqslant x_{i} \leqslant 1$ and $\operatorname{E}[x_{i}] = \mu$ , for $i = 1, 2, \ldots, n$ . Let $\bar{x} = (\sum_{i=1}^{n} x_{i}) / n$

$$
\begin{array}{r l} & {\mathrm{Prob} \{\bar {x} - \mu \geqslant t \}} \\ & {\quad \leqslant A _ {1} (t, \mu) \leqslant A _ {2} (t, \mu) \leqslant A _ {3} (t, \mu), \quad t <   1 - \mu ,} \\ & {\mathrm{Prob} \{\mu - \bar {x} \geqslant t \}} \\ & {\quad \leqslant A _ {1} (t, \mu) \leqslant A _ {2} (t, \mu) \leqslant A _ {3} (t, \mu), \quad t > 0,} \end{array}
$$

where

$$
A _ {1} (t, \mu) = e ^ {- n t ^ {2} G (t, \mu)},
$$

$$
A _ {2} (t, \mu) = e ^ {- n t ^ {2} g (\mu)},
$$

$$
A _ {3} (t, \mu) = e ^ {- 2 n t ^ {2}},
$$

and

$$
\begin{array}{r l} t ^ {2} G (t, \mu) & = (\mu + t) \ln [ 1 + t / \mu ] \\ & + (1 - \mu - t) \ln [ (1 - t) / \mu ] \end{array}
$$

$$
\text { for } \mu + t <   1,
$$

$$
g (\mu) = [ 1 / (1 - 2 \mu) ] \ln [ (1 - \mu) / \mu ]
$$

$$
g (\mu) = 1 / \left[ 2 \mu (1 - \mu) \right] \quad \text {for} 1 / 2 \leqslant \mu <   1.
$$

Proof of Theorem 6. $\theta$ is the probability of a misclassification under $f_{\mathrm{N}}$ . Let $x_{i} = 1$ if $f_{\mathrm{N}}$ misclassifies the $i$ th example and $x_{i} = 0$ otherwise. Clearly $\operatorname{E}(x_i) = \theta$ . Since we have $b$ out of $m$ misclassifications in $h' \Delta h_t^*$ , $x = b / m$ , lemma 5 gives

$$
\begin{array}{r l} \operatorname{Prob} \{\theta \geqslant \epsilon \} & = \operatorname{Prob} \{\theta - b / m \geqslant \epsilon - b / m \} \\ & \leqslant A _ {1} (\epsilon - b / m, \theta) \leqslant A _ {2} (\epsilon - b / m, \theta) \\ & \leqslant A _ {2} (\epsilon - b / m, \theta) = e ^ {- 2 m (\epsilon - b / m) ^ {2}}. \end{array}
$$

The last term always holds. $\square$

The proof of Theorem 6 actually gives three potential bounds each weaker but simpler than the preceding. The stronger bounds may be used when the appropriate conditions apply. The third bound applies for any $\theta$ ; Lemma 5 holds for sampling without replacement.

The following corollary covers the case where $0 < \epsilon' < b/m$ .

Corollary 1. Bound on the posterior estimate of the confidence parameter For any $0 < \epsilon' < b/m$ , the probability that $\theta \leqslant \epsilon'$ is less than

$$
e ^ {- 2 (b / m - \epsilon^ {\prime}) ^ {2} m}.
$$

Proof. The proof is similar to that of theorem 6. Since

$$
\operatorname{Prob} \left\{\theta \leqslant \epsilon^ {\prime} \right\} = \operatorname{Prob} \left\{b / m - \theta \geqslant b / m - \epsilon^ {\prime} \right\},
$$

from lemma 5

$$
\begin{array}{r l} \operatorname{Prob} \bigl \{\theta \leqslant \epsilon^ {\prime} \bigr \} & \leqslant A _ {1} (b / m - \epsilon^ {\prime}, \theta) \\ & \leqslant A _ {2} (b / m - \epsilon^ {\prime}, \theta) \\ & \leqslant A _ {3} (b / m - \epsilon^ {\prime}, \theta) \\ & = e ^ {- 2 (b / m - \epsilon^ {\prime}) ^ {2} m}. \end{array}
$$

□

From theorem 6 and corollary 1 we can conclude the following.

Corollary 2. Confidence estimate for an error range For $b / m \leqslant \epsilon$ and $0 < \epsilon' < b / m$ , then

$\operatorname{Prob}\{\epsilon' \leqslant \theta \leqslant \epsilon\}$

$$
\geqslant 1 - e ^ {- 2 (b / m - \epsilon) ^ {2} m} - e ^ {- 2 (b / m - \epsilon^ {\prime}) ^ {2} m}.
$$

In section 5 we apply the above results to a published application on loan default and bankruptcy and a published application on predicting stock market movements. In section 4 we present a learning algorithm used in section 5 and derive some results for this method.

## 4. An analysis of ID3

A popular inductive learning algorithm is ID3 [20]. ID3 is easy to implement and has given excellent results in a number of applications (e.g., see [19]). ID3 builds a decision tree from a training sample.

ID3 operates on domains where instances can be represented by a finite vector of attributes. The attributes may have nominal values. We assume that each attribute has a finite number of possible values. (This assumption can be relaxed as shown later).

ID3 constructs a decision tree as follows:

Algorithm 1. ID3 (1) If all instances are either positive or negative examples, then the tree is a single leaf node of corresponding sign.

(2) Otherwise:

(a) Let i be an attribute that optimizes some criterion for choosing an attribute. Create a node labeled with i;

(b) Partition the instances into k groups. For each partition, form a branch from the node to a decision tree recursively constructed.

In step 2a a large number of different criteria have been used, including a measure of information content [20], a chi-squared contingency table statistic [15], probability measures [16], gain-ratio [20], Marshall correlation [12], and others [16].

In step 2b., partitioning can be accomplished in a number of ways. For nominal or discrete attributes, the most common partitioning is along each possible value of the attribute. For attributes with a large number of values, the instances are typically split in two.

The decision tree constructed by ID3 will always correctly classify all the training examples provided that no two examples having identical attribute values yet are labelled as belonging to different groups. In such cases, either the set of attributes are insufficient for the classification or there is noise in the data. For this paper, we have implicitly assumed that the training sample, Q, does not contain such contradictions.

To determine the sample size for $(\epsilon,\delta)$ -learning using theorem 1, we have to determine the Vapnik-Chervonenkis dimension of the hypothesis space, H.

Let $A_{i}$ be the cardinality of the set of permissible values for attribute $i, 1 \leqslant i \leqslant L$ , where L is the number of attributes that define the domain X. Hence,

$$
n \equiv \prod_ {i = 1} ^ {L} A _ {i},
$$

is the total number of distinct instances in $X$ .

Since each distinct instance can be classified as positive or negative, the total number of concepts that can be defined by decision trees on X is $2^{n} = |H|$ .

For a sample that consists of n distinct instances (i.e., all X), the maximum number of possible concepts induced by H is $2^{n}$ , therefore

$$
\operatorname{VCdim} (H) = n.
$$

Applying Theorem 1 with $|H|=2^{n}$ and $\mathrm{VCdim}(H)=n$ , we can derive the sample size needed for $(\epsilon,\delta)$ -learning using inductive decision trees. This is summarized in the following.

Theorem 7. Sample size for ID3 (1) For any given $\epsilon$ and $\delta$ , with $0 \leqslant \epsilon$ , $\delta \leqslant 1$ , if the sample size is at least

$$
\left[ \ln (1 / \delta) + n \ln 2 \right] / \epsilon .
$$

then ID3 will $\epsilon$ -exhaust $H$ with probability at least $1 - \delta$ .

(2) For

$$
0 <   \epsilon <   1 / 2
$$

then ID3 must use a sample size of at least

$$
\max \left\{\left[ (1 - \epsilon) / \epsilon \right] \ln (1 / \delta), \right.
$$

$$
\left. n \big [ 1 - 2 (\epsilon (1 - \delta) + \delta) \big ] \right\}.
$$

Using $|H|=2^{n}$ and $\mathrm{VCdim}(H)=n$ , the second term of Theorem 1, part (1), can be shown to be greater than the first. This observation gives the first part of Theorem 7. It is also easy to show that part (1) of Theorem 7 gives a value always greater than the size of X. For ID3, this bound is too loose because $|H|$ and $\mathrm{VCdim}(H)$ are large. Further research is needed to find a better upper bound. The second part of Theorem 7 results from substituting the $\mathrm{VCdim}(H)$ for ID3 into part (2) of theorem 1.

When the training and testing domain are equivalent, then Theorem 5 can be used to obtain a bound on the probability of error. Otherwise, Theorem 6 and its corollaries provide a useful alternative since they are independent of $|H|$ and $\mathrm{VCdim}(H)$ .

For example, to use ID3 for a problem with 5 attributes, each having 5 possible values, and requiring $\epsilon = 0.01$ and $\delta = 0.01$ , at least

$\max \{455.9, 5^5(0.9602)\} = 3001,$

samples would be necessary. Suppose we used a sample size of 1000 for training and had a test sample of size 30 that gave one misclassification. Further suppose that the test and training domains are equivalent. The value of $p^{*}$ in Theorem 5 is 2736. From theorem 5 we get

$$
\begin{array}{r l} \operatorname{Prob} \{\theta \geqslant 0. 7 0 \} & \leqslant 1. 0 - 0. 0 0 0 1 4 6 \\ & = 0. 9 9 9 8 5 4, \end{array}
$$

and

$$
\begin{array}{r l} \operatorname{Prob} \{\theta \geqslant 0. 7 5 \} & \leqslant 1. 0 - 0. 9 9 9 4 3 2 \\ & = 0. 0 0 0 5 6 8. \end{array}
$$

Thus, the worst posterior estimate of the error, $\epsilon$ , is likely to be between 70 and 75%.

If the training and testing domains are different, Theorem 6 gives a bound of

$$
\begin{array}{r l} \operatorname{Prob} \{\theta \geqslant 0. 3 0 \} & \leqslant e ^ {- 2 (\epsilon - b / m) ^ {2} m} \\ & = e ^ {- 2 (0. 3 - 1 / 3 0) (0. 3 - 1 / 3 0) 3 0} \\ & = 0. 0 1 4 0 3, \end{array}
$$

and

$$
\begin{array}{r l} \operatorname{Prob} \{\theta \geqslant 0. 3 2 \} & \leqslant e ^ {- 2 (\epsilon - b / m) ^ {2} m} \\ & = e ^ {- 2 (0. 3 2 - 1 / 3 0) (0. 3 2 - 1. 3 0) 3 0} \\ & = 0. 0 0 7 2 2. \end{array}
$$

For the desired value of $\theta = 0.01$ , we get $\operatorname{Prob}\{\theta \geqslant 0.01\} \leqslant 0.96786$ .

Now consider the case where attributes can take on an infinite number of values. For real-valued attributes, the ID3 algorithm is usually modified as follows. Let $V_{i}=\{v_{1}<v_{2}<\ldots\}$ be the set of values of attribute i found in the training sample for use in step 2 of ID3. There are at most $|Q|$ such values. Consider the $k=|V_{i}|-1$ intervals of the form

$$
\begin{array}{l} \left[ - \infty , (v _ {1} + v _ {2}) / 2 \right], \\ \left[ - \infty , (v _ {2} + v _ {3}) / 2 \right], \\ \dots \\ \left[ - \infty , (v _ {k - 1} + v _ {k}) / 2 \right]. \end{array}
$$

One of these is chosen at step 2a and used to split the cases in step 2b.

When both $|H|$ and $\mathrm{VCdim}(H)$ are infinite, Theorem 1 provides no useful sample size bounds. Also, Theorem 5 is useless. It is precisely for reasons such as these that Theorem 3 and Theorem 6 and its corollaries are useful.

## 5. Applications

After a decision tree is constructed by ID3, it is applied to a test sample to evaluate its predictive accuracy. Researchers report the misclassification rate on test data, with lower rates signalling better results.

Messier and Hansen [13] used ID3 to classify default and non-default loans originally studied using discriminant analysis by Abdel-Khalik and El-Sheshai [1]. Thirty-two training examples were used to induce a decision tree. Sixteen independent test examples were used to validate their results. Many of the attributes in this study were real valued.

The training sample were selected from time periods prior to 1975. The validation sample was selected from 1975–1976 data. Hence, this represents a case of learning and validating with different domains.

Strictly speaking, since some of the attributes are real valued, we are unable to use theorem 1 to determine training sample sizes to guarantee PAC-identification. Even without this stumbling block, Theorem 7 casts considerable doubt on the adequacy of such a small sample size of 32 instances.

Applying Theorem 5, we can evaluate the inductive function determined with the 1975–1976 data. For the 16 test examples, 14 (87.5%) were classified correctly and 2 (12.5%) were misclassified.

Suppose we are interested in the probability that $\theta$ is greater than 0.2. Under the assumptions of Theorem 3 we get

$$
\begin{array}{l} \operatorname{Prob} \{\theta \geqslant 0. 2 \} \\ = \sum_ {k = 0} ^ {2} C _ {k} ^ {1 7} 0. 2 ^ {k} (1 - 0. 2) ^ {1 7 - k} = 0. 3 0 9 6. \end{array}
$$

In words, the probability that the error of the learned concept is greater than 20% is 0.3096. Theorem 6 gives

$$
\operatorname{Prob} \{\theta \geqslant 0. 2 \} \leqslant 0. 8 3 5 2 7,
$$

and

$$
\operatorname{Prob} \{\theta \geqslant 0. 3 \} \leqslant 0. 3 7 3 5 1.
$$

Messier and Hansen [13] further applied ID3 to discriminate bankrupt and non-bankrupt firms based on a study in [11]. Data on 39 Australian firm were split into 23 training examples and 16 testing examples. The inductive function derived from 23 training example successfully classified all 16 test examples. From Theorem 3, the likelihood that the error of this concept is greater than 0.2 is

and

$$
\operatorname{Prob} \{\theta \geqslant 0. 0 0 5 \} = 0. 9 1 8 3.
$$

For these same cases, Theorem 6 gives

$$
\operatorname{Prob} \{\theta \geqslant 0. 2 \} \leqslant 0. 2 7 8 8,
$$

$$
\operatorname{Prob} \{\theta \geqslant 0. 1 \} \leqslant 0. 7 2 6 2,
$$

$$
\operatorname{Prob} \{\theta \geqslant 0. 0 1 \} \leqslant 0. 9 9 6 8,
$$

and

$$
\operatorname{Prob} \{\theta \geqslant 0. 0 0 5 \} \leqslant 0. 9 9 2.
$$

The overall higher confidence of this study might be because the testing and training samples are actually from the same set of data.

Another application of ID3 can be found in predicting stock market behavior. Braun and

Chandler [5] used a data base of 80 examples from an expert's predictions dating from March 20, 1981 to September 24, 1982. Some of the variables were real valued.

Two tests were performed with this data base. The first test randomly split the examples into two groups of 40. ID3 was used to induce rules from one group. The rules was then used to predict the behavior of the other group, which correctly predicted 23 out of 40 (57.5%) examples. Using Theorem 3, we can compute

$$
\operatorname{Prob} \{\theta \geqslant 0. 5 \} = 0. 1 7 4 4.
$$

and

$$
\operatorname{Prob} \{\theta \geqslant 0. 3 \} = 0. 9 5 8 6.
$$

That is, the probability that the learned concept has an error greater than 30% is 0.9586. Theorem 6 gives

$$
\operatorname{Prob} \{\theta \geqslant 0. 5 \} \leq 0. 8 3 5 3,
$$

and

$$
\operatorname{Prob} \{\theta \geqslant 0. 3 \} \leq 0. 6 0 6 5.
$$

In an effort to improve their results, Braun and Chandler [5] increased the number of examples used for learning to 60. This left 20 examples for testing. The induced rules from 60 examples correctly predicted 13 out of 20 (65%) examples. Theorem 3 gives

and

$$
\operatorname{Prob} \{\theta \geqslant 0. 3 \} = 0. 7 2 3 0.
$$

Thus, there is up to a 77% chance that the learned concept has an error greater than 30% – essentially the same result obtained with the smaller training set. Theorem 6 gives

and

## 6. Summary and conclusions

Inductive inference methods are attractive for a number of reasons. Two of the more compelling reasons are: (1) They do not require parametric assumptions, unlike methods such as discriminant analysis; and (2) they can be used on nominal and structural attributes, in addition to rank or interval strength data.

Experimental studies have illustrated the usefulness of inductive inference methods. Recent theoretical analyses aimed at guaranteeing a given accuracy level for a learned concepts suggests, however, that large sample sizes may be required in many training sessions. Even worse, for some types of learning, there are no useful theoretical bounds for determining the size of an adequate sample. From a practical point of view, it is often impossible to obtain a sufficiently large sample size.

We provide several methods for measuring the accuracy of a learned concept. Our procedure uses the misclassification rate of the concept applied to a test sample. Bounds on the error and confidence factors are easily computed from the misclassification rate. Applying these bounds to several published studies casts some doubts on the results of the latter.

Another commonly encountered situation argues for our approach. It is often the case that a concept is learned from examples in one time period but applied to cases in another time period. Strictly speaking, the two domains are different. Our results show how the accuracy of the concept can be estimated in the new domain.

## References

[1] A.R. Abdel-Khalik and K.M. El-Sheshai, Information Choice and Utilization in an Experiment on Default Prediction, J. Accounting Research (Autumn 1980) 325-342.

[2] M. Abramowitz and I. Segun, Handbook of Mathematical Functions (Dover Publications, New York, 1968).

[3] D. Angluin and P. Laird, Learning from Noisy Examples, Machine Learning 2 (1988) 343–370.

[4] A. Blumer, A. Ehrenfeucht, D. Haussler and M. Warmuth, Learnability and the Vapnik-Chervonenkis Dimension, Technical Report UCSC-CRL-87-20 (Computer Research Laboratory, University of California, Santa Cruz, CA, 1987).

[5] H. Braun and J.S. Chandler, Predicting Stock Market Behavior through Rule Induction: An Application of the

Learning-from-Example Approach, Decision Sciences 18 (1987) 415–429.

[6] W.W. Cooley and P.R. Lohnes, Multivariate Data Analysis (Wiley, New York, 1971).

[7] A. Ehrenfeucht, D. Haussler, M. Kearns and L. Valiant, A General Lower Bound on the Number of Examples Needed for Learning, Technical Report UCSC-CRL-87-26 (Computer Research Laboratory University of California, Santa Cruz, CA, 1988).

[8] H.W. Gould, Combinatorial Identities (Morgantown Printing and Binding Co., Morgantown, WV, 1972).

[9] D. Haussler, Quantifying Inductive Bias: AI Learning Algorithms and Valiant's Learning Framework, Artificial Intelligence 36 (1988) 177–221.

[10] W. Hoeffding, Probability Inequalities for Sums of Bounded Random Variables, J. American Statistical Association 58 (1963) 13–30.

[11] R. Libby, K.T. Trotman and I. Zimmer, Member Variation, Recognition of Expertise, and Group Performance, J. Applied Psychology (1987) 81–87.

[12] R. Marshall, Partitioning Methods for Classification and Decision Making in Medicine, Statistics in Medicine 5 (1986) 517–526.

[13] W.F. Messier and J.V. Hansen, Inducing Rules for Expert Systems Development, Management Science 34, No. 12 (1988) 1403–1415.

[14] R.S. Michalski, A Theory and Methodology of Inductive Learning, Artificial Intelligence 20 (1983) 111–161.

[15] J. Mingers, Inducing Rules for Expert Systems, Journal of the Operational Research Society 37 (1986) 19–24.

[16] J. Mingers, An Empirical Comparison of Selection Measures for Decision-Tree Induction, Machine Learning 3 (1989) 319–342.

[17] T.M. Mitchell, Generalization as Search, Artificial Intelligence 18 (1982) 203–226.

[18] D.B. Peizer and J.W. Pratt, A Normal Approximation for Binomial, F, Beta and Other Common Related Tail Probabilities, I, American Statistical Association Journal (Dec. 1968) 1416–1456.

[19] J.R. Quinlan, Semi-Autonomous Acquisition of Pattern-Based Knowledge, Introductory Readings in Expert Systems (Gordon and Breach, New York, 1982).

[20] J.R. Quinlan, Induction of Decision Trees, Machine Learning 1 (1986) 81–106.

[21] H. Raiffa and R. Schlaifer, Applied Statistical Decision Theory (Division of Research, Harvard Business School, 1961).

[22] M.J. Shaw and J.A. Gentry, Using an Expert System with Inductive Learning to Evaluate Business Loans, Financial Management (Autumn 1988) 45–56.

[23] L.G. Valiant, A Theory of the Learnable, Comm. ACM 27, No. 11 (1984) 1134–1142.

[24] R.L. Winkler, Introduction to Bayesian Inference and Decision (Holt, Rinehart and Winston, New York, 1972).
