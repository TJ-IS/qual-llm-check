---
otero_id: 18366
otero_key: "SUAZYCB2"
title: "Models for computer system evaluation and selection"
authors: "Peretz Shoval; Yaacov Lugasi"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90074-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Models for Computer System Evaluation and Selection

Peretz SHOVAL and Yaacov LUGASI

Department of Industrial Engineering and Management, Ben-Gurion University of the Negev, P.O. Box 653, Beersheva 84 105, Israel

Three main models for evaluating and selecting computer systems are presented and compared: (a) the additive-weight model, (b) the Eigenvector model, and (c) the multi-attribute utility model. A case study describes the application of these three models to the selection of a computer for an organization. In this study, the three models showed almost identical results in ranking the alternatives.

Based on the data obtained from the case study and a comparison of the models' attributes, we recommend using the multi-attribute utility model in cases wherein the required assumptions of independence hold. To overcome the difficulties involved in understanding and applying the model, the development of an interactive decision-support system is recommended.

Keywords: Additive weight model, Benefit/cost analysis, Computer system selection, Eigenvector model, Evaluation models, Multi-attribute utility model.

![](/api/attachments/SUAZYCB2/fulltext/images/7197c53519aa826177ee42ff65af429893039ceb724766338c8518cc5af44370.jpg)

Peretz Shoval is on the faculty of the Department of Industrial Engineering & Management and the Department of Computer Science at Ben-Gurion University of the Negev. He is also affiliated with the Graduate School of Business Administration at Tel-Aviv University and with the Hebrew-University of Jerusalem. He received B.A. in Economics and M.Sc. in Information-Systems from Tel-Aviv University, and Ph.D. in Management Information Systems from the University of Pittsburgh, doing his thesis on expert systems for information retrieval.

Dr. Shoval's research and teaching interests include systems analysis & design methodologies, database design, expert systems, and information retrieval. He has published in journals such as Information Systems, Information Processing & Management, Int'l Journal of Man-Machine Studies, Data & Knowledge Engineering, and Data Base. Prior to moving into academia Dr. Shoval held managerial and consulting positions in computer companies and in the IDF.

## 1. Introduction

This paper concerns the evaluation and selection of computing alternatives for organizations (profit or non-profit) and individuals. The term computing may apply to hardware, software, vendor support, or any combination thereof. Computer system evaluation and selection usually consists of the following stages (see $[1,2,3,7,19]$ for a detailed discussion):

\- Stage 1: Analyzing the needs of the system.

\- Stage 2: Defining its requirements and attributes.

\- Stage 3: Issuing a request for proposals (RFP) to various suppliers (possibly including the information systems unit within the organization).

\- Stage 4: Performing initial screening and then evaluating and comparing the alternative proposals, using an appropriate evaluation model.

\- Stage 5: Selecting the best alternative (possibly with a benchmark) and making arrangements for acquiring the system.

\- Final Stage: Acceptance testing and acceptance.

This paper concerns the fourth stage, focusing on models used for evaluation. We introduce traditional methods applied in the MIS field as well as other methods in management science and decision-making theory that are applicable to selection.

![](/api/attachments/SUAZYCB2/fulltext/images/ea1d3cf2cf4536697fc5f0ff84b6470366711b1be4989461dd2c69ead89d69d6.jpg)  
Yaacov Lugasi specializes in industrial economics and decision making models. He earned B.Sc. and M.Sc. in Industrial-Engineering from Ben-Gurion University of the Negev. Mr. Lugasi lectures on the above topics at the Department of Industrial Engineering & management. Additionally, he is co-manager of a consulting company specializing in training and consulting on information-systems and industrial engineering.

In the process of evaluation and selection, a comparison of the alternatives should relate to predicted benefits and costs. The benefit aspect, unlike the cost, is generally difficult to measure in monetary or other quantitative terms. Detailed discussions of this problems are available in the literature, e.g. [2,4,5,11].

A list of criteria or attributes required of the system is needed to specify the benefits. Listing criteria or attributes is difficult, since there is no general list available as an aid. For every problem/need a specific list of attributes therefore has to be defined. In general, such a list may be organized in some sort of hierarchy. First, a group of major attributes is defined (e.g. software, hardware, support) and then each major group is broken down into more specific ones; it is usual to distinguish between two levels only.

A performance measure should be decided for each attribute to enable one to determine the relative value of the attribute in any given system. It may be measured in quantitative terms. For instance, in the attribute “memory capacity”, the performance measure may be size in bytes. However, an attribute is most often intangible, with no quantifiable performance measure. In this case a qualitative evaluation should be made, e.g., the attribute “documentation quality” must be measured on a relative scale, which will be subjective and limited. While determining the performance measures for attributes one must be aware that different attributes may have performance measures at different units and scales. When evaluating and comparing alternatives, one must be careful in dealing with different values and avoid mixing different units. To overcome this, one can convert to a normalized scale.

Aside from the definition of the attributes and their performance measures, one should define the mandatory requirements. This will assist in the initial screening of proposals that do not meet requirements. Among the mandatory requirements are performing measure of a certain minimal value (e.g., the system must allow a minimum of “x” work stations) or necessary existence and non-existence attributes (e.g., the system must have a compiler for COBOL).

## 2. Widely Used Models

## 2.1. The Efficient-Frontier Model

In this model $[2,9]$ , the preferred alternative is that which is dominant in all the attributes considered. Assume two alternatives are given with attribute values as follows:

$$
y ^ {\prime} = \left(y _ {1} ^ {\prime}, \dots , y _ {n} ^ {\prime}\right), \quad y ^ {\prime \prime} = \left(y _ {1} ^ {\prime \prime}, \dots , y _ {n} ^ {\prime \prime}\right).
$$

