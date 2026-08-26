---
otero_id: 6846
otero_key: "SGQSZYCD"
title: "Consensus model for multi-criteria large-group emergency decision making considering non-cooperative behaviors and minority opinions"
authors: "Xuan-hua Xu; Zhi-jiao Du; Xiao-hong Chen"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.08.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Consensus model for multi-criteria large-group emergency decision making considering non-cooperative behaviors and minority opinions

![](/api/attachments/SGQSZYCD/fulltext/images/579d831b8cded48174c0a66700ba2359426673e2efb52f3ef62819ddccf4964a.jpg)

Xuan-hua Xu, Zhi-jiao Du ⁎, Xiao-hong Chen

School of Business, Central South University, Changsha 410083, PR China

## a r t i c l e i n f o

Article history: Received 5 February 2015 Received in revised form 25 July 2015 Accepted 24 August 2015 Available online 2 September 2015

Keywords: Large-group emergency decision making Non-cooperative behavior Minority opinion Consensus

## a b s t r a c t

Emergency situations often demand high-quality decision-making results because a wrong decision may cause incalculable losses. Therefore, in such cases, the views of all decision makers should be fully considered, especially minority opinions, and the interests of all parties should be well balanced. Additionally, an emergency decision often has to be made within a short period of time, which may require the rational treatment of noncooperative behaviors. Classical consensus models mainly focus on group decision-making problems where a small number of decision makers participate. However, an emergency decision often involves many stakeholders, and thus requires the participation of larger number of decision makers. In this paper, an improved consensus model is proposed for large-group emergency decision making, and an approach to managing minority opinions and non-cooperative behaviors is described. By simulating the consensus reaching process, a method is presented to determine two important parameters: the minimum group consensus threshold and the maximum number of iterations. Finally, an illustrative example proves that the proposed consensus model is feasible and effective, and a detailed discussion highlights the advantages of this model for managing large-group emergency decision-making problems.

© 2015 Elsevier B.V. All rights reserved

## 1. Introduction

In recent years, emergency events have occurred frequently around the world, often resulting in devastating consequences. Emergency decision making is typically characterized by time limitations, partial or incomplete information, and decision pressure resulting from potentially serious outcomes [1–4]; therefore, emergency decision making poses a great challenge for both government and society. In general, there exist some response plans that play a crucial role in emergency management and disaster effect reduction [4,5]. Because of the accompanying complexity and uncertainty, an emergency decision often requires the involvement of multiple decision makers (DMs), which can lead to the multi-criteria group decision-making (MCGDM) problem. Currently, MCGDM problems are receiving increasing attention in the field of decision science [4,6–10]. Because emergencies often have a large impact on public interests, MCGDM applied to emergency management commonly involves the participation of large numbers of DMs from diverse professional backgrounds in the decision-making process. Such multi-criteria large-group emergency decision-making (MCLGEDM) problems are characterized by the following four features [3,11]: (a) the group usually involves more than 20 DMs from different sectors and professional fields, (b) the final decision must be made within a short period of time, (c) it is often very difficult to reach a unanimous agreement among the DMs, and (d) a wrong decision or one made too slowly may result in disastrous losses.

Because of the complex participant composition in MCLGEDM problems, opinion and preference differences among DMs are inevitable. Generally, both of the two processes are used to address such problems: the consensus process and the selection process [12,13]. Reaching a consensus is often a dynamic and iterative group-discussion process, which indicates that some DMs must modify their opinions to reach a compromise [14]. Ideally, consensus refers to unanimity among individuals when selecting an option or a course of action that best represents the interests of the entire group. However, unanimity is difficult to attain, particularly among large and diversified group members as is the case in real world settings. Thus, “soft” consensus level is widely used in the consensus process [15,16]. Soft consensus is more flexible and reflects the large spectrum of possible partial agreements. Research on consensus modeling has drawn increasing attention in the field of decision science [17–26]. However, traditional consensus models mostly focus on conventional decision-making problems involving a few DMs (e.g., 3–5 persons) without time limitations, which may not be appropriate for large-group decision making in an emergency environment. To address large-group decision-making problems, Palomares [27] proposed an attitude-based consensus model for large-scale group decision support in IT services management. Palomares et al. [28] presented a consensus model for managing large-scale DMs that incorporated a fuzzy clustering-based scheme to handle non-cooperative behaviors of individuals and subgroups. However, neither of these two consensus models [27,28] can be applied directly to MCLGEDM problems as they fail to consider time pressures and complexity. A wrong decision can result in inestimable losses, so all of the opinions provided by DMs, especially minority opinions, should be fully and seriously considered. Xiong et al. [29] stressed the importance of minority opinions in the process of consensus building and proposed a consensus mechanism to protect such opinions. Furthermore, an emergency decision must achieve a relatively satisfactory result within a short time period; this requires effective coordination of non-cooperative behaviors. Although non-cooperative behaviors should be taken into account to assure the quality of decision results, it is also very important to ensure the timeliness of decision making. Few existing studies focus on how to balance this relationship between quality and timeliness, or how to construct a reasonable consensus mechanism to deal with non-cooperative behaviors. Palomares et al. [28] presented a punishment mechanism to manage non-cooperative behaviors; however, the mechanism did not consider the emergency background and failed to provide an approach to deal with minority opinions. Therefore, it is of great theoretical significance and practical value to develop a consensus model that fully considers minority opinions and appropriately handles non-cooperative behaviors in MCLGEDM problems.

The remainder of this paper is organized as follows. Section 2 provides an introduction to minority opinions and non-cooperative behaviors as well as some preliminaries regarding MCLGEDM problems and consensus modeling. Section 3 shows how a clustering method can be used to manage a large group and analyze the group consensus level. In Section 4, an improved consensus model for MCLGEDM problems that considers minority opinions and non-cooperative behaviors is presented. In Section $5 ,$ an illustrative example is used to show the utility and applicability of the proposed consensus model. Section 6 provides a detailed discussion regarding the advantages of the proposed model in dealing with MCLGEDM problems. Finally, the main conclusions are presented in Section 7.

## 2. Background

This section provides preliminary information regarding minority opinions, non-cooperative behaviors, and MCLGEDM problems. Additionally, a typical consensus process, which is the key process to reach an agreement in MCGDM problems, is presented.

## 2.1. Minority opinion and non-cooperative behavior

Although differing opinions and minority preferences are often considered hindrances to decision making, proper treatment for them can lead to a more reasonable and appropriate decision result. Members who hold minority opinions in a group can generally be divided into the following four types [29]: (a) a leader, who is able to provide forward-looking and unique views, and has the right to determine the final decision alternative; (b) an expert, who often has a considerable understanding of the decision-making problem, and is able to propose professional and authoritative opinions; (c) a young and aggressive DM, who has relatively extreme, usually personally motivated opinions, and who is less affected by others' opinions; and (d) a noteworthy and independent DM, who provides a view that is often out of the ordinary, and generally does not follow herd mentality. Regarding these four types of DMs, the opinions provided by the first two should be assigned the greatest value, while those of the latter two must be considered with care.

In a MCLGEDM problem, there are commonly several individuals or subgroups who are unwilling to modify their respective opinions to reach an agreement because, for such individuals, making a compromise often means sacrificing their own interests. Therefore, it is advisable to improve existing consensus models to detect and manage non-cooperative individuals and subgroups [30].

## 2.2. MCLGEDM problems

A MCLGEDM problem can be defined as a situation where a large number of DMs must make a high-quality and timely decision to address multiple criteria in response to an emergency by choosing among a set of viable alternatives. The main elements of a typical MCLGEDM problem are as follows:

(a) A discrete finite set of emergency alternatives $X = \{ x _ { 1 } , x _ { 2 } , . . . , x _ { P } \}$ $( P \ge 2 ) ,$ , which present possible solutions to the problem;

(b) A set of DMs or experts $E = \{ e _ { 1 } , e _ { 2 } , . . . , e _ { M } \} \ ( M \geq 2 )$ who express their opinions (namely, judgments and preferences) about the alternatives in set X. The weight vector of the DMs is

$\pmb { \theta } = ( \theta _ { 1 } , \theta _ { 2 } , . . . , \theta _ { M } ) ^ { T }$ , where $\theta _ { i } \geq 0 ( i = 1 , 2 , . . . , M )$ and $\sum _ { i = 1 } ^ { M } \theta _ { i } = 1$

<sup>¼</sup>Usually, when the number of DMs in a group exceeds 11, that $\mathrm { i } s , M \geq 1 1$ , the group is considered a large group and the decision-making process in which they participate can be defined as large-group decision making [31].

(c) A set of criteria $F = \{ f _ { 1 } , f _ { 2 } , . . . , f _ { N } \} \left( N \geq 2 \right)$ , and the weight vector of the criteria ${ \pmb { \omega } } = ( \omega _ { 1 } , \omega _ { 2 } , . . . , \omega _ { N } ) ^ { T }$ , where $\omega _ { j } \geq 0 ( j = 1 , 2 , . . . , N )$ and $\sum _ { j = 1 } ^ { N } \omega _ { j } = 1 .$

(d) Time limitation is an important consideration in an emergency problem; the final decision result must be made within a limited period.

Let $V ^ { i } = ( \nu _ { l j } ^ { i } ) _ { P \times N } ( i = 1 , 2 , . . . , M )$ be the decision matrix given by DM $e _ { i } \in E ,$ where $\nu _ { l j } ^ { i }$ is an accurate value representing the opinion value for the alternative $x _ { l } \in X$ with respect to the criterion $f _ { j } \in F .$ . Based on Yu and Lai [4] and Palomares et al. [28], without considering opinion differences among DMs, MCLGEDM problem-solving usually comprises the following four steps:

Step 1 Normalize original individual decision matrices.

In MCLGEDM, decision-making criteria often fall into two categories: benefit criteria and cost criteria. Here, the individual decision matrix $V ^ { i } = ( \nu _ { l j } ^ { i } ) _ { P \times \ I }$ is normalized into a standardized decision matrix $R ^ { i } \ = \ ( r _ { l j } ^ { i } ) _ { P } \ \times \ N ,$ where [22] $r _ { l j } ^ { i } = \frac { \nu _ { l j } ^ { i } - \displaystyle \operatorname* { m i n } _ { l } \{ \nu _ { l j } ^ { i } \} } { \displaystyle \operatorname* { m a x } _ { l } \{ \nu _ { l j } ^ { i } \} - \displaystyle \operatorname* { m i n } _ { l } \{ \nu _ { l j } ^ { i } \} } ,$ , for benefit criterion $f _ { j } \in F , j =$

$1 , 2 , . . . , N ,$ and $r _ { l j } ^ { i } = \frac { \underset { l } { \operatorname* { m a x } } \{ \nu _ { l j } ^ { i } \} - \nu _ { l j } ^ { i } } { \underset { l } { \operatorname* { m a x } } \{ \nu _ { l j } ^ { i } \} - \underset { l } { \operatorname* { m i n } } \{ \nu _ { l j } ^ { i } \} }$ , for cost criterion $f _ { j } \in F , j = 1 , 2 , . . . , N .$

Step 2 Cluster the normalized individual decision matrices.

A clustering method is applied to divide the large group into $K ( 1 \leq K \leq M )$ small-scale subgroups. The clusters' decision matrices can then be obtained as $G ^ { k } = ( g _ { l j } ^ { k } ) _ { P \times N } ( k = 1 , 2 , . . . , K )$ Step 3 Aggregate the clusters' decision matrices.

Suppose that the weight vector of the clusters is $\lambda \ =$ $( \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { K } ) ^ { T }$ . The weighted averaging (WA) operator is usually used to aggregate the clusters' opinions and obtain the group decision matrix, that is, $R ^ { c } = ( r _ { l j } ^ { c } ) _ { P \times N } ,$ such that

$$
r _ {l j} ^ {c} = W A \left(g _ {l j} ^ {1}, g _ {l j} ^ {2}, \dots , g _ {l j} ^ {K}\right) = \sum_ {k = 1} ^ {K} \lambda_ {k} g _ {l j} ^ {k}\tag{1}
$$

where $\lambda _ { k }$ represents the weight of cluster $C ^ { k } ,$ meeting the conditions that ${ \lambda _ { k } \geq 0 } \left( k = 1 , 2 , . . . , K \right)$ and $\sum _ { k = 1 } ^ { K } \lambda _ { k } = 1$

