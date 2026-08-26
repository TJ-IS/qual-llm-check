---
otero_id: 8598
otero_key: "TXUU5YME"
title: "A multi-dimensional fuzzy decision support strategy"
authors: "Qimi Jiang; Chun-Hsien Chen"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.08.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A multi-dimensional fuzzy decision support strategy

Qimi Jiang\*, Chun-Hsien Chen

School of Mechanical and Production Engineering, Nanyang Technological University, 50 Nanyang Avenue, Singapore 639798, Singapore

Received 1 December 2002; accepted 1 August 2003

Available online 13 November 2003

## Abstract

Based on the theory of fuzzy pattern recognition and fuzzy optimization, this paper presents a kind of multi-dimensional fuzzy decision support strategy for multi-objective and multi-layer fuzzy decision support systems. Compared with conventional strategies of fuzzy optimization that just considers the relative membership u of decision j of down layer unit systems, this strategy also takes the relative bad membership $\displaystyle { \dot { \bar { u } } _ { j } = 1 - u _ { j } }$ as the input of up layer unit systems. Besides, unlike conventional strategies of fuzzy optimization, this strategy can provide multi-dimensional information to the decision-maker. With these advantages, this strategy founds a new theoretical basis for the multi-dimensional decision making of large systems <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Multi-dimensional; Fuzzy decision support strategy; Multi-objective and multi-layer system

## 1. Introduction

Fuzzy logic is increasingly used in decision-aided systems because it offers several advantages over other traditional decision making techniques. The fuzzy decision support systems can easily deal with incomplete and/or imprecise knowledge applied to either linear or nonlinear problems. These systems have successfully been applied to many different problems such as predictive maintenance [2], tool conditions monitoring [1], job dispatching [3], tolerance allocation [6], diagnosis decision [7], etc.

Recently, research in the domain of fuzzy decision support technology focuses on the following aspects. Williams and Steele [12] used prototypical decision classes as a basis for fuzzy decision support. Pierre and Philippe [10] described the practical implementation of the fuzzy decision support system and its interface to assist economists in charge of the economic calculus. Tam et al. [11] applied non-structural fuzzy decision support system (NSFDSS) to facilitate the decision making process for multi-objective problems. And their modified NSFDSS is suitable for the appraisal of complex construction problems, which allows assessment based on a pair-wise comparison of alternatives using semantic operators, even under the condition that insufficient precise information is available. Baron et al. [4] presented a genetic algorithm that automatically constructs the knowledge base used by fuzzy decision support system. This genetic algorithm can produce an optimal approximation of a set of sampled data from a very small amount of input information. Mario et al. [9] applied the fuzzy decision support technique to equipment repair under battle conditions. Dash et al. [5] presented a new approach to identify transient power quality disturbances using linear combiners and a fuzzy decision support system.

Yu and Miroslaw [13] presented a multi-criterion decision strategy for quantitative constructability analysis based on a neuro-fuzzy knowledge-based system. In their work, a multi-layer information aggregation network was proposed to incorporate the manager’s subjective preference information.

Although some researchers like Yu and Miroslaw [13] did some work in multi-layer decision support systems, research issue on multi-objective and multilayer fuzzy decision support systems has not been well addressed. Li et al. [8] also presented a theoretical model for multi-dimensional fuzzy decision-making of multi-objective system. But their model is just a two-layer model, not a general multi-layer model. In this paper, based on the work of Li et al. [8], we focus on the investigation of a new multi-dimensional fuzzy decision support strategy applied to general multiobjective and multi-layer decision support systems. The presented strategy is based on the theory of fuzzy pattern recognition as well as fuzzy optimization. Compared with the conventional strategy of fuzzy optimization that just considers the relative membership $u _ { j }$ of decision j of down layer unit systems, this strategy also takes the relative bad membership $\stackrel { \mathrm { b } } { u _ { j } } = 1 - u _ { j }$ as the input of up layer unit systems. In other words, this strategy can utilize sufficiently the information coming from down layer unit systems. Besides, unlike the conventional strategy of fuzzy optimization that has only one-dimensional information, this strategy can provide multi-dimensional information. These advantages make it possible for the multi-dimensional decision making of large systems. The next section presents the principle of multidimensional fuzzy decision support strategy. Followed is a simple example just used for demonstrating the decision-making by use of the presented strategy.