Alternative $y'$ is dominant if $y_i' \geqslant y_i''$ for every $i$ and $y_i' > y_i''$ for some $i$ . (The relationship $>$ expresses the dominance due to the decision maker's preference).

This method enables one to screen out the alternatives that are inferior in all attributes or are identical in some and inferior in at least one. The alternatives remaining after this screening form the “efficient frontier”. There remains the problem of selecting the preferred alternative, and this require other methods. It is evident, therefore, that this model is not sufficient. The model is applicable, at most, in performing initial screening.

## 2.2. Lexicographical Ordering

In this model $[2,9]$ , the alternatives are rank ordered according to a dominant attribute, (i.e. the most important one). Clearly, this is possible only if a dominant attribute exists and cannot be traded off with others. This model can, at most, help in the initial screening of alternatives which are deficient in an important attribute but it cannot choose the best.

## 2.3. Additive Weight

This is a practical method extensively used in evaluating and selecting computer systems $[1,3,12,17,19]$ . An importance weight is determined for each attribute and every alternative is given a score for each attribute. The selected alternative is that which maximizes the product:

$$
\begin{array}{l} \max \sum_ {i = 1} ^ {n} W _ {i} V _ {i j} (X _ {i}), \quad W _ {i} \geqslant 0, \\ \sum_ {i = 1} ^ {n} W _ {i} = 1, \quad V _ {i j} \leqslant 1 \end{array}
$$

where $W_{i}$ is the weight of attribute $X_{i}$ and $V_{ij}$ is the score granted to attribute $X_{i}$ in alternative j.

The advantage of this model is that it is simple. It also enables one to perform sensitivity analysis of the results to changes in the importance weights of the attributes. Its disadvantage is that it is not normative, i.e. it is not based on a system of axioms expressing rational behavior rules expected of the decision-maker. Thus it does not require an examination of assumptions of independence in the attributes, and the absence of such an examination may result in deviations; the following example demonstrates this:

Let us assume two proposals A and B, which are examined according to two attributes: “vendor support” and “equipment reliability”. If “vendor support” is evaluated as very good in proposal A and very bad in proposal B, this can affect the evaluation of “equipment reliability”. In alternative A the evaluator may grant a relatively high score to it, since “vendor support” is good, but not for B.

In addition, the model does not allow for the examination of consistency of the evaluators. Due to its nature, the model does not consider risk and uncertainty. It should be noted that granting scores in every attribute is in itself a difficult task and influenced by subjective considerations.

## 2.4. Cost Value

The cost-value method [7] considers cost only as a basis for selecting a system. According to this model, monetary values are determined to represent the forecast savings resulting from the particular way of implementing an attribute in an alternative. This does not include mandatory attributes. Then the credit values are summed for each alternative and subtracted from its total cost. The remainder represents the relative worth of each alternative. The alternative with the highest worth is then selected.

An advantage of this method is that it deals with a common value unit: money. However, it requires the determination of monetary values for savings predicted for each attribute. Additionally, it is not a normative model.

## 2.5. Saaty's Eigenvector Model

This is described in [14] and [16]. It allows the determination of both weights and scores for each attribute, in every alternative by using matrices to perform pairwise comparisons between attributes and between alternatives. Once weights and scores are obtained, the final score of each alternative is calculated according to the additive weight technique.

In order to determine the weight of n attributes, the decision maker fills up a matrix whose dimensions are $n \times n$ and in which a pairwise comparison is made between every two attributes. Thus in each cell (i, j) in the matrix, the decision maker expresses the relative importance of attribute i with respect to attribute j. (It is only necessary to fill up half of the matrix, because it is symmetric.) Then, the eigenvector of the matrix is calculated for the maximal eigenvalue. The eigenvector is normalized so that the total sum of its elements is 1. The values of this eigenvector constitute the attribute weights.

To determine the attribute scores for each alternative, the decision maker fills up a matrix of pairwise comparisons between alternatives. Altogether n matrices are filled (one for each attribute). The dimension of every matrix is the number of alternatives. Here too the normalized eigenvector is calculated, and the elements of every such vector express the scores of the alternative for the attribute.

The pairwise comparisons are accomplished with a relative numerical scale. Saaty has made experiments with scales of various types and found that a 1–9 scale is the most reliable, where 1 expresses identity between the two pairs compared and 9 expresses an absolute preference of one over the other.

The Eigenvector model enables one to examine the decision maker's consistency, using appropriate measures (in essence, if the decision maker is consistent in a certain matrix, the maximal eigenvector of the matrix equals the order of that matrix). On the other hand, this model ignores the issue of dependence between attributes. It also does not take into consideration risk and uncertainty, and it does not enable one to perform sensitivity analysis [16].

## 3. The Multi-Attribute Utility Model

Keeney's multi-attribute utility model [8,9,10] allows the evaluation of the utility function of the attributes and the calculation of their weights. It differs from the other models because it considers risk and uncertainty.

The application of the model requires both utility and preference independence. The first claims that for attributes $X_{1}\ldots X_{n}$ the utility of attribute $X_{i}$ does not depend on the remaining attributes. The second claims that preference between every pair of attributes does not depend on the fixed level of the remaining attributes. Cases where part of the assumptions do not hold are discussed in [9]).

There are two variants, which differ in the way they refer to risk: the additive model and the multiplicative model.

Additive model:

$$
U _ {j} = \sum_ {i = 1} ^ {n} k _ {i} U _ {i j} (X _ {i})
$$

Multiplicative model:

$$
U _ {j} = \left[ \left(\sum_ {i = 1} ^ {n} \left(1 + k k _ {i} U _ {i j} (X _ {i})\right)\right) - 1 \right] / k,
$$

where

$$
U _ {j} = \text { utility   of   alternative } j
$$

$$
k _ {i} = \text { scale   factor   (weight)   of   attribute } i
$$

$U_{ij}(X_i) =$ utility of attribute $X_{i}$ in alternative $j$

