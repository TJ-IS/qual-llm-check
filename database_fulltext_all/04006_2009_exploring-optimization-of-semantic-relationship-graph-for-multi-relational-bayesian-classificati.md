---
otero_id: 4006
otero_key: "Q8HWFPE3"
title: "Exploring optimization of semantic relationship graph for multi-relational Bayesian classification"
authors: "Hailiang Chen; Hongyan Liu; Jiawei Han; Xiaoxin Yin; Jun He"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploring optimization of semantic relationship graph for multi-relational Bayesian classi<sup>fi</sup>cation

Hailiang Chen <sup>a,</sup>⁎, Hongyan Liu <sup>b</sup>, Jiawei Han <sup>c</sup>, Xiaoxin Yin <sup>c</sup>, Jun He <sup>d</sup>

<sup>a</sup> Krannert School of Management, Purdue University, West Lafayette, IN, USA

<sup>b</sup> School of Economics and Management, Tsinghua University, Beijing, China

<sup>c</sup> Department of Computer Science, University of Illinois at Urbana-Champaign, Urbana, IL, USA

<sup>d</sup> School of Information, Renmin University of China, Beijing, China

## a r t i c l e i n f o

Article history: Received 17 March 2008 Received in revised form 7 April 2009 Accepted 7 July 2009 Available online 16 July 2009

Keywords: Multi-relational classi<sup>fi</sup>cation Naïve Bayesian classi<sup>fi</sup>cation Semantic relationship graph Feature selection Depth-<sup>fi</sup>rst Width-first

## a b s t r a c t

In recent years, there has been growing interest in multi-relational classi<sup>fi</sup>cation research and application, which addresses the dif<sup>fi</sup>culties in dealing with large relation search space, complex relationships between relations, and a daunting number of attributes involved. Bayesian Classi<sup>fi</sup>er is a simple but effective probabilistic classi<sup>fi</sup>er which has been shown to be able to achieve good results in most real world applications. Existing works for multi-relational Naïve Bayes classi<sup>fi</sup>er mainly focus on how to extend traditional <sup>fl</sup>at Naïve Bayes classi<sup>fi</sup>cation method to multi-relational environment. In this paper, we look into issues concerned with how to increase the accuracy of multi-relational Bayesian classi<sup>fi</sup>er but still retain its ef<sup>fi</sup>ciency. We develop a Semantic Relationship Graph (SRG) to describe the relationship between multiple tables and guide the search within relation space. Afterwards, we optimize the Semantic Relationship Graph by avoiding undesirable joins between relations and eliminating unnecessary attributes and relations. The experimental study on the realworld and synthetic databases shows that the proposed optimizing strategies make the multi-relational Naïve Bayesian classi<sup>fi</sup>er achieve improved accuracy by sacri<sup>fi</sup>cing a small amount of running time.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

Multi-relational data mining deals with knowledge discovery from relational databases consisting of multiple tables. Instead of squeezing data from multiple relations into a single table, multi-relational data mining seeks to collect and analyze data directly from a multi-relation database. Conventionally, many classi<sup>fi</sup>cation approaches can only be applied to a single relation. When performing these approaches on multi-relational data, it often requires transferring data into a single table by <sup>fl</sup>attening and feature construction, which is known as propositionalization. However, many of these methods are heuristic, so information is lost and the representation change is incomplete [10]. Other direct approaches in multi-relational classi<sup>fi</sup>cation mainly fall in the categories of Inductive Logic Programming (ILP) [13,16] and probabilistic relational learning [8,9]. Unfortunately, due to the irregular structures and complex links of relational data, it is timeconsuming to explore the hypothesis space in relational databases for useful attributes or relational structural neighbors, which makes these algorithms quite expensive in terms of runtime.

Naïve Bayesian [4,5] is a well-known classi<sup>fi</sup>er for its simplicity and robustness. In the literature, there are already some works [2,6,11,18,19] that extend Naïve Bayes classi<sup>fi</sup>cation to deal with multi-relational data directly. We have the following observations about them. First, most of such works use the ILP-based method. They are usually two-step based methods. In the <sup>fi</sup>rst step, a set of <sup>fi</sup>rst-order features or rules are extracted, and then in the second step, these features or rules are combined to compute probabilities according to Naïve Bayesian formula. Although these methods can deal with multi-relational data, most of them involve transforming tuples in tables into Prolog facts, which are structured objects consisting of a function name and a series of arguments that represent the properties of the objects. This type of pre-processing loses information and is also unnecessary. Second, some methods can deal with data in tables directly, but they limit the search space by only allowing one type of join paths. For example, while linking tables to target table, only tables along primary-key to foreignkey path are considered [2]. Tables in a foreign-key to primary-key path or foreign-key and primary-key mixed path are neglected. This constraint limits their application to real world situation. Third, most of these methods consider all tables linked to the target table equally important. Thus, the number of attributes linked to the target attribute could be very large, but many of them may be irrelevant to the classi<sup>fi</sup>cation task and could not improve the classi<sup>fi</sup>cation accuracy (Attribute relevance is de<sup>fi</sup>ned as the classifying power of the attribute within a set of data). In real-life applications, a domain expert can manually identify all the relevant attributes of the target attribute. Nevertheless, in many situations, such an expert is not available, and we have to make use of automated methods to <sup>fi</sup>lter out irrelevant attributes according to a given criterion. Therefore, how to deal with data in multiple tables directly, how to describe the relationship between tables, how to treat tables differently, and how to get rid of irrelevant data are major challenges to make a good multi-relational classi<sup>fi</sup>er, especially for a Naïve Bayesian classi<sup>fi</sup>er.

In response to these drawbacks, we propose a new algorithm called SRG-BC, to integrate relation selection and feature selection into the multi-relational Bayesian classi<sup>fi</sup>er. It builds a Semantic Relationship Graph (SRG), which describes the relationship between tables in the database and enables the learner to treat the relations linked to the target one differently. To reduce the adverse effect of weakly linked tables, SRG-BC adopts a pruning strategy to optimize the Semantic Relationship Graph so that it can prevent introducing irrelevant relations and keep its compact representation and structure. Furthermore, to ensure high accuracy of the learning system, we examine the correlation between candidate variables in selected relations and the target attribute, perform an iterative ranking of features, and thus determine discriminatory features in relevant relations. This makes the classi<sup>fi</sup>er freely choose a subset of all features in selected relations and exclude those that introduce bias.

