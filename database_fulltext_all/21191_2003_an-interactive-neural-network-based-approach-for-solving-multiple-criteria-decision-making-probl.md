---
otero_id: 21191
otero_key: "TWHSWC7H"
title: "An interactive neural network-based approach for solving multiple criteria decision-making problems"
authors: "Jian Chen; Song Lin"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00141-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An interactive neural network-based approach for solving multiple criteria decision-making problems

Jian Chen\*, Song Lin

Research Center for Contemporary Management, School of Economics and Management, Tsinghua University, Beijing 100084, China

Received 1 December 2000; received in revised form 1 June 2002; accepted 1 July 2002

## Abstract

In this paper, a new approach for solving multiple criteria decision-making (MCDM) problems is proposed based on Decision Neural Network (DNN). The DNN is used to capture and represent the Decision Maker’s (DM’s) preference. Then, with DNN, an optimization problem is solved to search for the most desirable solution. Procedures of model modification through an interactive procedure, and model optimization are also discussed. An example is given to illustrate the approach and the result is compared with the Interactive FFANN Procedure [Manage. Sci. 42 (1996)]. The result shows that the DNN approach is an encouraging and robust method for solving MCDM problems. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Multiple criteria analysis; Neural networks; Interactive procedures

## 1. Introduction

Multiple criteria decision making (MCDM) exists extensively in the real-world applications. MCDM is difficult, as the criteria are generally incompatible with each other. This difficulty is reinforced when the Decision Maker (DM) needs to satisfy the constraints of the problem while fulfilling his conflicting goals. (MCDM with constraints is also known as multiple criteria optimization problem, and is named as multiple objective linear optimization programming (MOLP) when all the constraints and objective functions take linear form. For MOLP, see discussions of

Ref. [8].) Solving MCDM problems has been a popular research topic for many decades. Different approaches have been proposed by lots of researchers, such as STAM [1], Geoffrion method [5], the Analytic Hierarchy Process (AHP) [13], the Reference Point Method [23]. For a survey of MCDM methods and applications [4,16,19].

The key process for solving an MCDM problem is to capture the preference structure of the DM, and many approaches have been developed. Multi-attribute utility function (MAUF) represents one major method among them. Since how to decide the structure of MAUF is a tough task in practice, some simple decomposition forms have been recommended. Additive, multiplicative, and multilinear forms are most commonly used. However, to apply them, the preference structure of the DM should conform to certain conditions, such as the independence among the attributes. The underlying assumptions are so restrictive that these conditions could hardly be fulfilled in real world [10].

Great progress has been made in the research of artificial neural networks (ANNs) in recent years. The ANN has many attractive advantages: it does not need any priori assumptions of the form of the mapping, and a feed-forward ANN with three layers can represent any continuous mappings [7]. These advantages make ANN a promising tool in solving MCDM problems in terms of approximating the MAUF and representing the preference of the DM. (For discussions on the approximating capacity, see Refs. [9,11].) Different neural network-based methods include Connectionist Approach for Preference Assessment [22], the Adaptive FFANN [10] and the Interactive FFANN Procedure [20].

To solve MCDM problems using ANN, the most important issues to be considered are how to elicit preference information from the DM and how to use the DM’s preference to guide the search for the most desirable solution. To obtain preference information of DM, it is necessary for the DM to evaluate many alternatives that are associated with multiple, conflicting and non-commensurate criteria. Two methods are suggested in the previous neural network-based studies: to let the DM assess the alternatives and give a numerical result directly, or to ask the DM to make pairwise comparisons between different alternatives and then calculate the principal eigenvector of the reciprocal comparison matrix, which is similar to the process in AHP [13]. The former (i.e., direct numerical ratings) is difficult in general, and the latter (pairwise comparison) is much easier. Also, the AHP-like methods (we call those methods that calculate the principal eigenvector of the pairwise comparison matrix AHPlike methods) are able to accommodate and handle the imprecise and conflict comparison results. However, the application of AHP causes a potential contradiction with ANN; we use ANN to capture the DM’s preference to avoid any priori assumptions of the structure of the preference while applying AHP requires some specific conditions. Furthermore, although traditional AHP-like methods are able to handle the conflicts, they may cause some ‘‘information loss’’ in terms of the training samples of the neural nets. (There are some new neural network-based methods that attempt to learn the conflict-solving mechanism in

AHP [17,21]). For example, in order to obtain the scores for 10 different alternatives, 10  (10 - 1)/ 2 = 45 comparisons need to be made (if the comparison matrix is full). Only those 10 ‘‘summary’’ scores are treated as the training data set for the neural network and the original 45 comparisons are ‘‘abandoned’’. As generally known, more training data points make the learning of the neural net more effective. That turns out to be a potential burden to the DM; he or she needs to make a large number of comparisons to achieve a sufficient number of training data set of the neural net. More errors tend to occur. We wish to use all these 45 points as training set and with more training data points the learning of the neural network is more effective.