$$
0 <   k _ {i} <   1; \quad 0 \leqslant U _ {i j} (X _ {i}), \quad 0 \leqslant U _ {j} \leqslant 1
$$

k is a constant which constrains U to be between 0 to 1. It is calculated from the expression:

$$
1 + k = \prod_ {i = 1} ^ {n} \left(1 + k k _ {i}\right).
$$

The application of the additive model or the multiplicative model depends on the decision maker's attitude towards risk. The discriminant is $\sum_{i=1}^{n} k_{i}$ . If it is 1, then the decision maker is indifferent to risk, and the additive model is applied. If it is greater than 1, then risk matters and the multiplicative model is applied. k is set to the range 0 > k > -1. When the discriminant is less than 1, the decision maker seeks risk and the multiplicative model is used, with k greater than 0.

In order to evaluate the utility function of the attributes and to calculate the weights/constants of the attributes, a gambling technique is used: a utility function of the Von-Neuman–Morgenstern type [20].

## 3.1. Evaluation of the Utility Function

Evaluation of the decision maker's utility function for every attribute is based on the following axioms of preference:

a) Transitivity: if alternative $a_i$ is preferable to $a_j$ , and $a_j$ is preferable to $a_k$ , then $a_i$ is superior to $a_k$ .

b) Continuity: if $a_{i}$ is preferable to $a_{j}$ , and $a_{j}$ is preferable to $a_{k}$ , then it is possible to perform a gamble on $a_{i}$ and $a_{k}$ such that the decision maker will be indifferent to the choice between the gamble alternative and $a_{j}$ (as described later).

If the above axioms are satisfied, it is possible to form a utility function for the decision maker for each attribute in the following manner.

Assume that one wants to build a utility function for attribute $x_{i}$ . First, we define the highest level of $x_{i}$ , and denote it as $x_{i}^{*}$ . Then we determine that $U(x_{i}^{*}) = 1$ . Similarly, we define the lowest level of $x_{i}$ , denote it as $x_{i}^{0}$ , and determine that $U(x_{i}^{0}) = 0$ . Thus, two extreme points are obtained on the utility curve of $x_{i}$ . Now, in order to evaluate the utility of a particular level of $x_{i}$ denoted as $x_{i}'$ we address the following question to the decision maker:

"You have the following two alternatives:

a) Alternative A: attribute $x_{i}$ is at level $x_{i}'$ and you are sure to get this alternative.

b) Alternative B: this is given on a lottery card, where there is probability p that the level of attribute $X_{i}$ is $X_{i}^{*}$ , and probability $(1-p)$ that the level of attribute X is $X_{i}^{0}$ .

In addition, the remaining attributes in the two alternatives are at the same level. At what value of p will you be indifferent to the choice between the two alternatives?"

When the decision maker is indifferent to both alternatives we say that the utility of the first alternative equals the expected utility of the second alternative. That is to say:

$$
U \left(X _ {i} ^ {\prime}\right) = p U \left(X _ {i} ^ {*}\right) + (1 - p) U \left(X _ {i} ^ {0}\right).
$$

Since $U(x_{i}^{*}) = 1$ and $U(X_{i}^{0}) = 0$ we obtain $U(X_{i}^{\prime}) = p$ .

In the same way, we continue to find the utility of other points for various levels of $X_{i}$ . The line that connects the points forms the utility curve of attribute $X_{i}$ .

In applying the model to the selection of a computer system, there is no need to build a continuous utility curve for each attribute. It is sufficient to evaluate the utility of several relevant values of the attribute. In order to examine whether the decision maker is consistent, several questions can be asked to determine the utility of an attribute at a certain level, each time changing the levels of the attributes in the second alternative. It is expected that the utility of the attribute at the examined level (in the first alternative) will be identical for the various levels of the attribute which appear on the lottery card (for the second alternative). If the expected utility is not identical the process of evaluating the utility function for the attribute is restarted.

## 3.2. Calculating the Weights / Constants of the Attributes

In order to calculate the weight/constant of each attribute the following question is addressed to the decision maker:

"Assume that you have the following two alternatives:

a) Alternative A: the level of attribute $X_{i}$ is $X_{i}^{*}$ , the remaining attributes are at their lowest level.

b) Alternative B is given on a lottery card, where the probability is p that all the attributes (including $X_{i}$ ) are at their highest level, and probability $(1 - p)$ that all the attributes are at their lowest level.

In choosing between the two alternatives, to which probability would you be indifferent?"

The utility of alternative B, when all the attributes are at their highest level, equals 1 and is denoted as $k^{*}=1$ . When the attributes are at their lowest level the utility of the alternative is 0, denoted $k^{0}=0$ .

When the decision maker is indifferent in choosing between the two alternatives, we obtain $k_{i}=pk^{*}+(1-p)k^{0}$ , ( $k_{i}=$ weight of attribute $X_{i}$ ), and then $k_{i}=p$ .

The weights/constants of all the attributes are calculated according to the above procedure. Again, it is possible to check consistency similar to the procedure described previously.

After evaluating the utility function and weights/constants for every attribute, the sum of the weights/constants is calculated and the appropriate model to apply is then determined. If the sum is other than 1 the multiplicative model is applied, and the value of k is then calculated. Subsequently, for every alternative the total utility of each attribute is determined according to the utility function of that attribute, and the utility of the alternative is calculated based on the utility formula of the model which is applied. The preferable alternative is that with the maximum utility.

The multi-attribute utility model is normative, since it forces the decision maker to accept a set of axioms which expresses preferences and it also requires the examination of independence assumptions before the model is applies. As already seen, this is the only model which considers risk and uncertainty. The model also enables one to make sensitivity analysis.

Compared with the other models, this model is more difficult for the decision maker to understand and apply, since determining a probability at which the decision maker is indifferent between alternatives and the concept of a “lottery” ae not always clear and acceptable [6].

