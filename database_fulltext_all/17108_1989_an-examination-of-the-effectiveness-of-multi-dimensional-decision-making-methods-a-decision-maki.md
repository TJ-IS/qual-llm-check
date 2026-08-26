---
otero_id: 17108
otero_key: "QW85R7MH"
title: "An examination of the effectiveness of multi-dimensional decision-making methods: A decision-making paradox"
authors: "Evangelos Triantaphyllou; Stuart H. Mann"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90037-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Examination of the Effectiveness of Multi-Dimensional Decision-Making Methods: A Decision-Making Paradox

Evangelos TRIANTAPHYLLOU \* and Stuart H. MANN \*\*

\* Department of Industrial and Management Systems Engineering, The Pennsylvania State University, PA 16802, USA.
\*\* School of Hotel, Restaurant, and Institutional Management, The Pennsylvania State University, PA 16802, USA

This paper presents the results of a study that compared four decision-making methods. The methods examined were the weighted sum model, the weighted product model, the analytic hierarchy process, and the revised analytic hierarchy process. Two evaluative criteria were used in an attempt to find the best method. The first criterion was to see if the method when accurate in a multi-dimensional situation remained accurate in a single-dimension case. The second criterion determined the stability of a method in yielding the same outcome when a nonoptimal alternative was replaced with a worse alternative. Tests were conducted using simulated decision problems where random numbers were used for the values of the many combinations of alternatives and criteria. The results illustrate the paradox of deciding on a single best decision-making method. While this paradox is not resolved, useful information is presented for comparing the four methods tested.

Keywords: Multi-Decision-Making, Weighted Sum Model, Weighted Product Model. Analytic Hierarchy Process, Eigenvectors.

ations Research and Man-Environment Relations in 1984 and the M.S. degree in Computer Science both from The Pennsylvania State University. His research interests are expert systems, decision support systems, fuzzy sets, and the application of optimization techniques to logical problems.

## 1. Introduction

Evangelos Triantaphyllou is a computer consultant and a research member in the Center for Academic Computing at The Pennsylvania State University while he is working on his dissertation for the Dual Ph.D. in Operations Research and Industrial and Management Systems Engineering at the same university. He received the Diploma in Architectural Engineering from the National Technical University of Athens, Greece, in 1983. He received a Dual M.S. degree in Oper-

With the continuing proliferation of decision methods and their modifications, it is important to have an understanding of their comparative value. Each of the methods uses numeric techniques to help decision-makers choose among a discrete set of alternative decisions. This is achieved on the basis of the impact of the alternatives on certain criteria and thereby on the overall utility of the decision-maker(s). The difficulty that always occurs when trying to compare decision methods and choose the best one is that a paradox is reached, i.e., What decision-making method should be used to choose the best decision-making method? This paper reports the results of a comparative analysis of four decision-making methods and illustrates the paradox.

![](/api/attachments/QW85R7MH/fulltext/images/cb732805302cb972fd0b6903f9346cea3e44dea1b02056566c9beb15d8d05b4a.jpg)

Despite the criticism that multi-dimensional methods have received, some of them are widely used. The weighted sum model (WSM) is the earliest and probably the most widely used method. The weighted product model (WPM) can be considered as a modification of the WSM, and has been proposed in order to overcome some of its weaknesses. The analytic hierarchy process (AHP), as proposed by Saaty [5], is a later development and it has recently become increasingly popular. Professors Belton and Gear [1] suggest a modification to the AHP that appears to be more powerful than the original approach.

![](/api/attachments/QW85R7MH/fulltext/images/b5193532325f06e22b72eba8cac73e506215814b5fbaf81deb83b67e356d42cb.jpg)  
Stuart H. Mann is Professor of Operations Research in the School of Hotel, Restaurant and Institutional Management at Penn State. He has a Ph.D. and a M.S. in Operations Research from Case Western Reserve University, and a B.S. in Mathematics from the University of Illinois. His research interests are in the application of decision-making methods to problems in the hospitality and service industries. He is an active consultant in the strategic management of retail operations.

In the section that follows these four methods are presented. In the second section the methods are tested in terms of two evaluative criteria. The last section uses the test findings and examines the implication of these findings on the effectiveness of the various decision-making approaches.

## 2. Some Decision-Making Methods

There are three steps in utilizing any decision-making technique involving numerical analysis of alternatives:

(1) Determining the relevant criteria and alternatives.

(2) Attaching numerical measures to the relative importance of the criteria and to the impacts of the alternatives on these criteria.

(3) Processing the numerical values to determine a ranking of each alternative.

This paper is only concerned with the effectiveness of the four methods in performing step 3.

## 2.1. The Weighted Sum Model

The weighted sum model (WSM) is probably the most commonly used approach, especially in single dimensional problems. If there are M alternatives and N criteria then, the best alternative is the one that satisfies (in the maximization case) the following expression (Fishburn, [3]):

$$
A _ {\mathrm{WSM}} ^ {*} = \max _ {i} \sum_ {j = 1} ^ {N} a _ {i j} w _ {j} \quad \text { for } \quad i = 1, 2, 3, \dots , M,\tag{1}
$$

where $A(\text{WSM score}) = \text{the WSM score of the best alternative, } N = \text{the number of criteria, } a_{ij} = \text{the actual value of the } i\text{th alternative in terms of the } j\text{th criterion, } w_j = \text{the weight of importance of the } j\text{th criterion.}$