Our purpose is to reduce DM’s cognitive burden and the number of evaluations while maintaining reliability and obtaining as more training data points as possible. Therefore, an alternative method, decision neural network (DNN), has been developed [3]. The DNN procedure is more similar to the way that a DM presents his/her preference information. Based on DNN, we propose an approach for solving MCDM problems in this paper—an interactive DNN approach. The approach developed in this paper can be used without assuming any specific function form for MAUF. With the approach presented in this paper, the DM can answer much fewer questions regarding pairwise assessments comparing with the traditional approaches. Furthermore, the DM may answer questions with flexibility to represent partial information about his preference to certain extent, e.g., the DM is asked to indicate pairwise comparison results in terms of approximate ratios or intervals rather than precise values. For more details about the discussion of approximate ratios and interval evaluations and how to apply them in the MCDM [14,15] and the software HIPRE [6]. Compared with the Interactive FFANN Procedure [20], the result shows that the DNN approach is an efficient and robust method for solving MCDM problems.

The rest of the paper is organized as follows. In Section 2, we provide some basic notations and definitions, while we discuss the interactive DNN approach phase by phase in Section 3. In Section 4, an example is presented to illustrate the approach proposed in this paper and some comparisons with the interactive FFANN procedure proposed by Sun et al. [20] are also given. Section 5 concludes the paper.

## 2. Notations and DNN

As for notation and terminology, a MCDM problem is written as

$$
\begin{array}{c} \max f (x) = [ f _ {1} (x), f _ {2} (x), \ldots , f _ {n} (x) ] ^ {T} \\ \text { s.t. } \qquad x \in X \end{array}\tag{1}
$$

where n is the number of criteria, $X$ is the decision space $( X$ can either be a continuous set or a discrete set), and $f _ { i } ( x )$ is the ith objective function. $\operatorname { I f } z _ { i }$ denotes the value of objective function $i ,$ the MCDM problem can be written as

$$
\max z = \left[ z _ {1}, z _ {2}, \dots , z _ {n} \right] ^ {T}
$$

$$
\begin{array}{l l} \text {s.t.} & x \in X \end{array}\tag{2}
$$

$$
z _ {i} = f _ {i} (x) \quad i = 1, 2, \dots , n
$$

Suppose $X$ is a continuous set, it can be represented by a set of inequalities: $g _ { i } \left( x \right) \leq 0 \ i = 1 , 2 , . \ . \ . , m$ , where m is the number of constraints.

Let $Z \subset R ^ { n }$ be the feasible region in criterion space where $z { \in } Z$ if and only if there exists an $x { \in } X$ such that $z { = } ( f _ { I } ( x ) , f _ { 2 } ( x ) , . . . , f _ { n } ( x ) ) ^ { T } .$ . Criterion vector $\bar { z } \in Z$ is nondominated if and only if there does not exist another $z { \in } Z$ such that $z _ { i } \geq \bar { z } _ { i }$ and for at least one $i , z _ { i } { > } \bar { z } _ { i } . \mathrm { ~ A ~ }$ point ${ \bar { x } } { \in } X$ is efficient if and only if its criterion vector $\bar { z } = ( f _ { 1 } ( \bar { x } ) , f _ { 2 } ( \bar { x } ) . ~ . ~ . , f _ { n } ( \bar { x } ) ) ^ { 2 }$ is non-dominated. The $z ^ { \mathrm { m a x } }$ is the ideal criterion vector where

$$
\begin{array}{c} z ^ {\max} = (z _ {1} ^ {\max}, z _ {2} ^ {\max}, \ldots , z _ {n} ^ {\max}) ^ {T} \\ z _ {i} ^ {\max} = \max f _ {i} (x) \qquad i = 1, 2, \ldots , n \end{array}
$$

$$
\begin{array}{l l} \text { s   .   t   . } & x \in X \end{array}
$$

And the $z ^ { \mathrm { m i n } }$ is the worst criterion vector where

$$
\begin{array}{c} z ^ {\min} = (z _ {1} ^ {\min}, z _ {2} ^ {\min}, \ldots , z _ {n} ^ {\min}) ^ {T} \\ z _ {i} ^ {\min} = \min f _ {i} (x) \qquad i = 1, 2, \ldots , n \end{array}
$$

$$
\begin{array}{l l} \text {s.t.} & x \in X \end{array}
$$

The ‘‘worst’’ vector can be obtained in different ways. One way is to define it as the vector whose elements take the minimum values of the efficient solution set, respectively, known as nadir solution, or it can be given by the DM or domain experts according to the real-world problem. In that case, a ‘‘worst’’ solution could be infeasible. The worst criterion vector is introduced for two reasons. The first one is to make the normalization procedure described below result in a value between 0 and 1; the second reason is to make the comparison procedure of the DM easier.

