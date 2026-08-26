---
otero_id: 2590
otero_key: "ZZ6E5RAQ"
title: "Efficiency measurement for network systems: IT impact on firm performance"
authors: "Chiang Kao; Shiuh-Nan Hwang"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.06.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ef<sup>fi</sup>ciency measurement for network systems: IT impact on <sup>fi</sup>rm performance

Chiang Kao <sup>a,</sup>⁎, Shiuh-Nan Hwang b

<sup>a</sup> Department of Industrial and Information Management, National Cheng Kung University, Tainan, Taiwan, Republic of China

<sup>b</sup> Graduate School of Management, Ming Chuan University, Taipei, Taiwan, Republic of China

## a r t i c l e i n f o

Available online 17 June 2009

Keywords: Data envelopment analysis Information technology Banking

## a b s t r a c t

A recent development in DEA (data envelopment analysis) examines the internal structure of a system so that more information regarding sources that cause inef<sup>fi</sup>ciency can be obtained. This paper discusses a network DEA model which distributes the system inef<sup>fi</sup>ciency to its component processes. The model is applied to assess the impact of information technology (IT) on <sup>fi</sup>rm performance in a banking industry. The results show that the impact of IT on <sup>fi</sup>rm performance operates indirectly through fund collection. The impact increases when the IT budget is shared with the pro<sup>fi</sup>t generation process.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

One of the most useful methodologies for measuring the relative ef<sup>fi</sup>ciency of a set of decision making units (DMUs) which utilize multiple inputs to produce multiple outputs is data envelopment analysis (DEA) developed by Charnes et al. [15]. This methodology has been applied to research related to decision support systems [32]; for example, facilitating the agent's intelligent behavior in agent-based merchandise management [50], selecting learning cases to improve the forecasting accuracy of neural networks [51], assessing the contribution of knowledge to business performance [1], measuring the ef<sup>fi</sup>ciency in Internet companies [55], selecting enterprise resource planning (ERP) software [7], performing group evaluation of production units [59], and evaluating data warehouse operations [44]. Advances in DEA methodology will further aid research and applications in decision support systems.

In a production system, the input usually goes through several processes before it becomes the output. Traditional DEA models treat the system as a whole unit, disregarding the interactions of the processes in the system when calculating the ef<sup>fi</sup>ciency. The <sup>fi</sup>rst paper discussing this idea was prepared by Charnes et al. [13], which found that the army recruitment had two processes: the <sup>fi</sup>rst created awareness through advertisement, and the second created contracts using other recruitment resources. Separating large operations into detailed processes helps identify sources of inef<sup>fi</sup>ciency and the real impact of factors. Many empirical studies have successfully applied this idea to real world problems. However, it has been frequently observed that, for some DMUs, the system is ef<sup>fi</sup>cient while the component processes are not. For this reason, Färe and Grosskopf [27] proposed the idea of network

DEA, taking the operation of component processes into consideration in calculating the ef<sup>fi</sup>ciency of the system.

Several models for measuring the ef<sup>fi</sup>ciency of network systems have been proposed [17,27,35,39,52,61,68]. They can be classi<sup>fi</sup>ed into three groups. The <sup>fi</sup>rst is an independent approach which recognizes the existence of the processes in the system, yet the ef<sup>fi</sup>ciencies of the system and all processes are calculated independently. The second is a connected approach, in that interactions between processes are taken into account in calculating the system ef<sup>fi</sup>ciency. There are several variations on this approach; some are able to calculate the system ef<sup>fi</sup>ciency and process ef<sup>fi</sup>ciencies in the same mathematical program, while others need to rely on the conventional DEA model to calculate the process ef<sup>fi</sup>ciencies separately. The third is a relational approach; its underlying concept is that some kind of mathematical relationship exists between the system ef<sup>fi</sup>ciency and the component process ef<sup>fi</sup>ciencies; for example, simple multiplications [37] and weighted average [18].

In this paper, we discuss a model which provides a uni<sup>fi</sup>ed mathematical relationship between the system ef<sup>fi</sup>ciency and process ef<sup>fi</sup>ciencies for all types of network structure. For illustration, the problem of assessing the impact of information technology on the performance of a <sup>fi</sup>rm as discussed in Wang et al. [65] and Chen and Zhu [21] is revisited. Moreover, a model for measuring the ef<sup>fi</sup>ciency when certain resources are being shared is used to obtain a better assessment.

The rest of this paper is organized as follows. Section 2 introduces the idea of the relational approach using an example. Section 3 discusses how this approach is used to model series and parallel systems. The problem of assessing the impact of IT on bank performance is discussed in Section 4. Finally, some conclusion is given in Section 5 based on the discussion of the results.

## 2. The relational model

DEA is concerned with performance evaluation for a set of decision making units (DMUs) utilizing multiple inputs to produce multiple outputs. Let $X _ { i j }$ and $Y _ { r j }$ denote the ith input, $i { = } 1 , { \ldots } , m ,$ , and rth output, $r = 1 , . . . , s ,$ respectively, of the jth DMU, $j = 1 , . . . , \ n$ . The relative ef<sup>fi</sup>ciency of DMU k under the assumption of constant returns to scale is calculated via the following CCR model [15]:

$$
\begin{array}{l} E _ {k} = \max. \sum_ {r = 1} ^ {s} u _ {r} Y _ {r k} \\ \text {s.t.} \sum_ {i = 1} ^ {m} v _ {i} X _ {i k} = 1 \\ \sum_ {r = 1} ^ {s} u _ {r} Y _ {r j} - \sum_ {i = 1} ^ {m} v _ {i} X _ {i j} \leq 0, \quad j = 1,..., n \\ u _ {r}, v _ {i} \geq \varepsilon , r = 1,..., s, i = 1,..., m, \end{array}\tag{1}
$$

where u and v are virtual multipliers and ε is a small non-Archimedean number [12,16] which is imposed to prevent any input/output factor from being ignored in calculating the ef<sup>fi</sup>ciency. This model was extended by Banker et al. [3] to account for variable returns to scale. Other variations have also been developed for different problems [14].

Model (1) is generally referred to as the ratio-form DEA model because the constraint $\Sigma _ { r = 1 } ^ { s } u _ { r } Y _ { r j } - \Sigma _ { i = 1 } ^ { m } \nu _ { i } X _ { i j } { \le } 0$ has a ratio form of $\begin{array} { r } { \sum _ { r = 1 } ^ { s } u _ { r } Y _ { r j } / \Sigma _ { i = 1 } ^ { m } \nu _ { i } X _ { i j } { \le } 1 , } \end{array}$ which is just the ef<sup>fi</sup>ciency of DMU k for $\displaystyle { \dot { } } j = k .$ This model is the dual of the following linear program:

$$
\begin{array}{l} E _ {k} = \min. \theta - \varepsilon (\sum_ {i = 1} ^ {m} s _ {i} ^ {-} + \sum_ {r = 1} ^ {s} s _ {r} ^ {+}) \\ \text {   s.t.   } \sum_ {j = 1} ^ {n} \lambda_ {j} X _ {i j} + s _ {i} ^ {-} = \theta X _ {i k}, i = 1, \dots , m \\ \sum_ {j = 1} ^ {n} \lambda_ {j} Y _ {r j} - s _ {r} ^ {+} = Y _ {r k}, r = 1, \dots , s \\ \lambda_ {j}, s _ {i} ^ {-}, s _ {r} ^ {+} \geq 0, j = 1, \dots , n, i = 1, \dots , m, r = 1, \dots , s \\ \theta \text {   unrestricted   in   sign.   } \end{array} \tag {2}
$$

Since the production possibility set is enveloped by $\begin{array} { r } { \Sigma _ { j = 1 } ^ { n } \lambda _ { r } X _ { i j } { \le } X , } \end{array}$ $\Sigma _ { j = 1 } ^ { n } \lambda _ { j } Y _ { r j } { \ge } \mathrm { Y } , \lambda _ { j } { \ge } 0 , j { = } 1 , . . . , n$ , this model is usually referred to as the envelopment-form DEA model. On optimality, $( \Theta X _ { i k } - s _ { i } ^ { - } , Y _ { r k } + s _ { r } ^ { + } )$ is the target for the inef<sup>fi</sup>cient DMU to achieve ef<sup>fi</sup>ciency.

Model (1) is used for calculating the ef<sup>fi</sup>ciency of the DMU considered as a whole system. In many cases, a system is composed of several processes, where some outputs are the inputs of others. That is, in addition to the <sup>fi</sup>nal output, there are intermediate products being produced and consumed within the system. There are also cases when the processes operate independently, without producing intermediate products for other processes to utilize. In these cases, it is possible that the conventional DEA model will evaluate the system as ef<sup>fi</sup>cient even if none of its component processes is ef<sup>fi</sup>cient. Cases have also been observed in which all the corresponding processes of one DMU are less ef<sup>fi</sup>cient than those of another, yet the system has a higher overall ef<sup>fi</sup>ciency score.

Consider a system that utilizes inputs $X _ { 1 }$ and $X _ { 2 }$ to produce outputs $Y _ { 1 }$ and $Y _ { 2 } .$ The production can be separated into two processes with an intermediate product Z produced by the <sup>fi</sup>rst process and utilized by the second, as depicted in Fig. 1. Table 1 shows the data of four DMUs, A, B, C, and D. The ef<sup>fi</sup>ciencies of the system for converting $X _ { 1 }$ and $X _ { 2 }$ to $Y _ { 1 }$ and $Y _ { 2 } ,$ that of Process 1 for converting $X _ { 1 }$ and $X _ { 2 }$ to Z, and that of Process 2 for converting Z to $Y _ { 1 }$ and $Y _ { 2 }$ can be calculated independently by applying the CCR Model (1). The last three columns of Table 1 show that A and B are ef<sup>fi</sup>cient at the system level despite both of their Process 2 being inef<sup>fi</sup>cient. Furthermore, the process ef<sup>fi</sup>ciencies of D are dominated by C, yet the system ef<sup>fi</sup>ciency of D is greater than that of C. Although it is well known that, due to differences in the reference set, the CCR ef<sup>fi</sup>ciency only identi<sup>fi</sup>es inef<sup>fi</sup>cient DMUs rather than providing a basis for ranking DMUs, these results still make evaluators feel uncomfortable. Therefore, the internal structure must be taken into account in order to obtain representative results.

![](/api/attachments/ZZ6E5RAQ/fulltext/images/ab139a31addfe4246c5fe64469ac8ca3b73b6e26f9bcdfe10617bbebc2d4fc8c.jpg)  
Fig. 1. Series system of two processes.

Data and CCR ef<sup>fi</sup>ciencies for the example.

<table><tr><td rowspan="2">DMU</td><td colspan="2">Input</td><td>Intermediate product</td><td colspan="2">Output</td><td colspan="3">CCR efficiency</td></tr><tr><td> $X_1$ </td><td> $X_2$ </td><td>Z</td><td> $Y_1$ </td><td> $Y_2$ </td><td>Process 1</td><td>Process 2</td><td>System</td></tr><tr><td>A</td><td>1</td><td>2</td><td>1.6</td><td>2</td><td>3</td><td>1</td><td>0.4187</td><td>1</td></tr><tr><td>B</td><td>2</td><td>1</td><td>1.0</td><td>2</td><td>1</td><td>1</td><td>0.3</td><td>1</td></tr><tr><td>C</td><td>4</td><td>5</td><td>0.67</td><td>3</td><td>3</td><td>0.1595</td><td>1</td><td>0.5000</td></tr><tr><td>D</td><td>5</td><td>5</td><td>0.6</td><td>4</td><td>2</td><td>0.1385</td><td>1</td><td>0.6000</td></tr></table>

