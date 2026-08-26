---
otero_id: 18474
otero_key: "N3BS9HS2"
title: "Computer systems selection: The graphical cost-benefit approach"
authors: "Peretz Shoval; Yaacov Lugasi"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90071-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computer Systems Selection: The Graphical Cost-Benefit Approach

Peretz Shoval and Yaacov Lugasi

Department of Industrial Engineering and Management, Ben Gurion University of the Negev, Beer Sheva 84105, Israel

A graphical cost-benefit approach to computer systems selection is presented. Using a cost-benefit graph the decision maker can select among alternative computer systems while considering not only the cost/benefit ratio, but also the relative importance of the benefit and cost factors in a given situation. In order to utilize the graphical approach, cost values of the alternatives have to be transformed onto a normalized-cost scale. Various transformation methods, which are based on linear, subjective and utility theory approaches, are discussed. We recommend the use of the graphical cost-benefit approach in conjunction with a cost transformation based on the utility model; this allows incorporation of risk and uncertainty consideration into the selection process.

Keywords: Computer system selection, Cost-benefit analysis, Decision making styles, Evaluation models, Eigenvector model, Utility model, Risk and uncertainty.

![](/api/attachments/N3BS9HS2/fulltext/images/e8c629c62f8557193a6cfa7fe20543bd3a934625a177508784202571efe1ab10.jpg)

Paretz Shoval is on the faculty of the Department of Industrial Engineering & Management and the Department of Computer Science at Ben-Gurion University of the Negev in Israel. Previous affiliations include Tel-Aviv University and Hebrew University of Jerusalem. He received B.A. (Economics) and M.Sc. (Information Systems) from Tel-Aviv University, and Ph.D (Management Information Systems) from the University of Pittsburgh. Dr. Shoval's research and teaching interests include systems analysis & design methodologies, database design, expert systems for information retrieval, and economics of computing. He has published in journals such as Information & Management, Information Systems, Information Processing & Management, Int'l Journal of Man-Machine Studies, Data & Knowledge Engineering, and Data Base. Prior to moving into academia Dr. Shoval held managerial and consulting positions in computer companies and in the IDF.

## 1. Introduction

In selecting a computer system, hardware or software, the following stages can be identified [e.g., 1, 2, 13]:

(a) analysing the needs of the system,

(b) defining its requirements and attributes,

(c) issuing a request for proposal (RFP) to various suppliers,

(d) performing initial screening and then evaluating and comparing the alternative proposals, using an appropriate evaluation model,

(e) selecting the best alternative (possibly with a benchmark) and making arrangements for acquiring the system,

(f) acceptance testing and acceptance.

This paper concerns the fourth stage, focusing on methods for comparing the costs and benefits of proposed alternatives. In the process of evaluation and selection, comparison of the alternatives should relate predicted benefits and costs. Ideally we would like to be able to express both expected benefits and costs in money values, and then to compare the benefit to the cost of each alternative. In reality, however, benefits aspect (unlike cost) is generally difficult to measure in monetary or other quantitative terms [3,4]. Therefore, usually a list of criteria or attributes required of the system is needed to specify the benefits; then a performance measure is decided for each attribute in any given system. While determining the measures for attributes, one must be careful in dealing with different values and avoid mixing different units. To overcome this, one can convert to a normalized scale. Once the attributes and their performance measures have been determined, an evaluation model can be applied in order to calculate the overall benefits of the alternatives. Various methods and models for that purpose have been discussed and compared in [13], including the efficiency frontier, lexicographical ordering, additive weight [9,12,14], cost value [5], Saaty's eigenvector [10,11] and Keeney's multi-attribute utility model [6,7,8]. In this paper we are not concerned with the pros and cons of the models. Suffice it to say, that we are able to compute or estimate the benefits of alternatives and express them on some scale (e.g., 0 to 1). Note that the cost factor is not included among the attributes that contribute to the benefit of a system. Costs of alternative systems may be composed of various components and be spread over different time horizons. Nevertheless, unlike benefits, cost can easily be measured in money values and there is usually no need to express cost in surrogate terms. It is only important to consider all types of cost and to express them in terms of their present values.

