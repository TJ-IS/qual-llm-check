---
otero_id: 8754
otero_key: "VPW4UBQJ"
title: "Histogram distance-based Bayesian Network structure learning: A supervised classification specific approach"
authors: "B. Sierra; E. Lazkano; E. Jauregi; I. Irigoien"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Histogram distance-based Bayesian Network structure learning: A supervised classi<sup>fi</sup>cation speci<sup>fi</sup>c approach

B. Sierra ⁎, E. Lazkano, E. Jauregi, I. Irigoien

Dept. of Computer Science and Artificial Intelligence, University of the Basque Country, Spain

## a r t i c l e i n f o

Article history: Received 16 May 2008 Received in revised form 12 June 2009 Accepted 22 July 2009 Available online 6 August 2009

Keywords: Bayesian Network Histogram distance Supervised classi<sup>fi</sup>cation Machine learning Structure learning

## a b s t r a c t

In this work we introduce a methodology based on histogram distances for the automatic induction of Bayesian Networks (BN) from a <sup>fi</sup>le containing cases and variables related to a supervised classi<sup>fi</sup>cation problem. The main idea consists of learning the Bayesian Network structure for classi<sup>fi</sup>cation purposes taking into account the classi<sup>fi</sup>cation itself, by comparing the class distribution histogram distances obtained by the Bayesian Network after classifying each case. The structure is learned by applying eight different measures or metrics: the Cooper and Herskovits metric for a general Bayesian Network and seven different statistical distances between pairs of histograms.

The results obtained con<sup>fi</sup>rm the hypothesis of the authors about the convenience of having a BN structure learning method which takes into account the existence of the special variable (the one corresponding to the class) in supervised classi<sup>fi</sup>cation problems

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

Almost any practical intelligent application requires dealing with uncertainty. This uncertainty may be motivated by the inherent complexity of the problem, by the technical limitation of the data collection machines (Interval Error in single data, low resolution in images, etc.), by safety considerations (radioactive trace of a patient could give good information, but it is not applicable), or it could be due to the impossibility to collect or to manage all the data needed to perform the reasoning.

Until recently, the application of strict probabilistic approaches to reasoning was considered impractical due to the problem of computing the joint probability distribution of a large number of random variables involved in reasoning. However, the emergence of the concept of conditional (in)dependency allowed to simplify the calculus involved and made the evolution of automatic methods for reasoning under uncertainty based on probability theory possible.

The last decade has seen signi<sup>fi</sup>cant theoretical advances and an increasing interest in probabilistic graphical models (PGMs), the most widely used of the probability based methods. These models represent dependency relationships within a set of random variables, where the random variables are represented as nodes in a graph. The absence of arcs in the graph corresponds to independence and its presence means possible dependence between two variables. One of the most popular types of graphical models is Bayesian Networks (BN). In these type of models arcs are directed, and there should not be a directed cycle in the whole graph [11,37,46]. Much research has been devoted to the BN structure learning task [13,14,25]. However, the problem of acquiring good BN structures in general, and in particular for structures which would serve as classi<sup>fi</sup>cation models, remains open.

Most of the structure learning algorithms need two components (score+ search): the learning algorithm itself that guides the search, and the metric for evaluating the structure at each time step of the learning process. The objective of this work is to look for new metrics for Bayesian Network structure learning algorithms. We concentrate on supervised classi<sup>fi</sup>cation problems and, more speci<sup>fi</sup>cally, on the use of histogram distances for computing the differences between the class a posteriori distribution a given net structure should give to a case, and the real category that case belongs to.

## 2. Motivation

Supervised classi<sup>fi</sup>cation tasks are related to classi<sup>fi</sup>cation problems in which the perfect classi<sup>fi</sup>er does not exist or is not known; these models belong to the machine learning (ML) area [43]. In the supervised classi<sup>fi</sup>cation process the goal is to distinguish the kind (class, category) of examples or cases. Given a database, experiments are usually carried out using a known learning algorithm to induce the corresponding classi<sup>fi</sup>er from the data; then the obtained model is used to classify new cases of the same problem. For example, given a database of patients, where each patient (case) is labelled as having or not having a speci<sup>fi</sup>c disease, a classi<sup>fi</sup>er for the cases in this database is constructed, and the obtained model is used to classify new patients (cases) with the aim of helping the physician in the process of diagnosis. Hence, it is only after the classi<sup>fi</sup>er is constructed that the obtained model can be used to classify new cases.

In the machine learning area, there are three main approaches to learn a classi<sup>fi</sup>er model:

1. Obtain a model by using a given measure for constructing the classi<sup>fi</sup>er; classi<sup>fi</sup>cation trees and rule inducers belong to this kind of models. With respect to the Bayesian Network induction, Naive Bayes models could also be considered as belonging to this category. Many machine learning/data mining applications use entropy or (conditional) mutual information as metrics for selecting features and/or structure in these models. And many common algorithms for learning decision trees use mutual information to select attributes for internal nodes of the trees [48] as well.

2. Obtain the classi<sup>fi</sup>er by maximizing some probability measure given the data. A learning procedure typically attempts to take out the parameters of the distribution P(Given case|Class) to maximize the likelihood of the training data. Most of the Bayesian Network structure learning algorithms work in this manner, for instance the K2 algorithm and the BIC approach, both described later on.

3. Obtain a classi<sup>fi</sup>cation model by maximizing the classi<sup>fi</sup>cation power itself. Neural Networks and Support Vector Machines are members of this third group, as well as most of the so-called multiclassi<sup>fi</sup>er systems [41].

On the other hand, probability based classi<sup>fi</sup>ers can be of two different types:

1. Generative models where all variables and responses are obtained from the joint probability distribution functions. Naive Bayes, Hidden Markov Models and Bayesian Networks are of this type of models.

2. Discriminative models, which only optimize a mapping from inputs to desired outputs [44], identifying outgoing parameters to maximize the ability of the model to discriminate between the classes. Examples of this kind of paradigms are logistic regression, Support Vector Machines, Neural Networks and K-nearest neighbor algorithm.

The histogram distance-based BN learning approach presented in this paper makes use of distances among the a posteriori distributions of the class variable to guide the search of the structure of BNs with classi<sup>fi</sup>cation purposes. This new method does not belong fully to any of above mentioned approaches. In fact, it can be considered a mixture. On the one hand, it looks for the structure that maximizes a measure and it performs a computation over the a posteriori probabilities of the class variable. On the other hand, it looks for a generalization model by means of a metric, with a clearly discriminative approach.

The main motivation of this approach is the hypothesis, based on previous experiences, that the relation between some metric values is not adequate when the future use of the BN is to classify new cases in supervised classi<sup>fi</sup>cation problems. We are concerned about the correctness of the metric calculation process, but we do realize that this does not guarantee the discriminative capability of the obtained model. The underlying idea is to have a measure of the classi<sup>fi</sup>cation capabilities of the BN, which at the same time should give good generalization capabilities.

The main characteristic of this new method is that it is intended to model the behavior of the class variable not only in the majority class value, but in all its amplitude. The obtained model should take into account the characteristic of the BNs — and of the probabilistic methods in general — of giving a certainty measure in relation to the classi<sup>fi</sup>cation assigned. In other words, the result a BN gives when classifying a case is a vector containing the a posteriori probabilities for all the values the class variable can take. For instance, if the class variable takes 4 different values, the classi<sup>fi</sup>cation response is a 4 element vector $\left( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } \right)$ where $\textstyle \sum x _ { 1 } = 1$ . Therefore, the vector contains the value distribution of the class variable for the given case. Typically, the case would be classi<sup>fi</sup>ed as belonging to the class x<sub>j</sub> with the highest a posteriori probability. However, taking into account the a posteriori distribution of the class variable during the BN structure leaning process should in principle allow to obtain models with higher classi<sup>fi</sup>cation capabilities.

The rest of the paper is organized as follows: Section 3 reviews how BNs are used as supervised classi<sup>fi</sup>ers. Section 4 brie<sup>fl</sup>y reviews the concept of BNs and it is fully devoted to the description of how the structure or graph of BNs can be automatically acquired from data. Section 5 presents the new proposed approach as a metric to measure how adequate a given structure is for a classi<sup>fi</sup>cation task; Section 6 shows the three phase experimental setup we have designed to evaluate the performance of the new approach, and the obtained results are presented in Section 7. Finally, in Section 8 conclusions are given and further work lines are pointed out.

## 3. Related work: Bayesian Networks as classi<sup>fi</sup>ers

