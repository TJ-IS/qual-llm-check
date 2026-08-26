---
otero_id: 16224
otero_key: "KQHM5UHM"
title: "A new approach to classification based on association rule mining"
authors: "Guoqing Chen; Hongyan Liu; Lan Yu; Qiang Wei; Xing Zhang"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.03.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A new approach to classification based on association rule mining

Guoqing Chen <sup>\*</sup>, Hongyan Liu, Lan Yu, Qiang Wei, Xing Zhang

Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, Beijing 100084, China

Received 19 February 2004; received in revised form 9 March 2005; accepted 9 March 2005 Available online 25 July 2005

## Abstract

Classification is one of the key issues in the fields of decision sciences and knowledge discovery. This paper presents a new approach for constructing a classifier, based on an extended association rule mining technique in the context of classification. The characteristic of this approach is threefold: first, applying the information gain measure to the generation of candidate itemsets; second, integrating the process of frequent itemsets generation with the process of rule generation; third, incorporating strategies for avoiding rule redundancy and conflicts into the mining process. The corresponding mining algorithm proposed, namely GARC (Gain based Association Rule Classification), produces a classifier with satisfactory classification accuracy, compared with other classifiers (e.g., C4.5, CBA, SVM, NN). Moreover, in terms of association rule based classification, GARC could filter out many candidate itemsets in the generation process, resulting in a much smaller set of rules than that of CBA. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Data mining; Association rule; Classification; Information gain

## 1. Introduction

Classification is one of the key issues in the field of decision sciences, a field which plays an important role in supporting business and scientific decision-making. In recent years, it has also been one of the focal points in data mining and knowledge discovery. Classification is finding a classifier that results from training datasets with predetermined targets, fine-tuning it with test datasets, and using it to classify other datasets of interest. There exists various ways of constructing classifiers in the form of, for example, rules, decision trees, Bayesian networks, support vectors machine, etc. [12,14–16,21,24,26,29–31]. Decision trees classifiers, such as Quinlan’s C4.5/5.0 classifier and its extensions [30], have received considerable attention due to its speed and understandability. Moreover, a number of efforts have been put forward to focus on the various aspects of improvements [5,9,25,33]. Another type of classification technique that has attracted an increasing number of attempts in recent years is finding classification rules based on association rule mining techniques, e.g., Refs. [4,20–23,29].

A classification rule is of the form X Z C, where X is a set of data items, and C is a class (label) and a predetermined target. With such a rule, a transaction or data record t in a given database could be classified into class C if t contains X. Apparently, a classification rule could be regarded as an association rule of a special kind.

Roughly speaking, an association rule is a relationship between data items. Two measures, namely the Degree of Support $( D _ { \mathrm { s u p p } } )$ and the Degree of Confidence $( D _ { \mathrm { c o n f } } )$ , are used to define a rule. For example, a rule like <sup>b</sup>Milk Z Diaper with $D _ { \mathrm { s u p p } } { = } 2 0 \% , \ D _ { \mathrm { c o n f } } { = }$ $8 0 \%$ means that <sup>b</sup>20% of the customers bought both Milk and Diaper<sup>Q</sup> and that <sup>b</sup>80% of the customers who bought Milk also bought Diaper<sup>Q</sup>. That is, $D _ { \mathrm { s u p p } }$ corresponds to statistical significance, while $D _ { \mathrm { c o n f } }$ is a measure of the rule’s strength [3].

Formally, let $I = \{ I _ { i } , i { = } 1 , . . . , s \}$ be a set of items. A transaction database T is a set of transactions, where each transaction t is a set of items such that $t \subseteq I .$ An association rule is of the form $X { \Rightarrow } Y ,$ where $X \subset I , \quad Y \subset I$ are called itemsets, and $X \cap Y = \emptyset .$ A transaction t is called to contain X, if $X \subseteq t .$ . Let $D _ { \mathrm { s u p p } } ( X )$ be the fraction of transactions that contain X in a database T, $D _ { \mathrm { s u p p } } ( X ) { = } { \| } X { \| } / { | } T$ The degree of support and degree of confidence for a rule $X { \Rightarrow } Y$ are defined as follows:

$$
D _ {\mathrm{supp}} (X \Rightarrow Y) = \| X \cup Y \| / | T |
$$

$$
D _ {\text { conf }} (X \Rightarrow Y) = \| X \cup Y \| / \| X \|
$$

where X and Y are itemsets with $X \cap Y { = } \emptyset , T$ is the set of all the transactions contained in the database concerned, ||X|| is the number of the transactions in T that contain $X , \| X \cup Y \|$ is the number of the transactions in T that contain X and Y, and |T| is the number of the transactions in T. In other words, $D _ { \mathrm { s u p p } } ( X { \Rightarrow } Y )$ is the percentage of transactions containing both X and Y in the whole dataset, while $D _ { \mathrm { c o n f } } ( X { \Rightarrow } Y )$ is the ratio of the number of transactions that contain X and Y over the number of transactions that contain X. They are used to evaluate a rule against given thresholds, minimal support a and minimal confidence $\beta ,$ respectively. In particular, if $D _ { \mathrm { s u p p } }$ of an itemset X is no less than a $( \mathrm { i . e . , } D _ { \mathrm { s u p p } } ( X ) \geq \alpha )$ , then X is called a frequent itemset, otherwise called an excluded itemset. There have been many efforts proposed to discover association rules in various ways [1,2,8,11–13,17,28,32,34,37], among which the Apriori algorithm by Agrawal and Srikant [1] is usually deemed as a classical algorithm.

In the classification based on association rules mining, a well-known method, namely the CBA method proposed by Liu et al. [21] and its modifications [20,23], uses an Apriori-type association rule mining approach [1] to generate classification rules, which usually generates all the frequent itemsets, followed by the rule generation process. Subsequently, filters may be applied to the rules so as to eliminate non-interesting ones such as conflicts and so on. In other words, basically, CBA directly employs the Apriori-type approach for a particular kind of association rule, namely classification rules in forms of $X { \Rightarrow } C$ . Thus, its efficiency heavily relies on the process of generating frequent itemsets. Like conventional association rules, classification rules are generated based on all the frequent itemsets generated. Then these rules are sorted according to a filtering measure, if desired.

While classifiers in forms of rules are often appealing for use and explanation by decision makers, directly applying the Apriori-type approach may however result in a large number of itemsets and then of rules, which would further increase the effort for understanding the rules as well as for resolving rule redundancy and conflicts. Therefore, it is considered desirable if some strategies such as itemset reduction and redundancy/conflict resolutions could be incorporated into the process of frequent itemsets generation, such that fewer itemsets need to be generated and therefore with fewer resultant rules. Apparently, a smaller set of classification rules is often preferable than a larger set at the same level of accuracy in terms of rule understandability.

Moreover, in the process of frequent itemsets generation, the Apriori-type method usually considers all the combinations of items in candidate itemsets. With massive datasets, the number of these combinations is generally very large. In fact, different items in these combinations may play different roles in measuring the degrees of support and degrees of confidence. Therefore, it is deemed desirable if only a part of the items (e.g., those <sup>b</sup>informative<sup>Q</sup> ones) in candidate itemsets need to be considered in generating frequent itemsets.

This paper addresses some of the above-mentioned issues and presents a new approach for constructing a classifier, based on an extended association rule mining technique in the context of classification. Section 2 describes the issues of concern along with the notion of information gain to be used in the mining process to reduce the number of candidate itemsets, as well as with the notions and certain related properties of rule redundancy and conflicts. In Section 3, the new mining algorithm called GARC (Gain based Association Rule Classification) is presented, which combines the processes of frequent itemsets generation and rule generation, where the measures for redundancy and conflicts avoidance and information gain are incorporated. Finally, results and respective analyses of data experiments are provided in Section 4.

## 2. Classification rules

## 2.1. Basic notions

As mentioned previously, the classification rules mining problem can be regarded as a special case of the association rules mining problem [21,22,27]. The task of classification is to find a set of rules so as to identify the classes of undetermined transactions. In classification, a classifier is usually built based upon a dataset that is divided into two groups: one is for training, and the other for testing, each consisting of data items and class labels. In terms of association rules, these class labels are special cases of items. For the sake of clarity, we hereafter refer to them separately, otherwise indicated where necessary.

Let T be the dataset with each transaction composed of a number of distinctive items in the set of all items I and a class label in $G = \{ C _ { I } , C _ { 2 } , \dots , C _ { g } \}$ , X be a subset of $I \ ( { \mathrm { i . e . , } } X \subseteq I )$ , and $C _ { k }$ be a class label in $G ( k = 1$ $2 , . . . , g )$ . Notably, in classification-oriented association rule mining, only those rules each with one single class label as its consequent need to be considered; therefore in this paper, each itemset (such as $X C _ { k } )$ is used to represent a rule (such as $X { \Rightarrow } C _ { k } )$ identically. In other words, itemset $X C _ { k }$ corresponds to rule $X { \Rightarrow } C _ { k }$ , with $D _ { \mathrm { s u p p } } ( X C _ { k } ) { = } | | X C _ { k } | | / | T$ and $D _ { \mathrm { c o n f } } ( X C _ { k } ) { = } { | | X C _ { k } | | } /$ ||X||. A transaction t in T is called to contain X if $t \supseteq X . X C _ { k }$ is called to be a p-itemset, if X contains $p$ items. If $D _ { \mathrm { s u p p } } ( X C _ { k } ) \geq \alpha$ , then $X C _ { k }$ is called a frequent itemset. Furthermore, if $D _ { \mathrm { c o n f } } ( X C _ { k } ) \ge \beta$ , then $X C _ { k }$ is called a qualified itemset, and can be used to produce a classification rule such as $X { \Rightarrow } C _ { k }$ . For a rule $X { \Rightarrow } C _ { k } ,$ sometimes $X$ is referred to as the antecedent of the rule and $C _ { k }$ as the consequent of the rule. Moreover, for the sake of convenience, two parameters namely lcount and wcount are sometimes used to denote ||X|| and $| | X C _ { k } | |$ , as the number of transactions containing X and the number of transactions containing $X C _ { k } ,$ respectively. Thus, mining classification rules is used to discover such qualified association rules as $X { \Rightarrow } C _ { k }$ for $k = 1 , 2 , . . . , g$

## 2.2. Information gain

Information gain is one of the measures used to select best split attributes in decision tree classifiers [7,35]. In this paper, it could also be used as a measure to reduce the number of itemsets. In the process of frequent itemsets generation, instead of considering all the combinations of items in candidate itemsets in the Apriori-type method, information gain measure will be used to select the best attribute. In this way, only those items containing the best item with maximum information gain need to be selected to further generate candidate itemsets.

Suppose an attribute A has n distinct values that partition the training dataset T into subsets $T _ { I } , T _ { 2 } , . . . ,$ $T _ { n }$ . For a dataset $S \subseteq T ,$ $\operatorname { f r e q } ( C _ { k } , \ S )$ represents the number of transactions in S that belong to class $C _ { k }$ Then info(S) is defined as follows to measure the average amount of information needed to identify the class of a transaction in S:

$$
\operatorname{info} (S) = - \sum_ {k = 1} ^ {g} \frac {\operatorname{freq} \left(C _ {k} , S\right)}{| S |} \times \log_ {2} \left(\frac {\operatorname{freq} \left(C _ {k} , S\right)}{| S |}\right)
$$

where $| S |$ is the number of transactions in S and g is the number of classes.

After the dataset T is partitioned in accordance with n values of attribute A, the expected information requirement could be defined as:

$$
\operatorname{info} _ {A} (T) = \sum_ {i = 1} ^ {n} \frac {\left| T _ {i} \right|}{\left| T \right|} \times \operatorname{info} \left(T _ {i}\right)
$$

The information gained by partitioning T according to attribute $A$ is defined as:

$$
\operatorname{gain} (A) = \operatorname{info} (T) - \operatorname{info} _ {A} (T)
$$

Among all attributes in dataset $T ,$ the best split attribute is the one that maximizes the information gain.

## 2.3. Rule redundancy and conflicts

Though classification rules can be discovered using Apriori-type association rule mining techniques directly, the whole set of classification rules $( \mathrm { i . e . } ,$ , rules satisfying a and $\beta )$ might be poor in quality. First, the number of classification rules may be too large to easily construct classifiers. More seriously, from the viewpoint of classification, there may exist conflicting rules $( { \mathrm { e . g . } } , X { \mathrm { = } } C _ { i }$ and $X { \Rightarrow } C _ { j } )$ and redundant rules $( { \mathrm { e . g . } } , \ X { \Rightarrow } C _ { i }$ and $X Y { \Rightarrow } C _ { i }$ , with $D _ { \mathrm { c o n f } } ( X { \Rightarrow } C _ { i } ) { \geq } D _ { \mathrm { c o n f } } ( X Y { \Rightarrow } C _ { i } ) )$ . The conflicting rules will lead to identifying a transaction into two classes, while the redundancy will result in a rule like $X Y { \Rightarrow } C _ { i }$ that is semantically meaningless for classification (given $X { \Rightarrow } C _ { i } )$

Definition 2.1. Rule r is called to precede rule $r ^ { \prime }$ if either $D _ { \mathrm { c o n f } } ( r ) { > } D _ { \mathrm { c o n f } } ( r ^ { \prime } )$ , or $D _ { \mathrm { c o n f } } ( r ) { = } D _ { \mathrm { c o n f } } ( r ^ { \prime } )$ and $D _ { \mathrm { s u p p } } ( r ) { > } D _ { \mathrm { s u p p } } ( r ^ { \prime } )$

Definition 2.2. Let $\psi$ be a set of discovered classification rules. Then rule $Z { \Rightarrow } C _ { i }$ in W is called redundant if there already exists a rule $X { \Rightarrow } C _ { i }$ in $\psi$ such that $Z \supset X$ . Moreover, for $i { \neq } j ,$ , rules $Z { \Rightarrow } C _ { j }$ and $X { \Rightarrow } C _ { i }$ in W are called conflicting if there already exists a rule $X { \Rightarrow } C _ { i }$ in W such that either $Z { = } X ,$ or $Z \supset X$ and $Z { \Rightarrow } C _ { j }$ does not precede $X { \Rightarrow } C _ { i }$

Apparently, coping with such rule redundancy and conflicts is desirable because otherwise (1) a transaction containing X may be classified into two classes $( \mathrm { e . g . , } C _ { i }$ and $C _ { j } ) , ( 2 )$ a rule $( \mathrm { e . g . , } X Y { \Rightarrow } C _ { i } )$ may not be regarded useful (i.e., redundant) for identifying a transaction due to the existence of another rule $( \mathrm { e . g . }$ $X { \Rightarrow } C _ { i } )$ , and (3) a transaction containing $X Y$ may be classified into two classes $( \mathrm { e . g . , } C _ { i }$ and $C _ { j } ) _ { : }$ or $X Y { \Rightarrow } C _ { j }$ is not significant enough to be used, compared with $X { \Rightarrow } C _ { i }$ . It is worth mentioning, however, that these notions of redundancy and conflict are particularly relevant for classification and may not be of concern for association rules in general.

Usually, given a (nonempty) set $\psi$ of discovered classification rules, i.e., $\psi = \{ r | r$ is a classification rule, $D _ { \mathrm { s u p p } } ( r ) { \geq } \alpha$ and $D _ { \mathrm { c o n f } } ( r ) { \geq } \beta \}$ , filters can be built to deal with the redundancy and conflicts. It can be seen that for any nonempty $\psi$ there exists a corresponding nonempty set $\psi _ { \mathrm { ~ c ~ } }$ of rules with such redundancy and conflicts removed. $\psi _ { \mathrm { ~ c ~ } }$ is referred to as a compact set of W. A constructive way to obtain $\psi _ { \mathrm { ~ c ~ } }$ is a repetitive resolution procedure as follows: First set $\psi _ { \mathrm { c } } = \Psi$ , then repeat the following steps until no further changes are made for $\psi _ { \mathrm { ~ c ~ } }$

(i) check each rule $X Y { \Rightarrow } C _ { i }$ in $\Psi _ { \mathrm { c } } ,$ if there exists a rule $X { \Rightarrow } C _ { i }$ in $\psi _ { \mathrm { { c } } }$ then delete $X Y { \Rightarrow } C _ { i }$ . That is, $\boldsymbol { \Psi } _ { \mathrm { c } } { = } \boldsymbol { \Psi } _ { \mathrm { c } } - \{ X Y { \Rightarrow } C _ { i } \}$

(ii) check each rule $X { \Rightarrow } C _ { i }$ $\psi _ { \mathrm { c } } ,$ if there exists a rule $X { \Rightarrow } C _ { j }$ in $\psi _ { \mathrm { ~ c ~ } }$ that does not precede $X { \Rightarrow } C _ { i } ,$ then delete $X { \Rightarrow } C _ { j }$ . That is, $\boldsymbol { \varPsi } _ { \mathrm { c } } { = \boldsymbol { \Psi } _ { \mathrm { c } } - \{ X { \Rightarrow } C _ { j } \} }$

(iii) check each rule $X Y { \Rightarrow } C _ { j }$ in $\psi _ { \mathrm { c } } ,$ if there exists a rule $X { \Rightarrow } C _ { i }$ in $\psi _ { \mathrm { ~ c ~ } }$ that precedes it, then delete $X Y { \Rightarrow } C _ { j }$ . That is, $\boldsymbol { \varPsi } _ { \mathrm { c } } { = \boldsymbol { \Psi } _ { \mathrm { c } } - \{ X Y \Rightarrow C _ { j } \} }$

Obviously, $\psi _ { \mathrm { ~ c ~ } }$ is nonempty if W is nonempty. Moreover, $\psi _ { \mathrm { ~ c ~ } }$ is not unique, depending on the order in which the above three steps are performed. Notably, in this paper, our primary attention is not paid to developing a separate filter to derive $\psi _ { \mathrm { ~ c ~ } }$ from $\Psi ,$ but to exploring certain ways to avoid rule conflicts and redundancy, which could be incorporated in the integrated mining process.

## 2.4. Strategies in avoiding rule conflicts and redundancy

When the strategies are incorporated into the process of generating $\Psi _ { \pmb { i } }$ , the rules in $\psi$ will be free of redundancy and conflict. More importantly, these strategies will help identify excluded (i.e., not frequent) itemsets inside the process of candidate itemsets generation, resulting in fewer itemsets to be generated.

With regard to the redundancy stated in Definition 2.2, the strategy that could be applied is that, if $X { \Rightarrow } C _ { i }$ holds, then any candidate itemset containing $X C _ { i }$ need not to be produced, because any such itemsets as $X Y C _ { i } \ ( \mathrm { i . e . , } \ Z { = } X Y )$ would not be regarded semantically necessary from the perspective of classification. In other words, if $X { \Rightarrow } C _ { i }$ holds, it means that any transaction containing X will be classified into class $C _ { i } ,$ , including any transaction containing XY. Note that the number of candidate itemsets to generate is reduced.

Next, consider rule conflicts for $Z = X$ in Definition 2.2. The following theorem indicates that it can simply be avoided if the pre-specified minimal confidence $\beta$ is set to be over 0.5, which is regarded reasonable in many real applications.

Theorem 2.1. If $\beta > 5 0 \%$ then rules $X { \Rightarrow } C _ { i }$ and $X { \Rightarrow } C _ { j }$ will not hold in T simultaneously.

Proof. Without loss of generality, assume that $X { \Rightarrow } C _ { i }$ holds in T with $D _ { \mathrm { c o n f } } ( X { \Rightarrow } C _ { i } ) { \geq } \beta { > } 5 0 \%$ . For $g \ge 2$ since $\textstyle | X \| = \| X C _ { i } \| + \sum _ { i = 1 } ^ { g } \| X C _ { j } \|$ ; and ${ \frac { \| X \| } { \| X \| } } = { \frac { \| X C _ { i } \| } { \| X \| } } +$ $\sum _ { \stackrel { j = 1 } { j \neq i } } ^ { g } { \frac { \| X C _ { j } \| } { \| X \| } }$ , then jpi

$$
\sum_{\substack{j = 1\\ j\neq i}}^{g}\frac{\|XC_{j}\|}{\|X\|} = 1 - D_{\text{conf}}(X\Rightarrow C_{i}).
$$

From ${ \frac { \parallel X C _ { j } \parallel } { \parallel X \parallel } } \geq 0 .$ , for $\mathbf { j } = 1 , \quad 2 , . . . , g .$ we have $\begin{array} { r } { \frac { \parallel X C _ { j } \parallel } { \parallel X \parallel } { \leq } 1 \stackrel { \parallel ^ { \perp } } { - } D c o n f ( X {  } \bar { C _ { i } } ) { < } 5 0 \% < \beta , } \end{array}$ , which means that $X { \Rightarrow } C _ { j }$ does not hold in T. 5

In other words, if both $X { \Rightarrow } C _ { i }$ and $X { \Rightarrow } C _ { j }$ hold simultaneously, both of them must involve two mutually disjoint sets of transactions (denoted as $T _ { X C _ { i } }$ and $T _ { X C _ { i } } )$ containing $X C _ { i }$ and $X C _ { j }$ respectively. Otherwise, if a transaction t is involved in generating both rules, we will have $X C _ { i } C _ { j } \subseteq t _ { : }$ , which is a contradiction to the structure of t, for t contains only a single class label of $\mathrm { G } { = } \{ C _ { I } , C _ { 2 } , . . . . , C _ { g } \}$ . That is, $T _ { X C _ { i } } \cap$ $T _ { X C _ { i } } { = } { \cal { O } } .$ Since these two sets are the subsets of $T _ { X }$ (where $T _ { X }$ is the set of transactions containing X), we have $| T _ { X C _ { i } } | / | T _ { X } | + | T _ { X C _ { i } } | / | T _ { X } | \le | T _ { X } | / | T _ { X } | = 1$ . Semantically, the following relationship exists: $\| X _ { C _ { i } } \| /$ $| | X | | + | | X _ { C _ { i } } | | / | | X | | \leq | | X | | / | | X | | = 1$ which means that $D _ { \mathrm { c o n f } } ( X { \xrightarrow { \prime } } C _ { i } ) + D _ { \mathrm { c o n f } } ( X { \xrightarrow { } } C _ { j } ) \leq 1$ . Apparently, however, this is a contradiction to the supposition that $D _ { \mathrm { c o n f } } ( X { \Rightarrow } C _ { j } ) { \leq } \beta { > } 0 . 5$ and $D _ { \mathrm { c o n f } } ( X { \Rightarrow } C _ { i } ) \geq \beta > 0 . 5 .$ In brief, the strategy to set $\beta$ to be over 0.5 will prevent the rule conflict from happening.

