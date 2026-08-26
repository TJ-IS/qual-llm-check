---
otero_id: 19580
otero_key: "MCC4FB6N"
title: "A three-level-similarity measuring method of participant opinions in multiple-criteria group decision supports"
authors: "Jun Ma; Jie Lu; Guangquan Zhang"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.10.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A three-level-similarity measuring method of participant opinions in multiple-criteria group decision supports

Jun Ma <sup>a,b,</sup>⁎, Jie Lu <sup>b,</sup>⁎⁎, Guangquan Zhang b

<sup>a</sup> SMART Infrastructure Facility, Faculty of Engineering and Information Sciences, University of Wollongong, Northfields Ave, Wollongong, NSW 2522, Australia <sup>b</sup> DeSI Lab, Centre for QCIS, School of Software, Faculty of Engineering and IT, University of Technology, Sydney (UTS), NSW 2007, Australia

## a r t i c l e i n f o

Article history: Received 22 June 2011 Received in revised form 21 October 2013 Accepted 22 October 2013 Available online 1 November 2013

Keywords: Multi-criteria group decision making Opinion similarity Measuring method Aggregation operator Opinion analysis

## a b s t r a c t

Measuring opinion similarity between participants is an important strategy to reduce the chance of making and applying inappropriate decisions in multi-criteria group decision making applications. Due to the small-sized opinion data and the varieties of opinion representations, measuring the similarity between opinions is dif<sup>fi</sup>cult and has not been well-studied in developing decision support. Considering that the similarity changes with the number of concerned criteria, this paper develops a gradual aggregation algorithm and establishes a three-levelsimilarity measuring (TLSM) method based on it to measure the opinion similarity at the assessment level, the criterion level and the problem level. Two applications of the TLSM method on social policy selection and energy policy evaluation are conducted. The study indicates that the TLSM method can effectively measure the similarity between opinions in small-size with possibly missing values and simulate the dynamic generation of a decision.

© 2013 Elsevier B.V. All rights reserved

## 1. Introduction

Multiple-criteria group decision making (MCGDM) is recognized as an ef<sup>fi</sup>cient strategy in many organizational decision problems [14,22], where a <sup>fi</sup>nal decision is made based on the opinions of individual participants. Overly similar opinions increase the chance of putting an inappropriate decision into effect. In practice, making an appropriate decision is already a time-consuming and costly task; however, tuning an inappropriate decision will cost even more. To reduce this risk, measuring opinion similarity between participants (MOSP) in advance is an important issue in developing decision support for essential decision problems.

Opinion similarity is used in many <sup>fi</sup>elds such as on-line recommender systems [1,31]. However, the MOSP problem is still an unsolved and challenging issue. Dif<sup>fi</sup>culties in solving the MOSP problem include the effective processing of small-size opinion data and the varied opinion representations. Due to the restrictions on time, cost, private policies, and other issues, a decision is often made on small sized opinion data of a limited number of participants. Even though all participants would like to express their opinions thoroughly in an ideal situation, the small-size opinion data makes it very hard to apply methods for large-size data in solving the MOSP problem. Varied opinion representation is another dif<sup>fi</sup>culty in solving the MOSP problem. Participants prefer to express their opinions in their own ways based on their understandings of and experiences in a given topic. However, this is bound to dif<sup>fi</sup>culties for measuring the similarity between their opinions. A strategy commonly used to regulate opinion representation is providing a <sup>fi</sup>xed number of choices, for example, some prede<sup>fi</sup>ned linguistic terms or a set of ordinal numbers [9,15,22]. However, this cannot completely avoid varied opinion representations because the prede<sup>fi</sup>ned choices may have different semantics for different persons and for different evaluation criteria.

Keeping the aforementioned dif<sup>fi</sup>culties in mind, this paper presents a three-level-similarity measuring (TLSM) method to solve the MOSP problem based on three assumptions: 1) Given a criterion, if the opinions of two participant are similar for the majority of options, then they are similar; 2) Given a set of criteria, if the opinions of two participants are similar for the majority of important criteria, then they are similar; and 3) Given a decision problem, if the opinions of two participants produce a similar decision, then they are similar.

The rest of the paper is organized as follows. Section 2 reviews related works in opinion analysis, similarity measurement and aggregation operations. Section 3 develops a gradual aggregation algorithm (GAA) which is used to generate an overall opinion similarity. In Section 4, we introduce the TLSM method in detail. Section 5 illustrates two case studies in social policy selection and energy policy evaluation

Table 2

problems. Section 6 summarizes the main contributions of the work and future study plans.

## 2. Related works

Opinion analysis is extensively studied in social psychology <sup>fi</sup>elds [2]; recently, requirements for effectively extracting, summarizing, and segmenting opinions of general or speci<sup>fi</sup>c users boosted the growing research on opinion mining and sentiment analysis [13,25,27]. Many opinion mining systems have been developed and applied [7,25,28]. However, these methods are not suitable for the MOSP problem because of the aforementioned dif<sup>fi</sup>culties. In the MCGDM <sup>fi</sup>eld, study of opinion analysis is conducted in two main areas. Qualitative studies analyze and simulate the behavior patterns of peoples based on their opinions of a considered affair [21,24]. Quantitative research focuses on how to represent and process opinions in a computational framework [9,26]. For instance, fuzzy sets and fuzzy logic are widely used as opinion representation and process facilities [8,10] because they can effectively interpret and model the subjective information with uncertainties. These computation-based techniques provide support to develop solutions for the MOSP problem.

Similarity measurement is widely studied in human knowledge representation, behavior analysis, and real-world problem solving [30,11,12]. Generally speaking, a similarity metric can be derived from a distance metric. The Euclidean metric, the absolute value metric, and the Chebyshev metric are commonly used. Noting that the majority of existing similarity metrics will ultimately produce a crisp numeric value, which cannot suf<sup>fi</sup>ciently depict the fuzziness in real cases, Chakraborty and Chakraborty [6] de<sup>fi</sup>ned a similarity metric whose value is a fuzzy set and implemented a clustering algorithm to solve a group decision making problem.

Using aggregation to integrate evaluations of individual participants is a crucial step to develop a solution for an MCGDM problem. According to whether or not an aggregation operator explicitly considers the relevant importance (weights) of the evaluation criteria, three main types of aggregation operators are used in MCGDM research. The <sup>fi</sup>rst type treats all evaluation criteria equally. Typical examples include the arithmetic mean, the geometric mean, and the t-norms (or t-conorms) [4,5]. The second type explicitly distinguishes the weights of the evaluation criteria either by their impacts on the decision problem, or by their processing order. The weighted mean and the ordered weighted aggregation (OWA) [29], as well as their extensions [18,19] belong to this type. A third type is de<sup>fi</sup>ned by certain integral theories, such as the Sugeno and Choquet integrals [16,17,20]. Currently existing aggregation operators in MCGDM research often assume that the inputs are complete and simply ignore any missing values when generating an aggregation result. This assumption is not consistent with the realities of applications. How to process missing values is, therefore, a key concern when applying an aggregation operator; but this issue has not yet been solved. Although so many powerful aggregation operators have been presented, little is known about how to select an appropriate one in real applications. Beliakov [3] reported a solution by using the mathematical programming technique to adjust the parameters of a form-<sup>fi</sup>xed aggregation operator.

![](/api/attachments/MCC4FB6N/fulltext/images/6a56d4495a7500986258012cdfd729345f2fdff2512265b664b70718dbfb5d12.jpg)  
Fig. 1. Changing weights with the number of inputs.

Table 1  
An example for processing a missing value

<table><tr><td rowspan="2">No.</td><td rowspan="2">Input</td><td>S1</td><td colspan="2">S2</td><td colspan="4">S3</td></tr><tr><td>OGA</td><td>DM</td><td>OGA-DM</td><td>IM-0</td><td>OGA-0</td><td>IM-M</td><td>OGA-M</td></tr><tr><td>1</td><td>0.840</td><td>0.840</td><td>0.840</td><td>0.840</td><td>0.840</td><td>0.840</td><td>0.840</td><td>0.840</td></tr><tr><td>2</td><td>0.783</td><td>0.812</td><td>0.912</td><td>0.876</td><td>0.000</td><td>0.420</td><td>0.549</td><td>0.694</td></tr><tr><td>3</td><td>0.912</td><td>0.845</td><td>0.335</td><td>0.696</td><td>0.912</td><td>0.584</td><td>0.912</td><td>0.767</td></tr><tr><td>4</td><td>0.335</td><td>0.718</td><td>0.278</td><td>0.591</td><td>0.335</td><td>0.522</td><td>0.335</td><td>0.659</td></tr><tr><td>5</td><td>0.278</td><td>0.630</td><td>0.477</td><td>0.568</td><td>0.278</td><td>0.473</td><td>0.278</td><td>0.583</td></tr><tr><td>6</td><td>0.477</td><td>0.604</td><td>0.365</td><td>0.535</td><td>0.477</td><td>0.474</td><td>0.477</td><td>0.565</td></tr><tr><td>7</td><td>0.365</td><td>0.570</td><td>0.952</td><td>0.594</td><td>0.365</td><td>0.458</td><td>0.365</td><td>0.537</td></tr><tr><td>8</td><td>0.952</td><td>0.618</td><td>0.636</td><td>0.599</td><td>0.952</td><td>0.520</td><td>0.952</td><td>0.588</td></tr><tr><td>9</td><td>0.636</td><td>0.620</td><td>0.142</td><td>0.549</td><td>0.636</td><td>0.533</td><td>0.636</td><td>0.594</td></tr><tr><td>10</td><td>0.142</td><td>0.572</td><td></td><td></td><td>0.142</td><td>0.494</td><td>0.142</td><td>0.549</td></tr><tr><td>Result</td><td>0.572</td><td>0.683</td><td>0.549</td><td>0.650</td><td>0.494</td><td>0.532</td><td>0.549</td><td>0.638</td></tr></table>

Suppose the second input 0.783 (bold) is missing, the IM-o method uses 0.000 (underlined) for it and the IM-M method uses the mean (0.549, underlined) of the other nine inputs for it. Row “Result” shows the results (bold) of different methods in the three scenarios, respectively.

