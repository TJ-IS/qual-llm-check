---
otero_id: 1004
otero_key: "YWZVTDN2"
title: "Cross-domain aspect extraction for sentiment analysis: A transductive learning approach"
authors: "Ricardo Marcondes Marcacini; Rafael Geraldeli Rossi; Ivone Penque Matsuno; Solange Oliveira Rezende"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.08.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
<table><tr><td>PII:</td><td>S0167-9236(18)30138-6</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.08.009</td></tr><tr><td>Reference:</td><td>DECSUP 12983</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>10 April 2018</td></tr><tr><td>Revised date:</td><td>27 July 2018</td></tr><tr><td>Accepted date:</td><td>21 August 2018</td></tr></table>

## Accepted Manuscript

Cross-domain aspect extraction for sentiment analysis: a transductive learning approach

Ricardo Marcondes Marcacini, Rafael Geraldeli Rossi, Ivone Penque Matsuno, Solange Oliveira Rezende

![](/api/attachments/YWZVTDN2/fulltext/images/4dfccfbf20f981071fa245bc421cee0cab1ef95fdb6d7934f89e5c172d7e3d01.jpg)

Please cite this article as: Ricardo Marcondes Marcacini, Rafael Geraldeli Rossi, Ivone Penque Matsuno, Solange Oliveira Rezende , Cross-domain aspect extraction for sentiment analysis: a transductive learning approach. Decsup (2018), doi:10.1016/ j.dss.2018.08.009

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Cross-domain aspect extraction for sentiment analysis: a transductive learning approach

Ricardo Marcondes Marcacini<sup>b,∗</sup>, Rafael Geraldeli Rossi<sup>b</sup>, Ivone Penque Matsuno<sup>a</sup>, Solange Oliveira Rezende<sup>a</sup>

<sup>a</sup>Institute of Mathematics and Computer Sciences (ICMC) University of São Paulo (USP)

Av. Trabalhador São Carlense, 400, 13566-590, São Carlos, SP, Brazil <sup>b</sup>Federal University of Mato Grosso do Sul (UFMS)

Av. Ranulpho Marques Leal, 3484, 79613-000, Três Lagoas, MS, Brazil

## Abstract

Aspect-Based Sentiment Analysis (ABSA) is a promising approach to analyze consumer reviews at a high level of detail, where the opinion about each feature of the product or service is considered. ABSA usually explores supervised inductive learning algorithms, which requires intense human efort for the labeling process. In this paper, we investigate Cross-Domain Transfer Learning approaches, in which aspects already labeled in some domains can be used to support the aspect extraction of another domain where there are no labeled aspects. Existing cross-domain transfer learning approaches learn classifiers from labeled aspects in the source domain and then apply these classifiers in the target domain, i.e., two separate stages that may cause inconsistency due to diferent feature spaces. To overcome this drawback, we present an innovative approach called CD-ALPHN (Cross-Domain Aspect Label Propagation through Heterogeneous Networks). First, we propose a heterogeneous networkbased representation that combines diferent features (labeled aspects, unlabeled aspects, and linguistic features) from source and target domain as nodes in a single network. Second, we propose a label propagation algorithm for aspect

ACCEPTED MANUSCRIPT

extraction from heterogeneous networks, where the linguistic features are used as a bridge for this propagation. Our algorithm is based on a transductive learning process, where we explore both labeled and unlabeled aspects during the label propagation. Experimental results show that the CD-ALPHN outperforms the state-of-the-art methods in scenarios where there is a high-level of inconsistency between the source and target domains — the most common scenario in real-world applications.

Keywords: Cross Domain, Opinion Mining, Aspect Extraction

## 1. Introduction

Opinion Mining and Sentiment Analysis have become very popular for automating the knowledge extraction from user reviews about products and services (Liu, 2012; Cambria, 2016; Breck & Cardie, 2017). In general, the goal is to determine the consumer’s opinion on some topic through the sentiment polarity expressed in textual reviews (e.g. positive, negative or neutral) (Liu & Zhang, 2012). While the first studies on sentiment analysis attempted to extract the polarity from the entire text review (document-level sentiment analysis) or from the text sentences (sentence-level sentiment analysis), more recent studies investigate aspect-based sentiment analysis (ABSA) (Feldman, 2013; Lau et al., 2014; Schouten & Frasincar, 2016; Akhtar et al., 2017). In this case, consumer reviews are analyzed at a high level of detail, where the opinion about each feature of the product or service is considered, such as quality of a camera’s photos, notebook weight, and food price. In fact, ABSA tasks are considered more complex (Mukherjee & Liu, 2012; Wang et al., 2014; Matsuno et al., 2017) because we need to deal with a challenging question during the sentiment analysis process: how to automatically extract the aspects of each product or service from consumer reviews?

Existing works for aspect extraction are based on linguistic features patterns (Rana & Cheah, 2016), where natural language processing techniques are used to identify grammatical classes and syntactic relations of the text reviews. In this case, a set of previously labeled aspects (training set) is used in a supervised inductive learning task, which induces a classification model considering only labeled examples. Next, aspects are extracted from the new text reviews according to the linguistic features presented to the classifier. For example, a supervised rule-based classifier that learned the following attern word h is a noun AND h is in a relationship with a verb t THEN h is extracted as an presented in Figure 1, where h=“camera” and t=“is”. The relationship between h and t is defined by the adjective “nice”.

![](/api/attachments/YWZVTDN2/fulltext/images/368189345782888359d024c325d54463740ae948cc9009f6841fafec1f00c326.jpg)  
Figure 1: Part-of-Speech (PoS) and Syntactic Relations extracted from the sentence “The camera is nice”.

Aspect-based sentiment analysis usually explores inductive supervised learning algorithms, which requires intense human efort for the labeling process in order to obtain satisfactory classification performances (Rana & Cheah, 2016; Schouten & Frasincar, 2016). However, frequent data labeling is not feasible in practical situations. To address this challenge, transductive learning is widely used when there are few labeled data, while unlabeled data are easy to collect (Kong et al., 2013; Chapelle et al., 2006; Belkin et al., 2006; Joachims, 1999). Transductive learning directly classifies unlabeled data and make use of this known unlabeled data to improve classification performance (Kong et al., 2013).

Another challenge related to the aspect extraction for sentiment analysis is to deal with specific characteristics and limitations of the application domain (Duric & Song, 2012; Deng et al., 2017). For example, reviews collected from social networks may contain short texts with informal language (e.g. neologisms, slang, and jargon terms), while specialized forums may contain more technical language and longer texts. Therefore, an important research question is how can we efectively exploit the already labeled aspects in some domain to aid the aspect extraction in another domain? Studies addressing this question are known as Cross-Domain Transfer Learning and have been reported as a promising solution to problems where frequent data labeling is impossible or expensive (Pan & Yang, 2010; Schouten & Frasincar, 2016; Zhang et al., 2016; Rana & Cheah, 2017).

The problems mentioned above can be attenuated with the use of transductive semi-supervised learning. While supervised inductive learning obtains a classification model to classify unknown examples with possibly diferent feature space and distributions, transductive semi-supervised learning already knows the predictive space and can make use of it to improve the classification performance. Besides, when cross-domain transfer learning is applied, usually the examples to be classified are already collected. Thus, transductive semi-supervised learning is more adequate for this type of situation. However, it is necessary to deal with two important research questions for transductive learning in transfer learning scenario: (1) How to properly structure information from diferent domains into a unified representation? (2) How to efectively exploit this unified representation to transfer knowledge from the source domain to the target domain? These questions motivated us to investigate and propose a specific transductive learning solution for aspect extraction considering the cross-domain transfer learning scenario.

In this paper, we present a cross-domain aspect extraction approach based on transductive learning called CD-ALPHN (Cross-Domain Aspect Label Propagation through Heterogeneous Networks). While existing cross-domain approaches learn classifiers from labeled aspects in the source domain and then apply these classifiers in the target domain, i.e., two separate stages that may cause inconsistency due to diferent feature spaces or diferent marginal probability distributions, we propose a unified transductive learning process from both source and target feature spaces. The main contributions are two-fold:

• We present a heterogeneous network-based model representation where labeled aspects of the source domain, linguistic features, and unlabeled aspects of the target domain are all mapped as nodes in a heterogeneous network — which allows diferent feature types in a unified representation model. Our proposed heterogeneous network model is an efective (preknowledge from diferent domains for cross-domain transfer learning.

• We present a transductive learning algorithm for heterogeneous networks, where labeled and unlabeled nodes are exploited in a label propagation process. In this case, the source domain label information (labeled aspects) are propagated to the linguistic features nodes. Next, linguistic feature labels are propagated to the target domain (aspect candidates nodes) — which then propagates label information back to the network. This propagation process continues until the convergence, i.e. when the label information of the network nodes are not changed significantly. Thus, the cross-domain transfer learning process is carried out in a more natural way, with the advantage of using a mathematical formalization framework and theoretic guarantees of convergence.

We carried out an experimental evaluation with seven benchmark datasets to compare our proposed CD-ALPHN with other state-of-the-art methods, such as Multilayer Perceptron Neural Networks (MLP) and Support Vector Machines (SVM). Experimental evaluation results show that our approach is very competitive, outperforming MLP and SVM methods in scenarios where there is a high-level of inconsistency between the source and target domains — the most common scenario in real-world applications. In addition, we also provide an overview of how our approach can be used in real-world applications by a Data Analytics System to support the decision-making process.

The remainder of this paper is organized as follows. Section 2 presents the main concepts about cross-domain transfer learning and transductive learning, as well as the related work about aspect extraction for sentiment analysis. Section 3 describes in detail our CD-ALPHN approach, especially our proposed heterogeneous network model and the proposed label propagation algorithm for transductive learning. The experimental evaluation results comparing our CD-ALPHN and five other state-of-the-art methods for cross-domain transfer learning are presented and discussed in Section 4. Finally, Section 5 discusses the conclusions of this work and directions for future work.

## 2. Related Work

Cross-Domain Transfer Learning aims to utilize labeled data from other domains to help current learning task (Pan & Yang, 2010). The domain with labeled data is called the source domain, while the domain without labeled data is called the target domain. In real-world applications, diferent domains may have diferent feature spaces as well as diferent underlying data distributions — thereby requiring appropriate learning approaches to address these drawbacks (Long et al., 2014a).

Most of the existing studies for cross-domain transfer learning are known as inductive transfer learning (Pan & Yang, 2010; Lu et al., 2015). In this case, the goal is to identify features that are useful in both the target domain and the source domain, thereby obtaining a shared feature space for the cross-domain transfer learning problem. In some studies, the best features for both source and target domains are selected and reweighted to improve the final classification (Chen et al., 2014; Lu et al., 2015). Inductive transfer learning is also presented as a two-stage cross-domain transfer learning (Wu & Tan, 2011; Rana & Cheah, 2017). In the first stage, a set of features that are common to both domains is extracted, and in the second stage, useful features specific to the target domain are selected to learn a classifier (Wu & Tan, 2011; Rana & Cheah, 2017).

Diferent strategies to learn classifier models have been proposed for crossdomain transfer learning (Lu et al., 2015). The most common strategy (with promising results) is to train well-known classifiers such as Multilayer Perceptron, SVM, Naive-Bayes, and kNN, considering the feature space that is common to both domains. Other strategies are based on the consensus of several classifiers with diferent data sampling from both the source and target domain (Luo et al., 2008; Zhuang et al., 2010). Moreover, there are strategies that use active learning to improve the transfer learning process, i.e., they require human feedback when a set of classifiers disagree about the class of some instance in the target domain (Li et al., 2013; Wu et al., 2017).

The vast majority of existing studies focus primarily on the transfer of sentiment polarity between diferent domains, while the use of cross-domain transfer learning for aspect extraction is underexplored (Al-Moslmi et al., 2017). Some recent initiatives explore linguistic features extracted from the aspects to obtain a common feature space between the two domains (Zhang et al., 2016; Rana & Cheah, 2017). However, these studies also use the two-stage inductive learning transfer approach, which works well only under the following assumption: the source and target domain data are drawn from the same feature space and the same distribution (Pan & Yang, 2010). In other words, inductive learning approaches will fail when there is a high level of inconsistency between the source and target domains — which is the most common case in real-world applications (Pan & Yang, 2010; Long et al., 2015).

In cross-domain transfer learning problems, recent studies claim that unifying diferent domains using graphs as an intermediate representation yields more satisfactory results (Rohrbach et al., 2013; Long et al., 2014b; Chang et al., 2017). Thus, graph nodes represent examples of both source and target domain and the edges represent the relations between examples. Some nodes are labeled and the learning process involves identifying the label of unlabeled nodes according to the topological properties of the graph. Both the graph construction and the graph-based learning algorithm are challenging tasks, especially in relation to the scalability problem of the graph-based transductive learning (Ryan & Michailidis, 2017). For example, a common technique for graph building is via nearest neighbor-based algorithm, which presents quadratic complexity of time and space.

Transductive learning is a promising approach that explores both labeled and unlabeled data (e.g. source and target domains) during the training process and is generally used in semi-supervised learning scenarios (Joachims, 2003). Unlike the supervised inductive classification, which aims to create a classification model to approximate a real class assignment function, the goal of transductive learning is to find an admissible function in which the unlabeled data are used to improve classification performance (Zhou et al., 2004). In practice, transductive learning assigns weights or relevance scores to examples for each one of the classes and the examples are classified considering these weights.

It is worth mentioning that transductive learning has shown to be helpful for cross-domain transfer learning problems (Wu & Tan, 2011; Al-Moslmi et al., 2017; Chang et al., 2017; Ryan & Michailidis, 2017). This observation has motivated us to employ related approaches for aspect extraction in sentiment analysis, which in this particular setting is a challenge not addressed in the literature.

## 3. Cross-Domain Aspect Label Propagation through Heterogeneous Networks

Our CD-ALPHN (Cross-Domain Aspect Label Propagation through Heterogeneous Networks) approach is presented in two steps. In the first step, we describe the heterogeneous network construction and its use as a unified representation between the source and target domains. In the second step, we discuss our proposed algorithm for transductive learning, which uses label propagation in the heterogeneous network to transfer label information of the labeled aspects from the source domain to the “candidate” aspects of the target domain, by using linguistic feature patterns as a bridge.

## 3.1. Cross-Domain Data Representation using Heterogeneous Networks

Network-based algorithms came up to avoid the drawbacks of the algorithms based on vector-space model and to improve transductive classification (Gupta et al., 2015; Rossi et al., 2016). Networks are mostly used for label propagation, in which some labeled objects propagate their labels to other objects through the network connections to perform transductive classification (Zhu & Goldberg, 2009; Rossi et al., 2014; Subramanya & Bilmes, 2008; Zhou et al., 2004). Moreover, the use of networks to model data allows extracting patterns which are not extracted by algorithms based on vector-space model (Breve et al., 2012).

In this paper, we propose a cross-domain unified representation based on a heterogeneous network, i.e., a network composed by diferent types of nodes by $G = ( V , E , W )$ , where V represents the set of nodes, E represents the edges connecting the nodes, and W represents the weights of the edges. The set V is composed of aspects from the source domain $( A ^ { S } )$ , aspects from the target domain (A<sup>T</sup> ) and linguistic features L extracted by a Part-of-Speech (PoS) process as shown in Figure 1. Thus, $V = \{ A ^ { S } \cup A ^ { T } \cup L \}$

Figure 2 illustrates the general scheme of the heterogeneous network proposed in this work. The set of edges E connect the linguistic features L to the nodes in sets $A ^ { S }$ and $A ^ { T }$ . Thus, if two aspects participate in the same syntactic relationship, then the two nodes that represent these aspects will be connected to the node representing the linguistic feature of this syntactic relation. The words of an aspect usually appear in many text reviews, and thus the set W indicates the weight of the edges — calculated by the frequency of occurrence between the (candidate) aspect nodes and the linguistic feature nodes. Linguistic features are common to both source and target domains and can be interpreted as a bridge between the two domains.

We argue that this type of representation is an intuitive strategy for combining information obtained from diferent domains. This unified representation also eliminates several inconsistencies of existing transfer learning approaches, since the feature space is shared by both source and target domains. Unlike most of the existing approaches, our proposed representation does not require the computation of the k nearest neighbors of an instance for the construction of the graph relations. In fact, the construction of our heterogeneous network can be done in linear time, since this representation maps directly the attributevalue table extracted from the text preprocessing.

![](/api/attachments/YWZVTDN2/fulltext/images/25ae6b550674c323c4d24c9fb2598ddc284d63ce9344cb313418009283c1d528.jpg)  
Figure 2: A general scheme of the heterogeneous network proposed for a unified representation of the feature spaces between the source domain (labeled aspect nodes) and the target domain (candidate aspect nodes), in which linguistic features are used as bridge nodes.

In order to exemplify the network generation through the proposed approach, we present a step-by-step example. In Table 1 we present respectively two sentences, PoS and syntactic relations, and the generated network from computers domain. Rectangular forms represent the terms, and a circular form represents the linguist features . Linguistic features are composed of the PoS tag, type of syntactic relation, and if it is an input relation (in) or an output relation (out).

For instance, considering the Sentence #1 in Table 1, the term battery (noun - NN) contains the input relation nsubj; and the term nice (adjective - JJ) contains the output relation nsubj. Thus, two nodes with their respective linguistic features are generated: NN:subj:in and JJ:subj:out. Also in the same example, we can notice that the weight of the edge between the term the and the linguistic feature DT:det:in is 2 since the term the occurs two times in Sentence #1 and in both time belongs to the relation DT:det:in.

In Table 2 we present four sentences about wine reviews that we consider as target domain in order to build a complete network considering aspect and non-aspects from the source domain, aspect candidates from the target domain,

Table 1: Examples of the network generations for each review about computers - domain source.  
![](/api/attachments/YWZVTDN2/fulltext/images/71bc4e967893f57ce5fd5587c675303c772498b05adf99e8149726d208c1e056.jpg)

and linguistic features from both domains. The complete network with labeled aspects from the source domain is illustrated in Figure 3. We disregard preposition, pronouns, and network components witch contains nodes from a single domain in order to better visualize the network.  
![](/api/attachments/YWZVTDN2/fulltext/images/76da91a4a746aef45ec8d00b9d9837702016ecc5ce3a3d5fa95d4b94dfaf7764.jpg)  
Figure 3: Illustration of the proposed network for cross-domain aspect extraction considering the sentences presented in Tables 1 and 2.

Table 2: Examples of the network generations for each review about wines - target domain.  
![](/api/attachments/YWZVTDN2/fulltext/images/26773a17071e1afad5c382171909e3af54c11f212d4bf39b5e2ab1e1d4016926.jpg)

In summary, our proposal for cross-domain data representation unifies features (and their relations) of the source and target domains. The proposed heterogeneous network contains (1) nodes with aspects labeled as “YES” and “NO” for source domain data, (2) nodes with aspect candidates that are terms (e.g. noun, verb, adjective, and adverb) extracted from the target domain, and (3) nodes with linguistic features extracted from the text reviews of both domains — which we use as a bridge to propagate the labels of the source domain to the nodes of the target domain. Moreover, all nodes in the network contain an information vector. For labeled nodes, this information vector represents the labels of the source domain. For all other nodes, this vector is randomly initialized (or initialized with zeros) and the network regularization function (described in detail in the next section) represents the propagation of the labeled information to all the unlabeled nodes, considering the network topology. Thus, even nodes with linguistic features will receive a vector of label information, although these nodes are only used as a bridge to transfer such information to the target domain.

## 3.2. Aspect Label Propagation through Linguistic Features

We present a transductive learning algorithm based on graph regularization to propagate label information from the source domain to the target domain, where the linguistic features are used as a bridge for this propagation. Our graph regularization algorithm was inspired by the successful use of a similar algorithm introduced in Zhu et al. (2003) and has the basic premise that nodes that share the same neighbor nodes tend to be classified with the same label.

The regularization function to be minimized representing the aspect label propagation is defined in Equation 1, where $a _ { s }$ is a node from the set $A ^ { S }$ representing labeled aspects of the source domain, $a _ { t }$ is a node from the set $A ^ { T }$ representing candidate aspects of the target domain and l is a node from the set L representing linguistic features. The edge weights between linguistic features and aspects are represented by $w _ { a _ { s } , l }$ (for labeled aspects) and $w _ { a _ { t } , l }$ (for candidate aspects). The matrix W will store the edge weights of each network node.

Each node of the network has a vector of labels f, which represents the pertinence level of a node to each one of a class $c _ { l } \in C$ . In the aspect extraction scenario, we have $C = \{ A s p e c t = Y e s , A s p e c t = N o \}$ . The matrix F summarizes the pertinence level of all the nodes and represents the solution of the regularization function. In case of labeled nodes, there is also a real label vector y. Such vector has the value 1 in the position corresponding to the class and 0 in the others. In our proposal, only nodes in the set $A ^ { S }$ will be previously labeled and therefore have y vector. The matrix Y will store all the y vector of the labeled aspects from the source domain.

$$
\begin{array}{l l} Q (\mathbf {F}) = & \sum_ {A ^ {S}, A ^ {T}, L \subset V} \frac {1}{2} \sum_ {a _ {s} \in A ^ {S}} \sum_ {l \in L} w _ {a _ {s}, l} \big (\mathbf {f} _ {a _ {s}} - \mathbf {f} _ {l} \big) ^ {2} \\ & + \frac {1}{2} \sum_ {a _ {t} \in A ^ {T}} \sum_ {l \in L} w _ {a _ {t}, l} \big (\mathbf {f} _ {a _ {t}} - \mathbf {f} _ {l} \big) ^ {2} \\ & + \lim _ {\mu \to \infty} \mu \sum_ {a _ {s} \in A ^ {S}} (\mathbf {f} _ {a _ {s}} - \mathbf {y} _ {a _ {s}}) \end{array}\tag{1}
$$

While the first two terms of Equation 1 determine that nearby nodes share similar label information, the last term determines that the f information of the labeled aspects is not modified during the label propagation process. This means that the node information of the labeled aspects must always be close to the true label information of the aspect nodes from source domain (y).

The minimization of the regularization function in Equation 1 can be obtained via an iterative algorithm since the use of solvers for quadratic programming optimization is computationally expensive and intractable for large numbers of nodes. In this way, we present an iterative algorithm for the cross-domain aspect label propagation through a heterogeneous network (CD-ALPHN). The first term of the Function Q(F), presented in Equation 1, can be iteratively minimized making the label vector of an object $o _ { i } \ ( \mathbf { f } _ { o _ { i } } )$ equals to the harmonic average of the label vector of the neighboring objects. Thus, this step of the iterative solution can be seen as an iterative computation of $\mathbf { F } = \mathbf { P } \mathbf { F }$ , in which $\mathbf P = ( \mathbf D ^ { - 1 } ) \mathbf W .$ Also, there is a reset step $\mathbf { F } _ { A ^ { S } } = \mathbf { Y } _ { A ^ { S } }$ in order to minimize the second term of Equation 1 .

Considering that the matrices F and P can be subdivided considering these three distinct types of network objects, $( A ^ { S } , A ^ { T }$ , and L) the label propagation can be seen as:

$$
\left[ \begin{array}{c} \mathbf {F} _ {A ^ {S}} \\ \mathbf {F} _ {A ^ {T}} \\ \mathbf {F} _ {L} \end{array} \right] = \left[ \begin{array}{c c c} \mathbf {P} _ {A ^ {S} A ^ {S}} & \mathbf {P} _ {A ^ {S} A ^ {T}} & \mathbf {P} _ {A ^ {S} L} \\ \mathbf {P} _ {A ^ {T} A ^ {S}} & \mathbf {P} _ {A ^ {S} A ^ {S}} & \mathbf {P} _ {A ^ {T} L} \\ \mathbf {P} _ {L A ^ {S}} & \mathbf {P} _ {L A ^ {T}} & \mathbf {P} _ {L L} \end{array} \right] \left[ \begin{array}{c} \mathbf {F} _ {A ^ {S}} \\ \mathbf {F} _ {A ^ {T}} \\ \mathbf {F} _ {L} \end{array} \right].\tag{2}
$$

In this case, the values of the submatrices ${ \mathbf { P } } _ { A ^ { s } A ^ { s } } , { \mathbf { P } } _ { A ^ { s } A ^ { T } } , { \mathbf { P } } _ { A ^ { T } A ^ { s } } , { \mathbf { P } } _ { A ^ { s } A ^ { s } }$ and $\mathbf { P } _ { L L }$ are 0 since there are no relations among objects of the same type. Hence, CD-ALPHN performs the transductive classification as presented in Algorithm 1, in which the input is composed of the node sets $A ^ { S } , A ^ { T } ,$ and L of the heterogeneous network, a matrix $\mathbf { Y } _ { A ^ { T } }$ with the real label information of agonal matrix D with the degree (sum of the edge weights) of each node, i.e., $\begin{array} { r } { d _ { v _ { i } , v _ { i } } = \sum _ { v _ { j } \in V } w _ { v _ { i } , v _ { j } } . } \end{array}$

These steps are repeated until stopping criteria are reached. We adopted as stopping criteria the maximum number of iterations, and the minimum mean squared diference between the values of matrix $\mathbf { F }$ in consecutive iterations. Both stopping criteria are possible since the diferences of the values of the matrix F in consecutive iterations will decrease, i.e., the values of the matrix F will converge as presented in the following paragraphs.

Through the iterative solution presented in Algorithm 1, $\mathbf { F } _ { L }$ and $\mathbf { F } _ { A ^ { T } }$ at the n-th iteration can be computed by the Equations 3 and 4 respectively.

$$
\begin{array}{r l} \mathbf {F} _ {L} ^ {(n)} = & \sum_ {i = 0} ^ {n - 1} (\mathbf {P} _ {A ^ {T} L} \mathbf {P} _ {L A ^ {T}}) ^ {i} \mathbf {P} _ {L A ^ {s}} \mathbf {Y} _ {A ^ {s}} + \\ & (\mathbf {P} _ {L A ^ {T}} \mathbf {P} _ {A ^ {T} L}) ^ {n - 1} \mathbf {P} _ {L A ^ {T}} \mathbf {F} _ {A ^ {T}} ^ {(0)} \end{array}\tag{3}
$$

$$
\begin{array}{r c l} \mathbf {F} _ {A ^ {T}} ^ {(n)} & = & \sum_ {i = 0} ^ {n - 1} (\mathbf {P} _ {A ^ {T} L} \mathbf {P} _ {L A ^ {T}}) ^ {i} \mathbf {P} _ {A ^ {T} L} \mathbf {P} _ {L A ^ {S}} \mathbf {Y} _ {A ^ {S}} + \\ & & (\mathbf {P} _ {A ^ {T} L} \mathbf {P} _ {L A ^ {T}}) ^ {n} \mathbf {F} _ {A ^ {T}} ^ {(0)} \end{array}\tag{4}
$$

Since each row of the matrix P is row-normalized, i.e., the sum of the values of the row is 1, the sum of the values of a row of the resulting matrix $( \mathbf { P } _ { A ^ { T } L } \mathbf { P } _ { L A ^ { T } } ) { \mathrm { ~ o r ~ } } ( \mathbf { P } _ { A ^ { T } L } \mathbf { P } _ { L A ^ { T } } )$ always will be lesser than 1. Thus, there exist a

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: Cross-Domain Aspect Label Propagation through Heterogeneous Network (CD-ALPHN)
Input: $A^{S}, A^{T}, L, \mathbf{Y}, \mathbf{W}, \mathbf{D}$
1 begin
2    $\mathbf{P} \leftarrow (\mathbf{D}^{-1}) \cdot \mathbf{W}$
3 repeat
4    foreach $A^{S}, A^{T}, L \subset V$ do
5    $\mathbf{F}_{A^{S}} \leftarrow \mathbf{Y}_{A^{S}}$;    /* Setting the f vector of the labeled aspects from the source domain equal to the real labels */
6    $\mathbf{F}_{L} \leftarrow \mathbf{P}_{L,A^{S}} \cdot \mathbf{F}_{A^{S}} + \mathbf{P}_{L,A^{T}} \cdot \mathbf{F}_{A^{T}}$;    /* Propagating labels from aspects to linguistic features */
7    $\mathbf{F}_{A^{T}} \leftarrow \mathbf{P}_{A^{T},L} \cdot \mathbf{F}_{L,A^{T}}$;    /* Propagating labels from linguistic features to aspect candidate from the target domain */
8    $\mathbf{F}_{A^{S}} \leftarrow \mathbf{P}_{A^{S},L} \cdot \mathbf{F}_{A^{S}}$;    /* Propagating labels from linguistic features to aspects from the source domain */
9    end
10 until stopping criteria;
11 end
12 return $\mathbf{F}(A^{T})$
</div>

γ such that

$$
\sum_ {j = 1} ^ {| A ^ {T} |} (P _ {A ^ {T} L} P _ {L A ^ {T}} [ i, j ]) \leq \gamma <   1  ,
$$

in which [i,j] means the value in $i - t h$ row and $j - t h$ column of a matrix.

At the n-th iteration we have:

$$
\sum_ {j = 1} ^ {| A ^ {T} |} (\mathbf {P} _ {A ^ {T} L} \mathbf {P} _ {L A ^ {T}} [ i, j ]) ^ {(n)} \leq \gamma^ {(n)}.\tag{5}
$$

For $n  \infty ,$

$$
\lim _ {n \to \infty} (\mathbf {P} _ {A ^ {T} L} \mathbf {P} _ {L A ^ {T}}) ^ {n} = 0,\tag{6}
$$

since for each real number $\gamma \leq 1 , \gamma ^ { n } = 0 { \mathrm { ~ w h e n ~ } } n$ tends to infinity. Thus, the proposed solutions for $\mathbf { F } _ { T } ^ { ( n ) }$ and $\mathbf { F } _ { A ^ { T } } ^ { ( n ) }$ converge since they both contains $( \mathbf { P } _ { A ^ { T } L } \mathbf { P } _ { L A ^ { T } } [ i , j ] ) ^ { ( n ) }$

The final classification of the network objects uses the Class Mass Normalization (CMN) concept. Hence, the class of an aspect candidate $a _ { i } \in A ^ { T }$ using CMN is given by Zhu et al. (2003):

$$
c l a s s (a _ {i}) = \arg \max _ {c _ {l} \in \mathcal {C}} P r (c _ {l}) \cdot \frac {f _ {a _ {i} , c _ {l}}}{\sum_ {a _ {j} \in \mathcal {A}} f _ {a _ {j} , c _ {l}}}\tag{7}
$$

in which $P r ( c _ { l } )$ is the prior probability of the class $c _ { l }$

In order to highlight the benefits of the proposed network representation and the network label propagation algorithm, in Figure 4 we illustrate the final labels of the target domain nodes after applying CD-ALPHN in the network presented in Figure 3. Through this illustration, we can notice that some features that do not occur in the source domain will be useful to classify aspect candidates in the target domain. For instance, neither aspect in the source domain is linked to a linguistic node NN:coupuound:out. However, some nodes in the target domain, acidity and palate, propagate the labels to the node NN:coupuound:out, which posteriorly propagates its label to the node aroma.

We highlight that the node aroma would not be classified as aspect in this examples if only the linguistic nodes which appear in the source domain would be considered. The same occurs for the domain target nodes pleasant and good. Those nodes do not have any relation to the linguistic nodes of the source good in the target domain.

![](/api/attachments/YWZVTDN2/fulltext/images/13db69b031f006e6b0d810b56a3b4a77209f766d7c095b1ff195975709ea47f4.jpg)  
Figure 4: Illustration of the label propagation through CD-ALPHN algorithm and considering the network presented in Figure 3.

## 4. Experimental Evaluation

We demonstrate the performance of our proposed CD-ALPHN by using seven benchmark datasets (products and services reviews), as presented in the next section. In addition, an example of Data Analytics System called “Websensors-SentimentAnalysis” is also presented to demonstrate the practical relevance of our proposal in real-world applications.

Our objective is to evaluate the efectiveness of the CD-ALPHN for crossdomain aspect extraction in sentiment analysis tasks. In the benchmark datasets, all sentences with aspects in the source domain have a sentimental word related to the polarity of the aspect (negative, positive or neutral). Although our CD-ALPHN approach does not directly use sentimental words to support the extraction of aspects, the grammatical and syntactic structure of this type of sentence has been mapped in our heterogeneous network.

## 4.1. Datasets

We used seven text review benchmark datasets that are widely cited in the aspect-based sentiment analysis literature. Table 3 presents an overview of the datasets, with the number of reviews (#Reviews), the total number of aspects (#Aspects), the total number of unique terms of the dataset after the text preprocessing (#TotalTerms), and the average number of terms per document (#AvgTerms). Datasets D1 to D5 were obtained from Hu & Liu (2004) and datasets D6 and D7 were obtained from Pontiki et al. (2014).

Table 3: Description of the text review datasets used in the experimental evaluation.

<table><tr><td>ID</td><td>Dataset</td><td>#Reviews</td><td>#Aspects</td><td>#TotalTerms</td><td>#AvgTerms</td></tr><tr><td>D1</td><td>Digital Camera 1</td><td>45</td><td>68</td><td>1045</td><td>54.46</td></tr><tr><td>D2</td><td>Digital Camera 2</td><td>34</td><td>47</td><td>734</td><td>48.74</td></tr><tr><td>D3</td><td>Cellular Phone</td><td>41</td><td>78</td><td>924</td><td>51.70</td></tr><tr><td>D4</td><td>MP3 Player</td><td>95</td><td>126</td><td>1614</td><td>63.95</td></tr><tr><td>D5</td><td>DVD Player</td><td>99</td><td>82</td><td>1074</td><td>33.02</td></tr><tr><td>D6</td><td>Laptop</td><td>3045</td><td>955</td><td>2559</td><td>5.26</td></tr><tr><td>D7</td><td>Restaurant</td><td>3045</td><td>1219</td><td>3083</td><td>5.34</td></tr></table>

All texts were preprocessed using the Stanford CoreNLP (Manning et al., 2014) natural language processing tool to extract the linguistic features.

## 4.2. Experiment Setup

We configured the experiments to compare our proposed CD-ALPHN ap- proach with the state-of-the-art cross-domain approaches for aspect extraction. Existing cross-domain aspect extraction approaches identify features that are common to both source and target domains and learns an inductive classifier from the labeled aspects in the source domain. The learned classifier is applied to classify aspects in the target domain. We used five popular classifiers and we selected the best configurations considering the following parameters:

• J48 (Decision tree-based classifier): we analyzed the values {0.15, 0.20, 0.25} for the confidence parameter.

• kNN (Instance-based classifier): we analyzed the values {1, 3, 5, 7, 9, 11, 13, 15} for the number of nearest neighbors (k parameter) with cosine similarity.

• MLP (Neural network-based classifier using a Multilayer Perceptron and the Backpropagation training algorithm): we analyzed the values {8, 16, 32} for the number of neurons in the hidden layer and the sigmoid function as the activation function.

• NB (Naive-Bayes Classifier): this classifier is parameter free.

• SVM (Support Vector Machine): we analyzed the values $\lbrace 1 0 ^ { - 3 } , 1 0 ^ { - 2 }$ 10<sup>−1</sup>, 10<sup>0</sup>, 10<sup>1</sup>, 10<sup>2</sup>, 10<sup>3</sup>} for the complexity C parameter with polynomial kernel.

• CD-ALPHN (Cross-Domain Aspect Label Propagation through Heterogeneous Networks): our proposed approach is parameter free.

The simulation of a cross-domain process for aspect extraction was performed as follows: given a dataset to represent the target domain, all other datasets are combined to compose the source domain. For example, if dataset D7 represents the target domain, then the source domain is represented by the labeled aspects (and their linguistic features) extracted from datasets D1, D2, D3, D4, D5, and D6. Thus, the proposed experimental evaluation is similar to a real-world scenario where labeled aspects from diferent source domains can be used to extract aspects of a new target domain.

Our experimental setup also considers the level of inconsistency between the source and target domains. In this case, we consider the number of aspects of the target domain $( A ^ { T } )$ that occur in the source domain $( A ^ { S } )$ to compute the level of inconsistency (β parameter), as defined in Equation 8.

$$
\beta = 1 0 0 \times \frac {| A ^ {T} \cap A ^ {S} |}{| A ^ {T} |}\tag{8}
$$

When the cross-domain transfer learning process is performed with low-level of inconsistency, the target domain feature space is well represented in the source domain (there is a significant amount of shared aspects between both domains). For example, we have low-level of inconsistency when the source domain contains aspects about some Digital Camera models (dataset D1) and the target domain contains aspects about another Digital Camera models (dataset D2). Although they are diferent models of Digital Camera, the aspects of this type of product are very similar. On the other hand, when the target domain consists of a completely new product or service with diferent aspects, then we have a highlevel of inconsistency.

Table 4 presents the experimental setup according to four levels of inconsistency (β): Very Low-Level $( \beta > 7 0 \% )$ , Low-Level $( 5 0 \% < \beta \leq 7 0 \% )$ , Mid-Level $( 2 0 \% < \beta \leq 5 0 \% )$ , and High-Level $( \beta ~ < ~ 2 0 \% )$ . We underlined the source domain datasets that have aspects shared with the target domain.

## 4.3. Evaluation Criteria

We use the F1-Measure (Equation 9) to evaluate the aspect extraction performance, which is the harmonic mean between the Precision (Equation 10) and Recall (Equation 11) measures, where:

T P (True Positive) indicates the number of terms inferred as aspects that were correctly extracted;

• F P (False Positive) indicates the number of inferred terms as aspects which are not real aspects; and

• F N (False Negative) indicates the number of terms that are aspects and which were not inferred as aspects.

Table 4: Level of inconsistency (β) considering the number of aspects of the target domain that occur in the source domain.

<table><tr><td>Source Domains</td><td>Target Domain</td><td>Level of Inconsistency</td></tr><tr><td>Digital Camera 2 (D2)Cellular Phone (D3)MP3 Player (D4)DVD Player (D5)Laptop (D6)Restaurant (D7)</td><td>Digital Camera 1 (D1)</td><td>Very Low-Level</td></tr><tr><td>Digital Camera 1 (D1)Cellular Phone (D3)MP3 Player (D4)DVD Player (D5)Laptop (D6)Restaurant (D7)</td><td>Digital Camera 2 (D2)</td><td>Very Low-Level</td></tr><tr><td>Digital Camera 1 (D1)Digital Camera 2 (D2)MP3 Player (D4)DVD Player (D5)Laptop (D6)Restaurant (D7)</td><td>Cellular Phone (D3)</td><td>Mid-Level</td></tr><tr><td>Digital Camera 1 (D1)Digital Camera 2 (D2)Cellular Phone (D3)DVD Player (D5)Laptop (D6)Restaurant (D7)</td><td>MP3 Player (D4)</td><td>Low-Level</td></tr><tr><td>Digital Camera 1 (D1)Digital Camera 2 (D2)Cellular Phone (D3)MP3 Player (D4)Laptop (D6)Restaurant (D7)</td><td>DVD Player (D5)</td><td>Low-Level</td></tr><tr><td>Digital Camera 1 (D1)Digital Camera 2 (D2)Cellular Phone (D3)MP3 Player (D4)DVD Player (D5)Restaurant (D7)</td><td>Laptop (D6)</td><td>High-Level</td></tr><tr><td>Digital Camera 1 (D1)Digital Camera 2 (D2)Cellular Phone (D3)MP3 Player (D4)DVD Player (D5)Laptop (D6)</td><td>Restaurant (D7)</td><td>High-Level</td></tr></table>

$$
F 1 = 2 \times \frac {P r e c i s i o n \times R e c a l l}{P r e c i s i o n + R e c a l l}\tag{9}
$$

$$
P r e c i s i o n = \frac {T P}{T P + F P},\tag{10}
$$

$$
R e c a l l = \frac {T P}{T P + F N},\tag{11}
$$

## 4.4. Results and Discussion

Table 5 presents the experimental results (F1-Measure) of the aspects extraction process. We highlighted the best algorithm for each dataset with a bold text in cells. Below we discuss the experimental results according to the level of inconsistency of the cross-domain process.

Table 5: F1-Measure results of the aspect extraction process for each approach.

<table><tr><td>Target Domain</td><td>CD-ALPHN</td><td>J48</td><td>kNN</td><td>MLP</td><td>NB</td><td>SVM</td></tr><tr><td>D1</td><td>0.560</td><td>0.554</td><td>0.550</td><td>0.570</td><td>0.559</td><td>0.566</td></tr><tr><td>D2</td><td>0.579</td><td>0.579</td><td>0.572</td><td>0.581</td><td>0.572</td><td>0.574</td></tr><tr><td>D3</td><td>0.600</td><td>0.585</td><td>0.589</td><td>0.598</td><td>0.591</td><td>0.598</td></tr><tr><td>D4</td><td>0.589</td><td>0.583</td><td>0.581</td><td>0.587</td><td>0.585</td><td>0.595</td></tr><tr><td>D5</td><td>0.570</td><td>0.573</td><td>0.578</td><td>0.581</td><td>0.565</td><td>0.583</td></tr><tr><td>D6</td><td>0.610</td><td>0.480</td><td>0.547</td><td>0.581</td><td>0.570</td><td>0.504</td></tr><tr><td>D7</td><td>0.683</td><td>0.543</td><td>0.583</td><td>0.668</td><td>0.649</td><td>0.569</td></tr></table>

Very Low-Level: Datasets D1 (Digital Camera 1) and D2 (Digital Camera 2) contain almost the same aspects. Thus, a cross-domain process based on two stages was suficient for the transfer learning process, since there are similar feature space and probability distribution. Neural Network (MLP) classifier obtained the best results.

Low-Level: Datasets D4 (MP3 Player) and D5 (DVD Player) contain many shared aspects, due to the similar functions of these two products. In the same way as described above (very low-level), a two-stage cross-domain process was suficient for the transfer learning process. Support Vector Machine (SVM) classifier obtained the best results.

Mid-Level: Dataset D3 (Cellular Phone) shares some aspects with the D1 (Digital Camera 1), D2 (Digital Camera 2), and D4 (MP3 Player) datasets. However, the target domain contains a significant amount of new aspects. In this scenario, the transductive learning process proposed in our CD-ALPHN algorithm obtains competitive results and obtained the best aspect extraction performance. The results are similar to traditional twostage approaches, especially when compared with MLP and SVM classifiers.

High-Level: Datasets D6 (Laptop) and D7 (Restaurant) represent scenarios in which there is a large set of new aspects in the target domain. In this case, traditional approaches based on two stages yield inferior performance compared to our CD-ALPHN. These experimental results are a strong evidence of the importance of a unified representation model based on heterogeneous networks for cross-domain transfer learning.

In summary, the use of transductive learning from a unified representation based on heterogeneous networks yields promising results for cross-domain transfer learning, outperforming MLP and SVM methods in scenarios where there is a high-level of inconsistency between the source and target domains — the most common scenario in real-world applications. Moreover, we emphasize that our proposed CD-ALPHN approach is competitive even when there is a low-level of inconsistency, being an interesting alternative to be used in diferent scenarios.

The CD-ALPHN approach is also advantageous in terms of computational time<sup>1</sup>. Table 6 shows the average execution time of each approach considering all datasets. Note that our CD-ALPHN approach is computationally fast for aspect extraction tasks, even when compared to simpler approaches such as Naive Bayes (NB). Transductive approaches have the advantage that it is not necessary to perform a previous stage of model building (training step), since it uses both the labeled and unlabeled data in an iterative label propagation process; which already returns the set of classified aspects.

## 4.5. Example of Application

To complement the experimental analysis based on benchmark datasets, we discuss the practical use of the CD-ALPHN approach integrated into a decision support system. Thus, we developed a data analytics system for aspectbased sentiment analysis called “Websensors-SentimentAnalysis” (Websensors for Aspect-based Sentiment Analysis), which uses the concept of “information as a sensor” (Marcacini et al., 2017). Websensors are proposed as an instance of the Web Science research area, with the diferential of exploring data science techniques and analytical intelligence to explore the relationship between the digital world and our physical world (Phethean et al., 2016). Websensors have been used successfully in real-world applications such as time series forecasting (Marcacini et al., 2016) and urban violence events (Florence et al., 2017). In this paper, we argue that sentiment analysis is a promising application to explore relationships between the virtual world (text reviews) and the real world (products and consumers) concept also investigated by authors who study human behavior in online ecommerce systems to support decision making (Zhang &

Table 6: Average execution time in seconds of each cross-domain aspect extraction approach considering all datasets.

<table><tr><td>Method</td><td>Model Building Time</td><td>Classification Time</td><td>Total</td></tr><tr><td>CD-ALPHN</td><td>—</td><td>2.26</td><td>2.26</td></tr><tr><td>NB</td><td>3.38</td><td>0.70</td><td>4.07</td></tr><tr><td>J48</td><td>78.81</td><td>0.01</td><td>78.82</td></tr><tr><td>kNN</td><td>—</td><td>373.47</td><td>373.56</td></tr><tr><td>MLP</td><td>25146.29</td><td>0.17</td><td>25146.46</td></tr><tr><td>SVM</td><td>25753.12</td><td>94.46</td><td>25847.58</td></tr></table>

Benyoucef, 2016). In this case, in addition to the text reviews, geographic information (e.g., consumer location) and time information (e.g., date of publication) are also collected to improve the information sensor.

Figure 5 illustrates one of the main interface of the Websensors-Sentiment-Analysis from 93 real reviews (written in Portuguese) about a Brazilian restaurant (source domain), where the aspect extraction are performed using our CDtially, we summarize all aspects according to the positive and negative polarities (Figure 5A), thereby providing an overview of the product or service. When the user selects a polarity of interest (Positive or Negative), the Websensors-SentimentAnalysis system presents: the text reviews with the highlighted aspects (Figure 5B), a temporal evolution of the polarity according to the frequency of positive or negative aspects over time (Figure 5C), and a geographical mapping according to the locality of the consumers that submitted the reviews (Figure 5D).

![](/api/attachments/YWZVTDN2/fulltext/images/57e0864d5447b8790b646f7cfa57dd5f44139f1366653cce78ad65a3d4f5b975.jpg)  
Figure 5: Overview of the Websensors-SentimentAnalysis (Data Analytics) system interface for aspect-based sentiment analysis.

Note that in Figure 5B we highlighted the aspects according to the matrix F(A<sup>T</sup> ) obtained by using the CD-ALPHN approach. The user can select the extracted aspects and then get an overview on which text reviews this aspect was classified as positive or negative. Thus, by selecting an aspect of interest and its polarity, we can combine the selected aspect with geographic information to build a heat map as shown in Figure 6, thereby presenting the geographical occurrence of an aspect according to the location of the consumers.

![](/api/attachments/YWZVTDN2/fulltext/images/7dc6240d5e8127bc0190afc3d4d858681531ad4af0c97eea20f3f14fca7b9541.jpg)  
Figure 6: Example of a heat map that represents the geographical occurrence of a selected aspect according to the location of the consumers.

Once the aspects are extracted, several other functionalities of a data analytics system can be implemented, such as notification of the occurrence of a new aspect, reports of the top-k aspects most commented in the reviews, and alerts with the aspects that need attention (increase of negative polarity). We believe that these functionalities can be used as guidelines for the development of new decision support systems for aspect-based sentiment analysis. Moreover, it is a promising example of how ABSA-based decision support systems can be constructed more quickly and easily if we use aspects already labeled in other domains combined with transductive learning methods.

## 5. Concluding Remarks

We present a new approach for aspect extraction of a given domain using aspects labeled from other diferent domains. Our approach innovates from existing solutions (1) by providing an unified representation of feature spaces between diferent domains through heterogeneous networks, and (2) by using a cross-domain transfer learning process through label propagation with transductive learning.

Experimental results validate the efectiveness (F1-Measure measure) and eficiency (computational time) of our approach. Our proposed CD-ALPHN (Cross-Domain Aspect Label Propagation through Heterogeneous Networks) was compared to the state-of-the-art approaches for cross-domain tasks and obtained competitive results considering all scenarios. Moreover, CD-ALPHN is potentially useful in scenarios where there is a high-level of inconsistency between the source and target domains, outperforming the state-of-the-art MLP (Multilayer Perceptron Neural Network) and SVM (Support Vector Machine) approaches. In fact, real-world applications often present high-level of inconsistency, since reviews are collected from diferent data sources and diferent writing styles. In addition to the experimental evaluation with benchmark datasets, we discussed how the proposed approach can be employed in decision support systems. Specifically, we present a data analytics system for aspect-based sentiment analysis (Websensors-SentimentAnalysis).

Directions for future work involve the enrichment of the model representation based on heterogeneous networks. We plan to include the sentiment polarity allowing the aspect extraction as well as the classification of the polarity of the aspects using labeled data from diferent domains. In fact, this is a challenging research direction that we believe will be a trend in the sentiment analysis field and will require advancements both in unified text representation models (e.g. statistical and linguistic features) and efective transductive learning methods for label propagation.

All the datasets used in this work, as well as the source code of our CD-ALPHN approach, are available at http://websensors.net.br/absa/.

## Acknowledgment

The authors acknowledge the Brazilian Research Agencies FUNDECT-MS [grant number 147/2016 - SIAFEM 25907], FINEP, CNPq, CAPES, and FAPESP [grant number 2014/08996-0 and 2017/08804-2] for their support to this work. The authors also thank the NVIDIA for donating computer equipment (GPU Grant Academic Program).

## References

Akhtar, M. S., Gupta, D., Ekbal, A., & Bhattacharyya, P. (2017). Feature selection and ensemble construction: A two-step method for aspect based sentiment analysis. Knowledge-Based Systems, 125 , 116–135.

Al-Moslmi, T., Omar, N., Abdullah, S., & Albared, M. (2017). Approaches to cross-domain sentiment analysis: A systematic literature review. IEEE

Belkin, M., Niyogi, P., & Sindhwani, V. (2006). Manifold regularization: A geometric framework for learning from labeled and unlabeled examples. Journal of Machine Learning Research, 7 , 2399–2434.

Breck, E., & Cardie, C. (2017). Opinion mining and sentiment analysis. In The Oxford Handbook of Computational Linguistics. (2nd ed.).

Breve, F. A., Zhao, L., Quiles, M. G., Pedrycz, W., & Liu, J. (2012). Particle competition and cooperation in networks for semi-supervised learning. IEEE Transasctions on Knowledge and Data Engineering, 24 , 1686–1698.

Cambria, E. (2016). Afective computing and sentiment analysis. IEEE Intelligent Systems, 31 , 102–107.

Chang, W.-C., Wu, Y., Liu, H., & Yang, Y. (2017). Cross-domain kernel induction for transfer learning. In Proceedings of the Thirty-First AAAI Conference on Artificial Intelligence (AAAI-17) (pp. 1763–1769).

Chapelle, O., Schölkopf, B., & Zien, A. (Eds.) (2006). Semi-Supervised Learning. MIT Press.

Chen, Z., Mukherjee, A., & Liu, B. (2014). Aspect extraction with automated prior knowledge learning. In Proceedings of the 52nd annual meeting of the Association for Computational Linguistics (pp. 347–358).

Deng, S., Sinha, A. P., & Zhao, H. (2017). Adapting sentiment lexicons to domain-specific social media texts. Decision Support Systems, 94 , 65–76.

Duric, A., & Song, F. (2012). Feature selection for sentiment analysis based on content and syntax models. Decision support systems, 53 , 704–711.

Feldman, R. (2013). Techniques and applications for sentiment analysis. Communications of the ACM , 56 , 82–89.

Florence, R., Nogueira, B., & Marcacini, R. (2017). Constrained hierarchical clustering for news events. In Proceedings of the 21st International Database Engineering & Applications Symposium (pp. 49–56). ACM.

Gupta, M., Kumar, P., & Bhasker, B. (2015). A new relevance measure for heterogeneous networks. In International Conference on Big Data Analytics and Knowledge Discovery (pp. 165–177). Springer.

Hu, M., & Liu, B. (2004). Mining and summarizing customer reviews. In Proceedings of the 10th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD-2004) (pp. 168–177).