## 4. Case Study

This cast study illustrates the application of three models to the selection process of a microcomputer system in a plant which needed an information system for hydraulic process control.

In the feasibility study stage the information requirements, arranged hierarchically, were analyzed, a list of attributes was determined, and mandatory requirements were defined. Three groups were determined – hardware, software and system support. Then every group was assigned several attributes. The attributes, as well as the mandatory requirements, are presented in Table 1.

For every attribute, a performance measure was determined. Some were quantitative (such as the measure of “memory capacity”) and others were determined according to an appropriate scale.

Ten different proposals were submitted by suppliers (including six for compatible systems by different manufacturers). In the first stage of the selection process an initial screening of the proposals was made, on the basis of the mandatory requirements. Four proposals remained at the end of this stage. These four proposals were then evaluated according to three models: the additive-weight, the Eigenvector, and the multi-attribute model.

```txt
Table 1
Attributes and Mandatory Requirements

Group Z₁ – Hardware
X₁ – memory capacity
X₂ – calculation speed
X₃ – I/O speed
X₄ – equipment reliability
X₅ – flexibility for expansion
Group Z₂ – Software
X₆ – availability of scientific software
X₇ – flexibility to changes
X₈ – software performance (variety of options in the operating system, DBMS and application generators)
Group Z3 – System Support
X₉ – manufacturer's reliability
X₁₀ – supplier's reliability
X₁₁ – supply time
X₁₂ – quality of hardware support
X₁₃ – quality of software support
X₁₄ – quality of documentation
Mandatory Requirements
–capability of 2 channel communication
–minimum memory 576 K
–availability of agent to supply hardware and software services
–supply time should not exceed 2 months
```

Before starting the evaluation and selection process the decision maker was asked to assign for each proposal a set of values for the list of attributes and then to rank order the proposals with respect to each of the attributes. The evaluator was also asked to rank the attributes (ordinally) according to their importance with regard to the others. The purpose of these rankings was to make it possible to check the evaluator's consistency. It was expected that the cardinal values obtained later, in every model applied, would correspond with these cardinal rankings: there was indeed a correspondence.

For each proposal, the annual capitalized cost was calculated. Since it was found that the difference in cost between the most and least expensive proposal was relatively small, it was decided not to take cost into account.

## 4.1. Evaluation According to the Additive-Weight Model

The additive-weight model is applicable for a plain list of non-hierarchical attributes. Since in our case attributes were arranged hierarchically, the model was adjusted accordingly. Evaluation was made in three stages.

a) Stage 1. For each proposal, the evaluator was asked to determine a score for every attribute, using the appropriate measure for the attribute. The scores were converted into a uniform scale of 0 to 1. The score of proposal j on attribute i is denoted $V_{ij}(X)$ .

b) Stage 2. The evaluator was asked to determine the relative weight of each attribute within a group (so that the total sum of weights within a group is 1) and also the relative weight of each of the three groups. The weight of a group is denoted by Z and the weight of attribute $X_{i}$ within a group k is denoted by W.

c) Stage 3. The weighted score of each of the four proposals was calculated, according to the formula:

$$
V _ {j} = \sum_ {k = 1} ^ {3} \sum_ {i = 1} ^ {n _ {k}} Z _ {k} W _ {i k} V _ {i j} (X _ {i})
$$

$$
(n _ {k} = \text { number   of   attributes   in   group } k)
$$

Table 2 presents the weights of the groups, the weights of attributes within each group, the scores given to each attribute for each of the four proposals, and the weighted score calculated for each proposal. In the last line the proposals are ranked from best to worst. The preferred system according to this model is A. (The ranking of all the proposals is introduced only to compare the results of this model to those obtained in the other models.)

## 4.2. Evaluation According to Saaty's Model

Pairwise comparisons were made on a 1–9 scale (where 9 expresses the highest preference and 1 expresses equality between each pair compared). The comparisons were made in three stages:

a) Stage 1: The evaluator made pairwise comparisons between the proposals, each time for another attribute. Hence, $14 (4 \times 4)$ matrices were completed. It was thus possible to compute the scores of the attributes for each proposal.

b) Stage 2. The evaluator made pairwise comparisons between the attributes within each group. Three matrices were loaded (for the 3 groups) where the dimension of each matrix equals the number of attributes in the group. It was thus possible to compute the weights of the attributes within each group.

Scores and Weights: The Additive-Weight Model

<table><tr><td rowspan="2">Groups and Attributes *</td><td rowspan="2">Weights</td><td colspan="4">Scores of Proposals</td></tr><tr><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>Hardware</td><td>0.30</td><td></td><td></td><td></td><td></td></tr><tr><td> $X_1$ </td><td>0.25</td><td>0.8</td><td>0.8</td><td>0.8</td><td>1.0</td></tr><tr><td> $X_2$ </td><td>0.25</td><td>0.8</td><td>0.8</td><td>0.8</td><td>0.6</td></tr><tr><td> $X_3$ </td><td>0.07</td><td>0.8</td><td>0.8</td><td>0.8</td><td>1.0</td></tr><tr><td> $X_4$ </td><td>0.25</td><td>1.0</td><td>1.0</td><td>0.7</td><td>0.9</td></tr><tr><td> $X_5$ </td><td>0.18</td><td>1.0</td><td>0.9</td><td>0.9</td><td>0.8</td></tr><tr><td>Software</td><td>0.30</td><td></td><td></td><td></td><td></td></tr><tr><td> $X_6$ </td><td>0.3</td><td>0.8</td><td>0.8</td><td>0.8</td><td>0.6</td></tr><tr><td> $X_7$ </td><td>0.3</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.1</td></tr><tr><td> $X_8$ </td><td>0.4</td><td>0.9</td><td>0.9</td><td>0.8</td><td>0.9</td></tr><tr><td>Support</td><td>0.40</td><td></td><td></td><td></td><td></td></tr><tr><td> $X_9$ </td><td>0.2</td><td>1.0</td><td>1.0</td><td>0.8</td><td>0.9</td></tr><tr><td> $X_{10}$ </td><td>0.2</td><td>0.9</td><td>0.9</td><td>0.7</td><td>0.8</td></tr><tr><td> $X_{11}$ </td><td>0.1</td><td>0.9</td><td>0.7</td><td>1.0</td><td>0.9</td></tr><tr><td> $X_{12}$ </td><td>0.2</td><td>1.0</td><td>1.0</td><td>0.8</td><td>1.0</td></tr><tr><td> $X_{13}$ </td><td>0.2</td><td>0.9</td><td>0.9</td><td>1.0</td><td>0.8</td></tr><tr><td> $X_{14}$ </td><td>0.1</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.9</td></tr><tr><td>Weighted score</td><td></td><td>0.92</td><td>0.90</td><td>0.84</td><td>0.86</td></tr><tr><td>Ranking</td><td></td><td>1</td><td>2</td><td>4</td><td>3</td></tr></table>