Measuring the ef<sup>fi</sup>ciency of network systems started with the innovative work of Färe and Grosskopf [25], whose basic idea was to take the production technology of individual processes into consideration when calculating the system ef<sup>fi</sup>ciency. Via intermediate products and shared resources, all processes are connected together. The connected approach is <sup>fl</sup>exible in modeling the production technology of the process, yet it is unable to show the mathematical relationship between system ef<sup>fi</sup>ciency and the process ef<sup>fi</sup>ciencies. Kao [35] proposed a relational approach to model network systems. The underlying assumption is that the virtual multiplier associated with the same factor should be the same no matter whether it is the output of one process or the input of another. In other words, the imputed price of a factor, as represented by the virtual multiplier, should be the same, no matter what role the factor plays. The rationale is that if this factor is treated as an output and is sold in the market, then an income equal to the price is earned. On the other hand, if the factor is used as an input and is bought from the market, then a cost equal to the price is incurred. Therefore, the same multiplier is used for the same factor. One consequence of this assumption is that, for a DMU, the sum of the constraints associated with the processes is exactly the constraint associated with the system, which re<sup>fl</sup>ects a desirable property of the network system that all intermediate products are produced and consumed within the system.

Since the network system does not have a general structure, we use an example to illustrate the relational model. Fig. 2 is the network system discussed in Lewis and Sexton [39]. Surprisingly, this simple network system is the most complicated one that has appeared in the literature. This system has <sup>fi</sup>ve processes linked by intermediate products. Process 1 uses inpu $X _ { 1 }$ to produce Intermediate Products $Z _ { 1 } ^ { 1 3 }$ $\dot { Z } _ { 2 } ^ { 1 3 }$ , and $Z ^ { 1 4 }$ ; Process 2 uses input X to produce Intermediate Products $Z _ { 1 } ^ { \bar { 2 } 4 }$ and $Z _ { 2 } ^ { 2 4 . } ;$ ; Process 3 uses input $X _ { 3 }$ and Intermediate Products $Z _ { 1 } ^ { 1 3 }$ and $Z _ { 2 } ^ { 1 3 }$ , produced by Process 1, to produce Intermediate Product $Z ^ { 3 5 } ;$ Process 4 uses Intermediate Products $Z ^ { 1 4 }$ , produced by Process 1, and Intermediate Products $Z _ { 1 } ^ { 2 4 }$ and $Z _ { 2 } ^ { 2 4 }$ , produced by Process 2, to produce Intermediate Product $Z ^ { 4 5 }$ ; and Process 5 uses Intermediate Products $Z ^ { 3 5 } \mathrm { a n d } Z ^ { 4 5 }$ , produced by Processes 3 and $^ { 4 , }$ respectively, to produce the <sup>fi</sup>nal output Y. The idea of Kao [35] is to represent a general network system by a series system where each stage of the latter has a parallel structure. Based on the series and parallel structures, the system ef<sup>fi</sup>ciency is decomposed into a complicated relationship of process ef<sup>fi</sup>ciencies. Notably, the series-parallel representation of a network system is not unique.

The relational approach in Kao [35] requires that the aggregated output be less than or equal to the aggregated input for all processes in addition to the usual requirement for the system. The key point is that the multipliers used in the aggregation are the same for the same factor. For the system in Fig. 2, the model for calculating the ef<sup>fi</sup>ciency of DMU k becomes

![](/api/attachments/ZZ6E5RAQ/fulltext/images/c60c35ef587c617089663e511285a89ff13a7b60ddd3d9f4b79e8e22dc38ca0e.jpg)  
Fig. 2. Network system discussed in Lewis and Sexton [39]

E = max:uY

$$
s. t. v _ {1} X _ {1 k} + v _ {2} X _ {2 k} + v _ {3} X _ {3 k} = 1
$$

$$
u Y _ {j} - (v _ {1} X _ {1 j} + v _ {2} X _ {2 j} + v _ {3} X _ {3 j}) \leq 0, \quad j = 1,..., n\tag{3.0}
$$

$$
w _ {1} ^ {1 3} Z _ {1 j} ^ {1 3} + w _ {2} ^ {1 3} Z _ {2 j} ^ {1 3} + w ^ {1 4} Z _ {j} ^ {1 4} - v _ {1} X _ {1 j} \leq 0,\tag{3.1}
$$

$$
w _ {1} ^ {2 4} Z _ {1 j} ^ {2 4} + w _ {2} ^ {2 4} Z _ {2 j} ^ {2 4} - v _ {2} X _ {2 j} \leq 0,
$$

$$
j = 1, \dots , n\tag{3.2}
$$

$$
w ^ {3 5} Z _ {j} ^ {3 5} - (w _ {1} ^ {1 3} Z _ {1 j} ^ {1 3} + w _ {2} ^ {1 3} Z _ {2 j} ^ {1 3} + \nu_ {3} X _ {3 j}) \leq 0, \qquad j = 1,..., n\tag{3.3}
$$

$$
w ^ {4 5} Z _ {j} ^ {4 5} - (w ^ {1 4} Z _ {j} ^ {1 4} + w _ {1} ^ {2 4} Z _ {1 j} ^ {2 4} + w _ {2} ^ {2 4} Z _ {2 j} ^ {2 4}) \leq 0, \quad j = 1,..., n\tag{3.4}
$$

$$
u Y _ {j} - (w ^ {3 5} Z _ {j} ^ {3 5} + w ^ {4 5} Z _ {j} ^ {4 5}) \leq 0,\tag{3.5}
$$

$$
u, v _ {1}, v _ {2}, v _ {3}, w _ {1} ^ {1 3}, w _ {2} ^ {1 3}, w ^ {1 4}, w _ {1} ^ {2 4}, w _ {2} ^ {2 4}, w ^ {3 5}, w ^ {4 5} \geq \varepsilon ,
$$

where constraint set (Eq. (3.0)) corresponds to the system, and constraint sets (Eqs. (3.1)) to (3.5) correspond to Processes 1 to 5, respectively. A characteristic of this model is that every intermediate product has the same multiplier, no matter what role it plays. For example, Intermediate Product $Z _ { 1 } ^ { 1 \bar { 3 } }$ always has the multiplier $w _ { 1 } ^ { \bar { 1 } 3 }$ , no matter whether it is considered as the output of Process 1 or the input of Process 3. Hence, the intermediate products cancel out when the constraints corresponding to the processes, Eqs. (3.1) to (3.5), are summed together. The result is the constraint corresponding to the system, Eq. (3.0).

Let $s _ { k }$ and ${ s _ { k } ^ { ( p ) } , p = 1 , . . . , 5 , }$ , be the slack variables associated with the system constraint and the pth process constraint of DMU k, respectively. Thus, we have:

$$
s _ {k} = s _ {k} ^ {(1)} + s _ {k} ^ {(2)} + s _ {k} ^ {(3)} + s _ {k} ^ {(4)} + s _ {k} ^ {(5)},\tag{4}
$$

because the sum of the process constraints is equal to the system constraint. That is, the inef<sup>fi</sup>ciency of the system, $s _ { k } ,$ is attributable to component processes; speci<sup>fi</sup>cally, the proportion of inef<sup>fi</sup>ciency due to Process $p$ is $s _ { k } ^ { ( p ) } / s _ { k } .$ Note that $s _ { k } ^ { ( \bar { p } ) }$ is not the inef<sup>fi</sup>ciency of Process $p$ because the aggregated input of each process is not necessarily equal to 1.

Denoting the optimal solution by “\*”, the system and process ef<sup>fi</sup>ciencies of DMU k are:

$$
\begin{array}{l} E _ {k} = u ^ {*} Y _ {k} / (v _ {1} ^ {*} X _ {1 k} + v _ {2} ^ {*} X _ {2 k} + v _ {3} ^ {*} X _ {3 k}) = 1 - s _ {k} ^ {*} \\ E _ {k} ^ {(1)} = (w _ {1} ^ {1 3 *} Z _ {1 k} ^ {1 3} + w _ {2} ^ {1 3 *} Z _ {2 k} ^ {1 3} + w ^ {1 4 *} Z _ {k} ^ {1 4}) / v _ {1} ^ {*} X _ {1 k} = 1 - s _ {k} ^ {(1) *} / v _ {1} ^ {*} X _ {1 k} = 1 - \hat {s} _ {k} ^ {(1) *} \\ E _ {k} ^ {(2)} = (w _ {1} ^ {2 4 *} Z _ {1 k} ^ {2 4} + w _ {2} ^ {2 4 *} Z _ {2 k} ^ {2 4}) / v _ {2} ^ {*} X _ {2 k} = 1 - s _ {k} ^ {(2) *} / v _ {2} ^ {*} X _ {2 k} = 1 - \hat {s} _ {k} ^ {(2) *} \\ E _ {k} ^ {(3)} = w ^ {3 5 *} Z _ {k} ^ {3 5} / (w _ {1} ^ {1 3 *} Z _ {1 k} ^ {1 3} + w _ {2} ^ {1 3 *} Z _ {2 k} ^ {1 3} + v _ {3} ^ {*} X _ {3 k}) \\ \quad = 1 - s _ {k} ^ {(3) *} / (w _ {1} ^ {1 3 *} Z _ {1 k} ^ {1 3} + w _ {2} ^ {1 3 *} Z _ {2 k} ^ {1 3} + v _ {3} ^ {*} X _ {3 k}) = 1 - \hat {s} _ {k} ^ {(3) *} \\ E _ {k} ^ {(4)} = w ^ {4 5 *} Z _ {k} ^ {4 5} / (w ^ {1 4 *} Z _ {k} ^ {1 4} + w _ {1} ^ {2 4 *} Z _ {1 k} ^ {2 4} + w _ {2} ^ {2 4 *} Z _ {2 k} ^ {2 4}) \\ \quad = 1 - s _ {k} ^ {(4) *} / (w ^ {1 4 *} Z _ {k} ^ {1 4} + w _ {1} ^ {2 4 *} Z _ {1 k} ^ {2 4} + w _ {2} ^ {2 4 *} Z _ {2 k} ^ {2 4}) = 1 - \hat {s} _ {k} ^ {(4) *} \\ E _ {k} ^ {(5)} = u ^ {*} Y _ {k} / (w ^ {3 5 *} Z _ {k} ^ {3 5} + w ^ {4 5 *} Z _ {k} ^ {4 5}) = 1 - s _ {k} ^ {(5) *} / (w ^ {3 5 *} Z _ {k} ^ {3 5} + w ^ {4 5 *} Z _ {k} ^ {4 5}) = 1 - \hat {s} _ {k} ^ {(5) *}, \end{array}\tag{5}
$$

where $\hat { \mathsf { S } } _ { k } ^ { ( p ) ^ { * } }$ is the inef<sup>fi</sup>ciency of Process $p , \ p { = } 1 , . . . , \ 5 .$ . From the relationship between $s _ { k } ^ { ( p ) ^ { * } }$ and $ { \hat { \mathbf { s } } } _ { k } ^ { ( p ) ^ { * } }$ expressed in Eq. (5), we have:

$$
\begin{array}{r l} & {(v _ {1} ^ {*} X _ {1 k}) \hat {s} _ {k} ^ {(1) ^ {*}} + (v _ {2} ^ {*} X _ {2 k}) \hat {s} _ {k} ^ {(2) ^ {*}} + (w _ {1} ^ {1 3 ^ {*}} Z _ {1 k} ^ {1 3} + w _ {2} ^ {1 3 ^ {*}} Z _ {2 k} ^ {1 3} + v _ {3} ^ {*} X _ {3 k}) \hat {s} _ {k} ^ {(3) ^ {*}}} \\ & {\qquad + (w ^ {1 4 *} Z _ {k} ^ {1 4} + w _ {1} ^ {2 4 ^ {*}} Z _ {1 k} ^ {2 4} + w _ {2} ^ {2 4 ^ {*}} Z _ {2 k} ^ {2 4}) \hat {s} _ {k} ^ {(4) ^ {*}}} \\ & {\qquad + (w ^ {3 5 *} Z _ {k} ^ {3 5} + w ^ {4 5 *} Z _ {k} ^ {4 5}) \hat {s} _ {k} ^ {(5) ^ {*}} = s _ {k} ^ {*}} \end{array}\tag{6}
$$