There is a lot of work devoted to the Bayesian Network structure learning for classi<sup>fi</sup>cation purposes. The related work shows that some structural learning approaches do take into account the existence of the class variable, and probably the most extended approach is to use the classi<sup>fi</sup>cation accuracy of the net as the metric value [1,58]. But none of the approaches treat the class variable distribution as the method proposed here treats it. Several approaches acquire the structure by representing the joint probability of all the variables involved in the model. Thus, [51] present a parameter learning for BNs devoted to classi<sup>fi</sup>cation tasks, maximizing the conditional (supervised) likelihood instead of the joint (unsupervised) one; [21] present a structural learning method that needs to take into account the existence of the class variable and obtains a tree-shaped structure, known as a Tree Augmented Network (TAN), in which the class variable is the root node. Keogh and Pazzani [29,30] present an approach to learn TAN structures not by means of probability, but guided by the accuracy; it is a greedy approach in which the concept of SuperParent method is presented. Greiner and Zhou [23] present the ELR algorithm. This algorithm maximizes the conditional likelihood of the class node to augment the discriminative capabilities of the acquired Bayesian Network. Grossman and Domingos [24] present the BNC algorithm to learn the structure of a BN maximizing the conditional likelihood; it is a greedy algorithm similar to that presented by Heckerman et al. [25] which combines user knowledge and statistical data.

Other authors take into account the conditional independence among the variables. For instance, [1] presents a local search in a space consisting of Partially Directed Acyclic Graphs (PDAGs), combining the two types of DAG equivalences: classi<sup>fi</sup>cation equivalence and independence equivalence; and [33] presents an approach that uses independence assumptions to learn BN <sup>fi</sup>nding subsets of predictor variables and augmenting the NB model using the dependencies found.

The interest in BNs as classi<sup>fi</sup>ers spreads to real applications such as microarray data analysis [34] or real world data treatment on information technology [27]. [57] uses BNs for the survival prediction of patients suffering from malignant skin melanoma. They extend the TAN approach, eliminating the restriction of the class variable to be the root node, but keeping all the predictor variables within the Markov Blanquet of the class variable. [39] uses PGMs to perform the diagnosis and control of autonomous vehicles in which the existence of the class variable is taken into account by the group of experts responsible for constructing the models. Similarly, [36] presents a real application of BNs for guiding a robot in door crossing behaviors using sonar sensor readings (which are a source of high uncertainty for the model); they show an attempt of integrating the expert knowledge of the sensor (predictor variables) location on the robot in the net structure. Bilmes et al. [3] present a real application of BNs as classi<sup>fi</sup>ers for speech recognition; they select the structure of the net by maximizing not the likelihood but a cost function that indicates how well the class conditional model performs.

## 4. Bayesian Network structure learning methods

Bayesian Networks (BN) are probabilistic graphical models represented by directed acyclic graphs (DAGs) in which nodes are variables and arcs show the (in)dependencies among the variables [10,28]. Fig. 1 shows an example of a BN structure speci<sup>fi</sup>cally obtained for a classi<sup>fi</sup>cation task, where $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ are the predictor variables and Cl, the variable corresponding to the class.

BNs are founded on the concept of conditional independence among variables [45]. This concept makes possible a factorization of the probability distribution of the n-dimensional random variable $( X _ { 1 } , . . . , X _ { n } )$ in the following way:

$$
P (x _ {1}, \ldots , x _ {n}) = \prod_ {i = 1} ^ {n} P (x _ {i} | \pi (x _ {i}))
$$

where x represents the value of the random variable $X _ { i } ,$ and π(x ) represents the value of the random variables parents of $X _ { i \cdot }$

Thus, in order to specify the probability distribution of a BN, one must give prior probabilities for all root nodes (nodes with no predecessors) and conditional probabilities for all other nodes, given all possible combinations of their direct predecessors. These values, in conjunction with the DAG, specify the BN completely. Once the network is constructed, it constitutes an ef<sup>fi</sup>cient device to perform probabilistic inference. Evidence propagation or probabilistic inference consists of, given an instantiation of some of the variables (i.e. giving values to some of the variables), obtaining the a posteriori probability of one or more of the non-instantiated variables [26]. This probabilistic reasoning inside the net can be carried out by exact methods, as well as by approximated methods. However, it is known that this computation is a NP-hard problem [16].

Summarizing, two things determine the behavior of a BN: its structure (the nodes and the links among the nodes) and the probability tables associated with the nodes. The structure and conditional probabilities necessary for characterizing the network can be either provided externally by experts or obtained from an algorithm which automatically induces them [13]. In order to establish the Bayesian Network structure [25], it can be the human expert who designs the network taking advantage of his/her knowledge about the relations among the variables; it is also possible to learn the structure by means of an automatic learning algorithm [13,14]; and, of course, a combination of both systems can be applied, mixing the expert's knowledge and the learning mechanism.

![](/api/attachments/VPW4UBQJ/fulltext/images/0e3a7dc5dec57290e84d9edf0a56ec83435e607ae4e4d9633654ad3636aba555.jpg)  
Fig. 1. An example of a Bayesian Network structure.

It is well known that modelling the expert knowledge has become an expensive, almost unreliable and time-consuming job, and that structure learning algorithms have become an important research area. During the last years, several papers have been devoted to the presentation of algorithms whose aim is to induce the structure of the Bayesian Network that better represents the conditional independence relationships underlying in the data; see for example [8,47], and more recently [22].

Regarding the structural learning methods, they generally need two components: the learning algorithm and the evaluation metric that will measure the goodness of the net during each learning step (score+ search). Most of the different approaches to the structure learning mentioned in the literature are related to multiple connected networks and are grouped according to the necessity or not of imposing order on the variables (see [25] for a good review). Assuming an order among the variables implies that a variable $X _ { i }$ can have the variable $X _ { j }$ as a parent only if $X _ { j }$ precedes $X _ { i }$ in the established order. With this restriction, the cardinality of the space that contains all the structures is given by $2 ^ { \binom { n } { 2 } }$ , where n is the number of variables in the system. Methods developed by [2,17,18] and [5] assume this restriction.

If we do not assume ordering between the nodes, the cardinality of the search space is bigger, and the number of networks grows hyperexponentially [49].

In the rest of this section the two structure learning algorithms involved in the experiments are reviewed: the K2 algorithm and the B-learning algorithm. These algorithms are used as prototypes for each of the approaches (ordered and non-ordered variables) with the aim of comparing the learning capabilities of the acquired BNs.

## 4.1. The K2 algorithm

K2 is an algorithm proposed by Cooper and Herskovits that creates and evaluates a BN from a database of cases. The K2 algorithm assumes that an ordering on the variables is available and that, a priori, all structures are equally likely. Fig. 2 shows the algorithm in pseudo-code form. Given a database D, K2 searches the BN structure $B _ { s ^ { * } }$ with maximal $P ( B _ { \cal { S } } | D )$ [17]:

$B _ { \varsigma ^ { * } } = \arg \operatorname* { m a x } _ { \varsigma } P ( B _ { \varsigma } | D )$ where $P ( B _ { 5 } | D ) = P ( B _ { 5 } ) \prod _ { i = 1 } ^ { n } g ( i , \pi ( X _ { i } ) )$ and

$\begin{array} { r } { g ( i , \pi ( X _ { i } ) ) = \prod _ { j } ^ { q _ { i } } { _ 1 \frac { ( r _ { i } - 1 ) ! } { ( N _ { i j } + r _ { i } - 1 ) ! } \prod _ { k } ^ { r _ { i } } } = { _ 1 N _ { i j k } } ! } \end{array}$ is the expression of the Cooper and Herskovits (CH) metric, also referred to as K2 metric.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Ordering, Database + metric.
Output: net structure
for i = 1 to n do
    $\pi_i = \emptyset$
    p_old = g(i, $\pi_i$)
    ok_to_proceed = true
    while ok_to_proceed and |$\pi_i$| &lt; max_parents
    do
    z = argmax_k g(i, $\pi_i \bigcup \{k\}$) where z ∈ pred(i)
    p_new = g(i, $\pi_i \bigcup \{z\}$)
    if p_new &gt; p_old then
    p_old = p_new
    $\pi_i = \pi_i \bigcup z$
    else
    ok_to_proceed = false
    end if
    end while
end for
</div>

Fig. 2. Pseudo-code of the K2 structural learning algorithm.