![](/api/attachments/N3BS9HS2/fulltext/images/31f8e6ef30f5da2629d061e38959ace5299d24cfb2e51f00c0739b4d230ebac2.jpg)  
Yanacov Legal specializes in industrial economics and decision making models. He earned B.Sc. and M.Sc. in Industrial Engineering from Ben-Gurion University of the Negev in Israel, where he is lecturing on the above topics. Additionally, he is consulting on information systems and industrial engineering.

Once the benefits of the alternative systems have been computed (using any of the above models), and the cost of each alternative has been calculated too, it remains to decide on the preferred system by comparing the benefit of each alternative to its cost.

## 2. Cost-Benefit Ratio

Given a set of alternative systems, each with calculated values of benefit and cost, a common way for selecting the preferred one is to divide the two factors and select the alternative with minimum (cost/benefit), or equivalently maximum (benefit/cost), where the first ratio expresses the cost of one unit of benefit, etc. An example is shown in Table 1, which details the benefit and cost of four alternative systems. Benefit is expressed on a 0–1 scale and cost in thousands of dollars. According to the cost/benefit ratio, alternative C is selected. Note that alternative D is inferior and could be eliminated from consideration because alternative C dominates it [cost(C) = cost(D) and benefit (C) > benefit(D)].

Table 1  
Cost/Benefit of Four Alternative Systems.

<table><tr><td rowspan="2">Factor</td><td colspan="4">Alternative</td></tr><tr><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>Cost</td><td>700</td><td>400</td><td>500</td><td>500</td></tr><tr><td>Benefit</td><td>0.9</td><td>0.5</td><td>0.8</td><td>0.6</td></tr><tr><td>Cost/Benefit</td><td>777.8</td><td>800</td><td>625</td><td>833.3</td></tr></table>

The cost-benefit method considers only the ratio between the two factors, but it does not consider their absolute values. Therefore, another alternative, with benefit 0.2 and cost 125, for example, is as good as alternative C - irrespective to the big difference in both cost and benefit between the two. The cost-benefit method does not consider the relative importance of the cost and benefit factors. These factors may be of different importance to the decision makers in different circumstances. There may be situations where the benefit factor, for example, is very important and cost considerations are of less concern (e.g., alternative A in Table 1), or other situations where the cost factor becomes crucial, e.g., lack of funds, and therefore benefit is perhaps sacrificed (e.g., alternative B). The importance of benefit and cost may vary: at one extreme the decision maker will select the most beneficial alternative irrespective (perhaps) of its high cost; at the other extreme select the least costly alternative, irrespective (perhaps) of its low benefit. In any other case the two factors may have varying importance, and the selection among the alternatives becomes sensitive to both the absolute values of cost and benefit, and to their relative importance.

## 3. Graphical Cost-Benefit Approach

To overcome the above limitations of the cost-benefit method a graphical cost-benefit approach is proposed. It enables the decision maker to consider and be sensitive to various levels of importance of benefit and cost. The method is show in Figure 1, where the alternatives A, B, and C from Table 1 are used. The two vertical axes are Benefit (B) and Normalized-Cost (NC). On the B axis are marked the benefit values of the alternatives, as obtained from the evaluation model. On the NC axis are marked normalized-cost values, i.e., cost values of the alternatives that are transformed in such a way that causes a more costly alternative to be lower on the scale, and a less costly one to be higher on the scale (transformation methods will be discussed in the sequel).

![](/api/attachments/N3BS9HS2/fulltext/images/5912b816533373cefd00225d56aadabe6b127a3eb876cb8664f7a0ec582a1dfa.jpg)  
Fig. 1. Cost-Benefit Graph: Method 'A' Transformation.

The horizontal axis is the weights scale, expressing the relative importance or weight of the benefit and cost factors. The weights scale is 0 to 1: at the intersection point with the B axis the weight of benefit (p) is 1 and that of cost (1 - p) is 0, etc. The line that connects between the B and NC values of each alternative signifies the expected benefit of the alternative at any given point on the weights axis. Let us refer now to the specific example in Figure 1. In this, the following cost transformation formula is applied:

$\mathbf{NC}(\min) = \mathbf{B}(\max)$ ;

$$
\mathrm{NC} (\mathrm{i}) = \frac {\mathrm{NC} (\min) \cdot \mathrm{C} (\min)}{\mathrm{C} (\mathrm{i})}.
$$

This method assigns to the least costly alternative a normalized-cost value which equals the value of the most beneficial alternative; the normalized-cost of any other alternative is decreased proportionally. Using the cost and benefit values of alternative A, B, and C we get:

$$
\mathrm{NC} (\mathbf {B}) = 0. 9; \quad \mathrm{NC} (\mathbf {A}) = \frac {0 . 9 \cdot 4 0 0}{7 0 0} = 0. 5 1;
$$

$$
\mathrm{NC} (\mathrm{C}) = \frac {0 . 9 \cdot 4 0 0}{5 0 0} = 0. 7 2.
$$

These values are marked on the NC axis and then connected to the respective points on the B axis. The lines of alternatives A and C intersect at point c.a, and the lines of alternative B and C intersect at b.c. The upper cover of the intersecting lines is of importance because it expresses the maximal expected benefit of all alternatives at any point on the weight axis. An alternative that is fully under this line is inferior and need not be considered at all (this would have been the case had we marked the appropriate line for alternative D of Table 1).

The decision on the preferred alternative depends now on the decision maker; i.e., on the relative importance of cost and benefit. In our example, for any point on the axis to the left of intersection b.c, alternative B is preferred; for any point which is to the right of the intersection c.a, alternative A is preferred; only at points which are in between is alternative C preferred. The weights (p) of benefit for which the pairs of lines intersect are 0.38 (for b.c) and 0.67 (for c.a); the calculations are shown in the Appendix part 1.

Thus we find that alternative C is preferred only when $0.38 \leq p \leq 0.67$ . This result should be compared to the initial cost–benefit method, which resulted in alternative C preferred at any rate.

## 4. Other Cost Transformations

In Figure 1, we utilized one method for transforming cost values onto the NC scale. Other transformations are possible. Figure 2 shows a transformation based on the formula:

$$
\begin{array}{l} \mathrm{NC(max)=B(min);} \\ \mathrm{NC(i)} = \frac {\mathrm{NC(max)} \cdot \mathrm{C(max)}}{\mathrm{C(i)}}. \end{array}
$$

This assigns to the most costly alternative a normalized-cost value which equals the value of the least beneficial alternative; the normalized-cost of any other alternative is increased proportionally. For the same three alternatives we get now:

$$
\begin{array}{l} \mathrm{NC(A)} = 0. 5; \quad \mathrm{NC(B)} = \frac {0 . 5 \cdot 7 0 0}{4 0 0} = 0. 8 7; \\ \mathrm{NC(C)} = \frac {0 . 5 \cdot 7 0 0}{5 0 0} = 0. 7. \end{array}
$$

We see in Figure 2 that the lines of the same pairs of alternatives intersect (at points b.c andc.a), so again the decision maker should consider alternatives B, or C, or A, depending on the relative importance of the cost and benefit factors. We calculate the weights (p) at the points of intersection (see Appendix part 2) and find out that this time alternative C is preferred when $0.37 \leq p \leq 0.67$ , whereas when p > 0.67 alternative A is preferred, and when p < 0.37, alternative B is preferred. Compared to Figure 1 the points on the weights axis, between which alternative C is preferred, shifted somewhat to the left, i.e., towards the cost factor. This happened because in the current transformation the NC values became smaller compared to the formed method (while B values did not change).

Obviously there is a problem here, since the two methods of transformation yield somewhat different results, at least in some range of weights. To amplify the problem we show, in Figure 3, a third transformation, based on the following scheme: first, a maximal value of cost is determined; this reflects the maximum cost that the decision maker is willing to pay for any alternative. Then, the normalized cost of each alternative is determined as the difference between that maximum and the actual cost of the alternative, divided by the maximum cost. Hence,

