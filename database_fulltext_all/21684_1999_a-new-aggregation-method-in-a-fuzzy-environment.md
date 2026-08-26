---
otero_id: 21684
otero_key: "6WKSTE4J"
title: "A new aggregation method in a fuzzy environment"
authors: "Dae-Young Choi"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00087-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A new aggregation method in a fuzzy environment

Dae-Young Choi )

Department of MIS, Yuhan College, 185-34 Koean-Dong, Sosa-Ku, Puchon City, Kyongki-Do, South Korea

Received 30 July 1997; accepted 11 November 1998

## Abstract

Information aggregation provides a starting point for the ability to make useful inferences from large collections of data, and so it plays an important role in many applications related to the development of intelligent systems. In a fuzzy environment, the existing aggregation operators are generally the t-norm, t-conorm, mean operators, Yager’s operator and -operator. However, these aggregation operators do not reflect the situation in the aggregation process, i.e., these types of aggregation operators are independent of the aggregation situation. In order to solve these problems, we propose a new aggregation method to reflect the situation in the aggregation process. It is the aggregation based on situation assessment Ž . Ž . ASA method. It consists of the situation assessment model SAM and the ASA algorithm. In this ASA method, the SAM is utilized to reflect the situation in the aggregation process. This model generates the parameter, which is controlled by the decision maker. It indicates the current degree of aggregation situation. Therefore, our method can be adapted to certain situations by using the parameter. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Aggregation situation; Aggregation based on situation assessment ASA ; Situation assessment model SAM Ž . Ž .

## 1. Introduction

The process of information aggregation appears in many applications related to the development of intelligent systems. One sees aggregation in neural networks, fuzzy logic controllers, vision systems, expert systems and multi-criteria decision support systems. Fuzzy set theory provides an attractive aggregation connectives for integrating membership values representing uncertain information. These connectives can be categorized into the following three classes: union, intersection and compensation connectives. In a fuzzy environment, the existing aggregation operators are, in general, the t-norm, t-conorm, mean operators 5 , Yager’s operator 9 <sup>w x</sup> <sup>w x</sup> and -operator 10,15 . These connectives have some problems in that they do not reflect the situation in the <sup>w</sup> <sup>x</sup> aggregation process, i.e., these types of aggregation are independent of the aggregation situation. Moreover, if several operators are necessary in order to describe a variety of phenomena, the question arises as to how many operators are needed. If one wants to use a very small number of operators to model many situation, then these operators have to be adaptable to the specific context. This can be achieved by parameterization. Although Yager’s operator and -operator use parameter, these operators do not define how to determine the value of the parameter. It is the tendency that the aggregation of human beings depends on the situation. However, there has been little effort to reflect this situation in the aggregation process. In order to solve these problems, we suggest the situation assessment model SAM to reflect the situation in the aggregation process. This model generatesŽ . the parameter, which is controlled by the decision maker. It indicates the current degree of aggregation situation and is determined depending on the aggregation situation. We propose a new aggregation method using the output of the SAM to reflect the situation in the aggregation process. We call it the aggregation based on situation assessment ASA . It is a new aggregation method, which makes the stepwise aggregation withŽ . direction according to the aggregation situation. Therefore, our method can be adapted to certain situations by using the parameter. This method has the advantages that the aggregation is obtained smoothly because the aggregation is made adaptively according to the aggregation situation and the compensation between data aggregated is smoothly handled depending on the situation. Moreover, it is a more systematic method, using algorithmic approach, than the existing aggregation methods.

Fuzzy set 13 may be used to design intelligent systems on the basis of knowledge expressed in natural<sup>w</sup> <sup>x</sup> language. Let us assume that we are looking for an ‘attractive car’, where ‘attractive’ means ‘comfortable and fast’. This kind of linguistic ‘and’ has never been formally or mathematically defined. Zimmermann 14 calls it<sup>w</sup> <sup>x</sup> ‘compensatory and’ by contrast to the ‘logical $a n d ^ { \prime }$ . In decision making, the ‘and’ connecting, for instance, two goals or criteria, most often allows for such a compensation. Possible mathematical models for such a ‘compensatory and’ are, for instance, the arithmetic or the geometric mean. However, these methods cannot reflect the situation in the aggregation process. We believe that human beings have a decision rule enabling him<sup>r</sup>her to choose the right connective for each situation. The main goal of this paper is to emulate the aggregation process of human beings. The aggregation of subjective categories in the framework of human decision almost always shows some degree of compensation. This indicates that human beings partially are using non-verbal aggregation procedures which do not correspond to the verbal and logical connectives $\cdot _ { a n d } ,$ and $\cdot _ { o r } ,$ . It is possible that human beings use many non-verbal connectives in their thinking and reasoning. One type of these connectives may be called ‘merging connectives’ 15 . In this paper we propose the ASA method<sup>w</sup> <sup>x</sup> which produces the biased result of aggregation between min and max depending on the situation. It implies that there is a compensation between min and max according to the situation. We call it ‘compensation based on situation’.

In Section 2, we briefly summarize the existing aggregation methods. We describe the SAM and show its rationality in Section 3. The ASA is described in Section 4. This section is divided into two parts, forms of ASA and its applications, and ASA algorithm and its related properties. In Section 5, we compare the ASA method with the existing aggregation methods. Finally, Section 6 concludes the paper and points out the directions of future research.

## 2. Summary of the existing aggregation operators

In a fuzzy environment, the existing aggregation operators are generally the t-norm, t-conorm, mean operators, Yager’s operator and -operator.

## 2.1. T-norm

An operator $T \colon [ 0 , 1 ] \times [ 0 , 1 ] \to [ 0 , 1 ]$ <sup>w x</sup>  is called t-norm operator 5 if

Ž .a $T ( a , b ) = T ( b , a )$ , commutativity;

Ž .b $T ( a , T ( b , c ) ) = T ( T ( a , b ) , c )$ , associativity;

Ž .c $T ( a , b ) \geq T ( c , d )$ if $a \geq c$ and $b \geq d ;$