In this paper, we consider MCDM problems with the assumption that there exists a MAUF that can represent the DM’s preference. We use a DNN [3] for representing MAUFs and enabling the DM to search the most desirable solution. With DNN, it does not assume and need not verify that the utility function is of any particular structure or property. The topology of DNN is shown as Fig. 1.

It consists of three parts: $\mathrm { A N N _ { 1 } }$ , ANN<sub>2</sub> and a comparison node. $\mathrm { A N N _ { 1 } }$ is a feed-forward neural network, and its input is the criterion vector. $\mathrm { A N N } _ { 2 }$ is a duplicate neural network and has the same structure as $\mathrm { A N N } _ { 1 } .$ . The output of DNN is equal to $\mathrm { A N N } _ { 1 } / \mathrm { A N N } _ { 2 }$ . Let $V ( z )$ be the MAUF where $z { = } ( z _ { 1 } ,$ $z _ { 2 } , . . . , z _ { n } )$ is the criterion vector. Then according to Hecht-Nielsen [7], there exists a feed-forward neural network ANN such that $\mathrm { A N N } ( z ) \approx V ( z )$ . If both $\mathrm { A N N _ { 1 } }$ and $\mathrm { A N N } _ { 2 }$ are congruent with ANN, for different criterion vector $z ^ { 1 }$ and $z ^ { 2 } , \mathrm { A N N } ( z ^ { 1 } )$ and $\operatorname { A N N } ( z ^ { 2 } )$ are the preference value of the DM for $z ^ { 1 }$ and $z ^ { 2 } ,$ respectively. The output of $\mathrm { D N N } ( z ^ { 1 } , z ^ { 2 } )$ , which is equal to $\mathrm { \bar { A } N N } ( z ^ { \mathrm { \bar { 1 } } } ) / \mathrm { A N N } ( z ^ { \mathrm { \bar { 2 } } } )$ , is the comparison ‘‘value’’.

![](/api/attachments/TWHSWC7H/fulltext/images/38e59b65479c51b2b2f17c5ecf183477d951181f2fa03060a7b50cdbc491171b.jpg)  
Fig. 1. The topology of DNN.

Therefore, we can use the comparison results as the training samples of DNN.

Proposition 1. DNN can represent any $g ( X , Y )$ , where $g ( X , Y ) = f ( X ) / f ( Y ) ,$ , X, $Y { \in } R ^ { n } , f ( Y ) \neq ~ 0 ,$ , and f is any continuous function.

Proposition 2. Given a $D N N ( X , Y ) = A N N ( X ) / A N N ( Y )$ and a MAUF V(Z), where X, Y, Z<sup>a</sup>R<sup>n</sup>, if for any X, $Y { \in } R ^ { n } , ~ A N N ( X ) { / } A N N ( Y ) = V ( X ) { / } V ( Y )$ , then $A N N ( X ) =$ $k { \cdot } V ( X )$ , k is a constant.

Therefore, the MCDM problem can be expressed as

max $V ( z ) = \mathrm { A N N } ( z )$

$$
\begin{array}{c} \text {s.t.} \quad x \in X \\ z = [ z _ {1}, z _ {2}, \ldots , z _ {n} ] ^ {T} \\ z _ {i} = f _ {i} (x) \qquad i = 1, 2, \ldots , n \end{array}\tag{3}
$$

Solving the optimization problem (3) yields the most desirable solution.

## 3. The interactive DNN approach

The interactive DNN approach consists of four phases: problem identification, modeling, solving MCDM, and implementation, as shown in Fig. 2.

## 3.1. Phase 1: problem identification

In this phase, the problem and its environment are carefully studied. Then the objectives and objective functions are set. The problem is written in a form similar to Eq. (1) or Eq. (2).

## 3.2. Phase 2: modeling

In this phase, we represent the preference of the DM in a formalized way. In other words, a DNN that reflects the DM’s preference is derived in this phase.

## 3.3. Subphase 1: model pre-processing

In order to get the DNN, some pre-processing work should be carried out first. This includes calculating the ideal and worst criterion vector and normalizing criterion vectors. The ideal and worst criterion vector are defined in Section 2, and they can be calculated directly. Based on the ideal and worst criterion vector, we can normalize all the criterion vectors. The transformation method is a linear one.

$$
z _ {i j} ^ {\prime} = \frac {z _ {i j} - z _ {j} ^ {\mathrm{min}}}{z _ {j} ^ {\mathrm{max}} - z _ {j} ^ {\mathrm{min}}}
$$

After normalization, all criterion vectors fall into the interval [0,1].

![](/api/attachments/TWHSWC7H/fulltext/images/e4f48585e2fde813cbdd026fced9d930ad571548b1f5f081eefb1adf6e99ac10.jpg)  
Fig. 2. The interactive DNN approach.

## 3.4. Subphase 2: preference training

In this subphase, some initial solutions are generated firstly. Then the DM is asked to make the pairwise comparison of those solutions. Finally, the DNN is trained.

