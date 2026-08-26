---
otero_id: 8786
otero_key: "J8AD43U9"
title: "A distance function to support optimized selection decisions"
authors: "Arne Løkketangen; David L. Woodruff"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.01.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A distance function to support optimized selection decisions

Arne Løkketangen<sup>a</sup>, David L. Woodruff<sup>b,</sup>\*

<sup>a</sup> Molde College, Britvn. 2, 6400 Molde, Norway

<sup>b</sup> Graduate School of Management, UC Davis, One Shields Avenue, Davis, CA 95616, USA

Received 3 June 2003; received in revised form 8 January 2004; accepted 16 January 2004 Available online 11 March 2004

## Abstract

Decision-makers often want to see a diverse collection of good solutions in addition to a solution that is in some mathematical sense an optimal solution to a problem. The purpose of the objective function is to quantify the notion ‘‘good’’, while the purpose of this paper is to exhibit a suitable function for quantifying the notion ‘‘diverse’’. We focus on the case where important aspects of the solutions are best represented as matrices or sets of vectors, such as when the solution involves selections. We establish a distance function and its connections with related distance functions used in optimization and psychology. A real-world application illustrates its use for decision support. <sup>D</sup> 2004 Elsevier B.V. All rights reserved

Keywords: Solution variety; Solution similarity; Sets of solution; Vectors; Filtration

## 1. Introduction

Optimization problem formulations must be an abstraction from the complexities of the real world. Consequently, decision-makers often want to see a diverse collection of good solutions in addition to a solution that is in some mathematical sense an optimal solution. For example, if the decision-maker has been shown a few trial solution vectors (perhaps including an optimal solution) and there are a few more good solution vectors that could be shown, the next solution to be displayed must be selected based on some criteria. The solution with the second best objective function value may well be extremely similar to one that has already been displayed and hence would waste the time of the decision-maker. It would be better to find a good solution that would diversify the set that has been displayed. The purpose of the objective function is to quantify the notion ‘‘good’’, while the purpose of this paper is to exhibit good dissimilarity functions for quantifying the notion ‘‘diverse’’.

In some settings, well-known families of norms, such as $L _ { k } ,$ can be used or extended to provide the basis for a metric [13]. When the solution vectors, or important portions of them, are binary then Hamming distances or similar metrics are sometimes appropriate. These methods provide metrics or dissimilarity functions in a space of numeric vectors.

In contrast, here, we focus on the case where important aspects of the candidate solutions are best represented as matrices or sets of heterogenous vectors. This is the case, for example, when part or all of the problems is to assign values to binary variables indicating the selection of an object. The objects available for selection have attributes that are important for considering the differences between solutions.

An example of this situation is provided by the effort to develop decision support technology for selection of highway construction projects in Norway. For this problem, there is a set of hundreds of potential highway projects each of which has 50 or 60 attributes that define and describe the project. Many of the attributes are real valued, but some are categorical. We can represent this set of n potential projects each described by p attributes as an $n \times p$ matrix. A solution to the problem of selecting the optimal set of projects can be represented by a binary n-vector where each element indicates whether the corresponding project is included in the solution. A more descriptive solution representation is a matrix containing the attributes of the selected projects. In Section 6, we provide details. This practical example is concerned with multiple criteria optimization (MCO) and illustrates important uses of a distance function.

Readers familiar with the MCO literature will notice this paper presents ideas that are potentially complimentary with filtering, which is often discussed in the context of MCO. Among the many works on the topic of MCO, see, e.g., Refs. [1,10,13]. For continuous optimization problems, the set of undominated solutions can be infinite, so MCO researchers have long suggested that dissimilarity functions or metrics are needed to reduce the number of undominated solutions to be shown. In addition, we note that, in practice, decision-makers can also be interested solutions close to the efficient frontier if they are different enough from those on the frontier. When the problem involves selections, the identification of solutions that are ‘‘different enough’’ in the eyes of the decisions maker can be enhanced by the use of dissimilarity functions that take into account the attributes of the objects selected using functions that we define in this paper.

Our research is quite different from sensitivity analysis. For optimization problems, there is a rich literature concerning the sensitivity of the optimum solution to changes in the problem data even for discrete optimization problems; see, e.g., Ref. [4] or Ref. [12]. Our work augments this by providing means to characterize dissimilarity between solutions. Our work is also different from recent work in the heuristic search literature, which offers some other approaches [2] for generating a varied set of solution vectors.

In order to introduce our notation, we consider the classic selection optimization, namely the knapsack problem:

max cx ðKÞ

subject to

axVb

$$
x \in \{0, 1 \} ^ {n}
$$