The rest of this paper is organized as follows. In Section 2, we introduce the related work in the multi-relational classi<sup>fi</sup>cation area. Section 3 brie<sup>fl</sup>y reviews the concepts of multi-relational Bayesian classi<sup>fi</sup>er and presents the de<sup>fi</sup>nition of Semantic Relationship Graph. In Section 4, we give a detailed summary of the optimizing strategies we use to improve accuracy, including methods related to relation selection and feature selection. Section 5 describes our proposed algorithm and Section 6 presents our experimental study on both realworld and synthetic databases. Finally, in Section 7 we draw conclusions.

## 2. Related work

There are already some research works on statistically based algorithms under the context of multi-relational classi<sup>fi</sup>cation. Some earlier approaches like ILP-R [19], 1BC [6], 1BC2 [11] try to extend Naïve Bayes classi<sup>fi</sup>cation to deal with multi-relational data directly. These three approaches are <sup>fi</sup>rst-order Bayesian classi<sup>fi</sup>ers working on a set of main-memory Prolog facts, which correspond to items in relational databases. ILP-R uses hypotheses to classify new instances based on naïve Bayesian reasoning. 1BC applies dynamic propositionalization to generate <sup>fi</sup>rst-order features exhaustively within a given feature bias. 1BC2 learns from structured data by <sup>fi</sup>tting various parametric distributions over sets and lists to the data. 1BC2 has a constraint on the number of literals per clause and larger values cause the system to crash. To address the disadvantages of using Prolog facts as input, Mr-SBC [2] is proposed to adopt an integrated approach in the computation of posterior probabilities that also makes use of <sup>fi</sup>rst order classi<sup>fi</sup>cation rules. Though successful in extending the naïve Bayes classi<sup>fi</sup>cation method to the multi-relational setting, Mr-SBC only considers the relations along the primary-key to foreign-key path and ignores other kinds of join paths such as foreign-key to primarykey path, while searching for <sup>fi</sup>rst-order rules.

There are also some recent probabilistic relational learners that search the relational space for useful attributes and relational structure of neighbors, e.g., Probabilistic Relational Models (PRMs) [8,9], Relational Probability Trees (RPTs) [17] and Relational Bayesian Classifiers (RBCs) [18]. However, these probabilistic relational learners examine the relational data at the instance level. The training and testing sets are groups of subgraphs, and each subgraph is assumed to contain one target instance to be classi<sup>fi</sup>ed. The target attribute of an instance might depend on the characteristics of instances it is related to either directly or through the chains of instances in the subgraph. This paper is different from these models as we focus on the multirelational Bayes classi<sup>fi</sup>er and aim to optimize its trade-off between accuracy and speed.

ILP approaches have also been widely applied to multi-relational classi<sup>fi</sup>cation tasks. Representative approaches include FOIL (a topdown <sup>fi</sup>rst-order inductive learner) [20] and TILDE (a decision tree based algorithm) [1]. FOIL is one of the <sup>fi</sup>rst and best known ILP systems in the public domain. TILDE induces logical decision trees from examples. CrossMine [23] is a recently proposed method to handle both accuracy and scalability problems for multi-relational classi<sup>fi</sup>cation. These algorithms are comparable to our approach in the sense that they also employ optimizing strategies and choose the best predicates in <sup>fi</sup>nding rules during the mining process. We use them as comparative baselines later in the experimental study to show the effectiveness of our optimization methods.

In this work, we also introduce feature selection that works together with relation selection. It has been shown that feature selection can improve the performance of learners in various areas such as text learning and authentication [3,15]. To apply feature selection to the classi<sup>fi</sup>cation tasks, we notice that even among the features that belong to the same relation, some are relevant and useful, while others may be redundant or irrelevant. If two or more features are highly correlated, they receive too much weight in the classi<sup>fi</sup>cation decision and this can result in a reduced accuracy [21]. Much work has been done concerning feature selection in a single table and shows that feature selection as a preprocessing step is effective in removing irrelevant data and increasing learning accuracy [12,14,21,22]. Closely related methods include greedy approaches for searching the attributes space, such as the sequential Bayesian classi<sup>fi</sup>er proposed in [14] and the selective Bayesian classi<sup>fi</sup>er in [12]. When it comes to the case of multi-relational data mining, available features come from multiple relations and may need to be joined together before they can be used. We confront this by adopting a greedy, iterative ranking method based on the actual performance of Bayesian classi<sup>fi</sup>er that constructs an optimal feature set.

## 3. Multi-relational Bayesian classi<sup>fi</sup>er based on semantic relationship graph

In a multi-relational classi<sup>fi</sup>cation task, there is one target relation containing the target attribute that has several class labels. Other relations in the database are directly or indirectly linked with the target relation. The goal is to predict the speci<sup>fi</sup>c class labels of unseen examples by making use of available data in the database. There are multiple ways to approach classi<sup>fi</sup>cation in a multi-relational context. Bayesian classi<sup>fi</sup>er is one of the most straightforward and widely used methods. For a tuple x with n attributes in the target tablet, assume there are l tuples in the joined table s that can be joined with x. These l tuples are $( y _ { k 1 } , y _ { k 2 } , . . . , y _ { k l } )$ and each is represented by m values $y _ { k i } =$ $( y _ { k i 1 } , y _ { k i 2 } , . . . , y _ { k i m } )$ . Under the assumption that each attribute (either in the target relation or other joined relations) is independent of others given the class, we have formula (1):

$$
\begin{array}{l} C _ {M A P} = \arg \max _ {c _ {i} \in C} P (c _ {i} | X) \\ = \arg \max _ {c _ {i} \in C} P (X | c _ {i}) P (c _ {i}) \\ = \arg \max _ {c _ {i} \in C} P (x _ {1},..., x _ {n}, y _ {k 1 1},... y _ {k 1 m},... y _ {k l 1},... y _ {k l m} | c _ {i}) P (c _ {i}) \\ = \arg \max _ {c _ {i} \in C} \prod_ {j = 1} ^ {n} P (x _ {j} | c _ {i}) \prod_ {q = k 1 t = 1} ^ {k l} \prod_ {} ^ {m} P (y _ {q t} | c _ {i}) P (c _ {i}) \end{array}\tag{1}
$$

In order to make the above expression operational, we should <sup>fi</sup>nd a feasible way to specify the probability distribution for each attribute and compute the associated conditional probabilities. In our algorithm, we adopt the tuple ID propagation method [23] to virtually join relations along each path and collect the required information for computation. To guide the search within the relation space, a Semantic Relationship Graph is also constructed to represent and summarize the relationships between various relations in the database.