## 3. A gradual aggregation algorithm

## 3.1. Motivations and implementations

Two practical issues are commonly faced in an MCGDM problem. The <sup>fi</sup>rst one is how to handle missing values. The other issue is how to generate a decision dynamically which refers to the procedure of making the <sup>fi</sup>nal decision from a sketched one based on a few number of criteria at the initial stage and then amending it in the following stages by considering more criteria added gradually. To solve these two issues, this section develops a gradual aggregation algorithm (GAA) which is implemented in two ways, i.e., the ordinary gradual aggregation (OGA) and the weighted gradual aggregation (WGA). The difference between them is that the OGA does not explicitly process the criteria weights but leaves it to the aggregation operator; while the WGA does.

Following the notations in [5], aggregation operator <sub>A</sub> over a closed set X is denoted by $\mathcal { A } : \cup _ { i \in \mathbb { N } ^ { + } } \{ A _ { i } : X ^ { i } {  } X \}$ where $A _ { i }$ is called the i-ary aggregation operator in . For convenience, let X be a closed subset of ℝ.

De<sup>fi</sup>nition 3.1. Let <sub>A</sub> and ℬ be two aggregation operators. A mapping $G _ { n }$ from $X ^ { n }$ to X is called an n-ary ordinary gradual aggregation (OGA) with respect to <sub>A</sub> and ℬ:

$$
G _ {n} (x _ {1}, \dots , x _ {n}) = B _ {n} (\{A _ {i} (x _ {1}, \dots , x _ {i}), i = 1, \dots , n \}).
$$

Outline of main processes in the TLSM method.

<table><tr><td>Process level</td><td>Main steps</td></tr><tr><td>Assessment</td><td>Input: two experts&#x27; evaluation reports; evaluation term set  $T_j$ Output: the similarity about criterion  $c_j$ 1.1 Determine a similarity matrix for evaluation terms for criterion  $c_j$ ;1.2 Determine a clustering algorithm;1.3 Generate semantic-equal groups by the clustering algorithm;1.4 Calculate similarity between two opinions for criterion.</td></tr><tr><td>Criterion</td><td>Input: the similarity at the assessment level and weights of criteriaOutput: similarity with respect to each criterion against the criteria set2.1 Identify a similarity utility function  $u_j$  of each criterion;2.2 Calculate similarity with respect to criterion  $c_j$  by  $u_j$ .</td></tr><tr><td>Problem</td><td>Input: similarities obtained at the criterion levelOutput: similarity between two opinions3.1 Construct the GAA from a pair of aggregation operators;3.2 Calculate the similarity between opinions using the GAA.</td></tr></table>

De<sup>fi</sup>nition 3.2. Let and ℬ be two aggregation operators; w the weight of input $x _ { i } , i = 1 , . . . , n . A$ mapping $G _ { n . }$ from $X ^ { n }$ to X is called an n-ary weight ed gradual aggregation (WGA) with respect to <sub>A</sub> and ℬ:

$$
G _ {n} (x _ {1}, \dots , x _ {n}; w _ {1}, \dots , w _ {n}) = B _ {n} (\{A _ {i} (x _ {1}, \dots , x _ {i}; w _ {1}, \dots , w _ {i}), i = 1, \dots , n \}).
$$

The OGA and the WGA inherit some properties of <sub>A</sub> and ℬ which are given below. These properties indicate that the OGA and the WGA can be used to implement aggregation procedure.

Proposition 3.1. If both <sub>A</sub> and ℬ are idempotent, so do OGA and WGA.□

Proposition 3.2. If both <sub>A</sub> and ℬ are monotonic, so do OGA and WGA.□

Proposition 3.3. If both <sub>A</sub> and ℬ are bounded, so do OGA and WGA.□

3.2. Weights assignment and adjustment

Although it does not explicitly process the weights of criteria, the OGA assigns implicitly a set of weights to its inputs based on their processing orders when both <sub>A</sub> and ℬ are arithmetic means. Suppose the inputs $x _ { 1 } , . . . , x _ { 1 }$ are indexed by their processing orders, whose weights are not given. Then by the OGA, we have

$$
A _ {i} (x _ {1}, x _ {2}, \dots , x _ {i}) = \frac {x _ {1} + x _ {2} + \dots + x _ {i}}{i}, \quad i = 1, \dots , n
$$

and

$$
G _ {n} \left(x _ {1}, \dots , x _ {n}\right) = \frac {\sum_ {i = 1} ^ {n} A _ {i} \left(x _ {1} , \dots , x _ {i}\right)}{n} = \sum_ {i = 1} ^ {n} x _ {i} \left(\frac {1}{n} \sum_ {j = i} ^ {n} \frac {1}{j}\right).\tag{1}
$$

Let $\beta _ { i }$ be the coef<sup>fi</sup>cient of x in Eq. (1), i.e., $\begin{array} { r } { \beta _ { i } = \frac { 1 } { n } { \sum _ { j = i } ^ { n } } \frac { 1 } { j } , i = 1 , . . . , n . } \end{array}$ The sum of $\beta _ { i } s$ is

$$
\beta_ {1} + \beta_ {2} + \dots + \beta_ {n} = 1,\tag{2}
$$

and the order of β s is

$$
\beta_ {1} > \beta_ {2} > \dots > \beta_ {n} > 0.\tag{3}
$$

Eq. (2) shows that $\beta _ { i } , . . . , \beta _ { n }$ form a set of weights and are assigned to the inputs implicitly. Eq. (3) indicates that the input processed earlier gains a larger weight. Intuitively, this weight assignment result is consistent with a real decision procedure where the most important criteria are often processed preferentially.

Furthermore, these assigned weights change their values with the number n of inputs. Fig. 1 illustrates changes of the <sup>fi</sup>rst <sup>fi</sup>ve assigned weights when $n \leq 1 8 .$ . It shows that each $\beta _ { i }$ is convergent with the increase of n. A conclusion is drawn from this observation that, given a larger n, the newly added inputs will exert little impact on a sketchy decision. Since the parameter n in a real problem cannot be too large, the impacts of the most important criteria corresponding to the inputs–which are processed preferentially–are therefore strengthened.

![](/api/attachments/MCC4FB6N/fulltext/images/784a5acdd709b0fb6b63aadd1c41ad436950c4d9aaaa6a97c46fca53f1dff30d.jpg)  
a) Linguistic assessmentsi n Munda’s method.  
Fig. 2. Semantic of linguistic terms.

Table 3  
Linguistic weight, numeric feature, parameter of the SUF of a criteria.

<table><tr><td> $wc_j$ </td><td>VH</td><td>FH</td><td>M</td><td>RL</td><td>VL</td></tr><tr><td>NF</td><td>0.9</td><td>0.767</td><td>0.5</td><td>0.233</td><td>0.1</td></tr><tr><td> $f(NF)$ </td><td>1.800</td><td>1.534</td><td>1</td><td>0.466</td><td>0.200</td></tr></table>

Compared with the OGA, the WGA can explicitly adjust the initially assigned weights of the inputs in its aggregation procedure. By replacing $A _ { i }$ with the weighted mean, and supposing the initial weight of input x<sub>i</sub> is $w _ { i } ,$ we have

$$
A _ {i} (x _ {1}, \dots , x _ {i}; w _ {1}, \dots , w _ {i}) = \frac {w _ {1}}{\sum_ {j = 1} ^ {i} w _ {j}} x _ {1} + \dots + \frac {w _ {i}}{\sum_ {j = 1} ^ {i} w _ {j}} x _ {i}, \quad i = 1, \dots , n
$$

and

$$
G _ {n} (x _ {1}, \dots , x _ {n}; w _ {1}, \dots , w _ {n}) = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} w _ {i} \left(\sum_ {k = i} ^ {n} \frac {1}{\sum_ {j = 1} ^ {k} w _ {j}}\right).
$$

Let $\cdot \beta _ { i }$ be the coef<sup>fi</sup>cient of x , i.e., $\begin{array} { r } { \mathrm { , } \beta _ { i } = \frac { w _ { i } } { n } { \sum _ { k = i } ^ { n } } \frac { 1 } { { \sum _ { j = 1 } ^ { k } } w _ { j } } , i = 1 , . . . , n . } \end{array}$ . Then we have

$$
\beta_ {1} + \beta_ {2} + \dots + \beta_ {n} = 1,\tag{4}
$$

$\mathrm { i . e . , } \beta _ { 1 } , \beta _ { 2 } , . . . , \beta _ { \mathrm { { n } } }$ form a set of weights and the inputs are re-weighted by them. Comparing $\beta _ { \mathrm { i } }$ and $w _ { i } ,$ we have a loose inequity that

$$
\beta_ {i} \geq \frac {n - (i - 1)}{n} w _ {i}, \quad i = 1, \dots , n.\tag{5}
$$

Further analysis indicates that $\beta _ { 1 } \geq w _ { 1 }$ and if n is larger enough and i is smaller, the <sup>fi</sup>rst several $\beta _ { 1 } s$ are very near to, even greater than, the initial w s. This means the impacts of the corresponding criteria are still preserved by the WGA.

The above algorithm and discussions indicate that the GAA can effectively maintain the impacts of important criteria that are very important feature for making decisions dynamically and processing missing values.

## 3.3. Dynamic decision and missing values

The processing order of the inputs emphasized in the GAA is closely related to the dynamic generation of a decision and process of missing values.

![](/api/attachments/MCC4FB6N/fulltext/images/d87b9e898c9cabe9bed3c3bf3be2f9921d4e22e3932dc8f9247f310b0615969c.jpg)  
b) Linguistic weightsin Case 2.

An illustrative example of social impact matrix.