```txt
Input: Database + metric.
Output: net structure
BN structure: let the starting structure be a fully disconnected BN
Value = metric(BN structure);
ok_to_proceed = true
while ok_to_proceed do
    Value_to_compare_with = metric(BN structure);
    Arc_to_add = none;
    for each of the possible arcs which could be added to BN structure do
    Add the current_arc to BN structure
    if introduces a cycle in the BN then
    remove current_arc from BN structure;
    else
    Value_act = metric(BN structure);
    if Value_act > Value_to_compare_with then
    Value_to_compare_with = Value_act;
    Arc_to_add = current_arc;
    end if
    end if
end for
if Arc_to_add = none then
    ok_to_proceed = false; /* No metric value increase with any arc */
else
    Add Arc_to_add to BN structure;
end if
end while
```  
Fig. 3. Pseudo-code of the B algorithm.

K2 is a greedy heuristic. It starts by assuming that a node does not have parents, and then, in every step, it incrementally adds the parent whose addition most increases the probability of the resulting structure. However, only those nodes that correspond to variables that precede the node being processed are considered as candidates. K2 stops adding parents to the nodes when the addition of a single parent cannot increase the probability. Obviously, this approach does not guarantee the selection of a structure with the highest probability.

## 4.2. B-learning algorithm

Algorithm B is an hill-climbing heuristic search that obtains a general purpose Bayesian Network structure (i.e. a DAG, not necessarily for classi<sup>fi</sup>cation tasks) and does not need any order on variables; this algorithm was <sup>fi</sup>rst proposed by Buntine in the early 90s [9]. Like algorithm K2, algorithm B is a greedy search algorithm that begins with the arc-less network and then, for each node, incrementally adds the parent whose addition most increases the score of the resulting structure and does not introduce a cycle into the structure. When no addition of a single parent can increase the score, it stops adding parents to the node. Fig. 3 shows the pseudo-code of this algorithm. In the <sup>fi</sup>gure, Bouckaert's [6] accurate explanation of the algorithm is presented.

![](/api/attachments/VPW4UBQJ/fulltext/images/73bd48957e604df742397e60018bac3db63d90c1dcb86ac8b4cb9997b1c2aa24.jpg)

## 5. Histogram distances as new metric for structural learning of BN

Histograms are no more than graphical representations of tabulated frequencies. In this paper histogram refers to the representation of the frequencies of the values that the variables we are working with can take. Histograms divide the feature space X into M regions, and these regions often form a regularly spaced grid, e.g. they are hypercubes of same size, although this is not a strict requirement. Since we work with discrete variables (the categories or classes), we will use discrete histograms showing the distribution of each of the class values. Another reason to use histograms is that they are simple non-parametric approaches for density estimation that can be computed very quickly and, what is more, they can be calculated incrementally. This last property is useful for the calculation of histograms in a parallel way. Fig. 4 shows an example of a frequency histogram and its corresponding cumulative histogram for a 6 value variable.

Histograms are popular in several research areas. For instance, in Choi et al. [15] histograms are applied in the area of biometrics. Within the supervised classi<sup>fi</sup>cation area, they are commonly used in real applications related to image analysis, both for image segmentation [61] and for object indexing within image databases [54,55] or object recognition in photographs [40].

Within the context of acquiring the structure of a BN, histogram comparisons can be used to measure the distance between the a posteriori distribution of the class variable given by the computation of the conditional probability of the class, and the real class.

Therefore, we use histogram distances as measures for the differences existing between two multinomial variable distributions. In this way, the computed distance is a mean of the distances among a set of cases; to compute this mean value, for each case, the distribution corresponding to the real class (known in the training data) is compared with the a posteriori distribution of the class variable, which is given by the Bayesian Network given the case. The idea has been inspired by the Neural Network research area [32,42,43,52].

For the sake of distance measurement goodness, the real class distribution is de<sup>fi</sup>ned by giving an α value to the real class of the case, and dividing the remaining (1−α) evenly among the rest of class values. For example, if we had a two class classi<sup>fi</sup>cation problem and a case belonging to the <sup>fi</sup>rst class value, the distribution would be considered to be {α, 1−α} instead of the real one {1, 0}; if the class was a <sup>fi</sup>ve value variable, and the training case was labelled as class number two, then the distribution used to calculate histogram distances would be $\left\{ { \frac { 1 - \alpha } { 4 } } , \alpha , { \frac { 1 - \alpha } { 4 } } , { \frac { 1 - \alpha } { 4 } } , { \frac { 1 - \alpha } { 4 } } \right\}$ that would replace {0.1, 1.0, 0.0, 0.0, 0.0}. Note that the histograms are normalized due to the nature of the data they contain.

![](/api/attachments/VPW4UBQJ/fulltext/images/01388d303712f3454bb76c99b2a2efdbebfb2a592847023cc76f6808ac93afb6.jpg)  
Fig. 4. Frequency and cumulative histograms corresponding to the same distribution.

Fig. 5 shows the new proposed BN structure evaluation method in algorithmic form. This algorithm gives the measure of a given structure, and can be used in conjunction with local search structure learning algorithms in order to evaluate a candidate structure to decide whether one arc has to be included or not; nevertheless, more complex approaches could be used (Genetic Algorithms [57], Estimation of Distribution Algorithms [50], etc.) which make use of other kinds of algorithms to evaluate candidate structures.

## 5.1. Histogram comparison

However, how to measure the dissimilarity between histograms of the real class and the a posteriori distribution of the class values offered by the evidence propagation must be de<sup>fi</sup>ned. In the rest of the article, we will refer to the whole histogram (H) with capital letters, and to the component values of the histogram $H { = } h _ { 1 } , h _ { 2 } { , \dots } , h _ { m }$ with lower-case letters. The histogram comparisons to be performed will consider the values of each category in both histograms, $H _ { 1 } = ( h 1 _ { 1 } , . . . ,$ $h 1 _ { m } )$ and $H _ { 2 } = ( h 2 _ { 1 } , . . . , h 2 _ { m } )$ in a general m class problem, and will work with these values to obtain the difference. The next subsections explain some well known distances that will be used later in the experimental phase. Although more approaches exist (see [53]), the authors believe that the tested distance set is variate enough to show how the working hypothesis holds for a set of standard databases.

## 5.2. Euclidean distance (Euk)

Probably the most used distance for any comparison is the well known Euclidean distance, which is computed as follows:

$$
E u k (H 1, H 2) = \sqrt {\sum_ {i = 1} ^ {m} (h 1 _ {i} - h 2 _ {i}) ^ {2}}.
$$

## 5.3. Kullback–Leibler distance (KL)

Mutual information is a measure of the shared information between two variables. The greater the mutual information, the

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Structure, Database with C cases, n
predictor variables and m classes + Histogram
distance function.
Output: net value
for Case = 1 to C do
    Let class(Case) = k
    Value = 0;
    H1Case = {(1) =  $\frac{1-\alpha}{m-1}$ , ..., (k) =  $\alpha$ , ..., (m) =  $\frac{1-\alpha}{m-1}$ };
    for Variable = 1 to n do
    /*Instantiation of the BN nodes*/;
    Node(Variable) = Case(Variable)
    end for
    /*Obtain the a posteriori probabilities for the
    m possible values of the class variable */;
    Propagate the evidence
    Let p(k) be the a posteriori probability of
    class = k
    H2Case = {(1) = p(1), ..., (k) = p(k), ..., (m) = p(m)};
    ValueCase = HistogramDistance(H1Case; H2Case);
    Value = Value + ValueCase;
end for
</div>

Fig. 5. Pseudo-code of the new proposed approach. A value for a given BN structure is obtained

higher the similarity between the two variables. The relative entropy, also known as the Kullback–Leibler's distance (KL) or the divergence is a measure that assesses the opposite of the mutual information. Assuming that two variables of the same type are characterized by their probability distribution H1 and H2, the relative entropy is given by:

$$
K L (H 1, H 2) = \sum_ {i = 1} ^ {m} \left(h 1 _ {i} \times \ln \frac {h 1 _ {i}}{h 2 _ {i}}\right)
$$

where m is the number of levels of the histogram. It has to be highlighted that the measure is asymmetrical (only H terms appear in the left side of the multiplication).

## 5.4. Manhattan distance (Manh)

This distance computes the differences between two histograms by simply summing up the absolute differences of each of the m components.

$$
M a n h (H 1, H 2) = \sum_ {i = 1} ^ {m} | h 1 _ {i} - h 2 _ {i} |.
$$

## 5.5. Kolmogorov–Smirnov distance (KS)

This is a very simple distance, but it has a wide use in the comparison of statistical distributions. The maximum absolute difference among the m values of each histogram is given as distance measure.

$$
K S (H 1, H 2) = \max _ {i = 1} ^ {m} | h 1 _ {i} - h 2 _ {i} |.
$$

$$
5. 6. C h i - s q u a r e d i s t a n c e (\chi^ {2})
$$

The chi-square test is used to test if a sample of data comes from a population with a speci<sup>fi</sup>c distribution.