## 2. Multi-dimensional fuzzy decision support strategy

Fig. 1 shows the structure between up and down layers of multi-dimensional fuzzy decision support strategy. Suppose there are n decisions (plans) in the system that form a decision set

$$
D = \left\{d _ {1}, d _ {2}, \dots , d _ {n} \right\}\tag{1}
$$

![](/api/attachments/TXUU5YME/fulltext/images/77f2fe0e5745874e4b5dd321b12c88fbb187941204a1cfa6ffa57c6adbcd648b.jpg)  
Fig. 1. Structure of multi-dimensional fuzzy decision support strategy.

To evaluate these plans, there are M objectives that form an evaluation objective set

$$
O = \left\{O _ {1}, O _ {2}, \dots , O _ {M} \right\}\tag{2}
$$

For multi-objective system, it is difficult to determine the weight values if single layer fuzzy decision strategy is adopted. So, to overcome this shortcoming, a multi-layer strategy is presented. According to the attribute of different objectives, the evaluation objectives of down layer are usually synthesized into several evaluation objectives of up layer. For example, if the evaluation objective set of down layer is expressed as

$$
O ^ {\mathrm{d}} = \left\{O _ {1} ^ {\mathrm{d}}, O _ {2} ^ {\mathrm{d}}, \dots , O _ {M \mathrm{d}} ^ {\mathrm{d}} \right\}\tag{3}
$$

Then, the Md evaluation objectives of down layer can be synthesized into Mu evaluation objectives of up layer, i.e.

$$
O ^ {\mathrm{u}} = \{O _ {1} ^ {\mathrm{u}}, O _ {2} ^ {\mathrm{u}}, \dots , O _ {M \mathrm{u}} ^ {\mathrm{u}} \}\tag{4}
$$

where

$$
O _ {i} ^ {\mathrm{u}} = \left\{O _ {1} ^ {\mathrm{d}}, O _ {2} ^ {\mathrm{d}}, \dots , O _ {m} ^ {\mathrm{d}} \right\}\tag{5}
$$

i.e. the evaluation objective i of up layer may contain m evaluation objectives of down layer.

If every decision has l evaluation levels that form an evaluation level set

$$
L = \left\{l _ {1}, l _ {2} \dots , l _ {l} \right\}\tag{6}
$$

$l _ { 1 }$ is the optimal decision, $l _ { 2 }$ is the sub-optimal decision and $l _ { l }$ is the most inferior decision.

2.1. Multi-dimensional fuzzy decision recognition strategy

Suppose the unit system k of down layer of the system contains m evaluation objectives, then the evaluation objective of decision j can be expressed as

$$
X _ {j} ^ {k} = (x _ {1 j} ^ {k}, x _ {2 j} ^ {k}, \dots , x _ {m j} ^ {k}) ^ {T}\tag{7}
$$

So the evaluation objectives of all n decisions of the unit system k will form a matrix as

$$
X ^ {k} = (x _ {i j} ^ {k})\tag{8}
$$

where $i = 1 , 2 , \cdot \cdot \cdot , m ; \ j = 1 , 2 , \cdot \cdot \cdot , n ; k = 1 , 2 , \cdot \cdot \cdot ,$ Mu; $x _ { i j } ^ { k }$ is the feature value of objective i and decision j of the unit system k. To eliminate the difference in quantity of the m evaluation objectives, it is necessary to make the following normalization process.

$$
f _ {i j} ^ {k} = \frac {x _ {i j} ^ {k} - x _ {i \mathrm{min}} ^ {k}}{x _ {i \mathrm{max}} ^ {k} - x _ {i \mathrm{min}} ^ {k}}\tag{9}
$$

or

$$
f _ {i j} ^ {k} = \frac {x _ {i \mathrm{max}} ^ {k} - x _ {i j} ^ {k}}{x _ {i \mathrm{max}} ^ {k} - x _ {i \mathrm{min}} ^ {k}}\tag{10}
$$

where $x _ { i \mathrm { m a x } } ^ { k }$ and $x _ { i \mathrm { m i n } } ^ { k }$ are the maximum and minimum feature values of objective i of unit system k, respectively, $f _ { i j } ^ { k }$ is the normalization value of $x _ { i j } ^ { k } .$ When the decision becomes better with the increase of the value of $f _ { i j } ^ { k } { : }$ , Eq. (9) is adopted. Otherwise, Eq. (10) is adopted.

