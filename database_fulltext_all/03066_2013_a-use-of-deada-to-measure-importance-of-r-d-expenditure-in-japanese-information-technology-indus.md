---
otero_id: 3066
otero_key: "8KKTWKXM"
title: "A use of DEA–DA to measure importance of R&D expenditure in Japanese information technology industry"
authors: "Toshiyuki Sueyoshi; Mika Goto"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.09.017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A use of DEA–DA to measure importance of R&D expenditure in Japanese information technology industry

Toshiyuki Sueyoshi <sup>a,</sup>⁎, Mika Goto <sup>b,1</sup>

<sup>a</sup> New Mexico Institute of Mining and Technology, Department of Management, 801 Leroy Place, Socorro, NM, 87801, USA

<sup>b</sup> Central Research Institute of Electric Power Industry, 1-6-1, Otemachi, Chiyodaku, Tokyo 100-8126, Japan

## a r t i c l e i n f o

Article history: Received 15 December 2011 Received in revised form 15 April 2012 Accepted 23 September 2012 Available online 29 September 2012

Keywords: DEA–DA Information Technology R&D Financial Performance

## a b s t r a c t

This study discusses a use of DEA–DA (Data Envelopment Analysis–Discriminant Analysis) to assess the corporate value of IT (Information Technology) <sup>fi</sup>rms and other manufacturing <sup>fi</sup>rms. It is widely known that Tobin's q is a ratio that serves as a measure of corporate value. This study explores a linkage between DEA–DA (as a methodology) and Tobin's q (as a theoretical basis for corporate performance) via the measurement of Altman's Z score (as a <sup>fi</sup>nancial performance). The Z score provides us with aggregated information regarding <sup>fi</sup>nancial ratios and other <sup>fi</sup>nancial measures that investors usually examine in their investment decisions. This study applies the proposed approach to compare between Japanese IT and manufacturing <sup>fi</sup>rms. The empirical evidence obtained in this study indicates that R&D (Research and Development) expenditure enhances the corporate value of Japanese IT and manufacturing <sup>fi</sup>rms. However, the R&D expenditure of IT <sup>fi</sup>rms is important but not essential, compared with other manufacturing <sup>fi</sup>rms in Japan. The empirical result is inconsistent with the opinion of many corporate leaders and individuals who are associated with the IT industry. They believe that the R&D expenditure is essential for the Japanese IT industry to maintain its international competitiveness in the global market. In addition to the R&D expenditure, the empirical study indicates that IT leaders need to pay attention to the reduction of an R&D cycle time to enhance their competitiveness because a market cycle time of IT products is less than that of the other manufacturing products. The <sup>fi</sup>ndings on Japanese IT and manufacturing industries are applicable to other industrial nations.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Information Technology (IT) heavily depends upon the development of telecommunications and consumer electronic devices that provides Internet and other various types of information system with global technology infrastructure by connecting computers and other communication systems in the world [2,5,7,24,33]. Decision Support Systems (DSS) discussed in this journal can be considered as an IT based decision-making system.

To enhance international competiveness in the IT industry, corporate leaders have long believed that their <sup>fi</sup>rms should make a large amount of expenditure on R&D (Research and Development). Their investment strategy originates from a business belief that IT <sup>fi</sup>rms are successful and competitive as long as they make large expenditure on R&D. It is indeed true that the R&D expenditure is important in developing new IT products, consequently enhancing the corporate value of IT <sup>fi</sup>rms. Thus, we expect that the R&D expenditure is a very important performance measure in evaluating IT <sup>fi</sup>rms. However, no previous study has investigated whether the R&D investment really enhances the corporate value of IT <sup>fi</sup>rms. In other words, does the R&D expenditure really enhance the competitiveness of IT <sup>fi</sup>rms? Does the R&D expenditure enhance their corporate values?

To reply such R&D policy issues regarding the IT industry, this study examines an in<sup>fl</sup>uence of R&D expenditure by comparing between Japanese IT and other manufacturing <sup>fi</sup>rms in terms of their corporate values. That is the purpose of this study.

A methodology used in this study is Discriminant Analysis (DA), or a classi<sup>fi</sup>cation method, that can predict the group membership of a newly sampled observation. In a use of DA, a group of observations, whose memberships are already identi<sup>fi</sup>ed, are used for estimating weights (or parameters) of a discriminant function by some criteria such as minimization of misclassi<sup>fi</sup>cations or maximization of correct classi<sup>fi</sup>cations. A new observation is classi<sup>fi</sup>ed into one of several groups by DA results. It is widely known that we use DA as a methodology of DSS such as data mining, decision tree, pattern recognition and many other methodologies developed in computer science.

Recently, Goto [23], Sueyoshi [48–50], Sueyoshi and Goto [51–53] have proposed a new type of nonparametric DA approach that provides a set of weights of a linear discriminant function(s), consequently yielding an evaluation score(s) for the determination of group membership. They have referred to the new nonparametric DA as “Data Envelopment

Analysis–Discriminant Analysis (DEA–DA),” because it maintains a discriminant capability by incorporating the nonparametric feature of DEA<sup>2</sup>into DA.

In evaluating the corporate value of Japanese IT and other manufacturing <sup>fi</sup>rms, this study faces many <sup>fi</sup>nancial criteria. One of such <sup>fi</sup>nancial criteria is Tobin's q<sup>3</sup>that indicates the ratio of a market value, or a growth potential, of a <sup>fi</sup>rm to the replacement cost of its physical assets. The ratio has been widely used in many <sup>fi</sup>nancial studies because it expresses a theoretical corporate value. This study attempts to make a linkage between DEA–DA and Tobin's q ratio (i.e. corporate value) of Japanese IT and manufacturing <sup>fi</sup>rms.

The remainder of this study is organized as follows: Section 2 reviews previous studies on DA and other classi<sup>fi</sup>cation methods. The section speci<sup>fi</sup>es the position of this study by comparing this study with the previous studies. Section 3 describes the research strategy of this study, including both DEA–DA formulations and corporate value assessment. Section 4 applies the proposed DEA– DA approach to measure the corporate value of Japanese IT and manufacturing <sup>fi</sup>rms. Section 5 concludes this study along with future research tasks.

## 2. Literature review

The literature of DA in DSS has a close linkage with decisionmaking and its applications in computer science. Thus, this review focuses upon a description on previous DA studies in the two research areas. The DA based decision-making has many research implications. This review <sup>fi</sup>rst focuses upon a description on previous studies, that have utilized mathematical programming for DA as a methodology of decision making, because this study belongs to the research area. After revisiting these previous efforts, this study directs toward previous research efforts on DA in computer science.

Mathematical Programming (MP): The previous research efforts on DA were methodologically classi<sup>fi</sup>ed into the following three groups: The <sup>fi</sup>rst contribution of this group was due to Charnes et al. [11] which documented how to formulate L metric regression by a GP (goal programming) model and how to solve the problem by linear programming algorithm. A popularity of MP-based DA among researchers occurred after the research effort of Freed and Glover [20,21]. They presented how DA problems could be formulated by GP. Based upon these optimization techniques, this group of DA studies was further classi<sup>fi</sup>ed into (a) linear programming approaches (e.g., Markowski and Markowski [36], Glover [22], Lam and Moy [32] and Mangasarian [35]), (b) nonlinear programming approaches (e.g., Cavalier et al. [10], Stam and Joachimsthaler [46],

Duarte Silva and Stam [14], and Falk and Karlov [16]) and (c) mixed integer programming approaches (e.g., Bajgier and Hill [4], Rubin [43], Abad and Banks [1], Wilson [58] and Yanev and Balev [59]). A comprehensive review on MP-based DA was found in Stam [46], Stam and Joachimsthaler [47], Doumpos et al. [13] and Zopounidis and Doumpos [62]. A methodological bene<sup>fi</sup>t of the research group is that the MP-based DA methods do not need any assumption on a group distribution. Meanwhile, a shortcoming of the MP-based DA is that statistical inferences and tests are not yet well established at the level of statistical and econometric approaches.

Computer Science: The group of DA research in computer science can be found in applications of Neural Network (NN), Decision Tree (DT) and other DSS techniques. For example, recently, NN has been successfully applied for classi<sup>fi</sup>cation and pattern recognition problems (e.g., Jain and Nag [27], Heinz et al. [25], Tam and Kiang [54], Markowski and Ragsdale [37] and We [57]). A methodological strength of the numerical approach is that NN is very <sup>fl</sup>exible so that it is not necessary to make any prior speci<sup>fi</sup>cation on a discriminant function. A learning process, incorporated into NN, constantly provides us with an updated discriminant rule. Those are indeed strengths of NN. A problem related to the NN approach is that it cannot guarantee the global optimality of NN solutions. Furthermore, NN produces many weights so that we cannot identify which factor is important or not in terms of group classi<sup>fi</sup>cation.

Meanwhile, DT is a heuristic approach that does not generate any classi<sup>fi</sup>cation rule. DT algorithms create a decision tree that properly classi<sup>fi</sup>es a training sample (Tam and Kiang [54]). There are several models available to us, such as tree induction proposed by Better et al. [8] and CART (Classi<sup>fi</sup>cation and Regression Trees) proposed by Breiman et al. [9] and used by Frydman et al. [19]. Both methods employ a non-backtracking splitting procedure that recursively partitions a set of examples into disjointed subsets. An algorithm incorporated in CART is usually structured in a binary classi<sup>fi</sup>cation tree that assigns observations into a priori selected groups. A data space is separated into several rectangular regions on a terminal node. All observations, falling into a given region of data space, are assigned to a subgroup (e.g., G or G ). The terminal nodes of a classi-<sup>fi</sup>cation tree are assigned to groups in such a way that the observed expected cost of misclassi<sup>fi</sup>cation of each assignment is minimized. A new object to be classi<sup>fi</sup>ed descends the classi<sup>fi</sup>cation tree and is assigned to the group identi<sup>fi</sup>ed with the terminal node into which it falls. Thus, the DT method is very intuitive in terms of group classi<sup>fi</sup>cation. However, it has methodological shortcomings similar to NN (e.g., no theoretical support on optimality).

Position of this study: It is clear that this study belongs to the MP group, in particular, the mixed integer programming approach. This article is the <sup>fi</sup>rst research effort that applies DEA–DA (as a methodology of DA in MP) to assess the corporate value of Japanese IT and manufacturing <sup>fi</sup>rms. Since the proposed use of DEA–DA is related to a decision-making process to assess the corporate value of <sup>fi</sup>rms, it can be considered as a methodology of DSS.