Joachims, T. (1999). Transductive inference for text classification using support vector machines. In Proceedings of the 16th International Conference on Machine Learning (ICML-99) (pp. 200–209).

Joachims, T. (2003). Transductive learning via spectral graph partitioning. In Proceedings of the 20th International Conference on Machine Learning (ICML-03) (pp. 290–297).

Kong, X., Ng, M. K., & Zhou, Z.-H. (2013). Transductive multilabel learning via label set propagation. IEEE Transactions on Knowledge and Data Engineering, 25 , 704–719.

Lau, R. Y., Li, C., & Liao, S. S. (2014). Social analytics: learning fuzzy product ontologies for aspect-oriented sentiment analysis. Decision Support Systems, 65 , 80–94.

Li, S., Xue, Y., Wang, Z., & Zhou, G. (2013). Active learning for cross-domain sentiment classification. In Proceedings of the 23rd International Joint Conference on Artificial Intelligence (IJCAI) (pp. 2127–2133).

Liu, B. (2012). Sentiment analysis and opinion mining. Synthesis lectures on human language technologies, 5 , 1–167.

Liu, B., & Zhang, L. (2012). A survey of opinion mining and sentiment analysis. In Mining text data (pp. 415–463). Springer.

Long, M., Wang, J., Ding, G., Pan, S. J., & Philip, S. Y. (2014a). Adaptation regularization: A general framework for transfer learning. IEEE Transactions on Knowledge and Data Engineering, 26 , 1076–1089.