where c and a are row vectors of length n given as data and x is a column vector of n variables; the budget b is a scalar provided as data. Generally, though, there are additional n vectors of length p each describing the object that will be selected if the corresponding element of x is one. The values of the corresponding elements of c and a may be included in these vectors but there is usually also a lot of other information about the objects being selected. All of this information is not used to find the solution to the optimization problem, but may be critical if one is to make statements about similarities and differences between solution vectors. So for mathematical programming solutions to the problem, we need only the binary vector representation of solutions while to consider solution variety we need to think of these solutions as representing matrices or sets of vectors of the attributes of the objects selected.

Creation of a distance function in the space of solutions using the vector representation is straightforward. For example, Hamming distances can be used. However, such a metric is unsatisfying because it ignores the nature of the projects that differ. A metric based on the attributes of the objects selected is rendered difficult in part by the fact that the dimension of the matrices of attributes (or the cardinality of sets of attribute vectors) can vary from solution to solution.

Consider a brutally simple example where the problem is to select one or two automobiles from the list given in Table 1. Maybe the knapsack formulation (K) is used to select potential solution vectors or perhaps a more complicated generalization with a nonlinear objective function and logical constraints. The optimization problem is not of interest here. Our interest is in characterizing the similarity between pairs of selections. Suppose the autos have been numbered in the order shown. To remove optimization considerations, suppose further that the following three vectors indicating selection of two autos each have the same, or about the same, objective function value:

Table 1  
A small example of a set hence selections can be made

<table><tr><td>Model</td><td>Doors</td><td>Year</td><td>Original price</td><td>Cost</td></tr><tr><td>Civic</td><td>2</td><td>1988</td><td>8000</td><td>7000</td></tr><tr><td>Civic</td><td>4</td><td>1988</td><td>8300</td><td>7000</td></tr><tr><td>Corolla</td><td>4</td><td>1996</td><td>12,000</td><td>9000</td></tr><tr><td>Cressida</td><td>4</td><td>1981</td><td>19,000</td><td>9000</td></tr><tr><td>Corolla</td><td>2</td><td>1995</td><td>13,000</td><td>9000</td></tr></table>

$$
\begin{array}{l l} x ^ {(1)} = (0, 1, 0, 0, 1) & x ^ {(2)} = (1, 0, 1, 0, 0) \\ x ^ {(3)} = (0, 1, 0, 1, 0) \end{array}
$$

We will provide details in Section 4, but it is easy to see that Hamming distances and $L _ { k }$ metrics will indicate that vector two, $x ^ { ( 2 ) } ,$ , is as far from vector one, $x ^ { ( 1 ) }$ , as it is from vector three, $x ^ { ( 3 ) }$ . However, this does not make intuitive sense given that the attributes of the cars indicated by the first two vectors are very similar, while the third is quite a bit different from the second. The first selects the four-door civic and the two-door corolla, while the second selects the two-door civic and the four door corolla. In all other ways, the selections are very similar. Solution vector three is the only one that includes a cressida, which is older and has a higher initial price in addition to being a different model. This small example will be the subject of sample calculations for our method in Section 5.

In Section 2, we discuss these issues in detail by reviewing some related similarity and distance functions described in the psychology literature. These methods are extended to measure the distance between sets of vectors in Section 3. We briefly contrast our proposal with metrics often proposed for filtration in Section 4. The description in Section 6 of a major real-world implementation affords the opportunity to illustrate application of our distance function for an important problem. The paper closes with some concluding remarks.

## 2. Categorical and set features

The problems of computing similarity and distance are complimentary and the literature is intertwined. We will use the terms similarity and distance function in their broad, intuitive sense and reserve the word metric for those functions $f ( \cdot )$ that obey four properties for all vector, set or matrix triplets $x , y$ and $z \mathrm { : }$

$$
\begin{array}{l} 1. f (x, x) = 0 (\text {   or   at   least   } f (x, x) = f (y, y)), \\ 2. f (x, y) > 0 \text {   if   } x \neq y, \\ 3. f (x, y) = f (y, x) \text {   and } \\ 4. f (x, y) + f (y, z) \geq f (x, z). \end{array}
$$

We will strive to identify distance functions with the first three properties, but will not concern ourselves with the final one, hence our functions are classified as semi-metrics. As an important aside, we note that there is evidence that neither the triangle inequality nor symmetry are needed to create distance functions that correspond to human perceptions about the similarity between bundles of objects (see, e.g., Refs. [3,6]).

We face the problem of comparing sets of vectors that contain categorical and numeric data. In some sense, the numeric data is the easy part since there are many metrics and distance functions for such data. It is the presence of categorical data that causes the difficulty. Insights can be gleaned considering the literature on two related problems: comparing vectors of categorical data and comparing sets of categorical data. This work has been extended to consider comparisons of vectors of sets of data, which is not our problem but it is close enough so that solutions to it are instructive. A unifying proposal for vectors of sets and a nice summary of related work is provided by Ryu and Eick [8].