In other words, the system inef<sup>fi</sup>ciency is a linear combination of process inef<sup>fi</sup>ciencies, where the coef<sup>fi</sup>cient for combination is the aggregated input of the corresponding process. Note that it is not a weighted average because the total weight of the <sup>fi</sup>ve processes is not equal to 1. Eqs. (4) and (6), which are essentially identical, can be used to interpret the relationship between the system ef<sup>fi</sup>ciency and process ef<sup>fi</sup>ciencies for general network systems.

The relational model can also be formulated in envelopment form, which is the dual of Model (3). Since constraint set (Eq. (3.0)) is redundant, it is deleted in formulating the dual model. The non-Archimedean number ε is ignored to get a better idea of the relationship between the processes. The model is formulated as follows:

min: θ

$$
\begin{array}{l} \text {s.t.} \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(1)} X _ {1 j} \leq \theta X _ {1 k} \\ \quad \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(2)} X _ {2 j} \leq \theta X _ {2 k} \\ \quad \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(3)} X _ {3 j} \leq \theta X _ {3 k} \\ \quad \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(5)} Y _ {j} \geq Y _ {k} \\ \hline \hline \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(1)} Z _ {1 j} ^ {1 3} - \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(3)} Z _ {1 j} ^ {1 3} \geq 0 \\ \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(1)} Z _ {2 j} ^ {1 3} - \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(3)} Z _ {2 j} ^ {1 3} \geq 0 \\ \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(1)} Z _ {j} ^ {1 4} - \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(4)} Z _ {j} ^ {1 4} \geq 0 \\ \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(2)} Z _ {1 j} ^ {2 4} - \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(4)} Z _ {1 j} ^ {2 4} \geq 0 \\ \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(2)} Z _ {2 j} ^ {2 4} - \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(4)} Z _ {2 j} ^ {2 4} \geq 0 \\ \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(3)} Z _ {j} ^ {3 5} - \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(5)} Z _ {j} ^ {3 5} \geq 0 \\ \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(4)} Z _ {j} ^ {4 5} - \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(5)} Z _ {j} ^ {4 5} \geq 0 \\ \lambda_ {j} ^ {(1)}, \lambda_ {j} ^ {(2)}, \lambda_ {j} ^ {(3)}, \lambda_ {j} ^ {(4)}, \lambda_ {j} ^ {(5)} \geq 0, \quad j = 1,..., n \end{array}\tag{7}
$$

θ unrestricted in sign:

The constraints above the dotted line correspond to the system inputs, $X _ { 1 } , X _ { 2 } ,$ , and $X _ { 3 } ,$ and <sup>fi</sup>nal output, Y, which are the constraints for the conventional envelopment-form DEA model. Those below the dotted line correspond to intermediate products, one for each of them. On optimality, $\Sigma _ { j = 1 } ^ { n } \lambda _ { j } ^ { * } Z _ { i j }$ represents the target value of Intermediate Product Z. In this context, each constraint requires that the target value of an intermediate product when considered as the output of the process that produces it must be greater than or equal to that considered as the input of the process that consumes it.

Here, it is important to note that, as indicated in Sueyoshi and Sekitani [58], all DEA models suffer from multiple solutions and, consequently, multiple projections. Therefore, the relational network DEA models (3) and (7) proposed in this study also suffer from an occurrence of the dif<sup>fi</sup>culty. The issue is an important future extension of this study.

In the next two sections, we discuss the formulation and characteristics of the relational model for the two basic structures of the network system, series and parallel.

## 3. Basic network structures

## 3.1. Series structures

The <sup>fi</sup>rst network system discussed in the DEA literature is the two-stage system of Charnes et al. [13] (which also appears on p.432 of Charnes et al. [14]). Since then, many applications of twostage DEA have been reported [40,42,43,48,53,56,65,69]. For the original settings, all intermediate products produced in the <sup>fi</sup>rst process are consumed by the second process. The second process does not utilize any exogenous input and the <sup>fi</sup>rst process does not produce <sup>fi</sup>nal outputs. A more general case is thus to take all the aspects into consideration. In addition, Processes 1 and 2 can share certain exogenous inputs [10,19,23,26,30,31,41]. Some studies have investigated systems with three [33,62] and four stages [60].

The general series system has the structure shown in Fig. 3, where q processes are linked by intermediate products. We denote $I = \{ 1 , 2 , . . . , m \} , 0 = \{ 1 , 2 , . . . , s \}$ , and $M = \{ 1 , 2 , . . . , t \}$ as the index sets of the input, output, and intermediate product, respectively; and similarly, ${ \bf \hat { \chi } } ^ { ( p ) } { \subset } { \cal I } , { \bf \hat { \cal O } } ^ { ( p ) } { \subset } { \cal O }$ , and $M ^ { \left( p \right) } \subset M \mathrm { { \widehat { a s } } }$ the corresponding index sets for Process $p .$ Process p utilizes inputs $X _ { i } ^ { ( p ) } , \ i \in I ^ { ( \bar { p } ) }$ , and intermediate products $Z _ { l } ^ { ( p - 1 ) } , \ l \in { \cal M } ^ { ( p - 1 ) }$ , produced by Process $( p - 1 )$ ), to produce outputs $Y _ { r } ^ { ( p ) } , r \in O ^ { ( p ) }$ , and intermediate products $Z _ { l } ^ { ( p ) } , \ l \in M ^ { ( p ) }$ . The intermediate products used by Process 1, $Z _ { l } ^ { ( 0 ) }$ $l \in { \cal M } ^ { ( 0 ) }$ , can be considered as exogenous inputs and the intermediate products produced by Process $q , \ Z _ { l } ^ { ( q ) } , \ l \in M ^ { ( q ) }$ , can be considered as <sup>fi</sup>nal outputs. In this paper, we assume that all $M ^ { ( p ) }$ $p { = } 1 { , } { \ldots } , q$ , are mutually exclusive (this constraint can be relaxed whenever necessary), and this is not required for ${ \cal I } ^ { ( p ) } , p = 1 , . . . , q ,$ and ${ { O } ^ { ( p ) } } , \ p = 1 , . . . , \ q$ . The dynamic model [46,47,49,54,57,61,64] belongs to this type. The total amount of input i utilized by System k is the sum of those utilized by all of its processes, $X _ { i k } { = } \dot { \Sigma } _ { p { = } 1 } ^ { q } X _ { i k } ^ { ( p ) }$ Similarly, the total amount of output r produced by System k is the sum of those produced by all of its processes, $Y _ { r k } { = } \overset { \cdot } { \Sigma } _ { p { = } 1 } ^ { q } Y _ { r k } ^ { ( p ) }$

The relational model for calculating the system ef<sup>fi</sup>ciency of DMU k in ratio form is as follows:

$$
\begin{array}{l} E _ {k} = \max. \sum_ {r = 1} ^ {s} u _ {r} Y _ {r k} \\ \text {s.t.} \sum_ {i = 1} ^ {m} v _ {i} X _ {i k} = 1 \\ \sum_ {r = 1} ^ {s} u _ {r} Y _ {r j} - \sum_ {i = 1} ^ {m} v _ {i} X _ {i j} \leq 0, \quad j = 1,..., n \\ (\sum_ {r \in O ^ {(p)}} u _ {r} Y _ {r j} ^ {(p)} + \sum_ {l \in M ^ {(p)}} w _ {l} Z _ {l j} ^ {(p)}) - (\sum_ {i \in I ^ {(p)}} v _ {i} X _ {i j} ^ {(p)} + \sum_ {l \in M ^ {(p - 1)}} w _ {l} Z _ {l j} ^ {(p - 1)}) \leq 0, \\ p = 1,..., q, \quad j = 1,..., n \\ u _ {r}, v _ {l}, w _ {l} \geq \varepsilon , \quad r = 1,..., s, i = 1,..., m, l = 1,..., t. \end{array}\tag{8.1}
$$

<sub>ð</sub>8:2<sub>Þ</sub>

Note that the same factor has the same multiplier, no matter which process it is associated with. Constraint set (Eq. (8.1)) essentially states that the aggregated system output must be less than or equal to the aggregated system input for all DMUs. Constraint set Eq. (8.2) is the process counterpart of Eq. (8.1). On optimality, the system ef<sup>fi</sup>ciency and process ef<sup>fi</sup>ciencies for DMU k are calculated as:

$$
\begin{array}{l} E _ {k} = \sum_ {r = 1} ^ {s} u _ {r} ^ {*} Y _ {r k} / \sum_ {i = 1} ^ {m} v _ {i} ^ {*} X _ {i k} = 1 - s _ {k} ^ {*} \\ E _ {k} ^ {(p)} = (\sum_ {r \in O ^ {(p)}} u _ {r} ^ {*} Y _ {r j} ^ {(p)} + \sum_ {l \in M ^ {(p)}} w _ {l} ^ {*} Z _ {l k} ^ {(p)}) / (\sum_ {i \in I ^ {(p)}} v _ {i} ^ {*} X _ {i j} ^ {(p)} + \sum_ {l \in M ^ {(p - 1)}} w _ {l} ^ {*} Z _ {l k} ^ {(p - 1)}) \\ = 1 - s _ {k} ^ {(p) *} / (\sum_ {i \in I ^ {(p)}} v _ {i} ^ {*} X _ {i j} ^ {(p)} + \sum_ {l \in M ^ {(p - 1)}} w _ {l} ^ {*} Z _ {l k} ^ {(p - 1)}) = 1 - \hat {s} _ {k} ^ {(p) *}, p = 1, \dots , q, \end{array}\tag{9.1}
$$

<sub>ð</sub>9:2<sub>Þ</sub>

where s<sup>\*</sup> and ${ s _ { k } ^ { ( p ) } } ^ { * } , p = 1 , . . . , q ,$ , are the slack variables associated with the system constraint Eq. (8.1) and process constraint Eq. (8.2), respectively. Since the sum of the q process constraints in Eq. (8.2) is equal to the system constraint in Eq. (8.1), we have $s _ { k } ^ { * } = \bar { \Sigma _ { p } ^ { q } } = 1 \bar { S _ { k } ^ { ( p ) ^ { * } } }$ . That is, the inef<sup>fi</sup>ciency of the system, $s _ { k } ^ { \ast } ,$ can be distributed to the component processes, with each having a proportion of $s _ { k } ^ { ( p ) ^ { * } } / s _ { k } ^ { ^ { * } }$ . Note that $s _ { k } ^ { ( p ) ^ { * } }$ is not the inef<sup>fi</sup>ciency of the process, but the difference between the aggregated input and aggregated output. The inef<sup>fi</sup>ciency of Process p is $\hat { \mathsf { S } } _ { k } ^ { ( p ) ^ { * } }$ , which is the slack variable $s { \boldsymbol { \xi } } _ { k } ^ { ( p ) ^ { * } }$ divided by the aggregated input $( \Sigma _ { i \in I ^ { ( \mathrm { p } ) } V _ { i } ^ { ' } } X _ { i k } ^ { ( p ) } + \Sigma _ { l \in M ^ { ( p - 1 ) } W _ { l } ^ { ' } } Z _ { l k } ^ { ( p - 1 ) } )$ , as expressed in (9.2). Thus, the system inef<sup>fi</sup>ciency and process inef<sup>fi</sup>ciencies have the following relationship:

$$
s _ {k} ^ {*} = \sum_ {p = 1} ^ {q} \left[ \sum_ {i \in I ^ {(p)}} v _ {i} ^ {*} X _ {i k} ^ {(p)} + \sum_ {l \in M ^ {(p - 1)}} w _ {l} ^ {*} Z _ {l k} ^ {(p - 1)} \right] \hat {s} _ {k} ^ {(p) *} = \sum_ {p = 1} ^ {q} \hat {w} ^ {(p)} \hat {s} _ {k} ^ {(p) *}\tag{10}
$$