From Eqs. (8), (9) and (10), a fuzzy matrix will be obtained as following

$$
F ^ {k} = (f _ {i j} ^ {k})\tag{11}
$$

where $i = 1 , 2 , \cdot \cdot \cdot , m ; \ j = 1 , 2 , \cdot \cdot \cdot , n ; k = 1 , 2 , \cdot \cdot \cdot , M \mathbf { u } .$ Suppose

$$
U ^ {k} = (u _ {p j} ^ {k})\tag{12}
$$

where $p { = } 1 , 2 , \cdot \cdot \cdot , l ; \ j { = } 1 , 2 , \cdot \cdot \cdot , n ; k { = } 1 , 2 , \cdot \cdot \cdot , M \mathbf { u } .$ $U ^ { k }$ is a multi-dimensional fuzzy decision recognition matrix. $u _ { p j } ^ { k }$ is the relative membership of decision j belonging to the standard decision pattern $p .$ It meets the following conditions.

$$
\left\{ \begin{array}{l} 0 \leq u _ {p j} ^ {k} \leq 1 \\ \sum_ {p = 1} ^ {l} u _ {p j} ^ {k} = 1 \end{array} \right.\tag{13}
$$

Suppose the standard objective fuzzy matrix can be expressed as

$$
S ^ {k} = (s _ {j p} ^ {k})\tag{14}
$$

$$
j = 1, 2, \dots , n; p = 1, 2, \dots , l; k = 1, 2, \dots , M u
$$

According to the relativity of decision evaluation, the evaluation objectives of the optimal and the most inferior decisions can be computed as

$$
\left\{ \begin{array}{l} S _ {1} ^ {k} = (s _ {1 1} ^ {k}, s _ {2 1} ^ {k}, \dots , s _ {m 1} ^ {k}) ^ {T} = \left(\bigvee_ {j = 1} ^ {n} r _ {1 j} ^ {k}, \bigvee_ {j = 1} ^ {n} r _ {2 j} ^ {k}, \dots , \bigvee_ {j = 1} ^ {n} r _ {m j} ^ {k}\right) ^ {T} \\ S _ {l} ^ {k} = (s _ {1 l} ^ {k}, s _ {2 l} ^ {k}, \dots , s _ {m l} ^ {k}) ^ {T} = \left(\bigwedge_ {j = 1} ^ {n} r _ {1 j} ^ {k}, \bigwedge_ {j = 1} ^ {n} r _ {2 j} ^ {k}, \dots , \bigwedge_ {j = 1} ^ {n} r _ {m j} ^ {k}\right) ^ {T} \end{array} \right.\tag{15}
$$

So, the evaluation objective of level $p$ decision pattern can be computed as

$$
S _ {i p} ^ {k} = S _ {i 1} ^ {k} + \frac {S _ {i l} ^ {k} - S _ {i 1} ^ {k}}{l - 1} (l - p)\tag{16}
$$

From Eqs. (15) and (16),

$$
S _ {p} ^ {k} = (S _ {1 p} ^ {k}, S _ {2 p} ^ {k}, \dots , S _ {m p} ^ {k}) ^ {T}\tag{17}
$$

Suppose the weight values of m evaluation objectives of decision j form a weight vector, i.e.

$$
W _ {j} ^ {k} = (w _ {1 j} ^ {k}, w _ {2 j} ^ {k}, \dots , w _ {m j} ^ {k}) ^ {T}\tag{18}
$$

where $( \Sigma _ { \mathrm { i } = 1 } ^ { m } w _ { i j } ^ { k } { = } 1 )$

To get the optimal fuzzy decision recognition matrix (12), build the following objective function minf $( u _ { p j } ^ { k } )$

$$
= \sum_ {j = 1} ^ {n} \min \left\{\sum_ {p = 1} ^ {l} \left[ u _ {p j} ^ {k} \left(\sum_ {i = 1} ^ {m} (w _ {i j} ^ {k} \mid r _ {i j} ^ {k} - s _ {i p} ^ {k} \mid) ^ {q}\right) ^ {1 / q} \right] ^ {2} \right\}\tag{19}
$$

Where q is a distance parameter, generally $q = 1$ or $q = 2$ . According to Eqs. (19) and (13), a Lagrange function will be made as

$$
L \left(u _ {p j} ^ {k}, \lambda\right) = \sum_ {p = 1} ^ {l} \left(u _ {p j} ^ {k}\right) ^ {2} d _ {p j} - \lambda \left(\sum_ {p = 1} ^ {l} u _ {p j} ^ {k} - 1\right)\tag{20}
$$

where

$$
d _ {p j} = \left[ \sum_ {i = 1} ^ {m} (w _ {i j} ^ {k}   |   r _ {i j} ^ {k} - s _ {i p} ^ {k}   |) ^ {q} \right] ^ {2 / q}.
$$

From Eq. (20),

$$
\frac {\partial L}{\partial u _ {p j} ^ {k}} = 2 u _ {p j} ^ {k} d _ {p j} - \lambda\tag{21}
$$

Make $( \partial L / \partial u _ { p j } ^ { k } ) { = } 0$ , then

$$
u _ {p j} ^ {k} = \frac {\lambda}{2 d _ {p j}}\tag{22}
$$

Similarly, from Eq. (20),

$$
\frac {\partial L}{\partial \lambda} = \sum_ {p = 1} ^ {l} u _ {p j} ^ {k} - 1\tag{23}
$$

Make (<sup>B</sup>L/<sup>B</sup>k) = 0, from Eqs. (22) and (23),

$$
\lambda = \frac {2}{\sum_ {p = 1} ^ {l} \frac {1}{d _ {p j}}}\tag{24}
$$

From Eqs. (22) and (24),

$$
u _ {p j} ^ {k} = \frac {1}{\sum_ {c = 1} ^ {l} \left[ \frac {\sum_ {i = 1} ^ {m} (w _ {i j} ^ {k} \mid r _ {i j} ^ {k} - s _ {i p} ^ {k} \mid) ^ {q}}{\sum_ {i = 1} ^ {m} (w _ {i j} ^ {k} \mid r _ {i j} ^ {k} - s _ {i c} ^ {k} \mid) ^ {q}} \right] ^ {2 / q}}\tag{25}
$$

where $i = 1 , 2 , \cdot \cdot \cdot , m ; \ j = 1 , 2 , \cdot \cdot \cdot , n ; k = 1 , 2 , \cdot \cdot \cdot , M u ;$ $p , c = 1 , \ 2 , \cdots , \ l .$ Eq. (25) is the multi-dimensional fuzzy decision recognition strategy of multi-objective unit systems. The fuzzy decision recognition matrix (12) can be computed from Eqs. (11), (15) f (18) and (25). Then, the multi-dimensional decision of unit system k can be made according to the principle of maximum membership. And the fuzzy decision recognition matrix $U ^ { k } ( k { = } 1 , ~ 2 , ~ \cdot ~ \cdot ~ , ~ t )$ of down layer computed by use of Eq. (25) will become the evaluation objectives of up layer.

## 2.2. Fuzzy relationship optimization strategy of multidimensional fuzzy decision

The output of down layer expressed by Eq. (12) can be used as the input of up layer. But this input information is not one-dimensional, but multi-dimensional. So the Eq. (25) is no longer suitable for the multi-dimensional fuzzy decision of up layer. However, up layer contains Mu evaluation objectives and every evaluation objective is a fuzzy relationship between the decision set D and the evaluation level set L. So, the information of multi-dimensional fuzzy decision of up layer can be obtained by way of synthesizing the Mu evaluation objectives using fuzzy relationship optimization of multi-objective systems.

Let $E ^ { i }$ denote the evaluation quota about objective i of up layer and make $( e _ { p j } ^ { i } ) { = } ( u _ { p j } ^ { i } )$ , then

$$
E ^ {i} = (e _ {p j} ^ {i}) = (u _ {p j} ^ {i})\tag{26}
$$

where $i = 1 , 2 , \cdot \cdot \cdot , M u ; p = 1 , 2 , \cdot \cdot \cdot , l ; j = 1 , 2 , \cdot \cdot \cdot , n .$ $E ^ { i }$ is referred as the fuzzy relationship matrix from L to D about objective i. If

$$
A ^ {i} = (a _ {p j} ^ {i}) = \left[ \begin{array}{c c c c} 1, & 1, & \dots , & 1 \\ 1, & 1, & \dots , & 1 \\ \dots & \dots & \dots & \dots \\ 1, & 1, & \dots , & 1 \end{array} \right]\tag{27}
$$

Then $\boldsymbol { A } ^ { i }$ is referred as the optimal decision fuzzy relationship matrix from L to D about objective i. If

$$
B ^ {i} = (b _ {p j} ^ {i}) = \left[ \begin{array}{c c c c} 0, & 0, & \dots , & 0 \\ 0, & 0, & \dots , & 0 \\ \dots & \dots & \dots & \dots \\ 0, & 0, & \dots , & 0 \end{array} \right]\tag{28}
$$

Then $B ^ { i }$ is referred as the most inferior decision fuzzy relationship matrix from L to D about objective i. Suppose the vector of objective weights is

$$
W = \left(w _ {1}, w _ {2}, \dots , w _ {M u}\right)\tag{29}
$$

where $( \Sigma _ { \mathrm { i = 1 } } ^ { M \mathrm { u } } w _ { i } { = } 1 )$

In the limited field L and D, there are $l \times n$ matches altogether. For match $( p , j )$ , the relationship of the relative membership of the optimal decision, $u _ { p j } ,$ and the relative membership of the most inferior decision, $u _ { p j } ^ { b } .$ , can be expressed as

$$
u _ {p j} + u _ {p j} ^ {b} = 1\tag{30}
$$

To compute the relative membership $u _ { p j } ,$ make the sum of squares of weighted general distances to be minimum in order to obtain the following objective function:

$$
\begin{array}{l} \min f (u _ {b j}) = \min \left\{(u _ {b j}) ^ {2} \left[ \sum_ {i = 1} ^ {M u} \left(w _ {i} \left(a _ {p j} ^ {i} - e _ {p j} ^ {i}\right)\right) ^ {q} \right] ^ {2 / q} \right. \\ \left. + (1 - u _ {p j}) ^ {2} \left[ \sum_ {i = 1} ^ {t} (w _ {i} (e _ {p j} ^ {i} - b _ {p j} ^ {i})) ^ {q} \right] ^ {2 / q} \right\} \end{array}\tag{31}
$$

From $( d f ( u _ { p j } ) / d u _ { p j } ) = 0$

$$
u _ {p j} = \frac {1}{1 + \left\{\frac {\sum_ {i = 1} ^ {M u} [ w _ {i} (1 - e _ {p j} ^ {i}) ] ^ {q}}{\sum_ {i = 1} ^ {M u} [ w _ {i} e _ {p j} ^ {i} ] ^ {q}} \right\} ^ {2 / q}}\tag{32}
$$

Eq. (32) is referred as the multi-dimensional fuzzy decision relationship optimization strategy of multiobjective systems.

For every fuzzy relationship matrix $E ^ { i } ( i = 1 , 2 , \cdots ,$ Mu), by use of Eq. (32), the following relative membership matrix will be got.

$$
U = (u _ {p j})\tag{33}
$$

where $p \ d = 1 , 2 , \cdot \cdot \cdot , l ; j \ d = 1 , 2 , \cdot \cdot \cdot , n .$

Eq. (33) is referred as the multi-dimensional fuzzy decision matrix of multi-objective systems. According to the maximum membership principle, the level of every decision can be determined by use of this equation.

2.3. Computing steps of multi-dimension fuzzy decision making

Shown as Fig. 2, the computational steps between up and down layers of multi-dimensional fuzzy decision-making are illuminated as follows:

Step 1 Multi-dimensional fuzzy decision-making of down layer:

Step 1.1 For every unit system of down layer, compute the objective normalization value by use of Eqs. (9) or (10) to get the fuzzy matrix $F ^ { k } .$

Step 1.2 To get $S _ { p } ^ { k } ,$ compute $S _ { 1 } ^ { k }$ and $S _ { l } ^ { k }$ by use of Eq. (15), then compute $S _ { i p } ^ { k }$ by use of Eq. (16).

Step 1.3 Compute the multi-dimensional fuzzy decision recognition matrix $\dot { U } ^ { k }$ by use of $\setminus F ^ { k } , \ S _ { p } ^ { k } , \ W _ { j } ^ { k }$ (determined by the user) and Eq. (25).

![](/api/attachments/TXUU5YME/fulltext/images/7a66f7f80d93b22c3cd372eacaafa50ef1c3e707d5ecbbc7d76e25cab3afbf02.jpg)  
Fig. 2. Computing steps of multi-dimensional decision-making.

Step 2 Multi-dimensional fuzzy decision-making of up layer: Step 2.1 Compute $E ^ { i }$ by use of Eq. (26). Step 2.2 Compute U by use of Eq. (32).

Step 3 Make decision according to the result of U.

## 3. A simple example

The presented strategy has been successfully applied to a very complex decision support system of a large petrochemical company. This is a joint research project between our group and the petrochemical company. However, our co-operator doesn’t agree to publish any details about this project. So, we replace it with a simple example to demonstrate the principle of the presented strategy. In the following, a general development system of some kind of product is taken as an application example. Generally, to develop a kind of product, there are many possible plans, i.e. decisions. Table 1 gives four possible plans, i.e. $D \mathrm { = } ( d _ { 1 } , d _ { 2 } , d _ { 3 } , d _ { 4 } )$ . Besides, Table 1 gives six objectives: concept design $o _ { 1 } { \mathrm { : } }$ detailed design $^ { O _ { 2 } , }$ , production preparation $o _ { 3 } ,$ production $O _ { 4 } ,$ assembly and debug $o _ { 5 }$ as well as test and modification $O _ { 6 } .$ These objectives fall into two subsystems: design $( o _ { 1 } , o _ { 2 } )$ and manufacture $( o _ { 3 } , \ o _ { 4 } , \ o _ { 5 } , \ o _ { 6 } )$ . To simplify the problem, the normalization value of each objective is given directly in Table 1. Suppose the evaluation level set $L { = } \{ l _ { 1 } , ~ l _ { 2 } , ~ l _ { 3 } \}$ , where $l _ { 1 }$ denotes the optimal plan, $l _ { 2 }$ the medium plan and $l _ { 3 }$ the most inferior plan.

## 3.1. The multi-dimensional fuzzy decision of subsystems (down layer)

As shown in Table 1, the product development system has two subsystems: design and manufacture. Take the design subsystem as a computing example. From Table 1, the objective normalization fuzzy matrix can be expressed as

$$
F ^ {d} = \left[ \begin{array}{c c c c} 0. 8 9 3 & 1 & 0. 5 3 8 & 0. 6 3 9 \\ 0. 8 1 5 & 1 & 0. 3 1 1 & 0. 2 3 1 \end{array} \right]
$$

From $\operatorname { E q } .$ . (15), the objective vectors of standard decision $l _ { 1 }$ and $l _ { 3 }$ can be computed as

$$
\left\{ \begin{array}{l} S _ {1} ^ {1} = (s _ {1 1} ^ {1}, s _ {2 1} ^ {1}) ^ {T} = (1, 1) ^ {T} \\ S _ {3} ^ {1} = (s _ {1 3} ^ {1}, s _ {2 3} ^ {1}) ^ {T} = (0. 5 3 8, 2 3 1) ^ {T} \end{array} \right.
$$

From Eq. (16), the objective vectors of standard decision $l _ { 2 }$ can be computed as

$$
S _ {2} ^ {1} = (s _ {1 2} ^ {1}, s _ {2 2} ^ {1}) ^ {T} = (0. 7 6 9, 0. 6 1 6) ^ {T}
$$

So

$$
S ^ {1} = \left[ \begin{array}{c c c} 1 & 0. 7 6 9 & 0. 5 3 8 \\ 1 & 0. 6 1 6 & 0. 2 3 1 \end{array} \right]
$$

Table 1  
Development system of some kind of product

<table><tr><td rowspan="2">Subsystem</td><td rowspan="2">Weight of subsystem</td><td rowspan="2">Objective</td><td rowspan="2">Weight of objective</td><td colspan="4">Normalization value of objective</td></tr><tr><td> $d_1$ </td><td> $d_2$ </td><td> $d_3$ </td><td> $d_4$ </td></tr><tr><td rowspan="2">Design ( $p_1$ )</td><td rowspan="2">0.425</td><td> $o_1$ </td><td>0.535</td><td>0.893</td><td>1</td><td>0.538</td><td>0.639</td></tr><tr><td> $o_2$ </td><td>0.465</td><td>0.815</td><td>1</td><td>0.311</td><td>0.231</td></tr><tr><td rowspan="4">Manufacture ( $p_2$ )</td><td rowspan="4">0.575</td><td> $o_3$ </td><td>0.215</td><td>1</td><td>0.143</td><td>0.779</td><td>0.832</td></tr><tr><td> $o_4$ </td><td>0.335</td><td>0.589</td><td>0.278</td><td>1</td><td>1</td></tr><tr><td> $o_5$ </td><td>0.184</td><td>1</td><td>0.428</td><td>0.148</td><td>0.783</td></tr><tr><td> $o_6$ </td><td>0.266</td><td>0.498</td><td>0.295</td><td>1</td><td>0.257</td></tr></table>

And

$$
W ^ {1} = (w _ {1} ^ {1}, w _ {2} ^ {1}) ^ {T} = (0. 5 3 5, 0. 4 6 5) ^ {T}
$$

From $E ^ { 1 } , W ^ { 1 } , S ^ { 1 }$ and Eq. (25), make $p { = } 2 ,$ , the multidimensional fuzzy decision matrix of the design subsystem can be computed as

$$
U ^ {d 1} = \left[ \begin{array}{c c c c} 0. 5 2 1 & 1. 0 0 0 & 0. 0 0 8 & 0. 0 1 6 \\ 0. 4 2 8 & 0. 0 0 0 & 0. 0 3 7 & 0. 0 7 2 \\ 0. 0 5 1 & 0. 0 0 0 & 0. 9 5 5 & 0. 9 1 2 \end{array} \right]
$$

From above matrix, for the design subsystem, the plan order from the optimal to the most inferior is $d _ { 2 } , d _ { 1 } , d _ { 4 }$ and $d _ { 3 }$ . Similarly, the multi-dimensional fuzzy decision matrix of the manufacture subsystem can be computed as

$$
U ^ {d 2} = \left[ \begin{array}{l l l l} 0. 2 6 4 & 0. 0 1 8 & 0. 4 8 6 & 0. 3 4 6 \\ 0. 6 0 3 & 0. 0 7 9 & 0. 4 0 1 & 0. 5 0 0 \\ 0. 1 3 2 & 0. 9 0 3 & 0. 1 1 3 & 0. 1 5 4 \end{array} \right]
$$

From above matrix, for the manufacture subsystem, the plan order from the optimal to the most inferior is $d _ { 3 } , d _ { 1 } , d _ { 4 }$ and $d _ { 2 }$

3.2. The multi-dimensional fuzzy decision of system (up layer)

The weight vector of the second layer is

$$
W ^ {u} = (0. 2 1 5, 0. 3 3 5, 0. 1 8 4, 0. 2 6 6) ^ {T}
$$

From Eq. (33), make $p { = } 2 ,$ , the multi-dimensional fuzzy decision matrix of up layer can be computed as

$$
U ^ {u} = \left[ \begin{array}{l l l l} 0. 2 1 2 & 0. 2 7 2 & 0. 2 7 7 & 0. 1 3 4 \\ 0. 6 1 0 & 0. 0 0 5 & 0. 1 8 9 & 0. 3 1 1 \\ 0. 0 1 7 & 0. 6 8 9 & 0. 3 0 2 & 0. 3 1 0 \end{array} \right]
$$

From above matrix, the plan order from the optimal to the most inferior is $d _ { 1 } , d _ { 3 } , d _ { 4 }$ and $d _ { 2 }$

## 4. Conclusion

This paper focuses on the investigation of a new multi-dimensional fuzzy decision support strategy for multi-objective and multi-layer decision support systems. The basic idea is to present a new strategy to utilize sufficiently the information coming from down layer unit systems to support the decision making of up layer unit systems. The presented multi-dimensional fuzzy decision support strategy is based on the theory of fuzzy pattern recognition as well as fuzzy optimization. Compared with the conventional strategy of fuzzy optimization that just considers the relative membership $u _ { j }$ of decision j of down layer unit systems, this strategy also takes the relative bad membership $u _ { j } ^ { l } { = } 1 - u _ { j }$ as the input of up layer unit systems. In other words, the presented strategy can utilize sufficiently the information coming from down layer unit systems. Besides, unlike the conventional strategy of fuzzy optimization that has only onedimensional information, the presented strategy can provide multi-dimensional information. In other words, the output information by use of the presented strategy is much more abundant. The given example validates the efficiency of the presented strategy because the computation is very simple. All these advantages make it as a new basis for the multidimensional decision making of large decision support systems with multi-objective and multi-layer.

## References

[1] M. Balazinski, K. Jemielniak, Tool conditions monitoring using fuzzy decision support, Proceedings of the V International Conference on Monitoring and Automatic Supervision in Manufacturing, Miedzeszyn, Poland, 1998, pp. 115 – 122.

[2] M. Balazinski, Z. Klim, Etude sur l’application de la logique floue pour la prediction de la maintenance preventive, International Industrial Engineering Conference, Polytechnique, Montreal, Canada, vol. II, 1995, pp. 1133 – 1142.

[3] M. Balazinski, L. Kops, P. Massicotte, Job dispatching using priority factors and fuzzy logic, ICME 98 CIRP International Seminar on Intelligent Computation in Manufacturing Engineering, Capri, Italy, 1998, pp. 147 – 153.

[4] L. Baron, et al., Fuzzy decision support system knowledge base generation using a genetic algorithm, International Journal of Approximate Reasoning 28 (2001) 125– 148.

[5] P.K. Dash, et al., A new approach to identification of transient power quality problems using linear combiners, Electric Power Systems Research 51 (1999) 1 – 11.

[6] E. Dupinet, M. Balazinski, E. Czogala, Tolerance allocation based on fuzzy logic and simulated annealing, Journal of Intelligent Manufacturing 7 (1996) 487– 497.

[7] A.O. Esbogue, R.C. Elder, Fuzzy sets and the modeling of the physician decision processes: Part II. Fuzzy diagnosis decision models, Fuzzy Sets and Systems 3 (1) (1980) 1 – 9.

[8] X. Li, W. Zhang, Y. Song, A theoretical model for multidimensional fuzzy decision-making of multi-objective system, Fuzzy Systems and Mathematics (China) 73 (3) (1999) 389– 395.

[9] S.-M. Mario, et al., A fuzzy decision support system for equipment repair under battle conditions, Fuzzy Sets and Systems 115 (2000) 141– 157.

[10] L.K. Pierre, F. Philippe, A fuzzy decision support system for the economic calculus in radioactive waste management, Information Sciences 142 (2002) 103–116.

[11] C.M. Tam, et al., Non-structural fuzzy decision support system for evaluation of construction safety management system, International Journal of Project Management 20 (2002) 303– 313.

[12] J. Williams, N. Steele, Difference, distance and similarity as a basis for fuzzy decision support based on prototypical decision classes, Fuzzy Sets and Systems 131 (2002) 35 – 46.

[13] W.-D. Yu, J.S. Miroslaw, Quantitative constructability analysis with a neuro-fuzzy knowledge-based multi-criterion decision support system, Automation in Construction 8 (1999) 553–565.

![](/api/attachments/TXUU5YME/fulltext/images/4d7b207556b37ae53293543709c4d4f8f9f7b3dd7e1a50b77ed93a96de577735.jpg)

Qimi Jiang is a Post-Doctoral Fellow in the School of Mechanical and Production Engineering at Nanyang Technological University in Singapore. He received his BS degree in Mechanical Engineering from Suzou University, MS degree in Mechanical Engineering from Harbin Institute of Technology and PhD degree in Mechanical Engineering from Huazhong University of Science and Technologuy, China. He

has several years of mechanical design and software development experience in industry. His research interests are computer-aided design, computer-aided test and artificial intelligence in engineering application.

Chun-Hsien Chen is an Assistant Professor in the School of Mechanical and Production Engineering at Nanyang Technological University in Singapore. He received his BS degree in Industrial Design from National Cheng Kung University, Taiwan, MS and PhD degrees in Industrial Engineering from the University of Missouri-Columbia, USA. He has several years of product design and development experience in industry. His teaching and research interests are in collaborative product development, knowledgebased decision support systems, and artificial intelligence in product/engineering design. He is a member of the Institute of Industrial Engineers (IIE) and American Society for Engineering Education (ASEE).