Considering $H _ { 1 }$ the observed distribution (the a posteriori probabilities obtained by the propagation approach for the class node) and $H _ { 2 }$ the expected one, the $\chi ^ { 2 }$ value can be calculated according to the following expression:

$$
\chi^ {2} (H 1, H 2) = \sum_ {i = 1} ^ {m} \frac {(h 1 _ {i} - h 2 _ {i}) ^ {2}}{h 2 _ {i}}.
$$

## 5.7. Histogram intersection (Int)

Histogram intersection yields a goodness of match value where 1.0 is a perfect match and 0.0 is the worst possible match. The intersection value is calculated by the following equation:

$$
I n t (H 1, H 2) = \sum_ {i = 1} ^ {m} \min (h 1 _ {i}, h 2 _ {i}).
$$

## 5.8. Jeffrey-divergence distance (Jeff)

The Jeffrey-divergence distance is the symmetric version of KL:

$$
J e f f (H 1, H 2) = \sum_ {i = 1} ^ {m} \bigg (h 1 _ {i} \times \ln \frac {h 1 _ {i}}{h 2 _ {i}} + h 2 _ {i} \times \ln \frac {h 2 _ {i}}{h 1 _ {i}} \bigg).
$$

## 6. Experimental setup

To perform the experimentation and evaluate the adequateness of the new approach, some datasets were selected from the UCI repository of machine learning datasets [4], as listed in Table 1. Some datasets are those included in the analysis in [21] and the rest are included in the analysis in [38]. We used 10-fold cross-validation [59] to get a validated classi<sup>fi</sup>cation accuracy. Table 1 provides details of the training set sizes used in this work. All datasets were preprocessed in the same way as previous authors did: datasets with continuous variables were discretised using the discretisation utility in MLC++ [31] with its default entropy-based setting [20], and cases with missing values removed from datasets. For the experiments described below, α was set to 0.7; this value was <sup>fi</sup>xed after the preliminary experiments were performed over <sup>fi</sup>ve of the databases.

Table 1 Details of databases.

<table><tr><td>Database</td><td>Num. of cases</td><td>Num. of classes</td><td>Num. of attributes</td></tr><tr><td>Breast</td><td>699</td><td>2</td><td>9</td></tr><tr><td>Cars</td><td>395</td><td>3</td><td>7</td></tr><tr><td>Cleveland</td><td>296</td><td>2</td><td>11</td></tr><tr><td>Corral</td><td>129</td><td>2</td><td>6</td></tr><tr><td>Crx</td><td>768</td><td>2</td><td>8</td></tr><tr><td>Diabetes</td><td>768</td><td>2</td><td>8</td></tr><tr><td>German</td><td>1000</td><td>2</td><td>15</td></tr><tr><td>Glass</td><td>214</td><td>7</td><td>7</td></tr><tr><td>Glass2</td><td>163</td><td>2</td><td>5</td></tr><tr><td>Iris</td><td>150</td><td>3</td><td>4</td></tr><tr><td>Lenses</td><td>24</td><td>3</td><td>4</td></tr><tr><td>Monk1</td><td>432</td><td>2</td><td>6</td></tr><tr><td>Vehicle</td><td>846</td><td>4</td><td>19</td></tr><tr><td>Vote</td><td>435</td><td>3</td><td>16</td></tr></table>

The selected databases are different in nature; some of them have a large number of predictor variables, or a large number of cases, and others are multi-class problems.

In order to overcome the problem of generalization capability of the Bayesian Network paradigms, specially with the so-called sparse data [35], and with the objective of performing a sound experimentation that would help in developing adequate conclusions, we divided the experiment into three separated phases.

## 6.1. Linear correlation analysis

The purpose of this phase is to analyze the relationship (if any) existing between the value each metric assigns to a given BN structure and the well classi<sup>fi</sup>ed performance obtained by using it as a classi<sup>fi</sup>cation model. The correlations to be analyzed are those among the different metrics and the performances obtained over the training set results, and also, over the test set results — obtained by means of the 10-fold cross-validation. This linear correlation would suggest the generalization capabilities of the obtained models, as training accuracies and the corresponding validated ones can be compared. The authors are aware that this relationship does not need to be linear, but they postulate that a linear relationship would determine a strong link among the value the metric gives to a given net structure and the percentage of well classi<sup>fi</sup>ed cases obtained with the net. The BN structures have been learned using the K2 algorithm, together with the eight different metrics previously mentioned. Since the K2 algorithm runs for a given variable ordering, the learning process was repeated for 1000 random orders for each of the metrics.

## 6.2. Structure learning by B algorithm

The objective of this phase is to show the validity of the proposed distances as metrics for BN structure learning algorithms to get models for supervised classi<sup>fi</sup>cation problems. The classi<sup>fi</sup>cation performance comparison itself is done using the Bayesian Networks obtained by each of the proposed metrics as supervised classi<sup>fi</sup>cation paradigms. In this second phase the B structure learning is used with the eight metrics, and the validated accuracy obtained by each of them is presented.

Table 2 Table 2  
Linear correlation value $( R ^ { 2 } )$ between the metric value and the accuracy for the training data.

<table><tr><td>DB</td><td>K2</td><td>Euk</td><td>Manh</td><td> $\chi^2$ </td><td>KL</td><td>KS</td><td>Int</td><td>Jeff</td></tr><tr><td>Breast</td><td>0.0013</td><td>0.5380</td><td>0.0003</td><td>0.0001</td><td>0.1229</td><td>0.5951</td><td>0.7149</td><td>0.2443</td></tr><tr><td>Cleveland</td><td>0.0000</td><td>0.0693</td><td>0.0013</td><td>0.0020</td><td>0.0057</td><td>0.0785</td><td>0.3124</td><td>0.9976</td></tr><tr><td>Cars</td><td>0.0040</td><td>0.8925</td><td>0.0022</td><td>0.0004</td><td>0.7393</td><td>0.6579</td><td>0.0011</td><td>0.0009</td></tr><tr><td>Crx</td><td>0.0297</td><td>0.0929</td><td>0.0992</td><td>0.2984</td><td>0.0968</td><td>0.5645</td><td>0.5939</td><td>0.0598</td></tr><tr><td>Corral</td><td>0.4674</td><td>-</td><td>0.2131</td><td>0.0909</td><td>0.1055</td><td>0.5766</td><td>0.4856</td><td>0.5184</td></tr><tr><td>Diabetes</td><td>0.0945</td><td>0.0150</td><td>0.0269</td><td>0.0196</td><td>0.3882</td><td>0.1126</td><td>0.6040</td><td>0.0929</td></tr><tr><td>Glass</td><td>0.3025</td><td>1.000</td><td>0.8168</td><td>0.8095</td><td>0.6350</td><td>0.0011</td><td>0.8927</td><td>0.2961</td></tr><tr><td>Glass2</td><td>0.1245</td><td>0.2402</td><td>0.0019</td><td>0.0200</td><td>0.0287</td><td>-</td><td>0.2688</td><td>0.1392</td></tr><tr><td>German</td><td>0.0004</td><td>0.5372</td><td>0.1704</td><td>0.2370</td><td>0.2110</td><td>0.1557</td><td>0.1367</td><td>0.9943</td></tr><tr><td>Iris</td><td>0.0093</td><td>-</td><td>0.0080</td><td>0.0095</td><td>0.0003</td><td>-</td><td>0.1919</td><td>0.9987</td></tr><tr><td>Lenses</td><td>0.5347</td><td>0.3180</td><td>0.8556</td><td>0.7209</td><td>0.7148</td><td>0.0781</td><td>0.8688</td><td>0.8682</td></tr><tr><td>Monk1</td><td>1.0000</td><td>-</td><td>0.0036</td><td>0.3912</td><td>1.0000</td><td>0.0145</td><td>0.0055</td><td>0.0188</td></tr><tr><td>Vehicle</td><td>0.093</td><td>-</td><td>0.471</td><td>0.0006</td><td>0.199</td><td>0.366</td><td>0.683</td><td>0.339</td></tr><tr><td>Vote</td><td>0.0271</td><td>0.0049</td><td>0.0058</td><td>0.0711</td><td>0.1581</td><td>0.1776</td><td>0.1424</td><td>0.2202</td></tr></table>

## 6.3. Classifier comparison

The aim of this last step is to obtain comparable results between the two approaches in order to validate the new method as a learning mechanism for Bayesian Networks with classi<sup>fi</sup>cation purposes. The B algorithm is used again in this <sup>fi</sup>nal phase, where the K2 metric is compared with one of the proposed histogram distances. New databases are selected from those used in the BN literature.