## 2.1. Distances between vectors of sets

Ryu and Eick [8] consider the problem of comparing vectors where some of the elements are scalars and some are sets. Furthermore, they consider the case where there is a mixture of categorical and numeric data. Their proposal is to compute distances for each vector element separately and then combine them using a weighted sum. We will employ a similar method for the problem of comparing sets of vectors where some of the vector elements are categorical and some are numeric. If we have a dissimilarity function for vector element $j , ~ \delta _ { j } ( \cdot )$ , then we write Ryu and Eick’s proposed distance function as

$$
\frac {\sum_ {j = 1} ^ {p} w _ {j} \delta_ {j} (x _ {j} , y _ {j})}{\sum_ {j = 1} ^ {p} w _ {j}}.
$$

for the dissimilarity between vectors x and y of length $p ,$ assuming that the user has provided an importance weight, $w _ { j } ,$ for each attribute j. This allows for vectors that are mixtures of scalars, categorical values and sets because $\delta _ { j } ( \cdot )$ can be established for each type of vector element. Distance functions for set valued elements are discussed next.

## 2.2. Distances between sets

Tversky [11] proposes general methods for computing the similarity between sets and justifies them with experiments and connections to psychology. He provides distance functions that can be written as differences and as a ratio, which will be our focus. The basic idea is congruent with Jacard’s matching coefficient: one looks at the ratio of the similarities to the possibilities for similarity. For set valued attributes, with sets Y and $Z ,$ an illustrative form of the ratio for similarity given by Tversky is

$$
\frac {| Y \cap Z |}{| Y \cup Z |},
$$

which takes values between zero and one. This is one particular instance of a more general, parameterized ratio-model expression for the similarity of objects with attributes given by two sets Y and $Z ,$ which is

$$
\frac {f (Y \cap Z)}{f (Y \cap Z) + \alpha f (Y - Z) + \beta f (Z - Y)},
$$

where a and $\beta$ are non-negative parameters and $f ( \cdot )$ is a scale function (e.g., the cardinality). The expression $( Y { - } Z )$ refers to the members of set $Y$ that are not members of set $Z .$ The similarity expression takes values on the zero – one interval; one minus the similarity provides a distance function.

## 3. A general method for sets of vectors

Our interest is in finding the distance between sets of vectors, which we also refer to as portfolios. In the Norwegian highway example, each vector gives the attributes of a particular project and a portfolio of projects is a collection of these vectors. We will use $p$ to denote the number of attributes that each project has. To compare two portfolios, we will need to specify a function for computaion of element-wise comparisons. We use this function to build up a generalization of Tversky’s ratio.

For two particular values of project attribute $j ,$ let the function $\delta _ { j } ( \cdot )$ take values on [0,1] corresponding to the dissimilarity between the two attribute values. For categorical attributes, including binary attributes, an appropriate function $\delta _ { j } ( \cdot )$ is an indicator of inequality so it will take on the value zero or one. If any of the vector elements are sets, then a measure such as Tversky’s can be used. For measured attributes, $\delta _ { j } ( \cdot )$ should provide a continuous measure of dissimilarity scaled by the variability as measured across all potential projects or some other set of interest. For example,

$$
\min \left(1, \frac {\left| a _ {j} - b _ {j} \right|}{s _ {j} (\cdot)}\right)
$$

where $s _ { j } ( \cdot )$ is a measure of the dispersion of the values for attribute $j .$ We assume that 0/0 is zero. Possibilities for $s _ { j } ( \cdot )$ include the standard deviation of the values of attribute $j$ for all projects in (or some multiple thereof). If robustness is an issue, then a multiple of the interquartile range can be used. The range can also be used for theoretical purposes.

In the situation where two vectors are being compared, one can use $\delta _ { j } ( \cdot ) _ { \cdot }$ , directly in the function advocated by Ryu and Eick. To compare two sets of vectors, we need some way of combining the information from multiple $\delta _ { j } ( \cdot )$ values to obtain one value for $d _ { j } ( \cdot )$ , which enables us to extend Tversky’s distance function.

Let $n _ { A }$ be the number of projects in a portfolio A. Bear in mind that a portfolio is a set so $n _ { A }$ is the cardinality of A. We (arbitrarily) order the set and introduce the notation $A ^ { i }$ to indicate project i in portfolio A. Hence, $\boldsymbol { A } _ { j } ^ { i }$ is attribute value j for project i in portfolio A.

Using this notation,