## 3.4.1. Generating the initial solutions

The initial solutions are generated from Eqs. (1) and (2). In the generating process, the ‘‘quantity’’ and ‘‘quality’’ of the solutions should be noticed. The number of the solutions should be a reasonable one. Too many or too few is unfavorable. The ‘‘quality’’ of the solutions means the proportion of the feasible and efficient solutions. Because the most desirable solution is a feasible and efficient one, most initial solutions should be feasible and efficient. The feasible solutions can be derived from Eqs. (1) and (2). There are many methods developed for searching efficient solutions, such as the augmented weighted Tchebycheff program [18].

Although a large proportion of the initial solutions should be feasible and efficient, the infeasible solutions should not be totally discarded. Some specific infeasible solutions $( \mathrm { e . g . , \bar { z } ^ { m a x } }$ and $z ^ { \mathrm { m i n } } )$ can be easily obtained, and they are favorable for describing the DM’s preference. In the initial solution set, a few infeasible solutions are helpful for the training process. These solutions are usually given directly by the DM.

## 3.4.2. Making comparison

After generating the initial solutions, the DM is asked to make the comparisons of the solutions. Each comparison result is a training sample $( z ^ { i } , z ^ { j } , a _ { i , j } )$ where $z ^ { i }$ and $z ^ { j }$ are two different solutions and $a _ { i , j }$ is the comparison value (the ratio of the preference value of $z ^ { i }$ to the preference value of z <sup>j</sup>). The DM can give some imprecise or interval comparison values, if he/ she is unable to express his/her preference over pairwise comparisons of solutions in a crisp manner.

In some real-world situations, the DM often presents his/her preference by making comparisons between different criteria. In that case, the objective comparison values can be transformed into training samples. For example, the DM thinks ‘‘the weight of criterion 1 is 1/2 of that of criterion 2’’. This can be transformed to a training sample $( x , \ y , \ 0 . 5 )$ , where $x { = } ( 1 , 0 , . . . . , 0 )$ and $y = ( 0 , 1 , 0 , . . . , 0 )$

## 3.4.3. Training the DNN

In this step, the DNN is trained until the error of DNN’s output decreases to an acceptable value. The training algorithm that we used in this paper is based on the back-propagation algorithm [12] as described in Ref. [3].

## 3.5. Phase 3: modification of the model

Now we get a DNN model. However, the current DNN model may not represent the DM’s preference very well. It needs to be verified. In this phase, some solutions are generated to test whether the DNN model is a satisfactory one. If the trained DNN’s results are not consistent with the results given by the DM, then the DNN needs to be modified. We go back to phase 2 with new solutions and re-train the DNN model. We continue this process until the DNN’s results are consistent with the DM’s assessments. This is an interactive procedure.

## 3.6. Phase 4: solving the MCDM problem

When an appropriate DNN is derived from above phases, we will search the most desirable solution by solving the following problem:

$$
\begin{array}{c} \max V (z) = \operatorname{ANN} (z) \\ \text {s.t.} g _ {j} (x) \leq 0 \\ z = (z _ {1}, z _ {2}, \dots , z _ {n}) ^ {T} \\ z _ {i} = f _ {i} (x) \quad i = 1, 2, \dots , n \quad j = 1, 2, \dots , m \end{array}\tag{4}
$$

where ANN is the subfeed-forward neural network in DNN.

This is very similar to a traditional optimization problem, except for the objective function, which is given in a neural network form. To solve Eq. (4), we can apply the penalty function method. The key problem is to determine the partial derivative of ANN, which could be calculated approximately as follows [2]:

$$
\begin{array}{l} \frac {\partial \operatorname{ANN} (x)}{\partial x _ {i}} \\ = \frac {\operatorname{ANN} \left(x _ {1} , \dots , x _ {i} + \varepsilon , \dots , x _ {n}\right) - \operatorname{ANN} \left(x _ {1} , \dots , x _ {i} - \varepsilon , \dots , x _ {n}\right)}{2 \varepsilon} \end{array}
$$

where e is a small positive scalar $( \mathrm { e . g . , } \varepsilon \mathrm { = } 0 . 0 0 1 )$ . Then by applying the traditional nonlinear programming algorithm, we can solve Eq. (4) and get the most desirable solution.

## 4. An example

The example comes from Ref. [20]. We use it to show how the interactive DNN approach works and compare the result with the interactive FFANN procedure [20]. Consider the following multi-objective linear programming problem:

$$
\begin{array}{r c l r c l r c l} \max z _ {1} & = & 2 x _ {2} & + 5 x _ {3} & + 5 x _ {4} & - 2 x _ {5} & + 5 x _ {6} \\ \max z _ {2} & = - x _ {1} & - 2 x _ {2} & & & + 4 x _ {5} & - x _ {6} \\ \max z _ {3} & = 5 x _ {1} & + 3 x _ {2} & - 2 x _ {3} & & - x _ {5} & - x _ {6} \\ \text { subject   to } \end{array}
$$