This relationship is not a weighted average because the sum of the weights, $\Sigma _ { p = 1 } ^ { \mathrm { q } } \hat { \mathbf { \Sigma } } _ { N } ^ { ( p ) }$ , is not 1.

Since all DEA models suffer from multiple solutions on multipliers [58], the inef<sup>fi</sup>ciency slack of each process may have different values. Consequently, the decomposition of the system inef<sup>fi</sup>ciency into process inef<sup>fi</sup>ciencies is different. Nevertheless, the relationship may state that the system inef<sup>fi</sup>ciency is a linear combination of the process inef<sup>fi</sup>ciencies as expressed by Eq. (10) if the equation still holds.

![](/api/attachments/ZZ6E5RAQ/fulltext/images/d02c493bcf9b8fdfc4e724adbce8b8be7d42d18d9a34832659bf47bd16b053c6.jpg)  
Fig. 3. General series system.

A special case of the series system is the one in which all processes, except the <sup>fi</sup>rst, are not allowed to utilize exogenous inputs and all processes, except the last, are not allowed to produce exogenous outputs. Kao and Hwang [37] have showed that, in this case, the system ef<sup>fi</sup>ciency is the product of process ef<sup>fi</sup>ciencies. This phenomenon is easily obtained from Eq. (9.2), where only the terms related to intermediate products are left. Chen et al. [20] have showed that the model of Chen and Zhu [21] is equivalent to Kao-Hwang’s model under constant returns to scale. The system ef<sup>fi</sup>ciency can also be expressed as a weighted average of process ef<sup>fi</sup>ciencies [18]. However, the system ef<sup>fi</sup>ciency de<sup>fi</sup>ned is not the conventional form of the aggregated exogenous output divided by the aggregated exogenous input, but all outputs, including intermediate ones, divided by all inputs, including intermediate ones.

To formulate the envelopment-form DEA model for the series system from Model (8), the redundant constraint set (Eq. (8.1)) is omitted and the non-Archimedean number ε is ignored. Moreover, the terms $\Sigma _ { i \in I } { } ^ { ( p ) }$ $\nu _ { i } X _ { i j } ^ { \left( p \right) }$ and $\Sigma _ { r \in O } { } ^ { ( p ) } u _ { r } Y _ { r j } ^ { ( p ) }$ in Eq. (8.2) are replaced by $\Sigma _ { i = 1 } ^ { m } \nu _ { i } X _ { i j } ^ { ( p ) }$ and $\begin{array} { r } { \Sigma _ { r = 1 } ^ { s } u _ { r } Y _ { r j } ^ { ( p ) } } \end{array}$ , respectively, where $X _ { i j } ^ { ( p ) } , \ : i \notin I ^ { ( p ) } ,$ , and $Y _ { r j } ^ { ( p ) } , r \not \in O ^ { ( p ) }$ , have a value of zero. Thus, we have the following envelopment model:

min: θ

$$
\begin{array}{l l} \text {s.t.} \sum_ {p = 1} ^ {q} \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(p)} X _ {i j} ^ {(p)} \leq \theta X _ {i k}, & i = 1, \dots , m \\ \sum_ {p = 1} ^ {q} \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(p)} Y _ {r j} ^ {(p)} \geq Y _ {r k}, & r = 1, \dots , s \\ \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(1)} Z _ {l j} ^ {(0)} \leq 0, & l \in M ^ {(0)} \\ \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(q)} Z _ {l j} ^ {(q)} \geq 0, & l \in M ^ {(q)} \\ \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(p)} Z _ {l j} ^ {(p)} - \sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(p + 1)} Z _ {l j} ^ {(p)} \geq 0, & l \in M ^ {(p)}, p = 1, \dots , q \\ \lambda_ {j} ^ {(p)} \geq 0, & j = 1, \dots , n, , p = 1, \dots , q \\ \theta \text {unrestricted in sign}. \end{array}\tag{11}
$$

The term $\Sigma _ { j = 1 } ^ { n } \lambda _ { j } ^ { \left( p \right) } Z _ { i j } ^ { \left( p \right) }$ represents the target value for Intermediate Product $Z _ { i j } ^ { ( p ) }$ , as the output of Process p, and $\begin{array} { r } { \sum _ { j = 1 } ^ { n } \lambda _ { j } ^ { ( p + 1 ) } Z _ { i j } ^ { ( p ) } } \end{array}$ represents the target value for $Z _ { i k } ^ { ( \hat { p } ) }$ , as the input of Process $p + 1 .$ The constraint $\Sigma _ { j = 1 } ^ { n } \lambda _ { j } ^ { ( \breve { p } ) } Z _ { i j } ^ { ( p ) } - \Sigma _ { j = 1 } ^ { n } \lambda _ { j } ^ { ( \breve { p } + 1 ) } Z _ { i j } ^ { ( p ) } \geq 0$ requires that the target value for $Z _ { l k } ^ { ( p ) }$ as the output of Process p must be greater than or equal to that as the input of Process $p + 1 .$ . Similarly, the constraint $\Sigma _ { j = 1 } ^ { n } \lambda _ { j } ^ { ( 1 ) } Z _ { l j } ^ { ( 0 ) } { \le } 0$ requires the target value for the initial intermediate product $Z _ { l k } ^ { ( 0 ) } ,$ , as the input, to be non-positive and the constraint $\Sigma _ { j = 1 } ^ { n } \lambda _ { j } ^ { ( q ) } Z _ { l j } ^ { ( q ) } { \geq } 0$ requires the target value for the <sup>fi</sup>nal intermediate product $Z _ { l k } ^ { ( q ) }$ <sup>)</sup>, as the output, to be non-negative.

## 3.2. Parallel structures

Another basic structure in network systems is the parallel structure, in which systems composed of parallel processes operate somewhat independently. The work of Färe and Primont [29], which discusses the ef<sup>fi</sup>ciency of <sup>fi</sup>rms with multiple plants, is probably the <sup>fi</sup>rst study of such systems. Their methodology was applied by Kao [34] to measure the ef<sup>fi</sup>ciency of forest districts with multiple working circles in Taiwan. An extension of the independent parallel system is a situation where certain resources are shared by some processes [5,24,28,45,63,67]. Castelli et al. [11] discussed a hierarchical structure which becomes a parallel system when there is only one layer.

A typical example of a parallel system is a university with departments. The ef<sup>fi</sup>ciency of the whole university can be calculated by the total inputs utilized and total outputs produced by all departments. Each speci<sup>fi</sup>c department can also have an ef<sup>fi</sup>ciency calculated by comparing it with the equivalent departments of other universities. Theoretically, a university is ef<sup>fi</sup>cient only if all its departments are ef<sup>fi</sup>cient. It is thus very probable that no university is ef<sup>fi</sup>cient, because it is not easy for every department of a university to have the best performance. However, this is not important because the ultimate goal of ef<sup>fi</sup>ciency measurement is to <sup>fi</sup>nd the sources of inef<sup>fi</sup>ciency and to make appropriate improvements so that inputs will be used more ef<sup>fi</sup>ciently.

For the general parallel system depicted in Fig. 4, there are q processes; each applies inputs $X _ { i } ^ { ( p ) } , i \in \hat { I } ^ { ( p ) }$ , to produce outputs $Y _ { r } ^ { \left( p \right) }$ $r \in O ^ { ( p ) }$ . Comparing Fig. 4 with Fig. 3, we <sup>fi</sup>nd that the parallel system is a special case of the series system in which there is no intermediate product. As de<sup>fi</sup>ned in the preceding section for series systems, it is not necessary for $I ^ { ( p ) } , p = 1 , . . . , q ,$ , and ${ \cal O } ^ { ( p ) } , p = 1 , . . . , q ,$ respectively, to be mutually exclusive. The relational model for the general parallel system in ratio form can be formulated as:

$$
\begin{array}{l l} E _ {k} = & \max. \sum_ {r = 1} ^ {s} u _ {r} Y _ {r k} \\ & \text { s.t. } \sum_ {i = 1} ^ {m} v _ {i} X _ {i k} = 1 \\ & \sum_ {r = 1} ^ {s} u _ {r} Y _ {r j} - \sum_ {i = 1} ^ {m} v _ {i} X _ {i j} \leq 0, \quad j = 1,..., n \\ & \sum_ {r \in O ^ {(p)}} u _ {r} Y _ {r j} ^ {(p)} - \sum_ {i \in I ^ {(p)}} v _ {i} X _ {i j} ^ {(p)} \leq 0, \quad p = 1,..., q, j = 1,..., n \\ & u _ {r}, v _ {i} \geq \varepsilon , \quad r = 1,..., s, i = 1,..., m. \end{array} \tag {12.1}
$$

As noted earlier, the parallel system is a special case of the series system in which there is no intermediate product. This model is exactly the same as Model (8) if the terms associated with the intermediate products are omitted.

On optimality, the system and process ef<sup>fi</sup>ciencies of the DMU being evaluated are determined as follows:

$$
\begin{array}{l} E _ {k} = \sum_ {r = 1} ^ {s} u _ {r} ^ {*} Y _ {r k} / \sum_ {i = 1} ^ {m} v _ {i} ^ {*} X _ {i k} = 1 - s _ {k} ^ {*} \\ E _ {k} ^ {(p)} = \sum_ {r \in O ^ {(p)}} u _ {r} ^ {*} Y _ {r k} ^ {(p)} / \sum_ {i \in I ^ {(p)}} v _ {i} ^ {*} X _ {i k} ^ {(p)} = 1 - s _ {k} ^ {(p) *} / \sum_ {i \in I ^ {(p)}} v _ {i} ^ {*} X _ {i k} ^ {(p)} = 1 - \hat {s} _ {k} ^ {(p) *}, p = 1, \dots , q, \end{array} \tag {13.1}\tag{13.2}
$$

where $s _ { k } ^ { * }$ and $s \hbar ^ { ( p ) ^ { * } }$ are slack variables associated with the system constraint (Eq. (12.1)) and process constraint (Eq. (12.2)), respectively. Similar to the series system, the sum of the constraints associated with the q processes in Eq. (12.2) is equal to the constraint associated with the system in Eq. (12.1). Hence, the slack variable added to the system constraint is equal to the sum of those added to the q process constraints, $s _ { k } ^ { * } = \Sigma _ { p = 1 } ^ { q } \hat { s } _ { k } ^ { ( p ) ^ { * } }$ . The system will be ef<sup>fi</sup>cient only if all processes are ef<sup>fi</sup>cient. Moreover, the system inef<sup>fi</sup>ciency, $s _ { k } ^ { * } ,$ is distributed to each process in the proportion of $s _ { k } ^ { ( p ) ^ { * } } / s _ { k } ^ { ^ { * } }$

![](/api/attachments/ZZ6E5RAQ/fulltext/images/4af3b3449d5d231716e06dc4398d05cf96e3909fb7ba4a971c3ff70408ae77bc.jpg)  
Fig. 4. General parallel system.

Table 2  
Classi<sup>fi</sup>cation of network DEA studies.

<table><tr><td>Network structure</td><td>Model</td><td>Number of processes</td><td>Studies</td></tr><tr><td rowspan="7">Series</td><td>Independent</td><td>2</td><td>[13,40,42,43,48,53,56,65,69]</td></tr><tr><td>Connected</td><td>2</td><td>[10,17,19,21,23,26,27,30,31,41]</td></tr><tr><td></td><td>3</td><td>[62]</td></tr><tr><td></td><td>4</td><td>[60]</td></tr><tr><td></td><td>Multiple (dynamic)</td><td>[33,46,47,49,57]</td></tr><tr><td>Relational</td><td>2</td><td>[18,20,37]</td></tr><tr><td></td><td>Multiple (dynamic)</td><td>[61,64]</td></tr><tr><td rowspan="4">Parallel</td><td>Connected</td><td>2</td><td>[5,28,45,63,67]</td></tr><tr><td></td><td>3</td><td>[24]</td></tr><tr><td></td><td>Multiple</td><td>[11]</td></tr><tr><td>Relational</td><td>Multiple</td><td>[36]</td></tr><tr><td rowspan="3">Mixed</td><td>Independent</td><td>5</td><td>[39]</td></tr><tr><td>Connected</td><td>3</td><td>[27,68]</td></tr><tr><td>Relational</td><td>3</td><td>[35]</td></tr></table>