Semantic Relationship Graph is a directed acyclic graph SRG (V, E, W), where V is a set of vertices, each of which corresponding to a table in the database. E is a set of directed edges, and an edge (v, w) means table w can be linked to table v by directly joining these two tables. W is a set of attributes, each of which links two tables. We call this kind of attribute link attribute.

Each edge of the Semantic Relationship Graph also shows a relationship between two tables. Two most common relationships between table v and table w are as follows:

(1) Primary-key to foreign-key relationship, indicating that table w contains foreign-key referring to primary-key in table v.

(2) Foreign-key to primary-key relationship, indicating that table v contains foreign-key referring to primary-key in table w.

In our algorithm we do not limit the relationships to the above two. As long as the join condition between two tables can be de<sup>fi</sup>ned, we can virtually join them by tuple ID propagation. The reason we de<sup>fi</sup>ne a directed graph instead of undirected graph is that we need to start from the target table and link other tables with the target table step by step. Suppose table t is the target table, and there is an edge pointing to v from t and an edge pointing to w from v. After joining table v with t, and join w with v, usually we do not need to join w and v by same link attribute in the same path again. For example, suppose table student contains information of each student, and another table professor contains information of each professor. Between these two tables, there is a semantic relationship by meaning of supervision, and assume there is no other relations between them in the context of the application. In this case, we can join table professor with table student. If they are only involved in one path, then this kind of join only needs to be done once. If they are involved in more than one path but with the same semantic relationship, then this join could be done many times. With directed graph, we can prevent unnecessary iteration for one speci<sup>fi</sup>c relationship in one path.

When there are more than one relationship between two tables or there is a relationship between tuples of one table (i.e., there is a selfjoin on that table), there might be a cycle in the relationship graph. In this case, to prevent the iteration to go on too deep, we can limit the number of iterations, and transform the cyclic graph into acyclic graph. We argue that this kind of links become weaker as more iterations are done. Taking table student and professor as example, suppose there is another relationship between them by meaning of friend, which means that a student is linked to a professor if the student is a friend of the professor. Now there is a cycle between these two tables. If two is the maximum number of iterations, then we can make two additional tables named student1 and professor1 to duplicate these two tables, and link them by directed edge.

We can also relax the constraints of Semantic Relationship Graph by allowing the existence of cycle. If so, in order to avoid the iteration doing too many times, we can also set a parameter to control the iteration times. In the following sections, we only regard SRG as an acyclic graph.

Semantic Relationship Graph is kind of similar to ER diagram, which usually can be automatically generated from those common commercial database systems. It facilitates the process of virtually joining the relations and acts just like road maps for the entire algorithm. One example of SRG for a <sup>fi</sup>nancial database from PKDD CUP99 is given in Fig. 1.

![](/api/attachments/Q8HWFPE3/fulltext/images/e63e4b81dddbeb17e50532d89bd252af433b619931fbec41a3b818d2da7757ed.jpg)  
Fig. 1. Semantic relationship graph for the <sup>fi</sup>nancial database from PKDD CUP99.

## 4. Optimization based on SRG

After introducing the concept of Semantic Relationship Graph, we now consider how to construct an accurate classi<sup>fi</sup>er based on SRG. It will be fairly easy to take all relations into account and make predictions using all variables. However, this not only is timeconsuming, but also generates biased results (we will show the performance of the original multi-relational Bayesian classi<sup>fi</sup>er for comparison in the experimental study section). In most cases, we know for sure that only part of all relations contribute to the improvement of classi<sup>fi</sup>cation accuracy. Therefore, we need to determine which part of the Semantic Relationship Graph needs to be considered in order to achieve better classi<sup>fi</sup>cation accuracy.

## 4.1. Relation selection

The pruning strategy we develop to approach this problem is called Relation Selection. We can search the relation space along the Semantic Relationship Graph in either a depth-<sup>fi</sup>rst or a width-<sup>fi</sup>rst manner. Each time we traverse a relation, we classify the training dataset using the probability information we already have and get an accuracy result. After traversing the whole graph, we cut off the SRG at the point of maximum classifying accuracy. Below is the interim algorithm Graph-NB based on depth-<sup>fi</sup>rst relation selection.

```txt
Algorithm: Graph-NB (depth-first approach)

Input: relations in the database, and the Semantic Relationship Graph G
Output: An optimized Semantic Relationship Graph OG, and a set P of attribute value probabilities corresponding to each class label.

Method:
1. maxAccuracy = CollectAndClassify(tt)
2. Initialize edgeNo = 0, maxEdgeNo = 0;
3. for each out edge of target table tt do
    edgeNo++;
    NextEdge(tt)
    endfor

4. Cut off all of edges with number ≥ maxEdgeNo, and output remaining part of G as OG.
Subroutine NextEdge(parentTable pt)

Method:
1. let t = table pointed to by edge with number edgeNo;
2. propagate(pt, t);
3. accuracy = CollectAndClassify(t);
4. if (accuracy > maxAccuracy) then
    maxAccuracy = accuracy;
    maxEdgeNo = edgeNo;
    endif

5. for each out edge of current table t do
    edgeNo++;
    NextEdge(t);
    endfor
```

First of all, in algorithm Graph-NB, function collectandClassify is called to scan target table tt, collect attribute value count information for each class label, and use this information to classify each tuple of target table tt. The overall classi<sup>fi</sup>cation accuracy is returned to variable maxAccuracy. Then in step 2, global variable edgeNo and maxEdgeNo are initialized, where edgeNo is a number used to record the processing order of all of the edges in graph G, and maxEdgeNo is one of these numbers with the maximum classi<sup>fi</sup>cation accuracy. After that, table pointed to by each out edge of the target table tt is processed by calling the main subroutine NextEdge. Finally, with best accuracy among all the edges in the graph, we can cut off all of edges with number greater than maxEdgeNo, and the remaining part of the graph will be used to classify test or unseen objects. In the mean time, probability of attribute value in every table pointed to by each edge included in the SRG will also be returned.

In subroutine NextEdge, for the table t pointed to by current edge with number edgeNo, function propagate is called to propagate tuple

ID from parent table pt to table t. Then Function collectandClassify is used to collect probability information and classify each tuple of the target table. If the current accuracy is better than the existing best one, value of maxAccuracy and maxEdgeNo are changed to re<sup>fl</sup>ect this. After that, in step 5, each out edge of current table t is dealt with by recursive call of NextEdge.

We can also develop the width-<sup>fi</sup>rst approach for Graph-NB. Everything is the same except that we adopt a queue data structure to facilitate the width-<sup>fi</sup>rst search. Starting from the target relation, we add all join edges of the current relation to the rear of queue, collect information about current relation's attributes, then pick out the front edge of the queue as the next join route, and use the tuple ID propagation method [23] to load data of the join edge's right relation. This process continues until the queue is empty. The detailed approach is summarized below.

