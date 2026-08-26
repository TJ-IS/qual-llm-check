---
otero_id: 4540
otero_key: "2BQ64NRW"
title: "Visualizing decision process on spheres based on the even swap concept"
authors: "Han-Lin Li; Li-Ching Ma"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.01.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Visualizing decision process on spheres based on the even swap concept

Han-Lin Li <sup>a</sup>, Li-Ching Ma <sup>b,⁎</sup>

<sup>a</sup> Institute of Information Management, National Chiao Tung University, Taiwan, ROC Department of Information Management, National United University, Taiwan, ROC

Received 24 April 2007; received in revised form 11 October 2007; accepted 21 January 2008 Available online 4 February 2008

## Abstract

The Even Swap method, originally outlined by Benjamin Franklin 230 years ago, is a rational way of finding the best alternative by evenly swapping decision criteria. This study develops a Decision Ball model to assist a decision maker in ranking alternatives and visualizing decision process based on the Even Swap concept. By viewing the moving trajectories of alternatives on spheres, a decision maker can specify trade-offs among criteria via the Even Swap process thus ranking alternatives more consistently © 2008 Elsevier B.V. All rights reserved.

Keywords: Visualization; Preference; Even Swap; Decision balls; Ranking

## 1. Introduction

In a multi-criteria decision making process, the more the decision criteria, the more the difficulties the decision maker (DM) has to face. Therefore, assistance in making reliable trade-offs among criteria thus ranking alternatives consistently is a critical issue in management research.

More than 230 years ago, Benjamin Franklin outlined the concept of Even Swaps in a letter (see Appendix A) about choosing between two alternatives. Franklin's fundamental idea is that if every alternative for a given criterion is rated equally, then the criterion can be ignored in making decision. Following this idea, Hammond, Keeney and Raiffa developed a mechanism for Even Swaps to provide a useful way for making trade-offs with a range of criteria across a range of alternatives [14]. “Even” implies equivalence and “Swap” represents exchange. An even swap increases the value of one criterion while decreasing the value of another criterion by an equivalent amount. By iteratively crossing out equally rated criteria to reduce the number of criteria, the best option can be determined.

The Even Swap method is an algorithm for multicriteria decision making under certainty. Each alternative has a scaled ranking of a number of criteria, some positive and the remainder negative. The DM is asked to make a number of indifferent judgments between the original alternative and the modified alternative. These adjustments are made to equalize all alternatives with respect to one of the criteria, thus rendering it irrelevant in the comparison. By successively applying this principle, as suggested by Benjamin Franklin, and recognizing when one alternative is dominated by another, alternatives can be ruled out until only one remains.

The Even Swap approach is a rational and practical way for finding the most preferred alternative. However, current Even Swap methods have the following inadequacies:

(i) Only the most preferred alternative is found. In an actual decision environment, the DM may also want to know the second or the third preferred alternatives.

(ii) Some trade-offs of criteria values, as specified by the DM, may not be consistent with each other. Current methods have no mechanism to check the consistency of these trade-offs.

(iii) The similarities among alternatives are not taken into account. Actually, the DM does not only want to know what the best option is but also the differences (or similarities) among alternatives.

The two main reasons for the above inadequacies in the current Even Swap methods are: First, they do not have a way to display differences (or similarities) among alternatives according to the trade-off values specified by the DM. Such a display can help the DM to see the differences among alternatives with different trade-off values. Second, they may not rank alternatives consistently according to even swaps made by the DM.

This study therefore develops a visualization model, the so called Decision Ball model, to assist a decision maker in ranking alternatives and visualizing decision process based on the Even Swap concept. By displaying all alternatives on spheres, the DM can see the differences among alternatives, can calculate the effects of different trade-off values, and can examine the moving trajectories of alternatives to check the consistency of even swaps. Thus, the DM can rank alternatives by viewing the adjustment outcomes displayed on the spheres.

Several graphic techniques have been developed to support decision-making process: for instance, deduction graphs to treat decision problems associated with expanding competence sets [19], a hyperbolic tree and a hierarchical list to visualize criminal relationships [23], and Gower Plots to detect inconsistencies in a decision maker's preferences and rank alternatives [11,12]. All these methods, however, used a 2-dimensional plane geometry to illustrate multidimensional data. A 2-dimensional plane model cannot depict three points that do not obey the triangular inequality (i.e. the total length of any two edges must be larger than the length of the third edge) neither can it display four points that are not on the same plane. For instance, as illustrated in Fig. 1, consider three points, A, B, C, where the distance between AB, BC, and AC are 3, 1, and 6, respectively, as shown in Fig. 1(b). It is impossible to show their relationships by three line segments on a 2-dimensional plane, as shown in Fig. 1 (a). If there are four points, A, B, C and D, which are not on the same plane, as shown in Fig. 1(c), it is impossible to present these four points on a 2-dimensional plane too.

Multidimensional scaling (MDS) [3,9] and a selforganizing map (SOM) [17] are commonly used techniques to map the similarities between points in a high dimensional space into a lower dimensional space (usually Euclidean). For instance, a visualization model, based on a scaling technique known as Sammon map [22], was proposed to visualize adjacency data [7]; a SOM network was extended to classify decision groups [16]; the fisheye views and fractal views were used to support the visualization of a category map based on SOM [24]. However, there are two restrictions in current multidimensional scaling and SOM models limiting their use in visualizing Even Swap process. First, they do not show inconsistencies in even swaps. Inconsistencies in preferences are common phenomena in decision-making. If these inconsistencies are significant, the reliability of decision-making might be reduced. Second, neither method displays the priorities of alternatives, which are essential for decision-making.

This study develops a Decision Ball model, based on the concept of multidimensional scaling techniques, to visualize Even Swap process on a sphere. A sphere model can display more information than a 2-dimensional plane model, and is easier to read than a 3-dimensional cube model. By mapping the alternatives into the points on the surface of a hemisphere, the Even Swap process is illustrated as moving trajectories among related points. The DM can examine these trajectories of points to obtain the information listed below:

![](/api/attachments/2BQ64NRW/fulltext/images/71b1a322be837b337cff7056a5d3857c1073462e7d6921a8b61c7c94c6e00c00.jpg)

![](/api/attachments/2BQ64NRW/fulltext/images/14c64b110e9343655189168616183a748f228257647030edcc8aa4cda24f9eae.jpg)

(c)  
![](/api/attachments/2BQ64NRW/fulltext/images/7950a046ef093646150bf1a9e8f559ac0da7c04fb79981d34d3223566df72b25.jpg)  
Fig. 1. Advantages of a sphere model (a) Display line segments on a 2-D plane (b) Display curves on a sphere (c) Display four points that are not on the same plane.

(i) Dissimilarities between alternatives. The longer the distance between alternatives on a sphere, the larger the dissimilarity between them.

(ii) The superiority (or dominance) of some alternatives over others by checking their longitude. Alternatives, which are located on the same longitude, exhibit clear dominance in relation to each other.

(iii) The consistency of even swaps by checking the latitude of alternatives after each even swap. The even swap, which causes the largest latitudinal shift of a given alternative, is the most inconsistent.

The proposed approach can be extensively applied in many fields. Possible applications are the selection of promotion plans in Marketing, investment decisions regarding financial products in Finance, evaluation of suppliers in Supply Chain Management, choice of colleges in Personal Decisions …etc.

This paper is organized as follows: Section 2 briefly reviews the conventional Even Swap method. Section 3 develops a Decision Ball model based on the Even Swap concept to rank and display alternatives forming the main theoretical part of this paper. Therefore, readers only interested in the application of proposed method can skip Section 3. Section 4 uses an example to demonstrate the whole decision process. Mathematical proofs of propositions and theorems are provided in the Appendices. A prototype Even Swap Decision Ball system has also been developed in this study, accessible from http://140.113.72.1/\~hlli01/index.htm to illustrate the usefulness of the proposed method.

## 2. Review of the conventional Even Swap method

Consider a set of alternatives $A = \{ A _ { 1 } , A _ { 2 } , . . . , A _ { \mathrm { n } } \}$ for solving a decision problem, where the decision maker selects m criteria to fulfill, denoted as $c _ { 1 } , . . . , c _ { m } .$ Suppose the decision problem is a discrete problem, in which no combination of alternatives can be selected. The conventional Even Swap method [13,14] begins by creating a consequence table specified by the DM. Such a table contains the consequences that the alternatives have for the given criteria. The DM can find the best alternative based on the following three steps.

Step 1. Eliminating dominated alternatives. The Even Swap method intends to eliminate as many alternatives as possible. Since the fewer the alternatives, the fewer the trade-offs the DM has to make. $A _ { i }$ is said to dominate $A _ { j }$ if alternative $A _ { i }$ is better than $A _ { j }$ in some criteria and no worse than $A _ { j }$ in all other criteria. All dominated alternatives are eliminated first.

Step 2. Choosing a target criterion. After eliminating dominated alternatives, the Even Swap method suggests that the DM chooses a target criterion whose values for all alternatives can be adjusted to be the same.

Step 3. Making even swaps. The DM chooses another criterion that can compensate for the changes in the target criterion. Then the DM assesses what changes in this criterion will compensate for the needed change in the target criterion. Finally, the even swaps are made and the target criterion is cancelled out.

Steps 1 through Step 3 are applied iteratively until the best alternative is found. Here, an example is given to illustrate the steps of the conventional Even Swap method.