<table><tr><td rowspan="2">Social actors</td><td colspan="7">Policy options</td></tr><tr><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_4$ </td><td> $a_5$ </td><td> $a_6$ </td><td> $a_7$ </td></tr><tr><td> $b_1$ </td><td>Very good</td><td>Good</td><td>Moderate</td><td>bad</td><td>Fairly good</td><td>Fairly bad</td><td>Very bad</td></tr><tr><td> $b_2$ </td><td>Very good</td><td>Good</td><td>Moderate</td><td>Bad</td><td>Fairly good</td><td>Very bad</td><td>Very bad</td></tr><tr><td> $b_3$ </td><td>Very bad</td><td>Fairly bad</td><td>Moderate</td><td>Good</td><td>Very good</td><td>Good</td><td>Moderate</td></tr><tr><td> $b_4$ </td><td>Very bad</td><td>Fairly bad</td><td>Fairly bad</td><td>Good</td><td>Fairly good</td><td>Good</td><td>Very good</td></tr><tr><td> $b_5$ </td><td>Very bad</td><td>Bad</td><td>Fairly bad</td><td>Moderate</td><td>Fairly good</td><td>Good</td><td>Very good</td></tr><tr><td> $b_6$ </td><td>Very bad</td><td>Good</td><td>Bad</td><td>Good</td><td>Good</td><td>Good</td><td>Very good</td></tr></table>

When making a decision, there is a natural processing order in the considered criteria, i.e., the most important criteria are often considered preferentially, then the secondary important criteria, and <sup>fi</sup>nally the not so important criteria. Similarly, as shown in Section 2, the GAA implementations can assign (reassign) a set of decreasingly changed weights to the inputs according to their processing orders. In this sense, the GAA implementations are models of the generation of a dynamic decision.

Two intuitive strategies to handle missing values are: 1) completely discard them; or 2) try to impute them. The GAA implementations can partially combine these. When the parameter n in GAA is smaller than the total number of inputs, some inputs will not be considered naturally. Obviously, if missing values exist in the unprocessed inputs; these missing values have no effect on the obtained aggregation result. However, if the missing values exist for some key criteria; in this situation, the GAA can partially impute the missing values through using <sub>A</sub> to calculate a set of candidate results by slightly assigning or adjusting the weights of those inputs and using the aggregation operator ℬ to generate an aggregation. To illustrate this procedure, let us consider the example below.

Example 3.1. For illustrative purpose, suppose 10 inputs are given (the second column in Table 1) and the aggregation algorithm used is the arithmetic mean. We compare three scenarios: (S1) no missing value; (S2) ignore missing value; and (S3) replace the missing value with 0 and the mean of the others.

For (S1), the aggregation result without using the OGA is 0.572 (column “Input”); while it is 0.683 (column “OGA”) with the OGA, where <sub>A</sub> and ℬ are both the arithmetic means, and the third column in Table 1 shows the intermediate results of using it. For (S2), the aggregation result without using the OGA is 0.549 (column “DM”); while it is 0.650 by using the OGA (column “OGA–DM”). For (S3), the aggregation results without using the OGA are 0.494 and 0.549 for replacing the missing value by 0 (column “IM-0”) and the mean of the others (column “IM-M”), respectively; while they are 0.532 (column “OGA-0”) and 0.638 (column “OGA-M”) by using the OGA, respectively.

If taking (S1) as benchmark, we noted that the OGA generates a result with bigger difference from the benchmark than the other methods. This fact indicates that the OGA pays more attention on the missing value.

## 4. A three-level-similarity measuring method for the MOSP problem

## 4.1. The MOSP problem

An MOSP problem is brie<sup>fl</sup>y addressed as follows: given an MCGDM problem with a set of candidate options, the participants evaluate them in terms of a set of evaluation criteria and everyone completes a report containing evaluations summarized in linguistic terms; after collecting these evaluation reports, a question arises: can we identify which two participants have similar opinions based on the collected evaluation reports?

For convenience of discussion, we use $O = \{ o _ { i } | i \in I \}$ for the candidate options, $C = \{ c _ { j } | j \in J \}$ for the evaluation criteria, and $E = \{ e _ { k } | k \in K \}$ for the participants. The evaluation report from participant $e _ { k }$ is denoted by a matrix $V _ { k } = ( \nu _ { i j } ) _ { I \times J } ,$ where $\nu _ { i j }$ is the evaluation (i.e., opinion) on option o about criterion cj. $\nu _ { i j }$ is either an element in T which is the collected linguistic terms used for criterion $c _ { j } ,$ or a blank for “not available” or “no answer”, or a question mark for “unclear”. Without loss of generality, we suppose that each participant provides only one term for each option about each criterion.

## 4.2. Overview of the TLSM method

The outline of the TLSM method is shown in Table 2. By this method, the similarity of two participants' opinions will be measured at three sequential levels, i.e., the assessment level, the criterion level, and the problem level.

At the assessment level, the evaluations of two participants are compared option by option in terms of a given criterion. The comparison is conducted based on the assumption that the more candidate options on which two participants have similar evaluations, the higher similarity of their opinions is. To determine whether two evaluations are similar or not, the TLSM method compares their semantics: two opinions are said to be similar (or have similar semantics) if they are represented by terms in the same semantic-equal group which is built through pairwisely comparing semantics of all terms used. By the option-by-option comparison conducted on the two participants' evaluations, how similar of the two participants' opinions is known on a given criterion. The similarity is proportional positively to the number of options with similar evaluations against the total number of options.

At the criterion level, the different impacts (weights) of evaluation criteria are further considered. The TLSM method de<sup>fi</sup>nes for each criterion a similarity utility function (SUF) based on its weight against those of other criteria. An SUF is proportional positively to similarity obtained at the assessment level and is proportional inversely to the weights of criteria. The SUF is used to emphasize that similarity of preferential criterion is more important than non-preferential criterion. Based on these SUFs, we can measure to what extent the two participants have similar opinions on each given criterion against a set of criteria.

At the problem level, the similarity is measured using the GAA. The GAA takes the similarities obtained at the criterion level as inputs and re-orders them according to the decreasing-ordered weights of the corresponding criteria. The aggregation algorithm will generate a set of candidate values of the overall similarity of two participants' opinions at the <sup>fi</sup>rst stage, and then derives the overall similarity from them at the second stage. The obtained overall similarity indicates to what extent the two participants have similar opinions on a decision problem.

Similarity matrix between six social actors.

<table><tr><td></td><td> $b_1$ </td><td> $b_2$ </td><td> $b_3$ </td><td> $b_4$ </td><td> $b_5$ </td><td> $b_6$ </td></tr><tr><td> $b_1$ </td><td>1</td><td>0.729</td><td>0.426</td><td>0.399</td><td>0.403</td><td>0.403</td></tr><tr><td> $b_2$ </td><td>0.729</td><td>1</td><td>0.410</td><td>0.386</td><td>0.390</td><td>0.390</td></tr><tr><td> $b_3$ </td><td>0.426</td><td>0.410</td><td>1</td><td>0.675</td><td>0.584</td><td>0.569</td></tr><tr><td> $b_4$ </td><td>0.399</td><td>0.386</td><td>0.675</td><td>1</td><td>0.729</td><td>0.672</td></tr><tr><td> $b_5$ </td><td>0.403</td><td>0.390</td><td>0.584</td><td>0.729</td><td>1</td><td>0.595</td></tr><tr><td> $b_6$ </td><td>0.403</td><td>0.390</td><td>0.569</td><td>0.672</td><td>0.595</td><td>1</td></tr></table>

![](/api/attachments/MCC4FB6N/fulltext/images/6ba2a115c46cd9f81eecdcc0fc3d97d3567fbcfbbb6209d4027353e978dd74c2.jpg)  
a) Result by Munda’s method.

![](/api/attachments/MCC4FB6N/fulltext/images/e46abdadd711b2e04ad09ba80faed3e87b0f1bb2eaff0d5dbe1cc3f69ac45c66.jpg)  
b) Result by the TLSM method.  
Fig. 3. Dendrograms of similarities between experts.

The details of the TLSM method are described in the following sections.

## 4.3. Measuring similarity at the assessment level

To measure similarity at the assessment level, we need to divide the term set T for criterion c into several semantic-equal groups. To do so, a similarity matrix of the terms in $T _ { j }$ is built by pair-wise comparison based on their semantics; then a clustering algorithm is used, such as the hierarchical clustering for fuzzy similarity matrix (HCFSM) [23], to generate semantic-equal groups. We use pair-wise comparison for some practical considerations. Firstly, the semantic interpretation of linguistic terms varies person to person and case by case. Pair-wise comparison can avoid dif<sup>fi</sup>culties in de<sup>fi</sup>ning a commonly-acceptable semantic of a term for all persons and for all cases. Secondly, some linguistic terms are incomparable. Hence it is hard to de<sup>fi</sup>ne an appropriate and rational similarity measurement for those terms. Thirdly, similarity between terms may be changeable. Two terms may be distinguishable in one context but indistinguishable in the other. Pair-wise comparison has been proved an effective strategy to analyze relationships between factors; for instance, the analytic hierarchy process (AHP) technique extensively uses pair-wise comparison to obtain local-priority and global-priority. Using it can better <sup>fi</sup>t an application's speci<sup>fi</sup>c setting and avoid potential heavy and complicated calculations. Nonetheless, we do not reject other methods to determine the semantic similarity matrix.

For a given criterion $c _ { j } ,$ the similarity matrix $S _ { j }$ is denoted by $S _ { j } = \left( s _ { p r } \right) _ { p _ { i } \tilde { n } p _ { i } } $ , where $s _ { p r }$ is the semantic similarity of terms $t _ { p }$ <sup>¼</sup>and $t _ { r } ,$ <sup>j</sup>, and $\begin{array} { r } { s _ { p r } \in [ 0 , 1 ] , s _ { r r } = 1 , s _ { p r } = s _ { r p } } \end{array}$ for any $p , \ r \in \{ 1 , . . . , p _ { j } \}$

After obtaining the similarity matrix, the TLSM method will segment the term set by a clustering algorithm. Noting that the total number of terms in the term set is often between 5 and 9, the TLSM method uses the HCFSM as an example to illustrate the segmenting:

• derive the transitive closure $\cdot \hat { S } _ { j }$ from ${ \cal S } _ { j } \flat \ y \hat { S } _ { j } = { \cal S } _ { j } \cup { \cal S } _ { j } ^ { 2 } \cup { \cal S } _ { j } ^ { 4 } \cup \cdots ,$ where $S _ { j } ^ { 2 k }$ is the max–min composition of S<sup>k</sup>;