\* The detailed list of attributes appears in Table 1.

c) Stage 3. The evaluator made pairwise comparisons between the three groups. One $3 \times 3$ matrix was completed; this allowed the computation of the relative weight of each group.

The matrices of the above three stages are shown in Figure 1.

After various matrices were entered, they were input to a program $[13]$ that calculated the maximal eigenvalue and the eigenvector which corresponds to the maximal normalized eigenvalue. It also calculated the consistency measure of each matrix (in our case it was found that the decision maker was consistent in all pairwise comparisons). Finally, the program calculated the weighted score of each proposal (similar to the calculation in the additive-weight model) and then ranked them.

Table 3 presents the weights of the groups and attributes, the scores of the proposals in each attribute as calculated from the matrices, the weighted scores of the proposals, and their final ranking.

Note the similarity between the attribute weights here compared to those in the additive-weight model (Table 2), and recall that here the attribute weights were calculated from the pairwise comparison matrices, whereas in the other model the weights were determined directly. On the other hand, the values of the scores obtained in the two models are different. The difference between the absolute values of scores in the Eigenvector model are meaningless, and so are the values of the weighted scores.

The ranking of the four proposals is almost the same in the two models. The only difference is in the reversed order of proposals C and D. Note that there is only a small difference between C and D within each model, whereas there is a relatively larger difference between these two and the first two proposals.

## 4.3. Evaluation According to the Multi-Attribute Utility Model

In order to apply the multi-attribute utility model, the assumptions of utility independence and preference independence had to be validated.

## 4.3.1. Checking Utility Independence

The assumption that the utility of attribute $X_{i}$ is independent of the level of the remaining attributes is examined when evaluating the utility of each attribute using the gambling technique. We checked the assumption with respect to the attribute “quality of documentation”. The performance of this attribute is measured on a 5-point scale. In order to estimate the utility function of this attribute using the gambling techniques we introduced two alternatives. In the first, which the decision maker is sure to get, the attribute ‘quality of documentation’ is given value 2 on the scale. The second alternative is available by lottery, where the probability is p that the value of the attribute will be 5 (maximum), and probability $(1-p)$ that the value of the attribute will be 1 (minimum). The remaining attributes in the two alternatives are at a fixed and identical level. The decision maker was asked to determine at which values of p it would not matter which of the two alternatives were chosen. He decided that it would be at p=0.25.

![](/api/attachments/SUAZYCB2/fulltext/images/9f2f32ab89e6d40753b6e4d7f953f420a237cd0a3bb6606a9c77a64a25502137.jpg)  
Fig. 1a. Matrices of Saaty's Model; Pairwise Comparisons Between Proposals

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Group $Z_{2}$ - Software
</div>

```txt
B. Pairwise comparisons between attributes
```

<table><tr><td rowspan="2"></td><td>Group</td><td colspan="4"> $Z_1$  - Hardware</td></tr><tr><td>X1</td><td>X2</td><td>X3</td><td>X4</td><td>X5</td></tr><tr><td>X1</td><td>1</td><td>1</td><td>5/2</td><td>1</td><td>3/2</td></tr><tr><td>X2</td><td>1</td><td>1</td><td>5/2</td><td>1</td><td>3/2</td></tr><tr><td>X3</td><td>2/5</td><td>2/5</td><td>1</td><td>1/3</td><td>1/2</td></tr><tr><td>X4</td><td>1</td><td>1</td><td>3</td><td>1</td><td>3/2</td></tr><tr><td>X5</td><td>2/3</td><td>2/3</td><td>2</td><td>2/3</td><td>1</td></tr></table>

<table><tr><td></td><td>X6</td><td>X7</td><td>X8</td><td>|</td></tr><tr><td></td><td colspan="3">----</td><td>|</td></tr><tr><td>X6</td><td>1</td><td>2</td><td>1</td><td>|</td></tr><tr><td>X7</td><td>1/2</td><td>1</td><td>1/2</td><td>|</td></tr><tr><td>X8</td><td>1</td><td>2</td><td>1</td><td>|</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Group $Z_{3}$ - System Support
</div>

<table><tr><td></td><td>X9</td><td>X10</td><td>X11</td><td>X12</td><td>X13</td><td>X14</td></tr><tr><td>X9</td><td>1</td><td> $3/2$ </td><td>5</td><td>3</td><td>3</td><td>4</td></tr><tr><td>X10</td><td> $2/3$ </td><td>1</td><td>3</td><td>2</td><td>2</td><td>3</td></tr><tr><td>X11</td><td> $1/5$ </td><td> $1/3$ </td><td>1</td><td> $1/3$ </td><td> $1/3$ </td><td>1</td></tr><tr><td>X12</td><td> $1/3$ </td><td> $1/2$ </td><td>3</td><td>1</td><td>1</td><td>2</td></tr><tr><td>X13</td><td> $1/3$ </td><td> $1/2$ </td><td>3</td><td>1</td><td>1</td><td>2</td></tr><tr><td>X14</td><td> $1/4$ </td><td> $1/3$ </td><td>1</td><td> $1/2$ </td><td> $1/2$ </td><td>1</td></tr></table>