Example 1. This example comes from Harvard Business Review [14] which describes a business problem: which office to rent. The DM has five major decision criteria to fulfill (Table 1): $( c _ { 1 } )$ sufficient space, $\left( c _ { 2 } \right)$ good access to his clients, $\left( c _ { 3 } \right)$ good office services, $( c _ { 4 } )$ a short commuting time from home to office, and $( c _ { 5 } )$ low cost. Office size is measured in square feet. The percentage of clients within an hour's drive from the office is used to measure the access to clients. A simple three-letter scale is used to describe the office services provided: $\mathbf { \ddot { \rho } } _ { \mathrm { A } } \mathbf { \vec { \rho } } _ { \mathrm { \vec { \rho } } }$ indicates full service; $\mathbf { \ddot { \delta B } } ^ { \prime \prime }$ means partial service; and $\mathrm { ^ { 6 6 } C ^ { 5 9 } }$ implies no service available. The commuting time is the average time in minutes needed to travel to work during rush hour, and cost is measured by monthly rent. Five alternative locations from $A _ { 1 }$ through $A _ { 5 }$ are considered. The two rightmost columns of Table 1 are the upper and lower bounds of each criterion, as illustrated in the next Section.

Using the Even Swap method, the problem can be solved as follows:

Iteration 1 bStep 1N The DM can eliminates $A _ { 5 }$ immediately because $A _ { 2 }$ dominates $A _ { 5 } .$ . The remaining alternatives are $A _ { 1 } , A _ { 2 } , A _ { 3 }$ and $A _ { 4 } . < \mathrm { S t e p } ~ 2 >$ The

Table 1  
The consequence table of Example 1 (A<sub>2</sub> ≻ A<sub>5</sub>)

<table><tr><td colspan="2">Criteria\Alternative</td><td>A1</td><td>A2</td><td>A3</td><td>A4</td><td>A5</td><td>Upper</td><td>Lower</td></tr><tr><td> ${\mathrm{c}}_{1}$ </td><td>Office size (Square feet)</td><td>800</td><td>700</td><td>500</td><td>950</td><td>700</td><td>1200</td><td>500</td></tr><tr><td> ${\mathrm{c}}_{2}$ </td><td>Customer access (%)</td><td>50</td><td>80</td><td>70</td><td>85</td><td>75</td><td>100</td><td>0</td></tr><tr><td> ${\mathrm{c}}_{3}$ </td><td>Office services</td><td>A</td><td>B</td><td>C</td><td>A</td><td>C</td><td>A</td><td>C</td></tr><tr><td> ${\mathrm{c}}_{4}$ </td><td>Commute (mins)</td><td>45</td><td>25</td><td>20</td><td>25</td><td>30</td><td>60</td><td>0</td></tr><tr><td> ${\mathrm{c}}_{5}$ </td><td>Monthly cost ($)</td><td>1850</td><td>1700</td><td>1500</td><td>1900</td><td>1750</td><td>2000</td><td>1500</td></tr></table>

DM chooses “commuting time” for target criterion. bStep 3N He decides to increase it from 20 to 25 for $A _ { 3 }$ and to decrease it from 45 to 25 for $A _ { 1 }$ so that the commuting time of all four alternatives would be equivalent. He uses 8 percentage points increase in customer access for $A _ { 3 }$ and 150 increases in monthly cost for $A _ { 1 }$ to compensate for the changes in commuting time for $A _ { 3 }$ and $A _ { 1 } ,$ , respectively (Table 2(a)). Iteration 2 bStep 1N The DM can eliminate $A _ { 1 }$ because $A _ { 4 }$ dominates $A _ { 1 }$ . The remaining alternatives are $A _ { 2 } , A _ { 3 }$ and $A _ { 4 } .$ . bStep 2N The DM chooses “office services” as a target criterion. bStep 3N He equates an increase in service level from C to B for $A _ { 3 }$ with a \$100 increase in monthly costs, and equates a decrease in service level from A to B for $A _ { 4 }$ with a \$100 decrease per month (Table 2(b)). Clearly, both “time” and “services” criteria are the same for all alternatives and can be eliminated.

Table 2  
Conventional even swap process of Example 1  
(a) (A4>A1)

<table><tr><td colspan="2">Alternative Criteria</td><td> ${\mathrm{A}}_{1}$ </td><td> ${\mathrm{A}}_{2}$ </td><td> ${\mathrm{A}}_{3}$ </td><td> ${\mathrm{A}}_{4}$ </td></tr><tr><td> ${\mathrm{c}}_{1}$ </td><td>Office size (Square feet)</td><td>800</td><td>700</td><td>500</td><td>950</td></tr><tr><td> ${\mathrm{c}}_{2}$ </td><td>Customer access (%)</td><td>50</td><td>80</td><td>70-78</td><td>85</td></tr><tr><td> ${\mathrm{c}}_{3}$ </td><td>Office services</td><td>A</td><td>B</td><td>C</td><td>A</td></tr><tr><td> ${\mathrm{c}}_{4}$ </td><td>Commute (mins)</td><td>45-25</td><td>25</td><td>20-25</td><td>25</td></tr><tr><td> ${\mathrm{c}}_{5}$ </td><td>Monthly cost ($)</td><td>1850-2000</td><td>1700</td><td>1500</td><td>1900</td></tr></table>

(c) (A4>A3)

<table><tr><td colspan="2">Criteria\Alternative</td><td>A2</td><td>A3</td><td>A4</td></tr><tr><td> ${\mathrm{c}}_{1}$ </td><td>Office size(Square feet)</td><td>700</td><td>500-700</td><td>950-700</td></tr><tr><td> ${\mathrm{c}}_{2}$ </td><td>Customeraccess (%)</td><td>80</td><td>78</td><td>85</td></tr><tr><td> ${\mathrm{c}}_{3}$ </td><td>Officeservices</td><td>B</td><td>B</td><td>B</td></tr><tr><td> ${\mathrm{c}}_{4}$ </td><td>Commute(mins)</td><td>25</td><td>25</td><td>25</td></tr><tr><td> ${\mathrm{c}}_{5}$ </td><td>Monthlycost ($)</td><td>1700</td><td>1600-1650</td><td>1800-1500</td></tr></table>

Iteration 3 bStep 1N There is no dominated alternative. bStep 2N “Office size” is chosen as target criterion. bStep 3N The DM equates an increase in office size from 500 to 700 for $A _ { 3 }$ with a \$50 increase in monthly costs, and equates a decrease in office size from 950 to 700 for $A _ { 4 }$ with a \$300 decrease per month (Table 2(c)). Iteration 4 bStep 1N Alternative $A _ { 3 }$ is eliminated because $A _ { 4 }$ dominates $A _ { 3 } ,$ . Only alternatives $A _ { 2 }$ and $A _ { 4 }$ are remaining now (Table 2(d)). bStep 2N The DM chooses “customer access” as a target criterion. bStep 3N He makes an even swap between customer access and monthly cost by increasing 5 percentage points access for $A _ { 2 }$ with an increase of \$100 per month. Iteration 5 bStep 1N Alternative $A _ { 2 }$ is eliminated because $A _ { 4 }$ dominates $A _ { 2 }$ . Since there is only one alternative remaining, the process can be terminated. Alternative $A _ { 4 }$ is the best option.

The Even Swap method provides a rational process for reaching the best option in making a decision. However, there still are some inadequacies. Take Example 1 for instance, illustrated as follows:

(b)

<table><tr><td colspan="2">Alternative Criteria</td><td> ${\mathrm{A}}_{2}$ </td><td> ${\mathrm{A}}_{3}$ </td><td> ${\mathrm{A}}_{4}$ </td></tr><tr><td> ${\mathrm{c}}_{1}$ </td><td>Office size (Square feet)</td><td>700</td><td>500</td><td>950</td></tr><tr><td> ${\mathrm{c}}_{2}$ </td><td>Customer access (%)</td><td>80</td><td>78</td><td>85</td></tr><tr><td> ${\mathrm{c}}_{3}$ </td><td>Office services</td><td>B</td><td>G、B</td><td>A、B</td></tr><tr><td> ${\mathrm{c}}_{4}$ </td><td>Commute (mins)</td><td>25</td><td>25</td><td>25</td></tr><tr><td> ${\mathrm{c}}_{5}$ </td><td>Monthly cost ($)</td><td>1700</td><td>1500、1600</td><td>1900、1800</td></tr></table>

(d) (A4> A2)

<table><tr><td colspan="2">Alternative Criteria</td><td>A2</td><td>A4</td></tr><tr><td> $c_{1}$ </td><td>Office size (Square feet)</td><td>700---</td><td>700---</td></tr><tr><td> $c_{2}$ </td><td>Customer access (%)</td><td>80-85</td><td>85</td></tr><tr><td> $c_{3}$ </td><td>Office services</td><td>-B---</td><td>-B---</td></tr><tr><td> $c_{4}$ </td><td>Commute (mins)</td><td>-25---</td><td>-25---</td></tr><tr><td> $c_{5}$ </td><td>Monthly cost ($)</td><td>1700-1800</td><td>1500</td></tr></table>

(i) As illustrated in Table $2 , A _ { 4 }$ is the most preferred alternative. However, it is difficult to say which one of $A _ { 1 } , A _ { 2 } , A _ { 3 }$ or $A _ { 5 }$ is second and which is third.

(ii) The dissimilarities among alternatives are difficult to determine. For example, as illustrated in Table 1, the DM finds it difficult to tell which are the dissimilarities among $A _ { 1 } , A _ { 2 } , A _ { 3 } , A _ { 4 }$ and $A _ { 5 } .$

(iii) Current Even Swap methods lack a mechanism for showing up serious inconsistencies in Even Swaps. (The detailed illustrations will be discussed in Section 3).

This study extends the concept of Even Swaps and proposes a model to assist the DM to rank alternatives, illustrate differences among alternatives, and check the inconsistencies of preferences.

## 3. The proposed decision ball model based on the even swap process