![](/api/attachments/N3BS9HS2/fulltext/images/6e961e46fbb0458f0ac37905878cf9f851246f699de5d11cc17e8af1caf231df.jpg)  
Fig. 2. Cost-Benefit Graph: Method 'B' Transformation.

![](/api/attachments/N3BS9HS2/fulltext/images/96cadb4c02dcd7d065cb85708ed94b671b9d3cf38ede4f5774f5bec679461d31.jpg)  
Fig. 3. Cost-Benefit Graph: Method 'C' Transformation.

$$
\mathrm{NC} (\mathrm{i}) = \frac {\max . \text { cost } - \text { cost } (\mathrm{i})}{\max . \text { cost }}.
$$

In our example, if max. cost = 850,

$$
\mathrm{NC(A)} = \frac {(8 5 0 - 7 0 0)}{8 5 0} = 0. 1 8;
$$

$$
\mathrm{NC} (\mathbf {B}) = \frac {(8 5 0 - 4 0 0)}{8 5 0} = 0. 5 3;
$$

$$
\mathrm{NC(C)} = \frac {(8 5 0 - 5 0 0)}{8 5 0} = 0. 4 1.
$$

Here again, the lines of the same pairs of alternatives intersect (at points marked b.c and c.a), but this time the respective points on the weights axis are 0.28 and 0.70 (see computation in the Appendix part 3). Here C is preferred when p is in the larger range of $0.28 \leq p \leq 0.7$ , because this transformation caused the NC value of alternative A to decrease and that of alternative B to increase in greater proportion than the previous two cases.

We now have three methods for cost transformation, but although the advantages of the graphical cost-benefit method over the plain cost-benefit method have been clarified, a new problem has been encountered: that of determining which transformation scheme to use, since each yields a different range of weights of cost and benefit factors. To overcome this problem, a different approach to cost transformation should be considered.

## 5. Subjective Cost Transformation: The Eigenvector Method

The former methods were based on a linear transformation of the cost values, where each time a different basis was used. Now a different transformation scheme is considered, which is based on a subjective transformation, based on Saaty's eigenvector model. It enables determination of preference among alternatives using a matrix to perform pairwaise comparisons between the alternatives. In order to determine preference among n alternatives, the decision maker enters values into an $n \times n$ matrix, using pairwise comparisons between all alternatives. Thus, in each cell $(i, j)$ , the decision maker expresses the relative importance of alternative i with respect to alternative j. (It is only necessary to enter half of the matrix, as it is symmetrical). Then the eigenvector of the matrix is calculated for the maximal eigenvalue, and normalized, so that the sum of its elements is 1. The values of this eigenvector constitute the scores of the alternatives.

Table 2  
Saaty's Matrix for Pairwise Comparisons.

<table><tr><td rowspan="2">i</td><td colspan="4">j</td></tr><tr><td>A</td><td>B</td><td>C</td><td>Normalized Eigenvector</td></tr><tr><td>A</td><td>1</td><td> $1/6$ </td><td> $1/4$ </td><td>0.09</td></tr><tr><td>B</td><td>6</td><td>1</td><td>2</td><td>0.56</td></tr><tr><td>C</td><td>4</td><td> $1/2$ </td><td>1</td><td>0.35</td></tr></table>

Saaty's model can be utilized as a method for cost transformation. In our case, the decision maker enters values into a matrix in which a pairwise comparison is made between the cost values. Thus, each cell (i, j) expresses the relative preference of (the cost of) alternative i with respect to j. Obviously, an alternative which is less costly is preferred. An example is shown in Table 2. It is based on the same initial alternatives. A 1–9 scale is used for the comparisons.

The last column of Table 2 shows the normalized eigenvector of the matrix, for the maximal eigenvector. The values of this eigenvector are used as NC values in the respective cost-benefit graph, as shown in Figure 4.