At the end of this section, it is necessary for us to describe three concerns. First, Tobin's q ratio, as a measure of corporate value, has already established a theoretical basis in previous <sup>fi</sup>nance studies. However, the ratio estimation has never completed because it contains imprecision in its information. The investigation on corporate value needs to improve a classi<sup>fi</sup>cation capability to overcome such a drawback related to the Tobin's q ratio measurement. To overcome such a dif<sup>fi</sup>culty, this research proposes a use of DEA–DA for assessing the corporate value. Second, DEA–DA has originated from DEA. See the research of Sueyoshi and Goto [52,53] that has described differences between DEA–DA and DEA. Since they provided a detailed description on the differences, this study does not describe it further except noting the references. Finally, Sueyoshi [49] has compared DEA–DA with many different approaches in computer science so that this study does not compare between them.

## 3. Research strategy

## 3.1. Computational flow

Fig. 1 visually describes a computational procedure of the proposed DEA–DA approach. First, the proposed approach identi<sup>fi</sup>es a high group of <sup>fi</sup>rms and a low group of <sup>fi</sup>rms based upon their Tobin's q ratios. This study refers to the two groups as “a high q group” and “a low q group”, respectively. This group classi<sup>fi</sup>cation based upon Tobin's q ratio is an initial step for the proposed approach. In this study, the high q group $\left( G _ { 1 } \right)$ consists of <sup>fi</sup>rms whose Tobin's q ratios belong to the top 25% and the low q group (G<sub>2</sub>) consists of <sup>fi</sup>rms whose Tobin's q ratios belong to the bottom 25%.

After obtaining the two groups, DEA–DA measures weight estimates of a discriminant function by using <sup>fi</sup>nancial factors regarding the two groups.

Based upon the weight estimates of a discriminant function, the proposed approach estimates the Altman's Z score of all <sup>fi</sup>rms and determines their <sup>fi</sup>nical performance by the Z scores. Altman [3] proposed the Z score for bankruptcy assessment, but this study uses it for the performance assessment of non-default <sup>fi</sup>rms. The use of Altman's Z score in this study is different from his original application. This study conceptually depends upon his approach, but replacing his methodology (i.e., Fisher [18] and Smith [27] as a DA tool) by DEA–DA (i.e., Sueyoshi [49]).

## 3.2. DEA–DA

Fig. 2 visually describes the computational process of DEA–DA. In the <sup>fi</sup>gure, the symbols (x and o) indicate the two groups of observations (i.e., <sup>fi</sup>rms). Two dimensions (e.g., <sup>fi</sup>nancial factors) in the <sup>fi</sup>gure measure each observation for our visual convenience. The <sup>fi</sup>rst stage identi<sup>fi</sup>es an overlap, or a shaded area, which is part of the area surrounded between the two lines (a-b and c-d) in Fig. 2. All the observations above the separation line (c-d) are classi<sup>fi</sup>ed as members of ${ \sf G } _ { 1 } .$ In contrast, all the observations below the separation line (a-b) are classi<sup>fi</sup>ed as members of $G _ { 2 } .$ The overlap corresponds to part of the area between the separation lines (a-b) and (c-d). The <sup>fi</sup>rst stage does not classify all the observations between the two lines, because the second stage classi<sup>fi</sup>es those in the overlap. The second stage estimates the separation line (e-f) for classifying all the observations in the overlap.

The identi<sup>fi</sup>cation of the overlap at the <sup>fi</sup>rst stage does not have any assumption. An exception is that DEA–DA identi<sup>fi</sup>es the overlap by two linear separation hyperplanes (i.e., a-b and c-d in Fig. 2). If we use another type of hyperplane (e.g., a non-linear hyperplane), the shape of an overlap is different from the one of Fig. 2. Thus, the number of observations depends upon the shape of an overlap. The two linear separation hyperplanes are because of our computational convenience.

![](/api/attachments/8KKTWKXM/fulltext/images/0eb4ed924e27cdaba260dc3504fe82db97e1ca395b9ed9623dbba0473942a24b.jpg)  
Fig. 2. Two stages of DEA–DA. (a) The observation (o) indicates the <sup>fi</sup>nancial performance of a <sup>fi</sup>rm in the group (G ). The performance of another <sup>fi</sup>rm in the group (G ) is speci<sup>fi</sup>ed by x. All observations are measured by the two <sup>fi</sup>nancial factors $( z _ { 1 }$ and z ).

Returning to the formulations of DEA–DA, the <sup>fi</sup>rst stage classi<sup>fi</sup>es observations not belonging to the overlap.

Stage 1: To discuss the <sup>fi</sup>rst stage, we consider the following formulation:

minimize s

$$
\begin{array}{l} \text {s.t.} \sum_ {f = 1} ^ {h} \lambda_ {f} z _ {f j} - d + s \geq 0, \mathrm{j} \in G _ {1}, \\ \sum_ {f = 1} ^ {h} \lambda_ {f} z _ {f j} - d - s \leq - \varepsilon , \mathrm{j} \in G _ {2}, \\ \sum_ {f = 1} ^ {h} \left| \lambda_ {f} \right| = 1, \\ \lambda_ {f}, \mathrm{dands:URS}. \end{array}\tag{1}
$$

The obiective function of Model (1) minimizes an unknown variable (s) that indicates a distance between $G _ { 1 }$ and $G _ { 2 } .$ . The unknown variable (s) indicates a size of the overlap surrounded by d-s (as a lower bound of $G _ { 1 } )$ and d+s (as an upper bound of $G _ { 2 } )$ . The discriminant score for group classi<sup>fi</sup>cation is expressed by a scalar value $\ " { } \mathtt { d } \ " { }$ Both d and s are unrestricted (URS) in Model (1). A very small number (ε) is incorporated into Model (1) in order to separate the two groups clearly. It is necessary for us to prescribe the number for Model (1). When an observation exists on an estimated discriminant function, we have a dif<sup>fi</sup>culty in its classi<sup>fi</sup>cation. Therefore, the small number (ε) is included in Model (1) for our classi<sup>fi</sup>cation convenience. All the <sup>fi</sup>nancial factors $( z _ { f j } )$ of the j-th observation are connected by a discriminant function $( \sum _ { f = 1 } ^ { h } \lambda _ { f } z _ { f j } )$ , where $\lambda _ { f }$ stands for the f-th weight to be estimated. The subscript (f) stands for the f-th <sup>fi</sup>nancial factor. These weights are restricted in such a manner that the sum of absolute values of $\lambda _ { f }$ (for all $\mathrm { f } = 1 , . . , \mathrm { h } )$ is unity. Consequently, Model (1) estimates each weight by a percentile expression, so that we can examine which weight is important or not in terms of group classi<sup>fi</sup>cation. This type of weight restriction is known as “normalization” in the area of DA.

![](/api/attachments/8KKTWKXM/fulltext/images/44991057f59db66c83af38126c5cf8e1f64ae62342ee8a3fd162facc005a83d9.jpg)  
Fig. 1. A computational <sup>fl</sup>ow for classi<sup>fi</sup>cation.

Since it is dif<sup>fi</sup>cult to solve Model (1) in a direct manner because of $\sum _ { f = 1 } ^ { h } \left| \lambda _ { f } \right| = 1$ , it is necessary to reformulate Model (1) to enhance the computational tractability. The reformulation of Model (1) has the following structure:

minimize s

$$
\begin{array}{l} \text { s.t. } \sum_ {f = 1} ^ {h} \left(\lambda_ {f} ^ {+} - \lambda_ {f} ^ {-}\right) z _ {f j} - d + s \geq 0, \mathrm{j} \in \mathrm{G} _ {1}, \\ \sum_ {f = 1} ^ {h} \left(\lambda_ {f} ^ {+} - \lambda_ {f} ^ {-}\right) z _ {f j} - d - s \leq - \varepsilon , \mathrm{j} \in \mathrm{G} _ {2}, \\ \sum_ {f = 1} ^ {h} \left(\lambda_ {f} ^ {+} + \lambda_ {f} ^ {-}\right) = 1, \\ \zeta_ {f} ^ {+} \geq \lambda_ {f} ^ {+} \geq \varepsilon \zeta_ {f} ^ {+} (\text { for   all   f }), \zeta_ {f} ^ {-} \geq \lambda_ {f} ^ {-} \geq \varepsilon \zeta_ {f} ^ {-} (\text { for   all   f }), \\ \zeta_ {\mathrm{f}} ^ {+} + \zeta_ {f} ^ {-} \leq 1 (\text { for   all   f }), \lambda_ {\mathrm{f}} ^ {+} + \lambda_ {\mathrm{f}} ^ {-} \geq \varepsilon (\text { for   all   f }), \\ \text { d   and   s:URS }, \zeta_ {\mathrm{f}} ^ {+} \& \zeta_ {\mathrm{f}} ^ {-}: \text { binary,and   all   other   variables } \geq 0. \end{array} \tag {2}
$$

In transforming $\lambda _ { f } \left( \mathrm { f } = 1 , . . . , \mathrm { h } \right)$ into a special ordered set of paired variables $( \lambda _ { f } = \lambda _ { f } ^ { + } - \bar { \lambda } _ { f } ^ { - } )$ , we de<sup>fi</sup>ne these variables as

$$
\lambda_ {f} ^ {+} = \left(\left| \lambda_ {f} \right| + \lambda_ {f}\right) / 2 \text {   and   } \lambda_ {f} ^ {-} = \left(\left| \lambda_ {f} \right| - \lambda_ {f}\right) / 2,\tag{3}
$$

each representing positive or negative part of $\lambda _ { f }$ respectively. These paired variables maintain the following relationships: $\lambda _ { f } = \lambda _ { f } ^ { + } - \lambda _ { f } ^ { - }$ and $\left| \lambda _ { f } \right| = \lambda _ { f } ^ { + } + \lambda _ { f } ^ { - }$

Such a transformation needs Non-Linear Condition (NLC: $\lambda _ { f } ^ { + } \lambda _ { f } ^ { - } = 0 )$ for each $\mathrm { f } ( = 1 , . . . , \mathrm { h } )$ in order to avoid a simultaneous occurrence of both $\lambda _ { f } ^ { + } > 0$ and $\lambda _ { f } ^ { - } > 0$ . To incorporate NLC, this study uses its MIP (Mixed Integer Programming) equivalence. Here, let $\zeta _ { f } ^ { + } ( = 0 \ \mathrm { o r } \ 1 )$ and $\zeta _ { f } ^ { - } ( = 0 \ \mathrm { o r } \ 1 )$ be two binary variables, then NLC is expressed by

$$
N L C: \quad \zeta_ {f} ^ {+} \geq \lambda_ {f} ^ {+} \geq \varepsilon \zeta_ {f} ^ {+} \text { and } \zeta_ {f} ^ {-} \geq \lambda_ {f} ^ {-} \geq \varepsilon \zeta_ {f} ^ {-} \quad (f = 1,.., h)\tag{4}
$$

$$
\zeta_ {f} ^ {+} + \zeta_ {f} ^ {-} \leq 1 \quad (\mathrm{f} = 1,.., \mathrm{h})\tag{5}
$$