Step 4 Select the best alternative(s).

Based on the group decision matrix, the WA operator is employed to aggregate all the elements in the l-th row of R<sup>c</sup>, and the overall evaluation value of every alternative, that is, $E V ( l ) ( l = 1 , 2 , . . . , P ) ,$ can be obtained as

$$
E V (l) = \sum_ {j = 1} ^ {N} \omega_ {j} r _ {l j} ^ {c}.\tag{2}
$$

The emergency alternatives can then be ranked based on the overall evaluation values and the best alternative(s) can be selected.

## 2.3. Consensus modeling in MCGDM problems

The ideal result of the consensus process is complete agreement among all DMs, that is, that they all hold the same opinion. However, it is quite difficult, if not impossible in many cases, to achieve such a high level of consensus in opinions. Thus, a more flexible approach, called “soft” consensus, is proposed, based on the measure of similarity or dissimilarity among DMs' opinions.

Definition 1. Suppose that $R ^ { i } = ( r _ { l j } ^ { i } ) _ { P \times N }$ is the normalized individual decision matrix provided by DM $e _ { i } ,$ and $R ^ { c } = ( r _ { l j } ^ { c } ) _ { P \times N }$ is the group decision matrix. Thus, the consensus level between R<sup>i</sup> and $R ^ { c }$ is defined as

$$
C I \left(R ^ {i}\right) = 1 - \frac {1}{P \times N} d \left(R ^ {i}, R ^ {c}\right)\tag{3}
$$

where $d ( R ^ { i } , R ^ { c } )$ is the Manhattan distance between $R ^ { i }$ and $R ^ { c } ,$ that is,

$$
d \left(R ^ {i}, R ^ {c}\right) = \sum_ {l = 1} ^ {P} \sum_ {j = 1} ^ {N} \left| r _ {l j} ^ {i} - r _ {l j} ^ {c} \right|.\tag{4}
$$

The group consensus level GCI can be obtained as

$$
G C I = \frac {1}{M} \sum_ {i = 1} ^ {M} C I (R ^ {i}).\tag{5}
$$

If GCI = 1, this indicates that all DMs have reached full and unanimous consensus among the group. A larger GCI indicates a higher level of consensus among all DMs. GCI is set as the predefined minimum group consensus threshold that is used to determine whether the consensus reaching process should be carried out. If GCI ≥GCI, the group consensus level is considered to be sufficiently high, and the selection process may progress; otherwise, the consensus process should be applied to change some opinions to achieve a higher level of consensus.

## 3. Opinion clustering and consensus measure

Because of the complexity and uncertainty of MCLGEDM problems, efforts should be made to address consensus challenges, and consensus models should be capable of integrating the large number of DMs.

## 3.1. Opinion clustering and aggregation

For MCLGEDM problems, opinion clustering is often used as the basis by which to analyze and manage DMs' opinions. Xu and Chen [32,33] proposed a vector space-based clustering method for addressing large-group decision-making problems. This paper extends the application of this clustering method to MCLGEDM problems. Using this clustering method, a large group can be divided into $K ( 1 \leq K \leq M )$ clusters. The DMs' respective weights in the decision-making process can be determined by using the following two rules: (a) DMs in the same cluster can be assigned the same weight because they have similar opinion information, and (b) DMs in larger-scale clusters should be assigned larger weights based on the majority principle. Therefore, the weight of DM $e _ { i }$ is calculated as

$$
\theta_ {i} = n _ {k} \Big / \sum_ {k = 1} ^ {K} (n _ {k}) ^ {2}\tag{6}
$$

where $i = 1 , 2 , . . . , n _ { k } , i \in C ^ { k } ,$ and n is the number of DMs in cluster $C ^ { k } .$ The weight of cluster $C ^ { k }$ can then be obtained as

$$
\lambda_ {k} = n _ {k} \cdot \theta_ {i}\tag{7}
$$

It is easy to know that $0 < \lambda _ { k } \leq 1$ and $\sum _ { k } ^ { K } = \ d _ { 1 } \lambda _ { k } = 1$ . By utilizing the WA operator, the decision matrix of cluster $C ^ { k }$ can be obtained as $\bar { G } ^ { k } =$ $( g _ { l j } ^ { k } ) _ { P \times N } ,$ where $\begin{array} { r } { g _ { l j } ^ { k } = \sum _ { i = 1 } ^ { n _ { k } } \theta _ { i } r _ { l j } ^ { i } } \end{array}$ . Similarly, the group decision matrix can be represented as $R ^ { c } = ( r _ { l j } ^ { c } ) _ { P \times N } ,$ where $\begin{array} { r } { r _ { l j } ^ { c } = \sum _ { k } ^ { K } = { _ { 1 } \lambda _ { k } } g _ { l j } ^ { k } } \end{array}$

## 3.2. Consensus measure

Definition 2. Based on Eqs. (3) and $( 4 ) ,$ , the cluster consensus level $C I ( G ^ { k } )$ between the cluster decision matrix $G ^ { k } ( k = 1 , 2 , . . . , K )$ and the group decision matrix $R ^ { c }$ is defined as

$$
C I \left(G ^ {k}\right) = 1 - d \left(G ^ {k}, R ^ {c}\right) = 1 - \frac {1}{P \times N} \sum_ {l = 1} ^ {P} \sum_ {j = 1} ^ {N} \left| g _ {l j} ^ {k} - r _ {l j} ^ {c} \right|.\tag{8}
$$

The group consensus level can be obtained as

$$
G C I = \frac {1}{K} \sum_ {k = 1} ^ {K} C I \left(G ^ {k}\right).\tag{9}
$$

Thus, it is simple to determine that $0 \leq G C I \leq 1$ . If $G C I { \geq } { \overline { { G C I } } }$ , the selection process is followed; otherwise, the consensus process should be applied to change some opinions.

4. Improved consensus model for MCLGEDM problems, which considers minority opinions and non-cooperative behaviors

Because a decision result is very important in a MCLGEDM problem, minority opinions and non-cooperative behaviors must be taken into account. This section outlines how these two factors are incorporated into the general consensus model and presents a simulation method to determine some important parameters in the consensus reaching process.

## 4.1. Determination of comprehensive adjustment coefficient

The pressures of decision making in MCLGEDM often lead to uncertainty and subjectivity in the opinion adjustment coefficients provided by the DMs. To improve decision credibility, we introduce a novel adjustment coefficient, here defined as comprehensive adjustment coefficient. Before discussing this new opinion adjustment coefficient, subjective and objective adjustment coefficients are first introduced.

## 4.1.1. Subjective adjustment coefficient

Suppose that $\bar { G } ^ { k ( t ) } = ( g _ { l j } ^ { k ( t ) } ) _ { P \times N }$ is the decision matrix of cluster $C ^ { k } ,$ and $\hat { R ^ { c ( t ) } } = ( r _ { l j } ^ { c ( t ) } ) _ { P \times N }$ is the group decision matrix in the t-th iteration. If the group consensus level $G C I ^ { ( t ) }$ is less than the predefined consensus threshold GCI after consensus measure, that ${ \mathrm { i } } s ,$ if $G C I ^ { ( t ) } { < } \overline { { G C I } } ,$ it will be necessary to initiate the consensus reaching process.

Suppose that cluster $C ^ { k ^ { * } } ( k ^ { * } = 1 , 2 , . . . , K )$ has the largest difference from the group, that $\mathrm { i } s , C I ( G ^ { k ^ { * } ( t ) } ) = m i n \{ C I ( G ^ { k ( t ) } ) \big | k = 1 , 2 , . . . , K \}$ . Based on the practical decision situation and group consensus level, cluster $C ^ { k ^ { * } }$ $( k ^ { * } = 1 , 2 , . . . , K )$ can give its adjustment coefficient denoted as $\eta _ { k ^ { * } } ^ { S ( t ) } ( 0 \leq$ $\eta _ { k ^ { * } } ^ { S ( t ) } \leq 1 )$ , which is an adjustment coefficient aimed at modifying the cluster's opinion. The adjustment coefficient put forward by cluster $C ^ { k ^ { * } }$ reflects its attitude towards the group consensus level and opinion amendment, and is therefore called a subjective adjustment coefficient.

## 4.1.2. Objective adjustment coefficient

$\begin{array} { r } { \mathrm { L e t } \eta _ { k ^ { * } } ^ { O ( t ) } = \frac { ( 1 - C I ( G ^ { k ^ { * } ( t ) } ) ) - ( 1 - \overline { { G C I } } ) } { 1 - C I ( G ^ { k ^ { * } ( t ) } ) } } \end{array}$ be the objective adjustment coefficient, which represents the degree of respect that cluster $C ^ { k ^ { * } }$ has for the group opinion in the t-th iteration according to the predefined calculation rules.

As a rule, the lower the cluster consensus level of cluster $C ^ { k ^ { * } }$ , the more corresponding objective adjustment coefficient $\eta _ { k ^ { * } } ^ { O ( t ) }$ . It follows logically that the larger the difference between a cluster and a group, the more the cluster's opinion may be modified to reach an agreement.

A further rule is that the higher GCI is set, the greater the effort that DMs must make, because a high level of group consensus usually requires more concessions to be made. Often GCI is set to be smaller than 0.90 [12,25], especially in a large-group decision making problem [27,28]. That is, $1 - C I ( G ^ { k ^ { * } ( t ) } )$ cannot be very close or equal to $0 ,$ and the value of the objective adjustment coefficient $\eta _ { k ^ { * } } ^ { O ( t ) }$ can fall into the interval [0, 1].

## 4.1.3. Comprehensive adjustment coefficient

By combining subjective and objective adjustment coefficients, the comprehensive adjustment coefficient $\eta _ { k ^ { * } } ^ { ( t ) }$ can be determined based on the following rules:

$\mathrm { i f } \eta _ { k ^ { * } } ^ { S ( t ) } \ge \eta _ { k ^ { * } } ^ { O ( t ) }$ , then $\eta _ { k ^ { * } } ^ { ( t ) } = \eta _ { k ^ { * } } ^ { S ( t ) }$ , and i $\dot { \eta } _ { k ^ { * } } ^ { \dot { S } ( t ) } < \eta _ { k ^ { * } } ^ { \ddot { O } ( t ) }$ Þ , then $\begin{array} { r } { \eta _ { k ^ { * } } ^ { ( t ) } = \varepsilon \eta _ { k ^ { * } } ^ { S ( t ) } + ( 1 - \varepsilon ) \eta _ { k ^ { * } } ^ { O ( t ) } } \end{array}$ , where $0 \leq \eta _ { k ^ { * } } ^ { ( t ) } \leq 1$ , and ε (0 ≤ ε ≤ 1) is a weight coefficient that is used to determine the weight of the subjective adjustment coefficient in the comprehensive adjustment coefficient.

Eq. (10) can then be used to modify the decision matrix of cluster $C ^ { k ^ { * } }$ as follows:

$$
G ^ {k ^ {*} (t + 1)} = \eta_ {k ^ {*}} ^ {(t)} R ^ {c (t)} + \left(1 - \eta_ {k ^ {*}} ^ {(t)}\right) G ^ {k ^ {*} (t)}\tag{10}
$$

where $G ^ { k ^ { * } ( t + 1 ) }$ represents the opinion of cluster $C ^ { k ^ { * } }$ after the t-th iteration. Using different types of adjustment coefficients, we obtain other opinion adjustment equations:

$$
G ^ {k ^ {*} (t + 1)} = \eta_ {k ^ {*}} ^ {S (t)} R ^ {c (t)} + \left(1 - \eta_ {k ^ {*}} ^ {S (t)}\right) G ^ {k ^ {*} (t)}\tag{10.a}
$$

$$
G ^ {k ^ {*} (t + 1)} = \eta_ {k ^ {*}} ^ {O (t)} R ^ {c (t)} + \left(1 - \eta_ {k ^ {*}} ^ {O (t)}\right) G ^ {k ^ {*} (t)}\tag{10.b}
$$

