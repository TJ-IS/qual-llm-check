---
otero_id: 11776
otero_key: "6N32APC8"
title: "Stochastic ordering and robustness in classification from a Bayesian network"
authors: "Sung-Ho Kim"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.10.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Stochastic ordering and robustness in classification from a Bayesian network

Sung-Ho Kim\*

Division of Applied Mathematics, Korea Advanced Institute of Science and Technology, Daejeon 305-701, South Korea

Received 7 August 2002; received in revised form 16 October 2003; accepted 16 October 2003 Available online 27 November 2003

## Abstract

Consider a model-based decision support system (DSS) where all the variables involved are binary, each taking on 0 or 1. The system categorizes the probability that a certain variable is equal to 1 conditional on a set of variables in an ascending order of the probability values and predicts for the variable in terms of category levels. Under the condition that all the variables are positively associated with each other, it is shown in this paper that the category levels are robust to the probability values. This robustness is illustrated by a simulated experiment using a variety of model structures where a set of probability values is proposed for a robust classification. A robust classification method is proposed as an alternative when exact or satisfactory probability values are not available.

Keywords: Agreement level; Basic structures of model; Conditional probability; Graphical model; Positive association

## 1. Introduction and motivation

One of the most significant trends over the past 20 years has been the evolution from individual standalone computers to the highly interconnected telecommunication network environment of today. This network environment has enhanced availability of decision support systems (DSSs) to a very large number of users, allowing more rapid exchange of information among the users [14]. Shim et al. [16] point to the importance of model-based DSSs as a powerful tool for decision aid in the web-based information sharing environment. Classification is a form of decision making under a certain loss structure [4], and DSSs for these purposes are in general modelbased (see, for example, Refs. [11,17,18]).

Although model-based DSSs are preferred due to, among others, consistency in decision-making and due to time-efficiency in model evaluation and modification, they are of no use unless they are ready when needed. Constructing a model may take time if a number of random variables are involved in the model and the model structure is not simple. Suppose that a group of users want model-based classifications from a web-based DSS soon after the information about the model structure and a corresponding data set is uploaded. We may not have enough time to go through the full model-building procedure to serve the users. However, we may be able to make reasonable modelbased classifications not from a model which is totally based on data but from a model which is based on data in part and satisfies some condition that will be described in Section 2. We will show in this paper that the classification from the latter model is robust under that condition. We will consider student diagnosis in education as a running example of the classification problem and will elaborate below on the problem in the context of educational testing. Of course, the problem domain can be extended to other classification problems.

In educational testing, test results are used for guessing students’ knowledge states. The need for better understanding of knowledge states calls for statistical technologies for linking performance outcomes to knowledge states [13]. Some of the technologies are used in the form of graphical models [19] whose model structures are represented in graphs, each of which consists of vertices and edges. The vertices represent random variables and the edges associative or causal relationships among the variables. The edges are directed if the relationships between the variables can be interpreted as causal and not directed otherwise. Since the relationship between abilities or knowledge units (KUs) is causal or hierarchical and the relationship between task performance and knowledge is causal, we will consider graphical models whose model structures are represented in the form of a Bayesian network [7,15].

We will call the graphical model of knowledge states and task performance a task performance model. All the variables considered in this paper are binary. The outcome of the task performance is classified as success (1) or failure (0) and the knowledge state good enough (1) or poor (0) for a given set of test items. If a student possesses a good enough knowledge for a test item, he or she has a high probability of a successful answer; otherwise, the probability will be low. When we diagnose a student’s knowledge state based on his or her test result, a best way is using the conditional probability that a certain KU is in a good enough state given his or her test result. A statistical technique for computing the conditional probability is what is called evidence propagation [12] and computer programs such as HUGIN [1] and ERGO [5] are available for the computing.

In reality, building a task performance model is, in most cases, time-consuming and the quality of the probability estimates for the model may often be unsatisfactory. However, if we are interested in diagnosing a student’s knowledge state in terms of class levels rather than the conditional probability, this concern may be safely resolved. As an example in this line of work, Kim [9] developed a task performance model [13] based on a test data set from a Mathematics test for a group of the 7th grade students and diagnosed the students for nine cognitive attributes or KUs. The diagnosis was carried out by classifying the students into one of five levels of the knowledge state for each KU. About 76% of the students said that the model-based diagnosis was helpful in their catch-up efforts. Of course, the test quality must be good enough for a successful diagnosis, and if the diagnosis is served sooner after the test, we can expect the better effect of the diagnosis.

In this paper, we are interested in a classification problem where the class levels are in accordance with the rank order of the probability values of a random variable. Thus, we have only to deal with relative magnitudes of the probability. This leads us to the notion of stochastic ordering which, incorporated with the rank-based classification, will play an important role in addressing the issue of robustness in classification. It is anticipated that the level of robustness varies according to the model structure. In order to see a possible range of the robustness in classification, a simulation experiment is carried out over a variety of models.

This paper is organized in four sections. Section 2 presents theorems showing that positive association among a set of binary variables preserves a stochastic ordering among the conditional probabilities of the binary variables. This result is carried over to Section 3 in the form of a simulated experiment in an effort to fathom the robustness of classification which is made based on the ordering of the conditional probabilities of an interested variable for a given data set. The simulation result shows a very high level of robustness when the variables are positively associated. Section 4 concludes the paper with a brief guideline of the proposed robust classification method.

## 2. Positive association and order preservation

All the variables considered in this paper are binary, taking on 0 or 1. We will use U for unobservable variables and X for observable variables. In educational testing, U may be regarded as a random indicator of possessing a certain knowledge and X an item-score. Vectors are bold-faced. For a pair of nvectors u and v of the same length, we write $\mathbf { u } \preceq \mathbf { v }$ when $u _ { i } \leq \nu _ { i }$ for $i = 1 ; . . . , n ,$ , and write $ { \mathbf { u } } { - }  { \mathbf { v } } \mathrm { i f }  { \mathbf { u } } \preceq  { \mathbf { v } }$ and $u _ { i } < \nu _ { i }$ for some $i = 1 , . . . , n$

![](/api/attachments/6N32APC8/fulltext/images/6508153a89094d8ea735a36fd18ee65a749a4e5d06c25ee22c3479075800b052.jpg)  
Fig. 1. A Bayesian network where U variables are latent and X variables observable.

In a directed independence graph or a Bayesian network such as the graph in Fig. 1, if a pair of nodes a and $b$ are connected by an arrow with the arrow heading towards b from $^ { a , }$ we call node a a parent node of node b and call node b a child node of node a. For instance, in Fig. 1, node $U _ { 1 }$ is the only parent node of nodes $U _ { 2 }$ and $U _ { 3 } ,$ and node $X _ { 7 }$ has three parent nodes $U _ { 4 ; } U _ { 5 } ,$ , and $U _ { 6 }$ . If a node does not have any parent node, it is called a root node. $U _ { 1 }$ is the only root node in the figure. If two nodes are connected by an arrow we say that the two nodes are neighbors or that they are connected directly each other.

Theorem 1. Let U and X be binary variables, taking on values 0 or 1. If

$$
0 <   P (U = 1) <   1 \text {   and   } 0 <   P (X = 1) <   1,\tag{1}
$$

then the following two inequalities are equivalent:

$$
P (X = 1 \mid U = 0) <   P (X = 1 \mid U = 1)\tag{2}
$$

$$
P (U = 1 \mid X = 0) <   P (U = 1 \mid X = 1).\tag{3}
$$

Proof. First, we assume inequality (2). When Eq. (1) holds, expression (3) is equivalent to

$$
\frac {P (X = 1 \mid U = 1)}{P (X = 1)} > \frac {P (X = 0 \mid U = 1)}{P (X = 0)}.
$$