From Eqs. (13.1 and 13.2), the system inef<sup>fi</sup>ciency, $\bar { s _ { k } } ,$ and process inef<sup>fi</sup>ciencies, $\hat { \mathsf { S } } _ { k } ^ { ( p ) ^ { * } }$ , have the following relationship:

$$
s _ {k} ^ {*} = \sum_ {p = 1} ^ {q} \left[ \sum_ {i \in I ^ {(p)}} v _ {i} ^ {*} X _ {i k} ^ {(p)} \right] \hat {s} _ {k} ^ {(p) *} = \sum_ {p = 1} ^ {q} \hat {w} ^ {(p)} \hat {s} _ {k} ^ {(p) *}\tag{14}
$$

Since the sum of the weights in this case has a value of $^ { 1 , }$ $\Sigma _ { p } ^ { q } = { { 1 } } \Sigma _ { { i } \in { I ^ { ( p ) } } } { \nu _ { i } ^ { * } } X _ { { i } k } ^ { ( p ) } = \Sigma _ { p } ^ { q } = { { 1 } } \Sigma _ { i = 1 } ^ { m } { \nu _ { i } ^ { * } } X _ { { i } k } ^ { ( p ) } = 1$ , the system inef<sup>fi</sup>ciency is a weighted average of process inef<sup>fi</sup>ciencies. Similar to the series case, when the redundant constraint set (Eq. (12.1)) is deleted, the non-Archimedean number ε is ignored, and $\dot { \Sigma _ { i \in I } } { } ^ { ( p ) } V _ { i } X _ { i j } ^ { ( p ) }$ and $\Sigma _ { r \in O } { } ^ { ( p ) } u _ { r } Y _ { r j } ^ { ( p ) }$ are replaced by $\Sigma _ { i = 1 } ^ { m } \nu _ { i } X _ { i j } ^ { ( p }$ <sup>)</sup>and $\begin{array} { r } { \Sigma _ { r = 1 } ^ { s } u _ { r } Y _ { r j } ^ { ( p ) } } \end{array}$ <sup>)</sup>, respectively, the envelopment-form DEA model has the following form:

min: θ

$$
\mathrm{s.t.} \sum_ {p = 1} ^ {q} (\sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(p)} X _ {i j} ^ {(p)}) \leq \theta X _ {i k}, \quad i = 1, \dots , m\tag{15.1}
$$

$$
\sum_ {p = 1} ^ {q} (\sum_ {j = 1} ^ {n} \lambda_ {j} ^ {(p)} Y _ {r j} ^ {(p)}) \geq Y _ {r k}, \quad r = 1, \dots , s\tag{15.2}
$$

$$
\lambda_ {j} ^ {(p)} \geq 0, \quad p = 1,..., q, j = 1,..., n
$$

θunrestricted in sign:

Again, this model is exactly the same as Model (11) for the series system when the terms associated with the intermediate product are omitted. Values in parentheses in Eqs. (15.1) and (15.2), i.e. $\stackrel { \bullet } { \Sigma _ { j } ^ { n } } { = } _ { 1 } \lambda _ { j } ^ { ( p ) } X _ { i j } ^ { ( p ) }$ and $\Sigma _ { j = 1 } ^ { n } \lambda _ { j } ^ { ( p ) } Y _ { r j , \ j } ^ { ( p ) } ,$ , are targets for Process p on optimality. Their sums, $\Sigma _ { p = 1 } ^ { q } \bar { \Sigma } _ { j = 1 } ^ { n } \bar { \lambda } _ { j } ^ { ( p ) } \bar { X } _ { i j } ^ { ( p ) }$ and $\Sigma _ { p = 1 } ^ { q } \Sigma _ { j = 1 } ^ { n } \lambda _ { j } ^ { ( p ) } Y _ { r j } ^ { ( p ) }$ , are targets for the system. When all processes have the same technology, that is, all q sets of ${ \mathrm { \dot { \langle } } } \lambda _ { j } ^ { ( p ) } , j { = } 1 , . . . , n ,$ are equal, then Model (15) becomes conventional DEA Model (2).

In the review of previous studies, research in network DEA can be classi<sup>fi</sup>ed, at the <sup>fi</sup>rst level, according to the network structure they discuss, i.e., series, parallel, or mixed. For each structure, three types of model for calculating the ef<sup>fi</sup>ciency are identi<sup>fi</sup>ed at the second level: independent models, connected models, and relational models. For independent models, each process is treated as an independent DMU when calculating the process ef<sup>fi</sup>ciency. For connected models, the performance of each process is taken into account when calculating the system ef<sup>fi</sup>ciency. However, the system ef<sup>fi</sup>ciency does not necessarily have any relationship with the process ef<sup>fi</sup>ciencies. Finally, for relational models, speci<sup>fi</sup>c relationship between the system ef<sup>fi</sup>ciency and the process ef<sup>fi</sup>ciencies can be derived. The classi<sup>fi</sup>cation is shown in Table 2.

## 4. IT impact on <sup>fi</sup>rm performance

Information technology (IT) is a fast developing tool that assists business operations. Several articles have investigated its impact on performance at different levels [2]. The study of Bender [6] on insurance <sup>fi</sup>rms indicated that IT investments were signi<sup>fi</sup>cantly correlated with <sup>fi</sup>rm pro<sup>fi</sup>tability. Brynjolfsson and Hitt [8,9] also found a positive relationship between IT investment and <sup>fi</sup>rm performance. Banker et al. [4] showed that IT improved the operational ef<sup>fi</sup>ciency of <sup>fi</sup>rms. However, there are also studies [22,66] that have pointed out that IT has little effect on business performance. According to Kauffman and Weill [38], this contradiction was due to the effects of unidenti<sup>fi</sup>ed mediating variables between IT investments and <sup>fi</sup>rm performance. They believe that the impact of IT on <sup>fi</sup>rm performance was indirect, and suggested the use of a two-stage model to explicitly incorporate the intermediate factors in the investigation.

Based on the idea of Kauffman and Weill [38], Wang et al. [65] separated the problem of assessing the impact of IT on bank performance into two stages connected in series. The <sup>fi</sup>rst stage is a fund collection stage, where IT is applied to collect funds from bank customers in the form of deposits. The second stage is a pro<sup>fi</sup>t generation stage, where deposits collected in the <sup>fi</sup>rst stage are invested in securities and provided for loans. The impact of IT on bank performance acts indirectly through fund collection. A bank with unsatisfactory performance, in terms of pro<sup>fi</sup>ts gained, may not be the result of unsatisfactory IT utilization in the <sup>fi</sup>rst stage, but due to improper investments and loans in the second stage.

Three factors were selected by Wang et al. [65] as the inputs for the <sup>fi</sup>rst stage: IT budget $\left( X _ { 1 } \right)$ , <sup>fi</sup>xed assets $( X _ { 2 } )$ , and the number of employees $( X _ { 3 } ) ;$ ; and one factor as the output: the dollar value of deposits $( Z )$ , which was in turn used as the input for the second stage. The outputs considered from the second stage were: pro<sup>fi</sup>ts earned $\left( Y _ { 1 } \right)$ and the percentage of loans recovered $( Y _ { 2 } )$ . The data set consists of 36 observations of 22 <sup>fi</sup>rms in the years 1987–1989. To avoid obtaining unreasonable results in DEA, <sup>fi</sup>rms with negative pro<sup>fi</sup>ts were omitted in this paper. Twenty-seven observations are left, as shown in Table 3.

Data set for assessing IT impact on <sup>fi</sup>rm performance

<table><tr><td rowspan="3">DMU</td><td>IT budget</td><td>Fixed assets</td><td>No. of employees</td><td>Deposits</td><td>Profit</td><td rowspan="2">Fraction of loans recovered</td></tr><tr><td>($ billions)</td><td>($ billions)</td><td>(thousands)</td><td>($ billions)</td><td>($ billions)</td></tr><tr><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td>Z</td><td> $Y_1$ </td><td> $Y_2$ </td></tr><tr><td>1</td><td>0.150</td><td>0.713</td><td>13.3</td><td>14.478</td><td>0.232</td><td>0.986</td></tr><tr><td>2</td><td>0.170</td><td>1.071</td><td>16.9</td><td>19.502</td><td>0.340</td><td>0.986</td></tr><tr><td>3</td><td>0.235</td><td>1.224</td><td>24.0</td><td>20.952</td><td>0.363</td><td>0.986</td></tr><tr><td>4</td><td>0.211</td><td>0.363</td><td>15.6</td><td>13.902</td><td>0.211</td><td>0.982</td></tr><tr><td>5</td><td>0.133</td><td>0.409</td><td>18.485</td><td>15.206</td><td>0.237</td><td>0.984</td></tr><tr><td>6</td><td>0.497</td><td>5.846</td><td>56.42</td><td>81.186</td><td>1.103</td><td>0.955</td></tr><tr><td>7</td><td>0.060</td><td>0.918</td><td>56.42</td><td>81.186</td><td>1.103</td><td>0.986</td></tr><tr><td>8</td><td>0.071</td><td>1.235</td><td>12.0</td><td>11.441</td><td>0.199</td><td>0.985</td></tr><tr><td>9</td><td>1.500</td><td>18.120</td><td>89.51</td><td>124.072</td><td>1.858</td><td>0.972</td></tr><tr><td>10</td><td>0.120</td><td>1.821</td><td>19.8</td><td>17.425</td><td>0.274</td><td>0.983</td></tr><tr><td>11</td><td>0.120</td><td>1.915</td><td>19.8</td><td>17.425</td><td>0.274</td><td>0.983</td></tr><tr><td>12</td><td>0.050</td><td>0.874</td><td>13.1</td><td>14.342</td><td>0.177</td><td>0.985</td></tr><tr><td>13</td><td>0.370</td><td>6.918</td><td>12.5</td><td>32.491</td><td>0.648</td><td>0.945</td></tr><tr><td>14</td><td>0.440</td><td>4.432</td><td>41.9</td><td>47.653</td><td>0.639</td><td>0.979</td></tr><tr><td>15</td><td>0.431</td><td>4.504</td><td>41.1</td><td>52.630</td><td>0.741</td><td>0.981</td></tr><tr><td>16</td><td>0.110</td><td>1.241</td><td>14.4</td><td>17.493</td><td>0.243</td><td>0.988</td></tr><tr><td>17</td><td>0.053</td><td>0.450</td><td>7.6</td><td>9.512</td><td>0.067</td><td>0.980</td></tr><tr><td>18</td><td>0.345</td><td>5.892</td><td>15.5</td><td>42.469</td><td>1.002</td><td>0.948</td></tr><tr><td>19</td><td>0.128</td><td>0.973</td><td>12.6</td><td>18.987</td><td>0.243</td><td>0.985</td></tr><tr><td>20</td><td>0.055</td><td>0.444</td><td>5.9</td><td>7.546</td><td>0.153</td><td>0.987</td></tr><tr><td>21</td><td>0.057</td><td>0.508</td><td>5.7</td><td>7.595</td><td>0.123</td><td>0.987</td></tr><tr><td>22</td><td>0.098</td><td>0.370</td><td>14.1</td><td>16.906</td><td>0.233</td><td>0.981</td></tr><tr><td>23</td><td>0.104</td><td>0.395</td><td>14.6</td><td>17.264</td><td>0.263</td><td>0.983</td></tr><tr><td>24</td><td>0.206</td><td>2.680</td><td>19.6</td><td>36.430</td><td>0.601</td><td>0.982</td></tr><tr><td>25</td><td>0.067</td><td>0.781</td><td>10.5</td><td>11.581</td><td>0.120</td><td>0.987</td></tr><tr><td>26</td><td>0.100</td><td>0.872</td><td>12.1</td><td>22.207</td><td>0.248</td><td>0.972</td></tr><tr><td>27</td><td>0.0106</td><td>1.757</td><td>12.7</td><td>20.670</td><td>0.253</td><td>0.988</td></tr></table>