The points at which the lines of alternatives A, C and alternatives B, C intersect are 0.72 and 0.42, respectively (see Appendix part 4), and hence alternative C is preferred at the range $0.42 \leq p \leq 0.72$ .

A transformation of cost based on the eigenvector model considers the relative importance, or preference, of each cost value, compared to the others. This, in our opinion, is preferable to the previous linear models. Moreover, it enables one to examine the decision maker's consistency, using appropriate means (details are beyond the scope of this paper). A drawback is that it is not based on a normative model of a decision maker reflecting behavioral rules and considering risk and uncertainty.

## 6. Cost Transformations Based on the Utility Model

We next propose Keeney's utility model for the purpose of cost transformation. The application of the model to the case of computer system evaluation and selection is described in [13]. The model allows evaluation of the utility function of the decision maker for a set of attributes. In order to evaluate the utility function a gambling technique is used: a utility function of the Von-Neuman -Morgenstern type [15]. It is based on the transitivity and continuity axioms of preference, thus enabling the decision maker to form a utility function.

![](/api/attachments/N3BS9HS2/fulltext/images/a80b8d95954fdeda3c83ebc39847372017ffea0dc67a8472beed0790b7619e29.jpg)  
Fig. 4. Cost-Benefit Graph: Transformation based on Saaty's Eigenvector Model.

The utility model can be applied to our cost transformation problem; from a given set of cost values (of the alternatives) the utility function, termed “utility of cost”, will be evaluated. To define the “utility of cost”, we first define a cost value $C_{i}^{*}$ for which the utility $U(C_{i}^{*}) = 1$ , and a cost value $C_{i}^{\circ}$ for which $U(C_{i}^{\circ}) = 0$ . For a given set of cost values (of the alternatives) it is straightforward to take the two extreme cost values, such that $C_{i}^{*}$ is the least costly alternative and $C_{i}^{\circ}$ is the most costly one. In our example $C_{B}^{*} = 400$ and $C_{A}^{\circ} = 700$ , and hence: $U(400) = 1$ and $U(700) = 0$ . Thus, two extreme points have been obtained on the “utility of cost” curve. Now, in order to evaluate the utility of a particular level of cost (denoted $C_{i}^{\prime}$ ) we address the following question to the decision maker:

"You have the following two options:

option 1: the cost of alternative i is $\mathbf{C}_i'$ , and you are sure of obtaining this alternative.

option 2: the cost of alternative i is given on a lottery card, in which there is probability q that the cost is $C_{i}^{*}$ and probability (1 - q) that the cost of the alternative is $C_{i}^{e}$ . Remaining attributes are at the same fixed level. At which value of q will you be indifferent to the choice between the two options?"

When the decision maker is indifferent to both options 1 and 2, we say that the “utility of cost” of the first option equals the expected “utility of cost” of the second option. That is to say:

$$
\mathbf {U} \left(\mathbf {C} _ {\mathrm{i}} ^ {\prime}\right) = \mathbf {q} \cdot \mathbf {U} \left(\mathbf {C} _ {\mathrm{i}} ^ {*}\right) + (1 - \mathbf {q}) \cdot \mathbf {U} \left(\mathbf {C} _ {\mathrm{i}} ^ {\circ}\right).
$$

Since $\mathbf{U}(\mathbf{C}_i^*) = 1$ and $\mathbf{U}(\mathbf{C}_i^\circ) = 0$ , we obtain $\mathbf{U}(\mathbf{C}_i') = \mathbf{q}$ .

That is to say, the probability is the “utility of cost” of alternative i. In this way we can find the “utility of cost” of various alternatives.

Returning to our example, we have already determined that for alternative A, U(700) = 0, and for alternative B, U(400) = 1. We now calculate U(500), the utility of the cost of alternative C, which is the probability (q) that will be determined by the decision maker to be the condition for indifferent to getting this alternative or the other two. This probability depends, of course, on the attitude to risk. Three possibilities exist: that the decision maker is (a) indifferent to risk; b) averse to risk; or c) seeks risk. We now examine the “utility of cost” of alternative C for these possibilities.