```txt
Algorithm: Graph-NB (width-first approach)
Input: relations in the database, Semantic Relationship Graph SRG
Output: An optimized Semantic Relationship Graph OG, and a set P of attribute value probabilities corresponding to each class label.
Declaration:
    <left, right> — one edge of SRG (<target relation, target relation> is the first edge of SRG)
    Q — Queue storing traversing edges in SRG
    addQ(<left, right>) — add edge to the rear of Q
    delQ() — return the front edge of Q and remove it
    propagate (<left, right>) — join relation right and load its data using tuple ID propagation method
Method:
    addQ(<target relation, target relation> ), maxAccuracy = 0
    while Q is not empty do
    propagate( delQ() ), edgeNo + + ;
    add propagating routes (or join edges)
    for each edge out of current relation do
    addQ(<current relation, right r>) 
    endfor
    accuracy = CollectAndClassify(current relation)
    if (accuracy > maxAccuracy) then
    maxAccuracy = accuracy;
    maxEdgeNo = edgeNo;
    endif
endwhile
```

## 4.2. Feature selection

Though relation selection has shown good accuracy and ef<sup>fi</sup>ciency, it is still subject to two restrictions. First, the performance of this approach is likely to depend on the inherent relationship between tables in different paths and the target one, as irrelevant and redundant relations introduced before may have a permanent harmful effect on subsequent operations. Another potential problem is that selection of only relations is often inadequate to ensure high predictive accuracy of the learning system. As mentioned before, among the features that belong to the same relation, some are relevant and useful, while others may be redundant or irrelevant. These undesirable features can dramatically change the performance of the current relation and produce a biased prediction. Thus, to mitigate this unpleasant effect, we propose feature selection methods to further optimize the SRG.

## 4.2.1. Chi-square test

Obviously, not all features (or attributes) are equally useful. Our goal is to select a subset of discriminatory features that are relevant to the target attribute and likely to contribute to making predictions. There are several relevance measures that are widely used in the <sup>fi</sup>eld of data mining, such as information gain, consistency, gain ratio, chisquare statistic, etc. In this work, we implement a chi-square test on each feature candidate to <sup>fi</sup>lter out irrelevant ones. The null hypothesis is that there is no relationship between the feature candidate and the target attribute. Or put in another way, this feature candidate is not discriminatory and should be excluded. The next step is to calculate the chi-square statistic. To illustrate the process, we construct a contingency table shown in Table 1. The rows represent the distribution information of each class label for the target attribute. The columns represent the distribution of all possible values for the tested feature.

Then the chi-square statistic is computed by

$$
\begin{array}{c} \chi^ {2} = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} \frac {(\text { Observed } - \text { Expected }) ^ {2}}{\text { Expected }} \\ = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} \frac {\left(\text { Observed } - \frac {C _ {i} \times V _ {j}}{N}\right) ^ {2}}{\frac {C _ {i} \times V _ {j}}{N}} \end{array}\tag{2}
$$

where N denotes the total number of all occurrences, C the number of occurrences in the ith class, $V _ { j }$ the number of occurrences for the jth value of the tested feature (Note that numeric attributes should be discretized <sup>fi</sup>rst).

The degree of freedom is given by

$$
d f = (m - 1) (n - 1).\tag{3}
$$

We should also assign a signi<sup>fi</sup>cance level to determine our threshold of tolerance for error. Observe that, this might have an in<sup>fl</sup>uence on the performance of the resulting classi<sup>fi</sup>er, since too many discriminatory features selected based on this test (larger signi<sup>fi</sup>cance level) will make the learner unnecessarily slow because of lengthy ranking procedures in the succeeding learning (we will explain this later), but too few features (smaller signi<sup>fi</sup>cance level) may degrade the learner's accuracy as valuable ones are also <sup>fi</sup>ltered out.

Finally, we compare the computed chi-square statistic with the value we would expect if the null hypothesis were true. If the chisquare statistic is larger, we reject the null hypothesis and believe that there is statistically signi<sup>fi</sup>cant relationship between the candidate feature and the target attribute. If opposite, the tested feature is discarded and will no longer be considered.

## 4.2.2. Further feature selection

If we use all the discriminatory features found from the above process as seeds, sort them according to their ratios of chi-square statistic to critical value $( \alpha , d f )$ , select top 10 features with highest ratios to train the classi<sup>fi</sup>er, we would discover that only slight improvement in accuracy is achieved on a case-by-case basis. This is because that chi-square test can not exclude correlated features which introduce dependencies and thus violate the independence assumption. To confront with this problem, we adopt a wrapper feature selection method to build an optimal set of features based on their actual performance on the training data. This method is similar to the sequential Bayesian classi<sup>fi</sup>er proposed in [14] and the selective Bayesian classi<sup>fi</sup>er in [12]. The selective Bayesian classi<sup>fi</sup>er will halt when addition of any feature results in reduced accuracy, but our method carries out a complete iteration procedure, ruling out the possibility that one feature is useless so far but can improve performance when taken with others. The general procedure, called IFS (Iterative Feature Selection) is as follows:

A chi-square contingency table.

<table><tr><td></td><td>Value1</td><td>Value2</td><td>-</td><td>Value n</td><td>Total</td></tr><tr><td>Class1</td><td> $D_{11}$ </td><td> $D_{12}$ </td><td>-</td><td> $D_{1n}$ </td><td> $C_1$ </td></tr><tr><td>Class2</td><td> $D_{21}$ </td><td> $D_{22}$ </td><td>-</td><td> $D_{2n}$ </td><td> $C_2$ </td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Class m</td><td> $D_{m1}$ </td><td> $D_{m2}$ </td><td>-</td><td> $D_{mn}$ </td><td> $C_m$ </td></tr><tr><td>Total</td><td> $V_1$ </td><td> $V_2$ </td><td>-</td><td> $V_n$ </td><td>N</td></tr></table>