$$
\begin{array}{c c c c c c c} & & & 7 x _ {4} & + 2 x _ {5} & + 6 x _ {6} & \leq 2 8 \\ 3 x _ {1} & & & & & + 4 x _ {6} & \leq 2 3 \\ 4 x _ {1} & & + 4 x _ {3} & + x _ {4} & & & \leq 2 3 \\ & x _ {2} & + 6 x _ {3} & + 7 x _ {4} & & + 4 x _ {6} & \leq 2 3 \\ 2 x _ {1} & + 5 x _ {2} & + 5 x _ {3} & + 5 x _ {4} & + 8 x _ {5} & & \leq 2 9 \\ x _ {j} \geq 0,   1 \leq j \leq 6 \end{array}
$$

Assume the underlying MAUF of the DM is

$$
V (z) = 5 0 - \left(\sum_ {i = 1} ^ {3} [ \lambda_ {j} (z _ {j} ^ {\max} - z _ {j}) ] ^ {4}\right) ^ {\frac {1}{4}}
$$

where k=(0.319, 0.416, 0.265). The optimal solution is shown in Table 1 [20].

Next we apply the interactive DNN approach to the example. The ideal and worst criteria vectors are

$$
\begin{array}{l} \text { Ideal }: z ^ {\max} = (3 3. 1 0 0, 1 4. 5 0 0, 3 9. 2 5 0), \\ V (z ^ {\max}) = 5 0. 0 0 0 \end{array}
$$

$$
\begin{array}{l} \text { Worst }: z ^ {\min} = (- 7. 2 5 0, - 1 6. 4 1 2, - 9. 2 0 7), \\ V (z ^ {\min}) = 3 3. 0 7 3 \end{array}
$$

respectively. Then the criteria vector and the MAUF are normalized by the following rules.

$$
z _ {i} ^ {\prime} = \frac {z _ {i} - z _ {i} ^ {\mathrm{min}}}{z _ {i} ^ {\mathrm{max}} - z _ {i} ^ {\mathrm{min}}}
$$

$$
V ^ {\prime} (z) = \frac {V (z) - V (z ^ {\mathrm{min}})}{V (z ^ {\mathrm{max}}) - V (z ^ {\mathrm{min}})}
$$

Seven different initial solutions are generated by the augmented weighted Tchebycheff program [18], which are all feasible and efficient ones and the same as those in Ref. [20], shown as Table 2.

In a complex decision environment, the DM is usually unable to express his/her preference over pairs of solutions in a crisp manner, he/she can provide only qualitative preference information due to impreciseness. Suppose that the DM can only give the comparison of alternatives in the interval form. We divide [0,1] into five intervals: [0,0.2], [0.2,0.4], [0.4,0.6], [0.6,0.8], [0.8,1] and the DM gives his/her comparison result by one of the above interval values. Then, 21 interval comparison results are obtained. We take these results as samples to train the DNN (the training algorithm of interval values is described in Ref. [3]) until it converges. We use a point (1, 0, 0) to test the DNN. Compare this point with solution 1 in Table 2. The DNN’s result is not consistent with the DM’s assessment very well. So, the DNN needs to be modified. We add four ‘‘specific point’’ to modify the DNN, as shown in Table 3.

The optimal solution of the example

<table><tr><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td> $X_4$ </td><td> $X_5$ </td><td> $X_6$ </td><td> $Z_1$ </td><td> $Z_2$ </td><td> $Z_3$ </td><td> $V^*$ </td></tr><tr><td>4.558</td><td>0</td><td>0</td><td>1.572</td><td>1.503</td><td>2.331</td><td>16.513</td><td>-0.878</td><td>18.956</td><td>42.423</td></tr></table>

Table 2 Initial solutions

<table><tr><td rowspan="2">Solution</td><td colspan="2">Criteria 1</td><td colspan="2">Criteria 2</td><td colspan="2">Criteria 3</td><td rowspan="2"> $V'(z)$ </td></tr><tr><td> $Z_1$ </td><td> $Z_1'$ </td><td> $Z_2$ </td><td> $Z_2'$ </td><td> $Z_3$ </td><td> $Z_3'$ </td></tr><tr><td>1</td><td>24.3546</td><td>0.78326</td><td>-11.5486</td><td>0.15733</td><td>27.6454</td><td>0.76052</td><td>0.35797</td></tr><tr><td>2</td><td>-5.6932</td><td>0.03858</td><td>14.1886</td><td>0.98993</td><td>-3.9363</td><td>0.10877</td><td>0.16117</td></tr><tr><td>3</td><td>22.8610</td><td>0.74624</td><td>2.2575</td><td>0.60396</td><td>-7.8865</td><td>0.02725</td><td>0.25501</td></tr><tr><td>4</td><td>-4.6175</td><td>0.06524</td><td>7.4575</td><td>0.77218</td><td>14.1959</td><td>0.48296</td><td>0.27308</td></tr><tr><td>5</td><td>29.5694</td><td>0.91250</td><td>-9.2083</td><td>0.23304</td><td>6.8242</td><td>0.33083</td><td>0.34667</td></tr><tr><td>6</td><td>2.3249</td><td>0.23730</td><td>-6.2767</td><td>0.32787</td><td>34.0354</td><td>0.89239</td><td>0.34785</td></tr><tr><td>7</td><td>-3.1758</td><td>0.10097</td><td>1.3395</td><td>0.57426</td><td>27.9001</td><td>0.76577</td><td>0.30770</td></tr></table>