Ž .d $T ( a , 1 ) = a , T ( a , 0 ) = 0$

The t-norm operators have been used to prototypically characterize the ‘and’ operator. The important examples of t-norm are min operator and product operator.

## 2.2. T-conorm

An operator $S { : } [ 0 , 1 ] \times [ 0 , 1 ]  [ 0 , 1 ]$ <sup>w x</sup> is called t-conorm operator 5 if

Ž .a $S ( a , b ) = S ( b , a )$ , commutativity;

Ž .b $S ( a , S ( b , c ) ) = S ( S ( a , b ) , c )$ , associativity;

Ž .c $S ( a , b ) \geq S ( c , d ) { \mathrm { ~ i f ~ } } a \geq c { \mathrm { ~ a n d ~ } } b \geq d ;$

Ž .d $ { \cal S } ( a , 1 ) = 1 , { \cal S } ( a , 0 ) = a$

The t-conorm operators have been used to prototypically characterize the $\cdot _ { o r } ,$ operator. The important examples of t-conorm are max operator and algebraic sum operator.

## 2.3. Mean operators

A mapping $M \colon [ 0 , 1 ] ^ { n }  [ 0 , 1 ]$ <sup>w x</sup>  is called a mean operator if it satisfies the following conditions 5 :

Ž .a $M ( a , a , \dots , a ) = a$ , idempotency;

Ž . b M is increasing in each of its arguments, monotonicity;

Ž .c It satisfies a generalized commutativity condition in that the order of the argument is irrelevant.

These conditions can be shown to imply that the mean always lies between the $\cdot _ { a n d } ,$ and $\cdot _ { o r } ,$ operator. In many applications, especially multi-criteria decision making, the union and intersection do not always capture the necessary aggregation of the fuzzy sets. In some of these cases, a mean-type aggregation is more appropriate.

## 2.4. Yager’s operator

Yager 9 suggests a general class of fuzzy intersections and fuzzy unions as follows: Assume A and B are <sup>w</sup> <sup>x</sup> fuzzy subsets of X with membership grades in the unit interval and this operation is defined pointwise.

## 2.4.1. Fuzzy intersection

$$
\mathrm{A} (x) \cap_ {p} \mathrm{B} (x) = \mathrm{C} _ {p} (x) \text {   in   which   } \mathrm{C} _ {p} (x) = 1 - \min \left[ 1, \left[ (1 - \mathrm{A} (x)) ^ {p} + (1 - \mathrm{B} (x)) ^ {p} \right] ^ {1 / p} \right],
$$

$$
\mathrm{for} p \geq 1\tag{1}
$$

If $p = \infty$ then $\mathbf { C } _ { p } ( x ) = \mathrm { m i n } [ \mathbf { A } ( x ) , \mathbf { B } ( x ) ]$ and if $p = 1$ then $\mathbf { C } _ { p } ( \mathbf { \boldsymbol { \mathit { x } } } ) = \operatorname* { m a x } [ 0 , \mathbf { A } ( \mathbf { \boldsymbol { \mathit { x } } } ) + \mathbf { B } ( \mathbf { \boldsymbol { \mathit { x } } } ) - 1 ]$ . It is obvious from the definition of $\mathbf { C } _ { p } ( x )$ that this form of intersection is commutative, associative for all p and a monotonically non-decreasing function of $\operatorname { A } ( x )$ and $\mathbf { B } ( x )$

## 2.4.2. Fuzzy union

$$
\mathrm{A} (x) \cup_ {p} \mathrm{B} (x) = \mathrm{D} _ {p} (x) \text {   in   which   } \mathrm{D} _ {p} (x) = \min \left[ 1, \left[ (\mathrm{A} (x)) ^ {p} + (\mathrm{B} (x)) ^ {p} \right] ^ {1 / p} \right], \quad \text {   for   } p \geq 1\tag{2}
$$

If $p = \infty$ then ${ \bf D } _ { p } ( { \boldsymbol { x } } ) = { \bf m a x } [ { \bf A } ( { \boldsymbol { x } } ) , { \bf B } ( { \boldsymbol { x } } ) ]$ and if $p = 1$ then $\mathbf { D } _ { p } ( x ) = \operatorname* { m i n } [ 1 , \mathbf { A } ( x ) + \mathbf { B } ( x ) ]$ . It is obvious from the definition of $\dot { \mathrm { D } _ { p } ^ { \mathrm { ~ } } } ( x )$ that this form of union is commutative, associative for all p and a monotonically non-decreasing function of $\operatorname { A } ( x )$ and $\mathbf { B } ( x )$

## 2.5. -Operator

Zimmermann and Zysno 15 suggest the <sup>w</sup> <sup>x</sup> -operator as follows:

$$
\mu_ {\theta} = \big (\Pi \mu_ {i} \big) ^ {1 - \gamma} \big (1 - \Pi \big (1 - \mu_ {i} \big) \big) ^ {\gamma},
$$

where i<sup>s</sup>1,2, . . . ,m, m<sup>s</sup>number of sets to be connected and $0 \leq \mu _ { i } \leq 1 , 0 \leq \gamma \leq 1$

3Ž .

If $\gamma = 0 .$ , then $\mu _ { \theta } = \varPi \mu _ { i }$ . This equals the product and provides the truth values for the connective $\cdot _ { a n d }$ . If $\gamma = 1$ , then $\mu _ { \theta } = 1 - \varPi ( 1 - \mu _ { i } )$ . This formula equals the generalized algebraic sum and provides the truth value for the connective $\cdot _ { o r } \cdot$ . The -operator is pointwise injective, continuous, monotonous, commutative and in accordance with the truth tables of dual logic.

In the meantime, considering the aggregation operator described above, t-norm and t-conorm are based on the theory of logic. The mean operators are based on the mathematical properties of averaging. However, these types of aggregation operators are independent of the aggregation situation. Even though Yager’s operator and -operator are suggested as an aggregation method using parameter, at present, the definition of such a parameter is still missing 15 . In order to use this class of operators in a meaningful manner, an operational<sup>w</sup> <sup>x</sup> definition should of course be available for the empirical determination of the value of parameter. If such a value does not exist, then the adequacy of the operator suggested must be doubted 15 . In order to solve these <sup>w</sup> <sup>x</sup> problems, we suggest the SAM.