• decompose $\hat { \boldsymbol { S } } _ { j }$ into a set of α-level equivalence class $\left( \hat { S } _ { j } \right) _ { { \cal { I } } }$ ; and

• terms in $T _ { j }$ whose similarities belong to the same $\left( \overset { \underset { \mathrm { u } } { } } { \hat { S } } _ { j } \right) _ { \alpha }$ form a semantic-equal term group $T G _ { j } ^ { \alpha }$ and are treated with similar semantic.

Based on the segmentation of $T _ { j } ,$ a similarity at the assessment level is de<sup>fi</sup>ned according to the number of candidate options (nsp ), on which the two opinions are similar, and the total number of candidate options n. As a simple illustrative example, the TLSM let the similarity be the ratio of them.

## 4.4. Measuring similarity at the criterion level

The main task in this step is to identify an appropriate SUF for each criterion which needs to satisfy two requirements: 1) it is proportional to similarity at the assessment level (PSA); and 2) it is proportional inversely to the weight of a criterion (PRW). Formally, an SUF is de<sup>fi</sup>ned below.

De<sup>fi</sup>nition 4.1. An SUF u(nsp,w) of a given criterion c is a mapping from $\mathbb { N } \times \mathbb { W } \mathrm { t o } \left[ 0 , 1 \right]$ if u satis<sup>fi</sup>es the PSA and PRW requirements, where ℕ is the set of natural numbers and W is the range of weights.

Functions satisfying De<sup>fi</sup>nition 4.1 are numerous. For simplicity, this study uses the following monotone and continuous function for illustrating purpose:

$$
u _ {j} \left(n s p _ {j}, w c _ {j}\right) = \left(\frac {n s p _ {j}}{n}\right) ^ {f \left(w c _ {j}\right)}\tag{6}
$$

where nsp /n is the similarity at the assessment level and $f ( w c _ { j } )$ is a parameter determined by $w c _ { j } .$ . Because the weight wc could be a numeric value or a linguistic term, we will consider these two forms accordingly.

## 4.4.1. Weights are non-negative real numbers

Suppose $w c _ { 1 } \geq w c _ { 2 } \geq \cdots \geq w c _ { m }$ is a set of normalized numeric weights and $w c _ { j } \geq 0 , ~ \textstyle \sum _ { j } ^ { m } = { _ { 1 } w c _ { j } = 1 } , ~ m = | C |$ . In this situation, we can determine the parameter $f ( w c _ { j } )$ as follows: 1) determine a reference value $w c _ { j 0 }$ and set $f ( w c _ { j 0 } ) = 1 ;$ and 2) for each $w c _ { j } ,$ set $f ( w c _ { j } ) = w c _ { j } / w c _ { j _ { 0 } }$ . To <sup>fi</sup>nd a wc from $w c _ { 1 } , . . . , w c _ { m }$ , the following illustrative method is used: if m is odd, then set $\begin{array} { r } { W C _ { j _ { 0 } } = W C _ { ( m + 1 ) / 2 } ; } \end{array}$ if m is even, then set $w c _ { j _ { 0 } } = \left( w c _ { m / 2 } + w c _ { m / 2 + 1 } \right) / 2$ <sup>¼ ð Þþ</sup>. Based on this wc , all <sup>¼</sup>wc s are then mapped to [0,∞) by

$$
f \left(w c _ {j _ {0}}\right) = 1, \quad f \left(w c _ {j}\right) = \frac {w c _ {j}}{w c _ {j _ {0}}}, \quad j = 1, \dots , m.\tag{7}
$$

## 4.4.2. Weights are linguistic terms

Linguistic weights are often represented by fuzzy numbers (or fuzzy sets). Speci<sup>fi</sup>c numeric features of a fuzzy number (set), such as its center of gravity (COG) or its generalized integral, can be used to determine the parameter f(wc ). A brief outline for determining this parameter is given as: 1) select a numeric feature NF of fuzzy numbers and calculate NF<sub>j</sub> of the linguistic weight wc<sub>j</sub>; and 2) determine f(NF<sub>j</sub>) following steps for f(wc ) in Section 4.4.1 and set $f ( w c _ { j } ) = f ( N F _ { j } )$ ).

Similarity matrix for linguistic assessments.

<table><tr><td>Term</td><td>Very bad</td><td>Bad</td><td>Fairly bad</td><td>Moderate</td><td>Fairly good</td><td>good</td><td>Very good</td></tr><tr><td>Very bad</td><td>1.0</td><td>0.8</td><td>0.7</td><td>0.5</td><td>0.3</td><td>0.2</td><td>0.0</td></tr><tr><td>Bad</td><td>0.8</td><td>1.0</td><td>0.9</td><td>0.7</td><td>0.5</td><td>0.4</td><td>0.2</td></tr><tr><td>Fairly bad</td><td>0.7</td><td>0.9</td><td>1.0</td><td>0.8</td><td>0.6</td><td>0.5</td><td>0.3</td></tr><tr><td>Moderate</td><td>0.5</td><td>0.7</td><td>0.8</td><td>1.0</td><td>0.8</td><td>0.7</td><td>0.5</td></tr><tr><td>Fairly good</td><td>0.3</td><td>0.5</td><td>0.6</td><td>0.8</td><td>1.0</td><td>0.9</td><td>0.7</td></tr><tr><td>Good</td><td>0.2</td><td>0.4</td><td>0.5</td><td>0.7</td><td>0.9</td><td>1.0</td><td>0.8</td></tr><tr><td>Very good</td><td>0.0</td><td>0.2</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0.8</td><td>1.0</td></tr></table>

![](/api/attachments/MCC4FB6N/fulltext/images/ebbf2ce33e8b5133a410345fb052fca5a76997ec737b18d32bc291820b37a0ec.jpg)  
Fig. 4. Dendrogram of linguistic assessments (terms).

Following this outline, suppose the linguistic weights are “Very high (VH)”, “Fairly high (FH)”, “Medium (M)”, “Rather low (RL)”, and “Very low (VL)” and their corresponding fuzzy numbers are shown in Fig. 2(b). Let the selected numeric feature be the horizontal coordinate of COG of a fuzzy number, i.e.,

$$
N F _ {j} = \frac {\int x \mu (x) d x}{\int \mu (x) d x}\tag{8}
$$

where $\mu ( x )$ is the membership function of the fuzzy number. By $\operatorname { E q . } \left( 8 \right)$ and following steps in Section 4.4.1, the f(NF ) is calculated and shown in Table 3. Replacing the f(wc<sub>j</sub>) in Eq. (7) by f(NF<sub>j</sub>), we obtain the SUFs for <sup>fi</sup>ve linguistic weights, which can then be applied to calculate the similarity at the criterion level.

After determining the SUF for each given criterion, we apply them to measure the similarity of the opinions of two participants at the criterion level. Suppose a referential criterion is weighted “FH” and the evaluations of two participants are treated similarly for seven out of nine candidate options, then the similarity of the opinions with respect to this criterion is 0.680 (=(7/9)1.534).

## 4.5. Measuring similarity at the problem level

The similarity of two opinions about each individual criterion provides a single perspective by which we observe the similarity of two opinions. While a set of criteria is considered, we need to integrate those observations to form a comprehensive one. The GAA developed in Section 3 is used for this task. The following two examples illustrate how to use it. Suppose the similarities about 10 criteria are obtained at the criterion level as shown in the second column of Table 1.

Example 4.1. This example illustrates the usage of OGA. Assume that both and ℬ are the arithmetic means. For the 10 inputs, the OGA <sup>fi</sup>rstly generates 10 candidate similarities for the <sup>fi</sup>nal one s by $A _ { i }$ $( i = 1 , . . . , 1 0 )$ and they are: 0.840 (s ), 0.812 (s ), 0.845 (s ), 0.718 $\left( { \overline { { S } } } _ { 4 } \right)$ $0 . 6 3 0 \left( \overline { { s } } _ { 5 } \right)$ , 0.604 $\left( \overline { { \boldsymbol { S } } } _ { 6 } \right)$ , 0.570 (s ), 0.617 (s ), 0.619 $\left( \overline { { S } } _ { 9 } \right)$ , and 0.572 $\left( \overline { { S } } _ { 1 0 } \right)$ Then the GAA applies $B _ { 1 0 } \mathrm { t } 0 \ \overline { { s } } _ { 1 } , . . . , \overline { { s } } _ { 1 0 }$ and produces $\overline { { s } } = 0 . 6 8 3$ , i.e., the similarity of the two experts' opinions is 0.683.

Number of options with similar opinions by pairwise comparison

<table><tr><td>nsp</td><td> $b_1$ </td><td> $b_2$ </td><td> $b_3$ </td><td> $b_4$ </td><td> $b_5$ </td><td> $b_6$ </td></tr><tr><td> $b_1$ </td><td>7</td><td>6</td><td>1</td><td>1</td><td>1</td><td>2</td></tr><tr><td> $b_2$ </td><td>6</td><td>7</td><td>1</td><td>1</td><td>1</td><td>2</td></tr><tr><td> $b_3$ </td><td>1</td><td>1</td><td>7</td><td>4</td><td>3</td><td>3</td></tr><tr><td> $b_4$ </td><td>1</td><td>1</td><td>4</td><td>7</td><td>6</td><td>6</td></tr><tr><td> $b_5$ </td><td>1</td><td>1</td><td>3</td><td>6</td><td>7</td><td>5</td></tr><tr><td> $b_6$ </td><td>2</td><td>2</td><td>3</td><td>6</td><td>5</td><td>7</td></tr></table>