```txt
C. Pairwise Comparison between Groups
```

<table><tr><td></td><td>21</td><td>22</td><td>23</td></tr><tr><td>21</td><td>1</td><td>1</td><td>1</td></tr><tr><td>22</td><td>1</td><td>1</td><td>1</td></tr><tr><td>23</td><td>1</td><td>1</td><td>1</td></tr></table>

Fig. 1b. Matrices of Saaty's Model; (B) Pairwise Comparisons Between Attributes; (C) Pairwise Comparison Between Groups

Table 3  
Scores and weights according to the Eigenvector model

<table><tr><td rowspan="2">Groups and attributes</td><td rowspan="2">Weights</td><td colspan="4">Scores of proposals</td></tr><tr><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>Hardware</td><td>0.333</td><td></td><td></td><td></td><td></td></tr><tr><td> $X_1$ </td><td>0.244</td><td>0.222</td><td>0.222</td><td>0.222</td><td>0.333</td></tr><tr><td> $X_2$ </td><td>0.244</td><td>0.286</td><td>0.286</td><td>0.286</td><td>0.143</td></tr><tr><td> $X_3$ </td><td>0.091</td><td>0.211</td><td>0.211</td><td>0.199</td><td>0.378</td></tr><tr><td> $X_4$ </td><td>0.253</td><td>0.316</td><td>0.316</td><td>0.158</td><td>0.210</td></tr><tr><td> $X_5$ </td><td>0.169</td><td>0.286</td><td>0.286</td><td>0.286</td><td>0.143</td></tr><tr><td>Software</td><td>0.333</td><td></td><td></td><td></td><td></td></tr><tr><td> $X_6$ </td><td>0.400</td><td>0.286</td><td>0.286</td><td>0.286</td><td>0.143</td></tr><tr><td> $X_7$ </td><td>0.200</td><td>0.250</td><td>0.250</td><td>0.250</td><td>0.250</td></tr><tr><td> $X_8$ </td><td>0.400</td><td>0.273</td><td>0.273</td><td>0.273</td><td>0.182</td></tr><tr><td>Support</td><td>0.333</td><td></td><td></td><td></td><td></td></tr><tr><td> $X_9$ </td><td>0.352</td><td>0.375</td><td>0.250</td><td>0.125</td><td>0.250</td></tr><tr><td> $X_{10}$ </td><td>0.235</td><td>0.316</td><td>0.284</td><td>0.142</td><td>0.258</td></tr><tr><td> $X_{11}$ </td><td>0.062</td><td>0.275</td><td>0.347</td><td>0.277</td><td>0.102</td></tr><tr><td> $X_{12}$ </td><td>0.139</td><td>0.351</td><td>0.351</td><td>0.109</td><td>0.189</td></tr><tr><td> $X_{13}$ </td><td>0.139</td><td>0.333</td><td>0.333</td><td>0.111</td><td>0.222</td></tr><tr><td> $X_{14}$ </td><td>0.072</td><td>0.315</td><td>0.315</td><td>0.153</td><td>0.216</td></tr><tr><td>Weighted score</td><td></td><td>0.295</td><td>0.280</td><td>0.213</td><td>0.212</td></tr><tr><td>Ranking</td><td></td><td>1</td><td>2</td><td>3</td><td>4</td></tr></table>

To check whether the utility of this attribute is independent of the utilities of the remaining attributes, we addressed the same question to the decision maker several times, each time defining different levels for the remaining attributes. We found that the utility of the attribute did not change when the fixed levels of the remaining attributes were changed, and therefore concluded that the assumption of utility independence for this attribute is valid. Similarly, we checked the assumption with regard to all the attributes, and we found that the assumption holds.

## 4.3.2. Checking Preference Independence

This procedure examines the assumption that preference between each pair of attributes is independent of the fixed levels of the remaining attributes. We verify the assumption for the pair of attributes: “quality of documentation” and “memory capacity”. Two alternatives were given to the evaluator. In the first alternative, “quality of documentation” was 2 (on a scale of 1–5) and “memory capacity” was 768K. In the second alternative, “quality of documentation” was 4 and “memory capacity” was $X'$ . The remaining attributes in the two alternatives were at similar levels and at their highest values.

The evaluator was asked to determine the value of “memory capacity” $X'$ in the second alternative at which he will be indifferent to the choice between the two alternatives. The evaluator determined $X'$ at 576K. Then the fixed values of the rest of the attributes in the two alternatives were changed to their lowest level, and again the two alternatives were reintroduced to the evaluator. His answer to the level of $X'$ did not change. In this manner we checked for various combinations of the two attributes and found out that the different values of the remaining attributes did not affect the evaluator's preferences. Thus, we conclude that preference between the two attributes is independent of the other attributes.

Similarly, we examined the assumption for the rest of the attribute pairs and we found that the assumption does hold for all the attribute pairs.

## 4.3.3. Evaluating the Utilities of Attributes

Having found that the independence assumptions hold, we proceeded to evaluate the utilities of the attributes. In our case the attributes had been organized hierarchically (in three groups). Although the utility model can be applied when the attributes are arranged hierarchically [9], its application is more difficult. Therefore we decided to treat all 14 attributes as one list and ignore their classification into groups.

Additionally, we decided not to build a continuous utility curve for all attributes (a task which involves unnecessary and tedious work). For our purposes it was necessary to compute the utilities of each attribute in at most 4 values, for each of the four proposals.