## 3. Situation assessment model SAM( )

Generally, it is difficult to assess the real world situation. We suggest the SAM to simplify these complex problems. It can be used to reflect the situation in the aggregation process. It is tendency that the decision making of human beings depends on the situation. However, there have been little efforts to reflect this situation in the aggregation process. This model generates the parameter, which is controlled by decision makers to reflect the situation in the aggregation process. The ASA method uses the output of SAM as an indicator of aggregation situation. Therefore, our aggregation method can be adapted to certain situations by using the parameter Fig. 1 . Ž .

## 3.1. Fuzzy expected Õalue FEV( )

The ability to summarize data provides an important method for getting a grasp of the meaning of a larger collection of data. It enables humans to help understand the environment in a manner amenable to future useful manipulation. It also provides a starting point for the ability to make useful inferences from large collections of data. The mean does help in understanding the content of data, but in some respects, it may be too terse as a summarization. The FEV 8 is usually used for evaluating the most ‘representative’ or ‘typical’ value of fuzzy<sup>w</sup> <sup>x</sup> set as a measure of general tendency. Let $\chi _ { \mathrm { A } }$ be a B-measurable function such that $\chi _ { \mathrm { A } } \in [ 0 , 1 ]$ . The FEV of $\chi _ { \mathrm { A } }$ over the set A, with respect to the fuzzy measure $\mu ( \cdot )$ is defined as

$$
\operatorname{FEV} \left(\chi_ {\mathrm{A}}\right) = \sup _ {T \in [ 0, 1 ]} \left\{\min \left[ T, \mu \left(\xi_ {T}\right) \right] \right\} = \sup _ {T \in [ 0, 1 ]} \left\{\min \left[ T, f _ {\mathrm{A}} (T) \right] \right\}\tag{4}
$$

where $\xi _ { \mathrm { T } } = \{ x | \chi _ { \mathrm { A } } ( x ) \geq T \}$ , and $\mu \{ x | \chi _ { \mathrm { A } } ( x ) \geq T \} = f _ { \mathrm { A } } ( T )$

Example 1. In a certain decision situation, for computational simplicity, we assume that the decision maker consider 100 situation factors to solve his<sup>r</sup>her decision problem. For each situation factor, the following question was asked: ‘what is the rate between 0 and 1 to which you agree, that ‘situation factor’ is good’. The results obtained are as follows:

![](/api/attachments/6WKSTE4J/fulltext/images/75f31eb4a24d9111acb13cc09e7f55d8e134e74109a5ccfe133fba85262d78e0.jpg)  
$\mathrm { { X } _ { i } ( i { = } 1 , 2 , \cdots , n ) : \mathrm { { F E V s } , p } }$ : The output as parameter for ASA  
Fig. 1. Relationship between SAM and ASA.

45 situation factors are rated: 0.0

40 situation factors are rated: 0.2

15 situation factors are rated: 0.25

We thus have three different thresholds 0.0, 0.2, 0.25 . The first thing we have to do is to check how manyŽ . answers are above each threshold percentage-wise . Obviously, 100 answers are above or equal to 0.0, 55Ž . answers are above or equal to 0.2, and 15 answers are above or equal to 0.25. Pairing these data and rearranging them by increasing order of the value of threshold, we obtain the following three <sup>w</sup> <sup>x</sup> T, pairs:

Ž . 0.0, 1.0

Ž . 0.2, 0.55

Ž . 0.25, 0.15

Now, the minimum value of each pair is:

min 0.0, 1.0Ž .<sup>s</sup>0.0

min 0.2, 0.55Ž . <sup>s</sup> 0.2

min 0.25, 0.15Ž .<sup>s</sup>0.15

Therefore, following Eq. 4 , the FEV, which is the maximum of all these minima, is: Ž .

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\max (0.0, 0.2, 0.15) = 0.2$.
</div>

It means that the representative value of ‘good’, in ‘decision situation is good’ is 0.2, i.e., FEV<sup>s</sup>0.2. In this case, arithmetic mean of these data is 0.1175. We know that arithmetic mean skewed toward 0.0 more than the FEV. Note that the FEV is a better representative value than the arithmetic mean. Generally, the FEV is more suitable than the value of averaging computation in searching for the representative value of fuzzy set 8 .<sup>w</sup> <sup>x</sup>

In the SAM, we assume that the aggregation situation have the n dimensions. The n dimensions have their own situation factors, respectively. The values of situation factors are evaluated by the decision maker. We utilize the FEV to obtain the representative value of these situation factors of each dimension. In addition, we assume that the values of situation factors are measured on a unit interval where a value above 0.5 is an optimistic situation factor and magnitude below 0.5 indicates a pessimistic situation factor.

## 3.2. Determination of parameter

If there is n-dimensional aggregation situations, then the n $\mathrm { F E V s } ( \mathrm { i . e . , } X _ { 1 } , X _ { 2 } , \cdot \cdot \cdot , X _ { n } )$ are made. The SAM generates the parameter using formulas 5 and 6 . It will be applied to the ASA algorithm as an indicator ofŽ . Ž . aggregation situation. The parameter is determined as follows:

$$
\text { situation\_value } = \left[ \left(\left(\sum X _ {i}\right) / n\right) \times 2 - 1 \right] \times k,\tag{5}
$$

where k is a positive integer and determined by Theorem 3.

p<sup>s</sup>the nearest integer of the situation\_value.

6Ž .

These ${ \mathrm { F E V s ~ } } ( \mathrm { i . e . , ~ } X _ { 1 } , ~ X _ { 2 } , \cdot \cdot \cdot , X _ { n } )$ have values between 0 and 1 by the definition of FEV. Hence, $( \sum X _ { i } ) / n$ becomes the value between 0 and 1. The situation\_value in 5 is a floating point variable and it is transformedŽ . into the nearest integer by the following algorithm.