The left-hand side and the right-hand side of this inequality are, respectively, equal to

$$
l = \frac {P (X = 1 \mid U = 1)}{P (U = 1) P (X = 1 \mid U = 1) + P (U = 0) P (X = 1 \mid U = 0)}
$$

and

$$
r = \frac {P (X = 0 \mid U = 1)}{P (U = 1) P (X = 0 \mid U = 1) + P (U = 0) P (X = 0 \mid U = 0)}
$$

Since $0 < P ( U = 1 ) < 1$ , we can see, by condition (2), that

$$
l > 1 \text {   and   } r <   1.
$$

Thus, Eq. (3) follows.

The proof for the other direction is the same as above except that U and X are exchanged in the expressions (2) and (3). 5

Under condition (2), we have

$$
\frac {P (X = 1 \mid U = 1) P (X = 0 \mid U = 0)}{P (X = 0 \mid U = 1) P (X = 1 \mid U = 0)} > 1,
$$

that is, U and X are positively associated.

We can extend this result to a situation where $X _ { i } ; i =$ $1 , 2 , . . . , I ,$ are influenced by multiple $U ^ { \ast } { \mathbf { s } } ,$ i.e., the conditional probability of $X _ { i }$ is subject to the states of some of $U _ { k } ; k = 1 , 2 , . . . . , K$ only. We may assume a Bayesian network for $U _ { k } , k { = } 1 , 2 { , } { \ldots } k$ as in Fig. 1. Note that since the conditional probability of $X _ { i }$ is subject to the states of $\{ U _ { k } \} _ { k = 1 } ^ { K }$ only, $X _ { i , } i { = } 1 , 2 , . . . , I ,$ are independent given $U _ { k } , k { = } 1 , 2 { \mathrm { , . ~ . . , } } K .$

Theorem 2. Let $X { = } ( X _ { 1 } , . . . , X _ { \mathrm { I } } )$ and $\pmb { U } \mathrm { = } ( U _ { 1 , \dots } , U _ { K } )$ where all the $X _ { i } { \dot { s } }$ and $U _ { k } { } ^ { \ ' }$ are binary, taking on 0 or 1. Then the following two statements are equivalent.

$$
\text {(i)} \text {   For   } i = 1, 2, \dots , I,
$$

$$
P (X _ {i} = 1 \mid \mathbf {u}) <   P (X _ {i} = 1 \mid \mathbf {v}), \text {   when   } \mathbf {u} \prec \mathbf {v}\tag{4}
$$

(ii) For $k = l , 2 , . . . . \ : K ,$

$$
P (U _ {k} = 1 \mid \mathbf {x}) <   P (u _ {k} = 1 \mid \mathbf {y}), \text {   when   } \mathbf {x} \prec \mathbf {y}.\tag{5}
$$

The strict inequality ( < ) in both Eqs. (4) and (5) may be replaced by the plain inequality ( V ).

Proof. We remove the kth component of U and denote the resulting vector by $\mathbf { U } ( \mathbf { \Sigma } _ { k } )$ . We will prove only that condition (i) implies condition (ii) since the proof for the other direction is the same except that X and U are exchanged in the inequalities (4) and (5). To avoid confusion, we write the marginal probability of $U$ as $P _ { U } ( \cdot )$ , the conditional probability of U conditional on X as $P _ { U | X } ( \cdot | \cdot )$ and analogously for $P _ { X } ( \cdot )$ and $P _ { X | U } ( \cdot | \cdot )$

$$
\begin{array}{l} P _ {U _ {k} | \mathbf {X}} (1 | \mathbf {y}) - P _ {U _ {k} | \mathbf {X}} (1 | \mathbf {x}) \\ = \frac {P (U _ {k} = 1) \sum_ {\mathbf {u} _ {(k)}} P (\mathbf {u} _ {(k)} \mid U _ {k} = 1) P _ {\mathbf {x} | \mathbf {u}} (\mathbf {y} \mid u _ {k} = 1 , \mathbf {u} _ {(k)})}{\sum_ {\mathbf {u}} P _ {\mathrm{U}} (\mathbf {u}) P _ {\mathrm{X} | \mathrm{U}} (\mathbf {y} \mid \mathbf {u})} \\ - \frac {P (U _ {k} = 1) \sum_ {\mathbf {u} _ {(k)}} P (\mathbf {u} _ {(k)} \mid U _ {k} = 1) P _ {\mathrm{X} | \mathrm{U}} (\mathbf {x} \mid u _ {k} = 1 , \mathbf {u} _ {(k)})}{\sum_ {\mathbf {u}} P _ {\mathrm{U}} (\mathbf {u}) P _ {\mathrm{X} | \mathrm{U}} (\mathbf {x} \mid \mathbf {u})} \\ = \frac {b}{a} - \frac {d}{c}, \end{array}\tag{6}
$$

where $a , b , c ,$ d are equal to the corresponding parts in expression (6).

$$
\begin{array}{l} \frac {b c - a d}{P (U _ {k} = 1)} \\ = \sum_ {\mathbf {u} _ {(k)}} P (\mathbf {u} _ {(k)} \mid U _ {k} = 1) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {y} \mid u _ {k} = 1, \mathbf {u} _ {(k)}) \\ \times \sum_ {\mathbf {u}} P _ {\mathbf {U}} (\mathbf {u}) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {x} \mid \mathbf {u}) - \sum_ {\mathbf {u} _ {(k)}} P (\mathbf {u} _ {(k)} \mid U _ {k} = 1) \\ \times P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {x} \mid u _ {k} = 1, \mathbf {u} _ {(k)}) \sum_ {\mathbf {u}} P _ {\mathbf {U}} (\mathbf {u}) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {y} \mid \mathbf {u}) \\ = \sum_ {\mathbf {u} _ {(k)}} \sum_ {\mathbf {v}} P (\mathbf {u} _ {(k)} \mid U _ {k} = 1) P _ {\mathbf {U}} (\mathbf {v}) \\ \times (P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {y} \mid u _ {k} = 1, \mathbf {u} _ {(k)}) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {x} \mid \mathbf {v}) \\ - P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {x} \mid u _ {k} = 1, \mathbf {u} _ {(k)}) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {y} \mid \mathbf {v})) \\ = \sum_ {\mathbf {u} _ {(k)}} \sum_ {\mathbf {v} _ {(k)}} P (\mathbf {u} _ {(k)} \mid U _ {k} = 1) P _ {\mathbf {U}} (v _ {k} = 0, \mathbf {v} _ {(k)}) \\ \times (P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {y} \mid u _ {k} = 1, u _ {(k)}) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {x} \mid v _ {k} = 0, \mathbf {v} _ {(k)}) \\ - P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {x} \mid u _ {k} = 1, \mathbf {u} _ {(k)}) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {y} \mid v _ {k} = 0, \mathbf {v} _ {(k)})) \\ + \sum_ {\mathbf {u} _ {(k)}} \sum_ {\mathbf {v} _ {(k)}} P (\mathbf {u} _ {(k)} \mid U _ {k} = 1) P (v _ {k} = 1, \mathbf {v} _ {(k)}) \\ \times (P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {y} \mid u _ {k} = 1, \mathbf {u} _ {(k)}) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {x} \mid v _ {k} = 1, \mathbf {v} _ {(k)}) \\ - P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {x} \mid u _ {k} = 1, \mathbf {u} _ {(k)}) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {y} \mid v _ {k} = 1, \mathbf {v} _ {(k)})) \end{array}\tag{7}
$$

After a simple computation, we can see that the second double summation in Eq. (7) is equal to zero, and we may rewrite the first double summation as

