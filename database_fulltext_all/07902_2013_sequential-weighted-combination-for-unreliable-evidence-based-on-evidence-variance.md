---
otero_id: 7902
otero_key: "AKB588FC"
title: "Sequential weighted combination for unreliable evidence based on evidence variance"
authors: "Deqiang Han; Yong Deng; Chongzhao Han"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Sequential weighted combination for unreliable evidence based on evidence variance

Deqiang Han <sup>a,</sup>⁎, Yong Deng <sup>b</sup>, Chongzhao Han

<sup>a</sup> MOE KLINNS Lab, Institute of Integrated Automation, Xi'an Jiaotong University, Xi'an 710049, China

<sup>b</sup> School of Electronics and Information Technology, Shanghai Jiaotong University, Shanghai 200240, China

## a r t i c l e i n f o

Article history: Received 18 July 2010 Received in revised form 5 February 2013 Accepted 9 May 2013 Available online 18 May 2013

Keywords: Evidence theory Bodies of evidence Evidence combination variance

## a b s t r a c t

Dempster–Shafer evidence theory is a powerful tool in uncertainty reasoning and decision-making. However counter-intuitive results can be encountered when unreliable bodies of evidence are combined by using Dempster's rule of combination in some cases. In this paper, a novel sequential evidence combination approach is proposed based on the weighted modi<sup>fi</sup>cation of bodies of evidence according to our proposed variances of evidence sequences. Experimental results show that the proposed approach is rational and effective. © 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In Dempster–Shafer evidence theory [12], multiple independent and reliable or equal-reliable bodies of evidence (BOE) can be combined by using Dempster's rule of combination. However in some cases of unreliable or unequal-reliable evidence combination, especially when the bodies of evidence to be combined are highly con<sup>fl</sup>icting, counter-intuitive results may be obtained based on Dempster's rule of combination. Here the “counter-intuitive results” mean that people believe that information fusion (or aggregation) can produce better forecasting results which are closer to human beings' intuition or expectation, but they do not produce such results.

For the reasons of counter-intuitive results encountered in evidence combination based on Dempster's rule, there exist disputes on the reasons. Some researchers think that counter-intuitive results are caused by Dempster' rule, so they modi<sup>fi</sup>ed Dempster's rule to suppress the counter-intuitive results [7,13,14,16,17]; some researchers think that the counter-intuitive results are caused by the evidence theory's inconsistency [2,11,15]; and other researchers think that counter-intuitive results should be imputed to the sensors or information sources. That is to say they think that Dempster's rule is designed for the combination of reliable or equal-reliable sources of evidence. Thus the rule itself should not be modi<sup>fi</sup>ed and the BOEs to be combined should be modi<sup>fi</sup>ed or preprocessed [1,9,10].

We think that Dempster's rule of combination should not be modi<sup>fi</sup>ed and the counter-intuitive behaviors in some cases should be imputed to the unreliability of BOEs, i.e., the sensors or the information sources where the data or the evidences come from. Dempster's rule has the assumption that the BOEs to be combined are all reliable or equal-reliable. However, in many real applications, some evidence sources are always unreliable. If all the BOEs are treated as reliable, the unreliable ones may bring a very bad in<sup>fl</sup>uence on combination result, and even leads to inconsistent results and wrong decisions. Thus the BOEs should be preprocessed according to their corresponding reliabilities before evidence combination, i.e., to take into account the reliability of each source in combination process to provide a more accurate result. As argued by Haenni [5], modifying data (i.e. BOEs) is more reasonable no matter whether from the viewpoint of engineering practice, mathematics or philosophical logic.

Some methods based on modi<sup>fi</sup>cations or preprocess of original evidences have been proposed [1,9,10]. Murphy proposed a combination approach based on arithmetic average of BOEs [10]. In Deng's work [1], he implemented evidence combination based on weighted average of BOEs by using Jousselme's distance of evidence [6]. Deng's method has better performance of convergence than Murphy's simple averaging method. Convergence speed represents the speed of increase for the mass assignment value of intuitively correct proposition. At each step, the mass assignment values of true proposition obtained by using some approach is more approximate to 1, the corresponding approach's convergence speed is faster.

In traditional approach to modifying evidence such as the Murphy's work [10] and our previous work, i.e., Deng's work [1], all the BOEs should be gathered and processed as a batch. But in some practical applications, the BOEs come sequentially. In this paper, a novel sequential weighted evidence combination approach is proposed based on our proposed variance of BOEs which is de<sup>fi</sup>ned based on the Jousselme's distance of evidence. The variance of BOEs can describe the <sup>fl</sup>uctuation degree of a given BOE sequence, which can represent the reliability of the given information source to some degree, so we use variance to generate reliability as weights. For the sequential evidence combination, each combination step can be seen as the fusion of the combination result in precedent step and the new arriving BOE in current step. In our proposed approach, the combination result in precedent step and the new arriving BOE in current step are weighted averaged and then combined by using Dempster's rule of combination, where the weights are generated by using our proposed variance of evidence sequence. The variance of all original BOEs acquired till the current step (including current step) are calculated to represent the reliability or quality of the new arriving BOE in the current step (i.e. new arriving information) while the variance of all the combination results in previous steps are calculated to represent the reliability or quality of the precedent combination result (i.e. available information). The larger the variance is, the less the reliability. Our proposed approach is in fact a sequential weighted combination based Dempster's rule, where weights are generated by using the variances of BOEs. Experimental results show that the proposed approach is rational and effective.

## 2. Counter-intuitive behaviors of unreliable evidence combination

## 2.1. Basics of evidence theory

In evidence theory [12], the elements in frame of discernment (FOD) Θ are mutually exclusive and exhaustive. De<sup>fi</sup>ne m : $2 ^ { \Theta }  [ 0 , 1 ]$ ] as basic probability assignment (BPA, also called mass function) satisfying:

$$
\sum \{m (A) | A \subseteq \theta \} = 1, m (\emptyset) = 0\tag{1}
$$

If $m ( A ) > 0 , A$ is called a focal element.

A BOE can be represented by focal elements and their corresponding mass assignment values. When multiple reliable independent BOEs are available, the combined BOE can be derived based on Dempster's rule of combination as follows:

$$
\left\{ \begin{array}{c} m (A) = \frac {1}{1 - K} \sum_ {\cap A _ {i} = A} \prod_ {1 \leq i \leq n} m _ {i} (A _ {i}), A \neq \emptyset \\ m (\emptyset) = 0, A = \emptyset \end{array} \right.\tag{2}
$$

where $K = \sum _ { \cap A _ { i } = \emptyset } \prod _ { 1 \leq i \leq n } m _ { i } ( A _ { i } )$ representing the total con<sup>fl</sup>icting or contra-<sup>¼</sup>dictory mass assignments. Dempster's rule is both commutative and associative. For Dempster's rule of combination, the con<sup>fl</sup>icting mass assignments are discarded.

In practical applications of evidence combination, there always exist con<sup>fl</sup>icts among the different BOEs to be combined. As referred above, the con<sup>fl</sup>icting mass assignments are discarded and the concordant propositions are reinforced in Dempster's rule of combination. However, for unreliable or unequal-reliable evidence combination, some counter-intuitive behaviors might be encountered by using Dempster's rule, which are illustrated below.

## 2.2. Counter-intuitive behavior I

Zadeh's Example [18]: Two doctors examine a patient and agree that he suffers from either meningitis $( M ) .$ contusion (C) or brain tumor (T). Thus the FOD is $\boldsymbol { \Theta } = \{ \boldsymbol { M } , \boldsymbol { C } , \boldsymbol { T } \}$ . Assume that the doctors agree in their low expectation of a tumor, but disagree in likely cause and provide the following diagnosis: $m _ { 1 } ( \{ M \} ) = 0 . 9 9 , m _ { 1 } ( \{ T \} ) = 0 . 0 1 ; m _ { 2 } ( \{ C \} ) =$ 0.99, $m _ { 2 } ( \{ T \} ) = 0 . 0 1$ . Based on Dempster's rule of combination, unexpected <sup>fi</sup>nal conclusion is derived: $m ( \{ T \} ) = 1$

This represents that the patient suffers from brain tumor absolutely. Obviously, this is counter-intuitive. It arises from the fact that the two BOEs (doctors) agree that the patient most likely does not suffer from tumor but are in almost full contradiction for the other causes of the disease. Such a result obviously is not in accordance with human being's expectation or intuition, so it is counter-intuitive. Such a counter-intuitive result is due to the high con<sup>fl</sup>ict between the two BOEs. The unreliability of some BOEs might be one of the important reasons for the con<sup>fl</sup>ict. So the counter-intuitive result cannot be imputed to Dempster's rule.

## 2.3. Counter-intuitive behavior II

The FOD is $\boldsymbol { \Theta } = \{ \boldsymbol { \theta } _ { 1 } , \boldsymbol { \theta } _ { 2 } , \boldsymbol { \theta } _ { 3 } \}$ . Consider that a principal resorts to l experts to obtain a good prediction. Different experts have different reliability. The corresponding unequal-reliable BOEs to be combined are as follows:

$$
\left\{ \begin{array}{l} m _ {i} ^ {n e w} (\{\theta_ {1} \}) = a \\ m _ {i} ^ {n e w} (\Theta) = 1 - a \end{array} \right.
$$

where $i = 1 , . . . , l .$ Combination result based on Dempster's rule is as follows.

$$
\left\{ \begin{array}{c} m _ {l} ^ {\text { comb }} (\{\theta_ {1} \}) = 1 - (1 - a) ^ {l} \\ m _ {l} ^ {\text { comb }} (\Theta) = (1 - a) ^ {l} \end{array} \right.
$$

We always hope that by aggregating the private information of a large population, the principal can generate fairly accurate predictions of future events. We tend to believe “The wisdom of crowds,” implies that aggregating dispersed information can produce accurate predictions. But the example shows a surprising result. If $a = 0 . 0 6$ and the number of BOEs is 50 (i.e., there are totally 50 experts), there exists $m ( \{ \theta _ { 1 } \} ) = 1 - ( 0 . 9 4 ) ^ { 5 0 } = 0 . 9 5 4 7$ which is very large, although for each BOE to be combined $m _ { i } ( \{ \theta _ { 1 } \} ) = 0 . 0 6$ which is very small. Each expert thinks $\theta _ { 1 }$ occurs with probability 0.06, but the principal thinks $\theta _ { 1 }$ occurs with probability 0.9547 if one combines diverse information by Dempster's rule of combination. We think it is a counter-intuitive example in this sense. It should be noted that although in this example, all BPAs are equal, there also exist con<sup>fl</sup>ict, which is called self-con<sup>fl</sup>ict or auto-con<sup>fl</sup>ict [9] between BOEs.

## 2.4. Counter-intuitive behavior III

The FOD is $\begin{array} { r } { \Theta = \{ \theta _ { 1 } , \theta _ { 2 } , \theta _ { 3 } \} . } \end{array}$ l pieces of unreliable or unequal-reliable BOEs to be combined are as follows [3]:

$$
\left\{ \begin{array}{c} m _ {1} (\{\theta_ {1} \}) = a \\ m _ {1} (\{\theta_ {1}, \theta_ {2} \}) = 1 - a \\ m _ {1} (\{\theta_ {3} \}) = 0 \\ m _ {1} (\{\Theta \}) = 0 \end{array} \right.
$$

$$
\left\{ \begin{array}{c} m _ {i} ^ {n e w} (\{\theta_ {1} \}) = 0 \\ m _ {i} ^ {n e w} (\{\theta_ {1}, \theta_ {2} \}) = b _ {1} \\ m _ {i} ^ {n e w} (\{\theta_ {3} \}) = 1 - b _ {1} - b _ {2} \\ m _ {i} ^ {n e w} (\Theta) = b _ {2} \end{array} \right.
$$

where $i = 2 , . . . l .$ When applying Dempster's rule of combination, one gets:

$$
\left\{ \begin{array}{c} m ^ {c o m b} (\{\theta_ {1} \}) = a = m _ {1} (\{\theta_ {1} \}) \\ m ^ {c o m b} (\{\theta_ {1}, \theta_ {2} \}) = 1 - a = m _ {1} (\{\theta_ {1}, \theta_ {2} \}) \end{array} \right.
$$

It is easy to verify that the combination results are always the same as $m _ { 1 }$ with new $m _ { i } ^ { n e w }$ added in. The value of con<sup>fl</sup>ict $K _ { 1 i } = 1 - b _ { 1 } - b _ { 2 } .$ We believe that information aggregation can produce a better forecasting result. In this example aggregating unreliable information using Dempster's rule cannot produce a reasonable result. It seems that the opinion of $m _ { 1 } \prime _ { S }$ expert dominates other experts' opinions. This is counter-intuitive because it does not accord with people's expectation or intuition. It should be noted that in this example, none of the sources are vacuous and there does exist a non-null con<sup>fl</sup>ict between them.

As we can see in the above examples, Dempster's rule of combination does bring out counter-intuitive behaviors, but we do not think Dempster's rule should be modi<sup>fi</sup>ed. Dempster's rule has its assumptions that all the BOEs to be combined are reliable or equal-reliable. We think that the counter-intuitive results should be imputed to the reliability of the information sources. As pointed by Haenni [5], no matter whether from the practical viewpoint, philosophical viewpoint or the mathematical view point, Dempster's rule should not be modi<sup>fi</sup>ed. To suppress the counter-intuitive behaviors, the BOEs to be combined should be modi<sup>fi</sup>ed or preprocessed. So here we attempt to propose a novel evidence combination approach for unreliable evidence combination by modifying BOEs as illustrated in the next section.

## 3. A novel sequential weighed evidence combination based on the variance of BOEs

In Murphy's approach, Deng's approach and other approaches to modifying the BOEs, all the BOEs to be combined are required to be available and be processed together to suppress the counterintuitive behaviors. In some practical applications, the BOEs are acquired sequentially, so we aim to propose a sequential weighted evidence combination approach for unreliable BOEs by using variances of BOE sequences. We attempt to de<sup>fi</sup>ne variance of distance based on distance of evidence. In Jousselme's work, a distance of evidence is de<sup>fi</sup>ned as follows:

$$
d _ {J} \left(m _ {i}, m _ {j}\right) = \sqrt {\frac {1}{2} \left(m _ {i} - m _ {j}\right) \mathbf {D} \left(m _ {i} - m _ {j}\right)}\tag{3}
$$

In Eq. (3), m and m are two BPAs de<sup>fi</sup>ned over the FOD Θ. The cardinality of Θ is n. D is a $2 ^ { n } \times 2 ^ { n }$ matrix. The element D in D is de<sup>fi</sup>ned as:

$$
D (A, B) = \frac {| A \cap B |}{| A \cup B |}\tag{4}
$$

where |A| represents the cardinality of A. The less the distance between two BOEs is, the more similarity between the two BOEs is.

If we can de<sup>fi</sup>ne the variance of BOEs, it can be used to describe the <sup>fl</sup>uctuation degree of a given BOE sequence, which can represent the reliability of the given information source to some degree. Based on the distance of evidence de<sup>fi</sup>ned in Eq. (3), we de<sup>fi</sup>ne the variance of BOEs in Eq. (5):

$$
\operatorname{Var} \left(m _ {1}, \dots , m _ {k}\right) = \sqrt {\frac {1}{k} \sum_ {i = 1} ^ {k} d _ {J} ^ {2} \left(m _ {i} , \overline {{m}}\right)}\tag{5}
$$

where $\overline { { m } } = { \scriptstyle { \frac { 1 } { k } } } \sum _ { i = 1 } ^ { k } m _ { i }$ and k represents the number of the BOEs in se-<sup>¼</sup>quence. Some other de<sup>fi</sup>nitions of variance of evidence can be found in [4] and [9].

For our proposed sequential evidence combination, there exists a sequence of the sequentially arrived original BOEs and a sequence of the combined BOEs in previous steps. Each combination step can be seen as the weighted fusion of the combination result in precedent step and the new arriving BOE in current step. The weights are generated sequentially and dynamically by using the variances of the two sequences of BOEs referred above. The variance of all the original BOEs acquired till current step (including current step) are calculated to represent the reliability or quality of the new arriving BOE in current step while the variance of all the combined BOEs in previous steps are calculated to represent the reliability or quality of the precedent combined BOE. The whole procedure is as follows:

Suppose that $m _ { i } ^ { n e w } , i = 1 , . . . ,$ n represents the new arriving BOE in step i and $m _ { i } ^ { c o m b } , i = 1 , . . . , n$ n represents the combined BOE in previous step $i - 1$ . All the $m _ { j } ^ { n e w } , j = 1 , \ldots$ , i constitute the arrived original BOE sequence at and before step i while all the $m _ { j } ^ { c o m b } , j = 1 , . . . , i$ constitute the combined BOE sequence before step i.

1). Step 1 and Step2: For the <sup>fi</sup>rst BOE $m _ { 1 } ^ { n e w }$ and the second BOE $m _ { 2 } ^ { n e w } ,$ Let $\overset { \overline { { \mathbf { \Lambda } } } } { m _ { 1 } ^ { c o m b } } = \overset { \overline { { \mathbf { \Lambda } } } } { m _ { 1 } ^ { n e w } }$ . The weighted averaging BOE at step 2 is $m _ { 2 } ^ { w } =$ $0 . 5 \cdot m _ { 1 } ^ { n e w } + 0 . 5 \cdot m _ { 2 } ^ { n e w }$ . The combined BOE in step 2 is $m _ { 2 } ^ { c o m b } =$ m<sub>2</sub><sup>w</sup> ⊕ m<sub>2</sub><sup>w</sup>.

2). After Step 2: For $i = 3 : k$

Do the following steps (a–e) repeatedly:

a) Calculate the variance of the sequence of combined BOEs in previous steps: $S ^ { c o m b } = [ m _ { 1 } ^ { c o m b } , . . . , \stackrel { \cdot } { m _ { i } ^ { c o m b } - 1 } ] ~ ( \mathrm { i . e . } ~ S ^ { c o m b }$ is constituted by all the combined BOEs before current step i) as follows:

$$
\overline {{{m}}} _ {i} ^ {\text { comb }} = \frac {1}{i - 1} \sum_ {j = 1} ^ {i - 1} m _ {j} ^ {\text { comb }}\tag{6}
$$

$$
\operatorname{Var} _ {i} ^ {\text { comb }} = \sqrt {\frac {1}{i - 1} \sum_ {j = 1} ^ {i - 1} d _ {J} ^ {2} \left(m _ {j} ^ {\text { comb }} , \overline {{m}} _ {i} ^ {\text { comb }}\right)}\tag{7}
$$

b) Calculate the variance of the sequence of arrived original BOEs: $S ^ { n e w } = [ m _ { 1 } ^ { n e w } , . . . , m _ { i } ^ { n e w } ] ( \mathrm { i } . \mathrm { e } . S ^ { n e w }$ is constituted by all the arrived BOEs before and at step i) as follows:

$$
\overline {{m}} _ {i} ^ {\text {new}} = \frac {1}{i} \sum_ {j = 1} ^ {i} m _ {j} ^ {\text {new}}\tag{8}
$$

$$
V a r _ {i} ^ {\text { new }} = \sqrt {\frac {1}{i} \sum_ {j = 1} ^ {i} d _ {J} ^ {2} \left(m _ {j} ^ {\text { new }} , \overline {{m}} _ {i} ^ {\text { new }}\right)}\tag{9}
$$

c) Generate the weights for new arriving BOE at current step i and for the combined BOE at the precedent step i-1 as follows:

$$
\left\{ \begin{array}{l} w _ {i} ^ {\text { new }} = \exp \bigl (- \alpha \cdot V a r _ {i} ^ {\text { new }} \bigr) \\ w _ {i} ^ {\text { comb }} = \exp \Bigl (- \alpha \cdot V a r _ {i} ^ {\text { comb }} \Bigr) \end{array} \right.\tag{10}
$$

The larger the variance is, the smaller the reliability or quality and vice versa. So negative exponential function is used in Eq. (10), where α is the parameter of the negative exponential function. The value of α does affect the performance of the proposed approach. If we want to strengthen the effect of the discounting or weighting in our approach, the value of α should be large. Otherwise, the value of α should be small. Based on our many experiments, $\alpha = 1 0$ is suggested.

d) Calculate the weighted averaging BOE at current step i:

$$
m _ {i} ^ {w} = \frac {w _ {i} ^ {\text { new }}}{w _ {i} ^ {\text { new }} + w _ {i} ^ {\text { comb }}} \cdot m _ {i} ^ {\text { new }} + \frac {w _ {i} ^ {\text { comb }}}{w _ {i} ^ {\text { new }} + w _ {i} ^ {\text { comb }}} \cdot m _ {i - 1} ^ {\text { comb }}\tag{11}
$$

e) Execute evidence combination based on Dempster's rule (⊕ represents the evidence combination by using Dempster's rule):

