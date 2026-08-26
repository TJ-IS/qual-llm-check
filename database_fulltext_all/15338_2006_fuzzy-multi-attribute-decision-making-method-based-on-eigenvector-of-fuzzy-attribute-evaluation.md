---
otero_id: 15338
otero_key: "CUV2WJQ5"
title: "Fuzzy multi-attribute decision-making method based on eigenvector of fuzzy attribute evaluation space"
authors: "Xiangbai Gu; Qunxiong Zhu"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.08.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fuzzy multi-attribute decision-making method based on eigenvector of fuzzy attribute evaluation space

Xiangbai Gu<sup>\*</sup>, Qunxiong Zhu

School of Information Science and Technology, Beijing University of Chemical Technology, Beijing 100029, China

Received 15 August 2003; received in revised form 8 August 2004; accepted 8 August 2004 Available online 15 September 2004

## Abstract

For fuzzy multi-attribute decision-making, a fuzzy symmetry matrix, by referring to covariance definition of random variables, is constructed as attribute evaluation space based on fuzzy decision-making matrix. Improving the fuzzy Analytic Hierarchy Process (AHP) method is proposed by using the approximate fuzzy eigenvector of such fuzzy symmetry matrix. This algorithm reflects the dispersed projection of decision information in general. It has better objectivity and resolving power for the decision-making. This algorithm is used for illustration and comparison with other methods. The results are applied in an example to illustrate that this algorithm is more efficient and objective for multi-attribute decision-making application. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Fuzzy eigenvector; Multi-alternative and multi-attribute; Fuzzy AHP; Fuzzy attribute evaluation space

## 1. Introduction

Frequently, real world decision-making problems are ill defined as their objectives and parameters are not precisely known. Many authors have dealt with these obstacles, which are due to lack of precision. But due to the fact that the requirements of the data and the environment are very strict and that many real world problems are fuzzy by nature and not random, the probability applications have not been very satisfactory in a lot of cases. On the other hand, the application of fuzzy set theory in real world decision-making problems has given very good results. Its main feature is that it provides a more flexible framework, where it is possible to redress many of the obstacles satisfactorily even with the lack of precise data.

The traditional system and the fuzzy system are compatible. Recently, Zadeh [20,21] has been promoting <sup>b</sup>soft calculation<sup>Q</sup> and tried to integrate the fuzzy theory with other systems and new technology. They can supplement each other and be comprehensively used. The fuzzy system can directly convert the experience, which is already successful in the exact system, into fuzzy knowledge through the fuzzy number. In addition, it might be converted into fuzzy knowledge through linguistic variants. It widely expands the channel to get fuzzy system knowledge. Meanwhile, the subjective influence of expert knowledge could be reduced and the objectivity of matching between system and knowledge in the fuzzy system is improved to some extent.

There are three principal areas where decision support is useful. (1) Assisting understanding of a new decision domain where expertise has not been developed. (2) Giving support for decisions when experts rarely advise. (3) Modeling the effects of policy changes on decision-making outcomes. In such domains, a mix of imprecise numeric information upon which linguistic variables are defined and purely linguistic variables, for which there is no formal measurement scale, often co-exist. For example, there may be cost information, which is referred to as <sup>d</sup>expensive<sup>T</sup> or <sup>d</sup>cheap<sup>T</sup> by using linguistic terms. On the other hand, environmental impact is often only assessed by using linguistic terms such as <sup>d</sup>beneficial<sup>T</sup> or <sup>d</sup>detrimental<sup>T</sup> as there are no predefined measurement scales.

Under many conditions, crisp data are inadequate to model real-life situations, since human judgments, including preferences, are often vague and cannot be estimated with exact numerical value. A more realistic approach may be to use linguistic assessments instead of numerical values, that is, to suppose that the ratings and weights of the criteria in the problem are assessed by means of linguistic variables. Considering the fuzziness in the decision data and group decision-making process, linguistic variables are used to assess the weights of all criteria and the rating of each alternative with respect to each criterion. We can convert the decision matrix into a fuzzy decision matrix and construct a normalized fuzzy decision matrix once the decision-makers fuzzy ratings have been pooled.

Regarding decision-making problems, the methods of describing attribute variant and objective variant could be quantitative, i.e., linguistic value, or they could be qualitative, i.e., linguistic terms. The data structure can be exact, i.e., rigid or alternatively inexact, i.e., flexible. Most of the decision-making algorithms that adopt fuzzy set theory concentrate on a subjective decision-making algorithm. That is to say, the decision mostly depends on expert knowledge, experience and favoritism [17]. To avoid subjective interference, difference driving weight principle is provided in this paper. The basic principle is that the weight coefficient is the measure of attribute differentiation between the target and other attribute. The weight of the original information should come directly from an objective environment. The relative attribute weight can be determined by the relative attribute’s information.

In order to develop the difference driving fuzzy decision-making method, the paper is organized as follows. In Section 2, we introduce linguistic variable and linguistic terms. In Section 3, the basic concepts of fuzzy numbers and relative operations are introduced. Section 4 presents the improved fuzzy AHP algorithm based on difference driving weight principle. In Section 5, we discuss uncertainty of fuzzy number ranking and in Section 6, the proposed method is illustrated with examples. Finally, some conclusions are highlighted at the end of this paper.

## 2. Linguistic variables and linguistic terms

In everyday use, it is not usual to be able to distinguish clearly the boundaries of a linguistic term so linguistic terms are vague predicate [19]. However, there is usually one value or range of values to which a variable can be applied with complete certainty. A model has been developed to share these features of linguistic terms, and uncertainty of linguistic terms is discussed in literature [18].

Linguistic hedges are words that qualify the meaning of linguistic terms. So far, it has been unnecessary to use hedges to develop sufficiently sensitive decision-making aids. The approach to hedges given by Bouchon-Meunier and Yap [2] is the most consistent with the overall approach taken here as it applies a left or right translation (rather than using intensifiers such as the square of the membership function) to base linguistic terms.

In general, imprecise and incomplete data information could be introduced to decision-making problems. Also the decisions made by the experts rely on their individual competence and are subjective. Therefore, it is more appropriate to present the data by fuzzy numbers instead of crisp numbers.

In many fuzzy multi-attribute decision-making problems, the final scores of alternatives are represented in terms of fuzzy numbers. In order to choose the best alternative, we need a method to establish a crisp total ordering from fuzzy numbers. To carry out the task of comparing fuzzy numbers, many authors have proposed fuzzy ranking methods that yield a totally ordered set or ranking. These methods can be used in a wide range, from the trivial to the complex and from including one fuzzy number attribute to including many fuzzy number attributes. A review and comparison of these existing methods can be found in Refs. [1,5].

Usually, experts express their opinions by means of numerical values (numerical setting). When experts are not able to give exact numerical values to express their opinions, a more realistic alternative option is to use linguistic assessments instead of numerical values [7,8,10]. In such a situation, for each variable in the problem domain, an appropriate linguistic label set is chosen and used by individuals who participate in the decision-making process to express their opinions. This setting is known as the linguistic setting. For a hybrid of exact and fuzzy variants, the trapezoidal fuzzy number can be used to convert an exact variant into a fuzzy variant.

In this paper, the experts’ opinions are described by linguistic terms, which can be expressed in trapezoidal fuzzy numbers. To obtain the consensus of the experts, we adopt fuzzy attribute evaluation space to adjust the fuzzy rating of every expert. A fuzzy symmetrical matrix is constructed by referring to covariance definition of random variables and the aggregate fuzzy numbers can be obtained by the corresponding approximate fuzzy eigenvector. The final results become ranking fuzzy number problems.

## 2.1. Ranking fuzzy numbers procedure