```txt
Procedure: IFS
Input: Set of discriminatory features, D
Output: Set of features, R
Declaration:
maxAccuracyIter — maximum accuracy in each iteration
maxPositionIter — position of the feature where maxAccuracyIter is achieved in each iteration
maxAccuracyTrain — maximum accuracy on training data
maxPositionTrain — position of the feature where maxAccuracyTrain is achieved on training data
accuracy - accuracy of each classifying operation
Method:
Let R = {}, maxAccuracyTrain = 0
while D is not empty do
    maxAccuracyIter = 0
    for each feature f in D do
classify training data using R + {f}
record accuracy
if accuracy > maxAccuracyIter then
    maxAccuracyIter = accuracy
    record maxPositionIter
endif
endfor
R = R + { feature at maxPositionIter }
D = D - { feature at maxPositionIter }
if maxAccuracyIter > maxAccuracyTrain then
    maxAccuracyTrain = maxAccuracyIter
    record maxPositionTrain
endif
endwhile
Remove the features in R with position larger than maxPositionTrain, use the left as discriminatory features
```

To summarize, the algorithm initializes the output set to the empty set, and carries out an iterative classifying and ranking method based on the SRG. In each iteration, the algorithm considers adding each feature in the current set of discriminatory features to the output set on a trial basis and <sup>fi</sup>nds out the feature that most improves the accuracy. Then this feature is permanently added to the output set and removed from the set of discriminatory features. After this iterative ranking of discriminatory features, the algorithm chooses the subset of features that achieves the highest accuracy on the training data, and discards others. The output set of features will be used to classify unseen tuples.

## 5. The SRG-BC algorithm

In this section we present the SRG based multi-relational Bayesian Classi<sup>fi</sup>cation algorithm named SRG-BC, which is outlined in Fig. 2. As shown in this <sup>fi</sup>gure, we use the queue data structure to adopt a width-<sup>fi</sup>rst approach to traverse the SRG. Starting from the target relation, add all join edges of the current relation to the rear of queue, carry out the chi-square tests on current relation's attributes and select discriminatory ones, then pick out the front edge of the queue as the next join route, use the tuple ID propagation method [23] to load data of the join edge's right relation. This process continues until the queue is empty. Afterwards, the algorithm conducts an iterative selection of the set of discriminatory features and constructs an optimal feature set. In addition, the algorithm will delete nonintermediary relations in the SRG that do not include any feature in the optimal set, and produce a much smaller and more compact SRG. This will further optimize the Semantic Relationship Graph and reduce the runtime cost of building the Naïve Bayesian Classi<sup>fi</sup>er.

To illustrate the effects of the relation and feature selection method adopted in our algorithm, we will take the <sup>fi</sup>nancial database from PKDD CUP99 as an example. This database initially has 8 relations which contain 35 feature candidates in total. Our optimization strategy <sup>fi</sup>nally selects only 4 relations with 6 features to build the Naïve Bayesian classi<sup>fi</sup>er. Irrelevant relations are removed from the SRG, and other features are discarded. Fig. 3 shows the optimized SRG for this <sup>fi</sup>nancial database. Note that the relation “Account” here does not contain any feature in the optimal set, but it is an intermediary relation used in virtual joining, so it is preserved in the SRG.

## 6. Experimental study

We <sup>fi</sup>rst design a set of experiments to explore the performance of Graph-NB and SRG-BC on both real-world and synthetic datasets, comparing with that of other well-known multi-relational classi<sup>fi</sup>ers such as CrossMine [23], FOIL [20], TILDE [1], 1BC [6], 1BC2 [11], and Mr-SBC [2]. All experiments were carried out on an IBM R40 laptop with Pentium 4 2.2 GHz CPU and 512 MB RAM, running Windows 2000 Professional. Regarding the implementation of these algorithms, the signi<sup>fi</sup>cance level (α) of chi-square tests in our algorithm was set to 0.005, if not speci<sup>fi</sup>ed. For CrossMine, we use CrossMine with sampling and the parameters are the same as in [23], that is, MIN FOIL GAIN=2.5. MAX RULE LENGTH=6. NEG POS RATIO=1. MAX NUM NEGATIVE =600.

In order to evaluate the sensitivity of different values for signi-<sup>fi</sup>cance level α, we also conduct extensive experiments using a series of parameter inputs to measure the quality of predictions.

## 6.1. Real-world databases

We use two sets of real-world datasets to analyze the accuracy and ef<sup>fi</sup>ciency of different classi<sup>fi</sup>ers.

The <sup>fi</sup>rst set of datasets is the Mutagenesis database that is widely used in the area of ILP. Some experimental results for other methods on this database are already available in the literature. The database contains 4 relations and 15,218 tuples. The target relation consists of 188 tuples with 124 being positive and 64 negative. We use three levels of background knowledge that appear in Table 2 for our experiments.

The dataset is analyzed by means of ten-fold cross-validation. The averaged results under three levels of background are shown in Tables 3, 4, and 5, respectively. Those in bold highlight the algorithms that show the best performance in terms of accuracy or runtime. The same applies to other tables. In these tables, results for FOIL, TILDE are taken from [1]. Results for 1BC are taken from [7]. Results for 1BC2 are taken from [11]. Results for Mr-SBC are taken from [2]. Table 6 reports the average accuracy for these three backgrounds.

Notice that the average accuracy of Multi-relational Bayes on BK0 in Table 3 is larger than that of Graph-NB but lower than that of SRG-BC, while the average accuracy of Multi-relational Bayes on BK1 in Table 4 is lower than that of both Graph-NB and SRG-BC, and Graph-NB performs better than SRG-BC on BK1. To interpret this we carried out the paired t-test analysis of the ten-fold cross validation accuracy results. Table 7 summarizes the results. As a negative t-statistic means an improvement in the algorithm performance, we see that SRG-BC performs better than Multi-relational Bayes on all three datasets, while Graph-NB performs better in two out of three cases. Both the tstatistics for BK1 are negative but not signi<sup>fi</sup>cant and Graph-NB yields a smaller p-value than SRG-BC does. These results imply that considering only relation selection (the interim algorithm Graph-NB) can be inadequate to guarantee higher accuracy, but incorporating both relation and feature selection will always be bene<sup>fi</sup>cial and yield higher accuracy than the multi-relational Bayesian classi<sup>fi</sup>er.

The second dataset is a financial database used in PKDD CUP 1999 Its Semantic Relationship Graph is shown in Fig. 1. We made the same modi<sup>fi</sup>cation as that in [23]. Table 8 shows the results of several selected classi<sup>fi</sup>ers using ten-fold cross-validation. The result for TILDE is taken from [23].

```txt
Method:
D={ }; addQ(<target relation, target relation>)
while Q is not empty do
    propagate(delQ( ))
    add propagating routes (or join edges)
    for each edge out of current relation do
    addQ(<current relation, right r>)
    end
    identify feature candidates
    collect features' distribution information
    chi-square tests:
    for each feature f in current relation do
    calculate chi-square statistic C
    if C > critical value(α, df) then
    D = D + {f}
    endif
    endfor
endwhile
R = IFS(D)
Delete non-intermediary relations which do not include any feature in R from SRG
Classify each testing instance based on R
```

