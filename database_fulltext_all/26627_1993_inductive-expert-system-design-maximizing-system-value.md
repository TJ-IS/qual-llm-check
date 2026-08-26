---
otero_id: 26627
otero_key: "XGJ9BJW5"
title: "Inductive Expert System Design: Maximizing System Value"
authors: "Vijay S. Mookerjee; Brian L. Dos Santos"
year: "1993"
journal: "Information Systems Research"
doi: "10.1287/isre.4.2.111"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [137.189.171.235] On: 18 October 2016, At: 20:11 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HSR

## Information Systems Research

![](/api/attachments/XGJ9BJW5/fulltext/images/d06cdb818efdaf44d243c2ae2960559cfcbb6f91f8360312151ff0e2abff01d1.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Inductive Expert System Design: Maximizing System Value

Vijay S. Mookerjee, Brian L. Dos Santos,

## To cite this article:

Vijay S. Mookerjee, Brian L. Dos Santos, (1993) Inductive Expert System Design: Maximizing System Value. Information Systems Research 4(2):111-140. http://dx.doi.org/10.1287/isre.4.2.111

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1993 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/XGJ9BJW5/fulltext/images/11dac66552daa499f13d5d7ab5c597f99ad0555ff0c0b1112e4082feb3f3693f.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Inductive Expert System Design: Maximizing System Value

Vijay S. Mookerjee

School of Business

Universıty of Washington

Seattle, Washington 9819

Brian L. Dos Santos

College of Business and Public Administration

Universıty of Louisville

Louisville, Kentucky 40292-0001

There is a growing interest in the use of induction to develop a special class of expert systems known as inductive expert systems. Existing approaches to develop inductive expert systems do not attempt to maximize system value and may therefore be of limited use to firrns We present an induction algorithm that seeks to develop inductive expert systems that maximize value. The task of developing an inductive expert system is looked upon as one of developing an optimal sequential information acquisition strategy. Information is acquired to reduce uncertainty only if the benefits gained from acquiring the information exceed its cost. Existing approaches ignore the costs and benefits of acquiring information. We compare the systems developed by our algorithm with those developed by the popular ID3 algorithm. In addition, we present results from an extensive set of experiments that indicate that our algorithm will result in more valuable systems than the ID3 algorithm and the ID3 algorithm with pessimistic pruning.

Inductive expert systemns—Information costs and benefits--Economic expert system design-Economics of machine learning

## 1. Introduction

he use of computer-based systems (CBS) to support management decision making has received considerable attention over the past three decades. Much of the early work in this area focused on the use of operations research models, data base management and the development of better user interfaces to support managers. More recently, however, there have been attempts to use artificial intelligence (AI) techniques to develop CBS that are able to replicate decisions made by human experts. Successful development of such systems could be extremely valuable. They could provide managers with easy access to expertise in some domains, reduce dependence on human experts and reduce the costs of acquiring expertise.

Expert systems (ES), the name given to these CBS, have recently received considerable attention in the academic literature and business press, and numerous commercial products now are available to help organizations develop such systems. Like much of the AI research, the primary objective in ES research has been to develop systems that perform at the level of human experts. Consequently, these systems attempt to maximize solution accuracy: i.e., maximize the number of cases in which the output (decision, recommendation) provided by the system is similar to that provided by human experts. The costs of using such systems, are, for the most part ignored (Turban 1993, Olson and Courtney 1992).'

In this paper, we focus on expert systems that support classification tasks, i.e., systems that attempt to classify an object as one of n categories. Expert systems can provide many benefits to an organization (Holsapple and Whinston 1987). For example, decisions can be more timely, decisions are more consistent, expertise is easily transferred, etc. Here, we consider only those benefits that are directly derived from the classification problems that the system is called upon to solve. In this context, the benefits of an ES (solution value) are determined by the system's ability to correctly classify objects and the value of correct and incorrect classification. Specifically, solution value is determined by the benefits of correctly classifying objects and the costs of incorrect classification. Hereafter, classification benefits and costs are referred to as classification costs, wherein correctly classifying an object results in negative classification costs, while incorrectly classifying objects results in positive classification costs. For example, a system that supports loan processing may allow two types of correct classifications: granting a loan when it should have been granted and, not granting a loan when it should not have been granted. Similarly, there may be two incorrect classifications: granting a loan when it should not have been granted and not granting a loan when it should have been granted. The sum of these classification costs for all the problems the system is called upon to solve, is the solution value.

To obtain solution value, costs are incurred. The costs include a fixed and a variable component. Fixed costs include costs of developing the system, such as time, money, materials, etc. Variable costs include information costs and computing costs incurred when the system is in use. Computing costs include the costs of the computing resources required to obtain a classification. Information costs are the costs of obtaining the information that a user of the system must provide before the system can arrive at a classification. For example, consider a system developed to support medical diagnosis. Information costs include the costs of conducting clinical tests that may be necessary for the system to arrive at a diagnosis. The cost of obtaining all the information that the system needs to solve all the problems it is presented with, is the solution cost.²

Therefore, the value of an ES to an organization (system value) is determined by the benefits (solution value) derived from the system's solutions, and the costs (solution costs) incurred in using the system to obtain these solutions.³ Profit-seeking organizations should attempt to design systems that maximize system value. Yet, the research to date emphasizes designs that attempt to maximize solution accuracy (Dos Santos and Mookerjee 1993; Jacob et al. 1988, 1989). The emphasis on solution accuracy, rather than system value, is not uncommon in other research areas that attempt to improve management decision making. For example, much of the research in management science focuses on the development and/or selection of algorithms based on computational complexity or worst-case analysis (Balakrishnan and Whinston 1991). Little attention is paid to the costs of acquiring the information that these algorithms need. There often is a tradeoff between the quality of the solutions and the cost of the information necessary to arrive at these solutions.

The fact that ES research does not seek to maximize system value has not gone unnoticed, and, theoretical and practical solutons have been proposed for specific cases (Hall et al. 1986, Dos Santos and Mookerjee 1993). Dos Santos and Mookerjee (1993), for example, show how the value of an existing expert system can be increased by redesigning the system to reduce information acquisition costs. Past efforts, however, have primarily dealt with the design of expert systems that use the traditional expert system architecture, wherein the system knowledge (knowledge base) is separated from its processing mechanism (inference engine).

Recently, expert systems using a different architecture have attracted considerable attention (Michalski 1986, Michie 1983). These systems, known as inductive expert systems, are developed using an induction algorıthm. An induction algorithm develops classification rules that can be used to determine the class of an object from its description, i.e., from the object's attributes. The classification rules developed by these algorithms can be depicted as a decision tree in which the nonleaf nodes of the tree prescribe inputs that must be observed, and the arcs represent values that the input variables can take. Leaf nodes in the tree indicate how an object is to be classified. Induction algorithms build such a tree from a set of preclassified cases referred to as the traintng set. It is computationally infeasible to find a decision tree of minimum size that is consistent with every case in the training set (Hyafil and Rivest 1976). As a result, greedy heuristics have been developed to generate these classification rules (Pearl 1984). In a greedy heuristic. an action is taken (i.e., an input is observed) based onlv upon its immediate effects (i.e., the state after observing the input).

Existing induction algorithms are unlikely to result in systems that maximize system value (Dos Santos and Mookerjee 1992). These algorithms implicitly assume that the inputs needed to classify an object are free. Often, such an assumption is unreasonable. For example, consider an expert system that processes commercial loans. Information needed by the system to arrive at a decision may include credit history, projected financial ratios, audit information, and so on. Obtaining this information can be costly. Therefore, if input costs are ignored when designing such a system, it is unlikely to maximize system value. Another aspect of system value that is neglected in the design of inductive expert systems is classification costs. Induction algorithms attempt to maximize classification accuracy, i.e., maximizing the number of correct classifications. The implicit assumption is that classification errors are equally costly. In the loan example, this is equivalent to assuming that making a bad loan is just as costly as not making a good loan. Maximizing classification accuracy will maximize solution value if correct classification costs (i.e., benefits) are equal and incorrect classification costs are equal. If' these costs vary, it is unlikely that maximizing accuracy will maximize solution value.

Designers of CBS have little theory to guide their design efforts. Much of a designer's work is based on rules-of-thumb The decision making model proposed by

Moore and Whinston (1986, 1987) provides a theoretical basis for the design of systems that acquire information sequentially. Their model is cost-benefit driven, based upon classical decision theory. The Moore and Whinston (M&W) model is the basis for a number of papers that deal with problems in different design contexts (Jacob et al. 1989, Moore et al. 1990, Balakrishnan et al. 1991, Moore et al. 1992). The work reported here also draws upon the M&W model. The proposed induction algorithm generates a decision tree that causes information to be acquired only if its value exceeds its cost. However, this work differs from earlier work in two significant ways: (1) it is the first to deal with the design of inductive expert systems, and (2) it is the first to empirically determine whether designs based on the M&W model result in better systems than those based upon previous design methods. A simulation study, involving a series of experiments, were conducted to compare the performance of the proposed algorithm with that of other induction algorithms. Results indicate that use of the proposed algorithm will result in greater system value than will the use of the popular ID3 algorithm (Quinlan 1986) and the ID3 algorithm with pessimistic pruning (Quinlan 1987).

This rest of this paper is organized as follows. In §2, the criteria used to evaluate induction algorithms are described and the factors that are important in the design of induction algorithms are discussed. In §3, the value-based (VB) induction algorithm is described. In §4, we show how differences in the design of the VB algorithm and the ID3 algorithm will affect systems that are designed with these algorithms. In §5, we describe a simulation study that compares the performance of the VB algorithm to two popular induction algorithms. A summary and conclusions are provided in §6.

## 2. Inductive Systems Research

In this section, we describe the criteria that have been used to evaluate inductive expert systems. We also discuss the key factors in the design of an induction algorithm and briefly review the literature in this context.

## 2.1. Evaluation Criteria

Induction algorithms generate a set of classification rules that can be rcpresented as a decision tree. These rules are generated from a set of training cases (i.e., the training data set) that include potentially relevant attributes of objects and the object's class. Different measures have been used to evaluate induction algorithms. Mingers (1989) proposes three measures: (a) accuracy, (b) understandability, and (c) size. These measures are related to the decision tree generated by the algorithm,

Accuracy is a measure of how well the decision tree is able to classify objects in a test data set. The test data set typically includes cases that are not in the training data. Accuracy is most commonly measured as the proportion of incorrect classifications in the test cases. Measured in this way, accuracy does not indicate how well the system predicts the different classes in the data. Hence, if classification costs differ across classes, increasing accuracy may not increase solution value. Accuracy measures that take into account the different classes in the data set are seldom used (Titterington et al. 1981).

An objective in expert systems design is to represent knowledge so that it can be easily understood. Decision trees can be difficult to understand (Cendrowska 1987). However, understandability is difficult to measure. Hence, this measure is used to contrast trees generated by different algorithms only when everything else about the trees is the same (Mingers 1989).

There is general agreement that smaller trees are more understandable (Quinlan 1986, Mingers 1986, Shepherd 1983, Kononenko et al. 1984). Moreover, the accuracy of induced decision trees often falls with an increase in size (Mingers 1989). Hence, minimizing the size of induced trees often is a design objective. The size of a tree may be measured in different ways, such as, the number of leaves in the tree (Mingers 1989), the number of nodes in the tree (Quinlan 1987), and the average rule size (i.e., the average number of nodes in a path in the tree) (Niblet and Bratko 1986). However, reducing the size of a tree may not reduce solution costs. A reduction in size will reduce the number of inputs required to classify an object and hence, reduce computing costs. However, if inputs are not equally costly, the use of fewer inputs may not reduce information costs.

This leads us to conclude that the criteria used to evaluate inductive expert systems fail to emphasize system value and, consequently, may result in systems that are less valuable than they could be. We next describe the design features of a typical induction algorithm and discuss whether these features are likely to result in systems that maximize value.

## 2.2. Algorithm Design Considerations

Induction algorithms develop a decision tree by incrementally creating nonleaf nodes and leaf nodes in the tree. Nonleaf nodes are labeled by input names. The input chosen to label a nonleaf node is determined using an input selection criterion and a set of cases. Once a nonleaf node has been labeled, q outgoing arcs are created at this node, where $q$ is the number of possible states of the input used to label the node. Each of the q arcs is labeled by a possible state of the input used to label the node. The set of cases used to label the node (for the root node this is the entire training set) is then partitioned into q subsets such that the state of the input used to label the node is the same within each subset. The tree can grow along each outgoing arc using the subset of cases corresponding to the state of the input used to label the arc. Creation of nonleaf nodes continues along each path of the tree until a stopping condition is reached, at which stage a leaf node is created. Leaf nodes are labeled using a classification function.

Formally, the induction process can be described using the following definitions: Let

D represent the set of cases in the training set,

$X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ are n observable input variables that may be used to classify an object,

$\boldsymbol { \mathscr { X } } _ { t } \mathrm { ~ } _ { 1 } , \boldsymbol { \mathscr { X } } _ { \iota 2 } , \mathrm { ~ } . \mathrm { ~ \mathscr ~ \cdot ~ } \mathrm { ~ \mathscr ~ \cdot ~ } \mathrm { ~ \mathscr { X } } _ { \iota q }$ are q possible states for input $X _ { \iota }$

$c _ { 1 } , c _ { 2 } , \ldots , c _ { m }$ are m possible ways in which an object can be classified.

$L \subseteq D$ is a subset of cases in the training set; referred to as the “current set,"

$k ( L )$ is a classification function that determines how a leaf node is labeled,

$g ( X , \ell )$ is a criterion value for input $X _ { i }$ given L, and

w is a cut-off value that is used to determine when a leaf node should be created.

The steps in an induction algorithm are described below. Initially, no nodes have been created.

Step 1. Set $L = D$

Step 2. Using $L .$ , select input $X _ { \ j }$ such that, $g ( X , L ) \geq g ( X _ { \iota } , L )$ , for $i = 1 , 2 , \dots , n$ ${ \mathfrak { I f } } g ( X _ { \prime } , L ) \leq w , \mathbf { g } \mathbf { o }$ to Step $^ { 5 , }$

Step 3. Create a nonleaf node labeled $X _ { \ j } .$ . Generate q arcs originating at this node. Label each arc by a state of the input $X _ { \ j }$ . Assuming q states for each input, arcs are labeled $x _ { \iota k } , \mathrm { f o r } k = 1 , 2 , \ldots , q .$

Step 4. For each arc $x _ { \ j k }$ determine $M \subseteq L$ , such that $X _ { \ j } = x _ { \ j \star }$ for every case in M. Set $L = M .$ . Go to Step 2.

Step 5. Create a leaf node. Label this leaf node $c _ { \lambda }$ such that $k ( L ) = c _ { \lambda }$ where $c _ { \lambda } \in \{ c _ { 1 } , c _ { 2 } , \ldots , c _ { m } \}$

Step 6. If leaf nodes have been created in all paths of the tree, stop; else, return to Step 4.

There are three important factors that must be considered in the design of an induction algorithm: (a) the input selection criterion, (b) the stopping rule, and (c) the classification function. The input selection criterion determines how, from a set of candidate inputs, an input is chosen to label a nonleaf node. The stopping rule determines when it is no longer beneficial to create nonleaf nodes in a path of the tree, and the classification function determines how a leaf node should be labeled. We elaborate on these factors below.

2.2.1. Input Selection Criterion. An induction algorithm uses some criterion to choose an input to label a nonleaf node. To begin, using the current set of cases $L$ (equal to D in this case), the input selection criterion is used to label the root node of the tree. For example, given $L _ { \textrm { : } }$ , the input $X _ { \ j }$ with the highest criterion value may be selected to label the root of the tree, i.e., $X ,$ is selected such that for all $i , g ( X , L )$ $\geq g ( X , L )$ . The same criterion is then used to identify inputs that label other nonleaf nodes in the tree.

Generally, the input selection criterion determines how well a particular input splits the various classes in the data. Quinlan (1979, 1983), for example, proposed the use of the entropy measure from information theory (Shannon and Weaver 1949). The input with the greatest information content is used to label a nonleaf node. Mingers (1986, 1987) proposed an input selection criterion based on the Chisquare statistic. It measures the likelihood that an input influences the outcome $( \mathrm { i . e . , }$ the classification). Numerous other measures have been proposed. Most of these measures are based on the information content of inputs (Mingers 1989).

Although the information content of an input is indicative ofits ability to discriminate among the different classes, the information acquisition costs must be considered to achieve a cost-effective design. A costly input that discriminates very well may be less cost-effective than one that has less discrimination power, but is much cheaper. Since induction algorithms do not consider costs or benefits of inputs, the value of systems developed using these algorithms may be adversely affected.

2.2.2. Stopping Rule. In many induction algorithms, an input is not used to label a node if its contribution to the objective does not exceed a cut-off value. Formally stated,

$$
\text { if   } g (X _ {j}, L) \leq w, \text {   then   } X _ {j} \text {   should   not   be   used   to   label   the   current   node. }
$$

At any stage, if all candidate inputs fail to exceed the cut-off value, creation of nonleaf nodes is terminated and a leaf node is created. In the ID3 algorithm (Quinlan 1986), $g ( X _ { J } , L )$ measures the reduction in information entropy provided by the input $X _ { \ j }$ for the set of cases in L. In ID3, w' equals zero, i.e., if none of the available inputs reduces information entropy, a leaf node is created

The stopping rules used in induction algorithms have not considered costs and benefits (Mingers 1989). Therefore, it is likely that nonleaf nodes will continue to be created even though they may not be cost-effective. To maximize system value, the stopping rule should consider the costs and benefits of observing an input. A nonleaf node should not be created if none of the candidate inputs has benefits that exceed its cost.

2.2.3. Classification Function. The classification function determines how a leaf node should be labeled. In many algorithms, the class that minimizes the probability of a classification error is used to label a leaf node. For example, in the ID3 algorithm (Quinlan 1986), a leaf node is labeled $c _ { \lambda }$ using a classification function $k ( L )$ such that

$$
f (c _ {\lambda}, L) \geq f (c _ {i}, L), \quad i = 1, 2, \dots , m,
$$

where, $f ( c , , L )$ is the proportion of cases in L with class $c _ { \iota }$ . Minimizing the probability of a classification error will maximize solution value only under certain circumstances, (e.g., if correct classification costs are equal and incorrect classification costs are equal). Frequently, a classification function that emphasizes accuracy will adversely affect solution value.

## 2.3. Summary

Judging from the criteria used to evaluate inductive systems, it is apparent that current induction algorithms do not attempt to maximize system value. Furthermore, the nature of the input selection criterion, stopping rule and classification function used in existing algorithms suggests that these algorithms are unlikely to maximize value. In the next section, we describe the Value-Based induction algorithm (VB) and use an example to demonstrate how the algorithm works.

## 3. The Value-based Induction Algorithm

This algorithm is based upon the sequential information acquisition paradigm (Marschak and Radner 1972, Moore and Whinston 1986, 1987). A decision maker can acquire information about a set of observable variables (e.g., results of clinical tests) in order to make a decision about an unobservable state of nature (e.g., the presence of a particular disease). A decision strategy consists of two components: (a) an information acquisition strategy, which specifies which input should be observed given the information already known to the decision maker, and (b) a decision rule, which determines the decision (action) that the decision maker should take. A decision strategy can be represented as a decision tree: nonleaf nodes specify what information should be acquired at any stage, and leaf nodes specify the decision or action to take, given the information that has been obtained.

An optimal decision strategy (tree) is one that maximizes the difference between the value generated by using the decision rule and the cost of information necessary to make a decision. To derive an optimal decision strategy, a decısion maker must trade-off the increase in value resulting from additional information (therefore, making better decisions) and the cost of acquiring the information. The input selection criterion, stopping rule and classification function in the VB algorıthm are designed to make this trade-off.

## 3.1. The VB Algorithm

Here, we describe the input selection criterion, stopping rule and classification function used in the algorithm. Let

$L =$ the current set of cases. Initially, $L = D$

$Z ( { \cal X } _ { r } )$ = the information acquisition cost of input $X _ { r }$

$C ( c _ { \iota } , c _ { \jmath } )$ = the cost of classifying an object of class $c _ { \imath }$ as class $c _ { y } . \mathbf { I f } i = j$ , the obiect is correctly classified, and

$f ( c _ { \iota } , L ) =$ the proportion of cases in L belonging to the class $c _ { \iota }$ . It is an estimate of the probability of class $c _ { \iota }$ , given the information already gathered, i.e., information that has resulted in $L$

The best single leaf tree (i.e., a tree consisting of one leaf node and no nonleaf nodes) has its leaf node labeled $c _ { \lambda } .$ , such that this class minimizes expected classification costs $\operatorname { E C } ( L )$ . The class $c _ { \lambda }$ is selected as that class whose value is $\operatorname { E C } ^ { * } ( L )$ , determined as follows:

$$
\operatorname{EC} ^ {*} (L) = \underset {J} {\operatorname{Min}} \left[ \sum_ {i = 1} ^ {m} f \left(c _ {i}, L\right) C \left\{c _ {i}, c _ {j} \right\} \right] = \sum_ {i = 1} ^ {m} f \left(c _ {i}, L\right) C \left\{c _ {i}, c _ {\lambda} \right\}.
$$

If two or more classes have the same value for $\mathbf { E C } ^ { * } ( L )$ , one is arbitrarily chosen

Consider the case where a single leaf tree is not created. Let the root node be labeled $X _ { r } .$ The label of the best leaf node at the end of the arc $x _ { r k }$ is determined by

$$
\operatorname{EC} ^ {*} (L \mid X _ {r} = x _ {r k}) = \underset {j} {\operatorname{Min}} \left[ \sum_ {i = 1} ^ {m} f \left(c _ {i}, L \mid X _ {r} = x _ {r k}\right) C \left\{c _ {i}, c _ {j} \right\} \right],
$$

where $( L | X _ { r } = x _ { r k } )$ are the cases in $L$ for which $X _ { r } = x _ { r k }$ . If a root node labeled $X _ { r }$ has $\pmb q$ arcs, then the expected classification cost if $X ,$ is observed, is

$$
\mathrm{EC} ^ {*} (L \mid X _ {r}) = \sum_ {k = 1} ^ {q} h (X _ {r} = x _ {r k}, L) \mathrm{EC} ^ {*} (L \mid X _ {r} = x _ {r k}),
$$

where $h ( X _ { r } = x _ { r k } , L )$ is the proportion of cases in L for which $X _ { r } = x _ { r k }$ . Hence, the benefit of labeling the root node $X _ { r }$ is given by

$$
\Delta \mathrm{EC} ^ {*} (L | X _ {r}) = \mathrm{EC} ^ {*} (L) - \mathrm{EC} ^ {*} (L | X _ {r}).
$$

The input selection criterion $g ( X _ { r } , L )$ is

$$
g (X _ {r}, L) = \left\{ \begin{array}{l l} \Delta \mathrm{EC} ^ {*} (L | X _ {r}) / Z (X _ {r}), & \text { if } Z (X _ {r}) \neq 0, \\ \Delta \mathrm{EC} ^ {*} (L | X _ {r}), & \text { if } Z (X _ {r}) = 0. \end{array} \right.
$$

In the VB algorithm, the input $X ,$ with the highest value for $g ( X _ { r } , L )$ is selected to label a nonleaf node. When $Z ( X _ { r } ) \neq 0 , g ( X _ { r } , L )$ is a measure of the benefit per unit cost of observing $X _ { r }$ . Otherwise, $g ( X , L )$ measures the benefit of observing $X _ { r }$ . The VB algorithm chooses the input with the highest criterion value to label a nonleaf node. An input with a nonzero input cost may be used as a label $\mathrm { i } \mathbf { f } g ( X _ { r } , L ) > 1 . \mathbf { A }$ free input may be used as a label if $g ( X , L ) > 0$

The stopping rule in the VB algorithm can be described as follows. The VB algorithm creates a leaf node if:

(a) for all inputs for which $Z ( X _ { r } ) \neq 0 , g ( X _ { r } , L ) \leq 1$ , and

(b) for all inputs for which $Z ( X _ { r } ) = 0 , g ( X _ { r } , L ) \leq 0$

When a stopping condition occurs, a leaf node is created. The classification function in the VB algorithm labels a leaf node with the class that minimizes expected classification cost. Formally, $k ( L ) = c _ { \lambda }$ , such that

Inductive Expert System Design: Maximizing System Value

<table><tr><td colspan="6">TABLE 1A Training Data Set</td></tr><tr><td rowspan="2">Case #</td><td colspan="4">Object&#x27;s Attributes (Inputs)</td><td rowspan="2">Object Classification</td></tr><tr><td> $\lambda_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td> $X_4$ </td></tr><tr><td>1</td><td> $T$ </td><td> $F$ </td><td> $F$ </td><td> $F$ </td><td> $Y$ </td></tr><tr><td>2</td><td> $F$ </td><td> $T$ </td><td> $T$ </td><td> $T$ </td><td> $Y$ </td></tr><tr><td>3</td><td> $T$ </td><td> $F$ </td><td> $F$ </td><td> $T$ </td><td> $N$ </td></tr><tr><td>4</td><td> $T$ </td><td> $F$ </td><td> $T$ </td><td> $T$ </td><td> $N$ </td></tr><tr><td>5</td><td> $F$ </td><td> $T$ </td><td> $F$ </td><td> $F$ </td><td> $Y$ </td></tr><tr><td>6</td><td> $T$ </td><td> $T$ </td><td> $T$ </td><td> $F$ </td><td> $N$ </td></tr></table>

$$
\mathrm{EC} ^ {*} (L) = \sum_ {i = 1} ^ {m} f (c _ {i}, L) C \left\{c _ {i}, c _ {\lambda} \right\}.
$$

## 3.2. An Example

To show how the VB algorithm works, we use the training set in Table 1. In this training set, there are four inputs, each of which can take the values T or F. Objects are classified as Y or N. The input and classification costs are shown in Table 2 (Panels A and B respectively). Initially, L consists of the six cases in Table 1.

The classification cost without gathering any information is

$$
\begin{array}{r l} \mathrm{EC} ^ {*} (L) & = \operatorname{Min} [ \left\{f (Y, L) C \left\{Y, Y \right\} + f (N, L) C \left\{N, Y \right\} \right\}, \\ & \quad \left\{f (Y, L) C \left\{Y, N \right\} + f (N, L) C \left\{N, N \right\} \right] \\ & = \operatorname{Min} [ \left\{0. 5 ^ {*} (- 1 0) + 0. 5 ^ {*} (1 5) \right\}, \left\{0. 5 ^ {*} (5) + 0. 5 ^ {*} (- 5) \right\} ] \\ & = 0. \end{array}
$$

The least classification cost of a single leaf tree is 0. 'The leaf node in this tree is labeled N, i.e., all objects would be classified as N, if no information is gathered.

(osts Associated with the Traıning Data in Table 1  
TABLE 2

<table><tr><td>Input</td><td>Panel AInput Costs</td><td>Cost</td></tr><tr><td> $X_1$ </td><td></td><td>3.00</td></tr><tr><td> $X_2$ </td><td></td><td>0.50</td></tr><tr><td> $X_3$ </td><td></td><td>0.75</td></tr><tr><td> $X_4$ </td><td></td><td>1.00</td></tr><tr><td>Classification</td><td>Panel BClassification Costs</td><td>Cost</td></tr><tr><td> $\{Y, Y\}$ </td><td></td><td>-10.0</td></tr><tr><td> $\{Y, N\}$ </td><td></td><td>50</td></tr><tr><td> $\{N, Y\}$ </td><td></td><td>150</td></tr><tr><td> $\{N, N\}$ </td><td></td><td>-5.0</td></tr></table>

TABLE 3  
Splutting of Cases in Table 1 If Input $X _ { 2 }$ Is Selected

<table><tr><td colspan="5">Panel ASubtable for  $X_{2} = T$ </td></tr><tr><td rowspan="2">Case #</td><td colspan="3">Inputs</td><td rowspan="2">Object Classification</td></tr><tr><td> $X_{1}$ </td><td> $X_{3}$ </td><td> $X_{4}$ </td></tr><tr><td>2</td><td>F</td><td>T</td><td>T</td><td>Y</td></tr><tr><td>5</td><td>F</td><td>F</td><td>F</td><td>Y</td></tr><tr><td>6</td><td>T</td><td>T</td><td>F</td><td>N</td></tr><tr><td colspan="5">Panel BSubtable for  $X_{2} = F$ </td></tr><tr><td rowspan="2">Case #</td><td colspan="3">Inputs</td><td rowspan="2">Object Classification</td></tr><tr><td> $X_{1}$ </td><td> $X_{3}$ </td><td> $X_{4}$ </td></tr><tr><td>1</td><td>T</td><td>F</td><td>F</td><td>Y</td></tr><tr><td>3</td><td>T</td><td>F</td><td>T</td><td>N</td></tr><tr><td>4</td><td>T</td><td>T</td><td>T</td><td>N</td></tr></table>

Next, it is necessary to compare the expected cost of this single leaf tree with that of a tree which uses some inputs to classify objects. To determine how the root of such a tree should be labeled, we determine how much classification costs would be reduced if each one of the four inputs were used to label the root node. In the example, if $X _ { 2 }$ is used to label the root node, two outgoing arcs have to be created from this root node, one for each of the two possible states of input $X _ { 2 }$ . The training set is then split into two subsets, one for each outgoing arc, based upon the values for $X _ { 2 }$ in each of the cases. These two subsets are shown in Table 3 (Panels A and B).

The least classification cost of leaf nodes created at the end of the arcs $X _ { 2 } = T$ and $X _ { 2 } = F$ is

$$
\mathrm{EC} ^ {*} (L \mid X _ {2} = T) = - \frac {5}{3} \quad \text { and } \quad \mathrm{EC} ^ {*} (L \mid X _ {2} = F) = - \frac {5}{3}.
$$

Hence,

$$
\mathrm{EC} ^ {*} (L \mid X _ {2}) = 0. 5 0 ^ {*} \left(- \frac {5}{3}\right) + 0. 5 0 ^ {*} \left(- \frac {5}{3}\right) = - \frac {5}{3}
$$

and

$$
\Delta \mathrm{EC} ^ {*} (L | X _ {2}) = 0 - \left(- \frac {5}{3}\right) = \frac {5}{3};
$$

$$
\therefore g (L \mid X _ {2}) = \frac {\Delta \mathrm{EC} ^ {*} (L \mid X _ {2})}{Z (X _ {2})} = \frac {5}{3} \times \frac {1}{0 . 5} = \frac {1 0}{3}.
$$

Similarly, $g ( L \vert X _ { 1 } ) = 5 / 3 ; g ( L \vert X _ { 3 } ) = 2 0 / 9 ;$ and $g ( L | X _ { 4 } ) = 5 / 3$ . Since $X _ { 2 }$ has the largest criterion value $( 1 0 / 3 )$ and this value is greater than 1, the root of the tree is labeled $X _ { 2 } , \mathbf { A }$ decision tree with $X _ { 2 }$ as the root node and two leaf nodes Y and N (corresponding to the arcs $X _ { 2 } = T$ and $X _ { 2 } = F )$ has a greater value (lower classification cost) than the single leaf tree that classifies all objects as N.

Having labeled the root node, two arcs emerging from the root are created and labeled. The cases in the training set are split into two subsets. One subset includes cases in the training set for which $X _ { 2 } = T$ , and the other subset includes those cases for which $X _ { 2 } = F$ . Using each of these two subsets, the above process is repeated.

Consider the arc $X _ { 2 } = T$ . The least classification cost for a leaf node at the end of this arc is

$$
\mathrm{EC} ^ {*} (L \mid X _ {2} = T) = \operatorname{Min} \left[ \frac {(- 2 0 + 1 5)}{3}, \frac {(1 0 + 5)}{3} \right] = - \frac {5}{3}.
$$

If, instead of creating a leaf node at the end of the above arc $( X _ { 2 } \ \simeq \ T )$ , we create a nonleaf node, the node can be labeled $X _ { 1 } , X _ { 3 }$ or $X _ { 4 }$ . If the node is labeled $X _ { t }$ , two arcs will result: $X _ { 1 } = T$ , and $X _ { 1 } = F$ . The least classification cost for leaf nodes at the end of these arcs are

$$
\mathrm{EC} ^ {*} (L \mid X _ {2} = T \wedge X _ {1} = T) = - 5 \quad \text { and } \quad \mathrm{EC} ^ {*} (L \mid X _ {2} = F \wedge X _ {1} = T) = - 1 0.
$$

Hence,

$$
\mathrm{EC} ^ {*} (L \mid X _ {2} = T, X _ {1}) = \left(\frac {1}{3}\right) (- 5) + \left(\frac {2}{3}\right) (- 1 0) = - \frac {2 5}{3},
$$

$$
\Delta \mathrm{EC} ^ {*} (L \mid X _ {2} = T, X _ {1}) = \left(- \frac {5}{3}\right) - \left(- \frac {2 5}{3}\right) = \frac {2 0}{3},
$$

$$
\therefore g (X _ {1}, L \mid X _ {2} = T) = \frac {2 0}{3} \times \frac {1}{3} = \frac {2 0}{9}.
$$

Similarly, the input selection criterion values for $X _ { 3 }$ and $X _ { 4 }$ are

$$
g (X _ {3}, L \mid X _ {2} = T) = \frac {2 0}{9} \quad \text { and } \quad g (X _ {4}, L \mid X _ {2} = T) = \frac {5}{3}.
$$

Since the benefit to cost ratios are greater than one, the arc originating from $X _ { 2 }$ for which $X _ { 2 } \ = \ T$ , will terminate at a nonleaf node. Since $X _ { \mathfrak { r } }$ and $X _ { 3 }$ have the same criterion value, one is arbitrarily chosen. This process continues until leaf nodes in all paths of the tree are created. For this example, the decision tree constructed by the VB algorithm is shown in Figure 1.

## 4. Differences in System Designs: VB and ID3

A majority of the proposed induction algorithms are based on the ID3 algorithm. The ID3 algorithm uses an information-theoretic evaluation function to select inputs. A classification is made when none of the candidate inputs provide any useful information to classify objects. ID3 attempts to minimize classifications errors. In this section, we show how the VB and ID3 algorithms result in different system designs even under conditions where it may appear that there will be no differences Since the input selection mechanism, stopping rule and classification function affects the structure of the decision trees created by an induction algorithm, we show how these differences can affect the resulting decision trees.

![](/api/attachments/XGJ9BJW5/fulltext/images/8a2291d8251c9f2a61f2e7dc51cedcd142efab266f10889bd8f8edbdc883a29e.jpg)  
FiGURE 1. Tree Generated by the VB Algorithm Using the Training Set in Table 1.

## 4.1. Input Selection

If classification costs are of equal magnitude, minimizing classification errors will maximize solution value.4 When inputs are equally costly, they should be selected to label nonleaf nodes so as to minimize the likelihood of errors. Under such conditions, it may appear that the VB and ID3 algorithms will select the same inputs to label nonleaf nodes. Such is not the case, as the following example demonstrates.

Figure 2 shows an example in which the training data set has 18 cases in which 8 objects are of class Y and 10 objects are of class $N$ . There are two inputs: $X _ { 1 }$ and $X _ { 2 }$ that have equal (nonzero) information acquisition costs. Assume the classification costs $( C \{ Y , Y \} , C \{ Y , N \} , C \{ N , Y \} , C \{ N , N \} )$ ) are of equal magnitude, say $\pm \$ 1$

4.1.1. ID3 Algorithm. The input selection criterion used in ID3 is based upon the following measure of information entropy (Shannon and Weaver 1949):

$$
I _ {E} = - \sum_ {i} f _ {i} \mathrm{Log} (f _ {i}).
$$

In the ID3 algorithm $\mathcal { I } _ { \iota }$ is a frequency estimate of the probability of the ith class, and Log is the base 2 logarithm. Therefore, in the example, the initial information entropy, $I _ { E } ( \phi )$ , is

![](/api/attachments/XGJ9BJW5/fulltext/images/a1d49276f27650a3c48700781fa1a07f99dedd757488fac90beccddbebaa5cfb.jpg)  
FiGURE 2. Example to Study Differences in Input Selection Behavior Between VB and ID3.

$$
I _ {E} (\phi) = - \left\{\frac {8}{1 8} \operatorname{Log} \left(\frac {8}{1 8}\right) + \frac {1 0}{1 8} \operatorname{Log} \left(\frac {1 0}{1 8}\right) \right\} = 1. 0.
$$

If input $X _ { \mathfrak { i } }$ is observed.

$$
\begin{array}{r l} I _ {E} (X _ {1}) = - \left\{\frac {6}{1 8} \left[ \frac {1}{6} \mathrm{Log} \left(\frac {1}{6}\right) + \frac {5}{6} \mathrm{Log} \left(\frac {5}{6}\right) \right] \right. \\ & \left. + \frac {1 2}{1 8} \left[ \frac {7}{1 2} \mathrm{Log} \left(\frac {7}{1 2}\right) + \frac {5}{1 2} \mathrm{Log} \left(\frac {5}{1 2}\right) \right] \right\} = 0. 8 7. \end{array}
$$

Therefore, the reduction in entropy provided by the input $X _ { 1 }$ is

$$
I _ {E} (\phi) - I _ {E} (X _ {1}) = 1. 0 - 0. 8 7 = 0. 1 3.
$$

Similarly, if input $X _ { 2 }$ is observed,

$$
\begin{array}{r l} I _ {E} (X _ {2}) & = - \left\{\frac {1 2}{1 8} \left[ \frac {4}{1 2} \operatorname{Log} \left(\frac {4}{1 2}\right) + \frac {8}{1 2} \operatorname{Log} \left(\frac {8}{1 2}\right) \right] \right. \\ & \quad \left. + \frac {6}{1 8} \left[ \frac {4}{6} \operatorname{Log} \left(\frac {4}{6}\right) + \frac {2}{6} \operatorname{Log} \left(\frac {2}{6}\right) \right] \right\} = 0. 9 2. \end{array}
$$

The reduction in entropy provided by the input $X _ { 2 }$ is

$$
I _ {E} (\phi) - I _ {E} (X _ {2}) = 1. 0 - 0. 9 2 = 0. 0 8.
$$

Hence, the ID3 algorithm would select $X _ { \mathfrak { l } }$

4.1.2. VB Algorithm. If inputs are equally costly, input cost will not affect the input selection process. Initially, the cost of the best guess classification $\operatorname { \mathbf { E C } } ^ { * } ( \phi )$ is $\mathrm { E C } ^ { * } ( \phi ) = \{ 8 - 1 0 \} = - 2$ , corresponding to the classification $Y , \operatorname { I f } X ,$ is observed,

![](/api/attachments/XGJ9BJW5/fulltext/images/07048488360cabce8ee40a2d154759a620b1974a0f6bde4c08b5cb519fee33b7.jpg)  
FIGURE 3. Example to Study Differences in Stopping Behavior VB and ID3

$$
\mathrm{EC} ^ {*} \left(X _ {1}\right) = \frac {6}{1 8} \{1 - 5 \} + \frac {1 2}{1 8} \{5 - 7 \} = - 2. 6 7.
$$

The reduction in classification cost provided by selecting input $X _ { 1 }$ is

$$
\Delta \mathrm{EC} ^ {*} (X _ {1}) = \mathrm{EC} ^ {*} (\phi) - \mathrm{EC} ^ {*} (X _ {1}) = - 2 - (- 2. 6 7) = 0. 6 7.
$$

If $X _ { 2 }$ is observed,

$$
\mathrm{EC} ^ {*} (X _ {2}) = \frac {1 2}{1 8} \left\{4 - 8 \right\} + \frac {6}{1 8} \left\{2 - 4 \right\} = - 3. 3 3.
$$

The reduction in classification cost provided by the input $X _ { 2 }$ is

$$
\Delta \mathrm{EC} ^ {*} (X _ {2}) = \mathrm{EC} ^ {*} (\phi) - \mathrm{EC} ^ {*} (X _ {2}) = - 2 - (- 3. 3 3) = 1. 3 3.
$$

Hence, the VB algorithm would select $X _ { 2 }$

This example illustrates that even when input costs are equal and classification costs are of equal magnitude, the two algorithms can create different decision trees.

## 4.2. Stopping Rule

If input costs are zero and classification costs are equal, it may appear that the VB and ID3 algorithms would stop selecting inputs under the same conditions. This is not the case. Consider the example in Figure 3. In this example, there are 18 cases and input $X _ { 1 }$ is the only input that can be observed. Input cost is zero and classification costs are of the same magnitude (±\$1).

4.2.1. ID3 Algorithm In this example, the initial entropy is the same as that computed for the example in Figure $2 \left( \mathrm { i . e . , ~ } I _ { E } ( \phi ) = 1 . 0 \right)$ . The information entropy after observing $X _ { 1 }$ is

$$
\begin{array}{r l} I _ {E} (X _ {1}) = - \left\{\frac {5}{1 8} \left[ \frac {1}{5} \operatorname{Log} \left(\frac {1}{5}\right) + \frac {4}{5} \operatorname{Log} \left(\frac {4}{5}\right) \right] \right. \\ & \left. + \frac {1 3}{1 8} \left[ \frac {7}{1 3} \operatorname{Log} \left(\frac {7}{1 3}\right) + \frac {6}{1 3} \operatorname{Log} \left(\frac {6}{1 3}\right) \right] \right\} = 0. 9 2. \end{array}
$$

The reduction in information entropy due to $X _ { 1 }$ is

$$
I _ {E} (\phi) - I _ {E} (X _ {1}) = 1. 0 - 0. 9 2 = 0. 0 8.
$$

Hence, the ID3 algorithm would use $X _ { 1 }$ to label the root node.

4.2.2. VB Algorithm. The initial classification cost is the same as that computed for the example in Figure $2 \left( \mathrm { i . e . , E C ^ { * } } ( \phi ) = - 2 . 0 \right)$ . If $X _ { 1 }$ is observed, the least classification cost is

$$
\mathrm{EC} ^ {*} (X _ {1}) = \frac {5}{1 8} (1 - 4) + \frac {1 3}{1 8} (6 - 7) = - 1. 5 5.
$$

The benefit of observing $X _ { \mathfrak { l } }$ is

$$
\Delta \mathrm{EC} ^ {*} (X _ {1}) = \mathrm{EC} ^ {*} (\phi) - \mathrm{EC} ^ {*} (X _ {1}) = - 2. 0 - (- 1. 5 5) = - 0. 4 5.
$$

Because $\Delta \mathrm { E C } ^ { * } ( X _ { 1 } )$ is negative, the VB algorithm will not use input $X _ { 1 }$ as a label. The VB algorithm stops since $X _ { \mathfrak { i } }$ is the only input. In this example, the VB algorithm stops because the input $X _ { 1 }$ does not reduce classification cost; instead, it increases cost. Therefore, the two algorithms behave differently. This example demonstrates that in certain situations, observing a particular input could reduce solution value.

## 4.3. Classification Function

The classification functions used by ID3 and VB differ in that ID3 labels leaf nodes based upon the frequency of classes in the tables. VB, on the other hand, labels leaf nodes based upon solution value. However, if the benefits of correct classification of all classes are equal and the costs of all misclassifications are equal, we show that the two algorithms will select the same label for a eaf node. Let

$k _ { 1 } > 0$ be a finite positive number,

$k _ { 2 } < 0$ be a finite negative number,

f, be the proportion of different classes in the current set of cases $( i = 1 , 2 , \dots , m )$ and

$$
C \left\{c _ {i}, c _ {j} \right\} = \left\{ \begin{array}{l l} k _ {1}, & i \neq j, \\ k _ {2}. & i = j. \end{array} \right.
$$

If, in the current set of cases, Jis the set of all classes excluding $c _ { r }$ , then the expected classification cost for the class $c _ { r }$ is

$$
\begin{array}{l} = f _ {r} C \left\{c _ {r}, c _ {r} \right\} + \sum_ {J} f _ {t} C \left\{c _ {t}, c _ {r} \right\} = f _ {r} k _ {2} + k _ {1} \sum_ {J} f _ {t} \\ = f _ {r} k _ {2} + k _ {1} [ 1 - f _ {r} ] = k _ {1} + f _ {r} [ k _ {2} - k _ {1} ]. \end{array}
$$

Since $[ k _ { 2 } - k _ { 1 } ] < 0$ , classification cost is minimum when $f _ { r }$ is maximum. Therefore, like ID3, VB will label a leaf node by the class with the highest frequency in the current set of cases.

## 4.4. Summary

In this section we have shown that the VB and ID3 algorithms may result in different input selection and stopping behavior even when input costs and classification costs are such that it appears that they could be ignored. We also show that under special conditions, the two algorithms use the same class to label a leaf node. Given differences in the trees generated by these algorithms, it is important to determine how they perform in different situations, and especially under those conditions where input and classification costs appear unimportant.

## 5. Comparison of Algorithm Performance

In this section, we describe three experiments that were conducted to compare the performance of the VB algorithm with the ID3 algorithm and the ID3 algorithm with pessimistic pruning (Quinlan 1987). The ID3 algorithm was chosen because it has been widely used (Shapiro 1987, Messier and Hansen 1988). Many variants of this algorithm have been proposed (e.g., ACLS (Niblet and Patterson 1982) and ASSIS-TANT (Kononenko et al. 1984)), and its properties have been extensively studied (Ouinlan 1987, Shapiro 1987, Niblet and Bratko 1986, Mingers 1989).

The ID3 algorithm often produces trees that are very large and difficult to understand (Quinlan 1987). Besides, the predictive ability of the algorithm deteriorates as the trees produced by the algorithm increase in size (Quinlan 1987). Pruning has been recommended to combat these problems (Quinlan 1987, Mingers 1989). Trees produced by the ID3 algorithm, when pruned, are smaller and often are more accurate than unpruned trees. However, little is known about how pruning affects system value. We also compare the trees produced by the VB algorithm to ID3 trees that are pruned using pessimistic pruning (referred to as the PR algorithm) (Quinlan 1987).⁵

The pessimistic pruning procedure uses a statistical measure to determine whether replacing a subtree by its best leaf (i.e., the classification that maximizes accuracy for a given set of cases) is likely to increase accuracy. If so, the subtree is replaced by its best leaf, otherwise it is retained. Subtrees are examined starting from the largest subtree (i.e., the entire tree).

Summarizing, the purpose of these experiments is to compare the performance of three induction algorithms: VB, ID3 and PR.6 The expected cost (i.e., system value) of using decision trees generated by these algorithms to classify a set of test cases is the performance measure. It includes information acquisition costs and classification costs.

## 5.1. Factors Affecting Performance

Induction algorithms used for real problems are likely to encounter a variety of situations. For example, input costs may be high and classification costs may be relatively low. In such cases, it could be best to guess an object's class without observing any inputs. When classification costs are high, it may be beneficial to observe some inputs in order to reduce misclassification costs. The costs of acquiring different inputs can vary a great deal; with some inputs being much more expensive than others, i.e., input cost variance can be high. Similarly, classification costs can vary a great deal, i.e., classification cost variance can be high. We attempt to determine how trees generated by the three algorithms will perform under these different conditions. We study the effects on algorithm performance, of: (1) different average input costs, (2) different classification cost variances, and (3) different input cost variances.

5.1.1. Average Input Cost. The PR and ID3 algorithms assume that inputs are free. We determine how the trees generated by these two algorithms perform relative to the VB algorithm when the average input costs vary. Because the stopping rules in the ID3 and PR algorithms are not cost-benefit driven, the performance of both the PR and ID3 algorithms relative to the VB algorithm should be adversely affected if the average input cost is increased. In this study, average input cost is chosen relative to a given set of classification costs using the procedure described below.

Consider a single leaf tree, S (i.e., no inputs are observed), which has the least classification cost among all single leaf trees for the set of cases in D. If S is used to classify cases, the expected classification cost $S _ { c }$ is

$$
S _ {c} = \underset {j} {\operatorname{Min}} \left[ \sum_ {i = 1} ^ {m} f (c _ {i}, D) C \left\{c _ {i}, c _ {j} \right\} \right].
$$

Now, consider a tree R that correctly classifies all cases. If R is used to classify cases, the expected classification cost $\pmb { R } _ { c }$ is

$$
R _ {c} = \left[ \sum_ {i = 1} ^ {m} f (c _ {i}, D) C \mid c _ {i}, c _ {i} \right\}.
$$

The reduction in classification cost resulting from the use of R instead of S is

$$
B = S _ {c} - R _ {c}.
$$

If R has an average of p nonleaf nodes in a path, and the average cost of an input is K, then the average information acquisition cost of classifying an object if R is used is $K \ast p$ . Therefore, the incremental value of using R instead of S to classify cases is [ B – K \* p]. If [ B – K  p] equals zero, then R and S have the same system value, i.e., although R correctly classifies all cases, nothing is gained by acquiring information.

Now, if the ID3 algorithm generates a tree, U, that has an average of q nonleaf nodes in a path, the maximum value of K for which the cost of using U will be lower than that of using S can be estimated by the cut-off ratio C, where

$$
C = \frac {B}{q} = \frac {S _ {c} - R _ {c}}{q}.
$$

If $K > C$ , the cost of using U is greater than that of using S. For a given data set, set of classification costs and average input cost, the cut-off ratio determines how the cost of using an ID3 tree compares with that of using the best single leaf tree. The cut-off ratio may also be used to predict the performance of an ID3 tree when classifying unseen cases. In this case, $U$ will not always classify objects correctly. Hence, the expected cost if U is used may be greater than $S _ { c }$ for values of K less than C. In general, the expected cost of using a tree generated by the ID3 algorithm will increase as average input cost increases. The same should hold for PR, since PR, like ID3, does not consider input and classification costs.

For a given data set and classification costs, the VB algorithm is likely to generate different trees for different values of average input cost. The average cost of using a VB tree to classify the cases in $D$ will never be greater than $S _ { c }$ . If the cases in $D$ are representative of the population of cases in the domain, $S _ { c }$ is an upper bound estimate of the expected cost of using the VB tree to classify cases in the domain. This upper bound estimate does not depend upon input costs. The performance of the three algorithms for different input costs can be summarized as

PRoposiTioN 1. The performance of the PR and ID3 algorithms relative to the VB algorithm will deteriorate with an increase in average input cost,

5.1.2. Classification Cost Variance. In decision making situations, classification costs can vary a great deal. Certain types of incorrect (correct) classifications may be much costlier (less costly) than others. Since both the PR and ID3 algorithms do not consider classification costs, a large classification cost variance is likely to adversely affect the performance of these algorithms relative to the VB algorithm.

The effects of two types of classification cost variance are investigated here: (1) classification costs are randomly varied, and (2) classification costs are skewed in such a way that the absolute costs corresponding to correct and incorrect classifications in certain classes are much higher than the costs in other classes.7 A class with relatively high classification costs is called a preferred class. The existence of preferred classes could have a great impact on the trees generated by the VB algorithm, while having no effect on the trees generated by the ID3 and PR algorithms. However, the existence of preferred classes may have a different effect on the relative performance of these algorithms, than does random classification cost variation. Hence, preferred class effects are studied. The anticipated effects of classification cost variation on the relative performance of the algorithms are:

PRoPosITiON 2A. The performance of the PR and ID3 algorithms relative to the VB algorithm will deteriorate when there is a preferred class.

PRoPosıTioN 2B. The performance of the PR and ID3 algorithms relative to the VB algorithm will deteriorate with an increase in classification cost variance.

5.1.3. Input Cost Variance. The performance of the PR and ID3 algorithms relative to the VB algorithm is likely to be affected if input costs vary. The VB algorithm should generate trees that perform better than the other algorithms when input cost variance is high. This can be stated as:

PRoposITioN 3. T'he performance of the PR and ID3 algorithms relative to the VB algorithm will deteriorate with an increase in input cost variance, if the average input cost is equal to or higher than the cut-off ratio.

However, if the average input cost is very low relative to classification costs (e.g., information costs are low, while error costs are high), input cost variance should not make much of a difference. This can be stated as:

PRoposITION 4. T'he performance of the PR and ID3 algorithms relative to the VB algorithm will stay the same with an increase in input cost variance, if the average input cost is much lower than the cut-off ratio

## 5.2. Experiments

Three experiments were conducted to investigate the propositions. In the first experiment, the impact of changes in average input cost and the existence of preferred classes was studied. This experiment addresses Propositions 1 and 2A. In this experiment, input cost variance was held constant. The impact of changes in input cost variance and random classification cost variance was studied in the second and third experiment, These two experiments investigate Propositions 2B, 3 and 4. In the second and third experiment, average input cost was held constant.

A data set consisting of fifty cases relating to the financial health of firms was used in each of these experiments (Liang 1992). Each case contains information about a single firm and includes eight input attributes and a classification of the firm. Firms are classified as bankrupt (ves) or healthy (no). The input attributes include financial ratios, opinions concerning firm health, etc. There are an equal number of cases in each class (i.e., 25 bankrupt and 25 healthy).

5.2.1. Experiment #1. In this experiment, a 3 × 2 × 2 factorial design was used. The three factors are: algorithm, average input cost, and classification cost variance. Algorithm had three levels: VB, PR and ID3. Average input cost had two levels: moderate (M), where the average input cost was equal to the cut-off ratio, and high (H), where the average input cost was four times the cut-off ratio. Classification cost variance had two levels: no variance (Z) and high variance (H). High variance classification costs were chosen such that the absolute value of these costs for the “no/yes" and “no/no" classifications, were four times higher than the costs in the other two classifications. Thus, “no" is a preferred class when classification cost variance is high. Table 4, Panel A, shows the treatments and the number of observations in each cell. There were a total of 12 treatments, with 30 observations for each treatment. Input cost variance was held constant.

For a fixed set of input and classification costs, the performance of the three algorithms was determined, resulting in three observations. These three observations were generated using the BASICGEN procedure described in Appendix A. The BA-SICGEN procedure randomly splits the data set (50 cases) into a training set (35 cases) and a holdout set (15 cases). The training set was used to construct decision trees with the VB, PR and ID3 algorithms. These trees were then used to classify the cases in the holdout set and their performance was determined. Since the choice of a training set affects the performance of the three algorithms, each algorithm was tested on 30 different, randomly generated training sets and the average performance of the algorithm across these different training sets provided a single observation

In this experiment, there were four distinct conditions for input and classification costs: (i) moderate input cost and zero classification cost variance, (ii) high input cost and zero classification cost variance, (iii) moderate input cost and high classification cost variance and (iv) high input cost and high classification cost variance. The COSTGEN procedure described in Appendix B was used to generate 90 observations (30 each for VB, PR and ID3), for each of the four conditions listed above. The COSTGEN procedure uses BASICGEN as a subprocedure.

Panel B  
Experiment #1: Input Cost Variance Set at Moderate  
TABLE 4  
Design of Experiments Showing the Number of Observations in Each Cell

<table><tr><td rowspan="3" colspan="2"></td><td colspan="6">Classification Cost Variance</td></tr><tr><td colspan="3">High (Preferred Class)</td><td colspan="3">Zero</td></tr><tr><td>VB</td><td>PR</td><td>ID3</td><td>VB</td><td>PR</td><td>ID3</td></tr><tr><td rowspan="2">Average Input Costs</td><td>High</td><td>30</td><td>30</td><td>30</td><td>30</td><td>30</td><td>30</td></tr><tr><td>Moderate</td><td>30</td><td>30</td><td>30</td><td>30</td><td>30</td><td>30</td></tr></table>

Experiment #2: Average Input Cost Set at Moderate

<table><tr><td rowspan="3" colspan="2"></td><td colspan="6">Classification Cost Variance</td></tr><tr><td colspan="3">High (random)</td><td colspan="3">Zero</td></tr><tr><td>VB</td><td>PR</td><td>ID3</td><td>VB</td><td>PR</td><td>ID3</td></tr><tr><td rowspan="2">Input Cost Variance</td><td>High</td><td>30</td><td>30</td><td>30</td><td>30</td><td>30</td><td>30</td></tr><tr><td>Zero</td><td>30</td><td>30</td><td>30</td><td>30</td><td>30</td><td>30</td></tr></table>

Results. Analysis of variance was used to compare the performance of the three algorithms under the different conditions. The results are presented in Table 5. All terms in the model are significant at the 0.0001 level. Thus, differences in average

TABLE 5  
Experiment #1: ANOVA Results

<table><tr><td>Source</td><td>DF</td><td>Sum of Squares</td><td>Mean Square</td><td>F value</td><td>p-value</td></tr><tr><td>Model</td><td>11</td><td>5142501.37</td><td>467500.12</td><td>2514.99</td><td>0.0001</td></tr><tr><td>Error</td><td>348</td><td>67338.79</td><td>193.50</td><td></td><td></td></tr><tr><td>Total</td><td>359</td><td>5209840.17</td><td></td><td></td><td></td></tr><tr><td>ALG</td><td>2</td><td>940072.29</td><td>470036.14</td><td>2429.10</td><td>0.0001</td></tr><tr><td>AIC</td><td>1</td><td>1656498.14</td><td>1656498.14</td><td>8560.61</td><td>0.0001</td></tr><tr><td>CCV</td><td>1</td><td>138127.52</td><td>138127.52</td><td>713.83</td><td>0.0001</td></tr><tr><td>ALG*AIC</td><td>2</td><td>691754.69</td><td>345877.34</td><td>1787.46</td><td>0.0001</td></tr><tr><td>ALG*CCV</td><td>2</td><td>443526.37</td><td>221763.18</td><td>1146.05</td><td>0.0001</td></tr><tr><td>AIC*CCV</td><td>1</td><td>879334.01</td><td>879334.01</td><td>4544.31</td><td>0.0001</td></tr><tr><td>ALG*AIC*CCV</td><td>2</td><td>393188.33</td><td>196594.16</td><td>1015.98</td><td>0.0001</td></tr></table>

The three factors are: Algorithm (ALG) [VB, ID3, PR], Average input cost (AIC) [set at moderate or high], Classification cost variance (CCV) [set at zero, or high (there is a preferred class)]. Input cost variance is fixed at 0.3 times average input cost.

TABLE 6  
Experıment #1. Differences in Means

<table><tr><td colspan="5">Panel AFirst Order Differences $^{2}$ </td></tr><tr><td>AIC</td><td>CCV</td><td>VB-PR</td><td>VB-ID3</td><td>ID3-PR</td></tr><tr><td>High</td><td>High</td><td>-111.54[-27.12](0.0001)</td><td>-385.83[-88.68](0.0001)</td><td>+274.28[+108.62](0.0001)</td></tr><tr><td>Moderate</td><td>High</td><td>-39.05[-20.46](0.0001)</td><td>-52.10[-17.83](0.0001)</td><td>+13.05[+9.73](0.0001)</td></tr><tr><td>High</td><td>Zero</td><td>-16.58[-17.97](0.0001)</td><td>-62.78[-79.66](0.0001)</td><td>+46.19[+80.09](0.0001)</td></tr><tr><td>Moderate</td><td>Zero</td><td>-11.97[-19.44](0.0001)</td><td>-14.72[-26.07](0.0001)</td><td>+2.75[+6.71](0.0001)</td></tr></table>

Panel B Second Order Differences

<table><tr><td>AIC</td><td>CCV</td><td> $\Delta (VB-PR)$ </td><td> $\Delta (VB-ID3)$ </td><td> $\Delta (ID3-PR)$ </td></tr><tr><td>High-Moderate</td><td>High</td><td>-72.49[-14.56](0.0001)</td><td>-333.73[-74.39](0.0001)</td><td>+261.23[+173.59](0.0001)</td></tr><tr><td>High-Moderate</td><td>Zero</td><td>-4.61[-5.33](0.0001)</td><td>-48.05[-53.15](0.0001)</td><td>+43.44[+173.46](0.0001)</td></tr><tr><td>High</td><td>High-Zero</td><td>-94.96[-24.95](0.0001)</td><td>-323.05[-80.30](0.0001)</td><td>+228.09[+112.69](0.0001)</td></tr><tr><td>Moderate</td><td>High-Zero</td><td>-27.08[-17.78](0.0001)</td><td>-37.38[-11.18](0.0001)</td><td>+10.30[+13.79](0.0001)</td></tr></table>

Values ın each cell are differences in means, t-values (un square brackets) and one-tailed p-values (in parenthesis).  
² Panel A results are interpreted as follows: a negative difference in the first row, third column (VB-PR) indicates that the VB algorithm performed better than the PR algorithm when average input cost (AIC) was high and classification cost variance (CCV) was high.

input cost and classification cost variance affect the performance of the three algorithms. In order to interpret these results, relevant mean differences are shown in Table 6, Panels A and B.

Panel A shows mean differences in performance for each pair of algorithms (VB-PR, VB-ID3), for each of the four conditions.8 The values in each cell show the numerical difference in mean performance, along with t-values and two-tailed pvalues. These results indicate that the VB algorithm classified objects at lower cost than the PR and ID3 algorithms in each of the four conditions.

Second order mean differences are shown in Panel B. The mean values in the first row of Panel B, are differences between the mean values in the first and second row in Panel A. The first row in Panel B shows the difference in performance when average input cost changed from high to moderate, and classification cost variance was high. In the first row in Panel B, a statistically significant negative value in the column ∆(Alg1-Alg2) indicates that the performance of algorithm Alg2 relative to algorithm Alg1, deteriorated as average input cost changed from moderate to high. Negative values in other rows of Panel B are interpreted in a similar manner. Results shown in Panel B indicate that the performance of the PR and ID3 algorithms relative to the VB algorithm got worse when average input cost was increased, with classification cost variance fixed at zero (row two). The results in rows one and two (Panel B) support Proposition 1.

The results in Panel B also indicate that when average input cost was high, the performance of the PR and ID3 algorithms relative to the VB algorithm worsened when a preferred class was introduced (row three). In the presence of a preferred class, the performance of the PR and ID3 algorithms relative to the VB algorithm worsened even when average input cost was moderate (row four). Although the VB algorithm performed better than the other algorithms when preferred classes were not present (classification cost variance was zero), its performance relative to the other algorithms improved when a preferred class was present. These results support Proposition 2A.

5.2.2. Experiment #2. The objective of this experiment was to determine the effects of input cost variance and random classification cost variance. Table 4, Panel B, shows the treatments in this experiment, corresponding to two levels for each of the two factors, input cost variance (ICV) and classification cost variance (CCV). Input cost variance has two levels: ICV is zero (Z), and ICV is high (H). Classification cost variance also has two levels: CCV is zero (Z), and CCV is high (H). High variance classification costs were randomly generated from a distribution with a large variance. Here, preferred classes were not deliberately generated. The third factor in this experiment was ALG (algorithm). As before, algorithm had three levels: VB, PR and ID3. Average input cost (AIC) was set at the cut-off ratio in this experiment. A 3 × 2 × 2 factorial design resulted in 12 treatments with 30 observations per treatment.

In this experiment, there were four distinct conditions for input and classification costs: (a) zero input cost variance and zero classification cost variance, (b) zero input cost variance and high classification cost variance, (c) high input cost variance and zero classification cost variance, and (d) high input cost variance and high classification cost variance. The VARGEN procedure described in Appendix C was used to generate 90 observations (30 each for VB, PR and ID3), for each cost condition described above. As in Experiment #1, the VARGEN procedure used BASICGEN as a subprocedure.

Results. Analysis of variance was used to determine whether there were differences in the performance of the three algorithms. The results are presented in Table 7. The main effects and the first order interactions involving ALG are significant at the 0.05 level, indicating that random classification cost variance and input cost variance affected the performance of the algorithms. In order to determine how these algorithms performed at different levels of CCV and ICV, first order mean differences are shown in Table 8, Panel A. We find that the VB algorithm performed better than the

TABLE 7  
Experiment #2. ANOV 4 Results

<table><tr><td>Source</td><td>DI</td><td>Sum of Squares</td><td>Mean Square</td><td>F value</td><td>p-value</td></tr><tr><td>Model</td><td>11</td><td>12280047.81</td><td>1116367.98</td><td>65.37</td><td>0.0001</td></tr><tr><td>Error</td><td>348</td><td>5942913.77</td><td>17077.33</td><td></td><td></td></tr><tr><td>Total</td><td>359</td><td>18222961.58</td><td></td><td></td><td></td></tr><tr><td>Alg</td><td>2</td><td>10733021.42</td><td>5366510.71</td><td>314.25</td><td>0.0001</td></tr><tr><td>ICV</td><td>1</td><td>220776.01</td><td>220776.01</td><td>12.93</td><td>0.0004</td></tr><tr><td>CCV</td><td>1</td><td>759814.52</td><td>759814.52</td><td>44.49</td><td>0.0001</td></tr><tr><td>Alg*ICV</td><td>2</td><td>241620.09</td><td>120810.04</td><td>7.07</td><td>0.0010</td></tr><tr><td>Alg*CCV</td><td>2</td><td>241342.74</td><td>125671.37</td><td>7.36</td><td>0.0007</td></tr><tr><td>ICV*CCV</td><td>1</td><td>41431.96</td><td>41431.96</td><td>2.43</td><td>0.1202</td></tr><tr><td>Alg*ICV*CCV</td><td>2</td><td>32041.04</td><td>16020.52</td><td>0.94</td><td>0.3924</td></tr></table>

The three factors are: Algorıthm (Alg) [VB, ID3, PR], Input cost variance (ICV) [set at zero, or high], Classification cost variance (CCV) [set at zero, or high]. Average input cost is fixed at the Moderate level.

ID3 algorithm in each of the four conditions. Even when both ICV and CCV were zero, the VB algorithm performed better than the ID3 algorithm, but, under these conditions VB did not do better than PR. When classification costs were uniform (CCV was zero), the performance of VB and ID3 was similar. Furthermore, since inputs were equally costly, there was not much of a difference between the input selection behavior of VB and ID3. However, since average input cost was moderate, input costs affected the stopping behavior of the VB algorithm. The ID3 algorithm is known to overfit data. This overfitting could account for differences between VB and ID3 performance under these conditions (CCV and ICV are zero). However, with pruning, overfitting is less likely. This likely is the reason that the performance of the VB and PR algorithms did not differ. In the other conditions, VB performed better than PR.

Because the PR and ID3 algorithms ignore classification costs, their performance relative to the VB algorithm should deteriorate when classification cost variance changes from zero to high. The statistically significant second order mean differences in the first row of Panel B (Table 8), indicate that the performance of the PR and ID3 algorithms relative to the VB algorithm worsened when classification cost variance increased from zero to high and input cost variance was high. The same is true when input cost variance was zero (second row). These results support Proposition 2B.

In this experiment, the average input cost was set at the cut-off level. Since the PR and ID3 algorithms ignore differences in individual input costs, a change in input cost variance from zero to high, should cause the performance of these algorithms to deteriorate relative to that of the VB algorithm. In Table 8, Panel B (third and fourth row), we find that the second order mean differences (∆(VB – PR) and ∆(VB – ID3)) are statistically significant and negative. This indicates that the performance of the PR and ID3 algorithms relative to the VB algorithm worsened as input cost variance changed from zero to high. These results support Proposition 3.

5.2.3. Experıment #3. The objective of this experiment was to study the impact of input cost variance when average input costs (AIC) are very low. When AIC is very low relative to classification costs, VB will try to classify all cases correctly, producing large trees. This experiment is identical to Experiment #2, except that AIC was set much below the cut-off ratio. The average input cost was set at 0.25 times the cut-off ratio.

<table><tr><td colspan="5">TABLE 8Experiment #2: Differences in Means1</td></tr><tr><td colspan="5">Panel AFirst Order Differences</td></tr><tr><td>ICV</td><td>CCV</td><td>VB-PR</td><td>VB-ID3</td><td>ID3-PR</td></tr><tr><td>High</td><td>High</td><td>-222.54[-9.31](0.0001)</td><td>-508.54[-17.98](0.0001)</td><td>+286.00[+15.47](0.0001)</td></tr><tr><td>High</td><td>Zero</td><td>-157.97[-7.55](0.0001)</td><td>-424.92[-18.67](0.0001)</td><td>+267.01[+20.21](0.0001)</td></tr><tr><td>Zero</td><td>High</td><td>-153.64[-5.80](0.0001)</td><td>-434.03[-15.33](0.0001)</td><td>+280.39[+25.79](0.0001)</td></tr><tr><td>Zero</td><td>Zero</td><td>+1.64[+1.15](0.2584)</td><td>-289.39[-39.13](0.0001)</td><td>+291.03[+41.15](0.0001)</td></tr><tr><td colspan="5">Panel BSecond Order Differences</td></tr><tr><td>ICV</td><td>CCV</td><td>Δ(VB-PR)</td><td>Δ(VB-ID3)</td><td>Δ(ID3-PR)</td></tr><tr><td>High</td><td>High-Zero</td><td>-64.63[-2.97](0.0059)</td><td>-83.62[-2.63](0.0134)</td><td>+18.98[+0.9743](0.3380)</td></tr><tr><td>Zero</td><td>High-Zero</td><td>-155.28[-5.88](0.0001)</td><td>-144.63[-5.26](0.0001)</td><td>-10.64[-1.86](0.0717)</td></tr><tr><td>High-Zero</td><td>High</td><td>-68.90[-2.64](0.0132)</td><td>-74.51[-2.62](0.0137)</td><td>+5.60[+0.4142](0.6818)</td></tr><tr><td>High-Zero</td><td>Zero</td><td>-159.54[-7.59](0.0001)</td><td>-135.52[-5.43](0.0001)</td><td>-24.02[-1.92](0.0639)</td></tr></table>

Values in each cell are differences in means, t-values (in square brackets) and one-tailed p-values (in parenthesis).

Results. The results are presented in Table 9. They indicate that in this case, input cost variance (ICV) had no significant impact on performance. Thus, Proposition 4 is supported. Interestingly, in this case, an increase in classification cost variance did not have an impact on the performance of the three algorithms (ALG\*CCV is insignificant at 0.10). When input costs are very low (relative to classification costs) VB generates large trees that attempt to classify every case correctly. Hence, when a stopping condition is detected, the current set of cases (L) typically is heavily skewed towards a particular class. Consequently, the VB classification function selects the same class as does the ID3 classification function. It should be noted that in this case too, the VB algorithm performed better than the other two algorithms.

<table><tr><td colspan="6">TABLE 9Experiment #3. ANOVA Results</td></tr><tr><td>Source</td><td>DF</td><td>Sum of Squares</td><td>Mean Square</td><td>F value</td><td>p-value</td></tr><tr><td>Model</td><td>11</td><td>404351.09</td><td>36759.19</td><td>2.26</td><td>0.0114</td></tr><tr><td>Error</td><td>348</td><td>5656194.92</td><td>16253.43</td><td></td><td></td></tr><tr><td>Total</td><td>359</td><td>6060546.01</td><td></td><td></td><td></td></tr><tr><td>Alg</td><td>2</td><td>223362.63</td><td>111681.31</td><td>6.87</td><td>0.0012</td></tr><tr><td>ICV</td><td>1</td><td>15479.97</td><td>15479.97</td><td>0.95</td><td>0.3298</td></tr><tr><td>CCV</td><td>1</td><td>118177.24</td><td>118177.24</td><td>7.27</td><td>0.0073</td></tr><tr><td>Alg*ICV</td><td>2</td><td>3823.91</td><td>1911.95</td><td>0.12</td><td>0.8891</td></tr><tr><td>Alg*CCV</td><td>2</td><td>24645.29</td><td>12322.64</td><td>0.76</td><td>0.4693</td></tr><tr><td>ICV*CCV</td><td>1</td><td>18447.19</td><td>18447.19</td><td>1.13</td><td>0.2875</td></tr><tr><td>Alg*ICV*CCV</td><td>2</td><td>414.83</td><td>207.41</td><td>0.01</td><td>0.9873</td></tr></table>

Three factors are: Algorıthm (Alg) [VB, ID3, PR], Input cost variance (ICV) [set at zero, or high] Classification cost variance (CCV) {set at zero, or highl. Average input cost is fixed at Low.

5.2.4. Summary of Results. The results are summarized in Table 10.ª Two general conclusions are:

1. Under a variety of conditions, the VB algorithm generates trees that will typically produce higher system value than the other two algorithms.

2. The performance of the VB algorithm relative to the PR and ID3 algorithms improves with an increase in input and classification cost variance and with an increase in average input cost.

## 5.3. Accuracy and Size Differences

The empirical study reported here used system value as the measure of performance. In previous studies, accuracy and stze of the decision trees have been the primary measures of performance (Quinlan 1986, Mingers 1989). Although not reported here, we also compared the performance of these algorithms in terms of accuracy and size. Accuracy was measured by the proportion of cases in the test data set that are correctly classified. The number of leaf nodes in the tree was used to measure the size of the decision trees generated by these algorithms. We briefly summarize the results of these investigations here.

1. The accuracy of VB trees is dependent upon input and classification costs. As average input costs decrease, VB trees increase in size. An increase in VB tree size improves accuracy. Hence, the accuracy of VB trees increases with a decrease in average input cost. In the presence of a preferred class, VB trees decrease in size and consequently, their accuracy decreases.

TABLE 10  
Summary of Results  
Panel A  
Experiment #1: Average Input Cost and Preferred Class Effects

<table><tr><td>P#</td><td>Average Input Cost</td><td>Input Cost Variance</td><td>Preferred Class</td><td>Relative Performance</td></tr><tr><td>1</td><td>Increases from Moderate to High</td><td>Unimportant</td><td>Unimportant</td><td>Gets Worse</td></tr><tr><td>2A</td><td>Unimportant</td><td>Unimportant</td><td>Changes from No to Yes</td><td>Gets Worse</td></tr></table>

Panel B

Experiment #2: Input Cost and Random Classification Cost Variance

<table><tr><td>P#</td><td>Average Input Cost</td><td>Input Cost Variance</td><td>Classification Cost Variance</td><td>Relative Performance</td></tr><tr><td>2B</td><td>Any value equal to or above Moderate</td><td>Increases</td><td>Unimportant</td><td>Gets Worse</td></tr><tr><td>3</td><td>Unimportant</td><td>Unimportant</td><td>Increases</td><td>Gets Worse</td></tr></table>

Panel C

Experiment #3: Effect of Input Cost Variance at Low Average Input Cost

<table><tr><td>P#</td><td>Average Input Cost</td><td>Input Cost Variance</td><td>Classification Cost Variance</td><td>Relative Performance</td></tr><tr><td>4</td><td>Low</td><td>Increases</td><td>Unimportant</td><td>Unchanged</td></tr></table>

¹ P# is the proposition number. Each row in Panels A, B, and C shows how the ID3 and PR algorithms perform relative to the VB algorithm, as average input costs, input cost variances and classification cost variances change. For example, the first row of Panel A indicates that: if the average cost of inputs increases from moderate to high, the performance of the PR and ID3 algorıthms with relative to the VB algorıthm gets worse. This is true regardless of the level chosen for input cost variance and whether preferred classes are present or not.

2. VB trees are smaller (never larger) than ID3 trees

3. VB trees are roughly the same size as PR trees.

The second result may appear surprising, since, if average input costs are low one would expect the size of the two trees to be similar. Size differences in such cases are due to differences in the stopping rule used by the two algorithms. This is due to the fact that when the ID3 algorithm stops and creates a leaf node, the VB algorithm does the same. However, the converse is not true, i.e., when the VB algorithm creates a leaf node, the ID3 algorithm may not do so. In effect, the cost-benefit stopping rule used in the VB algorithm, naturally prunes the tree. If smaller trees are easier to understand, VB trees will be easier to understand than ID3 trees.

## 6. Summary and Conclusions

The primary objective in inductive expert system research has been to develop systems that can accurately classify objects. These systems attempt to maximize solution accuracy: i.e., maximize the number of cases in which the output provided by the system is similar to that provided by human experts. Such an objective does not ensure that the resulting systems will provide value to an organization, because, the value of the system's outputs and the costs of information necessary to generate these outputs, are ignored. There are three important factors in the design of an induction algorithm: the input selection criterion. stopping rule and classification function. We show how these factors, in the popular ID3 algorithm, can adversely affect the value of a system.

In this paper, we describe the VB induction algorithm that develops systems that attempt to maximize system value. The design of this algorithm is based upon the sequential information acquisition paradigm (Moore and Whinston 1986, 1987). Information is acquired to reduce uncertainty only if the benefits gained from acquiring information exceed the cost of acquiring the information. Three experiments were conducted to compare the performance of the VB algorithm to that of the ID3 algorithm and the ID3 algorithm with pessimistic pruning, a post ınduction procedure that is believed to reduce the size and increase the accuracy of ID3 trees. The value of using the decision trees generated by these algorithms was determined. Value was determined by information acquisition costs and classification costs.

Results indicate that VB trees are typically more profitable than ID3 or PR trees. The performance of the PR and ID3 algorithms relative to the VB algorithm deteriorates when input acquisition costs vary. The sarne is true of classification costs, i.e., when these costs are not equal, the performance of the PR and ID3 algorithms deteriorates relative to the VB algorithm. The performance of the PR and ID3 algorithms relative to the VB algorithm also suffers if the average cost of the inputs increase. The accuracy of VB trees vary with input and classification costs. VB tree accuracy usually increases with size. VB trees are smaller than ID3 trees and roughly the same size as PR trees.

In many different areas of system design (e.g., interface design, file design, expert system design, etc.), there is little theory to guide the design effort. Recently, there have been attempts to remedy this problem in such areas as: interactive systems (Jacob et al. 1992), expert system design (Hall et al. 1986, Jacob et al. 1988), and information retrieval ( Moore et al. 1990). Much of this work is based upon classical decision theory. However, to our knowledge, this is the first attempt to demonstrate that the designs suggested by a decision theoretic framework are better than the rules-of-thumb approaches that have traditionally guided design

Moore and Whinston (1986, 1987) suggest that decision-making systems should trade-off information acquisition costs with improvements in decision quality. The VB algorithm develops decision trees that make such a tradeoff. The ID3 algorithm and its variants, however, are based on rules of thumb. Our results indicate that inductive systems designed to make this tradeoff will result in greater value to an organization than conventionally designed systems.

The VB algorithm employs a single-stage greedy heuristic to select inputs. It may be possible to improve upon this heuristic by considering longer term benefits. A value-based algorithm that employs a multistage heuristic requires much more computing time to develop decision trees. Limited 1ests of one such algorithm indicated that there was no appreciable gain in system value. However, multistage heuristics would have to be studied more extensively to say anything definitive about their performance relative to that of the VB algorithm.

The tradeoff between information costs and the value generated by obtaining additional information must be made in many areas of system design. Whether system designs that attempt to make this tradeoff are better than systems designed using conventional methods, needs to be investigated. In the AI area, the sequential information acquisition paradigm may be useful in designing other types of classification algorithms including those proposed in the area of machine learning.\*

Acknowledgments. We are grateful to the associate editor and the three reviewers whose suggestions have greatly improved this manuscript.

\* Andrew Whinston, Associate Editor. This paper was received on May 29, 1992, and has been with the authors $2 { \frac { 1 } { 2 } }$ months for 1 revision.

## Appendix A: The BASICGEN Procedure

In each of the three experiments, a set of three observations is obtained for the performance of the three algorithms for a fixed set of input and classification costs. This set of three observations is generated using the procedure described below.

Step 1. Randomly split the data set into a training set of 35 cases and a holdout set of 15 cases

Step 2. Using the training set, generate a tree with each of the three algorithms.

Step 3. Classify the cases in the holdout set using each of the three decision trees. Determine the cost of classifying the cases in the holdout set using each tree. This cost is the sum of the input cost and the classification cost for the 15 cases, divided by 15.

Step 4. Repeat steps 1 through 3, 30 times. Compute the average cost for these 30 iterations. This average cost provides one observation for each of the three algorithms.

Step 5. Stop.

## Appendix B: The COSTGEN Procedure

This procedure is used to generate 90 observations (30 each for VB, PR and ID3) for each of the cost conditions in Experiment #1.

Step 1. Randomly generate $" ( " , "$ a positive constant. Denote the zero variance classification costs by $\mathbf { C _ { z } }$ $\mathbf { \epsilon } = \{ - c , c , c , - c \}$ , corresponding to the classifications: “yes/yes," “yes/no,"“no/yes,"and $\mathrm { \ " m o / n o ^ { \prime } }$ respectively. Find the cut-off ratio for these classification costs. Calculate moderate $( K _ { m } )$ and high $( K _ { h } )$ levels of average input cost equal to the cut-off ratio and four times this ratio, respectively. Generate eight input costs corresponding to the moderate level from the uniform distribution $\mathcal { V } ( K _ { m } , 0 . 3 K _ { m } )$ , where $\textstyle K _ { m }$ is the mean and $0 . 3 K _ { m }$ is the variance. Denote the vector of moderate input costs by $\mathbf { X } _ { \mathbf { m } } .$ Similarly, generate $\mathbf { X } _ { \mathbf { a } } ,$ the vector of high input costs, from the distribution: $U ( K _ { h } , 0 . 3 K _ { h } )$

Step 2. Denote the vector of high variance classification costs by $\mathbf { C _ { h } }$ . Choose $\mathbf { C _ { \mathrm { { h } } } } = \left[ - c , c , 4 c , - 4 c \right\}$ corresponding to the classifications: $\mathrm  { } ^ { * * } y e s / y e s , \mathrm  { } ^ { * * } y e s / n o , \mathrm  { } ^ { * * } n o / y e s , \mathrm  { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * * } n o / y e s , \mathrm { { } ^ { * } n o / y e s , \mathrm { { } ^ { * } n o / y e s , \mathrm { { } ^ { * } n o / y e s , \mathrm { { } ^ { * } n o / y e s , \mathrm { { } ^ { * } n o / y e s , \mathrm { { } ^ { * } n o / y e s , \mathrm { { } ^ { * } n o / y e s , \mathrm { } } } } } } } } } } } } } } } } } } } } } } } } } } }$ and “no/no” respectively. Calculate another cut-off ratio corresponding to the above high variance classification costs. Calculate moderate and high levels of average input cost $( K _ { m } ^ { \prime }$ and $K _ { h } ^ { \prime } )$ equal to the new cut-off ratio and four times this ratio. Generate sets of moderate and high level input costs from the distributions: $U ( K _ { m } ^ { \prime } , 0 . 6 K _ { m } ^ { \prime } )$ and $U ( K _ { h } ^ { \prime } .$ $0 . 6 K _ { h } ^ { \prime } )$ . Denote the input cost vectors corresponding to moderate and high average input cost at high classification cost variance by $\mathbf { X } _ { \mathbf { m } } ^ { \prime }$ and $\mathbf { X } _ { \mathbf { \lambda } } ^ { \prime }$ respectively.