$$
m _ {i} ^ {\text { comb }} = m _ {i} ^ {w} \oplus m _ {i} ^ {w}\tag{12}
$$

3.1. End of for loop

The whole procedure can be illustrated in Fig. 1 below. In Fig. 1, $S ^ { c o m b }$ and $S ^ { n e w }$ represent the sequences of combined results and the new arriving BOEs, respectively.

![](/api/attachments/AKB588FC/fulltext/images/c9d1bd2cce9a4e9297d3db573aa6e3cc51ca81cca24010d4a46286904d299453.jpg)  
Fig. 1. The procedure of the sequential weighted evidence combination.

As illustrated in Fig. 1, if we regard the combination result in the precedent step as the forecasting of the current step and regard the new arriving BOE as the new measurement, the idea of our proposed sequential weighted evidence combination is a weighted fusion of the information provided by one-step forecasting (derived based on the information provided by previous steps) and the information provided by the new measurement.

## 4. Experiments

## 4.1. Example 1

A <sup>fi</sup>ctitious example is provided to illustrate the use of the proposed sequential weighted evidence combination approach and to show the rationality of the proposed approach according to counter-intuitive behavior I as illustrated in Section 2.2. In a multisensor-based automatic target recognition system, the FOD is $\boldsymbol { \Theta } = \{ \boldsymbol { \theta } _ { 1 } , \boldsymbol { \theta } _ { 2 } , \boldsymbol { \theta } _ { 3 } \}$ . Suppose the real target is θ . From different sensors, they acquire <sup>fi</sup>ve BOEs sequentially. The unreliable BOEs are listed as follows:

Comparison of combination results for Example 1.

<table><tr><td rowspan="2">BOEs</td><td colspan="4">Approach</td></tr><tr><td>Dempster&#x27;s rule</td><td>Murphy&#x27;s simple average</td><td>Deng&#x27;s weighted average</td><td>This paper</td></tr><tr><td rowspan="4"> $m_1, m_2$ </td><td> $m(\{\theta_1\}) = 0.7723$ </td><td> $m(\{\theta_1\}) = 0.7716$ </td><td> $m(\{\theta_1\}) = 0.7716$ </td><td> $m(\{\theta_1\}) = 0.7716$ </td></tr><tr><td> $m(\{\theta_2\}) = 0.0792$ </td><td> $m(\{\theta_2\}) = 0.0790$ </td><td> $m(\{\theta_2\}) = 0.0790$ </td><td> $m(\{\theta_2\}) = 0.0790$ </td></tr><tr><td> $m(\{\theta_3\}) = 0.1485$ </td><td> $m(\{\theta_3\}) = 0.1049$ </td><td> $m(\{\theta_3\}) = 0.1049$ </td><td> $m(\{\theta_3\}) = 0.1049$ </td></tr><tr><td></td><td> $m(\{\theta_2, \theta_3\}) = 0.0444$ </td><td> $m(\{\theta_2, \theta_3\}) = 0.0444$ </td><td> $m(\{\theta_2, \theta_3\}) = 0.0444$ </td></tr><tr><td rowspan="4"> $m_1, m_2, m_3$ </td><td> $m(\{\theta_1\}) = 0.0000$ </td><td> $m(\{\theta_1\}) = 0.3526$ </td><td> $m(\{\theta_1\}) = 0.6013$ </td><td> $m(\{\theta_1\}) = 0.5591$ </td></tr><tr><td> $m(\{\theta_2\}) = 0.8421$ </td><td> $m(\{\theta_2\}) = 0.5978$ </td><td> $m(\{\theta_2\}) = 0.3302$ </td><td> $m(\{\theta_2\}) = 0.4021$ </td></tr><tr><td> $m(\{\theta_3\}) = 0.1579$ </td><td> $m(\{\theta_3\}) = 0.0380$ </td><td> $m(\{\theta_3\}) = 0.0532$ </td><td> $m(\{\theta_3\}) = 0.0297$ </td></tr><tr><td></td><td> $m(\{\theta_2, \theta_3\}) = 0.0116$ </td><td> $m(\{\theta_2, \theta_3\}) = 0.0153$ </td><td> $m(\{\theta_2, \theta_3\}) = 0.0091$ </td></tr><tr><td rowspan="4"> $m_1, m_2, m_3, m_4$ </td><td> $m(\{\theta_1\}) = 0.0000$ </td><td> $m(\{\theta_1\}) = 0.5167$ </td><td> $m(\{\theta_1\}) = 0.7987$ </td><td> $m(\{\theta_1\}) = 0.6781$ </td></tr><tr><td> $m(\{\theta_2\}) = 0.8819$ </td><td> $m(\{\theta_2\}) = 0.4573$ </td><td> $m(\{\theta_2\}) = 0.1698$ </td><td> $m(\{\theta_2\}) = 0.3054$ </td></tr><tr><td> $m(\{\theta_3\}) = 0.1181$ </td><td> $m(\{\theta_3\}) = 0.0189$ </td><td> $m(\{\theta_3\}) = 0.0227$ </td><td> $m(\{\theta_3\}) = 0.0071$ </td></tr><tr><td></td><td> $m(\{\theta_2, \theta_3\}) = 0.0071$ </td><td> $m(\{\theta_2, \theta_3\}) = 0.0088$ </td><td> $m(\{\theta_2, \theta_3\}) = 0.0093$ </td></tr><tr><td rowspan="4"> $m_1, m_2, m_3, m_4, m_5$ </td><td> $m(\{\theta_1\}) = 0.0000$ </td><td> $m(\{\theta_1\}) = 0.6706$ </td><td> $m(\{\theta_1\}) = 0.8975$ </td><td> $m(\{\theta_1\}) = 0.8103$ </td></tr><tr><td> $m(\{\theta_2\}) = 0.9127$ </td><td> $m(\{\theta_2\}) = 0.3169$ </td><td> $m(\{\theta_2\}) = 0.0897$ </td><td> $m(\{\theta_2\}) = 0.1797$ </td></tr><tr><td> $m(\{\theta_3\}) = 0.0873$ </td><td> $m(\{\theta_3\}) = 0.0088$ </td><td> $m(\{\theta_3\}) = 0.0088$ </td><td> $m(\{\theta_3\}) = 0.0014$ </td></tr><tr><td></td><td> $m(\{\theta_2, \theta_3\}) = 0.0037$ </td><td> $m(\{\theta_2, \theta_3\}) = 0.0040$ </td><td> $m(\{\theta_2, \theta_3\}) = 0.0086$ </td></tr></table>