![](/api/attachments/Q8HWFPE3/fulltext/images/b7f08a709d82536a5c76139ce6637b113f7c351765a59b9a931562e19356759e.jpg)  
Fig. 3. Optimized SRG for the <sup>fi</sup>nancial database from PKDD CUP99.

We can also observe from Table 8 that Graph-NB and SRG-BC achieve improved accuracy compared with multi-relational Naïve Bayes without pruning strategy. SRG-BC gets the second highest accuracy among these six algorithms and only 0.75% lower than the highest accuracy. But, it is about one order of magnitude faster than CrossMine, several orders of magnitude faster than FOIL and TILDE. This is mainly because SRG-BC processes and formats data only once for each relation, even when the relation is repeatedly traversed in the SRG. However, these ILP-based methods usually need to scan each relation many times for best predicates, undermining their scalabilities. Similarly, we also perform the paired t-tests for this dataset and show the results in Table 9. Both the t-statistics are negative and signi<sup>fi</sup>cant, with the p-value of the second t-test being only 0.001.

Based on the comparative analysis of these experiments on realworld databases, we can conclude that our optimization of SRG pays off, and because of additional feature selection, SRG-BC guarantees stronger performance in terms of accuracy than Multi-relational Bayes does. However, these optimization strategies come along with the sacri<sup>fi</sup>ce of running time. To justify that it is still worthwhile to carry out the optimization, we perform further experiments on the synthetic databases to compare its scalability with ILP approaches with respect to the number of relations and the average number of tuples per relation.

## 6.2. Synthetic databases

The synthetic databases we use here are generated by a generator used in [23]. Details of parameter settings are displayed in Table 10.

As regard to the input parameters, we only vary two parameters and maintain others constant, when generating the databases. The chosen parameters are the number of relations and the expected number of tuples in each relation. We adopt the notation RxTy, where x represents the number of relations and y the number of tuples in

## Table 2

Background knowledge for mutagenesis databases

<table><tr><td>Background</td><td>Description</td></tr><tr><td> $BK_0$ </td><td>For each compound, it obtains atoms, bonds, bond types, atom types, and partial charges on atoms</td></tr><tr><td> $BK_1$ </td><td>Consists of definitions in  $BK_0$  plus attributes indl and inda in the mole table</td></tr><tr><td> $BK_2$ </td><td>Attributes logp and lumo are added to the mole table used in  $BK_1$ </td></tr></table>

Table 3  
Results on BK0 for mutagenesis.

<table><tr><td>Algorithm</td><td>Accuracy (%)</td><td>Runtime (second)</td></tr><tr><td>SRG-BC</td><td>80.8</td><td>1.6</td></tr><tr><td>Graph-NB</td><td>77</td><td>1.2</td></tr><tr><td>Multi-relational Bayes</td><td>77.5</td><td>1.1</td></tr><tr><td>CrossMine</td><td>68.8</td><td>2.5</td></tr><tr><td>FOIL</td><td>61</td><td>4950</td></tr><tr><td>TILDE</td><td>75</td><td>93</td></tr><tr><td>1BC</td><td>80.3</td><td>-</td></tr><tr><td>1BC2</td><td>72.9</td><td>-</td></tr><tr><td>Mr-SBC</td><td>76.5</td><td>36</td></tr></table>

Table 8

Table 4  
Results on BK1 for mutagenesis.

<table><tr><td>Algorithm</td><td>Accuracy (%)</td><td>Runtime (second)</td></tr><tr><td>SRG-BC</td><td>83.1</td><td>1.6</td></tr><tr><td>Graph-NB</td><td>84.1</td><td>1.1</td></tr><tr><td>Multi-relational Bayes</td><td>77</td><td>1.1</td></tr><tr><td>CrossMine</td><td>88.2</td><td>1.6</td></tr><tr><td>FOIL</td><td>61</td><td>9138</td></tr><tr><td>TILDE</td><td>79</td><td>355</td></tr><tr><td>1BC</td><td>-</td><td>-</td></tr><tr><td>1BC2</td><td>-</td><td>-</td></tr><tr><td>Mr-SBC</td><td>81</td><td>42</td></tr></table>

Table 5

Results on BK2 for mutagenesis.

<table><tr><td>Algorithm</td><td>Accuracy (%)</td><td>Runtime (second)</td></tr><tr><td>SRG-BC</td><td>87.24</td><td>1.7</td></tr><tr><td>Graph-NB</td><td>86.2</td><td>1.1</td></tr><tr><td>Multi-relational Bayes</td><td>78.1</td><td>1.1</td></tr><tr><td>CrossMine</td><td>88.8</td><td>1.4</td></tr><tr><td>FOIL</td><td>83</td><td>0.5</td></tr><tr><td>TILDE</td><td>85</td><td>221</td></tr><tr><td>1BC</td><td>87.2</td><td>-</td></tr><tr><td>1BC2</td><td>72.9</td><td>-</td></tr><tr><td>Mr-SBC</td><td>89.9</td><td>48</td></tr></table>

Table 6  
Average accuracy for mutagenesis.

<table><tr><td>Algorithm</td><td>Average accuracy (%)</td></tr><tr><td>SRG-BC</td><td>83.7</td></tr><tr><td>Graph-NB</td><td>82.3</td></tr><tr><td>Multi-relational Bayes</td><td>77.5</td></tr><tr><td>CrossMine</td><td>81.9</td></tr><tr><td>FOIL</td><td>68.3</td></tr><tr><td>TILDE</td><td>79.7</td></tr><tr><td>Mr-SBC</td><td>82.4</td></tr></table>

Table 7  
Results of the paired t-test (two-tail)

<table><tr><td>Paired t-test (df=9)</td><td>BK0</td><td>BK1</td><td>BK2</td></tr><tr><td>Multi-relational Bayes vs. Graph-NB</td><td>1.9 (0.08)</td><td>-1.9 (0.09)</td><td>-2.2 (0.05)</td></tr><tr><td>Multi-relational Bayes vs. SRG-BC</td><td>-2.3 (0.04)</td><td>-1.5 (0.14)</td><td>-2.2 (0.05)</td></tr></table>

Note: p-values are listed in parentheses.

Results on <sup>fi</sup>nancial database.