Consider a decision with a set of alternatives $A = \{ A _ { 1 }$ $A _ { 2 } , . . . , A _ { n } \}$ . The decision maker has m main decision criteria to fulfill, expressed as $c _ { 1 } , . . . , c _ { m } .$ Denote $c _ { i , k }$ as the kth raw criterion value of alternative $A _ { i } ,$ expressed as $A _ { i } { = } A _ { i } ( c _ { i , 1 } , . . . , c _ { i , k } , . . . , c _ { i , m } )$ . Denote $\underline { { c _ { k } } }$ and $\overline { { c _ { k } } }$ as the lower and upper bounds of the raw criterion value of $c _ { k }$ respectively. The value of $\underline { { c _ { k } } }$ and $\overline { { c _ { k } } }$ can be either given by the decision maker directly or calculated by the minimum and maximum raw criterion value of $c _ { k } .$ In Example 1, the value of $\underline { { c _ { k } } }$ and $\overline { { c _ { k } } }$ are assumed to be specified by the decision maker, as listed in the two rightmost columns of Table 1.

Here a sphere model based on the Even Swap process to rank n alternatives is proposed. An important assumption is that the proposed approach is dealing with objectives which can compensate for each other. In addition, the data types are restricted to continuous or ordinal data in this study. First, the following preprocessing should be performed.

## 3.1. Data preprocessing

(i) Data transformation. All ordinal data has to be transformed into numerical data in advance. There are several methods to deal with such transformation, such as monotonic transformation [15]. Since data transformation is not addressed by this study, it is assumed ordinal data can be mapped directly into numerical data by the DM, for simplicity (This transformation has not to be linear)

(ii) All criterion values, cost and benefit, are transformed to a scale of 1 to 10 based on min–max normalization.

(iii) Criteria values representing costs, which the DM prefers to be as small as possible, are transformed by subtracting from 11.

The symbols $c _ { i , k }$ and $C _ { i , k }$ are used for the kth criterion value of alternative $A _ { i }$ before and after preprocessing to distinguish between the raw and preprocessed criterion value. Denote $\underline { { C _ { k } } }$ and $\overline { { C _ { k } } }$ as the lower and upper bounds of preprocessed criterion value $C _ { k } ,$ where $C _ { k } = 1$ and $\overline { { C _ { k } } } = 1 0$ . The preprocessed consequence <sup>¼ ¼</sup>table of Example 1 is listed in Table 3. Take a benefit criterion value $C _ { 1 , 1 }$ and a cost criterion value $C _ { 1 , 5 }$ as examples, $C _ { 1 , 1 } = 9 ^ { * } \Big ( c _ { 1 , 1 } - \underline { { c } } _ { 1 } \Big ) / \Big ( \overline { { c _ { 1 } } } - \underline { { c } } _ { 1 } \Big ) + ~ 1 =$ $9 ^ { * } ( 8 0 0 - 5 0 0 ) / ( 1 2 0 0 - 5 0 0 ) + 1 = 4 . 8 6$ <sup>-</sup>and $C _ { 1 , 5 } =$ $1 1 - \left\{ 9 ^ { * } \Big ( c _ { 1 , 5 } - \underline { { c } } _ { 5 } \Big ) / \left( \overline { { c } } _ { 5 } - \underline { { c } } _ { 5 } \right) + 1 \right\} = 3 . 7 0 .$

In order to rank alternatives, one kind of score function has to be chosen before developing the ranking model. There are two main types of score functions: additive and multiplicative score functions. Instead of using an additive function, the score function of $A _ { i }$ is assumed to be in a multiplicative, nonlinear Cobb-Douglas [6] form with constant return to scale in this study because it is a well established and commonly used form, and also a kind of power function. Based on the concept of Brugha [4,5] and Barzilai [1,2], relative measured weights and scores should be synthesized using a power function. In addition, a multiplicative score function is good at reflecting a reasonable marginal rate of substitution. Denote $w _ { k }$ as the weight of criterion k. In order to reduce the complexity of the score function, all weights are assumed to be positive.

The preprocessed consequence table of Example 1

<table><tr><td colspan="2">Alternative Criteria</td><td> ${\mathrm{A}}_{1}$ </td><td> ${\mathrm{A}}_{2}$ </td><td> ${\mathrm{A}}_{3}$ </td><td> ${\mathrm{A}}_{4}$ </td><td> ${\mathrm{A}}_{5}$ </td></tr><tr><td> ${\mathrm{c}}_{1}$ </td><td>Office size (Square feet)</td><td>4.86</td><td>3.57</td><td>1.00</td><td>6.79</td><td>3.57</td></tr><tr><td> ${\mathrm{c}}_{2}$ </td><td>Customer access (%)</td><td>5.5</td><td>8.28.65</td><td>7.38.02</td><td>8.65</td><td>7.75</td></tr><tr><td> ${\mathrm{c}}_{3}$ </td><td>Office services</td><td>10</td><td>4</td><td>1</td><td>10</td><td>1</td></tr><tr><td> ${\mathrm{c}}_{4}$ </td><td>Commute (mins)</td><td>3.256.25</td><td>6.25</td><td>7.6.25</td><td>6.25</td><td>5.5</td></tr><tr><td> ${\mathrm{c}}_{5}$ </td><td>Monthly cost ($)</td><td>3.7 1</td><td>6.45.6</td><td>10</td><td>2.8</td><td>5.5</td></tr></table>

The score function of $A _ { i }$ is expressed below

$$
S _ {i} (\mathbf {w}) = w _ {0} C _ {i, 1} ^ {w _ {1}} C _ {i, 2} ^ {w _ {2}} \dots C _ {i, m} ^ {w _ {m}},\tag{1}
$$

where $w _ { 0 } , w _ { 1 } , . . . , w _ { m } { \geq } 0$ and $\sum _ { k = 1 } ^ { m } \ w _ { k } = 1$

<sup>¼</sup>It is assumed that the values of the weights $w _ { k }$ are implicitly in the DM's mind, but he can express them by even swaps.

For the purpose of comparison, two reference alternatives are defined: an ideal alternative $A * * = A * * ( \overline { { C } } _ { 1 }$ $\overline { { C _ { 2 } } } , \ldots , \overline { { C _ { m } } } )$ and a worst alternative $A _ { * } = A _ { * } ( C _ { 1 } , C _ { 2 }$ $\cdots , C _ { m } )$ <sup>Þ ¼ ð</sup>. Both alternatives may not be included in the <sup>Þ</sup>original alternative set A. Let the score of $\cdot _ { A * * }$ be 10. Then, $w _ { 0 } { = } 1$ and $S _ { * } { = } 1$

In order to distinguish between alternatives, the weighted difference $\delta _ { i , j } ( \mathbf { w } )$ between alternative $A _ { i }$ and $A _ { j }$ is defined as

$$
\delta_ {i, j} (\mathbf {w}) = \left[ \frac {\operatorname{Max} \left(C _ {i , 1} , C _ {j , 1}\right)}{\operatorname{Min} \left(C _ {i , 1} , C _ {j , 1}\right)} \right] ^ {w _ {1}} \times \dots \times \left[ \frac {\operatorname{Max} \left(C _ {i , m} , C _ {j , m}\right)}{\operatorname{Min} \left(C _ {i , m} , C _ {j , m}\right)} \right] ^ {w _ {m}},\tag{2}
$$

where $w _ { 0 } , w _ { 1 } , . . . , w _ { m } { \geq } 0$ and $\sum _ { t . \phantom { = } 1 } ^ { m } \ w _ { k } = 1$ . Since $\mathrm { M a x } ( C _ { i , k } ,$ $C _ { j , k } ) \leq 1 0$ and Min $( C _ { i , k } , C _ { j , k } ) \overset { n - 1 } { = } 1$ for all k, $1 \leq \delta _ { i , j } ( \mathbf { w } ) \leq 1 0$ and $\delta _ { i , j } \left( \mathbf { w } \right) { = } \delta _ { j , i } ( \mathbf { w } )$