The assumption that governs this model is the additive utility assumption. That is to say, the total value of each alternative is equal to the sum of products given as (1).

In single-dimensional cases where all the units are the same (e.g., dollars, feet, seconds) the WSM can be used without difficulty. Difficulty with this method emerges when it is applied to multi-dimensional decision-making problems. Then, in combining different dimensions, and consequently different units, the additive utility assumption is violated and the result is equivalent to adding apples and oranges.

## 2.2. The Weighted Product Model

The weighted product model (WPM) is very similar to the WSM. The main difference is that instead of addition in the model there is multiplication. Each alternative is compared with the others by multiplying a number of ratios, one for each criterion. Each ratio is raised to the power equivalent of the relative weight of the corresponding criterion. In general, in order to compare the alternatives $A_{K}$ and $A_{L}$ the following product (Bridgman [2] and Miller and Starr [4]) has to be calculated:

$$
R \left(A _ {K} / A _ {L}\right) = \prod_ {j = 1} ^ {N} \left(a _ {K j} / a _ {L j}\right) ^ {w _ {j}},
$$

where N = the number of criteria, $a_{ij}$ = the actual value of the ith alternative in terms of the jth criterion, $w_{j}$ = the weight of importance of the jth criterion.

If the term $R(A_{K}/A_{L})$ is greater than or equal to one, then it indicates that the alternative $A_{K}$ is more desirable than the alternative $A_{L}$ (in the maximization case). The best alternative is the one that is better than or at least equal to all the other alternatives.

The WPM is sometimes called dimensionless analysis because its structure eliminates any units of measure. Thus, the WPM can be used in single- and multi-dimensional decision-making problems. An advantage of the method is that instead of the actual values it can use relative ones. This is true because

$$
\frac {a _ {K j}}{a _ {L j}} = \frac {a _ {K j} / \sum_ {i = 1} ^ {N} a _ {K i}}{a _ {L j} / \sum_ {i = 1} ^ {N} a _ {L i}} = \frac {a _ {K j} ^ {\prime}}{a _ {L j} ^ {\prime}}.
$$

A relative value $a_{Kj}^{\prime}$ is calculating using the formula: $a_{Kj}^{\prime} = a_{Kj} / \sum_{i=1}^{N} a_{Ki}$ where $a_{Kj}$ 's are the actual values.

## 2.3. The Analytic Hierarchy Process

Part of the analytic hierarchy process (AHP) (Saaty, [5]) deals with the structure of an $M \times N$ matrix (M = the number of alternatives and N = the number of criteria). The matrix is constructed using the relative importances of the alternatives in terms of each criterion. The vector $(a_{i1}, a_{i2}, a_{i3}, \ldots, a_{iN})$ for each i is the principal eigenvector of an $N \times N$ reciprocal matrix which is determined by pairwise comparisons of the impact of the M alternatives on the ith criterion. Some evidence is presented in (Saaty, [5]) that supports the technique for eliciting numerical evaluations of qualitative phenomena from experts and decision-makers. However, we are not concerned here with the possible advantages and disadvantages of the pairwise comparison and eigenvector methods for determining values for the $a_{ij}$ 's. Instead, we examine the method used in AHP to process the $a_{ij}$ values after they have been determined. The entry $a_{ij}$ , in the $M \times N$ matrix, represents the relative value of the alternative $A_i$ when it is considered in terms of criterion j. In AHP the sum $\sum_{i=1}^{N} a_{ij}$ is equal to one.

According to AHP the best alternative (in the maximization case) is indicated by the following relationship (2):

$$
A _ {\mathrm{AHP}} ^ {*} = \max _ {i} \sum_ {j = 1} ^ {N} a _ {i j} w _ {j} \quad \text { for } \quad i = 1, 2, 3, \dots , M.\tag{2}
$$

The similarity between the WSM and the AHP is clear. The AHP uses relative values instead of actual ones. Thus, it can be used in single- or multi-dimensional decision-making problems.

## 2.4. The Revised Analytic Hierarchy Process

Belton and Gear [1] propose a revised version of the AHP model. They demonstrate that an inconsistency can occur when the AHP is used. A numerical example is presented that consists of three criteria and three alternatives. The indication of the best alternative changes when an identical alternative to one of the nonoptimal alternatives is introduced now creating four alternatives. According to the authors the root for that inconsistency is the fact that the relative values for each criterion sum up to one. Instead of having the relative values of the alternatives $A_{1}$ , $A_{2}$ , $A_{3}$ , ..., $A_{M}$ sum up to one, they propose to divide each relative value by the maximum value of the relative values.

## 3. Evaluation of Decision-Making Methods

The previous four methods appear often in the literature. As it will be seen in this section, however, these methods can give different answers to the same problem. Because only the last three methods are applicable both in single- and multidimensional decision-making, these are the methods that were examined.

Since the truly best alternative is the same regardless of the method chosen, an estimation of the accuracy of each method is highly desirable. The most difficult problem that arises here is how one can evaluate a multi-dimensional decision-making method when the true best alternative is not known. Two criteria are introduced for the above purpose.

The first criterion has to do with the premise that a method that is accurate in multi-dimensional problems should also be accurate in single-dimensional problems. There is no reason for an accurate multi-dimensional method to fail in giving accurate results in single-dimensional problems, since single-dimensional problems are special cases of multi-dimensional ones. Because the first method, the WSM, gives the most acceptable results for the majority of single-dimensional problems, the result of the WSM is used as the standard for evaluating the other three methods in this context.