The process of evaluating the utilities of each attribute involved two stages. In the first, the evaluator was asked to evaluate the highest value of the attribute (where the utility is denoted as $U(X^{*})=1$ ), and the lowest value for the attribute (where the utility is denoted $U(X^{0})=0$ ).

In the second stage, the evaluator was asked to determine the utilities of the other specific values of each attribute. An example for the evaluation of the utility of the attribute “memory capacity” is:

\- Its highest value is 1060K; thus $U(1060\mathrm{K}) = 1$ .
- Its lowest value is 576K; thus $U(576\mathrm{K}) = 0$ . (Recall that 576K is the threshold level of "memory capacity"; see Table 1.)

\- In one of the proposals “memory capacity” was 768K. In order to evaluate the utility of this memory capacity the following question was posed to the evaluator.

“Assume there are two alternative microcomputer systems:

\- In one system, which you are certain to received, memory capacity is 768K.

\- In the second system, which is available by lottery, the probability is $p$ that the memory capacity will be 1060K and probability (1 - $p$ ) that it will be 576K. The remaining attributes in the two systems are at the same level. At which value of $p$ will you be indifferent to the choice between the two systems?"

\- The evaluator responded that he would be indifferent to the two alternatives at $p = 0.3$ . This value is the utility of “memory capacity” 768K.

In this manner we evaluated the utilities of all the attributes, occasionally testing the evaluator's consistency by placing different values for the other attributes (in the second alternative). Generally, we found that the evaluator was consistent. In the few cases of inconsistency, we repeated the evaluation process for that attribute.

The utilities obtained for each of the attributes, for the four proposals, are presented in Table 4.

## 4.3.4. Evaluation of the Scaling Factors (Weights)

The following example illustrates the process of evaluating the scaling factor $k_{i}$ of attribute “memory capacity”. The following question was addressed to the evaluator:

Utility values and scaling factors: the multi-attribute utility model

<table><tr><td rowspan="2">Attributes</td><td rowspan="2">Scaling factors</td><td colspan="4">Utility of proposals</td></tr><tr><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td> $X_1$ </td><td>0.08</td><td>0.6</td><td>0.6</td><td>0.6</td><td>0.1</td></tr><tr><td> $X_2$ </td><td>0.07</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.5</td></tr><tr><td> $X_3$ </td><td>0.04</td><td>0.9</td><td>0.9</td><td>0.8</td><td>1.0</td></tr><tr><td> $X_4$ </td><td>0.12</td><td>1.0</td><td>0.9</td><td>0.7</td><td>0.9</td></tr><tr><td> $X_5$ </td><td>0.07</td><td>1.0</td><td>0.9</td><td>1.0</td><td>0.8</td></tr><tr><td> $X_6$ </td><td>0.07</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.8</td></tr><tr><td> $X_7$ </td><td>0.15</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td> $X_8$ </td><td>0.10</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.9</td></tr><tr><td> $X_9$ </td><td>0.15</td><td>1.0</td><td>0.9</td><td>0.7</td><td>0.8</td></tr><tr><td> $X_{10}$ </td><td>0.10</td><td>1.0</td><td>0.9</td><td>0.6</td><td>0.9</td></tr><tr><td> $X_{11}$ </td><td>0.05</td><td>0.8</td><td>0.7</td><td>1.0</td><td>0.9</td></tr><tr><td> $X_{12}$ </td><td>0.09</td><td>1.0</td><td>1.0</td><td>0.9</td><td>1.0</td></tr><tr><td> $X_{13}$ </td><td>0.08</td><td>1.0</td><td>1.0</td><td>0.7</td><td>0.8</td></tr><tr><td> $X_{14}$ </td><td>0.12</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.9</td></tr><tr><td>k=-0.44268</td><td>1.29</td><td></td><td></td><td></td><td></td></tr><tr><td>Utility</td><td></td><td>0.973</td><td>0.944</td><td>0.882</td><td>0.905</td></tr><tr><td>Ranking</td><td></td><td>1</td><td>2</td><td>4</td><td>3</td></tr></table>

"Assume there are two alternative micro-computer systems:

\- In one system the memory capacity is 1060K, but the remaining attributes are at their lowest level. This is a system you are certain to receive.
- In the second system, available by lottery, the probability is $p$ that all its attributes are at their highest level and probability $(1 - p)$ that all its attributes are at their lowest level.

At which value of p will you be indifferent in choosing between the two alternatives?"

The evaluator responded that he would be indifferent at p = 0.08. Therefore, according to Section 3, $k_{i} = pk^{*} + (1 - p)k^{0}$ , and hence $k_{i} = 0.08$ .

The scaling factors of all attributes were determined similarly. Occasionally we checked for consistency by relating to different levels of attributes in the second alternative. The evaluator was generally consistent.

The scaling factors obtained are presented in Table 4. Since the total sum of the scaling factor is 1.29, we concluded that the decision maker is averse to risk, and therefore the multiplicative utility model was applied. The utility values and weights were then computed. Constant k (for the multiplicative model) was found from:

$$
1 + k = \prod_ {i = 1} ^ {1 4} \left(1 + k k _ {i}\right)
$$

giving k = -0.44268. Then the utility of each proposal was computed. The utilities and ranking are given in the two last lines of Table 4.

The ranking of the four proposals is identical to the ranking obtained with the additive-weight model, but is different from the ranking in the Eigenvector model in the reversed order of the third and fourth proposals.

## 5. Results and Conclusions

As Tables 2, 3 and 4 indicate, an almost identical ranking of the proposals was obtained with the three models. Only a minor and insignificant difference was found; according to all three models, system A ranked first. Thus, this system was selected without any reservation.

As mentioned earlier, it was pointless to take cost into consideration, since the difference in the cost of the proposals was insignificant. Had it been significant, the final choice would have been made by the benefit/cost technique.