$$
\begin{array}{l} \sum_ {\mathbf {u} _ {(k)}} \sum_ {\mathbf {v} _ {(k)}} P (\mathbf {u} _ {(k)} \mid U _ {k} = 1) P _ {\mathbf {U}} (v _ {k} = 0, \mathbf {v} _ {(k)}) \\ \quad \times P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {y} \mid u _ {k} = 1, \mathbf {u} _ {(k)}) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {x} \mid v _ {k} = 0, \mathbf {v} _ {(k)}) \\ \quad - \sum_ {\mathbf {u} _ {(k)}} \sum_ {\mathbf {v} _ {(k)}} P (\mathbf {v} _ {(k)} \mid V _ {k} = 1) P _ {\mathbf {U}} (u _ {k} = 0, \mathbf {u} _ {(k)}) \\ \quad \times P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {y} \mid u _ {k} = 0, \mathbf {u} _ {(k)}) P _ {\mathbf {X} \mid \mathbf {U}} (\mathbf {x} \mid v _ {k} = 1, \mathbf {v} _ {(k)}), \end{array}\tag{8}
$$

which takes on, when $\mathbf { X } { \prec } \mathbf { \vec { y } } ,$ positive values by condition (i) of the theorem.

If we replace the strict inequality in condition (i) of the theorem with V , then by applying the same argument as above, we can see from Eq. (8) that the strict inequality ( < ) must be replaced in expression (5) with V . This completes the proof. 5

Inequality (4) is equivalent to that

$$
\frac {P (\mathbf {v} \mid X _ {i} = 1)}{P (\mathbf {u} \mid X _ {i} = 1)} > \frac {P (\mathbf {v})}{P (\mathbf {u})} > \frac {P (\mathbf {v} \mid X _ {i} = 0)}{P (\mathbf {u} \mid X _ {i} = 0)}.
$$

This inequality says that $\mathbf { U } = \mathbf { v }$ is more likely than U = u when $X _ { i } = 1$ than when $X _ { i } = 0$ . Furthermore, we can compare the likeliness of $U _ { k } { = } 1$ for individual $U _ { k } \mathbf { \bar { s } }$ as in Theorem 2.

It is worth noting that Theorem 2 holds for any relationship among $U _ { k }$ as long as $0 < P ( U _ { k } = 1 ) < 1$ $k { = } 1 , \ 2 , . . . . \ K$ and $0 < P ( X _ { i } = 1 ) < 1$ , i= 1, 2,. . ., I. When the < and  in expression (4) are replaced by $\leq \mathrm { ~ \ a n d ~ \alpha \preceq }$ , respectively, the expression actually means that the conditional distribution of $X _ { i }$ given U = u is stochastically larger than that of $X _ { i }$ given U = v. Holland and Rosenbaum [6] discuss properties concerning positive association among the X variables when the X variables are conditionally stochastically ordered given U. Junker and Ellis [8] characterize such X variables in more generic terms such as conditional association and vanishing conditional dependence.

Let a be a vector of $0 \mathrm { { ^ , } s }$ or 1’s, and denote by d(a) the number of 1-components in vector a.

Theorem 3. For $i , j = I , 2 , \ldots$ I, suppose that

$$
P (X _ {i} = 1 \mid \mathbf {u}) = P (X _ {j} = 1 \mid \mathbf {v}) \text { whenever } \delta (\mathbf {u}) = \delta (\mathbf {v}).
$$

Then we have, for $k { = } 1 , 2 { \mathrm { , . . . , } } K ,$ that

$$
P _ {U _ {k} | \mathbf {X}} (1 | \mathbf {x}) = P _ {U _ {k} | \mathbf {X}} (1 | \mathbf {y}) \text { whenever } \delta (\mathbf {x}) = \delta (\mathbf {y}).
$$

Proof. We may apply the same argument as for the Proof of Theorem 2 and show that the value of expression (8) equals zero. According to the condition of the theorem, $X _ { i } ; ~ i = 1 , ~ 2 , . ~ . . , ~ I ,$ are symmetric in index. So in Eq. (8), we may exchange x and y with each other in the second double summation. From this, follows the desired result. 5

The condition of this theorem is very strong, and if the condition becomes milder as follows:

$$
\begin{array}{l} P _ {X _ {i} | \mathbf {U}} (1 | \mathbf {u}) = P _ {X _ {i} | \mathbf {U}} (1 | \mathbf {v}) \text {   and, } \\ \text { for   } i \neq j, P _ {X _ {i} | \mathbf {U}} (1 | \mathbf {u}) \neq P _ {X _ {j} | \mathbf {U}} (1 | \mathbf {v}) \end{array}\tag{9}
$$

when $\delta ( { \mathbf { u } } ) = \delta ( { \mathbf { v } } )$ , then the result of the theorem is not guaranteed as illustrated in the example below.

Example 2.1. Consider a Bayesian network of three binary latent variables, $U _ { 1 } , U _ { 2 } , U _ { 3 } ,$ and three binary observables, $X _ { 1 } , X _ { 2 } , X _ { 3 }$ , whose relationship is depicted in Fig. 2 and whose conditional probabilities are listed in Table 1. The probability model as in Table 1 satisfies condition (9).

$P _ { U _ { k } | \mathbf { X } } ( 1 | \mathbf { x } )$ are listed in Table 2. For the configurations x with $\delta ( \mathbf { x } ) = 1$ , we see different values of $P _ { U _ { k } | \mathbf { X } } ( 1 | \mathbf { x } )$ , for each $k = 1 , 2 , 3$ . Under condition (9), the values of $P _ { U _ { k } | \mathbf { X } } ( 1 | \mathbf { x } )$ are subject to the structural relationship between U and X. Although the difference in value is subdued when $\delta ( \mathbf { x } ) = 2$ , we also see a similar result for the configurations x.

![](/api/attachments/6N32APC8/fulltext/images/32a6f417b1a7f4a976e17060bc28deace6f6f3a4e200daca48a40edf0f876064.jpg)  
Fig. 2. The Bayesian network considered in Example 2.1.

The conditional probabilities for the nodes in Fig. 2

<table><tr><td> $P(U_1=1)=0.8$ </td><td> $P(X_1=1|U_1=1,U_2=0)=0.3$  $P(X_1=1|U_1=1,U_2=1)=0.9$ </td></tr><tr><td> $P(U_2=1|U_1=0)=0.15$ </td><td></td></tr><tr><td> $P(U_2=1|U_1=1)=0.85$ </td><td> $P(X_2=1|U_1=0,U_3=0)=0.15$  $P(X_2=1|U_1=0,U_3=1)=0.25$ </td></tr><tr><td> $P(U_3=1|U_1=0,U_2=0)=0.1$ </td><td> $P(X_2=1|U_1=1,U_3=0)=0.25$ </td></tr><tr><td> $P(U_3=1|U_1=0,U_2=1)=0.15$ </td><td> $P(X_2=1|U_1=1,U_3=1)=0.9$ </td></tr><tr><td> $P(U_3=1|U_1=1,U_2=0)=0.15$ </td><td></td></tr><tr><td> $P(U_3=1|U_1=1,U_2=1)=0.9$ </td><td> $P(X_3=1|U_2=0,U_3=0)=0.05$  $P(X_3=1|U_2=0,U_3=1)=0.1$ </td></tr><tr><td> $P(X_1=1|U_1=0,U_2=0)=0.1$ </td><td> $P(X_3=1|U_2=1,U_3=0)=0.1$ </td></tr><tr><td> $P(X_1=1|U_1=0,U_2=1)=0.3$ </td><td> $P(X_3=1|U_2=1,U_3=1)=0.9$ </td></tr></table>