Example 4.2. This example illustrates the usage of WGA. Assume that is the OWA aggregation [29] and ℬ is the arithmetic mean. Because an OWA aggregation needs the weights of inputs, we randomly generate 10 unnormalized weights for them as: 0.394 (w ), 0.798 (w ), 0.198 $\left( w _ { 3 } \right)$ , 0.768 $\left( w _ { 4 } \right)$ , 0.554 $\left( w _ { 5 } \right)$ , 0.629 (w ), 0.513(w ), 0.916 $( w _ { 8 } ) .$ , 0.717 (w ), and 0.607 $( w _ { 1 0 } ) .$ . Then, the WGA calculates the candidate values of $\cdot _ { \bar { s } _ { i } }$ following OWA: 0.952 (s ), 0.925 (s ), 0.913 (s ), 0.866 $\left( { \overline { { S } } } _ { 4 } \right)$ , 0.819 (s ), 0.755 (s ), 0.703 (s ), 0.632 (s ), 0.586 (s ), and 0.541 (s ). Finally, the WGA applies the $B _ { 1 0 } \mathrm { t } 0 \bar { s } _ { 1 } , . . . , \bar { s } _ { 1 0 }$ to get the overall similarity, which is 0.769.

Based on the similarity measurement at the three levels, an overall similarity between the opinions of two participants is generated, which can be used as the answer of the MOSP problem.

## 5. Applications in policy selection and evaluation

This section applies the TLSM method to a social policy selection application and an energy policy evaluation application.

## 5.1. Case 1: do similarities exist between social actors?

This example is quoted from [23]. In a social policy selection problem, six social actors (i.e., participants) have presented their assessments for seven possible policies (i.e., options). The social impact matrix (i.e., evaluation report) is given in Table 4 and the semantics of the used linguistic terms is given in Fig. 2(a). The problem is to answer whether or not similarities exist between these social actors.

Firstly, we recited the solution in [23] as a comparison with the TLSM method. The Munda's method includes three main steps.

• Generate a similarity matrix between the social actors by a similarity measurement $\begin{array} { r } { s ( b _ { 1 } , b _ { j } ) \colon ( 1 + [ \sum _ { k = 1 } ^ { 7 } { ( \iint _ { x y } { | x - y | f _ { i } ( x ) g _ { j } ( y ) \mathrm { d } y \mathrm { d } x } ) ^ { 2 } } ] ^ { 1 / 2 } ) ^ { - { \bar { 1 } } } } \end{array}$ where ∬ |x − y|f(x)g(y)dydx is the semantic distance between two linguistic terms x and y. The obtained similarity matrix S is shown in Table 5. • Generate hierarchical clustering by the HCFSM algorithm (Fig. 3(a)) • Generate hierarchical clustering by the HCFSM algorithm (Fig. 3(a))

• Analyze clustering result: the social actors $b _ { 1 }$ and $b _ { 2 }$ have higher similarity.

We now measure the similarity between the social actors $b _ { 1 }$ and $b _ { 4 }$ as an illustration of the TLSM method procedure. Because the problem setting does not mention evaluation criteria, we assume that only one criterion is considered.

Step 1 Measuring similarity at the assessment level. Firstly, we de<sup>fi</sup>ne a distance measure $d ( t _ { i } , t _ { j } ) = | x _ { i } - x _ { j } |$ between two terms $t _ { i }$ and $t _ { j }$ whose membership functions are fuzzy numbers and $\mu _ { t _ { i } } ( x _ { i } ) = 1 ,$ $\mu _ { t _ { i } } ( x _ { j } ) = 1$ . Correspondingly, the similarity between t<sub>i</sub> and t<sub>j</sub> is <sup>¼</sup>de<sup>fi</sup>ned by $s _ { i j } = 1 - d ( t _ { i } , t _ { j } )$ and the similarity matrix obtained is shown in Table 6. The dendrogram for the seven evaluation terms by the HCFSM algorithm is presented in Fig. 4.

Pair-wise comparison of similarity at the criterion leve $( f ( w c ) = 1 ) .$

<table><tr><td></td><td> $b_1$ </td><td> $b_2$ </td><td> $b_3$ </td><td> $b_4$ </td><td> $b_5$ </td><td> $b_6$ </td></tr><tr><td> $b_1$ </td><td>1.000</td><td>0.857</td><td>0.143</td><td>0.143</td><td>0.143</td><td>0.286</td></tr><tr><td> $b_2$ </td><td>0.857</td><td>1.000</td><td>0.143</td><td>0.143</td><td>0.143</td><td>0.286</td></tr><tr><td> $b_3$ </td><td>0.143</td><td>0.143</td><td>1.000</td><td>0.571</td><td>0.429</td><td>0.429</td></tr><tr><td> $b_4$ </td><td>0.143</td><td>0.143</td><td>0.571</td><td>1.000</td><td>0.857</td><td>0.857</td></tr><tr><td> $b_5$ </td><td>0.143</td><td>0.143</td><td>0.429</td><td>0.857</td><td>1.000</td><td>0.714</td></tr><tr><td> $b_6$ </td><td>0.286</td><td>0.286</td><td>0.429</td><td>0.857</td><td>0.714</td><td>1.000</td></tr></table>

Table 9  
Pairwise comparison of similarity at the criterion level (f(wc) = 2).

<table><tr><td></td><td> $b_1$ </td><td> $b_2$ </td><td> $b_3$ </td><td> $b_4$ </td><td> $b_5$ </td><td> $b_6$ </td></tr><tr><td> $b_1$ </td><td>1.000</td><td>0.735</td><td>0.020</td><td>0.020</td><td>0.020</td><td>0.082</td></tr><tr><td> $b_2$ </td><td>0.735</td><td>1.000</td><td>0.020</td><td>0.020</td><td>0.020</td><td>0.082</td></tr><tr><td> $b_3$ </td><td>0.020</td><td>0.020</td><td>1.000</td><td>0.327</td><td>0.184</td><td>0.184</td></tr><tr><td> $b_4$ </td><td>0.020</td><td>0.020</td><td>0.327</td><td>1.000</td><td>0.735</td><td>0.735</td></tr><tr><td> $b_5$ </td><td>0.020</td><td>0.020</td><td>0.184</td><td>0.735</td><td>1.000</td><td>0.510</td></tr><tr><td> $b_6$ </td><td>0.082</td><td>0.082</td><td>0.184</td><td>0.735</td><td>0.510</td><td>1.000</td></tr></table>

Secondly, we take the 0.9-level equivalence-class in $\mathrm { F i g . }$ 4 to compare the evaluations of actors $b _ { 1 }$ and $b _ { 1 } .$ . It is noted that these two social actors have a similar opinion on policy $a _ { 5 }$ only. Table 7 lists the number of similar options of each pair of social actors.

Step 2 Measuring similarity at the criterion level. Based on the one criterion assumption, we need only to determine a unique parameter $f ( w c )$ for the SUF. Suppose the SUF is of the form in Eq. (6). Noticing that setting f(wc) to be less than, equal to, or greater than 1.0 gives three typical utilities of a criterion, we discuss them below respectively.

The <sup>fi</sup>rst situation is setting $f ( w c ) = 1 .$ The SUF is a linear function, by which the similarity between b<sub>1</sub> and $b _ { 4 }$ is 0.143. Table 8 illustrates the pair-wise similarity of all actors under this setting.

The second situation is setting f(wc)N1. The obtained SUF increases slowly with a smaller similarity at the assessment level and then increases quickly with a larger one. Suppose $f ( w c ) = 2$ , then the pair-wise similarities of the six actors are shown in Table 9.

The third situation is $f ( w c ) { > } 1$ . The obtained SUF increases quickly with a smaller similarity at the assessment level and then increases slowly with a bigger one. When setting $f ( w c ) = 1 / 3 ,$ , the pair-wise similarities are shown in Table 10. Based on the identi<sup>fi</sup>ed SUF, the similarity between $b _ { 1 }$ and $b _ { 4 }$ is obtained at the criterion level.

Step 3 Measuring similarity at the problem level. Because only one criterion is considered, no aggregation is needed; therefore, the similarity at the problem level is that at the criterion level, i.e., the similarity between $b _ { 1 }$ and $b _ { 4 }$ is 0.020.

Based on the similarity matrix in Table 10, we can use the HCFSM to obtain a similar dendrogram (Fig. 3(b)). Comparing the two dendrograms in Fig. 3, we recognized two minor differences: 1) social actor $b _ { 6 }$ will join the group of $b _ { 4 }$ and $b _ { 5 }$ earlier than social actor $b _ { 3 } ;$ and 2) the parameter α is slightly different.

## 5.2. Case 2: energy policy selection with missing assessments

A governmental consultant committee has designed three national energy policies $( O _ { 1 } , \ O _ { 2 } , \ O _ { 3 } )$ for sustainable development and sent them to six domain experts $( e _ { 1 } , . . . , e _ { 6 } )$ for evaluation in terms of 16 primary and secondary criteria $( c _ { 1 } , . . . , c _ { 1 } 6 )$ . An expert's evaluation report includes two components: 1) the assessments on the importance of all criteria; and 2) the assessments on the impacts of the three alternative policies on sustainable development according to all criteria. All assessments are expressed by a term selected from a set of provided linguistic terms, or left blank for “unavailable”, or with a question mark for “uncertain assessments (unknown or unsure)”. After collecting the evaluation reports (Table 11) from those experts, the committee wants to know which two experts have similar opinions.

Pairwise comparison of similarity at the criterion leve $( f ( w c ) = 1 / 3 )$

<table><tr><td></td><td> $b_1$ </td><td> $b_2$ </td><td> $b_3$ </td><td> $b_4$ </td><td> $b_5$ </td><td> $b_6$ </td></tr><tr><td> $b_1$ </td><td>1.000</td><td>0.950</td><td>0.523</td><td>0.523</td><td>0.523</td><td>0.659</td></tr><tr><td> $b_2$ </td><td>0.950</td><td>1.000</td><td>0.523</td><td>0.523</td><td>0.523</td><td>0.659</td></tr><tr><td> $b_3$ </td><td>0.523</td><td>0.523</td><td>1.000</td><td>0.830</td><td>0.754</td><td>0.754</td></tr><tr><td> $b_4$ </td><td>0.523</td><td>0.523</td><td>0.830</td><td>1.000</td><td>0.950</td><td>0.950</td></tr><tr><td> $b_5$ </td><td>0.523</td><td>0.523</td><td>0.754</td><td>0.950</td><td>1.000</td><td>0.894</td></tr><tr><td> $b_6$ </td><td>0.659</td><td>0.659</td><td>0.754</td><td>0.950</td><td>0.894</td><td>1.000</td></tr></table>