Long, M., Wang, J., Ding, G., Shen, D., & Yang, Q. (2014b). Transfer learning with graph co-regularization. IEEE Transactions on Knowledge and Data Engineering, 26 , 1805–1818.

Long, M., Wang, J., Sun, J., & Philip, S. Y. (2015). Domain invariant transfer kernel learning. IEEE Transactions on Knowledge and Data Engineering, 27 , 1519–1532.

Lu, J., Behbood, V., Hao, P., Zuo, H., Xue, S., & Zhang, G. (2015). Transfer learning using computational intelligence: a survey. Knowledge-Based Systems, 80 , 14–23.

Luo, P., Zhuang, F., Xiong, H., Xiong, Y., & He, Q. (2008). Transfer learning from multiple source domains via consensus regularization. In Proceedings of the 17th ACM conference on Information and knowledge management (pp. 103–112). ACM.

Manning, C., Surdeanu, M., Bauer, J., Finkel, J., Bethard, S., & McClosky, D. (2014). The Stanford CoreNLP natural language processing toolkit. In Proceedings of 52nd annual meeting of the association for computational linguistics: system demonstrations (pp. 55–60).

Marcacini, R. M., Carnevali, J. C., & Domingos, J. (2016). On combining websensors and dtw distance for knn time series forecasting. In Pattern Recognition (ICPR), 2016 23rd International Conference on (pp. 2521–2525). IEEE.