## Algorithm 1.

<sup>r</sup>) Let $[ ( ( \Sigma X _ { i } ) / n ) \times 2 - 1 ] \times k$ be stored at the situation\_value $^ * /$

<sup>r</sup>)  is a fractional part of the situation\_value $^ { * } /$

Case 1: $\delta < 0 . 5$

p<sup>s</sup>situation\_value<sup>y</sup>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Let $X_{1} = X_{2} = \cdots = X_{n} = 1$ then $(\sum X_{i}) / n = 1$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Case 2: $\delta = 0.5$ $p = \text{situation\_value} - \delta \text{ or } p = \text{situation\_value} + (1 - \delta)$  
/* It is depending on the characteristics of applications */  
Case 3: $\delta &gt; 0.5$ $p = \text{situation\_value} + (1 - \delta)$
</div>

Therefore, p in 6 is the integer value between Ž . <sup>y</sup>k and k. In our method, the k is the maximum number of steps to min or max in Algorithm 2 in Section 4.2.

Theorem 1. Considering the formula $\sim [ [ ( ( \Sigma X _ { i } ) / n ) \times 2 - 1 ] \times k ]$ in the SAM. For all $X _ { i } \ ( i = 1 , 2 , \ldots , n )$ , the value of this formula is a monotonically non-decreasing function.

Proof. For all a, $b \in [ 0 , 1 ] ,$ if $a < b$ then $\sim [ [ ( ( X _ { 1 } + X _ { 2 } + \cdot \cdot \cdot + a + \cdot \cdot \cdot + X _ { n } ) / n ) \times 2 - 1 ] \times k ] \le \sim [ [ ( ( X _ { 1 } + X _ { 2 } + \cdot \cdot \cdot + a + \cdot \cdot \cdot + X _ { n } ) / n ) \times 2 - 1 ] \times k ] \le \sim [ [ ( ( X _ { 1 } + X _ { 2 } + \cdot \cdot \cdot + X _ { n } ) / n ) \times 2 + \cdot \cdot \cdot ]$ $+ X _ { 2 } + \cdot \cdot \cdot + b + \cdot \cdot \cdot + X _ { n } ) / n ) \times 2 - 1 ] \times k ]$ . Therefore, $\sim [ [ ( ( \bar { \Sigma } X _ { i } ) / n ) \times 2 - 1 ] \times k ]$ is a monotonically non-decreasing function for all $X _ { i \cdot \ \square }$

Theorem 2. In the SAM, for all $X _ { i } \ ( i = 1 , 2 , \ldots , n ) , \ - k \leq p \leq k .$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Proof. Since $X_1, X_2, \ldots, X_n \in [0,1]$, the formula $(\sum X_i) / n$ is also between [0,1]. Case 1: When $(\sum X_i) / n = 0$ $\therefore p = -k$  
Case 2: When $0 &lt; (\sum X_i) / n &lt; 0.5$ $\therefore -k \leq p \leq 0$  
Case 3: When $(\sum X_i) / n = 0.5$ $\therefore p = 0$  
Case 4: When $0.5 &lt; (\sum X_i) / n &lt; 1$ $\therefore 0 \leq p \leq k$  
Case 5: When $(\sum X_i) / n = 1$ $\therefore p = k$  
Therefore, $-k \leq p \leq k$.
</div>

Example 2. We assume that the values of situation factors are measured on a unit interval where a value above 0.5 is an optimistic situation factor and magnitude below 0.5 indicates a pessimistic situation factor. In the SAM, the FEV $( { \mathrm { i . e . , ~ } } X _ { 1 } , \ X _ { 2 } , \cdots , X _ { n } )$ is utilized to obtain the representative value of these situation factors of each dimension.

Case 1: When all FEVs indicate the most pessimistic situation.

Case 2: When all FEVs indicate moderate situation.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Let $X_{1}=X_{2}=\cdots=X_{n}=0.5$ then $(\sum X_{i})/n=0.5$
</div>

Case 3: When all FEVs indicate the most optimistic situation.

In other combinations of FEVs cases, the SAM generate the parameter: $- k \leq p \leq k .$

Definition 1. According to Theorem 2 and Example 2, aggregation situation is parameterized depending on the situation.

Case 1: Optimistic situation: When p is the value between 1 and k. Let ${ \mathrm { o p } } = p$

Case 2: Moderate situation: When p is the value 0.

Case 3: Pessimistic situation: When p is the value between <sup>y</sup>1 and <sup>y</sup>k. Let $\mathsf { p p } = | p |$

Definition 2. In the SAM, the parameter, p, indicates the current degree of aggregation situation. It has the integer value between <sup>y</sup>k and k. The k is the maximum number of steps to min or max in Algorithm 2 in Section 4.2.

Theorem 3. In the case of applying Algorithm 2 in Section 4.2, k in 5 is determined as follows. Ž .

$k = \lfloor \log _ { 2 } n \rfloor + 1 ,$ where the range of data aggregated is $[ 0 , n ]$

Proof. In general, membership functions for representing fuzzy sets associate with each point in a real number in the interval 0,1 . Hence, we use the unit interval as a range of data aggregated. We assume that the data<sup>w</sup> <sup>x</sup> aggregated and the final result of aggregation are rounded to two fractional digits. That is, some of 0.00, 0.01, . . . , 0.99, 1.00 are given as data aggregated and the final result of aggregation has the same number of4 fractional digits. Since k is the maximum number of steps to min or max in Algorithm 2 in Section 4.2, k occurred in the cases when the extreme value of the universal range, i.e., 0,1 , is included in the data<sup>w x</sup> aggregated. That is, when the pessimistic situation occurs, the data aggregated include the extreme value 0, or when the optimistic situation occurs, the data aggregated include the extreme value 1.

The ASA algorithm makes the stepwise aggregation with direction according to the aggregation situation.