The idea of Expression (2) comes from the definition of an additive dissimilarity function, which is commonly defined as $\delta _ { i , j } ( \mathbf { w } ) = \sum _ { \iota , \iota } ^ { m } \ w _ { k } | C _ { i , k } - C _ { j , k } | = \sum _ { \iota , \iota } ^ { m } \ ( w _ { k } ( \mathbf { M a x }$ $\left( C _ { i , k } , C _ { j , k } \right) - \mathrm { M i n } \big ( C _ { i , k } ^ { k = 1 } , C _ { j , k } \big ) \big )$ with $\sum _ { k = 1 } w _ { k } = \bar { 1 } _ { : }$ , where $C _ { i , k }$ and $C _ { j , k }$ ¼are the kth normalized criterion values of alternative i and $j .$ The multiplicative dissimilarity function can then be constructed in a similar way as $\delta _ { i , j } ( \mathbf { w } ) =$ $\Pi _ { k = 1 } ^ { m } \left( \frac { \mathrm { M a x } \left( C _ { i , k } , C _ { j , k } \right) } { \mathrm { M i n } \left( C _ { i , k } , C _ { j , k } \right) } \right)$ w with $\sum _ { k = 1 } ^ { m } \ w _ { k } = 1$ . Because all cri-<sup>ð Þ</sup> ¼teria values in multiplicative form have been normalized to a [1,10] scale during the preprocessing stage, $1 \leq \delta _ { i , j } \ ( \mathbf { w } ) \leq 1 0$ and $\delta _ { i , j } \ ( \mathbf { w } ) { = } \delta _ { j , i } \ ( \mathbf { w } )$ . For instance, the scores of alternatives with consequences $( 1 , 1 )$ and $( 2 , 2 )$ are 1 and $^ { 2 , }$ respectively. Based on the multiplicative concept, the score of the later alternative is 2 times that of the former one. From Expression (2), the dissimilarity between these two alternatives is 2. Comparing with the alternatives with consequences (9, 9) and (10, 10), the scores of these two alternatives are 9 and 10, respectively, where the second score is 1.1 times of the first one. From Expression (2), the dissimilarity between these two alternatives is 1.1.

Here $A _ { i }$ and $A _ { j }$ are mapped into the two points $P _ { i }$ and $P _ { j }$ (denoted as the mapping points) on the surface of a hemisphere, such that the arc length connecting these two points expresses dissimilarity between $A _ { i }$ and $A _ { j } .$

Since it is easier to compute the Euclidean distance than to compute the arc length, it is essential to have the following proposition:

Proposition 1. Let $P _ { i }$ and $P _ { j }$ be two points on the surface of a sphere centered at point $O ( 0 , 0 , 0 )$ with radius r. Denote $\theta _ { i , j }$ as the angle $P _ { i } O P _ { j } ,$ and denote $\widehat { P _ { i } P _ { j } }$ as the shortest arc length along the great circle that passes through the two points. It is true that arc length $\acute { P } _ { i } \dot { P } _ { j }$ is monotonically related to the Euclidean distance $\overline { { P _ { i } P _ { j } } }$

The proof of this proposition is given in Appendix B. Referring to the non-metric multidimensional scaling method [9], it is more convenient to use the Euclidean distance $\overline { { P _ { i } P _ { j } } }$ rather than the arc length to approximate dissimilarities. Both approximation methods make very little difference to the resulting configuration [8]. Therefore, Euclidean distances are used in this paper for convenience.

Based on $A _ { * * } , A _ { * }$ and Proposition 1, a hemisphere is generated. It is centered at $( 0 , 0 , 0 )$ with radius $1 0 . \ : P _ { * * }$ ⁎ (the mapping point of $\dag _ { A _ { * * } } )$ is located at the north pole of this hemisphere with $( x _ { * * } , y _ { * * } , z _ { * * } ) { = } ( 0 , 1 0 , 0 )$ ), while $P _ { * }$ (the mapping point of $A _ { * } )$ is located at the equator with $x _ { * } , y _ { * } , z _ { * } { = } ( x _ { * } , 0 , z _ { * } )$ where $x _ { * } ^ { 2 } + z _ { * } ^ { 2 } = 1 0 ^ { 2 }$ , as depicted in Fig. 2. It is clear that the distance between $P _ { * * } ( 0 , 1 0 , 0 )$ and $O ( 0 , 0 , 0 )$ is 10, and the distance between $P _ { * * } ( 0 , 1 0 ,$ 0) and $P _ { * } ( x _ { * } , \ 0 , \ z _ { * } )$ is $1 0 \sqrt { 2 }$ . The Euclidean distance between $P _ { i }$ and $P _ { j } ,$ denoted as $d _ { i , j } ,$ is used to represent the logarithm of dissimilarity between $A _ { i }$ and $A _ { j }$ (i.e. $\ln ( \delta _ { i , j } ) )$ : the larger the difference, the longer the distance. Furthermore, the alternative with a higher score is designed to be closer to the north pole so that alternatives are located on the concentric circles in the order of score from top view.

The relationship between $S _ { i }$ and $d _ { i 9 * * }$ is defined as

$$
d _ {i, * *} = 1 0 \sqrt {2} \left(1 - \frac {\ln (S _ {i})}{\ln (1 0)}\right),\tag{3}
$$

where if $S _ { i } { = } 1$ then $d _ { i , \ast \ast } = 1 0 \sqrt { 2 }$ and if $S _ { i } { = } 1 0$ then $d _ { i , * * } = 0$

![](/api/attachments/2BQ64NRW/fulltext/images/e736de12eec21f4d076d9b87c8af86d260bb063ac7f9219afbaa3de6b754130a.jpg)  
Fig. 2. Ideal point $P _ { * * }$ and the worst point $P _ { * * }$

To map each $A _ { i }$ to a point $P _ { i } ( x _ { i } , y _ { i } , z _ { i } )$ on the surface of a hemisphere, the following conditions should be satisfied:

$$
\text {(i)} d _ {i, * *} = 1 0 \sqrt {2} \left(1 - \frac {\ln (S _ {i})}{\ln (1 0)}\right),
$$

ii $x _ { i } ^ { 2 } + y _ { i } ^ { 2 } + z _ { i } ^ { 2 } = 1 0 0 .$

iii $x _ { i } ^ { 2 } + \left( y _ { i } - 1 0 \right) ^ { 2 } + z _ { i } ^ { 2 } = d _ { i , * * } ^ { 2 }$

The following proposition is deduced.

Proposition 2. The relationship between $y _ { i }$ and $S _ { i }$ is expressed as

$$
y _ {i} = 1 0 - 1 0 \left(1 - \frac {\ln (S _ {i})}{\ln (1 0)}\right) ^ {2}.\tag{4}
$$

The proof of Proposition 2 is given in Appendix C. By mapping all $A _ { i }$ into the points on a sphere, relationships among alternatives can be examined. These relationships are discussed below.

Consider the following propositions:

Proposition 3. On a hemisphere, suppose there are two alternatives $A _ { i }$ and $A _ { j }$ with $S _ { i } { > } S _ { i } . P _ { * * } , P _ { i }$ and $P _ { j }$ are on the same longitude if and only $i f l n ( \delta _ { i , j } ) = l n ( \delta _ { j , * * } ) -$ $l n ( \delta _ { i , * * } )$

The proof of this proposition is given in Appendix D.