Many methods for ranking fuzzy numbers have been suggested. Each method appears to have some advantages as well as disadvantage [1,5]. In fuzzy multiple criteria decision-making problems, many triangular fuzzy numbers can intuitively be ranked and ordered by drawing their curves. If their ordering cannot be ranked by their figures, we can use other methods to rank fuzzy numbers. In this paper, we emphasize a fuzzy number ranking procedure by a simple method. This procedure can be introduced as follows:

![](/api/attachments/CUV2WJQ5/fulltext/images/eb48d0d3089062cb1839b3dbc7923aaf8a22669ffb56e9e8a529895dfccf4d7a.jpg)  
Fig. 1. The defuzzification value of the trapezoidal fuzzy number.

(1) Intuition ranking method. From membership function curves of fuzzy numbers, many fuzzy numbers can easily be ranked by intuition ranking method. Lee and Li [12] pointed out that human intuition would favour a fuzzy number with the characteristics of higher mean value and at the same time, lower spread.

(2) If its ordering cannot be ranked by the intuition ranking method. We can rank fuzzy numbers by a-cut method [15], fuzzy mean and spread [12], or other methods. In this paper, we use the defuzzification value of the trapezoidal fuzzy number to do the necessary rank orderings.

2.2. The defuzzification value of the trapezoidal fuzzy number

Definition 2.1. For a trapezoidal fuzzy number $A = ( a _ { 1 } , a _ { 2 } , a _ { 3 } , a _ { 4 } )$ , its defuzzification value [3] is defined to be:

$$
c = \left(a _ {1} + a _ {2} + a _ {3} + a _ {4}\right) / 4\tag{1}
$$

From Fig. 1, we can see that if the left area $\Delta a _ { 1 } p a _ { 2 } { + } \square a _ { 2 } p q c$ is equal to the right area 5cqra<sub>3</sub>+ $\Delta a _ { 3 } r a _ { 4 }$ , then $( I ) ( a _ { 2 } - a _ { 1 } ) / 2 + ( c - a _ { 2 } ) ( l ) = ( a _ { 3 } - c ) ( l ) +$ $( 1 ) ( a _ { 4 } - a _ { 3 } ) / 2 { \Rightarrow } c = ( a _ { 1 } + a _ { 2 } + a _ { 3 } + a _ { 4 } ) / 4$ . Therefore, we obtain the defuzzification value of the trapezoidal fuzzy number $c { = } ( a _ { 1 } { + } a _ { 2 } { + } a _ { 2 } { + } a _ { 4 } ) / 4$

## 3. The basic concepts of fuzzy numbers and relative operations

Special cases of fuzzy numbers include crisp real numbers and intervals of real numbers.

Although there are many shapes of fuzzy numbers, the trapezoidal shapes are used most often for representing fuzzy numbers. The following definition describes the membership function of trapezoidal fuzzy numbers and the operations on them.

Definition 3.1. For a trapezoidal fuzzy number $\tilde { A } = ( a _ { 1 } , a _ { 2 } , a _ { 3 } , a _ { 4 } ) , a _ { 1 } < a _ { 2 } < a _ { 3 } < a _ { 4 }$ (if $a _ { 2 } { = } a _ { 3 } , ~ \tilde { A }$ is a triangular fuzzy number), its membership function is

