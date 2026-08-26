---
otero_id: 19766
otero_key: "FVUJRXWY"
title: "A new approximate belief rule base expert system for complex system modelling"
authors: "You Cao; Zhi Jie Zhou; Chang Hua Hu; Shuai Wen Tang; Jie Wang"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113558"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A new approximate belief rule base expert system for complex system modelling

You Cao, Zhi Jie Zhou <sup>\*</sup>, Chang Hua Hu, Shuai Wen Tang, Jie Wang

High-Tech Institute of Xi’an, Xi’an, Shaanxi 710025, PR China

## A R T I C L E I N F O

Keywords: Belief rule base Expert systems Interpretability Complex system modelling

## A B S T R A C T

Expert knowledge is the foundation of the interpretability of belief rule base (BRB) expert system. However, the rule explosion problem and weak extendability of BRB limit the utilization of expert knowledge. To solve this problem, a new approximate belief rule with single attributes is proposed, with which a new expert system named as ABRB is constructed. In the new rule, the correlation among attributes is discounted by the inde pendency factor. To illustrate the similar modelling ability of ABRB and BRB, the universal approximation ability of ABRB is proved theoretically. In the proposed ABRB, the key components, such as attributes, referential values, and the frame of discernment, can be extended to guarantee its effectiveness in the long-term practice. A case study of the Lithium-ion power battery is conducted to verify the effectiveness of the proposed model.

## 1. Introduction

By studying the expression scheme of uncertain knowledge and the knowledge base, Yang et al. embedded the belief structure into the traditional fuzzy rule base (FRB), and a more general expert system named as belief rule base (BRB) is proposed [1]. Compared with FRB, the belief rule in BRB is more flexible in representing fuzziness, incompleteness and nonlinearity. The evidential reasoning (ER) approach has the transparent and strict mathematical description in dealing with various uncertainties. It serves as the reasoning engine of BRB to generate the final result [1,29,30]. In BRB, the belief structure, IF-THEN rules, and ER approach provide a more practical and trans parent framework to present the internal mechanism of real systems [1,2].

The applications of BRB can be divided into two categories: 1) The BRB model is used as a universal approximator, which focuses on gaining a higher approximation performance. In this sense, the BRB model is regarded as a black box tool similar to BP neural network (BPNN), support vector machine (SVM), and so on [2]. 2) The BRB model is adopted as an expert system. The rules and structure of BRB are expected to have the meaning related to real systems, and reflect the internal mechanism of real systems. In this sense, the BRB model should have higher modelling accuracy and interpretability [31,32].

Expert knowledge plays a key role in the BRB expert system to guarantee its accuracy and interpretability [35,36]. Three situations in establishing BRB should be discussed. 1) The system principle is clear. In this situation, a completely accurate and interpretable BRB model or an analytical model can be constructed as the alternative. 2) There is no expert knowledge. In this situation, BRB is usually used as a datadriven model with a certain degree of transparency. 3) There is limited expert knowledge. In such a common situation, BRB is usually established with the limited expert knowledge and optimized by using the observational data samples. The practice shows that BRB has been widely applied in many fields. Typically, Zhou et al. introduced the online updating method into the BRB model to simulate the dynamic system [3,4]. To predict the hidden behavior of complex systems, a new hidden BRB forecasting model (HBRB) was proposed [5–7]. To obtain a more reliable BRB model, fault tree analysis was adopted to generate the belief rules [8]. Aiming at the unreliable observational information, the attribute reliability was introduced into the BRB model by Feng et al. [9].

To construct an interpretable BRB expert system, the expert knowl edge should be embedded into rules. Unfortunately, this process may be constrained in the BRB model under conjunctive assumptions. It leads to the rule explosion problem. that is. the number of rules increases exponentially with the number of attributes or referential values. Such a BRB model with a large number of rules has weak readability and extendability. Meanwhile, the parameters of all rules can hardly be determined by experts intuitively. To meet the requirement of engi neering practice, the original expert system should be extended by using new information. In this paper, extendability refers to the ability of expert system to be extended without changing the original parameters and structure [14]. Concretely, the BRB with good extendability means that the original belief rules are not required to be redesigned when new referential values/rules/attributes are added or deleted. However, the transversal combination of referential values in the traditional BRB causes the undesirable redesign of original rules [11].

Many efforts have been made to solve the above problems. For practical systems whose attributes are conjunctively correlated with each other, the conjunctive assumption should be applied, and vice versa. When the attributes are inter-independent, the single-attribute belief rule should be constructed without connection assumptions. Chang et al. proposed the belief rule under disjunctive assumptions, which could describe the disjunctive relationship between two attri butes and could avoid the rule explosion problem [10,11]. However, how the attributes correlated with each other may be unclear due to the difficulty in analyzing complex systems. To address that, Chang et al. and Beliakov et al. held that the type of assumption can be determined according to the perception of experts and/or decision makers because there is no theoretical ambiguity between them [12,13]. This is acceptable as an alternative in some applications [21]. Under the conjunctive assumption and the disjunctive assumption, some different methods have been developed to adjust the number of rules and refer ential values [4,15,16]. However, there are relatively few studies devoted to adjusting the number of attributes.

Single-attribute rules without the combination of referential values can perform well in both readability and extendability. Thus, there are some tentative works to deal with the correlation between two attri butes. Feng et al. proposed a decoupling matrix to reduce the correla tion, but the input information was changed [24]. In the Bayes network model (BN), the correlation between two attributes was approximated by the product of each marginal probability with a normalization factor [18–20]. Inspired by this, Chen et al. established the belief rule with single attributes to describe the causal relationship between attributes and the consequence separately [17]. Unfortunately, the correlation between two attributes was ignored directly, which appeared less rigorous. Li et al. described the correlation by using a factor, and further used it to reduce the impact of the attribute correlation. However, the rule was still under conjunctive assumptions [25]. To handle the attri bute correlation, a new single-attribute belief rule is proposed in this paper, where the independency factor is used to describe and reduce the impact of the attribute correlation. The new belief rule can be regarded as an approximation of the original belief rule, which is defined as the approximate belief rule (ABR). Composed of these ABRs, the new BRB model is called the approximate belief rule base (ABRB) model.

The main contribution of this paper is the development of an ABRB expert system for complex system modelling. It can effectively solve the rule explosion problem and weak extendability problem of the original BRB, so that the expert knowledge can be well introduced into the model. Meanwhile, the universal approximation ability of ABRB is proved theoretically. As a result, the ABRB model can be established in a more interpretable and reliable way, and can provide a new idea for constructing the large-scale expert system in the future.

$$
R _ {1}: \text { if } (X _ {1} \text {   is   } 3 6. 5 ^ {\circ} \mathrm{C}) \wedge (X _ {2}
$$

$$
R _ {9}: \text {   if   } (X _ {1} \text {   is   } 3 9 ^ {\circ} \mathrm{C}) \wedge (X _ {2}
$$

The remainder of this paper is organized as follows. The original BRB expert system and its problems are introduced in Section 2. The ABRB model is proposed in Section $^ { 3 , }$ followed by its extendability analysis in Section 4. To verify the effectiveness of proposed model, a case study is presented in Section 5. Section 6 concludes this paper.

## 2. A review of the BRB expert system and its problems

In Subsection 2.1, the basic knowledge of BRB expert system is introduced briefly, followed by the problem formulation in Subsection 2.2.

## 2.1. BRB expert system

The BRB expert system consists of a series of belief rules, where the kth belie rule is shown as follows:

$$
\begin{array}{l} R _ {k}: \text {   If   } X _ {1} \text {   is   } A _ {1} ^ {k} \wedge X _ {2} \text {   is   } A _ {2} ^ {k} \vee X _ {3} \text {   is   } A _ {3} ^ {k}... \wedge X _ {T _ {k}} \text {   is   } A _ {T _ {k}} ^ {k}, \\ \text {   Then   } \{(D _ {1} \beta_ {1 k}),..., (D _ {N} \beta_ {N k}) \}, \left(\sum_ {n = 1} ^ {N} \beta_ {n k} \leq 1\right) \\ \text {   with   a   rule   weight   } \theta_ {k} (k = 1, 2,..., L) \\ \text {   and   attribute   weights   } \delta_ {i} (i = 1, 2,..., T _ {k}) \end{array}\tag{1-a}
$$

where $A _ { i } ^ { k } ( i { = } 1 , { \ldots } , T _ { k } )$ and δ $( i = 1 , 2 , . . . , T _ { k } )$ denote the referential value and the weight of X respectively. $T _ { k }$ represents the number of attributes. L denotes the number of rules. $\theta _ { k }$ is the rule weight of the kth rule. $\beta _ { n k }$ (n $\mathbf { \Phi } = 1 , 2 , . . . , N )$ represents the belief degree of the consequence $D _ { n } . \wedge$ and ∨ represent the conjunctive assumption and the disjunctive assumption respectively, which are used to describe the relationship between two attributes. Specially, if the attributes are independent with each other, the belief rules can be established by using the single attribute. In this way, the mth belief rule of the ith attribute is described as:

$$
R _ {i, m}: \text {   If   } X _ {i} \text {   is   } A _ {i, m}, \text {   Then   } \big \{\big (D _ {1}, \beta_ {1, i, m} \big),..., \big (D _ {N}, \beta_ {N, i, m} \big) \big \}, \left(\sum_ {n = 1} ^ {N} \beta_ {n, i, m} \leq 1\right),
$$

$$
\text { with   a   rule   weight } \theta_ {i, m} \text { and   attribute   weights } \delta_ {i} (i = 1,..., T, m = 1,..., M _ {i})\tag{1-b}
$$

where $A _ { i , m }$ is the mth referential value of $X _ { i \cdot } M _ { i } ( i { = } 1 , . . . , T )$ is the number of referential values of $X _ { i \cdot } \ \beta _ { n , \ i , \ m } \ ( n = 1 , . . . , N )$ represents the belief degree of $D _ { n } . \theta _ { i , m }$ is the rule weight of $\widetilde { R } _ { i , m }$

To illustrate the belief rule in details, an example is given. There are usually two important attributes in the diagnosis of a cold. One is the temperature of the patient, denoted by $X _ { 1 }$ . The other is whether the patient has got a cough, denoted by $X _ { 2 } .$ . The referential values of $X _ { 1 }$ and $X _ { 2 }$ are $\{ 3 6 . 5 ^ { \circ } \mathrm { C } , 3 7 ^ { \circ } \mathrm { C } , 3 9 ^ { \circ } \mathrm { C } \}$ and {normal,medium,severe} respectively. Due to the correlation between $X _ { 1 }$ and $X _ { 2 } ,$ doctors usually make the judgement by combining these two conditions. Thus, the BRB expert system can be established as follows:

$$
\left(\theta_ {4} = 0. 8, \delta_ {1} = 1, \delta_ {2} = 1\right)\tag{2-a}
$$

Y. Cao et al.

Suppose that there is no correlation between $X _ { 1 }$ and $X _ { 2 } ,$ the BRB expert system constructed by using single-attribute rules is shown as follows:

Decision Support Systems xxx (xxxx) xxx

3. The ABRB model

In this section, the attribute correlation is analyzed in Subsection 3.1,

R<sub>1,1</sub> : if(X<sub>1</sub> is 36.5 C), then{( got a cold, 40%), ( not got a cold, 60%)}, θ<sub>1,1</sub> = 0.75, δ<sub>1</sub> = 1

R <sub>,</sub> : if (X is 39<sup>◦</sup> C), then {( got a cold, 75%), (not got a cold, 25%)}, θ <sub>,</sub> = 0.8, δ = 1

R<sub>2,1</sub> : if (X<sub>2</sub> is normal), then {( got a cold, 30%), (not got a cold, 70%)}, θ<sub>2,1</sub> = 0.8, δ<sub>2</sub> = 1

R : if (X is severe), then {( got a cold, 80%), (not got a cold, 20%)}, θ = 0.88, δ = 1

(2-b)

As the input data is available, the activated belief rules are aggre gated by the ER approach to generate the final result [1,5,9,11,12].

## 2.2. Problem formulation

The key point to construct an interpretable and extendable BRB model is to ensure that the expert knowledge can be well embedded into rules. For BRB under conjunctive/disjunctive assumptions, the rule ex plosion and weak extendability make it difficult for experts to under stand and determine all the rules intuitively. The explanation is given as follows.

According to Chang et al., the size of BRB under conjunctive assumption is calculated by $\begin{array} { r } { L _ { 1 } = \prod _ { i = 1 } ^ { T } M _ { i } , } \end{array}$ , where T represents the number of attributes. It can be seen that $L _ { 1 }$ increases exponentially with the number of attributes and reference values. Such a BRB may consist of a large number of rules when modelling the complex system, which brings out the difficulty in determining all the parameters manually.

Furthermore, with the understanding of real systems going deep, more information, such as attributes and referential values, should be added into the BRB expert system. The extendability requirement makes the BRB extended without redesigning the whole model. However, in current belief rules under connection assumptions, it may be difficult to add or delete elements without redesigning the whole model. For the example mentioned in Section 2.1, when a new condition whether the patient has got a sore throat (denoted by X ) is added, whose referential values are {normal,abnormal}, the whole rule base is given as follows:

followed by the description and reasoning of ABRB expert system. In Section 3.3, the Stone-Weierstrass Theorem is used to clarify the similar approximation ability of ABRB and BRB. The optimization process is implemented in Subsection 3.4.

## 3.1. The correlation between two attributes

Both the independency and the correlation can be utilized to describe the relationship between two variables. The two variables are interindependent if there is no relationship between them. Otherwise, their relationship could be categorized into two types called the linear cor relation and the nonlinear correlation. Reducing the correlation be tween two variables is conductive to enhancing the independency between them.

The correlation between two attributes is universal in engineering. The correlated features may increase the complexity and computational cost of models. Besides, the noise in correlated features may also reduce the modelling accuracy. Several methods are usually adopted to elimi nate the correlation between two features [25,26]: 1) Separating the overlapping source of features. For example, the sensors are set up in an orthogonal way. 2) Deleting the redundant features by using some feature selection methods. A traditional method is conducted by analyzing the system mechanism artificially. Another method is to measure the correlation between two features, and then determine the threshold to remove redundant features. However, there is no general method to determine the threshold. According to literature [34], the mean value of correlation measurements is usually used as the threshold. Moreover, the threshold can also be determined based on the