## 7. Experimental results

## 7.1. Linear correlation analysis: results

Table 2 shows the $R ^ { 2 }$ values obtained with the training datasets for each metric, and in Table 3 the same $R ^ { 2 }$ values are shown but this time the comparison is made between the metrics and the validated accuracy. The “−” sign means that the same value has been obtained for all of the proposed orders, and hence it is not possible to obtain a linear regression among the points (they are all the same).

It can be noted that in both tables, except for a few exceptions, a notorious relationship does not exist, especially for the values corresponding to the cross-validation results in Table 2. The objective of this phase and of the numeric results provided is to show the tendency for that correlation to exist (direct or indirect, depending on the metric) as it can be appreciated in Figs. 6 and 7. The relationship between the values given by Int, KL and Jeff metrics, and the percentages of well classi<sup>fi</sup>ed cases obtained, with both training data and validation data must be highlighted. These correlation results prove the three metrics as promising measures to be used within BN structural learning algorithms for classi<sup>fi</sup>cation purposes. It is worth highlighting the results obtained with the K2 metric. Although the correlation is not impressive, it appears to be stronger with validation data than with training data. This result con<sup>fi</sup>rms the good performance and explains the wide use of the K2 metric in the literature for acquiring nets for classi<sup>fi</sup>cation.

Linear correlation (R<sup>2</sup>) between the metric value and the validated accuracy (10-fold cross-validation).

<table><tr><td>DB</td><td>K2</td><td>Euk</td><td>Manh</td><td> $\chi^2$ </td><td>KL</td><td>KS</td><td>Int</td><td>Jeff</td></tr><tr><td>Breast</td><td>0.272</td><td>0.453</td><td>0.001</td><td>0.002</td><td>0.123</td><td>0.548</td><td>0.715</td><td>0.099</td></tr><tr><td>Cleveland</td><td>0.409</td><td>0.075</td><td>0.020</td><td>0.009</td><td>0.006</td><td>0.078</td><td>0.312</td><td>0.995</td></tr><tr><td>Cars</td><td>0.014</td><td>0.889</td><td>0.001</td><td>0.000</td><td>0.750</td><td>0.661</td><td>0.000</td><td>0.000</td></tr><tr><td>Crx</td><td>0.027</td><td>0.091</td><td>0.104</td><td>0.249</td><td>0.097</td><td>0.564</td><td>0.594</td><td>0.06</td></tr><tr><td>Corral</td><td>0.641</td><td>1.000</td><td>0.218</td><td>0.075</td><td>0.559</td><td>0.423</td><td>0.455</td><td></td></tr><tr><td>Diabetes</td><td>0.127</td><td>0.006</td><td>0.025</td><td>0.019</td><td>0.388</td><td>0.113</td><td>0.604</td><td>0.093</td></tr><tr><td>Glass</td><td>0.406</td><td>1.000</td><td>0.782</td><td>0.739</td><td>0.635</td><td>0.000</td><td>0.875</td><td>0.299</td></tr><tr><td>Glass2</td><td>0.116</td><td>0.165</td><td>0.01</td><td>0.000</td><td>0.029</td><td>-</td><td>0.269</td><td>0.203</td></tr><tr><td>German</td><td>0.046</td><td>0.616</td><td>0.219</td><td>0.261</td><td>0.211</td><td>0.156</td><td>0.137</td><td>0.985</td></tr><tr><td>Iris</td><td>0.014</td><td>-</td><td>0.026</td><td>0.026</td><td>0.000</td><td>-</td><td>0.192</td><td>0.998</td></tr><tr><td>Lenses</td><td>0.609</td><td>0.239</td><td>0.741</td><td>0.711</td><td>0.549</td><td>0.332</td><td>0.676</td><td>0.645</td></tr><tr><td>Monk1</td><td>1.000</td><td>-</td><td>0.001</td><td>0.323</td><td>1.000</td><td>0.006</td><td>0.013</td><td>0.06</td></tr><tr><td>Vehicle</td><td>0.089</td><td>-</td><td>0.638</td><td>0.021</td><td>0.003</td><td>0.007</td><td>0.764</td><td>0.553</td></tr><tr><td>Vote</td><td>0.041</td><td>0.004</td><td>0.013</td><td>0.069</td><td>0.158</td><td>0.193</td><td>0.142</td><td>0.220</td></tr></table>

Figs. 6 and 7 show the existing linear correlation for the German and Vote databases respectively. Each plot shows the obtained classi<sup>fi</sup>cation accuracy and the corresponding metric value for each of the 1000 random orders. Hence, the X axis represents the classi<sup>fi</sup>cation accuracy $( 0 \% . . . , 1 0 0 \% )$ and the Y axis shows the metric value. Notice that the Y axis range varies depending on the metric function used.

The next subsection explains a different structural learning algorithm more appropriate for the classifying purposes sought in this work.

## 7.2. Structure learning by B algorithm: results

In this phase, B algorithm was used to obtain the BN structures; in every experiment the corresponding measure (K2 or a histogram distance) is used to decide whether an arc has to be added or not, and which arc when appropriate. Table 4 shows the results obtained. Note

![](/api/attachments/VPW4UBQJ/fulltext/images/6673350637b0a90dbaa2b3f50d2d04cc1970dc38bb8e0cd6406de14269f350d3.jpg)  
Fig. 6. German Credit database. X axis is the corresponding metric value and Y axis is the obtained accuracy.

![](/api/attachments/VPW4UBQJ/fulltext/images/7f4fd33d74dac715b34092f54441879a2cc05377437036588de5b2161eec5dd6.jpg)  
Fig. 7. Vote database. X axis is the corresponding metric value and Y axis is the obtained accuracy.

that all the metrics obtain valid classi<sup>fi</sup>cation results for every database when the B algorithm is used.

The K2 metric gives good results, obtaining the best performance for 5 of the 14 databases tested. All in all, K2 is one of the most powerful metrics within the area of BNs and it has been rather successfully used for classi<sup>fi</sup>cation purposes [36]. It can also be noted that good results are obtained with different metrics, outperforming K2 metric (here used as a reference) several times. For instance, KL and KS metrics present results within the best ones for 4 (of 14) databases, and Jeff performs the best for 6 of them (with some ties). At the other end of the performance spectrum, $\chi ^ { 2 }$ and Euk distances give poorer results than expected. It is worth noticing the high degree of variability obtained with the paradigms for the different classi<sup>fi</sup>cation problems; the same paradigm gives a very good performance for some of the problems while it performs badly for others. More precisely, KL and KS are among the worst, three and six times respectively, giving poor results on average.

To conclude, it must be highlighted that the K2 metric never gives the best results when the classi<sup>fi</sup>cation problem has more than two classes.

In order to have a reasonable impression of the obtained results, a comparison among all the metrics is performed, as proposed in [19]. As shown in Table 5, the best two approaches seem to be K2 and Jeffrey metrics, the latter having a better rank mean (2.96) than the former (3.56). However, the obtained Fisher–Snedecor F value is 1.86, which does not allow to decide if there is a best algorithm over all the others; and when Wilcoxon test is applied to these two metrics no signi<sup>fi</sup>cant differences are found. That is the reason for the inclusion of a third experimental phase, in which these best metrics are compared as classi<sup>fi</sup>ers using a new set of UCI data<sup>fi</sup>les.

Table 4  
Validated accuracies (10-fold cross-validation) obtained by using B algorithm.