$$
\alpha^ {\tilde {A}} = \left\{ \begin{array}{l l} 0 & x <   a _ {1} \\ (x - a _ {1}) / (a _ {2} - a _ {1}) & a _ {1} \leq x \leq a _ {2} \\ 1 & a _ {2} \leq x \leq a _ {3} \\ (x - a _ {4}) / (a _ {3} - a _ {4}) & a _ {3} \leq x \leq a _ {4} \\ 0 & x > a _ {4} \end{array} \right.\tag{2}
$$

Let $\tilde { A } { = } ( a _ { 1 } , a _ { 2 } , a _ { 3 } , a _ { 4 } )$ and $\tilde { B } { = } ( b _ { 1 } , b _ { 2 } , b _ { 3 } , b _ { 4 } )$ be any two positive trapezoidal fuzzy numbers. Then the operations $\{ + \ - \ \cdot \ | \}$ are defined by [4]:

$$
\begin{array}{c} \tilde {A} (+) \tilde {B} = (a _ {1}, a _ {2}, a _ {3}, a _ {4}) (+) (b _ {1}, b _ {2}, b _ {3}, b _ {4}) \\ = (a _ {1} + b _ {1}, a _ {2} + b _ {2}, a _ {3} + b _ {3}, a _ {4} + b _ {4}), \end{array}
$$

$$
\begin{array}{r l} \tilde {A} (-) \tilde {\boldsymbol {B}} & = (a _ {1}, a _ {2}, a _ {3}, a _ {4}) (-) (b _ {1}, b _ {2}, b _ {3}, b _ {4}) \\ & = (a _ {1} - b _ {1}, a _ {2} - b _ {2}, a _ {3} - b _ {3}, a _ {4} - b _ {4}), \end{array}
$$

$$
\begin{array}{r l} \tilde {A} (\cdot) \tilde {B} & = (a _ {1}, a _ {2}, a _ {3}, a _ {4}) (\cdot) (b _ {1}, b _ {2}, b _ {3}, b _ {4}) \\ & = (a _ {1} b _ {1}, a _ {2} b _ {2}, a _ {3} b _ {3}, a _ {4} b _ {4}) \end{array}
$$

$$
\begin{array}{r l} \tilde {A} (|) \tilde {B} & = (a _ {1}, a _ {2}, a _ {3}, a _ {4}) (|) (b _ {1}, b _ {2}, b _ {3}, b _ {4}) \\ & = (a _ {1} / b _ {4}, a _ {2} / b _ {3}, a _ {3} / b _ {2}, a _ {4} / b _ {1}) \end{array}\tag{3}
$$

## 4. Proposed fuzzy multi-attribute decision-making method

Since not all the attributes have the same importance, the analytic hierarchy process can be used to find weights for the attributes. These attributes can be broken down to give a series of linguistic variables. In applications, up to nine linguistic terms per variable are used and the term sets can be truncated to five or seven linguistic terms for actual applications.

Analysis of the hierarchy process breaks down complicated decision-making problems into several hierarchies through merging quality analysis and quantity analysis. Quantification of subjective judgment is provided for every hierarchy and analysis. The comprehensive decision weights for each alternative are calculated by weight sum.

For the classic multi-attribute decision-making, eigenvectors can be used to determine the weights of attributes (Saaty, 1977). This method can be used for fuzzy multi-attribute decision-making. The problem is how to construct a fuzzy attribute evaluation matrix and calculate the eigenvector. The proposed fuzzy multi-attribute decision-making method will focus on how to develop decision matrix information and define weights of all attributes based on regular $\mathrm { A H P }$ and the multi-attribute eigenvector decisionmaking method. m-dimensional fuzzy evaluation matrix of attribute $C _ { j } ( j { = } 1 , 2 , . . . , m )$ will be constructed by referring to covariance definition of random variables. The eigenvector of fuzzy attribute evaluation matrix are not calculated directly from a fuzzy eigenvector equations but are approximated. These eigenvectors could be adopted as optimize onedimensional space to determine the weight of a multiattribute. It is obvious that actual difference could be calculated by eigenvector of fuzzy attribute evaluation space. n points (or vector) of ${ \tilde { R } } ^ { n }$ (decision matrix) will be projected into one-dimensional space via eigenvector, so that all of these points will be very well dispersed. Finally, the decision-making becomes the fuzzy number ranking.

The detail steps for improved fuzzy AHP method are described as follows.

Step 1: Build up hierarchy structure model. Set $\tilde { A } { = } \{ A _ { 1 } , A _ { 2 } , . . . . , A _ { n } \}$ as alternatives from which decision makers have to choose. This set consists of alternatives hierarchy. Set $\tilde { C } { = } \{ C _ { 1 } , C _ { 2 } , . . . . , C _ { m } \}$ as attributes from which the performance of alternatives is measured. This set consists of attribute hierarchy.

Step 2: Construct decision matrix. For the alternative $A _ { i } \ ( i = 1 , 2 , . . . n ) , \tilde { h } _ { i j } \ \forall i j , i = 1 , 2 , . . . n , j = 1 , 2 , . . . , m$ is rating of alternative $A _ { i }$ with respect to j th $( j = 1 , 2 , \ldots . , m )$ attribute $C _ { j } .$ So the decision matrix can be expressed as $\tilde { \mathbf { H } } = \left( \tilde { h } _ { i j } \right) _ { n m } ,$ where $\tilde { h } _ { i j }$ can be expressed by trapezoidal fuzzy numbers as $\tilde { h } _ { i j } { = } ( a _ { i j } b _ { i j }$ $c _ { i j } \ d _ { i j } ) ( a _ { i j } < b _ { i j } < c _ { i j } < d _ { i j } , \ i = 1 , 2 , . . . n , j = 1 , 2 , . . . , m )$

Definition 4.1. Represent the $\tilde { h } _ { i j } \mathrm { ' s }$ in the fuzzy decision matrix by trapezoidal fuzzy numbers, we obtain

$$
\tilde {\mathbf {H}} = \begin{array}{c} A _ {1} \\ A _ {2} \\ \dots \\ A _ {n} \end{array} \left[ \begin{array}{c c c c} \tilde {\boldsymbol {h}} _ {1 1} & \tilde {\boldsymbol {h}} _ {1 2} & \dots & \tilde {\boldsymbol {h}} _ {1 m} \\ \tilde {\boldsymbol {h}} _ {2 1} & \tilde {\boldsymbol {h}} _ {2 2} & \dots & \tilde {\boldsymbol {h}} _ {2 m} \\ \dots & \dots & \dots & \dots \\ \tilde {\boldsymbol {h}} _ {n 1} & \tilde {\boldsymbol {h}} _ {n 2} & \dots & \tilde {\boldsymbol {h}} _ {n m} \end{array} \right] = \left[ \begin{array}{c c c c} (a _ {1 1} b _ {1 1} c _ {1 1} d _ {1 1}) & (a _ {1 2} b _ {1 2} c _ {1 2} d _ {1 2}) & \dots & (a _ {1 m} b _ {1 m} c _ {1 m} d _ {1 m}) \\ (a _ {2 1} b _ {2 1} c _ {2 1} d _ {2 1}) & (a _ {2 2} b _ {2 2} c _ {2 2} d _ {2 2}) & \dots & (a _ {2 m} b _ {2 m} c _ {2 m} d _ {2 m}) \\ \dots & \dots & \dots & \dots \\ (a _ {n 1} b _ {n 1} c _ {n 1} d _ {n 1}) & (a _ {n 2} b _ {n 2} c _ {n 2} d _ {n 2}) & \dots & (a _ {n m} b _ {n m} c _ {n m} d _ {n m}) \end{array} \right]\tag{4}
$$

Step 3: Construct m-dimensional fuzzy attribute evaluation space. m-dimensional fuzzy attribute $\left[ C _ { j } \ \left( j { = } 1 , 2 , . . \ . , m \right) \right]$ evaluation matrix will be constructed by referring to covariance definition of random variables.

(1) Construct Centrally normalized matrix $\tilde { \Phi } .$ Fuzzy variant standardizing includes type consistency and normalization. Type consistency is preferred to normalization although both are necessary [9]. Detail methods for type consistency are given in literature [13]. The new centrally normalized algorithm suitable for fuzzy sample set is given as follows. The linear scale transformation is used to transform the various attributes’ scale into a comparable scale. Therefore, we can obtain the centrally normalized fuzzy decision matrix denoted by H<sup>˜</sup> .

For formula (4), fuzzy average $\tilde { E } _ { j }$ can be expressed by trapezoidal fuzzy numbers, i.e., $\tilde { E } _ { j } { = } [ a _ { j } ^ { \prime } \ b _ { j } ^ { \prime } \ c _ { j } ^ { \prime } \ d _ { j } ^ { \prime } ]$ . Fuzzy variance $\bar { \tilde { S } } _ { j }$ can be expressed by trapezoidal fuzzy numbers, i.e., $\widetilde { S } { = } [ a _ { j } ^ { \prime \prime } b _ { j } ^ { \prime \prime } \ \overline { { { c } } } _ { j } ^ { \prime \prime } d _ { j } ^ { \prime \prime } ]$ where:

$$
a _ {j} ^ {\prime} = \frac {1}{n} \sum_ {i = 1} ^ {n} a _ {i j} \quad j = 1, 2, \dots m
$$

$$
b _ {j} ^ {\prime} = \frac {1}{n} \sum_ {i = 1} ^ {n} b _ {i j} \quad j = 1, 2, \dots m
$$

$$
c _ {j} ^ {\prime} = \frac {1}{n} \sum_ {i = 1} ^ {n} c _ {i j} \quad j = 1, 2, \dots m
$$

$$
d _ {j} ^ {\prime} = \frac {1}{n} \sum_ {i = 1} ^ {n} d _ {i j} \quad j = 1, 2, \dots m
$$

$$
a _ {j} ^ {\prime \prime} = \left[ \frac {1}{n} \sum_ {i = 1} ^ {n} \left(a _ {i j} - a _ {i} ^ {\prime}\right) ^ {2} \right] ^ {1 / 2} \quad j = 1, 2, \dots m
$$

$$
b _ {j} ^ {\prime \prime} = \left[ \frac {1}{n} \sum_ {i = 1} ^ {n} \left(b _ {i j} - b _ {i} ^ {\prime}\right) ^ {2} \right] ^ {1 / 2} \quad j = 1, 2, \dots m
$$

$$
c _ {j} ^ {\prime \prime} = \left[ \frac {1}{n} \sum_ {i = 1} ^ {n} \left(c _ {i j} - c _ {i} ^ {\prime}\right) ^ {2} \right] ^ {1 / 2} \quad j = 1, 2, \dots m
$$

$$
d _ {j} ^ {\prime \prime} = \left[ \frac {1}{n} \sum_ {i = 1} ^ {n} \left(d _ {i j} - d _ {i} ^ {\prime}\right) ^ {2} \right] ^ {1 / 2} \quad j = 1, 2, \dots m\tag{5}
$$

From formula (5), the centrally normalized algorithm for the trapezoidal fuzzy number as:

$$
\begin{array}{l} \tilde {\phi} _ {i j} = \left[ \frac {a _ {i j} - a _ {j} ^ {\prime}}{d _ {j} ^ {\prime \prime}} \frac {b _ {i j} - b _ {j} ^ {\prime}}{c _ {j} ^ {\prime \prime}} \frac {c _ {i j} - c _ {j} ^ {\prime}}{b _ {j} ^ {\prime \prime}} \frac {d _ {i j} - d _ {j} ^ {\prime}}{a _ {j} ^ {\prime \prime}} \right] \\ = \lfloor \alpha_ {i j} \beta_ {i j} \gamma_ {i j} \delta_ {i j} \rfloor i = 1, 2, \dots n, j = 1, 2, \dots m \\ \text { where } \alpha_ {i j} = \frac {a _ {i j} - a _ {j} ^ {\prime}}{d _ {j} ^ {\prime \prime}}, \beta_ {i j} = \frac {b _ {i j} - b _ {j} ^ {\prime}}{c _ {j} ^ {\prime \prime}}, \\ \gamma_ {i j} = \frac {c _ {i j} - c _ {j} ^ {\prime}}{b _ {j} ^ {\prime \prime}}, \delta_ {i j} = \frac {d _ {i j} - d _ {j} ^ {\prime}}{a _ {j} ^ {\prime \prime}} \end{array}\tag{6}
$$

(2) Positive migration for centrally normalized matrix. For applications in actual decision-making, the weight should, in general, be positive so that the decision could be easily understood. Based on Frobinius theory in linear algebra, we know that the eigenvector related to the maximum eigenvalue of matrix H should be positive when matrix H is positive. By this we mean that all of the elements of H are greater than 0.

If the m-dimensional fuzzy attribute evaluation space is established directly from $\tilde { \phi } _ { i j }$ by referring to

covariance definition, there should exist both zero and negative fuzzy numbers in such a space. Therefore, it is necessary to migrate the coordinate origin for each attribute so that all of elements in m-dimensional evaluation space are positive. Positive migration of the coordinate origin for each attribute is calculated and placed to eliminate the negative fuzzy numbers and small positive number e is used to eliminate zero for the fuzzy centrally normalized matrix.

Set $\tau _ { j } = \operatorname * { m i n } _ { i = 1 } { \sim } _ { n } \alpha _ { i j } , j = 1 , 2 , \ldots m .$ , then we can obtain $\tilde { r } _ { i j }$ as:

$$
\left\{ \begin{array}{l} \tilde {r} _ {i j} = \tilde {\varphi} _ {i j} = \lfloor \alpha_ {i j} \beta_ {i j} \gamma_ {i j} \delta_ {i j} \rfloor   i f \tau_ {j}   > 0 i = 1, 2, \ldots n; j = 1, 2, \ldots m. \\ \tilde {r} _ {i j} = \lfloor \alpha_ {i j} - \tau_ {j} + \varepsilon \beta_ {i j} - \tau_ {j} + \varepsilon \gamma_ {i j} - \tau_ {j} + \varepsilon \delta_ {i j} - \tau_ {j} + \varepsilon \rfloor   i f \tau_ {j}   \leq 0 i = 1, 2, \ldots n; j = 1, 2, \ldots m. \end{array} \right.
$$

The positive fuzzy centralization decision matrix $\tilde { \mathbf { R } } _ { n m }$ can be expressed as:

$$
\tilde {\mathbf {R}} _ {n m} = \left[ \begin{array}{c c c c} \tilde {r} _ {1 1} & \tilde {r} _ {1 2} & \ldots & \tilde {r} _ {1 m} \\ \tilde {r} _ {2 1} & \tilde {r} _ {2 2} & \ldots & \tilde {r} _ {2 m} \\ \ldots & \ldots & \ldots & \ldots \\ \tilde {r} _ {n 1} & \tilde {r} _ {n 2} & \ldots & \tilde {r} _ {n m} \end{array} \right]\tag{7}
$$

(3) Construct m-dimensional fuzzy attribute evaluation matrix. Referring to covariance matrix definition, the m-dimensional fuzzy attribute evaluation space can be established based on formula (7).

Theorem 4.1. For positive fuzzy centralization decision matrix $\tilde { \mathbf { R } } _ { n m }$ , let $\mathbf { C } \tilde { \mathbf { O } } \mathbf { R } { = } \tilde { \mathbf { R } } ^ { \mathrm { T } } \tilde { \mathbf { R } }$ , then CO<sup>˜</sup> R is fuzzy symmetry matrix.

Proof. From formula (7), CO<sup>˜</sup> R can be expressed as:

$$
\begin{array}{l} \mathbf {C O R} = \tilde {\mathbf {R}} ^ {\mathrm{T}} \tilde {\mathbf {R}} = \left[ \begin{array}{c c c c} \tilde {\boldsymbol {r}} _ {1 1} & \tilde {\boldsymbol {r}} _ {1 2} & \dots & \tilde {\boldsymbol {r}} _ {1 m} \\ \tilde {\boldsymbol {r}} _ {2 1} & \tilde {\boldsymbol {r}} _ {2 2} & \dots & \tilde {\boldsymbol {r}} _ {2 m} \\ \dots & \dots & \dots & \dots \\ \tilde {\boldsymbol {r}} _ {n 1} & \tilde {\boldsymbol {r}} _ {n 2} & \dots & \tilde {\boldsymbol {r}} _ {n m} \end{array} \right] ^ {T} \left[ \begin{array}{c c c c} \tilde {\boldsymbol {r}} _ {1 1} & \tilde {\boldsymbol {r}} _ {1 2} & \dots & \tilde {\boldsymbol {r}} _ {1 m} \\ \tilde {\boldsymbol {r}} _ {2 1} & \tilde {\boldsymbol {r}} _ {2 2} & \dots & \widetilde {\boldsymbol {r}} _ {2 m} \\ \dots & \dots & \dots & \dots \\ \tilde {\boldsymbol {r}} _ {n 1} & \tilde {\boldsymbol {r}} _ {n 2} & \dots & \tilde {\boldsymbol {r}} _ {n m} \end{array} \right] \\ = \left[ \begin{array}{c c c c} \sum_ {k = 1} ^ {n} \tilde {\boldsymbol {r}} _ {k 1} \tilde {\boldsymbol {r}} _ {k 1} & \sum_ {k = 1} ^ {n} \tilde {\boldsymbol {r}} _ {k 1} \tilde {\boldsymbol {r}} _ {k 2} & \dots & \sum_ {k = 1} ^ {n} \tilde {\boldsymbol {r}} _ {k 1} \tilde {\boldsymbol {r}} _ {k m} \\ \sum_ {k = 1} ^ {n} \tilde {\boldsymbol {r}} _ {k 2} \tilde {\boldsymbol {r}} _ {k 1} & \sum_ {k = 1} ^ {n} \tilde {\boldsymbol {r}} _ {k 2} \tilde {\boldsymbol {r}} _ {k 2} & \dots & \sum_ {k = 1} ^ {n} \tilde {\boldsymbol {r}} _ {k 2} \tilde {\boldsymbol {r}} _ {k m} \\ \dots & \dots & \dots & \dots \\ \sum_ {k = 1} ^ {n} \tilde {\boldsymbol {r}} _ {k m} \tilde {\boldsymbol {r}} _ {k 1} & \sum_ {k = 1} ^ {n} \tilde {\boldsymbol {r}} _ {k m} \tilde {\boldsymbol {r}} _ {k 2} & \dots & \sum_ {k = 1} ^ {n} \tilde {\boldsymbol {r}} _ {k m} \tilde {\boldsymbol {r}} _ {k m} \end{array} \right] \end{array}
$$

For the positive fuzzy numbers $\tilde { A }$ and ${ \tilde { B } } ,$ from formula (3), following formula (9) can be obtained:

$$
\tilde {A} + \tilde {B} = \tilde {B} + \tilde {A}
$$

$$
\tilde {A} \tilde {B} = \tilde {B} \tilde {A}\tag{9}
$$

ð8Þ

$\cdot \tilde { r } _ { i j }$ is positive fuzzy number, $\therefore \textstyle \sum _ { k = 1 } ^ { n } { \tilde { r } } _ { k i } { \tilde { r } } _ { k j }$ is positive fuzzy number, where $i { = } 1 , 2 , . . . . , m$ $j { = } 1 , 2 , . . . . , m$

Based on formula (9), $\begin{array} { r } { \sum _ { k = 1 } ^ { n } \tilde { r } _ { k i } \tilde { r } _ { k j } = \sum _ { k = 1 } ^ { n } \tilde { r } _ { k j } \tilde { r } _ { k i } , } \end{array}$ where $i { = } 1 , 2 , . . . , m , j { = } 1 , 2 , . . . , m$ . so CO<sup>˜</sup> R is positive fuzzy symmetry matrix.

m-dimensional fuzzy attribute $\left[ C _ { j } \ ( j { = } 1 , 2 , \ldots . . , m ) \right]$ evaluation matrix would be constructed by the above CO<sup>˜</sup> R. We can ensure that all of the weights of the eigenvector related to the maximum eigenvalue of m-dimensional positive fuzzy symmetry matrix, could be positive by referring to Frobinius theory.

Step 4: Eigenvector of m-dimensional fuzzy attribute evaluation space. The eigenvector of CO<sup>˜</sup> R is not calculated directly from a fuzzy eigenvector equation but is approximated. Approximated eigenvector of m-dimensional fuzzy evaluation space CO<sup>˜</sup> R can be calculated by product and root method (geometry average method) [9]. This eigenvector could be adopted as a disperse projection factor of such m-dimensional fuzzy attribute evaluation matrix in the proposed method. Therefore, importance of attribute-related alternatives could be ordered objectively based on this eigenvector.

Definition 4.2. Fuzzy eigenvector of fuzzy symmetry matrix with m rank CO<sup>˜</sup> R can be obtained by product and root method (geometry average method) as

$$
\tilde {W} _ {i} = \left(\frac {\alpha_ {i}}{\delta} \frac {\beta_ {i}}{\gamma} \frac {\gamma_ {i}}{\beta} \frac {\delta_ {i}}{\alpha}\right) i = 1, 2, \dots , m\tag{10}
$$

where

$$
\begin{array}{l} \alpha_ {i} = \left(\prod_ {j = 1} ^ {m} \alpha_ {i j}\right) ^ {\frac {1}{m}} i = 1, 2, \dots , m \quad \alpha = \sum_ {k = 1} ^ {m} \alpha_ {k} \\ \beta_ {i} = \left(\prod_ {j = 1} ^ {m} \beta_ {i j}\right) ^ {\frac {1}{m}} i = 1, 2, \dots , m \quad \beta = \sum_ {k = 1} ^ {m} \beta_ {k} \\ \gamma_ {i} = \left(\prod_ {j = 1} ^ {m} \gamma_ {i j}\right) ^ {\frac {1}{m}} i = 1, 2, \dots , m \quad \gamma = \sum_ {k = 1} ^ {m} \gamma_ {k} \\ \delta_ {i} = \left(\prod_ {j = 1} ^ {m} \delta_ {i j}\right) ^ {\frac {1}{m}} i = 1, 2,.., m \quad \delta = \sum_ {k = 1} ^ {m} \delta_ {k} \end{array}
$$

Eigenvector $\tilde { W } _ { i }$ of m-dimensional fuzzy attribute evaluation space can be calculated by Definition 4.2. Such a $\tilde { W } _ { i }$ has not embodied the relative importance of attribute $C _ { i }$ but it does represent the maximum disperse degree of project factor for $\{ \tilde { h } _ { i j } \}$ overall. So this $\tilde { W } _ { i }$ can be selected as the attribute’s weight for improved fuzzy AHP algorithm.

Step 5: Comprehensive weights of alternatives for all attributes. Comprehensive weights of alternatives for all attributes can be derived by projection nvectors to such one-dimensional space. The decision judgment value $\tilde { W } ( A )$ can be calculated by using $\tilde { W } _ { i }$ and formula (4):

$$
\begin{array}{l} \tilde {W} (A) = \tilde {\mathbf {H}} (\bullet) \tilde {W} ^ {\mathrm{T}} = \left[ \begin{array}{c c c c} \tilde {h} _ {1 1} & \tilde {h} _ {1 2} & \dots & \tilde {h} _ {1 m} \\ \tilde {h} _ {2 1} & \tilde {h} _ {2 2} & \dots & \tilde {h} _ {2 m} \\ \vdots & \vdots & \dots & \vdots \\ \tilde {h} _ {n 1} & \tilde {h} _ {n 2} & \dots & \tilde {h} _ {n m} \end{array} \right] \left[ \begin{array}{c} \tilde {W} _ {1} \\ \tilde {W} _ {2} \\ \vdots \\ \tilde {W} _ {m} \end{array} \right] \\ = \left[ \begin{array}{c c c c c} (a _ {1 1} b _ {1 1} c _ {1 1} d _ {1 1}) & (a _ {1 2} b _ {1 2} c _ {1 2} d _ {1 2}) & \dots & (a _ {1 m} b _ {1 m} c _ {1 m} d _ {1 m}) \\ (a _ {2 1} b _ {2 1} c _ {2 1} d _ {2 1}) & (a _ {2 2} b _ {2 2} c _ {2 2} d _ {2 2}) & \dots & (a _ {2 m} b _ {2 m} c _ {2 m} d _ {2 m}) \\ \dots & \dots & \dots & \dots \\ (a _ {n 1} b _ {n 1} c _ {n 1} d _ {n 1}) & (a _ {n 2} b _ {n 2} c _ {n 2} d _ {n 2}) & \dots & (a _ {n m} b _ {n m} c _ {n m} d _ {n m}) \end{array} \right] \left[ \begin{array}{c} \tilde {W} _ {1} \\ \tilde {W} _ {2} \\ \dots \\ \tilde {W} _ {m} \end{array} \right] \end{array}\tag{11}
$$

Step 6: Comprehensive ranking. Definition 2.1 can be used for comprehensive weights of alternatives for all attribute ranking. On the other hand, fuzzy variant ranking methods provided in literature [6,11,14] can also be adopted for such comprehensive ranking.

## 5. Uncertainty analysis

Although improved fuzzy AHP algorithm based on fuzzy eigenvector of fuzzy attribute evaluation space can keep external sequence regarding mainstream ranking, it could not keep sequence for branch alternatives, which are not very different. For such a case, the uncertainty of fuzzy number ranking must be considered.

![](/api/attachments/CUV2WJQ5/fulltext/images/d0e6fa0c06e292bb6c054a42ed14535a7ad1e88b3465fe778bdd3a351dd443cf.jpg)  
Fig. 2. Four of five possible fuzzy sets for uncertainty analysis.

If two or more fuzzy sets have intersections then this indicates that there is some uncertainty about the most appropriate course of action. The uncertainty increases as the size of the intersection increases. There are broadly five possible outcomes, four of which are illustrated in Fig. 2. For the sake of clarity, only two fuzzy sets are shown. In these figures, $\tilde { A }$ is the fuzzy set representing alternative $A _ { i } ,$ and $\tilde { B }$ is the fuzzy set representing alternative $A _ { j } .$ The support and the kernel of the fuzzy set are denoted supp and ker respectively and it is assumed in cases 1–4 that max(ker(A<sup>˜</sup>))max(ker(B<sup>˜</sup> )) [18].

(1) For case 1 where: supp(A<sup>˜</sup>)\supp(B<sup>˜</sup> )=% and, supp(A<sup>˜</sup> )\ker(B<sup>˜</sup> )=% and, ker(A<sup>˜</sup> )\ker(B<sup>˜</sup> )=%, where alternative $A _ { j }$ is more strongly preferred than alternative $A _ { i } ,$ the decision-maker would not usually hesitate to make this decision and might describe it as self-evident.

(2) For case 2 where: supp(A<sup>˜</sup>)\supp(B<sup>˜</sup> )p% and, supp(A<sup>˜</sup> )\ker(B<sup>˜</sup> )=% and, ker(A<sup>˜</sup> )\ker(B<sup>˜</sup> )=%, where alternative $A _ { j }$ is preferred, the decisionmaker would usually make this decision without much difficulty but it would not be self-evident.

(3) For case 3 where: supp(A<sup>˜</sup>)\supp(B<sup>˜</sup> )p% and, supp(A<sup>˜</sup> )\ker(B<sup>˜</sup> )p% and, ker(A<sup>˜</sup> )\ker(B<sup>˜</sup> )=%, where alternative $A _ { j }$ is marginally preferred, the decision-maker would be hesitant in making this decision and would make it with some difficulty. It is likely that they would want to review the evidence before committing themselves and might make the decision reluctantly.

(4) For case 4 where: supp(A<sup>˜</sup>)\supp(B<sup>˜</sup> )p% and, supp(A<sup>˜</sup> )\ker(B<sup>˜</sup> )p% and, ker(A<sup>˜</sup> )\ker(B<sup>˜</sup> )p%, where alternative $A _ { j }$ is highly marginal at best, the decision-maker might well consider it advisable to apply another test or rule (assuming one is available) before making a decision and would be very uncertain as to the best way to proceed.

(5) Either ker(A<sup>˜</sup> )<sup>K</sup>ker(B<sup>˜</sup> ) or ker(A<sup>˜</sup> )<sup>L</sup>ker(B<sup>˜</sup> ), where it is not possible to decide which alternative is the most appropriate decision on the basis of the evidence, these are the cases where the decision-maker would certainly consider it advisable to apply another test or rule (assuming one is available) before making a decision.

If the result of uncertainty analysis indicates that further tests and rules are necessary for this algorithm, fuzzy consistent decision matrix [16] can be adopted to improve intelligibility and reasonability for decision-making in the actual application.

## 6. Applications

The theoretical approach outlined in Section 4 has been applied to the airplane purchase example [13]. For the alternative and attribute relationship, see Table 1 (Ref. [13], p. 190).

Table 1  
Airplane procurement alternative and attribute relationship

<table><tr><td>Attribute alternative</td><td>Maximum speed (Mach)</td><td>Cruise radial (Mile)</td><td>Maximum load (Pound)</td><td>Price ($×106)</td><td>Reliabilitya</td><td>Maintainabilitya</td></tr><tr><td>1</td><td>2.0</td><td>1500</td><td>20,000</td><td>5.5</td><td>Normal (0.4, 0.5, 0.5, 0.6)</td><td>High (0.8, 0.9, 0.9, 1)</td></tr><tr><td>2</td><td>2.5</td><td>2700</td><td>18,000</td><td>6.5</td><td>Low (0.2, 0.3, 0.3, 0.4)</td><td>Normal (0.4, 0.5, 0.5, 0.6)</td></tr><tr><td>3</td><td>1.8</td><td>2000</td><td>21,000</td><td>4.5</td><td>High (0.6, 0.7, 0.7, 0.8)</td><td>Very High (0.6, 0.7, 0.7, 0.8)</td></tr><tr><td>4</td><td>2.2</td><td>1800</td><td>20,000</td><td>5.0</td><td>Normal (0.4, 0.5, 0.5, 0.6)</td><td>Normal (0.4, 0.5, 0.5, 0.6)</td></tr></table>

<sup>a</sup> To compare with other methods, the original triangle fuzzy number is directly converted into a trapezoidal fuzzy number.

Step 1: Build up hierarchy structure. $A _ { 1 } , A _ { 2 } , A _ { 3 } , A _ { 4 }$ are four selectable airplane alternatives; they form the alternative hierarchy. Maximum speed $( C _ { 1 } ) _ { : }$ Cruise radial $( C _ { 2 } )$ , maximum load $( C _ { 3 } ) _ { : }$ , price $( C _ { 4 } ) ,$ reliability $( C _ { 5 } )$ and maintainability $( C _ { 6 } )$ are six attributes; they form the attribute hierarchy.

Step 2: Construct decision matrix. Normalized decision matrix H<sup>˜</sup> is:

<table><tr><td> $\tilde{\mathbf{H}} = \left[ \begin{array}{llll} (0.8\ 0.8\ 0.8\ 0.8) & (0.55\ 0.55\ 0.55\ 0.55) & (0.95\ 0.95\ 0.95\ 0.95) \\ (1\ 1\ 1\ 1) & (1\ 1\ 1\ 1) & (0.86\ 0.86\ 0.86\ 0.86) \\ (0.72\ 0.72\ 0.72\ 0.72) & (0.74\ 0.74\ 0.74\ 0.74) & (1\ 1\ 1\ 1) \\ (0.88\ 0.88\ 0.88\ 0.88) & (0.67\ 0.67\ 0.67\ 0.67) & (0.95\ 0.95\ 0.95\ 0.95) \\ (0.82\ 0.82\ 0.82\ 0.82) & (0.50\ 0.71\ 0.71\ 1) & (0.8\ 1\ 1\ 1) \\ (0.69\ 0.69\ 0.69\ 0.69) & (0.25\ 0.43\ 0.43\ 0.67) & (0.4\ 0.56\ 0.56\ 0.75) \\ (1\ 1\ 1\ 1) & (0.75\ 1\ 1\ 1) & (0.6\ 0.78\ 0.78\ 1) \\ (0.9\ 0.9\ 0.9\ 0.9) & (0.50\ 0.71\ 0.71\ 1) & (0.4\ 0.56\ 0.56\ 0.75) \end{array} \right]$ </td></tr></table>

Step 3: Construct 6-dimensional fuzzy attribute evaluation space.

(1) Construct centrally normalized matrix $\tilde { \Phi }$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\tilde{\phi} = \left[ \begin{array}{lllll}(-0.4843 - 0.4843 - 0.4843 - 0.4843) &amp; (-1.1531 - 1.1531 - 1.1531 - 1.1531) &amp; (0.1980 0.1980 0.1980 0.1980)\\ (1.4501 1.4501 1.4501 1.4501) &amp; (1.5779 1.5779 1.5779 1.5779) &amp; (-1.5842 - 1.5842 - 1.5842 - 1.5842)\\ (-1.2568 - 1.2568 - 1.2568 - 1.2568) &amp; (0.0000 0.0000 0.0000 0.0000) &amp; (1.1882 1.1882 1.1882 1.1882)\\ (0.2900 0.2900 0.2900 0.2900) &amp; (-0.4248 - 0.4248 - 0.4248 - 0.4248) &amp; (0.1980 0.1980 0.1980 0.1980)\\ (-0.2865 - 0.2865 - 0.2865 - 0.2865) &amp; (-1.8780 - 0.0124 - 0.0124 1.8929) &amp; (-0.5025 1.5076 1.5076 1.7721)\\ (-1.4325 - 1.4325 - 1.4325 - 1.4325) &amp; (-2.9827 - 1.4017 - 1.4017 0.6245) &amp; (-2.5126 - 0.9045 - 0.9045 0.7297)\\ (1.3002 1.3002 1.3002 1.3002) &amp; (-0.7733 1.4265 1.4265 1.8929) &amp; (-1.5076 0.3015 0.3015 1.7721)\\ (0.4187 0.4187 0.4187 0.4187) &amp; (-1.8780 - 0.0124 - 0.0124 1.8929) &amp; (-2.5126 - 0.9045 - 0.9045 0.7297) \end{array} \right]$
</div>

(2) Positive migration for centrally normalized matrix (E=0.01)

<table><tr><td> $\tilde{\mathbf{R}} = \left[ \begin{array}{lllllll} (0.7843 & 0.7843 & 0.7843 & 0.7843) & (0.0100 & 0.0100 & 0.0100 & 0.0100) & (1.7923 & 1.7923 & 1.7923 & 1.7923) \\ (2.7169 & 2.7169 & 2.7169 & 2.7169) & (2.7410 & 2.7410 & 2.7410 & 2.7410) & (0.0100 & 0.0100 & 0.0100 & 0.0100) \\ (0.0100 & 0.0100 & 0.0100 & 0.0100) & (1.1631 & 1.1631 & 1.1631 & 1.1631) & (2.7824 & 2.7824 & 2.7824 & 2.7824) \\ (1.5568 & 1.5568 & 1.5568 & 1.5568) & (0.7383 & 0.7383 & 0.7383 & 0.7383) & (1.7923 & 1.7923 & 1.7923 & 1.7923) \\ (1.1560 & 1.1560 & 1.1560 & 1.1560) & (1.1147 & 2.9803 & 2.9803 & 4.8856) & (2.0201 & 4.0302 & 4.0302 & 4.2947) \\ (0.0100 & 0.0100 & 0.0100 & 0.0100) & (0.0100 & 1.5910 & 1.5910 & 3.6172) & (0.0100 & 1.6181 & 1.6181 & 3.2523) \\ (2.7427 & 2.7427 & 2.7427 & 2.7427) & (2.2194 & 4.4192 & 4.4192 & 4.8856) & (1.0150 & 2.8241 & 2.8241 & 4.2947) \\ (1.8612 & 1.8612 & 1.8612 & 1.8612) & (1.1147 & 2.9803 & 2.9803 & 4.8856) & (0.0100 & 1.6181 & 1.6181 & 3.2523) \end{array} \right]$ </td></tr></table>

(3) Construct six-dimensional fuzzy attribute evaluation matrix CO<sup>˜</sup> R

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\mathbf{C}\tilde{\mathbf{O}}\mathbf{R} = \left[ \begin{array}{lllll} (10.4187 &amp; 10.4187 &amp; 10.4187 &amp; 10.4187) &amp; (8.6158 &amp; 8.6158 &amp; 8.6158 &amp; 8.6158) &amp; (4.2429 &amp; 4.2429 &amp; 4.2429 &amp; 4.2429)\\ (8.6158 &amp; 8.6158 &amp; 8.6158 &amp; 8.6158) &amp; (9.4112 &amp; 9.4112 &amp; 9.4112 &amp; 9.4112) &amp; (4.6048 &amp; 4.6048 &amp; 4.6048 &amp; 4.6048)\\ (4.2492 &amp; 4.2492 &amp; 4.2492 &amp; 4.2492) &amp; (4.6048 &amp; 4.6048 &amp; 4.6048 &amp; 4.6048) &amp; (14.1664 &amp; 14.1664 &amp; 14.1664 &amp; 14.1664)\\ (3.8576 &amp; 3.8576 &amp; 3.8576 &amp; 3.8576) &amp; (4.6031 &amp; 4.6031 &amp; 4.6031 &amp; 4.6031) &amp; (13.0390 &amp; 13.0390 &amp; 13.0390 &amp; 13.0390)\\ (2.6580 &amp; 11.3411 &amp; 11.3411 &amp; 21.3095) &amp; (3.4429 &amp; 11.7311 &amp; 11.7311 &amp; 19.2532) &amp; (10.1711 &amp; 22.9949 &amp; 22.9949 &amp; 31.1423)\\ (1.6354 &amp; 10.1004 &amp; 10.1004 &amp; 17.3064) &amp; (1.2356 &amp; 8.9548 &amp; 8.9548 &amp; 16.3538) &amp; (6.4628 &amp; 17.9971 &amp; 17.9971 &amp; 25.5083)\\ (3.8576 &amp; 3.8576 &amp; 3.8576 &amp; 3.8576) &amp; (2.6580 &amp; 11.3411 &amp; 11.3411 &amp; 21.3095) &amp; (1.6354 &amp; 10.1004 &amp; 10.1004 &amp; 17.3064)\\ (4.6031 &amp; 4.6031 &amp; 4.6031 &amp; 4.6031) &amp; (3.4429 &amp; 11.7311 &amp; 11.7311 &amp; 19.2532) &amp; (1.2356 &amp; 8.9548 &amp; 8.9548 &amp; 16.3538)\\ (13.0390 &amp; 13.0390 &amp; 13.0390 &amp; 13.0390) &amp; (10.1711 &amp; 22.9949 &amp; 22.9949 &amp; 31.1423) &amp; (6.4628 &amp; 17.9971 &amp; 17.9971 &amp; 25.5083)\\ (12.3229 &amp; 12.3229 &amp; 12.3229 &amp; 12.3229) &amp; (9.4505 &amp; 21.1286 &amp; 21.1286 &amp; 28.1764) &amp; (5.1378 &amp; 15.4322 &amp; 15.4322 &amp; 22.8293)\\ (9.4505 &amp; 21.1286 &amp; 21.1286 &amp; 28.1764) &amp; (7.4110 &amp; 39.8250 &amp; 39.8250 &amp; 84.6906) &amp; (4.5158 &amp; 31.8880 &amp; 31.8880 &amp; 69.6175)\\ (5.1378 &amp; 15.4322 &amp; 15.4322 &amp; 22.8293) &amp; (4.5158 &amp; 31.8880 &amp; 31.8880 &amp; 69.6175) \end{array} \right]$
</div>

Step 4: Eigenvector of six-dimensional fuzzy attribute evaluation space. Approximated eigenvector $\tilde { \mathcal { W } } _ { i }$ of six-dimensional fuzzy evaluation space CO<sup>˜</sup> R can be calculated based on product and root method (geometry average method).

$$
\tilde {\boldsymbol {W}} _ {i} = \left[ \begin{array}{l l l l} (0. 0 5 8 8 & 0. 1 0 1 4 & 0. 1 0 1 4 & 0. 2 2 7) \\ (0. 0 6 0 1 & 0. 1 0 2 6 & 0. 1 0 2 6 & 0. 2 2 9 7) \\ (0. 1 0 7 4 & 0. 1 4 5 9 & 0. 1 4 5 9 & 0. 3 2 6 7) \\ (0. 0 9 8 1 & 0. 1 3 4 8 & 0. 1 3 4 8 & 0. 3 0 1 8) \\ (0. 0 7 5 8 & 0. 2 8 4 4 & 0. 2 8 4 4 & 0. 6 3 6 8) \\ (0. 0 4 6 4 & 0. 2 3 1 0 & 0. 2 3 1 0 & 0. 5 1 7 3) \end{array} \right]
$$

Step 5: Comprehensive weights $\tilde { W } ( A )$ of alternative for all attributes.

$$
\tilde {W} (A) = \left( \begin{array}{c c c c} (0. 3 3 7 5 & 0. 8 1 9 5 & 0. 8 1 9 5 & 1) \\ (0. 3 1 6 4 & 0. 6 7 4 0 & 0. 6 7 4 0 & 1) \\ (0. 3 7 7 0 & 0. 8 9 4 1 & 0. 8 9 4 1 & 1) \\ (0. 3 3 8 7 & 0. 7 4 9 1 & 0. 7 4 9 1 & 1) \end{array} \right)
$$

$$
W (A) = \left[ \begin{array}{c} 0. 7 4 4 1 \\ 0. 6 6 6 1 \\ 0. 7 9 1 3 \\ 0. 7 0 9 2 \end{array} \right]
$$

Step 6: Comprehensive ranking by referring to Definition 2.1. The comprehensive ranking weight (kernel of the fuzzy number) can be calculated for $\tilde { W } ( C )$ by Definition 2.1. The difference of alternatives’ kernel is clear, so uncertainty analysis for this case is not necessary. It is obvious that the ranking result is: $A _ { 3 } {  } A _ { 1 } {  } A _ { 4 } {  } A _ { 2 }$

Comparison results between the proposed algorithm and other algorithms are listed in Table 2.

It is apparent from Table 2 that the proposed improving fuzzy AHP algorithm based on fuzzy eigenvector of fuzzy attribute evaluation space is more efficient than others. It has good objectivity and resolution.

## 7. Conclusions

Multi-attribute decision-making method based on the approximate eigenvector of fuzzy attribute evaluation space adopts observation data to construct a normal fuzzy decision matrix. In addition, fuzzy attribute evaluation space is established by referring to covariance definition. Objectivity and high resolving power for decision-making can be obtained by adopting approximate eigenvector of m-dimensional fuzzy attribute evaluation matrix. Therefore, the proposed algorithm has features of minimum subjectivity and a transparent evaluation process, which can also be verified. Although the proposed method can make a big difference regarding mainstream ranking, it would not make so much difference for branch alternatives. For such cases, the uncertainty analysis that the method provided in Section 5 is necessary. Once the uncertainty analysis results indicate that improving is necessary, the proposed method can be further improved by constructing a fuzzy consistent decision matrix [16] in order to improve intelligibility and reasonability for decision-making in the actual application.

Table 2  
Comparison result for each algorithm

<table><tr><td>Algorithm</td><td>Decision-making benefit value</td><td>Decision-making result</td><td>Objectivity</td><td>Decision-making resolution</td></tr><tr><td>TOPSIS</td><td> $U(A_1)=0.643, U(A_2)=0.268,$  $U(A_3)=0.613, U(A_4)=0.312$ </td><td> $A_1 \succ A_3 \succ A_4 \succ A_2$ </td><td>Subjective</td><td>Low</td></tr><tr><td>Fuzzy Ideal Solution Algorithm</td><td> $D_1^+=0.1561, D_2^+=0.3440,$  $D_3^+=0.1620, D_4^+=0.3018$ </td><td> $A_1 \succ A_3 \succ A_4 \succ A_2$ </td><td>Subjective</td><td>Low</td></tr><tr><td>Fuzzy Negative Ideal Solution Algorithm</td><td> $D_1^-=0.2878, D_2^-=0.0177,$  $D_3^-=0.0631, D_4^-=0.0188$ </td><td> $A_1 \succ A_3 \succ A_4 \succ A_2$ </td><td>Subjective</td><td>Low</td></tr><tr><td>Fuzzy Ideal Solution and Fuzzy Negative Ideal Solution Combined Algorithm</td><td> $D_1=0.6483, D_2=0.0489,$  $D_3=0.2803, D_4=0.0586$ </td><td> $A_1 \succ A_3 \succ A_4 \succ A_2$ </td><td>Subjective</td><td>High</td></tr><tr><td>Comprehensive weight in advance, Fuzzy Ideal Solution and Fuzzy Negative Ideal Solution Combined Algorithm</td><td> $\lambda_1=0.87, \lambda_2=0, \lambda_3=0.94,$  $\lambda_4=0.3$ </td><td> $A_3 \succ A_1 \succ A_4 \succ A_2$ </td><td>Subjective</td><td>High</td></tr><tr><td>Improved Fuzzy AHP Algorithm</td><td> $W(A_1)=0.744, W(A_2)=0.666,$  $W(A_3)=0.791, W(A_4)=0.709$ </td><td> $A_3 \succ A_1 \succ A_4 \succ A_2$ </td><td>Objective</td><td>High</td></tr></table>

## Acknowledgements

This research was funded by the National Natural Science Foundation of China (project No. 29976003) and the Key Research Project of Science and Technology from Ministry of Education in China. We would like to thank Mr. Ian Brannan for reviewing the English. Many thanks are also due to the anonymous reviewers of this paper for useful comments.

## References

[1] G. Bortolan, R. Degani, A review of some methods of ranking fuzzy subsets, Fuzzy Sets and Systems 15 (1985) 1 – 19.

[2] B. Bouchon-Meunier, J. Yap, Linguistic modifiers and imprecise categories, International Journal of Intelligent Systems 7 (1) (1992) 25–36.

[3] S.M. Chen, Evaluating weapon systems using fuzzy arithmetic operations, Fuzzy Sets and Systems 77 (3) (1996) 265– 276.

[4] C.T. Chen, A study of fuzzy group decision-making method, 1998 6th National Conference on Fuzzy Theory and Its Applications, 1998.

[5] S.J. Chen, C.L. Hwang, Fuzzy Multiple Attribute Decision Making: Methods and Application, Springer, New York, 1992.

[6] C.H. Cheng, A new approach for ranking fuzzy numbers by distance method, Fuzzy Sets and Systems 95 (1998) 307–317.

[7] C.H. Cheng, D.L. Mon, Evaluating weapon system by analytical hierarchy process based on fuzzy scales, Fuzzy Sets and Systems 63 (1994) 1 – 10.

[8] M. Delgado, J.L. Verdegay, M.A. Vila, Linguistic decisionmaking models, International Journal of Intelligent Systems 7 (1992) 479 – 492.

[9] Y.J. Guo, Comprehensive Evaluation Theory and Methods, Science Publishing, Beijing, 2002.

[10] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, Choice processes for non-homogeneous group decision making in linguistic setting, Fuzzy Sets and Systems 94 (1998) 287–308.

[11] K. Kim, K.S. Park, Ranking fuzzy numbers with index of optimism, Fuzzy Sets and Systems 35 (1990) 143 – 150.

[12] E.S. Lee, R.L. Li, Comparison of fuzzy numbers based on the probability measure of fuzzy events, Computer and Mathematics with Application 15 (1988) 887 – 896.

[13] R.J. Li, Fuzzy Multi-Criteria Decision Theory and Application, Science Publishing, Beijing, 2002.

[14] T.S. Liou, M.J. Wang, Ranking fuzzy numbers with integral value, Fuzzy Sets and Systems 50 (1992) 247– 255.

[15] S. Mabuchi, An approach to the comparison of fuzzy subsets with an a-cut dependent index, IEEE Transactions on Systems, Man, and Cybernetics SMC-18 (2) (1988) 264– 272.

[16] C.Z. Sun, X.Y. Lin, Fuzzy consistent matrix based on AHP and its application, Fuzzy Systems and Mathematics 16 (3) (2002) 59–63.

[17] L.X. Wang, Fuzzy systems: challenges and chance—my experiences and perspectives, Acta Automatica Sinica 27 (4) (2001) 585–590.

[18] J. Williams, N. Steele, Difference, distance and similarity as a basis for fuzzy support based on prototypical decision class, Fuzzy Sets and Systems 131 (2002) 35–46.

[19] T. Williamson, Vagueness, Rout Ledge, London, 1994.

[20] L.A. Zadeh, Toward a theory of fuzzy information granulation and its centrality in human reasoning and fuzzy logic, Fuzzy Sets and System 19 (1997) 111 – 127.

[21] L.A. Zadeh, A new direction in AI: toward a computational theory of perceptions, AI Magazine 22 (2001) 73 – 84.

![](/api/attachments/CUV2WJQ5/fulltext/images/c1ed6f3e193a28ed14eb8d524cd31e8d76a0c857ef28d250e26ec7fac7e0cc82.jpg)  
Xiangbai Gu holds a BS degree in process and control engineering from the Fushun Petroleum Institute, PRC and an MBA from City University, Seattle, USA, PhD Candidate of Beijing University of Chemical Technology. He is a senior manager of the marketing department in Sinopec Engineering Inc. (SEI). Mr. Gu brings 10 years instrumentation and control system engineering experience and 6 years marketing management experience in the field petro-

chemical to the SEI organization.  
![](/api/attachments/CUV2WJQ5/fulltext/images/aba01324bdf7a174185f8c402b4fe4a3cad07689b2cda6b223f4b2ade4eb169f.jpg)

Qunxiong Zhu is a Professor of Beijing University of Chemical Technology. He is a Vice Dean of School of Information Science and Technology in Beijing University of Chemical Technology. Mr. Zhu has more than 20 years experience in Artificial Intelligence, Data Mining, Decision-making and Control research area.