Table 11  
Evaluation reports of six experts

<table><tr><td rowspan="2"> $c_i$ </td><td rowspan="2"> $w_i$ </td><td> $O_1$ </td><td> $O_2$ </td><td> $O_3$ </td><td> $O_1$ </td><td> $O_2$ </td><td> $O_3$ </td><td> $O_1$ </td><td> $O_2$ </td><td> $O_3$ </td></tr><tr><td colspan="3">Expert 1</td><td colspan="3">Expert 2</td><td colspan="3">Expert 3</td></tr><tr><td>1</td><td>VH</td><td>UL</td><td>L</td><td>AC</td><td>VL</td><td>VL</td><td>L</td><td>HUL</td><td>L</td><td>VL</td></tr><tr><td>2</td><td>FH</td><td>L</td><td>L</td><td>AC</td><td>UL</td><td>L</td><td>L</td><td>UL</td><td>UL</td><td>L</td></tr><tr><td>3</td><td>FH</td><td>UL</td><td>L</td><td>VL</td><td>UL</td><td>HUL</td><td>L</td><td>HUL</td><td>L</td><td>VL</td></tr><tr><td>4</td><td>FH</td><td>HUL</td><td>VL</td><td>AC</td><td>UL</td><td>UL</td><td>L</td><td>HUL</td><td>UL</td><td>HUL</td></tr><tr><td>5</td><td>FH</td><td>L</td><td>L</td><td>VL</td><td>L</td><td>VL</td><td>L</td><td>UL</td><td>VL</td><td>VL</td></tr><tr><td>6</td><td>FH</td><td>AC</td><td>VL</td><td>AC</td><td>VL</td><td>VL</td><td>UL</td><td>L</td><td>VL</td><td>AC</td></tr><tr><td>7</td><td>FH</td><td>L</td><td>UL</td><td>VL</td><td>UL</td><td>HUL</td><td>L</td><td>HUL</td><td>L</td><td></td></tr><tr><td>8</td><td>FH</td><td>VL</td><td>L</td><td>VL</td><td>AC</td><td>AC</td><td>AC</td><td>UL</td><td>VL</td><td>VL</td></tr><tr><td>9</td><td>FH</td><td>AC</td><td>VL</td><td>L</td><td>AC</td><td>AC</td><td>AC</td><td>UL</td><td>VL</td><td>AC</td></tr><tr><td>10</td><td>FH</td><td>L</td><td>UL</td><td>L</td><td>VL</td><td>L</td><td>L</td><td>VL</td><td>VL</td><td>UL</td></tr><tr><td>11</td><td>FH</td><td>UL</td><td>UL</td><td>?</td><td>L</td><td>L</td><td>VL</td><td>VL</td><td>VL</td><td>HUL</td></tr><tr><td>12</td><td>FH</td><td>HUL</td><td>UL</td><td>L</td><td>HUL</td><td>HUL</td><td>VL</td><td>AC</td><td>AC</td><td>L</td></tr><tr><td>13</td><td>VH</td><td></td><td></td><td></td><td></td><td></td><td></td><td>UL</td><td>VL</td><td>UL</td></tr><tr><td>14</td><td>VH</td><td>VL</td><td>VL</td><td>VL</td><td>VL</td><td>VL</td><td>VL</td><td></td><td>VL</td><td>UL</td></tr><tr><td>15</td><td>FH</td><td>UL</td><td>HUL</td><td>VL</td><td>HUL</td><td>HUL</td><td>UL</td><td>L</td><td>HUL</td><td>HUL</td></tr><tr><td>16</td><td>FH</td><td>UL</td><td>UL</td><td>L</td><td>HUL</td><td>HUL</td><td>L</td><td>L</td><td>VL</td><td>L</td></tr><tr><td></td><td></td><td colspan="3">Expert 4</td><td colspan="3">Expert 5</td><td colspan="3">Expert 6</td></tr><tr><td>1</td><td>VH</td><td>VL</td><td>L</td><td>UL</td><td>VL</td><td>UL</td><td>HUL</td><td>L</td><td>UL</td><td>HUL</td></tr><tr><td>2</td><td>FH</td><td>VL</td><td>L</td><td>VL</td><td>VL</td><td>UL</td><td>HUL</td><td>VL</td><td>L</td><td>UL</td></tr><tr><td>3</td><td>FH</td><td>AC</td><td>UL</td><td></td><td>VL</td><td>UL</td><td>HUL</td><td>L</td><td>HUL</td><td>HUL</td></tr><tr><td>4</td><td>FH</td><td>L</td><td>L</td><td>HUL</td><td>L</td><td>HUL</td><td>HUL</td><td>UL</td><td>UL</td><td>HUL</td></tr><tr><td>5</td><td>FH</td><td>AC</td><td>L</td><td>UL</td><td>AC</td><td>L</td><td>HUL</td><td>VL</td><td>VL</td><td>L</td></tr><tr><td>6</td><td>FH</td><td>UL</td><td>UL</td><td>HUL</td><td>AC</td><td>UL</td><td>HUL</td><td>L</td><td>UL</td><td>HUL</td></tr><tr><td>7</td><td>FH</td><td>UL</td><td>HUL</td><td>HUL</td><td>UL</td><td>L</td><td>HUL</td><td>HUL</td><td>HUL</td><td>HUL</td></tr><tr><td>8</td><td>FH</td><td>AC</td><td>VL</td><td>L</td><td>AC</td><td>UL</td><td>HUL</td><td>AC</td><td>AC</td><td>AC</td></tr><tr><td>9</td><td>FH</td><td>VL</td><td>AC</td><td>L</td><td>AC</td><td>UL</td><td>HUL</td><td>AC</td><td>AC</td><td>AC</td></tr><tr><td>10</td><td>FH</td><td>VL</td><td>L</td><td>AC</td><td>VL</td><td>UL</td><td>HUL</td><td>HUL</td><td>HUL</td><td>HUL</td></tr><tr><td>11</td><td>FH</td><td>HUL</td><td>HUL</td><td>L</td><td>L</td><td>UL</td><td>HUL</td><td></td><td></td><td></td></tr><tr><td>12</td><td>FH</td><td>AC</td><td>AC</td><td>VL</td><td>VL</td><td>UL</td><td>HUL</td><td>L</td><td>UL</td><td>HUL</td></tr><tr><td>13</td><td>VH</td><td>VL</td><td>L</td><td>UL</td><td>AC</td><td>L</td><td>UL</td><td>L</td><td>HUL</td><td>HUL</td></tr><tr><td>14</td><td>VH</td><td>VL</td><td>VL</td><td>UL</td><td>VL</td><td>L</td><td>UL</td><td></td><td></td><td></td></tr><tr><td>15</td><td>FH</td><td></td><td></td><td>UL</td><td>VL</td><td>UL</td><td>HUL</td><td>VL</td><td>UL</td><td>HUL</td></tr><tr><td>16</td><td>FH</td><td>UL</td><td>UL</td><td>HUL</td><td>VL</td><td>L</td><td>UL</td><td>L</td><td>UL</td><td>HUL</td></tr></table>

This study assumes that the linguistic terms used for weights of criteria and evaluations on policies are triangular normal fuzzy numbers as summarized in Table 12 and in Fig. 2(b).

Table 12  
Abbreviations and semantics of linguistic terms used in evaluation reports.

<table><tr><td>Abbreviation</td><td>Names</td><td>Semantics</td></tr><tr><td>VH (AC)</td><td>Very high (almost certain)</td><td>(0.7,1.0,1.0)</td></tr><tr><td>FH (VL)</td><td>Fairly high (very likely)</td><td>(0.5,0.8,1.0)</td></tr><tr><td>M (L)</td><td>Medium (likely)</td><td>(0.2,0.5,0.8)</td></tr><tr><td>RL (UL)</td><td>Rather low (unlikely)</td><td>(0.0,0.2,0.5)</td></tr><tr><td>VL (HUL)</td><td>Very low (highly unlikely)</td><td>(0.0,0.0,0.3)</td></tr><tr><td>NA</td><td>No answer</td><td></td></tr><tr><td>Segment level</td><td colspan="2">Segments</td></tr><tr><td>1.0</td><td colspan="2">{AC}, {VL}, {L}, {UL}, {HUL}</td></tr><tr><td>0.8</td><td colspan="2">{AC, VL}, {L}, {UL, HUL}</td></tr><tr><td>0.7</td><td colspan="2">{AC, VL, L, UL, HUL}</td></tr></table>

Based on the problem settings, the detailed steps are illustrated below.

Step 1 Measuring similarity at the assessment level. The similarity matrix S for assessment terms is obtained by using the same method in case 1 and it is:

<table><tr><td> $s_{ij}$ </td><td>AC</td><td>VL</td><td>L</td><td>UL</td><td>HUL</td></tr><tr><td>AC</td><td>1.0</td><td>0.8</td><td>0.5</td><td>0.2</td><td>0.0</td></tr><tr><td>VL</td><td>0.8</td><td>1.0</td><td>0.7</td><td>0.4</td><td>0.2</td></tr><tr><td>L</td><td>0.5</td><td>0.7</td><td>1.0</td><td>0.7</td><td>0.5</td></tr><tr><td>UL</td><td>0.2</td><td>0.4</td><td>0.7</td><td>1.0</td><td>0.8</td></tr><tr><td>HUL</td><td>0.0</td><td>0.2</td><td>0.5</td><td>0.8</td><td>1.0</td></tr></table>

By applying the HCSFM algorithm to $S ,$ we obtain three possible segments:

Note that only two weights (“VH” and “FH”) are used for the 16 criteria, and “VH” and “FH” are with same fuzzy membership functions o $\ " { \sf A C } ^ { n }$ and “VL”, this study uses the segments with 1.0-level for criteria with weight “VH” and the segments with 0.8-level for criteria with weight “FH”. (The segments with 0.7-level will not be used in this study because it lacks capability to distinguish different terms.) Therefore, we can compare experts' opinions at the assessment level. Let us take experts $e _ { 1 }$ and e<sub>2</sub> for example.