Table 2  
Comparison of combination results for Example 2.

<table><tr><td rowspan="2">BOEs Quantity</td><td colspan="4">Approach</td></tr><tr><td>Dempster&#x27;s rule</td><td>Murphy&#x27;s simple average</td><td>Deng&#x27;s weighted average</td><td>This paper</td></tr><tr><td>10</td><td> $m(\{\theta_1\}) = 0.4614$  $m(\Theta) = 0.5386$ </td><td> $m(\{\theta_1\}) = 0.4614$  $m(\Theta) = 0.5386$ </td><td> $m(\{\theta_1\}) = 0.4614$  $m(\Theta) = 0.5386$ </td><td> $m(\{\theta_1\}) = 0.3195$  $m(\Theta) = 0.6805$ </td></tr><tr><td>25</td><td> $m(\{\theta_1\}) = 0.7871$  $m(\Theta) = 0.2129$ </td><td> $m(\{\theta_1\}) = 0.7871$  $m(\Theta) = 0.2129$ </td><td> $m(\{\theta_1\}) = 0.7871$  $m(\Theta) = 0.2129$ </td><td> $m(\{\theta_1\}) = 0.3684$  $m(\Theta) = 0.6316$ </td></tr><tr><td>50</td><td> $m(\{\theta_1\}) = 0.9547$  $m(\Theta) = 0.0453$ </td><td> $m(\{\theta_1\}) = 0.9547$  $m(\Theta) = 0.0453$ </td><td> $m(\{\theta_1\}) = 0.9547$  $m(\Theta) = 0.0453$ </td><td> $m(\{\theta_1\}) = 0.3924$  $m(\Theta) = 0.6076$ </td></tr></table>

$$
\begin{array}{l l l l} m _ {1} ^ {n e w}: & m _ {1} ^ {n e w} (\{\theta_ {1} \}) = 0. 6 0, & m _ {1} ^ {n e w} (\{\theta_ {2} \}) = 0. 1 0, & m _ {1} ^ {n e w} (\{\theta_ {2}, \theta_ {3} \}) = 0. 3 0; \\ m _ {2} ^ {n e w}: & m _ {2} ^ {n e w} (\{\theta_ {1} \}) = 0. 6 5, & m _ {2} ^ {n e w} (\{\theta_ {2} \}) = 0. 1 0, & m _ {2} ^ {n e w} (\{\theta_ {3} \}) = 0. 2 5; \\ m _ {3} ^ {n e w}: & m _ {3} ^ {n e w} (\{\theta_ {1} \}) = 0. 0 0, & m _ {3} ^ {n e w} (\{\theta_ {2} \}) = 0. 9 0, & m _ {3} ^ {n e w} (\{\theta_ {2}, \theta_ {3} \}) = 0. 1 0; \\ m _ {4} ^ {n e w}: & m _ {4} ^ {n e w} (\{\theta_ {1} \}) = 0. 5 5, & m _ {4} ^ {n e w} (\{\theta_ {2} \}) = 0. 1 0, & m _ {4} ^ {n e w} (\{\theta_ {2}, \theta_ {3} \}) = 0. 3 5; \\ m _ {5} ^ {n e w}: & m _ {5} ^ {n e w} (\{\theta_ {1} \}) = 0. 5 5, & m _ {5} ^ {n e w} (\{\theta_ {2} \}) = 0. 1 0, & m _ {5} ^ {n e w} (\{\theta_ {2}, \theta_ {3} \}) = 0. 3 5; \end{array}
$$

The parameter α in Eq. (10) used in this example is $\alpha = 1 0 .$ The combination results derived based on different approaches are listed in Table 1.