<table><tr><td>DB</td><td>K2</td><td>Euk</td><td>Manh</td><td> $\chi^2$ </td><td>KL</td><td>KS</td><td>Int</td><td>Jeff</td></tr><tr><td>Breast</td><td>96.05 ± 2.67</td><td>95.75 ± 1.76</td><td>95.17 ± 1.95</td><td>95.32 ± 1.92</td><td>92.98 ± 4.07</td><td>95.32 ± 1.79</td><td>95.32 ± 2.04</td><td>95.76 ± 2.00</td></tr><tr><td>Clev</td><td>80.75 ± 6.74</td><td>72.05 ± 10.11</td><td>48.68 ± 9.48</td><td>72.03 ± 9.22</td><td>78.77 ± 8.76</td><td>48.68 ± 9.48</td><td>48.68 ± 9.48</td><td>76.69 ± 8.98</td></tr><tr><td>Cars</td><td>65.03 ± 7.75</td><td>68.59 ± 6.07</td><td>61.44 ± 5.90</td><td>68.81 ± 6.12</td><td>68.35 ± 9.64</td><td>61.44 ± 5.90</td><td>61.44 ± 5.90</td><td>73.19 ± 5.81</td></tr><tr><td>Corral</td><td>100.00 ± 0.00</td><td>76.47 ± 12.77</td><td>41.35 ± 9.32</td><td>78.14 ± 14.09</td><td>74.94 ± 10.31</td><td>41.35 ± 9.32</td><td>41.35 ± 9.32</td><td>78.91 ± 13.76</td></tr><tr><td>Crx</td><td>74.72 ± 8.91</td><td>86.23 ± 2.42</td><td>86.38 ± 2.46</td><td>86.38 ± 2.42</td><td>86.38 ± 2.78</td><td>86.38 ± 2.46</td><td>86.38 ± 2.46</td><td>86.38 ± 2.46</td></tr><tr><td>Diab</td><td>76.18 ± 3.47</td><td>64.72 ± 6.01</td><td>75.52 ± 5.20</td><td>75.52 ± 5.20</td><td>74.35 ± 3.08</td><td>64.07 ± 4.31</td><td>64.07 ± 4.31</td><td>74.35 ± 3.08</td></tr><tr><td>Glass</td><td>71.06 ± 7.04</td><td>67.23 ± 9.22</td><td>70.15 ± 10.42</td><td>62.68 ± 9.29</td><td>44.70 ± 17.84</td><td>76.08 ± 8.02</td><td>71.00 ± 9.58</td><td>72.86 ± 9.17</td></tr><tr><td>Glass2</td><td>83.38 ± 4.35</td><td>57.65 ± 9.18</td><td>87.68 ± 4.24</td><td>87.68 ± 4.24</td><td>87.68 ± 4.24</td><td>79.04 ± 9.10</td><td>79.04 ± 9.10</td><td>87.68 ± 4.24</td></tr><tr><td>Germ</td><td>72.90 ± 5.92</td><td>70.00 ± 4.08</td><td>70.00 ± 4.08</td><td>70.00 ± 4.08</td><td>70.00 ± 4.08</td><td>70.00 ± 4.08</td><td>70.00 ± 4.08</td><td>70.00 ± 4.08</td></tr><tr><td>Iris</td><td>94.00 ± 4.92</td><td>92.00 ± 6.89</td><td>91.33 ± 5.49</td><td>91.33 ± 5.49</td><td>96.00 ± 4.66</td><td>96.00 ± 3.44</td><td>96.00 ± 3.44</td><td>95.33 ± 4.50</td></tr><tr><td>Lenses</td><td>55.00 ± 30.48</td><td>65.00 ± 26.59</td><td>20.00 ± 26.99</td><td>65.00 ± 26.59</td><td>65.00 ± 26.59</td><td>15.00 ± 25.40</td><td>20.00 ± 26.99</td><td>65.00 ± 26.58</td></tr><tr><td>Monk1</td><td>46.17 ± 3.29</td><td>74.92 ± 6.14</td><td>48.96 ± 1.39</td><td>74.92 ± 6.14</td><td>74.92 ± 6.14</td><td>48.96 ± 1.39</td><td>48.96 ± 1.39</td><td>88.41 ± 13.00</td></tr><tr><td>Vote</td><td>95.41 ± 3.77</td><td>95.18 ± 3.98</td><td>95.63 ± 3.68</td><td>95.18 ± 3.98</td><td>95.18 ± 3.98</td><td>95.63 ± 3.68</td><td>95.63 ± 3.68</td><td>94.95 ± 3.72</td></tr><tr><td>Vehic</td><td>67.38 ± 6.13</td><td>56.03 ± 4.62</td><td>57.82 ± 5.35</td><td>58.29 ± 5.52</td><td>65.97 ± 7.18</td><td>63.01 ± 2.99</td><td>63.84 ± 4.19</td><td>71.76 ± 5.72</td></tr></table>

## 7.3. Classifier comparison: results

In the previous subsections the proposed approach is shown as comparable to the well known K2 metric; once the similarity has been shown, a comparison of the two approaches (K2 and Jeffrey metrics) as classi<sup>fi</sup>ers is presented here, using the B algorithm to obtain the BN structures. To do so, some new databases have been selected from those used in [38]. It can be noted in Table 6 that, again, the selected databases cover a wide variety of problem stereotypes. The Naive Bayes classi<sup>fi</sup>er (NB) has also been included in the table in order to have a comparison with a very well known paradigm.

Experimental results (also in Table 6) show that Jeffrey metric outperforms K2 for seven (of 11) databases. As can be noted, this difference is obtained not only for two-class problems (two to one) but also for multi-class problems (<sup>fi</sup>ve to three). Therefore, the metric presented in this work outperforms with a score of 15 to 10 of the 25 databases used. To sum up, the overall behavior of the nets acquired with the proposed methodology can be considered as very positive. These results lead the authors to state that the presented approximation is valid for learning the structure of BNs for classi<sup>fi</sup>cation purposes. Both approaches outperform the NB classi<sup>fi</sup>er in the used databases with the same discretisation.

## 8. Conclusions and further work

model obtained is being used for supervised classi<sup>fi</sup>cation problems. Although commonly used, they generally do not take into account the existence of a special variable, namely the class, that is of central interest for the intended model.

In this paper, a new method for BN structure learning is proposed with the aim of improving the behavior of the BN when the network

The new proposed metrics do take into account the <sup>fi</sup>nal objective of models for supervised classi<sup>fi</sup>cation problems and measure the goodness of the model being acquired in terms of its classi<sup>fi</sup>cation capabilities.

To validate the method, the relationship between the value each metric gives to a network structure and the classi<sup>fi</sup>cation performance of the structure has been analyzed, not only for the training datasets, but also for the data used for validating the model. Such relationship showed that the metrics proposed in this paper give better correlation values than other metrics between the metric value and the classi<sup>fi</sup>- cation capabilities of the models. They also improve the generalization capabilities of the models.

Obtained results con<sup>fi</sup>rm that the presented methodology is appropriate, and that some of the tested metrics are very well suited for measuring the classi<sup>fi</sup>cation capabilities of a BN model. Jeffrey distance stands out, showing good generalization capabilities and high percentages in the posterior validation of the obtained models. In fact, Jeffrey-divergence metric is one of the most successful distance metrics encountered in mobile robot localization, when whole image histogram features are used to identify their position in real time against a database of previously recorded images of locations in their environments [56].

Still, the effect of the α parameter has to be analyzed. This parameter not only can affect the correlation between the metric and the performance of the net, but also the classi<sup>fi</sup>cation accuracy itself. Using a <sup>fi</sup>xed value of α for all the databases we have obtained good classi<sup>fi</sup>cation results, but the selection of a speci<sup>fi</sup>c α value for each classi<sup>fi</sup>cation problem could be a way of improving the obtained accuracy.

Table 5  
Rank orders and Fisher test algorithm results for each of the metrics based on the results showed on Table 4.  
Table 6  
Details of databases and validated accuracies (10-fold cv) for K2 and Jeffrey metrics; B algorithm is used.

<table><tr><td>DB</td><td>K2</td><td>Euk</td><td>Manh</td><td> $X^{2}$ </td><td>KL</td><td>KS</td><td>Int</td><td>Jeff</td></tr><tr><td>Breast</td><td>1.00</td><td>3.00</td><td>7.00</td><td>5.00</td><td>8.00</td><td>5.00</td><td>5.00</td><td>2.00</td></tr><tr><td>Clev</td><td>1.00</td><td>4.00</td><td>7.00</td><td>5.00</td><td>2.00</td><td>7.00</td><td>7.00</td><td>3.00</td></tr><tr><td>Cars</td><td>5.00</td><td>3.00</td><td>7.00</td><td>2.00</td><td>4.00</td><td>7.00</td><td>7.00</td><td>1.00</td></tr><tr><td>Corral</td><td>1.00</td><td>4.00</td><td>7.00</td><td>3.00</td><td>5.00</td><td>7.00</td><td>7.00</td><td>2.00</td></tr><tr><td>Crx</td><td>8.00</td><td>6.50</td><td>3.00</td><td>6.50</td><td>3.00</td><td>3.00</td><td>3.00</td><td>3.00</td></tr><tr><td>Diab</td><td>1.00</td><td>6.00</td><td>2.50</td><td>2.50</td><td>4.50</td><td>7.50</td><td>7.50</td><td>4.50</td></tr><tr><td>Glass</td><td>3.00</td><td>6.00</td><td>5.00</td><td>7.00</td><td>8.00</td><td>1.00</td><td>4.00</td><td>2.00</td></tr><tr><td>Glass2</td><td>5.00</td><td>8.00</td><td>2.50</td><td>2.50</td><td>2.50</td><td>6.50</td><td>6.50</td><td>2.50</td></tr><tr><td>Germ</td><td>1.00</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td></tr><tr><td>Iris</td><td>5.00</td><td>6.00</td><td>7.50</td><td>7.50</td><td>2.00</td><td>2.00</td><td>2.00</td><td>4.00</td></tr><tr><td>Lenses</td><td>5.00</td><td>2.50</td><td>6.50</td><td>2.50</td><td>2.50</td><td>8.00</td><td>6.50</td><td>2.50</td></tr><tr><td>Monk1</td><td>8.00</td><td>3.00</td><td>6.00</td><td>3.00</td><td>3.00</td><td>6.00</td><td>6.00</td><td>1.00</td></tr><tr><td>Vote</td><td>4.00</td><td>6.00</td><td>2.00</td><td>6.00</td><td>6.00</td><td>2.00</td><td>2.00</td><td>8.00</td></tr><tr><td>Vehic</td><td>2.00</td><td>8.00</td><td>7.00</td><td>6.00</td><td>3.00</td><td>5.00</td><td>4.00</td><td>1.00</td></tr><tr><td>Rank mean</td><td>3.57</td><td>5.07</td><td>5.36</td><td>4.54</td><td>4.18</td><td>5.14</td><td>5.18</td><td>2.96</td></tr></table>