$$
\begin{array}{l} R _ {1}: \text {if} (X _ {1} \text {is} 3 6. 5 ^ {\circ} \mathrm{C}) \wedge (X _ {2} \text {is normal}) \wedge (X _ {3} \text {is normal}), \text {then} \left\{\left(\text {got a cold}, \beta_ {1, 1}\right), \left(\text {not got a cold}, \beta_ {2, 1}\right) \right\} \\ \dots \\ R _ {1 8}: \text {if} (X _ {1} \text {is} 3 9 ^ {\circ} \mathrm{C}) \wedge (X _ {2} \text {is severe}) \wedge (X _ {3} \text {is abnormal}), \text {then} \left\{\left(\text {got a cold}, \beta_ {1, 1 8}\right), \left(\text {not got a cold}, \beta_ {2, 1 8}\right) \right\} \end{array}\tag{3}
$$

where all the belief degrees should be redesigned. Especially, as the number of attributes increases, there is an increasing challenge to determine/understand all the belief degrees.

To avoid the above problem, it is a good alternative to construct the single-attribute rule in BRB. For the BRB constructed by using singleattribute rules, the model size is calculated by $\begin{array} { r } { L _ { 2 } = \sum _ { i = 1 } ^ { T } M _ { i } , } \end{array}$ where the increasing process of $L _ { 2 }$ is linear. Meanwhile, without connection as sumptions, the extension of BRB would be easier. Nevertheless, the correlation between two attributes is universal in engineering practice. In this paper, the proposed ABR can be regarded as the approximation of the original belief rule. The corresponding expert system is named as ABRB. Thus, the main problems to be solved are: 1) how to deal with the correlation between two attributes; 2) how to construct the ABR; 3) how to extend ABRB in engineering practice.

mechanism analysis and expert experience. 3) Modifying the weights of the features.

The first two methods aim at directly eliminating the correlation between two features while the third method can only reduce the impact of the correlation. Thus, in this paper, the strong correlation refers to the one that can be removed by using the first two methods. The weak correlation refers to the one whose impact can be reduced by the third method [25]. In the following contents, suppose that the strong corre lation between two features has been eliminated by using the first two methods. The third method will be adopted to handle the weak correlation.

In engineering practice, the correlation between different types of variables should be measured by different ways. Pearson coefficient is a classical correlation measurement, which has been widely applied in gene testing, machine learning, and so on. However, it only performs well in measuring the linear correlation between quantitative variables under normal distribution. Spearman coefficient and Kendall coefficient are used to measure the rank correlation between two variables without the requirement of normal distribution. Chi-squared test is usually used in analyzing the correlation between nominally categorical variables. Different from the above traditional methods, the mutual-informationbased method measures the correlation by measuring the change of information entropy. According to literature [33], the mutualinformation-based method is believed to have better generality and equitability, and can be used for various types of variables. In this paper, the correlation measure method is proposed based on the normalized mutual information between two variables.

Suppose that there are T feature variables denoted by $X _ { i } , ( i = 1 , . . . , T )$ The correlation between $X _ { i }$ and X can be described by using the maximal mutual information (MMI) as

$$
M M I \left(X _ {i} X _ {j}\right) = \max _ {\xi_ {x} \times \xi_ {y} <   B (n)} \left\{M I \left(\left(X _ {i} X _ {j}\right), \xi_ {x}, \xi_ {y}\right) \right\}\tag{4}
$$

where $\xi _ { x } \ \times \ \xi _ { y }$ denotes the mesh number, whose upper limitation is usually $B ( n ) \stackrel { \cdot } { = } n ^ { 0 . 6 }$ . n is the number of the data. $M I ( ( X _ { i } , X _ { j } ) , \xi _ { x } , \xi _ { y } )$ rep resents the mutual information (MI) between $X _ { i }$ and $X _ { j }$ under the mesh $\xi _ { x } \times \xi _ { y }$ , which is calculated by

$$
M I \left(X _ {i}, X _ {j}, \xi_ {x}, \xi_ {y}\right) = \sum_ {x _ {a} \in X _ {i}} \sum_ {x _ {b} \in X _ {j}} p (x _ {a}, x _ {b}) \log \frac {p (x _ {a} , x _ {b})}{p (x _ {a}) p (x _ {b})}\tag{5}
$$

where $x _ { i }$ and $x _ { j }$ are randomly divided into $\xi _ { x }$ and $\xi _ { y }$ bins to calculate the probabilities.

Definition 1. $\psi ( X _ { i } , X _ { j } )$ is defined as the degree of correlation between $X _ { i }$ and $X _ { j } ,$ which is calculated by

$$
\begin{array}{l} \widehat {E} (X _ {i}) = E (X _ {i}) - M M I (X _ {i}, X _ {j}) + M M I (X _ {i}, X _ {j}) \frac {E (X _ {i})}{E (X _ {i}) + E (X _ {j})} \\ = E (X _ {i}) \left[ 1 - \frac {M M I (X _ {i} , X _ {j})}{E (X _ {i}) + E (X _ {j})} \times \frac {E (X _ {j})}{E (X _ {i})} \right] = E (X _ {i}) \left[ 1 - \frac {1}{2} \psi (X _ {i}, X _ {j}) \frac {E (X _ {j})}{E (X _ {i})} \right] \end{array}\tag{7}
$$

Definition 2. The independency factor of $X _ { i }$ to $X _ { j }$ is defined as

$$
\varphi_ {i, j} = 1 - \frac {1}{2} \psi (X _ {i}, X _ {j}) \times \frac {E (X _ {j})}{E (X _ {i})}\tag{8}
$$

To reduce the weak correlation between $X _ { i }$ and $X _ { j } ,$ the attribute weight of $X _ { i }$ can be discounted by the independency factor as [25,26]:

$$
\delta_ {i} ^ {\prime} = \varphi_ {i, j} \times \delta_ {i}\tag{9-a}
$$

For further discussion, when there are T feature variables, $\operatorname { E q } .$ . (9-a) is presented as

$$
\delta_ {i} ^ {\prime} = \prod_ {j = 1, j \neq i} ^ {T} \varphi_ {i, j} \times \delta_ {i}\tag{9-b}
$$

## 3.2. The description and reasoning of the ABRB model

Suppose there are T attributes with $M _ { i } ( i = 1 , . . . , T )$ referential values. The mth ABR of the ith attribute in the ABRB model is described as:

$$
\begin{array}{l} \widetilde {R} _ {i, m}: \text {   If   } X _ {i} \text {   is   } A _ {i, m}, \text {   Then   } \big \{(D _ {1}, \beta_ {1, i, m}),..., (D _ {N}, \beta_ {N, i, m}) \big \}, \left(\sum_ {n = 1} ^ {N} \beta_ {n, i, m} \leq 1\right), \\ \text {   with   a   rule   weight   } \widetilde {\theta} _ {i, m} \text {   and   the   discounted   attribute   weights   } \delta_ {i} ^ {'} (i = 1,..., T, m = 1,..., M _ {i}) \end{array}\tag{10}
$$

$$
\psi \left(X _ {i}, X _ {j}\right) = \frac {2 M M I \left(X _ {i} , X _ {j}\right)}{M M I \left(X _ {i} , X _ {i}\right) + M M I \left(X _ {j} , X _ {j}\right)} = \frac {2 M M I \left(X _ {i} , X _ {j}\right)}{E \left(X _ {i}\right) + E \left(X _ {j}\right)}\tag{6}
$$

where E(X ) is the information entropy of $X _ { i } ,$ , which is equal to $M M I ( X _ { i } ,$ $X _ { i } ) \ [ 2 7 , 2 8 ] . \mathrm { I f } X _ { i }$ and $X _ { j }$ are independent, $\psi ( X _ { i } , X _ { j } )$ is 0. If X and $X _ { j }$ have a clear functional relationship, $\psi ( X _ { i } , X _ { j } )$ is 1. It is acceptable that the partial information entropy $E ( X _ { i } ) - { \dot { M } } { \dot { M } } I ( X _ { i } , X _ { j } )$ ) of $X _ { i }$ is independent with $E ( X _ { j } ) \mathrm { ~ - ~ } M M I ( X _ { i } , X _ { j } )$ of $X _ { j } .$ . Thus, the final independent information en tropy of $X _ { i }$ can be calculated by

When a data $x _ { i }$ of the ith attribute is imported into ABRB, it should be transformed into a belief distribution as $\{ ( A _ { i , m } , a _ { i , m } ) , i = 1 , . . . , T ; m = 1 ;$ $\ldots , M _ { i } \}$ by using the information transformation technique, such as the rule/utility-based equivalence transformation technique and the fuzzy membership function [1]. The matching degree between x and the rule can be calculated by $a _ { i } ^ { m } = \widetilde { \theta } _ { i , m } \big ( a _ { i , m } \big ) ^ { \overline { { \delta } } _ { i } ^ { ' } } .$ , where $\overline { { \delta } } _ { i } ^ { ' } = \delta _ { i } ^ { ' } { / m } a x _ { , T } \{ \delta _ { i } ^ { ' } \}$ denotes the normalized attribute weight. $\delta _ { i } ^ { \prime }$ is calculated by using Eqs. (4)–(9). Thus, the rule activation weight can be calculated by