The second criterion considers the premise that a desirable method should not change the indication of the best alternative when an alternative (not the best) is replaced by another worse alternative (given that the importance of each criterion remains unchanged).

A number of similar criteria could be introduced as well. For example, the fact that an accurate model should not indicate a change in the best alternative after the introduction of identical (or worse) nonoptimal alternatives, could be the basis for other criteria. However, the second criterion is stricter than these criteria and it affects more than one method.

It is important to note here that the testing (using the above two criteria) is sufficient to reveal that a method is ineffective in indicating the best alternative. But, if a method is in fact ineffective, then it is not necessarily true that the above criteria will detect this fact. The following subsections provide examples and present the results obtained from tests of the methods using the first and second criteria, respectively.

## 3.1. Testing the Methods Using the First Criterion

Example 1. Testing the method used by the Analytic Hierarchy Process using the first criterion.

Let us say that the matrix below depicts the actual values, measured in the same units, of the three alternatives $A_{1}$ , $A_{2}$ , and $A_{3}$ , in terms of the three criteria, with the following weights: $w_{1}=8/13$ , $w_{2}=2/13$ , and $w_{3}=3/13$ .

<table><tr><td rowspan="2"></td><td colspan="3">Criterion</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Alter.</td><td>(8/13)</td><td>2/13</td><td>3/13)</td></tr><tr><td> $A_{1}$ </td><td>1</td><td>9</td><td>9</td></tr><tr><td> $A_{2}$ </td><td>5</td><td>2</td><td>2</td></tr><tr><td> $A_{3}$ </td><td>1</td><td>5</td><td>9</td></tr></table>

Applying the WSM it can be shown that the alternative $A_{1}$ is the best one $[A_{1}=A_{WSM}^{*}=53/13]$ .

From the matrix with the actual values we can see that the three $3 \times 3$ matrices with the pairwise comparisons that correspond to this problem are as follows (perfect consistency in the pairwise comparisons is assumed):

$$
\left[ \begin{array}{c c c} 1 & 1 / 5 & 1 / 1 \\ 5 / 1 & 1 & 5 / 1 \\ 1 / 1 & 1 / 5 & 1 \end{array} \right] \left[ \begin{array}{c c c} 1 & 9 / 2 & 9 / 5 \\ 2 / 9 & 1 & 2 / 5 \\ 5 / 9 & 5 / 2 & 1 \end{array} \right] \left[ \begin{array}{c c c} 1 & 9 / 2 & 9 / 9 \\ 2 / 9 & 1 & 2 / 9 \\ 9 / 9 & 9 / 2 & 1 \end{array} \right]
$$

The $M \times N$ (i.e., $3 \times 3$ ) matrix with the relative importances of the alternatives in terms of each criterion that is used in the final step of the AHP is:

<table><tr><td rowspan="2"></td><td colspan="3">Criterion</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Alter.</td><td>(8/13)</td><td>2/13</td><td>3/13)</td></tr><tr><td> $A_{1}$ </td><td>1/7</td><td>9/16</td><td>9/20</td></tr><tr><td> $A_{2}$ </td><td>5/7</td><td>2/16</td><td>2/20</td></tr><tr><td> $A_{3}$ </td><td>1/7</td><td>5/16</td><td>9/20</td></tr></table>

Applying the last step of the AHP it turns out that the alternative $A_{2}$ is the best one $[A_{2}=A_{\mathrm{AHP}}^{*}=0.48]$ . Obviously, this is in contradiction with the conclusion derived using the WSM.

A computer program was written to generate random data and to solve problems with all possible combinations of 3, 5, 7, ..., 21 alternatives and 3, 5, 7, ..., 21 criteria. Thus, 100 different cases

![](/api/attachments/QW85R7MH/fulltext/images/65eb8cbec7b28eb78176d8a07c58a9673166905a1f780251634bf020f98a1aec.jpg)  
Fig. 1. Contradiction rate (%) between the WSM and the AHP.

![](/api/attachments/QW85R7MH/fulltext/images/c659161d778de2c799904c1652fdcd0f9ec14b5232a2eebf4fd93a4168afd376.jpg)  
Fig. 2. Contradiction rate (%) between the WSM and the revised AHP.

were examined. For each case, 10,000 different matrices of values were randomly generated. The problem was solved each time assuming random integer numbers between 1 and 9 as data using the WSM and AHP approaches as in Example 1. That is, the actual values were assumed to be random integers from 1 to 9. This range of values was used because in AHP each pairwise comparison is taken from the set: $\{x/y, where x, y=1,2,3,\ldots,9\}$ (due to the scale that is recommended by the AHP). If there were a contradiction between the two approaches, the program noted that the AHP yielded contradictory results.

In a similar manner, the revised AHP and

Table 1  
Contradiction rate (%) between the WSM and the AHP.