<table><tr><td>Database</td><td>Num. of cases</td><td>Num. of classes</td><td>Num. of attributes</td><td>NB</td><td>Jeff</td><td>K2</td></tr><tr><td>Balance-scale</td><td>625</td><td>3</td><td>4</td><td>90.23</td><td>69,57</td><td>90,23</td></tr><tr><td>Echocardiogram</td><td>131</td><td>2</td><td>7</td><td>67.20</td><td>67.20</td><td>62.58</td></tr><tr><td>Flare</td><td>1066</td><td>3</td><td>12</td><td>99.53</td><td>99.53</td><td>99.16</td></tr><tr><td>Hayes</td><td>162</td><td>3</td><td>4</td><td>66.25</td><td>67,50</td><td>63.13</td></tr><tr><td>Led</td><td>846</td><td>10</td><td>7</td><td>73.93</td><td>72.66</td><td>71.34</td></tr><tr><td>Lymphography</td><td>148</td><td>4</td><td>18</td><td>64.67</td><td>71.52</td><td>69.67</td></tr><tr><td>Mushroom</td><td>8123</td><td>2</td><td>22</td><td>94.37</td><td>99.42</td><td>99.82</td></tr><tr><td>Solar</td><td>323</td><td>6</td><td>12</td><td>61.45</td><td>72.99</td><td>72.36</td></tr><tr><td>Three_of_9</td><td>512</td><td>2</td><td>9</td><td>66.55</td><td>87.11</td><td>82.44</td></tr><tr><td>Waveform</td><td>5000</td><td>3</td><td>19</td><td>58.22</td><td>76.78</td><td>80.76</td></tr><tr><td>Zoo</td><td>101</td><td>7</td><td>16</td><td>75.27</td><td>81.27</td><td>86.27</td></tr></table>

Further work should include the use of more sophisticated paradigms as structure learning algorithms and the application of Estimation of Distribution Algorithms [50] in conjunction with the new proposed metric. A Feature Selection process [12] could also be used. It also would be interesting and highly recommendable to increase the effort in developing classi<sup>fi</sup>er comparison methods in ML, in the direction proposed by [7], and testing the approach with incomplete databases [60].

## Acknowledgements

This work has been supported by the Basque Country Government under Research Team <sup>fi</sup>nanciation, and by the University of the Basque Country.

## References

[1] S. Acid, L.M. de Campos, J.G. Castellano, Learning Bayesian Network classi<sup>fi</sup>ers: searching in a space of partially directed acyclic graphs, Machine Learning 59 (2005) 213–235.

[2] S. Acid, L.M. de Campos, J.F. Huete, The search of causal orderings: a short cut for learning belief networks, Proceedings of the European Conference on Symbolic and Quantitative Approaches to Reasoning with Uncertainty, 2001, pp. 216–227.

[3] J. Bilmes, G. Zweig, T. Richardson, K. Filali, K. Livescu, P. Xu, K. Jackson, Y. Brandman E. Sandness, E. Holtz, J. Torres, B. Byrne, Discriminatively structured graphica models for speech recognition, UWEE Technical Report Series, 2001.

[4] C.L. Blake, C.J. Merz, UCI Repository of Machine Learning Databases, 1998.

[5] R.R. Bouckaert, Properties of Bayesian Belief Network learning algorithms, Proceedings of the 10th Annual Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence (UAI-94), Morgan Kaufmann, San Francisco, CA, 1994, pp. 102–110.

[6] R.R. Bouckaert. Bayesian Belief Networks: from inference to construction. PhD thesis, Faculteit Wiskunde en Informatica, Utrecht University, 1995.

[7] R.R. Bouckaert, Estimating replicability of classi<sup>fi</sup>er learning experiments, Proceedings of the 21th International Conference on Machine Learning, 2004.

[8] R.R. Bouckaert, E. Castillo, J.M. Gutiérrez, A modi<sup>fi</sup>ed simulation scheme for inference in Bayesian Networks, International Journal of Approximate Reasoning 14 (1996) 55–80.

[9] W.L. Buntine, Theory re<sup>fi</sup>nement of Bayesian Networks, Uncertainty in Arti<sup>fi</sup>cial Intelligence, 1991.

[10] E. Castillo, J.M. Gutiérrez, A.S. Hadi, Expert Systems and Probabilistic Network Models, Springer-Verlag, 1997.

[11] H. Chan, A. Darwiche, On the revision of probabilistic belief using uncertain evidence, Artificial Intelligence 163 (2005) 67-90.

[12] Y. Chen, D. Liginlal, A maximum entropy approach to feature selection in knowledgebased authentication, Decision Support Systems 46 (2008) 388–398.

[13] J. Cheng, R. Greiner, J. Kelly, D. Bell, W. Liu, Learning belief networks from data: an information theory based approach, Arti<sup>fi</sup>cial Intelligence 137 (2002) 43–90.

[14] D.M. Chickering, Optimal structure identi<sup>fi</sup>cation with greedy search, Journal of Machine Learning Research 3 (2002) 507–554.

[15] S. Choi, S. Yoon, S.H. Cha, C.C. Tappert, Use of histogram distances in iris authentication, Proceedings of MCSCE 2004 MLMTA, 2004.

[16] G.F. Cooper, The computational complexity of probabilistic inference using Bayesian Belief Networks, Arti<sup>fi</sup>cial Intelligence 42 (2–3) (1990) 393–405.

[17] G.F. Cooper, E.A. Herskovits, A Bayesian method for the induction of probabilistic networks from data, Machine Learning 9 (1992) 309–347.

[18] L.M. de Campos, J.M. Puerta, Stochastic local algorithms for learning belief networks: searching in the space of orderings, Lecture Notes in Arti<sup>fi</sup>cial Intelligence 2143 (2001) 228–239.

[19] J. Demsar, Statistical comparisons of classi<sup>fi</sup>ers over multiple data sets, Journal of Machine Learning Research 7 (2006) 1–30.

[20] U.M. Fayyad, K.B. Irani, Multi-interval discretization of continuous-valued attributes for classi<sup>fi</sup>cation learning, in: Morgan Kauffman (Ed.), Proceedings of the 13th International Joint Conference on Arti<sup>fi</sup>cial Intelligence, 1993, pp. 1022–1029.

[21] N. Friedman, D. Geiger, M. Goldszmidt, Bayesian Network classi<sup>fi</sup>ers, Machine Learning 19 (4) (1997) 131–163.

[22] N. Friedman, D. Koller, Being Bayesian about network structure. A Bayesian approach to structure discovery in Bayesian Networks, Machine Learning 50 (2003) 95–125.

[23] R. Greiner, W. Zhou, Structural Extension to Logistic Regression: Discriminative Parameter Learning, 2002.

[24] D. Grossman, P. Domingos, Learning Bayesian Network classi<sup>fi</sup>ers by maximizing conditional likelihood Proceedings of the 21th International Conference on Machine Learning, 2004

[25] D. Heckerman, D. Geiger, D.M. Chickering, Learning Bayesian Networks: the combination of knowledge and statistical data, Machine Learning 20 (1995) 197–243.

[26] M. Henrion, Propagating uncertainty in Bayesian Networks by probabilistic logic sampling, Proceedings of the Fourth Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, 1988, pp. 149–163.

[27] Z. Huang, J. Li, H.S. George, S. Watts, H. Chen, Large-scale regulatory network analysis from microarray data: modi<sup>fi</sup>ed Bayesian network learning and association rule mining, Decision Support Systems 43 (2007) 1207–1225.