Marcacini, R. M., Rossi, R. G., Nogueira, B. M., Martins, L. V., Cherman, E. A., & Rezende, S. O. (2017). Websensors analytics: Learning to sense the real world using web news events. In Proceedings of 23th Brazilian Symposium on Multimedia and the Web. Workshop on tools and applications. (pp. 169–173).

Matsuno, I. P., Rossi, R. G., Marcacini, R. M., & Rezende, S. O. (2017). Aspectbased sentiment analysis using semi-supervised learning in bipartite heterogeneous networks. Journal of Information and Data Management, 7 , 141–154.

Mukherjee, A., & Liu, B. (2012). Aspect extraction through semi-supervised modeling. In Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics: Long Papers-Volume 1 (pp. 339–348). Association for Computational Linguistics.

Pan, S. J., & Yang, Q. (2010). A survey on transfer learning. IEEE Transactions on knowledge and data engineering, 22 , 1345–1359.

Phethean, C., Simperl, E., Tiropanis, T., Tinati, R., & Hall, W. (2016). The role of data science in web science. IEEE Intelligent Systems, 31 , 102–107.

Pontiki, M., Galanis, D., Pavlopoulos, J., Papageorgiou, H., Androutsopoulos, I., & Manandhar, S. (2014). Semeval-2014 task 4: Aspect based sentiment