$$
w _ {i, m} = a _ {i} ^ {m} \big / \sum_ {i ^ {*} = 1, m ^ {*} = 1} ^ {L} a _ {i ^ {*}} ^ {m ^ {*}}\tag{11}
$$

Then, generate the final belief degree by using the analytical ER approach as follows:

$$
\widehat {\beta} _ {n} = \frac {\left[ \prod_ {i = 1 , m = 1} ^ {L} \left(w _ {i , m} \beta_ {n , i , m} + \lambda_ {n} ^ {i , m}\right) - \prod_ {i = 1 , m = 1} ^ {L} \left(\lambda_ {n} ^ {i , m}\right) \right]}{\left[ \sum_ {n = 1} ^ {N} \prod_ {i = 1 , m = 1} ^ {L} \left(w _ {i , m} \beta_ {n , i , m} + \lambda_ {n} ^ {i , m}\right) - (N - 1) \prod_ {i = 1 , m = 1} ^ {L} \left(\lambda_ {n} ^ {i , m}\right) \right] - \left[ \prod_ {i = 1 , m = 1} ^ {L} \left(1 - w _ {i , m}\right) \right]}, \lambda_ {n} ^ {i, m} = 1 - w _ {i, m} \sum_ {n = 1} ^ {N} \beta_ {n, i, m}\tag{12}
$$

Finally, the result can be expressed as the following belief distribu tion form:

$$
S (A ^ {*}) = \left\{\left(D _ {n}, \widehat {\beta} _ {n}\right); n = 1, \dots , N \right\}\tag{13}
$$

where $A ^ { * }$ denotes the actual input vector, and the expected utility of S $( A ^ { * } )$ is expressed as:

$$
u (S (A ^ {*})) = \sum_ {n = 1} ^ {N} u (D _ {n}) \widehat {\beta} _ {n}\tag{14}
$$

Remark 1. The ABR in ABRB is actually a single-input rule, which is a special case of the original belief rule. It should be noted that the ABR is not proposed to replace the original belief rule, but an alternative option in modelling some complex systems.

Remark 2. The ABR is a single-input rule so that the difference be tween its attribute weight and rule weight should be explained. The attribute weight represents the relative importance of the corresponding attribute to others. The rule weight represents the relative importance of the corresponding rule to others, which can also reflect the confidence of experts to the prior knowledge in the rule.

## 3.3. The approximation ability of ABRB model

Both ABRB and BRB have clear semantic descriptions of the rela tionship between the attributes and the consequence. As for BRB, the correlation between two attributes is described by using connection assumptions. In ABR, the correlation between two attributes is reflected in the discounted attribute weights. Thus, these two types of rules will not produce ambiguity in expressing the same knowledge. To prove that ABRB has the same approximation ability as BRB, the related theorems and proof are presented as follows [2].

Theorem 1. (Universal Approximation Theorem) Let Ξ(x) be a set of ABRB models. Ω ∈ R denotes a compact set of input variables. For any given real continuous function h(x) and $\varepsilon > 0 ,$ , there exists an ABRB model f(x) ∈ $\Xi ( { \bf x } ) _ { i }$ , which satisfies

$$
\mathrm{SUP} _ {\mathbf {x} \in \Omega} | f (\mathbf {x}) - h (\mathbf {x}) | \leq \varepsilon\tag{15}
$$

where $\mathrm { \displaystyle { \cal S U P } } | \bullet |$ represents the upper bound. The output of ABRB expert system can be presented as

$$
\begin{array}{c} f (\mathbf {x}) = \frac {\sum_ {n = 1} ^ {N} u (D _ {n}) \zeta_ {n} (\mathbf {x})}{\sum_ {n = 1} ^ {N} \zeta_ {n} (\mathbf {x})}, \\ \zeta_ {n} (\mathbf {x}) = \prod_ {i = 1, m = 1} ^ {L} \left(w _ {i, m} (\mathbf {x}) \beta_ {n, i, m} + 1 - w _ {i, m} (\mathbf {x}) \sum_ {n = 1} ^ {N} \beta_ {n, i, m}\right) - \prod_ {i = 1, m = 1} ^ {L} \left(1 - w _ {i, m} (\mathbf {x}) \sum_ {n = 1} ^ {N} \beta_ {n, i, m}\right) \end{array}
$$

where $\zeta _ { n } ( \mathbf { x } )$ can be represented as a polynomial form of $w _ { i , m } ( { \bf x } )$

Theorem 2. (Stone-Weierstrass Theorem) Let Ξ(x) be a set of real continuous functions on a compact domain $\Omega \in \mathbb { R } .$ If 1)Ξ(x) is closed under addition, multiplication, and scalar multiplication; 2)For each x ∈ Ω, there exists $f ( \mathbf { x } ) \in \Xi ( \mathbf { x } )$ such that $f ( \mathbf { x } ) \neq 0 ;$ 3)For every $\mathbf { x } , \mathbf { x } ^ { \prime } \in \Omega , \mathbf { x } \neq \mathbf { x } ^ { \prime } ,$ there exists $f ( \mathbf { x } ) \in \Xi ( \mathbf { x } )$ such that $f ( \mathbf { x } ) \neq f ( \mathbf { x } ^ { \prime } )$ , then the uniform closure of Ξ(x) consists of all real continuous functions on Ω.

To prove the universal approximation properties of $f ( \mathbf { x } )$ , the Stone Weierstrass theorem is used for the following analysis.

Proof. Let $f _ { 1 } ( \mathbf { x } ) , f _ { 2 } ( \mathbf { x } ) \in \Xi ( \mathbf { x } )$ , and their sum and product can be calculated as follows:

$$
\begin{array}{c} f _ {1} (\mathbf {x}) + f _ {2} (\mathbf {x}) \\ = \frac {\sum_ {n 1 = 1} ^ {N 1} \sum_ {n 2 = 1} ^ {N 2} [ u _ {1} (D _ {n 1}) + u _ {2} (D _ {n 2}) ] \zeta_ {n 1} ^ {1} (\mathbf {x}) \zeta_ {n 2} ^ {2} (\mathbf {x})}{\sum_ {n 1 = 1} ^ {N 1} \sum_ {n 2 = 1} ^ {N 2} \zeta_ {n 1} ^ {1} (\mathbf {x}) \zeta_ {n 2} ^ {2} (\mathbf {x})} \end{array}\tag{17-a}
$$

$$
f _ {1} (\mathbf {x}) \times f _ {2} (\mathbf {x}) = \frac {\sum_ {n 1 = 1} ^ {N 1} \sum_ {n 2 = 1} ^ {N 2} u _ {1} (D _ {n 1}) u _ {2} (D _ {n 2}) \zeta^ {1} {} _ {n 1} (\mathbf {x}) \zeta^ {2} {} _ {n 2} (\mathbf {x})}{\sum_ {n 1 = 1} ^ {N 1} \sum_ {n 2 = 1} ^ {N 2} \zeta^ {1} {} _ {n 1} (\mathbf {x}) \zeta^ {2} {} _ {n 2} (\mathbf {x})}\tag{17-b}
$$

$$
c \times f (\mathbf {x}) = \frac {\sum_ {n = 1} ^ {N} c \times u (D _ {n}) \zeta_ {n} (\mathbf {x})}{\sum_ {n = 1} ^ {N} \zeta_ {n} (\mathbf {x})}\tag{17-c}
$$

where $c \in R .$ It is clear that $\zeta ^ { 1 } { } _ { n 1 } ( \mathbf { x } ) \zeta ^ { 2 } { } _ { n 2 } ( \mathbf { x } )$ can be presented as a poly nomial form of $w ^ { 1 } { } _ { i , m } ( \mathbf { x } ) w ^ { 2 } { } _ { i , m } ( \mathbf { x } )$ . In $\mathbf { A B R B } , w _ { i , m } ( \mathbf { x } )$ is calculated by the normalized matching function in Eq. (11) so $w ^ { 1 } { } _ { i , m } ( \mathbf { x } ) w ^ { 2 } { } _ { i , m } ( \mathbf { x } )$ has the same form as Eq. (11). In view of this, Eq. (17) can be represented as the same form of Eq. (16). Therefore, it can be concluded that Ξ(x) is closed under addition, multiplication, and scalar multiplication operations.

Obviously, it is easy to construct an ABRB that f(x) ∕= 0 when $u ( D _ { n } ) >$ $0 , n = 1 , . . . , N .$

To illustrate that there exists $f ( \mathbf { x } ) \in \Xi ( \mathbf { x } )$ such that $f ( \mathbf { x } ) \neq f ( \mathbf { x } ^ { \prime } ) , ( \mathbf { x } , \mathbf { x } ^ { \prime } \in$ $\mathbf { \Omega } \Omega , \mathbf { x } \neq \mathbf { x } ^ { \prime } )$ , a required ABRB with two rules is constructed as

$$
\begin{array}{l} \widetilde {R} _ {1, 1}: \text {If} X _ {1} \text {is} A _ {1, 1}, \text {Then} \left\{\left(D _ {1}, \beta_ {1, 1, 1}\right), \left(D _ {2}, \beta_ {2, 1, 1}\right) \right\} \text {with} \beta_ {1, 1, 1} = 1 \\ \widetilde {R} _ {1, 2}: \text {If} X _ {1} \text {is} A _ {1, 2}, \text {Then} \left\{\left(D _ {1}, \beta_ {1, 1, 2}\right), \left(D _ {2}, \beta_ {2, 1, 2}\right) \right\} \text {with} \beta_ {2, 1, 2} = 1 \end{array}\tag{18-a}
$$

where $A _ { 1 , 1 } , A _ { 1 , 2 }$ are the two referential values of $X _ { 1 } ,$ and $A _ { 1 , 1 } < A _ { 1 , 2 }$ Without loss of generality, suppose that $\mathbf { x } < \mathbf { x } ^ { \prime }$ for $\mathbf { x } , \mathbf { x } ^ { \prime } \in \Omega , \mathbf { x } \neq \mathbf { x } ^ { \prime }$ . It is clear that $w _ { 1 } ( \mathbf { x } ) < w _ { 1 } ( \mathbf { x } ^ { \prime } )$ and $w _ { 1 } ( { \bf x } ) + w _ { 2 } ( { \bf x } ) = 1$ . Thus, the output can be calculated by

(16)