where $0 \le \eta _ { k ^ { * } } ^ { S ( t ) } \le 1$ and $\hslash { \leq } \eta _ { k ^ { * } } ^ { O ( t ) }$ ≤1 as abovementioned. Based on Xu [22], it can be shown that the group consensus level can increase up to the predefined consensus threshold with time by applying one of the three opinion adjustment equations (i.e., Eqs. (10), (10.a) and (10.b)) to modify the DMs' opinions.

## 4.2. Determination of the required parameters in the consensus process

Before the consensus process begins, the minimum group consensus threshold GCI should be fixed. Herrera-Viedma et al. [12] stated that the determination of GCI should depend on the particular decision-making problem. When the decision to be made will result in a consequence of vital importance, the minimum group consensus threshold is required to be as high as possible. Conversely, in cases where the consequences are not as critical, but a solution is still urgently required, the threshold value is required to be close to 0.5. However, the idea proposed by Herrera-Viedma et al. [12] is qualitative and mainly depends on DMs' experience. Furthermore, Chiclana et al. [34] concluded that different distance functions could often lead to significantly different decision results. Thus, it is necessary to develop a practical and quantitative method to determine the minimum group consensus threshold. As time is limited in MCLGEDM problems, another parameter, the maximum number of iterations, denoted by $C T ,$ should also be fixed at the beginning of the consensus process.

An appropriate method to confirm the two parameters is to simulate the consensus reaching process by using Eq. (10.b) on the basis of the objective adjustment coefficient. Thus, simulation results can be obtained in which the relationship between the number of iterations and the group consensus threshold value is depicted in detail. The simulation results should also include opinion adjustment amounts.

Definition 3. (Zhang et al. [17]). Based on Eq. (4), the opinion adjustment amount between $G ^ { k ( t { \dot { \cdot } } 1 { \dot { ) } } }$ and $G ^ { k ( t ) }$ can be defined as

$$
A D \left(G ^ {k (t + 1)}, G ^ {k (t)}\right) = \frac {1}{P \times N} d \left(G ^ {k (t + 1)}, G ^ {k (t)}\right)\tag{11}
$$

where $d ( G ^ { k ( t + 1 ) } , G ^ { k ( t ) } )$ is the Manhattan distance between $G ^ { k ( t + 1 ) }$ and $G ^ { k ( t ) }$

Both timeliness and decision quality are important factors in a MCLGEDM problem. The minimum group consensus threshold should not be set too high, because a higher threshold means more iterations and greater adjustments will be required, and possibly leading to a distorted decision result. Based on the original decision information presented in the illustrative example (see Table 1 in Section $5 ) ,$ the simulation results are shown in Fig. 1. Intuitively, different predefined threshold values will usually result in differences in the number of iterations, the change trajectory of group consensus levels, and the opinion adjustment amount. Combining the simulation results (see Fig. 1) with the practical decision-making situation, DMs can assign relatively reasonable values to the two parameters.

Based on the original individual decision matrices presented in Section $5 ,$ the initial group consensus level is calculated as $G C I ^ { ( 0 ) } =$ 0.7386. The process of determining the two parameters should focus on the following three aspects:

(a) Check the decision condition to determine whether there is sufficient time to make the decision. Having enough time indicates that multiple iterations and a larger group consensus threshold can be set. For example, when the value GCI is set as 0.85, the number of iterations is 6 and the overall opinion adjustment amount is 0.6762 based on the simulation results shown in Fig. 1. Conversely, if less time is available, the number of iterations should be under a lower range. In this case, GCI will be set to meet the condition that 0:7386≤GCI≤0:85.

Original individual decision matrices $V ^ { i ( 0 ) } ( i = 1 , 2 , . . . , 2 0 ) .$

<table><tr><td></td><td></td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td></td><td></td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td></tr><tr><td rowspan="5"> $e_1$ </td><td> $x_1$ </td><td>10</td><td>3</td><td>0.7</td><td rowspan="5"> $e_2$ </td><td> $x_1$ </td><td>90</td><td>6</td><td>0.3</td></tr><tr><td> $x_2$ </td><td>20</td><td>2</td><td>0.4</td><td> $x_2$ </td><td>50</td><td>6</td><td>0.8</td></tr><tr><td> $x_3$ </td><td>30</td><td>8</td><td>0.5</td><td> $x_3$ </td><td>50</td><td>3</td><td>0.7</td></tr><tr><td> $x_4$ </td><td>40</td><td>1</td><td>0.2</td><td> $x_4$ </td><td>20</td><td>3</td><td>0.7</td></tr><tr><td> $x_5$ </td><td>50</td><td>9</td><td>0.4</td><td> $x_5$ </td><td>40</td><td>9</td><td>0.4</td></tr><tr><td rowspan="5"> $e_3$ </td><td> $x_1$ </td><td>80</td><td>6</td><td>0.2</td><td rowspan="5"> $e_4$ </td><td> $x_1$ </td><td>80</td><td>4</td><td>0.3</td></tr><tr><td> $x_2$ </td><td>50</td><td>5</td><td>0.8</td><td> $x_2$ </td><td>50</td><td>6</td><td>0.8</td></tr><tr><td> $x_3$ </td><td>60</td><td>3</td><td>0.6</td><td> $x_3$ </td><td>50</td><td>3</td><td>0.7</td></tr><tr><td> $x_4$ </td><td>30</td><td>3</td><td>0.6</td><td> $x_4$ </td><td>10</td><td>4</td><td>0.6</td></tr><tr><td> $x_5$ </td><td>50</td><td>8</td><td>0.3</td><td> $x_5$ </td><td>40</td><td>8</td><td>0.4</td></tr><tr><td rowspan="5"> $e_{17}$ </td><td> $x_1$ </td><td>50</td><td>6</td><td>0.7</td><td rowspan="5"> $e_{18}$ </td><td> $x_1$ </td><td>80</td><td>4</td><td>0.2</td></tr><tr><td> $x_2$ </td><td>60</td><td>6</td><td>0.2</td><td> $x_2$ </td><td>50</td><td>8</td><td>0.2</td></tr><tr><td> $x_3$ </td><td>50</td><td>6</td><td>0.1</td><td> $x_3$ </td><td>30</td><td>5</td><td>0.4</td></tr><tr><td> $x_4$ </td><td>40</td><td>9</td><td>0.6</td><td> $x_4$ </td><td>60</td><td>6</td><td>0.2</td></tr><tr><td> $x_5$ </td><td>60</td><td>2</td><td>0.4</td><td> $x_5$ </td><td>60</td><td>8</td><td>0.5</td></tr><tr><td rowspan="5"> $e_{19}$ </td><td> $x_1$ </td><td>10</td><td>5</td><td>0.9</td><td rowspan="5"> $e_{20}$ </td><td> $x_1$ </td><td>70</td><td>7</td><td>0.3</td></tr><tr><td> $x_2$ </td><td>90</td><td>6</td><td>0.2</td><td> $x_2$ </td><td>20</td><td>3</td><td>0.3</td></tr><tr><td> $x_3$ </td><td>60</td><td>5</td><td>0.1</td><td> $x_3$ </td><td>40</td><td>6</td><td>0.4</td></tr><tr><td> $x_4$ </td><td>40</td><td>7</td><td>0.1</td><td> $x_4$ </td><td>60</td><td>7</td><td>0.2</td></tr><tr><td> $x_5$ </td><td>60</td><td>5</td><td>0.6</td><td> $x_5$ </td><td>30</td><td>4</td><td>0.1</td></tr></table>

Notes: the completely original individual decision information is shown in the supplementary files.

![](/api/attachments/SGQSZYCD/fulltext/images/180bf3c997fe74af101585515fe5dae3e522bf4bd03acc842c22100e218e8f56.jpg)  
Fig. 1. Simulation results based on objective adjustment coefficients.

(b) Determine whether a high-quality decision is required. MCLGEDM problems often require a relatively high-quality decision result. However, obtaining an appropriate result within a limited amount of time is often of greater priority than that of obtaining a highquality decision. Therefore, the predefined group consensus threshold should not be very large, or very close to 1. As the emergency decision often has the nature of time limitation and complexity, the value of GCI can generally not exceed 0.90.

(c) Avoid extreme situations. On the one hand, if the group consensus threshold is temporarily selected as $\overline { { G C I } } = 0 . 7 0$ , nothing more is <sup>¼</sup>required to modify the clusters' respective opinions because the initial group consensus level is larger than the selected threshold. That is, the threshold we selected may be a little small, and not well represent the existing difference among the DMs. On the other hand, if GCI is set as 0.90, the consensus reaching process may continue until after the 12th iteration and the overall opinion adjustment amount can reach 0.9882. It is noted that greater adjustment amount may indicate the possibility of opinion distortion.

Considering the three aspects presented above, it is reasonable to set GCI to fall within the interval [0.7386, 0.85], and the maximum number of iterations may belong to [0, 6]. It is worth noting that the simulation results shown in Fig. 1 can be used as a reference to determine these two parameters (i.e., GCI and CT), and the final values of them must be combined with the practical decision problem.

## 4.3. Processing minority opinions

Minority opinions are important in emergency decision making. To treat minority opinions properly, a novel method (labeled as M1) is proposed, which comprises three phases: identification, discussion, and modification.

Step 1 Detect and identify minority opinion(s).

A cluster to be identified as a minority subgroup should satisfy the following two conditions:

(a) the cluster (subgroup) has an opinion farthest from the group opinion, and

(b) the cluster includes only one or a few members.

Suppose that cluster $C ^ { k ^ { * } } ( k ^ { * } = 1 , 2 , . . . , K )$ has the largest difference from <sup>ð ¼ Þ</sup>the group. Letn be the threshold that is used to determine whether cluster $\bar { C } ^ { k ^ { * } }$ belongs to a minority opinion subgroup in view of the cluster's scale. Generally, n is set as ${ \overline { { n } } } = [ M / K ] .$ , where [M/K] is the bracket func-<sup>¼ ½</sup>tion of the value of M divided by K. If $n _ { k ^ { * } } \leq \overline { { n } } ,$ cluster $C ^ { k ^ { * } }$ can be regarded as a minority opinion subgroup that has the lowest cluster consensus level.

Step 2 Outline the rationality of the minority opinion and have a discussion among DMs.

Members in cluster $C ^ { k ^ { * } }$ elaborate the rationality of the cluster's opinion, and then all DMs conduct a discussion about this opinion. Every cluster should conduct an extensive and in-depth discussion with one another based on the principle that minority opinions must be considered fully and treated reasonably.

Step 3 Proper modification.

After a full discussion, if more than half of the remaining clusters regard the opinion of cluster $C ^ { k ^ { * } }$ as worth considering, the weight of cluster $C ^ { k ^ { * } }$ will be increased to enhance its effect on the group. The weight adjustment function should be the increasing function of the number of clusters supporting the opinion of cluster $C ^ { k ^ { * } }$ . The more clusters in favor of cluster $C ^ { k ^ { * } }$ , the more weight cluster $C ^ { k ^ { * } }$ will be assigned.

If we select a specific numerical adjustment function, the parameters involved in the function may be difficult to determine and may hinder the actual operation. Therefore, a weight substitution method is proposed. Specifically, the weight vector of the clusters is first ranked in ascending order, that is, $\lambda ^ { ' ( t ) } =$ $( \lambda _ { 1 } ^ { ' ( t ) } , \lambda _ { 2 } ^ { ' ( t ) } , . . . , \lambda _ { K } ^ { ' ( t ) } ) ^ { T } ,$ , where $\bigwedge _ { q } ^ { \cdot } ( t )  \left( q = 1 , 2 , . . . , K \right)$ is the q-th smallest weight. Then, calculate the difference between the number of clusters in favor of the minority opinion (denoted as $n _ { k ^ { * } } ^ { M 1 ( t ) } )$ and half of the number of all remaining clusters:

$$
n d _ {k ^ {*}} ^ {M 1 (t)} = \left\{ \begin{array}{l l} r o u n d \left(n _ {k ^ {*}} ^ {M 1 (t)} - \frac {K - 1}{2}\right), & K \text {   is   a   even   number } \\ n _ {k ^ {*}} ^ {M 1 (t)} - \frac {K - 1}{2}, & K \text {   is   an   odd   number } \end{array} \right.,\tag{12}
$$

where n $d _ { k ^ { * } } ^ { M 1 ( t ) }$ is the difference between $n _ { k ^ { * } } ^ { M 1 ( t ) }$ and $( K - 1 ) / 2$ $n _ { k ^ { * } } ^ { M 1 ( t ) }$ is the number of clusters in favor of the minority opinion in the t-th iteration, and round(⋅) is the usual round operation.

Definition 4. Suppose that the weight vector of the clusters is $\pmb { \lambda } ^ { ( t ) } = ( \lambda _ { 1 } ^ { ( t ) } , \lambda _ { 2 } ^ { ( t ) } , . . . , \lambda _ { K } ^ { ( t ) } ) ^ { T }$ and cluster $C ^ { k ^ { * } }$ holds the minority opinion in the t-th iteration. Order the weight vector as $\pmb { \lambda ^ { \prime } } ^ { ( \pmb { t } ) } = \mathbf { \dot { \sigma } } ( \lambda _ { 1 } ^ { \prime } ^ { ( \pmb { t } ) }$ $\lambda _ { 2 } ^ { \prime } { } ^ { ( t ) } , ~ . . . , \lambda _ { ~ K } ^ { \prime } { } ^ { ( t ) } ) ^ { T }$ . The weight of cluster $C ^ { k ^ { * } }$ is the $q ^ { * } { \boldsymbol { \cdot } } { \mathrm { t h } }$ smallest weight, this is, $\lambda _ { k ^ { * } } ^ { ( t ) } = \lambda _ { q ^ { * } } ^ { \prime ( t ) }$ . The weight substitution function is expressed by

$$
\lambda_ {k ^ {*}} ^ {M 1 (t)} = \min \left\{\max \left\{\lambda_ {k} ^ {(t)} \mid k = 1, 2,..., K \right\}, \lambda_ {q ^ {*} + n d _ {k ^ {*}} ^ {M 1 (t)}} ^ {\prime (t)} \right\}\tag{13}
$$

where $\lambda _ { k ^ { * } } ^ { M 1 ( t ) }$ Þ represents the adjusted weight. To avoid excessive adjustment or the importance of the initial weights being overlooked, the adjusted weight $\lambda _ { k ^ { * } } ^ { M 1 ( t ) }$ should not exceed the maximum cluster's weight in the last iteration. After the weight adjustment by using Eq. (13), the adjusted weight of cluster $C ^ { k ^ { * } }$ will become the $( q ^ { * } + n d _ { k ^ { * } } ^ { M 1 ( t ) } )$ -th smallest weight in the updated weight vector of the clusters $\mathrm { i f } \lambda _ { k ^ { * } } ^ { M 1 ( t ) }$ Þbmax $\{ \lambda _ { k } ^ { ( t ) } | k = 1 , 2 , . . . , K \} . \mathrm { I f } \lambda _ { k ^ { \ast } } ^ { M 1 ( t ) } = m a x \{ \lambda _ { k } ^ { ( t ) } | k = 1 , 2 , . . . , K \} , \lambda _ { k ^ { \ast } } ^ { M 1 ( t ) }$ is considered to be the $( K - 1 )$ -th smallest weight.

Example 1. A decision group comprises six clusters. The ordered weight vector of the clusters is set as $\hat { \mathbf { \Lambda } ^ { \prime ( t ) } } = ( 0 . 0 5 , 0 . 1 5 , 0 . 1 5 , 0 . 1 5 , 0 . 2 4 , 0 . 2 6 ) ^ { T }$ Suppose that cluster $C ^ { 2 }$ holds a minority opinion in the t-th iteration and its weight is $\lambda _ { 2 } ^ { ( t ) } = 0 . 1 5$ , which is the second smallest value. If the number of clusters supporting the minority opinion is $n _ { 2 } ^ { M 1 ( t ) } = 4 ,$ the deviation can be calculated as $\bar { n d } _ { 2 } ^ { M 1 ( t ) } = r o u n d \bar { ( 4 - ( 6 - 1 ) / 2 ) } = 2 .$ . Thus, the adjusted weight is $\lambda _ { 2 } ^ { M 1 ( t ) } = m i n \{ 0 . 2 6 , \lambda ^ { \prime } { } _ { 2 + } ^ { ( t ) } { } _ { 2 } \} \stackrel { . } { = } m i n \{ 0 . 2 6 , 0 . 1 5 \} =$ 0.15. Noticing that although the weight value of cluster $C ^ { 2 }$ does not change by using Eq. (13), it can be thought that its weight has jumped two weights to become the fourth smallest weight.

By normalizing the adjusted weights of the clusters, the new weight vector of clusters can be obtained. The consensus measure is then repeated. If no more than half of the clusters support cluster $C ^ { k ^ { * } }$ , this indicates that most DMs are skeptical about the rationality of the opinion proposed by cluster $C ^ { k ^ { * } }$ . In such a case, it is not necessary to improve its weight and the processing of minority opinions comes to an end.

## 4.4. Processing non-cooperative behaviors

An emergency involving many stakeholders often requires a highquality decision result. In the decision-making process, DMs who are reluctant to adjust their own opinions are referred to as non-cooperative members [28]. Attention should be paid to non-cooperative behaviors, and an appropriate response is necessary. A method (labeled as M2) featuring the dynamic adjustment of DMs' weights is presented here, which focuses on managing non-cooperative behaviors.

Step 1 Detect and identify non-cooperative cluster(s). Step 1 Detect and identify non-cooperative cluster(s).

The remaining clusters $C ^ { k ^ { \prime } } ( \bar { k } ^ { \prime } = 1 , 2 , . . . , K ; \ k ^ { \prime } \ne k ^ { * } )$ give their ex-<sup>ð ¼ Þ</sup>pected adjustment suggestions regarding the opinion of cluster $C ^ { k ^ { * } }$ , i.e., $\boldsymbol { \eta } _ { \boldsymbol { k } ^ { \prime } \boldsymbol { k } ^ { \prime } } ^ { ( t ) }$ , where $\eta _ { k ^ { ^ { \prime } } k ^ { ^ { \prime } } } ^ { ( t ) }$ is a crisp number and $0 \le \eta _ { k ^ { ^ { \prime } } k ^ { ^ { * } } } ^ { ( t ) } \le 1$ . The objective adjustment coefficient can be calculated as $\eta _ { k ^ { * } } ^ { O ( t ) }$ $\begin{array} { r l r } {  { = \frac { ( 1 - C I ( G ^ { k ^ { * } ( t ) } ) ) - ( 1 - \overline { { G C I } } ) } { 1 - C I ( G ^ { k ^ { * } ( t ) } ) } } } \end{array}$ . By comparing $\eta _ { k k ^ { * } } ^ { ( t ) } ~ ( { \ k } ^ { \prime } = 1 , 2 , . . . , K ; { \ k } ^ { \prime } \ne k ^ { * } )$ with $\eta _ { k ^ { * } } ^ { O ( t ) }$ , the expected adjustment suggestion interval can be obtained: $\overline { { \eta } } _ { k ^ { \circ } } ^ { ( t ) } = [ m i n \{ \eta _ { k ^ { ^ { \prime } } k ^ { ^ { \circ } } } ^ { ( t ) } , \eta _ { k ^ { ^ { \ast } } } ^ { ( 0 ( t ) } \}$ ; max $\{ \eta _ { k ^ { ^ { \prime } } k ^ { * } } ^ { ( t ) } , \eta _ { k ^ { * } } ^ { O ( t ) } \} _ { . }$ . The interval $\overline { { \eta } } _ { k ^ { \circ } } ^ { ( t ) }$ is used to determine whether cluster $C ^ { k ^ { * } }$ belongs to a non-cooperative subgroup. When $\eta _ { k ^ { * } } ^ { S ( t ) }$ belongs to the interval or is smaller than the left-end point of the interval, cluster $C ^ { k ^ { * } }$ can be regarded as a non-cooperative subgroup.

Step 2 Measure the non-cooperative degree.

The non-cooperative degree is introduced to measure the degree to which a cluster is unwilling to modify its opinion to reach an agreement. The possibility degree is often used to determine the order of two interval numbers, which can be applied to measure the non-cooperative degree.

Definition 5. (Nakahara et al. [35]). Let $\bar { a } = [ a ^ { L } , a ^ { U } ]$ and $\overline { { { b } } } = [ b ^ { L } , \ b ^ { U } ]$ be the two interval numbers, and note that $l ( \bar { a } ) \dot { = } a ^ { U } - a ^ { L } , l ( \overline { { b } } ) \dot { = } b ^ { U } - \acute { b } ^ { L }$ Thus, the possibility degree of $\overline { { a } } \geq \overline { { b } }$ is defined as

$$
p (\bar {a} \geq \bar {b}) = \min \left\{\max \left\{\frac {a ^ {U} - b ^ {L}}{l (\bar {a}) + l (\bar {b})}, 0 \right\}, 1 \right\}.\tag{14}
$$

Definition 6. Suppose that the subjective adjustment coefficient provided by cluster $C ^ { k ^ { * } }$ is $\eta _ { k ^ { * } } ^ { S ( t ) }$ and the expected adjustment suggestion interval is $\overline { { \eta } } _ { k ^ { \circ } } ^ { ( t ) }$ . Regard $\eta _ { k ^ { * } } ^ { S ( t ) }$ as an interval number, i.e $\mathbf { \nabla } _ { \cdot } \overline { { \eta } } _ { k ^ { \ast } } ^ { S ( t ) } = \left[ \eta _ { k ^ { \ast } } ^ { S ( t ) L } , \eta _ { k ^ { \ast } } ^ { S ( t ) U } \right]$ where $\eta _ { k ^ { * } } ^ { S ( t ) L } = \eta _ { k ^ { * } } ^ { S ( t ) U } = \eta _ { k ^ { * } } ^ { S ( t ) }$ . The non-cooperative degree of modifying its opinion for cluster $C ^ { k ^ { * } }$ can be defined as

$$
\tau^ {(t)} \left(C ^ {k ^ {*}}\right) = 1 - p \left(\overline {{\eta}} _ {k ^ {*}} ^ {S (t)} \geq \overline {{\eta}} _ {k ^ {\circ}} ^ {(t)}\right).\tag{15}
$$

Based on the properties of the possibility degree presented in $[ 3 6 ] ,$ it is obvious that $\tau ^ { ( t ) } ( \hat { C } ^ { k ^ { * } } ) \in [ 0 ,$ ; 1 . For instance, if $\bar { p } ( \overline { { \eta } } _ { k ^ { * } } ^ { S ( t ) } \geq \overline { { \eta } } _ { k ^ { \circ } } ^ { ( t ) } ) = 0 . 3 \dot { 5 }$ , then <sup>ð Þ ½ </sup>the non-cooperative degree of cluster $C ^ { k ^ { * } } { \mathrm { ~ i s ~ } } 1 - 0 . 3 5 { \overset { \underset {  } {  } } { = } } 0 . 6 5$ Step 3 Proper modification.

Consider three different situations of non-cooperative behaviors.

(a) $\boldsymbol { \mathrm { I f } } \tau ^ { ( t ) } ( \boldsymbol { C } ^ { k ^ { * } } ) = \boldsymbol { 0 } ,$ , it indicates that cluster $C ^ { k ^ { * } }$ is a completely cooper-<sup>ð Þ ¼</sup>ative subgroup. Therefore, nothing more should be done regarding its weight, and a comprehensive adjustment coefficient can be used to modify its opinion.

(b) $\mathrm { I f } \tau ^ { ( t ) } ( C ^ { k ^ { * } } ) = 1$ , it means that cluster $C ^ { k ^ { * } }$ demonstrates a very high <sup>ð Þ ¼</sup>degree of non-cooperative behavior. To improve the speed of decision making and obtain an appropriate result in a short period of time, the member(s) can be advised to exit the decision process.

(c) If $0 < \tau ^ { ( t ) } ( C ^ { k ^ { * } } ) < 1$ , cluster $C ^ { k ^ { * } }$ is regarded as a partly non-<sup>ð Þ</sup>cooperative subgroup. Therefore, its weight can be properly adjusted to reduce its influence on the group opinion. The modified function should be a decreasing function of non-cooperative degree. The common weight adjustment functions are shown in Fig. 2. Different functions represent different strategies for weight adjustment. Curve 1 is a linear function, which means that, regardless of the degree of non-cooperation, the function slope is fixed. Curve 2 is a downward convex decreasing function. In this case, the DMs pay more attention to the fact that noncooperative behaviors exist, instead of the degree of noncooperation. When the non-cooperative degree is very close to 1, the DMs are not sensitive to any change in the noncooperative degree. Curve 3 is a downward concave decreasing function. The DMs focus more on how much the noncooperative cluster is not willing to modify its own opinion. If the non-cooperative degree is relatively small, the weight adjustment should also be small.

The three functions presented in Fig. 2 characterize the basic relationship between the weight adjustment and the non-cooperative degree. However, the parameters involved in the three functions are difficult to determine, which may bring great uncertainty and challenges to the actual operation. Therefore, a non-cooperative degree-based staircase weight adjustment function is developed. The interval [0, 1] that the non-cooperative degree belongs to can be divided into six smaller parts, each of which corresponds to a weight adjustment coefficient as shown in Fig. 3. The weight adjustment function is

![](/api/attachments/SGQSZYCD/fulltext/images/735e1b20a2795a46ef7685bc9f246738c6df2885576257bbc544412254e01b06.jpg)  
Fig. 2. Basic weight adjustment functions of the non-cooperative cluster.

$$
\lambda_ {k ^ {*}} ^ {M 2 (t)} = \left\{ \begin{array}{c} \lambda_ {k ^ {*}} ^ {(t)}, \tau^ {(t)} \Big (C ^ {k ^ {*}} \Big) \in [ 0. 0, 0. 2) \\ 0. 8 \times \lambda_ {k ^ {*}} ^ {(t)}, \tau^ {(t)} \Big (C ^ {k ^ {*}} \Big) \in [ 0. 2, 0. 4) \\ 0. 6 \times \lambda_ {k ^ {*}} ^ {(t)}, \tau^ {(t)} \Big (C ^ {k ^ {*}} \Big) \in [ 0. 4, 0. 6) \\ 0. 4 \times \lambda_ {k ^ {*}} ^ {(t)}, \tau^ {(t)} \Big (C ^ {k ^ {*}} \Big) \in [ 0. 6, 0. 8) \\ 0. 2 \times \lambda_ {k ^ {*}} ^ {(t)}, \tau^ {(t)} \Big (C ^ {k ^ {*}} \Big) \in [ 0. 8, 1. 0) \\ 0, \tau^ {(t)} \Big (C ^ {k ^ {*}} \Big) = 1. 0 \end{array} , \right.\tag{16}
$$

![](/api/attachments/SGQSZYCD/fulltext/images/101aa58aaf0f924f81f4660333bdfdf358ddd1008dd11c7d3deab7750254455f.jpg)  
Fig. 3. Proposed weight adjustment function of the non-cooperative cluster.

where $\lambda _ { k ^ { * } } ^ { ( t ) }$ is the weight of cluster $C ^ { k ^ { * } }$ after t rounds of iteration, and $\lambda _ { k ^ { * } } ^ { M 2 ( t ) }$ represents the adjusted weight by applying M2. For example, when the non-cooperative degree is $\tau ^ { ( t ) } ( C ^ { k ^ { * } } ) = 0 .$ :35 belonging to the interval [0.2, 0.4), the adjusted weight is $\lambda _ { k ^ { * } } ^ { M 2 ( t ) } = 0 . 8 \times \lambda _ { k ^ { * } } ^ { ( t ) }$ , where the number 0.8 is the weight adjustment coefficient. Then a comprehensive adjustment coefficient can be used to modify the non-cooperative cluster's opinion. By normalizing the adjusted clusters' weights, the new weight vector of clusters can be obtained.

## 4.5. Algorithm of the proposed consensus model for MCLGEDM problems

The basic idea of the proposed consensus model in this paper is to obtain a relatively satisfactory decision result with a proper consensus level among DMs within a short period of time. To facilitate analysis and extension thereafter, an algorithm for the proposed consensus model is summarized as follows (see Fig. 4).

Input: The initial standardized individual decision matrices $R ^ { i ( 0 ) } ( i =$ $1 , 2 , . . . , M )$ and the weight vector of the criteria .

Output: The number of iterations t\*, the final clusters' decision matrices $G ^ { k ( t ^ { * } ) }$ <sub>Þ</sub>, and the final group decision matrix $R ^ { c ( t ^ { * } ) }$

Step 1 Cluster the initial normalized individual decision matrices.

Divide the large group into $K ( 1 \leq K \leq M )$ clusters, and calculate the initial weight vector of the clusters: $\dot { \mathsf { \Lambda } } ^ { ( 0 ) } = ( \lambda _ { 1 } ^ { ( 0 ) } , \lambda _ { 2 } ^ { ( 0 ) } , . . . , \lambda _ { K } ^ { ( 0 ) } ) ^ { T } \mathrm { . }$ The initial clusters' decision matrices $G ^ { k ( 0 ) } = ( g _ { l j } ^ { k ( 0 ) } ) _ { P \times N } ( k =$ $1 , 2 , . . . , K )$ can then be obtained by using the WA operator. Let $t = 0 .$

Step 2 Calculate the temporal group decision matrix.

Aggregate the clusters' decision matrices into temporal group decision matrix $R ^ { c ( t ) } = ( r _ { l j } ^ { c ( t ) } ) _ { P } \times N$ by applying Eq. (1), where $r _ { l j } ^ { c ( t ) } = W A ( g _ { l j } ^ { 1 ( t ) } , g _ { l j } ^ { 2 ( t ) } , . . . , g _ { l j } ^ { \tilde { K } ( t ) } ) .$

Step 3 Simulate the consensus reaching process and determine the required parameters (the minimum group consensus threshold GCI and the maximum number of iterations CT).

The simulation results can be used as a reference of the relationship between the group consensus level and the iterative round as well as the opinion adjustment amount. By combining the reference and the real decision problem, DMs can determine the values of GCI and CT. It should be noted that this step is omitted in the following iteration once GCI and CT are fixed.

Step 4 Consensus measure.

Compute the cluster consensus level between each cluster's decision matrix and group decision matrix, i.e., $C I ( G ^ { k ( t ) } ) ( k = 1$ $2 , . . . . , K )$ , by using Eq. (8). The group consensus level $G C I ^ { ( t ) }$ can then be obtained via $\operatorname { E q . } \left( 9 \right)$ . If GCI <sup>t</sup> ≥GCI, proceed to Step 6; otherwise, proceed to the next step.

Step 5 Consensus reaching process.

(a) Detect and manage minority opinion(s).

M1 is used to identify which cluster belongs to the minority opinion subgroup and to determine whether the minority opinion cluster's weight requires modification. If necessary, modify its weight properly, let $t = t + 1$ , and then return to Step 2; otherwise, proceed to Step $5 ( \mathrm { b } )$

(b) Identify and deal with non-cooperative behavior(s).

M2 is used to determine whether a non-cooperative cluster exists. If so, use M2 to properly modify its weight; otherwise, nothing more needs to be done regarding the weight. Then, calculate the comprehensive adjustment coefficient and modify the opin ion of cluster $C ^ { k ^ { * } }$ by applying Eq. (10). After that, let $t = t + 1$ and return to Step 2.

Step 6 Output related decision information.

Let $t ^ { * } = t .$ Output the final clusters' decision matrices $G ^ { k ( t ^ { * } ) }$ $( k = 1 , 2 , . . . , K )$ and the final group decision matrix $R ^ { c ( t ^ { * } ) }$

![](/api/attachments/SGQSZYCD/fulltext/images/38c35427918c3197cc27846bd2d53859605315673f5582272a823db67b37434d.jpg)  
Fig. 4. Consensus process for MCLGEDM problems

## 5. An illustrative example

An actual MCLGEDM problem is described as follows. A flooding accident occurred in Xiaohebian coal mine in the city of Xuanwei in Yunnan Province at 4:30 pm on September 23, 2014. A total of seven miners escaped from the well and eight were trapped underground at the accident site. The emergency command department conducted a preliminary analysis of the incident and promptly invited 20 DMs $e _ { i } ( i = 1$ $2 , . . . , 2 0 )$ , including 5 emergency officials (marked as $e _ { 1 } , e _ { 2 } , e _ { 3 } , e _ { 4 } ,$ , and $e _ { 5 } ) _ { \cdot }$ 5 armed police (marked as $e _ { 6 } , e _ { 7 } , e _ { 8 } , e _ { 9 } ,$ and $e _ { 1 0 } )$ , 5 mine representatives (marked as $e _ { 1 1 } , e _ { 1 2 } , e _ { 1 3 } , e _ { 1 4 } ,$ and $e _ { 1 5 } )$ , and 5 geological experts (marked as $e _ { 1 6 } , e _ { 1 7 } , e _ { 1 8 } , e _ { 1 9 } ,$ and $e _ { 2 0 } )$ , to select the best rescue alternative within a short period of time. After a pre-evaluation, the following five alternatives expressed as $X = \{ x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } , x _ { 5 } \}$ were put forward for further discussion and evaluation: (a) using partial blasting and arranging mining machines (x ), (b) arranging the mechanically driven pumps to drain the water $( x _ { 2 } ) , ( \mathsf C )$ arranging partial blasting and clearing room for fire fighters to enter the mine (x ), (d) organizing armed police and fire fighters to clear obstacles and take mine cars down into the mine $\left( x _ { 4 } \right)$

and (e) arranging excavators and deep-hole drilling machines $\left( x _ { 5 } \right)$ We consider 3 criteria for each alternative $f _ { j } ( j = 1 , 2 , 3 ) \colon$ : personnel security rate f (scale: 0–100; unit: %; type: benefit criterion), required rescue time $f _ { 2 }$ (scale: 0–10; unit: day; type: cost criterion), and rescue cos $f _ { 3 }$ (scale: 0–1; type: cost criterion). The weight vector of the criteria is predefined as $\pmb { \omega } = ( 0 . 5 , 0 . 3 , 0 . 2 ) ^ { T }$ . Let the weight coefficient be $\varepsilon = 0 . 5 ,$ The original individual decision matrices are listed in Table 1. As the DMs involved are all experts (i.e., belonging to the second category presented in Section 2.1), each DM's opinion should be seriously considered. Suppose that no conflict of interest exists among the DMs. To obtain the best alternative(s), the following steps are followed.

## Step 1 Cluster the initial normalized individual decision matrices.

To save space, the normalized individual decision matrices are omitted. By using the clustering method proposed by Xu and Chen [32,33], the large group can be divided into several smaller clusters. Table 2 shows that the clustering results when the clustering threshold is set as $\gamma = 0 . 6 3$ , and the initial decision group can be divided into six clusters.

Clustering results with the threshold γ = 0.63.

<table><tr><td> $C^k$ </td><td> $n_k$ </td><td> $e_i$ </td><td> $λ_k^{(0)}$ </td><td> $G^{k(0)}$ </td><td></td><td></td><td> $C^k$ </td><td> $n_k$ </td><td> $e_i$ </td><td> $λ_k^{(0)}$ </td><td> $G^{k(0)}$ </td><td></td><td></td></tr><tr><td rowspan="5"> $C^1$ </td><td rowspan="5">1</td><td rowspan="5"> $e_1$ </td><td rowspan="5">0.0132</td><td>0</td><td>0.75</td><td>0</td><td rowspan="5"> $C^2$ </td><td rowspan="5">4</td><td> $e_2,e_3,$ </td><td rowspan="5">0.2105</td><td>0.75</td><td>0.55</td><td>0.9286</td></tr><tr><td>0.25</td><td>0.875</td><td>0.5</td><td rowspan="4"> $e_4,e_5$ </td><td>0.6</td><td>0.3750</td><td>0</td></tr><tr><td>0.5</td><td>0.125</td><td>0.3333</td><td>0.5875</td><td>1</td><td>0.1833</td></tr><tr><td>0.75</td><td>1</td><td>0.8333</td><td>0.1250</td><td>0.7000</td><td>0.2691</td></tr><tr><td>1</td><td>0</td><td>0.5</td><td>0.3723</td><td>0.0625</td><td>0.8583</td></tr><tr><td rowspan="5"> $C^3$ </td><td rowspan="5">5</td><td rowspan="5"> $e_6,e_9,$  $e_{12},e_{13},e_{17}$ </td><td rowspan="5">0.3289</td><td>0.5417</td><td>0.3143</td><td>0.7000</td><td rowspan="5"> $C^4$ </td><td rowspan="5">4</td><td> $e_7,e_8,$ </td><td rowspan="5">0.2105</td><td>0</td><td>0.9063</td><td>0.7500</td></tr><tr><td>0.3000</td><td>0.3857</td><td>0.6679</td><td rowspan="4"> $e_{10},e_{19}$ </td><td>0.7500</td><td>0.5938</td><td>0.4687</td></tr><tr><td>0.4833</td><td>0.2857</td><td>0.5000</td><td>0.3229</td><td>0.5313</td><td>1</td></tr><tr><td>0.3167</td><td>0.6238</td><td>0.3667</td><td>0.8438</td><td>0</td><td>0.2500</td></tr><tr><td>0.6750</td><td>0.9500</td><td>0.2893</td><td>0.9063</td><td>1</td><td>0.3437</td></tr><tr><td rowspan="5"> $C^5$ </td><td rowspan="5">3</td><td rowspan="5"> $e_{11},e_{15},e_{20}$ </td><td rowspan="5">0.1184</td><td>0.9444</td><td>0</td><td>0.1111</td><td rowspan="5"> $C^6$ </td><td rowspan="5">3</td><td rowspan="5"> $e_{14},e_{16},e_{18}$ </td><td rowspan="5">0.1184</td><td>1</td><td>1</td><td>1</td></tr><tr><td>0.5833</td><td>0.7143</td><td>0.4444</td><td>0.4</td><td>0</td><td>1</td></tr><tr><td>0.4111</td><td>0.4643</td><td>0.1111</td><td>0</td><td>0.75</td><td>0.3333</td></tr><tr><td>0.7389</td><td>0.6667</td><td>0.6389</td><td>0.6</td><td>0.5</td><td>1</td></tr><tr><td>0.0667</td><td>0.7738</td><td>0.6667</td><td>0.6</td><td>0</td><td>0</td></tr></table>

Notes $n _ { k }$ denotes the pumber of DMs in cluster Ck, and $\lambda _ { k } ^ { ( 0 ) }$ is the initial weight of cluster Ck

Step 2 Calculate the temporal group decision matrix. Aggregate the clusters' decision matrices into the temporal group decision matrix $R ^ { c ( 0 ) } = ( r _ { l j } ^ { c ( 0 ) } ) _ { 5 \times 3 }$ by using Eq. (1):

$$
R ^ {c (0)} = \left[ \begin{array}{c c c} 0. 5 6 6 3 & 0. 5 3 8 2 & 0. 7 1 5 1 \\ 0. 5 0 2 6 & 0. 4 2 6 9 & 0. 4 9 6 0 \\ 0. 4 0 5 9 & 0. 5 6 1 7 & 0. 4 7 0 6 \\ 0. 4 7 6 5 & 0. 5 0 3 9 & 0. 4 3 4 9 \\ 0. 5 8 3 3 & 0. 6 2 7 7 & 0. 4 3 3 7 \end{array} \right].
$$

Step 3 Simulate the consensus reaching process and determine the two parameters.

The simulation results of the consensus reaching process are displayed in detail in Fig. 1. Based on the analysis in Section 4.2, DMs reach an agreement that the minimum group consensus threshold is predefined as $\overline { { G C I } } = 0 . 8 0$ before making <sup>¼</sup>a decision and the maximum number of iterations is $C T = 5$ because of time limitation.

Step 4 Consensus measure.

Compute the cluster consensus levels, that is, $C I ( G ^ { 1 ( 0 ) } ) = 0 . 6 5 7 0$ $C I ( G ^ { \hat { 2 } ( 0 ) } ) = 0 . 7 4 1 6 , C I ( G ^ { 3 ( 0 ) } ) = 0 . 8 6 8 8 , C I ( \dot { G } ^ { 4 ( 0 ) } ) = 0 . 7 4 0 3$ $C I ( G ^ { 5 ( 0 ) } ) = 0 . 7 3 8 2$ , and $C I ( G ^ { 6 ( 0 ) } ) = 0 . 6 8 5 6$ . The initial group consensus level can be calculated as $G C I ^ { ( 0 ) } = 0 . 7 3 8 6$ . Because G $C I ^ { ( 0 ) } { < } \overline { { G C I } } = 0 . 8 0$ , the consensus process should be applied to <sup>¼</sup>change some opinions.

Step 5 Consensus reaching process.

(i) First consensus iteration

M1 is first used to detect and manage minority opinions. Based on the clustering results in Table 2, let $\overline { { n } } = [ 2 0 / 6 ] = 3$ be the threshold value used to determine whether a cluster is regarded as a minority opinion subgroup. As $C I ( G ^ { 1 ( 0 ) } ) = m i n \{ C I ( G ^ { k ( 0 ) } ) | k = 1 , 2 , 3 ,$ $4 , 5 , 6 \}$ and $n _ { 1 } = 1 { < } \overline { { { n } } } = 3 ,$ , cluster $C ^ { 1 }$ can be regarded as a minority <sup>¼ ¼</sup>opinion subgroup. Then, cluster $C ^ { 1 }$ should illustrate the rationality of its opinion in detail, and a thorough discussion is conducted among all DMs. After some discussion and compromise, all the remaining clusters hold that the opinion of cluster $C ^ { 1 }$ should be taken into account to a greater degree, that is, $n _ { 1 } ^ { M 1 ( 0 ) } = 5 \qquad $ . To ensure that the minority opinion is better reflected in the group opinion, use $\operatorname { E q . }$ (13) to change the weight of cluster $C ^ { 1 }$ . The ordered weight vector of the clusters is $\begin{array} { r } { \bar { \mathsf { A } } ^ { \prime ( 0 ) } = ( 0 . 0 1 3 2 , } \end{array}$ 0.1184, 0.1184, 0.2105, 0.2105, 0.3289)<sup>T</sup>. The weight of cluster $C ^ { 1 }$ is the smallest weight. The deviation between $\overset { - } { n _ { k } ^ { M 1 ( 0 ) } }$ and half of the number of the remaining clusters is $n d _ { 1 } ^ { M 1 ( 0 ) } = 3$ based on Eq. (12). Therefore, the adjusted weight of cluster $C ^ { 1 } \mathrm { i } s \lambda _ { 1 } ^ { M 1 ( 0 ) } =$ mi $\imath \{ m a x \{ \lambda _ { k } ^ { ( 0 ) } | k = 1 , 2 , 3 , 4 , 5 , 6 \} , \lambda ^ { \prime } _ { 1 + 3 } ^ { ( 0 ) } \} = \{ 0 . 3 2 8 9 , 0 . 2 1 0 5 \} =$ 0.2105. After normalization, the new weight vector of the clusters can be obtained as $\pmb { \lambda } ^ { ( 1 ) } = ( 0 . 1 7 5 8 , 0 . 1 7 5 8 , 0 . 2 7 4 7 , 0 . 1 7 5 8 , 0 . 0 9 8 9 ,$ 0.0989)<sup>T</sup>. It can be seen that the weight of cluster $C ^ { 1 }$ has jumped three weights to become the fourth smallest weight.

The WA operator is then adopted to calculate the updated temporal group decision matrix. Continuing consensus measure, the new cluster consensus levels are $C I ( G ^ { \overleftarrow { 1 } ( 1 ) } ) = 0 . 7 1 3 5 , C I ( G ^ { 2 ( 1 ) } ) =$ 0.7179, $C I ( G ^ { 3 ( 1 ) } ) = 0 . 8 5 4 9$ $C I ( G ^ { 4 ( 1 ) } ) = 0 . 7 3 0 0 , C I ( G ^ { 5 ( 1 ) } ) =$ 0.7477, and $C I ( G ^ { 6 ( 1 ) } ) = 0 . 6 7 3 2$ . The group consensus level is $G C$ $I ^ { ( 1 ) } = 0 . 7 3 9 5 { < } \overline { { G C I } }$ . Thus, the consensus reaching process <sup>¼</sup>continues.

(ii) Second consensus iteration

M1 is then used to identify and deal with minority opinions. As $C I ( G ^ { 6 ( 1 ) } ) = m i n \{ C I ( G ^ { k ( 1 ) } ) | k = 1 , 2 , 3 , 4 , 5 , 6 \}$ and $n _ { 6 } = 3 { \le } \overline { { n } } ,$ , cluster $C ^ { 6 } \thinspace { \mathrm { c a n } }$ <sup>¼</sup>be regarded as a minority opinion subgroup. Only two remaining clusters still support the opinion of cluster $C ^ { 6 }$ , so nothing more will be done to the clusters' weights.

M2 is used to manage non-cooperative behaviors. Based on the discussion results and the current group consensus level, the remaining clusters provide their expected adjustment suggestions on the opinion of cluster $C ^ { 6 } ~ ( \mathrm { i . e . , } ~ \eta _ { 1 6 } ^ { ( 1 ) } = 0 . 5 0 , \eta _ { 2 6 } ^ { ( 1 ) } = 0 . 6 5$ $\eta _ { 3 6 } ^ { ( 1 ) } = \dot { 0 . 3 5 } , \eta _ { 4 6 } ^ { ( 1 ) } = 0 . 7 0 ,$ , and $\eta _ { 5 6 } ^ { ( 1 ) } = 0 . 4 5 )$ . Meanwhile, the objective adjustment coefficient can be calculated as $\eta _ { 6 } ^ { O ( 1 ) } =$ 0.3880. By comparing the values in the adjustment suggestion set $\{ \eta _ { k ^ { ^ { \prime } } 6 } ^ { ( 1 ) } | k ^ { ^ { \prime } } = 1 , 2 , 3 , 4 , 5 \}$ with $\eta _ { 6 } ^ { O ( 1 ) }$ , the expected adjustment suggestion interval can be obtained: $\overline { { { \eta } } } _ { 6 } ^ { ( 1 ) } = [ m i n \{ \eta _ { k ^ { \prime } 6 } ^ { ( 1 ) } , \eta _ { 6 } ^ { 0 ( 1 ) } \} $ ; max $\{ \eta _ { k 6 } ^ { ( 1 ) } , \eta _ { 6 } ^ { O ( 1 ) } \} ] = [ 0 . 3 5 , 0 . 7 0 ]$ . The members in cluster $C ^ { 6 }$ then determine the subjective adjustment coefficient as $\eta _ { 6 } ^ { S ( 1 ) } = 0 . 1 0$ As $\tau ^ { ( 1 ) } ( C ^ { 6 } ) = 1$ , cluster ${ \bar { C } } ^ { 6 }$ is regarded as a completely noncooperative subgroup. To obtain an appropriate result within a short period of time, the members in cluster $C ^ { 6 }$ can be advised to exit the decision-making process. The weight vector of the clusters is updated as $\pmb { \Lambda } ^ { ( 2 ) } = ( 0 . 1 9 5 1$ 0.1951, 0.3049, 0.1951, 0.1098)<sup>T</sup>. The updated cluster consensus levels are now $C I ( G ^ { 1 ( 2 ) } ) ~ = ~ 0 . 7 1 7 8$ $C I ( G ^ { 2 ( 2 ) } ) ~ = ~ 0 . 7 1 7 8$ $C I ( G ^ { 3 ( 2 ) } ) = 0 . 8 4 7 2 , C I ( G ^ { 4 ( 2 ) } ) = 0 . 7 3 0 6 ,$ , and $C I ( G ^ { 5 ( 2 ) } ) = 0 . 7 8 2 2$ The group consensus level is calculated as $G C I ^ { ( 2 ) } = 0 . 7 5 9 1 { < } \overline { { G C I } } ;$ <sup>¼</sup>thus, the consensus reaching processing should continue.

(iii) Third consensus iteration

$\mathtt { A s } C I ( G ^ { 1 ( 2 ) } ) = C I ( G ^ { 2 ( 2 ) } ) = m i n \{ C I ( G ^ { k ( 2 ) } ) | k = 1 , 2 , 3 , 4 , 5 \}$ , it is time to turn to clusters $C ^ { 1 }$ and $C ^ { 2 } .$ . However, cluster $C ^ { 1 }$ was dealt with in the first iteration, therefore it is a priority to manage the opinion of cluster $C ^ { 2 } .$ . Because $n _ { 2 } = 4 { > } \overline { { n } }$ , cluster $C ^ { 2 }$ <sup>¼</sup>need not be regarded as a minority opinion subgroup.

M2 is used to manage non-cooperative behaviors. Based on the discussion results and current group consensus level, the remaining clusters provide their expected adjustment suggestions on the opinion of cluster $C ^ { 2 } { : } \eta _ { 1 2 } ^ { ( 2 ) } \overset { ^ { . } } { = } 0 . 6 5 , \eta _ { 3 2 } ^ { ( \bar { 2 } ) } = 0 . 6 0 , \eta _ { 4 2 } ^ { ( \overline { { 2 } } ) ^ { - } } = 0 . 7 5$ and $\eta _ { 5 2 } ^ { ( 2 ) } = 0 . 5 0$ . Meanwhile, the objective adjustment coefficient can be calculated as $\eta _ { 2 } ^ { O ( 2 ) } = 0 . 2 9 3 1$ . By comparing the values in the adjustment suggestion set $\{ \eta _ { k ^ { ^ { \prime } } 2 } ^ { ( 2 ) } | k ^ { \prime } = 1 , 3 , 4 , 5 \}$ with $\eta _ { 2 } ^ { O ( 2 ) }$ the expected adjustment suggestion interval can be obtained: $\overline { { { \eta } } } _ { 2 ^ { \circ } } ^ { ( 2 ) } = [ m i n \{ \eta _ { k ^ { ^ { \prime } } 2 } ^ { ( 2 ) } , \eta _ { 2 } ^ { 0 ( 2 ) } \}$ ; max $\{ \eta _ { _ { k ^ { \prime } 2 } } ^ { ( 2 ) } , \eta _ { 2 } ^ { O ( 2 ) } \} ] = [ 0 . 2 9 7 0 , 0 . 7 5 ]$ . The members in cluster $C ^ { 2 }$ then determine the subjective adjustment coefficient as $\eta _ { 2 } ^ { S ( 2 ) } = 0 . 8 0 . \mathsf { A s } \tau ^ { ( 2 ) } ( C ^ { 2 } ) = 0 ,$ , cluster $C ^ { 2 }$ is regarded as a completely cooperative subgroup. Because $\eta _ { 2 } ^ { S ( 2 ) } > \eta _ { 2 } ^ { O ( 2 ) }$ <sup>)</sup>, the comprehensive adjustment coefficient is $\eta _ { 2 } ^ { ( 2 ) } = \stackrel { \cdot } { 0 . 8 0 }$ . The comprehensive adjustment coefficient is used to modify the opinion of cluster $C ^ { 2 } .$

The new cluster consensus levels are $C I ( G ^ { 1 ( 3 ) } ) ~ = ~ 0 . 7 3 3 5$ $C I ( G ^ { 2 ( 3 ) } ) = 0 . 8 9 9 5 , C I ( G ^ { 3 ( 3 ) } ) = 0 . 8 5 2 6 , C I ( G ^ { 4 ( 3 ) } ) = 0 . 7 3 4 6 ,$ , and $C I ( G ^ { 5 ( 3 ) } ) = 0 . 7 8 4 3$ . The group consensus level is $G C I ^ { ( 3 ) } = 0 . 8 0 0 9 >$ <sup>¼</sup>GCI. After three iterations (including two weight adjustments and one opinion adjustment), the DMs reach an agreement that the final group consensus level satisfies the predefined requirement.

Step 6 Output related decision information.

Let $t ^ { * } = 3$ . The final group decision matrix is obtained as

$$
R ^ {c (3)} = \left[ \begin{array}{c c c} 0. 4 5 6 1 & 0. 5 2 2 6 & 0. 5 0 5 5 \\ 0. 5 0 4 5 & 0. 6 5 4 4 & 0. 5 5 4 1 \\ 0. 4 8 9 5 & 0. 4 2 2 9 & 0. 5 1 4 8 \\ 0. 6 4 6 5 & 0. 6 4 4 4 & 0. 5 3 6 4 \\ 0. 7 0 8 8 & 0. 7 3 9 3 & 0. 5 0 2 3 \end{array} \right].
$$

Calculating the overall evaluation values of $x _ { l } ( l = 1 , 2 , 3 , 4 , 5 )$ by using $\operatorname { E q . } \ ( 2 )$ , we obtain $E V ( x _ { 1 } ) = 0 . 4 8 5 9 , E V ( x _ { 2 } ) = 0 . 5 5 9 1$ $E V ( x _ { 3 } ) = 0 . 4 7 4 6 , E V ( x _ { 4 } ) = 0 . 6 2 3 9 ,$ and $E V ( x _ { 5 } ) = 0 . 6 7 6 6$ . The alternatives can be sorted according to the evaluation values: $x _ { 5 } \succ x _ { 4 } \succ x _ { 2 } \succ x _ { 1 } \succ x _ { 3 } .$ Thus, the best alternative is $x _ { 5 } ;$ the plan to arrange excavators and deep-hole drilling machines should be selected for the mining rescue.

## 6. Discussion

## 6.1. Advantage of comprehensive adjustment coefficient

To better reflect the advantages of the comprehensive adjustment coefficient in managing the opinion differences, the consensus reaching processes applied in this section do not take into account the processing of minority opinions and non-cooperative behaviors. The consensus consequences obtained by different types of adjustment coefficients are showed in Table 3.

It is clear that the group consensus level is constantly improved as the number of iterations increases, whichever type of adjustment coefficient we select. The differences lie in the number of iterations and the opinion adjustment amount. Because of the subjectivity and bounded rationality of DMs, a large fluctuation may appear in the adjustment coefficients provided by DMs if subjective adjustment coefficient is selected. As shown in Table 3, some DMs stick to their own opinions so strongly that the group consensus level cannot meet the requirement of the predefined consensus threshold until after the eighth round of the consensus process.

If objective adjustment coefficient is used, the arbitrariness and uncertainty of subjective revision can be reduced. However, the DMs own adjustment coefficients will not be taken into account. It may not be appropriate for MCLGEDM problems that are usually required to produce high-quality results to fully consider each DM's opinion.

If comprehensive adjustment coefficient is adopted, the limitations of the two types of adjustment coefficients presented above can be overcome to a certain extent. Specifically, when the subjective adjustment coefficient is lower than the objective one, and even close to 0 (i.e., there exists a cluster that sticks very strongly to its opinion), then the comprehensive adjustment coefficient can be calculated based on the rules presented in Section 4.1.3. By applying the comprehensive adjustment coefficient, the non-cooperative degree can be reduced and the proposed subjective adjustment coefficients can be taken into account to some extent.

6.2. Function of the proposed consensus model in dealing with minority opinions and non-cooperative behaviors

Thanks to stick to the principle that minority opinions should be fully considered, the weight of cluster $C ^ { 1 }$ increased from 0.0132 to 0.1951 after the third iteration, which means that the opinion of cluster $C ^ { 1 }$ has received a greater degree of recognition.

According to the original group decision matrix, the initial alternative ranking is $x _ { 1 } \succ x _ { 5 } \succ x _ { 2 } \succ x _ { 4 } \succ x _ { 3 } .$ . Compared with the final alternative ranking in the example presented in Section 5, there is a big difference in the order of the alternatives. Meanwhile, based on the initial opinion provided by cluster $C ^ { 1 }$ , the alternative ranking is $x _ { 4 } \succ x _ { 5 } \succ x _ { 2 } \succ x _ { 3 } \succ x _ { 1 } ,$ , which is similar with the ranking result presented in Section 5. That is, the opinion of cluster $C ^ { 1 }$ receives more attention, which is reflected in the final decision result after utilizing M1 to appropriately manage minority opinions.

In the second iteration, the opinion of cluster $C ^ { 6 }$ had the biggest difference from the group opinion and cluster $C ^ { 6 }$ was very reluctant to modify its opinion to reach an agreement. Therefore, the members of cluster $C ^ { 6 }$ were advised to exit the decision process to ensure the quality and timeliness of the decision. Furthermore, the group consensus level increased from $G C I ^ { ( 1 ) } = 0 . 7 3 9 5 \mathrm { t o } G C I ^ { ( 2 ) } = 0 . 7 5 9 1$ after cluster $C ^ { 6 }$ quitted the decision process. This shows that the $\mathsf { D M } ( \mathsf { s } )$ who expresses an opinion that is very different from the group opinion and is not willing to modify its opinion can be required to exit the process in a timely manner. Such a move will assist the remaining DMs to reach an agreement within the limited time period.

(b) An improved consensus model in consideration of the management of minority opinions and non-cooperative behaviors is presented, in which the DMs are assumed to be emergency experts who often have a relatively reasonable and comprehensive understanding of emergency decision making.

(c) Combining subjective adjustment coefficient with objective adjustment coefficient, the concept of comprehensive adjustment coefficient is proposed, which is useful to reduce the uncertainty and fluctuation of subjective adjustment coefficients provided by DMs, and to improve the quality of decision making.

Future studies should focus mainly on developing a web-based consensus support system that is helpful and convenient for DMs located in different areas to make decisions via a web interface. The improved consensus model presented in this paper can be also extended to decision making in other major projects, such as project bidding and national project evaluation.

(a) The idea of objective adjustment coefficient is introduced to stimulate the entire consensus process and to provide an effective reference for determining two key parameters (i.e., the minimum group consensus threshold GCI and the maximum number of iterations CT). This stimulation is conducive to improving the rationality and accuracy of decision making.

## Acknowledgments

## 7. Conclusion

The authors would like to thank the editors and anonymous reviewers for their insightful comments and suggestions. This research is supported by grants from the National Natural Science Foundation

Based on the analysis of the characteristics of emergency decision environment, an improved consensus model for MCLGEDM problems is presented, which focuses on managing minority opinions and noncooperative behaviors. The major contributions of this paper are as follows:

Table 3  
Consensus consequences by using different types of adjustment coefficients (suppose that the minimum consensus threshold is set as GCI  0:80 and the weight coefficient is ε = 0.50).

<table><tr><td rowspan="2">t</td><td colspan="4">Subjective adjustment coefficient</td><td colspan="4">Objective adjustment coefficient</td><td colspan="4">Comprehensive adjustment coefficient</td></tr><tr><td> $C^{k^{\prime}}$ </td><td> $\eta_{k^{\prime}}^{S(t)}$ </td><td> $GCI^{(t)}$ </td><td>Adjustment amount</td><td> $C^{k^{\prime}}$ </td><td> $\eta_{k^{\prime}}^{O(t)}$ </td><td> $GCI^{(t)}$ </td><td>Adjustment amount</td><td> $C^{k^{\prime}}$ </td><td> $\eta_{k^{\prime}}^{(t)}$ </td><td> $GCI^{(t)}$ </td><td>Adjustment amount</td></tr><tr><td>0</td><td> $C^1$ </td><td>0.10</td><td>0.7386</td><td>-</td><td> $C^1$ </td><td>0.4169</td><td>0.7386</td><td>-</td><td> $C^1$ </td><td>0.2585</td><td>0.7386</td><td>-</td></tr><tr><td>1</td><td> $C^6$ </td><td>0.80</td><td>0.7442</td><td>0.0343</td><td> $C^6$ </td><td>0.3635</td><td>0.7622</td><td>0.1430</td><td> $C^6$ </td><td>0.80</td><td>0.7532</td><td>0.0887</td></tr><tr><td>2</td><td> $C^2$ </td><td>0.05</td><td>0.7854</td><td>0.1361</td><td> $C^2$ </td><td>0.2245</td><td>0.7808</td><td>0.1142</td><td> $C^2$ </td><td>0.1373</td><td>0.7931</td><td>0.2514</td></tr><tr><td>3</td><td> $C^5$ </td><td>0.10</td><td>0.7892</td><td>0.0130</td><td> $C^5$ </td><td>0.2218</td><td>0.7907</td><td>0.0581</td><td> $C^1$ </td><td>0.2107</td><td>0.7992</td><td>0.0358</td></tr><tr><td>4</td><td> $C^4$ </td><td>0.05</td><td>0.7934</td><td>0.0257</td><td> $C^4$ </td><td>0.1863</td><td>0.7998</td><td>0.0570</td><td> $C^5$ </td><td>-</td><td>0.8082</td><td>0.0541</td></tr><tr><td>5</td><td> $C^2$ </td><td>0.01</td><td>0.7956</td><td>0.0126</td><td> $C^6$ </td><td>-</td><td>0.8081</td><td>0.0458</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>6</td><td> $C^2$ </td><td>0.03</td><td>0.7960</td><td>0.0025</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>7</td><td> $C^4$ </td><td>0.10</td><td>0.7973</td><td>0.0074</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>8</td><td> $C^2$ </td><td>-</td><td>0.8013</td><td>0.0241</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Notes: The subjective adjustment coef cient provided by cluster $C ^ { 1 }$ in the 4-th iteration i $\eta _ { 1 } ^ { S ( 3 ) } = 0 . 2 .$

of China (Nos. 71171202, 71210003, and 71431006) and the National Innovation Research Group Science Foundation for China (No. 71221061).

## Appendix A. Symbol descriptions

$X = \{ x _ { 1 } , x _ { 2 } , . . . , x _ { P } \}$ Discrete finite set of emergency alternatives $x _ { l } ( l = 1 , 2 , . . . , P )$ Element in X $F = \{ f _ { 1 } , f _ { 2 } , . . . , f _ { N } \}$ Set of finite criteria $f _ { j } ( j = 1 , 2 , . . . , N )$ Element in F $\omega _ { j } ( j = 1 , 2 , . . . , N )$ Weight of the criterion $f _ { j }$ $\boldsymbol { E } = \{ e _ { 1 } , e _ { 2 } , . . . , e _ { M } \}$ Set of decision makers $\boldsymbol { e } _ { i } ( i = 1 , 2 , . . . , M )$ Element in E $\theta _ { i } ( i = 1 , 2 , . . . , M )$ Weight of DM e $V ^ { i } = ( \nu _ { l j } ^ { i } ) _ { P \times \ I N }$ Decision matrix provided by DM e $R ^ { i } = ( r _ { l j } ^ { i } ) _ { P \times N }$ Normalized decision matrix of DM e $\gamma ( 0 \leq \gamma \leq 1 )$ Clustering threshold value $G ^ { k } = ( g _ { l j } ^ { k } ) _ { P \times N }$ Cluster decision matrix $R ^ { c } = ( r _ { l j } ^ { c } ) _ { P \times \ I }$ Group decision matrix $\lambda _ { k } ^ { ( t ) } \left( k = 1 , 2 , . . . , K \right)$ Weight of cluster $C ^ { k }$ in the t-th iteration $\overline { { G C I } } ( 0 \leq \overline { { G C I } } \leq 1 )$ Minimum group consensus threshold value $( I ( G ^ { k ( t ) } ) \left( k = 1 , 2 , . . . , K \right)$ Cluster consensus level in the t-th iteration $G \dot { C } I ^ { ( t ) }$ Group consensus level in the t-th iteration t Number of iterations $C T$ Maximum number of iterations $C ^ { k ^ { * } }$ Cluster whose opinion has the biggest difference from the group opinion $\eta _ { k ^ { * } } ^ { S ( t ) }$ Subiective adiustment coefficient provided by cluster $C ^ { k ^ { * } }$ $\eta _ { k ^ { * } } ^ { O ( t ) }$ Objective adjustment coefficient $\eta _ { k ^ { * } } ^ { ( t ) }$ Comprehensive adjustment coefficient $\hat { A } \hat { D } ( G ^ { k ( t + 1 ) } , G ^ { k ( t ) } )$ Opinion adjustment amount between $G ^ { k ( t + 1 ) }$ and $G ^ { k ( t ) }$ n Threshold value that is used to determine whether a cluster belongs to a minority opinion subgroup in the view of the cluster's scale $\eta _ { k ^ { \prime } k ^ { \prime } } ^ { ( t ) } ( k ^ { \prime } = 1 , 2 , . . . , K ; k ^ { \prime } \ne k ^ { * } )$ Remaining clusters' expected adjustment suggestions $\overline { { \eta } } _ { \boldsymbol { k } ^ { \circ } } ^ { ( t ) }$ Expected adjustment suggestion interval $\tau ^ { ( t ) } ( C ^ { k ^ { * } } )$ Non-cooperative degree of modifying its opinion for cluster $C ^ { k ^ { * } }$ in the t-th iteration

## Appendix B. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2015.08.009.

## References

[1] J. Cosgrave, Decision making in emergencies, Dis. Prev. Manag. 5 (4) (1996) 28–35.

[2] J.K. Levy, K. Taji, Group decision support for hazards planning and emergency management: A Group Analytic Network Process (GANP) approach, Math. Comput. Model. 46 (7) (2007) 906–917.

[3] K. Xie, G. Chen, Q. Wu, Y. Liu, P. Wang, Research on the group decision-making about emergency event based on network technology, Inf. Technol. Manag. 12 (2) (2011) 137–147.

[4] L. Yu, K.K. Lai, A distance-based group decision-making methodology for multiperson multi-criteria emergency decision support, Decis. Support. Syst. 51 (2) (2011) 307–315.

[5] K. Xie, J. Liu, G. Chen, P. Wang, S.S. Chaudhry, Group decision-making in an unconventional emergency situation using agile Delphi approach, Inf. Technol. Manag. 13 (4) (2012) 351–361.

[6] D.F. Li, Compromise ratio method for fuzzy multi-attribute group decision making, Appl. Soft Comput. 7 (3) (2007) 807–817.

[7] A. Sanayei, S. Farid Mousavi, A. Yazdankhah, Group decision making process for supplier selection with VIKOR under fuzzy environment, Expert Syst. Appl. 37 (1) (2010).24-30

[8] F.E. Boran, S. Genç, M. Kurt, D. Akay, A multi-criteria intuitionistic fuzzy group decision making for supplier selection with TOPSIS method, Expert Syst. Appl. 36 (8) (2009) 11363–11368.

[9] S. Liu, F.T. Chan, W. Ran, Multi-attribute group decision-making with multigranularity linguistic assessment information: An improved approach based on deviation and TOPSIS, Appl. Math. Model. 37 (24) (2013) 10129–10140.

[10] J.Q. Wang, Z.Q. Han, H.Y. Zhang, Multi-criteria group decision-making method based on intuitionistic interval fuzzy information, Group Decis. Negot. 23 (4) (2014) 715–733.

[11] B. Liu, Y. Shen, W. Zhang, X. Chen, X. Wang, An interval-valued intuitionistic fuzzy principal component analysis model-based method for complex multi-attribute large-group decision-making, Eur. J. Oper. Res. 245 (1) (2015) 209–225.

[12] E. Herrera-Viedma, L. Martinez, F. Mata, F. Chiclana, A consensus support system model for group decision-making problems with multigranular linguistic preference relations, IEEE Trans. Fuzzy Syst. 13 (5) (2005) 644–658.

[13] F.J. Cabrerizo, I.J. Pérez, E. Herrera-Viedma, Managing the consensus in group decision making in an unbalanced fuzzy linguistic context with incomplete information, Knowl.-Based Syst. 23 (2) (2010) 169–181.

[14] L. Martínez, J. Montero, Challenges for improving consensus reaching process in collective decisions, New Math. Natur. Comput. 3 (2) (2007) 203–217.

[15] F. Herrera, E. Herrera-Viedma, A model of consensus in group decision making under linguistic assessments, Fuzzy Sets Syst. 78 (1) (1996) 73–87.

[16] E. Herrera-Viedma, F.J. Cabrerizo, J. Kacprzyk, W. Pedrycz, A review of soft consensus models in a fuzzy environment, Inf. Fusion 17 (2014) 4–13.

[17] B. Zhang, Y. Dong, Y. Xu, Multiple attribute consensus rules with minimum adjustments to support consensus reaching, Knowl.-Based Syst. 67 (2014) 35–48.

[18] D. Ben-Arieh, T. Easton, Multi-criteria group consensus under linear cost opinion elasticity, Decis. Support. Syst. 43 (3) (2007) 713–721.

[19] D. Ben-Arieh, T. Easton, B. Evans, Minimum cost consensus with quadratic cost functions, IEEE Trans. Syst. Man Cybern. Syst. Hum. 39 (1) (2009) 210–217.

[20] Y. Dong, C.C. Li, Y. Xu, X. Gu, Consensus-based group decision making under multigranular unbalanced 2-tuple linguistic preference relations, Group Decis. Negot. 24 (2014) 217–242.

[21] F. Mata, L. Martínez, E. Herrera-Viedma, An adaptive consensus support model for group decision-making problems in a multigranular fuzzy linguistic context, IEEE Trans. Fuzzy Syst. 17 (2) (2009) 279–290.

[22] Z. Xu, An automatic approach to reaching consensus in multiple attribute group decision making, Comput. Ind. Eng. 56 (4) (2009) 1369–1374.

[23] R.O. Parreiras, P.Y. Ekel, J.S.C. Martini, R.M. Palhares, A flexible consensus scheme for multicriteria group decision making under linguistic assessments, Inf. Sci. 180 (7) (2010) 1075–1089.

[24] J. Xu, Z. Wu, Y. Zhang, A consensus based method for multi-criteria group decision making under uncertain linguistic setting, Group Decis. Negot. 23 (1) (2014) 127–148.

[25] R. Parreiras, P. Ekel, F. Bernardes, A dynamic consensus scheme based on a nonreciprocal fuzzy preference relation modeling, Inf. Sci. 211 (2012) 1–17.

[26] Z. Gong, H. Zhang, J. Forrest, L. Li, X. Xu, Two consensus models based on the minimum cost and maximum return regarding either all individuals or one individual Fur L Oper, Res 240 (1) (2015) 183–192

[27] I. Palomares, Consensus model for large-scale group decision support in IT services management, Intell. Decis. Technol. 8 (2) (2014) 81–94.

[28] I. Palomares, L. Martinez, F. Herrera, A consensus model to detect and manage noncooperative behaviors in large-scale group decision making, IEEE Trans. Fuzzy Syst. 22 (3) (2014) 516–530

[29] C.Q. Xiong, D.H. Li, L.H. Jin, Group consistency analysis for protecting the minority view, Syst. Eng. Theory Pract. 10 (2008) 102–107.

[30] R.R. Yager, Penalizing strategic preference manipulation in multi-agent decision making, IEEE Trans. Fuzzy Syst. 9 (3) (2001) 393–403.

[31] G. Song, H. Yang, The decision-making behavior of group decision analysis, Acad. Res. 3 (2000) 48-49

[32] X.H. Xu, X.H. Chen, Research on the group clustering method based on vector space, Syst, Eng, Electron, 27 (6) (2005) 1034-1037.

[33] X.H., Chen X.H. Xu Research of a kind of method of multi-attributes and multischemes large group decision making, J. Syst. Eng. 23 (2) (2008) 137–141.

[34] F. Chiclana, J.M. Tapia García, M.J. del Moral, E. Herrera-Viedma, A statistical comparative study of different similarity measures of consensus in group decision making, Inf. Sci. 221 (2013) 110 123.

[35] Y. Nakahara, M. Sasaki, M. Gen, On the linear programming problems with interval coefficients, Comput. Ind. Eng. 23 (1992) 301–304.

[36] Z. Xu, Dependent uncertain ordered weighted aggregation operators, Inf. Fusion 9 (2008) 310-316

Xuanhua Xu is a Professor at the School of Business, Central South University, Changsha, China. He received his PhD degree from Central South University in 2005. His current research interests include complex large group decision making, emergency management and decision, engineering management, and decision support systems. His research results have been published in Knowledge-Based Systems, Applied Mathematics, Computers & Operations Research, Systems Science and Information, Systems Engineering Procedia, and Soft Computing, among others.

Zhijiao Du is a master degree candidate at the School of Business, Central South University, Changsha, China. He received his B.S. degree from the Department of economics and management, Hainan University in 2008. His current research interests include emergency management, group decision making, and decision support systems.

Xiaohong Chen is a Professor at the School of Business, Central South University, Changsha, China. She received her PhD degree from Tokyo Institute of Technology in 1999. Her current research interests include group decision making, decision support systems, and the financing of small and medium enterprises. Her research results have been published in Marketing Science, Decision Support Systems, Expert Systems with Applications, Chinese Economical Review, International Journal Production Economics, and International Journal of Intelligent Systems, among others.