analysis. In Proceedings of the 8th International Workshop on Semantic Evaluation (SemEval- 2014) (pp. 27–35).

Rana, T. A., & Cheah, Y.-N. (2016). Aspect extraction in sentiment analysis: comparative analysis and survey. Artificial Intelligence Review , 46 , 459–483.

Rana, T. A., & Cheah, Y.-N. (2017). A two-fold rule-based model for aspect extraction. Expert Systems with Applications, 89 , 273–285.

Rohrbach, M., Ebert, S., & Schiele, B. (2013). Transfer learning in a transductive setting. In Proceedings of Advances in Neural Information Processing Systems (NIPS) (pp. 46–54).

Rossi, R. G., Lopes, A. A., & Rezende, S. O. (2014). A parameter-free label propagation algorithm using bipartite heterogeneous networks for text classification. In Proceedings of the Symposium on Applied Computing (pp. 79–84). ACM.

Rossi, R. G., Lopes, A. d. A., & Rezende, S. O. (2016). Optimization and label propagation in bipartite heterogeneous networks to improve transductive classification of texts. Information Processing & Management, 52 , 217–257.

Ryan, P. B. K. J., & Michailidis, M. V. C. G. (2017). Graph-based semisupervised learning with big data. Handbook of Research on Applied Cybernetics and Systems Science, (p. 154).