Step 3. Using BASICGEN, $\mathbf { X } _ { \mathbf { m } }$ and $\mathbf { C } _ { \pmb { \mathrm { ~ \mathscr ~ { ~ z ~ } ~ } } }$ , generate three observations corresponding to moderate input costs and zero classification cost variance.

Step 4. Using BASICGEN, $\mathbf { X } _ { \mathbf { \Delta } \mathbf { b } }$ and $\mathbf { C } _ { \mathbf { z } } ,$ generate three observations corresponding to high input costs and zero classification cost variance.

Step 5. Using BASICGEN, $\mathbf { X } _ { \mathbf { m } } ^ { \prime }$ and $\mathbf { C _ { b } } .$ , generate three observations corresponding to moderate input costs and high classification cost variance.

Step 6. Using BASICGEN, $\mathbf { X } _ { \mathbf { h } } ^ { \prime }$ and $\mathbf { C _ { \hat { \theta } } } _ { \mathbf { \tilde { a } } } .$ generate three observations corresponding to high input costs and high classification cost variance

Step 7. Repeat steps 1 through 6 for 30 randomly chosen values of the positive constant $" c . "$ Step 8 Stop.

## Appendix C: The VARGEN Procedure

This procedure is used to generate 90 observations (30 each for VB, PR and ID3) for each of the cost conditions in Experiments #2 and #3.