For criterion c : Because the weight of ${ \dot { c } } _ { 1 } { \dot { 1 } } s \ " \mathrm { V H " }$ , two assessments are similar if and only if they are identical. Hence, the number of assessments with similar semantics between (UL, L, AC) (of $e _ { 1 } )$ and (VL, ${ \cal U } , { \cal L } ) \left( \mathrm { o f } e _ { 2 } \right)$ about this criterion is 0.

For criterion $c _ { 2 } { : }$ Because the weight of $C _ { 2 } \mathrm { i } s ^ { \cdots } \mathrm { F H " }$ , the assessment $\ " { \sf A C } \ "$ is treated the same as “VL”; so do “UL” and “HUL”. Hence, the number of assessments with similar semantics between $\left( L , L , A C \right) \left( \operatorname { o f } e _ { 1 } \right)$ and (UL, L, L) (of $e _ { 2 } )$ about this criterion is 1 because the two opinions have the same assessment on policy $O _ { 2 }$ only.

Similarly, we can compare these two experts on the remaining 14 criteria one by one. Table 13 lists the number of options with similar opinion for all 16 criteria. Among the 16 criteria, criteria $c _ { 1 1 }$ and $c _ { 1 3 }$ are different from others due to the missing or uncertain assessments. This study treats them as dissimilar.

Step 2 Measuring similarity at the criterion level. This study uses the SUF de<sup>fi</sup>ned in Eq. (6). The parameter f(wc ) is determined by the same method as used in case 1. The numeric features of these <sup>fi</sup>ve linguistic terms are: $N F _ { V H } = 0 . 9 , N F _ { V H } = 0 . 7 6 7 ,$ $N F _ { M } = 0 . 5 , \ N F _ { R L } = 0 . 2 3 3$ , and $N F _ { V L } = 0 . 1$ . The study sets $f ( N F _ { M } ) = 1 . 0$ and calculates the parameters for the other four weights accordingly: $f ( N F _ { V H } ) = 1 . 8 , ~ f ( N F _ { H } ) = 1 . 5 3 4 ,$ $f ( N F _ { R L } ) = 0 . 4 6 6 , \mathrm { a n d } f ( N F _ { U L } ) = 0 . 2 .$

Once the SUFs of all evaluation criteria are <sup>fi</sup>nalized, they can be used to obtain similarity at the criterion level. For instance, consider the criteria $c _ { 1 }$ and $c _ { 6 } .$ The weight of $c _ { 1 }$ is “VH” and $f ( N F _ { V H } ) = 1 . 8 ;$ ; hence the similarity with respect to $c _ { 1 }$ is 0.000. Because the weight of $c _ { 6 } \ \mathrm { i } s ^ { \ \cdot \mathrm { e } } \mathrm { F H " }$ and the $f ( N F _ { F H } ) 1 . 5 3 4 ,$ then the similarity with respect to $c _ { 6 }$ is 0.537. For the other 14 criteria, the calculation is similar. The similarities at the criterion level between $e _ { 1 }$ and $e _ { 2 } { \mathrm { a r e } } ; s _ { 1 } = 0 . 0 0 0 ,$ $s _ { 2 } = 0 . 1 8 5 , s _ { 3 } = 0 . 1 8 5 , s _ { 4 } = 0 . 1 8 5 , s _ { 5 } = 0 . 1 8 5 , s _ { 6 } = 0 . 5 3 7 ,$ $s _ { 7 } = 0 . 1 8 5 , s _ { 8 } = 0 . 5 3 7 , s _ { 9 } = 0 . 5 3 7 , s _ { 1 0 } = 0 . 1 8 5 , s _ { 1 1 } = 0 . 0 0 0 ,$ $s _ { 1 2 } = 0 . 5 3 7 , s _ { 1 3 } = 0 . 0 0 0 , s _ { 1 4 } = 1 , s _ { 1 5 } = 0 . 5 3 7 , \mathrm { a n d } s _ { 1 6 } = 1 .$

Step 3 Measuring similarity at the problem level. The GAA is implemented as follows: 1) re-order the criteria by their weights in descending order; 2) set $A _ { i } \operatorname { t o }$ be the arithmetic mean, $i = 1 , . . . , 1 6 ;$ and 3) set $B _ { 1 6 }$ to be the t-conorm maximum max.

Number of options with similar opinion for 16 criteria with respect to $e _ { 1 }$ and $e _ { 2 } .$

<table><tr><td> $c_i$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td></tr><tr><td>No. of similar ass.</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td>2</td><td>1</td><td>0</td><td>2</td><td>0</td><td>3</td><td>2</td><td>3</td></tr></table>

To re-order the criteria, this study uses the NF values. Then following the order of criteria, the i-ary aggregation operator $A _ { i }$ is applied to those similarities at the criterion level to obtain candidate similarities between the two experts: 0.000, 0.000, 0.333, 0.296, 0.274, 0.259, 0.249, 0.285, 0.274, 0.300, 0.322, 0.310, 0.304, 0.320, 0.362, and 0.362. From them the biggest is selected by $B _ { 1 6 } ,$ which is 0.362. Therefore, the similarity between the experts $e _ { 1 }$ and $e _ { 2 }$ is 0.362.

Table 14 gives the pair-wise similarity of the six experts. Based on the pair-wise similarity measurement, the experts can be grouped again based on a clustering method. For instance, Fig. 5 is the dendrogram that uses the HCFSM algorithm. Further observation indicates that experts $e _ { 4 } , e _ { 5 } ,$ , and $e _ { 6 }$ have higher similarities in their opinions.

## 6. Conclusions and future works

MCGDM is an ef<sup>fi</sup>cient strategy to support decision making in many applications. However, overly similar opinions of participants may lead to an inappropriate decision. To reduce the potential risk of putting an inappropriate decision into practice, measuring opinion similarity between participants (MOSP) is an important issue, which has not been solved. To solve the MOSP problem, our research develops a gradual aggregation algorithm to model the dynamic generation of a decision and to process the missing value. Based on the gradual aggregation algorithm, a three-level-similarity measuring (TLSM) method for the MOSP problem is presented which measures the similarity between two opinions at the assessment level, the criterion level, and the problem level. Applying the TLSM method, two applications in social policy selection and energy policy evaluation are conducted.

The main contributions of this research are summarized as: Firstly, the TLSM method provides a workable processing framework for the MOSP problem. The MOSP problem is a signi<sup>fi</sup>cant but easily neglected practical topic in many applications. Existing opinion similarity measuring methods can tackle a part of the MOSP problem; however, they do not present a whole solution for it; Secondly, the small size of relevant opinion samples is a primary obstacle that prevents existing statistical learning techniques from being applied to the MOSP problem. The TLSM method can resolve these problems partially; Moreover, the TLSM method combines an opinion with its provider in its entire processing. This helps to develop more effective opinion similarity measuring and analysis techniques to overcome dif<sup>fi</sup>culties resulting from separation of opinions and their providers in real applications; Finally, the experiments indicate that the TLSM method effectively handle missing data, uncertain information, and linguistic assessments by adjusting the developed gradual aggregation algorithm. Highly satisfactory results have been obtained from the experiments.

Based on two case studies, some issues will be further studied. Firstly, the GAA is a novel technique to integrate information according to a group of inputs. The processing order of the inputs has special meaning and impact on the <sup>fi</sup>nal result. This study rearranges the inputs according to the descent order of the weights of criteria and a satisfactory result is obtained; however, the GAA still needs to be amended. Secondly, missing data and unclear answers are very common in real applications. The TSLM method treats them as distinct without distinguishing their real meanings and utilities further. This is an intuitive and simple processing strategy. Whether there is a better strategy is requiring investigation. Moreover, we will pay more attention on how to select a clustering algorithm for the TSLM method. For simplicity and illustrating purpose, this paper mainly used the HCFSM method. Although the experiment results are consistent with our expectation, it is by no means that the HCFSM is the best one. We recognized that selecting an appropriate clustering method should base on real applications. Thirdly, the MOSP problem is a special case of the user opinion analysis and behavior modeling problem. Due to a variety in the natures of different application contexts, effective techniques for solving the user opinion analysis and behavior modeling problem have not yet been found. Our next step is to extend the TLSM method and develop new techniques to provide applicable solutions for both the MOSP problem and the user opinion analysis and behavior modeling problem. Finally, the application of the proposed TSLM method involves heavy computational burden for large size decision making problems, which requires developing a corresponding decision support system. We currently implemented the presented method using the C++ and Java programming languages in a Linux distribution. We aim to amend and integrate the method into a decision support system which is being designed and developed.

Pair-wise similarities of all six experts.

<table><tr><td></td><td> $e_1$ </td><td> $e_2$ </td><td> $e_3$ </td><td> $e_4$ </td><td> $e_5$ </td><td> $e_6$ </td></tr><tr><td> $e_1$ </td><td>1</td><td>0.362</td><td>0.273</td><td>0.289</td><td>0.108</td><td>0.151</td></tr><tr><td> $e_2$ </td><td>0.362</td><td>1</td><td>0.275</td><td>0.277</td><td>0.189</td><td>0.379</td></tr><tr><td> $e_3$ </td><td>0.273</td><td>0.275</td><td>1</td><td>0.253</td><td>0.199</td><td>0.239</td></tr><tr><td> $e_4$ </td><td>0.289</td><td>0.277</td><td>0.253</td><td>1</td><td>0.493</td><td>0.337</td></tr><tr><td> $e_5$ </td><td>0.108</td><td>0.189</td><td>0.199</td><td>0.493</td><td>1</td><td>0.482</td></tr><tr><td> $e_6$ </td><td>0.151</td><td>0.379</td><td>0.239</td><td>0.337</td><td>0.482</td><td>1</td></tr></table>

![](/api/attachments/MCC4FB6N/fulltext/images/bc379f0ca46e79effc81e18bea027898c0be068aabe84bd1054157b013eaeee2.jpg)  
Fig. 5. Dendrogram of experts using the HCFSM.