Table 3 Specific points

<table><tr><td>Point</td><td> $Z_{1}'$ </td><td> $Z_{2}'$ </td><td> $Z_{3}'$ </td><td> $V'$ </td></tr><tr><td>A</td><td>1</td><td>0</td><td>0</td><td>0.0969</td></tr><tr><td>B</td><td>0</td><td>1</td><td>0</td><td>0.0965</td></tr><tr><td>C</td><td>0</td><td>0</td><td>1</td><td>0.0959</td></tr><tr><td>D</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

With these ‘‘specific points’’, we get three additional comparison results, $V ^ { \prime } ( A ) / V ^ { \prime } ( D ) , ~ V ^ { \prime } ( B ) / V ^ { \prime } ( D )$ and $V ^ { \prime } ( C ) / V ^ { \prime } ( D )$ , in interval values also. The additional comparison results are used along with the previous results (totally 24 samples) to retrain the DNN. Finally, we get the DNN as Fig. 3.

With the retrained DNN as shown in Fig. 3 as the objective function, the problem finally expresses as follows

max ANNðzVÞ

s:t:

$$
z _ {1} ^ {\prime} = \frac {z _ {i} + 7 . 2 5 0}{3 3 . 1 0 0 + 7 . 2 5 0}
$$

$$
z _ {2} ^ {\prime} = \frac {z _ {2} + 1 6 . 4 1 2}{1 4 . 5 0 0 + 1 6 . 4 1 2}
$$

$$
z _ {3} ^ {\prime} = \frac {z _ {3} + 9 . 2 0 7}{3 9 . 2 5 0 + 9 . 2 0 7}
$$

$$
\begin{array}{r c l r c l r c l} z _ {1} & = & 2 x _ {2} & + 5 x _ {3} & + 5 x _ {4} & - 2 x _ {5} & + 5 x _ {6} \\ z _ {2} & = - x _ {1} & - 2 x _ {2} & & & + 4 x _ {5} & - x _ {6} \\ z _ {3} & = 5 x _ {1} & + 3 x _ {2} & - 2 x _ {3} & & - x _ {5} & - x _ {6} \end{array}
$$

$$
\begin{array}{c c c c c c c} & & & 7 x _ {4} & + 2 x _ {5} & + 6 x _ {6} & \leq 2 8 \\ 3 x _ {1} & & & & & + 4 x _ {6} & \leq 2 3 \\ 4 x _ {1} & & + 4 x _ {3} & + x _ {4} & & & \leq 2 3 \\ & x _ {2} & + 6 x _ {3} & + 7 x _ {4} & & + 4 x _ {6} & \leq 2 3 \\ 2 x _ {1} & + 5 x _ {2} & + 5 x _ {3} & + 5 x _ {4} & + 8 x _ {5} & & \leq 2 9 \end{array}
$$

$$
x _ {j} \geq 0, 1 \leq j \leq 6
$$

Solving the above optimization problem, the final solution is found as shown in Table 4, which is an efficient one.

Compare the result with the interactive FFANN procedure [20]. In the interactive FFANN procedure, the same initial solutions as shown in Table 2 are generated first. The optimal solution calculated after the first iteration is

Z ¼ ð19:163; -4:444; 24:185Þ

$$
V (z) = 4 1. 8 0 9
$$

Through an interactive process with the DM, six new solutions are generated for the second iteration. The final solution was obtained in iteration 3 [20]

Z ¼ ð18:966; -2:529; 20:367Þ

$$
V (z) = 4 2. 2 7 6
$$

We can also apply the DNN approach to the case that the precise comparisons of alternatives are available. And the final solution is:

Z ¼ ð19:058; -1:480; 17:416Þ

VðzÞ ¼ 42:321

Table 5 summarizes the comparison between DNN approach and FFANN approach.

From Table 5, we can see that the DNN method takes fewer comparisons and generates a sufficient number of training samples compared with the FFANN method. When the comparison results are given in precise values, DNN’s result is slightly better than the FFANN’s (we think the difference is not significant, considering with the theoretical optimal objective function value); when the comparison results are given in interval forms, the DNN can also find a satisfactory solution. Furthermore, when the scale of the problem grows, in other words, when the number of criteria increases, the number of training samples are required to increase too. And the FFANN approach needs to take much more comparisons. For example, if the number of criteria is 10, and we need 20 training samples, FFANN requires (20  19)/ 2 = 190 comparisons. It is very difficult to persuade the DM to provide so many comparisons consistently. For the interactive DNN approach, the number of training samples is the same as the number of the comparison results, and the results can be given in fuzzy or interval values. The DNN approach is more competitive in the large scale, real-world MCDM problems.