In addition, the following theorem can be used to further reduce the number of candidate itemsets. This also corresponds to rule conflicts stated in Definition 2.2. It will be proved in Theorem 2.2 that, if $X { \Rightarrow } C _ { i }$ holds in T and if $D _ { \mathrm { c o n f } } ( X { \Rightarrow } C _ { i } ) { > } 1 - \alpha$ or $D _ { \mathrm { s u p p } } ( X ) { < } 2 \alpha$ , then $X Y { \Rightarrow } C _ { j }$ does not hold in T.

Theorem 2.2. Suppose rule $X { \Rightarrow } C _ { i }$ holds in T, (1) if $I - D _ { c o n f } ( X ^ { \Rightarrow } C _ { i } ) < \alpha ,$ then any itemset like $X Y C _ { j }$ is an excluded itemset; (2) $i f \left| \left| X \right| \right| < 2 \left| T \right| \alpha ,$ then any itemset like $X Y C _ { j }$ is an excluded itemset; where $Y \cap X = \emptyset ,$ $Y \cap C _ { k } = \emptyset , k { = } I , \ 2 , . \ . \ . , g ,$ , and $g \ge 2$

Proof. (1) Since $\begin{array} { r } { \| X \| { = } \| X C _ { i } \| { + } \textstyle \sum _ { j = 1 } g _ { 1 } \| X C _ { j } } \end{array}$ <sub>O</sub>; then $\begin{array} { r } { \frac { \parallel X C _ { j } \parallel } { \parallel X \parallel } { \leq } 1 - D _ { \mathrm { c o n f } } ( X { \Rightarrow } C _ { i } ) } \end{array}$ j p i 5

Further, $\begin{array} { r } { \frac { \parallel X Y C _ { j } \parallel } { \parallel X \parallel } \leq \frac { \parallel X C _ { j } \parallel } { \parallel X \parallel } { \leq } 1 - D _ { \mathrm { c o n f } } ( X { \Rightarrow } C _ { i } ) } \end{array}$ ; thus $\begin{array} { r } { \frac { \| X Y C _ { j } \| } { | T | } { \le } \frac { \| X Y C _ { j } \| } { \| X \| } { \le } 1 - D _ { \mathrm { c o n f } } ( X { \Rightarrow } C _ { i } ) } \end{array}$

Then since $1 - D _ { \mathrm { c o n f } } ( X { \Rightarrow } C i ) { < } \alpha$ , then $\frac { \| X Y C _ { j } \| } { | T | } < \alpha ,$ which means $D _ { \mathrm { s u p p } } ( X Y C _ { j } ) { < } \alpha$ . That is, $X Y \dot { C } _ { j }$ is an excluded itemset.

(2)Since ||X|| <sup>b</sup> 2|T|a, then $\frac { \parallel X \parallel - \parallel X C _ { i } \parallel } { | T | } < \frac { 2 | T | \alpha - \parallel X C _ { i } \parallel } { | T | }$

From ${ \frac { \parallel X C _ { i } \parallel } { | T | } } \geq \alpha$ , we have $\| X C _ { i } \| \geq | T | \alpha .$

Then $\begin{array} { r } { \frac { \parallel X \parallel - \parallel X C _ { i } \parallel } { \lvert T \rvert } < \frac { 2 \lvert T \rvert \alpha - \lvert T \rvert \alpha } { \lvert T \rvert } = \alpha . } \end{array}$

Since ${ \frac { \parallel X Y C _ { j } \parallel } { | T | } } \leq { \frac { \parallel X \parallel - \parallel X C _ { i } \parallel } { | T | } } , D { \mathrm { s u p p } } ( X Y C _ { j } ) < \alpha .$

That is, $X Y C _ { j }$ is an excluded itemset.

Thus, if rule $X { \Rightarrow } C _ { i }$ holds in T, and the conditions of Theorem 2.2 are satisfied, then the rule conflicts can be avoided, because hereby any itemset like $X Y C _ { j }$ is an excluded itemset. Accordingly, this strategy may be applied to the mining process, in which the itemset, $X Y C _ { j }$ , does not need to be considered further in generating larger candidate itemsets.

Example 1. Given a dataset as shown in Table 1, with $\beta { = } 0 . 8$ and $\alpha { = } 0 . 2 1$ . After the first scan of the dataset, rule <sup>b</sup>overcast Z play $( D _ { \mathrm { c o n f } } { = } 1 , D _ { \mathrm { s u p p } } { = } 0 . 2 9 ) ^ { \mathfrak { 3 } }$ can be obtained. Before executing the second scan, it has been already known that any larger candidate itemset such as {overcast, Y, don’t play} is an excluded itemset, because $1 - 1 < \alpha$ according to Theorem 2.2, where $Y \subseteq$ {Temperature, Humidity, Windy}.

Table 1 Training dataset

<table><tr><td>TID</td><td>Outlook</td><td>Temperature</td><td>Humidity</td><td>Windy</td><td>Class</td></tr><tr><td>1</td><td>Sunny</td><td>Mild</td><td>Normal</td><td>True</td><td>Play</td></tr><tr><td>2</td><td>Sunny</td><td>Hot</td><td>High</td><td>True</td><td>Don’t play</td></tr><tr><td>3</td><td>Sunny</td><td>Hot</td><td>High</td><td>False</td><td>Don’t play</td></tr><tr><td>4</td><td>Sunny</td><td>Mild</td><td>High</td><td>False</td><td>Don’t play</td></tr><tr><td>5</td><td>Sunny</td><td>Cool</td><td>Normal</td><td>False</td><td>Play</td></tr><tr><td>6</td><td>Overcast</td><td>Mild</td><td>High</td><td>True</td><td>Play</td></tr><tr><td>7</td><td>Overcast</td><td>Hot</td><td>High</td><td>False</td><td>Play</td></tr><tr><td>8</td><td>Overcast</td><td>Cool</td><td>Normal</td><td>True</td><td>Play</td></tr><tr><td>9</td><td>Overcast</td><td>Hot</td><td>Normal</td><td>False</td><td>Play</td></tr><tr><td>10</td><td>Rain</td><td>Mild</td><td>High</td><td>True</td><td>Don’t play</td></tr><tr><td>11</td><td>Rain</td><td>Cool</td><td>Normal</td><td>True</td><td>Don’t play</td></tr><tr><td>12</td><td>Rain</td><td>Mild</td><td>High</td><td>False</td><td>Play</td></tr><tr><td>13</td><td>Rain</td><td>Cool</td><td>High</td><td>False</td><td>Play</td></tr><tr><td>14</td><td>Rain</td><td>Mild</td><td>High</td><td>False</td><td>Play</td></tr><tr><td>15</td><td>Overcast</td><td>Cool</td><td>High</td><td>False</td><td>Don’t play</td></tr></table>

If another transaction as follows is added to Table 1:

<table><tr><td>15</td><td>Overcast</td><td>Cool</td><td>high</td><td>False</td><td>Don’t Play</td></tr></table>

then $D _ { \mathrm { { c o n f } } }$ (overcast Z play) = 0.8, so we have 1 $D _ { \mathrm { c o n f } } \left( \mathrm { o v e r c a s t } { \Rightarrow } \mathrm { p l a y } \right) = 1 - 0 . 8 = 0 . 2 < 0 . 2 1$ . Likewise, {overcast, $Y ,$ don’t play} is an excluded itemset. Suppose that the class label of transaction 9 in Table 1 is changed to be Don’t play, with $\beta { = } 0 . 7$ and $\alpha { = } 0 . 1 5$ . Then from ||overcast $\scriptstyle \| = 4 < 2 | \mathrm { T } | \alpha = 2 \times$ $1 4 \times 0 . 1 5 { = } 4 . 2$ (Theorem 2.2), itemsets {overcast, play} and {overcast, don’t play} can be excluded from the itemsets used to generate larger candidate itemsets.

## 3. Discovering classification rules

In this section, an algorithm called GARC (Gain based Association Rule Classification) will be presented, which could discover the compact set of classification rules. Though the general idea is in the spirit of association rule mining, it differs from conventional CBA techniques that directly apply the Apriori-type association rule mining procedures. The main characteristic of the proposed algorithm is threefold. First, it combines the conventional itemset generation and rule generation processes, and makes use of the information maintained for both rule itemsets and excluded itemsets. Second, the information gain measure is incorporated so as to only generate the itemsets including the best-split attribute value, which leads to a reduction of candidate itemsets. Third, certain strategies are applied into the mining process such that conflicting/redundant rules are avoided as well as the number of candidate itemsets generated is reduced. $\mathrm { A s }$ a result, the resultant compact set is more condensed and understandable (in terms of fewer rules), and in the mean time, as revealed by data experiments in the next sections, the classification accuracy turns out to be satisfactory.

## 3.1. GARC: gain based association rule classification

Generally speaking, one transaction in $T$ with s items can generate around $2 ^ { \mathrm { s } }$ candidate itemsets. To cope with this, the information gain measure is first used here to reduce the number of candidate itemsets. That is, only those candidate itemsets including the best split attribute value will be generated. Concretely, after the first scan of the database, all of 1-itemsets can be obtained and saved in a variable named Cand. According to the lcount and wcount values of each candidate itemset, information gain for each attribute $A ,$ , which could be used to partition the database $T$ into n datasets, may be calculated as follows:

$$
\begin{array}{l} \operatorname{info} _ {A} (T) = \sum_ {i = 1} ^ {n} \frac {\left| T _ {i} \right|}{\left| T \right|} \times \operatorname{info} (T _ {i}) = - \sum_ {i = 1} ^ {n} \frac {\left| T _ {i} \right|}{\left| T \right|} \\ \quad \times \left(\sum_ {k = 1} ^ {g} \frac {\operatorname{freq} \left(C _ {j} , T _ {i}\right)}{\left| T _ {i} \right|} \times \log_ {2} \frac {\operatorname{freq} \left(C _ {j} , T _ {i}\right)}{\left| T _ {i} \right|}\right) \\ = - \sum_ {i = 1} ^ {n} D _ {\text { supp }} (A = v _ {i}) \\ \quad \times \left(\sum_ {k = 1} ^ {g} D c _ {\text { conf }} (i _ {k}) \times \log_ {2} D _ {\text { conf }} (i _ {k})\right) \end{array}
$$

where $T _ { i }$ corresponds to the dataset whose attribute $\boldsymbol { A } ^ { * } \boldsymbol { \mathrm { s } }$ value equals $\nu _ { i } ,$ g is the number of classes, $i _ { k }$ represents itemset $\{ \nu _ { i } , C _ { k } \}$ . As a result, a best split attribute (called bestattr) can be selected after the first scan of the database. Then during the next scan of the database, only those itemsets containing this best split attribute specified by bestattr will be generated. The following example helps illustrate the idea.

Example 2. Let us consider Table 1 again. After the first scan of the dataset in Table 1, among the four attributes, attribute outlook is selected as the best split attribute. Then during the second scan of the database, tuple 1 can produce the following three candidate itemsets: {sunny, mild, play}, {sunny, normal, play}, and {sunny, true, play}. Note that {mild, normal, play}, {mild, true, play}, and {normal, true, play} will not be generated.

In addition to information gain, certain conflicts/ redundancy avoidance strategies are used to improve the quality of the rule set as well as to reduce the number of candidate itemsets, which is detailed in the next subsection, along with how excluded itemsets are dealt with.

## 3.2. Algorithmic details

As stated previously, an itemset XC is interchangeably referred to as a rule $X { \Rightarrow } C .$ . A qualified itemset

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 2
Algorithm GARC