$$
\begin{array}{l} f (\mathbf {x}) = \frac {u (D _ {1}) \zeta_ {1} (\mathbf {x}) + u (D _ {2}) \zeta_ {2} (\mathbf {x})}{\zeta_ {1} (\mathbf {x}) + \zeta_ {2} (\mathbf {x})} \\ \quad \quad \quad \quad \quad u (D _ {1}) \left[ \left(w _ {1, 1} (\mathbf {x}) \beta_ {1, 1, 1} + 1 - w _ {1, 1} (\mathbf {x})\right) \left(w _ {1, 2} (\mathbf {x}) \beta_ {1, 1, 2} + 1 - w _ {1, 2} (\mathbf {x})\right) - \left(1 - w _ {1, 1} (\mathbf {x})\right) \left(1 - w _ {1, 2} (\mathbf {x})\right) \right] \\ = \frac {+ u (D _ {2}) \left[ \left(w _ {1 , 1} (\mathbf {x}) \beta_ {2 , 1 , 1} + 1 - w _ {1 , 1} (\mathbf {x})\right) \left(w _ {1 , 2} (\mathbf {x}) \beta_ {2 , 1 , 2} + 1 - w _ {1 , 2} (\mathbf {x})\right) - \left(1 - w _ {1 , 1} (\mathbf {x})\right) \left(1 - w _ {1 , 2} (\mathbf {x})\right) \right]}{\left[ \left(w _ {1 , 1} (\mathbf {x}) \beta_ {1 , 1 , 1} + 1 - w _ {1 , 1} (\mathbf {x})\right) \left(w _ {1 , 2} (\mathbf {x}) \beta_ {1 , 1 , 2} + 1 - w _ {1 , 2} (\mathbf {x})\right) - \left(1 - w _ {1 , 1} (\mathbf {x})\right) \left(1 - w _ {1 , 2} (\mathbf {x})\right) \right]} \\ \quad \quad \quad + \left[ \left(w _ {1, 1} (\mathbf {x}) \beta_ {2, 1, 1} + 1 - w _ {1, 1} (\mathbf {x})\right) \left(w _ {1, 2} (\mathbf {x}) \beta_ {2, 1, 2} + 1 - w _ {1, 2} (\mathbf {x})\right) - \left(1 - w _ {1, 1} (\mathbf {x})\right) \left(1 - w _ {1, 2} (\mathbf {x})\right) \right] \\ = \frac {\left[ u (D _ {1}) + u (D _ {2}) \right] w _ {1 , 1} (\mathbf {x}) ^ {2} - 2 u (D _ {2}) w _ {1 , 1} (\mathbf {x}) + u (D _ {2})}{2 w _ {1 , 1} (\mathbf {x}) ^ {2} - 2 w _ {1 , 1} (\mathbf {x}) + 1} \end{array}\tag{18-b}
$$

Further, the derivative of f(x) can be calculated by

$$
\begin{array}{l} \left(2 (u (D _ {1}) + u (D _ {2})) w _ {1, 1} (\mathbf {x}) - 2 u (D _ {2})\right) \left(2 w _ {1, 1} (\mathbf {x}) ^ {2} - 2 w _ {1, 1} (\mathbf {x}) + 1\right) \\ \frac {\partial f (\mathbf {x})}{\partial w _ {1 , 1} (\mathbf {x})} = \frac {- \left((u (D _ {1}) + u (D _ {2})) w _ {1 , 1} (\mathbf {x}) ^ {2} - 2 u (D _ {2}) w _ {1 , 1} (\mathbf {x}) + u (D _ {2})\right) \left(4 w _ {1 , 1} (\mathbf {x}) - 2 w _ {1 , 1} (\mathbf {x}) + 1\right)}{\left(2 w _ {1 , 1} (\mathbf {x}) ^ {2} - 2 w _ {1 , 1} (\mathbf {x}) + 1\right) ^ {2}} \\ = \frac {2 w _ {1 , 1} (\mathbf {x}) \left[ (u (D _ {1}) - u (D _ {2})) (1 - w _ {1 , 1} (\mathbf {x})) \right]}{\left(2 w _ {1 , 1} (\mathbf {x}) ^ {2} - 2 w _ {1 , 1} (\mathbf {x}) + 1\right) ^ {2}} \end{array}\tag{2}
$$

(18-c)

where $( 2 w _ { 1 , 1 } ( { \bf x } ) ^ { 2 } - 2 w _ { 1 , 1 } ( { \bf x } ) + 1 ) ^ { 2 } > 0 ,$ . When $\begin{array} { r } { u ( D _ { 1 } ) > u ( D _ { 2 } ) , \frac { \partial f ( \mathbf { x } ) } { \partial w _ { 1 , 1 } ( \mathbf { x } ) } > 0 } \end{array}$ Thus, $f ( \mathbf { x } ) \neq f ( \mathbf { x } ^ { \prime } )$ , and $f ( \mathbf { x } ) < f ( \mathbf { x } ^ { \prime } )$

Based on the above analysis, it can be concluded that the ABRB model has the same universal approximation ability as the BRB model.

## 3.4. The optimization of ABRB model

Due to the limitation of expert knowledge, the initial parameters of ABRB should be further fine-tuned by using the observational data samples. The objective is to minimize the error between the output and the real value. The objective function is constructed as follows:

$$
\begin{array}{l} \min \{\psi (\widetilde {\theta}, \delta^ {^ {\prime}}, \beta) \} \\ s. t. 0 \leq \widetilde {\theta} _ {i, m} \leq 1, 0 \leq \delta_ {i} ^ {^ {\prime}} \leq 1, 0 \leq \beta_ {n, i, m} \leq 1, \sum_ {n = 1} ^ {N} \beta_ {n, i, m} \leq 1, \\ \beta_ {n, i, m} \sim I D _ {i, m}, (i = 1,..., T; n = 1,..., N; m = 1,..., M _ {i}) \end{array}\tag{19}
$$

where $\psi ( \widetilde { \boldsymbol { \theta } } , \delta ^ { \prime } , \beta )$ denotes the error between the outputs of ABRB and the real values. $I D _ { i , m }$ is the constraint for the belief distribution in rule $\widetilde { R } _ { i , m }$ to preserve its interpretability $[ 2 3 , 3 5 , 3 6 ]$

The optimization of ABRB is a typical nonlinear optimization prob

## 4. The extendability of ABRB model

The prior knowledge of the real system is accumulated gradually in long-term practice. For instance, in the early studies, the performance degradation process of Lithium-ion power battery (LPB) is believed to be a nonlinear process. However, with the advancement of these studies, the performance degradation process of LPB is proved to be a typical multi-stage process, that is, the degradation rate changes due to multiple changes in the working state of LPB. Thus, it is necessary to extend the corresponding expert system to guarantee the effectiveness of its final output. In this section, the extendability of ABRB model is discussed from three aspects: the extension of referential values, attributes and the frame of discernment (FoD).

## 4.1. The extension of attributes and referential values

Attributes are used to obtain the state information of real systems. The referential values are usually adopted to present the turning point of changes of system states. Due to the limitation of the expert knowledge, it may be difficult to determine all the proper attributes and referential values in a short time. To ensure the modelling accuracy, the referential value is usually adjusted by using the data samples. Actually, it is also effective to adjust the quantity of attributes and referential values in the long-term practice. For the example mentioned above, when the degradation process of LPB is continuously refined, the attributes and the corresponding referential values should be added or deleted to describe the changing law of the states of LPB.

In ABRB, each attribute corresponds to a series of ABRs, and each referential value corresponds to one of these ABRs. Thus, adjusting the quantity of attributes and referential values can be regarded as the adjustment of the number of rules. The extended ABRB model can be represented as:

$$
\begin{array}{l} \widetilde {R} _ {i, m}: \text {   If   } X _ {i} \text {   is   } A _ {i, m}, \text {   Then   } \big \{(D _ {1}, \beta_ {1, i, m}),..., (D _ {N}, \beta_ {N, i, m}) \big \}, \left(\sum_ {n = 1} ^ {N} \beta_ {n, i, m} \leq 1\right), \\ \text {   with   a   rule   weight   } \widetilde {\theta} _ {i, m} \text {   and   a   discounted   attribute   weight   } \delta_ {i} ^ {\prime} \left(i = 1,..., T + \widetilde {T}, m = 1,..., M _ {i} + \widetilde {M} _ {i}\right) \end{array}\tag{20}
$$

where $\left| \widetilde { T } \right| \mathrm { a n d } \left| \widetilde { M } _ { i } \right|$ respectively represent the number of attributes and referential values of X that should be added/deleted. When the attribute (or the referential value) is added, T<sup>̃</sup>(or M<sup>̃</sup> ) is a positive integer. Conversely, T<sup>̃</sup>(or M<sup>̃</sup> ) is a negative integer. Moreover, the discounted attribute weight δ <sup>′</sup> should be updated by using the updated indepen dency factors.

![](/api/attachments/FVUJRXWY/fulltext/images/17189ece0c9b894a773100cb3ccedc3120b4f9eea6825a8a630e398ff6ae8bd5.jpg)  
Fig. 1. The mechanism of capacity fade [39].

![](/api/attachments/FVUJRXWY/fulltext/images/3550ec8ec49556311fe6ec15bac901cc9739a8bd21d50d795d5db8074b424336.jpg)  
(a)

![](/api/attachments/FVUJRXWY/fulltext/images/48c43dccaa93b61df42022e2db1ded04557a13a107c1b9dc6747126f2b2e738c.jpg)  
(b)

![](/api/attachments/FVUJRXWY/fulltext/images/a76ab0872e227736c842f0eba53c981c79db5879c459b25f79878347dc4c3ed1.jpg)  
(c)

![](/api/attachments/FVUJRXWY/fulltext/images/2d1b3558463ca2959c843eb7f4a2d4040bfeb2eed3efb3308836861e34e59a18.jpg)  
(d)  
Fig. 2. (a) The capacity of LBP; (b)-(d) The observational features.

## 4.2. The extension of FoD

It is difficult to construct an accurate and complete FoD to describe a new engineering system. Thus, the adjustment of elements in FoD is necessary. The following discussion is conducted under the assumption that FoD is established by using the singleton propositions and universal set, which means that there are no local and global ignorance.

Suppose that the initial FoD is profiled as $\mathbf { \Theta } ^ { \Theta _ { 0 } } = \{ D _ { 1 } , D _ { 2 } , . . . , D _ { N } \}$ , and the “Then” part of $\widetilde { R } _ { i , m }$ is

Table 1  
The referential values of Time-CC

<table><tr><td>Referential points</td><td>VS</td><td>S</td><td>N</td><td>L</td><td>VL</td></tr><tr><td>Referential values (h)</td><td>0.4</td><td>0.5</td><td>0.65</td><td>0.8</td><td>1</td></tr></table>

$$
\left\{\left(D _ {1}, \beta_ {1, i, m}\right), \dots , \left(D _ {N}, \beta_ {N, i, m}\right) \right\}, \left(\sum_ {n = 1} ^ {N} \beta_ {n, i, m} \leq 1\right)\tag{21}
$$

where $\beta _ { 1 , ~ i , ~ m }$ is given by experts and further optimized by using data samples.

When a new element is added to the initial FoD, the “Then” part of $\widetilde { R } _ { i , m }$ is reconstructed as

Table 2  
The referential values of Time-CV.

<table><tr><td>Referential points</td><td>VS</td><td>S</td><td>N</td><td>L</td><td>VL</td><td>A</td></tr><tr><td>Referential values (h)</td><td>1.7</td><td>1.95</td><td>2.05</td><td>2.15</td><td>2.3</td><td>2.4</td></tr></table>

Table 3  
The referential values of LPB capacity.

<table><tr><td>Referential points</td><td>CS</td><td>S</td><td>LB</td><td>VB</td></tr><tr><td>Referential values (Ah)</td><td>1.96</td><td>1.7</td><td>1.5</td><td>1.2</td></tr></table>

$$
\left\{\left(D _ {1}, \beta_ {1, i, m} ^ {\prime}\right), \dots , \left(D _ {N}, \beta_ {N, i, m} ^ {\prime}\right), \left(D _ {N + 1}, \beta_ {N + 1, i, m} ^ {\prime}\right) \right\}, \left(\sum_ {n = 1} ^ {N + 1} \beta_ {n, i, m} ^ {\prime} \leq 1\right)\tag{22-a}
$$

