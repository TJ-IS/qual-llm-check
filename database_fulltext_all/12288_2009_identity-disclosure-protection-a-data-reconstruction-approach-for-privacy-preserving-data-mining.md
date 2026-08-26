---
otero_id: 12288
otero_key: "EBSFERA2"
title: "Identity disclosure protection: A data reconstruction approach for privacy-preserving data mining"
authors: "Dan Zhu; Xiao-Bai Li; Shuning Wu"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identity disclosure protection: A data reconstruction approach for privacy-preserving data mining<sup>☆</sup>

Dan Zhu <sup>a,</sup>⁎, Xiao-Bai Li <sup>b</sup>, Shuning Wu <sup>c</sup>

<sup>a</sup> Department of Logistics, Operations and MIS, Iowa State University, Ames, IA 50011, USA

<sup>b</sup> College of Management, University of Massachusetts Lowell, Lowell, MA 01854, USA

<sup>c</sup> ISO Innovative Analytics, 388 Market Street #750, San Francisco, CA 94111, USA

## a r t i c l e i n f o

Article history: Received 1 July 2008 Received in revised form 15 March 2009 Accepted 7 July 2009 Available online 15 July 2009

Keywords: Privacy Identity disclosure k-Anonymity Data mining Genetic algorithm

## a b s t r a c t

Identity disclosure is one of the most serious privacy concerns in today's information age. A well-known method for protecting identity disclosure is k-anonymity. A dataset provides k-anonymity protection if the information for each individual in the dataset cannot be distinguished from at least k 1 individuals whose information also appears in the dataset. There is a <sup>fl</sup>aw in k-anonymity that would still allow an intruder to discern the con<sup>fi</sup>dential information of individuals in the anonymized data. To overcome this problem, we propose a data reconstruction approach to achieve k-anonymity protection in predictive data mining. In this approach, the potentially identifying attributes are <sup>fi</sup>rst masked using aggregation (for numeric data) and swapping (for nominal data). A genetic algorithm technique is then applied to the masked data to <sup>fi</sup>nd a good subset of it. This subset is then replicated to form the released dataset that satis<sup>fi</sup>es the k-anonymity constraint.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Data-mining technologies have enabled organizations to extract useful knowledge from the data in order to better understand and serve their customers, and to gain competitive advantages [6,21,26]. While successful business applications of data mining are encouraging, there are increasing concerns about invasions to the privacy of personal information. A survey by Time/CNN [16] revealed that 93% of respondents believed companies selling personal data should be required to gain permission from the individuals whose information is being shared. In another study [9], more than 70% of participants responded negatively to questions related to the secondary use of private information. Concern about privacy threats has caused data quality and integrity to deteriorate. According to [34], 82% of online users have refused to give personal information and 34% have lied when asked about their personal habits and preferences.

This study deals with the con<sup>fl</sup>ict betweenprivacy and data mining in organizational decision support. Organizations that use their customers' records in data-mining activities are obligated to take actions to protect the identities of the individuals involved. It has been demonstrated that personal identities cannot be adequately protected by simply removing identity attributes from released data. There has been extensive research in the area of statistical databases (SDBs) on how to protect individuals' sensitive data when providing summary statistical information. The privacy issue arises in SDBs when summary statistics are derived on very few individuals' data. In this case, releasing the summary statistics may result in disclosing con<sup>fi</sup>dential data. The methods for preventing such disclosure can be broadly classi<sup>fi</sup>ed into two categories: (i) query restriction, which prohibits queries that would reveal con<sup>fi</sup>dential data, and (ii) data perturbation, which alters individual data in a way such that the summary statistics remain approximately the same. In general, both methods have been extensively investigated and employed [1]. Problems in data mining are somewhat different from those in SDBs. A data-mining task, such as classi<sup>fi</sup>cation or numeric prediction, requires working on individual records contained in a dataset. As a result, query restriction is no longer applicable and data perturbation or anonymization becomes the primary approach for privacy protection in data mining. Further, predictive data mining essentially relies on discovering relationships between data attributes. Preserving such relationships may not be consistent with preserving summary statistics. Researchers in the data-mining community have proposed various methods to resolve the con<sup>fl</sup>ict between data mining and privacy protection [4,7,14,22,23]. For example, a method for building a decision tree classi<sup>fi</sup>er from perturbed data is proposed in [3]. A framework for mining association rules from transaction data that have been randomized is presented in [11]. A set of algorithms for hiding sensitive rules is proposed in [36]. Techniques for preserving privacy in distributed data mining are discussed in [8].

A well-known method for privacy protection, called k-anonymity, was proposed in [31,33]. The basic idea is to anonymize the data such that each individual cannot be distinguished from a group of other individuals in the data. The method has gained increasing popularity in privacy-preserving data mining. However, the k-anonymity approach would, in some circumstances, still allow a data intruder to disclose the individual con<sup>fi</sup>dential information in the k-anonymized data. To overcome this problem, we propose a data reconstruction approach to achieve k-anonymity protection in predictive data mining. In this approach, the potentially identifying attributes are <sup>fi</sup>rst masked using aggregation (for numeric data) and swapping (for nominal data), without considering the k-anonymity constraint. A genetic algorithm technique is then applied to the masked data to <sup>fi</sup>nd a good subset of it. This subset is then replicated to form the released dataset that satis<sup>fi</sup>es the k-anonymity constraint. An experimental study is conducted to show the effectiveness of the proposed method.

## 2. Identity and con<sup>fi</sup>dentiality disclosure problem

A common practice for protecting identity disclosure is to remove identity related attributes from released data. Sweeney [33] demonstrated that this is not adequate in protecting personal identities. In fact, the author showed that 87% of the population in the United States can be uniquely identi<sup>fi</sup>ed using three demographic attributes: gender, date of birth, and 5-digit zip code. These attributes are normally not considered identity attributes. However, since they can potentially be used to uniquely identify a record, they are collectively called quasi-identifier (QI). The k-anonymity technique was proposed to address related identity disclosure problems [31,33]. A dataset provides k-anonymity protection if the values of the QI attributes for any individual matches those of at least k − 1 other individuals in the same dataset. The anonymity is achieved by generalization and suppression of the QI values. With k-anonymity, individual identities are better protected. However, as indicated in [20], it is still likely for an intruder to disclose the con<sup>fi</sup>dential information of individuals in the k-anonymized data. The following example demonstrates the problem.

Table 1  
An illustrative example.