$$
g (w; A, B) \equiv \sum_ {i \in \mathcal {I} _ {A - B}} \sum_ {i ^ {\prime} = 1} ^ {n _ {B}} \sum_ {j = 1} ^ {p} w _ {j} \delta_ {j} (A _ {j} ^ {i}, B _ {j} ^ {i ^ {\prime}}) \Bigg / \left(n _ {B} \sum_ {j = 1} ^ {p} w _ {j}\right)
$$

provides a generalization of $n _ { A - B } .$ . Observe that if $p = 1$ and all vector elements are treated as categorical variables $( \mathrm { i . e . , } A$ and B are sets), then g(w; $A , B ) = n _ { A - B } .$ This extends to binary set elements if the range is used to scale d. For more general sets, the function provides a bound, as indicated in Lemma 1.

Lemma 1. For a vector of non-negative weights w of length p and two sets of p-vectors A and B, $n _ { A - B } \geq g ( w ; ~ A , ~ B )$

Proof. Since $\delta _ { j } ( \cdot )$ is maximized by 1, the terms

$$
\sum_ {i ^ {\prime} = 1} ^ {n _ {B}} \sum_ {j = 1} ^ {p} w _ {j} \delta_ {j} (A _ {j} ^ {i}, B _ {j} ^ {i ^ {\prime}}) \Bigg / \left(n _ {B} \sum_ {j = 1} ^ {p} w _ {j}\right)
$$

achieve a maximum at 1. The summation over $\pmb { \mathcal { I } } _ { A - B }$ provides $n _ { A - B }$ of these terms. 5

The numerator in Tversky’s ratio is typically the cardinality of A\B, or $n _ { A \cap B }$ in our notation. We can make use of the fact that for simple sets, $n _ { A \cap B } = n _ { A } -$ $n _ { A - B } = n _ { B } - n _ { B - A }$ . Since, in general, $n _ { A } - g ( w ; A , B ) \neq$ $n _ { B } - g ( w ; B , A )$ , to obtain symmetry we use both in our bounding approximation to $n _ { A \cap B } ,$ namely,

$$
h (w; A, B) \equiv (n _ {A} - g (w; A, B) + n _ {B} - g (w; B, A)) / 2.
$$

As with $g ( \cdot ) , \ h ( w ; \ A , \ B ) = n _ { A \cap B }$ if A and B are simple sets and w is a vector of ones. An immediate consequence of Lemma 1 is Lemma 2.

Lemma 2. For a vector of non-negative weights w of length p and two sets of p-vectors A and B, $n _ { A \cap B } { \leq } h ( w ; A , B )$

This enables extension of Tversky’s similarity ratio to compute dissimilarity between sets of vectors. Let $\pmb { \mathcal { Z } } _ { A }$ be the set of project indexes that are present in A. Define

$$
d (w; A, B) \equiv 1 - \frac {h (w ; A , B)}{h (w ; A , B) + g (w ; A , B) + g (w ; B , A)}\tag{1}
$$

The function $d ( \cdot )$ that we have given offers the advantage over the Tversky ratio that instead of simply using the number of elements in the difference sets, we make use of a $\delta ( \cdot )$ function to find out how different they are. The relationship with the Tversky ratio provides a computationally useful bound that we now describe in the form of a straightforward remark. The two lemmas and the definition

$$
J (A, B) \equiv 1 - \frac {n _ {A \cap B}}{n _ {A \cap B} + n _ {A - B} + n _ {B - A}}
$$

lead immediately to the following remark:

Remark 1. For a vector of non-negative weights w of length p and two sets of p-vectors A and B,

$$
J (A, B) \geq d (w; A, B).
$$

This bound is equal to 1  Jacard’s similarity coefficient, which is defined in Section 4. As an aside, we note that $n _ { A - B } + n _ { B - A }$ is the traditional Hamming distance.

## 4. Contrast with traditional metrics

A simple way to compute the difference between two categorical or discrete vectors is to count mismatches, which is the so-called Hamming distance. This distance function can easily be projected onto the zero–one interval by dividing the distances by the vector length. When the categorical variables are binary and indicate selection, it is sometimes more reasonable to scale by the number of vector elements that are not zero in both vectors. This idea is provided by Jacard’s similarity coefficient:

$$
\frac {n _ {1 1}}{(n - n _ {0 0})}.
$$

In this expression, $n _ { \mathrm { 1 1 } }$ gives the number of attributes that are one in each vector, n gives the number of attributes and $n _ { 0 0 }$ gives the number of attributes that are zero in each vector. The Hamming distance divided by $n { - } n _ { 0 0 }$ is 1  Jacard’s similarity coefficient. Remark 1 provides the connection between our proposal for $d ( \cdot )$ as defined in Eq. (1) and these metrics.