Algorithm GARC:
1. rule={r|r is an 1-itemset, D$_{supp}$(r)≥α and D$_{conf}$(r)≥β}; //initiating the set of qualified itemsets//
2. excluded={e|e is an 1-itemset, and D$_{supp}$(e)&lt;α}; //initiating the set of excluded itemsets//
3. bestattr=gain;
4. if (β≤0.5) and (∀r:X⇒Ci ∈ rule, ∃r':X⇒Cj ∈ rule such that r' does not precede r) then
5. rule=rule - {X⇒Cj}; //deleting conflicting rules//
6. for k from 2 to m do //m is the number of ancetedent attributes//
7. empty(cand); // emptying cand, the set of candidate itemsets//
8. if coverall(rule)
9. break;
10. for each transaction t in T do
11. Ct=CandidateGen(t, bestattr, k);
12. for each c ∈ Ctdo
13. maintCand(rule, excluded, c, cand)
14. end for;
15. end for;
16. R={r|r ∈ cand, D$_{supp}$(r)≥α and D$_{conf}$(r)≥β}; //the set of qualified k-itemsets//
17. if (β≤0.5) and (∀r:X⇒i C ∈ R, ∃r':X⇒Cj ∈ R such that r' does not precede r) then
18. R=R - {X⇒Cj}; //deleting conflicting rules//
19. if (∀r:X⇒Ci ∈ R, ∃r':XY⇒Cj ∈ R such that Y≠∅, X∩Y=∅, and r' does not precede r) then
20. R=R - {XY⇒Cj}; //deleting conflicting rules//
21. rule=rule∪R;
22. E={e|e ∈ cand, D$_{supp}$(e)&lt;α};
23. excluded=excluded∪E;
24. end for;
25. sort(rule);
</div>

XC corresponds to a qualified rule $X { \Rightarrow } C .$ . In addition, for $X C , X$ is referred to the antecedent of XC, denoted by antecedent(XC) = X. The main algorithm is shown in Table 2.

Lines 1–3 perform the first scan of the database. It produces all the 1-itemsets from which qualified 1-itemsets are generated. By the method described above, the best split attribute is selected by gain, which employs the information gain measure and helps reduce the number of candidate itemsets (Table 3). Lines 6–24 perform the consecutive scans of the database. coverall(rule) tests whether rules already contain all of transactions in the training dataset, and if true, the main iteration breaks. During each scan, for a certain transaction $t ,$ CandidateGen(t, bestattr, k) generates all k-itemsets with each containing the bestattr. Working on these itemsets in $C t ,$ maintCand(rule, excluded, c, cand) then generates and maintains candidate itemsets according to qualified itemsets and excluded itemsets. Note that the itemsets returned by maintCand will be redundancy-free, and will not produce any conflicting rules if the conditions of Theorem 2.2 are satisfied. In the mean time, this will lead to generating fewer itemsets inside the process. Moreover, since rule conflicts with regard to Theorem 2.1 will be avoided if its condition $( \beta > 0 . 5 )$ is satisfied, lines 4–5 and 17–20 further remove conflicting rules (rV) when the conditions of Theorems 2.1 and 2.2 do not hold. The advantage of incorporating the conflict resolution strategy at the stages inside the k-itemset generation process (rather than after the process as a separate filter) is to further reduce the number of candidate itemsets generated (for k <sub>z</sub> 1). Finally, all rules are sorted, when the main procedure is terminated.