<table><tr><td rowspan="2">Number of alternatives</td><td colspan="10">Number of criteria</td></tr><tr><td>3</td><td>5</td><td>7</td><td>9</td><td>11</td><td>13</td><td>15</td><td>17</td><td>19</td><td>21</td></tr><tr><td>3</td><td>8.2</td><td>10.5</td><td>12.3</td><td>11.7</td><td>12.2</td><td>11.8</td><td>11.8</td><td>12.1</td><td>12.2</td><td>12.5</td></tr><tr><td>5</td><td>8.4</td><td>13.2</td><td>12.6</td><td>13.2</td><td>13.2</td><td>13.5</td><td>13.6</td><td>13.3</td><td>14.0</td><td>13.7</td></tr><tr><td>7</td><td>8.1</td><td>10.1</td><td>12.3</td><td>12.6</td><td>13.3</td><td>13.1</td><td>13.5</td><td>13.1</td><td>14.6</td><td>13.7</td></tr><tr><td>9</td><td>8.5</td><td>9.5</td><td>11.0</td><td>12.5</td><td>12.5</td><td>12.0</td><td>13.0</td><td>13.1</td><td>13.5</td><td>13.2</td></tr><tr><td>11</td><td>7.5</td><td>10.0</td><td>10.9</td><td>12.1</td><td>12.1</td><td>12.3</td><td>12.2</td><td>12.5</td><td>12.8</td><td>13.0</td></tr><tr><td>13</td><td>7.1</td><td>8.5</td><td>10.6</td><td>11.4</td><td>11.7</td><td>11.8</td><td>12.1</td><td>12.0</td><td>13.1</td><td>12.4</td></tr><tr><td>15</td><td>6.6</td><td>8.7</td><td>9.6</td><td>10.6</td><td>11.1</td><td>11.5</td><td>12.0</td><td>12.1</td><td>11.2</td><td>12.4</td></tr><tr><td>17</td><td>6.8</td><td>9.3</td><td>10.1</td><td>10.6</td><td>10.7</td><td>11.1</td><td>11.5</td><td>11.5</td><td>12.0</td><td>11.0</td></tr><tr><td>19</td><td>6.7</td><td>8.1</td><td>9.1</td><td>9.3</td><td>10.7</td><td>10.7</td><td>10.9</td><td>10.9</td><td>11.4</td><td>10.7</td></tr><tr><td>21</td><td>6.0</td><td>7.9</td><td>9.2</td><td>9.6</td><td>10.3</td><td>10.7</td><td>10.8</td><td>10.5</td><td>11.0</td><td>10.9</td></tr></table>

Table 2  
Contradiction rate (%) between the WSM and the revised AHP.

<table><tr><td rowspan="2">Number of alternatives</td><td colspan="10">Number of criteria</td></tr><tr><td>3</td><td>5</td><td>7</td><td>9</td><td>11</td><td>13</td><td>15</td><td>17</td><td>19</td><td>21</td></tr><tr><td>3</td><td>7.4</td><td>8.2</td><td>8.8</td><td>9.6</td><td>10.5</td><td>10.3</td><td>10.9</td><td>10.5</td><td>9.5</td><td>10.6</td></tr><tr><td>5</td><td>5.6</td><td>7.1</td><td>9.3</td><td>8.4</td><td>8.7</td><td>9.1</td><td>8.7</td><td>8.8</td><td>8.8</td><td>9.1</td></tr><tr><td>7</td><td>4.4</td><td>6.3</td><td>6.2</td><td>6.2</td><td>7.7</td><td>6.6</td><td>7.1</td><td>7.6</td><td>8.3</td><td>7.3</td></tr><tr><td>9</td><td>4.2</td><td>4.2</td><td>4.9</td><td>6.9</td><td>7.5</td><td>6.5</td><td>6.2</td><td>6.8</td><td>6.4</td><td>7.6</td></tr><tr><td>11</td><td>3.0</td><td>3.8</td><td>5.6</td><td>4.8</td><td>5.1</td><td>5.4</td><td>6.0</td><td>6.3</td><td>6.0</td><td>6.2</td></tr><tr><td>13</td><td>2.7</td><td>3.3</td><td>3.8</td><td>5.0</td><td>4.5</td><td>4.0</td><td>6.3</td><td>5.3</td><td>5.0</td><td>5.3</td></tr><tr><td>15</td><td>2.2</td><td>3.1</td><td>3.9</td><td>4.4</td><td>3.6</td><td>3.9</td><td>3.4</td><td>4.5</td><td>4.3</td><td>5.3</td></tr><tr><td>17</td><td>1.7</td><td>2.2</td><td>2.6</td><td>3.7</td><td>3.6</td><td>3.8</td><td>3.4</td><td>3.7</td><td>4.2</td><td>4.0</td></tr><tr><td>19</td><td>1.8</td><td>2.7</td><td>2.6</td><td>2.8</td><td>3.1</td><td>3.2</td><td>3.4</td><td>3.5</td><td>3.1</td><td>3.4</td></tr><tr><td>21</td><td>1.4</td><td>1.9</td><td>2.2</td><td>2.2</td><td>2.7</td><td>2.9</td><td>2.5</td><td>2.9</td><td>3.1</td><td>3.0</td></tr></table>

Table 3  
Contradiction rate (%) between the WSM and the WPM.