Results of the IT impact on <sup>fi</sup>rm performance without considering the IT budget used in Process 2.

<table><tr><td rowspan="2">DMU</td><td colspan="2">Process 1</td><td colspan="2">Process 2</td><td colspan="2">System</td></tr><tr><td>Efficiency</td><td>Slack</td><td>Efficiency</td><td>Slack</td><td>Efficiency</td><td>Slack</td></tr><tr><td>1</td><td>0.6388</td><td>0.3612</td><td>0.7459</td><td>0.1623</td><td>0.4764</td><td>0.5236</td></tr><tr><td>2</td><td>0.6507</td><td>0.3493</td><td>0.5537</td><td>0.2904</td><td>0.3603</td><td>0.6397</td></tr><tr><td>3</td><td>0.5179</td><td>0.4821</td><td>0.7730</td><td>0.1176</td><td>0.4003</td><td>0.5997</td></tr><tr><td>4</td><td>0.5986</td><td>0.4014</td><td>0.7142</td><td>0.1711</td><td>0.4275</td><td>0.5725</td></tr><tr><td>5</td><td>0.5556</td><td>0.4444</td><td>0.7236</td><td>0.1536</td><td>0.4020</td><td>0.5980</td></tr><tr><td>6</td><td>0.7599</td><td>0.2401</td><td>0.5758</td><td>0.3223</td><td>0.4376</td><td>0.5624</td></tr><tr><td>7</td><td>1</td><td>0</td><td>0.5758</td><td>0.4242</td><td>0.5758</td><td>0.4242</td></tr><tr><td>8</td><td>0.5352</td><td>0.4648</td><td>0.8250</td><td>0.0937</td><td>0.4415</td><td>0.5585</td></tr><tr><td>9</td><td>0.6249</td><td>0.3751</td><td>0.6347</td><td>0.2283</td><td>0.3966</td><td>0.6034</td></tr><tr><td>10</td><td>0.4961</td><td>0.5039</td><td>0.7188</td><td>0.1395</td><td>0.3566</td><td>0.6434</td></tr><tr><td>11</td><td>0.4945</td><td>0.5055</td><td>0.7188</td><td>0.1391</td><td>0.3555</td><td>0.6445</td></tr><tr><td>12</td><td>0.6685</td><td>0.3315</td><td>0.5949</td><td>0.2708</td><td>0.3977</td><td>0.6023</td></tr><tr><td>13</td><td>0.9487</td><td>0.0513</td><td>0.8582</td><td>0.1345</td><td>0.8141</td><td>0.1859</td></tr><tr><td>14</td><td>0.5880</td><td>0.4120</td><td>0.5783</td><td>0.2480</td><td>0.3400</td><td>0.6600</td></tr><tr><td>15</td><td>0.6582</td><td>0.3418</td><td>0.6034</td><td>0.2610</td><td>0.3972</td><td>0.6028</td></tr><tr><td>16</td><td>0.6646</td><td>0.3354</td><td>0.6434</td><td>0.2370</td><td>0.4276</td><td>0.5724</td></tr><tr><td>17</td><td>0.7177</td><td>0.2823</td><td>0.7877</td><td>0.1524</td><td>0.5653</td><td>0.4347</td></tr><tr><td>18</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>19</td><td>0.8144</td><td>0.1856</td><td>0.5926</td><td>0.3318</td><td>0.4825</td><td>0.5175</td></tr><tr><td>20</td><td>0.6933</td><td>0.3067</td><td>1</td><td>0</td><td>0.6933</td><td>0.3067</td></tr><tr><td>21</td><td>0.7067</td><td>0.2933</td><td>0.9935</td><td>0.0046</td><td>0.7022</td><td>0.2978</td></tr><tr><td>22</td><td>0.7942</td><td>0.2058</td><td>0.6408</td><td>0.2852</td><td>0.5089</td><td>0.4911</td></tr><tr><td>23</td><td>0.7802</td><td>0.2198</td><td>0.6993</td><td>0.2346</td><td>0.5456</td><td>0.4544</td></tr><tr><td>24</td><td>0.9300</td><td>0.0700</td><td>0.7135</td><td>0.2664</td><td>0.6636</td><td>0.3364</td></tr><tr><td>25</td><td>0.6270</td><td>0.3730</td><td>0.6516</td><td>0.2185</td><td>0.4085</td><td>0.5915</td></tr><tr><td>26</td><td>1</td><td>0</td><td>0.5152</td><td>0.4848</td><td>0.5152</td><td>0.4848</td></tr><tr><td>27</td><td>1</td><td>0</td><td>0.5644</td><td>0.4356</td><td>0.5644</td><td>0.4356</td></tr><tr><td>Average</td><td>0.7036</td><td>0.2791</td><td>0.6917</td><td>0.2151</td><td>0.4867</td><td>0.4942</td></tr></table>

This problem does not have <sup>fi</sup>nal products for the <sup>fi</sup>rst stage nor exogenous inputs for the second. By applying a simpli<sup>fi</sup>ed version of Model (8) and Eqs. (9.1) and (9.2) for general series systems, the system and process ef<sup>fi</sup>ciencies were calculated; the results are shown in Table 4. As a result of the relational model, the system ef<sup>fi</sup>ciency is the product of the two process ef<sup>fi</sup>ciencies. There is only one DMU (No. 18) which is ef<sup>fi</sup>cient for both the system and processes. Excluding this DMU, there are three DMUs which are ef<sup>fi</sup>cient for the <sup>fi</sup>rst stage and one which is ef<sup>fi</sup>cient for the second. Wang et al. [65] calculated the system and process ef<sup>fi</sup>ciencies independently. In their study, Unit 31 (Unit 23 in this study) has greater corresponding process ef<sup>fi</sup>ciencies than those of Unit 30 (Unit 22 in this study), yet smaller overall system ef<sup>fi</sup>ciency. This kind of unreasonable result will not occur in the relational model. Chen and Zhu [21] prepared a model to calculate the two process ef<sup>fi</sup>ciencies in one linear program, but were unable to obtain the system ef<sup>fi</sup>ciency at the same time. Although the system ef<sup>fi</sup>ciency can be calculated separately, the process ef<sup>fi</sup>ciencies do not have a mathematical relationship with the system ef<sup>fi</sup>ciency.

To maintain the property “when the processes are connected in series, the system ef<sup>fi</sup>ciency is the product of the process ef<sup>fi</sup>ciencies” of the relational model, we calculated the geometric mean, instead of the arithmetic mean, of the 27 DMUs. The results in the last row of Table 4 show that the system average, 0.4867, is still the product of the two process averages, 0.7036 and 0.6917. Due to the product effect, the system average is rather low. However, the average for Process 1 is the highest of the three averages, indicating an indirect impact of IT on bank performance

Another property of the relational model is that the inef<sup>fi</sup>ciency of the system is the sum of the values of the two process slacks. Referring to Table 4, the (arithmetic) average of the system slack is 0.4942, which is the sum of the averages of the two process slacks, 0.2791 and 0.2151. The proportions are 0.5648 and 0.4352, respectively, indicating that 56.48% of the system inef<sup>fi</sup>ciency is due to Process 1 and 43.52% is due to Process 2. Since the system slack is just the complement of the system ef<sup>fi</sup>ciency, the average system slack of all banks should be the complement of the average system ef<sup>fi</sup>ciency. Here, the average of system slacks, 0.4942, is different from the complement of the average system ef<sup>fi</sup>ciency, 1−0.4867, because the former is an arithmetic average while the latter is a geometric average.

In the above discussion, it was assumed that IT is used exclusively in Stage 1. However, many banks implement a loan process system in the pro<sup>fi</sup>t generation stage. Taking this into account, the structure of the series system becomes that shown in Fig. 5, where Process 2 utilizes an exogenous input, IT budget, in addition to the intermediate product, deposits, produced by Process 1. Due to a lack of information on how IT budgets were spent, we assume that a bank utilizes a proportion α of the IT budget for Process 1 operations and (1−α) for Process 2. Since the value of α is unknown, similar to selecting the virtual multiplier for each factor, we allow each bank to select the most favorable value of α in calculating the system ef<sup>fi</sup>ciency. For the purposes of this paper, we restrict the value of α to the range of [0.6, 0.9]. This idea has been applied in many studies discussing the effect of shared resources [5,24,28,67].

Incorporating this idea into our banking problem, the model for calculating the system and process ef<sup>fi</sup>ciencies becomes:

$$
\begin{array}{l} E _ {k} = \max. u _ {1} Y _ {1 k} + u _ {2} Y _ {2 k} \\ \text {s.t.} v _ {1} X _ {1 k} + v _ {2} X _ {2 k} + v _ {3} X _ {3 k} = 1 \\ \qquad w Z _ {j} - (v _ {1} \alpha X _ {1 j} + v _ {2} X _ {2 j} + v _ {3} X _ {3 j}) \leq 0, j = 1,..., 2 7 \\ \qquad u _ {1} Y _ {1 j} + u _ {2} Y _ {2 j} - [ w Z _ {j} + v _ {1} (1 - a) X _ {1 j} ] \leq 0, \qquad j = 1,... \\ \qquad 0. 6 \leq \alpha \leq 0. 9 \quad u _ {1}, u _ {2}, v _ {1}, v _ {2}, v _ {3}, w \geq \varepsilon , \end{array}\tag{16.1}
$$

<sub>ð</sub>16:2<sub>Þ</sub>

where constraint sets Eqs. (16.1) and (16.2) correspond to Processes 1 and 2, respectively. This model is nonlinear due to the nonlinear term $\nu _ { 1 } \alpha .$ Beasley [5] applied a nonlinear programming software package, GINO, to solve this type of problem. This nonlinear program can be linearized by substituting v α by a new variable, v̂, and replacing the constraint $0 . 6 { \le } \mathbf { { \alpha } } \le 0 . 9$ by $0 . 6 \nu _ { 1 } \leq \hat { \mathsf { v } } \leq 0 . 9 \nu _ { 1 } .$ . After the optimal values for v and v̂ are obtained, the optimal value for α is calculated as $\alpha = \hat { \mathsf { v } } / v _ { 1 }$ . Table 5 shows the results in a form similar to that of Table 4.

When a portion of the IT budget is shared with Process 2, the average of the system ef<sup>fi</sup>ciencies is increased from 0.4867 to 0.5362, approximately 10.2%. Note that the same geometric average has been used so that the results are comparable with those of Table 4. The increase is clearly due to the contribution of IT on Process 2 operations. In addition to DMU 18, two more DMUs, No. 7 and No. 27, are ef<sup>fi</sup>cient at the system level. The average ef<sup>fi</sup>ciency of Process 1 has dropped from 0.7036 to 0.6951, approximately 1.2%, because a portion of the IT budget, (1−α), is switched from this process to Process 2. Of the 27 DMUs,17 have the same ef<sup>fi</sup>ciency value as before and ten have smaller values. In contrast, the average ef<sup>fi</sup>ciency of Process 2 is increased from 0.6917 to 0.7472, approximately 8.0%, with 14 DMUs having higher, ten having the same, and three having smaller values. The reason, again, is that (1−α) of the IT budget has been switched to this process. Thus, switching a portion of the IT budget from Process 1 to Process 2 produces a relatively small decrease (1.2%) in the ef<sup>fi</sup>ciency of Process 1, and a relatively larger increase (8.0%) in the ef<sup>fi</sup>ciency of Process 2. The aggregated effect is a 10.2% increase on the system ef<sup>fi</sup>ciency.