What kind of conclusions can we draw from the comparisons we have made? Which model is preferable?

Tell [18] compared four models of selection, including the Eigenvector model and the multi-attribute utility model. He came to the conclusion that the Eigenvector model is easier to understand and to apply than the utility model. In our case study too the decision maker determined (at the end of the selection process) that the Eigenvector model is the easiest to use (because it did not require the determination of cardinal weights and scores, only pairwise preferences) and that the utility model is the most difficult to apply.

Shoemacker et al. [15] compared five models of decision making, including the three models that we used here. Their conclusion was that preference in using certain decision-making models is not unambiguous and depends on the specific characteristics of the problem.

Obviously, our comparison does not provide a “proof” as to which model to prefer. However, based on the attributes of the models in general, and on the limited experience gained in the application of the models in this case, we feel that the multi-attribute utility model is preferred for the following reasons:

a) This model is normative, based upon axioms which reflect the behavioral rules of the decision maker in determining preferences.

b) This is the only one of our models which checks assumptions of independence between attributes.

(c) This is the only model which takes into account the important issues of risk and uncertainty.

With these advantages of the multi-attribute utility model, one cannot ignore two difficulties which restrict its application:

a) The decision maker has difficulty in expressing preference between alternatives in the gambling technique [6].

b) The independence assumptions necessary for applying the models do not always hold. Although solutions were suggested for cases in which only a part of the assumptions hold [9], there are still cases where some of the assumptions do not hold. Thus, we come across two complementary limitations: first, the assumptions should be checked for each decision problem; and second, if, in fact, the assumptions do not hold, then the model is inapplicable.

The utility model is used in various fields of management science and decision making, and the difficulties described here exist in those domains also. Although we have not yet decided which decision model is preferable, and although the additive-weight model and the Eigenvector model are easier and simpler to apply, nevertheless we recommend adopting the multi-attribute utility model for the advantages of normativity, independence checking, and consideration of risk and uncertainty.

In cases wherein the independence assumptions do not hold, the utility model is inapplicable. Therefore the alternative model to use, in our opinion, is the Eigenvector model. This model is preferable to the additive-weight model because it allows one to test the decision maker's consistency and because it does not require the determination of cardinal values of weights and scores (although it does require more decisions).

We are aware of the difficulty in applying the utility model, but we believe that the difficulty should be resolved rather than ignored. We believe that the utility model will become easier to apply if an interactive decision support system for that purpose is developed. Such a system will guide the decision maker and help answer the various questions concerning the evaluation of utilities and scaling factors of the attributes. It is expected that the use of graphic aids in the system, along with the ability to explain and illustrate reactions expected from the user, will facilitate application of the model. It is our intention to develop a decision support system for this purpose. This system will also utilize alternative models in cases where the first model is not applicable.

## References

[1] Ahituv, N., “Techniques of Selecting Computers for Small Business”, Proceedings of the 24th Annual Conference of the International Council for Small Business, Quebec City, June 1979.

[2] Ahituv, N. and S. Neumann, Principles of Information Systems for Management, W.C. Brown Pub., Dubuque, Iowa, 1985.

[3] Borovit, I., Managing Computer Operations, Prentice-Hall, Englewood Cliffs, New Jersey, 1984.

[4] Davis, G.B. and M.H. Olson, Management Information Systems: Conceptual Foundations, Structure and Development, McGraw Hill, New York, 1985.

[5] Ein-Dor, P., “A dynamic approach to selecting computers”, Datamation, Vol. 23, June 1977, pp. 103–108.

[6] Hobbs, B.F., "Analytical multiobjective methods for power plant siting: a review of theory and applications", Division of Regional Studies, National Center for the Analysis of Energy Systems, Brookhaven National Laboratory, Upton, New York, 1979.

[7] Joslin, E.O., Computer Selection, Addison-Wesley, Reading, Mass. 1980.

[8] Keeney, R., “Multiplicative utility functions”, Operations Research, Vol. 22, 1974.

[9] Keeney, R. and H. Raiffa, Decisions with Multiple Objectives, John-Wiley and Sons, New York, 1976.

[10] Keeney, R., “Measurement scales for quantifying attributes”, Behavioral Science, Vol. 26, 1981, pp. 29–36.

[11] Lucas, H.C., Information Systems Concepts for Management, McGraw Hill, New York, 1978.

[12] Lucas, H.C. and J.R. Moor, “A multiple-criterion scoring approach to information system project selection”, Infor, Vol. 14, No. 1, February 1976.

[13] Lugasi, Y., A. Mehrez and Z. Sinuany-Stern, “Nuclear power plant site selection: a case study”, Nuclear Technology, Vol. 69, No. 1, April 1985, pp. 7–13.

[14] Saaty, T.L., “A scaling method for priorities in hierarchical structures”, Journal of Mathematical Psychology, Vol. 15, 1977.

[15] Schoemacker, P, and C. Waid, “An experimental comparison of different approaches to determining weights in the additive utility model”, Management Science, Vol. 28, No. 2, 1982, pp. 102–196.

[16] Seidmann, A. and A. Arbel, “Microcomputer selection process for Organizational Information Management”, Information & Management, Vol. 7, December 1984.

[17] Sharp, W.F., The Economics of Computers, Columbia Univ. Press, New York, 1979.

[18] Tell, B., “A comparative study of four multiple-criteria methods”, in H. Thirie and S. Zionts (eds.), Multiple Criteria Decision Making, Jouy-en-Josas, France, 1975, Springer-Verlag, New York, 1976.

[19] Timmreck, E., “Computer selection methodology”, Computer Surveys, Vol. 5, No. 4, December 1973.

[20] Von-Neuman, J. and O. Morgenstern, Theory of Games and Economic Behavior, 2nd Edition, Princeton University Press, Princeton, New Jersey 1947.