where $\beta _ { n , \ i , \ m } ^ { \prime } ( n = 1 , . . . , N , N + 1 )$ represents the updated belief degree. There are three methods to determine the updated belief degrees: 1) Adjust all the belief degrees manually. It may be impractical if the size of ABRB is large. 2) Optimize all the belief degrees by using the data samples. It may be efficient but still costly due to the difficulty in obtaining adequate data samples. 3) Redistribute the belief degrees by using some methods, which has a better feasibility. It is further explained in the following contents.

That $D _ { N + 1 }$ should be added into the initial FoD means that the state $D _ { N + 1 }$ is not distinguished from other states due to the limitation of expert knowledge. Thus, Eq. (21) can be regarded as

$$
\begin{array}{c} \big \{\big (\phi_ {1} \beta_ {1, i, m} \big),..., \big (\phi_ {N} \beta_ {N, i, m} \big) \big \}, \big (\sum_ {n = 1} ^ {N} \beta_ {n, i, m} \leq 1 \big), \\ \phi_ {n} = \big \{D _ {n} \big (D _ {N + 1} \gamma_ {n, i, m} \big) \big \} \end{array}\tag{22-b}
$$

where $\phi _ { n }$ is the nth element of FoD, which is a subset of propositions. $\gamma _ { n , i , }$ <sub>m</sub>, $( 0 < \gamma _ { n , i , m } \leq 1 )$ ) is the probability of combining $D _ { N + 1 }$ with $D _ { n }$ when the FoD is firstly determined. $\gamma _ { n , i , m }$ can be obtained according to the expert knowledge and the analysis of engineering systems. It can be seen from Eq. (22-b) that every $\phi _ { n }$ may contain the same singleton proposition $D _ { N + 1 }$ , which means that they may all support $D _ { N + 1 }$ . Thus, the redistri <sub>bution</sub> <sub>method</sub> <sub>can</sub> <sub>be</sub> <sub>developed</sub> <sub>based</sub> <sub>on</sub> <sub>the</sub> <sub>traditional</sub> <sub>D</sub>–<sub>S</sub> <sub>rule</sub> <sub>[22]:</sub>

$$
\begin{array}{l} \beta_ {N + 1, i, m} ^ {\prime} = \frac {\sum_ {\phi_ {a} \cap \phi_ {b} = D _ {N + 1}} \gamma_ {a , i , m} \gamma_ {b , i , m} \beta_ {a , i , m} \beta_ {b , i , m} + \gamma_ {a , i , m} \beta_ {a , i , m} + \gamma_ {b , i , m} \beta_ {b , i , m}}{1 - \sum_ {\phi_ {a} \cap \phi_ {b} = \varnothing} (1 - \gamma_ {a , i , m}) (1 - \gamma_ {b , i , m}) \beta_ {a , i , m} \beta_ {b , i , m}}, a \neq b \\ = 1, 2, \dots , N \end{array}\tag{22-c}
$$

where $\beta _ { a , i , m }$ is the belief degree given by experts and further optimized by using data samples. Then, other updated belief degrees can be calculated by

$$
\begin{array}{c} \beta_ {n, i, m} ^ {\prime} = \frac {\beta_ {n , i , m}}{\sum_ {n = 1} ^ {N} \beta_ {n , i , m} + \beta_ {N + 1 , i , m} ^ {\prime}}, \\ \beta_ {N + 1, i, m} ^ {\prime} = \frac {\beta_ {N + 1 , i , m} ^ {\prime}}{\sum_ {n = 1} ^ {N} \beta_ {n , i , m} + \beta_ {N + 1 , i , m} ^ {\prime}} \end{array}\tag{22-d}
$$

When an element in the initial FoD is deleted, the “Then” part of $\widetilde { R } _ { i , m }$ can be reconstructed as

$$
\left\{\left(D _ {1} \dot {\beta_ {1 , i , m}}\right), \dots , \left(D _ {N - 1} \dot {\beta_ {N - 1 , i , m}}\right) \right\}, \left(\sum_ {n = 1} ^ {N - 1} \dot {\beta_ {n , i , m}} \leq 1\right)\tag{23}
$$

where $\beta _ { n , \ i , \ m } ^ { \prime } ( n = 1 , . . . , N - 1 )$ represents the updated belief degree. Suppose $D _ { N }$ is deleted, then the belief degree of $D _ { N }$ should be assigned to other states. Thus. Eq. (21) can be regarded as

$$
\begin{array}{l} \big \{\big (\phi_ {1}, \beta_ {1, i, m} \big),..., \big (\phi_ {N - 1}, \beta_ {N - 1, i, m} \big), \big (\phi_ {N}, \beta_ {N, i, m} \big) \big \}, \left(\sum_ {n = 1} ^ {N} \beta_ {n, i, m} \leq 1\right), \\ \phi_ {n} = \{D _ {n} \}, \phi_ {N} = \Bigg \{\left(D _ {1}, \widetilde {\gamma} _ {1, i, m}\right),..., \left(D _ {N}, \widetilde {\gamma} _ {N, i, m}\right) \Bigg \}, n = 1,..., N - 1, 0 \leq \widetilde {\gamma} _ {n, i, m} \leq 1 \end{array}
$$

Table 4  
The initial ABRB model.

<table><tr><td>No.</td><td>Attributes</td><td>Rule weights</td><td>Referential points</td><td>LPB capacity {CS, S, LB, VB}</td></tr><tr><td>1</td><td rowspan="2">Time-CC ( $\delta_1$ =0.9)</td><td>0.9</td><td>VS</td><td>{0,0,0,1}</td></tr><tr><td>2</td><td>0.9</td><td>S</td><td>{0, 0, 0.4, 0.6}</td></tr><tr><td>3</td><td></td><td>1</td><td>N</td><td>{0, 0.45, 0.55, 0}</td></tr><tr><td>4</td><td></td><td>0.8</td><td>L</td><td>{0.3, 0.4, 0.3, 0}</td></tr><tr><td>5</td><td></td><td>1</td><td>VL</td><td>{1,0,0,0}</td></tr><tr><td>6</td><td rowspan="2">Time-CV ( $\delta_2$ =1)</td><td>0.9</td><td>VS</td><td>{0.7, 0.3, 0, 0}</td></tr><tr><td>7</td><td>0.8</td><td>S</td><td>{0, 0.7, 0.2, 0.1}</td></tr><tr><td>8</td><td></td><td>0.9</td><td>N</td><td>{0, 0.4, 0.3, 0.3}</td></tr><tr><td>9</td><td></td><td>0.8</td><td>L</td><td>{0, 0.2, 0.5, 0.3}</td></tr><tr><td>10</td><td></td><td>0.8</td><td>VL</td><td>{0, 0, 0.3, 0.7}</td></tr><tr><td>11</td><td></td><td>0.8</td><td>A</td><td>{0, 0, 0.15, 0.85}</td></tr></table>

Table 5  
The optimized ABRB expert system.

<table><tr><td>No.</td><td>Attributes</td><td>Rule weights</td><td>Referential points</td><td>LPB capacity {CS, S, LB, VB}</td></tr><tr><td>1</td><td>Time-CC ( $\delta_1 = 0.85$ )</td><td>1.00</td><td>VS</td><td>{0, 0.004, 0.026, 0.97}</td></tr><tr><td>2</td><td></td><td>1.00</td><td>S</td><td>{0.018, 0.1, 0.286, 0.596}</td></tr><tr><td>3</td><td></td><td>0.99</td><td>N</td><td>{0.047, 0.334, 0.575, 0.044}</td></tr><tr><td>4</td><td></td><td>0.63</td><td>L</td><td>{0.24, 0.601, 0.132, 0.027}</td></tr><tr><td>5</td><td></td><td>1.00</td><td>VL</td><td>{0.908, 0.08, 0.012, 0}</td></tr><tr><td>6</td><td>Time-CV ( $\delta_2 = 0.99$ )</td><td>0.76</td><td>VS</td><td>{0.56, 0.202, 0.133, 0.105}</td></tr><tr><td>7</td><td></td><td>0.65</td><td>S</td><td>{0.126, 0.555, 0.272, 0.047}</td></tr><tr><td>8</td><td></td><td>0.80</td><td>N</td><td>{0.192, 0.199, 0.353, 0.256}</td></tr><tr><td>9</td><td></td><td>0.52</td><td>L</td><td>{0.035, 0.074, 0.561, 0.33}</td></tr><tr><td>10</td><td></td><td>0.66</td><td>VL</td><td>{0.16, 0.194, 0.201, 0.445}</td></tr><tr><td>11</td><td></td><td>0.83</td><td>A</td><td>{0.072, 0.161, 0.166, 0.601}</td></tr></table>

where $\phi _ { N }$ is the universal set of propositions. $\widetilde { \gamma } _ { n , i , m }$ is the probability of $D _ { n }$ existing in $\phi _ { N } .$ Thus, the redistribution of $\beta _ { N , ~ i , ~ m }$ can be regarded as a process to reduce the global ignorance. Thus, the redistribution method can be developed as:

$$
\begin{array}{c} \beta_ {n, i, m} ^ {\prime \prime} = \frac {\sum_ {\phi_ {N} \cap \phi_ {n} = \phi_ {n}} \widetilde {\gamma} _ {n , i , m} \beta_ {N , i , m} \beta_ {n , i , m}}{1 - \sum_ {\phi_ {N} \cap \phi_ {n} = \emptyset} \left(1 - \widetilde {\gamma} _ {n , i , m}\right) \beta_ {N , i , m} \beta_ {n , i , m}}, \\ n = 1, 2, \dots , N - 1 \end{array}\tag{24-b}
$$

Then, other updated belief degrees can be calculated by

$$
\beta_ {n, i, m} ^ {\prime} = \frac {\beta_ {n , i , m} + \beta_ {n , i , m} ^ {\prime \prime}}{\sum_ {n = 1} ^ {N - 1} \beta_ {n , i , m} + \beta_ {n , i , m} ^ {\prime \prime}}, (n = 1,..., N - 1)\tag{24-c}
$$

(24-a)

![](/api/attachments/FVUJRXWY/fulltext/images/b9747d67169deb775997da7cfdc856dc1a417f82c84d44607f6a611d4ac897c8.jpg)  
Fig. 3. The comparison between the initial and the optimal belief distributions

![](/api/attachments/FVUJRXWY/fulltext/images/4325c95d57ce0a9378cb6e6248d12954a21c11b792cc24670048268fc8fecb7e.jpg)  
Fig. 4. The belief degrees of each health state generated by the optimized ABRB.

Remark 3. It should be noted that the updated belief rules ought to be checked by using the interpretability constraints from the analysis of real systems. For instance, Zhou et al. proposed the interpretability constraint for the belief distribution of consequences to preserve the interpretability of rules, where the interpretability constraint was ob tained according to the historical information, mass balance principle and the running patterns of pipeline leak [23]. The wrong rules should be further adjusted manually.

Remark 4. The above redistribution method is a secondary processing method, which may bring more errors to the model when the extension of FoD is complex. In engineering practice, the comprehensive appli cation of the above three methods to determine the updated belief de grees may achieve a better performance.

## 5. Case study