Given an alternative set $\mathbf { A } { = } ( A _ { 1 } , ~ A _ { 2 } { , . . . , ~ A _ { n } } )$ and a weight vector w, a corresponding Decision Ball of A and w is denoted as $\mathbf { D B } ( \mathbf { w } , \mathbf { I } ) { = } \{ ( x _ { i } , y _ { i } , z _ { i } ) | i { \in } \mathbf { I } { = } \{ 1 , 2 , . . . ,$ $n \}$ , where $( x _ { i } , y _ { i } , z _ { i } )$ is the coordinate of alternative $A _ { i }$ on the Decision Ball and $y _ { i } \geq 0$

Proposition 4. Consider a DB(w, I) with two alternatives $A _ { i }$ and $A _ { j }$ only, $i . e . , { \bf I } = \{ i , j \} . \ { \cal I } f A _ { i } \succ A _ { j } ,$ then $P _ { i }$ and $P _ { j }$ are on the same longitude.

The proof of this proposition is given in Appendix E. Proposition 5. For a DB(w, $\mathbf { I } ) f o r \mathbf { I } = \{ i , j \} . I f S _ { i } ( \mathbf { w } ) > S _ { j } ( \mathbf { w } )$ and $P _ { i }$ and $P _ { j }$ are on the same longitude, then $A _ { i } { \succ } A _ { j }$

The proof of this proposition is given in Appendix F. The following theorem is then deduced:

Theorem 1. For a DB(w, I), ${ \bf I } = \{ i , j \} ,$ , given $A _ { i }$ and $A _ { j }$ where ${ { S } _ { i } } \left( \mathbf { w } \right) { > } { { S } _ { i } } \left( \mathbf { w } \right)$ , if and only if $\gamma _ { A _ { i } \succ A _ { j } } ,$ then $P _ { i }$ and $\dot { P _ { j } }$ are on the same longitude of the ball connecting P , $P _ { i }$ and $P _ { j } .$

Denote $\mathbf { D S } ( \mathfrak { p } ) { = } \{ A _ { i _ { 1 } } , ~ A _ { i _ { 2 } } { , \ldots } , ~ A _ { i _ { p } } \}$ as a dominant set composed of p alternatives with dominant relationships $A _ { i _ { 1 } } { \succ } A _ { i _ { 2 } } { \succ } \ldots { \succ } A _ { i _ { p } }$

Proposition 6. Consider a dominant set $\mathbf { D S } ( k ) = \{ A _ { i _ { 1 } } ,$ $A _ { i _ { 2 } } , . . . , A _ { i _ { k } } \} .$ . Let DB(w, I), $\mathbf { I } = \{ I , ~ 2 , ~ . . . , ~ k \}$ be the corresponding Decision Ball for the alternatives $A _ { I } , A _ { 2 } ,$ $\ldots , A _ { k }$ where $A _ { 1 } \succ A _ { 2 } \succ . . . \succ A _ { k } .$ Connecting the mapping points $P _ { * * , \ P _ { 1 } , \ P _ { 2 } , \ . . . , \ P _ { k } }$ forms a longitude on the surface of this Decision Ball. That implies $a x _ { i } + c z _ { i } = 0$ for $i = 1 , 2 , . . . , k ,$ where a and c are constants.

The proof of Proposition 6 is given in Appendix G. A Decision Ball $\mathbf { D B } ( \mathbf { w } , \mathbf { I } ) { = } \{ ( x _ { i } , y _ { i } , z _ { i } ) | i { \in } \mathbf { I } { = } \{ 1 , 2 , { \ldots } \}$ $n \}$ is obtained by solving the model below.

Model 1. (A Decision Ball model with MDS concept)

$$
\underset {\{x _ {i}, y _ {i}, z _ {i} \}} {\text { Min }} \quad \text { Obj } = \sum_ {i = 1} ^ {n} \sum_ {j > i} ^ {n} \left(\hat {d} _ {i, j} - d _ {i, j}\right) ^ {2}
$$

$$
\mathrm{s.t.} \hat {d} _ {i, j} \leq \hat {d} _ {p, q} - \varepsilon , \forall \delta_ {i, j} <   \delta_ {p, q}, 1 \leq i, j, p, q \leq n,\tag{5}
$$

$$
d _ {i, j} ^ {2} = \left(x _ {i} - x _ {j}\right) ^ {2} + \left(y _ {i} - y _ {j}\right) ^ {2} + \left(z _ {i} - z _ {j}\right) ^ {2}, \forall i, j,\tag{6}
$$

$$
y _ {i} = 1 0 - 1 0 \left(1 - \frac {\ln (S _ {i})}{\ln (1 0)}\right) ^ {2}, \forall i,\tag{7}
$$

$$
x _ {i} ^ {2} + y _ {i} ^ {2} + z _ {i} ^ {2} = 1 0 0, \forall i,
$$

$$
x _ {i} z _ {j} = x _ {j} z _ {i}, \forall A _ {i} \succ A j,\tag{8}
$$

9

$$
- 1 0 \leq x _ {i} \leq 1 0, 0 \leq y _ {i} \leq 1 0, - 1 0 \leq z _ {i} \leq 1 0, \forall i,\tag{10}
$$

ε is a tolerable error.

The objective of Model 1 is to minimize the sum of squared differences between $d _ { i , j }$ and $\hat { d } _ { i , j }$ . Eq. (5) is the monotonic transformation from l $\mathbb { \Gamma } ( \delta _ { i , j } )$ to $\hat { d } _ { i , j }$ based on the concept of non-metric MDS [9,18]: the higher the dissimilarity, the longer the distance. Because $1 \leq \delta _ { i , j } \leq$ 10 for all $i , j , \delta _ { i , j } { < } \delta _ { p , q }$ implies ln $( \delta _ { i , j } ) < \ln ( \delta _ { p , q } )$ for all $i ,$ $j , p , q$ . That is, if $\delta _ { i , j } { < } \delta _ { p , q } , \ \hat { d } _ { i , j }$ is smaller than $\hat { d } _ { p , q } ;$ therefore, the distance between $A _ { i }$ and $A _ { j }$ is shorter than the distance between $A _ { p }$ and $A _ { q } .$ . The ε in Eq. (5) is a computational precision which can be normally set as $1 0 ^ { - \bar { 6 } }$ . Eq. (7) is from Proposition 2. All alternatives are graphed on the surface of the ball described by Eq. (8). $\operatorname { E q } .$ . (9) is obtained from Proposition 6. In Eq. (10), all alternatives are located on the upper hemisphere.

The number of variables used in Model 1 is $n ( n - 1 ) +$ $3 n ,$ where 3n is the number of decision variables used for $x _ { i } , y _ { i } , z _ { i }$ and $n ( n - 1 )$ is the number of variables used for $d _ { i , j }$ and $\hat { d } _ { i , j }$ . The maximal number of constraints used in Model 1 is $n ( n - 1 ) + 6 n$ in which Eqs. (5) and (6) account for $n ( n - 1 )$ constraints and Eqs. (7)–(10) contain no more than 6n constraints. Model 1 is a non-linear model, which can be solved by some commercialized optimization software, such as Global Solver of Lingo 9.0 [20], to obtain an optimum solution.

Let $A _ { i } ^ { \prime }$ be the alternative converted from $A _ { i }$ by the DM through making even swaps. $A _ { i }$ and $A _ { i } ^ { \prime }$ are called concurrent alternatives. $P _ { i }$ and $P _ { i } ^ { \prime } { \mathrm { . } }$ , which are mapping points of $A _ { i }$ and $A _ { i } ^ { \prime } ,$ are called concurrent points.

Remark 1. Given two alternatives $A _ { i }$ and $A _ { j } ,$ suppose the DM can stably make even swaps based on the score function in $( 1 ) ,$ , then $P _ { j }$ can be converted into another concurrent point $P _ { j } ^ { \prime }$ such that $P _ { * , } \ P _ { i }$ and $P _ { j } ^ { \prime }$ are on the same longitude.

Fig. 3 is used to interpret Remark 1. Here $S _ { i } { \geq } S _ { j }$ but $A _ { i }$ does not dominate $A _ { j } .$ Via Even Swap process, $A _ { j }$ is converted to $A _ { j } ^ { \prime }$ where $A _ { i } \succ A _ { j } ^ { \prime }$ . From Theorem 1, $P _ { j }$ is moved to a concurrent point $P _ { j } ^ { \prime }$ where $P _ { * , } P _ { i }$ and $P _ { j } ^ { \prime }$ are on the same longitude. $A _ { i }$ is said to be consistently even swapped into $\begin{array} { r } { A _ { i } ^ { \prime } \operatorname { i f } \frac { | S _ { i } - S _ { i } ^ { \prime } | } { S _ { i } } \leq \varepsilon , } \end{array}$ , where ε is a tolerable error.

Theorem 2. Given $A _ { i }$ with its concurrent alternative $A _ { i } ^ { \prime } ,$ and $P _ { i }$ with its concurrent point P′, $A _ { i }$ is consistently even swapped into $A _ { i } ^ { \prime }$ if and only $i f P _ { i }$ and $P _ { i } ^ { \prime }$ are on the same latitude.

The proof of this theorem is given in Appendix H.

Current Even Swap methods lack a mechanism to advise the DM when there are serious inconsistencies among even swaps. For instance, as illustrated in Table 2(a) and (d), based on the score function in Eq. (1), the weights of criteria can be calculated as follows (all criterion values have been transformed in the data preprocessing stage as listed in Table 3):

(i) For $A _ { 1 }$ in Table 2(a) (mapped to $A _ { 1 }$ column of Table $\begin{array} { r } { 3 ) , \frac { 3 . 2 5 ^ { w _ { 4 } } \times 3 . 7 ^ { w _ { 5 } } } { 6 . 2 5 ^ { w _ { 4 } } \times 1 ^ { w _ { 5 } } } = 1 } \end{array}$ ; then $\begin{array} { r } { \frac { w _ { 4 } } { w _ { 5 } } = 2 } \end{array}$

(ii) For $A _ { 3 }$ <sup> ¼</sup> in Table 2(a) (mapped to $A _ { 3 }$ column of Table 3), $\begin{array} { r } { \frac { 7 . 3 ^ { w _ { 2 } } \times 7 ^ { w _ { 4 } } } { 8 . 0 2 ^ { w _ { 2 } } \times 6 . 2 5 ^ { w _ { 4 } } } = 1 } \end{array}$ ; then $\frac { w _ { 2 } } { w _ { 4 } } = 1 . 2$

(iii) For $A _ { 2 }$ <sup> ¼</sup> in Table 2(d) (mapped to $A _ { 2 }$ column of Table 3), $\begin{array} { r } { \frac { 8 . 2 ^ { w _ { 2 } } \times 6 . 4 ^ { w _ { 5 } } } { 8 . 6 5 ^ { w _ { 2 } } \times 3 . 6 ^ { w _ { 5 } } } = \dot { 1 } } \end{array}$ ; then $\begin{array} { r } { \frac { w _ { 2 } } { w _ { 5 } } = 1 0 . 7 6 } \end{array}$

![](/api/attachments/2BQ64NRW/fulltext/images/0d16e33252c5b5d2814f560e8babab23e15e246e73988b9781e45382fd027866.jpg)  
Fig. 3. Moving trajectory of concurrent points.

From (i) and (ii), $\begin{array} { r } { \frac { w _ { 2 } } { w _ { 5 } } = 2 . 4 , } \end{array}$ which is quiet different <sup>¼</sup>from the result in (iii). These inconsistencies among even swaps, based on the same Cobb–Douglas score function, are not checked by the conventional Even Swap methods.

This study proposes Theorem 2 to check the consistency of Even Swap process made by the DM. For instance, as illustrated in Fig. 3, $P _ { j }$ is consistently even swapped into $P _ { j } ^ { \prime }$ , however, $P _ { j } ^ { \prime \prime }$ is not even swapped from $P _ { j }$ consistently. The more inconsistent a swap the DM has made, the bigger differences in score before and after even swap. That is, the difference between coordinate y<sub>j</sub> and y<sub>j</sub>′ is bigger.

Both Theorem 1 and Theorem 2 are utilized in this study to develop an algorithm to visualize the Even Swap process via a Decision Ball. By examining the moving trajectories of related points on a Decision Ball, the DM can rank the alternatives more consistently.

## 4. Decision process

This section uses the previous example (Example 1) to illustrate the process of ranking the alternatives using the proposed method. First, the DM sets initial weights for each criterion. If the DM cannot specify initial weights, equal weights are assumed at the beginning. These weights are iteratively adjusted when new preference information from the DM is acquired. The DM is assisted by a decision support system (DSS) composed of data, models and graphic interfaces. The process is summarized as follows:

Step 1 (Initialization). The DSS asks the DM to input a consequence table, to select criteria with cost features, to quantify the non-numerical criteria, and to specify the initial weights $\mathbf { w } ( J )$ for $J { = } 0 , J$ is used to record the number of iterations, and $J { = } 0$ indicates initial settings. A dominant set is initialized as $ { \mathbf { D } } \mathbf { S } ( J ) { = } \Phi$ , for $J { = } 0$

Step 2 (Displaying an initial Decision Ball). Set $J { = } 0$ . Based on $\mathbf { w } ( J ) ,$ , the DSS computes $S _ { i } ( \mathbf { w } )$ and $\delta _ { i , j } ( \mathbf { w } )$ in Eqs. (1) and (2), respectively. A Decision Ball $ { \mathbf { D } }  { \mathbf { B } } (  { \mathbf { w } } ,  { \mathbf { I } } )$ is displayed to the DM after solving Model 1.

Step 3 (Choosing the next alternative for even swap). The alternative $A _ { i } \not \in { \bf D } { \bf S } ( J )$ with the highest score is chosen as the next swap alternative by the DSS. The process stops if all alternatives are in $\mathbf { D } \mathbf { S } ( J )$ or the DM ceases to make further even swaps.

Step 4 (Making even swaps). The DM makes even swaps between $A _ { i }$ and alternatives in DS(J). $A _ { i }$ is changed to a concurrent alternative $A _ { i } ^ { \prime }$ such that $A _ { i } ^ { \prime }$ dominates or is dominated by an alternative in DS(J).

Step 5 (Updating weights and displaying a resulting sphere). For each even swap, the system computes the related weights by solving the following linear program:

Model 2. (Updating weights)

$$
\begin{array}{l} \underset {\left\{w _ {p}, w _ {q} \right\}} {\text { Min }} \quad \alpha \\ \text { s.t. } \quad | w _ {p} (\ln (C _ {i, p}) - \ln (C _ {i, p} ^ {\prime})) + w _ {q} (\ln (C _ {i, q}) - \ln (C _ {i, q} ^ {\prime})) | \leq \alpha , \text { for   an   even   swap } (C _ {p}, C _ {q}) \text { in } A _ {i}, \\ \sum_ {k = 1} ^ {m} w _ {k} = 1, \\ w _ {k} \geq 0, \forall k. \end{array}\tag{11}
$$

The weights of unadjusted criteria are kept the same as those in the previous step.

Variables $C _ { i , k }$ and $C _ { i , k } ^ { \prime }$ are the value of criterion k of $A _ { i }$ before and after the even swap respectively. The resulting sphere based on the new weights is displayed. Then J is incremented, i.e. $J { = } J { + } 1$

Step 6 (Updating the dominant set). $A _ { i }$ is added into $\mathbf { D } \mathbf { S } ( J )$ . Reiterate Steps 3–6.

Take Example 1 to illustrate the whole decision process. It is important to note that the decision maker still deals with raw criterion values. After the decision maker inputs these values, the system automatically transforms the raw criterion values into preprocessed criterion values. In addition, the even swaps made here are different from those made in the original example described in Section 2 because all dominated alternatives are eliminated in the original example; however, the proposed approach tries to rank all alternatives so that all alternatives have to be kept and compared.

Iteration 1. At Step 1, the DM inputs his consequence table, upper and lower bound values of each criterion (Table 1), where $c _ { 4 } , c _ { 5 }$ are criteria with a cost feature. Suppose the DM inputs the initial weights $\mathbf { w } ( 1 ) = ( w _ { 1 } , w _ { 2 } , w _ { 3 } , w _ { 4 } , w _ { 5 } ) = ( 0 . 2$ $0 . 2 , 0 . 2 , 0 . 2 , 0 . 2 )$ . The DSS asks the DM to answer some questions.

bDSSN Consider the qualitative criterion $c _ { 3 }$ . Please quantify the values of service level $\mathbf { A } ,$ B and C.

bDMN 4, 2, 1. (The preprocessed values are 10, 4, 1, respectively, using min–max normalization).

![](/api/attachments/2BQ64NRW/fulltext/images/4cf325cd920225be2a29f4af9a0a91c60d4f29aeddefc8c2a58e105a55b9007f.jpg)  
Fig. 4. Iteration 1: initial sphere.

(a)

<table><tr><td colspan="2">Alternative Criteria</td><td>A4</td><td>A2</td><td>A2</td></tr><tr><td> $c_1$ </td><td>Office Size (Square Feet)</td><td>950</td><td>700</td><td>850</td></tr><tr><td> $c_2$ </td><td>Customer Access (%)</td><td>85</td><td>80</td><td>80</td></tr><tr><td> $c_3$ </td><td>Office Services</td><td>A</td><td>B</td><td>B</td></tr><tr><td> $c_4$ </td><td>Commute (Mins)</td><td>25</td><td>25</td><td>25</td></tr><tr><td> $c_5$ </td><td>Monthly Cost ($)</td><td>1900</td><td>1700</td><td>1900</td></tr></table>

(b)  
![](/api/attachments/2BQ64NRW/fulltext/images/71987c6f6c291588bab6ea6a2d5f4c41138a02f71ac8e1426ab5da492b635fd5.jpg)  
Fig. 5. Iteration 2 (a) Adjusting $A _ { 2 }$ with respecting to $A _ { 4 }$ (b) Resulting sphere.

The transformed consequence table after preprocessing is listed in Table 3. At Step 2, based on the initial weights, the dissimilarities between alternatives and scores of alternatives are calculated. An initial sphere (Fig. 4) is displayed to the DM. Here $A _ { 4 }$ has the highest score. ${ \bf D S } ( 1 ) = \{ A _ { 4 } \}$

Iteration $2 . A _ { 2 }$ is chosen as the swapped alternative with $A _ { 4 }$ since $A _ { 2 }$ is the next best alternative.

bDSSN Examining the table values in Fig. 5(a). Choose a target criterion of $A _ { 2 }$ from $\{ c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 5 } \}$ , and adjust its value. The adjusted value should be the same as the target criterion of $A _ { 4 }$