Schouten, K., & Frasincar, F. (2016). Survey on aspect-level sentiment analysis. IEEE Transactions on Knowledge and Data Engineering, 28 , 813–830.

Subramanya, A., & Bilmes, J. (2008). Soft-supervised learning for text classi-Language Processing (pp. 1090–1099). Association for Computational Linguistics.

Wang, T., Cai, Y., Leung, H.-f., Lau, R. Y., Li, Q., & Min, H. (2014). Product aspect extraction supervised with online domain knowledge. Knowledge-Based Systems, 71 , 86–100.

Wu, F., Huang, Y., & Yan, J. (2017). Active sentiment domain adaptation. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (pp. 1701–1711). volume 1.

Wu, Q., & Tan, S. (2011). A two-stage framework for cross-domain sentiment classification. Expert Systems with Applications, 38 , 14269–14275.

Zhang, K. Z., & Benyoucef, M. (2016). Consumer behavior in social commerce: A literature review. Decision Support Systems, 86 , 95 – 108.

Zhang, P., Wang, J., Wang, Y., & Wang, Y. (2016). A statistical approach to opinion target extraction using domain relevance. In Proceedings of the 2nd IEEE International Conference on Computer and Communications (ICCC) (pp. 273–277). IEEE.

Zhou, D., Bousquet, O., Lal, T. N., Weston, J., & Schölkopf, B. (2004). Learning