LPB is the key part of spacecraft power systems, whose health state has a direct impact on the operation state of spacecrafts. Therefore, estimating the health state of LPB accurately by using a reliable and interpretable method is important for the operation/maintenance of spacecraft. As shown in Fig. 1, LPB is mainly composed of the current collector, the composite positive-negative electrode, the active material, the separator and the electrolyte [39]. The properties of these compo nents may gradually decay in the process of cyclic charging and dis charging. For instance, the corrosion may occur in the current collector. The positive electrode may dissolve, and the separator may consume the Lithium-ion. All the above changes are further reflected in the fading of battery capacity. Thus, the capacity of LBP is usually taken as a direct index of the health state of LPB. In the laboratory, the capacity of LPB can be easily obtained by using various testing instruments. However, when the LPB is loaded on the spacecraft, the observational features are limited and can be affected by many uncertain factors, such as the electromagnetic radiation and the load state change. This leads to the difficulty in estimating the capacity of LBP. Thus, it is necessary to establish an interpretable relationship between the observational fea tures and the capacity of LPB.

![](/api/attachments/FVUJRXWY/fulltext/images/6edf09daba5c3cc16f87a11b09ca2a79dbe2b62f9b7c8f72f66529c83d0f59b5.jpg)  
Fig. 5. The outputs of the initial ABRB and the optimized ABRB.

Table 6  
Comparative studies.

<table><tr><td>Models</td><td>MSE</td></tr><tr><td>Initial ABRB</td><td>1.51E-3</td></tr><tr><td>Optimized ABRB</td><td>1.04E-4</td></tr><tr><td>BRB</td><td>1.06E-4</td></tr><tr><td>FRB</td><td>1.67E-3</td></tr><tr><td>BPNN</td><td>0.98E-4</td></tr><tr><td>ELM</td><td>1.09E-4</td></tr></table>

Table 7  
Comparative studies between ABRB and BPNN.

<table><tr><td>Training set</td><td>MSE (ABRB)</td><td>MSE (BPNN)</td></tr><tr><td>10%</td><td>1.62E-4</td><td>1.48E-3</td></tr><tr><td>30%</td><td>1.10E-4</td><td>2.46E-4</td></tr><tr><td>50%</td><td>1.04E-4</td><td>0.98E-4</td></tr><tr><td>60%</td><td>0.95E-4</td><td>0.81E-4</td></tr></table>

A long-term testing experiment is conducted by simulating the working environment of LPB in NASA Ames Prognostics Center of Excellence, where the type of LPB is Gen 218,650-size with the nominal capacity 2000mAh, and the ambient temperature is 24 °C. The specific operation process is profiled as: 1) Charging Operation. It is divided into two stages. The first stage uses the constant current charging mode, named as CC-stage. The second stage uses the constant voltage charging mode, named as CV-stage. In CC-stage, LPB is charged at a constant current of 1.5A until the voltage reaches 4.2 V. Then, in the CV-stage, LPB is charged at a constant voltage of 4.2 V until the current drops to 20 mA; 2) Discharging Operation. The discharging load is 2A, and the cut-off voltage is 2.7 V.

145 cycles of data are collected in the experiment. Fig. 2-(a) shows the real fading process of capacity, and three observational features, named as the charging time of CC-stage, the charging time of CV-stage and the heating rate of CC-stage, are shown in Fig. 2 (b), (c), and (d) respectively. As can be seen from Fig. 2, although the features are correlative to the capacity of LPB, it is still difficult for experts to determine the capacity directly by using these features.

Table 8  
The referential values of Heating rate.

<table><tr><td>Referential points</td><td>L</td><td>M</td><td>H</td></tr><tr><td>Referential values (°C/h)</td><td>2.5</td><td>5</td><td>7</td></tr></table>

In related researches [37,38], the BRB expert system is used as an interpretable model to estimate the state of LPB. The proposed rule reduction method in literature [38] improved the readability of BRB. These researches were effective on a certain level, but they ignored the extendability requirement of BRB in the future. In the next subsection, an ABRB expert system is constructed to estimate the health state of LPB.

## 5.1. Construction and training of ABRB model for LPB health state estimation

In the ABRB model, the features Charging time of CC-stage (denoted by Time-CC) and Charging time of CV-stage (denoted by Time-CV) are used as two attributes. According to the operation state and historic knowledge of LPB, five and six referential points are assigned to Time-CC and Time-CV respectively. The referential points of Time-CC, named as Very Short (VS), Short (S), Normal (N), Long (L), and Very Long (VL), are shown in Table 1. The referential points of Time-CV, named as Very Short (VS), Short (S), Normal (N), Long (L), Very Long (VL) and Abnormal (A), are presented in Table 2.

According to the engineering application of LPB, when the capacity of LPB is higher than 98%. the health state of LPB is Completely Safe (CS). When the capacity of LPB decreases to 85% of the normal capacity, LPB is Safe (S). When the health state of LPB is Little Bad (LB) but still meets the application requirements, the capacity of LPB decreases to 75%. As the capacity of LPB decreases to 60%, the health state of LPB is Very Bad (VB). Then, the LPB should be replaced. The referential values of LPB capacity is shown in Table 3.

In the CC-stage, the charged capacity is in positive correlation with Time-CC, which reflects the positive correlation between Time-CC and the real capacity of LPB. The CV-stage is mainly affected by the prop erties of the positive-negative electrode materials and the electrolyte, which is further presented in Time-CV. Generally, the properties of the positive-negative electrode materials and the electrolyte change with the degradation of LPB performance so that Time-CV may increase. Based on the above analysis, the structure of ABRB is profiled as Eq. (25) and the initial ABRB model is given by experts as shown in Table 4. The initial attribute weights of Time-CC and Time-CV are 0.9 and 1 respec tively. By using Eqs. (4)–(9), the independency factors of Time-CC and Time-CV are 0.643 and 0.635 respectively.