Note that each of the rules included in the classifier built by the above algorithm satisfies the pre-specified minimal support and minimal confidence thresholds (i.e., (a and b). Moreover, the rules that cannot be predicated to be excluded itemsets according to Theorem 2.2 (line 6 in Table 4) will be added to the set of candidate itemsets and further counted. If c contains a qualified itemset or an excluded itemset, the class attribute in c is substituted by a fixed mark q that is different from all class labels of G (i.e., G is the set of all class labels) in the database for the purpose of counting lcount while not affecting wcount (Tables 4 and 5). In addition, the rules that are redundant according to Definition 2.2 will not be included (generated) in cand (line 13 in Table 4, and line 14 in Table 5).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 3
Sub-algorithm gain

gain
begin
    for each attribute $A_i \in \{A_1, A_2, \ldots, A_m\}$ do
    compute info($A_i$) using D$_{\text{supp}}$ and D$_{\text{conf}}$ values of all 1-itemsets
    end for
    bestattr = $A_1$; mininfo = info($A_1$);
    for each attribute $A_i \in \{A_1, A_2, \ldots, A_m\}$ do
    if mininfo &gt;info($A_i$) then
    mininfo = info($A_i$)
    bestattr = $A_i$
    end if
    end for
    return bestattr
end
</div>

```txt
Table 4
Sub-algorithm maintCand

maintCand(rule, excluded, c, cand)
1. begin
2. if ¬∃r ∈ rule, (c ⊃ r) and ¬∃e ∈ excluded, (c ⊃ e) then
3.    if ¬∃r ∈ rule, (c ⊃ ancetedent(r)) then
4.    addToCand(c, cand); //adding c into cand//
5.    else
6.    if ∃r ∈ rule, (c ⊃ ancetedent(r)) and ((1 - Dconf(r) ≥ α) and (Dsupp(X) ≥ 2α) then
7.    addToCand(c, cand);
8.    else //when c is an excluded itemset//
9.    excluded = excluded ∪ E;
10.    end if;
11.    end if;
12. else
13.    if ∃e ∈ excluded, (c ⊃ e) or ∃r ∈ rule, (c ⊃ r) then
14.    c' = ancetedent(e) ∪ {q}; //q is a fixed mark different from any class in G//
15.    addToCand(c', cand); //adding c' into cand//
16.    end if;
17. end if;
18. end;
```

Finally, the algorithm will terminate in a finite number of m passes at most, where m is the number of attributes. Notably, the set of resultant classification rules is a compact set. Moreover, if the discovered rule set without using the redundancy/conflict resolution strategies is not empty (e.g., if the set of qualified 1- itemsets is not empty), the compact set will not be empty either.

## 4. Experimental results

This section shows an empirical performance evaluation of algorithm GARC, along with some comparisons with other algorithms. The experiments consist of five parts. The first part is to compare GARC with C4.5-type [30], CBA [21], NN [10], and SVM [37] classifiers on accuracy. The second part of the experiments is to test how the pruning strategies affect the efficiency and further examines the execution time of GARC. The third part discusses the impact of minimal support and minimal confidence thresholds on GARC outcomes. In the fourth part, the use of information gain for rule reduction is examined. The last part compares GARC with the CBA classifier in terms of the number of rules produced. The experiments were conducted in the environment with Windows 2000 Server, Intel Pentium 4 1.5 GHz, 512 MB RAM and Visual C++. It should be mentioned that, all the following experiments are tested based on datasets from a commonly used benchmarking database in the field, namely the UCI Machine Learning Repository [27], including the 26 datasets that CBA method selected. In total, 30 datasets are used.

The basic information of the datasets is listed in Table 6.

Since some data are continuous and Apriori-type methods mainly focus on discrete data, the entropy based discretization method is applied in order to deal with continuous attributes for the experiments. More concretely, a recursive entropy minimization heuristic is used for discretization and combined with the Minimum Description Length criterion to control the number of intervals produced over a continuous space [15].

## 4.1. Accuracy

Accuracy is one of the basic performance measures for classification algorithms. For a classifier,

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 5
Sub-algorithm addToCand

addToCand(c, cand);
1. begin
2.    find=0; count=1;
3.    for each candidate itemset  $c_{i}$  in cand do
4.    if  $c = c_{i}$  then
5.    $c_{i}.wcount = c_{i}.wcount + 1$ ;
6.    $c_{i}.lcount = c_{i}.lcount + 1$ ;
7.    find = 1;
8.    else
9.    if ancetedent(c) = ancetedent( $c_{i}$ ) then
10.    $c_{i}.lcount = c_{i}.lcount + 1$ ;
11.    count = count +  $c_{i}.lcount$ ;
12.    end if;
13.    end for;
14.    if find = 0 and (consequent of c is not equal to q) then
//when c is not redundant//
15.    c is included in cand with c.lcount=count and
c.wcount=1;
16.    end if;
17. end;
</div>

Table 6  
Basic information of the 30 UCI datasets

<table><tr><td></td><td>Dataset</td><td>Attributes</td><td>Number of attributes</td><td>Null value (Y/N)</td><td>Number of training data</td><td>Number of testing data</td></tr><tr><td>1</td><td>Anneal</td><td>Discrete, continuous</td><td>38</td><td>Y</td><td>598</td><td>300</td></tr><tr><td>2</td><td>Australian</td><td>Discrete, continuous</td><td>14</td><td>N</td><td>460</td><td>230</td></tr><tr><td>3</td><td>Auto</td><td>Discrete, continuous</td><td>26</td><td>Y</td><td>136</td><td>69</td></tr><tr><td>4</td><td>Breast</td><td>Continuous</td><td>10</td><td>Y</td><td>466</td><td>233</td></tr><tr><td>5</td><td>Cleve</td><td>Discrete, continuous</td><td>13</td><td>N</td><td>202</td><td>101</td></tr><tr><td>6</td><td>Crx</td><td>Discrete, continuous</td><td>15</td><td>N</td><td>490</td><td>200</td></tr><tr><td>7</td><td>Diabetes</td><td>Continuous</td><td>8</td><td>N</td><td>512</td><td>256</td></tr><tr><td>8</td><td>German</td><td>Discrete, continuous</td><td>20</td><td>N</td><td>666</td><td>33</td></tr><tr><td>9</td><td>Glass</td><td>Continuous</td><td>9</td><td>N</td><td>142</td><td>72</td></tr><tr><td>10</td><td>Heart</td><td>Continuous</td><td>13</td><td>N</td><td>180</td><td>90</td></tr><tr><td>11</td><td>Hepatitis</td><td>Discrete, continuous</td><td>19</td><td>Y</td><td>103</td><td>52</td></tr><tr><td>12</td><td>Horse</td><td>Discrete, continuous</td><td>22</td><td>Y</td><td>300</td><td>68</td></tr><tr><td>13</td><td>Hypothyroid</td><td>Discrete, continuous</td><td>29</td><td>Y</td><td>2514</td><td>1258</td></tr><tr><td>14</td><td>Ionosphere</td><td>Continuous</td><td>34</td><td>Y</td><td>234</td><td>117</td></tr><tr><td>15</td><td>Iris</td><td>Continuous</td><td>4</td><td>N</td><td>100</td><td>50</td></tr><tr><td>16</td><td>Labor</td><td>Discrete, continuous</td><td>16</td><td>Y</td><td>40</td><td>17</td></tr><tr><td>17</td><td>Led7</td><td>Discrete</td><td>7</td><td>N</td><td>200</td><td>3000</td></tr><tr><td>18</td><td>Lymph</td><td>Discrete</td><td>18</td><td>N</td><td>98</td><td>50</td></tr><tr><td>19</td><td>Pima</td><td>Continuous</td><td>8</td><td>N</td><td>512</td><td>256</td></tr><tr><td>20</td><td>Sick</td><td>Discrete, continuous</td><td>29</td><td>Y</td><td>2800</td><td>972</td></tr><tr><td>21</td><td>Sonar</td><td>Continuous</td><td>60</td><td>N</td><td>138</td><td>70</td></tr><tr><td>22</td><td>Tic-tac-toe</td><td>Discrete</td><td>9</td><td>N</td><td>638</td><td>320</td></tr><tr><td>23</td><td>Vehicle</td><td>Continuous</td><td>18</td><td>N</td><td>564</td><td>282</td></tr><tr><td>24</td><td>Waveform</td><td>Continuous</td><td>21</td><td>N</td><td>300</td><td>1000</td></tr><tr><td>25</td><td>Wine</td><td>Continuous</td><td>13</td><td>N</td><td>118</td><td>60</td></tr><tr><td>26</td><td>Zoo</td><td>Discrete</td><td>16</td><td>N</td><td>67</td><td>34</td></tr><tr><td>27</td><td>Balance</td><td>Continuous</td><td>4</td><td>N</td><td>416</td><td>209</td></tr><tr><td>28</td><td>Lenses</td><td>Discrete</td><td>4</td><td>N</td><td>16</td><td>8</td></tr><tr><td>29</td><td>Monk2</td><td>Discrete</td><td>6</td><td>N</td><td>169</td><td>432</td></tr><tr><td>30</td><td>Vote</td><td>Discrete</td><td>16</td><td>N</td><td>300</td><td>135</td></tr></table>

its classification accuracy is the ratio of the number of cases truly predicted by the classifier over the total number of cases in the test dataset, e.g.,

$$
\text {Accuracy} = \frac {\text {num(test\_predicted} = \text {true})}{\text {num\_totaltest}} \times 100 \%.
$$

In this experiment, we compared GARC with C4.5 rule, CBA, NN and SVM classifiers based on the 30 UCI datasets. We obtained the accuracy results as shown in Tables 7, 8. It will be discussed in later subsections on how the settings of the thresholds are considered.

The results shown in Tables 7 and 8 indicate that the classification accuracy of GARC is satisfactory. On average, the accuracy of GARC seemed to be higher than that of the C4.5 rule and similar to that of CBA. Moreover the GARC classifier appeared to be more stable than CBA and C4.5 rule classifiers in terms of standard deviations of accuracy. These findings could be further justified by statistical significance tests. Moreover, Table 8 shows that the accuracy of GARC is lower than that of NN or SVM, and that the standard deviation of GARC is lower than that of NN and SVM. However, it is important to note that GARC, NN, SVM are not significantly different in accuracy.

Thus, we could test the significance of the accuracy mean difference for any two algorithms by approximately constructing a confidence interval at a given confidence level [6,18]. The testing results revealed that on average the accuracy of GARC was not significantly different from that of CBA, C4.5, NN or SVM. These have been shown in Table 9.

Table 7  
Algorithms’ accuracy on C4.5, CBA and GARC

<table><tr><td></td><td>Datasets</td><td>C4.5%</td><td>CBA%</td><td>GARC%</td></tr><tr><td>1</td><td>Anneal</td><td>88.70</td><td>98.00</td><td>89.30</td></tr><tr><td>2</td><td>Australian</td><td>87.00</td><td>86.96</td><td>87.39</td></tr><tr><td>3</td><td>Auto</td><td>62.70</td><td>72.46</td><td>71.32</td></tr><tr><td>4</td><td>Breast</td><td>95.70</td><td>96.57</td><td>94.85</td></tr><tr><td>5</td><td>Cleve</td><td>77.20</td><td>81.19</td><td>80.13</td></tr><tr><td>6</td><td>Crx</td><td>83.00</td><td>83.50</td><td>82.50</td></tr><tr><td>7</td><td>Diabetes</td><td>69.10</td><td>74.22</td><td>71.03</td></tr><tr><td>8</td><td>German</td><td>73.40</td><td>76.35</td><td>75.20</td></tr><tr><td>9</td><td>Glass</td><td>62.50</td><td>65.28</td><td>68.06</td></tr><tr><td>10</td><td>Heart</td><td>83.30</td><td>83.33</td><td>80.57</td></tr><tr><td>11</td><td>Hepatitis</td><td>80.80</td><td>76.92</td><td>86.69</td></tr><tr><td>12</td><td>Horse</td><td>85.30</td><td>80.88</td><td>75.00</td></tr><tr><td>13</td><td>Hypothyroid</td><td>99.20</td><td>98.20</td><td>94.79</td></tr><tr><td>14</td><td>Ionosphere</td><td>88.00</td><td>93.16</td><td>90.64</td></tr><tr><td>15</td><td>Iris</td><td>92.00</td><td>94.00</td><td>94.01</td></tr><tr><td>16</td><td>Labor</td><td>82.40</td><td>88.24</td><td>82.35</td></tr><tr><td>17</td><td>Led7</td><td>67.50</td><td>57.67</td><td>56.53</td></tr><tr><td>18</td><td>Lymph</td><td>70.00</td><td>84.00</td><td>77.56</td></tr><tr><td>19</td><td>Pima</td><td>76.60</td><td>76.17</td><td>73.83</td></tr><tr><td>20</td><td>Sick</td><td>99.00</td><td>96.50</td><td>93.83</td></tr><tr><td>21</td><td>Sonar</td><td>74.30</td><td>64.29</td><td>74.30</td></tr><tr><td>22</td><td>Tic-tac-toe</td><td>82.20</td><td>99.06</td><td>100.00</td></tr><tr><td>23</td><td>Vehicle</td><td>67.70</td><td>70.21</td><td>61.89</td></tr><tr><td>24</td><td>Waveform</td><td>70.40</td><td>75.66</td><td>71.15</td></tr><tr><td>25</td><td>Wine</td><td>85.00</td><td>86.67</td><td>83.46</td></tr><tr><td>26</td><td>Zoo</td><td>85.30</td><td>79.41</td><td>82.35</td></tr><tr><td>27</td><td>Balance</td><td>77.50</td><td>72.73</td><td>71.29</td></tr><tr><td>28</td><td>Lenses</td><td>62.50</td><td>62.50</td><td>75.32</td></tr><tr><td>29</td><td>Monk2</td><td>65.00</td><td>67.13</td><td>65.74</td></tr><tr><td>30</td><td>Vote</td><td>97.00</td><td>95.56</td><td>89.67</td></tr><tr><td></td><td>Mean</td><td>79.68</td><td>81.23</td><td>80.03</td></tr><tr><td></td><td>Derivation</td><td>1.23</td><td>1.40</td><td>1.15</td></tr><tr><td></td><td>Standard deviation</td><td>11.09</td><td>11.84</td><td>10.72</td></tr></table>

GARC is running with default setting of a = 0.01, b = 0.7.

In addition, two C4.5 extensions, namely C4.5 tree and C4.5 tree pruning [30], were tested on the same 30 datasets by means of confidence intervals, revealing that the accuracy of GARC was not significantly different from that of either C4.5 tree or C4.5 tree pruning at 95% confidence level. Furthermore, our test on the 30 datasets is, however, not supportive to the statement in Ref. [21] that the accuracy of the C4.5 rule is higher than that of either C4.5 tree or C4.5 tree pruning.

In summary, GARC is satisfactory in terms of accuracy, compared with CBA, C4.5-type, NN and

SVM. Worthwhile to mention is that, compared with non-rule-based classifiers (e.g., NN and SVM), GARC produces a classifier in the form of explicit rules, which are often appealing for use and explanation to decision makers.

Table 8  
Algorithms’ accuracy on SVM, NN and GARC

<table><tr><td></td><td>Datasets</td><td>SVM%</td><td>NN%</td><td>GARC%</td></tr><tr><td>1</td><td>Anneal</td><td>100.00</td><td>98.67</td><td>96.67</td></tr><tr><td>2</td><td>Australian</td><td>86.96</td><td>90.00</td><td>87.39</td></tr><tr><td>3</td><td>Auto</td><td>72.46</td><td>63.77</td><td>71.00</td></tr><tr><td>4</td><td>Breast</td><td>96.14</td><td>94.85</td><td>95.71</td></tr><tr><td>5</td><td>Cleve</td><td>82.18</td><td>81.19</td><td>81.19</td></tr><tr><td>6</td><td>Crx</td><td>82.50</td><td>85.00</td><td>85.50</td></tr><tr><td>7</td><td>Diabetes</td><td>73.83</td><td>78.13</td><td>74.61</td></tr><tr><td>8</td><td>German</td><td>71.86</td><td>75.15</td><td>76.35</td></tr><tr><td>9</td><td>Glass</td><td>79.17</td><td>73.61</td><td>68.06</td></tr><tr><td>10</td><td>Heart</td><td>88.88</td><td>87.78</td><td>88.00</td></tr><tr><td>11</td><td>Hepatitis</td><td>84.62</td><td>78.85</td><td>86.54</td></tr><tr><td>12</td><td>Horse</td><td>86.76</td><td>80.88</td><td>88.24</td></tr><tr><td>13</td><td>Hypothyroid</td><td>100.00</td><td>98.01</td><td>94.79</td></tr><tr><td>14</td><td>Ionosphere</td><td>96.58</td><td>94.87</td><td>94.85</td></tr><tr><td>15</td><td>Iris</td><td>94.00</td><td>96.00</td><td>96.00</td></tr><tr><td>16</td><td>Labor</td><td>100.00</td><td>94.12</td><td>82.35</td></tr><tr><td>17</td><td>Led7</td><td>68.97</td><td>67.73</td><td>67.47</td></tr><tr><td>18</td><td>Lymph</td><td>82.00</td><td>86.00</td><td>80.00</td></tr><tr><td>19</td><td>Pima</td><td>79.69</td><td>78.52</td><td>76.17</td></tr><tr><td>20</td><td>Sick</td><td>96.71</td><td>97.02</td><td>93.83</td></tr><tr><td>21</td><td>Sonar</td><td>88.57</td><td>78.57</td><td>74.30</td></tr><tr><td>22</td><td>Tic-tac-toe</td><td>99.38</td><td>97.50</td><td>100.00</td></tr><tr><td>23</td><td>Vehicle</td><td>79.08</td><td>78.37</td><td>67.36</td></tr><tr><td>24</td><td>Waveform</td><td>80.85</td><td>81.06</td><td>71.55</td></tr><tr><td>25</td><td>Wine</td><td>98.33</td><td>95.00</td><td>86.67</td></tr><tr><td>26</td><td>Zoo</td><td>88.24</td><td>88.24</td><td>85.29</td></tr><tr><td>27</td><td>Balance</td><td>99.04</td><td>92.34</td><td>73.21</td></tr><tr><td>28</td><td>Lenses</td><td>62.50</td><td>75.00</td><td>87.50</td></tr><tr><td>29</td><td>Monk2</td><td>84.72</td><td>100.00</td><td>74.54</td></tr><tr><td>30</td><td>Vote</td><td>97.78</td><td>99.26</td><td>96.30</td></tr><tr><td></td><td>Mean</td><td>86.73</td><td>86.18</td><td>83.38</td></tr><tr><td></td><td>Deviation</td><td>1.11</td><td>1.03</td><td>1.00</td></tr><tr><td></td><td>Standard deviation</td><td>10.52</td><td>10.13</td><td>10.01</td></tr></table>

SVM classifier use LIBSVM software package available online at http://www.csie.ntu.edu.tw/\~cjlin/libsvm Ref. [36]. For SVM, the parameters will largely affect the results. With default settings by LIBSVM, the average accuracy is 79.84. After parameters selection with 10-fold cross validation, SVM is running on the best situation.

NN classifier is using WEKA software package [35]. A 3-level Back-Propagation Model has been constructed, with the number of neurons set to 2, 4 and 8. The results are not sensitive to the number of neurons. NN is also running on the best situation. GARC is running on the best situation with corresponding a and b.

Confidence intervals on the mean difference for accuracy of classifiers

<table><tr><td></td><td>Confidence level %</td><td>Interval%</td><td>Significance</td></tr><tr><td rowspan="2">GARC-CBA</td><td>95</td><td>[-6.92,4.51]</td><td>No</td></tr><tr><td>90</td><td>[-6.00,3.59]</td><td>No</td></tr><tr><td rowspan="2">GARC-C4.5 rule</td><td>95</td><td>[-5.17,5.87]</td><td>No</td></tr><tr><td>90</td><td>[-4.28,4.98]</td><td>No</td></tr><tr><td rowspan="2">GARC-NN</td><td>95</td><td>[-8.71,1.74]</td><td>No</td></tr><tr><td>90</td><td>[-7.87,0.90]</td><td>No</td></tr><tr><td rowspan="2">GARC-SVM</td><td>95</td><td>[-9.35,1.30]</td><td>No</td></tr><tr><td>90</td><td>[-8.49,0.44]</td><td>No</td></tr></table>

## 4.2. GARC with pruning strategies

This subsection examines GARC’s pruning strategy effectiveness in terms of accuracy, understandability (e.g., the number of rules generated) and computational efficiency (e.g., the number of candidate itemsets generated, execution time, etc.). By a pruning strategy we mean the strategy discussed in Section 2.4 and incorporated in the mining process. Since we are to study the GARC performance with and without the strategy incorporation, the dataset used needs to be expansible and adjustable in size and complexity. Apparently, the previously used 30 datasets can hardly serve this purpose. Hence, as proposed in Ref. [3] for similar experiments, a synthetic database is employed. Each transaction in the database has 9 attributes shown in Table 10. There are ten classification functions available to produce data distributions with varied complexities. IBM Research Center developed a series of classification functions of increasing complexity that used the above attributes to classify people into different groups [19]. Four of them are selected, which include the low-complexity (function 2), mid-complexity (function 5 and 8) and the most complex function 10. Specifically, function 10 is one of the hardest to characterize and could result in the highest classification errors (Table 11). The Data generator source is from Ref. [19].

Attributes of the synthetic database

<table><tr><td>Attribute</td><td>Value</td></tr><tr><td>Salary</td><td>Uniformly distributed from 20000 to 150000</td></tr><tr><td>Commission</td><td>If salary ≥75000, commission=0 else uniformly distributed from 10000 to 75000</td></tr><tr><td>Age</td><td>Uniformly distributed from 20 to 80</td></tr><tr><td>Ed_level</td><td>Uniformly chosen from 0 to 4</td></tr><tr><td>Car</td><td>Make of the car, uniformly chosen from 1 to 20</td></tr><tr><td>Zipcode</td><td>Uniformly chosen from 9 available zipcodes</td></tr><tr><td>Housevalue</td><td>Uniformly distributed from 0.5*k*100000 to 1.5*k*100000, where 0≤k≤9 and depends on the zipcodes</td></tr><tr><td>Years owned</td><td>Uniformly distributed from 1 to 30</td></tr><tr><td>Loan</td><td>Uniformly distributed from 0 to 500000</td></tr></table>

Since GARC works with categorical attributes, the non-categorical attributes were discretized first. We used a simple equal-width method for discretization. The interval width and the number of intervals are shown in Table 12.

The performances of GARC with and without those (pruning) strategies proposed in Section 2 are shown in Fig. 1. The findings indicated that GARC with the strategies was superior to that without the strategies in three respects, namely, computational efficiency (fewer candidate itemsets and shorter execution time as shown in Fig. 1a,b), understandability (fewer rules as shown in Fig. 1c), and accuracy (similar rates as shown in Fig. 1d).

```txt
Table 11
Functions' definitions

Function 2:
Class A: ((age<40) ^ (50k≤salary≤100k))∨
    ((40≤age<60) ^ (75k≤salary≤125k))∨
    ((age60) ^ (25k≤salary≤75k)).
Function 5:
Class A: ((age<40) ^
    (((50k≤salary≤100k)) ? (100k≤loan≤300k) :
    (200k≤loan≤400k))))∨
    ((40≤age<60)∧
    (((75k≤salary≤125k)) ? (200k≤loan≤400k) :∨
    (300k≤loan≤500k) ))))∨
    ((age≥60)∧
    (((25k≤salary≤75k)) ? (300k≤loan≤500k) :
    (100k≤loan≤300k))))
Function 8:
    disposable = (0.67 × (salary + commission) - 5000 × elevel -20k)
Class A: disposable >0

Function 10
    hyears < 20⇒ equity=0
    hyears ≥ 20⇒ equity=0.1 hvalue (hyeares 20)
    disposable = (0.67 (salary+commission) 5000 × elevel + 0.2 equity -10k)
Class A: disposable >0
```  
\* A ? B : C stands for a logic expression meaning that if A is TRUE then B, else C.

Table 12  
Discretization of the attribute values

<table><tr><td>Attribute</td><td>Interval width</td><td>No. of intervals</td></tr><tr><td>Salary</td><td>25,000</td><td>6</td></tr><tr><td>Commission</td><td>10,000</td><td>7</td></tr><tr><td>Age</td><td>10</td><td>6</td></tr><tr><td>Ed_level</td><td>-</td><td>5</td></tr><tr><td>Car</td><td>-</td><td>20</td></tr><tr><td>Zipcode</td><td>-</td><td>9</td></tr><tr><td>Housevalue</td><td>100,000</td><td>14</td></tr><tr><td>Years owned</td><td>3</td><td>10</td></tr><tr><td>Loan</td><td>50,000</td><td>10</td></tr></table>

Further, Fig. 2 illustrates the execution time of GARC (e.g., for function 10) with the number of training samples increasing from 100,000 to 500,000, showing a near-linear computational complexity in time. This was also done for CBA and resulted in almost the same outcome.

## 4.3. Settings of minimal support and minimal confidence

As mentioned in previous subsections, the experiments were conducted with a setting of $\alpha { = } 0 . 0 1$ and $\beta { = } 0 . 7$ for min-support and min-confidence. In this section, we will discuss further the impact of such settings on the accuracy of GARC. With each of the same datasets, we could obtain the best setting of a and b in yielding the highest accuracy. Obviously, the best setting for one dataset is generally different from that for another dataset. To determine a single setting to be used in comparison for 30 datasets, we chose $\alpha { = } 0 . 0 1$ and $\beta { = } 0 . 7 ,$ as they appeared quite often (e.g., about 19 times out of 30 for $\alpha { = } 0 . 0 1$ and 14/30 for $\beta { = } 0 . 7 )$ Table 13 shows the details.

![](/api/attachments/KQHM5UHM/fulltext/images/a1c4ff0006e934daf7f6dcd1556a70aa35cbeaae1af37fe934e3c06e059a155c.jpg)  
Fig. 2. Running time vs. data size.

<table><tr><td></td><td>With Strategies</td><td>Without Strategies</td></tr><tr><td>Function 2</td><td>21</td><td>228</td></tr><tr><td>Function 5</td><td>21</td><td>336</td></tr><tr><td>Function 8</td><td>87</td><td>144</td></tr><tr><td>Function 10</td><td>29</td><td>249</td></tr></table>

Moreover, our experiments showed that as minconfidence increases, the accuracy would increase first then decrease. This may be because when minconfidence is too low, many useless rules will be generated, which will disturb the classifier. On the other hand, when min-confidence is too high, many actually meaningful rules will not be discovered, which will lead many transactions to being classified into the default class, resulting in lower accuracy. Generally, it could be found that the best performance of accuracy is around the situation where $\alpha { = } 0 . 0 1$ and $\beta { = } 0 . 7 .$

## 4.4. Impact of the information gain measure in GARC

As discussed previously, GARC uses information gain to retrieve the best split attribute. In this section, some experimental results are given to show how this measure affects the accuracy and efficiency of GARC.

(a) Number of Candidate Itemsets

<table><tr><td></td><td>With Strategies</td><td>Without Strategies</td></tr><tr><td>Function 2</td><td>5179</td><td>22231</td></tr><tr><td>Function 5</td><td>10302</td><td>26951</td></tr><tr><td>Function 8</td><td>11056</td><td>12000</td></tr><tr><td>Function 10</td><td>8435</td><td>28059</td></tr></table>

<table><tr><td></td><td>With Strategies</td><td>Without Strategies</td></tr><tr><td>Function 2</td><td>13.24</td><td>179.10</td></tr><tr><td>Function 5</td><td>21</td><td>190</td></tr><tr><td>Function 8</td><td>14.74</td><td>16.25</td></tr><tr><td>Function 10</td><td>11.21</td><td>182.39</td></tr></table>

(c) Number of Rules  
(b) Execution Time (sec.)

<table><tr><td></td><td>With Strategies</td><td>Without Strategies</td></tr><tr><td>Function 2</td><td>0.84</td><td>0.83</td></tr><tr><td>Function 5</td><td>0.81</td><td>0.85</td></tr><tr><td>Function 8</td><td>0.90</td><td>0.90</td></tr><tr><td>Function 10</td><td>0.84</td><td>0.86</td></tr></table>

(d) Accuracy  
Fig. 1. Performances of GARC with and without strategies.

Table 13  
Settings of a and b vs. accuracy

<table><tr><td rowspan="2"></td><td colspan="3">Highest accuracy</td><td colspan="2">Highest accuracy at α=0.01</td><td rowspan="2">Accuracy at α=0.01, β=0.7 (%)</td></tr><tr><td>%</td><td>α</td><td>β</td><td>%</td><td>β</td></tr><tr><td>Anneal</td><td>96.67</td><td>0.01</td><td>0.95</td><td>96.67</td><td>0.95</td><td>89.33</td></tr><tr><td>Australian</td><td>87.39</td><td>0.01</td><td>0.7</td><td>87.39</td><td>0.7</td><td>87.39</td></tr><tr><td>Auto</td><td>71</td><td>0.01</td><td>0.7</td><td>71</td><td>0.7</td><td>71.07</td></tr><tr><td>Balance</td><td>73.21</td><td>0.01</td><td>0.85</td><td>73.21</td><td>0.85</td><td>71.29</td></tr><tr><td>Breast</td><td>95.71</td><td>0.01</td><td>0.95</td><td>95.71</td><td>0.95</td><td>94.85</td></tr><tr><td>Cleve</td><td>81.19</td><td>0.01</td><td>0.9</td><td>81.19</td><td>0.9</td><td>80.2</td></tr><tr><td>Crx</td><td>85.5</td><td>0.05</td><td>0.9</td><td>84.5</td><td>0.9</td><td>82.5</td></tr><tr><td>Diabetes</td><td>74.61</td><td>0.01</td><td>0.85</td><td>74.61</td><td>0.85</td><td>71.48</td></tr><tr><td>German</td><td>76.35</td><td>0.01</td><td>0.75</td><td>76.35</td><td>0.75</td><td>76.05</td></tr><tr><td>Glass</td><td>68.06</td><td>0.01</td><td>0.7</td><td>68.06</td><td>0.7</td><td>68.06</td></tr><tr><td>Heart</td><td>88</td><td>0.01</td><td>0.5</td><td>88</td><td>0.5</td><td>81.11</td></tr><tr><td>Hepatitis</td><td>86.54</td><td>0.01</td><td>0.7</td><td>86.54</td><td>0.7</td><td>86.54</td></tr><tr><td>Horse</td><td>88.24</td><td>0.01</td><td>0.85</td><td>88.24</td><td>0.85</td><td>75</td></tr><tr><td>Hypo</td><td>94.79</td><td>0.01</td><td>0.7</td><td>94.79</td><td>0.7</td><td>94.79</td></tr><tr><td>Ionosphere</td><td>94.87</td><td>0.01</td><td>0.95</td><td>94.87</td><td>0.95</td><td>91.45</td></tr><tr><td>Iris</td><td>96</td><td>0.01</td><td>1</td><td>96</td><td>1</td><td>94</td></tr><tr><td>Labor</td><td>82.35</td><td>0.01</td><td>0.7</td><td>82.35</td><td>0.7</td><td>82.35</td></tr><tr><td>Led7</td><td>67.47</td><td>0.02</td><td>0.5</td><td>66.33</td><td>0.5</td><td>57</td></tr><tr><td>Lenses</td><td>87.5</td><td>0.07</td><td>0.8</td><td>75</td><td>0.7</td><td>75</td></tr><tr><td>Lymph</td><td>80</td><td>0.02</td><td>0.8</td><td>78</td><td>0.8</td><td>78</td></tr><tr><td>Monk2</td><td>74.54</td><td>0.01</td><td>0.95</td><td>74.54</td><td>0.95</td><td>67.13</td></tr><tr><td>Pima</td><td>76.17</td><td>0.01</td><td>0.85</td><td>76.17</td><td>0.85</td><td>73.83</td></tr><tr><td>Sick</td><td>93.83</td><td>0.01</td><td>0.7</td><td>93.83</td><td>0.7</td><td>93.83</td></tr><tr><td>Sonar</td><td>74.3</td><td>0.01</td><td>0.7</td><td>74.3</td><td>0.7</td><td>74.3</td></tr><tr><td>Tic-tac-toe</td><td>100</td><td>0.01</td><td>0.7</td><td>100</td><td>0.7</td><td>100</td></tr><tr><td>Vehicle</td><td>67.36</td><td>0.01</td><td>0.7</td><td>67.36</td><td>0.7</td><td>67.36</td></tr><tr><td>Vote</td><td>96.3</td><td>0.01</td><td>0.95</td><td>96.3</td><td>0.95</td><td>89.67</td></tr><tr><td>Waveform</td><td>71.55</td><td>0.02</td><td>0.7</td><td>69.51</td><td>0.9</td><td>71</td></tr><tr><td>Wine</td><td>86.67</td><td>0.09</td><td>0.7</td><td>83.33</td><td>0.7</td><td>83.33</td></tr><tr><td>Zoo</td><td>85.29</td><td>0.05</td><td>0.95</td><td>82.35</td><td>0.7</td><td>82.35</td></tr></table>

The results revealed that the average accuracy with information gain was slightly higher than that without information gain. Statistically, the accuracy with information gain is significantly similar to that without information gain at both 95% and 90% confidence levels. These are shown in Tables 14 and 15.

In addition, considering the average number of rules and running times, the results revealed that information gain would lead to much fewer rules and less computational time remarkably. This is largely due to the fact that the number of candidate itemsets has been considerably reduced through introducing information gain in the mining process. On average, the number of rules with information gain was only around 39% of that without the gain, and the execution time with information gain was only around 3.2% of that without information gain, according to the experiment (shownin Table 16).

Table 14  
Accuracy by using information gain and not using information gain

<table><tr><td>Datasets</td><td>Information gain incorporated</td><td>Information gain not incorporated</td></tr><tr><td>Anneal</td><td>89.33</td><td>90</td></tr><tr><td>Australian</td><td>87.39</td><td>87.39</td></tr><tr><td>Auto</td><td>71.07</td><td>65.22</td></tr><tr><td>Balance</td><td>71.29</td><td>72.25</td></tr><tr><td>Breast</td><td>94.85</td><td>94.85</td></tr><tr><td>Cleve</td><td>80.2</td><td>68.32</td></tr><tr><td>Crx</td><td>82.5</td><td>81.5</td></tr><tr><td>Diabetes</td><td>71.48</td><td>67.97</td></tr><tr><td>German</td><td>76.05</td><td>72.55</td></tr><tr><td>Glass</td><td>68.06</td><td>66.67</td></tr><tr><td>Heart</td><td>81.11</td><td>81.11</td></tr><tr><td>Hepatitis</td><td>86.54</td><td>86.54</td></tr><tr><td>Horse</td><td>75</td><td>75</td></tr><tr><td>Hypo</td><td>94.79</td><td>94.79</td></tr><tr><td>Ionosphere</td><td>91.45</td><td>91.45</td></tr><tr><td>Iris</td><td>94</td><td>94</td></tr><tr><td>Labor</td><td>82.35</td><td>82.35</td></tr><tr><td>Led7</td><td>57</td><td>55.8</td></tr><tr><td>Lenses</td><td>75</td><td>75</td></tr><tr><td>Lymph</td><td>78</td><td>78</td></tr><tr><td>Monk2</td><td>67.13</td><td>67.13</td></tr><tr><td>Pima</td><td>73.83</td><td>73.83</td></tr><tr><td>Sick</td><td>93.83</td><td>93.83</td></tr><tr><td>Sonar</td><td>74.3</td><td>67.14</td></tr><tr><td>Tic-tac-toe</td><td>100</td><td>100</td></tr><tr><td>Vehicle</td><td>67.36</td><td>63.83</td></tr><tr><td>Vote</td><td>89.67</td><td>84.44</td></tr><tr><td>Waveform</td><td>71</td><td>71.98</td></tr><tr><td>Wine</td><td>83.33</td><td>83.33</td></tr><tr><td>Zoo</td><td>82.35</td><td>82.35</td></tr><tr><td>Mean</td><td>80.34</td><td>78.95</td></tr><tr><td>Standard deviation</td><td>10.35</td><td>11.29</td></tr></table>

## 4.5. GARC and CBA

Though GARC and CBA are all based on association rule mining, they are different: CBA is basically of Apriori-type, whereas GARC is not. The main difference is that GARC combines rule generation with respective frequent itemset generation, making use of excluded itemsets in generating candidate itemsets. In addition, GARC uses information gain to reduce the number of candidate itemsets, which could then reduce the number of rules. Moreover, the number of rules could also be reduced using pruning/resolution strategies such that certain conflicting and redundant rules could be avoided, whereas the CBA algorithm itself will generate more rules. Table 17 tabulates the comparative results based on the 30 benchmarking datasets that were used pre-

Table 15  
Confidence intervals on the mean difference for accuracy

<table><tr><td>Information gain-No information gain</td><td>Confidence level%</td><td>Interval%</td><td>Significance</td></tr><tr><td rowspan="2">Accuracy</td><td>95</td><td>[-4.09, 6.87]</td><td>No</td></tr><tr><td>90</td><td>[-3.21, 5.99]</td><td>No</td></tr></table>

Table 16  
Number of rules and running time by using information gain (IG) and not using information gain (NIG)

<table><tr><td rowspan="2"></td><td colspan="2">Number of rules</td><td colspan="2">Running time (s)</td></tr><tr><td>IG</td><td>NIG</td><td>IG</td><td>NIG</td></tr><tr><td>Anneal</td><td>72</td><td>85</td><td>21.422</td><td>7269.953</td></tr><tr><td>Australian</td><td>17</td><td>17</td><td>0.125</td><td>0.0160</td></tr><tr><td>Auto</td><td>650</td><td>2156</td><td>3785.860</td><td>116901.047</td></tr><tr><td>Balance</td><td>4</td><td>10</td><td>0.000000001</td><td>0.063</td></tr><tr><td>Breast</td><td>21</td><td>25</td><td>20.5</td><td>237.328</td></tr><tr><td>Cleve</td><td>23</td><td>37</td><td>253.564</td><td>1578.468</td></tr><tr><td>Crx</td><td>21</td><td>64</td><td>2.031</td><td>61.812</td></tr><tr><td>Diabetes</td><td>11</td><td>13</td><td>25.985</td><td>112.078</td></tr><tr><td>German</td><td>78</td><td>188</td><td>559.766</td><td>21953.438</td></tr><tr><td>Glass</td><td>17</td><td>21</td><td>2.062</td><td>12.687</td></tr><tr><td>Heart</td><td>12</td><td>12</td><td>0.000000001</td><td>0.00000001</td></tr><tr><td>Hepatitis</td><td>23</td><td>23</td><td>0.063</td><td>0.010</td></tr><tr><td>Horse</td><td>26</td><td>26</td><td>0.125</td><td>0.016</td></tr><tr><td>Hypo</td><td>48</td><td>48</td><td>0.265</td><td>0.094</td></tr><tr><td>Ionosphere</td><td>67</td><td>67</td><td>0.360</td><td>0.160</td></tr><tr><td>Iris</td><td>7</td><td>10</td><td>0.000000001</td><td>0.000000001</td></tr><tr><td>Labor</td><td>15</td><td>42</td><td>0.093</td><td>0.266</td></tr><tr><td>Led7</td><td>33</td><td>51</td><td>0.234</td><td>1.766</td></tr><tr><td>Lenses</td><td>12</td><td>13</td><td>0.000000001</td><td>0.000000001</td></tr><tr><td>Lymph</td><td>17</td><td>17</td><td>0.296</td><td>0.100</td></tr><tr><td>Monk2</td><td>2</td><td>2</td><td>0.000000001</td><td>0.000000001</td></tr><tr><td>Pima</td><td>6</td><td>6</td><td>6.016</td><td>33.594</td></tr><tr><td>Sick</td><td>56</td><td>56</td><td>0.281</td><td>0.172</td></tr><tr><td>Sonar</td><td>16</td><td>33</td><td>2.765</td><td>549.750</td></tr><tr><td>Tic-tac-toe</td><td>26</td><td>26</td><td>0.063</td><td>0.010</td></tr><tr><td>Vehicle</td><td>112</td><td>543</td><td>173.688</td><td>4852.828</td></tr><tr><td>Vote</td><td>32</td><td>96</td><td>0.937</td><td>49.969</td></tr><tr><td>Waveform</td><td>25</td><td>168</td><td>0.250</td><td>30.078</td></tr><tr><td>Wine</td><td>16</td><td>16</td><td>0.093</td><td>0.010</td></tr><tr><td>Zoo</td><td>90</td><td>151</td><td>2.390</td><td>60.313</td></tr><tr><td>Mean</td><td>51.83</td><td>134.07</td><td>161.97</td><td>5123.53</td></tr><tr><td>IG/NIG</td><td>39%</td><td></td><td>3.2%</td><td></td></tr></table>

Table 17  
Number of rules generated by GARC and CBA

<table><tr><td></td><td>GARC</td><td>CBA</td></tr><tr><td>Anneal</td><td>72</td><td>533</td></tr><tr><td>Australian</td><td>17</td><td>1518</td></tr><tr><td>Auto</td><td>650</td><td>4505</td></tr><tr><td>Balance</td><td>4</td><td>147</td></tr><tr><td>Breast</td><td>21</td><td>21</td></tr><tr><td>Cleve</td><td>23</td><td>478</td></tr><tr><td>Crx</td><td>21</td><td>2686</td></tr><tr><td>Diabetes</td><td>11</td><td>40</td></tr><tr><td>German</td><td>78</td><td>1501</td></tr><tr><td>Glass</td><td>17</td><td>32</td></tr><tr><td>Heart</td><td>12</td><td>166</td></tr><tr><td>Hepatitis</td><td>23</td><td>700</td></tr><tr><td>Horse</td><td>26</td><td>988</td></tr><tr><td>Hypo</td><td>48</td><td>1557</td></tr><tr><td>Ionosphere</td><td>67</td><td>2891</td></tr><tr><td>Iris</td><td>7</td><td>14</td></tr><tr><td>Labor</td><td>15</td><td>52</td></tr><tr><td>Led7</td><td>33</td><td>533</td></tr><tr><td>Lenses</td><td>12</td><td>12</td></tr><tr><td>Lymph</td><td>17</td><td>2172</td></tr><tr><td>Monk2</td><td>2</td><td>397</td></tr><tr><td>Pima</td><td>6</td><td>21</td></tr><tr><td>Sick</td><td>56</td><td>1659</td></tr><tr><td>Sonar</td><td>16</td><td>883</td></tr><tr><td>Tic-tac-toe</td><td>26</td><td>200</td></tr><tr><td>Vehicle</td><td>112</td><td>3043</td></tr><tr><td>Vote</td><td>32</td><td>953</td></tr><tr><td>Waveform</td><td>25</td><td>3851</td></tr><tr><td>Wine</td><td>16</td><td>738</td></tr><tr><td>Zoo</td><td>90</td><td>2869</td></tr><tr><td>Mean</td><td>51.83</td><td>1205.33</td></tr><tr><td>GARC/CBA</td><td>4.3%</td><td></td></tr></table>

viously. Clearly, GARC generated much fewer rules than CBA, providing better understandability (at similar levels of accuracy). This can easily be verified by statistical significance tests. On average, the number of rules generated by GARC was only around 4.3% of that by CBA, according to the experiment.

## 5. Conclusions

Classification is one of the important issues in decision science and knowledge discovery. This paper has presented a new approach to discovering classification rules based on the concept of association rules. In doing so, the corresponding algorithm proposed, namely GARC, has integrated the generation of itemsets and rules, and incorporated information gain and certain conflicts/redundancy resolution strategies into the mining process. Finally, a compact set could be derived. Compared with other classifiers (e.g., CBA, C4.5-type, NN and SVM classifiers), the new approach could achieve a similar level of accuracy. Moreover, the experimental results have shown the advantages of GARC over CBA in terms of number of rules, and over SVM/NN in terms of explicit rules for use and explanation by decision makers. Future studies are centering on explorations of other optimization strategies so as to further improve the mining efficiency.

## Acknowledgements

This work was partly supported by the National Natural Science Foundation of China (79925001/ 70231010), and China’s MOE Funds for Doctoral Programs (20020003095).

## References

[1] R. Agrawal, R. Srikant, Fast algorithm for mining association rules, Proceeding of the 20th VLDB conference, Morgan Kaufmann, Santiago, Chile, 1994, pp. 487– 499.

[2] R. Agrawal, T. Imielinski, A. Swami, Database mining: a performance perspective, IEEE Transaction on Knowledge and Data Engineering 5 (1993) 914 – 925.

[3] R. Agrawal, T. Imielinski, A. Swami, Mining association rules between sets of items in large databases, Proceeding of 1993 ACM-SIGMOD International Conference on Management of Data, ACM Press, Washington, D.C., 1993, pp. 207 – 216.

[4] K. Ali, K. Manganaris, R. Srikant, Partial classification using association rules, Proceeding of the Third International Conference on Knowledge Discovery and Data Mining, The AAAI Press, Newport Beach, California, 1997, pp. 115 – 118.

[5] K. Alsabti, S. Ranka, V. Singh, CLOUDS: a decision tree classifier for large datasets, in: R. Agrawal, P. Stolorz, G. Piatetsky-Shapiro (Eds.), Proceeding of the Fourth Int. Conference on Knowledge Discovery and Data Mining, AAAI Press, Newport Beach, California, 1998, pp. 2 – 8 (New York, New York).

[6] D. Bertsimas, R.M. Freund, Data, Model, and Decisions: the Fundamentals of Management Science, South-Western College Publishing, 2000.

[7] L. Breiman, Classification and Regression trees, Wadsworth, Belmont, 1984.

[8] S. Brin, R. Motwani, J. Ullman, Dynamic itemset counting and implication rules for market basket data, Proceeding of 1997

ACM-SIGMOD International Conference on Management of Data, ACM Press, Tucson, Arizona, 1997, pp. 255 – 264.

[9] J. Catlett, Megainduction: Machine Learning on Very Large Databases. PhD thesis, University of Sydney, 1991.

[10] C.C. Chang, C.J. Lin, LIBSVM: a library for support vector machines, 2001.

[11] G.Q. Chen, Q. Wei, Fuzzy association rules and the extended mining algorithms, Information Sciences 147 (2002) 201 – 228.

[12] G.Q. Chen, Q. Wei, E. Kerre, Fuzzy data mining: discovery of fuzzy generalized association rules, in: G. Bordogna, G. Pasi (Eds.), Recent Research Issues on the Management of Fuzziness in Databases, Physica-Verlag (Springer), 1999.

[13] G.Q. Chen, Q. Wei, D. Liu, G. Wets, Simple association rules (SAR) and the SAR-based rule discovery, Computers and Industrial Engineering 43 (2002) 721 – 733.

[14] R. Duda, P. Hart, Pattern Classification and Scene Analysis, John Wiley and Sons, 1973.

[15] U.M. Fayyad, K.B. Irani, Multi-interval discretization of continuous-valued attributes for classification learning, Proceedings of the 13th International Joint Conference on Artificial Intelligence, 1993, pp. 1022– 1027.

[16] N. Friedman, D. Geiger, M. Goldszmidt, Bayesian network classifier, Machine Learning 29 (1997) 131 – 163.

[17] T. Fukuda, Y. Morimoto, S. Morishita, Data mining using twodimensional optimized association rules: scheme, algorithms, and visualization, Proc. of the 1996 ACM-SIGMOD Int’l Conf. on the Management of Data, 1996, pp. 12 – 13.

[18] Harshbarger,Thad R., Introductory Statistics: A Decision Map, Second edition. The City College, City University of New York, P 376, Macmillan Publishing Co., Inc. New York, Collier Macmillan Publishers, London, 1977.

[19] http://www.almaden.ibm.com/software/quest/Resources/data sets/syndata.html#classSynData.

[20] W. Li, J. Han, J. Pei, CMAR: accurate and efficient classification based on multiple class-association rules, ICDM 2001, IEEE Computer Society, San Jose, California, 2001, pp. 369 – 376.

[21] B. Liu, W. Hsu, Y. Ma, Integrity classification and association rule mining, in: R. Agrawal, P. Stolorz, G. Piatetsky-Shapiro (Eds.), Proceeding of the Fourth Int. Conference on Knowledge Discovery and Data Mining, AAAI Press, New York, New York, 1998, pp. 80 – 86.

[22] H.Y. Liu, J. Chen, G. Chen, Mining insightful classification rules directly and efficiently, Proceeding of the 1999 IEEE International Conference on Systems Man and Cybernetics, IEEE Computer Society, Tokyo, 1999, pp. 911 – 916.

[23] B. Liu, Y. Ma, C. Wong, Classification using association rules: weaknesses and enhancements, in: Vipin Kumar, et al., (Eds.), Data Mining for Scientific and Engineering Applications, 2001, p. 591.

[24] H. Lu, H. Liu, Decision tables: Scalable classification exploring RDBMS capabilities, Proceeding of the 26th International Conference on Very Large Databases, Morgan Kaufmann, Cairo, Egypt, 2000, pp. 373 – 384.

[25] M. Mehta, R. Agrawal, J. Rissanen, SLIQ: A fast scalable classifier for data mining, Proceeding of the Fifth Interna-

tional Conference on Extending Database Technology, Springer, Avignon, France, 1996, pp. 18 – 32.

[26] D. Meretakis, B. Wu¨thrich, Extending naı¨ve Bayes classifiers using long itemsets, Proceedings of 5th International Conference on Knowledge Discovery and Data Mining, San Diego, California, August 1999, 1999.

[27] C.J. Merz, P. Murphy, UCI Repository of Machine Learning Databases, 1996 (http://www.cs.uci.edu/\~mlearn/ MLRepository.html).

[28] A. Mueller, Fast Sequential and Parallel Algorithms for Association Rule Mining: A Comparison, 1995 (CS-TR-3515).

[29] G. Piatetsky-Shapiro, U. Fayyad, P. Smyth, From data mining to knowledge discovery, in: G. Piatetsky-Shapiro, U. Fayyad, P. Smyth (Eds.), An Overview. Advances in Knowledge Discovery and Data Mining, AAAI/MIT press, 1996, pp. 1 – 35.

[30] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, 1993.

[31] J. Roberto, J. Bayardo, Brute-force mining of high-confidence classification rules, Proceeding of the Third International Conference on Knowledge Discovery and Data Mining, AAAI Press, Newport Beach, California, 1997.

[32] J. Roberto, Bayardo Jr., R. Agrawal, D. Gunopulos, Constraint-based rule mining in large dense databases, Proc. of the 15th International Conference on Data Engineering, 1999, pp. 188– 197.

[33] J. Shafer, R. Agrawal, M. Mehta, SPRINT: A scalable parallel classifier for data mining, Proceeding of the 22nd VLDB Conference, Morgan Kaufmann, India, 1996, pp. 544 – 555.

[34] R. Srikant, Q. Vu, R. Agrawal, Mining association rules with item constraints, Proc. of the 3rd Int’l Conference on Knowledge Discovery in Databases and Data Mining, AAAI Press, Newport Beach, California, USA, 1997.

[35] S. Weiss, C. Kulikowski, Computer Systems that Learn: Classification and Prediction Methods from Statistics, Neural Nets, Machine Learning, and Expert Systems, Morgan Kaufman, 1991.

[36] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques with Java Implementations, Morgan Kaufmann, San Francisco, USA, 2000.

[37] M.J. Zaki, S. Parthasarathy, M. Ogihara, W. Li, New algorithms for fast discovery of association rules, American Association for Artificial Intelligence (1999).

Guoqing Chen received his PhD from the Catholic University of Leuven (K.U. Leuven, Belgium) and now is Professor of Information Systems at School of Economics and Management, Tsinghua University (Beijing, China). His research interests include Information Systems Management, Business Intelligence and Decision Support, and Soft Computing. Dr. Chen is member of ACM (SIG-MOD and SIGKDD) and AIS and has wide publications internationally including a monographic book on data modeling published by Kluwer Academic Publishers (Boston, 1998).

Hongyan Liu has received her PhD in Management Science from Tsinghua University, China. She is an associate professor in the Management Science and Engineering Department at Tsinghua University. Her current research interests include database and information system, data warehouse, knowledge discovery in database and bioinformatics.

Lan Yu has received his bachelor’s degree in Management Information Systems from the School of Economics and Management, Tsinghua University. He is a PhD candidate student in Management Science and Engineering Department at SEM. His current research interests focus on supervised learning (e.g., classification, reinforcement learning) and mainly apply them in finance and traffic domain.

Qiang Wei has received his PhD in Management Science from School of Economics and Management in 2003. He is an assistant professor in the Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, China. His current research interests include knowledge discovery, data mining techniques, management information systems, system simulations. He has been a lead author for papers that have appeared in Journal of Information Sciences, International Journal of Intelligent Systems, and Journal of Computer and Industrial Engineering.

Xing Zhang has received his bachelor’s degree in Management Information Systems from the School of Economics and Management, Tsinghua University. He is a PhD candidate student in Management Science and Engineering Department at SEM. His research interests focus on classification, reinforcement learning, and data mining techniques.