Since weighted $L _ { k }$ -based metrics are so popular for filtration in MCO, it seems worthwhile to contrast $d ( \cdot )$ with them. We will restrict our attention to numerical vectors since the $L _ { k }$ metrics are not usually defined for categorical or set valued variables, which is sensible given that these metrics were always intended for solution vectors that result from mathematical programming problems. For each vector element, $j ,$ let the range of values be given by $r _ { j }$ and let 0/0 be zero. For two vectors x and y and range vector r of length n, define the range weighted $L _ { k }$ distance as

$$
\left\| x - y \right\| _ {r} ^ {k} \equiv \left(\sum_ {j = 1} ^ {n} \left| \frac {x _ {j} - y _ {j}}{r _ {j}} \right| ^ {k}\right) ^ {1 / k}.
$$

Most of the study of metrics in the space of decision vectors has focused on real-valued elements. Since our interest is in solution elements that specify selection, they are binary (or can be transformed to binary). For binary vectors, the properties of the entire class of weighted $L _ { k }$ norms with respect to an ordering of distances can be studied by studying Hamming distances. This is highlighted by wellknown Remark 2, which is an immediate consequence of the definitions.

Remark 2. For a given k and binary vector $\mathbf { X } ,$ the distance to an arbitrary binary vector y of the same dimension, $\left\| \mathbf { X } - \mathbf { y } \right\| _ { r } ^ { k }$ , is a monotone function of the Hamming distance between x and y.

The $L _ { k }$ and Hamming-type norms ignore the characteristics of the items being selected and focus only on the vectors that represent the selections. This is highlighted in the example given in Section 5. Both require that the vectors being compared have the same length, which makes sense when comparing solution vectors, but not when comparing the selections that they imply. Under very special circumstances, the function d() and the Hamming metric will put the same order on distances, but this is generally only possible if the characteristics of the objects in the selection set does not matter.

## 5. Example calculations

In order to illustrate the computations and some of the concepts, consider the very small, hypothetical example where there are five candidate projects as given in Table 1 in Section 1. If a subset of these projects (or ‘‘objects’’) is to be selected using the knapsack formulation (K), then some of these attributes might be part of the data for the optimization problem. For example, the column labeled ‘‘cost’’ might be some or all of the data used for the cost vector, a. However, our interest is not in solving the optimization problem, but in characterizing the dissimilarity between different subsets of these projects. For this purpose, all of the attributes of the projects are potentially useful (although perhaps with varying importance weights).

Call the portfolio that consists of all five of these projects X. Hence, in our notation $X ^ { 4 } =$ =(cressida, 4, 1981, 19,000, 9000) and $X _ { 2 } ^ { 3 } { = } 4$ . Suppose that we are considering three feasible solutions with roughly the same objective function values:

$$
x ^ {(1)} = (0, 1, 0, 0, 1)
$$

$$
x ^ {(2)} = (1, 0, 1, 0, 0)
$$

$$
x ^ {(3)} = (0, 1, 0, 1, 0)
$$

Metrics that consider only the binary solution vectors do not consider this as shown in Table 2. In this table, the Hamming distances are scaled by n so they will be on the range [0; 1]. This has no effect on the ordering of distances, but makes it easier to compare with the values obtained using the Jacard similarity. As noted in Section 1, the attributes of the cars indicated by the first two vectors are very similar, while the third is quite a bit different from the second. However, the vector-only distance functions do not reflect this.

Traditional binary vector difference functions

<table><tr><td colspan="2"> $x^{(1)}, x^{(2)}$ </td><td colspan="2"> $x^{(1)}, x^{(3)}$ </td><td colspan="2"> $x^{(2)}, x^{(3)}$ </td></tr><tr><td>Hamming/n</td><td> $J(\cdot)$ </td><td>Hamming/n</td><td> $J(\cdot)$ </td><td>Hamming/n</td><td> $J(\cdot)$ </td></tr><tr><td>4/5</td><td>4/4</td><td>2/5</td><td>2/3</td><td>4/5</td><td>4/4</td></tr></table>

In order to appreciate the value of d(), it is useful to view the selections that imply, and are implied by, the decision vectors. To solve the optimization problem, the binary representations are sufficient, but to appreciate the differences between solutions, more information about the solutions is useful.

<table><tr><td></td><td>civic</td><td>4</td><td>1988</td><td>8300</td><td>7000</td></tr><tr><td> $x^{(1)} \leftrightarrow$ </td><td>corolla</td><td>2</td><td>1995</td><td>13,000</td><td>9000</td></tr><tr><td></td><td>civic</td><td>2</td><td>1988</td><td>8000</td><td>7000</td></tr><tr><td> $x^{(2)} \leftrightarrow$ </td><td>corolla</td><td>4</td><td>1996</td><td>12,000</td><td>9000</td></tr><tr><td></td><td>civic</td><td>4</td><td>1988</td><td>8300</td><td>7000</td></tr><tr><td> $x^{(3)} \leftrightarrow$ </td><td>cressida</td><td>4</td><td>1981</td><td>19,000</td><td>9000</td></tr></table>