$\widetilde { R } _ { 1 , 1 }$ : If Time − CC is VS, Then $\big \{ \big ( C S , \beta _ { 1 , 1 , 1 } \big ) , . . . , \big ( V B , \beta _ { 4 , 1 , 1 } \big ) \big \}$ , with rule weight $ { \widetilde { \theta } } _ { 1 , 1 }$ and discounted attribute weights $\delta _ { 1 } ^ { ' }$

$\widetilde { R } _ { 1 , 5 }$ : If Time − CC is VL, Then $\left\{ { \left( C S , \beta _ { 1 , 1 , 5 } \right) , . . . , \left( V B , \beta _ { 4 , 1 , 5 } \right) } \right\}$ , with rule weight $\widetilde { \theta } _ { 1 , 5 }$ and discounted attribute weights $\delta _ { 1 } ^ { ' }$

$\widetilde { R } _ { 2 , 1 }$ : If Time − CV is VS, Then $\left\{ \left( C S , \beta _ { 1 , 2 , 1 } \right) , . . . , \left( V B , \beta _ { 4 , 2 , 1 } \right) \right\}$ , with rule weight $ { \widetilde { \theta } } _ { 2 , 1 }$ and discounted attribute weights $\delta _ { 2 } ^ { ' }$

(25)

$\widetilde { R } _ { 2 , 6 }$ : If Time − CV is A, Then $\left\{ { \left( C S , \beta _ { 1 , 2 , 6 } \right) , . . . , \left( V B , \beta _ { 4 , 2 , 6 } \right) } \right\}$ , with rule weight $\widetilde { \theta } _ { 2 , 6 }$ and discounted attribute weights $\delta _ { 2 } ^ { ' }$

## 5.2. Training and testing of ABRB model

The objective function is given as Eq. (19), where $\psi ( \theta , \delta , \beta )$ is calcu lated by using the mean square error (MSE). $I D _ { i , m }$ is profiled as

$$
\begin{array}{c} I D _ {i, m} \to \beta_ {i, m} \not \in \left\{\beta | \big (\beta_ {n, i, m} \leq \beta_ {n - 1, i, m} \big) \& \big (\beta_ {n, i, m} \leq m a x \big (\beta_ {n + 1, i, m},..., \beta_ {N, i, m} \big) \big) \right\} \\ n = 2,..., N - 1,   i = 1,..., T, m = 1,..., M _ {i} \end{array}\tag{26}
$$

which means that the conflicted health state of LPB should not be sup ported with a high belief degree concurrently [35,36].

P-CMA-ES algorithm is adopted in this study, whose maximal itera tion is set to be 200 [35].50% data samples are selected randomly as the training data while the whole data set is treated as testing data. The parameters of the optimized ABRB are shown in Table 5. The initial and optimized belief distributions in the rules are compared in Fig. 3. It can be seen that the belief distributions in the optimized ABRB are close to the initial ABRB, which indicates that these parameters are optimized locally. Moreover, the optimized belief distributions are consistent with the constraints $I D _ { i , m }$ and the initial judgement from experts. The MSE of the optimized ABRB expert system is 1.04E-4, which can satisfy the accuracy requirement in engineering practice. The belief degrees of each health state generated by the optimized ABRB are shown in Fig. 4, which indicates the whole migration process of LPB health states.

The outputs of the initial and the optimized ABRB are shown in Fig. 5. It can be seen that the optimized ABRB can give a more accurate result than the initial ABRB. The MSE of the initial ABRB is 1.51E-3, and the accuracy of the optimized ABRB is improved by 93.11%. For further discussion, as shown in Fig. 5, the initial ABRB cannot estimate the capacity accurately when the health state of LPB is between LB and VB. The reason may be that the operation state is affected by the environ ment when the health state of LPB is bad, and the prior knowledge from experts cannot describe these uncertainties well. This reflects the importance of fine-tuning ABRB parameters by using the observational data.

Table 9  
The newly added initial rules.

<table><tr><td>No.</td><td>Attributes</td><td>Rule weights</td><td>Referential points</td><td>LPB capacity {CS, S, LB, VB}</td></tr><tr><td>12</td><td rowspan="3">Heating rate ( $\delta_3 = 0.9$ )</td><td>1</td><td>L</td><td>{1, 0, 0, 0}</td></tr><tr><td>13</td><td>1</td><td>M</td><td>{0, 0.2, 0.4, 0.4}</td></tr><tr><td>14</td><td>1</td><td>H</td><td>{0, 0, 0, 1}</td></tr></table>

Table 10  
The optimized rules.

<table><tr><td>No.</td><td>Attributes</td><td>Rule weights</td><td>Referential points</td><td>LPB capacity {CS, S, LB, VB}</td></tr><tr><td>12</td><td rowspan="2">Heating rate ( $\delta_3 = 0.91$ )</td><td>1</td><td>L</td><td>{0.68, 0.19, 0.13, 0}</td></tr><tr><td>13</td><td>0.67</td><td>M</td><td>{0.17, 0.18, 0.18, 0.47}</td></tr><tr><td>14</td><td></td><td>0.79</td><td>H</td><td>{0, 0.1, 0.16, 0.74}</td></tr></table>

Table 11

Remark 5. For a data-driven model, its initial parameters are gener ated randomly without prior knowledge. To optimize such a model, the search space of parameters is expected to cover all the parameters space. For the ABRB model, the prior knowledge acquired from the system principle and the testing data plays a key role in the model interpret ability. According to the prior knowledge, the meanings of the param eters constitute a constraint on the search space. Besides, the initial values of these parameters are also determined according to the prior

Table 12  
The extend ABRB model.

<table><tr><td>No.</td><td>Attributes</td><td>Rule weights</td><td>Referential points</td><td>LPB capacity {CS, S, LB, VB, CF}</td></tr><tr><td>1</td><td>Time-CC ( $\delta_1 = 0.85$ )</td><td>1.00</td><td>VS</td><td>{0, 0.003, 0.022, 0.809, 0.166}</td></tr><tr><td>2</td><td></td><td>1.00</td><td>S</td><td>{0.017, 0.093, 0.265, 0.552, 0.073}</td></tr><tr><td>3</td><td></td><td>0.99</td><td>N</td><td>{0.047, 0.334, 0.575, 0.044, 0}</td></tr><tr><td>4</td><td></td><td>0.63</td><td>L</td><td>{0.24, 0.601, 0.132, 0.027, 0}</td></tr><tr><td>5</td><td></td><td>1.00</td><td>VL</td><td>{0.908, 0.08, 0.012, 0, 0}</td></tr><tr><td>6</td><td>Time-CV ( $\delta_2 = 0.99$ )</td><td>0.76</td><td>VS</td><td>{0.56, 0.202, 0.133, 0.105, 0}</td></tr><tr><td>7</td><td></td><td>0.65</td><td>S</td><td>{0.126, 0.555, 0.272, 0.047, 0}</td></tr><tr><td>8</td><td></td><td>0.80</td><td>N</td><td>{0.192, 0.199, 0.353, 0.256, 0}</td></tr><tr><td>9</td><td></td><td>0.52</td><td>L</td><td>{0.035, 0.074, 0.561, 0.33, 0}</td></tr><tr><td>10</td><td></td><td>0.66</td><td>VL</td><td>{0.15, 0.182, 0.189, 0.417, 0.062}</td></tr><tr><td>11</td><td></td><td>0.83</td><td>A</td><td>{0.067, 0.149, 0.153, 0.556, 0.075}</td></tr><tr><td>12</td><td rowspan="2">Heating rate ( $\delta_3 = 0.91$ )</td><td>1</td><td>L</td><td>{0.68, 0.19, 0.13, 0, 0}</td></tr><tr><td>13</td><td>0.67</td><td>M</td><td>{0.159, 0.168, 0.168, 0.44, 0.065}</td></tr><tr><td>14</td><td></td><td>0.79</td><td>H</td><td>{0, 0.092, 0.147, 0.678, 0.083}</td></tr></table>

The probabilities given by experts.

<table><tr><td>No.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td> $\gamma_{1,i,m}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $\gamma_{2,i,m}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $\gamma_{3,i,m}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $\gamma_{4,i,m}$ </td><td>0.2</td><td>0.1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.1</td><td>0.1</td><td>0</td><td>0.1</td><td>0.1</td></tr></table>

![](/api/attachments/FVUJRXWY/fulltext/images/87f96c84f0d52fde455ab4f09415223d035f845307c5b01ba06684302dba5bf3.jpg)  
Fig. 6. The outputs of the extended ABRB with new FoD.

![](/api/attachments/FVUJRXWY/fulltext/images/8d8974090b3d80053101596352c3d6d48516d15bc3392d9606e2826f008d31e5.jpg)  
Fig. 7. The slope of the belief degrees to each health state.

knowledge. They are closer to the best point in the feasible search space. In this way, the optimization of ABRB is a local searching process based on the initial judgement from experts. Although the values of parameters do not change much, the optimization process is still effective, because it keeps a good balance between the model interpretability and the modelling accuracy. In other words, the optimized ABRB model inherits the initial judgement of experts, retains the meaning of parameters, and obtains the required modelling accuracy.

## 5.3. Comparative studies

In order to illustrate the effectiveness of the proposed ABRB expert system, comparative studies are implemented by using the original BRB expert system, back propagation neural network (BPNN), extreme learning machine (ELM) and fuzzy rule-based system (FRB). The refer ential values in the original BRB and FRB are the same as ABRB. The initial parameters of BPNN and ELM are determined randomly. FRB is constructed based on expert judgement. The MSEs of these models are profiled in Table 6. Similarly, 50% data samples are selected randomly as the training data while the whole data set is treated as the testing data.

Similar to the BRB model, ABRB also has a good modelling perfor mance. However, ABRB has 11 rules while BRB has 30 rules, which indicates that ABRB has a more compact structure. It may be more ad vantageous, especially when modelling the complex engineering system with a large number of features. As for the FRB, its modelling accuracy is influenced by the expert knowledge that cannot describe the real system accurately with various uncertainties. BPNN and ELM are the typical data-driven models, which can achieve an excellent performance when there are adequate data samples. As shown in Table $^ { 6 , }$ when 50% data samples are selected randomly as the training data, the BPNN has a better performance than ABRB. To further illustrate this issue, 10%, 30%, 60% data samples are selected randomly as the training data, and the MSEs of ABRB and BPNN are shown in Table 7. It can be seen that ABRB has a better performance than the BPNN in modelling the complex system with limited data samples.

Remark 6. In this paper, the training data set is selected randomly from the testing set (the whole set). It may lead to the biased evaluation of ABRB. For further illustration, suppose the data set is divided into two parts: the training set and the testing set. The outputs generated by the training set and the testing set are denoted by $y _ { i } ( i = 1 , . . . , N _ { 1 } )$ and $y _ { j } ( j =$ $1 , . . . , N _ { 2 } )$ respectively. The corresponding real values are denoted by $\widetilde { y } _ { i } ( i = 1 , . . . , N _ { 1 } )$ and $\widetilde { y } _ { j } ( j = 1 , . . . , N _ { 2 } )$ ) respectively. Thus, the correspond ing MSEs can be calculated by

$$
\begin{array}{l} M S E _ {1} = \left(\sum_ {i = 1} ^ {N _ {1}} \left(y _ {i} - \widetilde {y} _ {i}\right) ^ {2}\right) / N _ {1}, \\ M S E _ {2} = \left(\sum_ {j = 1} ^ {N _ {2}} \left(y _ {j} - \widetilde {y} _ {j}\right) ^ {2}\right) / N _ {2} \end{array}\tag{27-a}
$$

The MSE calculated by the whole data set is shown as

$$
M S E = \left(N _ {1} \cdot M S E _ {1} + N _ {2} \cdot M S E _ {2}\right) / \left(N _ {1} + N _ {2}\right)\tag{27-b}
$$

Further,

$$
M S E - M S E _ {2} = N _ {1} \cdot (M S E _ {1} - M S E _ {2}) / (N _ {1} + N _ {2})\tag{27-c}
$$

where $M S E _ { 1 } < M S E _ { 2 } ,$ so $M S E < M S E _ { 2 } .$ Therefore, the data set partition method in this paper leads to a biased evaluation of ABRB. However, such a data set partition method has no significant impact on analyzing the model performance, and it is common in engineering practice [17,35,40]. For instance, Xu et al. selected 500 samples from the whole 2008 samples in detecting the pipeline leak [40]. The reasons are: 1) the data set for training and testing are used for all models in the compar ative studies. It means that these models are compared fairly and effectively; 2) the working modes included in the training data set may also appear in the testing data set. This is in line with the engineering practice.

In the above comparison, let 50% samples are selected randomly as the training set while the rest 50% samples are the testing set. The MSEs of the optimized ABRB, BRB, BPNN and ELM are 1.08E-4, 1.11E-4, 1.05E-4 and 1.14E-4 respectively. It can be seen that BPNN has a better modelling accuracy, which is consistent with the results in Table 6. Moreover, the change of these MSEs also indicates a better learning performance of BPNN and a better generalization performance of ABRB. This is due to the utilization of expert knowledge in ABRB.

## 5.4. Extension of ABRB model

In the long-term operation of LPB, the current collector gradually melts, and the electrolyte may gradually be decomposed. The changes of the above inner properties lead to the change of heating rate in the charging stage. In view of this, Heating rate should be considered to es timate the capacity of LPB. Three referential points are set to describe the heating rate: Low (L), Middle (M) and High (H). The referential values are given as Table 8.

Due to the negative correlation between Heating rate and LPB ca pacity, the newly added initial rules can be given as Table 9. Moreover, the independency factors are updated as

$$
\boldsymbol {\varphi} = \left[ \begin{array}{c c c} - & \varphi_ {1, 2} & \varphi_ {1, 3} \\ \varphi_ {2, 1} & - & \varphi_ {2, 3} \\ \varphi_ {3, 1} & \varphi_ {3, 2} & - \end{array} \right] = \left[ \begin{array}{c c c} - & 0. 6 4 3 & 0. 6 5 6 \\ 0. 6 3 5 & - & 0. 6 5 7 \\ 0. 6 6 5 & 0. 6 7 4 & - \end{array} \right]\tag{28}
$$

In ABRB, the newly added rules can be optimized separately by using P-CMA-ES. The optimized rules are shown in Table 10. Based on the extended rule base (shown in Table 5 and 10), the MSE is 1.01E-4, which is improved.

Suppose that a new referential point of the capacity of LPB should be added, which is used to illustrate the complete failure (CF) of LPB. Thus, the identification framework of ABRB should be extended to $\{ C S , S , L B ,$ $V B , C F \}$ . Due to the similarity of the internal states of LPB when it is in VB and $\mathrm { C F } ,$ the belief degree to CF may be assigned to VB in the original FoD. In view of this, the corresponding belief degrees should be reas signed by using Eqs. (22-a)-(d), where the probabilities are given by experts as shown in Table 11. Finally, the extended ABRB is shown as Table $^ { 1 2 , }$ and the outputs are shown in Fig. 6. It can be seen that the extended FoD provides a more practical description for the health state of LPB, which is beneficial to detecting the potential risks early.

However, the MSE calculated by the outputs of extended ABRB is 2.6E-4, which is larger than the optimized ABRB but smaller than the initial ABRB. This is because that the above extension of the ABRB model is a secondary process, which brings some errors to the model. Thus, the above extension method is efficient within a limited scope. When it is used in a complex extension problem, the optimization by using a small number of data samples is necessary to eliminate the extra errors. The extension in complex situations should be further studied in the future.

## 5.5. Summary of the interpretability of ABRB model

The interpretability of the ABRB model is reflected in the following aspects:

1) The establishment of ABRB. It can be seen from Subsection 5.1 that ABRB can be established more compactly due to the simple form of ABR. In modelling the complex system with a large number of in dicators, the experts are more efficient to intuitively determine the relationship between one attribute and the consequence. The ABRB model provides a more effective framework for the introduction of expert knowledge.

2) The optimization of ABRB. A compact ABRB model means that fewer parameters are optimized. Besides, the effective introduction of expert knowledge guarantees the accuracy of the initial parame ters. The constraint shown in Eq. (26) is used to maintain the meaning of parameters in the optimization process. For example, the optimized belief distributions shown in Fig. 3 are consistent with common sense and the initial judgement from experts. The above measures also reduce the dependence on the data samples in optimization.

3) The extension of ABRB. Due to the simpler form of ABRs, the ABRB model has a better extendability. The new knowledge accumulated in practice can be well supplied into the ABRB model. This is the key to ensure the effectiveness (accuracy and interpretability) of ABRB model in the long-term practice.

4) The outputs of ABRB. An important advantage of the ABRB with interpretability is that it can provide more information than the black-box model. For example, ABRB can give the result in a belief distribution form while the BPNN and SVM cannot. The above three aspects are the guarantee of the effectiveness and reliability of model outputs, which are also conductive to the analysis of model outputs. In this case, the transition of LPB health state can be presented by the transition of the belief distributions shown in Figs. 4 and 6.

For further analysis, the slopes of the belief degree to each health state and the sum of their absolute values are shown in Fig. 7. The slope reflects the direction of state transition. In the preliminary stage of ca pacity fading, the belief degrees fluctuate between the first two states. This is consistent with the fluctuation of the capacity shown in Fig. 5. The sum of the absolute values of slopes can reflect the intensity of state transition. In engineering practice, without considering the testing error, the reversible capacity loss caused by the side reaction in LPB may be an important reason for the change of the intensity. As shown in Fig. 7, the intensity in the preliminary stage is higher than in the last stage. It in dicates that the side reaction may be more active in the preliminary stage.