<table><tr><td>Algorithm</td><td>Accuracy (%)</td><td>Runtime (second)</td></tr><tr><td>SRG-BC</td><td>86.5</td><td>1.28</td></tr><tr><td>Graph-NB</td><td>85.75</td><td>0.45</td></tr><tr><td>Multi-relational Bayes</td><td>82</td><td>0.44</td></tr><tr><td>CrossMine</td><td>87.25</td><td>13.4</td></tr><tr><td>FOIL</td><td>71.5</td><td>3479.3</td></tr><tr><td>TILDE</td><td>81.3</td><td>2429</td></tr></table>

## Table 9

Results of the paired t-test (two-tail).

<table><tr><td>Paired t-test (df=9)</td><td>Financial database</td></tr><tr><td>Multi-relational Bayes vs. Graph-NB</td><td>-3.3 (0.01)</td></tr><tr><td>Multi-relational Bayes vs. SRG-BC</td><td>-4.7 (0.001)</td></tr></table>

Note: p-values are listed in parentheses.

Parameters of database generator.

<table><tr><td>Name</td><td>Description</td><td>Def.</td></tr><tr><td>|R|</td><td># relations</td><td>x</td></tr><tr><td> $T_{\text{min}}$ </td><td>Min # tuples in each relation</td><td>50</td></tr><tr><td>T</td><td>Expected # tuples in each relation</td><td>y</td></tr><tr><td> $A_{\text{min}}$ </td><td>Min # attributes in each relation</td><td>2</td></tr><tr><td>A</td><td>Expected # attributes in each relation</td><td>5</td></tr><tr><td> $V_{\text{min}}$ </td><td>Min # values in each relation</td><td>2</td></tr><tr><td>V</td><td>Expected # values in each relation</td><td>10</td></tr><tr><td> $F_{\text{min}}$ </td><td>Min # foreign-keys in each relation</td><td>2</td></tr><tr><td>F</td><td>Expected # foreign-keys in each relation</td><td>z</td></tr><tr><td>|r|</td><td># rules</td><td>10</td></tr><tr><td> $L_{\text{min}}$ </td><td>Min # complex predicates in each rule</td><td>2</td></tr><tr><td> $L_{\text{max}}$ </td><td>Max # complex predicates in each rule</td><td>6</td></tr><tr><td> $f_{\text{A}}$ </td><td>Prob. of a predicate on active relation</td><td>0.25</td></tr></table>

each relation. The expected number of foreign keys in each relation is set to 1. For each generated database, we divide it into two parts with the <sup>fi</sup>rst 90% of the target relation as training data and the remainder as testing data. Accuracy is obtained for the testing data.

Since CrossMine has shown its better scalability than most other multi-relational classi<sup>fi</sup>ers such as FOIL and TILDE, now we only compare the performance of SRG-BC with CrossMine. In our setting, there are two sets of experiments to be carried out. The <sup>fi</sup>rst set is to evaluate the accuracy and scalability with respect to the number of relations in the database. We construct three kinds of databases with 10, 15 and 20 relations, respectively. For each database, the expected number of tuples in each relation is 1000. Accuracy and runtime results are displayed in Figs. 4 and 5. The second set is to evaluate the accuracy and scalability with respect to the number of tuples per relation. We construct four databases with 1000, 3000, 6000 and 10000 expected tuples per relation, respectively. For each database, the expected number of relations is set to 10. Figs. 6 and 7 report the accuracy and runtime for this set of experiments.

![](/api/attachments/Q8HWFPE3/fulltext/images/6e8cf3181b3903c705a699313710ead476d71580eebe28f90484d9cb3d29a73e.jpg)  
Fig. 4. Accuracy on R\*.T1000.

![](/api/attachments/Q8HWFPE3/fulltext/images/d1888b8dbf7f114a891a9caca5791aeb375d2aad34c69fdbae40129150476083.jpg)  
Fig. 5. Runtime on R\*.T1000.

![](/api/attachments/Q8HWFPE3/fulltext/images/485024550b8d203fc2e15b64e1723dd592d1ed6d1564c28787f82d24d91974d4.jpg)  
Fig. 6. Accuracy on R10.T\*.

At the <sup>fi</sup>rst glance, we notice that SRG-BC dominates in speed, no matter how many relations and tuples are in the tested databases, as there is obvious difference between the runtime of these two algorithms. As to accuracy, the results for SRG-BC and CrossMine are almost comparable to each other. In 3 out of 6 cases, SRG-BC is more accurate than CrossMine, while in the remaining cases, CrossMine is more accurate. This proves that our optimization strategies described in Section 4 are effective, making SRG-BC outperform CrossMine in terms of runtime and retain comparable accuracy.

## 6.3. Sensitivity of significance level parameter

In Section 4.1, we have mentioned the impact signi<sup>fi</sup>cance levelα will exert on the predictive power of the algorithm. Now we will look into this issue in more detail. Depending on the value of signi<sup>fi</sup>cance level, the algorithm may generate different sets of discriminatory features (either in terms of set size or feature member), thus this may result in different outputs of optimal feature sets which will be used to build the Bayesian classi<sup>fi</sup>ers. We investigate this impact by setting signi<sup>fi</sup>cance level α to a series of values from large to small. Theoretically, larger values of signi<sup>fi</sup>cance level α will <sup>fi</sup>lter out fewer features and produce more discriminatory features for iterative ranking, which in turn implies it will take more time to complete the process. However, it is dif<sup>fi</sup>cult to decide straightforwardly that there is direct relationship between signi<sup>fi</sup>cance level and accuracy. We hope the following experimental results could shed light on this issue.

![](/api/attachments/Q8HWFPE3/fulltext/images/3070f0a85a6a78b2f219f031e6b08ca39b58b007bfe9dedfc8d161e05bb4f2b6.jpg)  
Fig. 7. Runtime on R10.T\*.

We have chosen 0.1, 0.05, 0.005, and 0.0005 for experiments. We test these parameters using both real-world and synthetic databases described above. The results are shown in Table 11.

As illustrated in Table 11, it turns out that the accuracies are almost the same for these small-value cases (0.05, 0.005, and 0.0005), with the 0.0005 case being the highest. Besides, $\alpha { = } 0 . 1$ gives relatively weaker accuracies compared with others. We can thus conclude that accuracy does not change a lot with the change of signi<sup>fi</sup>cance level.

We can analyze the number of chosen features and relations to further investigate what results in the insensitivity of signi<sup>fi</sup>cance level. Fig. 8 shows the number of chosen features versus different signi<sup>fi</sup>cance levels for six synthetic databases.