$$
\begin{array}{c c c c c}\text {The smallest min}&\leftarrow&\text {The direction of aggregation} \rightarrow&\text {The largest max}\\\hline M _ {K} ^ {P}&\dots&M _ {1} ^ {P}&M _ {0} ^ {M}&M _ {1} ^ {O}\\\hline\end{array}
$$

We assume that the min is the value of the most pessimistic data aggregated and the max is the value of the most optimistic data aggregated. The $M _ { 0 } ^ { \mathrm { M } }$ is the arithmetic mean of data aggregated and it is the result of aggregation when p is 0. When the moderate situation occurs, since the result of aggregation is the arithmetic mean, by Algorithm 2 in Section 4.2, there is no need to obtain the min or max. Thus, the number of steps to min or max is 0. The $M _ { 1 } ^ { \mathrm { o } }$ is a result of aggregation when the aggregation situation is optimistic with degree 1. The $M _ { 1 } ^ { \mathrm { P } }$ is a result of aggregation when the aggregation situation is pessimistic with degree 1, i.e., the superscript represents the situation by Definition 1 and the subscript represents the degree of situation. As a generalization, $M _ { i } ^ { \mathrm { P } } , \ M _ { i } ^ { \mathrm { O } }$ are determined by Algorithm 2 in Section 4.2 as follows: $\bar { M } _ { i } ^ { \mathrm { P } } = ( M _ { i - 1 } ^ { \mathrm { P } } + \operatorname* { m i n } ) / 2$ $( i = 1 , 2 , \ldots , \mathsf { p p }$ and $M _ { 0 } ^ { \dot { \mathrm { P } } } = M _ { 0 } ^ { \mathrm { M } } )$ and $M _ { i } ^ { \mathrm { o } } = \stackrel { \cdot } { ( } M _ { i - 1 } ^ { \mathrm { o } } + \mathrm { m a x } ) / 2 , ( i = 1 , 2 , . . . , \mathrm { o p }$ and $M _ { 0 } ^ { 0 } = M _ { 0 } ^ { \mathrm { M } } )$ T

To simplify the proof, we consider the cases when the number of data aggregated is two. In other combinations of data aggregated cases, the number of steps to min or max is in this boundary also.