<table><tr><td>ID</td><td>Age</td><td>Marital status</td><td>Blood pressure</td><td>Blood type</td><td>Test result</td></tr><tr><td colspan="6">(a) Original patient data</td></tr><tr><td>1</td><td>23</td><td>Never married</td><td>75/120</td><td>O</td><td>Negative</td></tr><tr><td>2</td><td>25</td><td>Never married</td><td>66/113</td><td>O</td><td>Positive</td></tr><tr><td>3</td><td>27</td><td>Never married</td><td>74/115</td><td>A</td><td>Negative</td></tr><tr><td>4</td><td>28</td><td>Never married</td><td>77/128</td><td>AB</td><td>Negative</td></tr><tr><td>5</td><td>32</td><td>Married</td><td>72/125</td><td>B</td><td>Negative</td></tr><tr><td>6</td><td>33</td><td>Married</td><td>93/147</td><td>O</td><td>Negative</td></tr><tr><td>7</td><td>35</td><td>Married</td><td>75/124</td><td>AB</td><td>Positive</td></tr><tr><td>8</td><td>37</td><td>Divorced</td><td>95/142</td><td>O</td><td>Negative</td></tr><tr><td>9</td><td>40</td><td>Widow(er)</td><td>88/146</td><td>A</td><td>Positive</td></tr><tr><td>10</td><td>43</td><td>Divorced</td><td>110/155</td><td>O</td><td>Positive</td></tr><tr><td>11</td><td>45</td><td>Married</td><td>90/140</td><td>O</td><td>Positive</td></tr><tr><td>12</td><td>45</td><td>Divorced</td><td>104/145</td><td>B</td><td>Positive</td></tr><tr><td colspan="6">(b) k-anonymized patient data (k=4)</td></tr><tr><td>1</td><td>20–29</td><td>Never married</td><td>75/120</td><td>O</td><td>Negative</td></tr><tr><td>2</td><td>20–29</td><td>Never married</td><td>66/113</td><td>O</td><td>Positive</td></tr><tr><td>3</td><td>20–29</td><td>Never married</td><td>74/115</td><td>A</td><td>Negative</td></tr><tr><td>4</td><td>20–29</td><td>Never married</td><td>77/128</td><td>AB</td><td>Negative</td></tr><tr><td>5</td><td>30–39</td><td>Married</td><td>72/125</td><td>B</td><td>Negative</td></tr><tr><td>6</td><td>30–39</td><td>Married</td><td>93/147</td><td>O</td><td>Negative</td></tr><tr><td>7</td><td>30–39</td><td>Married</td><td>75/124</td><td>AB</td><td>Positive</td></tr><tr><td>8</td><td>30–39</td><td>Married</td><td>95/142</td><td>O</td><td>Negative</td></tr><tr><td>9</td><td>40–49</td><td>Married</td><td>88/146</td><td>A</td><td>Positive</td></tr><tr><td>10</td><td>40–49</td><td>Married</td><td>110/155</td><td>O</td><td>Positive</td></tr><tr><td>11</td><td>40–49</td><td>Married</td><td>90/140</td><td>O</td><td>Positive</td></tr><tr><td>12</td><td>40–49</td><td>Married</td><td>104/145</td><td>B</td><td>Positive</td></tr></table>

Table 1(a) shows a complete list of 12 patients administered at a hospital in a year for a sensitive disease. The test result is con<sup>fi</sup>dential. To protect privacy, the identity related attributes, such as name and address, were removed from the dataset. Knowing they were protected in this way, the patients authorized the hospital to share the data with related professionals and organizations for medical research purposes. However, it can be seen that the value combination of the Age and Marital Status attributes for each record is unique in the dataset. Therefore, it would not be dif<sup>fi</sup>cult for an intruder to <sup>fi</sup>nd the test results of a patient if he had some knowledge about the patient's age and martial status (quasi-identi<sup>fi</sup>er). Assume, for example, a medical school student, Allen, acquired this dataset from the hospital. If he knew that a 35-year old, married classmate took this test at the hospital during the year, he can effectively identify his classmate as patient #7, who had a positive test result. Suppose Allen knew that one of his friends, aged 45 and divorced, was also in the list. Then he could also easily <sup>fi</sup>nd that his friend was patient #12, who also had a positive test result.