$< { \bf D } { \bf M } > c _ { 5 }$ and 1900.

In the same way, the DM makes a 150 increase in $c _ { 1 }$ to compensate for the increase of $c _ { 5 }$ from 1700 to $1 9 0 0 ( A _ { 2 }$ is changed to a concurrent point $A _ { 2 } ^ { \prime } .$ , and $A _ { 4 } \succ A _ { 2 } ^ { \prime } )$ . Model 2 is then formulated as the following program:

$$
\begin{array}{l} \underset {\{w _ {1}, w _ {5} \}} {\text { Min }} \quad \alpha \\ \text { s.t. } \quad | w _ {1} (\ln (3. 5 7) - \ln (5. 5)) + w _ {5} (\ln (6. 4) - \ln (2. 8)) | \leq \alpha , \\ \qquad \qquad w _ {2} = w _ {3} = w _ {4} = 0. 2, \sum_ {k = 1} ^ {5} w _ {k} = 1,   w _ {k} \geq 0,   \forall k = 1, \ldots , 5. \end{array}
$$

Solving the above program yields $\mathbf { w } ( 2 ) { = } ( 0 . 2 6 , 0 . 2 , 0 . 2 , 0 . 2 , 0 . 1 4 )$ . The resulting sphere is shown in Fig. 5(b). At Step 6, the DSS sets ${ \bf D S } ( 2 ) = \{ A _ { 4 } , A _ { 2 } ^ { \prime } \}$

(a)

<table><tr><td colspan="2">Alternative Criteria</td><td> ${\mathrm{A}}_{2}^{\prime }$ </td><td> ${\mathrm{A}}_{1}$ </td><td> ${\mathrm{A}}_{1}^{\prime }$ </td></tr><tr><td> ${c}_{1}$ </td><td>Office Size (Square Feet)</td><td>850</td><td>800</td><td>850</td></tr><tr><td> ${c}_{2}$ </td><td>Customer Access (%)</td><td>80</td><td>50</td><td>75</td></tr><tr><td> ${c}_{3}$ </td><td>Office Services</td><td>B</td><td>A</td><td>B</td></tr><tr><td> ${c}_{4}$ </td><td>Commute (Mins)</td><td>25</td><td>45</td><td>45</td></tr><tr><td> ${c}_{5}$ </td><td>Monthly Cost ($)</td><td>1900</td><td>1850</td><td>1900</td></tr></table>

![](/api/attachments/2BQ64NRW/fulltext/images/766750c7107fd8934b7de272fd9cd813cd9df2de020834c3f8adaf7ce8a186c6.jpg)  
w = (0.28, 0.29, 0.11, 0.2, 0.12)  
Fig. 6. Iteration 3 (a) Adjusting $A _ { 1 }$ with respecting to A (b) Resulting sphere.

<table><tr><td colspan="2">Alternative Criteria</td><td> $A_1$ </td><td>A5</td><td> $A_5$ </td></tr><tr><td> $c_1$ </td><td>Office Size (Square Feet)</td><td>850</td><td>700→</td><td>800</td></tr><tr><td> $c_2$ </td><td>Customer Access (%)</td><td>75</td><td>75</td><td>75</td></tr><tr><td> $c_3$ </td><td>Office Services</td><td>B</td><td>C→</td><td>B</td></tr><tr><td> $c_4$ </td><td>Commute (Mins)</td><td>45</td><td>30→</td><td>45</td></tr><tr><td> $c_5$ </td><td>Monthly Cost ($)</td><td>1900</td><td>1750→</td><td>1950</td></tr></table>

![](/api/attachments/2BQ64NRW/fulltext/images/e3e7e3c465eb8c4c7c317f0401cbc8f424859475f68d3c0dc157c6bd71c08efe.jpg)  
Fig. 7. Iteration 4 (a) Adjusting $A _ { 5 }$ with respecting to $A _ { 1 }$ (b) Resulting sphere.

Iteration 3. Alternative $A _ { 1 }$ is chosen as the swap alternative. Suppose the DM equates a decrease in $c _ { 3 }$ from A to B with a 25 increase in $c _ { 2 } ,$ , and equates an increase in $c _ { 5 }$ from 1850 to 1900 with a 50 increase in $c _ { 1 }$ . The corresponding changes are depicted in Fig. 6(a) and (b). ${ \bf D S } ( 3 ) = \{ A _ { 4 } , A _ { 2 } ^ { \prime } , A _ { 1 } ^ { \prime } \}$ . The top three options have been found. The DM can then choose to terminate or continue to the next iteration.

Iteration $4 . A _ { 5 }$ is chosen as a swap alternative. Suppose the DM equates an increase in $c _ { 3 }$ from C to B with a 200 increase in $c _ { 5 } ,$ and equates an increase in $c _ { 4 }$ from 30 to 45 with a 100 increase in $c _ { 1 } ,$ as listed in Fig. 7(a). Fig. 7(b) shows the resulting sphere.

Iteration 5. Suppose the DM wants to continue the process. $A _ { 3 }$ is chosen as a swap alternative. Suppose the consequence table and corresponding Decision Ball after even swaps are as shown in Fig. 8(a) and (b), where $\mathrm { { \bf D S } } ( 5 ) = \{ A _ { 4 } , A _ { 2 } ^ { \prime } , A _ { 1 } ^ { \prime } , A _ { 5 } ^ { \prime } , A _ { 3 } ^ { \prime } \}$ . The process is then terminated.

The consistencies among even swaps can be checked by the moving trajectory of concurrent points. The even swap, which causes the largest latitudinal shift of a given alternative, is the most inconsistent. For instance, the moving trajectory of $\dot { \boldsymbol { A } } _ { 3 }$ is shown in Fig. 9, where $3 ^ { J }$ stands for concurrent point $P _ { 3 }$ after the Jth iteration. The most inconsistent even swaps the DM has made are at Iteration 2 and 5 because $3 ^ { 2 }$ and $3 ^ { 5 }$ are furthest away from the latitude formed by all $3 ^ { J }$ based on Theorem 2. Here the scores of points $3 ^ { 1 } 3 ^ { 2 } , 3 ^ { 3 } , 3 ^ { 4 }$ and $3 ^ { 5 }$ are 3.48, 3.01, 3.49, 3.40 and 4.00, respectively. The DM can revise these inconsistencies by re-iterating the even swap process at Iteration 2 or 5. For instance, if the DM chooses to re-iterate the even swap process at Iteration 2 (as listed in Fig. 5a) and equates an increase in $c _ { 5 }$ from