<table><tr><td rowspan="2">Number of alternatives</td><td colspan="10">Number of criteria</td></tr><tr><td>3</td><td>5</td><td>7</td><td>9</td><td>11</td><td>13</td><td>15</td><td>17</td><td>19</td><td>21</td></tr><tr><td>3</td><td>14.7</td><td>12.7</td><td>12.1</td><td>13.9</td><td>15.3</td><td>14.3</td><td>13.8</td><td>12.6</td><td>13.6</td><td>14.5</td></tr><tr><td>5</td><td>12.0</td><td>14.8</td><td>15.7</td><td>17.0</td><td>17.5</td><td>19.6</td><td>18.9</td><td>17.1</td><td>18.7</td><td>18.1</td></tr><tr><td>7</td><td>12.2</td><td>17.1</td><td>18.7</td><td>18.0</td><td>22.0</td><td>19.5</td><td>19.9</td><td>20.2</td><td>21.8</td><td>20.3</td></tr><tr><td>9</td><td>11.2</td><td>16.5</td><td>18.9</td><td>19.7</td><td>20.9</td><td>21.5</td><td>23.0</td><td>23.4</td><td>21.6</td><td>23.3</td></tr><tr><td>11</td><td>11.8</td><td>17.5</td><td>20.9</td><td>21.3</td><td>21.8</td><td>23.6</td><td>22.9</td><td>22.0</td><td>22.2</td><td>23.0</td></tr><tr><td>13</td><td>11.7</td><td>17.2</td><td>21.1</td><td>20.8</td><td>22.8</td><td>23.4</td><td>24.9</td><td>25.0</td><td>25.7</td><td>25.1</td></tr><tr><td>15</td><td>11.3</td><td>19.5</td><td>19.4</td><td>21.8</td><td>24.9</td><td>24.8</td><td>23.3</td><td>25.0</td><td>26.9</td><td>24.7</td></tr><tr><td>17</td><td>11.2</td><td>17.1</td><td>21.2</td><td>23.3</td><td>23.9</td><td>26.4</td><td>22.5</td><td>25.2</td><td>26.3</td><td>26.2</td></tr><tr><td>19</td><td>11.3</td><td>18.9</td><td>21.3</td><td>22.7</td><td>23.6</td><td>25.7</td><td>25.2</td><td>28.6</td><td>26.9</td><td>27.7</td></tr><tr><td>21</td><td>11.3</td><td>18.2</td><td>21.1</td><td>24.0</td><td>25.4</td><td>26.6</td><td>25.9</td><td>27.5</td><td>26.4</td><td>25.7</td></tr></table>

![](/api/attachments/QW85R7MH/fulltext/images/6f0b1ced85d78e47a5776c4c105c690b104167e07c54ad337a69d0ae89c4f60a.jpg)  
Fig. 3. Contradiction rate (%) between the WSM and the WPM.

WPM were examined. Because at the beginning of this study the purpose was to get a general idea of the contradiction rates, the sample sizes were not determined using the standard deviations of the observations. However, the findings indicate that the sample sizes were satisfactorily large in that the rates of contradiction reached limits numerically. The following figures and tables present the results.

## 3.2. Testing the Methods Using the Second Criterion

Example 2. Testing the method used by the Analytic Hierarchy Process using the second criterion.

Let us say that the following is a matrix of eigenvectors produced by the AHP process. That is to say, the matrix contains relative values for the importance of the alternatives instead of the actual values. Assume the criteria have weights $w_{1}=2/7$ , $w_{2}=2/7$ , and $w_{3}=3/7$ .

Matrix M1

<table><tr><td rowspan="2"></td><td colspan="3">Criterion</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Alter.</td><td>(2/7)</td><td>2/7</td><td>3/7)</td></tr><tr><td> $A_{1}$ </td><td>9/19</td><td>2/12</td><td>2/7</td></tr><tr><td> $A_{2}$ </td><td>5/19</td><td>1/12</td><td>4/7</td></tr><tr><td> $A_{3}$ </td><td>5/19</td><td>9/12</td><td>1/7</td></tr></table>

It can be shown (by multiplying the matrix with the relative importances by the vector with the weights of the 3 criteria followed by normalization) that the priority vector of the alternatives (according to AHP) is (0.305, 0.344, 0.351).

Apparently, the best alternative is $A_{3}$ . If in the above problem the alternative $A_{1}$ (which is not the best one and was defined by the relative values (9/19 2/12 2/7), is replaced by $A_{1}^{\prime}$ which is worse than the original $A_{1}$ , then, the above matrix is modified as follows:

Matrix M2

<table><tr><td rowspan="2"></td><td colspan="3">Criterion</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Alter.</td><td>(2/7)</td><td>2/7</td><td>3/7)</td></tr><tr><td> $A_{1}'$ </td><td>8/18</td><td>1/11</td><td>1/6</td></tr><tr><td> $A_{2}$ </td><td>5/18</td><td>1/11</td><td>4/6</td></tr><tr><td> $A_{3}$ </td><td>5/18</td><td>9/11</td><td>1/6</td></tr></table>

Matrix M1 can be considered as the matrix with the relative values obtained from the following three $3 \times 3$ matrices with pairwise comparisons (perfect consistency in the pairwise comparisons is assumed):

<table><tr><td colspan="3">Criterion 1</td></tr><tr><td>1</td><td>9/5</td><td>9/5</td></tr><tr><td>5/9</td><td>1</td><td>5/5</td></tr><tr><td>5/9</td><td>5/5</td><td>1</td></tr></table>

Matrix M2 has been derived from matrix M1 by substituting the alternative $A_{1}$ with the lesser $A_{1}^{\prime}=8/18\ 1/11\ 1/6)<(9/19\ 2/12\ 2/7)$ . That is to say, instead of 9 it is now 8, instead of 2 it is now 1, instead of 19 it is now 18.

Similarly, the priority vector for matrix M2 is (0.224, 0.391, 0.385). It is clear that now the best alternative is $A_{2}$ .

The last statement is, obviously, in contradiction with the original result namely, that the best alternative is $A_{3}$ . Thus, by introducing a new worse alternative (different from the best one) it is possible to have a change in the indication of the best alternative.