Case 1: 0.00, 0.00 or 1.00, 1.00 : In this case, min and max are equal.  4  4 [ For all situations, the number of steps to min or max is 0.

Case 2: 0.00, 1.00  4

We consider the aggregation of the extreme values to show the cases when the maximum number of steps to min or max, i.e., k, occurs. We assume that the final result of aggregation is rounded to two fractional digits. Ž .i When the moderate situation occurs

$$
M _ {0} ^ {\mathrm{M}} = (0. 0 0 + 1. 0 0) / 2 = 0. 5 0
$$

[ In this case, there is no need to obtain the min or max. Thus, the number of steps to min or max is 0.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(ii) When the pessimistic situation occurs
$M_{1}^{\mathrm{P}} = (0.50 + \min)/2 = (0.50 + 0.00)/2 = 0.25$ $M_{2}^{\mathrm{P}} = (0.25 + \min)/2 = (0.25 + 0.00)/2 = 0.125$ $M_{3}^{\mathrm{P}} = (0.125 + \min)/2 = (0.125 + 0.00)/2 = 0.0625$ $M_{4}^{\mathrm{P}} = (0.0625 + \min)/2 = (0.0625 + 0.00)/2 = 0.03125$ $M_{5}^{\mathrm{P}} = (0.03125 + \min)/2 = (0.03125 + 0.00)/2 = 0.015625$ $M_{6}^{\mathrm{P}} = (0.015625 + \min)/2 = (0.015625 + 0.00)/2 = 0.0078125$ $M_{7}^{\mathrm{P}} = (0.0078125 + \min)/2 = (0.0078125 + 0.00)/2 = \underline{0.00390625} \cong 0.00$ (the smallest min)
∴ The number of steps to min is 7.
(iii) When the optimistic situation occurs
$M_{1}^{\mathrm{O}} = (0.50 + \max)/2 = (0.50 + 1.00)/2 = 0.75$ $M_{2}^{\mathrm{O}} = (0.75 + \max)/2 = (0.75 + 1.00)/2 = 0.875$ $M_{3}^{\mathrm{O}} = (0.875 + \max)/2 = (0.875 + 1.00)/2 = 0.9375$ $M_{4}^{\mathrm{O}} = (0.9375 + \max)/2 = (0.9375 + 1.00)/2 = 0.9687$ $M_{5}^{\mathrm{O}} = (0.9687 + \max)/2 = (0.9687 + 1.00)/2 = 0.984375$ $M_{6}^{\mathrm{O}} = (0.984375 + \max)/2 = (0.984375 + 1.00)/2 = 0.9921875$ $M_{7}^{\mathrm{O}} = (0.9921875 + \max)/2 = (0.9921875 + 1.00)/2 = \underline{0.99609} \cong 1.00$ (the largest max)
∴ The number of steps to max is 7.
To applying the log function, the range of the data aggregated, i.e., {0.00, 0.01, ..., 0.99, 1.00} is transformed into {0, 1, ..., 99, 100}, i.e., n = 100. And $2^{7-1} &lt; 2^{7}$. In this case, k is 7. Therefore, using log function, the relationship between k and n is represented by the following formula: $k = [\log_2 n] + 1$. □
</div>

## 4. Aggregation based on situation assessment ASA( )

In a fuzzy environment, the existing aggregation operators are generally the t-norm, t-conorm, mean operators, Yager’s operator and -operator. However, these connectives do not reflect the situation in the aggregation process, i.e., these types of aggregation are independent of the aggregation situation. Although Yager’s operator and -operator use parameter, these operators do not define how to determine the value of the parameter. In order to solve these problems, we suggest the SAM. Using the SAM, we propose a new aggregation method to reflect the situation in the aggregation process. It is the ASA. It makes the stepwise aggregation with direction according to the aggregation situation. This method has the advantage that the aggregation is obtained smoothly because the aggregation is made adaptively according to the aggregation situation, i.e., the ASA method can be adapted to certain situations. Moreover, it is the more systematic method, using algorithmic approach, than the existing aggregation methods.

## 4.1. Forms of ASA and its applications

We suggest the ASA as a new aggregation method in which the rule contains propositions with fuzzy concepts. The fact is the parameter, which is made by using the SAM. It has the following forms.

## 4.1.1. Aggregation for one object

$$
\begin{array}{l} \text {Rule: IF X is E^{1} AND X is E^{2} AND,\cdots,X is E^{n} THEN Y = f(E^{1},E^{2},\cdots,E^{n})} \\ \text {Fact: p} \end{array}\tag{7}
$$

$$
\mathrm{Y} ^ {\prime} = f _ {\mathrm{P}} \left(\mathrm{E} ^ {1}, \mathrm{E} ^ {2}, \dots , \mathrm{E} ^ {\mathrm{n}}\right)
$$

where the variable X takes values in universe of discourse U and $E ^ { i , \ast } \mathrm { ~ s ~ } ( i = 1 , 2 , \cdot \cdot \cdot , n )$ are description of the linguistic variable X, which is approximated by point values over U. The $E ^ { i \bullet } \mathbf { s }$ are characterized by a membership function, which associate with each point in a real number in the unit interval 7 . In this case, for<sup>w</sup> <sup>x</sup> one object X, if there are different values of $E ^ { i , \ast } \mathrm { ~ s ~ } ( i = 1 , 2 , \cdot \cdot \cdot , n )$ , then aggregate $E ^ { i , \ast } \mathrm { ~ s ~ } ( i = 1 , 2 , \cdot \cdot \cdot , n )$ are based on the aggregation situation. In order to obtain a conclusion, the parameter is required to reflect the aggregation situation in the aggregation process. The conclusions of this form of ASA method are changed according to the parameter, i.e., the ASA method produces the biased results of aggregation depending on the parameter.

## 4.1.2. Aggregation for many objects

$$
\begin{array}{l} \text {Rule: IF \alpha is A AND \beta is B AND, \cdots, \gamma is C THEN Y = f(A,B,\cdots,C)} \\ \text {Fact: p} \end{array}\tag{8}
$$

$$
\mathrm{Y} ^ {\prime} = f _ {\mathrm{P}} (\mathrm{A}, \mathrm{B}, \dots , \mathrm{C})
$$

where variables $\alpha , \beta , . . . , \gamma$ take values in universe of discourse U, $\mathrm { V } , \ \ldots , \mathrm { W } ,$ , respectively and $\mathbf { A } , \mathbf { B } , \ldots , \mathbf { C }$ are descriptions of the linguistic variables , $\beta , \ . . . , \gamma$ , respectively which are approximated by point values over U, V, . . . , W, respectively. $\mathbf { A } , \mathbf { B } , \ldots , \mathbf { C }$ are characterized by membership functions which associate with each point of real number in the unit interval. The conclusions of this form of ASA method are also changed according to the parameter.

The ASA method is designed for emulating the human aggregation behavior. We believe that the reflection of situation, in emulating the human aggregation process, is one of the essential factors. Thus, we propose the ASA method to reflect the situation in the aggregation process.

In the meanwhile, it is applicable to the aggregation problems in neural networks, fuzzy logic controllers, vision systems, expert systems, multi-criteria decision support systems and group decision support systems.

## 4.2. ASA algorithm

In general, the existing aggregation methods use t-norm, t-conorm, mean operators, Yager’s operator and -operator. These methods have some problems in that they do not reflect the aggregation situation in the aggregation process. In order to solve these problems, we propose the ASA method to reflect the aggregation situation in the aggregation process. The typical application areas of this method are multi-criteria decision support systems and group decision support systems. Using the ASA method, decision makers can aggregate the many values based on situation. Let the data to be aggregated be $E ^ { i } \left( i = 1 , 2 , \dots , n \right)$ and $E ^ { i } \left( \mathrm { i } = 1 , 2 , \dots , n \right)$ are descriptions of linguistic variables. Using 6 and definition 1, the ASA is executed by the following algorithm. Ž . Let $E ^ { 1 } = v _ { 1 } , E ^ { 2 } = v _ { 2 } , \mathbf { \partial } \cdot \cdot \cdot , E ^ { n } = v _ { n } $ , and the $E ^ { i } \mathrm {  ~ s ~ }$ are characterized by membership functions which associate <sup>w</sup> <sup>x</sup> with each point of real number in the interval 0,1 . We assume that the values of $E ^ { i } \mathrm { ^ s }$ are measured on a scale between 0 and 1, where a value above 0.5 is desirable and a magnitude below 0.5 indicates an undesirable impact 1,4 , i.e., we assume that min is the value of the most pessimistic data aggregated and max is the value of the most optimistic data aggregated.

## Algorithm 2.

Case 1: When the aggregation situation is optimistic

Step 1: aggregation\_value $= ( v _ { 1 } + v _ { 2 } + \cdot \cdot \cdot + v _ { n } ) / n$

Step 2: $h v = \operatorname* { m a x } [ v _ { 1 } , v _ { 2 } , \cdot \cdot \cdot , v _ { n } ]$

Step 3: FOR i<sup>s</sup>1 TO op DO

aggregation\_value<sup>s</sup>Ž . aggregation\_value<sup>q</sup>hÕ <sup>r</sup>2

END $\big / *$ op is obtained by Definition $1 ~ * /$

Step 4: aggregation\_result<sup>s</sup>aggregation\_value

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Case 2: When the aggregation situation is moderate
Step 1: $\text{aggregation\_value} = (v_1 + v_2 + \cdots + v_n)/n$
Step 2: $\text{aggregation\_result} = \text{aggregation\_value}$
Case 3: When the aggregation situation is pessimistic
Step 1: $\text{aggregation\_value} = (v_1 + v_2 + \cdots + v_n)/n$
Step 2: $lv = \min[v_1, v_2, \cdots, v_n]$
Step 3: FOR i = 1 TO pp DO
$\text{aggregation\_value} = (\text{aggregation\_value} + lv)/2$
END /* pp is obtained by Definition 1 */
Step 4: $\text{aggregation\_result} = \text{aggregation\_value}$
</div>

Therefore, the results of aggregation using the ASA algorithm are biased toward min or max according to the situation.

In the meantime, even though the same data are aggregated, the different results are produced. The reason is that the results of aggregation using the ASA algorithm are changed depending on the parameter.

## 4.2.1. Properties of the ASA algorithm

The ASA algorithm shows the following properties: first, when the optimistic situation occurs, the results of ASA algorithm come closer to the max as the value of parameter increases, i.e., it is converging to the most optimistic data aggregated as the value of parameter increases. Second, when the moderate situation occurs, the result of ASA algorithm is the arithmetic mean of data aggregated. Third, when the pessimistic situation occurs, the results of ASA algorithm come closer to the min as the absolute value of parameter increases, i.e., it is converging to the most pessimistic data aggregated as the absolute value of parameter increases. Hence, the ASA algorithm produces the biased results of aggregation between min the most pessimistic data and max the Ž . Ž most optimistic data depending on the parameter. In our method the values of parameter are changed depending . on the aggregation situation. Therefore, the ASA algorithm can be adapted to the aggregation situation by using the parameter. Moreover, it is the more systematic method, using algorithmic approach, than the existing aggregation methods. It makes the stepwise aggregation with direction according to the parameter Fig. 2 .Ž .

## 4.2.2. Compensation using the ASA algorithm

The aggregation of subjective categories in the framework of human decision almost always shows some degree of compensation. This indicates that human beings are partially using non-verbal aggregation procedures which do not correspond to the verbal and logical connectives ‘and’ and ‘or’. It is possible that human beings use many non-verbal connectives in their thinking and reasoning. One type of these connectives may be called ‘merging connectives’ 15 . We propose the ASA method to aggregate the many values based on situation. The<sup>w</sup> <sup>x</sup> ASA method produces the biased result of aggregation between min and max depending on the situation. It implies that there is a compensation between min and max according to the aggregation situation. We call it ‘compensation based on situation’.

![](/api/attachments/6WKSTE4J/fulltext/images/ba8102f954070b7f3a9ecee538a3f3bffa613762282fe943d6ba10192d2dde1b.jpg)  
Fig. 2. The directionality of the ASA algorithm.

![](/api/attachments/6WKSTE4J/fulltext/images/193948bc87de29b6c39348c84a7a6f9a9b415f2e392a5380617cc6e6400cbdf9.jpg)  
Fig. 3. The directionality of the ASA algorithm in optimistic situation.

A central issue in the development of the theory of approximate reasoning is the aggregation of linguistic variables 12 . The ASA method may be used to aggregate the linguistic variables in the condition of if–then<sup>w</sup> <sup>x</sup> rules. In this case, compensation between linguistic variables is handled by ‘compensation based on situation’.

## 4.2.3. Numerical example of the ASA algorithm

Let the data to be aggregated be 0.68, 0.41, 0.19, 0.57, 0.42 , then the ASA algorithm makes the results of 4 aggregation depending on the situation. In this algorithm, using the SAM, the aggregation situation is represented by the parameter.

Ž .i When the optimistic situation occurs. The results of ASA algorithm are changed depending on the parameter as shown in Fig. 3.

Ž .ii When the moderate situation occurs. The result of ASA algorithm is the arithmetic mean of data aggregated, i.e., $( 0 . 6 8 + 0 . 4 1 + 0 . 1 9 + 0 . 5 7 + 0 . 4 2 ) / 5 = 0 . 4 5$

Ž . iii When the pessimistic situation occurs. The results of ASA algorithm are changed depending on the absolute value of parameter as shown in Fig. 4.

From this numerical example, we know that the ASA algorithm makes the stepwise aggregation with direction according to the parameter. Moreover, when the aggregation situation is pessimistic or optimistic, the number of steps to min or max, respectively is 6. The 6 is smaller than the maximum number of steps, k, in Theorem 3. Thus, this example shows the correctness of Theorem 3.

![](/api/attachments/6WKSTE4J/fulltext/images/bf302a3f7b6c45a5c0396b185a270f1b66d25edd91bb035e4cc24524c255432e.jpg)  
Fig. 4. The directionality of the ASA algorithm in pessimistic situation.

Table 1  
Comparisons between the ASA method and the existing aggregation methods

<table><tr><td>Attributes</td><td>The existing aggregation methods</td><td>ASA method</td></tr><tr><td>Aggregation situation</td><td>Not reflect</td><td>Reflect</td></tr><tr><td>Directionality of aggregation</td><td>No</td><td>Yes</td></tr><tr><td>Aggregation method</td><td>Operators using t-norm, t-conorm, mean operator, etc.</td><td>Stepwise aggregation based on situation</td></tr><tr><td>Compensation</td><td>No or limited</td><td>Compensation based on situation</td></tr><tr><td>Aggregation result</td><td>Ad-hoc depending on the operators</td><td>Adaptive depending on the situation</td></tr></table>

## 5. Comparisons between the ASA method and the existing aggregation methods

Bellman and Zadeh’s method 2,11 to determine the optimal decision could not reflect the aggregation<sup>w</sup> <sup>x</sup> situation in the aggregation process. They assume that the aggregation situation is the most pessimistic situation. Therefore, their method makes the result of aggregation with min operator unconditionally. In addition, their method could not reflect the interaction between criteria. It implies that there is no compensation between criteria. Observing managerial decisions, one finds that there are hardly any decisions with no compensation between either different degrees of goal achievement or the degrees to which restrictions are limiting the scope of decisions 15 . Although Yager’s operator and  -operator use parameter, these operators do not define how to determine the value of the parameter. In order to handle these problems, we propose the ASA method using the SAM. If we use the ASA method in the decision problems, then the optimal decision is determined according to the situation. Thus, the ASA method aids the decision maker to get a suitable decision according to the situation. Moreover, in the ASA method the compensation between data to be aggregated occurs depending on the situation. Therefore, using the ASA method, the reflection of aggregation situation and the compensation between data aggregated are smoothly handled depending on the situation. Hence, the ASA method improves the adaptability in aggregation.

We summarize the differences between the ASA method and the existing aggregation methods in Table 1.

## 6. Conclusion and future work

Generally, it is difficult to assess the real world situation. We suggest the situation assessment model SAMŽ . to simplify these complex problems. It can be used to reflect the situation in the aggregation process. It is the tendency that the aggregation of human beings depends on the situation. However, there has been little effort to reflect this situation in the aggregation process. In a fuzzy environment, the existing aggregation methods are generally the t-norm, t-conorm, mean operator, Yager’s operator and -operator. These methods have some problems in that they do not reflect the aggregation situation. In order to solve these problems, we propose a new aggregation method using the SAM and the ASA algorithm to reflect the situation in the aggregation process.

The ASA method is designed for emulating the human aggregation behavior. We believe that the reflection of situation, in emulating the human aggregation process, is one of the essential factors. This ASA method assists the decision maker to reflect the situation in the aggregation process. It makes the stepwise aggregation with direction according to the aggregation situation, i.e., it can be adapted to certain situations. Using the ASA method, decision makers can aggregate the many values based on situation. Thus, the ASA method aids the decision maker to get a suitable decision according to the situation. This method has the advantages in that the aggregation is obtained smoothly because the aggregation is made adaptively according to the aggregation situation, and the compensation between data aggregated is smoothly handled depending on the situation. Hence, our method improves the adaptability in aggregation. In addition, it is the more systematic method, using algorithmic approach, than the existing aggregation methods.

In this paper, we show the rationality of the ASA method and analyze the differences between the ASA method and the existing aggregation methods.

Future research may be extended in several directions based on the current results: First, we will consider another method to determine the representative value in treating fuzzy sets. For example, weighted fuzzy expected value 3 , neural network 6 , etc. Second, the precise weight assignment methods between data<sup>w x</sup> <sup>w x</sup> aggregated must be considered.

## Acknowledgements

The author wish to thank Dr. Kyung-Whan Oh, the professor of Sogang university in South Korea, for his instruction and support; and Sun-Gyung Jung, plan and control manager<sup>r</sup>education center of oracle Korea, for her encouragement and support. This work has been supported by Yuhan College.

## References

<sup>w</sup> <sup>x</sup> 1 H.A. Alley, C.P. Bacinello, K.W. Hipel, Fuzzy set approaches to planning in the grand river basin, Advances in Water Resources 2 Ž .1979 3–12.

<sup>w</sup> <sup>x</sup> 2 R.E. Bellman, L.A. Zadeh, Decision-making in a fuzzy environment, Management Science 17 4 1970 B141–B164.Ž . Ž .

<sup>w</sup> <sup>x</sup>3 M. Friedman, M. Schneider, A. Kandel, The use of weighted fuzzy expected value in fuzzy expert systems, Fuzzy Sets and Systems Ž . Ž .North-Holland 31 1989 37–45.

<sup>w</sup> <sup>x</sup> 4 K.W. Hipel, in: M.M. Gupta, E. Sanchez Eds. , Fuzzy Set Methodologies in Multicriteria Modeling, Fuzzy Information and Decision Ž . Process, North-Holland, 1982, pp. 279–287.

<sup>w</sup> <sup>x</sup> 5 G.J. Klir, T.A. Folger, Fuzzy Sets, Uncertainty and Information, Prentice Hall, 1988.

<sup>w</sup> <sup>x</sup> 6 J.L. McClelland, D.E. Rumelhart, The PDP Research Group, Parallel Distributed Processing 1, The MIT Press, 1986.

<sup>w</sup> <sup>x</sup> 7 H. Nakanishi, I.B. Turksen, M. Sugeno, A review and comparison of six reasoning methods, Fuzzy Sets and Systems North-Holland Ž . 57 1993 257–294.Ž .

<sup>w</sup> <sup>x</sup> 8 R.R. Yager, On a general class of fuzzy connectives, Fuzzy Sets and Systems 4 1980 235–242. Ž .

<sup>w</sup> <sup>x</sup> 9 R.R. Yager, Connectives and quantifiers in fuzzy sets, Fuzzy Sets and Systems 40 1991 39–75. Ž .

<sup>w</sup> <sup>x</sup> 10 M. Schneider, M. Friedman, A. Kandel, On fuzzy reasoning in expert systems, FSU-SCRI-87-09, March, 1987.

<sup>w</sup> <sup>x</sup> 11 L.A. Zadeh, Outline of a new approach to the analysis of complex systems and decision process, IEEE Transactions on SMC 3 1973Ž . 28–44.

<sup>w</sup> <sup>x</sup> 12 L.A. Zadeh, A theory of approximate reasoning, in: J.E. Hayes et al. Eds. , Machine Intelligence, Wiley, 1979 pp. 149–194. Ž .

<sup>w</sup> <sup>x</sup> 13 L.A. Zadeh, Fuzzy sets, Infomation and Control 8 1965 338–353. Ž .

<sup>w</sup> <sup>x</sup> 14 H.J. Zimmermann, Fuzzy sets, Decision Making and Expert Systems, Kluwer Academic Publishers, 1986.

<sup>w</sup> <sup>x</sup> 15 H.J. Zimmermann, P. Zysno, Latent connectives in human decision making, Fuzzy Sets and Systems North-Holland 4 1980 37–51. Ž . Ž .

![](/api/attachments/6WKSTE4J/fulltext/images/33429614abb137a6ee04d95837d67afa64c33fb8686d8c7bf4eb1d6b429c1026.jpg)  
Dae-Young Choi is a full-time lecturer in the Department of MIS at Yuhan College in Puchon city, South Korea. Previously, he was a research fellow at the Korea Institute for Defense Analyses from 1985 to 1990. He received his BS, MS and PhD degrees in computer science from Sogang University, in 1985, 1992 and 1996, respectively. He has a national certificate of professional engineer for information processing systems. His research interests include applications of artificial intelligence, fuzzy systems, expert systems and group decision support systems.