(1) The decision maker is indifferent to risk:

For this case let us assume that q = 0.67, i.e.:

$$
\begin{array}{r l} \mathrm{U(500)} & = \mathrm{q} \cdot \mathrm{U(400)} + (1 - \mathrm{q}) \cdot \mathrm{U(700)} \\ & = 0. 6 7 \cdot 1 + (1 - 0. 6 7) \cdot 0 = 0. 6 7. \end{array}
$$

The expected cost of option 2 with q = 0.67 yields: $0.67 \cdot 400 + (1 - 0.67) \cdot 700 = 500$ . Hence, the expected cost of option 2 equals the cost of option 1.

(2) The decision maker is averse to risk:

For this case let us assume that q = 0.9, i.e., U(500) = 0.9. The meaning here of risk aversion is that the condition for the decision maker to select the uncertain option 2 is a higher probability (0.9 > 0.07) for getting the less costly system. The expected cost here is less than the cost of the alternative the decision maker is sure to obtain:

$$
0. 9 \cdot 4 0 0 + (1 - 0. 9) \cdot 7 0 0 = 4 3 0 <   5 0 0.
$$

(3) The decision maker seeks risk:

Here we assume that q = 0.4. The meaning of risk seeking is that the decision maker will select the uncertain option (2) for a lower probability $(0.4 < 0.67)$ of getting the less costly system. The expected cost is now more than the cost of the sure option:

$$
0. 4 \cdot 4 0 0 + (1 - 0. 4) \cdot 7 0 0 = 5 8 0 > 5 0 0.
$$

The above three cases are summarized in Figure 5, which suggests the form of the utility curves for the three decision making styles. The horizontal axis is the cost values (from high to low) and the vertical axis is the “utility of cost”: (1) signifies a decision maker indifferent to risk, (2) risk averse, and (3) for a risk seeker.

The appropriate q values for the cost 500 (of alternative C) are marked on the utility axis.

Now that we have seen three possible transformations of cost values for three decision making styles, we are ready to return to the cost-benefit graph, and to examine which of the three original alternatives is preferable, and the level of importance of their cost and benefit factors.

![](/api/attachments/N3BS9HS2/fulltext/images/3c88f2156e84eaef57093f37281cab7e674d3975ec23662d2e4df5ea2ece457d.jpg)  
Fig. 5. Utility Curves of Three Decision Making Styles.

![](/api/attachments/N3BS9HS2/fulltext/images/31c5383ab80c86fe74c621485aac34d16923e4bc5ed00ce09630b3862b67e551.jpg)  
Fig. 6. Cost-Benefit Graph: Transformation based on Keeny's Utility Model.

Figure 6 shows the cost-benefit graphs of the three cases. For alternatives A and B the NC values (in all cases) are 0 and 1, respectively. For alternative C, three different NC values are marked, for the three different decision making styles, and hence three different lines are drawn of this alternative: line $\mathbf{C}_1$ (for $q = 0.67$ ), line $c_2$ (for $q = 0.9$ ), and line $c_3$ (for $q = 0.4$ ).

For the three cases (C lines) three different sets of intersection points between pairs of alternatives are obtained. The p values, on the weights axis, are (per computation in Appendix part 5):

(1) for the case of $C_{1}$ (indifferent to risk):

$$
0. 5 3 \leq p \leq 0. 8 7;
$$

$$
\begin{array}{l} \text {(2) for the case of C_{2} (risk averse):} \\ 0. 2 5 \leq p \leq 0. 9; \end{array}
$$

$$
\begin{array}{l} \text {(3) for the case of C_{3} (risk seeker):} \\ 0. 6 7 \leq p \leq 0. 8. \end{array}
$$

What can be learned from this? We learn that the more the decision maker seeks risk, the narrower is the range of p to prefer alternative C; the more risk averse, the wider is the range for the alternative.

The behavior of a person who is risk averse is more similar to the behavior of a decision maker who takes the “pure” cost-benefit approach, according to which alternative C is preferred at any rate. The opposite is true for a risk seeker, who tends to prefer the “certain” alternative C less.