## Acknowledgments

This work is supported by Australian Research Council under Discovery Project DP0880739. We sincerely appreciate Professor Da Ruan, who passed away during the review procedure, from Belgian Nuclear Research Center (SCK · CEN) for providing the experiment data. May he rest in peace in heaven! We sincerely thank the editor and anonymous reviewers for their suggestions and comments to improve the presented work.

## References

[1] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 737–749, http://dx.doi.org 10.1109/TKDE.2005.99.

[2] S. Banisch, T. Araújo, On the empirical relevance of the transient in opinion models, Physics Letters A 374 (31–32) (2010) 3197–3200, http://dx.doi.org/10.1016/ j.physleta.2010.05.071.

[3] G. Beliakov, J. Warren, Appropriate choice of aggregation operators in fuzzy decision support systems, IEEE Transactions on Fuzzy Systems 9 (6) (2001) 773–784, http://dx.doi.org/10.1109/91.971696.

[4] In: H. Bustince, F. Herrera, J. Montero (Eds.), Fuzzy Sets and Their Extensions: Representation, Aggregation and Models, Studies in Fuzziness and Soft Computing, vol. 220, Springer-Verlag, Berlin Heidelberg, 2008, http://dx.doi.org/10.1007/ 978-3-540-73723-0.

[5] T. Calvo, A. Kolesárová, M. Komorníková, R. Mesiar, Aggregation Operators: Properties, Classes and Construction Methods, in: T. Calvo, G. Mayor, R. Mesiar (Eds.), Aggregation operators Physica-Verlag GmbH Heidelberg Germany Germany, 2002 pp. 3-104.

[6] C. Chakraborty, D. Chakraborty, A fuzzy clustering methodology for linguistic opinions in group decision making, Applied Soft Computing 7 (3) (2010) 858–869 http://dx.doi.org/10.1016/j.asoc.2006.02.006.

[7] H. Chen, D. Zimbra, AI and opinion mining, IEEE Intelligent Systems 25 (3) (2010) 74–76, http://dx.doi.org/10.1109/MIS.2010.75.

[8] E. Herrera-Viedma, F. Chiclana, F. Herrera, S. Alonso, Group decision-making model with incomplete fuzzy preference relations based on additive consistency, IEEE Transactions on Systems, Man, and Cybernetics. Part B, Cybernetics 37 (1) (2007) 176–189, http://dx.doi.org/10.1109/TSMCB.2006.875872

[9] F. Herrera, E. Herrera-Viedma, F. Chiclana, Multiperson decision-making based on multiplicative preference relations, European Journal of Operational Research 129 (2) (2001) 372–385, http://dx.doi.org/10.1016/S0377-2217(99)00197-6.

[10] V.-N. Huynh, Y. Nakamori, A satisfactory-oriented approach to multiexpert decision-making with linguistic assessments, IEEE Transactions on Systems, Man, and Cybernetics. Part B, Cybernetics 35 (2) (2005) 184–196, http://dx.doi.org 10.1109/TSMCB.2004.842248

[11] J. Inglada, G. Mercier, A new statistical similarity measure for change detection in multitemporal SAR images and its extension to multiscale change analysis, IEEE Transactions on Geoscience and Remote Sensing 45 (5) (2007) 1432–1445, http://dx.doi.org/10.1109/TGRS.2007.893568.

[12] E. Iosif, A. Potamianos, Unsupervised semantic similarity computation between terms using web documents, IEEE Transactions on Knowledge and Data Engineering 22 (11) (2010) 1637–1647, http://dx.doi.org/10.1109/TKDE.2009.193.

[13] B. Liu, Sentiment analysis: a multifaceted problem, IEEE Intelligent Systems 25 (3) (2010) 76–80, http://dx.doi.org/10.1109/MIS.2010.75.

[14] J. Lu, G. Zhang, F. Wu, Multi-objective Group Decision Making: Methods, Software and Applications with Fuzzy Set Techniques, Imperial College Press, London, UK, 2007.

[15] J. Lu, J. Ma, G. Zhang, Y. Zhu, X. Zeng, L. Koehl, Theme-based comprehensive evaluation in new product development using fuzzy hierarchical criteria group decision-making method, IEEE Transactions on Industrial Electronics 58 (6) (2011) 2236–2246, http://dx.doi.org/10.1109/TIE.2010.2096171.

[16] J.-L. Marichal, An axiomatic approach of the discrete Choquet integral as a tool to aggregate interacting criteria, IEEE Transactions on Fuzzy Systems 8 (6) (2000) 800–807, http://dx.doi.org/10.1109/91.890347.

[17] J.-L. Marichal, An axiomatic approach of the discrete Sugeno integral as a tool to aggregate interacting criteria in a qualitative framework, IEEE Transactions on Fuzzy Systems 9 (1) (2001) 164–172, http://dx.doi.org/10.1109/91.917122.

[18] R. Mesiar, A. Kolesárová, T. Calvo, M. Komorníková, A Review of Aggregation Functions, in: H. Bustince, F. Herrera, J. Montero (Eds.), Fuzzy Sets and Their Extensions: Representation, Aggregation and Models, Studies in Fuzziness and Soft Computing, vol. 220, Springer-Verlag, Berlin Heidelberg, 2008, pp. 121–144, http://dx.doi.org/ 10.1007/978-3-540-73723-0-7

[19] R. Mesiar, J. Špirková, L. Vavríková, Weighted aggregation operators based on minimization, Information Sciences 178 (4) (2008) 1133–1140, http://dx.doi.org/ 10.1016/j.ins.2007.09.023.

[20] P. Meyer, M. Roubens, On the use of the Choquet integral with fuzzy numbers in multiple criteria decision support, Fuzzy Sets and Systems 157 (7) (2006) 927–938, http://dx.doi.org/10.1016/j.fss.2005.11.014.

[21] D.T. Miller, K.R. Morrison, Expressing deviant opinions: believing you are in the majority helps, Journal of Experimental Social Psychology 45 (4) (2009) 740–747, http://dx.doiorg/10.1016/i.iesp.2009.04.008

[22] G. Munda, Social Multi-Criteria Evaluation for a Sustainable Economy, Springer-Verlag, Berlin Heidelberg, 2008. http://dx,doi,org/10.1007/978-3-540-73703.

[23] G. Munda, A con<sup>fl</sup>ict analysis approach for illuminating distributional issues in sustainability policy, European Journal of Operational Research 194 (1) (2009) 307–322, http://dx.doi.org/10.1016/j.ejor.2007.11.061.

[24] M. Pandelaere, B. Briers, S. Dewitte, L. Warlop, Better think before agreeing twice mere agreement: a similarity-based persuasion mechanism, International Journal of Research in Marketing 27 (2) (2010) 133–141, http://dx.doi.org/10.1016 j.ijresmar.2010.01.003.

[25] B. Pang, L. Lee, Opinion mining and sentiment analysis, foundations and trend in information retrieval, 2 (1–2) (2008) 1–135, http://dx.doi.org/10.1561/1500000001.

[26] G. Pasi, R.R. Yager, Modeling the concept of majority opinion in group decision making, Information Sciences 176 (4) (2006) 390–414, http://dx.doi.org/10.1016/ j.ins.2005.07.006.

[27] O. Vechtomova, Facet-based opinion retrieval from blogs, Information Processing and Management 46 (1) (2010) 71–88, http://dx.doi.org/10.1016/j.ipm.2009.06.005.

[28] Y. Wu, F. Wei, S. Liu, N. Au, W. Cui, H. Zhou, H. Qu, OpinionSeer: interactive visuali zation of hotel customer feedback, IEEE Transactions on Visualization and Computer Graphics 16 (6) (2010) 1109–1118, http://dx.doi.org/10.1109/TVCG.2010.183.

[29] R.R. Yager, On ordered weighted averaging aggregation operators in multi-criteria decision making, IEEE Transactions on Systems, Man, and Cybernetics 18 (1) (1988) 183–190, http://dx.doi.org/10.1109/21.87068.

[30] J. Yu, J. Amores, N. Sebe, P. Radeva, Q. Tian, Distance learning for similarity estimation, IEEE Transactions on Pattern Analysis and Machine Intelligence 30 (3) (2008) 451–462, http://dx doi org/10.1109/TPAML 2007.70714

[31] L. Yu, K.K. Lai, A distance-based group decision-making methodology for multiperson multi-criteria emergency decision support, Decision Support Systems 51 (2) (2011) 307–315, http://dx.doi.org/10.1016/j.dss.2010.11.024.

Jun Ma received his Ph.D in Computer Sciences from University of Technology, Sydney, Australia. He is currently a Data Mining Scientist in SMART Infrastructure Facility, University of Wollongong, Australia. His research interests lie in automated and approximate reasoning with linguistic information and their application in decision making and data analysis. He has about 40 publications in international journals and conferences.

Professor Jie Lu received her Ph.D from Curtin University of Technology, Australia. Now she is the Head of School of Software and the Director of the Decision Systems and e-Services Intelligence Laboratory of QCIS centre in Faculty of Engineering and Information Technology, University of Technology, Sydney (UTS), Australia. Her research interests lie in the area of intelligent decision support systems, linguistic term processing and e-service intelligence. She has over 300 publications in international journals and conferences, and <sup>fi</sup>ve books. She has received <sup>fi</sup>ve Australian Research Council (ARC) discovery grants, and served as a guest editor of <sup>fi</sup>ve special issues for international journals, a keynote/feature speaker and a co-chair/chair for several conferences.

Dr Guangquan Zhang received his Ph.D from Curtin University of Technology, Australia. Now he is Associate Professor in QCIS centre, Faculty of Engineering and Information Technology, University of Technology, Sydney (UTS), Australia. His research interests lie in the area of fuzzy sets and fuzzy measure theory, intelligent decision-making, and uncertain information processing methods. He has over 250 publications in international journals and conferences and published two monographs and three textbooks. He has completed and is working on four Australian research council (ARC) discovery grants. He has served as an advisory or a guest editor for several international journals, and a co-chair for many conferences.