Zhu, X., Ghahramani, Z., & Laferty, J. D. (2003). Semi-supervised learning using gaussian fields and harmonic functions. In Proceedings of the 20th International conference on Machine learning (ICML-03) (pp. 912–919).

Zhu, X., & Goldberg, A. B. (2009). Introduction to Semi-Supervised Learning. Morgan and Claypool Publishers.

Zhuang, F., Luo, P., Xiong, H., Xiong, Y., He, Q., & Shi, Z. (2010). Crossdomain learning from multiple sources: A consensus regularization perspective. IEEE Transactions on Knowledge and Data Engineering, 22 , 1664–1678.

## Biography

Ricardo Marcondes Marcacini is an associate professor of Information Systems at the Federal University of Mato Grosso do Sul, Brazil. He has a PhD in Computer Science from Institute of Mathematics and Computer Science at the University of São Paulo, Brazil. His research interests include machine learning, data clustering and data analytics systems. He has published papers in a number of international journals and conferences, such as Pattern Recognition Letters, Journal of Information and Data Management, International Conference on World Wide Web, Web Intelligence Conference, and ACM Symposium on Document Engineering.

Ivone Penque Matsuno is a doctoral candidate at the Institute of Mathematics and Computer Science at the University of São Paulo, Brazil. Her research interests include sentiment analysis and opinion mining. Her research has appeared in the Journal of Information and Data Management, and in conference proceedings, such as Brazilian Symposium on Multimedia and the Web and International Conference on Engineering Design.

Rafael Geraldeli Rossi is an associate professor of Information Systems at the Federal University of Mato Grosso do Sul, Brazil. He has a PhD in Computer Science from Institute of Mathematics and Computer Science at the University of São Paulo, Brazil. His research interests include machine learning, text classification and network models for data representation. He has published papers in a number of international journals and conferences, such as Knowledge-Based Systems, Pattern Recognition Letters, Intelligent Data Analysis, Information Processing & Management, International Conference on Data Mining, and Annual ACM Symposium on Applied Computing.

Solange Oliveira Rezende is a full professor of Computer Science at the University of São Paulo, Brazil. She has a PhD in Mechanical Engineering from University of São Paulo and a postdoctoral degree in Computer Science at the University of Minnesota, USA. Her research interests include data and text mining, machine learning, and recommendation systems. She has published papers in a number of international journals, such as Pattern Recognition Letters, Journal of Information and Data Management, Knowledge-Based Systems, Intelligent Data Analysis, Information Retrieval Journal, and Information Processing & Management.

## Highlights

• We show that transductive learning is promising for cross-domain aspect extraction.

• A heterogeneous network model to fuse knowledge for cross-domain transfer learning.

• Aspect label propagation using linguistic features as a bridge between domains.

• Experimental results validate the effectiveness and efficiency of our approach.

![](/api/attachments/YWZVTDN2/fulltext/images/46b79ee27c4e6cfd1d332b05e18e024112587f91fe1a92a486eb48ee9ed64efc.jpg)  
Figure 1

![](/api/attachments/YWZVTDN2/fulltext/images/45abde5f283d99cbdb945a19f4b005fb686b79f6d20f09eaf7b52d97a138eda1.jpg)  
Figure 2

![](/api/attachments/YWZVTDN2/fulltext/images/778912edae3f7206cf470f8165a138f56ebd58ea08b3bf24a5eca7dbc7e1e24a.jpg)  
Figure 3

![](/api/attachments/YWZVTDN2/fulltext/images/4091f687bb22c4f85f543f9dcd855bc441192cfe24c2acebad65da7f9fedc539.jpg)  
Figure 4

<table><tr><td colspan="4">ASBA - RESTAURANTS - BRAZIL</td></tr><tr><td>#</td><td>Websensor</td><td>Signal</td><td>Action</td></tr><tr><td>1</td><td>All Reviews</td><td>0.00</td><td></td></tr><tr><td>2</td><td>Positive</td><td>0.75</td><td></td></tr><tr><td>3</td><td>Negative</td><td>0.25</td><td></td></tr></table>

![](/api/attachments/YWZVTDN2/fulltext/images/dd330f557d78884a5a85630476e1ebe42bed8fe1d775f324df56f3ffb80b6281.jpg)

![](/api/attachments/YWZVTDN2/fulltext/images/be97acfdc316d82189cd10766cdde168e439480a0c9ee79e4e019c6015fea835.jpg)  
Figure 5

![](/api/attachments/YWZVTDN2/fulltext/images/91a699352a5d2c8e37c4a78c2ea88cfa7691508e9d68685f2d5e000e3a8653c0.jpg)  
Figure 6