Theorem 2 implies that, if we are interested in the ordering of $P _ { U _ { k } | \mathbf { X } } ( 1 | \mathbf { x } )$ for a set of x values that are totally ordered in terms of $\preceq$ , we can order them without regard to the exact values of $P ( X _ { i } = 1 | \mathbf { u } )$ . This fact throws light on the possibility that students may be ordered to some extent in accordance with the level of a certain KU without resort to the exact (mean) values of the probabilities of correct responses conditional on every possible state of the test-relevant KUs (denoted by U). For instance, for each of the six KUs as symbolized by $U _ { k }$ in Fig. 1, we can arrange reasonably well a group of students in order of the knowledge level without knowing the exact values of $P ( X _ { i } = 1 | \mathbf { u } )$ where $X _ { i }$ symbolizes the score of item i. We can see in Table 2 that the inequality (5) holds when the x values are ordered.

In reality, the item-score patterns X may not be fully ordered for a group of students. For a threeitem test set as considered in Table 2, all the six patterns in the first column of the table are possible for any group of students. However, it is important to note that, if more KUs in the test domain are causally related among themselves, then it is more likely that the item-score patterns of the students are ordered. Another point of view is that the item-score patterns may be in accordance with the item difficulty levels. For instance, as for the test set of Table 2, suppose that items 1, 2, and 3 are ordered from easy to difficult. Then, the item-score patterns such as (0,1,0), (0,0,1), (1,0,1), and (0,1,1) are less likely than $( 1 , 0 , 0 ) , ( 1 , 1 , 0 ) , ( 1 , 1 , 1 )$ , where the latter patterns are well ordered. This causal or hierarchical relation among the KUs and the item difficulty level, in addition to the positive association property of Theorem 2, lead to the robustness of classification. We will explore the level of robustness by a simulation experiment in the next section.

Values of $P _ { U _ { k } | \mathbf { x } } ( 1 | \mathbf { x } )$ as obtained from the model with the corresponding structure and the conditional probabilities given in Fig. 2 and Table 1

<table><tr><td rowspan="2">x</td><td colspan="3"> $P_{U_k}|_x(1|x)$ </td></tr><tr><td>k=1</td><td>k=2</td><td>k=3</td></tr><tr><td>(1,0,0)</td><td>0.780</td><td>0.596</td><td>0.082</td></tr><tr><td>(0,1,0)</td><td>0.572</td><td>0.159</td><td>0.322</td></tr><tr><td>(0,0,1)</td><td>0.453</td><td>0.496</td><td>0.458</td></tr><tr><td>(1,1,0)</td><td>0.954</td><td>0.819</td><td>0.692</td></tr><tr><td>(1,0,1)</td><td>0.960</td><td>0.966</td><td>0.878</td></tr><tr><td>(0,1,1)</td><td>0.956</td><td>0.937</td><td>0.956</td></tr></table>

## 3. A simulation experiment

We will begin a simulation experiment with a good deal of variations of the model in Fig. 1. In the simulation, we presuppose that we predict the states of $U _ { k } , k { = } 1 , . . . , 6 .$ , in terms of five levels of the $P ( U _ { k } { = } 1 | \mathbf { X } { = } \mathbf { x } )$ , where the levels are based on the data for X to which a given model fits. For a set of data $\left\{ { \bf x } _ { j } \right\} _ { j } ^ { n } = 1$ with $\mathbf { x } _ { j } = ( x _ { j 1 } , . . . , x _ { j 9 } )$ , we obtain a set of conditional probabilities $\{ ( P ( U _ { k } = 1 | \mathbf { x } _ { \mathrm { i } } )$ $k { \in } \{ 1 , . . . . , 9 \} ) \} _ { j = 1 } ^ { n }$ , and then arrange $\{ P ( U _ { k } = 1 | \mathbf { x } _ { j } ) \} _ { j = 1 } ^ { \bar { n } }$ in the descending order and rank them from the largest down. We then categorize the states of $U _ { k } ,$ $\{ P _ { U _ { k } | \mathbf { X } } ( 1 | \mathbf { x } ) \} _ { k = 1 } ^ { 6 }$ , for each $k ,$ into five levels from 1 through 5, 1 for the first 20% of the cases, 2 for the next 20% of the cases, and so on.

Recall that $U _ { k }$ is the random indicator of possessing the knowledge of KU k. Then we may interpret $P ( U _ { k } { = } 1 )$ as the probability of possession of KU k that is required for a given task. So, from the view-point of subjective probability [10], we may regard the probability as a level of familiarity with the KU, 1 as a mastery level, 5 as a bottom level, and the intermediate values for the intermediate levels.

Our interest is in robustness of the classification for the knowledge states. The probability model for the Bayesian network as in Fig. 1 can be expressed as a product of $P ( V { = } z | p a ( V ) )$ where $p a ( V )$ denotes the set of the parent nodes of V. The robustness is with respect to the set of the conditional probabilities $\{ P ( V { = } z | p a ( V ) ) \} _ { V \in \varPsi }$ where W is the set of all the variables involved in a given Bayesian network. We try many different values on the conditional probabilities under condition (4) as described below and see how the predicted classes vary across a wide range of the values of the conditional probabilities.