Table 3 shows the results of d() using a weight vector that is all ones and a d() where the two numeric variables are scaled by four standard deviations as measured across all projects, i.e.,

$$
\delta_ {j} (A _ {j} ^ {i}, B _ {j} ^ {i}) = \left\{ \begin{array}{l l} I (A _ {j} ^ {i} \neq B _ {j} ^ {i}), & j = 1, 2 \\ \min \bigg (1, \frac {| A _ {j} ^ {i} - B _ {j} ^ {i} |}{4 \sigma_ {X _ {j}}} \bigg), & j = 3, 4 \end{array} \right.
$$

where $\sigma _ { X _ { i } }$ refers to the standard deviation of the values in column j of the portfolio X and I() is the usual indicator function that takes the value one if its argument is true and zero otherwise. The results are not qualitatively sensitive to the multiple of $\sigma _ { X _ { j } }$ . We use four because that corresponds to plus and minus two standard deviations. We treated the number of doors as a categorical variable.

Set of vectors difference functions: the d function for numeric fields is scaled by four standard deviations as measured across all autos

<table><tr><td>w</td><td> $d(w; x^{(1)}, x^{(2)})$ </td><td> $d(w; x^{(1)}, x^{(3)})$ </td><td> $d(w; x^{(2)}, x^{(3)})$ </td></tr><tr><td>(1,1,1,1,1)</td><td>0.47</td><td>0.44</td><td>0.60</td></tr><tr><td>(1,20,1,1,1)</td><td>0.63</td><td>0.62</td><td>0.81</td></tr><tr><td>(1,1,1,20,1)</td><td>0.32</td><td>0.37</td><td>0.50</td></tr></table>

Table 3 illustrates one drawback of the ratio function: it is non-linear on [0; 1] so the magnitude of differences are difficult to interpret. However, as Tversky and other researchers have noted, numerous studies indicate that functions with this form produce a rank ordering on distances that corresponds to human perception. One implication of the non-linearity is that comparisons between rows in the table are difficult; however, a practitioner would only be interested in within-row comparisons. That is, given a set of importance weights, one would want to know which vectors imply selection sets that are relatively close and which are relatively distant. It is not surprising that d() produces an ordering on the distances that makes sense given the characteristics of the autos selected. In this example, we used solutions that each selected the same number of objects in the interest of simplicity; however, this is not required. This is important in the major example described in Section 6.

## 6. Major example

This example is a recurring problem for NPRA, the Norwegian Public Roads Administration, the governmental body in charge of the main roads in Norway. Every 4 years, they have to select which road development projects to pursue, from a much larger set of worthy projects (details are in Ref. [5]). The potential road development projects can be evaluated on several objectives. For most projects, the potential socioeconomic value can be evaluated, i.e. the overall gain for the society. For many other objectives, it is more difficult to quantify the benefit. This relates to many of the so-called green factors, like esthetics, noise, safety and other measures like geographic spread. Some of these criteria can have a sensible cardinal measure (like the estimated reduction in the number of people subjected to severe noise), while others are strictly ordinal in nature (like esthetics). The problem is then to select a portfolio of road projects, so as to use up the budget while maximizing the socioeconomic value, and maximize the scores in the other objectives as well. The NPRA uses the five objectives listed in Table 4 to select their recommended portfolio. These are somewhat loosely described by the government, and choices with respect to their concrete implementation must be made by the NPRA.

The original practice at the NRPA was to generate a portfolio for each of the objectives one at a time, disregarding the other objectives. These are generated by a greedy process, based on the bang-per-buck ratio of the individual projects. The recommended portfolio was then generated based on these single objective portfolios in a somewhat unclear process. There are several problems with this approach. As the underlying single objective problem is a 0/1 knapsack problem (K), the greedy heuristic can fail to give the optimal solution. Worse is the observation that the projects selected according to each objective separately are somewhat extreme in that they score high on the selected objective and poorly on the others. Projects that are only good, on all or most, objectives, will not be part of the single objective portfolios, and are thus not considered at all for the final recommended portfolio.

The single objective portfolio selection problem is a 0/1 knapsack problem given above as problem (K), which has pseudo-polynomial time complexity. These problems can be solved efficiently using dynamic programming, DP (see, e.g., Ref. [9]). We have adopted Pisinger’s code, minknap.c, to use as a subproblem solver [7].

The multiple objective portfolio selection problem is transformed to a sequence of 0/1 knapsack problems by forming a single objective function coefficient for each candidate project by weighing together the objective function coefficients for the $\kappa = 5$ objectives. Let $\hat { c } _ { i j }$ be the objective function coefficient for project i and objective j. We then form the elements of the vector c for a particular weight vector k using

$$
c _ {i} = \sum_ {j = 1} ^ {\kappa} \lambda_ {j} \hat {c} _ {i j}
$$

where k is required to have the property that $\textstyle \sum _ { j = 1 } ^ { \kappa } \lambda _ { j } = 1$ . By varying k one can explore the efficient frontier, which is the set of solutions that are optimal for various $\lambda$ vectors. Although it is well known that the convex hull generated by varying k will not generate every efficient solution for a discrete optimization problem, it generates more than enough solutions for a decision support system to be used by the NPRA.

In fact, part of the purpose of solving a number of instances generated by different k vectors is to help the DM roughly determine a k vector of interest. Having determined a reasonably value for this vector, a new multi-objective problem is spawned. The value of k is fixed and a search is launched for solutions that satisfy the constraints of problem (K), and minimize an objective function that combines cx and the distance from solutions that have been displayed so far. This is helpful to the DM, because although cx captures some of the objectives of the stakeholders, it does not capture all considerations. Hence, a variety of solutions is desired.

To avoid generating too many solutions, and thus overwhelming the DM, solution generation and filtration are conducted simultaneously to generate an interesting set of solutions for a variety of k values. Our goal in solution generation is to map the solutions on the efficient frontier in the k space. The space is far too large, so we need to proactively select k vectors that will tend to diversify the set of solutions generated. The selective mapping of the efficient frontier is done by partitioning the k space based on the distance function that we have given as d().

Let j be the number of objectives in the MCO. For this example, j = 5. Begin by generating the k-points for each of the single objectives (i.e., one k-value = 1 and the (j  1) others equal to 0), and the corresponding j solutions to the implied knapsack problems. Then form the center point in k space (i.e., the average of the extreme point k values) and the corresponding solution. We now have j + 1 solutions. The center point is said to have the j extreme points as its parents. In order to recursively generate the desired number of solutions, look at the distance, d(), from each point generated to its parents and select the pointparent pair corresponding to the greatest distance. This pair then defines the region to be partitioned.

The NPRA sets the importance weight vector, w, to 1 for approximately 50 of the project attributes. In the data used for this example, there are 1119 projects, with a total cost of 118,371 MNOK (million Norwegian kroners). The corresponding calculated socioeconomic benefit is 76,905 MNOK. In the 4-year period, the available budget is 11,652 MNOK.

As an example the first 10 portfolios generated are shown in Table 5. The headers in the table correspond to the objectives given in Table 4. In a practical setting, somewhere between 25 and 50 portfolios would be generated. The first five portfolios correspond to the five single objective portfolios. They score the highest, as expected, on their own objectives, while scoring rather badly on the other objectives. The spread in the objective values is also quite high. The next five represent solutions for different values of k selected by partitioning the space according to the maximum values of d(). The preprocessing time for generating the attribute statistics pair-wise project distances is about 5 s on a 2.6-MHz Pentium IV. This needs to recalculated whenever the user changes the attribute preference weights, w, or some of the project data are changed. The time to generate 100 portfolios is less than 30 s with most of that time devoted to solving knapsack problems. The speed of computation makes the methods quite suitable for an interactive decision support system.

## 7. Conclusions

Many users of decision support systems want to see a diverse set of good solutions in addition to an optimal solution. While research in the area of optimization algorithms has produced an impressive array of methods, there is a need for new and better distance functions to support creation of decision support tools. This paper provides a distance function for selection problems that takes into account the nature of the objects selected. Traditional metrics such as the Hamming distances and weighted $L _ { k }$ metrics are not appropriate because they must be restricted to a numeric solution vector representation rather than the heterogenous sets of vectors that correspond to the meaningful attributes of the objects. We have described a computable distance function for selection problems and its connections with functions from optimization and psychology.

A major example illustrates one application of such a function. As is the case with many optimized selection problems, the many perceptions of highway project selections cannot be captured in an optimization formulation even when it explicitly includes multiple objectives. Hence, decision-makers want to be presented with a variety of solutions for consideration. It is important that the definition of variety take into account the characteristics of the projects selected, which is done by basing distance functions on sets of vectors composed of the categorical and numeric data describing the selections.

Table 5  
The first 10 portfolios selected

<table><tr><td>Portfolio</td><td>Projects in portfolio</td><td>Socioeconomic</td><td>District</td><td>Safety</td><td>Access.</td><td>Environ.</td></tr><tr><td>1</td><td>201</td><td>51,588</td><td>-100</td><td>418</td><td>152</td><td>698</td></tr><tr><td>2</td><td>434</td><td>23,298</td><td>2182</td><td>144</td><td>640</td><td>56</td></tr><tr><td>3</td><td>286</td><td>29,925</td><td>-465</td><td>895</td><td>30</td><td>1249</td></tr><tr><td>4</td><td>547</td><td>19,746</td><td>1293</td><td>308</td><td>1059</td><td>317</td></tr><tr><td>5</td><td>248</td><td>23,895</td><td>-530</td><td>470</td><td>89</td><td>1970</td></tr><tr><td>6</td><td>237</td><td>51,232</td><td>224</td><td>430</td><td>253</td><td>1075</td></tr><tr><td>7</td><td>338</td><td>46,937</td><td>1079</td><td>425</td><td>480</td><td>1454</td></tr><tr><td>8</td><td>229</td><td>51,356</td><td>113</td><td>435</td><td>204</td><td>1093</td></tr><tr><td>9</td><td>238</td><td>51,231</td><td>233</td><td>430</td><td>255</td><td>1064</td></tr><tr><td>10</td><td>228</td><td>51,364</td><td>97</td><td>435</td><td>197</td><td>1100</td></tr></table>

Many research opportunities remain. A small study would involve adding the parameters a and $\beta$ to the denominator of the function d() to allow control over the relative importance of terms in the denominator. A much more significant undertaking would be the development of other functional forms that can be compared with the function presented here. A further area of research that we intend to pursue is computational issues related to the use of these functions to support the search for a highly varied set of solutions with good objective function values.

## Acknowledgements

This work was partially funded by the Norwegian Ministry of Transport and Communications under the POT program.

## References

[1] M. Ehrgott, X. Gandibleux (Eds.), Multiple Criteria Optimi zation: State of the Art Bibliographic Surveys, Kluwer Academic Publishing, Boston, 2002.

[2] F. Glover, A. Løkketagen, D.L. Woodruff, Scatter search to generate diverse MIP solutions, in: M. Laguna, J.L. Gonzales-Velarde (Eds.), Computing Tools for Modeling Optimization and Simulation, Kluwer Academic Publishing, Boston, 2000, pp. 299– 320.

[3] B. Goertzel, From Complexity to Creativity: Explorations in Evolutionary, Autopoietic, and Cognitive Dynamics, Kluwer Academic Publishing, Dordrecht, 1997.

[4] H.J. Greenberg, An annotated bibliography for post-solution analysis in mixed integer programming and combinatorial optimization, in: D.L. Woodruff (Ed.), Advances in Computational and Stochastic Optimization, Logic Programming, and Heuristic Search, Kluwer Academic Publishing, Boston, MA, 1998, pp. 97 – 148.

[5] A. Løkketangen, J. Odeck, D.L. Woodruff, Prioritering av prosjektporteføljer na˚r noen av konsekvensene ikke lar seg ma˚le i kroner, I program for overordnet transportforskning, POT, Prosjektrapport Møreforskning 0301 (2003) (in Norwegian).

[6] D.L. Medin, R.L. Goldstone, D. Gentner, Respects for similarity, Psychological Review 100 (1993) 254 – 278.

[7] D. Pisinger, A minimal algorithm for the bounded knapsack problem, INFORMS Journal on Computing 12 (2000) 75–84.

[8] T. Ryuand, C.F. Eick, A unified similarity measure for attributes with set or bag of values for database clustering, Proc. Sixth International Workshop on Rough Sets, Data Mining and Granular Computing (RSDMGrC ’98), 1998.

[9] M. Sniedovich, Dynamic Programming, Marcel Dekker, New York, 1991.

[10] R. Steuer, Multiple Criteria Optimization: Theory, Computation and Application, Wiley, New York, 1986.

[11] A. Tversky, Features of similarity, Psychological Review 84 (1977) 327– 352.

[12] H.M. Wagner, Global sensitivity analysis, Operations Research 43 (1995) 948 – 969.

[13] M. Zeleny, Multiple Criteria Decision Making, McGraw-Hill, New York, 1982.

![](/api/attachments/J8AD43U9/fulltext/images/b001194647b5df176f11875a7fdd61bc81033af0151a9064e6e965a147a7c90b.jpg)  
Arne Løkketangen is a professor in informatics/optimization at Molde University College in Molde, Norway. He received his Ph.D. from the University of Bergen in 1995. Løkketangen has published in a wide range of journals, and is on the editorial board of several international journals.

![](/api/attachments/J8AD43U9/fulltext/images/6c0586a46bda6966ad298d1e25e9a09971ab54b3069a89a2dda5208f6435dcb0.jpg)  
David L. Woodruff is Professor of Management in the Graduate School of Management at the University of California, Davis. He received a Ph.D. from Industrial Engineering Department at Northwestern University. He has served in various society and editorial posts, including Chair of the INFORMS Computing Society.