Section 2.3. The FOD is $\boldsymbol { \Theta } = \{ \boldsymbol { \theta } _ { 1 } , \boldsymbol { \theta } _ { 2 } , \boldsymbol { \theta } _ { 3 } \}$ . The unequal-reliable BOEs (representing l different experts) sequentially acquired from the sensors are as follows:

$$
\left\{ \begin{array}{c} m _ {i} ^ {n e w} (\{\theta_ {1} \}) = 0. 0 6 \\ m _ {i} ^ {n e w} (\Theta) = 0. 9 4 \end{array} \right.
$$

It should be noted that in Murphy's simple average and the Deng's weighted average, the averaging operation is made by using the total <sup>fi</sup>ve BOEs in a batch while in our proposed approach, the fusion is executed sequentially. For the BOEs sequence listed above, the $m _ { 3 } ^ { n e w }$ can be considered as an interference item. As illustrated in Table 1, $m _ { 3 } ^ { n e w } ( \{ \theta _ { 1 } \} ) = 0 . 0 0 .$ Although in $m _ { 4 } ^ { n e w }$ and $m _ { 5 } ^ { n e w }$ the mass assignments for the proposition $\{ \theta _ { 1 } \}$ are all 0.55, for the combination result based on Dempster's rule of combination, the value of $m ( \{ \theta _ { 1 } \} )$ is always 0 after the arrival of $\ m _ { 3 } ^ { n e w }$ . This is a counter-intuitive behavior. To compare different combination approaches, convergence speed is de<sup>fi</sup>ned which represents the speed of increase for the mass assignment value of intuitively correct proposition. As we can see in Table 1, based on Murphy's simple average, Deng's weighted average and our proposed approach, the counter intuitive results can be suppressed. The convergence speed of our proposed approach is more rapid than that of Murphy's simple average and slower than that of Deng's weighted average. By using the weighted combination approaches (including our approach), we obtain the results which are closer to people's expectation.

where $i = 1 , . . . , l .$

Based on Dempster's combination rule, Murphy's simple average, Deng's weighted average, the combination results are the same as follows:

$$
\left\{ \begin{array}{c} m _ {l} ^ {c o m b} (\{\theta_ {1} \}) = 1 - 0. 9 4 ^ {l} \\ m _ {l} ^ {c o m b} (\Theta) = 0. 9 4 ^ {l} \end{array} \right.
$$

The parameter α in Eq. (10) used in this example is $\alpha = 1 0 .$ The combination results derived based on different approaches are listed in Table 2.

Another example is provided to show the rationality of the proposed approach according to counter-intuitive behavior II as illustrated in

## 4.2. Example 2

As illustrated in Table 2, Dempster's combination rule, Murphy's simple average and Deng's weighted average all bring out the counter-intuitive results. With the increase of the number of BOEs: l, $m ( \{ \theta _ { 1 } \} )$ become larger and larger, although for each BOE, $m _ { i } ^ { n e w } ( \{ \theta _ { 1 } \} ) =$ 0.06, which is very small. In our approach, this type of counter-intuitive result is not so signi<sup>fi</sup>cant as those in other combination approaches referred above. For example, when the 50th BOE has arrived, the combination result of our proposed approach is $m ( \{ \theta _ { 1 } \} ) = 0 . 3 9 2 4$ , based on which the correct decision can also be made while based on other approaches, $m ( \{ \theta _ { 1 } \} ) = 0 . 9 5 4 7$ can be derived, which can cause the wrong decision. The reason for the counter-intuitive results in this example is that the combined BOE changes in each step, although the new arriving BOEs are the same. Based on our approach, the variance of the sequence of the new arriving BOEs is always 0, which is always less than the variance of the sequence of the combined BOEs. Thus the effects of the new arriving BOEs are strengthened while the effects of the combined BOEs are suppressed. Based on the experimental results and the analysis above, it can be concluded that the type of counter-intuitive behavior illustrated in Example 2 can be effectively counteracted by our proposed approach. Our proposed approach can produce a better forecasting result with information aggregation, which is closer to people's expectation.

Table 3  
Comparison of combination results for Example 3.

<table><tr><td rowspan="2">BOEs</td><td colspan="4">Approach</td></tr><tr><td>Dempster&#x27;s rule</td><td>Murphy&#x27;s simple average</td><td>Deng&#x27;s weighted average</td><td>This paper</td></tr><tr><td> $m_1, m_2$ </td><td> $m(\{\theta_1\}) = 0.7000$  $m(\{\theta_1, \theta_2\}) = 0.3000$ </td><td> $m(\{\theta_1\}) = 0.5250$  $m(\{\theta_1, \theta_2\}) = 0.1179$  $m(\{\theta_3\}) = 0.3000$  $m(\Theta) = 0.0571$ </td><td> $m(\{\theta_1\}) = 0.5250$  $m(\{\theta_1, \theta_2\}) = 0.1179$  $m(\{\theta_3\}) = 0.3000$  $m(\Theta) = 0.0571$ </td><td> $m(\{\theta_1\}) = 0.5250$   $m(\{\theta_1, \theta_2\}) = 0.1179$  $m(\{\theta_3\}) = 0.3000$  $m(\Theta) = 0.0571$ </td></tr><tr><td> $m_1, m_2, m_3$ </td><td> $m(\{\theta_1\}) = 0.7000$  $m(\{\theta_1, \theta_2\}) = 0.3000$ </td><td> $m(\{\theta_1\}) = 0.3379$  $m(\{\theta_1, \theta_2\}) = 0.0615$  $m(\{\theta_3\}) = 0.5622$  $m(\Theta) = 0.0384$ </td><td> $m(\{\theta_1\}) = 0.1032$  $m(\{\theta_1, \theta_2\}) = 0.0290$  $m(\{\theta_3\}) = 0.8122$  $m(\Theta) = 0.0555$ </td><td> $m(\{\theta_1\}) = 0.2362$  $m(\{\theta_1, \theta_2\}) = 0.0363$  $m(\{\theta_3\}) = 0.6369$  $m(\Theta) = 0.0906$ </td></tr><tr><td> $m_1, m_2, m_3, m_4$ </td><td> $m(\{\theta_1\}) = 0.7000$  $m(\{\theta_1, \theta_2\}) = 0.3000$ </td><td> $m(\{\theta_1\}) = 0.1794$  $m(\{\theta_1, \theta_2\}) = 0.0292$  $m(\{\theta_3\}) = 0.7711$  $m(\Theta) = 0.0203$ </td><td> $m(\{\theta_1\}) = 0.1032$  $m(\{\theta_1, \theta_2\}) = 0.0093$  $m(\{\theta_3\}) = 0.9344$  $m(\Theta) = 0.0246$ </td><td> $m(\{\theta_1\}) = 0.0676$  $m(\{\theta_1, \theta_2\}) = 0.0089$  $m(\{\theta_3\}) = 0.8298$  $m(\Theta) = 0.0937$ </td></tr></table>

Table 4  
Comparison of combination results for Example 4.

<table><tr><td rowspan="2">Combination results</td><td colspan="4">Combination rules</td></tr><tr><td>Dempster&#x27;s rule</td><td>Murphy&#x27;s simple average</td><td>Deng&#x27;s weighted average</td><td>This paper</td></tr><tr><td rowspan="3">Mass</td><td>m(H) = 0.4579</td><td>m(H) = 0.4346</td><td>m(H) = 0.4532</td><td>m(H) = 0.4705</td></tr><tr><td>m(T) = 0.5417</td><td>m(T) = 0.5648</td><td>m(T) = 0.5460</td><td>m(T) = 0.5234</td></tr><tr><td>m(H,T) = 0.0004</td><td>m(H,T) = 0.0006</td><td>m(H,T) = 0.0008</td><td>m(H,T) = 0.0061</td></tr><tr><td rowspan="2">BetP</td><td>BetP({0}) = 0.4581</td><td>BetP({0}) = 0.4349</td><td>BetP({0}) = 0.4536</td><td>BetP({0}) = 0.4735</td></tr><tr><td>BetP({1}) = 0.5419</td><td>BetP({1}) = 0.5651</td><td>BetP({1}) = 0.5464</td><td>BetP({1}) = 0.5265</td></tr></table>

## 4.3. Example 3

This example is provided to show the rationality of the proposed approach according to counter-intuitive behavior III as illustrated in Section 2.4. The FOD is $\boldsymbol { \Theta } = \{ \boldsymbol { \theta } _ { 1 } , \boldsymbol { \theta } _ { 2 } , \boldsymbol { \theta } _ { 3 } \}$ . There are four unreliable BOEs as below:

$$
\begin{array}{c} m _ {1} (\{\theta_ {1} \}) = a, m _ {1} (\{\theta_ {1}, \theta_ {2} \}) = 1 - a \\ m _ {i} (\{\theta_ {3} \}) = b, m _ {i} (\{\theta_ {1}, \theta_ {2}, \theta_ {3} \}) = 1 - b; i = 2, 3, 4 \end{array}
$$

Here $a = 0 . 7 , b = 0 . 6 , \alpha = 1 0 .$ . The combination results based on different methods are shown in Table 3.

It can be seen that according to Dempster's rule, the combination results are always the same as m . Based on Murphy's simple average, Deng's weighted average and our proposed approach, the counterintuitive results can be suppressed. The convergence speed of our proposed approach is more rapid than that of Murphy's simple average and slower than that of Deng's weighted average. By using the weighted combination approaches (including our approach), we obtain the results which are closer to people's expectation.

## 4.4. Example 4

This example is about the coin <sup>fl</sup>ips, which is to predict performance of different approaches. Suppose that there are <sup>fi</sup>ve subjects. Each subject is privately shown a unique sample of coin <sup>fl</sup>ips of the chosen coin for 20 times. The subjects report their estimated probabilities (head and tail) sequentially, and we will have BOEs in the lab experiment. Since we know the underlying distribution of random variable in the lab experiment(0.5:0.5), it is possible to compare the prediction performance of different approaches to see the result of which approach is the most approximate to (0.5:0.5).

For each subject, the probabilities estimated are as follows:

(H: Head; T: Tail):

$$
\begin{array}{l} P _ {1} (h e a d) = 0. 4 7 5 0, P _ {1} (t a i l) = 0. 5 2 5 0; P _ {2} (h e a d) = 0. 4 5 0 0, P _ {2} (t a i l) = 0. 5 5 0 0; \\ P _ {3} (h e a d) = 0. 4 5 0 0, P _ {3} (t a i l) = 0. 5 5 0 0; P _ {4} (h e a d) = 0. 5 0 0 0, P _ {4} (t a i l) = 0. 5 0 0 0; \\ P _ {5} (h e a d) = 0. 5 5 0 0, P _ {5} (t a i l) = 0. 4 5 0 0. \end{array}
$$

The reliability of <sup>fi</sup>ve subjects is $W = [ 0 . 9 5 , 0 . 8 , 0 . 7 , 0 . 8 5 , 0 . 9 ] . \mathrm { ~ B y ~ }$ using discounting, i.e.,

$$
\left\{ \begin{array}{c} m _ {i} (A) = \alpha \cdot P _ {i} (A), \forall A \neq \Theta \\ m _ {i} (\Theta) = 1 - \alpha \end{array} \right.
$$

the corresponding BPAs of <sup>fi</sup>ve subjects are as follows:

$$
m _ {1} (H) = 0. 4 5 1 2, m _ {1} (T) = 0. 4 9 8 7, m _ {1} (H, T) = 0. 0 5 0 0
$$

$$
m _ {2} (H) = 0. 3 6 0 0, m _ {2} (T) = 0. 4 4 0 0, m _ {2} (H, T) = 0. 2 0 0 0
$$

<sup>ð Þ ¼ ð Þ ¼ ð Þ ¼</sup>m H 0:4250; m T 0:4250; m H; T 0:1500

According to four different combination approaches, the combination results can be obtained as shown in Table 4. Here we compare all the approaches' prediction capability, i.e., to see which is the most approximating to the ground-truth (0.5: 0.5).

Based on the results listed in Table 4, it can be concluded that our proposed new approach can bring out the result which is most ap proximate to the ground-truth (0.5:0.5).

## 5. Conclusions

For the combination of unreliable or unequal-reliable BOEs, we always obtain the counter-intuitive results which are far from people's intuition or expectation. To suppress the counter-intuitive results in evidence combination of unreliable or unequal-reliable BOEs, a novel sequential weighted evidence combination approach is proposed in this paper. The variances of BOE sequences are used to generate the weights, which to some degree represent the quality or the reliability of the BOEs. Comparisons of different modi<sup>fi</sup>ed evidence combination approaches are provided, which can verify that our proposed approach can suppress the counter-intuitive behavior in the combination of unreliable BOEs as illustrated in Example 1–Example 3. Furthermore it has good prediction performance as illustrated in Example 4. In fact, the combination rule used in our approach is still Dempster's rule of combination, only the BOEs to be combined are modi<sup>fi</sup>ed sequentially.

Some recent works [7,8] pointed out not only how to implement con<sup>fl</sup>icting evidence combination but also how to de<sup>fi</sup>ne and determine the con<sup>fl</sup>ict degree between BOEs which is still an open issue, and is one of our research works in the future.

## Acknowledgments

This work is supported by the National Natural Science Foundation of China (no. 61104214, no. 67114022, no. 61203222, no. 61074176), the Fundamental Research Funds for the Central Universities (no. xjj2012104), the China Postdoctoral Science Foundation (no. 20100481337, no. 201104670), the Foundation for Innovative Research Groups of the National Natural Science Foundation of China (no. 61221063) and Chongqing Natural Science Foundation (no. CSCT, 2010BA2003).

## References

[1] Y. Deng, W.K. Shi, Z.F. Zhu, et al., Combining belief functions based on distance of evidence, Decision Support Systems 38 (2004) 489–493.

[2] J. Dezert, P. Wang, A. Tachamova, On the validity of Dempster–Shafer theory, Proc. of the 15th International Conference on Information Fusion, IEEE Press, Singapore, July 2012, pp. 655–660.

[3] A. Tachamova, J. Dezert, On the behavior of Dempster's rule of combination and the foundations of Dempster-Shafer theory, Proc. of the 6th IEEE International Conference on Intelligent Systems, IEEE Press, So<sup>fi</sup>a, Bulgaria, Sept 2012, pp. 108–113

[4] M.C. Florea, E. Bossé, Crisis Management using Dempster Shafer Theory: Using Dissimilarity Measures to Characterize Sources' Reliability C3I for Crisis, Emergency and Consequence Management, 2009. 17-1–17-14.

[5] R. Haenni, Are alternatives to Dempster's rule of combination real alternative? Comments on “About the belief function combination and the conflict manage: ment problem", Information Fusion 3 (2002) 237-239

[6] A.-L. Jousselme, D. Grenier, E. Bosse, A new distance between two bodies of evidence Information Fusion 2 (2001) 91–101

[7] E. Lefevre, O. Colot, P. Vannoorenberghe, Belief functions combination and con-<sup>fl</sup>ict management, Information Fusion 3 (2002) 149–162

[8] W.R. Liu, Analyzing the degree of con<sup>fl</sup>ict among belief functions, Arti<sup>fi</sup>cial Intelligence 170 (2006) 909–924.

[9] A. Martin, A. Jousselme, C. Osswald, Con<sup>fl</sup>ict measure for the discounting operation on belief functions, International Conference on Information Fusion, 2008, pp. 1003–1010.

[10] C.K. Murphy, Combining belief functions when evidence con<sup>fl</sup>icts, Decision Support Systems 29 (2000) 1–9.

[11] J. Pearl, Reasoning with belief functions: an analysis of compatibility, International Journal of Approximate Reasoning 4 (1990) 363–389.

[12] G. Shafer, A Mathematical Theory of Evidence, Princeton University Press, Princeton, NJ, 1976.

[13] F. Smarandache, J. Dezert, Applications and Advances of DSmT for Information Fusion American Research Press Rehoboth NM USA 2009

[14] P. Smets, The combination of evidence in the transferable belief mode, IEEE Transactions on Pattern Analysis and Machine Intelligence 12 (1990) 447–458

[15] P. Wang, A defect in Dempster–Shafer theory [C], Proc. of 10th Conf. on Uncertainty in AI, 1994, pp. 560–566.

[16] R.R. Yager, On the Dempster–Shafer framework and new combination rules, The Information of the Science 41 (1987) 93-137.

[17] K. Yamada, A new combination of evidence based on compromise, Fuzzy Sets and Systems 159 (2008) 1689–1708

[18] L.A. Zadeh, A simple view of the Dempster–Shafer theory of evidence and its implication for the rule of combination, AI Magazine 2 (1986) 85–90.

![](/api/attachments/AKB588FC/fulltext/images/ba3027709e02958228b7f01a4fb29f2c4feda77b3deafbc2dc9277a882340bd5.jpg)  
Deqiang Han was born in 1980, in Shaanxi, PR China. He received the Bachelor's degree in Communication and Control Engineering from Xi'an Jiaotong University, Xi'an, China, in 2001, the Master's degree in Control Science and Engineering from Xi'an Jiaotong University, Xi'an, China, in 2004 the Ph.D. degree in Control Science and Engineering from Xi'an Jiaotong University, Xi'an, China, in 2008. He is currently an associate professor in the School of Electronic and Information Engineering, Xi'an Jiaotong University. His research <sup>fi</sup>elds include the information fusion, evidence theory and pattern classi<sup>fi</sup>cation.

![](/api/attachments/AKB588FC/fulltext/images/867e54260def072fce54f2270d2f7548e04e98d9b1d3f242711bfd320f37c3da.jpg)

![](/api/attachments/AKB588FC/fulltext/images/918af3a6ce7cbcacd8925d60afe1e53b5f012668ce71d79cbbd04afd7733af81.jpg)

Yong Deng was born in 1975, in Hunan, PR China. He received the Bachelor's degree in physics from Shanxi Normal University, Xi'an, China, in 1997, the Master's degree in In strument engineering from Hunan University, Changsha, China, in 2000, the Ph.D. degree in precise instrument and mechanic engineering from Shanghai Jiao Tong University, Shanghai, China, in 2003. He is currently an associate professor in the School of Electronics & Information Technology, Shanghai Jiao Tong University. His research interests are in the areas of information fusion, fuzzy logic and decision anal ysis.

Chongzhao Han was born in 1943, in Shaanxi, PR China. He is now the Professor in School of Electronic and Information Engineering, Xi'an Jiaotong University. His research <sup>fi</sup>elds include information fusion, automatic control and nonlinear system analysis.