The k-anonymity technique can help protect against such identity disclosure problems. Table 1(b) shows the anonymized dataset released by the hospital. The generalization method was applied to the original data where the Age values were grouped into three intervals and Marital Status values were combined into two groups (with Married representing three original categories: Married, Divorced and Widow). From this dataset, Allen can no longer identify his classmate (#7) or the classmate's test result. As far as his other friend (#12) is concerned, however, Allen is still able to access con<sup>fi</sup>dential information. Although he cannot identify which record is his friend's, he still knows that his friend has a positive test result, since all of the four records in the group containing his friend's record have the same test result.

The example above demonstrates that it is still quite possible for a data intruder to disclose the con<sup>fi</sup>dential information of an individual in the k-anonymized data. k-anonymity protects identity disclosure by generalizing different but similar QI attribute values into the same value. The new values produced by the generalization operation are still correct with respect to the generalized categories. Since con<sup>fi</sup>dential values (e.g., test result) remain unchanged in k-anonymity, individuals in a group are subject to high disclosure risk if their con<sup>fi</sup>dential values in the group are the same. To overcome this problem, Machanavajjhala et al. [20] proposed a new privacy principal, called l-diversity, which requires, in addition to k-anonymity, that the con<sup>fi</sup>dential attribute should include at least l “well-represented” values in the anonymized data. This additional constraint can sometimes be hard to satisfy and usually causes much larger group sizes.

Another drawback with the k-anonymity approach, in terms of data utility, is that it signi<sup>fi</sup>cantly changes the univariate statistical properties of the QI attributes, which are very important in statistical and data warehousing applications. This problem is due to the use of generalization and suppression methods: generalization creates new nominal values instead of keeping the original nominal values in the data, while suppression results in skewed distributions (partial suppression) or no univariate information at all (full suppression) for the QI attributes. This loss of univariate information also exists in other k-anonymity based techniques such as l-diversity. The problem becomes worse when the technique is geared towards speci<sup>fi</sup>c data-mining algorithms, such as that proposed in [13].

The data reconstruction approach we propose addresses both the privacy protection and information loss problems mentioned above. Our proposed method masks the QI attributes by aggregating numeric values and swapping nominal values. Aggregation and swapping operations differ from generalization in that the aggregated and swapped values are “faked” values (as opposed to “correct” values produced by generalization). As a result, the proposed approach provides a better protection against identity disclosure. In addition, aggregation preserves approximately some important numeric univariate statistics (e.g., mean), while swapping preserves the univariate frequency distributions of nominal attributes.

## 3. The data reconstruction approach

This study deals with privacy protection problem in the context of predictive data mining. We focus our approach on classi<sup>fi</sup>cation analysis, which is a common data-mining task. The basic idea of our approach also applies to the other predictive data-mining tasks such as numerical prediction (regression). We do not, however, target unsupervised learning problems such as clustering and association rules mining (see [2,13] for example studies in these areas). The objective of our approach is to preserve classi<sup>fi</sup>cation accuracy while achieving k-anonymity. We are interested in situations where the class attribute is con<sup>fi</sup>dential (if the con<sup>fi</sup>dential attribute is a non-class attribute, it should be generally easier to accomplish the above objective, since the attribute might not be important to the classi<sup>fi</sup>cation model and consequently anonymization of the attribute may have little impact on the model). In this setting, there are three types of attributes:

• Confidential attribute, which contains private information that an individual typically does not want revealed, such as test result in the illustrative example. In k-anonymity, a con<sup>fi</sup>dential attribute will not be masked.

• Quasi-identifier, which contains attributes that can be acquired from other sources and then used to identify an individual, such as age and marital status in the example. Quasi-identi<sup>fi</sup>ers will be masked in k-anonymity.

• Non-QI attributes, which is unlikely to be obtained by an intruder, such as blood pressure and blood type in the example. These attributes will not be changed in k-anonymity.

We <sup>fi</sup>rst apply numeric value aggregation to numeric QI attributes and then nominal value swapping to nominal QI attributes.

## 3.1. Numeric value aggregation

For each numeric QI attribute, a supervised discretization method [12] is used to divide the numeric values into groups. The goal of this method is to preserve the relationships between the con<sup>fi</sup>dential (class) attribute and the numeric attributes after discretization. The method recursively splits an attribute to minimize the class entropy and uses a minimum description length criterion to determine when to stop. The algorithm evaluates the information gain on each of the potential cut points, and chooses the one with the maximum value to split. This process is repeated recursively until a stopping criterion is reached (e.g., the subset contains a single class only). Groups are formed based on the cut points, and the value of a numeric attribute is subsequently set for each instance as the median value in corresponding group. For example, in Table 1(a), when Age is considered as a QI attribute, its values will be divided into two groups based on this algorithm:

$$
\begin{array}{l} \text { Group   1:age\geq34,with   median = 28;} \\ \text { Group   2:age > 34,with   median = 40.} \end{array}
$$

Then the Age values are set to 28 for the <sup>fi</sup>rst six instances, and 40 for the last six instances.

## 3.2. Nominal value swapping

For each nominal QI attribute, we use a data swapping method, based on [29], to mask the value of the attribute. With this method, a part of the current values of the QI attributes are replaced with new values such that the lower-order statistical distributions of the masked data will be close to those of the original data. We apply a second-order feedback algorithm as described in [29], which computes the second-order frequency distributions of the original data and swaps the data such that the new data have approximately the same distributions. In [29], the data are assumed to be 0–1 valued; i.e., the number of different values for each nominal attribute $r = 2 .$ . We extend the algorithm to $r { > } 2$ to handle general multi-category data.

For classi<sup>fi</sup>cation problems, it is important to maintain the 2nd-order statistics between the class attribute and each of the QI attributes, because in many classi<sup>fi</sup>cation techniques, such as decision trees and naïve Bayes method, classi<sup>fi</sup>cation models are built based on such 2ndorder statistics. Let Y be the class attributes, which has M categories. Let $X _ { 1 } , . . . , X _ { Q }$ be the Q nominal QI attributes, including the discretized numeric QI attributes. Let N be the total number of instances of the dataset. The algorithm is described below:

1. Compute the 1st-order frequency tables $F _ { 1 } ( X _ { q } ) \ ( q = 1 , . . . , Q )$ and the 2nd-order frequency tables $F _ { 2 } ( X _ { q } , ~ Y ) ~ ( q = 1 , . . . , ~ Q )$ using the original data.

2. For $q = 1 , . . . , Q$ , perform the following swapping procedure: Find a masked $N { \times } 2$ dataset, $D = \{ Z , Y \}$ , where Z corresponds to the masked values of $X _ { q } .$ We want the 1st- and 2nd-order frequency distributions of D to be as close to $F _ { 1 } ( X _ { q } )$ and $F _ { 2 } ( X _ { q } , Y )$ as possible. This is implemented as below:

$$
\begin{array}{l l} \text {For i = 1 To N, Do} \\ \text {Choose (i, f_{i} (j), x_{qj}),} & \forall j = 1,..., J _ {q}, \\ \text {Choose (i, f_{1} (j,m), x_{qj}),} & \forall j = 1,..., J _ {q} \text {and m = ...,M}. \\ \text {End} \end{array}
$$

where $x _ { q \ j }$ is the jth category of attribute $X _ { q } , J _ { q }$ is the number of categories in $X _ { q } ,$ , and M is the number of categories in Y. Choose $( i , f ,$ x) sets the ith instance of Z as $z _ { i } = x$ with probability f. And $f _ { 1 } ( j )$ and f ( j, m) are de<sup>fi</sup>ned respectively as:

$$
f _ {1} (j) = \frac {F _ {1} \left(X _ {q} = x _ {q j}\right)}{N},\tag{1}
$$

where $F _ { 1 } ( X _ { q } = x _ { q j } )$ is the count for attribute value $x _ { q j } ,$ and

$$
f _ {2} (j, m) = \left\{ \begin{array}{l l} \frac {F _ {2} \big (X _ {q} = z _ {i} , Y = y _ {m} \big)}{F _ {1} \big (X _ {q} = z _ {i} \big)} & \text { if } F _ {1} \big (X _ {q} = z _ {i} \big) \neq 0 \\ 1 / J _ {q} & \text { otherwise } \end{array} \right.,\tag{2}
$$

where $\gamma _ { m }$ is the mth category of the class attribute Y, and $F _ { 2 } ( X _ { q } = z _ { i } ,$ $Y = \gamma _ { m } )$ is the count when $X _ { q } = z _ { i }$ and $Y = \gamma _ { m } .$ At the end of each Choose() iteration, the counts $F _ { 1 }$ and $F _ { 2 }$ are updated and the algorithm will incorporate such feedback.

We should point out that this swapping algorithm aims at preserving the 2nd-order statistics between the class attribute and each QI attribute, but it is not intended to preserve such statistics between a QI attribute and a non-QI (or another QI) attribute. If the released data will also be used to study such relationships, the above algorithm can be modi<sup>fi</sup>ed by adding additional iterations where the class attribute Y is replaced with a concerned QI or non-QI attribute. The relationships among the class and non-QI attributes are completely preserved since their values are not changed by this algorithm. Modi<sup>fi</sup>cations can also be made to preserve higher-order statistics. For instance, if we want to study the joint impact of Age and Blood Type on Test Result in the above example, we can create a compound attribute (called, say, “Age×Blood Type”) that includes all possible combinations of aggregated Age and Blood Type values as its values. The above algorithm can then be applied in terms of Test Result and the compound attribute. The computational cost will increase when attempting to preserve more and higher-order relationships, however.

## 3.3. Genetic algorithm based instance selection

Next, we consider reconstructing the data to achieve k-anonymity. The basic idea is to <sup>fi</sup>rst apply an instance selection technique to <sup>fi</sup>nd a good subset, S, of n records, where $\begin{array} { r } { n = N / k , } \end{array}$ , and then replicate the QI attribute values of each record in S for k−1 times to get a full dataset of size $N ,$ which satis<sup>fi</sup>es k-anonymity.

The instance selection technique we use is based on genetic algorithms (GAs) [15]. The process of natural evolution and genetics has been studied by computing and biology scientists and enormous progress has been made over the past two decades. Genetic algorithms have been applied to a variety of applications, including instance and feature selection [5,18,19], and modeling of decision support systems [27]. Prior research in instance selection has shown that evolutionarybased techniques like GAs outperform traditional methods such as random sampling and nearest neighbour search. Genetic algorithms typically result in higher classi<sup>fi</sup>cation accuracy and smaller subset size [5,18,28].

A genetic algorithm (GA) is a search technique to <sup>fi</sup>nd approximate solutions to optimization and search problems. GAs are a particular class of evolutionary algorithms that use techniques inspired by evolutionary biology such as inheritance, mutation, natural selection, and recombination (or crossover). They are typically implemented as a computer simulation in which a collection of candidate solutions (called chromosomes) to an optimization problem evolves toward better solutions. The evolution starts from a population of random chromosomes and takes place in generations. In each generation, the <sup>fi</sup>tness of the whole population is evaluated, multiple chromosomes are stochastically selected from the current population (based on their <sup>fi</sup>tness), modi<sup>fi</sup>ed (mutated or recombined) to form a new population, which becomes current in the next iteration of the algorithm.

The whole instance selection process is illustrated in Fig. 1. To begin, the original data set is randomly divided into two parts: data set $T ^ { * }$ and test set $\boldsymbol { D } ^ { * } \boldsymbol { T } ^ { * }$ is then sampled with replacement |T<sup>⁎</sup>| times, each taking one instance, to generate the training set T. The instances that are not selected form an independent validation set ${ \boldsymbol { D } } { = } { \boldsymbol { T } } ^ { * } \backslash { \boldsymbol { T } } .$ (Note that D is used to validate the classi<sup>fi</sup>cation models in the process of GA algorithm, while $D ^ { * }$ is used to evaluate the performance of the models built on the <sup>fi</sup>nal GA outputs.)

## 3.3.1. Fitness function

Our objective is to select a subset S out of the training set T such that the classi<sup>fi</sup>cation model ψ(S) induced on this subset is able to maintain adequate prediction accuracy compared to the model ψ(T) induced on the entire training set. We hence de<sup>fi</sup>ne the <sup>fi</sup>tness function as follows:

$$
f (S) = 1 - \hat {e} (\psi (S))\tag{3}
$$

where ê(ψ) is the estimated error rate from the classi<sup>fi</sup>cation model ψ. The estimation is done using a bootstrapping approach. We know that the chance that a particular instance is not selected into the training set T is $\bigl ( 1 - { \textstyle \frac { 1 } { n } } \bigr ) ^ { n } \approx \bar { e } ^ { - 1 } = 0 . 3 6 8$ (where e is the base of natural logarithms, 2.7183). Thus for a reasonably large data set, the test set D will contain about 36.8% of the instances, and the training set T will contain about 63.2% of them. A classi<sup>fi</sup>cation model ψ(S) is built based on a subset and its estimated error rate is evaluated using sets T and D, as below [37]:

$$
\hat {e} (\psi (S)) = 0. 6 3 2 \cdot e _ {D} (\psi (S)) + 0. 3 6 8 \cdot e _ {T} (\psi (S)),\tag{4}
$$

where $e _ { D } ( \psi ( S ) )$ is the error when the model ψ(S) is applied to set D, and $e _ { T } ( \psi ( S ) )$ is the error when it is applied to set T.

The optimization problem is thus to <sup>fi</sup>nd the subset that minimizes Eq. (4). We use a GA implementation to <sup>fi</sup>nd a heuristic solution to this problem. The solution space is de<sup>fi</sup>ned in terms of chromosomes, each of which represents a subset of instances (genes) in T.

## 3.3.2. GA operations and heuristic solution

Let $S _ { h } ^ { ( g ) }$ be the hth subset (chromosome) in the gth GA generation. The GA search starts with an initial population of subsets (chromosomes), ${ \cal S } _ { 1 } ^ { ( 0 ) } , { \cal S } _ { 2 } ^ { ( 0 ) } , . . . , { \cal S } _ { k } ^ { ( 0 ) }$ , which are selected by sampling with replacement from T. Each subset has a size of $V = \bar { \left\lfloor | T | / k \right\rfloor } .$ . Starting with this initial population, the usual GA operations of selection, crossover, and mutation are applied to improve the population. These operations are described as follows.

For the selection, in the gth generation of the GA search, the current population of chromosomes, $S _ { 1 } ^ { ( g ) } , S _ { 2 } ^ { ( g ) } , . . . , S _ { k } ^ { ( g ) }$ <sup>)</sup>, are ranked according to the <sup>fi</sup>tness,

$$
f \left(S _ {[ 1 ]} ^ {(g)}\right) \geq f \left(S _ {[ 2 ]} ^ {(g)}\right) \geq ... \geq f \left(S _ {[ k ]} ^ {(g)}\right).\tag{5}
$$

The (1−c)k <sup>fi</sup>ttest ones are selected into the next generation, where c is the crossover rate. The crossover operator probabilistically selects $c k / 2$ pairs of the chromosomes, randomly chooses two crossover sections of the same number of instances (genes) from two chromosomes, and then swaps the crossover sections between the two chromosomes. In mutation, an instance of a chromosome is chosen with some probability and then replaced by a new instance randomly selected from T.

The GA operations are repeated for a speci<sup>fi</sup>ed number of G generations, resulting in a <sup>fi</sup>nal population of chromosomes, $S _ { [ 1 ] } ^ { ( G ) } , S _ { [ 2 ] } ^ { ( G ) } , . . . ,$ $S _ { [ k ] } ^ { ( G ) }$ , ranked as in Eq. (5) above. The heuristic solution to the best subset is then obtained by selecting n instances that are contained in the top $t ( t \leq k )$ chromosomes in this population; that is,

$$
S ^ {*} = \left\{\mathbf {x} _ {i}: \mathbf {x} _ {i} \in S _ {[ 1 ]} ^ {(G)} \cup S _ {[ 2 ]} ^ {(G)} \dots \cup S _ {[ t ]} ^ {(G)} \text {   and   } | S ^ {*} | = n \right\}.\tag{6}
$$

![](/api/attachments/EBSFERA2/fulltext/images/37b784f2c0f770816f847c36e3b443ee6d086d3ca1907fb3b96a0316603ebffd.jpg)  
Fig. 1. GA-based instance selection.

## 3.4. K-anonymity procedure

Once we have obtained $S ^ { * } ,$ , the <sup>fi</sup>nal step is to create k-anonymity for the original dataset based on $S ^ { * }$ . For each instance x in $S ^ { * } ,$ , this is done by <sup>fi</sup>nding the k−1 nearest instances to $\mathbf { x } _ { i }$ from the original set, and then changing the QI attribute values of these instances to those of $\mathbf { x } _ { i \cdot }$ The pseudo code for this approach is as following:

$$
\text { FOR   } i = 1 \text {   TO   } n \text {   where   } \mathbf {x} _ {i} \in S ^ {*}, \text {   DO   }
$$

• Compute the Euclidean distance between x and each instance in the original set, where numeric data are normalized to [0, 1], and distance between two nominal values is de<sup>fi</sup>ned as zero if they are the same, and one otherwise.

• Find (k − 1) instances having the smallest distance to x<sub>i</sub>.

• Replace the values of the QI attributes for these (k−1) instances with the values of the corresponding QI attributes of x<sub>i</sub>.

END

## 3.5. Computational complexity

The time complexity for the numeric value discretization procedure is of O(N log N) [12]. For nominal value swapping, the computational cost is also low, since only the 1st-order statistics and a part of the 2nd-order statistics are involved. It is clear from the swapping algorithm that the time complexity is of $\begin{array} { r } { O \left( M \sum _ { q } ^ { Q } \right. = \left. 1 J _ { q } \right) } \end{array}$ , where M is the number of categories in the con<sup>fi</sup>dential attribute and $J _ { q }$ is the number of categories in the qth QI attribute. Therefore, $M { \dot { \sum _ { q = 1 } } } J _ { q }$ is the total number of nominal value combinations between the con-<sup>fi</sup>dential attribute and QI attributes (after the numeric value aggregation). This quantity is typically smaller than N in a large datamiming problem.

A GA generation essentially involves building k decision trees, each based on a subset of size $V = \left. \lvert T \rvert / k \right. .$ So, the time complexity of the whole GA procedure is of O(GkV log V), which is smaller than O(GN log N), where the number of generations G can be set by the user to a reasonable level. The convergence of GAs has been analyzed by numerous researchers [10,30,32]. Empirical studies in [18,19,28] have also shown the GA's convergence behaviour in instance selection problems.

Finally, it is clear that the procedure for creating k-anonymized dataset from $S ^ { * }$ is of order $O ( n N ) ,$ , where n and N are the size of $\boldsymbol { \cdot } _ { S } { * }$ and the original dataset, respectively. To sum up, the worst-case time complexity for the entire proposed algorithm is of order O N log N + $\bar { O } \Bigl ( M \bar { \Sigma } _ { q = 1 } ^ { Q } J _ { q } \Bigr ) + O ( G \bar { N } \mathrm { l o g } \bar { N } ) _ { \scriptscriptstyle - } + O ( n N )$ , which should be somewhere between O(N log N) and $O ( N ^ { 2 } )$ . Clearly, this time complexity is comparable to those of major data-mining algorithms, and thus the proposed algorithm is scalable to large data size.

## 4. An illustrative example

In this section, we demonstrate our approach using the example data in Table 1(a). As mentioned earlier, Test Result is the con-<sup>fi</sup>dential attribute in this dataset. Age and Marital Status are the QI attributes, and Blood Pressure and Blood Type are non-QI attributes. In k-anonymity, the QI attributes are masked while the other attributes are unchanged. To illustrate, let k = 3.

Step 1. Aggregate numeric Age values into discretized values (labeled as Age2). As described in Section 3.1, the attribute is aggregated into two values: 28 and 40.

Step 2. Apply the 2nd-order swapping procedure in Section 3.2 to swap the Age2 and Marital Status attribute values. The 2ndorder statistics that we want to preserve as much as possible is the counts for the categorical combinations between the class attribute

Test Result and Age2, and those between Test Result and Marital Status. The data after aggregation and swapping are shown in Table 2. It is easy to verify that the 1st-order statistics are completely preserved. The class-related 2nd-order statistics before and after swapping are given in Table 3. It can be seen that these 2nd order statistics are also completely preserved. However, it is still not dif<sup>fi</sup>cult to <sup>fi</sup>nd the test results for some records in the data. As in Section 2, for example, if Allen wants to identify his 35-year-old, married classmate, he will <sup>fi</sup>nd out two closest records (#2 and #12), which have Age=40 and Marital Status=Married; both of them have a positive test result.

Step 3. Apply GA-based instance selection procedure. The resulting subset of four instances is shown in Table 4, where the ID column shows the record IDs in the original (and swapped) dataset, and the SID column denotes the record IDs in the subset.

Step 4. Perform k-anonymity using partial duplication. Here all of the non-con<sup>fi</sup>dential attributes are used in calculating the Euclidean distance to <sup>fi</sup>nd the k−1 closest instances, while only the QI attribute values (i.e., Age2 and Marital Status) are used for duplication. The k-anonymized data are shown in Table 5, listed in the original order in Part (a) and by anonymized group in Part (b), respectively. It is clear that not only are the QI values anonymized, but also con<sup>fi</sup>dential values are different in each group. The class-related 2ndorder statistics change slightly after the GA and k-anonymity steps, as shown in Table 6.

## 5. Computational experiments and results

A set of numerical experiments was conducted using two realworld datasets. Both datasets were taken from the Machine Learning Repository of the University of California at Irvine [17]. The characteristics of these two datasets are described in Table 7.

The <sup>fi</sup>rst dataset, Diabetes, contains 768 instances of patient information, with nine numeric and nominal attributes, including diagnostic result, age, number of times pregnant, and a few lab test measures. Diagnostic result was considered as the con<sup>fi</sup>dential (class) attribute. The second dataset, German Credit, consists of 21 numerical and nominal attributes, representing credit rating, age, gender with marital status, years of employment, housing type, job type, phone status, foreign worker indicator, and a number of attributes related to the customer's account. Credit rating (nominal) was considered as con<sup>fi</sup>dential (class) attribute. In general, QI attributes are those that are accessible to a potential intruder. Identifying such attributes in our experiment requires more background information about the data than what we have available. Therefore, instead of selecting the QI attributes subjectively, we selected those attributes that appear frequently in the decision tree models as the QI attributes. The idea behind this selection method is that if the proposed approach works well for these QI attributes, then it should be more effective when the attributes not appearing (or appearing infrequently) in the tree models are selected because, in this case, it is easier to anonymize the QI attributes while preserving classi<sup>fi</sup>cation models.

Aggregated and swapped data.

<table><tr><td>ID</td><td>Age2</td><td>Marital status</td><td>Blood ressure</td><td>Blood type</td><td>Test result</td></tr><tr><td>1</td><td>28</td><td>Never married</td><td>75/120</td><td>O</td><td>Negative</td></tr><tr><td>2</td><td>40</td><td>Married</td><td>66/113</td><td>O</td><td>Positive</td></tr><tr><td>3</td><td>40</td><td>Divorced</td><td>74/115</td><td>A</td><td>Negative</td></tr><tr><td>4</td><td>28</td><td>Married</td><td>77/128</td><td>AB</td><td>Negative</td></tr><tr><td>5</td><td>28</td><td>Never married</td><td>72/125</td><td>B</td><td>Negative</td></tr><tr><td>6</td><td>28</td><td>Married</td><td>93/147</td><td>O</td><td>Negative</td></tr><tr><td>7</td><td>28</td><td>Never married</td><td>75/124</td><td>AB</td><td>Positive</td></tr><tr><td>8</td><td>28</td><td>Never married</td><td>95/142</td><td>O</td><td>Negative</td></tr><tr><td>9</td><td>40</td><td>Widow(er)</td><td>88/146</td><td>A</td><td>Positive</td></tr><tr><td>10</td><td>40</td><td>Divorced</td><td>110/155</td><td>O</td><td>Positive</td></tr><tr><td>11</td><td>40</td><td>Divorced</td><td>90/140</td><td>O</td><td>Positive</td></tr><tr><td>12</td><td>40</td><td>Married</td><td>104/145</td><td>B</td><td>Positive</td></tr></table>

Table 3  
The 2nd-order statistics before and after swapping.

<table><tr><td>Age2</td><td>Test result</td><td>Original counts</td><td>Counts after swapping</td><td>Marital status</td><td>Test result</td><td>Original counts</td><td>Counts after swapping</td></tr><tr><td>28</td><td>Negative</td><td>5</td><td>5</td><td>Never married</td><td>Negative</td><td>3</td><td>3</td></tr><tr><td>28</td><td>Positive</td><td>1</td><td>1</td><td>Never married</td><td>Positive</td><td>1</td><td>1</td></tr><tr><td>40</td><td>Negative</td><td>1</td><td>1</td><td>Married</td><td>Negative</td><td>2</td><td>2</td></tr><tr><td>40</td><td>Positive</td><td>5</td><td>5</td><td>Married</td><td>Positive</td><td>2</td><td>2</td></tr><tr><td></td><td></td><td></td><td></td><td>Divorced</td><td>Negative</td><td>1</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>Divorced</td><td>Positive</td><td>2</td><td>2</td></tr><tr><td></td><td></td><td></td><td></td><td>Widow(er)</td><td>Negative</td><td>0</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>Widow(er)</td><td>Positive</td><td>1</td><td>1</td></tr></table>

Existing k-anonymity approaches [31,33], including l-diversity [20], are all based on generalization method, which typically create new higher-level categorical values for QI attributes. Our approach primarily uses swapping and selection methods, which keep categorical values at their original level. Given this difference, it is very dif<sup>fi</sup>cult to <sup>fi</sup>nd disclosure risk and data utility measures that can be used to consistently compare the results of our approach with those of the existing k-anonymity related approaches. In our experiment, therefore, we focus on how disclosure risk and data quality vary with different degree of anonymization using the proposed approach. We also compare the results with and without GA procedure (i.e., using aggregation and swapping only) to examine the impacts of aggregation/swapping and GA instance selection separately.

Subset from GA instance selection.

<table><tr><td>SID</td><td>ID</td><td>Age2</td><td>Marital status</td><td>Blood pressure</td><td>Blood type</td><td>Test result</td></tr><tr><td>a</td><td>1</td><td>28</td><td>Never married</td><td>75/120</td><td>O</td><td>Negative</td></tr><tr><td>b</td><td>4</td><td>28</td><td>Married</td><td>77/128</td><td>AB</td><td>Negative</td></tr><tr><td>c</td><td>12</td><td>40</td><td>Married</td><td>104/145</td><td>B</td><td>Positive</td></tr><tr><td>d</td><td>10</td><td>40</td><td>Divorced</td><td>110/155</td><td>O</td><td>Positive</td></tr></table>

k-anonymized data (k= 3).

<table><tr><td>ID</td><td>Closest instance in GA subset</td><td>Age</td><td>Marital status</td><td>Blood pressure</td><td>Blood type</td><td>Test result</td></tr><tr><td colspan="7">(a) Listed in original order</td></tr><tr><td>1</td><td>a</td><td>28</td><td>Never married</td><td>75/120</td><td>O</td><td>Negative</td></tr><tr><td>2</td><td>a</td><td>28</td><td>Never married</td><td>66/113</td><td>O</td><td>Positive</td></tr><tr><td>3</td><td>a</td><td>28</td><td>Never married</td><td>74/115</td><td>A</td><td>Negative</td></tr><tr><td>4</td><td>b</td><td>28</td><td>Married</td><td>77/128</td><td>AB</td><td>Negative</td></tr><tr><td>5</td><td>b</td><td>28</td><td>Married</td><td>72/125</td><td>B</td><td>Negative</td></tr><tr><td>6</td><td>c</td><td>40</td><td>Married</td><td>93/147</td><td>O</td><td>Negative</td></tr><tr><td>7</td><td>b</td><td>28</td><td>Married</td><td>75/124</td><td>AB</td><td>Positive</td></tr><tr><td>8</td><td>d</td><td>40</td><td>Divorced</td><td>95/142</td><td>O</td><td>Negative</td></tr><tr><td>9</td><td>c</td><td>40</td><td>Married</td><td>88/146</td><td>A</td><td>Positive</td></tr><tr><td>10</td><td>d</td><td>40</td><td>Divorced</td><td>110/155</td><td>O</td><td>Positive</td></tr><tr><td>11</td><td>c</td><td>40</td><td>Married</td><td>90/140</td><td>O</td><td>Positive</td></tr><tr><td>12</td><td>d</td><td>40</td><td>Divorced</td><td>104/145</td><td>B</td><td>Positive</td></tr><tr><td>Group</td><td>ID</td><td>Age</td><td>Marital status</td><td>Blood pressure</td><td>Blood type</td><td>Test result</td></tr><tr><td colspan="7">(b) Listed by anonymized group</td></tr><tr><td rowspan="3">a</td><td>1</td><td>28</td><td>Never married</td><td>75/120</td><td>O</td><td>Negative</td></tr><tr><td>2</td><td>28</td><td>Never married</td><td>66/113</td><td>O</td><td>Positive</td></tr><tr><td>3</td><td>28</td><td>Never married</td><td>74/115</td><td>A</td><td>Negative</td></tr><tr><td rowspan="3">b</td><td>4</td><td>28</td><td>Married</td><td>77/128</td><td>AB</td><td>Negative</td></tr><tr><td>5</td><td>28</td><td>Married</td><td>72/125</td><td>B</td><td>Negative</td></tr><tr><td>7</td><td>28</td><td>Married</td><td>75/124</td><td>AB</td><td>Positive</td></tr><tr><td rowspan="3">c</td><td>6</td><td>40</td><td>Married</td><td>93/147</td><td>O</td><td>Negative</td></tr><tr><td>9</td><td>40</td><td>Married</td><td>88/146</td><td>A</td><td>Positive</td></tr><tr><td>11</td><td>40</td><td>Married</td><td>90/140</td><td>O</td><td>Positive</td></tr><tr><td rowspan="3">d</td><td>8</td><td>40</td><td>Divorced</td><td>95/142</td><td>O</td><td>Negative</td></tr><tr><td>10</td><td>40</td><td>Divorced</td><td>110/155</td><td>O</td><td>Positive</td></tr><tr><td>12</td><td>40</td><td>Divorced</td><td>104/145</td><td>B</td><td>Positive</td></tr></table>

The performance in data utility is evaluated based on classi<sup>fi</sup>cation accuracy. Two popular classi<sup>fi</sup>cation techniques were used in the experiment: the C4.5 decision tree classi<sup>fi</sup>er [25] and support vector machine [35]. Each dataset was randomly divided into two parts: approximately 75% for data set T<sup>⁎</sup>, and 25% for test set $D ^ { * }$ . The data set T<sup>⁎</sup> serves as the “original” set for anonymization (and subsequently for building the classi<sup>fi</sup>cation models), while the test set $D ^ { * }$ were not subject to anonymization. To examine the effectiveness of our method for privacy protection, a disclosure risk measure called record linkage [24] is used. Record linkage measures disclosure risk using the Euclidean distances between records in the masked dataset and those in the original set. It is primarily used for numeric data, which are normalized to [0, 1]. For nominal data, a common practice is to assign a distance of zero if the corresponding attribute values of the two records are the same; otherwise, the distance is one. A record in the masked set is said to be “linked” if the closest record in the original set is indeed the corresponding unmasked record. A record in the masked set is “second closely linked” if the second closest record in the original set is the corresponding one. Then the record linkage measure is de<sup>fi</sup>ned as the percentage of records that are either “linked” or “second closely linked”. We call this measure “RL ratio”.

The anonymity parameter k was varied with three values: k=2, 6, and 10. For each dataset, the proposed method was run ten times. The average results of the classi<sup>fi</sup>cation accuracies, as well as false negative (FN) and false positive (FP) rates, were then reported. In order to examine the convergence of the GA instance selection procedure, we record the classi<sup>fi</sup>cation accuracy for each different number of GA generations. It was observed that accuracies increased steadily until about the 50th generation and then levelled off afterwards. The number of GA generations G is thus set to 50. This convergence rate is very fast and actually faster than that of many other GA applications. Similar situations have also been observed in other instance selection studies using GAs [19].

The 2nd-order statistics before and after k-anonymization.

<table><tr><td>Age</td><td>Test result</td><td>Original counts</td><td>Counts after k-anonymity</td><td>Marital status</td><td>Test result</td><td>Original counts</td><td>Counts after k-anonymity</td></tr><tr><td>28</td><td>Negative</td><td>5</td><td>4</td><td>Never married</td><td>Negative</td><td>3</td><td>2</td></tr><tr><td>28</td><td>Positive</td><td>1</td><td>2</td><td>Never married</td><td>Positive</td><td>1</td><td>1</td></tr><tr><td>40</td><td>Negative</td><td>1</td><td>2</td><td>Married</td><td>Negative</td><td>2</td><td>3</td></tr><tr><td>40</td><td>Positive</td><td>5</td><td>4</td><td>Married</td><td>Positive</td><td>2</td><td>3</td></tr><tr><td></td><td></td><td></td><td></td><td>Divorced</td><td>Negative</td><td>1</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>Divorced</td><td>Positive</td><td>2</td><td>2</td></tr><tr><td></td><td></td><td></td><td></td><td>Widow(er)</td><td>Negative</td><td>0</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>Widow(er)</td><td>Positive</td><td>1</td><td>0</td></tr></table>

Table 7 Test datasets

<table><tr><td>Dataset</td><td>Number of instances</td><td>Number of attributes</td><td>Number of classes</td></tr><tr><td>Diabetes</td><td>768</td><td>9</td><td>2</td></tr><tr><td>German credit</td><td>1000</td><td>21</td><td>2</td></tr></table>

The results of the experiments for classi<sup>fi</sup>cation performance are shown in Table 8. It can be seen that aggregation and swapping preserve the classi<sup>fi</sup>cation accuracies very well. However, the RL ratios after aggregation and swapping are fairly large (particularly for the diabetes data), which indicates high disclosure risks. After applying the GA procedure, both the classi<sup>fi</sup>cation accuracies and the RL ratios decrease. As we can see from Table 8, it is clear that the RL ratios drop much more rapidly than the classi<sup>fi</sup>cation accuracy as k increases. This indicates that the GA-based k-anonymity signi<sup>fi</sup>cantly reduce the disclosure risk while still maintaining reasonable data quality. The FN and FP rates based on the reconstructed data are fairly close to those on the original data but the differences are relatively large compared to the accuracy results. This is understandable because our proposed method is intended to minimize overall classi<sup>fi</sup>cation error rate, not the FN or FP error rates. The results on support vector machine (SVM) indicate that the proposed method works not only for decision trees, but also for other classi<sup>fi</sup>cation techniques.

In addition to classi<sup>fi</sup>cation performance, we have also evaluated our proposed method in terms of simple descriptive statistics. The related performance measures are de<sup>fi</sup>ned separately for numerical and nominal attributes as below:

Let $U _ { 1 } , . . . , U _ { A }$ be the A numeric QI attributes, and $W _ { 1 } , . . . , W _ { B }$ be the B nominal QI attributes; $A + B = Q$ (the total number of QI attributes). The error for numeric simple statistics is measured using average deviation in mean (ADIM), de<sup>fi</sup>ned as:

$$
\mathrm{ADIM} = \frac {1}{A} \sum_ {j = 1} ^ {A} \frac {| \overline {{u}} _ {j} ^ {\prime} - \overline {{u}} _ {j} |}{| \overline {{u}} _ {j} |}
$$

where $\overline { { u _ { j } } }$ and $\overline { { u } } _ { j } ^ { \prime }$ are the mean for numeric attribute $U _ { j } ,$ calculated from the original and reconstructed data respectively. A small ADIM value indicates that the means on the reconstructed data are on average close to those on the original data. Clearly, the smaller the ADIM values, the smaller the information loss in means due to data reconstruction.

The error for simple nominal statistics is measured using average deviation in frequency count (ADIFC), de<sup>fi</sup>ned as:

$$
\text { ADIFC } = \frac {1}{B} \sum_ {j = 1} ^ {B} \left(\frac {1}{C _ {j}} \sum_ {h = 1} ^ {C _ {j}} \frac {\left| w _ {j h} ^ {\prime} - w _ {j h} \right|}{w _ {j h}}\right)
$$

where $w _ { j h }$ is the frequency count for the hth category of nominal attribute $W _ { j }$ in the original data, and $w _ { j h } ^ { \prime }$ is the corresponding count in the reconstructed data; $C _ { j }$ is the number of categories in $W _ { j } .$ Again, a smaller ADIFC value is desirable since it indicates a smaller information loss in frequency count.

Table 9 shows the experimental results for the above statistics. As we can see, the proposed data reconstruction method preserves these statistics reasonably well. It appears that the errors with the numerical attributes are smaller than those with the categorical attributes, particularly when the k values are relatively large. The results from decision tree and SVM methods are fairly consistent. As k increases, the results based on the reconstructed data deviate more from those on the original data. This is understandable since a large k value implies a higher degree of change to the original data.

## 6. Conclusion and discussion

This paper presents a novel instance selection method based on genetic algorithm for identity disclosure protection. We introduce a data reconstruction approach to achieve k-anonymity protection in privacy-preserving data mining. The empirical evaluation results indicate that our proposed approach can lead to signi<sup>fi</sup>cantly improved performance. The insights gained from this study can help business make effective decisions on privacy protection in data mining.

Our work illustrates the usefulness of using instance selection for privacy protection, and the effectiveness of using genetic algorithm for obtaining solutions to the problem. Future research will take into account more complicated situations, and in particular characterize dataset where this approach is most likely to work well. In particular, we will consider how such parameters as number of instances, number of class values, and number of attributes in<sup>fl</sup>uence the performance of the algorithm. We will also explore other alternative distance measures in addition to the Euclidean distance. The basic idea behind our proposed approach can also be applied to numeric prediction problem such as regression. We will investigate approaches to extend our work to numeric prediction problems in future research.

In a classi<sup>fi</sup>cation problem, there is only one class attribute. By designating the class attribute con<sup>fi</sup>dential and non-class attributes non-con<sup>fi</sup>dential, we have implicitly assumed that there is only one con<sup>fi</sup>dential attribute in the data. The proposed method can be extended to handle multiple nominal con<sup>fi</sup>dential attributes. In this situation, we can consider all con<sup>fi</sup>dential attributes together as one compound attribute. Suppose, for instance, the Marital Status attribute in the example in Table 1 is also con<sup>fi</sup>dential. A compound attribute called “Marital Status×Test Result” can be created, which would have eight categories, formed by different combinations of Marital Status and Test Result values. The transformed dataset would have three noncon<sup>fi</sup>dential and one (compound) con<sup>fi</sup>dential attributes. The proposed method can then be applied to this transformed dataset.

Experimental results of classi<sup>fi</sup>cation performance.

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">Treatments</td><td colspan="4">C4.5</td><td colspan="4">SVM</td></tr><tr><td>RL (%)</td><td>Accuracy (%)</td><td>FN (%)</td><td>FP (%)</td><td>RL (%)</td><td>Accuracy (%)</td><td>FN (%)</td><td>FP (%)</td></tr><tr><td rowspan="5">Diabetes</td><td>Original</td><td> $N/A^a$ </td><td>77.78</td><td>10.00</td><td>42.59</td><td> $N/A^a$ </td><td>78.47</td><td>9.70</td><td>62.26</td></tr><tr><td>Aggregate and swap only</td><td>30.51</td><td>74.98</td><td>17.78</td><td>35.19</td><td>30.51</td><td>77.78</td><td>9.70</td><td>66.04</td></tr><tr><td>Aggregate, swap and GA: k=2</td><td>29.77</td><td>73.33</td><td>13.33</td><td>44.44</td><td>30.08</td><td>77.47</td><td>5.97</td><td>79.24</td></tr><tr><td>Aggregate, swap and GA: k=6</td><td>24.72</td><td>71.53</td><td>11.11</td><td>55.56</td><td>23.91</td><td>77.19</td><td>17.91</td><td>52.83</td></tr><tr><td>Aggregate, swap and GA: k=10</td><td>4.86</td><td>69.44</td><td>23.33</td><td>40.74</td><td>7.62</td><td>75.28</td><td>10.44</td><td>73.58</td></tr><tr><td rowspan="5">Credit</td><td>Original</td><td> $N/A^a$ </td><td>75.40</td><td>6.67</td><td>46.30</td><td> $N/A^a$ </td><td>80.75</td><td>10.45</td><td>41.51</td></tr><tr><td>Aggregate and swap only</td><td>8.93</td><td>73.10</td><td>10.00</td><td>42.59</td><td>8.93</td><td>77.01</td><td>13.43</td><td>47.17</td></tr><tr><td>Aggregate, swap and GA: k=2</td><td>5.23</td><td>72.78</td><td>15.56</td><td>35.19</td><td>5.35</td><td>75.19</td><td>8.96</td><td>64.15</td></tr><tr><td>Aggregate, swap and GA: k=6</td><td>1.73</td><td>72.63</td><td>6.67</td><td>51.85</td><td>1.96</td><td>74.76</td><td>14.18</td><td>52.83</td></tr><tr><td>Aggregate, swap and GA: k=10</td><td>1.35</td><td>71.57</td><td>8.89</td><td>51.85</td><td>1.72</td><td>73.32</td><td>10.45</td><td>71.70</td></tr></table>

<sup>a</sup> Theoretically, the RL ratio for the original data is 100%.

Table 9  
Experimental results of simple statistics.

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">Treatments</td><td colspan="2">C4.5</td><td colspan="2">SVM</td></tr><tr><td>ADIM (%)</td><td>ADIFC (%)</td><td>ADIM (%)</td><td>ADIFC (%)</td></tr><tr><td rowspan="4">Diabetes</td><td>Aggregate and swap only</td><td>2.53</td><td>N/Aa</td><td>1.73</td><td>N/Aa</td></tr><tr><td>Aggregate, swap and GA: k=2</td><td>4.82</td><td>N/Aa</td><td>1.93</td><td>N/Aa</td></tr><tr><td>Aggregate, swap and GA: k=6</td><td>8.59</td><td>N/Aa</td><td>12.62</td><td>N/Aa</td></tr><tr><td>Aggregate, swap and GA: k=10</td><td>14.26</td><td>N/Aa</td><td>14.58</td><td>N/Aa</td></tr><tr><td rowspan="4">Credit</td><td>Aggregate and swap only</td><td>2.05</td><td>1.18</td><td>0.66</td><td>0.88</td></tr><tr><td>Aggregate, swap and GA: k=2</td><td>3.07</td><td>1.31</td><td>2.04</td><td>1.17</td></tr><tr><td>Aggregate, swap and GA: k=6</td><td>10.00</td><td>19.38</td><td>13.93</td><td>18.35</td></tr><tr><td>Aggregate, wap and GA: k=10</td><td>14.26</td><td>38.84</td><td>14.58</td><td>36.39</td></tr></table>

<sup>a</sup> All attributes of the diabetes data (except the class attribute) are numeric.

## Acknowledgement

This research is partially supported by funds from the Information Infrastructure Institute (iCube), Center for Information Protection Center, and College of Business at Iowa State University. We would like to thank the editor and three anonymous reviewers for their detailed comments that help improve the paper.

## References

[1] N.R. Adam, J.C. Wortmann, Security-control methods for statistical databases: a comparative study, ACM Computing Surveys 21 (4) (1989) 515–556.

[2] G. Aggarwal, T. Feder, K. Kenthapadi, S. Khuller, R. Panigrahy, D. Thomas, A. Zhu, Achieving anonymity via clustering, Proceedings of the 25th Symposium on Principles of Database Systems (PODS'06), Chicago, IL, 2006, pp. 153–162.

[3] R. Agrawal, R. Srikant, Privacy-preserving data mining, Proceedings of 2000 ACM SIGMOD International Conference on Management of Data Dallas TX 2000, pp. 439–450.

[4] A. Amiri, Dare to share: protecting sensitive knowledge with data sanitization, Decision Support Systems 43 (1) (2007) 181–191.

[5] J.R. Cano, F. Herrera, M. Lozano, Using evolutionary algorithms as instance selection for data reduction in KDD: an experimental study, IEEE Transactions on Evolutionary Computation 7 (6) (2003) 561–575.

[6] H. Chen, Intelligence and security informatics: information systems perspective Decision Support Systems 41 (3) (2006) 555–559.

[7] D.S. Chowdhury, G.T. Duncan, R. Krishnan, S.F. Roehrig, S. Mukherjee, Disclosure detection in multivariate categorical databases: auditing con<sup>fi</sup>dentiality protection through two new matrix operators, Management Science 45 (12) (1999) 1710–1723.

[8] C. Clifton, M. Kantarcioglu, J. Vaidya, X. Lin, M. Zhu, Tools for privacy preserving distributed data mining, SIGKDD Explorations 4 (2) (2002) 38–44

[9] M. Culnan, How did they get my name?: an exploratory investigation of consumer attitudes toward secondary information use, MIS Ouarterly 17 (3) (1993) 341–363

[10] L. Ding, J. Yu, Some theoretical results about the computation time of evolutionary algorithms, Proceedings of the 2005 Conference on Genetic and Evolutionary Computation, Washington, DC, 2005, pp. 1409–1415.

[11] A. Ev<sup>fi</sup>mievski, R. Srikant, R. Agrawal, J. Gehrke, Privacy preserving mining of association rules, Proceedings of 8th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Edmonton, Canada, 2002, pp. 217–228.

[12] U.M. Fayyad, K.B. Irani, On the handling of continuous-valued attributes in decision tree generation, Machine Learning 8 (1992) 87–102.

[13] A. Friedman, A. Schuster, R. Wolff, Providing k-anonymity in data mining International Journal on Very Large Data Bases 17 (2008) 789–804.

[14] R. Gar<sup>fi</sup>nkel, R. Gopal, P. Goes, Privacy protection of binary con<sup>fi</sup>dential data against deterministic, stochastic, and insider threat, Management Science 48 (6) (2002) 749–764.

[15] D.E. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning, Kluwer Academic Publishers, Boston, MA, 1989.

[16] S. Greengard, Privacy: entitlement or illusion? Personnel Journal 75 (5) (1996) 74–88.

[17] S. Hettich, D. Bay, The UCI KDD Archive, University of California, Department of Information and Computer Science, Irvine, CA, 1999, http://kdd.ics.uci.edu.

[18] H. Ishibuchi, T. Nakashima, M. Nii, Genetic-algorithm-based instance selection and feature selection, In: H. Liu, H. Motoda (Eds.), Instance Selection and Construction for Data Mining, Kluwer Academic, Norwell, MA, 2001, pp. 96–112.

[19] X.-B. Li, V.S. Jacob, Adaptive data reduction for large-scale transaction data, European Journal of Operational Research 188 (3) (2008) 910–924.

[20] A. Machanavajjhala, J. Gehrke, D. Kifer, M. Venkitasubramaniam, l-diversity: privacy beyond k-anonymity, Proceedings of the 22nd IEEE International Conference on Data Engineering (ICDE 2006), Atlanta, GA, 2006.

[21] D. Martens, L. Bruynseels, B. Baesens, M. Willekens, J. Vanthienen, Predicting going concern opinion with data mining, Decision Support Systems 45 (4) (2008) 765–777.

[22] S. Menon, S. Sarkar, Minimizing information loss and preserving privacy, Management Science 53 (1) (2007) 102–116.

[23] S. Menon, S. Sarkar, S. Mukherjee, Maximizing accuracy of shared databases when concealing sensitive patterns, Information Systems Research 16 (3) (2005) 256–270.

[24] D. Pagliuca, G. Seri, Some results of individual ranking method on the system of enterprise accounts annual survey, Esprit SDC Project, Deliverable MI-3/D2, 1999.

[25] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Mateo, CA, 1993.

[26] T.S. Raghu, H. Chen, Cyberinfrastructure for homeland security: advances in information sharing, data mining, and collaboration systems, Decision Support Systems 43 (4) (2007) 1321–1323.

[27] J. Rees, G.J. Koehler, Leadership and group search in group decision support systems, Decision Support Systems 30 (1) (2000) 73–82.

[28] C.R. Reeves, D.R. Bush, Using genetic algorithms for training data selection in RBF networks, In: H. Liu, H. Motoda (Eds.), Instance Selection and Construction for Data Mining, Kluwer Academic, Norwell, MA, 2001, pp. 339–356.

[29] S.P. Reiss, Practical data-swapping: the <sup>fi</sup>rst steps, ACM Transactions on Database Systems 9 (1) (1984) 20–37.

[30] G. Rudolph, Convergence analysis of canonical genetic algorithms, IEEE Transactions on Neural Networks 5 (1) (1994) 96–101.

[31] P. Samarati, Protecting respondents' identities in microdata release, IEEE Transactions on Knowledge and Data Engineering 13 (6) (2001) 1010–1027.

[32] J. Suzuki, A Markov chain analysis on simple genetic algorithms, IEEE Transactions on Systems, Man and Cybernetics 25 (4) (1995) 655–659.

[33] L. Sweeney, k-Anonymity: a model for protecting privacy, International Journal on Uncertainty, Fuzziness and Knowledge-based Systems 10 (5) (2002) 557–570.

[34] M. Teltzrow, A. Kobsa, Impacts of user privacy preferences on personalized systems: a comparative study, In: C.M. Karat, J. Blom, J. Karat (Eds.), Designing Personalized User Experiences in eCommerce, Kluwer Academic Publishers, Dordrecht, Netherlands 2004, pp. 315–332.

[35] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer-Verlag, New York, 1995.

[36] V.S. Verykios, A.K. Elmagarmid, E. Bertino, Y. Saygin, E. Dasseni, Association rule hiding, IEEE Transactions on Knowledge and Data Engineering 16 (4) (2004) 434–447.

[37] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques Morgan Kaufmann, San Francisco, CA, 2005.

Dan Zhu is an associate professor in the Department of Logistics, Operations and Management Information Systems at the Iowa State University. She obtained her Ph.D. degree from Carnegie Mellon University. Her current research focuses on developing and applying intelligent and learning technologies to business and management that lies in decision support systems, information security and privacy, and business intelligence. Dr. Zhu’s research has been published in the Decision Support Systems, Proceedings of National Academy of Sciences Information System Research Naval Research Logistics, Annals of Statistics. Annals of Operations Research. Decision Sciences, Omega, Journal of Databases, Journal of Electronic Commerce Research, International Journal of Knowledge Management, Journal of Information and Software Technology, etc.

Xiao-Bai (Bob) Li is an associate professor of management information systems in the Ddepartment of Operations and Manufacturing/Management Information Systems at the University of Massachusetts Lowell Group. His research interests include data mining, information privacy, and information economicsdatabases, and privacy and security issues. His work has appeared or is forthcoming in Decision Support Systems, Information Systems Research, Operations Research, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transactions on Automatic Control, Communications of the ACM, Decision Support Systems, INFORMS Journal on Computing, the European Journal of Operational Research, among others.

Shuning Wu is a Senior Statistical Analyst at ISO Innovative Analytics. He holds a PhD degree in Industrial Engineering from Iowa State University. Dr. Wu’s research is focused on data mining, instance selection and metaheuristic optimization. He is now working on applying the advanced predictive modeling and data mining techniques to insurance industry. He has published in European Journal of Operational Research, Journal of Decision Support System, International Conference on Information Systems, Journal of Tsinghua University and so on.