Table 5  
![](/api/attachments/QW85R7MH/fulltext/images/d210b75a5c035251319c3f5c7316597154dd02d411f13f29152152915a495bde.jpg)  
Fig. 4. Rate of change (%) of the indication of the optimum alternative when a nonoptimum alternative is replaced by a worse one. The AHP case.

![](/api/attachments/QW85R7MH/fulltext/images/188d6d176a08c8cbd812a9ebfddd96cc6168578e691a02a00fdc29f144dccbab.jpg)  
Fig. 5. Rate of change (%) of the indication of the optimum alternative when a nonoptimum alternative is replaced by a worse one. The case of the revised AHP.

Table 4  
Rate of change (%) of the indication of the optimum alternative when a nonoptimum alternative is replaced by a worse one. The AHP case.

<table><tr><td rowspan="2">Number of alternatives</td><td colspan="10">Number of criteria</td></tr><tr><td>3</td><td>5</td><td>7</td><td>9</td><td>11</td><td>13</td><td>15</td><td>17</td><td>19</td><td>21</td></tr><tr><td>3</td><td>0.16</td><td>0.26</td><td>0.26</td><td>0.32</td><td>0.30</td><td>0.26</td><td>0.54</td><td>0.28</td><td>0.40</td><td>0.26</td></tr><tr><td>5</td><td>0.34</td><td>0.36</td><td>0.40</td><td>0.54</td><td>0.46</td><td>0.32</td><td>0.32</td><td>0.40</td><td>0.38</td><td>0.42</td></tr><tr><td>7</td><td>0.30</td><td>0.42</td><td>0.42</td><td>0.40</td><td>0.36</td><td>0.40</td><td>0.34</td><td>0.42</td><td>0.16</td><td>0.26</td></tr><tr><td>9</td><td>0.16</td><td>0.36</td><td>0.22</td><td>0.20</td><td>0.22</td><td>0.26</td><td>0.26</td><td>0.26</td><td>0.18</td><td>0.26</td></tr><tr><td>11</td><td>0.14</td><td>0.18</td><td>0.12</td><td>0.24</td><td>0.06</td><td>0.22</td><td>0.48</td><td>0.22</td><td>0.22</td><td>0.20</td></tr><tr><td>13</td><td>0.06</td><td>0.22</td><td>0.22</td><td>0.28</td><td>0.18</td><td>0.24</td><td>0.26</td><td>0.22</td><td>0.08</td><td>0.28</td></tr><tr><td>15</td><td>0.04</td><td>0.10</td><td>0.18</td><td>0.12</td><td>0.22</td><td>0.14</td><td>0.12</td><td>0.10</td><td>0.20</td><td>0.14</td></tr><tr><td>17</td><td>0.08</td><td>0.10</td><td>0.14</td><td>0.24</td><td>0.06</td><td>0.06</td><td>0.10</td><td>0.18</td><td>0.04</td><td>0.08</td></tr><tr><td>19</td><td>0.08</td><td>0.04</td><td>0.10</td><td>0.10</td><td>0.10</td><td>0.12</td><td>0.12</td><td>0.04</td><td>0.08</td><td>0.08</td></tr><tr><td>21</td><td>0.06</td><td>0.10</td><td>0.10</td><td>0.04</td><td>0.08</td><td>0.10</td><td>0.10</td><td>0.10</td><td>0.06</td><td>0.02</td></tr></table>

Rate of change $(\%)$ of the indication of the optimum alternative when a nonoptimum alternative is replaced by a worse one. The case of the revised AHP.

<table><tr><td rowspan="2">Number of alternatives</td><td colspan="10">Number of criteria</td></tr><tr><td>3</td><td>5</td><td>7</td><td>9</td><td>11</td><td>13</td><td>15</td><td>17</td><td>19</td><td>21</td></tr><tr><td>3</td><td>0.50</td><td>0.50</td><td>0.60</td><td>0.30</td><td>0.30</td><td>0.10</td><td>0.00</td><td>0.10</td><td>0.10</td><td>0.10</td></tr><tr><td>5</td><td>0.50</td><td>0.50</td><td>0.80</td><td>0.80</td><td>1.30</td><td>0.80</td><td>0.40</td><td>0.50</td><td>0.50</td><td>0.00</td></tr><tr><td>7</td><td>0.60</td><td>0.60</td><td>1.70</td><td>0.90</td><td>0.80</td><td>0.50</td><td>0.50</td><td>0.50</td><td>0.40</td><td>0.20</td></tr><tr><td>9</td><td>0.70</td><td>0.30</td><td>1.30</td><td>0.80</td><td>0.80</td><td>1.00</td><td>1.10</td><td>0.70</td><td>0.60</td><td>0.20</td></tr><tr><td>11</td><td>0.30</td><td>1.00</td><td>0.60</td><td>1.00</td><td>0.50</td><td>1.10</td><td>0.60</td><td>0.60</td><td>0.80</td><td>0.70</td></tr><tr><td>13</td><td>0.20</td><td>0.60</td><td>1.40</td><td>0.80</td><td>1.20</td><td>1.20</td><td>0.80</td><td>0.80</td><td>0.40</td><td>0.40</td></tr><tr><td>15</td><td>0.30</td><td>0.90</td><td>0.80</td><td>1.20</td><td>0.90</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.90</td></tr><tr><td>17</td><td>0.00</td><td>0.40</td><td>0.80</td><td>0.40</td><td>0.90</td><td>0.80</td><td>0.80</td><td>1.20</td><td>0.50</td><td>0.30</td></tr><tr><td>19</td><td>0.20</td><td>0.10</td><td>0.20</td><td>0.50</td><td>0.80</td><td>1.20</td><td>0.80</td><td>0.60</td><td>1.00</td><td>0.70</td></tr><tr><td>21</td><td>0.10</td><td>0.20</td><td>0.30</td><td>0.40</td><td>0.70</td><td>0.60</td><td>0.70</td><td>0.40</td><td>1.20</td><td>0.60</td></tr></table>