Step 1. Randomiy generate $" c ,"$ a positive constant. Denote the zero variance classification costs by $\mathbf { C _ { z } }$ $\mathbf { \Psi } = \left[ - c , c , c , - c \right]$ , corresponding to the classifications: “yes/yes," “yes/no," "no/yes," and $" \mathrm { n o } / \mathrm { n o } ^ { \prime \prime }$ respectively Find the cut-off ratio corresponding to the above classification costs. Let the average input cost, K, equal the cut-off ratio. Let $\mathbf { X } _ { \pmb { z } }$ be the vector of zero variance input costs, where each input cost equals K. Generate four random values $\left( c _ { 1 } , c _ { 2 } , c _ { 3 } \right.$ and $c _ { 4 } )$ from the uniform distribution: $U ( c , 0 . 6 c )$ , where $\ " _ { c } \ "$ is the mean and $\ " 0 . 6 \ "$ is the variance. Denote the vector of high variance classification costs by $\mathbf { C _ { \mathbf { b } } }$ $= [ { \bf \tilde { \tilde { \tau } } } ( { \bf \dot { \tilde { \eta } } } _ { 1 } , { \bf \Phi } _ { 2 } , { \bf \Phi } _ { 3 } ,$ – c4}. corresponding to costs associated with the classifications: $\mathrm { { } ^ { * * } y e s / y e s , \mathrm { { } ^ { * * } y e s / n o , \mathrm { { } ^ { * * } } } }$ $\ " \mathrm { n o / y e s " } \ : \mathrm { a n d } \ : \mathrm { \ " } \mathrm { n o / n o " }$ , respectively. Generate four random values $( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } )$ from the distribution: U(K, 0.6K). Denote the vector of high variance input costs by $\mathbf { X _ { \lambda _ { b } } } = \left[ \begin{array} { l } { \mathbf { \mathrm { r } } _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } } \end{array} \right]$

Step 2. Using BASICGEN, generate three observations corresponding to zero variance input costs and zero variance classification costs, i.e., using X, and $\mathbf { C _ { \lambda } }$

Step 3. Using BASICGEN, generate three observations corresponding to high variance input costs and zero variance classification costs, i.e., using $\mathbf { X } _ { \mathbf { \lambda } }$ and $\mathbf { C _ { \pmb { \nu } } }$

Step 4. Using BASICGEN. generate three observations corresponding to zero variance input costs and high variance classification costs, 1.e., using X, and $\mathbf { C _ { b } }$

Step 5. Using BASICGEN, generate three observations corresponding to high variance input costs and high variance classification costs, r.e., using $\mathbf { X } _ { \mathbf { \lambda } }$ and $\mathbf { C _ { \hat { n } } }$

Step 6. Repeat steps 1 through 5, 30 times, each time using different, randomly generated values for the positive constant $\because \gamma$

Step 7. Stop.

## References

Balakrishnan, A. and A. B. Whinston, “Information Issues in Model Specification," Informatton Systems Research, 2, 4 (1991), 263–286.

, J. C. Moore, R. Pakath and A. B. Whinston, “nformation Tradeoffs in Model Building: A Network Routing Application," Computer Science in Économıcs and Management, 4 (1991), 210– 227

Cendrowska, J.. "PRISM: An Algorithm for Inducıng Modular Rules," Internattonal Journal of Man-Machine Studtes, 27 (1987), 349–370.

Chandler, J., T Liang and I Han, "An Empirical Investigation of Some Data Effects on the Classification Accuracy of PROBIT and ID3," Working Paper, Depar:ment of Accountancy, University of Illinois, 1990.

Dos Santos, B. L. and V. S. Mookerjee, “An Economic Approach to the Development of Inductive Expert Systems," Proceedings of the Twenty-fifth Annual Hawau International Conference on System Sctences, IEEE Computer Society Press, Vol. III (Janua:y 1992), 36–46

and , "Expert System Design: Minimizing Information Acquisition Costs," Decision Support Systems, 9, 2 (1993), 161–181,

Feigenbaum, E., “Expert Systems in the 1980s," in A. Bond (Ed ), State of the Art Report on Machine Intelligence, Pergamon-Infotech, Maidenhead, 1981.

Hall, H. K., J C Moore and A. B. Whinston, “A Theoretical Basis for Expert Systems," in L. Pau (Ed.), Artfictal Intelligence in Economies and Management, Elsevier Science Publishers, 1986, 11-20.

Holsapple, C. and A. B. Whınston, Busıness Expert Systen.s, Irwin, Homewood, IL., 1987.

Hyafil, L and R. Rivest, "Construction of Optimal Binary Dec ision Trees Is NP-complete," Information Processing Leuters, 5, 1 ( 1976), 15–17.

Jacob. V S., J C Moore and A. B. Whinston, “Artificıal Intelligence and the Management Science Practitioner: Rational Choice and Artificial Intelligence " Interfaces. 18, 4 (1988), 24–35.

\_\_ and . , “An Analysis of Human and Computer Decısion-Making Capabilı- tes," Informaton & Munagement, 6, 5 (1989), 247–255.

and "Design of Interaciive Systems: A Formal Approach," Internatonat Journal of Man-Mac hıne Studies, 37 (1992), 23- 46

Kononenko, I. I Bratko and E. Roskar, “Experıments it Automatic Learning of Medıcal Diagnostıc Rules," Technıal Report. Jozef Stefan Institute, Ljubljiana. Yugoslavia, 1984

Liang. T , “A Composite Approach to Inducing Knowledge for Expert System Design," Management Sctence, 38, 1 (1992). 1 -17.

Marschak, J. and R. Radner, Economu Theory of Teams, Cowles Foundation, 1972.

Messier, W. and J Hansen, 'Inducing Rules for Expert Systems Development: An Example Using Default and Bankruptc Data," Management Sctence, 24, 12 (1988), 1403–1415

Michalski, R., "Understanding the Nature of Learning," in R. Michalski, J. G. Carbonell and T. M. Mitchell, (Eds.), Machine Learning. An Artificial Intelligence Approach, Vol. 2, Morgan Kaufmann Inc., CA, 1986, 3–25.

Michie, D., “Inductive Rule Generation in the Context of the Fifth Generation," Proceedıngs of the Second International Machine Learning Workshop, University of Illinois at Urbana-Champaign, 1983.

Mingers, J., “Inducing Rules for Expert Systems—Statistical Aspects," The Professional Statıstician, 5 (1986), 19–24.

, “Expert Systems—Rule Induction with Statistical Data," Journal of the Operational Research Society, 38 (1987), 39–47.

, “An Empirical Comparison of Selection Measures for Decision-Tree Induction,"Machine Learning, 3 (1989), 319–342.

, R. Rao and A. B. Whinston, "Information Processing for a Finite Resource Allocation Mechanism," CMME Working Paper Series, No. 92-9-1, Krannert Graduate School of Management, Purdue University, 1992.

, W. Richmond and A. B. Whinston, “A Decision-Theoretic Approach to Information Retrieval," ACM Transactions on Database Systems, 15, 3 (1990), 311–340.

Moore, J. C. and A. B. Whinston, “A Model of Decision-Making with Sequential Information Acquisition —Part I," Decision Support Systems, 2, 4 (1986), 285–307.

and , “A Model of Decision-Making with Sequential Information Acquisition—Part II," Decision Support Systems, 3, 1 (1987), 47–72.

Niblet, T. and I. Bratko, “"Learning Decision Rules in Noisy Domains," in Research and Development in Expert Systems, Proceedings of the Sixth Technical Conference of the BCS Specialist Group on Expert Systems, Brighton, UK, 1986.

and A. Patterson, ACLS Manual, Intelligent Terminals Ltd., Edinburgh, UK and Champaign, IL, 1982.

Olson, D. and J. Courtney, Decision Support Models and Expert Systems, Macmillan Publishing Company, New York, 1992.

Pearl, J., Heuristics: Intelligent Search Strategies for Computer Problem Solving, Addison-Wesley Publishing Co., Reading, MA, 1984.

Quinlan, J., “Discoverıng Rules by Induction from Large Collections of Examples," in D. Michie (Ed.) Expert Systems in the Micro Electronic Age, Edinburgh University Press, 1979.

“Learning Efficient Classification Procedures and Their Application to Chess Endgames," in Michalski, R., J. G. Carbonell and T. M. Mitchell (Eds.), Machıne Learning. An Artificial Intelligence Approach, Tioga Publishing Company, Palo Alto, 1983.

, “Induction of Decision Trees," Machine Learning, 1 (1986), 81–106.

"Simplifying Decision Trees," International Journal of Man-Machine Studies, 27 (1987), 221-234.

, “Induction, Knowledge and Expert Systems," in J. S. Gero and R. Stanton (Eds.), Artificıal Intelligence Developments and Applications, Elsevier Science Publishers, North-Holland, 1988

Shannon, C. and W. Weaver, The Mathematical Theory of Communication, University of Illinois Press Urbana, 1949 (Published in 1964).

Shapiro, A., Structured Induction in Expert Systems, Turing Institute Press (in association with Addison Wesley Publishing Company), New York, 1987.

Shepherd, B., “An Appraisal of a Decision-tree Approach to Image Classification," Proceedings of the Eighth International Joınt Conference on Artificial Intelligence, Morgan-Kaufmann, Karlsruhe, West Germany, 1983.

Titterington, D., L. Murray, G. Murray, D. Spiegelhalter, A. Skene, J. Habbema and G. Gelpke, “Comparison of Discrimination Techniques Applied to a Complex Data Set of Head Injured Patients," Journat of the Roval Society, A Series, 144 (1981), 144–175.

Turban, E., Decision Support and Expert Systems (3rd ed.), Macmillan Publishing Company, New York, 1993.