Eq. (4) implies the upper bound $( = 1 )$ and lower bound (=0) of ${ \lambda } _ { f } ^ { + }$ and those bounds of $\lambda _ { f } ^ { - }$ , respectively. Eq. (5) implies that the sum of these binary variables is less than or equal to unity. If both $\lambda _ { f } ^ { + } \ge \varepsilon > 0$ and $\lambda _ { f } ^ { - } \ge \varepsilon > 0$ occur simultaneously in Eq. (4), then Eq. (5) becomes $\zeta _ { f } ^ { + } + \bar { \zeta } _ { f } ^ { - } = 2 .$ The result is infeasible in Eq. (5). Thus, the simultaneous occurrence of $\lambda _ { f } ^ { + } > 0$ and $\bar { \lambda _ { f } } ^ { - } > 0$ is excluded from the computational process of Model (2). All the other $( \lambda _ { f } ^ { + }$ and $\lambda _ { f } ^ { - } )$ combinations become feasible in Eqs. (4) and (5), so being feasible in Model (2).

At the end of the <sup>fi</sup>rst stage of DEA–DA, it is necessary to separate all observations into four subsets. To explain the classi<sup>fi</sup>cation, let $\lambda _ { f } ^ { * } ( = \lambda _ { f } ^ { + } ^ { * } - \lambda _ { f } ^ { - } ^ { * } )$ , d\* and $s ^ { * }$ be an optimal solution of Model (2). Then, the original data set (G) is classi<sup>fi</sup>ed by the following subsets

<sub>¼</sub> j∈G<sub>1</sub><sup>--</sup>-<sub>-</sub><sup>8<</sup> h $\mathrm { G } { = } G _ { 1 } \cup G _ { 2 } { = } C _ { 1 } \cup D _ { 1 } \cup C _ { 2 } \cup D _ { 2 }$ where C<sub>1</sub> <sup>X</sup> λ-<sub>f</sub> z<sub>fj</sub> > d<sup>-</sup> <sub>þ</sub> sf 1- $C _ { 2 } = \left\{ j { \in } G _ { 2 } \Biggl | \sum _ { f = 1 } ^ { h } \lambda _ { f } ^ { * } z _ { f j } { < } d ^ { * } - s ^ { * } \right\} , D _ { 1 } = G _ { 1 } - C _ { 1 }$ and $D _ { 2 } { = } G _ { 2 } { - } C _ { 2 }$ . The classi-<sup>fi</sup>cation determines that observations in $C _ { 1 }$ belong $\mathrm { t o } G _ { 1 }$ and those of $C _ { 2 }$ belong to $G _ { 2 }$ because the observations locate clearly above or clearly below an overlap identi<sup>fi</sup>ed from Model (2). The two subsets $\left( D _ { 1 } \cup D _ { 2 } \right)$ consist of the overlap whose observations are not yet classi-<sup>fi</sup>ed in the <sup>fi</sup>rst stage.

Sign of the unknown variable (s): The <sup>fi</sup>rst stage identi<sup>fi</sup>es the existence of an overlap by $s ^ { * } { \geq } 0$ on optimality of Model (2). An opposite case $( s ^ { * } { < } 0 )$ indicates no overlap. In this case, the DEA–DA stops at the <sup>fi</sup>rst stage.

Stage 2: In the case when two groups have an overlap, it is necessary to reclassify all the observations in the overlap $( D _ { 1 } \cup D _ { 2 } )$ , because the group membership of these observations is still unknown and needs to be determined. Mathematically, the second stage has the following formulation:

$$
\begin{array}{l} \text { minimize } \sum_ {j \in D _ {1}} y _ {j} + \sum_ {j \in D _ {2}} y _ {j} \\ s. t. \sum_ {f = 1} ^ {h} \left(\lambda_ {f} ^ {+} - \lambda_ {f} ^ {-}\right) z _ {f j} - c + M y _ {j} \geq 0, \quad j \in D _ {1}, \\ \sum_ {f = 1} ^ {h} \left(\lambda_ {f} ^ {+} - \lambda_ {f} ^ {-}\right) z _ {f j} - c - M y _ {j} \leq - \varepsilon , \quad j \in D _ {2}, \\ \sum_ {f = 1} ^ {h} \left(\lambda_ {f} ^ {+} + \lambda_ {f} ^ {-}\right) = 1, \\ \zeta_ {f} ^ {+} \geq \lambda_ {f} ^ {+} \geq \varepsilon \zeta_ {f} ^ {+} (\text { for   all   f }), \zeta_ {f} ^ {-} \geq \lambda_ {f} ^ {-} \geq \varepsilon \zeta_ {f} ^ {-} (\text { for   all   f }), \\ \zeta_ {f} ^ {+} + \zeta_ {f} ^ {-} \leq 1 (\text { for   all   f }), \zeta_ {f} ^ {+} + \zeta_ {f} ^ {-} \geq \varepsilon (\text { for   some   f }), \\ c: U R S, \zeta_ {f} ^ {+}, \zeta_ {f} ^ {-} \& y _ {j}: b i n a r y, a n d a l l o t h e r v a r i a b l e s \geq 0. \end{array}\tag{6}
$$

Here, the binary variable (y ) counts the number of observations classi-<sup>fi</sup>ed incorrectly in the two groups $( D _ { 1 } \cup D _ { 2 } )$ . The objective function minimizes the number of misclassi<sup>fi</sup>cations. It is necessary to prescribe a large number (M) in Model (6). A discriminant score (c) is newly incorporated into Model (6) as an unknown unrestricted variable. The new score (c) for the second stage substitutes for the previous discriminant score (d) in Model (2) for the <sup>fi</sup>rst stage.

Non-Zero Condition (NZC): A possibility, to which we need to pay attention, is a simultaneous occurrence of $\lambda _ { f } ^ { + } = 0$ and $\lambda _ { f } ^ { - } = 0$ in Models (2) and (6). To control the number of positive $\lambda _ { f }$ estimates, we may add the following Non-zero condition (NZC) in Models (2) and (6):

$$
\text { NZC }: \quad \lambda_ {f} ^ {+} + \lambda_ {f} ^ {-} \geq \varepsilon \quad (\text { for   some   f })\tag{7}
$$

Here, several pairs avoid a simultaneous occurrence of $\lambda _ { f } ^ { + } = 0$ and $\begin{array} { r } { \lambda _ { f } ^ { - } = 0 . } \end{array}$ Of course, we can specify that all the pairs can avoid the condition (7). The selection of Eq. (7) depends upon a user who can make his decision by considering the degree of freedom in DEA–DA. Since Model (2) uses all observations, the NZC may not be a major issue at the <sup>fi</sup>rst stage. However, Model (6) uses only observations (so, limited) in an overlap so that it is important for us to pay serious attention to NZC (7) at the second stage.

After obtaining an optimal solution on ${ \lambda } _ { f } ^ { * }$ and $c ^ { * }$ from Model (6), the second stage classi<sup>fi</sup>es observations in the overlap as follows: if $\sum _ { f = 1 } ^ { h } \lambda _ { f } ^ { * } z _ { f j } \ge c ^ { * }$ , then the j-th observation (<sup>fi</sup>rm) belongs to ${ \sf G } _ { 1 }$ or if

$\sum _ { f = 1 } ^ { h } \lambda _ { f } ^ { * } z _ { f j } \leq c ^ { * } - \varepsilon ,$ , then it belongs to ${ \bf G } _ { 2 } .$ Thus, all the observations in G

are classi<sup>fi</sup>ed into either ${ \sf G } _ { 1 }$ or ${ \sf G } _ { 2 }$ at the end of the second stage.

## 3.3. Altman's Z score

DEA–DA provides a performance measure due to the work of Altman [3]. Following his work, the <sup>fi</sup>nancial performance of the j-th <sup>fi</sup>rm is measured by a score $\left( Z _ { j } = \sum _ { f = 1 } ^ { h } \lambda _ { f } ^ { * } z _ { f j } \right)$ where $\lambda _ { f } ^ { * }$ is the f-th weight estimate of a discriminant function. This study cannot directly compute Altman's Z score because DEA–DA produces two discriminant functions for group classi<sup>fi</sup>cation. Hence, it is necessary to modify the Z score for our research purpose.

To describe the modi<sup>fi</sup>cation, this study returns to the computational processes of DEA–DA in which the <sup>fi</sup>rst stage estimates a discriminant function $\left( \sum _ { f = 1 } ^ { h } \lambda _ { f } ^ { 1 * } z _ { f } \right)$ and the second stage estimates a discriminant function $\left( \sum _ { f = 1 } ^ { h } \lambda _ { f } ^ { 2 * } z _ { f } \right)$ . The Z score for the j-th <sup>fi</sup>rm (for $\mathrm { j } = 1 , . . , \mathrm { n } )$ is de<sup>fi</sup>ned as follows:

$$
\begin{array}{l} Z _ {j} = \frac {n}{n + \# (\text {overlap})} \sum_ {f = 1} ^ {h} \lambda_ {f} ^ {1 *} z _ {f j} + \frac {\# (\text {overlap})}{n + (\text {overlap})} \sum_ {f = 1} ^ {h} \lambda_ {f} ^ {2 *} z _ {f j} \\ = \sum_ {f = 1} ^ {h} \left(\frac {n}{n + \# (\text {overlap})} \lambda_ {f} ^ {1 *} + \frac {\# (\text {overlap})}{n + \# (\text {overlap})} \lambda_ {f} ^ {2 *}\right) z _ {f j}. \end{array}\tag{8}
$$

This study refers to the above equation as “Altman's Z score” or simply “Z score”. Exactly speaking, the above equation is slightly different from the equation for the original Z score proposed by Altman [3]. However, this study uses the term to honor his research work.

The proposed Z score consists of weight estimates adjusted by the number of observations used in the <sup>fi</sup>rst and second stages of DEA– DA. The adjustment is due to the computational process of DEA–DA in which the <sup>fi</sup>rst stage (for overlap identi<sup>fi</sup>cation) estimates weights of a discriminant function by using all the observations. The total sample size $" \mathrm { n } "$ is used for the <sup>fi</sup>rst stage. Meanwhile, the second stage of DEA–DA utilizes only observations in the overlap. The sample size used in the second stage is # (overlap), or the number of observations belonging to the overlap. Thus, this study combines two groups of weight estimates measured by DEA–DA into a single set of weight estimates in order to compute the Z score. Using the Z score, this study determines the level of <sup>fi</sup>nancial performance of all <sup>fi</sup>rms (observations). Furthermore, we can rank all <sup>fi</sup>rms based upon their Z scores. This study uses the ranking scores to conduct a rank sum test.

Finally, the proposed use of DEA–DA has two stages for computation as depicted in Fig. 2. As a result, the use of DEA–DA has double standards for classi<sup>fi</sup>cation. This study is fully aware of the double standard issue. To handle the issue, we have previously documented DEA–DA with a single-stage (often referred to as “standard”) for computation. See, for example, Sueyoshi [49] has proposed a single-stage approach for DEA– DA. A problem of the single-stage approach is that its computation time is much longer than that of the two-stage model. The correct classi-<sup>fi</sup>cation rate, often referred to as “a hit rate”, of the single-stage approach is always lower than that of the two-stage approach. See, for example, Sueyoshi [49] who has compared the two (single-stage and two-stage) approaches in terms of a computation time and a classi<sup>fi</sup>cation rate. Moreover, the two-stage approach is more robust to the change of M and ε than the single-stage approach. Thus, this study uses the twostage approach for DEA–DA. To solve the double standard issue partly, Eq. (8) combines two discriminant functions into a single function to obtain Altman's Z score. Of course, Eq. (8) does not have any mathematical justi<sup>fi</sup>cation but it is intuitively acceptable. The double standard issue of the two-stage approach will be an important future research task.

## 3.4. A practical use of DEA–DA weight estimates and Altman's Z score

Our underlying view on Tobin's q assessment is that the q ratio is imprecise in measuring the corporate value of a <sup>fi</sup>rm. However, as discussed by the previous <sup>fi</sup>nancial studies (e.g., Chung and Wright [12]), it is easily imagined that <sup>fi</sup>rms belonging to the top 25% group in the Tobin's q ratio have high corporate value and those of the bottom 25% group have low corporate value even though these ratios are imprecise. A problem is that it is very dif<sup>fi</sup>cult for us to determine clearly the corporate value of <sup>fi</sup>rms, belonging to the remaining 50% group, because the measurement of Tobin's q ratio has imprecision on those <sup>fi</sup>rms. Therefore, the proposed use of DEA–DA uses only the top 25% and bottom 25% groups, as a training sample, to obtain its weight estimates and it excludes imprecise information on Tobin's q ratio regarding <sup>fi</sup>rms between the top and bottom groups because their information is unreliable.

Fig. 3 depicts the use of DEA–DA weight estimates and its derived Altman's Z score from a practical perspective. It is possible for us to use the proposed approach for the two types of practical applications.

![](/api/attachments/8KKTWKXM/fulltext/images/c3ee9b4c662a10d41a5ca1a22d416ca00294e9e169bdffbbd6173118beb78e2b.jpg)  
Fig. 3. Practical use of DEA–DA weight estimates and Altman's Z score. (a) Decision makers (e.g., corporate leaders and managers) do not have an analytical capability because of their bounded rationality and limited information processing capabilities. The proposed approach, centering upon DEA–DA, assists them by providing an analytical capability in predicting the corporate value of a newly sampled firm, The interaction between DEA-DA and decision makers is important in designing DSS for financial decisions

One of the two types of applications is that we can determine the group classi<sup>fi</sup>cation of a newly sample observation, or a new <sup>fi</sup>rm, that does not have any information on its Tobin's q ratio except the information on <sup>fi</sup>nancial factors. Furthermore, even though the new <sup>fi</sup>rm has its Tobin's q ratio, we cannot use the q ratio as reliable information if it does not belong to the top 25% or the bottom 25% in a whole sample. In this case, it is dif<sup>fi</sup>cult to assess immediately the corporate value of the <sup>fi</sup>rm. It is recommended that we assess the corporate value of the <sup>fi</sup>rm by DEA–DA. The other application is that we can compute the Z scores of all observed <sup>fi</sup>rms and then rank them based upon their Z scores. Using their ranks, this study conducts a rank sum test to examine a null hypothesis (i.e. no difference between the two groups). DEA–DA does not have any statistical inference. Therefore, the rank sum test partly overcomes the methodological drawback of DEA–DA. Moreover, we can use the Z scores and ranks of <sup>fi</sup>rms for their corporate value assessment, originally based upon Tobin's q ratio of 50% (top 25% and bottom 25%) <sup>fi</sup>rms. Such a new type of assessment is applicable to all <sup>fi</sup>rms even though they (e.g., <sup>fi</sup>rms not belonging to the top and bottom groups) have imprecise information on their Tobin's q ratios.

## 3.5. Methodological comparison: Logit and probit models vs DEA–DA

By extending statistical approaches (e.g., Fisher [18] and Smith [45]), econometricians (e.g., McFadden [40,41]) have developed several DA methods that are closely linked to the theory of a probabilistic choice discussed by psychologists. The most well known econometric models are logit and probit models that are usually solved by maximum-likelihood methods. An important feature of logit and probit analyses is that they provide the conditional probability of an observation belonging to a certain class, given its independent variables (<sup>fi</sup>nancial factors in this study). Both models are based on a cumulative probability function. For example, the logit model depends upon a logistic distribution and the probit model depends upon a normal distribution. The two models do not require that independent variables are multivariate normal or that groups have equal covariance matrices, unlike the requirements of statistical DA. Based upon such assumptions, these approaches are closely linked to statistical inferences and various tests.

By comparing DEA–DA with the logit and probit models, this study describes the methodological strengths and drawbacks of DEA–DA.

First, the two econometric models produce parameter estimates for a linear discriminant function to predict the group classi<sup>fi</sup>cation of an observation(s). In this sense, the econometric approaches belong to parametric estimation. In contrast, DEA–DA produces weight estimates for the linear discriminant function. Thus, DEA–DA belongs to nonparametric estimation.

Second, DEA–DA estimates weights under the condition that it minimizes the number of misclassi<sup>fi</sup>cations. It is not necessary for us to make any assumption on the distribution of a cumulative probability. Meanwhile, the two econometric models maximize the value of a log-likelihood function under postulated distribution assumptions (i.e., a logistic distribution for the logit model and a normal distribution for the probit model) on the cumulative probability. Thus, DEA–DA can become a nonparametric alternative to the logit and probit models.

Third, the two econometric approaches provide us with various convenient statistical tests in prevalent computer software tools. In contrast, DEA–DA does not have any statistical test based upon the asymptotic theory. No user-friendly software on DEA–DA is available to us. The development of user-friendly software including many statistical tests is necessary for enhancing the practicality of DEA–DA. This study proposes a use of DEA–DA combined with a rank sum test in order to overcome partly the statistical problem associated with DEA–DA.

Finally, the selection of M and ε in<sup>fl</sup>uences weight estimates and a discriminant score. Hence, such an in<sup>fl</sup>uence may change a classi<sup>fi</sup>cation rate. Different selections on such values often produce different weight estimates and different classi<sup>fi</sup>cation rates. That is a major shortcoming of DEA–DA. This study selects the two values heuristically after considering many different combinations. The selection of the best combination among them is still unknown. The task to identify the best combination is an important future extension of this study. The two econometric approaches do not have such a methodological problem.

## 4. An application to Japanese IT and manufacturing <sup>fi</sup>rms

## 4.1. Business hypotheses

This study empirically compares between IT and manufacturing <sup>fi</sup>rms in terms of the in<sup>fl</sup>uence of R&D expenditure on their corporate values. In this study, the IT industry includes computer, telecommunications and electrical machinery and apparatuses <sup>fi</sup>rms. Meanwhile, the manufacturing industry includes nonferrous, general machinery, auto and transportation machinery and apparatuses <sup>fi</sup>rms. This study selects these manufacturing industries because they are major corporate players in Japan. In particular, the machinery and auto industries export their products all over the world and generate a trade surplus for Japan.

Hypothesis 1. The R&D expenditure increases the corporate value (measured by Tobin's q) of Japanese IT and manufacturing <sup>fi</sup>rms.

Hypothesis 2. The R&D expenditure is more in<sup>fl</sup>uential on the manu facturing <sup>fi</sup>rms than the IT <sup>fi</sup>rms.

The two hypotheses are due to the previous study (Sueyoshi and Goto [51]) that has investigated whether R&D expenditure in<sup>fl</sup>uenced the <sup>fi</sup>nancial performance of Japanese machinery industry and electric equipment industry. The investigation, based upon bankruptcy-based assessment, identi<sup>fi</sup>ed that the R&D expenditure made a positive impact on the <sup>fi</sup>nancial performance of Japanese machinery industry, but it yielded a negative impact on Japanese electric equipment industry. The result implies that the in<sup>fl</sup>uence of R&D expenditure on <sup>fi</sup>nancial performance (including the avoidance of bankruptcy) depends upon the type of an industry. This study extends the previous study by changing the criterion from bankruptcy to corporate value. This study replaces a data set related to the two industries, as well.

The importance of the two hypotheses can be also found in the research of Mallick and Schroeder [34]. Their study did not <sup>fi</sup>nd any signi<sup>fi</sup>cant linkage between R&D expenditure and corporate/<sup>fi</sup>nancial performance in US electric equipment industry. According to their study [34], the electronics industry faces a high rate of change in technology and market conditions and, accordingly, it is classi<sup>fi</sup>ed as a high clock speed industry (Mendelson and Pillai [42]). It is well known that electronics are subject to short product life cycles and associated with fast new product development (Eisenhardt and Tabrizi [15] and Fine [17]).

In addition to the hypotheses related to R&D expenditure, this study examines the following hypotheses:

Hypothesis 3. Firms in the top 25% of Tobin's q outperform those between the top 25% and the bottom 25% of Tobin's q. They outperform <sup>fi</sup>rms in the bottom 25% of Tobin's q. The criterion for comparison is the <sup>fi</sup>nancial performance (measured by Altman's Z spore) of the two industries.

Hypothesis 4. The IT and manufacturing industries have increased their <sup>fi</sup>nancial performance (measured by Altman's Z score) over the sample period.

The third hypothesis is due to the research of Chung and Wright [12] that has classi<sup>fi</sup>ed sample companies into two groups: companies with high corporate performance (because of their high q ratios) and those with low corporate performance (because of their low q ratios). The classi<sup>fi</sup>cation indicates that if a <sup>fi</sup>rm is in the top 25% of Tobin's q ratios, the <sup>fi</sup>rm belongs to the high q group. On the other hand, if a <sup>fi</sup>rm is in the bottom 25% of Tobin's q ratios, the <sup>fi</sup>rm belongs to the low q group.

The fourth hypothesis is due to a performance shift of the two industries in a time horizon. We expect that there is technology advancement that enhances their <sup>fi</sup>nancial performance. Therefore, the technology advancement may improve the operational performance of those <sup>fi</sup>rms. However, the enhancement in their operational performance may not immediately improve their <sup>fi</sup>nancial performance because there is a time lag between the performance measures. Thus, this study needs to examine the fourth hypothesis.

## 4.2. Data description

To investigate the four hypotheses, this study sampled the <sup>fi</sup>nancial factors of 357 (IT and other manufacturing) <sup>fi</sup>rms from 2004 to 2007 in accordance with Japanese accounting period (April to March). All the <sup>fi</sup>rms are listed in the <sup>fi</sup>rst section of Tokyo stock exchange market. The total sample size is 1071 (=3 annual periods×357 <sup>fi</sup>rms). The manufacturing industry contains 219 <sup>fi</sup>rms so that the total sample size is 657 (=3 annual periods×219 <sup>fi</sup>rms). Meanwhile, the IT industry contains 138 <sup>fi</sup>rms so that the total sample size is 414 (=3 annual periods×138 <sup>fi</sup>rms). This study has obtained the data set from “Financial Data Bank” of the Japan Economic Research Institute (2008).

It is important to note that the <sup>fi</sup>rms used in this study cover almost all large <sup>fi</sup>rms listed in the <sup>fi</sup>rst section of Tokyo stock exchange market. There are other stock exchange markets (e.g., the second section of Tokyo stock exchange market as well as Osaka and Nagoya stock exchange markets). The <sup>fi</sup>rst section of Tokyo stock exchange market collects only major Japanese <sup>fi</sup>rms. It is indeed true that a sample size may affect the accuracy of our computational results. However, all the <sup>fi</sup>rms examined in this study really represent Japanese economy and industry so that the sample size does not in-<sup>fl</sup>uence the business implications obtained from this study.

This study computes the Tobin's q ratio of <sup>fi</sup>rms by the simple q ratio. Each <sup>fi</sup>rm is characterized by the following six <sup>fi</sup>nancial factors: First, R&D I (R&D Intensity): R&D expenditure divided by total revenue (%)<sup>4</sup>. Second, NITR (Ratio of net income to total revenue): net income divided by total revenue (%)<sup>5</sup>. Third, LISE (Ratio of liability with interest to shareholder's equity): total liability with interest divided by shareholder's equity (%)<sup>6</sup>. Fourth, Gror1 (Growth rate of total revenue on 1 year): (total revenue in this period–total revenue in the previous period)/total revenue in this period (%)<sup>7</sup>. Fifth, Exec (Ratio of executive shareholdings to total shares): executive shareholdings divided by total shares (%)<sup>8</sup>. Sixth, DPR (Dividend payout ratio): total dividend divided by earnings before tax (%)<sup>9</sup>.

Table 1 provides descriptive statistics regarding the two <sup>fi</sup>rm groups. Tables 2 and 3 document the correlation matrix of two groups along with these eigenvalues of X<sup>T</sup>X. If any of the eigenvalues of X<sup>T</sup>X is zero, then the estimates fail to be unique, where X is a data matrix of six <sup>fi</sup>nancial factors. If any eigenvalue is negative, then there is a problem of multicollinearity. However, even if these conditions are satis<sup>fi</sup>ed, another dif<sup>fi</sup>culty may appear if some of the positive eigenvalues are very small. The near-collinearity problem occurs in the case.

The two tables indicate that the correlation among <sup>fi</sup>nancial factors is low. Furthermore, all the eigenvalues are much larger than zero. Thus, all the <sup>fi</sup>nancial factors are independent of each other and the problem of multicollinearity does not occur in the two data sets

## 4.3. Computational results and comparison with alternatives

Tables 4 and 5 summarize resulting weights or parameter estimates of DEA–DA, logit and probit regressions. This study uses the logit and probit models as methodological alternatives of the proposed DEA–DA<sup>10</sup>. The two tables correspond to manufacturing and IT <sup>fi</sup>rms, respectively. The correct classi<sup>fi</sup>cation rate in the two tables indicates the number of observations classi<sup>fi</sup>ed correctly divided by the number of observations in the high q group or the low q group. The total indicates the classi<sup>fi</sup>cation rate of the combined two groups.

As summarized in the two tables, DEA–DA outperforms the logit and probit models in terms of the total classi<sup>fi</sup>cation rate. For example, DEA–DA has 76.52% in Table 4 and 78.50% in Table 5 as the total classi<sup>fi</sup>cation rates, respectively. Meanwhile, the corresponding rates of the logit model are 69.82% in Table 4 and is 69.71% in Table 5, respectively. A similar result can be found in the classi<sup>fi</sup>cation rate of the probit model.

Here, it is important to mention that this study does not deny the importance of logit and probit models. Rather, this type of empirical study needs to consider the existence of a methodological bias (i.e., different methods produce different results). Therefore, we use the results from the three methods as our empirical evidence.

In Table 4, R&D I and NITR have the same sign between DEA–DA and the logit/probit models in the two industries. Exec and DPR have the same sign between them in the manufacturing industry. Furthermore, when DEA–DA has a large magnitude on a weight estimate, the logit/probit models identify statistical signi<sup>fi</sup>cance on them.

Tables 4 and 5 document that DEA–DA has a positive weight estimate on R&D intensity in both IT and manufacturing <sup>fi</sup>rms. The result indicates the validity of Hypothesis 1. Furthermore, the magnitude of the weight estimate on R&D intensity in the manufacturing <sup>fi</sup>rms is larger than that of the IT <sup>fi</sup>rms. The result indicates the validity of Hypothesis 2. This research con<sup>fi</sup>rms the two empirical results by the logit and probit models, as well.

## 4.4. R&D cycle time and market cycle time

To investigate further the business implication mentioned above, this study examines an R&D cycle time and a market cycle time related to manufacturing and IT industries. The R&D cycle time is a period from the start of R&D to the initial production of a product. The market cycle time is a period from the initial sale of a product to its production/sale termination.

Fig. 4 depicts the market cycle time of the IT and manufacturing industries. The averages of the market cycle time of the manufacturing industry are 12.7, 10.1 and 7.2 years, respectively, in the three annual periods (1988–1993, 1993–1998 and 2002–2007)<sup>11</sup>. Meanwhile, the averages of the market cycle time of the IT industry are 8.2, 6.6 and 4.4 years, respectively, in the three annual periods. The <sup>fi</sup>gure visually implies that the manufacturing industry has a longer market cycle time than the IT industry. Furthermore, the market cycle time of the two industries has a declining trend in the observed periods. The two empirical results indicate that products of the manufacturing <sup>fi</sup>rms can stay in a market enough to recoup the R&D investment, compared with the IT <sup>fi</sup>rms.

Table 2  
Table 1  
Descriptive statistics of IT and manufacturing industries (top 25% and bottom 25%).

<table><tr><td></td><td>R&amp;D I</td><td>NITR</td><td>LISE</td><td>Gror1</td><td>Exec</td><td>DPR</td></tr><tr><td colspan="7">High q group</td></tr><tr><td>Average</td><td>7.02</td><td>13.89</td><td>125.63</td><td>31.40</td><td>4.53</td><td>9.42</td></tr><tr><td>Median</td><td>5.43</td><td>10.00</td><td>12.92</td><td>7.26</td><td>0.58</td><td>15.79</td></tr><tr><td>Max.</td><td>53.17</td><td>146.15</td><td>9627.63</td><td>2466.40</td><td>42.69</td><td>400.31</td></tr><tr><td>Min.</td><td>0.00</td><td>-44.94</td><td>0.00</td><td>-96.60</td><td>0.00</td><td>-1899.55</td></tr><tr><td>S.D.</td><td>7.54</td><td>21.37</td><td>942.28</td><td>242.64</td><td>8.43</td><td>200.25</td></tr><tr><td colspan="7">Low q group</td></tr><tr><td>Average</td><td>4.52</td><td>4.05</td><td>66.94</td><td>2.42</td><td>5.54</td><td>38.52</td></tr><tr><td>Median</td><td>4.09</td><td>3.88</td><td>17.37</td><td>1.85</td><td>0.82</td><td>23.62</td></tr><tr><td>Max.</td><td>19.37</td><td>20.49</td><td>4189.20</td><td>23.25</td><td>41.99</td><td>822.22</td></tr><tr><td>Min.</td><td>0.00</td><td>-29.20</td><td>-150.11</td><td>-63.23</td><td>0.03</td><td>-40.01</td></tr><tr><td>S.D.</td><td>3.29</td><td>6.24</td><td>409.81</td><td>9.96</td><td>10.09</td><td>91.59</td></tr><tr><td>t test</td><td>3.04***</td><td>4.53***</td><td>0.57</td><td>1.22</td><td>-0.78</td><td>-1.37</td></tr></table>

(a) The t-test at the bottom indicates the result of Welch's t test. The superscript \*\*\* rejects a null hypothesis (there is no difference between two groups) at the level of 1% signi<sup>fi</sup>cance.

Fig. 5 indicates the R&D cycle time of the IT and manufacturing <sup>fi</sup>rms. In Fig. 4, the averages of the R&D cycle time of the IT industry are 4.2, 3.2 and 2.2 years, respectively, in the three annual periods (1988–1993, 1993–1998 and 2002–2007). Meanwhile, the manufacturing industry has 3.3, 2.6 and 1.7 years as the averages of the R&D cycle time, respectively, in the three periods. Thus, the <sup>fi</sup>gure visually explains that the R&D cycle time of the IT industry is longer than that of the manufacturing industry. The R&D cycle time shows an opposite result to the market cycle time. This result implies that the IT industry needs more time for R&D than the manufacturing industry because R&D activities in the IT industry need more advanced technology than those in the manufacturing industry.

Figs. 4 and 5 visually indicate that the IT industry needs to produce constantly new products for their survival purposes under a short market cycle time and a long R&D cycle time, compared with the manufacturing industry. The IT industry faces a high rate of change in technology and market conditions. Accordingly, this study can consider that the industry is a high-clock speed industry. As a result, the R&D process of the IT industry needs more time (so, more cost) than that of the manufacturing industry. Consequently, the R&D expenditure is important but not essential in the IT industry.

## 4.5. Classification accuracy on validation sample

Fig. 6 depicts a visual relationship between DEA–DA and training/ validation samples. Tables 6 and 7 document the classi<sup>fi</sup>cation accuracy of the three approaches on the two validation samples. The two tables indicate that DEA–DA outperforms the logit and probit regressions in terms of classi<sup>fi</sup>cation accuracy. For example, Table 6 exhibits that DEA–DA has 58.50% in the classi<sup>fi</sup>cation accuracy (measured by a correct classi<sup>fi</sup>cation rate) on the validation sample of the manufacturing industry. Meanwhile, the corresponding classi<sup>fi</sup>cation accuracies of logit and probit regressions are 47.72% and 48.02%, respectively. Table 7 shows a similar result on the classi<sup>fi</sup>cation accuracy on the three approaches. The validation sample is separated into two groups (above unity in Tobin q and below unity in Tobin's q). The correct classi<sup>fi</sup>cation rate indicates the number of observations (<sup>fi</sup>rms) classi<sup>fi</sup>ed correctly divided by the number of each validation sample.

Correlation matrix (manufacturing industry).

<table><tr><td></td><td>R&amp;D I</td><td>NIOR</td><td>LISER</td><td>Gror1</td><td>Exec</td><td>DPR</td></tr><tr><td>R&amp;D I</td><td>1.00</td><td>-0.30</td><td>-0.15</td><td>-0.02</td><td>-0.01</td><td>-0.01</td></tr><tr><td>NIOR</td><td></td><td>1.00</td><td>-0.16</td><td>0.09</td><td>0.14</td><td>0.01</td></tr><tr><td>LISER</td><td></td><td></td><td>1.00</td><td>-0.06</td><td>-0.10</td><td>-0.03</td></tr><tr><td>Gror1</td><td></td><td></td><td></td><td>1.00</td><td>0.01</td><td>0.00</td></tr><tr><td>Exec</td><td></td><td></td><td></td><td></td><td>1.00</td><td>-0.01</td></tr><tr><td>DPR</td><td></td><td></td><td></td><td></td><td></td><td>1.00</td></tr></table>

(a) The eigenvalues of <sup>fi</sup>nancial factors are R&D I=898.93, NIOR=377.14, LISER=780.20, Gror1=649.09, Exec=572.64 and DPR=658.00, respectively. The eigenvalues indicate no occurrence of multicollinearity among <sup>fi</sup>nancial factors because they are much larger than zero.

Table 3  
Correlation matrix (IT industry).

<table><tr><td></td><td>R&amp;D I</td><td>NIOR</td><td>LISER</td><td>Gror1</td><td>Exec</td><td>DPR</td></tr><tr><td>R&amp;D I</td><td>1.00</td><td>0.07</td><td>-0.08</td><td>-0.05</td><td>-0.06</td><td>0.04</td></tr><tr><td>NIOR</td><td></td><td>1.00</td><td>-0.07</td><td>-0.03</td><td>0.22</td><td>0.04</td></tr><tr><td>LISER</td><td></td><td></td><td>1.00</td><td>-0.01</td><td>-0.06</td><td>0.00</td></tr><tr><td>Gror1</td><td></td><td></td><td></td><td>1.00</td><td>0.06</td><td>-0.57</td></tr><tr><td>Exec</td><td></td><td></td><td></td><td></td><td>1.00</td><td>-0.06</td></tr><tr><td>DPR</td><td></td><td></td><td></td><td></td><td></td><td>1.00</td></tr></table>

(a) The eigenvalues of <sup>fi</sup>nancial factors are R&D I=440.25, NIOR=519.56, LISER=377.17, Gror1=657.01, Exec=305.58 and DPR=178.43, respectively. The eigenvalues indicate no occurrence of multicollinearity among <sup>fi</sup>nancial factors because they are much larger than zero.

It is a common practice in statistics that a training sample should be twice larger than a validation sample. This study uses the 25% cutoff criterion to separate a total sample into half-and-half because of the imprecision in Tobin's q ratio. The research of Chung and Wright [12] has proposed such a data treatment. Thus, the proposed data treatment can be considered as a special case because this study needs to deal with a <sup>fi</sup>nancial data set related to Tobin's q ratio.

## 4.6. Kruskal–Wallis rank sum test

To examine statistically the third and fourth hypotheses, this study uses the Kruskal–Wallis rank sum test. The whole data set is separated into T groups. To compute the Kruskal–Wallis statistic (H), this study ranks all <sup>fi</sup>rms $\left( n = \sum _ { t = 1 } ^ { T } { n _ { t } } ^ { t } \right)$ in T groups from the greatest to the least by their Altman's Z scores. Here, n stands for the number of <sup>fi</sup>rms in the t-th group. Let $R _ { j t }$ denote the rank of the j-th <sup>fi</sup>rm in the t-th group. The rank sum of all <sup>fi</sup>rms in the t-th group is $\begin{array} { r } { R _ { t } = \sum _ { j = 1 } ^ { n _ { t } } R _ { j t } . } \end{array}$ Then, the Kruskal–Wallis statistic (H) is determined by

Results of DEA–DA and logit/probit models (manufacturing industry).

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Top 25% and bottom 25%DEA-DA</td></tr><tr><td>1 Stage</td><td>2 Stage</td><td>Logit</td><td>Probit</td></tr><tr><td rowspan="7">Variables</td><td>Constant</td><td>-0.035</td><td>-0.056</td><td>-0.028</td><td>-0.007</td></tr><tr><td>R&amp;D I</td><td>0.107</td><td>0.207</td><td>1.070***(0.268)</td><td>0.641***(0.256)</td></tr><tr><td>NITR</td><td>0.022</td><td>0.408</td><td>0.690***(0.172)</td><td>0.359***(0.143)</td></tr><tr><td>LISE</td><td>-0.129</td><td>0.205</td><td>0.186(0.046)</td><td>0.103(0.041)</td></tr><tr><td>Gror1</td><td>-0.036</td><td>0.027</td><td>0.378***(0.094)</td><td>0.216***(0.086)</td></tr><tr><td>Exec</td><td>-0.038</td><td>-0.154</td><td>-0.108(-0.027)</td><td>-0.069(-0.028)</td></tr><tr><td>DPR</td><td>-0.667</td><td>-0.000</td><td>-1.676*(-0.419)</td><td>-0.971*(-0.388)</td></tr><tr><td rowspan="3">Correct Classification Rate</td><td>High q firms</td><td colspan="2">81.10%</td><td>65.24%</td><td>64.63%</td></tr><tr><td>Low q firms</td><td colspan="2">71.95%</td><td>74.39%</td><td>74.39%</td></tr><tr><td>Total firms</td><td colspan="2">76.52%</td><td>69.82%</td><td>69.51%</td></tr><tr><td rowspan="3">Number of Observations</td><td>High q firms</td><td colspan="2"></td><td>164</td><td></td></tr><tr><td>Low q Firms</td><td colspan="2"></td><td>164</td><td></td></tr><tr><td>Total Firms</td><td colspan="2"></td><td>328</td><td></td></tr></table>

(a) The number within () indicates a marginal effect of each parameter measured by logit and probit regressions. Note that this study normalizes a data set for a use of the two regressions. The marginal effect (0.268) of R&D I indicates that if an observation increases an amount of R&D intensity by a single standard deviation of the data then the probability for the observation to be classi<sup>fi</sup>ed into G1 (the high q group) increases by 0.268.  
(b) The symbols (\*\*\* and \*) indicate a signi<sup>fi</sup>cance level of 1% and 10%, respectively.

Results of DEA–DA and logit/probit models (IT industry).

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Top 25% and bottom 25%DEA-DA</td></tr><tr><td>1 Stage</td><td>2 Stage</td><td>Logit</td><td>Probit</td></tr><tr><td rowspan="7">Variables</td><td>Constant</td><td>-0.185</td><td>-0.013</td><td>0.262</td><td>0.170</td></tr><tr><td>R&amp;D I</td><td>0.091</td><td>0.102</td><td>0.932***(0.229)</td><td>0.566***(0.223)</td></tr><tr><td>NITR</td><td>0.161</td><td>0.256</td><td>1.338***(0.329)</td><td>0.679***(0.267)</td></tr><tr><td>LISE</td><td>0.038</td><td>0.000</td><td>0.245(0.060)</td><td>0.146(0.057)</td></tr><tr><td>Gror1</td><td>0.555</td><td>0.347</td><td>1.571(0.386)</td><td>1.072(0.422)</td></tr><tr><td>Exec</td><td>-0.070</td><td>0.000</td><td>-0.256(-0.063)</td><td>-0.140(-0.055)</td></tr><tr><td>DPR</td><td>-0.086</td><td>0.295</td><td>-0.268(-0.066)</td><td>-0.227(-0.089)</td></tr><tr><td rowspan="3">Correct Classification Rate</td><td>High q firms</td><td colspan="2">69.23%</td><td>66.35%</td><td>66.35%</td></tr><tr><td>Low q firms</td><td colspan="2">87.50%</td><td>73.08%</td><td>73.08%</td></tr><tr><td>Total firms</td><td colspan="2">78.50%</td><td>69.71%</td><td>69.71%</td></tr><tr><td rowspan="3">Number of Observations</td><td>High q firms</td><td colspan="2"></td><td>104</td><td></td></tr><tr><td>Low q firms</td><td colspan="2"></td><td>104</td><td></td></tr><tr><td>Total firms</td><td colspan="2"></td><td>208</td><td></td></tr></table>

(a) See the footnote under Table 4.

$$
H = \frac {1 2}{n (n + 1)} \sum_ {t = 1} ^ {T} \frac {R _ {t} ^ {2}}{n _ {t}} - 3 (n + 1)\tag{9}
$$

The statistic (H) follows the $\chi ^ { 2 }$ distribution with T-1 degrees of freedom. See Hollander and Wolfe [26] for both a detailed description on the H statistic and a description regarding how to deal with an occurrence of multiple <sup>fi</sup>rms on a same rank.

![](/api/attachments/8KKTWKXM/fulltext/images/7842ffaee6cfb906b85c78b19be8a0a9c163c615578f5a872c1a8e5fcff2d897.jpg)  
Fig. 4. Market cycle time. Source: Japan Federation of Economic Organization (1998) and Minister of Economy, Trade and Industry (METI: 2007).

![](/api/attachments/8KKTWKXM/fulltext/images/7c615081fe522a7b5ac7059e9c7c467410a1624e88b9a84d07d565d558bf2083.jpg)  
Fig. 5. R&D cycle time. Source: Japan Federation of Economic Organization (1998) and Ministry of Economy, Trade and Industry (METI: 2007).

Returning to Eq. (8), this study computes the Altman's Z score of <sup>fi</sup>rms in the manufacturing industry by the following equation:

$$
\begin{array}{r l} \frac {3 2 8}{3 2 8 + 2 9 0} (0. 1 0 7 * \mathrm{R} \& \mathrm{DI} + 0. 0 2 2 * \mathrm{NITR} - 0. 1 2 9 * \mathrm{LISE} \\ & - 0. 0 3 6 * \text {Gror} 1 - 0. 0 3 8 * \text {Exec} - 0. 6 6 7 * \text {DPR}) \\ & + \frac {2 9 0}{3 2 8 + 2 9 0} (0. 2 0 7 * \mathrm{R} \& \mathrm{DI} + 0. 4 0 8 * \mathrm{NITR} + 0. 2 0 5 * \text {LISE} \\ & + 0. 0 2 7 * \text {Gror} 1 - 0. 1 5 4 * \text {Exec} - 0. 0 0 0 * \text {DPR}) \end{array}
$$

Here, 328 indicate the total number of whole observations and 290 indicate the number of observations existing in the overlap between the two groups (G1 and G2). Table 4 lists such weight estimates.

In the similar manner, Eq. (8) for the IT industry becomes as follows:

$$
\begin{array}{r l} \frac {2 0 8}{2 0 8 + 1 6 0} (0. 0 9 1 * \mathrm{R} \& \mathrm{DI} + 0. 1 6 1 * \mathrm{NITR} + 0. 0 3 8 * \mathrm{LISE} \\ & + 0. 5 5 5 * \text {Gror} 1 - 0. 0 7 0 * \text {Exec} - 0. 0 8 6 * \text {DPR}) \\ & + \frac {1 6 0}{2 0 8 + 1 6 0} (0. 1 0 2 * \mathrm{R} \& \mathrm{DI} + 0. 2 5 6 * \mathrm{NITR} + 0. 0 0 0 * \text {LISE} \\ & + 0. 3 4 7 * \text {Gror} 1 + 0. 0 0 0 * \text {Exec} + 0. 2 9 5 * \text {DPR}) \end{array}
$$

Here, 208 indicate the total number of whole observations and 160 indicate the number of observations existing in an overlap between the two groups (G1 and G2). See Table 5 that lists the weight estimates of the IT <sup>fi</sup>rms.

![](/api/attachments/8KKTWKXM/fulltext/images/6efe9da679899851c2d64eb0a8074ff11661e80406d2aba1e337c2a27f16f498.jpg)  
Fig. 6. Training and validation samples.

Table 7  
Table 6  
Classi<sup>fi</sup>cation accuracy of three approaches (manufacturing industry).

<table><tr><td></td><td>DEA-DA</td><td>Logit</td><td>Probit</td></tr><tr><td>Correct classification rate</td><td>58.50%</td><td>47.72%</td><td>48.02%</td></tr><tr><td>Misclassification rate</td><td>41.50%</td><td>52.28%</td><td>51.98%</td></tr></table>

Table 8 indicates the rank sum and the average rank of manufacturing <sup>fi</sup>rms. This study applies the Kruskal–Wallis rank sum test to examine the null hypothesis (i.e., there is no difference among the <sup>fi</sup>nancial performance of the three groups). As listed in the last row of Table 8, the H score (H=80.99) rejects the null hypothesis at the 1% level of signi<sup>fi</sup>- cance because 80.99>9.21 (the critical value of $\chi ^ { 2 }$ under two degrees of freedom). The Kruskal–Wallis rank sum test and Table 8 indicate that the three groups are different in their <sup>fi</sup>nancial performance. The average rank of the top 25% group is the best performer because it is the smallest among the three groups. The second group (between 50%) has the second average rank. The bottom 25% group is the last. Hence, the third hypothesis is valid in the manufacturing industry.

Table 9 indicates the rank sum and the average rank of the IT industry. This study applies the Kruskal–Wallis rank sum test to examine the null hypothesis. As listed in the last row of Table 9, the H score (H=65.51) rejects the null hypothesis at the 1% level of signi<sup>fi</sup>cance because 65.51>9.21 (the critical value of $\chi ^ { 2 }$ under two degrees of freedom). The Kruskal–Wallis rank sum test and Table 9 indicate that the three groups are different in their <sup>fi</sup>nancial performance. The average rank of the top 25% group is the best performer because it is the smallest among the three groups. The second is the average rank of the second group (between 50%). The bottom 25% group is the last. Hence, the third hypothesis is valid in the IT industry.

To examine the fourth hypothesis, we separate the whole data set into the three annual periods: April (2004)–March (2005), April (2005)– March (2006), and April (2006)–March (2007). Table 10 indicates the rank sum and the average rank of the manufacturing industry. This study applies the Kruskal–Wallis rank sum test to examine the null hypothesis (i.e., <sup>fi</sup>rms do not have any difference in their <sup>fi</sup>nancial performance over the three annual periods). As listed in the last row of Table 10, the H score (H=1.42) cannot reject the null hypothesis at the 5% level of signi<sup>fi</sup>cance because 1.42b5.99 (the critical value of $\chi ^ { 2 }$ under two degrees of freedom). The Kruskal–Wallis rank sum test indicates that <sup>fi</sup>rms are not different in their <sup>fi</sup>nancial performance over the three years. Hence, the fourth hypothesis is invalid in the manufacturing industry. However, the average rank decreases over time. This implies the technology improvement in the manufacturing industry even though we cannot statistically con<sup>fi</sup>rm such an improvement.

Table 11 indicates the rank sum and the average rank of the IT industry. This study applies the Kruskal–Wallis rank sum test to examine the null hypothesis. As listed in the last row of Table 11, the H score (H=3.19) obtained from Eq. (9) cannot reject the null hypothesis at the 5% level of signi<sup>fi</sup>cance because 3.19b5.99 (the critical value of $\chi ^ { 2 }$ under two degrees of freedom). The Kruskal–Wallis rank sum test indicates that <sup>fi</sup>rms are not different in their <sup>fi</sup>nancial performance over the three periods. Hence, the fourth hypothesis is invalid in the IT industry, as well. However, the average rank decreases over time. This implies that the technology improves in the IT industry even though we cannot statistically con<sup>fi</sup>rm such an improvement.

Classi<sup>fi</sup>cation accuracy of three approaches (IT industry).

<table><tr><td></td><td>DEA-DA</td><td>Logit</td><td>Probit</td></tr><tr><td>Correct classification rate</td><td>57.77%</td><td>33.01%</td><td>33.98%</td></tr><tr><td>Misclassification rate</td><td>42.23%</td><td>66.99%</td><td>66.02%</td></tr></table>

Table 8  
Rank sum and average rank (manufacturing industry).

<table><tr><td></td><td>Rank sum</td><td>Avg. rank</td></tr><tr><td>Top 25%</td><td>38,949</td><td>237</td></tr><tr><td>Between (50%)</td><td>107,345</td><td>326</td></tr><tr><td>Bottom 25%</td><td>69,859</td><td>426</td></tr><tr><td></td><td colspan="2">H=80.99</td></tr></table>

## 5. Conclusion and future extensions

This study discussed a use of DEA–DA to assess the corporate value of Japanese IT and manufacturing <sup>fi</sup>rms. The DEA–DA needs to prescribe group classi<sup>fi</sup>cation before its application. This study used Tobin's q ratio, as the classi<sup>fi</sup>cation criterion, to measure their <sup>fi</sup>nancial performance. In extending DEA–DA to <sup>fi</sup>nancial performance assessment, we explored a linkage between DEA–DA (as a methodology) and Tobin's q (as a theoretical basis) via the measurement of Altman's Z score (as a <sup>fi</sup>- nancial performance score). The Z score is a well-known measure for bankruptcy prediction. This study extended the Z score from the bankruptcy prediction to the corporate value assessment. The Z score provides us with aggregated information regarding <sup>fi</sup>nancial ratios and other <sup>fi</sup>nancial measures that many individuals usually examine when they make their investment decisions. In addition, this study combined the proposed approach with the Kruskal–Wallis rank sum test in order to examine statistically the four null hypotheses related to Japanese IT and manufacturing <sup>fi</sup>rms.

The proposed use of DEA–DA based upon Tobin's q ratio has provided the following four business implications: First, the R&D expenditure increases the corporate value (measured by Tobin'q ratio) of Japanese IT and manufacturing <sup>fi</sup>rms. Second, the impact of R&D expenditure on the manufacturing industry is larger than that of the IT industry because the weight and parameter estimate of the R&D I in DEA–DA and logit/ probit regressions for the manufacturing industry is larger than those of the IT industry. This result is because the two industries have a difference in their R&D cycle time and market cycle time. That is, the R&D cycle time of the IT industry is longer than that of the manufacturing industry. In contrast, the market cycle time of the IT industry is shorter than that of the manufacturing industry. The R&D expenditure may save the manufacturing industry from a <sup>fi</sup>nancial dif<sup>fi</sup>culty, but it may not save the IT industry from the <sup>fi</sup>nancial dif<sup>fi</sup>culty. In other words, the R&D expenditure is indeed an important factor both to improve the corporate value of the manufacturing industry and to reduce a possible occurrence of bankruptcy. However, the IT industry needs not only the R&D expendi ture but also other management factors (e.g., the reduction in R&D cycle time) to avoid a <sup>fi</sup>nancial dif<sup>fi</sup>culty and bankruptcy at the worst case. Third, this study followed the classi<sup>fi</sup>cation proposed by Chung and Wright [12] that separated sample companies into the high q group (the top 25% of Tobin's q) and the low q group (the bottom 25% of Tobin's q). The rank sum test con<sup>fi</sup>rmed that the classi<sup>fi</sup>cation method overcame the methodological drawback of Tobin's q ratio due to its imprecision. Fourth, the rank sum test con<sup>fi</sup>rmed that <sup>fi</sup>rms were not different in their <sup>fi</sup>nancial performance over the observed periods even though we found the technology improvement in the Japanese IT and manufacturing <sup>fi</sup>rms. This result supported that this study treated a time-series data set as a single pooled data set. In other words, this study can combine all data sets in the observed annual periods and treat the combined data as a single cross-sectional data for the proposed approach.

Table 9  
Rank sum and average rank (IT industry).

<table><tr><td></td><td>Rank sum</td><td>Avg. rank</td></tr><tr><td>Top 25%</td><td>13,182</td><td>127</td></tr><tr><td>Between (50%)</td><td>46,833</td><td>227</td></tr><tr><td>Bottom 25%</td><td>25,890</td><td>249</td></tr><tr><td></td><td colspan="2">H=65.51</td></tr></table>

Table 10  
Rank sum and average rank from 2004 to 2007 (manufacturing industry).

<table><tr><td></td><td>Rank sum</td><td>Avg. rank</td></tr><tr><td>2004–2005</td><td>74,226</td><td>339</td></tr><tr><td>2005–2006</td><td>72,402</td><td>331</td></tr><tr><td>2006–2007</td><td>69,525</td><td>317</td></tr><tr><td></td><td></td><td>H = 1.42</td></tr></table>

Table 11  
Rank sum and average rank from 2004 to 2007 (IT industry).

<table><tr><td></td><td>Rank sum</td><td>Avg. rank</td></tr><tr><td>2004–2005</td><td>30,626</td><td>222</td></tr><tr><td>2005–2006</td><td>28,063</td><td>203</td></tr><tr><td>2006–2007</td><td>27,216</td><td>197</td></tr><tr><td></td><td></td><td>H = 3.19</td></tr></table>

It is indeed true that the proposed approach is not perfect. This study has future research agendas, all of which need to be overcome in the near future. First, it is necessary for us to extend DEA–DA in such a manner that it can deal with the classi<sup>fi</sup>cation of more than two groups. That is a methodological drawback of the current structure of DEA–DA. Furthermore, the proposed use of DEA–DA for Tobin's q assessment is applicable to other industries in Japan and other nations such as the United States and European countries. Such research extensions will be able to enhance the methodological validity of the proposed approach.

Finally, it is hoped that this study contributes in the performance analysis of DEA–DA. We look forward to seeing future extensions as discussed in this study.

## Acknowledgment

The authors thank Dr. A Whinston, Ms. V. Whinston and <sup>fi</sup>ve reviewers whose comments have improved the quality of this study. This work is supported by JSPS Grant-in-Aid for Scienti<sup>fi</sup>c Research (C) 24530287.

## References

[1] P.L. Adad, W.J. Banks, New LP-based heuristics for the classi<sup>fi</sup>cation problem European Journal of Operational Research 67 (1993) 88–100.

[2] P. Ahluwalia, U. Varshney, Composite quality of service and decision making perspective in wireless networks, Decision Support Systems 46 (2009) 542–551.

[3] E.I. Altman, Financial ratios, discriminant analysis and the prediction of corporate bankruptcy, Journal of Finance 23 (1968) 589–609.

[4] S.M. Bajgier, A.V. Hill, A comparison of statistical and linear programming approaches to the discriminant problem, Decision Sciences 13 (1982) 604–618.

[5] J.S. Benamati, A.L. Lederer, Decision support systems infrastructure: the root problems of management of changing IT, Decision Support Systems 45 (2008) 833–844.

[6] S. Benartzi, R. Michaely, R.H. Thaler, Do changes in dividends signal the future or the past? Journal of Finance 52 (1997) 1007–1034.

[7] E.W.N. Bernroider, V. Stix, Pro<sup>fi</sup>le distance method—a multi-attribute decision making approach for information system investments, Decision Support Systems 42 (2006) 988–998.

[8] M. Better, F. Glover, M. Samorani, Classi<sup>fi</sup>cation by vertical and cutting multihyperplane decision tree induction, Decision Support Systems 43 (2010) 430-436

[9] L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classi<sup>fi</sup>cation and Regression Trees, Wadsworth, Inc., Belmont, CA. USA. 1984.

[10] T.M. Cavalier, J.P. Ignizio, A.L. Soyster, Discriminant analysis via mathematical programming: certain problems and their causes, Computers and Operations Research 16 (1989) 353-362

[11] A. Charnes, W.W. Cooper, R.O. Ferguson, Optimal estimation of executive compensation by linear programming, Management Science 1 (1955) 138–151.

[12] K.H. Chung, P. Wright, Corporate policy and market value: a q-theory approach, Review of Quantitative Finance and Accounting 11 (1998) 293–310.

[13] M. Doumpos, S.H. Zanakis, C. Zopounidis, Multicriteria preference disaggregation for classi<sup>fi</sup>cation problems with an application to global investing risk, Decision Sciences 32 (2001) 333–385.

[14] A.P. Duarte Silva, A. Stam, Second-order mathematical programming formulations for discriminant analysis, European Journal of Operational Research 74 (1994) 4–22.

[15] K.M. Eisenhardt, B.N. Tabrizi, Accelerating adaptive process: product innovation in the global computer industry, Administrative Science Quarterly 40 (1995) 84–110

[16] J.E. Falk, V.E. Karlov, Robust separation of <sup>fi</sup>nite sets via quadratics, Computers and Operations Research 28 (2001) 537–561.

[17] R.H. Fine, Clock Speed-Winning Industry Control in the Age of Temporary Advantage, Preseus Books, Massachusetts, 1998.

[18] R.A. Fisher, The use of multiple measurements in taxonomy problems, Annals of Eugenics 7 (1936) 179–188

[19] H. Fraydman, E. Altman, D. Kao, Introducing recursive partitioning for <sup>fi</sup>nancial classi<sup>fi</sup>cation: the case of <sup>fi</sup>nancial distress, Journal of Finance 40 (1985) 269–291.

[20] N. Freed, F. Glover, A linear programming approach to the discriminant problem, Decision Sciences 12 (1981) 68–74

[21] N. Freed, F. Glover, Simple but powerful goal programming models for discriminant problems, European Journal of Operational Research 7 (1981) 44–60.

[22] F. Glover, Improved linear programming models for discriminant analysis, Decision Sciences 21 (1990) 771–785.

[23] M. Goto, Financial performance analysis of US and world telecommunications companies: importance of information technology in the telecommunications industry after the AT&T breakup and the NTT divesture, Decision Support Systems 43 (2010) 447–456.

[24] T. Han, C. Woo, J.L. Zhao, Recent advances in information technology and systems in the internet-era: introduction to the WITS'05 special issue for decision support systems, Decision Support Systems 45 (2008) 663–664.

[25] M.G. Heinz, S. Colburn, L.H. Carney, Evaluating auditory performance limits: I and II, Neural Computation 13 (2001) 2273–2338.

[26] M. Hollander, D.A. Wolfe, Nonparametric Statistical Methods, John Wiley, New York, 1999.

[27] B.A. Jain, B.N. Nag, Arti<sup>fi</sup>cial neural network models for pricing initial public offerings, Decision Sciences 26 (1995) 283–302.

[28] M.C. Jensen, Agency costs of free cash <sup>fl</sup>ow, corporate <sup>fi</sup>nance and takeovers, American Economic Review 76 (1986) 323–329.

[29] M.C. Jensen, Eclipse of the public corporation, Harvard Business Review 67 (1986) 61–74.

[30] C. Kao, S.-N. Hwang, Ef<sup>fi</sup>ciency measurement for network systems: IT impact on <sup>fi</sup>rm performance, Decision Support Systems 43 (2010) 437–446.

[31] R. La Porta, F. Lopez-de-Silanes, A. Shleifer, R. Vishny, Investor protection and corporate valuation, Journal of Finance 57 (2002) 1147–1170.

[32] K.F. Lam, J.W. Moy, An experimental comparison of some recently developed linear programming approaches to the discriminant problem, Computers and Operations Research 24 (1997) 593–599.

[33] W.T. Lin, The business value of information technology as measured by technical ef<sup>fi</sup>ciency: evidence from country-level data, Decision Support Systems 46 (2009) 865–874.

[34] D.N. Mallick, R.G. Schroeder, An integrated framework for measuring product development performance in high technology industries, Production and Operation Management 14 (2005) 142-158.

[35] O.L. Mangasarian, Arbitrary-norm separating plane, Operations Research Letters 24 (1999)15-23.

[36] C.A. Markowski, E.P. Markowski, An experimental comparison of several approaches to the discriminant problem with both qualitative and quantitative variables, European Journal of Operational Research 28 (1987) 74–78

[37] C.A. Markowski, C.T. Ragsdale, Combining neural network and statistical predictions to solve the classi<sup>fi</sup>cation problem in discriminant analysis, Decision Sciences 26 (1995) 229–242.

[38] J.J. McConnell, H. Servaes, Additional evidence on equity ownership and corporate value, Journal of Financial Economics 27 (1990) 595–612.

[39] J.J. McConnell, H. Servaes, Equity ownership and the two faces of debt, Journal of Financial Economics 39 (1995) 131–157.

[40] D. McFadden, Conditional logit analysis of qualitative choice behavior, in: P. Zarembka (Ed.), Frontier in Econometrics, Academic Press, New York, 1973.

[41] D. McFadden, Econometric models for probabilistic choice, Journal of Business 53 (1980) 513–529.

[42] H. Mendelson, R.R. Pillai, Industry clockspeed: measurement and operational implications, Manufacturing and Service Operations Management 1 (1999) 1–20.

[43] P.A. Rubin, Heuristic solution procedures for a mixed-integer programming discriminant model, Managerial and Decision Economics 11 (1990) 255–266.

[44] H. Servaes, The value of diversi<sup>fi</sup>cation during the conglomerate merger wave, Journal of Finance 51 (1996) 1201–1225.

[45] C.A.B. Smith, Some examples of discrimination, Annals of Eugenics 13 (1947) 272–282.

[46] A. Stam, Nontraditional approaches to statistical classi<sup>fi</sup>cation: some perspectives on L -norm methods, Annals of Operations Research 74 (1997) 1–36.

[47] A. Stam, E.A. Joachimsthaler, Solving the classi<sup>fi</sup>cation problem via linear and nonlinear programming methods, Decision Sciences 20 (1989) 285–293.

[48] T. Sueyoshi, Mixed integer programming approach of extended-discriminant analysis, European Journal of Operational Research 152 (2004) 45–55.

[49] T. Sueyoshi, DEA-discriminant analysis: methodological comparison among eight discriminant analysis approaches, European Journal of Operational Research 169 (2006) 247–272.

[50] T. Sueyoshi, Financial ratio analysis of the electric power industry, Asia-Paci<sup>fi</sup>c Journal of Operational Research 22 (2005) 349–376.

[51] T. Sueyoshi, M. Goto, Can R&D expenditure spending avoid corporate bankruptcy? Comparison between Japanese machinery and electric equipment industries using DEA-discriminant analysis, European Journal of Operational Research 196 (2009) 289–311.

[52] T. Sueyoshi, M. Goto, DEA-DA for bankruptcy-based performance assessment: misclassi<sup>fi</sup>cation analysis of the Japanese construction industry, European Journa of Operational Research 199 (2009) 576–594.

[53] T. Sueyoshi, M. Goto, Methodological comparison between DEA (data envelopment analysis) and DEA–DA (discriminant analysis) from the perspective of bankruptcy as sessment, European Journal of Operational Research 199 (2009) 561–575.

[54] K.Y. Tam, M.Y. Kiang, Managerial applications of neural networks: the case of bank failure, Management Science 38 (1992) 926–947.

[55] J. Tobin, A general equilibrium approach to monetary theory, Journal of Money, Credit, and Banking 1 (1969) 15–29.

[56] J. Tobin, Monetary policies and the economy: the transmission mechanism, Southern Economic Journal 44 (1978) 421-431.

[57] J.M. We, Natural discriminant analysis using interactive Potts models, Neural Computation 14 (2002) 689–713.

[58] J.M. Wilson, Integer programming formulation of statistical classi<sup>fi</sup>cation problems, Omega: International Journal of Management Science 24 (1996) 681–688.

[59] N. Yanev, S. Balev, A combinatorial approach to the classi<sup>fi</sup>cation problem European Journal of Operational Research 115 (1999) 339–350.

[60] D. Yermack, Higher market valuation of companies with a small board of directors, Journal of Financial Economics 40 (1996) 185–211.

[61] D. Zhu, A hybrid approach for ef<sup>fi</sup>cient ensembles, Decision Support Systems 48 (2010) 480–487.

[62] C. Zopounidis, M. Doumpos, Multicriteria classi<sup>fi</sup>cation and sorting methods: a literature review, European Journal of Operational Research 138 (2002) 229–246.

T. Sueyoshi (the corresponding author) is a full professor at New Mexico Institute of Mining and Technology, Department of Management, 801 Leroy Place, Socorro, NM, 87801, USA. E-mail: toshi@nmt.edu, Tel: 1-575-835-6452, Fax: 1-575-835-5498. He obtained his Ph.D. from the University of Texas at Austin. He has published more than 200 articles in international journals.

M. Goto is a senior research economist at Central Research Institute of Electric Power Industry, 1-6-1, Otemachi, Chiyodaku, Tokyo 100-8126, Japan. e-mail: mika@criepi.denken.or.jp, Tel: 81-3-3201-6601, Fax:81-3-3201-6601. She obtained her Ph.D. from Nagoya Universit in Japan. She has published more than 30 articles in international journals.