It should be noted that the further verification of the above analysis requires more experiments. However, it is acceptable that, as a grey-box model, the description and reasoning of ABRB is more transparent. The outputs of ABRB are more reliable and interpretable, which can present more information about the real system. This is conductive to the de cision making by using the model output in applications.

## 6. Conclusion

The rule explosion and weak extendability problem of the original BRB model lead to the difficulty in introducing expert knowledge. It may undermine the interpretability of BRB. Aiming at these problems, a new ABRB expert system is developed in this paper. The main contributions are: 1) The approximation belief rule is proposed, in which the corre lation between two attributes is handled by the discounted weight. By using these rules, an ABRB model can be established compactly, and has a better extendability; 2) The universal approximation ability of the ABRB model is proved; 3) A new extension method is proposed to extend the key components of the ABRB model.

Designing and maintaining the expert system in a changing engi neering practice requires a rethinking of how systems provide value to stakeholders over time. Developing an expert system with good inter pretability and extendability is a key approach to promoting value sustainment. This paper provides a new idea for constructing the largescale BRB expert system with good interpretability and extendability in the future. However, this paper still has some limitations. One is that more technologies about the method to reduce the attribute correlation should be investigated and analyzed. Another is that the extension of ABRB in complex situations should be further studied. A general extension approach is desirable in the future.

## Acknowledgment

This work was supported in part by the Natural Science Foundation of China under Grants 61773388, 61751304, and 61833016, the Shaanxi Outstanding Youth Science Foundation under Grant 2020JC-34.

## References

[1] J.B. Yang, J. Liu, J. Wang, H.S. Sii, H.W. Wang, Belief rule-base inference methodology using the evidential reasoning approach-RIMER, IEEE Trans. Syst. Man Cyber.: Syst. 36 (2006) 266–285.

[2] Y.W. Chen, J.B. Yang, D.L. Xu, et al., On the inference and approximation properties of belief rule-based systems, Inf. Sci. 234 (2013) 121–135.

[3] Z.J. Zhou, C.H. Hu, J.B. Yang, et al., Online updating belief-rule-based system using the RIMER approach, IEEE Trans. Syst. Man Cybern.: Syst. 41 (2011) 1225–1243.

[4] Z.J. Zhou, C.H. Hu, J.B. Yang, et al., A sequential learning algorithm for online constructing belief-rule-based systems, Expert Syst. Appl. 37 (2010) 1790–1799

[5] Z.J. Zhou, C.H. Hu, G.Y. Hu, et al., Hidden behavior prediction of complex systems under testing influence based on semi-quantitative information and belief rule base, JEEE Trans, Fuzzy Syst. 23 (2015) 2371–2386.

[6] Z.J. Zhou, C.H. Hu, B.C. Zhang, D.L. Xu, Y.W. Chen, Hidden behavior prediction of complex systems based on hybrid information, IEEE Trans. Cybern. 43 (2013) 402–411.

[7] Z.J. Zhou, G.Y. Hu, B.C. Zhang, C.H. Hu, Z.J. Zhou, P.L. Qiao, A model for hidden behavior prediction of complex systems based on belief Rule Base and power set, IEEE Trans. Syst. Man Cybern.: Syst. 37 (2017) 1–7.

[8] Y. Cao, Y.J. Wei, G.Y. Hu, et al., BRB fault diagnosis model based on fault tree analysis, Chin. Auto. Congr. (2018) 783–787, https://doi.org/10.1109/ CAC.2018.8623670.

[9] Z.C. Feng, Z.J. Zhou, C.H. Hu, et al., A new belief rule base model with attribute reliability, IEEE Trans. Fuzzy Syst. 27 (2019) 903–916.

[10] L.L. Chang, Z.J. Zhou, et al., Belief rule based expert system for classification problems with new rule activation and weight calculation procedures, Inf. Sci. 336 (2015) 75–91.

[11] L.L. Chang, Z.J. Zhou, H.C. Liao, Generic disjunctive belief-rule-base modeling inferencing, and optimization, IEEE Trans. Fuzzy Syst. 27 (2019) 1866–1880.

[12] L.L. Chang, Y.W. Chen, Z. Hao, et al., Indirect disjunctive belief rule base modeling using limited conjunctive rules: two possible means, Int. J. Approx. Reason. (2019) 1-20.

[13] G. Beliakov, J. Warren, Appropriate choice of aggregation operators in fuzzy decision support systems. JEEE Trans. Fuzzy Syst, 9 (2001) 773–784.

[14] A.M. Ross, D.H. Rhodes, D.E. Hastings, et al., Defining changeability: reconciling flexibility, adaptability, scalability, modifiability, and robustness for maintaining system life cycle value, Syst. Eng. 11 (2008) 246–262.

[15] L.L. Chang, Z.J. Zhou, Y.W. Chen, Belief rule base structure and parameter joint optimization under disjunctive assumption for nonlinear complex system modeling, IEEE Trans. Syst. Man Cybern. Syst. 48 (2018) 1542–1554.

[16] L.L. Chang, L. Wang, Akaike information criterion-based objective for belief rule base optimization, in: International Conference on Intelligent Human-machine Systems & Cybernetics, 2016.

[17] Y. Chen, X. Xu, et al., A data-driven approximate causal inference model using the evidential reasoning rule. Knowl.-Based Syst. (2015) 264–272.

[18] J.H. Kim, J. Pearl, A computational model for combined causal and diagnostic reasoning in inference systems, in: Proceedings of the Eighth International Joint Conference on Artificial Intelligence. Germany. 1983. pp. 380–385

[19] J. Pearl, Causality: Models, Reasoning, and Inference, Cambridge University Press, Cambridge, 2000.

[20] D. Tang, J.B. Yang, K.S. Chin, Z.S.Y. Wong, X. Liu, A methodology to generate a belief rule base for customer perception risk analysis in new product development, Expert Syst. Appl. 38 (2011) 5373–5383.

[21] E. Hisdal, Logical Structures for Representation of Knowledge and Uncertainty, Physica-Verlag, Hiedelbery, Germany, 1998

[22] Z.G. Liu, Q. Pan, J. Dezert, G. Mercier, Hybrid classification system for uncertain data, JEEE Trans, Syst. Man Cybern.: Syst. 47 (2016) 2783–2790

[23] Z.J. Zhou, C.H. Hu, J.B. Yang, D.L. Xu, Online updating belief rule based system for pipeline leak detection under expert intervention, Expert Syst. Appl. 36 (2009) 7700–7709.

[24] Z.C. Feng, Z.J. Zhou, C.H. Hu, et al., Fault diagnosis based on belief rule base with considering attribute correlation, IEEE Access (2018) 2055–2067.

[25] G.L. Li, Z.J. Zhou, C.H. Hu, et al., An optimal safety assessment model for complex systems considering correlation and redundancy, Int. J. Approx. Reason. (2019) 38–56.

[26] X.F. Xu, R.B. Xiao, An approach of eliminating correlation of assessment-index, Syst. Eng.-Theory Pract. 22 (2002) 1–5.

[27] R. Jirouˇsek, P.P. Shenoy, A new definition of entropy of belief functions in the Dempster–Shafer theory, Int. J. Approx. Reason. 92 (2017) 49–65.

[28] Y. Wu, J. Yang, et al., On the evidence inference theory, Inf. Sci. 89 (1996) 245–260.

[29] Z. J. Zhou, S. W. Tang, C. H. Hu, Y. Cao, J. Wang, Evidential reasoning theory and its applications, Acta Automat. Sin., DOI: 10.16383/j.aas.c190676.

[30] S. W. Tang, Z. J. Zhou, C. H. Hu, J. B. Yang, Y Cao, Perturbation analysis of evidential reasoning rule, IEEE Trans. Syst. Man Cybern.: Syst.. DOI: https://doi. org/10.1109/TSMC.2019.2944640.

[31] K.S. Chin, Y.M. Wang, K.K. Poon, J.B. Yang, Failure mode and effects analysis by data envelopment analysis, Decis, Support. Syst, 48 (2009) 246–256

[32] D.L. Xu, G. McCarthy, J.B. Yang, Intelligent decision system and its application in business innovation self-assessment. Decis, Support, Syst, 42 (2006) 664–673.

[33] D.N. Reshef, Y.A. Reshef, H.K. Finucane, S.R. Grossman, G. McVean, P. J. Turnbaugh. E.S. Lander. M. Mitzenmacher. P.C. Sabeti. Detecting novel associations in large data sets, Science 334 (2011) 1518–1524.

[34] H.C. Peng, C. Ding, Minimum redundancy feature selection from microarray gene

[35] Y. Cao, Z. J. Zhou, C. H. Hu, W. He, S. W. Tang, On the interpretability of belief rule based expert systems, JEEE Trans. Fuzzy Syst., DOI: https://doi,org/10.1109 /TFUZZ,2020.3024024

[36] Z. J. Zhou, Y. Cao, G. Y. Hu, Y. M. Zhang, S. W. Tang, Y. Chen, New health-state assessment model based on belief rule base with interpretability. Sci. China Inf. Sci., DOI: https://doi.org/10.1007/s11432-020-3001-7.

[37] Y.Z. Lu, M.Q. Xiao, X.L. Tang, SOC estimation of lithium battery based on belief rule base, J. Air Force Eng, Univ, 20 (2019) 39–45

[38] H.Z. Zhu, M.Q. Xiao, J.F. Li, Battery status estimation using extended belief rule base with novel rule reduction method, J. Phys. Conf. Ser. 1507 (2020) 8–24.

[39] V. Ramadesigan, K. Chen, N.A. Burns, Parameter estimation and capacity fade analysis of lithium-ion batteries using reformulated models. J. Electrochem. Soc. 158 (2011) 1048–1054.

[40] D.L. Xu, J. Liu, J.B. Yang, G.P. Liu, J. Wang, I. Jenkinson, J. Ren, Inference and learning methodology of belief-rule-based expert system for pipeline leak detection, Expert Syst. Appl. 32 (2007) 103–113.

You Cao received the B.Eng. degree in control science and management from the Harbin University of Science and Technology, Harbin, China, in 2017. He is currently pursuing the doctor’s degree in High-Tech Institute of Xi’an, China. His research interests include belief rule base, deep learning, safety assessment, fault prognosis and optimal maintenance of dynamic systems.

Zhijie Zhou received the B.Eng. and M.Eng. degrees from the Rocket Force University of Engineering, Xi’an, China, in 2001 and 2004, respectively, and the Ph.D. degree from

Tsinghua University, Beijing, China, in 2010, all in control science and management. He is currently an Professor with the High-Tech Institute of Xi’an. His research interests includ belief rule base, and fault prognosis.

Changhua Hu received the B.Eng. and M.Eng. degrees from the Rocket Force University of Engineering, Xi’an, China, in 1987 and 1990, respectively, and the Ph.D. degree from North Western Polytechnic University, Xi’an, in 1996, all in control science and man agement. He is currently a Professor with the High-Tech Institute of Xi’an. His current research interests include fault diagnosis and prediction, life prognosis.

Shuaiwen Tang received the B.Eng. degree in control science and management from the High-Tech Institute of Xi’an, Xi’an, China, in 2017, where he is currently pursuing the doctor’s degree. His research interests include evidential reasoning, information fusion, safety assessment, fault prognosis and optimal maintenance of dynamic systems.

Jie Wang received the B.Eng. degree from the Hefei University of Technology, Hefei, China, in 2018, where he is currently pursuing the doctor’s degree. His research interest covers evidential reasoning, reliability, fault prognosis, performance analysis, and safety assessment.