A computer program was written to solve random problems (5,000 trials per case) in a manner similar to Example 2. Again, 100 different cases were examined. Each random problem was solved using the AHP and thereafter replacing one random alternative (not the best) with another worse one in a way similar to Example 2 (i.e., subtracting 1 from both the numerator and denominator).

The cases of the revised AHP and WPM were examined in a similar way. However, it can be shown that the WPM does not yield contradictory results when it is tested in terms of the second criterion because of its structure. The following figures and tables present the results of the above testing. Please note here that the vertical scale has been changed in the following figures in order to better illustrate the impact.

## 4. Explaining the Graphs

In figure 1 the contradiction rate between the WSM and the AHP methods decreases as the number of alternatives increases. This occurs because the quantities $(1/\sum_{i=1}^{N}a_{ij})$ that are used to multiply each entry $a_{ij}$ approach the same value (law of large numbers) as the number N of alternatives increases (the $a_{ij}$ 's are random integer numbers equal to 1, 2, ..., 9). In the WSM each entry can be multiplied by the same quantity without altering the results. Hence, the AHP tends to behave like the WSM as the number of alternatives increases.

Also in the same figure, the contradiction rate increases with the number of criteria. This is true because as M, the number of criteria, increases, the probability that the multipliers $(1/\sum_{i=1}^{N}a_{i,j}\quad j=1,2,3,\ldots,M)$ will deviate significantly increases. Thus, the AHP can differ substantially from the WSM.

In the revised AHP method, the multipliers are the quantities $(1/\max\{a_{ij}, i=1,2,\ldots,N\})$ . As N, the number of alternatives, increases, all of the multipliers tend to the same number (i.e., 9). Since this convergence is very fast, the AHP approaches the WSM very quickly (figure 2).

The number of criteria plays exactly the same role in the revised AHP as in the original AHP. The only difference is that the contradiction rates are smaller, because the multipliers are not as different as in the original AHP.

Figure 3 shows the contradiction rate for the WPM case. In order to get an understanding of the shape of the graph in, we consider the simple case where all the criteria are of the same importance. For the purposes of figure 3, we can view the WSM not in matrix form but instead, we consider only two alternatives at a time (as we do with the WPM). Now, we can see that if one entry $a_{ij}$ is very different from the rest, it causes more impact in the WPM (since it multiplies or divides a sequence of terms) than in the WSM (where it has only an additive effect). The more criteria that are involved the more likely it is that this phenomenon will take place. This is why the rates in figure 2 increase with the number of criteria.

This reasoning is also true as the number of alternatives (see also table 3). Hence, the contradiction rate increases with the number of alternatives.

The rate of change (\%), of the indication of the optimum alternative when a nonoptimum alternative is replaced by a worse one (for the AHP case), does not depend on the number of criteria as seen in figure 4. This occurs because, for every criterion, the same constant value $(-1)$ was used to alter the nonoptimal alternative. It is expected (although not tested) that if the $a_{ij}$ were to be changed by a random number not a constant value $(-1)$ , the contradiction rate would be dependent on the number of criteria. Because the constant value $(-1)$ was used the bias, if any, would be in favor of the original AHP over the revised AHP.

However, the role of alternatives is a critical one. When N, the number of alternatives, increases the role of the multipliers $(1/\sum_{i=1}^{N}a_{ij})$ is more critical than the impact of replacing a nonoptimal alternative by a worse one. Since the number of alternatives overrides the role of the previous replacements the rates in figure 4 decrease as the number of alternatives increases.

Finally, figure 5, for the revised AHP, illustrates that the rate of change of the indication of the optimal alternative when a nonoptimal alternative is replaced by a worse one decreases as the number of alternatives increases. This occurs because as the number of alternatives increases the multipliers $(1/\max\{a_{ij}, i=1,2,\ldots,N\})$ becomes closer to 9 (i.e., the max) and thus the altered alternative still remains nonoptimal. As in the previous paragraph, as the number of criteria increases there is greater chance that the multipliers will differ substantially and alternative changes will have greater impact.

Because in the revised AHP the multipliers (i.e., the quantities $(1/\max\{a_{ij}, i=1,2,\ldots,N\})$ are more stable than the corresponding ones of the original AHP the revised AHP performs better in terms of the first evaluative criterion. This is not the case when the second evaluative criterion is used. However, now the difference in the rates does not seem to be so dramatic.

## 5. Conclusions

The previous analyses make it clear that none of the decision-making methods reviewed is perfectly effective in terms of both evaluative criteria. The results that were obtained by testing the methods using the two criteria indicate that the models yield different rates of contradiction.

The findings of the analyses are summarized in table 6. This presents the structure of the typical decision-making problem with which this study is concerned and illustrates the decision-making paradox. In this table, decision-making methods are treated as alternatives and the two evaluative criteria as the criteria of the problem. The two criteria are considered in terms of cases with 3 alternatives and 3 criteria, 3 alternatives and 5 criteria, 3 alternatives and 7 criteria, and so forth. Thus, 100 subcriteria are generated per criterion. The numbers $w_{1}$ and $w_{2} = 100 - w_{1}$ , where $w_{1} = 1, 2, 3, \ldots, 100$ , are assumed to be the relative weights of the two criteria. The relative weights of the first 100 subcriteria are assumed to be $w_{1}/100$ and for the last 100 subcriteria $w_{2}/100$ .

![](/api/attachments/QW85R7MH/fulltext/images/6d1a6fbae62893e523d1664a046cb36df874f75fa4ea61778ef09d7cc8da142e.jpg)  
Fig. 6. Indication of the best method according to different approaches.

Since it is not clear which method is the best, the problem of selecting the best decision-making method was solved using successively the WSM, the AHP, and the revised AHP. The occurrence of zeros in table 6 made the applicability of the WPM difficult (divisions by zeros). Thus, the WPM was not considered for solving the problem. Figure 6 presents the results for different weights $w_{1}$ and $w_{2}$ .

Table 6
Summary of the findings.

<table><tr><td rowspan="2"></td><td colspan="10">Criterion</td></tr><tr><td></td><td>1</td><td></td><td></td><td></td><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="11">Cases with</td></tr><tr><td>Number of alter.</td><td>3</td><td>3</td><td>3</td><td>...</td><td>21</td><td>3</td><td>3</td><td>3</td><td>...</td><td>21</td></tr><tr><td>Number of criter.</td><td>3</td><td>5</td><td>7</td><td>...</td><td>21</td><td>3</td><td>5</td><td>7</td><td>...</td><td>21</td></tr><tr><td>Subcriterion</td><td>1</td><td>2</td><td>3</td><td>...</td><td>100</td><td>101</td><td>102</td><td>103</td><td>...</td><td>200</td></tr><tr><td colspan="11">Method</td></tr><tr><td>WPM</td><td>14.7</td><td>12.7</td><td>12.1</td><td>...</td><td>25.7</td><td>0</td><td>0</td><td>0</td><td>...</td><td>0</td></tr><tr><td>AHP</td><td>8.2</td><td>10.5</td><td>12.3</td><td>...</td><td>10.9</td><td>0.16</td><td>0.26</td><td>0.26</td><td>...</td><td>0.02</td></tr><tr><td>rev. AHP</td><td>7.4</td><td>8.2</td><td>8.8</td><td>...</td><td>3.0</td><td>0.50</td><td>0.50</td><td>0.50</td><td>...</td><td>0.60</td></tr></table>

Because the number of criteria in a decision-making problem is seen to play a critical role, this number is considered in the final phase of the evaluation of the three decision-making methods. In the horizontal axis of figure 6, we consider for each method the cases of having only 3, 5, 7, ..., 21 criteria in a decision-making problem (as we do in table 6). Since in table 6 all values are presented in the same units (the numbers represent percentages), the WSM is the method that, when used to choose between, WPM, AHP, and revised AHP, would yield the most reliable answer to the problem of choosing the most effective decision-making method.

The first column in the chart of figure 6 represents the evaluation derived by using the WSM. That chart suggests that the revised AHP appears to be the best method over a wide range of different combination of weights $w_{1}$ and $w_{2}$ . Only for $w_{1}$ less than 10 per cent the revised AHP is not the best method. For $w_{1}$ less than 10 and above 3 per cent the AHP appears to be superior than the others, while for $w_{1}$ less than 3 per cent the WPM becomes the best method.

The charts that correspond to the results, summarized in table 6, by using the AHP or the revised AHP, appear to be of the same shape. From figure 6 we can conclude generally that as $w_{1}$ increases WPM is replaced by the AHP then by the revised AHP as the best method. This probably happens because both methods behave in the same way for problems with 100 criteria and 3 alternatives (as is the case in table 6). However, both methods recommend the WPM to be the best and not themselves! They also recommend the revised AHP to be second best approach, while the original AHP is the better one only for a very small portion of combinations of weights $w_{1}$ and $w_{2}$ . The same figure also suggests that the number of criteria in a given decision-making problem is critical in deriving which method appears to be the best. Although almost all the columns in figure 6 indicate that the influence of this number is consistent a regular behavior cannot be established.

The above study, with the findings summarized in figure 6, demonstrates that it is impossible to determine precisely the best decision-making method, for to do so one needs to use the best decision-making method! This problem of finding the best decision-making method always reaches a Decision-Making Paradox which makes any attempt in solving this problem to be of limited success. However, the results of this study recommend that for most of the cases of different weights of the two evaluative criteria the revised AHP appears to be the best decision-making method of the four examined, while the original AHP, appears to be the most inaccurate one.

## References

[1] Belton, V., and T. Gear, On a Short-coming of Saaty's Method of Analytic Hierarchies, Omega, pp. 228–230, December 1983.

[2] Bridgman, P.W., Dimensional Analysis, Yale University Press, New Haven, 1922.

[3] Fishburn, P.C., Additive Utilities with Incomplete Product Set: Applications to Priorities and Assignments, Operations Research, 1967.

[4] Miller, D.W., and M.K. Starr, Executive Decisions and Operations Research, Prentice-Hall, Inc., Englewood Cliffs, New Jersey, 1969.

[5] Saaty, T.L., The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[6] Triantaphyllou, E., Evaluation of Alternatives in Single and Multi-Dimensional Decision-Making Problems, Masters thesis, The Pennsylvania State University, 1985.