Considering in more detail the case of a risk seeker, we see that, in some situations, alternative C will not be considered at all, only alternative A or B will be selected. This will happen for q values that cause line $C_{3}$ to be below the point of intersection between lines A and B. At that point:

0.9·p + 0·(1 - p)

$$
= 0. 5 \cdot p + 1 \cdot (1 - p); \Rightarrow p = 0. 7 1.
$$

At p = 0.71 the following equation holds:

$$
0. 9 \cdot 0. 7 1 + 0. 9 \cdot (1 - 0. 7 1)
$$

$$
= 0. 8 \cdot 0. 7 1 + q \cdot (1 - 0. 7 1),
$$

from which we obtain: q = 0.25.

Therefore, if the decision maker (who seeks risk) is indifferent between the two options at $q \leq 0.25$ the cost-benefit graph method shows that alternative C will never be selected. Rather, if the importance of the benefit $p \geq 0.71$ (and that of the cost $(1-p)\leq0.29$ the decision maker will prefer alternative A. and alternative B if the importance of benefit is $p\leq0.71$ .

A cost transformation based on Keeney's utility model is, in our opinion, preferable to the other methods, because it is based on a normative model, including axioms that reflect behavioral rules of the decision maker in determining preference, considering the important factors of risk and uncertainty. The difficulty in applying the utility model is minimized, since the utility of just a few cost values must be determined. The combination of the graphical cost–benefit methods, in conjunction with the utility model for cost transformation, seem to be the appropriate method for selecting among alternative computer systems.

## 7. Conclusions

This paper is a continuation of our earlier paper [13] where we discussed methods for measuring and comparing benefits. In this, we concentrate on the final comparison of benefit to cost.

We use the graphical tool to clarify why the cost-benefit ratio alone is not sufficient, and why it is important to consider also the absolute values of the parameters, their relative importance to the decision maker, and his attitude to risk and uncertainty. We succeed in combining cost-benefit graphs with both Saaty's Eigenvector model and Keeny's utility function approach. We do not sacrifice algorithms for graphs; we combine them. Graphs enable us to highlight what is otherwise "hidden" in the (trivial) cost-benefit ratio.

This may seem a typical OR problem. However, we feel that the main contribution is not just the introduction of a graph: it is the analysis of various ways to normalize cost, and the combination of it with the Eigenvector and utility models. We also have shown the connection between cost-benefit considerations and decision styles (i.e., attitude to risk and uncertainty).

In order to “modularize” the technique, since evaluators presumably have access to a computer, we have created a model of the technique using LOTUS. The model accepts cost and benefit values of a given set of alternatives, and produces cost-benefit graphs, as based on the methods of transformation discussed. It also computes the p-values, that signify the weight/importance of cost and benefit factors at which different alternatives are preferred.

## Appendix

Computations of p Values for the Various Cost Transformation Methods.

1. Linear transformation method A (see Fig. 1):
(a) for intersection point c.a: $0.9p + 0.51(1 - p) = 0.8p + 0.72(1 - p) \Rightarrow p = 0.67$

(b) for intersection point b.c: $0.8\mathbf{p} + 0.72(1 - \mathbf{p}) = 0.5\mathbf{p} + 0.9(1 - \mathbf{p})\Rightarrow$ $\mathbf{p} = 0.38.$

2. Linear transformation method B (see Fig. 2):

a) for intersection point c.a: $0.9\mathrm{p} + 0.5(1 - \mathfrak{p}) = 0.8\mathrm{p} + 0.7(1 - \mathfrak{p})\Rightarrow$ $\mathfrak{p} = 0.67$

(b) for intersection point b.c: $0.8p + 0.7(1 - p) = 0.5p + 0.87(1 - p) \Rightarrow p = 0.37.$

3. Linear transformation method C (see Fig. 3):

(a) for intersection point c.a: $0.9\mathrm{p} + 0.18(1 - \mathbf{p}) = 0.8\mathrm{p} + 0.41(1 - \mathbf{p})\Rightarrow$ $\mathfrak{p} = 0.7$