![](/api/attachments/TWHSWC7H/fulltext/images/54309dc4b86ee0644442a42ea2e0a460b5d2f80c263644d0bb8ba211333588b9.jpg)  
Fig. 3. ANN (DNN) after re-training.

Table 4  
The final solution of the example

<table><tr><td> $X_{1}$ </td><td> $X_{2}$ </td><td> $X_{3}$ </td><td> $X_{4}$ </td><td> $X_{5}$ </td><td> $X_{6}$ </td><td> $Z_{1}$ </td><td> $Z_{2}$ </td><td> $Z_{3}$ </td><td>V</td></tr><tr><td>5.103</td><td>0.009</td><td>0.128</td><td>2.076</td><td>0.966</td><td>1.923</td><td>18.719</td><td>-3.178</td><td>22.395</td><td>42.166</td></tr></table>

Table 5  
Comparison between the two approaches

<table><tr><td></td><td>FFANN</td><td>DNN</td><td>DNN</td><td>The optimal solution</td></tr><tr><td>Comparison matrix</td><td>Precise</td><td>Precise</td><td>Interval value</td><td></td></tr><tr><td>Number of comparisons</td><td>51</td><td>21</td><td>24</td><td></td></tr><tr><td>Number of samples</td><td>19</td><td>21</td><td>24</td><td></td></tr><tr><td>Final solution  $V(z)$ </td><td>42.276</td><td>42.321</td><td>42.166</td><td>42.423</td></tr><tr><td> $Z_1$ </td><td>18.966</td><td>19.058</td><td>18.719</td><td>16.517</td></tr><tr><td> $Z_2$ </td><td>-2.529</td><td>-1.480</td><td>-3.178</td><td>-0.886</td></tr><tr><td> $Z_3$ </td><td>20.367</td><td>17.416</td><td>22.395</td><td>18.970</td></tr></table>

In the interactive FFANN procedure, five iterations are conducted, that is, the total number of pairwise comparisons and the number of samples are 81 and 31, respectively. However, the most desirable solution is obtained in iteration 3. In that case, there are 51 pairwise comparisons are required and 19 samples are used.

## 5. Conclusion

Based on the DNN model, a new interactive approach based on DNN is presented in this paper. A DNN is used in this approach because of the ability of a neural network to describe complicated mappings, so that it does not assume any particular structure or property of the DM’s utility function during the problem solving process. The main phases of the approach are discussed in details as well. Because of the unique structure of the DNN, the approach has many advantages comparing with traditional neural networks-based approaches. Furthermore, fuzzy or interval comparison values can be directly applied, which provide the DM certain flexibility to represent his partial information about his preferences.

An example is also presented for illustrating the approach. From the example, we see that with a few comparisons, the DNN approach can easily find a satisfactory solution. Further analysis shows that when the MCDM problem is a large scale one, the approach presented in this paper is much better than the FFANN procedure, that is, the DNN approach is an efficient and robust method for solving MCDM problems.

Much work still remains to be done in the future to make the DNN approach more effective, especially exploring an effective learning algorithm for DNN and developing a DSS based on the framework proposed in this paper.

## Acknowledgements

We extend thanks to the editor and two anonymous reviewers for their valuable comments and suggestions that helped improve the presentation of this paper. This work is supported partly by the National Science Foundation of China (Grant No. 69674037, 70071015 and 79825102) and the Fund for PhD Disciplines (Grant No. 9500365).

## References

[1] R. Benayoun, J. de Montgolfier, J. Teargny, et al., Linear programming with multiple objective functions: step method (STAM), Mathematical Programming 14 (1) (1971).

[2] R.L. Burden, J.D. Faires, Numerical analysis, Prindle, 4th ed., Weber & Schmidt, Boston, MA, 1989.

[3] J. Chen, S. Lin, A neural network approach—decision neural network (DNN) for preference assessment, Working paper, Tsinghua University (1999).

[4] L.R. Gardiner, R.E. Steuer, Unified interactive multiple objective programming, European Journal of Operational Research 74 (5) (1994).

[5] M. Geoffrion, J.S. Dyer, A. Feinberg, An interactive approach for multi-criterion optimization, with an application to the operation of an academic department, Management Science 19 (4) (1972).

[6] R.P. Ha¨ma¨la¨inen, H. Lauri, HIPRE 3+ User’s Guide, Systems Analysis Laboratory, Helsinki University of Technology, 1995.

[7] R. Hecht-Nielsen, Theory of the backpropagation neural networks, Proceedings of the International Joint Conference on Neural Networks, 1989.