![](/api/attachments/ZZ6E5RAQ/fulltext/images/b029ecde172086c09976c0c7a1a141564710c0eda870081b1380c0925f4d4e1e.jpg)  
Fig. 5. IT budget shared by Processes 1 and 2.

Table 5  
Results of the IT impact on <sup>fi</sup>rm performance considering the IT budget used in Process 2.

<table><tr><td rowspan="2">DMU</td><td colspan="2">Process 1</td><td colspan="2">Process 2</td><td colspan="2">System</td></tr><tr><td>Efficiency</td><td>Slack</td><td>Efficiency</td><td>Slack</td><td>Efficiency</td><td>Slack</td></tr><tr><td>1</td><td>0.6388</td><td>0.3612</td><td>0.7459</td><td>0.1623</td><td>0.4764</td><td>0.5236</td></tr><tr><td>2</td><td>0.6507</td><td>0.3493</td><td>0.7819</td><td>0.1419</td><td>0.5087</td><td>0.4913</td></tr><tr><td>3</td><td>0.5179</td><td>0.4821</td><td>0.7730</td><td>0.1176</td><td>0.4003</td><td>0.5997</td></tr><tr><td>4</td><td>0.5986</td><td>0.4014</td><td>0.7142</td><td>0.1711</td><td>0.4275</td><td>0.5725</td></tr><tr><td>5</td><td>0.5556</td><td>0.4444</td><td>0.7236</td><td>0.1536</td><td>0.4020</td><td>0.5980</td></tr><tr><td>6</td><td>0.7599</td><td>0.2145</td><td>0.6014</td><td>0.3131</td><td>0.4724</td><td>0.5276</td></tr><tr><td>7</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>8</td><td>0.5339</td><td>0.4261</td><td>0.8505</td><td>0.0858</td><td>0.4881</td><td>0.5119</td></tr><tr><td>9</td><td>0.6249</td><td>0.3751</td><td>0.6347</td><td>0.2283</td><td>0.3966</td><td>0.6034</td></tr><tr><td>10</td><td>0.4961</td><td>0.4595</td><td>0.7325</td><td>0.1446</td><td>0.3959</td><td>0.6041</td></tr><tr><td>11</td><td>0.4939</td><td>0.4616</td><td>0.7325</td><td>0.1440</td><td>0.3943</td><td>0.6057</td></tr><tr><td>12</td><td>0.5400</td><td>0.3755</td><td>0.7870</td><td>0.1330</td><td>0.4915</td><td>0.5085</td></tr><tr><td>13</td><td>0.9487</td><td>0.0513</td><td>0.8582</td><td>0.1345</td><td>0.8141</td><td>0.1859</td></tr><tr><td>14</td><td>0.5798</td><td>0.3694</td><td>0.5637</td><td>0.2751</td><td>0.3555</td><td>0.6445</td></tr><tr><td>15</td><td>0.6515</td><td>0.3065</td><td>0.6018</td><td>0.2762</td><td>0.4173</td><td>0.5827</td></tr><tr><td>16</td><td>0.6632</td><td>0.3012</td><td>0.6640</td><td>0.2348</td><td>0.4640</td><td>0.5360</td></tr><tr><td>17</td><td>0.7113</td><td>0.2596</td><td>0.8207</td><td>0.1327</td><td>0.6077</td><td>0.3923</td></tr><tr><td>18</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>19</td><td>0.7871</td><td>0.1873</td><td>0.6040</td><td>0.3218</td><td>0.4908</td><td>0.5092</td></tr><tr><td>20</td><td>0.6784</td><td>0.2821</td><td>1</td><td>0</td><td>0.7179</td><td>0.2821</td></tr><tr><td>21</td><td>0.6931</td><td>0.2707</td><td>0.9889</td><td>0.0081</td><td>0.7212</td><td>0.2788</td></tr><tr><td>22</td><td>0.7942</td><td>0.2058</td><td>0.6408</td><td>0.2852</td><td>0.5089</td><td>0.4911</td></tr><tr><td>23</td><td>0.7802</td><td>0.2198</td><td>0.6993</td><td>0.2346</td><td>0.5456</td><td>0.4544</td></tr><tr><td>24</td><td>0.9300</td><td>0.0617</td><td>0.7511</td><td>0.2335</td><td>0.7048</td><td>0.2952</td></tr><tr><td>25</td><td>0.6270</td><td>0.3383</td><td>0.6754</td><td>0.2148</td><td>0.4469</td><td>0.5531</td></tr><tr><td>26</td><td>1</td><td>0</td><td>0.5558</td><td>0.4442</td><td>0.5558</td><td>0.4442</td></tr><tr><td>27</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Average</td><td>0.6951</td><td>0.2668</td><td>0.7472</td><td>0.1700</td><td>0.5362</td><td>0.4369</td></tr></table>

This effect can be also discussed with respect to the slack variable. The average value of the system slacks decreased from 0.4942 to 0.4369. For the two processes, Process 1 dropped from 0.2791 to 0.2668 and Process 2 dropped from 0.2151 to 0.1700, both have dropped. In proportion of the system slack, Process 1 is increased from 56.48% to 61.08% and Process 2 is dropped from 43.52% to 38.92%.

It should be noted that the impact of IT on <sup>fi</sup>rm performance is indirect. If the indirect relationship is not speci<sup>fi</sup>ed correctly, then the impact may not be revealed. For example, the relationship between IT and <sup>fi</sup>rm performance speci<sup>fi</sup>ed in this study is a two-stage production process connected by the intermediate product, deposits. It is observed that the impact of IT on <sup>fi</sup>rm performance cannot be accurately determined because IT also appears in the second stage, although the proportion is relatively small. It should also be noted that the boundary of IT is vague. For example, what IT expenditures should be included and which employees should be considered as IT employees is unclear. All these will affect the impact of IT on <sup>fi</sup>rm performance.

This example discusses the IT impact on <sup>fi</sup>rm performance for a speci<sup>fi</sup>c period. The operation of <sup>fi</sup>rms is usually long-term. The performance of one period will affect the performance of the next. For example, the pro<sup>fi</sup>t of a period will be partly returned to stockholders as dividends and partly reinvested in the next period. In other words, the money for generating pro<sup>fi</sup>t is not only from deposits collected in the current period, but also from the pro<sup>fi</sup>ts of the previous period. Moreover, the IT budget, assets, and number of employees may be different from period to period. The performance assessment problem is actually dynamic, with the structure shown in Fig. 6. For a horizon of T periods, the ef<sup>fi</sup>ciencies of fund collection and pro<sup>fi</sup>t generation in each period can be measured by applying the network DEA model introduced in this paper. The long-term performance of the system is an aggregation of the performance of individual periods. Since the same factor at different stages may have different imputed price due to the opportunity cost of time, different multipliers may be used. However, the intermediate product at the same stage, for example, deposits in Fig. 6, should have the same multiplier no matter whether it is the output of Process 1 or the input of Process 2. The results give a better idea of the performance of the two processes, fund collection and pro<sup>fi</sup>t generation, and a clearer picture of the impact of IT on <sup>fi</sup>rm performance.

## 5. Conclusion

Conventional DEA models for measuring the ef<sup>fi</sup>ciency of a system treat the system as a black box, disregarding its internal structure. More representative and informative results can be obtained if interactions of the component processes within the system are taken into account. The independent network approach calculates the system and process ef<sup>fi</sup>ciencies independently, which sometimes produces inconsistent results between the system and process ef<sup>fi</sup>ciencies. The connected network approach does not have this problem, but the relationship between the system ef<sup>fi</sup>ciencyand process ef<sup>fi</sup>ciencies cannot be obtained.

This paper discusses a relational network approach which took into account interactions between component processes when calculating the system ef<sup>fi</sup>ciency. The system and process ef<sup>fi</sup>ciencies can be calculated at the same time and the relationship between them can be obtained: the system slack is the sum of process slacks. Based on this relationship, the system inef<sup>fi</sup>ciency can be distributed to processes according to the proportion of process slack in the system slack. The key processes, which cause the system to be inef<sup>fi</sup>cient, are thus consistently identi<sup>fi</sup>ed.

![](/api/attachments/ZZ6E5RAQ/fulltext/images/e2c89241b37483b124b043f57e1083560c2e3d3279fa5090d2d8b2d8412ac48b.jpg)  
Fig. 6. Dynamic system for performance assessment.

The problem of “the IT impact on <sup>fi</sup>rm performance” was discussed. The impact of ITon <sup>fi</sup>rm performance is indirectly through an IT-produced product, namely deposits. This conclusion is consistent with those of previous studies. For the bank system, approximately 56% and 44% of the system inef<sup>fi</sup>ciency were attributed to the two component processes, fund collection and pro<sup>fi</sup>t generation, respectively. By allowing a portion of the IT budget to switch from the fund collection operations to pro<sup>fi</sup>t generation operations, the bank performance improved approximately 10.2%. This result also provides a better estimate of the bank performance.

The model discussed in this paper was a CCR-type model with the underlying assumption of constant returns to scale. It should not be dif<sup>fi</sup>cult to extend it to the BCC-type model [3] to accommodate situations of variable returns to scale. The economies of scale of the system and component processes can then be discussed. With the <sup>fl</sup>exibility of the relational model for modeling general network systems, the dynamic performance of the bank system in the long run can also be measured to obtain a clearer idea of the IT impact on <sup>fi</sup>rm performance.

Recently, the ef<sup>fi</sup>ciency of banking <sup>fi</sup>rms has received increased interest due to bad performing loans. Bad performing loans, if they exist, cannot be ignored in ef<sup>fi</sup>ciency evaluation because they increase managerial risk. Since conventional DEA models fail to account for risk factors, the resulting ef<sup>fi</sup>ciency measures will be biased if a banking <sup>fi</sup>rm has bad performing loans. The network DEA model can deal with risk factors by incorporating them as undesirable output. This concern provides a direction for future study.

## Acknowledgments

This research is supported by the National Science Council, Republic of China (Taiwan), under contract number NSC95-2416-H-006-026-MY3.

## References

[1] J.H. Ahn, S.G. Chang, Assessing the contribution of knowledge to business performance: the KP<sup>3</sup> methodology, Decision Support Systems 36 (2004) 403–416

[2] J.Y. Bakos, C.F. Kemerer, Recent applications of economic theory in information technology research, Decision Support Systems 8 (1992) 365–386.

[3] R.D. Banker, A. Charnes, W.W. Cooper, Some models for estimating technical and scale ef<sup>fi</sup>ciencies in data envelopment analysis, Management Science 30 (1984) 1078-1092.

[4] R.D. Banker, R.J. Kauffman, R.C. Morey, Measuring gains in operational ef<sup>fi</sup>ciency from information technology: a study of the Positran deployment at Hardee’s Inc, Journal of Management Information Systems 7 (1990) 29–54.

[5] J.E. Beasley, Determining teaching and research ef<sup>fi</sup>ciencies, Journal of Operational Research Society 46 (1995) 441–452.

[6] D. Bender, Financial impact of information processing, Journal of Management Information Systems 3 (1986) 232–238.

[7] E.W.N. Bernroider, V. Stix, Pro<sup>fi</sup>le distance method—a multi-attribute decision making approach for information system investments, Decision Support Systems 42 (2006) 988–998.

[8] E. Brynjolfsson, L. Hitt, Paradox lost? Firm-level evidence on the returns to information systems spending, Management Science 42 (1996) 541–558

[9] E. Brynjolfsson, L. Hitt, Beyond the productivity paradox, Communications of the ACM.41 (1998).49-56

[10] P.E. Byrnes, J.E. Storbeck, Ef<sup>fi</sup>ciency gains from regionalization: economic development in China revisited, Socio-Economic Planning Sciences 34 (2000) 141–154.

[11] L. Castelli, R. Pesenti, W. Ukovich, DEA-like models for the ef<sup>fi</sup>ciency evaluation of hierarchically structured units, European Journal of Operational Research 154 (2004) 465–476.