(b) for intersection point b.c: $0.8p + 0.41(1 - p) = 0.5p + 0.53(1 - p) \Rightarrow p = 0.28.$

4. Subjective transformation based on the eigenvector model (see Fig. 4):

(a) for intersection point c.a: $0.9\mathbf{p} + 0.09(1 - \mathbf{p}) = 0.8\mathbf{p} + 0.35(1 - \mathbf{p})\Rightarrow$ $\mathbf{p} = 0.72$

(b) for intersection point b.c.: $0,8p + 0.35(1 - p) = 0.5p + 0.56(1 - p) \Rightarrow p = 0.42.$

5. Transformations based on the utility model (see Fig. 6):

(1) The case of $c_{1}$ (indifferent to risk):

$$
\begin{array}{l} \text {(a) for intersection point c_{1}.a:} \\ 0. 9 p + 0 (1 - p) = 0. 8 p + 0. 6 7 (1 - p) \Rightarrow \\ p = 0. 8 7 \end{array}
$$

(b) for intersection point b.c₁:
0.8p + 0.67(1 - p) = 0.5p + 1(1 - p) ⇒
p = 0.53.

(2) The case of $\mathbb{C}_2$ (risk averse):

(a) for intersection point $c_2.a$ : $0.9p + 0(1 - p) = 0.8p + 0.9(1 - p) \Rightarrow p = 0.9$

(b) for intersection point b.c₂:
0.8p + 0.9(1 - p) = 0.5p + 1(1 - p) ⇒
p = 0.25.

(3) The case of $c_{3}$ (risk seeker):

(a) for intersection point $c_3 \cdot a$ : $0.9p + 0(1 - p) = 0.8p + 0.4(1 - p) \Rightarrow p = 0.8$

(b) for intersection point b.c₃:
0.8p + 0.4(1 - p) = 0.5p + 1(1 - p) ⇒
p = 0.67.

## References

[1] I. Borovitz, Management of Computer Operations, Prentice-Hall, Englewood Cliffs, N.J., 1984.

[2] i. Borovitz and M. Zviran, "Computer-family selection methodology for organizational information system", Information & Management, Vol. 12 (3), March 1987. pp. 107-115.

[3] G.B. Davis and M.H. Olson, Management Information Systems: Conceptual Foundations, Structure and Development, McGraw Hill, New York, N.Y., 1985.

[4] P. Ein-Dor, "A dynamic approach to selecting computers", Datamation, Vol. 23 (6), June 1977, pp. 103-108.

[5] E.G. Joslin, Computer Selection, Addison-Wesley, Reading, Mass., 1980.

[6] R. Keeney, "Multiplicative utility functions", Operations Research, Vol. 22, 1974.

[7] R. Keeney and H. Raiffa, Decisions with Multiple Objectives, John-Wiley and Sons, New York, N.Y., 1976.

[8] R. Keeney, "Measurement scales for quantifying attributes", Behavioral Science, Vol. 26, 1981, pp. 29–36.

[9] H.C. Lucas and J.R. Moor, "A multiple-criterion scoring approach to information system project selection", Infor, Vol. 14, (1), February 1976.

[10] T.L. Saaty, "A scaling method for priorities in hierarchical structures", Journal of Mathematical Psychology, Vol. 15, 1977.

[11] A. Seidmann and A. Arbel, "Microcomputer selection process for organizational information management", Information & Management, Vol. 7, December 1984.

[12] W.F. Sharp, The Economics of Computers, Columbia Univ. Press, New York, N.Y., 1979.

[13] P. Shoval and Y. Lugasi, "Models for computer system evaluation and selection", Information & Management, Vol 12 (3), March 1987, pp. 117–129.

[14] E. Timmreck, “Computer selection methodology”, Computing Surveys, Vol. 5 (4), December 1973.

[15] J. Von-Neuman and O. Morgenstern, Theory of Games and Economic Behavior, 2nd Edition, Princeton Univ. Press, Princeton, N.J., 1947.