[8] B. Malakooti, A decision support system for discrete multicriteria problems: under certainty, uncertainty, and hierarchical, Applied Mathematics and Computation 54 (2 and 3) (1993).

[9] B. Malakooti, S. Subramanian, Multiple criteria approach for integrated matching supervision, machinability, and tool performance with polynomial utility functions, Engineering Valuation and Cost Analysis 2 (6) (2000).

[10] B. Malakooti, Y. Zhou, Feed-forward artificial neural networks for solving discrete multiple criteria decision making problems, Management Science 40 (11) (1994).

[11] B. Malakooti, Y. Zhou, Approximating polynomial functions by feedforward artificial neural networks: capacity, analysis, and design, Applied Mathematics and Computation 90 (1) (1998).

[12] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning internal representations by error propagation, in: D.E. Rumelhart, J.L. McClelland (Eds.), Parallel Distributed Processing: Explorations in the Microstructures of Cognition, Foundations, vol. I, MIT Press, Cambridge, MA, USA, 1986, pp. 318 – 362.

[13] T.L. Saaty, Multicriteria Decision Making: The Analytic Hierarchy Process, RWS Publications, Pittsburgh, PA, 1990.

[14] A.A. Salo, R.P. Ha¨ma¨la¨inen, Interactive decision support through interval judgments, Proc. of the 2nd International Symposium on the Analytic Hierarchy Process, Pittsburgh, USA, August 1991

[15] A.A. Salo, R.P. Ha¨ma¨la¨inen, Preference programming through approximate ratio comparisons, European Journal of Operational Research 82 (3) (1995).

[16] Y. Siskos, A. Spyridakos, Intelligent multi-criteria decision support: overview and perspective, European Journal of Operational Research 113 (2) (1999).

[17] A. Stam, M. Sun, M. Haines, Artificial neural network representations for pairwise preference structures, Computers & Operations Research 23 (12) (1996).

[18] R.E. Steuer, E.U. Choo, An interactive weighted tchebycheff procedure for multiple objective programming, Mathematical Programming 26 (3) (1983).

[19] T.J. Stewart, A critical survey on the status of multiple criteria decision making theory and practice, Omega 20 (5 and 6) (1992).

[20] A. Sun, A. Stam, R.E. Steuer, Solving multiple objective programming problems using feed-forward artificial neural networks: the interactive FFANN procedure, Management Science 42 (6) 1996, pp. 835– 849.

[21] M. Sun, A. Stam, R. Steuer, Interactive multiple objective programming problems using Tchebycheff programs and artificial neural networks, Computers & Operations Research 27 (7 and 8) (2000) 601 – 620.

[22] J. Wang, B. Malakooti, A feedforward neural network for multiple criteria decision making, Computers & Operations Research 19 (2) (1992).

[23] A.P. Wierzbicki, A mathematical basis for satisficing decision making, Mathematical Modeling 3 (5) (1982).

![](/api/attachments/TWHSWC7H/fulltext/images/2ce5e1df5e22b002ca3bdab516479e57d5f35176ab16bf8ecc53d9ccf4d05b1b.jpg)

Jian Chen is a Professor and Chairman of Management Science Department, Tsinghua University. He received his BS degree in Electrical Engineering from Tsinghua University in 1983, the MS degree, and the PhD degree both in Systems Engineering from the same University in 1986 and 1989, respectively. He is a senior member of IEEE and a member of INFORMS. He served as a member of the Administrative Committee of IEEE Systems, Man and

Cybernetics Society (1998 – 2000), and serves a member of the Standing Committee of Systems Engineering Society of China (1998 – present), a member of the Standing Committee of China Information Industry Association (1998 – present) and a member of the Standing Committee of Decision Science Society of China (2000 – present). He is the recipient of Outstanding Contribution Award of IEEE Systems, Man and Cybernetics Society, 1996; and Young Scientist Award of China, 1992. He has over 100 technical publications and has been a principal investigator for over 20 grants or research contracts with National Science Foundation of China, governmental organizations and companies. He is on the Editorial Advisory Board of ‘‘The International Journal of Electronic Business’’, and on the Editorial Board of ‘‘Systems Research and Behavioral Science’’. His main research interests include supply chain management, decision support systems and information systems. He is the secretary general of the 1996 IEEE International Conference on Systems, Man and Cybernetics, Chair of the 1st Asian eBiz Workshop, and a member of the IPC of over 20 international conferences.

![](/api/attachments/TWHSWC7H/fulltext/images/62764e76f6d48b5cfc66674375dd857f165297f439af7a7dfdf6e0f2ed4aa84a.jpg)  
Song Lin was born in 1975. He got his BS degree from Tsinghua University in 1997, and the MS in the same university in 1999. He is now a PhD candidate at University of Virginia. His research interests include data mining techniques and its applications. He has a couple of papers on outlier detection and association published in international conferences.