(a)

<table><tr><td colspan="2">Alternative Criteria</td><td> ${\mathrm{A}}_{5}^{\prime }$ </td><td> ${\mathrm{A}}_{3}$ </td><td> ${\mathrm{A}}_{3}^{\prime }$ </td></tr><tr><td> ${c}_{1}$ </td><td>Office Size (Square Feet)</td><td>800</td><td>500 ...</td><td>750</td></tr><tr><td> ${c}_{2}$ </td><td>Customer Access (%)</td><td>75</td><td>70</td><td>70</td></tr><tr><td> ${c}_{3}$ </td><td>Office Services</td><td>B</td><td>C ...</td><td>B</td></tr><tr><td> ${c}_{4}$ </td><td>Commute (Mins)</td><td>45</td><td>20 ...</td><td>45</td></tr><tr><td> ${c}_{5}$ </td><td>Monthly Cost ($)</td><td>1950</td><td>1500 ...</td><td>1950</td></tr></table>

(b)  
![](/api/attachments/2BQ64NRW/fulltext/images/7f6c94d97d9e0a372f32c0925071c8799f95601750c9a7da87ccecc192e7c3ec.jpg)  
w = (0.23, 0.29, 0.10, 0.18, 0.20)  
Fig. 8. Iteration 5 (a) Adjusting $A _ { 3 }$ with respecting to $A _ { 5 }$ (b) Resulting sphere.

![](/api/attachments/2BQ64NRW/fulltext/images/5b9d560371ce4e9a2dbe9e424ac075512c899e6c506763083bf0dee0300c77e2.jpg)  
Fig. 9. The moving trajectories of $A _ { 3 }$ after even swaps.

1700 to 1900 for $A _ { 2 }$ with a 250 increase in $^ { c _ { 1 } , }$ , the score of $3 ^ { 2 }$ is changed from 3.01 to 3.25. It is worth noticing that, since the sphere can be rotated to present different views, the relative longitude positions of concurrent points might be different from those in Figs. 4–8. In addition, the position of the concurrent point in the first iteration can be ignored because the initial weights may be given arbitrarily.

This problem was solved by Global Solver of Lingo 9.0 [20] on a Pentium 4 personal computer. The running time was less than five seconds for each iteration.

## 5. Concluding remarks

The Even Swap is a rational and straightforward method which provides a mechanism for making trades so that a DM can make the best choice. Based on the concept of Even Swaps, this study proposes a graphic method to help the DM rank and visualize alternatives. Rather than revealing the best option only in a conventional Even Swap method, the proposed approach can fully rank all alternatives. In addition, the DM can find the similarities among alternatives, can iteratively adjust preferences, and see the corresponding changes on the Decision Ball.

The proposed approach meets most of the requirements of a useful decision model, known as decision calculus [21]. First, it is simple because it is easy for a DM to understand. Second, it is robust because the method is logically correct for finding a rational solution. Third, it is easy to control, adapt, and complete. Finally, since the DM can adjust inputs and visualize outputs via the Decision Balls, the proposed approach facilitates convenient communication between the DM and the DSS.

One restriction of this approach is the running time that may considerably increase when the number of alternatives becomes large because the time complexity of Model 1 is $n ^ { 2 }$ . In future study, how to linearize this non-linear model to deal with large size problems can be addressed. Nevertheless, because the Even Swap method is good for small size problems or the final stage of decisions, the proposed approach is especially help in the case of alternatives fewer than 10.

## Appendix A. A letter from Benjamin Franklin to Joseph Priestly

In the affair of so much importance to you, wherein you ask my advice, I cannot, for want of sufficient premises, advise you what to determine, but if you please I will tell you how. When those difficult cases occur, they are difficult, chiefly because while we have them under consideration, all the reasons pro and con are not present to the mind at the same time; but sometimes one set present themselves, and at other times another, the first being out of sight. Hence the various purposes or inclinations that alternatively prevail, and the uncertainty that perplexes us. To get over this, my way is to divide half a sheet of paper by a line into two columns; writing over the one Pro, and over the other Con. Then, during three or four days consideration, I put down under the different heads short hints of the different motives, that at different times occur to me, for or against the measure. When I have thus got them all together in one view, I endeavor to estimate their respective weights; and where I find two, one on each side, that seem equal, I strike them both out. If I find a reason pro equal to some two reasons con, I strike out the three. If I judge some two reasons con, equal to three reasons pro, I strike out the five; and thus proceeding I find at length where the balance lies; and if, after a day or two of further consideration, nothing new that is of importance occurs on either side, I come to a determination accordingly. And, though the weight of the reasons cannot be taken with the precision of algebraic quantities, yet when each is thus considered, separately and comparatively, and the whole lies before me, I think I can judge better, and am less liable to make a rash step, and in fact I have found great advantage from this kind of equation, and what might be called moral or prudential algebra. Wishing sincerely that you may determine for the best, I am ever, my dear friend, yours most affectionately. (London, Sept 19, l772)

From: “Letter to Joseph Priestly”, Benjamin Franklin Sampler [10].

## Appendix B

Proof of Proposition 1. $\begin{array} { r } { \overline { { P _ { i } P _ { j } } } = 2 r \sin \frac { \theta _ { i , j } } { 2 } , \widehat { P _ { i } P _ { j } } = r \theta _ { i , j } = } \end{array}$ $2 r \sin ^ { - 1 } \frac { \overline { { P _ { i } P _ { j } } } } { 2 r } .$ <sup>.</sup> Since $0 \leq \overline { { P _ { i } P _ { j } } } \leq 2 r _ { \mathrm { : } }$ , we have $\underline { { 0 \le \overline { { \mathit { P } _ { i } \mathit { P } _ { j } } } } } \le 1$ That is, $0 \overset {  } { \leq } \sin ^ { - 1 } \frac { \overline { { P _ { i } P } } _ { j } } { 2 r } { \leq \frac { \pi } { 2 } [ 1 5 ] }$ . Because sin $- 1 \frac { \overline { { P _ { i } P _ { j } } } } { 2 r }$ is monotonically related to $\frac { \overline { { P _ { i } P _ { j } } } } { 2 r }$ while $\begin{array} { r } { 0 \leq \frac { \overline { { P _ { i } P _ { j } } } } { 2 r } { \leq } 1 , \widehat { P _ { i } P _ { j } } } \end{array}$ , is monotonically related to $\overline { { P _ { i } P _ { j } } }$ □

## Appendix C

Proof of Proposition 2. The variable $d _ { i \thinspace s * * }$ represents the Euclidean distance between $A _ { i }$ located at $( x _ { i } , y _ { i } , z _ { i } )$ and A located at the north pole $( 0 , 1 0 , 0 )$

$$
\begin{array}{l} d _ {i, * *} ^ {2} = (x _ {i} - 0) ^ {2} + (y _ {i} - 1 0) ^ {2} + (z _ {i} - 0) ^ {2} \\ \quad = \left(x _ {i} ^ {2} + y _ {i} ^ {2} + z _ {i} ^ {2}\right) - 2 0 y _ {i} + 1 0 0 \\ \quad = 1 0 ^ {2} - 2 0 y _ {i} + 1 0 0 = 2 0 0 - 2 0 y _ {i}. \end{array}
$$

From Eq. $( 3 ) , d _ { i , * * } ^ { 2 } = 2 0 0 \Big ( 1 - \frac { \ln { ( S _ { i } ) } } { \ln { ( 1 0 ) } } \Big ) ^ { 2 } = 2 0 0 - 2 0 y _ { i } ,$ we can obtain $y _ { i } = 1 0 - \overset { \cdot } { 1 0 } \bigg ( 1 - \frac { \ln { ( S _ { i } ) } } { \ln { ( 1 0 ) } } \bigg ) ^ { 2 }$ . That is, if $S _ { i } { = } 1$ <sup>ð</sup>then y =0, and if S =10 then y =10. □

## Appendix D

Proof of Proposition 3. If $P * * , \ P _ { i }$ and $P _ { j }$ are on the same longitude with $S _ { i } { > } S _ { j }$ , then $\widehat { P _ { i } P _ { j } } = \widehat { P * * P _ { j } } - \widehat { P * * P _ { i } }$ That is, the value of $\widehat { P _ { * * } } P _ { i } + \widehat { P _ { i } P _ { j } } - \widehat { P _ { * * } } P _ { j }$ is minimal for known $S _ { i }$ and $S _ { j }$ <sup>þ -</sup>. By referring to Proposition 1, the value of $d _ { * * } , ( \mathbf { w } ) + d _ { i , j } \ ( \mathbf { w } ) - d _ { * * } , j \ ( \mathbf { w } )$ is minimal. Since $d _ { i , j }$ is used to represent $\ln ( \delta _ { i , j } )$ , it implies $\ln ( \delta _ { i , * * } ) + \ln ( \delta _ { i , j } ) -$ $\ln ( \delta _ { * * } , )$ is minimal.

$$
\ln \left(\delta_ {i, * *}\right) + \ln \left(\delta_ {i, j}\right) - \ln \left(\delta_ {* *, j}\right)
$$