For convenience’ sake, we call by model 1 the model in Fig. 1. We will consider two versions of this model, version 1 and version 2. In version 1, we use a fixed set of numbers for the conditional probabilities $\{ P ( V { = } \nu | p a ( V ) ) \} _ { V \in \psi }$ of the model, while we use a wide range of numbers between 0.01 and 0.99 for the conditional probabilities in version 2. In version 2, the values for $P ( V { = } 1 | p a ( V )$ takes on 0 values only have mean 0.12 with standard deviation 0.037, those for $P ( V { = } 1 | p a ( V )$ are in perfect states range from about 0.1 up to 0.99, and the values for the other imperfect states of $p a ( V )$ are selected so that condition (4) may be satisfied. The wide range for the perfect state of $p a ( V )$ is in an effort to reflect the real situation as much as possible. The fixed set of values for version 1 is listed in Table 3, where we use V instead of U and X to denote observable and unobservable random variables. In the expression $\{ P ( V { = } \nu | p a ( V ) ) $ , V and pa may all be unobservable when they are for KUs. We can easily see that the values $\{ P ( V { = } \nu | p a ( V ) ) \} _ { V \in \varPsi }$ in Table 3 satisfy condition (4). For instance, as for $V _ { 4 } ,$ the vectors of $( \nu _ { 1 } , \ \nu _ { 2 } , \ \nu _ { 3 } ) , \ ( 1 , 0 , 0 )$ and (1,1,0) are ordered, and $P ( V _ { 4 } = 1 | V _ { 1 } = 1$ , V<sub>2</sub> = 0, $V _ { 3 } = 0 ) = 0 . 1 5$ $< P ( V _ { 4 } = 1 | V _ { 1 } = 1$ $V _ { 2 } = 1$ $V _ { 3 } = 0 ) = 0 . 2 5$ . The values in this table were found after a number of trials with many different values between 0.01 and 0.99 under the positive association condition (Eq. (4)).

In the simulation, we compare the classifications between the two versions of a model. Suppose that the classifications are made for N students who took a given test for which model 1 is appropriate with nine test items and six KUs that are relevant to the test. For the given model, we denote by $Y _ { h j k }$ the predicted class by version h for student j regarding KU k and let $D _ { j k } { = } Y _ { 2 j k } { - } Y _ { 1 j k }$ Since the class levels are labelled 1 through 5, we have that $- 4 \leq D _ { j k } \leq 4$ From the distribution of D, we can define a measure of agreement between the two sets of predictions.

Table 3 The (conditional) probabilities for the version 1 of a model

$$
P (V _ {1} = 1) = 0. 5 5
$$

$$
P (V _ {3} = 1 \mid v _ {1}, v _ {2}) = \left\{ \begin{array}{l l} 0. 1 & \text { if } s _ {2} = 0 \\ 0. 1 5 & \text { if } s _ {2} = 1 \\ 0. 6 5 & \text { if } s _ {2} = 2 \end{array} \right.
$$

$$
P \left(V _ {5} = 1 \mid v _ {1}, v _ {2}, v _ {3}, v _ {4}\right) = \left\{ \begin{array}{l l} 0. 1 & \text { if } s _ {4} = 0 \\ 0. 1 5 & \text { if } s _ {4} = 1 \\ 0. 2 5 & \text { if } s _ {4} = 2 \\ 0. 3 5 & \text { if } s _ {4} = 3 \\ 0. 6 5 & \text { if } s _ {4} = 4 \end{array} \right.
$$

$$
\begin{array}{l} P (V _ {2} = 1 \mid V _ {1} = v _ {1}) = \left\{ \begin{array}{l l} 0. 1 5 & \text { if } v _ {1} = 0 \\ 0. 6 5 & \text { if } v _ {1} = 1 \end{array} \right. \\ P (V _ {4} = 1 \mid v _ {1}, v _ {2}, v _ {3}) = \left\{ \begin{array}{l l} 0. 1 & \text { if } s _ {3} = 0 \\ 0. 1 5 & \text { if } s _ {3} = 1 \\ 0. 2 5 & \text { if } s _ {3} = 2 \\ 0. 6 5 & \text { if } s _ {3} = 3 \end{array} \right. \end{array}
$$

$$
P (V _ {6}) = 1 \mid v _ {1}, v _ {2}, v _ {3}, v _ {4}, v _ {5} = \left\{ \begin{array}{l l} 0. 1 & \text { if } s _ {5} = 0 \\ 0. 1 5 & \text { if } s _ {5} = 1 \\ 0. 2 5 & \text { if } s _ {5} = 2 \\ 0. 3 5 & \text { if } s _ {5} = 3 \\ 0. 4 5 & \text { if } s _ {5} = 4 \\ 0. 6 5 & \text { if } s _ {5} = 5 \end{array} \right.
$$

$$
P (V _ {7} = 1 \mid v _ {1}, v _ {2}, v _ {3}, v _ {4}, v _ {5}, v _ {6}) = \left\{ \begin{array}{l l} 0. 1 & \text { if } s _ {6} = 0 \\ 0. 1 5 & \text { if } s _ {6} = 1 \\ 0. 2 & \text { if } s _ {6} = 2 \\ 0. 3 & \text { if } s _ {6} = 3 \\ 0. 4 & \text { if } s _ {6} = 4 \\ 0. 5 & \text { if } s _ {6} = 5 \\ 0. 6 5 & \text { if } s _ {6} = 6 \end{array} \right.
$$

In this table, we use V instead of U and X to represent a random variable. For convenience’ sake, we write $P ( V _ { 3 } = 1 | \nu _ { 1 } , \nu _ { 2 } )$ for $P ( V _ { 3 } = 1 | V _ { 1 } = \nu _ { 1 }$ $V _ { 2 } = \nu _ { 2 } )$ and let $\begin{array} { r } { s _ { k } = \sum _ { i = 1 } ^ { k } \nu _ { i } . } \end{array}$

For KU $k ,$ we can express the relative frequencies of D as

$$
r _ {k d} = \frac {\text { the   number   of   cases   that } D _ {j k} = d}{N}.
$$

These $r _ { k d }$ values are obtained for each set of the conditional probabilities for version 2 of a model.

Also, by generating 50 different sets of conditional probabilities for version 2, the average of the 50 accruing $r _ { k d }$ values was obtained for each k (denote it by $\bar { r } _ { k } )$ . The averages for model 1 are listed in Table 4, and the table is obtained in the following procedure:

(a) For version 1 of the model, we use the probability values as listed in Table 3, where the value which is used for a variable, say $V ^ { * }$ , is determined by the number of parent variables of $V ^ { * }$ and the number of the parent variables whose values are equal to 1.

(b) Version 2 is regarded as a model from the real world, and so we randomly generate any real number between 0.01 and 0.99 for each variable in such a way that the positive association condition (Eq. (4)) is satisfied.

Table 4 $\bar { r } _ { k }$ values for model 1

<table><tr><td> $U_i$ </td><td> $\bar{r}_{-4}$ </td><td> $\bar{r}_{-3}$ </td><td> $\bar{r}_{-2}$ </td><td> $\bar{r}_{-1}$ </td><td> $\bar{r}_0$ </td><td> $\bar{r}_1$ </td><td> $\bar{r}_2$ </td><td> $\bar{r}_3$ </td><td> $\bar{r}_4$ </td><td> $\sum_{d=-1}^{1} \bar{r}_d$ </td></tr><tr><td> $U_1$ </td><td>0.000</td><td>0.000</td><td>0.003</td><td>0.106</td><td>0.734</td><td>0.142</td><td>0.015</td><td>0.000</td><td>0.000</td><td>0.982</td></tr><tr><td> $U_2$ </td><td>0.000</td><td>0.000</td><td>0.002</td><td>0.109</td><td>0.727</td><td>0.153</td><td>0.009</td><td>0.000</td><td>0.000</td><td>0.989</td></tr><tr><td> $U_3$ </td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.066</td><td>0.809</td><td>0.123</td><td>0.001</td><td>0.000</td><td>0.000</td><td>0.998</td></tr><tr><td> $U_4$ </td><td>0.000</td><td>0.000</td><td>0.005</td><td>0.096</td><td>0.743</td><td>0.148</td><td>0.008</td><td>0.000</td><td>0.000</td><td>0.987</td></tr><tr><td> $U_5$ </td><td>0.000</td><td>0.005</td><td>0.035</td><td>0.082</td><td>0.702</td><td>0.143</td><td>0.033</td><td>0.000</td><td>0.000</td><td>0.927</td></tr><tr><td> $U_6$ </td><td>0.000</td><td>0.001</td><td>0.005</td><td>0.074</td><td>0.795</td><td>0.115</td><td>0.009</td><td>0.000</td><td>0.000</td><td>0.984</td></tr><tr><td>Average</td><td>0.000</td><td>0.001</td><td>0.008</td><td>0.089</td><td>0.752</td><td>0.137</td><td>0.012</td><td>0.000</td><td>0.000</td><td>0.978</td></tr></table>

(c) Once the probability values are assigned to all the variables of the model in Fig. 1, we generate a random vector $( U _ { 1 } , \ U _ { 2 } , . . . , \ U _ { 6 } , \ X _ { 1 } , . . . , \ X _ { 9 } )$ following the direction of arrows one after another by applying the Monte-Carlo method and repeat this generation until the Nth such vector is obtained. After generating these N vectors, we remove the first 6 U values in each vector and use the remaining X values only since these X variables only are assumed observable. Recall that the U variables are for KUs and the X variables for item-scores. These N vectors of the X variables are treated as a data set of size N from the version 2 of the model. We denote the jth of these vectors by $\mathbf { X } _ { j } .$ In other words, we regard $\mathbf { X } _ { j }$ as the item-score vector of the jth student.

(e) We repeat the steps b– d 50 times and get the average $( \bar { r } _ { k d } )$ of the $r _ { k d }$ values for each k and $d .$

(d) We obtain $\{ P ^ { h } ( U _ { k } = 1 | \mathbf { x } _ { j } ) ; k = 1 , . . . , 6 , j = 1 , . . . , N \}$ from version h of the model for $h = 1 , 2$ . For each $h = 1 , ~ 2$ , we then obtain, $y _ { h j k } , \ j = 1 , . . . , \ 6$ rankordering the $P ^ { h }$ values as in the first paragraph of this section. From these Y values, we can obtain the $r _ { k d }$ values for $k { = } 1 , . . . , 6 \ d { = } - 4 , . . . , 4 .$

Table 4 is obtained with $n = 1 0 , 0 0 0$ , which is large enough for comparing the predictions that are made in terms of five category levels. For a given model structure, we generated 50 different sets of probability values and the corresponding data sets to obtain the $\bar { r } _ { k d }$ values. ${ \mathrm { S o } } ,$ for each k, we may regard these $5 0 ~ \bar { r } _ { k d }$ values as random observations from a distribution which is defined over the closed interval [0,1]. Therefore, the $\bar { r } _ { k d }$ value can be used as an unbiased estimate of $P ( D _ { 1 k } = d )$ . We can have a better approximation to $P ( D _ { 1 k } = d )$ with a larger number of repetition for ${ \bar { r } } _ { k d } ,$ but 50 is large enough in the context of the Central Limit Theorem if we are interested in $P ( D _ { 1 k } = d )$ rather than in the distribution $r _ { k d }$ of itself.

It is indicated in Table 4 that on average, the classifications from the two versions exactly agree for about 75% of the cases (see the column of $\bar { r } _ { 0 }$ in the table) and the last column of the table shows that almost all the classifications agree up to one class level. The average of the six values in the last column is 0.978. This suggests that almost all of the classifications for the knowledge states may be different only up to one class level.

Further simulations were carried out to investigate how the agreement level varies across the model structures. In these simulations also, the sample size (N) is 10,000 and 50 different sets of conditional probabilities are used for the version 2 of a model. It is usually the case that the KUs are related each other according to their intrinsic nature and that multiple KUs are required for a test item to be solved. For example, in Fig. 1, it is indicated that the state of KU 3 is influenced by the state of KUs 1 and 2 and similarly for the other KUs and that test item 1 requires KU 1 only while test item 7 requires KUs $4 , 5 ,$ , and 6. In this figure, six items tap only one KU and the other three tap three KUs.

When the KUs are connected together in a model, the conditional probability of a KU depends upon

all the item-score variables (X’s). For example, although $U _ { 1 }$ in Fig. 1 is the only neighbor of $X _ { 1 } ,$ $P ( U _ { 1 } = 1 | x _ { 1 , \cdot } \cdot \cdot , x _ { 9 } ) \not = P ( U _ { 1 } = 1 | x _ { 1 } )$ . It looks likely that $X _ { 1 }$ influences most upon the conditional probability $P ( U _ { 1 } = 1 | x _ { 1 , \cdot } \dots x _ { 9 } )$ , but it is time-consuming to compute the amount of the influence. The influence upon the conditional probability of a node is subject to the model structure in the neighborhood of the node. If $U _ { 1 }$ is isolated from the other U variables and is tapped by $X _ { 1 }$ only, then $P ( U _ { 1 } = 1 | x _ { 1 } )$ takes on two different values since $X _ { 1 }$ is binary. Thus, under condition (4), the class predictions must agree between the two versions for any values of $P ( X _ { 1 } = 1 | U _ { 1 } )$ . Such a perfect agreement is not guaranteed in general when U is tapped by multiple X’s.

We will investigate the agreement level not over model structures but over individual U variables with a variety of their neighborhood situations. Some basic situations of neighborhood are listed in Fig. 3. Since our classifications are based on $P _ { U _ { k } } | \mathbf { x } ( 1 | \mathbf { x } )$ , it is important to look into how X variables are connected to an interested U variable.

If there is a sequence of edges (without regard to their directions) between two nodes which are not neighbors, we will say that the two nodes are connected indirectly. When we do not distinguish the two types of connectedness, we will just say that a pair of nodes is connected.

![](/api/attachments/6N32APC8/fulltext/images/0374d3480d4490f7fefd8ee6bf62f22d4bccbd3e3a50b58f5bb4dceaf2c0695d.jpg)  
Fig. 3. Basic model structures that are considered for the simulation study.

In panels 1– 5, only one U variable is a parent node of X variables, in which case, we will say that the U variable is in a Type-1 neighborhood situation. In panels 6–8, the X variables have only one parent (U) variable and there are at least two U variables, as parents of X variables, that are connected each other, in which case, we will say that the U variable which is a parent of at least one X variable is in a Type-2 neighborhood situation.

In these two neighborhood situations, each X variable has only one parent node. However, in panels 9–15, all the X variables have multiple parents. In panels 9–15 except 13, every X variable has three parent nodes, while every X variable has five parent nodes in panel 13. When U is one of multiple parents of an X variable, we will say that the U is in a Type-3 neighborhood situation. A common feature in panels 9– 13 is that all the U variables are tapped by an equal number of X variables, but it is not the case for panels 14 and 15. In panel 14, $U _ { 1 }$ is connected directly to $X _ { 1 }$ only and connected indirectly to $X _ { 2 }$ and $X _ { 3 }$ through other U variables. The three types of neighborhood situations are summarized in Table 5. If a U variable is in a Type-t neighborhood situation, we will call the U variable a Type-t U variable.

Recall that X and U variables are respectively for the item-scores and the knowledge states. The Type-1 neighborhood situation is not common in educational testing, but Types 2 and 3 are.

However, we pay attention to these three basic situations to explore how the neighborhood situations affect the classification robustness. Almost every neighborhood situation of $U$ can be expressed as a mixture of Types 2 and 3.

Table 5  
The three neighborhood types of a U variable as depicted in Fig. 3

<table><tr><td>Neighborhood situation</td><td>Description</td><td>Corresponding panels in Fig. 3</td></tr><tr><td>Type 1</td><td>There is only one U variable as a parent node of X&#x27;s.</td><td>1, 2, 3, 4, 5</td></tr><tr><td>Type 2</td><td>There are more than one Type-1 U variables and they are connected.</td><td>6, 7, 8</td></tr><tr><td>Type 3</td><td>There is an X variable which has multiple parent (U) variables.</td><td>9 through 15</td></tr></table>

We define the agreement level up to class-difference j in predictions for variable $U _ { k }$ by

$$
\alpha_ {j} (U _ {k}) = \sum_ {| d | \leq j} \overline {{r}} _ {k d}.
$$

In particular, $\alpha _ { 0 } ( U _ { k } )$ is the exact agreement level for $U _ { k } .$ When confusion is not likely, we will simply use $\alpha _ { j }$ instead of $\alpha _ { j } \left( U _ { k } \right)$

The $\mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega }$ and $\alpha _ { 1 }$ values for the 15 panels in Fig. 3 are listed in Table 6. The $\alpha _ { 1 } ( U _ { 1 } )$ values are larger than or equal to 0.97 when $U _ { 1 }$ is a Type-1 or Type-2 variable. It is also the case in the Type-3 situations when the U variable is connected to other U variables. In panels 12 and 15, all the U variables are marginally independent each other, and it is interesting to see that the $\alpha _ { 1 }$ values for $U _ { 1 } , U _ { 2 } ,$ , and $U _ { 3 }$ in panel 12 are all high around 0.95 while those for $U _ { 1 } , . . . , U _ { 5 }$ in panel 15 are 0.86, 0.97, 0.98, 0.96, and 0.85, respectively. In panel 15, $U _ { 1 }$ and $U _ { 5 }$ each are connected directly to only one X variable, and their $\alpha _ { 1 }$ values are around 0.85, while the $\alpha _ { 1 }$ values for the other U variables in panels 12 and 15 are all larger than or equal to 0.95.

It is worthwhile to compare the a values between the set of panels 1, 2, and 3 and the set of panels 9, 10, and 11. The only difference between the two sets is in the number of the U variables. In the latter set of panels, all the three U variables are the parents of every X variable involved. Both $\mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega }$ and $\alpha _ { 1 }$ values are comparable between panels 1 and 9, between panels 2 and 10, and between panels 3 and 11. In panel 13, every U variable is a parent node of the three X variables, $X _ { 1 } , X _ { 2 } ,$ , and $X _ { 3 } ,$ , and the a values are more or less the same as those for panels 3 and 11, where the U variables are connected. In panel 14, the a values of a U variable vary according to the number of its child X variables. From this observation, we can say that the a values of a U variable are affected more by the number of its child X variables than by how the U variable is connected to other U variables as long as the U variables are connected.

Connectedness among the U variables is an important factor for the a values. The U variables are marginally independent among themselves in panel 12, while it is not the case in panel 11. Also, the a values for panel 12 are smaller than those for panel 11.

$\alpha _ { 1 }$ and $\alpha _ { 0 }$ values for the neighborhood situations as listed in Figs. 3 and 4

<table><tr><td rowspan="2">N. type $^{a}$ </td><td rowspan="2">Panel</td><td colspan="2"> $U_1$ </td><td colspan="2"> $U_2$ </td><td colspan="2"> $U_3$ </td><td colspan="2"> $U_4$ </td><td colspan="2"> $U_5$ </td><td colspan="2"> $U_6$ </td></tr><tr><td> $\alpha_1$ </td><td> $\alpha_0$ </td><td> $\alpha_1$ </td><td> $\alpha_0$ </td><td> $\alpha_1$ </td><td> $\alpha_0$ </td><td> $\alpha_1$ </td><td> $\alpha_0$ </td><td> $\alpha_1$ </td><td> $\alpha_0$ </td><td> $\alpha_1$ </td><td> $\alpha_0$ </td></tr><tr><td>1</td><td>1</td><td>1.00</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>2</td><td>1.00</td><td>0.91</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>3</td><td>0.98</td><td>0.84</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>4</td><td>0.97</td><td>0.71</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>5</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>6</td><td>1.00</td><td>0.90</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>7</td><td>1.00</td><td>0.95</td><td>1.00</td><td>0.95</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>8</td><td>0.99</td><td>0.79</td><td>0.99</td><td>0.80</td><td>1.00</td><td>0.81</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>9</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>10</td><td>1.00</td><td>0.89</td><td>1.00</td><td>0.89</td><td>1.00</td><td>0.89</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>11</td><td>0.99</td><td>0.80</td><td>0.99</td><td>0.78</td><td>1.00</td><td>0.80</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>12</td><td>0.95</td><td>0.69</td><td>0.95</td><td>0.69</td><td>0.96</td><td>0.72</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>13</td><td>0.98</td><td>0.83</td><td>0.97</td><td>0.83</td><td>0.98</td><td>0.83</td><td>0.98</td><td>0.84</td><td>0.98</td><td>0.83</td><td></td><td></td></tr><tr><td>3</td><td>14</td><td>1.00</td><td>0.93</td><td>0.97</td><td>0.84</td><td>0.99</td><td>0.83</td><td>0.98</td><td>0.88</td><td>1.00</td><td>0.98</td><td></td><td></td></tr><tr><td>3</td><td>15</td><td>0.86</td><td>0.58</td><td>0.97</td><td>0.68</td><td>0.98</td><td>0.70</td><td>0.96</td><td>0.66</td><td>0.85</td><td>0.56</td><td></td><td></td></tr><tr><td></td><td></td><td colspan="2"> $U_2^{8b}$ </td><td colspan="2"> $U_3^8$ </td><td colspan="2"> $U_1^{11}$ </td><td colspan="2"> $U_2^{11}$ </td><td colspan="2"> $U_3^{11}$ </td><td colspan="2"> $U_1^8$ </td></tr><tr><td>2 and 3</td><td>11a</td><td>0.99</td><td>0.73</td><td>1.00</td><td>0.81</td><td>0.99</td><td>0.74</td><td>0.93</td><td>0.70</td><td>0.98</td><td>0.80</td><td>0.98</td><td>0.73</td></tr><tr><td>2 and 3</td><td>11b</td><td>0.98</td><td>0.71</td><td>0.99</td><td>0.70</td><td>0.99</td><td>0.77</td><td>1.00</td><td>0.79</td><td>0.99</td><td>0.75</td><td>0.99</td><td>0.74</td></tr><tr><td>2 and 3</td><td>16</td><td>0.99</td><td>0.74</td><td>0.93</td><td>0.57</td><td>0.97</td><td>0.69</td><td>0.94</td><td>0.55</td><td>0.95</td><td>0.53</td><td>0.98</td><td>0.73</td></tr><tr><td>2 and 3</td><td>17</td><td>0.96</td><td>0.68</td><td>0.91</td><td>0.58</td><td>0.94</td><td>0.55</td><td>0.85</td><td>0.38</td><td>0.85</td><td>0.39</td><td>0.93</td><td>0.67</td></tr></table>

<sup>a</sup> ‘‘N. type’’ is an abbreviation of ‘‘the type of the neighborhood situation.’’  
<sup>b</sup> Panels 11a and 11b are for comparison with the basic structures in panels 8 and 11. $U _ { i } ^ { j }$ stands for the node U<sub>i</sub> in panel j. The a values in the last four rows of the table are comparable with the a values for the nodes as indicated in the fifth row from the bottom of the table.

The marginal independence implies that the U variables are free to take on any values from their support sets and so the influence of $U _ { 1 }$ upon $X _ { 1 }$ is in general less than the influence when there is no marginal independence among the $U$ variables. If $U _ { 1 } , U _ { 2 } ,$ , and $U _ { 3 }$ are associated among themselves so highly that we may regard them as one variable, $\alpha _ { 1 }$ and $\alpha _ { 0 }$ values may be as large as those for $U _ { 1 }$ in panel 3 or 11. We just saw this phenomenon by comparing the a values between panels 11 and 12, and a similar phenomenon is also seen between panels 14 and 15, where the U variables are all marginally independent in panel 15 and they are connected in panel 14. Note that the difference is more obvious in the $\alpha _ { 0 }$ values. The simulation result strongly indicates that a high association among a set of $U$ variables may yield larger a values for the individual U variables in the set than for the U variables which are less associated among themselves.

Fig. 4 displays four graphs as an extension to Fig. 3. Panel 11a is a combined graph of panels 8 and 11 with only one edge added between $U _ { 1 }$ and $U _ { 3 }$ , and two more edges are added to panel 11a to obtain panel 11b. Thus, it makes sense to compare the a values among panels 8, 11, 11a, and 11b. In the table, the row of $U _ { i } ^ { j } { } ^ { , } \mathrm { \bf { s } }$ which are explained at a footnote to the table is inserted for the convenience of the readership. For instance, in panel 11a, variables $U _ { 1 }$ and $U _ { 3 }$ correspond respectively to $U _ { 2 }$ in panel 8 and $U _ { 1 }$ in panel 11. The $\alpha _ { 1 }$ values are almost the same between the variables of each corresponding pair, while $\mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega }$ values are slightly smaller for panel 11a. Panel 11b was considered to see how additional edges affect the a values, and no special trend is found between panels 11a and 11b. The a values are more or less the same between the two panels.

Panels 16 and 17 are obtained by further adding edges to the graph in panel 11a. Note that variables $X _ { 1 } , . . . . X _ { 3 }$ each has four and five parent nodes respectively in panels 16 and 17. We can see a trend in the a values that they decrease as we move across panels in the order of 11a, 16, and 17. The $\mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega }$ values decreased by considerable amounts while the $\alpha _ { 1 }$ values did not change much. Fortunately, for most of the cases in Table 6, the $\alpha _ { 1 }$ values were close to 1 and none of the values were smaller than 0.85. In other words, the classification were very robust up to class level 1.

![](/api/attachments/6N32APC8/fulltext/images/21c75397004835db80c02fd6a53c863491b95921f671a0784652a34a7cd47362.jpg)  
Fig. 4. Some more model structures as an extension to the model structures in Fig. 3. The thick arrows in panel 11b are the only addition to the graph in panel 11a.

In a nutshell, the simulation result strongly shows a general trend that, as is implicitly manifested in the panels 1– 5 and in the pair of panels 13 and 14, as a U variable becomes a parent of more X variables, its a values gets smaller. Another important phenomenon is that, as is observed among others in the pair of panels 11 and 12 and the pair of panels 14 and 15, as the U variables become more associated each other, the a values tend to increase. These two phenomena are apparent in every model structure that we have considered in this section.

## 4. Concluding remarks

When we are in a situation of classifying for some variable, it is desirable that we look into the model structure regarding conditional independence and conditional stochastic ordering. Theorem 2 says that when classifications are to be made on U variables and the conditional independence and the conditional stochastic ordering hold for X variables given U, the classifications are robust to some extent.

We have considered some ‘‘basic’’ structures for investigating the classification robustness. The size of the set of all the possible model structures increases exponentially with the number of variables involved in the model. So it is almost impossible to consider all of them to find the range of classification robustness, nor is it easy to find a measure of the robustness for a particular model structure. Such a task, however, seems not necessary at all since it is indicated in the simulation result that the robustness (for example, the $\alpha _ { 1 }$ values) in classification for a U variable is affected by the number of its child X variables and by the connectedness or the association among the U variables.

In the experiment, we considered the model structures where a U variable is a parent node of up to six X variables. It is possible that the $\alpha _ { 1 }$ value falls below 0.85 for a U variable. If such is the case, we may exclude the U variable from our robust classification scheme, or we may classify for the variable with the corresponding $\alpha _ { 1 }$ value. We are now at a position to recommend a robust classification approach as follows:

Suppose that for a Bayesian network of binary variables, we are to predict for every $U$ variable in the model in terms of class-level. Provided that there is no variable in the model that has more than six parent variables, we apply the method as in the simulation experiment in the previous section to obtain the $\alpha _ { 1 }$ values for all the $U$ variables in the model. We then make classifications for the subjects in the real data using the version 1 of the Bayesian network. The $\alpha _ { 1 } ( U _ { k } )$ value can be used as a robustness index for $U _ { k }$

There is no easy way of finding such a table as Table 3 when a given model is complicated involving a large number of variables which may often be the case in the real world. Actually Table 3 was found after a sequence of trial and error experiments and it worked well for a variety of model structures.

Although we have considered Bayesian networks only, the classification robustness would be valid for other forms of graphical models such as Markov networks [15] and mixture of the two types. One of the reasons is that these two forms of graphs share the Markov properties that are essentially transformable with a few exceptions into the same graphical layout [2,3].

The result of this paper is relevant to all the problems where classifications may be made based on the relative magnitudes of the conditional probabilities under the assumption that the variables are binary and are positively associated with each other. The robustness of classification will save much of our time and effort provided that the positive association condition (Eq. (4)) is satisfied and so enhancing the utility of model-based DSSs.

## References

[1] S.K. Andersen, F.V. Jensen, K.G. Olesen, F. Jensen, HUGIN: A Shell for Building Bayesian Belief Universes for Expert Systems [Computer Program], HUGIN Expert, Aalborg, Denmark, 1989.

[2] S.A. Andersson, D. Madigan, M.D. Perlman, On the Markov equivalence of chain graphs, undirected graphs, and acyclic digraphs, Scandinavian Journal of Statistics 24 (1997) 81– 102.

[3] S.A. Andersson, D. Madigan, M.D. Perlman, A characterization of Markov equivalence classes for acyclic digraphs, The Annals of Statistics 25 (2) (1997) 505– 541.

[4] M.H. DeGroot, Optimal Statistical Decisions, McGraw-Hill, New York, 1970.

[5] ERGO [computer program] Noetic Systems, Baltimore, MD (1991).

[6] P.W. Holland, P.R. Rosenbaum, Conditional association and unidimensionality in monotone latent variable models, The Annals of Statistics 14 (4) (1986) 1523–1543.

[7] F.V. Jensen, An Introduction to Bayesian Networks, Springer, NewYork, 1996.

[8] B.W. Junker, J.L. Ellis, A characterization of monotone unidimensional latent variable models, The Annals of Statistics 25 (3) (1997) 1327– 1343.

[9] S.-H. Kim, Ability diagnosis in junior high school first year Mathematics and a survey result, Proceedings of the First International Commission on Mathematical Instruction— East Asia Regional Conference on Mathematics Education. (98 ICMI-EARCOME 1, Aug. 17 21, 1998), vol. 2, Korea Society of Mathematical Education, Seoul, South Korea, 1998, pp. 637– 645.

[10] H.E. Kyburg Jr., H.E. Smokler (Eds.), Studies in Subjective Probability, Robert E. Krieger Publishing Company, Huntington, New York, 1980.

[11] O.I. Larichev, A.V. Kortnev, D.Y. Kochin, Decision support systems for classification of a finite set of multicriteria alternatives, Decision Support Systems 33 (2002) 13 – 21.

[12] S.L. Lauritzen, D.J. Spiegelhalter, Local computations with probabilities on graphical structures and their application to expert systems, Journal of the Royal Statistical Society, B 50 (2) (1988) 157 – 224.

[13] R.J. Mislevy, Evidence and inference in educational assessment, Psychometrika 59 (4) (1994) 439– 483.

[14] J.C. Partyka, R.W. Hall, On the road to service, ORMS Today 27 (4) (2000) 26 – 30.

[15] J. Pearl, Probabilistic Reasoning In Intelligent Systems: Networks of Plausible Inference, Morgan Kaufmann, San Mateo, CA, 1988.

[16] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Carlsson, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2002) 111 – 126.

[17] P.C. Verhoef, B. Conkers, Predicting customer potential value an application in the insurance industry, Decision Support Systems 32 (2001) 189 – 199.

[18] S. Walczak, W.E. Pofahl, R.J. Scorpio, A decision support tool for allocating hospital bed resources and determining required acuity of care, Decision Support Systems 34 (4) (2003) 445– 456.

[19] J. Whittaker, Graphical Models in Applied Multivariate Statistics, Wiley, New York, 1990.

![](/api/attachments/6N32APC8/fulltext/images/9004dc587ba3c6fb81835d4b328bfceb98368a2c68a8dbb7f12e6c13491d4302.jpg)

Sung-Ho Kim is an Associate Professor of Statistics in the Division of Applied Mathematics at the Korea Advanced Institute of Science and Technology (KAIST). He received his BA degree from Seoul National University and MA and PhD degrees in Statistics from Carnegie Mellon University. He held a position as a research scientist at Educational Testing Service, Princeton from 1989 to 1993, where he got interested in statisti-

cal modelling for problem solving. Dr. Kim has taught Statistics at KAIST since he joined the university in 1993 and has published about 30 articles. The journals where his articles have appeared include Journal of the American Statistical Association, Computational Statistics and Data Analysis, and Journal of Statistical Planning and Inference. He has worked as a consultant for government and private institutes on statistical technologies for educational testing in South Korea. He is on the editorial board of Intelligent Data Analysis. His present research interests include large modelling for educational testing data, model combining, and statistical methods for on-line diagnosis.