First, we can observe from the vertical axis that the numbers are generally very small (less than 18, sometimes as low as 3, remembering that each database contains at least 10 tables). This means SRG-BC successfully chooses the most useful features to construct the Bayesian classi<sup>fi</sup>er. Second, half of these curves are <sup>fl</sup>at, and others’ disparities in the number of chosen features are less than 4. Therefore, under different signi<sup>fi</sup>cance levels, SRG-BC is robust enough to exclude harmful or unnecessary features and at the same time identify the most discriminatory ones.

## 7. Conclusion

In this paper, we present an improved algorithm SRG-BC for multirelational classi<sup>fi</sup>cation. Depending on Bayesian classi<sup>fi</sup>ers’ inherent robustness and resilience against noise, we adopt relation selection and feature selection to optimize the training process based on Semantic Relationship Graph. We simplify SRG by keeping only relevant relations that either contain selected features or are useful in virtual joining. We implement chi-square tests on all available features to select a pool of discriminatory features as input for an iterative classifying and ranking process, rather than straightforwardly building the classi<sup>fi</sup>er using all features. In our setting, the optimizing strategy for SRG is a combination of relation and feature selection, producing a simpli<sup>fi</sup>ed Semantic Relationship Graph. The selection of relevant relations and a pool of discriminatory features makes SRG-BC achieve improved accuracy over the simple multi-relational Bayes classi<sup>fi</sup>er at small costs. The performance comparison of SRG-BC and CrossMine shows that both have comparable accuracy, but SRG-BC requires much less running time.

Although our experimental results have been encouraging, there remain many possibilities for future work. Currently, we only use chisquare statistic as a <sup>fi</sup>lter method to select discriminatory features. There are a lot of other methods that can be used to achieve the same goal. Comparative study of different methods could help us <sup>fi</sup>nd an optimal approach to determining features with good predictive power under the multi-relational context. In addition, the iterative classifying and ranking method is a greedy method which may undermine the algorithm's ef<sup>fi</sup>ciency. More work can be done to resolve this issue to enhance ef<sup>fi</sup>ciency further.

Result for different signi<sup>fi</sup>cance levels.

<table><tr><td rowspan="2">Data sets</td><td colspan="4">Significance level</td></tr><tr><td>0.1</td><td>0.05</td><td>0.005</td><td>0.0005</td></tr><tr><td>Fin_DB</td><td>85.5</td><td>84.75</td><td>86.5</td><td>84</td></tr><tr><td>Muta_BK0</td><td>80.8</td><td>80.8</td><td>80.8</td><td>80.27</td></tr><tr><td>Muta_BK1</td><td>83.1</td><td>83.1</td><td>83.1</td><td>83.1</td></tr><tr><td>Muta_BK2</td><td>87.24</td><td>87.24</td><td>87.24</td><td>87.24</td></tr><tr><td>R10T1000</td><td>85</td><td>89</td><td>87</td><td>88</td></tr><tr><td>R10T3000</td><td>91</td><td>91</td><td>91</td><td>91</td></tr><tr><td>R10T6000</td><td>98</td><td>98</td><td>98</td><td>98</td></tr><tr><td>R10T10000</td><td>71.4</td><td>71.4</td><td>71.4</td><td>71.4</td></tr><tr><td>R15T1000</td><td>69</td><td>74</td><td>74</td><td>75</td></tr><tr><td>R20T1000</td><td>82</td><td>86</td><td>86</td><td>89</td></tr><tr><td>Average</td><td>83.30</td><td>84.53</td><td>84.50</td><td>84.70</td></tr></table>

![](/api/attachments/Q8HWFPE3/fulltext/images/e5002fe85820b52490cac9f968097b6016a7f77d8432520b3c2b7864a16876b1.jpg)  
Fig. 8. Number of chosen features.

Finally, the results of this study demonstrate that Bayesian classi<sup>fi</sup>ers can perform remarkably well in the multi-relational setting if relation selection and feature selection can be incorporated in the training process. The feature selection method can be directly used as a preprocessing step of other classi<sup>fi</sup>cation algorithms such as rule based or decision tree algorithms. In future research, we will study how relation and feature selection can be utilized in improving the performance of other kinds of learning algorithms.

## Acknowledgements

This paper was supported in part by the National Natural Science Foundation of China under Grant No. 70871068, 70621061, 70890083, and Key Laboratory of Data Engineering and Knowledge Engineering (Renmin University of China), Ministry of Education under Grant No. 2008001.

## References

[1] H. Blockeel, L. De Raedt, J. Ramon, Top-down induction of logical decision trees, In Proc. 1998 Int. Conf. Machine Learning (ICML'98), Madison, WI, 1998, Aug.

[2] M. Ceci, A. Appice, D. Malerba, Mr-SBC: A multi-relational naive bayes classi<sup>fi</sup>er, in: N. Lavrac, D. Gamberger, L. Todorovski, H. Blockeel (Eds.), Knowledge discovery in databases PKDD 2003, Lecture Notes in Arti<sup>fi</sup>cial Intelligence, 2838, Springer, Berlin, Germany, 2003, pp. 95–106.

[3] Y. Chen, D. Liginlal, A maximum entropy approach to feature selection in knowledgebased authentication, Decision Support Systems 46 (1) (2008) 388–398 December

[4] P. Domingos, M. Pazzani, Beyond independence: Conditions for the optmality of th simple Bayesian classi<sup>fi</sup>er, In Proc.13th Intl. Conf. Machine Learning,1996, pp.105–112

[5] R. Duda, P. Hart, Pattern classi<sup>fi</sup>cation and scene analysis, John Wiley & Sons, New York, 1973.

[6] P. Flach, N. Lachiche, 1BC: A <sup>fi</sup>rst-order Bayesian classi<sup>fi</sup>er, Proceedings of the 9th International Workshop on Inductive Logic Programming, 1999, pp. 92–103.

[7] P. Flach and N. Lachiche. First-order Bayesian classi<sup>fi</sup>cation with 1BC. Submitted. Downloadable from http://hydria.u-strasbg.fr/\~lachiche/1BC.ps.gz.

[8] N. Friedman, L. Getoor, D. Koller, A. Pfeffer, Learning probabilistic relational models, In Sixteenth International Joint Conference on Arti<sup>fi</sup>cial Intelligence (IJCAI 1999.

[9] D. Koller, A. Pfeffer, Probabilistic frame-based systems, In Proceedings of the fifteenth national conference on artificial intelligence, AAAI Press, Madison, WI. 1998 pp. 580-587

[10] M. Krogel, S. Rawles, F. Zelezny, P. Flach, N. Lavrac, S. Wrobel, Comparative evaluation of approaches to propositionalization, in: T. Horváth, A. Yamamoto