$$
\begin{array}{l} = \sum_ {k = 1} ^ {m} w _ {k} \big (\ln (C _ {k}) - \ln \big (C _ {i, k} \big) \big) + \sum_ {k = 1} ^ {m} w _ {k} \big (\ln \big (\operatorname * {M a x} \big (C _ {i, k}, C _ {j, k} \big) \big) \\ \quad - \ln \big (\operatorname * {M i n} \big (C _ {i, k}, C _ {j, k} \big) \big) \big) - \sum_ {k = 1} ^ {m} w _ {k} \big (\ln \big (\overline {{C}} _ {k} \big) - \ln \big (C _ {j, k} \big) \big) \\ = \sum_ {k = 1} ^ {m} w _ {k} \big (\ln \big (\operatorname * {M a x} \big (C _ {i, k}, C _ {j, k} \big) \big) - \ln \big (C _ {i, k} \big) \big) \\ \quad + \sum_ {k = 1} ^ {m} w _ {k} \big (\ln \big (C _ {j, k} \big) - \ln \big (M i n \big (C _ {i, k}, C _ {j, k} \big) \big) \big). \end{array}
$$

Since $1 \leq c _ { i , k } \leq 1 0$ for al $i ,$ the minimum value of ln $( \delta _ { i , * * } ) +$ $\ln ( \delta _ { i , j } ) - \ln ( \delta _ { * * , j } )$ is 0. That implies l $\scriptstyle 1 ( \delta _ { i } , _ { j } ) = \ln ( \delta _ { j , * * } ) -$ $\ln ( \delta _ { i , * * } )$ . On the other hand, if ln $( \delta _ { i \cdot j } ) { = } \ln ( \delta _ { j , { * * } } ) - \ln ( \delta _ { i , { * * } } ) .$ , it implies $d _ { * * , i } ( \mathbf { w } ) + d _ { i , j } ( \mathbf { w } ) - d _ { * * , j } ( \mathbf { w } )$ is minimal, which means $P * * , P _ { i }$ and $P _ { j }$ are located on the same arc along the great circle. That is, $P _ { * * , \ P _ { i } }$ and $P _ { j }$ are on the same longitude. □

## Appendix E

Proof of Proposition 4. $A _ { i } \succ A _ { j }$ implies $C _ { i , k } { \geq } C _ { j , k } ,$ for all k. From Eq. (3),

$$
\begin{array}{l} \ln \left(\delta_ {i, j}\right) \\ = \left(\sum_ {k = 1} ^ {m} w _ {k} \left(\ln \left(\operatorname{Max} \left(C _ {i, k}, C _ {j, k}\right)\right)\right) - \ln \left(\operatorname{Min} \left(C _ {i, k}, C _ {j, k}\right)\right)\right) \\ = \sum_ {k = 1} ^ {m} w _ {k} \left(\ln \left(C _ {i, k}\right) - \ln \left(C _ {j, k}\right)\right) \\ = \sum_ {k = 1} ^ {m} w _ {k} \left((\ln (1 0) - \ln \left(C _ {j, k}\right)) - (\ln (1 0) - \ln \left(C _ {i, k}\right))\right) \\ = \ln \left(\delta_ {j, * *}\right) - \ln \left(\delta_ {i, * *}\right). \end{array}
$$

From Proposition 3, $P _ { * * , \textit { P } _ { i } }$ and $P _ { j }$ are on the same longitude.

## Appendix F

Proof of Proposition 5. Since $S _ { i } ( \mathbf { w } ) { > } S _ { j } ( \mathbf { w } )$ and $P _ { i } , P _ { j }$ are on the same longitude, $\ln ( \delta _ { i \cdot i } ) { = } \ln ( \delta _ { j , { * * } } ) - \ln ( \delta _ { i , { * * } } )$ $\ln \left( \delta _ { j , \ast \ast } \right) - \ln \left( \delta _ { i , \ast \ast } \right) = \sum _ { k = 1 } ^ { m } w _ { k } \left( \ln \left( 1 0 \right) - \ln \left( C _ { j , k } \right) - \ln ( 1 0 ) + \right.$ ln $\left( C _ { i , k } \right) ) = \sum _ { , \ast } ^ { m } \ w _ { k } \left( \ln ( C _ { i , k } ) - \ln ( C _ { j , k } ) \right) = \ln ( \delta _ { i , j } ) =$ $\sum _ { k = 1 } ^ { m } w _ { k } \big ( \ln \bigl ( \mathrm { M a x } \bigl ( C _ { i , k } , C _ { j , k } \bigr ) \bigr ) - \ln \bigl ( \mathrm { M i n } \bigl ( C _ { i , k } , C _ { j , k } \bigr ) \bigr ) \bigr )$ ; which <sup>¼</sup>implies $C _ { i , k } { \ge } C _ { j , k }$ for all k. That is $A _ { i } { \succ } A _ { j }$

## Appendix G

Proof of Proposition 6. The proof is similar to Propositions 4 and 5. In addition, all points mapped at the same longitude of a sphere must be located at the same cutting plane of a sphere, i.e. $ a x _ { i } + b y _ { i } + c z _ { i } + d = 0$ , where $a , b , c$ and d are constants. Because the cutting plane has to pass through the origin $( 0 , 0 , 0 )$ and the north pole $( 0 , 1 0 , 0 ) , b = d = 0$ . That is, all points located at the same longitude of a sphere must satisfy equality $a x _ { \mathrm { i } } + c z _ { i } { = } 0$

## Appendix H

Proof of Theorem 2. (i) If $A _ { i }$ is consistently even swapped into $A _ { i } ^ { \prime } ,$ then $S _ { i } { = } S _ { i } ^ { \prime } ,$ , which means $y _ { i } { = } y _ { i } ^ { \prime }$ (Proposition 2). Therefore, $P _ { i }$ and $P _ { i } ^ { \prime }$ are on the same latitude. (ii) If $P _ { i }$ and $P _ { i } ^ { \prime }$ are on the same latitude, then $y _ { i } { = } y _ { i } ^ { \prime }$ which implies $S _ { i } { = } S _ { i } ^ { \prime } . ~ A _ { i } ^ { \prime }$ therefore is consistently even swapped from $A _ { i } .$

## References

[1] J. Barzilai, Deriving weights from pairwise comparison matrices, Journal of the Operational Research Society 48 (12) (1997) 1226–1232.

[2] J. Barzilai, Measurement and preference function modeling, International Transactions in Operational Research 12 (2005) 173–183.

[3] I. Borg, P. Groenen, Modern Multidimensional Scaling, Springer, New York, 1997.

[4] C.M. Brugha, Relative measurement and the power function, European Journal of Operational Research 121 (2000) 627–640.

[5] C.M. Brugha, Phased multicriteria preference finding, European Journal of Operational Research 158 (2004) 308–316.

[6] C.W. Cobb, P.H. Douglas, A theory of production, American Economic Review 18 (Supplement) (1928) 139–165.

[7] E. Condon, B. Golden, S. Lele, S. Raghavan, E. Wasil, A visualization model based on adjacency data, Decision Support Systems 33 (2002) 349–362.

[8] T.F. Cox, M.A.A. Cox, Multidimensional scaling on a sphere, Communications on Statistics – Theory and Methods 20 (9) (1991) 2943–2953.

[9] T.F. Cox, M.A.A. Cox, Multidimensional Scaling, CRC Press, 2000.

[10] B. Franklin, Letter to Joseph Priestly, Benjamin Franklin Sampler, 1956.

[11] C. Genest, S.S. Zhang, A graphical analysis of ratio-scaled paired comparison data, Management Science 42 (3) (1996) 335–349.

[12] J.C. Gower, The analysis of asymmetry and orthogonality, in: J.-R. Barra, F. Brodeau, G. Romier, B. Van Cutsem (Eds.),

Recent Developments in Statistics, North-Holland, Amsterdam, 1977, pp. 109–123.

[13] R.P. Hämäläinen, J. Mustajoki, Making even swaps even easier, http://www.smart-swaps.hut.fi/, System Analysis Laboratory, Helsinki University of Technology, 2004.

[14] J.S. Hammond, R.L. Keeney, H. Raiffa, Even Swaps — A Rational Method for Making Trade-offs. Harvard Business Review on Decision Making, March–April 1998.

[15] R.E. Johnson, F.L. Kiokemeister, E.S. Wolk, Calculus with Analytic Geometry, Allyn and Bacon, Inc., 1978, pp. 312–313.

[16] M.Y. Kiang, Extending the Kohonen self-organizing map networks for clustering analysis, Computations Statistics and Data Analysis 38 (2001) 161–180.

[17] T. Kohonen, Self-Organizing Maps, Springer, Berlin, 1995.

[18] J.B. Kruskal, Non-metric multidimensional scaling: a numerical method, Psychometrica 29 (1964) 115–129.

[19] H.L. Li, Incorporation competence sets of decision makers by deduction graphs, Operations Research 47 (2) (1999) 209–220.

[20] Lindo System Inc., Lingo 9.0, 2005 www-document http://www. lindo.com/.

[21] J.D.C. Little, Comments on models and managers: the concept of a decision calculus, Management Science 50 (12) (2004) 1854–1860.

[22] J. Sammon, A nonlinear mapping for data structure analysis, IEEE Transactions on Computers C-18 (5) (1969) 401–409.

[23] Y. Xiang, M. Chau, H. Atabakhsh, H. Chen, Visualizing criminal relationships: comparison of a hyperbolic tree and a hierarchical list, Decision Support Systems 41 (2005) 69–83.

[24] C.C. Yang, H. Chen, K. Hong, Visualization of large category map for internet browsing, Decision Support Systems 35 (2003) 89–102.

Han-Lin Li is a Chair Professor of National Chiao Tung University, Taiwan. He received his PhD degree from University of Pennsylvania, USA. His articles have appeared in Decision Support Systems, Operations Research, Fuzzy Sets and Systems, Journal of the Operational Research Society, European Journal of Operational Research, Journal of Global Optimization, Computers and Operational Research, and many other publications.

Li-Ching Ma is an Associate Professor in the Department of Information Management at National United University, Taiwan. She received her PhD degree in Information Management from National Chiao Tung University, Taiwan. Her research interests include decision-making, visualization, and optimization.