[28] F.V. Jensen, Introduction to Bayesian Networks, University College of London, 1996.

[29] E. Keogh, M. Pazzani, Learning Augmented Bayesian Classi<sup>fi</sup>ers: A Comparison of Distribution-based and Classi<sup>fi</sup>cation-based Approaches, 1999

[30] E. Keogh, M. Pazzani, Learning the structure of augmented Bayesian classi<sup>fi</sup>ers, International Journal on Arti<sup>fi</sup>cial Intelligence Tools 11 (4) (2002) 587–601.

[31] R. Kohavi, D. Sommer<sup>fi</sup>eld, J. Dougherty, Data mining using MLC++, a machine learning library in c++, International Journal of Arti<sup>fi</sup>cial Intelligence Tools 6 (4) (1997) 537–566.

[32] T. Kohonen, G. Barna, R. Chrisley, Statistical pattern recognition with neural networks: benchmark studies, Proceedings of the Second Annual IEEE International Conference on Neural Networks vol. 1. 1988.

[33] P. Kontkanen, P. Myllymäki, H. Tirri, Classi<sup>fi</sup>er learning with supervised marginal likelihood, Workshop of the Uncertainty on Arti<sup>fi</sup>cial Intelligence Conference, UAI 2001, 2001, pp. 277–284

[34] J.M. Lauría, P.J. Duchessi, A Bayesian belief network for it implementation decision support, Decision Support Systems 42 (2006) 1573–1588.

[35] E. Lazkano, B. Sierra, Bayes-nearest: a new hybrid classi<sup>fi</sup>er combining Bayesian Network and distance based algorithms, Lecture Notes in Arti<sup>fi</sup>cial Intelligence 2902 (2003) 171–183.

[36] E. Lazkano, B. Sierra, A. Astigarraga, J.M. Martínez-Otzeta, On the use of Bayesian Networks to develop behavior for mobile robots, Robotics and Autonomous Systems (2006), doi:10.1016/j.robot.2006.08.003.

[37] P.J.F. Lucas, Bayesian Network modelling through qualitative patterns, Arti<sup>fi</sup>cial Intelligence 163 (2005) 233–263

[38] M.G. Madden, The performance of Bayesian Network classi<sup>fi</sup>ers constructed using different techniques, Proceedings of the Probabilistic Graphical Models for Classi<sup>fi</sup>cation Workshop, ECML Conference, 2003, pp. 59–70.

[39] L.L. Madsen, U.B. Kjærulff, J. Kalwa, M. Perrier, M.A. Sotelo, Applications of probabilistic graphical models to diagnosis and control of autonomous vehicles, Whorkshop of the Uncertainty on Arti<sup>fi</sup>cial Intelligence Conference, UAI 2004, 2004.

[40] J. Martinet, Y. Chiaramella, P. Mulhem, A model for weighting image objects in home photographs, 14th International Conference on Information and Knowledge Management, 2005, pp. 760–767.

[41] J.M. Martínez-Otzeta, B. Sierra, E. Lazkano, A. Astigarraga, Classi<sup>fi</sup>er hierarchy learning by means of genetic algorithms, Pattern Recognition Letters 27 (2006) 1998–2004.

[42] W. McCulloch, W. Pitts, A logical calculus of ideas immanent in nervous activity, Bulletin of Mathematical Biophysics 5 (1943) 115–133.

[43] T. Mitchell, Machine Learning, McGraw-Hill, 1997.

[44] M. Narasimhan, J. Bilmes, A submodular–supermodular procedure with applications to discriminative structure learning, Proceedings of the 21th Annual Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence (UAI-05), AUAI Press, Arlington, Virginia, 2005, pp. 404–441.

[45] J. Pearl, Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference, Morgan Kaufmann, 1988.

[46] J. Pearl, S. Russel, Bayesian Networks, 2000

[47] G.M. Provan, M. Singh, Learning Bayesian Networks using feature selection, Fifth International Workshop on Artificial Intelligence and Statistics. 1995, pp. 450–456.

[48] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann Publishers, Los Altos, California, 1993.

[49] R.W. Robinson. Counting unlabeled acyclic digraphs. Lecture Notes in Mathematics 622: Combinatorial mathematics V 622:28-43. 1977

[50] D. Romero, P. Larrañaga, B. Sierra, Learning Bayesian Networks on the space of orderings with estimation of distribution algorithms, International Journal on Pattern Recognition and Arti<sup>fi</sup>cial Intelligence, 18 (4) (2004) 607–625.

[51] T. Roos, H. Wettig, P. Grünwald, P. Myllymäki, H. Tirri, On discriminative Bayesian Network classi<sup>fi</sup>ers and logistic regression, Machine Learning 59 (2005) 267–296.

[52] F. Rosenblatt, The perceptron: a probabilistic model for information storage and organization in the brain, Psychological Review 65 (1958) 386–408.

[53] Y. Rubner, C. Tomasi, L.J. Guibas, The earth mover's distance as a metric for image retrieval, International Journal of Computer Vision 40 (2) (2000) 99–121.

[54] E. Saykol, U. Güdükbay, O. Ulusoy, A histogram-based approach for object-based query-by-shape-and-color in image and video databases, Image and Vision Computing 23 (13) (2005) 1170–1180.

[55] D. Shen, Image registration by local histogram matching, Pattern Recognition 40 (2007) 1161–1172.

[56] R. Siegwart, I.R. Nourbakhsh, Introduction to Autonomous Mobile Robots, MIT Press, 2004.

[57] B. Sierra, P. Larrañaga, Predicting survival in malignant skin melanoma using Bayesian Networks automatically induced by genetic algorithms. An empirical comparison between different approaches, Arti<sup>fi</sup>cial Intelligence in Medicine 14 (1998) 215–230.

[58] B. Sierra, N. Serrano, P. Larrañaga, E.J. Plasencia, I. Inza, J.J. Jiménez, P. Revuelta, M.L. Mora Using Bavesian Networks in the construction of a bi-level multi-classifier Artificial Intelligence in Medicine 22 (2001) 233–248

[59] M. Stone, Cross-validation choice and assessment of statistical procedures, Journal of Royal Statistical Society 36 (1974) 111–147.

[60] M.L. Wong, Y.Y. Guo, Learning Bayesian networks from incomplete databases using a novel evolutionary algorithm, Decision Support Systems 45 (2008) 368–383.

[61] J. Xu, T. Yamasaki, K. Aizawa, 3d video segmentation using point distance histograms IEEE Int. Conf. on Image Processing (ICIP2005), 2005.

B. Sierra is an Assistant Professor in the Computer Sciences and Arti<sup>fi</sup>cial Intelligence Department at the University of the Basque Country. He received his BSc in Computer Sciences in 1990, MSc in Computer Science and Architecture in 1992 and PhD in Computer Sciences in 2000 at the University of the Basque Country. He is codirector of the Robotics and Autonomous Systems Group in Donostia-San Sebastian. Dr. Sierra is presently a researcher in the <sup>fi</sup>elds of Robotics and Machine Learning, and he is working on the use of different paradigms to improve behaviors.

E. Lazkano is an Assistant Professor in the Computer Sciences and Arti<sup>fi</sup>cial Intelligence Department at the University of the Basque Country (UPV/EHU). She received her BSc in Computer Sciences in 1992 (UPV/EHU), MSc in Arti<sup>fi</sup>cial Intelligence (Katholieke Universiteit Leuven, Belgium, 1993) and PhD in Computer Sciences in 2004 (UPV/EHU). She is codirector of the Robotics and Autonomous Systems Group in Donostia-San Sebastian. Dr. Lazkano is presently a researcher in the <sup>fi</sup>elds of Robotics, being a member of the Program Committee of International Conferences and reviewer of International Journals; she is working on the development of a behavior-based distributed probabilistic control architecture.

E. Jauregi is a PhD Student in the Department of Computer Science and Arti<sup>fi</sup>cial Intelligence of the University of the Basque Country. He obtained his BSc Degree in Computer Science in 2005. He is a member of the Robotics and Autonomous Systems Group, and a third-year PhD student. His research interests include Machine Learning Bayesian Networks and Robotics.

I. Irigoien is an Assistant Professor in the Computer Sciences and Arti<sup>fi</sup>cial Intelligence Department at the University of the Basque Country. She received his BSc in Mathematics in 1996, and PhD in Computer Sciences in 2008 at the University of the Basque Country. She has published papers in referred journals and conferences, and is the unsupervised classi<sup>fi</sup>cation expert of the research team.