[12] A. Charnes, W.W. Cooper, The non-Archimedean CCR ratio for ef<sup>fi</sup>ciency analysis: a rejoinder to Boyd and Färe, European Journal of Operational Research 15 (1984) 333-334

[13] A. Charnes, W.W. Cooper, B. Golany, R. Halek, G. Klopp, E. Schmitz, D. Thomas, Two phase data envelopment analysis approach to policy evaluation and management of army recruiting activities: tradeoffs between joint services and army advertising, Research Report CCS no. 532, Center for Cybernetic Studies, The University of Texas, Austin, Texas, 1986.

[14] A. Charnes, W.W. Cooper, A.R. Lewin, L.M. Seiford, Data envelopment analysis: theory, methodology and applications, Kluwer Academic Publishers, Boston, 1994

[15] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the ef<sup>fi</sup>ciency of decision making units, European Journal of Operational Research 2 (1978) 429–444

[16] A. Charnes, W.W. Cooper, E. Rhodes, Short communication: measuring the ef<sup>fi</sup>ciency of decision making units, European Journal of Operational Research 3 (1979) 339.

[17] C.M. Chen, A network-DEA model with new ef<sup>fi</sup>ciency measures to incorporate the dynamic effect in production networks, European Journal of Operational Research 194 (2009) 687–699.

[18] Y. Chen, W.D. Cook, N. Li, J. Zhu, Additive ef<sup>fi</sup>ciency decomposition in two-stage DEA, European Journal of Operational Research 196 (2009) 1170–1176.

[19] Y. Chen, L. Liang, F. Yang, J. Zhu, Evaluation of information technology investment: a data envelopment analysis approach, Computers & Operations Research 33 (2006) 1368–1379.

[20] Y. Chen, L. Liang, J. Zhu, Equivalence in two-stage DEA approaches, European Journal of Operational Research 193 (2009) 600–604

[21] Y. Chen, J. Zhu, Measuring information technology's indirect impact on <sup>fi</sup>rm performance, Information Technology & Management Journal 5 (2004) 9–22.

[22] W. Cron, M. Sobol, The relationship between computerization and performance: a strategy for maximizing economic bene<sup>fi</sup>ts of computerization, Information and Management 6 (1983) 171–181.

[23] R. Färe, Measuring Farrell ef<sup>fi</sup>ciency for a <sup>fi</sup>rm with intermediate inputs, Academia Economic Papers 19 (1991) 329–340.

[24] R. Färe, R. Grabowski, S. Grosskopf, S. Kraft, Ef<sup>fi</sup>ciency of a <sup>fi</sup>xed but allocatable input: a non-parametric approach, Economics Letters 56 (1997) 187–193.

[25] R. Färe, S. Grosskopf, Intertemporal Production Frontiers: With Dynamic DEA Kluwer Academic Publishers, Boston, 1996

[26] R. Färe, S. Grosskopf, Productivity and intermediate products: a frontier approach, Economics Letters 50 (1996) 65–70.

[27] R. Färe, S. Grosskopf, Network DEA, Socio-Economic Planning Sciences 34 (2000) 35-49.

[28] R. Färe, S. Grosskopf, S.K. Li, Linear programming models for <sup>fi</sup>rm and industry performance, Scandinavian Journal of Economics 94 (1992) 599–608.

[29] R. Färe, D. Primont, Ef<sup>fi</sup>ciency measures for multiplant <sup>fi</sup>rms, Operations Research Letters 3 (1984) 257–260.

[30] R. Färe, G. Whittaker, An intermediate input model of dairy production using complex survey data, Journal of Agricultural Economics 46 (1995) 201–213.

[31] B. Golany, S.T. Hackman, U. Passy, An ef<sup>fi</sup>ciency measurement framework for multi-stage production systems, Annals of Operations Research 145 (2006) 51–68.

[32] ISI Web of Knowledge, http://apps.isiknowledge.com/, August 10, 2008 visited.

[33] E.C. Jaenicke, Testing for intermediate outputs in dynamic DEA models: accounting for soil capital in rotational crop production and productivity measures, Journal of Productivity Analysis 14 (2000).247-266

[34] C. Kao, Measuring the ef<sup>fi</sup>ciency of forest districts with multiple working circles, Journal of Operational Research Society 49 (1998) 583–590.

[35] C. Kao, Ef<sup>fi</sup>ciency decomposition in network data envelopment analysis: a relational model, European Journal of Operational Research 192 (2009) 949–962.

[36] C. Kao, Ef<sup>fi</sup>ciency measurement for parallel production systems, European Journal of Operational Research 196 (2009) 1107–1112.

[37] C. Kao, S.N. Hwang, Ef<sup>fi</sup>ciency decomposition in two-stage data envelopment analysis: an application to non-life insurance companies in Taiwan, European Journal of Operational Research 185 (2008) 418–429.

[38] R.J. Kauffman, P. Weill, An evaluative framework for research on the performance effects of Information Technology investment, Proceedings of the 10th International Conference on Information Systems, Boston, MA, 1989, pp. 377–388.

[39] H.F. Lewis, T.R. Sexton, Network DEA: efficiency analysis of organizations with complex internal structure, Computers & Operations Research 31 (2004) 1365–1410.

[40] S.F. Lo, W.M. Lu, Does size matter? Finding the pro<sup>fi</sup>tability and marketability benchmark of <sup>fi</sup>nancial holding companies, Asia-Paci<sup>fi</sup>c Journal of Operational Research 23 (2006) 229–246.

[41] M. Löthgren, M. Tambour, Productivity and customer satisfaction in Swedish pharmacies: a DEA network model, European Journal of Operational Research 115 (1999) 449–458.

[42] C.A.K. Lovell, L.C. Walters, L.L. Wood, Strati<sup>fi</sup>ed models of education production using modi<sup>fi</sup>ed DEA and regression analysis, in: A. Charnes, W.W. Cooper, A.Y. Lewin, L.M. Seiford (Eds.), Data envelopment analysis: theory, methodology, and application, Kluwer, Boston, 1994, pp. 329–351.

[43] X.M. Luo, Evaluating the pro<sup>fi</sup>tability and marketability of large banks—an application of data envelopment analysis, Journal of Business Research 56 (2003) 627–635.

[44] M. Mannino, S.N. Hong, I.J. Choi, Ef<sup>fi</sup>ciency evaluation of data warehouse operations, Decision Support Systems 44 (2008) 883–898.

[45] C. Mar Molinero, On the joint determination of ef<sup>fi</sup>ciencies in a data envelopment analysis context, Journal of Operational Research Society 47 (1996) 1273–1279.

[46] J. Nemoto, M. Goto, Dynamic data envelopment analysis modeling intertemporal behavior of a firm in the presence of productive inefficiencies. Economics Letters 64 (1999) 51–56.

[47] J. Nemoto, M. Goto, Measuring dynamic ef<sup>fi</sup>ciency in production: an application of data envelopment analysis to Japanese electric utilities, Journal of Productivity Analvsis 19 (2003)191-210

[48] A.G. Noulas, T. Hatzigayios, J. Lazaridis, K. Lyroudi, Non-parametric production frontier approach to the study of ef<sup>fi</sup>ciency of non-life insurance companies in Greece, Journal of Financial Management and Analysis 14 (2001) 19–26

[49] P. Ouellette, L. Yan, Investment and dynamic DEA, Journal of Productivity Analysis 29 (2008) 235–247.

[50] J.H. Park, S.C. Park, Agent-based merchandise management in business-tobusiness electronic commerce, Decision Support Systems 35 (2003) 311–333.

[51] P.C. Pendharkar, J.A. Rodger, Technical ef<sup>fi</sup>ciency-based selection of learning cases to improve forecasting accuracy of neural networks under monotonicity assumption, Decision Support Systems 36 (2003) 117–136

[52] A.M. Prieto, J.L. Zo<sup>fi</sup>o, Network DEA ef<sup>fi</sup>ciency in input–output models: with an application to OECD countries, European Journal of Operational Research 178 (2007) 292–304.

[53] L.M. Seiford, J. Zhu, Pro<sup>fi</sup>tability and marketability of the top 55 US commercial banks, Management Science 45 (1999) 1270–1288.

[54] J.K. Sengupta, A dynamic ef<sup>fi</sup>ciency model using data envelopment analysis, International Journal of Production Economics 62 (1999) 209–218.

[55] C. Serrano-Cinca, Y. Fuertes-Callen, C. Mar-Molinero, Measuring DEA ef<sup>fi</sup>ciency in Internet companies, Decision Support Systems 38 (2005) 557–573.

[56] T.R. Sexton, H.F. Lewis, Two-stage DEA: an application to Major League Baseball Journal of Productivity Analysis 19 (2003) 227–249.

[57] T. Sueyoshi, K. Sekitani, Returns to scale in dynamic DEA, European Journal of Operational Research 161 (2005) 536–544.

[58] T. Sueyoshi, K. Sekitani, An occurrence of multiple projections in DEA-based measurement of technical ef<sup>fi</sup>ciency: theoretical comparison among DEA models from desirable properties, European Journal of Operational Research 196 (2009) 764–794.

[59] A.P. Tchangani, A satis<sup>fi</sup>cing game theory approach for group evaluation of production units, Decision Support Systems 42 (2006) 778–788.

[60] K. Tone, B.K. Sahoo, Scale, indivisibility and production function in data envelopment analysis, International Journal of Production Economics 84 (2003) 165–192.

[61] K. Tone, M. Tsutsui, Network DEA: a slacks-based measure approach, European Journal of Operational Research 197 (2009) 243–252.

[62] M.D. Troutt, P.J. Ambrose, C.K. Chan, Optimal throughput for multistage input– output processes, International Journal of Operations & Production Management 21 (2001) 148–158.

[63] P.F. Tsai, C. Mar Molinero, A variable returns to scale data envelopment analysi model for the joint determination of ef<sup>fi</sup>ciencies with an example of the UK health service, European Journal of Operational Research 141 (2002) 21–38.

[64] M. Tsutsui, M. Goto, A multi-division ef<sup>fi</sup>ciency evaluation of US electric power companies using a weighted slacks-based measure, Socio-Economic Planning Sciences 43 (2009) 201–208.

[65] C.H. Wang, R. Gopal, S. Zionts, Use of data envelopment analysis in assessing information technology impact on <sup>fi</sup>rm performance, Annals of Operations Research 73 (1997) 191–213.

[66] P. Weill, Strategic investment in Information Technology: an empirical study Information Age 12 (1990) 141–147.

[67] M.M. Yu, Measuring the ef<sup>fi</sup>ciency and return to scale status of multi-mode bus transit—evidence from Taiwan’s bus system, Applied Economics Letters 15 (2008) 647–653.

[68] M.M. Yu, E.T.J. Lin, Ef<sup>fi</sup>ciency and effectiveness in railway performance using a multi-activity network DEA model, Omega 36 (2008) 1005–1017.

[69] J. Zhu, Multi-factor performance measure model with an application to Fortune 500 companies, European Journal of Operational Research 123 (2000) 105–124.

Chiang Kao is a professor at the Department of Industrial and Information Management, National Cheng Kung University, Taiwan, Republic of China. He received his BS degree from National Taiwan University, Taiwan, and holds an MS and a Ph.D. degree both earned from Oregon State University, USA. His research interest is in the applications of operations research and IT, with articles published in journals such as INFORMS Journal on Computing, IEEE Trans. on Systems, Man and Cybernetics, Computers in Industry, Interfaces, European Journal of Operational Research, and Computers & Operations Research.

Shiuh-Nan Hwang is a professor at the Graduate School of Management, Ming Chuan University, Taiwan, Republic of China. He received his BS degree from National Taiwan University, MS degree from National Cheng Kung University, and Ph.D. from National Chiao Tung University. His research interest is in management in industries as well as the government sector, with several publications in European Journal of Operational Research, Computers & Operations Research, International Journal of Management, Tourism Management, Journal of Environmental Management, etc.
